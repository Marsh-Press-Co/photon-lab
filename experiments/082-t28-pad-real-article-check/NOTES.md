# exp-082 — The PAD-loaded real-article check (T28, Iteration 59)

**Panel Iteration 59.** Lead: **QUANTUM OPTICS** (by rotation). Phase 1
proposed this cycle's build; Phase 2 (five blind critiques + Red Team's
audit, `phase2_redteam_audit.md`) found the primary verdict's MECHANICAL
computation correct but its SUBSTANTIVE mechanism-continuity prose
overclaimed; Phase 3 (Director synthesis, `phase3_synthesis.md`) adopted
Red Team's six-item fix docket in full and corrected the language below in
place — it supersedes the pre-audit wording it replaces, per this program's
own standing convention (see `experiments/081-.../NOTES.md`'s own
Phase-3-supersedes-Phase-1 structure for the precedent). Phase 5 (blind
review + Red Team final audit) has not yet run.

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

**Primary metric: `ratio = A_scene/A_empty = 0.6573`. VERDICT: SURVIVES
stands MECHANICALLY** (pre-registered band `[0.5,2.0]`), decisively inside
the band, not near either boundary — the computation itself is correct and
reproduces bit-exact. **Corrected by Phase 3** (`phase2_redteam_audit.md`
§0d–k, Attack 1): the substantive "same mechanism reaches the channel"
reading is NOT established and is shown, from four independent lines of
evidence (an exact permutation test, p=0.953; the two series' free periods
diverging 190%; a ground-truth check recovering the wrong period for a
signal of independently-known period; a 200,000-trial null-permutation
control showing the achieved R² is common under pure noise at n=7), to be
UNRESOLVABLE at this cycle's own 7-point statistical power — not merely
under-supported. Full numbers: `phase1_proposal.md`'s corrected PHASE 1
RESULTS section; full derivation: `phase2_redteam_audit.md` §0d–k.

**Secondary (disclosed, relabeled per Phase 3 as an
instrument-uncertainty-budget number, not a perceptual-detectability
claim): `A_scene/C_thr = 0.6815`** on this one 7-point/`PAIR_PAD`/flagship-
article instance. Three correctly-labeled comparators against T16's own
corrected empty-scene-only `PAIR_PAD` reading (`≈0.12×`, Iteration 54/R9):
naive/mismatched-convention ≈5.5×, properly like-for-like (`ptp`-to-`ptp`)
≈2.77× (Red Team's own re-derivation, `phase2_redteam_audit.md` §0l —
VISION's own Phase-2 "≈4.2×" correction did not reproduce from its own
stated operands and is not used), each measuring a different thing. Full
table: `phase1_proposal.md`'s corrected PHASE 1 RESULTS section.

**Settling precondition (disclosed): `rel_dev=9.81×10⁻⁵`** — three orders
of magnitude below the primary metric's own scale; one directional
spot-check, no evidence STEPS=2800 is insufficient with the article present.

Full numbers, self-scoring, and idealizations: `phase1_proposal.md`
"PHASE 1 RESULTS" section (below its pre-registered bands, appended after
the run, never hand-typed — copied from `results.json`/`run_output.txt`).

## Learned

*(Items 1–2 corrected by Phase 3 — `phase3_synthesis.md` — per Red Team's
fix-docket items 1–2, `phase2_redteam_audit.md` Attacks 1–2. The pre-audit
wording of both items overclaimed; the corrected wording below supersedes
it in force.)*

1. **A comparable-scale oscillation on the empty-scene `PAD`-sensitivity
   axis reaches the real, article-loaded Weber-contrast channel, for the
   flagship, strongly-absorbing article class specifically** — this is
   established mechanically (`ratio=0.6573`, reproduces bit-exact) and is
   scoped explicitly to `materials.graded_black_shell`+`pec_disk`, not
   "real absorbing articles" in general (MATERIALS' Phase-2 finding,
   adopted in full). Whether this is the SAME lossless phase mechanism
   Iteration 53 characterized on the empty scene, merely observed through
   the article's own shadow term, or a qualitatively different,
   article-mediated interaction of similar scale, is **open and shown to
   be unresolvable at this cycle's own statistical power** (item 2, below)
   — this is NOT the "empty-scene-only status is retired" claim the
   pre-audit record made; that claim assumed mechanism continuity this
   cycle cannot establish.
