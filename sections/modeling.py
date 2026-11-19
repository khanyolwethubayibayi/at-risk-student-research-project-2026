"""Model Development page (model notebook): live Logistic Regression and Random Forest."""
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from config import FAIL_MARK, REPORTED, REPORTED_COLS, SUBJECT_COLUMNS, TARGET_NUM
from core import modeling as M
from utils import plots


@st.cache_resource(show_spinner="Training the models...")
def _fit(df, rf_trees, n_boot):
    return M.fit_all(df, rf_trees, n_boot)


@st.cache_resource(show_spinner="Running cross-validation (this can take a minute)...")
def _cv(df, repeats, rf_trees):
    return M.run_cv(df, repeats, rf_trees)


def _show(fig):
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def render(df):
    st.header("Model Development")
    if df is None or len(df) == 0:
        st.info("Load a dataset to train the models.")
        return
    if not M.enough_data(df):
        st.warning("Too few students (or too few at-risk / not-at-risk students) after filtering. "
                   "Relax the sidebar filters to train the models.")
        return
    st.markdown("Logistic Regression and Random Forest are trained on a stratified 70/30 split of the selected "
                "students. **Set A** uses background variables only; **Set B** adds the ten subject marks.")
    st.info("At-risk status is defined from the same subject marks used in Set B "
            "(a mark below %d in any subject), so Set B shows an upper bound and not a true forecast. "
            "Set A is the realistic early-warning scenario." % FAIL_MARK)
    rule = ((df[SUBJECT_COLUMNS].min(axis=1) < FAIL_MARK).astype(int) == df[TARGET_NUM]).mean()
    st.caption(f"The rule 'any mark below {FAIL_MARK}' matches the at-risk label for {rule:.1%} of these students.")
    with st.expander("Settings"):
        rf_trees = st.slider("Random Forest trees", 50, 500, 300, 50)
        n_boot = st.select_slider("Bootstrap resamples for the AUC interval", [200, 500, 1000], value=500)
        thr = st.slider("Classification threshold", 0.1, 0.9, 0.5, 0.05)
        st.caption("Lower thresholds raise recall (fewer missed at-risk students) at the cost of more false alarms. "
                   "Live models use default hyperparameters; tuned results are under 'Reported results'.")
    res = _fit(df, rf_trees, n_boot)
    st.caption(f"Training students: {len(res['y_train'])} | Test students: {len(res['y_test'])} "
               f"({int(res['y_test'].sum())} at risk)")
    labels = list(M.FEATURE_SETS)
    tabs = st.tabs(["Test-set results", "Confusion matrices", "ROC curves", "Importance",
                    "Cross-validation", "Reported results"])
    with tabs[0]:
        for lab in labels:
            st.subheader(lab)
            st.dataframe(M.test_table(res, lab, thr).style.format("{:.3f}"), use_container_width=True)
    with tabs[1]:
        model = st.radio("Model", M.MODEL_NAMES[1:], horizontal=True, key="cm_model")
        cols = st.columns(2)
        for c, lab in zip(cols, labels):
            cm = M.confusion(res, lab, model, thr)
            with c:
                _show(plots.confusion_plot(cm, f"{model}\nSet {lab[0]}"))
                tn, fp, fn, tp = cm.ravel()
                st.caption(f"Caught {tp} of {tp + fn} at-risk students (recall {tp / max(tp + fn, 1):.1%}); "
                           f"{fn} missed, {fp} false alarms.")
    with tabs[2]:
        cols = st.columns(2)
        for c, lab in zip(cols, labels):
            with c:
                _show(plots.roc_plot(res["y_test"], {n: res["proba"][lab][n] for n in M.MODEL_NAMES[1:]},
                                     f"ROC curves, Set {lab[0]}"))
    with tabs[3]:
        lab = st.radio("Feature set", labels, index=1, horizontal=True, key="imp_set")
        feats = M.FEATURE_SETS[lab]
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Logistic Regression odds ratios** (top 15; marks are per 1 standard deviation)")
            orr = M.odds_ratios(res["fitted"][lab]["Logistic Regression"]).head(15)
            _show(plots.hbar(orr["Predictor"], orr["Odds ratio"], "Odds ratio (1 = no effect)", "Odds ratio", ref=1))
        with c2:
            st.markdown("**Random Forest impurity importance** (top 15)")
            imp = M.rf_importance(res["fitted"][lab]["Random Forest"], feats).head(15)
            _show(plots.hbar(imp["Variable"], imp["Importance"], "Impurity importance", "Importance"))
        st.markdown("**Permutation importance on the test set** (drop in ROC-AUC when a variable is shuffled)")
        c1, c2 = st.columns(2)
        for c, name in zip((c1, c2), M.MODEL_NAMES[1:]):
            with c:
                p = M.perm_importance(res["fitted"][lab][name], res["X_test"][lab], res["y_test"], 10).head(12)
                _show(plots.hbar(p["Variable"], p["Drop in ROC-AUC"], name, "Drop in ROC-AUC", ref=0))
        st.caption("Importance shows how much a variable matters, not the direction of its effect. "
                   "Correlated variables share importance.")
    with tabs[4]:
        reps = st.select_slider("Repeats of 10-fold cross-validation", [1, 2, 3], value=1)
        if st.button("Run cross-validation"):
            for lab, tbl in _cv(df, reps, rf_trees).items():
                st.subheader(lab)
                st.dataframe(tbl.style.format("{:.3f}"), use_container_width=True)
        st.caption("The report used 10 folds x 3 repeats on the training set only.")
    with tabs[5]:
        st.markdown("Full-dataset results from the written report (Tables 4.13 and 4.14), including the tuned models.")
        for name, rows in REPORTED.items():
            st.subheader(name)
            st.dataframe(pd.DataFrame(rows, columns=REPORTED_COLS), hide_index=True, use_container_width=True)
