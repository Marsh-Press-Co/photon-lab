# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 48 · exp-071

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat 6). T1 N/A this
cycle, constraint 3 not engaged — my perceptual-threshold duty has no
direct target. Per the Director's own framing for this review, I looked
instead for process-discipline issues, numeric-accuracy issues, and
whether the write-up's own claims are honestly bounded. Every number below
was checked against `results.json` or reproduced by re-running code
directly, not taken from any document's prose.*

## 0. What I independently verified

- `python3 design_geometry.py`: reproduces every figure in
  `phase1_proposal.md`/`phase3_synthesis.md` bit-for-bit — the congruent
  table, `A=752` fixed, peak-angle fractions 0.949/0.984, the Rayleigh
  resolution-floor arithmetic (0.9484/0.5967/0.0949, break-even at
  spread=39.3%), and the 78-call/6266.6-CPU-s/30.64-min budget. **No
  hand-typed figure found — R4 clean.**
- Cross-checked every number in `phase4_results.md`/`NOTES.md` against
  `results.json` directly: per-config free periods and R² (all 4 configs),
  linear-fit slope/intercept/R² (0.0025564/2.3459/0.8664), `spread_40_80`
  (3.90%), `max_pair_spread` (3.93%), `trend_resolution_ratio` (0.095), all
  6 pairwise spreads/ratios, both `Block SETTLE-C60C70` ratio sets
  (2.5e-4/4.3e-5/1.5e-4/4.0e-5), both `P-071-4` ratios (1.234/1.047), and
  both `P-071-5` ratios (1.71/3.55). **Every single one matches exactly.**
  This is the cleanest numeric-accuracy record of any cycle I've reviewed —
  no finding below is a mismatch between the write-up and the data.
- Spot-checked 4 of the 7 (really 8, with the audit's own #7/#8) mandatory
  Red-Team fixes in code, not prose: (1) `score_settle_c60c70` and
  `Block SETTLE-C60C70` — implemented, correctly scored on `GATE_HARD` per
  idealization 10; (2) `rayleigh_resolution_ratio()` gating both CONFIRM
  and REFUTE — implemented in `score_trend_and_pairs`; (5) `_free_period_search`
  imported by reference with an asserted-defaults check — confirmed at
  `design_geometry.py:125-134`, the assertion is live code, not a comment;
  (6) `fdtd_budget_minimum()`'s docstring correctly names Block
  SETTLE-C60C70 and the resolution-floor computation as never-de-scoped.
  All four implemented as specified. `lab/caveat_lint.py` reruns clean (0
  required-site failures).

## 1. Is the Combined Verdict (NEITHER) justified by the data?

**Yes, the verdict itself is correct** — G1 passed, both binding
preconditions genuinely CONFIRM (settling ratios 2–4 orders of magnitude
under `GATE_HARD`; peak-cell R3 ratios cleanly inside [0.3,3.0]), and the
raw trend statistic (spread 3.9%, R²=0.866) does not clear either
pre-registered band. NEITHER is the honest, pre-committed outcome, not a
dressed-up PARTIAL.

**But the write-up materially overclaims *why* it's NEITHER, in a way that
matters for how confidently this result should be cited going forward.**
This is my sharpest finding.

### Finding A (sharpest): the "resolution-floor gate was decisive" claim doesn't survive checking the code's own reason field

`phase4_results.md` states: *"**Resolution-floor gate (mandatory fix
2) — decisive.**"* `NOTES.md`'s Learned §1 goes further: *"Without the
resolution-floor gate, this cycle would likely have reported a spurious
REFUTE (`max_pair_spread` clears 15%) or at minimum an unqualified 'trend
not significant' reading."*

I checked this against `results.json` directly:

```
trend.raw_confirm       = False
trend.raw_refute        = False
trend.unresolved_only   = False
trend.trend_resolved    = False
trend.all_pairs_resolved= False
combined_reason: "...raw trend statistic (spread/R^2) landed in the gray
                   zone between the CONFIRM and REFUTE bands..."
```

