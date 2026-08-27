# exp-078 — T28 Y-Wall (Transverse-Normal) Echo: Closed-Form Period Pre-Screen

**Panel Iteration 55.** Lead: PHOTONICS (by rotation). Director synthesis
post Phase 2 (five blind critiques + Red Team's Phase-2 audit, verdict
**PROCEED-WITH-MANDATORY-FIXES, 7-item docket, ALL 7 items ADOPTED, ZERO
overridden** — full record in `phase1_proposal.md`, `phase2_critique_
{materials,em,thermodynamics,quantum,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`). Phase 5: six blind reviews (unanimous PARTIAL) +
Red Team's final audit (PARTIAL, one substantial extension — see below).

## Mandate

PLAN.md's Iteration-55 queue, Tier 0 item 2 (PHOTONICS #1, EM #1,
independently convergent at exp-077 Phase 5): a closed-form, zero-FDTD
period pre-screen of a coherent echo off a wall whose **normal is
transverse (y)** to the beam's principal (x) propagation axis — a
genuinely untested mechanism class, since every prior T28 echo model
(exp-075/076/077) tested only the **x-normal** wall, and none of them ever
checked `clear_span_y` (0/40/0 across `C40`/`G40`/`C80`), the parameter
that actually tracks T28's dominant `PAIR_PAD` signal.

## Hypothesis

A wave from the source aperture's near edge (`y_lo`), reflected off its
own nearby y-wall (weighted by `r(theta;ABSORB)` — the *identical*
transfer-matrix reflectance already gated for the x-wall, since
`Sim._damping` applies one shared ramp to all four domain edges), produces
a coherent interference pattern at the observation plane whose period
should match T28's established periodicities (`P*≈2.84°`/`4.2–4.6°`) if
this is the real mechanism. Unlike the x-wall case, mirroring the source
*in y* touches the aperture's own driven-phase coordinate, so the clean
two-plane-wave reduction that works for the x-wall does not transfer — the
model instead reduces to a single edge point vs. its own image
(edge-dominance idealization), a genuinely different derivation, not a
coordinate swap.

## Setup

Reuses committed machinery programmatically throughout (R4 discipline):

- **Geometry**: `experiments/065-.../design_geometry.py::CONFIGS`.
- **Reflectance/gates**: `experiments/075-.../boundary_reflectance.py`
  (`n_profile_exact`, `reflection_coefficient`, the three sanity/passivity
  gates).
- **Period fitting**: `experiments/069-.../run.py::_free_period_search`.
- **Real data**: `experiments/076-.../results.json::headline` (31 angles,
  36–42°, 0.2° step, 600nm, settled `STEPS=2800`).
- **Pre-registered band**: Test A (period) only, reused verbatim from
  exp-075/077 (`rel_dev` ≤0.30 SUPPORT / >1.00 REFUTE); no Test B (no
  full field model built — this is explicitly a pre-screen, not a
  propagator).

## Result

**Official Combined result (Phase 4, frozen predictions confirmed
exactly): INCONCLUSIVE, Test-A-only, 0/3 comparisons SUPPORT, 0/3
REFUTE**, under the geometrically corrected `90−θ_beam` incidence-angle
convention. The as-filed Phase-1 proposal's apparent 2/3-SUPPORT reading
was entirely an angle-convention bug (raw `θ_beam` fed to the reused
x-wall reflectance function, when `90−θ_beam` is the correct angle for a
y-stratified wall) — independently caught by three blind critics
(MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS) and confirmed a fourth way
by Red Team's own from-scratch re-derivation. `PAIR_PAD` (T28's actual
dominant empirical target) is essentially unmoved by the fix
(`rel_dev` `0.3136→0.3021`) and was never close to SUPPORT under either
angle convention. A fresh, house-standard 20,000-trial null-calibration
control confirms none of the corrected numbers are statistically
distinguishable from pure noise (`p=0.13`–`0.40` per target; Fisher-
combined omnibus `p=0.148` period / `p=0.632` R²).

