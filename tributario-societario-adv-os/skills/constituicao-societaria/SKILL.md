---
name: constituicao-societaria
description: >
  Minuta de contrato social (LTDA/SLU), estatuto social (S/A) e atos constitutivos. Inclui clausulas essenciais, advertencia sobre registro na Junta Comercial ou RCPJ. Aciona: abrir empresa, contrato social, constituir sociedade, estatuto, minuta de constituicao, ato constitutivo.
---

# CONSTITUICAO SOCIETARIA

> Skill **Tier 2 — Societario** — elabora minutas de atos constitutivos (contrato social para LTDA/SLU e estatuto social para S/A/SAS) e orienta o registro. Implementa PA-14, PA-15, PA-22. Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "abrir empresa", "contrato social", "constituir sociedade", "estatuto social", "minuta de constituicao", "ato constitutivo", "SLU", "minuta LTDA".

Entrega: minuta de contrato social (LTDA/SLU) ou estatuto social (S/A/SAS) + roteiro de registro.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`, `escolha-tipo-societario` (apos tipo definido), operador direto.
- **Entrega para:** `registro-empresarial` (arquivamento), `governanca-e-acordos` (acordo de socios), `planejamento-tributario` (Tier 4) para regime tributario,
  `suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).
- **Pre-requisito:** tipo societario ja definido (via `escolha-tipo-societario`) e `analisador-legislacao-vigente` confirmando norma vigente.

---

## 2. CLAUSULAS ESSENCIAIS — CONTRATO SOCIAL (LTDA/SLU)

Base: CC art. 997 (aplicavel a LTDA via CC 1.054).

### 2.1 Estrutura minima obrigatoria

```
1. Qualificacao das partes (socios/socio unico)
   - Nome completo, nacionalidade, estado civil, profissao, RG, CPF, endereco
   - Pessoa juridica: denominacao, CNPJ, sede, representante legal

2. Denominacao ou firma social e objeto social
   - Denominacao: pode incluir termo de fantasia + "Ltda." ou "Sociedade Limitada"
   - Firma: nome(s) do(s) socio(s) + ramo de atividade
   - Objeto social: descricao precisa (CNAE — verificar restricoes de atividade)

3. Sede e foro (municipio e estado)

4. Capital social
   - Valor total; divisao em quotas; valor por quota
   - Forma de integralizacao (dinheiro, bens, creditos — CC 1.055)
   - Prazo de integralizacao (se nao a vista)

5. Quota de cada socio e participacao percentual

6. Responsabilidade dos socios: limitada ao valor das quotas, ate a integralizacao total do capital

7. Administracao
   - Forma: administrador(es) socio(s) ou terceiro(s) nao socio(s) (CC 1.060)
   - Nome(s) do(s) administrador(es) designado(s)
   - Poderes e vedacoes (ex.: limite para contrair obrigacoes, endossar titulos)

8. Prazo de duracao (indeterminado ou determinado)

9. Data do exercicio social (geralmente 31/12 de cada ano)

10. Forma de distribuicao de lucros e de participacao em perdas
    - Regra: proporcional a quota; admite distribuicao desigual por contrato

11. Hipoteses de dissolucao parcial e total (CC 1.033-1.044)

12. Clausula de limitacao de responsabilidade (padrao para LTDA)

13. Foro competente para dirimir controversias

14. Data e assinaturas (socios + testemunhas) + reconhecimento de firmas ou assinatura digital ICP-Brasil
```

### 2.2 Clausulas facultativas recomendadas

