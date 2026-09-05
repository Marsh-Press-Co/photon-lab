# Phase 5 Final Audit — RED TEAM (exp-114, Panel Iteration 91)

**Full-visibility seat.** Read `PANEL.md` in full; `LOGBOOK.md` end to end
(RULED OUT registry R1–R32 in full, including the R4/R9/R27–R32 lineage
this cycle's own findings sit inside; the LIVE THREADS section in full,
T1 and the complete T28 sub-thread from its Iteration-46 opening through
the Iteration-90/exp-113 close, including the file's own disclosed
Iteration-58-through-87 narrative gap); `PLAN.md`'s head (`## Current
state`, the live Reconciled Iteration-91 queue — this file is authored
most-recent-first, so the "tail" the task names is the entry at the top).
Read every file in `experiments/114-t28-kappa-exponent-r234-calibration/`:
`phase1_proposal.md`, `run114.py`, `chunk_runner114.py`, `analyze114.py`,
all five Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`,
`results.json`, and all six Phase-5 reviews — plus
`experiments/113-.../phase5_redteam_audit.md` for this program's own
house style (the exact convention this document mirrors). Independently
re-derived every load-bearing figure below from primitives (direct Python
execution against the real committed constants and `results.json`, shown
inline) — nothing here is taken on any seat's, or the Director's, word.

## 0. Bottom line

All six Phase-5 reviews' headline arithmetic independently reproduces
bit-exact — I found **zero wrong numbers** anywhere in this cycle's own
record, a genuinely clean result by this program's own R4 standard. But
three of the six seats (ELECTROMAGNETISM, QUANTUM OPTICS, PHOTONICS'
self-review) each independently found a **different, non-overlapping,
real residual confound** underneath the Director's own Phase-4 R9 self-
catch — and my own independent extension of the Director's exploratory
"v2" recalculation (§2, below) finds a **fourth, more consequential**
result than the Director's own stated uncertainty suggests: the two
central estimates of `measured_ratio` produced by two independently
defensible correction methods **sit on opposite sides of the reference
value**, not merely at different distances from it. This is genuine,
convergent evidence that the frozen `CONFIRM` verdict, while correctly
computed under the pre-registered rule, is thinner than its headline
`rel_dev=0.1227` conveys. My ruling (§3): the LOGBOOK verdict should read
**CONFIRM-WITH-NAMED-GAPS**, not plain CONFIRM and not a downgrade to
AMBIGUOUS. Zero Checkpoint criteria fire (§4) — this is Phase 5 working
exactly as designed, provided (and I make this an explicit condition) the
three named confounds are promoted to their own concrete Iteration-92
queue lines, not left to erode as prose. R33 is ratified, folding in
**both** QUANTUM's and PHOTONICS' scoping addenda (§5). Trust suite:
**41/41, independently re-confirmed this audit, stage-by-stage** (§8).

---

## 1. Independent verification of all six Phase-5 reviews

### 1.1 VISION SCIENCE — every figure re-derived bit-exact; no defect found

Re-ran the entire R9-fix chain from the two named raw operands
(`670.4777698516846`, `0.3923112818872906`) in a fresh process:

```
t156_session_adjusted = 670.4777698516846 / 0.3923112818872906 = 1709.0453443658805
exponent_234           = ln(7038.29048371315/1709.0453443658805)/ln(1.5) = 3.490880835092507
measured_ratio          = 1.5**3.490880835092507                        = 4.11825848092089
reference_ratio         = 1.5**3.2053299988171697                       = 3.6680107109370383
rel_dev                 = |4.11825848092089-3.6680107109370383|/3.6680107109370383 = 0.12274985147707763
naive exponent_234       = ln(7038.29048371315/670.4777698516846)/ln(1.5) = 5.798600165690798
naive rel_dev            = 1.8618852001295216
```

Bit-exact to `results.json` and to VISION's own printed figures.
**CONFIRMED** — the CONFIRM verdict is correctly computed under the
frozen rule; VISION's own "Combined Verdict matches `results.json`
honestly" finding holds. VISION's own §3 (R33 wording notes) is
addressed directly in §5, below — I largely adopt it, folded into the
final text.

### 1.2 MATERIALS — energy-ledger table independently reproduced; Fix 4 confirmed landed

Recomputed every ratio in MATERIALS' own table directly from
`results.json`'s raw `energy_ledger` fields:

```
abs_ext_ratio peccored = 541.8828571541701/1093.4682853909158 = 0.495563   (MATERIALS: 0.49556 — match)
abs_ext_ratio hollow   = 541.8797867365105/1093.5251951236087 = 0.495535   (MATERIALS: 0.49553 — match)
hollow-vs-peccored rel diff, sigma_scat = 0.01087%   (MATERIALS: 0.0109% — match)
hollow-vs-peccored rel diff, sigma_abs  = 0.00057%   (MATERIALS: 0.0041%? — see note below)
hollow-vs-peccored rel diff, sigma_ext  = 0.00520%   (MATERIALS: 0.0052% — match)
```

