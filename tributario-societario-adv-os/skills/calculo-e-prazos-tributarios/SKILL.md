---
name: calculo-e-prazos-tributarios
description: >
  Calculo tributario estimado (debito/credito, Selic, multas, atualizacao) e prazos processuais e decadenciais/prescricionais. Todo valor e estimativa marcada, sujeita a conferencia. Aciona: calcular, qual o prazo, decadencia, prescricao, valor do debito.
---

# CALCULO E PRAZOS TRIBUTARIOS

> Skill **Tier 1** — calculo tributario estimado e mapeamento de prazos processuais e decadenciais/prescricionais. Implementa o Protocolo de Calculo (todo valor e estimativa marcada) e o Protocolo de Competencia (prazos variam por esfera). Mode-aware: tributario contencioso e consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada com "calcular", "qual o prazo", "decadencia", "prescricao", "valor do debito", "atualizar o debito", "quanto deve", "prazo para impugnar", "prazo para recorrer".

Entrega: estimativa de valor atualizado em tabela estruturada + mapa de prazos com datas estimadas, todos marcados como estimativa sujeita a conferencia contabil/fiscal.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `analise-documental-empresarial`, `estrategia-de-caso-empresarial`, operador direto.
- **Entrega para:** `estrategia-de-caso-empresarial` (insumo para matriz de risco) + `CASO.md`.
- **Limitacao critica:** o plugin **nao tem acesso** a escrituracao fiscal do cliente (SPED, EFD-Contribuicoes, ECF, e-CAC). Todo calculo e baseado nos dados fornecidos pelo operador.

---

## 2. PROTOCOLO DE CALCULO (Protocolo 5) — REGRAS OBRIGATORIAS

### 2.1 Marcacao obrigatoria

Todo valor monetario calculado ou estimado nesta skill recebe a marcacao:

```
[ESTIMATIVA — sujeita a conferencia contabil/fiscal — PA-09]
```

Nunca apresentar valor como definitivo. O plugin nao substitui o calculo oficial (e-CAC, PGFN, SEFAZ) nem o trabalho do contador.

### 2.2 Limitacoes declaradas

Declarar antes de qualquer calculo: baseado nos dados do operador; sem acesso a SPED/EFD/ECF/e-CAC; Selic datada (reverificar mensalmente); multas baseadas no fundamento do auto; garantia processual: usar valor oficial RFB/PGFN.

### 2.3 Formato da tabela de calculo

```
ESTIMATIVA DE DEBITO TRIBUTARIO — [nome do caso] — [DD/MM/AAAA]
[ESTIMATIVA — sujeita a conferencia contabil/fiscal — PA-09]

| Item               | Valor (R$) | Base | Data-base |
|--------------------|------------|------|-----------|
| Tributo principal  |            | [norma/auto] | [data] |
| Multa de oficio    |            | [art. X Lei Y] | [data] |
| Multa qualificada  | N/A ou %   | [se houver agravamento] | |
| Juros (Selic)      |            | [taxa ref. + periodo] | [DD/MM/AAAA] |
| **Total estimado** |            | | [DD/MM/AAAA] |

Projecao Selic: indicar meses adicionais e taxa estimada; total projetado sempre marcado [ESTIMATIVA].
```

---

## 3. REGRAS DE CALCULO — TRIBUTOS FEDERAIS

### 3.1 Multas (federal — RFB)

| Tipo | Percentual | Fundamento |
|------|-----------|------------|
| Multa de lancamento de oficio | 75% do tributo | Art. 44, I, Lei 9.430/1996 |
| Multa qualificada (fraude/dolo/simulacao) | 150% do tributo | Art. 44, II, Lei 9.430/1996 |
| Multa por reincidencia | +50% sobre a multa | Art. 44, §1o, Lei 9.430/1996 |
| Multa isolada (descumprimento obrigacao acessoria) | Variavel por tipo | [VERIFICAR norma especifica] |

> **PA-04** — confirmar na fonte oficial (SIJUT) o percentual exato da multa citada no auto antes de usar.

### 3.2 Juros — Selic

Selic acumulada desde o vencimento (art. 13 Lei 9.065/1995 c/c art. 61 Lei 9.430/1996). Incide sobre tributo + multa. Indicar data-base. Reverificar taxa mensal em bcb.gov.br.

### 3.3 Parcelamento