- **Restricao de cessao de quotas:** condicionar a cessao a aprovacao dos demais socios (CC 1.057).
- **Direito de preferencia:** socios tem preferencia na aquisicao de quotas ofertadas por outro socio.
- **Exclusao de socio:** remissao ao CC 1.085 (socio que coloca em risco a continuidade da empresa, por deliberacao de maioria).
- **Quorum qualificado para deliberacoes relevantes:** mesmo apos Lei 14.451/2022, pode-se estabelecer quorum contratual superior ao legal minimo por clausula expressa (desde que inferior a unanimidade, salvo dispositivo expresso).
- **Nao-concorrencia dos socios:** definir prazo (razoavel, sugere-se ate 2 anos), territorio e atividades vedadas (PA-18).
- **Acordo de socios em separado:** remeter ao instrumento a ser averbado na Junta (art. 118 da Lei 6.404/76 por analogia + registro registral — CC 1.054 §2o nao regula averbacao de acordo de socios; aplicar o art. 118 LSA por analogia [VERIFICAR]).

---

## 3. CLAUSULAS ESSENCIAIS — ESTATUTO SOCIAL (S/A E SAS)

Base: Lei 6.404/76 (art. 5o para S/A; LC 182/2021 para SAS).

### 3.1 Clausulas obrigatorias (Lei 6.404/76, art. 5o)

```
1. Denominacao social (+ "S.A." ou "S/A" ou "Sociedade Anonima")
2. Sede (municipio) e foro
3. Objeto social (precisao do CNAE)
4. Duracao (indeterminada — regra; determinada — excecao)
5. Capital social, numero e valor nominal das acoes (ou sem valor nominal)
   - Classes: ordinarias (ON) e preferenciais (PN); vantagens das PN
   - Limite: acoes PN sem voto <= 50% do total emitido
6. Forma e prazo de integralizacao
7. Autorizacao ou nao para emissao de acoes acima do capital (capital autorizado)
8. Orgaos sociais:
   a) Assembleia Geral (AGO e AGE) — quoruns e competencias
   b) Conselho de Administracao (facultativo em S/A fechada; obrigatorio se capital autorizado)
   c) Diretoria — minimo 2 diretores; mandato; poderes; remuneracao
   d) Conselho Fiscal (facultativo em S/A fechada; funcionamento permanente ou nao)
9. Forma de convocacao das assembleias
10. Modo de liquidacao
11. Exercicio social
```

### 3.2 Especificidades da SAS (LC 182/2021)

- Denominacao: "Sociedade Anonima Simplificada" ou sigla "SAS".
- Dispensa publicacao em jornal oficial ou de grande circulacao para atos societarios.
- Assembleia geral pode ser substituida por decisao escrita assinada por todos os acionistas.
- Faturamento bruto anual: respeitar teto previsto na LC 182/2021 [VERIFICAR teto vigente].
- Pode ser unipessoal (1 acionista).

---

## 4. MODELO DE MINUTA — CONTRATO SOCIAL LTDA (ESQUEMA)

