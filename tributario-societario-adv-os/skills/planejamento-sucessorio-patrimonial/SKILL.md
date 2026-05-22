---
name: planejamento-sucessorio-patrimonial
description: >
  Planejamento sucessorio empresarial — holding familiar, doacao de quotas com reserva de
  usufruto, impacto do ITCMD progressivo (EC 132/2023, LC 227/2026), janela de planejamento.
  Nunca promete economia garantida de ITCMD nem afirma que a estrutura elimina a legitima dos
  herdeiros necessarios. Aciona: sucessao, heranca, doacao de quotas, holding familiar,
  planejamento sucessorio, usufruto, ITCMD progressivo.
---

# PLANEJAMENTO SUCESSORIO PATRIMONIAL

> Skill **Tier 3 — Estruturacao Patrimonial** — orienta o planejamento sucessorio empresarial
> via holding familiar, doacao de quotas com reserva de usufruto e gestao do ITCMD progressivo.
> Implementa PA-19, PA-21, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "sucessao", "heranca", "doacao de quotas", "holding familiar", "planejamento
sucessorio", "usufruto", "ITCMD progressivo", "doacao em vida", "transferencia de bens para
filhos", "blindagem sucessoria" (termo incorreto — ver secao 4.3).

Entrega: diagnostico sucessorio + mapa de instrumentos (holding familiar, doacao com usufruto,
testamento, acordo de socios) + impacto ITCMD + alertas de legitima e janela de planejamento.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `estruturacao-holdings` (Tier 3) quando o contexto e sucessorio.
- **Entrega para:** `estruturacao-holdings` (se a holding ainda nao foi estruturada),
  `governanca-e-acordos` (acordo de socios/acionistas familiar), `mitigacao-de-risco-fiscal`
  (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio em pareceres com impacto fiscal).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar EC 132/2023, LC 227/2026
  [VERIFICAR — confirmar promulgacao e numero oficial], CC 1.845-1.846 vigentes; Protocolo 1.

---

## 2. HOLDING FAMILIAR

### 2.1 Conceito e finalidade

Holding familiar e a sociedade (geralmente LTDA ou S/A fechada) que concentra o patrimonio
da familia (participacoes em empresas operacionais, imoveis, investimentos financeiros) e
permite: (a) gestao unificada do patrimonio; (b) planejamento sucessorio organizado;
(c) governanca com regras de entrada, saida e administracao.

**Nao e:** mecanismo de "blindagem" contra Receita, credores ou herdeiros necessarios (PA-21).

### 2.2 Constituicao

- Tipo societario: LTDA (mais flexivel para governanca familiar) ou S/A fechada (se ha planos
  de crescimento ou entrada de investidores).
- Capital: integralizacao dos ativos familiares (imoveis, participacoes) com laudo de avaliacao
  (S/A) ou deliberacao fundamentada (LTDA).
- Administracao: geralmente o(s) patriarca(s) ou genitor(es); acordo de socios regula a transicao.
- Substancia economica obrigatoria (ver `estruturacao-holdings` secao 4).

### 2.3 Doacao de quotas / acoes com reserva de usufruto

**Mecanismo:** o titular doa as quotas/acoes aos herdeiros (antecipacao da heranca), reservando
para si o usufruto (direito de administrar e receber os frutos — dividendos, JCP — durante a
vida). Os filhos ficam com a nua-propriedade.

**Vantagens:**
- Sucessao ocorre sem inventario para as quotas doadas.
- O doador mantem o controle de gestao e o recebimento dos dividendos via usufruto.
- ITCMD pode ser recolhido parceladamente, durante a vida, com a aliquota vigente no momento
  da doacao (evitar tributacao futura mais alta — ver secao 3).

**Cuidados:**
- A doacao e transmissao de bens — ITCMD incide no momento da doacao.
- O valor da quota/acao para fins de ITCMD e o valor de mercado ou patrimonial [VERIFICAR
  criterio adotado pela SEFAZ do estado — pratica varia].
- Doacao sem reserva de usufruto transfere tambem o controle — cuidado no acordo de socios.

---

## 3. ITCMD — IMPACTO E JANELA DE PLANEJAMENTO

### 3.1 Base legal

- **EC 132/2023:** determina que o ITCMD seja progressivo (aliquota aumenta com o valor da
  base de calculo). Estados tem prazo para adequar a legislacao.
- **LC 227/2026 [VERIFICAR — confirmar promulgacao e numero oficial]:** disciplina o ITCMD
  sobre bens no exterior, herancas e doacoes internacionais e trusts. Progressividade
  obrigatoria tambem para bens no exterior.
- Aliquotas: variam por Estado (de 2% a 8% — limite atual da Resolucao 09/1992 do Senado
  [VERIFICAR se o limite foi alterado]).
- **Progressividade obrigatoria pos EC 132/2023:** estados devem adequar suas leis; verificar
  a legislacao estadual do domicilio do doador/de cujus.

### 3.2 Janela de planejamento

