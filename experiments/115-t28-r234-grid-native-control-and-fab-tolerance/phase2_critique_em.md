# Phase 2 Critique — ELECTROMAGNETISM — Panel Iteration 92 (candidate exp-115)

*Charter: field/wave behavior, impedance matching, energy coupling; owns the
reciprocity / passivity / causality bookkeeping and formalizes what T1 permits
and forbids. Fresh context, blind to the other five Phase-2 critiques and to
Red Team's Phase-2 audit. Read in full this session: `PANEL.md`; `LOGBOOK.md`
(RULED OUT R1–R34 line by line, ESTABLISHED, LIVE THREADS T1–T28, Iterations
85–91 and 46–52 at their own entries); `PLAN.md` 1–110; this cycle's
`phase1_proposal.md`; the exp-114 record (`run114.py`, `chunk_runner114.py`,
`analyze114.py`, `results.json`, `phase5_review_em.md` — my own seat's prior
review — `phase5_review_{materials,photonics,quantum}.md`,
`phase5_redteam_audit.md`); `experiments/113-.../{run113.py,
chunk_runner113.py}`; `experiments/112-.../{run112.py,results.json}`;
`experiments/110-.../run.py`; `experiments/108-.../{run.py,results.json}`;
`experiments/061-.../NOTES.md`; `lab/materials.py`; `lab/sections.py`;
`lab/validation/VALIDATION.md`; `lab/ARTIFACTS.md`. Every figure below was
recomputed by direct execution against committed JSON/source — nothing is
restated from the proposal's own prose (R4).*

---

## 1. Steel-man (≤150 words)

The §1 identity is real, and I re-derived it bit-exact. `geom_fixedabs_cpl`
sets `STEPS = round(3200·κ·1.25)` — 8000 and 12000, *exactly*, no rounding
slack — and both legs run three scenes, so exp-114's `measured_ratio` is
`(STEPS₂₃₄/STEPS₁₅₆)·G = 1.5·G`, with `HISTORICAL_R156_CPL25_TOTAL_S`
cancelling identically (`t156_adj ≡ 24000 × this_session_per_step_s`). That
is a genuinely new fact about a filed verdict: exp-114's CONFIRM carries
**zero** information from the historical session, and its true residual is
protocol mismatch, not cross-session normalization. Measuring `G` directly on
both grids in one session is the right instrument for that, and it is the one
queue item that answers Red Team's v2 straddle with data rather than a third
assumption. The scope discipline is exemplary: exactly one falsifiable FDTD
question, an upstream graceful-degradation gate, declined items numbered per
R25, and MATERIALS' seven-cycle debt finally written as a quotable claim.

## 2. Sharpest attack (≤150 words)

**§2.2's A,B,A,B order does not de-bias `G` — it guarantees a one-sided
bias.** For readings of duration `a` (r=156) and `b` (r=234) run A,B,A,B, the
mean r=234 midpoint trails the mean r=156 midpoint by exactly `(a+b)/2` =
6.25 r=156-units ≈ 22% of the session (A3). Under any monotone throughput
drift `f(t)`, **both** sustained pairs inherit the **same-signed** bias, so
averaging does not cancel it and `d_rep` — the cycle's only noise instrument
— reads ≈ 0. M4 is structurally blind to the systematic it exists to catch.
Scale: exp-114's own `R_DEG = 7.596%` arose across ~900 s; a comparable drift
over this lag biases `G` by several percent, against the **2.43%** headroom
from `G_E` to M5's CONFIRM edge (A4). A,B,B,A makes both mean midpoints
identically `T₀+a+b` for any `a,b` — the bias cancels in the mean and
`|G₁−G₂|` *measures* drift with a 2× lever arm.

## 3. Verdict

**support-with-changes.**

**The single protocol change that would flip me to plain support:** reorder
readings 3–6 from `U156, U234, U156b, U234b` to **`U156, U234, U234b,
U156b`** (A,B,B,A), and score M5 on the mean of the two pairwise
`G` values (`G₁ = U234/U156`, `G₂ = U234b/U156b`), with `d_rep = |G₁−G₂|/Ḡ`
feeding the composition rules. Zero cost, zero extra `Sim.run()` calls, and
it converts a first-order systematic that is currently invisible into one
that is both cancelled and measured (A3). It simultaneously discharges the
R33-addendum-(a) selection exposure in A5 (M5 would no longer pre-commit to
one of two equally-valid same-session readings) and makes M3's own question
answerable.

