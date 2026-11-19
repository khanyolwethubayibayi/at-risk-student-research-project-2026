"""Central configuration for the Student At-Risk web app."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FINAL_DATA_PATH = ROOT / "data" / "df_final.xlsx"   # not committed to Git (confidential)
REPORT_DIR = ROOT / "report_content"
FIG_DIR = ROOT / "assets" / "figures"

# Raw -> short column names (same mapping as the notebooks)
RENAME_MAP = {
    "APPLIED MECHANICS": "Applied Mechanics", "COMPUTER SKILLS": "Computer Skills",
    "CONSTRUCTION MATERIALS TECHNOLOGY": "Construction Materials",
    "ENGINEERING CHEMISTRY": "Engineering Chemistry", "ENGINEERING DRAWING 1": "Engineering Drawing 1",
    "ENGINEERING MATHEMATICS 1": "Engineering Mathematics 1", "ENGINEERING PHYSICS": "Engineering Physics",
    "PROFESSIONAL AND TECHNICAL COMMUNICATION": "Professional Communication",
    "SURVEYING": "Surveying", "THEORY OF STRUCTURES": "Theory of Structures",
    "Language Name": "Home Language", "Ethnic Group Name": "Ethnic Group",
    "Previous Activity Desc": "Previous Activity", "Age_At_Enrolment": "Age at Enrolment",
    "Residence_Status": "In Residence", "Secondary_School_Quintile": "School Quintile",
    "At_Risk_Status": "At Risk",
}
SUBJECT_COLUMNS = ["Applied Mechanics", "Computer Skills", "Construction Materials", "Engineering Chemistry",
                   "Engineering Drawing 1", "Engineering Mathematics 1", "Engineering Physics",
                   "Professional Communication", "Surveying", "Theory of Structures"]
BACKGROUND = ["Gender", "Home Language", "Ethnic Group", "Previous Activity", "Matric Type",
              "Age at Enrolment", "Bursary Type", "Funded", "In Residence", "School Quintile"]
NUMERIC_COLS = ["Age at Enrolment"] + SUBJECT_COLUMNS
TARGET, TARGET_NUM = "At Risk", "At_Risk_Numeric"
CAT_TEST_COLS = ["Academic Year", "Gender", "Home Language", "Ethnic Group", "Previous Activity", "Matric Type",
                 "Bursary Type", "Funded", "In Residence", "School Quintile", "Age Group"]
NUM_TEST_COLS = ["Age at Enrolment"]
AGE_BINS, AGE_LABELS = [0, 18, 19, 20, 100], ["18 or younger", "19", "20", "21 or older"]
FAIL_MARK, TEST_SIZE, RANDOM_STATE = 50, 0.30, 42

FILTERABLE_COLUMNS = {
    "In Residence": "In Residence", "At Risk": "At Risk", "School Quintile": "School Quintile",
    "Gender": "Gender", "Academic Year": "Academic Year", "Funded": "Funded", "Bursary Type": "Bursary Type",
    "Home Language": "Home Language", "Ethnic Group": "Ethnic Group",
    "Previous Activity": "Previous Activity", "Matric Type": "Matric Type", "Age Group": "Age Group",
}
REQUIRED_RAW = list(RENAME_MAP) + ["Gender", "Academic Year", "Matric Type", "Bursary Type", "Funded"]

# Results reported in the written report (full dataset, tuned models, Tables 4.13 and 4.14)
REPORTED = {
    "Logistic Regression": [
        ["Without marks (Set A)", 0.596, 0.455, 0.556, 0.500, "0.572 (0.453-0.695)", "Default settings"],
        ["With marks (Set B)", 0.859, 0.824, 0.778, 0.800, "0.932 (0.878-0.974)", "Default settings"],
        ["Tuned, with marks (Set B)", 0.808, 0.730, 0.750, 0.740, "0.915 (0.857-0.962)", "C = 0.1; solver = liblinear"]],
    "Random Forest": [
        ["Without marks (Set A)", 0.535, 0.381, 0.444, 0.410, "0.497 (0.376-0.619)", "Default settings"],
        ["With marks (Set B)", 0.869, 0.848, 0.778, 0.812, "0.940 (0.895-0.977)", "Default settings"],
        ["Tuned, with marks (Set B)", 0.869, 0.871, 0.750, 0.806, "0.937 (0.887-0.977)", "max_depth = 8"]],
}
REPORTED_COLS = ["Scenario", "Accuracy", "Precision", "Recall", "F1-score", "ROC-AUC (95% CI)", "Best parameters"]
