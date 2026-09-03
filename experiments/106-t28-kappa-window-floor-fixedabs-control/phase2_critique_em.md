# PHASE 2 — CRITIQUE · Panel Iteration 83 · Seat: ELECTROMAGNETISM
## exp-106 candidate — "Floor-Gating, Settling, Risk-Propagation, and the Fixed-Absolute-Thickness Control for `kappa_window`"

*Blind to other seats' current-cycle critiques, per PANEL.md. Verified
directly against `phase1_proposal.md`, `experiments/105-t28-kappa-scale-
bridge/run.py` and `NOTES.md`, `experiments/052-fixed-absolute-thickness-
shell/design_geometry.py`, and `lab/materials.py::graded_black_shell`/
`lab/sections.py::radial_absorbed_power` before writing this.*

## T1 / passivity-reciprocity-causality bookkeeping — clean, correctly N/A

No new σ/ε/μ physics. Item 4's control varies only `R_CORE`/`sigma_max`
at fixed `r_out`, reusing exp-052's own already-audited, already-passive
`graded_black_shell` construction verbatim — `sigma_max_fixedabs=0.5`
and every self-similar `sigma_max=0.5/κ` stay strictly positive, no gain
introduced. `graded_black_shell`'s ramp `d=clip((r_out-rr)/thickness,0,1)`
is expressed in a normalized shell coordinate, so its SHAPE is invariant
to absolute thickness — meaning `tau_shell = sigma_max·thickness` really
is a shape-constant-consistent optical-depth proxy across both families,
not just a nominal label. T1 is correctly N/A.

## `p3_trusted` (§4) — the reasoning is honestly stated but reuses the
## wrong diagnostic for the wrong measurement

The proposal is right that `nyquist_margin(312)=1.234` is a fixed
geometric property, so `p3_trusted` is structurally forced False — and,
credit due, this is disclosed explicitly rather than smuggled. But the
deeper problem is upstream of that: `nyquist_margin`/`predicted_ripple_
period` (`run.py::geom()`) was derived to answer one specific question —
does `DENSE_PITCH=2` alias the ripple sampled at discrete `dense_x`
points along a line? — for the point/wide channels. `kappa_window` is not
sampled at `dense_x` at all; `window_stats()` is a **spatial mean over a
fixed 100×40=4,000-cell box**. A box integral of a spatially-periodic
near-field ripple is a low-pass filter on exactly the spatial frequency
`DENSE_PITCH`-aliasing concerns — if anything it suppresses the aliasing
risk the Nyquist tier was built to flag, it doesn't inherit it unchanged.
Applying `nyquist_trust_tier(g312["nyquist_margin"])` to gate a
box-averaged statistic, with the identical ≥2.0 TRUSTED threshold built
for point-sampling, is an unargued transplant of one channel's resolution
diagnostic onto a physically different one. This doesn't make
`p3_trusted=False` *wrong* — it may still be the right conservative
call — but the "symmetric to `p4_156_trusted`" framing overstates how
apples-to-apples the two gates actually are.

## Steel-man (139 words)

Item 3 is real, load-bearing self-correction: my own prior-cycle finding
(exp-105 Phase 5) — that P3's headline number carries P4's identical
MARGINAL-tier r=312 risk with no equivalent gate — is closed in the
cheapest possible way, by literal structural analogy to code already
running (`p4_156_trusted`), not a new instrument. Pre-registering
`p3_trusted=False` as a *predicted*, falsifiable-in-principle outcome
(not asserted as a conclusion) is exactly right R3 discipline: the
settling leg still runs and scores in full, so a genuine surprise
(settling FAIL, independent of the Nyquist tier) remains visible rather
than being hidden behind the forced-False headline. Item 1's decision to
persist full per-cell arrays rather than a lossy summary is the correct
call given `window_stats()`'s own history of silently discarding exactly
the data a later cycle (this one) needed. The floor-gate reuses
`floor_gate()` verbatim — no new statistic invented.

## Sharpest attack (147 words)

Item 4's own falsifiable bands treat `shape_ratio_fixedabs` as
discriminating exactly two hypotheses — geometric z/z_R vs. growing
electrical thickness — but a real energy-budget asymmetry between the
families is never checked. Self-similar's `R_CORE/R_COAT` ratio is
pinned at T9's validated 0.385 at *every* r (30/78 by construction).
Fixed-abs reaches 108/156=0.692 at r=156 and 264/312=0.846 at r=312 —
both far past 0.385, the *only* ratio this program has ever verified the
PEC core is "energetically incidental" at (`design_geometry.py`'s own
comment, citing T9). exp-052's own Fix 3 required exactly this check
(`sections.radial_absorbed_power`) before trusting a construction above
0.385 — never invoked here. A thinner coating in front of a much larger
hard PEC disk can raise specular/diffracted core-reflection into the
forward window independent of any electrical-thickness or z/z_R effect.
A `shape_ratio_fixedabs≤8.0` reading could be core-reflection leakage,
not reduced attenuation — the two-hypothesis framing doesn't rule this
out, and no absorbed/reflected/transmitted ledger is proposed to
distinguish them.

## Verdict: **support-with-changes**

## Flip condition

Add one `sections.radial_absorbed_power` ledger call (reusing exp-028's
already-validated instrument, zero new mechanism) on the fixed-abs
family at r=156 and r=312 — the two points where its own
`R_CORE/R_COAT` ratio (0.692, 0.846) exceeds T9's validated 0.385 anchor
for the first time on this channel — confirming or refuting whether the
core stays energetically incidental at these new ratios before
`shape_ratio_fixedabs`'s two-hypothesis bands are trusted as
discriminating. Absent that, item 4's CONFIRMS/REFUTES bands should be
reported as three-way ambiguous (thickness law vs. core-reflection vs.
both) rather than a clean binary.
