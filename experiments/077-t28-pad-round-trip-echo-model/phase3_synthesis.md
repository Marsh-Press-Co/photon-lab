# PHASE 3 — SYNTHESIS · Panel Iteration 54 · exp-077

**Director's synthesis.** Per PANEL.md, the Director does not vote in Phase
2 and states here which criticisms are accepted and which are overridden.

## 1. Disposition of Phase 2

Five blind Phase-2 critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS — VISION SCIENCE correctly absent as this
cycle's rotation lead), all `support-with-changes`. Red Team's Phase-2
audit (`phase2_redteam_audit.md`): **PROCEED-WITH-MANDATORY-FIXES, 5
items, zero overridden** — independently re-verified every load-bearing
claim (a third, from-scratch two-wall retarget matching PHOTONICS'/EM's
numbers to 4 decimal places; direct source reads confirming MATERIALS' and
THERMODYNAMICS' claims; a spot-check of QUANTUM's null-calibration figures)
before ruling. Red Team's own Attack 4 caught a new, non-load-bearing
arithmetic slip inside THERMODYNAMICS' own critique text (not the
committed record) — folded into fix 4 below rather than treated as a
sixth item, since it only changes which absolute percentages fix 4 quotes.

**Accepted, in full — nothing overridden.** Red Team's audit is unusually
clean: every critic's claim was independently re-derived by Red Team
itself (not merely cross-referenced), and no critique overreached. The
Director has no basis to override anything Red Team already checked by
hand.

## 2. The five mandatory fixes, as they will be executed

