# PHASE 2 — CRITIQUE · THERMODYNAMICS · exp-090 ("Floor-Frac Threshold Fit")

## Independent verification performed before writing this critique

I did not take any of the proposal's numbers on faith. From raw
`results.json` primitives (exp-083/087/088/089), I independently:

- Recomputed `RMS[frac_contrast]` over exp-083's own committed 31-point
  window directly from `per_theta[*]["delta_scene"]`/`["C40_C"]`:
  **1.9174375118374476×10⁻³**, giving `FLOOR = 1.91744×10⁻⁴` — bit-exact
  to the proposal's cited value.
- Recomputed all 7 `frac_contrast`/`margin`/`ratio_k` triples from
  exp-087/088/089's own `results.json` fields — bit-exact match to
  Table 1, confirming the perfect rank separation (AUC=1.0) and the
  exact zone `[1.4764, 2.1709]`.
- Re-implemented Firth's bias-reduced logistic regression from scratch
  (Newton–Raphson on the modified score, closed-form hat matrix) on
  `log₁₀(margin)`: **converges** to `(β₀,β₁)=(1.7806,−5.6315)`,
  `m₅₀=2.0710` — inside the zone, matching the proposal's disclosed
  informal figure (≈2.07) to 4 s.f. A naive (unpenalized) MLE on the
  identical data diverges (`|β|` runs into the hundreds under
  Nelder–Mead before hitting its iteration/tolerance floor) — P1/P4 both
  independently confirmed, not merely restated.
- Re-ran the 7-fold LOO jackknife myself: the zone edges move exactly as
  predicted (lower edge 1.4764→1.3095 only when 40.2° is held out; upper
  edge 2.1709→3.8793 only when 37.2° is held out) — P5 confirmed
  bit-exact.

Every load-bearing statistical claim in this proposal reproduces. My
critique is about scope, not arithmetic.

## Steel-man (≤150 words)

This is disciplined use of the panel's own machinery, not a re-tune
dressed up as rigor. It correctly diagnoses why an ordinary MLE is the
wrong tool at a perfectly-separated n=7 (I confirmed the divergence
myself) and answers Red Team's actual ask — a graduated caution zone —
with an assumption-light order statistic first, a properly-penalized fit
as a corroborating second opinion, and an exhaustive (not resampled)
permutation test and jackknife sized honestly to n=7's own resolution
limits. It correctly declines to admit `frac_p_abs` as a regressor,
citing the exact circularity R13's floor gate was built to avoid, and
correctly treats R14's numerator hazard and R13's denominator hazard as
distinct, non-competing questions rather than conflating them. Idealization
7 scopes constraint-3/NETD out cleanly and does not reopen
`REALIZABILITY_MEMO.md` — the T28 desk-cycle discipline this program has
enforced since exp-069 is intact here.

## Sharpest attack (≤150 words)

The caution zone is framed purely as a trust label on `ratio_k`, but it
will function, in practice, as a sampling-priority signal for the
already-queued next energy-interception instrument — the Tier-1
individual-`σ_abs(θ)` build this program's own Iteration-66 ranking says
is "doubly motivated" by exactly this fit. By construction, `margin` is
small precisely where `delta_scene` is near a zero — which is precisely
where *my own* R14 finding says the `σ_ext(θ)` config-differential term
(the physical quantity a σ_abs build exists to resolve) is doing its
most active work. A future build that treats "CAUTION"/sub-zone angles as
second-class evidence, to avoid `ratio_k` noise, would systematically
under-sample the exact neighborhoods where the still-open (PARTIAL, not
ruled out) energy-contrast coupling question from exp-087 is most
diagnostic — the opposite of what a denser energy-ledger characterization
needs. Nothing in §§6–7 names this risk; only NETD/constraint-3 scope is
disclaimed, not this forward sampling-bias interaction.

## Verdict: support-with-changes

## Parameter change that would flip my verdict to unconditional support

Add one sentence to §7 (or a ninth Idealization) stating explicitly that
the caution zone governs trust in `ratio_k`'s *classification label* only
and must not be used to deprioritize or exclude CAUTION-zone/sub-zone
angles from any future denser `σ_abs(θ)`/energy-interception sampling
design — if anything, those angles should be *oversampled* there, since
they are where R14's own established `σ_ext(θ)` differential signal
concentrates. Absent that disclosure, a future Tier-1 build inheriting
this zone uncritically risks quietly starving the exact measurement this
program's own energy-interception thread most needs next.
