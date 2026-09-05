# Phase 2 Critique — ELECTROMAGNETISM (blind) — Panel Iteration 91 (exp-114)

*Charter: field/wave behavior, impedance matching, energy coupling; owns
reciprocity/passivity/causality bookkeeping and formalizes what T1
permits/forbids. This seat has not seen any other seat's critique this
cycle.*

## Charter-fit / T1 confirmation (not taken on faith)

I read the full proposal, `run114.py`, and `chunk_runner114.py` before
writing anything below. This is genuinely pure instrument-calibration
work: no `sigma(I)`/`sigma(x,t)`/angular-selectivity/sub-threshold content
appears anywhere, the material recipe (`materials.graded_black_shell`,
`materials.pec_disk`) is reused byte-for-byte unchanged from the already-
validated `fixedabs` family, `tau_shell` is held invariant across r by
construction, and no constraint-1/2/3/4 verdict is scored anywhere in the
document. **T1 escape-route "N/A" is correct**, not merely asserted — my
own charter question does not bind this cycle. No reciprocity/passivity/
causality bookkeeping issue arises because no field-level physics is
being varied at all, only a geometry-scaling function's evaluation point
and a wall-time cost model.

## Verification performed (independently re-run, not taken from the document)

- **`R110.cost_gate_check()` hardcoding claim** — confirmed by direct
  read of `experiments/110-.../run.py` line 398:
  `kappa_ratio = kappa_of(312) / kappa_of(156)` is literally hardcoded
  inside the function body, not parameterized by a target r. The
  proposal's claim that reusing it verbatim for r=234 would silently
  apply the wrong ratio (2.0 instead of 1.5) is correct and the
  deviation (`cost_gate_check_r234()`, a structural duplicate with only
  that one line changed) is necessary, not a style choice.
- **All headline numbers reproduced by independent execution**, not by
  reading the document's prose: `1.5**3.2053299988171697 = 3.6680107…`,
  `2.0**k = 9.2236003…`, ratio `= 0.397677 (39.77%, not MATERIALS'
  Iteration-90 "~32%")`, `projected_234_total_s = 2705.25s` (75.0%
  margin), matching `run114.py --predictions-only`'s own live output
  token-for-token.
- **Geometry identity** — re-ran `python3 run114.py --verify-geometry`
  myself: `{"pass_": true, "mismatches": []}` at r=156/234/312.
- **R9 commensurability of the R31 control reuse** — read
  `run113.py::r31_control_ratio`/`combine_control_readings` directly:
  both operate ONLY on the r=156/cpl=25 pilot's own re-timing this
  session vs. `HISTORICAL_PER_STEP_S` (also r=156-derived) — neither
  references a target r at all. Reuse is genuinely commensurable; only
  `cost_gate_check_r31_r234()` (the one function that must know the
  target-r-specific `kappa_ratio`) was rewritten, mirroring
  `R113.cost_gate_check_r31()`'s structure exactly except for that one
  substitution. No unit/normalization mismatch.
- **"Zero real `Sim.run()` calls in Phase 1"** — confirmed. `run114.py`
  contains no `.run(` call at all (only prose mentions). `chunk_runner114.py`
  does contain two (`step_budgeted`, `_time_control_blend`) but this
  cycle's own scratch directory
  (`/tmp/.../scratchpad/exp114/`) is empty — no walltime logs, no
  checkpoints, no `r31_control.json` — and `git status`/`git log` show no
  `lab/` diff and a single already-committed Phase-1 commit. The claim
  holds.
- **Trust suite**: `python3 lab/validation/run_all.py --only 12346789`
  re-run from repo root this session — **41/41 green**, no regression.

## One steel-man (143 words)

The cycle's one real code deviation, `cost_gate_check_r234()` replacing
`R110.cost_gate_check()`, is necessary and minimal, and I verified it
myself rather than trusting the proposal's word. R110's `run.py` line 398
hardcodes `kappa_ratio = kappa_of(312)/kappa_of(156) = 2.0` inside the
function body, not parameterized by r; calling it unmodified for r=234
would silently apply the wrong ratio, projecting cost about 2.5 times too
high (`2.0^k/1.5^k`, k=3.2053, equals 2.51). `run114.py`'s replacement
duplicates only that one line, reusing every other constant unchanged. I
independently re-ran `run114.py --verify-geometry` and got `pass_=true`
at r=156/234/312. The R31 control machinery (`r31_control_ratio`/
`combine_control_readings`, from `run113.py`) is reused unmodified
without an R9 commensurability problem: both functions characterize only
this session's throughput against the r=156 pilot, never the target r;
only the gate wrapper, correctly rewritten to thread kappa_ratio=1.5,
needed changing. Zero `Sim.run()` calls in `run114.py`; `chunk_runner114.py`'s
calls are confirmed uninvoked (empty scratch dir, no walltime logs).

## One sharpest attack (141 words)

The pre-registered CONFIRM/REFUTE bands (0.15/0.30), named "the
falsifiable heart of this cycle," rest on a category error I verified
independently. `run114.py` justifies `KAPPA_EXPONENT_CONFIRM_REL=0.15` as
matching "R28's own already-tolerated founding miss magnitude (~15%)."
But R28's ~15% is a deviation in projected-COST space: measured
r=312/r=156 ratio 9.224x vs. an exponent=3.0 projection of 8.0x,
`(9.224-8.0)/8.0=15.3%`. `classify_kappa_exponent_check()` instead
computes `rel_dev` directly on the EXPONENT:
`|exponent_234-3.2053|/3.2053` — a different quantity. I computed the
exponent-space deviation implied by that same historical episode:
`log(9.224)/log(2)=3.2054` vs. 3.0 is only a 6.4-6.8% exponent-space
miss — roughly half the 0.15 band it is cited to justify. At
kappa_ratio=1.5 (this leg) a ±15% exponent swing maps to only
-18%/+22% multiplier swing, so no verdict currently flips, but the
band's own stated justification is numerically wrong, not merely
imprecise, and the error compounds at kappa_ratio=2.0 (would license
~28-40% multiplier misses under the same nominal 0.15).

## Verdict: **support-with-changes**

Run the r=234 leg as scoped — the geometry, the cost-gate adaptation,
and the R31 control reuse are all independently verified correct. But
correct the CONFIRM/REFUTE band derivation for
`classify_kappa_exponent_check()` before Phase 4's own real `t234` is
scored against it: either (a) recompute `KAPPA_EXPONENT_CONFIRM_REL`
directly in exponent-space from the actual precedent
(≈0.065-0.07, not 0.15), or (b) keep 0.15 but drop the false claim that
it "matches R28's own ~15% miss" and justify it as an independent,
looser choice on its own terms. This is an R9-class commensurability
defect in the classifier's own justification (conflating an
exponent-relative-deviation with a multiplier-relative-deviation), not
in the arithmetic that was actually re-run — everything I could
independently execute reproduced bit-exact.

## Single parameter change that would flip this to full support

Replace `KAPPA_EXPONENT_CONFIRM_REL = 0.15` with a value independently
re-derived in exponent-space from the R28 precedent it claims to match
(≈0.065-0.07), or remove the R28-precedent citation and state the 0.15
choice as freestanding — either one resolves the commensurability defect
without touching anything else in the document.

## Trust suite

`python3 lab/validation/run_all.py --only 12346789` re-run this session
from repo root: **41/41 green**, no regression.
