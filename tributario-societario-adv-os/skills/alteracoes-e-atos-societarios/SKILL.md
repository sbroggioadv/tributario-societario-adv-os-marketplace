---
name: alteracoes-e-atos-societarios
description: >
  Minutas de alteracao contratual (LTDA/SLU), atas de assembleia e reuniao de socios, com checagem de quorum legal vigente. Atencao: quorum de 3/4 da LTDA foi revogado pela Lei 14.451/2022 — alteracao contratual = maioria (mais da metade do capital social — CC 1.076). Aciona: alterar contrato, ata, assembleia, mudar capital, entrada de socio, retirada.
---

# ALTERACOES E ATOS SOCIETARIOS

> Skill **Tier 2 — Societario** — minutas de alteracoes contratuais, atas de assembleia e reunioes de socios. Implementa o quorum vigente pos-Lei 14.451/2022 (PA-13). Mode: consultivo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "alterar contrato", "ata de assembleia", "ata de reuniao de socios", "mudar capital", "entrada de socio", "retirada de socio", "mudanca de objeto", "mudanca de sede", "aumentar capital", "reduzir capital", "alterar administracao".

Entrega: minuta de alteracao contratual ou ata de assembleia/reuniao + tabela de quoruns aplicavel + roteiro de arquivamento.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial` (societario consultivo), operador direto.
- **Entrega para:** `registro-empresarial` (arquivamento da alteracao), `governanca-e-acordos` (se envolver acordo de socios), `dissolucao-e-saida-de-socio` (se envolver saida formal),
  `suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).
- **Pre-requisito:** `analisador-legislacao-vigente` confirmar normas vigentes (CC + Lei 14.451/2022).

---

## 2. QUORUNS VIGENTES — LTDA (POS-LEI 14.451/2022)

> **PA-13 — ALERTA CRITICO:**
> O quorum de **3/4 do capital** para alteracao do contrato social **NAO EXISTE MAIS** para a LTDA.
> Foi revogado pela Lei 14.451/2022 (art. 1o, que alterou o CC 1.076).
> Desde 23/11/2022: alteracao contratual = **maioria (mais da metade do capital social — CC 1.076)**.

### 2.1 Tabela de quoruns LTDA (CC 1.076 — redacao pos-Lei 14.451/2022)

| Deliberacao | Quorum | Base legal |
|------------|--------|-----------|
| Alteracao do contrato social | maioria (mais da metade do capital social — CC 1.076) | CC 1.076, I (redacao Lei 14.451/2022) |
| Designacao/destituicao de administradores nao socios | maioria (mais da metade do capital social — CC 1.076) | CC 1.076, II |
| Destituicao de administrador socio | maioria (mais da metade do capital social — CC 1.076) — salvo clausula | CC 1.063, §1o |
| Aprovacao das contas | maioria (mais da metade do capital social — CC 1.076) | CC 1.076, II |
| Exclusao de socio por justa causa | maioria dos demais socios (por cabeca, nao do capital — CC 1.085) | CC 1.085 |
| Dissolucao | maioria (mais da metade do capital social — CC 1.076) | CC 1.033, III |
| Transformacao, incorporacao, fusao, cisao | Unanimidade (salvo clausula em contrario) | CC 1.114-1.116 [VERIFICAR] |

> O contrato social pode estabelecer quorum contratual MAIS ELEVADO para determinadas materias, mas nunca abaixo do minimo legal.

### 2.2 Quoruns S/A (Lei 6.404/76)

| Deliberacao | Quorum (instalacao) | Quorum (aprovacao) | Base legal |
|------------|--------------------|--------------------|-----------|
| AGO / AGE (1a convocacao) | > 25% do capital votante | Maioria dos presentes | LSA 125/129 |
| AGO / AGE (2a convocacao) | Qualquer numero | Maioria dos presentes | LSA 125/129 |
| Reforma estatutaria relevante (emissao debentures, aumento capital, mudanca de objeto) | > 50% do capital votante (1a conv.) | Maioria absoluta | LSA 135 |
| Dissolucao voluntaria | > 50% do capital votante | Maioria absoluta | LSA 136, VIII |
| Transformacao, incorporacao, fusao, cisao | > 50% do capital votante | Maioria absoluta (dissidentes tem direito de retirada) | LSA 136-137 |

