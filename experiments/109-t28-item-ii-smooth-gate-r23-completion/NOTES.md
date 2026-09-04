# exp-109 — The R24 Second-Instance Smooth Gate, and R23's Missing `RESULT_TEXT` Half

Panel Iteration 86. Lead seat: MATERIALS & METAMATERIALS (rotation lead).
Governance/instrumentation cycle — zero new FDTD, no mechanism proposed,
no constraint-1/2/3/4 verdict touched. Executes the four Tier-0
UNBLOCKED items from the Reconciled Iteration-86 queue (LOGBOOK.md
Iteration 85 CHECKPOINT block / `experiments/108-.../phase5_redteam_audit.md`
§9): gate `classify_item_ii()` on `fit["smooth"]` (the R24 second-instance
fix itself); wire `build_result_text()` into an executed path; restore
both founding `assert DISCLAIMER` calls; persist `predictions_text`/
`result_text` into a new, exp-109-own `results.json`. **Tier-0 item 0 —
ruling on the Iteration-85 Checkpoint-4 firing itself — is Marsh's call,
not a Panel proposal's, and is explicitly out of scope for this document.**

## Hypothesis

`classify_item_ii()` (`experiments/108-.../run.py`) currently reports a
detrended `residual_std` as "the genuine floor" unconditionally, even
though the identical `fit["smooth"]` diagnostic correctly gates its
sibling `classify_item_i()`'s own REFUTE branch. This is the second
instance of R24 (a Phase-2 mandatory fix's own if/then consequence,
Phase-3-claimed "adopted in full," never wired into the classification
logic it was written to gate) — it fired CHECKPOINT CRITERION 4 at
Iteration 85's own Phase-5 final audit. Gating the statistic on
`fit["smooth"]`, falling back to the raw (undetrended) `np.std` when the
fit is not smooth, closes the second instance for real (wired into the
executed path, not merely re-disclosed a third time) without reversing
either of exp-108's own already-CONFIRMed outcomes.

## Phase 1 → Phase 2 → Phase 3: synthesis of the debate

Phase 1 (MATERIALS, `phase1_proposal.md`): proposed exactly the four
Tier-0 items above, with `classify_item_ii()`'s new body given verbatim,
predicted outcomes computed from already-committed primitives (not
deferred to Phase 4), and an explicit three-way comparison of candidate
non-smooth-branch substitutes (raw std / forced AMBIGUOUS / undocumented
gate), picking raw std and rejecting the other two with reasons.

