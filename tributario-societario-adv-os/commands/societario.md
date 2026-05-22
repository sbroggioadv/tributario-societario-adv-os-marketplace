---
description: Roteia para as skills societarias (Tier 2) — escolha de tipo, constituicao, alteracoes, reorganizacao, dissolucao, governanca, M&A e registro empresarial.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [demanda societaria — ex: constituir LTDA, alterar contrato social, M&A]
---

Voce foi acionado pelo comando `/societario` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** rotear a demanda societaria para a skill Tier 2 adequada.

## PROTOCOLO

1. **Verificar** se o `CASO.md` esta criado. Se nao, acionar `triagem-empresarial` primeiro.
2. **Verificar** se o Selo de Validacao Legal foi emitido. Se nao, acionar `analisador-legislacao-vigente` antes de prosseguir (PA-01).
3. **Identificar** a demanda e rotear para a skill Tier 2 correspondente:

| Demanda | Skill |
|---------|-------|
| Qual tipo de empresa abrir? LTDA, SLU, S-A, SAS, SCP... | `escolha-tipo-societario` |
| Redigir contrato social, estatuto, SLU | `constituicao-societaria` |
| Alterar contrato, lavrar ata, checagem de quorum | `alteracoes-e-atos-societarios` |
| Transformacao, incorporacao, fusao, cisao | `reorganizacao-societaria` |
| Dissolucao, exclusao de socio, apuracao de haveres | `dissolucao-e-saida-de-socio` |
| Acordo de socios/acionistas, tag/drag, vesting, governanca | `governanca-e-acordos` |
| SPA, due diligence, M&A, reps & warranties | `ma-e-due-diligence` |
| Registro Junta Comercial, RCPJ, IN DREI | `registro-empresarial` |

4. **Acionar** a skill identificada passando o contexto do `CASO.md`.
5. Ao concluir, acionar `suprema-corte-empresarial` (R1-R4) antes de entregar qualquer peca ou minuta.

**Skills do Tier 2:** `escolha-tipo-societario`, `constituicao-societaria`, `alteracoes-e-atos-societarios`, `reorganizacao-societaria`, `dissolucao-e-saida-de-socio`, `governanca-e-acordos`, `ma-e-due-diligence`, `registro-empresarial`.
