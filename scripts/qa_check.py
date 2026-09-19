#!/usr/bin/env python3
"""Final QA check for EXP-0007 repository."""
import os
import sys
import json
import re

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

REQUIRED_FILES = [
    "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md", "SECURITY.md", "METHODS.md", "RESULTS.md",
    "CITATION.cff", "requirements.txt", "pyproject.toml",
    ".gitignore", "metadata.json", "configs/config.json",
    "docs/experiment-overview.md", "docs/r14-validation.md",
    "docs/bug-history.md", "docs/mathematical-background.md",
    "docs/detector-analysis.md", "docs/propagation-implementation.md",
    "docs/research-timeline.md", "docs/limitations.md", "docs/faq.md",
    "docs/zenodo-release.md", "REPRODUCIBILITY.md",
    ".github/workflows/test.yml", ".github/workflows/reproducibility.yml",
    ".github/workflows/lint.yml",
    "scripts/run_r14.py", "scripts/validate_environment.py",
    "scripts/reproduce_figures.py", "scripts/generate_report.py",
    "tests/test_field_construction.py", "tests/test_propagation.py",
    "tests/test_winding.py", "tests/test_detector.py",
    "tests/test_reproducibility.py", "tests/test_regression.py",
]

REQUIRED_DIRS = [
    "docs", "src", "tests", "data/raw", "data/processed",
    "data/validation", "results/r14", "results/figures",
    "results/tables", "results/summaries", "scripts", "configs",
    ".github/workflows", ".github/ISSUE_TEMPLATE",
    "archive/superseded", "archive/bugs", "archive/historical-results",
    "experiments/r01", "experiments/r14",
]

def check_files():
    missing = []
    for f in REQUIRED_FILES:
        path = os.path.join(REPO, f)
        if not os.path.exists(path):
            missing.append(f)
    return missing

def check_dirs():
    missing = []
    for d in REQUIRED_DIRS:
        path = os.path.join(REPO, d)
        if not os.path.isdir(path):
            missing.append(d)
    return missing

def check_json_validity():
    errors = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', '.venv'}]
        for f in files:
            if f.endswith('.json'):
                path = os.path.join(root, f)
                try:
                    with open(path) as fh:
                        json.load(fh)
                except json.JSONDecodeError as e:
                    errors.append(f"{path}: {e}")
    return errors

def main():
    print("EXP-0007 FINAL QA CHECK")
    print("=" * 50)
    
    all_pass = True
    
    print("\n[1] Checking required files...")
    missing_files = check_files()
    if missing_files:
        print(f"  MISSING: {missing_files}")
        all_pass = False
    else:
        print("  PASS — All required files exist")
    
    print("\n[2] Checking required directories...")
    missing_dirs = check_dirs()
    if missing_dirs:
        print(f"  MISSING: {missing_dirs}")
        all_pass = False
    else:
        print("  PASS — All required directories exist")
    
    print("\n[3] Checking JSON validity...")
    json_errors = check_json_validity()
    if json_errors:
        print(f"  ERRORS: {json_errors}")
        all_pass = False
    else:
        print("  PASS — All JSON files valid")
    
    print("\n[4] Checking for hardcoded paths...")
    import re
    path_issues = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__'}]
        for f in files:
            if f.endswith(('.py', '.md', '.json', '.yml', '.yaml', '.txt', '.sh')):
                path = os.path.join(root, f)
                try:
                    with open(path, errors='ignore') as fh:
                        content = fh.read()
                    if re.search(r'C:\\Users\\natha|/Users/natha|C:\\\\Users\\\\natha', content):
                        path_issues.append(path)
                except Exception:
                    pass
    if path_issues:
        print(f"  WARN: {path_issues}")
    else:
        print("  PASS — No hardcoded local paths")
    
    print("\n[5] Checking for secrets...")
    secret_issues = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__'}]
        for f in files:
            path = os.path.join(root, f)
            try:
                with open(path, errors='ignore') as fh:
                    content = fh.read()
                if re.search(r'(api[_-]?key|apikey|secret|password|token|credential)', content, re.I):
                    if 'placeholder' not in content.lower() and 'example' not in content.lower():
                        secret_issues.append(path)
            except Exception:
                pass
    if secret_issues:
        print(f"  WARN: Possible secrets in {secret_issues}")
    else:
        print("  PASS — No apparent secrets")
    
    print("\n" + "=" * 50)
    if all_pass and not path_issues and not secret_issues:
        print("QA RESULT: PASS")
    elif all_pass:
        print("QA RESULT: PASS (with warnings)")
    else:
        print("QA RESULT: FAIL")
    print("=" * 50)
    
    return 0 if all_pass else 1

if __name__ == "__main__":
    sys.exit(main())
