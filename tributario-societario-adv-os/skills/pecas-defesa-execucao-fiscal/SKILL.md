---
name: pecas-defesa-execucao-fiscal
description: >
  Minutas de defesa na execucao fiscal — embargos a execucao fiscal (exige garantia
  do juizo, prazo 30 dias, admite ampla prova) e excecao de pre-executividade (dispensa
  garantia, apenas materia de ordem publica sem dilacao probatoria, Sumula 393 STJ).
  Nunca confunde os dois instrumentos (PA-08). Aciona: execucao fiscal, embargos,
  excecao de pre-executividade, fui executado, penhora, CDA, divida ativa, LEF.
---

# PECAS DE DEFESA NA EXECUCAO FISCAL

> Skill **Tier 5 — Tributario Contencioso** — embargos a execucao fiscal (LEF) e
> excecao de pre-executividade. A distincao entre os dois e critica e nunca pode
> ser confundida (PA-08). Mode: contencioso.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "execucao fiscal", "embargos", "excecao de pre-executividade",
"fui executado", "penhora", "CDA", "divida ativa", "LEF", "citado na execucao",
"oficio de penhora", "executado pela Fazenda".

Entrega: tabela comparativa (embargos x excecao) + checklist de selecao + minuta
do instrumento adequado.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `analise-auto-de-infracao` (Tier 5), `estrategia-de-caso-empresarial`,
  `analise-documental-empresarial`, operador direto.
- **Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
  `calculo-e-prazos-tributarios` (valor da divida e garantia).
- **Pre-requisito:** `analisador-legislacao-vigente` (CDA, titulo, normas);
  `calculo-e-prazos-tributarios` (prazo 30 dias, valor garantia).

---

## 2. TABELA COMPARATIVA — PA-08 (NUNCA CONFUNDIR)

| Criterio | Embargos (LEF art. 16) | Excecao de Pre-Executividade |
|----------|------------------------|------------------------------|
| **Garantia** | **EXIGE** — penhora / fianca / deposito | **DISPENSA** |
| **Prazo** | 30 dias da penhora/citacao `[PA-03]` | Sem prazo fixo |
| **Materia** | Ampla — merito, vicios, decadencia, prescricao, excesso, pagamento | Restrita — **ordem publica** conhecivel de oficio |
| **Prova** | Ampla — pericial e documental | Documentos apenas — sem dilacao probatoria (Sumula 393 STJ) |
| **Efeito suspensivo** | Sim, se garantia integral (LEF art. 16 §1) | Nao automatico — requer tutela |
| **Quando usar** | Ha merito; cliente tem patrimonio; prazo vivo | Sem patrimonio para garantia; vicio de ordem publica documentado |

> **PA-08** — usar o instrumento errado e erro grave: embargos sem garantia = extintos;
> excecao com dilacao probatoria = nao conhecida.

---

## 3. CHECKLIST DE SELECAO DO INSTRUMENTO

```
1. Credito inscrito em CDA? [sim/nao]
2. Citacao/penhora ja realizada? [sim/nao]
3. Garantia disponivel (penhora/fianca/deposito)? [sim/nao/parcial]
4. Prazo de 30 dias da penhora ainda vivo? [sim/nao — PA-03 VERIFICAR]
5. Materia e de ordem publica (prescricao/decadencia/nulidade/ilegitimidade)? [sim/nao]
6. Ha necessidade de dilacao probatoria? [sim/nao]

→ Garantia + prazo vivo + merito: EMBARGOS
→ Sem garantia + ordem publica + prova documental: EXCECAO
→ Ambos possiveis: preferir embargos (mais amplo) se houver garantia
```

---

## 4. EMBARGOS A EXECUCAO FISCAL (LEF art. 16)

Prazo: **30 dias da garantia/citacao** `[PA-03 — confirmar data; LEF art. 16]`