Phase 2: five blind critiques, ALL support-with-changes, ZERO opposition,
ZERO outcome-reversing findings — PHOTONICS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE. Red Team's own audit
(`phase2_redteam_audit.md`) independently re-derived every load-bearing
number from primitives (the OLS inequality; `classify_item_i()`'s actual
code path; `results.json`'s `n_fdtd_calls`/`total_wall_s`/`fit`/
`delta_values` fields; exp-108's own Phase-5 VISION §2d citation) before
adopting five of five critiques' findings, with one explicit, narrow
override (declining to extend QUANTUM's critique into a mandatory
re-derivation of the shared `R2_SMOOTH_THRESHOLD=0.90` this cycle —
non-outcome-reversing, out of this cycle's own disclosed scope, already
correctly queued as Tier 2 item 3). Verdict: **PROCEED-WITH-MANDATORY-FIXES**,
six mandatory fixes, one non-blocking recommended fix. Director (this
document) adopts Red Team's Phase-2 audit in full — no further overrides.

**The six mandatory fixes, and how each is incorporated below:**

1. **[PHOTONICS + Red Team]** The proposal's own rejection of the
   forced-AMBIGUOUS alternative leaned on a misdescribed sibling-code
   analogy (`classify_item_i()`'s CONFIRM branch is not "deliberately
   unconditional on smoothness" — traced to source, it never reaches the
   `linear_fit_1_over_margin`/smoothness-test code path at all, since
   CONFIRM requires `not runs` and the fit is only called inside
   `for (i0,j0) in runs:`). Corrected below (§ "Why raw std, not forced
   AMBIGUOUS") to rest on the OLS-inequality proof plus a stronger ground
   Red Team found independently: the *original* Iteration-85 mandatory
   fix's own text (`experiments/108-.../phase2_redteam_audit.md:340-347`)
   already specifies raw `std` as the pre-registered non-smooth default —
   the fix's own words, not an analogy to a different function.
2. **[ELECTROMAGNETISM]** "Raw std is more conservative in every case" is
   corrected to a two-sided statement: conservative against a false
   CONFIRM (inflating the stat cannot make the reported floor read
   smaller than the trusted detrended value), simultaneously liberal/
   anti-conservative against a false REFUTE (inflating the stat only ever
   makes `stat >= boxA` easier to satisfy). Not outcome-reversing at
   either tested r (both land deep inside CONFIRM) but the universal
   framing was wrong and matters at Tier 2's own queued r=624 point.
   Corrected in both this document's own prose and the generated
   `stat_source` string itself (the artifact a future citation will
   actually quote).
3. **[QUANTUM OPTICS]** The raw/residual ratio (1.729× at r=156, 1.010×
   at r=312, both independently re-derived exact by Red Team) is now
   persisted in `classify_item_ii()`'s own return dict
   (`raw_over_residual_ratio`) and narrated in `stat_source`, so a future
   reader sees the fallback is discarding a materially different amount
   of demonstrated trend at each point rather than treating both
   non-smooth cases as equivalent.
4. **[THERMODYNAMICS]** `gate_p0_pass`/`repro_pass`'s own reduction rule
   (four per-r booleans → two scalars) is stated explicitly, in code and
   docstring, as the logical AND of both r's `pass_` fields — not left
   for a reader to infer.
5. **[THERMODYNAMICS]** `build_result_text()` gains an explicit,
   optional `wall_time_source` argument, threaded through this cycle as
   an attribution note disclosing that the `n_fdtd_calls=6`/
   `total_wall_s=7712.0` figures are exp-108's own historical spend,
   reused verbatim — zero new FDTD calls this cycle — so a verbatim
   citation of `result_text` cannot misread that spend as exp-109's own.
6. **[VISION SCIENCE]** Binding requirement, below and in this document's
   own Result section once Phase 4 completes: NOTES.md's Result section
   quotes `results.json['result_text']` and `['predictions_text']`
   **verbatim, in full** — not a paraphrase — closing the "human-readable-
   citation" half of R23 that exp-108's own Phase-5 VISION review (§2d)
   found still open after the code/persistence half was already fixed.

**Non-blocking recommendation adopted** (Attack 6, Red Team): the
`analyze.py` line-85 companion call site is shown as an exact diff below
(§ Setup), not left as prose-only, extending the R18 disclosure to name
both `classify_item_ii()`'s new branch and this call site.

## Setup

All four items touch only already-committed data
(`experiments/108-t28-reclassification-angular-pattern-batch/results.json`)
and code in exp-108's own directory (patched in place — exp-108 itself
set this precedent patching exp-106's own `run.py` directly), plus one
new script and one new `results.json` in exp-109's own directory.
**Zero new `Sim.run()` calls anywhere; zero `lab/` diff.**

### `classify_item_ii()`'s exact new body (`experiments/108-.../run.py`)

```python
def classify_item_ii(r, fit, delta_values):
    """R24 second-instance fix (Panel Iteration 86, exp-109): gate the
    reported floor statistic on fit["smooth"], mirroring classify_item_i's
    own smoothness-gated fit machinery. When the 6-margin sequence is
    smooth, use the detrended residual_std (exp-108's own original logic,
    unchanged). When it is not smooth, fall back to the raw, undetrended
    np.std(delta_values) -- the original Iteration-85 mandatory fix's own
    text already specifies this as the non-smooth default (a stronger
    ground than the OLS-inequality proof alone, itself independently
    airtight: for any OLS fit with an intercept, residual_std <= raw_std
    always, since the constant model is a feasible fit point -- 'residual
    std' can never exceed 'raw std'). NOTE this inequality is one-sided:
    the raw-std fallback is conservative against manufacturing a false
    CONFIRM (it cannot make the reported floor read smaller than the
    trusted detrended estimate) but simultaneously liberal/anti-
    conservative against a false REFUTE (inflating the statistic only
    ever makes stat>=boxA easier to satisfy) -- NOT 'more conservative in
    every case.'"""
    boxA = DELTA_BOXA[r]
    raw_std = float(np.std(delta_values))
    ratio = raw_std / fit["residual_std"] if fit["residual_std"] else float("inf")
    if fit["smooth"]:
        stat = fit["residual_std"]
        stat_source = (f"detrended (fit smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f})")
    else:
        stat = raw_std
        stat_source = (f"raw/undetrended (fit NOT smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f} < {R2_SMOOTH_THRESHOLD:.2f} -- "
                        f"residual_std is not trusted as 'the genuine floor'; falls back to "
                        f"raw std, which is provably >= residual_std for any OLS fit with an "
                        f"intercept term (conservative against a false CONFIRM; liberal/"
                        f"anti-conservative against a false REFUTE, since inflating the "
                        f"statistic only ever makes stat>=boxA easier to satisfy -- NOT "
                        f"'conservative in every case'). raw/residual ratio this point: "
                        f"{ratio:.3f}x)")
    if stat <= 0.5 * boxA:
        verdict = "CONFIRM"
    elif stat >= boxA:
        verdict = "REFUTE"
    else:
        verdict = "AMBIGUOUS"
    return dict(verdict=verdict, stat_used=stat, stat_source=stat_source, boxA=boxA,
                raw_std=raw_std, residual_std=fit["residual_std"],
                raw_over_residual_ratio=ratio)
```

### `analyze.py` line-85 companion call site — exact diff (Attack 6, non-blocking, adopted)

```python
# OLD:
    fit = R.linear_fit_1_over_margin(R.MARGINS, delta_values)
    item_ii_verdict, boxA = R.classify_item_ii(r, fit["residual_std"])
    item_ii = dict(margins=list(R.MARGINS), delta_values=delta_values, fit=fit,
                   verdict=item_ii_verdict, delta_boxA=boxA)

# NEW:
    fit = R.linear_fit_1_over_margin(R.MARGINS, delta_values)
    item_ii_result = R.classify_item_ii(r, fit, delta_values)
    item_ii = dict(margins=list(R.MARGINS), delta_values=delta_values, fit=fit,
                   verdict=item_ii_result["verdict"], delta_boxA=item_ii_result["boxA"],
                   stat_used=item_ii_result["stat_used"],
                   stat_source=item_ii_result["stat_source"],
                   raw_std=item_ii_result["raw_std"],
                   residual_std=item_ii_result["residual_std"],
                   raw_over_residual_ratio=item_ii_result["raw_over_residual_ratio"])
```

Not re-run against live captures this cycle (no committed pickles exist —
session-scratch only, per exp-108's own Idealizations); shown here so the
call site is not left inconsistent with the new function signature, and
so this companion edit is disclosed alongside the R18 gap it shares with
`classify_item_ii()`'s own new branch (neither gets a fault-injection
positive/negative control this cycle — see Idealizations).

### `run.py`'s `--predictions-only` block — R23 assert restoration (item 2a)

```python
# OLD:
    if "--predictions-only" in sys.argv:
        print(build_predictions_text())

# NEW:
    if "--predictions-only" in sys.argv:
        predictions_text = build_predictions_text()
        assert DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
        print(predictions_text)
```

### `build_result_text()` — wall-time attribution note (fix 5)

```python
def build_result_text(n_fdtd_calls, total_wall_s, gate_p0_pass, repro_pass,
                       item_i, item_ii, item_iii, item_iv, closure_rows,
                       wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    return f"""RESULT (exp-108, Panel Iteration 85)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time, zero `lab/` diff except the new stage26 addition.{wall_time_note}

**Gate P0: {{'PASS' if gate_p0_pass else 'FAIL'}}.**
**Reproduction precondition: {{'PASS' if repro_pass else 'FAIL'}}.**
**Item i:** {{item_i}}
**Item ii:** {{item_ii}}
**Item iii:** {{item_iii}}
**Item iv:** {{item_iv}}
**closure:** {{closure_rows}}
"""
```

`wall_time_source` is optional (default `None`, backward-compatible with
any future caller that doesn't need it) — this cycle's own call passes
`"exp-108's own historical spend, reused verbatim -- exp-109 makes zero
new Sim.run() calls"`.

### `experiments/109-.../reclassify_108.py` (new)

Direct sibling of `experiments/108-.../reclassify_106.py`, same zero-FDTD
import-and-recompute idiom (`importlib.util.spec_from_file_location`,
since the source directory name is not a valid package identifier; loads
the **patched** `experiments/108-.../run.py`, module-level exec only —
`Sim.run()` is unreachable outside `if __name__ == "__main__":`). Flow:

1. Load the patched `experiments/108-.../run.py` module.
2. Load `experiments/108-.../results.json` (read-only — not modified).
3. For each `r` in `(156, 312)`: pull `tier1[f"r{r}"]["item_ii"]["fit"]`
   and `["delta_values"]` (both already persisted) and call the patched
   `classify_item_ii(r, fit, delta_values)`. Print OLD verdict (exp-108's
   own committed string) vs. NEW verdict/`stat_used`/`stat_source`/ratio.
4. Call `build_predictions_text()`; assert `DISCLAIMER in predictions_text`.
5. Read `gate_p0_pass = tier1["r156"]["gate_p0"]["pass_"] and
   tier1["r312"]["gate_p0"]["pass_"]` (explicit AND, fix 4) — likewise
   `repro_pass` from both `reproduction_precondition.pass_` fields.
   Read `n_fdtd_calls`/`total_wall_s` directly from `results.json`'s own
   top-level keys. Build `item_i`/`item_iii`/`item_iv`/`closure_rows`
   summary strings from exp-108's own committed, UNCHANGED values (this
   cycle does not re-score items i/iii/iv/closure) and an `item_ii`
   summary string from the new gated verdicts. Call `build_result_text(
   ..., wall_time_source="exp-108's own historical spend, reused
   verbatim -- exp-109 makes zero new Sim.run() calls")`; assert
   `DISCLAIMER in result_text`.
6. Write `experiments/109-.../results.json`: `predictions_text`,
   `result_text`, `item_ii_reclassified.r156`/`.r312` (each: `old_verdict`,
   `new_verdict`, `stat_used`, `stat_source`, `raw_std`, `residual_std`,
   `raw_over_residual_ratio`, `fit` passthrough), and a provenance pointer
   to exp-108's own committed `results.json` (its git blob hash via
   `git hash-object`, recorded at run time — not hand-typed).

## Predictions — committed BEFORE any Phase 4 execution

All four items are deterministic, zero-FDTD reproducibility gates on
already-committed primitives, independently re-derived from those
primitives three separate times this cycle (Phase 1's own proposal,
five blind Phase-2 critiques, and Red Team's own audit) — not physical-
uncertainty forecasts.

### Item 4 (the substantive question)

`fit["smooth"]` is already persisted in exp-108's own `results.json` at
both r: `r=156`: `is_monotonic=False`, `r_squared=0.6654 < 0.90` →
`smooth=False`. `r=312`: `is_monotonic=False`, `r_squared=0.0205 < 0.90`
→ `smooth=False`. **Both r therefore take the new raw-fallback branch.**

| r | `stat_used` (raw `np.std`) | `residual_std` (detrended, unused this branch) | `raw_over_residual_ratio` | CONFIRM bar | REFUTE bar | Predicted verdict |
|---|---|---|---|---|---|---|
| 156 | **5.008328×10⁻⁶** | 2.897163×10⁻⁶ | **1.729×** | 1.4845×10⁻⁵ | 2.969×10⁻⁵ | **CONFIRM** (2.96× inside) |
| 312 | **2.124086×10⁻⁶** | 2.102199×10⁻⁶ | **1.010×** | 1.234×10⁻⁵ | 2.468×10⁻⁵ | **CONFIRM** (5.81× inside) |

**Prediction: `reclassify_108.py` reports `new_verdict="CONFIRM"` at both
r, `stat_used` matching the table above to <1e-9 relative,
`raw_over_residual_ratio` matching to <1e-3 relative, and `stat_source`
containing the substring `"raw/undetrended"` (not `"detrended"`) at both
r.** Falsified by any deviation. **Non-outcome-reversing** — CONFIRM
survives at both r, exactly as exp-108's own Phase-5 annotation already
disclosed informally — but this closes R24's second instance for real: a
coded, executed, falsifiable gate, not an unscored footnote.

### Items 1–3 (mechanical — a coded/persisted-or-not check)

| Check | Predicted | Falsified if |
|---|---|---|
| `assert DISCLAIMER in predictions_text` (`run.py --predictions-only`, and `reclassify_108.py`) | passes silently, both call sites | `AssertionError`, either site |
| `assert DISCLAIMER in result_text` (`reclassify_108.py`, first-ever live-fired call to `build_result_text()` with real values) | passes silently | `AssertionError` |
| `experiments/109-.../results.json["predictions_text"]` | present, non-empty, contains `DISCLAIMER`'s exact text | absent, empty, or missing the substring |
| `experiments/109-.../results.json["result_text"]` | present, non-empty, contains `DISCLAIMER`'s exact text, contains both `"CONFIRM"` strings and both ratio figures from the table above, contains the wall-time attribution note (fix 5) | any of the above missing or contradicted |
| `grep -c "assert" experiments/108-.../run.py experiments/109-.../reclassify_108.py` | ≥1 in `run.py`, ≥2 in `reclassify_108.py` | either returns 0 |
| `gate_p0_pass`/`repro_pass` (fix 4, explicit AND) | both `True` (all four source booleans independently confirmed `True` by Red Team, §0.4 of `phase2_redteam_audit.md`) | either `False`, or the reduction rule is not the stated AND |
| Trust suite (`--only 12346789`) | remains green, unaffected (zero `lab/` diff) | any regression |

**Binding execution requirement (VISION's mandatory fix 6, R25-precedent
conditional):** this document's own Result section, once Phase 4
completes, quotes `results.json['result_text']` and
`['predictions_text']` **verbatim, in full** — not a paraphrase or a
description of having asserted them.

## Idealizations

- Scoped to exactly the four Tier-0 UNBLOCKED items. **Not attempted:**
  Tier-0 item 0 (ruling on the Iteration-85 Checkpoint-4 firing — Marsh's
  call, blocked, out of scope); every Tier-1/2/3 item on the same queue
  (item i's global-vs-local renormalization, a synthetic positive/
  negative control for `linear_fit_1_over_margin`'s own smooth/noise
  discriminator, `stage26`'s symmetric negative control, the r=624 fourth
  point, the fabrication-tolerance framing, the oblique-angle/750-450nm/
  `G40`/x-wall/`PAD` items, `box_dev`'s own thinning margin).
- **R18 discipline, flagged not discharged, extended this cycle to name
  both sites.** `classify_item_ii()`'s new branch AND `analyze.py`'s
  companion call site are new/changed logic joining an already-partially-
  verified architecture (`linear_fit_1_over_margin`, `classify_item_i`'s
  own sibling gate). Neither receives its own fault-injection positive/
  negative control this cycle — validated only by (a) the general OLS
  inequality proof (holds for any data, not fault-injected) and (b) exact
  reproduction against the two already-committed r points. The
  Iteration-86 queue's own Tier-1 item 2 (a synthetic control for
  `linear_fit_1_over_margin` itself) is the natural place to extend that
  control to cover both — named here, not executed, not silently assumed
  complete.
- **`R2_SMOOTH_THRESHOLD=0.90` itself is not re-derived or re-calibrated
  for item ii's own question this cycle** (QUANTUM's named-but-not-
  mandatory concern, Red Team's own explicit, disclosed override,
  above) — non-outcome-reversing at both tested r, correctly queued as
  Tier 2 item 3, not dropped.
- `classify_item_ii()`'s signature change (`(r, residual_std)` →
  `(r, fit, delta_values)`) and return-type change (bare tuple → dict) are
  breaking changes for any future caller; none exists today outside
  `analyze.py`'s own single call site (patched here) and
  `reclassify_108.py` (new, this cycle).
