---
name: escolha-tipo-societario
description: >
  Recomenda o tipo societario — LTDA, SLU, S/A aberta/fechada, SAS, sociedade simples, SCP — conforme objetivo, faturamento, governanca e numero de socios. Nunca sugere EIRELI (extinta — usar SLU). Aciona: qual tipo de empresa abrir, LTDA ou SA, melhor sociedade, SLU, constituir empresa.
---

# ESCOLHA DO TIPO SOCIETARIO

> Skill **Tier 2 — Societario** — recomenda o tipo societario adequado ao objetivo, faturamento, estrutura de governanca e numero de socios. Implementa PA-12 (EIRELI extinta) e PA-14 (nao confundir tipos). Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "qual tipo de empresa abrir", "LTDA ou SA", "melhor sociedade", "SLU", "constituir empresa", "que tipo de pessoa juridica", "holding qual tipo", "empresa individual".

Entrega: recomendacao fundamentada do tipo societario com arvore de decisao, tabela comparativa e alertas de PA.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial` (modo consultivo-societario), operador direto.
- **Entrega para:** `constituicao-societaria` (com o tipo definido), `registro-empresarial`, `estruturacao-holdings` (Tier 3).
- **Pre-requisito recomendado:** `analisador-legislacao-vigente` validar as normas do tipo escolhido antes de prosseguir.

---

## 2. TIPOS SOCIETARIOS — PANORAMA LEGAL

### 2.1 Tabela comparativa

| Tipo | Base legal | Socios | Responsabilidade | Registro |
|------|-----------|--------|-----------------|----------|
| LTDA | CC art. 1.052-1.087 | 2+ (ou 1 como SLU) | Limitada ao capital | Junta Comercial |
| SLU | CC art. 1.052 §§1-2 (Lei 13.874/2019) | 1 socio (PF ou PJ) | Limitada ao capital | Junta Comercial |
| S/A fechada | Lei 6.404/76 | 1+ (Lei 13.874) | Limitada ao valor das acoes | Junta Comercial |
| S/A aberta | Lei 6.404/76 + CVM | 1+ | Limitada ao valor das acoes | Junta Comercial + CVM |
| SAS | LC 182/2021 | 1+ (S/A fechada simplificada) | Limitada ao valor das acoes | Junta Comercial |
| Sociedade Simples | CC art. 997-1.038 | 2+ | Solidaria (regra geral) | RCPJ |
| SCP | CC art. 991-996 | 2+ (ostensivo + participantes) | Ostensivo responde ilimitado | RCPJ (CNPJ) |

> **PA-12 — EIRELI EXTINTA:** a EIRELI foi extinta pela Lei 14.195/2021. Nunca propor. Empresas individuais de responsabilidade limitada: usar **SLU** (CC art. 1.052 §§1-2).
> **PA-14:** nao confundir LTDA (contrato social) com S/A (estatuto). Nao confundir SAS (S/A simplificada, LC 182) com sociedade simples.

### 2.2 Caracteristicas-chave por tipo

**LTDA (CC 1.052-1.087):**
- 2 ou mais socios (ou 1 como SLU).
- Capital dividido em quotas; contrato social registrado na Junta.
- Administracao: socio ou terceiro nao socio (CC 1.060).
- Lucros e distribuicao: livres, vedado capital nao integralizado.
- Porte: qualquer faturamento; compativel com Simples, Presumido, Real.
- Reuniao de socios: CC 1.072; alteracao contratual: maioria (mais da metade do capital social — CC 1.076).

**SLU (CC 1.052 §§1-2):** 1 socio (PF ou PJ); regras LTDA aplicam-se no que couber; para admitir outro socio, basta alterar para a modalidade pluripessoal (LTDA com 2+ socios, CC 1.052 caput) — nao e transformacao de tipo; substitui a EIRELI extinta (Lei 14.195/2021).

**S/A fechada (Lei 6.404/76):** 1 ou mais acionistas (Lei 13.874); capital em acoes; orgaos: assembleia geral, diretoria (conselho facultativo); acoes ordinarias e preferenciais (limite 50% votante); livros sociais obrigatorios; qualquer faturamento.

**S/A aberta (Lei 6.404/76 + CVM):** valores mobiliarios negociados em bolsa/balcao; registro CVM obrigatorio; disclosure periodico; custo regulatorio alto — indicada para captacao publica ou pre-IPO.

**SAS — Sociedade Anonima Simplificada (LC 182/2021):** S/A fechada simplificada para faturamento ate R$ 78 mi/ano [VERIFICAR teto vigente]; dispensa publicacao em jornal; pode ser unipessoal; assembleia pode ser substituida por decisao escrita; ideal para startups.

**Sociedade Simples (CC 997-1.038):** atividade intelectual/liberal/artistica; registro RCPJ; responsabilidade solidaria como regra (CC 1.023) — pode ser limitada por clausula contratual; nao registra na Junta Comercial.

**SCP (CC 991-996):** sem personalidade juridica propria; socio ostensivo responde ilimitado perante terceiros; socios participantes: responsabilidade interna; CNPJ obrigatorio (IN RFB [VERIFICAR]); contrato apenas interno; uso tipico: joint ventures e empreendimentos imobiliarios.

---

## 3. ARVORE DE DECISAO

### Passo 1 — Quantos socios?

```
1 socio (PF ou PJ)?
  → Atividade intelectual/liberal (sem natureza empresarial)?
      Sim → exercicio individual da profissao (sem constituir pessoa juridica) ou, havendo 2+ profissionais, Sociedade Simples (CC 997 exige no minimo 2 pessoas) [VERIFICAR atividade]
      Nao → SLU (CC 1.052 §§1-2)  ← NUNCA EIRELI (extinta — PA-12)

