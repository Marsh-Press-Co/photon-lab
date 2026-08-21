# Phase 2 Critique — QUANTUM OPTICS (blind, independent)

**Reviewing:** `experiments/054-heff-length-scale-rederivation/phase1_proposal.md`

## Steel-man

Within Block C's actual implementation the independence claim is exact, not
approximate. exp-045's Host D rate constants (`k_f_on = r * k_r_d`, `k_r_d
=10.0`) come from an exogenous `RATIOS` grid, never derived from `w_on` or
`r_out` — so `n(t)` genuinely carries zero L-dependence in this code path. The
targeted figure, `max_dT_periodic_decoupled_K`, is a pure product
`dt_ss_full * n(t)`, so rescaling `dt_ss_full` by the ON-endpoint's factor
rescales it by exactly that factor — I re-ran `coupled_segment_general`
numerically to check this. It also doesn't hide behind the coupled-vs-
decoupled gap: since `dwell/tau_thermal` is already deep in the quasi-static
limit at both lengths (21x, 194x per Iteration 23), that gap (1.2–3.4%,
conservative) shrinks further, not worse, under the `r_out` correction. The
carry-over is mathematically sound for what it's actually applied to.

## Sharpest attack

The "independence" is the boundary of a disclosed idealization, not a
physical result. `lab/kinetics.py`'s `integrate_two_state` refuses a
time-varying `I_profile` ("k_f is taken as a given constant, not re-derived
from I(t) via microphysics"), and Block C's `k_f` is a bare exogenous ratio,
never built from `sigma_ext`/`w_on`/`r_out`. But Host D *is* T17's σ(I)
mechanism (`dn/dt = k_f(I)(1-n) - k_r*n`) — the class this program exists to
test. The moment a future cycle closes that standing idealization and
re-derives `k_f` from actual absorbed intensity (necessarily normalized
against the same `w_on`-vs-`r_out` cross-section this cycle is correcting),
`n(t)` inherits the length-scale dependence P-054-3 asserts away. The
proposal states the carry-over as an unconditional, permanent fact rather
than one conditioned on a currently-open idealization boundary — no caveat
scopes P-054-3 to "as long as k_f/k_r stay exogenous."

## Verdict

**support-with-changes**

## Parameter change that would flip to plain support

Add one sentence to P-054-3 (or the idealizations list) scoping the
independence claim explicitly: it holds only as long as `k_f`/`k_r` remain
exogenous rate-constant grid parameters rather than being re-derived from
I(t) via the corrected cross-section convention — flagging it as a
scope-bound fact tied to `lab/kinetics.py`'s standing `I_profile`
idealization, not a permanent decoupling of the σ(I) mechanism from L.
