---
name: dissolucao-e-saida-de-socio
description: >
  Distrato, dissolucao (consensual, judicial, de pleno direito) e liquidacao; exclusao de
  socio (CC 1.085 — quorum: maioria dos demais socios por cabeca, nao do capital); apuracao
  de haveres (CPC 606, balanco de determinacao, sem lucros futuros — STJ). Aciona: fechar
  empresa, distrato, sair da sociedade, excluir socio, apuracao de haveres, dissolucao.
---

# DISSOLUCAO E SAIDA DE SOCIO

> Skill **Tier 2 — Societario** — distrato, dissolucao (consensual/judicial/pleno direito),
> liquidacao, saida voluntaria e exclusao de socio (CC 1.085), com foco na apuracao de
> haveres (CPC 606, balanco de determinacao, sem lucros futuros). Implementa PA-13, PA-22.
> Mode: ambos (consultivo na prevencao; contencioso na dissolucao judicial e exclusao litigiosa).

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "fechar empresa", "distrato", "encerrar sociedade", "dissolucao", "sair da
sociedade", "retirada de socio", "exclusao de socio", "apuracao de haveres", "recesso",
"balanco de determinacao", "liquidacao".

Entrega: mapa das hipoteses + esquema de documentos + roteiro de apuracao de haveres.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
  `alteracoes-e-atos-societarios` (saida via alteracao contratual), operador direto.
