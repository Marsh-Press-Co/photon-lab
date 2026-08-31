# Phase 5 Review — MATERIALS & METAMATERIALS (exp-097, Panel Iteration 74)

*Blind review, fresh context. Charter: sub-wavelength structure /
realizability bound — N/A this cycle (no material or mechanism proposed;
independently confirmed: `T1 escape route` and `Realizability bound` both
read "N/A" in `phase1_proposal.md` §4 and `NOTES.md`, and
`REALIZABILITY_MEMO.md` is not touched anywhere in the diff). Per this
cycle's charge, applying this seat's general discipline instead:
independently re-deriving claimed figures from source rather than trusting
the document's own arithmetic — with particular attention to this seat's
own Check-5 extension (`R3`/`R5`, the item this seat itself proposed at
Phase 1), since a lead seat's own Phase-5 self-review is expected to be at
least as adversarial toward its own prior work as any other seat's (the
exp-095 PHOTONICS precedent PANEL.md's own framing cites).*

## What I independently re-ran and re-derived this session

- **Full bit-exact re-execution.** Ran
  `python3 experiments/097-t28-r18-tier0-gate-closure/run.py` fresh and
  diffed the output against the committed `results.json` (excluding the
  non-deterministic `wall_time_s` field): **identical, every field.**
  Confirms the committed record is a genuine, reproducible artifact, not a
  hand-edited one.
- **Check 5's own R3/R5 hand-arithmetic** (this seat's own Phase-1
  design), independently re-derived directly from
  `experiments/069-t21-block-mini-period-match-power-up/
  design_geometry.py`'s own `r3_config()`/`r5_config()` source (not their
  comments): `R3` (`pad=0`, `ratio=1.5`): `y_hi = ny − y_lo =
  round(1584·1.5) − round(40·1.5) = 2376 − 60 = 2316`. `R5` (`pad=0`,
  `ratio=2.5`): `y_hi = round(1584·2.5) − round(40·2.5) = 3960 − 100 =
  3860`. Both bit-exact against the values `check5_recipe_spot_check_
  extended()` actually asserts against (`R3_CONFIGS["C40_R3"]`/
  `R5_CONFIGS["C40_R5"]`'s own stored fields) — **confirms the executable
  check is correct**, and independently confirms EM/THERMODYNAMICS/Red
  Team's own finding: the desk-check *prose*, in both §0 and §2b of
  Phase 1, cited the wrong comparison target (`R{n}_BASE_NY` = 2376/3960,
  the *domain-height* constant) instead of `y_hi` (2316/3860, the
  *source-placement* quantity, offset from `NY` by `y_lo`) — non-load-
  bearing to the code, and I confirm the fix landed correctly in this
  document's own `NOTES.md` (§Setup, item 3: "matches... `2316`/`3860`",
  not the domain-height figures).
- **The `family_ok`/`NOTES_MD_FROZEN_FAMILY_BY_LINE` re-keying**, cross-
  checked line-by-line against `experiments/095-.../NOTES.md`'s own
  prose at 265/291/304/437/445/476/495/511 by direct grep this session:
  Rank 2=`R5`/`cpl=50` (265), Rank 3=`R4`/`cpl=40` (291), Rank 4=`R3`/
  `cpl=30` (304); lines 437/445/495 are `R4` points, 476 is `R5`, 511 is
  `R3` — all eight bit-exact against `NOTES_MD_FROZEN_FAMILY_BY_LINE`.

## A genuine, independently-found gap (not raised by Red Team's Phase-2
## audit or any of the five blind critiques — I checked all six documents
## before writing this)

**`Idealization 40` (and `run.py`'s own docstring for
`check6_positional_and_cpl`) misdescribes the actual independence of
`cpl_ok` — understating, not overstating, what the committed code does.**

Both texts state `cpl_ok` "is STILL keyed by `pt['family']` on both
sides" and is therefore "not an independent per-point check" in isolation
from `family_ok`. I read the actual code (`run.py`, and NOTES.md's own
`Setup` snippet — identical):

```python
family_frozen = NOTES_MD_FROZEN_FAMILY_BY_LINE[line]        # keyed by notes_line
cpl_frozen, _ = NOTES_MD_FROZEN_CPL_BY_FAMILY[family_frozen] # RHS: keyed by family_frozen, NOT pt["family"]
...
cpl_ok = bool(CPL[pt["family"]] == cpl_frozen)               # LHS only: keyed by pt["family"]
```

Only the left-hand operand is keyed by the untrusted `pt["family"]`; the
right-hand operand (`cpl_frozen`) is sourced via `family_frozen`, itself
keyed by `notes_line` — independent of `pt["family"]`, exactly the same
independence property `family_ok` has. I verified this is not merely a
reading of the code but has real behavioral consequence, by direct
execution: calling `check6_positional_and_cpl` on the FI-H mislabeled
point (`family` overridden `"R3"→"R4"`, `notes_line=511` untouched)
returns `family_ok=False` **and** `cpl_ok=False` — `CPL["R4"]=40 ≠
cpl_frozen=NOTES_MD_FROZEN_CPL_BY_FAMILY["R3"][0]=30` — not the
uninformative/trivially-passing value Idealization 40's "not independent
in isolation" framing implies. (`results.json`'s own `FI_H` block records
only `new_family_ok`, not `cpl_ok`, so this was not visible without
re-executing the function directly, which I did.)

