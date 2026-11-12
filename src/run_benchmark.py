#!/usr/bin/env python3
"""Compatibility entry point for ``python src/run_benchmark.py``."""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")

from certiq_chirp.pipeline import main

if __name__ == "__main__":
    main()