### 2.3 Quoruns SCP (CC 991-996)

SCP nao tem personalidade juridica; deliberacoes regem-se pelo contrato interno entre socios. Sem registro societario na Junta — alteracoes sao apenas contratuais (entre socios).

---

## 3. ALTERACAO CONTRATUAL — LTDA/SLU

### 3.1 Materias mais comuns e documentos necessarios

| Materia | Instrumento | Documentos adicionais |
|---------|------------|----------------------|
| Mudanca de sede | Alteracao contratual | Comprovante do novo endereco |
| Mudanca de objeto social | Alteracao contratual | CNAE novo; verificar licencas |
| Entrada de novo socio (cessao de quotas) | Alteracao contratual + instrumento de cessao | Qualificacao do novo socio; direito de preferencia dos socios |
| Saida de socio (cessao ou retirada) | Alteracao contratual + ato de apuracao de haveres se retirada | Ver `dissolucao-e-saida-de-socio` |
| Aumento de capital | Alteracao contratual | Comprovante de integralizacao (se em dinheiro) ou laudo (se em bens) |
| Reducao de capital | Alteracao contratual | Publicacao previa (CC 1.082) + prazo para oposicao de credores (60 dias) |
| Alteracao de administracao | Alteracao contratual ou ata de reuniao | Qualificacao do novo administrador |
| Prorrogacao do prazo (se determinado) | Alteracao contratual | — |

### 3.2 Esquema de alteracao contratual

```markdown
PRIMEIRA ALTERACAO DO CONTRATO SOCIAL DE [DENOMINACAO] LTDA.

Os socios abaixo assinados, titulares de [%] do capital social, reunidos em [data] na sede
social sita a [endereco], deliberaram por [unanimidade / maioria representando [%] do capital
— conforme CC 1.076 redacao dada pela Lei 14.451/2022], alterar o contrato social nos
seguintes termos:

CLAUSULA [N]a — [MATERIA A SER ALTERADA]
Onde se lia: "[redacao anterior]"
Passa a vigorar: "[nova redacao]"

As demais clausulas do contrato social permanecem inalteradas.

{{CIDADE}}, [data].

[Assinaturas dos socios + administrador + testemunhas]
```

---

## 4. ATA DE REUNIAO DE SOCIOS — LTDA

Reuniao de socios: prevista no CC 1.072; obrigatoria para LTDA com + de 10 socios (AGO). Com ate 10 socios, admite-se reuniao informal ou deliberacao por escrito (CC 1.072, §§3o-6o).

### 4.1 Esquema de ata de reuniao

```markdown
ATA DE REUNIAO DE SOCIOS DE [DENOMINACAO] LTDA.

DATA: [DD/MM/AAAA]
LOCAL: sede social — [endereco completo] / ou: realizada por videoconferencia conforme CC 1.072, §6o [VERIFICAR]
HORA DE INICIO: [hh:mm]
PRESENTES: [Nome Socio A] — [n] quotas — [%]; [Nome Socio B] — [n] quotas — [%]
REPRESENTANDO: [%] do capital social total
MESA: presidente [nome]; secretario [nome]

1. ABERTURA
[Verificacao de quorum e instalacao da reuniao.]

2. PAUTA
2.1 [Primeiro item da pauta]
2.2 [Segundo item da pauta]

3. DELIBERACOES

3.1 [Descricao da materia]: Colocado em votacao, APROVADO por [unanimidade / maioria
representando [%] do capital — quorum CC 1.076, I, redacao Lei 14.451/2022].

3.2 [Descricao da materia]: [...].

4. ENCERRAMENTO
Nada mais havendo, encerrou-se a reuniao, da qual se lavrou a presente ata, lida e aprovada
por todos os presentes.

{{CIDADE}}, [data].

Presidente: _________________________ Secretario: _________________________

[Assinaturas dos socios presentes]
```

