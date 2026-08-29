# PHASE 5 — REVIEW · Panel Iteration 67 · exp-090 · Seat: PHOTONICS (self-review)

Fresh context. No memory of proposing this cycle — PHOTONICS led exp-090's
own Phase 1, so this is the self-review this program's own convention
requires (cf. QUANTUM OPTICS on its own Iteration-65 proposal, VISION
SCIENCE on its own Iteration-66 proposal). Read in full: `PANEL.md`,
`LOGBOOK.md` start to end (R1–R14 in the RULED OUT registry; the complete
T28 live-thread arc, Iterations 46–66), and every exp-090 document
(`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `run_output.txt`,
`results.json`), plus exp-087/088/089's `NOTES.md`/`results.json` for the
source data this cycle reuses.

## 1. Independent reproduction (spot-checks, not trust)

I did not take `run_output.txt`/`results.json` on faith. From the raw
persisted numbers, computed independently, from scratch:

- **`margin(41.4°)`**: `frac_contrast=2.510967×10⁻⁴`, `FLOOR=1.917438×10⁻⁴`
  → `1.309543×` — matches `results.json::table1[0].margin` to the printed
  digit.
- **Gap ratios (Q8)**: `gap_ratio_margin = 2.170947/1.476388 = 1.470445`;
  `gap_ratio_distance = 0.072754/0.065420 = 1.112107` — both match
  `results.json::q8` bit-exact. `margin` genuinely carries ~32% more
  relative headroom than raw crossing-distance at this sample.
- **`m50` (Firth 50%-crossing)**: `10^(-1.7805895/-5.6315196) = 10^0.316246
  = 2.071013` — matches `q4.m50=2.071012796646712` to the printed
  precision.
- **Q7's resolved-margin recomputation**: from `j089["thermo"]`/
  `["box_dev"]` primitives cited in `run.py` (`p_abs_w(C40,37.2°)=
  2.812704×10⁻¹²`, `p_abs_w(G40,37.2°)=2.808673×10⁻¹²`,
  `box_dev_max=4.569131×10⁻⁴`): `Δp_abs=4.0315×10⁻¹⁵`,
  `noise_floor=3×box_dev_max×p_C40=3.8555×10⁻¹⁵`, ratio `=1.04566×` —
  matches `results.json::q7_disclosure.recomputed_resolved_margin` and
  independently confirms exp-089's own filed `1.046×` (Learned #4) is the
  same quantity to printed precision, not a discrepancy.

All four independently reproduce exactly. Nothing in this cycle's numbers
is taken on the strength of the document alone.

## 2. Did Phase 3 apply all nine of Red Team's Phase-2 mandatory fixes?

Checked each against the actual committed `NOTES.md` text, not the
synthesis's own claim to have applied them:

| # | Fix | Where it landed in `NOTES.md` | Applied? |
|---|---|---|---|
| 1 | Dual-section carried-idealizations banner | Present verbatim at both the Predictions section (lines ~66–75) and the Result section (lines ~238–242) | **Yes** |
| 2 | R3 spatial-resolution disclosure | Idealization 9 | **Yes** |
| 3 | Forward-sampling-bias disclosure | Idealization 10 | **Yes** |
| 4 | Reword P2's evidentiary claim | Q2, both Predictions and Result, "diagnostic sanity check... NOT independent evidence" | **Yes** |
| 5 | Reword P5's falsifiability claim | Q5, both sections, "deterministic illustration... NOT a live falsification test" | **Yes** |
| 6 | Reclassify P2/P5 as diagnostic, not falsifiable | `run.py`'s own field names (`q2_diagnostic_only`, `q5_diagnostic_only`) plus NOTES.md prose | **Yes** |
| 7 | Disclose 37.2°'s pre-existing resolved-margin fragility next to the zone's upper edge/`m50` | Q7 (new), cross-referenced in the Result section immediately after Q4/`m50` | **Yes** |
| 8 | Compute (not argue) the distance-to-crossing sensitivity comparison | Q8, computed in `run.py`, reproduced above | **Yes** |
| 9 | Disclose the n=7 population as curated/crossing-proximity-enriched | Idealization 11 | **Yes** |

All nine land, correctly, in the committed record — not merely claimed in
`phase3_synthesis.md`'s own disposition table. I found no residual
`phase1_proposal.md`-only language (the pre-fix framing) anywhere in
`NOTES.md` itself.

## 3. From the PHOTONICS lens: does anything sit awkwardly with the optical mechanism?

My charter is optical-response coherence across wavelength and angle. This
cycle is zero-FDTD desk statistics on an already-existing dataset — there
is no new optical *prediction* to check for wavelength/angle coherence in
the usual sense. But the method's own physical premises (§5's "locally
linear near a simple zero" argument, and Q8's margin-vs-distance
comparison) ARE optical claims, and they are checkable against the raw
per-theta primitives already in the record. Three findings:

**3a. A genuinely new (if small) finding: the four established
`delta_scene` crossings do NOT share one local slope — a ~1.8× spread,
already implicit in the cycle's own committed numbers, never stated.**
Since `margin(θ) ≈ frac_contrast(θ)/FLOOR ≈ |slope|·|θ−θ₀|/FLOOR` very
near a simple zero, `margin/distance` estimates each crossing's own local
steepness in FLOOR-units/degree. Computing this from the cycle's own Q3/Q8
tables:

| Crossing (θ₀) | Nearest sampled angle | `margin/distance` (≈ local slope) |
|---|---|---|
| 38.590° (the original R13-founding node) | 38.4°, 38.8° | **39.40, 38.23** |
| 37.127° | 37.2° | **29.84** |
| 40.265° | 40.2° | **22.57** |
| 41.461° | 41.4° | **21.50** |

The founding 38.590° node is ~1.8× steeper than the 40.265°/41.461° pair,
with 37.127° in between. This is consistent with — and gives a concrete,
quantitative mechanism for — Q8's own headline finding that `margin` beats
raw angular distance as a regressor: it is not that `margin` is an
abstractly "better-behaved" statistic, it is that `margin` correctly
encodes a REAL inhomogeneity in the underlying oscillation's local
steepness across the four crossings that a pure distance measure cannot
see. This is also consistent with, not in tension with, this sub-thread's
own long-standing finding that the ~2.84–2.95° periodicity is chirped/
non-stationary rather than a fixed-amplitude single-tone sinusoid
(exp-084's "chirped" reading; exp-085's Method-C classification attempt,
later downgraded on reliability grounds, not on the chirp premise itself).
I did not find this slope-spread stated anywhere in `phase1_proposal.md`,
`phase3_synthesis.md`, or `NOTES.md` — it is implicit in already-committed
numbers, not a new falsifiable claim (this is a desk observation from
existing data, not a new measurement), and I flag it as a candidate
Iteration-68 line item rather than a defect in this cycle.

**3b. The far-from-crossing points (36.0°, 41.8°) behave exactly as an
oscillatory (not runaway) signal should, and the method's own §5 argument
is correctly scoped to avoid over-claiming there.** At 36.0°
(distance≈1.127°, more than a third of a period away) the local-linear
slope model would predict `margin ≈ 29.8×1.127 ≈ 33.6` — the actual value
is 3.88, an order of magnitude smaller, because `delta_scene` saturates/
oscillates rather than growing without bound. `phase1_proposal.md` §5's
"locally linear near a simple zero" argument is never invoked for these
two points and is not needed to be — it is used only to justify excluding
raw θ as a second regressor for the five near-crossing points, where the
approximation is actually being used. I confirm this scoping is correct
and does not overreach.

**3c. Two independently-motivated fragility signals happen to concentrate
at the same point (37.2°), and this is worth naming explicitly even though
Q7 already discloses one half of it.** 37.2° simultaneously (i) sets the
Q3 zone's upper edge and Firth's shallow-end anchor via `frac_contrast`'s
own floor-margin (2.1709×, comfortable), and (ii) carries this
sub-thread's own thinnest-ever `resolved`-gate significance margin
(1.0456×, on the *numerator* noise floor — a different, decoupled
quantity, correctly kept decoupled per the Q7-vs-Q3 discipline
exp-089 established). These two quantities are algebraically independent
(one is a denominator-floor ratio, the other a numerator signal-to-noise
ratio) and I found no reason to believe they share a common cause. But
their co-location at the single point most load-bearing for this cycle's
own upper-edge citation is a coincidence a future reader should not read
past — Q7 already names the "drop 37.2°" LOO scenario as operationally
primary; I'd add that a genuinely independent re-measurement at 37.2°
(tighter settling, or a finer local bracket) would relieve BOTH fragilities
at once, not just the one Q7 is scoped to.

**None of 3a–3c overturns anything in this cycle's own Result.** They are
confirmations-with-mechanism (3a, 3b) and a naming of an already-partially-
disclosed coincidence (3c), not a new defect. I looked specifically for a
wavelength-coherence problem (this whole fit is single-λ/single-article,
correctly and repeatedly disclosed as Idealization 3/16) and an
angle-coherence problem (the curated-sample caveat, RT-2/Idealization 11)
and found both already correctly scoped by the cycle's own mandatory-fix
docket — I have nothing to add there beyond 3a's quantitative texture.

## 4. Verdict: CONCUR

Every frozen prediction reproduces bit-exact on independent re-derivation
(§1). All nine of Red Team's Phase-2 mandatory fixes are actually present
in the committed `NOTES.md`, not merely claimed (§2). The method's own
physical premises hold up under a photonics-specific stress test I ran
myself from already-committed numbers, and in fact gain a small,
previously-unstated mechanistic explanation (§3a) rather than developing a
crack. This is a correctly-scoped, zero-FDTD instrument-calibration cycle
(T1 route N/A, matching every T28 desk cycle since exp-069) with a real,
usable deliverable — the `[1.4764, 2.1709]` caution zone — and no
unresolved mechanism claim smuggled in. I find nothing here that should be
weighed as PARTIAL-with-reservations; this is a clean CONCUR.

## 5. Ranked top-3 candidate directions for Iteration 68 (PHOTONICS' own lens; not coordinated with any other seat)

1. **PHOTONICS' own long-queued grazing-incidence validity check.** Named
   "near-unanimous #1 on the whole T28 board" every cycle since roughly
   Iteration 51 and never once executed. This is squarely my own seat's
   charter question (angular dependence of the optical response as θ
   approaches grazing) and directly bears on whether `delta_scene`/
   `frac_contrast`'s behavior at 36°–42° extrapolates safely toward the
   window's own edges, where every T28 near-field/diffraction model this
   sub-thread has tested (T21's fringe, the x-wall/y-wall echo families)
   has needed its own separate grazing-incidence correction. Overdue by
   this cycle's own count and by every prior cycle's.

2. **The R3 spatial (`cpl`) resolution check on the `frac_contrast`/
   `frac_p_abs`/`ratio_k` channel, at minimum at 40.2°/41.4°.** This
   cycle's own Idealization 9 names it undischarged three cycles running
   (088, 089, 090) and correctly identifies that it bears directly on the
   two points setting the Q3 zone's LOWER edge — the more operationally
   consequential edge for future NODE-UNRESOLVABLE/CAUTION decisions,
   since it is closer to the existing hard floor. A ~7% historical R3
   "survives resolution" precedent exists elsewhere on this bench
   (exp-005/exp-015); this specific channel has never been checked at all.

3. **A denser local sweep at/near 37.2°, explicitly targeting the local
   slope of `frac_contrast(θ)` at each of the four established crossings**
   (not just 37.2°) — both to test §3a's slope-spread finding above with
   real, finer-grid FDTD data rather than the existing 0.2°-grid points,
   and to independently stress-test whether 37.2°'s own thin
   `resolved`-gate margin (§3c) is a one-off or reproducible at nearby
   angles. This single measurement relieves the two independent
   fragilities Q7 and §3c both name, at the cycle's own single
   most-load-bearing point, more directly than any other item on the
   current board.

(The x-wall wavelength-generality leg — now sixteen consecutive cycles
deferred, 076–090, and squarely within my own charter's wavelength axis —
remains a standing concern but I rank the three items above higher this
cycle because they are cheaper, more directly load-bearing for THIS
cycle's own deliverable, and one of them, item 1, has a longer unbroken
deferral streak on a near-unanimous board pick specifically.)
