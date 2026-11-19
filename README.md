# Student At-Risk Dashboard

A Streamlit app for the project *Machine Learning Approach for Identification of At-Risk Students in the
Diploma in Civil Engineering* (CPUT). It brings together the written report, the data preparation, the
exploratory analysis (`Student_at_risk_data_analysis.ipynb`) and the Logistic Regression and Random Forest
models (`Student_at_risk_model_development.ipynb`), with shared sidebar filters.

## 1. Install

```bash
cd student_risk_app
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Add your data

Put the dataset at `data/df_final.xlsx` (the file both notebooks load). If it is missing, the sidebar shows an
upload box (`.xlsx` or `.csv`). **The data contains confidential student records and is excluded from Git by
`.gitignore`. Do not commit it.**

## 3. Run

```bash
streamlit run app.py
```

## 4. Pages

| Page | What it shows |
|---|---|
| Report | The written report chapter by chapter, with its 30 figures |
| Data Preparation | Cleaning log, class balance, missing values, outlier check |
| Exploratory Data Analysis | Distributions, at-risk rate by variable, subject analysis, Holm-adjusted association tests |
| Model Development | Set A (no marks) vs Set B (with marks): test metrics, confusion matrices, ROC curves, odds ratios, importance, cross-validation, and the reported tuned results |

Sidebar filters (residence, at-risk status, school quintile, gender, academic year, funding, bursary, language,
ethnic group, previous activity, matric type, age group) apply to the EDA and Model pages. Leave a filter empty
to include everyone.

## 5. Structure

```
app.py                  entry point and navigation
config.py               column names, feature sets, constants, reported results
data/cleaning.py        the notebook's cleaning steps as a function
data/loader.py          loads df_final.xlsx (or an upload) and cleans it
core/stats.py           chi-square / Mann-Whitney tests, Holm adjustment, subject summary
core/modeling.py        pipelines, split, metrics, bootstrap AUC interval, importance
sections/               one module per page
utils/                  filters and plotting helpers
tools/rebuild_report.py Word report -> report_content/*.md + assets/figures
report_content/, assets/figures/   generated from the Word report
```

## 6. Updating the report

`report_content/` is a one-time export of the Word report. After editing the document, either use "Update
report from a new Word document" on the Report page, or run:

```bash
python tools/rebuild_report.py "path/to/report.docx"
```

If you rename a chapter heading, update
`CHAPTER_MAP` in the tool. The report text and figures are public if this repository is public.

## 7. Notes

- The app mirrors the notebooks: stratified 70/30 split, seed 42, median/mode imputation, standardised marks,
  one-hot categories, balanced class weights, Random Forest with 300 trees and 3 observations per leaf.
- Live models use **default hyperparameters** and retrain on the filtered students, so results change with the
  filters and with very small groups they are unreliable (the app asks for at least 80 students with 15 in each
  class). The tuned, full-dataset results are on the "Reported results" tab.
- At-risk status is defined from the same marks used in Set B, so Set B is an upper bound, not a forecast.
