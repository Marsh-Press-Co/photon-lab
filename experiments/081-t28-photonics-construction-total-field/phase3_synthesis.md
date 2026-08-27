# PHASE 3 — SYNTHESIS · Director · Panel Iteration 58 · exp-081

**Role: Director** (synthesizes, does not vote). Read the complete Phase 1
record (`phase1_proposal.md`, `photonics_construction.py`,
`phase1_results.json`, `NOTES.md`), all five blind Phase-2 critiques, and Red
Team's Phase-2 audit (`phase2_redteam_audit.md`) in full before writing this.
Also read `experiments/080-.../validity_precheck.py`'s
`reflection_coefficient_vec_realizable` (already-fixed docstring) and
`experiments/079-.../y_wall_aperture_sum.py` §[7]/§[7b] (the
reflectance-ablation-control idiom this synthesis reuses).

## 1. Disposition of Red Team's Phase-2 audit

Red Team's ruling: **PROCEED-WITH-MANDATORY-FIXES**, a 7-item prioritized fix
docket (`phase2_redteam_audit.md` §3), zero overrides of any of the five
blind critiques (all five ADOPTED IN FULL, two factual sub-claims corrected
evenhandedly — MATERIALS' implied outcome-urgency, VISION's historical
generalization). Red Team did not merely re-argue the three consequential
"missing check" findings the blind critiques raised (MATERIALS' realizable-
admittance gap, PHOTONICS'/QUANTUM's convergent ablation-control gap, EM's
phase-convention gap) — it **ran all three to completion**, independently,
from primitives, in its own from-scratch scratch script, after first
reproducing exp-081's own committed item-1 result bit-exact as a wiring
check. Every existing number in `phase1_results.json` and all five blind
critiques reproduced exactly (§0 of the audit); three genuinely new numeric
results (§0 items A/B/C, plus the phase-divergence explanation item D) had
to be computed to adjudicate whether the critiques' concerns are
outcome-determining.

