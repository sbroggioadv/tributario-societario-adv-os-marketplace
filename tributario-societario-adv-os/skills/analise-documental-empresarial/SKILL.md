---
name: analise-documental-empresarial
description: >
  Le e mapeia documentos — autos de infracao, CDA, contratos sociais, atas, declaracoes, decisoes administrativas e judiciais, minutas de terceiros — extraindo fatos, prazos e riscos. Aciona: analisar documento, ler auto de infracao, revisar contrato, o que diz esse documento.
---

# ANALISE DOCUMENTAL EMPRESARIAL

> Skill **Tier 1** — leitura e mapeamento de documentos empresariais (tributarios e societarios). Extrai fatos, prazos criticos e riscos de cada tipo de documento. Mode-aware: tributario contencioso (auto de infracao, CDA, decisoes), societario consultivo (contrato social, ata, acordo, SPA).

---

## 0. ESCOPO E ACIONAMENTO

Acionada com "analisar documento", "ler auto de infracao", "revisar contrato", "o que diz esse documento", "mapear o processo". O operador fornece o texto ou descricao do documento.

Entrega: ficha de analise estruturada com fatos, prazos, riscos e flag de inconsistencias.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`, operador direto.
- **Entrega para:** `estrategia-de-caso-empresarial` (insumo factual), skills Tier 2-5 conforme dominio do documento.
- **Integra com:** `CASO.md` — atualizar secao "Documentos recebidos" e registrar fatos relevantes.

---

## 2. IDENTIFICACAO DO TIPO DE DOCUMENTO

Antes de iniciar a leitura, identificar a categoria:

| Categoria | Documentos |
|-----------|-----------|
| **Tributario contencioso** | Auto de Infracao, Notificacao Fiscal, CDA, Acordao DRJ/CARF/CSRF, Mandado de Penhora |
| **Tributario consultivo** | Consulta Fiscal, Solucao de Consulta COSIT, Parecer Normativo |
| **Societario** | Contrato Social, Estatuto Social, Alteracao Contratual, Ata, Acordo de Socios/Acionistas, Distrato |
| **M&A / Estruturacao** | SPA, MOU, Term Sheet, Laudo de Avaliacao, Relatorio de Due Diligence |
| **Decisao judicial** | Sentenca, Acordao TRF/TJ, Acordao STJ/STF, Mandado de Penhora |
| **Documentos mistos** | Contrato com clausula fiscal, Ata com deliberacao sobre reorganizacao |

---

## 3. CHECKLIST DE LEITURA — AUTO DE INFRACAO

Documento tributario contencioso mais comum. Ler sistematicamente:

```
FICHA — AUTO DE INFRACAO
Numero do auto: [XXXXX]
Data de lavratura: [DD/MM/AAAA]
Autoridade lavradora: [nome + cargo + matricula]
Tributado autuado: [nome/CNPJ]
Tributo(s) exigido(s): [IRPJ/CSLL/PIS/COFINS/ICMS/ISS/outro]
Periodo de apuracao: [mes/ano a mes/ano]

VICIO FORMAL:
[ ] Identificacao completa do autuado
[ ] Identificacao do agente fiscal e delegatario competente
[ ] Descricao clara do fato tributavel
[ ] Base legal expressa (art. X da Lei Y)
[ ] Valor do tributo, multa e juros discriminados
[ ] Intimacao valida (data + meio + prova de recebimento)
[ ] Prazo de impugnacao indicado

MERITO — PONTOS DE ATAQUE:
[ ] Fato gerador descrito e aquele que realmente ocorreu?
[ ] Regime tributario correto para o periodo autuado?
[ ] Calculo da base de calculo esta correto?
[ ] Aliquota aplicada e a vigente no periodo? (PA-06)
[ ] Multa: fundamento legal expresso? Percentual correto?
[ ] Juros: Selic desde quando?
[ ] Decadencia: fato gerador ha mais de 5 anos? (CTN art. 150 §4o ou art. 173)
[ ] Prescricao: credito ja constituido ha mais de 5 anos? (CTN art. 174)

PRAZO DE IMPUGNACAO:
Data da intimacao: [DD/MM/AAAA]
Prazo legal: 30 dias (Dec. 70.235/72, art. 15)
Vencimento estimado: [DD/MM/AAAA] [VERIFICAR — contar dias uteis conforme regulamento]

