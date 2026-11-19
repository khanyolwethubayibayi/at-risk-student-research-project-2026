"""Exploratory Data Analysis page (analysis notebook)."""
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from config import CAT_TEST_COLS, SUBJECT_COLUMNS, TARGET_NUM
from core.stats import association_tests, at_risk_rate, subject_summary
from utils import plots


def _show(fig):
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def render(df):
    st.header("Exploratory Data Analysis")
    if df is None or len(df) == 0:
        st.info("No students to show. Load a dataset or relax the sidebar filters.")
        return
    tabs = st.tabs(["Overview", "Distributions", "At-risk rate", "Subjects", "Statistical tests"])
    cats = [c for c in CAT_TEST_COLS if c in df.columns]
    with tabs[0]:
        k = st.columns(4)
        k[0].metric("Students", f"{len(df):,}")
        k[1].metric("At risk", f"{int(df[TARGET_NUM].sum()):,}")
        k[2].metric("At-risk rate", f"{100 * df[TARGET_NUM].mean():.1f}%")
        k[3].metric("Average mark", f"{df['Average Mark'].mean():.1f}")
        _show(plots.count_plot(df, "At Risk"))
        if "Academic Year" in df:
            st.subheader("At-risk rate by academic year")
            st.dataframe(at_risk_rate(df, "Academic Year"), hide_index=True, use_container_width=True)
    with tabs[1]:
        col = st.selectbox("Variable", cats + ["Age at Enrolment"], key="dist_var")
        _show(plots.hist_plot(df, col) if col == "Age at Enrolment" else plots.count_plot(df, col))
        if col != "Age at Enrolment":
            t = df[col].astype(str).value_counts().rename_axis(col).reset_index(name="Students")
            t["Share (%)"] = (100 * t["Students"] / len(df)).round(1)
            st.dataframe(t, hide_index=True, use_container_width=True)
    with tabs[2]:
        col = st.selectbox("Variable", cats, key="rate_var")
        _show(plots.rate_plot(df, col))
        st.dataframe(at_risk_rate(df.assign(**{col: df[col].astype(str)}), col), hide_index=True,
                     use_container_width=True)
    with tabs[3]:
        summ = subject_summary(df)
        _show(plots.failure_plot(summ))
        st.dataframe(summ.round(2), hide_index=True, use_container_width=True)
        _show(plots.marks_box(df, SUBJECT_COLUMNS))
    with tabs[4]:
        st.markdown("Chi-square tests of independence (categorical variables) and a Mann-Whitney U test (age) "
                    "against at-risk status, with Holm-Bonferroni adjustment across all tests.")
        res = association_tests(df)
        if res.empty:
            st.info("Not enough variation in the selected students to run the tests.")
        else:
            st.dataframe(res.style.format({"Statistic": "{:.3f}", "p (raw)": "{:.4f}",
                                           "p (Holm-adjusted)": "{:.4f}", "Effect size": "{:.3f}"}),
                         hide_index=True, use_container_width=True)
            st.caption("Effect size: Cramer's V (chi-square) or rank-biserial correlation (Mann-Whitney U). "
                       "Tests on a small filtered group have little power, so a non-significant result "
                       "is not evidence of no effect.")
        col = st.selectbox("Cross-tabulation", cats, key="ct_var")
        ct = pd.crosstab(df[col], df["At Risk"])
        st.dataframe(ct, use_container_width=True)
