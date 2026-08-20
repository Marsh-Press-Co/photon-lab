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

Full sweep: 1944/1944 completeness-ledger records, 6225.3s (103m45s) —
about 15% over the ≈90-minute estimate (§ Cost). Trust suite re-verified
41/41 (`--only 12346789`) immediately before the run; zero `lab/` file
touched throughout. One implementation bug self-caught before any result
was produced: the first execution crashed with `KeyError: 'n401'` —
exp-049's own committed `results.json` uses the field name `c401` for this
quantity, not this module's internal `n401` key. Fixed pre-result (no
science number was ever generated by the buggy version); full sweep
re-run clean.

**True total compute cost, disclosed (Red Team mandatory-fix 2,
THERMODYNAMICS' own catch, independently re-derived from `git log` by Red
Team, not merely asserted):** the discarded first (buggy) run's crash site
sits *after* both full 972-call sweeps complete — `main()` calls both
`sweep()` invocations before the regression-anchor comparison loop that
raised the `KeyError` — so the discarded attempt almost certainly paid
close to the full compute cost before crashing. Git commit-timestamp gaps
corroborate this closely (implementation→bugfix: 6287s; bugfix→results:
6203s, matching `elapsed_s` to within ordinary commit overhead). **True
total cost across both attempts is ≈12,490s (≈208 minutes), not the
disclosed single-run figure of 6225.3s (≈104 minutes)** — the original
Results text reported only the clean second run, not the full cost of
reaching a working implementation. Non-load-bearing (no scored prediction
references runtime), but a genuine disclosure gap, corrected here per
house discipline. Forward guidance for future geometry-parameterized
cycles (THERMODYNAMICS' own recommendation): persist a partial/crash-state
timing record from process start, not only the final successful run's
`elapsed_s`. The attributed root cause (`_G_for_g`'s lack of a `_Gcache`-
style memoization, unlike exp-042's own cached `_G_for`) is real and
uncorrected — call counts are identical to exp-049's own (972/geometry),
so the missing cache is pure avoidable overhead, not a lower call-count
trade-off (the `design_geometry.py` docstring's original justification was
itself wrong and has been corrected in-line, per the same mandatory fix).

| ID | Outcome | Measured |
|---|---|---|
| P-NCONV27-0 | **CONFIRMED, all 3 functions independently** | `incoherent`, `incoherent_corrected`, `coherent` each match exp-049's own committed `per_cell_summary` to **0.0 relative error** (bit-exact) on every `c41`/`c401`/`converged_value`, all 36 rows per function, zero `nstar` mismatches — including the two functions (`incoherent`, `coherent`) exercising the geometry-dict generalization of the obliquity-on-E convention for the first time in this program's history (THERMODYNAMICS' Phase-2 request, mandatory-fix 5) |
| P-NCONV27-1 | **CONFIRMED** | global max n\* across all 108 GEOM78 combinations = **81**, zero NOT-CONVERGED-WITHIN-RANGE — matches exp-049's own A=752 maximum exactly |
| P-NCONV27-2 | **REFUTED** | **3 total violations, not the predicted ≤1.** The 1 pre-registered exempt violation (750nm, θ₀=40°, FWHM=20°, `incoherent_corrected`, tier 0→1) occurred exactly as Red Team's own pre-Phase-4 check found (`phase2_redteam_audit.md` Attack 3) — but **2 additional, NON-exempt violations occurred at 600nm** (θ₀=36° and θ₀=40°, FWHM=20°, both `incoherent_corrected`, both tier 0→1), at coordinates neither Attack 1's Nyquist diagnostic nor Attack 2's grating-lobe-truncation mechanism flagged — see Reading, below |
| P-NCONV27-3 | **CONFIRMED** | 6/9 FWHM=20° coherent cells have n\*>41 (inside the predicted 6–9 band, below the 8/9 central estimate) |
| P-NCONV27-4 | **CONFIRMED** | 6/9 FWHM=20° `incoherent_corrected` cells have n\*>41 (inside the predicted 3–7 band, above the 5/9 central estimate) |
| P-NCONV27-5 | **CONFIRMED** | pooled FWHM≤10° convergence at n=41 = **100%** (81/81) — matches exp-049's own result exactly |
| P-NCONV27-6 | **CONFIRMED** | sharpest-stakes cell (750nm/38°/FWHM=2°/`incoherent_corrected`): n\*=41 (unchanged), relative move at convergence = **0.0%** |
| P-NCONV27-6b | **CROSS-VALIDATED** | GEOM78 converged value = **+1.4646953954144948×10⁻⁴** (headroom vs `C_THR`: 3313.7%) vs GEOM_EXP042_OLD's **−4.006497410421138×10⁻³** (headroom 24.8%) — a **27.35× magnitude collapse and a sign flip**. Phase 4's own independent computation agrees with Red Team's own rounded pre-check (+1.465×10⁻⁴) to **0.021% relative** — the two independent implementations (Red Team's scratch code, the Director's own committed `design_geometry.py`) cross-validate each other |
| P-NCONV27-7 | **CONFIRMED** | coherent worst-cell move at GEOM78 = **4.742%** (inside [3.0%,6.5%]), at (450nm, 36°, FWHM=20°) — **not** one of the three truncation-governed cells named in P-NCONV27-3's disclosure (those are 750nm-only); the worst-case coherent cell is governed by the same period-growth-adjacent mechanism as at A=752 (exp-049's own worst cell was also 450nm/36°/FWHM=20°), not by truncation |

**Tally: 7 CONFIRMED, 1 REFUTED (P-NCONV27-2), 1 CROSS-VALIDATED
(informational, P-NCONV27-6b — not scored confirm/refute by its own
design). 0 unresolved.**

## Reading

The headline instrument-fidelity question (P-NCONV27-1) holds cleanly:
n=41 stays safe for the same 100/108 GEOM78 combinations as at A=752, the
global maximum n\* is unchanged at 81, and every prediction Red Team's own
mandatory-fix docket touched with a numeric band (P-NCONV27-3/4/5/6/6b/7)
lands inside its committed band, several matching exp-049's own A=752
figures almost exactly (P-NCONV27-1, -5, -6's n\*=41-unchanged result).

**But P-NCONV27-2 — the prediction Red Team's own pre-Phase-4 live check
most directly informed — is REFUTED, honestly and informatively, not
narrowly.** Red Team's pre-check ran only the two 750nm coordinates its own
two independent mechanisms (Nyquist-sampling proximity, grating-lobe-
replica truncation) flagged, and found exactly 1 violation there — matching
its own central estimate precisely. Phase 4's full 108-combination sweep,
which Red Team's own pre-check never ran in full, finds that violation
plus **two more, at 600nm, in the same function** (`incoherent_corrected`)
but at coordinates *neither* mechanism examined. This is the single most
informative structural result of this cycle: **the pre-registered
exemption zone was correctly identified for the mechanism it was built
from, but the mechanism itself does not exhaustively characterize where
tier instability occurs at GEOM78** — a genuinely open question, not
resolved by this cycle's own design.

A candidate mechanism, disclosed here as an observation Phase 5 should
scrutinize, not asserted as established: all three violating cells
(750°/40°/600nm/750nm at FWHM=20°, `incoherent_corrected` only) share
`|C|` values of order 10⁻⁴, **two to three orders of magnitude below
`C_THR=0.005`** — deep inside the convergence criterion's own "exempted"
regime (§Setup: the relative clause is exempted whenever `|C(2n)|<C_THR`,
leaving only the absolute-tolerance bound `ABS_TOL=5×10⁻⁴` to govern
convergence). At (36°,600nm), `c41`=+3.17×10⁻⁴ and the converged value is
−3.69×10⁻⁴ — a sign flip inside a magnitude range where the exemption
formula's own ABS_TOL bound (5×10⁻⁴) is comparable to the values
themselves, not small relative to them. This resembles, structurally, the
same "spurious behavior near `|C|≈0`" regime QUANTUM OPTICS' own
Iteration-26 finding named for a *different* function (the P-NCONV26-2
correlation metric) — but this cycle's own exemption fix (designed for
that metric, not for `nstar` computation directly) does not obviously
prevent a genuinely small-signal cell from needing extra doubling steps to
settle near a sign crossing. **Resolved at Phase 5 (Red Team's audit, adjudicating a genuine PHOTONICS-
vs-QUANTUM/EM disagreement by direct execution, not by seat count — full
record: `phase5_redteam_audit.md` Attack 1):** the H-vs-E propagator
convention is **not** the origin of the pathology. `beam_divergence_
incoherent` (the strictly-non-negative `|E|²` convention, PHOTONICS' own
Phase-5 candidate for immunity) shows the **identical qualitative near-zero
instability** at all three violating coordinates — including an outright
sign flip at 36°/600nm — and at a fourth, previously-masked cell
(450nm/38°, whose `nstar` was already 81 at both geometries so its own
41→81 tolerance breach never registered as a tier "violation"). Both
conventions execute a genuine, fast-settling (converged by n≥161, stable to
9 significant figures) destructive-interference null of the same
underlying FWHM=20° angular integral at the T21 fringe scale; which
convention's n=41→81 step happens to cross the fixed `ABS_TOL=5×10⁻⁴` line
is a **reproducible ~1.9–2.3× magnitude coincidence** (`incoherent_
corrected`'s step is consistently 1.9–2.3× larger than `incoherent`'s at
the same coordinates), not a qualitative difference in kind. **This
narrower asymmetry is itself new, real, and unexplained** — queued as
Iteration 28's top-ranked priority, below — not resolved by this cycle or
its own Phase-5 audit.

**A second, separately disclosed risk (Red Team mandatory-fix 3, VISION
SCIENCE's own Phase-5 finding, independently reproduced from both
committed `results.json` files):** n-convergence CONFIRMED at a cell
certifies only its numerical stability under quadrature refinement — it
licenses no inference about the physical value's stability under a
geometry change, however small. This distinction is not cosmetic:
P-NCONV27-6/6b's own sharpest-stakes cell (750nm, θ₀=38°, FWHM=2°,
`incoherent_corrected`) sits, at GEOM78, almost exactly on a fringe
zero-crossing (the 27.35×-collapse, sign-flip, 3313.7%-headroom finding
above) — but its immediate 2°-step grid neighbors, already present in this
cycle's own committed 108-row table, tell a different story:

| θ₀ | A=752 converged `C` | A=724 converged `C` |
|---|---|---|
| 36° | +1.7045681500076344×10⁻³ | **−5.450293920551405×10⁻³ — \|C\| > C_THR=0.005** |
| 38° | −4.006497410421138×10⁻³ (headroom 24.8%) | +1.4646953954144948×10⁻⁴ (headroom 3313.7%) |
| 40° | −2.9086034530989564×10⁻³ | **+6.498600122495588×10⁻³ — \|C\| > C_THR=0.005** |

At A=752, all three angles stayed comfortably below `C_THR`. At A=724, the
tracked cell (38°) is the deepest null of a fringe that **exceeds threshold
outright at both immediate 2°-step neighbors** — a threshold crossing that
did not exist in this angular family's raw reading at the old geometry. No
prediction this cycle scores is affected (P-NCONV27-6/6b are both correctly
scored at the 38° cell they name), but any *future* citation reading
"GEOM78's sharpest-stakes cell: 3313% headroom" in isolation would be
citing the deepest point of a fringe that breaches threshold one grid-step
away on either side — a materially sharper risk than the single-cell
headroom-swing finding alone conveys. **Standing rule, adopted here**: any
future near-boundary headroom citation at any geometry must be re-measured
at its own citation's actual geometry and checked against its own immediate
angular neighbors, not read from a single tracked cell in isolation.

**What this changes going forward:** GEOM78's own n=41 default is
known-safe for the same 100/108 combinations as A=752's (matching
exp-049's own headline finding almost exactly), closing the follow-up
trigger PLAN.md queued at Iteration 26's close — no future near-boundary
citation at GEOM78 needs to defer to a re-run before using n=41 outside
the FWHM=20° `incoherent_corrected`/`coherent` regime. Inside that regime,
n≥81 is required (as at A=752), and three specific cells (36°/40°/750nm
and 36°/40°/600nm, `incoherent_corrected`) show tier instability whose
mechanism is not yet identified — a genuinely new, narrower open question
than the one this cycle set out to answer, not a re-opening of P-NCONV27-1's
own headline result. **Updated at Phase 5** (see below): the mechanism is
now substantially, though not completely, resolved — the H-vs-E convention
is not its origin; a reproducible ~1.9–2.3× magnitude asymmetry between the
two conventions' own quadrature-refinement steps is real and remains
unexplained.

---

## Phase 5 (six fresh blind seats, then Red Team audit)

**Six blind reviews**: PHOTONICS, MATERIALS, ELECTROMAGNETISM — **PROMISING**
(3); QUANTUM OPTICS — **PROMISING overall, with the specific H-vs-E-
convention mechanism it proposed RULED OUT** by its own re-execution;
THERMODYNAMICS, VISION SCIENCE — **PARTIAL** (2), each finding a real,
same-shift-fixable disclosure gap adjacent to, not inside, this cycle's own
scored predictions. PHOTONICS proposed a specific mechanism for
P-NCONV27-2's REFUTAL (the corrected convention's signed cross-term is
uniquely prone to near-zero sign crossings, unlike `incoherent`'s strictly
non-negative `|E|²`); QUANTUM OPTICS and ELECTROMAGNETISM, independently,
each re-ran `incoherent` at the same coordinates and found it shows the
identical qualitative pathology, just narrowly escaping `ABS_TOL`.