1. **Fold the two-wall-cavity retarget into `pad_round_trip_model.py`
   itself**, as a primary, pre-registered co-result — not a deferred
   idealization footnote. Reuses `two_wall_cavity.py`'s
   `image_geometry_right`/`c_empty_two_wall` verbatim (zero new machinery,
   per exp-075's own precedent for this exact extension). Report Test A/B
   for both single- and two-wall cuts, side by side, for both `PAIR_PAD`
   and `PAIR_ABSORB40`.
2. **Correct the headline language.** "REFUTE... same failure shape" is
   replaced with: Combined REFUTE for `PAIR_PAD` is robust across both
   cuts, but via *different* tests (single-wall: period-dominated;
   two-wall: shape-dominated, and worse); `PAIR_ABSORB40`'s verdict is
   **not** robust to the far-wall term (INCONCLUSIVE→REFUTE) and is
   reported as such, not folded silently into the `PAIR_PAD` headline.
3. **Add an explicit realizability sentence** next to the two-wall
   extension: the `+x` wall is built from the identical unrealizable
   matched-`eps=mu` admittance class as the `-x` wall (`lab/fdtd2d.py::
   _damping`, symmetric across all four edges, independently confirmed by
   MATERIALS and Red Team) — the two-wall cut is an instrument-fidelity
   check only; it cannot move MATERIALS' realizability bound in either
   direction.
4. **Rewrite §3 (THERMODYNAMICS sidecar).** For `PAIR_PAD`: replace "PAD
   is lossless vacuum" with the correct reasoning — `r_for["C40"]` and
   `r_for["G40"]` are the literal same array object
   (`pad_round_trip_model.py` line 176), so the absorbed-power fraction is
   common-mode by code-level construction, not by PAD's own lossless
   status (which remains true but is not the operative reason for THIS
   pair). For `PAIR_ABSORB40`: add the explicit, computed
   Δabsorbed-fraction disposition and argue its thermodynamic
   insignificance quantitatively. **Use the Red-Team-recomputed absolute
   percentages** (Red Team found THERMODYNAMICS' own cited range
   contained an arithmetic slip — the load-bearing Δ figure was
   unaffected and is kept).
5. **Add a null-calibration appendix** — a 20,000-trial pure-noise Monte
   Carlo null and a 20,000-trial bootstrap ground-truth-recovery check,
   both against the actual committed `_free_period_search` (not
   reimplemented) — to `pad_round_trip_model.py`/
   `pad_round_trip_results.json`, cited numerically in the corrected
   proposal, before REFUTE is treated as fully closed on the record.

All five are zero new FDTD, zero `lab/` diff — matching this cycle's
original zero-marginal-cost scope. Red Team's own disposition table is
adopted verbatim; see `phase2_redteam_audit.md` for the full docket text.

## 3. FROZEN PREDICTIONS — committed before this cycle's corrected script
is executed

Three independent implementations (PHOTONICS, ELECTROMAGNETISM, Red Team),
each built from scratch, already agree to four decimal places on what the
two-wall retarget produces. Per house discipline (predictions committed
BEFORE any run), the Director states the expected outcome of folding fix 1
into the single committed script BEFORE executing it as Phase 4, so that
Phase 4 is a confirmation, not a first look:

- `PAIR_PAD` two-wall: `P*_model ≈ 8.6677°`, Test A `rel_dev ≈ 0.8797` →
  **INCONCLUSIVE** (period test, flipped from single-wall's REFUTE);
  Test B `r² ≈ 0.0001` → **REFUTE** (shape test, four orders of magnitude
  worse than single-wall's already-weak `0.0444`). **Combined: REFUTE**
  (via Test B alone — the disjunctive combining rule requires only one
  REFUTE).
- `PAIR_ABSORB40` two-wall: `P*_model ≈ 7.0372°`, Test A `rel_dev ≈
  0.6851` → INCONCLUSIVE (little changed); Test B `r² ≈ 0.0418` →
  **REFUTE** (down from single-wall's `0.1997` INCONCLUSIVE). **Combined:
  REFUTE (flipped from single-wall's INCONCLUSIVE).**
- Gates (G-LOSSLESS, G-N1, G-PASSIVITY) re-run on the same `r(theta)`
  values: expected to pass identically to the single-wall run (the gates
  test the transfer-matrix code, not which wall(s) the propagator sums)
  — worst `|r|=0.0064`, well inside `|r|≤1`.
- Null-calibration appendix (fix 5): expected to show both curves' fitted
  `R²` values are far outside what 20,000 pure-noise trials produce
  (QUANTUM's own finding, independently spot-checked by Red Team at
  reduced scale) — i.e. the appendix is expected to *strengthen*, not
  threaten, the REFUTE verdicts above.

**If Phase 4's actual re-run of the corrected, single committed script
disagrees with any number above by more than rounding, that disagreement
itself becomes the headline finding of this cycle** (a fourth independent
implementation disagreeing with three prior ones would be far more
newsworthy than another REFUTE) — the frozen numbers are not a target to
reach, they are a check on Phase 4's own arithmetic.

## 4. T1 / Checkpoint disposition, carried from Phase 2

**T1 escape route: N/A**, unchanged — instrument/model-fidelity thread,
constraint 3 not engaged (Red Team's audit confirms this explicitly).
**No Checkpoint criterion fires** at Phase 3: every gap Phase 2 raised was
caught before this freeze, matching the program's own established
non-firing pattern. Should Phase 4 fail to reproduce any frozen number
above, or should the corrected write-up's own headline still read as if
the two-wall result were "the same failure shape" after this synthesis
explicitly corrects that language, that would be a fresh, mechanically
predictable Criterion-4 firing — the entire point of writing the
prediction down now.

## 5. What Phase 4 will do

Implement fixes 1/3/4/5 in `pad_round_trip_model.py` (fix 2 is a prose
change to `phase1_proposal.md`, applied when the corrected write-up is
finalized post-run); re-run the single committed script end-to-end;
compare every number against §3's frozen predictions; write
`phase4_results.md` stating CONFIRMED/NOT CONFIRMED per prediction, and
update `phase1_proposal.md` (or supersede it with a corrected
`NOTES.md`-facing summary, per house convention for a Phase-3 fix-driven
rebuild) with the corrected §1/§3/§5 language.
