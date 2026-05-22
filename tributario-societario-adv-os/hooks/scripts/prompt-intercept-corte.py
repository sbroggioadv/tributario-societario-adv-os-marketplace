#!/usr/bin/env python3
"""
Hook UserPromptSubmit do plugin Tributário-Societário-Adv-OS.

Logica (ativacao automatica por contexto):
1. Le o prompt via stdin (JSON padrao Claude Code hooks).
2. Detecta bypass explicito: flags `--no-corte`, `--quick`, `--no-suprema`, `/corte off`.
3. Detecta GATILHO TRIBUTARIO-SOCIETARIO via keywords (3 niveis):
   - Gatilho 1: prompt contem palavras do dominio tributario/societario
   - Gatilho 2: keywords fortes do dominio (CARF, SPED, holding, LTDA, reforma tributaria,
     CBS, IBS, IRPJ, CSLL, ITCMD, execucao fiscal, auto de infracao, etc.)
   - Gatilho 3: comandos `/start-tributario-societario`, `/empresarial-master`, etc.
4. Se gatilho dispara:
   - Verifica se `tributario-societario/cowork-state.json` existe no path atual
   - SIM: injeta protocolo R1-R4 + aponta para skill `tributario-societario-master`
   - NAO: sugere `/start-tributario-societario` ao usuario (mas nao bloqueia)
5. Se ha bypass: reafirma em stdout que o bypass foi aceito (transparencia).
6. Se nao eh tarefa tributaria/societaria nem juridica geral: silencio (exit 0 sem output).

Tambem respeita state.json: se `suprema_corte.enabled = false`, nunca injeta R1-R4.

Stdlib only.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import importlib.util
spec = importlib.util.spec_from_file_location("hook_utils", PLUGIN_ROOT / "scripts" / "hook-utils.py")
hook_utils = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook_utils)


# Gatilho 1: palavras do dominio tributario-societario (case insensitive)
TRIGGER_TRIBUTARIO = [
    r"\btributario\b",
    r"\btributária\b",
    r"\btributários\b",
    r"\btributárias\b",
    r"\bsocietario\b",
    r"\bsocietária\b",
    r"\bempresarial\b",
    r"\bdireito\s+tributario\b",
    r"\bdireito\s+tributário\b",
    r"\bdireito\s+empresarial\b",
    r"\bdireito\s+societario\b",
]

# Gatilho 2: keywords fortes do dominio tributario-societario brasileiro
DOMAIN_KEYWORDS = [
    # Orgaos e instancias tributarias
    r"\bCARF\b", r"\bTIT\b", r"\bCSRF\b", r"\bRFB\b", r"\bSEFAZ\b",
    r"\bReceita\s+Federal\b", r"\bDRFO\b",
    # Tributos e bases
    r"\bIRPJ\b", r"\bCSLL\b", r"\bPIS\b", r"\bCOFINS\b",
    r"\bICMS\b", r"\bISS\b", r"\bIPI\b", r"\bIOF\b",
    r"\bITCMD\b", r"\bITBI\b",
    r"\bCBS\b", r"\bIBS\b",
    # Reforma tributaria
    r"\breforma\s+tributaria\b", r"\breforma\s+tributária\b",
    r"\bLC\s+214\b", r"\bLC214\b",
    # Obrigacoes acessorias e sistemas
    r"\bSPED\b", r"\bECF\b", r"\bEFD\b", r"\bDCTF\b",
    r"\bPER/DCOMP\b", r"\bPER\.DCOMP\b",
    r"\bauto\s+de\s+infracao\b", r"\bauto\s+de\s+infração\b",
    r"\bCDA\b",
    # Contencioso tributario
    r"\bexecucao\s+fiscal\b", r"\bexecução\s+fiscal\b",
    r"\bembargos\s+a\s+execucao\s+fiscal\b", r"\bembargos\s+à\s+execução\s+fiscal\b",
    r"\bexcecao\s+de\s+pre-executividade\b",
    r"\bimpugnacao\s+fiscal\b", r"\bimpugnação\s+fiscal\b",
    r"\bmandado\s+de\s+seguranca\b", r"\bmandado\s+de\s+segurança\b",
    r"\brepeticao\s+de\s+indebito\b", r"\brepetição\s+de\s+indébito\b",
    # Planejamento e estruturacao
    r"\bholding\b", r"\boffshore\b", r"\btrust\b",
    r"\bplanejamento\s+tributario\b", r"\bplanejamento\s+tributário\b",
    r"\bplanejamento\s+sucessorio\b", r"\bplanejamento\s+sucessório\b",
    r"\belisao\s+fiscal\b", r"\belisão\s+fiscal\b",
    r"\bevasao\s+fiscal\b", r"\bevasão\s+fiscal\b",
    r"\bproposito\s+negocial\b", r"\bpropósito\s+negocial\b",
    # Societario
    r"\bLTDA\b", r"\bSLU\b", r"\bSAS\b",
    r"\bcontrato\s+social\b", r"\bestatuto\s+social\b",
    r"\bata\s+de\s+assembleia\b", r"\bata\s+de\s+reuniao\b",
    r"\bacordo\s+de\s+socios\b", r"\bacordo\s+de\s+acionistas\b",
    r"\bincorporacao\b", r"\bincorporação\b",
    r"\bcisao\b", r"\bcisão\b", r"\bfusao\b", r"\bfusão\b",
    r"\bJunta\s+Comercial\b",
    r"\bdue\s+diligence\b", r"\bM&A\b",
    r"\bSPA\b", r"\bMOU\b",
]

# Gatilho 3: commands prefixados do plugin
PLUGIN_COMMANDS = [
    "/start-tributario-societario",
    "/empresarial-master",
    "/caso-empresarial",
    "/legislacao",
    "/societario",
    "/holding",
    "/tributario",
    "/contencioso-fiscal",
    "/parecer",
    "/jurisprudencia",
    "/revisao-final",
    "/status-empresarial",
]

# Keywords juridicas gerais (fallback — se prompt e juridico mas nao tributario/societario,
# ainda assim aplica protocolo cauteloso de Suprema Corte Empresarial)
LEGAL_KEYWORDS_GENERAL = [
    r"\bpeticao\b", r"\bpetição\b", r"\bcontestacao\b", r"\bcontestação\b",
    r"\brecurso\b", r"\bapelacao\b", r"\bapelação\b",
    r"\bembargos\b", r"\breplica\b", r"\bréplica\b",
    r"\bparecer\b", r"\bjurisprudencia\b", r"\bjurisprudência\b",
    r"\bsentenca\b", r"\bsentença\b", r"\bdecisao\b", r"\bdecisão\b",
    r"\baudiencia\b", r"\baudiência\b", r"\bprocesso\b",
]

BYPASS_TOKENS = [
    "--no-corte",
    "--no-suprema",
    "--quick",
    "/corte off",
    "/corte-off",
]


def _load_input() -> dict:
    raw = sys.stdin.read().strip()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except Exception:
        return {}


def _matches_any(text: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False


def _is_tributario_societario(prompt: str) -> bool:
    """Detecta se o prompt e do dominio tributario-societario (gatilhos 1, 2 ou 3)."""
    if _matches_any(prompt, TRIGGER_TRIBUTARIO):
        return True
    if _matches_any(prompt, DOMAIN_KEYWORDS):
        return True
    low = prompt.lower()
    for cmd in PLUGIN_COMMANDS:
        if cmd.lower() in low:
            return True
    return False


def _is_legal_general(prompt: str) -> bool:
    """Detecta se e tarefa juridica em geral (mesmo nao sendo tributario-societario)."""
    return _matches_any(prompt, LEGAL_KEYWORDS_GENERAL)


def _has_bypass(prompt: str) -> str | None:
    low = prompt.lower()
    for token in BYPASS_TOKENS:
        if token in low:
            return token
    return None


def _has_tributario_state(cowork: Path | None) -> bool:
    """Verifica se existe `tributario-societario/cowork-state.json` no path."""
    if cowork is None:
        return False
    return (cowork / "tributario-societario" / "cowork-state.json").exists()


def _suprema_corte_enabled(cowork: Path | None) -> bool:
    """Le state.json e verifica suprema_corte.enabled. Default true se ausente."""
    if cowork is None:
        return True
    sf = cowork / "tributario-societario" / "cowork-state.json"
    if not sf.exists():
        return True
    try:
        state = json.loads(sf.read_text(encoding="utf-8"))
        return bool(state.get("suprema_corte", {}).get("enabled", True))
    except Exception:
        return True


def _resolve_cowork() -> Path | None:
    """Resolve COWORK root via env TRIBSOC_COWORK_PATH ou cwd ancestral."""
    env = os.environ.get("TRIBSOC_COWORK_PATH") or os.environ.get("COWORK_PATH")
    if env:
        p = Path(env)
        if (p / "tributario-societario" / "cowork-state.json").exists():
            return p
    return hook_utils.find_cowork(Path.cwd())


def main() -> int:
    payload = _load_input()
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not isinstance(prompt, str) or not prompt.strip():
        return 0

    cowork = _resolve_cowork()
    bypass = _has_bypass(prompt)

    is_trib = _is_tributario_societario(prompt)
    is_legal_other = _is_legal_general(prompt) and not is_trib

    # Caso 1: bypass explicito
    if bypass and (is_trib or is_legal_other):
        sys.stdout.write(
            f"[tributario-societario-adv-os] Bypass detectado ({bypass}). "
            "Pecas, pareceres e estrategias serao entregues SEM validacao "
            "da Suprema Corte Empresarial (R1-R4). Use por sua conta e risco.\n"
        )
        return 0

    # Caso 2: tarefa tributario-societario + plugin configurado
    if is_trib and _has_tributario_state(cowork):
        if not _suprema_corte_enabled(cowork):
            sys.stdout.write(
                "[tributario-societario-adv-os] Demanda tributaria/societaria detectada. "
                "Suprema Corte Empresarial DESATIVADA na configuracao. Aciono apenas a cadeia de skills.\n"
                "Acionar skill: tributario-societario-master.\n"
            )
        else:
            sys.stdout.write(
                "[tributario-societario-adv-os] Demanda tributaria/societaria detectada. Plugin ativado.\n"
                "\n"
                "PROTOCOLO AUTOMATICO:\n"
                "1. Acionar skill `tributario-societario-master` (Tier 0 — sempre ativa)\n"
                "2. Aplicar Hierarquia das 4 Camadas (1-Proibicoes, 2-Protocolos, 3-Estilo, 4-Skills)\n"
                "3. Verificar as 22 Proibicoes Absolutas (PA-01 a PA-22), com atencao especial:\n"
                "   - PA-01: Selo de Validacao Legal Previa antes de qualquer estrategia\n"
                "   - PA-02: validar vigencia/redacao da norma no ano do fato gerador (lei e alvo movel)\n"
                "   - PA-06: travar regime tributario do ano (transicao CBS/IBS 2026-2033)\n"
                "   - PA-09: todo calculo e estimativa — nunca valor final\n"
                "   - PA-10: crime tributario exige constituicao definitiva do credito (SV 24)\n"
                "   - PA-20: direito estrangeiro → sinalizar advogado local, nao opinar\n"
                "4. Acionar os 6 Protocolos da Camada 2 conforme demanda\n"
                "5. Antes de entregar: Suprema Corte Empresarial R1->R2->R3->R4\n"
                "\n"
                "Bypass disponivel: `--no-corte`, `--quick`, `/corte off`.\n"
            )
        return 0

    # Caso 3: tarefa tributario-societario mas plugin NAO configurado
    if is_trib and not _has_tributario_state(cowork):
        sys.stdout.write(
            "[tributario-societario-adv-os] Detectei demanda tributaria/societaria, mas o plugin "
            "ainda nao foi configurado neste diretorio.\n"
            "\n"
            "RECOMENDACAO: rode /start-tributario-societario para configurar (~5 min).\n"
            "Vou criar uma pasta `tributario-societario/` aqui com sua identidade, areas de "
            "atuacao, tom de voz e configuracao das skills empresariais.\n"
            "\n"
            "Caso queira prosseguir SEM configurar, trabalho em modo fallback generico "
            "(persona neutra, qualidade reduzida). Apenas avise.\n"
        )
        return 0

    # Caso 4: tarefa juridica geral (nao tributaria/societaria) — protocolo cauteloso
    if is_legal_other:
        sys.stdout.write(
            "[tributario-societario-adv-os] Tarefa juridica detectada (nao especificamente tributaria/societaria). "
            "Aplique protocolo padrao:\n"
            "1. Questionamento previo (sem suposicoes silenciosas).\n"
            "2. Apresentar estrutura + premissas antes de redigir.\n"
            "3. Aguardar confirmacao do usuario.\n"
            "4. Antes de entregar: executar Suprema Corte Empresarial R1-R4 se aplicavel.\n"
            "Bypass: `--no-corte`, `--quick`, `/corte off`.\n"
        )
        return 0

    # Caso default: nao e tarefa juridica — silencio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
