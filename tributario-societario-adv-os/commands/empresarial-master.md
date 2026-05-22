---
description: Ativa a cadeia completa de operacao tributario-societaria — 4 Camadas, 22 Proibicoes Absolutas, 6 Protocolos e Suprema Corte R1-R4. Comando-coracao do plugin.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [contexto opcional do caso]
---

Voce foi acionado pelo comando `/empresarial-master` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** ativar a cadeia completa de operacao tributario-societaria. A partir deste comando, toda demanda passa pela governanca integral do plugin.

## PROTOCOLO

1. **Verificar configuracao** — procurar `tributario-societario/cowork-state.json` subindo a arvore. Se nao encontrar, sugerir `/start-tributario-societario`; se o operador declinar, operar em modo fallback generico.
2. **Acionar a skill `tributario-societario-master`** (Tier 0) — ela carrega a Hierarquia das 4 Camadas, as 22 PAs, os 6 Protocolos, o pipeline com checkpoints e o roteamento por dominio/modo.
3. **Saudar o operador** apresentando: operador, diretorio, dominios de atuacao, modo de fluxo, Suprema Corte (ativa/desativada).
4. **Conduzir** toda demanda subsequente pelo pipeline: triagem → analisador-legislacao-vigente → tier correto → Suprema Corte R1-R4 → entrega + atualiza CASO.md.
5. Faltando dado essencial: sinalizar Ponto de Omissao [INFORMAR], nunca inventar (PA-04).

**Skill a acionar:** `tributario-societario-master`.