**Phase 5 addendum — the cycle's most consequential finding, net of
everything (Red Team's final audit, confirming and extending
ELECTROMAGNETISM's blind review):** even the `90−θ_beam` convention Phase
2/3/4 adopted is **not** the physically rigorous incidence angle for this
specific model's own point-source (Euclidean-distance image) construction
— it is the correct angle for a *plane-wave*, whole-aperture-steered
picture, a representation this model already abandoned (§3.2's own
argument for why the x-wall formula doesn't transfer by coordinate swap).
The rigorous, per-config-constant stationary-phase bounce angle
(`atan(D_SP/(OBJ_Y+y_lo))`, 13.7°–15.0° from the y-wall's own normal,
**independent of the swept beam angle**) collapses `Delta_phi_self(theta)`
to a perfectly flat curve for every config (`ptp=0.000°`, verified to
float precision, `ss_tot` ratio to real data's own scale: `5.9×10⁻²⁷`).
**This is a decisively stronger negative result for this specific
edge-image/single-near-wall reduction than the official INCONCLUSIVE** —
not a wrong period, the absence of any predicted oscillation at all — though
it is not filed as a formal REFUTE (the pre-registered band presupposes
two comparably-determined nonzero periods, a precondition this zero-
amplitude result does not meet). **The frozen Phase-4 numbers are not
edited or superseded by this finding** — they remain a correct,
independently-reproduced computation of exactly what the `90−θ_beam`
convention predicts; the Phase-5 finding is a deeper characterization of
the same reduction, not a correction of a wrong number.

## Learned

1. **The y-wall echo mechanism class is not closed by this pre-screen.**
   Neither angle convention's result rules out the class as a whole: the
   full, non-edge-reduced y-mirrored aperture sum and the far-edge/
   far-wall image pair both remain untested, and `phase1_proposal.md`'s
   own stationary-phase argument leaves open whether the flat,
   zero-amplitude result generalizes from the single-edge reduction to
   the full sum.
2. **A second, deeper angle-convention error can hide inside a
   "corrected" fix.** The as-filed bug (raw `theta` vs `90-theta`) and
   the deeper representational-mismatch bug (plane-wave angle plugged
   into a point-source geometry) are two different defects, at two
   different levels of the same model — catching the first did not
   automatically catch the second. Both were found only because
   independent, blind seats kept re-deriving the physics from primitives
   rather than trusting the prior phase's own "corrected" label.
3. **A numerically-flat array is not the same as an exactly-zero one**,
   and a period-search R² computed against it can misreport a spurious
   near-perfect fit. `SS_TOT_DEGENERATE_FLOOR` (added this cycle,
   `y_wall_prescreen.py::free_period_with_widening`) generalizes this
   guard for any future call site in this file.
4. `PAIR_PAD`'s own Test-A period is **structurally forced** to equal
   `C40`'s own individual period whenever `ABSORB` is shared between the
   paired configs (VISION's Phase-5 finding, independently re-derived
   and confirmed by Red Team via a trig identity) — a real methodological
   limitation of this comparison for T28's actual dominant target,
   independent of which angle convention is used.
5. **A period-only pre-screen cannot, on its own, license building a
   full coherent field model** — this cycle's own honest bottom line
   (per its own Phase-1 self-score, corrected at Phase 3/4/5) is that
   the evidence for building the full y-mirrored propagator is now
   substantially weaker than the as-filed document argued, not stronger.

## Next

Reconciled Iteration-56 ranking (Red Team's Phase-5 final audit, 4 tiers,
13 items; `phase5_redteam_audit.md` §7 has the full text). **Tier 0 — zero
FDTD, run as one batch:** (1) does the flat/zero-amplitude result (Phase 5
addendum) generalize from the single-edge reduction to the full,
non-edge-reduced y-mirrored aperture sum — the single highest-value item
on the board; (2) this cycle's own record-hygiene docket (done, this
shift); (3) retarget the still-unexecuted realizable-admittance (`μ_r=1`)
refit at the x-wall's two-wall model, not the y-wall (MATERIALS' own
re-ranking — the y-wall's period is admittance-choice-invariant,
Pearson r>0.9997); (4) wire the Fisher-combined omnibus statistic into
the null-calibration record (done, this shift); (5) gate the already-
collected 750nm two-wall x-wall spot-check (the single oldest deferred
item on the whole T28 board); (6) the `ss_tot`-scale sanity guard (done,
this shift); (7) pre-register the amplitude/normalization convention for
any future Test-B build, before it is built. **Tier 1 — cheap FDTD:**
(9) the full-width non-aliased `G40` leg (now deferred THREE consecutive
cycles); (10) broadband pulsed reflectance spectroscopy of the `ABSORB`
boundary. **Tier 2 — the standing charter-relevant test:** (11) whether
`PAD`-sensitivity survives with a real absorbing article loaded — now
deferred THREE consecutive cycles, the single most overdue item on the
whole T28 board, should not be deferred a fourth time without an explicit
reason. **Tier 3 — governance:** (12) Checkpoint criterion 2 (mechanism-
class boundary) ruled NOT YET RIPE this cycle — at least four concrete,
unpriced items remain open. Full record: this directory; LOGBOOK.md
Iteration 55; PLAN.md's own Iteration-56 queue.
