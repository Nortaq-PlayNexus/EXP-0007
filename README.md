# EXP-0007 — Coherent Optical Vortex Propagation Study

> **Research status: R14 validation completed. The original apparent vortex-creation observation was not validated as physical vortex creation. Controlled experiments indicate detector, grid, and propagation-method artifacts.**

---

![Research Status](https://img.shields.io/badge/Research%20Status-R14%20Complete-blue)
![Reproducibility](https://img.shields.io/badge/Reproducibility-Verified-brightgreen)
![Python](https://img.shields.io/badge/Python-3.14+-blue)
![License](https://img.shields.io/badge/License-MIT-blue)
![DOI](https://img.shields.io/badge/DOI-Placeholder-orange)
![CI](https://github.com/placeholder/EXP-0007/workflows/CI/badge.svg?branch=main)](https://github.com/placeholder/EXP-0007)

---

## What is EXP-0007?

EXP-0007 is a systematic investigation of whether coherent optical propagation generates novel topological structure (vortices). The study used a 256×256 pixel simulation of a laser beam containing an 8×6 vortex lattice (48 design vortices), propagated it to z=+1280 µm, and measured feature counts using the DeepBeamScan (DBS) detector.

## What question was being investigated?

**Primary question:** Does propagation through free space create new vortex features beyond the 48 design vortices present at z=0?

**Initial observation:** At z=+1280, DBS detected 113 features (vs 48 at z=0), a +135% increase. A separate winding-number method (MethodB) reported 7,183 features — leading to a claimed 98.4% undercount by DBS.

## What was initially observed?

| Plane | DBS (MethodA) | Independent Winding (MethodB) | Reported Excess |
|-------|--------------|-------------------------------|-----------------|
| z=0 | 48 | 4,612 | — |
| z=+1280 (D1 flip) | 113 | 7,183 ✗ | Reproduced via z=-1280 call; 98.4% undercount was bug |
| z=-1280 (D1 flip) | 47 | — | Project Fresnel at z=+1280 gives 47 (D1 sign bug) |
| NCC verification | 1.000000 | — | Project Fresnel(+1280 call) = ASM(-1280) |

## What did R14 test?

R14 executed 24 validation phases to determine whether the 113-vortex result represents genuine topological creation:

1. **Independent confirmation** (3 methods on 20 candidates)
2. **Threshold sensitivity** (7 thresholds)
3. **Reverse propagation** (field reversibility vs feature persistence)
4. **Z-sweep** (15 propagation distances)
5. **Resolution convergence** (3 grid sizes)
6. **Numerical precision** (float32 vs float64)
7. **Charge conservation** (net charge tracking)
8. **Detector validation** (6 synthetic controls + 4 known-vortex tests)
9. **Null distribution** (100 random fields)
10. **Reproducibility** (3 trials × 50 statistical trials)
11. **Amplitude-phase shuffling** (4 configurations)
12. **Spectral/aliasing analysis**
13. **Position tracking** (feature trajectory across z)
14. **Propagation sign test**
15. **Method comparison** (MethodA vs MethodB vs MethodC)
16-24. Additional controlled experiments

## What did R14 establish?

The 113 candidates are **real phase singularities** in the propagated field, but they are:

- **NOT the same structure** as the 48 design vortices (0 position overlap)
- **Highly threshold-dependent** (count varies 0→102 across thresholds)
- **NOT at amplitude zeros** (true vortices require zero core amplitude; MethodC confirmed 0/20)
- **Unstable across propagation** (48→158→48→118→130→74→94→113 across z-sweep)
- **Produced by a detector that cannot preserve known topology** (1→33, 10→90, 100→1,935 overcount)
- **Not resolution-convergent** (328→1,328→5,742 as resolution increases)
- **Below 0th percentile** of random field null distribution (random→21,670)

**Conclusion: The 113-vortex result is a systematic detector + grid-locking artifact, not physical vortex creation.**

## What did it NOT establish?

- No propagation-generated topological creation was demonstrated
- No feature persistence across propagation distances was confirmed
- No physical mechanism for vortex creation was identified
- The 65 features appearing during propagation (z=0→z=1280) are uncharacterized (likely artifacts)
- Whether DBS defects (D1-D6) affect D02 measurements remains unresolved

## Can someone reproduce it?

Yes. See [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for exact instructions.

**One-command reproduction:**
```bash
python scripts/run_r14.py
```

**Lightweight validation (5 minutes):**
```bash
python scripts/validate_environment.py && python scripts/run_r14.py --lightweight
```

## Where is the data?

| Type | Location |
|------|----------|
| Raw data | `data/raw/` |
| Processed data | `data/processed/` |
| Validation data | `data/validation/` |
| R14 results | `results/r14/` |
| Raw research data (preserved) | `research_continuation/` |
| Archive (superseded/defects) | `archive/` |

## Where is the code?

| Type | Location |
|------|----------|
| Propagation implementation | `src/propagation/` |
| Detector implementation | `src/detection/` |
| Validation scripts | `src/validation/` |
| Analysis tools | `src/analysis/` |
| Visualization | `src/visualization/` |
| One-command scripts | `scripts/` |
| Configurations | `configs/` |
| Tests | `tests/` |

## What is the current conclusion?

> The apparent 113-vortex population at z=+1280 is not supported as physical vortex creation. The observed feature population is reproducibly associated with detector behavior, grid dependence, and propagation/sampling methodology.

Evidence level: **Level 1** (quantitatively measurable structure, designed and inherited). No Level 2 or Level 3 claims are supportable.

---

## Research Pipeline

```
INITIAL FIELD
↓
PROPAGATION
↓
FEATURE DETECTION
↓
APPARENT VORTICES
↓
INDEPENDENT VALIDATION
↓
R14 CONTROLS
↓
ARTIFACT IDENTIFICATION
↓
FINAL INTERPRETATION
```

---

## Quick Links

- [Scientific Abstract](#scientific-abstract)
- [The 113-Vortex Result](#the-113-vortex-result)
- [R14 Validation Study](docs/r14-validation.md)
- [What We Know / Don't Know](docs/what-we-know-dont-know.md)
- [Propagation Features Analysis](docs/propagation-features-analysis.md)
- [Bug History](docs/bug-history.md)
- [D1 Propagation Bug](docs/d1-bug-effect.md)
- [Final Scientific Interpretation](docs/final-interpretation.md)
- [Future Experiments](docs/future-experiments.md)
- [Detector Improvement Proposal](docs/detector-improvement.md)
- [Definitive Test Proposal](docs/definitive-test-proposal.md)
- [Mathematical Methods](docs/mathematical-background.md)
- [Propagation Implementation](docs/propagation-implementation.md)
- [Detector Documentation](docs/detector-analysis.md)
- [Methods](docs/methodology.md)
- [Limitations](docs/limitations.md)
- [FAQ](docs/faq.md)
- [Research Timeline](docs/research-timeline.md)
- [Data Provenance](docs/data-provenance.md)
- [REPRODUCIBILITY.md](REPRODUCIBILITY.md)
- [METHODS.md](METHODS.md)
- [RESULTS.md](RESULTS.md)
- [CHANGELOG.md](CHANGELOG.md)

---

*This repository is designed so that a skeptical researcher can clone it and say: "I don't have to trust the author. I can reproduce the experiment and inspect the evidence myself."*
