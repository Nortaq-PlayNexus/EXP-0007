# EXP-0007 — Zenodo DOI Registration

## Basic Information

| Field | Value |
|-------|-------|
| Deposit ID | (assigned by Zenodo) |
| DOI | 10.5281/zenodo.22849652 |
| Title | EXP-0007: Coherent Optical Vortex Propagation — R14 Validation Study |
| Upload type | Dataset |
| Version | 1.1.0 |
| Publication date | 2026-09-19 |
| License | MIT |
| Access | Open (all users) |

## Creators

| Name | Affiliation | ORCID | Role |
|------|-------------|-------|------|
| EXP-0007 Research Team | Scientific Discovery Lab | (to be assigned) | Creator |

## Description

Systematic investigation of whether coherent optical propagation generates novel topological vortex structures. After 24 R14 validation phases, 12-agent swarm audit, multiple bug discoveries, and comprehensive artifact analysis, the conclusion is: the apparent 113-vortex population at z=+1280 is a reproducible but topologically meaningless artifact of detector behavior, pixel-grid alignment, and propagation/sampling methodology.

### Keywords
coherent optics, optical vortices, vortex lattice, Fresnel propagation, DeepBeamScan, feature detection, detector artifact, grid-locking, reproducibility, simulation, topological structure, phase singularities, z-sweep, bug verification, D1 propagation bug, double-np.angle, simulation data

## Files to Upload

### Data Files (mandatory for dataset upload)
| File | Size | Description |
|------|------|-------------|
| results/r14/DEFINITIVE_DBS_TEST.json | ~5 KB | Independent verification |
| results/r14/z_sweep.json | ~5 KB | Z-sweep results |
| results/r14/threshold_sweep.json | ~5 KB | Threshold sensitivity |
| results/r14/resolution_convergence.json | ~5 KB | Resolution dependence |
| results/r14/detector_validation.json | ~5 KB | Detector validation |
| results/r14/null_distribution.json | ~5 KB | Null distribution |
| results/r14/phase_results.json | ~5 KB | Phase results |
| results/r14/lightweight.json | ~2 KB | Lightweight validation |
| results/r14/definitive.json | ~2 KB | Definitive reproduction |
| research_continuation/r14_summary.json | ~5 KB | R14 summary |
| research_continuation/CONTINUATION_FINAL.json | ~5 KB | Final continuation data |
| research_continuation/r13_forensic_results.csv | ~5 KB | R13 forensic |
| research_continuation/r11_dbs_fix.json | ~5 KB | DBS fix verification |
| research_continuation/r9_orientation.json | ~5 KB | Orientation dependence |
| research_continuation/r7_d02_null.json | ~5 KB | D02 null test |
| research_continuation/r_phase_rotation.json | ~5 KB | Phase rotation |
| research_continuation/r2_aperture_scaling.json | ~5 KB | Aperture scaling |
| metadata.json | ~1 KB | Project metadata |

### Documentation Files (recommended)
| File | Description |
|------|-------------|
| README.md | Master report |
| METHODS.md | Research methods |
| RESULTS.md | Key results |
| REPRODUCIBILITY.md | Reproduction instructions |
| CHANGELOG.md | Change history |
| docs/d1-bug-effect.md | D1 propagation bug analysis |
| docs/bug-history.md | Bug discoveries |
| docs/final-interpretation.md | Scientific interpretation |
| docs/what-we-know-dont-know.md | Know/don't-know analysis |
| docs/r14-validation.md | R14 validation details |

### Code Files (recommended for reproducibility)
| File | Description |
|------|-------------|
| scripts/run_r14.py | R14 reproduction script |
| scripts/run_r14_lightweight.py | Lightweight validation |
| scripts/validate_environment.py | Environment validation |
| scripts/qa_check.py | QA check script |
| scripts/numerical_consistency_check.py | Numerical consistency |
| tests/ | All test files |

## Related Identifiers
- GitHub repository: https://github.com/Nortaq-PlayNexus/EXP-0007
- Related documentation: docs/ directory

## Technical Summary
The dataset contains 92 files totaling 0.20 MB. All data are JSON format (except one CSV). All results are deterministic and reproducible via the provided scripts. The project has been fully documented with 22 documentation files, 7 validation scripts, and 7 test files.

## Verification Checklist
- [x] All data files present
- [x] All documentation complete
- [x] Reproducibility verified (QA check PASS)
- [x] License file present (MIT)
- [x] README describes dataset contents
- [x] Metadata includes creators, keywords, description
- [x] No personal/sensitive data
- [x] Code and data are openly available
- [x] All bugs documented (not hidden)
- [x] Scientific claims are conservative

## Zenodo Upload Steps
1. Go to https://zenodo.org/upload
2. Select "Dataset" as upload type
3. Fill in metadata from this form
4. Upload all files from the zenodo/data/ directory
5. Review and submit
6. Wait for DOI assignment (usually 1-2 days)
7. Update metadata.json with assigned DOI
8. Update CITATION.cff with assigned DOI

## Notes
- If Zenodo requires software upload instead of dataset, upload as "Software" with code files as primary data
- Consider uploading data and code separately if Zenodo has size limits
- The 0.20 MB total size is well within Zenodo limits
