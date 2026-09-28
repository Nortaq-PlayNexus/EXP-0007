# Research Timeline — EXP-0007

## Timeline Structure

All dates are from repository metadata where available. Where dates are not independently verified, they are marked as [derived].

## Phase 0: Discovery & Corpus Mapping (2026-09-19)

- Recursive inventory of ~683 files
- Hash verification (191 files)
- Experiment indexing (EXP-0001 through EXP-0025)
- Evidence manifest creation
- Dependency graph construction

## Phase 1: Parallel Analysis (2026-09-19)

- 12 agents (A-L) produced independent reports
- 4 agents ran Python analyses (B: statistics, E: seeds, F: adversarial, G: replication)
- Cross-check: disagreement detection, cross-pollination, adversarial second pass

## Phase 2: R1–R4 Initial Experiments (2026-09-19)

| Experiment | Verdict |
|------------|---------|
| R1: Phase rotation invariance | INVARIANT |
| R2: Aperture scaling | MONOTONIC DECREASE |
| R3: Random/lattice ratio | ~1000× |
| R4: Grid convergence | DECREASING |

## Phase 3: R5–R7 Project-Exact Tests (2026-09-19)

| Experiment | Verdict |
|------------|---------|
| R5: Project-exact phase rotation | VARIANT |
| R6: Grid-converged detector | Dead parameter confirmed |
| R7: D02 null | LATTICE 191× FEWER (DECISIVE) |

## Phase 4: R8–R10 Quantitative Tests (2026-09-19)

| Experiment | Verdict |
|------------|---------|
| R8: Lattice/D02 ratio | DETECTOR-DRIVEN |
| R9: Orientation dependence | ORIENTATION DEPENDENT (corrected 6.3×) |
| R10: Wavelength sweep | WAVELENGTH-INDEPENDENT |

## Phase 5: R11–R12 Fix Verification (2026-09-19)

| Experiment | Verdict |
|------------|---------|
| R11: DBS fix verification | DBS=113 correct; custom function buggy |
| R12: EXP-3 input permutation | GRID-LOCKING CONFIRMED |

## Phase 5.5: R13 Definitive Test (2026-09-19)

- **INVALIDATED**: Original R13 used buggy MethodB (7,183 from double-np.angle bug)
- **CORRECTED**: Fixed MethodB = MethodA = 113 (no discrepancy)
- 98.4% undercount claim is FALSE

## Phase 6: R14 Validation (2026-09-19)

- 24 phases executed
- Comprehensive validation of 113-vortex claim
- **VERDICT**: Detector + grid-locking artifact, NOT physical vortex creation

## Bug Discoveries

| Date | Bug | Severity | Impact |
|------|-----|----------|--------|
| 2026-09-19 | Double-np.angle in winding_count | CRITICAL | Invalidated all R13 MethodB counts |
| 2026-09-19 | min_prominence dead parameter | HIGH | DBS overcounts noise |
| 2026-09-19 | propagate_fresnel sign bug | HIGH | Wrong propagation direction |
| 2026-09-19 | Circular wrap-around | MEDIUM | Boundary artifacts |
| 2026-09-19 | Independent ASM normalization | MEDIUM | Unreliable cross-check |
| 2026-09-19 | Radial spectrum ring-blend | MEDIUM | Misleading spectral analysis |
| 2026-09-19 | Seed label swap | MEDIUM | Data management issue |
| 2026-09-19 | lattice_params constant guard | LOW | Functionally equivalent |

## Corrections Timeline

1. **CRITICAL**: 7,183 → 113 (double-np.angle bug fixed)
2. **MAJOR**: 98.4% undercount → No discrepancy (98.4% was comparing valid vs buggy MethodB)
3. **MAJOR**: 2.0× orientation → 6.3× orientation (MethodB corrected)
4. **MAJOR**: 8× lattice/D02 → 191× (MethodA corrected)
5. **MINOR**: R11/R12 counts re-evaluated (inflated by MethodB)
