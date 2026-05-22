---
name: estilo-juridico-empresarial
description: >
  Estrutura e estilo das pecas — modelo FIRAC, tom, formatacao, abertura com data da validacao legal e fechamento com ressalva de revisao OAB. Transversal, acionada por todas as skills produtoras. Aciona: redacao, estilo da peca, formatar, estrutura do documento.
---

# ESTILO JURIDICO EMPRESARIAL

> Skill **transversal** — define a estrutura, o estilo e a formatacao de toda peca e parecer produzidos pelo plugin. Acionada automaticamente por todas as skills produtoras (Tier 1-5) antes de redigir qualquer documento. Invariante de dominio e modo.

---

## 0. ESCOPO E ACIONAMENTO

Acionada implicitamente por toda skill que produz documento (peca, parecer, contrato, calculo, estrategia). Ativacao direta pelo operador: "estilo da peca", "como estruturar", "formatar o documento", "redacao juridica", "estrutura FIRAC".

Entrega: template de estrutura aplicado ao documento solicitado, com tom ajustado pelo perfil do operador.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** toda skill produtora (Tier 1-5) ao iniciar a redacao de um documento.
- **Integra com:** `suprema-corte-empresarial` — a auditoria R4 verifica se esta skill foi aplicada (FIRAC presente, abertura e fechamento corretos).
- **Pre-requisito para:** qualquer entrega — documento sem estrutura FIRAC falha na R4.

---

## 2. ESTRUTURA FIRAC

Toda peca, parecer, estrategia e analise segue o modelo **FIRAC**:

### F — Fatos

```
FATOS
[Data de validacao legal: DD/MM/AAAA — normas verificadas: ...]

Relato dos fatos relevantes do caso:
- Quem sao as partes (cliente, contraparte, orgao fiscal, Junta)?
- Qual o fato gerador / fato juridico central?
- Periodo de competencia / ano do fato gerador?
- Documentos recebidos e analisados?
- Cronologia relevante?
```

Regra: fatos devem ser neutros e precisos. Nao antecipar a tese nos fatos.

### I — Identificacao da questao juridica

```
QUESTAO JURIDICA
[Formular a questao de forma clara e delimitada.]

Exemplo: "Verifica-se se o aproveitamento de credito de PIS/COFINS sobre
[insumo] e admissivel no regime de apuracao nao-cumulativa, para o periodo
de competencia [AAAA], ante a redacao do art. [X] da Lei [Y] vigente naquele
exercicio."
```

Regra: uma questao principal, ate 2 questoes acessorias. Questoes demais = escopo nao delimitado (falha R1).

### R — Regra (norma vigente + jurisprudencia classificada)

```
FUNDAMENTO LEGAL E JURISPRUDENCIAL
Data-base desta analise: [DD/MM/AAAA]

Legislacao aplicavel:
- [Lei/Decreto/IN vigente no ano do fato gerador, com o artigo exato]
- [Norma infralegal ou local relevante, se houver]
- [MP/PL pendente, se relevante — sinalizar [VERIFICAR]]

Jurisprudencia (Protocolo 3 — classificada):
- Vinculante: [Tema/Sumula/acordao — numero e resultado]
- Em disputa: [tese — sinalizar [VERIFICAR — tese em disputa]]
- Superada: [tese superada — indicar o que a substituiu]
```

Regra: toda norma citada recebe o ano de vigencia. Nenhuma referencia inventada — marcar [VERIFICAR] se incerto (PA-04).

### A — Aplicacao

```
APLICACAO AO CASO CONCRETO

[Raciocinio de subsuncao: norma vigente no periodo + fatos do caso →
 como a regra se aplica ao caso especifico do cliente]

[Identificar: o que encaixa? o que nao encaixa? o que e disputado?]
[Para cada tese: classificar risco — Provavel / Possivel / Remoto]
```

### C — Conclusao

```
CONCLUSAO

[Resposta objetiva a questao juridica levantada na secao I]
[Recomendacao ao operador — o que fazer?]
[Ressalvas remanescentes — o que ainda precisa de verificacao?]

RESSALVA: esta [peca / parecer / analise] e uma minuta tecnica baseada nas
informacoes fornecidas e nas normas vigentes na data indicada. Sujeita a
revisao pelo advogado responsavel antes de qualquer ato processual,
contratual ou declaratorio. Responsabilidade OAB do signatario. PA-22.
```

---

## 3. ABERTURA OBRIGATORIA — SELO DE VALIDACAO LEGAL

Todo documento abre com o **Selo de Validacao Legal Previa** (Protocolo 1):

```
---------------------------------------------------------------------
VALIDACAO LEGAL PREVIA
Data da validacao: [DD/MM/AAAA]
Normas verificadas: [lista das normas auditadas]
Vigencia confirmada: [sim / parcial — ver ressalvas]
Emitido por: analisador-legislacao-vigente
---------------------------------------------------------------------
```

Se o Selo ainda nao foi emitido, bloquear a redacao e acionar `analisador-legislacao-vigente` (PA-01).

---

## 4. FECHAMENTO OBRIGATORIO — RESSALVA OAB

Todo documento fecha com:

