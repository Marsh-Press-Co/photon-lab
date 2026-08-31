# Phase 5 Review — THERMODYNAMICS (blind), Iteration 73 / exp-096

*Seat charter (PANEL.md, verbatim): where absorbed energy goes; always asks
what re-radiates and whether it would be detectable; owns the per-proposal
energy sidecar (post-run analytic calculation, labeled as such, not an
FDTD output). This cycle computes no thermal/NETD quantity — confirmed
independently below — so this review applies the seat's other established
strength per the assignment: bookkeeping/accounting consistency, the same
lens that produced R16.*

## 0. Confirmed scope: no thermal quantity anywhere in this cycle

Walked the full `results.json` tree programmatically for any key matching
`netd`/`therm`/`p_abs`/`temp`: **zero hits.** `run.py` never calls
`cell_metrics_r{3,4,5}` or `netd_row()`, matching the compliance header's
own claim and the Phase-2 self-critique's steel-man. R16 is not engaged —
correctly, not by omission. Confirmed: `git status --short lab/` and
`git diff --stat lab/` against HEAD both empty, matching the Result
section's "zero `lab/` diff" claim.

## 1. Independent re-verification (bit-exact, from primary source)

**Re-ran `run.py` from scratch this session** (fresh process, not trusting
the committed `results.json`): reproduces `registration_gate_outcome:
CLEAN`, `representative_all_clean: True`, `check5.clean: True`,
`check6_all_clean: True`, and the fault-injection triad (positive control
CLEAN; FI-A/B/C all DEFECT-FOUND) bit-exact against the committed file.

**`sim_construction_count` / `representative_results` length (the specific
re-count this assignment asked for):** `results.json`'s own
`sim_construction_count` = `{representative: 16, fault_injection_new: 2,
total: 18}`; `len(representative_results)` = 16, confirmed by direct
count. NOTES.md's Result section states "Total: 18 `Sim` constructions" —
this **matches `results.json` and `run.py`'s own computed field
bit-exact**. On the narrow question asked (does NOTES.md's figure match
what `run.py` computed and `results.json` reports), the answer is **yes,
cleanly** — see §3 below for a deeper finding this narrow check doesn't
surface.

**Desk-bound migration figures, re-derived independently from the original
source files** (`experiments/090/results.json::q8.crossings_deg[2:4]`,
`experiments/092/results.json::rank1.crossing_report`), not from NOTES.md
prose: `0.1935812644838535° / 0.3201659178026546° / 0.3767516353289935°`
— bit-exact against both `results.json`'s `desk_bound.migration_figures_deg`
and NOTES.md's stated `0.193582°/0.320166°/0.376752°`.

**Containment ratios — bit-exact against `results.json`'s own
`desk_bound.containment_ratios`,** independently recomputed (δ/M for all
three δ×three M combinations): ±0.2° → `1.0332/0.6247/0.5309`; ±0.4° →
`2.0663/1.2494/1.0617`; ±0.5° → `2.5829/1.5617/1.3271`, matching both
`results.json` and `run_output.txt` to 4 decimal places.

**`check4_max_abs_diff` figures:** FI-B = `1.6355117919003987` (NOTES.md
states `1.636`, correct rounding); FI-C = `298.6310235614485` (NOTES.md
states `298.6`, correct). Both bit-exact.

**Check 6 line citations (437/445/476/495/511) independently re-verified**
by `grep -n` against the live `experiments/095-.../NOTES.md` file, not
taken on the proposal's word: all five line numbers land on the exact
sentence fragments the check claims. Clean.

**Trust-suite/wall-time claims:** `wall_time_s: 2.175` matches
`run_output.txt` header exactly. Trust-suite "41/41" claim not
independently re-run this review (outside this seat's charter and outside
the specific re-verification list this assignment names); flagged as
unverified-by-me, not disputed.

## 2. R16 self-check (the standing rule this seat's own founding finding
## produced)

R16 governs a disclaimer traveling without the byproduct field it covers
being persisted. Not engaged here — there is no NETD byproduct field of
any kind in this cycle's design or output (§0). No recurrence to report,
and none owed: applying R16's discipline to a cycle that computes no NETD
quantity would be a category error, not a diligence.

## 3. Sharpest finding

**The desk-bound containment-ratio triple in NOTES.md's Result section is
printed in two different, unlabeled orderings across three adjacent
bullets — a real misreading risk, though the underlying numbers are all
individually correct.**

NOTES.md's Result section reads: *"±0.2° insufficient (1.03×/0.62×/0.53×
— barely covers only the smallest figure, misses the other two); ±0.4°
clears all three but at only 1.06× margin against the largest
(`upper_window_2`); ±0.5° gives 1.33×/1.56×/2.58×, the most defensible of
the three candidates examined..."*

The ±0.2° triple (`1.03/0.62/0.53`) is in the canonical
`lower_window/upper_window_1/upper_window_2` order — matching
`results.json` and `run_output.txt`'s own dict order exactly
(`1.0332/0.6247/0.5309`). The ±0.5° triple (`1.33/1.56/2.58`) is **not** —
in canonical order the ±0.5° figures are `2.5829/1.5617/1.3271`
(`lower_window`/`upper_window_1`/`upper_window_2`). `1.33/1.56/2.58` only
reproduces if the three values are read in the *reverse* order
(`upper_window_2`/`upper_window_1`/`lower_window`). I confirmed this
against `run_output.txt`, which always prints the dict in canonical
insertion order and shows `lower_window=2.5829` at ±0.5°, not `1.33`.

