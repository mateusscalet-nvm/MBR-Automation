# Doc Construction — MBR SMB

**Specification canônica de como o relatório MBR é montado.** Define a ordem dos blocos, os artefatos visuais (charts e tabelas) e a estrutura textual de cada seção, para BR / AR / MX.

- **Escopo:** SMB · BR, AR, MX
- **Comprimento-alvo:** 1-2 páginas executivas (TL;DR + Main KPIs) + 3-5 páginas de seções de negócio + BACK-UP
- **Fonte de KPIs:** `KPI_CATALOG.md` (toda referência a um KPI usa o nome canônico do catálogo)
- **Regras textuais:** `ANALYSIS_RULES.md`
- **Última atualização:** 2026-06-02
- **Owner:** Marketing Ops

---

## 0. Convenções

### 0.1 Estrutura geral do documento

```
1. TL;DR
2. Main KPIs
3. Brand & Comms
4. Acquisition
5. Lifecycle
6. BACK-UP
```

Cada seção de negócio (B&C, Acquisition, Lifecycle) segue o mesmo padrão interno:

```
SEÇÃO
├── Bloco 1 — Charts (2×2 grid)
├── Bloco 2 — Tables (sumário do período)
└── Bloco 3 — Análise textual (Results / Gap & Hypothesis / Moving Forward)
```

### 0.2 Página e tipografia

- **Página:** A4, margens 1,5 cm, retrato
- **Fonte de texto:** Arial (corpo, headings)
- **Fonte de tabela e chart:** Roboto
- **Tamanhos:** 16pt título do doc · 13pt seção · 10pt corpo · 9pt células de tabela

Tokens completos em `config/design.py`.

### 0.3 Cores (Nuvemshop Insti Styleguide)

- **Brand:** `#0050C3` (header de tabela, títulos de seção)
- **Brand Dark:** `#171E43` (headings)
- **Linhas alternadas:** `#F5FAFF`
- **Bordas:** `#E7E8E9`
- **Condicional MoM/YoY:** verde `#0CA76B` (positivo), amarelo `#9A7000` (neutro), vermelho `#CC3333` (negativo)

### 0.4 Chart specs (padrão)

| Atributo | Valor |
|---|---|
| **Janela histórica** | 24 meses terminando no mês de referência |
| **Tamanho half-width** | 8.1 cm × 7.5 cm (para grid 2×2) |
| **Tamanho full-width** | 17 cm × 7.5 cm |
| **DPI** | 150 |
| **Eixo X** | Labels mensais (`%b '%y`) com ano apenas na primeira ocorrência |
| **Eixo Y** | Formatação `K`/`M` para grandes números, `%` para ratios |
| **Mês de referência** | Destacado (cor mais forte, anotação de valor) |
| **Grid Y** | Linhas sutis cinza `#E7E8E9`, sem grid X |
| **Spines** | Apenas linha inferior visível |

### 0.5 Table specs (padrão)

| Atributo | Valor |
|---|---|
| **Header** | Fundo `#0050C3`, texto branco bold |
| **Linhas alternadas** | Branco / `#F5FAFF` |
| **Linha "Total"** | Fundo `#F3F3F3` (destaque) |
| **Borda final** | 1pt cinza separador |
| **Colunas-padrão** | Metric · Real · M-1 · MoM% · (YoY% ou Plan/Attainment%) |
| **Padding vertical** | 2pt |
| **Coloração condicional** | MoM% e YoY% com cor da fonte (verde/amarelo/vermelho) |

### 0.6 Composição de chart grid 2×2

Implementada via tabela Word invisível (2 colunas × N linhas, sem bordas). Cada célula contém uma imagem PNG do matplotlib. Padrão por seção de negócio:

```
+----------------+----------------+
| Chart 1        | Chart 2        |
+----------------+----------------+
| Chart 3        | Chart 4        |
+----------------+----------------+
```

### 0.7 Comparações temporais

- **Real:** mês de referência (`MONTH_LABEL`)
- **M-1:** mês anterior (`PRIOR_MONTH_LABEL`)
- **YoY:** mesmo mês do ano anterior (`PRIOR_YEAR_MONTH_LABEL`)
- **Plan / Attainment%:** apenas para KPIs com `expected_monthly_*` (ver catálogo)
- **YTD:** Jan até mês de referência
- **Quarter:** trimestre corrente até mês de referência

---

## 1. TL;DR

Seção executiva no topo. Foco em narrativa, sem charts ou tabelas próprias.

### Estrutura

