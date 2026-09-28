# Final Scientific Interpretation — EXP-0007

## Summary

EXP-0007 was designed to investigate whether coherent optical propagation generates novel topological vortex structures. After 24 R14 validation phases, 12-agent swarm audit, multiple bug discoveries, and comprehensive artifact analysis, the conclusion is:

> **No propagation-generated vortex creation was demonstrated.** The apparent 113-vortex population at z=+1280 is a reproducible but topologically meaningless artifact of detector behavior, pixel-grid alignment, and propagation/sampling methodology. The previously claimed 98.4% undercount was caused by a double-np.angle software bug (see docs/bug-history.md), not a real discrepancy.

## The Evidence Picture

### What We Can Trust (HIGH confidence)

1. **DBS finds 113 features at z=+1280** — This is a reproducible measurement of phase singularities. The count is deterministic (113/113/113) and independently verified (MethodA = fixed MethodB = 113).

2. **The lattice has 48 design vortices at z=0** — This is a designed/inherited property, not a measurement.

3. **Random fields produce ~191× more features than the lattice** — Random phase produces ~21,608 vs lattice 113 at 256×256. This is a robust finding across all detectors, grid sizes, and conditions.

4. **The 7,183 "independent" count was a software bug** — The double-np.angle bug in winding_count created a binary phase map that overcounts by 64-152×. Fixed MethodB = MethodA = 113.

5. **Six code defects exist (D1-D6)** — All confirmed by independent code inspection and testing.

6. **The detector cannot preserve known topology** — DBS overcounts single vortices by 33×, misses vortex pairs entirely, and overcounts 100-vortex structures by 19×.

### What We Should Question (MEDIUM confidence)

7. **113 features are phase singularities** — Methods A and B confirm phase winding, but MethodC found 0/20 at true amplitude zeros. These are rapid phase changes at nonzero amplitude, not true phase singularities in the strict mathematical sense.

8. **Orientation dependence is real** — 48 at 0° → 977 at 45° (8.65×). This is confirmed but at corrected scale. The question is whether this is grid-locking or physical.

9. **65 features appear during propagation** — 113 (z=+1280) minus 48 (z=0) = 65 extra features. These are reproducible but their nature is unknown.

### What We Should Reject

10. **98.4% undercount** — INVALID. Was comparing valid MethodA vs buggy MethodB. No discrepancy exists.

11. **7,183 independent winding count** — INVALID. Caused by double-np.angle bug.

12. **2.0× orientation dependence** — CORRECTED to 6.3× (113→977 at 45°).

13. **8× lattice/D02 deficit** — CORRECTED to 191× (113 vs 21,608 at 256×256).

14. **Propagation creates vortices** — CONTRADICTED by 24 R14 phases.

## The Unanswered Question

The most important unresolved question is: **Do the 65 features at z=+1280 represent real propagation-induced phase structure?**

The evidence strongly suggests they are artifacts:
- No position persistence across z
- Chaotic z-sweep (7 discontinuities)
- Below null distribution (0th percentile)
- Detector overcounts known topology
- Features disappear on reverse propagation
- No grid convergence

However, this conclusion relies on the current detector (DBS), which is known to overcount and grid-lock. An improved detector (proposed in docs/detector-improvement.md) could definitively resolve this.

## Evidence Level Assessment

| Claim | Level | Justification |
|-------|-------|---------------|
| DBS finds 113 at z=+1280 | Level 1 | Measurable, reproducible |
| Lattice has 48 design vortices | Level 1 | Designed/inherited |
| Random >> lattice | Level 1 | Measurable, reproducible |
| Orientation dependence 8.65× | Level 1 | Measurable, reproducible |
| No vortex creation | Level 1 | Supported by multiple independent tests |
| 65 propagation features are artifacts | Level 1-2 | Strong evidence but detector-dependent |
| DBS overcounts noise | Level 1 | Directly measured |
| DBS overcounts known topology | Level 1 | Directly measured |

No Level 3 (independent reproducibility by different groups) claims exist.

## Comparison to Original Claims

| Original Claim | Current Status | Confidence |
|---------------|----------------|------------|
| 113 vortices at z=+1280 | 113 phase variations, not vortices | HIGH |
| 98.4% undercount | No discrepancy exists | HIGH |
| Propagation creates structure | No creation demonstrated | HIGH |
| DBS is reliable | DBS overcounts 9-19× | HIGH |
| Pipeline is correct | Correct with bugs (D1-D6) | HIGH |
| 7,183 independent count | Software artifact | HIGH |
| Orientation 2.0× | Corrected to 8.65× | HIGH |
| Lattice/D02 = 8× | Corrected to 191× | HIGH |

## Recommended Citation

If this work is cited, the following should be stated:

> EXP-0007 investigated whether coherent optical propagation generates novel vortex structures. The study found no evidence of physical vortex creation. The apparent 113-vortex population at z=+1280 is a reproducible detector + grid-locking artifact. All data, code, and validation results are provided for full reproducibility.

## Path Forward

1. **Immediate**: Fix DBS dead parameter (docs/future-experiments.md F1)
2. **Short-term**: Sub-pixel grid independence test (F4)
3. **Medium-term**: Time-lapse propagation study (F2)
4. **Long-term**: Build improved detector (docs/detector-improvement.md)
5. **Definitive**: Run definitive vortex creation test (docs/definitive-test-proposal.md)
