# PHASE 2 — CRITIQUE (PHOTONICS, blind) · exp-082

**Charter check performed.** `build_article()` (`materials.pec_disk(sim,cx,cy,30)`
+ `materials.graded_black_shell(sim,cx,cy,30,dg.R_OUT)`) is byte-identical to
`experiments/024-.../run.py::build("absorber")` — verified by direct read of
both files, not merely the docstring's claim. Location: `(obj_x,obj_y)` is
`BASE_OBJ_X+pad, BASE_OBJ_Y+pad` per `dg065._geom_derived`, i.e. the article
rides the same rigid `pad` translation that keeps C40/G40 a true congruent
pair (`170,792` vs `210,832`) — not a new confound, wavelength/cpl/radius
(600 nm, 20, `R_OUT=78`) unchanged from the established flagship. No
divergence from the cited ancestor found.

## Steel-man (149 words)

The construction is clean: verbatim flagship absorber, congruent-series-
correct placement, bit-exact reproduction of exp-076's empty leg before the
new leg is trusted. A `ratio≈0.66` — decisively inside SURVIVES, not
boundary-hugging — is physically not surprising. `C = (B_obj−B_flank)/
B_flank` is a *ratio*, not a raw subtraction: the article does not remove
the field structure producing the PAD ripple, it only collapses `B_obj`
toward the shadow floor while the flank window (well outside `R_OUT=78`,
past `GUARD_OUT=185`) sees the same background field the empty run does.
A domain-scale coherent modulation superimposed on the illumination
reaching the object window has no obvious reason to divide out cleanly
once the absorber dominates `B_obj`'s absolute level — partial persistence
at material, sub-unity amplitude is the physically expected outcome of a
ratio-channel measurement under a large shadow term, not evidence of a bug.

## Sharpest attack (150 words)

The SURVIVES verdict rests on one aggregate number — `ptp` ratio of two
7-point series sampled at 1° steps against an established `P*=2.8421°`
period: 2.84 samples/period, barely above Nyquist. I independently computed
the point-wise Pearson correlation between `delta_scene(θ)` and
`delta_empty(θ)` from `results.json` (not reported anywhere in the write-up):
**r = 0.031** — statistically indistinguishable from zero. The two series
are not the same oscillation at reduced amplitude; element-wise ratios swing
from −0.56 to +2.36 in sign and magnitude. A `ptp` comparator cannot
distinguish "the PAD mechanism persists, phase-shifted by the article's own
added path length" from "two decorrelated ~10⁻³-scale ripples of unrelated
origin whose peak-to-peak spans happen to land within a factor of 1.5" — and
at near-Nyquist sampling, phase alone can move `ptp` by that much with zero
change in true amplitude. SURVIVES is not yet distinguishable from an
artifact of the 7-point/1°-step design.

## Verdict: **support-with-changes**

## Parameter change that would flip it

Add point-wise shape/phase agreement (e.g. require Pearson `r(delta_scene,
delta_empty) ≥ 0.5` across the shared angles, or a cross-correlation peak at
zero lag) as a co-gating criterion alongside the `ptp` ratio. At the actual
measured `r=0.031`, this flips the verdict from SURVIVES to INCONCLUSIVE —
the full 31-point/0.2° window (already named as the natural follow-up in
Idealization 2) is the clean way to settle it at real statistical power.