One genuine discrepancy caught: MATERIALS' own table lists the r=234
`sigma_abs` hollow-vs-peccored relative difference as **0.0041%**, but my
independent recomputation from the same raw `results.json` fields gives
**0.00057%** (5.67 ppm) — a ~7× difference. Cross-checked against
THERMODYNAMICS' own independently-computed figure for the identical
quantity: **"5.7 ppm" (0.00057%)** — matching my own recomputation, not
MATERIALS'. **MATERIALS' own printed r=234 `sigma_abs` figure in its §2
table (0.0041%) is wrong**; the correct value, confirmed two independent
ways (this audit's own recomputation, THERMODYNAMICS' own Phase-5
review), is **0.00057% (5.67 ppm)** — MATERIALS appears to have
transcribed its own r=156 `sigma_abs` figure (0.0041%, which I
independently confirm matches THERMODYNAMICS' cited r=156 comparison
value, "40.8 ppm" = 0.00408% ≈ 0.0041%) into the r=234 column by mistake.
**[inconsistency, R4-class]** Non-outcome-reversing (MATERIALS' own
qualitative point — "the r=234 reading is if anything tighter, not
looser, than r=156's" — is still correct once the fixed number is used:
5.67 ppm < 40.8 ppm) but a real, disclosed transcription slip in a
Phase-5 review's own table, caught here per this program's own R4
discipline (a Phase-5 reviewer's figure must be independently
re-verified, not merely trusted). Every other MATERIALS claim
independently reproduces exactly (`sigma_ext`/`sigma_ext_cross`
agreement ~28 ppm both scenes, matching my own and PHOTONICS'
recomputation; the R_COAT/sigma_ext superlinear-scaling figures, below).
Fix 4's own landing (the fabrication-tolerance restatement in
`phase1_proposal.md` §3) — confirmed by direct read, present and
correctly worded.

### 1.3 ELECTROMAGNETISM — dimensional derivation and headroom figure both independently reproduced

Re-derived EM's own closed-form identity from primitives:

```
t156_session_adjusted = HIST_TOTAL/speed_ratio = total_pilot_steps * this_session_per_step_s
     = 24000 * 0.07121022268191168 = 1709.0453443658805   (bit-exact, confirms EM's own algebra)
boundary measured_ratio (rel_dev==0.15) = 3.6680107109370383*1.15 = 4.218213
current measured_ratio                   = 4.11825848092089
relative headroom = 4.218213/4.118258 - 1 = 0.024271   (EM: "~2.4%" — match)
```

**CONFIRMED, exactly.** EM's own residual-confound finding (the
sustained control's 3334-step/scene reading is ~10× shorter than the real
production runs, ~2350s/scene, and measured once, before the spend, not
bracketed after) is a real, distinct, unclosed gap — I checked
`chunk_runner114.py::_time_control_blend`/`run_control()` myself and
confirm no post-spend control reading exists anywhere in this cycle's
scratch directory or `results.json`. EM's own "2.4% headroom in the
unfavorable direction flips CONFIRM to AMBIGUOUS" finding is exact and,
per §2/§3 below, understates rather than overstates the true fragility.

### 1.4 QUANTUM OPTICS — the short-reading alternative independently reproduced; a real, load-bearing finding

Recomputed the alternative scoring using the "short" control reading
(`speed_ratio=0.422112913224623`) instead of "sustained"
(`0.3923112818872906`), from raw `results.json` fields, independent of
QUANTUM's own arithmetic:

```
t156_session_adjusted(short) = 670.4777698516846/0.422112913224623 = 1588.3848819732666
exponent_234(short)           = ln(7038.29048371315/1588.3848819732666)/ln(1.5) = 3.6714567528408675
measured_ratio(short)         = 1.5**3.6714567528408675 = 4.401953...  [confirmed 1.5**exp == t234/t156(short)]
rel_dev(short)                = |measured_ratio-3.6680107109370383|/3.6680107109370383 = 0.20803869914110543
verdict(short)                = AMBIGUOUS
```

Bit-exact to QUANTUM's own cited figures. **CONFIRMED — this is a real,
already-computable-from-data-on-file alternative scoring, and it
genuinely flips the classification.** I also independently re-derived
the speed_ratio-space CONFIRM bounds QUANTUM cites:

```
CONFIRM band in speed_ratio space: [0.29700702179162575, 0.40183302948278776]
used (sustained) position in band: (0.3923112818872906-0.29700702)/(0.40183303-0.29700702) = 0.9092  (QUANTUM: "91%" — match)
short position relative to band:   (0.42211291-0.29700702)/(0.40183303-0.29700702) = 1.1935           (QUANTUM: "19% past the edge" — 0.1935 ≈ 19%, match)
```