VALOR DO DEBITO:
Tributo: R$ [valor] (estimativa dos dados do auto — PA-09)
Multa: R$ [valor] — fundamento: [art. X Lei Y]
Juros (Selic): R$ [valor estimado na data do auto]
Total na data do auto: R$ [valor] [ESTIMATIVA — VERIFICAR com contador]
```

---

## 4. CHECKLIST DE LEITURA — CDA (CERTIDAO DE DIVIDA ATIVA)

```
FICHA — CDA
Numero: [XXXXX]
Inscricao em DA em: [DD/MM/AAAA]
Devedor: [nome/CNPJ]
Tributo: [tipo + periodo]
Valor inscrito: R$ [valor] [ESTIMATIVA — atualizar pela Selic ate hoje]
Ajuizamento da execucao fiscal: [sim/nao — data se sim]
Garantia exigida: [penhora/seguro/deposito]

PRAZO DE EMBARGOS (se execucao ajuizada):
Data da penhora/citacao: [DD/MM/AAAA]
Prazo: 30 dias (LEF art. 16)
Vencimento estimado: [DD/MM/AAAA] [VERIFICAR]

ANALISE DE VICIO NA CDA:
[ ] Nome e endereco do devedor corretos?
[ ] Fundamento legal da divida indicado?
[ ] Valor original e encargos discriminados?
[ ] Data da inscricao compativel com a decadencia?
[ ] Regularidade formal da certidao (assinatura + cargo do procurador)?

EXCECAO DE PRE-EXECUTIVIDADE (sem garantia):
Cabimento apenas para materias de ordem publica:
  [ ] Prescricao/decadencia
  [ ] Ilegitimidade de parte
  [ ] Vicio formal da CDA
  [ ] Incompetencia absoluta do juizo
  Sumula 393 STJ — limite: materia de prova simples, sem dilacao probatoria
```

---

## 5. CHECKLIST DE LEITURA — CONTRATO SOCIAL / ESTATUTO

```
FICHA — CONTRATO SOCIAL / ESTATUTO
Tipo societario: [LTDA / SLU / S/A / SAS / Simples / SCP]
Data de constituicao: [DD/MM/AAAA]
NIRE / Registro Junta: [numero]
CNPJ: [numero]
Socios/acionistas: [nome + qualificacao + participacao %]

OBJETO SOCIAL:
  [ ] Objeto compativel com atividade exercida?
  [ ] Adequado para o regime tributario (Simples/Presumido/Real)?
  [ ] Vedacoes setoriais respeitadas?

CAPITAL SOCIAL:
  [ ] Valor integralizado vs subscrito
  [ ] Integralizacao em prazo e forma legal

ADMINISTRACAO:
  [ ] Gerente(s)/diretor(es) identificados
  [ ] Poderes de representacao expressos e limitados
  [ ] Responsabilidade solidaria/subsidiaria do administrador indicada?

DELIBERACOES — QUORUM:
  [ ] Quorum de alteracao contratual: maioria simples (>50%) [Lei 14.451/2022]
  [ ] Quorum para exclusao de socio: maioria representando +50% [CC 1.085]
  [ ] Quorum para dissolucao: conforme contrato ou CC
  Atencao: quorum de 3/4 da LTDA nao existe mais — Lei 14.451/2022

CLAUSULAS DE RISCO:
  [ ] Nao-concorrencia com limites de prazo/territorio/atividade (PA-18)?
  [ ] Pre-empcao / direito de preferencia?
  [ ] Dissolucao parcial em caso de morte/exclusao?

REGISTRO:
  Tipo: [Junta Comercial / RCPJ]
  Status: [registrado/pendente/irregular]
  Data do ultimo arquivamento: [DD/MM/AAAA]
```

---

## 6. CHECKLIST DE LEITURA — ATA DE ASSEMBLEIA / REUNIAO

```
FICHA — ATA
Tipo: [assembleia geral / reuniao de socios / reuniao de diretoria]
Data: [DD/MM/AAAA]
Quorum de instalacao: [% do capital presente] — valido?
Quorum de deliberacao: [% votaram a favor] — legal para a materia?
Materia deliberada: [descricao]
Resultado: [aprovado/rejeitado/parcial]

PONTOS DE ATENCAO:
  [ ] Convocacao regular (prazo + forma + pauta)?
  [ ] Socios dissidentes registrados?
  [ ] Assinatura de todos os presentes?
  [ ] Averbacao necessaria (Junta Comercial/RCPJ) ja providenciada?
  [ ] Acordos de voto averbados (art. 118 LSA se S/A)?
```

---

## 7. CHECKLIST DE LEITURA — DECISAO ADMINISTRATIVA (DRJ/CARF/CSRF)

```
FICHA — DECISAO ADMINISTRATIVA
Orgao: [DRJ / CARF 1a/2a/3a Secao / CSRF]
Numero do processo: [XXXXX]
Data da decisao: [DD/MM/AAAA]
Resultado: [provimento total/parcial/improvimento/empate — favorece o contribuinte (Lei 14.689/2023)]

