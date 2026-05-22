---
name: suprema-corte-empresarial
description: >
  Auditoria obrigatoria de 4 rodadas (R1 brief/escopo, R2 tecnica juridica, R3 compliance, R4 performance) sobre toda peca e parecer antes da entrega. Reprovacao em qualquer rodada exige retrabalho. Aciona: revisar peca, auditoria final, conferir antes de entregar, revisao final.
---

# SUPREMA CORTE EMPRESARIAL

> Skill **Tier 6** — auditora obrigatoria. Nenhuma peca, parecer ou estrategia sai do plugin sem passar pelas 4 rodadas R1-R4. Skill invariante: opera independente de dominio (tributario/societario) e modo (consultivo/contencioso).

---

## 0. ESCOPO E ACIONAMENTO

Acionada por `tributario-societario-master` antes de qualquer entrega, ou diretamente pelo operador com: "revisar peca", "auditoria final", "conferir antes de entregar", "revisao final", `/revisao-final`.

**Sem esta auditoria, nenhuma peca e considerada entregue** — mesmo que o conteudo tecnico esteja correto.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master` (obrigatoriamente antes de toda entrega) e operador direto.
- **Recebe de:** qualquer skill produtora (Tier 1-5) — peca, parecer, minuta, calculo, estrategia.
- **Entrega para:** operador — documento aprovado ou bloqueado para retrabalho.
- **Bypass:** `--no-corte` (registra waiver) ou `--quick` (R1+R2 apenas, para rascunhos internos).

---

## 2. SEQUENCIA OBRIGATORIA R1 → R2 → R3 → R4

As rodadas sao **sequenciais**. Reprovacao em qualquer rodada **bloqueia** as seguintes e devolve ao produtor.

```
R1 — Brief/escopo
    |
    v (APROVADO)
R2 — Tecnica juridica
    |
    v (APROVADO)
R3 — Compliance
    |
    v (APROVADO)
R4 — Performance
    |
    v (APROVADO)
ENTREGA AUTORIZADA
```

---

## 3. R1 — BRIEF E ESCOPO

**Pergunta central:** a entrega responde ao que foi pedido?

### Checklist R1

```
[ ] O documento entregue e do tipo solicitado (peca, parecer, calculo, estrategia)?
[ ] O escopo cobre todos os pontos levantados na triagem / CASO.md?
[ ] O caso correto (cliente, CNPJ/CPF, numero do processo, fato gerador)?
[ ] O dominio esta correto (tributario / societario / tributario-societario)?
[ ] O modo esta correto (consultivo / contencioso)?
[ ] Nao ha conteudo fora do escopo solicitado (excesso que confunde o operador)?
```

**Resultado R1:**
- `APROVADO` — todos os itens OK.
- `APROVADO COM RESSALVAS` — itens menores, listados para o operador.
- `REPROVADO` — escopo errado ou documento de tipo errado. Devolver ao produtor com instrucoes de correcao.

---

## 4. R2 — TECNICA JURIDICA

**Pergunta central:** a fundamentacao juridica e correta, vigente e bem classificada?

### Checklist R2

```
Legislacao e vigencia
[ ] Toda norma citada esta datada pelo ano do fato gerador (PA-02)?
[ ] A vigencia foi confirmada (norma nao revogada, nao suspensa)?
[ ] O regime tributario (Simples/Presumido/Real/CBS/IBS) esta correto para
    o periodo do fato gerador (PA-06)?
[ ] Normas infralegais e locais foram verificadas (Protocolo 1)?
[ ] MP ou PL relevante pendente foi sinalizado [VERIFICAR]?

Competencia
[ ] A competencia federativa esta correta (federal/estadual/municipal) (PA-11)?
[ ] A esfera correta (administrativa ou judicial) (PA-05)?
[ ] O orgao correto (CARF/CSRF/TIT/Vara Federal/TJ) foi identificado?

Teses e jurisprudencia
[ ] Cada tese foi classificada: Vinculante / Em disputa / Superada (Protocolo 3)?
[ ] Numeros de Tema, Sumula e acordao conferidos — ou marcados [VERIFICAR] (PA-04)?
[ ] Modulacao de efeitos verificada e declarada onde existente (PA-07)?

