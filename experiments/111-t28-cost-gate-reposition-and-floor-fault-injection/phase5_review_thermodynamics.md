# Phase 5 Review — THERMODYNAMICS (self-review of this cycle's own rotation-lead proposal)

**Panel Iteration 88, exp-111.** Charter: where absorbed energy goes;
always asks what re-radiates and whether it would be detectable; owns the
per-proposal energy sidecar. This is a self-review — extra scrutiny
applied throughout, not less; every headline number below was re-derived
from primitives by actually running the committed code in this session,
not by trusting NOTES.md's or results.json's own prose.

## Verdict: **CONFIRM-WITH-GAPS**

All seven mandatory-fix-gating claims (item 1's FI-A/B/C + non-regression,
item 2's all 5 cases, item 4's all 3 cases) reproduce bit-exact from
committed source, independently re-run by me end-to-end. The self-disclosed
FI-D miss is honestly reported with a mechanism that is *correct but
incomplete* (below). T1/energy-sidecar N/A is genuinely, verifiably clean —
I checked this myself rather than accepting the claim. Two real,
non-blocking gaps survive Phase-3 freeze that no Phase-2 critique (including
my own seat's) or the Phase-2 Red Team audit caught, because both postdate
Phase 2 (they concern the frozen NOTES.md/results.json text itself). Neither
is outcome-reversing; neither fires any existing R-rule on a single instance.

## 1. T1 / energy-sidecar N/A — independently confirmed, not trusted

Ran `git diff` on every line this cycle actually touched
(`experiments/110-.../{run.py,chunk_runner.py,analyze.py}`) and grepped it,
plus every new file in `experiments/111-.../`, for `sigma_abs`, `sigma_ext`,
`absorb`, `extinction`, `p_abs`, `watt`, `joule`, `thermal`, `temperature`:
**zero hits, in either the diff or the new files.** `classify_item_i_local`'s
patch touches only a `floor>0.0` boolean and a `nan`-vs-`inf` fill on
angular-*scattering*-pattern arrays (not absorbed power); `cost_gate_check`/
`check_cost_gate_for_312` touch only wall-clock projection and orchestration
ordering. **The N/A claim holds exactly as stated — nothing in items 1/2/4
touches any energy quantity this cycle, confirmed structurally, not merely
asserted.** Item 3 (the one item with physical content) is deferred,
untouched. This is the cleanest T1-N/A self-check I can produce for my own
seat's own cycle.

## 2. Independently re-derived key numbers (all bit-exact against committed source)

- `KAPPA_COST_EXPONENT`: re-ran `ln(t312/t156)/ln(2)` against exp-110's own
  `results.json` myself: `t156=752.2232966423035`, `t312=6938.207038640976`,
  ratio `9.223600318696624`, exponent `3.2053299988171697` — **exact match**.
- Re-ran `floor_fault_injection_control.py`, `gate_reposition_control.py`,
  `cost_gate_formula_control.py`, `cpl_cost_table.py` fresh (not read-only):
  every case reproduces **bit-identical** to the committed
  `*_output.json` files (FI-A `4.999999999999996e-4`, FI-B `0.0`, FI-C
  `floor_degenerate=True`/all-False/no-inf, FI-D floor range
  `[0.0, 3.53406793027197e-4]` = 70.7% of amplitude at max; gate-reposition
  5/5 PASS; formula control 3/3 PASS incl. discriminating case
  `10799.0s`(PASS, old) vs `13695.778228220666s`(FAIL, new); cpl table
  cpl=30 "Both r" `=7.2098h`, confirming MATERIALS' caught slip).
- Ran the house trust suite myself: **43/43 green**, 141s.
- Ran `git diff --stat` across the whole Iteration-88 commit range against
  `lab/`: **zero output** — zero `lab/` diff independently confirmed.
- Confirmed house discipline from `git log` timestamps directly, not
  narrative: Phase-3 synthesis commit `9cee2bf` (21:29:28 UTC) precedes
  Phase-4 results commit `f095726` (21:33:08 UTC) by ~3.7 minutes; `git show
  --stat` on `9cee2bf` shows the code patches landed in that same commit,
  "nothing executed for real yet" per its own message — predictions-before-run
  house discipline verified, not merely trusted.
- Verified PHOTONICS' Phase-2 claim that the two named bins (`-146.25°`
  r=156, `+168.75°` r=312) are NOT a mirror pair of each other: computed
  indices directly (`i=4`↔mirror `43`≡`+146.25°`; `i=46`↔mirror `1`≡`-168.75°`)
  — confirmed false that they pair with one another.

## 3. Gap found #1 — NOTES.md's Phase-3 disposition table overclaims mandatory-fix 5's completeness

NOTES.md's own Phase-3 table states fix 5 was "Implemented as:
`predictions_result_88.py`... `build_predictions_text_88()`/
`build_result_text_88()`, **both** assert `DISCLAIMER_88 in ...`." I read
`predictions_result_88.py` directly and grepped the whole exp-111 directory
for `assert`: there is exactly **one** `assert DISCLAIMER_88 in ...` call in
committed code (line 180, inside the `if "--predictions-only" in sys.argv`
branch of `__main__`), and it fires only on `predictions_text`.
`build_result_text_88()` itself contains no assert, and **no committed
script anywhere in this tree ever calls `build_result_text_88()` with real
data and checks its output** — there is no `--result-only` branch, no
`finalize.py`-equivalent driver (contrast exp-110's own `finalize.py`,
LOGBOOK Iteration 87, which asserted `DISCLAIMER in` *both*
`predictions_text`/`result_text` as committed, re-invocable code).

I independently tested whether the *content* is at least right: I loaded
the four real `*_output.json` files this cycle produced and called
`build_result_text_88(fi, gate, formula, cpl)` myself — it did **not**
reproduce `results.json["result_text"]` byte-for-byte (missing one line)
until I supplied the omitted `wall_time_source` keyword argument, at which
point it matched **exactly**. So the content is genuinely correct and
reproducible from committed primitives, given the right invocation — this
is not a fabricated or hand-typed figure. But the specific claim "both...
assert" is false as literally stated: only one of the two functions has a
committed, re-invocable self-check; the other's real data must have been
fed to it through an ad hoc invocation this session never captured as
code. This is a narrower recurrence of this exact sub-thread's own
"predictions half done, result half not" R23 shape (Iteration 85/exp-108,
where `build_result_text()` had zero call sites at all) — here the
function *was* genuinely exercised with real data, but its own asserted
self-check was not, and NOTES.md's own frozen text claims otherwise.
Non-blocking (content correct, zero verdict-arithmetic impact), but a
genuine documentation-accuracy defect surviving Phase-3 freeze that no
Phase-2 critique could have caught (Phase 2 predates this code) and that
I would not have caught either without actually trying to re-invoke the
function against the real committed outputs myself.

## 4. Gap found #2 — the FI-D Interpretation's mechanism is correct but incomplete: a second, unstated factor

The task specifically asked me to stress-test this. NOTES.md's
Interpretation paragraph explains the phase-0°/180° exact-zero collapse as
following from `BIN_CENTERS_DEG[i] == -BIN_CENTERS_DEG[47-i]` (confirmed —
I verified this identity holds exactly for all 48 bins) plus "cos is even
in its argument." This is directionally correct and I confirmed the
qualitative conclusion (bit-exact match to FI-B's own mechanism at those two
phases). But I went one step further and derived the closed form directly:
writing `θ_i = 2π·BIN_CENTERS_DEG[i]/P*`, the per-pair difference is

```
arr(i) - arr(47-i) = -2·amplitude·sin(phase)·sin(θ_i)
```

(from `cos(A+B) - cos(A-B) = -2 sin A sin B`). **This vanishes identically
across every bin pair if and only if `sin(phase)=0` — i.e. `phase = 0°` or
`180°` — completely independently of `P*`.** I verified this numerically by
re-running FI-D's own construction at four other periods (`1°`, `13.7°`,
`100°`, plus the real `P*=2.8421°`): the exact-zero collapse occurs at
`phase=0°/180°` **in every case**, with no other period-dependence. **This
is the second factor the Interpretation paragraph misses**: the collapse is
not a special aliasing interaction between T28's own established
`P*=2.8421°` and this instrument's `7.5°` bin pitch — it is a completely
generic property of testing with a *single pure cosine* on any
mirror-symmetric bin grid, true for literally any period. Framing it via
"`BIN_CENTERS_DEG`'s own convention" is correct but incomplete: the missing
half of the explanation is that the choice of test-function *family*
(a single sinusoid), not the specific period value, is what guarantees two
degenerate phases per sweep. Practically, this means FI-D's own claim to
"characterize... the realistic aliased/intermediate regime" is weaker than
stated: a pure single-frequency perturbation can **never** fully escape
periodically revisiting the FI-A/FI-B pure extremes, at *any* chosen period
— a structural property of the test-function family, not evidence specific
to T28's real echo mechanism. A genuinely more informative probe of the
"neither clean odd nor even" regime PHOTONICS originally asked for (Phase-2
critique) would need a non-sinusoidal or multi-harmonic perturbation shape,
which no case here provides. Non-blocking (FI-D remains explicitly
informational, and its qualitative point — phase-dependent recovery between
the two extremes — still stands over the other 22/24 swept phases), but a
real refinement to the record's own stated mechanism that neither the
proposal, its critiques, nor the Director's own Interpretation paragraph
identified.

