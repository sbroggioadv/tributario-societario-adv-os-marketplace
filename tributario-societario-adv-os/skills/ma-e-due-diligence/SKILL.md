---
name: ma-e-due-diligence
description: >
  M&A: SPA, MOU, term sheet, due diligence legal e clausulas (reps e warranties, MAC,
  earnout, escrow, indenizacao com caps e survival). Orienta a sequencia pre-contratual
  (MOU/LOI), due diligence (checklist e red flags) e contrato definitivo (SPA). Aciona:
  M&A, compra de empresa, due diligence, SPA, venda de participacao, fusao e aquisicao.
---

# M&A E DUE DILIGENCE

> Skill **Tier 2 — Societario** — orienta o processo de M&A desde MOU/LOI ate o SPA definitivo,
> com foco em due diligence legal e clausulas criticas de SPA. Implementa PA-04, PA-18, PA-22.
> Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "M&A", "compra de empresa", "venda de empresa", "due diligence", "SPA", "venda
de participacao", "term sheet", "MOU", "LOI", "fusao e aquisicao", "aquisicao de controle",
"reps and warranties", "earnout", "escrow", "indenizacao M&A".

Entrega: mapa do processo de M&A + checklist de due diligence legal + orientacao sobre
clausulas criticas de SPA.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `reorganizacao-societaria`,
  `governanca-e-acordos`.