Verificar existencia de programa especial vigente (PERT ou similar) — condicoes variam por prazo de adesao. `[VERIFICAR — Fonte: RFB / PGFN]`

---

## 4. REGRAS DE CALCULO — TRIBUTOS ESTADUAIS E MUNICIPAIS

Calculos de ICMS (estadual) e ISS (municipal) dependem de:
- Regulamento estadual/municipal vigente na data do fato gerador (PA-02);
- Aliquota especifica do estado/municipio;
- Multas e juros previstos na legislacao local — **nao usar percentuais federais**.

> **PA-06** — regime e aliquota sempre datados pelo fato gerador.
> Sinalizar ao operador: "Informar o estado/municipio e a data do fato gerador para calculo com legislacao correta."

---

## 5. DECADENCIA — REGRAS DO CTN

A decadencia extingue o direito de a Fazenda constituir o credito tributario. Mapear antes de qualquer defesa.

### 5.1 Lancamento por homologacao (contribuinte apura e recolhe — IRPJ, CSLL, PIS, COFINS, ICMS declarado, ISS declarado)

**CTN art. 150, §4o:** prazo de 5 anos a contar da data do fato gerador.

```
Fato gerador: [DD/MM/AAAA]
Prazo de decadencia: 5 anos = [DD/MM/AAAA] [VERIFICAR — possivel suspensao/interrupcao]
Situacao: [vencido / em curso / verificar]
```

**Excecao — dolo, fraude ou simulacao:** prazo conta a partir do 1o dia do exercicio seguinte ao que o lancamento poderia ter sido efetuado (art. 173, I) — nao do fato gerador. Resultado: prazo mais longo.

### 5.2 Lancamento de oficio (IPVA, IPTU e lancamentos diretos)

**CTN art. 173, I:** prazo de 5 anos a contar do 1o dia do exercicio seguinte ao que o lancamento poderia ter sido efetuado.

```
Exercicio do fato gerador: [AAAA]
Inicio do prazo: 1o dia do exercicio seguinte = 01/01/[AAAA+1]
Vencimento da decadencia: 01/01/[AAAA+6] [VERIFICAR]
```

### 5.3 Interruptores da decadencia

Regra geral: nao ha causas de suspensao ou interrupcao da decadencia no CTN — o prazo corre de forma irrefragavel. Excecao (art. 173, II): quando um lancamento e anulado por vicio formal em decisao definitiva, o prazo de 5 anos reinicia da data dessa decisao — o Fisco pode lavrar novo lancamento. Sinalizar [VERIFICAR — art. 173, II aplicavel?] sempre que houver lancamento anterior anulado.

> **PA-03** — ao informar prazo decadencial, sempre incluir: "Prazo estimado. Verificar data exata do fato gerador, possibilidade de lancamento por homologacao vs. de oficio, e eventuais decisoes judiciais que afastem a decadencia no caso concreto."

---

## 6. PRESCRICAO — REGRAS DO CTN

A prescricao extingue a acao de cobranca do credito ja constituido definitivamente.

**CTN art. 174:** prazo de 5 anos a contar da constituicao definitiva do credito tributario.

### 6.1 Marco inicial da prescricao

```
Constituicao definitiva = data em que o credito nao comporta mais recurso administrativo.
Exemplos:
  - Auto de infracao sem impugnacao: data do fim do prazo de impugnacao (30 dias)
  - Auto de infracao com recursos esgotados: data da decisao final do CARF/CSRF
  - Declaracao do contribuinte sem pagamento (DCTF, GIA): data do vencimento da declaracao
    (Sumula 436 STJ: a entrega da declaracao constitui o credito, dispensando o lancamento)

Constituicao definitiva no caso: [DD/MM/AAAA ou VERIFICAR]
Prazo prescricional: 5 anos = [DD/MM/AAAA] [VERIFICAR]
```

### 6.2 Interrupcao da prescricao (CTN art. 174, paragrafo unico)

Causas (reiniciam do zero): despacho do juiz que ordena citacao em execucao fiscal; protesto judicial; ato judicial que constitua em mora o devedor; reconhecimento expresso do debito pelo devedor.

Suspensao da exigibilidade (CTN art. 151): moratoria, deposito integral, impugnacoes/recursos, liminar/tutela, parcelamento — suspende a prescricao durante o periodo.

