# Doc Construction — MBR

**Canonical specification of how the MBR report is assembled.** Defines section order, visual artifacts (charts and tables), recurring table templates, and the textual structure of each block.

- **Scope:** SMB · single file parameterized by `country` (BR, AR, MX)
- **Cadence:** monthly MBR *(QBR out of scope for now)*
- **KPI source:** `KPI_CATALOG.md` v2 — every KPI reference uses the catalog's canonical name; definitions and formulas live there, not here
- **Writing rules:** `ANALYSIS_RULES.md` *(to be created)*
- **Language:** English (machine-consumed; report output is in English)
- **Last updated:** 2026-06-02
- **Owner:** Marketing Ops

---

## 0. Conventions

### 0.1 Overall document structure

```
1. TL;DR
2. Main KPIs
3. Brand & Comms
4. Acquisition
5. Company Metrics
6. Financial
7. BACK-UP
```

Each business section (B&C, Acquisition, Company Metrics, Financial) follows the same internal 3-block pattern:

```
SECTION
├── Block 1 — Charts (2×2 grid)
├── Block 2 — Tables (period summary)
└── Block 3 — Textual analysis (Results / Gap & Hypothesis / Moving Forward)
```

### 0.2 Country parameterization

The document is **single**, generated per country via the `country` parameter. All KPIs, filters, and comparisons respect the current country. No structure changes across BR/AR/MX — only the data. Baseline exceptions (e.g., Share of Market) are already handled in the data itself (see catalog §2.1).

Base filter for the whole report: `country = <param>` AND `business_unit = 'SMB'`.

### 0.3 Page and typography

- **Page:** A4, 1.5 cm margins, portrait
- **Text font:** Arial (body, headings)
- **Table and chart font:** Roboto
- **Sizes:** 16pt document title · 13pt section · 10pt body · 9pt table cells

### 0.4 Colors (Nuvemshop Insti Styleguide)

- **Brand:** `#0050C3` (table header, section titles)
- **Brand Dark:** `#171E43` (headings)
- **Alternating rows:** `#F5FAFF`
- **Borders:** `#E7E8E9`
- **Conditional MoM/YoY/Attainment:** green `#0CA76B` (positive), amber `#9A7000` (neutral), red `#CC3333` (negative)

### 0.5 Chart specs (default)

| Attribute | Value |
|---|---|
| **Historical window** | 24 months ending in the reference month |
| **Half-width size** | 8.1 cm × 7.5 cm (for 2×2 grid) |
| **Full-width size** | 17 cm × 7.5 cm |
| **DPI** | 150 |
| **X axis** | Monthly labels (`%b '%y`) with year only on first occurrence |
| **Y axis** | `K`/`M` formatting for large numbers, `%` for ratios |
| **Reference month** | Highlighted (stronger color, value annotation) |
| **Y grid** | Subtle gray lines `#E7E8E9`, no X grid |
| **Spines** | Bottom line only |

### 0.6 Table specs (default)

| Attribute | Value |
|---|---|
| **Header** | `#0050C3` fill, white bold text |
| **Alternating rows** | White / `#F5FAFF` |
| **"Total" row** | `#F3F3F3` fill (highlight, bold) |
| **Final border** | 1pt gray separator |
| **Vertical padding** | 2pt |
| **Conditional coloring** | MoM% / YoY% / Attainment% as font color (green/amber/red) |

### 0.7 2×2 chart grid composition

Grid of 4 charts via an invisible table (2 columns × 2 rows, no borders), each cell holding a PNG image:

```
+----------------+----------------+
| Chart 1        | Chart 2        |
+----------------+----------------+
| Chart 3        | Chart 4        |
+----------------+----------------+
```

### 0.8 Temporal comparisons

- **Real:** reference month
- **M-1 / MoM%:** prior month and variation
- **YoY / YoY%:** same month previous year and variation
- **Plan / Attainment%:** only for KPIs with `expected_monthly_*` (see catalog)
- **YTD:** Jan through reference month
- **Forecast:** when the KPI has `forecast_*`

### 0.9 Data source

The MBR runs over **closed months**, therefore it consumes the data products' **monthly snapshots** (`*__agg_snapshot_monthly` — see catalog §0.1 and §3.1) whenever available. For the 24-month historical charts, the daily/snapshot variant is used depending on the KPI. Placeholder KPIs (Company Metrics) use CSV until DP5; GMV uses DP4.

### 0.10 Standard breakdowns (drill-down dimensions)

**By `mkt_source`** (4-level hierarchy — see catalog §3.4):
- **Level 4 (Branded / Non-Branded)** → subsection grouper in Acquisition
- **Level 2 (9 sources, incl. Misc Sources)** → rows within each group

**By `icp`** (see catalog §2.10) → additional drill-down of funnel KPIs in Acquisition. ⚠️ Depends on external classification source (backlog B12).

