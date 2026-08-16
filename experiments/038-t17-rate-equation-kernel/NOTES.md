# exp-038 — The T17 Rate-Equation Kernel

Panel Iteration 15 · Runner: cloud panel shift · Lead: MATERIALS & METAMATERIALS (rotation)

Full seven-seat cycle: Phase 1 proposal (MATERIALS) → 5 blind parallel critiques
(PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE —
unanimous **support-with-changes**, five non-overlapping fixes) → Red Team last
with everything (verdict: **proceed-with-mandatory-fixes**, 6 numbered attacks,
full independent re-derivation and adjudication of all five seats' fixes) →
Phase 3 synthesis (this file) → predictions committed here, before any run →
Phase 4 build + run. Verbatim panel transcript: this shift's session record
(LOGBOOK.md Iteration 15 carries the full text).

## Pre-flight (this shift)

Fresh container, deps installed per the recorded wrinkle (numpy/scipy/
matplotlib/pillow/autograd/fdtd via pip, then `ceviche --no-deps`). Bench
trust suite 41/41 green (`--only 12346789`) before this shift's work.

**T18 re-confirmation (Director, before Phase 1):** re-tested WebFetch this
shift against three scholarly domains (arxiv.org, semanticscholar.org,
nature.com) — all three returned `EGRESS_BLOCKED`. WebSearch itself works.
This is the fourth consecutive confirmation of T18's blockage in a fresh
container. PLAN.md's Iteration-15 priority #1 (retroactive re-verification
"via a working full-text access route if one can be found") has no route
available this shift; priority #2 (escalating the blockage) is not something
a panel proposal can fix — it is a network-policy matter outside agent
control, already logged as "escalation overdue" in T18, and is reported to
Marsh as part of this shift's own record rather than left implicit. That
leaves priority #3 — build the T17 rate-equation kernel in-engine — as this
cycle's executable candidate, which MATERIALS (this cycle's lead) proposed.

## Hypothesis

Iteration 14 closed with three independent seats (QUANTUM OPTICS, VISION
SCIENCE, ELECTROMAGNETISM, across two cycles) naming the same Iteration-15
build: a validated numerical integrator for T17's kinetics equation
dn/dt = k_f(I)(1−n) − k_r·n, to bench-test the at-rest population directly
rather than resting on hand-derived closed forms. The pre-registered
hypothesis: (a) a correctly-built integrator reproduces the closed-form
logistic solution to machine precision; (b) the linear-vs-logistic
divergence EM flagged at Iteration 14's close is a real, exactly-r
discrepancy across exp-037's own open n_ss range; (c) constraint 4's
"a later sweep passes unimpeded" claim, tested directly via repeated
beam-transit pulses, holds for inter-pulse intervals long compared to the
kinetics class's own relaxation time and does not hold in general for short
intervals — with the specific prediction that whichever host regime has the
largest achievable n_ss also has the slowest relaxation, so the two
"risk axes" this thread has separately worried about turn out to co-locate,
not vary independently.

## Phase 1 — Proposal (MATERIALS, abridged)

Full verbatim: this shift's session record. Proposed a standalone, 0D,
kinetics-only numerical kernel (no `Sim`, no FDTD calls) — two cross-checked
propagators (an exact-exponential piecewise-constant stepper as primary, an
RK4 cross-check), a 5-host (carrier-lifetime) × 5-ratio (k_f/k_r) = 25-point
sweep grid anchored to exp-037's own cited fast/long-lifetime FCA hosts plus
two deliberate MATERIALS-owned boundary probes (Host E, r=1), a
constraint-3-at-rest test (Test A: time to 99% of n_ss) and a constraint-4
test (Test B: repeated beam-transit pulses at two inter-pulse intervals,
5τ and 0.5τ). New machinery: `lab/kinetics.py` + trust-suite stage 12, at
least one absolute identity gate (exact reproduction of the closed-form
logistic solution). Explicitly scoped as NOT touching T1's central tension
and NOT a new escape route — T17 nests inside σ(I) but is materially
distinct (history-dependent, not memoryless).

## Phase 2 — Critique (five blind, then Red Team) — summary

All five blind seats independently returned **support-with-changes**:

- **PHOTONICS**: the k_f grid values are traceable to Soref & Bennett's
  cross-sections, already flagged (PLAN.md Iteration-15 priority #1,
  LOGBOOK Iteration 14) as applied unscaled from their telecom source
  wavelength — risking laundering a known defect into gate-clean numbers.
  Required either per-point wavelength disclosure or an explicit
  dimensionless/λ-decoupled framing.
