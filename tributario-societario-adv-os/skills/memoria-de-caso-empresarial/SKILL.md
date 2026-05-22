---
name: memoria-de-caso-empresarial
description: >
  Mantem o CASO.md persistente e compartimentado — uma pasta por caso, com modo, partes, prazos, historico. Transversal. Aciona: memoria do caso, retomar caso, historico, atualizar o caso.
---

# MEMORIA DE CASO EMPRESARIAL

> Skill **transversal** — gestao do `CASO.md` persistente por caso. Compartimentada por pasta de caso: cada cliente/processo tem sua propria pasta sob `<cwd>/tributario-societario/casos/`. Opera em modo consultivo e contencioso; tributario e societario.

---

## 0. ESCOPO E ACIONAMENTO

Acionada com: "memoria do caso", "retomar caso", "historico do caso", "atualizar o caso", "abrir caso novo", "onde paramos", "registrar atualizacao".

Tambem acionada automaticamente por `triagem-empresarial` (criacao do CASO.md inicial) e por cada skill produtora ao finalizar uma entrega (atualizacao do historico).

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `tributario-societario-master`, `triagem-empresarial`, qualquer skill produtora ao final de entrega, operador direto.
- **Entrega para:** todas as skills — o `CASO.md` e a fonte de contexto compartilhada.
- **Integra com:** `triagem-empresarial` (criacao inicial), `suprema-corte-empresarial` (registro de resultado R1-R4).

---

## 2. ESTRUTURA DE PASTAS

```
<cwd>/tributario-societario/
├── persona.md            (identidade do operador — fora do plugin)
├── config.md             (configuracoes do escritorio)
├── cowork-state.json     (estado do plugin)
└── casos/
    └── <slug-do-caso>/
        ├── CASO.md       (ficha master do caso)
        └── MEMORY.md     (log de atualizacoes e pecas produzidas)
```

**Slug do caso:** formato `<cliente-slug>-<assunto-slug>` — ex: `empresa-abc-auto-infracao-irpj`, `holding-familia-x-constituicao`. Letras minusculas, sem espacos, sem acentos, separado por hifens.

---

## 3. CASO.md — ESTRUTURA CANONICA

O `CASO.md` e a ficha master do caso. Criado pela `triagem-empresarial`, atualizado a cada entrega.

```markdown
# CASO.md — [Nome do Cliente / Empresa]
CNPJ/CPF: [numero ou INFORMAR]
Slug: [slug-do-caso]

## Identificacao
- Cliente: [nome]
- Advogado responsavel: {{ADVOGADO_NOME}}, OAB/{{ADVOGADO_UF}} {{ADVOGADO_OAB}}
- Escritorio: {{FIRM_NAME}}, {{CIDADE}}/{{UF}}
- Data de abertura: [DD/MM/AAAA]
- Ano do fato gerador principal: [AAAA ou INFORMAR]

## Classificacao
- Dominio: [tributario | societario | tributario-societario]
- Modo: [consultivo | contencioso | consultivo-contencioso]
- Competencia federativa: [federal | estadual | municipal]
- Esfera: [administrativa | judicial | administrativa-judicial]
- Orgao atual: [nome — ex: CARF, DRJ, TIT, Vara Federal, Junta Comercial]

## Prazos em curso
- Prazo mais urgente: [descricao — vence em DD/MM/AAAA (estimativa, VERIFICAR)]
- Fase processual: [pre-autuacao | autuado | impugnacao | recurso-carf |
  csrf | judicial | execucao | consultivo-ativo | societario-ativo]

## Resumo da demanda
[2-4 linhas descrevendo o problema central do caso]

## Documentos recebidos
- [lista de documentos ou "nenhum ate o momento"]

## Selos e validacoes
- Selo de Validacao Legal: [A emitir | Emitido em DD/MM/AAAA — normas: ...]
- Ultima auditoria Suprema Corte: [N/A | DD/MM/AAAA — R1/R2/R3/R4: APROVADO]

## Pecas produzidas
| Data | Tipo de peca | Skill produtora | Resultado SC |
|------|-------------|----------------|--------------|
| [DD/MM/AAAA] | [tipo] | [skill] | [APROVADO/RESSALVAS/N/A] |

## Historico de updates
- [DD/MM/AAAA]: [descricao do que foi feito]
```

---

## 4. MEMORY.md — LOG DE ATUALIZACOES

O `MEMORY.md` dentro da pasta do caso e o diario de bordo tecnico — mais detalhado que o historico do `CASO.md`.

```markdown
# MEMORY.md — [slug-do-caso]

## Estado atual
- Fase: [fase processual]
- Ultima etapa concluida: [descricao]
- Proximo passo: [acao imediata]

## Pendencias / Pontos de Omissao
- [INFORMAR]: [dado ausente]
- [VERIFICAR]: [item a confirmar]

## Log cronologico
| Data | Evento | Skill | Detalhe |
|------|--------|-------|---------|
| [DD/MM/AAAA] | [evento] | [skill] | [detalhe tecnico] |
```

