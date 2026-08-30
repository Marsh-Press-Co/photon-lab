# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 68 · exp-091

## Verification performed before writing this review

Re-derived, from `results.json`/`run_output.txt` directly (not from
`NOTES.md`'s Predictions section, which is all that exists there — see §0
below), every load-bearing number cited in this review: the (a) per-theta
`delta_scene`/`frac_contrast` ratios and sign flags, the (a2) bracket pairs
and their `v0`/`v1` values, the (b) `ratio_k` table at all three legs, and
(b2)'s `frac_p_abs` ratios. Independently rebuilt the exp-087/088/089 n=7
FLOOR-margin/label table from each experiment's own primary `results.json`
(`087.../results.json::frac_contrast`, `088.../results.json`'s Q3/Q5 tables,
`089.../NOTES.md`'s Q3 table) and cross-checked it bit-exact against
`090-t28-floor-frac-threshold-fit/results.json::table1`, which carries the
identical seven `(theta, margin, ratio_k, y)` rows. All arithmetic below
(the AUC/zone-inversion computation in §2, the linear-extrapolation crossing
estimates in §3) was computed directly from these primitives, not asserted.

## §0. A process gap, flagged before the substance: no Result section exists yet

Unlike exp-087/088/089/090's own `NOTES.md` — each of which already carried
a written Result section (Q-item verdicts, tables, prose) by the time blind
Phase-5 review began — exp-091's `NOTES.md`, as committed, stops at
Idealization 10 (line 221). There is no Result section. `results.json` and
`run_output.txt` exist and are internally consistent, but nothing in the
record yet states, in prose, what they mean, cross-references item 10 as
the Phase-3 docket required, or carries the mandatory dual-section
idealizations banner into a Result section (Iteration-65 CHECKPOINT's own
non-discretionary rule — the two-section requirement literally cannot have
been satisfied yet because the second section does not exist). Everything
in this review's §§1–4 was derived directly from the raw JSON/log, not from
a stated claim I am checking. This is not itself a violation — it may
simply reflect this cycle's own workflow ordering — but it means the
Director's Result write-up, whenever filed, needs to independently
reproduce (not retrofit around) every finding below, including the ones
that are less than fully comfortable for this cycle's own headline framing.

## §1. Verdict: **CONCUR-WITH-GAP**

The design is sound, the mandatory-fix docket (all ten items, including my
own) was genuinely discharged rather than nominally checked off, all house
gates pass, and the PRIMARY REFUTE is reported as a REFUTE rather than
softened — this cycle's own Phase-1/Phase-3 authors did nothing wrong. I
concur with the measurements as run and with treating (a) as a genuine
REFUTE. The gap is downstream, not upstream: as filed, the record does not
yet work through what this REFUTE does to `exp-090`'s already-LOGBOOK-cited
"sound, usable" caution zone (§2, below) or give the (a2) REFUTE's own
"crossing not reproduced" language the more informative reading the
available data supports (§3). Neither gap is a gate failure or a falsified
prediction; both are completeness gaps a Phase-5 review exists to catch
before a Combined Verdict is written around an incomplete accounting.

## §2. The sharpest question: does this validate my own Phase-2 metric — and should it become a standing rule?

**The bare fact, independently reconfirmed:** my Phase-2 critique
(`phase2_critique_quantum.md`) used the proposal's own cited numbers to show
41.4° (FLOOR margin 1.3095×, crossing distance 0.0609°) is the harder case
on both metrics than 40.2° (1.4764×, 0.0654°) — the proposal had the two
angles backwards in its own §4c2/Idealization 10. The Director adopted this
in full (`phase3_synthesis.md` §1 item 1: "run both," not merely relocate).
The run then produced exactly the asymmetric outcome my attack's own
framing would have predicted if pressed: 41.4° is the angle that
reclassifies (ENERGY-DOMINANT 28.85 → CONSISTENT 9.21); 40.2° survives, but
by a hair (10.0744, 0.74% above `RATIO_HIGH=10.0`).

**Is this a mechanistically real predictive relationship, or a coincidence
dressed up as one?** I think it is real in *direction* but has not yet
earned standing-rule status, for three separable reasons.

1. **The mechanism is not mysterious.** `ratio_k ∝ 1/frac_contrast` near a
   zero-crossing of `delta_scene`, and `frac_contrast`'s own FLOOR-margin
   is a monotonic (if indirect) proxy for distance from that
   zero-crossing. A quantity behaving like `1/x` near `x=0` is, by
   construction, more sensitive to any perturbation — resolution
   refinement included — the smaller `x` (here, margin) is. So a metric
   built from margin/crossing-distance predicting *which* of two
   near-threshold points is more fragile under a resolution change is not
   numerology; it is the same nonlinearity R13's own founding text already
   named. In that sense the result is unsurprising, not lucky.

2. **But the metric's own discriminating power between the two candidates
   here was thin, and the observed outcome separation was not.** The two
   "hardness" numbers differ by only ~13% (margin) and ~6% (crossing
   distance) between 40.2° and 41.4° — yet the actual driver of the
   differential outcome, the `frac_contrast_R3/frac_contrast_cpl20` growth
   ratio, differs by 50% between them (2.7793× at 40.2° vs. 4.1554× at
   41.4°, per `run_output.txt` (a)), and only one of the two crosses
   `RATIO_HIGH`. A `1/x`-type nonlinearity can absolutely amplify a small
   input difference into a large output difference near a pole — so this
   is *consistent* with my metric being predictive, but a single instance
   with this much amplification cannot by itself distinguish "the metric
   is quantitatively predictive" from "the metric got the sign right by
   luck this once, and the amplification is really being driven by some
   other, uncharacterized feature of the local curve shape." Telling those
   apart needs a dose-response check across more than one pair.

3. **n=1 is exactly the sample size this program's own house discipline
   says not to generalize from.** R5 killed a phase-offset "predictor" that
   looked decisive on a small check until a systematic AUC/null-permutation
   sweep was run. R7 forbids certifying a claim from an un-fit design's
   conditioning number alone. R12 requires ≥5–8 independent draws before a
   tail-statistic claim is "settled," not "suggestive." My own metric here
   has exactly one confirming comparison (two candidates, one correct
   call) — the same evidentiary weight R5's dense search or R12's
   single-seed match had before this program's own discipline required
   more. Minting a standing rule off this would repeat that exact shape,
   from the seat whose job is to catch it.

**My recommendation:** log this as a *candidate* predictive signal, worth a
name (something like "crossing-proximity fragility index") and worth the
cheap, direct test that would actually validate or kill it — not yet a
standing rule. The correct next check (folded into §4's ranked list) is a
systematic one: compute the margin/crossing-distance metric for several
more points spanning a range of values (not just the two already run) and
check whether `frac_contrast` growth ratio or reclassification frequency
scales with it in a fitted, out-of-sample-checked way — the same discipline
R5's own AUC sweep and R10's circular-shift null represent, applied here to
a resolution-fragility question instead of a period or phase claim. Until
that exists, the honest statement is: *this cycle's result is compatible
with, and mechanistically consistent with, my Phase-2 metric being a real
fragility indicator — not yet proof that it is one.*

## §3. Sample-construction check: what this does to exp-090's n=7 caution zone

This is the sharper and, I think, more consequential of the two questions
this review was asked to reason through concretely, so I did the arithmetic
rather than describing it qualitatively.

**The caution zone's actual construction (re-verified from
`090.../results.json::table1`, not from prose):** `Y(θ)=1` iff the
*cpl=20* `ratio_k(θ)` exceeds `RATIO_HIGH=10`; `Y=0` otherwise. The zone is
`[max{margin : Y=1}, min{margin : Y=0}]` — a purely order-statistic object
that depends on exactly two points: whichever `Y=1` point has the *largest*
margin, and whichever `Y=0` point has the *smallest*. In the filed n=7:

| θ | margin (FLOOR) | ratio_k (cpl=20) | Y |
|---|---|---|---|
| 41.4° | 1.3095 | 28.807 | **1** |
| 40.2° | 1.4764 | 25.082 | **1** ← sets lower edge |
| 37.2° | 2.1709 | 3.443 | 0 ← sets upper edge |
| 36.0° | 3.8793 | 2.642 | 0 |
| 41.8° | 6.5889 | 5.710 | 0 |
| 38.4° | 7.4946 | 0.908 | 0 |
| 38.8° | 8.0187 | 3.873 | 0 |

Zone = `[1.4764, 2.1709]`, exactly as filed. Note first: **both `Y=1`
points are the two angles exp-091 just resolution-tested, and both are now
independently shown resolution-fragile** — not just 41.4°. 40.2° is the
point that *sets the zone's own lower edge*, and it is exactly the point
where (a) PRIMARY REFUTED: `delta_scene(40.2°)` changes *sign* between
cpl=20 (`−1.5427×10⁻⁴`) and cpl=30 (`+4.3699×10⁻⁴`). Its `ratio_k`
classification survives cpl=30 only because `frac_contrast` is built from
`|delta_scene|` and the classification landed at 10.0744 — 0.74% above the
`RATIO_HIGH=10` line the whole zone is calibrated against. So the point
*defining* the zone's boundary is now shown qualitatively unstable (wrong
sign of the underlying physical quantity) even though its *derived* label
survived by a coin's-edge margin. 41.4° is the point whose *label itself*
flips. Between them, **100% of the n=7 sample's positive (`Y=1`) class has
now failed a resolution-stability check this cycle ran for the first time**
— one completely, one at the level of the quantity feeding it.