```markdown
CONTRATO SOCIAL DE [DENOMINACAO SOCIAL] LTDA.

[Socios], entre si, celebram o presente Contrato Social de constituicao de Sociedade Limitada,
regida pelo Codigo Civil (Lei 10.406/2002, arts. 1.052-1.087) e pelas seguintes clausulas:

CLAUSULA 1a — DENOMINACAO E SEDE
A sociedade girara sob a denominacao [DENOMINACAO SOCIAL] Ltda., com sede na Rua [...],
no Municipio de {{CIDADE}}, Estado de {{UF}}.

CLAUSULA 2a — OBJETO SOCIAL
[descricao da atividade — CNAE [VERIFICAR restricoes de licenca/registro]]

CLAUSULA 3a — CAPITAL SOCIAL
O capital social e de R$ [valor] ([extenso]), dividido em [n] quotas de R$ [valor unitario] cada,
totalmente subscritas e integralizadas neste ato em dinheiro, na seguinte proporcao:
  [Socio A]: [n] quotas — [%]
  [Socio B]: [n] quotas — [%]

CLAUSULA 4a — RESPONSABILIDADE
A responsabilidade de cada socio e restrita ao valor de suas quotas, respondendo todos
solidariamente pela integralizacao do capital social (CC art. 1.052).

CLAUSULA 5a — ADMINISTRACAO
A administracao sera exercida pelo socio [Nome], brasileiro, [estado civil], [profissao],
portador do RG [...] e CPF [...], residente em [...], que fica desde ja investido nos
poderes de administracao [...] [definir poderes e vedacoes].

CLAUSULA 6a — DELIBERACOES
As deliberacoes serao tomadas em reuniao de socios, observado o quorum previsto em lei.
[Clausulas de quorum qualificado contratual, se houver.]

CLAUSULA 7a — CESSAO DE QUOTAS
[Condicionar ou nao a aprovacao dos demais socios — CC 1.057.]

CLAUSULA 8a — EXERCICIO SOCIAL E LUCROS
O exercicio social encerra-se em 31 de dezembro de cada ano. Os lucros apurados serao
distribuidos em [periodicidade] [ou conforme deliberacao dos socios].

CLAUSULA 9a — DISSOLUCAO E LIQUIDACAO
A sociedade se dissolve nos casos previstos no CC art. 1.033, observadas as regras dos
arts. 1.102-1.112.

CLAUSULA 10a — FORO
Fica eleito o foro da Comarca de {{CIDADE}}/{{UF}} para dirimir qualquer controversia.

{{CIDADE}}, [data].

[Assinaturas dos socios e testemunhas]
```

> Esta e uma minuta-esquema. Adaptar ao caso concreto. Toda minuta e sujeita a revisao pelo advogado responsavel (PA-22).

---

## 5. ALERTAS PRE-REGISTRO

- Objeto social incompativel com CNAE exige pre-registro em orgao regulatorio (ex.: atividade financeira — BACEN; saude — ANVISA; advocacia — OAB) — verificar antes do arquivamento.
- Socio estrangeiro: exige CNPJ/CPF, representante legal com poderes no Brasil, autorizacao do BACEN para capital estrangeiro (BACEN-CBE) [VERIFICAR].
- Integralizacao em bens imoveis: exige descricao e avaliacao; transferencia registrada em cartorio de imoveis apos registro do contrato.
- Integralizacao em creditos: socios solidariamente responsaveis pela existencia e valor (CC 1.055, §2o).
- Capital social minimo: sem minimo legal geral para LTDA/SLU, mas algumas atividades reguladas exigem capital minimo (verificar).

---

## 6. VEDACOES ESPECIFICAS

- **PA-12** — nunca incluir EIRELI. SLU e a modalidade unipessoal vigente.
- **PA-14** — nao usar clausulas de estatuto de S/A em contrato social de LTDA (formatos distintos).
- **PA-15** — nunca omitir a obrigatoriedade de registro na Junta Comercial (LTDA/SLU/S/A/SAS) ou RCPJ (Sociedade Simples). Acionar `registro-empresarial` apos a minuta.
- **PA-22** — toda minuta e sujeita a revisao e assinatura pelo advogado responsavel.
- Nao afirmar que a constituicao confere beneficio fiscal especifico sem validar com `analisador-legislacao-vigente` e `planejamento-tributario`.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — confirmar arts. do CC/LSA/LC 182 vigentes na data da constituicao.
- **Protocolo 4** (Competencia) — LTDA/S/A/SAS: Junta Comercial. Sociedade Simples: RCPJ.

---

## 8. INTEGRACAO

**Chamada por:** `escolha-tipo-societario` (apos tipo definido), `triagem-empresarial` (modo consultivo-societario), operador direto.

**Entrega para:** `registro-empresarial` (arquivamento do ato constitutivo), `governanca-e-acordos` (acordo de socios, se houver), `planejamento-tributario` (Tier 4) para definir regime tributario pre-inicio de atividades,
`suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).

**Sem esta skill:** constituicao feita sem clausulas obrigatorias — risco de rejeicao na Junta/RCPJ e invalidade parcial do ato.
