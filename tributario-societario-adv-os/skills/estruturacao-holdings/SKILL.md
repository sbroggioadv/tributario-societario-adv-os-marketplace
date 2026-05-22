---
name: estruturacao-holdings
description: >
  Estrutura holdings pura vs mista, arranjos de 1, 2 e 3 celulas (escalonamento em camadas),
  com exigencia de substancia economica real em cada celula. Nunca sugere camada vazia nem
  estrutura sem proposito negocial. Nunca afirma que holding blinda ativos contra Receita,
  credores ou herdeiro necessario. Aciona: holding, holding patrimonial, holding de participacoes,
  estruturar holding, 3 celulas, holding pura, holding mista.
---

# ESTRUTURACAO DE HOLDINGS

> Skill **Tier 3 — Estruturacao Patrimonial** — orienta a arquitetura de holdings (pura vs
> mista, arranjos de 1/2/3 celulas) com foco em substancia economica, proposito negocial e
> limites juridicos. Implementa PA-16, PA-19, PA-21, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "holding", "holding patrimonial", "holding de participacoes", "estruturar holding",
"3 celulas", "holding pura", "holding mista", "holding familiar patrimonial", "blindagem
patrimonial" (termo incorreto — ver secao 4.4).

Entrega: mapa do arranjo recomendado + exigencias de substancia economica + alertas de risco
(desconsideracao, fraude a credores) + fluxo de implementacao.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `planejamento-sucessorio-patrimonial` (Tier 3), `reorganizacao-societaria` (Tier 2).
- **Entrega para:** `planejamento-sucessorio-patrimonial` (se contexto sucessorio),
  `offshore-e-trust` (se holding com camada internacional), `planejamento-tributario` (Tier 4),
  `mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).
- **Pre-requisito:** `analisador-legislacao-vigente` validar CC 1.052-1.087 e LSA 6.404/76
  vigentes; Protocolo 1 emitir Selo.

---

## 2. HOLDING PURA VS MISTA

### 2.1 Holding pura

Objeto social: exclusivamente participar do capital de outras sociedades (como socia ou
acionista). Nao exerce atividade operacional propria. Receita = dividendos, JCP, ganhos de
capital nas participacoes.

**Uso tipico:** centralizacao de controle; governanca do grupo; protecao dos ativos operacionais
do risco do negocio (o risco fica na subsidiaria operacional, nao na holding).

**Tributacao da holding pura (Lucro Real ou Presumido):**
- Dividendos recebidos de PJ brasileira: isentos (RIR — verificar vigencia com Lei 15.270/2025
  e regras de transparencia [VERIFICAR]).
- Ganho de capital na alienacao de participacoes: IRPJ + CSLL sobre o ganho.
- Regime recomendado: Lucro Real quando ha alienacoes frequentes; Lucro Presumido se receita
  e previsivel e de baixo valor. [VERIFICAR impacto da Lei 15.270/2025 na equacao Presumido vs Real]

### 2.2 Holding mista

Objeto social: participacoes + atividade propria (imobiliaria, administracao de bens, servicos).
Recebe dividendos das subsidiarias E tem receita operacional propria.

**Uso tipico:** quando a holding tambem e proprietaria de imoveis (aluguel), marcas (royalties)
ou presta servicos de gestao ao grupo.

**Atencao:** receita operacional propria da holding mista e tributada normalmente (PIS/COFINS,
IRPJ, CSLL). Misturar renda de participacoes com renda operacional exige segregacao contabil
clara para evitar contingencias.

---

## 3. ARRANJOS DE CELULAS: 1, 2 E 3

### 3.1 Arranjo de 1 celula

```
Socios/PF
   |
Holding (pura ou mista)
   |          |          |
Op-A       Op-B       Ativo X
```

**Uma unica holding** concentra participacoes nas operacionais e os ativos patrimoniais.

**Quando usar:** grupo pequeno, ativos homogeneos, ausencia de risco cruzado relevante entre
as operacoes.

**Risco:** ativos patrimoniais e participacoes ficam na mesma PJ que pode ser atingida por
contingencias das operacionais se mal estruturada.

### 3.2 Arranjo de 2 celulas

```
Socios/PF
   |
Holding Controladora (pura)
   |                    |
Holding Patrimonial   Operacional
(imoveis, marcas)     (negocio principal)
```

**Controladora pura** controla as demais. Abaixo: holding patrimonial ("cofre" de ativos
imobiliarios e/ou marcas) separada da operacional (onde vive o risco do negocio).

**Quando usar:** separar ativos patrimoniais do risco operacional; planejamento sucessorio
sobre imoveis sem contaminar a operacao.

### 3.3 Arranjo de 3 celulas

```
Socios/PF
   |
Holding Controladora (pura)
   |              |              |
