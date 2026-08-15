# exp-034 — The Paired Floor-Convergence / r=156 Scale-Bridge Cycle

Panel Iteration 11. Lead: **THERMODYNAMICS** (rotation). Runner: cloud panel
shift, 2026-08-15. Full seven-seat cycle recorded verbatim in LOGBOOK.md
Iteration 11; this file is the experiment-local record — hypothesis, setup,
idealizations, and the predictions committed to git **before** any scored
run (house discipline, non-negotiable).

## Hypothesis

Iteration 10 closed with two Director-ranked, high-priority items, and Red
Team's explicit instruction to pair them in one cycle rather than sequence
them: (1) a third resolution point (cpl=40) testing whether the empty-scene
decision floor and the actually-scored raw-C currency are converging or
diverging (the floor got *worse*, physically anomalously, at cpl 20→30);
(2) VISION's r=156 `off_pass` scale-bridge leg — a committed, unconditional
Iteration-11 trigger with a Checkpoint-4 tripwire on non-execution, carrying
three mandatory riders from prior Phase-5 reviews (dual-currency
pre-registration, a fresh δ_C(156) remeasurement, an N17 angular-quadrature
convergence check).

exp-034 runs **four independent blocks**, none gating another's execution,
reconciled only at Phase 5 — see design_geometry.py for the full parameter
tables (every number computed/asserted in code, not hand-copied).

## Phase 1 — Proposal (THERMODYNAMICS, abridged; full verbatim text:
LOGBOOK.md Iteration 11)

Three blocks proposed: **CPL40** (a third resolution point, r=78 physical,
self-similar RATIO=2.0 rescale, empty+off_pass only, 20 calls), **R156**
(off_pass's PASS-boundary finding extended to r=156, exp-030's r-family
idiom, τ_center held fixed; off_lab/off_field reused verbatim from exp-030,
only off_bracket/off_pass/empty new, 27 calls), **N17** (a 17-angle,
±40°-span angular-quadrature convergence check on off_pass at r=156, on a
freshly-widened domain, 34 calls). Dual-currency pre-declared throughout:
raw C is the sole scored ladder currency; g_corr is a labeled diagnostic,
never substituted.

## Phase 2 — Critique (five blind, then Red Team) — summary

All five blind seats (PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM
OPTICS, VISION SCIENCE) independently verified the proposal's arithmetic to
the digit (no fabricated numbers found by any seat, nor by Red Team) and
returned **support-with-changes**, each catching a distinct or convergent
defect. **Three seats (PHOTONICS, QUANTUM, EM) independently converged** on
one root defect: Block R156's scale-invariance disposition (comparing the
r=156 fit intercept A₁₅₆ against the r=78 anchor A₇₈) risked being either
(a) guaranteed near-invariant by construction if the r=156-vs-78 floor
shift is common-mode across all four τ articles (EM), or (b) miscalibrated
because A₇₈ itself is not a portable reference — PHOTONICS' own Iteration-10
finding (T15) that g₀ sits ~15% below its own geometric chord model,
specific to this bench's own geometry (PHOTONICS, QUANTUM; Red Team
corrected the specific mechanism cited — z/z_R is the moving quantity, not
W_OBJ/r_out, which is an invariant ratio=1 across every geometry this
program has built). **MATERIALS** found the ε_r≡1 restriction — a fourth
recurrence across exp-031/032/033 of the same documentation gap — stated
once in §5 but not inline at the headline PASS/MARGINAL citations. **VISION**
found Block N17 (as proposed, at r=156 only) tests the wrong geometry: it
never retests the specific, still-standing, already-cited r=78/cpl=30
"first-ever σ(I) OFF-state PASS" (margin 4.14×10⁻⁴), whose own N5-vs-N9
convergence increment (4.8×10⁻⁴) already exceeds it — the letter of
VISION's own rider was met, its substance wasn't.

