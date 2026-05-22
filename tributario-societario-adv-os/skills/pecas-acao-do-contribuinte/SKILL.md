---
name: pecas-acao-do-contribuinte
description: >
  Acoes do contribuinte contra a cobranca fiscal — mandado de seguranca preventivo
  e repressivo (120 dias para o repressivo, Lei 12.016/2009 art. 23), acao anulatoria,
  acao declaratoria, acao de repeticao de indebito (art. 166 CTN para tributo indireto).
  Aciona: mandado de seguranca, acao anulatoria, declaratoria, repeticao de indebito,
  acao contra a Fazenda, impugnar judicialmente, questionar tributo, MS tributario.
---

# PECAS — ACOES DO CONTRIBUINTE

> Skill **Tier 5 — Tributario Contencioso** — minutas das acoes do contribuinte
> contra a cobranca fiscal: mandado de seguranca (preventivo/repressivo), acao
> anulatoria, declaratoria e repeticao de indebito. Implementa PA-03, PA-04,
> PA-05, PA-07, PA-22. Mode: contencioso.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "mandado de seguranca tributario", "acao anulatoria", "acao declaratoria",
"repeticao de indebito", "acao contra a Fazenda", "impugnar judicialmente",
"MS preventivo", "MS repressivo", "restituicao de tributo pago indevidamente".

Entrega: tabela de selecao + minuta da acao escolhida com requisitos e ressalvas.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `analise-auto-de-infracao` (Tier 5), `estrategia-de-caso-empresarial`,
  `analise-documental-empresarial`, operador direto.
- **Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
  `calculo-e-prazos-tributarios` (valor credito/indebito; prescricao),
  `recursos-judiciais-tributarios` (fase recursal).
- **Pre-requisito:** `analisador-legislacao-vigente`; Protocolo 1.

---

## 2. TABELA DE SELECAO DA ACAO

| Acao | Quando usar | Prazo | Observacao critica |
|------|-------------|-------|-------------------|
| MS preventivo | Ameaca certa de ato coator ainda nao praticado | Sem prazo (ameaca continua) | Exige prova atual da ameaca |
| MS repressivo | Ato coator ja praticado | **120 dias do ato** — Lei 12.016/2009 art. 23 `[PA-03]` | Vencido: so anulatoria ou ordinaria |
| Acao anulatoria | Credito constituido; anular antes/apos execucao | 5 anos da constituicao definitiva — CTN art. 174 `[PA-03]` | Cumulavel com tutela antecipada |
| Acao declaratoria | Inexistencia de relacao tributaria; antes do lancamento | Sem prazo — preventiva | Nao serve para credito ja constituido |
| Repeticao de indebito | Tributo pago indevidamente | 5 anos do pagamento — CTN art. 168, I `[PA-03]` | Art. 166 CTN: indireto exige nao-repercussao |

> **PA-05** — acao judicial e independente da impugnacao administrativa.
> Estrategias paralelas: alinhar com `estrategia-de-caso-empresarial`.

---

## 3. MANDADO DE SEGURANCA TRIBUTARIO

Fundamento: CF art. 5, LXIX; Lei 12.016/2009. Exige direito liquido e certo
(prova documental, sem dilacao probatoria) + ato de autoridade publica coatora.

**Prazo repressivo:** 120 dias do ato coator `[PA-03 — confirmar data do ato]`

```
MANDADO DE SEGURANCA [PREVENTIVO | REPRESSIVO]
[{{FIRM_NAME}} | {{CIDADE}}/{{UF}}]

MM. JUIZ [FEDERAL | DA VARA DA FAZENDA] DE [CIDADE/UF]

[NOME DA EMPRESA], CNPJ n. ___, por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}}
{{ADVOGADO_OAB}}, nos termos dos arts. 5, LXIX, CF e 1 e ss. da Lei 12.016/2009,
impetra MS [PREVENTIVO | REPRESSIVO] contra ato [ameacado por | praticado por]
[nome/cargo da autoridade coatora].

I — TEMPESTIVIDADE (repressivo): ato em [data]; 120 dias: [data] [VERIFICAR — PA-03].
II — DO ATO COATOR E DO DIREITO LIQUIDO E CERTO:
  [Ato coator descrito / ameaca concreta com prova documental — Docs. 01-__]
III — DAS RAZOES (FIRAC):
  F Fatos: [historico objetivo]
  I Questao: [questao juridica]
  R Regra: [norma vigente + jurisprudencia classificada — PA-04]
  A Aplicacao: [subsuncao]
  C Conclusao: [direito liquido e certo — resultado pedido]
IV — DO PEDIDO DE LIMINAR (se urgente):
  Fumus: [norma/precedente]. Periculum: [risco concreto].
  Pede liminar para [suspender exigibilidade / impedir ato — especificar].
V — DOS PEDIDOS: seguranca definitiva para [anular ato / reconhecer inexistencia
  da obrigacao / determinar devolucao — especificar]; honorarios `[VERIFICAR
  Sumula 512 STF e 105 STJ — PA-04]`.

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
RESSALVA (PA-22): verificar autoridade coatora, prazo (repressivo), prova documental
completa e competencia antes de protocolar.
```

