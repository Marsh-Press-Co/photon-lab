# exp-111 — Panel Iteration 88

**Lead seat: THERMODYNAMICS (rotation lead).** Governance/instrumentation
cycle continuing the T28 sub-thread. Executes Reconciled Iteration-88
Tier-1 items 1, 2, 4 (all zero new FDTD, per the queue's own text);
item 3 (PHOTONICS' cpl-refinement floor spot-check) explicitly deferred a
second time, reasoned. Tier-0 item 0 (ruling on the Iteration-85
Checkpoint-4/R24 firing) is Marsh's call, out of scope, not attempted.

Full record: `phase1_proposal.md` (THERMODYNAMICS), `phase2_critique_
photonics.md`, `phase2_critique_materials.md`, `phase2_critique_em.md`,
`phase2_critique_quantum.md`, `phase2_critique_vision.md` (five blind
Phase-2 critiques), `phase2_redteam_audit.md` (Red Team's Phase-2 audit).

## Phase 3 — Synthesis (Director)

Verdict inherited from Red Team's own Phase-2 audit: **PROCEED-WITH-
MANDATORY-FIXES**, 7 mandatory fixes, all tagged `[inconsistency]`, zero
`unfalsifiable`/`inexpressible`/`constraint-#N-violation` tags. Zero
Checkpoint criteria implicated (checked directly against PANEL.md's own
five-item list, `phase2_redteam_audit.md` Sec 7).

**Disposition — all 7 mandatory fixes ADOPTED IN FULL by the Director,
zero further overrides on top of Red Team's own two disclosed partial
overrides (PHOTONICS' urgency/framing; VISION's escalation-framing —
both already resolved by Red Team itself, substance adopted either way,
see `phase2_redteam_audit.md` Sec 3):**

| # | Fix (Red Team's own numbering, `phase2_redteam_audit.md` Sec 5) | Implemented as |
|---|---|---|
| 1 | Bind `gate_reposition_control.py`'s "genuinely upstream" claim to the REAL `chunk_runner` module, not a reimplementation | `gate_reposition_control.py` imports the real `chunk_runner` module, patches its actual `build_sim` attribute, calls its actual unmodified `step_once()`; two explicit identity assertions (`chunk_runner.build_sim is stub`, `chunk_runner.step_once is ORIGINAL_STEP_ONCE`) run before every case is trusted |
| 2 | A fifth control case: r=312 already done, r=156 logs absent/stale | `gate_reposition_control.py::case_already_done_312_stale_156()` — predicts zero gate evaluation, zero `build_sim` calls; `chunk_runner.py`'s own guard is placed AFTER the existing done-file early-return (not before, as originally drafted) so this state is handled correctly by construction |
| 3 | Extend the `floor>0.0` guard to `local_snr_peccored`/`local_snr_hollow` (nan, not inf) + FI-C assertion | `run.py::classify_item_i_local()` patched (both fields now `nan`-filled when `floor<=0`); `floor_fault_injection_control.py::fi_c()` asserts `no_inf_snr` |
| 4 | Correct §3's cost-projection table (cpl=30 "Both r" is 7.21h, not 6.5h); regenerate via script, not hand-typing | `cpl_cost_table.py` (new, this cycle) — see Result, below, for its actual output |
| 5 | Extend `DISCLAIMER` (or its Iteration-88 successor string) with the three new scope caveats; wire predictions/result text; re-fire `assert DISCLAIMER in ...` | `predictions_result_88.py` — new `DISCLAIMER_88 = R.DISCLAIMER + NEW_CAVEATS_88` (does NOT mutate exp-110's own frozen `DISCLAIMER`, avoiding an R4-shaped regression against that cycle's own already-quoted verbatim text); `build_predictions_text_88()`/`build_result_text_88()`, both assert `DISCLAIMER_88 in ...` |
| 6 | Narrow the "closes the last open R18 gap" claim; strongly recommended (not required) to add PHOTONICS' own FI-D case | **Both**: FI-D (a swept-phase quasi-periodic perturbation at `P*=2.8421°`) added to `floor_fault_injection_control.py` since it costs zero new FDTD; the claim itself is narrowed below (Idealizations) regardless of FI-D's own outcome, per Red Team's own minimum bar |
| 7 | Carry item 3's deferral forward as its own explicit, numbered Reconciled-Iteration-89 Tier-1 line (R25 discipline) | Done — see Reconciled Iteration-89 queue, below (written now, preventatively, per Red Team's own instruction) |

## T1 escape route: N/A

Confirmed structurally against exactly what this cycle changes (not
copied from a prior cycle's language): item 1 touches only a
`floor>0.0` boolean guard, a new `floor_degenerate` status field, and a
`nan`-vs-`inf` fill choice on an already-informational angular-noise-floor
diagnostic. Item 2 touches only checkpoint/resume orchestration (WHEN a
chunk is permitted to run), not what any chunk computes. Item 4 touches
only an exponent and a multiplicative constant in a wall-clock projection
formula. None of the three scores or moves any constraint-1/2/3/4
verdict, and item 3 (the one item with any physical content at all) is
untouched this cycle. THERMODYNAMICS' own energy sidecar is N/A for the
identical reason: no new absorbed-power/extinction data is captured by
items 1/2/4 (governance on already-existing arrays/orchestration/a
formula constant), and item 3 — the one item that would produce new
absorbed-power data — is deferred.

## Setup

- `experiments/110-t28-item-i-local-norm-and-controls/run.py` (edited in
  place, matching this sub-thread's own precedent of patching a prior
  cycle's committed classifier code — e.g. exp-108's own
  `classify_shape_ratio_fixedabs` extraction into exp-106's own `run.py`,
  Iteration 85; exp-109's own `classify_item_ii` patch into exp-108's own
  `run.py`, Iteration 86): `classify_item_i_local()` (mandatory fixes 3);
  `cost_gate_check()` (mandatory-fix-4-adjacent — the recalibrated
  formula, `KAPPA_COST_EXPONENT`/`COST_GATE_SAFETY_MARGIN`). `DISCLAIMER`
  itself and `build_predictions_text()`/`build_result_text()` are **left
  unmodified** — exp-110's own frozen historical Predictions/Result text
  must remain independently re-reproducible from that cycle's own
  committed `run.py` (R4 discipline); this cycle's own new text lives in
  `predictions_result_88.py` instead (mandatory fix 5).
- `experiments/110-t28-item-i-local-norm-and-controls/chunk_runner.py`
  (edited in place): new `check_cost_gate_for_312()`, called from
  `step_once()` for `r==312` **after** the existing already-DONE
  early-return (mandatory fix 2's own ordering requirement).
- `experiments/110-t28-item-i-local-norm-and-controls/analyze.py` (edited
  in place): its own existing `cost_gate_check()` call site is kept but
  its comment corrected to state it is now a downstream, redundant
  reporting/persistence step, not the enforcement point.
- `experiments/111-.../floor_fault_injection_control.py` (new): FI-A/B/C/D
  + non-regression, all zero `Sim.run()` calls.
- `experiments/111-.../cost_gate_formula_control.py` (new): 3 formula
  cases, pure arithmetic.
- `experiments/111-.../gate_reposition_control.py` (new): 5 cases, bound
  to the real `chunk_runner` module (mandatory fix 1), zero `Sim.run()`
  calls, throwaway control scratch directory.
- `experiments/111-.../cpl_cost_table.py` (new): regenerates the item-3
  deferral cost table from exp-110's own real committed wall times
  (mandatory fix 4), correcting MATERIALS' own found arithmetic slip.
- `experiments/111-.../predictions_result_88.py` (new): `DISCLAIMER_88`,
  `build_predictions_text_88()`, `build_result_text_88()` (mandatory
  fix 5, R23).
- Zero `lab/` diff this cycle — trust suite unaffected, re-confirmed green
  before Phase 4 below as standing discipline.

## Predictions (committed to git BEFORE any Phase-4 code is executed for
## real, house discipline, non-negotiable — verbatim quote of
## `predictions_result_88.py::build_predictions_text_88()`'s own output)

PREDICTIONS (pre-registered, exp-111, Panel Iteration 88)

Raw physical angular-scattering-pattern and absorbed-power/ extinction ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility. angular_scattered_pattern() is a square-path near-to-mid-field angular sample, not a true circular far-field pattern (function's own docstring). The absolute-floor six-margin family and item 1's own mirror-symmetry floor are both new conventions this cycle, not independently re-derived from a resolution or aliasing bound. Item 1's mirror floor characterizes grid-discretization/floating-point noise for the IDEALIZED simulated geometry ONLY -- a bin clearing it licenses NO inference about a physically realized coated disk's own achievable angular-pattern symmetry (real deposition/machining tolerances sit orders of magnitude above this floor's ~1e-9-1e-4 scale). Item 1's mirror floor is structurally BLIND to common-mode/even noise (a bias, not variance -- any bias identical at bin i and its mirror bin cancels exactly in the differencing construction, at any sample size, unclosed by pooling) -- a RESOLVED bin under this gate is cleared only against the ODD/antisymmetric noise component, not validated clean of common-mode contamination. Item 1's diagnostic is INFORMATIONAL ONLY and does not replace, gate, or reclassify item i's own existing frozen CONFIRM verdict. Panel Iteration 88 (exp-111) adds three new caveats to the above, carried forward as part of this same single-source-of-truth string (R23): (1) `floor_degenerate` is a new status field, distinct from `resolved`/RESOLVED -- it marks the genuinely degenerate case where the pooled floor itself collapses to exactly 0.0 (both parent patterns exactly mirror-symmetric); a bin with `floor_degenerate=True` is UNRESOLVED-BY-CONSTRUCTION, not silently RESOLVED, and its `local_snr_peccored`/`local_snr_hollow` fields are `nan`, not `inf`. (2) `KAPPA_COST_EXPONENT=3.2053299988171697` and `COST_GATE_SAFETY_MARGIN=1.10` are an empirical re-derivation from a SINGLE geometry/kappa_ratio=2.0 data point (exp-110's own r=156/r=312 combined wall times) -- this does NOT establish that either constant generalizes to a different kappa_ratio (e.g. a future r=624 point); a future cycle introducing one must re-derive or re-validate this formula, not assume it transfers. (3) The R27/R28 cost gate's own enforcement point is repositioned this cycle from `analyze.py` (downstream, reporting-only as of this cycle) to `chunk_runner.py` (genuinely upstream of every real r=312 `Sim.run()` call) -- verified by a control bound to the real, imported `chunk_runner` module, never a hand-copied reimplementation.

**Item 1** (fault-injection control, `mirror_pooled_floor`/
`classify_item_i_local`): FI-A recovers `5.0e-4` exactly (`<1e-12` abs
diff). FI-B recovers `0.0` exactly (`<1e-12`) despite a 2x larger
common-mode input. FI-C (degenerate): `floor_peccored_pooled==
floor_hollow_pooled==0.0` exactly; post-fix, `floor_degenerate=True`,
`resolved==[False]*48`, and (closing QUANTUM's own Phase-2 finding)
neither `local_snr_peccored` nor `local_snr_hollow` is `inf` anywhere.
FI-D (PHOTONICS' own recommended addition, informational): the pooled
floor's recovered magnitude is NOT constant across a 24-point phase sweep
of a `P*=2.8421deg`-period synthetic perturbation (spread > 1% of the
injected amplitude), and no swept phase drives the floor to exactly 0.0
or exactly the full injected amplitude. Non-regression: the patched
function, re-run against all 12 real (r, margin) cells already committed
in exp-110's own `results.json`, reports `floor_degenerate=False`
everywhere and `n_resolved` bit-identical to the frozen dicts. Falsified
by any single deviation from the above.

**Item 2** (cost-gate reposition control, bound to the real `chunk_runner`
module): favorable case reaches `build_sim` (raises `StubReached`, call
counter `==1`), with `r312_costgate.json` written showing
`proceed_to_r312=True` BEFORE the stub is reached. Both unfavorable cases
(budget-exceeded; r=156 precondition incomplete) raise `RuntimeError`
before `build_sim` is ever called (counter `==0`), with the predicted
substring (`"REFUSED"` / `"not complete"`) present. The r=156 scope-
precision case reaches `build_sim` unconditionally (counter `==1`) --
the guard fires only for `r==312`. The fifth case (r=312 already DONE,
r=156 logs absent/stale) returns `True` immediately, WITHOUT evaluating
the cost gate at all (`r312_costgate.json` not written this call,
`build_sim` counter `==0`) -- the fixed guard ordering (done-check before
gate-check) never re-evaluates the gate on an idempotent status check.
Falsified by any call reaching `build_sim` in an unfavorable case, any
unfavorable case reaching it via `step_once(156, ...)` instead, or the
fifth case ever writing/evaluating the gate.

**Item 4** (cost-gate formula recalibration control): unit-arithmetic case
`==10.145960350566288` (`<1e-9`); non-regression case (exp-110's own real
r=156 pilot data) `==7632.027742505074s`, `<10800s` (PASS, an OVERestimate
of the real measured r=312 total `6938.207038640976s` -- the opposite
direction from the old formula's own `6017.786...s` UNDERestimate, the
fix's whole point); discriminating case: old formula (exponent 3.0, no
margin) `==10799.0s` (PASS), new formula `==13695.778220666s` (FAIL) --
the two formulas diverge in their pass/fail decision on this constructed
near-boundary input. Falsified if the non-regression case flips to FAIL,
or if the two formulas do not diverge on the discriminating case.

**Item 3**: no outcome predicted -- deferred, not run this cycle (see
NOTES.md Setup/Idealizations for the reasoned scoping decision and the
regenerated `cpl_cost_table.py` output, correcting Sec 3's own
hand-typed-table arithmetic slip MATERIALS' Phase-2 critique caught --
mandatory fix 4).

**T1**: N/A. Confirmed structurally: item 1 touches only a `floor>0.0`
boolean guard, a new status field, and a `nan`-vs-`inf` fill choice on an
already-informational angular-noise-floor diagnostic; item 2 touches only
checkpoint/resume orchestration (WHEN a chunk is permitted to run), not
what any chunk computes; item 4 touches only an exponent and a
multiplicative constant in a wall-clock projection formula. None of the
three scores or moves any constraint-1/2/3/4 verdict. Item 3, the one
item with any physical content, is untouched this cycle.

## Result (after Phase 4 — verbatim quote of
## `predictions_result_88.py::build_result_text_88()`'s own output, fed
## the real captured control outputs, persisted in `results.json`)

RESULT (exp-111, Panel Iteration 88)

{DISCLAIMER_88 — identical to the Predictions block above, omitted here for brevity; verbatim in `results.json["result_text"]`}

Zero new FDTD calls this cycle (items 1/2/4 are synthetic/orchestration/
formula-only, item 3 deferred), zero `lab/` diff.
(zero new FDTD this cycle; all figures from exp-110's own already-committed results.json plus this cycle's own synthetic/formula controls)

**Item 1 (fault-injection control):** FI-A PASS (recovered `5.000000e-04`,
predicted `5.000000e-04`). FI-B PASS (recovered `0.000000e+00` despite
`1.0e-03` injected common-mode magnitude). FI-C PASS (`floor_degenerate`=
`True`, `resolved` all False=`True`, no `inf` in `local_snr`=`True`). **FI-D
(informational) FAIL** on its own "never exactly zero" sub-claim (floor
range `0.000e+00`–`3.534e-04`, spread `3.534e-04` = 70.7% of injected
amplitude — genuinely phase-dependent, as predicted; but at 2 of the 24
swept phases (0°, 180°) the pooled floor reads *exactly* `0.0`, not merely
small). Non-regression: all 12 real cells match=`True`.

**Item 2 (gate reposition control, bound to the real `chunk_runner`
module):** 5/5 cases PASS. Favorable reaches `build_sim` (calls=1), gate
written before the stub with `proceed_to_r312`=`True`. Both budget/
precondition-unfavorable cases refuse before `build_sim` (calls=0). r=156
scope-precision case reaches `build_sim` unconditionally (calls=1). The
already-done/stale-156 case (mandatory-fix 2) returns `True` with zero
gate evaluation and zero `build_sim` calls, as predicted.

**Item 4 (cost-gate formula recalibration control):** 3/3 cases PASS.
Non-regression projects `7632.028s` (overestimates the real measured
r=312 total by `693.8s`; the OLD formula underestimated it by `920.4s`).
Discriminating case: old formula `10799.0s` (PASS) vs new formula
`13695.8s` (FAIL) — the two formulas diverge as predicted.

**Item 3 (deferred, not run):** regenerated cost table (`cpl_cost_table.py`,
correcting MATERIALS' own found arithmetic slip): cpl=25: `4.17h`, cpl=30:
`7.21h` (was hand-typed as "~6.5h" in `phase1_proposal.md` — that figure
was the r=312-alone column's own value, misplaced; corrected here per
mandatory fix 4). Recommendation for Iteration 89 unchanged: `cpl=25`,
r=156-alone-first.

### Interpretation — FI-D's own falsified sub-claim (disclosed, not hidden)

FI-D's predicted band (`non_constant AND never_exactly_zero AND
never_exactly_full`) was **falsified on one of its three conjuncts**:
`never_exactly_zero` is false — the pooled floor reads exactly `0.0` at
swept phases 0° and 180° (out of 24). The mechanism, verified directly by
re-running the construction: `BIN_CENTERS_DEG[i] == -BIN_CENTERS_DEG[47-i]`
by this instrument's own convention (confirmed against `analyze.py`'s own
bin-center construction and the two PHOTONICS-named bins' own mirror
partners), so `cos(2·pi·BIN_CENTERS_DEG/P* + 0)` is an EVEN function of
the bin index under `i<->47-i` at phase=0/180° specifically (`cos` is even
in its argument, and the argument itself is odd in `i<->47-i` at those two
phases only) — collapsing FI-D's own swept perturbation to a purely
common-mode/even signal at exactly those two points, i.e. **the identical
mechanism FI-B already demonstrates**, not a new pathology. This is a
genuine Director-level prediction error (the "never exactly zero" clause
was written without checking phase=0/180° specifically), disclosed here
rather than silently reworded post-hoc (R4 discipline applied to the
Director's own Phase-3 text, not only to seats' claims). **Non-blocking**:
FI-D is explicitly informational (mandatory fixes 3/6 do not depend on
FI-D's own predicted band; R18's own literal text is satisfied by FI-A/B
alone, per Red Team's own Phase-2 ruling); the qualitative point FI-D
exists to demonstrate — that a realistic, neither-clean-odd-nor-clean-even
periodic perturbation produces a floor reading that depends on where in
its cycle it sits, spanning the full range from FI-B's exact blindness
(at the two symmetric phases) up to 70.7% of the injected amplitude
recovered (near phase=90°/270°, the maximally antisymmetric alignment) —
still stands, and is if anything sharpened by finding the exact
blind-spot phases rather than merely a nonzero minimum.

## Combined Verdict (Director, pending Phase 5)

**PARTIAL** (LOGBOOK-level vocabulary) — not RULED OUT (T1 correctly N/A
throughout); not a clean, unqualified PASS, since FI-D's own predicted
band was falsified on one conjunct (disclosed above, non-blocking, with a
verified mechanism). All mandatory-fix-gating items (1's FI-A/B/C +
non-regression, 2's all 5 cases, 4's all 3 cases) PASS exactly as
predicted; zero new FDTD; zero `lab/` diff; trust suite green throughout
(41/41, before and after this cycle's code patches). Six blind Phase-5
reviews plus Red Team's own final audit, below, will independently
re-verify all of the above and may revise this label.

## Reconciled Iteration-89 queue (written now, per R25 discipline —
## mandatory fix 7 — not a parenthetical)

**Tier 0** — rule on the Iteration-85 Checkpoint-4/R24 firing at the next
convened checkpoint (unchanged, still Marsh's call, still pending).

**Tier 1** — (1) Execute item 3 (PHOTONICS' own independent, non-
differencing floor check, a `cpl`-refinement spot check) at the two named
bins (−146.25° at r=156, +168.75° at r=312), protected by this cycle's own
repositioned, safety-margined, real-module-verified cost gate — this
proposal's own recommendation: start with `cpl=25`, r=156-alone-first
(~24.5 min, cheapest genuinely informative option per the regenerated
`cpl_cost_table.py`), expand to r=312 only if r=156's own result is
decisive; genuine new FDTD, correctly deferred twice now, should not be
deferred a third time without new, equally explicit reasoning. (2) The
long-outstanding `R2_SMOOTH_THRESHOLD=0.90` re-derivation (queued since
Iteration 86 Tier 2b, now a fifth consecutive cycle naming it undone).
(3) MATERIALS' own fabrication-tolerance quantitative bound (now a fourth
consecutive cycle naming it undone).

**Tier 2** — a full per-margin item-1c/1d Result-section table (still
outstanding, Iteration-87 Tier 2 item 3); `CLOSURE_CONFIRM`/
`CLOSURE_FALSIFY` dead-code cleanup (Iteration-87 Tier 2 item 4); a fourth
r-point (r=624) — note this would require re-deriving or re-validating
`KAPPA_COST_EXPONENT`/`COST_GATE_SAFETY_MARGIN` at a new `kappa_ratio`
(this cycle's own Idealizations, above), not assuming they transfer.

**Tier 3 — unchanged standing items**: the oblique-angle extension; the
750/450nm leg; the `G40` full-width leg; the x-wall admittance refit;
`PAD`-with-article survival; `box_dev`'s own thinning margin (~9.0× at
r=312, still unresolved).

## Idealizations — what this cycle does and does not establish

- **Does establish**: `mirror_pooled_floor`/`classify_item_i_local` now
  has a genuinely bound (mandatory fix 1), correctly-ordered (mandatory
  fix 2) fault-injection control covering the two mathematical corner
  cases (pure odd/asymmetric, pure even/symmetric-or-degenerate) plus one
  realistic aliased/phase-swept case (FI-D) that sharpens rather than
  merely narrows the claim — the "closes the last open R18 gap" language
  is correctly narrowed (mandatory fix 6) to: R18's own literal positive/
  negative-control requirement is satisfied in full; the realistic
  aliased/intermediate regime is now *characterized* (phase-dependent,
  spanning 0%–70.7% of injected amplitude recovered), not merely flagged
  as untested. The `floor==0` degenerate construction gap (QUANTUM,
  Iteration 87) is closed with no live self-contradiction remaining
  (mandatory fix 3). The R27/R28 cost gate is now genuinely, verifiably
  upstream of every real r=312 `Sim.run()` call, bound to the real
  production module (mandatory fixes 1/2) — not merely shown to branch
  somewhere, the exact gap R28 exists to close. The gate's own projection
  formula now uses an empirically re-derived exponent plus an explicit
  safety margin, verified non-regressive against exp-110's own real
  historical pilot data and shown to change the decision on a constructed
  near-boundary case.
- **Does NOT establish**: anything about constraint 1/2/3/4, T1, or any
  physical mechanism (T1 explicitly N/A). Does not establish that
  `KAPPA_COST_EXPONENT=3.2053`/`COST_GATE_SAFETY_MARGIN=1.10` generalize
  beyond exp-110's own single geometry/`kappa_ratio=2.0` data point — a
  future cycle introducing a different `kappa_ratio` (e.g. r=624) must
  re-derive or re-validate this formula, not assume it transfers. Does not
  resolve whether the two PHOTONICS-named bins carry real, common-mode-
  masked structure or pure discretization noise — item 3's own unresolved
  question, deferred here a second time with reasons stated (sequencing,
  predicted cost, density risk — `phase1_proposal.md` Sec 3), not
  answered. Does not re-derive `R2_SMOOTH_THRESHOLD=0.90` or MATERIALS' own
  fabrication-tolerance bound (both Tier 1/2, unchanged, now undone a
  fourth/fifth consecutive cycle respectively). `chunk_runner.py`'s own
  upstream gate is only as good as the *current* live session's own
  wall-time logs — it cannot, and does not try to, reach back into a
  different session's ephemeral scratchpad (a standing property of this
  whole re-capture idiom, unchanged from exp-110's own disclosure).
