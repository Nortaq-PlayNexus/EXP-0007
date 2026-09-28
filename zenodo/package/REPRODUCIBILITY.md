# REPRODUCIBILITY — EXP-0007

## How to Reproduce

### 1. Clone the Repository

```bash
git clone https://github.com/<username>/EXP-0007.git
cd EXP-0007
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

Or with conda:

```powershell
conda env create -f environment.yml
conda activate exp-0007
```

### 3. Validate Environment

```powershell
python scripts/validate_environment.py
```

This checks:
- Python version (≥3.10)
- NumPy version
- SciPy version
- Matplotlib version
- Required packages

### 4. Reproduce R14 (Full)

```powershell
python scripts/run_r14.py
```

This will:
1. Validate environment
2. Load configuration
3. Run R14 experiments
4. Generate derived data
5. Generate figures
6. Generate summary report

### 5. Reproduce R14 (Lightweight Validation)

```powershell
python scripts/run_r14.py --lightweight
```

Runs a subset of R14 phases for quick validation (~5 minutes).

### 6. Run Individual Phases

```powershell
# Run threshold sensitivity test
python scripts/run_r14.py --phase threshold

# Run resolution convergence test
python scripts/run_r14.py --phase resolution

# Run detector validation
python scripts/run_r14.py --phase detector

# Run null tests
python scripts/run_r14.py --phase null
```

### 7. Inspect Raw Data

```powershell
# View R14 summary
cat results/r14/summary.json

# View phase results
cat results/r14/phase_*.json

# View raw research data (preserved from original)
cat research_continuation/r14_summary.json
```

### 8. Reproduce Figures

```powershell
python scripts/reproduce_figures.py
```

### 9. Compare with Published Results

```powershell
python scripts/generate_report.py --compare
```

## Platform-Specific Instructions

### Windows

```powershell
# Ensure Python is in PATH
python --version
pip --version

# Install dependencies
pip install -r requirements.txt

# Run reproduction (full)
python scripts/run_r14.py

# Run reproduction (lightweight, ~5 minutes)
python scripts/run_r14_lightweight.py

# Validate environment
python scripts/validate_environment.py

# Run QA check
python scripts/qa_check.py

# Check numerical consistency
python scripts/numerical_consistency_check.py

# Generate figures
python scripts/reproduce_figures.py

# Generate report
python scripts/generate_report.py
```

### Linux/macOS

```bash
python3 --version
pip3 --version

pip install -r requirements.txt

# Run reproduction (full)
python3 scripts/run_r14.py

# Run reproduction (lightweight, ~5 minutes)
python3 scripts/run_r14_lightweight.py

# Validate environment
python3 scripts/validate_environment.py

# Run QA check
python3 scripts/qa_check.py

# Check numerical consistency
python3 scripts/numerical_consistency_check.py

# Set project path if needed
export EXP0007_PROJECT="/path/to/project"
```

## Reproduction Results (Verified)

| Command | Expected Output | Actual | Status |
|---------|----------------|--------|--------|
| `python scripts/validate_environment.py` | "ENVIRONMENT VALIDATED" | PASS | ✓ |
| `python scripts/run_r14.py` | z=0: 48, z=+1280: 113 | PASS | ✓ |
| `python scripts/run_r14_lightweight.py` | z=0: 48, z=+1280: 113 | PASS | ✓ |
| `python scripts/qa_check.py` | "QA RESULT: PASS" | PASS (warnings) | ✓ |
| `python scripts/numerical_consistency_check.py` | Key values found | 48(30), 113(34), etc. | ✓ |

## Requirements

- Python ≥3.10
- NumPy ≥1.24
- SciPy ≥1.11
- Matplotlib ≥3.7

See `requirements.txt` and `pyproject.toml` for exact versions.

## Configuration

Experiment parameters are centralized in `configs/`. Do not scatter magic numbers in scripts.

Key parameters:
- Wavelength: 694.3 nm
- Grid size: 256 × 256
- Pixel size: 1 µm
- Propagation distance: 1280 µm
- Random seed: 42
