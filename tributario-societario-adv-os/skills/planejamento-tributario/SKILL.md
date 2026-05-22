---
name: planejamento-tributario
description: >
  Analise comparativa de regimes tributarios (Simples Nacional, Lucro Presumido, Lucro Real)
  e modelagem de cenarios de carga tributaria. Raciocinio sempre datado pelo ano do fato
  gerador — inclui impacto da reforma tributaria (CBS/IBS). Nunca promete economia fiscal
  garantida. Aciona: planejamento tributario, qual regime, Simples ou presumido, reduzir
  impostos, carga tributaria, trocar de regime.
---

# PLANEJAMENTO TRIBUTARIO

> Skill **Tier 4 — Tributario Consultivo** — analisa e compara regimes tributarios (Simples
> Nacional, Lucro Presumido, Lucro Real) e constroi modelagem de cenarios de carga tributaria.
> Implementa PA-02, PA-06, PA-09, PA-21, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "planejamento tributario", "qual regime", "Simples ou Presumido", "Lucro Real ou
Presumido", "reduzir impostos", "carga tributaria", "trocar de regime", "opcao pelo regime",
"quanto pago de imposto em cada regime", "melhor regime para minha empresa".

Entrega: comparativo dos 3 regimes com carga estimada no ano do fato gerador + cenarios
modelados + alerta de impacto da reforma tributaria + recomendacao fundamentada.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `estruturacao-holdings` (Tier 3), `tributacao-lucros-e-dividendos` (Tier 3).
- **Entrega para:** `reforma-tributaria-transicao` (Tier 4) se contexto 2027+,
  `recuperacao-de-creditos` (Tier 4) se Lucro Real com creditos de PIS/COFINS,
  `mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar tetos vigentes (Simples e
  Lucro Presumido podem ser alterados por lei); Protocolo 1 + PA-06 (datar o fato gerador).

---

## 2. BALIZA TEMPORAL OBRIGATORIA (PA-06)

Antes de qualquer comparativo, datar o fato gerador:

```
Ano do fato gerador: [AAAA]
Regime tributario travado para esse ano: [Simples / Presumido / Real — ja optado ou a optar]
Tetos vigentes no ano: [VERIFICAR — podem ter sido atualizados por lei]
Impacto CBS/IBS: [aplicavel? — ver secao 5]
```

> **PA-06 — nunca aplicar aliquotas ou tetos sem datar o fato gerador.** Tetos do Simples
> Nacional e Lucro Presumido sao `[VERIFICAR]` a cada exercicio.

---

## 3. OS TRES REGIMES — COMPARATIVO

### 3.1 Simples Nacional (LC 123/2006)

**Acesso:** faturamento bruto anual ate R$ 4,8 milhoes [VERIFICAR teto vigente no ano].
Vedacoes: tipos societarios incompativeis (S/A, SCP sem opcao); atividades vedadas (LC 123
art. 17) [VERIFICAR regra completa do art. 17 LC 123/2006]; participacao societaria em outra PJ acima de 10% se a PJ participada ja e optante
e o conjunto supera o teto [VERIFICAR regra atual].

**Apuracao:** aliquotas progressivas por faixa de receita bruta, por Anexo (I a V). Aliquota
efetiva = (RBT12 x Aliq - PD) / RBT12.

**Incluidos no DAS (regime unificado):** IRPJ, CSLL, PIS, COFINS, IPI (quando aplicavel),
CPP (previdencia patronal), ICMS (se comercio/industria), ISS (se servico).

**Vantagens:** simplificidade; menor carga para pequenas empresas; apuracao mensal via DAS.
**Desvantagens:** sem aproveitamento de creditos de PIS/COFINS (regime cumulativo dentro do
Simples); sem deducao de despesas reais para IRPJ/CSLL; teto pode ser superado com crescimento.

**Aliquotas por Anexo (referencias de maio/2026 — [VERIFICAR faixas atualizadas]):**
- Anexo I (comercio): 4% a 19% (6 faixas)
- Anexo II (industria): 4,5% a 30% (6 faixas)
- Anexo III (servicos geral): 6% a 33% (6 faixas)
- Anexo IV (construcao civil, limpeza): 4,5% a 30% — sem CPP no DAS (INSS normal)
- Anexo V (servicos de alto valor): 15,5% a 30% (6 faixas)

> Aliquotas nominais acima sao referencias — confirmar tabelas do ano do fato gerador via
> Resolucao CGSN vigente `[VERIFICAR]`.

### 3.2 Lucro Presumido

**Acesso:** faturamento ate R$ 78 milhoes no ano anterior [VERIFICAR teto vigente].
Vedado para: obrigadas ao Lucro Real (financeiras, factoring, empresas com lucros/ganhos
no exterior, beneficiarias de reducao de IRPJ, etc. — RIR art. 257 [VERIFICAR redacao]).

**Apuracao:** IRPJ e CSLL calculados sobre base presumida (percentual da receita bruta):
- Comercio/industria: 8% (IRPJ) / 12% (CSLL).
- Servicos em geral: 32% (IRPJ e CSLL).
- Intermediacao: 32% (IRPJ) / 32% (CSLL).
- Atividades mistas: percentual por atividade.

**Aliquotas sobre a base presumida:** IRPJ 15% + adicional 10% sobre lucro que supere
R$ 20.000/mes [VERIFICAR valores]. CSLL 9%.

**PIS/COFINS:** regime cumulativo — 0,65% e 3% sobre receita bruta (sem creditos).

**Vantagens:** simplicidade na apuracao; previsibilidade se margem real > margem presumida.
**Desvantagens:** sem aproveitamento de prejuizo fiscal; PIS/COFINS cumulativo (sem creditos);
pode ser desvantajoso se margem real for muito inferior a presumida.

### 3.3 Lucro Real

**Obrigatorio para:** faturamento acima de R$ 78 milhoes [VERIFICAR]; financeiras; empresas
com lucros no exterior; beneficiarias de reducao de IRPJ. Opcional para demais.

**Apuracao:** IRPJ e CSLL calculados sobre o lucro contabil ajustado (adicoes, exclusoes e
compensacoes previstas no RIR). Aliquota IRPJ 15% + adicional 10% sobre excesso de
R$ 20.000/mes. CSLL 9%.

**PIS/COFINS nao-cumulativo:** 1,65% e 7,6% sobre receita bruta, com direito a creditos
(insumos, depreciacoes, energia, alugueis — Leis 10.637/02 e 10.833/03 [VERIFICAR]).

**Vantagens:** aproveitamento de prejuizo fiscal (30% do lucro por periodo); creditos de
PIS/COFINS; deducao de despesas reais; pode ser vantajoso para margens baixas.
**Desvantagens:** obrigacoes acessorias extensas (ECF, EFD-Contribuicoes, SPED); custo
contabil elevado; complexidade.

---

## 4. MODELAGEM DE CENARIOS

### 4.1 Dados necessarios para o modelo

```
Faturamento bruto anual estimado: R$ ___
Folha de pagamento mensal: R$ ___
Margem de lucro real estimada: ___%
Atividade principal (CNAE): ___
Insumos tributados (para credito PIS/COFINS no Real): R$ ___/ano
Regime atual (se ja optante): ___
Ano do fato gerador: ____
```

### 4.2 Template de comparativo (PA-09 — estimativas sujeitas a conferencia)

```
MODELAGEM DE CENARIOS — [empresa] — [ano]
Dados: Faturamento R$ ___ | Margem real ___% | Folha R$ ___/mes

