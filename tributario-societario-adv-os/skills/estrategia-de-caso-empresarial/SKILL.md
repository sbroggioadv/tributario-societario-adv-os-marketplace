---
name: estrategia-de-caso-empresarial
description: >
  Define a estrategia do caso — mapa de teses, classificacao jurisprudencial (vinculante/em disputa/superada), analise de risco, decisao via administrativa vs judicial. Aciona: estrategia, qual a melhor via, analise de risco, tese, vale a pena recorrer.
---

# ESTRATEGIA DE CASO EMPRESARIAL

> Skill **Tier 1** — define a estrategia do caso empresarial (tributario ou societario). Aplica o Protocolo Jurisprudencial, constroi o mapa de teses, quantifica o risco e decide entre via administrativa e judicial. Mode-aware: consultivo (planejamento e orientacao) e contencioso (decisao de forum e tese).

---

## 0. ESCOPO E ACIONAMENTO

Acionada apos triagem concluida e Selo de Validacao Legal emitido. Gatilhos: "estrategia", "qual a melhor via", "analise de risco", "tese", "vale a pena recorrer", "montar o plano do caso".

Entrega: mapa de teses com classificacao jurisprudencial + matriz de risco + recomendacao de via (administrativa x judicial) + proximos passos.

---

## 1. POSICAO NA ORQUESTRA

- **Pre-requisito:** `CASO.md` gravado (triagem concluida) + Selo de Validacao Legal emitido.
- **Chamada por:** `tributario-societario-master`, operador direto.
- **Entrega para:** skills Tier 2-5 (societario, estruturacao, tributario consultivo, contencioso) conforme roteamento estrategico.

---

## 2. PRE-VERIFICACAO OBRIGATORIA

Antes de iniciar qualquer analise estrategica, verificar:

```
[x] CASO.md existe e esta preenchido (dominio + modo + competencia)?
[x] Selo de Validacao Legal emitido (analisador-legislacao-vigente)?
[x] Competencia identificada (federal/estadual/municipal; adm/judicial)?
```

Se algum item estiver pendente: acionar a skill correspondente antes de prosseguir (PA-01).

---

## 3. PROTOCOLO JURISPRUDENCIAL (Protocolo 3) — MAPA DE TESES

Para cada tese juridica identificada no caso, classificar obrigatoriamente:

### 3.1 Classificacao de teses

| Nivel | Criterio | Tratamento |
|-------|----------|------------|
| **Vinculante** | Tema STF com repercussao geral julgado; Tema STJ com recurso repetitivo julgado; Sumula Vinculante STF; Sumula STJ/STF aplicavel | Citar com numero do Tema, dispositivo do acordao e resultado da modulacao (se houver). Aplicavel se fatos coincidirem. |
| **Em disputa** `[VERIFICAR]` | Tese em julgamento (pauta STF/STJ); divergencia entre camaras do CARF; multiplas Solucoes de Consulta contraditoria; tema pendente de pacificacao | Sinalizar `[VERIFICAR — tese em disputa]`. Apresentar os dois lados. Nao prometer resultado. |
| **Superada** | Tese expressamente abandonada por acordao posterior; Tema julgado contrariamente; Sumula cancelada | Indicar tese superada e qual decisao a substituiu. Nao usar para fundamentar estrategia. |

> **PA-04 — Alucinacao vedada:** se nao tiver certeza do numero do Tema, Sumula ou acordao, marcar como `[VERIFICAR — confirmar na fonte oficial]`. Nunca inventar referencia.

### 3.2 Modulacao de efeitos (PA-07)

Quando houver modulacao de efeitos em decisao vinculante, identificar:
- Quem pode aproveitar (contribuinte fez requerimento de habilitacao tempestivo?);
- A partir de quando os efeitos se aplicam;
- Se o caso concreto esta dentro do periodo coberto.

### 3.3 Formato do mapa de teses

```
MAPA DE TESES — [nome do caso]
Data-base: [DD/MM/AAAA]

Tese 1: [descricao]
  Classificacao: [Vinculante | Em disputa | Superada]
  Fundamento: [norma + acordao/tema/sumula ou VERIFICAR]
  Modulacao: [sim/nao — detalhe se sim]
  Aproveitamento no caso: [sim/possivel/nao/verificar]

Tese 2: [...]
```

---

## 4. MATRIZ DE RISCO

Avaliar o risco de cada tese/estrategia em tres niveis:

| Nivel | Criterio |
|-------|----------|
| **Provavel** (>60%) | Tese vinculante favoravel; jurisprudencia consolidada; fato gerador claro; sem modulacao adversa |
| **Possivel** (30-60%) | Tese em disputa; divergencia entre orgaos; jurisprudencia estadual vs federal conflitante |
| **Remoto** (<30%) | Tese superada; jurisprudencia consolidada contra; risco de multa qualificada (150%) se rejeitada |

Marcar cada estrategia recomendada com seu nivel de risco:

```
MATRIZ DE RISCO — [nome do caso]
Estrategia A: [descricao]
  Risco: [Provavel/Possivel/Remoto]
  Fundamento da classificacao: [...]
  Exposicao financeira estimada: [valor ou INFORMAR — estimativa, VERIFICAR]
  Mitigadores: [...]
```