- **Entrega para:** `reorganizacao-societaria`, `governanca-e-acordos` (pos-M&A),
  `planejamento-tributario` (Tier 4), `mitigacao-de-risco-fiscal` (Tier 4),
  `suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar LSA, CC, CTN, Lei 12.529/2011 vigentes.

---

## 2. FLUXO DO PROCESSO DE M&A

```
NDA → MOU / LOI / Term Sheet → Due Diligence → Negociacao → Signing (SPA)
→ Condicoes Precedentes → Closing → Pos-Closing (earnout, escrow, survival)
```

---

## 3. PRE-CONTRATUAL — NDA, MOU E TERM SHEET

**NDA (confidencialidade):** primeiro instrumento. Cobre definicao de informacao confidencial,
obrigacoes das partes, excecoes, prazo (2-3 anos), penalidade, non-solicitation de funcionarios
(prazo com PA-18).

**MOU / LOI / Term Sheet:** pre-contratuais, em regra **nao-vinculantes** quanto ao preco e
condicoes definitivas.

**Clausulas vinculantes mesmo em instrumentos nao-vinculantes:**
- Exclusividade (lock-out): vendedor nao negocia com terceiros no periodo.
- Confidencialidade.
- Obrigacao de boa-fe nas negociacoes.
- Responsabilidade pelos custos de due diligence.

**Conteudo minimo do term sheet:** estrutura da operacao (share deal vs asset deal; % de
aquisicao); preco indicativo; mecanismo de ajuste (locked box ou completion accounts);
forma de pagamento; exclusividade; condicoes precedentes (CADE, autorizacoes regulatorias);
cronograma.

---

## 4. DUE DILIGENCE LEGAL — CHECKLIST E RED FLAGS

### 4.1 Estrutura societaria
Contratos sociais/estatutos + todas as alteracoes · livros de atas e registros de acoes/quotas
· acordos de socios · organograma societario completo.

### 4.2 Contratos relevantes
Locacao (prazo, multa, cessao) · fornecedores/clientes · financiamentos e garantias ·
licencas e autorizacoes operacionais · contratos de IP.
> **Red Flag:** **clausula de change of control** — pode ensejar rescisao ou vencimento
> antecipado. Mapear TODOS os contratos com essa clausula antes do signing.

### 4.3 Trabalhista
Numero de funcionarios e terceirizados · passivo trabalhista (TRT, FGTS, INSS) · acordos
coletivos · PLR/bonus pre-existentes · irregularidades (pejotizacao, terceirizacao ilicita).
> **Red Flag:** muitas reclamacoes trabalhistas = passivo oculto. Pedir certidao do TRT.

### 4.4 Tributario
Certidoes negativas (federal, estadual, municipal, FGTS) · autos de infracao em andamento ·
parcelamentos vigentes · passivo fiscal oculto · conformidade com o regime tributario adotado.
> **Red Flag:** CND pendente ou auto de infracao em fase final = passivo certo. Negociar
> retencao em escrow ou abatimento de preco.

### 4.5 Ambiental e regulatorio
Licencas ambientais vigentes e transferiveis · passivo ambiental (areas contaminadas, TAC) ·
autorizacao setorial pos-aquisicao (BACEN, ANATEL, ANEEL, ANVISA).
**CADE (Lei 12.529/2011):** verificar se a operacao atinge os limiares para notificacao
obrigatoria (art. 88 — R$ 750mi e R$ 75mi [VERIFICAR valores vigentes]).

### 4.6 Propriedade intelectual
Marcas no INPI (titularidade, validade) · patentes · software (titularidade do codigo,
licencas de terceiros) · dominios e redes sociais.
> **Red Flag:** IP relevante registrado no nome do fundador PF (nao da PJ) = risco de litigio.

---

## 5. SPA — CLAUSULAS CRITICAS

### 5.1 Reps & Warranties (Declaracoes e Garantias)

Declaracoes do vendedor sobre o estado da empresa no signing/closing. Cobrem: situacao
societaria, financeira, tributaria, trabalhista, contratos, IP, conformidade legal.

**Disclosure Letter:** o vendedor lista excecoes conhecidas. Risco divulgado = excluido de
indenizacao futura.
**Knowledge qualifier:** algumas reps limitadas "ao melhor conhecimento do vendedor" —
negociar escopo (so diretores? toda a organizacao?).
**Materiality threshold:** violacao so gera indenizacao se superar determinado valor (1-2% do
preco de aquisicao).

### 5.2 MAC — Material Adverse Change

Permite ao comprador desistir se evento relevante negativo ocorrer entre signing e closing.
**Excecoes da definicao:** condicoes gerais de mercado, guerra, pandemia, alteracoes legais
aplicaveis a toda a industria — nao sao MAC especifica da empresa.
MAC acionavel: queda de receita acima de X%, perda de cliente-chave, passivo descoberto acima de Y.

### 5.3 Earnout

Pagamento diferido condicionado a desempenho pos-closing.
**Estrutura tipica:** preco base no closing + parcelas condicionadas a EBITDA/receita/metas
por 2-3 anos.
**Pontos criticos:** definir metricas com precisao (EBITDA ajustado ou reportado? quais
politicas contabeis?); autonomia operacional do vendedor-gestor durante o earnout;
direito de auditoria do vendedor nos calculos.
Tratamento fiscal: ganho de capital ou rendimento? [VERIFICAR posicao RFB].

### 5.4 Escrow

Retencao de parte do preco (10-20% e comum) em conta garantia por periodo de survival
(12-36 meses), para cobrir indenizacoes por reps quebradas descobertas apos o closing.
Clausulas do escrow: valor retido e prazo; condicoes de liberacao; resolucao de disputas
(arbitragem); remuneracao (juros/CDI — para quem?).

### 5.5 Indenizacao — Caps e Survival

**Survival period:** prazo de exigibilidade das reps apos o closing.
- Reps gerais: 12-24 meses.
- Reps tributarias: ate 5 anos (prazo decadencial CTN).
- Reps ambientais e trabalhistas: 5-10 anos.
- Reps de titularidade/organizacao societaria: podem ser perpetuas.

**Cap:** valor maximo de responsabilidade do vendedor (10-100% do preco, conforme risco).
**Basket:** o vendedor so e acionado se perdas acumuladas superarem determinado valor (ex.:
1% do preco). **Tipping basket:** atingido o threshold, responde por tudo desde o primeiro real.
**Deductible:** responde apenas pelo excedente.

### 5.6 Nao-concorrencia no SPA (PA-18)

**Tres elementos obrigatorios:** prazo maximo (em contexto de M&A o mercado aceita ate 3 anos; em acordos de socios comuns o padrao e 1-2 anos), territorio e atividade.
Preco que inclui nao-concorrencia pode ter tratamento fiscal especifico — acionar
`planejamento-tributario` (Tier 4).

---

## 6. SHARE DEAL VS. ASSET DEAL

| Criterio | Share Deal | Asset Deal |
|---------|-----------|-----------|
| O que se adquire | Participacao societaria (PJ com passivos) | Ativos especificos |
| Passivos ocultos | Assumidos via reps/indenizacao | Nao assumidos (em regra) |
| Tributacao vendedor | Ganho de capital sobre quotas/acoes | Ganho de capital + IRPJ/CSLL/PIS/COFINS |
| Preferencia comprador | Asset deal (evita passivos) | — |
| Preferencia vendedor | Share deal (ganho de capital) | — |

---

## 7. VEDACOES ESPECIFICAS

- **PA-04** — nunca inventar clausula de SPA, precedente de CADE ou tese tributaria de earnout.
  Se incerto, marcar como [VERIFICAR].
- **PA-18** — nao-concorrencia no SPA: prazo, territorio e atividade obrigatorios.
- **PA-22** — toda minuta (MOU, term sheet, NDA, SPA) sujeita a revisao pelo advogado responsavel.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** — confirmar LSA 118, 254-A, CC, Lei 12.529/2011 vigentes; limiares CADE.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — due diligence como identificacao de risco; disclosure letter como protecao.
- **Protocolo 4** — CADE (federal); Junta Comercial (transferencia de quotas/acoes); RFB (ganho
  de capital).
- **Protocolo 5** — earnout, ajuste de preco e passivos sao estimativas; nunca apresentar como
  definitivo.

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, operador direto.

**Entrega para:** `reorganizacao-societaria`, `governanca-e-acordos` (pos-closing),
`planejamento-tributario` (Tier 4), `mitigacao-de-risco-fiscal` (Tier 4),
`suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).

**Sem esta skill:** M&A sem due diligence — risco de assumir passivos ocultos (trabalhista,
tributario, ambiental) e clausulas de SPA sem protecao adequada.
