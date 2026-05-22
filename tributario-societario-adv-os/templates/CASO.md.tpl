# CASO — {{CLIENTE}} x {{ADVERSO}}

> Ficha do caso empresarial. Fonte única da variável de **polo** — todas as
> skills leem os campos `Modo` e `Domínio` daqui. Vive em
> `<COWORK>/tributario-societario/casos/{{CASO_SLUG}}/CASO.md`.

---

## Modo e partes

- **Modo:** {{MODO}}
  <!-- consultivo | contencioso -->
- **Domínio:** {{DOMINIO}}
  <!-- tributario | societario | ambos -->
- **Parte atendida (cliente):** {{CLIENTE}}
- **Parte adversa:** {{ADVERSO}}
- **Órgão / Instância:** {{ORGAO}}
  <!-- CARF | TIT | Vara Federal | Vara Estadual | Junta Comercial | consultivo (sem processo) -->
- **Nº do processo:** {{NUMERO}}
- **Fase processual:** {{FASE}}
  <!-- pre-processual | impugnacao administrativa | recurso voluntario | recurso especial CSRF | execucao fiscal | judicial 1o grau | recursal | consultivo -->
- **Tipo de tarefa:** {{TAREFA}}

---

## Dados do caso

- **Tipo societário / regime tributário:** {{TIPO_ENTIDADE}}
- **Fato gerador / data-base:** {{FATO_GERADOR}}
- **Tributo(s) envolvido(s):** {{TRIBUTOS}}
- **Competência (federal/estadual/municipal):** {{COMPETENCIA}}
- **Exercício / ano-calendário:** {{ANO_EXERCICIO}}

---

## Marco intertemporal

- **Ano / data do fato gerador:** {{FATO_GERADOR_DATA}}
  <!-- Data ou exercício do fato gerador que origina o caso. Determina qual regime tributário se aplica. -->
- **Regime tributário aplicável (EC 132/2023 + LC 214/2025):** {{REGIME_TRIBUTARIO_MARCO}}
  <!-- Regimes possíveis:
       ANTES DA REFORMA — fato gerador até 31/12/2025 (PIS/COFINS vigentes, sem CBS/IBS)
       ANO-TESTE 2026  — fase experimental CBS/IBS (PIS/COFINS ainda em vigor concomitante)
       2027+           — CBS em vigor, PIS/COFINS extintos; IBS em implantação progressiva (até 2033)
       TRANSIÇÃO 2027-2033 — alíquotas reduzidas de CBS/IBS + extinção gradual PIS-COFINS/ISS/ICMS
  -->

> Protocolo 6 — *tempus regit actum*. O regime tributário vigente no **ano do fato gerador**
> é o aplicável. Fatos geradores anteriores a 2026 não são alcançados pela CBS/IBS (LC 214/2025).
> Travar o cronograma da Reforma Tributária antes de qualquer estratégia de planejamento (PA-02/PA-06).

---

## Prescrição e Decadência

- **Prazo decadencial (art. 150 §4º / art. 173 CTN):** {{PRAZO_DECADENCIAL}}
- **Prescrição (art. 174 CTN):** {{PRAZO_PRESCRICIONAL}}

> PA-03: nunca cravar prazo como definitivo sem ressalva — verificar interrupções/suspensões.

---

## Linha estratégica

{{LINHA_ESTRATEGICA}}

<!-- Preenchida pela linha-estrategica-empresarial após o Checkpoint 4:
     tese central, teses subsidiárias, riscos. -->

---

## Prazos

| Prazo | Termo inicial | Vencimento | Observação |
|-------|---------------|------------|------------|
| {{PRAZO_TIPO}} | {{PRAZO_INICIO}} | {{PRAZO_FIM}} | {{PRAZO_OBS}} |

<!-- Impugnação CARF = 30 dias; Recurso Voluntário CARF = 30 dias;
     Embargos Execução Fiscal = 30 dias; MS = 120 dias. Sempre verificar portaria/edital. -->

---

## Documentos do caso

{{DOCUMENTOS}}

<!-- Lista dos documentos em casos/{{CASO_SLUG}}/documentos/ —
     auto de infração, CDA, decisão administrativa, contrato social, ata, DCTF/SPED, laudos, contratos. -->

---

**Plugin:** `tributario-societario-adv-os` v{{PLUGIN_VERSION}}
**Caso aberto em:** {{GENERATED_AT}}