**The Director adopts Red Team's audit in full — all seven fix-docket items,
zero overrides.** This is not a rubber stamp: Red Team's audit independently
reproduced every existing number bit-exact, actually ran all three flagged
gaps to completion rather than merely arguing about them, found the
ablation-control result (item 2 of the docket) is **pair-specific and MORE
damaging to the lone SUPPORT than any of the five critiques anticipated**
(neither PHOTONICS' nor QUANTUM's own binary flip-condition framing
survived contact with the actual per-pair result), and corrected both an
over-worried critique (MATERIALS' implied urgency-by-analogy to exp-080's
part(b), shown not to transfer to item 1's own more-grazing angle regime)
and an over-stated one (VISION's "every cycle since exp-076" historical
claim, shown to not survive an independent `git log` check against exp-079)
**evenhandedly — no self-serving asymmetry in which direction the
corrections run.** This matches this program's own established practice
(exp-080 Iteration 57's own Phase 3) of adopting a rigorous, non-self-serving
Red Team fix docket in full rather than re-litigating findings Red Team has
already independently re-derived from primitives.

## 2. Corrected headline language (supersedes `phase1_proposal.md`'s
## PHASE 1 RESULTS and `NOTES.md`'s pre-audit prose, precisely, not by
## restatement)

These five corrections replace, verbatim in force, the pre-audit language
Red Team's audit (`phase2_redteam_audit.md` §3, items 1–6) found overclaims
or misstates what was actually established:

1. **Combined Verdict NEITHER for item 1 stands under BOTH admittance
   families** (periods shift ≤0.0075° between families — not
   outcome-determining; the phase-divergence at this cycle's 48–54° range is
   only 8.4–10.6°, much smaller than exp-080 part(b)'s 54.0–83.6° at 5–15°,
   which is WHY this differs from that precedent). This corrects
   `phase1_proposal.md`'s single-admittance-family headline (Red Team's
   Attack 1, MATERIALS' Phase-2 finding).

2. **Item 1c's "REFUTE-leaning" reading is PAIR-SPECIFIC, not uniform.**
   `PAIR_ABSORB40` is genuinely `r()`-dependent (ablated signal exactly
   degenerate vs real `rel_dev=0.5139`); `C80−C40` — the ONE pair carrying
   the lone SUPPORT — survives ablation to `r()=1` almost unchanged
   (`≈0.2937` vs real `0.2910`), **proving that SUPPORT requires no wall
   reflectance at all**, i.e. it is NOT evidence for a real y-wall echo
   mechanism; `PAIR_PAD` is partially dependent (`~0.15°` shift). The
   substantive reading is REFUTE for the mechanism as a whole, **now on
   firmer ground than the Phase-1 draft's own hedge** — the ablation control
   Phase 1 lacked (Red Team's Attack 2, PHOTONICS'/QUANTUM's convergent
   Phase-2 finding) is what actually proves this, not merely the
   T21-proximity distance comparison item 1c originally rested on alone.

3. **Item 2's magnitude-only gates (G-LOSSLESS/G-N1/G-PASSIVITY) do NOT
   resolve the `r` vs `conj(r)` phase-convention ambiguity** (R8's own
   concern, EM's Phase-2 finding) — `NOTES.md`'s "item 1's own construction
   can be trusted at this range going forward" language is corrected to
   state precisely what a magnitude-only battery establishes (algebraic
   self-consistency of `reflection_coefficient_vec`, `|r|` bounded by 1) and
   does NOT establish (the sign/phase convention item 1's entire
   period-recovery result is actually driven by). The `conj(r)` sensitivity
   result computed this cycle (no verdict flips) is **reassuring, not
   resolving** — the true empirical question of which convention the real
   graded-loss boundary's physics realizes at this new, more-grazing angle
   range remains genuinely open and requires new FDTD. **Explicitly queued
   for Iteration 59**: extend `phase5_redteam_phase_convention_check.py`'s
   own idiom to 2–3 angles inside `[47.5°,54.5°]`, mirroring exp-075's own
   `[0°,20°,39°]` precedent. Not run this cycle (Idealization 7, zero new
   FDTD).

4. **Git-provenance claim, corrected.** PANEL.md's literal text binds the
   non-negotiable git-before-run mandate to **Phase 3**'s FROZEN PREDICTIONS
   commit specifically — this document, committed before
   `photonics_construction.py`'s Phase-3 extensions are run. VISION's
   Phase-2 finding that Phase 1's own single combined commit (`ff73016`)
   lacked a separately-verifiable pre-registration is real and is fixed
   here, but Red Team's Attack 4 correctly found VISION's "every cycle since
   exp-076" historical generalization does not hold (exp-079's own Phase 1
   also combined proposal+run into one commit, with no objection raised in
   that cycle's record; exp-076/077 predate this repo's visible git history
   entirely). The two-commit split is exp-080's own individual practice, not
   an established multi-cycle norm this cycle regressed from — restored
   here as this cycle's own practice, going forward.

5. **Item 3's energy-budget headline, disambiguated by which bound covers
   which tested object.** The `theta_local`-convention bound (`≈1.3×10⁻⁸`
   matched / `≈2.6×10⁻⁸` realizable, ABSORB=40) covers a construction item 1
   never built or period-tested — item 1's own tested object uses the
   `90°−θ_beam` convention throughout, whose own bound is the far looser
   `0.15%` (`1.4943×10⁻³`). Both are legitimately negligible in absolute
   terms, but `NOTES.md`'s "negligible... under either angle convention"
   framing is corrected to state explicitly which bound is a bound on the
   object item 1 actually tested and scored, and which is a bound on a
   different, physically-more-correct but not-yet-built construction (EM's
   secondary Phase-2 point, Red Team fix-docket item 6).

## 3. Fixes folded into committed, reusable code

Per Red Team's fix docket §3 items 1–3 (the three items requiring new
computation, not merely prose correction), `photonics_construction.py` is
extended in place (this document's own companion commit) with:

- `_image_term_curve_generic(cfg, absorb_for_r, thetas_beam_deg,
  admittance="matched"|"realizable", r_transform=None)` — the one generic
  image-term builder underlying `d80.photonics_image_term_curve()`,
  parameterized by admittance family and an optional transform on
  `r(90°−θ_beam)`, replacing what would otherwise be three near-duplicate
  copies of that function's own loop. `main_phase4()`'s own wiring check
  asserts this reproduces `d80.photonics_image_term_curve()` bit-exact at
  its default settings before any variant built on it is trusted — the same
  discipline Red Team's own audit script used.
- `item1_admittance_family_rescore()` — fix docket item 1: re-scores item
  1's free-period fit under BOTH admittance families, reports the period
  shift and phase-divergence explanation (item D).
- `item1c_ablation_control()` — fix docket item 2: the reflectance-ablation
  control (`r(90°−θ_beam)→1` exactly, `y_wall_aperture_sum.py` §[7]'s own
  convention), computed **per pair**, not aggregated.
- `item2_conj_sensitivity()` — fix docket item 3: the `r→conj(r)`
  sensitivity check, reporting per-pair verdict flips (or their absence).
- `main_phase4()` — orchestrates the above, verifies the frozen predictions
  below against the actual output, and writes `phase4_results.json`.

Zero new FDTD anywhere in this extension (Idealization 7, carried forward
unchanged from Phase 1). Zero `lab/` changes.

## 4. PRE-REGISTERED, FALSIFIABLE PREDICTIONS for the corrected re-run
## (frozen here, BEFORE `photonics_construction.py`'s Phase-3 extensions
## are run — house discipline, non-negotiable, PANEL.md Phase 3)

**The corrected script, run fresh, will reproduce Red Team's own
independently-computed audit numbers (§0 of `phase2_redteam_audit.md`) to
within numerical noise:**

- Realizable-admittance periods within **≤0.0075°** of the matched-family
  periods.
- All three per-pair verdicts **unchanged** from the original matched-only
  run (`PAIR_PAD`/`PAIR_ABSORB40` INCONCLUSIVE, `C80−C40` SUPPORT; Combined
  Verdict NEITHER under both families).
- `PAIR_ABSORB40`'s ablated signal **exactly degenerate** (bit-identical
  across the swept `θ_beam` grid, since it's now literally testing a
  config-invariant construction).
- `C80−C40`'s ablated score **≈0.2937** (within ~0.01 of the real `0.2910`).
- `PAIR_PAD`'s ablated shift **≈0.15°**.
- `conj(r)` sensitivity produces **zero verdict flips**.

This IS a genuine, falsifiable pre-registration — a third independent
computation (this cycle's own extended script) should match Red Team's own
scratch computation and this cycle's original committed run, but might not
if either had an undisclosed bug. Matching this program's own R4 discipline:
independently reproduce, don't just trust, even a Red Team audit. **If any
of the above does not reproduce as predicted, that is itself the finding to
report — not something to paper over.**

## 5. Checkpoint ruling (Red Team's, re-reasoned through by the Director,
## same conclusions — nothing in this synthesis changes any of the five)

- **Criterion 1**: N/A (zero constraint-3 or any-constraint engagement,
  confirmed independently by Red Team's own `grep -il` sweep).
- **Criterion 2**: NOT YET RIPE. This cycle's own actually-decisive test
  (total field, real-data free-period fit), now sharpened by the
  admittance-family rescore and the pair-specific ablation control, remains
  a single result on the `90°−θ_beam` global-steering construction at one
  wavelength (600nm) on an empty scene. The board's own oldest-overdue items
  (750/450nm wavelength-generality, the PAD-loaded real-article check, both
  six consecutive cycles deferred as of this iteration) remain the natural
  next tests before any mechanism-class boundary is declared.
- **Criterion 3**: N/A (zero new FDTD, this cycle's own extension included).
- **Criterion 4**: does not fire, conditioned explicitly on this document
  adopting Red Team's fix docket in full — which it does. Repeating
  `NOTES.md`'s pre-audit language verbatim without folding in the
  realizable-admittance, ablation, and phase-convention-sensitivity results
  (§2 above) would have been the firing shape; this document is written
  specifically to avoid that.
- **Criterion 5**: not at risk — this cycle delivers the sub-thread's own
  actually-decisive test, sharpened by three independently-run verification
  extensions.

## 6. Gates

Zero `lab/` changes this entire cycle (Phase 1 or this Phase-3 extension) —
`photonics_construction.py`'s new functions import only already-committed
`dg065`/`br`/`ywas`/`d80` primitives. The house trust suite
(`lab/validation/run_all.py --only 12346789`) is re-confirmed green at
Phase 4 (see `phase4_results.md`); no `lab/` diff this cycle means no new
trust-suite stage is required by house discipline.

## 7. Git provenance for this cycle

This document (`phase3_synthesis.md`) and `photonics_construction.py`'s
Phase-3 extensions (code only — not yet run) are committed together as the
FROZEN-PREDICTIONS commit, genuinely separate from and strictly before the
commit that executes the corrected script and records results — restoring
exp-080's own two-commit standard (§2 item 4 above), per Red Team fix-docket
items 4–5.

Full record: `experiments/081-t28-photonics-construction-total-field/` —
`phase1_proposal.md`, `photonics_construction.py`, `phase1_results.json`,
`NOTES.md`, five Phase-2 critiques, `phase2_redteam_audit.md`, this
document, and (after the next commit) `phase4_results.json`/
`phase4_results.md`.
