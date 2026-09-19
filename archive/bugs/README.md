# Archive: Bug Artifacts

This directory contains artifacts related to discovered bugs.

## Contents

- `CRITICAL_BUG_REPORT.md` — Original bug report (double-np.angle in winding_count)
- Original buggy scripts (preserved from research_continuation/)

## Purpose

Documenting bugs transparently is essential for scientific credibility.

## Key Artifact

The double-np.angle bug in winding_count:
- Converted continuous phase to binary {0, π} map
- Caused 127× overcount on single vortices
- Invalidated all R13-based MethodB conclusions
- Corrected: fixed MethodB = MethodA = 113
