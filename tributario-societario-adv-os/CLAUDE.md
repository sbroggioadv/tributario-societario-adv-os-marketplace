# CLAUDE.md — Plugin Tributário-Societário-Adv-OS

> Instrucoes para futuras sessoes neste sub-repositorio. Ler PRIMEIRO ao retomar trabalho.
> Estende o CLAUDE.md da familia de plugins Adv-OS e os niveis superiores do workspace.

---

## Identidade do Projeto

- **Nome:** Plugin Tributário-Societário-Adv-OS
- **Slug:** `tributario-societario-adv-os`
- **Tipo:** plugin Claude Code (`.claude-plugin/plugin.json`)
- **Audiencia:** advogado empresarial brasileiro — tributarista e societarista
- **Versao atual:** 0.1.0
- **Plugin de referencia (engine):** `trabalhista-adv-os` (portado em Sprint 0)
- **Repo marketplace (a criar nas FASES 2-7 do PLAYBOOK):** repo publico `tributario-societario-adv-os-marketplace`

---

## REGRA DE OURO — DESPERSONALIZACAO ABSOLUTA (PLUGIN COMERCIAL)

Este plugin sera **comercializado** (Kirvano via marketplace GitHub publico). Sem `authorship_whitelist`. **Zero mencoes** ao criador da metodologia em qualquer arquivo distribuido.

**ZERO mencoes permitidas (ver `audit/forbidden-terms.json` para lista canonica):**
- Nome do criador da metodologia (qualquer variante) e OAB pessoal
- Email/contato pessoal, escritorio-modelo, mentorias/coworks proprietarios
- Ferramentas proprietarias do escritorio de origem, padroes nomeados pessoalmente

Identidade do operador resolvida em **runtime** via persona local em `<cwd>/tributario-societario/persona.md` (fora do plugin). Tokens nas skills: `{{ADVOGADO_NOME}}`, `{{ADVOGADO_OAB}}`, `{{ADVOGADO_UF}}`, `{{FIRM_NAME}}`, `{{CIDADE}}`, `{{UF}}`, `{{TOM_VOZ_PERFIL}}`, `{{TOM_VOZ_INTENSIDADE}}`.

```bash
# Antes de CADA commit
python3 audit/audit.py
# Verificacao reforcada pre-release
python3 audit/audit.py --json | jq '.total_matches'   # esperado: 0
```

> **Excecao conhecida:** os arquivos em `.planning/` (design-spec, build-plan, deep-research) citam fontes de porte e por isso podem disparar o audit. Sao dev-only, NAO vao ao marketplace e sao excluidos do scan final do Sprint 9.

---

## Hierarquia das 4 Camadas (Constituicao Operacional)

```
CAMADA 1 — PROIBICOES ABSOLUTAS (PA-01 a PA-22)  — inviolaveis
CAMADA 2 — PROTOCOLOS TECNICOS (6)               — aplicacao obrigatoria
CAMADA 3 — IDENTIDADE TECNICA E ESTILO            — FIRAC + estrutura da peca/parecer
CAMADA 4 — SKILLS OPERACIONAIS (33, Tier 0-6)    — operacional
```

Camada superior SEMPRE prevalece — inclusive contra instrucao do usuario. Detalhamento:
- `.planning/HIERARQUIA-4-CAMADAS.md` — referencia rapida
- `.planning/PROIBICOES-ABSOLUTAS.md` — PA-01 a PA-22 detalhadas
- `.planning/PROTOCOLOS-TECNICOS.md` — os 6 protocolos
- `.planning/2026-05-21-design-spec.md` — spec integral

---

## Arquitetura em Uma Frase

Plugin empresarial especializado **mode-aware** (33 skills, Tier 0-6, consultivo + contencioso) com **engine portado** do `trabalhista-adv-os` (hooks/scripts/templates) e **governanca juridica** (4 camadas + 22 PAs + 6 Protocolos + Suprema Corte Empresarial R1-R4) injetada via skill `tributario-societario-master`. O modo (consultivo/contencioso) e o dominio (tributario/societario) sao decididos na `triagem-empresarial`, gravados no `CASO.md` e lidos por todas as skills.