`raw_refute` requires `max_pair_spread ≤ 15% **AND** R² ≤ 0.30`
(`TREND_REFUTE_MAX_R2 = 0.30`, `design_geometry.py:251`). `max_pair_spread`
(3.93%) clears its half, but **R²=0.8664 fails the R² half on its own,
with or without any resolution-floor gate** — that conjunct was part of
the pre-committed REFUTE band from `phase1_proposal.md` onward, unchanged
through Phase 3. The code confirms this precisely: `unresolved_only=False`
means the resolution-floor branch of the NEITHER-reason logic
(`run.py::main`, the `if trend["unresolved_only"]:` branch) was **never
even reached** — the actual reason string that fired is the plain
gray-zone catch-all, not the resolution-floor branch. Removing the
resolution-floor gate entirely and re-running the exact same pre-committed
REFUTE band on this exact data would **still** produce NEITHER, not
REFUTE, because R² alone already disqualifies it. `phase4_results.md`'s
own body actually gets this half right two paragraphs earlier ("R² = 0.8664
sits far above REFUTE's own R² ≤ 0.30 ceiling... too well-fit-looking...
to count as 'flat'") — the overclaim is specifically in labeling the
resolution-floor gate "decisive" and in NOTES.md's counterfactual claim
about what would have happened without it.

This does **not** change the Combined Verdict (still correctly NEITHER),
and the resolution-floor computation is real, correctly computed, and
scientifically important context (it tells you *why you shouldn't trust
either band even if the raw stat had cleared one* — a live risk for
`C40` vs `C60`, e.g., where `max_pair_spread`=3.34% together with the
already-known R² structure could plausibly clear a REFUTE-shaped
band in a differently-parameterized future test). But as *this cycle's*
mechanism for reaching NEITHER, it is inert, and describing it as
"decisive" overstates what the code's own logic shows. **A future reader
citing "the resolution-floor gate prevented a spurious REFUTE this cycle"
would be citing something the code itself does not support.**

### Finding B: the pre-registered `FROZEN_PREDICTIONS` text does not match the code that scored `Block SETTLE-C60C70` — inside the same commit

`NOTES.md` states its predictions table is *"Reproduced verbatim from
`run.py`'s `FROZEN_PREDICTIONS` string (this program's own established
discipline: the committed prose and the executed code cannot drift
apart)."* That claim is false for one row. `run.py`'s own
`FROZEN_PREDICTIONS` string (lines 99–102) reads:

> `Block SETTLE-C60C70 ... relative to |dC(2800-1400)| at the same cells
> (1400 values reused from exp-065's own committed Block SWEEP -- loaded
> programmatically). ... CONFIRM (settled) <= 1% relative ... REFUTE
> (unsettled) >= 5% relative...`

But the function that actually scores it, `score_settle_c60c70()` (same
file, lines 441–475), does something categorically different — and says
so in its own docstring: *"37.2/41.4deg are off the coarse angle grid
exp-065's own committed STEPS=1400 data covers -- there is no 1400-STEPS
comparator at these exact cells, so this cycle's own new settling check is
scored on the ABSOLUTE 2800-vs-4200 shift relative to GATE_HARD..."* This
is exactly what actually ran (`results.json`'s `rel_to_gate_hard` field,
`gate_hard=0.001`), and it is exactly what `NOTES.md`'s own predictions
*table* (as opposed to its verbatim-reproduction *claim*) and idealization
10 correctly describe. `git log -p` confirms both the stale
`FROZEN_PREDICTIONS` text and the correct `score_settle_c60c70` docstring
were introduced in the **same** Phase-3 commit (`1bd57d2`) — this is not
later drift, it's an internal self-contradiction present at the moment
"predictions frozen BEFORE any run" was committed. It did not affect the
outcome (the code, not the stale prose, is what ran, and it used the
correct construction), but it is precisely the failure shape this
program's own non-negotiable discipline ("the committed prose and the
executed code cannot drift apart") exists to prevent, and it slipped past
five blind Phase-2 critiques and Red Team's own audit undetected.

### Finding C: a latent scoring bug in the resolution-floor code, inert this cycle but real

