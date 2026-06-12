"""
MBR Automation — Fase 1: Data fetch
Reads all KPIs from Databricks (monthly snapshots) + CSV placeholder,
computes temporal comparisons, and writes a "data pack" JSON.

Aligned with KPI_CATALOG.md v2 (cookbook §9) and DOC_CONSTRUCTION.md.

Usage:
    python src/fetch.py
    (requires DATABRICKS_TOKEN, or loads it from `databricks auth token`)
"""
import os
import sys
import json
import math
import logging

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C

logging.basicConfig(level=logging.INFO, format="%(levelname)s  %(message)s")
log = logging.getLogger("fetch")


# ---------------------------------------------------------------------------
# Connection
# ---------------------------------------------------------------------------
def _connect():
    from databricks import sql
    token = os.environ.get("DATABRICKS_TOKEN", "")
    if not token:
        raise EnvironmentError("DATABRICKS_TOKEN not set.")
    return sql.connect(
        server_hostname=C.DATABRICKS_HOST.replace("https://", ""),
        http_path=C.DATABRICKS_HTTP_PATH,
        access_token=token,
    )


def _q(conn, sql_text: str) -> pd.DataFrame:
    with conn.cursor() as cur:
        cur.execute(sql_text)
        return cur.fetchall_arrow().to_pandas()


def _labels_in(labels: list) -> str:
    return ", ".join(f"'{m}'" for m in labels)


def _num(v, default=0.0):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return default
    return float(v)


def _ratio(num, den):
    num, den = _num(num), _num(den)
    return num / den if den else None


def _chg(curr, prior):
    curr, prior = _num(curr), _num(prior)
    return (curr - prior) / abs(prior) if prior else None


def _attain(real, plan):
    real, plan = _num(real), _num(plan)
    return real / plan if plan else None


def make_kpi(real, plan=None, prior=None, yoy=None, ytd=None, ytd_plan=None, ytd_prior=None):
    """Build a KPI dict. Only includes the comparison fields that are provided.
    Adds YTD / %Achv YTD / YoY YTD when YTD inputs are given (DOC_CONSTRUCTION T1)."""
    d = {"real": _num(real)}
    if plan is not None:      d["plan"] = _num(plan); d["attainment"] = _attain(real, plan)
    if prior is not None:     d["m1"] = _num(prior); d["mom"] = _chg(real, prior)
    if yoy is not None:       d["yoy"] = _num(yoy); d["yoy_pct"] = _chg(real, yoy)
    if ytd is not None:       d["ytd"] = _num(ytd)
    if ytd_plan is not None:  d["ytd_plan"] = _num(ytd_plan); d["attainment_ytd"] = _attain(ytd, ytd_plan)
    if ytd_prior is not None: d["yoy_ytd_pct"] = _chg(ytd, ytd_prior)
    return d


# ---------------------------------------------------------------------------
# Generic snapshot helpers
# ---------------------------------------------------------------------------
def _bu_filter():
    return f"country = '{C.COUNTRY}' AND business_unit = '{C.BUSINESS_UNIT}'"


def _snap_row(conn, table, exprs, month_label) -> dict:
    """Aggregate (SUM) snapshot metrics for one month into a dict."""
    sql = f"SELECT {exprs} FROM {table} WHERE {_bu_filter()} AND month_label = '{month_label}'"
    df = _q(conn, sql)
    return df.iloc[0].to_dict() if not df.empty else {}


def _snap_ytd(conn, table, exprs, labels) -> dict:
    sql = f"SELECT {exprs} FROM {table} WHERE {_bu_filter()} AND month_label IN ({_labels_in(labels)})"
    df = _q(conn, sql)
    return df.iloc[0].to_dict() if not df.empty else {}