2+ socios?
  → Ir para Passo 2
```

### Passo 2 — Natureza da atividade

```
Atividade intelectual/liberal/artistica (sem fins predominantemente empresariais)?
  → Sociedade Simples (CC 997) — registro RCPJ
  Obs.: verificar se socio nao e empresario; contrato pode limitar responsabilidade.

Atividade empresarial (industria, comercio, prestacao de servico sem carater intelectual exclusivo)?
  → Ir para Passo 3
```

### Passo 3 — Faturamento e porte

```
Faturamento bruto esperado <= R$ 4,8 mi/ano?
  → Simples Nacional elegivel: LTDA e SLU sao as mais comuns
  → SAS tambem elegivel se estrutura acionaria for necessaria

Faturamento bruto >= R$ 78 mi/ano?
  → Lucro Real obrigatorio: LTDA, S/A ou SAS
  → SAS nao disponivel acima do teto (confirmar LC 182/2021)

Entre R$ 4,8 mi e R$ 78 mi?
  → Lucro Presumido ou Real: LTDA, SLU, SAS ou S/A fechada
```

### Passo 4 — Governanca e investidores

```
Precisa de estrutura acionaria (entrada/saida facil de investidores, opcoes/vesting, acoes preferenciais)?
  → S/A fechada (Lei 6.404/76) ou SAS (LC 182/2021)
  Obs.: SAS e mais simples (dispensa publicacoes); S/A tradicional e mais robusta.

Acesso a mercado de capitais (IPO ou emissao publica)?
  → S/A aberta (registro CVM)

Controle familiar simples ou parceria de 2-4 socios?
  → LTDA (contrato social e mais flexivel e barato)
  → SLU se for 1 socio

Joint venture temporaria ou empreendimento especifico?
  → SCP (CC 991-996) — nao tem personalidade juridica propria
```

### Passo 5 — Holding

```
Estrutura holding pura (so participacoes) ou mista?
  → LTDA (holding familiar simples, menores custos) ou S/A fechada (+ socios/investidores)
  → SAS: opcao intermediaria para holding de startup
  → Verificar: estruturacao-holdings (Tier 3) para arranjos multi-celula e aspectos fiscais
```

---

## 4. QUADRO-RESUMO DE RECOMENDACAO

| Perfil | Tipo recomendado | Observacao |
|--------|-----------------|------------|
| 1 socio, atividade empresarial | SLU | Nunca EIRELI (PA-12) |
| 2+ socios, controle simples, faturamento < R$ 78mi | LTDA | Mais usada no Brasil; flexivel e barata |
| Startup com socios e plano de captacao < R$ 78mi | SAS (LC 182/2021) | Dispensa publicacoes; estrutura acionaria acessivel |
| Empresa de maior porte ou com 5+ investidores | S/A fechada | Orgaos formais; acoes ordinarias e preferenciais |
| Captacao publica / pre-IPO | S/A aberta | Registro CVM obrigatorio |
| Profissional liberal (medico, advogado, engenheiro) | Sociedade Simples | Registro RCPJ; responsabilidade pode ser limitada por clausula |
| Joint venture temporaria / imobiliario | SCP | Socio ostensivo responde ilimitado; sem personalidade juridica |

---

## 5. ASPECTOS TRIBUTARIOS RELEVANTES (resumo — ver Tier 4 para aprofundamento)

| Aspecto | Impacto por tipo |
|---------|-----------------|
| Simples Nacional (LC 123/2006) | Elegivel: LTDA, SLU, SAS (verificar restricoes de atividade e porte). S/A geralmente incompativel. |
| Lucro Presumido (teto R$ 78mi) | Elegivel: LTDA, SLU, S/A fechada, SAS. |
| Lucro Real | Obrigatorio acima de R$ 78mi; obrigatorio para S/A aberta; opcional abaixo do teto. |
| Distribuicao de dividendos | Isenta de IR (ate 2025 — verificar Lei 15.270/2025 para impacto em 2026+). |
| Deducao de pro-labore | Reduce base do IRPJ/CSLL no Lucro Real; nao reduz no Presumido. |

> **PA-06:** todo raciocinio tributario e datado pelo ano do fato gerador. Confirmar regime aplicavel com `planejamento-tributario` (Tier 4).

---

## 6. VEDACOES ESPECIFICAS

- **PA-12** — nunca sugerir EIRELI (extinta pela Lei 14.195/2021). Alternativa: SLU.
- **PA-14** — nao confundir tipos societarios. LTDA != S/A. SAS != Sociedade Simples. SLU != EIRELI.
- **PA-22** — toda recomendacao e parecer preliminar; advogado responsavel valida antes da constituicao.
- Nao afirmar que determinado tipo "garante" vantagem fiscal sem validar com `analisador-legislacao-vigente` e `planejamento-tributario`.
- Nao recomendar SCP como blindagem de responsabilidade — o socio ostensivo responde ilimitado.

---

## 7. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — validar vigencia de CC/LSA/LC 182 no ano da constituicao.
- **Protocolo 4** (Competencia) — sociedade simples: RCPJ; demais: Junta Comercial.
- **Protocolo 2 — Mitigacao de Risco Fiscal** — verificar substancia economica se o tipo for escolhido por razoes exclusivamente fiscais.

---

## 8. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial` (modo consultivo), operador direto.

**Entrega para:** `constituicao-societaria` (tipo definido → minuta de contrato/estatuto), `registro-empresarial` (tipo define onde registrar), `estruturacao-holdings` (Tier 3) quando for holding.

**Sem esta skill:** constituicao ou reorganizacao pode adotar tipo inadequado ao perfil do cliente — risco de governanca, fiscal e registral.