`rayleigh_resolution_ratio()`'s own docstring
(`design_geometry.py:280-292`) explicitly warns: *"Two periods identical
returns +inf (trivially unresolvable AND uninformative -- treated as
unresolved by the caller, never as a false REFUTE)."* But the caller,
`score_trend_and_pairs()` (`run.py:389-390`), computes
`resolved=bool(ratio >= dg.RESOLUTION_FLOOR_RATIO_THRESHOLD)` — and
`inf >= 1.0` evaluates `True` in Python. The exact C70–C80 tie
(`resolution_ratio: Infinity`) is marked `"resolved": true` in
`results.json`, contradicting the design's own stated intent. This is
inert this cycle only because the other 5 of 6 pairs are independently
unresolved, so `all_pairs_resolved` is `False` regardless. But it is a
live bug: if a future reuse of this exact machinery produces an
exact-tie pair *alongside* pairs that genuinely clear the resolution
floor, this bug would let a discretization-grid coincidence — the same
species of artifact `NOTES.md` itself flags as "plausibly a grid-search
discretization coincidence, not evidence" — silently count as "resolved"
toward `all_pairs_resolved=True`, which gates a REFUTE. Cheap, one-line
fix (`resolved = bool(math.isfinite(ratio) and ratio >= threshold)`)
before this scoring code is reused.

### Finding D: no caveat-lint registry entry protects this cycle's own headline number

exp-070's own Phase-5 mandatory-fix docket added a
`caveat_lint_config.json` entry (`exp070-t28-named-constant-null-control`)
specifically because its headline near-miss numbers (`A_eff≈518.81`,
`A_alt≈233.19`) looked like strong evidence by raw closeness alone and
needed their disqualifying context locked to any future citation. exp-071
has the identical shape of risk: `P*(ABSORB)` rises monotonically with
`R²=0.8664` — a number that, quoted alone in a future LOGBOOK entry or
proposal, reads as a strong trend. `lab/caveat_lint_config.json` has no
entry for exp-071 at all (confirmed by grep), and this cycle's own
mandatory-fix docket (7 items, `phase3_synthesis.md`) does not include
adding one — a regression of the exact registry-propagation practice
established one cycle ago for the identical failure class (raw-statistic-
looks-decisive-but-is-gated-NEITHER). `lab/caveat_lint.py` currently runs
clean only because there's nothing registered to check.

## 2. Does the Combined Verdict over- or under-claim in either direction?

Neither, on the label itself — NEITHER is correctly earned and correctly
not padded into a soft PARTIAL. Where I'd push back is narrower than the
verdict: the write-up's *narrative* about the resolution-floor gate's role
(Finding A) inflates how load-bearing mandatory fix 2 was **this
specific run**, even though the fix itself (gating both directions) is
sound design that will matter on a future run with different numbers. The
honest framing is: "the raw trend statistic already failed to clear either
band on its own; the resolution-floor computation independently confirms
neither band *could* be trusted here even if it had cleared" — not "the
gate resolved the ambiguity" or "without it we'd have gotten a spurious
REFUTE."

## 3. Mandatory-fix spot-check summary

| # | Fix | Verified in code? |
|---|---|---|
| 1 | Block SETTLE-C60C70, GATE_HARD-relative, binding precondition | Yes — implemented, but `FROZEN_PREDICTIONS` text describes a different (1400-relative) construction (Finding B) |
| 2 | Resolution floor gates both CONFIRM and REFUTE | Yes, implemented correctly — but inert for this cycle's actual verdict (Finding A); has a latent tie-handling bug (Finding C) |
| 3 | ABSORB-not-material caveat reinstated | Yes — `ABSORB_NOT_MATERIAL_CAVEAT` printed unconditionally, CONFIRM branch renamed |
| 5 | `_free_period_search` imported by reference + defaults asserted | Yes — live `assert` at import time, not a comment |
| 6 | De-scope docket protects new mandatory fixes | Yes — `fdtd_budget_minimum()` docstring names both |

