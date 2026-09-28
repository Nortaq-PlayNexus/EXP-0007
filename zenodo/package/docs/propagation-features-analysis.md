# Propagation Features Analysis — The 65 Extra Features

## Question

DBS finds 113 features at z=+1280 but only 48 at z=0. The 65 extra features (113-48) appear during propagation. Are they real propagation-generated vortices or artifacts?

## Evidence FOR Artifact

### 1. No Position Persistence
R14 Phase 21 tracked feature positions:
- All tracked features LOST at other z values
- 0 persistence across z
- Features appear/disappear without tracking

### 2. Z-Sweep Shows Chaotic Behavior
R14 Phase 4 (15 distances):
```
z=-2560: 201 → z=-1280: 47 → z=0: 48 → z=+1280: 113 → z=+2560: 269
```
7 large discontinuities (>20 change between adjacent z values). Physical vortex creation/annihilation should be smooth, not chaotic.

### 3. Below Null Distribution
Random fields produce ~21,670 features. The lattice's 113 is at the 0th percentile. If propagation created 65 real features, they should still be detectable above noise.

### 4. Detector Cannot Preserve Known Topology
R14 Phase 15: Known vortex structures are overcounted by 9-19×. A detector that overcounts this much cannot reliably claim to have found new features.

### 5. Threshold Dependence
R14 Phase 2: Count varies 0→102 across thresholds. At any reasonable threshold (I≥0.01), only 2 features survive. The 113 count is threshold-specific.

### 6. Features Not at Amplitude Zeros
R14 Phase 1: MethodC confirmed 0/20 features at true amplitude zeros. True vortices require |E|→0 at the core. These are rapid phase changes at nonzero amplitude — consistent with grid-locking, not genuine vortices.

### 7. Intensity Profile
- 98.2% of 113 features have I < 0.01
- Median intensity: 0.0012
- Features are at very low intensity, consistent with phase artifacts

### 8. Reverse Propagation
Forward 0→+1280: 113 features. Reverse +1280→0: 48 features. The 65 features disappear when propagating back. They are not preserved by the field.

### 9. No Grid Convergence
R14 Phase 7: Count changes from 328→1,328→5,742 with resolution. The 113 count at 256×256 is just one point on a diverging series.

## Evidence FOR Real (Unlikely)

### 1. Reproducibility
3 trials give identical results (113/113/113). But deterministic artifacts are also reproducible.

### 2. Low Intensity
All 113 features have intensity < 0.1. This is consistent with phase singularities (vortex cores have zero amplitude).

### 3. Phase Singularity Nature
R14 Phase 1: Methods A and B confirm these are phase singularities (56 loops confirmed).

### 4. No Known Alternative Explanation
While grid-locking explains the total count, it doesn't fully explain the 48→113 increase specifically at z=+1280.

## Analysis by Orientation

From R9 orientation data (corrected MethodA):
- At 0° (aligned with grid): 113 features (grid-locked, matches design pattern)
- At 45° (misaligned): 977 features (grid-unlocked, more features visible)
- At 90° (aligned): 113 features (grid-locked again)

**Key insight**: The 113 count at standard orientation may be grid-locked. At 45°, the detector finds 977 features. The "65 extra features" might be a subset of the 977 that happen to align with the grid at z=+1280.

## Analysis by Resolution

From R14 Phase 7:
- 64×64: 328 features
- 128×128: 1,328 features
- 256×256: 5,742 features (R14 detector, not DBS)

The count grows as resolution². The 113 count (DBS at 256×256) is a tiny fraction of the 5,742 found by the R14 detector at the same resolution. This suggests DBS is severely undercounting at standard orientation due to grid-locking.

## Conclusion

**The 65 propagation-generated features are most likely grid-locking artifacts**, not physical vortex creation. The evidence overwhelmingly supports this interpretation:

1. No persistence across z (Phase 21)
2. Chaotic z-sweep behavior (Phase 4)
3. Below null distribution (Phase 13)
4. Detector overcounts known topology (Phase 14-15)
5. Threshold-dependent (Phase 2)
6. Not at amplitude zeros (Phase 1)
7. Features disappear on reverse propagation (Phase 3)
8. No resolution convergence (Phase 7)

**Confidence**: HIGH that these are artifacts. The only remaining question is whether some subset of the 113 represents real propagation-induced phase structure that the detector is misclassifying as artifacts. This requires a better detector to resolve.

## Recommended Experiment

**F2: Time-lapse propagation study**
- Run at sub-pixel offsets (1/3 px, 1/4 px)
- Track features at z=0→320→640→960→1280 at each offset
- Compare position sets across offsets and z values
- If features are grid-locked, they will appear/disappear differently at different offsets
- If features are physical, they will persist consistently across offsets