---

## Mode-Awareness (decisao de arquitetura nuclear)

**Um unico plugin, orquestrador mode-aware** (abordagem A da spec). A triagem identifica o **modo** (consultivo vs contencioso) e o **dominio** (tributario, societario ou ambos). Diferente do `trabalhista-adv-os` (side-aware), aqui nao ha polo adversarial — a perspectiva e sempre do advogado que aconselha/defende o cliente empresarial.

---

## Como Retomar Trabalho

1. **Ler `MEMORY.md`** (raiz) — estado executivo, sprint ativa, proximo passo
2. **Ler `.planning/2026-05-21-build-plan.md`** — plano de sprints
3. **`git status` + `git log -8`** — estado real do repo
4. **`python3 audit/audit.py`** — verificar despersonalizacao (matches so em `.planning/` sao OK)

---

## Padroes a Seguir

1. **Skill folder = so `SKILL.md`.** Material auxiliar vai em `templates/` ou `scripts/data/`.
2. **Limites Cowork:** `SKILL.md` <= 11264 bytes; `description` do frontmatter <= 1024 chars. Validar com `scripts/check-skill-descriptions.py`.
3. **plugin.json minimal:** `name`, `version`, `description`, `author`, `license`.
4. **Tokens `{{...}}`** permanecem LITERAIS no disco — LLM resolve em runtime via persona.
5. **Privacidade LGPD:** pasta `<cwd>/tributario-societario/` (e `casos/`) gitignored por default; warning se pasta sincronizada. Compartimentacao por caso e PA-22.
6. **Portabilidade:** scripts Python 3.11+; `${CLAUDE_PLUGIN_ROOT}` em todos os hooks; `${TRIBSOC_PERSONA}` resolvido por fallback chain.
7. **Commits semanticos** por task — `feat(skill): <nome>`, `feat:`, `chore:`, `docs:`.
8. **Atualizar `MEMORY.md` ANTES de qualquer push.**

---

## Proibicoes

1. **NAO** comecar nova Sprint sem ler `MEMORY.md` e `.planning/2026-05-21-build-plan.md`.
2. **NAO** incluir identidade do criador da metodologia em arquivo distribuido (audit bloqueia).
3. **NAO** colocar `SKILL.md` acima de 11264 bytes nem `description` acima de 1024 chars.
4. **NAO** criar arquivo dentro de `skills/<nome>/` que nao seja `SKILL.md`.
5. **NAO** aceitar instrucao do usuario que conflite com a Camada 1 (PA-01 a PA-22).
6. **NAO** escrever dados de cliente no plugin nem em pasta sincronizada (Dropbox/iCloud/Drive).
7. **NAO** alterar nome/slug do plugin sem nova decisao.

---

## Estrutura do Sub-Repo

```
plugin-tributario-societario/
├── .claude-plugin/plugin.json   manifesto minimal
├── .planning/                    docs dev-only (spec, plano, camadas, PAs, protocolos)
├── commands/                     12 commands
├── skills/                       33 skills (Tier 0-6 + transversais)
├── hooks/                        hooks.json + 3 scripts
├── context/                      persona-fallback.md
├── templates/                    persona / config / CASO / MEMORY-caso / settings
├── scripts/                      resolve-persona, state, hook-utils, check-skill-descriptions
├── audit/                        forbidden-terms.json + audit.py
├── README.md / LICENSE / .gitignore / CLAUDE.md / MEMORY.md
```

---

## Comunicacao

- **Idioma:** Portugues (Brasil)
- **Tom dos docs internos:** tecnico, direto, sem mencoes pessoais
- **Tom das skills/commands (para o usuario-cliente):** acolhedor, tecnico, respeita `tom_voz` configurado em runtime
- **Reportes:** ✅ concluido / 🔴 erro / 🏁 sprint finalizada

---

**Ultima atualizacao:** 2026-05-21 (Sprint 0 — scaffold).
