# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 63 · exp-086

*Fresh context, blind to all other seats' current-cycle Phase-5 reviews.
Read in full: PANEL.md; LOGBOOK.md RULED OUT (R1–R11, esp. R6–R11) and the
complete T28 live-thread entry (lines 426–4117, Iterations 46–62); the full
exp-086 record (`phase1_proposal.md`, all five Phase-2 critiques including
my own, `phase2_redteam_audit.md`, `phase3_synthesis.md`, all Phase-4
scripts/results, `NOTES.md`); and `experiments/077-.../pad_round_trip_
model.py` line-by-line, both `free_period_with_widening` and
`free_period_with_widening_quiet`, plus `experiments/078-.../
y_wall_prescreen.py`'s own copy.*

## 0. Charter applicability

**The realizability bound does not engage this cycle** — same finding as
my own Phase-2 critique and exp-085's own Phase-5 review: zero
permittivity/admittance/reflectance parameters anywhere in the repair or
the re-score. I apply my seat's rigor to independent re-derivation of the
cycle's own two headline numeric claims instead, as instructed.

## 1. The fix itself: verified real and correct, line-by-line, not merely claimed

Read `pad_round_trip_model.py::free_period_with_widening` (lines 399–440),
`::free_period_with_widening_quiet` (lines 367–396), and
`y_wall_prescreen.py::free_period_with_widening` (lines 322–378) directly.
All three now carry the identical `for...else` shape: a genuine interior
optimum still wins and `break`s as before (unchanged); if the loop runs to
completion without ever breaking (every stage `at_boundary`), the `else`
clause fires and resets `chosen` to the **last** stage's own record
(`last_rec` / `out_list[-1]` — the widest stage, since stages are
appended/evaluated in narrow→wide order), tagged
`converged=False, no_interior_optimum=True`. This is the correct,
algebraically sufficient detection condition R11 specifies, applied
identically at all three sites — confirmed by my own read, not accepted
from the proposal's paraphrase or Red Team's own re-derivation.

## 2. Independent re-derivation — Method C re-score

Loaded `phase4_rescore_results.json` directly and recomputed, myself, from
`method_c_rescore.sub_results` (not from `NOTES.md`'s prose):

```
boundary set (not converged): {45.0, 59.0, 61.0, 63.0, 71.0, 73.0} — 6/37
recovered (converged ∧ p_local_corrected≤6.0° ∧ r2_local≥0.30): 21/37 = 0.5675675...
```

**Confirmed exactly**, bit-for-bit, matching NOTES.md's cited `21/37=0.5676`
and the boundary set cited in `phase3_synthesis.md`. This is now the
**fourth** independent computation to land on this figure (Phase 1's own
arithmetic, Red Team's from-scratch reimplementation, the automated
`phase4_rescore.py` pipeline, and this review), each via a different route.
Also independently re-verified the Spearman stride-phase table
(`spearman_stride_phases` in the same JSON) reproduces the frozen
prediction's three figures exactly (ρ=0.857/p=0.024 at phase 5°;
0.429/0.354 and 0.536/0.236 at phases 7°/9°) and the prior-citation audit
(`phase4_prior_citation_audit_results.json`) finds exactly the two
already-known-inert instances (exp-078, exp-079), nothing new.

## 3. Independent spot-check — the controlled null-calibration comparison (the load-bearing task)

This is the claim I raised the audit-coverage gap against at this cycle's
own Phase 2, and the one instructed to actually re-run, not trust from
JSON. I wrote a **fresh, from-scratch reimplementation** (not a copy of
`phase4_null_calibration_controlled_comparison.py`) of the pre-R11 buggy
`free_period_with_widening_quiet` logic, derived from my own line-by-line
read of the current (fixed) source with the `else` clause removed, and ran
it against the actual **imported, live, committed** corrected function, at
the same N=3000/seed=7, same `thetas`/`sigma` (both loaded independently
from `pad_round_trip_results.json`, matching the committed script's own
data source).

**Result, run twice (once for headline stats, once with a per-trial diff
trace):**

