# Phase 2 Critique — QUANTUM OPTICS seat, Panel Iteration 79 (exp-102)

Fresh sub-agent. I am the same seat that found the `i_inc`/cosθ
commensurability artifact in exp-101 (Phase-5), so this critique checks the
proposed fix against `lab/sections.py` directly, not against its own prose.

## Steel-man (≤150 words)

The fix correctly generalizes past a naive 1/cosθ patch. Rather than
dividing `i_inc` by cosθ (fragile if the true launch angle drifts from
nominal, or grid dispersion bends the wavefront), `I0_corrected`
reconstructs the local Poynting vector's true Pythagorean magnitude,
`√(Sx²+Sy²)`, from first principles — valid at any effective propagation
angle, not only the nominal θ. Gate C makes the cosθ relationship a
*tested consequence*, not an assumed correction — exactly right. The
primary witness metric `κ(θ)` is designed even more robustly: a same-point
`|Ez|²` ratio that never calls `i_inc` or `sc.widths()` at all, so it is
structurally immune to the artifact rather than merely corrected for it —
the cleanest possible resolution of precondition (a) for the metric that
actually matters. Nothing here imports a non-classical assumption: `κ`,
`Δφ`, and `I0_corrected` are all classical Poynting/field quantities — the
instrument stays fully expressible on a passive, classical article
throughout, satisfying this seat's contract.

## Sharpest attack (≤150 words)

`I0_corrected(θ) = mean_y[√(Sx(y)²+Sy(y)²)]` has an order-of-operations
flaw invisible without checking it against `i_inc`'s own convention: it
averages the per-cell *magnitude*, not the components. By Jensen's
inequality, the mean of a noisy vector's norm is systematically ≥ the norm
of its mean — any residual ripple in the empty-scene reference strip (ABC
leakage, edge-taper residue) biases `I0_corrected` upward, unlike
`i_inc = mean_y(Sx)` itself, a plain linear average that cancels zero-mean
ripple exactly. This is precisely the coherent-vs-incoherent-averaging
distinction this instrument is built to respect for `κ` (hence Prediction
4's point-vs-region check) — yet `I0_corrected`, the one channel Gate C
promotes to a *permanent* gate for every future absolute-intensity
citation, has no equivalent disclosed check. Gate C's blanket 1%
self-consistency tolerance can pass while masking this specific bias
rather than diagnosing it. Fix: `I0_corrected(θ) = √((mean_y Sx)² +
(mean_y Sy)²)` — average components first, mirroring `i_inc`'s own
established convention exactly.

## Verdict: **support-with-changes**

The fix is directionally and structurally correct — it is not the same
class of error as the defect it replaces (this is a genuine vector-
magnitude reconstruction, not another disguised projection), and the
primary witness metric `κ(θ)` sidesteps the artifact entirely rather than
merely correcting for it. The one flaw is a second-order averaging-order
bias in the secondary, non-scored `I0_corrected`/Gate-C channel, not a
repeat of the commensurability defect itself.

## Parameter change that would flip verdict to plain "support"

Replace `I0_corrected(θ) = mean_y sqrt(Sx(y)^2 + Sy(y)^2)` with
`I0_corrected(θ) = sqrt( (mean_y Sx(y))^2 + (mean_y Sy(y))^2 )` in
precondition-(a)'s Fix (§4) — average the component fields first, then
combine, exactly mirroring `i_inc`'s own established linear-mean
convention. Cheap (removes a nonlinearity, not a computation), and closes
the one channel this proposal itself elevates to a permanent gate.

## RULED OUT / Live Thread check

No re-tread found. The proposal's own §"Why nothing here re-treads..."
audit (R1, R5, R13/14, R15, R17, R20/21; T8, T9, T28) is accurate as far as
this seat's own domain can verify: no mechanism/material parameter is
touched (R1 correctly N/A), the amplitude-floor discipline (R13/14
lineage) is applied proactively even though not structurally mandated, and
the citations of this seat's own prior finding — `Q_ext≈1.54–1.56`
corrected, `sigma_scat_downstream` cannot distinguish shadow from cloak-
like refilling by phase — match `phase5_review_quantum.md` exactly, not a
restated or drifted figure. No R9/R20-shaped citation defect found in this
proposal's own treatment of my seat's prior finding.
