"""Association tests and descriptive tables (same method as the analysis notebook)."""
import numpy as np
import pandas as pd
from scipy import stats
from config import CAT_TEST_COLS, NUM_TEST_COLS, SUBJECT_COLUMNS, TARGET_NUM


def holm_adjust(p_values):
    p = np.asarray(p_values, dtype=float)
    out = np.full(len(p), np.nan)
    idx = np.where(~np.isnan(p))[0]
    running, m = 0.0, len(idx)
    for rank, i in enumerate(idx[np.argsort(p[idx])]):
        running = max(running, (m - rank) * p[i])
        out[i] = min(1.0, running)
    return out


def association_tests(df):
    """Chi-square (categorical) and Mann-Whitney U (age) vs at-risk, Holm-adjusted."""
    rows = []
    for col in [c for c in CAT_TEST_COLS if c in df]:
        ct = pd.crosstab(df[col], df[TARGET_NUM])
        if ct.shape[0] < 2 or ct.shape[1] < 2:
            continue
        chi2, p, _, exp = stats.chi2_contingency(ct)
        k = min(ct.shape) - 1
        rows.append({"Feature": col, "Test": "Chi-square", "Statistic": chi2, "p (raw)": p,
                     "Effect size": np.sqrt(chi2 / (ct.values.sum() * k)) if k > 0 else 0.0,
                     "Cells with expected < 5": int((exp < 5).sum())})
    for col in [c for c in NUM_TEST_COLS if c in df]:
        a = df.loc[df[TARGET_NUM] == 1, col].dropna()
        b = df.loc[df[TARGET_NUM] == 0, col].dropna()
        if len(a) < 2 or len(b) < 2:
            continue
        u, p = stats.mannwhitneyu(a, b, alternative="two-sided")
        rows.append({"Feature": col, "Test": "Mann-Whitney U", "Statistic": u, "p (raw)": p,
                     "Effect size": abs(1 - 2 * u / (len(a) * len(b))), "Cells with expected < 5": np.nan})
    res = pd.DataFrame(rows)
    if res.empty:
        return res
    res["p (Holm-adjusted)"] = holm_adjust(res["p (raw)"])
    res["Significant (alpha = 0.05)"] = np.where(res["p (Holm-adjusted)"] < 0.05, "Yes", "No")
    return res.sort_values("p (raw)").reset_index(drop=True)


def at_risk_rate(df, col):
    g = df.groupby(col)[TARGET_NUM].agg(["count", "sum", "mean"]).reset_index()
    g.columns = [col, "Students", "At risk", "At-risk rate (%)"]
    g["At-risk rate (%)"] = (g["At-risk rate (%)"] * 100).round(1)
    return g


def subject_summary(df):
    n = len(df)
    rows = []
    for s in SUBJECT_COLUMNS:
        f = int((df[s] < 50).sum())
        r = f / n
        half = 1.96 * np.sqrt(r * (1 - r) / n)
        rows.append({"Subject": s, "Failures": f, "Failure rate (%)": 100 * r, "Pass rate (%)": 100 * (1 - r),
                     "95% CI low": 100 * max(0, r - half), "95% CI high": 100 * min(1, r + half),
                     "Students 50-59%": int(df[s].between(50, 59.999).sum()),
                     "Mean mark": df[s].mean(), "Median mark": df[s].median()})
    return pd.DataFrame(rows).sort_values("Failures", ascending=False).reset_index(drop=True)
