# PHASE 2 — CRITIQUE · THERMODYNAMICS · exp-091 ("R3 Resolution & Denser Recheck")

## Verification performed before writing this critique

Traced the absorbed-power chain this cycle exercises, from primitives:
`p_abs_w = ts.absorbed_power_established_ratio(IRR_CENTRAL_W_CM2,
sigma_ext_cells, DX_M, ratio_abs_ext_clamped)["p_abs_w"]`
(`experiments/087-.../run.py`), i.e. `p_abs_w = I_incident · (sigma_ext_cells
· DX_M)² · ratio_abs_ext`, with `IRR_CENTRAL_W_CM2 = 6.584362139917695e-06`
a fixed constant (unaffected by `cpl`). Confirmed §2a's `L_GEOMETRIC_M`
identity (2.34µm held exactly across cpl=20→30 by the R3 rescale's own
construction) and confirmed via §2c's call table that the STEPS=6300
settling spot-check (rows 25–28) runs **both** "empty" and "article" scenes
— i.e. it does exercise the same `widths()`/Poynting-box field data that
feeds `sigma_ext_cells → p_abs_w`, not only the ambient `C_empty` channel.

## Steel-man (≤150 words)

The energy-accounting scaffold is sound where it matters: `p_abs_w`'s only
resolution-sensitive input is `sigma_ext_cells` (a measured box-ledger
quantity); `IRR_CENTRAL_W_CM2` is fixed and `L_GEOMETRIC_M` is held
identical across cpl by construction (§2a), so a finer grid cannot silently
rescale the absorbing area — only genuinely shift the measured extinction
width, which this program's own box-ledger track record (T9/T10/T11: ~6.5%
spread under cpl refinement, judged flat) bounds as predictable, not
open-ended. The STEPS=6300 spot-check is a thermodynamically legitimate
settling probe for the absorbed-power leg specifically, not just a
relabeled ambient check: it runs "article" scenes too, so it exercises the
identical field data `sigma_ext`/`p_abs_w` are extracted from, sharing one
settling time-constant with the channel it's nominally scoped to. The
R14(a) smoothness gate, extended to cpl=30 for the first time, is a
reasonable minimum floor.

## Sharpest attack (≤150 words)

Nowhere does this design test `frac_p_abs`'s own cross-resolution value
match. (a)/(b) score `frac_contrast`/`delta_scene`/`ratio_k` against
cpl=20 values with CONFIRM/REFUTE bands; §4(d)'s "R14(a)-style" check only
verifies `p_abs_w(C40_R3,θ)`/`p_abs_w(G40_R3,θ)` are smooth *across angle*
at cpl=30 alone and directionally consistent with the native trend —
never whether `frac_p_abs(θ,cpl=30)` reproduces `frac_p_abs(θ,cpl=20)`
within any stated tolerance. Since `ratio_k` depends on both halves
equally, and R14 exists precisely because `frac_p_abs` is a
subtractive-cancellation construction that already produced a spurious
non-monotonic dip from ordinary *angular* sampling density alone (38.4°,
not resolution) — with the swing traced, by my own Iteration-65 finding,
into `σ_ext(θ)`'s config-differential term, exactly the quantity a finer
grid could shift differently between C40_R3/G40_R3 — leaving this half
completely unchecked while touting the other half's resolution
robustness is asymmetric. The 40.2°-only settling spot-check compounds
this: it was chosen for ambient-crossing proximity, not because 40.2° is
`frac_p_abs`'s own worst case (R14's founding dip sat at 38.4°) — nothing
here bounds 37.2°/41.4°'s absorbed-power settling or resolution stability
at all.

## Verdict: support-with-changes

## Parameter change that would flip my verdict to unconditional support

Add `frac_p_abs(θ,cpl=30)` vs `frac_p_abs(θ,cpl=20)` as a co-equal PRIMARY
prediction at all three angles, reusing (a)'s own `[0.3,3.0]` CONFIRM /
`[0.1,10]` REFUTE band structure — zero marginal FDTD cost, since
`p_abs_w` is already computed at both resolutions this cycle from the
already-budgeted 28 calls. Absent that, THERMODYNAMICS' own numerator
receives no resolution-robustness scrutiny of the kind the ambient
channel's numbers get, even though `ratio_k`'s classification rests on it
exactly as much.
