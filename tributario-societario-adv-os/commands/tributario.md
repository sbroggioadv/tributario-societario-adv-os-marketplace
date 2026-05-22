---
description: Roteia para as skills tributarias consultivas (Tier 4) — planejamento tributario, reforma tributaria, recuperacao de creditos, parecer fiscal e mitigacao de risco fiscal.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [demanda tributaria consultiva — ex: comparar regimes, recuperar PIS/COFINS, parecer]
---

Voce foi acionado pelo comando `/tributario` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** rotear a demanda tributaria consultiva para a skill Tier 4 adequada.

## PROTOCOLO

1. **Verificar** se o `CASO.md` esta criado. Se nao, acionar `triagem-empresarial` primeiro.
2. **Verificar** se o Selo de Validacao Legal foi emitido. Se nao, acionar `analisador-legislacao-vigente` antes de prosseguir (PA-01). Atentar para a reforma tributaria: CBS/IBS em coexistencia por ano do fato gerador (PA-06).
3. **Identificar** a demanda e rotear:

| Demanda | Skill |
|---------|-------|
| Comparar Simples/Presumido/Real, modelagem de cenarios | `planejamento-tributario` |
| CBS/IBS, coexistencia de regimes, LC 214/2025 | `reforma-tributaria-transicao` |
| Creditos recuperaveis, compensacao, PER/DCOMP | `recuperacao-de-creditos` |
| Parecer tributario, consulta fiscal formal | `parecer-e-consulta-fiscal` |
| Elisao vs evasao, proposito negocial, substancia, malha fina/CRS | `mitigacao-de-risco-fiscal` |

4. **Nunca** propor planejamento sem o Protocolo 2 (Mitigacao de Risco Fiscal) — elisao deve ter proposito negocial real e substancia economica (PA-19).
5. Ao concluir, acionar `suprema-corte-empresarial` (R1-R4) antes de entregar qualquer parecer ou analise.

**Skills do Tier 4:** `planejamento-tributario`, `reforma-tributaria-transicao`, `recuperacao-de-creditos`, `parecer-e-consulta-fiscal`, `mitigacao-de-risco-fiscal`.