- Does not re-run `analyze.py` against exp-108's own live phasor
  captures — those pickles live in a session-scoped scratch directory,
  not committed to git; every input this cycle's reclassification needs
  is already persisted in exp-108's own committed `results.json`
  (`tier1.r{r}.item_ii.fit` and `.delta_values`, both present, both
  independently re-verified from that file three separate times this
  cycle), matching `reclassify_106.py`'s own established zero-FDTD,
  import-and-recompute idiom exactly.
- `experiments/108-.../results.json`, `NOTES.md`, and
  `phase5_redteam_audit.md` are **not** modified — historical record, left
  as-is, matching the R4 "annotated, not overwritten" discipline this
  document family already applied one cycle upstream to exp-106's own
  record. `experiments/108-.../run.py` and `.../analyze.py` (code, not
  results) **are** patched in place — the precedent exp-108 itself set
  patching exp-106's own `run.py`.
- Does not reopen R25 (genuinely, independently discharged, a different
  channel) or the R23 ratify-as-scoped ruling's own OUTCOME (only closes
  the specific evidentiary gap — `build_result_text()` unexercised, the
  DISCLAIMER never live-fired in a Result document, the human-readable-
  citation half unbound — that ruling's own bound condition and exp-108's
  own Phase-5 VISION review named as still open).
- No thermal sidecar, no ambient/perceptual scoring, no new FDTD anywhere
  in this document. `lab/` diff: none.

## T1 escape-route statement

**N/A.** Nothing in this document builds, varies, or claims any σ(I)/
σ(x,t)/angular-selectivity/sub-threshold mechanism; no constraint-1/2/3/4
verdict is scored or moved. Confirmed structurally by Red Team's own
Phase-2 audit (Attack 7, a negative-result check stated explicitly rather
than left an unchecked assertion): every touched or added code path is a
classification-statistic gate or a text/persistence pipeline over
already-committed scalars, none of which reads or writes an optical,
absorption, or perceptual parameter.

## Result

*(Phase 4 not yet run. This section is filled in after execution, quoting
`results.json['result_text']`/`['predictions_text']` verbatim per the
binding execution requirement above — Predictions section, and mandatory
fix 6.)*