---

## 4. ACAO ANULATORIA DE DEBITO FISCAL

Prazo: 5 anos do credito definitivo (CTN art. 174) `[PA-03 — verificar interrupcoes]`

Deposito: nao obrigatorio, mas suspende exigibilidade (CTN art. 151, II).
Tutela antecipada: possivel sem deposito (CPC art. 300 — fumus + periculum).

**Estrutura (FIRAC sumaria):**
```
I — DOS FATOS: auto, fase processual, valor `[PA-09: estimativa]`
II — TEMPESTIVIDADE: lancamento definitivo [data]; prescricao [data] `[PA-03 — CTN 174]`
III — DO DIREITO: norma + jurisprudencia classificada `[PA-04]`
IV — TUTELA (se urgente): fumus + periculum + pedido de suspensao
V — PEDIDOS: anulacao do lancamento; custas/honorarios
{{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}} | {{FIRM_NAME}}
```

---

## 5. ACAO DECLARATORIA

Preventiva — antes da constituicao do credito; quer certeza de que NAO deve o tributo.
Nao serve para credito ja constituido — usar anulatoria.
Cumular com tutela antecipada (CPC art. 300) se houver risco de cobranca iminente.

---

## 6. REPETICAO DE INDEBITO

Prazo: 5 anos do pagamento indevido (CTN art. 168, I) `[PA-03 — verificar interrupcoes]`

### 6.1 Art. 166 CTN — Tributo Indireto (regra critica)

Tributos que repercutem o encargo no consumidor (IPI, ICMS, ISS) exigem prova de
que o contribuinte NAO transferiu o encargo ao consumidor final, OU autorizacao
expressa do terceiro que arcou.

- **Tributos diretos** (IRPJ, CSLL, IRRF): legitimidade direta, sem exigencia do art. 166.
- **Tributos indiretos** (IPI/ICMS/ISS): sem prova de nao-repercussao = carencia de acao.

### 6.2 Formas de recuperacao

- **Repeticao em especie** — acao de restituicao.
- **Compensacao PER/DCOMP** — com tributos vincendos da mesma especie; mais rapida;
  sujeita a homologacao RFB/SEFAZ; verificar com `recuperacao-de-creditos` (Tier 4).

```
REPETICAO DE INDEBITO
I — DOS FATOS: tributo pago, periodo, valor `[PA-09 estimativa]`
II — DO DIREITO: tese + norma `[PA-04]`; modulacao se aplicavel `[PA-07]`
III — LEGITIMIDADE (se indireto): prova de nao-repercussao — CTN art. 166; Documento: ___
IV — DA PRESCRICAO: pagamentos a partir de [hoje menos 5 anos] `[PA-03 VERIFICAR]`
V — PEDIDOS: repeticao em especie OU compensacao (CTN art. 170); Selic; honorarios
{{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}} | {{FIRM_NAME}}
```

---

## 7. VEDACOES ESPECIFICAS

- **PA-03** — 120 dias MS repressivo; 5 anos anulatoria/repeticao: estimativas. Verificar.
- **PA-04** — nao inventar Tema, Sumula ou acordao. Incerto = `[VERIFICAR]`.
- **PA-05** — via judicial independente da administrativa; nao confundir.
- **PA-07** — verificar modulacao de teses tributarias STF antes de calcular credito.
- **PA-22** — toda peca e minuta; advogado assina antes de protocolar.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** — CTN, LEF, Lei 12.016/2009 e normas validadas.
- **Protocolo 3** — teses classificadas; modulacao verificada (PA-07).
- **Protocolo 4** — Justica Federal (federal) ou Estadual/Municipal; vara correta.
- **Protocolo 5** — valor do credito/indebito: estimativa (PA-09).

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`analise-auto-de-infracao` (Tier 5), `estrategia-de-caso-empresarial`,
`analise-documental-empresarial`, operador direto.

**Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
`calculo-e-prazos-tributarios`, `recursos-judiciais-tributarios`.

**Sem esta skill:** MS repressivo perdido por prazo (120 dias); repeticao de indireto
sem prova de nao-repercussao = carencia; credito calculado sem verificar modulacao.
