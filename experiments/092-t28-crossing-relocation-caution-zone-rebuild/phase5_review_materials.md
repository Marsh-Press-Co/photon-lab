# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (fresh context) · exp-092 · Panel Iteration 69

*Fresh sub-agent, no memory of any prior cycle. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15 in full, ESTABLISHED, and the complete T28
live thread from its Iteration-46/exp-069 opening through Iteration-68/
exp-091's close, both CHECKPOINT entries in that span); the complete
exp-092 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`results.json`, `run_output.txt`); exp-091's own full record including my
own seat's prior-cycle self-review (`phase5_review_materials.md`,
`results.json`) and its `phase5_redteam_audit.md`; `lab/materials.py`
(`graded_black_shell`, `pec_disk`); `experiments/034-.../REALIZABILITY_
MEMO.md` Entry 2 (checked specifically for a possible connection to this
cycle's own `sigma_max` correction, §4 below). This is a blind review — I
have not read any other seat's Phase-5 file for this cycle. Every load-
bearing number below was recomputed by me from `results.json`/`run.py`
directly, not copied from `NOTES.md`'s prose.*

## 0. Verdict

**CONCUR-WITH-GAPS.**

Rank 3's CONFIRM verdict is correctly computed, and I independently
reproduce all six raw (ratio, sign_match) cells bit-exact (§1). The
resequencing fix, the `sigma_max_R3=1/3` derivation, and the empty-leg
re-run-not-reuse fix are all correctly implemented in `run.py` exactly as
`phase3_synthesis.md` specifies (§2). But two things in this record are
not what they present themselves as. **First**, "CONFIRM, cleanly" is true
of the six cells actually measured, but the write-up's own forward-looking
language ("Rank 1's own results below are therefore directly comparable to
exp-091's own filed `cpl=20` data with no sigma-scaling caveat") reads as
broader than what was tested: Rank 3's three census angles do not include,
or sit anywhere near, the genuinely new and far more fragile structure Rank
1 itself discovers this same cycle — a near-total interference null
straddled by two crossings 0.057° apart, with a `delta_scene` magnitude
roughly an order of magnitude smaller than anything Rank 3 checked. The
three tested ratios (0.92–1.18) show no clean trend with distance-to-
crossing that would license confident extrapolation into that much more
extreme regime either way (§2). **Second**, a genuine, previously-uncaught
data-completeness defect: `results.json::rank1.crossing_report` persists
only the *first* of the two upper-window crossings `run.py` itself finds
and correctly counts (`len(upper_crossings)=2`, driving the correct NEITHER
verdict) — the second crossing (`41.8377°`) exists only in
`run_output.txt`'s stdout and in `NOTES.md`'s own hand-transcribed table,
not in the committed JSON a future cycle would normally build from (§5).
Iteration 70's own top-ranked queue item explicitly proposes rebuilding
R15's caution zone from "the two newly located `cpl=30` crossings (or
three, counting the upper pair separately)" — exactly the number this JSON
field cannot currently supply. Neither gap changes this cycle's own scored
verdicts (§1 confirms every number filed); both are real, cheap-to-fix,
and load-bearing for what comes next.

## 1. Independent reproduction — the six raw Rank-3 cells, recomputed from `results.json` myself (R4/R9 discipline)

I did not trust the printed ratios; I recomputed each directly from the
`sigma_corrected_*`/`filed_*` pairs in `results.json::rank3.per_theta`.

| θ | `delta_scene` ratio (mine / filed) | sign_match | `frac_contrast` ratio (mine / filed) | Cell verdict |
|---|---|---|---|---|
| 37.2° | `0.0011506212/0.0012470908 = 0.922644` / `0.922644` | filed `+`, corrected `+` → **True** | `0.0020290098/0.0021626774 = 0.938193` / `0.938193` | inside `[0.3,3.0]` both |
| 40.2° | `0.0004431720/0.0004369899 = 1.014147` / `1.014147` | filed `+`, corrected `+` → **True** | `0.0008087580/0.0007877482 = 1.026671` / `1.026671` | inside `[0.3,3.0]` both |
| 41.4° | `0.0006593351/0.0005625525 = 1.172042` / `1.172042` | filed `+`, corrected `+` → **True** | `0.0012311296/0.0010409190 = 1.182733` / `1.182733` | inside `[0.3,3.0]` both |

All six cells reproduce to the printed digit; `ratio_sign_verdict` (`sm
and all(0.1<=r<=10)` REFUTE-gate, `all(0.3<=r<=3.0)` CONFIRM-gate — read
directly from `experiments/091-.../run.py:253-263`, reused verbatim, no
edits) correctly returns CONFIRM for both `delta_scene` and
`frac_contrast` sub-verdicts, so the overall R3 verdict (worst-case across
both) is correctly CONFIRM. `SIGMA_R3_CORRECTED = 78.0/(2*117) =
0.333333...`, asserted `abs(...-1/3)<1e-12` in `run.py:119-120` — I
independently re-derived this the same way my own exp-091 self-review did
(`τ_center=2·σ·r_out(cells)` held at its native value 78 by solving
`2·σ_R3·117=78`) and it is exact. `build_article_r3_sigma`
(`run.py:127-132`) calls `materials.pec_disk(sim,cx,cy,PEC_R_R3)` then
`materials.graded_black_shell(sim,cx,cy,PEC_R_R3,R3_R_OUT_CELLS,
sigma_max=sigma_max)` — identical two-call geometry to exp-091's own
`build_article_r3`, confirmed against `lab/materials.py`'s actual
signature (`graded_black_shell(sim, cx, cy, r_in, r_out, sigma_max=0.5,
eps_max=1.0)`, line 74) — only `sigma_max` is exposed as a parameter, no
other geometric or profile-shape change. No bug in the construction.

`R3b`'s `p_abs_w` ratios (`0.9610`/`0.9619`/`0.9602`) and
`ratio_abs_ext_dev_from_anchor` (`0.7688%`/`0.5378%`/`0.9281%`, my own
recompute of `abs(ratio_abs_ext_raw_c - 0.51)/0.51` matches
`results.json`'s own field exactly at all three angles) also reproduce
bit-exact.

## 2. Is Rank 3's CONFIRM actually as broad an evidentiary basis as the Result section's forward-looking sentence claims?

**On its own six cells: yes, the CONFIRM is real and correctly computed,
not marginal.** None of the six ratios sits anywhere near the `[0.3,3.0]`
boundary — the closest is `1.18` at 41.4°, less than half-way to `3.0`
on a log scale, and no sign flip occurs anywhere. This is a genuinely
different, better-supported result than a boundary-clearing pass (compare
exp-091's own (b2) CONFIRM, ratios up to `2.78×` — this cycle's worst
ratio, `1.18×`, is markedly tighter). Calling the six-cell result "clean"
is fair.

**Where the write-up over-reaches is the implicit generalization to Rank
1's own 28 calls, in particular to the region Rank 1 itself discovers.**
Rank 3's three census angles (37.2°, 40.2°, 41.4°, inherited unchanged
from exp-087/088/089's own original census, not re-chosen for this
cycle's own new findings) sit at these distances from the `cpl=30`
crossing locations Rank 1 *itself* only locates later in the same run:

| Rank-3 angle | Distance to nearest `cpl=30` crossing (of the 3 this cycle locates) | Measured ratio deviation from 1.0 |
|---|---|---|
| 37.2° | 2.872° (far) | 6.2–7.7% |
| 40.2° | 0.128° (close) | 1.4–2.7% |
| 41.4° | 0.381° (moderate) | 17.2–18.3% |

I computed the distance column myself from `results.json::rank1.
crossing_report` and `run.py`'s own printed crossings (`41.781067°`,
`41.837653°`, §5). **The pattern is not monotonic with proximity** — the
angle closest to a crossing (40.2°) shows the *smallest* ratio deviation,
and the largest deviation (41.4°, ~18%) occurs at neither the closest nor
the farthest point — so I cannot honestly extrapolate a "sensitivity grows
near a node" story from this n=3 sample, and I do not think the record
should either. What I *can* say, precisely: **none of the three tested
points sits anywhere near the upper window's own newly-discovered
structure** — the nearest tested angle (41.4°) is `0.38°`–`0.44°` away
from either of the two crossings straddling the near-total null at 41.8°,
and that null's own `delta_scene` magnitude (`1.865×10⁻⁵` at 41.8°, per
`results.json::rank1.per_theta`) is 8–33× *smaller* than any of the three
values Rank 3 actually perturbed (`4.37×10⁻⁴` to `1.25×10⁻³` range,
filed exp-091 values). A ratio-based confound test calibrated on
signal magnitudes an order of magnitude larger says nothing directly
about whether the same absolute sigma perturbation could matter more, in
either direction, right at a point R13/R14's own established mechanism
already flags as maximally fragile to any perturbation, precisely because
its own denominator is close to zero. **This is not a claim that the
confound *does* contaminate the near-null region — I have no evidence
either way, which is exactly the problem.** The Result section's sentence
("Rank 1's own results below are therefore directly comparable to exp-091's
own filed `cpl=20` data with no sigma-scaling caveat") is stated without
this scope qualifier; a reader citing the double-crossing finding (§Next
item 1's own stated purpose — feeding an R15 caution-zone rebuild) would
reasonably assume Rank 3 already cleared this specific region, and it did
not test it.

**This is a narrower, but real, residual of the exact gap MATERIALS' own
Phase-2 critique named and Red Team's own audit partially, not fully,
closed** (`phase2_redteam_audit.md` §2, "A residual limitation resequencing
does NOT fully close"): Red Team's own disclosed residual was about net
*placement* (only live if Rank 3 REFUTEs/NEITHERs); it does not cover the
case actually realized — Rank 3 CONFIRMs, Rank 1 then *discovers new
structure the CONFIRM never sampled*. Not disclosed anywhere in this
cycle's own idealizations (Idealization 9 states the angles are non-
representative in general terms, but does not name this specific,
retrospectively-obvious gap).

## 3. The empty-leg re-run-not-reuse fix and the "bit-exact match" claim

**Correctly implemented in code, verified directly.** `_run_sim_r3_sigma`
(`run.py:135-148`) calls `build_article_r3_sigma` only inside `if
with_article:` — no other code path in the empty-leg branch touches
`materials.graded_black_shell` or reads its `sigma_max` argument at all.
This is not an inference from behavior; it is structurally guaranteed by
the `if` statement itself — the empty-leg field is bit-independent of
`sigma_max` by construction, exactly as claimed. I also independently
confirmed the Director's claim that no T28-family experiment persists raw
FDTD captures: `find experiments -iname "*.npz" -o -iname "*.npy" -o
-iname "*.pkl"` returns files only under `experiments/000`, `001`, and
`058` — none from exp-069 onward — so "the empty-leg profile array needed
… is not retrievable from anything committed to git" is accurate, not an
excuse.

**What the "ALL MATCH=True" empty-leg reproduction actually demonstrates,
precisely.** The Learned section's own item 4 states this as "empirical
confirmation… that 'this bench's FDTD is deterministic as assumed.'" That
is true but undersells what is actually the more useful half of the
result: determinism of a fixed FDTD update rule given identical inputs
(no RNG anywhere in this solver) was never seriously in doubt — the real
value of the bit-exact match is as a **configuration-fidelity check**,
proving that `_run_sim_r3_sigma`'s box geometry, `cpl`, `STEPS`, taper,
and source construction were reproduced with zero drift from exp-091's own
`_run_sim_r3` for these six cells specifically (a typo in any one of
`PEC_R_R3`, `R3_R_OUT_CELLS`, `BOX_CLEARANCE_*_R3`, or the taper width
would have broken this match just as surely as non-determinism would have).
Both framings are true; the record states only the less informative one.
Non-load-bearing — I am not disputing the check's validity, only its own
characterization of what it proves.

## 4. `graded_black_shell` realizability: does the `sigma_max=1/3` correction touch it, and should it have been flagged?

I checked this specifically because the task brief for this review asked
me to, and because the correction formula looked, at first read, close
enough to something already on this program's own books to be worth
tracing down. **`experiments/034-.../REALIZABILITY_MEMO.md` Entry 2**
(Iteration 25/exp-048, amended through Iteration 39/exp-062) derives and
uses **the identical formula**: `sigma_max_shell(r) = 0.5/(r/78)`, for a
completely different purpose — computing what conductivity a *physically
larger* (witness-scale, 0.5–1.5 m) self-similar build of `graded_black_shell`
would need at fixed grid-cell-count convention, in service of that memo's
own UNOBTANIUM-WITH-PARAMETERS verdict (driven by a 70–350× thickness gap
against real CNT-forest/Vantablack coatings, Amendment 6). At `r=117`
(this cycle's own `R3_R_OUT_CELLS`), that formula gives `0.5/(117/78) =
1/3` — bit-identical to this cycle's own `SIGMA_R3_CORRECTED`.

**Having traced it, I conclude this is a coincidence of the SAME
mathematical identity (hold `τ_center=2·σ·r_out(cells)` fixed while
`r_out(cells)` scales) arising from two physically different operations,
and this cycle's own "REALIZABILITY_MEMO.md untouched, Checkpoint
criterion 2 N/A" framing is correct, not a gap.** REALIZABILITY_MEMO
Entry 2's `r_out` scales because the **real, physical object** grows
(dx held fixed, meters-per-cell unchanged) — a genuinely different
material recipe is needed at every size, which is the crux of that memo
entry's own realizability argument. exp-091/exp-092's `R3_RATIO=1.5`
scales `r_out(cells)` for the opposite reason: the **grid gets finer**
(`cpl` 20→30) while the *physical* radius is held exactly fixed (`L_
GEOMETRIC_M_R3` unchanged, independently confirmed in my own exp-091
self-review, §3 there) — this is a pure numerical-discretization
renormalization, restoring the SAME simulated physical absorber's
accumulated optical depth, not asking a real material to do anything
different. No realizability content follows from this cycle's own
`sigma_max` correction, and the record is right to say so.

**One thing worth stating for future readers, though, since nothing in
this record currently does**: the two operations produce the *identical*
formula and, at this cycle's own specific geometry (`r_out=117`), the
identical numeric result (`1/3`), by coincidence of ratio (`R3_RATIO`
here is 1.5, the same value REALIZABILITY_MEMO's own r=117/78 witness-scale
row happens to use). A future citation pulling "`sigma_max=1/3`" out of
context, without also carrying which of the two operations it came from,
risks conflating a numerical-resolution bookkeeping fix with a physical
device-scaling claim — exactly the kind of unit/normalization
conflation R9 already exists to guard against, applied here pre-emptively
rather than after an actual instance. I recommend a one-sentence forward
note in `NOTES.md` (or the next cycle that cites this number) disambiguating
the two, not a correction to anything already filed.

## 5. A previously-uncaught defect: `results.json` silently drops the second upper-window crossing

`run.py:461-471` computes `upper_crossings = find_zero_crossings(
upper_window, upper_vals)` and **correctly finds and prints both**:

```
[R1a/R1b] upper window [41.4, 41.6, 41.8, 42.0]
          crossings found: [41.781067311937264, 41.8376530294636]
[R1a PRIMARY] VERDICT=NEITHER  (lower crossings: 1, upper crossings: 2)
```

(`run_output.txt` lines 100-104, verified verbatim) — and `r1a_verdict`
itself is computed correctly from `len(upper_crossings)`, so the **scored
NEITHER verdict is unaffected**. But `r1b_report` (`run.py:486-487`)
persists only:

```python
upper_crossing_cpl30=(float(upper_crossings[0]) if len(upper_crossings) else None)
```

— a **singular** field, capturing only the first (`41.781067°`) of the two
found values. I confirmed `results.json::rank1.crossing_report` has no
other key carrying the second crossing (`grep`/direct key enumeration,
§0 preamble) — the committed, machine-readable record of this cycle's own
most novel finding (the double-crossing near-null) recoverable from
`results.json` alone undercounts it by one. I independently re-derived
`41.837653°` by linear interpolation between the filed `41.6°` cpl=30
value (`+1.7838×10⁻⁴`, exp-091's own filed a2-bracket) and this cycle's
own `41.8°` value (`−1.865×10⁻⁵`) — reproduces `run_output.txt`'s printed
figure exactly, confirming the number itself is right; only its
persistence is incomplete.

`NOTES.md`'s own Result section correctly reports both crossings (copied
correctly from `run_output.txt`, not hand-computed independently — no R4
violation), so the record's own prose is not wrong. But **`NOTES.md`'s
own Next item 1 explicitly proposes feeding "the two newly located
`cpl=30` crossings (or three, counting the upper pair separately)" into
an R15 caution-zone rebuild** — the single top-ranked item this cycle
hands to Iteration 70. A future cycle building that rebuild from
`results.json` (this program's own normal convention — `NOTES.md`
prose is the citable narrative, but `results.json` is the machine-readable
source most reused code pulls from, per this cycle's own reuse of exp-090's
and exp-091's functions) would silently receive only two of the three
located crossing values, not three. This is not a Checkpoint-4 matter
(caught here, blind, before this LOGBOOK entry, non-load-bearing to any
of this cycle's own scored verdicts) but it is a real, concrete,
cheap-to-fix forward risk sitting directly in the path of the very next
queued item.

## 6. Other checks, no issues found

- The sigma-branch decision logic (`run.py:386-395`) is implemented
  exactly as `phase3_synthesis.md` §1's pre-registered branch rule
  specifies — CONFIRM→`0.5`, REFUTE/NEITHER→`1/3`, both paths present in
  code even though only the CONFIRM path executed this cycle. No
  post-hoc branch selection.
- `RANK3_ANGLES == [dg.DENSE_ANGLES[6], dg.DENSE_ANGLES[21], dg.DENSE_
  ANGLES[27]]` (`run.py:117`) — a live index assertion, not a hand-typed
  angle list — matches this program's own R4-safe convention (compare
  exp-091's own bracket-angle-by-value check).
- `xi_pass`/`nonneg_pass`/`vac_pass` all asserted `True` before any
  downstream computation runs (`run.py:270,306,309`) — hard `assert`
  statements, not soft warnings; a gate failure would have halted the
  run, not merely flagged it.
- `RANK1_ANGLES` are all confirmed members of `dg.DENSE_ANGLES` by a live
  `assert` (`run.py:123-124`), not a hand-typed list independent of the
  grid.
- The print-parity fix (Red Team's mandatory item 7) is genuinely
  implemented: `netd_disclaimer`/`scope_note`/`sigma_branch_disclaimer`
  all appear in `run_output.txt` lines 131-133, not only in `results.
  json` — verified directly, not merely asserted present.
- No `constraint-1–4`/T1 claim anywhere in the record;
  `REALIZABILITY_MEMO.md` correctly untouched (§4 confirms this is the
  right call, not merely an unexamined one). Checkpoint criterion 2
  correctly N/A.

## 7. Ranked top-3 candidate directions for Iteration 70

1. **A small, targeted `sigma_max` PRIMARY-channel check at the upper
   window's own newly-discovered near-null/double-crossing region**
   (e.g. 41.6°–42.0° at the corrected `sigma_max=1/3`, mirroring Rank 3's
   own six-call recipe — 4-8 calls) — before that region's crossing
   locations are cited as sigma-validated inputs to any caution-zone
   rebuild. This closes the specific scope gap §2 identifies: Rank 3's
   real CONFIRM does not currently cover the one region this cycle's own
   Rank 1 discovered to be both the most novel finding and, by raw
   magnitude, an order of magnitude more fragile than anything Rank 3
   tested.
2. **Fix `results.json::rank1.crossing_report` to persist the full list
   of found crossings in each window, not `crossings[0]`** — zero-FDTD,
   a few lines of `run.py`, prevents Iteration 70's own top-ranked queue
   item from silently losing the second upper crossing if built from the
   committed JSON rather than `run_output.txt`'s stdout.
3. **Re-fit R15's own caution zone using the (now sigma-validated,
   JSON-complete) newly-located crossings** — `NOTES.md`'s own top-ranked
   Next item, which I concur is the right next step, gated explicitly on
   items 1–2 above and on `NOTES.md`'s own Next item 2 (resolving whether
   the 0.057°-separated double-crossing is a genuine two-node feature or
   an under-resolved single deep null) — rebuilding a calibration boundary
   on a pair of crossing locations that might collapse to one under finer
   resolution would risk a fresh instance of exactly the failure mode R15
   itself exists to catch.

No new numbered rule is warranted this cycle — §2 and §5 are both
concrete, disclosed-scope gaps in a single cycle's own record, not a
recurrence of a "known, named, ignored" pattern from R6 through R15's own
lineage.
