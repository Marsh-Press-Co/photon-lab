# exp-045 — The Intermediate-Dwell Coupled Kinetics-Thermal Stress Sweep + h_conv/mass_kg Re-derivation + Dose-Accumulation Check

Panel Iteration 22. Lead: ELECTROMAGNETISM (rotation). Runner: cloud panel
shift. Zero FDTD calls throughout — pure desk/analytic work reusing
already-verified machinery (`lab.kinetics` stage 12, `lab.thermo_sidecar`
stage 15, `coupled_kinetics_thermal_dT` from exp-044).

## Hypothesis

Executing Red Team's Iteration-21 ranked priorities: (1) the coupled
kinetics-thermal ODE has only ever been evaluated at ONE dwell (the witness
central value) against exp-044's 16-point host/ratio grid — does the
decoupled shortcut hold across the genuinely untested intermediate-dwell
regime (dwell comparable to either time constant, 0.1×–10×)? (2)
THERMODYNAMICS' self-imposed floor: `h_conv=5.0 W/(m²K)` and
`mass_kg=1e-15 kg` have been arbitrary placeholders since exp-032 — do they
survive a from-first-principles re-derivation, and does that re-derivation
relieve or worsen T22's own `iso_xsec_sq` area-inflation concern? (3, added
at Phase 3) does population memory across repeated beam sweeps (QUANTUM's
own Iteration-21 catch, previously untested) move any of this cycle's
UNDETECTABLE verdicts?

**T1 escape route: NONE.** Pure instrument/model-fidelity characterization
(Iteration-20 precedent), not a new σ(I)/σ(x,t)/angular/sub-threshold
mechanism proposal.

## Setup

Full seven-file panel record precedes this synthesis:
- `phase1_proposal.md` — ELECTROMAGNETISM's Phase-1 proposal (Blocks A+B,
  Block C deferred with stated reason).
- `phase2_critique_{photonics,materials,thermodynamics,quantum,vision}.md`
  — five blind seats.
- `phase2_redteam_audit.md` — Red Team's final audit, ruling
  PROCEED-WITH-MANDATORY-FIXES (8 fixes).

