# exp-111 — Panel Iteration 88 (candidate)

**Lead seat: THERMODYNAMICS (rotation lead, PHOTONICS→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM→VISION SCIENCE).** Governance/
instrumentation cycle continuing the T28 sub-thread. Executes the
Reconciled Iteration-88 queue (LOGBOOK.md Iteration 87, exp-110's own
Combined Verdict; full text `experiments/110-t28-item-i-local-norm-and-
controls/phase5_redteam_audit.md` §8). Tier-0 item 0 (ruling on the
Iteration-85 Checkpoint-4/R24 firing) is Marsh's call, explicitly out of
scope, not attempted — the Tier-0 text-correction/ratification items are
already applied, same-shift, inside exp-110's own record.

## 1. Mechanism/execution narrative (≤300 words)

Execute Tier-1 items 1, 2, and 4 in full (all zero new FDTD, per the
queue's own text), and make an explicit, reasoned scoping decision on item
3 (below: **deferred**).

**Item 1** closes the last open R18 gap on last cycle's own new
instrument, `mirror_pooled_floor`/`classify_item_i_local`: four
deterministic synthetic 48-bin arrays show (a) the floor correctly
recovers a known injected ODD/asymmetric perturbation; (b) the floor is
structurally blind to an even-larger SYMMETRIC/common-mode perturbation
(the disclosed blind spot, now measured, not merely asserted); (c) a
genuinely degenerate, fully mirror-symmetric input drives the floor to
exactly 0.0 — QUANTUM's own Phase-5 gap. Rather than leave that gap as an
unscored observation (R24 discipline), I propose a small code fix: guard
`resolved` on `floor > 0` and add an explicit `floor_degenerate` field —
verified to change nothing on the 12 real, already-committed cells
(bit-identical `n_resolved`).

**Item 2** repositions the R27/R28 cost gate genuinely upstream:
`chunk_runner.py` itself refuses any r=312 chunk unless r=156's three
scenes are complete and `cost_gate_check()` clears — verified by a fully
mocked control (zero `Sim.run()` calls), not merely by re-confirming a
branch exists. A grounding-fact check, this session, found the queue's own
premise that r=156's wall-time logs are "already-logged" is false — that
scratch is gone (the identical shape as the Iteration-86/87 gap) — so the
control uses synthetic logs and the fix's own docstring describes the
mechanism, not stale historical numbers.

**Item 4** replaces `kappa_ratio**3.0` with an empirically re-derived
exponent (3.2053, independently recomputed here from exp-110's own
committed `results.json`) plus a 10% safety margin, verified via a
formula-level fault-injection control.

**Item 3** (PHOTONICS' cpl-refinement spot check) is deferred, reasoned
explicitly in §3 below.

## 2. Parameter table

### 2.0 Grounding-fact correction (independently re-verified, this session, before proposing anything)

| Claim in the Iteration-88 queue | Checked | Result |
|---|---|---|
| Item 2: "using r=156's own already-logged `total_wall_time()` figures" | `ls "/tmp/claude-0/.../99fb0d5c-.../scratchpad/exp110"` (exp-110's own hardcoded `SCRATCH`) | **Path does not exist in this session.** exp-110's own per-chunk wall-time log files (`r156_*_walltime.json`) live only in that prior, now-defunct session's scratchpad — the identical shape of gap Iteration 87 found in exp-108's own pickles (LOGBOOK Iteration 87). **Non-blocking**: item 2's own fault-injection control (§2.3) needs no real historical log data — it exercises the gate's *logic* with synthetic logs. But `check_cost_gate_for_312()`'s own docstring must describe the *mechanism* (any live session's own fresh `log_wall_time()`/`total_wall_time()` calls, populated by that session's own real r=156 run), not assert that specific historical numbers are read back this cycle, since **zero real `Sim.run()` calls happen anywhere in this cycle** (items 1/2/4 are synthetic-only, matching the queue's own "zero new FDTD" text). |
| R4 re-derivation, exponent ≈3.2 | `python3 -c "..."` against exp-110's own committed `results.json` (not hand-typed) | Confirmed: `t156=752.2232966423035s`, `t312=6938.207038640976s`, ratio `9.223600318696624`, `kappa_ratio=2.0`, `ln(ratio)/ln(2) = 3.2053299988171697`. Matches the phase5 audit's rounded "≈3.2" exactly. |
| Real floor range / `n_resolved` sums cited by exp-110's own Result | `python3 -c "..."` against `results.json` | Confirmed exactly: floors `2.3458e-4`–`2.0959e-3`; `n_resolved` r=156 `{24:32,32:34,40:36,48:34,57:34,65:33}` (Σ203/288); r=312 `{24:36,32:38,40:40,48:36,57:36,65:36}` (Σ222/288); `n_total=48` bins/margin, confirmed both r. |

### 2.1 Item 1 — `classify_item_i_local` fix + fault-injection control

**File to modify**: `experiments/110-t28-item-i-local-norm-and-controls/run.py`

```python
def classify_item_i_local(r, margin, pattern_peccored, pattern_hollow, pattern_delta,
                           K=MIRROR_FLOOR_K, percentile=MIRROR_FLOOR_PERCENTILE):
    ...
    floor = K * max(floor_p, floor_h)
    floor_degenerate = bool(floor <= 0.0)                      # NEW
    resolved = ((floor > 0.0)                                  # NEW guard
                & (np.abs(pattern_peccored) >= floor)
                & (np.abs(pattern_hollow) >= floor))
    ...
    return dict(..., floor_degenerate=floor_degenerate, ...)    # NEW field
```

`floor_degenerate=True` is an explicit status **distinct from RESOLVED**
(queue's own required disjunction, first branch taken) — when the floor
collapses to exactly 0.0, every bin now reads `resolved=False`, not the
current code's trivial `True` (since `abs(x) >= 0` is a mathematical
identity for any real `x`, independent of signal content).

**New file**: `experiments/111-t28-cost-gate-reposition-and-floor-fault-
injection/floor_fault_injection_control.py`. `n=48` throughout (matches
the real bin count, confirmed §2.0). All four cases zero `Sim.run()`.

| Case | Construction (exact numbers) | Tests |
|---|---|---|
| **FI-A** (asymmetric, positive/ground-truth-recovery) | `baseline=5.0e-3`; for pair index `k=0..23`, `i=k`, `j=47-k`: `arr[i]=baseline+p`, `arr[j]=baseline-p`, `p=5.0e-4` | `mirror_pooled_floor(arr) == 5.0e-4` (recovers the injected odd component exactly) |
| **FI-B** (symmetric/common-mode, negative/blindness demo) | `arr[i] = baseline + q` for **all** `i=0..47`, `q=1.0e-3` (2× FI-A's `p`, still a uniform, trivially mirror-symmetric shift) | `mirror_pooled_floor(arr) == 0.0` **despite** a common-mode perturbation twice the magnitude of FI-A's detected one — the qualitative contrast IS the control |
| **FI-C** (degenerate, `floor==0` branch) | `peccored[i] = 3.0e-3 + 1.0e-6·(i-23.5)²`; `hollow[i] = 1.5e-3 + 4.0e-7·(i-23.5)²`, `i=0..47` (both exactly symmetric under `i↔47-i` since `(i-23.5)²` is invariant) | `floor_peccored_pooled==floor_hollow_pooled==0.0` exactly. **Pre-fix** (stated as a mathematical identity, `np.abs(x)>=0` for any real `x` — not re-derived from now-superseded code): naive `resolved` would read `[True]*48`. **Post-fix** (the actual patched function, executed for real): `floor_degenerate=True`, `resolved==[False]*48` |
| **Non-regression** (real committed data) | `raw_patterns` for all 12 real `(r,margin)` cells, read directly from exp-110's own committed `results.json` (zero new FDTD) | Patched function: `floor_degenerate=False` at all 12 cells (floor confirmed strictly positive, §2.0); `n_resolved` **bit-identical** to the frozen dicts in §2.0 |

### 2.2 Item 4 — cost-gate formula recalibration + control

**File to modify**: `experiments/110-t28-item-i-local-norm-and-controls/run.py`

```python
KAPPA_COST_EXPONENT = 3.2053299988171697   # re-derived §2.0, this session
COST_GATE_SAFETY_MARGIN = 1.10             # +10%, since the exponent above is a
                                            # single-geometry/kappa_ratio empirical
                                            # fit, not a first-principles law

def cost_gate_check(pilot_empty_wall_s, pilot_total_wall_s,
                     kappa_exponent=KAPPA_COST_EXPONENT,
                     safety_margin=COST_GATE_SAFETY_MARGIN):
    pilot_pass = pilot_empty_wall_s < COST_GATE_PILOT_S
    kappa_ratio = kappa_of(312) / kappa_of(156)
    projected_312_total_s = pilot_total_wall_s * (kappa_ratio ** kappa_exponent) * safety_margin
    total_pass = projected_312_total_s < COST_GATE_TOTAL_S
    proceed = bool(pilot_pass and total_pass)
    return dict(..., kappa_exponent=kappa_exponent, safety_margin=safety_margin, ...)
```

**New file**: `experiments/111-.../cost_gate_formula_control.py`. Three
cases, all pure arithmetic (zero FDTD, zero mocking needed):

| Case | Inputs | Predicted output (exact, independently computed this session) |
|---|---|---|
| Positive (formula-arithmetic sanity) | `pilot_total_wall_s=1.0` unit | `projected = 2.0**3.2053299988171697 * 1.10 = 10.145960350566288` (assert `<1e-9` abs diff) |
| Non-regression (real exp-110 pilot data) | `pilot_empty=250.6266098022461`, `pilot_total=752.2232966423035` (exp-110's own committed r=156 figures) | `projected_312_total_s = 7632.027742505074s` (< bound `10800s`) → **still PASS** — exp-110's own already-completed r=312 leg remains licensed under the corrected, *stricter* formula (non-outcome-reversing). Contrast: this is now an **overestimate** of the real measured r=312 total (`6938.207s`), the opposite direction from the old formula's `6017.786s` **underestimate** — the fix's whole point |
| Discriminating negative control | Constructed `pilot_total_wall_s = 1349.875` | Old formula (`3.0`, no margin): `projected=10799.0s` → **PASS** (just under the `10800s` bound). New formula: `projected=13695.778228220666s` → **FAIL**. The fix changes the decision on this constructed near-boundary case |

### 2.3 Item 2 — `chunk_runner.py` upstream gate + control

**File to modify**: `experiments/110-t28-item-i-local-norm-and-controls/chunk_runner.py`

```python
def check_cost_gate_for_312():
    """R27/R28 fix (Iteration-88 Tier-1 item 2): refuses any r=312 chunk
    unless r=156's three scenes are DONE and cost_gate_check() clears.
    Uses THIS session's own log_wall_time()/total_wall_time() -- see
    §2.0's grounding-fact correction: does not assume a prior session's
    historical log files are present."""
    for which in ("empty", "hollow", "peccored"):
        _, done_path = path_for(156, which)
        if not os.path.exists(done_path):
            raise RuntimeError(f"cost gate: r=156/{which} not complete -- "
                                f"cannot evaluate cost_gate_check() before r=312.")
    pilot_empty = total_wall_time(156, "empty")
    pilot_total = sum(total_wall_time(156, w) for w in ("empty", "hollow", "peccored"))
    gate = R.cost_gate_check(pilot_empty, pilot_total)
    with open(os.path.join(SCRATCH, "r312_costgate.json"), "w") as f:
        json.dump(gate, f, indent=2)
    if not gate["proceed_to_r312"]:
        raise RuntimeError(f"R27/R28 cost gate REFUSED r=312: {gate}")
    return gate

def step_once(r, which):
    if r == 312:
        check_cost_gate_for_312()          # NEW -- genuinely upstream of build_sim/Sim.run below
    ... (existing body unchanged)
```

`analyze.py`'s own existing `cost_gate_check()` call site is **kept**, but
its comment is corrected to state plainly that it is now a **downstream,
redundant reporting/persistence step** — the enforcement point is
`chunk_runner.py`, traced end-to-end (below).

**New file**: `experiments/111-.../gate_reposition_control.py`. Monkeypatches
`chunk_runner.build_sim` with a call-counting stub that raises a sentinel
`StubReached` exception (never touches the real `Sim`/`lab` engine), and
writes synthetic `_done.pkl` marker files + synthetic `*_walltime.json`
logs into a throwaway control directory (not exp-110's own `SCRATCH`).
Zero `Sim.run()` calls anywhere in this control.

| Case | Synthetic r=156 state | Predicted `step_once(312, "empty")` behavior |
|---|---|---|
| Favorable | 3 done-markers present; logged walltimes = exp-110's own real committed figures (`empty=250.6266s`, `hollow=250.0832s`, `peccored=251.5135s`) | Raises `StubReached` (i.e. reaches `build_sim`); `build_sim` call-counter `==1`; `r312_costgate.json` written with `proceed_to_r312=True` **before** the stub is reached |
| Unfavorable (budget) | 3 done-markers present; `empty` walltime forced to `10000s` (> `COST_GATE_PILOT_S=5400s`) | Raises `RuntimeError` containing `"REFUSED"`; `build_sim` call-counter stays `0` |
| Unfavorable (precondition) | 0 done-markers (fresh r=156) | Raises `RuntimeError` containing `"not complete"`; `build_sim` call-counter stays `0` |
| Scope-precision negative control | any r=156 state at all | `step_once(156, "empty")` reaches `build_sim` **unconditionally** (call-counter `==1`) — the new guard only fires for `r==312`, proving the fix does not touch r=156's own path |

## 3. Item 3 scoping decision: DEFER (explicit reasoning, not silent)

This is the **second** deferral (Iteration 87's own queue named it once,
not attempted — the task's own framing reserves alarm for a *third*
silent one). Deferring again, explicitly, for three stated reasons:

1. **Sequencing.** Item 3 is the first genuinely new, uncertain-cost FDTD
   spend since the R27/R28 cost gate was built (exp-110). Items 2 and 4,
   *this* cycle, are exactly the fix that gate needs before it protects a
   spend like item 3's own. Running item 3 in the same cycle that repairs
   the gate's own causal position and formula defeats the point of fixing
   it first — item 3 should be the gate's first real beneficiary, not run
   alongside its own repair.
2. **Cost, predicted now regardless of the decision** (queue's own
   requirement): a `cpl`-refinement re-capture needs the same 3-scene
   (empty/hollow/peccored) × up-to-2-r geometry as exp-110's own
   re-capture — cost is per `Sim.run()` call, not per bin, so testing both
   named bins costs **up to 6 new FDTD calls**; testing r=156's `-146.25°`
   bin alone first is a genuine, cheaper, **3-call** option. Projected
   wall time (by analogy to the kappa-scaling reasoning above — a
   disclosed analogy, not a re-derived law: CPL increases per-axis grid
   density *and* time-step count, so cost is expected to scale roughly as
   `cpl_ratio**3`, the same shape §2.2 just corrected):
   | `cpl` target (from `CPL_600=20`) | ratio | r=156 (3 calls) | r=312 (3 calls) | Both r (6 calls) |
   |---|---|---|---|---|
   | 25 | 1.25× | ~1469s (~24.5 min) | ~13,550s (~226 min) | ~15,020s (~4.2h) |
   | 30 | 1.50× | ~2539s (~42 min) | ~23,417s (~390 min) | ~25,956s (~6.5h) |
   The r=312 leg dominates every option — consistent with item 4's own
   finding that r=312 is the expensive leg by a near-order-of-magnitude.
3. **Density risk.** Bundling a fourth substantial item (three governance/
   instrumentation fixes plus one genuine new-physics spot-check) risks
   repeating exactly the gap-density pattern every T28 governance cycle
   since Iteration 82 has landed under (PARTIAL, not PROMISING) — keeping
   this cycle to the zero-FDTD triad is the narrower, safer scope, matching
   how MATERIALS (Iteration 86) and ELECTROMAGNETISM (Iteration 87) each
   scoped their own governance cycles.

**Recommendation for Iteration 89**: run item 3 as its own, dedicated
Tier-1 item, `cpl=25`, r=156 alone first (~24.5 min, cheapest genuinely
informative option) — protected by *this* cycle's own repositioned,
safety-margined gate — and expand to r=312 only if r=156's own result is
decisive.

## 4. T1 escape route: N/A (verified against this cycle's own scoped changes, not copied)

Confirmed structurally against exactly what this cycle changes, not
exp-110's language: item 1 touches only a `floor>0` boolean guard and a
status field on an already-informational angular-noise-floor diagnostic
— no σ(I)/σ(x,t)/angular-selectivity/sub-threshold content is expressible
in a guard clause. Item 2 touches only checkpoint/resume orchestration
(when a chunk is permitted to run), not what any chunk computes. Item 4
touches only an exponent and a multiplicative constant in a wall-clock
projection formula. None of the three scores or moves any constraint-1/2/
3/4 verdict, and item 3 (the one item with any physical content at all)
is explicitly deferred, untouched, this cycle. **THERMODYNAMICS' own
energy sidecar is N/A this cycle for the same reason**: no new absorbed-
power/extinction data is captured by items 1/2/4 (governance on
already-existing arrays), and item 3 — the one item that would produce
new absorbed-power data — is deferred; the sidecar is owed to whichever
future cycle executes item 3, not fabricated here against nothing.

## 5. Per-item predicted outcomes — falsifiable bands (stated before any code from this proposal is written or run)

- **Item 1**: FI-A recovers `5.0e-4` exactly (`<1e-12` abs diff); FI-B
  recovers `0.0` exactly (`<1e-12`) despite a 2× larger common-mode
  input — falsified if FI-B's floor is anything but (numerically) zero.
  FI-C pre-fix: `resolved==[True]*48` (mathematical certainty, not a
  contingent measurement — falsified only if `numpy`'s own `abs(x)>=0`
  semantics differ from IEEE-754, which would itself be a distinct,
  reportable defect). FI-C post-fix: `floor_degenerate=True`,
  `resolved==[False]*48` — falsified by any `True` entry. Non-regression:
  `floor_degenerate=False` at all 12 real cells, `n_resolved` bit-identical
  to §2.0's frozen dicts — falsified by any single-bin deviation.
- **Item 2**: favorable case reaches `build_sim` (`StubReached`,
  counter`==1`); both unfavorable cases raise `RuntimeError` before
  `build_sim` is ever called (counter`==0`), with the predicted substring
  (`"REFUSED"` / `"not complete"`) present; r=156 path unaffected
  (counter`==1` unconditionally) — falsified by any call reaching
  `build_sim` in either unfavorable case, or any unfavorable case reaching
  it via `step_once(156, ...)` instead.
- **Item 4**: unit-arithmetic case `==10.145960350566288` (`<1e-9`);
  non-regression case `==7632.027742505074s`, `<10800s` (PASS, same
  direction as exp-110's own historical PASS); discriminating case: old
  formula `==10799.0s` (PASS), new formula `==13695.778228220666s` (FAIL)
  — falsified if the two formulas do not diverge on this constructed input,
  or if the non-regression case flips to FAIL.
- **Item 3**: no outcome predicted — deferred, not run.

## 6. Idealizations — what this cycle does and does not establish

- **Does establish**: `mirror_pooled_floor`/`classify_item_i_local` now
  has its own R18 fault-injection control (asymmetric recovery + symmetric
  blindness + degenerate `floor==0` handling), closing a gap open since
  exp-110's own founding cycle; the `floor==0` construction gap QUANTUM
  found now has an explicit, code-level, non-`RESOLVED` status rather than
  a silent pass-through, verified not to change any of exp-110's own
  already-scored real-data classifications. The R27/R28 cost gate is now
  genuinely, traceably upstream of every r=312 `Sim.run()` call in this
  tree, verified by a control that never touches the real FDTD engine.
  The gate's own projection formula now uses an empirically re-derived
  exponent plus an explicit safety margin, verified non-regressive against
  exp-110's own real historical pilot data and shown to change the
  decision on a constructed near-boundary case.
- **Does NOT establish**: anything about constraint 1/2/3/4, T1, or any
  physical mechanism (T1 explicitly N/A, §4). Does not establish that
  `KAPPA_COST_EXPONENT=3.2053`/`COST_GATE_SAFETY_MARGIN=1.10` generalize
  beyond exp-110's own single geometry/`kappa_ratio=2.0` data point — a
  future cycle introducing a different `kappa_ratio` (e.g. `r=624`, Tier 2
  item 5) must re-derive or re-validate this formula, not assume it
  transfers. Does not resolve whether the two PHOTONICS-named bins
  (`-146.25°` at r=156, `+168.75°` at r=312) carry real, common-mode-masked
  structure or pure discretization noise — that is exactly item 3's own
  unresolved question, deferred here with reasons stated, not answered.
  Does not re-derive `R2_SMOOTH_THRESHOLD=0.90` (Tier 2, unchanged, now a
  fourth consecutive cycle naming it undone) or MATERIALS' own
  fabrication-tolerance bound (Tier 2, now a fourth consecutive cycle).
  `chunk_runner.py`'s own upstream gate is only as good as the *current*
  live session's own wall-time logs — it cannot, and does not try to,
  reach back into a different session's ephemeral scratchpad (§2.0);
  this is a standing property of this whole re-capture idiom, not a new
  defect this cycle introduces.
