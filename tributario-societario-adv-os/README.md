# Plugin Tributário-Societário Adv-OS

Plugin Claude Code para advocacia empresarial brasileira — tributário e societário.

---

## O Que Este Plugin Faz

O **Tributário-Societário Adv-OS** especializa o Claude Code para atuar como assistente técnico-jurídico nas áreas de **direito tributário** e **direito societário** brasileiro. Cobre tanto o **consultivo** (planejamento, estruturação, pareceres) quanto o **contencioso** (CARF, TIT, execução fiscal, judicial).

### Funcionalidades

- **33 skills** organizadas em Tier 0-6 (orquestrador → núcleo → societário → estruturação patrimonial → tributário consultivo → tributário contencioso → Suprema Corte)
- **Validação de legislação vigente** como premissa de qualquer estratégia — lei é alvo móvel (reforma tributária 2026-2033)
- **22 Proibições Absolutas** (PA-01..PA-22) aplicadas automaticamente em todas as peças e pareceres
- **6 Protocolos Técnicos** (Validação Legal Prévia, Mitigação de Risco, Jurisprudencial, Competência, Cálculo, Internacional)
- **Suprema Corte Empresarial R1-R4** — auditoria obrigatória antes de entregar qualquer peça ou parecer
- **Onboarding guiado** via `/start-tributario-societario` — configura identidade do escritório, áreas, tom de voz e modo de fluxo em ~5 minutos
- **Persona em runtime** — identidade do operador vive fora do plugin, nunca hardcoded

### Áreas Cobertas

**Tributário Consultivo:** planejamento tributário (Simples/Presumido/Real), reforma tributária (CBS/IBS/IS), recuperação de créditos, pareceres e consultas fiscais, mitigação de risco fiscal.

**Tributário Contencioso:** análise de auto de infração, impugnação e recurso ao CARF, defesa em execução fiscal (embargos + exceção de pré-executividade), mandado de segurança, ações do contribuinte, recursos judiciais tributários.

**Societário:** constituição (LTDA/SLU/S.A./SAS), reorganizações (incorporação/fusão/cisão), dissolução, governança e acordos de sócios/acionistas, M&A e due diligence, registro empresarial.

**Estruturação Patrimonial e Internacional:** holdings puras/mistas/1/2/3 células, planejamento sucessório, offshore e trust (Lei 14.754/2023, COSIT 75/2025), empresa estrangeira no Brasil, tributação de lucros e dividendos (Lei 15.270/2025).

---

## Instalação

1. Abra o **Claude Code** (Cowork)
2. Acesse **Settings → Plugins → Pessoal → "+" Uploads locais**
3. Cole a URL do repositório marketplace do plugin (fornecida na sua compra)
4. Clique em **Instalar**

Após instalação, rode `/start-tributario-societario` em qualquer sessão para configurar seu escritório.

---

## Uso

```
/start-tributario-societario    # onboarding — configure identidade e áreas
/empresarial-master             # orquestrador geral
/tributario                     # consultivo tributário
/contencioso-fiscal             # peças tributárias contenciosas
/societario                     # atos societários
/holding                        # estruturação patrimonial/internacional
/parecer                        # parecer tributário
/revisao-final                  # Suprema Corte R1-R4 (auditoria)
```

---

## Requisitos

- Claude Code (Cowork) instalado
- Python 3.11+ (para os scripts internos de hooks)

---

## Licença

MIT — ver `LICENSE`.