Everything else below I file as required corrections rather than
verdict-determining, on the stated ground that they are correctable at any
time up to Phase 5, whereas the run order is not correctable after Phase 4
starts. The sidecar findings (A7–A10) are the most consequential of those:
M9(d) is written to be quoted forward for years, and as drafted it rests on
a floor with provably zero differential content and an exponent that is wrong
by a factor of `exp(+τ_true) ≈ 3.9×10³`.

---

## 4. Appendix — derivations, re-derived figures, rule findings

### A1. The load-bearing identity — CONFIRMED bit-exact, with one caveat the proposal does not state

`experiments/112-.../run112.py:114` — `STEPS = round(R.STEPS0 * k * ratio)`,
with `STEPS0 = 3200` (`experiments/110-.../run.py:55`), `k = kappa_of(r) =
r/78` (`:93–94`), `ratio = cpl/CPL_600 = 1.25`. At r=156: `3200·2.0·1.25 =
8000` exactly; at r=234: `3200·3.0·1.25 = 12000` exactly. Both legs run three
scenes.

Therefore
`measured_ratio = (3·STEPS₂₃₄·p₂₃₄)/(3·STEPS₁₅₆·p₁₅₆) = (STEPS₂₃₄/STEPS₁₅₆)·G`.

Verified against `experiments/114-.../results.json:52,53,58,96`:

```
p234 = 7038.29048371315/36000            = 0.19550806899203194
p156 = r31_control.sustained.this_session_per_step_s
                                          = 0.07121022268191168
G_E  = p234/p156                          = 2.74550565394726
1.5 * G_E                                 = 4.11825848092089
filed measured_ratio                      = 4.11825848092089   (bit-exact, 15 digits)
t156_session_adjusted = 24000*p156        = 1709.0453443658805 = filed
```

**CONFIRMED.** The proposal's §1/§2.0 claim reproduces exactly.

**Caveat the proposal should state:** the identity is
`STEPS_ratio × G`, and `STEPS_ratio = kappa_ratio` only because
`round(3200·κ·1.25)` happens to be exact at both κ. Written as
`measured_ratio ≡ kappa_ratio × G` it is a numerical coincidence of these two
geometries presented as a construction identity; at an r where `round()` bites
(e.g. any κ with a non-terminating `3200·κ·1.25`) it fails. One line in
`analyze115.py` asserting `STEPS₂₃₄ == 1.5 * STEPS₁₅₆` discharges this (R19
discipline: assert the invariant, do not narrate it).

### A2. What the identity does — and does *not* — license about the v2 straddle

The proposal's §1 says this cycle "can confirm or refute a filed CONFIRM," and
§2 of Red Team's exp-114 audit (`phase5_redteam_audit.md:240–336`) says the
grid-native burst is "the one check that would resolve §2's own straddle
finding with real data."

Both are true *only on the machine the straddle lives on*. The straddle is
between two normalizations of **exp-114's own cloud-session r=156
denominator**. A bench-measured `G` bears on it only under the assumption that
`G` is machine-transferable — which is exactly M6, which this same proposal
labels an `N = 2` test (`§7` Idealization 3, `phase1_proposal.md:620–624`).
The reasoning is therefore circular as framed: the untested assumption is used
to license the claim that the straddle is resolved.

The proposal is honest about the ingredient (Idealization 3) but not about the
consequence. **Required correction:** state in §1 and in `result_text` that
this cycle answers the straddle *for the bench*, and that closing it in
exp-114's own record still requires a grid-native control **in a cloud
session**. Additionally, Red Team's queue item 1 carries a second clause —
"re-score `kappa_exponent_result` against the corrected denominator"
(`experiments/114-.../phase5_redteam_audit.md:616–620`) — which this cycle
structurally cannot execute, and which does **not** appear among §3's numbered
declined items (`phase1_proposal.md:190–221`). That is precisely the R25 shape
(a queue clause dropped without a numbered decline). It does not fire (R25's
own text places the fault with queue authorship, not the inheriting cycle),
but it must be added to §3 so it is not marked discharged at the Iteration-92
close.

### A3. The A,B,A,B ordering bias — closed form

Let readings have durations `a` (r=156, 3334 steps) and `b` (r=234, 3334
steps), `b ≈ G·a ≈ 2.75a`. Take the reading's effective sampling time as its
midpoint (exact for a linear drift).

**A,B,A,B** starting at `T₀`:
midpoints `T₀+a/2`, `T₀+a+b/2`, `T₀+a+b+a/2`, `T₀+2a+b+b/2`.
mean(A) `= T₀ + a + b/2`; mean(B) `= T₀ + 1.5a + b`.
**lag = mean(B) − mean(A) = (a+b)/2**, for any `a,b`.

