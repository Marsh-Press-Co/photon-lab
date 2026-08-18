# exp-042 — The Edge-Diffraction Magnitude Bridge (T21) (panel Iteration 19)

**2026-08-18 · driver: Clyde as panel Director · status: predictions committed, run not yet executed**

Nineteenth experiment of the panel program (PANEL.md / LOGBOOK.md). Lead
seat: **VISION SCIENCE** (rotation). Executes LOGBOOK.md Iteration 18's
Red-Team-ranked #1 priority for Iteration 19, live thread **T21**: an
analytic edge-diffraction model scoring ELECTROMAGNETISM's own Iteration-18
Phase-5 mechanism (Huygens edge-wave radiators at the source's taper rim,
offset A=752 cells from the object window center, oscillation period
P(θ)=λ/(A·cosθ)) against all 30 of exp-041's Block MAIN signed C_empty(θ,λ)
rows — magnitude-level, not just sign/ranking, the one gap T21's Iteration-18
close left open. Paired with VISION's own zero-cost beam-divergence/
contamination-risk check. Zero new FDTD calls. This file is the **Phase-3
synthesis**: one testable configuration, five critiques and a Red Team audit
resolved on the record, predictions committed before the first run.

## Phase 1 — the proposal (VISION SCIENCE, lead)

Not a mechanism proposal — pure instrument characterization. Proposed
generalizing EM's two-point-source picture into a full coherent
Huygens–Fresnel sum over the ENTIRE known source aperture (the exact tapered
`p(y)` array `add_line_source` builds), propagated via the 2D free-space
cylindrical Green's function through vacuum, reduced through the bench's own
`window_means`/`weber` machinery — EM's mechanism at full strength, not a
two-point caricature of it (the two-edge picture and P(θ)=λ/(A·cosθ) are the
model's own stationary-phase limit, recoverable from it, not assumed).
Verified A=752 independently from two already-pinned geometry constants
(OBJ_Y−ABSORB = 792−40 = 752, matching (NY−ABSORB)−OBJ_Y = 1544−792 = 752
exactly — not a fit), and cross-checked the straight-line rim-to-observer
distance √(D_SP²+A²)≈784.4 cells against Red Team's own Iteration-18
"≈784" figure.

Claimed zero free parameters, on the argument that Weber contrast is
homogeneous degree 0 in any UNIFORM complex source-calibration rescale (the
FDTD-soft-source-vs-true-line-current ambiguity), so that ambiguity cancels
exactly regardless of Green's-function normalization convention — later
sharpened at Phase 2 (see below): this protects only a uniform rescale, not
every implementation choice.

VISION's own first-pass run (disclosed explicitly as non-final due
diligence, "a fresh, reviewed implementation may differ"): sign agreement
27/30; R²(raw)=0.656; per-λ ranking prediction (600nm best, nearest the 2°
Nyquist edge; 750/450nm worse; misses concentrated at small-magnitude
θ=±39° rows); a predicted systematic UNDER-prediction with best-fit scale
c≈1.6 (R²→0.78), attributed — untested — to unmodeled Yee-grid dispersion
and the source rim sitting at the absorbing-boundary onset. Beam-divergence
check (incoherent power sum over a Gaussian angular kernel): predicted every
tested cell washes below C_thr=0.005 for FWHM≥5°, EXCEPT a predicted
exception at 750nm/θ0=40°/FWHM≈20° (|C_avg|≈0.006) — a genuine, narrow
contamination-risk finding, not a false alarm.

Proposed target (adopted): `experiments/042-t21-magnitude-bridge/`.

## Phase 2 — critiques (five seats blind, then Red Team with everything)

**PHOTONICS — support-with-changes.** Independently reimplemented the model
from scratch and reproduced VISION's own sign-agreement number exactly
(27/30) — real external corroboration the mechanism is correct physics.
Sharpest attack: the "zero free parameter" claim hides an undisclosed
choice — does the coherent sum reduce to field intensity |E|² or to
directional Poynting FLUX (what the bench's own B(y) actually is)? Raw
|E|² gives R²=0.78, c≈1.15; adding the correct Rayleigh–Sommerfeld
obliquity factor (cosψ=Δx/r) COLLAPSES R² to 0.42 and pushes the needed
scale to c≈2.6 — sign agreement barely moves (28/30). Flip: mandate the
flux-correct reduction, report both as disclosed alternates.

**MATERIALS — support-with-changes.** Steel-man: zero-parameter, targets
exactly what `REALIZABILITY_MEMO.md` Amendment 1 leans on, cannot move
either UNOBTANIUM verdict. Sharpest attack: the exp-032 PASS→MARGINAL
downgrade Amendment 1 actually cites (Δ=6.522×10⁻⁴) was measured on Block
N17_NATIVE_V2 (exp-035), built by the RATIO=1.5 domain-construction method —
NOT exp-024/041's MARGIN_MULT=3.5 domain that Block MAIN (the 30 rows this
leg scores against) actually uses. A clean fit here says nothing rigorous
about that specific citation at a different domain. Flip (mandatory):
realizability cap + explicit domain-mismatch disclosure.

**ELECTROMAGNETISM — support-with-changes.** Steel-man: the correct,
rigorous completion of EM's own Iteration-18 heuristic; reciprocal/
passive/causal, so T1 bookkeeping untouched; independently re-verified
A=752 exact and kr(D_SP)=56.0–93.4 (asymptotic far-field legitimately
valid). Sharpest attack: independently verified `weber()`'s scale-invariance
directly in code — but that PROOF CUTS AGAINST the c≈1.6 diagnostic, not
for it: since no uniform source-scale factor can move a properly-reduced
contrast prediction, a fitted c that DOES move R² cannot be a benign
calibration echo — it must be a real, non-cancelling residual, and calling
it benign is a direct self-contradiction. Also flagged the λ-dependent
causal transit margin (13.0/9.8/7.8 periods at 450/600/750nm, thinnest at
750nm — the same λ that falsified P-M1 in exp-041) as an idealization gap.

