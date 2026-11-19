"""Load df_final.xlsx (or an uploaded file) and clean it."""
import pandas as pd
import streamlit as st
from config import FINAL_DATA_PATH, REQUIRED_RAW
from data.cleaning import clean_dataset


@st.cache_data(show_spinner=False)
def _clean(raw):
    return clean_dataset(raw)


def load_dataset(uploaded=None):
    """Return (raw, clean, log) or None. Student IDs are dropped during cleaning."""
    try:
        if uploaded is not None:
            raw = pd.read_csv(uploaded) if uploaded.name.lower().endswith(".csv") else pd.read_excel(uploaded)
        elif FINAL_DATA_PATH.exists():
            raw = pd.read_excel(FINAL_DATA_PATH)
        else:
            return None
    except Exception as exc:  # unreadable file
        st.sidebar.error(f"Could not read the file: {exc}")
        return None
    raw.columns = raw.columns.astype(str).str.strip()
    missing = [c for c in REQUIRED_RAW if c not in raw.columns]
    if missing:
        st.sidebar.error("The file is missing columns: " + ", ".join(missing))
        return None
    clean, log = _clean(raw)
    return raw, clean, log
