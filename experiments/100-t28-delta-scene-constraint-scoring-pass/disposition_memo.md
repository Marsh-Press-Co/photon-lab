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

**Same-shift Phase-5 addition (Red Team's final audit, adopting MATERIALS' Phase-5 review in full).** This is not a fresh, unprecedented ambiguity: it is a named instance of R15's own Iteration-71/exp-094 addendum, which already covers a two-resolution-family disagreement on this exact `delta_scene` signal and already specifies the remedy -- "a third, differently-ratioed resolution point is the minimum required to distinguish [genuine convergence, a persistent recipe artifact, or a genuinely non-convergent oscillation]... before that point is trusted, the new family must additionally be shown to reproduce the ALREADY-KNOWN-CORRECT sign at a robust, far-from-null angle on the same channel" (LOGBOOK.md, R15 addendum). R3 (n=33, r=0.486) vs. R4 (n=35, r=0.110, the LARGER family) is exactly this shape, on the exact channel R15's addendum already names. The addendum explicitly rejects defaulting to either resolution as automatically correct -- "neither resolution's reading is individually trustworthy" is the standard, not "R3 is probably the artifact" or "R4, being denser, should govern." R5 (`cpl=50`) currently sits at n=4, a small bracket construction, nowhere near the ~30+-point density needed to serve as R15's own third point. The correctly-targeted next step is therefore a properly-powered, ground-truth-gated R5 census at R3/R4 density (not a fresh R3-family spend, which can only confirm what R3 already reads and cannot, per the addendum, distinguish a real effect from an R3-recipe-specific artifact on its own).

**Ceiling, stated once for future cycles (MATERIALS' Phase-5 finding).** Under NO branch of this memo's own per-outcome conditional does a genuine new realizability question ever open. Branch (i) is "no tier applies." Branch (ii), even in the strongest possible confirmed-coupling case, is "published, no new material or structure required" -- `delta_scene`'s own periodicity is either an inherited domain artifact or diffraction off the already-built, already-measured `graded_black_shell` geometry (PEC core, quintic-smoothstep graded absorptive coat, σ_abs/σ_ext=0.51, LOGBOOK ESTABLISHED). A future cycle that eventually resolves the R3/R4/R5 contradiction should not misread "coupling confirmed" as reopening a live plausible/unobtainium question -- it would only ever re-attribute an already-published structure's own diffraction, never certify a new one.

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
