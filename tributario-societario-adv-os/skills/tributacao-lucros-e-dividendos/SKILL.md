---
name: tributacao-lucros-e-dividendos
description: >
  Tributacao de lucros e dividendos sob a Lei 15.270/2025 — IRRF de 10% sobre distribuicao
  PJ para PF acima de R$ 50.000 por mes, IRPFM (imposto complementar), regra de transicao
  para lucros deliberados ate 31/12/2025. Impacto em estruturas de holding e estrategia
  pro-labore vs dividendo. Vigencia 2026. Aciona: dividendos, distribuicao de lucros,
  tributacao de lucro, IRRF, pro-labore vs dividendo.
---

# TRIBUTACAO DE LUCROS E DIVIDENDOS

> Skill **Tier 3 — Estruturacao Patrimonial** — orienta o regime de tributacao de dividendos
> e lucros distribuidos sob a Lei 15.270/2025, com impacto em holdings e na estrategia
> de remuneracao do socio. Implementa PA-02, PA-09, PA-21, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "dividendos", "distribuicao de lucros", "tributacao de lucro", "IRRF sobre
dividendos", "pro-labore vs dividendo", "10% sobre dividendos", "Lei 15.270", "IRPFM",
"regra de transicao dividendos", "dividendos PJ para PF".

