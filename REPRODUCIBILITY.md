# Reproducing and inspecting EXP-0007

## Scope

The archived R14 records are historical evidence, not results computed during installation or CI. This checkout does not contain the original app.optics implementation. Its full simulation tests need that external sandbox. No fresh physical finding is claimed here.

## Install the analysis environment

Use Python 3.12 or later. From this repository:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install pytest
python scripts/validate_environment.py
```

## Checks available in this checkout

```bash
python -m pytest tests/test_reproducibility.py tests/test_validation_entrypoints.py -q
```

These check environment availability, record structure and command failure behavior. They do not establish optical reproduction. Other tests import the external app.optics code; run them only after configuring that prerequisite.

## Full historical runner

Obtain the original coherent-optical-ai-sandbox source independently and record its exact commit. This repository does not supply or pin it. Set EXP0007_PROJECT to its root (the directory containing app/optics), then run:

```powershell
$env:EXP0007_PROJECT = 'C:\path\to\coherent-optical-ai-sandbox'
python scripts/run_r14.py --output r14-reproduction.json
```

On Linux/macOS:

```bash
export EXP0007_PROJECT=/path/to/coherent-optical-ai-sandbox
python scripts/run_r14.py --output r14-reproduction.json
```

The output path is resolved before the runner changes directory. Existing files are refused, preserving archived outputs. Use a fresh filename for each run. Record both source commits, dependency versions and the complete console output alongside it.

The runner computes detector counts and repeated runs, but also prints historical sign-convention commentary. Its NCC string and dead-threshold flag are not independently measured by that runner. Its count assertions do not establish physical vortex creation. Evaluate these limitations before interpreting the output.

## Retired lightweight command

scripts/run_r14_lightweight.py previously printed fixed counts and wrote reproducible=true without running the optical model. It now exits 2 and writes nothing. The old output is retained in the historical record; it is not independent verification. The full runner rejects unsupported --lightweight and --phase options instead of silently ignoring them.

## Preserved evidence

Read research_continuation/, results/r14/, METHODS.md, RESULTS.md and docs/limitations.md together. Do not overwrite them with a fresh run. The original apparent vortex-creation interpretation remains unvalidated.
