---
name: reforma-tributaria-transicao
description: >
  Assistente da transicao CBS/IBS/Imposto Seletivo — coexistencia do regime antigo
  (PIS/COFINS/ICMS/ISS) e novo, sempre datada pelo ano do fato gerador (cronograma
  2026-2033). Percentuais de transicao 2029-2032 sao disputados — usa [VERIFICAR].
  Trata split payment, creditos de PIS/COFINS pre-extincao e impacto em holdings.
  Aciona: reforma tributaria, CBS, IBS, imposto seletivo, transicao tributaria, split
  payment, quando acaba o ICMS, quando acaba ISS.
---

# REFORMA TRIBUTARIA TRANSICAO

> Skill **Tier 4 — Tributario Consultivo** — orienta a transicao do sistema tributario
> vigente (PIS/COFINS/ICMS/ISS) para o modelo CBS+IBS+Imposto Seletivo, datando o
> raciocinio pelo ano do fato gerador. Base normativa: EC 132/2023 + LC 214/2025.
> Implementa PA-02, PA-06, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "reforma tributaria", "CBS", "IBS", "imposto seletivo", "transicao tributaria",
"split payment", "quando acaba ICMS", "quando acaba ISS", "quando acaba PIS/COFINS",
"como fica minha empresa com a reforma", "CBS cheia 2027", "LC 214".

