# EXP-0007 Discussion Guide

## Appropriate Research Questions

This repository actively invites discussion and **falsification**. The following are appropriate topics:

### Detector Methodology
- Could DBS be redesigned to avoid grid-locking?
- What alternative vortex detection methods would be more reliable?
- How could min_prominence be properly implemented?
- Are there operating conditions where DBS gives accurate counts?

### Numerical Assumptions
- Is the Fresnel propagation sign bug physically meaningful?
- How do boundary conditions affect vortex detection?
- What resolution is needed for reliable vortex counting?
- Are phase unwrapping methods affecting results?

### Topology Interpretation
- Are any of the 113 features true topological singularities?
- Could MethodC (zero-search) detect real vortices?
- What is the difference between phase gradients and phase singularities?
- How many features would a "perfect" detector find?

### Propagation Methodology
- Does independent ASM propagation reveal different features?
- How does propagation sign affect vortex detection?
- Are there propagation distances where features are more reliable?

### Null Models
- Is the D02 matched-spectrum null appropriate?
- Could random field statistics be used as a baseline?
- What controls would definitively distinguish physics from artifacts?

## Encouraged Activities

1. **Falsification attempts**: Try to prove the 113 features ARE real
2. **Alternative detectors**: Implement different vortex counters
3. **Sensitivity analysis**: Vary ALL parameters systematically
4. **Cross-validation**: Use multiple independent methods
5. **Reproduction**: Run on different platforms, different versions
6. **Theoretical challenges**: Propose physical explanations
7. **Methodological critiques**: Question any assumption

## Not Appropriate

- Claiming vortex creation without independent confirmation
- Ignoring detector validation failures
- Selective reporting of positive results
- Removing negative results from the record

## Discussion Format

Open GitHub Issues using the appropriate template:
- Bug Report: for code issues
- Reproduction Failure: for failed reproductions
- Scientific Question: for research questions
- Methodology Issue: for methodological concerns
- Feature Request: for new experiments/analyses
