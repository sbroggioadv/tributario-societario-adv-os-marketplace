---
name: triagem-empresarial
description: >
  Porta de entrada de todo caso empresarial. Identifica dominio (societario/tributario), modo (consultivo/contencioso), competencia (federal/estadual/municipal; administrativa/judicial), prazos em curso, e grava no CASO.md. Aciona: novo caso, triagem, abrir caso, analisar demanda, cliente novo.
---

# TRIAGEM EMPRESARIAL

> Skill **Tier 1** — porta de entrada obrigatoria de todo caso empresarial. Executa entrevista estruturada, classifica dominio e modo, identifica competencia e prazos em curso, e grava o resultado no `CASO.md`. Sem triagem concluida, nenhuma skill estrategica (Tier 1-5) opera.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por `tributario-societario-master` ao receber novo caso, ou diretamente pelo operador com "novo caso", "triagem", "abrir caso", "analisar demanda", "cliente novo".

Entrega: `CASO.md` preenchido com dominio, modo, competencia, prazos e fase atual. Roteamento para o tier correto.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master` (Tier 0) ao receber demanda nova.
- **Entrega para:** `estrategia-de-caso-empresarial`, `analise-documental-empresarial`, `calculo-e-prazos-tributarios` (Tier 1) e skills Tier 2-5 via roteamento.
- **Pre-requisito para:** toda skill estrategica Tier 1-5 — sem `CASO.md` gravado, as skills operam sem contexto.

---

## 2. ENTREVISTA ESTRUTURADA DE TRIAGEM

Conduzir em ate 5 perguntas objetivas, na ordem abaixo. Adaptar conforme respostas anteriores.

### Bloco A — Identificacao do caso

```
1. Qual e o nome do cliente/empresa e o CNPJ ou CPF (se pessoa fisica)?
2. Qual e o problema ou demanda em termos praticos?
   (Ex.: "recebi um auto de infracao", "quero constituir uma holding",
    "fui notificado pela Junta Comercial", "preciso planejar tributacao da empresa".)
3. Ja existe algum processo, auto de infracao, CDA, notificacao ou prazo
   correndo? Se sim, qual a data do documento mais recente?
4. O fato que originou o caso ocorreu em qual ano/periodo?
   (Necessario para validar a legislacao aplicavel.)
5. Ja houve algum advogado ou consultoria trabalhando nesse caso antes?
   Se sim, ha documentos anteriores para analisar?
```

Respostas incompletas: fazer pergunta de acompanhamento cirurgica. Nao supor fatos — registrar como `[INFORMAR]` no `CASO.md`.

---

## 3. IDENTIFICACAO DO DOMINIO

Com base nas respostas, classificar o caso:

| Dominio | Indicadores tipicos |
|---------|---------------------|
| **Tributario** | Auto de infracao, CDA, notificacao fiscal, planejamento de tributos, IRPJ/CSLL/PIS/COFINS/ICMS/ISS/IPI, recuperacao de creditos, parcelamento, reforma tributaria (CBS/IBS) |
| **Societario** | Constituicao, alteracao, reorganizacao, dissolucao, saida de socio, M&A, holding, acordo de socios, registro Junta/RCPJ, governanca |
| **Tributario + Societario** | Reorganizacao com implicacao fiscal, holding com planejamento tributario, offshore/trust, estruturacao patrimonial, M&A com due diligence fiscal |

Registrar no `CASO.md`: `dominio: tributario | societario | tributario-societario`

---

## 4. IDENTIFICACAO DO MODO

| Modo | Indicadores |
|------|-------------|
| **Consultivo** | Planejamento, estruturacao, constituicao, orientacao preventiva, parecer, reorganizacao antes do fato gerador, contrato a redigir |
| **Contencioso** | Auto de infracao, CDA, notificacao fiscal, prazo processual em curso, defesa administrativa (CARF/TIT), execucao fiscal, acao judicial ja proposta ou a propor |
| **Consultivo + Contencioso** | Caso com fase preventiva e litigio ativo simultaneos (ex.: planejamento + defesa de auto anterior) |

Registrar no `CASO.md`: `modo: consultivo | contencioso | consultivo-contencioso`

---

## 5. PROTOCOLO DE COMPETENCIA (Protocolo 4)

Identificar obrigatoriamente antes de qualquer roteamento (PA-11):

### 5.1 Competencia tributaria federativa

| Tributo / Situacao | Competencia | Fiscalizacao | Contencioso adm. |
|--------------------|-------------|--------------|------------------|
| IRPJ, CSLL, PIS, COFINS, IPI, IOF, CIDE | Federal | RFB | CARF → CSRF |
| CBS (a partir de 2026) | Federal | RFB | CARF |
| ICMS, ITCMD | Estadual | SEFAZ | TIT (SP) / conselhos estaduais |
| ISS, IPTU, ITBI | Municipal | Prefeitura | Conselhos municipais |
| IBS (transicao) | Compartilhada | A definir em regulamentacao | A definir |

### 5.2 Competencia processual

```
Administrativo federal: DRJ (1a instancia) → CARF (2a) → CSRF (especial)
Administrativo estadual (ex. SP): Delegacia Tributaria → TIT
Administrativo municipal: Conselho Municipal de Contribuintes
Judicial: Vara Federal (tributos federais) → TRF → STJ (REsp) → STF (RE)
          Vara Civel/Empresarial (societario) → TJ → STJ
