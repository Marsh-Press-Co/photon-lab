# PHASE 2 — CRITIQUE (THERMODYNAMICS) · Panel Iteration 66 · exp-089

*Fresh context, blind to all other seats' current-cycle critiques. Read
PANEL.md, LOGBOOK.md RULED OUT (R1–R14, in full) and LIVE THREADS/T28
(Iterations 58–65, both CHECKPOINT entries, in full), this cycle's
`phase1_proposal.md` in full, and — for house-style calibration only —
exp-088's `phase2_critique_thermodynamics.md`/`phase5_review_thermodynamics.md`
and `lab/thermo_sidecar.py` source. Independently re-derived every
load-bearing numeric claim below from primitives, not restated from the
proposal's own prose (R4/R9 discipline).*

## Independent verification performed

- **§4's R13 margin arithmetic reproduces exactly.** Pulled
  `experiments/083-.../results.json::per_theta` directly for 37.2°/40.2°/
  41.4° and recomputed `frac_contrast=|delta_scene|/|C40_C|`:
  `4.162655×10⁻⁴`, `2.830881×10⁻⁴`, `2.510967×10⁻⁴` — bit-exact to the
  proposal's cited values. Dividing by the cited `FLOOR=1.91744×10⁻⁴`
  reproduces the margins exactly: **2.1709×, 1.4764×, 1.3095×** (proposal:
  2.17×, 1.48×, 1.31×). No defect found here.
- **The "zero marginal FDTD cost" claim for a thermo-sidecar extension is
  independently checkable against source, and holds.** Read
  `lab/thermo_sidecar.py::absorbed_power_established_ratio` (line 124),
  `mixed_length_scale_regime` (333), `netd_disposition` (778) directly:
  all three are pure post-hoc functions of already-in-hand quantities
  (`p_abs_w`, geometry/material constants reused verbatim from exp-087/088)
  — nothing in that chain requires a new FDTD call. This is the same fact
  THERMODYNAMICS' own exp-088 Phase-2 critique used to force Q6/Q7 into
  that cycle at zero marginal cost.
- **§4(a)'s attribution check.** exp-089 states R14(a)'s parent-quantity
  smoothness check "mirrors THERMODYNAMICS' exp-088 Phase-5 decomposition."
  Re-reading R14's own LOGBOOK text: the parent-curve monotonicity finding
  is credited to "QUANTUM OPTICS' own Phase-5 self-review... re-derived
  ... by Red Team's Phase-5 final audit"; THERMODYNAMICS' own contribution
  was a *different*, downstream thing — the `ratio_abs_ext` T9-flatness
  argument that the swing is forced into `σ_ext(θ)`'s config-differential
  term specifically. The proposal conflates the two.

## Steel-man (≤150 words)

The design is genuinely economical: one 12-call set answers both the
node census and the gap census by construction, reusing exp-088's pipeline
verbatim (zero new statistical machinery). §4's floor-gate margins are
honestly disclosed as the thinnest this sub-thread has ever sent to FDTD
(1.31–2.17×, vs. 3.88–8.02× previously) rather than smoothed into a
comfortable-looking PASS row — the right instinct after R13/R14. R14(b)/(c)
are engaged with real numbers, not waved off: the shared-config-pair risk
is named and a period-fit explicitly declined rather than silently skipped,
and the tightest interior gap (1.4° vs. a [1.42°,1.475°] half-period bound)
is flagged as a near-exact clearance, not buried in an aggregate pass. Every
number I re-derived from primitives reproduces exactly.

## Sharpest attack (≤150 words)

`frac_p_abs`/`ratio_k` at the three new angles cannot exist without
computing `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` — i.e., without running
the full thermo-sidecar chain that also produces the NETD classification
and the T9-anchor (`ratio_abs_ext`) cross-check, established at exp-088
(itself THERMODYNAMICS' own Phase-2 push, adopted Phase 3, delivered as
Q6/Q7) as a *zero-marginal-cost* extension once `p_abs_w` is in hand. This
proposal's §7 machinery inventory never names `thermo_sidecar`, and §6 has
no Q6/Q7-equivalent pre-registered prediction — the free check exp-088
established as house practice is silently absent here, at exactly the
angles (1.31–1.48× floor margin) where a T9-anchor sanity check is most
valuable as an independent corroboration that nothing near a denominator
node is contaminating the ratio. Separately, Idealization 8's NETD banner
lives only in §5; §6 (the Predictions section the Iteration-65 CHECKPOINT
explicitly named) carries zero inline occurrence — a fifth instance of the
disclaimer-erosion shape that has fired Checkpoint criterion 4 four times
running, this time before Phase 4 even runs.

## Verdict: support-with-changes

## Flip-to-support parameter

Add the NETD/T9-anchor extension (reusing `p_abs_w` already required for
`frac_p_abs`) at all three new angles as a pre-registered prediction
(mirroring exp-088's Q6/Q7 exactly — `dt_ss_full_K`/`netd_classification`/
`ratio_abs_ext` vs. the 0.51 T9 anchor), and inline-restate the
Idealization 8/9 banner verbatim inside §6 itself, not only §5. Both are
zero marginal FDTD cost. Secondary, non-blocking: replace §4(a)'s vague
"individually smooth/monotonic" with a concrete, code-executable criterion
(e.g., non-decrease of `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` across the
combined 8-point sorted angle list, within each point's own `box_dev`
noise floor) and state explicitly whether that check runs in `run.py`
(Phase 4, automatable) or is left to Phase-5 prose judgment — as written,
"mandatory Phase-4 check" names no threshold and no owner.
