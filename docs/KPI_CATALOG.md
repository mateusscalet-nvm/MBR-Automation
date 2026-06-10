# KPI Catalog — Marketing Analytics

**Última actualización / Última atualização:** 2026-06-02

---

## 🌐 Idioma

- [🇦🇷 Español (Argentina)](#-versión-es-ar)
- [🇧🇷 Português (Brasil)](#-versão-pt-br)

---

# 🇦🇷 Versión ES-AR

## Índice (ES)

0. [Convenciones generales](#0-convenciones-generales)
1. [Glosario de términos](#1-glosario-de-términos)
2. [Diccionario de dimensiones](#2-diccionario-de-dimensiones)
3. [Tablas de referencia](#3-tablas-de-referencia)
4. [KPIs — Brand](#4-kpis--brand-es)
   - 4.1 [Search Presence](#41-search-presence-es)
   - 4.2 [PR (Public Relations)](#42-pr-public-relations-es)
   - 4.3 [Social (Instagram)](#43-social-instagram-es)
5. [KPIs — Acquisition](#5-kpis--acquisition-es)
   - 5.1 [Funnel (Macro)](#51-funnel-macro-es)
   - 5.2 [Funnel Efficiency (CVRs)](#52-funnel-efficiency-cvrs-es)
   - 5.3 [Investment (CAC, Spend)](#53-investment-cac-spend-es)
   - 5.4 [By Lever](#54-by-source--lever-es)
6. [KPIs — Company Metrics](#6-kpis--company-metrics-es)
   - 6.1 [Base Health](#61-base-health-es)
   - 6.2 [Inflow](#62-inflow-es)
   - 6.3 [Outflow](#63-outflow-es)
7. [KPIs — Financial](#7-kpis--financial-es)
   - 7.1 [Volume](#71-volume-es)
   - 7.2 [Productivity](#72-productivity-es)
8. [Apéndice — Notas técnicas](#8-apéndice--notas-técnicas)
9. [Cookbook — SQL snippets](#9-cookbook--sql-snippets-es)
10. [Backlog](#10-backlog-es)
11. [Changelog](#11-changelog-es)

---

## Vista panorámica — KPI Matrix

Tabla única con todos los KPIs catalogados, para búsqueda rápida. Orden: **Company Metrics · Financial · Acquisition · Brand**.

| # | KPI | Dominio · Subdominio | Fuente | Status |
|---|---|---|---|---|
| 1 | Merchant Base | Company Metrics · Base Health | CSV → DP5 | 🟡 Placeholder |
| 2 | Net Adds | Company Metrics · Base Health | CSV → DP5 | 🟡 Placeholder |
| 3 | First Payments (Company Metrics) | Company Metrics · Inflow | CSV → DP5 | 🟡 Placeholder |
| 4 | New Phoenix | Company Metrics · Inflow | CSV → DP5 | 🟡 Placeholder |
| 5 | Old Phoenix | Company Metrics · Inflow | CSV → DP5 | 🟡 Placeholder |
| 6 | Ajuste | Company Metrics · Inflow (Reconciliation) | CSV → DP5 | 🟡 Placeholder |
| 7 | Churns | Company Metrics · Outflow | CSV → DP5 | 🟡 Placeholder |
| 8 | Downsell to Freemium | Company Metrics · Outflow | CSV → DP5 | 🟡 Placeholder |
| 9 | Churn + Downgrade | Company Metrics · Outflow | derivado | 🟡 Placeholder |
| 10 | Churn Rate | Company Metrics · Outflow | derivado | 🟡 Placeholder |
| 11 | GMV (Total, LC) | Financial · Volume | DP4 | Activo |
| 12 | GMV (Total, USD) | Financial · Volume | DP4 | Activo |
| 13 | GMV (Total, Finance USD) | Financial · Volume | DP4 | Activo |
| 14 | GMV (On-Platform sin POS) | Financial · Volume | DP4 | Activo |
| 15 | GMV (POS) | Financial · Volume | DP4 | Activo |
| 16 | Orders (Total) | Financial · Volume | DP4 | Activo |
| 17 | Avg Ticket (Total) | Financial · Volume | DP4 | Activo |
| 18 | % Seller | Financial · Productivity | DP5 | ⚠️ Bloqueado |
| 19 | GMV per Seller | Financial · Productivity | DP4+DP5 | ⚠️ Bloqueado |
| 20 | Sessions | Acquisition · Funnel | DP2 | Activo |
| 21 | Bounced Sessions | Acquisition · Funnel (Quality) | DP2 | Activo |
| 22 | Total Users | Acquisition · Funnel | DP2 | Activo |
| 23 | Organic Users | Acquisition · Funnel | DP2 | Activo |
| 24 | Avg Pageviews per Session | Acquisition · Funnel (Quality) | DP2 | Activo |
| 25 | Avg Session Duration | Acquisition · Funnel (Quality) | DP2 | Activo |
| 26 | Trials | Acquisition · Funnel | DP1 | Activo |
| 27 | New Payments (NPs) | Acquisition · Funnel | DP1 | Activo |
| 28 | Payment Created At | Acquisition · Funnel (Alt) | DP1 | Activo |
| 29 | New Sellers | Acquisition · Funnel | DP1 | Activo |
| 30 | New Seller Created At | Acquisition · Funnel (Alt) | DP1 | Activo |
| 31 | QLs (Qualified Leads) | Acquisition · Funnel | DP1 | Activo |
| 32 | CVR Session → Trial | Acquisition · Funnel Efficiency | DP1+DP2 | Activo |
| 33 | CVR Trial → NP | Acquisition · Funnel Efficiency | DP1 | Activo |
| 34 | Spend | Acquisition · Investment | DP6 | ⚠️ Bloqueado |
| 35 | CAC | Acquisition · Investment | derivado | ⚠️ Bloqueado |
| 36 | Branded Searches | Brand · Search Presence | DP3 | Activo |
| 37 | Branded CTR % | Brand · Search Presence | DP3 | Activo |
| 38 | Share of Market | Brand · Search Presence | DP3 | Activo |
| 39 | Share of Market (excl. Wix) | Brand · Search Presence | DP3 | Activo |
| 40 | Total Market Search Volume | Brand · Search Presence | DP3 | Activo |
| 41 | SOV AI Platforms | Brand · Search Presence | Manual | 🔵 Manual |
| 42 | Total Publications | Brand · PR | Clipping | Activo |
| 43 | Gold Media | Brand · PR | Clipping | Activo |
| 44 | Tier 1 | Brand · PR | Clipping | Activo |
| 45 | Tier 2 | Brand · PR | Clipping | Activo |
| 46 | Proactive Publications | Brand · PR | Clipping | Activo |
| 47 | Total Reach (PR) | Brand · PR | Clipping | Activo |
| 48 | Total Reach (Social) | Brand · Social | Social Insights | Activo |
| 49 | Organic Reach | Brand · Social | Social Insights | Activo |
| 50 | Paid Reach | Brand · Social | Social Insights | Activo |
| 51 | Collab Reach | Brand · Social | Social Insights | Activo |
| 52 | Interactions | Brand · Social | Social Insights | Activo |
| 53 | Saves | Brand · Social | Social Insights | Activo |
| 54 | Shares | Brand · Social | Social Insights | Activo |
| 55 | Engagement Rate | Brand · Social | Social Insights | Activo |
| 56 | Profile Followers | Brand · Social | IG Followers | Activo |
| 57 | Net New Followers | Brand · Social | IG Followers | Activo |
| 58 | Unfollowers | Brand · Social | IG Followers | Activo |

---

## 0. Convenciones generales

### 0.1 Tipos de fuente

| Tipo | Estándar | Cómo consumir |
|---|---|---|
| **Data Product — Daily** (`*__agg_daily`) | 6 familias de columnas: `effective_*`, `forecast_*`, `expected_monthly_*`, `ponderation_key_*`, `expected_daily_linear_*`, `expected_daily_weighted_*` | `SUM` o `MAX` de los días del período. Para charts intra-mes, análisis diario y plan refinado por tipo de día (linear vs weighted) |
| **Data Product — Snapshot mensual** (`*__agg_snapshot_monthly`) | **3 familias** de columnas: `effective_*`, `forecast_*`, `expected_monthly_*`. Una fila por mes cerrado | Para análisis de meses cerrados. Corre el **día 4 del mes siguiente**, append-only, **congela** el mes — cambios retroactivos aguas arriba no se reflejan |
| **Raw event aggregation** | Tablas `s__*__event` con datos granulares | La agregación es responsabilidad del consumidor (COUNT, SUM, MAX) |
| **CSV / fuente externa** | Archivos planos mientras un DP no existe | Lectura vía pandas / planilla |

**Cuándo usar daily vs snapshot:**
- **Snapshot mensual** — reportes de meses cerrados (MBR, QBR), análisis retrospectivos, KPI catalog de plan vs real. Ventaja: 1 fila por mes × dimensión (queries simples, sin agregación temporal).
- **Daily** — charts intra-mes, monitoring diario, análisis de tendencia. Necesario cuando se necesita el plan diario (linear/weighted) o histórico denso.

### 0.2 Status

- **Activo** — fuente disponible, KPI utilizable hoy
- **🟡 Placeholder** — usando fuente temporal hasta que el DP correspondiente entre en producción
- **⚠️ Bloqueado** — KPI definido pero sin fuente disponible; aguardando DP futuro
- **🔵 Manual** — KPI cuya medición depende de input humano/externo (sin automatización posible actualmente)

### 0.3 Formato de cada entrada de KPI

Cada KPI sigue este template:

- **Dominio · Subdominio:** taxonomía funcional (Brand · Search Presence, Acquisition · Funnel, etc.)
- **Definición (business):** narrativa ejecutiva, contiene los insights operacionales relevantes del schema (ej.: "excluye Next/Evolución")
- **Definición (schema):** cita literal del `comment` de la columna en Databricks (cuando aplica)
- **Fórmula:** expresión lógica
- **Source type / Tabla / Columnas**
- **Agregación:** SUM, MAX, SUM(num)/SUM(den), session-weighted
- **Status:** Activo / Placeholder / Bloqueado / Manual
- **Gotchas:** alertas importantes — muchos vienen directo del schema
- **Related KPIs:** referencia cruzada cuando hay solapamiento o variantes

Los KPIs derivados (CVR, Engagement Rate, CAC) y los placeholder no tienen `Definición (schema)` — solo business.

### 0.4 Comparaciones temporales estándar

- **Real** — período corriente
- **M-1** — mes anterior
- **YoY** — mismo mes del año anterior
- **MoM%** y **YoY%** — variación porcentual
- **Plan / Attainment%** — cuando el KPI tiene `expected_monthly_*`
- **Forecast** — cuando el KPI tiene `forecast_*`
- **YTD** — Ene hasta el mes corriente
- **Quarter** — meses del trimestre corriente hasta el mes corriente
- **EOP / EOM** — End of Period / End of Month (snapshot fin del período)

### 0.5 Agregación correcta de ratios

**Error común:** `AVG(ctr_diario)` o `AVG(share_diario)` → resultado sesgado por días con poco volumen.

**Correcto:** `SUM(numerador) / SUM(denominador)` para el período.

Aplicable a: **CTR, Branded Share, Marketplace Share, Engagement Rate, CVRs, Churn Rate**.

### 0.6 Agregación correcta de averages session-weighted

Para `avg_pageviews` y `avg_session_duration` (DP2), agregar como:

```sql
SUM(effective_avg_pageviews * effective_total_sessions)
  / NULLIF(SUM(effective_total_sessions), 0)
```

(Documentado por el schema: *"Session-weighted average..."*)

### 0.7 Plans con agregación distinta de SUM

| KPI | Columna de plan | Agregación |
|---|---|---|
| Branded Share | `expected_monthly_branded_share_tiendanube_kwp_daily` | **MAX** mensual (% no es aditivo) |
| Engagement Rate Social | `engagement_rate_social` | **MAX** mensual (constante diaria) |
| Reach Social | `reach_social` | SUM (distribuido por día) |
| Branded Searches SC | `expected_monthly_branded_searches_sc_daily` | SUM |
| Trials / NPs / QLs / etc. | `expected_monthly_*` | SUM |

---

## 1. Glosario de términos

### 1.1 Conceptos de negocio

| Término | Definición |
|---|---|
| **Phoenix (New)** | Comerciantes que volvieron a la base vía funnel Phoenix con ventana corta de reactivación (reactivación reciente) |
| **Phoenix (Old)** | Comerciantes que volvieron a la base luego de haber churned hace más tiempo (long-tail de reactivación) |
| **Net Adds** | Saldo neto en la base del período: inflow (nuevos + reactivaciones) − outflow (churn + downsell) + ajuste contable |
| **Branded Levers** | Sources de adquisición que operan sobre marca ya reconocida (Nivel 4 — Branded): Direct, Organic, Performance Brand. Ver §3.4 |
| **Non-Brand Levers** | Sources que construyen demanda nueva (Nivel 4 — Non-Branded): Performance No Brand, Organic Growth, Affiliates, Partners, Low Volume. Ver §3.4 |
| **Low Volume** | Agregación de sources individualmente poco significativas (Nivel 2): Brand & Comms, Eea, Enp, Mandae, Mid-market, Nurturing, Others, Product Marketing, Store Referral. Ver §3.4 |
| **Performance (Nivel 3)** | Mecánica de adquisición con medios pagos atribuibles: Performance Brand + Performance No Brand |
| **Organic (Nivel 3)** | Mecánica de adquisición sin medios pagos directos: Direct, Organic, Organic Growth |
| **Indirect (Nivel 3)** | Mecánica de adquisición vía terceros: Affiliates, Partners |
| **Seller** | Comerciante con ≥7 ventas en los últimos 90 días (ventana móvil). Métrica de "comerciante activo generando transacciones" |
| **Non-Seller** | Comerciante en la base que no alcanza el criterio de Seller |
| **Mean-click attribution** | Modelo de atribución en el que cada conversión se reparte igualmente entre todos los clicks que la precedieron |
| **D2C (Direct-to-Consumer)** | Universo de marcas oficiales con tienda propia (Nuvemshop/Tiendanube + competidores oficiales) — denominador del Share of Market |
| **Marketplace** | Categoría distinta de D2C — agrupa marketplaces (Mercado Libre, Amazon, Shopee, etc.) |
| **Special Days** | Fechas con comportamiento atípico de demanda (Black Friday, Cyber, etc.) listadas en `ext__marketing__acquisition__key_dates_by_country` |
| **Trial → Payment lag** | Intervalo temporal entre un trial y el primer pago — el NP del mes X puede venir del Trial del mes X-1 |

### 1.2 ICPs (Ideal Customer Profile)

Framework de adquisición que segmenta el universo por **atributo del comerciante** (no por rango de GMV). Los 5 segmentos **no suman 100%** del universo — perfiles solapados son aislados a propósito para mantener cada ICP "limpio".

| Tier | ICP | Nombre | Atributo definidor |
|---|---|---|---|
| **Premium** | **ICP 1** | Platform Migrants | Comerciantes migrando de otra plataforma — ese es el atributo definidor |
| **Premium** | **ICP 2** | Social Sellers | Comerciantes vendiendo principalmente en redes sociales (Instagram, WhatsApp) — ese es el atributo definidor |
| **Premium** | **ICP 3** | Offline Sellers | Comerciantes saliendo de tienda física hacia digital — economics premium |
| **Mid-Premium** | **ICP 4** | Marketplace Sellers | Marketplace-only (ML, Shopee) — social-only tail aislado para mantener ICP 4 limpio |
| **SMBs** | **ICP 5a** | D2C Starters | Emprendedores D2C primerizos — el motor de volumen del modelo |
| **SMBs** | **ICP 5b** | Affiliates / Dropshippers | Sub-programa Loja Pronta (en descontinuación) + otros affiliates de calidad inferior |

**Notas:**
- Los ICPs se definen por **atributo del comerciante**, no por rango de GMV
- Los 5 segmentos no cubren 100% del universo — solapamientos son deliberadamente excluidos para mantener cada ICP "limpio"
- Owner: RevOps / Marketing Ops (verificar fuente de verdad para definiciones operacionales detalladas)

### 1.3 Acrónimos

| Sigla | Significado |
|---|---|
| **NP** | New Payment — primer pago de un nuevo comerciante |
| **NS** | New Seller — nuevo comerciante que se convirtió en seller |
| **QL** | Qualified Lead |
| **Trial** | Nuevo registro free (trial iniciado) |
| **CVR** | Conversion Rate |
| **CTR** | Click-Through Rate |
| **SOM** | Share of Market |
| **SOV** | Share of Voice |
| **EOP / EOM** | End of Period / End of Month |
| **BU** | Business Unit (SMB o MM) |
| **MoM / YoY / YTD** | Month-over-Month / Year-over-Year / Year-to-Date |
| **GMV** | Gross Merchandise Value |
| **CAC** | Customer Acquisition Cost |
| **LTV** | Lifetime Value |
| **DP** | Data Product |
| **SC** | Search Console (Google) |
| **KWP** | Keyword Planner (Google) |
| **GA4** | Google Analytics 4 |
| **FX** | Foreign Exchange (conversión de moneda) |

---

## 2. Diccionario de dimensiones

Las dimensiones son los campos que **describen** los KPIs (no los miden). Filtros y segmentaciones se aplican sobre ellas.

### 2.1 `country`

- **Definición:** Código ISO-2 del país del comerciante / de la query / del evento.
- **Valores posibles por fuente:**

| Fuente | Países cubiertos |
|---|---|
| DP1 (meanclick) | AR, BR, MX, CL, CO |
| DP2 (GA4 Sessions) | AR, BR, MX, CL, CO *(según atribución GA4)* |
| DP3 (GSC + KWP) | AR, BR, MX, CL, CO, PE |
| Raw events B&C (clipping, social, followers) | AR, BR, MX |
| CSV Net Adds | AR, BR, CL, CO, MX |

### 2.2 `business_unit`

- **Definición:** Segmento de negocio del comerciante — **SMB** (small/medium) o **MM** (Mid-Market).
- **Cómo identificar por fuente:**

| Fuente | Criterio MM | Criterio SMB |
|---|---|---|
| DP1 (meanclick) | `page_subgroup = 'Next'` OR `mkt_subteam = 'Mid-Market'` | todo lo que no es MM |
| DP2 (GA4) | `page_subgroup = 'Next'` OR `mkt_subteam = 'Mid-Market'` | todo lo que no es MM |
| DP3 (Search / KWP) | `is_next_evolucion = true` en la query | `is_next_evolucion = false` |
| Raw events B&C | sin columna explícita — asumir SMB | — |

- **Definición (schema, DP1):** *"Business unit classification at the time of store acquisition (SMB or MM) based on store `first_contract_type` from acquisition profile. SMB: all non-enterprise contracts; MM: enterprise contracts."*
- **Gotchas:**
    - Criterio aún en revisión por el equipo de Ops — puede cambiar
    - MM corresponde a la marca **Next / Evolución**
    - La columna `brand_segment` en DP3 traduce: `'Nuvemshop / Tiendanube'` (SMB) o `'Next / Evolución'` (MM)

### 2.3 `mkt_source` ⭐ (canónica para análisis por source/lever)

- **Definición:** Marketing source aligned to attribution model — la source canónica que viene del modelo mean-click. **Esta es la columna a usar para cualquier análisis por source o agrupamiento por lever.**
- **Definición (schema):** *"Marketing source aligned to attribution (`mkt_source_attribution` from the plan ref when the row is plan-driven)."*
- **Disponible en:** DP1, DP2 (daily y snapshot mensual)
- **Valores observados** (DP1, 2026 YTD — 16 sources raw):

`Affiliates`, `Brand & Comms`, `Direct`, `Eea`, `Enp`, `Mandae`, `Mid-market`, `Nurturing`, `Organic`, `Organic Growth`, `Others`, `Partners`, `Performance Brand`, `Performance No Brand`, `Product Marketing`, `Store Referral`

→ Para la jerarquía de agrupamiento (Low Volume · Performance/Organic/Indirect · Branded/Non-Branded), ver **§3.4 Jerarquía de mkt_source**.

- **Gotchas:**
    - **Siempre usar `mkt_source`** para breakdowns y agrupamientos — no `plan_mkt_source_ops`
    - `Mandae` solo aparece en `mkt_source`, no en `plan_mkt_source_ops` (attribution-only — sin fila de plan)

### 2.4 `plan_mkt_source_ops` (uso restringido)

- **Definición:** Label de marketing source que viene de la planilla de plan de Ops. **No usar para breakdowns analíticos — usar solo para análisis plan-only** (ej.: validación de qué sources tienen meta cargada).
- **Definición (schema):** *"Ops / spreadsheet marketing source label from the plan ref for the plan grain (source-only before 2026-01-01; source + subteam from 2026); null when there is no plan row (attribution-only)."*
- **Disponible en:** DP1, DP2
- **Gotchas:**
    - **NULL** para filas sin plan (attribution-only) — puede "desaparecer" sources reales como Mandae en breakdowns
    - Labels iguales a los de `mkt_source` (excepto por la ausencia de Mandae)
    - Usar `mkt_source` en lugar de esta columna en la enorme mayoría de los casos (ver §2.3)

### 2.5 `mkt_subteam`

- **Definición:** Bucket de subteam de marketing.
- **Definición (schema):** *"Marketing subteam bucket. For full_date before 2026-01-01 this column is always empty string (source-level grain). From 2026-01-01 onward it follows attribution/plan subteam; empty string when not specified (not SQL NULL), for stable merge keys."*
- **Disponible en:** DP1, DP2
- **Gotchas:** Antes de 2026-01-01 siempre es `''` (no NULL — string vacío)

### 2.6 `date` y variantes de calendario

- **`date` / `full_date`:** fecha de calendario diaria (grain de las tablas diarias)
- **`date_day` / `date_month` / `date_quarter` / `date_year` / `date_week`:** componentes derivados — `date_month` en formato `'YYYY-MM'`, `date_quarter` en formato `'YYYY-QN'`
- **`day_name`:** nombre del día de la semana

### 2.7 `brand_segment` (DP3)

- **Definición:** Label legible de la variante de marca de la fila.
- **Definición (schema):** *"Human-readable label of the brand variant carried in business_unit: 'Nuvemshop / Tiendanube' for SMB, 'Next / Evolución' for MM."*

### 2.8 `is_store_blocked` (DP1)

- **Definición:** Flag de tienda bloqueada. Las tiendas bloqueadas son **excluidas** de los `effective_*` por construcción del DP.
- **Gotchas:** El filtro ya está aplicado en los `effective_*` — no hace falta filtrar de nuevo. Pero para análisis sobre `raw_*` o joins con otras tablas, recordar.

### 2.9 `special_days` (calendario marketing)

- **Definición:** Días con comportamiento atípico de demanda. Vienen de la tabla manual `ext__marketing__acquisition__key_dates_by_country`.
- **Uso:** Para KPIs con plan, los special days cambian la ventana de forecast (180d en lugar de 90d).
- **Ejemplos:** Black Friday, Cyber Monday, Hot Sale (AR), Buen Fin (MX).

### 2.10 `icp` (Ideal Customer Profile)

- **Definición:** Segmento del comerciante según el framework de ICPs (ver §1.2). Usado para abrir KPIs de funnel (Trials, NPs, CVR Trial→NP) por perfil de adquisición.
- **Valores:** ICP 1 (Platform Migrants), ICP 2 (Social Sellers), ICP 3 (Offline Sellers), ICP 4 (Marketplace Sellers), ICP 5a (D2C Starters), ICP 5b (Affiliates / Dropshippers). Ver §1.2 para definiciones.
- **Status:** ⚠️ **Fuente de clasificación pendiente** — hoy no existe una columna de tag de ICP por comerciante en ningún DP. La apertura por ICP en los MBRs se construye con una fuente externa (planilla / clasificación manual).
- **Gotchas:**
    - Los MBRs históricos (BR, MX) usan la **nomenclatura antigua** (ICP 1-4 + "Fallback"), que **no** coincide 1:1 con el framework nuevo de §1.2. Validar el mapeo antiguo → nuevo antes de comparar series temporales.
    - El framework nuevo (§1.2) es la referencia canónica; los reportes deben migrar hacia él.
    - Los segmentos no suman 100% del universo (ver §1.2).

---

## 3. Tablas de referencia

### 3.1 Data Products activos

Cada DP tiene dos variantes: **daily** (granularidad diaria, 6 familias) y **snapshot monthly** (mensual, 3 familias). Ver §0.1 para cuándo usar cada una.

| DP | Daily | Snapshot mensual | Granularidad | Dominio principal |
|---|---|---|---|---|
| **DP1 — Acquisition (meanclick)** | `g__general__meanclick_budget_forecast__agg_daily` | `g__general__meanclick_budget_forecast__agg_snapshot_monthly` | (fecha o mes) × país × `mkt_source` × `mkt_subteam` × BU | Acquisition |
| **DP2 — GA4 Sessions** | `g__general__ga4_sessions_budget_forecast__agg_daily` | `g__general__ga4_sessions_budget_forecast__agg_snapshot_monthly` | (fecha o mes) × país × `mkt_source` × `mkt_subteam` × BU | Acquisition |
| **DP3 — GSC + KWP Searches** | `g__general__gsc_kwp_searches_budget_forecast__agg_daily` | `g__general__gsc_kwp_searches_budget_forecast__agg_snapshot_monthly` | (fecha o mes) × país × BU | Brand |
| **DP4 — GMV (Finance Segments)** | `g__general__gmv_finance_segments_budget_forecast__agg_snapshot_daily` | `g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly` | (fecha o mes) × país × `finance_segment` × BU | Financial |

Todas están bajo `data_products_prd.data_marketing`.

**Snapshot mensual — comportamiento:**
- Corren el día **4 del mes siguiente** y congelan el mes anterior
- Append-only — cambios retroactivos aguas arriba (ej.: flips en `flg_gmv`) **no** se reflejan después del snapshot
- Particionados por `snapshot_month` (INT `yyyyMM`)
- Tienen solo las 3 familias canónicas (`effective_*`, `forecast_*`, `expected_monthly_*`) — sin `ponderation_key_*`, sin split linear/weighted (no tiene sentido en grain mensual)

### 3.2 Raw event tables (Brand & Comms)

| Dominio | Tabla | Granularidad |
|---|---|---|
| **PR Clipping** | `data_products_prd.data_marketing.s__brand_and_comms__clipping__event` | publicación |
| **Social Insights** | `data_products_prd.data_marketing.s__brand_and_comms__social_insights__event` | fecha × país |
| **Instagram Followers** | `data_products_prd.data_marketing.s__brand_and_comms__instagram_followers__event` | fecha × país |
| **B&C Goals** | `data_products_prd.data_marketing.s__brand_and_comms__goals__event` | fecha × país |

### 3.3 Data Products en construcción

| DP | KPIs esperados | Status |
|---|---|---|
| **DP5 — Merchant Base** | Merchant Base, Net Adds, Churn, Downgrade, New Phoenix, Old Phoenix, Ajuste | En construcción. Placeholder: CSV |
| **DP6 — Marketing Expenses & Headcount** | Spend, Headcount Cost, Headcount # | En construcción. **Sin placeholder** |

### 3.4 Jerarquía de `mkt_source` (4 niveles)

La columna canónica es **`mkt_source`** (no `plan_mkt_source_ops` — ver §2.3 y §2.4). Los 16 valores raw se agrupan en 3 niveles adicionales para análisis de breakdown — cada nivel ofrece una "lente" diferente:

- **Nivel 1** — `mkt_source` (16 valores raw, provenientes de la atribución)
- **Nivel 2** — consolidación: las 9 sources de bajo volumen individual se agrupan en **Low Volume**, resultando en **8** valores
- **Nivel 3** — agrupamiento por **mecánica de adquisición** (4 valores): Performance · Organic · Indirect · Low Volume
- **Nivel 4** — agrupamiento por **relación con la marca** (2 valores): Branded · Non-Branded

| Nivel 1 (mkt_source — 16) | Nivel 2 (8) | Nivel 3 (4) | Nivel 4 (2) |
|---|---|---|---|
| Direct | Direct | Organic | Branded |
| Organic | Organic | Organic | Branded |
| Performance Brand | Performance Brand | Performance | Branded |
| Performance No Brand | Performance No Brand | Performance | Non-Branded |
| Organic Growth | Organic Growth | Organic | Non-Branded |
| Affiliates | Affiliates | Indirect | Non-Branded |
| Partners | Partners | Indirect | Non-Branded |
| Brand & Comms | Low Volume | Low Volume | Non-Branded |
| Eea | Low Volume | Low Volume | Non-Branded |
| Enp | Low Volume | Low Volume | Non-Branded |
| Mandae | Low Volume | Low Volume | Non-Branded |
| Mid-market | Low Volume | Low Volume | Non-Branded |
| Nurturing | Low Volume | Low Volume | Non-Branded |
| Others | Low Volume | Low Volume | Non-Branded |
| Product Marketing | Low Volume | Low Volume | Non-Branded |
| Store Referral | Low Volume | Low Volume | Non-Branded |

**Cuándo usar cada nivel:**

| Nivel | Caso de uso típico |
|---|---|
| 1 | Análisis operacionales granulares; investigación de variación por source específica |
| 2 | Breakdowns en reportes (MBR, dashboards) — esconde ruido de sources marginales |
| 3 | Vista consolidada de mecánica (performance vs orgánico vs indirecto) |
| 4 | Storytelling ejecutivo — narrativa de Branded Levers vs Non-Branded Levers |

**Notas:**
- "Others" en el Nivel 1 no se descarta — pasa a formar parte del **Low Volume** en el Nivel 2
- El Nivel 2 debe ser el estándar para tablas y charts de reportes — combina legibilidad y cobertura
- Direct se clasifica como Organic en el Nivel 3 (no hay gasto pago) pero Branded en el Nivel 4 (el usuario busca la marca)

---

## 4. KPIs — Brand {#4-kpis--brand-es}

### 4.1 Search Presence {#41-search-presence-es}

#### Branded Searches

- **Dominio · Subdominio:** Brand · Search Presence
- **Definición (business):** Volumen de búsquedas en Google que contienen la marca Nuvemshop/Tiendanube. En SMB, excluye la marca Mid-Market "Next/Evolución". Dos fuentes complementarias: **Search Console (SC)** mide impresiones reales que recibimos; **Keyword Planner (KWP)** mide el tamaño del mercado branded. El plan oficial está en SC.
- **Definición (schema, SC):** *"Daily branded impressions in Google Search Console for the brand variant of this row. Counts impressions where `is_nuvemshop_tiendanube=true` AND (`d2c_match_type='exact'` OR `marketplace_match_type='exact'`), split by `is_next_evolucion` (SMB=false, MM=true). NULL for future dates."*
- **Fórmula (SC, oficial p/ plan):** `SUM(effective_branded_searches_sc_daily)`
- **Fórmula (KWP, p/ Share of Market):** `SUM(effective_branded_searches_tiendanube_kwp_daily)`
- **Source type:** Data Product (DP3)
- **Columnas:** real `effective_branded_searches_sc_daily` · plan `expected_monthly_branded_searches_sc_daily` · forecast `forecast_branded_searches_sc_daily`
- **Agregación:** SUM
- **Status:** Activo
- **Gotchas:**
    - No confundir SC con KWP — fuentes y universos diferentes
    - KWP se distribuye linealmente desde el mensual — poca utilidad para variación intra-mes
    - Plan SMB solo en SC; MM sin plan hoy
- **Related KPIs:** Branded CTR, Share of Market, Total Market Search Volume

#### Branded Searches CTR %

- **Dominio · Subdominio:** Brand · Search Presence
- **Definición (business):** Click-through rate sobre queries branded en Google Search Console — qué % de los usuarios que ven el resultado branded hace click.
- **Definición (schema):** *"Daily click-through rate for branded SC traffic: `effective_branded_clicks_sc_daily / effective_branded_searches_sc_daily`. 0 when no impressions."*
- **Fórmula:** `SUM(effective_branded_clicks_sc_daily) / SUM(effective_branded_searches_sc_daily)`
- **Source type:** Data Product (DP3)
- **Agregación:** **SUM(num) / SUM(den)** — nunca promedio de CTRs diarios
- **Status:** Activo (sin plan)
- **Gotchas:**
    - Existe una columna lista `effective_branded_ctr_sc_daily` para el ratio diario — para período usar `SUM(num)/SUM(den)`
    - SC, no KWP — CTR no existe en KWP
- **Related KPIs:** Branded Searches

#### Share of Market (Branded Share KWP)

- **Dominio · Subdominio:** Brand · Search Presence
- **Definición (business):** Participación de la marca en el universo de búsquedas D2C oficiales (Nuvemshop/Tiendanube + competidores oficiales identificados por KWP). Mide "porción de mente" del consumidor en el mercado.
- **Definición (schema):** *"Daily branded market share: `effective_branded_searches_tiendanube_kwp_daily / effective_d2c_searches_kwp_daily` (our official-D2C brand impressions over the total official-D2C market). 0 when denominator is 0. SMB only; NULL for MM."*
- **Fórmula:** `SUM(effective_branded_searches_tiendanube_kwp_daily) / SUM(effective_d2c_searches_kwp_daily)`
- **Source type:** Data Product (DP3)
- **Columnas:** real `effective_branded_share_tiendanube_kwp_daily` (pre-calc diario) · plan `expected_monthly_branded_share_tiendanube_kwp_daily`
- **Agregación:** SUM(num) / SUM(den) — no el promedio del ratio diario
- **Status:** Activo
- **Gotchas:**
    - El plan viene como **MAX** mensual — share es % único por mes, no aditivo
    - Cada país tiene su universo de competidores propio, ya segmentado por el DP
- **Related KPIs:** Share of Market (excl. Wix), Total Market Search Volume

#### Share of Market — excl. Wix

- **Dominio · Subdominio:** Brand · Search Presence
- **Definición (business):** Variante del Share of Market que **excluye Wix** del universo D2C. Más comparable internacionalmente, ya que la presencia de Wix sesga el denominador en algunos mercados.
- **Definición (schema):** *"Daily branded market share excluding Wix from the denominator. SMB only; NULL for MM."*
- **Fórmula:** `SUM(effective_branded_searches_tiendanube_kwp_daily) / SUM(effective_d2c_searches_kwp_excl_wix_daily)`
- **Source type:** Data Product (DP3)
- **Agregación:** SUM(num) / SUM(den)
- **Status:** Activo (sin plan)
- **Related KPIs:** Share of Market

#### Total Market Search Volume

- **Dominio · Subdominio:** Brand · Search Presence (Market Context)
- **Definición (business):** Volumen total de búsquedas en Keyword Planner — branded + non-branded. Dimensiona el tamaño absoluto del mercado.
- **Definición (schema):** *"Daily total Keyword Planner impressions across all queries (branded + non-branded). Monthly source distributed linearly by days in the month. SMB only; NULL for MM."*
- **Fórmula:** `SUM(effective_total_market_searches_kwp_daily)`
- **Source type:** Data Product (DP3)
- **Status:** Activo (sin plan)
- **Gotchas:**
    - Distribuido linealmente desde el mensual — no usar para análisis intra-mes

#### SOV AI Platforms

- **Dominio · Subdominio:** Brand · Search Presence (AI)
- **Definición (business):** Share of Voice en plataformas de búsqueda AI (ChatGPT, Perplexity, Gemini, etc.).
- **Source type:** 🔵 Manual — input externo
- **Status:** 🔵 Manual

### 4.2 PR (Public Relations) {#42-pr-public-relations-es}

#### Total Publications

- **Dominio · Subdominio:** Brand · PR
- **Definición (business):** Total de publicaciones cubiertas por el clipping de PR en el período.
- **Fórmula:** `COUNT(*)` en `s__brand_and_comms__clipping__event` filtrado por país y mes
- **Source type:** Raw event aggregation
- **Status:** Activo
- **Plan:** ✅ vía `publicaciones_totales_pr` en `s__brand_and_comms__goals__event`

#### Gold Media

- **Dominio · Subdominio:** Brand · PR
- **Definición (business):** Publicaciones en medios clasificados como Golden — tier máximo, por encima de los tiers numéricos (1-4).
- **Definición (schema, `golden_media_flag`):** *"Indicates whether the media outlet is classified as Golden (premium tier)"*
- **Fórmula:** `SUM(CASE WHEN golden_media_flag = TRUE THEN 1 ELSE 0 END)`
- **Status:** Activo

#### Tier 1

- **Dominio · Subdominio:** Brand · PR
- **Definición (business):** Publicaciones tier 1 que **no** son Gold (Gold se cuenta aparte).
- **Definición (schema, `tier`):** *"Tier or priority classification of the media outlet (1, 2, 3, 4)"*
- **Fórmula:** `SUM(CASE WHEN tier = 1 AND golden_media_flag = FALSE THEN 1 ELSE 0 END)`
- **Status:** Activo
- **Plan:** ✅ vía `publicaciones_t1_pr`

#### Tier 2

- **Dominio · Subdominio:** Brand · PR
- **Fórmula:** `SUM(CASE WHEN tier = 2 THEN 1 ELSE 0 END)`
- **Status:** Activo

#### Proactive Publications

- **Dominio · Subdominio:** Brand · PR
- **Definición (business):** Publicaciones originadas proactivamente por el equipo (push), en oposición a reactivas (pickup de noticia externa).
- **Definición (schema, `origin_type`):** *"Indicates whether the article is Original or Replica (pickup). For BR: Proativa maps to Original, Reativa maps to Replica."*
- **Fórmula:** `SUM(CASE WHEN origin_type = 'Original' THEN 1 ELSE 0 END)`
- **Status:** Activo
- **Gotchas:** En BR los labels vienen en portugués ("Proativa"/"Reativa") y se mapean a Original/Replica en el DP

#### Total Reach (PR)

- **Dominio · Subdominio:** Brand · PR
- **Definición (business):** Alcance estimado total de las publicaciones en el período.
- **Definición (schema, `reach`):** *"Estimated audience reach or potential impressions. Returns NULL for invalid values (not 0). WARNING: Invalid numeric values should be caught and fixed in source data."*
- **Fórmula:** `SUM(COALESCE(reach, 0))`
- **Status:** Activo
- **Gotchas:**
    - Valores inválidos vienen como **NULL** (no 0) — usar `COALESCE` al sumar
    - La calidad del dato tiene WARNING en el schema — problemas aguas arriba

### 4.3 Social (Instagram) {#43-social-instagram-es}

#### Total Reach (Social)

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Alcance total en Instagram, sumando 4 buckets: orgánico, pago, colabs con 3rd party, y manual_non_classified.
- **Definición (schema):** *"Total reach: organic + paid + third_party_collabs + manual_non_classified"*
- **Fórmula:** `SUM(reach_total)`
- **Source type:** Raw event aggregation
- **Tabla:** `s__brand_and_comms__social_insights__event`
- **Status:** Activo
- **Plan:** ✅ vía `reach_social`
- **Gotchas:** Ya es la suma de los 4 componentes — no recalcular como `reach_organic + reach_paid_total + reach_collab_third_party` (pierde el bucket `manual_non_classified`)

#### Organic Reach

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Alcance vía contenido orgánico (no-pago, no-colab). Fuente: Supermetrics.
- **Fórmula:** `SUM(reach_organic)`
- **Status:** Activo

#### Paid Reach

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Alcance vía campañas pagas en Instagram.
- **Fórmula:** `SUM(reach_paid_total)`
- **Status:** Activo

#### Collab Reach

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Alcance vía colaboraciones con terceros (creators, partnerships). No está incluido en el orgánico.
- **Fórmula:** `SUM(reach_collab_third_party)`
- **Status:** Activo

#### Interactions

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Total de interacciones en Instagram (likes, comentarios, saves, shares), sumando los 4 buckets.
- **Fórmula:** `SUM(interactions_total)`
- **Status:** Activo

#### Saves

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Posts guardados por los usuarios — señal fuerte de interés.
- **Fórmula:** `SUM(saves_total)`
- **Status:** Activo

#### Shares

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Contenido compartido por los usuarios — señal de propagación.
- **Fórmula:** `SUM(shares_total)`
- **Status:** Activo

#### Engagement Rate

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Tasa de engagement — interacciones por alcance.
- **Fórmula:** `SUM(interactions_total) / SUM(reach_total)`
- **Source type:** Raw event aggregation (derivado)
- **Agregación:** SUM(num) / SUM(den) — nunca promedio de rates diarios
- **Status:** Activo
- **Plan:** ✅ vía `engagement_rate_social` (MAX en el mes — constante diaria)

#### Profile Followers

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Total de seguidores en Instagram. A nivel mensual, usamos el último snapshot disponible (fin del período).
- **Fórmula:** `MAX(profile_followers)` en el período
- **Tabla:** `s__brand_and_comms__instagram_followers__event`
- **Filtros:** `status = 'ok'`
- **Agregación:** MAX
- **Status:** Activo
- **Gotchas:** **Filtrar `status = 'ok'`** — excluye datos en revisión (`review`) o duplicados (`review_dup`)

#### Net New Followers

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Saldo neto de nuevos seguidores en el período. **Ya viene neto** en la columna `new_followers` (nuevos − unfollowers). Puede ser negativo.
- **Definición (schema):** *"Number of new followers gained on the given date (can be negative if more users unfollowed than followed)"*
- **Fórmula:** `SUM(new_followers)`
- **Status:** Activo
- **Gotchas:** No sumar con `unfollowers` — ya está neto

#### Unfollowers

- **Dominio · Subdominio:** Brand · Social
- **Definición (business):** Total de unfollows en el período.
- **Fórmula:** `SUM(unfollowers)`
- **Status:** Activo

---

## 5. KPIs — Acquisition {#5-kpis--acquisition-es}

### 5.1 Funnel (Macro) {#51-funnel-macro-es}

#### Sessions

- **Dominio · Subdominio:** Acquisition · Funnel
- **Definición (business):** Total de sesiones en el sitio marketing-atribuibles, **excluyendo sesiones "login-only"** (el usuario solo se logueó, no navegó). Viene de GA4.
- **Definición (schema):** *"Sum of `distinct_session_count` where `only_login_session = 0`. Null for future dates; 0 when no sessions observed."*
- **Fórmula:** `SUM(effective_total_sessions)`
- **Source type:** Data Product (DP2)
- **Columnas:** real `effective_total_sessions` · plan **NULL hoy** (cols reservadas) · forecast `forecast_total_sessions`
- **Agregación:** SUM
- **Status:** Activo (sin plan)
- **Gotchas:** GA4 reescribe datos hasta 5 días después — el DP rehace los últimos 5 días cada corrida; **sin plan hoy** — attainment % no disponible
- **Related KPIs:** Bounced Sessions, Total Users, Organic Users, CVR Session→Trial

#### Bounced Sessions

- **Dominio · Subdominio:** Acquisition · Funnel (Quality)
- **Definición (business):** Sesiones que rebotaron — sesiones en las que el usuario no engagó (no hizo interacción significativa).
- **Definición (schema):** *"Sum of `distinct_session_count` where `only_login_session = 0` AND `session_status != 'Engaged'`. Null for future dates."*
- **Fórmula:** `SUM(effective_bounced_sessions)`
- **Source type:** Data Product (DP2)
- **Status:** Activo (sin plan)

#### Total Users

- **Dominio · Subdominio:** Acquisition · Funnel
- **Definición (business):** Usuarios únicos en el período (excluyendo login-only).
- **Fórmula:** `SUM(effective_total_users)`
- **Source type:** Data Product (DP2)
- **Status:** Activo (sin plan)

#### Organic Users

- **Dominio · Subdominio:** Acquisition · Funnel
- **Definición (business):** Usuarios únicos provenientes de canales orgánicos.
- **Fórmula:** `SUM(effective_organic_users)`
- **Source type:** Data Product (DP2)
- **Status:** Activo

#### Avg Pageviews per Session

- **Dominio · Subdominio:** Acquisition · Funnel (Quality)
- **Definición (business):** Profundidad de navegación — promedio de pageviews por sesión. **Session-weighted**: días con más sesiones pesan más.
- **Fórmula:** `SUM(effective_avg_pageviews × effective_total_sessions) / SUM(effective_total_sessions)`
- **Source type:** Data Product (DP2)
- **Agregación:** Session-weighted average (ver §0.6)
- **Status:** Activo (sin plan)

#### Avg Session Duration

- **Dominio · Subdominio:** Acquisition · Funnel (Quality)
- **Definición (business):** Duración promedio de la sesión. Session-weighted.
- **Fórmula:** `SUM(effective_avg_session_duration × effective_total_sessions) / SUM(effective_total_sessions)`
- **Source type:** Data Product (DP2)
- **Agregación:** Session-weighted average
- **Status:** Activo (sin plan)

#### Trials

- **Dominio · Subdominio:** Acquisition · Funnel
- **Definición (business):** Nuevos trials (registros free) atribuidos a marketing por el modelo **mean-click**. Contados por la **fecha de creación de la tienda**. Excluye tiendas bloqueadas.
- **Definición (schema):** *"Sum of `trials_mean_click` by `store_created_date` at the model grain. 0 if none."*
- **Fórmula:** `SUM(effective_trials)`
- **Source type:** Data Product (DP1)
- **Columnas:** real `effective_trials` · plan `expected_monthly_trials` · forecast `forecast_trials`
- **Status:** Activo
- **Gotchas:** Antes de 2026-01-01: grain (fecha × país × source × BU). Desde 2026-01-01: agrega subteam
- **Related KPIs:** CVR Session→Trial, CVR Trial→NP

#### New Payments (NPs)

- **Dominio · Subdominio:** Acquisition · Funnel
- **Definición (business):** Primeros pagos atribuidos a marketing por el modelo mean-click, contados por la **fecha del primer pago** del comerciante. Excluye tiendas bloqueadas.
- **Definición (schema):** *"Sum of `trials_mean_click` bucketed by `first_payment_date`. 0 if none."*
- **Fórmula:** `SUM(effective_new_payments)`
- **Source type:** Data Product (DP1)
- **Status:** Activo
- **Gotchas:** Distinta de `payment_created_at` (que cuenta por fecha de creación del pago); trial y NP del mismo comerciante pueden caer en meses diferentes
- **Related KPIs:** Payment Created At, First Payments (Company Metrics), CVR Trial→NP

#### Payment Created At

- **Dominio · Subdominio:** Acquisition · Funnel (Alt. Attribution)
- **Definición (business):** Pagos contados por la **fecha de creación del pago** (no por la fecha del trial). Métrica alternativa para análisis temporales más ajustados.
- **Fórmula:** `SUM(effective_payment_created_at)`
- **Source type:** Data Product (DP1)
- **Status:** Activo

#### New Sellers

- **Dominio · Subdominio:** Acquisition · Funnel · Company Metrics
- **Definición (business):** Nuevos sellers atribuidos a marketing, contados por la fecha en que se convirtieron en seller — **solo cuando esta fecha es posterior a la fecha del primer pago** (excluye casos en que pago y primera venta ocurren el mismo día).
- **Definición (schema):** *"Sum of `trials_mean_click` bucketed by `first_seller_date` where `first_seller_date > first_payment_date`. 0 if none."*
- **Fórmula:** `SUM(effective_new_sellers)`
- **Source type:** Data Product (DP1)
- **Status:** Activo
- **Gotchas:** Distinta de `effective_new_seller_created_at` (que usa el path `first_seller_at`)

#### New Seller Created At

- **Dominio · Subdominio:** Acquisition · Funnel (Alt. Attribution)
- **Definición (business):** Nuevos sellers contados por el path `first_seller_at` — atribución alternativa, distinta de New Sellers.
- **Fórmula:** `SUM(effective_new_seller_created_at)`
- **Source type:** Data Product (DP1)
- **Status:** Activo

#### QLs (Qualified Leads)

- **Dominio · Subdominio:** Acquisition · Funnel
- **Definición (business):** Leads calificados atribuidos a marketing por el modelo mean-click. Excluye tiendas bloqueadas.
- **Fórmula:** `SUM(effective_qls)`
- **Source type:** Data Product (DP1)
- **Status:** Activo (con plan)

### 5.2 Funnel Efficiency (CVRs) {#52-funnel-efficiency-cvrs-es}

#### CVR Session → Trial

- **Dominio · Subdominio:** Acquisition · Funnel Efficiency
- **Definición (business):** Conversión de sesión en trial — qué % de las sesiones se convierte en registro.
- **Fórmula:** `SUM(effective_trials) / SUM(effective_total_sessions)`
- **Source type:** Derivado (cross-DP: DP1 + DP2)
- **Agregación:** SUM(num) / SUM(den)
- **Status:** Activo
- **Gotchas:** **Cross-DP** — garantizar mismos filtros (country, BU, date, source) en ambos lados; DP2 excluye sesiones login-only; DP1 excluye tiendas bloqueadas — poblaciones no 100% alineadas

#### CVR Trial → NP

- **Dominio · Subdominio:** Acquisition · Funnel Efficiency
- **Definición (business):** Conversión de trial en new payment — qué % de los trials se vuelve pagador.
- **Fórmula:** `SUM(effective_new_payments) / SUM(effective_trials)`
- **Source type:** Derivado (DP1)
- **Agregación:** SUM(num) / SUM(den)
- **Status:** Activo
- **Gotchas:** **Mismatch temporal:** NPs del mes X pueden venir de Trials del mes X-1 (o anterior). Para análisis por cohorte, usar `payment_created_at` cruzado con `new_seller_created_at`

### 5.3 Investment (CAC, Spend) ⚠️ {#53-investment-cac-spend-es}

#### Spend (Marketing Investment)

- **Dominio · Subdominio:** Acquisition · Investment
- **Definición (business):** Inversión total en medios en el período. No existe en DP actual.
- **Source type:** ⚠️ Bloqueado (DP6 — Marketing Expenses)
- **Status:** ⚠️ Bloqueado

#### CAC (Cost per Acquisition)

- **Dominio · Subdominio:** Acquisition · Investment
- **Definición (business):** Costo de adquisición por nuevo cliente pagador.
- **Fórmula:** `Spend / SUM(effective_new_payments)`
- **Source type:** ⚠️ Bloqueado (depende de DP6)
- **Status:** ⚠️ Bloqueado

### 5.4 By Source / Lever (jerarquía de 4 niveles) {#54-by-source--lever-es}

Los KPIs de funnel (Sessions, Trials, NPs, New Sellers, QLs, CVRs) pueden abrirse en cualquiera de los 4 niveles de `mkt_source` definidos en **§3.4**:

- **Nivel 1** (16 sources raw) — análisis operacionales granulares
- **Nivel 2** (8 sources, con Low Volume) — estándar para tablas/charts de reportes
- **Nivel 3** (4 categorías — Performance · Organic · Indirect · Low Volume) — mecánica de adquisición
- **Nivel 4** (Branded · Non-Branded) — narrativa ejecutiva

Filtrar siempre por **`mkt_source`** (no `plan_mkt_source_ops`). Los niveles 2-4 son derivados vía CASE/mapping en el SELECT — ver snippet en §9.4.

- **Sessions por nivel:** DP2 — sin plan hoy
- **Trials / NPs / QLs por nivel:** DP1 — con plan
- **Spend / CAC por nivel:** ⚠️ Bloqueado (DP6)

**Apertura adicional por ICP:** los KPIs de funnel (Trials, NPs, CVR Trial→NP) también se abren por **`icp`** (ver §2.10) en los MBRs — además de por `mkt_source`. ⚠️ La clasificación por ICP depende de una fuente externa (sin tag de ICP en los DPs hoy).

---

## 6. KPIs — Company Metrics 🟡 {#6-kpis--company-metrics-es}

Todos los KPIs de esta sección están en **CSV placeholder** hasta que **DP5 — Merchant Base** entre en producción. Cuando esté disponible, migrar a queries SQL en el estándar de los demás DPs.

### 6.1 Base Health {#61-base-health-es}

#### Merchant Base

- **Dominio · Subdominio:** Company Metrics · Base Health
- **Definición (business):** Total de comerciantes pagadores activos al fin del período (snapshot EOP/EOM).
- **Source type:** 🟡 CSV Placeholder (futuro: DP5)
- **Tabla placeholder:** `data/net_adds_placeholder.csv`, columna `Merchant Base`
- **Agregación:** valor EOP directo
- **Status:** 🟡 Placeholder
- **Related KPIs:** Net Adds, % Seller

#### Net Adds

- **Dominio · Subdominio:** Company Metrics · Base Health
- **Definición (business):** Saldo neto en la merchant base del período. Diferencia entre inflow (nuevos + reactivaciones) y outflow (churn + downsell), incluyendo ajustes contables.
- **Fórmula:** `first_payments + new_phoenix + old_phoenix − churn_and_downgrade + ajuste`
- **Source type:** 🟡 CSV Placeholder
- **Tabla placeholder:** `data/net_adds_placeholder.csv`, columna `Net Customers`
- **Status:** 🟡 Placeholder
- **Gotchas:** Cuando se publique DP5, migrar a `SUM(effective_net_adds)`

### 6.2 Inflow {#62-inflow-es}

#### First Payments (Company Metrics)

- **Dominio · Subdominio:** Company Metrics · Inflow
- **Definición (business):** Nuevos comerciantes que hicieron el primer pago en el período — inflow nuevo. **Diferencia vs NPs del DP1:** Company Metrics usa la definición de base (no atribuida a marketing); DP1 cuenta solo los marketing-attributed.
- **Fórmula:** `SUM(first_payments)`
- **Source type:** 🟡 CSV Placeholder (futuro: DP5)
- **Status:** 🟡 Placeholder

#### New Phoenix

- **Dominio · Subdominio:** Company Metrics · Inflow
- **Definición (business):** Comerciantes que volvieron a la base vía funnel Phoenix (reactivación reciente).
- **Fórmula:** `SUM(new_phoenix)`
- **Source type:** 🟡 CSV Placeholder
- **Status:** 🟡 Placeholder

#### Old Phoenix

- **Dominio · Subdominio:** Company Metrics · Inflow
- **Definición (business):** Reactivación de comerciantes churned hace más tiempo (long-tail).
- **Fórmula:** `SUM(old_phoenix)`
- **Source type:** 🟡 CSV Placeholder
- **Status:** 🟡 Placeholder

#### Ajuste

- **Dominio · Subdominio:** Company Metrics · Inflow (Reconciliation)
- **Definición (business):** Reconciliación contable residual que cierra el Net Adds con la variación real de la Merchant Base.
- **Fórmula:** `SUM(ajuste)`
- **Status:** 🟡 Placeholder
- **Gotchas:** Componente pequeño pero necesario. Verificar con DP5 si este concepto sigue

### 6.3 Outflow {#63-outflow-es}

#### Churns

- **Dominio · Subdominio:** Company Metrics · Outflow
- **Definición (business):** Comerciantes que dejaron de pagar en el período.
- **Fórmula:** `SUM(churns)`
- **Source type:** 🟡 CSV Placeholder (futuro: DP5)
- **Status:** 🟡 Placeholder

#### Downsell to Freemium

- **Dominio · Subdominio:** Company Metrics · Outflow
- **Definición (business):** Comerciantes pagadores que bajaron a plan freemium — outflow no-churn.
- **Fórmula:** `SUM(downsell_freemium)`
- **Status:** 🟡 Placeholder

#### Churn + Downgrade

- **Dominio · Subdominio:** Company Metrics · Outflow
- **Definición (business):** Outflow total — suma de churns + downsell.
- **Fórmula:** `churns + downsell_freemium`
- **Status:** 🟡 Placeholder

#### Churn Rate

- **Dominio · Subdominio:** Company Metrics · Outflow
- **Definición (business):** % de churn sobre la base inicial del período.
- **Fórmula:** `churns / merchant_base_t-1`
- **Source type:** Derivado (CSV)
- **Agregación:** SUM(num) / SUM(den)
- **Status:** 🟡 Placeholder

---

## 7. KPIs — Financial {#7-kpis--financial-es}

### 7.1 Volume {#71-volume-es}

Los KPIs de GMV vienen del **DP4 — GMV (Finance Segments)**. Existen 4 variantes de "GMV" en el DP — cada una con 3 versiones de moneda:

| Variante | Significado | ¿Aditivo? |
|---|---|---|
| **on_platform** ⭐ | GMV transaccionado dentro de la plataforma (tienda online) — incluye POS | ✅ |
| **off_platform** | GMV vía sistemas de pago externos (canales fuera de la plataforma) | ✅ (pero residual) |
| **pos** | GMV vía PDV físico (Point of Sale) | ⚠️ **Subset de on_platform — no sumar** |
| **total** | `on_platform + off_platform` | ✅ |

⭐ **Recomendación:** usar **`on_platform`** como GMV principal en los reportes. Off-platform es despreciable (<1% del total en todos los países observados en Mar/26) — la diferencia entre `on_platform` y `total` es estadísticamente irrelevante. POS es parte de on-platform y relevante en CL/CO/MX (17-26% del on-platform) — exhibir por separado donde tenga sentido.

Versiones de moneda:
- **LC (Local Currency)** — moneda local (ARS, BRL, MXN, etc.)
- **USD (source-runtime)** — USD convertido al momento del procesamiento
- **Finance USD** — USD convertido con FX promedio YTD acumulado (preferido para Finance/FP&A)

#### GMV (Total, LC)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** Gross Merchandise Value total (on-platform + off-platform) en moneda local.
- **Fórmula:** `SUM(effective_gmv_total_lc)`
- **Source type:** Data Product (DP4)
- **Tabla:** snapshot mensual — `g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly`
- **Status:** Activo
- **Gotchas:** No sumar POS (POS es subset de on_platform — sumar genera double-count)

#### GMV (Total, USD)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** GMV total en USD convertido al momento del procesamiento (source-runtime).
- **Fórmula:** `SUM(effective_gmv_total_usd)`
- **Source type:** Data Product (DP4)
- **Status:** Activo

#### GMV (Total, Finance USD)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** GMV total en USD convertido con FX promedio YTD acumulado — versión preferida para Finance/FP&A.
- **Fórmula:** `SUM(effective_gmv_total_finance_usd)`
- **Source type:** Data Product (DP4)
- **Status:** Activo

#### GMV (On-Platform, sin POS)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** GMV solo de la plataforma online, excluyendo POS — comparable con la métrica histórica de "GMV de la tienda".
- **Fórmula:** `SUM(effective_gmv_on_platform_lc) − SUM(effective_gmv_pos_lc)` (LC), o `_usd` / `_finance_usd`
- **Plan:** `expected_monthly_gmv_on_platform_without_pos_lc` / `_finance_usd`
- **Source type:** Data Product (DP4)
- **Status:** Activo

#### GMV (POS)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** GMV vía PDV físico. Subset de on_platform.
- **Fórmula:** `SUM(effective_gmv_pos_lc)` / `_usd` / `_finance_usd`
- **Plan:** `expected_monthly_gmv_pos_lc` / `_finance_usd`
- **Source type:** Data Product (DP4)
- **Status:** Activo

#### Orders (Total)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** Volumen total de transacciones (órdenes pagadas) — on_platform + off_platform.
- **Fórmula:** `SUM(effective_orders_total)`
- **Plan:** solo para `on_platform_without_pos` y `pos` por separado
- **Source type:** Data Product (DP4)
- **Status:** Activo

#### Avg Ticket (Total)

- **Dominio · Subdominio:** Financial · Volume
- **Definición (business):** Ticket promedio = GMV / Orders del período.
- **Fórmula:** `SUM(effective_gmv_total_lc) / SUM(effective_orders_total)` (calcular el ratio, no sumar `effective_avg_ticket_total_lc`)
- **Source type:** Data Product (DP4)
- **Agregación:** SUM(num) / SUM(den) — no el promedio del ratio diario
- **Status:** Activo

### 7.2 Productivity {#72-productivity-es}

#### % Seller

- **Dominio · Subdominio:** Financial · Productivity (también Company Metrics)
- **Definición (business):** % de la merchant base clasificada como Seller — comerciante con ≥7 ventas en los últimos 90 días (ventana móvil).
- **Fórmula:** `sellers_count / merchant_base_eop`
- **Source type:** ⚠️ Bloqueado (hasta DP5 — Merchant Base)
- **Status:** ⚠️ Bloqueado

#### GMV per Seller

- **Dominio · Subdominio:** Financial · Productivity
- **Definición (business):** Productividad media del seller — GMV generado por seller activo.
- **Fórmula:** `GMV (DP4) / (Merchant Base EOP × % Seller)` *(numerador disponible; denominador depende de DP5)*
- **Source type:** ⚠️ Bloqueado (numerador OK vía DP4; denominador bloqueado hasta DP5)
- **Status:** ⚠️ Bloqueado

---

## 8. Apéndice — Notas técnicas

### 8.1 Forecast — comportamiento

El `forecast_*` en DPs es proyección rolling average anclada: 90d en días normales, 180d en special days. **Nunca lee otros forecasts** — solo `effective_*` reales. Para fechas futuras sin plan, `forecast_*` viene `NULL`. Fallbacks: 180d sin filtro → 365d sin filtro → 0.

### 8.2 Refresh y latencia

| Fuente | Refresh | Latencia |
|---|---|---|
| DP1 (meanclick) | Diario 10am BA | T-1 |
| DP2 (GA4) | Diario 10am BA | T-1 + reescribe últimos 5 días |
| DP3 (GSC + KWP) | Diario 10am BA | T-1 |
| Raw events B&C | Variable (por evento) | — |

### 8.3 Ventana histórica estándar

Charts históricos usan histórico móvil de **24 meses** terminando en el período corriente.

### 8.4 Anti-patterns

Errores comunes a evitar — extraídos de las gotchas de los schemas. En cada fila: ❌ **no hacer** vs ✅ **hacer correctamente** y el **porqué**.

| ❌ No hacer | ✅ Hacer | Por qué |
|---|---|---|
| `AVG(effective_branded_ctr_sc_daily)` | `SUM(clicks) / SUM(searches)` | El promedio de ratios diarios está sesgado por días con poco volumen |
| `AVG(effective_branded_share_tiendanube_kwp_daily)` | `SUM(numerador) / SUM(denominador)` | Misma razón. Share es %, no aditivo |
| `AVG(engagement_rate_diario)` | `SUM(interactions_total) / SUM(reach_total)` | Idem |
| `AVG(effective_avg_pageviews)` | `SUM(effective_avg_pageviews × effective_total_sessions) / SUM(effective_total_sessions)` | Avg de avg sin peso por sesiones distorsiona — es session-weighted |
| `SUM(reach_organic + reach_paid_total + reach_collab_third_party)` | `SUM(reach_total)` | La versión "manual" pierde el bucket `manual_non_classified` (son 4 componentes, no 3) |
| `MAX(profile_followers)` sin filtro de `status` | `MAX(profile_followers) WHERE status = 'ok'` | Incluye datos en revisión — calidad dudosa |
| `SUM(new_followers) + SUM(unfollowers)` para calcular el saldo | `SUM(new_followers)` | `new_followers` ya es neto. Puede ser negativo |
| `SUM(reach)` en PR sin `COALESCE` | `SUM(COALESCE(reach, 0))` | Valores inválidos se vuelven NULL (no 0) en el schema del clipping |
| Buscar CTR en KWP | Usar SC | KWP no tiene clicks, por lo tanto no tiene CTR |
| `SUM(branded_searches_sc) + SUM(branded_searches_kwp)` | Elegir una única fuente | SC y KWP miden universos diferentes — sumar es double-count |
| Comparar `effective_new_sellers` con `effective_new_seller_created_at` sin distinguir | Elegir una y fijar la definición | Son paths de atribución distintos |
| Comparar `effective_new_payments` con `effective_payment_created_at` sin distinguir | Elegir una | Definidos por buckets temporales diferentes |
| Calcular CVR Trial→NP en el mismo mes sin nota | Mencionar el **mismatch temporal** en el análisis | NPs del mes X pueden venir de Trials del mes X-1 |
| `WHERE business_unit = 'SMB'` sin entender qué se excluye | Identificar SMB vs MM según [§2.2](#22-business_unit), aplicar el filtro conscientemente | Filtros automáticos sin contexto pierden claridad |
| Usar `forecast_*` para análisis de meses pasados como si fuera real | Usar `effective_*` para el pasado; `forecast_*` solo para proyección futura | Forecast nunca sustituye al real |
| Cross-DP (DP1 + DP2) sin alinear filtros | Garantizar `country`, `business_unit`, `mkt_source`, `full_date` consistentes | Poblaciones desalineadas → ratio falso |
| `GROUP BY plan_mkt_source_ops` para breakdown por lever | `GROUP BY mkt_source` | `plan_mkt_source_ops` es NULL para attribution-only. `mkt_source` es canónica |
| Mezclar niveles de la jerarquía de `mkt_source` en el mismo chart | Elegir **un único nivel** (1, 2, 3 o 4) y mantener consistencia | Double-count y confusión de granularidades |
| Tratar "Low Volume" como "Others" en el Nivel 1 | Low Volume solo existe a partir del Nivel 2 | Conceptos distintos |
| `SUM(effective_gmv_on_platform) + SUM(effective_gmv_pos)` para "GMV total" | Usar `effective_gmv_total` o `effective_gmv_on_platform − effective_gmv_pos` | POS es subset de on_platform — sumar es double-count |
| `AVG(effective_avg_ticket_total_lc)` | `SUM(effective_gmv_total_lc) / SUM(effective_orders_total)` | Avg ticket es ratio — recalcular por componentes |
| Usar daily DP para análisis de mes cerrado | Usar el snapshot mensual (`*__agg_snapshot_monthly`) | Snapshot ya está agregado, congelado y refleja el estado de cierre |

---

## 9. Cookbook — SQL snippets {#9-cookbook--sql-snippets-es}

Snippets listos para los principales KPIs. Reemplazar los parámetros `:country`, `:business_unit`, `:month_label` (formato `'YYYY-MM'`) según el análisis.

> ⚠️ Los snippets usan `business_unit = 'SMB'`. Para análisis de MM, ajustar — ver [§2.2](#22-business_unit).

### 9.1 Brand — Search Presence (DP3)

```sql
-- Branded Searches (SC) — Real + Plan, mes de referencia
SELECT
  SUM(effective_branded_searches_sc_daily)       AS branded_searches_real,
  SUM(expected_monthly_branded_searches_sc_daily) / COUNT(DISTINCT full_date) AS branded_searches_plan,
  SUM(forecast_branded_searches_sc_daily)        AS branded_searches_forecast
FROM data_products_prd.data_marketing.g__general__gsc_kwp_searches_budget_forecast__agg_daily
WHERE country       = :country
  AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- Branded CTR % — SUM(num)/SUM(den) sobre el período
SELECT
  SUM(effective_branded_clicks_sc_daily)
    / NULLIF(SUM(effective_branded_searches_sc_daily), 0) AS branded_ctr
FROM data_products_prd.data_marketing.g__general__gsc_kwp_searches_budget_forecast__agg_daily
WHERE country = :country AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- Share of Market — Real + Plan
SELECT
  SUM(effective_branded_searches_tiendanube_kwp_daily)
    / NULLIF(SUM(effective_d2c_searches_kwp_daily), 0)              AS som_real,
  MAX(expected_monthly_branded_share_tiendanube_kwp_daily)          AS som_plan
FROM data_products_prd.data_marketing.g__general__gsc_kwp_searches_budget_forecast__agg_daily
WHERE country = :country AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- Total Market Search Volume + descomposición branded / non-branded
SELECT
  SUM(effective_total_market_searches_kwp_daily)            AS total_market,
  SUM(effective_branded_searches_tiendanube_kwp_daily)      AS branded,
  SUM(effective_nonbranded_searches_kwp_daily)              AS nonbranded
FROM data_products_prd.data_marketing.g__general__gsc_kwp_searches_budget_forecast__agg_daily
WHERE country = :country AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;
```

### 9.2 Brand — PR (Clipping)

```sql
-- PR — publicaciones por tier + reach + proactive
SELECT
  COUNT(*)                                                                AS total_publications,
  SUM(CASE WHEN golden_media_flag = TRUE THEN 1 ELSE 0 END)               AS gold,
  SUM(CASE WHEN tier = 1 AND golden_media_flag = FALSE THEN 1 ELSE 0 END) AS tier1,
  SUM(CASE WHEN tier = 2 THEN 1 ELSE 0 END)                               AS tier2,
  SUM(CASE WHEN origin_type = 'Original' THEN 1 ELSE 0 END)               AS proactive,
  SUM(COALESCE(reach, 0))                                                 AS total_reach
FROM data_products_prd.data_marketing.s__brand_and_comms__clipping__event
WHERE country    = :country
  AND date_month = :month_label;
```

### 9.3 Brand — Social

```sql
-- Instagram Insights — reach por bucket + interactions + engagement rate
SELECT
  SUM(reach_total)                                          AS reach_total,
  SUM(reach_organic)                                        AS reach_organic,
  SUM(reach_paid_total)                                     AS reach_paid,
  SUM(reach_collab_third_party)                             AS reach_collab,
  SUM(interactions_total)                                   AS interactions_total,
  SUM(saves_total)                                          AS saves,
  SUM(shares_total)                                         AS shares,
  SUM(interactions_total) / NULLIF(SUM(reach_total), 0)     AS engagement_rate
FROM data_products_prd.data_marketing.s__brand_and_comms__social_insights__event
WHERE country    = :country
  AND date_month = :month_label;

-- Instagram Followers — snapshot fin de mes + net new
SELECT
  MAX(profile_followers) AS profile_followers_eom,
  SUM(new_followers)     AS net_new_followers,
  SUM(unfollowers)       AS unfollowers
FROM data_products_prd.data_marketing.s__brand_and_comms__instagram_followers__event
WHERE country    = :country
  AND date_month = :month_label
  AND status     = 'ok';

-- Plans B&C (PR + Social)
SELECT
  SUM(publicaciones_totales_pr)  AS pr_total_plan,
  SUM(publicaciones_t1_pr)       AS pr_tier1_plan,
  SUM(reach_social)              AS social_reach_plan,
  MAX(engagement_rate_social)    AS social_engagement_plan
FROM data_products_prd.data_marketing.s__brand_and_comms__goals__event
WHERE country    = :country
  AND date_month = :month_label;
```

### 9.4 Acquisition — Funnel (DP1 + DP2)

```sql
-- Macro Funnel: Trials, NPs, QLs + plan
SELECT
  SUM(effective_trials)              AS trials_real,
  SUM(expected_monthly_trials)
    / COUNT(DISTINCT full_date)      AS trials_plan,
  SUM(effective_new_payments)        AS np_real,
  SUM(expected_monthly_new_payments)
    / COUNT(DISTINCT full_date)      AS np_plan,
  SUM(effective_qls)                 AS qls_real,
  SUM(effective_new_sellers)         AS new_sellers_real
FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_daily
WHERE country       = :country
  AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- Funnel por mkt_source — Nivel 1 (16 sources raw, canónico)
SELECT
  mkt_source                         AS source_l1,
  SUM(effective_trials)              AS trials,
  SUM(effective_new_payments)        AS nps,
  SUM(effective_qls)                 AS qls
FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_daily
WHERE country       = :country
  AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label
GROUP BY mkt_source
ORDER BY nps DESC;

-- Funnel por la JERARQUÍA de mkt_source (Niveles 2, 3, 4 — ver §3.4)
WITH mapped AS (
  SELECT
    mkt_source AS source_l1,
    -- Nivel 2: Low Volume consolida sources poco significativas
    CASE
      WHEN mkt_source IN ('Brand & Comms','Eea','Enp','Mandae','Mid-market',
                          'Nurturing','Others','Product Marketing','Store Referral')
        THEN 'Low Volume'
      ELSE mkt_source
    END AS source_l2,
    -- Nivel 3: mecánica de adquisición
    CASE
      WHEN mkt_source IN ('Performance Brand','Performance No Brand')      THEN 'Performance'
      WHEN mkt_source IN ('Direct','Organic','Organic Growth')              THEN 'Organic'
      WHEN mkt_source IN ('Affiliates','Partners')                          THEN 'Indirect'
      ELSE 'Low Volume'
    END AS source_l3,
    -- Nivel 4: relación con la marca
    CASE
      WHEN mkt_source IN ('Direct','Organic','Performance Brand')           THEN 'Branded'
      ELSE 'Non-Branded'
    END AS source_l4,
    effective_trials,
    effective_new_payments,
    effective_qls
  FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_daily
  WHERE country       = :country
    AND business_unit = :business_unit
    AND date_format(full_date, 'yyyy-MM') = :month_label
)
SELECT
  source_l2,  -- cambiar a source_l3 o source_l4 según el análisis
  SUM(effective_trials)        AS trials,
  SUM(effective_new_payments)  AS nps,
  SUM(effective_qls)           AS qls
FROM mapped
GROUP BY source_l2
ORDER BY nps DESC;

-- CVR Trial→NP en el período
SELECT
  SUM(effective_new_payments)
    / NULLIF(SUM(effective_trials), 0) AS cvr_trial_to_np
FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_daily
WHERE country = :country AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- Sessions (DP2) + Bounced + Users
SELECT
  SUM(effective_total_sessions)      AS sessions,
  SUM(effective_bounced_sessions)    AS bounced,
  SUM(effective_total_users)         AS users,
  SUM(effective_organic_users)       AS organic_users
FROM data_products_prd.data_marketing.g__general__ga4_sessions_budget_forecast__agg_daily
WHERE country = :country AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- Avg Pageviews / Avg Session Duration — session-weighted
SELECT
  SUM(effective_avg_pageviews * effective_total_sessions)
    / NULLIF(SUM(effective_total_sessions), 0) AS avg_pageviews,
  SUM(effective_avg_session_duration * effective_total_sessions)
    / NULLIF(SUM(effective_total_sessions), 0) AS avg_session_duration
FROM data_products_prd.data_marketing.g__general__ga4_sessions_budget_forecast__agg_daily
WHERE country = :country AND business_unit = :business_unit
  AND date_format(full_date, 'yyyy-MM') = :month_label;

-- CVR Session→Trial (cross-DP)
SELECT
  (SELECT SUM(effective_trials)
   FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_daily
   WHERE country = :country AND business_unit = :business_unit
     AND date_format(full_date, 'yyyy-MM') = :month_label
  ) / NULLIF(
    (SELECT SUM(effective_total_sessions)
     FROM data_products_prd.data_marketing.g__general__ga4_sessions_budget_forecast__agg_daily
     WHERE country = :country AND business_unit = :business_unit
       AND date_format(full_date, 'yyyy-MM') = :month_label
    ), 0
  ) AS cvr_session_to_trial;
```

### 9.5 Financial — GMV & Orders (DP4)

```sql
-- GMV + Orders + Avg Ticket — mes cerrado (usando SNAPSHOT mensual)
SELECT
  SUM(effective_gmv_total_lc)            AS gmv_total_lc,
  SUM(effective_gmv_total_usd)           AS gmv_total_usd,
  SUM(effective_gmv_total_finance_usd)   AS gmv_total_finance_usd,
  SUM(effective_gmv_on_platform_lc - effective_gmv_pos_lc) AS gmv_on_platform_without_pos_lc,
  SUM(effective_gmv_pos_lc)              AS gmv_pos_lc,
  SUM(effective_orders_total)            AS orders_total,
  SUM(effective_gmv_total_lc) / NULLIF(SUM(effective_orders_total), 0) AS avg_ticket_total_lc,
  SUM(expected_monthly_gmv_on_platform_without_pos_lc) AS gmv_on_platform_plan_lc,
  SUM(expected_monthly_gmv_pos_lc)       AS gmv_pos_plan_lc
FROM data_products_prd.data_marketing.g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly
WHERE country       = :country
  AND business_unit = :business_unit
  AND month_label   = :month_label;

-- GMV por finance segment
SELECT
  finance_segment,
  SUM(effective_gmv_total_finance_usd) AS gmv_finance_usd,
  SUM(effective_orders_total)          AS orders
FROM data_products_prd.data_marketing.g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly
WHERE country = :country AND business_unit = :business_unit
  AND month_label = :month_label
GROUP BY finance_segment
ORDER BY gmv_finance_usd DESC;
```

### 9.6 Snapshot mensual — patrón de consumo

Cuando el mes está **cerrado** (después del día 4 del mes siguiente), los 4 DPs tienen snapshots listos. Para análisis de período cerrado, usar la tabla snapshot directamente:

```sql
-- Patrón: 1 fila por mes × país × dimensiones — sin necesidad de SUM temporal
SELECT
  month_label,
  country,
  mkt_source,
  effective_trials,
  effective_new_payments,
  expected_monthly_trials,
  expected_monthly_new_payments,
  forecast_trials
FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_snapshot_monthly
WHERE country     = :country
  AND business_unit = :business_unit
  AND month_label = :month_label;
```

Ventajas vs daily:
- Sin `GROUP BY` temporal — el mes ya está agregado
- Solo 3 familias de columnas (más simple)
- Estado **congelado** — no sufre cambios retroactivos
- Particionado por `snapshot_month` (`yyyyMM`)

### 9.7 Histórico 24 meses (template genérico)

```sql
-- Patrón para charts históricos de 24 meses, terminando en :month_label
WITH bounds AS (
  SELECT
    add_months(to_date(:month_label || '-01'), -23) AS history_start,
    last_day(to_date(:month_label || '-01'))         AS history_end
)
SELECT
  date_format(full_date, 'yyyy-MM') AS month_label,
  SUM(effective_trials)             AS trials  -- reemplazar por el KPI deseado
FROM data_products_prd.data_marketing.g__general__meanclick_budget_forecast__agg_daily, bounds
WHERE country       = :country
  AND business_unit = :business_unit
  AND full_date BETWEEN bounds.history_start AND bounds.history_end
GROUP BY 1
ORDER BY 1;
```

---

## 10. Backlog {#10-backlog-es}

Ítems identificados como pendiente de catalogación, definición o validación. No bloquean el uso actual del catálogo, pero deben ser abordados en versiones futuras.

| # | Ítem | Dominio | Notas |
|---|---|---|---|
| B1 | **`finance_segment` (DP4)** | Financial | DP4 abre GMV en 7 buckets de finance segment (FP&A). Por ahora **no usamos este breakdown** en el MBR — sumamos todos los segments. Cuando FP&A consolide los 7 buckets, retomar. |
| B2 | **Plans para GMV total / off-platform** | Financial | DP4 tiene plan solo para `on_platform_without_pos` y `pos`. Verificar con Ops cómo presentar "GMV vs Plan" en el MBR. |
| B3 | **Sources extras de `mkt_source`** | Acquisition | 8 sources caen hoy en "Low Volume". Validar con Ops si alguna merece subir al Nivel 2. |
| B4 | **`forecast_new_sellers` en DP1** | Acquisition | Columna `forecast_new_sellers` no existe en DP1. Reportar al equipo de Data. |
| B5 | **Inconsistencia de naming en DP1** | Acquisition | `effective_new_payments` × `forecast_payments` (sin "new"). Reportar al equipo de Data. |
| B6 | **Goals B&C (Branded Searches + Market Share)** | Brand | Validar con Beto si el archivo de Goals B&C debe usarse, o si la fuente canónica es el snapshot DP3. |
| B7 | **SOV AI Platforms** | Brand | Hoy Manual. Investigar si hay fuente automatizable. |
| B8 | **DP5 — Merchant Base** | Company Metrics | Aguardar publicación. Migrar Net Adds, Merchant Base, Churn, Phoenix, Ajuste, Downsell de CSV a SQL. |
| B9 | **DP6 — Marketing Expenses & Headcount** | Acquisition · Investment | Aguardar publicación. Desbloquea Spend, CAC. |
| B10 | **GMV per Seller + % Seller** | Financial · Productivity | Bloqueado hasta DP5 (denominador). Numerador ya disponible vía DP4. |
| B11 | **Versiones EN y ES del catálogo** | Documento | Después de estabilizar PT, traducir. |
| B12 | **Fuente de clasificación por ICP** | Acquisition | La dimensión `icp` (§2.10) no tiene tag por comerciante en ningún DP. La apertura por ICP se hace hoy con fuente externa (planilla). Definir fuente canónica y mapear nomenclatura antigua (ICP 1-4 + Fallback) al framework nuevo (§1.2). |

---

## 11. Changelog {#11-changelog-es}

Para el historial completo de cambios, ver el [Changelog en la versión PT-BR](#11-changelog).

---

# 🇧🇷 Versão PT-BR

## Índice

0. [Convenções gerais](#0-convenções-gerais)
1. [Glossário de termos](#1-glossário-de-termos)
2. [Dicionário de dimensões](#2-dicionário-de-dimensões)
3. [Tabelas de referência](#3-tabelas-de-referência)
4. [KPIs — Brand](#4-kpis--brand)
   - 4.1 [Search Presence](#41-search-presence)
   - 4.2 [PR (Public Relations)](#42-pr-public-relations)
   - 4.3 [Social (Instagram)](#43-social-instagram)
5. [KPIs — Acquisition](#5-kpis--acquisition)
   - 5.1 [Funnel (Macro)](#51-funnel-macro)
   - 5.2 [Funnel Efficiency (CVRs)](#52-funnel-efficiency-cvrs)
   - 5.3 [Investment (CAC, Spend)](#53-investment-cac-spend-)
   - 5.4 [By Lever](#54-by-lever)
6. [KPIs — Company Metrics](#6-kpis--company-metrics-)
   - 6.1 [Base Health](#61-base-health)
   - 6.2 [Inflow](#62-inflow)
   - 6.3 [Outflow](#63-outflow)
7. [KPIs — Financial](#7-kpis--financial-)
   - 7.1 [Volume](#71-volume)
   - 7.2 [Productivity](#72-productivity)
8. [Apêndice — Notas técnicas](#8-apêndice--notas-técnicas)
9. [Cookbook — SQL snippets](#9-cookbook--sql-snippets)
10. [Backlog](#10-backlog)
11. [Changelog](#11-changelog)

---

## Visão de pássaro — KPI Matrix

Tabela única com todos os KPIs catalogados, para busca rápida. Ordem: **Company Metrics · Financial · Acquisition · Brand**.

| # | KPI | Domínio · Subdomínio | Fonte | Status |
|---|---|---|---|---|
| 1 | Merchant Base | Company Metrics · Base Health | CSV → DP5 | 🟡 Placeholder |
| 2 | Net Adds | Company Metrics · Base Health | CSV → DP5 | 🟡 Placeholder |
| 3 | First Payments (Company Metrics) | Company Metrics · Inflow | CSV → DP5 | 🟡 Placeholder |
| 4 | New Phoenix | Company Metrics · Inflow | CSV → DP5 | 🟡 Placeholder |
| 5 | Old Phoenix | Company Metrics · Inflow | CSV → DP5 | 🟡 Placeholder |
| 6 | Ajuste | Company Metrics · Inflow (Reconciliation) | CSV → DP5 | 🟡 Placeholder |
| 7 | Churns | Company Metrics · Outflow | CSV → DP5 | 🟡 Placeholder |
| 8 | Downsell to Freemium | Company Metrics · Outflow | CSV → DP5 | 🟡 Placeholder |
| 9 | Churn + Downgrade | Company Metrics · Outflow | derivado | 🟡 Placeholder |
| 10 | Churn Rate | Company Metrics · Outflow | derivado | 🟡 Placeholder |
| 11 | GMV (Total, LC) | Financial · Volume | DP4 | Ativo |
| 12 | GMV (Total, USD) | Financial · Volume | DP4 | Ativo |
| 13 | GMV (Total, Finance USD) | Financial · Volume | DP4 | Ativo |
| 14 | GMV (On-Platform sem POS) | Financial · Volume | DP4 | Ativo |
| 15 | GMV (POS) | Financial · Volume | DP4 | Ativo |
| 16 | Orders (Total) | Financial · Volume | DP4 | Ativo |
| 17 | Avg Ticket (Total) | Financial · Volume | DP4 | Ativo |
| 18 | % Seller | Financial · Productivity | DP5 | ⚠️ Bloqueado |
| 19 | GMV per Seller | Financial · Productivity | DP4+DP5 | ⚠️ Bloqueado |
| 20 | Sessions | Acquisition · Funnel | DP2 | Ativo |
| 21 | Bounced Sessions | Acquisition · Funnel (Quality) | DP2 | Ativo |
| 22 | Total Users | Acquisition · Funnel | DP2 | Ativo |
| 23 | Organic Users | Acquisition · Funnel | DP2 | Ativo |
| 24 | Avg Pageviews per Session | Acquisition · Funnel (Quality) | DP2 | Ativo |
| 25 | Avg Session Duration | Acquisition · Funnel (Quality) | DP2 | Ativo |
| 26 | Trials | Acquisition · Funnel | DP1 | Ativo |
| 27 | New Payments (NPs) | Acquisition · Funnel | DP1 | Ativo |
| 28 | Payment Created At | Acquisition · Funnel (Alt) | DP1 | Ativo |
| 29 | New Sellers | Acquisition · Funnel | DP1 | Ativo |
| 30 | New Seller Created At | Acquisition · Funnel (Alt) | DP1 | Ativo |
| 31 | QLs (Qualified Leads) | Acquisition · Funnel | DP1 | Ativo |
| 32 | CVR Session → Trial | Acquisition · Funnel Efficiency | DP1+DP2 | Ativo |
| 33 | CVR Trial → NP | Acquisition · Funnel Efficiency | DP1 | Ativo |
| 34 | Spend | Acquisition · Investment | DP6 | ⚠️ Bloqueado |
| 35 | CAC | Acquisition · Investment | derivado | ⚠️ Bloqueado |
| 36 | Branded Searches | Brand · Search Presence | DP3 | Ativo |
| 37 | Branded CTR % | Brand · Search Presence | DP3 | Ativo |
| 38 | Share of Market | Brand · Search Presence | DP3 | Ativo |
| 39 | Share of Market (excl. Wix) | Brand · Search Presence | DP3 | Ativo |
| 40 | Total Market Search Volume | Brand · Search Presence | DP3 | Ativo |
| 41 | SOV AI Platforms | Brand · Search Presence | Manual | 🔵 Manual |
| 42 | Total Publications | Brand · PR | Clipping | Ativo |
| 43 | Gold Media | Brand · PR | Clipping | Ativo |
| 44 | Tier 1 | Brand · PR | Clipping | Ativo |
| 45 | Tier 2 | Brand · PR | Clipping | Ativo |
| 46 | Proactive Publications | Brand · PR | Clipping | Ativo |
| 47 | Total Reach (PR) | Brand · PR | Clipping | Ativo |
| 48 | Total Reach (Social) | Brand · Social | Social Insights | Ativo |
| 49 | Organic Reach | Brand · Social | Social Insights | Ativo |
| 50 | Paid Reach | Brand · Social | Social Insights | Ativo |
| 51 | Collab Reach | Brand · Social | Social Insights | Ativo |
| 52 | Interactions | Brand · Social | Social Insights | Ativo |
| 53 | Saves | Brand · Social | Social Insights | Ativo |
| 54 | Shares | Brand · Social | Social Insights | Ativo |
| 55 | Engagement Rate | Brand · Social | Social Insights | Ativo |
| 56 | Profile Followers | Brand · Social | IG Followers | Ativo |
| 57 | Net New Followers | Brand · Social | IG Followers | Ativo |
| 58 | Unfollowers | Brand · Social | IG Followers | Ativo |

---

## 0. Convenções gerais

### 0.1 Tipos de fonte

| Tipo | Padrão | Como consumir |
|---|---|---|
| **Data Product — Daily** (`*__agg_daily`) | 6 famílias de colunas: `effective_*`, `forecast_*`, `expected_monthly_*`, `ponderation_key_*`, `expected_daily_linear_*`, `expected_daily_weighted_*` | `SUM` ou `MAX` dos dias do período. Para charts intra-mês, análise diária e plan refinado por tipo de dia (linear vs weighted) |
| **Data Product — Snapshot mensal** (`*__agg_snapshot_monthly`) | **3 famílias** de colunas: `effective_*`, `forecast_*`, `expected_monthly_*`. Uma linha por mês fechado | Para análise de meses fechados. Roda **dia 4 do mês seguinte**, append-only, **congela** o mês — mudanças retroativas a montante não refletem |
| **Raw event aggregation** | Tabelas `s__*__event` com dados granulares | A agregação é responsabilidade do consumidor (COUNT, SUM, MAX) |
| **CSV / fonte externa** | Arquivos planos enquanto um DP não existe | Leitura via pandas / planilha |

**Quando usar daily vs snapshot:**
- **Snapshot mensal** — relatórios de meses fechados (MBR, QBR), análises retrospectivas, KPI catalog de plan vs real. Vantagem: 1 linha por mês × dimensão (queries simples, sem agregação temporal).
- **Daily** — charts intra-mês, monitoring diário, análise de tendência. Necessário quando precisa do plan diário (linear/weighted) ou histórico denso.

### 0.2 Status

- **Ativo** — fonte disponível, KPI utilizável hoje
- **🟡 Placeholder** — usando fonte temporária até DP correspondente entrar em produção
- **⚠️ Bloqueado** — KPI definido mas sem fonte disponível; aguardando DP futuro
- **🔵 Manual** — KPI cuja apuração depende de input humano/externo (sem automação possível atualmente)

### 0.3 Formato de cada entrada de KPI

Cada KPI segue este template:

- **Domínio · Subdomínio:** taxonomia funcional (Brand · Search Presence, Acquisition · Funnel, etc.)
- **Definição (business):** narrativa executiva, contém os insights operacionais relevantes do schema (ex: "exclui Next/Evolución")
- **Definição (schema):** citação literal do `comment` da coluna no Databricks (quando aplicável)
- **Fórmula:** expressão lógica
- **Source type / Tabela / Colunas**
- **Agregação:** SUM, MAX, SUM(num)/SUM(den), session-weighted
- **Status:** Ativo / Placeholder / Bloqueado / Manual
- **Gotchas:** alertas importantes — muitos vêm direto do schema
- **Related KPIs:** referência cruzada quando há sobreposição ou variantes

KPIs derivados (CVR, Engagement Rate, CAC) e em placeholder não têm `Definição (schema)` — apenas business.

### 0.4 Comparações temporais padrão

- **Real** — período corrente
- **M-1** — mês anterior
- **YoY** — mesmo mês do ano anterior
- **MoM%** e **YoY%** — variação percentual
- **Plan / Attainment%** — quando o KPI tem `expected_monthly_*`
- **Forecast** — quando o KPI tem `forecast_*`
- **YTD** — Jan até mês corrente
- **Quarter** — meses do trimestre corrente até o mês corrente
- **EOP / EOM** — End of Period / End of Month (snapshot fim do período)

### 0.5 Agregação correta de ratios

**Erro comum:** `AVG(ctr_diario)` ou `AVG(share_diario)` → resultado enviesado por dias com pouco volume.

**Correto:** `SUM(numerador) / SUM(denominador)` para o período.

Aplicável a: **CTR, Branded Share, Marketplace Share, Engagement Rate, CVRs, Churn Rate**.

### 0.6 Agregação correta de averages session-weighted

Para `avg_pageviews` e `avg_session_duration` (DP2), agregar como:

```sql
SUM(effective_avg_pageviews * effective_total_sessions)
  / NULLIF(SUM(effective_total_sessions), 0)
```

(Documentado pelo schema: *"Session-weighted average..."*)

### 0.7 Plans com agregação diferente do SUM

| KPI | Coluna de plan | Agregação |
|---|---|---|
| Branded Share | `expected_monthly_branded_share_tiendanube_kwp_daily` | **MAX** mensal (% não é aditivo) |
| Engagement Rate Social | `engagement_rate_social` | **MAX** mensal (constante diária) |
| Reach Social | `reach_social` | SUM (distribuído por dia) |
| Branded Searches SC | `expected_monthly_branded_searches_sc_daily` | SUM |
| Trials / NPs / QLs / etc. | `expected_monthly_*` | SUM |

---

## 1. Glossário de termos

### 1.1 Conceitos de negócio

| Termo | Definição |
|---|---|
| **Phoenix (New)** | Merchants que retornaram à base via funil Phoenix com janela curta de reativação (reativação recente) |
| **Phoenix (Old)** | Merchants que voltaram à base após churned há mais tempo (long-tail de reativação) |
| **Net Adds** | Saldo líquido na base do período: inflow (novos + reativações) − outflow (churn + downsell) + ajuste contábil |
| **Branded Levers** | Sources de aquisição que operam sobre marca já reconhecida (Nível 4 — Branded): Direct, Organic, Performance Brand. Ver §3.4 |
| **Non-Brand Levers** | Sources que constroem demanda nova (Nível 4 — Non-Branded): Performance No Brand, Organic Growth, Affiliates, Partners, Low Volume. Ver §3.4 |
| **Low Volume** | Agregação de sources individualmente pouco significativas (Nível 2): Brand & Comms, Eea, Enp, Mandae, Mid-market, Nurturing, Others, Product Marketing, Store Referral. Ver §3.4 |
| **Performance (Nível 3)** | Mecânica de aquisição com mídia paga atribuível: Performance Brand + Performance No Brand |
| **Organic (Nível 3)** | Mecânica de aquisição sem mídia paga direta: Direct, Organic, Organic Growth |
| **Indirect (Nível 3)** | Mecânica de aquisição via terceiros: Affiliates, Partners |
| **Seller** | Merchant com ≥7 vendas nos últimos 90 dias (janela móvel). Métrica de "merchant ativo gerando transações" |
| **Non-Seller** | Merchant na base que não atinge o critério de Seller |
| **Mean-click attribution** | Modelo de atribuição em que cada conversão é repartida igualmente entre todos os cliques que a precederam |
| **D2C (Direct-to-Consumer)** | Universo de marcas oficiais de loja própria (Nuvemshop/Tiendanube + competidores oficiais) — denominador de Share of Market |
| **Marketplace** | Categoria distinta de D2C — agrupa marketplaces (Mercado Livre, Amazon, Shopee etc.) |
| **Special Days** | Datas com comportamento atípico de demanda (Black Friday, Cyber, etc.) listadas em `ext__marketing__acquisition__key_dates_by_country` |
| **Trial → Payment lag** | Intervalo temporal entre um trial e o primeiro pagamento — o NP do mês X pode vir do Trial do mês X-1 |

### 1.2 ICPs (Ideal Customer Profile)

Framework de aquisição que segmenta o universo por **atributo do merchant** (não por faixa de GMV). Os 5 segmentos **não somam 100%** do universo — perfis sobrepostos são isolados de propósito para manter cada ICP "limpo".

| Tier | ICP | Nome | Atributo definidor |
|---|---|---|---|
| **Premium** | **ICP 1** | Platform Migrants | Merchants migrando de outra plataforma — esse é o atributo definidor |
| **Premium** | **ICP 2** | Social Sellers | Merchants vendendo primariamente em redes sociais (Instagram, WhatsApp) — esse é o atributo definidor |
| **Premium** | **ICP 3** | Offline Sellers | Merchants saindo de loja física para o digital — economics premium |
| **Mid-Premium** | **ICP 4** | Marketplace Sellers | Marketplace-only (ML, Shopee) — social-only tail isolado para manter ICP 4 limpo |
| **SMBs** | **ICP 5a** | D2C Starters | Empreendedores D2C de primeira viagem — motor de volume do modelo |
| **SMBs** | **ICP 5b** | Affiliates / Dropshippers | Sub-programa Loja Pronta (em descontinuação) + outros affiliates de qualidade inferior |

**Notas:**
- ICPs definidos por **atributo do merchant**, não por faixa de GMV
- Os 5 segmentos não cobrem 100% do universo — sobreposições são deliberadamente excluídas para manter cada ICP "limpo"
- Owner: RevOps / Marketing Ops (verificar fonte de verdade para definições operacionais detalhadas)

### 1.3 Acrônimos

| Sigla | Significado |
|---|---|
| **NP** | New Payment — primeiro pagamento de um novo merchant |
| **NS** | New Seller — novo merchant que virou seller |
| **QL** | Qualified Lead |
| **Trial** | Novo cadastro free (trial iniciado) |
| **CVR** | Conversion Rate |
| **CTR** | Click-Through Rate |
| **SOM** | Share of Market |
| **SOV** | Share of Voice |
| **EOP / EOM** | End of Period / End of Month |
| **BU** | Business Unit (SMB ou MM) |
| **MoM / YoY / YTD** | Month-over-Month / Year-over-Year / Year-to-Date |
| **GMV** | Gross Merchandise Value |
| **CAC** | Customer Acquisition Cost |
| **LTV** | Lifetime Value |
| **DP** | Data Product |
| **SC** | Search Console (Google) |
| **KWP** | Keyword Planner (Google) |
| **GA4** | Google Analytics 4 |
| **FX** | Foreign Exchange (conversão de moeda) |

---

## 2. Dicionário de dimensões

Dimensões são os campos que **descrevem** os KPIs (não os medem). Filtros e segmentações se aplicam sobre elas.

### 2.1 `country`

- **Definição:** Código ISO-2 do país do merchant / da query / do evento.
- **Valores possíveis por fonte:**

| Fonte | Países cobertos |
|---|---|
| DP1 (meanclick) | AR, BR, MX, CL, CO |
| DP2 (GA4 Sessions) | AR, BR, MX, CL, CO *(conforme atribuição GA4)* |
| DP3 (GSC + KWP) | AR, BR, MX, CL, CO, PE |
| Raw events B&C (clipping, social, followers) | AR, BR, MX |
| CSV Net Adds | AR, BR, CL, CO, MX |

### 2.2 `business_unit`

- **Definição:** Segmento de negócio do merchant — **SMB** (small/medium) ou **MM** (Mid-Market).
- **Como identificar por fonte:**

| Fonte | Critério MM | Critério SMB |
|---|---|---|
| DP1 (meanclick) | `page_subgroup = 'Next'` OR `mkt_subteam = 'Mid-Market'` | tudo que não é MM |
| DP2 (GA4) | `page_subgroup = 'Next'` OR `mkt_subteam = 'Mid-Market'` | tudo que não é MM |
| DP3 (Search / KWP) | `is_next_evolucion = true` na query | `is_next_evolucion = false` |
| Raw events B&C | sem coluna explícita — assumir SMB | — |

- **Definição (schema, DP1):** *"Business unit classification at the time of store acquisition (SMB or MM) based on store `first_contract_type` from acquisition profile. SMB: all non-enterprise contracts; MM: enterprise contracts."*
- **Gotchas:**
    - Critério ainda em revisão pelo time de Ops — pode mudar
    - MM corresponde à marca **Next / Evolución**
    - Coluna `brand_segment` no DP3 traduz: `'Nuvemshop / Tiendanube'` (SMB) ou `'Next / Evolución'` (MM)

### 2.3 `mkt_source` ⭐ (canônica para análises por source/lever)

- **Definição:** Marketing source aligned to attribution model — a source canônica vinda do modelo mean-click. **Esta é a coluna a ser usada para qualquer análise por source ou agrupamento por lever.**
- **Definição (schema):** *"Marketing source aligned to attribution (`mkt_source_attribution` from the plan ref when the row is plan-driven)."*
- **Disponível em:** DP1, DP2 (daily e snapshot mensal)
- **Valores observados** (DP1, 2026 YTD — 16 sources raw):

`Affiliates`, `Brand & Comms`, `Direct`, `Eea`, `Enp`, `Mandae`, `Mid-market`, `Nurturing`, `Organic`, `Organic Growth`, `Others`, `Partners`, `Performance Brand`, `Performance No Brand`, `Product Marketing`, `Store Referral`

→ Para a hierarquia de agrupamento (Low Volume · Performance/Organic/Indirect · Branded/Non-Branded), ver **§3.4 Hierarquia de mkt_source**.

- **Gotchas:**
    - **Sempre usar `mkt_source`** para breakdowns e agrupamentos — não `plan_mkt_source_ops`
    - `Mandae` só aparece em `mkt_source`, não em `plan_mkt_source_ops` (attribution-only — sem linha de plan)

### 2.4 `plan_mkt_source_ops` (uso restrito)

- **Definição:** Label de marketing source vinda da planilha de plan de Ops. **Não usar para breakdowns analíticos — usar apenas para análises plan-only** (ex: validação de quais sources têm meta cadastrada).
- **Definição (schema):** *"Ops / spreadsheet marketing source label from the plan ref for the plan grain (source-only before 2026-01-01; source + subteam from 2026); null when there is no plan row (attribution-only)."*
- **Disponível em:** DP1, DP2
- **Gotchas:**
    - **NULL** para linhas sem plan (attribution-only) — pode "sumir" sources reais como Mandae em breakdowns
    - Labels iguais aos de `mkt_source` (exceto pela ausência de Mandae)
    - Use `mkt_source` em vez desta coluna na esmagadora maioria dos casos (ver §2.3)

### 2.5 `mkt_subteam`

- **Definição:** Bucket de subteam de marketing.
- **Definição (schema):** *"Marketing subteam bucket. For full_date before 2026-01-01 this column is always empty string (source-level grain). From 2026-01-01 onward it follows attribution/plan subteam; empty string when not specified (not SQL NULL), for stable merge keys."*
- **Disponível em:** DP1, DP2
- **Gotchas:** Antes de 2026-01-01 é sempre `''` (não NULL — string vazia)

### 2.6 `date` e variantes calendário

- **`date` / `full_date`:** data calendário diária (grain das tabelas diárias)
- **`date_day` / `date_month` / `date_quarter` / `date_year` / `date_week`:** componentes derivados — `date_month` no formato `'YYYY-MM'`, `date_quarter` no formato `'YYYY-QN'`
- **`day_name`:** nome do dia da semana

### 2.7 `brand_segment` (DP3)

- **Definição:** Label legível da variante de marca da linha.
- **Definição (schema):** *"Human-readable label of the brand variant carried in business_unit: 'Nuvemshop / Tiendanube' for SMB, 'Next / Evolución' for MM."*

### 2.8 `is_store_blocked` (DP1)

- **Definição:** Flag de loja bloqueada. Lojas bloqueadas são **excluídas** dos `effective_*` por construção do DP.
- **Gotchas:** O filtro já está aplicado nos `effective_*` — não precisa filtrar de novo. Mas para análises sobre `raw_*` ou joins com outras tabelas, lembrar.

### 2.9 `special_days` (calendário marketing)

- **Definição:** Dias com comportamento atípico de demanda. Vêm da tabela manual `ext__marketing__acquisition__key_dates_by_country`.
- **Uso:** Para KPIs com plan, special days mudam a janela de forecast (180d em vez de 90d).
- **Exemplos:** Black Friday, Cyber Monday, Hot Sale (AR), Buen Fin (MX).

### 2.10 `icp` (Ideal Customer Profile)

- **Definição:** Segmento do merchant segundo o framework de ICPs (ver §1.2). Usado para abrir KPIs de funnel (Trials, NPs, CVR Trial→NP) por perfil de aquisição.
- **Valores:** ICP 1 (Platform Migrants), ICP 2 (Social Sellers), ICP 3 (Offline Sellers), ICP 4 (Marketplace Sellers), ICP 5a (D2C Starters), ICP 5b (Affiliates / Dropshippers). Ver §1.2 para definições.
- **Status:** ⚠️ **Fonte de classificação pendente** — hoje não existe coluna de tag de ICP por merchant em nenhum DP. A abertura por ICP nos MBRs é construída com fonte externa (planilha / classificação manual).
- **Gotchas:**
    - Os MBRs históricos (BR, MX) usam a **nomenclatura antiga** (ICP 1-4 + "Fallback"), que **não** corresponde 1:1 ao framework novo de §1.2. Validar o mapeamento antigo → novo antes de comparar séries temporais.
    - O framework novo (§1.2) é a referência canônica; os relatórios devem migrar para ele.
    - Os segmentos não somam 100% do universo (ver §1.2).

---

## 3. Tabelas de referência

### 3.1 Data Products ativos

Cada DP tem duas variantes: **daily** (granularidade diária, 6 famílias) e **snapshot monthly** (mensal, 3 famílias). Ver §0.1 para quando usar cada.

| DP | Daily | Snapshot mensal | Granularidade | Domínio principal |
|---|---|---|---|---|
| **DP1 — Acquisition (meanclick)** | `g__general__meanclick_budget_forecast__agg_daily` | `g__general__meanclick_budget_forecast__agg_snapshot_monthly` | (data ou mês) × país × `mkt_source` × `mkt_subteam` × BU | Acquisition |
| **DP2 — GA4 Sessions** | `g__general__ga4_sessions_budget_forecast__agg_daily` | `g__general__ga4_sessions_budget_forecast__agg_snapshot_monthly` | (data ou mês) × país × `mkt_source` × `mkt_subteam` × BU | Acquisition |
| **DP3 — GSC + KWP Searches** | `g__general__gsc_kwp_searches_budget_forecast__agg_daily` | `g__general__gsc_kwp_searches_budget_forecast__agg_snapshot_monthly` | (data ou mês) × país × BU | Brand |
| **DP4 — GMV (Finance Segments)** | `g__general__gmv_finance_segments_budget_forecast__agg_snapshot_daily` | `g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly` | (data ou mês) × país × `finance_segment` × BU | Financial |

Todas estão sob `data_products_prd.data_marketing`.

**Snapshot mensal — comportamento:**
- Rodam dia **4 do mês seguinte** e congelam o mês anterior
- Append-only — mudanças retroativas a montante (ex: flips em `flg_gmv`) **não** refletem após o snapshot
- Particionados por `snapshot_month` (INT `yyyyMM`)
- Têm apenas as 3 famílias canônicas (`effective_*`, `forecast_*`, `expected_monthly_*`) — sem `ponderation_key_*`, sem split linear/weighted (não faz sentido no grão mensal)

### 3.2 Raw event tables (Brand & Comms)

| Domínio | Tabela | Granularidade |
|---|---|---|
| **PR Clipping** | `data_products_prd.data_marketing.s__brand_and_comms__clipping__event` | publicação |
| **Social Insights** | `data_products_prd.data_marketing.s__brand_and_comms__social_insights__event` | data × país |
| **Instagram Followers** | `data_products_prd.data_marketing.s__brand_and_comms__instagram_followers__event` | data × país |
| **B&C Goals** | `data_products_prd.data_marketing.s__brand_and_comms__goals__event` | data × país |

### 3.3 Data Products em construção

| DP | KPIs esperados | Status |
|---|---|---|
| **DP5 — Merchant Base** | Merchant Base, Net Adds, Churn, Downgrade, New Phoenix, Old Phoenix, Ajuste | Em construção. Placeholder: CSV |
| **DP6 — Marketing Expenses & Headcount** | Spend, Headcount Cost, Headcount # | Em construção. **Sem placeholder** |

### 3.4 Hierarquia de `mkt_source` (4 níveis)

A coluna canônica é **`mkt_source`** (não `plan_mkt_source_ops` — ver §2.3 e §2.4). Os 16 valores raw são agrupados em 3 níveis adicionais para análises de breakdown — cada nível oferece uma "lente" diferente:

- **Nível 1** — `mkt_source` (16 valores raw, vindos da atribuição)
- **Nível 2** — consolidação: as 9 sources de baixo volume individual são agrupadas em **Low Volume**, resultando em **8** valores
- **Nível 3** — agrupamento por **mecânica de aquisição** (4 valores): Performance · Organic · Indirect · Low Volume
- **Nível 4** — agrupamento por **relação com a marca** (2 valores): Branded · Non-Branded

| Nível 1 (mkt_source — 16) | Nível 2 (8) | Nível 3 (4) | Nível 4 (2) |
|---|---|---|---|
| Direct | Direct | Organic | Branded |
| Organic | Organic | Organic | Branded |
| Performance Brand | Performance Brand | Performance | Branded |
| Performance No Brand | Performance No Brand | Performance | Non-Branded |
| Organic Growth | Organic Growth | Organic | Non-Branded |
| Affiliates | Affiliates | Indirect | Non-Branded |
| Partners | Partners | Indirect | Non-Branded |
| Brand & Comms | Low Volume | Low Volume | Non-Branded |
| Eea | Low Volume | Low Volume | Non-Branded |
| Enp | Low Volume | Low Volume | Non-Branded |
| Mandae | Low Volume | Low Volume | Non-Branded |
| Mid-market | Low Volume | Low Volume | Non-Branded |
| Nurturing | Low Volume | Low Volume | Non-Branded |
| Others | Low Volume | Low Volume | Non-Branded |
| Product Marketing | Low Volume | Low Volume | Non-Branded |
| Store Referral | Low Volume | Low Volume | Non-Branded |

**Quando usar cada nível:**

| Nível | Caso de uso típico |
|---|---|
| 1 | Análises operacionais granulares; investigação de variação por source específica |
| 2 | Breakdowns em relatórios (MBR, dashboards) — esconde ruído de sources marginais |
| 3 | Visão consolidada de mecânica (performance vs orgânico vs indireto) |
| 4 | Storytelling executivo — narrativa de Branded Levers vs Non-Branded Levers |

**Notas:**
- "Others" no Nível 1 não é descartada — vira parte do **Low Volume** no Nível 2
- O Nível 2 deve ser o padrão para tabelas e charts de relatórios — combina legibilidade e cobertura
- Direct é classificada como Organic no Nível 3 (não há gasto pago) mas Branded no Nível 4 (usuário busca a marca)

---

## 4. KPIs — Brand

### 4.1 Search Presence

#### Branded Searches

- **Domínio · Subdomínio:** Brand · Search Presence
- **Definição (business):** Volume de buscas no Google contendo a marca Nuvemshop/Tiendanube. Em SMB, exclui a marca Mid-Market "Next/Evolución". Duas fontes complementares: **Search Console (SC)** mede impressões reais que recebemos; **Keyword Planner (KWP)** mede o tamanho do mercado branded. O plan oficial está em SC.
- **Definição (schema, SC):** *"Daily branded impressions in Google Search Console for the brand variant of this row. Counts impressions where `is_nuvemshop_tiendanube=true` AND (`d2c_match_type='exact'` OR `marketplace_match_type='exact'`), split by `is_next_evolucion` (SMB=false, MM=true). NULL for future dates."*
- **Fórmula (SC, oficial p/ plan):** `SUM(effective_branded_searches_sc_daily)`
- **Fórmula (KWP, p/ Share of Market):** `SUM(effective_branded_searches_tiendanube_kwp_daily)`
- **Source type:** Data Product (DP3)
- **Colunas:** real `effective_branded_searches_sc_daily` · plan `expected_monthly_branded_searches_sc_daily` · forecast `forecast_branded_searches_sc_daily`
- **Agregação:** SUM
- **Status:** Ativo
- **Gotchas:**
    - Não confundir SC com KWP — fontes e universos diferentes
    - KWP é distribuído linearmente do mensal — pouca utilidade para variação intra-mês
    - Plan SMB só em SC; MM sem plan hoje
- **Related KPIs:** Branded CTR, Share of Market, Total Market Search Volume

#### Branded Searches CTR %

- **Domínio · Subdomínio:** Brand · Search Presence
- **Definição (business):** Click-through rate sobre queries branded no Google Search Console — qual % dos usuários que veem o resultado branded clica nele.
- **Definição (schema):** *"Daily click-through rate for branded SC traffic: `effective_branded_clicks_sc_daily / effective_branded_searches_sc_daily`. 0 when no impressions."*
- **Fórmula:** `SUM(effective_branded_clicks_sc_daily) / SUM(effective_branded_searches_sc_daily)`
- **Source type:** Data Product (DP3)
- **Agregação:** **SUM(num) / SUM(den)** — nunca média de CTRs diários
- **Status:** Ativo (sem plan)
- **Gotchas:**
    - Existe coluna pronta `effective_branded_ctr_sc_daily` para o ratio diário — para período usar `SUM(num)/SUM(den)`
    - SC, não KWP — CTR não existe em KWP
- **Related KPIs:** Branded Searches

#### Share of Market (Branded Share KWP)

- **Domínio · Subdomínio:** Brand · Search Presence
- **Definição (business):** Participação da marca no universo de buscas D2C oficiais (Nuvemshop/Tiendanube + competidores oficiais identificados pelo KWP). Mede "fatia de mente" do consumidor no mercado.
- **Definição (schema):** *"Daily branded market share: `effective_branded_searches_tiendanube_kwp_daily / effective_d2c_searches_kwp_daily` (our official-D2C brand impressions over the total official-D2C market). 0 when denominator is 0. SMB only; NULL for MM."*
- **Fórmula:** `SUM(effective_branded_searches_tiendanube_kwp_daily) / SUM(effective_d2c_searches_kwp_daily)`
- **Source type:** Data Product (DP3)
- **Colunas:** real `effective_branded_share_tiendanube_kwp_daily` (pre-calc diário) · plan `expected_monthly_branded_share_tiendanube_kwp_daily`
- **Agregação:** SUM(num) / SUM(den) — não a média do ratio diário
- **Status:** Ativo
- **Gotchas:**
    - Plan vem como **MAX** mensal — share é % único por mês, não aditivo
    - Cada país tem seu universo de competidores próprio, já segmentado pelo DP
- **Related KPIs:** Share of Market (excl. Wix), Total Market Search Volume

#### Share of Market — excl. Wix

- **Domínio · Subdomínio:** Brand · Search Presence
- **Definição (business):** Variante do Share of Market que **exclui Wix** do universo D2C. Mais comparável internacionalmente, já que a presença de Wix enviesa o denominador em alguns mercados.
- **Definição (schema):** *"Daily branded market share excluding Wix from the denominator: `effective_branded_searches_tiendanube_kwp_daily / effective_d2c_searches_kwp_excl_wix_daily`. 0 when denominator is 0. SMB only; NULL for MM."*
- **Fórmula:** `SUM(effective_branded_searches_tiendanube_kwp_daily) / SUM(effective_d2c_searches_kwp_excl_wix_daily)`
- **Source type:** Data Product (DP3)
- **Agregação:** SUM(num) / SUM(den)
- **Status:** Ativo (sem plan)
- **Related KPIs:** Share of Market

#### Total Market Search Volume

- **Domínio · Subdomínio:** Brand · Search Presence (Market Context)
- **Definição (business):** Volume total de buscas no Keyword Planner — branded + non-branded. Dimensiona o tamanho absoluto do mercado.
- **Definição (schema):** *"Daily total Keyword Planner impressions across all queries (branded + non-branded). Monthly source distributed linearly by days in the month. SMB only; NULL for MM."*
- **Fórmula:** `SUM(effective_total_market_searches_kwp_daily)`
- **Source type:** Data Product (DP3)
- **Status:** Ativo (sem plan)
- **Gotchas:**
    - Distribuído linearmente do mensal — não usar para análise intra-mês
- **Related KPIs:** Non-Branded Searches (KWP)

#### SOV AI Platforms

- **Domínio · Subdomínio:** Brand · Search Presence (AI)
- **Definição (business):** Share of Voice em plataformas de busca AI (ChatGPT, Perplexity, Gemini, etc.).
- **Source type:** 🔵 Manual — input externo
- **Status:** 🔵 Manual

### 4.2 PR (Public Relations)

#### Total Publications

- **Domínio · Subdomínio:** Brand · PR
- **Definição (business):** Total de publicações cobertas pelo clipping de PR no período.
- **Fórmula:** `COUNT(*)` em `s__brand_and_comms__clipping__event` filtrado por país e mês
- **Source type:** Raw event aggregation
- **Status:** Ativo
- **Plan:** ✅ via `publicaciones_totales_pr` em `s__brand_and_comms__goals__event`
- **Related KPIs:** Gold Media, Tier 1, Tier 2

#### Gold Media

- **Domínio · Subdomínio:** Brand · PR
- **Definição (business):** Publicações em veículos classificados como Golden — tier máximo, acima dos tiers numéricos (1-4).
- **Definição (schema, `golden_media_flag`):** *"Indicates whether the media outlet is classified as Golden (premium tier)"*
- **Fórmula:** `SUM(CASE WHEN golden_media_flag = TRUE THEN 1 ELSE 0 END)`
- **Source type:** Raw event aggregation
- **Status:** Ativo

#### Tier 1

- **Domínio · Subdomínio:** Brand · PR
- **Definição (business):** Publicações tier 1 que **não** são Gold (Gold já está contado à parte).
- **Definição (schema, `tier`):** *"Tier or priority classification of the media outlet (1, 2, 3, 4)"*
- **Fórmula:** `SUM(CASE WHEN tier = 1 AND golden_media_flag = FALSE THEN 1 ELSE 0 END)`
- **Source type:** Raw event aggregation
- **Status:** Ativo
- **Plan:** ✅ via `publicaciones_t1_pr`

#### Tier 2

- **Domínio · Subdomínio:** Brand · PR
- **Fórmula:** `SUM(CASE WHEN tier = 2 THEN 1 ELSE 0 END)`
- **Status:** Ativo

#### Proactive Publications

- **Domínio · Subdomínio:** Brand · PR
- **Definição (business):** Publicações originadas proativamente pelo time (push), em oposição a reativas (pickup de notícia externa).
- **Definição (schema, `origin_type`):** *"Indicates whether the article is Original or Replica (pickup). For BR: Proativa maps to Original, Reativa maps to Replica."*
- **Fórmula:** `SUM(CASE WHEN origin_type = 'Original' THEN 1 ELSE 0 END)`
- **Status:** Ativo
- **Gotchas:** No BR, os labels vêm em português ("Proativa"/"Reativa") e são mapeados para Original/Replica no DP

#### Total Reach (PR)

- **Domínio · Subdomínio:** Brand · PR
- **Definição (business):** Alcance estimado total das publicações no período.
- **Definição (schema, `reach`):** *"Estimated audience reach or potential impressions. Returns NULL for invalid values (not 0). WARNING: Invalid numeric values should be caught and fixed in source data."*
- **Fórmula:** `SUM(COALESCE(reach, 0))`
- **Status:** Ativo
- **Gotchas:**
    - Valores inválidos vêm como **NULL** (não 0) — usar `COALESCE` ao somar
    - Qualidade do dado tem WARNING no schema — problemas a montante

### 4.3 Social (Instagram)

#### Total Reach (Social)

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Alcance total no Instagram, somando 4 buckets: orgânico, pago, colabs com 3rd party, e manual_non_classified.
- **Definição (schema):** *"Total reach: organic + paid + third_party_collabs + manual_non_classified"*
- **Fórmula:** `SUM(reach_total)`
- **Source type:** Raw event aggregation
- **Tabela:** `s__brand_and_comms__social_insights__event`
- **Status:** Ativo
- **Plan:** ✅ via `reach_social`
- **Gotchas:**
    - Já é a soma dos 4 componentes — não recalcular como `reach_organic + reach_paid_total + reach_collab_third_party` (perde o bucket `manual_non_classified`)
- **Related KPIs:** Organic Reach, Paid Reach, Collab Reach

#### Organic Reach

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Alcance via conteúdo orgânico (não-pago, não-colab). Fonte: Supermetrics.
- **Definição (schema):** *"Reach from organic (Supermetrics) data"*
- **Fórmula:** `SUM(reach_organic)`
- **Status:** Ativo

#### Paid Reach

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Alcance via campanhas pagas no Instagram.
- **Definição (schema):** *"Reach from paid campaigns"*
- **Fórmula:** `SUM(reach_paid_total)`
- **Status:** Ativo

#### Collab Reach

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Alcance via colaborações com terceiros (creators, parcerias). Não está incluído no orgânico.
- **Definição (schema):** *"Reach from third-party collaborations (not in organic)"*
- **Fórmula:** `SUM(reach_collab_third_party)`
- **Status:** Ativo

#### Interactions

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Total de interações no Instagram (likes, comentários, saves, shares), somando os 4 buckets.
- **Definição (schema):** *"Total interactions: organic + paid + third_party_collabs + manual_non_classified"*
- **Fórmula:** `SUM(interactions_total)`
- **Status:** Ativo

#### Saves

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Posts salvos pelos usuários — sinal forte de interesse.
- **Fórmula:** `SUM(saves_total)`
- **Status:** Ativo

#### Shares

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Conteúdo compartilhado pelos usuários — sinal de propagação.
- **Fórmula:** `SUM(shares_total)`
- **Status:** Ativo

#### Engagement Rate

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Taxa de engajamento — interações por reach.
- **Fórmula:** `SUM(interactions_total) / SUM(reach_total)`
- **Source type:** Raw event aggregation (derivado)
- **Agregação:** SUM(num) / SUM(den) — nunca média de rates diários
- **Status:** Ativo
- **Plan:** ✅ via `engagement_rate_social` (MAX no mês — constante diária)

#### Profile Followers

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Total de seguidores no Instagram. No nível mensal, usamos o último snapshot disponível (fim do período).
- **Definição (schema):** *"Total number of Instagram profile followers on the given date"*
- **Fórmula:** `MAX(profile_followers)` no período
- **Tabela:** `s__brand_and_comms__instagram_followers__event`
- **Filtros:** `status = 'ok'`
- **Agregação:** MAX
- **Status:** Ativo
- **Gotchas:**
    - **Filtrar `status = 'ok'`** — exclui dados em revisão (`review`) ou duplicados (`review_dup`)

#### Net New Followers

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Saldo líquido de novos seguidores no período. **Já vem líquido** na coluna `new_followers` (novos − unfollowers). Pode ser negativo.
- **Definição (schema):** *"Number of new followers gained on the given date (can be negative if more users unfollowed than followed)"*
- **Fórmula:** `SUM(new_followers)`
- **Status:** Ativo
- **Gotchas:** Não somar com `unfollowers` — já está líquido

#### Unfollowers

- **Domínio · Subdomínio:** Brand · Social
- **Definição (business):** Total de unfollows no período.
- **Fórmula:** `SUM(unfollowers)`
- **Status:** Ativo

---

## 5. KPIs — Acquisition

### 5.1 Funnel (Macro)

#### Sessions

- **Domínio · Subdomínio:** Acquisition · Funnel
- **Definição (business):** Total de sessões no site marketing-atribuíveis, **excluindo sessões "login-only"** (usuário só logou, não navegou). Vem do GA4.
- **Definição (schema):** *"Sum of `distinct_session_count` where `only_login_session = 0`. Null for future dates; 0 when no sessions observed."*
- **Fórmula:** `SUM(effective_total_sessions)`
- **Source type:** Data Product (DP2)
- **Colunas:** real `effective_total_sessions` · plan **NULL hoje** (cols reservadas) · forecast `forecast_total_sessions`
- **Agregação:** SUM
- **Status:** Ativo (sem plan)
- **Gotchas:**
    - GA4 reescreve dados até 5 dias depois — DP refaz últimos 5 dias a cada corrida
    - **Sem plan hoje** — attainment % indisponível
- **Related KPIs:** Bounced Sessions, Total Users, Organic Users, CVR Session→Trial

#### Bounced Sessions

- **Domínio · Subdomínio:** Acquisition · Funnel (Quality)
- **Definição (business):** Sessões que rebotaram — sessões em que o usuário não engajou (não fez interação significativa).
- **Definição (schema):** *"Sum of `distinct_session_count` where `only_login_session = 0` AND `session_status != 'Engaged'`. Null for future dates."*
- **Fórmula:** `SUM(effective_bounced_sessions)`
- **Source type:** Data Product (DP2)
- **Status:** Ativo (sem plan)

#### Total Users

- **Domínio · Subdomínio:** Acquisition · Funnel
- **Definição (business):** Usuários únicos no período (excluindo login-only).
- **Definição (schema):** *"Sum of `distinct_user_count` where `only_login_session = 0`. Null for future dates."*
- **Fórmula:** `SUM(effective_total_users)`
- **Source type:** Data Product (DP2)
- **Status:** Ativo (sem plan)

#### Organic Users

- **Domínio · Subdomínio:** Acquisition · Funnel
- **Definição (business):** Usuários únicos provenientes de canais orgânicos.
- **Definição (schema):** *"Sum of `distinct_user_count` where `only_login_session = 0` AND `organic_results = 'Organic'`. Null for future dates."*
- **Fórmula:** `SUM(effective_organic_users)`
- **Source type:** Data Product (DP2)
- **Status:** Ativo

#### Avg Pageviews per Session

- **Domínio · Subdomínio:** Acquisition · Funnel (Quality)
- **Definição (business):** Profundidade de navegação — média de pageviews por sessão. **Session-weighted**: dias com mais sessões pesam mais.
- **Definição (schema):** *"Session-weighted average of `avg_pageviews_per_session` where `only_login_session = 0`. Null for future dates or when no sessions."*
- **Fórmula:** `SUM(effective_avg_pageviews × effective_total_sessions) / SUM(effective_total_sessions)`
- **Source type:** Data Product (DP2)
- **Agregação:** Session-weighted average (ver §0.6)
- **Status:** Ativo (sem plan)

#### Avg Session Duration

- **Domínio · Subdomínio:** Acquisition · Funnel (Quality)
- **Definição (business):** Duração média da sessão. Session-weighted.
- **Definição (schema):** *"Session-weighted average of `avg_session_duration` where `only_login_session = 0`. Null for future dates or when no sessions."*
- **Fórmula:** `SUM(effective_avg_session_duration × effective_total_sessions) / SUM(effective_total_sessions)`
- **Source type:** Data Product (DP2)
- **Agregação:** Session-weighted average
- **Status:** Ativo (sem plan)

#### Trials

- **Domínio · Subdomínio:** Acquisition · Funnel
- **Definição (business):** Novos trials (cadastros free) atribuídos a marketing pelo modelo **mean-click**. Contados pela **data de criação da loja**. Exclui lojas bloqueadas.
- **Definição (schema):** *"Sum of `trials_mean_click` by `store_created_date` at the model grain (by source before 2026-01-01, by source and subteam from 2026). 0 if none."*
- **Fórmula:** `SUM(effective_trials)`
- **Source type:** Data Product (DP1)
- **Colunas:** real `effective_trials` · plan `expected_monthly_trials` · forecast `forecast_trials`
- **Status:** Ativo
- **Gotchas:**
    - Antes de 2026-01-01: grão (data × país × source × BU). De 2026-01-01: adiciona subteam
- **Related KPIs:** CVR Session→Trial, CVR Trial→NP

#### New Payments (NPs)

- **Domínio · Subdomínio:** Acquisition · Funnel
- **Definição (business):** Primeiros pagamentos atribuídos a marketing pelo modelo mean-click, contados pela **data do primeiro pagamento** do merchant. Exclui lojas bloqueadas.
- **Definição (schema):** *"Sum of `trials_mean_click` bucketed by `first_payment_date`. 0 if none."*
- **Fórmula:** `SUM(effective_new_payments)`
- **Source type:** Data Product (DP1)
- **Status:** Ativo
- **Gotchas:**
    - Distinta de `payment_created_at` (que conta por data de criação do pagamento)
    - Trial e NP do mesmo merchant podem cair em meses diferentes — cuidado em análises de CVR
- **Related KPIs:** Payment Created At, First Payments (Company Metrics), CVR Trial→NP

#### Payment Created At

- **Domínio · Subdomínio:** Acquisition · Funnel (Alt. Attribution)
- **Definição (business):** Pagamentos contados pela **data de criação do pagamento** (não pela data do trial). Métrica alternativa usada em análises temporais mais ajustadas.
- **Definição (schema):** *"Sum of `payment_created_at_mean_click` at the model grain; excludes blocked stores. 0 if none."*
- **Fórmula:** `SUM(effective_payment_created_at)`
- **Source type:** Data Product (DP1)
- **Status:** Ativo
- **Related KPIs:** New Payments

#### New Sellers

- **Domínio · Subdomínio:** Acquisition · Funnel · Company Metrics
- **Definição (business):** Novos sellers atribuídos a marketing, contados pela data em que viraram seller — **somente quando esta data é posterior à data do primeiro pagamento** (i.e., exclui casos em que pagamento e primeira venda ocorrem no mesmo dia).
- **Definição (schema):** *"Sum of `trials_mean_click` bucketed by `first_seller_date` where `first_seller_date > first_payment_date`. 0 if none."*
- **Fórmula:** `SUM(effective_new_sellers)`
- **Source type:** Data Product (DP1)
- **Status:** Ativo
- **Gotchas:**
    - Distinta de `effective_new_seller_created_at` (que usa o path `first_seller_at` — outra atribuição)
- **Related KPIs:** New Seller Created At

#### New Seller Created At

- **Domínio · Subdomínio:** Acquisition · Funnel (Alt. Attribution)
- **Definição (business):** Novos sellers contados pelo path `first_seller_at` — atribuição alternativa, distinta de New Sellers.
- **Definição (schema):** *"Sum of `new_seller_created_at_mean_click` at the model grain; excludes blocked stores. Distinct from `effective_new_sellers` (`first_seller_at` path)."*
- **Fórmula:** `SUM(effective_new_seller_created_at)`
- **Source type:** Data Product (DP1)
- **Status:** Ativo

#### QLs (Qualified Leads)

- **Domínio · Subdomínio:** Acquisition · Funnel
- **Definição (business):** Leads qualificados atribuídos a marketing pelo modelo mean-click. Exclui lojas bloqueadas.
- **Definição (schema):** *"Sum of `qls_mean_click` at the model grain; excludes blocked stores (same join as other effectives). 0 if none."*
- **Fórmula:** `SUM(effective_qls)`
- **Source type:** Data Product (DP1)
- **Status:** Ativo

### 5.2 Funnel Efficiency (CVRs)

#### CVR Session → Trial

- **Domínio · Subdomínio:** Acquisition · Funnel Efficiency
- **Definição (business):** Conversão de sessão em trial — qual % das sessões viram cadastro.
- **Fórmula:** `SUM(effective_trials) / SUM(effective_total_sessions)`
- **Source type:** Derivado (cross-DP: DP1 + DP2)
- **Agregação:** SUM(num) / SUM(den)
- **Status:** Ativo
- **Gotchas:**
    - **Cross-DP** — garantir mesmos filtros (country, BU, date, source) nos dois lados
    - DP2 exclui sessões login-only; DP1 exclui lojas bloqueadas — populações não 100% alinhadas

#### CVR Trial → NP

- **Domínio · Subdomínio:** Acquisition · Funnel Efficiency
- **Definição (business):** Conversão de trial em new payment — qual % dos trials viram pagantes.
- **Fórmula:** `SUM(effective_new_payments) / SUM(effective_trials)`
- **Source type:** Derivado (DP1)
- **Agregação:** SUM(num) / SUM(den)
- **Status:** Ativo
- **Gotchas:**
    - **Mismatch temporal:** NPs do mês X podem vir de Trials do mês X-1 (ou anterior). Para análise por coorte, usar `payment_created_at` cruzado com `new_seller_created_at`

### 5.3 Investment (CAC, Spend) ⚠️

#### Spend (Marketing Investment)

- **Domínio · Subdomínio:** Acquisition · Investment
- **Definição (business):** Investimento total em mídia no período. Não existe em DP atual.
- **Source type:** ⚠️ Bloqueado (DP6 — Marketing Expenses)
- **Status:** ⚠️ Bloqueado

#### CAC (Cost per Acquisition)

- **Domínio · Subdomínio:** Acquisition · Investment
- **Definição (business):** Custo de aquisição por novo cliente pagante.
- **Fórmula:** `Spend / SUM(effective_new_payments)`
- **Source type:** ⚠️ Bloqueado (depende de DP6)
- **Status:** ⚠️ Bloqueado

### 5.4 By Source / Lever (hierarquia de 4 níveis)

Os KPIs de funnel (Sessions, Trials, NPs, New Sellers, QLs, CVRs) podem ser abertos em qualquer um dos 4 níveis de `mkt_source` definidos em **§3.4**:

- **Nível 1** (16 sources raw) — análises operacionais granulares
- **Nível 2** (8 sources, com Low Volume) — padrão para tabelas/charts de relatórios
- **Nível 3** (4 categorias — Performance · Organic · Indirect · Low Volume) — mecânica de aquisição
- **Nível 4** (Branded · Non-Branded) — narrativa executiva

Filtrar sempre por **`mkt_source`** (não `plan_mkt_source_ops`). Os níveis 2-4 são derivados via CASE/mapping no SELECT — ver snippet em §9.4.

- **Sessions por nível:** DP2 — sem plan hoje
- **Trials / NPs / QLs por nível:** DP1 — com plan
- **Spend / CAC por nível:** ⚠️ Bloqueado (DP6)

**Abertura adicional por ICP:** os KPIs de funnel (Trials, NPs, CVR Trial→NP) também são abertos por **`icp`** (ver §2.10) nos MBRs — além de por `mkt_source`. ⚠️ A classificação por ICP depende de fonte externa (sem tag de ICP nos DPs hoje).

---

## 6. KPIs — Company Metrics 🟡

Todos os KPIs desta seção estão em **CSV placeholder** até **DP5 — Merchant Base** entrar em produção. Quando disponível, migrar para queries SQL no padrão dos demais DPs.

### 6.1 Base Health

#### Merchant Base

- **Domínio · Subdomínio:** Company Metrics · Base Health
- **Definição (business):** Total de merchants pagantes ativos no fim do período (snapshot EOP/EOM).
- **Source type:** 🟡 CSV Placeholder (futuro: DP5)
- **Tabela placeholder:** `data/net_adds_placeholder.csv`, coluna `Merchant Base`
- **Agregação:** valor EOP direto
- **Status:** 🟡 Placeholder
- **Related KPIs:** Net Adds, % Seller

#### Net Adds

- **Domínio · Subdomínio:** Company Metrics · Base Health
- **Definição (business):** Saldo líquido na merchant base no período. Diferença entre inflow (novos + reativações) e outflow (churn + downsell), incluindo ajustes contábeis.
- **Fórmula:** `first_payments + new_phoenix + old_phoenix − churn_and_downgrade + ajuste`
- **Source type:** 🟡 CSV Placeholder
- **Tabela placeholder:** `data/net_adds_placeholder.csv`, coluna `Net Customers`
- **Status:** 🟡 Placeholder
- **Gotchas:** Quando DP5 for publicado, migrar para `SUM(effective_net_adds)`
- **Related KPIs:** First Payments, Phoenix (New/Old), Churn+Downgrade, Ajuste

### 6.2 Inflow

#### First Payments (Company Metrics)

- **Domínio · Subdomínio:** Company Metrics · Inflow
- **Definição (business):** Novos merchants que fizeram primeiro pagamento no período — inflow novo. **Diferença vs NPs do DP1:** Company Metrics usa a definição de base (não atribuída a marketing); DP1 conta só os marketing-attributed.
- **Fórmula:** `SUM(first_payments)`
- **Source type:** 🟡 CSV Placeholder (futuro: DP5)
- **Status:** 🟡 Placeholder
- **Related KPIs:** New Payments (DP1)

#### New Phoenix

- **Domínio · Subdomínio:** Company Metrics · Inflow
- **Definição (business):** Merchants que retornaram à base via funil Phoenix (reativação recente).
- **Fórmula:** `SUM(new_phoenix)`
- **Source type:** 🟡 CSV Placeholder
- **Status:** 🟡 Placeholder
- **Related KPIs:** Old Phoenix

#### Old Phoenix

- **Domínio · Subdomínio:** Company Metrics · Inflow
- **Definição (business):** Reativação de merchants churned há mais tempo (long-tail).
- **Fórmula:** `SUM(old_phoenix)`
- **Source type:** 🟡 CSV Placeholder
- **Status:** 🟡 Placeholder

#### Ajuste

- **Domínio · Subdomínio:** Company Metrics · Inflow (Reconciliation)
- **Definição (business):** Reconciliação contábil residual que fecha o Net Adds com a variação real da Merchant Base.
- **Fórmula:** `SUM(ajuste)`
- **Status:** 🟡 Placeholder
- **Gotchas:** Componente pequeno mas necessário. Conferir com DP5 se este conceito continua

### 6.3 Outflow

#### Churns

- **Domínio · Subdomínio:** Company Metrics · Outflow
- **Definição (business):** Merchants que deixaram de pagar no período.
- **Fórmula:** `SUM(churns)`
- **Source type:** 🟡 CSV Placeholder (futuro: DP5)
- **Status:** 🟡 Placeholder
- **Related KPIs:** Churn Rate, Churn + Downgrade

#### Downsell to Freemium

- **Domínio · Subdomínio:** Company Metrics · Outflow
- **Definição (business):** Merchants pagantes que rebaixaram para plano freemium — outflow não-churn.
- **Fórmula:** `SUM(downsell_freemium)`
- **Source type:** 🟡 CSV Placeholder
- **Status:** 🟡 Placeholder

#### Churn + Downgrade

- **Domínio · Subdomínio:** Company Metrics · Outflow
- **Definição (business):** Outflow total — soma de churns + downsell.
- **Fórmula:** `churns + downsell_freemium`
- **Status:** 🟡 Placeholder

#### Churn Rate

- **Domínio · Subdomínio:** Company Metrics · Outflow
- **Definição (business):** % de churn sobre a base inicial do período.
- **Fórmula:** `churns / merchant_base_t-1`
- **Source type:** Derivado (CSV)
- **Agregação:** SUM(num) / SUM(den)
- **Status:** 🟡 Placeholder

---

## 7. KPIs — Financial

### 7.1 Volume

Os KPIs de GMV vêm do **DP4 — GMV (Finance Segments)**. Existem 4 variantes de "GMV" no DP — cada uma com 3 versões de moeda:

| Variante | Significado | Aditivo? |
|---|---|---|
| **on_platform** ⭐ | GMV transacionado dentro da plataforma (loja online) — inclui POS | ✅ |
| **off_platform** | GMV via sistemas de pagamento externos (canais fora da plataforma) | ✅ (mas residual) |
| **pos** | GMV via PDV físico (Point of Sale) | ⚠️ **Subset de on_platform — não somar** |
| **total** | `on_platform + off_platform` | ✅ |

⭐ **Recomendação:** usar **`on_platform`** como GMV principal nos relatórios. Off-platform é negligível (<1% do total em todos os países observados em Mar/26) — a diferença entre `on_platform` e `total` é estatisticamente irrelevante. POS é parte de on-platform e relevante em CL/CO/MX (17-26% do on-platform) — exibir separadamente onde fizer sentido.

Versões de moeda:
- **LC (Local Currency)** — moeda local (ARS, BRL, MXN, etc.)
- **USD (source-runtime)** — USD convertido na hora do processamento
- **Finance USD** — USD convertido com FX médio YTD cumulativo (preferido para Finance/FP&A)

#### GMV (Total, LC)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** Gross Merchandise Value total (on-platform + off-platform) em moeda local — total transacionado pelos merchants no período.
- **Definição (schema):** *"`effective_gmv_on_platform_lc + effective_gmv_off_platform_lc` as of snapshot time."*
- **Fórmula:** `SUM(effective_gmv_total_lc)`
- **Source type:** Data Product (DP4)
- **Tabela:** snapshot mensal — `g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly`
- **Status:** Ativo
- **Gotchas:** Não soma POS (POS é subset de on_platform — somar dá double-count)

#### GMV (Total, USD)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** GMV total em USD convertido na hora do processamento (source-runtime).
- **Fórmula:** `SUM(effective_gmv_total_usd)`
- **Source type:** Data Product (DP4)
- **Status:** Ativo

#### GMV (Total, Finance USD)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** GMV total em USD convertido com FX médio YTD cumulativo — versão preferida para Finance/FP&A.
- **Definição (schema):** *"Daily on-platform GMV in Finance USD (cumulative YTD avg FX) as of snapshot time."*
- **Fórmula:** `SUM(effective_gmv_total_finance_usd)`
- **Source type:** Data Product (DP4)
- **Status:** Ativo

#### GMV (On-Platform, sem POS)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** GMV apenas da plataforma online, excluindo POS — comparável com a métrica histórica de "GMV da loja".
- **Fórmula:** `SUM(effective_gmv_on_platform_lc) − SUM(effective_gmv_pos_lc)` (LC), ou `_usd` / `_finance_usd`
- **Plan:** `expected_monthly_gmv_on_platform_without_pos_lc` / `_finance_usd`
- **Source type:** Data Product (DP4)
- **Status:** Ativo

#### GMV (POS)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** GMV via PDV físico. Subset de on_platform.
- **Fórmula:** `SUM(effective_gmv_pos_lc)` / `_usd` / `_finance_usd`
- **Plan:** `expected_monthly_gmv_pos_lc` / `_finance_usd`
- **Source type:** Data Product (DP4)
- **Status:** Ativo

#### Orders (Total)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** Volume total de transações (pedidos pagos) — on_platform + off_platform.
- **Definição (schema):** *"`effective_orders_on_platform + effective_orders_off_platform` as of snapshot time."*
- **Fórmula:** `SUM(effective_orders_total)`
- **Plan:** apenas para `on_platform_without_pos` e `pos` separadamente
- **Source type:** Data Product (DP4)
- **Status:** Ativo

#### Avg Ticket (Total)

- **Domínio · Subdomínio:** Financial · Volume
- **Definição (business):** Ticket médio = GMV / Orders no período.
- **Definição (schema):** *"(on + off gmv) / (on + off orders) as of snapshot time."*
- **Fórmula:** `SUM(effective_gmv_total_lc) / SUM(effective_orders_total)` (calcular o ratio, não somar `effective_avg_ticket_total_lc`)
- **Source type:** Data Product (DP4)
- **Agregação:** SUM(num) / SUM(den) — não média do ratio diário
- **Status:** Ativo

### 7.2 Productivity

#### % Seller

- **Domínio · Subdomínio:** Financial · Productivity (também Company Metrics)
- **Definição (business):** % da merchant base classificada como Seller — merchant com ≥7 vendas nos últimos 90 dias (janela móvel).
- **Fórmula:** `sellers_count / merchant_base_eop`
- **Source type:** ⚠️ Bloqueado (até DP5 — Merchant Base)
- **Status:** ⚠️ Bloqueado

#### GMV per Seller

- **Domínio · Subdomínio:** Financial · Productivity
- **Definição (business):** Produtividade média do seller — GMV gerado por seller ativo.
- **Fórmula:** `GMV (DP4) / (Merchant Base EOP × % Seller)` *(numerador disponível; denominador depende de DP5)*
- **Source type:** ⚠️ Bloqueado (numerador OK via DP4; denominador bloqueado até DP5)
- **Status:** ⚠️ Bloqueado

---

## 8. Apêndice — Notas técnicas

### 8.1 Forecast — comportamento

O `forecast_*` em DPs é projeção rolling average ancorada: 90d em dias normais, 180d em special days. **Nunca lê outros forecasts** — apenas `effective_*` reais. Para datas futuras sem plan, `forecast_*` vem `NULL`. Fallbacks: 180d sem filtro → 365d sem filtro → 0.

### 8.2 Refresh e latência

| Fonte | Refresh | Latência |
|---|---|---|
| DP1 (meanclick) | Diário 10am BA | T-1 |
| DP2 (GA4) | Diário 10am BA | T-1 + reescreve últimos 5 dias |
| DP3 (GSC + KWP) | Diário 10am BA | T-1 |
| Raw events B&C | Variável (por evento) | — |

### 8.3 Janela histórica padrão

Charts históricos usam histórico móvel de **24 meses** terminando no período corrente.

### 8.4 Anti-patterns

Erros comuns a evitar — extraídos das gotchas dos schemas. Em cada linha: ❌ **não fazer** vs ✅ **fazer correto** e o **porquê**.

| ❌ Não fazer | ✅ Fazer | Por quê |
|---|---|---|
| `AVG(effective_branded_ctr_sc_daily)` | `SUM(clicks) / SUM(searches)` | A média de ratios diários é enviesada por dias com pouco volume |
| `AVG(effective_branded_share_tiendanube_kwp_daily)` | `SUM(effective_branded_searches_tiendanube_kwp_daily) / SUM(effective_d2c_searches_kwp_daily)` | Mesma razão. Share é %, não aditivo |
| `AVG(engagement_rate_diario)` | `SUM(interactions_total) / SUM(reach_total)` | Idem |
| `AVG(effective_avg_pageviews)` | `SUM(effective_avg_pageviews × effective_total_sessions) / SUM(effective_total_sessions)` | Avg de avg sem peso por sessões distorce — é session-weighted |
| `SUM(reach_organic + reach_paid_total + reach_collab_third_party)` | `SUM(reach_total)` | A versão "manual" perde o bucket `manual_non_classified` (são 4 componentes, não 3) |
| `MAX(profile_followers)` sem filtro de `status` | `MAX(profile_followers) WHERE status = 'ok'` | Inclui dados em revisão (`review`, `review_dup`) — qualidade duvidosa |
| `SUM(new_followers) + SUM(unfollowers)` para calcular o saldo | `SUM(new_followers)` | `new_followers` já é líquido (novos − unfollowers). Pode ser negativo |
| `SUM(reach)` em PR sem `COALESCE` | `SUM(COALESCE(reach, 0))` | Valores inválidos viram NULL (não 0) no schema do clipping |
| Buscar CTR no KWP | Usar SC (`effective_branded_clicks_sc_daily`) | KWP não tem clicks, portanto não tem CTR |
| `SUM(branded_searches_sc) + SUM(branded_searches_kwp)` | Escolher uma única fonte conforme a análise | SC e KWP medem universos diferentes — somar é double-count |
| Comparar `effective_new_sellers` com `effective_new_seller_created_at` sem distinguir | Escolher uma e fixar a definição | São paths de atribuição distintos (`first_seller_date > first_payment_date` vs `first_seller_at`) |
| Comparar `effective_new_payments` com `effective_payment_created_at` sem distinguir | Escolher uma | Definidos por buckets temporais diferentes (data de atribuição vs data de criação do pagamento) |
| Calcular CVR Trial→NP no mesmo mês sem nota | Mencionar o **mismatch temporal** na análise | NPs do mês X podem vir de Trials do mês X-1 ou anterior |
| `WHERE business_unit = 'SMB'` sem entender o que é excluído | Identificar SMB vs MM conforme [§2.2](#22-business_unit), aplicar `WHERE business_unit = 'SMB'` consciente de que exclui Next/Evolución | Filtros automáticos sem contexto perdem clareza |
| Usar `forecast_*` para análise de meses passados como se fosse o realizado | Usar `effective_*` para passado; `forecast_*` apenas para projeção futura ou monitoramento intra-mês | Forecast nunca substitui o real |
| Cross-DP (DP1 + DP2) sem alinhar filtros | Garantir `country`, `business_unit`, `mkt_source`, `full_date` consistentes nos dois lados | Populações ficam desalinhadas e o ratio fica falso |
| `GROUP BY plan_mkt_source_ops` para breakdown por lever | `GROUP BY mkt_source` | `plan_mkt_source_ops` é NULL para attribution-only (ex: Mandae some do breakdown). `mkt_source` é canônica |
| Misturar níveis da hierarquia de `mkt_source` no mesmo chart (ex: `Performance Brand` lado a lado com `Performance`) | Escolher **um único nível** (1, 2, 3 ou 4 — ver §3.4) e manter o agrupamento consistente | Soma fica double-count e o leitor confunde granularidades |
| Tratar "Low Volume" como "Others" no Nível 1 | Low Volume só existe a partir do Nível 2 — é a consolidação de 9 sources, incluindo a própria `Others` | Conceitos distintos: `Others` (Nível 1) é uma source raw; `Low Volume` (Nível 2+) é um bucket de consolidação |
| `SUM(effective_gmv_on_platform) + SUM(effective_gmv_pos)` para "GMV total" | Usar `effective_gmv_total` (= on + off) ou `effective_gmv_on_platform − effective_gmv_pos` se quiser on sem POS | POS é **subset** de on_platform — somar é double-count |
| `AVG(effective_avg_ticket_total_lc)` | `SUM(effective_gmv_total_lc) / SUM(effective_orders_total)` | Avg ticket é ratio — recalcular pelos componentes |
| Usar daily DP para análise de mês fechado | Usar o snapshot mensal (`*__agg_snapshot_monthly`) | Snapshot já está agregado, congelado e tem o estado-de-verdade do mês de fechamento |

---

## 9. Cookbook — SQL snippets

✅ **Os snippets SQL estão prontos e disponíveis na versão ES-AR deste documento.**

👉 Ver [**§9 Cookbook — SQL snippets (ES-AR)**](#9-cookbook--sql-snippets-es)

O conteúdo é único — código SQL é language-agnostic. Para evitar duplicação e manter uma fonte única de verdade, os snippets completos vivem apenas na versão ES-AR. Cobrem:

- §9.1 Brand — Search Presence (DP3)
- §9.2 Brand — PR (Clipping)
- §9.3 Brand — Social
- §9.4 Acquisition — Funnel (DP1 + DP2)
- §9.5 Financial — GMV & Orders (DP4)
- §9.6 Snapshot mensal — padrão de consumo
- §9.7 Histórico 24 meses (template genérico)

> Use os parâmetros `:country`, `:business_unit`, `:month_label` (formato `'YYYY-MM'`) conforme a análise.

---

## 10. Backlog

Itens identificados como pendência de catalogação, definição ou validação. Não bloqueiam o uso atual do catálogo, mas precisam ser endereçados em versões futuras.

| # | Item | Domínio | Notas |
|---|---|---|---|
| B1 | **`finance_segment` (DP4)** | Financial | DP4 abre GMV em 7 buckets de finance segment (FP&A). Por enquanto **não usamos esse breakdown** no MBR — somamos todos os segments. Quando o time de FP&A consolidar a definição dos 7 buckets, retomar para detalhar a documentação e considerar inclusão em deepdives. |
| B2 | **Plans para GMV total / off-platform** | Financial | DP4 tem plan apenas para `on_platform_without_pos` e `pos`. Não há plan para `total` nem `off_platform`. Verificar com Ops como apresentar "GMV vs Plan" no MBR. |
| B3 | **Sources extras de `mkt_source`** | Acquisition | 8 sources (`Brand & Comms`, `Eea`, `Enp`, `Mandae`, `Mid-market`, `Nurturing`, `Product Marketing`, `Store Referral`) caem hoje em "Low Volume". Validar com Ops se algumas merecem subir para o Nível 2 (ex: Nurturing pode ser relevante como source própria). |
| B4 | **`forecast_new_sellers` em DP1** | Acquisition | Coluna `forecast_new_sellers` não existe no DP1 (todas outras têm). Reportar ao time de Data. |
| B5 | **Inconsistência de naming no DP1** | Acquisition | `effective_new_payments` × `forecast_payments` (sem o "new"). Reportar ao time de Data. |
| B6 | **Goals B&C (Branded Searches + Market Share)** | Brand | Validar com Beto se o arquivo de Goals B&C deve ser usado para Branded Searches/Market Share, ou se a fonte canônica é o snapshot DP3. Atualmente o catálogo usa DP3. |
| B7 | **SOV AI Platforms** | Brand | Hoje é Manual. Investigar se há fonte automatizável (ex: APIs de busca AI ou ferramentas de SOV em LLMs). |
| B8 | **DP5 — Merchant Base** | Company Metrics | Aguardar publicação. Quando ativo, migrar Net Adds, Merchant Base, Churn, Phoenix, Ajuste, Downsell de CSV placeholder para SQL. |
| B9 | **DP6 — Marketing Expenses & Headcount** | Acquisition · Investment | Aguardar publicação. Desbloqueia Spend, CAC. |
| B10 | **GMV per Seller + % Seller** | Financial · Productivity | Bloqueado até DP5 (denominador). Numerador já está disponível via DP4. |
| B11 | **Versões EN e ES do catálogo** | Documento | Após estabilização do conteúdo em PT, traduzir. |
| B12 | **Fonte de classificação por ICP** | Acquisition | A dimensão `icp` (§2.10) não tem tag por merchant em nenhum DP. A abertura por ICP é feita hoje com fonte externa (planilha). Definir fonte canônica e mapear nomenclatura antiga (ICP 1-4 + Fallback) ao framework novo (§1.2). |

---

## 11. Changelog

- **2026-06-09** — (9ª iteração) Renomeado o bucket **`Long Tail` → `Low Volume`** em todo o projeto (catálogo ES-AR + PT-BR, DOC_CONSTRUCTION, ANALYSIS_RULES, código `config.py`).
- **2026-06-02** — (8ª iteração) Auditoria de cobertura cruzando MBRs BR/AR/MX: adicionada dimensão **`icp`** (§2.10) com referência ao framework de §1.2; menção de abertura por ICP em §5.4 (Trials/NPs/CVR Trial→NP); item **B12** no backlog (fonte de classificação ICP pendente — sem tag em DP, nomenclatura antiga ICP 1-4+Fallback a mapear). Aplicado em ambos os idiomas. Demais gaps auditados ficaram fora: GMV by channel (on hold), CRM funnel (fora de escopo), AI Visibility (mantém Manual), estruturas de tabela Acq×Activation/Perf-vs-Budget (vão para DOC_CONSTRUCTION), domínio Lifecycle/PMM (não criado — coberto por NSs/Churn em outros domínios).
- **2026-06-02** — (7ª iteração) (1) **§6 Lifecycle renomeado para Company Metrics** em ambos os idiomas (heading, domain tags, anchors, glossário, KPI matrix, backlog, cross-references); (2) **KPI Matrix reorganizada**: coluna "Plan?" removida; ordem agora é Company Metrics · Financial · Acquisition · Brand; (3) **Cookbook SQL** unificado na versão ES-AR — versão PT-BR passa a apontar para o link, evitando duplicação de código.
- **2026-06-02** — (6ª iteração) §1.2 **ICPs reescrita** com o framework canônico de 5 segmentos (Platform Migrants, Social Sellers, Offline Sellers, Marketplace Sellers, D2C Starters, Affiliates/Dropshippers) tiered em Premium / Mid-Premium / SMBs. Aplicado em ambos os idiomas (ES-AR + PT-BR).
- **2026-06-02** — (5ª iteração) Investigação de GMV: off-platform é <1% do total em todos os países (Mar/26) → recomendação no §7.1 de usar `on_platform` como GMV principal. Adicionado **§10 Backlog** com 11 pendências (finance_segment, plans, sources extras, naming bugs do DP1, SOV AI, DP5/DP6, etc.).
- **2026-06-02** — (4ª iteração) **Hierarquia formal de 4 níveis para `mkt_source`** definida (§3.4 reescrita com tabela completa 16 → 8 → 4 → 2): Nível 1 raw (16), Nível 2 com Low Volume (8), Nível 3 mecânica de aquisição (Performance · Organic · Indirect · Low Volume), Nível 4 relação com marca (Branded · Non-Branded). Glossário §1.1 expandido com Low Volume + Performance/Organic/Indirect. SQL snippet §9.4 ganhou CTE com mapping CASE para todos os níveis. Anti-patterns §8.4 ganharam alertas sobre mistura de níveis e Others vs Low Volume.
- **2026-06-02** — (3ª iteração) Incorporação dos inputs da reunião de Ops: (1) **`mkt_source` é canônica** para breakdowns por source/lever — `plan_mkt_source_ops` relegado a uso plan-only; (2) **DP4 — GMV (Finance Segments)** ativo: adicionados ~8 KPIs de Volume (GMV total/on/off/POS em LC/USD/Finance USD + Orders + Avg Ticket) removendo placeholders; (3) **Snapshots mensais** dos 4 DPs documentados como padrão de consumo paralelo ao daily (3 famílias vs 6); (4) §3.4 expandido com 8 sources observadas em `mkt_source` ainda a classificar em Brand/Non-Brand com Ops; (5) anti-patterns novos (POS double-count, avg ticket via avg, daily-em-vez-de-snapshot, plan_mkt_source_ops em breakdowns); (6) §9.5 cookbook GMV + §9.6 padrão snapshot.
- **2026-06-02** — (2ª iteração do dia) Adicionados: **Índice navegável** com âncoras, **KPI Matrix** (visão de pássaro de todos os KPIs catalogados), **§8.4 Anti-patterns** (15 erros comuns com correção + porquê), **§9 Cookbook** (SQL snippets prontos por domínio + template histórico 24m).
- **2026-06-02** — Reestruturação para virar referência cross-time. Removidos filtros project-specific (country/BU). Adicionados: §1 Glossário (conceitos + ICPs + acrônimos), §2 Dicionário de Dimensões, tags taxonômicas (Domínio · Subdomínio), Related KPIs cruzados. Reorganização dos KPIs por domínio (Brand · Acquisition · Company Metrics · Financial). Adicionados KPIs antes ausentes do DP1/DP2: Bounced Sessions, Total/Organic Users, Avg Pageviews, Avg Session Duration, Payment Created At, New Seller Created At. Adicionado Share of Market — excl. Wix.
- **2026-05-25 → 2026-06-02 (anterior)** — Enriquecimento com schemas oficiais dos DPs e raw events. Cada KPI ativo ganha `Definição (schema)` literal + gotchas extraídas do schema.
- **2026-05-25** — Versão inicial.
