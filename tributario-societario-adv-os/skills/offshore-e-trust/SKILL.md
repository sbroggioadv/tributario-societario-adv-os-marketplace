---
name: offshore-e-trust
description: >
  Offshore e trust sob a Lei 14.754/2023 — entidade controlada no exterior (lucro tributado
  a 15% anualmente, mesmo sem distribuicao), trust (transparencia fiscal: bens permanecem do
  instituidor ate distribuicao ou morte). Trata a COSIT 75/2025 (trust discretionario) como
  zona de litigio, nunca como regra pacifica. Nunca presta consultoria de direito estrangeiro.
  Nunca afirma blindagem contra Receita ou herdeiros. Aciona: offshore, trust, entidade no
  exterior, conta no exterior, planejamento internacional.
---

# OFFSHORE E TRUST

> Skill **Tier 3 — Estruturacao Internacional** — orienta o regime tributario de entidades
> controladas no exterior (offshore) e de trusts sob a Lei 14.754/2023 e IN RFB 2.180/2024,
> com tratamento rigoroso da COSIT 75/2025 como zona de litigio. Implementa PA-19, PA-20,
> PA-21, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "offshore", "trust", "entidade no exterior", "conta no exterior", "planejamento
internacional", "holding offshore", "BVI", "Cayman", "Delaware", "opcao de transparencia",
"beneficiario de trust", "trustee".

Entrega: mapa do regime fiscal brasileiro (Lei 14.754/2023) + obrigacoes de declaracao +
alertas COSIT 75/2025 + sinalizacao de advogado no pais-sede (PA-20).

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `estruturacao-holdings` (Tier 3) quando ha camada internacional, `planejamento-sucessorio-
  patrimonial` (Tier 3) quando ha bens no exterior.
