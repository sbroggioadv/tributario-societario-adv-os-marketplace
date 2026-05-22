---
name: pecas-defesa-administrativa
description: >
  Minutas de defesa no contencioso administrativo tributario — impugnacao a auto de
  infracao (30 dias), recurso voluntario ao CARF (30 dias), recurso especial a CSRF
  (15 dias, exige acordao paradigma), defesa em TIT e conselhos estaduais/municipais.
  Nunca confunde esfera administrativa e judicial (PA-05). Aciona: impugnacao, recurso
  CARF, recurso voluntario, CSRF, defesa administrativa, TIT, PAF.
---

# PECAS DE DEFESA ADMINISTRATIVA TRIBUTARIA

> Skill **Tier 5 — Tributario Contencioso** — minutas para o contencioso
> administrativo tributario: impugnacao (PAF federal, Dec. 70.235/72), recurso
> voluntario ao CARF, recurso especial a CSRF, defesa no TIT-SP e conselhos
> estaduais/municipais. Implementa PA-03, PA-04, PA-05, PA-11, PA-22.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "impugnacao", "recurso CARF", "recurso voluntario", "CSRF", "defesa
administrativa", "TIT", "contencioso administrativo", "PAF", "DRJ".

Entrega: minuta da peca escolhida (impugnacao / recurso voluntario / recurso especial
/ defesa em conselho estadual/municipal) com FIRAC e ressalvas obrigatorias.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `analise-auto-de-infracao` (Tier 5), `estrategia-de-caso-empresarial`, operador direto.
- **Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
  `calculo-e-prazos-tributarios` (valor em disputa).
- **Pre-requisito:** `analise-auto-de-infracao`; `analisador-legislacao-vigente`.

---

## 2. INSTANCIAS ADMINISTRATIVAS FEDERAIS

```
Auto de infracao → IMPUGNACAO (DRJ) — 30 dias [PA-03]
  → Acordao DRJ → RECURSO VOLUNTARIO (CARF) — 30 dias [PA-03]
    → Acordao CARF → RECURSO ESPECIAL (CSRF) — 15 dias + paradigma [PA-03]
      → Decisao CSRF → constituicao definitiva → prescricao inicia (CTN art. 174)
```

> **PA-05** — contencioso administrativo e judicial sao independentes. Impugnacao
> suspende a exigibilidade (CTN art. 151, III). Rota judicial paralela: consultar
> `estrategia-de-caso-empresarial`.

---

## 3. IMPUGNACAO A AUTO DE INFRACAO

Prazo: **30 dias da ciencia** (Dec. 70.235/72, art. 15) `[PA-03 — ESTIMATIVA — confirmar
data da ciencia; verificar suspensao por forca maior]`

Apresentacao: protocolo na unidade RFB ou e-CAC `[VERIFICAR modulo disponivel]`.

**Preclusao probatoria (Dec. 70.235/72, art. 16 §4):** toda prova documental deve
ser juntada na impugnacao. Provas retidas para instancias superiores so sao admitidas
se o contribuinte provar indisponibilidade anterior. `[PA-22 — reunir documentos antes
de protocolar]`

```
IMPUGNACAO — Auto n. ___ / [ANO]
[{{FIRM_NAME}} | {{CIDADE}}/{{UF}}]

EXCELENTISSIMO SENHOR DELEGADO DA RFB EM [CIDADE/UF]

[NOME DA EMPRESA], CNPJ n. ___, por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}}
{{ADVOGADO_OAB}}, nos termos do art. 15 do Dec. 70.235/72 e CTN art. 151, III,
impugna o auto lavrado em [data], cientificado em [data]:

I — DOS FATOS: [fato gerador, contexto do auto — FIRAC F]
II — DA QUESTAO: [questao juridica delimitada — FIRAC I]
III — DO DIREITO:
  III.1 Vicios formais (se houver): [norma + jurisprudencia — PA-04]
  III.2 Merito: [norma vigente no ano do fato gerador — PA-02 + PA-04]
  III.3 Decadencia (se arguivel): [CTN art. 150 §4 ou 173, I — PA-03 ressalva]
IV — DOS PEDIDOS: cancelar/reduzir lancamento; subsidiariamente, receber para recurso.

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
RESSALVA (PA-22): minuta — revisar, conferir prazos e assinar antes do protocolo.
```