---

## 5. ATA DE ASSEMBLEIA GERAL — S/A E SAS

### 5.1 Elementos obrigatorios (LSA art. 130)

```markdown
ATA DE ASSEMBLEIA GERAL [ORDINARIA/EXTRAORDINARIA] DE [DENOMINACAO] S.A.

Data, hora e local; convocacao (modo: jornal / dispensa em SAS ou unanimidade); presenca
(lista de acionistas + qualificacao + acoes por classe); quorum de instalacao verificado;
mesa (presidente + secretario); pauta; resumo das discussoes; deliberacoes com quoruns
registrados; resultado das votacoes; encerramento; assinatura da mesa.
```

### 5.2 Publicacao

- S/A fechada: publicacao em jornal de grande circulacao e no Diario Oficial (arts. 289 e 294 LSA [VERIFICAR]), salvo dispensa prevista no estatuto ou unanimidade dos acionistas.
- SAS: dispensa publicacao em jornal (LC 182/2021). Ata arquivada na Junta sem publicacao.

---

## 6. PUBLICIDADE DE ATOS SOCIETARIOS

| Tipo | Publicacao obrigatoria | Base |
|------|----------------------|------|
| LTDA | Nao exige publicacao em jornal (regra geral) — apenas arquivamento na Junta | CC 1.151 |
| S/A fechada | Ata de AGO e balancos no Diario Oficial e jornal (pode ser dispensada por unanimidade em S/A com ate 20 acionistas — art. 294 LSA [VERIFICAR]) | LSA 130, 289 |
| SAS | Sem publicacao em jornal | LC 182/2021 |
| Reducao de capital LTDA | Publicacao previa obrigatoria + prazo 60 dias credores | CC 1.082 |

---

## 7. CESSAO DE QUOTAS — ASPECTOS CRITICOS

- **Cessao entre socios:** livre, salvo restricao contratual.
- **Cessao a terceiro:** cessao de quota a terceiro: livre se nao houver oposicao de socios titulares de mais de 1/4 do capital (CC 1.057), salvo clausula contratual mais restritiva.
- Direito de preferencia: se houver clausula, socios tem preferencia pelo mesmo preco oferecido ao terceiro.
- Instrumento: alteracao contratual (ou instrumento de cessao averbado + alteracao para refletir nova composicao).
- Responsabilidade do cedente: solidaria com o cessionario por 2 anos pelas obrigacoes da sociedade anteriores a cessao (CC 1.003, §unico).

---

## 8. VEDACOES ESPECIFICAS

- **PA-13** — nunca citar quorum de 3/4 como exigencia vigente para LTDA. Alteracao contratual exige maioria (mais da metade do capital social — CC 1.076) desde 23/11/2022 (Lei 14.451/2022). Quorum contratual mais elevado por clausula: permitido.
- **PA-14** — nao aplicar quoruns da S/A em LTDA nem vice-versa.
- **PA-15** — toda alteracao contratual e ata de AGE com materia sujeita a registro devem ser arquivadas na Junta Comercial (LTDA/S/A) ou RCPJ (Sociedade Simples). Acionar `registro-empresarial`.
- **PA-22** — toda minuta e sujeita a revisao pelo advogado responsavel antes da assinatura e arquivamento.

---

## 9. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — confirmar CC 1.076 na redacao da Lei 14.451/2022 + LSA vigente.
- **Protocolo 4** (Competencia) — LTDA/S/A: Junta Comercial. Sociedade Simples: RCPJ.

---

## 10. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, operador direto.

**Entrega para:** `registro-empresarial` (arquivamento), `governanca-e-acordos` (se envolver acordo de socios ou tag/drag along), `dissolucao-e-saida-de-socio` (se envolver saida formal de socio),
`suprema-corte-empresarial` (R1-R4 obrigatorio antes da entrega da minuta/peca ao cliente).

**Sem esta skill:** atos societarios lavrados com quorum incorreto — risco de invalidade e rejeicao na Junta.
