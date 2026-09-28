# R14 Validation — Central Study

## Overview

R14 is the central validation study for EXP-0007. It tested whether the R13 finding of 113 vortices at z=+1280 represents genuine topological creation. **24 phases were executed.**

## Verdict

**The 113-vortex result is a SYSTEMATIC DETECTOR + GRID-LOCKING ARTIFACT, not physical vortex creation.**

## Summary of All 24 Phases

### Phase 1: Independent Validation
Three independent methods on 20 candidates:
- Method A (loop winding): 56 loops confirmed (87.5% on design)
- Method B (complex circulation): 56 loops (matches A)
- Method C (zero search): **0/20 confirmed** — NOT at amplitude zeros

### Phase 2: Threshold Sensitivity
Count varies 0→102 across 7 thresholds. At I≥0.01, only 2 features survive.

### Phase 3: Reverse Propagation
- Forward 0→+1280: 113 vortices
- Reverse +1280→0: **48 vortices** (features disappear)
- Propagation perfectly reversible (NCC=1.0), vortices NOT preserved

### Phase 4: Z-Sweep
15 distances tested. **7 large discontinuities** (>20 vortex changes). Chaotic, not smooth.

### Phase 5: Defect Analysis
6 defects (D1-D6) documented but do NOT explain 113 vs 113 (no discrepancy).

### Phase 6: Propagation Sign
H(+z)×H(-z)≈1 verified. **PASS** — propagation implementation is correct.

### Phase 7: Resolution Convergence
328→1,328→5,742 with increasing resolution. **NO CONVERGENCE.**

### Phase 8: Numerical Precision
Float32=Float64=113 (113/113 overlap). **NOT a floating-point artifact.**

### Phase 9: Amplitude-Phase Shuffling
- Original lattice: 113
- Shuffled phase: **21,608** — phase suppresses detection
- Shuffled amplitude: 2,755
- Shuffled both: 21,794

### Phase 10: Charge Conservation
- z=0: net=0 (balanced)
- z=+1280: net=-1 (4 boundary vortices explain imbalance)

### Phase 11: DBS Defect Verification
6 defects confirmed (D1-D6). None individually explain a discrepancy (because none exists).

### Phase 12: Null Field Comparison
Null fields have ~15× more features than propagated lattice. Confirmed with DBS.

### Phase 13: Null Distribution (100 random fields)
- Mean random: 21,670
- **113 at 0th percentile** — far below random expectations

### Phase 14: Detector Validation (6 controls + 4 known vortices)
- Plane wave: PASS (0→0)
- Random phase: **FAIL** (21,638, massive false positive)
- Single vortex: **FAIL** (33× overcount)
- Vortex-antivortex: **FAIL** (complete miss)

### Phase 15: Known Vortex Validation
- 1 vortex → 33 (33× overcount)
- 2 pair → 0 (complete miss)
- 10 → 90 (9× overcount)
- 100 → 1,935 (19× overcount)

### Phase 16: Comparison with Independent ASM
Independent ASM propagation finds **0 vortices** vs DBS 113. **FAIL.**

### Phase 17: Amplitude-Phase Shuffling
Detailed shuffling analysis confirms lattice phase pattern suppresses detection from 21,608→113.

### Phase 18: Spectral/Aliasing
0% edge energy at z=0 and z=1280. No Nyquist folding. Central peak dominant.

### Phase 19: Propagation Time-Lapse
Features appear/disappear across z with no persistence pattern.

### Phase 20: Statistical Stability
50 trials: 113/113/113... all identical. **DETERMINISTIC** (not random, but also not physical).

### Phase 21: Position Tracking
All tracked features LOST at other z values. **0 persistence** across z.

### Phase 22: Reproducibility
3 trials: 113/113/113. **DETERMINISTIC.**

### Phase 23: Threshold × Grid Interaction
Feature count depends on interaction of threshold and grid size. No stable count.

### Phase 24: Final Assessment
12 critical questions answered:
- **5 NO**
- **2 UNRESOLVED**
- **1 PARTIALLY**
- **2 YES** (stability, reproducibility — but these don't imply physics)

**Verdict: NOT confirmed as physical vortex creation.**

## Evidence Matrix

| Test | Result | Implication |
|------|--------|-------------|
| Method C zero search | 0/20 confirmed | Not true phase singularities |
| Threshold sweep | 0→102 | Highly threshold-dependent |
| Reverse propagation | 113→48 | Not preserved by reversal |
| Z-sweep | 7 discontinuities | Unstable across z |
| Resolution | No convergence | Scales with grid density |
| Known vortex 1→33 | 33× overcount | Detector unreliable |
| Random field | 21,670 | Massive false positive |
| Null distribution | 0th percentile | 113 far below random |
| Independent propagation | FAIL | Angular spectrum: 0 vs 113 |
| Position tracking | SUPPORTED | All features LOST at other z |

## Claim Status

| Claim | Status |
|-------|--------|
| 113 candidates confirmed | **NO** — Method C: 0/20 |
| Survives threshold changes | **NO** — 0→102 |
| Survives resolution changes | **NO** — 328→5,742 |
| Survives float32→64 | YES — Stable |
| Independent propagation | **NO** — 0 vs 113 |
| Forward/backward reversible | PARTIALLY — field yes, vortices no |
| Charge explained by boundaries | LIKELY |
| Phase-unwrapping valid | UNRESOLVED |
| Detector passes controls | **NO** — 9-19× overcount |
| Exceeds null expectations | **NO** — 0th percentile |
| Vortex trajectories show creation | **NO** — 0 persistence |
| Initial field has structure | YES — 48 design vortices |
