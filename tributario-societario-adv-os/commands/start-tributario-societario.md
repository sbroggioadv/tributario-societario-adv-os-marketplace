---
description: Inicia o wizard de configuracao do plugin Tributario-Societario — cria a pasta tributario-societario/ com identidade, areas de atuacao, tom e modo de fluxo.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [--update para reconfigurar]
---

Voce foi acionado pelo comando `/start-tributario-societario` do plugin Tributario-Societario-Adv-OS.

Argumento recebido: `$ARGUMENTS`

**Objetivo:** configurar o plugin tributario-societario no ambiente do operador.

## PROTOCOLO

1. **Acionar a skill `tributario-societario-onboarding`** imediatamente — ela conduz o wizard completo.
2. O wizard cria `<cwd>/tributario-societario/` com `persona.md`, `config.md`, `casos/` e o `cowork-state.json`, alem de `.claude/settings.local.json`.
3. Se ja existir `tributario-societario/cowork-state.json`, a skill oferece continuar / atualizar / recriar (idempotencia).
4. Se o argumento for `--update`, ir direto para o fluxo de atualizacao.

**Atencao LGPD:** a skill avisa se o diretorio estiver em pasta sincronizada (iCloud/OneDrive/Dropbox/Drive).

**Skill a acionar:** `tributario-societario-onboarding`.
