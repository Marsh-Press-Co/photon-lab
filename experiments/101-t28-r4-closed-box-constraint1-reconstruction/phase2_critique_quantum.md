# Phase-2 Critique — QUANTUM OPTICS seat, Panel Iteration 78 (exp-101)

Fresh sub-agent, no knowledge of any other seat's critique this cycle. All
figures below were independently recomputed from committed source (not taken
on the proposal's word): `pool_rows()` re-executed directly against
`experiments/100-.../run.py` in this repo; `R4_CONFIGS`/`R4_BASE_ABSORB`/
`box_for_r4`/`BOX_CLEARANCE_B_R4` traced through
`experiments/069-.../design_geometry.py`; the absorbing-boundary ramp
mechanics read from `lab/fdtd2d.py` (applied symmetrically to all four
domain edges, confirmed by reading the `d[...]=ramp` lines, not assumed).

## 1. Steel-man (≤150 words)

From this seat's own expressibility contract — mechanisms must enter the
bench only as effective classical parameters or be struck — this proposal is
maximally clean: §3 states T1 escape route N/A and it is true by
construction. Nothing needs translating into σ(I), σ(x,t), dispersive ε(ω),
or gain, because no new physics is asserted; the article, geometry, and
`sigma_max` are byte-identical to the already-committed R4 config. Zero
surface for a fuzzy "quantum" narrative to sneak past Red Team as untestable
— the exact failure mode this seat polices on mechanism cycles.
Independently re-executing `pool_rows()` (75 rows, matching exp-100's stored
count) confirms the angle re-selection to the digit: θ=39.200000 (R4,
exp-095, `-3.149521e-3`) is the true pool-wide largest magnitude,
θ=42.960901 (R4, exp-099, `+2.778079e-3`) second, and exp-100's own
`40.960901` is genuinely only 10th (`+2.471869e-3`) — survives independent
recomputation exactly, no restatement defect (R4/R20) found.

## 2. Sharpest attack (≤150 words) — verified, not speculative

§2.5's due-diligence gate (`box_dev_scat_downstream ≤ 0.12`, reusing
`XI_TOL`) is the exact R17 pattern its founding case warns about: reusing a
bound without checking the largest comparable shift on file. That shift
exists and is far larger: exp-003 documents `box_dev` reaching 2–6
(200–600%) — a "domain-sizing bug, not physics" — under a required ≥60-cell
clearance from the absorbing boundary (`ABSORB=40` there). I recomputed,
from committed constants (`R4_BASE_NX=720`, `R4_BASE_OBJ_X=340`,
`R4_BASE_ABSORB=80`, `BOX_CLEARANCE_B_R4=48`), that `BOX_B` for `C40_R4`
places its low-x face — the *downstream* face `sigma_scat_downstream` is
built from — at **x0=136, only 56 cells from the absorb layer's inner edge
(80)**: below exp-003's 60-cell threshold, and R4's absorb depth is double
exp-003's, so the true margin needed is likely larger. `BOX_A` (the
reported measurement) is safe at 80 cells; only the QA cross-check is
exposed. A spurious fail would be mislabeled genuine `back_frac` fragility,
not a domain artifact — the R20 mislabeling shape.

## 3. Verdict

**Support-with-changes.** The Tier-0 fix itself (closed-box reconstruction
via already-gated `sc.widths()`, corrected angle set, zero `lab/` diff) is
sound and independently verified; the flaw is confined to one new
due-diligence gate, not the core deliverable.

## 4. Parameter change that would flip to unconditional support

Before Phase 4 runs: widen `BOX_CLEARANCE_B_R4` (or grow `C40_R4`'s domain
padding for this check only) so `BOX_B`'s low-x face clears ≥90–100 cells
from the absorb boundary for `C40_R4`, matching the margin `G40_R4` already
has by construction (136 cells) — and pre-register that a
`box_dev_scat_downstream` failure at insufficient clearance is read as a
domain-sizing artifact, not a `back_frac`-fragility finding, per exp-003's
own precedent.