# ---------------------------------------------------------------------------
# Acquisition — DP1 (meanclick) + DP2 (GA4 sessions)
# ---------------------------------------------------------------------------
_DP1_METRICS = """
    SUM(effective_trials)         AS trials,
    SUM(effective_new_payments)   AS nps,
    SUM(effective_new_sellers)    AS nss,
    SUM(effective_qls)            AS qls,
    SUM(expected_monthly_trials)        AS trials_plan,
    SUM(expected_monthly_new_payments)  AS nps_plan,
    SUM(expected_monthly_new_sellers)   AS nss_plan,
    SUM(expected_monthly_qls)           AS qls_plan
"""
_DP2_METRICS = """
    SUM(effective_total_sessions)   AS sessions,
    SUM(effective_total_users)      AS users,
    SUM(effective_organic_users)    AS organic_users,
    SUM(effective_bounced_sessions) AS bounced
"""


def fetch_acquisition(conn) -> dict:
    log.info("Acquisition (DP1 + DP2)...")
    out = {"macro": {}, "by_source": [], "history": {}}

    # --- Macro period values ---
    m   = _snap_row(conn, C.DP1_SNAPSHOT, _DP1_METRICS, C.MONTH_LABEL)
    pm  = _snap_row(conn, C.DP1_SNAPSHOT, _DP1_METRICS, C.PRIOR_MONTH_LABEL)
    yy  = _snap_row(conn, C.DP1_SNAPSHOT, _DP1_METRICS, C.PRIOR_YEAR_MONTH_LABEL)
    ytd  = _snap_ytd(conn, C.DP1_SNAPSHOT, _DP1_METRICS, C.YTD_MONTH_LABELS)
    ytdp = _snap_ytd(conn, C.DP1_SNAPSHOT, _DP1_METRICS, C.PRIOR_YEAR_YTD_MONTH_LABELS)
    s_m  = _snap_row(conn, C.DP2_SNAPSHOT, _DP2_METRICS, C.MONTH_LABEL)
    s_pm = _snap_row(conn, C.DP2_SNAPSHOT, _DP2_METRICS, C.PRIOR_MONTH_LABEL)
    s_yy = _snap_row(conn, C.DP2_SNAPSHOT, _DP2_METRICS, C.PRIOR_YEAR_MONTH_LABEL)
    s_ytd  = _snap_ytd(conn, C.DP2_SNAPSHOT, _DP2_METRICS, C.YTD_MONTH_LABELS)
    s_ytdp = _snap_ytd(conn, C.DP2_SNAPSHOT, _DP2_METRICS, C.PRIOR_YEAR_YTD_MONTH_LABELS)

    out["macro"] = {
        "sessions":     make_kpi(s_m.get("sessions"), None, s_pm.get("sessions"), s_yy.get("sessions"),
                                 s_ytd.get("sessions"), None, s_ytdp.get("sessions")),
        "trials":       make_kpi(m.get("trials"), m.get("trials_plan"), pm.get("trials"), yy.get("trials"),
                                 ytd.get("trials"), ytd.get("trials_plan"), ytdp.get("trials")),
        "new_payments": make_kpi(m.get("nps"), m.get("nps_plan"), pm.get("nps"), yy.get("nps"),
                                 ytd.get("nps"), ytd.get("nps_plan"), ytdp.get("nps")),
        "new_sellers":  make_kpi(m.get("nss"), m.get("nss_plan"), pm.get("nss"), yy.get("nss"),
                                 ytd.get("nss"), ytd.get("nss_plan"), ytdp.get("nss")),
        "qls":          make_kpi(m.get("qls"), m.get("qls_plan"), pm.get("qls"), yy.get("qls"),
                                 ytd.get("qls"), ytd.get("qls_plan"), ytdp.get("qls")),
        "cvr_session_trial": {"real": _ratio(m.get("trials"), s_m.get("sessions")),
                              "m1": _ratio(pm.get("trials"), s_pm.get("sessions")),
                              "ytd": _ratio(ytd.get("trials"), s_ytd.get("sessions"))},
        "cvr_trial_np":      {"real": _ratio(m.get("nps"), m.get("trials")),
                              "m1": _ratio(pm.get("nps"), pm.get("trials")),
                              "ytd": _ratio(ytd.get("nps"), ytd.get("trials"))},
    }

    # --- By source (Level 1 raw -> grouped in compute step) ---
    sql = f"""
        SELECT mkt_source,
               SUM(effective_trials)        AS trials,
               SUM(effective_new_payments)  AS nps,
               SUM(effective_new_sellers)   AS nss,
               SUM(expected_monthly_new_payments) AS nps_plan
        FROM {C.DP1_SNAPSHOT}
        WHERE {_bu_filter()} AND month_label = '{C.MONTH_LABEL}'
        GROUP BY mkt_source
    """
    out["by_source"] = _q(conn, sql).to_dict(orient="records")

    # --- History 24m (charts) ---
    sql_h = f"""
        SELECT month_label,
               SUM(effective_trials)       AS trials,
               SUM(effective_new_payments) AS nps
        FROM {C.DP1_SNAPSHOT}
        WHERE {_bu_filter()} AND month_label IN ({_labels_in(C.HISTORY_MONTH_LABELS)})
        GROUP BY month_label ORDER BY month_label
    """
    out["history"]["funnel"] = _q(conn, sql_h).to_dict(orient="records")
    sql_s = f"""
        SELECT month_label, SUM(effective_total_sessions) AS sessions
        FROM {C.DP2_SNAPSHOT}
        WHERE {_bu_filter()} AND month_label IN ({_labels_in(C.HISTORY_MONTH_LABELS)})
        GROUP BY month_label ORDER BY month_label
    """
    out["history"]["sessions"] = _q(conn, sql_s).to_dict(orient="records")
    return out