REGIME          BASE CALC.     IRPJ/CSLL   PIS/COFINS   CPP/INSS   CARGA TOTAL
Simples (Anx _) Receita bruta  R$ ___      (incluso)    (incluso)  R$ ___  (___%)
Lucro Presumido Base pres. ___% R$ ___     R$ ___       R$ ___     R$ ___  (___%)
Lucro Real      Lucro ajustado R$ ___      R$ ___ - cred R$ ___    R$ ___  (___%)

ESTIMATIVA — sujeita a conferencia contabil e fiscal. PA-09.
```

### 4.3 Fatores qualitativos

Alem da carga numerica, considerar:
- Custo de compliance (Lucro Real > Presumido > Simples).
- Necessidade de credito tributario (Lucro Real vantajoso para insumos elevados).
- Planejamento de distribuicao de dividendos (ver skill `tributacao-lucros-e-dividendos`).
- Crescimento projetado — risco de superar teto do Simples ou do Presumido.
- Regime da reforma tributaria no ano: CBS/IBS (ver secao 5).

---

## 5. IMPACTO DA REFORMA TRIBUTARIA (PA-06)

A modelagem de carga tributaria DEVE considerar o regime vigente no ano do fato gerador:

| Ano | Regime PIS/COFINS | Observacao |
|-----|------------------|------------|
| 2026 | PIS/COFINS vigentes; CBS 0,9% / IBS 0,1% destacados (sem cobranca) | Modelagem normal 2026 |
| 2027 | CBS cheia. PIS e COFINS EXTINTOS. | Refazer modelo com CBS |
| 2028+ | Transicao CBS/IBS — [VERIFICAR percentuais na LC 214/2025] | Atualizar anualmente |

> **Para anos 2027+, acionar `reforma-tributaria-transicao` (Tier 4)** antes de fechar o
> comparativo de regimes, pois as aliquotas de PIS/COFINS (extintos) e CBS/IBS alteram
> materialmente o calculo.

> **PA-06** — nunca modelar cenarios sem travar o regime tributario do ano.

---

## 6. VEDACOES ESPECIFICAS

- **PA-02** — validar vigencia das aliquotas, tetos e anexos do Simples no ano do fato gerador.
- **PA-06** — nunca aplicar regime sem datar o fato gerador e travar o regime do ano.
- **PA-09** — todo valor monetario estimado na modelagem e sujeito a conferencia contabil.
- **PA-21** — nunca prometer economia fiscal garantida; modelagem e cenario, nao certeza.
- **PA-22** — toda analise e minuta sujeita a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — confirmar tetos e aliquotas vigentes no ano; LC 123/2006
  e IN CGSN vigente para Simples; RIR para Presumido e Real; Leis 10.637/02 e 10.833/03.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — opcao tributaria deve ter proposito negocial
  real; nao configurar planejamento abusivo.
- **Protocolo 4** (Competencia) — IRPJ/CSLL/PIS/COFINS: federal (RFB); ICMS: estadual
  (impacto no DAS Simples); ISS: municipal.
- **Protocolo 5** (Calculo) — toda estimativa marcada como sujeita a conferencia.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`estruturacao-holdings`, `tributacao-lucros-e-dividendos`.

**Entrega para:** `reforma-tributaria-transicao` (Tier 4) se fato gerador 2027+,
`recuperacao-de-creditos` (Tier 4) se Lucro Real com creditos identificados,
`mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** empresa operando no regime errado — carga tributaria desnecessariamente
alta ou compliance incompativel com o porte e atividade da empresa.
