# PHASE 1 — PROPOSAL · Panel Iteration 86 (candidate exp-109)
## Lead seat: MATERIALS & METAMATERIALS (rotation lead)
## "Closing exp-108's Own Reconciled Tier-0 Queue: The R24 Second-Instance Smooth-Gate Fix, and R23's Missing `RESULT_TEXT` Half"

### 0. What kind of cycle this is

This is a **governance/instrumentation cycle, not a mechanism proposal** —
matching exp-107 and exp-108's own precedent exactly. **T1 escape route:
N/A.** No σ(I)/σ(x,t)/angular-selectivity machinery is built, varied, or
even touched; no material is proposed; no constraint-1/2/3/4 verdict is
scored or moved by any branch of this document. This cycle is scoped
**exactly** to the Reconciled Iteration-86 queue's four Tier-0 UNBLOCKED
items (`LOGBOOK.md` Iteration 85 CHECKPOINT block; `phase5_redteam_audit.md`
§9 of exp-108). Tier-0 item 0 — **ruling on the Iteration-85 Checkpoint-4
firing itself** — is Marsh's call, not a Panel proposal's; this document
names it, does not attempt it, and treats it as blocked/out of scope
throughout, exactly as the queue itself states.

### 1. Narrative (≤300 words)

MATERIALS did not build item ii's smoothness diagnostic and does not own
`sections.py`'s box-family machinery — but the realizability discipline my
charter owns (published/plausible/unobtainium, stated as concrete,
checkable parameters) is exactly the discipline this queue item is
missing: `classify_item_ii()` currently reports a number as "the genuine
floor" with no checkable condition attached to that label at all. My
job this cycle is the same shape as always, one level of abstraction
down: **make the classifier's own confidence claim as checkable as a
material parameter, no exceptions, no silent fallback.**

