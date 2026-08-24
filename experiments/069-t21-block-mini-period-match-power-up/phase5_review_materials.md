# PHASE 5 — REVIEW · Panel Iteration 46 · Seat: MATERIALS & METAMATERIALS

*Fresh sub-agent, MATERIALS & METAMATERIALS charter, blind to any other
seat's Phase-5 review this cycle, per PANEL.md's independence mechanics.
Reviewing exp-069 (Block MINI's period-match test, powered up) against
this program's full process record and my own Phase-2 critique's demands,
independently re-derived where possible rather than restated.*

## 0. What I independently re-verified, and how

This is instrument/model-fidelity work (T1 route N/A) — my seat's
realizability bound is not directly engaged, so I spent my review budget
on (a) re-checking whether my own Phase-2 demand was actually honored in
the committed artifacts, not just claimed to be; (b) independently
recomputing the headline statistics from the raw `results.json` data,
since a fresh eye re-deriving a number from source is worth more than
re-reading a table; and (c) auditing the cost arithmetic and its
reconciliation against the actual run, per my assignment.

**Recomputed independently from `results.json`'s raw `block_dense` rows**
(own script, not copy-pasted from any committed file):
- P-069-1: `ptp=0.0040263, mean=-0.0002485, ratio=16.2003` — **bit-exact
  match** to the committed `16.200320424677294`.
- P-069-2: fixed-`T=20/752` fit, `R²=0.2016` — **bit-exact match**.
- P-069-3: free-period grid search (had to correct my own first attempt —
  the code converts a candidate `P*` in *linear-θ-at-39°* convention into
  a *sinθ*-period via `Tc = radians(P*)·cos(39°)`, not a period directly in
  sinθ units; once I matched that convention, `P*=2.8421°, R²=0.6272`
  reproduced **bit-exact**, and is stable — I swept the search bound out to
  20° and the same optimum re-emerges every time, so this is a genuine
  global optimum over the physically sensible range, not a boundary
  artifact or a search-grid coincidence).
- P-069-4, P-069-5, and G-1: hand-checked against the raw cell values —
  all reproduce exactly; G-1's four reference values were independently
  pulled from exp-065's own committed
  `settled_sweep_steps2800_diagnostic.json` and match bit-for-bit.

**Conclusion: the headline result is real, not a computation error, not a
search-range artifact, and not fabricated.** T28 (a genuine, resolution-
robust, settled ~2.84°-period oscillation in the `C80−C40` padding delta
that does not match T21's own predicted ~1.96° period) is a solid finding
on its own numbers. This matters for my seat specifically because it is
the kind of surprising-but-verified result that could tempt a later cycle
into premature materials-realizability language before its mechanism is
pinned — see §3.

## 1. R_contact disclosure — my own Phase-2 mandatory fix 9, checked in the committed text

**Properly done, not merely claimed.** I checked the actual committed
artifacts, not the process narrative:

- `NOTES.md` Idealization 9 (line 92-96): states plainly R_contact
  "remains untouched this cycle... still blocked on WebSearch/WebFetch
  tooling, not picked up in parallel despite PLAN.md's explicit
  invitation."
- `NOTES.md`'s own "Next" section (line 197-198): repeats the disposition
  at the close of the document, where a reader scanning only the end would
  still see it.
- `results.json`'s own `r_contact_disposition` field (line 511): a
  machine-readable disposition, not just prose — this is a genuine
  improvement over some earlier cycles' pattern of disclosing a deferral
  only in NOTES.md prose. It is worded consistently with the NOTES.md
  text, not a paraphrase drift.
- `phase4_results.md`'s own dedicated "R_contact" section (line 100-103)
  repeats it a third time at the results-artifact level.

Three independent, consistently-worded sites, one of them machine-readable
— this is a stronger disclosure than my own Phase-2 critique actually
demanded (one sentence). No overclaim, no silent narrowing. **Confirmed
clean.**

## 2. Cost arithmetic: the 32.5-min prediction was reasonable, but the "2.2× faster" explanation in `phase4_results.md` does not survive a block-level check

I reran `design_geometry.py::fdtd_budget()` directly (`python3
design_geometry.py`) rather than trusting the quoted numbers, and it
reproduces the committed prediction exactly: **100 calls, 6637.3 CPU-s,
wall=32.45 min, 3× envelope=97.36 min** — matching NOTES.md/
`phase3_synthesis.md`'s "100 calls, ≈6637 CPU-s, wall ≈32.5 min, 3×
envelope ≈97.4 min" to the reported precision. The arithmetic is sound and
reproducible from committed code, not hand-typed (house rule R4 honored).

The actual run: **100 calls, 885.8s (14.76 min)** — a real number, not
disputed; `sum(block elapsed_s)` = 428.37+65.29+163.68+228.47 = 885.81s,
matching `total_elapsed_s` to rounding. `phase4_results.md`'s own line 1-6
is honest that a gap exists and offers a stated reason ("actual ran ~2.2×
faster... `CPU_S_PER_CALL`'s own contention figures were measured under
different concurrent load than this shift's") — **this is disclosed, not
silently absorbed**, which is the literal thing I was asked to check, and
on that narrow question the cycle passes.

**But the offered explanation does not hold up against the cycle's own
per-block data**, and nobody checked this at any phase. If lower
concurrent load/contention were the uniform cause, every block running
under the same `ProcessPoolExecutor(max_workers=4)` should show a roughly
similar speedup ratio. Computing each block's *predicted* wall-clock
component from `fdtd_budget()`'s own formula (`overhead×cpu/(workers×eff)`,
applied per-block using the block's own `cpu_s`) and comparing to its
*actual* `elapsed_s`:

| Block | n_calls | predicted wall (s) | actual `elapsed_s` | ratio (pred/actual) |
|---|---|---|---|---|
| DENSE | 62 | 1087.7 | 428.37 | **2.54×** faster |
| SETTLE-C80 | 2 | 61.3 | 65.29 | **0.94×** — actually *slower* than predicted |
| R3 | 4 | 236.8 | 163.68 | 1.45× faster |
| LEG750 | 32 | 561.4 | 228.47 | **2.46×** faster |

The two large-batch blocks (DENSE, LEG750) show closely-matched ~2.5×
speedups, consistent with a genuine lower-contention story. But
SETTLE-C80 — 2 calls only — shows **no speedup at all** (if anything,
slightly slower than predicted), and R3 (4 calls, exactly `n_workers`)
sits at an intermediate 1.45×. A uniform "less contention this shift"
cause predicts a uniform ratio across all four blocks; it does not predict
this monotonic call-count dependence.

The much more likely mechanism, never tested by the design or the
results write-up: `fdtd_budget()`'s wall formula divides total CPU by
`n_workers=4` unconditionally, which is the correct approximation **only
when the batch has many more tasks than workers** (so the pool stays
saturated). For SETTLE-C80 (2 tasks, 4 workers), the true wall floor is
close to a *single call's* CPU time, not `total_cpu/4` — the formula
structurally under-*predicts* wall for that block, which is exactly what
the data shows (predicted 61.3s came out too low, not too high, unlike
every other block). For R3 (4 tasks = `n_workers` exactly), the formula
is at its own break-even point, and the residual 1.45× likely reflects
genuine per-call speedup superimposed on a smaller batch-fill effect.

**This is a real, previously-uncaught gap: the "2.2× faster, lower
contention" explanation in `phase4_results.md` is an aggregate story that
happens to fit the two large blocks and is contradicted by the smallest
one, and no one — not the Phase-1 design, not the Red Team audit (which
only reviewed the *predicted* budget, correctly, before any run occurred),
not `phase4_results.md` itself — checked the explanation against the
block-level breakdown that was sitting in the same `results.json` file
the whole time.** It does not change any scored verdict (all five
predictions and G-1 are computed from the physics data, not the timing
data), and it does not threaten the hard-stop discipline (14.76 min
finished nowhere near either the 75-min or 100-min stop). But it is a
concrete, fixable defect in this cycle's own explanation of its own
numbers, of exactly the "asserted, not re-verified" species this program
has burned real Checkpoint cycles on before (e.g. Iteration 39's
CHECKPOINT #2, where a "the fix already covers it" claim wasn't actually
checked against the file it should have covered). I recommend a one-line
correction at Iteration 47's docket: `fdtd_budget()`'s wall estimate is
only valid for batches with `n_calls >> n_workers`; small legs (≤`n_workers`
tasks) should be estimated as roughly single-call CPU time, not
`total_cpu/n_workers`. Low cost, closes a real gap, does not touch any
physics.

## 3. T28's own write-up: stays properly descriptive, does not drift toward realizability language

Checked `phase4_results.md`'s "New live thread — T28" section (line
81-98) and the "Learned" items in `NOTES.md` against my own charter's
standard (does anything here imply a real material could realize this
behavior, or does it stay a statement about the simulated Huygens-source
geometry?).

**Clean.** The section explicitly frames T28 as a question about the
`ABSORB`-boundary/aperture-geometry `Sim` construction, not a material
property: candidate mechanisms offered are "a boundary-thickness-scale
mechanism specific to the `ABSORB` band itself" and "a genuinely new
candidate mechanism requiring its own Phase-1 proposal" — both scoped to
the simulated construction, with zero reference to any real material,
absorber, or metamaterial structure anywhere in the section. It explicitly
states "no constraint-3 verdict is implicated" and explicitly *declines*
Checkpoint-criterion-2 candidacy ("T28 is a real, unresolved mechanism
question, not yet a proven mechanism-class boundary") — the correct,
conservative call; nothing here has been shown to be a *mechanism*, let
alone a mechanism-class boundary a realizability bound could attach to.
`NOTES.md`'s Idealization 5 (inherited verbatim from Phase 1, never
weakened) keeps the load-bearing hedge in place: the period-match
statistics test *consistency with* T21's own established model, not an
independently-verified ground truth, and a REFUTE outcome is disclosed as
not ruling out an unmodeled periodic mechanism, not claimed to positively
identify one. My own charter's realizability-tier language (published /
plausible / unobtainium-with-parameters) is correctly never invoked here
— there is no material claim of any kind to bound. **No drift found.**

## 4. Process-completeness gap this cycle should have caught and didn't: a stale, unwidened caveat-lint registry entry

This is the one substantive gap I found that no phase of this cycle
addressed, and it is squarely in the "caveat propagation / registry
entries" category I was asked to scrutinize.

`lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-plane-channel`
entry — the registry entry that has tracked Block MINI/`P-VIS42-10`'s
open-vs-closed status across three prior cycles (widened at Iteration 43
close and again at Iteration 45 close) — **still reads, verbatim, in its
committed description text**: *"P-VIS42-10 (Block MINI's period-match
test) remain[s] RETRACTED/UNDECIDED pending re-verification... Block
MINI's period-match test (P-VIS42-10) remains untouched by exp-068
(explicitly out of scope...) and STILL UNDECIDED."* That is now **false**:
exp-069 formally retired `P-VIS42-10` this cycle (`Combined Verdict:
FORMAL_RETIREMENT_NON_DECISIVE`). The entry's `required_sites` list (four
files, all from exp-065/exp-068) was never widened to add exp-069's own
`NOTES.md`/`phase4_results.md`, and its description was never updated to
record the retirement.

