# Phase 5 Review — ELECTROMAGNETISM (Panel Iteration 88, exp-111)

**Charter** (verbatim): field/wave behavior, impedance matching, energy
coupling — owns the reciprocity/passivity/causality bookkeeping. Task this
cycle: re-verify, from primitives, my own Phase-2 critique's own mandatory
fix 1's own disposition — does `gate_reposition_control.py` genuinely bind
to the real `chunk_runner` module, or does it merely claim to; does
`check_cost_gate_for_312()` genuinely sit upstream of EVERY real r=312
`Sim.run()` call, including the fifth (already-done/stale-156) case; and
check the cost-gate recalibration for any remaining causal/physical
inconsistency Phase 2 missed.

## 0. Independent verification method

Everything below was re-derived by running Python directly against the
real committed source and `results.json` this session, or by executing
the actual committed control scripts myself and diffing against
`results.json` — never by trusting the proposal's, a critique's, or Red
Team's own prose (R4/R4-Third-Addendum discipline, applied here to my own
prior-cycle critique as well).

## 1. Mandatory fix 1 — does `gate_reposition_control.py` genuinely bind to the real `chunk_runner`?

**Yes, confirmed by direct execution, not merely by reading the identity
asserts.**

- Re-ran `gate_reposition_control.py` in place: output is bit-identical to
  `results.json["gate_reposition_control"]` across all 5 cases (favorable,
  unfavorable_budget, unfavorable_precondition, scope_precision_r156,
  already_done_312_stale_156) — `ALL CASES PASS: True`, independently
  reproduced.