ANALISE DO ACORDAO:
  [ ] Fundamentacao legal da decisao correta?
  [ ] Tese acolhida ou rejeitada (classificar: vinculante/em disputa/superada)?
  [ ] Ha acordao paradigma para Recurso Especial CSRF?
  [ ] Modulacao de efeitos aplicavel?
  [ ] Decisao colegiada ou singula? Casting vote (Pres. CARF)?

PRAZO DE RECURSO:
  Recurso Voluntario CARF: 30 dias da ciencia do acordao de 1a instancia
  Recurso Especial CSRF: 15 dias da ciencia + exige acordao de camara diferente divergente
  Acao Anulatoria judicial: prescricao de 5 anos (CTN art. 174) apos constituicao definitiva
  Vencimento estimado: [DD/MM/AAAA] [VERIFICAR]
```

---

## 8. CHECKLIST DE LEITURA — SPA / MOU / TERM SHEET

```
FICHA — DOCUMENTO M&A
Tipo: [SPA / MOU / Term Sheet / Carta de Intencoes]
Partes: [comprador / vendedor / target]
Data: [DD/MM/AAAA]
Status: [vinculante/nao-vinculante]

CLAUSULAS CRITICAS:
  [ ] Preco e mecanismo de ajuste (locked box / closing accounts)
  [ ] Reps & Warranties: abrangencia, sobrevivencia, baskets
  [ ] MAC (Material Adverse Change): definicao e alcance
  [ ] Earnout: metricas, prazo, controle do negocio no periodo
  [ ] Escrow: valor, prazo, condicoes de liberacao
  [ ] Nao-concorrencia: prazo/territorio/atividade (PA-18)?
  [ ] Condicoes precedentes (CPs): aprovacao regulatoria (CADE?), due diligence, aprovacoes societarias

RISCOS IDENTIFICADOS:
  [ ] Contingencias fiscais nao reveladas?
  [ ] Due diligence societaria completa?
  [ ] Riscos trabalhistas e previdenciarios do target?
  [ ] Passivos ambientais?
```

---

## 9. FORMATO DE ENTREGA

```
ANALISE DOCUMENTAL — [tipo do documento] — [nome do caso]
Data da analise: [DD/MM/AAAA]

TIPO: [categoria]
IDENTIFICACAO: [numero/data/partes]

FATOS EXTRAIDOS:
  [lista dos fatos juridicamente relevantes]

PRAZOS CRITICOS:
  - [descricao do prazo] — vence em [DD/MM/AAAA] [ESTIMATIVA — VERIFICAR]

RISCOS IDENTIFICADOS:
  - [risco 1 — nivel: alto/medio/baixo]
  - [risco 2 — ...]

PONTOS DE ATENCAO ESPECIFICOS:
  - [detalhe relevante para a estrategia]

INCONSISTENCIAS DETECTADAS:
  - [o que parece incorreto ou incompleto no documento — marcar [VERIFICAR]]

RECOMENDACAO DE ACAO:
  [proxima acao recomendada com base na analise]

RESSALVA: esta analise e baseada no documento fornecido. Sujeita a revisao
pelo advogado responsavel. PA-22.
```

---

## 10. VEDACOES ESPECIFICAS

- **PA-03** — nao cravar prazo decadencial/prescricional sem ressalva de interrupcoes e suspensoes.
- **PA-04** — zero alucinacao de artigo, lei, sumula ou tema — marcar `[VERIFICAR]`.
- **PA-06** — nao aplicar regime tributario sem datar o fato gerador.
- **PA-08** — nao confundir embargos a execucao x excecao de pre-executividade.
- **PA-09** — qualquer valor monetario e estimativa marcada.
- **PA-13** — verificar quorum legal de deliberacao societaria; quorum de 3/4 nao existe mais na LTDA (Lei 14.451/2022).
- **PA-15** — verificar necessidade de registro Junta/RCPJ e averbacao de acordo.
- **PA-22** — toda saida e minuta; advogado responsavel valida.

---

## 11. PROTOCOLOS ACIONADOS

- **Protocolo 4** (Competencia) — identificar o orgao emissor do documento e a esfera competente.
- **Protocolo 5** (Calculo) — qualquer valor extraido do documento e marcado como estimativa.
- **Protocolo 3** (Jurisprudencial) — ao identificar tese citada no documento, classificar.

---

## 12. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, operador direto.

**Entrega para:** `estrategia-de-caso-empresarial` (insumo factual) + `CASO.md` (secao "Documentos recebidos" + fatos e prazos).

**Sem esta skill:** estrategia montada sem base documental verificada — risco de erro factual grave.
