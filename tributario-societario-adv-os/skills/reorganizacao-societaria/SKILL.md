---
name: reorganizacao-societaria
description: >
  Transformacao, incorporacao, fusao e cisao: protocolo, justificacao e intersecao
  tributaria (agio, prejuizo fiscal, proposito negocial). Nunca estrutura agio artificial
  nem promete aproveitar prejuizo fiscal da incorporada. Aciona: incorporacao, fusao, cisao,
  transformar empresa, reorganizacao societaria, protocolo de reorganizacao.
---

# REORGANIZACAO SOCIETARIA

> Skill **Tier 2 — Societario** — orienta as 4 modalidades de reorganizacao (transformacao,
> incorporacao, fusao, cisao), o protocolo/justificacao obrigatorios e a intersecao fiscal
> critica. Implementa PA-13, PA-14, PA-16, PA-17, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "incorporacao", "fusao", "cisao", "transformar empresa", "reorganizacao",
"protocolo de reorganizacao", "cisao parcial", "spin-off", "transformar LTDA em SA".

Entrega: mapa das 4 operacoes + protocolo/justificacao + analise tributaria (agio × prejuizo
fiscal × proposito negocial) + alertas PA-16/PA-17.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `planejamento-tributario`
  (Tier 4) quando a reorganizacao tem motivacao fiscal.
- **Entrega para:** `registro-empresarial`, `mitigacao-de-risco-fiscal` (Tier 4),
  `estruturacao-holdings` (Tier 3) se contexto holding, `suprema-corte-empresarial`
  (R1-R4 obrigatorio em analises com impacto fiscal).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar CC 1.113-1.122 e LSA 220-234
  vigentes; Protocolo 1 emitir Selo.

---

## 2. AS 4 OPERACOES DE REORGANIZACAO

### 2.1 Transformacao (CC 1.113-1.115; LSA 220-222)

Mudanca de tipo societario sem dissolucao — a PJ permanece (mesmo CNPJ). Ex.: LTDA → S/A.
**Quorum:** unanimidade, salvo clausula contraria (CC 1.114; LSA 221 — dissidente pode retirar).
**Documentos:** deliberacao (ata/reuniao); novo contrato social ou estatuto; arquivamento Junta.

### 2.2 Incorporacao (LSA 227; CC 1.116)

Incorporadora absorve a incorporada, que se extingue. Patrimonio (ativo e passivo) transfere
para a incorporadora. Socios da incorporada recebem participacao na incorporadora ou reembolso.
**Quorum (S/A):** AGE de ambas; maioria absoluta (LSA 136); dissidentes tem direito de retirada.
**Documentos:** protocolo de incorporacao; justificacao; laudo de avaliacao; deliberacao das AGEs;
certidao de baixa da incorporada na Junta.

### 2.3 Fusao (LSA 228; CC 1.119)

Todas as sociedades fusionadas se extinguem e uma nova PJ e criada.
**Base legal:** LSA 228 (S/A); CC 1.119 (LTDA).
**Documentos:** protocolo; justificacao; laudo de avaliacao de cada patrimonio; deliberacoes
das AGEs; registro de constituicao da nova sociedade + baixa das extintas.

### 2.4 Cisao (LSA 229; aplicacao analogica para LTDA)

Transferencia de parcelas do patrimonio para nova(s) sociedade(s).
- **Total:** a cisandada se extingue; todo patrimonio vai para novas sociedades.
- **Parcial (spin-off):** a cisandada permanece com parte; outra parte vai para nova sociedade.
Responsabilidade solidaria das resultantes pelas obrigacoes da cisandada, salvo rateio expresso
e publicacao (LSA 233).
**Documentos:** protocolo; justificacao; laudo; deliberacao da AGE; arquivamento Junta.

---

## 3. PROTOCOLO E JUSTIFICACAO

**Protocolo (LSA 224):** obrigatorio para incorporacao/fusao/cisao de S/A. Conteudo minimo:
relacao de troca de acoes, criterios de avaliacao do patrimonio, direitos dos dissidentes,
prazo da operacao, data-base do balanco.

