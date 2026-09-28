# FAQ — EXP-0007

## General

### What is EXP-0007?
EXP-0007 is a systematic investigation of whether coherent optical propagation generates new vortex topological structures. The study found **no evidence** of physical vortex creation.

### What was the original claim?
The original claim was that propagation from z=0 to z=+1280 µm creates new vortices: 48 at z=0 → 113 at z=+1280 (+135%).

### What is the current conclusion?
The 113-vortex result at z=+1280 is a systematic detector + grid-locking artifact, not physical vortex creation.

### Why is this important?
It demonstrates the critical importance of:
- Detector validation with synthetic controls
- Resolution convergence testing
- Null distribution analysis
- Independent reproducibility

## Scientific

### Are there really 113 vortices at z=+1280?
DBS detects 113 phase singularities at z=+1280. Whether these represent "real" vortices (topological structures) depends on definition. They are phase variations, but NOT true phase singularities (MethodC confirmed 0/20 at amplitude zeros).

### Why does DBS give 113 but random fields give 21,670?
DBS detects phase gradients, not just true vortices. Random phase has many gradients. The lattice's specific phase pattern suppresses detection from 21,608 (shuffled) to 113 (original).

### Is the propagation implementation correct?
The ASM reference implementation is verified (NCC=1.000000). The Fresnel implementation has a sign bug (D1) but is reversible. The propagation itself is NOT the cause of the 113-vortex anomaly.

### What is the double-np.angle bug?
The `winding_count` function applies `np.angle()` to a phase array that already contains phase values. This binary-wraps the phase, creating a {0, π} map that generates thousands of false windings. Fixed MethodB = MethodA = 113.

### Why does orientation matter?
The pixel grid creates a reference frame. When the lattice is aligned (0°, 90°), the detector finds fewer features (grid-locking). When misaligned (45°), it finds more (8.65× range). This is a sampling artifact.

### What does "resolution convergence" mean?
A valid physical measurement should stabilize at higher resolution. If counts keep increasing, they're likely numerical artifacts. DBS counts increase from 328→1,328→5,742 with resolution.

## Reproduction

### Can I reproduce this?
Yes! See REPRODUCIBILITY.md for exact instructions.

### What do I need?
- Python ≥3.10
- NumPy, SciPy, Matplotlib
- See requirements.txt

### How long does it take?
Full R14: ~30 minutes. Lightweight validation: ~5 minutes.

### Does it work on Linux/macOS?
Yes, the instructions cover both platforms.

## Data

### Where is the raw data?
`data/raw/` (structured), `research_continuation/` (preserved from original research).

### Are the data reproducible?
Yes — deterministic simulation. Same inputs always produce same outputs.

### What about the seed swap?
The data files exp2b_D02_42.jsonl and exp2b_D02_7.jsonl have swapped seed labels. Code-level seed usage is correct; file labeling needs correction.

## Future

### Will you test with a physical laser?
Not planned — this is a simulation study. Physical validation would require significant additional resources.

### What's next?
1. Fix DBS dead parameter
2. Characterize 65 propagation features
3. Re-run with corrected MethodB
4. Publish grid-locking characterization
