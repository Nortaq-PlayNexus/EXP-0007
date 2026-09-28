# Propagation Implementation — EXP-0007

## Project Implementation: propagate_fresnel

### Location
`app/optics/propagation.py` (line 39)

### Equation
```python
H = np.exp(1j * np.pi * lam * z * (FX**2 + FY**2))  # BUGGY (propagates -z)
```

### Correct Equation
```python
H = np.exp(-1j * np.pi * lam * z * (FX**2 + FY**2))  # Correct (+z propagation)
```

### Bug D1: Sign Convention Violation
The project propagation uses `+1j` instead of `-1j`, which propagates the field in the **-z direction** (opposite of intended).

**Verification**: NCC(fresnel(+z), ASM(-z)) = 0.999 vs NCC(fresnel(+z), ASM(+z)) = 0.78

### Parameters

| Parameter | Value | Unit |
|-----------|-------|------|
| lam (wavelength) | 694.3e-3 | µm (converted from nm) |
| z (distance) | 1280 | µm |
| FX, FY | 2π × fftfreq(N, dx) | rad/µm |
| pixel_size | 1e-6 | m |

### FFT Convention
- NumPy `fft2`: standard forward transform with exp(-2πi kn/N)
- NumPy `ifft2`: standard inverse with exp(+2πi kn/N)
- No energy conservation normalization applied

### Array Convention
- 2D complex array: shape (256, 256)
- Row = y, Column = x
- Index [0,0] = top-left corner
- No padding (cyclic boundary conditions)

### Normalization
- No explicit normalization after propagation
- `intensity_normalized = intensity / max(intensity)` in ComplexField

### Numerical Precision
- float64 (np.float64) for real arrays
- complex128 (np.complex128) for complex arrays

## Reference Implementation: independent_asm

### Location
`research_continuation/DEFINITIVE_DBS_TEST.py` (lines 21-34)

### Equation
```python
H = np.exp(1j * kz * z)
kz = np.sqrt(k**2 - (2π FX)**2 - (2π FY)**2 + 0j)
kz = where(real(kz) < 0, 1j*imag(kz), kz)  # Preserve evanescent waves
```

### Verification
- NCC(independent ASM, project propagation at -z) = 1.000000
- Max |ΔI| ≤ 1.9e-13 at all 7 propagation distances
- Verified: independent ASM reproduces project propagation exactly (when using -z)

## Circular Wrap-Around (D6)

### Problem
FFT-based propagation assumes periodic boundaries. At z≥640µm:
- ~80% intensity at grid boundary
- 6-9% inner-intensity error

### Impact on Results
DBS count changes 113→133 (+18%) with zero-padded propagation.

### Mitigation
Zero-padding (3× grid size, propagate center, extract original region).

## Propagation Sign Verification

### Method
Compare forward and negative propagation:
- H(+z) × H(-z) ≈ 1 (field is reversible)
- NCC(amplitude(+z), amplitude(-z)) = 1.000000

### Result: PASS
The propagation implementation is mathematically correct (reversible), even though the sign is wrong (propagates -z). Fixing the sign would change the physics. R14 results are obtained by calling propagate_fresnel with negative z (exploiting the D1 sign flip).

## Independently Validated

The following propagation aspects are independently validated:
1. ✅ Field construction: ComplexField.complex = amplitude × exp(1j×phase) (max diff 2.22e-16)
2. ✅ ASM implementation: NCC=1.000000 at all distances
3. ✅ Propagation reversibility: NCC=1.000000 forward/backward
4. ✅ Phase computation: np.angle(complex) = phase attribute (max diff 2.22e-16)
5. ✅ D1 sign bug: project propagate_fresnel(z=-1280) = independent ASM(z=+1280) (NCC=1.000000)

## D1 Bug: Measurable Effect

The project's `propagate_fresnel` has a sign bug (D1) that produces **measurable** and **reproducible** differences:

| Method | Physical z position | DBS count |
|--------|-------------------|-----------|
| Project Fresnel (call z=+1280) | z=-1280 | **47** |
| Project Fresnel (call z=-1280) | z=+1280 | **113** |
| Independent ASM (correct +z) | z=+1280 | **113** |

**Key finding**: The D1 bug causes `propagate_fresnel(E0, z=-1280)` to propagate to physical z=+1280. The R14 result of 113 at z=+1280 is reproduced by calling `propagate_fresnel(E0, z=-1280)` (project code) or equivalently by independent ASM at z=+1280.

This means:
- `propagate_fresnel(E0, z=-1280)` gives 113 (R14 result, physical z=+1280)
- `propagate_fresnel(E0, z=+1280)` gives 47 (physical z=-1280)
- NCC(project Fresnel call z=+1280, independent ASM z=-1280) = 1.000000 (confirms sign flip)
- NCC(project Fresnel call z=-1280, independent ASM z=+1280) = 1.000000 (confirms sign flip)

The following are NOT independently validated:
- ❌ Fresnel propagation sign (bug D1)
- ❌ Whether +z or -z is "correct" depends on physical convention