**What happens to the zone if 41.4° is honestly relabeled `Y=0` (its
cpl=30 finding)?** New `Y=1` set = `{40.2°: 1.4764}` alone. New `Y=0` set
includes `41.4°: 1.3095`. `min{margin:Y=0} = 1.3095 < max{margin:Y=1} =
1.4764` — **the order-statistic zone inverts** (lower edge exceeds upper
edge), which is *exactly* `090.../NOTES.md`'s own Q3 pre-registered
falsification clause: "Falsified if the computed zone is empty, inverted,
or the underlying separation has any tie/inversion (would mean Q1 itself
was wrong)." Computing the AUC under this relabeling (6 negative, 1
positive; correctly-ordered pairs = 5 of 6, since only 41.4° itself, now
negative, ranks below the lone positive) gives **AUC=5/6≈0.833** — a drop
from the filed AUC=1.0, but not a collapse. **This is the point worth
underlining: the aggregate statistic (AUC) looks only mildly damaged while
the specific non-parametric-zone construction — which depends on the two
*extreme* order statistics of a 2-point positive class, not the bulk
ranking — breaks completely.** A method built entirely on order statistics
from an n=2 positive class is far more fragile to a single relabeling than
a bulk concordance measure would suggest, and that fragility was invisible
until the labels themselves were tested against an independent
(higher-resolution) reading.