I ran `lab/caveat_lint.py` directly to check whether this is a live tool
failure: **it is not** — `13 caveat(s) checked, 0 required-site
failure(s)`, exit 0. But this is a false-negative, not a clean bill of
health: exp-069's `NOTES.md`/`phase4_results.md` both happen to contain
the string `"0.827"` (from the R²=0.7852→0.8271 citation, a real but
unrelated fact), which satisfies one of this entry's `phrase_patterns`
regexes by coincidence and suppresses the tool's WARN output for those
files. `lab/caveat_lint.py`'s own docstring is explicit that it "has no
opinion on whether any measurement is correct" — it is a substring
checker, not a truth checker, and this is exactly the class of gap it
cannot catch on its own: a **stale description**, not a missing phrase.

Concretely, this means: any future cycle or fresh Phase-5/Phase-1 agent
that reads this registry entry (rather than the primary NOTES.md chain)
for Block MINI's status will be told, in a program-of-record registry
file, that Block MINI is "STILL UNDECIDED" — one cycle after it was
formally, deliberately, and correctly retired. That is a real
stale-caveat risk of the same species this program fired Checkpoint
criterion 4 on at Iterations 37, 39 (twice), and 40. It is not itself a
Checkpoint-4-caliber event this cycle (no live citation of the stale text
has occurred yet, and the false-negative is a tooling limitation rather
than a violated disclosure promise), but it is a concrete, disclosed,
fixable gap that belongs in Iteration 47's mandatory-fix docket: update
the entry's description to record the retirement, and widen
`required_sites` to include exp-069's `NOTES.md`/`phase4_results.md` so
future edits to those files are actually checked.

