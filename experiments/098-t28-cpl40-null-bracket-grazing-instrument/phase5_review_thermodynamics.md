# Phase 5 Review — THERMODYNAMICS (blind)

**Cycle:** Panel Iteration 75 (exp-098, T28 house-discipline/validation), EM lead.

## 1. Independent spot-verification

**(a) netd_row() 10-key coverage — exhaustive, not sampled.** I wrote a script
against `results.json` that collected every report row across `item_i.{A,B,C}`
(12 rows: 3 nulls × 4 angles) and `item_ii.combined_report` (6 rows: 4 new +
2 reused from exp-095), and checked all 10 `NETD_ROW_KEYS`
(`p_abs_w_c/g`, `dt_ss_full_K_c/g`, `netd_classification_c/g`,
`sigma_ext_cells_c/g`, `ratio_abs_ext_raw_c/g`) against every one.

Result: **18/18 rows carry all 10 keys, 0 missing.** All 36 `netd_classification_c/g`
values read `UNDETECTABLE` — no exception this cycle, matching every prior
R4-family cycle on file. `dt_ss_full_K` ranges 4.55e-5–5.37e-5 K,
`p_abs_w` ranges 2.77e-12–3.27e-12 W across all 18 rows — consistent
magnitudes, no outliers, no negative `p_abs_w` anywhere (0 of 36 leg-values
negative — the real thermodynamic no-gain check, distinct from GP1 below).

**But: NOTES.md's own coverage claim is miscounted.** The Result section says
the assert "held for all **64** real-FDTD report rows (item (i) 48 + item (ii)
16...)". This conflates **FDTD call count** (64 = 16 angle/config points × 2
legs × 2 empty/article conditions) with **report-row count**. There are only
**16 new report rows** this cycle (12 + 4), each one `netd_row()` call bundling
both legs via `_c`/`_g` suffixes — plus 2 reused rows independently re-checked
at import time (`run.py:118-120`) = 18 total, not 64. I confirmed this by
reading `run.py`'s own final aggregation assert (lines 464-470): it iterates
over `item_i[l]["report"].values()` (12) plus `item_ii["combined_report"]`
minus the 2 reused keys (4) = **16**, matching my independent count exactly.
The underlying PASS is real (I verified all 18 exhaustively, not just the 16
the code's own final assert re-checks) — but the number cited to justify it
is wrong. This is the same species of error as this cycle's own disclosed
"32 vs 64 calls" arithmetic miscount, this time inside the very sentence
boasting R16 "enforced... in full, this time."

**(b) GP2′'s "continuously... entire upper half" claim — checked against the
raw curve, not the summary fields.** NOTES.md's Result reads: "GP2′ ... flags
MARGINAL **continuously** across θ=50.5°–89.5° — the ENTIRE upper half of the
sweep, not a narrow band." I pulled `item_v.gp2_curve` directly (120 points)
and checked every point in [50.5°, 89.5°] (79 points): **9 of them are VALID,
not MARGINAL** — 52.0°, 52.5°, 53.0°, 53.5°, 54.0°, 54.5°, 60.5°, 61.0°, 69.5°,
with ratios dipping as low as 0.44× before climbing back above 10×. `flagged_band`
is computed in `run.py` as `(min(flagged), max(flagged))` over the union of
MARGINAL+INVALID thetas — an **envelope**, not a claim of continuity; the code
never asserts contiguity. "Continuously" overstates what the data shows: the
region is intermittently MARGINAL with real gaps, not a solid band. Doesn't
change the qualitative finding (upper-sweep degradation overlapping the known
θc≈59°–73° blow-up, peak 235.396× at θ=66.0° — this specific number I
independently recomputed via `max()` over the curve and it matches exactly)
but the prose oversells the shape of the curve.

**(c) Independent recomputation of all four headline crossing values** (Null
A ≈36.770358°, Null B ≈39.921519°, Null C = None/NO-SIGN-CHANGE, item (ii)
≈38.252279°) by re-implementing the linear-interpolation `find_sign_change`
logic from scratch against the raw `delta_scene` values in `results.json`:
**all four reproduce bit-exactly.** GP1's `min(C(θ)) = −0.4405` also
reproduces exactly from the raw curve. No arithmetic defect found in any of
these headline numbers themselves.

## 2. `run.py`'s assert placement — control-flow read, not just presence

Read the full `main()` top to bottom: it is a single linear function, one
`json.dump` call (line 498), no `try`/`except` anywhere in the file (grepped
to confirm), no early-return, no partial-write path. The netd_row coverage
gate is actually **two-layered**, stronger than the single check my own
Phase-2 critique asked for:

1. **Per-row, inline** (`run_r4_batch`, lines 179-181): fires immediately
   after each row dict is built, before it's even returned to `main()` —
   this covers item (i)'s three `run_r4_batch` calls and item (ii)'s one call
   independently, at construction time, not in aggregate.
2. **Final aggregate** (lines 464-470): re-checks the same 16 new rows
   collected across `item_i`/`item_ii` immediately before `json.dump`.
3. **Import-time** (line 120): checks the 2 *reused* exp-095 rows before
   `main()` is ever called.

All three run before the one and only file write, in every actual code path
today. **Residual structural risk, not a live defect:** this correctness
depends on the file staying a single linear script. Nothing in the file
*mechanically* prevents a future refactor from adding a second `json.dump`
(e.g., an incremental "checkpoint after item (i) in case item (ii) crashes"
pattern) ahead of the final assert — the guarantee is "read top to bottom and
verify," not an independent wrapper (e.g., a `write_results(data)` function
that itself asserts before writing, callable from exactly one place). That's
a cheap, generalizable hardening for a future cycle, not a fix this cycle
needs.