---

## 4. RECURSO VOLUNTARIO AO CARF

Prazo: **30 dias da ciencia do acordao DRJ** (Dec. 70.235/72, art. 33)
`[PA-03 — prazos nao suspendem por recesso; verificar Lei 14.689/2023 sobre preparo]`

```
RECURSO VOLUNTARIO — CARF — Processo n. ___
[NOME DA EMPRESA], CNPJ n. ___, por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}}
{{ADVOGADO_OAB}}, nos termos do art. 33 do Dec. 70.235/72, recorre do Acordao
DRJ n. ___ [data], cientificado em [data] — prazo: [data] [VERIFICAR — PA-03].

I — TEMPESTIVIDADE: [demonstrar]
II — SUMARIO DAS RAZOES: [pontos de reforma]
III — DAS RAZOES: [norma + jurisprudencia CARF/STJ/STF — classificada — PA-04]
IV — DOS PEDIDOS: provimento para cancelar/reduzir lancamento.

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
```

---

## 5. RECURSO ESPECIAL A CSRF

Prazo: **15 dias da ciencia do acordao CARF** (Dec. 70.235/72, art. 37) `[PA-03]`

**Exigencia critica:** acordao paradigma de **OUTRA camara ou turma do CARF** com
conclusao diferente sobre a mesma questao de direito. Sem paradigma valido: recurso
nao conhecido.

```
Checklist de admissibilidade:
[ ] Camara diferente (nao a mesma turma)
[ ] Mesma materia de DIREITO (nao de fato)
[ ] Paradigma nao superado por sumula CARF
[ ] Tempestividade: 15 dias [PA-03]
[ ] Paradigma autenticado na fonte oficial CARF [PA-04]

RECURSO ESPECIAL — CSRF — Processo n. ___
[NOME DA EMPRESA], por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}},
nos termos do art. 37 do Dec. 70.235/72, interpoe RECURSO ESPECIAL contra
Acordao CARF n. ___ [data].

I — ADMISSIBILIDADE: tempestividade [data — PA-03] + paradigma: Acordao n. ___,
  Camara ___ [VERIFICAR autenticidade — PA-04], divergencia: [resumo].
II — DAS RAZOES: [demonstrar divergencia; norma + precedente classificado — PA-04]
III — DOS PEDIDOS: reformar o acordao conforme o paradigma.

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
```

---

## 6. CONSELHOS ESTADUAIS E MUNICIPAIS (TIT-SP E OUTROS)

| Esfera | Orgao | Rito | Prazo |
|--------|-------|------|-------|
| Estadual SP (ICMS) | TIT | Lei 13.457/09-SP | `[VERIFICAR — PA-03]` |
| Demais estados | Conselho estadual | Regimento local | `[VERIFICAR — PA-03]` |
| Municipal (ISS/IPTU) | Conselho municipal | Legislacao local | `[VERIFICAR — PA-03]` |

> **PA-11** — identificar esfera antes de estruturar a peca. Usar estrutura da
> impugnacao federal como base e adaptar ao rito local `[VERIFICAR]`.

---

## 7. VEDACOES ESPECIFICAS

- **PA-03** — todo prazo e estimativa; confirmar data de ciencia no caso concreto.
- **PA-04** — zero alucinacao de acordao, sumula, tema. Incerto = `[VERIFICAR]`.
- **PA-05** — via administrativa e judicial sao independentes; nao confundir.
- **PA-11** — esfera identificada antes de qualquer peca.
- **PA-22** — minuta; advogado responsavel assina antes do protocolo.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** — normas validadas no ano do fato gerador.
- **Protocolo 3** — precedentes classificados (vinculante/em disputa/superado);
  modulacao verificada (PA-07).
- **Protocolo 4** — instancia correta por esfera.
- **Protocolo 5** — valor em disputa: estimativa (PA-09).

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`analise-auto-de-infracao` (Tier 5), `estrategia-de-caso-empresarial`, operador direto.

**Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
`calculo-e-prazos-tributarios`.

**Sem esta skill:** prazo de impugnacao perdido; preclusao probatoria nao alertada;
recurso especial sem paradigma — inadmissivel.
