# EXP-0007 — Research Data Index

## Primary Results

| File | Content | Location |
|------|---------|----------|
| DBS at z=0 | 48 features | results/r14/DEFINITIVE_DBS_TEST.json |
| DBS at z=+1280 | 113 features | results/r14/DEFINITIVE_DBS_TEST.json |
| Z-sweep | 15 distances, 7 discontinuities | results/r14/z_sweep.json |
| Threshold sweep | 0→102 across thresholds | results/r14/threshold_sweep.json |
| Resolution convergence | 328→5,742 (no convergence) | results/r14/resolution_convergence.json |
| Detector validation | 7 controls, overcounts 9-19× | results/r14/detector_validation.json |
| Null distribution | 21,670 random, 113 at 0th % | results/r14/null_distribution.json |
| R14 phase results | 24 phases documented | results/r14/phase_results.json |

## Preserved Original Data

All original research data from EXP-0007-SWARM-AUDIT preserved in `research_continuation/`:

| File | Content |
|------|---------|
| FINAL_MANIFEST.json | Master file manifest (46 files, 12 agents) |
| r14_summary.json | R14 summary (24 phases, verdict) |
| CONTINUATION_FINAL.json | Consolidated R1-R12 results |
| R_CONTINUATION_REPORT.md | Phase 2-3 report |
| R_CONTINUATION_V2.md | Phase 4 report |
| MASTER_FINAL_REPORT.md | Master final report |
| r1_phase_rotation.json | R1 results (INVARIANT) |
| r2_aperture_scaling.json | R2 results (MONOTONIC DECREASE) |
| r3_random_mechanism.json | R3 results (~1000× ratio) |
| r4_grid_convergence.json | R4 results (DECREASING) |
| r5_phase_rotation_project.json | R5 results (VARIANT) |
| r6_grid_converged.json | R6 results (dead parameter) |
| r7_d02_null.json | R7 results (LATTICE 191× FEWER) |
| r8_lattice_d02_ratio.json | R8 results (DETECTOR-DRIVEN) |
| r9_orientation.json | R9 results (ORIENTATION DEPENDENT, corrected) |
| r11_dbs_fix.json | R11 results (DBS=113 correct) |
| r12_exp3_null.json | R12 results (GRID-LOCKING CONFIRMED) |
| r13_forensic_results.csv | R13 forensic (Phases 1-4) |
| CRITICAL_BUG_REPORT.md | Double-np.angle bug (CRITICAL) |
| FINAL_CORRECTED_REPORT.md | All R13 results corrected |
| R14_EXHAUSTIVE_VORTEX_VALIDATION.md | R14 master report |

## Data Provenance

```
RAW: research_continuation/ (preserved)
  → r14_summary.json, CONTINUATION_FINAL.json, FINAL_MANIFEST.json
  → R1-R12 individual JSONs
  → CRITICAL_BUG_REPORT.md, FINAL_CORRECTED_REPORT.md

DERIVED: results/r14/ (documented)
  → DEFINITIVE_DBS_TEST.json, z_sweep.json, etc.

SUMMARY: docs/ (documented)
  → README.md, METHODS.md, RESULTS.md, etc.
```