**Justificacao:** expoe o **proposito negocial legitimo** — eficiencia operacional, acesso a
capital, reducao de sobreposicao societaria, sucessao, saida de socio. Documento-chave para
defesa perante RFB/CARF.

**Laudo de avaliacao:** perito ou empresa especializada; patrimonio a valores de mercado.

**Direito de retirada (recesso):** socio dissidente de reorganizacao tem direito de recesso.
S/A: reembolso pelo valor patrimonial das acoes, prazo 30 dias apos publicacao (LSA 137).
LTDA: aplicacao analogica [VERIFICAR posicao doutrinaria/jurisprudencial].

---

## 4. INTERSECAO TRIBUTARIA CRITICA

### 4.1 Agio e amortizacao fiscal

**Agio legitimo:** diferenca paga acima do valor patrimonial, justificada por rentabilidade
futura real, com laudo fundamentado, adquirida de terceiro independente. Amortizavel via
incorporacao genuina apos registro contabil correto.

**Agio artificial / "agio interno" — VEDADO (PA-16):** operacao estruturada sem terceiro
independente para gerar o agio (holding criada ad hoc apenas para glosar o "premio").
**RFB e CARF glosam sistematicamente** essas estruturas (Sumula CARF 125; precedentes de
planning abusivo). Resultado: multa qualificada (150%) + risco penal pos SV 24 STF.

**Este plugin nunca orienta agio artificial ou "agio interno".**

### 4.2 Prejuizo fiscal — vedacao (PA-17)

**Regra:** a incorporadora NAO aproveita os prejuizos fiscais acumulados da incorporada.
Vedacao expressa do IRPJ (RIR art. 580 [VERIFICAR numeracao atual]). Jurisprudencia
pacifica do CARF glosa essa operacao quando e o objetivo exclusivo da incorporacao.

Teses de incorporacao reversa com aproveitamento sao zona de litigio elevado — tratar
como tese em disputa (Protocolo 3), nunca como certeza.

**Este plugin nunca afirma que a incorporadora aproveita o prejuizo fiscal da incorporada.**

### 4.3 Proposito negocial e substancia economica

Toda reorganizacao deve demonstrar: (1) proposito negocial independente do beneficio fiscal;
(2) substancia economica real na nova estrutura; (3) anterioridade ao fato gerador;
(4) documentacao robusta (justificacao, laudo, atas, contratos).

---

## 5. VEDACOES ESPECIFICAS

- **PA-13** — verificar quorum aplicavel (LTDA vs S/A) por modalidade de reorganizacao.
- **PA-14** — nao aplicar regras de S/A a LTDA indiscriminadamente.
- **PA-16** — nunca estruturar agio artificial, "agio interno" ou reorganizacao sem proposito
  negocial. Toda sugestao parte de proposito negocial documentado.
- **PA-17** — nunca afirmar que a incorporadora aproveita o prejuizo fiscal da incorporada.
- **PA-22** — minuta de protocolo/justificacao sujeita a revisao pelo advogado responsavel.

---

## 6. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — confirmar CC 1.113-1.122 e LSA 220-234 vigentes.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — proposito negocial documentado; elisao licita vs evasao.
- **Protocolo 3** (Jurisprudencial) — classificar tese de agio/prejuizo como "em disputa";
  mencionar Sumula CARF 125.
- **Protocolo 4** (Competencia) — Junta Comercial (protocolo); RFB (agio); CARF (contencioso).

---

## 7. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `planejamento-tributario`
(Tier 4) quando a reorganizacao tem motivacao fiscal.

**Entrega para:** `registro-empresarial`, `mitigacao-de-risco-fiscal` (Tier 4),
`estruturacao-holdings` (Tier 3) se contexto holding, `suprema-corte-empresarial`
(R1-R4 obrigatorio em analises com impacto fiscal).

**Sem esta skill:** reorganizacao sem protocolo/justificacao ou com risco de agio artificial e
aproveitamento de prejuizo fiscal — exposicao a autuacao com multa qualificada (150%).
