---
name: registro-empresarial
description: >
  Checklist de arquivamento na Junta Comercial ou RCPJ — exigencias da IN DREI vigente, documentos, prazos, averbacao de acordo de socios. Aciona: registrar na junta, arquivamento, DREI, registro do contrato social, arquivar ato societario, registro societario.
---

# REGISTRO EMPRESARIAL

> Skill **Tier 2 — Societario** — checklist e roteiro de arquivamento de atos societarios na Junta Comercial (LTDA, S/A, SAS, SCP) ou RCPJ (Sociedade Simples). Implementa PA-15. Mode: ambos (consultivo e contencioso).

---

## 0. ESCOPO E ACIONAMENTO

Acionada por "registrar na junta", "arquivamento", "DREI", "registro do contrato social", "arquivar ato societario", "registro societario", "arquivar ata", "averbacao de acordo".

Entrega: checklist de documentos e exigencias por tipo de ato + prazos + roteiro de averbacao de acordo de socios.

---

## 1. POSICAO NA ORQUESTRA

- **Chamada por:** `constituicao-societaria`, `alteracoes-e-atos-societarios`, `reorganizacao-societaria`, `dissolucao-e-saida-de-socio`, `governanca-e-acordos` (averbacao de acordo), triagem direto.
- **Pre-requisito:** aciona `analisador-legislacao-vigente` para confirmar a IN DREI vigente antes do checklist — a IN e periodicamente atualizada (PA-02).
- **Entrega para:** operador (checklist pronto para protocolo na Junta/RCPJ).
- **Atencao:** a IN DREI 81/2020 foi objeto de atualizacoes em 2024 e 2025 — confirmar versao vigente antes de usar este checklist (PA-02).

---

## 2. ONDE REGISTRAR — COMPETENCIA REGISTRAL

| Tipo societario | Orgao de registro | Base legal |
|----------------|------------------|-----------|
| LTDA | Junta Comercial do estado da sede | CC 1.150; Lei 8.934/1994 |
| SLU | Junta Comercial do estado da sede | CC 1.052 §§1-2; Lei 8.934/1994 |
| S/A fechada e aberta | Junta Comercial do estado da sede | Lei 8.934/1994 |
| SAS | Junta Comercial do estado da sede | LC 182/2021 |
| SCP | RCPJ para CNPJ fiscal; contrato interno nao e arquivado na Junta | CC 991-996; IN RFB [VERIFICAR] |
| Sociedade Simples | RCPJ (Registro Civil de Pessoas Juridicas) | CC 998; nao e empresaria, nao vai a Junta |
| Sociedade Simples com forma de S/A ou LTDA | Junta Comercial | CC 983, §unico [VERIFICAR] |

> **PA-15** — nunca omitir o registro: a personalidade juridica da LTDA/S/A/SAS somente se adquire com o arquivamento do ato constitutivo na Junta Comercial (CC 985; Lei 8.934/1994).

---

## 3. CHECKLIST — CONSTITUICAO (LTDA/SLU)

Documentos exigidos pelo DREI (IN 81/2020 e atualizacoes — [VERIFICAR versao vigente]):

```
[ ] Requerimento de arquivamento assinado pelo administrador (FCN — Formulario de Cadastro Nacional)
[ ] Contrato social original (3 vias assinadas, conforme Junta estadual — verificar exigencia local)
[ ] Reconhecimento de firma ou assinatura digital ICP-Brasil dos socios e testemunhas
[ ] Copia autenticada dos documentos de identidade e CPF de todos os socios
[ ] Comprovante de residencia dos socios (alguns estados exigem)
[ ] Comprovante da sede social (contrato de locacao / escritura / declaracao de uso)
[ ] CNPJ (solicitado simultaneamente via integrador DBE/REDESIM ou CNPJ.gov.br)
[ ] Autorizacao previa do orgao regulador, se atividade regulada (BACEN, ANVISA, OAB, CVM)
[ ] Taxa de arquivamento (verificar tabela vigente da Junta estadual)
[ ] Licenca de funcionamento (Alvara — municipal — geralmente pos-registro)
```

### 3.1 EIRELI x SLU — transicao