Entrega: cronograma datado por ano do fato gerador + coexistencia de regimes em cada ano
+ impacto CBS/IBS nos setores + split payment + alertas de incerteza normativa.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `planejamento-tributario` (Tier 4), `recuperacao-de-creditos` (Tier 4).
- **Entrega para:** `planejamento-tributario` (Tier 4) para refazer modelagem 2027+,
  `mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar LC 214/2025 vigente e
  regulamentacoes infralegais mais recentes; Protocolo 1; PA-06 (datar o fato gerador).

---

## 2. BALIZA OBRIGATORIA: ANO DO FATO GERADOR (PA-06)

Todo raciocinio desta skill parte do ano do fato gerador, nao de "hoje":

```
REFORMA TRIBUTARIA — BALIZA TEMPORAL
Ano do fato gerador: [AAAA]
Regime aplicavel no ano: [ver tabela secao 3]
Incerteza normativa: LC 214/2025 tem regulamentacoes infralegais pendentes [VERIFICAR]
```

> **PA-06** — NUNCA aplicar regime tributario sem datar o fato gerador. O raciocinio juridico
> e o modelo financeiro mudam radicalmente dependendo do ano.

---

## 3. CRONOGRAMA DA TRANSICAO (EC 132/2023 + LC 214/2025)

### 3.1 Tabela por ano do fato gerador

| Ano | Regime vigente | Eventos criticos |
|-----|---------------|-----------------|
| **2026** | Ano-teste. CBS 0,9% e IBS 0,1% sao destacados nas notas fiscais mas SEM cobranca efetiva. PIS/COFINS integrais. ICMS e ISS integrais. | Empresas devem destacar CBS/IBS mesmo sem pagar — obrigacao acessoria. |
| **2027** | **CBS cheia. PIS e COFINS EXTINTOS.** IPI zerado (exceto ZFM). Imposto Seletivo passa a ser cobrado sobre bens prejudiciais. ICMS e ISS permanecem. | Virada grande — modelos de credito PIS/COFINS migram para CBS. |
| **2028** | CBS consolidada. ICMS e ISS permanecem integrais. IBS em aliquota-teste. | Coexistencia CBS + ICMS/ISS. |
| **2029-2032** | Transicao gradual IBS/ICMS/ISS. IBS sobe, ICMS e ISS descem em percentuais anuais. | **Percentuais exatos: [VERIFICAR percentuais na LC 214/2025]** — sao disputados e sujeitos a regulamentacao infralegal. |
| **2033** | ICMS e ISS extintos. Modelo pleno CBS+IBS+IS. | Reforma concluida. |

> **Alerta de incerteza:** os percentuais da transicao 2029-2032 constam da LC 214/2025 mas
> regulamentacoes infralegais ainda estavam pendentes em maio/2026. **Nao cravar percentuais
> anuais sem confirmar na fonte oficial** `[VERIFICAR percentuais na LC 214/2025]`.

### 3.2 Natureza juridica dos tributos

**CBS (Contribuicao sobre Bens e Servicos):** substitui PIS e COFINS. Competencia federal.
Nao-cumulativa por design. Base ampla. Aliquota referencia a ser definida em regulamento
`[VERIFICAR aliquota de referencia CBS na LC 214/2025]`.

**IBS (Imposto sobre Bens e Servicos):** substitui ICMS e ISS. Competencia dual
(estados + municipios), gerido pelo Comite Gestor do IBS. Nao-cumulativo. Aliquota = soma
de aliquota estadual + aliquota municipal. Cada ente fixa sua propria aliquota dentro de
regras do Comite `[VERIFICAR aliquotas referenciais por Estado/municipio quando disponibilizadas]`.

**Imposto Seletivo (IS):** incide sobre bens e servicos prejudiciais a saude ou ao meio
ambiente (cigarros, bebidas alcoolicas, veiculos, armamentos, etc.). Competencia federal.
Monofasico. Nao gera credito para outros tributos.

---

## 4. COEXISTENCIA DE REGIMES (2026-2032)

### 4.1 O que coexiste e quando

No periodo de transicao, podem coexistir obrigacoes de **dois sistemas tributarios simultaneos**:
- Apurar e recolher PIS/COFINS (ate 2026 inclusive) E destacar CBS/IBS (2026 sem cobranca).
- A partir de 2027: CBS substitui PIS/COFINS; ICMS/ISS permanecem ate 2032 decrescendo.
- Creditos de PIS/COFINS existentes em 31/12/2026: verificar regras de aproveitamento pelo
  regime CBS `[VERIFICAR regras de credito remanescente na LC 214/2025]`.

### 4.2 Creditos de PIS/COFINS pre-extincao

Saldos credores de PIS/COFINS apurados ate 31/12/2026 (ultimo exercicio com esses tributos):
- Regras de compensacao/ressarcimento pre-extincao ou conversao em credito CBS
  `[VERIFICAR disposicoes transitorias da LC 214/2025]`.
- Prazo para aproveitamento: `[VERIFICAR]`.
- Acionar `recuperacao-de-creditos` (Tier 4) para instrucao de PER/DCOMP se aplicavel.

### 4.3 Obrigacoes acessorias no periodo de transicao

- Ano-teste 2026: destacar CBS e IBS nas NF-e mesmo sem cobranca.
- SPED/EFD-Contribuicoes: verificar formato de escrituracao durante transicao
  `[VERIFICAR instrucoes RFB e Comite IBS]`.
- Faturamento internacional: CBS incide sobre importacoes; verificar credito na cadeia.

---

## 5. SPLIT PAYMENT

### 5.1 O que e

Mecanismo pelo qual o valor dos tributos (CBS/IBS) e retido automaticamente no momento do
pagamento da nota fiscal, antes de chegar ao fornecedor. O pagador (adquirente) segrega
automaticamente o tributo embutido no preco e o recolhe diretamente ao Fisco.

### 5.2 Impacto pratico

- **Fluxo de caixa do fornecedor:** recebe o valor liquido de tributo imediatamente. Nao ha
  mais o intervalo entre o faturamento e o recolhimento — o tributo nunca entra no caixa
  do fornecedor.
- **Credito do adquirente:** o comprovante de recolhimento via split payment e a prova do
  credito de CBS/IBS `[VERIFICAR mecanismo de comprovacao na LC 214/2025]`.
- **Inadimplencia tributaria:** o split payment, em tese, elimina a possibilidade de uso
  do tributo como capital de giro antes do vencimento.
- **Operacionalizacao:** depende de regulamentacao da infraestrutura bancaria e da RFB/Comite IBS
  `[VERIFICAR cronograma de implementacao do split payment]`.

---

## 6. IMPACTO SETORIAL — PONTOS DE ATENCAO

### 6.1 Servicos

ISS (municipal, ate 5%) sera substituido por IBS (municipal + estadual). Para prestadores de
servico, a transicao pode ser complexa pois hoje ISS e calculado sobre preco bruto (cumulativo)
e IBS sera nao-cumulativo. Verificar impacto na precificacao e nos contratos de longo prazo.

### 6.2 Comercio e industria

ICMS substituido por IBS. O ICMS hoje tem muitas isencoes e beneficios fiscais estaduais
(guerra fiscal) — esses beneficios serao gradualmente extintos na transicao. Verificar
impacto nos beneficios fiscais ICMS vigentes `[VERIFICAR tratamento de beneficios fiscais
estaduais na transicao — LC 214/2025 e negociacoes com estados]`.

### 6.3 Holdings e grupos empresariais

A holding pura que recebe dividendos (isentos ou tributados conforme Lei 15.270/2025 [VERIFICAR vigencia]) nao e
diretamente impactada pela CBS/IBS (que incidem sobre operacoes com bens e servicos). Mas
holdings mistas com atividade propria (aluguel, royalties, servicos de gestao) devem analisar
a substituicao de ISS/ICMS pelo IBS em cada atividade.

---

## 7. VEDACOES ESPECIFICAS

- **PA-02** — validar vigencia de LC 214/2025 e regulamentacoes infralegais no ano do fato
  gerador; a reforma e um alvo movel.
- **PA-06** — nunca aplicar regime CBS/IBS sem datar o fato gerador; a resposta correta
  depende totalmente do ano.
- **PA-22** — toda analise e minuta sujeita a revisao pelo advogado responsavel.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — EC 132/2023 + LC 214/2025 vigentes; regulamentacoes
  infralegais pendentes [VERIFICAR]; cronograma pode ter alteracoes por MP ou lei.
- **Protocolo 4** (Competencia) — CBS: federal (RFB); IBS: dual (estados + municipios, Comite IBS);
  IS: federal.
- **Protocolo 5** (Calculo) — qualquer projecao de carga tributaria pos-reforma e estimativa
  marcada, sujeita a conferencia quando aliquotas forem regulamentadas.

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`planejamento-tributario` (Tier 4), `recuperacao-de-creditos` (Tier 4).

**Entrega para:** `planejamento-tributario` (Tier 4) para refazer modelagem com CBS/IBS,
`mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** empresa modelando carga tributaria com PIS/COFINS para fatos geradores
2027+ — erro material que invalida o planejamento e os contratos de longo prazo.
