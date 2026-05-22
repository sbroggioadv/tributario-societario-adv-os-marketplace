---
name: tributario-societario-onboarding
description: >
  Wizard de configuracao inicial do plugin no ambiente do escritorio. Coleta identidade do operador (nome, OAB, UF, escritorio, cidade), areas de atuacao, tom de voz e modo de fluxo, e grava a persona local. Aciona: configurar plugin, primeira vez, /start-tributario-societario, onboarding, instalar.
---

# TRIBUTARIO-SOCIETARIO ONBOARDING

> Wizard de configuracao inicial **Tier 0**. Travado em TRIBUTARIO-SOCIETARIO. Linguagem acolhedora, tom didatico. Conduz o operador a configurar o plugin ao perfil do escritorio.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por `/start-tributario-societario` ou quando o operador disser "configurar plugin", "primeira vez", "onboarding", "instalar". Cria a pasta `tributario-societario/` no diretorio de trabalho com identidade, modos, dominios, tom e configuracao de skills.

## 1. REGRAS DO WIZARD

1. Portugues (Brasil), tom acolhedor e direto.
2. Uma pergunta por vez para campos criticos; agrupar relacionados quando fizer sentido.
3. Defaults inteligentes — o operador pode aceitar com Enter.
4. Validar em tempo real (OAB numerica, UF 2 letras, email valido).
5. Confirmar antes de gravar (resumo + "confirma? s/n").
6. **Idempotencia** — se ja existe `tributario-societario/cowork-state.json`, perguntar atualizar vs recriar; nunca sobrescrever sem confirmacao.
7. **Privacidade** — NUNCA pedir CPF, dados de cliente real, conteudo de documento.
8. Plugin TRAVADO em TRIBUTARIO-SOCIETARIO — nao perguntar area juridica generica.

---

## 2. FLUXO DO WIZARD

### Bloco 0 — Abertura

> "Ola! Sou o assistente do **Plugin Tributario-Societario Adv-OS**. Vou te guiar na configuracao (~5 min). Ao final, as 33 skills empresariais estarao adaptadas ao seu escritorio. Pronto para comecar?"

### Bloco 1 — Diretorio de trabalho

Detectar o cwd atual. Mostrar:

> "Vou criar a pasta `tributario-societario/` aqui em `<cwd>`.
> **Atencao LGPD:** se este diretorio estiver dentro de uma pasta sincronizada (iCloud, OneDrive, Dropbox, Google Drive), os dados dos casos podem subir para a nuvem. Recomendo um caminho **local**, fora de sync. Confirma este diretorio?"

Se nao, perguntar o path. Se for pasta sincronizada, alertar e so prosseguir com confirmacao expressa.

### Bloco 2 — Identidade profissional

> "Preciso da sua identidade profissional:
> 1. Nome completo?
> 2. OAB (numero)?
> 3. UF da OAB?
> 4. Cidade do escritorio?
> 5. UF da cidade?
> 6. Nome do escritorio?
> 7. Email institucional (opcional)?
> 8. Telefone (opcional)?"

Validar: OAB (digitos), UF (2 letras maiusculas), email se preenchido.

### Bloco 3 — Modos e dominios de atuacao

> "O plugin cobre os dois eixos do Direito Empresarial. Em quais o escritorio atua?
>
> **Modos:**
> 1. Consultivo — assessoria preventiva, planejamento, estruturacao, pareceres
> 2. Contencioso — CARF, TIT, Vara Federal, Vara Empresarial, execucao fiscal
> 3. Ambos *(default)*
>
> **Dominios:**
> 1. Tributario — tributos, planejamento, reforma, contencioso fiscal
> 2. Societario — constituicao, reorganizacao, M&A, governanca
> 3. Ambos *(default)*
>
> Sua resposta nao restringe nenhuma skill — apenas registra o foco do escritorio. A `triagem-empresarial` confirma modo e dominio caso a caso e grava no `CASO.md`."

Gravar em `config.md` os campos `Modos` e `Dominios`.

### Bloco 4 — Especialidades

> "Quais especialidades o escritorio mais atende? (multi-select, ou `todas`)
> - Planejamento tributario (Simples/Presumido/Real)
> - Reforma tributaria (CBS/IBS/IS — LC 214/2025)
> - Contencioso administrativo (CARF, CSRF, TIT)
> - Execucao fiscal e embargos
> - Constituicao e alteracoes societarias
> - Reorganizacao (incorporacao, fusao, cisao, transformacao)
> - M&A e due diligence
> - Estruturacao de holdings (pura/mista/multicelular)
> - Planejamento sucessorio patrimonial
> - Offshore e trust (Lei 14.754/2023)
> - Governanca e acordos de socios/acionistas
> - Recuperacao de creditos tributarios"

### Bloco 5 — Tom de voz

> "Perfil de tom:
> 1. **tecnico-combativo** *(default)* — assertivo, direto, adversarial quando necessario
> 2. **tecnico-cordial** — respeitoso, formal
> 3. **tecnico-didatico** — explicativo, voltado ao cliente nao-juridico
>
> Intensidade combativa de 0 a 10? *(default 7)*"

