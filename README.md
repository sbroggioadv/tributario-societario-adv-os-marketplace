# Tributário-Societário Adv-OS — Marketplace

Marketplace oficial do plugin **Tributário-Societário Adv-OS** para Claude Code — um assistente técnico-jurídico especializado em **direito tributário** e **direito societário** brasileiro, para advocacia empresarial.

---

## O que é

O Tributário-Societário Adv-OS transforma o Claude Code em um copiloto jurídico empresarial que cobre o ciclo completo da advocacia tributária e societária — do **consultivo** (planejamento, estruturação, pareceres) ao **contencioso** (CARF, TIT, execução fiscal, judicial).

- **33 skills** organizadas em Tier 0-6 (orquestrador → núcleo → societário → estruturação patrimonial → tributário consultivo → tributário contencioso → Suprema Corte Empresarial)
- **Validação de legislação vigente** como premissa de toda estratégia — a lei é alvo móvel (reforma tributária 2026-2033: CBS/IBS/IS)
- **22 Proibições Absolutas** e **6 Protocolos Técnicos** aplicados automaticamente em peças e pareceres
- **Suprema Corte Empresarial R1-R4** — auditoria obrigatória antes de qualquer entrega
- **Onboarding guiado** via `/start-tributario-societario` (~5 minutos)
- **100% configurável** ao perfil do escritório em runtime — identidade, áreas, tom de voz e modo de fluxo. Nada hardcoded.

### Áreas cobertas

| Frente | Escopo |
|--------|--------|
| Tributário consultivo | Planejamento (Simples/Presumido/Real), reforma tributária (CBS/IBS/IS), recuperação de créditos, pareceres e consultas fiscais, mitigação de risco |
| Tributário contencioso | Auto de infração, impugnação e recurso ao CARF, execução fiscal (embargos + exceção de pré-executividade), mandado de segurança, recursos judiciais |
| Societário | Constituição (LTDA/SLU/S.A./SAS), reorganizações (incorporação/fusão/cisão), dissolução, acordos de sócios/acionistas, M&A e due diligence |
| Estruturação patrimonial e internacional | Holdings puras/mistas/1/2/3 células, planejamento sucessório, offshore e trust (Lei 14.754/2023, COSIT 75/2025), tributação de lucros e dividendos (Lei 15.270/2025) |

---

## Instalação

1. Abra o **Claude Code** (Cowork)
2. Vá em **Settings → Plugins → aba Pessoal → "+" → Uploads locais**
3. Cole a URL deste repositório:
   ```
   https://github.com/sbroggioadv/tributario-societario-adv-os-marketplace
   ```
4. Sincronize e instale o plugin **tributario-societario-adv-os**
5. Em qualquer sessão, rode `/start-tributario-societario` para configurar seu escritório

---

## Conteúdo do marketplace

| Plugin | Descrição |
|--------|-----------|
| [`tributario-societario-adv-os`](./tributario-societario-adv-os) | Plugin completo — 33 skills, 12 commands, 4 hooks |

---

## Requisitos

- Claude Code (Cowork)
- Python 3.11+ (scripts internos de hooks)

---

## Licença

O marketplace é distribuído sob licença MIT (ver [`LICENSE`](./LICENSE)). O uso comercial do plugin segue os termos da licença de uso fornecida na aquisição.