Notably, **Red Team's own Phase-2 audit already had this right**: its §3
fix code explicitly re-keys `cpl_frozen`'s lookup through
`NOTES_MD_FROZEN_FAMILY_BY_LINE[pt["notes_line"]]` and states outright
"`cpl_ok`... no longer both keyed by the untrusted field" — directly
contradicting Idealization 40's later "STILL keyed... on both sides."
Synthesis (Phase 3/NOTES.md) implemented Red Team's own correct code but
then wrote a description of it that reverted to describing the *prior*
(genuinely tautological) Phase-1 draft's property, not the fixed one now
running. This is the identical *class* of defect this cycle's own mandate
exists to police (R18: a check's documented scope must match its actual
code) — occurring inside the very document that resolved R18's founding
gate, and in a direction (understating coverage) opposite to every other
instance found this cycle, so it is not dangerous the way an overclaim
would be, but it is a real, independently-derivable inaccuracy a future
cycle citing "`cpl_ok` alone is not independent" would inherit uncorrected.
**Non-load-bearing to any verdict this cycle** (nothing in `results.json`,
the CLEAN outcome, or the fault-injection triad depends on this
characterization being right) — flagged as a same-shift documentation fix,
not a re-run.

## Everything else: independently re-verified, sound

- The `y_hi`/`BASE_NY` mis-citation fix (docket item 1) landed correctly
  in the frozen NOTES.md text, confirmed by direct comparison against
  `design_geometry.py` source above.
- The standing-items ledger line (docket item 2) is restored, with
  correct counts: grazing-incidence "TEN... Iterations 64–74" is
  consistent with the program's own established count style (which
  already excluded Iteration 66 as of exp-096's "NINE... 64–73"); x-wall
  "TWENTY-TWO... 076–097" is a clean contiguous count, `097−076+1=22`.
- FI-G's 3-leg extension (docket item 3) is genuinely present and all
  three legs independently miscompare against distinct true values
  (`452≠450`, `602≠600`, `752≠750` — Python's banker's rounding on the
  `.5` cases checked by hand and confirmed non-coincidental).
- The taper formula (Check 7) is a bit-exact reproduction of
  `lab/fdtd2d.py:160–164`, confirmed by direct read.
- `git diff --stat HEAD -- lab/` is empty — the zero-`lab/`-diff claim
  holds; no need to re-run the full trust suite for a code-verification
  cycle that touches no engine file.
- The Result section carries the carried-idealizations banner (§6's own
  governance commitment, VISION's flip condition) — confirmed present by
  direct read, discharging that commitment as designed.

## Verdict: **CONCUR-WITH-GAP(S)**

The registration-readback gate's extension is sound: Checks 5/6/7 now
each carry a genuine, executed fault-injection control; Red Team's own
Phase-2-caught tautology in `cpl_ok`/`family_ok` is correctly fixed in the
actual code (independently confirmed by direct execution, not merely by
reading the prose); the CLEAN outcome and all nine fault-injection
scenarios reproduce bit-exact under my own fresh re-run. **Gap:**
`Idealization 40` and `run.py`'s matching docstring both misdescribe
`cpl_ok`'s actual independence (understating it) — a real, if
non-load-bearing and non-dangerous, instance of documented-scope-vs-actual-
code drift, inside the cycle whose purpose is eliminating exactly that
class of drift. Recommend a same-shift text fix (no re-run needed): correct
Idealization 40 to state that `cpl_ok`'s frozen operand is sourced via
`family_frozen` (from `notes_line`), making it independently informative
of a family mislabel even in isolation from `family_ok`, though the two
remain correlated defenses against the identical fault class.

## Ranked candidate directions for Iteration 75

1. **The re-centered, directionally-weighted node-bracketing re-run at
   θ₀≈38.590°**, sized to this sub-thread's own confirmed ≥0.5°
   single-sided half-width (exp-096's desk bound; ~8–16 calls) — the
   direct answer to the question this entire two-cycle registration
   detour exists to enable, now unblocked: the registration gate is
   CLEAN under substantially more discriminating machinery than at
   exp-096, with this cycle's one documentation gap independently
   confirmed non-load-bearing.
2. **Bracket the other three established `cpl=20` nulls at `cpl=40`**
   (~24 calls) — the decisive discriminator between a family-wide
   registration/recipe defect and feature-dependent node migration,
   complementary to (1) and already queued as Tier 1 item 6.
3. **Discharge — not merely re-restate — PHOTONICS' own grazing-incidence
   validity check.** Now ten consecutive cycles named in every T28
   document's closing ledger and never executed. This program's own
   R16/R17/R18 lineage exists specifically to stop a "known, named,
   ignored" item from silently accumulating; an item repeatedly restated
   without ever being scheduled is the documentation analog of exactly
   that pattern, even though no single rule currently governs standing
   ledger items the way R16 governs disclaimers. Flagging as a genuine
   program-health risk this seat can name but not itself resolve
   (realizability is N/A while this item stays unscheduled) — either
   schedule it or have the Director/Red Team make an explicit, reasoned
   call to formally deprioritize it, closing Iteration 61's still-open
   "ritualization governance question" for this specific item rather than
   letting the count climb indefinitely.
