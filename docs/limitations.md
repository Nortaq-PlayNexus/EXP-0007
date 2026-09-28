# Limitations — EXP-0007

## Unresolved Questions

### 1. Are the 65 propagation-generated features real?
**Status**: UNRESOLVED
The 65 features appearing at z=+1280 (vs 48 at z=0) could be:
- Real propagation-generated vortices (unlikely given all other evidence)
- Grid-locking artifacts (most likely — phase complexity increases with propagation)
- Numerical artifacts (possible — detector instability at propagation distances)

### 2. Does D02 use the buggy winding_count?
**Status**: UNRESOLVED
D02 measurements (~21,608) may or may not be affected by the double-np.angle bug. If D02 uses the project's own `find_features` (which doesn't have the bug), D02 is unaffected.

### 3. What is the TRUE vortex count at z=+1280?
**Status**: UNRESOLVED
113 seems correct for DBS at 256², but grid-locking effects at different orientations (8.65× range) suggest this is grid-dependent.

### 4. Are R11 and R12 results affected?
**Status**: PARTIALLY RESOLVED
Both used MethodB (double-wrap buggy). Absolute counts are wrong. Ratios may still be valid if both compared quantities used the same buggy method.

### 5. Phase-unwrapping statistic
**Status**: UNRESOLVED
The 773,912 change needs independent audit (R14 Phase 8).

### 6. Wavelength sweep with corrected MethodB
**Status**: UNVERIFIED
R10 wavelength-independence finding may still hold but needs confirmation with corrected MethodB.

## Known Bugs (Do Not Explain Non-Existent Discrepancy)

| Bug | Severity | Affects R13? |
|-----|----------|-------------|
| D1: propagate_fresnel sign | HIGH | Yes (minor) |
| D2: find_features dead parameter | HIGH | Yes (reverse) |
| D3: lattice_params constant guard | LOW | No |
| D4: independent_asm normalization | MEDIUM | No |
| D5: radial_power_spectrum bias | MEDIUM | No |
| D6: Circular wrap-around | MEDIUM | Yes (minor) |

## Methodological Limitations

1. **DBS overcounts noise**: 21,638 features from random phase
2. **No resolution convergence**: Feature count depends on grid size
3. **Threshold dependence**: Count varies 0→102 across thresholds
4. **Orientation dependence**: 8.65× range at z=+1280
5. **Grid-locking**: Features depend on pixel alignment
6. **Single detector**: All results from one detector type
7. **Simulation only**: No physical experimental validation

## Data Limitations

1. All EXP-0001 through EXP-0025 directories are EMPTY
2. EXP-0007's own reports/ subdir is EMPTY
3. No git history available
4. Seed labels in data files were swapped (exp2b_D02_42.jsonl and exp2b_D02_7.jsonl)
5. Some large PNG figures (5+ MB) excluded from hash manifest

## Interpretive Limitations

1. No physical mechanism for vortex creation proposed or demonstrated
2. Propagation sign bug (D1) means all +z results are actually -z results
3. DBS defects affect measurement quality but don't explain a non-existent discrepancy
4. Cannot distinguish grid-locking from physical effects with current data alone
