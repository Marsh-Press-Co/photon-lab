# exp-080 — EM's Validity Pre-Check of the Plane-Wave/Global-Steering Y-Wall Construction

**Panel Iteration 57.** Lead: **ELECTROMAGNETISM** (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's Phase-2 audit,
verdict **PROCEED-WITH-MANDATORY-FIXES, 5-item docket, ALL 5 items
ADOPTED, ZERO overridden** — full record in `phase1_proposal.md`,
`phase2_critique_{materials,photonics,quantum,thermodynamics,vision}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`). Phase 5: six blind
reviews (unanimous PARTIAL) + Red Team's final audit (PARTIAL — see
`phase5_redteam_audit.md`). *Written retroactively, same shift as the
Phase-5 final audit, per that document's own mandatory-fix docket item 1
(VISION's Phase-5 finding: this cycle was missing the `NOTES.md` every T28
cycle 076–079 has) — reconstructed honestly from this cycle's complete,
already-committed Phase 1–5 record, not from memory.*

## Mandate

`experiments/079-.../phase5_redteam_audit.md` §3/§7 Tier-0 item 1 and
`experiments/079-.../phase5_review_photonics.md` §4: before anyone builds
the plane-wave/global-steering y-wall construction Red Team's exp-079
final audit recommended (and PHOTONICS' own Phase-5 review sketched a
concrete build for), formalize whether replacing the already-tested
per-point bounce angle `theta_local(y_s)` with one global angle is even a
defensible approximation of the real multi-point aperture-wall
interaction — a validity pre-condition check on a not-yet-built
instrument, not a mechanism claim of its own.

## Hypothesis

Two independent, falsifiable questions, pre-registered before any code
beyond `phase1_proposal.md` was written:

- **(a) Fraunhofer/far-field margin + `theta_local` spread.** Predicted
  **FORECLOSE** — the aperture-to-wall geometry (`dist_image`/`d_F` ratio,
  `theta_local` spread across the aperture) was expected to reproduce
  exp-079's own Red Team audit's independently-derived figures
  (`0.8–2.1%`/`2.8×` for C40) closely, since the geometry has not changed.
- **(b) Single-angle reproduction of the full per-point envelope.**
  Predicted **SUPPORT**, with real, disclosed uncertainty: exp-079's own
  reflectance-ablation control showed total ablation of `r(theta_local(y_s))`
  to a bare constant barely moved two of three pair-delta periods, so a
  gentler single-`theta_eff` simplification was expected to track the true
  curve's *shape* at least as well — in real tension with (a)'s own
  predicted FORECLOSE, disclosed explicitly as a competing consideration
  rather than smoothed over.

## Setup

Reuses committed machinery programmatically throughout (R4 discipline),
zero new FDTD anywhere in this cycle:

- **Geometry**: `experiments/065-.../design_geometry.py::CONFIGS` (`W`,
  `D_SP`, `OBJ_Y`, `y_lo`/`y_hi` per congruent config, re-confirmed by
  direct import, never hand-typed).
- **Reflectance**: `experiments/075-.../boundary_reflectance.py`
  (`CPL`, `damp_e_profile`/`nu_profile`/`n_profile_exact`).
- **Per-point machinery**: `experiments/079-.../y_wall_aperture_sum.py`
  (`theta_local_deg`, `dist_image_cells`, `aperture_amplitude`,
  `source_driven_phase`, `reflection_coefficient_vec`,
  `build_aperture_grid`, `echo_field_curve`, `K600`, `CONGRUENT_KEYS`) —
  all already gated in that file's own `main()` (G-LOSSLESS/G-N1/
  G-PASSIVITY, a bit-exact vectorized-vs-scalar validation).