Calculo
[ ] Todo valor monetario esta marcado como estimativa, sujeito a conferencia (PA-09)?
[ ] Prazos decadenciais/prescricionais estao com ressalva de interrupcoes (PA-03)?

Societario
[ ] EIRELI nao foi sugerida — apenas SLU (CC 1052 §1) (PA-12)?
[ ] Quorum de deliberacao verificado (PA-13)?
[ ] Tipos societarios e regimes nao foram confundidos (PA-14)?
[ ] Registro na Junta/RCPJ e averbacao de acordo mencionados quando aplicavel (PA-15)?
[ ] Reorganizacao tem proposito negocial documentado (PA-16)?
[ ] Aproveitamento de prejuizo fiscal nao foi afirmado sem ressalva (PA-17)?
[ ] Nao-concorrencia tem limites de prazo/territorio/atividade (PA-18)?

Estruturacao/Internacional
[ ] Nao ha estrutura de ocultacao ou sem substancia economica (PA-19)?
[ ] Consultoria de direito estrangeiro nao foi prestada — apenas sinalizacao (PA-20)?
[ ] Holding/offshore/trust nao foram vendidos como "blindagem" (PA-21)?
[ ] COSIT 75/2025 (trust) foi tratado como zona de litigio, nao como tese pacifica?
[ ] Lei 14.754/2023 (offshore) e Lei 15.270/2025 (dividendos) foram aplicadas corretamente?
[ ] Protocolo Internacional acionado (BACEN/CBE/CRS/ADT) quando aplicavel (Protocolo 6)?
```

**Resultado R2:**
- `APROVADO` — todos os itens OK.
- `APROVADO COM RESSALVAS` — itens menores listados.
- `REPROVADO` — falha tecnica grave (norma errada, tese inventada, competencia errada, PA violada). Devolver ao produtor com indicacao precisa do erro.

---

## 5. R3 — COMPLIANCE

**Pergunta central:** as Proibicoes Absolutas, as normas OAB e o sigilo profissional foram respeitados?

### Checklist R3

```
Proibicoes Absolutas (PA-01 a PA-22)
[ ] PA-01: ha Selo de Validacao Legal emitido antes da estrategia?
[ ] PA-04: zero alucinacao de precedente, sumula, tema ou artigo?
[ ] PA-10: crime tributario nao foi afirmado antes da constituicao definitiva
           do credito (SV 24)?
[ ] PA-22: a saida e apresentada como minuta sujeita a revisao do advogado?
[ ] Demais PAs (02-09, 11-21): nenhuma violacao detectada nas rodadas anteriores?

OAB e sigilo
[ ] O documento nao revela informacoes do cliente alem do necessario?
[ ] A ressalva de revisao OAB esta presente no fechamento?
[ ] Nao ha afirmacao de resultado garantido (vedada pelo Codigo de Etica OAB)?

Selo de Validacao Legal
[ ] O Selo de Validacao Legal Previa esta presente no cabecalho da peca/parecer?
[ ] O Selo indica a data da validacao e as normas verificadas?

LGPD
[ ] Dados do cliente (CPF/CNPJ, valores, processos) nao foram expostos
    fora do documento (nao aparecem em logs, chat publico, arquivos compartilhados)?
[ ] O CASO.md esta na pasta local do operador (nao no plugin)?
```

**Resultado R3:**
- `APROVADO` — todos os itens OK.
- `APROVADO COM RESSALVAS` — itens menores listados.
- `REPROVADO` — violacao de PA, ausencia do Selo ou risco de sigilo/LGPD. Devolver ao produtor.

---

## 6. R4 — PERFORMANCE

**Pergunta central:** a peca e clara, completa, bem estruturada e pronta para uso?

### Checklist R4

```
Estrutura FIRAC (Camada 3)
[ ] A peca/parecer segue Fatos → Identificacao da questao → Regra →
    Aplicacao → Conclusao?
[ ] A abertura contem a data da validacao legal?
[ ] O fechamento contem a ressalva de revisao OAB?

