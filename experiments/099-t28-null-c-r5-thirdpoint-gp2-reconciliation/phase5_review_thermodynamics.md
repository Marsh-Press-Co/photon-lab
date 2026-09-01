# Panel Iteration 76 (exp-099) — Phase 5 Review — THERMODYNAMICS

*Fresh sub-agent, self-reviewing my own Phase-1 proposal / Phase-3 synthesis
from this same cycle. Blind to every other seat's Phase-5 review. Adversarial
self-audit, per the Director's brief — not a rubber stamp.*

## 1. Independent spot-verification

I recomputed the following load-bearing numbers directly from `results.json`
and `run.py` (not trusted from `NOTES.md`'s own prose), plus traced two
figures to the underlying code that produces them.

1. **Null C interval-slope-decay ratio `r₃`.** From the four filed points
   (`combined_report`): Δ₁ = 1.512684e-3 − 2.471869e-3 = −9.59185e-4,
   Δ₂ = 5.854146e-4 − 1.512684e-3 = −9.27269e-4, Δ₃ = 4.704114e-4 −
   5.854146e-4 = −1.150032e-4. `r₃ = |Δ₃|/|Δ₂| = 0.12402` → matches the
   cited `r₃=0.1240` (~8.06× drop) exactly.
2. **The two new `r_ratios`.** Continuing the sequence with the three new
   points (42.294201°/42.627601°/42.960901°): Δ₄ = 1.322251e-3 − 4.704114e-4
   = 8.518395e-4, Δ₅ = 2.456623e-3 − 1.322251e-3 = 1.134372e-3, Δ₆ =
   2.778079e-3 − 2.456623e-3 = 3.214553e-4. `|Δ₅|/|Δ₄| = 1.33167`,
   `|Δ₆|/|Δ₅| = 0.28337` — both match `results.json::item_1.r_ratios`
   exactly (`[1.3316739748300177, 0.28337723580831364]`), and both feed
   `amplitude_criteria_met = all(r<0.5 for r in r_ratios)` correctly to
   `False`, matching the filed value. **See §3 below — this exact
   verification surfaces a real, distinct labeling defect in `NOTES.md`'s
   own prose, though the underlying code and verdict are correct.**
3. **`crossing_cpl50` / `shift_40_50`.** θc40 = 39.921519316666235°
   (established), θc50 = 39.77686992722644° (this cycle's own new interior
   sweep, linear crossing between the 39.688519°/39.854519° bracket).
   θc50 − θc40 = −0.14464938943979° — matches
   `results.json::item_2.step3.richardson_30_40_50.shift_30_40` exactly
   (the field is relabeled per the proposal's own disclosed positional
   convention, not a duplicate/stale figure).
4. **Richardson `observed_ratio`.** `(−0.14464938943979)/(−0.15031902190763)
   = 0.96228` — matches `observed_ratio=0.962282667915931` exactly.
   `naive_order2_ratio = (40/50)² = 0.64` — matches exactly.
5. **Step-2 settling `rel_dev`.** `|5.243753061360268e-4 −
   5.253136125293878e-4| / 5.253136125293878e-4 = 0.17862%` — matches
   `rel_dev=0.0017861832836256804` exactly. Settling PASS (≤1% band) is
   correctly called.
6. **R13 floor gate.** `floor = 0.1 × RMS[frac_contrast]`:
   `0.1 × 0.0019174375118374476 = 0.00019174375118374476` — matches
   `r13_floor_gate.floor` exactly; the (unchanged, re-applied not
   recomputed) `FLOOR_FRAC=0.10` convention is honored correctly.
7. **Null C bracket margins.** `1.500°/0.3767516353289935° = 3.982×` and
   `1.500°/0.3201659178026546° = 4.685×` — match the cited "3.98×"/"4.69×"
   to stated precision.
8. **Item 3 tail ratio, spot check at θc=79°.**
   `0.21735385064978663/0.00025576654006225 = 849.81×` — matches
   `ratios_new[0].ratio_to_theta_c_5=849.8134689427543` exactly.

All eight independently reproduce. I additionally traced, in source
(`run.py`, not merely `results.json`), how `step1`/`step2` (item 2) are
constructed — the basis for §3's sharpest finding — confirming `run_r5_batch`
(Step 1) and `pair_metrics_full` (Step 2) both genuinely compute the
`p_abs_w_c/g`/`dt_ss_full_K_c/g`/`netd_classification_c/g` fields internally
before those fields are dropped by the caller (line-level citations below).

## 2. Steel-man

This is a disciplined, honestly-executed house-discipline cycle that does
real work inside its own declared scope. Three things are genuinely
creditable, independent of my own authorship of Phase 1:

- **R5's first-ever real FDTD spend was gated exactly as hard as Phase 2
  demanded, and the gates were not theater.** The three-way Phase-2
  convergence (MATERIALS' R15-addendum ground-truth-sign gap, QUANTUM's
  fault-injection-coverage gap, EM's unpriced-HALT gap) was independently
  re-verified by Red Team from source, adopted in full, and then actually
  discharged in Phase 4: Step 0's fault-injection re-scoring at
  `family="R5"` caught every one of six injected defects it was supposed to
  catch and passed every clean case; Step 1's far-from-null sign check at
  36.0° reproduced the established R4 sign
  (`-1.064305e-3` vs. `-8.776529e-4`, both negative); only then did Step 3
  run and find a genuine, cleanly-bracketed sign change. This is the
  correct order of operations for a resolution family this program's own
  R15 addendum was written specifically to distrust, and it is now
  demonstrably discharged rather than merely argued.
- **Item 1 followed its own tightened pre-registration faithfully, including
  the fix that made a favorable-looking result unavailable.** PHOTONICS'
  Phase-2 attack (Attack 5, adopted) raised the VANISHING-AMPLITUDE bar to
  require a half-width ≥ one full established period — which this cycle's
  own bracket cannot reach — and the Result section reports
  INCONCLUSIVE-AT-THIS-WIDTH exactly as that constraint requires, rather
  than quietly reporting the more publication-friendly VANISHING-AMPLITUDE
  the original (weaker) Phase-1 criterion would have allowed. The genuinely
  new finding underneath the label (a smooth local trough/bounce, not a
  monotonic decay) is disclosed, not buried.
- **Item 3's non-resolution is reported as a non-resolution.** The
  pre-registered falsification criterion (shape-match vs. shape-mismatch
  over the 74°–87° overlap) does not cleanly resolve either way — an
  unpredicted 77°→79° increase, partial-but-incomplete decline afterward,
  neither curve reaching its own "recovered" regime — and the Result
  section says so plainly instead of forcing a lean the data do not
  support.

## 3. Sharpest finding (THERMODYNAMICS charter)

**Item 2's own thermal/energy sidecar — this seat's own charter
instrument — is silently computed and then dropped at exactly the two
"first-ever" R5 measurement points this cycle exists to validate (Step 1,
R5's first-ever real angle in this program's history; Step 2, R5's
first-ever settling check), and my own `NOTES.md` never once mentions the
sidecar anywhere in Hypothesis/Setup/Predictions/Result/Learned.**

Traced precisely, in source, not merely alleged:

- `run_r5_batch()` (`run.py:233-276`, used by Step 1) builds each report row
  via `row = dict(delta_scene=..., frac_contrast=..., ratio_k=...,
  floor_pass=..., **netd_row(pm))` and *asserts*
  `NETD_ROW_KEYS <= set(row.keys())` before returning — i.e. Step 1's own
  underlying call genuinely computes and asserts the presence of
  `p_abs_w_c/g`, `dt_ss_full_K_c/g`, `netd_classification_c/g` for θ=36.0°.
  But the `step1` dict actually written to `results.json`
  (`run.py:414-418`) keeps only `theta`, `delta_scene`, `floor_pass`,
  `established_sign_negative`, `sign_match`, `established_reference`,
  `n_calls`, `wall_s`, `preflight` — every thermo field `run_r5_batch`
  computed and asserted is discarded before persistence. Confirmed against
  `results.json::item_2.step1`: no `p_abs_w`/`dt_ss_full_K`/
  `netd_classification` key anywhere in that object.
- `pair_metrics_full()` (imported from `experiments/093-.../run.py`, the
  literal `_full`/NETD-surfacing function R16 names) is called directly for
  Step 2 (`run.py:447-448`, `pm_7000`/`pm_10500`) and internally sets
  `pm["p_abs_w_g"] = g_cell["thermo"]["p_abs_w"]`,
  `pm["dt_ss_full_K_g"] = g_cell["thermo"]["dt_ss_full_K"]` (confirmed at
  `experiments/093-.../run.py:177-178`) — the C-side fields are present in
  `pm` under its own internal naming too. `netd_row()` is never called on
  `pm_7000`/`pm_10500` at all, and `step2`'s own dict (`run.py:462-464`)
  keeps only `angle`, `delta_scene_r5_steps`, `delta_scene_r5_steps_stress`,
  `rel_dev`, `verdict`, `n_calls`, `wall_s`, `preflight`. Confirmed against
  `results.json::item_2.step2`: no thermo field anywhere.
- By contrast, item 1's `combined_report` and item 2's own Step 3 `report`
  (both built through the same `run_r4_batch`/`run_r5_batch` idiom) *do*
  carry the full sidecar for every one of their cells, all reading
  `UNDETECTABLE` (`dt_ss_full_K` ≈ 4.9–5.5×10⁻⁵ K throughout, comfortably
  below every microbolometer NETD reference this program has sourced since
  T5/exp-043) and `ratio_abs_ext_raw` ≈ 0.5121–0.5153 at every one of this
  cycle's 11 new article cells — a further, unremarked-on confirmation of
  T9's established σ_abs/σ_ext≈0.51 anchor, now extending cleanly to R5
  resolution for the first time. **None of this — not the UNDETECTABLE
  read, not the T9-anchor extension, not the fact that two of item 2's own
  four sub-steps carry no energy reading at all — appears anywhere in
  `NOTES.md`'s prose.** `grep -in "netd\|p_abs\|energy"` against `NOTES.md`
  returns only the `netd_row()` function-name citation in §Setup and one
  unrelated "absorbing article" phrase in §Next — zero substantive mentions.

**Why this is squarely a self-critique, not a process nitpick.** THERMODYNAMICS'
charter is explicitly "owns the per-proposal energy sidecar... always asks
what re-radiates and whether it would be detectable." I am the rotation lead
this cycle; the `step1`/`step2` dict-construction code that drops these
fields is code I (as Director, synthesizing my own Phase-1 proposal) wrote
into `run.py`, and the `NOTES.md` Learned section I wrote states flatly "R5's
first-ever real FDTD spend passed every gate it was asked to clear" (Learned
#3) — true of the gates Phase 2 named (`xi_ext`/`sigma_abs_nonneg`/settling/
GT-sign), but silently incomplete about my own charter's instrument at
exactly the two points a future reader would most want the thermal read for
(R5's literal first-ever angle, and R5's first-ever settling check) —
precisely the "confident claim, unverified/incomplete in the delivered
record" shape this sub-thread's own THERMODYNAMICS self-review caught in
its own prior cycle (Iteration 70/exp-093, an almost identical self-critique
pattern one rotation-lead-THERMODYNAMICS cycle before this one).

**Is this an R16 violation?** Precisely, no — not as written. R16's
triggering shape is "a disclaimer travels... but the field it is meant to
cover is never persisted." No `netd_disclaimer`/`scope_note` key exists
anywhere in this cycle's `results.json` at all, so the specific "disclaimer
present, field absent" test R16 was built to catch does not literally fire
here (there is no disclaimer to check against). This is a narrower,
adjacent, first-seen-this-cycle shape: the byproduct is computed and
*asserted present* by the underlying function, then discarded by the caller
with **no disclaimer either way** and no prose acknowledgment. I flag this
precisely rather than claim it fires R16's own forward-elevating third-
instance clause (that would require the same "disclaimer travels, field
doesn't" shape, which is not what happened here) — but it is squarely the
failure R16 exists to prevent in substance, on the newest, least-tested
family this program has ever run, and it should be named, not merely
absorbed into "close but non-firing" by pattern-matching to R16 without the
precondition actually holding.

**Fix, cheap and deterministic** (matching the exp-094/R16 precedent
exactly): re-run `netd_row(pm)` against the already-captured `pm` objects
for Step 1 and Step 2 and backfill `results.json::item_2.step1`/`step2` —
zero new `sim.run()` calls, the underlying captures already exist, this is
a pure post-processing retrofit.

## 4. Secondary finding — a genuine `r`-index mislabeling in my own Result prose

Independently re-deriving the "bounce" description in `NOTES.md`'s Result
section against the four filed + three new points (§1 item 2, above): the
text states *"`r₄=|Δ₄|/|Δ₃|=1.332` (>1, growing...)"*. This is
internally inconsistent as written: `|Δ₄|/|Δ₃| = |8.518395e-4| /
|1.150032e-4| ≈ 7.41`, not 1.332. The value actually reported (1.332) is
`|Δ₅|/|Δ₄|` — the code's own `r_ratios[0]` (`run.py:363-365` builds
`diffs` from `[last filed point] + [3 new points]`, i.e. `diffs[0]=Δ₄`,
and `r_ratios[i]=|diffs[i+1]|/|diffs[i]|`, so `r_ratios[0]=|Δ₅|/|Δ₄|` by
construction — the ratio spanning the trough itself, `Δ₄` vs. `Δ₃`, is
never computed by the code at all). The underlying scored quantities
(`r_ratios`, `amplitude_criteria_met`, the verdict) are unaffected — this
is a prose-labeling error, not a computation error, and does not change
INCONCLUSIVE-AT-THIS-WIDTH. But it is exactly the R4-house-discipline shape
this program's own registry exists to name: a "not hand-typed"/"re-verified"
document (this cycle's own §1 leans explicitly on that rhetoric, and Red
Team's own Phase-2 audit already caught two sibling instances in the same
document — the θ₀ digit insertion and the interior-angle-label mismatch)
committing a *third*, Phase-5-only-caught instance of "a cited formula/index
does not reproduce as stated," one document, one cycle, three separate
occurrences of the identical failure shape (θ₀ citation, filed-table labels,
now the `r`-index in Result prose). Non-load-bearing to any verdict; worth
naming precisely because three instances of the same shape in one document,
even individually harmless, is the sub-thread's own established
recurrence-threshold ("a channel three prior R-rules have already shown
goes unowned" — see R19's own founding language) — this seat does not
propose a new rule on a single cycle's evidence, but names it for Red
Team's own aggregation across seats.

## 5. Tertiary finding — the T1 escape-route disposition holds up, and is
sharpened, not merely reaffirmed

Re-reading my own Phase-1 §3/`NOTES.md`'s §T1 disposition against the actual
Result: the ruling (option (b), T1: N/A justified this cycle, with an
explicit, self-overriding Iteration-77 trigger) holds up cleanly — nothing
in items 1–3's actual outcomes constitutes a new candidate mechanism, so
forcing a T1 entry would still have been the "unfalsifiable claim
manufactured to fill a field" Red Team's charter exists to strike. But the
actual Result *strengthens*, not merely repeats, the case for the trigger I
wrote: `delta_scene(θ)`'s sign structure is now resolution-tested at FOUR
cpl points at Null B (20/30/40/50, the first null in this program's history
with that much resolution depth) and newly shown, at Null C, to have
genuine non-monotonic (trough/bounce) structure inside the window this
program would need to convert into an angular-selectivity mask — i.e., the
"evidentiary basis" my own disposition said was not yet cashed out is now
*better characterized*, not merely *further validated*, than when I wrote
that trigger. If Iteration 77 defers the constraint-scoring pass again, the
case for reading my own disposition as overridden is stronger after this
cycle's own data than it was before it ran.

## 6. Verdict: **CONCUR-WITH-GAP(S)**

The cycle's three scored outcomes (item 1 INCONCLUSIVE-AT-THIS-WIDTH, item 2
SIGN-CHANGE-FOUND at θc50≈39.777° with all gates cleared, item 3 genuine
non-resolution) are correctly computed, independently reproduced from
primitives above, and honestly reported under their own pre-registered
rules — no verdict is disputed. The gaps found (§3, §4) are real,
independently verified from source, non-load-bearing to any scored outcome,
and both are cheap, same-shift-fixable. §3 in particular is a genuine miss
inside this seat's own charter duty that survived my own Phase-3 synthesis
undetected — disclosed here, not smoothed over, matching this sub-thread's
own established discipline for a self-reviewing lead seat.

## 7. Ranked top-3 candidate directions for Iteration 77

Independently re-derived from the actual Result, not merely restated from
my own `NOTES.md` draft Next section — I agree with my own Next §2 (the T1
trigger) and elevate it to #1 for the reason in §5 above; I **diverge** from
my own Next §3 (which asked only whether the Richardson pattern
*generalizes to Null A*) in favor of a sharper question the data now
support asking first.

1. **Execute the constraint-1/2/3/4 scoring pass — do not defer a second
   time.** This is my own Phase-1 committed trigger (§3/§T1 disposition,
   above), reaffirmed after re-reading the actual Result, not merely
   restated: cash out `delta_scene(θ)`'s now-four-resolution-point-deep
   sign structure at Null B, and its newly-discovered trough at Null C, as
   an angular-selectivity mask scored against `emit.observer_record`,
   `lab/ambient.py`, and the beam-behind box (PANEL.md's own Metrics
   table) — the actual phenomenon-target instruments this seven-cycle
   sub-thread has never once engaged. If Iteration 77 files T1: N/A again
   without addressing this, my own disposition should be read as
   overridden per its own terms.

2. **A formal convergence test at Null B, using all four now-available
   resolution points (cpl=20/30/40/50), asking whether the crossing
   location is converging to a fixed continuum value at all — not merely
   whether the super-linear pattern generalizes to a different null.** This
   is a genuine sharpening of, not a repeat of, my own draft Next §3: both
   observed Richardson ratios at Null B (0.777 at 20/30/40, 0.962 at
   30/40/50) sit far above the naive 2nd-order expectation (0.5625/0.64)
   *and* close to 1 — a ratio near 1 across successive resolution doublings
   is the textbook signature of a sequence that is barely contracting, if
   at all, not one converging cleanly to a fixed point. With four points on
   file for the first time on this sub-thread, a proper geometric/Aitken
   extrapolation (fit θc(cpl) against a `θc∞ + A·r^n` form and test whether
   `r` is bounded away from 1) can directly answer whether "Null B's
   crossing is migrating toward a stable continuum location" is even the
   right description, independent of and prior to asking whether the same
   pattern shows up at Null A — R15's own addendum was written precisely
   because two points cannot distinguish genuine convergence from a
   persistent recipe-level artifact; four points, for the first time, can
   start to.

3. **Backfill `netd_row()` into item 2's Step 1/Step 2 (§3, above), and run
   a bounded scan for any other T28 cell since exp-094 where a `_full`/
   NETD-surfacing function was called but its output was not persisted
   under any disclaimer at all** (the narrower, un-disclaimered sibling of
   the R16 shape this cycle's own Step 1/2 instantiate). Both are cheap,
   deterministic, zero-new-FDTD closing items directly inside this seat's
   own charter, and the second closes a real audit gap: R16's own bounded
   historical scans (exp-094, exp-097) checked for "disclaimer present,
   field absent" specifically — none has ever checked for "field computed,
   never disclaimed or persisted at all," the shape this cycle's own Step
   1/2 show is possible without tripping R16's own literal text.