- **Entrega para:** `registro-empresarial` (baixa Junta/RFB), `calculo-e-prazos-tributarios` (Tier 1)
  para estimativa de haveres, `estrategia-de-caso-empresarial` (Tier 1) se contencioso,
  `suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar CC 1.028-1.044 e CPC 606.

---

## 2. CAUSAS DE DISSOLUCAO

### 2.1 LTDA / Sociedade Simples (CC 1.033-1.034)

| Causa | Modalidade |
|-------|-----------|
| Prazo determinado vencido | Pleno direito |
| Consenso de todos os socios | Consensual |
| Deliberacao por maioria do capital (CC 1.076) | Deliberativa |
| Falta de pluralidade de socios por mais de 180 dias | Pleno direito |
| Extincao da autorizacao para funcionar | Pleno direito |
| Sentenca judicial (CC 1.034) | Judicial |

### 2.2 S/A — causas adicionais (LSA 206)

Deliberacao de AGE (maioria absoluta do capital votante — LSA 136 VIII); falencia;
liquidacao judicial; cassacao de autorizacao; numero de acionistas abaixo do minimo legal.

### 2.3 Distrato social (dissolucao consensual LTDA)

Instrumento de dissolucao consensual (unanimidade). Conteudo minimo: identificacao da
sociedade e socios; declaracao de dissolucao; nomeacao de liquidante; inventario inicial
de ativo e passivo; autorizacao ao liquidante; data e assinaturas.
Apos distrato: arquivar na Junta → liquidante realiza ativo e paga passivo → balancete de
encerramento → partilha → baixa no CNPJ (RFB) → certidao de baixa na Junta.

### 2.4 Dissolucao judicial (CC 1.034; LSA 206 II)

Hipoteses: exaurimento do objeto; impossibilidade de preenchimento; grave violacao contratual
ou legal; insolvencia nao decretada como falencia.
Procedimento: acao de dissolucao (CPC 599-609) → sentenca → liquidante judicial → liquidacao.

---

## 3. SAIDA VOLUNTARIA DE SOCIO

**Retirada imotivada (LTDA — prazo indeterminado):** a qualquer tempo, com 60 dias de
antecedencia (CC 1.029). Direito irrenunciavel.

**Recesso (dissidencia):** incorporacao, fusao, cisao, transformacao (CC 1.077; LSA 137).
Prazo: 30 dias a contar da publicacao da deliberacao.

**Saida por cessao de quotas:** ver `alteracoes-e-atos-societarios`. Responsabilidade solidaria
do cedente por 2 anos pelas obrigacoes anteriores (CC 1.003).

---

## 4. EXCLUSAO DE SOCIO (CC 1.085)

### 4.1 Requisitos materiais

Socio que coloca em risco a continuidade da empresa por atos de inegavel gravidade:
desvio de recursos, concorrencia desleal, inadimplemento de aporte, violacao grave de deveres.

### 4.2 Quorum — REGRA CRITICA (PA-13)

> **Erro frequente:** o quorum de exclusao NAO e maioria do capital social.
> **E: maioria dos DEMAIS socios — por CABECA (nao pelo capital).**
> Base: CC 1.085 — "maioria dos demais socios".
> O socio a ser excluido nao vota; quorum conta entre os demais socios.

Exemplo: 3 socios (A — 50%, B — 30%, C — 20%). Para excluir C: precisam A e B (ambos),
pois o quorum e por cabeca entre os 2 demais, nao por participacao.

### 4.3 Requisito formal

**O contrato social DEVE prever expressamente a possibilidade de exclusao** para via
extrajudicial (CC 1.085). Sem clausula: unico caminho e acao de dissolucao parcial judicial.

### 4.4 Procedimento extrajudicial

1. Deliberacao dos socios remanescentes (maioria por cabeca dos demais).
2. Ata de reuniao de socios.
3. Notificacao do socio excluido (contraditorio minimo recomendado pela doutrina e STJ).
4. Alteracao do contrato social refletindo a exclusao.
5. Arquivamento na Junta Comercial.
6. Apuracao de haveres (ver secao 5).

### 4.5 Exclusao judicial

Quando nao houver clausula contratual ou quando a exclusao for contestada: acao de
dissolucao parcial (CPC 599-609). Juiz pode determinar a exclusao e nomear perito.

---

## 5. APURACAO DE HAVERES (CPC 606)

### 5.1 Balanco de determinacao — regra geral

Quando o contrato for **omisso** quanto ao criterio, aplica-se o **balanco de determinacao**
(CPC art. 606): balancete levantado especificamente para a apuracao, com o ativo avaliado
a **valor de mercado** (nao custo historico). Inclui imoveis, estoques, contas a receber e
intangiveis mensuravelmente verificaveis. Data-base: data do evento.

### 5.2 Lucros futuros — vedacao STJ

> **Regra absoluta:** lucros futuros, goodwill projetado e rentabilidade esperada
> NAO INTEGRAM os haveres do socio retirante ou excluido.
> Posicao consolidada do STJ — varios acordaos alinhados [VERIFICAR precedentes atuais].
> O que entra e o patrimonio atual a valor de mercado, nao projecao.

### 5.3 Criterio convencional

O contrato pode prever criterio diferente (valor patrimonial contabil, multiplo de
faturamento). Se claramente desproporcional, pode ser questionado judicialmente.

### 5.4 Pagamento

- Regra geral (CC 1.031): dinheiro; prazo de 90 dias a contar da liquidacao das quotas.
- Dissolucao parcial judicial: juiz fixa prazo e forma (CPC 606, §4o).
- Se haveres superarem o lucro acumulado: reducao de capital com publicacao e prazo de
  oposicao de credores (CC 1.082).

---

## 6. LIQUIDACAO — ROTEIRO RESUMIDO

Nomeacao do liquidante → inventario e balanco de abertura → realizacao do ativo (cobrancas,
vendas) → pagamento do passivo (preferencialmente trabalhistas e fiscais) → balancete final
→ partilha do saldo → baixa na RFB (CNPJ), Junta Comercial, INSS, prefeitura (ISS),
Estado (ICMS se aplicavel).

---

## 7. VEDACOES ESPECIFICAS

- **PA-13** — quorum de exclusao (CC 1.085): maioria dos demais socios por cabeca, nao por
  capital. Nunca inverter.
- **PA-22** — minuta de distrato, ata de exclusao e acordo de haveres sujeitos a revisao
  pelo advogado responsavel.
- Nunca afirmar que lucros futuros integram os haveres.
- Nunca orientar exclusao extrajudicial sem clausula expressa no contrato social.

---

## 8. PROTOCOLOS ACIONADOS

- **Protocolo 1** — confirmar CC 1.028-1.044, 1.085, 1.031 e CPC 599-609 vigentes.
- **Protocolo 4** — Junta Comercial para baixa; RFB para baixa do CNPJ; Vara Empresarial
  para dissolucao judicial.
- **Protocolo 5** — haveres sao estimativa sujeita a peritos; nunca apresentar como definitivo.

---

## 9. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`,
`alteracoes-e-atos-societarios`.

**Entrega para:** `registro-empresarial` (baixa), `calculo-e-prazos-tributarios` (Tier 1),
`estrategia-de-caso-empresarial` (Tier 1) se litigio,
`suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).

**Sem esta skill:** dissolucao ou exclusao sem fundamento legal — risco de invalidade e
de condenacao a pagar haveres majorados com lucros futuros.
