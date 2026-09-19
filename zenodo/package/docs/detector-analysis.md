# Detector Analysis — DeepBeamScan (DBS)

## Overview

DeepBeamScan (DBS) is the feature detector used throughout EXP-0007. It identifies phase singularities using winding-number topology.

## Inputs

| Input | Description |
|-------|-------------|
| ComplexField | 2D complex optical field E(x,y) |
| (optional) min_prominence | **DEAD PARAMETER** — declared but never used |

## Outputs

| Output | Description |
|--------|-------------|
| features[] | List of detected features |
| features[].y | Row position |
| features[].x | Column position |
| features[].charge | Topological charge (integer) |
| features[].intensity | Normalized intensity at feature |
| features[].type | Feature type classification |

## Algorithm

1. **Phase differences**: Compute δ = phase[i+1,j] - phase[i,j] for all adjacent pairs
2. **Phase wrapping**: Apply `np.angle(exp(1j*δ))` to get principal phase difference
3. **Curl calculation**: Sum 4 plaquette contributions around each 2×2 cell
4. **Charge quantization**: `Q = round(curl / 2π)`
5. **Threshold**: Count features where `|Q| > 0.5`

## Known Defects

### D2: Dead min_prominence Parameter
- **Location**: `find_features(self, field, min_prominence=0.02)`
- **Issue**: Parameter declared but never used in function body
- **Effect**: Cannot filter features by intensity; counts ALL phase-gradient plaquettes
- **Impact**: DBS overcounts random noise (14,113 features in random field)
- **Verified**: Only 1 occurrence of 'min_prominence' in entire deep_scan.py (signature only)

## Detector Validation Results (R14)

| Test | Expected | Actual | Verdict |
|------|----------|--------|---------|
| Plane wave | 0 | 0 | PASS |
| Random phase | ~0 | 21,638 | **FAIL** |
| Gaussian | 0 | 0 | PASS |
| Single vortex | 1 | 33 | **FAIL** (33×) |
| Vortex pair | 2 | 0 | **FAIL** (missed) |
| 10 vortices | 10 | 90 | **FAIL** (9×) |
| 100 vortices | 100 | 1,935 | **FAIL** (19×) |

## Known Limitations

1. **Overcounts noise**: 21,638 features from random phase (should be ~0)
2. **Overcounts on known topology**: 33× for single vortex, 19× for 100 vortices
3. **Misses paired vortices**: Complete miss on vortex-antivortex pair
4. **Grid-dependent**: Feature count varies with lattice orientation (grid-locking)
5. **Threshold-dependent**: Count varies 0→102 across thresholds
6. **Not resolution-convergent**: 328→1,328→5,742
7. **Not resolution-convergent**: 328→1,328→5,742

## R14 Demonstrated Artifacts

R14 demonstrated detector overcounting in controlled tests:
- **9-19× overcount** on known topology
- **Complete misses** on vortex pairs
- **0th percentile** of null distribution (113 far below random 21,670)

## Comparison with Methods

| Method | Single Vortex | 4 Vortices | Lattice z=0 | Lattice z=1280 |
|--------|--------------|------------|-------------|----------------|
| MethodA (DBS) | 1 ✓ | 4 ✓ | 48 ✓ | 113 ✓ |
| MethodB (fixed) | 1 ✓ | 4 ✓ | 48 ✓ | 113 ✓ |
| MethodB (buggy) | 127 ✗ | 609 ✗ | 4,612 ✗ | 7,183 ✗ |
| MethodC (zero) | — | — | — | 0/20 confirmed |

## Recommendations for Future

1. Fix `min_prominence` parameter to actually filter by intensity
2. Add sub-pixel interpolation
3. Implement adaptive thresholding
4. Add synthetic validation tests to detector codebase
5. Consider alternative vortex detection methods (e.g., phase gradient, zero-crossing)
