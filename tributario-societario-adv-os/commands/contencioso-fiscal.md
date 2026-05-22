---
description: Roteia para as skills de tributario contencioso (Tier 5) — analise de auto de infracao, defesa administrativa (CARF/TIT), execucao fiscal, acao do contribuinte e recursos judiciais.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [demanda contenciosa — ex: auto de infracao IRPJ, embargos execucao fiscal, MS]
---

Voce foi acionado pelo comando `/contencioso-fiscal` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** rotear a demanda tributaria contenciosa para a skill Tier 5 adequada.

## PROTOCOLO

1. **Verificar** se o `CASO.md` esta criado com competencia e esfera identificadas (PA-11). Se nao, acionar `triagem-empresarial` primeiro — a triagem mapeia prazos em curso imediatamente.
2. **Verificar** se o Selo de Validacao Legal foi emitido (PA-01).
3. **Identificar prazo urgente** no `CASO.md` — se houver prazo em curso, alertar o operador antes de qualquer outra acao.
4. **Identificar** a demanda e rotear:

| Demanda | Skill |
|---------|-------|
| Dissecar auto de infracao: vicios, merito, decadencia, opcoes | `analise-auto-de-infracao` |
| Impugnacao, recurso voluntario CARF, CSRF, TIT, conselhos | `pecas-defesa-administrativa` |
| Embargos a execucao fiscal, excecao de pre-executividade | `pecas-defesa-execucao-fiscal` |
| Mandado de seguranca, anulatoria, declaratoria, repeticao de indebito | `pecas-acao-do-contribuinte` |
| Apelacao, REsp, RE — requisitos de admissibilidade | `recursos-judiciais-tributarios` |

5. **Nunca** confundir embargos a execucao (exige garantia) com excecao de pre-executividade (PA-08).
6. **Nunca** confundir esfera administrativa e judicial (PA-05).
7. Ao concluir cada peca, acionar `suprema-corte-empresarial` (R1-R4) antes de qualquer protocolo ou entrega ao orgao competente.

**Skills do Tier 5:** `analise-auto-de-infracao`, `pecas-defesa-administrativa`, `pecas-defesa-execucao-fiscal`, `pecas-acao-do-contribuinte`, `recursos-judiciais-tributarios`.