**Red Team's final audit (everything: results + all six reviews):
PROMISING, no Checkpoint criterion fires.** Resolved the PHOTONICS-vs-
(QUANTUM+EM) disagreement by direct execution, not seat-counting (running
`beam_divergence_incoherent` itself through the full doubling series at all
three violating coordinates plus a fourth, previously-masked cell,
450nm/38°): QUANTUM's ruling is correct — both conventions share a genuine,
fast-settling destructive-interference null of the same angular integral;
which one trips the fixed tolerance is a reproducible ~1.9–2.3× magnitude
coincidence, not a difference in kind. Independently re-derived
THERMODYNAMICS' true-cost finding from raw `git log` timestamps (confirmed:
≈208 total minutes across both the discarded buggy run and the clean
re-run, not the disclosed ≈104) and VISION's threshold-breach finding
directly from both committed `results.json` files (confirmed exact, digit
for digit). All three findings are real; none is load-bearing to any of
this cycle's eight scored predictions; all three are same-shift,
zero-new-computation fixes, applied above (Reading/Results sections) and in
`design_geometry.py`'s corrected `_G_for_g` docstring. **Checkpoint
disposition: all five criteria explicitly checked, none fires** — in
particular criterion 4 (program-integrity drift), scrutinized directly
against THERMODYNAMICS'/VISION's findings, does not fire: neither finding
is an unfalsifiable claim or a quietly-dropped constraint (this cycle
claims no constraint-3/4 verdict to drop), and this program's own hardened
R4 tripwire (a third consecutive post-R4 non-reproducing headline figure)
is not triggered — every number checked in the Phase-5 audit reproduced
exactly. **Verdict: PROMISING.** Full record: `phase5_redteam_audit.md`;
all six blind reviews at `phase5_review_*.md`.

