# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 58 · exp-081

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections — owns: is the proposal's optical
response coherent as stated, across wavelength and angle?)

Independent read of `phase1_proposal.md`, `photonics_construction.py`,
`phase1_results.json`, `_output.txt`, `NOTES.md`, plus the cited ancestors
(exp-080's `phase5_review_photonics.md` §4, `validity_precheck.py`; exp-079's
`phase5_review_photonics.md` §4, `y_wall_aperture_sum.py`). No other seat's
current-cycle critique consulted.

---

## Steel-man (≤150 words)

The construction is a faithful, verified transcription of PHOTONICS' own
formula (`E_direct+r(90°−θ_beam;ABSORB)·W(θ_beam)`, exp-080 §4): I traced
`e_direct_curve`/`dist_direct_cells` against the cited formula and confirmed
it reuses the SAME `source_driven_phase`/`aperture_amplitude` convention as
the already-gated `photonics_image_term_curve`, differing only by the sign
on `y_s` in the propagation distance — no daylight between spec and code.
Item 1a's bit-exact PAD-invariance re-check and item 1b's honest handling of
its own "technically REFUTED, substantively CONFIRMED" 10⁻¹⁴ residual are
genuinely rigorous, not smoothed over. The Combined Verdict (NEITHER) is
computed mechanically from the pre-registered bands, with no visible thumb
on the scale — a real methodology fix over exp-080's wrong-target scoring.

## Sharpest attack (≤150 words)

**Item 1c's "REFUTE-leaning" reading was never pre-registered, and the one
check that would ground it — a reflectance-ablation control on THIS
construction, scored THIS cycle's correct way — was never run.**
`W(θ_beam)` IS exp-079's own `r_ablated=1` image integral (§[7], cited
verbatim in `photonics_image_term_curve`'s docstring), whose period was
already known (exp-079 §5.3) to land near T21 regardless of any wall
reflectance. Item 1c shows `E_total`'s recovered periods also sit near T21
— but nobody multiplied `W(θ_beam)` by a θ_beam-*constant* stand-in for
`r(90°−θ_beam)` and rescored it via `_free_period_search` against the SAME
real T28 targets to check whether the genuinely angle-dependent reflectance
term moves the recovered period at all. Without that ~15-line, zero-FDTD
check (reusing already-gated `free_period_with_widening`), "REFUTE-leaning"
conflates two different claims: *the wall's reflectance disfavors T28* vs.
*this test, like its two predecessors, is structurally insensitive to
r(θ)'s value* — the latter is what all prior evidence in this sub-thread
(exp-078, exp-079) actually points toward, and item 1c cannot distinguish
them.

## Verdict: **support-with-changes**

The build is faithful and the mechanical Combined Verdict is trustworthy.
But the write-up's *substantive* headline ("REFUTE-leaning," carried into
`NOTES.md`'s Result/Learned sections as the actionable reading for
Iteration 59's Checkpoint-2 weighing) rests on a post-hoc diagnostic that
cannot yet distinguish "disfavored mechanism" from "insensitive test" — the
same ambiguity this exact sub-thread already resolved for two earlier
constructions only by running an ablation control. Do not let the
un-pre-registered item 1c language stand as a closing argument against this
construction family without that control.

## Flip condition

Add the reflectance-ablation control to `photonics_construction.py`:
replace `r(90°−θ_beam;ABSORB)` with a θ_beam-constant value (e.g. its own
mean over the sweep, or `1.0`) inside `e_total_curve`, rescore the same 3
pair-deltas against the same real T28 targets via the same
`free_period_with_widening`/`score_period` call, and report whether the
recovered periods/verdicts shift materially. If they do not shift (matching
exp-078/079's own precedent), I'd support labeling this a third,
independently-confirmed **insensitivity** finding — a real result, but a
different and more precise one than "REFUTE-leaning" states — and the verdict
becomes full support. If they shift materially, item 1c's reading is
vindicated and I'd support it as-is.
