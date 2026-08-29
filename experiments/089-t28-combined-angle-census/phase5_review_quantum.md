# PHASE 5 — REVIEW · QUANTUM OPTICS · exp-089 · Panel Iteration 66→67

*Fresh context, blind to any other seat's current-cycle Phase-5 review. Read in
full: PANEL.md; LOGBOOK.md's RULED OUT (R1–R14, R14 in full — my own seat's
founding finding, adopted Iteration 65 from my own seat's Phase-5 self-review
of exp-088) and ESTABLISHED; LOGBOOK.md's T28 live-thread history (Iterations
58–65, both CHECKPOINT entries) through exp-088's close; the full exp-089
record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`); and
exp-088's own `phase5_review_quantum.md` for house-style calibration. All
numeric claims below were independently recomputed from
`experiments/083-.../results.json`, `experiments/087-.../results.json`,
`experiments/088-.../results.json` and `experiments/089-.../results.json`
primitives — not restated from any document's own prose (R4/R9 discipline).*

## Verdict: PARTIAL — the swing is real and correctly disclosed, but it is
## almost entirely an R13 (denominator) story wearing R14's (numerator's)
## clothes, and one sentence of `NOTES.md`'s own Result section is false

Q3's decisive miss (`ratio_k`=25.08/28.81 at 40.2°/41.4°, both formally
floor-clearing) is genuine, reproduces bit-exact from primitives, and
`NOTES.md` discloses it honestly rather than smoothing it over. R14(a)'s
smoothness gate correctly PASSES — `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` really
are smooth and monotonic across all 8 points, independently reconfirmed below —
and that PASS is not a false negative: this is not, in fact, the R14 numerator
hazard recurring. Decomposing `ratio_k`'s two operands (§2) shows the swing is
driven overwhelmingly by the DENOMINATOR (`frac_contrast`, an R13-class,
already-named hazard: both angles sit within one grid step of a `delta_scene`
zero-crossing, exactly as designed), not by any numerator anomaly. `NOTES.md`'s
own Q5/Learned-item-2 already reach the correct high-level diagnosis
(`FLOOR_FRAC=0.10` is not fully protective) — but Q6's prose, one paragraph
away in the same document, states these angles are "away from any
previously-known zero-crossing's immediate neighborhood," which is
demonstrably false and sits in tension with Q5's own correct framing (§3).
Not RULED OUT (no mechanism class touched — T1: N/A, as every T28 cycle since
exp-069) and not PROMISING (no constraint-metric progress claimed, correctly,
by this cycle's own scope).

## 1. Independent re-verification of `ratio_k`'s primitives at 40.2°/41.4°

Recomputed from scratch — `p_abs_w(C40,θ)`/`p_abs_w(G40,θ)` from
`results.json::thermo`, `frac_contrast` from `experiments/083-.../
results.json::per_theta` — not trusted from any table in the record:

| θ | `p_abs_w(C40)` | `p_abs_w(G40)` | `G40−C40` | `frac_p_abs` | `frac_contrast` | `ratio_k` |
|---|---|---|---|---|---|---|
| 40.2° | 3.077251×10⁻¹² | 3.055402×10⁻¹² | −2.185×10⁻¹⁴ | 7.100420×10⁻³ | 2.830881×10⁻⁴ | **25.0820** |
| 41.4° | 3.164949×10⁻¹² | 3.187843×10⁻¹² | +2.289×10⁻¹⁴ | 7.233392×10⁻³ | 2.510967×10⁻⁴ | **28.8072** |

Both reproduce bit-exact against `results.json::frac_p_abs`,
`::frac_contrast_new_angles`, `::ratio_k_new_angles`. No arithmetic,
indexing, or citation defect found.

**R14(a)'s smoothness gate, independently re-run over the full combined
8-point sorted set** (36.0°, 37.2°, 38.4°, 38.6°, 38.8°, 40.2°, 41.4°,
41.8°) — pulling `p_abs_w` from all three source files:

```
θ      p_abs_w(C40)     p_abs_w(G40)     step
36.0   2.748814e-12     2.754216e-12     —
37.2   2.812704e-12     2.808673e-12     UP / UP
38.4   2.925321e-12     2.929136e-12     UP / UP
38.6   2.941857e-12     2.953626e-12     UP / UP
38.8   2.955771e-12     2.973373e-12     UP / UP
40.2   3.077251e-12     3.055402e-12     UP / UP
41.4   3.164949e-12     3.187843e-12     UP / UP
41.8   3.234850e-12     3.258186e-12     UP / UP
```

**Both curves are strictly non-decreasing at every one of the 8 sampled
points, confirmed independently** — `NOTES.md`'s Result claim ("R14(a)
smoothness gate: PASS") reproduces exactly and is not overclaimed: it states
precisely what it checked (parent-curve monotonicity) and does not extend
that into a claim about `ratio_k` or `frac_p_abs`'s own behavior. Good
discipline, worth crediting explicitly since this exact seat's prior cycle
(exp-088) is the one that first drew the R4/R9 distinction between "checked"
and "restated."

## 2. Which term drives the swing — the task's central question, answered
## quantitatively

**The denominator. Not close.** Two counterfactual substitutions, both
computed directly from the primitives above, isolate each operand's
contribution:

**(a) Swap in a "typical" (non-near-node) denominator, keep the actual
measured numerator.** Averaging `frac_contrast` at the two nearest
CONSISTENT, non-crossing-adjacent points (38.8°: 1.5375×10⁻³; 41.8°:
1.2634×10⁻³) gives a "typical" magnitude of 1.4005×10⁻³ — still well inside
`delta_scene`'s own established oscillation envelope (peak-to-peak
magnitude ≈1.4–3.4×10⁻³ across the 36°–42° window, independently confirmed
from `exp-083/results.json::per_theta` below). Substituting this for the
actual (near-zero-crossing-suppressed) `frac_contrast`:

- 40.2°: `7.100×10⁻³ / 1.4005×10⁻³ = 5.07` — **CONSISTENT**, not
  ENERGY-DOMINANT (actual: 25.08).
- 41.4°: `7.233×10⁻³ / 1.4005×10⁻³ = 5.17` — **CONSISTENT** (actual: 28.81).

A single denominator swap, using magnitudes both angles' own immediate
non-node neighbors already show, collapses the "swing" by ~5× and lands
squarely back in the band the proposal's own naive interpolation
originally expected qualitatively.

**(b) Swap in the numerator's own "smooth-trend" desk estimate (Q4's own
pre-registered comparator, computed from the 38.8°→41.8° linear trend,
independently reproduced by every Phase-2 critique and Red Team's audit),
keep the actual measured denominator:**

- 40.2°: `6.5427×10⁻³ / 2.8309×10⁻⁴ = 23.11` vs. actual `25.08` — **7.9%
  difference**.
- 41.4°: `7.0463×10⁻³ / 2.5110×10⁻⁴ = 28.06` vs. actual `28.81` — **2.6%
  difference**.

Replacing the entire numerator with an independent, pre-committed
"smooth-continuation" estimate — the exact comparator `NOTES.md`'s own
Idealization 13 already flags as biased — moves `ratio_k` by under 8%. The
denominator swap moves it by ~80%. **The swing is >90% attributable to
`frac_contrast`, essentially 0% attributable to any anomaly in
`frac_p_abs`.**

This is not a coincidence of where these two points happen to sit — it is
their entire reason for existing in this cycle's own design. Confirming
directly from `exp-083/results.json::per_theta`, independent of anything
this cycle computed:

```
θ      delta_scene       frac_contrast
40.0  -6.899e-04        1.266e-03
40.2  -1.541e-04        2.831e-04   ← sampled point
40.4  +3.170e-04        5.832e-04   ← zero-crossing between here and 40.2
40.6  +6.582e-04        1.213e-03
...
41.2  +5.263e-04        9.819e-04
41.4  +1.337e-04        2.511e-04   ← sampled point
41.6  -3.055e-04        5.781e-04   ← zero-crossing between here and 41.4
```

`frac_contrast` at 40.2°/41.4° sits at the local trough of its own
established oscillation, by construction — both angles were chosen
(`phase1_proposal.md` §1: "the tightest-floor-margin grid neighbor of each
remaining zero-crossing") specifically for this property. Linear
interpolation places the true zero-crossings at 40.2654° (0.0654° from the
sampled point) and 41.4609° (0.0609° from the sampled point) — on a 0.2°
grid, this is the closest a sampled point could be without falling on the
opposite (thinner-margin, floor-failing) side.

**Conclusion for my own charter's lens**: nothing here requires positing
non-classical absorption or any mechanism outside the bench's existing
classical parameters. More specifically to this seat's own R14 finding:
this is **not** a recurrence of R14's numerator subtractive-cancellation
hazard — `frac_p_abs` at both angles tracks its own independently-computed
smooth extrapolation within single-digit percent, the opposite of what an
R14-hazard event would look like. It is a **sharper, quantified instance of
R13's own already-adopted hazard**: a ratio's denominator, near (but not
past) a real zero-crossing, can still dominate the ratio's value even after
formally clearing a floor gate — exactly the open question Q5 was
pre-registered to test, and exactly what it found (§4, below).

## 3. Self-skeptical check on `NOTES.md`'s own Result section — one claim is
## false, and it undercuts the document's own correct diagnosis two lines away

Per this seat's own standing discipline (my prior cycle's false "no fourth
instance exists" claim, caught by Red Team and logged as an R4/R9 registry
note): checked every unqualified interpretive claim in `NOTES.md`'s Result
and Learned sections against the primitives, not trusted from prose.

**Q5's language is sound and properly scoped.** "CONFIRMED — the gate is
not fully protective at this margin" restates exactly the pre-registered
CONFIRM signature (`any new angle reads >10 while floor-clearing`), which
both 40.2° and 41.4° literally satisfy — not an overclaim.

**Q6's language contains a claim that is false, independently checked
against the primitives above (§2), and self-contradicts Q5 one paragraph
earlier in the same document:**

> "This is a SECOND and THIRD floor-clearing, **non-artifactual**
> ENERGY-DOMINANT angle — not one isolated node (38.6°, already excluded by
> R13) but two more, **both away from any previously-known zero-crossing's
> immediate neighborhood**."

Both 40.2° and 41.4° sit 0.065° and 0.061° from a `delta_scene`
zero-crossing — the closest available grid point to that crossing, chosen
*for* that reason by this cycle's own Phase-1 rationale (§1's own
"tightest-floor-margin grid neighbor of each remaining zero-crossing," §4's
own margin table showing these as the two thinnest floor-gate margins ever
sent to FDTD besides 38.6° itself, 1.48× and 1.31×). Describing them as
"away from any... zero-crossing's immediate neighborhood" directly
contradicts the same document's own §4/Idealization-16 framing, and, per §2
above, is also *substantively* wrong: node proximity is what is actually
driving the reading. And it sits in tension with the very next sentence's
own correct diagnosis (Q5: `FLOOR_FRAC=0.10` "is not fully protective near
a zero-crossing") — Q6 calls the finding "non-artifactual" in the same
document where Q5 correctly attributes it to a floor-gate calibration gap
*at* a zero-crossing. Read charitably, "non-artifactual" may mean only
"not excluded by R13's own binary `floor_pass` classifier" (true, narrowly)
— but as written it reads as, and will very likely be cited as, "not
explicable by zero-crossing proximity," which §2 shows is the opposite of
the truth. This is exactly the shape of claim this sub-thread's own R4/R9
discipline exists to catch: an absence/negation claim ("away from...",
"non-artifactual") stated without a citation to the specific distance or
check that would support it — precisely the failure mode my own seat's
exp-088 Secondary Note fell into one cycle ago. **This was not caught by
either Phase-2 critique round or Red Team's audit because it did not exist
yet at that stage** — it is Result-section prose, written after Phase 4 ran,
with no further review layer before this Phase-5 pass. Recommend: correct
Q6's sentence to state the actual distances (0.065°/0.061° from the
respective zero-crossings, the closest available grid points) and drop or
qualify "non-artifactual" to the narrow R13-classifier sense only.

## 4. Answering the task's framing directly

**Is "smooth parents, wild ratio" even possible under R14(a) if the check
is doing its job?** Yes, straightforwardly — and this cycle is a clean,
non-contradictory illustration, not a counterexample. R14(a)'s minimum
discharge (LOGBOOK text, part (a)) verifies only that the numerator's own
two parent quantities are individually smooth — it says nothing about, and
was never designed to bound, the denominator. `ratio_k = frac_p_abs /
frac_contrast` can swing arbitrarily even with a perfectly smooth,
non-anomalous numerator, purely from denominator behavior — which is
exactly R13's own hazard, already named, already floor-gated (just not
tightly enough, per §2). R14(a) "did its job" correctly: it certified the
numerator is clean, and the numerator *is* clean (§1, §2b). The apparent
tension the task poses dissolves once the two operands are decomposed
separately rather than treated as one construction: **a smoothness check
on the two parent curves separately is not the wrong test for what it
claims to test (the numerator) — it is simply not a test of the
denominator at all, and was never claimed to be.** R13 already owns that
side, via `floor_pass`, and this cycle's real finding is that R13's own
threshold (`FLOOR_FRAC=0.10`) is calibrated too loosely to fully protect
against it — not that R14(a)'s check has a gap.

**Does this data demonstrate R14's construction fragility, or a hole in
R14(a)'s check?** Neither, on the numbers. It demonstrates R13's own
open question (Q5, already correctly identified by this cycle) more
sharply than any prior T28 cycle has: a `floor_pass=True` point at
1.31–1.48× margin can still produce a `ratio_k` an order of magnitude past
`RATIO_HIGH`, driven almost entirely by the denominator continuing to
shrink toward its own zero inside the "cleared" region. That is a genuine,
independently quantified (§2) instrument-calibration finding — but it
belongs to R13's file, not R14's, and `NOTES.md` should say so without the
Q6 language that muddies which of the two named hazards is actually in
play.

## Sharpest finding

Two counterfactual primitive substitutions (§2) show `ratio_k`'s 25–29×
swing at 40.2°/41.4° is **>90% attributable to `frac_contrast`** (denominator,
R13's hazard — swapping in a typical non-node-adjacent magnitude alone
collapses both readings to `ratio_k≈5.1–5.2`, squarely CONSISTENT) and
**under 8% attributable to `frac_p_abs`** (numerator, R14's hazard — it
tracks its own independently pre-registered smooth-trend estimate within
2.6–7.9%). R14(a)'s PASS is therefore correct, not a false negative — this
cycle is not a numerator-hazard recurrence. But `NOTES.md`'s own Result
section (Q6) states these two angles are "away from any previously-known
zero-crossing's immediate neighborhood" and calls the reading
"non-artifactual" — both angles sit 0.061–0.065° from a real
`delta_scene` zero-crossing (the closest available grid point, chosen
*for* that reason by this cycle's own Phase-1 design), and the claim
directly conflicts with Q5's own correct diagnosis one paragraph away
(`FLOOR_FRAC` "not fully protective near a zero-crossing"). This is a
false, uncited absence-claim in the frozen Result record — the same shape
this seat's own prior-cycle mistake was caught making — and it points
future readers toward the wrong hazard (R14) instead of the right one
(R13's own floor-margin calibration).

## Ranked top-3 for the Director's Iteration-67 queue

1. **[Tier 0, zero-FDTD, immediate]** Correct `NOTES.md`'s Q6 sentence: (a)
   the "away from any... zero-crossing's immediate neighborhood" claim is
   false — both angles sit 0.061–0.065° from a real crossing, the closest
   available grid point, by the cycle's own design; (b) file this review's
   §2 decomposition (`ratio_k`'s swing is >90% denominator-driven, <8%
   numerator-driven, both counterfactuals reproducible from already-
   committed primitives at zero new cost) as the citable record correcting
   which named hazard (R13, not R14) this cycle's own headline finding
   belongs to. Cheapest, most decisive, most directly load-bearing item
   this review produced — a future citation of exp-089 should not read
   "two new non-artifactual ENERGY-DOMINANT points" without this context.
2. **[Tier 1, cheap FDTD]** Recalibrate `FLOOR_FRAC` empirically using this
   cycle's own now-larger sample (`NOTES.md`'s own Next-item-2, already
   named): both misses sit at 1.31×/1.48× margin, comfortably inside the
   current 1.0× pass line — determine, from the combined 8-point set, what
   `FLOOR_FRAC` value (or graduated caution zone) would correctly exclude
   40.2°/41.4° as unresolved-by-construction while still passing the
   genuinely CONSISTENT points (36.0°, 37.2°, 38.4°, 38.8°, 41.8°) — this
   is now the single most load-bearing open instrument question on the
   whole T28 `ratio_k` channel.
3. **[Tier 1, cheap FDTD]** A tight bracket at 40.2°/41.4° (mirroring
   exp-088's own 38.6° bracket design, ±0.2°), explicitly framed as a test
   of THIS review's own §2 prediction: if the swing is denominator-driven
   as shown, `ratio_k` should track `1/frac_contrast(θ)` closely across the
   bracket (rising toward the true crossing, falling away from it) with
   `frac_p_abs(θ)` continuing its own smooth trend throughout — a
   falsifiable, cheap discriminator between "this review's decomposition is
   right" and "there is a second, still-hidden effect" before the Director
   commits to recalibrating `FLOOR_FRAC` on item 2 above.
