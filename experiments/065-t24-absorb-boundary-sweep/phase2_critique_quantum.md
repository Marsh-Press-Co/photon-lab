# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 42

*Seat charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or
Red Team strikes them. Reviewed blind, independent of any other seat's
Phase-2 critique.*

## 1. Steel-man (≤150 words)

The proposal's T25/T26 scoping claim is verified, not hand-waved. Direct
code inspection confirms `lab/ambient.py::incoherent_sum` only ever combines
separately-run, single-source `Sim` calls (`add_line_source`, one angle per
call, `rel_phase=0.0` default) as real, already-time-averaged flux profiles,
each normalized by its own empty-run flank mean — structurally identical to
the pipeline T25 closed at flux level (Iteration 35, ≤0.7% relative error
against the random-phase-ensemble mean). `lab/phase_lines.py`'s
`rel_phase`/joint-reconstruction machinery — the actual apparatus T26's
artifact requires — is never imported anywhere in this proposal's
`design_geometry.py` or its described `run.py` blocks. So §6 idealization
5's claim ("no coherent joint injection occurs... T26's artifact is
structurally out of scope") is correct on inspection, not merely asserted
past a live risk. This is the right way to close a standing thread against
a new proposal: name the specific missing import, not just wave at the
module name.

## 2. Sharpest attack (≤150 words)

§6 idealization 6 claims matched-angle differencing "cancels the quadrature
phase error to first order" — the load-bearing premise behind P-VIS42-2/6/7
(the headline plus both N9-aggregate deltas) — yet it carries no falsifiable
band and sits in tension with this program's own standing evidence. The desk
propagator is explicitly "boundary-FREE" (`design_geometry.py:32`); it
models nothing about the graded-loss band's own residual reflectivity,
which is coherent with the CW source and can perturb T21's established
edge-diffraction fringe rather than add to it smoothly. T24's own two
already-measured legs show exactly that signature: ABSORB 40→60 moved
`C_empty` by **+0.0070** at one cell and **−0.0022** at another — opposite
sign, not a monotone leakage term. A boundary-induced coherent-phase
perturbation of the fringe is at least as consistent with that data as the
proposal's "additive systematic" framing, and none of §4's nine predictions
distinguishes the two — P-VIS42-2's median/max/Spearman battery cannot.

## 3. Verdict

**Support-with-changes.**

## 4. The parameter change that would flip this to unqualified support

Add one pre-registered, falsifiable test of the "first order" cancellation
premise itself, before P-VIS42-2/6/7 are trusted: a dense (≤0.5°-step) mini
angular sweep of `ΔC_empty(θ) = C_empty(C80,θ) − C_empty(C40,θ)` spanning at
least one full T21 fringe period at 600 nm (the λ T21 found closest to
Nyquist-critical, hence cleanest signal), scored for whether the *delta
itself* oscillates with T21's own predicted period `P(θ)=λ/(A·cosθ)`
(falsifying "clean additive boundary systematic") or stays flat across the
period (confirming first-order cancellation as claimed). Cost is small — one
extra angle block at one λ, on domains already built for Block SWEEP.
Without it, the proposal cannot distinguish a genuine boundary-loss
systematic from a boundary-perturbed coherent interference pattern, and the
distinction is exactly the one that decides whether P-VIS42-2's REFUTE band
("absolute transfer... every near-threshold constraint-3 citation... is
un-decidable") is being triggered by the right physics.

## Additional note, outside the four required items (task-directed)

The τ_center=0.0065 Block ARTICLE disk's self-classification (§3, "static,
linear, time-invariant... not a hysteretic one") correctly discharges this
seat's expressibility contract and T17's standing self-classification
requirement: it is a fixed-σ, non-kinetic dielectric slab with no `k_f`/`k_r`
in play, squarely an ordinary linear classical material — no smuggled
non-classical assumption found anywhere in its construction or its use in
P-VIS42-7.