2. **The shape/mechanism-identity question is demonstrated, not merely
   under-supported, to be below this instrument's own resolving power at
   n=7** — Red Team's audit ran four independent checks (an exact
   permutation test on the observed `r=0.031`, p=0.953; the real
   free-period-search machinery run directly on both series, giving
   periods 190% apart; a ground-truth check showing the same instrument
   recovers the WRONG period, 78% off, for a signal whose true period is
   independently known; a 200,000-trial null-permutation control showing
   the achieved R²≈0.86 is what ~26–27% of pure noise clears at this n) —
   all four converge on the same conclusion, from data already in
   `results.json`, zero new FDTD. This merges with THERMODYNAMICS' own
   mechanism-identity finding (Iteration 53's losslessness proof is
   empty-scene-only, never re-verified with a real absorber in the echo
   path) into one open question, not two footnotes (Red Team Attack 3).
3. **The reproduction-precondition discipline paid for itself immediately**:
   confirming this cycle's own new FDTD harness reproduces six-cycle-old
   committed numbers bit-exactly, before trusting a single new (article-
   loaded) number, is exactly the R4 discipline this program's history
   argues for — and it passed cleanly here, at the tightest possible bar
   (`max_dev=0.0`, not merely "small").

## Next

This result has now been through blind Phase-2 critique (five seats,
unanimous support-with-changes) and Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, six-item fix docket, adopted in full by
Phase 3 — `phase3_synthesis.md`). It should be read as the corrected
"Result"/"Learned" sections above state it, not the pre-audit framing.
Natural follow-ups, named explicitly:

- **The near-null σ(I) article follow-up (MATERIALS' own flip condition,
  Red Team Attack 2)** — rerun the identical `PAIR_PAD`/C40–G40 harness
  with `build_article` replaced by the near-null σ(I) OFF-state
  construction (`off_pass`, `τ_off≈0.0065`, exp-032/exp-034) in place of
  `graded_black_shell`, and check whether `ratio`/`A_scene/C_thr` land in
  a comparable range to this cycle's flagship-article reading. This is the
  test that would extend the Combined self-score's own flagship-only
  scoping to the near-threshold case where the confound could plausibly be
  perceptually load-bearing. Named here as a board item per the task
  brief's own instruction; the PLAN.md queue edit itself is a Phase-5
  Director action, not made in this pass.
- **The full 31-point/0.2° window at this same `PAIR_PAD` pair** — the
  single test that would give the free-period search the statistical power
  Red Team's own audit shows this cycle's 7-point reduction demonstrably
  lacks (§0i–k), and so the most direct way to settle the mechanism-
  identity open question (Learned item 2, above).
- Extend to `PAIR_ABSORB40`/`C80−C40` (not re-tested this cycle).
- A proper R3-grade settling convergence study with the article present
  (this cycle ran one directional spot-check, corroborated by EM's own
  independent second spot-check at a different angle/STEPS pair — still
  2 of 14 config×angle cells, not full-grade).

Riders folded into this same cycle (PLAN.md Iteration-59 Tier 0/Tier 1,
`x_wall_realizable_refit.py`/`phase_convention_extension.py`, results
reported in the Director's report to the panel): the x-wall realizable-
admittance refit (item 1) and the phase-convention tie-breaker extension to
`[47.5°,54.5°]` (Tier 1 item 4). THERMODYNAMICS' hygiene bundle (items 2–3)
applied directly to `experiments/081-.../photonics_construction.py`/
`NOTES.md`, same-shift.
