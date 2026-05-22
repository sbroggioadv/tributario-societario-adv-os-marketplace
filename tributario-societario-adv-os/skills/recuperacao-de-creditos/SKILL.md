---
name: recuperacao-de-creditos
description: >
  Identificacao e instrucao de creditos tributarios recuperaveis e compensacao via
  PER/DCOMP. Trata o art. 166 CTN para tributos indiretos (prova de nao-repercussao).
  Abrange IRPJ/CSLL, PIS/COFINS, contribuicoes previdenciarias, ICMS (Estadual), ISS.
  Nunca crava valor de credito como definitivo — estimativa sujeita a homologacao RFB.
  Aciona: recuperar credito, compensacao, PER/DCOMP, credito tributario, restituicao.
---

# RECUPERACAO DE CREDITOS

> Skill **Tier 4 — Tributario Consultivo** — identifica creditos tributarios recuperaveis,
> instrui a compensacao via PER/DCOMP e trata as restricoes do art. 166 CTN para tributos
> indiretos. Implementa PA-02, PA-03, PA-09, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "recuperar credito", "compensacao", "PER/DCOMP", "credito tributario",
"restituicao de tributo", "pagamento indevido", "aproveitamento de credito PIS/COFINS",
"tese tributaria para recuperar credito", "prescricao de credito tributario".