**By `country`** → the entire document (global parameter).

---

## Canonical table templates

Recurring tabular structures across the MBRs. Each section references the applicable template instead of redefining columns.

### T1 — Performance vs Budget

The flagship table for any KPI with a plan.

| KPI | Real | Plan | %Achv | YoY | YTD | %Achv YTD | YoY YTD |
|---|---|---|---|---|---|---|---|

### T2 — Performance Month-over-Month

| KPI | Real | M-1 | MoM% | YoY | YoY% |
|---|---|---|---|---|---|

### T3 — Breakdown by Source (Acquisition)

Grouped by Level 4 (Branded / Non-Branded), rows in Level 2:

| Source | Trials | NPs | NSs | CVR T→NP | NP Attainment% |
|---|---|---|---|---|---|
| **Branded** *(subtotal)* | | | | | |
| ↳ Performance Brand | | | | | |
| ↳ Organic | | | | | |
| ↳ Direct | | | | | |
| **Non-Branded** *(subtotal)* | | | | | |
| ↳ Performance No Brand | | | | | |
| ↳ Affiliates | | | | | |
| ↳ Partners | | | | | |
| ↳ Organic Growth | | | | | |
| ↳ Nurturing | | | | | |
| ↳ Misc Sources | | | | | |
| **Total** | | | | | |

### T4 — Breakdown by ICP (Acquisition)

| KPI | ICP 1 | ICP 2 | ICP 3 | ICP 4 | ICP 5a | ICP 5b |
|---|---|---|---|---|---|---|
| Trials | | | | | | |
| NPs | | | | | | |
| CVR Trial→NP | | | | | | |

⚠️ Source-blocked (catalog B12). Include only once ICP classification is available.

### T5 — Acquisition × Activation funnel

End-to-end funnel view in a single row:

| Stage | Branded Searches | → Trials | → NPs | → NSs |
|---|---|---|---|---|
| Volume | | | | |
| CVR (vs prior stage) | — | | | |

---

## 1. TL;DR

Executive section at the top. Pure narrative, no own charts or tables. **Generated last** in the orchestration (consumes the Results of all business sections), but **positioned first** in the document.

### Structure

```
1.1 Executive Summary          — 3-4 sentence synthesis + month's "Defining Theme"
1.2 The Funnel Narrative       — Demand/Branded Searches → Acquisition → CVRs
1.3 Base Health & Retention    — Net Adds → Churn (Seller vs Non-Seller)
1.4 Business & Financial Impact — GMV (local currency + USD), Orders, GMV per Seller
1.5 Critical Discussion Topics — top 3 bottlenecks for leadership
1.6 Prioritized Action Plan    — Immediate Fixes (30d) + Strategic Bets (Q+1)
```

### Rules

