---
name: analisador-legislacao-vigente
description: >
  Valida se cada norma (lei, artigo, sumula, tema) citada esta vigente e na redacao correta para o ANO DO FATO GERADOR. Consulta fontes oficiais (Planalto, LexML, normas.leg.br, DOU, Receita, DREI, CVM). Emite o Selo de Validacao Legal — pre-requisito de toda estrategia juridica. Trata a lei como alvo movel (reforma tributaria 2026-2033). Aciona: validar lei, lei vigente, a norma ainda vale, checar legislacao, reforma tributaria.
---

# ANALISADOR DE LEGISLACAO VIGENTE

> Skill **Tier 0** — Protocolo 1 em operacao. Pre-requisito absoluto de toda skill estrategica (Tier 1-5). Emite o Selo de Validacao Legal. Implementa PA-01 e PA-02.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por `tributario-societario-master` antes de qualquer estrategia, ou diretamente pelo operador com `/legislacao`, "validar lei", "checar se a norma vale", "a lei ainda esta em vigor", "reforma tributaria impacta". Recebe: (norma citada, tipo de caso, ano do fato gerador). Entrega: laudo de vigencia + Selo de Validacao Legal.

## 1. POSICAO NA ORQUESTRA

- Chamada por: `tributario-societario-master` (Tier 0), `triagem-empresarial` (Tier 1), qualquer skill Tier 1-5 que precise validar norma.
- Entrega para: skill estrategica solicitante + `CASO.md` (campo `Selo de Validacao Legal`).
- Dependencia PA-01: **nenhuma skill estrategica opera sem o Selo**.

---

## 2. OS 8 PASSOS DO PROTOCOLO 1

### Passo 1 — Datar o fato gerador

Identificar a data exata do evento tributavel ou ato societario. Esta data e o marco para determinar qual redacao da lei se aplica — nao a data de hoje, nao a data do build do plugin.

> Perguntar ao operador se nao informado: "Qual a data do fato gerador (ou do ato societario)? Exemplo: 15/03/2026."

### Passo 2 — Inventariar as normas

Listar todas as normas relevantes para o caso:

- Lei Complementar / Lei Ordinaria / Decreto / Instrucao Normativa / Portaria / Solucao de Consulta / Ato Declaratorio Interpretativo
- Normas estaduais se houver ICMS, ITCMD, ITBI
- Normas municipais se houver ISS, IPTU
- Regulamentos setoriais (CVM, BACEN, Previc) se houver estrutura de capital ou offshore

### Passo 3 — Validar vigencia

Para cada norma listada:

1. Data de publicacao (DOU)
2. Vacatio legis (prazo antes da vigencia)
3. Data de inicio da vigencia efetiva
4. Revogacao expressa ou tacita anterior ao fato gerador?
5. Classificar: **VIGENTE** / **ALTERADA** / **REVOGADA** / **VACATIO** / **INDETERMINADO**

Norma **INDETERMINADO** → sinalizar e pedir orientacao ao operador antes de prosseguir.

### Passo 4 — Checar redacao efetiva no ano

A norma pode ter sido alterada por multiplas MPs ou leis apos a edicao original. Verificar a **redacao vigente no ano do fato gerador**, nao a redacao atual. Indicar a versao da norma usada.

> Exemplo: art. 74 da Lei 9.430/1996 teve sua redacao alterada multiplas vezes. A versao aplicavel depende do ano do fato gerador da compensacao.

### Passo 5 — Travar o regime tributario do ano

Critico durante a transicao CBS/IBS (2026-2033):

| Ano do fato gerador | Regime aplicavel |
|---------------------|-----------------|
| ate 2026 | PIS/COFINS integrais; CBS 0,9%/IBS 0,1% so de teste |
| 2027 | CBS plena. PIS e COFINS extintos. IPI zerado (salvo ZFM). IS cobrado. |
| 2028 | CBS consolidada; ICMS/ISS integrais; IBS em aliquota-teste |
| 2029-2032 | Transicao gradual: ICMS/ISS reduzem e IBS sobe progressivamente — [VERIFICAR percentuais exatos de cada ano na LC 214/2025 / EC 132/2023] |
| 2033+ | ICMS e ISS extintos. Modelo pleno CBS+IBS+IS |

> Base: EC 132/2023 + LC 214/2025 (regulamentacao infralegal pendente — reverificar a cada uso).

### Passo 6 — Verificar infralegais/locais

- Instrucao Normativa da RFB vigente (ex.: IN RFB 2.180/2024 para offshore)
- Decreto Estadual do ICMS do estado do contribuinte
- Regulamento Municipal do ISS
- IN DREI vigente para atos societarios
- Circular/Resolucao BACEN para capital estrangeiro

