# Configuração — tributario-societario-adv-os

> Configuração operacional do plugin no ambiente do escritório. Vive em
> `<COWORK>/tributario-societario/config.md`. Gerada pelo `/start-tributario-societario`. Editável
> manualmente — mudanças valem na próxima sessão.

---

## Modos e Domínios de Atuação

- **Modos:** {{MODOS}}
  <!-- consultivo | contencioso | ambos -->
- **Domínios:** {{DOMINIOS}}
  <!-- tributario | societario | ambos -->

> Define os modos (consultivo/contencioso) e domínios (tributário/societário) em que o escritório
> atua. A `triagem-empresarial` confirma o modo e o domínio caso a caso e grava no `CASO.md`.

---

## Especialidades

- **Especialidades:** {{ESPECIALIDADES}}
  <!-- ex: holding pura/mista, offshore/trust, reforma tributária, CARF, execução fiscal,
       planejamento sucessório, M&A/due diligence, reorganização societária, consultivo tributário -->

---

## Tom de voz

- **Perfil:** {{TOM_VOZ_PERFIL}}
  <!-- tecnico-combativo | tecnico-cordial | tecnico-didatico | personalizado -->
- **Intensidade combativa:** {{TOM_VOZ_INTENSIDADE}}/10
- **Postura default:** {{POSTURA_DEFAULT}}

---

## Modo de fluxo

- **Modo:** {{MODO_FLUXO}}
  <!-- checkpoint (default) | continuo -->

> `checkpoint` — o pipeline para e confirma com o advogado ao fim de cada fase
> (4 checkpoints). `continuo` — entrega o pacote completo de uma vez, sem parar.

---

## Suprema Corte

- **Auditoria R1-R4:** {{SUPREMA_CORTE_STATUS}}
  <!-- ATIVA (default) | DESATIVADA -->
- Bypass por demanda: `--no-corte`, `--quick`, `/corte off`.

---

## Ferramentas declaradas

- **Ferramentas:** {{FERRAMENTAS}}
  <!-- sistema de gestão processual, transcrição, CRM, etc. — campos livres -->

---

**Plugin:** `tributario-societario-adv-os` v{{PLUGIN_VERSION}}
**Gerado em:** {{GENERATED_AT}}
**State source:** `{{COWORK_PATH}}/tributario-societario/cowork-state.json`
