# Phase 2 Critique — ELECTROMAGNETISM

**Cycle:** exp-076, Iteration 53 (G40/PAD decorrelation). **Seat:** ELECTROMAGNETISM (blind, independent — no other seat's Phase-2 output read).

## Steel-man

G40 is a well-posed, single-variable instrument change. Verified directly against `design_geometry_output.txt` §1: G40 is bit-identical to C80 in `NX`, `NY`, `SRC_X`, `PLANE_X`, `OBJ_Y`, `y_lo`, `y_hi`, `A=752`, `aperture_cells=1504`, and — critically for causality — `D_SP=223`, the direct source→plane path length. Only `ABSORB` (40 vs 80) differs, so first-arrival timing at the plane is provably unaffected by the ABSORB/PAD split. The originally-proposed dynamic causal-identity gate (my own prior catch, exp-065 §4) was correctly retired — its `n=247<319` void is geometry-general, not something this cycle re-litigates — and its replacement, `static_construction_identity` (§4b, `max_diff=0.0e0` across `damp_e`/`damp_hx` at all three scored windows), is accurately re-cited, not overstated. Reusing exp-069's exact `block_dense` grid, `STEPS`, and scoring formula keeps the new points commensurable with the committed baseline without inventing a new convention mid-thread.

## Sharpest attack

`STEPS=2800`'s settling status rests on exactly two independently-tested geometries, and both confound the two variables this cycle exists to split: C40 (thin, more-reflective `ABSORB=40` boundary, at the SMALL `NY=1584` domain — short boundary round-trip) and C80 (thick, well-graded `ABSORB=80` boundary, at the LARGE `NY=1664` domain — long round-trip but strong per-bounce loss). `G40` is the untested third cell: C40's thin, leakier boundary sitting at C80's larger domain — its own clearances (`clear_plane` 37→77, `clear_src` 20→60) show there is *more* vacuum between the weak boundary and the scored window than either settling anchor ever had. A leakier reflector with a longer transit time before its echo re-crosses the window is exactly the combination most likely to need more, not the same, ring-down time — and it's the one combination neither exp-066's C40 test nor exp-069's Block-SETTLE C80 test (STEPS=2800 vs 4200, C80 only) actually probed. The two G40-specific checks in this proposal — the causal-arrival-step gate and `static_construction_identity` — are both *static*, zero-or-one-timestep checks; neither measures dynamic ring-down. No Block-SETTLE-style STEPS=2800-vs-4200 leg on G40 itself is in the 31-call budget.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to plain support

Add a 2-call G40 settling-stress leg (STEPS=2800 vs STEPS=4200 at θ=39°/40°, mirroring exp-069's own `block_settle` construction on C80) inside this cycle's own budget, gated the same way — before `amp_ratio(PAIR_PAD)`/`amp_ratio(PAIR_ABSORB40)` are read as decision-grade against §4's pre-registered bands. At <10% marginal FDTD cost this closes the one load-bearing gap the causal/settling bookkeeping actually has; everything else in the construction checks out.