**A,B,B,A**: mean(A) `= T₀ + a + b`; mean(B) `= T₀ + a + b`. **lag = 0**, for
any `a,b`.

With `a = 3334` steps × 3 scenes at r=156 and `b = G·a`, in units `u` = one
1000-step 3-scene r=156 reading (`= S156`), the proposal's full sequence spans
`1 + 2.75 + 3.334 + 9.17 + 3.334 + 9.17 = 28.76 u`, and the sustained lag is
`6.252 u` — **21.7% of the whole session**.

For a slow multiplicative drift `f(t) = 1+εt`, under A,B,A,B:
`G₁ ≈ G_true(1 + 6.252uε)` and `G₂ ≈ G_true(1 + 6.252uε)` — identical bias,
`d_rep ≈ 0`. Under A,B,B,A: `G₁ ≈ G_true(1 + 6.252uε)`,
`G₂ ≈ G_true(1 − 6.252uε)` — mean is unbiased to first order and
`d_rep ≈ 12.5uε`, i.e. the drift becomes the measured quantity.

**The proposal's own justification for A,B,A,B is factually wrong** as
written: "Alternating pairs each sustained reading with an adjacent
**same-duration** reading on the other grid" (`phase1_proposal.md:163–164`).
The readings are matched in **step count**, not duration; the r=234 reading
takes ≈ 2.75× the wall time of its partner. That mismatch *is* the lag.

This is the R30/R32-family failure shape one level up: an instrument whose
only null channel (`d_rep`) cannot produce the reading that would falsify the
measurement it guards.

### A4. M4's REPEATABLE bar is looser than M5's own decision headroom — recomputed

All band edges reproduce exactly from `run114.py:143`
(`KAPPA_COST_EXPONENT = 3.2053299988171697`):

```
G_ref = 1.5**(k-1)                = 2.4453404739580256   (proposal: 2.4453404739580256) OK
CONFIRM window in G               = [2.0785394028643216, 2.812141545051729]  OK
REFUTE  bounds  in G              = <=1.7117383317706178 or >=3.1789426161454335  OK
eps(2.0) = 2**(k-3)               = 1.152950039837078    (== R28 founding miss 0.15295) OK
const-eps model G                 = 2.25*1.152950039837078 = 2.5941375896334256  OK
models differ                     = 2.5941375896334256/2.4453404739580256 - 1 = 0.060849  OK
eps_E(1.5) = G_E/2.25             = 1.2202247350876712   OK  (5.835% / 12.275% from the two models) OK
R_DEG = sustained/short - 1       = 0.07596424755863729  OK  (from results.json:96,88)
```

Every M5/M6/M7 figure in `phase1_proposal.md:272–409` is confirmed. **No
arithmetic defect found in the bands.**

But: `headroom(G_E → CONFIRM upper edge) = 2.812141545/2.745505654 − 1 =
**2.427%**` — identical to the figure I filed at exp-114 Phase 5
(`phase5_review_em.md:210–219`) and re-derived independently by Red Team
(`phase5_redteam_audit.md:118–124`). M4's **REPEATABLE** bar is `d_rep ≤ 0.02`
(`phase1_proposal.md:309`), i.e. **82% of that entire headroom**. A full
"REPEATABLE" pass therefore certifies nothing about M5's band assignment if
the bench lands anywhere near the disclosed prior.

The proposal already knows how to fix this: M7 carries a pre-registered power
condition (`d_rep > 0.03 ⇒ UNDERPOWERED, not scored`,
`phase1_proposal.md:400–404`) precisely because its two models differ by
6.085%. **M5 — declared PRIMARY, the falsifiable heart — carries no power
condition at all.** That asymmetry is internally inconsistent, and it is R24's
own shape one step earlier (a consequence stated for one classifier and not
its sibling; cf. `classify_item_i` vs `classify_item_ii`, LOGBOOK Iteration
85 CHECKPOINT, lines 8944–8962).

**Required:** M5 gets a coded composition rule of the same form. The A,B,B,A
reorder makes the natural one available: score both pairs through the
unmodified classifier and report `UNINTERPRETABLE` if they land in different
bands.

### A5. M5's single-reading selection rule is a live R33-addendum-(a) exposure

`phase1_proposal.md:731–733` claims R33 is "made inapplicable by construction
for M5 — no scored operand mixes sessions." The cross-session half is indeed
removed. But R33's ratified text carries addendum (a) verbatim
(`LOGBOOK.md:1462–1472`): *when more than one same-session control reading
exists and the selection rule was justified for a different purpose, that
reuse requires its own independent justification, and any alternative
reading(s) must be disclosed as a stated, not-scored sensitivity.*