## 5. Everything else I checked and found clean

- **Mandatory-fix docket (10 items, my own R_contact item among them):**
  spot-checked against the actual committed code/text for items 1 (P-069-4
  wired as a binding conjunct in `run.py::score()`'s `coherent` boolean —
  confirmed by reading the line directly), 3 (five-way conjunction,
  confirmed), and 4 (the non-decisive branch fires exactly as specified,
  confirmed by the combined-verdict trace above) — all landed as claimed,
  not just asserted.
- **`A=752`/`A_r3=1128` congruent-construction assertions**
  (`design_geometry.py` lines 114, 217-218) are live `assert` statements,
  not comments — they would have hard-failed the run if violated, not
  merely documented an assumption.
- **The §1 misattribution correction** (exp-066→exp-065, mandatory fix 8):
  checked `NOTES.md`'s desk-check section — the corrected attribution is
  present and exp-066 is not credited with testing `C80` anywhere in the
  committed text.

## Verdict: **PROMISING**

Not "promising" toward the phenomenon program's own constraints — this is
explicitly T1-N/A instrument work — but promising as *process*: this is
the strongest single piece of engineering discipline this specific
four-cycle-deferred instrument has ever received, it honored its own
pre-committed non-decisive-outcome rule under real pressure (a genuinely
ambiguous result that a weaker design could have argued into another
deferral), and every number I independently re-derived came back
bit-exact. R_contact's disclosure (my own Phase-2 demand) is honored more
strongly than I asked for. The two gaps I found (the cost-arithmetic
explanation and the stale registry entry) are both real, both concrete,
both cheap to fix, and neither threatens the headline finding or any
scored verdict — they are the kind of thing a fresh Phase-5 pass exists to
catch, not evidence the cycle was undisciplined.

