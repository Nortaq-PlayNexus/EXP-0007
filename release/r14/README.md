# EXP-0007 R14 Release Package

## Summary

- **Experiment**: EXP-0007 DeepBeamEmergenceControl
- **Date**: 2026-09-19
- **Version**: v1.0.0-r14
- **Status**: R14 validation complete

## Key Results

| Measurement | Value |
|-------------|-------|
| DBS at z=0 | 48 |
| DBS at z=+1280 | 113 |
| Independent verification | 113 = 113 (verified) |
| 98.4% undercount claim | **INVALID** (bug-based) |
| Conclusion | Detector + grid-locking artifact |

## Contents

| File | Description |
|------|-------------|
| DEFINITIVE_DBS_TEST.json | Independent verification results |
| z_sweep.json | Z-sweep results (15 distances) |
| threshold_sweep.json | Threshold sensitivity (7 thresholds) |
| resolution_convergence.json | Resolution dependence |
| detector_validation.json | Detector validation (7 controls) |
| null_distribution.json | Null distribution (100 random fields) |
| r14_summary.json | R14 phase results (24 phases) |
| README.md | Package documentation |

## Reproduction

```powershell
python scripts/run_r14.py
```

## Limitations

- 65 propagation-generated features uncharacterized
- R11/R12 need re-run with corrected MethodB
- No physical experimental validation