> **PA-03** — nunca cravar prazo prescricional sem verificar interrupcoes e suspensoes no historico do processo.

---

## 7. PRAZOS PROCESSUAIS — MAPA RAPIDO

### 7.1 Contencioso administrativo federal (Dec. 70.235/72 + Lei 14.689/23)

| Ato | Prazo | Referencia |
|-----|-------|------------|
| Impugnacao ao auto de infracao | 30 dias da ciencia | Dec. 70.235/72, art. 15 |
| Recurso voluntario ao CARF | 30 dias da ciencia do acordao de 1a instancia | Dec. 70.235/72, art. 33 |
| Recurso especial a CSRF | 15 dias da ciencia + exige acordao paradigma de camara diferente | Dec. 70.235/72, art. 37 |

### 7.2 Contencioso judicial

| Acao | Prazo | Referencia |
|------|-------|------------|
| Embargos a execucao fiscal | 30 dias da penhora/citacao + exige garantia | LEF art. 16 (Lei 6.830/80) |
| Excecao de pre-executividade | Sem prazo fixo; apenas materias de ordem publica | Sumula 393 STJ |
| Mandado de seguranca repressivo | 120 dias do ato coator | Lei 12.016/2009, art. 23 |
| Acao anulatoria de debito fiscal | 5 anos da constituicao definitiva | CTN art. 174 (prescricao) |
| Repeticao de indebito | 5 anos do pagamento indevido | CTN art. 168, I |
| Apelacao (CPC) | 15 dias da intimacao da sentenca | CPC art. 1.003, §5o |
| Recurso Especial (STJ) | 15 dias da publicacao do acordao | CPC art. 1.003, §5o |

### 7.3 Formato do mapa de prazos

```
MAPA DE PRAZOS — [nome do caso] — [DD/MM/AAAA]

Prazo mais urgente:
  Ato: [descricao]
  Data do termo inicial: [DD/MM/AAAA]
  Prazo legal: [X dias]
  Vencimento estimado: [DD/MM/AAAA] [ESTIMATIVA — VERIFICAR dias uteis e eventuais suspensoes]
  Status: [em curso / vencido / nao iniciado]

Prazos secundarios:
  [lista com mesmo formato]

Prazos de longo prazo:
  Decadencia: [vence em DD/MM/AAAA — VERIFICAR]
  Prescricao: [vence em DD/MM/AAAA — VERIFICAR]
```

---

## 8. CALCULO DE CREDITO A RECUPERAR

Campos minimos: tributo + periodo + regime (PIS/COFINS: nao-cumulativo 9,25% vs cumulativo 3,65%) + base do credito + valor estimado [ESTIMATIVA] + forma de aproveitamento (PER/DCOMP / restituicao) + prescricao 5 anos (CTN art. 168). Calculo final exige levantamento contabil — sem acesso a EFD/SPED.

---

## 9. VEDACOES ESPECIFICAS

- **PA-03** — nao cravar prazo decadencial/prescricional sem ressalva de interrupcoes/suspensoes.
- **PA-06** — regime tributario e aliquota sempre datados pelo fato gerador.
- **PA-09** — todo valor e estimativa marcada. Nunca apresentar como definitivo.
- **PA-22** — toda saida e minuta; o advogado e contador responsaveis validam antes de qualquer ato.
- Nao calcular sem dados fornecidos pelo operador — nunca supor base de calculo.
- Nao usar percentuais federais para tributos estaduais ou municipais sem verificar a legislacao local.

---

## 10. PROTOCOLOS ACIONADOS

- **Protocolo 5** (Calculo) — esta skill **e** o Protocolo 5 em operacao. Todo valor e estimativa.
- **Protocolo 4** (Competencia) — identificar a esfera para aplicar a legislacao correta de prazos e multas.
- **Protocolo 1** (Validacao Legal Previa) — confirmar que a norma de calculo (multa, juros, prazo) esta vigente no ano do fato gerador.

---

## 11. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `analise-documental-empresarial`, `estrategia-de-caso-empresarial`, operador direto.

**Entrega para:** `estrategia-de-caso-empresarial` (insumo para matriz de risco) + `CASO.md` (prazo mais urgente + estimativa de debito).

**Sem esta skill:** estrategia montada sem mapa de prazos — risco de perda de prazo fatal e calculo de debito errado.