```
1.1 Executive Summary               — síntese de 3-4 frases. "Defining Theme" do mês
1.2 The Funnel Narrative            — Traffic → Acquisition Quality
1.3 Base Health & Retention         — Net Adds → Churn breakdown (Seller vs Non-Seller)
1.4 Business & Financial Impact     — GMV (Local + USD), Transactions, GMV per Seller
1.5 Critical Discussion Topics      — top 3 bottlenecks que pedem atenção da liderança
1.6 Prioritized Action Plan         — Immediate Fixes (30 dias) + Strategic Bets (Q+1)
```

### Regras

- Cada subseção: 2-5 frases máximo
- Todo número citado deve ter "**because**" (regra de causalidade — ver `ANALYSIS_RULES.md`)
- Terminologia: Phoenix, Branded Levers, ICP 1/2, Seller vs Non-Seller, "softness"/"gap" para misses
- Idioma: **English**
- Geração: **Claude API runtime** (recebe Main KPIs + sumários de cada seção de negócio + regras)

### Inputs do gerador

- Outputs estruturados das seções 3, 4, 5 (Results de cada uma)
- KPIs principais já calculados (Main KPIs)
- Mês de referência e comparações temporais

> **Status do projeto:** TL;DR é o último módulo a ser construído. Por enquanto, ignorado.

---

## 2. Main KPIs

Bloco logo após o TL;DR, com a visão consolidada do funil + base.

### Bloco 2.1 — Tabela "Main KPIs"

Tabela única horizontal com os indicadores macro.

| Coluna | Conteúdo |
|---|---|
| Metric | Nome do KPI (referência ao catálogo) |
| Real | Valor mês de referência |
| Plan | `expected_monthly_*` (quando aplicável) |
| Attainment% | `Real / Plan` |
| M-1 | Valor mês anterior |
| MoM% | (Real − M-1) / M-1 |
| YoY | Mesmo mês ano anterior |
| YoY% | (Real − YoY) / YoY |

**KPIs incluídos** (na ordem, do topo do funil ao impacto financeiro):

1. Branded Searches
2. Sessions
3. Trials
4. CVR Session → Trial
5. New Payments
6. CVR Trial → NP
7. Net Adds 🟡
8. Merchant Base 🟡
9. GMV (USD) 🟡
10. Transactions / Orders 🟡
11. % Seller ⚠️
12. GMV per Seller ⚠️

🟡 = placeholder · ⚠️ = bloqueado (vide catálogo)

### Bloco 2.2 — Charts complementares (4 charts, 2×2)

Histórico de 24 meses para os KPIs mais relevantes do funil:

```
+---------------------------+---------------------------+
| Chart 1 — Trials          | Chart 2 — New Payments    |
| (bars + plan line)        | (bars + plan line)        |
+---------------------------+---------------------------+
| Chart 3 — Net Adds        | Chart 4 — Merchant Base   |
| (bars +/- coloridos)      | (line + area fill)        |
+---------------------------+---------------------------+
```

**Status do projeto:** módulos A (tabela) e B (charts) já implementados, **alinhar com este spec na refatoração final**.

---

## 3. Brand & Comms

### 3.1 Macro Results

#### Bloco 3.1.1 — Charts (2×2)

```
+---------------------------+---------------------------+
| Branded Searches #        | Branded CTR %             |
| (bars, 24m, ref destacado)| (bars, 24m, ref destacado)|
+---------------------------+---------------------------+
| Total Market Search Vol   | Share of Market           |
| (bars + lines branded/    | (line, real + plan dotted)|
|  non-branded)             |                           |
+---------------------------+---------------------------+
```

#### Bloco 3.1.2 — Tabela "B&C Macro"

| Metric | Real | M-1 | MoM% | Plan | Attainment% |
|---|---|---|---|---|---|
| Branded Searches # | … | … | … | … | … |
| Branded CTR % | … | … | … | — | — |
| Share of Market | … | … | … | … | … |
| Total Market Search Volume | … | … | … | — | — |

#### Bloco 3.1.3 — Análise (Results / Gap & Hypothesis / Moving Forward)

Texto gerado pela LLM. Ver `ANALYSIS_RULES.md`.

- **Results** — 2-3 frases objetivas. Cada número com seu "because"
- **Gap & Hypothesis** — onde houve softness/gap e qual a hipótese principal (1-3 bullets)
- **Moving Forward** — ações concretas para o próximo mês (1-3 bullets)

### 3.2 PR

#### Bloco 3.2.1 — Tabela "PR — Publications by Tier"

