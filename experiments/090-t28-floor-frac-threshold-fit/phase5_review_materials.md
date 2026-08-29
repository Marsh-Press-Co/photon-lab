# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (blind) · exp-090 · Panel Iteration 67

*Fresh context, no memory of critiquing this cycle at Phase 2. Read: PANEL.md
in full; LOGBOOK.md's RULED OUT (R1–R14) in full, the ESTABLISHED section,
and LIVE THREADS/T28 in full through Iteration 66/exp-089 (both CHECKPOINT
entries at Iterations 61 and 65 read in full); the complete exp-090 cycle
record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`); exp-087/088/089's `NOTES.md`/`results.json`
for the source data this cycle reuses. Every load-bearing number below was
independently recomputed by me, from raw JSON or by re-executing the
committed function, not trusted from any prose restatement — including this
cycle's own Phase-2 critique bearing my seat's name, which I treat as a
different agent's work product to be checked, not inherited.*

## 0. Verdict

**CONCUR-WITH-GAP.**

The core deliverable — the non-parametric caution zone (Q3), Firth's
corroborating fit (Q4), and the distance-to-crossing regressor comparison
(Q8) — is sound, correctly scoped, and independently over-verified (by all
five Phase-2 critiques, Red Team's Phase-2 audit, and the Director, before
this review; I re-confirm the same numbers below by a sixth/seventh/eighth
independent route). The disclosure discipline this program has spent
fourteen standing rules building (R3 spatial-resolution gaps, the
dual-section idealizations banner, sample-curation caveats) was correctly
applied per Red Team's nine-item docket. **But one genuine, previously
uncaught defect survived eight independent verification passes (five
Phase-2 critiques, Red Team's Phase-2 audit, the Director's own
pre-freeze check, and the committed run itself) into the document now
sitting in front of Phase 5**: `NOTES.md`'s own Result section describes
the naive-MLE divergence diagnostic (Q1) as occurring "after 2000
Newton–Raphson steps, still climbing" — a claim that does not reproduce
from the actual committed `run.py`. This is non-load-bearing (Q1 is
explicitly a diagnostic, not a scored prediction, and the qualitative
conclusion — the naive MLE diverges without a finite optimum — is
correct) but it is exactly the shape this program's R4 lineage exists to
catch, and it sits alongside a second, related, wholly unreconciled
number in `phase3_synthesis.md` itself. Both are named in full below,
with a same-shift fix recommended. Neither changes the Combined Verdict
or any PRIMARY (Q3/Q4/Q8) finding.

## 1. Independent reproduction — spot-checks against raw JSON/code (R4/R9 discipline)

I did not trust any cited figure without recomputing it myself, from the
committed artifacts, before writing anything below.

| Quantity | My independent computation | Cited (NOTES.md/results.json) | Match |
|---|---|---|---|
| `FLOOR = 0.10 × RMS[frac_contrast]` | `1.9174375118374476×10⁻⁴` | `1.91744×10⁻⁴` | exact |
| `margin(41.4°) = frac_contrast/FLOOR` | `2.510967422703893×10⁻⁴ / 1.9174375118374476×10⁻⁴ = 1.309543...` | `1.309543287435571` | exact |
| Zone `[1.4764, 2.1709]` and gap ratio (`upper/lower`) | `2.170947121651026/1.4763877483857824 = 1.470445...` | `1.4704450941323812` | exact |
| Q7 recomputed resolved-margin, 37.2° | `noise_floor = 3.0×0.00045691305539087×2.8127043563514567×10⁻¹² = 3.8555×10⁻¹⁵`; `Δp_abs = |2.808672836407139×10⁻¹² − 2.8127043563514567×10⁻¹²| = 4.0315×10⁻¹⁵`; `margin = 1.04566` | `1.0456585785601518` | exact |
| Q8 zero-crossings + nearest-distance table, all 7 angles | recomputed by linear interpolation of `j083["delta_scene"]` against `j083["thetas"]`, matching `run.py::find_zero_crossings` line-for-line | `[37.1272, 38.5902, 40.2654, 41.4609]`; distances `0.0609…1.1272` | exact |
| Q8 gap ratios (`distance` vs `margin`) | `0.07275362.../0.06541960... = 1.112107`; margin's own `1.470445` | `1.1121073393138168` / `1.4704450941323812` | exact |
| AUC(margin) rank separation | by inspection: both `Y=1` margins (`1.3095`,`1.4764`) strictly below all five `Y=0` margins (`2.1709`–`8.0187`), no ties | `AUC=1.0` | confirmed |

Everything PRIMARY (Q3, Q4, Q8) and every disclosure-gate number (Q7)
reproduces bit-exact from the raw JSON. This is the same conclusion five
Phase-2 critiques and Red Team's audit already reached — I am adding an
eighth/ninth independent confirmation, not correcting any of it.

## 2. A genuine, previously-uncaught defect: Q1's "2000 Newton–Raphson steps" does not reproduce

I re-implemented `naive_mle_diverges()` from `run.py` verbatim and ran it
against the committed 7-point `margin`/`Y` data to see exactly how the
cited `β=(26.11,−103.01)` is reached:

```
beta = [ 26.11462482 -103.01357742]  diverged = True
stopped at iteration index 10 (0-based) -- i.e. after 11 Newton-Raphson steps
```

This is bit-exact to `results.json::q1.naive_mle_beta` and to
`run_output.txt` — so the **number** is right. But `NOTES.md`'s Result
section states: *"Naive unpenalized MLE diverges (`β=(26.11,−103.01)`
after 2000 Newton–Raphson steps, still climbing)"* (line 251). Reading
`run.py::naive_mle_diverges()` itself: the loop returns **immediately**,
inside the `for` loop, the first time `np.max(np.abs(beta)) > blowup`
(`blowup=100.0`) — it does not run to `max_iter=2000` and then report
whatever it finds; it exits as soon as the blowup guard fires, which my
trace above shows happens at iteration 11, not 2000. **"After 2000
Newton–Raphson steps, still climbing" misdescribes the actual computation
by roughly two orders of magnitude in iteration count** — the real
behavior is a fast, decisive blowup within eleven steps, not a slow climb
that is merely still ongoing when an arbitrary ceiling is reached. The
*qualitative* claim this diagnostic exists to support (the naive MLE has
no finite optimum on perfectly-separated data) is unaffected — my own
trace confirms the divergence is real and immediate, if anything a
*stronger* demonstration of the hazard than "still climbing after a long
run" would be — but the specific runtime narrative in the permanent
record does not reproduce from the code that produced the number sitting
next to it.

**A second, related, wholly unreconciled figure compounds this.**
`phase3_synthesis.md`'s own "Director's own independent verification"
section — written specifically to confirm every proposal number
*before* freezing anything — states: *"Naive (unpenalized) MLE: diverges
as predicted — 2000 Newton–Raphson steps drive `β→(65.0, −256.8)` and
climbing"* (line 25). This is a **third, different beta** from the same
nominal computation: `(65.0, −256.8)` matches neither the Phase-1
proposal (which states no specific number), nor the final committed
`run.py`/`results.json`/`NOTES.md` figure (`26.11, −103.01`), nor my own
from-scratch re-implementation of the committed function (which
reproduces `26.11, −103.01` exactly). The Director's own throwaway
pre-freeze script evidently used a different divergence criterion or no
blowup guard at all — and this discrepancy between the Director's own
cited "independent verification" number and the number the committed
pipeline actually produces was never reconciled or flagged anywhere in
the record, unlike every OTHER number in this cycle (Firth's `m₅₀`, the
permutation `p`, the LOO table, Q8's crossings), each of which was
explicitly cross-checked digit-for-digit across five to nine independent
parties before this review.

**Why this matters, stated precisely.** Q1 is explicitly scoped
"diagnostic, not scored" (Idealizations 6/7/13 apply, and Q1 makes no
falsifiable claim per `phase3_synthesis.md`'s own frozen spec) — so this
does **not** touch the Combined Verdict, does not touch Q3/Q4/Q8, and is
not outcome-determining for anything this cycle certifies. But it is
precisely the shape R4 and its addenda (Iterations 25, 50, 51) name: a
descriptive claim about a computation's own mechanics ("after 2000
steps"), and a distinct "verification" figure cited as confirming a
result, that do not reproduce from the actual committed function when
independently re-run. That eight parties (five Phase-2 critiques, Red
Team's Phase-2 audit, the Director's own Phase-3 verification pass, and
the committed script itself) all handled this exact diagnostic without
anyone tracing the iteration count or reconciling the Director's own two
cited beta values is worth naming plainly: every one of those parties
checked the numbers that were SCORED (Q3, Q4, Q8) far more thoroughly
than the one explicitly marked "not scored" — a reasonable prioritization
in the moment, but the gap should not go unrecorded now that a Phase-5
seat has found it.

**Recommended fix (same-shift, zero-cost, non-blocking):** correct
`NOTES.md`'s Q1 Result line to state the true behavior — e.g., "diverges
decisively: the blowup guard (`|β|>100`) fires after only 11
Newton–Raphson steps (β=(26.11,−103.01)), not a slow asymptotic climb" —
and add a one-line reconciling footnote to `phase3_synthesis.md` noting
that its own pre-freeze throwaway figure (`65.0,−256.8`) used a
different, uncommitted divergence check and does not itself need to
match the final committed number, since Q1 was never a frozen,
falsifiable prediction requiring bit-exact Director/Phase-4 agreement the
way Q4 and Q8 were.

## 3. My own Phase-2 critique's R3 spatial-resolution gap: disclosed, adequately, with one carry-forward softness

This cycle's own MATERIALS Phase-2 critique (a different fresh agent, not
me) flagged that the n=7 `frac_contrast` values — especially 40.2°/41.4°,
which set the caution zone's own **lower** edge — have never passed an
R3-mandated spatial (`cpl`) resolution check on this channel, and that
this gap is undischarged going on three cycles (exp-088, exp-089, now
exp-090). I independently confirm the underlying physical concern is
real and correctly targeted: `grep`-ing `phase1_proposal.md` for
"R3"/"resolution" returns nothing, and `VALIDATION.md` line 319 ("λ/20
resolution staircases the tensor") independently corroborates that
resolution sensitivity is the default expectation on this bench, not an
exotic risk — Red Team's own citation of this line checks out verbatim.

**Was it disclosed as required?** Yes. `NOTES.md` carries it as
Idealization 9 ("The n=7 `frac_contrast` values — especially 40.2°/41.4°,
which set the zone's own LOWER edge — have not passed an R3-mandated
spatial (`cpl`) resolution check on this exact channel... undischarged
two cycles running as of exp-089 and remains undischarged here"), cited
inline at Q3's own Predictions-section entry ("Idealizations 6/7/13,
9-11 apply"), and restated as Next item 1 ("undischarged three cycles
running as of this document"). This is a real, load-bearing, correctly
targeted disclosure — adequate as filed.

**One softness, worth naming but not blocking.** Q3's Predictions-section
entry cites "Idealizations 6/7/13, 9-11" inline; Q3's own Result-section
entry ("caution zone = `[1.4764, 2.1709]`, width `0.6946`... bit-exact as
predicted") carries no inline idealization citation at all — only the
Result section's own top-level banner (6/7/13) applies generically. This
is a strictly milder version of the exact "banner scoped to one section
fails to propagate to the parallel section" shape that fired Checkpoint
criterion 4 at Iteration 65 — milder because the mandatory NETD/
constraint banner itself (6/7/13) IS present in both sections, and only a
*supplementary*, this-cycle-specific idealization number (9, plus 10/11)
drops from the Result section's per-item citation. I do not think this
rises to a fresh instance of the disclaimer-erosion lineage (the general
banner rule is satisfied), but it is a genuine, real asymmetry a future
citation of Q3's Result line alone (without the Predictions section
alongside it) would miss. Recommend: future T28 documents extend the
"restated inline at each item, not stated once and dropped" convention
explicitly adopted for the Predictions section to the Result section's
own per-item entries too, not just its top banner — closing this gap
before it has the chance to compound the way the NETD/constraint-3
omission did across Iterations 53/63/64/65.

## 4. Charter question: FLOOR/RMS/zone/`m₅₀` scope-specificity — correctly and consistently carried, one new connective finding

`graded_black_shell`/600nm scope-specificity (Idealization 3) is stated
in the parameter table's "Reuse convention" row, restated at Idealization
3, and re-invoked at Idealization 5 (`FLOOR_FRAC`/`NOISE_MULT` as
inherited house-style constants, not re-derived). I confirm this scope is
carried correctly through **both** of this cycle's new sections: Q7
(37.2°'s resolved-gate margin is computed from `graded_black_shell`/600nm
primitives specifically, same article/config as everything else in the
document) and Q8 (the distance-to-crossing comparator is built entirely
from `exp-083`'s own 31-point window — the identical article/wavelength,
never a different one). No cross-material or cross-wavelength leakage
anywhere in the document; I find no place where the zone, `m₅₀`, or Q8's
gap ratio is invoked, even implicitly, as if portable to a different
absorber or λ.

**New finding, this seat's own lens, not raised by any Phase-2 critique
or Red Team's audit:** Idealization 11 (Red Team's RT-2 fix — the n=7
population is a crossing-proximity-enriched sample, not a representative
draw) deserves an explicit cross-reference this document does not yet
make. Every one of the four `delta_scene` zero-crossings this fit's own
Q8 locates (`37.13°, 38.59°, 40.27°, 41.46°`) is a feature of the
`C40`/`G40` config pair this program's own exp-076 already proved,
independently and rigorously (`PAD` is provably lossless vacuum — the
damping-mask construction has zero dependence on domain padding), to be
a **coherent propagation-phase/domain-geometry artifact, not an
absorption or material effect** — MATERIALS' own Iteration-59 "zero
realizability content" framing rule, already established and reaffirmed
at every T28 desk cycle since. This means the caution zone's own
*edges* — not merely the raw `ratio_k` signal the zone gates — are built
entirely from angles selected for proximity to a domain-geometry
artifact's zero-crossings, not from any physically-motivated material
absorption feature. This does not change anything this cycle claims (no
realizability content was ever asserted here), but it sharpens
Idealization 11 in a way worth stating explicitly in a future citation:
this calibration's own **support** (the specific angles informing the
zone) is drawn entirely from the neighborhood of a known non-physical
artifact, so `FLOOR_FRAC`'s eventual recalibration (queued repeatedly in
this sub-thread's own Next sections) inherits not just an
article/wavelength scope restriction but an artifact-class restriction —
it characterizes how this instrument behaves near a `PAD`-echo-driven
zero, not how it would behave near a genuine material-absorption feature
were one ever found. Recommend naming this explicitly, once, the next
time `FLOOR_FRAC` itself is recalibrated (not urgent for this cycle,
which correctly declines to recalibrate it).

## 5. Minor, non-blocking observation: a small counting drift in the "consecutive cycles deferred" figure

`NOTES.md`'s Next item 3 states the x-wall wavelength-generality leg is
"now **SIXTEEN** consecutive cycles deferred (076–090)." Counting
inclusively, exp-076 through exp-090 spans 15 experiments (090−076+1=15),
not 16. Tracing this back through LOGBOOK.md, the count is internally
consistent (each successive T28 cycle increments the prior cycle's own
cited figure by exactly one) back to Iteration 64/exp-087, which
correctly states "TWELVE... (076–087)" (87−76+1=12, correct) — but
Iteration 65/exp-088 then states "FOURTEEN... (076–088)" (88−76+1=13,
should be THIRTEEN), an apparent one-count jump that has propagated
unchanged, incrementing correctly by one each cycle since, through
exp-089's "FIFTEEN" and now exp-090's "SIXTEEN." This is a trivial,
purely rhetorical figure (it gates no decision and scores nothing) and I
am not recommending any Checkpoint action on it — but it is a small,
real instance of exactly the "restated, not independently recomputed"
pattern R4's own addenda target, now three cycles old, and cheap to fix
(one arithmetic correction) whenever this line is next touched.

## 6. Other checks performed, no issues found

- Q6 (out-of-sample 38.6°): `margin=0.3865`, `P(Y=1)=0.9838` — I
  independently re-evaluated the fitted Firth logit at `log₁₀(0.38646)`
  using the committed `β=(1.78059,−5.63152)` and reproduce `0.98379`
  exactly.
- Q5 (LOO jackknife): QUANTUM's Phase-2 order-statistics argument (that
  every LOO outcome is a deductive consequence of Q1's tie-free
  separation, not new information) is correct and I confirm it requires
  no computation to verify — a subsequence of a strict total order stays
  strictly ordered, and a min/max order statistic is invariant to
  removing any point other than the current argmin/argmax. Phase 3's
  reclassification of Q5 (and Q2) from "falsifiable predictions" to
  "diagnostic sanity checks" is the correct fix and is applied
  consistently throughout the final document.
- The "D"-class (ENERGY-DECOUPLED) scope exclusion (Idealization 4) is
  honored throughout — no place in the document treats this as a 3-class
  calibration.
- Checkpoint criterion 2: correctly N/A throughout (T1 route N/A, no
  mechanism-class claim, matching every T28 desk cycle since exp-069).
  No REALIZABILITY_MEMO.md reopening anywhere.

## 7. Ranked top-3 candidate directions for Iteration 68 (from my own charter's lens)

1. **The R3 spatial (`cpl` 20→30) resolution check on the
   `frac_p_abs`/`ratio_k`/`frac_contrast` channel**, specifically at the
   two points that set this cycle's own zone's lower edge (40.2°/41.4°)
   plus the fragile 37.2° upper-edge point (Q7). This is the single
   cheapest, most information-dense next step: it is undischarged three
   cycles running (exp-088/089/090), it directly validates or
   invalidates the numerical inputs the caution zone itself is built
   from, and every prior cycle's own Phase-5 review (including my seat's
   at exp-088 and exp-089) has already ranked it #1 or top-2 without it
   running.
2. **A repeat or denser FDTD measurement at 37.2° specifically**
   (`NOTES.md`'s own Next item 5). This one angle is simultaneously the
   caution zone's own upper-edge anchor, Firth's most load-bearing
   C-class point, and an independently-flagged "felt-lucky pass" at its
   own separate `resolved`-gate margin (1.0457×, this cycle's own Q7
   finding, independently reconfirmed by me in §1 above) — resolving its
   own reliability with one concrete measurement outranks any further
   desk-only recalibration of the zone built on top of it.
3. **The x-wall wavelength-generality (450/750nm) leg** — the single
   oldest, most consecutively-deferred item on the whole T28 board (15
   cycles by my own corrected count, §5). From this seat's own
   realizability-bound charter: every scope caveat this entire T28 desk
   sub-thread carries, this cycle's `FLOOR`/`RMS`/zone/`m₅₀` included, is
   pinned to `graded_black_shell`/600nm specifically; until this leg
   runs, none of it can be said to generalize even within this program's
   own established 3-λ sweep, let alone to a genuinely different
   material.