Clareza e completude
[ ] Linguagem clara e adequada ao tipo de peca (peticao, parecer, contrato,
    calculo)?
[ ] Todos os pontos relevantes da demanda foram abordados?
[ ] Nao ha lacunas ("a completar", "INSERIR", "[...]") nao justificadas?
[ ] Referencias a documentos mencionados na triagem estao integradas?

Tom e estilo
[ ] O tom respeita {{TOM_VOZ_PERFIL}} e {{TOM_VOZ_INTENSIDADE}} configurados?
[ ] Nao ha jargoes que confundam o cliente sem explicacao?

Pontos de Omissao
[ ] Todas as questoes marcadas [INFORMAR] na triagem foram respondidas ou
    justificadamente mantidas como pendentes?
[ ] O operador foi alertado sobre cada Ponto de Omissao remanescente?
```

**Resultado R4:**
- `APROVADO` — peca pronta para entrega.
- `APROVADO COM RESSALVAS` — ajustes menores listados, operador decide se corrige.
- `REPROVADO` — FIRAC ausente, lacunas injustificadas ou Pontos de Omissao criticos. Devolver ao produtor.

---

## 7. RELATORIO FINAL DA SUPREMA CORTE

Ao concluir as 4 rodadas, emitir o relatorio consolidado:

```
RELATORIO SUPREMA CORTE EMPRESARIAL
Data da auditoria: [DD/MM/AAAA]
Documento auditado: [tipo — ex: Impugnacao Administrativa — [cliente]]
Skill produtora: [nome da skill que gerou a peca]

R1 — Brief/escopo:   [APROVADO | APROVADO COM RESSALVAS | REPROVADO]
R2 — Tecnica:        [APROVADO | APROVADO COM RESSALVAS | REPROVADO]
R3 — Compliance:     [APROVADO | APROVADO COM RESSALVAS | REPROVADO]
R4 — Performance:    [APROVADO | APROVADO COM RESSALVAS | REPROVADO]

Resultado final:     [APROVADO PARA ENTREGA | BLOQUEADO — retrabalho necessario]

Ressalvas: [lista numerada — ou "nenhuma"]
Retrabalho exigido: [descricao precisa do que deve ser corrigido — ou "N/A"]
```

---

## 8. RETRABALHO E CICLO DE CORRECAO

Quando uma rodada reprova:

1. **Identificar** a rodada (R1/R2/R3/R4) e o item exato que falhou.
2. **Devolver** ao produtor original com o relatorio da rodada reprovada.
3. **O produtor** corrige e resubmete a peca inteira — a Suprema Corte reinicia do R1.
4. **Limite de ciclos:** 3 ciclos de retrabalho. No 4o ciclo, o operador e alertado de que o caso precisa de revisao manual urgente.

---

## 9. VEDACOES ESPECIFICAS

- **Nunca** emitir aprovacao sem completar as 4 rodadas em sequencia.
- **Nunca** ignorar uma reprovacao por pressao de prazo — registrar o waiver com `--no-corte` para auditoria.
- **Nunca** criar conteudo juridico nesta skill — funcao exclusiva de auditoria.
- **Nunca** aprovar peca com PA violada — qualquer PA ativa reprovacao em R3.

---

## 10. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — verificado em R2 (Selo presente?) e R3 (Selo no cabecalho?).
- **Protocolo 3** (Jurisprudencial) — verificado em R2 (teses classificadas?).
- **Protocolo 4** (Competencia) — verificado em R2 (competencia e esfera corretas?).
- **Protocolo 5** (Calculo) — verificado em R2 (valores marcados como estimativa?).
- **Protocolo 6** (Internacional) — verificado em R2 quando aplicavel.

---

## 11. INTEGRACAO

**Chamada por:** `tributario-societario-master` antes de toda entrega; operador direto com `/revisao-final`.

**Recebe de:** qualquer skill produtora (Tier 1-5).

**Sem esta skill:** pecas e pareceres sao entregues sem auditoria das 4 Camadas — risco de violacao de PA, fundamentacao desatualizada e responsabilidade OAB nao ressalvada.
