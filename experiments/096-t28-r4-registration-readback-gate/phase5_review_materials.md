# Phase 5 Review — MATERIALS & METAMATERIALS

*Blind review of exp-096 (Panel Iteration 73), read fresh, not having seen
any other seat's current Phase-5 output. Charter: sub-wavelength structure;
what could physically realize the proposed optical behavior; owns the
realizability bound (published/plausible/unobtainium-with-parameters).
This cycle is pure instrument-validation — T1 route N/A, realizability
N/A, `REALIZABILITY_MEMO.md` untouched, confirmed independently below —
so this review applies discipline-lens scrutiny to the construction/
recompute claims instead, per this cycle's own precedent (my Phase-2
critique) and per the assignment's brief.*

## 1. Independent re-verification (bit-exact where possible)

Ran `experiments/096-.../run.py` fresh in this session (not trusting the
committed `results.json`) and diffed the output against both the committed
`results.json` and `run_output.txt`. All headline numbers reproduce
bit-exact:

- **Registration gate: CLEAN.** All 16 representative constructions pass
  Checks 1–4; Check 6 clean at all 8 points.
- **Check 5 (my own Phase-2 fix, MATERIALS' recipe-internal spot-check):**
  `src_x_recomputed=600, y_lo_recomputed=80, y_hi_recomputed=3088`,
  bit-exact against `dg.R4_CONFIGS["C40_R4"]`'s own stored
  `{src_x:600, y_lo:80, y_hi:3088}`. Confirmed CLEAN, confirmed the numbers
  are real, not restated from prose.
- **Fault-injection triad:** positive control CLEAN; FI-A/B/C all correctly
  flagged DEFECT-FOUND, with `check4_max_abs_diff` = 1.6355… (FI-B) and
  298.631… (FI-C), matching NOTES.md's cited 1.636/298.6. I additionally
  confirmed a detail NOTES.md does not spell out but Red Team's attack #3
  predicts: **FI-A's own `check4_phase_ramp` reads `True`** (only Check 1
  catches FI-A) — because Check 4 recomputes its comparator from the
  already-corrupted `sim.lam` itself, so a `cpl`-swap defect is
  self-consistent under Check 4 alone. This is real, present in the actual
  run data, and exactly the failure mode attack #3 named — a good sign the
  audit's reasoning tracks the executable, not just the prose.
- **Zero-FDTD desk bound:** independently re-pulled `crossings_deg` from
  `experiments/090-.../results.json` and `rank1.crossing_report` from
  `experiments/092-.../results.json` myself (not from `run.py`'s
  intermediary) and recomputed the three migration figures directly:
  `0.1935812644838535 / 0.3201659178026546 / 0.3767516353289935` —
  bit-exact against the cited `0.193582°/0.320166°/0.376752°`. Containment
  ratios recompute identically to the printed table.
- **No `lab/` diff**: confirmed via `git log`/`git status` — the last
  commit touching `lab/` predates this cycle; consistent with the "0 FDTD
  calls, zero `lab/` diff" claim. I did not re-run the full trust suite
  (no engine code changed, so low marginal value against the time cost);
  flagged as the one claim in this document I did not independently
  re-execute.

**Everything I could check, checked out.** No arithmetic or provenance
defect found anywhere in the headline results.

## 2. Check 5, independently re-derived from source (the assignment's core ask)

Read `r4_config()` directly in
`experiments/069-t21-block-mini-period-match-power-up/design_geometry.py`
(lines 265–282) and the module-level constants that feed it (lines
228–255), alongside `check5_recipe_spot_check()` in this cycle's `run.py`.

**`r4_config(80, 0)` (= `C40_R4`) computes:**
```
R4_BASE_SRC_X = round(300 * 2.0) = 600      # module-level, line 233
R4_BASE_ABSORB = round(40 * 2.0) = 80       # module-level, line 232
R4_BASE_NY = round(1584 * 2.0) = 3168       # module-level, line 231
src_x = R4_BASE_SRC_X + pad = 600 + 0
y_lo  = R4_BASE_ABSORB + pad = 80 + 0
y_hi  = ny - y_lo = (R4_BASE_NY + 2*pad) - y_lo = 3168 - 80
```

**Check 5's hand-written recompute does, line for line, the identical
two-stage arithmetic** (`round(native × RATIO)`, then `+ pad`, then
`y_hi = ny − y_lo`), using the identical native literals (`300, 40, 1584`)
and identical `RATIO=2.0`, just typed a second time instead of invoked as
a function call:
```
src_x_recomputed = round(300 * 2.0) + 0
y_lo_recomputed  = round(40 * 2.0) + 0
y_hi_recomputed  = round(1584 * 2.0) - y_lo_recomputed
```

