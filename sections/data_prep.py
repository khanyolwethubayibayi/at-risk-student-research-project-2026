"""Data Preparation page (cleaning steps of the analysis notebook)."""
import pandas as pd
import streamlit as st
from config import SUBJECT_COLUMNS
from data.cleaning import outlier_table


def render(raw, df, log):
    st.header("Data Preparation")
    if df is None:
        st.info("Load a dataset (data/df_final.xlsx or the sidebar upload) to see the cleaning summary.")
        return
    st.markdown("The student identifier is dropped, columns are renamed, only students with all ten subject marks "
                "are kept, labels are standardised, missing categories become *Not Specified* and school "
                "quintile is treated as a category (1 to 5, or *Others*).")
    st.subheader("Cleaning log")
    st.dataframe(pd.DataFrame(log, columns=["Step", "Value"]), hide_index=True, use_container_width=True)
    c1, c2 = st.columns(2)
    c1.subheader("Class balance")
    bal = df["At Risk"].value_counts().rename_axis("At risk").reset_index(name="Students")
    bal["Share (%)"] = (100 * bal["Students"] / len(df)).round(1)
    c1.dataframe(bal, hide_index=True, use_container_width=True)
    c2.subheader("Missing values (cleaned data)")
    miss = df.isna().sum().rename("Missing").reset_index().rename(columns={"index": "Column"})
    c2.dataframe(miss[miss["Missing"] > 0] if (miss["Missing"] > 0).any() else miss.head(0),
                 hide_index=True, use_container_width=True)
    st.subheader("Outlier check (1.5 x IQR rule)")
    st.dataframe(outlier_table(df), hide_index=True, use_container_width=True)
    st.subheader("Cleaned data preview")
    st.dataframe(df.drop(columns=["At_Risk_Numeric"]).head(10), use_container_width=True)
    st.caption("A mark below 50 in any of the ten subjects defines an at-risk student.")