```
---------------------------------------------------------------------
RESSALVA DE REVISAO
Esta [peca / parecer / minuta / analise] e produto do plugin Tributario-
Societario-Adv-OS, elaborado como suporte tecnico ao advogado operador.
Nao substitui o juizo profissional do advogado responsavel pela causa.
Revisao obrigatoria pelo advogado antes de qualquer ato formal. OAB — PA-22.
Data de geracao: [DD/MM/AAAA]
Operador: {{ADVOGADO_NOME}}, OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
          {{FIRM_NAME}}, {{CIDADE}}/{{UF}}
---------------------------------------------------------------------
```

---

## 5. TOM E VOZ

O tom do documento respeita a persona configurada em runtime:

| Token | O que configura |
|-------|----------------|
| `{{TOM_VOZ_PERFIL}}` | Perfil do tom — ex: "tecnico e assertivo", "didatico e acessivel" |
| `{{TOM_VOZ_INTENSIDADE}}` | Intensidade de 1 a 10 — 1 = academico frio, 10 = combativo incisivo |

### Guia de aplicacao por perfil

| Intensidade | Caracteristicas |
|-------------|----------------|
| 1-3 | Academico: construcao doutrinaria, citacoes longas, tom neutro, sem juizos de valor |
| 4-6 | Tecnico-assertivo (padrao): fundamentacao solida, tese clara, evita ambiguidades |
| 7-8 | Combativo: reforco dos argumentos favoraveis, antecipacao adversarial explicitada |
| 9-10 | Incisivo: destacar fraquezas da parte contraria, postura pro-ativa nas teses |

> Independente do tom, a fundamentacao juridica e sempre rigorosa — o tom afeta a densidade argumentativa e o estilo retorico, nao a precisao tecnica.

---

## 6. FORMATACAO POR TIPO DE DOCUMENTO

### 6.1 Peticoes processuais (impugnacao, recurso, embargos, MS)

```
EXCELENTISSIMO(A) SENHOR(A) [CARGO / ORGAO]

[CLIENTE], [qualificacao], por seu advogado [{{ADVOGADO_NOME}}, OAB/{{ADVOGADO_UF}}
{{ADVOGADO_OAB}}], vem, respeitosamente, perante Vossa Excelencia, apresentar

[TIPO DE PECA] n. [numero do processo, se houver],

pelos fundamentos a seguir:

[Corpo — FIRAC]

REQUERIMENTO FINAL
[pedidos objetivos numerados]

Termos em que,
Pede deferimento.

{{CIDADE}}, [DD] de [mes] de [AAAA].

{{ADVOGADO_NOME}}
OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
{{FIRM_NAME}}
```

### 6.2 Pareceres e consultas

```
PARECER [NUMERO/ANO]
Consulente: [nome/CNPJ]
Objeto: [tema da consulta]
Data-base: [DD/MM/AAAA]

[Corpo — FIRAC]

CONCLUSAO
[resposta objetiva]

{{CIDADE}}, [DD] de [mes] de [AAAA].

{{ADVOGADO_NOME}}
OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
{{FIRM_NAME}}
```

### 6.3 Atos societarios (contrato social, ata, acordo)

```
[TIPO DE ATO]

[Cabecalho: partes, qualificacoes, CNPJ]
[CLAUSULAS numeradas — nao usar letras, apenas numeros]
[Clausula de foro: Comarca de {{CIDADE}}/{{UF}}]

[Assinaturas: {{ADVOGADO_NOME}}, OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}]
```

### 6.4 Analises e estrategias

Formato livre, mas sempre com:
- Cabecalho: cliente, data-base, dominio, modo.
- Corpo FIRAC adaptado (Fatos → Questao → Fundamento → Analise → Recomendacao).
- Fechamento com ressalva OAB.

---

## 7. PONTOS DE OMISSAO

Quando dados necessarios nao foram fornecidos, nao supor — sinalizar:

```
[INFORMAR]: [dado ausente]
```

Exemplos:
- `[INFORMAR]: valor do credito tributario autuado`
- `[INFORMAR]: data do auto de infracao`
- `[INFORMAR]: CNPJ do cliente`

Acumular todos os Pontos de Omissao ao fim do documento em lista separada.

---

## 8. VEDACOES ESPECIFICAS

- **PA-01** — nunca redigir peca sem o Selo de Validacao Legal no cabecalho.
- **PA-04** — nunca inventar norma, artigo, sumula ou acordao — marcar [VERIFICAR].
- **PA-09** — nunca apresentar valor monetario sem marca de estimativa.
- **PA-22** — a ressalva OAB no fechamento e obrigatoria em todo documento.
- Nao usar o caractere en-dash (Unicode U+2013) como travessao — usar em-dash (`—`) ou virgula.

---

## 9. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — Selo de Validacao no cabecalho.
- **Protocolo 3** (Jurisprudencial) — jurisprudencia classificada na secao R do FIRAC.
- **Protocolo 5** (Calculo) — valores marcados como estimativa.

---

## 10. INTEGRACAO

**Chamada por:** toda skill produtora (Tier 1-5) ao iniciar redacao de documento.

**Entrega para:** `suprema-corte-empresarial` (a R4 verifica a aplicacao desta skill).

**Sem esta skill:** documentos entregues sem estrutura FIRAC, sem abertura de Selo, sem fechamento OAB — reprovados em R4 da Suprema Corte.