**Verdict on the assignment's question: numbers match bit-exact, YES —
but the recompute is only *partially* independent of `r4_config()`, and
NOTES.md's framing does not disclose which part.** It is genuinely
independent of two specific failure surfaces: (a) `r4_config()` never
being *called* — so a bug in argument-passing at the call site, or a
corrupted `R4_BASE_*` module constant (e.g. a stray reference to
`R3_RATIO` instead of `R4_RATIO`, or a typo'd native literal inside
`design_geometry.py` itself), *would* be caught, since Check 5 supplies
its own copies of `300/40/1584/2.0` rather than reading
`R4_BASE_SRC_X`/`R4_RATIO` off the module. That is a real, non-trivial
check, not a tautology.

But it is **not** independent of the *formula itself*: the
`round(native×RATIO)` two-stage structure, the choice to add `pad`
post-rounding, and the `y_hi = ny − y_lo` convention are reproduced
verbatim, not re-derived from an independent description of the intended
geometry (e.g. a physical-units derivation, or a value pulled from a
different committed source such as exp-094/095's own NOTES.md constants
table). A defect embedded in that *shared formula* — the exact class
Idealization 17 and my own Phase-2 critique named as the live concern —
would, if present in `r4_config()`, most plausibly have been written the
same way into Check 5 too, since Check 5 was necessarily authored by
reading `r4_config()`'s own source to know what to reproduce. This is
narrower than "independently recompute... outside `r{n}_config()`"
suggests to a reader who hasn't opened both files side by side: the
independence is *from the function call and the module constants*, not
*from the arithmetic method*.

**One alternative concern I checked and ruled out, for the record (verify-
before-claim, not just before-report):** I suspected the `round()` calls
might hide a banker's-rounding-vs-round-half-up ambiguity — this file's
own comments flag exactly that risk for `PLANE_X`/`GUARD_OUT` at
`R3_RATIO=1.5` (`77*1.5=115.5`). I checked whether the three quantities
Check 5 actually tests (`src_x`, `absorb`→`y_lo`, `ny`→`y_hi`) are
exposed to it: native `300/40/1584` are all even, so `×1.5/×2.0/×2.5`
never lands on a half-integer for any of R3/R4/R5 — confirmed by direct
computation. **This particular risk does not apply to Check 5's fields at
any ratio; I am not raising it as a finding**, but note it here so a
future reviewer doesn't have to re-derive it.

## 3. Is Check 5's "one point, R4/C40 only" scope sufficient? (the assignment's second question)

**Materially better than the bare "R3/R5/G untested" framing suggests,
for a specific, verifiable reason NOTES.md doesn't spell out — but still
not sufficient to call the recipe-level hypothesis space closed.**

I read `r3_config()`/`r4_config()`/`r5_config()` side by side (all three,
directly). They are **structurally identical function bodies** — same
seven-line sequence of `+pad`/`+2*pad`/`y_hi = ny - y_lo`, differing only
in which family's `R{n}_BASE_*` names they close over. Because the
*function logic* is one shared, mechanically-copied block, a defect in
that logic (wrong operator, wrong offset target, wrong sign) would fire
identically in R3/R4/R5 alike — Check 5's single R4 point is a reasonable
proxy for the *function-body* class specifically, precedented by this
program's own established practice of trusting one verified instance of
mechanically-identical code (e.g. Gate 3's own cross-family congruence
check already leans on this same code-identity fact).

What Check 5's single point genuinely does **not** cover, and where the
residual risk actually concentrates: the **per-family `R{n}_BASE_*`
literal definitions themselves** — `R3_BASE_ABSORB`, `R5_BASE_NY`, etc.
are each separately typed module-level lines, not generated by a shared
function; a typo specific to `R5_BASE_NY` (say) would leave R4 completely
clean and be invisible to this cycle's Check 5 entirely. NOTES.md's
Idealization 39 states this residual honestly but generically
("a different family... would not be caught"); my read narrows *why* —
the exposure is specifically at the **per-family constant-literal layer**,
not the shared arithmetic-logic layer, which sharpens what a follow-up
check would need to target (see §5).

