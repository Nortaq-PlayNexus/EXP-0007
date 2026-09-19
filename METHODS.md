# Methods — EXP-0007

## Experimental Design

### Field Generation

A vortex crystal field is generated with the following parameters:

- **Grid**: 256 × 256 pixels
- **Vortex lattice**: 6 rows × 8 columns = 48 design vortex positions
- **Pixel size**: 1 µm (= 1e-6 m)
- **Wavelength**: λ = 694.3 nm (red laser)
- **Pixel pitch**: 32 µm (x), 42.67 µm (y)

### Propagation

Two propagation methods are used:

1. **Angular Spectrum Method (ASM)** — Reference implementation
   - `H(kx,ky,z) = exp(j × kz × z)` where `kz = sqrt(k² - kx² - ky²)`
   - Verified: NCC(independent ASM, project propagation) = 1.000000 at all 7 distances

2. **Fresnel Propagation** — Project implementation (contains sign bug D1)
   - Intended: `H = exp(-1j * π * λ * z * (kx² + ky²))`
   - Actual: `H = exp(+1j * π * λ * z * (kx² + ky²))` (propagates -z)
   - NCC(fresnel(+z), ASM(-z)) = 0.999; NCC(fresnel(+z), ASM(+z)) = 0.78

### Detector: DeepBeamScan (DBS)

DBS uses winding-number phase topology to identify features:

1. Compute phase differences across 2×2 plaquettes
2. Calculate curl from plaquette contributions
3. Quantize charge: `Q = round(curl / 2π)`
4. Count features where `|Q| > 0.5`

**Known defect**: `find_features` declares `min_prominence=0.02` but never uses it (D2).

### Independent Winding Method (MethodB)

Uses `np.mod(x-y+π, 2π)-π` for phase differences instead of `np.angle(exp(1j*δ))`.

**Critical bug**: When given a phase array, `winding_count` applies `np.angle()` again (double-wrap), creating a binary {0, π} phase map that overcounts by 127× for single vortices.

### Validation Methods

- **MethodA**: DBS `find_features` — validated on synthetic 1-vortex (→1), 4-vortex (→4) cases
- **MethodB**: `winding_count` with fixed code (no double-wrap) — validated identically to MethodA
- **MethodC**: Zero-amplitude search — expects features at amplitude nulls for true vortices
- **Independent ASM**: From-scratch numpy implementation, NCC=1.000000

## Statistical Framework

### Controls (26-control matrix)

- **C07/D01**: Random-input generation-of-order (completeness)
- **C11/D02**: Exact matched-spectrum surrogate (primary decisive test)
- **C23**: Pitch positive controls (detector calibration)
- **C03**: Grid refinement (numerical artifact test)

### Evidence Levels

- **Level 1**: Quantitatively measurable structure, designed and inherited
- **Level 2**: Specific physical mechanism, testable and confirmed
- **Level 3**: Generic physical signature, reproducible by independent means

All EXP-0007 claims are Level 1. No Level 2 or Level 3 claims are supportable.