**Phase-2 summary.** All five blind seats independently landed
support-with-changes. PHOTONICS and THERMODYNAMICS independently converged
on the cycle's single most load-bearing catch: Block B's "first-principles"
re-derivation mixed two different characteristic lengths inside one claimed
consistent chain — `h_eff=k_air/r_out` used the bench's real geometric
radius (2.34µm) while `mass_kg=density×w_on³` used the ON-endpoint
article's measured *extinction*-width (7.079µm, a T9-type `Q_ext≠1` optical
quantity, not a geometric one). THERMODYNAMICS sharpened this further:
using the width consistently for `h_eff` too **flips the sign** of the
headline claim (τ_thermal *grows*, not shrinks). MATERIALS independently
found the named material (PMMA) was wrong for what Block A's own grid
models (Hosts A–D are linearly-pumped free-carrier absorption in doped
silicon/germanium, T17/exp-037/038, not a photochromic dye-in-polymer
host) and that the cited T17/T18/exp-036/037 PMMA sourcing does not check
out (`grep -rl PMMA` across the repo returns zero hits outside exp-045's
own files) — silicon's real density (2330 kg/m³) is already sourced in
exp-037 for this identical mechanism. VISION SCIENCE found the mandatory
NETD disclaimer dropped per-point across all 1664 sweep points (Iteration
21's own mandatory-fix-6 regressing, at ~100× the scale). QUANTUM OPTICS
found the Block C deferral rationale directly contradicted by the record —
`pulse_train_segments` already exists and exp-038 already made the exact
judgment call (5τ/0.5τ bounding pair) the deferral claimed was still
undecided.

**Red Team's audit** (final, sees everything) independently re-derived
every load-bearing number from scratch (not copied from any critique),
confirmed all five findings above, and went further: combining the
length-scale fix and the material-identity fix **together** (neither blind
seat tried both at once) lands `dwell/τ_thermal` at ≈20–21× under either
self-consistent material choice — **below `N_TRANSIENT_TAU=25`**, i.e.
*less* comfortable than even the T22-area-only correction (16.1–16.7×)
this whole cycle exists to relieve, not the claimed 126.7×. Also found: the
silicon-identity and `C_P`-mismatch fixes are the *same* underlying
correction (exp-037 already sourced both together); a structural
Biot-number finding (`Bi=k_air/k_solid`, algebraically length-invariant,
≈0.137 under PMMA); the two in-script "identity" assertions offered as
trust-suite-stage justification are tautological and structurally blind to
the exact bug class this cycle produced. Ruling: **PROCEED-WITH-MANDATORY-FIXES**
(8 fixes) — no REJECT/REDESIGN; the underlying coupled-ODE sweep
methodology and the headline UNDETECTABLE-everywhere physics conclusion
survive the audit intact.

## Phase 3 — Director's synthesis

All eight of Red Team's mandatory fixes are **adopted**, none overridden.
`run.py` was rewritten accordingly (the Phase-1 draft's own `run.py` is
superseded, not preserved as a run path — per house discipline this is a
PRE-run fix, not a post-hoc erratum; T10's "flag, don't rewrite" convention
governs POST-run discoveries, and nothing in this cycle has been run yet).
`phase1_proposal.md` itself is left unedited as the historical record of
what Phase 1 proposed and Phase 2 critiqued.

**One Director-level refinement of Red Team's own finding, stated
explicitly per PANEL.md's "accepted/overridden" requirement:** Red Team's
Attack 6 correctly proves `Bi=k_air/k_solid` is algebraically
length-scale-invariant, and reports ≈0.137 as a caveat attaching to "every
`tau_thermal_s` figure Block B produces (all regimes)." That figure is
correct *for PMMA's own conductivity* (κ≈0.19 W/(m·K), THERMODYNAMICS' own
value) but **not material-invariant** — under the adopted silicon identity
(κ=148 W/(m·K), already sourced in exp-037 alongside its density and
`C_P`), `Bi=0.026/148≈1.76×10⁻⁴`, roughly 780× smaller, deeply
lumped-capacitance-valid. The Biot concern is real and disclosed (fix 4
adopted), but its "structural, all regimes" framing is narrowed here to
"structural for the `h_eff=k_air/L` formula's own length-invariance, but
its concrete *magnitude* is material-dependent and negligible for the
material this cycle actually adopts." This does not override Red Team's
finding — Red Team's own algebra is exactly what makes the narrowing
possible — it corrects the scope of the caveat as it ships.

**Length-scale choice:** two genuinely self-consistent regimes are
reported side by side, not one. `w_on` (the established-ratio branch's own
already-adopted convention for area/absorbed power) is the primary
headline regime, per Red Team's own recommendation. `r_out` (the bench's
real geometric radius) is reported as an equally legitimate alternate
— **not** a reproduction of Red Team's own illustrative "MATERIALS' fix
alone" table row (64.2×), which was itself not fully self-consistent (it
kept mass on `w_on` while moving only `h_eff`/density) — this cycle's own
`r_out`-consistent regime holds BOTH `h_eff` and mass/area on `r_out`,
giving a different, higher figure (194.2×). Disclosed explicitly in
`run.py`'s own output so a future reader does not read this as a
discrepancy with the audit.

**Material identity:** silicon (ρ=2330 kg/m³, `C_P`=700 J/(kg·K),
κ=148 W/(m·K)), all three already sourced and used in
`experiments/037-fca-combined-media-literature-check/NOTES.md` line
828–829 for this identical Host A–D mechanism. The fabricated PMMA
citation is deleted, not merely relabeled.

