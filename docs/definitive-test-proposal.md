# Definitive Test Proposal — Can Propagation Create Vortices?

## The Core Question

Does coherent optical propagation from z=0 to z=+1280 µm create new topological vortex structures beyond the 48 design vortices present at z=0?

## Why This Is Hard to Answer

The current evidence suggests "No" but doesn't definitively prove it because:
1. The detector (DBS) has known artifacts
2. The 113 count at z=+1280 is reproducible but may be grid-locked
3. No alternative detector has been used
4. Sub-pixel grid independence has not been tested

## The Definitive Test

### Design Principle
A definitive test must use a grid-locking-immune detector and demonstrate feature persistence across propagation.

### Proposed Protocol

```
DEFINITIVE VORTEX CREATION TEST
=================================

STEP 1: BASELINE (z=0)
  For each sub-pixel offset (0, 1/4, 1/2, 3/4 px in x and y):
    a. Generate lattice field (48 design vortices)
    b. Run improved detector (zero-amplitude + sub-pixel winding)
    c. Record: confirmed vortex positions and counts
  Expected: ~48 vortices at ALL offsets (physical structure is grid-independent)

STEP 2: PROPAGATION (z=+1280)
  For each sub-pixel offset (0, 1/4, 1/2, 3/4 px in x and y):
    a. Propagate lattice to z=+1280
    b. Run improved detector
    c. Record: confirmed vortex positions and counts
  Expected: ~48 vortices at ALL offsets if no creation
  Expected: >48 vortices at SOME offsets if creation occurs

STEP 3: PERSISTENCE TEST
  Match vortices between z=0 and z=+1280 at each offset:
    a. Pair vortices by nearest-neighbor matching
    b. Count matched pairs (persistent)
    c. Count unmatched at z=+1280 (new)
    d. Count unmatched at z=0 (disappeared)
  Expected (no creation): 48 matched, 0 new, 0 disappeared
  Expected (creation): 48 matched, >0 new, 0 disappeared (or few disappeared)

STEP 4: REPRODUCIBILITY
  Repeat Steps 1-3 with different random seeds (42, 7, 123)
  Expected: Identical results (deterministic simulation)

STEP 5: CONTROL TESTS
  a. Random phase input: should produce 0 persistent vortices at any z
  b. Phase-shuffled lattice: should produce ~0 persistent vortices
  c. Plane wave: should produce 0 vortices

STEP 6: CROSS-VALIDATION
  Run same test with:
    a. DBS (current detector) — for comparison
    b. Angular spectrum propagation (independent from Fresnel)
    c. Fixed propagation sign (D1 correction)
  Compare results across methods

PASS CRITERIA
==============

PASS: 
  - Vortex count stable across sub-pixel offsets (±2)
  - All 48 z=0 vortices persist to z=+1280
  - 0-2 new vortices created (within noise)
  - Random phase produces 0 persistent vortices
  - Results identical across propagation methods

FAIL (Vortex Creation Confirmed):
  - >5 new persistent vortices at z=+1280
  - Vortex count varies significantly across sub-pixel offsets
  - New vortices persist across offsets
  - Random phase produces persistent vortices

INCONCLUSIVE:
  - Results between PASS and FAIL criteria
  - Requires improved detector or more data
```

### Why This Is Definitive

1. **Grid-locking immune**: Sub-pixel offsets break grid alignment
2. **Persistence tested**: Features tracked across propagation
3. **Multiple detectors**: DBS vs improved detector vs independent ASM
4. **Proper controls**: Random phase, phase-shuffled, plane wave
5. **Reproducible**: Multiple seeds, deterministic
6. **Cross-validated**: Multiple propagation methods

### Why Previous Experiments Don't Suffice

| Previous Test | Why It's Insufficient |
|---------------|----------------------|
| R14 Phase 1 (3 methods) | All used same grid, no sub-pixel |
| R14 Phase 3 (reverse) | Tracked counts, not positions |
| R14 Phase 4 (z-sweep) | Coarse z spacing, no sub-pixel |
| R14 Phase 7 (resolution) | Resolution ≠ grid independence |
| R14 Phase 21 (position) | Tracked few features, not all |

### Expected Result

Based on all existing evidence, the expected result is:
- **PASS (no creation)**: ~48 persistent vortices, 0-2 new, stable across offsets
- The 113 count from DBS is explained by grid-locking + overcounting
- The 65 "extra" features are grid-locked artifacts that disappear at sub-pixel offsets

### Resources Required
- Detector implementation: 2 weeks
- Test infrastructure: 1 week
- Run time: 1-2 days
- Analysis: 1 week
- Total: ~4 weeks

### Significance
This test would definitively answer the core question of EXP-0007 and settle the vortex creation debate. It is the highest-impact experiment that can be designed with current understanding.
