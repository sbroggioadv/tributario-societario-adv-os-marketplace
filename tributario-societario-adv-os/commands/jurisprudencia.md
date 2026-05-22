---
description: Localiza, classifica e prioriza precedentes tributarios e societarios — busca viva nos tribunais superiores, classificacao em vinculante/em disputa/superada, com verificacao de modulacao de efeitos.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, WebFetch
argument-hint: [tese ou tema a pesquisar — ex: exclusao ICMS PIS/COFINS, Tema 69 STF]
---

Voce foi acionado pelo comando `/jurisprudencia` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** localizar e classificar jurisprudencia tributaria e societaria para uma tese.

## PROTOCOLO

1. **Acionar a skill `estrategia-de-caso-empresarial`** — acionar especificamente o Protocolo Jurisprudencial (Protocolo 3).
2. Identificar a tese ou o tema a pesquisar (do argumento ou do caso ativo no `CASO.md`).
3. Busca viva: `WebSearch`/`WebFetch` nos portais do STF (repercussao geral), STJ (recursos repetitivos), CARF (sumulas e acordaos) e TRFs. Usar `firecrawl` para portais JS-pesados se disponivel.
4. **Classificar** cada precedente obrigatoriamente (PA-04):
   - `Vinculante` — Tema STF com repercussao geral julgada; Tema STJ com recurso repetitivo julgado; Sumula Vinculante; Sumula CARF de efeito vinculante.
   - `Em disputa [VERIFICAR]` — tese em julgamento; divergencia entre camaras CARF; Solucoes de Consulta contraditorias.
   - `Superada` — tese expressamente abandonada por acordao posterior; Tema julgado contrariamente.
5. **Verificar modulacao de efeitos** em toda decisao vinculante (PA-07) — quem aproveita, a partir de quando, prazo de habilitacao.
6. **Nunca inventar** numero de Tema, Sumula ou acordao — marcar `[VERIFICAR — confirmar na fonte oficial]` se incerto (PA-04).
7. Apresentar os precedentes hierarquizados: STF > STJ-1a Secao > CARF-CSRF > TRF > CARF-Camaras.

**Skill a acionar:** `estrategia-de-caso-empresarial` (Protocolo Jurisprudencial).