| Statistic | My OLD-BUGGY (fresh reimpl.) | My CORRECTED (live import) | Committed JSON |
|---|---|---|---|
| `max_r2_over_trials` | 0.5179691995509128 | 0.5179691995509128 | 0.5179691995509128 (both) |
| `p_r2_ge_070` | 0.0 | 0.0 | 0.0 (both) |
| boundary-pin firing rate | 201/3000 = 6.70% | 201/3000 = 6.70% | 6.70% (Red Team's cited figure) |

**Bit-identical, independently confirmed.** This is not a re-run of the
committed script — it is a second, independently-written implementation
that reaches the identical floating-point value, the strongest form of
confirmation this program's own R4/R6 reproduction standard asks for.

**A genuine new finding, not in NOTES.md or the committed JSON**: I traced
*why* the effect is negligible, not just *that* it is. Of the 201 trials
where every stage boundary-pins, only **10** show ANY difference in
`r_squared` between the old (stage-1/narrowest) and corrected
(stage-2/widest) return value — the other 191 boundary-pinned trials
report the *same* R² from both stages to full float precision, because for
pure-noise curves the `[1,4]°` and `[1,15]°` search windows both converge
to the same low-`p` edge fit. Of the 10 that do differ, the largest value
on either side (old or new) is 0.269 — nowhere near the 0.518 maximum,
which is set entirely by a genuinely-converged (non-boundary) trial. This
confirms the "negligible effect" conclusion by a second, independent
mechanism (not just "boundary trials don't set the max," which the
committed record already states, but "most boundary trials aren't even
corrected to a different value in the first place") — strengthens, not
merely reproduces, the committed claim.

**Also independently checked** (my own addition, not asked for but
load-bearing for the Director's own Phase-3 "clarifying finding" under fix
2): re-read `pad_round_trip_results.json::verdict_pad` directly.
`period_refute=True` **and** `shape_refute=True` both hold for the
`pair_pad` REFUTE citation — the Director's framing ("driven by
`shape_r_squared_*`... untouched by this bug") is correct in substance but
incomplete: `period_refute` is *also* independently true here, and I
confirmed both the real and model `test_a_pair_pad` fits land at an
interior optimum (`at_boundary: False` for both), not a boundary-pinned
value — so this citation is doubly, not singly, unaffected by the R11 bug.
Worth stating more precisely in any future citation of this finding, not a
correction to the verdict.

**Also independently verified** (closing a gap in my own read of the
audit's scope): the prior-citation audit script scans experiments
"077–085" (18 files, matching `files_scanned` in its own results JSON), a
narrower window than `phase1_proposal.md`'s own "full 069–085 board"
framing. Its docstring asserts "069–076... grep-confirmed: zero
`at_boundary` occurrences." I independently grepped all 13 committed JSON
files across experiments 069–076 myself: **zero `at_boundary` occurrences,
confirmed** — the scope narrowing is justified, not a silent gap.

## 4. Assessment of the six mandatory fixes and Phase 2/3 process

All six of Red Team's Phase-2 mandatory fixes were adopted in full at
Phase 3, zero overrides, and each is independently verified present and
correct in the Phase-4 output: three pre-registered stride phases reported
together (not cherry-picked); the quiet-variant fix extended beyond mere
audit to an actual source-level repair, with the controlled comparison
resolving MATERIALS' own flip parameter; the energy-interception exemption
sentence present in NOTES.md; the instrument-reliability caveat carried
into every place `classification_a`/`NOT STABLY PERIODIC` is reported;
`ss_tot_full`/`ptp` persisted per sub-window (confirmed present in the
JSON); the title corrected. This is the cleanest process outcome this
sub-thread has shown across several cycles — no defect this review found
required escalation.

## Verdict: **PARTIAL**

The repair is real, correctly applied at all three sites, and now the
subject of four independent confirmations of its two headline numeric
consequences (Method C re-score; the null-calibration controlled
comparison). The audit-coverage gap I raised at this cycle's own Phase 2
is genuinely closed, not merely disclosed: Red Team's 6.70% firing-rate
finding is confirmed exact by a second, from-scratch implementation, and
the follow-on question it left open ("does this materially move the cited
statistics") is answered — negligibly, for a mechanistic reason now
independently traced two ways. This is instrument-repair/record-hygiene
work; Checkpoint criterion 2 is correctly N/A (matches every T28 desk
cycle since exp-069) and nothing here rules in or out a mechanism class —
`classification_a=NOT STABLY PERIODIC` is a statement about instrument
reliability, carried with its caveat intact, not a phenomenon finding.
No new defect rises to Checkpoint-criterion-4 weight in this review.

## Ranked top candidate next-steps (my own; none re-propose RULED OUT R1–R11)

1. **Finish the full-scale (N=60,001) `null_calibration_appendix` re-run
   on the corrected `free_period_with_widening_quiet` and formally update
   exp-077's own cited headline statistics.** My own independent spot-check
   confirms the fix's differential effect is negligible and mechanistically
   well-understood at N=3000 (bit-identical `max_r2_over_trials`; only
   10/201 boundary trials even change value) — this materially de-risks
   the full run, converting it from "might move a settled REFUTE" to "cheap
   confirmation that closes a still-officially-open Tier-2 item," making it
   the single highest-value-per-cost item left on the board.
2. **Resolve PHOTONICS' disclosed-but-unresolved grazing-incidence
   model-validity question** — whether `edge_diffraction_c_empty_corrected`
   remains inside its own valid near-field/Kirchhoff regime at the
   sub-windows where `ptp` grows 5,444×–6,631× (θc≳57–69°) — before any
   future cycle treats the corrected 21/37 "recovered" set as physically
   meaningful. This bears directly on the recovered set's own upper edge
   (θc=57° is the sole recovered point beyond θc=43°) and is cheap
   (a regime/dimensionless-parameter check against the model's own stated
   validity bounds, zero new FDTD).
3. **Name the energy-interception cross-check's now-four-cycle
   deferral/exemption streak (083/084/085/086) explicitly as approaching
   the R8/R10-style escalation shape** on the record, so the next
   scene-bearing T28 cycle either runs it or states an explicit reason —
   a governance note, not a new rule, matching this program's own practice
   of naming a pattern before it becomes a firing.
