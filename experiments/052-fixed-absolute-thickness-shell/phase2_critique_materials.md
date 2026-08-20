# MATERIALS & METAMATERIALS — Phase 2 Critique, Iteration 29

**Steel-man:** Holding `sigma_max` fixed at the literal r=78-gated value is
the realizability-faithful instrument for the narrow question this cycle
asks. Real coating conductivity/doping is set by material composition, not
by the curvature or size of whatever it's painted on; "same recipe,
different substrate" is exactly what fixed `sigma_max` encodes as a
simulation parameter, without inventing a new invariant — rejecting
reflectance-preserving or optical-depth-rescaling alternatives (§3) is the
right call, since either would smuggle in an unmotivated free choice. Because
`_graded_black`'s depth variable is normalized by absolute shell thickness
(`d=(r_out-rr)/(r_out-r_in)`), the coating's grading law is bit-identical at
every `r_out` — a genuinely reusable recipe, not merely a relabeled
rescaling. The `τ_shell=24` coincidence with the self-similar family is
disclosed as a byproduct of the design choice, not a hidden confound.

**Sharpest attack:** §9 checks only half the realizability claim. It
converts 48 cells → 1.44µm and compares that against the memo's cited
CNT-forest thickness range — but never converts `sigma_max=0.5` (a
dimensionless FDTD-unit parameter) into a real absorption coefficient and
checks *that* against the same literature. `τ_shell=24` packed into 1.44µm
implies an effective absorption length near 60nm — far shorter than cited
CNT-forest figures, which describe near-total absorption over several µm to
tens of µm, not sub-100nm. Right thickness, unchecked (and implausibly
concentrated) absorptivity is not shown realizable. Separately, "in
principle, a literal witness-scale core" overreaches past the memo's own
caveat: the dx-bridge to meter-scale radii needs ~10⁷-cell runs "orders of
magnitude beyond anything this engine has ever run," and every tested
`r_out` (78–312 cells, 2.3–9.4µm) keeps thickness at 15–61% of `r_out` —
never approaching the thin-coating-on-large-substrate regime the CNT
precedent describes.

**Verdict:** support-with-changes

**Parameter change that would flip verdict (optional):** Add to §9 the
implied absorption coefficient `α = τ_shell/thickness` (or equivalent
FDTD-to-physical conductivity conversion) and check it against a cited
CNT-forest optical-depth figure, not thickness alone, and restate the
memo's own witness-scale dx-bridge caveat rather than asserting "in
principle, a literal witness-scale core." If that check lands inside a
published α range, move to full support; if it doesn't, the 1.44µm claim
collapses and the correct call becomes oppose (on §9's realizability
language specifically, not on running the FDTD comparison itself, which is
sound as a geometric-law test either way).
