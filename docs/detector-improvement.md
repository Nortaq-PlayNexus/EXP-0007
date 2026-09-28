# Detector Improvement Proposal — EXP-0007

## Current Detector: DeepBeamScan (DBS)

### How It Works
1. Compute phase differences across 2×2 plaquettes
2. Calculate curl from plaquette contributions
3. Quantize charge: `Q = round(curl / 2π)`
4. Count features where `|Q| > 0.5`

### Known Defects
1. **Dead min_prominence**: Cannot filter by intensity
2. **Overcounts noise**: 21,638 features from random phase
3. **Overcounts known topology**: Single vortex → 33, pair → 0
4. **Grid-locked**: Count varies 48-977 with orientation
5. **Threshold-dependent**: Count varies 0-102 across thresholds
6. **Not resolution-convergent**: 328→1,328→5,742

## Proposed Improved Detector Design

### Core Principle
A vortex is defined by two properties:
1. **Zero amplitude** at the core (|E| → 0)
2. **Non-trivial phase winding** around the core

The improved detector will require BOTH conditions.

### Algorithm

```
Phase 1: Candidate Identification
  Find all grid cells where amplitude < amplitude_threshold
  (Initial threshold: median amplitude / 10)

Phase 2: Winding Verification
  For each candidate:
    Compute winding number at sub-pixel positions
    around the candidate position (5 radii: 1, 2, 3, 4, 5 pixels)
    If winding number is non-zero at any radius:
      Mark as confirmed vortex
    If winding number is zero at all radii:
      Reject as noise

Phase 3: Intensity Validation
  For each confirmed vortex:
    Verify intensity at core < intensity_threshold
    (Default: 0.01 of maximum intensity)

Phase 4: Duplicate Removal
  For closely spaced candidates (< 2 pixels apart):
    Keep only the one with lowest amplitude
    (True vortices have zero amplitude)

Phase 5: Validation
  Run on synthetic test cases:
    Single vortex: expected 1
    4 vortices: expected 4
    100 vortices: expected 100
    Random phase: expected ~0
    Lattice z=0: expected 48
```

### Design Decisions

#### Why Zero-Amplitude First?
- True vortices have |E|→0 at the core
- R14 Phase 1 confirmed: 0/20 DBS features at amplitude zeros
- This is the most fundamental vortex property
- Grid-locking doesn't create amplitude zeros

#### Why Sub-pixel Winding?
- Grid-locking is a pixel-level artifact
- Phase winding is a sub-pixel property
- A vortex has the same topology regardless of grid alignment
- Sub-pixel computation breaks grid-locking

#### Why Multiple Radii?
- A feature might have winding at small radius but not large
- Or vice versa
- Multiple radii captures both core and extended vortices
- Also provides robustness against grid artifacts

#### Why Duplicate Removal?
- A single vortex may span multiple low-amplitude cells
- Without deduplication, one vortex could be counted multiple times
- Keeping the lowest amplitude ensures the true core is selected

### Validation Protocol

| Test | Expected | Purpose |
|------|----------|---------|
| 1 vortex | 1 | Basic correctness |
| 2 (pair) | 2 | Pair detection |
| 4 vortices | 4 | Multiple detection |
| 10 vortices | 10 | Scale test |
| 100 vortices | 100 | Scale test |
| Random phase | ~0 | False positive rate |
| Plane wave | 0 | No false positives |
| Gaussian | 0 | No false positives |
| Lattice z=0 | 48 | Matches design |
| Lattice z=+1280 | ≤113 | Should find fewer than DBS |
| Single vortex (sub-pixel) | 1 | Sub-pixel accuracy |

### Implementation Plan

#### Step 1: Zero-Amplitude Search (Week 1)
- Implement Phase 1: Find amplitude minima
- Validate on synthetic cases
- Tune amplitude_threshold

#### Step 2: Winding Verification (Week 2)
- Implement Phase 2: Sub-pixel winding number
- Validate on synthetic cases
- Tune radii and thresholds

#### Step 3: Full Pipeline (Week 3)
- Combine all phases
- Run full validation suite
- Optimize performance

#### Step 4: Comparison (Week 4)
- Run on all EXP-0007 data
- Compare with DBS results
- Document differences
- Publish comparison

### Expected Outcomes

#### If Improved Detector Finds ~48 at z=+1280
- Evidence that DBS overcounts due to grid-locking
- 113 was primarily a detector artifact

#### If Improved Detector Finds ~113 at z=+1280
- DBS count is correct despite grid-locking
- 65 extra features may be real propagation effects
- More investigation needed

#### If Improved Detector Finds <48 at z=+1280
- DBS overcounts at z=+1280
- Some "features" are not real vortices
- Even fewer features are propagation-generated

### Advantages Over DBS

| Property | DBS | Improved |
|----------|-----|----------|
| Zero-amplitude requirement | No | Yes |
| Sub-pixel computation | No | Yes |
| Grid-locking immune | No | Partially |
| Noise rejection | No (21K from random) | Yes (target ~0) |
| Known vortex validation | Fails | Passes |
| Intensity filtering | Dead parameter | Active |
| Duplicate removal | No | Yes |

### Disadvantages

- More computationally expensive (~10× slower)
- More complex implementation
- Sub-pixel computation requires careful implementation
- May miss features that don't have zero amplitude (if they exist)

### Code Structure

```
src/detection/
├── improved_detector.py          # Main detector class
├── zero_amplitude_search.py      # Phase 1
├── subpixel_winding.py           # Phase 2
├── intensity_validation.py       # Phase 3
├── duplicate_removal.py          # Phase 4
└── validation_suite.py           # Phase 5
```

### Dependencies
- NumPy (same as EXP-0007)
- SciPy (for sub-pixel interpolation)
- No new dependencies required