**THERMODYNAMICS — support-with-changes.** Steel-man: charter-clean, no
article/absorbed-power claim anywhere. Sharpest attack: silent on PLAN.md's
two queued THERMO items (docket #7; `thermo_sidecar.py` rescoping) that
exp-041's own Phase-3 explicitly deferred "to Iteration 19" — and THIS cycle
declares zero new FDTD calls, so no budget conflict excuses silence this
time. Flip: an explicit Phase-3 disposition sentence.

**QUANTUM OPTICS — support-with-changes.** Steel-man: squarely QUANTUM's
own established territory — `add_line_source` drives every aperture cell
from one phase-locked oscillator, and QUANTUM's own Iteration-6 (exp-029)
already proved this engine's coherent superposition exact to 2.483×10⁻¹⁵
RMS relative error. Sharpest attack: the coherent/incoherent boundary is
drawn on the WRONG AXIS — the magnitude-bridge half correctly treats the
FULL aperture as one coherent emitter, but the beam-divergence check then
combines DIFFERENT injection angles by INCOHERENT summation, borrowing
`lab.ambient.incoherent_sum`'s convention (built for genuinely separate
illuminants) for what are, in the model's own terms, angular-spectrum
components of the SAME coherent aperture. Representing divergence
incoherently can get the contamination-risk direction backward. Flip:
require a coherent finite-angular-spread cross-check alongside the
incoherent number; label any contamination-risk claim provisional until
both exist.

**RED TEAM — numbered attacks, independently re-verified against code, then
overall ruling PROCEED-WITH-MANDATORY-FIXES:**

1. [inconsistency, LOAD-BEARING] PHOTONICS' reduction-convention attack
   CONFIRMED to 3 sig figs by an independent third implementation
   (naive: R²(c=1)=0.7789, c*=1.1550, 27/30; flux: R²(c=1)=0.4177, c*=2.6026,
   28/30). `cosψ` measured to range ~0.65–1.0 across the scored windows —
   not remotely uniform.
2. [inconsistency] Sharper than either seat alone: the "zero free
   parameters" claim conflates a uniform-rescale invariance (proven, real)
   with the reduction-convention choice (not a uniform rescale, unprotected
   by that proof).
3. [inconsistency] EM's self-contradiction finding is correct as a proof,
   premature as applied to VISION's specific c: VISION's own cited pair
   (0.656→0.78 at c≈1.6) matches NEITHER tested convention exactly.
4. [inconsistency, new finding] A THIRD, still-undisclosed implementation
   choice underlies VISION's own headline numbers — echoes T15's own
   three-uncommitted-chord-model precedent.
5. [constraint-3-adjacent misattribution risk, LOAD-BEARING] MATERIALS'
   domain-mismatch claim CONFIRMED directly against code — Block N17_NATIVE_V2
   is a structurally different domain (RATIO=1.5, R_OUT=117) from exp-041's
   own (MARGIN_MULT=3.5, R_OUT=78 native); domain construction alone moves
   C_empty by 3.55×10⁻⁴ at r=156, 54% the size of the very downgrade cited.
6. [unfalsifiable, provisional, LOAD-BEARING] QUANTUM's coherent/incoherent
   attack independently reproduced and found WORSE than framed: a standalone
   check at 750nm/θ0=40°/FWHM=20° gave incoherent C=−0.00215 (reads "safe")
   vs. coherent (phase-referenced at the aperture center) C=−0.987 (near-total
   silhouette) — a >2-orders-of-magnitude, opposite-conclusion swing. The true
   answer is unknown without the mandated cross-check.
7. [inconsistency, minor] QUANTUM's docstring citation overstates its
   source — the substantive physics point survives independently.
8. [inconsistency, verified] EM's causal-transit-margin arithmetic
   independently confirmed near-exactly (r_edge=784.36, margins
   13.07/9.80/7.84 periods at 450/600/750nm).
9. [inconsistency, precedent-elevated, LOAD-BEARING] THERMO's disposition-gap
   claim confirmed against PLAN.md's own text — Iteration 19's own ranked
   list already states "no resource conflict" for docket #7/`thermo_sidecar`
   against a zero-FDTD-call cycle; the one excuse that justified silence at
   Iteration 18 is gone this cycle.
10–12. [not found, for completeness] no `[inexpressible]` finding (pure
   post-hoc analytic scoring, zero new engine physics); no direct
   constraint-1/2/4 violation; the proposal's own falsification bands are
   internally coherent (non-overlapping, correctly ordered).

**Adjudication:** every mandatory ask above independently re-verified,
cheap, proportionate. **No ask from any of the five seats rejected as
overreach.**

**Overall ruling: PROCEED-WITH-MANDATORY-FIXES.** Not KILL (the underlying
mechanism is real, independently reproduced by three implementations at
27–28/30 sign agreement). Not MAJOR-REVISION (every fix is a definitional/
disclosure correction to a fundamentally sound computation, zero additional
FDTD cost). Eight mandatory fixes specified (see Phase 3, below).

## Phase 3 — Synthesis (Director)

**All eight of Red Team's mandatory fixes adopted exactly as specified.
Nothing overridden; no seat's ask ruled overreach.**

1. **[PHOTONICS/Red Team, load-bearing]** The flux/Poynting reduction
   (Rayleigh–Sommerfeld obliquity factor `cosψ=D_SP/r` applied per Huygens
   wavelet before the coherent sum) is the PRIMARY, headline-scoring model —
   because `lab.ambient.observer_profile` is verified by direct code read
   (`lab/ambient.py:35-37`, `-sections.flux_profile_x`) to return a Poynting
   flux, not `|E|²`. The naive `|E|²` reduction is reported as an explicitly
   labeled SECONDARY/context reading.
