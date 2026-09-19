# Future Experiments — EXP-0007

## Experiment Design Principles

1. Every experiment must have a clear question and predicted outcome
2. Every experiment must be reproducible from scratch
3. Every experiment must include controls
4. Every experiment must document failures, not just successes
5. No experiment should claim "vortex creation" without independent confirmation

## F1: Fix DBS Dead Parameter

### Question
What does DBS actually detect when intensity filtering is properly applied?

### Hypothesis
If min_prominence were functional, DBS would filter out non-vortex phase gradients and find a more accurate feature count.

### Method
1. Fix `find_features` to use `min_prominence` for intensity filtering
2. Run at z=0 and z=+1280
3. Compare with unmodified DBS
4. Test multiple thresholds: 0.001, 0.005, 0.01, 0.05, 0.1, 0.5

### Controls
- Unmodified DBS (baseline)
- Random field (should find ~0 features with filtering)
- Known vortex structures (should find correct count)

### Predicted Outcome
- Filtered DBS will find fewer features than unfiltered
- At z=+1280: may find 782 (with I<0.5) or fewer at stricter thresholds
- Random field: should find ~0 features
- Known vortices: should find 1, 4, etc.

### Significance
First publication-ready result: a detector calibration study showing that DBS overcounts without intensity filtering.

### Resources
- Code fix: ~2 hours
- Run time: ~30 minutes
- Analysis: ~2 hours

---

## F2: Characterize 65 Propagation Features (Time-Lapse)

### Question
Do the 65 features that appear at z=+1280 represent real propagation-generated structure?

### Hypothesis
If propagation creates vortices, features should:
(a) persist across propagation distances, (b) be stable at sub-pixel offsets, (c) appear gradually during propagation

### Method
1. Generate lattice field
2. Propagate to z = 0, 80, 160, 240, 320, 400, 480, 560, 640, 720, 800, 880, 960, 1040, 1120, 1200, 1280
3. At EACH z value, run at 3 sub-pixel offsets: (0,0), (1/3, 0), (0, 1/3)
4. Record: position, intensity, charge for every feature at every (z, offset)
5. Track: which features persist, which appear/disappear, which shift

### Controls
- Random field at same z values (should have no persistent features)
- Lattice at z=0 (baseline 48 features)
- Phase-shuffled lattice (should have ~21,608 features)

### Predicted Outcome (Artifact Hypothesis)
- Features will NOT persist consistently across sub-pixel offsets
- Features will appear/disappear irregularly
- Different offsets will give different counts at same z
- No gradual emergence pattern

### Predicted Outcome (Real Hypothesis)
- Features will persist across sub-pixel offsets
- Features will appear gradually during propagation
- Same features at different offsets (shifted slightly)
- Emergence pattern correlates with propagation physics

### Significance
This is the definitive test for propagation-generated structure. If features don't persist across sub-pixel offsets, they are grid-locking artifacts.

### Resources
- Code: ~4 hours (sub-pixel interpolation, tracking)
- Run time: ~2-4 hours (many z values × offsets × detectors)
- Analysis: ~4-8 hours (tracking, visualization)

---

## F3: D02 Method Audit

### Question
Does D02 use the buggy winding_count (double-np.angle)?

### Hypothesis
If D02 uses the project's find_features, it is unaffected by the bug. If D02 uses independent winding_count, its counts are inflated 64-152×.

### Method
1. Audit D02 measurement code in `research/next_phase/`
2. Identify which method computes D02 features
3. If winding_count is used, fix double-np.angle
4. If find_features is used, D02 is unaffected
5. Re-compute D02 at 256×256 with correct method

### Controls
- D02 at multiple grid sizes (64×64, 128×128, 256×256, 512×512)
- D01 (random) for comparison
- Known vortex structures for validation

### Predicted Outcome
- D02 likely uses find_features (no bug)
- D02 at 256×256: ~21,608 features (confirmed from existing data)
- Lattice/D02 = 113/21,608 = 0.0052

### Significance
Validates the 191× deficit and confirms grid-locking as the explanation.

