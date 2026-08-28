# PHASE 2 — CRITIQUE (MATERIALS & METAMATERIALS, blind) · exp-084

## Steel-man (≤150 words)

This is the first T28 cycle to model a *diffractor* instead of a *reflector*,
correctly diagnosed as a category error in the prior `P_edge_B` far-field
formula (0.197% of the Fraunhofer range — deep Fresnel, confirmed by the
new `√(λ·D_SP)≈66.8`-cell length scale replacing `A`). From my own charter:
the raised-cosine (Hann) taper isn't an exotic idealization — amplitude
apodization of an aperture illumination is a standard, published,
trivially-realizable antenna/optics technique, so nothing here strains
realizability on the taper's own account. Best practice: Anchor 1 validates
the discrete Green's-function machinery against the classical Hecht/Born–Wolf
formula to 3.3×10⁻³ (paraxial substitute) before trusting the exact variant;
Anchor 2 is then run on leg (b) and *fails* its own convergence-checked
composition-identity test (ratio stable at 2.894–2.895 across 1×–8×
oversampling) — a genuine self-caught instrument defect, honestly withheld
rather than reported as REFUTE. That is real house discipline.

## Sharpest attack (≤150 words)

Leg (a)'s SUPPORT is scored against `P_edge_A`, but the proposal's own
structural corollary proves `max|C_model(C80)−C_model(C40)|=0.0` exactly —
this model cannot, even in principle, produce the real signal `P_edge_A` was
originally defined from. It is scored instead against an individual-config
curve, and exp-070 already established that this same family's individual-
config fits (R²=0.26–0.30) look "more consistent with a compromise fit
between two nearby, imperfectly-separated frequencies" (T21's 1.9608° vs.
the ~2.84° signal) than genuine confirmation — leg (a)'s R²=0.3697 sits in
exactly that marginal band. So even granting SUPPORT, my seat's realizability
bound is unmoved either way: at best this shows the empty-scene *source*
geometry (not any material) is congruent with `P_edge_A`, reinforcing exp-082's
zero-realizability-content rule for that reading — while leg (b), the one leg
that would engage my Iteration-59 article-rim-vs-artifact ambiguity (my own
prior-cycle finding: reading (i) domain-artifact = zero realizability;
reading (ii) rim diffraction = trivially-realizable/published), fails Anchor 2
and returns no usable answer. Zero realizability content still applies to
what this cycle actually delivers.

## Verdict

**Support-with-changes.** The instrument work (Anchors 1–2, R5 specificity
control) is sound and should be committed as-is. But leg (a)'s SUPPORT should
be reported with an explicit caveat that it cannot distinguish "genuine
source-edge diffraction" from "compromise fit near T21's own established
1.9608° fringe" (the exact R²-band ambiguity exp-070 already flagged for this
family), and leg (b) needs a corrected single-integral (Rayleigh–Sommerfeld)
kernel — not a patched two-stage composition — before the article-rim
question, the one with genuine realizability content, can be adjudicated
either way.

## Parameter change that would flip my verdict

Rebuild leg (b) with a proper single-integral double-diffraction kernel (or
an explicit RS boundary term at the intermediate surface) so it passes its
own Anchor 2 to the same tolerance leg (a) achieved, and report a real
SUPPORT/INCONCLUSIVE/REFUTE against `P*`. A clean result either way finally
resolves my own Iteration-59 realizability ambiguity — that would move me to
full support.
