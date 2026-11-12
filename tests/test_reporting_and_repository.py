"""Narrative/JSON parity, report generation, and CLI smoke tests."""

import json
import os
import subprocess
import sys
import tomllib
from pathlib import Path

import pandas as pd

import certiq_chirp
from certiq_chirp.config import SEEDS
from certiq_chirp.reporting import engineering_gate_results, generate_report

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def test_thirty_engineering_gates_pass(benchmark_summary):
    gates = engineering_gate_results(benchmark_summary)
    metrics = pd.read_csv(RESULTS / "benchmark_metrics.csv")

    assert len(gates) == 30
    assert all(gates)
    assert len(metrics) == 30


def test_readme_headlines_match_canonical_json(benchmark_summary, stage2_result, stage3_result):
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    winner = benchmark_summary["stage1_oof_metrics"][benchmark_summary["winner_model"]]

    assert benchmark_summary["winner_model"] == "rank_calibrated_hybrid"
    assert f"{winner['roc_auc']:.7f}" in readme
    assert f"{winner['pr_auc']:.7f}" in readme
    assert f"{winner['brier']:.7f}" in readme
    assert f"{winner['log_loss']:.7f}" in readme
    assert f"{winner['ece']:.7f}" in readme
    assert ", ".join(stage2_result["selected_6_customer_ids"]) in readme
    assert f"{stage2_result['objective_value']:.6f}" in readme
    assert f"{stage3_result['exact_analytical_probability']}" in readme
    assert f"{stage3_result['noiseless_finite_shot_probability']}" in readme
    assert "30/30 passed" in (RESULTS / "benchmark_report.md").read_text(encoding="utf-8")


def test_report_generator_keeps_the_technical_report_in_sync():
    report_path = generate_report()
    report = report_path.read_bytes()
    technical_report = (ROOT / "docs/04_TECHNICAL_REPORT.md").read_bytes()
    benchmark_readme = (ROOT / "docs/BENCHMARK_README.md").read_text(encoding="utf-8")

    assert report == technical_report
    assert "src/certiq_chirp/" in report.decode("utf-8")
    assert "requirements-dev.txt" in benchmark_readme
    assert "/home/user/" not in benchmark_readme


def test_compatibility_and_module_clis_support_help():
    commands = [
        [sys.executable, "src/run_benchmark.py", "--help"],
        [sys.executable, "src/make_report.py", "--help"],
        [sys.executable, "-m", "certiq_chirp", "--help"],
    ]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    for command in commands:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
            timeout=45,
        )
        assert completed.returncode == 0, completed.stderr
        assert "usage:" in completed.stdout.lower()


def test_package_sets_omp_default_before_numerical_imports():
    env = os.environ.copy()
    env.pop("OMP_NUM_THREADS", None)
    env["PYTHONPATH"] = str(ROOT / "src")
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            "import os, certiq_chirp; assert os.environ['OMP_NUM_THREADS'] == '1'",
        ],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    assert completed.returncode == 0, completed.stderr


def test_project_files_cover_dependencies_seeds_and_build_caches():
    requirements_path = ROOT / "requirements.txt"
    requirements = requirements_path.read_text(encoding="utf-8")
    dev_requirements = (ROOT / "requirements-dev.txt").read_text(encoding="utf-8")
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    pinned_dependencies = [line for line in requirements.splitlines() if line.strip()]
    tracked_seeds = json.loads((ROOT / "seeds.json").read_text(encoding="utf-8"))

    assert "openpyxl==3.1.5" in requirements
    assert project["requires-python"] == ">=3.12"
    assert project["version"] == certiq_chirp.__version__
    assert project["dependencies"] == pinned_dependencies
    assert tracked_seeds == SEEDS
    assert "-r requirements.txt" in dev_requirements
    assert "pytest==9.0.3" in dev_requirements
    for ignored in (".pytest_cache/", "*.egg-info/", "build/", "dist/"):
        assert ignored in gitignore
