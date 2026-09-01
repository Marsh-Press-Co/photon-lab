# Phase 2 Critique — THERMODYNAMICS

## Steel-man (≤150 words)

The proposal threads the sidecar's own established scope correctly. Tier 1
item 1(c) extends T9/R14's already-validated `ratio_abs_ext` flatness
(<0.1%, exp-087) to the full pooled census — the right zero-cost
energy-partition check to run before any new FDTD spend, and a genuine,
appropriately modest extension rather than a fresh claim. Idealization 63
explicitly discloses that `frac_p_abs` and `delta_scene` share the same
four-call variance rather than being independent confirmations — exactly
the energy-bookkeeping caution this seat exists to enforce, stated
unprompted rather than left for a critic to find. Tier 2 Leg B's own
extraction design is architecturally sound: `beam_behind_t28`/
`observer_record_t28` are pulled from captures "already needed for
`cell_metrics_r4`" at zero marginal `sim.run()` cost — the sidecar's own
ΔT/NETD chain rides along for free rather than driving new spend, which is
the correct posture for a post-run analytic layer.

## Sharpest attack (≤150 words)

`cell_metrics_r4` (reused verbatim per §2) unconditionally computes the
full thermo dict — `sigma_ext_cells`, `ratio_abs_ext_raw`, `p_abs_w`,
`dt_ss_full_K`, `netd_classification`
(`experiments/094-.../run.py:335-345`) — for every cell it processes.
Leg B's 16 calls feed exactly 8 such cells (`C40_R4`/`G40_R4` × 4 angles),
forming 4 pairs shaped precisely for `netd_row()`
(`experiments/093-.../run.py:185-196`), which §2 also lists as reused.
Yet neither Leg B's own procedure, §4's Predictions table, nor §5's new
Idealizations (62–66) commits to calling `netd_row()` or reporting
ΔT/NETD for these 16 points — the identical "computed but never
extracted into the report" shape R16 exists to close, one cycle after
THERMODYNAMICS' own Iteration-76 self-review (LOGBOOK 6688–6691) found its
charter instrument "silently omitted from Result/Learned" on this exact
sub-thread. §1 defers "THERMODYNAMICS' own persistence-gap backfills" to
Tier 3, declared out of scope — deferring the fix while this cycle
manufactures a fresh instance of the same unextracted data.

## Verdict

**support-with-changes**

## Parameter change that would flip my verdict

Add one line to Tier 2 Leg B: call `netd_row()` on all 4 `(C40_R4,
G40_R4)` pairs produced by the new 16 calls and persist the result in
`results.json`, disclaimed per the module's own EXPRESSIBILITY CONTRACT
(post-run analytic, not an FDTD output) and per `netd_disposition`'s own
NETD≠human-perceptual-threshold disclaimer. With that commitment stated,
I support the design as filed.
