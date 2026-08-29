# PHASE 5 — REVIEW · QUANTUM OPTICS · exp-088 · Panel Iteration 65→66

*Fresh context. No memory of the agent who drafted this cycle's Phase 1
proposal under the same seat label — reviewed with the same fresh eyes as
any other seat's work. Read in full: LOGBOOK.md's RULED OUT (R1–R13) and
LIVE THREADS/T28 through Iteration 64/exp-087; PANEL.md; the complete
exp-088 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`results.json`). All numeric claims below were independently recomputed
from `experiments/083-.../results.json`, `experiments/087-.../results.json`
and `experiments/088-.../results.json` primitives — not restated from any
document's own prose (R4/R9 discipline).*

## Verdict: PARTIAL, with a genuinely new finding this cycle's own review
docket did not surface

This cycle did exactly what it set out to do — cheaply, honestly, gate-
disciplined — and its own Phase-5-visible "surprise" (`ratio_k(38.4°)
=0.908`, missing its own `[1.5,5.0]` predicted band) is real and correctly
disclosed, not smoothed over. But independent decomposition of the
PRIMARY metric's numerator (below) shows the miss did not require any new
physics, non-classical or otherwise, to produce — and shows a structural
hazard in `ratio_k`'s own construction that R13, as adopted, does not yet
cover. Not RULED OUT (nothing here forecloses a mechanism class — this is
still T28 instrument work, T1 route N/A) and not a clean CONFIRM of Q4 as
filed.

## 1. Independent re-verification of `ratio_k`/`frac_p_abs` from primitives

Recomputed from scratch, not trusted from any table in the record:

- `RMS[frac_contrast(θ)]` over exp-083's 31-point window:
  `1.9174375118374476×10⁻³` → `FLOOR=1.91744×10⁻⁴`. Matches every cited
  figure exactly.
- `delta_scene(θ)` zero-crossings by linear interpolation between adjacent
  grid points: **37.127°, 38.590°, 40.265°, 41.461°** — matches
  PHOTONICS'/Red Team's own figures exactly, four crossings confirmed, not
  three.
- All five floor-gate margins reproduce to full precision: 36.0°=3.879×,
  38.6°=0.386× (fails), 41.8°=6.589×, 38.4°=7.495×, 38.8°=8.019×, plus the
  two un-bracketed near-node points 40.2°=1.476×, 41.4°=1.310× — all
  exactly as filed.
- `frac_p_abs(38.4°)=1.30414×10⁻³`, `frac_contrast(38.4°)=1.43705×10⁻³`,
  `ratio_k(38.4°)=0.90751` — reproduces bit-exact from
  `results.json::thermo` (`p_abs_w` for C40/G40 at 38.4°) through the
  literal `frac_p_abs = |p_g40−p_c40|/p_c40` and `ratio_k = frac_p_abs /
  frac_contrast` formulas in `run.py`. Same for 38.8°
  (`ratio_k=3.87325`). No arithmetic, indexing, or citation defect found
  anywhere in this cycle's PRIMARY metric.

## 2. Is the 38.4° non-monotonicity a real anomaly, or unsurprising given what `ratio_k` measures?

**Unsurprising — and the reason is a structural hazard in `ratio_k`'s
numerator that nobody in this cycle's review chain looked for, because
R13's own text only names the denominator.**

I decomposed `frac_p_abs(θ) = |p_abs_w(G40,θ) − p_abs_w(C40,θ)| /
p_abs_w(C40,θ)` into its two raw operands across all five now-measured
angles (exp-087 + exp-088 combined):

| θ | `p_abs_w(C40)` | `p_abs_w(G40)` | `G40−C40` | `frac_p_abs` |
|---|---|---|---|---|
| 36.0° | 2.7488×10⁻¹² | 2.7542×10⁻¹² | 5.403×10⁻¹⁵ | 1.965×10⁻³ |
| 38.4° | 2.9253×10⁻¹² | 2.9291×10⁻¹² | **3.815×10⁻¹⁵** | **1.304×10⁻³** |
| 38.6° | 2.9419×10⁻¹² | 2.9536×10⁻¹² | 1.177×10⁻¹⁴ | 4.001×10⁻³ |
| 38.8° | 2.9558×10⁻¹² | 2.9734×10⁻¹² | 1.760×10⁻¹⁴ | 5.955×10⁻³ |
| 41.8° | 3.2349×10⁻¹² | 3.2582×10⁻¹² | 2.334×10⁻¹⁴ | 7.214×10⁻³ |