- **THERMODYNAMICS**: "no thermal feedback modeled" is not the same claim
  as "no THERMO sidecar owed" — Iteration 14's own precedent (a THERMO
  estimate ruled "load-bearing, not queueable" at zero FDTD cost) applies
  identically here. Required a ΔT_ss post-processing step.
- **ELECTROMAGNETISM**: Test B is described as "smoothly time-varying" but
  is actually a discontinuous step function — undermining the RK4
  cross-check's claimed convergence order and gate 4's validity. Required
  fixing the profile/stepper mismatch.
- **QUANTUM OPTICS**: the adiabatic-elimination assumption (dephasing fast
  vs k_f, k_r) — needed for the rate equation to be a valid reduction of
  real two-level population dynamics — was never stated. Also flagged risk
  of conflating Test B's `A` (a bare irradiance ratio) with T18's
  field-enhancement factor (a different physical quantity). Required both
  disclosures.
- **VISION SCIENCE**: P-MAT-5's "(negligible buildup)" language and its
  "constraint 4 is satisfied by this kinetics class" framing reuse
  PANEL.md's own perceptual-scoring verbs for an uncarried population
  fraction — the identical language-cap violation Iteration 14 caught on
  this seat's own prior cycle. Required rewording plus restating the
  T3-provisional tag at P-MAT-5's own point of claim, not just P-MAT-4's.

**Red Team (PROCEED-WITH-MANDATORY-FIXES).** Independently re-derived
every seat's claim rather than trusting characterizations, and found two
defects none of the five blind seats caught:

1. **[inconsistency]** P-MAT-3's own predicted-value table contradicts the
   "exact algebraic identity" (error = r, exactly) it claims, at 2 of 5
   points (1.001e-3/0.111 instead of the correct 1.000e-3/0.100) —
   independently re-derived by the Director (see below) and confirmed.
2. **[inconsistency]** The RK4 step-size spec ("Δt ≤ τ_min/20") is
   ambiguous between per-configuration and grid-global readings that differ
   by ~9-12 orders of magnitude in cost; the grid-global reading directly
   contradicts the "well under 1 second" cost claim.
3. **[inconsistency]** Gate 2's "n∈[0,1] exact by construction" is true for
   the exponential stepper (a provable convex-combination argument) but not
   for RK4, which needs an empirical check instead.
4. **[inconsistency]** Confirmed EM's Test-B/RK4 mismatch independently and
   ruled it must be fixed jointly with attack #2, not separately.
5. **[inconsistency, minor]** The proposed stage name `stage12_...` was
   never wired to `__main__`'s `--only` parsing; under the existing naive
   `"12" in only` substring convention, stage 12 would **silently fire on
   every existing invocation**, including CI's own `--only 12346789` and
   the local default `123456789` (both happen to contain "1" immediately
   followed by "2"), purely by accident of decimal-digit concatenation.
6. **[constraint-4-violation]** Independently confirmed VISION SCIENCE's
   catch against PANEL.md's own constraint-4 definition (an observer-side
   perceptual criterion, not a population-fraction threshold) and flagged
   that, if uncorrected, this would be the third consecutive cycle this
   exact language-cap pattern occurred on the VISION SCIENCE seat's own
   cited quantities — a program-integrity trend worth escalating if it
   recurs a fourth time.

