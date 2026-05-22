---
name: parecer-e-consulta-fiscal
description: >
  Parecer tributario fundamentado com ressalvas e graduacao de risco (provavel/possivel/
  remoto) e formulacao de consulta fiscal formal aos orgaos fazendarios (RFB, SEFAZ,
  Prefeitura). Toda entrega abre com data de validacao legal e fecha com ressalva OAB.
  Nunca substitui o juizo do advogado responsavel. Aciona: parecer, consulta fiscal,
  opiniao legal, analise de viabilidade de tese, pergunta formal a Receita, COSIT.
---

# PARECER E CONSULTA FISCAL

> Skill **Tier 4 — Tributario Consultivo** — estrutura o parecer tributario fundamentado
> (com ressalvas e graduacao de risco) e a consulta fiscal formal aos orgaos fazendarios.
> Implementa PA-01, PA-03, PA-04, PA-07, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "parecer tributario", "consulta fiscal", "opiniao legal", "analise de viabilidade
de tese", "pergunta formal a Receita", "COSIT", "consulta formal ao Fisco", "opiniao sobre
tributacao", "parecer sobre ICMS", "posso fazer isso", "qual o risco dessa operacao".

Entrega: parecer tributario estruturado (FIRAC + graduacao de risco) OU minuta de consulta
fiscal formal para o orgao competente.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `estrategia-de-caso-empresarial` (Tier 1), operador direto.
- **Entrega para:** `mitigacao-de-risco-fiscal` (Tier 4) se o parecer identificar risco
  de elisao abusiva ou evasao; `suprema-corte-empresarial` (R1-R4 obrigatorio antes da
  entrega ao cliente).
- **Pre-requisito:** `analisador-legislacao-vigente` emitir Selo de Validacao Legal (PA-01);
  Protocolo 1 completo.

---

## 2. PARECER TRIBUTARIO — ESTRUTURA FIRAC

Todo parecer desta skill segue a estrutura FIRAC:

```
PARECER TRIBUTARIO — [TITULO]
Data de validacao legal: [DD/MM/AAAA]
Base normativa auditada ate: [DD/MM/AAAA]

F — FATOS
  [Descricao objetiva dos fatos relevantes — quem, o que, quando, valor, competencia]

I — QUESTAO (ISSUE)
  [A questao juridica precisa que o parecer deve responder]

R — REGRA
  [Normas vigentes identificadas + classificacao jurisprudencial]

A — APLICACAO
  [Subsuncao dos fatos a norma + analise de risco]

C — CONCLUSAO
  [Resposta precisa a questao + classificacao de risco + orientacao pratica]

RESSALVA OBRIGATORIA (PA-22):
  Este parecer e uma analise juridica preliminar baseada nas informacoes
  fornecidas e nas normas vigentes na data-base indicada. Nao substitui o
  juizo profissional do advogado responsavel, que deve revisar e assinar
  antes de qualquer ato. Alteracoes normativas posteriores podem modificar
  as conclusoes. OAB.
```

---

## 3. GRADUACAO DE RISCO DO PARECER

Todo parecer deve classificar a tese/operacao em um dos tres niveis:

| Nivel | Criterio de aplicacao |
|-------|-----------------------|
| **Provavel** (>60%) | Norma expressa favoravel; tese vinculante STF/STJ favoravel sem modulacao adversa; pratica reiterada da RFB/SEFAZ sem autuacao conhecida; doutrina e jurisprudencia convergentes. |
| **Possivel** (30-60%) | Norma admite duas ou mais interpretacoes defensaveis; tese em disputa no CARF ou entre TRFs; divergencia de Solucoes de Consulta COSIT; jurisprudencia estadual vs federal conflitante. |
| **Remoto** (<30%) | Tese ja rejeitada por STF/STJ com transito; sumula vinculante ou tese repetitiva contraria; multa qualificada (150%) provavel se rejeitada; estrutura com risco de requalificacao por simulacao. |

> Aplicar os criterios do Protocolo 3 (Jurisprudencial) — classificar cada tese em
> vinculante/em disputa/superada antes de graduar o risco.

### 3.1 Formato da secao de risco no parecer

```
GRADUACAO DE RISCO
Tese/Operacao: [descricao]
Classificacao: [Provavel | Possivel | Remoto]
Fundamento da classificacao:
  - Norma: [...]
  - Jurisprudencia: [vinculante/em disputa/superada — citar ou [VERIFICAR]]
  - Modulacao de efeitos: [sim/nao — detalhe se sim]
Mitigadores disponiveis: [...]
Exposicao financeira estimada se rejeitada: R$ ___ (estimativa — PA-09)
Orientacao pratica: [o que o advogado deve fazer a seguir]
```

---

## 4. FUNDAMENTACAO JURIDICA DO PARECER

### 4.1 Como tratar normas

- **Norma vigente:** citar dispositivo + texto relevante + data de vigencia confirmada
  (PA-02). Usar linguagem: "nos termos do art. X da Lei Y, vigente no exercicio Z...".
- **Norma alterada ou revogada:** nunca citar como vigente sem ressalva. Se a norma mudou
  no periodo relevante, indicar a redacao aplicavel ao fato gerador especifico.
- **Norma incerta:** quando a vigencia ou redacao nao estiver confirmada, usar
  `[VERIFICAR redacao e vigencia no ano do fato gerador]`.
