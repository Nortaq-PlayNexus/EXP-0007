# Bug History — EXP-0007

## CRITICAL: Double-np.angle in winding_count

**Severity**: CRITICAL — Invalidated all R13-based MethodB conclusions
**Status**: VERIFIED AND CONFIRMED

### What the Bug Was

The `winding_count` function took a **phase array** (values in [-π, π]) and applied `np.angle()` to it. Since `np.angle()` of a real number gives 0 (for positive) or π (for negative), this converts the continuous phase into a **binary map {0, π}**.

### Where It Occurred

- `research_continuation/DEFINITIVE_DBS_TEST.py` line 36
- `research_continuation/r13_forensic_experiment.py` line 35
- `research_continuation/r13_validation.py` line 80
- `research_continuation/r13_validation2.py` line 9
- `research_continuation/exp_phase3.py` line 188
- `research_continuation/exp_continuation.py` line 149
- `research_continuation/r13_verify_all.py` line 17 (different pattern)

### How It Affected Earlier Results

| Synthetic case | Expected | Buggy MethodB | Correct MethodB | Overcount |
|---|---|---|---|---|
| 1 vortex | 1 | 127 | 1 | 127× |
| 4 vortices | 4 | 609 | 4 | 152× |
| Lattice z=0 | N/A | 4,612 | 48 | 96× |
| Lattice z=1280 | N/A | 7,183 | 113 | 64× |

The 7,183 "independent" winding count was entirely caused by this bug. The TRUE independent count equals DBS: **113 = 113**.

> **NOTE**: The 98.4% undercount claim referenced in earlier R13 reports is INVALID — it was based on comparing valid MethodA results against buggy MethodB results. With the bug fixed, both methods give 113 = 113. See [FINAL_CORRECTED_REPORT.md](../archive/historical-results/FINAL_CORRECTED_REPORT.md) for details.

### How It Was Corrected

```python
# BUGGY
def winding_count(phase_2d):
    ph = np.angle(phase_2d)  # Double-wrap!

# FIXED
def winding_count(phase_2d):
    ph = phase_2d.astype(np.float64)  # Use phase directly
```

### Which Experiments Were Re-Run

- R13 forensic reproduction (all phases re-verified)
- R9 orientation dependence (corrected from 2.0× to 6.3×)
- R11 DBS fix verification (7,844→6,558 was inflated)
- R12 EXP-3 null (counts re-evaluated)
- All R1-R12 continuation experiments (absolute counts inflated)

### Which Conclusions Changed

1. **98.4% undercount claim** → INVALID (no discrepancy exists)
2. **R9 magnitude** → Corrected from 7,844→15,598 (2.0×) to 113→977 (8.65×)
3. **R11 95 count** → Corrected to 113 (MethodA verified)
4. **R7 D02 deficit** → Corrected from 8× to 191×
5. **All MethodB absolute counts** → Inflated 64-152× (ratios may be valid)

### Verification

Fixed MethodB = MethodA for all synthetic cases:
- 1 vortex: 1 = 1 ✓
- 4 vortices: 4 = 4 ✓
- Flat phase: 0 = 0 ✓
- Lattice z=0: 48 = 48 ✓
- Lattice z=1280: 113 = 113 ✓

## HIGH: find_features Dead Parameter (D2)

### Original Behavior
`def find_features(self, field, min_prominence=0.02)` — parameter declared but never used.

### Why It Mattered
Cannot distinguish true optical vortices (intensity nulls) from arbitrary phase gradients. Random fields produce 21,353+ features.

### Correction
The parameter should be used for intensity filtering. When manually applied (I < 0.5), DBS changes from 113→782 (ADDS features, not removes).

### Validation
- Only 1 occurrence of 'min_prominence' in entire deep_scan.py (signature only)
- Confirmed by code inspection and testing (R11)

### Resulting Detector Behavior
DBS overcounts random noise. At z=+1280, DBS finds 113 features for the lattice but would find 782 with intensity filtering — the "dead parameter" actually causes undercounting relative to its designed behavior.

## HIGH: propagate_fresnel Sign Bug (D1)

### Original Behavior
```python
H = np.exp(1j * np.pi * lam * z * (FX**2 + FY**2))  # +1j → propagates -z
```

### Why It Mattered
Propagates in the wrong direction (-z instead of +z). Changes phase structure of propagated field.

### Correction
```python
H = np.exp(-1j * np.pi * lam * z * (FX**2 + FY**2))  # -1j → propagates +z
```

### Validation
NCC(fresnel(+z), ASM(-z)) = 0.999 confirms propagation is in -z direction.

### Resulting Detector Behavior
DBS count changes 113→150 (+33%). MethodB count changes 7,183→4,067 (-43%). Minor contributor to discrepancy (150 vs 4,067 still differ 27×).

## MEDIUM: Circular Wrap-Around (D6)

### Original Behavior
FFT-based propagation with cyclic convolution. 256×256 aperture has ~80% intensity at boundary.

### Why It Mattered
At z≥640µm, boundary wrap-around creates 6-9% inner-intensity error.

### Correction
Zero-padded propagation (3× padding).

### Validation
DBS changes 113→133 (+18%).

### Resulting Detector Behavior
Minor change to DBS count. MethodB more affected (7,183→5,192).

## MEDIUM: Independent ASM Normalization (D4)

### Original Behavior
R-S convolution with z-dependent normalization mismatch (7.24x at z=40µm).

### Why It Mattered
Cannot validate ASM results at short distances.

### Correction
Normalize R-S convolution consistently across distances.

### Validation
No effect on R13 pipeline. Affects cross-validation methodology only.

## MEDIUM: Radial Power Spectrum Bias (D5)

### Original Behavior
Azimuthal averaging over full 2π mixes distinct reciprocal lattice peaks.

### Why It Mattered
"41.66 c/mm" is a blend artifact; true peak is 31.25 c/mm.

### Correction
Separate analysis of individual lattice peaks.

### Validation
No effect on R13 pipeline. Affects spectral analysis only.

## LOW: lattice Params Constant Guard

### Original Behavior
`guard = 8` declared; `crossing = np.where(profile[8:] > 0.15)` hardcodes 8.

### Why It Mattered
Code smell — guard declared but index hardcoded to same value.

### Correction
Use `guard` variable instead of hardcoded 8.

### Validation
No functional change (guard=8 is correct). Affects spacing reports only.

## Data Management Bug: Seed Label Swap

### Original Behavior
- `exp2b_D02_42.jsonl` contains seed=7 data
- `exp2b_D02_7.jsonl` contains seed=42 data

### Correction
Swap file labels to match code-level seed usage.

### Impact
Data management issue. Code-level seed usage is correct.