## 5. Self-review honesty check — did THERMODYNAMICS (this cycle's own proposing seat) under-report anything?

Actively looked for this failure mode, per the task's instruction. The one
place a proposing seat might be tempted to round up is exactly where I
found gap #1: NOTES.md's own table states a mandatory fix was implemented
"in full" ("both... assert") when only half is committed, re-invocable
code. I do not believe this was a deliberate soft-pedal — the *content* is
genuinely correct (I verified it reproduces exactly once the right argument
is supplied), and the omission is a process/reproducibility gap, not a
numeric or physical one — but it is precisely the shape of claim a
self-review has the strongest incentive to wave through ("the text is
right, so why check whether the code that produced it is committed?") and
the shape an outside blind seat would need actual code-level verification,
not just prose-reading, to catch. I did the code-level verification. No
other under-reporting found: the T1/N/A claim checks out clean (§1), and
FI-D's own falsification was already disclosed honestly in NOTES.md before
I started (not something I had to surface myself) — I only added *why* the
disclosed mechanism is incomplete, not that a mechanism was hidden.

## 6. Ranked top-3 candidate directions for Iteration 89

1. **Execute item 3 (PHOTONICS' cpl-refinement spot check, `cpl=25`,
   r=156-alone-first) under this cycle's now-verified, genuinely-upstream
   cost gate — and, from THERMODYNAMICS' own seat, add one cheap
   cross-check while the r=156 capture is in hand: pull the already-computed
   per-margin `sigma_abs`/`sigma_ext` ledger (from `reproduction_precondition`,
   zero new FDTD beyond item 3's own spend) and check whether either named
   bin's cpl-refined local structure has ANY counterpart in a per-margin
   absorbed-power delta.** `angular_scattered_pattern` is a scattering
   diagnostic; nothing in this sub-thread has ever asked whether a localized
   scattering anomaly at these two bins also shows up as a localized
   absorption signature — exactly the question my charter exists to ask
   ("what re-radiates and whether it would be detectable"), and it costs
   nothing beyond item 3's own already-planned spend.
2. **Close gap #1 (above): wire a committed, re-invocable driver
   (`--result-only` branch in `predictions_result_88.py`, or a small
   `finalize_88.py`) that actually calls `build_result_text_88()` with real
   data and fires `assert DISCLAIMER_88 in result_text_88`, matching R23's
   own founding standard (both halves committed, both independently
   re-confirmed by execution).** Cheap, same-shift-sized, and prevents this
   exact "content right, process unrecorded" shape from recurring a third
   time on this channel.
3. **The `R2_SMOOTH_THRESHOLD=0.90` re-derivation (now a fifth consecutive
   cycle deferred), bundled with validating `KAPPA_COST_EXPONENT`/
   `COST_GATE_SAFETY_MARGIN` at a genuinely different `kappa_ratio`** before
   either constant is trusted at any future geometry (e.g. the still-queued
   r=624 point) — both are single-data-point empirical fits this cycle
   itself explicitly disclaims as non-generalizing; a future r=624 cycle
   that reuses either without re-deriving it would be exactly the "assumed
   transfer" this cycle's own Idealizations warns against.

## Independently reproduced artifacts

`floor_fault_injection_control.py`, `gate_reposition_control.py`,
`cost_gate_formula_control.py`, `cpl_cost_table.py` all re-run fresh this
review, outputs bit-identical to committed `*_output.json`; house trust
suite re-run fresh, 43/43 green; `git log`/`git show --stat`/`git diff
--stat` used directly to verify commit ordering and zero `lab/` diff.
