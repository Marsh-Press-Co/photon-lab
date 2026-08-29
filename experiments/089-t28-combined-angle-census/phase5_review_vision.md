# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 66 · exp-089

Fresh context, no memory of any other seat's current-cycle output. Read in full:
`PANEL.md`; `LOGBOOK.md` RULED OUT (R1–R14, in full) and ESTABLISHED; T28 LIVE
THREADS through Iteration 65/exp-088 (both CHECKPOINT entries, in full,
including my own seat's exp-088 Phase-5 review, read for house-style
calibration only); this cycle's complete record — `phase1_proposal.md`, all
five `phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json`.

## Verdict, up front

**CONCUR** — every arithmetic claim in the Result section independently
reproduces (§1 below), and the two structural fixes this sub-thread adopted
one cycle ago (the mandatory dual-section banner; the correctly-scoped NETD/
T9-anchor extension) both actually landed and hold up. No Checkpoint-4-grade
defect exists in this cycle's record.

But: **one real, if non-fatal, framing risk sits in `NOTES.md`'s own Learned
item 1**, and it is exactly the "confident language creeps in where the data
doesn't fully support it" shape this exact sub-thread has fired Checkpoint
criterion 4 on four times — not disclaimer *dropping* this time, but *causal
over-generalization* dressed in careful prose. I recommend it be corrected
before any future LOGBOOK/PLAN.md citation quotes it (see §3, §4). Two
smaller, non-blocking completeness gaps are also logged (§2, §5).

## §1. Independent recomputation (not trusted from NOTES.md's own prose)

Recomputed directly from `results.json`'s raw `thermo`/`box_dev` primitives,
reproducing the Result-section table bit-for-bit:

| θ | p_abs_w(C40) | p_abs_w(G40) | frac_p_abs (recomputed) | frac_contrast | ratio_k (recomputed) | resolved margin (recomputed) |
|---|---|---|---|---|---|---|
| 37.2° | 2.812704e-12 | 2.808673e-12 | `\|Δp\|/p_C40` = **1.4333×10⁻³** | 4.1627×10⁻⁴ | **3.4433** | **1.045×** |
| 40.2° | 3.077251e-12 | 3.055402e-12 | **7.1004×10⁻³** | 2.8309×10⁻⁴ | **25.082** | **2.087×** |
| 41.4° | 3.164949e-12 | 3.187843e-12 | **7.2334×10⁻³** | 2.5110×10⁻⁴ | **28.807** | **4.686×** |

