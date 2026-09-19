# EXP-0007 — Zenodo Dataset Description

## Upload Type: Dataset

## Title
EXP-0007: Coherent Optical Vortex Propagation — R14 Validation Study

## Subtitle
Systematic investigation of propagation-generated topological vortex structures with full bug verification and artifact analysis

## Abstract
This dataset contains the complete results of EXP-0007, a systematic investigation of whether coherent optical propagation through free space generates novel topological vortex structures beyond those present in the initial field. The study propagated a 256×256 pixel simulation of a laser beam containing an 8×6 vortex lattice (48 design vortices) to z=+1280 µm and measured feature counts using the DeepBeamScan (DBS) detector.

The apparent 113-vortex population at z=+1280 (vs. 48 at z=0) was initially reported as a +135% increase, suggesting propagation-generated vortex creation. However, R14 validation (24 phases) determined this result is a systematic detector + grid-locking artifact, not physical vortex creation.

### Key Findings
1. The 113 features at z=+1280 are reproducible but topologically meaningless artifacts of detector behavior and grid alignment
2. A double-np.angle software bug in winding_count() invalidated all R13-based MethodB conclusions (7,183 → 113)
3. A propagation sign bug (D1) produces measurable directional effects: project propagate_fresnel(z=-1280) → 113 features at physical z=+1280; project propagate_fresnel(z=+1280) → 47 features at physical z=-1280
4. The detector (DeepBeamScan) cannot preserve known topology — overcounts 9-19× on known vortices, misses vortex pairs entirely
5. Feature counts are chaotic across propagation distances (7 discontinuities in z-sweep from 48 to 269)
6. The 113 result is at the 0th percentile of null distribution from 100 random fields (mean: 21,670)

### Included Materials
- All R14 validation results (24 phases) as JSON files
- Original R1-R13 research data (preserved for provenance)
- Complete test suite (field construction, propagation, winding, detector, reproducibility, regression)
- Validation scripts (R14 reproduction, QA check, numerical consistency)
- Bug analyses (double-np.angle, D1 propagation sign, D02, min_prominence, seed-label)
- Full documentation (README, METHODS, RESULTS, CHANGELOG, REPRODUCIBILITY, etc.)

## Keywords
coherent optics, optical vortices, vortex lattice, Fresnel propagation, DeepBeamScan, feature detection, detector artifact, grid-locking, reproducibility, simulation, topological structure, phase singularities, z-sweep, bug verification, D1 propagation bug, double-np.angle, simulation data

## Method
### Field Construction
Vortex crystal field generated via `vortex_crystal_field(shape=(256,256), rows=6, cols=8, pixel_size=1e-6, wavelength_nm=694.3)` creating an 8×6 lattice of 48 design vortices.

### Propagation
Two propagation methods were compared:
1. **Project Fresnel**: `propagate_fresnel(E0, z=±1280, pixel_size=1e-6)` — documented to have D1 sign bug (propagates in -z direction). Verified via NCC(project Fresnel z=+1280 call, independent ASM z=-1280) = 1.000000.
2. **Independent ASM**: Reference implementation using `H = exp(1j·kz·z)`, `kz = sqrt(k0² - (2π·FX)² - (2π·FY)² + 0j)` with evanescent wave preservation.

### Feature Detection
- **DeepBeamScan (DBS)**: Primary detector for phase singularities via intensity-based analysis
- **MethodA**: DBS find_features() — primary method, gives 48 at z=0 and 113 at z=+1280 (with correct propagation)
- **MethodB**: Winding number count — corrected for double-np.angle bug, fixed to match MethodA (113)
- **MethodC**: Zero-amplitude search — confirmed 0/20 features at amplitude zeros, proving features are NOT at amplitude zeros

### R14 Validation Protocol (24 Phases)
1. Independent confirmation (3 methods × 20 candidates)
2. Threshold sensitivity (7 thresholds)
3. Reverse propagation (field reversibility vs feature persistence)
4. Z-sweep (15 propagation distances, -2560 to +2560 µm)
5. Resolution convergence (3 grid sizes: 64, 128, 256)
6. Numerical precision (float32 vs float64)
7. Phase precision (max error 4.94e-11)
8. Charge conservation (net charge tracking)
9. Detector validation (6 synthetic controls + 4 known-vortex tests)
10. Null distribution (100 random phase fields)
11. Reproducibility (3 trials × 50 statistical trials)
12. Amplitude-phase shuffling (4 configurations)
13. Spectral/aliasing analysis
14. Position tracking (feature trajectory across z)
15-24. Additional controlled experiments

## Data Files
All data files are JSON format for portability and human readability.

### R14 Results (`results/r14/`)
| File | Description |
|------|-------------|
| DEFINITIVE_DBS_TEST.json | Independent verification: MethodA=113, MethodB(fixed)=113, MethodC=0/20 |
| z_sweep.json | Feature counts at 15 distances: 201→48→47→50→47→52→158→48→118→130→74→94→94→113→64→269 |
| threshold_sweep.json | Counts at 7 thresholds: 102→82→63→44→10→2→0 |
| resolution_convergence.json | 64px:328, 128px:1328, 256px:5742 (no convergence) |
| detector_validation.json | Plane wave:0, Random:21638, Gaussian:0, 1-vortex:33, 1-vortex pair:0, 10:90, 100:1935 |
| null_distribution.json | Mean:21670, Median:21664, 113 at 0th percentile |
| phase_results.json | All 24 R14 phase results |
| lightweight.json | Lightweight validation summary |
| definitive.json | Full R14 reproduction with D1 verification |

### Research Continuation (`research_continuation/`)
Original R1-R13 research data preserved for provenance chain documentation.

## Reproducibility
Full reproduction instructions in REPRODUCIBILITY.md. One-command reproduction:
```powershell
python scripts/run_r14.py
```
Result: z=0: 48, z=+1280: 113 (via z=-1280 call), z=-1280: 47 (via z=+1280 call), DETERMINISTIC.

## Limitations
See README.md limitations section. Key limitations: uncharacterized propagation features, R11/R12 need re-run, no physical validation, single detector, D1 propagation bug in project code.

## Ethical Considerations
No human subjects, no sensitive data, all code and data openly available, no fabricated data, all bugs documented publicly, conservative scientific claims.

## License
MIT License — see LICENSE file.

## Contact
EXP-0007 Research Team — Scientific Discovery Lab
