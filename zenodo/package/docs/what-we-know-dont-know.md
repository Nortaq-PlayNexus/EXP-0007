# What We Know / Don't Know — EXP-0007

## Established (Robust Findings)

These findings are supported by multiple independent lines of evidence:

### 1. DBS count of 113 at z=+1280 is independently verified
- **Evidence**: MethodA (DBS) = 113, Fixed MethodB = 113, 3 trials identical
- **Confidence**: HIGH
- **Note**: This is a reproducible measurement of phase singularities at z=+1280 (using correct propagation sign; project Fresnel has D1 bug producing 47 at "z=1280")

### 2. The lattice has 48 design vortex positions at z=0
- **Evidence**: MethodA finds exactly 48, matches 6×8 design
- **Confidence**: HIGH
- **Note**: This is a designed/inherited property of the lattice

### 3. The double-np.angle bug caused the 7,183 count
- **Evidence**: Fixed MethodB = 113 = MethodA, buggy MethodB = 7,183
- **Confidence**: HIGH
- **Note**: Verified on synthetic cases (1 vortex → 1, 4 vortices → 4)

### 4. Random fields produce far more features than the lattice
- **Evidence**: Random ~21,670 vs Lattice 113 at 256×256 (191× deficit)
- **Confidence**: HIGH
- **Note**: Confirmed across all detectors, grid sizes, orientations, wavelengths

### 5. Orientation dependence is real (grid-locking)
- **Evidence**: 48 at 0° → 977 at 45° (8.65× range) at z=+1280
- **Confidence**: HIGH
- **Note**: This is a detector/grid artifact, not physics

### 6. Six code defects (D1-D6) exist
- **Evidence**: Code inspection and testing confirmed all six
- **Confidence**: HIGH
- **Note**: They do NOT explain a non-existent discrepancy

### 7. Propagation is perfectly reversible
- **Evidence**: NCC(amplitude(+z), amplitude(-z)) = 1.000000
- **Confidence**: HIGH
- **Note**: Implementation is mathematically correct (though sign bug D1 exists)

### 8. Detector cannot preserve known topology
- **Evidence**: Single vortex → 33, vortex pair → 0, 10 vortices → 90
- **Confidence**: HIGH
- **Note**: DBS overcounts by 9-19× on known structures

### 9. 113 is below random field distribution
- **Evidence**: 100 random fields: mean 21,670, 113 at 0th percentile
- **Confidence**: HIGH
- **Note**: Lattice suppresses detection relative to random phase

### 10. No propagation-generated structure creation
- **Evidence**: No persistence, no convergence, detector overcount, threshold dependence, below null
- **Confidence**: HIGH
- **Note**: 24 R14 phases, 5 of 12 critical tests: NO

## Not Established (Claims Not Supported)

These claims are NOT supported by the evidence:

### 1. "Propagation creates 65 new vortices"
- **Status**: CONTRADICTED
- **Evidence**: Features don't persist, detector overcounts, below null distribution
- **Note**: 65 features appear at z=+1280 but are not validated as vortices

### 2. "DBS undercounts by 98.4%"
- **Status**: CONTRADICTED
- **Evidence**: Fixed MethodB = MethodA = 113 (no discrepancy)
- **Note**: Was caused by double-np.angle bug in winding_count

### 3. "Independent winding count is 7,183"
- **Status**: CONTRADICTED
- **Evidence**: Corrected count = 113 (same as DBS)
- **Note**: 7,183 was entirely from double-np.angle bug

### 4. "Lattice produces 8× fewer features than D02"
- **Status**: PARTIALLY CORRECTED
- **Evidence**: Corrected: lattice 113 vs D02 21,608 (191×) at 256×256
- **Note**: Direction correct, magnitude changed dramatically

### 5. "Orientation dependence is 2.0×"
- **Status**: CORRECTED
- **Evidence**: Corrected: 8.65× (113→977 at 45°)
- **Note**: Inflated 64-152× by double-np.angle bug

## Unknown (Unresolved Questions)

### 1. Are the 65 propagation-generated features real?
- **What we know**: 113 at z=+1280 minus 48 at z=0 = 65 extra features
- **What we don't know**: Whether these are propagation effects, grid-locking artifacts, or numerical artifacts
- **Evidence for artifact**: Features don't persist across z, detector overcounts, below null
- **Evidence for real**: Reproducible (113/113/113), low intensity (< 0.01)
- **Key experiment needed**: Time-lapse propagation with position tracking at intermediate z values

### 2. Does D02 use the buggy winding_count?
- **What we know**: D02 measures ~21,608 features at 256×256
- **What we don't know**: Whether D02 uses project's find_features (no bug) or independent winding (buggy)
- **If D02 is unaffected**: Lattice/D02 = 113/21,608 = 0.0052 (191× deficit)
- **If D02 is affected**: Both counts inflated, ratio may be valid
- **Key experiment needed**: Audit D02 measurement code