Entrega: mapa de creditos recuperaveis identificados + instrucao PER/DCOMP + tratamento
do art. 166 CTN + alertas de prazo prescricional.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `planejamento-tributario` (Tier 4), `reforma-tributaria-transicao` (Tier 4).
- **Entrega para:** `mitigacao-de-risco-fiscal` (Tier 4) se tese com risco de autuacao,
  `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar vigencia das normas do tributo
  alvo; Protocolo 1; prazo prescricional (PA-03).

---

## 2. IDENTIFICACAO DE CREDITOS RECUPERAVEIS

### 2.1 Categorias de credito

| Categoria | Exemplo | Prazo prescricional |
|-----------|---------|---------------------|
| Pagamento indevido | Tributo recolhido sem fato gerador | 5 anos contados do pagamento (CTN 168 I) |
| Pagamento a maior | Calculo errado ou aliquota majorada sem base legal | 5 anos contados do pagamento |
| Credito escritural nao aproveitado | Creditos de PIS/COFINS nao escriturados | 5 anos (restituicao) ou sem prescricao (compensacao escritural pendente — [VERIFICAR — prescricao do credito escritural e controversa no STJ; nao tratar como ausencia de prazo]) |
| Tese tributaria acolhida | Tese vinculante (STF/STJ) que gera credito retroativo | 5 anos antes do ajuizamento ou do pedido admin. (CTN 168; Sumula 328 STJ [VERIFICAR]) |

> **PA-03** — nunca cravar prazo prescricional como definitivo sem ressalva. Interrupoes e
> suspensoes (CTN 169, parcelamento, impugnacao) alteram a contagem. Verificar marco
> inicial aplicavel ao caso concreto `[VERIFICAR]`.

### 2.2 Tributos federais (competencia RFB)

**IRPJ/CSLL:** pagamento antecipado (estimativas mensais Lucro Real) superior ao IRPJ/CSLL
apurado no ajuste anual — saldo credor utilizavel como compensacao ou pedido de restituicao.

**PIS/COFINS nao-cumulativo:** creditos de insumos, depreciacoes, energia, alugueis, fretes
nao aproveitados em periodos anteriores. Verificar escrituracao correta na EFD-Contribuicoes.
[VERIFICAR regras de aproveitamento de saldo credor de PIS/COFINS apos extincao em 2026/2027
— LC 214/2025 deve conter disposicoes transitorias].

**Contribuicoes previdenciarias:** empresas com exclusao de parcelas indevidas da base de
calculo das contribuicoes (ex.: tercos de ferias, FGTS sobre aviso previo [VERIFICAR teses
vigentes em 2026]). Acionar levantamento por periodo.

**CSLL:** isencoes ou nao-incidencias setoriais [VERIFICAR se aplicavel ao setor do cliente].

### 2.3 Tributos estaduais e municipais

**ICMS:** credito acumulado por exportacoes (LC 87/96 — Lei Kandir: assegurado o credito nas
entradas mesmo quando a saida e isenta/nao-tributada pela exportacao); credito de ativo
permanente (1/48 avos por mes); credito presumido; transferencia de credito acumulado
[VERIFICAR regras do Estado do cliente].

**ISS:** pagamento indevido por incidencia em servico nao tributavel pelo municipio do
estabelecimento prestador [VERIFICAR competencia municipal — LC 116/03 + criterios STJ].

---

## 3. COMPENSACAO — PER/DCOMP

### 3.1 Mecanismo

A compensacao tributaria federal e realizada via **PER/DCOMP** (Pedido Eletronico de
Restituicao, Ressarcimento ou Reembolso e Declaracao de Compensacao), transmitida via
Programa PER/DCOMP Web (Portal e-CAC da RFB).

Base legal: CTN arts. 170-170-A + IN RFB 2.055/2021 (e alteracoes) `[VERIFICAR versao vigente]`.

### 3.2 Etapas do PER/DCOMP

1. **Levantamento do credito:** documentar cada periodo de competencia, valor pago, base de
   calculo, aliquota aplicada, comprovante de recolhimento (DARF/GPS/DAS).
2. **Pedido de restituicao (PER) ou declaracao de compensacao (DCOMP):**
   - PER: solicitar restituicao em dinheiro (sujeito a analise RFB, pode demorar anos).
   - DCOMP: declarar compensacao do credito com debito tributario vincendo — efeito
     imediato pendente de homologacao em 5 anos `[VERIFICAR prazo — IN RFB vigente]`.
3. **Documentacao de suporte:** SPED/EFD, DCTF, ECF, DARF, GPS, notas fiscais, laudos
   se houver tese tecnica.
4. **Monitoramento:** acompanhar situacao no e-CAC; responder notificacoes de RFB no prazo.

### 3.3 Vedacoes ao PER/DCOMP

Nao e possivel compensar:
- Credito de terceiros (salvo cessao permitida em lei — [VERIFICAR]).
- Creditos objeto de discussao judicial sem desistencia da acao.
- Debitos de FGTS (competencia CEF).
- Debitos inscritos em Divida Ativa da Uniao pendentes de parcelamento `[VERIFICAR]`.

> **PA-09** — o valor do credito apurado e uma estimativa ate a homologacao pela RFB (prazo
> de 5 anos). A RFB pode glosar parcialmente ou integralmente.

---

## 4. ART. 166 CTN — TRIBUTO INDIRETO E NAO-REPERCUSSAO

### 4.1 A regra

O CTN art. 166 condiciona a restituicao (ou compensacao) de tributo indireto a:
- **Prova de que o contribuinte assumiu o encargo** do tributo (nao repassou ao consumidor);
  OU
- **Autorizacao expressa** daquele a quem o encargo foi transferido (o consumidor final que
  suportou a carga).

### 4.2 O que e tributo indireto para fins do art. 166

Classicamente: ICMS e IPI (e PIS/COFINS no regime nao-cumulativo, segundo parte da
jurisprudencia — `[VERIFICAR posicao atual STJ]`). O ISS tambem pode ser tratado como
indireto dependendo do contexto contratual.

**Dificuldade pratica:** o contribuinte de direito (quem recolhe) usualmente repassa o tributo
no preco ao consumidor final. Para pedir restituicao/compensacao, precisa provar que NAO
repassou (assumiu o encargo) — o que e raro em operacoes de varejo.

### 4.3 Aplicacao em teses tributarias

Quando uma tese vitoriosa (ex.: exclusao do ICMS da base do PIS/COFINS — RE 574.706 STF)
gera credito em periodos passados, o contribuinte pessoa juridica que recolheu PIS/COFINS
sobre base maior pode pedir restituicao/compensacao — mas a RFB pode exigir prova de
nao-repercussao se entender que o tributo foi repassado ao consumidor.

**Solucao pratica:** para teses de pessoa juridica que calculou tributo sobre base incorreta
(ex.: ICMS erroneamente incluido), o entendimento majoritario e que o onus economico ficou
com a propria empresa contribuinte (nao com o consumidor final no caso de B2B). Mas ha
decisoes em sentido contrario `[VERIFICAR posicao atual STJ/TRFs no caso concreto]`.

> Registrar o risco de impugnacao pelo art. 166 na analise e orientar documentacao de
> suporte para afastar a argumentacao.

---

## 5. VEDACOES ESPECIFICAS

- **PA-02** — validar vigencia de IN RFB 2.055/2021 e suas alteracoes no ano do fato gerador.
- **PA-03** — nunca cravar prazo prescricional sem ressalva de interrupcoes e suspensoes.
- **PA-09** — todo valor de credito identificado e estimativa ate homologacao RFB.
- **PA-22** — toda instrucao e minuta de PER/DCOMP sujeita a revisao pelo advogado responsavel.

---

## 6. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — CTN 165-170-A; IN RFB vigente sobre PER/DCOMP;
  norma especifica do tributo alvo (PIS/COFINS, IRPJ, ICMS estadual).
- **Protocolo 3** (Jurisprudencial) — classificar a tese que fundamenta o credito
  (vinculante/em disputa/superada); verificar modulacao de efeitos.
- **Protocolo 4** (Competencia) — tributos federais: RFB (PER/DCOMP); estaduais: SEFAZ;
  municipais: Prefeitura.
- **Protocolo 5** (Calculo) — todo levantamento de credito e estimativa marcada.

---

## 7. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`planejamento-tributario` (Tier 4), `reforma-tributaria-transicao` (Tier 4).

**Entrega para:** `mitigacao-de-risco-fiscal` (Tier 4) se tese com risco de autuacao,
`suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** credito tributario prescrito por inacao; compensacoes realizadas sem
instrucao adequada (PER/DCOMP glosado); risco do art. 166 CTN nao avaliado — devolucao
negada pela RFB por nao-comprovacao de nao-repercussao.