2. **[Red Team, load-bearing]** "Zero free parameters" is scoped precisely
   in `design_geometry.py`'s own docstring: only a uniform source-amplitude
   rescale is proven invariant (re-derived from `weber()`'s own code); the
   reduction-convention choice is a separate, unprotected axis (`cosψ`
   measured to range ~0.65–1.0 — 0.26–1.0 at the object window specifically,
   including the far-window edges — across the scored windows, printed by
   `design_geometry.main()`).
3. **[Red Team, load-bearing]** This experiment's OWN committed-code numbers
   (Phase 4, below) supersede VISION's Phase-1 preliminary run, which
   matches neither tested convention exactly (a fourth, undisclosed
   implementation detail) — Predictions below are scored against numbers
   this file's own code will generate, not VISION's first-pass figures.
4. **[Red Team, load-bearing]** The best-fit scale `c*` is reported and
   labeled **"of undetermined origin — real residual vs. leftover convention
   artifact not yet distinguished"** — not asserted as definitely real
   physics (EM's original language) nor as a benign calibration echo
   (VISION's implicit framing).
5. **[MATERIALS/Red Team, load-bearing]** Domain-mismatch disclaimer added
   verbatim to `design_geometry.py` and restated in Results: this leg's
   geometry (exp-024/041's own, MARGIN_MULT=3.5, R_OUT=78 native) is NOT the
   domain (exp-035's Block N17_NATIVE_V2, RATIO=1.5, R_OUT=117) that produced
   the exp-032 PASS→MARGINAL delta `REALIZABILITY_MEMO.md` Amendment 1
   cites. A clean fit here is information about the edge-diffraction
   mechanism at exp-041's own geometry, not evidence about that specific
   citation. MATERIALS' realizability-relevance cap carried forward
   unchanged (this leg's result, either direction, cannot move either
   UNOBTANIUM-WITH-PARAMETERS verdict). MATERIALS' own optional ask
   (cross-score against N17_NATIVE_V2's own empty-scene points) is NOT
   adopted this cycle — ruled correctable-not-mandatory by Red Team;
   queued for Phase 5 ranking instead, to keep this cycle's own scope
   tractable given the eight mandatory fixes already committed.
6. **[QUANTUM OPTICS/Red Team, load-bearing]** Block BEAM reports BOTH an
   incoherent angular power-sum (reusing `lab.ambient.incoherent_sum`
   directly, matching the convention this program's real angular-quadrature
   measurements use) AND a coherent finite-angular-spread sum (each angular
   component's field coherently added, sharing the same aperture-center
   phase origin every single-angle call already uses) — an analytic
   realization of the coherent-superposition PRINCIPLE exp-029 bench-
   validated, disclosed explicitly as NOT a literal reuse of exp-029's own
   FDTD injection code (this leg is desk-only throughout). Any
   contamination-risk language in Results is gated on both readings being
   reported together, and stays provisional if they diverge sharply.
7. **[THERMODYNAMICS/Red Team, load-bearing]** Explicit disposition:
   PLAN.md's two queued THERMO items (docket #7's sourced witness table;
   `lab/thermo_sidecar.py` re-scoping) are **DEFERRED, explicitly, with
   reason** — this cycle's own Phase-2 debate already produced eight
   mandatory fixes spanning two independent physical conventions (the
   flux/intensity reduction axis and the coherent/incoherent beam-spread
   axis); docket #7 is a WebSearch-grounded literature-sourcing task and the
   sidecar re-scoping is a separate code deliverable — bundling either in
   risks under-resourcing both, the same scope-discipline concern exp-041's
   own Phase-3 raised. Unlike exp-041's cycle, THIS deferral is NOT excused
   by a budget conflict (there is none, this leg is zero-FDTD-cost) — it is
   a scope-discipline call, stated as such, not silence. Ranked the
   EXPLICIT #1 priority for Iteration 20 in Phase 5 below, not left to
   recur silently an eighth time.
8. **[ELECTROMAGNETISM/Red Team]** Idealizations extended with the
   λ-dependent causal transit margin (13.0/9.8/7.8 periods at 450/600/750nm,
   thinnest at 750nm) — see `design_geometry.py`'s `MARGIN_PERIODS`,
   computed, not hand-typed.

**Overridden: none.**

## Setup

Every geometry constant copied VERBATIM from
`experiments/041-t20-angle-audit/design_geometry.py` — see this file's
`design_geometry.py` module docstring for the full pinned-constant table.
No domain rescaling. Zero new FDTD calls — Block MAGNITUDE scores against
exp-041's own committed `results.json`; Block BEAM is pure analytic
propagation over a λ×θ0×FWHM grid.

## T1 escape-route statement

**None.** Pure instrument/mechanism characterization of the ambient-contrast
measurement channel itself (as exp-041 and every T20/T21 leg before it) — no
σ(I)/σ(x,t)/ε(ω)/gain parameter appears anywhere in this leg.

## Predictions — committed before this experiment's official run

Grounded in the Director's own due-diligence prototype (independent from,
but code-identical to, this file's committed `design_geometry.py`/`run.py`
— the actual Phase-4 run is expected to reproduce these to machine
precision; any discrepancy is itself reported, not silently reconciled).

**P-MAG1 (Block MAGNITUDE, PRIMARY/flux convention, sign agreement).**
Central **28/30**, band **[26,30]**. **Falsified if ≤22/30** (binomial
p<0.05 vs. a 50% null, VISION's own original threshold, retained).

**P-MAG2 (Block MAGNITUDE, PRIMARY/flux convention, R² at c=1).** Central
**0.42**, band **[0.30, 0.50]**. **Falsified if R²<0.15 or R²>0.85**
(VISION's original outer bounds retained as absolute falsification limits;
central estimate tightened to reflect three independently-converging
implementations — VISION's PHOTONICS-matching reimplementation, Red Team's,
and this module's own prototype — all landing within 0.01 of 0.4177).

**P-MAG3 (Block MAGNITUDE, best-fit scale c*, PRIMARY convention,
descriptive only — no pass/fail).** Central **2.60**, band **[2.0, 3.2]**.
Per mandatory fix 4, this number is reported and labeled
undetermined-origin regardless of where it lands — not scored as
confirming or refuting any physical claim.

**P-MAG4 (Block MAGNITUDE, SECONDARY/naive convention, context only).**
Central sign agreement **27/30**, R²(c=1) central **0.78**, c* central
**1.15** — reported for comparison, not scored pass/fail (mandatory fix 1).

**P-MAG5 (per-λ breakdown, PRIMARY convention).** 600nm best (central
**10/10**, matching T21's own "nearest 2° Nyquist" reading); 450nm and
750nm each **≥8/10**; misses (if any) concentrated at the small-magnitude
θ=±39° rows specifically at 750nm (VISION's original claim also named
450nm — this prediction narrows it to 750nm only, based on the Director's
own prototype run, an explicit, disclosed sharpening of VISION's Phase-1
band, not a silent one). **Falsified if** 600nm's own sign agreement is
NOT the best of the three λ, or if any λ falls below 7/10.

**P-BEAM1 (Block BEAM, incoherent/PRIMARY reading, contamination risk).**
Central prediction: **zero** of the 36 (λ,θ0,FWHM) cells exceed
C_thr=0.005 in magnitude under the incoherent reading — REVISING VISION's
own Phase-1 predicted exception (750nm/θ0=40°/FWHM≈20°) toward NO exception
found, based on the Director's own prototype (a disclosed correction, not
silent). **Falsified if ≥3 cells exceed C_thr** (a margin against the
possibility the official run's numerics differ from the prototype's).

**P-BEAM2 (Block BEAM, coherent/mandatory cross-check reading).** Central
prediction: **≥30 of 36 cells** exceed C_thr, most reaching |C|>0.6 — i.e.
the coherent reading predicts near-silhouette-level contrast across most of
the grid, sharply diverging from P-BEAM1. This divergence is PREDICTED, not
an anomaly to explain away: full angular coherence across a beam spread this
wide (multiple degrees) is expected to behave like a focused/interfering
phased array, not like a real (spatially/temporally limited-coherence)
flashlight — the coherent reading is predicted to be an artifact of the
full-coherence assumption for any real emitter, not a literal contamination
risk. **Falsified if <15 of 36 cells exceed C_thr under the coherent
reading** (i.e. if the coherent and incoherent readings turn out to agree
much more than predicted — itself the more surprising, informative outcome
if it occurs).

## Idealizations

2D TMz, ε_r≡1 (vacuum) between source and observation plane, single CW
frequency, steady state — no object present (pure empty-scene instrument
characterization; this model cannot and does not speak to exp-041's Block
OBJPRESENT coupling question). Each source cell an independent point
radiator in its own asymptotic (kr≫1) far field — validity checked
(kr≈56–636 across the swept geometry, worst case still 56, well above the
kr≫1 threshold), not assumed. Yee-grid numerical dispersion (finite
cpl=15–25) is **not** modeled — a continuum propagator, not a discretized
one — named as a leading candidate for the systematic gap between predicted
and measured magnitudes at c*≠1, untested this cycle. The source aperture's
hard rim coincides exactly with the absorbing/damping boundary's onset
(y=ABSORB) — untested, a second under-prediction candidate. **New this
cycle (mandatory fix 8):** the edge-to-observer causal transit margin is
λ-dependent — 13.0/9.8/7.8 periods of settling margin at 450/600/750nm
(STEPS=1400, r_edge=784.4 cells, S=0.700 cells/step) — THINNEST at 750nm,
the same wavelength whose P-M1 magnitude prediction exp-041's own Phase-4
record shows was refuted; this continuum model has no settling dynamics at
all and cannot see this effect, only flag it as a candidate confound for
750nm's expected worse fit. Settling in the ORIGINAL FDTD runs (exp-041's
own Block MAIN) is otherwise assumed complete, per that experiment's own
idealizations, not re-litigated here. The FDTD "soft source" injection is
treated as equivalent, up to the uniform calibration scale, to a true
physical line current (an existing engine-level idealization, inherited).
Block BEAM's incoherent reading matches `lab.ambient.incoherent_sum`'s own
convention (the physically appropriate model for a genuinely spatially-
extended, low-coherence emitter); the coherent reading uses one specific,
simple, disclosed phase convention (shared aperture-center origin) — NOT
asserted as the physically correct model for a real flashlight, only as the
mandated cross-check bound (mandatory fix 6). No sourced real-flashlight
beam-FWHM or coherence-length figure exists yet in this program — a swept
range (2°/5°/10°/20° FWHM) stands in for the former; a partial-coherence
model bridging the incoherent/coherent extremes is out of this cycle's
scope entirely (a candidate Iteration-20+ item if the divergence found here
warrants it).

## Run plan

`python3 run.py` — zero new FDTD calls; Block MAGNITUDE scores against
`experiments/041-t20-angle-audit/results.json` (read-only), Block BEAM
sweeps a 3×3×4 (λ×θ0×FWHM) grid × 2 conventions, results written to
`results.json`. Full bench (`lab/validation/run_all.py --only 12346789`)
reverified green before and after (no `lab/` change, a formality per house
discipline).

## PHASE 4 — RESULTS (run 2026-08-18)

Bench reverified green immediately before and after (no `lab/` change):
`lab/validation/run_all.py --only 12346789` **41/41** both times, matching
Iteration 18's own committed record. Zero new FDTD calls, 2.9s total
wall-clock. Full data: `results.json`. The official run reproduces the
Director's own due-diligence prototype to machine precision — no
discrepancy to report.

### Block MAGNITUDE

**P-MAG1 (sign agreement, PRIMARY/flux) — CONFIRMED, exactly central.**
Measured **28/30**, matching the predicted central value exactly (band
[26,30], falsification floor 22).

**P-MAG2 (R² at c=1, PRIMARY/flux) — CONFIRMED, near-exact.** Measured
**R²=0.4176** vs. predicted central 0.42 (band [0.30,0.50]) — a genuine,
magnitude-level confirmation of EM's edge-diffraction mechanism under the
physically-correct (flux/Poynting) instrument convention. **This closes
the specific gap Iteration 18 left open**: T21's fringe is now validated
against signed magnitudes, not just sign/ranking, at zero FDTD cost.

**P-MAG3 (best-fit scale c*, descriptive) — reported as predicted.**
Measured **c*=2.6023** (flux) — inside the predicted band [2.0,3.2], and
per mandatory fix 4, labeled **of undetermined origin**, not asserted as
real non-cancelling physics or a benign calibration echo. Distinguishing
the two remains open, unscoped this cycle.

**P-MAG4 (naive/secondary convention, context) — CONFIRMED, near-exact.**
Measured **sign=27/30, R²(c=1)=0.7787, c*=1.1547** — matches predicted
central values (27/30, 0.78, 1.15) closely. Numerically better-fitting than
the flux convention, but **not the physically correct reduction** (per
mandatory fix 1 — `lab.ambient.observer_profile` measures flux, not `|E|²`)
— reported here as context only, never as the headline result.

**P-MAG5 (per-λ breakdown, PRIMARY/flux) — PARTIALLY CONFIRMED, precisely.**
Measured: **450nm 10/10, 600nm 10/10, 750nm 8/10.** The sharpened claim
("misses concentrated at θ=±39° specifically at 750nm") is **CONFIRMED
exactly** — both 750nm misses are at θ=±39°, the smallest-magnitude rows in
that λ's own set (measured 0.00383/0.00396 vs. predicted −0.00248/−0.00241
— correct magnitude order, wrong sign, exactly the near-zero-crossing
fragility VISION's original Phase-1 language anticipated). But the "600nm
uniquely best" framing is **not quite right, honestly reported rather than
rounded up**: 450nm ALSO scores 10/10 under the flux convention — the two
are TIED for best, not 600nm alone. This is itself informative: the
"nearest-2°-Nyquist" narrative that explains 600nm's clean *sign*
alternation under the ORIGINAL (naive-convention, exp-041 Phase-5) reading
does not cleanly predict which λ wins under the flux-corrected convention's
own sign-agreement count — a nuance for any future cycle citing this
ranking, not a refutation of the underlying mechanism.

### Block BEAM

**P-BEAM1 (incoherent/PRIMARY reading) — CONFIRMED, exactly.** **Zero of
36** (λ,θ0,FWHM) cells exceed C_thr=0.005 in magnitude — the largest
measured |C| is 0.00301 (750nm, θ0=38°, FWHM=2°), still 40% below
threshold. **This is a STRONGER finding than VISION's own original
Phase-1 prediction**, which flagged a specific exception at 750nm/θ0=40°/
FWHM≈20° — that exact cell measures |C|=0.00026 here, far below C_thr, not
an exception. Under the properly flux/obliquity-consistent, committed model,
**the T21 fringe shows NO contamination risk anywhere in the tested grid**
for any beam with angular FWHM≥2° — even a beam only 2° wide already washes
the fringe to <60% of C_thr at every tested (λ,θ0) combination.

**P-BEAM2 (coherent/mandatory cross-check reading) — CONFIRMED, exceeded.**
**36 of 36** cells exceed C_thr (predicted ≥30/36) — every single tested
cell, not just most. 27 of 36 (all FWHM∈{5,10,20}°) reach |C|>0.6, several
approaching |C|≈0.99–1.00 (near-total geometric silhouette contrast); the
remaining 9 (FWHM=2° only) range 0.03–0.47, still all above C_thr. **The
predicted sharp divergence between the two readings is confirmed, and the
reasoning for it stated in the predictions holds up**: coherently summing
plane-wave tilts spanning several degrees of angular spread reproduces the
physics of a focused/interfering phased array, not a real flashlight — no
ordinary incandescent or LED emitter maintains spatial coherence across an
aperture radiating a multi-degree angular spread at these path lengths, so
this reading is read as **an artifact of the full-coherence idealization**,
not a literal physical contamination-risk finding, exactly as flagged before
the run. **The contamination-risk question is therefore NOT settled by
either reading alone** — the incoherent number is very likely close to
physical reality for any real flashlight, but this cycle builds no
partial-coherence model that would let a single number replace "probably
near the incoherent reading, bounded above by the coherent one." Mandatory
fix 6 (QUANTUM/Red Team) is satisfied: both readings are reported together,
and the contamination-risk language above is stated as probable, not
certain.

### Discussion

**T21 status: the magnitude-level gap Iteration 18 left open is now
closed**, cleanly, at zero FDTD cost, under a Red-Team-hardened, precisely-
scoped convention — three independent implementations (VISION's own
prototype, PHOTONICS' and Red Team's Phase-2 reimplementations, and this
committed module) converge on the same qualitative and (for the latter two)
quantitative picture: sign/ranking robust (27–28/30 across both
conventions), R² convention-dependent (0.42 flux vs. 0.78 naive) but
clearing the falsification floor either way, and a genuine, as-yet-
unexplained systematic scale gap (c*) whose origin is explicitly left open
rather than claimed either direction. **The domain-mismatch disclaimer
(mandatory fix 5) stands unmodified by this result**: this leg validates
the mechanism at exp-041's own geometry (MARGIN_MULT=3.5, R_OUT=78 native)
— it says nothing new about `REALIZABILITY_MEMO.md` Amendment 1's own
cited number, which lives at a structurally different domain
(N17_NATIVE_V2, RATIO=1.5, R_OUT=117). The realizability-relevance cap
(carried from exp-041) holds: nothing here moves either UNOBTANIUM-WITH-
PARAMETERS verdict.

**New, sharp open question from Block BEAM**: the incoherent/coherent
divergence is large enough (near 0 vs. near-total silhouette) that it
cannot be waved away as a rounding-level nuance — a genuine partial-
coherence model (a real emitter's finite coherence length/area, bridging
the two extremes measured here) is the natural next test if this program
ever needs a settled, single-number contamination-risk verdict for a
near-±40°/near-3λ-scale-shell constraint-3 run. Not scoped this cycle;
queued for Phase 5 ranking.

**THERMO disposition (mandatory fix 7) — holds as stated.** PLAN.md's two
queued THERMO items (docket #7's sourced witness table; `thermo_sidecar.py`
re-scoping) remain explicitly deferred, ranked as Iteration 20's own #1
priority below — not silently dropped an eighth time.

## PHASE 5 — REVIEW (six fresh blind seats, then Red Team audit)

**PHOTONICS (PROMISING).** Independently re-derived every headline number,
all exact. New finding: best-fit scale c* computed PER WAVELENGTH —
450nm≈1.81, 600nm≈2.74, 750nm≈3.23, a clean monotonic increase — contradicts
Yee-grid dispersion as the driver (450nm has the coarsest grid, cpl=15, so
dispersion error should be WORST there; instead it fits BEST) and instead
matches the causal-transit-margin idealization's own ordering (thinnest
margin at 750nm, worst fit at 750nm). Called NOTES.md's original "cleanly
closed" language "a shade generous" (58% of variance unexplained at c=1
under the then-primary convention). Ranked #1: a real FDTD settling-margin
test.

**MATERIALS (PARTIAL).** Confirmed the domain-mismatch disclaimer holds
exactly. Found (traced constants directly): Block N17_NATIVE_V2 is an EXACT
×1.5 rescale of this leg's own geometry (R_OUT 78→117, ABSORB 40→60, SRC_X
300→450, NY 1584→2376, CPL 20→30, all ×1.5 precisely; A in wavelength units
identical: 37.6λ both) — the SAME 600nm scenario at finer resolution, not
an unrelated domain. Reframes its own Phase-2 deferred cross-score ask as
MORE valuable (a real resolution-refinement diagnostic on c*) but corrects
that it is NOT zero-cost — `block_n17()` only persists pooled aggregates,
not the full per-angle table a real fit needs (~8–17 new FDTD calls).

**ELECTROMAGNETISM (PROMISING, with one load-bearing correction) — see
ERRATUM below.** Independently re-verified every committed number exactly,
then found the committed PRIMARY convention misapplies the obliquity
factor for this bench's actual (soft, additive current-array) source
model, and derived a corrected convention scoring sign=27/30,
R²(c=1)=0.6570, c*=1.6196, R²(c*)=0.7852 — matching VISION's own original
Phase-1 preliminary numbers (0.656/≈1.6) to 3 significant figures,
identifying mandatory-fix-3's "fourth, undisclosed implementation choice."
Also traced Block BEAM's coherent reading physically: the "near-total
silhouette" is the coherent beam's geometric-ray-optics footprint
(y−OBJ_Y = D_SP·tanθ0, exactly) landing off the object window and
retreating into the flank window as FWHM grows — a geometry-alignment
effect, sharpening (not contradicting) the "artifact" reading.

**THERMODYNAMICS (PARTIAL).** Confirmed charter-clean silence. Sharp
attack: this is the THIRD consecutive iteration (17→18 implicitly, 18→19
explicitly) docket #7/`thermo_sidecar` haven't moved, and "ranked #1 for
next iteration" has climbed in priority language across three closes
without the action count ever leaving zero. Rules Checkpoint criterion 4
does NOT fire this cycle (honestly disclosed, reasoned, not falsely
excused) but PRE-REGISTERS a tripwire: a fourth consecutive deferral should
escalate to Red Team under criterion 4's spirit without further debate.

**QUANTUM OPTICS (PROMISING).** Independently verified Block BEAM's
coherent-sum quadrature is numerically converged (n=21→321 changes C by
&lt;10⁻⁴) and smooth in θ0 — no bug, the near-|C|=1 numbers are real outputs
of the stated math. Traced the physics: this engine's aperture (≈75λ at
600nm) has a natural single-coherent-mode divergence of ≈0.76°; a genuine
single-mode coherent emitter with FWHM=20° divergence needs an aperture
≈2.5λ≈50 cells — 3–30× SMALLER than the fixed 75λ aperture every angular
component actually shares. Diagnosis sharpened: this construction models a
deliberately BEAMFORMED/FOCUSED synthetic array (verified: coherent peak
lands within 0–2 cells of the pure ray-optics prediction
y=OBJ_Y+D_SP·tanθ0 for narrow-moderate FWHM, at ~250–340× a single
component's own peak), not a naturally-divergent single-mode emitter —
"artifact of holding the aperture FIXED while imposing an angular power
spectrum on it," a more precise diagnosis than "artifact of coherence."
Ranked #1 (zero-cost): an aperture-consistent single-coherent-mode beam
(shrink the taper to the diffraction-implied width per FWHM, inject one
angle) — predicted to land much closer to the incoherent reading.

**VISION SCIENCE (PARTIAL, self-review) — see ERRATUM below.** Confirmed
Block MAGNITUDE's discipline (no rounding-up anywhere). Load-bearing
attack: `beam_divergence_incoherent`/`beam_divergence_coherent` both use
the SAME raw (c=1, uncorrected) pathway `edge_diffraction_c_empty` uses —
Block BEAM never applies Block MAGNITUDE's own best-fit c* correction
anywhere, despite Block MAGNITUDE's own fit showing systematic
under-prediction by roughly that factor. Applying the committed c*=2.6023
to Block BEAM's own largest incoherent cell (0.0030, 750nm/θ0=38°/
FWHM=2°) gives ≈0.0078 — ABOVE C_thr=0.005, reversing P-BEAM1's own "zero
of 36, CONFIRMED exactly" headline for at least that cell. Ranked #1
(zero-cost): re-score Block BEAM against both c=1 and c=c*.

**RED TEAM — numbered findings, independently re-derived (redid the
load-bearing arithmetic from scratch, not taken on any seat's word), then
overall ruling:**

1. [inconsistency, LOAD-BEARING] EM's obliquity-derivation independently
   re-derived from Faraday's law and CONFIRMED exact: for a locally-
   outgoing 2D cylindrical wave, Hy=Ez·cosψ/η — obliquity enters ONCE, via
   H, not squared via E. Source-model check against `lab/fdtd2d.py:
   235-237` confirms `add_line_source` is soft/additive (an array of
   independent driven currents), not a fixed-field screen — EM's physical
   characterization is correct, not merely plausible. Red Team's own
   independent implementation reproduces EM's numbers exactly:
   sign=27/30, R²(c=1)=0.6570, c*=1.6196, R²(c*)=0.7852.
2. [inconsistency, LOAD-BEARING] The corrected convention's numeric
   agreement with VISION's own original (mandatory-fix-3-superseded)
   preliminary run — 0.6570 vs. 0.656, 1.6196 vs. "≈1.6" — is far tighter
   than coincidence; a strong (not certain, VISION's original code isn't
   preserved) identification of that fix's own "fourth, undisclosed
   implementation choice."
3. [inconsistency, LOAD-BEARING, STRENGTHENED] VISION's Block-BEAM/c* gap
   independently re-verified and found to SURVIVE the EM correction, not
   dissolve with it: recomputing Block BEAM self-consistently under EM's
   own corrected convention still gives 0/36 at c=1 (worst cell −0.004006,
   same 750nm/θ0=38°/FWHM=2° cell, margin below threshold shrinks from
   40% to 20%) — but applying THAT convention's own best-fit c*=1.6196 to
   its own worst cell gives −0.006489, still above threshold. In every
   methodologically self-consistent combination tested (committed
   convention × its own c*; corrected convention × its own c*), at least
   the worst cell flips above C_thr — only an illegitimate cross-
   convention shortcut avoids a flip.
4–8. [verified, correctable] PHOTONICS' per-λ c* trend, MATERIALS' ×1.5-
   rescale finding and its own not-zero-cost correction, QUANTUM's
   aperture/beamforming critique, and THERMO's three-cycle deferral count
   all independently re-verified exact — none load-bearing to the
   committed record beyond what's already corrected below.
9. [inconsistency, minor, unfixable] Commit `a138cd7`'s own subject line
   ("...under the physically-correct incoherent reading") states as
   settled fact exactly what findings 1 and 3 show is not settled — git
   history is immutable by house discipline; this NOTES.md erratum is the
   flag, per T10's own precedent.

**Overall ruling: mandatory same-shift erratum required** (below) —
neither KILL nor silent acceptance; this is ordinary scientific
self-correction via the panel's own blind-fresh-context design, not
program-integrity drift, PROVIDED the erratum is applied this same shift.

## ERRATUM (Panel Iteration 19 Phase 5 — mandatory same-shift correction,
## per Red Team's Tier-0 ruling; original Phase 1–4 text below stands
## unmodified, per house convention — T10's own precedent: flag and
## correct, never silently rewrite)

**The committed PRIMARY convention (`edge_diffraction_c_empty(...,
obliquity=True)`, R²(c=1)=0.4176/c*=2.6023/sign=28/30) applies the
Rayleigh–Sommerfeld obliquity factor to each Huygens wavelet's FIELD
before the coherent sum — the correct recipe for a Kirchhoff/RS
fixed-field APERTURE SCREEN problem. This bench's actual source
(`lab/fdtd2d.py:132-172,235-237`, verified directly) is a soft, ADDITIVE
array of independently-driven line currents, not a fixed-field screen —
Faraday's law gives Hy=cosψ·Ez/η per wavelet, so obliquity enters flux
ONCE, via H, not squared via E.**

**A CORRECTED convention (`edge_diffraction_c_empty_corrected`,
`erratum.py`, added this shift — bare/no-obliquity coherent E-sum,
obliquity-weighted coherent H-sum, Sx=−Re(Ez·conj(Hy))) is now this
experiment's best physically-grounded reading:**

- **Block MAGNITUDE (corrected): sign=27/30, R²(c=1)=0.6570, c*=1.6196,
  R²(c*)=0.7852** — better-fitting at c=1 than the committed convention
  (0.4176) AND better physically justified. **R²=0.4176/c*=2.6023 should
  not be re-cited elsewhere as "the physically-correct flux reading"
  without this caveat attached** — it remains a valid, internally-
  consistent, pre-registered-and-scored measurement (P-MAG1/2 both
  CONFIRMED against it, honestly), just not the best available physical
  model. The naive/secondary `|E|²` reading (R²=0.7787, c*=1.1547) stands
  unchanged, still context-only.
- **Per-λ (corrected): 450nm 9/10 (new miss at θ=−39°), 600nm 10/10 (zero
  misses), 750nm 8/10 (misses at θ=±39°, unchanged from the committed
  convention).** Under the corrected convention, 600nm is uniquely best —
  the original "nearest-2°-Nyquist" narrative DOES cleanly hold; the
  committed convention's "450nm and 600nm tied" finding does not survive
  this correction.
- **Block BEAM (corrected, incoherent, c=1): still 0/36 cells exceed
  C_thr=0.005** — largest cell −0.004006 (same 750nm/θ0=38°/FWHM=2° cell
  as the committed convention), margin below threshold shrinks from 40%
  to 20%. **Applying this convention's own best-fit c*=1.6196 to that
  cell: −0.006489 — ABOVE C_thr.** Cross-check against the committed
  convention's own worst cell × its own c*=2.6023: −0.007829, also above
  C_thr. **VISION's Phase-5 finding is CONFIRMED and does not depend on
  which convention is used: P-BEAM1's "zero contamination risk, CONFIRMED
  exactly" is correct strictly as an unscaled (c=1) reading; it does not
  resolve whether the T21 fringe poses contamination risk once either
  convention's own demonstrated systematic under-prediction is accounted
  for.** The contamination-risk question T21/Block BEAM set out to answer
  is **NOT closed** by this cycle.
- **Full-grid flip count** (c* applied to every one of Block BEAM's 36
  cells, each convention self-consistently): committed convention **2/36**
  cells flip above threshold (750nm/θ0=38°/FWHM=2° at −0.00783; 600nm/
  θ0=36°/FWHM=2° at −0.00540); corrected convention **1/36** (the same
  750nm/θ0=38°/FWHM=2° cell). *(Correction to Red Team's own Phase-5 text,
  which cited "6/36" for the committed convention — the Director's
  independent recomputation, `erratum.py`, run this shift and checked
  against `results.json` directly, finds 2/36; the single-cell finding
  central to Question B, which is what actually matters for the
  contamination-risk verdict, is unaffected and reproduces exactly either
  way. Flagged per this program's own verify-independently discipline —
  Red Team's own arithmetic gets the same scrutiny as any other seat's.)*

**Nothing above changes**: MATERIALS' domain-mismatch disclaimer, the
realizability-relevance cap, P-MAG1's CONFIRMED sign-agreement verdict
(27/30 also lands inside the pre-registered [26,30] band), THERMO's
disposition, or any constraint-1/2/4 bookkeeping. Full corrected data:
`results.json`'s new `"phase5_erratum"` key.

### Director's close of Iteration 19

**Verdict: PARTIAL** (Red Team's adjudication, all six Phase-5 seats
consulted: 3 PROMISING — PHOTONICS, EM, QUANTUM OPTICS — 3 PARTIAL —
MATERIALS, THERMO, VISION). The magnitude-level mechanism confirmation is
genuine and now independently re-verified FOUR separate ways (VISION's
prototype, PHOTONICS' and Red Team's Phase-2 reimplementations, and this
shift's own corrected-convention rederivation) — T21's fringe is real,
mechanistically explained, and validated at magnitude level, not just
sign/ranking, closing Iteration 18's own specific gap. But the two
headline claims built on top of it this shift — "the physically-correct
flux convention" and Block BEAM's "zero contamination risk, exactly" —
both required a load-bearing, same-shift correction, and the corrected
picture is genuinely LESS settled, not more: even the best-grounded
convention available still flips Block BEAM's worst cell above threshold
once its own best-fit correction is honestly applied. This is the same
pattern this program has hit repeatedly (T10, T15, T20→T21 itself): a
Phase-5 fresh-context read catching a modeling choice Phase 1–4 didn't
examine — the process working exactly as designed, this time on the
cycle's own headline claim rather than a peripheral one, which is why this
closes PARTIAL rather than PROMISING. **No Checkpoint criterion fires**
(Red Team's ruling, adopted): criterion 4 does not fire because this is
ordinary panel self-correction, applied in this same shift with an
explicit erratum, not left uncorrected into a next cycle — but Red Team
weighed this seriously given the object corrected is a headline physics
convention in an already-pushed commit, not a wording gap, and states
plainly this should NOT be read as establishing that pattern is generally
safe from criterion 4 — only that catching and fixing within the same
shift, as done here, is what keeps it from firing. **THERMO's own
tripwire stands, independently, as Iteration 20's own binding
instruction**: a fourth consecutive deferral of docket #7/`thermo_sidecar`
fires criterion 4 without further debate.

**Next lead per rotation: PHOTONICS** (Iteration 20; VISION→PHOTONICS→
MATERIALS→ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→repeat).

**Ranked priorities for Iteration 20** (Red Team's tiered synthesis,
adopted in full):

**Tier 0 (mandatory, applied this shift):** the erratum above.

**Tier 1 (zero/low-cost):**
1. Docket #7 + `thermo_sidecar.py` rescoping (THERMO's own #1 ask,
   three-cycle deferral, tripwire live for Iteration 20 — a FOURTH
   deferral fires Checkpoint criterion 4 without further debate).
2. Bridge Block BEAM's now-unresolved contamination-risk question: re-
   score against both c=1 and c=c* as a committed table (VISION's #1,
   doubly motivated by the erratum), and/or build the genuine partial-
   coherence (Gaussian Schell-model) bridge (QUANTUM's #2) — paired with
   a sourced real-flashlight coherence-length/beam-FWHM figure (VISION's
   #2, van Cittert–Zernike against a cited bulb/LED geometry).
3. QUANTUM's aperture-consistent single-coherent-mode beam check (shrink
   the taper to the diffraction-implied width per FWHM, inject one angle)
   — cheapest test of whether the coherent reading is a beamforming
   artifact; directly informs priority 2.

**Tier 2 (real FDTD, moderate cost):**
4. The settling-margin FDTD test (PHOTONICS'/EM's #1 — rerun a few
   exp-041 points at increased STEPS) — the one falsifiable discriminator
   between causal-transit-margin and Yee-grid dispersion as c*'s driver,
   sharper now that the corrected c*≈1.62 is smaller but not zero.
5. MATERIALS' resolution-refinement leg (cross-score against
   N17_NATIVE_V2, now correctly costed at ~8–17 new FDTD calls) — a real
   diagnostic on whether c* is resolution-dependent, enabled by MATERIALS'
   own Phase-5 finding that the two domains are an exact λ-normalized
   rescale of one scenario.

*Deprioritized, with reasons*: a program-wide re-audit of every N17-vs-N9
citation for this obliquity-convention error (unnecessary — the correction
is a predictor-side artifact of this analytic bridge only, and touches no
FDTD-measured `results.json` row anywhere in the program, exp-041's
included); reopening `REALIZABILITY_MEMO.md` Amendment 1's own wording
(correctable but non-urgent — the substantive disclaimer already in place,
no verdict moves).
