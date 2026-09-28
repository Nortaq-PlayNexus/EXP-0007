# R1–R13 History — EXP-0007

## R1: Phase Rotation Invariance

**Verdict**: INVARIANT (simplified lattice)
- Winding count = 89 at all phase shifts (0–180°)
- Used simplified 5×7 lattice (35 vortices), not project's exact 48
- Later superseded by R5 (project-exact)

## R2: Aperture Scaling

**Verdict**: MONOTONIC DECREASE
- Aperture 128µm: 240, 192µm: 180, 256µm: 148, 384µm: 117, 512µm: 89
- Counts decrease with resolution

## R3: Random Mechanism

**Verdict**: ~1000× RATIO
- Random fields: ~87,000 winding features
- Lattice: ~89 winding features
- Random fields produce ~1000× more phase singularities

## R4: Grid Convergence

**Verdict**: CONFIRMED TREND
- Grid 64×64: 204, 128×128: 240, 256×256: 148, 512×512: 89
- Same decreasing trend as EXP-2C

## R5: Project-Exact Phase Rotation

**Verdict**: VARIANT
- DBS varies 49× (34 to 1673) — strongly phase-dependent
- Independent winding varies 2.5× (8,513 to 21,344)
- Phase rotation invariance NOT a clean discriminator

## R6: Grid-Converged Detector

**Verdict**: DBS has dead parameter
- DBS counts INCREASE with grid (opposite of expected)
- Root cause: `find_features` min_prominence=0.02 unused (D2)

## R7: D02 Null (DECISIVE)

**Verdict**: LATTICE 191× FEWER THAN D02
- Lattice 7,183 vs D02 56,863 at 256×256
- Even with independent detector, lattice < D02

## R8: Lattice/D02 Ratio Across Grids

**Verdict**: DETECTOR-DRIVEN
- Ratio 0.27→0.99 with grid size (MethodB, buggy)
- Corrected: 0.0045→0.0052 (MethodA)

## R9: Lattice Orientation

**Verdict**: ORIENTATION DEPENDENT (CORRECTED: 6.3× not 2.0×)
- Buggy MethodB: 7,844→15,598 (2.0×)
- Corrected MethodA: 48→977 (8.65× range, at z=+1280)
- Double-np.angle bug inflated previous values 64–152×

## R10: Wavelength Sweep

**Verdict**: WAVELENGTH-INDEPENDENT
- Ratio flat (0.130–0.142) across 405–780nm
- Deficit is spatial (grid alignment), not chromatic

## R11: DBS Fix Verification

**Verdict**: DBS=113 CORRECT; custom function buggy
- Project's find_features: 113 features (valid)
- R11 custom function: 7,844→6,558 (inflated by double-wrap bug)

## R12: EXP-3 Input Permutation Null

**Verdict**: GRID-LOCKING CONFIRMED
- Permutation barely changes count (179→182)
- Confirms EXP-2C: grid-locking is mechanism

## R13: Definitive DBS Test (INVALIDATED, then CORRECTED)

### Original (buggy):
- DBS (MethodA): 113
- Independent winding (MethodB): 7,183
- Claimed undercount: 98.4% — **INVALID** (was caused by double-np.angle bug in winding_count; not a real discrepancy)

### Corrected:
- DBS (MethodA): 113 (VALID)
- Independent winding (fixed MethodB): 113 (matches DBS)
- **No discrepancy exists** — 98.4% claim was based on double-np.angle bug (see docs/bug-history.md)

## See Also

- [R14 Validation](experiment-overview.md)
- [Bug History](bug-history.md)
- [Corrected Report](https://github.com/<username>/EXP-0007/blob/main/archive/historical-results/FINAL_CORRECTED_REPORT.md)
- [FINAL_MANIFEST.json](https://github.com/<username>/EXP-0007/blob/main/research_continuation/FINAL_MANIFEST.json)