| Tier | Real | M-1 | MoM% |
|---|---|---|---|
| Gold | … | … | … |
| Tier 1 | … | … | … |
| Tier 2 | … | … | … |
| **Total** | … | … | … |

Linha "Total" em destaque (bold, fundo cinza).

#### Bloco 3.2.2 — KPIs adicionais (mini-tabela ou inline)

- Proactive Publications
- Total Reach (PR)
- Plan vs Real (Total Publications, Tier 1) com attainment%

#### Bloco 3.2.3 — Análise (Results / Gap & Hypothesis / Moving Forward)

Foco: hit rate da meta, mix Gold/Tier 1/Tier 2, reach, qualidade vs quantidade.

### 3.3 Social

#### Bloco 3.3.1 — Tabela "Social — Instagram"

| Metric | Real | M-1 | MoM% |
|---|---|---|---|
| Total Reach | … | … | … |
| Organic Reach | … | … | … |
| Paid Reach | … | … | … |
| Collab Reach | … | … | … |
| Net Followers | … | … | … |
| Profile Followers | … | … | … |
| Engagement Rate | … | … | … |
| Interactions | … | … | … |

#### Bloco 3.3.2 — Análise (Results / Gap & Hypothesis / Moving Forward)

Foco: mix de reach (orgânico vs pago vs collab), engagement rate vs plano, crescimento de followers.

> **Status do projeto:** módulo C implementado parcialmente. Falta dividir em 3.1 / 3.2 / 3.3 e adotar template Results/Gap/Moving Forward.

---

## 4. Acquisition

### 4.1 Macro Results

#### Bloco 4.1.1 — Charts (2×2)

```
+---------------------------+---------------------------+
| Sessions                  | Trials                    |
| (bars, 24m)               | (bars + plan line)        |
+---------------------------+---------------------------+
| New Payments              | CVR Trial → NP            |
| (bars + plan line)        | (line, 24m)               |
+---------------------------+---------------------------+
```

#### Bloco 4.1.2 — Tabela "Acquisition Macro"

| Metric | Real | Plan | Attainment% | M-1 | MoM% | YoY% |
|---|---|---|---|---|---|---|
| Sessions | … | — | — | … | … | … |
| Trials | … | … | … | … | … | … |
| New Payments | … | … | … | … | … | … |
| QLs | … | … | … | … | … | … |
| CVR Session → Trial | … | — | — | … | … | … |
| CVR Trial → NP | … | — | — | … | … | … |
| CAC ⚠️ | — | — | — | — | — | — |

#### Bloco 4.1.3 — Análise (Results / Gap & Hypothesis / Moving Forward)

Foco: onde o funil quebrou (topo vs meio vs fundo), qualidade vs quantidade de leads, sazonalidade.

### 4.2 Brand Levers

**Sources:** Performance Brand, Organic, Direct.

#### Bloco 4.2.1 — Tabela "Brand Levers — by Source"

Estrutura 2-dimensional (lever × KPI):

| Lever | Sessions | Trials | NPs | CVR T→NP | NP Attainment% |
|---|---|---|---|---|---|
| Performance Brand | … | … | … | … | … |
| Organic | … | … | … | … | … |
| Direct | … | … | … | … | … |
| **Brand Total** | … | … | … | … | … |

#### Bloco 4.2.2 — Charts (opcional, 1-2)

- Stacked bar: NPs por lever (24 meses)
- Line: CVR Trial→NP por lever

#### Bloco 4.2.3 — Análise (Results / Gap & Hypothesis / Moving Forward)

### 4.3 Non-Brand Levers

**Sources:** Performance Non-Branded, Affiliates, Partners, Organic Growth, Others.

#### Bloco 4.3.1 — Tabela "Non-Brand Levers — by Source"

Mesma estrutura da 4.2.1, com as 5 sources Non-Brand + linha total.

#### Bloco 4.3.2 — Charts (opcional, 1-2)

#### Bloco 4.3.3 — Análise (Results / Gap & Hypothesis / Moving Forward)

> **Status do projeto:** seção Acquisition ainda não construída.

---

## 5. Lifecycle 🟡

Todos os blocos usam **CSV placeholder** até DP5 estar disponível.

### 5.1 Merchant Base & Net Adds

#### Bloco 5.1.1 — Charts (2×2)

```
+---------------------------+---------------------------+
| Merchant Base             | Net Adds                  |
| (line, 24m, area fill)    | (bars, 24m, +/- colored)  |
+---------------------------+---------------------------+
| Inflow Components         | Outflow Components        |
| (stacked: FP + New        | (stacked: Churns +        |
|  Phoenix + Old Phoenix)   |  Downsell)                |
+---------------------------+---------------------------+
```

