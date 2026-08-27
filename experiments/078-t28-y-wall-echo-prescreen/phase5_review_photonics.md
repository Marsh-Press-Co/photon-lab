# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 55 · exp-078

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections). Fresh context, blind to the other
six seats' Phase-5 reviews. Read `PANEL.md`, `AGENTS.md`, `LOGBOOK.md` in
full (RULED OUT R1–R9; T28's live-thread entry, Iterations 46–54 in full),
the complete exp-078 record (`phase1_proposal.md` as corrected in place,
`y_wall_prescreen.py`, `y_wall_prescreen_results.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `phase4_null_calibration_corrected.py`/`_results.json`),
plus background (`experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`).

## 1. Verdict: **PARTIAL**

This cycle is a correctly self-scored INCONCLUSIVE, and the angle-convention
correction that got it there is genuinely right physics, independently
reconstructible from first principles (§2). From my own charter's angle —
is the optical response coherent, across wavelength and angle — the
corrected model is internally consistent (smooth `r(θ)`, correct incidence
convention, gates re-run in the new envelope) but structurally incomplete
on exactly the two axes I own: it never scores its own primary model against
a second wavelength, and it treats five configurations whose reflectance
magnitudes span roughly two orders of magnitude (`|r|` from `≈0.039` at
`ABSORB=40` down to `≈2×10⁻⁴` at `ABSORB=80`, corrected angle, verified §2/§3)
as equal-weight contributors to every period comparison. Neither gap is new
information this cycle invented — both are disclosed idealizations (§6.2,
§6.7) — but neither was touched by the angle-correction docket either, so
they stand exactly where the as-filed document left them. That is a real,
not cosmetic, gap in "coherent across wavelength and angle," which is why
this is PARTIAL rather than PROMISING: the mechanism is not ruled out, but
the pre-screen has not yet honestly tested the two dimensions my seat is
responsible for.

## 2. Independent verification performed

**(a) Re-derived the angle correction from scratch, not from the write-up's
own claim.** `lab/fdtd2d.py::add_line_source`'s docstring states the direct
wave travels along `(−cosθ, +sinθ)`. For a wall whose normal is `x̂`, the
angle from that normal is `arccos(|−cosθ|) = θ` — the x-wall's original,
never-corrected usage. For a wall whose normal is `ŷ`, the angle from that
normal is `arccos(|sinθ|) = 90°−θ`. This is exactly `y_wall_incidence_angle`
in `y_wall_prescreen.py` line 235. I did this derivation independently
before opening `phase2_redteam_audit.md`, then compared: it matches. This is
correct trigonometry, not a convention call the program is choosing between
two defensible options — one of the two calls was simply wrong, and it is
now fixed everywhere the corrected model is used (`use_corrected_angle=True`
by construction, §Phase-3 fix 1).

**(b) Spot-checked whether `arg(r)`/`|r|` at deep `ABSORB` are noise or real
structure — the specific claim VISION's Phase-2 critique flagged and Red
Team's `mpmath` re-implementation confirmed.** I called
`br.reflection_coefficient` myself at `ABSORB∈{40,60,70,80}`, θ ∈
{48°,48.5°,49°,51°,54°} (the corrected envelope):

```
ABSORB=80:  θ=48.0°  |r|=2.02e-04  arg(r)=  47.56°
            θ=48.5°  |r|=2.63e-04  arg(r)=  64.62°
            θ=49.0°  |r|=3.37e-04  arg(r)=  79.28°
            θ=51.0°  |r|=7.77e-04  arg(r)= 126.79°
            θ=54.0°  |r|=1.89e-03  arg(r)=−169.11°
```

Both `|r|` and `arg(r)` vary smoothly and monotonically over this window at
every `ABSORB` depth I tried, including 80 — not the erratic, sign-flipping
behavior float noise at the ~10⁻¹⁶ level would produce on a quantity this
small. This independently corroborates VISION's finding (11–13 significant
figures of real precision) without relying on either VISION's or Red Team's
own script — I recomputed it fresh, in ordinary double precision, and the
qualitative signature (smoothness) alone is enough to rule out "float
noise." THERMODYNAMICS' replacement caution — near-total absorption leaves
little power to carry a coherent phase signature — is the physically
correct concern; it is a statement about signal amplitude/detectability, not
about whether the number itself is trustworthy, and I agree it is the right
one to carry forward.

**(c) Reproduced the three load-bearing scored numbers directly from the
committed JSON, not from prose.** `python3 -c "..."` against
`y_wall_prescreen_results.json::primary_model_scores`:

```
c80_c40_vs_2.8421:       P*_model=4.0000°  rel_dev=0.4074  INCONCLUSIVE
pair_pad_vs_4.6113:      P*_model=3.2180°  rel_dev=0.3021  INCONCLUSIVE
pair_absorb40_vs_4.1761: P*_model=2.8045°  rel_dev=0.3284  INCONCLUSIVE
```

and `primary_model_pair_deltas.stages.c80_c40` confirms all three widening
stages (`narrow[1,4]→wide[1,15]→widest[1,60]`) land `at_boundary: true`,
with R² climbing to `0.9535`/`0.9693` at the two widest stages — the
signature of a fit with no real interior periodic optimum in this window,
not a well-resolved 4° period. Every number matches `phase1_proposal.md`
§5.3 and `phase4_results.md` §1 exactly — no discrepancy found. I also spot-
checked `phase4_null_calibration_corrected_results.json`: `P(null
rel_dev≤observed)` = 0.396/0.126/0.174 for the three comparisons, all far
above 0.05 — none of the corrected numbers carry statistically
distinguishable signal, confirming the frozen prediction and the headline.

**(d) Checked commensurability of the R² comparison used in §7's reasoning
(R9 discipline, applied on my own initiative).** `_fixed_period_fit`'s R² is
affine-invariant, so comparing model-R² (0.12–0.25) to real-data-R²
(0.63–0.82) as "how much of the variance a single sinusoid explains" is a
legitimate like-for-like statistic — the two curves are physically
different quantities (a measured contrast delta vs. an unweighted unit-
amplitude phase proxy) but the R² metric itself does not care. I agree with
VISION's Phase-2 finding that the *inference* drawn from the gap ("therefore
noise-driven") is weaker than the number alone proves, since `Δφ_self(θ)`'s
own non-linearity in θ (two `hypot()` terms plus `arg(r(θ))`) could produce
this R² range even for a mechanistically real effect — but QUANTUM's null-
calibration (independently reproduced by me in (c) above) settles this more
directly than the R²-gap argument does: pure noise matches or beats the
model's own R² 65–83% of the time on this window, which is decisive on its
own regardless of how the R²-comparison inference is read.

## 3. What this pre-screen's own INCONCLUSIVE does — and does not — establish, from my charter

**Angular coherence: now genuinely established, where it was not
as-filed.** The as-filed document's two nominal SUPPORTs were artifacts of
querying `r(θ)` at the wrong angle relative to the y-wall's own normal — a
frame error, not a convention choice (EM's Phase-2 critique states this
distinction correctly, and I agree with it independently from (a) above).
With that fixed, the model's angular dependence is now sourced from the
physically correct tangential-wavevector fraction (`cos²θ`, not `sin²θ`,
for a y-stratified layer), and the gates were re-run in the previously-
untested 48°–54° envelope and pass cleanly. This is real, load-bearing
progress on exactly the question my seat owns, and it is why I do not read
this cycle as "just a bug fix" — it is the first time this y-wall candidate
has actually been asked the geometrically correct question at all.

**Wavelength coherence: still untested for the primary model, and this
matters more here than it has for the x-wall analogs.** §6.7 discloses
"600nm only" as an idealization, but the practical consequence is stronger
than that phrasing suggests: `Δφ_self`'s θ-dependence is now dominated
entirely by `arg(r(θ;ABSORB))` (EM's Phase-2 finding, which I independently
confirm from the code — the geometric term `k·fixed_offset` is
θ-independent by construction, see `edge_image_phase_difference`), and
`arg(r)` is a genuinely dispersive quantity through both `k=2π/λ` inside the
transfer matrix and through `CPL`'s own per-λ cells-per-wavelength discretization.
A mechanism whose entire oscillatory content rides on one dispersive complex
coefficient is exactly the kind of candidate where a 600nm-only period match
(even a strong one, which this is not) would be weak evidence — the
established real-data comparator PHOTONICS' own prior cycle (exp-077) found
even the vetted two-wall x-model's period match reverses sign and
significance between 600nm and 750nm on the same physical dataset. This
cycle's own reference table (§5.1) carries a 750nm `PAIR_PAD` citation
(`3.8271°`) forward as a target, but the y-wall's own primary edge-image
curves are never evaluated at `CPL[750]` — only the explicitly-naive,
already-disclaimed secondary coordinate-swap candidates are. This is a gap
in what my charter is supposed to certify, not merely an omitted nice-to-
have.

**Amplitude/angular-response coherence within the primary model itself: an
unaddressed internal inconsistency, not just missing weighting.**
Idealization 2 (§6) discloses that `cos(Δφ_self(θ))` is used unweighted by
`|r(θ)|`, but the consequence deserves sharper statement than "almost
certainly overstating evidentiary weight." I pulled the corrected-angle
`|r|` bounds directly from `y_wall_prescreen_results.json::
primary_model_edge_curves` (not the as-filed table, which reports a
different, uncorrected range): at `ABSORB=80`, `|r|∈[2.02×10⁻⁴,
1.89×10⁻³]`; at `ABSORB=40`, `|r|∈[1.58×10⁻², 3.87×10⁻²]` — and my own
same-angle spot-check in §2(b) shows the ratio at fixed θ runs roughly
**20×–80×** across the 48°–54° corrected envelope (θ=54°: 0.0387/0.00189
≈ 20×; θ=48°: 0.0158/0.000202 ≈ 78×), not a fixed constant. `C80−C40` and
`PAIR_ABSORB40` both mix a `C80` term whose own physical echo amplitude is
one-to-two orders of magnitude smaller than the term it is compared or
differenced against, yet the scored `cos(Δφ_self)` proxy treats both terms
as unit-amplitude oscillators before differencing. This means two of the
three scored comparisons are, by the model's own stated construction,
weighting a real (if weak) predicted oscillation equally against a term
riding on a much smaller carrier — not necessarily wrong, but not a fair
test of the mechanism's own relative contributions either. `PAIR_PAD` is
the one comparison immune to this (both `C40`/`G40` share `ABSORB=40`,
identical `|r|`), which is also, not coincidentally, the one comparison the
whole pre-screen actually needs to land on for T28's own dominant signal —
and it is the one that stays essentially unmoved by any of this cycle's
fixes, at `rel_dev=0.302`, just over the SUPPORT line and statistically
indistinguishable from chance. That convergence (the physically cleanest
comparison is also the target comparison, and it independently fails on its
own terms) is, to me, the single most informative fact in this cycle's
record — stronger than the angle-correction headline itself for judging
whether to build the full propagator.

## 4. Ranked candidates for Iteration 56 (PHOTONICS' own view)

1. **`|r(θ)|`-weight the self-echo proxy curve and re-score all three
   comparisons — desk-only, zero FDTD, reuses every already-committed
   piece.** Replace `cos(Δφ_self)` with `|r(θ)|·cos(Δφ_self)` (or an
   equivalent normalized-amplitude curve) in `edge_image_curve`, re-run the
   same `_free_period_search`/`score_period` pipeline. This is the direct,
   quantitative version of §3's finding above: does `C80−C40`'s current
   "runs to the 60° search boundary" behavior change once its `C80` term is
   properly discounted relative to `C40`'s, and does `PAIR_ABSORB40`'s
   `rel_dev=0.328` move once `C80`'s negligible-amplitude contribution stops
   being treated as equal-footing? This was explicitly named as the
   pre-screen's own open question 2 (§8) and never executed at Phase 2/3 —
   the angle-correction docket fixed a different, also-real defect, but
   left this one exactly where the as-filed document found it. Given how
   large the `|r|` disparity actually is (roughly 20×–190× depending on
   angle, per §3, not merely "smaller"), I rank this above a wavelength
   check: it could materially change which comparisons are even worth
   taking to a second λ.
2. **Score the primary edge-image model itself (not just the naive
   secondary candidates) at 750nm, against the already-carried
   `PAIR_PAD_750nm=3.8271°` reference — desk-only, `CPL[750]=25`
   substituted for `CPL[600]=20`, zero new FDTD.** This is squarely my
   seat's own charter question and it is currently answered only for the
   naive, already-disclaimed candidates, never for this cycle's actual
   primary claim. Given `arg(r(θ))` is dispersive and is the sole source of
   this model's oscillatory content (§3), a model that cannot reproduce its
   own period ordering across two wavelengths on the same physical geometry
   is a materially weaker candidate than one that has simply never been
   asked — exp-077's own 750nm two-wall check (x-wall analog) found exactly
   this kind of wavelength-dependent reversal, so there is a concrete,
   in-program precedent for expecting this check to be informative rather
   than a formality.
3. **Add the far edge (`y_hi`) and its own far-wall image, and check
   whether it moves the period or only the amplitude — desk-only,
   Idealization 3.** The x-wall precedent (exp-075→exp-077) found the
   two-wall extension left the period bit-identical to the single-wall
   model and only changed shape/amplitude — if the same holds here, that
   is useful confirmation the single-edge reduction is a safe idealization
   for Test-A purposes specifically, closing §8 open question 4 cheaply; if
   it does not hold (plausible, since the y-wall image construction is not
   a coordinate swap of the x-wall's, per §3.2's own finding), that is a
   more significant result — it would mean the edge-dominance idealization
   is doing more work here than it did for the x-wall, and the "does the
   full aperture sum matter" question (§8 item 3) would need to move up the
   queue rather than stay deferred.

None of these three repeats a RULED-OUT item (R1–R9) or a named dead end
(`A_alt≈3·R_OUT`, the `519`-cluster, the P-normalized phase-offset regressor,
the x-normal/unrealizable-admittance coherent echo). All three are
zero-FDTD, reuse only already-committed and already-gated machinery, and
none require building the full y-mirrored Test-B propagator the pre-screen
was explicitly scoped to avoid — consistent with this cycle's own finding
that the case for that larger build is currently weak.

## Compliance note

No RULED OUT item is re-proposed or re-litigated. This review does not
modify `LOGBOOK.md`/`PLAN.md`/`SESSION_LOG.md` or any experiment file, and
makes no git changes.