Resolved margin recomputed as `|p_G40−p_C40| / (NOISE_MULT × max(box_dev_ext,
box_dev_abs across both configs and boxes) × p_C40)`, matching the formula in
`run.py`'s own `resolved[th]` block — all three reproduce NOTES.md's cited
1.046×/2.087×/4.685× to the displayed precision. FLOOR margins
(`frac_contrast/FLOOR`, FLOOR=1.91744×10⁻⁴) reproduce exactly as 2.171×/
1.476×/1.310×. `classify_resolved`'s veto rule (`experiments/087-.../
run.py::classify_resolved`, read directly): any ratio_k in the resolved set
exceeding `RATIO_HIGH=10` forces `"X"`→`ENERGY-DOMINANT` outright — with
25.08 and 28.81 both in the 7-ratio combined list, the Q6 ENERGY-DOMINANT
classification is not a judgment call, it is this function's literal,
correctly-applied output. No arithmetic or citation defect found anywhere in
the Result section.

## §2. NETD/T9-anchor extension (Q7) — correctly scoped, no conflation found

This is precisely my seat's duty (pin thresholds before they're trusted, and
watch for an instrument threshold being read as a human-perceptibility one).
I checked it hard and found it clean. `lab/thermo_sidecar.py::netd_disposition`
returns a `disclaimer` string carried verbatim into every one of the 6 `thermo`
cells in `results.json` ("NETD is an instrument/detector threshold, not a
human perceptual one — this classification does NOT bear on constraint-3/4's
human-eye verdict"), and `NOTES.md`'s own Q7 Result paragraph restates this
inline, correctly, not just by reference: *"NETD is an instrument/detector
threshold, not a human-eye one — this does NOT bear on constraint-3/4's
human-eye verdict (Idealization 9)."* `ratio_abs_ext` (0.5126–0.5151) is
explicitly labeled "informal context, not a scored falsifier" both in the
frozen Predictions and in the Result — it is never used to license any
detectability or human-visibility claim. This is the correct, disciplined
use of an energy/thermal instrument reading, and it is the third consecutive
T28 cycle (087, 088, 089) to get this specific separation right. No finding
here beyond confirming it holds.

## §3. The dual-section banner — present, correctly worded, but its own internal citation discipline still drifts

The literal Phase-3 fix-docket item 1 requirement — a "carried idealizations"
banner block at the top of both the Predictions section and the Result
section — **is satisfied**. I read both blocks directly: Predictions opens
with *"Carried idealizations banner (Phase-2 fix item 1, MANDATORY
dual-section requirement per the Iteration-65 CHECKPOINT): every prediction
below is governed by Idealizations 9-10 ... and Idealization 16 ..."*; Result
opens with the parallel *"every finding restated below is governed by
Idealizations 9-10 ... and Idealization 16 ..."* plus an explicit
self-audit line ("the second consecutive T28 cycle... to carry this banner
independently at both... sections"). This is real, and it is the fix working
as designed — a genuine improvement over exp-088's own filed defect.

But the banner's own header text promises more than the document below it
delivers: it says "restated inline **at each restatement below**," yet a
per-item audit of every Q1–Q7 paragraph in both sections shows the actual
citations are selectively scoped, not uniform, and — more to the point —
**not always identical between Predictions and Result for the same item**:

| Item | Predictions cites | Result cites |
|---|---|---|
| Q1 | Idealizations 8, 16 | *(none)* |
| Q3 | Idealizations 9-10, 12 | Idealizations 9-10, 16 |
| Q5 | Idealizations 9-10, 16 | Idealization 16 only |
| Q6 | Idealizations 9-10, 12 | Idealizations 9-10 (12's substance kept in prose, not cited by number) |
| R14(a) gate | Idealization 11 | *(none)* |

None of these drops touches the item where it would actually matter — Q3,
Q6, and Q7 (the ratio_k/ENERGY-DOMINANT-bearing paragraphs) all correctly
carry 9-10 in **both** sections, so there is no live human-eye/NETD
conflation risk anywhere in this cycle's record. This is why I rule it
non-blocking and explicitly **not** a fifth instance of the R6–R14
"disclaimer erosion" shape (that shape is specifically about NETD/
constraint-3 language vanishing from a load-bearing prose restatement; here
it never vanishes from any load-bearing one). But given this exact
sub-thread fired Checkpoint criterion 4 four times on drift of precisely
this kind, and given the banner's own text claims a uniformity the document
does not actually have even one cycle after being written specifically to
guarantee it, I log it now rather than let a sixth instance of *some*
version of this shape reach a future cycle unflagged.

## §4. Sharpest finding — Learned item 1's framing outruns what this cycle's own margin/outcome pattern supports

`NOTES.md`'s Learned section, item 1 (bolded, first, the item most likely to
be quoted forward): *"The 'single-node-artifact' reading is dead... Whatever
T28's energy-interception channel is actually doing, it is **not confined to
one node's immediate neighborhood**."*

Read against the combined 8-point dataset this cycle itself produced and Q1
already tabulates, this headline is at serious risk of being over-read. I
built the full margin/outcome table directly from `results.json` and the
retroactive exp-088 reclassification it cites:

| θ | distance to nearest `delta_scene` zero-crossing | FLOOR margin | outcome |
|---|---|---|---|
| 36.0° | 1.127° | 3.88× | CONSISTENT |
| 37.2° | 0.073° | **2.17×** | CONSISTENT (barely — 1.046× resolved margin, thinnest ever) |
| 38.4° | 0.190° | 7.49× | CONSISTENT |
| 38.6° | ≈0.01° (the crossing) | 0.39× | NODE-UNRESOLVABLE |
| 38.8° | 0.210° | 8.02× | CONSISTENT |
| 40.2° | 0.065° | **1.48×** | **ENERGY-DOMINANT** |
| 41.4° | 0.061° | **1.31×** | **ENERGY-DOMINANT** |
| 41.8° | 0.339° | 6.59× | CONSISTENT |

Sorted by FLOOR margin: the three thinnest resolved margins in the entire
8-point set — 37.2° (2.17×), 41.4° (1.31×), 40.2° (1.48×) — are, without
exception, the three points this cycle deliberately chose *as the closest
available grid neighbor to a zero-crossing* (§4 of `phase1_proposal.md`'s
own selection rule). Every point with a comfortable margin (≥3.88×) reads
cleanly CONSISTENT; every point with a thin margin (≤2.17×) either fails the
floor gate outright (38.6°) or reads ENERGY-DOMINANT/barely-resolved (40.2°,
41.4°, 37.2°). This is not a coincidence of the census design — it is the
census design, and the outcome tracks it almost monotonically.

That pattern is at least as well explained by, and arguably more
parsimoniously explained by, **Learned item 2's own reading**
("`FLOOR_FRAC=0.10` looks materially too permissive... both misses happened
well inside the 'clears' region") than by item 1's own headline framing. Item
1, read plainly by a future citer skimming only the bolded first line, reads
as "this is a broad, node-independent phenomenon" — a categorically stronger
and more general claim than "R13's own floor gate is still letting
node-proximate distortion through at more nodes than we knew," which is what
the actual margin/outcome correlation in this cycle's own data most directly
supports. `NOTES.md` never explicitly reconciles these two adjacent Learned
bullets, and item 1's own qualifier ("not confined to **one** node") is
technically defensible in isolation but invites exactly the broader reading
its neighbor bullet argues against. This is squarely my seat's charter: a
signal read as "real and general" when the more careful, threshold-aware
reading is "concentrated precisely where the detection instrument is
weakest" is the same failure shape as a near-threshold visual detection
being mistaken for a suprathreshold one.

**This is not an arithmetic defect** (every number here reproduces exactly,
§1) **and it is not a vanished disclaimer** (§3) — it is a genuinely new
Phase-5-only finding (the FDTD data this table is built from did not exist
at Phase 1/2/3) about how the cycle's own headline prose characterizes its
own data. I recommend Phase-5 synthesis correct or explicitly hedge Learned
item 1 — e.g., "not confined to the single node found by exp-088" (narrowly
true) rather than "not confined to one node's immediate neighborhood" (reads
as a general claim) — and note the margin/outcome correlation as the
competing, better-supported reading, before either framing is cited into
LOGBOOK.md or PLAN.md.

## §5. Secondary, non-blocking finding — R14(a)'s smoothness gate uses a proxy tolerance where real data was available

`NOTES.md`'s Idealization 11 promises the R14(a) check runs "within **each
point's own** `box_dev` noise floor." Reading `run.py` directly: for the 3
new angles this is true (real `box_dev` computed this cycle). For the 5
historical points (36.0°/38.6°/41.8° from exp-087, 38.4°/38.8° from exp-088),
`run.py` instead uses a flat fallback, `tol = NOISE_MULT * 0.02 * v_prev`
(≈6% of the previous value) — even though I confirmed by reading
`experiments/087-.../results.json` and `experiments/088-.../results.json`
directly that the real, point-specific `box_dev` values **are** present in
both files (e.g. `C40_38.8: abs=0.00046991`). The proxy tolerance (6%) is
roughly 40×–400× looser than what the real `box_dev`-derived tolerance would
give (≈0.015%–0.14%, computed from the actual stored values).

**Non-load-bearing this cycle**: every single step in both the C40 and G40
series is a strict increase (`v_cur > v_prev` at all 7 steps, both
configs — confirmed directly from `results.json::r14a_smoothness_gate`), so
the tolerance width was never actually exercised; the gate's PASS conclusion
is correct and, in fact, stronger than claimed (genuinely monotonic, not
merely "within noise floor"). But the code does not implement what
Idealization 11 says it implements, using an available-but-unused real
input, and a future cycle where a real near-monotonic wobble occurs could
get a materially wrong PASS/FAIL call from the loose proxy rather than the
real noise floor. Cheap to fix (call the real `box_dev` dicts already loaded
from `res87`/`res88` instead of the flat 2% approximation) — worth doing
before this code path is reused a third time.

## Ranked top-3 for the Director's Iteration-67 queue

1. **Immediate, zero-cost, before any LOGBOOK/PLAN.md citation**: correct or
   explicitly hedge `NOTES.md`'s Learned item 1 (§4) — replace "not confined
   to one node's immediate neighborhood" with language that does not outrun
   the margin/outcome correlation this cycle's own data shows, and state the
   two competing readings (broad phenomenon vs. still-node-confined-but-
   under-gated) side by side rather than headlining only the more general
   one. This is the single highest-value fix on the board precisely because
   it is free and because this sub-thread's own record shows headline
   framing, not raw numbers, is what actually propagates into permanent
   citations.
2. **Sharpen NOTES.md's own "Next" item 1 (densify around 40.2°/41.4°) using
   §4's finding directly**: don't just bracket each point in isolation —
   test whether `ratio_k` decays away from 40.2°/41.4° at the *same rate*
   `frac_contrast` decayed away from 38.6° (i.e., sample the ≈0.19–0.21°
   "second-ring" neighbors of the 40.265°/41.461° crossings, mirroring
   38.4°/38.8°'s own comfortable-margin relationship to 38.590°). If both
   decay the same way, that is a decisive, cheap discriminator FOR "still
   node-confined, gate too loose" (Learned item 2) over "broadly
   distributed" (item 1's headline) — resolving §4's open reconciliation
   with real data rather than more prose.
3. **Fold in Red Team's still-queued FLOOR_FRAC recalibration, informed by
   the margin table in §4**: refit `FLOOR_FRAC` (or replace the binary gate
   with a graduated caution zone) using all 4 now-known crossings' nearest-
   neighbor margins (0.39×, 1.31×, 1.48×, 2.17×) and their outcomes, not
   just the single 38.6° data point R13 was originally calibrated against —
   a 4-point calibration set is a real, if still small, improvement over the
   1-point set the current `FLOOR_FRAC=0.10` was never actually fit to
   begin with. Secondary, cheap, zero-FDTD: fix the R14(a) smoothness gate's
   proxy-vs-real-`box_dev` mismatch (§5) before it is reused a third time.