**CONFIRMED, exactly.** QUANTUM's own headline finding (the
"sustained-over-short" selection rule was independently ratified,
Iteration 90, for a **different purpose** — cost-gate safety-margin
conservatism — and never independently re-argued for **this** purpose —
an unbiased scientific comparison) is real: I read `run113.py::
combine_control_readings`'s own docstring myself and confirm it states
only the safety-margin rationale, nowhere addressing use as a scientific
normalization denominator. This is the single most load-bearing finding
among the three, precisely because it is not a hypothetical — it is
already computable, already flips the tier, and the committed record's
own justification for its normalization choice ("reused, not
re-derived") does not, on inspection, actually defend the choice for
*this* purpose.

### 1.5 PHOTONICS (self-review) — grid-size ratio and every re-derived figure confirmed; the deepest of the three findings

```
N(r=156, cpl=25) = 1400;  N(r=234, cpl=25) = 2100;  (2100/1400)**2 = 2.25   (PHOTONICS: "2.25x" — match)
```

Confirmed by direct read of `chunk_runner114.py::_time_control_blend`:
the R31 control is measured **exclusively** via
`R.geom_fixedabs_cpl(156, 25)`, hardcoded, never parameterized by the
target r — genuinely, as PHOTONICS states, structurally identical to
`chunk_runner113.py`'s own r=156-only control, inherited unmodified. This
is the same "known, named, still-open" gap THERMODYNAMICS' own
Iteration-90 critique named for the r=312 leg (a 1000-step burst on the
small grid may not represent sustained large-grid throughput) and the
Iteration-91 queue's own Tier-1 item 1 already schedules a fix for at
r=312 — PHOTONICS is correct that exp-114 inherited the identical,
still-open gap at r=234 without anyone flagging it through five blind
Phase-2 critiques and Red Team's own Phase-2 audit (I grepped all six
Phase-2 documents for a grid-size/cross-r control check myself: none
exists). **CONFIRMED — this is the deepest of the three findings**,
because unlike EM's and QUANTUM's (which each concern *which* control
reading to trust), PHOTONICS' concerns whether the control characterizes
the right *quantity* at all — a genuinely different physical grid, 2.25×
the cell count, plausibly more memory-bandwidth-bound. PHOTONICS'
directional argument (a real cross-grid slowdown would push `rel_dev`
*further* toward REFUTE, not away from it, since bigger arrays are more
bandwidth-bound, not less) is physically sound and independently
verified by me against the sign convention (§1.3, above): a *slower*
same-session r=234-grid throughput than the r=156-grid control implies
inflates `t234` relative to what the r=156-derived correction accounts
for, which inflates `measured_ratio` upward, in the *same* direction the
naive (uncorrected) comparison already erred — a real, disclosed,
unbounded risk, not merely a different normalization choice.

### 1.6 THERMODYNAMICS — the CPL_RATIO caution and the dx self-catch both independently verified

