# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 84 (exp-107 candidate)

*Blind to all other seats' Phase-2 critiques, per PANEL.md's isolation
discipline. Charter: sub-wavelength structure realizability; owns the
published/plausible/unobtainium-with-parameters bound.*

## Steel-man (150 words)

The census design is a genuine methodological upgrade over R3/R4
themselves: a single coherent 31-point grid (reproducing exp-069's own
original Block MINI span) replaces R3's and R4's own patchwork pooling
across five to ten differently-scoped sub-windows, and the mandatory
Gate G0 (sign-and-magnitude agreement against BOTH existing families
before any correlation counts) operationalizes R15's addendum's own
text as a pre-registered, non-post-hoc selection rule for the first
time on this signal. Red Team's own text forecloses a silent eighth
deferral, and a scoped-but-unexecuted plan does not discharge that
mandate. Given that constraint, this is the correctly-bounded way to
spend the FDTD budget: a hard ground-truth gate, a pre-committed
three-way outcome table whose "neither" branch is itself a formal
retirement (not another open item), and a cost-gated pilot-and-abort
safety net. If the census must run, this is close to the cleanest
version of it available.

## Sharpest attack (150 words, concrete and numeric)

My own seat's exp-100 disposition memo already establishes the
governing fact this proposal quotes but does not act on: under NO
branch of the R3/R4/R5 outcome does a realizability question ever
open — best case ("coupling detected") is "published, no new
material or structure required" (re-attribution of the already-
measured `graded_black_shell` rim's own diffraction); worst case is
"not a material property to bound" at all. The proposal spends ~66
real `sim.run()` calls, 3.3–4.0h wall (itself a ×1.95 cost-scaling
*extrapolation*, ratio³, "not a precisely-recomputed figure"), at
cpl=50 — a resolution family never before exercised in this
program — to determine which of two numerically-disagreeing families
(R3 r=0.486, R4 r=0.110) is "correct," on a signal whose own
established peak (3.15×10⁻³ at θ=39.2°) is already ≈63% of
`C_thr_lab` and, per the proposal's own R9-corrected figure, only
0.08–0.12× the same bar regardless of which family wins. The
"NEITHER/formal retirement" branch this census can land on is reached
today, for zero FDTD cost, by citing the disposition memo directly —
the census can only ever reach that conclusion at ~4h higher cost,
never a cheaper or more decisive one, from MATERIALS' own charter.

## The two substantive calls this proposal asks MATERIALS to make

**Tier 0 (execute vs. formally retire) — my verdict: formally retire,
do not execute the R5 census.** The disposition memo's ceiling is not
a soft lean; it is exhaustive over the outcome space (i/ii/iii, all
three already enumerated and none opens new realizability content).
R5 data cannot change that ceiling — it can only relabel which
existing-family reading future citations should prefer, or confirm
"neither," which the memo already states in effect. That is a
citation-hygiene and instrument-trust question for PHOTONICS/Red
Team's governance charter, not a realizability question, and it does
not require ~4h of cpl=50 FDTD to close. I recommend Iteration 84
retire the `delta_scene` R3-vs-R4-vs-R5 thread by citing exp-100's own
ceiling finding verbatim, matching Iteration-51's own no-seventh-cycle
precedent in substance (a standing item closed by written
disposition, not by one more data point that cannot move the
substantive answer).

**Tier 1 item 1 (hollow-vs-PEC-cored test at R_CORE/R_COAT=0.692/0.846)
— my verdict: this does NOT quietly extrapolate past a bound I have
set, and I support running it.** The quantity my seat has bounded
(REALIZABILITY_MEMO.md AMENDMENT 6/7) is the coating's **absolute**
thickness — 1.44µm delivered vs. 100–500µm required, a 70–350× gap,
UNOBTANIUM-WITH-PARAMETERS. `exp-052/design_geometry.py`'s
fixed-absolute-thickness family holds that exact 48-cell/1.44µm
thickness constant at every r (`ABS_THICKNESS=48`, asserted
`tau_shell==24.0` at every r in the family) — the already-locked
verdict is unchanged and unaffected by r. The rising R_CORE/R_COAT
ratio (0.692 at r=156, 0.846 at r=312, vs. T9's validated 0.385
anchor) is a pure consequence of the CORE growing while the coating
stays fixed-thickness, not a claim about a thinner or differently-
realizable coating — a real metamaterial coating can in principle be
applied to a core of any size. What this test actually probes is
whether `sections.radial_absorbed_power`'s "core is energetically
incidental" null (T9, Δσ_abs/σ_ext≈1.56×10⁻⁶–6.8×10⁻⁶, validated only
at ratio 0.385) still holds at these more extreme ratios — an
instrument-validity question, cheap (~75–90 min, 2 new article
calls), and the only instrument on the board that can discharge Red
Team's own founding Attack 9 concern (core-reflection leakage) behind
exp-106's own falling `abs_ext_ratio` signature. Legitimate,
correctly scoped, not a bound violation.

## Verdict: **support-with-changes**

Support the three bundled zero/low-marginal-cost Tier-1 closeouts
(items 1, 3, 4 of §5) without reservation — none touches a realizability
question outside what has already been bounded, and item 1 specifically
is the right next step for discharging Attack 9. Oppose executing the
R5 census as designed; the single change that would flip me to full
support is replacing the census's Tier-0 disposition with formal
retirement, citing exp-100's own ceiling finding, and redirecting the
freed ~3.3–4.0h budget to Tier-1 item 1 plus the deferred r=312
settling leg on `kappa_window` (exp-106's own still-open, genuinely
uncertain item) — both of which sit inside a live realizability/
instrument-trust question, unlike the census.

## Single parameter change that would flip my verdict on Tier 0

If the census's own G0 gate and three-way table were reframed so that
even the "R3-CORROBORATED" or "R4-CORROBORATED" branches were shown to
change something MATERIALS actually still has open — e.g. if a future
proposal identified a live realizability question that genuinely
depends on which family is correct (none exists on the record today) —
I would flip to support. Absent that, the census answers a question
whose entire outcome space I have already exhausted for my own
discipline at zero cost.