This cycle **creates** two equally-valid same-session sustained readings
(`U156/U234` and `U156b/U234b`) and pre-commits to scoring the first
(`measured_ratio_B = 1.5 × G_sustained`, `:324`), with no stated justification
and no requirement to persist the repeat pair's own M5 score as a
`..._DO_NOT_SCORE` sensitivity. That is the identical structure QUANTUM's
exp-114 finding was about — and exp-114's precedent is that the alternative
reading **flipped the tier** (`phase5_redteam_audit.md:134–172`).

Separately: `run113.py:166–180` `combine_control_readings` selects the
**lower** `speed_ratio`, not "sustained." The proposal reuses it unmodified
for the bench-native R31 artifact (`:173–176`) while M8 argues at length that
"sustained" is correct on protocol-commensurability grounds (`:427–436`). If
the bench's short reading comes back lower, the same `results.json` will carry
`used_label = "short"` alongside an M8 paragraph defending "sustained." State
the override explicitly, or the record contradicts itself.

**Required:** persist `sensitivity_repeat_pair_M5_DO_NOT_SCORE` (and
`sensitivity_short_pair_M5_DO_NOT_SCORE`, free once M1 exists), and state the
selection rule as a deliberate override of `combine_control_readings`.

### A6. M6's caveat fires on only one of four possible M3 states

`phase1_proposal.md:366–371`: "If M3 reads `DOES-NOT-CANCEL`, M6 is persisted
with `g_e_protocol_caveat = True` and reported as directional only."

