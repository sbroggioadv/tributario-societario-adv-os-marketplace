---
name: analise-auto-de-infracao
description: >
  Dissecacao de auto de infracao — vicios formais do lancamento, merito, decadencia,
  e opcoes estrategicas (impugnar, pagar com desconto, parcelar, discutir judicialmente).
  Toda estimativa de prazo inclui ressalva PA-03. Nunca confunde esfera administrativa
  e judicial (PA-05). Aciona: auto de infracao, fui autuado, recebi autuacao,
  notificacao da Receita, AIIM, termo de intimacao fiscal.
---

# ANALISE DE AUTO DE INFRACAO

> Skill **Tier 5 — Tributario Contencioso** — dissecar o auto de infracao (federal,
> estadual ou municipal): vicios formais, merito, decadencia, prescricao, e opcoes
> estrategicas. Implementa PA-03, PA-04, PA-05, PA-11, PA-22 e o Protocolo 4
> (Competencia). Mode: contencioso.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "auto de infracao", "AIIM", "fui autuado", "recebi autuacao",
"notificacao da Receita", "termo de intimacao fiscal", "lavrei auto", "auto fiscal",
"lei de infracao tributaria", "recebi notificacao do Fisco".

Entrega: analise estruturada do auto em 5 blocos (identificacao, vicios formais,
merito, decadencia/prescricao, opcoes estrategicas) + recomendacao de rota.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `analise-documental-empresarial`, `estrategia-de-caso-empresarial`, operador direto.
- **Entrega para:** `pecas-defesa-administrativa` (se rota administrativa escolhida),
  `pecas-defesa-execucao-fiscal` (se o credito ja estiver inscrito em divida ativa),
  `pecas-acao-do-contribuinte` (se rota judicial antecipada for indicada),
  `calculo-e-prazos-tributarios` (estimativa do debito), `suprema-corte-empresarial`
  (R1-R4 antes da entrega ao cliente).
- **Pre-requisito:** `analisador-legislacao-vigente` validar as normas citadas no auto;
  `calculo-e-prazos-tributarios` confirmar prazos e valor do debito.

---

## 2. BLOCO A — IDENTIFICACAO DO AUTO

Antes de qualquer analise, mapear:

```
AUTO DE INFRACAO — IDENTIFICACAO
Numero do auto: [numero]
Orgao lavrador: [RFB / SEFAZ-UF / Prefeitura-Municipio]
Competencia: [Federal | Estadual | Municipal] — PA-11
Tributo: [IRPJ / CSLL / PIS / COFINS / ICMS / ISS / outro]
Fato gerador: [descricao breve e datas dos periodos]
Exercicio(s) autuado(s): [anos]
Valor do auto: R$ ___ (principal + multa + juros — confirmar no auto)
Data de ciencia pelo autuado: [DD/MM/AAAA — marco dos prazos]
Prazo de impugnacao: 30 dias da ciencia [ESTIMATIVA — PA-03 — verificar Dec. 70.235/72
  art. 15 para federal; legislacao estadual/municipal para outros]
Vencimento estimado do prazo: [DD/MM/AAAA — VERIFICAR]
```

> **PA-11** — identificar competencia antes de qualquer analise. Prazos, instancias
> e recursos variam radicalmente entre federal (CARF), estadual (TIT/conselhos) e
> municipal (conselhos de contribuintes).

---

## 3. BLOCO B — VICIOS FORMAIS DO LANCAMENTO

Vicios formais podem anular o auto independentemente do merito. Verificar:

### 3.1 Vicios que invalidam o lancamento

