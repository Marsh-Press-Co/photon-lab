# PHASE 2 — CRITIQUE · Panel Iteration 67 · exp-090 · Seat: MATERIALS & METAMATERIALS

## Steel-man (≤150 words)

For a perfectly-separated n=7 sample, this is disciplined statistics, not
overreach. It correctly diagnoses that ordinary MLE is degenerate here
(driving |β|→∞) rather than quietly reporting a knife-edge boundary as if
it had confidence attached, and it responds with the right tool stack: a
non-parametric order-statistic zone as the assumption-light primary
deliverable Red Team actually asked for, an *exact* permutation test (no
Monte-Carlo/seed dependency at n=7, where that would matter), and Firth's
bias-reduced logistic fit as a corroborating point estimate rather than a
replacement. The regressor choice (`margin`, not θ or `frac_p_abs`) is
argued correctly against a real circularity risk (R13's own gate purpose)
and R14's numerator-hazard class. I independently recomputed every
`frac_contrast`/margin value in Table 1 from the three source
experiments' raw `results.json` and it reproduces bit-exact. The
single-article/single-wavelength scoping (Idealization 3) matches the
house convention this seat itself has pushed in exp-088/089.

## Sharpest attack (≤150 words)

The entire n=7 population this fit rests on — `frac_contrast`, hence
`margin`, hence the caution zone's edges and the permutation test's
AUC=1.0 — has never passed an R3-mandated spatial (`cpl`) resolution
check on this exact channel. This is not a new observation: my own
seat's Phase-5 review of exp-088 named it explicitly ("this channel has
never received an R3-mandated spatial (`cpl`) resolution check, only a
temporal-settling one"), and exp-089's own NOTES.md carried it forward as
"undischarged two cycles running." I grepped exp-090's `phase1_proposal.md`
for "R3" and "resolution" — zero occurrences. It is not named anywhere in
§4's idealizations (1–8) or falsifiable predictions.

This is not a generic small-print gap — it bites exactly where the method
is most load-bearing. The zone's *lower* edge (1.4764) is fixed by 40.2°
and 41.4°, the two points closest to a real, established `delta_scene`
zero-crossing — precisely the regime where Yee-grid staircasing error is
most amplified relative to signal, since a small absolute perturbation to
a near-zero denominator produces a large relative shift in `frac_contrast`
and hence in `margin`. `VALIDATION.md`'s own recorded lesson is that this
bench's λ/20 grid "staircases the tensor" as a matter of course — resolution
sensitivity near a feature is the default expectation here, not an exotic
risk. A `cpl` 20→30 check could plausibly move 40.2° or 41.4°'s margin by
enough to shift the zone's own lower edge, which is also this cycle's own
P5 (LOO jackknife) most fragile prediction (already flagged as moving
under a single held-out point). The proposal presents the zone's edges
as bit-exact, order-statistic facts about seven numbers — they are that,
but the seven numbers themselves carry an acknowledged-elsewhere,
undisclosed-here numerical-convergence gap at exactly the two points that
set the boundary the whole method is built to certify.

## Verdict: support-with-changes

## Parameter that would flip my verdict

Add, as an explicit Idealization/§4 disclosure (not a new FDTD run,
zero-cost to state): "the n=7 `frac_contrast` values have not passed an
R3 spatial-resolution check on this channel; the zone's lower edge in
particular (set by 40.2°/41.4°, the points nearest an established
denominator zero-crossing) is not yet shown resolution-stable, and the
same `cpl` 20→30 check queued at Iteration 66/67 for other reasons would
also discharge this gap for this fit's own load-bearing inputs." With
that one sentence added and the zone/`m₅₀` numbers explicitly labeled
provisional pending it, I would move to support.