M3 has four reachable states: CANCELS, PARTIAL, DOES-NOT-CANCEL, and
UNINTERPRETABLE (M4's own composition rule, `:314–316`), plus the
`repeat_skipped` path (`:317–320`). **PARTIAL, UNINTERPRETABLE and
repeat-skipped all escape the caveat** — and UNINTERPRETABLE is precisely the
state in which least is known. This is verbatim the composition gap Red Team
had to close in code at exp-113 Phase 5 (`direction_validated` conflating
distinct states into one `False`, LOGBOOK.md:1429–1435, R32's own founding
record).

Worse, PARTIAL is the *most likely* M3 outcome by construction: M3's
DOES-NOT-CANCEL bar is set at the **full** single-grid `R_DEG`, which requires
the other grid to degrade by exactly zero. The physically plausible case (the
2.25×-larger grid degrades somewhat more, being more bandwidth-bound) lands in
the uninformative middle *and* releases M6's caveat.

**Required:** invert the rule — `g_e_protocol_caveat = True` unless M3 reads
`CANCELS`.

### A7. The sidecar's floor gate has provably ZERO differential content — derivation

This is my seat's core finding on M9. `lab/sections.py:130–133,148–151`:

```python
p_scat      =  _face_flux(ps, box)          # ps = scene - empty
p_abs       = -_face_flux(pt, box)          # pt = pi + ps
p_ext_cross = -_cross_flux(pi, ps, box)
"sigma_ext":       (p_scat + p_abs)/i_inc
"sigma_ext_cross":  p_ext_cross/i_inc
```

`_face_flux` is bilinear in (E,H), so `F(pi+ps) = F(pi) + F_cross(pi,ps) +
F(ps)`. Hence

```
p_ext = p_scat + p_abs = F(ps) - [F(pi) + F_cross(pi,ps) + F(ps)]
      = -F(pi) - F_cross(pi,ps)
p_ext_cross = -F_cross(pi,ps)
=> p_ext_cross - p_ext = F(pi)
```

**`σ_ext_cross − σ_ext` is identically the EMPTY run's own net incident flux
imbalance through the box, divided by `i_inc`.** It depends only on
`cap_empty` and the box — it contains **no scene information at all**, and it
cancels exactly in any config difference.

Confirmed against real data (`experiments/114-.../results.json:33–45`,
`experiments/112-.../results.json`):

```
r=234:  resid(peccored) = 3.03914978344437258784e-02
        resid(hollow)   = 3.03914978344437258784e-02      difference = 0.000e+00  (BIT-IDENTICAL)
r=156:  difference of residuals = -2.27e-13               ( = 1.5e-11 of d_sigma_ext, pure roundoff)
```

So M9(b)'s entire "0.2×–12.6× the channel's own optical-theorem
self-consistency floor … the correct statement is therefore an upper bound,
not a resolved measurement" (`phase1_proposal.md:463–469`) is built on a
quantity that is **exactly common-mode to the two configurations being
differenced**. It is not a floor on this measurement in either direction; it
is an R9 incommensurability of the purest kind (a within-scene model-vs-model
residual used to gate a between-scene difference).

**Required:** replace the floor gate with a genuinely differential one. Two
are already on file at zero cost: exp-108's item-ii absolute box-ledger noise
floor (`residual_std` over the six-margin family, r=156/312, LOGBOOK Iteration
85 lines 8796–8799) and the six-margin spread itself. Report both, and state
the optical-theorem residual for what it is — a solver self-consistency
statistic on the empty capture, not a differential floor.

### A8. The `exp(−2τ_true)` estimate uses the wrong exponent for a coherently-measured cross-section

`phase1_proposal.md:471–476`: "the core-dependent contribution to the far
field is `O(exp(−2·τ_true)) = 6.71e-08` in intensity … three orders of
magnitude below anything this instrument can resolve, fully consistent with
(b)'s reading that the measurement is floor-limited."

`τ_true = 2·(2π/cpl)·thickness_cells·I_graded`
(`experiments/061-.../NOTES.md:42–49`) — the leading `2` is the
intensity-absorption convention `α = 2k₀·Im(n)`, and `α_true = 5.7353×10⁴
cm⁻¹` with a **174.36 nm e-fold** confirms it: `τ_true` is a **one-way
INTENSITY** optical depth. So `exp(−2τ_true)` is the fraction of incident
**power** that makes a round trip and re-emerges. That is the right quantity
only if the core's contribution added **incoherently in power**.

It does not. `σ_scat = ∮|E_shell + δE|²` with the shell a strong scatterer
(`σ_ext ≈ 1093` cells against a `2·R_COAT = 584`-cell width — the near-Babinet
≈1.87× extinction paradox, ESTABLISHED/T9). The observable is the **cross
term**:

```
Δσ_scat/σ_scat ~ 2·Re<E_shell*, δE>/|E_shell|² ~ 2·|δE|/|E_shell|
```

and `|δE|/|E_inc|` is the **round-trip AMPLITUDE** factor
`exp(−τ/2)·exp(−τ/2) = exp(−τ_true)`, not `exp(−2τ_true)`. One factor of `τ`,
not two. The proposal's estimate is therefore low by `exp(+τ_true) ≈
3.86×10³`.

Numerically (`τ_true = 8.258819829686677`):

| quantity | value | vs measured Δ (8.36e-5 … 1.53e-4) |
|---|---|---|
| `exp(−2τ_true)` (proposal) | `6.706e-08` | measured is **1.25×10³ – 2.28×10³ ×** larger |
| `2·exp(−τ_true)` (coherent cross term) | `5.179e-04` | measured is **0.16 – 0.30 ×** of it |

**The corrected zero-parameter estimate lands within a factor 3–6 of every
measured delta; the proposal's lands 3+ decades away.** Robustness: the
proposal's own Idealization 9 (`:658–662`) notes `τ` at the cpl=25/σ_max=0.4
member is smaller (Im(n) concave in σ), bounded below by the linear-in-σ value
`≈6.6`. Even at `τ=6.6`, `exp(−2τ) = 1.9×10⁻⁶` is still 55–80× below the
measurements while `2exp(−τ) = 2.7×10⁻³` brackets them from above. The
conclusion is exponent-choice-driven, not `τ`-value-driven.

Two consequences the record must carry:

1. **(b) and (c) as drafted are mutually inconsistent, and the proposal calls
   them "fully consistent."** If the physics were `6.7×10⁻⁸` and the floor
   `6.6×10⁻⁶`, then a measured `8.4×10⁻⁵` (12.6× the stated floor, by the
   proposal's own gate) would be an unexplained 12.6× excess — not a
   floor-limited null. Under the corrected exponent the numbers instead form a
   coherent story: a **real, resolved, physically-predicted** core-scattering
   cross term, ~3–6× below a crude estimate that ignores angular overlap and
   the core's own aperture fraction.
2. **M9(e)'s forward conditional inherits the error.** "the bound scales as
   `exp(−2·τ_true)` and τ_true grows with thickness, so a realizable coating is
   exponentially *more* backing-independent" (`:526–529`) has twice the true
   exponent. The correct scaling is `exp(−τ_true)` — still exponential, still
   supports the conditional's direction, but the claimed benefit per unit
   thickness is halved in the exponent. Correct it before it is quoted.

Weakly suggestive, offered as an observation and explicitly **not** a claim
(two points; R15's own two-point caution): the ratio (measured / corrected
estimate) tracks the core's aperture fraction in the right direction —
`R_CORE/R_COAT = 0.692 → 0.161` at r=156, `0.795 → 0.210` at r=234.

### A9. "Three independent energy-ledger channels" is false — two channels and their exact sum

`phase1_proposal.md:497`. From `lab/sections.py:150`, `sigma_ext ≡ (p_scat +
p_abs)/i_inc` is an algebraic definition, so the three deltas satisfy
`Δσ_ext ≡ Δσ_scat + Δσ_abs` identically. Verified on the real ledgers:

```
r=234 signed:  Δσ_scat=+0.059980150352544  Δσ_abs=-0.003070417659615  Δσ_ext=+0.056909732692930
               Δσ_scat + Δσ_abs - Δσ_ext = 0.0                (exact)
r=156 signed:  +0.029306826271295  -0.014275951913930  +0.015030874357421
               residual = -5.68e-14                            (roundoff)
```

This is not a new discovery: **my own seat found it one cycle earlier**, and
LOGBOOK records it verbatim — "ELECTROMAGNETISM found the persisted
`sigma_ext≈sigma_abs+sigma_scat` cross-check is a code-level TAUTOLOGY
(`lab/sections.py` *defines* it that way)" (`LOGBOOK.md:24456–24458`).
`lab/sections.py:216–219` states the same principle for the angular channel in
its own docstring. Citing `σ_ext` as a third corroborating channel is
double-counting — and it is the *flattering* kind, because at r=156 the two
genuine channels partially cancel (`+0.0293` against `−0.0143`), making the
derived `σ_ext` delta about half the size of the largest real one.

**Required:** either write "two independent channels and their exact sum," or —
better, and free — promote `σ_ext_cross` to the third channel. It is a
genuinely independent computational route (the near-field optical theorem),
and its config difference is already on file:
`Δσ_ext_cross/σ_ext_cross = 5.204371×10⁻⁵` at r=234, agreeing with
`Δσ_ext = 5.204381×10⁻⁵` to 2 ppm. *That* agreement is a real cross-check and
is worth stating; the tautological one is not.

### A10. "far-field optical signature" mischaracterizes the instrument

M9(d) claims a bound on the article's "**far-field** optical signature"
(`phase1_proposal.md:492–493`). Every channel in the table is a
near-to-mid-field box quantity: `lab/sections.py:212–215` says so explicitly
("a square-path angular sample, not a true circular far-field pattern —
consistent with `sigma_scat`'s own near-to-mid-field box convention"), and
this bench's near-zone status is an ESTABLISHED finding of its own —
`σ_abs/σ_ext = 0.51` and `0.606–0.608` both **exceed** the geometric-optics
far-field Babinet ceiling of 0.5, precisely because "this bench's box sits
deep in the shadow's near zone" (`LOGBOOK.md:1556–1564`, T9 at `:1822–1832`).
This is my seat's own founding caveat on that anchor and it applies unchanged
here.

**Required (one word each):** "near-to-mid-field box-ledger signature," and in
the `Fabrication consequence` sentence, "at this bench's measurement geometry."
A near-field bound does not license an unqualified far-field fabrication
claim, and this blockquote is written expressly to be quoted forward.

### A11. Two cited "established" figures that the record does not support

**(i) "`peccored` steps are ~14% costlier"** (`phase1_proposal.md:147–148`,
offered as what "exp-113's own Fix 3b established"). Its origin is
`run113.py:151–152`, itself sourced to an exp-113 EM critique that Red Team
records as "an *estimate*, explicitly 'not a profiled measurement'"
(`experiments/114-.../phase5_redteam_audit.md:322–325`). The only real
per-scene data in the program contradicts the magnitude
(`experiments/114-.../results.json:47–51`):

```
empty 0.196328 s/step   hollow 0.193850   peccored 0.196346
peccored/empty = 1.00009   hollow/empty = 0.98738   (full spread 1.28%, not 14%)
```

The 3-scene mix decision is still right on protocol-matching grounds — my
attack is on the citation, not the design. But the real 1.28% spread is itself
a *useful* number for this cycle: scene-mix commensurability contributes ≲1.3%
to `G`, comfortably inside M4's bands, which materially strengthens §2.2's
argument rather than weakening it. Cite the measurement, not the estimate.

**(ii) `R_DEG` may be session drift, not duration dependence.** `R_DEG =
7.596%` is the ratio of exp-114's sustained to short readings — which were run
**sequentially**, short first (`chunk_runner114.py:190–191`). exp-114 never
separated duration from elapsed-time drift, and this proposal adopts `R_DEG`
as the anchor for **both** M3 and M4 (`:289–296`, `:308–311`) without noting
the confound. The only long-run counter-evidence in the record points the
other way: within the r=234 `empty` production scene, the first 3000 steps ran
at `0.20510 s/step` (Red Team's three quoted chunk times) while the remaining
9000 averaged `(2355.937−615.29)/9000 = 0.19341` — **5.7% FASTER with
duration**, opposite in sign to `R_DEG`.

That sign conflict also undercuts M8's `sustained_choice_justification`
(`:427–436`), which argues sustained is right because "duration measurably
matters." It may matter; it does not currently have a consistent sign. The
proposal's own M3 is the right test — but only after the A,B,B,A fix, which
is what lets `d_rep` separate drift from duration at all.

### A12. Smaller items

1. **M5 cannot discriminate the only alternative on the table.** Pure `N²`
   scaling is, per the proposal's own §2.0 row (`:100`), algebraically
   `k = 3.0` exactly — the hardcoded exponent R28 replaced. At `κ_ratio=1.5`,
   `G = 2.25` gives `rel_dev = |2.25/2.4453405 − 1| = 0.0799`, **inside M5's
   ±0.15 CONFIRM band**. The entire hypothesis space between the old and new
   exponents is 7.99% wide; M5's CONFIRM band is 15% wide. A CONFIRM therefore
   does not distinguish "`k=3.2053` generalizes" from "`k=3.0` was fine all
   along." The proposal found the fact (`:100`, "Not previously stated
   anywhere in the record" — correct, and a good catch) and did not follow it
   into the power implication. State it in Result prose so the CONFIRM is not
   over-read.
2. **M5's stated call signature does not match the function.**
   `classify_kappa_exponent_check(exponent_234, kappa_ratio=…)`
   (`run114.py:258`) takes an **exponent**; M5 says it passes
   `measured_ratio_B = 1.5 × G_sustained` (`:324`). The conversion
   (`math.log(1.5*G)/math.log(1.5)`) is trivial but unstated — R18 asks that a
   check's documented use match its code before it is relied on.
3. **The `18 Sim.run() calls` assert conflicts with §6's own skip branch.**
   `:168` and `:717` commit to asserting 18 calls; `:588–591` permits skipping
   readings 5–6, which yields 12. Make the assert conditional on
   `repeat_skipped` (R19 requires the invariant be coded, and a coded
   invariant that can fire spuriously on the graceful path is worse than none).
4. **Zero-cost instrument upgrade, strongly recommended.** Persist per-scene
   *and* per-1000-step-block sub-timings inside each reading, not only the
   3-scene blend. This costs nothing, and it (a) gives M3/M4 the data to
   separate warm-up, drift and grid effects directly rather than by inference,
   (b) permanently closes Idealization 6's per-scene-split loss
   (`:640–645`) for the bench, and (c) would let a future cycle test whether
   the within-scene warm-up in A11(ii) is real. Given that this cycle's entire
   product is a timing measurement, discarding the sub-structure of that
   measurement is the one avoidable information loss in the design.
5. **"two grid resolutions (cpl 20 and 25)"** (`:496`) is not a resolution
   check on any single channel: the per-bin channel exists only at cpl=20
   (r=156/312) and the aggregate channels only at cpl=25 (r=156/234) — channel
   and resolution are fully confounded, as §7 Idealization 7 (`:646–650`)
   itself discloses for the radius axis. The individual deltas are cpl-safe
   (each is a within-cpl ratio, so exp-112's `CPL_RATIO` raw-magnitude artifact
   cancels), but the *bound* has not been shown resolution-robust — an R3/R15
   over-read in the quotable blockquote. Recommend: "two grid resolutions
   across (not within) channels."
6. **`R_COAT` is not exactly congruent between the timed grids.**
   `round(234×1.25) = 292` (banker's rounding of 292.5), so `R_COAT/r =
   1.2479` at r=234 vs `1.2500` at r=156 — a 0.17% article-size difference.
   Irrelevant to timing (cost is set by `N=2100`, exact) and irrelevant to the
   thickness claim (`R_COAT−R_CORE = 60` cells exactly at both, so the 1.440 µm
   invariance in `:108` is correct as stated). Noted only so it is not
   discovered at Phase 5 as an undisclosed asymmetry.

### A13. Rule-compliance summary

| Rule | Finding |
|---|---|
| **R4** | Every band edge, `G_ref`, `G_E`, `ε(2.0)`, `R_DEG`, the `1.5×G` identity, and all six sidecar deltas reproduce **bit-exact** from committed sources. Two citations do not: A11(i) ("~14% costlier") and A8 (`exp(−2τ)`). The sidecar table's denominator convention (arithmetic **mean** of the two configs) is unstated — reproducing it requires guessing; state it. |
| **R9** | **Live violation, A7**: a within-scene solver residual used as the floor for a between-scene difference, when the residual is provably scene-independent. Also A2 (a bench `G` used to close a cloud-session straddle). |
| **R13** | The floor gate M9(b) invokes is not a floor (A7). R13 is *not* satisfied by the current construction; it would be by exp-108's item-ii differential floor. |
| **R17** | M3/M4/M6/M7 anchors are correctly derived from on-file magnitudes (`R_DEG`, R28's 0.15295) and re-derived here bit-exact. **Compliant.** One caveat: `R_DEG`'s own duration/drift confound (A11(ii)) is inherited undisclosed. |
| **R18** | A12(2) — M5's documented invocation does not match the function's signature. |
| **R19** | A12(3) — the committed call-count assert conflicts with §6's skip branch. |
| **R21** | M9(d) is written to be quoted in Result — good. But its own constraint-3 disclaimer lives in §4 and M9(e), **outside** the quotable blockquote. Move it inside; a byproduct's headline must carry its own caveat where a future citation will read it. |
| **R24** | A4/A6 — a stated consequence not wired to the classifier it should gate (M5 has no power condition; M6's caveat covers 1 of 4 M3 states). Not a firing (nothing is claimed "adopted in full" yet) but it is R24's shape at Phase 2, which is where it is cheapest to close. |
| **R25** | A2 — Red Team's queue item 1's second clause ("re-score `kappa_exponent_result`") is neither executed nor listed among §3's numbered declines. Fault lies with queue authorship per R25's own text; add the numbered decline. |
| **R30/R32** | The proposal declares both N/A (`:727–730`). I **partly disagree**: `d_rep` is a null/noise instrument gating three verdicts, and A3 shows it is structurally incapable of registering the dominant systematic. That is R30's substance (an uncalibrated instrument cited evidentially) even if not its letter. The A,B,B,A fix makes the declaration true. |
| **R33** | Addendum (a) exposure, A5 — two same-session sustained readings, one pre-committed for scoring, no alternative persisted. |
| **R34** | No criterion-4 firing is open on this channel. Nothing here fires one. |

### A14. Constraint 3 and the metrics table

**No quiet constraint-3 violation found**, and I checked this structurally
rather than by reading the proposal's own assurance. Item 1 computes wall
times only — no `full_capture`, no `widths`, no `window_stats`, no ambient
instrument (`:166–168`), so no constraint-1/2/3/4 metric is produced or moved.
Item 5's article (`graded_black_shell`, `tau_shell=24`, `eps_r≡1`) is passive,
linear and time-invariant, and LOGBOOK's ESTABLISHED section already records
it as failing constraint 3 by construction; a core/backing-insensitivity bound
on such an article cannot be constraint-3 progress and the proposal says so
(`:250–261`, `:530–533`). **T1 escape route NONE / N/A is correct.**

Two disclosures the cycle owes the metrics table, neither currently written:

- The **energy-budget / THERMO-sidecar row is genuinely N/A this cycle** — the
  1000/3334-step control bursts are far short of the 8000/12000-step settled
  production counts, so no ledger, no absorbed-power figure, and no thermal
  sidecar is computable from anything this cycle runs. Say so explicitly
  rather than leaving the row silent; a silent row and an N/A row read
  identically, which is the exact failure mode `lab/ARTIFACTS.md:18–21`
  names for the Evidence Gate ("a silent gate and an absent gate produce
  identical observations").
- The one sentence that could be misread as constraint-relevant is M9(d)'s
  "the material behind it is a free parameter over the entire span from vacuum
  to a perfect conductor." Inside the blockquote, unqualified, that reads as a
  design-freedom claim about the bench's workhorse absorber. With A10's
  near-field qualifier and the constraint-3 disclaimer moved inside the quote,
  it is safe. Without them, it is the sentence a future cycle quotes wrong.

---

**ELECTROMAGNETISM — verdict: support-with-changes.** The falsifiable heart is
well-chosen and the identity underneath it is real and load-bearing. The
design as drafted has one irreversible defect (the run order) and one
quotable-forever defect (the sidecar's floor and exponent). Fix the order
before Phase 4; fix the sidecar before freeze.
