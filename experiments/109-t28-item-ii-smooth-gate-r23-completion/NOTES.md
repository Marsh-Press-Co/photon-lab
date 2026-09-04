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

Phase 4 executed. All four items confirmed exactly as predicted, zero
new `Sim.run()` calls, zero `lab/` diff (`git diff --stat lab/` empty),
trust suite green before and after (41/41, `--only 12346789`, 100s/102s).
Full console record: `run_output.txt`. `results.json` written with all
predicted keys present.

**Item 4 (the substantive question) — CONFIRMED exactly as predicted.**
`new_verdict="CONFIRM"` at both r; `stat_used` matches the frozen table
to <1e-9 relative (`5.008328e-06`/`2.124086e-06`); `raw_over_residual_ratio`
matches to <1e-3 relative (`1.7287`/`1.0104` vs. predicted `1.729×`/
`1.010×`); `stat_source` contains `"raw/undetrended"` (not `"detrended"`)
at both r. Falsification condition (any deviation) did not fire.

**Items 1–3 (mechanical) — all confirmed exactly as predicted.**
`assert DISCLAIMER in predictions_text` passed silently, both call sites
(`run.py --predictions-only` and `reclassify_108.py`). `assert DISCLAIMER
in result_text` passed silently on `build_result_text()`'s first-ever
live-fired call with real values. `results.json["predictions_text"]` and
`["result_text"]` are both present, non-empty, and contain the
`DISCLAIMER` text (independently checked: `"no Weber-contrast" in
predictions_text`/`result_text"` both `True`). `grep -c "assert"`:
`run.py` = 1 (≥1, predicted), `reclassify_108.py` = 3 (≥2, predicted).
`gate_p0_pass`/`repro_pass` (explicit AND, fix 4) both `True`. Trust
suite remained green, unaffected.

**Binding execution requirement (VISION's mandatory fix 6) — quoted
verbatim, in full, below.**

### `predictions_text` (quoted verbatim from `results.json['predictions_text']`)

```
PREDICTIONS (pre-registered, exp-108, Panel Iteration 85)

Raw physical angular-scattering-pattern and absorbed-power/ extinction ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility. angular_scattered_pattern() is a square-path near-to-mid-field angular sample, not a true circular far-field pattern (function's own docstring). The absolute-floor six-margin family is a new convention this cycle, interpolating/extending the already-validated box_a/box_b pair, not independently re-derived from a resolution or aliasing bound.

**Tier 0, item 1** (deterministic): reclassify_106.py's reported string
contains "THREE-WAY-AMBIGUOUS"; all other fields bit-identical to
exp-106's own committed results.json.

**Gate P0** (ground-truth reproduction, zero cost): geom_fixedabs(156/312)
reproduces exp-106's own committed geom_156_fixedabs/geom_312_fixedabs
exactly. Falsified by ANY mismatch -> halt.

**Reproduction precondition** (item i, must PASS before any angular claim
is trusted): fresh PEC-cored capture's sections.widths() at box_a
reproduces exp-106's own committed ledger_r{r}['fixedabs'] to <1e-6
relative.

**Item i** (angular_scattered_pattern, unified multi-margin fix): CONFIRM
if every floor-cleared bin <=5% relative deviation at ALL 6 margins;
REFUTE if a >=3-bin contiguous run clears a 15% bar at margin=32 AND its
6-point across-margin sequence is smooth (monotonic or R^2>=0.90 fit to
A+B/margin); else AMBIGUOUS.

**Item ii** (absolute floor, six-margin, detrended): fit Delta(margin) =
A + B/margin; CONFIRM if residual_std <= 0.5*|Delta_boxA|; REFUTE if
residual_std >= |Delta_boxA|; else AMBIGUOUS. |Delta_boxA| = 2.969e-05
(r=156) / 2.468e-05 (r=312), reused from exp-107.

**Item iii** (numerator floor-gate, PEC-cored PRIMARY article):
frac_unresolved within +/-0.05 of exp-107's own hollow-article reading
(0.18275 at r=156, 0.2675 at r=312).

**Item iv** (chunked-vs-continuous suite-stage identity): positive control
max|diff|=0.0; negative control (corrupted checkpoint) deviates >1%
relative.

**closure** (ledger sanity, both articles, both r): <=0.1%, falsified if
>1%.

Cost gate (reused verbatim, exp-106's own r312_primary_committed rule):
pilot r=156 (3 calls) first; commit r=312 (3 calls) only if pilot empty-
scene wall time <90 min AND projected 3-call r=312 total <180 min.
```

*(This block is `run.py`'s own frozen exp-108 Predictions text, unchanged
by exp-109 — reproduced here only because `reclassify_108.py` calls
`build_predictions_text()` live and asserts the DISCLAIMER against it,
per this cycle's own R23 restoration. It documents exp-108's own frozen
predictions, not exp-109's — exp-109's own predictions are the
Predictions section above.)*

### `result_text` (quoted verbatim from `results.json['result_text']`)

```
RESULT (exp-108, Panel Iteration 85)

Raw physical angular-scattering-pattern and absorbed-power/ extinction ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility. angular_scattered_pattern() is a square-path near-to-mid-field angular sample, not a true circular far-field pattern (function's own docstring). The absolute-floor six-margin family is a new convention this cycle, interpolating/extending the already-validated box_a/box_b pair, not independently re-derived from a resolution or aliasing bound.

6 real FDTD calls, 7712.0s (128.53 min)
total wall time, zero `lab/` diff except the new stage26 addition.
(exp-108's own historical spend, reused verbatim -- exp-109 makes zero new Sim.run() calls)

**Gate P0: PASS.**
**Reproduction precondition: PASS.**
**Item i:** r=156 verdict=CONFIRM, r=312 verdict=CONFIRM (exp-108's own committed values, unchanged this cycle)
**Item ii:** r=156: OLD=CONFIRM -> NEW=CONFIRM (stat_used=5.008328e-06, raw/residual ratio=1.729x); r=312: OLD=CONFIRM -> NEW=CONFIRM (stat_used=2.124086e-06, raw/residual ratio=1.010x) -- both take the raw/undetrended fallback branch (fit not smooth at either r); both CONFIRM survives, non-outcome-reversing, exp-108's own Phase-5 annotation informally disclosed this, now a coded, executed, falsifiable gate (R24 second instance closed)
**Item iii:** r=156: 0.1827 pass=True, r=312: 0.2525 pass=True (exp-108's own committed values, unchanged this cycle)
**Item iv:** {'positive_control_max_diff': 0.0, 'positive_control_pass': True, 'negative_control_rel_diff': 2.0, 'negative_control_pass': True, 'stage': 'stage26_chunked_run_identity, lab/validation/run_all.py'} (exp-108's own committed value, unchanged this cycle)
**closure:** hollow: r156=0.000196, r312=0.000563; peccored: r156=0.000160, r312=0.000581 (exp-108's own committed values, unchanged this cycle)
```

*(This is exp-108's own `build_result_text()` template — its header line
literally reads "RESULT (exp-108, Panel Iteration 85)" because the
function is exp-108's own, unrenamed; exp-109 calls it, does not
reauthor it, per this cycle's own scope: patch exp-108's code in place,
do not fork it. The wall-time attribution line — fix 5 — makes clear
whose spend the header figures are.)*

## Same-shift note on R18 (disclosed, not discharged)

As disclosed in Idealizations: neither `classify_item_ii()`'s new branch
nor `analyze.py`'s companion call site received a fault-injection
positive/negative control this cycle. Validated instead by (a) the OLS
inequality (general, not fault-injected) and (b) exact reproduction
against both already-committed r points, immediately above. Queued as
Iteration-86's own Tier-1 item 2 (a synthetic control for
`linear_fit_1_over_margin` itself) — the natural place to extend that
control to cover both new/changed sites.

