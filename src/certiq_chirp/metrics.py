"""Probability metrics and small, deterministic evaluation utilities."""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_auc_score, average_precision_score, brier_score_loss, log_loss,
    balanced_accuracy_score, matthews_corrcoef, f1_score, accuracy_score,
    roc_curve,
)
from sklearn.model_selection import StratifiedKFold


def native(x):
    if isinstance(x, (np.integer,)): return int(x)
    if isinstance(x, (np.floating,)): return float(x)
    if isinstance(x, (np.bool_,)): return bool(x)
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, dict): return {str(k): native(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [native(v) for v in x]
    return x


def clip(p):
    return np.clip(np.asarray(p, dtype=float), 1e-6, 1 - 1e-6)


def logit(p):
    p = clip(p)
    return np.log(p / (1 - p))


def ece_mce(y, p, bins=10):
    y = np.asarray(y); p = clip(p)
    edges = np.linspace(0, 1, bins + 1)
    ece = 0.0; mce = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (p >= lo) & (p < hi if hi < 1 else p <= hi)
        if m.any():
            err = abs(p[m].mean() - y[m].mean())
            ece += m.mean() * err
            mce = max(mce, err)
    return float(ece), float(mce)


def calibration_slope_intercept(y, p):
    X = logit(p).reshape(-1, 1)
    lr = LogisticRegression(C=1e6, max_iter=2000, solver="lbfgs")
    lr.fit(X, y)
    return float(lr.coef_[0, 0]), float(lr.intercept_[0])


def ndcg_at_k(y, p, k):
    y = np.asarray(y); p = np.asarray(p)
    order = np.argsort(-p)[:k]
    gains = y[order].astype(float)
    dcg = np.sum((2 ** gains - 1) / np.log2(np.arange(2, k + 2)))
    ideal = np.sort(y)[::-1][:k].astype(float)
    idcg = np.sum((2 ** ideal - 1) / np.log2(np.arange(2, k + 2)))
    return float(dcg / idcg) if idcg > 0 else 0.0


def metric_bundle(y, p):
    y = np.asarray(y, int); p = clip(p)
    prevalence = y.mean()
    k = max(1, int(round(0.10 * len(y))))
    order = np.argsort(-p, kind="stable")[:k]
    tp = int(y[order].sum())
    precision = tp / k
    recall = tp / max(1, int(y.sum()))
    f1_top = 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)
    fpr, tpr, _ = roc_curve(y, p)
    ece, mce = ece_mce(y, p)
    slope, intercept = calibration_slope_intercept(y, p)
    ll = log_loss(y, p, labels=[0, 1])
    brier = brier_score_loss(y, p)
    naive = np.full_like(p, prevalence)
    brier_naive = brier_score_loss(y, naive)
    logloss_naive = log_loss(y, naive, labels=[0, 1])
    yhat = (p >= 0.5).astype(int)
    return {
        "roc_auc": float(roc_auc_score(y, p)),
        "pr_auc": float(average_precision_score(y, p)),
        "brier": float(brier),
        "log_loss": float(ll),
        "ece": ece,
        "mce": mce,
        "calibration_slope": slope,
        "calibration_intercept": intercept,
        "precision_at_10pct": float(precision),
        "recall_at_10pct": float(recall),
        "f1_at_10pct": float(f1_top),
        "lift_at_10pct": float(precision / prevalence),
        "ndcg_at_10pct": ndcg_at_k(y, p, k),
        "ks": float(np.max(tpr - fpr)),
        "balanced_accuracy_0.5": float(balanced_accuracy_score(y, yhat)),
        "mcc_0.5": float(matthews_corrcoef(y, yhat)),
        "f1_0.5": float(f1_score(y, yhat, zero_division=0)),
        "accuracy_0.5": float(accuracy_score(y, yhat)),
        "brier_skill": float(1 - brier / brier_naive),
        "logloss_skill": float(1 - ll / logloss_naive),
        "prevalence": float(prevalence),
        "k_top": k,
    }


def bootstrap_ci_width(y, p, seed=1618, n_boot=300):
    rng = np.random.default_rng(seed)
    y = np.asarray(y, int); p = clip(p)
    vals = []
    n = len(y)
    for _ in range(n_boot):
        idx = rng.integers(0, n, n)
        if len(np.unique(y[idx])) < 2:
            continue
        vals.append(average_precision_score(y[idx], p[idx]))
    if len(vals) < 10:
        return float("nan"), [float("nan"), float("nan")]
    lo, hi = np.percentile(vals, [2.5, 97.5])
    return float(hi - lo), [float(lo), float(hi)]


def meta_cv_predictions(Xmeta, y, seeds=(999, 1009, 1019, 1029, 1039)):
    outs = []
    for seed in seeds:
        pred = np.zeros(len(y))
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        for tr, va in skf.split(Xmeta, y):
            lr = LogisticRegression(C=1.0, max_iter=2000, solver="lbfgs")
            lr.fit(Xmeta[tr], y[tr])
            pred[va] = lr.predict_proba(Xmeta[va])[:, 1]
        outs.append(clip(pred))
    return np.asarray(outs)