EIRELI extinta pela Lei 14.195/2021: arquivos de EIRELI existentes foram automaticamente convertidos em SLU. Novo pedido deve ser SLU.

---

## 4. CHECKLIST — CONSTITUICAO (S/A FECHADA E SAS)

```
[ ] Requerimento de arquivamento (FCN)
[ ] Estatuto social (3 vias) — S/A: assinado por todos os fundadores; SAS: idem
[ ] Ata de assembleia de constituicao (ou instrumento particular de constituicao assinado por todos os acionistas — LSA art. 88 [VERIFICAR])
[ ] Lista de presenca da assembleia de constituicao
[ ] Laudo de avaliacao (se integralizacao em bens — por peritos ou empresa especializada, nomeados em assembleia: LSA art. 8o)
[ ] Comprovante de deposito bancario (integralizacao inicial em dinheiro — 10% do capital subscrito — LSA art. 80, II [VERIFICAR percentual vigente])
[ ] Qualificacao e aceite dos primeiros administradores (diretores e conselheiros, se houver)
[ ] Autorizacao previa do orgao regulador, se necessaria
[ ] Publicacao de edital de convocacao (se fundadores publicos) ou dispensa (SAS)
[ ] Taxa de arquivamento da Junta
[ ] Registro CVM (somente S/A aberta)
```

---

## 5. CHECKLIST — ALTERACAO CONTRATUAL (LTDA/SLU)

```
[ ] Instrumento de alteracao contratual com clausulas alteradas (versao consolidada ou so alteracoes)
[ ] Assinaturas: socios presentes (quorum CC 1.076 — maioria, pos-Lei 14.451/2022) + administrador
[ ] Reconhecimento de firma ou assinatura digital ICP-Brasil
[ ] Ata de reuniao de socios (se deliberacao em reuniao formal) ou instrumento de deliberacao escrita
[ ] Documentos do novo administrador ou novo socio (se houver alteracao subjetiva)
[ ] Comprovante de integralizacao (se aumento de capital em dinheiro) ou laudo (bens)
[ ] Publicacao previa (somente reducao de capital — CC 1.082: 60 dias para oposicao de credores)
[ ] Requerimento de arquivamento
[ ] Taxa da Junta
```

---

## 6. CHECKLIST — ARQUIVAMENTO DE ATA (S/A)

```
[ ] Ata de assembleia geral ordinaria ou extraordinaria
[ ] Lista de presenca de acionistas
[ ] Publicacao previa de convocacao (S/A fechada: jornal + DO ou dispensa unanimidade — S/A com ate 20 acionistas art. 294 LSA [VERIFICAR]; SAS: dispensada)
[ ] Procuracoes de acionistas representados
[ ] Requerimento de arquivamento assinado pelo secretario da mesa
[ ] Taxas da Junta
[ ] Publicacao pos-arquivamento (S/A fechada: DO e jornal; SAS: dispensada)
```

---

## 7. PRAZOS DE ARQUIVAMENTO

| Ato | Prazo | Base legal |
|-----|-------|-----------|
| Ato constitutivo (LTDA/SLU/S/A/SAS) | Arquivar em ate 30 dias da assinatura para efeitos a partir da data do ato; apos 30 dias, a eficacia perante terceiros data do arquivamento | CC 1.151, §2o; Lei 8.934/1994, art. 36 |
| Alteracoes contratuais e atas | Prazo recomendado: 30 dias da deliberacao; sem prazo fatal na lei federal para LTDA (verificar legislacao estadual) | Lei 8.934/1994, art. 36 [VERIFICAR] |
| Ata de AGO (S/A) | Publicar e arquivar no prazo de 1 mes da realizacao | LSA art. 133, §3o [VERIFICAR] |
| Nomeacao de administrador | Arquivar antes de exercer o cargo (prazo recomendado: 30 dias) | CC 1.062 |

> **PA-03 (adaptado):** nunca cravar prazo de arquivamento sem verificar a legislacao estadual da Junta correspondente — algumas Juntas tem prazos ou exigencias adicionais.

---

## 8. AVERBACAO DE ACORDO DE SOCIOS/ACIONISTAS

### 8.1 LTDA

