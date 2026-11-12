"""Shared repository paths and fixtures for the benchmark tests."""

import json
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


@pytest.fixture(scope="session")


def benchmark_summary():
    return json.loads((RESULTS / "benchmark_summary.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")


def stage2_result():
    return json.loads((RESULTS / "stage2_selection.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="session")


def stage3_result():
    return json.loads((RESULTS / "stage3_simulation.json").read_text(encoding="utf-8"))
