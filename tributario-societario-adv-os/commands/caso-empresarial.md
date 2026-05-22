---
description: Abre um caso empresarial novo ou retoma um caso existente — cria/le a pasta do caso, o CASO.md e o MEMORY.md.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [nome do caso — ex: empresa-x-auto-infracao-irpj]
---

Voce foi acionado pelo comando `/caso-empresarial` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** abrir um caso novo ou retomar um caso existente.

## PROTOCOLO

1. **Acionar a skill `memoria-de-caso-empresarial`**.
2. Se o argumento corresponde a um caso existente em `tributario-societario/casos/`, **retomar** — ler o `CASO.md` e o `MEMORY.md`, apresentar resumo (dominio, modo, fase, ultima etapa, pendencias, prazos).
3. Se nao existe, **abrir caso novo** — acionar a `triagem-empresarial` para colher dominio, modo, competencia e dados do cliente, e criar a pasta `casos/<slug-do-caso>/` com `CASO.md`, `MEMORY.md` e as subpastas.
4. Confirmar com o operador antes de criar a pasta.

**Skills a acionar:** `memoria-de-caso-empresarial` (e `triagem-empresarial` se for caso novo).