## Combined Verdict: **CONFIRM** (governance/instrumentation cycle —
no PROMISING/PARTIAL/RULED-OUT scoring applies; T1 correctly N/A
throughout, confirmed structurally by Red Team's Phase-2 Attack 7)

The R24 second instance is genuinely, verifiably discharged: the fix is
wired into the executed classification path (not merely narrated a third
time), independently re-derived by five blind Phase-2 critiques and Red
Team's own audit before this run, and reproduces exactly on execution.
R23's code/persistence half (items 2/3) is closed with a live-fired,
asserted, persisted `result_text`/`predictions_text`; its human-readable-
citation half (mandatory fix 6) is closed in this document, above,
by verbatim quotation — the specific gap exp-108's own Phase-5 VISION
review found still open after the code half was already fixed. All six
Red Team mandatory fixes were incorporated before this run (not after);
zero deviations from Predictions on execution; zero R-rule firings this
cycle (all six gaps caught blind, before freeze, exactly this program's
own unbroken discharge-test pattern).

## Next — candidate Iteration 87 directions (Director's own ranking)

Reconciled Iteration-87 queue (this cycle's own Tier-0 items are now
fully closed; nothing carries forward from them):

**Tier 0** — rule on the Iteration-85 Checkpoint-4 firing (still pending
Marsh; unchanged by this cycle, which fixed the code defect that CAUSED
the firing but does not itself rule on the firing's own governance
consequence — Red Team's own Phase-2 audit confirmed these are separate
acts, §3 of `phase2_redteam_audit.md`).

**Tier 1** (from exp-108's own still-open queue, unchanged by this cycle
— nothing here was touched) — re-normalize (or floor-gate) item i's
per-bin comparison against each bin's own LOCAL magnitude, not the
global peak (zero new FDTD, the single highest-value item on this
queue); a synthetic positive/negative control for `linear_fit_1_over_
margin`'s own smooth/noise discriminator — now doubly motivated, since
it would also discharge this cycle's own disclosed R18 gap on both
`classify_item_ii()`'s new branch and `analyze.py`'s companion call
site; extend `stage26`'s negative control to the symmetric truncation
direction.

**Tier 2** — a fourth r-point (r=624), now sharpened by this cycle's own
Attack 2 finding: the raw-std fallback is liberal toward false REFUTE,
not merely conservative toward false CONFIRM, so r=624's own reading
should be checked against BOTH bars, not assumed safe by the same margin
logic that held at r=156/312; MATERIALS' own fabrication-tolerance
framing for item i's CONFIRM with Red Team's own observer-angle caveat
folded in; formalize the absolute-floor six-margin family from a
resolution/aliasing bound, now including a re-derivation of
`R2_SMOOTH_THRESHOLD=0.90` for item ii's own question specifically
(QUANTUM's named-but-not-mandatory concern this cycle, Red-Team-deferred
here, not dropped).

**Tier 3** — the oblique-angle extension; the 750/450nm leg; the `G40`
full-width leg; the x-wall admittance refit; `PAD`-with-article survival;
`box_dev`'s own thinning margin (~9.0× at r=312, still unresolved).

Full record: `experiments/109-t28-item-ii-smooth-gate-r23-completion/`,
LOGBOOK.md Iteration 86.