A lei pode ser federal mas a regulamentacao e local — nunca assumir padrao uniforme.

### Passo 7 — Rastrear PL/MP pendente

Verificar se ha proposta legislativa ou medida provisoria relevante em tramitacao:

- PL 4/2025 — reforma do Codigo Civil (pode alterar LTDA/SCP/simples)
- Regulamentacoes pendentes da LC 214/2025 (CBS/IBS)
- COSIT 75/2025 (trust discretionario) — entendimento controverso [VERIFICAR]
- LC 227/2026 (ITCMD internacional) [VERIFICAR — confirmar promulgacao e numero oficial] — estados ainda atualizando legislacao local

Sinalizar ao operador qualquer norma pendente com potencial de impacto no caso.

### Passo 8 — Emitir o Selo de Validacao Legal

```
SELO DE VALIDACAO LEGAL
Data-base: [DD/MM/AAAA]
Fato gerador datado: [data]
Normas validadas:
  - [norma] — VIGENTE — redacao de [data], art. [X] em vigor desde [data]
  - [norma] — ALTERADA — redacao vigente no ano: [versao especifica]
  - [norma] — [VERIFICAR] — vigencia indeterminada, confirmar antes de usar
Regime tributario travado: [PIS/COFINS | CBS/IBS | transicao X%]
Infralegais verificadas: [lista resumida]
Alertas normativos: [PLs/MPs pendentes com potencial impacto]
Validade: este Selo reflete a legislacao na data-base acima.
          Reverificar se o caso for fechado apos [data + 60 dias].
```

O Selo e registrado no `CASO.md` (campo `Selo de Validacao Legal`). Qualquer skill estrategica que receber demanda sem Selo deve acionar esta skill primeiro.

---

## 3. FONTES OFICIAIS DE VALIDACAO

| Fonte | URL | Uso |
|-------|-----|-----|
| Planalto (Legislacao Federal) | planalto.gov.br/ccivil_03 | Leis, LCs, Decretos, MPs |
| normas.leg.br | normas.leg.br | Busca federal consolidada |
| LexML | lexml.gov.br | Jurisprudencia + legislacao estruturada |
| DOU / in.gov.br | in.gov.br | Publicacao oficial — data de vigencia |
| SIJUT / Receita | normas.receita.fazenda.gov.br | INs, ADIs, Solucoes de Consulta RFB |
| DREI | gov.br/drei | Instrucoes Normativas societarias |
| Juntas Comerciais | (por estado) | Requisitos de arquivamento |
| CVM | cvm.gov.br | Instrucoes e resolucoes CVM |
| BACEN | bcb.gov.br | Circulares, resolucoes cambiais |

> **PA-04 — Alucinacao vedada:** se nao tiver certeza do numero de artigo, lei, sumula ou tema, marcar como `[VERIFICAR — confirmar na fonte oficial]` e indicar o caminho de busca. Nunca inventar ou aproximar referencia.

---

## 4. FLAG DE NORMA DESATUALIZADA

Se o operador citar norma revogada, alterada ou com virada iminente:

```
[ALERTA NORMATIVO]
A norma citada ([ex.: art. X da Lei Y]) nao se aplica ao fato gerador de [ano].
Motivo: [revogada por / alterada por / substituida por]
Norma aplicavel ao periodo: [Z]
Acao recomendada: [substituir a referencia / verificar texto vigente / aguardar regulamentacao]
```

Nunca prosseguir com norma sinalizada como REVOGADA sem confirmacao expressa do operador.

---

## 5. VEDACOES ESPECIFICAS

- **PA-01** — Selo nao emitido = estrategia bloqueada.
- **PA-02** — Redacao atual nao substitui redacao vigente no ano do fato gerador.
- **PA-04** — Zero alucinacao de norma, artigo, sumula ou tema.
- **PA-06** — Regime tributario travado pelo ano do fato gerador, nunca por "hoje".
- Nunca emitir Selo sem completar os 8 passos.
- Nunca afirmar vigencia sem checar fonte oficial.

---

## 6. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — esta skill **e** o Protocolo 1.
- **Protocolo 3** (Jurisprudencial) — aplicado a sumulas e temas citados.
- **Protocolo 4** (Competencia) — identificar a competencia tributaria da norma.

---

## 7. INTEGRACAO

**Chamada por:** `tributario-societario-master` (obrigatorio antes de Tier 1-5), `triagem-empresarial`, qualquer skill que receba citacao de norma juridica.

**Entrega para:** skill estrategica que aguarda o Selo + campo `Selo de Validacao Legal` no `CASO.md`.

**Sem esta skill:** nenhuma estrategia tributaria ou societaria com implicacao fiscal pode prosseguir (PA-01 + Protocolo 1).
