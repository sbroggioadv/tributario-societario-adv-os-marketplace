---
description: Submete um documento empresarial a auditoria final da Suprema Corte (R1-R2-R3-R4) antes da entrega — brief/escopo, tecnica juridica, compliance e performance.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [documento a auditar]
---

Voce foi acionado pelo comando `/revisao-final` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** auditar um documento empresarial pela Suprema Corte antes da entrega.

## PROTOCOLO

1. **Acionar a skill `suprema-corte-empresarial`**.
2. Identificar o documento a auditar e o caso ativo (`CASO.md`).
3. Executar a sequencia obrigatoria:
   - **R1** — Brief/escopo: a entrega responde ao pedido? escopo correto?
   - **R2** — Tecnica juridica: norma vigente e datada? competencia certa? teses classificadas? calculos marcados?
   - **R3** — Compliance: todas as 22 PAs respeitadas? Selo de Validacao Legal presente? ressalva OAB?
   - **R4** — Performance: FIRAC aplicado? clareza e completude? Pontos de Omissao alertados?
4. Cada rodada emite `APROVADO` / `APROVADO COM RESSALVAS` / `REPROVADO`. Reprovacao bloqueia e devolve ao produtor.
5. Apresentar o relatorio final consolidado com resultado de cada rodada.

Bypass disponivel: `--no-corte` (registra waiver) ou `--quick` (R1+R2 apenas, para rascunhos internos).

**Skill a acionar:** `suprema-corte-empresarial`.
