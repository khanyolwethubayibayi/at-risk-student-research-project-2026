"""Matplotlib helpers used by the EDA and modelling pages."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import roc_curve
from config import AGE_LABELS, TARGET_NUM

ORDER = {"School Quintile": ["1", "2", "3", "4", "5", "Others"], "Age Group": AGE_LABELS + ["Not Specified"]}
sns.set_style("whitegrid")


def _order(df, col):
    present = list(df[col].dropna().astype(str).unique())
    if col in ORDER:
        return [c for c in ORDER[col] if c in present]
    return list(df[col].astype(str).value_counts().index)


def _rot(ax, labels):
    if len(labels) > 6 or max(len(str(l)) for l in labels) > 10:
        plt.setp(ax.get_xticklabels(), rotation=35, ha="right")


def count_plot(df, col, top_n=12):
    order = _order(df, col)[:top_n]
    counts = df[col].astype(str).value_counts().reindex(order)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    sns.barplot(x=counts.index, y=counts.values, hue=counts.index, palette="viridis", legend=False, ax=ax)
    for i, v in enumerate(counts.values):
        ax.text(i, v, f"{v:,}\n({100 * v / counts.sum():.1f}%)", ha="center", va="bottom", fontsize=8)
    ax.set_xlabel(col); ax.set_ylabel("Students"); ax.margins(y=0.2); _rot(ax, order)
    ax.set_title(f"{col} distribution", fontweight="bold", fontsize=11)
    fig.tight_layout()
    return fig


def hist_plot(df, col):
    fig, ax = plt.subplots(figsize=(7, 3.6))
    sns.histplot(df[col].dropna(), bins=15, color="#3b6a8a", ax=ax)
    ax.set_title(f"{col} distribution", fontweight="bold", fontsize=11); fig.tight_layout()
    return fig


def rate_plot(df, col):
    order = _order(df, col)
    g = df.assign(_c=df[col].astype(str)).groupby("_c")[TARGET_NUM].agg(["mean", "count"]).reindex(order)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    sns.barplot(x=g.index, y=g["mean"].values, hue=g.index, palette="viridis", legend=False, ax=ax)
    for i, (m, n) in enumerate(zip(g["mean"], g["count"])):
        ax.text(i, m, f"{100 * m:.1f}%", ha="center", va="bottom", fontsize=8)
    ax.set_xticks(range(len(g))); ax.set_xticklabels([f"{i}\n(n={int(n)})" for i, n in zip(g.index, g["count"])], fontsize=8)
    ax.axhline(df[TARGET_NUM].mean(), ls="--", color="grey", lw=1, label="Overall rate")
    ax.set_ylim(0, min(1, max(g["mean"].max() * 1.25, 0.1))); ax.set_ylabel("At-risk rate"); ax.legend(fontsize=8)
    ax.set_title(f"At-risk rate by {col}", fontweight="bold", fontsize=11); _rot(ax, order)
    fig.tight_layout()
    return fig


def failure_plot(summary):
    s = summary.sort_values("Failure rate (%)")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh(s["Subject"], s["Failure rate (%)"], color="#c0392b")
    for y, v in enumerate(s["Failure rate (%)"]):
        ax.text(v, y, f" {v:.1f}%", va="center", fontsize=8)
    ax.set_xlabel("Failure rate (%)"); ax.set_title("Failure rate by subject", fontweight="bold", fontsize=11)
    ax.margins(x=0.15); fig.tight_layout()
    return fig


def marks_box(df, subjects):
    fig, ax = plt.subplots(figsize=(7, 4.2))
    sns.boxplot(data=df[subjects], orient="h", color="#8fa3b3", ax=ax)
    ax.axvline(50, color="#c0392b", ls="--", lw=1)
    ax.set_xlabel("Mark (%)"); ax.set_title("Mark distribution by subject (red line = pass mark)", fontsize=11, fontweight="bold")
    fig.tight_layout()
    return fig


def confusion_plot(cm, title):
    fig, ax = plt.subplots(figsize=(3.6, 3.2))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax,
                xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
    ax.set_xlabel("Predicted at risk"); ax.set_ylabel("Actual at risk"); ax.set_title(title, fontsize=10, fontweight="bold")
    fig.tight_layout()
    return fig


def roc_plot(y, probas, title):
    fig, ax = plt.subplots(figsize=(4.6, 4))
    for name, p in probas.items():
        fpr, tpr, _ = roc_curve(y, p)
        ax.plot(fpr, tpr, label=name)
    ax.plot([0, 1], [0, 1], "k--", lw=1, label="Chance")
    ax.set_xlabel("False positive rate"); ax.set_ylabel("True positive rate"); ax.legend(fontsize=8)
    ax.set_title(title, fontsize=10, fontweight="bold"); fig.tight_layout()
    return fig


def hbar(labels, values, title, xlabel, ref=None):
    fig, ax = plt.subplots(figsize=(6.5, 0.32 * len(labels) + 1.2))
    ax.barh(list(labels)[::-1], list(values)[::-1], color="#3b6a8a")
    if ref is not None:
        ax.axvline(ref, color="#c0392b", ls="--", lw=1)
    ax.set_xlabel(xlabel); ax.set_title(title, fontsize=10, fontweight="bold"); fig.tight_layout()
    return fig