- **Comparison target**: `y_wall_aperture_sum_results.json::primary_model_curves`
  (exp-079's own frozen, native-grid record), with a version-drift guard
  recomputing the true curve fresh before trusting any comparison built on
  it.
- **Pre-registered bands** (frozen in `phase1_proposal.md`, commit
  `6fb6b99`, before `validity_precheck.py` existed): part (a)
  FORECLOSE/MARGINAL/DOES-NOT-FORECLOSE by Fraunhofer-ratio and
  `theta_local`-spread thresholds; part (b) SUPPORT/INCONCLUSIVE/REFUTE
  by `R²` bands matching this sub-thread's own `Re{E_echo}`-primary /
  `|E_echo|`-secondary convention.

## Idealizations (from `phase1_proposal.md` §3, carried forward)

1. `theta_eff`'s definition (amplitude-weighted mean) is a modeling
   choice, not a derivation; a midpoint cross-check bounds but does not
   eliminate this sensitivity.
2. A high part-(b) `R²` would not itself validate PHOTONICS' own,
   structurally different, `θ_beam`-dependent §4 construction — a
   narrower, necessary-but-not-sufficient question.
3. The Fraunhofer criterion's numerical prefactor (`d_F=W²/λ`, no factor)
   is a classical heuristic, not a unique constant.
4. Every physics primitive (`theta_local_deg`, `aperture_amplitude`,
   `dist_image_cells`, `source_driven_phase`, `reflection_coefficient_vec`)
   is inherited, not independently re-verified, from `y_wall_aperture_sum.py`.
5. Comparison is against the already-committed native-grid (`oversample=1`)
   curves — the same discretization exp-079's own Combined Verdict used.
6. The version-drift guard checks for accidental drift between the frozen
   record and the live function it imports, not a re-audit of exp-079's
   own result.

**Predictions committed to git before the run**: `phase1_proposal.md`,
commit `6fb6b99` (15:06:19 UTC), before `validity_precheck.py` (commit
`23203cc`, 15:08:40 UTC) — confirmed by independent `git log` checks in
both the Phase-2 VISION critique and the Phase-5 VISION review.

## Result

**(a) FORECLOSE, exactly as predicted.** Worst `dist_image/d_F` ratio
`2.145%` (≈4.7× inside the FORECLOSE threshold), worst `theta_local`
spread `2.752×` (≈1.8× past the FORECLOSE threshold), at every one of the
5 congruent configs, not merely C40 — generalizing and reproducing
exp-079's own audit-cited figures from a fresh script. Robust across the
program's own full 450/600/750nm wavelength sweep (PHOTONICS' Phase-5
addition, not part of the original pre-registered run, but independently
checked and confirmed non-fragile to the untested wavelengths).

**(b) INCONCLUSIVE under the matched admittance — REFUTING my own
pre-registered SUPPORT prediction.** Mean `R²(Re,primary)=0.7345`, C70
minimum `0.5214`, falling in the pre-registered INCONCLUSIVE band, not the
predicted SUPPORT band. Phase 3's fold-in (adopting Red Team's Phase-2
fix docket in full) then established this verdict is **admittance-family-
dependent**, not a single number: mean `R²=0.4305` (**REFUTE**) under the
realizable (`μ_r=1`) admittance, with C40/G40 going negative — worse
exactly at the ABSORB depth (40) the two admittance families are
independently known to diverge most. MATERIALS' Phase-5 review further
showed this REFUTE survives a best-fit-scale robustness check
(`R²≈0.16–0.21` even with a free, sign-flipping scalar) — a genuine
phase/shape failure, not a calibration artifact.

**(c) PHOTONICS' own §4 image-term construction: a real amplitude-regime
finding about its image-only component, not a scored test of the actual
construction.** QUANTUM's blind Phase-2 critique built
`E_photonics(θ_beam)=r(90°−θ_beam;ABSORB)·W(θ_beam)` (zero new FDTD,
Red-Team-adopted into `validity_precheck.py` as `photonics_image_term_curve()`)
and found a catastrophic raw amplitude mismatch (100–400×) against
exp-079's own per-point curve — a direct numerical consequence of part
(a)'s own FORECLOSE finding (the aperture never actually presents
`90°−θ_beam` to the wall). But the Phase-5 layer (QUANTUM again, this
cycle's own fresh instance, independently confirmed by this cycle's Red
Team final audit against the primary source) found this construction
omits `E_direct` **and** was never scored the way PHOTONICS' own original
exp-079 sketch specified (a free-period fit against real T28 data, not an
R²-shape-comparison against a candidate curve) — two compounding gaps,
not one. PHOTONICS' own Phase-5 review separately proved, from primitives,
that the natural `E_direct(θ_beam)` term is bit-identical across all 5
congruent configs at every `θ_beam` — so it cancels exactly in every
pair-delta the eventual correct test needs, closing the one open question
standing between this cycle's record and that test.

## Learned

