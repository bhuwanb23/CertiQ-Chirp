"""Exact Stage 2 optimization and retained QAOA certificate checks."""

import json
from pathlib import Path

import pandas as pd
import pytest

from certiq_chirp.data import load_data
from certiq_chirp.stage2_qaoa import exact_stage2_selection
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def test_exhaustive_stage2_solution_matches_canonical_certificate(stage2_result, benchmark_summary):
    _, _, stage2_data, _, _, _ = load_data()
    stage1 = pd.read_csv(RESULTS / "stage1_predictions.csv")
    top10_ids = stage1.loc[stage1["is_top_10"], "customer_id"].tolist()
    top10, exact_combo, exact_ids, exact = exact_stage2_selection(
        stage2_data, stage1, top10_ids
    )

    assert len(top10) == 10
    assert len(exact_combo) == 6
    assert list(exact_ids) == stage2_result["selected_6_customer_ids"]
    assert list(exact_ids) == ["C0059", "C0170", "C0256", "C0327", "C0372", "C0374"]
    assert exact["feasible_subset_count"] == 210
    assert exact["objective_value"] == exact["classical_bruteforce_optimum"]
    assert exact["absolute_optimality_gap"] == 0.0
    assert exact["objective_value"] == pytest.approx(stage2_result["objective_value"], abs=1e-12)
    assert exact["top_10_candidate_ids"] == benchmark_summary["stage1_test"]["top_10_ids"]

    # The saved QAOA warm start and hybrid repair are tied back to that same exact answer.
    qaoa = stage2_result["qaoa"]
    exact_index = sum(
        1 << index
        for index, customer_id in enumerate(top10["customer_id"].tolist())
        if customer_id in set(exact_ids)
    )
    assert qaoa["exact_certificate_bitstring"] == format(exact_index, "010b")
    assert set(qaoa["hybrid_repaired_selected_ids"]) == set(exact_ids)
    assert qaoa["certified_hybrid_gap"] == 0.0
    assert qaoa["qaoa_gap_to_exact"] > 0.0


def test_stage_result_json_and_csv_companions_have_expected_schemas():
    stage2_csv = pd.read_csv(RESULTS / "stage2_selection.csv")
    stage3_csv = pd.read_csv(RESULTS / "stage3_simulation.csv")
    stage3_json = json.loads((RESULTS / "stage3_simulation.json").read_text(encoding="utf-8"))

    assert stage2_csv.shape == (1, 25)
    assert stage3_csv.shape == (1, 27)
    assert len(stage3_json["selected_customer_ids"]) == 6
    assert set(stage3_json["customer_to_qubit_mapping"].values()) == {
        "q0", "q1", "q2", "q3", "q4", "q5"
    }
