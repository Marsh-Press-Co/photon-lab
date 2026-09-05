# Phase 5 Review — QUANTUM OPTICS

**Cycle:** exp-114, Panel Iteration 91. Fresh context, blind to the other
seats' current Phase-5 reviews, per PANEL.md's independence mechanics.
Charter note (unchanged from my own Phase-2 critique, `phase2_critique_
quantum.md`): pure T28 instrument-calibration work, zero σ(I)/σ(x,t)/
dispersive-ε(ω)/gain content — my seat's actual value here, per this
program's own R32 precedent (my own founding catch, exp-113), is
adversarial reading of code/math for silent inversions and premise
violations. That is exactly what this review does.

## Headline finding — stated first, per the task's own instruction

**The corrected CONFIRM verdict is fragile to a normalization choice the
committed record never independently defends, and an equally legitimate
alternative choice already sitting in this cycle's own `results.json`
flips it to AMBIGUOUS.** This is not a claim that CONFIRM is wrong — I
think it is more likely right than not, for reasons given below — but the
record currently asserts it as settled, and it is not, on the record as
written. Full derivation follows in §1.

## 1. Independently re-deriving the R9 fix from scratch

I recomputed everything from `results.json`/`run114.py`'s own primitives,
not from `NOTES.md`'s prose:

```
t156_hist (raw historical)      = 670.4777698516846
t234_cpl25 (this session, real) = 7038.29048371315
KAPPA_COST_EXPONENT             = 3.2053299988171697
kappa_ratio                     = 1.5
reference_ratio = 1.5**3.2053299988171697 = 3.6680107109370383
```

