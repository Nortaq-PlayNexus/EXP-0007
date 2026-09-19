# ROADMAP — EXP-0007

## Completed

- [x] R14 validation (24 phases executed)
- [x] Bug discovery and documentation (6 defects identified)
- [x] Independent verification (MethodA = fixed MethodB = 113)
- [x] Repository build (this repository)
- [x] Test suite creation
- [x] CI/CD workflows
- [x] Documentation (all required docs)

## Next Steps (Priority Order)

### 1. Fix DBS Dead Parameter (HIGH)
- Fix `find_features` min_prominence in project code
- Re-run and publish detector calibration finding
- **Potential publication**: Detector calibration study

### 2. Characterize 65 Propagation Features (HIGH)
- Time-lapse propagation: z=0→320→640→960→1280
- Determine if features are propagation effects, grid-locking artifacts, or numerical artifacts
- Check intensity profiles at intermediate z values

### 3. Re-run with Corrected MethodB (HIGH)
- Fix `winding_count` in all research continuation scripts
- Re-run R11, R12, R9 with fixed MethodB for absolute counts
- Verify R7 D02 direction with corrected counts

### 4. Verify D02 Method (MEDIUM)
- Confirm D02 measurement method does not use buggy winding_count
- If D02 uses valid method, the lattice/D02 deficit (113 vs 21,608) is robust

### 5. Publish Grid-Locking Study (MEDIUM)
- Orientation dependence (8.65× range) is publishable as grid-locking characterization
- Resolution dependence data available
- Null test data available

### 6. EXP-3 Input Permutation (MEDIUM)
- Designed but not executed
- Would provide additional null-test evidence

### 7. Zenodo Archival (LOW)
- Prepare for Zenodo release (see docs/zenodo-release.md)
- Obtain DOI through Zenodo

### 8. Future Experiments (LOW)
- Alternative detector designs (sub-pixel, adaptive)
- 3D propagation studies
- Physical experimental validation (if feasible)