#### Bloco 5.1.2 — Tabela "Lifecycle Summary"

| Metric | Real | M-1 | MoM% | YoY% |
|---|---|---|---|---|
| **Net Adds** | … | … | … | … |
| First Payments | … | … | … | … |
| Churn + Downgrade | … | … | … | … |
| **Merchant Base (EOP)** | … | … | … | … |

Linhas "Net Adds" e "Merchant Base" em destaque (bold).

### 5.2 Net Adds Components

Tabela de decomposição do Net Adds em inflow e outflow.

#### Bloco 5.2.1 — Tabela "Net Adds Decomposition"

| Component | Real | M-1 | MoM% |
|---|---|---|---|
| First Payments | … | … | … |
| New Phoenix | … | … | … |
| Old Phoenix | … | … | … |
| **Total Inflow** | … | … | … |
| Churns | … | … | … |
| Downsell to Freemium | … | … | … |
| **Total Outflow** | … | … | … |
| Ajuste | … | … | … |
| **Net Adds** | … | … | … |

### 5.3 Churn Breakdown

#### Bloco 5.3.1 — Tabela "Churn"

| Segment | Real | M-1 | MoM% |
|---|---|---|---|
| Churn Rate | … | … | … |
| Churns absolute | … | … | … |
| Downsell to Freemium | … | … | … |
| Net Adds Quality (% Seller no NA) ⚠️ | — | — | — |

### 5.4 Análise (Results / Gap & Hypothesis / Moving Forward)

Foco: balanço inflow vs outflow, where the leak is happening (Seller vs Non-Seller), Phoenix performance, sazonalidade de churn.

> **Status do projeto:** módulo D implementado com CSV placeholder. Estrutura precisa adequação às 4 subseções (5.1 / 5.2 / 5.3 / 5.4) e ao template Results/Gap/Moving Forward.

---

## 6. BACK-UP

Apêndice ao final do documento com tabelas e charts detalhados, organizados por seção de negócio. Não é narrativa — é referência consultiva.

### Estrutura

```
6.1 B&C Back-up
    - Tabela detalhada de PR por meio/origem
    - Tabela detalhada de Social com plan e attainment%
    - Histórico 24m por KPI (charts adicionais)

6.2 Acquisition Back-up
    - Tabela detalhada de Brand Levers com plan, attainment% e CAC (quando disponível)
    - Tabela detalhada de Non-Brand Levers
    - Charts complementares por source

6.3 Lifecycle Back-up
    - Tabela detalhada de Net Adds por source (quando DP5 estiver pronto)
    - Histórico 24m de cada componente do Net Adds
    - Churn breakdown por segmento (Seller vs Non-Seller — bloqueado)
```

### Regras

- Sem texto analítico (já está nas seções principais)
- Pode usar tabelas full-width
- Charts podem ser full-width (não precisa do grid 2×2)

> **Status do projeto:** ainda não construído.

---

## 7. Convenções de orquestração

### 7.1 Ordem de geração

A geração do documento segue a ordem:

```
1. Fetch de dados (fetcher genérico baseado no catálogo)
2. Cálculo de comparações temporais (M-1, YoY, Plan, Attainment%)
3. Renderização: Main KPIs → B&C → Acquisition → Lifecycle → BACK-UP
4. Geração de análises textuais (Claude API) por seção
5. Geração do TL;DR (recebe outputs das seções)
6. Composição final do .docx
```

### 7.2 Entrada do gerador

```python
data = {
    "meta": {
        "month_label": "2026-03",
        "country": "BR",
        "business_unit": "SMB",
        "prior_month_label": "2026-02",
        "prior_year_month_label": "2025-03",
    },
    "main_kpis": { ... },         # KPIs calculados
    "brand_comms": { ... },       # estruturado por subseção
    "acquisition": { ... },
    "lifecycle": { ... },
    "analyses": {                 # gerado pela LLM
        "brand_comms": { results, gap, moving_forward },
        "acquisition": { ... },
        "lifecycle": { ... },
        "tldr": { ... },
    },
}
```

### 7.3 Saída

Arquivo `.docx` em `output/MBR_<COUNTRY>_<MONTH_LABEL>.docx`.

---

## 8. Changelog

- **2026-06-02** — Versão inicial. Define a estrutura canônica do MBR com 6 seções e o padrão Charts/Tables/Analysis para cada seção de negócio. Padrão Results/Gap/Moving Forward unificado.
