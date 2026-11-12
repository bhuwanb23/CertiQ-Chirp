"""Project paths and fixed experiment configuration."""

import os
from pathlib import Path

# Preserve the benchmark's original thread-limit policy before numerical imports.
os.environ.setdefault("OMP_NUM_THREADS", "1")

_PACKAGE_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _resolve_project_root() -> Path:
    """Find the checkout root for source, editable, and console-script runs."""
    expected_data = Path("data/raw/bank_campaign_participant_release.xlsx")
    for candidate in (_PACKAGE_PROJECT_ROOT, Path.cwd().resolve()):
        if (candidate / expected_data).is_file():
            return candidate
    return _PACKAGE_PROJECT_ROOT

ROOT = _resolve_project_root()
OUT = ROOT / "results"
WORKBOOK = ROOT / "data" / "raw" / "bank_campaign_participant_release.xlsx"
SEEDS = {"sampling": 42, "split": 42, "cv_repeats": [42, 142, 242], "meta_cv": 999,
         "qaoa": 2026, "simulator": 31415, "monte_carlo": 27182, "bootstrap": 1618}
SHOTS = 32768
N_QK = 4
P_QK = 1
REPEATS = 3
FOLDS = 5