Holding        Holding         Operacional
Patrimonial    de Marcas/IP    (risco do negocio)
("cofre")      (royalties)
```

Maxima segregacao de risco. Cada celula tem objeto, tributacao e exposicao diferente.

**Quando usar:** grupo com ativos heterogeneos (imoveis + propriedade intelectual + operacao
de alto risco); sucessao multigeracional complexa; entrada de capital ou M&A futuro.

**Custo:** maior custo de manutencao contabil, fiscal e societaria. Cada CNPJ tem obrigacoes
acessorias proprias (ECF, EFD, SPED).

---

## 4. SUBSTANCIA ECONOMICA — EXIGENCIA ABSOLUTA

### 4.1 O que e substancia economica

Cada celula da estrutura deve ter existencia real e demonstravel: (a) objeto social compativel
com a atividade desenvolvida; (b) patrimonio proprio; (c) estrutura operacional minima (sede,
gestao, registros contabeis); (d) movimentacao financeira condizente com o objeto.

### 4.2 Consequencias da camada vazia

Holding criada apenas no papel — sem atividade, sem patrimonio proprio, sem gestao —
e desconsiderada pela RFB e pelo Judiciario:

- **Desconsideracao da personalidade juridica (CC 50):** quando ha abuso de forma societaria
  ou confusao patrimonial, o Judiciario pode atingir o patrimonio pessoal dos socios ou
  das demais PJs do grupo.
- **Requalificacao pela RFB:** estrutura sem substancia e tratada como simulacao (CTN 149 VII).
  Autuacao com multa qualificada (150%) e risco penal apos SV 24 STF.
- **PA-16:** este plugin nunca orienta criacao de camada societaria cujo unico proposito seja
  reduzir tributo sem substancia economica.

### 4.3 Proposito negocial obrigatorio

Cada celula deve ter razao de ser independente do beneficio fiscal:
- Holding patrimonial: centralizar imoveis para gestao e sucessao;
- Holding de marcas: licenciar uso a operacionais com precificacao de mercado;
- Operacional: executar a atividade-fim com limitacao de responsabilidade.

A justificativa deve constar de ata/reuniao de constituicao e, se houver reorganizacao,
do Protocolo e Justificacao (LSA 224, aplicavel analogicamente).

### 4.4 O mito da "blindagem patrimonial" — PA-19, PA-21

> **ALERTA — PA-19 e PA-21:** o termo "blindagem" e tecnicamente impreciso e comercialmente
> perigoso. Nenhuma estrutura "blinda" ativos contra:
> - **Receita Federal:** estruturas sem substancia sao desconsideradas; CRS e e-Financeira
>   automaticamente reportam contas e investimentos; SISCOSERV e SISBACEN monitoram remessas.
> - **Herdeiros necessarios:** a legitima (CC 1.845-1.846) e indisponivel. Doacao ou
>   transferencia de bens a holding nao elimina a legitima dos filhos e conjuge.
> - **Credores pre-existentes:** transferencia de bens para holding apos divida constituida
>   pode ser anulada como fraude contra credores (CC 158-165) ou fraude a execucao (CPC 792).

**Este plugin nunca usa o termo "blindagem" como promessa. Usa: "segregacao de risco" e
"planejamento estruturado transparente".**

---

## 5. FLUXO DE IMPLEMENTACAO

1. **Diagnostico:** mapear ativos, passivos, operacoes, socios, credores e herdeiros.
2. **Definir arranjo:** 1, 2 ou 3 celulas conforme complexidade e objetivos.
3. **Protocolo 1 (Validacao Legal):** confirmar vigencia de CC, LSA, IN RFB relevante.
4. **Protocolo 2 — Mitigacao de Risco Fiscal:** checklist proposito negocial + substancia + anterioridade.
5. **Constituicao das celulas:** contrato social ou estatuto por celula; registrar na Junta.
6. **Integralizacao e transferencia:** conferencia de bens com laudo de avaliacao (se S/A) ou
   deliberacao fundamentada (se LTDA); ITBI (imoveis) ou ITCMD (doacao de quotas) podem incidir
   — verificar regime do Estado [VERIFICAR beneficio de nao-incidencia vigente].
7. **Acordo de socios:** governanca do grupo; tag/drag; regras de saida.
8. **Compliance corrente:** ECF, EFD, SPED, CBE (se offshore), CRS por cada celula.

---

## 6. VEDACOES ESPECIFICAS

- **PA-16** — nunca estruturar camada sem proposito negocial ou para gerar agio artificial.
- **PA-19** — nunca sugerir ocultacao de bens ou holding sem substancia economica.
- **PA-21** — nunca afirmar que holding "blinda" contra Receita, credores ou herdeiros
  necessarios. Nunca prometer resultado fiscal garantido.
- **PA-22** — toda estrutura e minuta sujeita a revisao pelo advogado responsavel.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal) — CC 1.052-1.087, LSA 6.404/76, IN RFB vigente.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — proposito negocial, substancia, anterioridade,
  transparencia (CRS, e-Financeira, SISBACEN).
- **Protocolo 4** (Competencia) — Junta Comercial (constituicao); RFB (IRPJ/CSLL/ITBI);
  SEFAZ (ITCMD/ITBI estadual); municipio (ITBI municipal).

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`planejamento-sucessorio-patrimonial`, `reorganizacao-societaria`.

**Entrega para:** `planejamento-sucessorio-patrimonial` (se holding familiar),
`offshore-e-trust` (se camada internacional), `planejamento-tributario` (Tier 4),
`mitigacao-de-risco-fiscal` (Tier 4), `suprema-corte-empresarial` (R1-R4 obrigatorio).

**Sem esta skill:** grupo estruturado sem segregacao de risco, sem substancia economica
documentada e vulneravel a desconsideracao da personalidade juridica e autuacao por simulacao.