Combined with §2's finding (even the one tested point is a
formula-*restatement*, not a formula-*independent* derivation), the honest
scope is a notch narrower than Idealization 38's own summary ("gets one
spot-check against the shared-recipe class") implies: what was actually
gained is a real check against *module-constant corruption at one family*,
not a check against *recipe-formula correctness* anywhere. NOTES.md's
Result section is otherwise careful and un-overclaiming (states "not
exhaustive... per Idealization 39" explicitly) — this is a depth
refinement of an already-disclosed gap, not a discovery that the
disclosure is false.

## 4. Does CLEAN change my realizability-adjacent read?

**No change to the realizability bound — still correctly N/A this
cycle — and this finding does not, on its own, create new realizability
content for a future cycle either.** T28 remains a numerics/instrument
sub-thread investigating the simulator's own resolution-dependent
behavior (`delta_scene(θ)` sign structure across `cpl`), not a claim about
any physical mechanism or fabricatable structure; `REALIZABILITY_MEMO.md`
is untouched, correctly.

One thing worth flagging for whoever eventually reconnects this sub-thread
to a phenomenon-mechanism proposal, *if* genuine node migration (rather
than discretization artifact) is eventually confirmed: the migration
magnitude at the three already-measured crossings **grows**, not shrinks,
from the smaller `cpl=20→30` step (`RATIO` 1.0→1.5, one figure at 0.194°)
to the not-yet-measured `cpl=20→40` step this desk bound is estimating for
(`RATIO` 1.0→2.0, a larger discretization jump) — the desk bound's own
Idealization 36 already flags this as "optimistic, not conservative."
From a materials lens: if this angular feature is ever promoted into a
mechanism claim (e.g. an angle-selective absorption edge), a
resolution-sensitivity on the order of several tenths of a degree, that
does not obviously shrink with finer discretization, is exactly the kind
of parameter fragility that would need to be priced into a future
realizability bound — a real sub-wavelength structure's own fabrication
tolerance would need to be assessed against whatever physical linewidth
this angular feature corresponds to, not assumed benign by default. This
is a flag for *future* work, not a claim about this cycle's (N/A)
realizability status.

## 5. Verdict

**CONCUR-WITH-GAP(S).**

The gate's headline (CLEAN, fault-injection genuine, desk bound correct)
reproduces bit-exact under independent re-execution and re-derivation from
raw source — I found no arithmetic, provenance, or logical defect in
anything actually claimed. The gap is in precision of the *scope
language*, not in the numbers: Check 5 is real evidence, but it is
evidence against a narrower defect class (module-constant corruption at
one family, function-body-identity assumed) than "spot-check against the
shared-recipe class" reads as to a reader who has not opened
`design_geometry.py` and this cycle's `run.py` side by side. I do not
consider this fatal to the cycle's central, load-bearing claim (Gate 5 has
genuinely never checked this axis before; it does now, and the
fault-injection triad proves the check is real) — but the "2:1 to 3:1,
impressionistic" strengthening toward genuine migration should be
understood as resting on a Check 5 that closes *less* of the recipe-level
hypothesis space than its own write-up implies, on top of the
already-disclosed R3/R5/G-config scope gap.

## 6. Sharpest finding

**Check 5 is a restatement of `r4_config()`'s own arithmetic with the same
native literals and `RATIO`, not an independent re-derivation — verified
by reading both functions side by side, not inferred from the write-up.**
It correctly rules out module-constant/call-site corruption (a real,
useful result) but cannot in principle catch a defect shared identically
by both the recipe and its own restatement — the exact residual class
Idealization 17 (my own Phase-2 lineage) already named as most concerning,
now still open at a level one layer deeper than NOTES.md's language
suggests.

## 7. Ranked candidate directions, Iteration 74

1. **Extend Check 5 to a genuinely formula-independent recompute at R3 and
   R5, sourced from outside `design_geometry.py`.** Re-derive at least one
   `R3`/`R5` placement value from a textually separate committed source
   (e.g. exp-033's/exp-094's/exp-095's own NOTES.md constants tables, or a
   from-scratch physical-units derivation) rather than re-typing
   `design_geometry.py`'s own native literals a second time — this closes
   both the disclosed scope gap (R3/R5 untested) and the depth gap found
   here (restatement vs. independence), before any further FDTD spend
   leans harder on "the recipe is clean." Zero-FDTD, cheap, directly
   answers the open question this review sharpens.
2. **Proceed with reconciled-queue item 4** (the node-bracketing re-run at
   θ₀≈38.590°, half-width ≥0.5° per this cycle's own confirmed desk bound)
   — now unblocked by the CLEAN registration result, the most direct test
   of whether Rank 1c's own FAIL reflects genuine migration.
3. **Proceed with item 3** (bracketing the other three `cpl=20` nulls at
   `cpl=40`, ~24 calls) — same unblocking logic, next in the reconciled
   queue's own sequencing.
4. **Longer-horizon, materials-adjacent:** once/if node migration is
   confirmed genuine rather than a discretization artifact, begin scoping
   what angular tolerance a real sub-wavelength structure would need to
   survive, given the migration magnitude is not yet shown to shrink with
   finer resolution (§4) — not urgent this cycle (T1/realizability remain
   N/A), but worth naming now so it isn't rediscovered cold later.
