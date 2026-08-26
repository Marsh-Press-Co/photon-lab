# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 51 · exp-074

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (PANEL.md: sub-wavelength
structure; what could physically realize the proposed optical behavior; owns
the realizability bound — published/plausible/unobtainium-with-parameters).
Blind to the other six seats' current-cycle critiques.*

---

## Independent verification performed

Re-ran `desk_check_pricing.py` unmodified: output is byte-identical to the
committed `desk_check_pricing_results.json` (CHECK0 `worst_rel_err=0.00e+00`,
all per-pair `cond5`/`cond9`/`VIF_Rq`/`z_ols`/`lev_ratio`/`L(fringe)` figures
match). Diffed the re-implemented `_amp_phase_at`/`carrier_fit`/
`design_matrix` against exp-073's actual committed `run.py` line-by-line —
formulas are identical (the `curvature` kwarg, unused here, is the only
difference). Independently confirmed the `θ` grids for `C40`(exp-069),
`C60`/`C70`(exp-071) are bit-identical (36.0–42.0°, 31 pts, matching `g0a`).
Recomputed `z_joint(optimistic)` at 51° from baseline `z_ols`/`SE_inflation`
by hand — matches the reported `[2.55, 4.10]`. Traced the cited `cond=529`/
`36.6×`/`L(1.9608°)≈26.8` figures to their actual source paragraphs
(`exp-072/phase5_review_em.md` §6 item 2, `phase5_review_quantum.md` §3) —
correctly attributed.

## Steel-man (≤150 words)

This is the cleanest instance of my seat's own discipline I've seen in the
T28 thread. `ABSORB` is stated as a non-material boundary-condition
parameter twice, explicitly (Idealization 2, §3), and §3's T1 statement
doesn't merely assert innocence — it names exactly what isn't touched (no
`ε(ω)`, no S-parameter, no passivity comparison), which is the harder,
checkable form of the same claim. Every headline number is independently
reproducible: I reran the script and it matches to machine precision.
Converting two informal, hand-typed Phase-5 numbers (`cond≈529`, `L(T)`)
into committed code, verified against all four pairs instead of one, and
tied to the design's own already-established leverage mechanism
(`mean diag(M5)=(n−p)/n`), is real progress — a five-cycle-old qualitative
claim ("non-identifiable") becomes a falsifiable, zero-cost, decisively
negative quantitative bound. The formal-retirement language is scoped to
"this estimator on this substrate," not to any claim about real materials.

## Sharpest attack (≤150 words)

§6 stakes the differential/two-tone method's last life on "exactly one more
properly-priced attempt" at ~51°, costed as "≈45 new FDTD calls for a
two-config extension, cf. EM's exp-072 §6.2 costing." That citation doesn't
hold up. EM's §6.2 only ever priced 40 calls, for a *46°* extension (20 new
points/config × 2 configs). Applying EM's own arithmetic to 51°: 45 new
points per config (42→51 at 0.2° step) × 2 configs = **~90 calls**, not 45 —
"new points per config" has been conflated with "total calls." Worse: §2e/§5's
own pricing tables score **all four pairs** (C40-C60, C60-C70, C70-C80,
C40-C80), which needs all **four** `ABSORB` configs extended, not two — the
real cost of the test this proposal itself specifies is closer to **~180
calls**, a 4× understatement. This is precisely the geometry-build costing
check my seat owns (cf. G40/`PAD`'s own corrected 62–93→31 figure, itself a
MATERIALS finding) — a proposal titled "price the window" should not
mis-price its own follow-on.

## Verdict: **support-with-changes**

The CLOSURE-CONFIRM finding for the current 36°–42° window is independently
verified, decisive, and correctly disclaims any realizability implication —
I support formally retiring the differential/two-tone-fit route in this
exact window. The realizability-bound duty is correctly held in abeyance
here (§3's explicit "Checkpoint-criterion-2 candidacy: none" is right — no
mechanism or medium is proposed, so my charter has nothing to bound this
cycle). The one substantive defect is the widened-window forward-cost
citation (above), which should be corrected — stating explicitly whether
Phase 3 means a 2-config (~90-call) preliminary check or the full 4-config
(~180-call) build actually needed to score all four pairs — before it
anchors a "one more attempt, no further deferral" decision rule that a
future cycle will be held to.

## Single parameter change that would flip my verdict to full support

Replace §6's "≈45 new FDTD calls for a two-config extension" with the
corrected, scope-explicit figure (~90 calls if only C40/C80 is re-extended
as a preliminary check; ~180 calls if all four configs are extended to
actually populate the four-pair test this proposal's own bands are built
around) — with that fixed, I'd move to unqualified support.