**Red Team (verdict: PROCEED-WITH-MANDATORY-FIXES).** Independently
verified every load-bearing number in the proposal and all five critiques
against the actual code/data — found no arithmetic error anywhere (a first
for this program's Red Team reviews, explicitly noted). Confirmed the
three-way PHOTONICS/QUANTUM/EM convergence as real and load-bearing, ruled
that **both** proposed fixes (EM's common-mode decomposition AND the
geometry-corrected chord-model null) are needed together, not either alone.
Corrected PHOTONICS'/QUANTUM's shared mechanism claim (W_OBJ/r_out is
invariant; z/z_R is the real moving axis). Confirmed VISION's attack and
corrected VISION's own cost estimate upward (~34 calls, not ~17–26 — a
properly-scoped check needs the full N9 subset rerun fresh on a re-derived
±40° domain, mirroring Block N17's own domain-widening discipline) —
**elevated to a Director budget call: fold in this cycle or make it
Iteration 12's unconditional trigger, do not silently drop a fifth time.**
Caught a real, unrecorded risk in the proposal's own run-count bookkeeping
architecture (a shared cross-block ARTICLES tuple would reproduce exp-033's
own 47→50 bug class) and elevated MATERIALS' documentation-gap attack from
recommended to mandatory (a fourth recurrence). Full sixteen... (seven,
this cycle)-attack verbatim record: LOGBOOK.md Iteration 11.

## Phase 3 — Synthesis (Director)

**All seven of Red Team's mandatory fixes accepted, folded into
`design_geometry.py`/`run.py`:**

1. **Run-count bookkeeping guard.** Each block computes its own scoped
   article list and sigma values from its own block-local `R_OUT`
   variable — no shared cross-block `ARTICLES` tuple. `run.py` asserts the
   actual call count against the committed table (115 total) at close.
2. **Common-mode-vs-differential floor decomposition** (EM's fix) —
   `block_r156()` computes ΔC(78→156) per article against established r=78
   native-cpl20 anchors and reports the spread/common-mode fraction
   *before* any SCALE-INVARIANT/DIVERGENT language is trusted.
3. **Geometry-corrected chord-model null** (PHOTONICS'/QUANTUM's fix,
   Red Team's mechanism correction). The exact formula PHOTONICS/QUANTUM
   used at Iteration 10 to derive g₀_geo is **not preserved anywhere in
   this repo** — checked directly (absent from exp-033's results.json,
   NOTES.md, and design_geometry.py; it was an in-session Phase-5
   derivation, never committed as reusable code). Rather than guess at an
   unrecorded formula and risk misattributing a fabricated number to
   another seat, this cycle **re-derives a fresh geometric (ray-chord,
   zero-free-parameter) null** (`design_geometry.py::chord_model_g0`),
   reusing the precedented weak-absorption chord idiom from exp-024's own
   `window_means(..., transmission=True)` — the same code path that
   originally validated the dilute-sponge calibration article to
   0.001–0.003 of itself. Evaluated at r=78-native: g₀_geo=0.6857 (1.9%
   from the measured A₇₈=0.689593 — a plausible, independently-obtained
   sanity bound, **not asserted to reproduce Iteration 10's own unrecorded
   number exactly**). Evaluated at r=156: g₀_geo=0.7012.
4. **ε_r≡1 restriction restated inline** at every PASS/MARGINAL headline
   below, not just once — flagging this as a **fourth recurrence** of the
   same documentation gap (exp-031/032/033/034), per Red Team's elevation.
5. **Block N17_NATIVE folded in, Director's budget call.** VISION's
   substance-attack is correct and load-bearing — the program's only-ever
   constraint-3 PASS citation (r=78/cpl=30) has never had its own quadrature
   convergence checked, and the check that exists (N5-vs-N9, at a
   *different* resolution, cpl=20) already shows the increment exceeds the
   PASS margin. Given the total run-count budget (81→115, +42%) is still
   modest against this program's own exp-030 precedent (89 calls, one
   block), and given this program's own standing lesson about deferring the
   same high-value check repeatedly (r=156 itself was deferred four times),
   this Director folds Block N17_NATIVE in **this cycle** rather than
   deferring a fifth time. Built at exp-033's own exact geometry (R_OUT=117,
   PLANE_DX=22 inherited unchanged, cpl=30), NY/GUARD_OUT re-derived at
   ±40° via the same formula validated against exp-030's own r=156/±35°
   numbers (see design_geometry.py's own self-check assertion).
6. **`lab/` build identity, stated explicitly.** Zero commits to `lab/`
   between exp-030 (Iteration 7) and this cycle — the trust suite is
   reconfirmed 46/46 green immediately before this cycle's run (see Phase
   4), with no diff against exp-030's own suite state at the time it
   produced the reused off_lab/off_field/empty(156) anchors.
7. **P-CPL40-2's disposition gap closed** — see Predictions, below.

**Director's own catch, Phase 3 (not raised by any Phase-2/Red-Team
seat — logged per house convention, flag don't silently fix):** the N17
angle set (`(-40,-30,-20,-10,0,10,20,30,40)` ∪ `N17_EXTRA`) is **exactly**
the "PRIMARY" ±40° geometry that Panel Iteration 2 (exp-024) found failed
the δ_C≤0.001 gate at **all six** λ/weighting combinations, non-
monotonically — and margin-widening (MARGIN_MULT 2.0→3.5) was tested and
**refuted** as the fix; only *dropping* the ±40° angles (adopting the
±35° fallback used ever since) resolved it. PLAN.md's own words:
"localizing the real mechanism to something angle-specific at ±40°, not
margin-ratio-driven." **Neither N17 block in this cycle can assume that
problem is margin-solved** just because this cycle's own coverage formula
computes a wider NY than exp-024's original failing geometry did — exp-024's
own MARGIN_MULT=3.5 test (a *much* wider margin than the original failing
geometry) *also* failed. This is why **P-N17-1 (the empty-scene coverage/
decision-floor gate) is treated as load-bearing and checked explicitly for
both N17 blocks before any N9-vs-N17 comparison is trusted** — a gate
failure here would not be a bug to route around; it would be this
program's second independent confirmation of a real ±40°-specific
artifact, itself a finding worth having, not a null result to discard.

**Overridden: none this cycle** — every Red Team fix was either accepted
outright or (fix 5) accepted with an explicit Director budget decision
(fold in, reasons stated above), not overridden or dropped.

**Checkpoint criterion 4 (r=156's own long-standing tripwire): does NOT
fire.** The committed r=156 `off_pass` leg (Block R156) executes this
cycle, unconditionally, as required.

## Parameter tables

See `design_geometry.py` for the complete, self-checking parameter tables
(every geometry value computed and asserted at import time — including a
self-check that this cycle's own generalized ±span-degree coverage formula
reproduces exp-030's established r=156/±35° geometry *exactly* before being
trusted at ±40°). Summary:

| Block | R_OUT (cells) | cpl | Angles | NX×NY | STEPS | New FDTD calls |
|---|---|---|---|---|---|---|
| CPL40 | 156 | 40 | N=9 (±35° fallback) | 720×3168 | 2800 (+1400 settling) | 20 |
| R156 | 156 | 20 | N=9 (±35° fallback) | 660×2480 | 2706 | 27 |
| N17_156 | 156 | 20 | N=17 (±40°) | 660×2672 | 2706 | 34 |
| N17_NATIVE | 117 | 30 | N=17 (±40°) | 540×2272 | 2100 | 34 |
| **TOTAL** | | | | | | **115** |

Wall-clock estimate: the Phase-1 proposal's own rate anchors (exp-030's
39.6 s/call, exp-033's 18.9 s/call) were measured on a different execution
environment. **A pilot timing check on this cycle's own hardware (this
program's own "pilot before committing" discipline, exp-030's §7
precedent) found this environment runs FDTD roughly 3× slower per call**
(N17_NATIVE single angle-group, 2 sim-calls: 113.8 s measured vs. ~38 s
anticipated from the proposal's rate anchors) — flagged honestly, not
smoothed over, echoing this program's own standing lesson about
proposal-time estimates needing margin (previously always attributed to
κ³ FDTD scaling; this time to environment/hardware variance, a new
category for this specific lesson). Revised estimate, 4 parallel workers
(only 4 CPUs available this environment, checked via `os.cpu_count()`):
CPL40 ≈16 min, R156 ≈15 min, N17_156 ≈18 min, N17_NATIVE ≈10 min ⇒
**≈60 minutes wall-clock total**, run in background.

## T1 escape-route statement

Unchanged from exp-032/033: **intensity-gated absorption σ(I)**,
instrumented here only at its static/linear OFF-state endpoint. Every
article in all four blocks is an ordinary uniform-conductivity disk:
σ_engine ≥ 0, real, frequency-independent, **ε_r ≡ 1.0 exactly — a
gas/aerosol-host-only idealization, load-bearing for constraints 2 and 3
alike: a realizable condensed-phase host (n=1.33–1.5) gives two-surface
ambient contrast C=−0.040 to −0.078 (VISION-ladder FAIL, independent of τ)
and specular return 143–571× the established camera floor (constraint-2
violation) — no PASS/MARGINAL number below is a material transfer
function** (mandatory fix 4, restated here and at every point of use).
Trivially reciprocal, causal, passive. Nothing switchable, time-varying, or
intensity-dependent is built or claimed anywhere in this cycle. The
realizability tension this line has already established (σ_on/σ_off ≈
537–600×; the 9–12 order-of-magnitude flashlight-irradiance-vs-RSA/
two-photon-onset gap) is **untouched by this cycle** — MATERIALS'
Phase-2 review independently confirmed D_req=τ_on/τ_off=600× exactly,
algebraically R_OUT-independent, so nothing in this cycle can move that
number in either direction.

## Predicted outcomes (falsifiable bands, committed BEFORE the scored run)

**P-CPL40-1 (primary, data quality/trend).** Empty-scene decision floor at
600nm/cpl=40: established floor(20)=3.3166×10⁻⁵, floor(30)=1.165×10⁻⁴ (a
3.51× jump, physically anomalous). Three-way disposition, gap-closed
(mandatory fix 7): **CONVERGING** floor(40) < floor(30); **DIVERGING**
floor(40) ≥ 1.4×10⁻⁴; **PLATEAU** 0.93×10⁻⁴ ≤ floor(40) < 1.4×10⁻⁴ (closed
interval, no gap). No strong prior — PHOTONICS' own finding that this
bench's floor is non-monotone/non-convergent across λ gives no basis to
expect convergence here specifically.

**P-CPL40-2 (primary, scored) — raw C(off_pass, 600) trend, ε_r≡1
gas/aerosol-host-only (mandatory fix 4).** Established: |C(20)|=0.00450,
|C(30)|=0.00459. **CONTINUING** |C(40)| ≥ 0.004636; **REVERSING**
|C(40)| ≤ 0.004545; **PLATEAU** 0.004545 < |C(40)| < 0.004636 (gap
closed). **PASS-AT-RISK:** |C(40)| ≥ 0.0050 flips this program's
only-ever σ(I) OFF-state PASS to MARGINAL.

**P-CPL40-3 (settling control).** |ΔC|/|C| between STEPS=1400 and
STEPS=2800 at θ=0 ≤ 3%.

**P-R156-1 (data-quality gate).** Free 4-point g_corr(τ) fit residual ≤
3.0×10⁻³ (reused verbatim from exp-033; per Red Team's own mechanism
correction, this gate detects floor-*mismeasurement*, not floor *size*, so
it is correctly NOT rescaled for r=156's much larger δ_C).

**P-R156-2a (common-mode decomposition, mandatory fix 2, computed
BEFORE any disposition language).** ΔC(78→156) per article (off_bracket,
off_pass, off_lab, off_field) against established r=78/native-cpl20
anchors. **COMMON-MODE** (guaranteed-by-construction risk): the four
deltas' spread is ≤20% of their mean magnitude. **DIFFERENTIAL** (real
τ-dependent curvature): spread > 50% of mean magnitude. Between: reported,
not forced into either label.

**P-R156-2b (geometry-corrected disposition, mandatory fix 3).**
ΔA_chord156 = |A₁₅₆_fit − g₀_geo(156)| (g₀_geo(156) computed fresh in code,
central desk estimate 0.7012 — see design_geometry.py). **Central
expectation: ΔA_chord156 substantially smaller than the naive ΔA_vs_A78
(desk estimate ≈0.0121)** — if the geometry correction is doing real work,
comparing A₁₅₆ against its OWN geometry's chord null should explain most
of the naive discrepancy (desk check: |0.7017_desk − 0.7012_chord| ≈
0.0005, ~96% smaller than the naive 0.0121). **CONFIRMED (geometry-aware):**
ΔA_chord156 ≤ 0.010. **NOT EXPLAINED BY GEOMETRY:** ΔA_chord156 ≥ 0.020 (a
residual discrepancy even after the geometry correction would be the more
surprising, more informative outcome).

**P-R156-3 (primary, scored ladder currency, ε_r≡1 gas/aerosol-host-only —
mandatory fix 4; the load-bearing prediction of this whole cycle).** Desk
central estimate C(off_pass,156) ≈ −0.00576, **predicted disposition
MARGINAL, not PASS** — band [−0.0068,−0.0045]; only the top of this range
stays PASS. C(off_bracket,156) central ≈ −0.00331 (PASS), band
[−0.0043,−0.0025].

**P-R156-4 (rider b, δ_C transfer/determinism).** Fresh empty(156)
reproduces exp-030's own −0.0012113954918918646 to within 5×10⁻⁵.

**P-N17-1 (coverage/decision-floor gate, LOAD-BEARING per the Director's
own catch above — checked for BOTH N17 blocks).** |C_empty(N17)| ≤ 0.005
(this program's own suite-level absolute-identity bound, the tightest
established bar for this exact quantity). **A gate failure here is
pre-registered as informative, not discarded**: it would be this
program's second independent confirmation that the ±40° angle set carries
a real, angle-specific artifact (exp-024's own Iteration-2 finding,
margin-independent) — reported as such, not smoothed into "inconclusive."

**P-N17-2 (primary, angular convergence, BOTH blocks — gated on P-N17-1
passing).** |C(N17) − C(N9, same domain)| for off_pass. Central
expectation ≤ 3×10⁻⁴ (below the established N5-vs-N9 increment, 4.8×10⁻⁴);
band [0, 6×10⁻⁴]; ≥6×10⁻⁴ is the alarming outcome VISION's own review
warned about.

**P-N17-3 (N17_NATIVE only, the load-bearing deliverable of VISION's own
substance-attack).** C(N9, this cycle's own ±40°-margin domain) vs.
exp-033's own established C(off_pass,cpl=30,±35°-fallback)=−0.0045865.
**Central expectation: close agreement**, |Δ| ≤ 2×10⁻⁴ — if the ±40°
domain (once its own P-N17-1 gate is checked) reproduces the ±35° fallback's
own established PASS reading, that is real, direct evidence the still-cited
PASS is not an artifact of the fallback geometry's own angle restriction. A
miss here (|Δ| ≥ 5×10⁻⁴) reopens the established PASS itself, not just its
quadrature-convergence question.

**P-THERMO-1 (sidecar, extended).** Absorbed-fraction chord model
(reused verbatim from exp-033), newly applied to off_lab (0.626%) and
off_field (2.479%) — previously only informal Phase-5 estimates. Predicted
steady-state ΔT: off_lab≈1.00×10⁻³K, off_field≈3.98×10⁻³K (linear scaling
from exp-033's own established off_pass steady-state 8.17×10⁻⁴K). Against
exp-033's own implied NETD band [0.020,0.050]K: off_lab ≈20–49× below
NETD; off_field ≈5–13× below NETD (testing Iteration-10 Phase-5's own
flagged discrepancy — "narrower than this seat's own informally-cited
Iteration-10 finding," between 5× and 24–49×). **Post-run analytic only
(expressibility contract) — not an FDTD output.**

## Idealizations (lab convention, stated in full)

2D TMz, single polarization. **600nm only, all four blocks** (single-λ
scope, matching exp-030's/exp-033's own precedent). Static, linear,
time-invariant media throughout; σ(I) instrumented only at its OFF-state
static endpoint, nothing switchable is built. Ambient = FALLBACK/N17-family
discrete incoherent plane waves, post-hoc intensity summation (the
linear-media idiom — invalid for any gated article). Back-lit ambient
only, no front-lit/reflectance channel. **ε_r≡1.0 (index-matched,
gas/aerosol-host-only idealization) is load-bearing for constraints 2 and
3 alike — see T1 escape-route statement above for the numbers; every
PASS/MARGINAL below is a property of a gas/aerosol-host article only,
never a material transfer function.** The g_corr free-curvature fit is a
first-order weak-perturbation bench-calibration estimator (valid at
τ≤0.032, unchanged from exp-033). All runs are steady CW ambient
illumination, not a swept beam — constraint 4's dwell-limited caveat
(held at hypothesis-not-result since exp-033) is inherited, unresolved,
not triggered by anything here. Block R156 deliberately holds PLANE_DX
fixed (not self-similar, z/z_R=0.0123) — NOT comparable to Block CPL40's
z/z_R (self-similar, identical to r=78-native, 0.0493) despite both
blocks sharing R_OUT=156 cells by coincidence (flagged explicitly in
design_geometry.py, distinct sigma values computed independently per
block, asserted). The chord-model null (mandatory fix 3) is a **pure
ray-optics, zero-diffraction prediction** — it is expected to differ from
the true FDTD-measured g₀ by real diffractive-leakage physics (PHOTONICS'
own T15 finding), not to reproduce it exactly; its role here is only to
provide a geometry-aware comparator for ΔA, not a claim that g₀ IS the
chord value. No coherent-superposition interaction (Iteration 6,
untouched). Bench scale ≈10–20λ; nothing here is a Tier-W/Tier-A
constraint-3 verdict.

## Phase 4 — Results

*(filled in after the run — see below)*

## Learned

*(filled in after the run)*

## Phase 5 — Review

*(filled in after Phase 5)*

## Next

*(filled in at close)*