- **Entrega para:** `estrutura-internacional-empresarial` (Tier 3) se ha operacao empresarial
  (nao so holding passiva), `mitigacao-de-risco-fiscal` (Tier 4),
  `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar Lei 14.754/2023 e IN RFB
  2.180/2024 vigentes e sem alteracao relevante; Protocolo 1.

---

## 2. OFFSHORE — ENTIDADE CONTROLADA NO EXTERIOR

### 2.1 Base legal

**Lei 14.754/2023 (arts. 1-6) + IN RFB 2.180/2024.**
Vigencia: exercicios a partir de 2024 (fatos geradores 2024+).

Fim do diferimento: o lucro da entidade controlada no exterior passa a ser tributado
**anualmente**, apurado em 31 de dezembro de cada exercicio, na DAA (Declaracao de Ajuste
Anual) do titular, independentemente de distribuicao efetiva ao Brasil.

### 2.2 Aliquota e base

- **Aliquota fixa: 15% sobre o lucro apurado.** [VERIFICAR vigencia — Lei 14.754/2023 + IN RFB 2.180/2024]
- Base: resultado contabil da entidade no exterior convertido para BRL na taxa PTAX de 31/12.
- Momento: no IRPF do titular (PF) ou no IRPJ/CSLL da controladora PJ, a depender de quem
  detem a participacao.

### 2.3 Quando a tributacao anual se aplica obrigatoriamente

Entidade controlada enquadrada em qualquer dos criterios da Lei 14.754/2023:
- (a) domiciliada em pais ou dependencia com tributacao favorecida (paraiso fiscal); ou
- (b) com renda ativa propria inferior a 60% da renda total.

Renda ativa: receitas de bens e servicos proprios da entidade (ex.: vendas, prestacao de
servicos). Renda passiva: dividendos, juros, royalties, ganhos de capital de participacoes.
Se renda ativa >= 60%, pode haver diferimento (verificar condicoes adicionais da lei e da IN
2.180/2024 [VERIFICAR]).

### 2.4 Opcao de transparencia fiscal (offshore)

A lei permite ao titular optar por tratar a entidade controlada como se fosse transparente
fiscalmente (ativos e passivos sao declarados diretamente na DAA do titular, em vez de como
participacao na offshore).

**ATENCAO: opcao de transparencia e IRREVOGAVEL** (Lei 14.754/2023, [VERIFICAR artigo exato]).
Uma vez exercida, nao pode ser desfeita. Decisao deve ser tomada com analise patrimonial
completa e assessoria fiscal especializada.

---

## 3. TRUST — REGIME FISCAL BRASILEIRO

### 3.1 Base legal

**Lei 14.754/2023 (arts. 10-13)** — primeira regulacao tributaria de trust no Brasil.
Trust nao tem personalidade juridica propria no direito brasileiro; e um arranjo contratual
reconhecido para fins fiscais.

### 3.2 Transparencia fiscal do trust

**Principio geral:** para fins do IRPF brasileiro, bens e direitos alocados em trust
**permanecem do instituidor** (settlor) ate que ocorra distribuicao efetiva ao beneficiario
ou ate o falecimento do instituidor.

- Enquanto vivos os bens no trust, o instituidor declara os ativos do trust em sua DAA como
  se fossem seus (Ficha de Bens e Direitos).
- Rendimentos gerados pelo trust sao tributados na DAA do instituidor, no momento em que
  auferidos pelo trust (independentemente de distribuicao ao beneficiario).

### 3.3 COSIT 75/2025 — ZONA DE LITIGIO (PA-21, Protocolo 3)

> **ALERTA CRITICO:** A Solucao de Consulta COSIT 75/2025 trata o trust discricionario de
> forma especifica — segundo o entendimento da Receita Federal nessa COSIT, o beneficiario de
> trust discricionario seria tributado desde a constituicao do trust (nao apenas na distribuicao).
>
> **Este entendimento e CONTROVERSO e deve ser tratado como zona de litigio:**
> - Ha posicoes doutrinarias divergentes sobre o momento do fato gerador no trust discricionario.
> - A COSIT 75/2025 pode ser questionada via consulta individual, impugnacao ou acao judicial.
> - **Este plugin NUNCA apresenta a COSIT 75/2025 como regra pacifica.** Sempre sinalizar:
>   `[VERIFICAR — COSIT 75/2025: entendimento controverso da RFB; tratar como tese em litigio
>   — recomendar consulta ao advogado tributarista especializado em trust antes de constituir
>   ou modificar a estrutura]`

### 3.4 Tipos de trust relevantes

- **Trust revogavel:** instituidor pode revogar; bens claramente permanecem do instituidor.
  Regime: transparencia fiscal plena (instituidor = titular fiscal).
- **Trust irrevogavel:** instituidor nao pode revogar; bens "saem" do seu patrimonio
  juridicamente. Para fins fiscais brasileiros, ainda assim sujeito ao regime da Lei 14.754/2023.
- **Trust discricionario:** trustee tem poder de decidir quando e quanto distribuir aos
  beneficiarios. Este e o ponto de controversia da COSIT 75/2025.
- **Trust determinado/fixo:** beneficiarios e suas quotas sao pre-definidas.

---

## 4. OBRIGACOES DE DECLARACAO E COMPLIANCE

### 4.1 DAA (Declaracao de Ajuste Anual — IRPF)

- Ficha de Bens e Direitos: offshore (participacao) e trust (ativos do trust).
- Ficha de Rendimentos: lucros tributados anualmente da offshore (GCAP ou tributacao especial).
- Prazo: abril de cada ano (DAA do exercicio anterior).

### 4.2 CBE (Capitais Brasileiros no Exterior) — BACEN

- Obrigados: residentes com ativos no exterior superiores a USD 1.000.000 (ou conforme regras
  da Circular BACEN vigente [VERIFICAR limite atual]).
- Declaracoes: anual (DCBE ate 5 de abril) e trimestral para patrimonio >= USD 100.000.000
  [VERIFICAR limites atuais].
- Trust e offshore devem ser declarados no CBE, com descricao do ativo, pais e valor.

### 4.3 CRS (Common Reporting Standard)

A maioria dos paises com jurisdicoes classicamente "offshore" (Cayman, BVI, Jersey, Luxemburgo,
Suica) assinou o CRS e envia dados de contas automaticamente para a RFB. A opacidade fiscal
e crescentemente limitada. Estruturas devem ser montadas assumindo que a RFB recebera informacoes.

### 4.4 ITCMD sobre trust — LC 227/2026 [VERIFICAR]

Segundo a LC 227/2026 [VERIFICAR — confirmar promulgacao e numero oficial], a distribuicao
de bens de trust ao beneficiario e tributavel pelo ITCMD. Verificar o momento do fato gerador
adotado pela legislacao estadual.

---

## 5. PA-20 — DIREITO ESTRANGEIRO: SO SINALIZAR

> **ALERTA PA-20:** a constituicao, governanca, sucessao e liquidacao do trust ou da offshore
> no pais-sede (Cayman, BVI, Delaware, Luxemburgo, Malta, etc.) e materia de **direito
> estrangeiro**. Este plugin NAO presta consultoria de direito estrangeiro.
>
> Este plugin apenas sinaliza: "a estruturacao da entidade no pais-sede requer advogado
> licenciado naquele pais". O plugin analisa apenas as implicacoes do direito **brasileiro**
> (Lei 14.754/2023, IN RFB 2.180/2024, BACEN-CBE, CRS, ITCMD).

---

## 6. VEDACOES ESPECIFICAS

- **PA-19** — nunca sugerir offshore ou trust com finalidade de ocultar titularidade ou
  sem substancia economica. CRS e e-Financeira monitoram.
- **PA-20** — nunca opinar sobre constituicao, governanca, sucessao ou liquidacao no pais-
  sede. Apenas sinalizar a necessidade de advogado local.
- **PA-21** — nunca afirmar que offshore ou trust "blinda" contra Receita ou herdeiros
  necessarios. Nunca tratar COSIT 75/2025 como regra pacifica.
- **PA-22** — toda estrategia e minuta sujeita a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — Lei 14.754/2023, IN RFB 2.180/2024, LC 227/2026
  [VERIFICAR], Circular BACEN (CBE) vigente.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — substancia economica; CRS; transparencia perante RFB.
- **Protocolo 3** (Jurisprudencial) — COSIT 75/2025: classificar como `[tese em litigio]`.
- **Protocolo 6** (Internacional) — offshore/trust → sinalizar advogado no pais-sede;
  verificar CBE/CRS; identificar regime Lei 14.754/2023.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`estruturacao-holdings`, `planejamento-sucessorio-patrimonial`.

**Entrega para:** `estrutura-internacional-empresarial` (se ha operacao comercial no exterior),
`tributacao-lucros-e-dividendos` (Tier 3) se ha distribuicao de lucros da offshore para o
Brasil, `mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** cliente com offshore ou trust sem conhecimento da tributacao anual (15%),
sem conformidade com CBE/CRS e exposto ao entendimento controvertido da COSIT 75/2025 sem
aviso de risco.