| Vicio | Norma | Impacto |
|-------|-------|---------|
| Ausencia de identificacao do sujeito passivo | Dec. 70.235/72, art. 11, I | Nulidade — PA-04: confirmar no auto |
| Descricao insuficiente da infracao | Dec. 70.235/72, art. 11, II | Nulidade |
| Ausencia de indicacao da legislacao infringida | Dec. 70.235/72, art. 11, II | Nulidade |
| Lancamento por autoridade incompetente | CTN arts. 142, 7 | Nulidade |
| Ausencia de assinatura do agente fiscal | Dec. 70.235/72, art. 11, IV | Nulidade |
| Erro na identificacao do fato gerador | CTN art. 114 | Anulabilidade |
| Cerceamento do direito de defesa | CF art. 5, LV | Arguir em impugnacao |

### 3.2 Vicios materiais (merito)

Vicios de merito — tributo nao devido, base de calculo incorreta, aliquota errada,
regime tributario incorreto — sao tratados no Bloco C (merito).

> **PA-04** — nunca afirmar nulidade sem verificar se o requisito do Dec. 70.235/72
> esta realmente ausente no documento. Indicar como [VERIFICAR NO AUTO FISICO].

---

## 4. BLOCO C — MERITO DO LANCAMENTO

### 4.1 Questoes de merito a verificar

```
[ ] Base de calculo esta correta? (art. indicado no auto corresponde ao tributo?)
[ ] Aliquota aplicada e a vigente no ano do fato gerador? (PA-02/PA-06)
[ ] Regime tributario do contribuinte esta correto no auto? (Simples/Presumido/Real)
[ ] Creditos e deducoes do contribuinte foram considerados?
[ ] Ha nota fiscal fria, omissao de receita ou simulacao alegada?
    — Se sim: verificar se ha prova documental no auto
[ ] Multa aplicada e proporcional? (75% padrao ou 150% qualificada?)
    — 150% exige dolo/fraude/simulacao documentada (art. 44 §1 Lei 9.430/1996)
[ ] Houve reducao de multa por pagamento a vista? (art. 6 Lei 8.218/91 — VERIFICAR)
```

### 4.2 Teses de merito mais comuns (por tributo)

- **PIS/COFINS:** regime cumulativo x nao-cumulativo; creditos admissivos; insumos.
- **IRPJ/CSLL:** glosa de despesas; distribuicao disfarada de lucros; transferencia
  de precos; estimativas mensais.
- **ICMS:** credito de ICMS estadual cruzado com outro estado; base de calculo do
  frete; beneficio fiscal estadual questionado.
- **ISS:** local do estabelecimento prestador; competencia do municipio; CNAE.

> **PA-02** — sempre conferir a redacao da norma no ANO DO FATO GERADOR, nao a redacao
> atual. Alteracoes legislativas entre o fato gerador e o auto sao frequentes.

---

## 5. BLOCO D — DECADENCIA E PRESCRICAO

### 5.1 Decadencia — o credito podia ser lancado?

```
Exercicio autuado: [AAAA]
Tipo de lancamento: [homologacao | oficio]

Se homologacao (IRPJ/CSLL/PIS/COFINS/ICMS declarado — CTN art. 150 §4):
  Fato gerador: [data]
  Prazo decadencial: 5 anos = [data limite — VERIFICAR]
  Ha alegacao de dolo/fraude? Se sim, prazo muda para art. 173, I (mais longo).

Se oficio (IPTU/IPVA/lancamento direto — CTN art. 173, I):
  1o dia do exercicio seguinte: 01/01/[AAAA+1]
  Prazo decadencial: 5 anos = 01/01/[AAAA+6] — [VERIFICAR]

Lancamento anterior anulado? CTN art. 173, II — prazo reinicia da decisao anulatoria.
```

> **PA-03** — nunca cravar decadencia como definitiva sem ressalva de interrupcoes,
> suspensoes, e tipo exato de lancamento. Incluir: "[VERIFICAR — prazo estimado
> sujeito a revisao com os autos completos]".

### 5.2 Prescricao — o debito ja esta prescrito?

Prescricao (CTN art. 174) corre a partir da constituicao definitiva. Se o auto foi
lavrado mas o prazo de impugnacao ainda nao correu, o credito NAO esta constituido
definitivamente — prescricao ainda nao iniciou.

