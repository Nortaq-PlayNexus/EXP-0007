# CHANGELOG — EXP-0007

## v1.1.0 (2026-09-19) — R14 Reproduction & D1 Bug Verification

### New Tests

- R14 reproduction script (`scripts/run_r14.py`) — full 6-phase validation using project codebase
- Lightweight validation (`scripts/run_r14_lightweight.py`) — no project codebase needed
- D1 propagation sign bug confirmed via asymmetric feature counts
- NCC verification: project Fresnel(z=+1280 call) = independent ASM(z=-1280)
- QA check: PASS (with warnings)
- Numerical consistency: all key values tracked across 40+ files

### Key New Findings

- **D1 bug confirmed**: `propagate_fresnel(E0, z=-1280)` → physical z=+1280 → 113 features (R14 result)
- **D1 bug confirmed**: `propagate_fresnel(E0, z=+1280)` → physical z=-1280 → 47 features
- R14 result of 113 at z=+1280 is reproducible via `propagate_fresnel(E0, z=-1280)` (exploiting D1 sign flip)
- NCC(project Fresnel z=+1280 call, ASM z=-1280) = 1.000000 (confirms sign flip)
- All 91 files committed to git, pushed to GitHub

### Files Created

- `docs/d1-bug-effect.md` — Detailed analysis of propagation sign bug
- `scripts/run_r14.py` — Updated to 6-phase validation with D1 verification
- `scripts/run_r14_lightweight.py` — Lightweight validation (D1-aware)

### Files Modified

- `FINAL_OUTPUT.md` — Updated with new test results
- `README.md` — Updated with D1 bug notes
- `docs/propagation-implementation.md` — Added D1 effect table and verification

## v1.0.0 (2026-09-19) — Initial Repository Build

### Major Changes

- Complete repository audit of EXP-0007-SWARM-AUDIT workspace
- Created master README with scientific abstract, research pipeline, and validation summary
- Documented all 24 R14 validation phases with results
- Created bug history documentation (double-np.angle bug, min_prominence dead parameter, seed-label correction)
- Built test suite with regression tests for all discovered bugs
- Created CI/CD workflows (test, reproducibility, lint)
- Established data provenance framework
- Created release package at `release/r14/`

### Key Findings Documented

- DBS count of 113 at z=+1280 is independently verified (MethodA = fixed MethodB = 113)
- 7,183 "independent" winding count was caused by double-np.angle bug (NOT a measurement)
- 98.4% undercount claim is INVALID — caused by double-np.angle bug, not a real discrepancy
- 113-vortex result is a detector + grid-locking artifact, NOT physical vortex creation
- Orientation dependence confirmed at corrected scale (6.3× at 45°, not 2.0×)

### Files Created

- README.md, LICENSE, CITATION.cff, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- docs/ (10 documentation files)
- src/ (5 source directories)
- tests/ (test suite)
- scripts/ (5 automation scripts)
- configs/ (configuration files)
- data/ (raw, processed, validation, examples)
- results/ (R14 results, figures, tables, summaries)
- experiments/ (R01-R14 experiment directories)
- archive/ (superseded, bugs, historical-results)
- release/r14/ (release package)
- research_continuation/ (preserved raw research data)

### Bug Fixes Documented

- **CRITICAL**: Double-np.angle in winding_count (invalidate all R13-based MethodB counts)
- **HIGH**: find_features dead min_prominence parameter
- **MEDIUM**: propagate_fresnel sign bug
- **MEDIUM**: Circular wrap-around in propagation
- **MEDIUM**: Independent ASM normalization mismatch
- **MEDIUM**: Radial power spectrum ring-blend bias
- **LOW**: lattice_params constant guard (functionally equivalent)

### Known Limitations

- 65 propagation-generated features uncharacterized (real vs artifact)
- R11/R12 results need re-run with corrected MethodB
- D02 measurements need method verification
- Wavelength sweep (R10) needs re-verification with corrected MethodB
