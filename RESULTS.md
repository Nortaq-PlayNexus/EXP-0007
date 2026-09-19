# Results — EXP-0007

## Primary Result

The DBS detector at z=+1280 µm reports **113 features** (independently verified by MethodA and fixed MethodB).

## Validation Results (R14 Phases)

### Independent Confirmation

| Method | Confirmed | Notes |
|--------|-----------|-------|
| A: Loop winding (radii 1-5) | 56 loops | 87.5% on z=0 design (42/48) |
| B: Complex circulation | 56 loops | Matches Method A |
| C: Zero search | 0 | NOT at amplitude zeros |

### Threshold Sensitivity

| Threshold | Count |
|-----------|-------|
| 0.0001 | 102 |
| 0.0005 | 82 |
| 0.0010 | 63 |
| 0.0020 | 44 |
| 0.0050 | 10 |
| 0.0100 | 2 |
| 0.0200+ | 0 |

**Count varies 0→102 across thresholds.** The 113 result is highly threshold-dependent.

### Reverse Propagation

| Test | Vortex Count | Net Charge |
|------|-------------|------------|
| 0 → +1280 (forward) | 113 | -1 |
| +1280 → 0 (reverse) | 48 | 0 |
| 0 → -1280 (negative) | 47 | +1 |
| -1280 → 0 (recovery) | 48 | 0 |

**Propagation is perfectly reversible** (NCC=1.000000), but vortex count drops from 113→48 upon return.

### Z-Sweep

| z | Count | | z | Count |
|---|-------|-|---|-------|
| -2560 | 201 | | -320 | 74 |
| -1920 | 48 | | -160 | 52 |
| -1280 | 47 | | -80 | 158 |
| -640 | 50 | | 0 | 48 |
| -160 | 47 | | +80 | 118 |
| -80 | 158 | | +160 | 130 |
| 0 | 48 | | +320 | 74 |
| +80 | 118 | | +640 | 94 |
| +160 | 130 | | +1280 | 113 |
| +320 | 74 | | +1920 | 64 |
| +640 | 94 | | +2560 | 269 |
| +960 | 94 | | | |

**7 large discontinuities** (>20 vortex changes between adjacent z values). Chaotic and discontinuous.

### Resolution Convergence

| Resolution | Count | Net Charge | Density |
|------------|-------|------------|---------|
| 64×64 | 328 | +4 | 0.080 |
| 128×128 | 1,328 | +16 | 0.081 |
| 256×256 | 5,742 | +22 | 0.088 |

**NO CONVERGENCE.** Count grows as resolution².

### Detector Validation

| Control | Expected | Actual | Verdict |
|---------|----------|--------|---------|
| Plane wave | 0 | 0 | PASS |
| Random phase | ~0 | 21,638 | MASSIVE FALSE POSITIVE |
| Gaussian | 0 | 0 | PASS |
| Single vortex | 1 | 33 | 33× OVERCOUNT |
| Vortex-antivortex | 2 | 0 | COMPLETE MISS |

### Known Vortex Validation

| Known | Expected | Actual | Overcount |
|-------|----------|--------|-----------|
| 1 vortex | 1 | 33 | 33× |
| 2 (pair) | 2 | 0 | Missed entirely |
| 10 | 10 | 90 | 9× |
| 100 | 100 | 1,935 | 19× |

### Null Tests (100 random fields)

| Metric | Value |
|--------|-------|
| Mean random count | 21,670 |
| Median | 21,664 |
| Std | 118 |
| Range | 21,375 - 21,939 |
| **113 at percentile** | **0.0%** |

### Reproducibility (Phase 22)

3 trials: 113/113/113. **DETERMINISTIC.**

### Amplitude-Phase Shuffling (Phase 17)

| Configuration | Count | Implication |
|---------------|-------|-------------|
| Original lattice | 113 | Baseline |
| Shuffled phase | 21,608 | Phase suppresses detection |
| Shuffled amplitude | 2,755 | Amplitude also matters |
| Shuffled both | 21,794 | Both contribute |

## Results Table (Master Evidence)

| Experiment | Question | Result | Evidence Strength | Artifact Risk | Status |
|------------|----------|--------|-------------------|---------------|--------|
| R1 | Phase rotation invariance | INVARIANT (simplified) | MEDIUM | MEDIUM | SUPPORTED |
| R2 | Aperture scaling | MONOTONIC DECREASE | HIGH | LOW | SUPPORTED |
| R3 | Random/lattice ratio | ~1000× ratio | HIGH | LOW | CONFIRMED |
| R4 | Grid convergence | DECREASING TREND | HIGH | LOW | CONFIRMED |
| R5 | Project-exact phase rotation | VARIANT | MEDIUM | HIGH | SUPPORTED |
| R6 | Grid-converged detector | DBS has dead parameter | HIGH | MEDIUM | CONFIRMED |
| R7 | D02 null | LATTICE 191× FEWER | HIGH | LOW | CONFIRMED |
| R8 | Lattice/D02 ratio | DETECTOR-DRIVEN | MEDIUM | HIGH | SUPPORTED |
| R9 | Orientation dependence | ORIENTATION DEPENDENT (8.65× corrected) | HIGH | HIGH | CONFIRMED |
| R10 | Wavelength sweep | WAVELENGTH-INDEPENDENT | MEDIUM | LOW | CONFIRMED |
| R11 | DBS fix verification | DBS=113 correct; custom buggy | HIGH | MEDIUM | CONFIRMED |
| R12 | EXP-3 input permutation | GRID-LOCKING CONFIRMED | HIGH | LOW | CONFIRMED |
| R14 Phase 1 | Independent confirmation | 0/20 at amplitude zeros | HIGH | LOW | CONTRADICTED |
| R14 Phase 2 | Threshold sensitivity | 0→102 range | HIGH | LOW | CONTRADICTED |
| R14 Phase 3 | Reverse propagation | 113→48 (not preserved) | HIGH | LOW | CONTRADICTED |
| R14 Phase 7 | Resolution convergence | 328→5,742 (no convergence) | HIGH | LOW | CONTRADICTED |
| R14 Phase 14 | Detector controls | 9-19× overcount | HIGH | HIGH | CONTRADICTED |
| R14 Phase 15 | Known vortex controls | 33× overcount | HIGH | HIGH | CONTRADICTED |
| R14 Phase null | Null distribution | 0th percentile | HIGH | LOW | CONTRADICTED |