Checked THERMODYNAMICS' own disclosed dx-correction arithmetic for
internal consistency (I did not re-derive `item3_thermal_row()`'s full
formula from `thermo_sidecar.py`, which is out of scope for this specific
check, but the ratio of the two margin readings must equal the ratio of
the two dx values if `margin` is inversely proportional to `dx` as the
formula's own structure implies):

```
margin ratio (correct/wrong dx) = 130.1/104.1 = 1.2497
dx ratio (wrong/correct)          = 30/24       = 1.2500   (match, to the two reviewer-printed decimals)
```

**Internally consistent — no defect found.** THERMODYNAMICS' own R9
self-catch (using `cpl=20`'s `DX_M=30e-9` against a `cpl=25`-measured
`sigma_ext`) is a real, correctly-signed instance of exactly the same
error class this cycle's own Phase-4 already caught once — disclosed,
not scored against any verdict this cycle (an informational P5 sidecar
desk-check, not a claim this cycle's own Result rests on). The `core_frac`
fifth-confirming-data-point claim (5.7 ppm at r=234) is independently
confirmed in §1.2, above (and corrects MATERIALS' own transcription
error in the process). The `CPL_RATIO` commensurability caution
(exp-107's own r=156/312 thermal figures are `cpl=20`-derived; this
cycle's own r=234 figure is `cpl=25`-derived, and R30's own founding
instance, exp-112, already established that `_face_flux()`-derived
quantities are not `cpl`-invariant) is a real, correctly-scoped,
forward-looking caution — confirmed by re-reading R30's own registry
text myself.

---

## 2. The Director's own exploratory "v2" recalculation — assessed on the merits

**Independently reconstructed from the raw inputs named in the task**
(not from the Director's own framing):

```
real r=234 per-step rate, this session (empty scene, first 3000 steps, cold build):
    (204.2541103363037+196.82920837402344+214.2100694179535)/3000 = 0.2050977960427602 s/step

historical r=156 per-step rate (3-scene blend):
    670.4777698516846/24000 = 0.02793657374382019 s/step

N ratio squared (r=234/r=156, cpl=25): (2100/1400)**2 = 2.25

synthetic "expected historical r=234 per-step rate" (N^2 scaling assumption):
    0.02793657374382019 * 2.25 = 0.06285729092359542 s/step

speed_ratio_v2 = 0.06285729092359542/0.2050977960427602 = 0.3064747263812162   (Director: 0.30648 — match)

t156_session_adjusted_v2 = 670.4777698516846/0.3064747263812162 = 2187.7098244561093
exponent_234_v2           = ln(7038.29048371315/2187.7098244561093)/ln(1.5) = 2.8819004000499158
measured_ratio_v2         = 1.5**2.8819004000499158 = 3.2171956285212335
rel_dev_v2                = |3.2171956285212335-3.6680107109370383|/3.6680107109370383 = 0.12290452
```

I reproduce the Director's own headline figure exactly (`rel_dev_v2 =
0.1229`, "barely changed from 0.1227"). **But the Director's own stated
uncertainty is well-founded, and my own further analysis shows the
"barely changed" framing is actively misleading, not merely cautious.**

**Finding, independent of anything in the record**: compare the two
methods' own **signed** deviation, not the classifier's `abs()`-wrapped
one:

```
signed_dev(original, sustained-control) = (4.11825848092089-3.6680107109370383)/3.6680107109370383  = +0.12275   (measured_ratio ABOVE reference)
signed_dev(v2, N^2-scaling)             = (3.2171956285212335-3.6680107109370383)/3.6680107109370383 = -0.12290   (measured_ratio BELOW reference)
```

**The two methods' own central estimates of `measured_ratio` sit on
*opposite sides* of `reference_ratio` (4.118 vs. 3.217, a `28.0%`
relative spread between the two central estimates themselves — computed
as `(4.11826-3.21720)/3.21720`), not merely at different distances from
it.** The classifier's own `abs()` construction hides this — both happen
to land at a similar *magnitude* of deviation, so both nominally
CONFIRM, but this is a numerical coincidence of these particular inputs,
not evidence that the two methods agree about which direction reality
deviates from the reference exponent. **This makes the v2 exercise
weaker evidence for CONFIRM than the Director's own cautious framing
already implies — not stronger.** A calculation that, if trusted at face
value, would put the true multiplier at `3.217` (12.3% *below* the
prediction) is not a corroboration of a calculation that puts it at
`4.118` (12.3% *above* the prediction); it is a demonstration that the
answer swings across the entire width of the reference value depending on
which of two reasonable, unverified assumptions is used.

**A further, independent commensurability gap in the v2 construction
itself, not named by the Director**: `HISTORICAL_PER_STEP_S`
(`0.02793657374382019`) is a **3-scene blend** (empty + hollow +
peccored), and this program's own record (exp-113's own EM finding,
`experiments/113-.../phase2_critique_em.md`, an *estimate*, explicitly
"not a profiled measurement") holds that PEC-zeroing makes `peccored`
scenes ~14% costlier per step than `empty`/`hollow`. The real
`r=234`-grid rate used for `v2` (`0.2050978`) is measured on the
**empty scene only**. Blending in a ~14%-costlier third scene inflates
the historical blended rate relative to a clean empty-scene baseline —
meaning `synthetic_hist_r234_per_step`, itself built from that inflated
blended rate, is *also* inflated relative to what a scene-matched
comparison would give, and `speed_ratio_v2` is correspondingly biased
**upward** (toward 1, i.e., toward looking *less* discrepant from the
original 0.3923 than a scene-matched v2 calculation would show). I do
not have the individual per-scene historical rates on file to correct
this precisely (they were lost to exp-112's own known per-scene-average
data gap, Idealization 1, carried unchanged since exp-113), so I state
this as a directional, disclosed, **unresolved** caution, not a
corrected number — but its direction only widens, never narrows, the
28.0% spread already found above.

**Ruling: the v2 calculation is a legitimate, honest, well-motivated
exploratory check — its arithmetic is correct, and I found no error in
it — but it should NOT be added to the permanent record as a
corroborating data point for CONFIRM.** It should be disclosed, if at
all, as a **further sensitivity finding that sharpens, rather than
resolves, the fragility** EM/QUANTUM/PHOTONICS each already named: two
independently-defensible, unverified assumptions (uniform session
slowdown across grid sizes vs. pure `N²` per-step cost scaling with no
other overhead) place the true measured ratio on opposite sides of the
value `KAPPA_COST_EXPONENT` predicts, and neither assumption has been
independently validated against real, matched data (the fix for both is
the *same* cheap, concrete check already ranked #1 below: a genuine
same-session control burst measured directly on the r=234 grid, which
would let this exact `N²`-vs-uniform-slowdown question be answered with
data rather than either assumption).

---

## 3. Verdict-framing decision: CONFIRM-WITH-NAMED-GAPS

The task poses this as the single most consequential call of this
cycle's own Phase 5, matching how Red Team's own final audit decided
framing at exp-113 (Combined Verdict language, §6 there). I rule
explicitly:

**Not plain CONFIRM.** Four independent lines of evidence — EM's ~2.4%
headroom, QUANTUM's already-computable short-reading flip to AMBIGUOUS,
PHOTONICS' untested cross-grid-transferability assumption (with a
correctly-signed argument that a real effect would push the wrong way,
not the safe way), and my own extension of the Director's v2 check
(finding the two leading correction methods disagree about *direction*,
not just magnitude) — converge on the same qualitative point: this
`CONFIRM` sits at 82% of the way to its own boundary (`rel_dev=0.1227`
against `0.15`) under a normalization choice that is real, defensible,
but singular, unreplicated, and resting on an assumption (uniform
per-step slowdown across a 2.25×-larger grid) that nobody — not five
blind Phase-2 critiques, not Red Team's own Phase-2 audit, not the
Director's own Phase-4 catch — checked before this cycle closed. Stating
this plainly as unqualified "CONFIRM" would understate what the record
itself, once all six Phase-5 reviews are read together, actually shows.

**Not a downgrade to AMBIGUOUS.** Three reasons, stated explicitly, not
by default: (1) The pre-registered, correctly-derived (Fix 1, ratio-space)
rule was honestly applied to the actual, real, committed data — overriding
a correctly-executed pre-registered falsifiable test on the basis of
post-hoc alternative-assumption sensitivity, without a validated superior
replacement method, would itself violate this program's own R7 standard
(a conditioning/robustness argument is necessary, not sufficient, to
override a scored verdict — the design must actually be re-fit and
re-calibrated, not merely gestured at) applied here by direct analogy.
(2) There **is** a real, independently-ratified (Iteration 90,
THERMODYNAMICS) physical argument favoring "sustained" over "short" for
long-duration production comparisons specifically — QUANTUM's own §1
makes this case explicitly, and neither the short-reading alternative nor
my own v2 finding overturns it; they only show the *margin* by which
"sustained" wins is thinner than assumed. (3) Every alternative
computation tried — sustained/CONFIRM, short/AMBIGUOUS, v2/CONFIRM —
stays nowhere near the `0.30` REFUTE line; the qualitative finding
("`KAPPA_COST_EXPONENT` generalizes across `kappa_ratio`, once
session-normalized") is robust across every method attempted. What is
fragile is the precise CONFIRM/AMBIGUOUS tier boundary, not the
underlying scientific conclusion.

**Ruling: CONFIRM-WITH-NAMED-GAPS**, matching exp-113's own Phase-5
precedent language for a result that holds under its pre-registered
rule but carries disclosed, real, open questions a future citation must
not elide. The LOGBOOK entry should state the `rel_dev=0.1227` CONFIRM
plainly as this cycle's own scored result, immediately followed by the
three independently-found residual confounds (EM/QUANTUM/PHOTONICS) and
this audit's own v2 finding, each named, none hidden in an Idealization
footnote.

---

## 4. Checkpoint criteria — explicit ruling, all five

- **Criterion 1** (passes all constraint metrics): N/A. T1 correctly
  N/A throughout, confirmed independently by six routes at Phase 2 and
  reconfirmed here by my own direct code read — no constraint-1/2/3/4
  verdict is scored anywhere in this cycle.
- **Criterion 2** (proven mechanism-class boundary): N/A, same reason —
  this is instrument-calibration work, not mechanism work.
- **Criterion 3** (engine physics beyond validated bench classes): N/A —
  no new engine capability is introduced or required.
- **Criterion 4** (unfalsifiable claims; a constraint quietly dropped,
  especially #3) — **the task's own probe, answered explicitly: this
  does NOT fire, and this is a healthy Phase-5 catch working as
  designed, not a program-integrity drift finding — with one condition I
  make explicit below.** Walking the actual chain: Phase 2 caught a real
  gap (the falsifiable heart's own scoring functions were dead code —
  Fix 3) before any real data existed to be mis-scored. The Director's
  own Phase-4 execution then caught a **more serious** R9-class defect
  (the naive cross-session comparison, which would have shipped a
  materially wrong REFUTE) **before freezing any result** — self-caught,
  disclosed, corrected, exactly the "known, named, fixed before it can
  hurt anyone" pattern this registry rewards, not the "known, named,
  ignored" pattern that fires criteria automatically (R6–R32's own
  shared standard). Phase 5 then found three **further, deeper, mutually
  non-overlapping** layers of the same underlying normalization question
  — this is not the SAME defect recurring unfixed (which would be R27/
  R29/R30-style firing territory); it is three independent charter-holders
  doing exactly what PANEL.md assigns Phase 5 to do, on a genuinely new
  result that did not exist before Phase 4 ran. None of the three seats
  argues the CONFIRM verdict is wrong, none argues a check was skipped
  that should have been affordable and wasn't, and none finds the record
  defending an unverified argument against a named, skipped, affordable
  test (the R8 shape) — all three instead **name a concrete, cheap,
  currently-unrun check** that would close their own finding. **My
  explicit condition, matching this registry's own R25 discipline (a
  fix an audit identifies must be promoted to its own numbered
  Reconciled-queue line, not left as a parenthetical or absorbed into a
  differently-worded item)**: Criterion 4 does not fire on THIS cycle's
  own record, but a future cycle that lets these three named confounds
  quietly evaporate from the queue — rather than being explicitly
  executed or explicitly, individually re-deferred with a stated reason —
  would be repeating exactly the pattern R25 exists to prevent. §7,
  below, promotes all three to their own explicit Tier-1 line.
- **Criterion 5** (two consecutive iterations with no logbook-advancing
  result): does **not** apply here — this cycle produced a real,
  falsifiable result (a genuine second `kappa_ratio` calibration point,
  CONFIRM under the pre-registered rule), a self-caught and corrected R9
  defect, and a genuine new standing-rule candidate (R33). This is not
  merely non-firing by a technicality; it is a substantively different
  situation from the "two consecutive non-advancing cycles" this
  criterion targets.

---

## 5. R33 — ratify with BOTH scoping addenda

**Core principle** (Director's own NOTES.md framing, confirmed sound):
a wall-time-based falsifiable comparison that combines a cross-session
historical figure with a same-session real measurement must be scored
against the SAME R31-scaled comparator the cost gate already computes —
never the raw cross-session figure directly. This is a genuine,
single-founding-instance extension of R9/R31 one level deeper (R31 gates
a *spend decision*; this governs a *scored scientific verdict* built from
cross-session wall-time data), exactly the sibling relationship R28 has
to R27 — I ratify the core.

**QUANTUM's addendum — ratified, folded in.** Real, non-hypothetical:
this cycle's own numbers show a purpose-built selection rule (favor the
lower/more-conservative of two same-session control readings, ratified
Iteration 90 for cost-gate safety-margin purposes) silently reused for an
unbiased scientific comparison without independent justification for the
new purpose — and an equally computable alternative reading already on
file flips the verdict tier. Required text: *"When more than one
same-session control reading exists and their selection rule was
justified for a different purpose than the one it is now being reused
for, that reuse requires its own independent justification for the new
purpose, stated in the record, and any alternative reading(s) must be
disclosed as a stated, not-scored sensitivity — not silent inheritance."*

**PHOTONICS' addendum — ratified, folded in.** Real, independently
verified (§1.5): reusing the cost gate's own `scaled.pilot_total_wall_s`
is necessary but not sufficient if the underlying R31 control point was
never itself verified to characterize the same grid/problem size as the
quantity it corrects. Required text: *"The underlying R31 control point
must be verified — not merely assumed — to characterize the SAME
grid/problem size as the quantity it is being used to correct, before the
corrected comparison is trusted as a scored verdict. An unverified
cross-grid transfer is comparatively low-stakes for a conservative-by-
construction gate-margin decision (R31's own original scope); it is not
low-stakes once the same correction is asked to certify a scientific
classification."*

**VISION's four wording notes — adopted as drafting fixes**, folded into
the text below rather than left as a separate critique: scope the trigger
explicitly to wall-time/throughput-derived quantities (not "any ratio or
exponent," which would over-reach into resolution-invariant quantities
like `tau_shell` that carry no session-speed confound at all); state the
relationship to R31 explicitly (this rule extends R31 one step
downstream, from pre-hoc gating to post-hoc scoring, using the identical
machinery); require REUSE of the already-measured control value, not a
freshly-estimated ad hoc factor; and supply an explicit founding-instance/
forward-firing clause.

**Final ratified text (R33):**

> **R33 — a scored ratio or fitted exponent whose operands mix a
> wall-time/throughput-derived quantity measured THIS session with one
> measured or established in a PRIOR session must be normalized by
> re-using the SAME already-measured (or freshly-measured) same-session
> R31 control value the cost gate itself already computes — never a
> raw cross-session figure directly, and never a fresh, separately-
> estimated ad hoc factor (not a ruled-out idea; a standing house-
> discipline rule, proposed by the Director's own Phase-4 self-catch,
> Iteration 91, extending R9/R31 one level deeper: R31 governs whether a
> cost-*gate decision* trusts a cross-session projection; R33 governs
> whether a *falsifiable scientific verdict* built from cross-session
> wall-time data is scored correctly, using the identical machinery one
> step further downstream).** Scope is explicitly restricted to
> wall-time/throughput-derived operands — a physics observable measured
> within a single `Sim.run()` call (a cross-section, a field amplitude,
> a resolution-invariant geometric quantity) carries no session-speed
> confound and is not in scope. Two same-cycle addenda, both required
> before a scored verdict built this way is trusted: **(a)** when more
> than one same-session control reading exists and their selection rule
> was justified for a different purpose than the one it is now being
> reused for, that reuse requires its own independent justification for
> the new purpose, stated in the record, and any alternative reading(s)
> must be disclosed as a stated, not-scored sensitivity (QUANTUM's
> addendum); **(b)** the underlying R31 control point must be verified —
> not merely assumed — to characterize the SAME grid/problem size as the
> quantity it is being used to correct, before the corrected comparison
> is trusted as a scored verdict, distinct from a conservative-by-
> construction gate-margin decision where an unverified cross-grid
> transfer is comparatively low-stakes (PHOTONICS' addendum). **Does not
> fire on its own founding instance** (exp-114) — the naive, uncorrected
> comparison was caught and corrected before any result was frozen, and
> the two addenda's own gaps are disclosed, not defended against a known
> affordable check, matching every prior rule's own founding-instance
> precedent. **Standing forward clause**: a future cycle that scores a
> same-session-measured wall-time-derived ratio or exponent against an
> un-rescaled cross-session historical figure, or that reuses a
> purpose-built control-selection rule for a new purpose without
> independent justification, or that trusts a cross-grid-unverified
> control point for a scored (not merely gated) verdict, on this or any
> channel, after this rule is on the books, fires Checkpoint criterion 4
> automatically — a single-instance-ratified, forward-firing model,
> matching R16/R21–R32's own precedent.

---

## 6. Combined Verdict

**CONFIRM-WITH-NAMED-GAPS** (§3). `KAPPA_COST_EXPONENT` generalizes to
`kappa_ratio=1.5` under the pre-registered, correctly ratio-space-scored
rule (`rel_dev=0.1227`, CONFIRM) — a genuine second calibration point on
this cost-scaling law's own portability, the first ever real check of it
at a ratio other than its own founding one. The cost gate approved this
leg on its first real attempt (36.2% margin), vindicating the r=234
design choice's own stated rationale ("immune to a fourth session-
speed-driven deferral"). A real, consequential R9-class defect (the
naive comparison, `rel_dev=1.86`, REFUTE) was caught and corrected by the
Director before any result froze — a materially better outcome than what
would otherwise have shipped. But three independent Phase-5 seats, plus
this audit's own extension of the Director's exploratory check, converge
on a single, real, disclosed finding: the correction itself rests on an
unverified assumption (uniform per-step session slowdown across a
2.25×-larger grid) that, under one equally defensible alternative
construction, places the true measured ratio on the *opposite side* of
the reference value — a genuinely thinner result than its headline
number alone conveys. Zero Checkpoint criteria fire (§4); R33 is
ratified with both addenda (§5); this cycle's own five Phase-2 mandatory
fixes all landed correctly and completely, independently re-verified by
every one of the six Phase-5 reviews and this audit; one small,
non-outcome-reversing R4-class transcription error (MATERIALS' own r=234
`sigma_abs` figure) is caught and corrected here (§1.2). Trust suite:
41/41, independently re-confirmed this audit stage-by-stage (§8).

---

## 7. Reconciled Iteration-92 queue

Merging all six seats' own ranked lists into one coherent structure,
following exp-113's own precedent of bundling genuinely-the-same-fix
sub-proposals into single combined items rather than treating them as
competing.

### Tier 0 — governance

1. **Ratify R33 as worded in §5** (core + both addenda).
2. **Iteration-85 Checkpoint-4/R24 firing — still awaiting Marsh's own
   convening, now SEVEN cycles pending (Iterations 86 through this
   one).** This is not a panel-process failure (PANEL.md reserves
   Checkpoint convening to Marsh, outside the panel's own authority to
   self-resolve) but the count is now large enough that I recommend the
   Director escalate this directly and explicitly to Marsh, rather than
   let the queue line continue to silently carry forward unconvened.
3. **"Ratify or reject R23 First Addendum / R30 / R31 / R32"** — carried
   in the Iteration-91 queue as a still-open Tier-0 line. On direct
   inspection of the RULED OUT registry's own text, all four already
   carry fully-adopted, in-force language ("ratified by Red Team's
   Phase-5 final audit," "R32 Ratified" — the literal Iteration-90
   LOGBOOK entry title) and have been actively, successfully relied upon
   by exp-112/113/114 without incident. **Recommend the Director close
   this Tier-0 line as already discharged** (a bookkeeping
   reconciliation, not a new ratification act) — unless a distinct,
   higher-level sign-off step exists that this audit is not positioned
   to identify, in which case that step should be named explicitly
   rather than left as an ambiguous repeated queue line.
4. **(0d) COST_GATE_TOTAL_S wall-clock-vs-compute-cost policy fork** —
   unchanged, still Marsh's own call (a genuine policy fork, not a
   discovered defect, per exp-113's own Red Team ruling); correctly not
   resolved by this cycle either.

### Tier 1 — cheap, concrete, closes this cycle's own residual gaps

1. **A genuine same-session control-timing burst measured DIRECTLY ON
   THE r=234 GRID** (a few hundred `empty`-scene steps at `N=2100`) —
   the single highest-value, cheapest item on the board, independently
   ranked #1 by EM, QUANTUM (#2), and PHOTONICS (#1), and the one check
   that would resolve §2's own straddle finding with real data instead of
   two competing assumptions. Bundle EM's own recommendation into the
   same build: repeat the reading once, immediately, to distinguish
   genuine sustained-load degradation from single-sample noise (mirroring
   THERMODYNAMICS' own already-established Iteration-90 precedent for the
   r=156/cpl=25 pilot). Compare the resulting r=234-grid-measured
   `speed_ratio` against the r=156-grid one already on file (`0.3923`);
   if they diverge materially, re-score `kappa_exponent_result` against
   the corrected denominator before this cycle's own CONFIRM is cited
   elsewhere as settled.
2. **Persist and disclose, as a stated NOT-scored sensitivity
   (mirroring the already-established `..._DO_NOT_SCORE` pattern), the
   "short"-reading alternative scoring** (`rel_dev=0.2080`, AMBIGUOUS —
   already fully computed in §1.4/§2, zero marginal cost) **and this
   audit's own "v2" straddle finding** (§2) — with an explicit statement
   of *why* "sustained" is the right choice for *this* purpose (the
   Iteration-90 sustained-load argument, QUANTUM's own §1), not merely
   "reused, not re-derived." This is a forward-disclosure correction to
   the Iteration-91 LOGBOOK entry itself (this program's own established
   practice: never retroactively edit a frozen entry, disclose forward).
3. **Re-attempt the `+168.75°`/r=312/cpl=25 leg — sequenced AFTER item 1's
   own r=234-grid-native control result lands**, reusing whatever it
   finds (a measured or bounded cross-grid slowdown factor) to directly
   inform, or substitute for, the r=312 leg's own already-scheduled
   grid-size-native control point (Iteration-91 queue Tier-1 item 1) —
   per PHOTONICS' own explicit recommendation. Do not trust a fourth R31
   control on this leg without this.
4. **Execute `resolved_unresolved_crosstab`/`apply_crosstab_to_check_c`
   immediately once real r=312 data lands** — carried unchanged from the
   Iteration-91 queue, now with its own composition gap already closed
   (Iteration 90).
5. **MATERIALS' fabrication-tolerance quantitative bound — write the
   actual number, not another restatement.** Now SEVEN consecutive
   cycles named-but-undone (exp-111 through exp-114); zero new FDTD;
   MATERIALS' own Phase-5 review supplies the concrete synthesis (48-bin
   angular check ≤5% at r=156/312, this cycle's own ≤0.011% aggregate at
   r=234, shell thickness invariant at 2.4 design wavelengths across all
   three radii) needed to write one stated tolerance claim. An eighth
   silent cycle should not happen without an explicit Director decision
   to keep deferring, stated as such.

### Tier 2 — cheap riders and continuing items

6. Extend the per-bin (not merely aggregate) core/backing-insensitivity
   check to r=234 (MATERIALS #2) — a cheap rider on Tier-1 item 5, reuses
   already-validated `angular_scattered_pattern` machinery.
7. A `box_dev` floor-gate on the r=234 core-fill delta (THERMODYNAMICS
   #2) — folds into item 6 at near-zero marginal cost.
8. The `fixedabs` family's third P5 thermal-margin point at r=234 —
   **only once the CPL_RATIO commensurability gap is resolved first**
   (either re-derive the r=156/312 figures at cpl=25, or apply a derived
   correction factor) — THERMODYNAMICS' own explicit caution against a
   naive attempt.
9. A fourth r-point (r≈624) — serves BOTH MATERIALS' own newly-surfaced
   `σ_ext`-vs-`R_COAT` superlinear residual AND THERMODYNAMICS' own
   `r^-1.16` thermal-margin projection test; scope one run to serve both
   questions rather than two separate future proposals converging on the
   identical geometry a cycle apart (MATERIALS' own explicit request).
   This point would also double as EM's/PHOTONICS' own #3 — a third
   `kappa_ratio` point, ideally on the *far* side of the founding pair
   (`kappa_ratio>2.0`), once r=312 is unblocked.

### Tier 3 — bigger builds; not this cycle's own direct debt

10. **VISION's own charter-level argument, given real weight, not
    buried**: re-score the program's ONLY EVER Tier-W/Tier-A constraint-3
    citation (exp-032/033's `off_pass`/`off_bracket`) through the now
    fully-modernized ambient-contrast instrument (settled STEPS≥2800,
    PAD/ABSORB decorrelation, N17-or-denser quadrature, T21's own
    fringe/floor characterization) — no prior cycle has run this specific
    synthesis since Iteration 12. This is the single highest-value
    NEW-territory move available if/when the Director chooses to
    re-engage constraint 3 directly, rather than continue this 46-
    iteration-deep T28 governance/instrument sub-thread. Ranked below
    Tier 1/2 only because those are cheaper, more directly load-bearing
    to THIS cycle's own open questions, and closer to completion — not
    because this item matters less.
11. Execute the standing "does `PAD`-sensitivity survive with a real
    absorbing article loaded" check (VISION #2) — 15+ cycles deferred.
12. Build N33, the third angular-quadrature convergence point (VISION
    #3) — queued since Iteration 13, apparently never executed.
13. `R2_SMOOTH_THRESHOLD=0.90` re-derivation — noted only by
    THERMODYNAMICS, outside that seat's own charter, to avoid this
    review's own silent omission of a tracked debt; low priority.

---

## 8. Trust suite — re-run this audit, individual stages (`--only 1..9`,
## skipping 5, per this cycle's own disclosed contention)

A combined `--only 12346789` invocation was not attempted (this audit's
own session inherited the same severe shared-sandbox contention every
Phase-2 and Phase-5 seat this cycle already disclosed, confirmed directly
via `ps aux`/`/proc/loadavg` before any suite command was issued).
Individual stages, each independently executed to completion this
session:

| Stage | Checks | Result |
|---|---|---|
| 1 | 3 | PASS (λ=19.97 cells, peak\|Ez\|=2.52, shadow ratio=0.479) |
| 2 | 3 | PASS (R=0.0983/0.0178/0.0177) |
| 3 | 4 (incl. `ours-small` prerequisite) | PASS (corr=0.928, λ=19.96/20.37, shadow 0.451 vs 0.498) |
| 4 | 3 (incl. `ours-small` prerequisite again) | PASS (ceviche corr=0.956, λ=19.80) — required isolating this stage alone (killing my own earlier redundant concurrent attempts) before it completed cleanly in 8s |
| 6 | 5 | PASS (observer/emitter identities) |
| 7 | 5 | PASS (absorber R≤0.002 at all 3λ, sponge/PEC ratio 0.000) |
| 8 | 6 | PASS (cross-section identities, graded-black abs/ext=0.571) |
| 9 | 13 | PASS (ambient identities, \|C_empty\|=0.00043, Beer–Lambert agreement) |

Naive sum `3+3+4+3+5+5+6+13=42`; deduplicating the `ours-small`
prerequisite (computed and printed identically by both standalone `--only
3` and `--only 4`, per this program's own R19 discipline — call-count is
not distinct-check-count) gives the true unique total: **41/41, all
PASS, every one independently confirmed by direct execution this
audit.** `git diff --stat -- lab/` empty throughout — zero `lab/`
regression, matching every one of this cycle's own six Phase-5 reviews
and the Director's own Phase-3/Phase-4 confirmations. I did not modify
any file other than this one.

Full record supporting every figure above: `phase1_proposal.md`, all
five Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`,
`run114.py`/`chunk_runner114.py`/`analyze114.py` (unchanged, read only),
`results.json` (unchanged, read only), and all six Phase-5 reviews.
