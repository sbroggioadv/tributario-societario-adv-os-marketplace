---
description: Roteia para as skills de estruturacao patrimonial e internacional (Tier 3) — holdings, planejamento sucessorio, offshore, trust, estrutura internacional e tributacao de lucros/dividendos.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [demanda patrimonial — ex: holding familiar, offshore, planejamento sucessorio]
---

Voce foi acionado pelo comando `/holding` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** rotear a demanda de estruturacao patrimonial e internacional para a skill Tier 3 adequada.

## PROTOCOLO

1. **Verificar** se o `CASO.md` esta criado. Se nao, acionar `triagem-empresarial` primeiro.
2. **Verificar** se o Selo de Validacao Legal foi emitido. Se nao, acionar `analisador-legislacao-vigente` antes de prosseguir (PA-01). Atentar para normas criticas: Lei 14.754/2023 (offshore), Lei 15.270/2025 (dividendos), EC 132/LC 227 (ITCMD), COSIT 75/2025 (trust — zona de litigio).
3. **Identificar** a demanda e rotear:

| Demanda | Skill |
|---------|-------|
| Holding pura/mista, arranjos de celulas, substancia economica | `estruturacao-holdings` |
| Holding familiar, doacao de quotas, usufruto, ITCMD, janela de planejamento | `planejamento-sucessorio-patrimonial` |
| Offshore, trust, Lei 14.754/2023, COSIT 75/2025 | `offshore-e-trust` |
| Empresa estrangeira no Brasil, filial vs subsidiaria, ADT, BACEN/CBE | `estrutura-internacional-empresarial` |
| IRRF sobre dividendos, Lei 15.270/2025, impacto em holdings | `tributacao-lucros-e-dividendos` |

4. **Atentar** para o Protocolo 6 (Internacional) em qualquer demanda com offshore, trust ou empresa estrangeira — sinalizar necessidade de advogado no pais-sede (PA-20).
5. **Nunca** apresentar holding/offshore/trust como "blindagem" contra Receita ou herdeiro necessario (PA-21).
6. Ao concluir, acionar `suprema-corte-empresarial` (R1-R4) antes de entregar qualquer parecer ou estrategia.

**Skills do Tier 3:** `estruturacao-holdings`, `planejamento-sucessorio-patrimonial`, `offshore-e-trust`, `estrutura-internacional-empresarial`, `tributacao-lucros-e-dividendos`.
