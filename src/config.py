"""
MBR Automation — Configuration
Central settings for the report generator. Aligned with KPI_CATALOG.md v2.

Override via environment variables:
  MBR_REFERENCE_DATE  (YYYY-MM-DD, first day of reference month)
  MBR_COUNTRY         (BR | AR | MX)
  MBR_BUSINESS_UNIT   (SMB)
  DATABRICKS_TOKEN
"""
import os
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


# ---------------------------------------------------------------------------
# Reference period
# ---------------------------------------------------------------------------
_ref = os.environ.get("MBR_REFERENCE_DATE", "2026-04-01")
REFERENCE_DATE: date = datetime.strptime(_ref, "%Y-%m-%d").date()

COUNTRY       = os.environ.get("MBR_COUNTRY", "BR")
BUSINESS_UNIT = os.environ.get("MBR_BUSINESS_UNIT", "SMB")

# Derived labels
MONTH_LABEL            = REFERENCE_DATE.strftime("%Y-%m")
PRIOR_MONTH_LABEL      = (REFERENCE_DATE - relativedelta(months=1)).strftime("%Y-%m")
PRIOR_YEAR_MONTH_LABEL = (REFERENCE_DATE - relativedelta(years=1)).strftime("%Y-%m")
YEAR_LABEL             = REFERENCE_DATE.strftime("%Y")

# YTD: January .. reference month (current + prior year)
YTD_MONTH_LABELS = [f"{REFERENCE_DATE.year}-{m:02d}" for m in range(1, REFERENCE_DATE.month + 1)]
PRIOR_YEAR_YTD_MONTH_LABELS = [f"{REFERENCE_DATE.year - 1}-{m:02d}" for m in range(1, REFERENCE_DATE.month + 1)]

# 24-month history window for charts (ends at reference month)
HISTORY_START       = REFERENCE_DATE - relativedelta(months=23)
HISTORY_START_LABEL = HISTORY_START.strftime("%Y-%m")
HISTORY_MONTH_LABELS = [
    (HISTORY_START + relativedelta(months=i)).strftime("%Y-%m") for i in range(24)
]


# ---------------------------------------------------------------------------
# Databricks
# ---------------------------------------------------------------------------
DATABRICKS_HOST      = os.environ.get("DATABRICKS_HOST", "https://dbc-83e77cbe-a29d.cloud.databricks.com")
DATABRICKS_HTTP_PATH = os.environ.get("DATABRICKS_HTTP_PATH", "/sql/1.0/warehouses/fcf2f11681b56dbd")
DATABRICKS_TOKEN     = os.environ.get("DATABRICKS_TOKEN", "")

CATALOG = "data_products_prd"
SCHEMA  = "data_marketing"
_P = f"{CATALOG}.{SCHEMA}"

# Data Products — daily (long history, for charts) + monthly snapshot (closed month, source of truth)
DP1_DAILY    = f"{_P}.g__general__meanclick_budget_forecast__agg_daily"
DP1_SNAPSHOT = f"{_P}.g__general__meanclick_budget_forecast__agg_snapshot_monthly"
DP2_DAILY    = f"{_P}.g__general__ga4_sessions_budget_forecast__agg_daily"
DP2_SNAPSHOT = f"{_P}.g__general__ga4_sessions_budget_forecast__agg_snapshot_monthly"
DP3_DAILY    = f"{_P}.g__general__gsc_kwp_searches_budget_forecast__agg_daily"
DP3_SNAPSHOT = f"{_P}.g__general__gsc_kwp_searches_budget_forecast__agg_snapshot_monthly"
DP4_SNAPSHOT = f"{_P}.g__general__gmv_finance_segments_budget_forecast__agg_snapshot_monthly"

# Raw event tables — Brand & Comms
CLIPPING_TABLE  = f"{_P}.s__brand_and_comms__clipping__event"
SOCIAL_TABLE    = f"{_P}.s__brand_and_comms__social_insights__event"
FOLLOWERS_TABLE = f"{_P}.s__brand_and_comms__instagram_followers__event"
BC_GOALS_TABLE  = f"{_P}.s__brand_and_comms__goals__event"


# ---------------------------------------------------------------------------
# mkt_source hierarchy (KPI_CATALOG.md §3.4)
# ---------------------------------------------------------------------------
LOW_VOLUME_SOURCES = [
    "Brand & Comms", "Eea", "Enp", "Mandae", "Mid-market",
    "Nurturing", "Others", "Product Marketing", "Store Referral",
]
# Level 2 core sources (everything else maps to itself; low-volume collapses)
LEVEL2_CORE = [
    "Performance Brand", "Organic", "Direct",
    "Performance No Brand", "Affiliates", "Partners", "Organic Growth",
]
# Level 4: Branded vs Non-Branded
BRANDED_SOURCES = ["Direct", "Organic", "Performance Brand"]

def level2(mkt_source: str) -> str:
    return "Low Volume" if mkt_source in LOW_VOLUME_SOURCES else mkt_source

def level4(mkt_source: str) -> str:
    return "Branded" if mkt_source in BRANDED_SOURCES else "Non-Branded"


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR    = os.path.join(_ROOT, "data")
FONTS_DIR   = os.path.join(_ROOT, "assets", "fonts")
OUTPUT_DIR  = os.path.join(_ROOT, "output")
CONTEXT_DIR = os.path.join(_ROOT, "context")
NET_ADDS_CSV = os.path.join(DATA_DIR, "net_adds_placeholder.csv")

DATA_PACK_PATH = os.path.join(OUTPUT_DIR, f"data_pack_{COUNTRY}_{MONTH_LABEL}.json")
CONTEXT_PATH   = os.path.join(CONTEXT_DIR, f"{MONTH_LABEL}_{COUNTRY}.md")
DOCX_PATH      = os.path.join(OUTPUT_DIR, f"MBR_{COUNTRY}_{MONTH_LABEL}.docx")
