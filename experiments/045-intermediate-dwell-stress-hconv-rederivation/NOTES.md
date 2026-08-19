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

**[Corrected at Phase 5 close — see below]** Seven of Red Team's eight
mandatory fixes are adopted in full. Fix 6 is adopted in full for its
`run.py`/`results.json` per-point requirement (verified: 2096/2096 NETD
dispositions carry a non-empty disclaimer) but its `phase1_proposal.md`
§4-inlining sub-requirement is explicitly **OVERRIDDEN**, for the reason
given below. `run.py` was rewritten accordingly (the Phase-1 draft's own
`run.py` is superseded, not preserved as a run path — per house discipline
this is a PRE-run fix, not a post-hoc erratum; T10's "flag, don't rewrite"
convention governs POST-run discoveries, and nothing in this cycle had been
run yet at Phase 3). `phase1_proposal.md` itself is left unedited (beyond a
one-line superseded banner added at Phase 5 close, fix 2) as the historical
record of what Phase 1 proposed and Phase 2 critiqued — **this is the
stated override of fix 6's own §4-inlining request**: T10's own precedent
(flag a historical document, do not rewrite it) is extended here, for the
first time, to a Phase-1 draft rather than a post-run results file. Phase
5's own Red Team audit confirmed this specific gap (the original version of
this paragraph claimed "none overridden," which was not accurate — VISION
SCIENCE's own Phase-5 catch, independently confirmed by Red Team; corrected
here as part of this cycle's own same-shift close, not left to a future
cycle).

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

**NETD is an instrument/detector threshold, not a human perceptual one —
none of the "UNDETECTABLE" classifications below bear on constraint-3/4's
human-eye verdict** (standing disclaimer; VISION SCIENCE's Phase-5 catch:
this sentence was present in `results.json` at every point (2096/2096) but
absent from this section's own prose in the Phase-3/4 draft — added here at
Phase 5 close, fix 3).

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
  5τ gap (≤1.05) and 1.4509 at 0.5τ gap (in [1.2,1.8]). **Correction at
  Phase 5 close (QUANTUM's catch, fix 8):** the 0.5τ figure should be
  compared against exp-038's own Host-D-specific 0.5τ maximum (1.2865), not
  only the looser programwide 1.4–1.6 band — exp-045's own 1.4509 reads
  ~13% above that specific figure. Likely cause, disclosed as a stated
  idealization rather than left unexplained: Block C's OFF gap uses a hard
  `k_f=0` (no ambient generation at all between sweeps), unlike exp-038's
  own "ambient" segments, which are never a true dark state — a different,
  disclosed idealization, not a discrepancy in the underlying kinetics
  machinery. Max periodic decoupled ΔT = 7.385×10⁻⁷ K, margin 27,080× below
  `netd_lo` (≥500× predicted) — population memory is real but does not
  threaten the UNDETECTABLE verdict.
- **P-IT22-D (new at Phase 5 close, fix 9 — commits EM's own Phase-5
  finding as permanent data, not only prose):** the decoupled ΔT proxy used
  for Block C's classification is a genuine OVER-estimate, never an
  under-estimate, at every one of the 8 points tested — the exact
  coupled-ODE solution (via a from-scratch generalization of
  `coupled_kinetics_thermal_dT` to nonzero segment-start population/
  temperature, `coupled_segment_general`, self-checked against the original
  formula at n0=dT0=0) sits 1.2%–3.4% BELOW the decoupled estimate at every
  point (`worst_case_exact_vs_decoupled_ratio`=0.9660). Independently
  spot-checked sound by Red Team's own Phase-5 audit (re-derived the
  governing monotone-approach inequality from the coupled ODE directly).
  Not a general proof for arbitrary future host/gap choices — the exact
  closed form now exists in `run.py` and can be reused directly, closing
  part (the direction/safety half) of THERMODYNAMICS' and QUANTUM's own
  Iteration-21/22 "warm-started exposure" concern; the fully general
  extension (feeding this closed form through a genuinely swept host/ratio
  grid beyond Host D) remains Iteration-23's own Tier-1 #3 priority.

## Learned

