# Phase 2 Critique — PHOTONICS seat (Panel Iteration 78, exp-101)

## Steel-man (own charter: optical-response coherence across wavelength/angle)

The closed-box four-face Poynting reconstruction is the physically correct
instrument for constraint 1's optical question. I read `lab/sections.py` in
full: `p_scat`/`p_abs`/`p_ext` are full-perimeter flux integrals with no
lateral-centering assumption, so "cannot miss the shadow regardless of which
way it walks" is verified in the code, not asserted — immune to the exact
defect that broke `beam_behind_t28` (a shadow walk of 125.7–154.6 cells
against a 160-cell window half-width). The `back_frac`/`fwd_frac`
downstream/sourceward relabeling for this bench's reversed (`-x`)
propagation is also correctly grounded: `_face_flux`/`widths()` measure
`p_back` at the box's low-`x` face, consistent with `src_x>obj_x>plane_x`.
Reusing `box_for_r4`/`ref_for_r4`/`widths_direction_corrected` unmodified,
with a genuine independent `BOX_B` cross-check, is the right scope for a
zero-mechanism instrument fix, and keeps `lab/` diff at zero as required.

## Sharpest attack

Two of the six angles — 39.200000° and 42.960901° (the R4-family
"pool-largest-magnitude" picks) — are selected purely because
`|delta_scene(θ)|` peaks there. But exp-100's own Tier-1 test (`results.json`,
reproduced independently: `by_family["R4"]` → n=35, r=0.1103, p=0.5249) found
NO significant correlation between `delta_scene` and the article's own
absorbed-power fraction (`frac_p_abs`) for exactly this R4 family — versus a
real, significant coupling at R3 (r=0.486, p=0.0042). `delta_scene`'s
realizable content is proven to reduce to at most a lossless-vacuum `PAD`
interference term (exp-076); for R4 specifically there is no established
evidence it tracks the article's optical engagement at all. Yet predictions
#2/#3 read violations at these two angles as meaningful article-optical
findings ("a real, surprising finding," "worth a dedicated Phase-5 flag") —
the selection metric may just as well be tracking where an unrelated domain
artifact peaks, not the article's own angular response. Section 5's
idealizations never disclose this dependency.

## Verdict

**Support-with-changes.** The box-reconstruction mechanics (Tier 0's actual
mandate) are sound and should run as proposed. But predictions #2 and #3
must be re-labeled before Phase 3 freezes: any pass/fail at the two
`delta_scene`-extremal angles (39.2°, 42.960901°) should be reported as
instrument-behavior data (does the box partition stay sane there), not as a
finding about the article's true angular scattering extrema, until Tier 1
resolves whether `delta_scene` tracks the article at all for R4. This is a
labeling fix to the interpretation, not a re-run — it does not block Tier 0
execution.

## Parameter change that would flip to unconditional support

Add one disclosure sentence to §5 (Idealizations): that the two R4-pool
angles are selected on a criterion (`delta_scene` magnitude) with no
established correlation to the article's own optical engagement in the R4
family (r=0.110, p=0.525, exp-100) — so a violation of predictions #2/#3 at
those two angles specifically must be read as evidence about the instrument
at that grid registration, not as evidence about the article's genuine
angle-dependent scattering, pending Tier 1.
