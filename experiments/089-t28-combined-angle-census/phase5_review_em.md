# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-089 · Panel Iteration 66

*Fresh context. Read in full: PANEL.md; LOGBOOK.md's RULED OUT (R1–R14) and
ESTABLISHED sections; LIVE THREADS/T28 (Iterations 58–65, both CHECKPOINT
entries); `phase1_proposal.md`, all five Phase-2 critiques (including my own
`phase2_critique_em.md`), `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `results.json`, `run.py` — this cycle's complete record; and
exp-088's `phase5_review_em.md` for house-style calibration. All numbers
below independently recomputed from `results.json`/`experiments/083-.../
results.json` primitives with a standalone script, not restated from
NOTES.md's own prose (R4/R9 discipline).*

## Verdict

**CONCUR with the filed result — Q1/Q2/Q3/Q5/Q6/Q7/R14(a) all reproduce
exactly, and no sign, registration, or passivity/energy-conservation defect
exists anywhere in these 12 cells.** The 25–29× `ratio_k` spike at
40.2°/41.4° is real, resolved, gate-clean measured data, not a bookkeeping
artifact — but the record as filed does not yet say *why* it is real in the
precise way the data itself supports, and my own Phase-2 concern about
R14(c)'s borrowed yardstick is only partially resolved, not settled, by
what this cycle measured. Three genuinely new findings below, none raised
by any Phase-2 critique or NOTES.md: (1) the raw signed numerator
`p_abs(G40,θ)−p_abs(C40,θ)` — not just its magnitude — flips sign four
times across the now-8-point combined set, at intervals whose coarse
timing is broadly consistent with half of T28's established ~2.84–2.95°
period, arguing for a genuine oscillatory EM origin over a bookkeeping
bias; (2) `frac_p_abs` at 40.2°/41.4° is essentially *on*-trend against a
local linear interpolation (+8.5%/+2.6%), unlike 38.4°'s ~68% dip — the
25–29× spike is mechanistically an R13 (denominator-near-zero) effect
riding on an unremarkable numerator, not a second instance of 38.4°'s own
R14 numerator anomaly, and NOTES.md's Learned section does not currently
draw this distinction; (3) `run.py`'s R14(a) smoothness gate does not
implement what Idealization 11/NOTES.md claims — it applies a flat 2%-of-
`v_prev` tolerance to every step, never the per-point `box_dev` this
cycle's own new angles have on hand — non-blocking here (every step passes
by a wide margin regardless) but a real prose/code mismatch.

## 1. Independent recomputation

**`xi_ext` (P4 gate), 3 of 12 cells recomputed from `widths` primitives,
all bit-exact:**

| Cell | recomputed `xi_ext` | filed | match |
|---|---|---|---|
| `C40_40.2_BOX_A` | 2.1448116976585476×10⁻⁴ | same | exact |
| `C40_41.4_BOX_B` | 6.598371138698003×10⁻⁵ | same | exact |
| `G40_37.2_BOX_A` | 2.132952344104603×10⁻⁴ | same | exact |

All three (and, by the same formula applied by eye to the rest of the
`widths` block, the remaining 9) sit two to three orders of magnitude
inside `XI_TOL=0.12` — the extinction-routes-agreement gate is not merely
passing, it is passing by a wide margin everywhere. **The extinction
identity `σ_scat+σ_abs=σ_ext` holds to machine precision at every cell I
checked** (e.g. `C40_40.2_BOX_A`: `155.10095203648922+163.16241122961705
=318.26336326610624`, exact to the last printed digit) — basic energy
bookkeeping is intact, not merely gated.

**Passivity bound.** `ratio_abs_ext_raw = σ_abs/σ_ext` at all 12 cells sits
in `[0.5126, 0.5151]` (`results.json::ratio_abs_ext_new_angles`) —
comfortably inside the required `[0,1]` and within 0.5–1.0% of T9's
established 0.51 broadside anchor, matching exp-087/088's own range. No
cell approaches either boundary.

**`i_inc`/sign hygiene.** `i_inc` is positive, smooth, and monotonically
increasing with θ at every one of the 12 cells (`C40`: 0.3228→0.3409;
`G40`: 0.3247→0.3398), `direction_correction_sign_applied=-1.0` uniformly
— the identical pattern my own exp-088 Phase-5 review found at that
cycle's 8 new cells. No near-zero `i_inc`, no branch flip, no third
instance of the exp-024/exp-087 sign hazard.

**`ratio_k` and `FLOOR`, full re-derivation from `experiments/083-.../
results.json::per_theta`** (independent of `run.py`, `dg069`, or any
cited intermediate): `frac_contrast(θ)=|delta_scene|/|C40_C|` at
37.2°/40.2°/41.4° reproduces to `4.16265545×10⁻⁴`/`2.83088125×10⁻⁴`/
`2.51096742×10⁻⁴` exactly; `FLOOR=0.10×RMS` over the full 31-point window
reproduces to `1.91744×10⁻⁴` exactly; `ratio_k=frac_p_abs/frac_contrast`
reproduces to `3.443295`/`25.082014`/`28.807194` exactly. The
resolved-margin figures NOTES.md cites (1.046×/2.087×/4.685×, computed as
`|Δp_abs|/(NOISE_MULT×box_dev_max×p_abs(C40))`) also reproduce exactly
from raw `widths`/`box_dev` fields. **No arithmetic defect anywhere in
this cycle's own record** — consistent with all five Phase-2 critiques'
and Red Team's own findings.

## 2. Is the 25–29× swing genuine passive-scattering physics, or a
construction artifact of the ratio itself?

This is the question my seat was asked to settle from the data, and the
data gives a real, if partial, answer.

**First: separate the two spike angles from 38.4°'s own dip mechanistically.**
I computed the local linear-interpolation trend for `frac_p_abs` at 40.2°
and 41.4° the same way NOTES.md's own Q4 section does (between the
nearest already-filed flanking points, 38.8° and 41.8°): trend(40.2°)
`=5.955×10⁻³+0.4667×(7.214×10⁻³−5.955×10⁻³)=6.543×10⁻³` vs. measured
`7.100×10⁻³` (**+8.5%** over trend); trend(41.4°)`=7.046×10⁻³` vs.
measured `7.233×10⁻³` (**+2.6%** over trend). Compare 38.4°'s own
documented deviation from the *equivalent* trend construction: **−68%**
(QUANTUM's/Red Team's own Phase-2 figure, `1.3041×10⁻³` actual vs.
`4.1373×10⁻³` wide-trend-predicted). **The numerator is behaving
unremarkably at both spike angles — it is the R13-flagged denominator,
sitting at 1.31–1.48× FLOOR next to a genuine `delta_scene` zero-crossing,
that is doing essentially all of the work.** This is a materially
different mechanism from 38.4°'s own R14 numerator anomaly, and NOTES.md's
Learned §1 ("whatever T28's energy-interception channel is actually doing,
it is not confined to one node's immediate neighborhood") reads as though
both new spikes are instances of the same open mystery as 38.4°'s dip.
They are not, on this data: **38.4° is an R14 (numerator) event; 40.2°/
41.4° are R13 (denominator) events, compounding, not duplicating, each
other.** This should be stated explicitly in any Phase-3-equivalent
correction or forward citation.

**Second: is the underlying numerator itself a genuine oscillatory EM
quantity, or a systematic bias?** I built the full 8-point combined
`p_abs_w(G40,θ)−p_abs_w(C40,θ)` signed-difference series (pulling
`thermo::p_abs_w` from this cycle plus exp-087's 36.0°/38.6°/41.8° and
exp-088's 38.4°/38.8°, all bit-exact against their own committed JSON):

| θ | `p_abs(G40)−p_abs(C40)` | sign |
|---|---|---|
| 36.0° | +5.403×10⁻¹⁵ | + |
| 37.2° | **−4.032×10⁻¹⁵** | **−** |
| 38.4° | +3.815×10⁻¹⁵ | + |
| 38.6° | +1.177×10⁻¹⁴ | + |
| 38.8° | +1.760×10⁻¹⁴ | + |
| 40.2° | **−2.185×10⁻¹⁴** | **−** |
| 41.4° | +2.289×10⁻¹⁴ | + |
| 41.8° | +2.334×10⁻¹⁴ | + |

**This is a new observation — no Phase-2 critique or NOTES.md checked the
sign of the raw (non-absolute-valued) numerator across the combined
8-point set.** My own exp-088 Phase-5 review checked exactly this for the
5 points then available and found *zero* sign flips (uniformly positive).
Adding this cycle's 3 points changes that picture: **the signed difference
now flips sign four times** (36.0°→37.2°, 37.2°→38.4°, 38.8°→40.2°,
40.2°→41.4°). Every one of these differences is individually `resolved`
(above its own noise floor — `resolved_new_angles` all `true` for this
cycle's points; exp-087/088's own retroactive reclassification shows the
same for 36.0°/38.4°/38.8°/41.8°), so this is not noise scatter around
zero — it is a real, measured, alternating-sign signal.

Linearly interpolating the four zero-crossings: **36.687°, 37.817°,
39.425°, 40.786°** — successive gaps **1.13°, 1.61°, 1.36°** (mean
1.37°), sitting close to, though not tightly inside, the `[1.42°,1.475°]`
half-period band R14(c) borrows from `delta_scene`'s established period.
**A systematic bookkeeping or registration bias (e.g. a fixed coordinate
offset between the `C40`/`G40` configs) would be expected to produce a
consistent-sign difference, not one that flips sign on a length scale
loosely tracking this exact config pair's own already-established
interference period.** Combined with §1's clean sign/passivity bookkeeping,
this is real evidence favoring "genuine coherent interference riding on a
smooth common-mode baseline" — exactly the mechanism THERMODYNAMICS'/
PHOTONICS'/QUANTUM's three complementary R14 explanatory layers already
argued for the 38.4° dip — over any construction-artifact reading, for
*this* aspect of the finding.

**But this does not fully vindicate a single-tone reading, and does not
fully discharge my own Phase-2 attack.** I checked whether a single pure
sinusoid at the established period (crossing at 37.817°, `P=2.9°`)
predicts the *amplitude* growth from 38.4°→38.6°→38.8° — the segment
whose 3.07×/0.2° jump my own Phase-2 critique flagged as evidence of a
possibly much narrower native scale. A pure single-tone model near a
zero-crossing predicts *slowing* growth as phase advances toward
90° (`sin(72.4°)=0.953→sin(97.2°)=0.992`, a 4% step); the data shows a
**3.09× step** over the identical interval. **A naive single ~2.9° tone
does not explain this local segment's curvature** — something with more
structure than one fundamental (a second harmonic, an amplitude-modulated
envelope, or a genuinely narrower co-located feature) is still a live
possibility there specifically, even though the coarse crossing-timing
across the full 5.8° span is period-plausible. **This is not itself a
period claim** — no null-permutation control was run against it (R5/R10
still applies, and this cycle explicitly, correctly, declined to run a
formal fit) — it is a raw, disclosed, from-primitives observation that
sharpens rather than resolves the open question, and belongs directly in
front of the still-queued R14(b) formal fit (Idealization 14), which
should test for structure beyond a single tone, not only fit one.

**Bottom line on the assigned question:** on the evidence available, the
25–29× swing is *not* a construction/bookkeeping artifact — the sign,
extinction-identity, and passivity checks are all clean, and the
underlying signed numerator behaves like a genuine, resolved, coherent
EM interference term riding on a smooth baseline, with crossing-timing
loosely consistent with this config pair's own established period. But
the swing's *magnitude* is overwhelmingly an R13 phenomenon (a smooth,
on-trend numerator divided by a near-zero, genuinely oscillatory
denominator), not a fresh R14 numerator spike — and the numerator's own
internal structure (the 38.4°→38.8° amplitude ramp specifically) is not
yet explained by any model tested to date, single-tone included.

## 3. Is R14(a)'s smoothness gate itself electromagnetically informative?

**Yes, and it says something sharper than "gate passed."** I recomputed
the per-step percentage change in both parent curves directly:

`p_abs(C40,θ)` steps: +2.32%, +4.00%, +0.57%, +0.47%, +4.11%, +2.85%,
+2.21% (36.0°→41.8°, 7 steps). `p_abs(G40,θ)`: +1.98%, +4.29%, +0.84%,
+0.67%, +2.76%, +4.34%, +2.21%. **Every single step, both curves, is
positive — R14(a) passes with zero steps requiring its own tolerance at
all**, not a narrow tolerance-assisted pass. This is genuinely consistent
with ordinary passive scattering: absorption cross-section rising smoothly
with incidence angle at a fixed, lossy article is the expected behavior
with no exotic assumption needed, and it is not in tension with anything
`delta_scene` has independently shown about this config pair.

**Smooth-parents-but-wild-signed-difference is exactly what §2 shows is
happening, and it makes complete physical sense — this is not a paradox
requiring new physics.** The two parent curves track each other to within
~0.1–0.7% of each other's own magnitude at every angle (e.g. at 40.2°,
`C40=3.0773×10⁻¹²` vs `G40=3.0554×10⁻¹²`, a 0.71% gap). A ~0.1–0.7%-scale
coherent modulation superimposed on a common ~2–4%-per-step rising
baseline is exactly R14's own founding logic: **individually smooth,
strictly monotone parent curves place no constraint whatsoever on the
smoothness of their small residual difference**, because monotonicity is
a statement about the *dominant* (common-mode) term, while the
oscillation lives entirely in the *sub-percent residual* the two curves
don't share. R14(a) passing, here, is not evidence against a real
sub-feature in `frac_p_abs` — it actively predicts one is *possible*
without ruling out its presence, which is precisely what §2 finds. **This
confirms — does not merely "not contradict" — the subtractive-cancellation
fragility QUANTUM named at exp-088's own R14 founding instance, now with
a second independent instance (this cycle's own 4-fold sign alternation)
rather than a lucky/unlucky one-off.**

## 4. R14(c) revisited, given this cycle's own new data

My own Phase-2 sharpest attack argued the ~2.84–2.95° `delta_scene` period
is the wrong yardstick for `frac_p_abs`'s own gaps, because the only prior
direct evidence (38.4°→38.6°, a 3.07×/0.2° jump) suggested a much narrower
native scale. §2 above partially walks this back and partially sustains
it: the *coarse* crossing-spacing of the newly-visible 4-fold sign
alternation (mean 1.37°, vs. the borrowed half-period band
`[1.42°,1.475°]`) is close enough that a single ~2.9° tone is at least
plausible as *a* component of `frac_p_abs`'s own structure — my original
framing ("an entirely different, much narrower native scale") over-stated
the mismatch. But the 38.4°→38.8° amplitude ramp's failure to fit that
same single-tone model (§2) means R14(c)'s implicit assumption — that
clearing half of `delta_scene`'s period guarantees no missed
sub-feature — is still not established, just for a more precise reason
than my Phase-2 critique originally gave: not "wrong period entirely,"
but "possibly right fundamental, with unmodeled additional structure
riding on it." **Net: my own attack is downgraded from likely to
unresolved-but-narrowed** — exactly the kind of thing the still-queued
R14(b) fit (Idealization 14) needs to settle, this time informed by both
the crossing-timing evidence (§2) and the amplitude-ramp mismatch (§2).

## 5. Other findings

- **`run.py`'s R14(a) gate does not implement what NOTES.md's Idealization
  11 describes.** Idealization 11 states the check runs "within each
  point's own `box_dev` noise floor." The actual code
  (`run.py` lines ~373–380) applies `tol = NOISE_MULT * 0.02 * v_prev` —
  a flat 2%-of-previous-value proxy — to *every* step, including this
  cycle's own 3 new angles, where the genuine per-point `box_dev` is
  already computed and available in the same script (`box_dev[(key, th)]`,
  used elsewhere for Q3's own resolved-margin test). The code comment
  ("conservative fallback box_dev proxy for filed-only points") signals
  the intent was to use real `box_dev` where available and fall back only
  for the 5 filed-only points — but the implementation never branches;
  it always uses the flat proxy. **Non-blocking this cycle**: I confirmed
  directly (§3) that every step passes by 10×–30× margin under *either*
  tolerance (the flat 2% proxy or a tight, `box_dev`-derived one, e.g.
  `C40` 37.2°→38.4°: actual step `1.126×10⁻¹³` vs. a `box_dev`-derived
  tolerance of `~3.7×10⁻¹⁵` — the gate would still PASS). But this is a
  genuine prose/code mismatch in an R4/R9-relevant "verification gate,"
  the second such self-check defect this cycle discloses on top of
  NOTES.md's own honestly-flagged Idealization-15 bug — worth a Phase-3-
  equivalent correction so a future cycle with a genuinely borderline step
  does not silently rely on the looser tolerance while believing the
  tighter, documented one is in force.
- **Fix-docket compliance, independently spot-checked**: the dual-section
  banner (fix item 1) is present verbatim at both the Predictions and
  Result sections of NOTES.md; the false superlative (item 2) is corrected
  and properly scoped to floor-*clearing* comparisons; the 1.4° gap caveat
  (item 3) is stated inline at Idealization 12, not buried; Q4 reports raw
  numbers only, no CONFIRM/REFUTE label (item 4); the NETD/T9 extension
  (item 5) ran and is UNDETECTABLE at all 6 cells, `ratio_abs_ext` within
  1% of the T9 anchor at all 6, matching Q7's prediction exactly. No
  regression found on any of the nine adopted fixes.
- **T9 anchor**, now confirmed a further 6 cells (14 cumulative across
  exp-087/088/089): `ratio_abs_ext` stays inside 0.51–0.52 at oblique
  incidence with no outlier, continuing to sit nowhere near the idealized
  `≤0.5` geometric-optics ceiling in a way that would reopen that ESTABLISHED
  caveat.

## Sharpest finding

**The raw signed numerator `p_abs(G40,θ)−p_abs(C40,θ)` — not merely its
magnitude — flips sign four times across the newly-completed 8-point
combined set (at 37.2°, 40.2°, points my own exp-088 Phase-5 review never
had), with crossing-to-crossing spacing (mean 1.37°, range 1.13°–1.61°)
loosely tracking half of T28's own established ~2.84–2.95° period. This is
the single strongest piece of evidence in this cycle's own record against
a bookkeeping/construction-artifact reading of the numerator: a systematic
registration or sign bias would be expected to hold one consistent sign,
not alternate on a length scale approximately matching this exact config
pair's own already-established interference period. At the same time, a
naive single-tone check at that same period fails to explain the
38.4°→38.6°→38.8° amplitude ramp by a wide margin (predicts a ~4% step,
observes 3.09×) — so this is evidence for *genuine, structured* EM
physics in the numerator, not evidence that a simple period fit will
close the question. Separately and more decisively for the specific
25–29× spike values: `frac_p_abs` itself is essentially on-trend
(+2.6%/+8.5%) at both 40.2° and 41.4°, unlike 38.4°'s ~68% dip — meaning
this cycle's own headline ENERGY-DOMINANT result is mechanistically an
R13 (denominator-near-zero) finding, not a second R14 (numerator-anomaly)
finding, a distinction the filed record does not currently draw.

## Ranked top-3 for Iteration 67

1. **Run the still-queued R14(b) formal, null-controlled fit against the
   raw signed difference `p_abs(G40,θ)−p_abs(C40,θ)`** (Red Team's
   Iteration-65 Tier-2 item, Idealization 14 here) — now with a
   materially stronger case than when it was first queued: §2's 4-fold
   sign alternation at roughly period-consistent spacing, and its
   simultaneous failure to fit a naive single-tone amplitude model near
   38.4°–38.8°. The fit should explicitly test single-tone vs.
   two-component (fundamental + higher-harmonic/envelope) models against
   this signed series, under full R5/R10 circular-shift-null discipline —
   not a repeat of exp-083's own reversed `delta_scene` two-tone claim
   (a different quantity, never tested this way), but a genuinely new
   question this cycle's own data motivates for the first time.
2. **Separate the R13 (denominator) and R14 (numerator) diagnosis
   explicitly in the record before any further densification is
   proposed.** NOTES.md's own "Next" section frames 40.2°/41.4° as an
   open "isolated spike vs. broader elevated region" question mirroring
   38.4°'s own shape; §2 shows this conflates two mechanistically distinct
   findings. A future densification bracket at 40.2°/41.4° should target
   the *denominator's* local curvature (finer-than-0.2° sampling of
   `delta_scene` near its own two zero-crossings) as the actual
   discriminating measurement, not `frac_p_abs` itself, which this
   cycle's own data shows is behaving unremarkably there.
3. **Fix `run.py`'s R14(a) gate to use each point's own measured
   `box_dev`-derived tolerance, as Idealization 11 already claims it
   does**, rather than the flat 2%-of-`v_prev` proxy actually implemented
   (§5) — cheap, zero marginal FDTD cost, and closes a genuine prose/code
   mismatch before a future cycle relies on the gate at a step thin enough
   for the two tolerances to disagree.