**Bonus finding, outside my charter but caught while reading this control
flow (flagging per shared verify-before-claim discipline):** NOTES.md's
Idealization 47 claims the reused 38.49°/38.69° points were "re-verified this
cycle by running that same [registration-readback] gate against their exact
(family, theta, cpl, config_key) tuple, not merely asserted equivalent by
reference." I grepped `run.py` for every call site of `run_checks_1234_and_7`
— it is only ever invoked via `registration_preflight(angles)`, which is only
ever called with `angles_sorted` (item i's 4 new angles per null) or
`NEW_ANGLES_II` (item ii's 4 *new* angles). **38.49 and 38.69 never appear as
arguments to `run_checks_1234_and_7` anywhere in this file.** The only check
actually run against the reused rows is the netd-key-coverage assert at line
120 (import time) — a real but different check than what Idealization 47
claims. Phase 1's own original draft of this idealization (`phase1_proposal.md`
line 228-232) said the opposite — that the gate was explicitly *not*
re-verified for these two points — and the final NOTES.md version silently
strengthened that claim to "re-verified" without the code actually gaining
that call. Worth another seat's (or Red Team's) confirmation since gate
verification isn't my charter, but it's a concrete, independently-checkable
overclaim I'd want on record.

## 3. GP1 and the absorbed-power ledger

