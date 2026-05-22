---
name: estrutura-internacional-empresarial
description: >
  Empresa estrangeira operando no Brasil: filial (exige autorizacao do Executivo Federal,
  CC 1.134-1.141) vs subsidiaria (PJ brasileira, sem decreto — modelo dominante). Tratados
  para evitar dupla tributacao (ADT/MLI/PPT). Compliance de capital estrangeiro (BACEN, CBE,
  RDE-IED). Nunca presta consultoria de direito estrangeiro — apenas sinaliza a necessidade
  de advogado no pais-sede. Aciona: empresa estrangeira, filial no Brasil, subsidiaria,
  capital estrangeiro, tratado de bitributacao, ADT.
---

# ESTRUTURA INTERNACIONAL EMPRESARIAL

> Skill **Tier 3 — Estruturacao Internacional** — orienta a entrada de empresa estrangeira no
> Brasil (filial vs subsidiaria), os acordos para evitar a dupla tributacao (ADT/MLI) e o
> compliance de capital estrangeiro perante o BACEN. Implementa PA-20, PA-21, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "empresa estrangeira", "filial no Brasil", "subsidiaria", "capital estrangeiro",
"tratado de bitributacao", "ADT", "MLI", "PPT", "BACEN", "RDE-IED", "CBE",
"empresa americana no Brasil", "empresa europeia no Brasil", "remessa ao exterior".