The fix itself is small and entirely reused: `classify_item_i()`, built in
the identical Phase-3 synthesis, already gates its REFUTE branch on
`fit["smooth"]` — item ii's own gate is the same diagnostic, ungated. I
propose gating the **statistic**, not inventing a new verdict bucket: when
`fit["smooth"]` is True, keep the detrended `residual_std` unchanged
(exp-108's own logic, untouched). When it is False, fall back to the raw,
undetrended `np.std(delta_values)` — provably ≥ `residual_std` for any
ordinary-least-squares fit with an intercept term (§4 below), so the
fallback can only make the floor read *more* conservatively, never
artificially tighter. Both branches are scored against the SAME
CONFIRM/AMBIGUOUS/REFUTE bands exp-108 already froze; nothing about the
bands themselves changes. Bundled at true zero marginal cost (all inputs
already sit in exp-108's own committed `results.json`): wiring
`build_result_text()` into an actually-executed path, restoring both
founding `assert DISCLAIMER in ...` calls, and persisting the resulting
`predictions_text`/`result_text` strings as real `results.json` keys —
closing R23's own "predictions-only-compliant" gap named at exp-108
Phase 5.

### 2. Parameter table

All four items touch only already-committed data
(`experiments/108-t28-reclassification-angular-pattern-batch/results.json`)
and code in exp-108's own directory (patched in place, the established
R25-precedent shape: exp-108 itself patched `experiments/106-.../run.py`
directly rather than forking it) plus one new script in exp-109's own
directory. **Zero new `Sim.run()` calls anywhere; zero `lab/` diff.**

| # | File | Old | New |
|---|---|---|---|
| 4 | `experiments/108-.../run.py` — `classify_item_ii()` | `def classify_item_ii(r, residual_std):` — never reads `fit`; unconditionally bands `residual_std` into CONFIRM/AMBIGUOUS/REFUTE | `def classify_item_ii(r, fit, delta_values):` — see exact body, below. Returns a dict `{verdict, stat_used, stat_source, boxA}` (was a bare `(verdict, boxA)` tuple) |
| 4 | `experiments/108-.../analyze.py` line 85 (call site) | `item_ii_verdict, boxA = R.classify_item_ii(r, fit["residual_std"])` | `item_ii_result = R.classify_item_ii(r, fit, delta_values)`; `item_ii` dict below gains `stat_used`/`stat_source` keys, `verdict`/`delta_boxA` keys unchanged in name and meaning — required companion edit so `analyze.py` does not raise `TypeError` against the new signature; not re-run against live captures (see Idealizations) |
| 1, 2b, 3 | `experiments/109-.../reclassify_108.py` (**new**, direct sibling of exp-108's own `reclassify_106.py`, same zero-FDTD import-and-recompute idiom) | does not exist | imports `classify_item_ii`, `build_predictions_text`, `build_result_text`, `DISCLAIMER` from the **patched** `experiments/108-.../run.py` (via the same `importlib.util.spec_from_file_location` trick `reclassify_106.py` already uses — the directory name is not a valid package identifier); loads exp-108's own committed `results.json` **read-only**; see exact flow, below |
| 2a | `experiments/108-.../run.py` — `if "--predictions-only" in sys.argv:` block | `print(build_predictions_text())` — no assert | `predictions_text = build_predictions_text()`; `assert DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"`; `print(predictions_text)` — exp-104's own founding call-site pattern, restored verbatim |
| 3 | `experiments/109-.../results.json` (**new file, this cycle's own** — exp-108's own `results.json` is NOT touched, matching the R4 "annotated, not overwritten" precedent this exact document family already applied to exp-106's `results.json`) | does not exist | contains, at minimum: `predictions_text` (str), `result_text` (str), `item_ii_reclassified.r156`/`.r312` (each: `old_verdict`, `new_verdict`, `stat_used`, `stat_source`, `fit` passthrough), `source_results_json_sha` or equivalent provenance pointer to exp-108's own committed file |

**`classify_item_ii()`'s exact new body** (the R24 second-instance fix
itself):

```python
def classify_item_ii(r, fit, delta_values):
    boxA = DELTA_BOXA[r]
    if fit["smooth"]:
        stat = fit["residual_std"]
        stat_source = (f"detrended (fit smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f})")
    else:
        stat = float(np.std(delta_values))
        stat_source = (f"raw/undetrended (fit NOT smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f} < {R2_SMOOTH_THRESHOLD:.2f} -- "
                        f"residual_std is not trusted as 'the genuine floor'; falls back to the "
                        f"more conservative raw std, which is provably >= residual_std for any "
                        f"OLS fit with an intercept term)")
    if stat <= 0.5 * boxA:
        verdict = "CONFIRM"
    elif stat >= boxA:
        verdict = "REFUTE"
    else:
        verdict = "AMBIGUOUS"
    return dict(verdict=verdict, stat_used=stat, stat_source=stat_source, boxA=boxA)
```

**`reclassify_108.py`'s exact flow:**

1. Load the patched `experiments/108-.../run.py` module (module-level
   exec only, matching `reclassify_106.py`'s own guard comment — no
   `Sim.run()` is reachable outside `if __name__ == "__main__":`).
2. Load `experiments/108-.../results.json`.
3. For `r` in `(156, 312)`: pull `tier1[f"r{r}"]["item_ii"]["fit"]` and
   `["delta_values"]` (both already persisted — verified present, this
   document's own §4 below) and call the patched `classify_item_ii(r, fit,
   delta_values)`.
4. Print, for each `r`: OLD verdict (`tier1[f"r{r}"]["item_ii"]["verdict"]`,
   exp-108's own committed string) vs. NEW verdict/`stat_used`/`stat_source`
   — the same "OLD vs. NEW, quoted inline" idiom `reclassify_106.py` and
   exp-108's own Result section already used for Tier-0 item 1.
5. Call `build_predictions_text()`; assert `DISCLAIMER in predictions_text`.
6. Assemble `build_result_text()`'s remaining arguments
   (`n_fdtd_calls=6`, `total_wall_s=7712.0`, `gate_p0_pass=True`,
   `repro_pass=True` — all four read directly from exp-108's own committed
   `results.json`, not hand-typed) with `item_i`/`item_iii`/`item_iv`/
   `closure_rows` summary strings built from exp-108's own committed,
   UNCHANGED values (this cycle does not re-score items i/iii/iv/closure)
   and an `item_ii` summary string built from the **new** gated verdicts.
   Call `build_result_text(...)`; assert `DISCLAIMER in result_text`.
7. Write `experiments/109-.../results.json` per the table above.

### 3. T1 escape-route statement

**N/A**, matching exp-107/exp-108's own governance-cycle framing.
Nothing in this document builds, varies, or claims any σ(I)/σ(x,t)/
angular-selectivity/sub-threshold mechanism; no constraint-1/2/3/4 verdict
is scored or moved. Confirmed structurally by construction: the only code
touched is a classification-statistic gate and a text/persistence
pipeline, neither of which contains or can contain a perceptual-scoring
code path.

### 4. Predicted outcomes — falsifiable bands, computed now from
already-committed primitives (deterministic; these are reproducibility
gates on the patch's own correctness, not physical-uncertainty forecasts)

**Item 4 (the substantive question — computed here, not deferred).**
`fit["smooth"]` is already persisted in exp-108's own `results.json` at
both r: `r=156`: `is_monotonic=False`, `r_squared=0.6654 < 0.90` →
`smooth=False`. `r=312`: `is_monotonic=False`, `r_squared=0.0205 < 0.90` →
`smooth=False`. **Both r therefore take the NEW raw-fallback branch.**
Independently computed by me, now, from the already-committed
`delta_values` arrays (`tier1.r{r}.item_ii.delta_values`, 6 values each):

| r | `stat_used` (`np.std(delta_values)`) | CONFIRM bar (`0.5·|Δ_boxA|`) | REFUTE bar (`|Δ_boxA|`) | Predicted verdict |
|---|---|---|---|---|
| 156 | **5.008328×10⁻⁶** | 1.485×10⁻⁵ | 2.969×10⁻⁵ | **CONFIRM** (2.96× inside the bar) |
| 312 | **2.124086×10⁻⁶** | 1.234×10⁻⁵ | 2.468×10⁻⁵ | **CONFIRM** (5.81× inside the bar) |

**Prediction: `reclassify_108.py` reports `new_verdict="CONFIRM"` at both
r, `stat_used` matching the two values above to <1e-9 relative, and
`stat_source` containing the substring `"raw/undetrended"` (not
`"detrended"`) at both r.** Falsified by any deviation — this is exact
arithmetic on numbers already in git, not a physical measurement.
**Non-outcome-reversing** (CONFIRM survives at both r, exactly as exp-108's
own Phase-5 Result-section annotation already disclosed informally) — but
this is the difference between a disclosed footnote and a coded,
checkable gate: R24's own text requires the latter, and only the latter
closes the second instance for real.

**Why the raw-std fallback, not a forced AMBIGUOUS (the alternative I
considered and reject).** Two candidate substitutes exist for the
non-smooth branch; I was asked to pick one, falsifiably:

- *(a) Raw, undetrended `np.std(delta_values)` — my choice.* This is
  provably conservative, not merely empirically so this cycle: for any
  ordinary-least-squares fit whose design matrix includes an intercept
  column (`linear_fit_1_over_margin`'s own `A_mat = [1, 1/margin]` does),
  the constant model `ŷ=mean(y)` is itself a feasible point in the
  least-squares search space, so the optimal fit's own residual sum of
  squares can never exceed `Σ(y−ȳ)²` — i.e. `R²≥0` always, i.e.
  `residual_std ≤ raw_std` always. Detrending can only shrink the
  apparent floor or leave it unchanged; it can never inflate it. Using the
  raw statistic when the detrending step itself is not licensed by a
  smooth trend is therefore the *more* conservative choice in every case,
  not merely this one — it cannot manufacture a false CONFIRM the way an
  unlicensed detrend can (exactly item ii's own R24 defect, one level
  removed). It is also independently what QUANTUM's own Phase-5 review of
  exp-108 computed by hand and confirmed non-outcome-reversing
  (`phase5_review_quantum.md` §"Single most important finding") — this
  proposal makes that hand-check the pre-registered, coded behavior
  instead of an informal aside.
- *(b) Force straight to AMBIGUOUS regardless of magnitude — rejected.*
  This is `classify_item_i()`'s own pattern for its REFUTE branch, but the
  analogy does not transfer: `classify_item_i()` only gates the branch
  that claims a *positive* finding (a real anisotropy) behind smoothness;
  its CONFIRM (null) branch is unconditional on smoothness, exactly
  because a null finding needs no trend-removal story to be believed.
  Item ii's CONFIRM branch is the same kind of null claim (the floor is
  small) — forcing it to AMBIGUOUS on a non-smooth fit would apply a
  stricter standard to item ii's null than item i's own sibling gate
  applies to ITS null, an inconsistency, not a parallel. It would also
  overshoot what the Phase-2 mandatory fix's own text ever asked for: that
  text only ever specified which STATISTIC to trust ("if smooth, report
  residual-from-fit... the raw std conflates..."), never a verdict-bucket
  override. Manufacturing a third rule the fix never specified is exactly
  the kind of un-pre-registered addition Red Team would flag as
  overreach at Phase 2.
- *(c) Leaving the gate undocumented/comment-only (the queue's own named
  alternative) — rejected outright.* R24's own operative text (element 3,
  `phase5_redteam_audit.md` §3 of exp-108) is precisely "the consequence
  was never coded — merely computed and left as an unscored, undisclosed
  observation." A code comment explaining why no gate exists IS that same
  failure shape, formalized. Only a coded, executed, falsifiable gate
  closes it.

**Items 1–3 (mechanical — a coded/persisted-or-not check, not a physical
prediction).**

| Check | Predicted | Falsified if |
|---|---|---|
| `assert DISCLAIMER in predictions_text` (`run.py --predictions-only`, and `reclassify_108.py`) | passes silently, both call sites | `AssertionError` raised, either site |
| `assert DISCLAIMER in result_text` (`reclassify_108.py`, the first-ever live-fired call to `build_result_text()` with real values) | passes silently | `AssertionError` raised |
| `experiments/109-.../results.json["predictions_text"]` | present, non-empty string, contains `DISCLAIMER`'s exact text | key absent, empty, or missing the substring |
| `experiments/109-.../results.json["result_text"]` | present, non-empty string, contains `DISCLAIMER`'s exact text, and contains both `"CONFIRM"` strings from item 4's own table above | key absent, empty, missing the substring, or item-ii language in it contradicts the reclassified verdicts |
| `grep -c "assert" experiments/108-.../run.py experiments/109-.../reclassify_108.py` | ≥1 in `run.py` (the restored predictions-side assert), ≥2 in `reclassify_108.py` (both restored asserts) | either file returns 0 |
| **Execution requirement (binding, per R25's own conditional, reused verbatim from exp-108's own Tier-0 item 1 table)** | Phase 4's Result section quotes, inline, the actual printed OLD-vs-NEW `item_ii` comparison and the pass/fail of both live asserts — not merely a description or recommendation | Result section only describes/recommends the fix without confirming execution — a live R25/R24 concern to flag even short of a fresh firing instance |

### 5. Idealizations

- Scoped to exactly the four Tier-0 UNBLOCKED items. **Not attempted:**
  Tier-0 item 0 (ruling on the Iteration-85 Checkpoint-4 firing — Marsh's
  call, blocked, out of scope); every Tier-1/2/3 item on the same queue
  (item i's global-vs-local renormalization, a synthetic positive/negative
  control for `linear_fit_1_over_margin`'s own smooth/noise discriminator,
  `stage26`'s symmetric negative control, the r=624 fourth point, the
  fabrication-tolerance framing, the oblique-angle/750-450nm/`G40`/x-wall/
  `PAD` items, `box_dev`'s own thinning margin).
- **R18 discipline, flagged not discharged.** `classify_item_ii()`'s new
  branch is new classification logic joining an already-partially-verified
  architecture (`linear_fit_1_over_margin`, `classify_item_i`'s own
  sibling gate) — R18 asks that such an addition receive its own
  fault-injection positive/negative control the SAME cycle it is added.
  This document's item-4 fix is validated here only by (a) the general
  OLS inequality proof (§4, holds for any data, not fault-injected) and
  (b) exact reproduction against the two already-committed r points — it
  does NOT inject a synthetic known-smooth or known-noisy 6-point sequence
  and confirm the branch selection falls out correctly. The Iteration-86
  queue's own Tier-1 item 2 (a synthetic control for
  `linear_fit_1_over_margin` itself) is the natural place to extend that
  same control to cover this new branch — named here, not executed by
  this Tier-0-only document, and not silently assumed complete.
- `classify_item_ii()`'s signature change (`(r, residual_std)` →
  `(r, fit, delta_values)`) is a breaking change for any future caller;
  none exists today outside `analyze.py`'s own single call site (patched
  here) and `reclassify_108.py` (new, this cycle).
- Does not re-run `analyze.py` against exp-108's own live phasor captures
  — those pickles live in a session-scoped scratch directory
  (`/tmp/claude-0/.../scratchpad/exp108/...`) and are not committed to
  git; every input this document's reclassification needs is already
  persisted in exp-108's own committed `results.json` (`tier1.r{r}.
  item_ii.fit` and `.delta_values`, both present and independently
  re-verified from that file at Phase 1, above), matching
  `reclassify_106.py`'s own established zero-FDTD, import-and-recompute
  idiom exactly.
- `experiments/108-.../results.json`, `NOTES.md`, and
  `phase5_redteam_audit.md` are **not** modified — historical record,
  annotated already by exp-108's own Phase-5 audit, left as-is, matching
  the R4 "annotated, not overwritten" discipline this exact document
  family already applied one cycle upstream to exp-106's own record.
  `experiments/108-.../run.py` and `.../analyze.py` (code, not results)
  ARE patched in place — the same precedent exp-108 itself set patching
  exp-106's own `run.py`.
- Does not reopen R25 (genuinely, independently discharged, a different
  channel) or the R23 ratify-as-scoped ruling's own OUTCOME (only closes
  the specific evidentiary gap — `build_result_text()` unexercised — that
  ruling's own bound condition named as still open).
- No thermal sidecar, no ambient/perceptual scoring, no new FDTD anywhere
  in this document. `lab/` diff: none.