**Enquanto os estados ainda estao adequando a legislacao para a progressividade**, pode haver
janela para realizar a doacao sob aliquotas menores (escalonamento). Mas:

- A janela e imprevisivel — depende de cada estado e da velocidade de promulgacao das novas
  leis.
- A consolidacao de doacoes sucessivas pode ser tratada pela lei estadual como uma unica base
  de calculo (anti-fracionamento). [VERIFICAR legislacao do estado do cliente]
- **PA-21:** este plugin nunca promete economia de ITCMD garantida. A janela e uma hipotese
  de planejamento sujeita a confirmacao da legislacao local vigente.

### 3.3 ITCMD sobre bens no exterior (LC 227/2026 [VERIFICAR])

Bens situados no exterior (participacoes em offshores, contas, imoveis), herancas de nao-
residentes e trusts passam a estar sujeitos ao ITCMD, segundo a LC 227/2026. [VERIFICAR
vigencia, regulamentacao e pratica dos estados]

Para estruturas com offshore ou trust, acionar tambem `offshore-e-trust` (Tier 3).

---

## 4. LEGITIMA E LIMITES INVIOLAVEIS

### 4.1 Herdeiros necessarios (CC 1.845-1.846)

Sao herdeiros necessarios: descendentes, ascendentes e conjuge (CC 1.845). A LEGITIMA
corresponde a metade do patrimonio do de cujus e e **indisponivel e inviolavel** (CC 1.846).
Nenhuma estrutura societaria elimina a legitima.

**Consequencias praticas:**
- Doacao em vida (antecipacao da heranca) nao elimina a legitima — e computada como adiantamento.
- Se a doacao ultrapassa a metade disponivel, os herdeiros necessarios podem postular a
  reducao (acao de colacao ou reducao de liberalidades — CC 2.004-2.012).
- Holding familiar com transferencia de todos os bens ao conjuge/socio pode ser atacada pelos
  filhos como reducao de legitima.

### 4.2 Colacao

Bens doados aos herdeiros necessarios sao colacionados ao monte-mor para igualar as legitimas
(CC 2.002). Se o testador dispensar a colacao, a dispensa vale so ate a parte disponivel.

### 4.3 O mito da "blindagem sucessoria" — PA-21

Holding familiar bem estruturada FACILITA a transferencia (sem inventario das quotas doadas)
e ORGANIZA a gestao, mas nao "blinda" contra:
- Acao de reducao de liberalidades por herdeiros necessarios.
- Acao de anulacao de doacao em fraude contra credores (CC 158-165).
- Imposto sucessorio (ITCMD incide sobre a heranca, inclusive quotas nao doadas).

**Este plugin nunca promete eliminar inventario total, zerar ITCMD ou excluir herdeiros necessarios.**

---

## 5. TESTAMENTO E INSTRUMENTOS COMPLEMENTARES

- **Testamento (CC 1.857-1.990):** valido para a parte disponivel (50% do patrimonio). Define
  distribuicao, nomeia testamenteiro, contem legados e condicoes. Nao substitui o planejamento
  em vida, mas o complementa.
- **Acordo de socios/acionistas familiar:** regras de entrada de quotas herdadas na holding,
  requisitos para novos socios (conjuges, netos), direito de preferencia, restricao de alienacao.
- **Previdencia privada (PGBL/VGBL):** VGBL nao entra no inventario (contrato de seguro)
  [VERIFICAR — incidencia de ITCMD sobre VGBL e contestada por alguns Estados];
  PGBL entra [VERIFICAR — entendimento em disputa no STJ].

---

## 6. VEDACOES ESPECIFICAS

- **PA-19** — nunca sugerir transferencia de bens para holding com finalidade de ocultar
  titularidade ou fraudar credores pre-existentes.
- **PA-21** — nunca afirmar que holding ou doacao "blinda" contra herdeiros necessarios ou
  Receita. Nunca prometer economia de ITCMD garantida.
- **PA-22** — estrutura sucessoria e minuta de doacao sujeitas a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — confirmar EC 132/2023, CC 1.845-1.846, LC 227/2026
  [VERIFICAR], legislacao estadual do ITCMD vigente.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — doacao antes do fato gerador; substancia da holding;
  transparencia perante RFB/BACEN.
- **Protocolo 3** (Jurisprudencial) — aliquotas ITCMD progressivas: estado de implementacao
  varia [VERIFICAR — em disputa no STJ/STF quanto ao momento de vigencia].
- **Protocolo 4** (Competencia) — ITCMD: competencia estadual; ITBI (imoveis): municipal;
  IRPJ (ganho de capital na holding): federal.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`estruturacao-holdings` (Tier 3).

**Entrega para:** `estruturacao-holdings` (se holding ainda nao constituida),
`offshore-e-trust` (se ha bens no exterior), `governanca-e-acordos`,
`mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** transferencia de patrimonio sem planejamento = inventario cheio, custas
elevadas, conflito entre herdeiros e ITCMD sem otimizacao possivel.
