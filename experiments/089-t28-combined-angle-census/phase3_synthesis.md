# PHASE 3 — SYNTHESIS · exp-089 · Panel Iteration 66

Director (this shift's runner). Read: `phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md` in full.

## Disposition of Red Team's 9-item fix docket

Red Team's ruling: PROCEED-WITH-MANDATORY-FIXES, zero items overridden, zero
conflicts between the five critiques. I adopt all nine items in full — Red
Team's own re-derivation from primitives (§0 of its audit) leaves nothing for
the Director to re-litigate; every attack it sustained was independently
confirmed exact, and its own reasoning for elevating items 1/2/4 to blocking
(rather than merely recommended) is sound and is adopted verbatim.

1. **[BLOCKING, adopted] Dual-section carried-idealizations banner.** Added
   inline at the top of NOTES.md's Predictions section (mirrors exp-088's own
   fix-item-2 banner exactly), naming Idealizations 2, 7, 8, 9/10, 11, and a
   restated FLOOR/RMS material-and-wavelength-specificity idealization. Will
   also open the Result section once Phase 4 runs — carried forward as a
   same-shift Phase-4 obligation, not deferred.
2. **[BLOCKING, adopted] False superlative corrected.** "41.4° is the
   thinnest margin of any angle this sub-thread has ever sent to FDTD" is
   dropped; restated scoped to floor-*clearing* angles specifically (38.6° at
   0.39× was sent to FDTD twice, at exp-087 and exp-088, and failed the
   floor gate — it is not a "floor-clearing" comparison point).
3. **[BLOCKING, adopted] The 1.4° gap's protection explicitly scoped down.**
   NOTES.md states plainly, alongside the combined-picture prediction, that
   the 38.8°→40.2° gap is NOT protected against a feature at `frac_p_abs`'s
   own demonstrated sub-0.4° native scale — the only directly-measured
   evidence of that quantity's own angular structure (exp-088's 38.4°→38.6°
   step) argues the reverse of what the borrowed `delta_scene`-period
   yardstick implies.
4. **[BLOCKING, adopted — Director's choice between Red Team's two named
   paths] Q4 recalibrated by dropping CONFIRM/REFUTE labels entirely.** Of
   Red Team's two offered fixes (rebase thresholds via the 3.17× bias
   correction and add a non-aliased control angle at 16 total calls; or drop
   the labeled verdict and report raw numbers only), I choose the second,
   cheaper, more conservative path: `frac_p_abs(40.2°)` and
   `frac_p_abs(41.4°)` are reported as raw measured numbers, explicitly NOT
   scored as a periodicity-inheritance CONFIRM/REFUTE, pending the
   still-queued formal null-controlled period fit (Idealization 12/R14(b)).
   Reasoning: a bias-correction factor measured at a single point (38.4°)
   and applied to two different angles is itself an unverified
   extrapolation — introducing a second desk-estimated correction on top of
   an already-contested one adds a new disputable number rather than closing
   the gap. Reporting raw numbers with the aliasing risk and the correlated-
   with-Q3 disclaimer (fix item 4's own second half, adopted below) is
   simpler, keeps the frozen 12-call budget VISION SCIENCE originally
   proposed (inside Red Team's own "~8–16" estimate without the top-of-range
   overshoot item 7 would have required), and defers the actual periodicity
   claim to the disciplined instrument (a real null-controlled fit) rather
   than a second-order correction to an already-flagged-biased one. The
   §7.1 decoupling disclaimer (Q4's reading does not corroborate or
   undercut any Q3 finding at the same angle) is adopted verbatim regardless
   of which path was chosen, exactly as Red Team specified.
5. **[Recommended, adopted, zero marginal cost] NETD/T9-anchor extension.**
   Added at all three new angles, mirroring exp-088's own Q6/Q7 exactly —
   `p_abs_w` is already a mandatory Phase-4 output for `frac_p_abs` itself,
   so `netd_disposition`/`ratio_abs_ext` cost nothing further.
6. **[Recommended, adopted, minor] Attribution corrected.** R14(a)'s
   parent-curve smoothness finding is credited to QUANTUM OPTICS' own
   Phase-5 self-review (not THERMODYNAMICS), per R14's own LOGBOOK text.
7. **[N/A given item 4's chosen path.]** Red Team's item 7 (a non-aliased
   control angle) was conditioned explicitly on choosing path (a) for item
   4. Since item 4 above adopts path (b) instead, item 7 does not apply —
   noted here so its absence from `run.py` is not read as a dropped fix.
8. **[Recommended, adopted, zero cost] R14(a) given a concrete criterion and
   owner.** `run.py` (Phase 4, automated, not Phase-5 prose judgment) will
   assert `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` are each non-decreasing
   across the combined 8-point sorted angle list, within each point's own
   `box_dev` noise floor — printed as an explicit pass/fail line, not silently
   checked.
9. **[Recommended, adopted, house discipline] Idealization-13-equivalent
   claim re-verified against real code, not carried as an assumption.**
   `run.py`, once written, will be grepped directly for any read of
   `back_frac`/`fwd_frac` before NOTES.md repeats the "not read anywhere in
   this cycle's own scored quantities" claim — Phase 4 obligation, checked
   before Result is written, not assumed from exp-088's own precedent.

Zero items overridden — Red Team's own audit found no conflicts to
adjudicate and no attack the Director judges unsound. This is a confirmatory
adoption, not a fresh weighing call.

## Checkpoint criterion 4 — Director's own explicit ruling, before NOTES.md exists

Red Team ruled (§6/§9 of its audit): the missing banner does not currently
fire criterion 4 (caught blind, at Phase 2, before Phase 3 exists — the
program's own established non-firing shape, identical to exp-088's own
precedent one cycle ago) but is elevated to a MANDATORY fix given Iteration
65's own escalated dual-section rule, with an explicit warning that a fifth
instance reaching Phase 3/NOTES.md unfixed would leave "no room for a
'caught blind, same cycle' discharge argument." I adopt that ruling in full
and close the gap in this same synthesis, before NOTES.md's Predictions
section is written — the banner (fix item 1) and its Result-section
counterpart (carried as a same-shift Phase-4 obligation) are both satisfied
inside this cycle's own Phase 3/4, not left for Phase 5 to catch. Checkpoint
criterion 4 does not fire this cycle.

## Frozen configuration (unchanged from phase1_proposal.md §7)

12 new FDTD calls: 2 configs (`C40`, `G40`) × 3 angles (37.2°, 40.2°, 41.4°)
× 2 legs (empty, article). The R13 floor gate itself costs zero additional
calls. No new control angle is added (item 4's chosen path makes item 7
N/A) — the budget stays exactly as VISION SCIENCE's Phase-1 proposal framed
it.

## NOTES.md

Hypothesis/Setup/Idealizations/Predictions sections follow, in
`NOTES.md`, all nine adopted fixes applied. Committed to git in the same
commit as this file — the house discipline (predictions frozen BEFORE any
Phase-4 code exists) applies to both documents jointly; `run.py` does not
exist yet.