```
EMBARGOS A EXECUCAO FISCAL — Processo n. ___
[{{FIRM_NAME}} | {{CIDADE}}/{{UF}}]

MM. JUIZ [DA VARA DE EXECUCOES FISCAIS / FEDERAL] DE [CIDADE/UF]

[NOME DA EMPRESA], CNPJ n. ___, garantido o juizo pela penhora de fls.___/
deposito de [data], por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}},
nos termos dos arts. 16 e ss. da Lei 6.830/80, embarga a execucao fiscal n. ___
movida por [EXEQUENTE]:

I — TEMPESTIVIDADE E GARANTIA: penhora em [data]; 30 dias: [data] [VERIFICAR — PA-03].
II — DA CDA — PRESSUPOSTOS: [liquidez, certeza, exigibilidade — LEF art. 2 §5]
III — DAS TESES (FIRAC):
  III.1 Decadencia/prescricao (se arguivel) — CTN arts. 150 §4 / 173 / 174 [PA-03]
  III.2 Nulidade do lancamento — vicios formais [PA-04: citar sem inventar]
  III.3 Merito — tributo indevido, base errada, regime incorreto
  III.4 Excesso de execucao — valor [PA-09: estimativa]
  III.5 Pagamento/compensacao — prova documental juntada
IV — DAS PROVAS: [documental / pericial — juntar toda prova disponivel]
V — DOS PEDIDOS: efeito suspensivo (LEF art. 16 §1); extinguir/reduzir execucao;
  honorarios.

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
RESSALVA (PA-22): minuta — conferir garantia, prazo e documentos antes de protocolar.
```

---

## 5. EXCECAO DE PRE-EXECUTIVIDADE

Fundamento: **Sumula 393 STJ** — admissivel nas materias conheciveis de oficio que
nao demandem dilacao probatoria. `[PA-04 — confirmar redacao na fonte STJ]`

**Materias tipicas admitidas:**
- Prescricao (CTN art. 174) e decadencia (CTN arts. 150 §4 / 173, I)
- Nulidade absoluta da CDA (LEF art. 2 §5 — requisito essencial ausente)
- Ilegitimidade passiva (empresa incorreta; socio sem ato doloso — CTN 135)
- Falta de citacao valida
- Pagamento anterior a inscricao (com prova documental)

```
EXCECAO DE PRE-EXECUTIVIDADE — Processo n. ___

MM. JUIZ [...]

[NOME DA EMPRESA], por {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}},
nos autos da execucao fiscal n. ___, apresenta EXCECAO DE PRE-EXECUTIVIDADE
(STJ Sumula 393), pelos fundamentos a seguir.

I — DA ADMISSIBILIDADE: materia de ordem publica ([prescricao | decadencia |
  nulidade | ilegitimidade]); prova estritamente documental — sem dilacao
  probatoria (Sumula 393 STJ).

II — DA MATERIA:
  [Se prescricao:] CTN art. 174; constituicao definitiva em [data];
    prescricao em [data] [PA-03 — ESTIMATIVA — verificar interrupcoes];
    prova: documento juntado: ___.
  [Se decadencia:] CTN art. [150 §4 ou 173, I]; fato gerador [data];
    decadencia em [data] [PA-03 — verificar tipo de lancamento].
  [Se ilegitimidade:] nao e o sujeito passivo correto; documento juntado: ___.

III — DOS PEDIDOS: acolher excecao para [extinguir execucao / excluir executado];
  honorarios.

[Cidade, data] — {{ADVOGADO_NOME}} | OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
RESSALVA (PA-22): verificar se toda materia e ordem publica e prova e documentada.
```

---

## 6. REDIRECIONAMENTO AO SOCIO (CTN art. 135)

Fisco pede redirecionamento ao socio-gerente: defesa exige demonstrar ausencia de
dissolucao irregular (Sumula 435 STJ) e ausencia de ato doloso pessoal (CTN 135, III).
Divergencia sobre merito e responsabilidade = dilacao probatoria = embargos (com
garantia), nao excecao.

---

## 7. VEDACOES ESPECIFICAS

- **PA-08** — NUNCA confundir embargos (garantia + ampla prova) com excecao
  (sem garantia + so ordem publica + sem dilacao probatoria).
- **PA-03** — prazo de 30 dias dos embargos e estimativa. Confirmar data de ciencia.
- **PA-04** — Sumula 393 STJ e fundamento central — confirmar redacao. Nao inventar.
- **PA-09** — valor da execucao e estimativa; confirmar na CDA e PGFN.
- **PA-11** — esfera (federal/estadual/municipal) antes de redigir.
- **PA-22** — minuta; advogado assina antes do protocolo.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** — LEF, CTN e normas validadas.
- **Protocolo 3** — Sumula 393 e 435 STJ classificadas; modulacao verificada (PA-07).
- **Protocolo 4** — Justica Federal (tributos federais) ou Estadual/Municipal.
- **Protocolo 5** — valor da divida e garantia: estimativa (PA-09).

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`analise-auto-de-infracao` (Tier 5), `estrategia-de-caso-empresarial`,
`analise-documental-empresarial`, operador direto.

**Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio),
`calculo-e-prazos-tributarios`.

**Sem esta skill:** instrumento errado — embargos sem garantia extintos; excecao
com merito nao conhecida — defesa perdida totalmente.