```

Registrar no `CASO.md`:
- `competencia_federativa: federal | estadual | municipal`
- `esfera: administrativa | judicial | administrativa-judicial`
- `orgao_atual: [DRJ/CARF/CSRF/TIT/Conselho/Vara/TRF/outra]`

---

## 6. MAPEAMENTO DE PRAZOS EM CURSO

Se houver processo ativo, identificar:

| Item | Verificar |
|------|-----------|
| Data do auto de infracao / CDA / notificacao | Calcular prazo de impugnacao / embargo |
| Impugnacao administrativa (30 dias — Dec. 70.235/72, art. 15) | Ja impugnou? Em prazo? |
| Recurso voluntario CARF (30 dias) | Acordao de 1a instancia data de? |
| Recurso especial CSRF (15 dias) | Acordao paradigma disponivel? |
| Embargos a execucao fiscal (30 dias + garantia) | CDA ajuizada? Data? |
| Mandado de seguranca repressivo (120 dias) | Data do ato coator? |
| Decadencia (CTN art. 150 §4o / art. 173) | Ano do fato gerador + 5 anos |
| Prescricao (CTN art. 174) | Constituicao definitiva + 5 anos |

> **PA-03:** nunca cravar prazo decadencial/prescricional sem ressalva de interrupcoes e suspensoes. Anotar como estimativa marcada.

Registrar no `CASO.md`:
- `prazo_mais_urgente: [descricao] — vence em [data estimada] [VERIFICAR]`
- `fase_processual: [pre-autuacao | autuado | impugnacao | recurso-carf | csrf | judicial | execucao]`

---

## 7. GRAVACAO NO CASO.md

Ao concluir a triagem, gerar ou atualizar o `CASO.md` com o cabecalho estruturado:

```markdown
# CASO.md — [Nome do Cliente / Empresa]

## Identificacao
- Cliente: [nome]
- CNPJ/CPF: [numero ou INFORMAR]
- Data de abertura: [DD/MM/AAAA]
- Ano do fato gerador principal: [AAAA ou INFORMAR]

## Classificacao
- Dominio: [tributario | societario | tributario-societario]
- Modo: [consultivo | contencioso | consultivo-contencioso]
- Competencia federativa: [federal | estadual | municipal]
- Esfera: [administrativa | judicial | administrativa-judicial]
- Orgao atual: [nome]

## Prazos em curso
- Prazo mais urgente: [descricao — vence em DD/MM/AAAA (estimativa, VERIFICAR)]
- Fase processual: [fase]

## Resumo da demanda
[2-4 linhas descrevendo o problema central do caso]

## Documentos recebidos
- [lista ou "nenhum ate o momento"]

## Selo de Validacao Legal
- [A emitir — acionar analisador-legislacao-vigente]

## Historico de updates
- [DD/MM/AAAA]: Triagem inicial concluida.
```

---

## 8. ROTEAMENTO POS-TRIAGEM

Com base em dominio + modo + competencia, rotear para:

| Classificacao | Proxima skill recomendada |
|---------------|--------------------------|
| Tributario + Contencioso | `analise-auto-de-infracao` (Tier 5) ou `analise-documental-empresarial` (Tier 1) |
| Tributario + Consultivo | `planejamento-tributario` (Tier 4) ou `estrategia-de-caso-empresarial` (Tier 1) |
| Societario + Consultivo | `escolha-tipo-societario` ou `constituicao-societaria` (Tier 2) |
| Tributario-Societario | `estrategia-de-caso-empresarial` (Tier 1) → skills Tier 2-5 conforme facetas |
| Execucao fiscal em curso | `pecas-defesa-execucao-fiscal` (Tier 5) — verificar prazo de embargo imediatamente |

**Sempre** solicitar acionamento do `analisador-legislacao-vigente` antes de qualquer estrategia.

---

## 9. VEDACOES ESPECIFICAS

- **PA-03** — nao cravar prazos decadenciais/prescricionais sem ressalva de interrupcoes.
- **PA-05** — nao confundir esfera administrativa e judicial.
- **PA-11** — nao concluir triagem sem identificar competencia federativa.
- **PA-22** — toda saida e minuta; o advogado responsavel valida antes de qualquer ato.
- Nao supor dominio ou modo sem perguntar — registrar como `[INFORMAR]` se incerto.

---

## 10. PROTOCOLOS ACIONADOS

- **Protocolo 4** (Competencia) — identificar obrigatoriamente na triagem.
- **Protocolo 1** (Validacao Legal Previa) — acionar `analisador-legislacao-vigente` logo apos triagem.

---

## 11. INTEGRACAO

**Chamada por:** `tributario-societario-master` ao receber novo caso.

**Entrega para:** `CASO.md` (gravacao) + skills Tier 1-5 (roteamento).

**Sem esta skill:** as skills estrategicas operam sem contexto de dominio/modo, gerando analise inadequada para o caso.
