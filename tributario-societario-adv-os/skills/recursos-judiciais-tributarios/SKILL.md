---
name: recursos-judiciais-tributarios
description: >
  Recursos no contencioso judicial tributario — apelacao (15 dias, CPC art. 1.003),
  recurso especial ao STJ (15 dias, prequestionamento obrigatorio), recurso
  extraordinario ao STF em materia tributaria (repercussao geral, prequestionamento,
  modulacao de efeitos PA-07). Aciona: apelacao tributaria, recurso especial, recurso
  extraordinario, recorrer da sentenca fiscal, REsp tributario, RE tributario.
---

# RECURSOS JUDICIAIS TRIBUTARIOS

> Skill **Tier 5 — Tributario Contencioso** — recursos no contencioso judicial
> tributario: apelacao, recurso especial (STJ) e recurso extraordinario (STF).
> Foco em admissibilidade, prequestionamento e modulacao de efeitos. Implementa
> PA-03, PA-04, PA-07, PA-11, PA-22. Mode: contencioso.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "apelacao tributaria", "recurso especial tributario", "recurso
extraordinario tributario", "recorrer da sentenca fiscal", "REsp tributario",
"RE tributario", "segunda instancia tributaria", "prequestionamento tributario",
"TRF", "STJ tributario", "STF tributario", "repercussao geral tributaria".

Entrega: analise de admissibilidade + minuta do recurso adequado com checklist
de prequestionamento e ressalvas obrigatorias.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `pecas-acao-do-contribuinte` (Tier 5), `pecas-defesa-execucao-fiscal` (Tier 5),
  `estrategia-de-caso-empresarial`, operador direto.
- **Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
  `calculo-e-prazos-tributarios` (prazo recursal e valor).
- **Pre-requisito:** `analisador-legislacao-vigente` (CPC, RISTJ, RISTF vigentes).

---

## 2. MAPA DOS RECURSOS JUDICIAIS TRIBUTARIOS

```
SENTENCA (Juiz Federal / Vara da Fazenda)
  |
  v
APELACAO → TRF (tributos federais) | TJ (estaduais/municipais)
  Prazo: 15 dias da intimacao — CPC art. 1.003 §5 [PA-03]
  |
  v
ACORDAO TRF/TJ
  |--- REsp (STJ) — violacao de lei federal ou divergencia entre tribunais
  |    Prazo: 15 dias da publicacao do acordao [PA-03]
  |    Exige: prequestionamento; lei federal violada OU paradigma divergente
  |
  |--- RE (STF) — materia constitucional
       Prazo: 15 dias da publicacao do acordao [PA-03]
       Exige: prequestionamento; repercussao geral reconhecida
```

> **PA-11** — competencia (Federal x Estadual) define se o acordao vai a TRF ou TJ,
> mas STJ e STF sao instancias de ambas as justicas em materia federal e constitucional.

---

## 3. APELACAO TRIBUTARIA

Prazo: **15 dias da intimacao da sentenca** (CPC art. 1.003 §5) `[PA-03 — confirmar data]`

Preparo: custas da tabela do TRF/TJ competente `[VERIFICAR tabela vigente]`. Fazenda
Publica e isenta. Contribuinte paga salvo gratuidade.

```
Checklist de admissibilidade:
[ ] Tempestividade: 15 dias da intimacao [PA-03]
[ ] Preparo recolhido ou isento
[ ] Decisao apelavel (sentenca de merito — CPC art. 1.009)
[ ] Parte sucumbente

APELACAO CIVEL — Processo n. ___
[{{FIRM_NAME}} | {{CIDADE}}/{{UF}}]

EGREGIOS DESEMBARGADORES DO TRF ___ REGIAO / TJESTADO

[NOME DA EMPRESA], por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}},
nos termos do art. 1.009 do CPC, apela da sentenca de [data] (intimacao: [data]).

I — TEMPESTIVIDADE: 15 dias: [data] [VERIFICAR — PA-03]. Tempestivo.
II — PREPARO: custas recolhidas (guia juntada: ___) [ou: isento — ___].
III — DAS RAZOES (FIRAC):
  F: [historico + sentenca recorrida — pontos de reforma]
  I: [questao recursal]
  R: [norma vigente + jurisprudencia classificada — PA-04]
  A: [critica ao julgado — erro de fato e/ou de direito]
  C: [reforma pedida]
IV — DO PREQUESTIONAMENTO (obrigatorio se houver REsp/RE potencial):
  Requer manifestacao expressa do Tribunal sobre os arts.: [listar dispositivos].
  [Prequestionar TODOS os artigos que pretende levar ao STJ/STF nesta oportunidade]
V — PEDIDOS: conhecimento e provimento para [resultado].

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
RESSALVA (PA-22): verificar prazo, preparo e prequestionamento completo.
```