**Does the sample need to drop 41.4°, relabel it, or is there a principled
reason to still trust its cpl=20 label for this specific calibration
purpose?** I do not think "trust cpl=20 anyway" survives scrutiny, but I
also do not think "relabel to cpl=30 and declare it fixed" is fully
licensed by what exp-091 actually showed:

- The caution zone's entire *purpose* is to identify which low-margin
  `ratio_k` labels are untrustworthy relics of denominator-crossing
  proximity (R13's founding logic) — treating the same-resolution label as
  ground truth for calibrating "how much do I trust this resolution's
  labels" is circular by construction. There is no principled reason to
  keep it as ground truth specifically *because* the entire reason this
  calibration exists is to catch exactly this failure mode.
- But cpl=30 is not yet shown to be *converged* ground truth either.
  41.4°'s own `frac_contrast` grew 4.1554× from cpl=20→30 — outside the
  tight `[0.3,3.0]` CONFIRM band, inside only the wider REFUTE-avoiding
  `[0.1,10]` band, i.e. explicitly flagged by this cycle's own protocol as
  a "NEITHER" outcome, not a clean confirmation of stability. Nothing rules
  out a further swing at cpl=40. Treating cpl=30 as settled truth to
  relabel against would be exactly the kind of single-step, unverified
  substitution this program's own house discipline (R6/R8's "verify the
  alternative independently, don't just reason about it") warns against.
- The defensible position is therefore: **41.4°'s true classification is
  currently unresolved, not newly resolved to CONSISTENT** — and that
  status, on its own, is already sufficient to invalidate the n=7 sample's
  claimed clean perfect-separation property, independent of which specific
  alternate label eventually turns out correct. The concrete next step
  (§4, item 1) is to recompute the zone/AUC/Firth fit under *both*
  candidate treatments (drop; relabel) and report them side by side — the
  same "report both, more conservative governs" discipline R10 already
  established for a disagreement between two null constructions, applied
  here to a disagreement between two resolutions' labels.

**One further point of caution, not yet a firing concern (see §5):**
Iteration-67's own Combined Verdict (LOGBOOK, exp-090) called the caution
zone and Firth's fit "sound, correctly scoped, and now independently
reproduced by at least nine parties across every phase." That characterization
is now shown, by data this same sub-thread collected one cycle later, to
rest on a sample whose founding perfect-separation property does not
survive its own two `Y=1` points being resolution-checked. Nothing about
this is a failure of exp-090's own cycle — the gap was flagged as open at
the time (MATERIALS' own repeated Phase-2/5 critiques, adopted verbatim
into exp-091's own hypothesis) — but the LOGBOOK's standing characterization
of the zone as "sound" needs an explicit amendment when this cycle's entry
is written, not silent inheritance forward.

## §4. Is the (a2) "REFUTE, cannot interpolate" conclusion the right one, or does it hide a short double-crossing?

Reasoned through with the four available cpl=30 points plus the two known
cpl=20 anchors at the same four angles (all pulled directly from
`run_output.txt`/`083.../results.json`):

| θ | delta_scene, cpl=20 | delta_scene, cpl=30 |
|---|---|---|
| 40.2° | −1.5408×10⁻⁴ | **+4.3699×10⁻⁴** |
| 40.4° | +3.1697×10⁻⁴ | +9.8564×10⁻⁴ |
| 41.4° | +1.3374×10⁻⁴ | +5.6255×10⁻⁴ |
| 41.6° | −3.0545×10⁻⁴ | +1.7838×10⁻⁴ |

**The formal (a2) test only checks for a sign change *within* each cpl=30
bracket pair** — it never compares a bracket point against its own cpl=20
value. That is too narrow a test of what actually happened, and the richer
signal is visible in the table above without needing the bracket at all:
**the sign flip already happened *at* 40.2° itself** (negative at cpl=20,
positive at cpl=30) — the same fact (a)'s PRIMARY REFUTE is built on. That
alone tells us the crossing near 40.265° has moved to some angle *below*
40.2° at cpl=30 (assuming locally monotonic behavior, discussed below) —
independent of, and more informative than, "no sign change was found
between 40.2° and 40.4°."

**Can the two remaining data points distinguish "the crossing moved
outside the bracket" from "a short-lived double-crossing (in and back out)
that the 0.2° step missed"?** Two arguments favor "moved," neither
conclusive alone:

1. **Slope consistency.** At cpl=20, `delta_scene` is *increasing* through
   40.2°→40.4° (−1.54×10⁻⁴ → +3.17×10⁻⁴) and *decreasing* through
   41.4°→41.6° (+1.34×10⁻⁴ → −3.05×10⁻⁴). At cpl=30, the same two windows
   preserve the same local slope *sign* (40.2°→40.4° still increasing,
   41.4°→41.6° still decreasing) even though both have shifted to sit
   entirely on the positive side. A short in-and-out double-crossing
   requires a local slope *reversal* inside the window; nothing in the
   sign pattern here shows one. This is necessary, not sufficient — a
   double-crossing squeezed well inside the 0.2° window could still
   recover the same endpoint signs — but it is the piece of evidence the
   two endpoints alone can actually offer, and it points toward "shifted,"
   not "dipped and returned."
2. **Naive linear extrapolation using each pair's own local slope**
   (illustrative, not a claim of precision — see caveat below): at
   40.2°→40.4°, slope = `(9.8564−4.3699)×10⁻⁴/0.2° = 2.743×10⁻³/°`;
   extrapolating backward from 40.2° (`+4.3699×10⁻⁴`) to zero gives a
   crossing near **40.04°**, a shift of **≈−0.22°** from the cpl=20
   crossing (40.265°) — larger than the full 0.2° grid step. At
   41.4°→41.6°, slope = `(1.7838−5.6255)×10⁻⁴/0.2° = −1.921×10⁻³/°`;
   extrapolating forward from 41.6° (`+1.7838×10⁻⁴`) gives a crossing near
   **41.69°**, a shift of **≈+0.23°** from 41.461°. Both estimates are
   large — bigger than "just past the edge of the bracket" — and in
   *opposite* directions (one crossing moves down in angle, the other up),
   which is itself informative: a uniform "everything shifted the same
   way" story (e.g. a systematic angular calibration offset between cpl=20
   and cpl=30) is disfavored; whatever is moving these two crossings is
   doing so independently at each one.
3. **No established mechanism in this record operates at the relevant
   length scale for a double-crossing.** Every periodicity this sub-thread
   has ever confirmed on this channel (T21's Huygens fringe, ~1.4–2.5°;
   `delta_scene`'s own established period, ~2.84–2.95°) is 7–15× longer
   than the 0.2° window in question. A brief in-and-out dip fully contained
   within 0.2° would be new, unprecedented fine structure with no proposed
   physical origin — not impossible, but it is the less parsimonious
   reading given everything else this program has found on this exact
   channel.

**Caveat, stated plainly:** the two extrapolated shift estimates above are
a 2-point linear fit over a window this same record already knows carries
real curvature (the established ~2.84–2.95° period), so treating ±0.22°/
±0.23° as precise crossing-location numbers would overclaim — they are
order-of-magnitude sanity checks, not a filed result, and I have not filed
them as such. **My conclusion:** the (a2) REFUTE verdict is the procedurally
correct call given the pre-registered test, but its own filed language
("crossing not reproduced in this bracket") undersells what the data
already shows — this is more informative than an unlocated miss. The
available evidence favors "the crossing moved substantially (plausibly
more than a full grid step, in opposite directions at the two nodes)" over
"a short double-crossing hid inside the bracket," but that reading rests on
a rough extrapolation, not a located point, and the honest next step is to
go get the located point (§5, item 2) rather than adopt the extrapolation
as fact.

## §5. Ranked candidates for Iteration 69, and Checkpoint criterion 4

**Rank 1 — zero-FDTD: rebuild exp-090's caution zone/Firth fit under both
the "drop 41.4°" and "relabel 41.4° to Y=0" treatments, reporting both
alongside the original, and note the qualitative sign-flip found at 40.2°
(the zone's *own* lower-edge point) explicitly.** This is the cheapest,
most direct discharge of §3's own finding and should not wait on new FDTD —
it uses only already-committed data. Ranked first because, unlike a new
FDTD bracket, this directly determines whether the *existing*, already
LOGBOOK-cited caution zone can still be cited as filed, which several other
open T28 items (the still-queued full-scale null-calibration re-run,
R12-into-standard-practice) may implicitly assume it can.

**Rank 2 — cheap FDTD: locate the actual cpl=30 crossings directly**, e.g.
4–8 more calls extending outward from the existing brackets (39.8°/40.0° on
the low side of 40.2°, given the extrapolation in §4 points below 40.2°;
41.8°/42.0° on the high side of 41.6°) rather than inward. This converts
§4's rough linear-extrapolation estimate into a measured crossing location,
directly answers the double-crossing-vs-moved question with data instead of
inference, and — combined with Rank 1 — gives the caution-zone rebuild a
third, directly-measured cpl=30 margin/label pair rather than only two
resolution-contested ones.

**Rank 3 — a genuine third resolution point (cpl=40) at 40.2°/41.4°
specifically.** A two-point (cpl=20→30) comparison cannot distinguish
"converging toward a stable value" from "still drifting" — and 41.4°'s own
`frac_contrast` grew >4× even under the outcome this cycle scored as
non-REFUTE. Without a third point, neither cpl=20 nor cpl=30 can be
confidently treated as this channel's converged answer at these two angles,
which is the load-bearing assumption Rank 1's "relabel" branch would
otherwise be making. This is the direct, standard R3 continuation (this
program's own established cpl=20/30/40 sequence elsewhere, e.g. T15) and
should outrank any work that is not needed to interpret this cycle's own
result.

Still open, unaffected, not re-ranked ahead of the above: PHOTONICS' own
grazing-incidence validity check (still the single most-repeated item on
the whole T28 board); the x-wall wavelength-generality leg (now sixteen-plus
consecutive cycles deferred); the still-queued R14(b) formal
null-controlled period fit; the Rank-2-in-exp-090's-own-queue unbiased
margin-vs-distance rebuild on the full 31-point window (Q8's own confound,
separate from this cycle).

**Checkpoint criterion 4 — reasoned explicitly, not by pattern-match.**
Does not fire. Three separate things could look adjacent to it, and I
worked through each:

1. *Is the n=7 sample's now-demonstrated fragility a "known, named, ignored"
   instance in the R6–R14 lineage?* No — it is the opposite shape. The
   resolution gap was named (MATERIALS, three consecutive cycles) and this
   cycle exists specifically to discharge it. Discovering, on discharging a
   named gap, that the underlying sample is shakier than believed is
   science working as intended, not drift.
2. *Is my own §3 finding itself a "caught blind, before LOGBOOK" instance
   that should stay non-firing, per this program's own repeated
   precedent?* Yes, and that is the operative test here: this review is the
   first place in the record (per §0, no Result section exists yet to have
   already stated or omitted it) that works through the caution zone's own
   inversion under relabeling. It is being surfaced now, blind, before any
   LOGBOOK entry — the same discharge condition R6 through R14 have each
   applied. Non-firing is the correct call *provided* it is actually
   incorporated into the Combined Verdict and LOGBOOK entry, not left as an
   unintegrated Phase-5 aside — that is a condition on the Director's
   synthesis, not a fact yet in evidence either way.
3. *Does the missing Result section (§0) itself constitute an omission
   pattern in the R4/R9/disclaimer-erosion lineage?* No — those rules fire
   on an existing caveat or figure failing to propagate into a written
   restatement. Here no Result prose exists yet for anything to have failed
   to propagate into. It is a completeness gap worth naming so the eventual
   Result section is held to the same standard as every other quantity in
   this review, not a fired violation.

No mechanism claim is made anywhere in this cycle (T1 route N/A, matching
every T28 desk/instrument cycle since exp-069), so no constraint is at risk
of being quietly dropped. Criterion 5 (two non-advancing cycles) is N/A —
exp-090 closed PARTIAL with a usable (if now-qualified) deliverable, and
this cycle, once its own downstream consequences are worked through,
directly advances the board's single oldest undischarged item.