---

## 5. OPERACOES

### 5.1 Criar caso novo

Quando o operador inicia um novo caso:

1. Verificar se ja existe pasta com o mesmo slug. Se sim, oferecer retomar.
2. Perguntar o nome do cliente/empresa e o assunto central (para compor o slug).
3. Criar a pasta `<cwd>/tributario-societario/casos/<slug>/`.
4. Criar o `CASO.md` com o cabecalho canonico (secao 3) preenchido com os dados da triagem.
5. Criar o `MEMORY.md` inicial (secao 4).
6. Acionar `triagem-empresarial` se ainda nao foi feita.

### 5.2 Retomar caso existente

Quando o operador retoma um caso:

1. Localizar a pasta do caso pelo slug (argumento) ou listar pastas disponíveis em `casos/`.
2. Ler o `CASO.md` e o `MEMORY.md`.
3. Apresentar resumo:

```
RESUMO DO CASO — [cliente] | [slug]

Dominio: [tributario/societario/tributario-societario]
Modo: [consultivo/contencioso]
Fase: [fase processual]
Prazo urgente: [prazo ou "nenhum em curso"]
Ultima etapa: [do MEMORY.md]
Pendencias: [lista de [INFORMAR] e [VERIFICAR]]
Proximo passo: [do MEMORY.md]
```

4. Perguntar se o operador quer continuar de onde parou ou iniciar nova etapa.

### 5.3 Atualizar caso apos entrega

Ao final de toda entrega aprovada pela `suprema-corte-empresarial`:

1. Abrir o `CASO.md` do caso ativo.
2. Adicionar a peca entregue na tabela "Pecas produzidas".
3. Registrar o resultado da Suprema Corte (R1-R4).
4. Atualizar a "Fase processual" se mudou.
5. Atualizar o prazo mais urgente se aplicavel.
6. Adicionar entrada no "Historico de updates".
7. Atualizar o `MEMORY.md` com a nova entrada no log cronologico.

### 5.4 Listar casos

```
CASOS ATIVOS — {{FIRM_NAME}}
[Lista das pastas em casos/ com: slug, cliente, dominio, modo, fase, prazo urgente]
```

---

## 6. COMPARTIMENTACAO POR CASO

**Regra absoluta:** cada caso ocupa sua propria pasta. Dados de um caso nunca aparecem no `CASO.md` de outro.

- O operador pode ter multiplos casos abertos simultaneamente.
- O caso ativo e o referenciado no argumento do comando ou o mais recente atualizado.
- Em caso de ambiguidade, perguntar qual caso antes de qualquer acao.

---

## 7. PRIVACIDADE E LGPD

**Dados do cliente:** CPF, CNPJ, valores de tributo, numeros de processo — sao dados pessoais/empresariais sensiveis.

- Os arquivos `CASO.md` e `MEMORY.md` residem no diretorio local do operador (`<cwd>/tributario-societario/casos/`) — **nunca no plugin**.
- O plugin nao acessa esses dados remotamente.
- O operador e responsavel por nao sincronizar esses arquivos para servicos de nuvem sem controle de acesso (iCloud, Dropbox, Google Drive em pasta publica).
- **Alerta automatico:** se o diretorio `casos/` for detectado dentro de pasta sincronizada, emitir:
  ```
  ALERTA LGPD: o diretorio casos/ parece estar em pasta sincronizada ([caminho]).
  Dados de clientes nao devem ser sincronizados sem controle de acesso adequado.
  Mova para um diretorio local seguro.
  ```
- Ao exibir dados de caso no chat, usar apenas os dados necessarios para a tarefa.

---

## 8. VEDACOES ESPECIFICAS

- **PA-22** — o operador e o advogado responsavel; o plugin apenas organiza as informacoes.
- Nao criar caso sem pelo menos o nome do cliente e o assunto central.
- Nao mesclar dados de clientes distintos no mesmo `CASO.md`.
- Nao assumir qual caso esta ativo sem verificar — sempre confirmar com o operador em caso de ambiguidade.

---

## 9. PROTOCOLOS ACIONADOS

- **Protocolo 4** (Competencia) — o `CASO.md` registra competencia e esfera identificadas na triagem.
- **Protocolo 1** (Validacao Legal Previa) — o `CASO.md` registra se o Selo foi emitido.

---

## 10. INTEGRACAO

**Chamada por:** `tributario-societario-master`, `triagem-empresarial`, skills produtoras (atualizacao pos-entrega), operador direto.

**Entrega para:** todas as skills — o `CASO.md` e o contexto compartilhado do caso ativo.

**Sem esta skill:** cada sessao reinicia do zero; prazos, historico e documentos sao perdidos entre conversas.
