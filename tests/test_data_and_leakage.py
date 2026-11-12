"""Workbook integrity and fold-local preprocessing checks."""

import inspect

import numpy as np

from certiq_chirp.data import load_data
from certiq_chirp.stage1_hybrid import fit_transform_fold, run_stage1_cv


def test_workbook_sheets_have_expected_shapes_and_labels():
    train, test, stage2, X, y, X_test = load_data()

    assert train.shape == (300, 17)
    assert test.shape == (100, 16)
    assert len(stage2) == 400
    assert X.shape == (300, 15)
    assert X_test.shape == (100, 15)
    assert int(y.sum()) == 35
    assert "y" not in test.columns
    assert train["customer_id"].is_unique
    assert test["customer_id"].is_unique
    assert not train.isna().any().any()
    assert not test.isna().any().any()
    assert not stage2.isna().any().any()


def test_fold_preprocessor_fits_only_on_training_rows():
    _, _, _, X, _, _ = load_data()
    train_indices = np.arange(24)
    validation_indices = np.array([24, 25])
    numeric = ["age", "balance", "day", "campaign", "pdays", "previous"]

    # A deliberately extreme held-out value must not alter training statistics.
    X_with_outlier = X.copy()
    X_with_outlier.iloc[validation_indices[0], X.columns.get_loc("balance")] = 1_000_000_000
    X_train, X_validation, preprocessor = fit_transform_fold(
        X_with_outlier, train_indices, validation_indices
    )

    scaler = preprocessor.named_transformers_["num"]
    expected_training_mean = X_with_outlier.iloc[train_indices][numeric].mean().to_numpy()
    np.testing.assert_allclose(scaler.mean_, expected_training_mean)
    assert X_train.shape[0] == len(train_indices)
    assert X_validation.shape[0] == len(validation_indices)
    assert scaler.mean_[numeric.index("balance")] != X_with_outlier["balance"].mean()
    assert "fit_transform_fold(X, tr, va)" in inspect.getsource(run_stage1_cv)
