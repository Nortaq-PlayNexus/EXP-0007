# Zenodo Upload Package — EXP-0007

## Upload Configuration

| Field | Value |
|-------|-------|
| Upload type | dataset |
| Title | EXP-0007: Coherent Optical Vortex Propagation — R14 Validation Study |
| Subtitle | Systematic investigation of propagation-generated topological vortex structures with full bug verification and artifact analysis |
| Version | v1.1.0 |
| Publication date | 2026-09-19 |
| DOI | (to be assigned by Zenodo) |
| Description | See description/abstract below |

## Creators

| Name | Affiliation | ORCID |
|------|-------------|-------|
| EXP-0007 Research Team | Scientific Discovery Lab | (to be assigned) |

## Keywords

coherent optics, optical vortices, vortex lattice, Fresnel propagation, DeepBeamScan, feature detection, detector artifact, grid-locking, reproducibility, simulation, topological structure, phase singularities, z-sweep, bug verification, D1 propagation bug, double-np.angle, simulation data

## Description / Abstract

This dataset contains the complete results of EXP-0007, a systematic investigation of whether coherent optical propagation through free space generates novel topological vortex structures beyond those present in the initial field. The study propagated a 256×256 pixel simulation of a laser beam containing an 8×6 vortex lattice (48 design vortices) to z=+1280 µm and measured feature counts using the DeepBeamScan (DBS) detector.

The apparent 113-vortex population at z=+1280 (vs. 48 at z=0) was initially reported as a +135% increase, suggesting propagation-generated vortex creation. However, R14 validation (24 phases) determined this result is a systematic detector + grid-locking artifact, not physical vortex creation.

Key findings documented in this dataset:
1. The 113 features at z=+1280 are reproducible but topologically meaningless artifacts
2. A double-np.angle software bug in winding_count() invalidated all R13-based MethodB conclusions (7,183 → 113)
3. A propagation sign bug (D1) in the project's propagate_fresnel function produces measurable, reproducible directional effects (47 vs 113 at |z|=1280 depending on sign)
4. The detector cannot preserve known topology (overcounts 9-19× on known vortices, misses vortex pairs entirely)
5. Feature counts are chaotic across propagation distances (7 discontinuities in z-sweep)
6. 113 is at the 0th percentile of random field null distribution (21,670 mean)

This dataset includes all raw data, processed results, validation scripts, test suites, bug analyses, and complete documentation for full reproducibility.

## Technical Methods

### Field Construction
- Vortex crystal field: `vortex_crystal_field(shape=(256,256), rows=6, cols=8, pixel_size=1e-6, wavelength_nm=694.3)`
- Complex field representation: ComplexField(amplitude, phase, pixel_size, wavelength)

### Propagation Methods
1. Project Fresnel: `propagate_fresnel(E0, z=±1280, pixel_size=1e-6)` — has D1 sign bug (propagates -z)
2. Independent ASM: Reference implementation using `H = exp(1j·kz·z)`, `kz = sqrt(k0² - (2π·FX)² - (2π·FY)²)`
3. NCC verification: NCC(project Fresnel z=+1280 call, ASM z=-1280) = 1.000000 (confirms D1)

### Feature Detection
- DeepBeamScan (DBS): Primary detector for phase singularities
- MethodA: DBS find_features() — primary method
- MethodB: Winding number count — fixed (double-np.angle bug corrected)
- MethodC: Zero-amplitude search — confirms 0/20 features at amplitude zeros

### Validation Phases (R14 — 24 phases executed)
1. Independent confirmation (3 methods × 20 candidates)
2. Threshold sensitivity (7 thresholds: 0.0001 to 0.02)
3. Reverse propagation (NCC=1.0, recovery verified)
4. Z-sweep (15 distances from -2560 to +2560 µm)
5. Resolution convergence (64×64, 128×128, 256×256)
6. Numerical precision (float32 vs float64)
7. Phase precision (max error 4.94e-11)
8. Charge conservation
9. Detector validation (6 synthetic controls + 4 known-vortex tests)
10. Null distribution (100 random fields)
11. Reproducibility (3 trials × 50 statistical trials)
12. Amplitude-phase shuffling (4 configurations)
13. Spectral/aliasing analysis
14. Position tracking (feature trajectory across z)
15-24. Additional controlled experiments

## Data Collection

### Data Sources
| Source | Description | Location |
|--------|-------------|----------|
| vortex_crystal_field | Initial 48-vortex lattice | scripts/run_r14.py |
| propagate_fresnel | Project propagation (D1 bug) | Project codebase |
| independent_asm | Reference propagation | scripts/run_r14.py |
| DeepBeamScan.find_features | Primary detector | Project codebase |
| winding_count | Fixed MethodB | scripts/run_r14.py |

### Data Files
| File | Description | Size |
|------|-------------|------|
| results/r14/DEFINITIVE_DBS_TEST.json | Independent verification | ~5 KB |
| results/r14/z_sweep.json | Z-sweep (15 distances) | ~5 KB |
| results/r14/threshold_sweep.json | Threshold sensitivity (7 thresholds) | ~5 KB |
| results/r14/resolution_convergence.json | Resolution dependence | ~5 KB |
| results/r14/detector_validation.json | Detector validation (7 controls) | ~5 KB |
| results/r14/null_distribution.json | Null distribution (100 fields) | ~5 KB |
| results/r14/phase_results.json | R14 phase results | ~5 KB |
| results/r14/lightweight.json | Lightweight validation | ~5 KB |
| results/r14/definitive.json | Definitive R14 reproduction | ~5 KB |
| research_continuation/*.json | Original R1-R12 data | ~5-15 KB each |
| research_continuation/r14_summary.json | R14 summary (22 phases) | ~5 KB |
| research_continuation/r13_forensic_results.csv | R13 forensic analysis | ~5 KB |

## Limitations

1. **65 propagation-generated features uncharacterized**: Features appearing during propagation (z=0→z=+1280) are likely grid-locking artifacts but not fully characterized
2. **R11/R12 need re-run with corrected MethodB**: Absolute counts were inflated by 64-152×
3. **D02 measurement method unverified**: D02 count of 21,608 may or may not use buggy winding_count
4. **Wavelength sweep (R10) needs re-verification**: Wavelength-independence finding may hold but needs confirmation
5. **No physical experimental validation**: This is a simulation study only
6. **Single detector**: All results from DeepBeamScan — other detectors may give different results
7. **Project code has D1 propagation bug**: Results using project's propagate_fresnel at z=+1280 are actually at z=-1280 (47 features, not 113)

## Ethical Considerations

- No human subjects involved
- No sensitive data
- All code and data are openly available
- No fabricated data or results
- All bugs are documented, not hidden
- Scientific claims are conservative and evidence-based

## Funding

(To be completed by author)

## References

1. EXP-0007 repository: https://github.com/Nortaq-PlayNexus/EXP-0007
2. R14 validation phases (24 total) documented in docs/r14-validation.md
3. Bug history documented in docs/bug-history.md
4. D1 propagation bug documented in docs/d1-bug-effect.md
5. Full methods in docs/mathematical-background.md and docs/propagation-implementation.md
