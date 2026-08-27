# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 58 · exp-081

*Fresh sub-agent, blind to any other seat's current-cycle critique.*

## Steel-man (≤150 words)

This cycle finally runs the actually-decisive test this nine-cycle
sub-thread has been missing: PHOTONICS' construction built AS SPECIFIED
(`E_direct+E_image`, both terms present, `E_direct` cited not re-derived,
its PAD-invariance re-confirmed bit-exact — the fourth independent
confirmation) and scored the way PHOTONICS specified — a free-period fit
against REAL T28 data, not exp-080's own mistaken R² shape-comparison
against a candidate curve. Item 1b's honest handling (the literal
"bit-identical" prediction technically refuted at `~1e-14`, substantive
claim confirmed to 11+ orders below signal scale) is disclosure done right.
Item 1c's T21-proximity diagnostic correctly downgrades the lone
near-boundary SUPPORT (`C80−C40`, margin 0.9 points) to a look-elsewhere
artifact rather than letting a mechanically-NEITHER verdict read as
partial confirmation. Item 3's energy bound checks BOTH admittance
families and finds both negligible — the right multi-family discipline.
Item 4's docstring fix matches MATERIALS' own exp-080 Phase-5
recommendation exactly.

## Sharpest attack (≤150 words)

Item 1's entire headline test — the one this cycle calls "the actually
decisive test," producing Combined Verdict NEITHER/REFUTE-leaning — was
run **exclusively under the matched (unobtainium) admittance**.
`photonics_image_term_curve()` calls `ywas.reflection_coefficient_vec`
(matched only); `reflection_coefficient_vec_realizable` is never invoked
anywhere in item 1's construction or item 2's gate re-run — only in item 3,
at a *different* angle convention (`theta_local`, ~5–15°, not the
`90°−θ_beam`≈[48,54]° range item 1 actually uses). This is exactly the gap
exp-080's part (b) exposed one cycle ago (INCONCLUSIVE matched, mean
R²=0.7345, vs. REFUTE realizable, mean R²=0.4305) — and MATERIALS' own
exp-080 Phase-5 review found the two families diverge in **phase** by
−72.6° specifically at ABSORB=40 (vs. ~1.1–1.5° elsewhere). Every one of
this cycle's three scored pairs (`PAIR_PAD`, `PAIR_ABSORB40`, `C80−C40`)
touches ABSORB=40. The lone SUPPORT clears its bar by 0.9 percentage
points. NOTES.md's item 4(a) "within 2×" reassurance is a *magnitude*
comparison at the *wrong* angle range — irrelevant to a phase-sensitive
periodicity fit. This test was never actually checked for
admittance-family-dependence.

## Verdict: **support-with-changes**

The methodology fix (total field, real-data scoring) is a genuine,
correctly-executed advance and should stand. But item 1's Combined Verdict
should not be cited as settled, nor "REFUTE-leaning" treated as a third
independent line of negative evidence for the mechanism class, until the
same construction is re-scored with `E_image` built from
`reflection_coefficient_vec_realizable` at the identical `90°−θ_beam` range
— the tooling already exists in this exact file (`d80`) and was already
used for item 3. This is a cheap, zero-FDTD, same-shift-sized addition, not
a new build.

## Single parameter change that would flip my verdict to support

Re-run item 1's free-period fit with `E_image` computed under
`reflection_coefficient_vec_realizable` (μ_r=1) at the same `90°−θ_beam`
range, and report whether the Combined Verdict / T21-proximity reading is
qualitatively unchanged. If it is — REFUTE-leaning under both admittance
families — that single additional result would fully close the gap and I
would support without reservation.
