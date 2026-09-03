# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 82
## exp-105 — "The T8 r=78/156/312 Bridge, Extended to the Coherent Point/Region-Intensity Channel"

*Fresh seat, blind to any other seat's current-cycle Phase-5 review. Read in
full before writing: `PANEL.md`, `LOGBOOK.md` (RULED OUT R1–R23; T1, T8,
T9, T13, T14, T28 Live Threads; the exp-030/Iteration-7 and
exp-102/103/104/Iteration-79/80/81 full transcripts), the complete exp-105
record (`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`), and
`experiments/030-scale-bridge/NOTES.md` for direct comparison.*

## 0. Independent numeric verification (direct against `results.json`)

Recomputed every headline figure from the raw persisted fields, not from
NOTES.md's prose:

- `kappa_windows`: r78=0.018336958179764707, r156=0.0008866623871477821,
  r312=4.79303718569495e-06 — matches NOTES.md exactly.
- Step ratios, computed directly: **r78/r156 = 20.6809** (NOTES.md's
  "~20.7×"), **r156/r312 = 184.99** (NOTES.md's "~185×") — both confirmed
  to 4 sig figs.
- `p3.shape_ratio = 19.787847024468125` — confirmed exactly:
  `(k78−k156)/(k156−k312) = 19.787847...`. Model-A miss = 0.855461... =
  **85.55%**; Model-B miss = 0.759276... = **75.93%** — both confirmed
  exactly against the persisted `model_A_miss`/`model_B_miss` fields.
- `geom_*` Fresnel/Nyquist fields (`nyquist_margin`, `predicted_ripple_
  period`, `z_over_zr`): recomputed from the stated formulas
  (`z_over_zr(r)=D_EFF·LAMBDA_CELLS/r²`, `predicted_period=LAMBDA_CELLS·
  D_EFF/r`, `margin=period/(2·DENSE_PITCH)`) — all reproduce exactly:
  r78 margin=4.9359 (TRUSTED), r156 margin=2.4679 (TRUSTED), r312
  margin=1.2340 (MARGINAL). This is the corrected figure — the Phase-1
  proposal's own hand-typed `z_over_zr` sentence (a 10×-low triple
  compounded with a second, separately-wrong ≈6.1×-low range bracket, per
  three independent Phase-2 catches plus Red Team's own fourth
  re-derivation) was fixed exactly as committed; `run.py::geom()` now
  computes and prints it, never hand-typing it again. Verified.
- r156 settling: recomputed `max(rel_change)=0.01380` (1.38%, tolerance
  20%, **~14.5× inside**) and `max(phase_diff)=0.00673` rad (0.386°,
  tolerance 0.20 rad ≈ 11.46°, **~30× inside**) directly from the 53
  persisted `settling` records. This is not a marginal pass — it is
  comfortably clean, by more than an order of magnitude on both channels.
  `settling_overall_pass=True`, `p4_trusted(r156)=True` — confirmed.
- Gate P0/P1: `pass_=True` both, `max_rel=0.0` for Gate P1 — confirmed.
  `n_fdtd_calls=6`, `total_wall_s=3883.3` — confirmed against the file.

**All headline numeric claims in NOTES.md's Result/Learned sections
reproduce exactly from `results.json`.** No R4-class citation defect found
on independent re-derivation.

## 1. Is the accelerating collapse optically coherent? — a sharper diagnostic than NOTES.md's own framing

NOTES.md correctly declines to interpret the accelerating shape (R3
meta-rule: a surprising feature gets a resolution check before a
mechanism debate) and flags it for Phase 5. Independently deriving the
mechanism question the task poses:

**The proposed mechanism ("fixed window offset as an ever-shrinking
fraction of the growing object's own radius, pushing the measurement
deeper into the near zone") is directionally correct but, taken as any
single global power law, predicts a *self-similar, non-accelerating*
decline — not the observed one.** Because `x(r)=√(z/z_R)∝1/r` is forced
exactly (`x78:x156:x312 = 4:2:1`, independently confirmed:
0.50311/0.25156=2.0000, 0.25156/0.12578=2.0000), any two-parameter power
law of the form `κ(x)=κ_∞+B·x^n` obeys a clean, exact identity for this
specific 4:2:1 geometry:

```
shape_ratio = [κ(4X)−κ(2X)] / [κ(2X)−κ(X)]
            = (4^n−2^n)/(2^n−1) = 2^n(2^n−1)/(2^n−1) = 2^n
```

independent of κ_∞ and B, and independent of n. (Sanity check: n=1 gives
2, n=2 gives 4 — exactly the two pre-registered bands, confirming this is
the same forcing already implicit in how those bands were derived, just
generalized to arbitrary n.) **The measured `shape_ratio=19.79` therefore
does not merely miss the two pre-registered candidates — it is exactly
equivalent to an implied global exponent `n = log₂(19.79) ≈ 4.31`.** That
is a specific, falsifiable characterization NOTES.md's own text does not
state, and it sharpens rather than merely restates the miss percentages.

**Is n≈4.3 physically plausible for this mechanism?** Direct transmission
through the shell is not the relevant channel here (τ_shell=24 held
constant at every r kills it identically at all three scales — e^-24 is
negligible regardless of r, so it cannot be the source of an r-dependent
signal). The physical channel that *can* carry an r-dependent signal into
this fixed-offset, on-axis window is edge diffraction around the shell's
own boundary — exactly the mechanism this program's own founding T8 cycle
(exp-030 Phase 5, my seat, and independently EM) identified for the
*identical* article and the *identical* forced x-ratio structure, using
classical Fresnel-zone/boundary-diffraction-wave (Rubinowicz–Maggi)
theory: intensity deep in a hard-edged obstacle's geometric shadow falls
off asymptotically as a low power of the Fresnel number (order N_F^-1,
i.e. n≈2 in this x-convention, for a knife-edge/disk asymptotic — which
is exactly Model B's own pre-registered "linear-law" candidate). An
implied **n≈4.3 is roughly double the steepest of the two
theory-motivated candidates already tested and refuted**, not merely
"outside the band" but requiring a qualitatively steeper falloff than
standard scalar edge-diffraction asymptotics predict for this geometry.
Note also this shell is *apodized* (graded conductivity, not a hard PEC
edge) — apodization is the standard technique for *suppressing*
Fresnel-ripple and diffractive leakage, which if anything should make the
falloff *shallower*, not steeper, than the hard-edge asymptotic — the
opposite of what n≈4.3 would require if it is a real optical effect.

**Directly answering the task's question: the "fixed-offset-as-shrinking-
fraction" mechanism, taken as a single global near-field power law, does
NOT by itself predict acceleration of this magnitude or shape — it
predicts a constant per-halving ratio (self-similar decline) for ANY
fixed exponent.** The four-orders-of-magnitude total drop is not, on its
own, absurd for a τ=24 shell's diffracted leakage over this x-range; the
*specific accelerating* two-ratio pattern (20.7× then 185×, an 8.9×
further steepening) is what is not explained by the stated mechanism, and
is not obviously explained by any standard edge-diffraction asymptotic
either — a genuine anomaly, correctly left uninterpreted by NOTES.md, but
more precisely characterized here as "the data, if it follows this
family's own functional form at all, implies n≈4.3 — well outside the
n≈1–2 range motivated by the standard theory, and moving in the wrong
direction for an apodized edge specifically" rather than merely "misses
both bands by a lot."

## 2. A genuine, independently-found defect: the headline metric itself is never floor-gated

This program has a repeated, hard-won house lesson (T7's δ_C empty-scene
floor; T11's box-ledger floor; the R13/R14 ratio-floor lineage) that a
small or collapsing reading must be checked against a measured decision
floor before it is trusted, especially the smaller/more surprising it is.
Checked `run.py` directly for whether this discipline was applied to
`kappa_window` — the metric that actually produces the headline
shape_ratio=19.79 finding:

- `floor_gate()` is called exactly three times in this file (lines 586,
  587, 675): on the per-x `wide`/`point` DENSE_X channel intensities at
  r=156 (both channels) and r=312 (wide channel only). **It is never
  called on `window_stats()`'s own output at any r** — `win_e156`,
  `win_a156`, `win_e312`, `win_a312` (lines 571–572, 666–667) feed
  directly into `kappa_window_156`/`kappa_window_312` with no floor check
  of any kind. `window_stats()` itself computes `min`/`max`/`std` in
  addition to `mean` (line 234) — none of the three unused fields is ever
  read, printed, or persisted; only `mean` is used.
- **The r=312 point-channel raw intensities are not merely unfloor-gated
  — they are discarded outright.** Line 673: `k_p, _, _ =
  kappa_region_point(ez_e312, ez_a312, x, g312["CY"])` — the two
  underscores throw away `i_e_p`/`i_a_p`. Unlike the r=156 leg (which
  persists `point_channel`, `floor_gate_point`, `wide_channel`,
  `floor_gate_wide` in full), `results.json::r312` persists only `p2,
  p2_reversals, p4, nyquist_tier, quintiles, committed` — no window means,
  no point-channel intensities, no floor gate of any kind for the r=312
  leg. I confirmed this by direct inspection of the persisted dict.

**Consequence: NOTES.md's own Next item 1 asks "is `kappa_window(312)=
4.8e-6` a genuine effect or a floor/dynamic-range artifact?" — and the
one piece of instrumentation that would answer that question (a floor
gate on the window itself, or even just the raw persisted window/point
means at r=312) does not exist anywhere in this cycle's own code or
output.** This is not a hypothetical gap: r=312 is simultaneously (a) the
point doing most of the work in the "accelerating" framing (the 185×
step, not the 20.7× one) and (b) the least-instrumented point this cycle
built — MARGINAL Nyquist tier, no settling leg, and now confirmed no
floor gate and no persisted raw intensities either. None of the five
Phase-2 critiques or Red Team's own audit caught this specific gap (their
attention, correctly, went to the settling leg on the point-channel P4
machinery and the Nyquist/Fresnel pre-check — both real and both
correctly fixed, see §3) — this is a fresh finding at Phase 5.

This does not overturn P2 (monotonicity) or invalidate the r=78→156 step,
which is well inside every gate this cycle built. It does mean the
specific numeric claim "accelerating, not merely failing to fit a power
law" — which leans most heavily on the r=312 point — rests on a reading
this cycle cannot itself distinguish from a floor/dynamic-range artifact,
by its own now-identified missing instrumentation, not merely by
inference.

## 3. Settling/Nyquist-gating machinery (mandatory fixes 3/4) — implemented correctly, and it makes good optical sense

Checked this from an optical-coherence standpoint, as asked. Two separate
pieces of machinery, both correctly built:

- **The Fresnel/Nyquist pre-check** (`geom()`'s `z_over_zr`/`predicted_
  ripple_period`/`nyquist_margin`) is a sound, physically-motivated
  desk-only diagnostic: it predicts, before any r=312 call ran, that the
  sub-Nyquist sampling margin on `DENSE_PITCH=2` cells would degrade
  exactly to the MARGINAL tier at r=312 (1.234) while staying TRUSTED at
  r=156 (2.468) — and the run confirms these are the tiers actually
  applied. This is the right fix for QUANTUM's Phase-2 attack (a fixed
  absolute pitch under a shrinking predicted ripple period as N_F grows)
  and correctly propagates reduced confidence to r=312's P4 reading
  without silently treating it as equal to r=156's.
- **The point-channel settling leg is correctly targeted and physically
  sensible.** A zero-averaging, single-cell (`H_REGION_POINT=0`) phasor
  reading is exactly the kind of measurement most exposed to residual
  transient/interference structure that a spatially-averaged box would
  suppress (this program's own precedent: exp-103's Phase-5 finding that
  an 11-cell box average suppresses ~91% of a comparable ripple via a
  sinc argument) — so a settling check that only ever covered the wide
  channel (exp-103's own leg) genuinely does not bound the point channel
  P4 depends on, exactly as EM's Phase-2 attack argued. For a linear,
  passive, non-resonant medium (confirmed T1-clean, no gain, no cavity),
  doubling STEPS should drive both amplitude and phase toward their true
  steady-state values monotonically as boundary-launched transients decay
  — and §0 above shows this is exactly what happened, with large margin
  (14.5×/30× inside tolerance), not a narrow pass. The chosen tolerances
  (20% relative on intensity, 0.20 rad on phase) are the same house
  convention already established for the wide channel (exp-103), so this
  is a like-for-like extension, not a new arbitrary bar — and the actual
  result cleared it by more than an order of magnitude, so the specific
  tolerance choice is not doing any real work in this outcome.

One disclosed, correctly-flagged gap remains, not a defect: no settling
leg exists at r=312 at all (an explicit Next item), which is exactly the
scale where §2's own missing-floor-gate concern also concentrates — two
independent reasons the r=312 leg specifically should not be read with
the same confidence as r=156's clean 20.7× step.

## 4. A pre-registered prediction silently dropped: P3b

The Phase-1 proposal's own §4 explicitly pre-registers **P3b**, framed
in its own words as "this cycle's own genuinely new prediction, not in
T8's own structure" and "materially informative for T13 either way": the
**sign of Model A's slope B**. `B>0` was defined as the "right-direction"
reading (does not replicate T14's own wrong-direction-shallowing
pathology on the ambient channel); `B<0` would "directly replicate T14's
own... pathology on this new, structurally different coherent-intensity
channel."

Checked NOTES.md (Predictions and Result/Learned sections), `run.py`'s
`build_predictions_text()`/`result_text`, and grepped for "P3b", "sign",
"right-direction", "wrong-direction", "T13", "T14" throughout NOTES.md:
**P3b is entirely absent from the frozen Predictions text, the Result
section, and the Learned section.** It is not falsified, not scored, not
mentioned. The underlying number needed to answer it, however, **is**
computed and persisted: `results.json::p3.model_A_B = +0.007011...` —
positive, i.e. the "right-direction" reading — meaning this cycle's own
data, silently, already answers the one genuinely-new (not
T8-replicating) sub-question this proposal itself flagged as materially
informative for the still-open T13 thread, and that answer never reached
NOTES.md's prose. This is the same shape this program's own R21 rule
names (a persisted field's own headline finding never stated in
Result/Learned prose) applied one level upstream — here a whole
*pre-registered prediction*, not merely a sidecar byproduct, silently
disappeared between Phase 1 and the frozen Phase-3 text, with no Phase-2
critique or Red Team fix discussing its removal. Given R21's own
three-strike forward clause is scoped to the NETD/thermal channel
specifically, I am not asserting this fires any numbered rule — I am
independently reporting it as a genuine gap this seat's numeric-
verification duty (R4/R9 discipline) is obligated to surface.

## Verdict

**CONFIRM-WITH-GAPS.**

All numeric claims (shape_ratio, model misses, kappa_window values,
Nyquist/Fresnel margins, settling residuals, wall time, gate results)
independently reproduce exactly from `results.json`. The settling and
Nyquist-gating machinery (mandatory fixes 3/4) is correctly implemented,
physically well-targeted, and passed with large, non-marginal margins.
P2/Gate P0/Gate P1/P5 are all sound as reported. NOTES.md's own decision
to not interpret the accelerating shape this cycle is the right call
under the R3 meta-rule.

The gaps are real and independently found, not restatements of Phase-2
concerns already fixed: (1) the P2/P3 headline metric, `kappa_window`
itself, has zero floor-gate check at any r, and the raw window/point
intensities needed to construct one after the fact were never persisted
(and, for the r=312 point channel, never even computed past a discarded
intermediate) — precisely at the scale carrying the more extreme half of
the "accelerating" claim; (2) P3b, a pre-registered, self-described
"genuinely new" falsifiable prediction bearing directly on T13, was
silently dropped between Phase 1 and the frozen Predictions/Result text,
even though its answer (B>0, right-direction) is sitting unstated in
`results.json`. Neither gap changes any scored verdict this cycle
reports, but both should be closed before the accelerating-collapse
finding is escalated or interpreted as physics.

## Ranked top-3 candidate directions for Iteration 83

**1. Floor-gate `kappa_window`/`window_stats()` directly, and re-run r=312
with the point-channel raw intensities persisted (not discarded), before
any interpretation of the accelerating shape proceeds.** This is a
sharper, concretely-specified version of NOTES.md's own Next item 1
(which names the floor/artifact question but not a mechanism to answer
it): apply `floor_gate()` to `win_e`/`win_a` at every r using this
program's own established `FLOOR_FRAC=0.10`-of-RMS convention, persist
`min`/`max`/`std` alongside `mean` for the window at every r, and stop
discarding `i_e_p`/`i_a_p` in the r=312 point-channel loop. Zero marginal
FDTD cost if r=312's field arrays are still available this shift;
otherwise one re-run of the already-inexpensive (1867.5s pilot) r=312
pair. This is the direct, load-bearing precondition for trusting or
refuting the accelerating-collapse finding at all.

**2. Score P3b explicitly, and report the implied global exponent
`n=log₂(shape_ratio)≈4.31` alongside the existing Model-A/B miss
percentages.** Zero marginal cost (pure post-processing of
already-captured `results.json` fields) — narrate `model_A_B`'s sign
against the pre-registered T13/T14 framing, and add the `shape_ratio≡2^n`
identity derived in §1 as a standing, reusable diagnostic for this exact
4:2:1 geometry family (useful at r=624/1248 or any future doubling in
this same bridge, not a one-off). This directly answers "how steep would
a single power law have to be" rather than only "does it miss the two
pre-registered candidates," and closes a real pre-registered-prediction
gap independently of the floor question in item 1.

**3. A fourth r-point (e.g. κ=2.83, r≈221, the geometric mean of 156/312)
to break the two-point degeneracy in the shape fit.** With only three
points beyond a two-parameter model, this cycle cannot distinguish "a
genuine, steeper-than-theory-predicts single power law (n≈4.3 throughout)"
from "a regime transition or measurement artifact specific to the
r=156→312 step." A genuine third *interval* (giving two independent
shape-ratio-style comparisons instead of one) would show whether the
local effective exponent keeps climbing (supporting either a real regime
change or a compounding artifact) or stabilizes near ~4.3 (supporting a
single, if unexpectedly steep, near-field law) — the single most direct
way to adjudicate the §1 finding with new data rather than desk analysis
alone. Should be built with floor-gating and settling machinery included
from the start (per item 1), not retrofitted after the fact.