### Resources
- Code audit: ~2 hours
- Re-computation: ~30 minutes
- Analysis: ~1 hour

---

## F4: Sub-pixel Grid Independence Test

### Question
Is the feature count grid-dependent?

### Hypothesis
If grid-locking is the mechanism, feature count should vary with pixel alignment. At sub-pixel offsets, the count should change.

### Method
1. Generate lattice field
2. Shift lattice by sub-pixel amounts: 0, 1/8, 1/4, 1/3, 1/2 pixels in x and y
3. Propagate to z=+1280 for each offset
4. Count features with DBS for each (z, offset) combination
5. Compare counts

### Controls
- z=0 at each offset (baseline)
- Random phase at each offset (should be similar)

### Predicted Outcome (Grid-Locking)
- At 0° offset: 113 features
- At 1/3 px offset: different count (more or fewer)
- At 1/4 px offset: different count
- Pattern of counts reveals grid-locking mechanism

### Predicted Outcome (Physical)
- Count should be stable across sub-pixel offsets (physical vortices don't care about pixel grid)

### Significance
Definitively demonstrates grid-locking if counts vary, or physical origin if they don't.

### Resources
- Code: ~3 hours (sub-pixel interpolation)
- Run time: ~1-2 hours
- Analysis: ~2 hours

---

## F5: Re-run R11/R12 with Fixed MethodB

### Question
What are the corrected absolute counts for R11 and R12?

### Hypothesis
Absolute counts are inflated 64-152×. Ratios may be preserved.

### Method
1. Fix winding_count in R11 and R12 scripts
2. Re-run both experiments
3. Compare with original results

### Controls
- Original results (preserved in archive/)
- Synthetic validation cases (1, 4 vortices)

### Predicted Outcome
- R11: corrected DBS count may differ from 6,558
- R12: corrected lattice/D02 ratio may differ
- Ratios should be approximately preserved

### Significance
Validates continuation experiment results and ensures all published numbers are correct.

### Resources
- Code fix: ~1 hour
- Run time: ~1 hour per experiment
- Analysis: ~2 hours

---

## F6: Improved Vortex Detector

### Question
Can we build a detector that correctly identifies vortex cores?

### Design Principles
1. Must find exactly 1 for a single vortex (not 33)
2. Must find exactly 2 for a vortex pair (not 0)
3. Must find exactly N for N known vortices (not overcount)
4. Must find 0 for random phase (not 21,638)
5. Must find 48 for the lattice at z=0 (matches design)

### Proposed Methods

#### Method 1: Zero-Amplitude Search
- Find points where |E| < threshold
- Check if these are surrounded by phase winding
- Advantage: True vortices have zero amplitude
- Disadvantage: Numerical noise near zero

#### Method 2: Sub-pixel Phase Winding
- Compute winding number at sub-pixel positions
- Use adaptive mesh refinement near high-curl regions
- Advantage: Not grid-locked
- Disadvantage: Computationally expensive

#### Method 3: Combined Approach
- Find zero-amplitude regions
- Verify phase winding at sub-pixel resolution
- Validate against known structures
- Advantage: Most rigorous
- Disadvantage: Most complex

### Validation Protocol
1. Synthetic cases: 1, 2, 4, 10, 100 known vortices
2. Lattice z=0: should find 48
3. Random phase: should find ~0
4. Propagated lattice: should find 48 or fewer (not 113)

### Significance
An improved detector could definitively resolve whether the 65 extra features are real.

### Resources
- Design: ~1 week
- Implementation: ~1-2 weeks
- Validation: ~1 week
- Publication-ready result

---

## Experiment Priority Order

| Priority | Experiment | Time | Impact |
|----------|-----------|------|--------|
| 1 | F1: Fix DBS parameter | 1 day | Detector calibration paper |
| 2 | F3: D02 audit | 1 day | Validates deficit |
| 3 | F5: Re-run R11/R12 | 2 days | Corrected counts |
| 4 | F4: Sub-pixel test | 3 days | Definitive grid-locking test |
| 5 | F2: Time-lapse | 1 week | Core question |
| 6 | F6: Improved detector | 3 weeks | Resolution |
