# Mathematical Background — EXP-0007

## Complex Optical Field

The field is represented as:

**E(x,y) = A(x,y) × exp(iφ(x,y))**

Where:
- A = amplitude (|E|)
- φ = phase (in radians, wrapped to [-π, π])
- i = imaginary unit

Plain English: The field at each point has a strength (amplitude) and a wave position (phase). The complex representation combines both into one number.

## Vortex Definition

A vortex is a point where:
1. The phase winds around the point (non-trivial circulation)
2. Classically, the amplitude goes to zero at the core

The **winding number** (topological charge) counts how many times the phase winds:

**Q = (1/2π) × ∮ ∇φ · dl**

Plain English: Walk around the point in a circle. Count how many full phase cycles (2π) you pass through. That's the winding number.

For the lattice: 6 rows × 8 cols = **48 design vortex positions**.

## Phase Wrapping

Computers store phase in [-π, π]. When a phase difference crosses π, it "wraps" to -π:

- δ = 3.0 radians → no wrapping needed
- δ = 4.0 radians → wrapped to -2.28 radians (4.0 - 2π)

Plain English: Phase is circular, like a clock. Going past 360° wraps back to 0°.

## Phase Unwrapping

Phase unwrapping removes the 2π jumps to recover the continuous phase:

- `np.unwrap(phase)` — removes consecutive 2π jumps
- Important for detecting smooth phase changes
- The 773,912 change in Phase 8 needs independent audit

## Winding Number Calculation

### MethodA (DBS — correct for |δ| < π)
```
_dphi(a, b) = np.angle(np.exp(1j * (a - b)))
```
This computes the principal phase difference in (-π, π].

Plain English: "How much does the phase change between adjacent points?" Wrap to the shortest angle.

### MethodB (Independent — buggy double-wrap)
```
dphi(x, y) = np.mod(x - y + π, 2π) - π  # Correct formula
ph = np.angle(phase_2d)                   # BUG: redundant wrap!
```
When given a phase array, MethodB wraps AGAIN, creating a binary {0, π} map. This causes 127× overcounting on single vortices.

### Critical Difference at δ = π
- MethodA: δ=π → +π (positive)
- MethodB: δ=π → -π (negative)
- This 2π sign difference cascades through the curl calculation

## Amplitude and Intensity

- **Amplitude**: |E|, the magnitude of the complex field
- **Intensity**: |E|² / max(|E|²), normalized to [0, 1]
- **Vortex core**: Where amplitude → 0 (intensity → 0)

For DBS features: All 113 features at z=+1280 have intensity < 0.1 (median 0.0012).

## Propagation

### Angular Spectrum Method (ASM)
```
E_out = IFFT2[ FFT2[E_in] × H ]
H = exp(j × kz × z)
kz = sqrt(k² - kx² - ky² + 0j)
```

Plain English: Break the field into spatial frequencies, multiply by a propagation filter, and reconstruct.

### Fresnel Approximation
```
H = exp(±j × π × λ × z × (kx² + ky²))
```
Sign convention: `-j` for +z propagation (correct). Project code uses `+j` (bug D1).

Plain English: A simplified approximation valid when z >> aperture size.

## FFT Conventions

NumPy FFT uses the standard convention:
- Forward: `A[k] = Σ a[n] × exp(-2πi × kn/N)`
- Inverse: `a[n] = (1/N) × Σ A[k] × exp(+2πi × kn/N)`
- `fftfreq(N, d)` → spatial frequencies in cycles/unit

## Sampling

- Grid: 256 × 256 pixels
- Pixel pitch: dx = 1 µm
- Spatial frequency resolution: dkx = 2π/(N×dx)
- Nyquist frequency: k_Nyq = π/dx
- Maximum resolved frequency: k_max = π/(2dx)

Plain English: The grid can only resolve features larger than 2 pixels. Smaller features may be artifacts.

## Grid Dependence

The pixel grid introduces a reference frame. When the vortex lattice is aligned with the grid (0°, 90°), fewer features are detected (grid-locking). When misaligned (45°), more features appear.

Plain English: The digital grid itself creates artificial structure detection — like seeing shapes in aligned dots that disappear when you rotate them.

## Nyquist Limits

At z=+1280 µm:
- Feature size approaches sub-pixel scale
- Phase variations may exceed Nyquist sampling
- Grid-locking is a sampling artifact, not physics

## Resolution Convergence

A valid physical quantity should stabilize with increasing resolution. For DBS:
- 64×64: 328 features
- 128×128: 1,328 features
- 256×256: 5,742 features (R14 Phase 7, using R14 detector)

**Count increases with resolution** → NOT converging → artifact.