# ---------------------------------------------------------------------------
# Brand — DP3 (search) + raw events (PR, Social, Followers)
# ---------------------------------------------------------------------------
# NOTE: monthly snapshot columns drop the `_daily` suffix (not daily anymore)
_DP3_METRICS = """
    SUM(effective_branded_searches_sc)            AS bs_sc,
    SUM(effective_branded_clicks_sc)              AS clicks_sc,
    SUM(effective_branded_searches_tiendanube_kwp) AS bs_kwp,
    SUM(effective_d2c_searches_kwp)               AS d2c_kwp,
    SUM(effective_nonbranded_searches_kwp)        AS nonbranded_kwp,
    SUM(effective_total_market_searches_kwp)      AS total_market,
    SUM(expected_monthly_branded_searches_sc)     AS bs_sc_plan,
    MAX(expected_monthly_branded_share_tiendanube_kwp) AS som_plan
"""


def fetch_brand(conn) -> dict:
    log.info("Brand (DP3 + PR + Social)...")
    out = {"macro": {}, "pr": {}, "social": {}, "history": {}}

    m  = _snap_row(conn, C.DP3_SNAPSHOT, _DP3_METRICS, C.MONTH_LABEL)
    pm = _snap_row(conn, C.DP3_SNAPSHOT, _DP3_METRICS, C.PRIOR_MONTH_LABEL)
    yy = _snap_row(conn, C.DP3_SNAPSHOT, _DP3_METRICS, C.PRIOR_YEAR_MONTH_LABEL)
    ytd  = _snap_ytd(conn, C.DP3_SNAPSHOT, _DP3_METRICS, C.YTD_MONTH_LABELS)
    ytdp = _snap_ytd(conn, C.DP3_SNAPSHOT, _DP3_METRICS, C.PRIOR_YEAR_YTD_MONTH_LABELS)

    out["macro"] = {
        "branded_searches": make_kpi(m.get("bs_sc"), m.get("bs_sc_plan"), pm.get("bs_sc"), yy.get("bs_sc"),
                                     ytd.get("bs_sc"), ytd.get("bs_sc_plan"), ytdp.get("bs_sc")),
        "branded_ctr": {"real": _ratio(m.get("clicks_sc"), m.get("bs_sc")),
                        "m1": _ratio(pm.get("clicks_sc"), pm.get("bs_sc")),
                        "ytd": _ratio(ytd.get("clicks_sc"), ytd.get("bs_sc"))},
        "share_of_market": {"real": _ratio(m.get("bs_kwp"), m.get("d2c_kwp")),
                            "plan": _num(m.get("som_plan")),
                            "m1": _ratio(pm.get("bs_kwp"), pm.get("d2c_kwp")),
                            "ytd": _ratio(ytd.get("bs_kwp"), ytd.get("d2c_kwp"))},
        "total_market": make_kpi(m.get("total_market"), None, pm.get("total_market"), yy.get("total_market"),
                                 ytd.get("total_market"), None, ytdp.get("total_market")),
    }

    # PR (clipping) — raw event, by date_month
    def pr_row(label):
        sql = f"""
            SELECT COUNT(*) AS total,
                   SUM(CASE WHEN golden_media_flag THEN 1 ELSE 0 END) AS gold,
                   SUM(CASE WHEN tier=1 AND golden_media_flag=FALSE THEN 1 ELSE 0 END) AS tier1,
                   SUM(CASE WHEN tier=2 THEN 1 ELSE 0 END) AS tier2,
                   SUM(CASE WHEN origin_type='Original' THEN 1 ELSE 0 END) AS proactive,
                   SUM(COALESCE(reach,0)) AS reach
            FROM {C.CLIPPING_TABLE}
            WHERE country='{C.COUNTRY}' AND date_month='{label}'
        """
        df = _q(conn, sql)
        return df.iloc[0].to_dict() if not df.empty else {}
    pr_m, pr_pm = pr_row(C.MONTH_LABEL), pr_row(C.PRIOR_MONTH_LABEL)
    out["pr"] = {"month": pr_m, "prior_month": pr_pm}

    # Social insights + followers
    def soc_row(label):
        sql = f"""
            SELECT SUM(reach_total) AS reach_total, SUM(reach_organic) AS reach_organic,
                   SUM(reach_paid_total) AS reach_paid, SUM(reach_collab_third_party) AS reach_collab,
                   SUM(interactions_total) AS interactions
            FROM {C.SOCIAL_TABLE} WHERE country='{C.COUNTRY}' AND date_month='{label}'
        """
        df = _q(conn, sql)
        return df.iloc[0].to_dict() if not df.empty else {}
    def fol_row(label):
        sql = f"""
            SELECT MAX(profile_followers) AS followers, SUM(new_followers) AS net_followers
            FROM {C.FOLLOWERS_TABLE}
            WHERE country='{C.COUNTRY}' AND date_month='{label}' AND status='ok'
        """
        df = _q(conn, sql)
        return df.iloc[0].to_dict() if not df.empty else {}
    soc_m, soc_pm = soc_row(C.MONTH_LABEL), soc_row(C.PRIOR_MONTH_LABEL)
    fol_m, fol_pm = fol_row(C.MONTH_LABEL), fol_row(C.PRIOR_MONTH_LABEL)
    # goals
    sqlg = f"""SELECT SUM(publicaciones_totales_pr) AS pr_total_plan,
                      SUM(publicaciones_t1_pr) AS pr_t1_plan,
                      SUM(reach_social) AS reach_plan,
                      MAX(engagement_rate_social) AS eng_plan
               FROM {C.BC_GOALS_TABLE} WHERE country='{C.COUNTRY}' AND date_month='{C.MONTH_LABEL}'"""
    dfg = _q(conn, sqlg)
    goals = dfg.iloc[0].to_dict() if not dfg.empty else {}
    out["social"] = {"month": soc_m, "prior_month": soc_pm,
                     "followers_month": fol_m, "followers_prior_month": fol_pm}
    out["pr"]["goals"] = goals
    out["social"]["goals"] = goals

    # History 24m (DP3 snapshot)
    sql_h = f"""
        SELECT month_label,
               SUM(effective_branded_searches_sc) AS branded_searches,
               SUM(effective_branded_clicks_sc)   AS clicks,
               SUM(effective_total_market_searches_kwp) AS total_market,
               SUM(effective_branded_searches_tiendanube_kwp) AS branded_kwp,
               SUM(effective_nonbranded_searches_kwp) AS nonbranded_kwp,
               SUM(effective_d2c_searches_kwp) AS d2c_kwp
        FROM {C.DP3_SNAPSHOT}
        WHERE {_bu_filter()} AND month_label IN ({_labels_in(C.HISTORY_MONTH_LABELS)})
        GROUP BY month_label ORDER BY month_label
    """
    out["history"]["search"] = _q(conn, sql_h).to_dict(orient="records")
    return out


