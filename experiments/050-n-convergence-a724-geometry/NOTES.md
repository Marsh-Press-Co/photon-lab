# exp-050 — The n-Convergence Audit at the A=724 Fallback Geometry

*Panel Iteration 27. Lead: MATERIALS & METAMATERIALS (rotation), executing
Red Team's Iteration-26 Phase-5 ranked #1 item and MATERIALS' own Phase-2
Attack-1 follow-up trigger on exp-049: exp-049's n\* findings are scoped to
exp-042/046's A=752/NY=1584 geometry only and must not be cited as
governing exp-048's actual A=724/NY=1528 fallback geometry without this
cheap re-run. Instrument/model-fidelity cycle, Iteration-20/22/23/26 class.
T1 escape route: NONE. No constraint-3/4 verdict issued or implied.*

## Hypothesis

exp-049 (Iteration 26) formally convergence-tested `gaussian_angle_weights`'s
quadrature order `n` for all three committed `beam_divergence_*` functions,
finding a global maximum n\*=81 across the full 108-cell-function grid — but
**only** at exp-042/046's own hardcoded module-global geometry (`A=752`,
`NY=1584`). exp-048 (Iteration 25) already established `GEOM78` (`A=724`,
`NY=1528`) as the geometry any actual near-boundary constraint-3 or
realizability citation would use. This audit reuses exp-049's own
Phase-3-corrected machinery unmodified (`N_SERIES`, the exemption-not-floor
convergence criterion, the 36-cell grid, all three function definitions) but
generalizes the three `beam_divergence_*` functions to take a geometry
dict — following exp-048 Block B's own `_geom_derived`/`field_and_h(θ,λ,g)`
precedent — and re-runs the identical audit at `GEOM78`, with a mandatory
regression anchor against `GEOM_EXP042_OLD` checked first.

**Physical prior** (§2.4 of `phase1_proposal.md`, LOGBOOK's own T21
fringe-period model reused by analogy, twice-compounded per idealization 3):
the fringe period `P(θ)=λ/(A·cosθ)` grows uniformly ~3.87% at `A=724` vs
`A=752` — samples-per-period at n=41 should improve (never worsen) almost
everywhere, so n\* values should stay the same or shrink at GEOM78, never
grow. **Corrected at Phase 3** (Red Team's Attacks 1–3, below): this
directional argument is magnitude-only and does not account for phase/
aliasing-boundary proximity or absolute grating-lobe-replica position —
two independent mechanisms (Nyquist-sampling proximity, aperture truncation
of an A-independent grating-lobe replica) both flag the same two
coordinates, 750nm/θ₀∈{38°,40°}/FWHM=20°, as elevated-risk, and Red Team's
own pre-Phase-4 live check already found one real, measured tier violation
there (see Phase 2/Red Team disposition, below) — a corrected, narrower,
still-falsifiable prior, not the original uniform-improvement claim.

## Phase 2/Red Team disposition

Five blind critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE): unanimous **support-with-changes**. Red Team's
sequential audit (everything): **PROCEED-WITH-MANDATORY-FIXES**, 7 numbered
attacks, 5-item mandatory-fix docket, all adopted, none overridden — see
`phase2_redteam_audit.md` and `phase3_synthesis.md` for the full record.