O CC nao preve forma especifica para acordo de socios, mas a doutrina e a IN DREI admitem a averbacao. Procedimento: protocolar instrumento de acordo (assinado e com reconhecimento de firma) na Junta, requerendo averbacao na ficha da empresa. Efeito: oponibilidade perante terceiros.

### 8.2 S/A (art. 118 LSA)

O acordo de acionistas deve ser arquivado na sede da companhia e averbado nos livros de registro de acoes. Para oponibilidade a terceiros: arquivamento na Junta Comercial.

Requisitos para oponibilidade (LSA art. 118, §§):
- Arquivado na sede da companhia;
- Averbado nos livros de registro (acoes nominativas);
- A companhia so executa a transferencia ou o exercicio do direito de voto conforme o acordo.

### 8.3 Conteudo do protocolo de averbacao

```
[ ] Requerimento de averbacao (identificando a empresa, NIRE, ato a averbar)
[ ] Via original ou copia autenticada do acordo de socios/acionistas
[ ] Reconhecimento de firma ou assinatura digital
[ ] Taxa de averbacao da Junta
[ ] Declaracao de enquadramento (se LTDA nao obrigada a publicacao)
```

---

## 9. REJEICAO NA JUNTA — CAUSAS FREQUENTES

| Causa | Prevencao |
|-------|----------|
| Reconhecimento de firma ausente ou ilegivel | Exigir ICP-Brasil ou cartorio antes de protocolar |
| Objeto social com atividade regulada sem autorizacao previa | Verificar CNAE e orgao regulador antes de redigir o contrato |
| Quorum incorreto na ata (ex.: citar quorum de 3/4 revogado) | Usar tabela de quoruns desta skill — PA-13 |
| Endereco de sede incompleto ou sem comprovante | Incluir CEP, numero e complemento; anexar comprovante |
| Socio sem CPF regularizado na Receita Federal | Verificar situacao cadastral antes |
| Capital nao integralizado sem prazo/forma descrita | Incluir clausula de integralizacao no contrato |
| Denominacao igual ou semelhante a empresa ja registrada | Pesquisar na Junta estadual e no SISBACEN antes de protocolar |

---

## 10. SISTEMA INTEGRADO — REDESIM / CNPJ.GOV.BR

Desde a Lei 14.195/2021 e Dec. 10.278/2020, o registro empresarial foi simplificado:
- Integracao Junta + Receita Federal (CNPJ) + Previdencia Social via portal unico.
- Abertura em ate 1 dia util em estados com integracao plena [VERIFICAR estado da sede].
- Dispensa de reconhecimento de firma para documentos com assinatura digital ICP-Brasil.

---

## 11. VEDACOES ESPECIFICAS

- **PA-15** — toda constituicao, alteracao ou dissolucao societaria que produza efeitos perante terceiros exige arquivamento na Junta Comercial (LTDA/S/A/SAS) ou RCPJ (Sociedade Simples). Nunca omitir.
- **PA-13** — nao citar quorum de 3/4 em atos de LTDA. Validar quorum pela Lei 14.451/2022.
- **PA-02** — a IN DREI e periodicamente atualizada. Verificar versao vigente no DREI (drei.gov.br) antes de cada arquivamento.
- **PA-22** — todo roteiro e sujeito a revisao pelo advogado responsavel.

---

## 12. PROTOCOLOS ACIONADOS

- **Protocolo 1** (Validacao Legal Previa) — confirmar IN DREI vigente e exigencias locais da Junta estadual.
- **Protocolo 4** (Competencia) — LTDA/S/A/SAS: Junta Comercial. Sociedade Simples: RCPJ. SCP: nao arquiva contrato na Junta.

---

## 13. INTEGRACAO

**Chamada por:** `constituicao-societaria`, `alteracoes-e-atos-societarios`, `reorganizacao-societaria`, `dissolucao-e-saida-de-socio`, `governanca-e-acordos`.

**Entrega para:** operador (checklist finalizado para protocolo na Junta/RCPJ).

**Sem esta skill:** atos societarios lavrados sem registro nao produzem efeitos perante terceiros — risco de invalidade de atos praticados pelo administrador antes do arquivamento.
