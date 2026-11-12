"""Leakage-safe hybrid Stage 1 model selection and quantum-kernel utilities."""

import time

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.svm import SVC
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from qiskit import transpile
from qiskit.circuit.library import zz_feature_map
from qiskit.quantum_info import Statevector

from .config import FOLDS, N_QK, P_QK, REPEATS, SEEDS
from .metrics import clip, metric_bundle


def build_preprocessor():
    numeric = ["age", "balance", "day", "campaign", "pdays", "previous"]
    categorical = [c for c in ["job", "marital", "education", "default", "housing", "loan", "contact", "month", "poutcome"]]
    return ColumnTransformer([
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical),
    ], sparse_threshold=0.0)


def fit_transform_fold(X, train_indices, validation_indices):
    """Fit preprocessing on a training fold only, then transform its held-out fold."""
    pre = build_preprocessor()
    Xtr = pre.fit_transform(X.iloc[train_indices])
    Xva = pre.transform(X.iloc[validation_indices])
    return Xtr, Xva, pre


def classical_models(seed, y_train=None):
    if y_train is None:
        spw = 1.0
    else:
        y_train = np.asarray(y_train)
        spw = float((len(y_train) - y_train.sum()) / max(1, y_train.sum()))
    return {
        "logistic": LogisticRegression(C=0.5, class_weight="balanced", max_iter=3000, random_state=seed),
        "hist_gb": HistGradientBoostingClassifier(max_iter=160, learning_rate=0.06, max_leaf_nodes=15,
                                                  min_samples_leaf=10, l2_regularization=1.0,
                                                  class_weight="balanced", random_state=seed),
        "lightgbm": LGBMClassifier(n_estimators=220, learning_rate=0.045, num_leaves=15, max_depth=4,
                                   min_child_samples=12, subsample=0.9, colsample_bytree=0.9,
                                   class_weight="balanced", random_state=seed, verbosity=-1, n_jobs=1),
        "catboost": CatBoostClassifier(iterations=260, depth=4, learning_rate=0.05, l2_leaf_reg=3.0,
                                       loss_function="Logloss", auto_class_weights="Balanced",
                                       random_seed=seed, verbose=False, allow_writing_files=False,
                                       thread_count=1),
        "xgb": XGBClassifier(n_estimators=250, max_depth=3, learning_rate=0.04, subsample=0.9,
                             colsample_bytree=0.9, scale_pos_weight=spw, eval_metric="logloss",
                             random_state=seed, n_jobs=1),
    }


def quantum_states(angles):
    fm = zz_feature_map(feature_dimension=N_QK, reps=P_QK, entanglement="full")
    states = []
    for row in np.asarray(angles):
        qc = fm.assign_parameters(row)
        states.append(Statevector.from_instruction(qc).data)
    return np.asarray(states, dtype=complex)


def quantum_kernel(A, B):
    return np.abs(A @ B.conj().T) ** 2


def quantum_preprocess(Xtr, Xval, seed):
    pca = PCA(n_components=N_QK, random_state=seed, svd_solver="full")
    mm = MinMaxScaler(feature_range=(0.0, np.pi))
    Atr = mm.fit_transform(pca.fit_transform(Xtr))
    Aval = mm.transform(pca.transform(Xval))
    return Atr, Aval


def run_stage1_cv(X, y):
    n = len(y)
    model_names = ["logistic", "hist_gb", "lightgbm", "catboost", "xgb", "quantum_kernel_svc"]
    oof = {m: np.zeros((REPEATS, n)) for m in model_names}
    times = {m: [] for m in model_names}
    qk_specs = None
    for r, seed in enumerate(SEEDS["cv_repeats"]):
        skf = StratifiedKFold(n_splits=FOLDS, shuffle=True, random_state=seed)
        for fold, (tr, va) in enumerate(skf.split(X, y)):
            t0 = time.perf_counter()
            Xtr, Xva, pre = fit_transform_fold(X, tr, va)
            models = classical_models(seed + fold, y[tr])
            for name, est in models.items():
                t = time.perf_counter()
                est.fit(Xtr, y[tr])
                oof[name][r, va] = clip(est.predict_proba(Xva)[:, 1])
                times[name].append(time.perf_counter() - t)
            # Quantum kernel SVC, fitted and calibrated within the training fold only.
            t = time.perf_counter()
            Atr, Ava = quantum_preprocess(Xtr, Xva, seed + fold)
            psitr = quantum_states(Atr)
            psiva = quantum_states(Ava)
            Ktr = quantum_kernel(psitr, psitr)
            Kva = quantum_kernel(psiva, psitr)
            qsvc = SVC(kernel="precomputed", C=1.0, class_weight="balanced",
                       probability=True, random_state=seed + fold)
            qsvc.fit(Ktr, y[tr])
            oof["quantum_kernel_svc"][r, va] = clip(qsvc.predict_proba(Kva)[:, 1])
            times["quantum_kernel_svc"].append(time.perf_counter() - t)
            if qk_specs is None:
                fm = zz_feature_map(feature_dimension=N_QK, reps=P_QK, entanglement="full")
                tfm = transpile(fm, basis_gates=["u", "cx"], optimization_level=1)
                qk_specs = {
                    "logical_qubits": N_QK,
                    "reps": P_QK,
                    "logical_depth": fm.depth(),
                    "transpiled_depth": tfm.depth(),
                    "transpiled_ops": {k: int(v) for k, v in tfm.count_ops().items()},
                    "statevector_dimension": 2 ** N_QK,
                }
            print(f"CV repeat {r+1}/{REPEATS}, fold {fold+1}/{FOLDS}: {time.perf_counter()-t0:.1f}s")
    pooled = {m: clip(oof[m].mean(axis=0)) for m in model_names}
    repeat_metrics = {}
    for m in model_names:
        repeat_metrics[m] = [metric_bundle(y, oof[m][r]) for r in range(REPEATS)]
    return oof, pooled, repeat_metrics, times, qk_specs, model_names