---

## 6. BLOCO E — OPCOES ESTRATEGICAS

Apos mapear vicios formais, merito e decadencia, apresentar as opcoes:

```
OPCOES ESTRATEGICAS — [CASO]

OPCAO 1 — Impugnar administrativamente
  Prazo: 30 dias da ciencia (Dec. 70.235/72, art. 15 — VERIFICAR na legislacao
    estadual/municipal se nao for federal) [PA-03]
  Vantagem: suspende a exigibilidade (CTN art. 151, III); sem deposito.
  Desvantagem: instancia administrativa pode ser demorada (CARF: anos).
  Indicada quando: ha vicios formais fortes OU tese de merito com jurisprudencia
    favoravel no CARF/TIT OU decadencia arguivel.

OPCAO 2 — Pagar com reducao de multa
  Verificar programa especial vigente (PERT ou similar — VERIFICAR RFB).
  Pagamento a vista antes do contencioso: reducao de 50% da multa e 50% dos juros
    em programas de parcelamento — [VERIFICAR programa vigente].
  Indicada quando: tese de merito e fraca; risco de multa qualificada (150%).

OPCAO 3 — Parcelar (PERT ou parcelamento ordinario)
  Parcelamento ordinario: ate 60 meses (Lei 10.522/2002 art. 10 — VERIFICAR).
  Indicada quando: cliente quer regularizar sem pagar a vista mas sem brigar.

OPCAO 4 — Questionar judicialmente (acao anulatoria ou mandado de seguranca)
  Possivel em paralelo ou apos esgotamento da via administrativa.
  MS preventivo: antes do lancamento definitivo — PA-05 distinguir via adm x judicial.
  Indicada quando: tese de merito solida com jurisprudencia STF/STJ favoravel;
    exige deposito ou afiancamento.

OPCAO 5 — Aguardar e monitorar decadencia/prescricao
  So em casos onde o calculo da decadencia indica prazo proximo ao vencimento.
  Risco alto — nunca recomendar sem ressalva e sem confirmacao do prazo.
```

---

## 7. VEDACOES ESPECIFICAS

- **PA-03** — todo prazo (impugnacao 30 dias, decadencia, prescricao) e estimativa
  marcada. Incluir ressalva "[ESTIMATIVA — VERIFICAR — PA-03]".
- **PA-04** — nunca inventar numero de artigo, sumula ou acordao. Incerto = [VERIFICAR].
- **PA-05** — nao confundir via administrativa (impugnacao/CARF) com via judicial
  (acao anulatoria/MS). Sao independentes, mas a eleicao da via tem consequencias.
- **PA-09** — valor do debito e estimativa. Confirmar no e-CAC ou PGFN.
- **PA-11** — identificar competencia (federal/estadual/municipal) ANTES de qualquer
  analise de prazos ou instancias.
- **PA-22** — toda analise e minuta sujeita a revisao do advogado responsavel.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — verificar normas citadas no auto no ANO do fato
  gerador (PA-02); dec 70.235/72, CTN, lei do tributo autuado.
- **Protocolo 3** (Jurisprudencial) — classificar tese de merito: vinculante/em
  disputa/superada; verificar modulacao (PA-07).
- **Protocolo 4** (Competencia) — federal/estadual/municipal; instancias corretas.
- **Protocolo 5** (Calculo) — valor do auto e estimativa marcada (PA-09).

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`analise-documental-empresarial`, `estrategia-de-caso-empresarial`, operador direto.

**Entrega para:** `pecas-defesa-administrativa` (rota adm), `pecas-defesa-execucao-fiscal`
(divida ativa), `pecas-acao-do-contribuinte` (rota judicial antecipada),
`calculo-e-prazos-tributarios` (valores e prazos), `suprema-corte-empresarial` (R1-R4).

**Sem esta skill:** cliente recebe opcoes sem dissecacao do auto — vicios formais
nao identificados, decadencia nao arguida, prazo de impugnacao perdido.
