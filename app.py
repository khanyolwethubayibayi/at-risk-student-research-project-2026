"""
Student At-Risk Dashboard
=========================
Report, data preparation, exploratory analysis and the Logistic Regression / Random Forest models for the
Diploma in Civil Engineering at-risk-student project, with shared sidebar filters.

Run with:  streamlit run app.py
"""
import streamlit as st

from data.loader import load_dataset
from sections import data_prep, eda, modeling, report
from utils.filters import apply_filters, filter_summary_caption, render_filters

st.set_page_config(page_title="Student At-Risk Dashboard", page_icon="🎓", layout="wide")


def main():
    st.sidebar.title("🎓 Student At-Risk Dashboard")
    page = st.sidebar.radio("Section", ["Report", "Data Preparation", "Exploratory Data Analysis",
                                        "Model Development"])
    data = load_dataset()
    if data is None:
        up = st.sidebar.file_uploader("Upload df_final.xlsx (or .csv)", type=["xlsx", "csv"])
        if up is not None:
            data = load_dataset(up)
    raw = df = filtered = log = None
    if data is not None:
        raw, df, log = data
        sel = render_filters(df)
        filtered = apply_filters(df, sel)
        st.sidebar.caption(filter_summary_caption(df, filtered))
    else:
        st.sidebar.info("Place df_final.xlsx in the data/ folder or upload it above to enable the data pages.")

    if page == "Report":
        report.render()
    elif page == "Data Preparation":
        data_prep.render(raw, df, log)
    elif page == "Exploratory Data Analysis":
        eda.render(filtered)
    else:
        modeling.render(filtered)


if __name__ == "__main__":
    main()
