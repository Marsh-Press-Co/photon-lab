# PHASE 5 REVIEW — THERMODYNAMICS (blind) · exp-095 · Panel Iteration 72

*Fresh sub-agent, THERMODYNAMICS charter: where absorbed energy goes; owns
the per-proposal energy sidecar (absorbed power → temperature rise →
emission band → detectability), expressed as a post-run analytic
calculation, labeled as such. Read in full: PANEL.md; LOGBOOK.md (RULED
OUT R1–R16 — R16 in full, its own founding case one cycle ago; LIVE
THREADS T1–T28, T28's complete Iteration-46→71 history, T5); the complete
exp-095 record (`phase1_proposal.md`, all five Phase-2 critiques including
my own prior-cycle critique, `phase2_redteam_audit.md`, `NOTES.md`,
`run.py`, `run_output.txt`, `results.json`,
`gate5_wiring_defect_verification_result.json`). Did not read any other
seat's Phase-5 review. Every number below was pulled directly from
`results.json`/`run.py` this session, not taken from prose on faith.*

## Verdict: **CONCUR, NO R16 GAP FOUND — a genuinely clean cycle on my
charter's own founding failure mode**

## 0. The single most consequential check: does R16 fire a third time?

**No. Direct inspection of `results.json` finds full compliance for every
Rank that actually ran.** Table below is pulled field-by-field, not
summarized from `NOTES.md`'s prose claim:

| Rank | θ | `p_abs_w_c` | `p_abs_w_g` | `dt_ss_full_K_c` | `dt_ss_full_K_g` | `netd_classification_c/g` |
|---|---|---|---|---|---|---|
| 1a | 39.2° | 2.9625e-12 | 2.9714e-12 | 4.8671e-05 | 4.8817e-05 | UNDETECTABLE/UNDETECTABLE |
| 1a | 39.4° | 2.9853e-12 | 2.9820e-12 | 4.9046e-05 | 4.8991e-05 | UNDETECTABLE/UNDETECTABLE |
| 1c | 38.49° | 2.9072e-12 | 2.9279e-12 | 4.7762e-05 | 4.8102e-05 | UNDETECTABLE/UNDETECTABLE |
| 1c | 38.69° | 2.9200e-12 | 2.9442e-12 | 4.7972e-05 | 4.8371e-05 | UNDETECTABLE/UNDETECTABLE |
| 4 | 38.4° (corrected) | 2.9094e-12 | 2.9216e-12 | 4.7798e-05 | 4.7999e-05 | UNDETECTABLE/UNDETECTABLE |

All ten values present, all `sigma_ext_cells_c/g` and `ratio_abs_ext_raw_c/g`
present alongside them — the full `netd_row()` schema, at every cell this
cycle's Phase-4 actually spent an FDTD call on.

Traced this to source in `run.py`, not just to the JSON: `netd_row(pm)` is
splatted directly into `rank1a_report[th]` (line 564), `rank1c_report[th]`
(line 632), and the Rank-4 output dict (`netd_row_r4`, computed line 720,
merged line 1288) — in every case at the exact point the report dict is
constructed, with no intervening filter, allow-list, or "informational
subset" step between computation and the final `out = dict(...)` that gets
`json.dump`-ed. `netd_row()` itself is not reinvented — `netd_row =
exp094.netd_row` (line 212), which is itself exp-093's original committed
function, imported transitively, never re-typed. This is the literal
"successor" convention R16's own text names, applied correctly.

**Ranks 2 and 3 never ran** (`rank2.skipped=true`, `rank3.skipped=true`,
reason `"Rank 1 combined go/no-go gate did not PROCEED"`) — so `cell_metrics_r5`
was never *exercised* this cycle, meaning it cannot be scored a pass or fail
on persistence in the way Rank 1/4 can. But the task asks whether it is
nonetheless correctly present/callable for a future cycle, since Rank 2 is
exactly the fresh-code shape (`box_for_rN`/`ref_for_rN`/`_run_sim_rN_sigma`,
hand-copied per family) that produced R16's founding gap. Read
`cell_metrics_r5` directly (`run.py:350-399`): it calls
`ts.absorbed_power_established_ratio` → `ts.mixed_length_scale_regime` →
`ts.netd_disposition`, builds a `thermo` dict carrying
`sigma_ext_cells`/`ratio_abs_ext_raw`/`p_abs_w`/`dt_ss_full_K`/
`netd_classification` — line-for-line structurally identical to
`cell_metrics_r4` (`experiments/094-.../run.py:305-342`), substituting only
`R5`-scoped constants (`box_for_r5`, `PEC_R_R5`, `dg.R5_R_OUT`, `DX_M_R5`,
`L_GEOMETRIC_M_R5`, `dg.R5_W_OBJ`, `dg.R5_GUARD_OUT`, `dg.R5_W_FLANK`). Every
downstream call site that *would* have run this cycle — Rank 2a
(`pm_r5_7000`/`pm_r5_10500`, `netd_row_r2a_7000/10500` merged into the
output dict at lines 1159–1161), Rank 2b and Rank 2b-native (`netd_row(pm)`
splatted at lines 867 and 933) — is written with the merge already wired
into the same diff that defines the function, exactly matching Red Team's
own mandatory-fix #7 and THERMODYNAMICS' own Phase-2 critique text verbatim.
**If Rank 1 had PASSED and Rank 2 had actually run, R16 compliance would
have held on the evidence in the code as committed — this is not a case of
a fix that only exists in prose.** This closes the loop my own Phase-2
critique opened: the gap I flagged (no named `cell_metrics_r5` in the
Phase-1 draft) was fixed exactly as I asked, in the same diff, and the fix
demonstrably reached `run.py` rather than stopping at `NOTES.md`.

**No `_full`-style computation anywhere in this cycle's actually-executed
code path (Rank 1a/1c/4 — the only Ranks that ran) computes a NETD
byproduct that fails to reach `results.json`.** I checked every call site
that invokes `pair_metrics_full` or `cell_metrics_r4`/`cell_metrics_full`
in the executed branches; each is immediately followed by a `netd_row()`
merge before the value is ever assigned to a report dict. **The standing
forward-elevating clause (a third disclaimer-without-persistence occurrence
auto-fires Checkpoint criterion 4) does not fire — there is no second-or-
later occurrence to name.** This cycle is the clean discharge, not a third
strike.

## 1. Thermal/energy angle on Rank 1c's own FAIL

Rank 1c failed because both bracket points read the **same sign**
(38.49°: `delta_scene=-1.5168e-3`; 38.69°: `delta_scene=-2.5385e-3` — both
negative, both `floor_pass=True`) rather than straddling zero around the
established `cpl=20` null at 38.590°. My own charter's question: does the
energy channel show any companion anomaly, or does the anomaly live purely
in the coherent `delta_scene` channel?

Comparing `p_abs_w_c` across all five Rank-1/Rank-4 points measured this
cycle (2.9072e-12 → 2.9200e-12 → 2.9625e-12 → 2.9853e-12 → 2.9094e-12,
spanning 38.49°–39.4° plus 38.4°): the full spread is **≈2.7%** of the
central value, and the G/C ratio at every single point sits within
0.30%–0.83% of unity (`p_abs_w_g/p_abs_w_c` = 1.0071 at 38.49°, 1.0083 at
38.69°, 1.0030 at 39.2°, 0.9989 at 39.4°, 1.0042 at 38.4°-corrected) — all
comfortably inside the pre-registered 1–5% informational band.
`ratio_abs_ext_raw` sits at 0.5130–0.5140 throughout, within ~0.8% of the
T9 0.51 anchor at every point, and every `dt_ss_full_K` value sits in the
same narrow 4.78e-5–4.90e-5 K band, UNDETECTABLE by a comfortable margin
against the 8.6 mK NETD floor. **Meanwhile the coherent channel, over the
identical five points, ranges from -1.52e-3 to -3.15e-3 at Rank 1 (a ~2×
spread) and then collapses to -2.94e-6 with `floor_pass=False` at Rank 4's
corrected-sigma leg — three orders of magnitude smaller and unresolvable.**
This is exactly the established R13/R14 pattern this program has now
confirmed at every resolution point it has ever measured (`cpl`∈{20,30,40},
now including this cycle's `cpl=40` node-bracket window): the oscillatory/
sign-sensitive structure lives entirely in `σ_ext(θ)`'s coherent-differential
channel, never in the absorption/scattering energy partition. Rank 1c's
FAIL is not accompanied by, and gives no evidence of, any energy-channel
anomaly — it is a purely coherent-channel finding, consistent with every
prior instance on this sub-thread.

## 2. Broader adversarial read — is Rank 1c's FAIL actually evidence of a
registration defect, or a known-migration artifact this cycle's own design
didn't rule out?

This sits outside my charter's narrow energy question, but the task asks
for a broader read and I found something worth naming plainly, independent
of anything already in Red Team's Phase-2 audit (which attacked the
*control-angle* choice for Rank 1a, not the *bracket premise* for Rank 1c).

Rank 1c's entire validity rests on treating 38.590° (the second of four
`cpl=20` crossings) as a fixed, resolution-stable reference point, bracketed
at only ±0.1°/±0.2° span. But this program's own already-filed data shows
known crossing migration between `cpl=20` and `cpl=30` **in this exact
window** of 0.19°–0.38° (exp-092 `results.json::rank1.crossing_report`:
`shift_vs_cpl20_lower=-0.1935813`, `shift_vs_cpl20_upper=0.3201659`,
`shift_vs_cpl20_upper_second=0.3767516`) — magnitudes that would, on their
own, already carry a null clean outside a ±0.1° bracket. Critically, I
checked whether 38.590° itself (unlike the other three `cpl=20` crossings)
has ever been tracked into `cpl=30`: `exp-092`'s own `crossing_report` names
only a `lower`/`upper`/`upper-second` triplet (40.072°, 41.781°, 41.838°) —
the 41.6°–42.0° window this whole sub-thread is built around. **38.590°'s
own `cpl=30` fate was never measured; there is no prior data establishing
whether it drifts by 0°, by the ~0.2°–0.4° this program has already
documented elsewhere, or by more, before this cycle's own `cpl=40` bracket
test.** Given that, a same-sign FAIL at ±0.1°/±0.2° is at least as
consistent with "the null migrated outside the bracket by an amount
comparable to migrations already on record for this window" as with "the
null vanished / a registration defect exists" — and the two explanations
carry very different implications (the first is business-as-usual grid
refinement; the second is the integrity finding NOTES.md flags it as).
Idealization 28 half-names this ("tests presence... not exact location")
but does not connect it to the concrete, already-filed 0.2°–0.4° migration
scale that makes a too-narrow bracket the more parsimonious explanation.
This does not overturn Rank 1c's FAIL as reported (it is reported honestly,
un-oversold, exactly as designed), but it does mean "FAIL" should not yet
be read as evidence weighted toward a registration/wiring defect over an
ordinary, previously-observed migration — the combined gate's conservative
HALT was still the right call either way.