No item I checked was claimed-but-not-implemented. The gap is not
non-compliance; it's an internal-consistency defect (B) and a
narrative-overclaim (A) inside fixes that were otherwise genuinely applied.

## 4. Checkpoint determination

I concur none of the five criteria fire. This is real, verified process
progress (both mandatory Phase-2 concerns tested and closed cleanly) on a
genuinely narrowed-not-answered question, matching the program's own
non-firing precedent. Findings A–D above are the species of defect this
program has fired criterion 4 on before (Iterations 36–40) when they
survived undetected into a later cycle — none of these have yet done that;
this is Phase 5 catching them within-cycle, which is the discipline
working. They should still go on record, not be waved off, because Finding
A specifically risks exactly that kind of downstream miscitation if
uncorrected before LOGBOOK's iteration entry is written.

## 5. Rating: **PARTIAL**

Real, verified narrowing: both of Red Team's Phase-2 load-bearing concerns
(settling, resolution floor) were genuinely tested, not just asserted, and
came back clean; the per-config periods do rise smoothly and monotonically
with `ABSORB` depth, a real shape worth carrying forward; the Combined
Verdict is honestly NEITHER, not a hedge. Not PROMISING — the substantive
causal question (does the ~2.84°-family period track `ABSORB` depth?) ends
this cycle exactly where it started, structurally: unresolved, now for a
quantified reason instead of an unquantified one. Not RULED-OUT — nothing
here forecloses either hypothesis; the window's own physics, not the data,
is what's inconclusive.

## 6. Proposed next move for T28 (Iteration 49) — concrete and falsifiable, this seat's lens

Before any new FDTD dense-sweep repeats this test, **pin the required
window size numerically, in code, before spending calls** — the same
"pin the number before scoring against it" discipline my charter states
for perceptual thresholds, applied here to instrument resolving power:

1. **Do not re-run the identical 36°–42° window a third time.** It has now
   been used at this exact resolving power in exp-069, exp-070 (desk-only),
   and exp-071, and `design_geometry.py`'s own arithmetic shows it supplies
   `Δ(sinθ)=0.0813`, while resolving the smallest pairwise difference in
   play (C40 vs C60, 3.3% spread) needs `Δ(sinθ)≥0.136` (1.7× the current
   window) and resolving the full C40-vs-C80 spread needs `Δ(sinθ)≥0.857`
   (10.5× the current window, Red Team's own §1 figure, independently
   reproduced here). A fourth run at the same window would not be a new
   test.
2. **Concrete option A — widen the window and pre-register the exact
   multiple needed.** Compute, before any FDTD call, the window width in
   degrees required to reach `resolution_ratio ≥ 1.0` for the C40-vs-C60
   pair specifically (the smallest, hence hardest, gap) using the already-
   built `rayleigh_resolution_ratio()` function, and require the proposed
   `DENSE_ANGLES` span to clear it — not the old 6° window plus a vague
   aspiration to "widen it."
3. **Concrete option B — abandon the angular free-period-fit discriminator
   entirely** (NOTES.md's own second suggestion) in favor of a direct
   pairwise measurement that doesn't require Rayleigh-resolving two close
   periods against each other at all: e.g. a fixed-angle, multi-STEPS
   phase-tracking comparison between `C40` and `C60` (not `C80`, the
   smallest ABSORB gap, hence the sharpest test of "does the period track
   depth continuously") — falsifiable band to be pinned before the run,
   not after.
4. **Same-shift, zero-FDTD-cost, before Iteration 49's proposal is
   written:** fix Findings B–D above — reconcile `FROZEN_PREDICTIONS`
   with `score_settle_c60c70`'s actual construction (or vice versa, if the
   1400-relative scheme is somehow recoverable — check before assuming
   GATE_HARD-relative is the intended final form), patch the `inf`-tie
   `resolved` bug with an explicit `math.isfinite` guard, and add a
   `caveat_lint_config.json` entry locking the resolution-floor context to
   any future citation of exp-071's `R²=0.8664`/`spread=3.9%` trend
   numbers. None of these require a new FDTD call or touch `lab/`.