**Both individual absorbed-power curves — `p_abs_w(C40,θ)` and
`p_abs_w(G40,θ)` — are smooth and strictly monotonically increasing
across all five sampled angles, with no anomaly whatsoever.** The entire
"dip" lives in the *difference* `G40−C40`, which is itself non-monotonic:
it *falls* from `5.40×10⁻¹⁵` (36.0°) to `3.82×10⁻¹⁵` (38.4°) before rising
steeply and monotonically through 38.6°→38.8°→41.8°. `frac_p_abs` — the
"bulk energy quantity" half of `ratio_k`, in the framing this review was
asked to test — is architecturally *not* a bulk quantity at all: it is a
**small difference between two nearly-equal, independently smooth
quantities, divided by one of them.** That is exactly the mathematical
shape (a fraction whose small-magnitude component is itself
sign-sensitive/oscillation-prone) that R13 already identified as
dangerous for `frac_contrast`/`delta_scene` — just on the other side of
the ratio. Two smooth, boring, monotonic curves are entirely sufficient
to produce a non-monotonic *difference* between them, with no new
physics, resonance, or coherent effect required.

This has a concrete physical grounding, not just a numerological one:
`C40` (`ABSORB=40, PAD=0`) and `G40` (`ABSORB=40, PAD=40`,
`design_geometry.py`) differ *only* in the presence of the far-boundary
PAD — the identical geometric feature already established (T28's whole
periodicity, `P_edge_A≈2.84°`) as the physical driver of the
oscillatory edge-diffraction structure imprinted on `delta_scene`. It
would be more surprising if the PAD's own differential effect on absorbed
power did *not* carry some comparable-order oscillatory component from
the same diffractive mechanism, superimposed on both curves' otherwise
smooth θ-trend, than if it did. The 36.0°→38.4° gap this cycle's own
linear-interpolation anchor spans is `2.4°≈0.81–0.84` T28 periods — almost
exactly enough room for one such local minimum to appear between two
sample points and be missed entirely by a two-point linear model.

**Conclusion for my own charter's lens**: nothing here requires positing
non-classical absorption, a state-dependent cross-section, or any
mechanism outside the bench's existing classical parameters (σ, ε(ω),
diffraction geometry already in play). The "surprise" is a construction
artifact of dividing a difference of two close, smooth numbers — expected
once you look at what `frac_p_abs` is actually built from, not evidence
of new physics on the absorbed-power channel. This does **not**, however,
mean the number is wrong or the finding is void — a genuine narrow
differential feature at the PAD-diffraction scale is real, disclosed
correctly by NOTES.md, and worth resolving (§4).

## 3. Was Q4's linear-interpolation prediction method deserving of its confidence?

**No — in hindsight the ±20% band was undersized by a wide margin, and
the gap that caused it was named, in writing, by this cycle's own
Phase-2 process, but never actually fixed.**

Concretely: Q4 interpolated `frac_p_abs` linearly between 36.0° and
41.8° — a 5.8° span, ≈2.0 T28-established periods (`2.8421°–2.9474°`) —
calibrated its ±20% band against exactly *one* interior check (the 38.6°
point, which the same linear model missed by 7.9%), and produced a band
(`[1.5,5.0]` at 38.4°) that the real measurement (`0.908`) missed by
**39% below the band's own lower edge**, and by **68% below the raw
linear-interpolation central estimate** — nowhere close to a ±20%
tolerance, however widened.

This was not an unforeseeable failure. PHOTONICS' own Phase-2 critique
named the exact mechanism, verbatim: *"Q4's linear-trend prediction for
`frac_p_abs` spans 5.8° (≈2 periods of this same established
oscillation) and is corroborated by exactly one interior point (38.6°,
7.9% miss) — no argument is offered for why `frac_p_abs`, unlike its
sibling `frac_contrast`, should be smooth here."* That sentence is a
correct, prospective diagnosis of precisely the failure mode this
cycle's own Result section later disclosed. EM's independent Phase-2
critique raised the structurally identical gap elsewhere in the same
document (the bracket-width claim never invoking T28's own periodicity
as a smoothness bound) — two seats, independently, flagged "no physical
argument for smoothness was ever offered against a known periodic
structure" as a live defect in this proposal, in two different places.

