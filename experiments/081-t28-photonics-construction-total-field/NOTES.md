# exp-081 — PHOTONICS' Construction, As Originally Specified: Total Field vs Real T28 Periods

**Panel Iteration 58.** Lead: **THERMODYNAMICS** (by rotation). Executes
PLAN.md's Iteration-58 Tier-0 batch in full — all four items, in order
(Red Team's `experiments/080-.../phase5_redteam_audit.md` §6/§7
reconciliation of exp-080's six blind Phase-5 seats).

## Mandate

`experiments/080-.../phase5_redteam_audit.md` §6 Tier-0 item 1 (the single
highest-value item on the whole T28 board, per Red Team's own Phase-5 final
audit): build the construction PHOTONICS actually specified in its own
exp-079 Phase-5 review §4 — `E(θ_beam)=E_direct(θ_beam)+r(90°−θ_beam;
ABSORB)·W(θ_beam)`, total field, both terms present — and score its
`PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` pair-deltas via `_free_period_search`/
staged-widening against the REAL T28 reference periods, not the R²
shape-comparison against a candidate curve exp-080's own
`photonics_image_term_curve()`/`part_d_photonics_construction()` mistakenly
ran (missing `E_direct` AND the wrong methodology — QUANTUM's Phase-5
finding, independently confirmed by Red Team against the primary source).
Folded in alongside: EM's gate re-run at `[47.5°,54.5°]` (item 2),
THERMODYNAMICS' own energy-budget upper bound (item 3), and MATERIALS'
docstring/disclaimer hygiene (item 4).

## Hypothesis

Pre-registered in `phase1_proposal.md` before `photonics_construction.py`
was written:

- **Item 1**: Combined Verdict predicted **NEITHER, leaning REFUTE** —
  part (a)'s FORECLOSE finding (exp-080) and PHOTONICS' own feasibility
  probe (exp-079 §4: `r(90°−θ_beam)`'s phase swings too slowly to produce
  an independent short period) both argue against a clean SUPPORT, but this
  is the first time this exact free-period-against-real-data test has ever
  been run on a `θ_beam`-dependent `r()` term, so real uncertainty was
  disclosed rather than a foregone conclusion.
- **Item 1b**: `E_direct` (config-invariant, PHOTONICS' own proof, cited)
  predicted to cancel EXACTLY (`0.0`, bit-identical) out of every pair-delta.
- **Item 2**: PASS on all three gates at `[47.5°,54.5°]`.
- **Item 3**: the `≤0.15%` `θ_beam`-convention anchor reproduces exactly;
  the physically-correct `theta_local(y_s)`-convention bound predicted to
  be many orders of magnitude smaller.

## Setup

Reuses committed machinery programmatically throughout (R4 discipline),
zero new FDTD:

- **Geometry/reflectance**: `experiments/065-.../design_geometry.py`,
  `experiments/075-.../boundary_reflectance.py`.
- **Per-point machinery**: `experiments/079-.../y_wall_aperture_sum.py`
  (`theta_local_deg`, `aperture_amplitude`, `source_driven_phase`,
  `reflection_coefficient_vec`, `build_aperture_grid`, `_trapz`, `K600`,
  `CONGRUENT_KEYS`, `score_period`, `rel_dev`, `free_period_with_widening`,
  `SS_TOT_DEGENERATE_FLOOR`) — all already gated.
- **Image-term construction**: `experiments/080-.../validity_precheck.py`
  (`photonics_image_term_curve`, `reflection_coefficient_vec_realizable`,
  `part_c_power_budget_at_true_angle`) — reused unchanged.
- **New this cycle**: `dist_direct_cells`/`e_direct_curve` (the direct,
  unmirrored term PHOTONICS' construction needs and no prior T28 cycle has
  built) — ~15 lines, PHOTONICS' own exp-080 Phase-5 formula cited verbatim.
- **Real reference data**: `experiments/076-.../results.json::headline`
  (`C40`/`G40`/`C80`, 31-point/600nm/settled-STEPS=2800), read fresh, never
  hand-typed.
- **Pre-registered bands**: `rel_dev≤0.30` SUPPORT / `>1.00` REFUTE / else
  INCONCLUSIVE per pair (this sub-thread's own convention since Iteration 46);
  Combined Verdict SUPPORT/REFUTE only if all 3 pairs agree, else NEITHER —
  stated explicitly before running (frozen in `phase1_proposal.md` before
  `photonics_construction.py` existed).

## Idealizations

See `phase1_proposal.md` §4 for the full list (7 items). The two most
consequential: (2) `E_direct`'s config-invariance is cited from PHOTONICS'
own proof, numerically re-verified here, not re-derived from first
principles; (5) item 3's interception factor is upper-bounded at 1 (a real,
disclosed idealization that can only loosen, never tighten, the reported
energy bound).

## Result

**Item 1a — `E_direct` PAD-invariance: CONFIRMED, bit-identical** (`0.0`
exactly, all 5 configs, all 31 θ_beam values) — the fourth independent
confirmation of PHOTONICS' own exp-080 Phase-5 proof.

**Item 1 — Combined Verdict: NEITHER** (mechanically: 1 SUPPORT + 2
INCONCLUSIVE + 0 REFUTE). `PAIR_PAD` INCONCLUSIVE (`rel_dev=0.5973`),
`PAIR_ABSORB40` INCONCLUSIVE (`rel_dev=0.5139`), `C80−C40` SUPPORT
(`rel_dev=0.2910`, just inside the 0.30 bar). **This is a REFUTE-leaning
result, not a genuine partial confirmation, once item 1c's own diagnostic
is read**: all three model periods (1.86°/2.03°/2.02°) sit within 2.8–5.3%
of T21's own established 1.9608° fringe but 29–60% from their own scored
T28 targets — the sole SUPPORT is the same "compromise fit between two
nearby frequencies" pattern this program flagged in Iteration 47
(exp-070's P-070-1), not independent evidence. PHOTONICS' own exp-079 §4
feasibility probe predicted exactly this outcome before the construction
was built: "expect the dominant recovered period to still land close to
T21's 1.96°."

**Item 1b — `E_direct`'s effect on the pair-delta scores: cancels to
float-precision noise (`~10⁻¹⁴` absolute, `~10⁻¹⁶` relative to `E_direct`'s
own `O(100)` magnitude), NOT literally bit-identical.** The pre-registered
"`0.0`, bit-identical" prediction is technically REFUTED — honestly
disclosed, not smoothed over — but the substantive claim it tested
(`E_direct` changes nothing about which periods/verdicts this test reports)
is CONFIRMED to 11+ orders of magnitude below the signal scale. Traced:
`|E_direct|≈89–111` is 4–5 orders of magnitude larger than `|E_image|≈
1.3×10⁻⁴`–`3.5×10⁻³` — `E_direct` genuinely is the dominant carrier
PHOTONICS' own analysis predicted, and its cancellation in every pair-delta
is why the actual mechanism signal (all of it in `E_image`) is what gets
scored, exactly as intended.

**Item 2 — PASS, all three gates, at `[47.5°,54.5°]`**: G-LOSSLESS
`2.220×10⁻¹⁶`, G-N1 `3.140×10⁻¹⁵`, G-PASSIVITY worst `|r|=0.041413` — all
comfortably inside their bars. `reflection_coefficient_vec` is now formally
gated at this range, not merely hand-checked in a Phase-5 review.

**Item 3 — the `≤0.15%` anchor reproduces exactly (`1.4943×10⁻³`); the
physically-correct bound is `~116,000×` smaller (`1.289×10⁻⁸` matched,
`2.638×10⁻⁸` realizable, ABSORB=40, interception=1).** Even under the
loosest possible interception assumption (100%), this entire construction
family could never matter to constraint 3's energy budget — and the honest,
`theta_local(y_s)`-based physical bound is many orders of magnitude more
negligible than the `90°−θ_beam`-convention anchor PLAN.md cited as a
sanity check.

**Item 4 — applied**: `reflection_coefficient_vec_realizable()`'s docstring
in `experiments/080-.../validity_precheck.py` corrected (`mu_r=ni^2`→
`mu_r=ni`). Two explicit disclaimers stated here, per MATERIALS'/EM's own
item-4 text:

(a) **The realizable (`μ_r=1`) number, not the matched one, is the only
one that could ever describe a real material.** The matched-admittance
family used throughout `reflection_coefficient_vec`/`echo_field_curve`/
`photonics_image_term_curve` (implicitly `μ_r=ni`, corrected this cycle) is
an established-elsewhere (exp-075) unobtainium construct — every number in
this cycle computed under it (item 1's `E_image`/`E_total`, item 3's
matched-family energy bound) describes a mathematically convenient but
physically unrealizable admittance, not a buildable coating. Item 3's own
realizable-admittance figure (`2.638×10⁻⁸`) is the one that could ever
describe a real material; it happens to be within `2×` of the matched
figure at this specific ABSORB depth and angle range (unlike part (b)'s own
finding elsewhere in this sub-thread, where the two families diverge
sharply at ABSORB=40), but that proximity is a fact about this specific
angle range, not a general license to treat the two families as
interchangeable.

(b) **A valid global-angle y-wall construction needs an angle convention
built from `theta_local(y_s)`'s own fixed-observer geometry, not a borrowed
`θ_beam`-steering convention.** `90°−θ_beam` is PHOTONICS' own construction
choice (a genuine, `θ_beam`-dependent modeling decision, not a claim about
the wall's true physical incidence geometry) — item 3's own `~116,000×`
gap between the two conventions' energy bounds is a direct, quantitative
consequence of this distinction: `theta_local(y_s)` (`5.27°–15.50°` across
the aperture) is the angle the wall's fixed-observer geometry actually
presents; `90°−θ_beam` (`48°–54°`) is an artifact of PHOTONICS' own
θ_beam-steering modeling choice, evaluated at a range item 2 now confirms
is gate-clean but which resolving the near-field problem (part (a)'s own
FORECLOSE finding) alone would not make physically correct.

## Learned

1. **A pre-registered "bit-identical" prediction can be technically
   refuted while its substantive claim is confirmed more strongly than the
   prediction itself asked for** — item 1b's `~10⁻¹⁴` residual is not `0.0`,
   but tracing it to `E_direct`'s own `O(100)`-vs-`O(10⁻³)` magnitude gap
   against `E_image` shows the residual is exactly what floating-point
   arithmetic predicts for two analytically-equal `O(100)` numbers, a
   sharper and more informative finding than the naive "== 0.0" check would
   have delivered on its own.
2. **A construction's first-ever correctly-scored test can produce a result
   that looks partially positive (1 of 3 SUPPORT) purely as a look-elsewhere
   artifact of a nearby, unrelated, already-established periodicity (T21)** —
   the T21-proximity diagnostic (item 1c, not originally in the
   pre-registered band structure but added because a lone near-boundary
   SUPPORT deserves scrutiny, per this sub-thread's own R5 discipline) turns
   a mechanically-NEITHER Combined Verdict into a substantively REFUTE-
   leaning one, without changing the mechanically-computed verdict itself.
3. **This nine-cycle T28 y-wall sub-thread's actually-decisive test, run for
   the first time this cycle, produced the SAME qualitative outcome
   PHOTONICS' own author predicted before the construction was even built**
   (exp-079 §4's feasibility probe) — a genuine confirmation that this
   sub-thread's own physical reasoning has been tracking real structure in
   the problem, even where the construction itself does not reproduce T28's
   real signal.
4. **An energy-budget "sanity anchor" computed under one angle convention
   can overstate the true physical bound by five orders of magnitude** —
   item 3's `~116,000×` gap between the `90°−θ_beam` anchor and the
   `theta_local(y_s)`-based bound is a concrete, quantitative instance of
   why EM's own item-4 caution (a borrowed steering convention is not a
   physical incidence-geometry convention) matters even for a quantity
   (the energy budget) that was never in dispute as "negligible" under
   either convention.

## Next

The plane-wave/global-steering coherent-echo mechanism class (single-edge,
exp-078; full-aperture-sum, exp-079; plane-wave pre-check, exp-080; total
field as originally specified, this cycle) has now had its actually-decisive
test run, for the first time, against real T28 data — and the result is
REFUTE-leaning on the substantive reading (item 1c), joining exp-078's and
exp-079's own structural forecloses as a third independent line of negative
evidence against this construction family specifically. Checkpoint criterion
2 (mechanism-class boundary) is a genuine question for Iteration 59's own
Red Team final audit to weigh explicitly — this cycle supplies the missing
test, not a formal ruling on whether the class is now closed. PLAN.md's own
Tier 1/2/3 items (the deferred 750/450nm wavelength-generality leg, now SIX
consecutive cycles; the PAD-loaded real-article check, now SIX consecutive
cycles) remain the board's own oldest-overdue items, unaddressed by this
cycle's own Tier-0 scope — Iteration 59 should weigh whether continuing to
defer them, now that this construction's own actually-decisive test has
landed REFUTE-leaning, still has an explicit, non-inertial reason.

---

## PHASE 3 — DIRECTOR SYNTHESIS (corrected headline language)

Red Team's Phase-2 audit (`phase2_redteam_audit.md`) ruled
**PROCEED-WITH-MANDATORY-FIXES** and the Director adopts its 7-item fix
docket **in full, zero overrides** — full rationale in `phase3_synthesis.md`
§1. The above Result/Learned/Next sections are Phase 1's own self-scored
language, **written before this audit** and left unedited above as the
historical record — this section is the corrected reading that supersedes
it in force, precisely, not by restatement:

1. **Combined Verdict NEITHER for item 1 stands under BOTH admittance
   families** (periods shift ≤0.0075° between families — not
   outcome-determining; the phase-divergence at this cycle's 48–54° range is
   only 8.4–10.6°, much smaller than exp-080 part(b)'s 54.0–83.6° at 5–15°,
   which is WHY this differs from that precedent).
2. **Item 1c's "REFUTE-leaning" reading is PAIR-SPECIFIC, not uniform.**
   `PAIR_ABSORB40` is genuinely `r()`-dependent (ablated signal exactly
   degenerate); `C80−C40` — the ONE pair carrying the lone SUPPORT —
   survives ablation to `r()=1` almost unchanged (`≈0.2937` vs real
   `0.2910`), proving that SUPPORT requires no wall reflectance at all —
   it is NOT evidence for a real y-wall echo mechanism; `PAIR_PAD` is
   partially dependent (`~0.15°` shift). The substantive reading is REFUTE
   for the mechanism as a whole, now on firmer ground than Phase 1's own
   hedge above.
3. **Item 2's magnitude-only gates do NOT resolve the `r` vs `conj(r)`
   phase-convention ambiguity** (R8's own concern) — "can be trusted going
   forward" (Phase 1's own Result section, item 2) overclaimed. The
   `conj(r)` sensitivity result (no verdict flips) is reassuring, not
   resolving; the actual FDTD-based phase-convention extension is queued for
   Iteration 59, not run this cycle.
4. **Git-provenance claim, corrected**: PANEL.md's non-negotiable
   git-before-run mandate binds to Phase 3's FROZEN PREDICTIONS commit
   specifically (`phase3_synthesis.md`, committed before this cycle's
   corrected script was run) — not to Phase 1.
5. **Item 3's energy-budget headline, disambiguated**: the tight
   `theta_local`-convention bound (`~1.3×10⁻⁸`) covers a construction item 1
   never built or period-tested; the looser `0.15%` `90°−θ_beam`-convention
   bound covers the object item 1 actually tested and scored. Both
   negligible in absolute terms; conflating which covers which was the
   Phase-1 draft's own overclaim.

Full rationale, the pre-registered frozen predictions for the corrected
re-run, and the Checkpoint ruling: `phase3_synthesis.md`. Confirmed numbers
from the corrected re-run: `phase4_results.md`/`phase4_results.json`.
