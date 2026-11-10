"""A historical summary must not report a successful reproduction."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_lightweight_fails_closed_without_writing_results():
    results = ROOT / "results" / "r14"
    before = {p.name: p.read_bytes() for p in results.glob("*") if p.is_file()}
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_r14_lightweight.py")],
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == 2
    assert "NOT RUN" in result.stderr
    assert before == {p.name: p.read_bytes() for p in results.glob("*") if p.is_file()}


def test_runner_reports_missing_external_project(tmp_path):
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_r14.py")],
        env=dict(os.environ, EXP0007_PROJECT=str(tmp_path / "absent")),
        cwd=tmp_path, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 2
    assert "EXP0007_PROJECT" in result.stderr
    assert "Traceback" not in result.stderr


def test_runner_rejects_unsupported_flags():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_r14.py"), "--lightweight"],
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == 2
    assert "unrecognized arguments" in result.stderr


def test_runner_refuses_existing_output(tmp_path):
    output = tmp_path / "historical.json"
    output.write_text("preserve me")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_r14.py"), "--output", str(output)],
        capture_output=True, text=True, check=False,
    )
    assert result.returncode == 2
    assert "already exists" in result.stderr
    assert output.read_text() == "preserve me"
