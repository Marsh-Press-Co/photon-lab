# PHASE 1 — PROPOSAL · Panel Iteration 63 · exp-086 · Lead seat: ELECTROMAGNETISM

## "Fixing the Boundary-Pinning Defect and Re-Scoring exp-085 on the Corrected Machinery" — a zero-FDTD instrument-repair batch executing Red Team's Reconciled Iteration-63 Ranking, Tier-1 items (1)–(5)

### 1. Mechanism narrative (≤300 words)

This is not a mechanism proposal. Like every T28 desk cycle since exp-069,
it proposes no absorption physics and touches no constraint-3 scene —
**Checkpoint criterion 2 is N/A, stated plainly, not argued through a T1
escape-route framework that does not apply here** (see §3).

The object under repair is `free_period_with_widening`'s own
`chosen`-selection loop (`pad_round_trip_model.py`, exp-077's origin;
`y_wall_prescreen.py`, exp-078's verbatim copy, the version exp-085's own
Method C actually calls). When a staged widening search — `narrow[1,4]` →
`wide[1,15]` → `widest[1,60]` degrees — never finds an interior optimum at
ANY stage, the loop's own `chosen is None or (chosen["at_boundary"] and
not at_boundary)` update rule fires exactly once, at the *first* (narrowest)
stage, and never again: it silently returns the least-widened,
worst-informed candidate as if it were a converged fit, indistinguishable
in the output from genuine convergence. LOGBOOK's new standing rule R11
(Iteration 62) names the fix: when every stage is boundary-pinned, return
the *widest* stage's own value with an explicit `converged=False`/
`no_interior_optimum=True` flag, surfaced through every caller — never the
narrowest stage silently.

This cycle exists because exp-085's own Red Team final audit found the
defect live in Method C's 37 sliding sub-windows (6/37 exact all-stage
pins, 15/37 in the broader "period exceeds the window's own physical
width" category), corrupting the filed "STRONG COHERENT CHIRP"
classification into something the corrected `frac_recovered=0.595` cannot
actually support. Iteration 63's mandate, per that audit's own §7
reconciled ranking, is to apply the fix to the shared machinery, re-score
exp-085's own already-collected data on it, harden the significance
statistics the same audit flagged as separately invalid, bound-audit prior
citations for silent corruption, and close two cosmetic/hygiene gaps — one
batch, zero new FDTD, precondition for every other queued T28 fix to mean
anything.

### 2. Parameter table

| Quantity | Value / signature | Reused unchanged / New |
|---|---|---|
| Function fixed (site 1) | `free_period_with_widening(thetas, delta, label)` — `experiments/077-t28-pad-round-trip-echo-model/pad_round_trip_model.py`, currently lines 374–407 | **MODIFIED** — post-loop fallback logic only; the 3-stage search loop itself (`stages`, `_free_period_search` calls, `at_boundary` computation) is **UNTOUCHED** |
| Function fixed (site 2) | `free_period_with_widening(thetas, delta, label, out_list)` — `experiments/078-t28-y-wall-echo-prescreen/y_wall_prescreen.py`, currently lines 325–361 — **the version exp-085's `phase4_derivation.py` actually imports and calls** (traced: `phase4_derivation.py` loads `experiments/084-.../phase1_derivation.py`, which does `ywp = _load(EXP078_DIR/y_wall_prescreen.py)`, `free_period_with_widening = ywp.free_period_with_widening`) | **MODIFIED**, identical fix shape; `SS_TOT_DEGENERATE_FLOOR`/degenerate-array guard (already present, a prior docket item) **UNTOUCHED** |
| Fix logic (both sites) | After the stage loop: `if chosen["at_boundary"]: chosen = <widest-stage record>; chosen["converged"]=False; chosen["no_interior_optimum"]=True` else `chosen["converged"]=True; chosen["no_interior_optimum"]=False`. `chosen["at_boundary"]` is `True` after the loop **if and only if** every stage was boundary-pinned (the loop only ever sets `at_boundary=False` on the record that triggers `break`) — this is the exact, sufficient detection condition for R11's own "all-stages-boundary" case, no new heuristic invented. | **NEW** (~6 lines/site) |
| Explicitly OUT of this batch's scope | `pad_round_trip_model.py::free_period_with_widening_quiet` — a *different*, 2-stage (`[1,4]`,`[1,15]`) function used inside exp-077's own 20,000-trial Monte Carlo null loops. Different signature, different stage list, feeds already-published, already-gated null distributions this batch's zero-new-FDTD/re-score-only scope should not silently perturb. | **UNTOUCHED**, named as a forward item (§5, idealization 6), not silently left broken |
| Re-score target | exp-085's Method C: 37 sub-windows, `θc∈{5°,7°,…,77°}`, each `θc±3°`/0.2° step (31 pts) | Curve data **NOT persisted** per sub-window in `derivation_results.json` (only summary stats: `p_local_reported_at_39`, `p_local_corrected`, `r2_local`, `window`) — regenerated via `FastEval` (exp-085's own cached-Green's-function evaluator, already verified bit-identical to `dg048.edge_diffraction_c_empty_corrected` at 7 spot-check angles) on the **identical, already-committed** `theta_centers`/sub-window recipe. Deterministic formula, deterministic grid ⇒ bit-identical curves guaranteed by construction, not a new evaluation in any physics sense — **cheap** (37×31=1,147 evaluations, sub-second, the same cost exp-085's own realizability note already priced) |
| Re-score target | exp-085's Method A: `θ∈[2°,80°]`, step 0.02°, N=3,901 | Curve (`c_wide`) **IS persisted** (`derivation_results.json::method_a.curve`, 3,901 floats) — **read directly, zero re-evaluation**, only the fit/null re-run through the corrected `free_period_with_widening` |
| "Recovered" criterion for the corrected `frac_recovered` | `r2_local ≥ 0.30` **AND** `converged == True` **AND** `p_local_corrected ≤ 6.0°` (the sub-window's own physical width — Red Team's audit §1.4 criterion, kept as the operative "unresolvable regardless of fit quality" bound alongside the new flag; a converged fit can still report a period the 31-point/6°-wide window cannot possibly resolve one cycle of) | **NEW** — combines R11's own flag with the audit's own pre-existing period-width bound; see §4 for why using the flag *alone* is insufficient |
| Circular-shift null coverage | All 37 Method C sub-windows (was 10/37, evenly strided) | **EXTENDED**, reusing `circular_shift_null()` verbatim from `phase4_derivation.py` (exhaustive, 30 offsets/sub-window) |
| Spearman significance correction | Non-overlapping stride subsample of the RECOVERED-only sub-windows (33.3%-pairwise-non-overlapping stride, since sub-windows are 6°-wide/2°-step ⇒ stride-3 apart = 6° apart = adjacent, non-overlapping) — Red Team audit §1.8's own reconstruction as the starting method, applied here to the corrected/recovered data, not the as-filed data it was demonstrated on | **NEW** application of an **existing, audit-verified** method |
| Timing persistence | Per-stage (`elapsed_s` per `free_period_with_widening` call) and per-null (`elapsed_s` per `circular_shift_null` call, already computed in-memory, currently discarded before `json.dump`) | **NEW** JSON fields only — zero new computation, `time.time()` deltas already exist in local scope |
| `rd_wide_fft` mislabel | `phase4_derivation.py` line ~405/418: `rd_wide_fft = rel_dev(P_wide, P_fft)` printed under `"vs mean"` | **NOT** re-edited in exp-085's own historical file (house convention: flag, don't silently rewrite a closed cycle's own record) — corrected **in this cycle's own script and write-up**; NOTES.md's "62.8%...of their mean" citation corrected here to 91.6% (mean-relative), both independently recomputed, not hand-typed (R4) |
| Prior-citation audit scope | All committed `*.json` in `experiments/069-085` carrying `free_period_with_widening`/`_free_period_search` output (21 files identified: `069/results.json`, `070–073/results.json`, `074`'s 2 files, `075`'s 3 files, `076`'s 2 files, `077/pad_round_trip_results.json`, `078`'s 5 files, `079/y_wall_aperture_sum_results.json`, `080/validity_precheck_results.json`, `081`'s 2 files, `082`'s 3 files, `083`'s 2 files, `084/derivation_results.json`, `085/derivation_results.json`) | Grep for explicit `at_boundary` keys (present ⇒ direct read); where absent, flag any period-like numeric field within 0.5% of `{1.0, 4.0, 15.0, 60.0}°` (the 3-stage boundaries) or `{1.0, 4.0, 15.0}°` (the quiet-variant's 2-stage boundaries) as a candidate, then **directly re-derive** (re-run the raw staged search) each flagged candidate — audit §1.5's own method, exact, extended in file coverage from "077–084" to the full "069–085" board |

**Correction, added post-Phase-5 (Red Team's final audit §1.3/§6 item 2;
house convention: flag this cycle's own still-open document, don't
silently rewrite the frozen table above)**: the "Prior-citation audit
scope" row's own "069–085, 21 files" framing was never actually executed
— `phase4_prior_citation_audit.py` correctly scanned only `experiments/
077–085` (18 files), matching this document's OWN prediction (4) text two
paragraphs below, which already correctly reasons that the defect
"postdates exp-076" and is "absent from 069–076's own committed code
paths." Independently confirmed absent by two separate grep methods
(THERMODYNAMICS' Phase-2 critique, MATERIALS' Phase-5 review): zero
`free_period_with_widening`/`at_boundary` occurrences anywhere in
069–076's committed JSON. No citation is at risk from this
table-vs-prediction inconsistency; it is a self-citation/documentation-
precision defect, closed here.

### 3. Checkpoint criterion 2 statement

**N/A**, matching every T28 desk cycle since exp-069 and exp-085's own §0/
§4 ruling verbatim. This is instrument-repair/record-hygiene work on
already-committed, model-internal search machinery — no absorption
mechanism is proposed, no constraint-3 scene is touched, and nothing here
bears on T1's escape-route taxonomy. There is no "T1 escape route" for this
cycle to take; forcing that section would misstate the work.

### 4. Falsifiable predicted outcomes

**(1) Corrected `frac_recovered`: predict 0.595 (22/37), tolerance
±1 window (0.568–0.622, i.e. 21–23/37).** Red Team's audit hand-computed
0.595 by excluding the 15 sub-windows whose AS-FILED `p_local_corrected`
exceeds 6° from the numerator, denominator held at 37. This proposal's own
re-derivation of that exclusion set (§2, table row "Recovered criterion")
found a subtlety the audit's own hand table does not resolve: of the 6
confirmed all-stage-boundary windows (`θc=45°,59°,61°,63°,71°,73°`), one —
`θc=45°` — has an AS-FILED `p_local_corrected=4.397°`, *under* the 6° cutoff
purely by coincidence of what the narrowest (wrong) stage happened to
report, so the audit's own `>6°`-width proxy filter does not catch it, even
though it is a confirmed silent-fallback artifact. Under the mandatory,
flag-based criterion this proposal adopts (`converged==True` required,
not merely `period≤6°`), `θc=45°` is correctly excluded regardless of what
its *corrected* (widest-stage) period turns out to number, landing the
count at 21/37=0.568 rather than 22/37=0.595. **The load-bearing,
robust claim — the one this prediction is actually staked on — is that
BOTH figures fail the shared `≥0.80` gate by a wide margin**; only the
third decimal is uncertain, and that uncertainty is itself pre-registered
and explained, not discovered after the fact.

**(2) Corrected `classification_a`: predict NOT STABLY PERIODIC.** Gate:
`phase4_derivation.py`'s own existing decision code, `frac_recovered<0.80
⇒ NOT STABLY PERIODIC` (unconditional, first-checked branch) — since (1)
predicts `frac_recovered∈[0.568,0.622]`, this branch fires regardless of
`spread`/`ρ`'s own corrected values. Falsified only if the corrected
`frac_recovered` clears 0.80 — which would require at least 30/37 windows
to independently pass `r2≥0.30 AND converged AND period≤6°`, a 8–9-window
swing from this prediction's own band.

**(3) Corrected Spearman significance under the overlap-adjusted test:
predict NOT independently significant** at the corrected sample. Applying
a non-overlapping (stride-3, 6°-apart) subsample restricted to the
RECOVERED-only sub-window set (~21–22 of 37, concentrated at
`θc≤45°` plus one point at `57°` — the tail driving the as-filed
`ρ=0.882` trend is disproportionately the excluded `θc≥47°` region) leaves
roughly **7–9 independent points**. Predict `|ρ_corrected|≤0.75` and
`p>0.05` on that reduced, non-overlapping, recovered-only set — i.e., the
overlap-and-exclusion-corrected test does NOT independently rescue a
significant monotonic trend, consistent with (not decisively refuting)
the audit's own §1.6 finding that a real, much more modest residual
(~2× growth over the naive `1/cosθ` prediction, not the as-filed ~6×)
survives in the clean region. **Falsified** if the corrected test clears
`p<0.05` with `|ρ|>0.75` at this reduced n — that would reopen, not settle,
a genuine near-normal-quarter periodic-structure question this cycle is
not positioned to adjudicate either way.

**(4) Prior-citation audit outcome: predict no currently-cited T28
headline number is corrupted**, matching exp-085's own audit finding
(exp-078, exp-079 — both confirmed fired, both confirmed inert). Extending
file coverage to the full 069–085 board (vs. the audit's own 077–084) is
this proposal's own addition; predict it finds zero NEW firings beyond
those two, since the defect's origin (`free_period_with_widening`'s
specific `chosen`-loop shape) postdates exp-076 and the function is absent
from 069–076's own committed code paths. **Falsified** by finding any
`at_boundary:true`/boundary-proxy value feeding a period, spread, or
correlation figure that is STILL actively cited (in LOGBOOK.md's RULED
OUT/LIVE THREADS text, or PLAN.md's active queue) as of this cycle's own
close, undisclosed at the time it was cited.

**(5) Cosmetic fixes: zero classification impact**, confirmed already by
exp-085's own audit §1.10 (`disagreement` boolean already used the correct
mean-relative formula; only the *printed* label was wrong) — restated here
as a named, trivial prediction rather than left implicit.

### 5. Idealizations

1. **Zero new FDTD.** Every quantity re-scored is already a deterministic,
   zero-noise closed-form evaluation (`edge_diffraction_c_empty_corrected`)
   or a re-run of existing search/null machinery on already-committed or
   cheaply-regenerable inputs — identical scope discipline to exp-084/085.
2. **Reuses exp-085's own already-committed θ-grids and sub-window recipe
   verbatim** — no new sampling design, no new window width, no new
   center-angle convention. Any classification change is attributable
   entirely to the machinery fix, not to a re-specified instrument.
3. **The "recovered" criterion (§2) is a disclosed, reasoned design choice,
   not a re-derivation from first principles** — combining the R11 flag
   with the pre-existing period-width bound is this proposal's own
   judgment call, made explicit and falsifiable (§4-1) precisely because
   the two criteria do not coincide on all 37 windows, and the difference
   is arithmetically material only for `θc=45°`.
4. **`free_period_with_widening_quiet` (exp-077's Monte Carlo helper) is
   explicitly out of scope** — a different function, feeding different
   (already-published, already-gated) 20,000-trial null distributions;
   fixing it is a separate, future-scoped decision, not silently bundled
   here.
5. **The prior-citation audit (§2/§4-4) is bounded, not exhaustive** — a
   grep of committed JSON, not a dynamic re-run of every historical call
   site (Red Team's own docket item 7 explicitly ruled the fuller version
   "not required to close this cycle out"). A flagged candidate is
   directly re-derived; an unflagged one is not independently re-executed.
6. **This cycle does not re-open Checkpoint criterion 4's own
   forward-binding text** (LOGBOOK Iteration 62, R11's own closing
   paragraph): applying this fix IS the compliance action that clause
   requires of any future reuse of this machinery — it is not itself a
   new tripwire event.

### 6. Phase 4 plan (for Phase 2 critics to react to)

A single new script, `experiments/086-t28-free-period-boundary-fix-rescore/
phase4_rescore.py`, will: (a) apply the fix in-place to both
`pad_round_trip_model.py` and `y_wall_prescreen.py` (§2); (b) load
`experiments/085-.../derivation_results.json` read-only for `theta_centers`,
`method_a.curve`, and every already-published headline number (R4 — read,
never hand-typed); (c) regenerate the 37 Method C sub-window curves via
`FastEval` (re-verified bit-identical at the same 7 spot-check angles
exp-085 used, before any use); (d) re-fit all 37 via the corrected
`free_period_with_widening`, extend the circular-shift null to all 37,
recompute `frac_recovered`/`spread`/`ρ` under the §2 "recovered" criterion,
and run the overlap-corrected Spearman test; (e) re-fit Method A's
persisted curve through the corrected function (curve unchanged, fit
re-run); (f) run the bounded prior-citation grep/audit across the 21 named
JSON files, re-deriving any flagged candidate; (g) persist per-stage/
per-null `elapsed_s` fields; (h) fix the `rd_wide_fft` label. Output:
`phase4_rescore_results.json` + a `NOTES.md` reporting the corrected
`classification_a`, the overlap-adjusted significance figure, and the
audit outcome — each stated against this document's own pre-registered
bands (§4), not narrated after the fact.
