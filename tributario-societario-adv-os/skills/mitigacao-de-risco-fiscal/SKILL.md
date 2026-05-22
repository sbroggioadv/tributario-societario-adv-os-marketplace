---
name: mitigacao-de-risco-fiscal
description: >
  Mitiga riscos de elisao abusiva, evasao fiscal e malha fina — fronteira licito/ilicito,
  proposito negocial, substancia economica, transparencia (CRS). Busca a saida tecnica
  viavel e defensavel. Nunca orienta evasao, simulacao ou ocultacao. Aciona: risco fiscal,
  malha fina, elisao, evasao, isso e legal, planejamento agressivo, estrutura suspeita,
  proposito negocial, substancia economica, blindagem fiscal.
---

# MITIGACAO DE RISCO FISCAL

> Skill **Tier 4 — Tributario Consultivo / Ambos** — identifica e mitiga riscos de elisao
> abusiva, evasao fiscal e malha fina. Trabalha a fronteira licito/ilicito por meio dos
> 5 pilares (proposito negocial, substancia economica, anterioridade, formalidade,
> transparencia). Sempre busca a saida tecnica viavel e defensavel.
> Implementa PA-16, PA-19, PA-21, PA-22 e o Protocolo 2. Mode: ambos.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "risco fiscal", "malha fina", "elisao", "evasao", "isso e legal",
"planejamento agressivo", "estrutura suspeita", "proposito negocial", "substancia economica",
"blindagem fiscal", "quero pagar menos imposto", "risco de autuacao", "CRS", "e-Financeira".

Entrega: classificacao da estrutura/operacao (elisao licita, elisao abusiva ou evasao),
os 5 pilares avaliados, diagnostico de risco e a saida tecnica viavel.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `estruturacao-holdings` (Tier 3), `planejamento-tributario` (Tier 4),
  `parecer-e-consulta-fiscal` (Tier 4), `recuperacao-de-creditos` (Tier 4).
- **Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio antes de qualquer
  entrega ao cliente que envolva risco fiscal).
- **Pre-requisito:** `analisador-legislacao-vigente` validar normas relevantes; Protocolo 1.

---

## 2. TABELA ELISAO x ELISAO ABUSIVA x EVASAO

| Modalidade | Definicao | Licitude | Consequencias |
|------------|-----------|----------|---------------|
| **Elisao fiscal licita** | Planejamento tributario anterior ao fato gerador, com substancia economica real, proposito negocial genuino, formalidade documental e transparencia. | Licita | Valida. Reconhecida pelo Fisco se bem estruturada. |
| **Elisao abusiva (planejamento agressivo)** | Operacao formalmente licita mas sem substancia economica real, sem proposito negocial independente do beneficio fiscal, ou realizada apos o fato gerador. CTN art. 116 §unico. | Zona cinza — alta probabilidade de requalificacao | Autuacao com 75% (multa de oficio padrao) ou 150% se a RFB caracterizar simulacao/fraude (CTN art. 44 §1). Desconsideracao da operacao pela RFB. |
| **Evasao fiscal** | Supressao ou reducao de tributo por acao dolosa: omissao de receita, notas fiscais frias, declaracoes falsas, subfaturamento, interposicao fraudulenta. Crimes da Lei 8.137/90. | Ilicita | Autuacao; multa qualificada (150%); representacao fiscal para fins penais (SV 24 — aguarda constituicao definitiva do credito); pena privativa de liberdade (2-5 anos + multa). |

> **PA-19** — este plugin NUNCA orienta evasao, simulacao, ocultacao de bens/titularidade
> ou estrutura sem substancia economica. A saida entregue SEMPRE sera a viavel e defensavel.
> **PA-21** — nunca afirmar que estrutura "blinda" contra Receita; nunca prometer resultado
> fiscal garantido.

---

## 3. OS 5 PILARES DA ELISAO LICITA

Para que um planejamento tributario seja defensavel como elisao licita, deve satisfazer
TODOS os 5 pilares:

### Pilar 1 — Proposito Negocial

A operacao deve ter razao de ser INDEPENDENTE do beneficio fiscal. A motivacao tributaria
pode ser um dos objetivos, mas nao pode ser o UNICO.

**Checklist:**
```
[ ] Ha justificativa de negocio documentada (ata, memorando, protocolo de reorganizacao)?
[ ] A operacao seria realizada mesmo sem o beneficio fiscal?
[ ] O beneficio fiscal e consequencia, nao causa principal?
[ ] A documentacao registra a motivacao de negocio?
```

**Risco:** operacao cujo unico proposito e reduzir tributo e requalificada como elisao
abusiva (art. 116 §unico CTN). Ex.: incorporacao realizada exclusivamente para usar
prejuizo fiscal da incorporada pela incorporadora — PA-17 veda + jurisprudencia CARF.

### Pilar 2 — Substancia Economica

Cada estrutura/entidade deve ter existencia economica real:
- Sede fisica funcional; gestao efetiva; estrutura operacional minima.
- Patrimonio proprio compativel com o objeto.
- Movimentacao financeira condizente com a atividade declarada.
- Estrutura nao pode ser "papel" criado exclusivamente para interposicao fiscal.

**Risco:** holding ou offshore sem substancia = desconsideracao (CC 50); requalificacao
como simulacao (CTN 149 VII); multa qualificada 150%.

### Pilar 3 — Anterioridade ao Fato Gerador

O planejamento deve ser estruturado ANTES do fato gerador tributario. Reorganizacao,
doacao, transferencia patrimonial ou mudanca de regime realizados APOS o fato gerador
(ou em reacao a autuacao) sao tratados como evasao/simulacao.

