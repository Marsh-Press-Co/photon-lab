# PHASE 2 — ELECTROMAGNETISM CRITIQUE · Panel Iteration 85 (exp-108)

## Steel-man

The T1 "N/A throughout" claim survives direct check: nothing in Tiers 0/1
builds, varies, or scores any σ(I)/σ(x,t)/angular-selectivity/sub-threshold
mechanism — `materials.graded_black_shell`/`pec_disk` are reused unchanged,
and `angular_scattered_pattern` is applied as a passive diagnostic on an
already-non-candidate shell, not a new escape-route mechanism; no
constraint-1/2/3/4 verdict is touched. R25/R23 are read correctly — I
re-grepped both registry entries myself: R25's "proposed and ratified…
Iteration 84" language and R23's still-open Iteration-82 scope question
match verbatim. The Tier-0 patch is well specified: I traced `run.py`
753–765/593–596/672–675 myself and confirmed `p_abs_frac_diff`=0.1231/0.1796
and `shape_ratio_fixedabs`=18.2283 exact, still unwired, exactly as claimed.
`sum(pattern)==sigma_scat` is correctly labeled an implementation identity,
not a physical test — matching the function's own docstring verbatim.

## Sharpest attack

Item i's REFUTE gate requires a candidate feature to reproduce "same
location, same sign" at `box_b` — conflating two EM facts. Total flux
through any closed, source-free surface IS box-independent (Poynting),
so ≤0.12 on `sigma_scat`/`sigma_ext` is sound. But the ANGULAR
DISTRIBUTION of that flux is not invariant across radii — the docstring
itself admits a square-path, near-to-mid-field sample, not a far-field
pattern. I verified the separation: `k=r/78` gives `box_a`/`box_b`
margins of `round(32k)`/`round(57k)` cells beyond `R_COAT` — ≈2.5λ apart
at r=156, ≈5λ at r=312 (`CPL_600=20` cells/λ), well inside Fresnel-zone
territory where lobe migration reshapes a passive scatterer's pattern
with zero energy violation. This gate can wrongly discard a real
anisotropy, or pass by coincidence — it doesn't test what §4/§7 claim.
Separately, `ledger_check()`'s `closure` field — the real two-route
energy identity here — is absent from this cycle's plan for a third
straight cycle, never named as a deferral.

## Verdict

**support-with-changes**

## Flip condition (optional)

Replace item i's box-independence bar: keep the integrated
`sum(pattern)==sigma_scat`/`≤0.12` check as the conservation gate, but drop
"same angular location/sign at `box_b`" as the sole arbiter of whether a
feature is trusted. Either (a) require the pattern to converge as a
function of box radius across ≥3 box sizes rather than match at two points
2.5–5λ apart, or (b) relabel a `box_a`-only feature that fails only this
bar as `NEAR-FIELD-RADIUS-DEPENDENT` rather than folding it into a
not-trusted REFUTE-denial — and add `closure` (already computed by
`ledger_check`, zero new FDTD if `sigma_e` is captured alongside the
PEC-cored fields item i already schedules) to the predictions table as a
named check, not a silent omission.