# ---------------------------------------------------------------------------
# Financial — DP4 (GMV)
# ---------------------------------------------------------------------------
# GMV principal = on-platform (catalog §7.1; off-platform <1%, so on ~= total)
_DP4_METRICS = """
    SUM(effective_gmv_on_platform_lc)          AS gmv_lc,
    SUM(effective_gmv_on_platform_usd)         AS gmv_usd,
    SUM(effective_gmv_on_platform_finance_usd) AS gmv_fin_usd,
    SUM(effective_gmv_on_platform_lc - effective_gmv_pos_lc) AS gmv_on_wo_pos_lc,
    SUM(effective_gmv_pos_lc)            AS gmv_pos_lc,
    SUM(effective_orders_on_platform)    AS orders,
    SUM(expected_monthly_gmv_on_platform_without_pos_lc) AS gmv_on_wo_pos_plan,
    SUM(expected_monthly_gmv_pos_lc)     AS gmv_pos_plan
"""


def fetch_financial(conn) -> dict:
    log.info("Financial (DP4)...")
    out = {"gmv": {}, "history": {}}
    m  = _snap_row(conn, C.DP4_SNAPSHOT, _DP4_METRICS, C.MONTH_LABEL)
    pm = _snap_row(conn, C.DP4_SNAPSHOT, _DP4_METRICS, C.PRIOR_MONTH_LABEL)
    yy = _snap_row(conn, C.DP4_SNAPSHOT, _DP4_METRICS, C.PRIOR_YEAR_MONTH_LABEL)
    ytd  = _snap_ytd(conn, C.DP4_SNAPSHOT, _DP4_METRICS, C.YTD_MONTH_LABELS)
    ytdp = _snap_ytd(conn, C.DP4_SNAPSHOT, _DP4_METRICS, C.PRIOR_YEAR_YTD_MONTH_LABELS)

    out["gmv"] = {
        "gmv_lc":      make_kpi(m.get("gmv_lc"), None, pm.get("gmv_lc"), yy.get("gmv_lc"),
                                ytd.get("gmv_lc"), None, ytdp.get("gmv_lc")),
        "gmv_usd":     make_kpi(m.get("gmv_usd"), None, pm.get("gmv_usd"), yy.get("gmv_usd"),
                                ytd.get("gmv_usd"), None, ytdp.get("gmv_usd")),
        "gmv_fin_usd": make_kpi(m.get("gmv_fin_usd"), None, pm.get("gmv_fin_usd"), yy.get("gmv_fin_usd")),
        "orders":      make_kpi(m.get("orders"), None, pm.get("orders"), yy.get("orders"),
                                ytd.get("orders"), None, ytdp.get("orders")),
        "avg_ticket":  {"real": _ratio(m.get("gmv_lc"), m.get("orders")),
                        "m1": _ratio(pm.get("gmv_lc"), pm.get("orders")),
                        "ytd": _ratio(ytd.get("gmv_lc"), ytd.get("orders"))},
        "gmv_pos":     make_kpi(m.get("gmv_pos_lc"), m.get("gmv_pos_plan"), pm.get("gmv_pos_lc")),
    }
    sql_h = f"""
        SELECT month_label, SUM(effective_gmv_on_platform_lc) AS gmv_lc,
               SUM(effective_gmv_on_platform_usd) AS gmv_usd
        FROM {C.DP4_SNAPSHOT}
        WHERE {_bu_filter()} AND month_label IN ({_labels_in(C.HISTORY_MONTH_LABELS)})
        GROUP BY month_label ORDER BY month_label
    """
    out["history"]["gmv"] = _q(conn, sql_h).to_dict(orient="records")
    return out