Entrega: mapa do regime Lei 15.270/2025 (IRRF + IRPFM) + regra de transicao + impacto em
holdings + analise pro-labore vs dividendo + alertas.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `estruturacao-holdings` (Tier 3), `planejamento-tributario` (Tier 4).
- **Entrega para:** `estruturacao-holdings` (impacto no arranjo de celulas),
  `planejamento-tributario` (Tier 4) para modelagem de cenarios,
  `mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar Lei 15.270/2025 vigente e
  sem alteracao posterior relevante; Protocolo 1.

---

## 2. LEI 15.270/2025 — TRIBUTACAO DE DIVIDENDOS

### 2.1 Vigencia e fato gerador

**Lei 15.270/2025.** Vigencia: exercicio fiscal de 2026 (fatos geradores a partir de
01/01/2026). Distribuicoes anteriores a essa data seguem o regime anterior (isentos para
PF — ver regra de transicao na secao 3).

### 2.2 IRRF sobre distribuicao PJ para PF

- **Sujeito passivo:** socio ou acionista pessoa fisica que recebe dividendos ou lucros
  distribuidos por PJ brasileira.
- **Aliquota:** 10% (IRRF na fonte, retido pela PJ distribuidora).
- **Limite de isencao mensal:** R$ 50.000 por mes [VERIFICAR se o limite e por CPF ou por
  fonte pagadora — lei pode distinguir].
- **Base de calculo:** distribuicao que supere R$ 50.000/mes ao mesmo beneficiario PF.
  A parcela ate R$ 50.000/mes permanece isenta (confirmar redacao definitiva [VERIFICAR]).
- **Momento da retencao:** no pagamento ou credito dos dividendos.

**Exemplo estimativo (PA-09 — valor sujeito a conferencia):**
- Dividendos mensais R$ 100.000 a unico socio PF:
  - Base tributavel: R$ 50.000 (excesso sobre R$ 50.000/mes).
  - IRRF retido na fonte: R$ 5.000 (10% de R$ 50.000).
  - Dividendo liquido recebido: R$ 95.000.
  Estimativa — sujeita a conferencia contabil e interpretacao da legislacao local.

### 2.3 IRPFM (Imposto de Renda Progressivo Minimo)

Alem do IRRF, a Lei 15.270/2025 introduz o IRPFM (Imposto de Renda sobre Pessoas Fisicas
de elevada renda — imposto complementar), que visa garantir tributacao efetiva minima para
contribuintes PF com renda total elevada.

[VERIFICAR: a regulamentacao do IRPFM pode estar em instrucao normativa propria —
confirmar aliquotas, base de calculo e prazo de recolhimento com o texto definitivo da lei
e regulamentacao].

O IRPFM pode resultar em tributacao complementar sobre dividendos mesmo dentro do limite
mensal isento, se a renda total do socio ultrapassar determinado patamar.

### 2.4 Distribuicao PJ para PJ

Dividendos distribuidos de PJ para PJ (ex.: operacional distribui para holding, holding
distribui para outra holding) — verificar regime de tributacao aplicavel:
- Participacao societaria com beneficio de isencao [VERIFICAR — regras sobre lucros
  recebidos por PJ podem ter sido alteradas pela Lei 15.270/2025].
- Se houver cadeia de holdings, avaliar impacto em cada elo (regras de transparencia
  [VERIFICAR redacao final da lei]).

---

## 3. REGRA DE TRANSICAO

### 3.1 Lucros deliberados ate 31/12/2025

**Regra de transicao:** lucros apurados e deliberados (aprovados pela assembleia/reuniao
de socios) ate **31 de dezembro de 2025** estao sujeitos ao regime anterior — isencao de
IRPF sobre dividendos (regime vigente ate 2025).

**Implicacao pratica:**
- Lucros acumulados de anos anteriores (ate 2025) que sejam formalmente deliberados
  (ata de distribuicao) ate 31/12/2025 podem ser distribuidos aos socios PF com isencao de
  IRPF mesmo que o pagamento ocorra em 2026 [VERIFICAR condicoes exatas na lei — o criterio
  pode ser a data de deliberacao ou a data do pagamento].
- **Janela de planejamento:** deliberar a distribuicao de lucros acumulados ate 31/12/2025
  pode reduzir a base de incidencia do IRRF em 2026+. Mas:
  - PA-21: este plugin nunca promete resultado fiscal garantido.
  - A deliberacao deve ser autentica — nao um ato simulado para fins exclusivos de
    planejamento tributario (PA-16, Protocolo 2).
  - Verificar se ha caixa disponivel ou se a distribuicao sera so escritural [VERIFICAR
    impacto contabil].

---

## 4. IMPACTO EM ESTRUTURAS DE HOLDING

### 4.1 Holding pura com socios PF

A holding pura recebe dividendos isentos das operacionais (regime PJ→PJ, sujeito a
confirmacao — ver 2.4) e distribui para os socios PF. A distribuicao da holding para o
socio PF esta sujeita ao IRRF 10% sobre o excesso de R$ 50.000/mes.

**Ponto de atencao:** o limite de R$ 50.000/mes e individual (por CPF) [VERIFICAR — confirmar
se por CPF ou por fonte pagadora na Lei 15.270/2025]. Em grupos com
multiplas holdings distribuindo para o mesmo socio, o agregado pode superar o limite.

### 4.2 Holding mista

Receita operacional + receita de participacoes. A tributacao na holding e normal (IRPJ,
CSLL, PIS/COFINS). O dividendo que sai da holding para o socio PF e tributado nas mesmas
regras acima.

### 4.3 Impacto no arranjo de celulas

Estruturas de 2 ou 3 celulas com distribuicao em cascata (operacional → patrimonial →
controladora → socios PF) devem ser reavaliadas:
- Cada camada deve ter substancia economica real (PA-16/PA-19).
- Eventual recaracterizacao de distribuicao como distribuicao indireta [VERIFICAR RFB].
- Custo adicional do IRRF em cada camada que eventualmente distribua a PF.

---

## 5. PRO-LABORE VS DIVIDENDO

### 5.1 Logica pre-Lei 15.270/2025

Antes de 2026, dividendos eram isentos e pro-labore era tributado pela tabela progressiva
do IRPF (ate 27,5%) + previdencia. O planejamento classico priorizava dividendos.

### 5.2 Pos-Lei 15.270/2025

O diferencial de tratamento entre pro-labore e dividendos diminuiu para socios de alta renda
(dividendos agora com IRRF 10% + eventual IRPFM complementar). A analise deve ser feita
caso a caso:

- Pro-labore: dedutivel no IRPJ/CSLL da empresa (reduz base tributavel); tributado no
  socio pela tabela progressiva IRPF (0% a 27,5%) + previdencia.
- Dividendos: nao dedutivel no IRPJ/CSLL da empresa; tributado no socio a 10% IRRF sobre
  excesso + eventual IRPFM.
- A equacao depende do regime tributario da empresa, do volume de distribuicao e da renda
  total do socio. [VERIFICAR impacto especifico para Simples Nacional — regras de
  distribuicao no Simples podem ser diferentes].

**PA-09 — toda estimativa comparativa e sujeita a conferencia contabil e fiscal.**

---

## 6. VEDACOES ESPECIFICAS

- **PA-02** — validar vigencia e redacao da Lei 15.270/2025 no ano do fato gerador;
  regulamentacao pode ter alterado detalhes.
- **PA-09** — todo valor de IRRF estimado e sujeita a conferencia contabil/fiscal.
- **PA-21** — nunca prometer economia fiscal garantida na estrategia dividendos vs pro-labore.
- **PA-22** — toda analise e minuta sujeita a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — Lei 15.270/2025 vigente; IN RFB de regulamentacao
  [VERIFICAR]; impacto no Simples Nacional [VERIFICAR].
- **Protocolo 2 — Mitigacao de Risco Fiscal** — deliberacao de lucros pre-2026 deve ser autentica
  e ter substancia.
- **Protocolo 4** (Competencia) — IRRF: competencia federal; retencao pela PJ distribuidora.
- **Protocolo 5** (Calculo) — toda estimativa de IRRF e IRPFM marcada como estimativa.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`estruturacao-holdings`, `planejamento-tributario` (Tier 4).

**Entrega para:** `estruturacao-holdings` (impacto em celulas),
`planejamento-tributario` (Tier 4) modelagem de cenarios,
`mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** socio PF recebendo dividendos sem conhecimento do IRRF 10%, sem analise
da regra de transicao de lucros pre-2026 e sem comparativo pro-labore vs dividendo atualizado
para 2026.