**Load-bearing finding, no blind seat caught it whole**: PHOTONICS and
ELECTROMAGNETISM independently flagged the same underlying concern (the
period-growth argument is magnitude-only, not phase-aware) and QUANTUM
independently flagged a structurally different mechanism (grating-lobe
replica truncation, A-independent absolute position vs. a shifting taper
zone) — Red Team resolved both to the *identical two coordinates*
(750nm/θ₀=38°, 750nm/θ₀=40°, both FWHM=20°) and then **ran the proposal's
own machinery, built from prose since no code yet existed, through the full
doubling series at those coordinates before this synthesis** — finding one
real, measured tier violation: (750nm, θ₀=40°, FWHM=20°,
`incoherent_corrected`) moves from n\*=41 at A=752 to n\*=81 at A=724, in a
function neither individual mechanism alone had specifically flagged. The
design below (P-NCONV27-2, amended) is the corrected Phase-3 design, not
the original Phase-1 proposal (preserved unedited at `phase1_proposal.md`
per this program's "flag, don't rewrite" convention). **Red Team's own
numbers are a disclosed pre-check, not a substitute for Phase 4** — see
`phase3_synthesis.md`'s "A note on Red Team's own pre-Phase-4 computation."

## Setup

- **Zero new FDTD calls.** Pure `numpy`. New module
  `experiments/050-.../design_geometry.py` generalizes exp-042's three
  `beam_divergence_*` functions to take a geometry dict `g` (reusing
  `gaussian_angle_weights` and `aperture_profile` unmodified — neither
  touches geometry), following exp-048 Block B's `_geom_derived`/
  `_src_amp(θ,k,gd)` pattern. Two geometry dicts: `GEOM_EXP042_OLD`
  (`NY=1584, OBJ_Y=792, A=752, GUARD_OUT=185`, the regression anchor) and
  `GEOM78` (`NY=1528, OBJ_Y=764, A=724, GUARD_OUT=186`, the scored target),
  both reproduced verbatim from `experiments/048-evidentiary-chord-closure/
  design_geometry.py:145-158`.
- **Grid:** θ₀∈{36,38,40}°, FWHM∈{2,5,10,20}°, λ∈{450,600,750}nm (36 cells,
  unchanged) × 3 functions = 108 cell-function combinations, evaluated at
  BOTH geometries (216 total cell-function-geometry combinations).
- **N_SERIES** = (41, 81, 161, 321, 641, 1281, 2561, 5121), **N_REGRESSION**
  = 401 — identical to exp-049, reused unmodified.
- **Convergence criterion** — identical to exp-049's Phase-3-corrected
  design (exemption, not floor): for a doubling step n→2n,
  `Δabs(n)=|C(2n)−C(n)|`; `Δrel(n)=100·|C(2n)−C(n)|/|C(2n)|` **if**
  `|C(2n)|≥C_THR=0.005`, **else the relative clause is exempted** and the
  step is judged on `Δabs(n)≤ABS_TOL=5×10⁻⁴` alone. Trustworthy n\* =
  smallest N_SERIES entry where two consecutive doublings both converge.
- **Mandatory regression anchor (P-NCONV27-0, checked first — see Phase 3
  amendment 5):** the new geometry-parameterized functions, called at
  `g=GEOM_EXP042_OLD`, reported PER FUNCTION against exp-049's own
  committed `results.json` `per_cell_summary` (all 108 rows): `c41`,
  `c401`, `nstar`, `converged_value` must match to ≤10⁻⁹ relative
  (`c41`/`c401`/`converged_value`) and exact integer identity (`nstar`).
  `incoherent_corrected` reproduces already-precedented machinery
  (exp-048 Block B's own `field_and_h` generalization); `incoherent` and
  `coherent` are the first-ever geometry-dict generalization of the
  obliquity-on-E convention (`_G_for`) anywhere in this program's history —
  reported as a distinct evidentiary claim, not pooled.
- **Completeness ledger:** one entry per (cell, function, geometry,
  N_SERIES-entry) — 36×3×2×8 = 1728 doubling evaluations, plus
  36×3×2 = 216 n=401 checks = **1944 expected records**.

## Falsifiable predictions — FROZEN before any code runs (Phase-3-amended)

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-NCONV27-0** | **Regression anchor, checked first.** The parameterized functions at `g=GEOM_EXP042_OLD` reproduce exp-049's own `per_cell_summary`, reported per function | ≤10⁻⁹ relative on every `c41`/`c401`/`converged_value`; exact integer match on every `nstar`, all 108 rows, for each of the 3 functions independently | any row mismatches beyond float noise, in any function ⇒ no GEOM78 number in this audit is trusted until resolved |
| **P-NCONV27-1** | The global maximum n\* across all 108 GEOM78 cell-function combinations does not exceed exp-049's own A=752 maximum | max n\* ≤ **81** | any combination needs n\*>81, or is flagged NOT CONVERGED WITHIN RANGE |
| **P-NCONV27-2** | *(Amended, Attacks 1+3+4.)* Outside a pre-identified 6-combination exemption zone, no cell-function combination needs a strictly larger N_SERIES tier at GEOM78 than at A=752. Exemption zone (named here, before Phase 4 runs): all three functions × {(750nm,θ₀=38°,FWHM=20°), (750nm,θ₀=40°,FWHM=20°)} — the two coordinates where the samples-per-period diagnostic crosses the integer boundary 1.0 between A=752 and A=724 (Attack 1's own computed table) | **0 of the other 102** combinations move to a strictly larger tier; **at most 1 of the 6** exempted combinations may move to a strictly larger tier without falsifying (central estimate: exactly 1, per Red Team's own pre-check) | any of the 102 non-exempted combinations moves to a larger tier, or more than 1 of the 6 exempted combinations does |
| **P-NCONV27-3** | *(Carries an inline disclosure, Attack 2.)* The coherent-function FWHM=20° under-convergence pattern (exp-049: 8/9 cells fail n=41) reproduces at GEOM78, same direction, comparable count. **Disclosed: 3 of these 9 cells (750nm/θ₀∈{36°,38°,40°}) are governed by a distinct mechanism at GEOM78 — the n=41 grating-lobe replica falls partly or fully outside the source aperture's physical support (truncated to 0 at 38°/40°, amplitude 1.0→0.34 at 36°) — not the period-growth story; their direction is not predicted by §2.4 alone** | **6–9 of 9** FWHM=20° coherent cells have n\*>41, central estimate 8/9 | ≤2/9 fail |
| **P-NCONV27-4** | `incoherent_corrected`'s FWHM=20° residual failure count (exp-049: 5/9) reproduces in a comparable range | **3–7 of 9** FWHM=20° `incoherent_corrected` cells have n\*>41, central estimate 5/9 | 0/9 or 9/9 |
| **P-NCONV27-5** | FWHM≤10° stays universally, cleanly converged at n=41 (exp-049: 81/81) | **≥95%** of the 81 FWHM≤10° cell-function combinations converged at n=41 (central estimate 81/81, 100%) | <70% pooled |
| **P-NCONV27-6** | The GEOM78 analogue of exp-042's sharpest-stakes near-boundary cell (750nm, θ₀=38°, FWHM=2°, `incoherent_corrected`) stays converged at n=41, no flip. Disclosed: FDTD-unvalidated here; LOGBOOK's T24 boundary systematic was measured at A=752, carried over by analogy only | n\*=41 (unchanged), converged-value relative move ≤**1%** | n\*>41, or relative move >5% |
| **P-NCONV27-6b** | *(New, Attack 6/mandatory-fix 4.)* The sharpest-stakes cell's actual converged `|C|` value at GEOM78, reported against `C_THR=0.005` and against exp-049's own 24.8%-headroom figure at A=752 — an amplitude/headroom disclosure, not a pass/fail band. Red Team's own pre-check: −4.007×10⁻³ at A=752 (24.8% headroom) → a claimed +1.465×10⁻⁴ at A=724 (a ~27× collapse and sign flip, headroom improving to ~3314%), attributed to a genuine fringe-phase zero-crossing, not a computational artifact | Phase 4's own independent computation is reported as-measured; consistency with Red Team's pre-check number (≤1% relative, since both use the identical corrected function) is itself checked as a cross-validation of Red Team's own arithmetic | Phase 4's own number disagrees with Red Team's pre-check by >1% relative ⇒ one of the two independent implementations has a bug, investigated before this prediction is scored |
| **P-NCONV27-7** | *(Carries the same Attack-2 disclosure as -3.)* The coherent-function worst-cell relative move at converged n\* stays close to exp-049's own 4.4747% figure — the mechanism is primarily set by the aperture's own grating-lobe structure, and the aperture geometry shifts only ~3.7–3.9%. **Disclosed: the worst cell may or may not be one of the 3 truncation-governed cells named in P-NCONV27-3 — Phase 4 reports which** | worst coherent move at GEOM78 in **[3.0%, 6.5%]**, central estimate ≈4.5% | <1.5% or >10% |

**What would make this cycle a failure, stated plainly:** if P-NCONV27-2
falls the way its own hard-falsification band names (any of the 102
non-exempted combinations moves to a larger tier, or more than 1 of the 6
exempted combinations does), the corrected, narrower period-growth argument
this synthesis adopted is itself wrong, not just under-scoped — a real,
pre-registered way for this cycle to lose, matching exp-049's own
convention. **Note, disclosed in advance**: Red Team's own pre-check
(`phase2_redteam_audit.md`, Attack 3) already found exactly 1 of the 6
exempted combinations violating — if Phase 4's own independent
implementation reproduces that exact count, P-NCONV27-2 is scored
CONFIRMED (the tight, not slack, edge of its own band), not a coincidence
requiring further comment; if Phase 4 finds a *different* count, that is
new information about either the geometry-dict generalization or Red
Team's own pre-check, investigated before scoring.

## Idealizations

1. Scope: geometry only (`half_width_factor=2.5`, `N_SERIES`, `ABS_TOL`/
   `REL_TOL`, the exemption criterion all held exactly as exp-049's own
   Phase-3-corrected design fixed them — no further tuning in scope).
2. The convergence criterion is a disclosed modelling choice, inherited
   from exp-049 (corrected once already at that cycle's own Phase 3), not
   re-litigated here.
3. The T21 fringe-period model is reused by analogy, twice-compounded:
   first (inherited from exp-049) the model was derived for
   `edge_diffraction_c_empty`, a single-angle sweep, not `beam_divergence_*`'s
   own integrated quantity; second (new this cycle) the model's own
   magnitude-level validation (exp-042, Iteration 19) was performed only at
   A=752, never separately checked at A=724 — used only directionally,
   never as a magnitude claim at the new geometry, and even the directional
   claim is now known (Phase 3, Attacks 1–3) to be incomplete on its own,
   requiring the grating-lobe-truncation mechanism (Attack 2) as a
   companion, not a substitute.
4. `GUARD_OUT` differs by 1 cell (185→186) between the two geometries, used
   verbatim from `GEOM78` as committed by exp-048, not adjusted to match.
5. Desk-only; the desk-propagator-vs-FDTD cross-check (exp-046 Block A5)
   was performed only at A=752 — GEOM78's own numbers carry no independent
   FDTD validation, at any n.
6. T24's ABSORB-boundary systematic (~+0.0070) was measured at A=752, not
   GEOM78 — its relevance to a GEOM78 near-boundary reading is carried by
   analogy only. A genuine FDTD `ABSORB` sweep at GEOM78 is out of this
   cycle's zero-FDTD scope (LOGBOOK's separately-queued item (2)).
7. Floating-point accumulation negligible (exp-049's own bound, ≈10⁻¹²
   relative at n=5121 — the smaller GEOM78 Y-domain only reduces this
   further).
8. n=401 remains a single fixed regression/reproduction value at both
   geometries, not a doubling-series member.
9. No perceptual claim; `C_THR=0.005` cited only as the pre-existing
   decision line these readings are already scored against.
10. Sign/ordering conventions are stated explicitly wherever a directional
    comparison is scored (P-NCONV27-2's own tier-index definition,
    unambiguous: "larger tier" = later position in the 8-entry `N_SERIES`
    tuple) — a direct, disclosed response to exp-049's own self-caught
    Phase-4 `predicted_difficulty_rank()` sign-inversion erratum.
11. **(New, Phase 3.)** Red Team's own pre-Phase-4 computation
    (`phase2_redteam_audit.md`) is a disclosed pre-check that informed this
    synthesis's amendments — Phase 4's official numbers are produced by an
    independent implementation (the Director's own, from this NOTES.md's
    frozen design), not copied from Red Team's scratch code; agreement
    between the two is reported as a cross-validation, not assumed.

## Cost

**New FDTD calls: 0.** Estimated wall-clock ≈90 minutes single-threaded
(§6 of `phase1_proposal.md`, Red Team-verified: doubling exp-049's own
*measured* 2743.2s), for 2× exp-049's own evaluation count (both
geometries).

---

## Results (Phase 4)

*To be filled in after `run.py` executes, in a separate commit, per house
discipline — predictions above are frozen now.*
