---
description: Mostra o estado do caso empresarial ativo — dominio, modo, fase, linha estrategica, prazos, pendencias e configuracao do plugin.
allowed-tools: Read, Bash, Glob, Grep
argument-hint: [nome do caso — opcional]
---

Voce foi acionado pelo comando `/status-empresarial` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** apresentar um diagnostico do caso empresarial ativo (ou do indicado no argumento) e da configuracao do plugin.

## PROTOCOLO

1. Localizar o caso: se o argumento indica um caso, usar; senao, usar o caso ativo / o mais recente em `tributario-societario/casos/`.
2. **Ler o `CASO.md`** e o `MEMORY.md` do caso (mantidos pela `memoria-de-caso-empresarial`).
3. Apresentar o resumo:

```
STATUS — [cliente] | [slug-do-caso]

Dominio: [tributario | societario | tributario-societario]
Modo: [consultivo | contencioso | consultivo-contencioso]
Competencia: [federal/estadual/municipal — adm/judicial]
Orgao atual: [nome]
Fase processual: [fase]
Prazo urgente: [prazo ou "nenhum em curso"]
Ultima etapa concluida: [do MEMORY.md]
Pendencias / Pontos de Omissao: [lista]
Pecas produzidas: [lista com veredito R1-R4]
Proximo passo sugerido: [do MEMORY.md]
```

4. Exibir tambem o estado da configuracao do plugin:

```
CONFIGURACAO DO PLUGIN
Operador: {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
Escritorio: {{FIRM_NAME}}, {{CIDADE}}/{{UF}}
Tom: {{TOM_VOZ_PERFIL}}, intensidade {{TOM_VOZ_INTENSIDADE}}/10
Suprema Corte: [ativa | desativada]
```

5. Se nao houver caso configurado, sugerir `/caso-empresarial` ou `/start-tributario-societario`.

**Sem skill obrigatoria** — leitura direta do `CASO.md` e do `MEMORY.md`.
