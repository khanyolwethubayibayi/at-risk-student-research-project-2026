"""Logistic Regression / Random Forest pipelines (same design as the model notebook)."""
import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, make_scorer, precision_score,
                             recall_score, roc_auc_score)
from sklearn.model_selection import RepeatedStratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from config import BACKGROUND, NUMERIC_COLS, RANDOM_STATE, SUBJECT_COLUMNS, TARGET_NUM, TEST_SIZE

FEATURE_SETS = {"A: Without marks": BACKGROUND, "B: With marks": BACKGROUND + SUBJECT_COLUMNS}
MODEL_NAMES = ["Baseline (Majority)", "Logistic Regression", "Random Forest"]


def enough_data(df):
    n, pos = len(df), int(df[TARGET_NUM].sum())
    return n >= 80 and pos >= 15 and (n - pos) >= 15


def build_pipeline(features, name, rf_trees=300):
    num = [c for c in features if c in NUMERIC_COLS]
    cat = [c for c in features if c not in NUMERIC_COLS]
    pre = ColumnTransformer([
        ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]), num),
        ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                          ("onehot", OneHotEncoder(handle_unknown="ignore"))]), cat)])
    model = {"Baseline (Majority)": DummyClassifier(strategy="most_frequent"),
             "Logistic Regression": LogisticRegression(class_weight="balanced", max_iter=1000,
                                                       random_state=RANDOM_STATE),
             "Random Forest": RandomForestClassifier(n_estimators=rf_trees, min_samples_leaf=3,
                                                     class_weight="balanced", random_state=RANDOM_STATE,
                                                     n_jobs=-1)}[name]
    return Pipeline([("preprocessor", pre), ("model", clone(model))])


def auc_ci(y, proba, n_boot=500, seed=RANDOM_STATE):
    rng = np.random.default_rng(seed)
    y, p = np.asarray(y), np.asarray(proba)
    aucs = []
    for _ in range(n_boot):
        i = rng.integers(0, len(y), len(y))
        if len(np.unique(y[i])) == 2:
            aucs.append(roc_auc_score(y[i], p[i]))
    return tuple(np.percentile(aucs, [2.5, 97.5])) if aucs else (np.nan, np.nan)


def metrics_at(y, proba, thr=0.5):
    pred = (np.asarray(proba) >= thr).astype(int)
    return {"Accuracy": accuracy_score(y, pred), "Precision": precision_score(y, pred, zero_division=0),
            "Recall": recall_score(y, pred, zero_division=0), "F1-Score": f1_score(y, pred, zero_division=0),
            "ROC-AUC": roc_auc_score(y, proba)}


def fit_all(df, rf_trees=300, n_boot=500):
    """Stratified 70/30 split, fit every model on every feature set, keep test probabilities."""
    y = df[TARGET_NUM]
    tr, te = train_test_split(df.index, test_size=TEST_SIZE, stratify=y, random_state=RANDOM_STATE)
    out = {"y_train": y.loc[tr], "y_test": y.loc[te], "X_train": {}, "X_test": {}, "fitted": {},
           "proba": {}, "ci": {}}
    for label, feats in FEATURE_SETS.items():
        out["X_train"][label], out["X_test"][label] = df.loc[tr, feats], df.loc[te, feats]
        out["fitted"][label], out["proba"][label], out["ci"][label] = {}, {}, {}
        for name in MODEL_NAMES:
            pipe = build_pipeline(feats, name, rf_trees).fit(out["X_train"][label], out["y_train"])
            p = pipe.predict_proba(out["X_test"][label])[:, 1]
            out["fitted"][label][name], out["proba"][label][name] = pipe, p
            out["ci"][label][name] = auc_ci(out["y_test"], p, n_boot)
    return out


def test_table(res, label, thr=0.5):
    rows = {}
    for name in MODEL_NAMES:
        m = metrics_at(res["y_test"], res["proba"][label][name], thr)
        lo, hi = res["ci"][label][name]
        m["AUC 95% CI low"], m["AUC 95% CI high"] = lo, hi
        rows[name] = m
    return pd.DataFrame(rows).T


def confusion(res, label, name, thr=0.5):
    pred = (res["proba"][label][name] >= thr).astype(int)
    return confusion_matrix(res["y_test"], pred, labels=[0, 1])


def run_cv(df, repeats=1, rf_trees=300):
    """Stratified 10-fold cross-validation on the training set (repeats x 10 scores per model)."""
    y = df[TARGET_NUM]
    tr, _ = train_test_split(df.index, test_size=TEST_SIZE, stratify=y, random_state=RANDOM_STATE)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=repeats, random_state=RANDOM_STATE)
    scoring = {"accuracy": "accuracy", "precision": make_scorer(precision_score, zero_division=0),
               "recall": "recall", "f1": make_scorer(f1_score, zero_division=0), "roc_auc": "roc_auc"}
    out = {}
    for label, feats in FEATURE_SETS.items():
        rows = {}
        for name in MODEL_NAMES:
            s = cross_validate(build_pipeline(feats, name, rf_trees), df.loc[tr, feats], y.loc[tr],
                               cv=cv, scoring=scoring, n_jobs=-1)
            rows[name] = {"Accuracy": s["test_accuracy"].mean(), "Precision": s["test_precision"].mean(),
                          "Recall": s["test_recall"].mean(), "F1-Score": s["test_f1"].mean(),
                          "ROC-AUC": s["test_roc_auc"].mean(), "ROC-AUC SD": s["test_roc_auc"].std()}
        out[label] = pd.DataFrame(rows).T
    return out


def odds_ratios(pipe):
    names = pipe.named_steps["preprocessor"].get_feature_names_out()
    coef = pipe.named_steps["model"].coef_[0]
    t = pd.DataFrame({"Predictor": [n.split("__", 1)[1] for n in names], "Odds ratio": np.exp(coef)})
    t["Distance from 1"] = (np.log(t["Odds ratio"])).abs()
    return t.sort_values("Distance from 1", ascending=False).drop(columns="Distance from 1").reset_index(drop=True)


def rf_importance(pipe, features):
    names = pipe.named_steps["preprocessor"].get_feature_names_out()
    imp = pipe.named_steps["model"].feature_importances_
    tot = {c: 0.0 for c in features}
    for n, v in zip(names, imp):
        body = n.split("__", 1)[1]
        match = [c for c in features if body == c or body.startswith(c + "_")]
        if match:
            tot[max(match, key=len)] += v
    return pd.Series(tot).sort_values(ascending=False).rename("Importance").reset_index().rename(
        columns={"index": "Variable"})


def perm_importance(pipe, X_test, y_test, n_repeats=10):
    r = permutation_importance(pipe, X_test, y_test, scoring="roc_auc", n_repeats=n_repeats,
                               random_state=RANDOM_STATE)
    return pd.DataFrame({"Variable": X_test.columns, "Drop in ROC-AUC": r.importances_mean,
                         "SD": r.importances_std}).sort_values("Drop in ROC-AUC", ascending=False
                                                               ).reset_index(drop=True)