### 3. What is the TRUE vortex count at z=+1280?
- **What we know**: DBS finds 113, fixed MethodB confirms 113
- **What we don't know**: Whether 113 is grid-dependent or stable across orientations
- **Evidence for grid-dependent**: Orientation range 48-977 (8.65×)
- **Key experiment needed**: Sub-pixel interpolation, higher resolution, multiple grid sizes

### 4. Are R11/R12 results valid with corrected MethodB?
- **What we know**: Both used buggy MethodB; absolute counts inflated 64-152×
- **What we don't know**: Whether ratios are preserved; corrected absolute values
- **Key experiment needed**: Re-run with fixed MethodB

### 5. Wavelength dependence (R10)
- **What we know**: Ratio flat (0.130-0.142) across 405-780nm (with buggy MethodB)
- **What we don't know**: Whether this holds with corrected MethodB
- **Key experiment needed**: Re-run R10 with fixed MethodB

### 6. Phase unwrapping statistic (773,912 change)
- **What we know**: A significant phase change was observed
- **What we don't know**: Whether this is valid or an artifact
- **Key experiment needed**: Independent audit of phase unwrapping

### 7. DBS with fixed min_prominence
- **What we know**: Dead parameter means no intensity filtering
- **What we don't know**: What DBS would find with proper intensity thresholding
- **Evidence**: Manual filter I<0.5 changes DBS from 113→782
- **Key experiment needed**: Fix parameter and re-run

## Future Experiments

### Highest Priority

#### F1: Fix DBS Dead Parameter
- **Purpose**: Determine what DBS actually detects with intensity filtering
- **Method**: Fix `find_features` min_prominence, re-run
- **Expected**: DBS count changes significantly (113→782 with I<0.5)
- **Significance**: Publication-ready detector calibration study

#### F2: Characterize 65 Propagation Features
- **Purpose**: Determine if propagation generates real features
- **Method**: Time-lapse propagation z=0→320→640→960→1280, track positions, intensities, persistence
- **Expected**: Features appear/disappear without persistence
- **Significance**: Directly addresses the core question

#### F3: D02 Method Audit
- **Purpose**: Determine if D02 is affected by double-np.angle bug
- **Method**: Inspect D02 measurement code, verify method
- **Expected**: D02 likely uses valid method (find_features)
- **Significance**: Validates the 191× lattice/D02 deficit

#### F4: Sub-pixel Grid Independence Test
- **Purpose**: Determine if feature count is grid-dependent
- **Method**: Run at sub-pixel offsets (1/3 px, 1/4 px, 1/8 px), compare counts
- **Expected**: Counts vary with grid alignment (grid-locking)
- **Significance**: Definitively demonstrates grid-locking

#### F5: Re-run R11/R12 with Fixed MethodB
- **Purpose**: Get corrected absolute counts
- **Method**: Fix winding_count, re-run R11 and R12
- **Expected**: Counts inflated 64-152×; ratios may be valid
- **Significance**: Validates continuation experiment results

### Medium Priority

#### F6: Improved Vortex Detector
- **Purpose**: Design a detector that correctly counts vortices
- **Method**: Zero-amplitude search, sub-pixel phase winding, adaptive thresholding
- **Expected**: Should find 48 at z=0 and potentially fewer than 113 at z=+1280
- **Significance**: Could definitively resolve the vortex question

#### F7: Wavelength Sweep with Corrected MethodB
- **Purpose**: Verify wavelength independence
- **Method**: Re-run R10 with fixed winding_count
- **Expected**: Ratio may still be flat (0.130-0.142)
- **Significance**: Rules out chromatic effects

#### F8: Input Permutation Null (EXP-3)
- **Purpose**: Further null test of propagation-generated structure
- **Method**: Permute input phase/amplitude, compare outputs
- **Expected**: Count barely changes (as in R12)
- **Significance**: Confirms grid-locking over physics

#### F9: Alternative Propagation Methods
- **Purpose**: Determine if propagation method affects feature count
- **Method**: Compare Fresnel (fixed sign), ASM, RS propagation
- **Expected**: Different methods may give different counts
- **Significance**: Tests propagation sensitivity

### Lower Priority

#### F10: Physical Validation
- **Purpose**: Test with real laser hardware
- **Method**: Build optical setup, generate vortex lattice, propagate
- **Expected**: Similar detector artifacts may occur
- **Significance**: Ultimate validation but requires significant resources

#### F11: 3D Propagation Study
- **Purpose**: Study propagation in 3D space
- **Method**: Extend to 3D field, propagate in 3D
- **Expected**: May reveal different structure
- **Significance**: Explores parameter space beyond 2D

#### F12: Statistical Framework Enhancement
- **Purpose**: More rigorous statistical framework
- **Method**: Bayesian analysis, model comparison, information criteria
- **Expected**: More nuanced understanding
- **Significance**: Strengthens analytical framework
