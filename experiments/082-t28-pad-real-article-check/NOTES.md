# exp-082 — The PAD-loaded real-article check (T28, Iteration 59)

**Panel Iteration 59.** Lead: **QUANTUM OPTICS** (by rotation). Phase 1
only in this document at time of writing — Phase 2 (blind critique), Phase
3 (Director synthesis), Phase 4 (any corrected re-run), and Phase 5 (blind
review + Red Team final audit) have not yet run. This NOTES.md records
Phase 1's own hypothesis/setup/result/learned/next; the Director's Phase 3
synthesis supersedes it in force where the two differ, per this program's
own standing convention (see `experiments/081-.../NOTES.md`'s own
Phase-3-supersedes-Phase-1 structure for the precedent).

## Hypothesis

PLAN.md's Iteration-59 queue Tier 2 item 7 (deferred SIX consecutive T28
cycles, 076–081; a seventh deferral without an explicit stated reason fires
Checkpoint criterion 4 outright, per the standing tripwire). Route (a)
taken: build and run it as this cycle's own primary item — see
`phase1_proposal.md` §0 for the full reasoning.

Does the empty-scene `PAD`-sensitivity axis (`PAIR_PAD≡(C40,G40)`,
Iteration 53's own dominant finding) survive into the REAL, article-loaded
Weber-contrast channel (`C`, computed via `lab/ambient.py::
contrast_from_runs`, exactly as every constraint-3 citation this program
has ever issued is scored), or does it cancel in the object-window-vs-
flank-window subtraction real scoring performs?

## Setup

`dg065.CONFIGS["C40"]`/`["G40"]` (`PAIR_PAD`), the established flagship
absorber (`materials.pec_disk` + `materials.graded_black_shell`, bit-
identical to `experiments/024-.../run.py::build("absorber")`) loaded at
each config's own `(obj_x, obj_y)`, radius `R_OUT=78`. 7 angles
θ∈{36°,...,42°} (1° step, exact grid points of the established 31-point
dense sweep), 600nm, STEPS=2800 (T28's own established settled value for
this geometry). 28 main FDTD calls (2 configs × 7 angles × {empty, scene}
legs) + 1 settling-precondition call. Full parameter table, pre-registered
falsifiable SURVIVES/CANCELS/INCONCLUSIVE bands, T1 disposition (N/A),
R6/new-machinery dispositions: `phase1_proposal.md` §1–5.

## Result

**Reproduction precondition PASSED, bit-exact** (`max_dev=0.0` vs
`experiments/076-.../results.json::headline` at all 7 shared angles) —
this cycle's own new harness verified correct before the new leg is
trusted.

**Primary metric: `ratio = A_scene/A_empty = 0.6573`. VERDICT: SURVIVES**
(pre-registered band `[0.5,2.0]`) — the PAD-sensitivity confound reaches
the real, article-loaded channel at roughly two-thirds the amplitude of its
empty-scene reading, decisively inside the SURVIVES band, not near either
boundary.

**Secondary (disclosed): `A_scene/C_thr = 0.6815`** — 68% of VISION's
frozen photopic lab bar on this one 7-point/`PAIR_PAD` instance; roughly
5.5× larger relative to `C_thr` than T16's own corrected empty-scene-only
`PAIR_PAD` reading (`≈0.12×`, Iteration 54/R9).

**Settling precondition (disclosed): `rel_dev=9.81×10⁻⁵`** — three orders
of magnitude below the primary metric's own scale; one directional
spot-check, no evidence STEPS=2800 is insufficient with the article present.

Full numbers, self-scoring, and idealizations: `phase1_proposal.md`
"PHASE 1 RESULTS" section (below its pre-registered bands, appended after
the run, never hand-typed — copied from `results.json`/`run_output.txt`).

## Learned

1. **This nine-cycle sub-thread's own empty-scene-only status is retired**:
   the PAD confound is not a hypothetical risk any future constraint-3
   citation might inherit — it is now a measured, quantified, real-scene
   effect at material (not negligible, not dominant) amplitude relative to
   this program's own perceptual bar.
2. **The confound's relative weight against `C_thr` grew, not shrank, once
   a real article was loaded** (0.12×→0.68× on the comparable normalization)
   — the opposite of VISION's own exp-076 "good news" hypothesis (that the
   object-minus-flank subtraction would suppress a pure background
   systematic). This is the more consequential of the two possible outcomes
   this cycle's own pre-registration named as informative either way.
3. **The reproduction-precondition discipline paid for itself immediately**:
   confirming this cycle's own new FDTD harness reproduces six-cycle-old
   committed numbers bit-exactly, before trusting a single new (article-
   loaded) number, is exactly the R4 discipline this program's history
   argues for — and it passed cleanly here, at the tightest possible bar
   (`max_dev=0.0`, not merely "small").

## Next

This result is Phase 1's own self-scored reading only — it has not yet
been through blind Phase-2 critique, a Red Team audit, or Phase-5 review,
and per this program's own standing practice should not be treated as a
Combined Verdict until it has. Natural follow-ups this cycle's own
idealizations name explicitly: extend to `PAIR_ABSORB40`/`C80−C40`; the
full 31-point window at this reduced-power result's own confirmed scale;
a second, weaker (σ(I)-style) article to test whether visibility of the
confound in `C` scales with the article's own absorption strength; a
proper R3-grade settling convergence study with the article present (this
cycle ran one directional spot-check only).

Riders folded into this same cycle (PLAN.md Iteration-59 Tier 0/Tier 1,
`x_wall_realizable_refit.py`/`phase_convention_extension.py`, results
reported in the Director's report to the panel): the x-wall realizable-
admittance refit (item 1) and the phase-convention tie-breaker extension to
`[47.5°,54.5°]` (Tier 1 item 4). THERMODYNAMICS' hygiene bundle (items 2–3)
applied directly to `experiments/081-.../photonics_construction.py`/
`NOTES.md`, same-shift.