## Steel-man (my own discipline)

The energy-channel bookkeeping this cycle is the most complete this
sub-thread has produced: every one of the ten article-bearing cells that
actually ran carries its full NETD sidecar, wired at construction time
rather than retrofitted post-audit, and Rank 2a's settling gate additionally
computes a dedicated `p_abs_w`-specific three-way band (mandatory fix #8) —
the first time this cycle-family has scored energy-channel settling
independently of the coherent channel's own settling criterion, rather than
assuming one implies the other. That check never ran (Rank 1 didn't PROCEED)
but the machinery is there, tested at zero marginal cost the moment Rank 2
does run.

## Sharpest attack

Rank 1c's own conclusion ("the established node appears to have vanished
from this window in the `R4` family") is stated as the FAIL branch's
label in both `NOTES.md` and the go/no-go criterion text, but the bracket
that produced it (±0.1°/±0.2°) was never checked against this program's own
already-filed evidence that nulls in this exact angular neighborhood
migrate by comparable or larger amounts between resolutions — an omission
that costs nothing to fix (it is a desk check against already-committed
`results.json` data) and would have changed how confidently the FAIL is
framed, though not the HALT decision itself.

## Ranked top candidate next step

1. **(Cheapest, most directly responsive to my own §2 finding.)** Before
   trusting Rank 1c's FAIL as a registration-defect candidate, run a
   zero-FDTD desk check: does 38.590°'s own null, if it migrated by the
   same 0.19°–0.38° this window's other two crossings already showed
   between `cpl=20`→`cpl=30`, land inside or outside a wider bracket (e.g.
   ±0.4°) at `cpl=40`? If a wider bracket would have bracketed a sign
   change, Rank 1c's FAIL is better read as "bracket too narrow for a known
   migration scale," not "node vanished" — a materially different, less
   alarming finding, discoverable from already-filed data alone.
2. A widened-bracket re-run of Rank 1c specifically (not Rank 1a, whose
   PASS is independently sound) at ±0.4°–0.5° around 38.590°, gated on (1)
   suggesting it is worth the ~8 additional calls — this is the one
   remaining ambiguity standing between this cycle's HALT and an actual
   verdict on whether `R4`'s own registration is sound.
3. Only after (1)/(2) resolve: re-open Rank 2/3 (the `cpl=50` third
   resolution point and the sigma-comparability closes) — both are fully
   speced and `cell_metrics_r5`-ready per §0 above, so no redesign is
   needed, only Rank 1's own gate clearing honestly.

## Standing-rule check

No RULED-OUT item (R1–R16) is revisited or contradicted by anything above.
§0 is a direct, evidence-based **non-firing** report on R16's own forward-
elevating clause — I looked specifically for a third disclaimer-without-
persistence occurrence and did not find one; this should be read as
active confirmation the clause does not fire this cycle, not merely silence
on the question. §2 does not propose a new standing rule; it names a
gap in this cycle's own bracket-width justification for Red Team's final
audit to weigh, per this program's convention that a reviewing seat names,
not adjudicates, that question.
