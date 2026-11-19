"""Sidebar filters shared by the EDA and modelling pages."""
import pandas as pd
import streamlit as st
from config import FILTERABLE_COLUMNS


def _key(v):
    return (0, int(v), "") if str(v).isdigit() else (1, 0, str(v))


def render_filters(df):
    sel = {}
    with st.sidebar.expander("Filters (leave empty = all)", expanded=False):
        for col, label in FILTERABLE_COLUMNS.items():
            if col in df.columns:
                opts = sorted(df[col].dropna().astype(str).unique(), key=_key)
                sel[col] = st.multiselect(label, opts, key=f"flt_{col}")
    return sel


def apply_filters(df, sel):
    mask = pd.Series(True, index=df.index)
    for col, vals in sel.items():
        if vals:
            mask &= df[col].astype(str).isin(vals)
    return df.loc[mask].reset_index(drop=True)


def filter_summary_caption(df, filtered):
    return f"Showing {len(filtered):,} of {len(df):,} students"
