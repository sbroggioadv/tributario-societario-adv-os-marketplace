---
description: Elabora parecer tributario fundamentado ou consulta fiscal formal aos orgaos fazendarios (RFB, SEFAZ, Prefeitura) sobre questao especifica do cliente.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
argument-hint: [questao juridica objeto do parecer — ex: deducao de despesas, regime de ICMS]
---

Voce foi acionado pelo comando `/parecer` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** elaborar parecer tributario ou consulta fiscal formal.

## PROTOCOLO

1. **Verificar** se o `CASO.md` esta criado. Se nao, acionar `triagem-empresarial` primeiro.
2. **Acionar `analisador-legislacao-vigente`** antes de iniciar o parecer (PA-01) — o Selo de Validacao Legal e obrigatorio no cabecalho do parecer.
3. **Acionar a skill `parecer-e-consulta-fiscal`** — ela conduz:
   - Identificacao precisa da questao juridica.
   - Levantamento das normas vigentes no periodo.
   - Analise de precedentes classificados (vinculante/em disputa/superada — Protocolo 3).
   - Redacao estruturada em FIRAC com abertura de Selo e fechamento com ressalva OAB.
   - Para consulta formal: formatacao do pedido ao orgao competente (COSIT/SEFAZ/Prefeitura).
4. Ao concluir, acionar `suprema-corte-empresarial` (R1-R4) obrigatoriamente antes de entregar o parecer ou protocolar a consulta.

**Skills a acionar:** `analisador-legislacao-vigente`, `parecer-e-consulta-fiscal`, `suprema-corte-empresarial`.