> **PA-09** — qualquer valor monetario na matriz e estimativa marcada, sujeita a conferencia.

---

## 5. DECISAO ADMINISTRATIVA X JUDICIAL

Comparativo objetivo para orientar o operador:

### 5.1 Contencioso tributario — criterios de decisao

| Criterio | Via Administrativa | Via Judicial |
|----------|--------------------|--------------|
| Custo direto | Sem custas (gratuito) | Custas judiciais + honorarios |
| Prazo medio | 3-7 anos (CARF) | 5-15 anos (1a instancia a STJ/STF) |
| Suspensao do credito | Sim (durante impugnacao/recurso) | Sim (com deposito, seguro, ou liminar) |
| Penhora preventiva | Nao | Possivel (execucao fiscal em paralelo) |
| Precedentes vinculantes | Sumulas CARF (efeito interno); STF/STJ vinculam | STF/STJ vinculam diretamente |
| Cabimento CSRF | Exige paradigma de acordao de camara diferente | N/A |
| Vantagem especifica | Nao ha custas; suspensao automatica | Sumulas e temas vinculantes aplicaveis imediatamente; possivel liminar/tutela |

### 5.2 Regras de roteamento estrategico

- **Tese vinculante STF/STJ favoravel + habilitacao tempestiva:** judicial (mandado de seguranca preventivo ou acao anulatoria) pode ser mais rapido que aguardar CARF.
- **Tese em disputa no CARF:** administrativa primeiro — esgotar sem custo; preservar prazo judicial.
- **Execucao fiscal em curso:** embargos (30 dias + garantia) ou excecao de pre-executividade (PA-08) — nao confundir os dois instrumentos.
- **Prazo prescricional judicial:** 5 anos da constituicao definitiva (CTN art. 174) — monitorar.
- **Decadencia do credito tributario:** CTN art. 150 §4o (lancamento por homologacao) ou art. 173 (lancamento de oficio) — nunca confundir (PA-03).

> **PA-05** — nunca tratar a via administrativa e judicial como equivalentes ou intercambiaveis sem analise das especificidades de cada caso.
> **PA-08** — nunca confundir embargos a execucao fiscal (exige garantia) com excecao de pre-executividade (dispensa garantia, restrito a materias de ordem publica — Sumula 393 STJ).

---

## 6. ANTECIPACAO ADVERSARIAL

Para cada estrategia recomendada, construir a melhor tese do adversario (Fisco/parte contraria):

```
Melhor argumento adversarial:
  [construir o raciocinio mais forte que o Fisco ou parte contraria usaria]
Neutralizacao:
  [como o cliente/advogado rebate esse argumento]
Ponto fragil residual:
  [o que nao tem resposta definitiva — registrar honestamente]
```

Isso prepara o operador para questionamentos do julgador (filtro CARF/juiz cetico).

---

## 7. FORMATO DE ENTREGA

```
ESTRATEGIA DO CASO — [nome do cliente] — [DD/MM/AAAA]

1. MAPA DE TESES
   [...]

2. MATRIZ DE RISCO
   [...]

3. VIA RECOMENDADA
   Recomendacao: [administrativa | judicial | ambas em paralelo]
   Justificativa: [...]
   Riscos da recomendacao: [...]

4. ANTECIPACAO ADVERSARIAL
   [...]

5. PROXIMOS PASSOS
   a) [acao imediata — prazo urgente se houver]
   b) [segunda acao]
   c) [...]

RESSALVA: esta estrategia e uma analise preliminar baseada nas informacoes
fornecidas. Sujeita a revisao pelo advogado responsavel antes de qualquer
ato processual ou contratual. PA-22.
```

---

## 8. VEDACOES ESPECIFICAS

- **PA-01** — nenhuma estrategia sem Selo de Validacao Legal emitido.
- **PA-03** — nao cravar prazo decadencial/prescricional sem ressalva de interrupcoes.
- **PA-04** — zero alucinacao de precedente, sumula ou tema — marcar `[VERIFICAR]`.
- **PA-05** — nao confundir esfera administrativa e judicial.
- **PA-07** — nao omitir modulacao de efeitos em tese com modulacao.
- **PA-08** — nao confundir embargos a execucao x excecao de pre-executividade.
- **PA-09** — qualquer valor monetario e estimativa marcada.
- **PA-22** — toda saida e minuta; advogado responsavel valida antes de qualquer ato.

---

## 9. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — pre-requisito; Selo deve estar emitido.
- **Protocolo 3** (Jurisprudencial) — classificar cada tese: vinculante/em disputa/superada + modulacao.
- **Protocolo 4** (Competencia) — confirmar federativa e esfera processual.
- **Protocolo 5** (Calculo) — qualquer valor na matriz de risco e estimativa marcada.

---

## 10. INTEGRACAO

**Pre-requisito:** `CASO.md` + Selo de Validacao Legal.

**Chamada por:** `tributario-societario-master`, operador direto.

**Entrega para:** skills Tier 2-5 conforme roteamento + atualizacao do `CASO.md` com a estrategia escolhida.