Adjudication of the five seats' fixes: **PHOTONICS adopted in full**
(re-verified against PLAN.md/LOGBOOK directly); **ELECTROMAGNETISM adopted,
folded together with Red Team's own attack #2** (fixing the discontinuity
alone while leaving Δt underspecified doesn't close the gap); **QUANTUM
OPTICS adopted in full** (both disclosures, cheap and correct);
**VISION SCIENCE adopted in full** (independently re-verified, no part
rejected); **THERMODYNAMICS adopted in substance, rejected as literally
stated** — converting n(t) to ΔT_ss needs a photon-energy/site-density
parameter that exists in neither the proposal's table nor THERMODYNAMICS'
own fix text, and that derivation is explicitly out of this cycle's scope
(Section 5's own idealization). Director's resolution below.

## Phase 3 — Synthesis (2026-08-16, Director)

**All six Red Team mandatory-fix items adopted in full. No criticism
overridden.** Independently re-verified attack #1 (P-MAT-3 arithmetic) and
attack #5 (the stage-wiring collision) myself before accepting them — both
confirmed exactly as Red Team stated (see "Director's independent checks,"
below). Final synthesized configuration:

**1. P-MAT-3 table corrected.** (n_lin−n_exact)/n_exact = r exactly, for
all r (algebraic identity: n_lin=r, n_exact=r/(1+r), so the difference is
r²/(r/(1+r))·... simplifies to r — verified numerically to double
precision, see below). Corrected predicted values at r =
10⁻⁹/10⁻⁵/10⁻³/10⁻¹/1: **1.000×10⁻⁹ / 1.000×10⁻⁵ / 1.000×10⁻³ / 1.000×10⁻¹
/ 1.000**, each to ≤1×10⁻¹⁰ relative — matching Section 7's gate
description (which was already stated correctly; only the Section-4 table
had the error).

**2. RK4 step size pinned per-configuration, not grid-global.** For each of
the 25 (k_f, k_r) grid points, Δt = τ_local/20 where τ_local = 1/(k_f+k_r)
for whichever segment (ambient or pulsed) is currently being integrated —
never the single global minimum across all 25 points. This keeps Section
8's "well under 1 second" cost estimate valid (re-verified: worst case is
Host A/r=1 integrated on its own 25-point-independent Δt, not against
Host A's τ borrowed by a slower host).

**3. Test B redefined explicitly as piecewise-constant** (ambient →
ambient·A → ambient — a step function, not smooth), removing the
"smoothly time-varying" language that contradicted its own definition.
**RK4's step grid is pinned exactly to the five pulse-edge transition
times** — RK4 restarts fresh at each edge using that segment's own
per-configuration Δt (resolution #2), so it never integrates across a
discontinuity mid-step. This resolves EM's attack and Red Team's attack #4
jointly, as required. (A genuinely smooth ramp profile, needed if a future
cycle wants to test a state-dependent/bleaching-feedback generation law,
stays explicitly out of scope — parked, not built, this cycle.)

**4. Gate 2 rescoped into two gates.** Gate 2a (exponential stepper):
n(t)∈[0,1] **exact by construction** — n(t) is a convex combination of n0
and n_eq (both in [0,1]) by the closed-form update's own algebra, so no
run-time violation is possible; the suite check is a construction-validity
assertion, not a numerical tolerance. Gate 2b (RK4): n(t)∈[−1×10⁻⁹,
1+1×10⁻⁹] (floating-point slack only) **empirically checked**, explicitly
labeled as empirical, not exact-by-construction, per Red Team's ruling.

**5. Suite wiring fixed at the root, not papered over.** The naive
`"12" in only` substring check is broken for a stage numbered "12"
specifically because "1" immediately followed by "2" already appears at
the start of every `--only` string that includes both stage 1 and stage 2
(the local default `123456789` and CI's own `12346789` both qualify) —
confirmed by direct test (see below). Fix: stage 10, 11, and the new stage
12 are now gated by a digit-boundary-aware regex,
`re.search(rf'(?<!\d){N}(?!\d)', only)`, instead of plain substring `in`.
Verified this correctly EXCLUDES stage 12 from both the local default and
CI's `--only 12346789`, and correctly INCLUDES it when explicitly requested
(e.g. `--only 12` alone, or a comma-joined `--only 5,12`). This also
retroactively hardens stage 10/11's own gating, which shared the identical
latent fragility (undocumented until now) purely by not having been
triggered yet.

**6. VISION SCIENCE's P-MAT-5 language fixes applied verbatim**, per the
seat's own proposed rewording (below).

**7. THERMODYNAMICS' sidecar rescoped, not rejected.** Converting n(t) to
an absorbed-power/ΔT figure needs a photon-energy and absorbed-power-density
(or site-density) input this cycle's parameter table does not supply
(deliberately — Section 5 scopes the k_f↔σ_abs microphysics derivation out,
naming it PHOTONICS' territory). Borrowing exp-037's own ΔT_ss≈7mK figure
and scaling it to this cycle's n_ss grid would require knowing that
estimate's own underlying reference n_ss precisely enough to scale
correctly — the Director does not have that figure memorized precisely
enough to do so honestly without risking a fabricated linkage, and
Red Team's own ruling explicitly permitted "an honest n/a" as the
alternative to a disclosed borrowed figure. **Decision: THERMO sidecar
marked N/A this cycle for all 25 grid cells**, with the reason stated
explicitly (no photon-energy/site-density parameter in scope) rather than
silently omitted — queued as a genuine follow-up once PHOTONICS'
already-queued wavelength-retag (PLAN.md priority #1) supplies real
absorbed-power-density inputs a sidecar could correctly use.

**8. QUANTUM OPTICS' two disclosures added** to Section 5 (Idealizations,
below) verbatim.

### Director's independent checks (before commit)

- **P-MAT-3 arithmetic**, computed directly in Python at each of the 5
  ratio points: errors came back 1.0000e-9 / 1.0000e-5 / 1.0000e-3 /
  1.0000e-1 / 1.0 relative to r — confirms Red Team's correction exactly,
  refutes the original proposal's table at r=10⁻³ and r=10⁻¹.
- **Stage-12 wiring collision**, tested directly: `"12" in "123456789"` →
  `True`; `"12" in "12346789"` (CI's own string) → `True`. Both would have
  silently fired stage 12 under the original naive scheme. The
  boundary-aware regex correctly returns `False` for both strings and
  `True` for an explicit `"12"` or `"5,12"` request.

## Final parameter table (corrected, as it will actually run)

Unchanged from Phase 1 except where noted above: ODE
dn/dt = k_f(I)(1−n) − k_r·n, k_f(I) = G·I (linear, thresholdless); 5 hosts
(τ_r = 1ns/1µs/1ms/100ms/1s) × 5 ratios (r = 10⁻⁹/10⁻⁵/10⁻³/10⁻¹/1) = 25
grid points; Test A (at-rest reach time, t₉₉); Test B (5 repeated pulses,
A∈{10,10³,10⁶}, Δt_sweep∈{5τ, 0.5τ}, now explicitly piecewise-constant with
RK4 pinned to pulse edges).

## Falsifiable predictions (pre-registered, corrected, committed before run)

**P-MAT-1 (exact reproduction gate).** Relative error, exponential stepper
vs closed-form logistic, constant-I, all 25 points: central ~1×10⁻¹⁵,
band ≤1×10⁻¹². *Falsified by any single point exceeding the band.*

**P-MAT-2a (exp-stepper boundedness, exact by construction).** n(t)∈[0,1],
zero violations — provable, not merely predicted; a violation would
indicate an implementation bug, not new physics.

**P-MAT-2b (RK4 boundedness, empirical).** n(t)∈[−1×10⁻⁹, 1+1×10⁻⁹] across
all Test-A/B evaluations. *Falsified by any excursion outside this
floating-point-slack band.*

**P-MAT-3 (linear-vs-logistic divergence, corrected).** Relative error of
the linear approximation equals r exactly at all 5 ratio points:
1.000×10⁻⁹ / 1.000×10⁻⁵ / 1.000×10⁻³ / 1.000×10⁻¹ / 1.000, each ≤1×10⁻¹⁰
relative. **Materials read (unchanged):** exp-037's own upper-bound
n_ss≈10⁻¹ figure sits at exactly 10% linear-approximation error — the edge
where "which formula governs" starts to matter numerically.

**P-MAT-4 (transient time constants vs T3's provisional window,
unchanged).** t₉₉ = 4.605·τ: Host A ~5ns, B ~5µs, C ~5ms, D ~0.3–0.5s, E
~3–5s. **Prediction: only Host D's points land inside/near T3's provisional
10ms–1s window**; Hosts A–C sit 3–8 orders of magnitude below it, Host E
exceeds the upper bound. Explicitly T3-provisional (unsourced band) — not a
scored perceptual verdict.

**P-MAT-5 (sweep-to-sweep memory, Test B — reworded per VISION SCIENCE's
mandatory fix).** For Δt_sweep=5·τ: periodic/first-pulse peak-n ratio
≤1.02 — **T3-provisional; not a scored perceptual verdict** (restated here,
at this point of claim, not only at P-MAT-4's). For Δt_sweep=0.5·τ (stress
case): periodic/first-pulse peak-n ratio ≈1.4–1.6 — **T3-provisional; not
a scored perceptual verdict** — predicted measurable only at Hosts D/E, the
same regime P-MAT-4 already flags as slowest and the tier table (below)
already flags as having the largest achievable n_ss. **This kinetics
class's population-level relaxation criterion is met whenever the real
inter-sweep interval exceeds ~5·τ — not a constraint-4 perceptual verdict,
which needs T3's still-unbuilt instrument and a carried
ε_colored/path-length/geometry/threshold chain this cycle does not
provide.**

## Idealizations

Unchanged from Phase 1, plus the two Iteration-15 additions:

- 0D, kinetics-only, decoupled from the FDTD Maxwell solver. I(t) externally
  imposed, not measured from a running EM scene. No spatial coupling into
  any `Sim` this cycle.
- k_f independent of n (no bleaching/saturation feedback). No bistability/
  multi-valued steady states — single-well relaxation kinetics only.
- Rate constants temperature-independent — no thermal feedback on (k_f,
  k_r) themselves modeled.
- **THERMO sidecar: N/A this cycle for all 25 grid cells** (Director's
  Phase-3 resolution, above) — no photon-energy/site-density parameter in
  scope; queued once the wavelength-retag priority supplies one.
- No perceptual scoring attaches to any n_ss or n(t) value this cycle —
  enforced at every point of claim this time, not only in a caveats
  section (P-MAT-4 and P-MAT-5 both restate the T3-provisional tag).
- k_r host-lifetime anchors and A values are order-of-magnitude, inherited/
  bounded from exp-037's own cited figures where possible, flagged as
  MATERIALS' own extension where not (Host E, r=1) — and, per PHOTONICS'
  adopted fix, **explicitly disclosed as wavelength-untagged**: this grid
  is a dimensionless (k_f, k_r) exploration, decoupled from any specific λ
  or from exp-037's telecom-anchored figures until the still-open
  wavelength-retag priority (PLAN.md #1) lands. No claim here should be
  read as validating a real, wavelength-specific FCA host.
- **QUANTUM OPTICS' adiabatic-elimination disclosure**: the rate equation
  dn/dt=k_f(1−n)−k_r·n is a valid reduction of two-level population
  dynamics only once coherence/dephasing (T2) is adiabatically eliminated —
  i.e. dephasing fast relative to 1/k_f and 1/k_r. Assumed valid for
  incoherent CW/ambient pumping (this cycle's regime); NOT asserted for
  coherent ultrafast excitation.
- **QUANTUM OPTICS' A-vs-field-enhancement disclosure**: Test B's `A`
  (peak/ambient generation-rate enhancement, dimensionless) is a bare
  irradiance ratio, NOT T18's resonant near-field/plasmonic
  field-enhancement factor — a different physical quantity. No result this
  cycle should be cited as field-enhancement evidence.
- Does not re-derive k_f from I_ambient/G/σ_abs microphysics (PHOTONICS'
  territory, not exercised here).

## Realizability bound (MATERIALS' own charter, unchanged from Phase 1)

Addresses the T17 at-rest axis (n_ss magnitude, sweep-to-sweep memory) —
does not override Amendment 2's existing D_req/dynamic-range verdict for
linearly-pumped FCA (UNOBTANIUM-WITH-PARAMETERS, unchanged).

| Regime | n_ss (predicted) | Tier | Basis |
|---|---|---|---|
| Hosts A–B (r≤10⁻³) | ≤10⁻³ | PUBLISHED | routine doped/defect-engineered Si, Ge carrier lifetimes |
| Hosts C–D, r∈[10⁻³,10⁻¹] | 10⁻³–9×10⁻² | PLAUSIBLE | long-minority-carrier-lifetime Si, less common in engineered devices |
| Host E (any r) | — | UNOBTANIUM-WITH-PARAMETERS | boundary probe, beyond any published device-grade lifetime |
| r=1 (any host) | 0.5 | UNOBTANIUM-WITH-PARAMETERS | boundary probe |

## New machinery / trust-suite stage (final, corrected)

`lab/kinetics.py`: `integrate_two_state(k_f, k_r, t_span, n0=0.0,
I_profile=None, method="exp"|"rk4")`. Suite stage 12
(`stage12_kinetics_kernel`), gated via a digit-boundary regex (not plain
substring `in`), verified excluded from both the local default and CI's
`--only 12346789`, includable via an explicit `--only 12` or `--only
5,12`-style request. Gates: (1) P-MAT-1, absolute, ≤1e-12. (2a) P-MAT-2a,
exact-by-construction. (2b) P-MAT-2b, empirical, RK4 slack band. (3)
P-MAT-3, absolute, ≤1e-10, corrected table. (4) empirical convergence,
exp-stepper vs pulse-edge-pinned RK4, RMS relative difference ≤1e-6 on
Test B's actual (piecewise-constant) trajectory.

## Cost note

Unchanged: pure Python/numpy scalar-ODE integration, zero FDTD calls, zero
WebSearch/WebFetch calls. Estimated well under 1 second wall-clock
(re-verified valid under the corrected per-configuration Δt, resolution
#2).