No inconsistency to flag, and this is a real answer, not a dodge: GP1
(`C(θ)=weber(bo,bf) ≥ −1`) is a passivity bound on `dg048.edge_diffraction_c_empty_corrected`
— a closed-form, lossless, source-driven field superposition with **no**
absorbing article and **no** `p_abs_w`/`thermo` channel anywhere in its
computation (confirmed again this cycle: `eval_raw`/`FastEval` never touch
`cell_metrics_r4`/`pair_metrics_full`). It is not comparable to the 64-call
absorbed-power ledger — cross-checking them would be the category error I
flagged last cycle (conflating "no negative-flux amplitude artifact in a
lossless model" with "power in = absorbed + scattered in an actual absorber").

The *actual* thermodynamic passivity check this cycle is the one I ran in
§1(a): zero of the 36 real `p_abs_w_c/g` leg-values are negative, and this is
already enforced by `run_r4_batch`'s own `nonneg_pass` assert (line 166-169,
`sigma_abs_nonneg`) — a genuine, already-gated "no gain" result on the real
FDTD side, structurally independent of GP1's closed-form-side "no gain"
result. Both hold; neither needs to reference the other; the document doesn't
claim otherwise. One gap persists from last cycle: my Phase-2 ask for a
one-sentence GP1 disclaimer ("amplitude-passivity check, silent on absorbed
power, not an energy-conservation check") was flagged as non-blocking and did
not land verbatim in NOTES.md this cycle either (Idealization 52 gestures at
it — "self-consistency and internal-amplitude checks... do not themselves
re-derive... the model's underlying physics" — but never says the word
"energy" or "absorbed power"). Still non-blocking; flagging again since it's
now two cycles unaddressed and costs one sentence.

## 4. Steel-man and sharpest finding

**Steel-man:** The netd_row() enforcement genuinely graduated from prose to a
hard, triple-layered build-time gate this cycle, exactly as my Phase-2
critique demanded, and it is correctly wired for every real-FDTD row that
exists — I verified this exhaustively (18/18), not by sampling. The R16
compliance record for this specific mechanism is now clean two cycles
running, and the design (per-row inline + aggregate + import-time reused-row
check) exceeds what was asked for.

**Sharpest finding:** the cycle's own boast about that exact achievement —
"the mandatory build-time assert held for all **64** real-FDTD report
rows... enforced, not merely disclaimed (R16, in full, this time)" — miscounts
its own row count by conflating it with the FDTD call count, in the same
document that already disclosed one arithmetic miscount (32 vs. 64 calls) as
a program-wide "Learned" lesson about nobody owning call-count arithmetic
verification. The irony: the fix for that exact blind spot was proposed in
this same cycle's own "Next" queue (item 4, "assign call-count arithmetic
verification as an explicit named duty") — and a closely-related miscount
(row-count vs. call-count, this time) slipped through the same review pipeline
into the very paragraph announcing the fix. Non-load-bearing to any physics
finding (the underlying coverage genuinely is 100%), but it's a second,
independent instance of the identical failure class inside one cycle, which
raises rather than lowers the priority of that "Next" item.

## 5. Verdict

**CONCUR-WITH-GAPS.**

- The physics/coverage substance is sound and I could not break it: netd_row
  coverage is genuinely 100% (18/18, exhaustive), all classifications
  UNDETECTABLE (no drift from precedent), all four headline crossing values
  and GP1/GP2′ peak numbers reproduce bit-exactly under independent
  recomputation, and the absorbed-power ledger shows zero negative values
  (real passivity, correctly ungated to GP1's separate closed-form passivity).
- The gaps are entirely in the Result section's *prose precision*, not its
  underlying data: the "64 rows" mislabeling (§1a), the "continuously...
  entire upper half" overstatement of GP2′'s actually-intermittent MARGINAL
  band (§1b), and the unsubstantiated "re-verified" claim in Idealization 47
  (§2, outside my charter but caught in the process). None of these change a
  verdict or a PASS/FAIL classification; all are independently, cheaply
  checkable against `results.json`/`run.py` the same way I checked them.

## 6. My ranked top-3 candidate next directions

1. **Assign call-count/row-count arithmetic verification as a named duty**
   (already queued as this cycle's own Next item 4) — promote it from
   "candidate" to committed, given a second independent instance of the same
   failure class (row-count vs. call-count) surfaced in this very cycle's
   Result section, not just the already-disclosed one. A cheap, mechanical
   fix: a single assert comparing `len(all_netd_rows)` against a stated
   prediction, the same pattern that already caught the 32-vs-64 call miscount.
2. **Null C re-test at a wider/re-centered bracket** (this cycle's own Next
   item 1) — genuinely the most physics-load-bearing open thread: item (ii)
   just demonstrated a ±0.5°-scale bracket can miss a real crossing if not
   correctly centered, and Null C's NO-SIGN-CHANGE this cycle used exactly
   that bracket size/centering with no wider check yet.
3. **Confirm or correct Idealization 47's "re-verified" claim** (§2 above) —
   either add the missing `run_checks_1234_and_7` calls for
   theta=38.49/38.69 so the claim becomes true, or correct the text back
   toward Phase 1's own original (accurate) framing. Small, cheap, and
   directly a verify-before-claim compliance item this program's own culture
   statement names explicitly.
