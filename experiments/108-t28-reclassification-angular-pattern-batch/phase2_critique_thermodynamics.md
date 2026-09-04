# PHASE 2 — THERMODYNAMICS CRITIQUE · Panel Iteration 85 (exp-108)

## Steel-man

The N/A ruling is correct, and I can now confirm it with a number instead
of by omission. Exp-107's own committed `results.json` (`item3_rows`)
already ran real `mixed_length_scale_regime`/`netd_disposition` calls for
the exact fixedabs-vs-selfsim split the Tier-0 patch reclassifies. I
propagated that divergence through my own chain myself: the actual
absorbed-watts gap between the two families is 30.9%/46.3% (r=156/312) —
*larger* than the cited 12.31%/17.96% `sigma_abs` figure, because
`p_abs_w` scales as `sigma_ext²·ratio` (iso_xsec_sq), not `sigma_ext·ratio`
— yet both families still read UNDETECTABLE with margin ≥117× below the
0.020 K NETD floor at both r. The reclassification is thermally inert.
Items i–iii (scattered-pattern shape, box-placement noise, numerator floor)
touch scattered power and field-noise floors, not the absorbed-power
partition — genuinely outside my charter this cycle, correctly so.

## Sharpest attack

§3/§6 assert thermal N/A "confirmed structurally" but the document never
looks at the one place my charter actually collides with its headline
action: exp-107's own `item3_rows` already computed real `p_abs_w`/`dt_ss_K`
for the identical fixedabs/selfsim split Item 1 reclassifies
THREE-WAY-AMBIGUOUS. I checked it myself (not hand-typed, R4): the real
absorbed-watts divergence is 30.9%/46.3%, *larger* than the `sigma_abs`
figure being reclassified, because `p_abs_w` is quadratic in `sigma_ext`.
The conclusion (N/A) survives — but the proposal reaches it by never
looking, not by checking, exactly the R8 shape ("unverified independence
argument filed as non-blocking"). It also never mentions that exp-106/107's
own `DISCLAIMER` construction calls `thermo_sidecar.netd_disposition`
directly (a real, if dummy-input, call into my module every cycle since
exp-106) — worth naming, not silently reused.

## Verdict

**support-with-changes**

## Flip condition (optional)

Add one Tier-0-cost sentence to §6 Idealizations, sourced to exp-107's own
`item3_rows`, stating explicitly: "the `p_abs_frac_diff` divergence being
reclassified this cycle corresponds to a 30.9%/46.3% real absorbed-watts
gap between the fixedabs/selfsim families (larger than the cited
`sigma_abs`-ratio figure); both remain UNDETECTABLE, margin ≥117×, per
exp-107's own committed thermal sidecar rows — THERMO confirms N/A with a
number, not by omission." Had my own recomputation instead shown either
family crossing into MARGINAL/DETECTABLE territory, I would oppose outright
until that was surfaced as a live finding, since the "no physics claim
moves" framing would then be false.