Every individual number is bit-exact and correctly rounded — this is not
a data error. But a reader moving from the ±0.2° bullet to the ±0.5°
bullet with no reordering cue would naturally read the first number in
each triple as "the same window," and would come away believing
`lower_window`'s margin at ±0.5° is a thin `1.33×` rather than its actual
comfortable `2.58×` — inverting which of the three migration windows is
best- and worst-covered by the ±0.5° candidate. This is exactly the class
of gap R16 exists to catch generalized to a different artifact (a
presentation/labeling slip rather than a missing-persistence slip): a
correct number, correctly computed, made to communicate the wrong thing
by an inconsistency in how it's presented next to its own sibling figure
two sentences earlier. Non-load-bearing to this cycle's own verdict (the
Predictions section's earlier, single-number framing — "±0.5° gives 1.33×
margin, the most defensible" — already correctly identifies 1.33× as the
*minimum* across all three, i.e. the binding constraint, so the headline
conclusion survives), but worth a same-shift correction: label each
triple explicitly (`lower/upper1/upper2:`) rather than relying on
positional order that silently flips.

## 4. Secondary finding: "18 Sim constructions" measures distinct
## configurations, not actual `Sim()` object instantiations

Instrumented `lab.Sim.__init__` and re-ran `run.py`'s `main()` in-process
this session to count actual constructor invocations, independent of what
`sim_construction_count` reports: **20 `Sim()` objects are actually
constructed**, not 18. The gap traces to fix #5's own "spends zero new
constructions" framing for the positive control and FI-B: both legs call
`run_checks_1234(...)` → `construct_sim(...)` → `Sim(...)` a second time,
with parameters identical to already-built representative points 1 and 4
respectively — they do not literally reuse the Python objects built in the
`main()` loop. "Zero new *constructions*" is accurate only under the
reading "zero new distinct *(family, cpl, θ, config)* combinations added
to the check catalog" — which is what the `18` figure actually counts —
not "zero additional `Sim.__init__` calls," which the field's own name
(`sim_construction_count`) most naturally suggests. This is
non-load-bearing (the 0-FDTD-calls guarantee is untouched either way —
none of the 20 reach `sim.run()` — and the 2.175s wall time already
reflects the true 20-object cost, not an 18-object one, so no downstream
number is actually wrong), but it is a field-name/claim mismatch in
exactly the shape my seat's charter exists to catch: a reported count
that doesn't match what the code that produced it actually did, caught
only by re-instrumenting the code rather than by re-reading the documents
that describe it.

## 5. Verdict

**CONCUR-WITH-GAP(S).**

Every headline number I could independently re-derive — the registration
gate's CLEAN outcome (re-run from scratch, not just re-read), the
fault-injection triad, Check 5/6, the desk-bound migration figures and
containment ratios, `check4_max_abs_diff` — is bit-exact against
`results.json` and, where traceable further, against the original
upstream source files (`experiments/090`, `experiments/092`,
`experiments/095/NOTES.md`). NOTES.md's own "18 total" construction-count
claim matches `results.json`'s own field precisely, on the specific
re-count this assignment named. The two gaps found (§3's triple-ordering
ambiguity, §4's construction-count field-name imprecision) are both
real, both independently verified from source rather than inferred, and
both non-load-bearing to the registration-gate CLEAN verdict, the
fault-injection MUST-catch predictions, or the desk bound's ≥0.5°
recommendation — the reason this is CONCUR-WITH-GAP(S), not DISPUTE.

## 6. Ranked candidate directions for Iteration 74

1. **Execute reconciled queue item 4 — the node-bracketing re-run at
   θ₀≈38.590°, using ≥0.5° single-sided half-width** (this cycle's own
   desk bound, independently re-confirmed bit-exact above): the direct,
   now-unblocked follow-up to exp-095's Rank 1c FAIL. With registration
   ruled CLEAN this cycle (within the stated, correctly-scoped residual
   per Idealization 38), migration is the sole surviving named candidate
   worth testing directly, and this cycle's own arithmetic already pins
   the bracket width needed to trust the result either way.
2. **Execute reconciled queue item 3 — bracket the other three established
   `cpl=20` nulls at `cpl=40` (~24 calls)**: the decisive discriminator
   between a family-wide migration pattern and a feature-specific one, and
   incidentally exercises more of the shared `r{n}_config()` recipe than
   Check 5's single `R4`/`C40` spot-check did (Idealization 39's own
   named residual) — real, if partial, additional coverage of the class
   this cycle could only spot-check.
3. **From this seat: pre-wire NETD-sidecar extraction (`netd_row()`) into
   whichever of items 1/2's `run.py` computes `delta_scene`/`frac_contrast`
   or any `_full` metrics variant, from first commit, per R16** — a
   preventive rather than retrospective application of the standing rule.
   Both queued items resume real FDTD spend on exactly the code path
   (`_run_sim_r{3,4,5}_sigma`-family calls) whose sibling functions have
   twice produced an R16-class gap (exp-092/093, exp-094); wiring the
   sidecar in before the run, not auditing for its absence after, is the
   cheap version of the same fix.
4. **(Deferred, correctly, per unanimous prior seats.)** The `cpl=50`/`R5`
   interior sweep (item 6) should remain unscheduled until items 1/2
   above resolve — reuse the already-built, gate-verified family rather
   than rebuild it.