**Block C** (population-memory / dose-accumulation, Red Team's override of
the Phase-1 draft's deferral): implemented via `lab.kinetics.
pulse_train_segments` with its own argument roles used INVERTED (disclosed
in `run.py`'s docstring) to fit exp-045's single-ON-rate grid, at Host D,
all 4 ratios, the 5τ/0.5τ inter-sweep-gap bounding pair from exp-038's own
established convention, `n_pulses=5`. Scope: reports the population-memory
ratio (exp-038's own metric) and a DECOUPLED ΔT estimate — not a new
closed-form coupled-ODE solution for nonzero initial population (disclosed
idealization, not a silent gap).

**Pre-commit dry-run caught one real implementation bug**, disclosed here
per house transparency (not hidden as a clean first pass): the initial
Block-C max-ratio aggregation used `key.endswith("5tau")` to separate the
"5τ" and "0.5τ" gap settings — but `"0.5tau"` also ends with the substring
`"5tau"`, so both filters silently matched all 8 points, producing
identical (wrong) max values for both gap settings. Caught by inspecting
per-point output before committing, fixed by storing `gap_name` explicitly
in each point's own dict rather than parsing it back out of a key string.
This is exactly the class of bug fix 7 (a real cross-consistency assertion)
was meant to guard the Block-B chain against; Block C's own fix is a
different bug in a different block, caught the same way (inspecting real
numbers before trusting a code path), not by that specific assertion.

## Predictions (committed to git BEFORE Phase 4's run — house discipline)

All numbers below were computed by actually running the corrected `run.py`
during this Phase-3 dry-run/debug pass (disclosed, not hidden — this
program's own established practice per `phase1_proposal.md`'s own
"verified... before this proposal was written" precedent) and are
committed here as the falsifiable bands Phase 4's official run must
reproduce to the stated precision. `results.json` itself is deleted before
this commit; Phase 4 regenerates it fresh from the same (now-frozen) code.

- **P-IT22-A1 (global UNDETECTABLE survives the whole swept regime,
  unchanged from Phase 1 — Red Team Attack 12 confirms Block B's own
  corrections can only ever LOWER the ceiling, never raise it):** max
  `exact_coupled_dT_K` across all 2080 sweep points ∈ [3.0×10⁻⁴, 4.0×10⁻⁴]
  K, ≥50× below `netd_lo`=0.020K. ALL points classify UNDETECTABLE-or-better
  (none DETECTABLE). **NETD is an instrument/detector threshold, not a
  human perceptual one — this does not bear on constraint-3/4's human-eye
  verdict** (standing disclaimer, propagated per-point in `results.json`
  this cycle, fix 6).
- **P-IT22-A2 (Host D axis-K curve, unchanged from Phase 1 — computed
  against the `uncorrected` regime specifically, unaffected by any Block-B
  fix):** relative difference decreases monotonically with R from
  [10%,25%] at R=0.1 through [1.40%,1.55%] at R≈0.67–0.73 down to
  [1×10⁻⁸,1×10⁻⁵] at R=10.
- **P-IT22-A3 (Host-D witness-dwell consistency check, unchanged):** the
  sweep's own axis-K point nearest R≈0.67–0.73 reproduces exp-044's
  published 1.44–1.50% figure at all 4 Host-D ratios.
- **P-IT22-A4 (short-dwell benign artifact, unchanged):** at R=0.1 on axis
  K, Hosts A/B/C read relative difference ≥10× (1000%) while absolute ΔT
  stays ≤10⁻⁵K, ≥2000× below `netd_lo` — a metric artifact, not new
  physics, disclosed in advance.
- **P-IT22-A5 (T22-area-only ≤10% shift, unchanged — uses the
  `t22_area_only_x2.9`/`x3.0` regimes, untouched by any Block-B fix):**
  worst-case relative shift ≤10% at every host between the uncorrected and
  T22-area-only regimes.
- **P-IT22-A6 (REVISED — supersedes the Phase-1 draft's own, now-retracted
  [100×,160×] claim):** under the fully self-consistent `w_on`+silicon
  regime, `dwell/τ_thermal` ∈ [19×,23×] — **BELOW `N_TRANSIENT_TAU=25`**,
  i.e. this is genuinely LESS comfortable than the Phase-1 draft's own
  claimed headline, though still MORE comfortable than the T22-area-only
  correction (16.1–16.7×) and far more comfortable than nothing at all. The
  properly-derived correction **partially, not fully, relieves** T22's
  concern — the "relief" framing does not survive self-consistency. Under
  the alternate, equally self-consistent `r_out`+silicon regime,
  `dwell/τ_thermal` ∈ [180×,210×] — comfortably above 25×. Both figures
  are reported; neither is silently preferred.
- **P-IT22-B (Biot number, new):** `Bi(silicon) ∈ [1×10⁻⁴,3×10⁻⁴]` at
  BOTH length-scale regimes (algebraically length-invariant, confirmed
  numerically), ≈780× smaller than the PMMA-based Bi≈0.137 that motivated
  Red Team's fix-4 caveat — the lumped-capacitance assumption is deeply
  valid for the material this cycle actually adopts.
- **P-IT22-C (Block C dose-accumulation, new — Red Team's override of the
  Phase-1 deferral):** at Host D, max periodic/first-pulse population
  ratio ≤1.05 at the 5τ gap (near-complete relaxation between sweeps) and
  ∈[1.2,1.8] at the 0.5τ gap (real, order-of-magnitude-consistent memory
  buildup, matching exp-038's own established 1.4–1.6 finding at a
  different pulse duration). Max periodic decoupled ΔT ≤2×10⁻⁵ K, ≥500×
  below `netd_lo` — population memory is real but does not threaten the
  UNDETECTABLE verdict at Host D.

## Phase 4 — Results (run 2026-08-19)

Bench unchanged (no `lab/` file touched this cycle) — 41/41 fast stages
stand as pre-flight-verified this shift. Zero new FDTD calls, 0.27s.
`results.json` regenerated fresh from the frozen, predictions-committed
code (`24406dc`).

**8 of 9 predictions CONFIRMED, 1 PARTIAL (disclosed, not hidden):**

- **P-IT22-A1 CONFIRMED**: max ΔT = 3.585×10⁻⁴ K (in-band), margin 55.8×
  below `netd_lo` (≥50×), all 2080 points UNDETECTABLE-or-better.
- **P-IT22-A2 PARTIAL** — 3 of 4 Host-D ratio points at the R-grid point
  nearest 0.67–0.73 land inside the predicted [1.40%,1.55%] band (1.451%,
  1.451%, 1.452%); the r=1e-1 point reads **1.60%**, just outside the
  predicted ceiling. Genuine, disclosed miss, small in magnitude (5
  percentage-points-of-the-value overshoot) — an artifact of the fixed
  R-grid's nearest point not landing exactly on r=1e-1's own dwell/τ_k
  ratio (unlike A3, which tests the EXACT witness dwell directly and
  matches cleanly — see below). Does not affect any UNDETECTABLE
  classification (still comfortably sub-NETD at every point on this axis).
- **P-IT22-A3 CONFIRMED**: all 4 Host-D ratios reproduce exp-044's
  published 1.44–1.50% figure at the exact witness dwell (1.4955%,
  1.4955%, 1.4950%, 1.4422% — all inside [1.44%,1.50%]).
- **P-IT22-A4 CONFIRMED**: Hosts A/B/C at R=0.1 read relative difference
  2.7×10⁴%–3.0×10⁷% (comfortably ≥1000%, the stated falsification floor),
  while absolute ΔT stays 1.1×10⁻⁶–1.4×10⁻²⁰ K — many orders below NETD.
  Confirmed benign-artifact, not new physics.
- **P-IT22-A5 CONFIRMED** — worst-case *relative_difference* shift between
  the uncorrected and T22-area-only regimes (the correct comparison: each
  regime's own worst-case coupled-vs-decoupled relative difference on axis
  T, not a raw ΔT comparison at matching R — axis T's R denotes a different
  actual dwell per regime by construction, since dwell=R×τ_thermal(regime)):
  Host A 5×10⁻⁴%, Host B 0.50%, Host C 4.22%, Host D 0.045% — all ≤10%.
- **P-IT22-A6 CONFIRMED both readings**: `dwell/τ_thermal` = 21.24× at the
  primary `w_on`-consistent silicon regime (in [19×,23×], **below**
  `N_TRANSIENT_TAU=25` as predicted — the Phase-1 draft's "relief" framing
  does not survive self-consistency) and 194.18× at the alternate
  `r_out`-consistent silicon regime (in [180×,210×]).
- **P-IT22-B CONFIRMED**: Bi(silicon) = 1.7568×10⁻⁴ at BOTH length-scale
  regimes (in [1×10⁻⁴,3×10⁻⁴]), confirming length-invariance numerically
  and confirming the Biot concern is specific to the (superseded) PMMA
  identity's low conductivity, not structural under silicon.
- **P-IT22-C CONFIRMED**: Host D max periodic/first-pulse ratio 1.0051 at
  5τ gap (≤1.05) and 1.4509 at 0.5τ gap (in [1.2,1.8], matching exp-038's
  own order-of-magnitude finding at a different pulse duration). Max
  periodic decoupled ΔT = 7.385×10⁻⁷ K, margin 27,080× below `netd_lo` (≥500×
  predicted) — population memory is real but does not threaten the
  UNDETECTABLE verdict.

## Learned

1. **The genuinely untested intermediate-dwell regime does not threaten any
   UNDETECTABLE verdict this program has issued** — the coupled-ODE ceiling
   argument (Attack 12, structurally proven: Block B's own corrections can
   only ever lower `dt_ss_full`, never raise it) holds across 2080 points
   spanning 0.1×–10× of both time constants, 5 regimes, and a genuine
   population-memory check. This is the load-bearing physics result of the
   cycle.
2. **"First-principles" re-derivations need the SAME discipline this
   program applies to FDTD runs**: a from-scratch analytic correction
   (Block B) produced a real, sign-flipping, falsification-condition-firing
   defect (mixed length scales) that five blind critiques and one Red Team
   audit were needed to catch and fix — instrument-fidelity work is not
   lower-risk than mechanism-testing work just because it has zero FDTD
   cost.
3. **A material-identity fix can silently repair an unrelated-looking
   caveat**: adopting silicon (fixing MATERIALS' citation catch) also
   resolved THERMODYNAMICS' Biot-number concern almost entirely (Bi
   dropping ~780×) — a coupling between two seats' independent findings
   neither seat's own critique stated, caught only at Phase 3 synthesis.
4. **Self-consistency has a real, disclosed cost**: the properly-derived
   correction (21.2×) is genuinely LESS comfortable than the Phase-1
   draft's own (buggy) headline claim (126.7×) — dropping below the
   informal `N_TRANSIENT_TAU=25` comfort heuristic, though this does not
   threaten any actual verdict since Block A always uses the exact closed
   form, never the decoupled shortcut this heuristic originally governed.

## Next

Per Red Team's own next-seat note: QUANTUM OPTICS leads Iteration 24; this
cycle's Block C should be read as ELECTROMAGNETISM/Red-Team executing
QUANTUM's own design on QUANTUM's behalf this shift, not as preempting
QUANTUM's Iteration-24 leadership. QUANTUM's own aperture-consistent
single-coherent-mode beam check (self-imposed Checkpoint-4 tripwire, now a
THIRD deferral if not run at Iteration 23) remains untouched by this cycle
and is still due. See PLAN.md for the full ranked Iteration-23 queue,
updated this shift.

## Idealizations (carried from Phase 1, corrected/extended at Phase 3)

- Block A's `coupled_kinetics_thermal_dT` is reused verbatim from exp-044,
  independently re-verified a third time this cycle (Red Team). Not
  independently re-checked against `scipy.integrate.odeint` at this
  cycle's own 2080 points — exp-044's own <4×10⁻⁴ check at its 16 points is
  the standing verification, a disclosed gap not hidden.
- Block B's `w_on`/`r_out` choice, silicon identity, and the Knudsen/slip
  and Biot-number sensitivity notes are all disclosed per-regime in
  `results.json`, not asserted once and forgotten.
- Block C reuses `pulse_train_segments` with its argument roles inverted
  from exp-038's own convention (disclosed in `run.py`'s docstring) and
  reports a DECOUPLED ΔT estimate at the memory-accumulated population, not
  a new coupled-ODE closed form for nonzero initial population — a stated
  scope limit for this "bounded" check, not a silent gap.
- `k_air`, silicon's ρ/`C_P`/κ, and the Knudsen mean-free-path figure are
  all textbook/previously-cited values, not independently re-sourced this
  cycle (T18's WebFetch blockage stands, per every prior cycle since
  Iteration 13).
- No new formal trust-suite stage is added. Per Red Team's fix 7, one real
  cross-consistency assertion (the length variable feeding `h_eff` must
  match the one feeding `mass_kg`/area, by construction — `run.py`'s
  `self_consistent_regime()` takes a single `length_m` parameter, making
  the bug class Attack 1 found structurally unrepresentable, not merely
  checked) replaces the two tautological assertions Red Team's Attack 10
  found inadequate.