**NETD is an instrument/detector threshold, not a human perceptual one —
none of the findings below bear on constraint-3/4's human-eye verdict**
(fix 3, Phase 5 close).

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
   informal `N_TRANSIENT_TAU=25` comfort heuristic. **Corrected at Phase 5
   close (fix 7, THERMODYNAMICS' catch):** this does not threaten any
   actual verdict because BLOCK A always uses the exact closed form, never
   the decoupled shortcut this heuristic originally governed — the
   original wording of this sentence overgeneralized that claim to the
   whole cycle. Block C's own classification DOES use the decoupled
   shortcut (by disclosed design); see P-IT22-D above for why that choice
   is now shown, not merely assumed, to be conservative at Host D.
5. **(new, Phase 5 close) An analytic length scale calibrated for one
   physical quantity is not automatically safe to reuse for another.**
   `w_on` was correctly calibrated (by `absorbed_power_established_ratio`)
   as the length governing absorbed POWER — Block B's own Phase-3
   correction reused it, additionally, as the length governing CONDUCTION
   and MASS, on internal-bookkeeping-consistency grounds, without
   independently arguing (only Phase-5 disclosed, via PHOTONICS+
   ELECTROMAGNETISM's convergent finding) that an extinction-derived
   optical width is the physically-licensed length for `h_eff=k_air/L`,
   which is only rigorously the Nu=2 formula for a REAL geometric length.
   Elevated to Iteration-23's own Tier-1 #2 priority (see PLAN.md) rather
   than left as two disclosed, unargued endpoints (21.2×/194.2×).

## Phase 5 — Review (six fresh blind seats) and Red Team's final audit

Full record: `phase5_review_{photonics,materials,em,thermodynamics,
quantum,vision}.md`, `phase5_redteam_audit.md`.

**Six fresh blind seats:** MATERIALS (PROMISING); PHOTONICS, ELECTROMAGNETISM
(reviewing its own Phase-1 draft), THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE (all PARTIAL, one trending PROMISING). Zero arithmetic defects found
by any seat — every headline number independently re-derived and confirmed.
Real findings: PHOTONICS+EM independently converged on the `w_on`-vs-`r_out`
length-scale question being genuinely open, not resolved by disclosing two
endpoints (see Learned #5 above); EM closed the THERMO/QUANTUM
decoupled-shortcut-direction concern with a hand-and-numerically-verified
proof (P-IT22-D above); VISION caught that fix 6's `phase1_proposal.md`
§4-inlining sub-requirement was not actually done, and that this section's
own prose (pre-Phase-5) restated "UNDETECTABLE" without the disclaimer
several times; MATERIALS caught a missing "superseded" banner on
`phase1_proposal.md`'s own fabricated-PMMA text; QUANTUM caught an imprecise
Host-D comparison (fix 8, above) and confirmed its own literal Phase-2
proposal (`A=1`) was actually unimplementable — the shipped `A=0.0`
role-inversion is a correct repair, not an unfaithful rendering.

**Red Team's final audit** (sees everything): independently reconfirmed
every finding above from source, not on any seat's word. Ruled the
`w_on`-vs-`r_out` question **load-bearing and genuinely unresolved** —
elevated to Iteration-23 Tier-1 #2. Ruled EM's decoupled-shortcut closure
**sound** (independently re-derived the governing inequality). Ruled the
"all eight fixes adopted" inaccuracy **CONFIRMED** — a real instance of this
program's own named fix-docket-delivery pattern (Red Team's own Iteration-21
count: 5 of 7 prior iterations; this is a 6th-plus occurrence), but assessed
its severity as small (the load-bearing artifact, `results.json`, was fully
compliant; the gap was confined to a historical-record document and one
paragraph's internal consistency). **Checkpoint criterion 4: triggers the
pattern, does NOT fire**, contingent on the same-shift fixes below — the
identical mechanism this program applied at Iterations 19 and 21.

**Verdict: PARTIAL** (adjudicated over MATERIALS' lone PROMISING dissent,
preserved on the record — per this program's own established precedent that
verdict turns on whether open questions close, not seat count, applied
previously at Iterations 9, 10, 12, 17, 21). What closed cleanly: the
headline physics (no UNDETECTABLE verdict threatened anywhere in the swept
regime); the pre-run catch-and-fix of Block B's own sign-flipping defect
(the fix-docket pattern's WORSE failure mode — physics claimed-fixed-but-
not-delivered — did NOT recur this cycle, the specific risk Red Team's own
Phase-2 audit had flagged); the decoupled-shortcut-direction question. What
did not close, or closed only partway: the "all eight fixes" claim (fixed
here, this same shift); the `w_on`-vs-`r_out` question (elevated, not
resolved — Iteration 23's own #2 priority); the Biot caveat's block-scope-
only propagation (fixed here, fix 5); the exact coupled-ODE-at-nonzero-n0
solution (partially closed this shift by fix 9, fully general case still
open); prose-level disclaimer/citation gaps (fixed here, fixes 2/3/4).

**Ten same-shift mandatory fixes, ALL applied in this close** (see
`phase5_redteam_audit.md` §(e) for Red Team's own numbered list; cross-
referenced against this file's own inline fix-N markers above and against
`run.py`'s own code comments): (1) NOTES.md's Phase-3 claim corrected, with
the override explicitly stated in writing (above); (2) `phase1_proposal.md`
now carries a one-line SUPERSEDED banner; (3) NETD disclaimer added to this
section and Learned; (4) `run.py`'s two short console prints now carry the
disclaimer inline; (5) the Biot-number caveat is now propagated to every one
of the 832 Block-A sweep points that consume the two silicon-corrected
regimes (`biot_number`/`biot_disclaimer` fields), not block-scope only; (6)
PHOTONICS' σ_ext wavelength-flatness check is now committed as computed data
in `results.json` (`sigma_ext_wavelength_flatness_check`: 2.19% spread,
~5× the ratio's own 0.45%, headline confirmed robust at 20.3–21.2× across
all 3λ; the SAME check for the flagship absorber is disclosed as impossible
this shift — no 3λ σ_ext series for `graded_black_shell` exists anywhere in
the repo, a standing gap, not silently skipped); (7) Learned #4 corrected
(above); (8) the exp-045-vs-exp-038 Host-D comparison reconciled (above,
P-IT22-C); (9) EM's Block-C-conservative-bound table is now committed as
actual re-runnable data (`coupled_segment_general`, P-IT22-D above), not
only a Phase-5 review file's prose; (10) the hardened aperture-beam-check
rule is stated below and in LOGBOOK.md's own Iteration 22 entry.

**HARDENED RULE (Red Team's own explicit ruling, fix 10 — permanently
closing a counting ambiguity in the Iteration-21 tripwire, not a new rule):**
QUANTUM's aperture-consistent single-coherent-mode beam check was correctly
NOT due this cycle (a disclosed, reasoned Tier-2 scope decision at Phase 1,
not silent drift) — Checkpoint criterion 4 does not fire at this close on
that account. **It MUST be executed at Iteration 23, by any lead seat
(native or not, per this program's own Iteration-18/20/21/22 precedent). If
Iteration 23 closes without it having been run, Checkpoint criterion 4
fires automatically and immediately — no further debate, no seat vote, no
Director discretion, and no further one-cycle extensions via prose.**

**Next lead per rotation: THERMODYNAMICS** (Iteration 23; VISION→PHOTONICS→
MATERIALS→ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→repeat).

**Ranked priorities for Iteration 23** (Red Team's Phase-5 synthesis across
all six seats, adjudicated not concatenated): **Tier 1 (mandatory /
near-zero-FDTD-cost):** (1) QUANTUM's aperture-consistent single-coherent-
mode beam check — hardened rule above, 5-of-6-seat convergence at #1; (2)
resolve the `w_on`-vs-`r_out` `h_eff` length-scale question (PHOTONICS+EM,
elevated by Red Team) — compute the third, physically-motivated "mixed"
regime (power on `w_on` per its own calibration, conduction/mass on `r_out`
per Nu=2's own derivation requirement); (3) extend `coupled_segment_general`
(built this shift) to a genuinely swept host/ratio grid beyond Host D,
closing THERMODYNAMICS'/QUANTUM's own remaining ask in full. **Tier 2:**
VISION's own glare/adaptation Tier-W sidecar (self-imposed tripwire, now
due); extend Block C's dose-accumulation check to the remaining 12 host/
ratio points, scored against `REALIZABILITY_MEMO.md`'s own per-host tiers
(EM+MATERIALS convergent pick — directly tests MATERIALS' own new Phase-5
finding that memory-buildup risk and dynamic-range shortfall may be
structurally coupled axes). **Tier 3 (standing, several still blocked):**
the rigorous RSA/TPA/FCA primary-source literature check (T18/WebFetch, 9+
consecutive shift confirmations); T21's contamination-risk re-score;
PHOTONICS' R3 recheck of exp-044's 0.45% achromatic-flatness claim;
`realizability_tier` de-duplication housekeeping.

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