The naive comparison (`t234` vs. raw `t156_hist` directly) reproduces
`results.json`'s own `kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE`
bit-exact: `exponent_234=5.7986`, `rel_dev=1.8619`, REFUTE. This confirms
the defect the Director caught is real: `t156_hist` was measured in a
different session running at a genuinely different (and, per R31's
`used_speed_ratio=0.3923`, ~2.55× slower-appearing) per-step throughput
than this session — comparing it directly against a same-session `t234`
is exactly an R9-class operand-commensurability violation (the registry's
own text: *"verifying a cited ratio's arithmetic is not sufficient to
verify the comparison's own claim; the operands' commensurability must be
independently confirmed"*). **The catch itself is correct and a real,
valuable find** — a materially wrong REFUTE would otherwise have frozen.

But the task's own probe — short vs. sustained — is the right one to
press, and it exposes something real:

```
                          t156_session_adjusted   exponent_234   rel_dev   verdict
sustained (0.3923, USED)  1709.045s               3.4909         0.1227    CONFIRM
short     (0.4221, ALT)   1588.385s               3.6715         0.2080    AMBIGUOUS
```

**Both figures are re-derived bit-exact from `results.json`'s own
`r31_control` block** (`short.speed_ratio=0.422112913224623`,
`sustained.speed_ratio=0.3923112818872906`) — this is not a hypothetical,
it is a second scoring already computable from data already on file this
cycle, using the exact same `refit_kappa_exponent`/
`classify_kappa_exponent_check` functions, with no new FDTD spend. The
choice between two control readings measured in the *same* R31 pre-spend
control step, at the *same* session, flips the falsifiable heart of this
cycle's own result between CONFIRM and AMBIGUOUS.

**Why this happened, mechanistically:** `analyze114.py` line 111
(`t156_session_adjusted = R.HISTORICAL_R156_CPL25_TOTAL_S /
control["used_speed_ratio"]`) reuses `combine_control_readings()`'s
`used_speed_ratio` — a value `run113.py`'s own docstring (reused verbatim
by `run114.py`, confirmed unmodified) says is selected by *"gate[ing] on
the LOWER of the two speed_ratio values (lower speed_ratio = this session
reads/is assumed SLOWER relative to history = a LARGER, more conservative
scaled projection)"*. That selection rule was designed, justified, and
ratified (Iteration 90, R31/Fix 4) for exactly one purpose: a **cost-gate
scope decision**, where the asymmetric risk (an overrun spend is expensive;
an over-cautious refusal is cheap) makes deliberately biasing toward "the
session is slower than it looks" the correct engineering choice. `analyze
114.py`'s Fix-1/R9 correction imports this exact same selected value,
unmodified, into a **different kind of question** — a symmetric-risk
scientific comparison, where what is wanted is the best unbiased estimate
of this session's true relative throughput, not a deliberately
conservative one. Nowhere in `run114.py`, `analyze114.py`, or `NOTES.md`
is that substitution independently argued; `NOTES.md` itself says only
"reused, not re-derived." **This is precisely the mirror-image risk the
task asked me to check for**: not that the R9 fix inverted a sign, but
that it silently carried a purpose-specific selection rule (safety-margin
gating) across into a purpose it was never validated for (unbiased
scientific rescaling) — the same species of defect as R32's own founding
instance (a recalibrated statistic's *direction* needing independent
validation before being scored evidentially in a new context), one level
removed: here it is a control mechanism's *selection rule*, not a
statistic's *direction*, that crossed a purpose boundary unvalidated.

**Does this mean CONFIRM is wrong?** I do not think the record supports
that stronger claim, and I want to be precise about why, because the
physical case for `sustained` is not vacuous. THERMODYNAMICS' own
Iteration-90 Phase-2 finding (ratified into Fix 4, `LOGBOOK.md` Iteration
90) established that a 1000-step burst under-samples sustained-load
effects (turbo-boost decay, cache/memory-bandwidth saturation) and reads
"anti-conservatively" (artificially fast) relative to true sustained
throughput — i.e., there is an independently-ratified, house-established
physical argument that `sustained` is not merely "more conservative" in a
safety-margin sense but closer to the *true* long-run throughput. Because
this leg's real production runs (2326–2356s/scene) are themselves
long-duration jobs, `sustained`'s own physical rationale (closer to
true sustained-load throughput) is the more directly applicable one for
*this* purpose too, not an accidental transplant. And critically, the
direction of any residual error cuts the *safe* way: if the true speed_
ratio during the actual ~2340s/scene runs is even lower than sustained's
own 712s-control reading (because degradation continues past what a
712s burst can see — a live, unresolved possibility, since this leg's
production runs are themselves ~3.3× longer than the sustained control
and both control readings still only exercise the r=156 grid, not r=234 —
the same GRID-SIZE half of the confound VISION SCIENCE's own Iteration-90
review flagged as unclosed for the r=312 leg, inherited here unmentioned),
`measured_ratio` moves further *below* 4.118, i.e. **toward**, not away
from, `reference_ratio=3.668` — this would make CONFIRM *more* secure, not
less. The vulnerable direction is the other one: some mechanism by which
throughput partially *recovers* after an initial sustained-load dip (e.g.
transient throttling settling to a stationary rate faster than the
1000-step burst suggests) would push the true speed_ratio back up toward
or past 0.4018 (the CONFIRM band's own upper edge in speed_ratio-space —
see §3), which is a live possibility this cycle's two-point (short,
sustained) control cannot rule out, only bound.

**Recommendation, concrete and cheap:** before this freezes, `NOTES.md`/
`analyze114.py`'s own comment should state the actual justification (the
Iteration-90 sustained-load argument) for reusing `used_speed_ratio` in
the kappa_exponent context, not merely "reused, not re-derived" — and
should disclose the short-reading alternative and its AMBIGUOUS result as
a stated sensitivity, exactly as the naive/uncorrected reading is already
disclosed (not scored) alongside the corrected one. The mechanism for
disclosing an alternative that was tried and rejected already exists in
this exact file (`kappa_exponent_result_naive_uncorrected_DO_NOT_SCORE`);
the short-reading alternative deserves the identical treatment, e.g.
`kappa_exponent_result_short_control_sensitivity_DO_NOT_SCORE`, computed
at zero marginal cost from data already on file.

## 2. Fresh sign/direction/base check, as if new

Independently re-derived, ignoring `NOTES.md`'s narrative:

- `refit_kappa_exponent(t156, t234, kr) = ln(t234/t156)/ln(kr)` — same
  direction as the founding fit (`ln(t312/t156)/ln(2.0)`, R110). No sign
  flip: `t234 > t156` and `kr=1.5>1` both point the same way as the
  founding case (`t312>t156`, `kr=2.0>1`); a slower/larger-r scene costing
  more is the physically expected sign, and the code delivers it in both
  the founding and this leg's own instance.
- `classify_kappa_exponent_check`'s `measured_ratio = kr**exponent_234`
  is `kr**(ln(t234/t156)/ln(kr))`, which is algebraically identical to
  `t234/t156` by construction (`kr**(log_kr(x)) = x`) — I confirmed this
  numerically (`4.118258...` both ways) rather than trusting the identity
  by inspection. No hidden asymmetry between `measured_ratio` and
  `reference_ratio`'s own construction — both are `kr**(exponent)`
  evaluated at the same `kr`, one from a fresh fit, one from the frozen
  founding constant. This is the correct, base-consistent comparison; I
  found no inversion here.
- `t156_session_adjusted = t156_hist / speed_ratio`, not `t156_hist *
  speed_ratio` — checked the direction against the definition
  (`speed_ratio = historical_per_step_s / this_session_per_step_s`,
  `run113.py` line 158): `speed_ratio < 1` means this session is slower,
  so `t156_hist` (measured on the faster historical session) must be
  **inflated** (divided by a number <1) to estimate what it would have
  cost on this slower session — the code does this correctly. I checked
  the alternative (multiplying) explicitly and it gives a nonsensical
  answer (`t156_hist * 0.3923 = 263s`, implying the historical run would
  have been *faster* on a session already established to be *slower* —
  wrong-signed on its face), confirming the actual code's direction is
  the correct one, not merely unchallenged.
- The Fix-1 ratio-space rescoring itself: re-verified
  `(1.5**KAPPA_COST_EXPONENT)` independently equals `3.6680107109370383`
  and that this is what `reference_ratio` uses — not, e.g., a leftover
  `2.0`-base holdover from the founding fit. Confirmed clean.

No sign, direction, or base error found anywhere in the R9 fix or in
Fix 1's own ratio-space rescoring. The one defect I found (§1) is a
purpose-mismatch in which of two legitimately-measured numbers gets used,
not an arithmetic or directional error.

## 3. Single-measurement fragility (task item 3)

`refit_kappa_exponent` is fit from exactly one real `t234` value (no
replicate), exactly the fragility pattern `KAPPA_COST_EXPONENT` itself
already carries from its own single-`(t156,t312)`-pair founding fit
(exp-110/111) — this cycle adds a second single-point pair to that
chain, it does not cure the pattern.

Is `rel_dev=0.1227` against the `0.15` CONFIRM band comfortable? **No —
it is close, and demonstrably close in a load-bearing sense.** Converting
the band to `speed_ratio`-space (holding everything else fixed) gives a
CONFIRM-compatible range of `speed_ratio ∈ [0.2970, 0.4018]`. The reading
actually used, `0.3923`, sits at **91% of the way from the band's lower
edge to its upper edge** — i.e. within about 9% of the band's own width
from flipping to AMBIGUOUS, and the short reading (`0.4221`) is already
19% of a band-width past that edge. Given this program's own
independently-established session-to-session throughput swing of
`0.39×`–`2.19×` (over 5× total spread, LOGBOOK Iteration 89/90/this
cycle), and given that even a *same-session* choice between two control
readings already spans more than half the CONFIRM band's own width, a
single uncontrolled re-measurement of `t234` in a different session could
plausibly land anywhere from comfortably CONFIRM to REFUTE. **This is
exactly the kind of single-measurement fragility this program's own
KAPPA_COST_EXPONENT founding fit already carries — this cycle inherits
it, at a margin (~82% of the way to the CONFIRM boundary) that should be
called "close," not "comfortable."**

## 4. Should R33 be ratified, as scoped?

**Ratify the core, but only with a scoping addendum before it freezes.**
The core principle — a cross-session historical figure must not be
compared directly against a same-session real measurement without a
same-session-control rescaling — is real, correctly generalizes R9, and
this cycle is a genuine, non-hypothetical founding instance (the naive
reading really would have shipped a wrong REFUTE). It should be ratified.

But as narrated in `NOTES.md`, R33 says only "rescale by the session's
own measured speed_ratio" — it does not address *which* of several
candidate same-session-control readings to use when more than one exists,
nor that a selection rule built for one purpose (a conservative cost-gate
margin) is not automatically valid for a different purpose (an unbiased
scientific-comparison denominator) without independent justification for
the new use. §1 shows this is not a hypothetical gap: it is the exact
gap this cycle's own numbers expose. **Recommended addendum, to be
folded into R33's text before it freezes, not left as a separately-named
future risk:** *"When more than one same-session control reading exists
and their selection rule (e.g., 'use the more conservative/lower of two
readings') was justified for a different purpose than the one it is now
being reused for, that reuse requires its own independent justification
for the new purpose, stated in the record — not silent inheritance."*
This is the natural, narrow extension of R32's own precedent (a
recalibrated statistic's *direction* needs independent validation before
evidentiary use in a new context) to a control *mechanism's selection
rule* crossing the same kind of purpose boundary.

## 5. Argument for Iteration 92, from this seat's own lens

Ranked:

1. **Close the sensitivity gap named in §1 before this result is cited
   evidentially anywhere else** — persist the short-reading alternative
   scoring (`kappa_exponent_result_short_control_sensitivity_DO_NOT_SCORE`,
   mirroring the naive-uncorrected field's own disclosure pattern) and
   state explicitly, in `NOTES.md`, why `sustained` rather than `short` is
   the right choice for *this* purpose (the Iteration-90 sustained-load
   argument, not merely "reused, not re-derived"). Zero marginal FDTD
   cost — both numbers already exist in `results.json`'s own inputs.
2. **Fold the R9/R33 finding into a concrete third control point on the
   real target grid** (a bounded, cheap `r=234`-grid empty-scene timing,
   the same fix the Iteration-91 queue already schedules for the r=312
   leg's own grid-size confound, Tier-1 item 1) — this would replace the
   §1 sensitivity question with a direct measurement rather than a
   disclosed uncertainty, for whichever leg runs next.
3. **Tighten R33's text per §4** before the Director's LOGBOOK entry
   freezes it — cheap, document-only, and closes exactly the gap this
   review found.
4. Continue the Tier-1 `+168.75°`/r=312 leg per the Reconciled
   Iteration-91 queue, applying R33 (as tightened) to its own R31 control
   from the start rather than retrofitting it.

## Trust suite

Re-ran `python3 lab/validation/run_all.py --only 12346789` from repo
root, this session, fresh: **41/41 checks PASS**, clean single run
(2461.6s wall, no contention this time — this session had the sandbox to
itself). No `--only 1..9` fallback was needed. This matches every prior
seat's own confirmation this cycle and the Director's own Phase-4
re-confirmation; no new `lab/` diff exists for this suite run to have
caught, and none was introduced by this review (read-only throughout,
this file excepted).

## Verdict

**PARTIAL.** Not RULED OUT — T1 escape route is correctly N/A throughout
(confirmed independently by six routes at Phase 2, reconfirmed here by a
direct, fresh code read finding no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold content anywhere in this cycle); the R9 catch is real and
prevented a materially wrong REFUTE from freezing; the cost gate's own
first-attempt approval genuinely vindicates this leg's r=234 design
choice; nothing here is falsified. Not cleanly PROMISING either: the
CONFIRM verdict this cycle presents as its own "falsifiable heart"
resolving cleanly is, on independent re-derivation, a result whose
verdict flips to AMBIGUOUS under an equally legitimate, already-measured
alternative normalization present in this cycle's own `results.json` —
and the committed record neither discloses this sensitivity nor argues
for its own choice beyond "reused, not re-derived." That gap should be
closed (§1/§4, cheap, zero-FDTD) before this cycle's CONFIRM verdict
freezes into LOGBOOK.md as settled fact alongside R33.