Entrega: comparativo filial vs subsidiaria + exigencias legais + mapa de ADTs relevantes +
checklist BACEN/CBE + sinalizacao de advogado no pais-sede (PA-20).

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `offshore-e-trust` (Tier 3) quando ha operacao comercial (nao so holding passiva).
- **Entrega para:** `constituicao-societaria` (Tier 2) se ha constituicao de subsidiaria,
  `registro-empresarial` (Tier 2), `mitigacao-de-risco-fiscal` (Tier 4),
  `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar CC 1.134-1.141 vigentes e
  ADT com o pais de origem; Protocolo 1.

---

## 2. FILIAL VS SUBSIDIARIA

### 2.1 Filial (ou sucursal) de empresa estrangeira no Brasil

**Base legal:** CC arts. 1.134-1.141.

- A filial **nao tem personalidade juridica propria** — e extensao da empresa estrangeira no
  Brasil.
- **Exige autorizacao do Executivo Federal** (decreto presidencial), concedida pelo
  Ministerio do Desenvolvimento, Industria e Comercio (MDIC) ou pelo ministerio competente
  conforme a atividade.
- Processo: requerimento com documentos da matriz, traducao juramentada, apostila ou
  reconhecimento consular; publicacao no DOU; registro na Junta Comercial apos autorizacao.
- A matriz responde integralmente pelas obrigacoes da filial no Brasil (CC 1.137).
- **Tributacao:** IRPJ e CSLL sobre o resultado apurado no Brasil (Lucro Real obrigatorio);
  remessas a matriz podem estar sujeitas a IRRF.

### 2.2 Subsidiaria (empresa brasileira controlada por estrangeira)

**Base legal:** CC 1.052-1.087 (LTDA) ou Lei 6.404/76 (S/A).

- A subsidiaria **tem personalidade juridica propria** — e uma PJ brasileira (LTDA, S/A ou
  outra) cujo controle pertence a estrangeira.
- **Nao exige autorizacao do Executivo Federal.** Constitui-se como qualquer empresa
  brasileira (contrato social ou estatuto, registro na Junta Comercial).
- Capital social pode ser integralizado com recursos vindos do exterior (aporte de capital
  estrangeiro), sujeito a registro no BACEN (RDE-IED).
- **Modelo dominante recomendado** para a maioria dos casos: processo mais rapido, sem decreto,
  menos burocracia.
- **Tributacao:** mesmas regras de qualquer empresa brasileira (IRPJ, CSLL, PIS/COFINS, ISS
  ou ICMS, conforme atividade e regime tributario escolhido).

### 2.3 Criterios de escolha

| Criterio | Filial | Subsidiaria |
|----------|--------|-------------|
| Personalidade juridica | Nao (extensao da matriz) | Sim (PJ brasileira) |
| Autorizacao federal | Sim (decreto) | Nao |
| Responsabilidade da matriz | Integral | Limitada ao capital |
| Velocidade de setup | Lenta (meses) | Mais rapida |
| Tributacao no Brasil | IRPJ/CSLL Lucro Real | Qualquer regime |
| Recomendacao geral | Casos especificos | Regra geral |

---

## 3. TRATADOS PARA EVITAR A DUPLA TRIBUTACAO (ADT)

### 3.1 O que e o ADT

Acordo bilateral entre o Brasil e outro pais para definir qual pais tributa cada tipo de renda
(dividendos, juros, royalties, ganhos de capital, salarios, servicos). Base: Modelo OCDE
ou Modelo ONU (Brasil usa variante propria).

**Numero de ADTs vigentes:** cerca de 36 acordos [VERIFICAR lista atualizada na RFB —
novos acordos podem ter sido ratificados].

**Metodo adotado pelo Brasil:** em geral, metodo do credito (o imposto pago no exterior e
creditado contra o IRPJ/IRRF no Brasil, ate o limite do imposto brasileiro).

### 3.2 MLI (Instrumento Multilateral) e PPT

O Brasil aderiu ao **MLI (Multilateral Instrument)** da OCDE para combate ao BEPS (Base
Erosion and Profit Shifting). O MLI incorpora o **PPT (Principal Purpose Test)**:
se o principal proposito de uma estrutura for obter beneficio do ADT sem substancia, o
beneficio pode ser negado.

**Implicacao pratica:** treaty shopping (criar entidade no pais A apenas para aproveitar o ADT
Brasil-A) e combatido. A estrutura deve ter substancia real no pais-sede do ADT.

### 3.3 Como aplicar

1. Identificar o pais de origem da empresa estrangeira.
2. Verificar se ha ADT Brasil-[pais] vigente ([VERIFICAR na lista RFB]).
3. Consultar a aliquota prevista no ADT para: dividendos, juros, royalties.
4. Comparar com a aliquota do IRRF interna (remessas sem ADT: IRRF 15% dividendos [VERIFICAR
   com Lei 15.270/2025], 15% juros, 15% royalties — sujeito a variacao).
5. Verificar PPT: a estrutura tem substancia no pais-sede?

---

## 4. COMPLIANCE DE CAPITAL ESTRANGEIRO

### 4.1 RDE-IED (Registro Declaratorio Eletronico — Investimento Estrangeiro Direto)

Todo aporte de capital estrangeiro na subsidiaria brasileira deve ser registrado no
SISBACEN (modulo RDE-IED). Base: Resolucao BCB [VERIFICAR numero atual].

- Prazo de registro: 30 dias apos o ingresso dos recursos.
- Sem registro: impossibilidade de remeter dividendos/lucros ao exterior e de repatriar
  o capital.
- Documentos: comprovante de ingresso de cambio, contrato social alterado, laudo de
  avaliacao (se integralizacao em bens).

### 4.2 CBE (Capitais Brasileiros no Exterior) e DCBE

Se a estrutura for inversa (empresa brasileira investindo no exterior), aplica-se o CBE.
Para a empresa estrangeira no Brasil, o BACEN monitora via RDE-IED e declaracoes periodicas.

### 4.3 Remessas ao exterior

- **Dividendos:** remessa ao socio estrangeiro — verificar IRRF aplicavel e ADT [VERIFICAR
  impacto da Lei 15.270/2025].
- **Juros sobre capital proprio (JCP):** IRRF 15%; pode ser usado como deducao no IRPJ;
  verificar limite.
- **Royalties:** IRRF; limite de deducao (Lei 4.131/62 e RIR [VERIFICAR artigos atuais]).
- **Servicos:** IRRF + CIDE (se envolver transferencia de tecnologia); verificar ADT.

---

## 5. PA-20 — DIREITO ESTRANGEIRO: SO SINALIZAR

> **ALERTA PA-20:** a constituicao da empresa estrangeira em seu pais de origem (governanca,
> autorizacao dos socios, poderes dos representantes, lei societaria local) e materia de
> **direito estrangeiro**. Este plugin NAO presta consultoria de direito estrangeiro.
>
> Este plugin apenas sinaliza: a empresa estrangeira deve contar com advogado licenciado no
> pais-sede para as questoes de direito local. O plugin analisa apenas o direito **brasileiro**
> aplicavel (CC, tributacao no Brasil, BACEN, ADT do lado brasileiro).

---

## 6. VEDACOES ESPECIFICAS

- **PA-20** — nunca opinar sobre constituicao, governanca, liquidacao ou compliance da empresa
  estrangeira em seu pais de origem. Apenas sinalizar.
- **PA-21** — nunca afirmar resultado fiscal garantido em estrutura internacional; nunca prometer
  economia tributaria definitiva via ADT ou arranjo filial/subsidiaria.
- **PA-22** — toda analise e minuta sujeita a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — CC 1.134-1.141; ADT do pais relevante [VERIFICAR];
  MLI/PPT; Resolucao BCB (RDE-IED) vigente.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — substancia economica no pais-sede; PPT.
- **Protocolo 4** (Competencia) — MDIC (autorizacao filial); Junta Comercial (registro);
  BACEN (RDE-IED, CBE); RFB (IRPJ, CSLL, IRRF); CVM (se S/A aberta).
- **Protocolo 6** (Internacional) — empresa estrangeira no Brasil → filial vs subsidiaria;
  ADT; BACEN/CBE; sinalizar direito do pais-sede.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `offshore-e-trust`.

**Entrega para:** `constituicao-societaria` (se subsidiaria nova), `registro-empresarial`,
`mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** empresa estrangeira operando no Brasil sem autorizacao federal (filial),
sem registro BACEN (capital irregular) e sem analise de ADT — exposicao a sancoes
administrativas e tributacao em duplicidade evitavel.
