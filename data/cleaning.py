"""The cleaning steps of the analysis notebook, as one reusable function."""
import numpy as np
import pandas as pd
from config import AGE_BINS, AGE_LABELS, RENAME_MAP, SUBJECT_COLUMNS

YES_NO = {1: "Yes", 0: "No", "Yes": "Yes", "No": "No", "Y": "Yes", "N": "No"}
CAT_IMPUTE = ["Gender", "Home Language", "Ethnic Group", "Previous Activity", "Matric Type",
              "Bursary Type", "Funded", "In Residence"]


def clean_dataset(raw: pd.DataFrame):
    """Return (clean dataframe, list of (step, value)) following the notebook."""
    log = []
    df = raw.copy()
    df.columns = df.columns.astype(str).str.strip()
    log.append(("Rows loaded", len(df)))
    if "Student_ID" in df:
        log.append(("Duplicated Student_ID", int(df["Student_ID"].duplicated().sum())))
    df = df.drop(columns=["Student_ID"], errors="ignore").rename(columns=RENAME_MAP)
    df[SUBJECT_COLUMNS] = df[SUBJECT_COLUMNS].apply(pd.to_numeric, errors="coerce")
    incomplete = df[SUBJECT_COLUMNS].isnull().any(axis=1)
    log.append(("Removed: missing a subject mark", int(incomplete.sum())))
    df = df.loc[~incomplete].reset_index(drop=True)
    for c in ["Funded", "In Residence", "At Risk"]:
        df[c] = df[c].map(YES_NO)
    if df["At Risk"].isna().any():
        raise ValueError("'At Risk' has values other than Yes/No")
    df["Gender"] = df["Gender"].replace({"F": "Female", "M": "Male"})
    cols = [c for c in CAT_IMPUTE if c in df]
    df[cols] = df[cols].fillna("Not Specified")
    q = pd.to_numeric(df["School Quintile"], errors="coerce")
    df["School Quintile"] = q.where(q.between(1, 5)).map(lambda v: "Others" if pd.isna(v) else str(int(v)))
    df["Age at Enrolment"] = pd.to_numeric(df["Age at Enrolment"], errors="coerce")
    df["Age Group"] = pd.cut(df["Age at Enrolment"], bins=AGE_BINS, labels=AGE_LABELS).astype(object)
    df["Age Group"] = df["Age Group"].fillna("Not Specified")
    df["Academic Year"] = df["Academic Year"].astype(str)
    df["At_Risk_Numeric"] = df["At Risk"].map({"Yes": 1, "No": 0})
    df["Average Mark"] = df[SUBJECT_COLUMNS].mean(axis=1)
    log.append(("Students kept", len(df)))
    return df, log


def outlier_table(df):
    rows = []
    for col in SUBJECT_COLUMNS + ["Age at Enrolment"]:
        s = df[col].dropna()
        q1, q3 = s.quantile(0.25), s.quantile(0.75)
        lo, hi = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
        n = int(((s < lo) | (s > hi)).sum())
        rows.append({"Variable": col, "Lower fence": lo, "Upper fence": hi, "Outliers": n,
                     "% of students": 100 * n / len(s)})
    return pd.DataFrame(rows).round(2)