- **PA-04 — alucinacao de precedente:** nunca inventar numero de Tema, Sumula ou acordao.
  Se nao ha certeza, usar `[VERIFICAR — confirmar numero na fonte oficial]`.

### 4.2 Como tratar jurisprudencia

```
Classificacao obrigatoria de cada precedente citado:
  [Vinculante] Tema ___ STF/STJ — Resultado: [favoravel/desfavoravel] —
    Modulacao: [sim/nao — a partir de DD/MM/AAAA]
  [Em disputa] Tese em julgamento — pauta prevista: [data ou VERIFICAR] —
    Posicoes: [resumo dos dois lados]
  [Superado] Tese X, antes fundamentada em [precedente antigo], foi superada
    por [Tema ___ / Sumula ___] — nao usar para fundamentar estrategia.
```

---

## 5. CONSULTA FISCAL FORMAL

### 5.1 Quando usar

A consulta fiscal formal (arts. 46-58 do Decreto 70.235/72 + IN RFB 1.396/2013 e alteracoes
`[VERIFICAR versao vigente]`) e o instrumento para obter pronunciamento oficial do Fisco
sobre a interpretacao de norma tributaria em relacao a fato determinado do consulente.

**Quando recomendar:** tese juridica com resultado Possivel ou incerto; operacao relevante
cujo tratamento tributario e controverso; duvida genuina sobre subsuncao do fato a norma;
situacao nao coberta por Solucao de Consulta COSIT publicada.

**Efeito da consulta respondida (IN RFB 1.396/2013 art. 9):** durante a tramitacao e ate 30
dias apos a intimacao da decisao, suspende o curso do prazo para recolhimento do tributo
objeto da consulta (se o tributo ainda nao venceu) e impede lavratura de auto de infracao
`[VERIFICAR alcance exato da protecao na versao vigente da IN]`.

### 5.2 Competencia para receber a consulta

- **RFB (COSIT/SRRF):** tributos federais (IRPJ, CSLL, PIS, COFINS, IPI, INSS).
- **SEFAZ estadual:** ICMS.
- **Secretaria Municipal / Conselho de Contribuintes Municipal:** ISS, IPTU, ITBI.

### 5.3 Minuta de consulta fiscal — estrutura

```
CONSULTA FISCAL — [DATA]
[Timbrado do escritorio — {{FIRM_NAME}} — {{CIDADE}}/{{UF}}]

AO AUDITOR-FISCAL DA RECEITA FEDERAL DO BRASIL / [ORGAO COMPETENTE]
[Endereco / canal oficial]

IDENTIFICACAO DO CONSULENTE
  Razao Social: [nome da empresa cliente]
  CNPJ: [CNPJ]
  Endereco: [endereco do estabelecimento]
  Atividade: [CNAE principal]
  Representante: {{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}

QUESTAO CONSULTADA
  [Descrever a questao juridica de forma precisa e em relacao a fato determinado]

DESCRICAO DOS FATOS
  [Descricao objetiva dos fatos com documentos de suporte disponiveis]

LEGISLACAO APLICAVEL
  [Elencar normas relevantes com texto dos dispositivos pertinentes]

INTERPRETACAO DO CONSULENTE
  [Posicao do consulente sobre a interpretacao da norma — obrigatorio pela IN]

FORMULACAO DO PEDIDO
  Requer seja a presente Consulta recebida e respondida nos termos do art. 46
  do Decreto 70.235/72 e da IN RFB [numero vigente], esclarecendo:
  [Pergunta objetiva 1]
  [Pergunta objetiva 2, se houver]

[cidade], [data]
{{ADVOGADO_NOME}} — OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
```

> **PA-22** — a minuta deve ser revisada e assinada pelo advogado responsavel antes do envio.
> Consultas com fatos incompletos ou interpretacao mal formulada podem ser ineficazes.

---

## 6. VEDACOES ESPECIFICAS

- **PA-01** — nenhum parecer sem Selo de Validacao Legal emitido.
- **PA-03** — nao cravar prazo prescricional ou decadencial como definitivo sem ressalva.
- **PA-04** — zero alucinacao: precedente sem certeza = `[VERIFICAR — confirmar na fonte]`.
- **PA-07** — nao omitir modulacao de efeitos em tese com modulacao.
- **PA-22** — toda entrega e minuta sujeita a revisao e responsabilidade do advogado OAB.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — pre-requisito absoluto; Selo exigido antes do parecer.
- **Protocolo 3** (Jurisprudencial) — classificar cada tese citada: vinculante/em disputa/
  superada; verificar modulacao de efeitos (PA-07).
- **Protocolo 4** (Competencia) — identificar orgao fazendario correto (federal/estadual/
  municipal) antes de formular a consulta.
- **Protocolo 5** (Calculo) — exposicao financeira no parecer e estimativa marcada.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`estrategia-de-caso-empresarial` (Tier 1).

**Entrega para:** `mitigacao-de-risco-fiscal` (Tier 4) se risco identificado,
`suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega ao cliente).

**Sem esta skill:** cliente operando sem parecer fundamentado sobre teses controversas;
consulta fiscal formulada de forma incorreta (sem interpretacao do consulente — invalida
pela IN RFB); risco Possivel ou Remoto nao comunicado ao cliente.