1. **A pre-registered directional prediction can be honestly falsified
   and still leave the program better off** — EM's own SUPPORT prediction
   for part (b) was wrong (the actual result landed INCONCLUSIVE, then
   REFUTE-under-the-realizable-family), and disclosing that plainly,
   with the reasoning that should have called it more sharply, is exactly
   the R4/verify-before-claim discipline this program runs on.
2. **A single-admittance-family headline number, even when correctly
   computed, can be materially incomplete when the tested family is
   already established elsewhere in the program as unobtainium** — the
   realizable-family rerun (MATERIALS, folded in at Phase 3) moved part
   (b) from a coin-flip-reading INCONCLUSIVE to a REFUTE-range warning
   concentrated exactly where the two families are known to diverge most.
3. **"Effectively already built" is not the same claim as "built and
   scored under this program's own pre-registration discipline"** —
   QUANTUM's Phase-2 critique computing PHOTONICS' construction as part of
   a blind critique, and Red Team adopting it as canonical, is a
   reasonable practice for folding in a correctly-computed number, but it
   is not the same as freezing a SUPPORT/INCONCLUSIVE/REFUTE band before
   running the actually-decisive test — a gap QUANTUM's own Phase-5
   instance caught in its own Phase-2 instance's language, and which
   Iteration 58 should close by running the real test, not by treating
   the desk-level R² comparison as though it already were one.
4. **A cross-seat synthesis can require two Phase-5 seats, not one** —
   PHOTONICS' `E_direct`-cancellation proof and QUANTUM's methodology
   finding are complementary, not overlapping: neither alone tells
   Iteration 58 it now has every ingredient in hand to run the correct
   test for the first time in this eight-cycle sub-thread's history.
5. **A missing `NOTES.md` is a real, if minor, process gap even when its
   substance exists elsewhere** — `phase1_proposal.md` fully carried the
   hypothesis/setup/idealizations/pre-registered-predictions content this
   file would normally hold, but the convention (CLAUDE.md: "every
   experiment... a NOTES.md each") exists precisely so a reader does not
   have to know that in advance — the same defect class Iteration 56 (its
   own precedent, exp-078) caught and closed same-shift, recurring here
   until this Phase-5 layer caught it.

## Next

Reconciled Iteration-58 ranking (Red Team's Phase-5 final audit,
`phase5_redteam_audit.md` §6, full detail there). **Tier 0 — zero FDTD,
run as one batch**: (1) build the construction PHOTONICS actually
specified, scored the way PHOTONICS actually specified — total field
`E_direct(θ_beam)+r(90°−θ_beam;ABSORB)·W(θ_beam)`, with `E_direct` now
derived and proven to cancel in every needed pair-delta, scored via
`_free_period_search` against real T28 reference periods, under a FRESH
pre-registered band committed to git before running — the single
highest-value item on the board, now fully specified for the first time;
(2) re-run the house gates over the `[47.5°,54.5°]` angle range this
cycle's own construction evaluates `reflection_coefficient_vec` at,
currently only hand-checked, not committed; (3) price the geometric-
interception × material-reflectivity energy budget THERMODYNAMICS' Phase-5
review identifies as the still-missing third quantity for constraint 3's
own bookkeeping; (4) fix a non-load-bearing docstring error
(MATERIALS) and carry forward the realizability disclaimer explicitly.
**Tier 1 — cheap FDTD**: (5) the real 750/450nm wavelength-generality leg
(deferred FIVE consecutive cycles, 076–080); (6) broadband pulsed
reflectance spectroscopy of the `ABSORB` boundary; (7) the 750nm x-wall
two-wall spot-check. **Tier 2 — the standing charter-relevant test, now
the single most overdue item on the board**: (8) whether the `PAD`-
sensitivity axis survives with a real absorbing article loaded — deferred
FIVE consecutive cycles; if deferred a sixth time, the reason must be
stated explicitly against this cycle's own finding, not by inertia.
**Tier 3 — governance**: (9) Checkpoint criterion 2 ruled NOT YET RIPE,
more precisely specified than before; (10) Checkpoint criterion 4 ruled
non-firing, conditioned explicitly on this cycle's own corrected framing
(not the pre-Phase-5 "does not clear a bar" language) being what
Iteration 58 and LOGBOOK.md actually inherit. Full record: this directory;
`phase5_redteam_audit.md`; LOGBOOK.md Iteration 57.