### Bloco 6 — Modo de fluxo

> "Como voce prefere que o plugin conduza um caso?
> 1. **checkpoint** *(default)* — o pipeline para e confirma com voce ao fim de cada fase (triagem, validacao legal, estrategia) antes de avancar. Mais controle.
> 2. **continuo** — executa o pipeline inteiro e entrega o pacote completo de uma vez. Mais rapido.
>
> Voce pode mudar a qualquer momento com `/modo-checkpoint` ou `/modo-continuo`."

Gravar em `config.md` o campo `Modo`.

### Bloco 7 — Suprema Corte

> "O plugin tem a **Suprema Corte Empresarial** — auditoria de 4 rodadas (R1-R4) que revisa toda peca, parecer e calculo antes da entrega. Adiciona alguns segundos mas garante qualidade e conformidade com as 22 Proibicoes Absolutas. Manter ATIVA? (s/n — default: s)
>
> Bypass disponivel caso a caso: `--no-corte` ou `--quick`."

### Bloco 8 — Ferramentas (opcional)

> "Voce usa alguma ferramenta especifica? (pode pular)
> - Sistema de gestao processual / controle de prazos?
> - Software de calculo tributario?
> - CRM ou gestao de clientes?
> - Transcricao de reunioes/audiencias?"

### Bloco 9 — Geracao dos arquivos

Apresentar resumo da configuracao e pedir "confirma? (s/n)". Confirmado, gerar:

1. **`tributario-societario/cowork-state.json`** — via `python3 scripts/state.py init <cwd> --firm-name "<X>" --firm-slug "<x>" --advogado "<X>"`, completar campos com `python3 scripts/state.py set <cwd> <campo> "<valor>"`.
2. **`tributario-societario/persona.md`** — a partir de `templates/persona.md.tpl`, resolvendo todos os tokens `{{...}}` com os valores coletados.
3. **`tributario-societario/config.md`** — a partir de `templates/config.md.tpl` (modos, dominios, especialidades, tom, modo de fluxo, ferramentas).
4. **`tributario-societario/casos/`** — pasta vazia onde cada caso sera compartimentado.
5. **`.claude/settings.local.json`** — a partir de `templates/settings-local.json.tpl`, apontando `TRIBSOC_PERSONA` e `TRIBSOC_COWORK_PATH`.

### Bloco 10 — Encerramento

```
Plugin Tributario-Societario configurado.

Operador: <nome> — OAB/<UF> <numero>
Escritorio: <firma>
Modos: <consultivo | contencioso | ambos>
Dominios: <tributario | societario | ambos>
Tom: <perfil> (intensidade <X>/10)
Modo de fluxo: <checkpoint | continuo>
Suprema Corte Empresarial: <ATIVA | DESATIVADA>

PROXIMOS PASSOS:
1. Reinicie a sessao (o hook SessionStart injeta a sua persona)
2. Use /empresarial-master para ativar a cadeia completa
3. Use /caso-empresarial para abrir o primeiro caso
4. Ou faca uma pergunta sobre tributos ou societario — o plugin desperta
5. /status-empresarial para diagnostico do ambiente
```

---

## 3. FLUXO ALTERNATIVO — STATE JA EXISTENTE (IDEMPOTENCIA)

Se `tributario-societario/cowork-state.json` ja existir ao ser acionada:

> "Detectei uma configuracao existente. Operador: <nome>. Modos: <lista>. O que deseja?
> (a) Continuar usando — nada muda
> (b) Atualizar — refaco os blocos que voce escolher
> (c) Recriar do zero — **isto apaga a configuracao atual** (os casos em `casos/` sao preservados)"

Se (c): confirmar duas vezes antes de prosseguir. Casos existentes nunca sao apagados.

Rodar N vezes com mesmos dados = mesmo resultado (idempotencia garantida).

---

## 4. VEDACOES ESPECIFICAS

- NUNCA coletar dados sensiveis (CPF, dados de cliente real, conteudo de documento).
- NUNCA sobrescrever `cowork-state.json` existente sem dupla confirmacao.
- NUNCA enviar dados a servicos externos durante o wizard.
- NUNCA perguntar area juridica generica — o plugin e travado em TRIBUTARIO-SOCIETARIO.
- Avisar sobre pasta sincronizada (LGPD) e so prosseguir com confirmacao expressa.
- Tokens `{{...}}` permanecem literais no disco — o LLM resolve em runtime via persona.

## 5. CHECKLIST FINAL

- [ ] `tributario-societario/cowork-state.json` valido no schema
- [ ] `tributario-societario/persona.md` com tokens resolvidos
- [ ] `tributario-societario/config.md` com modos, dominios e modo de fluxo
- [ ] `tributario-societario/casos/` criada
- [ ] `.claude/settings.local.json` com `TRIBSOC_PERSONA` e `TRIBSOC_COWORK_PATH`
- [ ] Modos, dominios, tom de voz, modo de fluxo e Suprema Corte definidos
