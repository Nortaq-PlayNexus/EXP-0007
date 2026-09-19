# EXP-0007 — Code Index

## Source Code Structure

```
src/
├── propagation/                   # Propagation implementations
│   ├── angular_spectrum.py        # Reference ASM implementation
│   ├── fresnel.py                 # Project Fresnel (has D1 sign bug)
│   └── README.md                  # Propagation documentation
├── detection/                     # Feature detection
│   ├── deepbeamscan.py            # DBS detector (has D2 dead parameter)
│   ├── improved_detector.py       # Proposed improved detector (NEW)
│   ├── zero_amplitude_search.py   # Phase 1 of improved detector (NEW)
│   ├── subpixel_winding.py        # Phase 2 of improved detector (NEW)
│   └── README.md                  # Detector documentation
├── validation/                    # Validation scripts
│   ├── winding_count.py           # Winding number calculation
│   ├── validate_environment.py    # Environment validation
│   └── README.md                  # Validation documentation
├── analysis/                      # Analysis tools
│   ├── metrics.py                 # Radial power spectrum (has D5 bias)
│   ├── statistics.py              # Statistical analysis
│   └── README.md                  # Analysis documentation
└── visualization/                 # Visualization tools
    ├── figures.py                 # Figure generation
    └── README.md                  # Visualization documentation
```

## Script Index

```
scripts/
├── run_r14.py                     # One-command R14 reproduction
├── run_r14_lightweight.py         # Lightweight validation (~5 min)
├── validate_environment.py        # Environment validation
├── reproduce_figures.py           # Figure generation
├── generate_report.py             # Report generation
├── qa_check.py                    # QA check
├── numerical_consistency_check.py # Numerical consistency
└── README.md                      # Script documentation
```

## Test Index

```
tests/
├── test_field_construction.py     # ComplexField, lattice construction
├── test_propagation.py            # ASM, Fresnel, FFT, reversibility
├── test_winding.py                # Winding count, regression tests
├── test_detector.py               # DBS, controls, dead parameter
├── test_reproducibility.py        # Environment, data, reproducibility
├── test_regression.py             # Known bug regression tests
└── README.md                      # Test documentation
```

## Configuration

```
configs/
├── config.json                    # Experiment configuration (JSON)
├── experiment_config.json         # Experiment parameters (Python)
└── README.md                      # Configuration documentation
```

## Key Parameters

| Parameter | Value | Location |
|-----------|-------|----------|
| Grid shape | 256 × 256 | configs/config.json |
| Lattice rows | 6 | configs/config.json |
| Lattice cols | 8 | configs/config.json |
| Pixel size | 1.0 µm | configs/config.json |
| Wavelength | 694.3 nm | configs/config.json |
| Propagation z | 1280 µm | configs/config.json |
| Random seed | 42 | configs/config.json |
| Detector threshold | 0.5 | configs/config.json |
| min_prominence | 0.02 (DEAD) | configs/config.json |