**No new numbered live thread opened.** Red Team's own recommendation,
adopted: the near-|C|≈0 tier-instability finding and VISION's adjacent-cell
threshold-breach finding are both real and reproducible, but both are the
same underlying T21 edge-diffraction-fringe mechanism now shown to also
govern `beam_divergence_*`'s own integrated quantity at a second geometry —
not a new physical phenomenon — and both are concretely, cheaply testable
(Iteration 28's own top-ranked priority) rather than standing mysteries.
Folded into T21's existing LOGBOOK entry instead.

**Ranked priorities for Iteration 28** (Red Team's synthesis, reconciling
all six seats): (1) a phase-corrected difficulty-predictor test across the
full FWHM=20° grid, including `|C(n=81)|/ABS_TOL` as a regressor, to derive
the unexplained ~1.9–2.3× asymmetry (near-unanimous top pick — PHOTONICS,
ELECTROMAGNETISM, MATERIALS, QUANTUM OPTICS, this audit); (2) a sub-degree
angular sweep across 36°–40° at 750nm/FWHM=2° at GEOM78 (VISION), now
concretely motivated by the adjacent-cell threshold-breach finding; (3) the
standing genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry — now the
sole remaining uncharacterized uncertainty source on this program's
sharpest near-boundary cell family; (4) MATERIALS' own fixed-absolute-
thickness `graded_black_shell` variant, 9+ iterations deferred; (5)
THERMODYNAMICS' overdue `h_eff` re-derivation; (6) low-priority: cache
`_geom_derived`/`_G_for_g` before any future geometry-parameterized cycle.