---

## 4. RECURSO ESPECIAL (STJ)

Fundamento: CF art. 105, III — violacao de lei federal (alinea "a") ou divergencia
jurisprudencial (alinea "c"). Em tributario: CTN, LEF, leis de tributos federais, CPC.

Prazo: **15 dias da publicacao do acordao no DJe** `[PA-03]`

```
Checklist de admissibilidade:
[ ] Tempestividade [PA-03]
[ ] Prequestionamento: acordao se manifestou expressamente sobre a lei federal
    (Sumula 211 STJ — [PA-04: confirmar redacao])
[ ] Fundamento: violacao de lei federal OU divergencia (paradigma + confronto analitico)
[ ] Materia de direito (nao de fato — Sumula 7 STJ)
[ ] Se divergencia: paradigma de outro tribunal; demonstrar identidade fatica e
    solucao juridica diferente
[ ] Preparo (RISTJ vigente — VERIFICAR)
```

**Tecnica de prequestionamento:** se o acordao nao decidiu expressamente o artigo,
opor EMBARGOS DE DECLARACAO (CPC art. 1.022, prazo 5 dias `[PA-03]`) por omissao
antes de interpor o REsp. Uso protelatario gera multa (CPC art. 1.026 §2).

```
RECURSO ESPECIAL — Processo n. ___
I — TEMPESTIVIDADE: acordao publicado [data]; 15 dias: [data] [VERIFICAR — PA-03]
II — PREQUESTIONAMENTO: acordao decidiu arts. [listar] (fls. ___) [ou: embargos
     de declaracao fls. ___ supriram a omissao]
III — CABIMENTO: [violacao do art. ___ da Lei ___ / divergencia: acordao paradigma
     n. ___ — [TRIBUNAL] `[VERIFICAR autenticidade — PA-04]`]
IV — DAS RAZOES: norma violada + interpretacao correta + jurisprudencia STJ
     favoravel classificada `[PA-04]`
V — PEDIDOS: conhecimento e provimento

{{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}} | {{FIRM_NAME}}
```

---

## 5. RECURSO EXTRAORDINARIO (STF)

Fundamento: CF art. 102, III — violacao direta da Constituicao (alinea "a"). Em
tributario: legalidade (CF art. 150, I), anterioridade, imunidades, nao-cumulatividade.

Prazo: **15 dias da publicacao do acordao** `[PA-03]`

**Repercussao geral** (EC 45/2004; CPC art. 1.035): requisito intransponivel.
Sem RG reconhecida: RE nao conhecido.

Estrategia: verificar Tema STF na materia `[VERIFICAR — portal STF — PA-04]`.

> **PA-07 — OBRIGATORIO:** verificar modulacao de efeitos do Tema STF antes de
> calcular credito ou propor acao. Modulacao prospectiva pode tornar o RE inutil
> para contribuintes que nao ajuizaram antes do julgamento.

```
Checklist RE:
[ ] Tempestividade [PA-03]
[ ] Prequestionamento da questao constitucional (idem sequencia REsp)
[ ] Repercussao geral: Tema STF reconhecido `[VERIFICAR — PA-04]` OU demonstrar RG
[ ] Questao constitucional (nao legal — diferente do REsp)
[ ] Modulacao: verificar se Tema tem modulacao e qual o alcance `[PA-07]`
[ ] Preparo (RISTF vigente — VERIFICAR)
```

---

## 6. VEDACOES ESPECIFICAS

- **PA-03** — todos os prazos (15 dias apelacao/REsp/RE; 5 dias embargos) sao
  estimativas. Confirmar data de intimacao/publicacao.
- **PA-04** — nao inventar Tema, Sumula ou acordao paradigma. Incerto = `[VERIFICAR]`.
- **PA-07** — verificar modulacao do Tema STF antes de calcular credito ou indicar rota.
- **PA-11** — esfera correta (Federal x Estadual) define instancia superior.
- **PA-22** — minuta; advogado assina antes de protocolar.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** — CPC, RISTJ, RISTF e normas tributarias validadas.
- **Protocolo 3** — teses classificadas (vinculante/em disputa/superado); modulacao
  verificada (PA-07) para TODOS os Temas tributarios relevantes.
- **Protocolo 4** — instancia recursal correta por esfera.
- **Protocolo 5** — valor em disputa: estimativa (PA-09).

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`pecas-acao-do-contribuinte` (Tier 5), `pecas-defesa-execucao-fiscal` (Tier 5),
`estrategia-de-caso-empresarial`, operador direto.

**Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
`calculo-e-prazos-tributarios`.

**Sem esta skill:** prequestionamento ausente na apelacao — REsp/RE inadmissivel;
modulacao de efeitos nao verificada — credito calculado indevidamente; RE sem RG
demonstrada — nao conhecido.