# ---------------------------------------------------------------------------
# Company Metrics — CSV placeholder
# ---------------------------------------------------------------------------
def fetch_company_metrics() -> dict:
    log.info("Company Metrics (CSV placeholder)...")
    # dtype=str: keep raw text so "97.690" isn't inferred as float 97.69 (loses trailing zero)
    raw = pd.read_csv(C.NET_ADDS_CSV, usecols=range(12), dtype=str)
    raw.columns = ["date", "country", "month_name", "ajuste", "churns", "net_adds",
                   "downsell_freemium", "first_payments", "new_phoenix", "old_phoenix",
                   "merchant_base", "churn_and_downgrade"]
    numcols = ["ajuste", "churns", "net_adds", "downsell_freemium", "first_payments",
               "new_phoenix", "old_phoenix", "merchant_base", "churn_and_downgrade"]
    for c in numcols:
        raw[c] = pd.to_numeric(
            raw[c].astype(str).str.strip().str.replace(".", "", regex=False).str.replace(",", ".", regex=False),
            errors="coerce").fillna(0)
    raw["month_label"] = pd.to_datetime(raw["date"], format="%d/%m/%Y", errors="coerce").dt.strftime("%Y-%m")
    br = raw[raw["country"] == C.COUNTRY].sort_values("month_label").reset_index(drop=True)

    def row(label):
        r = br[br["month_label"] == label]
        return r.iloc[0].to_dict() if not r.empty else {c: 0 for c in numcols}
    m, pm, yy = row(C.MONTH_LABEL), row(C.PRIOR_MONTH_LABEL), row(C.PRIOR_YEAR_MONTH_LABEL)

    def _ytd_sum(col, labels):
        return float(br[br["month_label"].isin(labels)][col].sum())

    def kpi(col, flow=True, inverted=False):
        d = {"real": _num(m.get(col)), "m1": _num(pm.get(col)), "mom": _chg(m.get(col), pm.get(col)),
             "yoy": _num(yy.get(col)), "yoy_pct": _chg(m.get(col), yy.get(col))}
        if flow:  # stock metrics (merchant_base, EOP) don't accumulate
            ytd = _ytd_sum(col, C.YTD_MONTH_LABELS)
            ytdp = _ytd_sum(col, C.PRIOR_YEAR_YTD_MONTH_LABELS)
            d["ytd"] = ytd
            d["yoy_ytd_pct"] = _chg(ytd, ytdp)
        return d

    hist = br[br["month_label"].isin(C.HISTORY_MONTH_LABELS)][
        ["month_label"] + numcols].to_dict(orient="records")
    return {
        "base": {"merchant_base": kpi("merchant_base", flow=False), "net_adds": kpi("net_adds"),
                 "first_payments": kpi("first_payments"), "churn_and_downgrade": kpi("churn_and_downgrade")},
        "components": {k: kpi(k) for k in ["first_payments", "new_phoenix", "old_phoenix",
                                           "churns", "downsell_freemium", "ajuste", "net_adds"]},
        "history": hist,
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def fetch_all() -> dict:
    conn = _connect()
    log.info(f"Connected. Fetching {C.COUNTRY} {C.MONTH_LABEL}...")
    pack = {
        "meta": {
            "country": C.COUNTRY, "business_unit": C.BUSINESS_UNIT,
            "month_label": C.MONTH_LABEL, "prior_month_label": C.PRIOR_MONTH_LABEL,
            "prior_year_month_label": C.PRIOR_YEAR_MONTH_LABEL,
            "history_labels": C.HISTORY_MONTH_LABELS,
        },
        "acquisition":     fetch_acquisition(conn),
        "brand":           fetch_brand(conn),
        "financial":       fetch_financial(conn),
        "company_metrics": fetch_company_metrics(),
    }
    conn.close()
    return pack


if __name__ == "__main__":
    if not os.environ.get("DATABRICKS_TOKEN"):
        import subprocess
        try:
            r = subprocess.run(["databricks", "auth", "token", "--profile", "databricks_mcp"],
                               capture_output=True, text=True, timeout=20)
            os.environ["DATABRICKS_TOKEN"] = json.loads(r.stdout).get("access_token", "")
            log.info("Token loaded from profile databricks_mcp")
        except Exception as e:
            log.error(f"Could not load token: {e}")
            sys.exit(1)

    os.makedirs(C.OUTPUT_DIR, exist_ok=True)
    pack = fetch_all()
    with open(C.DATA_PACK_PATH, "w", encoding="utf-8") as f:
        json.dump(pack, f, indent=2, ensure_ascii=False, default=str)
    log.info(f"Data pack saved: {C.DATA_PACK_PATH}")
