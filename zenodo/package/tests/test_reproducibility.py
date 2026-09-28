import numpy as np
import pytest
import sys, os
"""Test reproducibility and environment validation."""

PROJECT = os.environ.get("EXP0007_PROJECT", r"C:\Users\natha\code\coherent-optical-ai-sandbox")
sys.path.insert(0, PROJECT)
sys.path.insert(0, os.path.join(PROJECT, "app"))


class TestEnvironment:
    def test_python_version(self):
        import platform
        version = platform.python_version()
        major = int(version.split('.')[0])
        assert major >= 3, f"Python 3+ required, got {version}"

    def test_numpy_available(self):
        import numpy
        assert numpy.__version__ >= "1.24", f"NumPy >= 1.24 required, got {numpy.__version__}"

    def test_scipy_available(self):
        import scipy
        assert scipy.__version__ >= "1.11", f"SciPy >= 1.11 required, got {scipy.__version__}"

    def test_determinism_numpy_seed(self):
        """Same seed should give same results."""
        np.random.seed(42)
        r1 = np.random.rand(100)
        np.random.seed(42)
        r2 = np.random.rand(100)
        assert np.allclose(r1, r2), "NumPy seeding not deterministic"


class TestDataSchema:
    def test_r14_summary_structure(self):
        import json
        path = os.path.join(os.path.dirname(__file__), "..", "research_continuation", "r14_summary.json")
        with open(path) as f:
            data = json.load(f)
        assert "R14" in data
        assert "verdict" in data["R14"]
        assert "phases" in data["R14"]

    def test_FINAL_MANIFEST_structure(self):
        import json
        path = os.path.join(os.path.dirname(__file__), "..", "research_continuation", "FINAL_MANIFEST.json")
        with open(path) as f:
            data = json.load(f)
        assert "project" in data
        assert "key_findings" in data
        assert "status" in data

    def test_all_required_docs_exist(self):
        import os
        docs = [
            "README.md", "LICENSE", "METHODS.md", "RESULTS.md", "CHANGELOG.md",
            "REPRODUCIBILITY.md", "docs/experiment-overview.md", "docs/r14-validation.md",
            "docs/bug-history.md", "docs/mathematical-background.md",
            "docs/detector-analysis.md", "docs/propagation-implementation.md",
            "docs/research-timeline.md", "docs/limitations.md", "docs/faq.md",
        ]
        for doc in docs:
            path = os.path.join(os.path.dirname(__file__), "..", doc)
            assert os.path.exists(path), f"Missing: {doc}"


class TestReproducibilityCommands:
    def test_validate_environment_script_exists(self):
        import os
        path = os.path.join(os.path.dirname(__file__), "..", "scripts", "validate_environment.py")
        assert os.path.exists(path), "validate_environment.py missing"

    def test_run_r14_script_exists(self):
        import os
        path = os.path.join(os.path.dirname(__file__), "..", "scripts", "run_r14.py")
        assert os.path.exists(path), "run_r14.py missing"
