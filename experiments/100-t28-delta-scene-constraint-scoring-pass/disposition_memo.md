# exp-100 Tier 1 item 2 -- MATERIALS' disposition memo

Rescoped per-outcome conditional (Red Team Phase-2 mandatory fix 6,
NOTES.md). Decided by Tier 1 item 1's own pooled correlation result.

## Established, unchanged fact (cpl-is-inert)

`cpl` (the FDTD grid-density/numerical-resolution knob, `CPL={R3:30,R4:40,
R5:50}`) is confirmed purely numerical: `L_GEOMETRIC_M` is invariant to
1e-12 across R3/R4/R5 (Gate 3, every `R{n}` cycle since exp-094). This is
a resolution-knob fact, closed, and orthogonal to the question below.

## This cycle's own finding (delta_scene's realizability disposition)

Pooled dataset: 75 rows across 7 experiment directories
({'cpl20-native': 3, 'R3': 33, 'R4': 35, 'R5': 4}), r(delta_scene, frac_p_abs) = 0.2065,
permutation p = 0.0758 (20,000 trials), joint rule
(p<0.05 AND |r|>=0.2) on the pooled set: **NOT MET**.
Family-stratified contradiction (Idealization 70): **True**.
Overall outcome: **AMBIGUOUS**.

Branch (iii) -- ambiguous/underpowered (Idealization 70, pre-registered before this script ran). The pooled test (r=0.2065, p=0.0758, coupling_detected=False) is CONTRADICTED by at least one family-stratified result: {'R3': {'n': 33, 'r': 0.4862068708642141, 'p': 0.00415, 'coupling_detected': True}, 'R4': {'n': 35, 'r': 0.1102867253871392, 'p': 0.5249, 'coupling_detected': False}, 'R5': {'n': 4, 'r': 0.9010050941024483, 'p': 0.1644, 'coupling_detected': False}}. A real, general article-coupling effect should recur across families (R15's own addendum discipline); a family-specific-only signal is evidence for a family-specific recipe artifact, not genuine coupling. Disposition deferred -- no realizability claim made this cycle.

Per-family breakdown (a real cross-term should recur across families,
R15's own addendum discipline): {
  "R3": {
    "n": 33,
    "r": 0.4862068708642141,
    "p": 0.00415,
    "coupling_detected": true
  },
  "R4": {
    "n": 35,
    "r": 0.1102867253871392,
    "p": 0.5249,
    "coupling_detected": false
  },
  "R5": {
    "n": 4,
    "r": 0.9010050941024483,
    "p": 0.1644,
    "coupling_detected": false
  }
}
