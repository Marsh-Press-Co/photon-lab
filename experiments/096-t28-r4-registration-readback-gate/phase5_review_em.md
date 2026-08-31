# Phase 5 Review — ELECTROMAGNETISM (blind)

*Panel Iteration 73, exp-096. Charter (verbatim): field/wave behavior,
impedance matching, energy coupling; owns the reciprocity/passivity/
causality bookkeeping. Written blind to every other seat's current Phase-5
output. This seat's own Phase-2 critique (`phase2_critique_em.md`) is
reviewed here with no deference — including whether Red Team's override of
its proposed remedy was actually correct, now that the executed Check 6
code and its results are visible.*

## 1. Independent re-verification of the headline results

All bit-exact re-derivations below were computed independently this
session, from source, not copied from any document under review.

**Phase-ramp formula fidelity.** Read `lab/fdtd2d.py:75` (`self.lam =
float(cells_per_lambda)`) and `lab/fdtd2d.py:171-175` (`k = 2π/self.lam;
phase = k·sin(radians(angle_deg))·(yy − 0.5·(y_lo+y_hi)) + rel_phase`)
directly. `run.py::phase_expected()` (lines 130-138) is a line-for-line
match — same constants, same operation order, `rel_phase` defaulted to
0.0 exactly as every representative point uses it. **Confirmed, no
paraphrase, no drift.**