- Each subsection: 2-5 sentences
- Mandatory causality (every number with a "because") — see `ANALYSIS_RULES.md`
- Canonical terminology: Phoenix, Branded/Non-Branded Levers, ICP, Seller vs Non-Seller, "softness"/"gap" for misses
- Language: English
- Generation: LLM (receives Main KPIs + each section's Results/Gap/Moving Forward)

---

## 2. Main KPIs

Block right after the TL;DR — consolidated view of funnel + base + financials.

### Block 2.1 — "Main KPIs" table (template T1)

KPIs in top-of-funnel → financial-impact order:

1. Branded Searches
2. Sessions
3. Trials
4. CVR Session → Trial
5. New Payments
6. CVR Trial → NP
7. New Sellers
8. Net Adds 🟡
9. Merchant Base 🟡
10. GMV (on-platform, local currency + USD)
11. Orders
12. % Seller ⚠️
13. GMV per Seller ⚠️

🟡 = placeholder (CSV until DP5) · ⚠️ = blocked (see catalog)

### Block 2.2 — Complementary charts (2×2)

```
+---------------------------+---------------------------+
| Trials (bars + plan line) | New Payments (bars+plan)  |
+---------------------------+---------------------------+
| Net Adds (bars +/-)       | GMV (line + plan)         |
+---------------------------+---------------------------+
```

---

## 3. Brand & Comms

### 3.1 Macro Results

**Block 3.1.1 — Charts (2×2)**

```
+---------------------------+---------------------------+
| Branded Searches #        | Branded CTR %             |
+---------------------------+---------------------------+
| Total Market Search Vol   | Share of Market           |
| (bars + branded/non-br.)  | (line, real + plan)       |
+---------------------------+---------------------------+
```

**Block 3.1.2 — "B&C Macro" table** (template T1; KPIs: Branded Searches, Branded CTR %, Share of Market, Total Market Search Volume)

**Block 3.1.3 — Analysis** (Results / Gap & Hypothesis / Moving Forward)

### 3.2 PR

**Block 3.2.1 — "PR — Publications by Tier" table**

| Tier | Real | M-1 | MoM% | Plan | Attainment% |
|---|---|---|---|---|---|
| Gold · Tier 1 · Tier 2 · **Total** | | | | | |

Complement: Proactive Publications, Total Reach (PR).

**Block 3.2.2 — Analysis** (Results / Gap & Hypothesis / Moving Forward)

### 3.3 Social

**Block 3.3.1 — "Social — Instagram" table** (template T2)

Rows: Total Reach, Organic Reach, Paid Reach, Collab Reach, Net Followers, Profile Followers, Engagement Rate, Interactions.

**Block 3.3.2 — Analysis** (Results / Gap & Hypothesis / Moving Forward)

---

## 4. Acquisition

### 4.1 Macro Results

**Block 4.1.1 — Charts (2×2)**

```
+---------------------------+---------------------------+
| Sessions                  | Trials (bars + plan)      |
+---------------------------+---------------------------+
| New Payments (bars+plan)  | CVR Trial → NP (line)     |
+---------------------------+---------------------------+
```

**Block 4.1.2 — "Acquisition Macro" table** (template T1)

Rows: Sessions, Trials, New Payments, New Sellers, QLs, CVR Session→Trial, CVR Trial→NP. (CAC ⚠️ blocked — DP6.)

Optional complement: end-to-end funnel (template T5).

**Block 4.1.3 — Analysis** (Results / Gap & Hypothesis / Moving Forward)

### 4.2 By Source — Branded & Non-Branded (template T3)

Single table grouped by Level 4 (Branded / Non-Branded), rows in Level 2 (see §0.10). Group subtotals + grand total.

**Optional charts:** stacked bar of NPs by source (24m); line of CVR Trial→NP by group.

**Analysis** (Results / Gap & Hypothesis / Moving Forward) — focus: which lever drove/held the result, Branded vs Non-Branded mix.

### 4.3 By ICP (template T4)

⚠️ **Source-blocked** (catalog B12). Once ICP classification is available: Trials/NPs/CVR table by ICP 1-5b + acquisition-quality analysis by profile.

---

## 5. Company Metrics 🟡

All blocks use **CSV placeholder** until DP5 is available (see catalog §6).

### 5.1 Merchant Base & Net Adds

**Block 5.1.1 — Charts (2×2)**

```
+---------------------------+---------------------------+
| Merchant Base (line+area) | Net Adds (bars +/-)       |
+---------------------------+---------------------------+
| Inflow Components         | Outflow Components        |
| (stacked: FP+New+Old Phx) | (stacked: Churns+Downsell)|
+---------------------------+---------------------------+
```

**Block 5.1.2 — "Company Metrics Summary" table** (template T2 + YoY)

Rows: **Net Adds**, First Payments, Churn + Downgrade, **Merchant Base (EOP)**. (Net Adds and Merchant Base highlighted.)

### 5.2 Net Adds — Decomposition

| Component | Real | M-1 | MoM% |
|---|---|---|---|
| First Payments · New Phoenix · Old Phoenix · **Total Inflow** | | | |
| Churns · Downsell to Freemium · **Total Outflow** | | | |
| Ajuste · **Net Adds** | | | |

### 5.3 Churn Breakdown

Rows: Churn Rate, Churns (abs), Downsell to Freemium. (Seller vs Non-Seller ⚠️ blocked.)

### 5.4 Analysis (Results / Gap & Hypothesis / Moving Forward)

Focus: inflow vs outflow balance, where the leak is, Phoenix performance, churn seasonality.

---

## 6. Financial

GMV comes from **DP4** (active — see catalog §7). Breakdowns by channel and by ICP are **on hold** for now.

### 6.1 GMV

**Block 6.1.1 — Chart** — GMV (on-platform) 24m history, line + plan.

**Block 6.1.2 — "GMV & Orders" table** (template T1)

| KPI | Real | Plan | %Achv | YoY | YTD |
|---|---|---|---|---|---|
| GMV (local currency) | | | | | |
| GMV (USD) | | | | | |
| Orders | | | | | |
| Avg Ticket | | | | | |
| GMV POS *(where relevant: CL/CO/MX)* | | | | | |

Notes: use `on_platform` as the primary GMV (off-platform <1% — catalog §7.1); do not add POS to on-platform (POS is a subset).

**Block 6.1.3 — Analysis** (Results / Gap & Hypothesis / Moving Forward)

### 6.2 Productivity ⚠️

% Seller and GMV per Seller — **blocked** until DP5. Include when available.

---

## 7. BACK-UP

Consultative appendix at the end — detailed tables and charts per section, no narrative.

```
7.1 B&C Back-up         — PR by outlet/origin; Social with plan/attainment; extra 24m charts
7.2 Acquisition Back-up — full source breakdown (Level 1, 16 sources); charts by source
7.3 Company Metrics Back-up — Net Adds components 24m; churn by segment (once DP5)
7.4 Financial Back-up   — GMV by currency (LC/USD/Finance USD); Avg Ticket by channel
```

**Rules:** no analytical text; tables and charts may be full-width (no 2×2 grid).

---

## 8. Orchestration conventions

### 8.1 Generation order

```
0. Collect Context Cards per country (see §8.4)
1. Fetch data per country (monthly snapshots + CSV placeholders)
2. Compute comparisons (M-1, YoY, Plan, Attainment%, YTD)
3. Render business sections: Main KPIs → B&C → Acquisition → Company Metrics → Financial → BACK-UP
4. Generate textual analyses (LLM) per section — Results / Gap & Hypothesis / Moving Forward (uses Context Cards)
5. Generate TL;DR (consumes the Results of all sections)
6. Final document composition
```

### 8.2 Generator input

```
meta:            country, business_unit, month_label, prior_month_label, prior_year_month_label
context_cards:   [ ... ]   ← collected in step 0 (see §8.4); empty if nothing happened
main_kpis:       computed KPIs
brand_comms:     { macro, pr, social }
acquisition:     { macro, by_source, by_icp }
company_metrics: { base, net_adds_components, churn }
financial:       { gmv }
analyses:        { per section: results, gap, moving_forward } + { tldr }  ← LLM
```

### 8.3 Output

One document per country and month: `MBR_<COUNTRY>_<MONTH_LABEL>`.

### 8.4 Context collection flow

External context (real-world events) enters the report **only** through Context Cards. The fields and how the LLM *uses* them are defined in `ANALYSIS_RULES.md` §2; this section defines how they are *collected*.

**Mechanism — LLM interview that materializes a versioned file:**

```
0a. Before generating a country's MBR, the LLM asks, in plain language:
    "Anything relevant happen in <COUNTRY> this month? Tell me — or say 'nothing'."

0b. The human answers freely (or "nothing").

0c. The LLM structures the answer into Context Cards, mapping affected KPIs to
    canonical catalog names and inferring `status` from the human's wording
    ("should have / probably" → expected/hypothesis; "confirmed / it spiked" → confirmed),
    then echoes them back for confirmation.

0d. On confirmation, the cards are saved to a versioned file:
    context/<YYYY-MM>_<COUNTRY>.md

0e. The generator reads that file at step 1.
```

**Degradation (no human present):** in a fully batch run, step 0a-0c is skipped and the generator reads a pre-filled `context/<YYYY-MM>_<COUNTRY>.md`. The **file is the source of truth** in both modes; the interview is only the comfortable way to fill it. If neither interview nor file exists → the LLM operates on internal causality only and speculates nothing (safe default — see `ANALYSIS_RULES.md` §1.3).

**File format** — `context/<YYYY-MM>_<COUNTRY>.md`:

```markdown
# Context — BR · 2026-04

## Card 1 — Billing incident
- affected_kpis: New Payments, Trials
- direction: down
- magnitude: large
- status: expected
- description: Billing incident extended trials to 30 days
- analyst_take: Likely the month's biggest factor; confirm with Product

## Card 2 — Joel Jota brand campaign
- affected_kpis: Total Reach (Social), Engagement Rate
- direction: up
- magnitude: medium
- status: confirmed
- description: Influencer campaign peaked mid-month
- analyst_take: —
```

An empty file (no cards) is valid and means "nothing relevant happened" → internal causality only.

*(If a future code-only generator needs strict parsing, swap markdown for YAML — same fields.)*

---

## 9. Changelog

- **2026-06-02** — (v2.1) Added **Context collection flow** (§8.4): LLM interview that materializes a versioned `context/<YYYY-MM>_<COUNTRY>.md` file; degrades to pre-filled file in batch mode; empty file = internal causality only. Generation order gains step 0; generator input gains `context_cards`.
- **2026-06-02** — (v2) Aligned with KPI Catalog v2 and converted to English (machine-consumed, output is EN): `Lifecycle` → **Company Metrics**; **Financial** becomes its own section (§6) with GMV/Orders/Avg Ticket active via DP4; Acquisition restructured into **§4.2 by source** (Level 4 groups, Level 2 rows) + **§4.3 by ICP** (blocked); added **canonical table templates** (T1 Performance vs Budget, T2 MoM, T3 Source breakdown, T4 ICP, T5 Acq×Activation funnel); **monthly snapshot** as data source (§0.9); `country` parameterization (§0.2); **TL;DR activated** (described first, generated last). Removed Python-module status notes (docs-first paradigm).
- **2026-06-02** — Initial version (PT). Canonical MBR structure with 6 sections and the Charts/Tables/Analysis pattern.