- Independently introspected the imported module object (not the
  control's own claims about it): `chunk_runner.__file__ ==
  ".../experiments/110-t28-item-i-local-norm-and-controls/chunk_runner.py"`
  — the real, committed file, not a copy. `inspect.getsource(chunk_runner.
  step_once)` returns the exact committed function body, confirming the
  control's own `assert chunk_runner.step_once is ORIGINAL_STEP_ONCE`
  is checking something real, not a tautology against a reimplementation.
- Confirmed by grep across every `.py` file in the exp-110/111 tree that
  `chunk_runner.py` is the sole file constructing `Sim(...)` (line 69) or
  calling `.run(` (line 138) — `analyze.py` only reads pickles/logs via
  `CR.SCRATCH`/`CR.total_wall_time`, never calls `CR.build_sim` or
  `CR.step_once`. The "sole caller" premise the whole reposition argument
  rests on is still true, independently re-confirmed.
- The patch mechanism itself is sound, not merely asserted: `build_sim`
  inside `step_once` is a free variable resolved against the module's
  global namespace at call time, so `chunk_runner.build_sim = stub`
  genuinely redirects the real function's real call — this is not a
  reimplementation risk (EM's own Phase-2 sharpest attack, now closed).

**Verdict on mandatory fix 1: genuinely discharged.** This is not R28's
founding-instance shape recurring — the control is bound to the real
production call chain, verified by execution this session.

## 2. Does `check_cost_gate_for_312()` genuinely sit upstream of EVERY real r=312 `Sim.run()` call?

**Structurally yes — confirmed by direct source trace and, going beyond
what any of the five official control cases or Red Team's own audit
checked, by my own additional executed probe. But the shipped control
suite has a genuine, previously unflagged coverage gap on the branch that
is actually the MORE common one in real usage.**

### 2.1 The fifth case, re-verified

`case_already_done_312_stale_156`: r=312's `done_path` written, r=156
markers/logs absent. Re-ran it standalone (via the full script) and got
`build_sim_calls=0`, `exception_type=None`, `returned=True`,
`gate_evaluated=False` — bit-identical to `results.json`. This is correct:
`step_once`'s own early-return for an already-DONE scene sits (correctly,
per mandatory fix 2) **before** the `if r==312: check_cost_gate_for_312()`
line — direct read of the committed `chunk_runner.py` confirms this
ordering exactly. No new spend is possible in this state (nothing calls
`build_sim` downstream of the early return), so skipping the gate here is
correct, not a hole.

### 2.2 A gap none of the five Phase-2 critiques or Red Team's own audit tested: the checkpoint-RESUME branch

`step_once`'s real control flow, read directly:

```
if os.path.exists(done_path): return True                    # early exit
if r == 312: check_cost_gate_for_312()                        # the gate
if os.path.exists(ckpt_path):
    sim = state["sim"]            # RESUMED from pickle -- build_sim NEVER called
else:
    sim = build_sim(g, which)     # FRESH start -- the only path the control tests
sim.run(chunk)
```

All five of `gate_reposition_control.py`'s own cases call `fresh_scratch()`
and never write a `ckpt_path` — every single one exercises only the
**fresh-build** branch (`build_sim` reached, or refused before it). None
constructs the **resume** state (`ckpt_path` present, `done_path` absent),
in which `sim.run()` is reached via a deserialized pickle, never through
`build_sim` at all — so the call-counting stub the whole control is built
around is structurally blind to this branch.

This branch is not an edge case. `STEPS0=3200`, `CHUNK_STEPS=2200`,
`kappa_of(312)=312/78=4.0` ⟹ `STEPS(312)=round(3200·4.0)=12800`, needing
**6 chunks** per scene (`12800/2200→6`); `kappa_of(156)=2.0` ⟹
`STEPS(156)=6400`, 3 chunks. In the real, already-completed exp-110 r=312
capture, **5 of every 6 real `Sim.run()` calls per r=312 scene went
through the untested resume branch**, not the one branch the control
actually instruments.

I independently constructed and ran the missing case myself (not editing
the committed control — a standalone probe against the real imported
`chunk_runner` module, favorable r=156 logs, a checkpoint written for
r=312/"empty" with a stand-in sim object whose own `.run()` raises a
sentinel the moment it is reached, and a spy wrapped around the real
`check_cost_gate_for_312` to count calls):

```
[empty r=312] resumed at steps_done=2200
RESULT: sim.run() reached via RESUME branch: resumed sim.run(2200) reached
gate_called count = 1
```

The gate fires (count=1) before the sentinel `sim.run()` exception —
**the causal property genuinely holds on the resume branch too**,
confirmed by actual execution, not only by reading the `if`/`else`
structure. So the underlying claim mandatory fix 1 exists to secure is
true in full. But it was proven here, this review, for the first time —
`gate_reposition_control.py` as shipped never tests it, meaning the
control's own claim to have moved past "shown to branch somewhere" to
"traced against the real call site" is one branch short of what it
implies: it traces the *fresh-build* call site exhaustively (5 cases) and
leaves the *resume* call site — the majority of real invocations —
unverified by execution, resting on a correct but untested code-reading
argument alone. This is the identical shape R28 itself was founded to
retire (a claim resting on structural reading rather than executed
tracing), recurring one branch deeper, non-outcome-reversing only because
I checked it and it happens to hold.

**This is a real, concrete gap missed by all five Phase-2 critiques
(including my own) and by Red Team's own Phase-2 audit** — none of the
seven mandatory fixes address it, and NOTES.md's own "Does establish"
language ("genuinely, verifiably upstream of every real r=312 `Sim.run()`
call") is, on this specific point, one execution short of what it claims,
though the claim itself turns out to be correct.

## 3. Cost-gate formula recalibration — any remaining inconsistency Phase 2 missed?

Re-derived independently against `results.json`: `t156=752.2232966423035`,
`t312=6938.207038640976`, `ratio=9.223600318696624`,
`ln(ratio)/ln(2)=3.2053299988171697` — matches `KAPPA_COST_EXPONENT`
exactly, matching every Phase-2 critique's and Red Team's own
re-derivation. Re-ran `cost_gate_formula_control.py` myself: all 3 cases
reproduce `results.json` bit-exactly.

One point genuinely worth stating precisely, not raised by any Phase-2
layer: because `KAPPA_COST_EXPONENT` is *defined* as
`ln(t312/t156)/ln(kappa_ratio)` from the one historical `(t156,t312)` pair,
the formula's own "non-regression" check (`projected≈7632s` vs. real
`6938s`) is **not an independent predictive validation** — without the
`1.10` margin, the formula reproduces the real historical total to
floating-point precision *by construction*, since the exponent was solved
to make exactly that true. The genuinely informative content is entirely
in the `1.10` margin (an explicit, disclosed guess at how much a *future*,
not-yet-measured geometry might deviate from this one point's exponent),
not in the exponent's own fit to data it was derived from. NOTES.md's own
disclaimer already states the constants don't generalize beyond this one
`kappa_ratio=2.0` point — that disclaimer is correct and sufficient; I am
only making explicit *why* the non-regression check cannot be read as
independent evidence of forward accuracy, so a future reader does not
mistake "reproduces exp-110's own number" for "validated against unseen
data."

Second, smaller point: `cost_gate_check()`'s own `kappa_ratio` is
hardcoded as `kappa_of(312)/kappa_of(156)` inside the function body, not
parametrized by an `r` argument — it is a 156→312-specific function by
construction (matching `check_cost_gate_for_312()`'s own name). This is
consistent with this cycle's stated scope and already flagged as a Tier-2
item (a future `r=624` point requires re-deriving the formula), so it is
not a new gap, only a confirmation that the disclaimer's own scope-limit
language is accurate to the code, not narrower than it.

Third: the gate as built is a **static, one-shot pre-flight projection**,
re-evaluated identically on every chunk call for `r==312` (confirmed:
`total_wall_time(156, ...)` is fixed once r=156 is done, so every
re-evaluation returns the same verdict) but **never incorporates the
REAL, accumulating r=312 wall-clock spend** as chunks actually complete.
A real overrun during the r=312 run itself — the exact class of risk R27/
R28 exist to guard against — would not be caught mid-run by this
mechanism, only by the single pre-flight check before the first chunk.
This is not a defect in what item 2 was scoped to do (reposition the
existing check causally upstream, not add live monitoring — confirmed
against the Iteration-88 queue's own text), so I do not score it as an
inconsistency in this cycle's own claims. I flag it because it is a real,
physically-relevant gap in the cost/energy-bookkeeping discipline my own
seat owns, and it is a natural next step once item 2's own causal-position
fix is in place.

## 4. Everything else independently re-checked (no new defect found)

- Item 1 (`classify_item_i_local`'s `floor_degenerate` guard,
  `local_snr_*` nan-fill): re-ran `floor_fault_injection_control.py`
  myself — FI-A/B/C/non-regression all PASS exactly as `results.json`
  states; FI-D correctly, disclosedly FAILS its own "never exactly zero"
  sub-claim at phases 0°/180° (mechanism independently checked: at those
  two phases the injected perturbation collapses to a purely common-mode
  signal under `i↔47-i`, the identical FI-B mechanism) — matches NOTES.md's
  own disclosed correction exactly.
- `local_snr_peccored`/`local_snr_hollow` are `nan`-filled, not `inf`, when
  `floor<=0` — read directly from `run.py`'s committed
  `classify_item_i_local`; QUANTUM's Phase-2 gap is genuinely closed.
- All 12 real `(r,margin)` cells: `floor_degenerate=False`, `n_resolved`
  bit-identical to exp-110's own frozen dicts — reproduces exactly.
- Guard-ordering fix (mandatory fix 2): direct read of committed
  `step_once` confirms `check_cost_gate_for_312()` sits **after** the
  done-file early-return and **before** both the resume and fresh-build
  branches — matches NOTES.md's own claimed ordering exactly (this is the
  fix that makes §2's resume-branch result come out correctly once
  someone checks it, which I now have).
- MATERIALS' §3 cost-table arithmetic-slip fix (mandatory fix 4):
  `cpl_cost_table.py`'s committed output matches `results.json`'s own
  regenerated `4.17h`/`7.21h` figures; the original hand-typed "~6.5h" is
  correctly retired from the frozen Result text.
- R23 extension (mandatory fix 5): `predictions_text`/`result_text` in
  `results.json` both contain the three new Iteration-88 caveats verbatim;
  `DISCLAIMER_88` does not mutate exp-110's own frozen `DISCLAIMER` (R4
  discipline preserved for that cycle's own citation).
- `n_fdtd_calls=0`, `lab_diff=False` in `results.json` — this cycle's own
  "zero new FDTD, zero `lab/` diff" claim holds exactly.

No arithmetic, citation, or T1-applicability defect survived independent
re-derivation anywhere in this cycle's own claims.

## Verdict: **CONFIRM-WITH-GAPS**

Not RULED OUT (T1 correctly N/A throughout, re-confirmed structurally);
not a clean CONFIRM (a real, concrete, previously-unflagged coverage gap
in the very control this cycle built to prove mandatory fix 1, found only
by executing a case none of the seven mandatory fixes or six prior review
layers — five Phase-2 critiques plus Red Team's own audit — thought to
construct). The substantive claims this cycle rests on are, however, all
independently reproduced and, on the one point I could newly test, shown
to hold under actual execution rather than only under code-reading. Zero
Checkpoint criteria fire from anything in this review: nothing here is
unfalsifiable, inexpressible, or a constraint violation, and the resume-
branch gap is a verification-coverage shortfall on a claim that turns out
to be true, not a discovered defect that reverses any outcome — matching
this sub-thread's own repeated non-firing precedent for a first-found gap
of a genuinely new shape (R13/R14/R15/R26 lineage).

## Ranked top-3 candidate directions for Iteration 89

1. **Close the resume-branch coverage gap in `gate_reposition_control.py`
   (or a same-shift sibling), zero new FDTD.** Add a sixth case:
   checkpoint present (not done) for r=312, patch the resumed sim's own
   `.run()` (or `Sim.run` generically) rather than `build_sim`, and assert
   the gate fires before it — exactly the probe this review used. Cheap,
   concrete, and the branch that actually dominates real usage
   (5-of-6 chunks per r=312 scene in exp-110's own historical run).
2. **Execute Item 3** (PHOTONICS' own cpl-refinement floor spot-check at
   the two named bins, −146.25°/r=156 first, `cpl=25`) — the Reconciled
   Iteration-89 queue's own Tier-1 item 1, now genuinely protected by a
   cost gate whose causal position and formula are both independently
   re-verified this review, and the only instrument that can settle
   whether those two bins carry real common-mode-masked structure.
3. **Upgrade the cost gate from a static pre-flight projection to a
   running check against actual accumulating r=312 wall-clock spend**
   (§3, above) — a genuine energy/cost-bookkeeping improvement in this
   seat's own charter, distinct from and complementary to R27/R28's
   already-closed "causal position" concern; would also let a future
   `r=624` point (Tier-2 item 5) be introduced with a live safety net
   rather than only a re-derived static exponent.
