# PHASE 2 — QUANTUM OPTICS CRITIQUE · Panel Iteration 85 (exp-108)

## Steel-man

This is a disciplined governance/instrument cycle that does exactly what
it says: no σ(I)/σ(x,t)/angular-selectivity/sub-threshold mechanism is
proposed, so T1=N/A is correct and my expressibility contract is not
engaged. Every headline number I independently checked reproduces exactly:
`p_abs_frac_diff_156=0.1231`/`_312=0.1796`, `shape_ratio_fixedabs=18.2283`,
`abs_ratio(156)=1.0852`/`(312)=1.8797` all match `results.json` to the
digit; the classification block is verified at lines 753–765 (not
754–765) with `p_abs_frac_diff` genuinely absent from it; the r=312
margin=65 box (`hw=572`, x∈[436,1580]) sits correctly inside `N=2240`'s
`[40,2200]` interior. Critically, `angular_scattered_pattern` (`lab/
sections.py:200`) is pure classical time-averaged Poynting flux
(`Re(E·H*)/2`) from steady-state phasors — the SAME construction
`widths()` already uses — and the proposal never invokes "coherent"
language at all, correctly avoiding this program's loaded T28 usage.
Nothing non-classical is smuggled anywhere.

## Sharpest attack

Item ii's "std across the 6-box family" is presented as a noise-floor
proxy comparable to the T9 anchor spread, but the six margins
{24,32,40,48,57,65}×k are not exchangeable samples — they are an ordered
sequence around the SAME deterministic field snapshot, where the
box-integral necessarily trends with margin as it converges from
near-field toward the asymptotic cross-section. A monotonic or
smoothly-varying trend across margin inflates "std" even with zero
underlying measurement randomness, and a large std would then reflect
convergence *bias*, not "box-placement sensitivity comparable to the
signal" — a materially different physical claim from what the
falsified-if branch asserts, and from what Tier-2 item 1 ("re-derive the
confirms band") is being asked to lean on. This is the same floor-gating
rigor gap QUANTUM already flagged on this exact thread at exp-107 Phase 5
(FLOOR_FRAC unre-derived, "worsens with r" resting on 2 correlated
points) — recurring in a new instrument, uncaught by this document's own
§7 falsification list.

## Verdict

**support-with-changes**

## Flip condition (optional)

Before letting the item-ii std stand in for a noise floor (and before any
future cycle treats it as discharging Tier-2 item 1), report whether the
6-margin sequence is monotonic in margin at both r; if it is, replace the
raw std with a residual-from-fit (e.g. linear or `1/margin` detrend vs.
margin, std of the residual) so a systematic near-field convergence trend
cannot be miscounted as placement noise. This is a reporting/statistics
fix on data already captured — zero new `Sim.run()` calls — so it costs
nothing to add before Phase 3 freezes the interpretation.