**What went wrong in the review chain, not just the prediction**: neither
critique's own proposed remedy asked for Q4's numeric band itself to be
revisited. PHOTONICS' flip-parameter asked only for disclosure (tighter
floor-gate margins at 40.2°/41.4°) and language-narrowing (Q5's scope).
Red Team's audit (§1) explicitly rated PHOTONICS' fix "necessary...but
not sufficient" for "the underlying representativeness gap" — one more
step than PHOTONICS took — and yet still redirected the remedy toward a
forward-tripwire *sampling* item (§6.2/Fix 4), never toward tightening,
re-deriving, or flagging Q4's own already-frozen `[1.5,5.0]`/`[1.5,5.5]`
bands as under-justified on the identical smoothness-argument grounds
already established as valid in the very same audit. Phase 3 adopted all
10 fix-docket items faithfully — but none of the 10 touches Q4's own
predicted numbers. The diagnosis was made, twice, in writing, before any
FDTD ran; the cure was never applied to the specific falsifiable claim it
undermined. This is a genuine process gap, not merely bad luck in a
committed prediction — and since this seat led the original Phase-1
proposal that set the ±20% band in the first place, the self-critical
reading is that my own seat's originating draft under-argued the
smoothness assumption from the start, and neither of the two seats that
correctly spotted it (PHOTONICS, EM) pushed the fix far enough to reach
the number itself.

## 4. A concrete, well-scoped next test for the 38.4° dip

Two complementary items, both cheaper than the still-open 3-angle
forward-tripwire (12 calls: ≈37.1–37.2°, 40.2°, 41.4°):

**(a) Zero-FDTD, immediate.** File the decomposition in §2 above
(individual `p_abs_w(C40,θ)`/`p_abs_w(G40,θ)` are smooth/monotonic; the
non-monotonicity lives entirely in their difference) as a named,
citable finding — it costs nothing (both values already sit in committed
`results.json` files across exp-087+exp-088) and directly answers half of
MATERIALS' still-queued "passive transducer, not resonant source" test
(Red Team's Iteration-65 ranking item 2) at the 5 already-measured
angles, without any of that item's 124-call cost. Recommend also flagging
this as a candidate **R13 addendum**: R13's text floor-gates a ratio's
*denominator* when it derives from a quantity with known/knowable real
zero-crossings; this finding shows `ratio_k`'s own *numerator*
(`frac_p_abs`) is a structurally identical small-difference-over-base
construction and deserves the same scrutiny before any future cycle
trusts a single-point reading of it near a suspected feature.

**(b) Low-cost FDTD, ≈4–8 calls.** Sample 1–2 intermediate established-
grid angles inside the *currently unsampled* 36.0°→38.4° gap (e.g.
37.0° and/or 37.4°, on the existing 0.2° `DENSE_ANGLES` grid) and compute
`p_abs_w(C40,θ)`/`p_abs_w(G40,θ)` there. This directly tests whether the
`G40−C40` differential's fall from `5.40×10⁻¹⁵` (36.0°) to `3.82×10⁻¹⁵`
(38.4°) continues toward (or through) a genuine local minimum/sign
change in that gap — the numerator-side analogue of what R13 already did
for the denominator — or instead reverses smoothly, consistent with
ordinary curvature and no localized feature at all. At 4 calls (1 angle
× 2 configs × 2 legs) this is a third the cost of the still-open 3-angle
tripwire and answers a genuinely different question (numerator
fragility/local structure) than that tripwire's own denominator-
multiplicity question — complementary, not a substitute, and cheap enough
to dispatch alongside it in the same shift if either is ever run.

## Ranked top-3 for the Director's Iteration-66 queue

1. **[Tier 1, zero-FDTD]** File the `p_abs_w(C40)`/`p_abs_w(G40)`
   decomposition (§2/§4a) as a named LOGBOOK/board item, and open a
   candidate R13-addendum: `ratio_k`'s numerator (`frac_p_abs`), not only
   its denominator, is a small-difference-of-close-quantities
   construction and should be floor-gated (or at minimum flagged) the
   same way — before any future cycle trusts a single-point `frac_p_abs`
   reading near a feature this fragile. Cheapest, most decisive item on
   the board this cycle produced.
2. **[Tier 1, ≈4–8 calls]** Bracket the 36.0°→38.4° gap (37.0°/37.4°) to
   resolve whether the `G40−C40` differential has a genuine local
   minimum/near-zero feature there — cheaper than, and complementary to,
   the still-open 3-angle forward-tripwire; directly answers whether the
   38.4° dip is a narrow, real, PAD-diffraction-scale feature or ordinary
   curvature undersampled by this cycle's own 0.4°-wide bracket.
3. **[Tier 1, standing, unaffected]** Complete the already-committed
   3-angle forward-tripwire (≈37.1°/37.2°, 40.2°, 41.4°) — still the
   single most overdue, previously pre-registered item on the T28 board;
   if a future shift samples angles near 37°, items 2 and 3 can share the
   same dispatch for near-zero marginal extra cost.

## Secondary note (process hygiene, not board-ranked)

The disclaimer-carry discipline this cycle was built specifically to
protect (Idealizations 9/10, the fourth-instance Checkpoint-4 tripwire
from Iteration 64) held cleanly through to `NOTES.md`'s own Result
section — verified directly, not assumed: every Q1/Q4/Q5/Q6 restatement
in the committed record carries the NETD-not-human-eye and
constraint-3-not-tested disclaimers inline, and the historical-record
note (exp-087 unedited, exp-088 a separate forward-citable reading) is
stated explicitly. No fourth disclaimer-erosion instance found in the
filed record. This is worth recording precisely because three of the
last four cycles on this sub-thread failed it.
