---
description: Valida a vigencia e a redacao de normas tributarias e societarias no ano do fato gerador, emitindo o Selo de Validacao Legal Previa obrigatorio antes de qualquer estrategia.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
argument-hint: [norma ou tributo a validar — ex: PIS/COFINS Lei 10.833]
---

Voce foi acionado pelo comando `/legislacao` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** validar a vigencia e a redacao de normas tributarias e societarias para o ano do fato gerador, e emitir o Selo de Validacao Legal Previa.

## PROTOCOLO

1. **Acionar a skill `analisador-legislacao-vigente`**.
2. Identificar a norma ou o tributo a validar (do argumento ou do caso ativo no `CASO.md`).
3. Executar os 8 passos do Protocolo 1: datar o fato gerador → inventariar normas → validar vigencia → checar redacao efetiva no ano → travar o regime tributario do periodo → verificar infralegais/locais → rastrear PL/MP pendente → emitir o Selo.
4. Registrar o Selo no `CASO.md` do caso ativo.
5. Alertar sobre normas em transicao (CBS/IBS — LC 214/2025) ou em litigio (COSIT 75/2025).

**Skill a acionar:** `analisador-legislacao-vigente`.