## My ranked top-3 candidate directions for Iteration 47 (own charter, not PLAN.md restated)

**1. Close the registry staleness from §4 as a zero-cost rider, same-shift
as whatever else Iteration 47 does.** This is the cheapest possible
process fix in this review — update one JSON entry's description field
and widen one `required_sites` list — and it directly prevents the exact
failure mode (a stale caveat cited as current) that has cost this program
multiple Checkpoint firings. It requires zero FDTD, zero rotation-slot
competition, and should not wait for a dedicated cycle.

**2. T28's mechanism, from MATERIALS' own angle: is the ~2.84° period
consistent with the *taper* (`TAPER=40` cells) acting as its own,
separate diffracting aperture, rather than the full A=752-cell half-
aperture?** T28's write-up (correctly) leaves the mechanism open and
offers boundary-thickness and "new candidate" hypotheses, but never
proposes the simplest structural candidate a MATERIALS/METAMATERIALS lens
would reach for first: a raised-cosine taper region has its own
characteristic length (`TAPER=40` cells, ~5.3% of A), and a *second*,
shorter-period Huygens-type fringe from an effectively-narrower radiating
sub-aperture (e.g. the taper's own transition zone, or the `ABSORB`
band's own physical width) is a structurally motivated, cheap-to-test
candidate: recompute `P_deg`-style formulas using `TAPER` or `ABSORB`
band width in place of `A` and check whether either lands near 2.84°
before proposing a full new Phase-1 mechanism cycle. This is desk-only
arithmetic, zero FDTD, and could either close T28 immediately or sharpen
what a future FDTD test should isolate.

**3. R_contact's literature search, unblocked the moment WebSearch/
WebFetch tooling clears — still the only queue item that can move a real
materials number.** This is PLAN.md's own item 2, but I rank it my #2-vs-3
independently: three consecutive cycles of correct, disciplined,
zero-content disclosure is not the same as progress, and it remains the
single highest-value materials question this program has open
(`REALIZABILITY_MEMO.md` Entry 3, TD-5's margin literally undetermined
between two >4×-disagreeing endpoints). I rank it third here only because,
unlike items 1-2, its blocker is tooling availability, not agent
attention — it cannot be advanced by argument alone, so it is not
"ranked" in the sense of competing for a rotation slot, only in the sense
of standing readiness the moment it can move.