**`check4_max_abs_diff` re-derivation (the task's specific ask).**
Independently computed in Python, from the same formula, at FI-B's and
FI-C's actual parameters (`R4`/`C40_R4`, `y_lo=80, y_hi=3088`, `cpl=40`):

- FI-B (`θ_actual=38.69°` vs `θ_intended=39.2°`): `1.6355117919003836` —
  matches `results.json`'s `1.6355117919003987` to 12 significant figures
  (residual is float64 accumulation-order noise, itself well inside
  `atol=1e-9`'s own stated purpose).
- FI-C (`θ_actual=−39.2°` vs `θ_intended=+39.2°`): `298.6310235614485` —
  bit-exact match to `results.json`.

Both reproduce. **Against my own Phase-2 estimate** ("smallest plausible
defect signal ≈1.4 rad"): the true FI-B figure is 1.636 rad, ~17% above my
rough estimate — consistent to order of magnitude, the gap fully explained
by my Phase-2 arithmetic rounding `sin(39.2°)−sin(38.69°)` to "≈0.006"
(true value 0.00636) and using an approximate rather than exact half-span.
The conclusion my Phase-2 steel-man drew from it — `atol=1e-9` sits ~9
orders of magnitude below the smallest genuine defect signal and ~5 orders
above the float64 roundoff floor, comfortable margin both directions —
holds exactly, now confirmed against the executed numbers rather than a
pre-run estimate.

**Desk bound.** Re-pulled `experiments/090-.../results.json::q8.
crossings_deg[2:4]` and `experiments/092-.../results.json::rank1.
crossing_report` directly; recomputed all three migration figures
(0.193582°/0.320166°/0.376752°) and all nine containment ratios —
bit-exact against `results.json`'s `desk_bound` block.

**Check 5 (recipe spot-check).** Independently traced `R4_BASE_SRC_X =
round(300×2.0)=600`, `R4_BASE_ABSORB = round(40×2.0)=80`, `R4_BASE_NY =
round(1584×2.0)=3168` from `design_geometry.py` (the actual file at
`experiments/069-t21-block-mini-period-match-power-up/design_geometry.py`
— note the proposal's own citation shorthand, "`069-.../design_geometry.
py`," names the wrong T28-adjacent 069 directory by number; the real file
lives in the *T21* exp-069, reused by import chain since). `y_lo=80,
y_hi=3088, src_x=600` for `C40_R4` (`pad=0`) reproduces exactly. **Clean,
confirmed independently.**

**Check 6 (NOTES.md cross-check).** Grepped `experiments/095-.../NOTES.md`
directly at the five cited line numbers (437/445/476/495/511) and
confirmed the hand-transcribed `NOTES_MD_FROZEN_LINE_VALUES` dict in
`run.py` matches the actual prose at every line, exactly. **Confirmed —
the transcription this cycle performed is itself correct.**

**No `lab/` diff.** `git status --porcelain lab/` is empty; the formula
match above confirms the claim independently regardless.

**All headline claims independently reproduce.** No arithmetic or
citation defect found anywhere in the executed pipeline.

## 2. Was Red Team's override of my Phase-2 remedy correct?

**Yes, in principle — but the adopted fix, as executed, ships with a real,
uncaught residual gap of exactly the shape my own attack predicted.**

My Phase-2 remedy (hand-transcribe the 8 tuples as fresh literal constants
inside the gate module) was correctly diagnosed by Red Team as adding no
real independence: a second manual copy of `run.py`'s own numbers guards
against a keystroke slip, not a source-of-truth defect — the exact
class my own attack named. QUANTUM's alternative (cross-check against
exp-095's NOTES.md, a textually and temporally separate document,
committed before `run.py` existed) is structurally the right fix, and I
confirm it independently in §1 above: it is not vulnerable to a defect
shared between `run.py`'s job constants and this gate's own "intended"
values, because its ground truth comes from a different file entirely.
**On the merits, the override was correct.**

But reading the executed `check6_notes_md_cross_check()` (`run.py:193-207`)
closely reveals it does not fully deliver on that promise:

```python
found = any(abs(pt["theta"] - v) < 1e-9 for v in frozen_values)
```

This is a **set-membership** test against each `notes_line`'s value list,
not a **positional** one. For every one of this cycle's 8 points, two
values share a line (`RANK1A_ANGLES=[39.2,39.4]` at line 437,
`RANK1C_ANGLES=[38.49,38.69]` at line 445, `RANK2B_NATIVE_ANGLES=
[41.825,41.850]` at line 476). If `RANK1A_ANGLES` (or either sibling pair)
had its two indices swapped anywhere upstream — the same "job-list
indexing bug" shape the proposal's own FI-B scenario explicitly names as
"a real, plausible defect shape" — Check 6 would still read CLEAN at both
points: each swapped value is still a member of the same two-element set.
So would Checks 1-4, since they read `theta_intended` from the identical,
already-swapped `exp095.RANK1A_ANGLES[i]`. **No check in this cycle's
six-check architecture would catch a same-line index swap.**

I traced the physical consequence and it is genuinely limited for
*today's* specific data: NOTES.md's own frozen predictions for every
affected line (Rank 1a's "both < 0," Rank 1c's "signs differ across the
pair," Rank 2b-native's "preserve sign/classification at both angles")
are order-symmetric — an index swap would not silently substitute a wrong
physical test, only relabel which array slot carries which already-tested
angle. So this residual gap is **not shown to threaten this cycle's own
CLEAN verdict**. But it is a genuine implementation-vs-specification gap
in the fix billed, in NOTES.md's own Learned §2, as "the single most
valuable Phase-2 finding this cycle produced" and "the single most
load-bearing fix in this docket" — precisely the fix substituted for my
own overridden remedy — and nothing in this cycle's own text discloses it.

The deeper, more general point: **Checks 1-4 have a real, executed
fault-injection triad (FI-A/B/C) that empirically proves they discriminate
correctly. Checks 5 and 6 have none.** `run_fault_injection()`
(`run.py:210-245`) calls `run_checks_1234` exclusively — no scenario
exercises `check5_recipe_spot_check()` or `check6_notes_md_cross_check()`
under a deliberately injected defect. Both are trusted as genuine
discriminators purely by code inspection, which is exactly the standard
this program's own R6/R8 lineage ("a check with no positive/negative
control is not evidence," invoked verbatim by this very proposal's own
§2b) was built to reject for a correctness-critical check. Had a
same-line-swap fault-injection scenario been run against Check 6, it would
have surfaced the gap above directly, this cycle, rather than requiring a
Phase-5 code read to find it.

**One further, minor, related finding, independently confirmed by
execution (§1):** the proposal's and NOTES.md's own fault-injection table
(both Phase 1 §2b and NOTES.md's Setup/Predictions) list FI-A's
"must be caught by" as "Check 1 (transitively, Check 4)." The executed
`results.json` shows `FI_A_family_cpl_swap.check4_phase_ramp: true` —
Check 4 does **not** independently flag FI-A; only Check 1 does. This is
the exact mechanism Red Team's own attack #3 named theoretically (Check 4
recomputes using the *already-corrupted* `sim.lam`, so a pure-`cpl`
mismatch with the angle held correct is invisible to Check 4 alone) — now
empirically demonstrated, not just argued. NOTES.md's own Result section
quietly drops the "transitively, Check 4" language when reporting FI-A
("caught by Check 1 as predicted") — the correct number is reported, but
the contradiction with the pre-registered claim is never disclosed as
such, a smaller instance of the same "confident claim not walked back
explicitly" shape this program's R4/R12 lineage exists to catch. Non-
load-bearing (the overall `caught_as_defect=True` verdict is unaffected),
but it is the same underlying mechanism as the Check-6 gap above, and the
document should say so.

## 3. Verdict

**CONCUR-WITH-GAP(S).**

The registration-readback gate's core value stands, independently
re-verified: nineteen cycles never checked this axis; this cycle built a
real instrument, with a genuinely demonstrated (for Checks 1-4) positive/
negative control, that ruled out caller-level plumbing and — via Check
6's NOTES.md cross-check, correctly transcribed and independently
confirmed here — ruled out `run.py`-vs-NOTES.md transcription drift for
every point actually probed, at zero FDTD cost. The desk bound is
correctly computed and its ≥0.5° recommendation is sound. Red Team's
override of my own Phase-2 remedy in favor of QUANTUM's NOTES.md
cross-check was the right call in principle. But the implementation of
that adopted fix — the single check billed as most load-bearing, the one
substituted for my own overridden proposal — has a real, unflagged
coverage gap (set-membership instead of positional correspondence) and,
along with Check 5, no fault-injection control of its own, unlike the
sibling checks it was meant to strengthen. This does not overturn the
CLEAN outcome for this cycle's own data, but it means the gate's own
"single most load-bearing fix" is not yet verified to the standard this
program applies to everything else in the six-check architecture, and
Idealization 38's own "narrows, does not close" framing should be read as
narrower still than currently stated.

## 4. Ranked candidate directions for Iteration 74

1. **Close the fault-injection gap on Checks 5 and 6 (near-zero FDTD
   cost, directly responsive to the finding above).** Add a same-line
   index-swap scenario (deliberately swap `RANK1A_ANGLES[0]`/`[1]` — or
   equivalent — feeding both the "actual" construction and Check 6's own
   `theta_intended`, and confirm the CURRENT set-membership implementation
   does *not* flag it) as a documented, disclosed limitation, or fix Check
   6 to compare `pt["theta"] == frozen_values[index_within_pair]`
   positionally and re-verify CLEAN survives with the stronger check. Add
   one negative-control scenario for Check 5 (a deliberately wrong
   `RATIO` or native constant) to demonstrate it is a genuine
   discriminator, not merely a passing spot-check. This is the most
   direct way to raise the CLEAN result's own evidentiary standard to
   match Checks 1-4's already-demonstrated one, before any further
   Iteration-73-queue spend leans on it.
2. **Proceed with the already-queued items 3/4** (bracketing the other
   three `cpl=20` nulls at `cpl=40`, ~24 calls; a reconciled node-
   bracketing re-run at 38.590° with a ≥0.5° single-sided half-width,
   per this cycle's own independently-confirmed desk bound) — the
   registration question is now answered within its properly (and, per
   §2 above, slightly more narrowly than stated) scoped bounds, and
   further stalling on it is not justified by the residual found here,
   which does not touch this cycle's own substantive CLEAN finding.
3. **Same-shift documentation fix (near-zero cost):** correct the
   "Check 1 (transitively, Check 4)" claim for FI-A in both Setup and
   Predictions to match the executed behavior, and correct the citation
   shorthand for `design_geometry.py`'s actual location (it lives in the
   T21 `069-t21-block-mini-period-match-power-up/` directory, not a T28
   `069-...` one, despite the recurring "069-.../design_geometry.py"
   shorthand used across this sub-thread).
4. **Extend Check 5's recipe spot-check to `R3`/`R5` and to a `G`
   (padded) config** — currently one point only (`R4`/`C40`), explicitly
   disclosed as such (Idealization 39); a defect isolated to a different
   family or to `pad`-arithmetic specifically would not be caught. Lower
   priority than items 1-3 since it is an explicitly disclosed, not
   silent, scope limit.