**Exemplo:** venda de imovel seguida de doacao da holding para o filho — se a doacao foi
feita apos a decisao de vender (visando ITCMD menor), a RFB pode requalificar. A doacao
anterior a decisao de venda e defensavel.

### Pilar 4 — Formalidade Documental

Toda operacao de planejamento deve estar documentada:
- Atos societarios registrados (ata de deliberacao, alteracao contratual, averbacao de acordo).
- Laudo de avaliacao quando ha transferencia de ativos.
- Contratos escritos para operacoes interpartes (emprestimos, royalties, prestacao de servicos).
- Preco de mercado em operacoes entre partes relacionadas (transfer pricing — OCDE/RFB).

**Risco:** falta de documentacao = impossibilidade de provar proposito negocial; operacao
informal pode ser desconsiderada.

### Pilar 5 — Transparencia (CRS / e-Financeira / SISCOSERV)

Em estruturas internacionais ou de alta renda:
- **CRS (Common Reporting Standard):** Brasil participa do intercambio automatico de
  informacoes financeiras (IN RFB 1.571/2015 e atualizacoes). Contas no exterior sao
  reportadas automaticamente para a RFB.
- **e-Financeira:** operacoes financeiras acima de determinados limites sao informadas pelas
  instituicoes financeiras diretamente a RFB.
- **CBE/SISBACEN:** capitais brasileiros no exterior devem ser declarados ao BACEN (CBE anual
  + trimestral acima de limites — [VERIFICAR limites vigentes]).
- **SISCOSERV:** servicos internacionais (suspenso — [VERIFICAR se foi reativado]).

> Nenhuma estrutura "esconde" bens da Receita Federal em ambiente de CRS. A pretensao de
> opacidade e, por si so, um sinal de alerta de evasao.

---

## 4. DIAGNOSTICO DE RISCO — CHECKLIST

```
DIAGNOSTICO DE RISCO FISCAL — [operacao/estrutura]
Data-base: [DD/MM/AAAA]

PILAR 1 — Proposito negocial
  Justificativa documentada: [sim/nao/parcial]
  Beneficio fiscal e o unico objetivo: [sim/nao]
  Risco: [Baixo/Medio/Alto]

PILAR 2 — Substancia economica
  Sede/estrutura fisica: [sim/nao/parcial]
  Patrimonio proprio: [sim/nao]
  Operacao real: [sim/nao]
  Risco: [Baixo/Medio/Alto]

PILAR 3 — Anterioridade
  Operacao anterior ao fato gerador: [sim/nao]
  Cronograma documentado: [sim/nao]
  Risco: [Baixo/Medio/Alto]

PILAR 4 — Formalidade
  Atos societarios registrados: [sim/nao/pendente]
  Contratos escritos: [sim/nao]
  Laudos quando necessarios: [sim/nao]
  Risco: [Baixo/Medio/Alto]

PILAR 5 — Transparencia
  Declaracoes ao BACEN/RFB: [em dia/pendente]
  Exposicao ao CRS: [sim/nao]
  e-Financeira: [monitorado/nao aplicavel]
  Risco: [Baixo/Medio/Alto]

CLASSIFICACAO FINAL: [Elisao licita | Elisao abusiva | Evasao | Zona cinza]
RISCO GERAL: [Baixo/Medio/Alto/Critico]
SAIDA TECNICA RECOMENDADA: [...]
```

---

## 5. MALHA FINA — SINAIS DE ALERTA

Situacoes que aumentam o risco de malha fina ou autuacao:
- Distribuicao de dividendos acima da capacidade de lucro apurado.
- Despesas incompativeis com o porte da empresa (dedutibilidade questionavel).
- Pro-labore muito abaixo do mercado (possivel requalificacao como dividendo disfarcado).
- Operacoes interpartes sem contrato ou sem preco de mercado.
- Offshore ou conta no exterior nao declarada ao BACEN/RFB.
- Mudanca de regime tributario ou reorganizacao societaria sem documentacao de proposito negocial.
- Tese tributaria agressiva sem consulta fiscal ou parecer formal.

---

## 6. VEDACOES ESPECIFICAS

- **PA-16** — nunca estruturar agio artificial, incorporacao sem proposito negocial,
  ou operacao cuja unica funcao e gerar beneficio fiscal.
- **PA-19** — nunca sugerir ocultacao de bens, interposicao de pessoa sem substancia,
  ou estrutura projetada para confundir o Fisco.
- **PA-21** — nunca afirmar que holding/offshore/trust blinda contra Receita ou herdeiro
  necessario; nunca prometer resultado fiscal garantido.
- **PA-22** — toda analise e minuta sujeita a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — validar CTN 116 §unico, CC 50, Lei 8.137/90 e
  normas de transparencia (IN RFB vigente sobre CRS/e-Financeira).
- **Protocolo 2 — Mitigacao de Risco Fiscal** — este e o protocolo central desta skill:
  elisao x elisao abusiva x evasao; 5 pilares; malha fina/CRS; saida viavel e defensavel.
- **Protocolo 4** (Competencia) — identificar qual esfera tem competencia sobre o risco
  (federal/estadual/municipal; adm/judicial).

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`estruturacao-holdings` (Tier 3), `planejamento-tributario` (Tier 4),
`parecer-e-consulta-fiscal` (Tier 4), `recuperacao-de-creditos` (Tier 4).

**Entrega para:** `suprema-corte-empresarial` (R1-R4 obrigatorio antes de qualquer
entrega que envolva risco fiscal).

**Sem esta skill:** cliente operando em zona cinza sem diagnostico formal de risco;
estrutura de planejamento tributario montada sem checklist dos 5 pilares — vulneravel
a autuacao com multa qualificada (150%) e representacao para fins penais.
