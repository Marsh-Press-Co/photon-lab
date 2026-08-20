# PHOTONICS — Phase 2 Critique, Iteration 29

**Steel-man:** The design cleanly isolates one geometric variable. Because
both families hold τ_shell=σ_max·thickness=24.0 exactly (verified in
`design_geometry.py`'s own asserted self-similar law and reproduced by this
proposal's arithmetic), normal-incidence extinction is identical between
them at every r_out by construction — whatever `C` difference emerges is
attributable only to the rim/near-silhouette geometry, not a confounded
optical-depth change. Since the fixed-absolute shell's radial σ(r) profile
is literally unchanged (same 48 cells, same σ_max=0.5) as r_out grows, while
the self-similar profile rescales, the qualitative claim — a fixed-width
leak channel becomes a shrinking angular fraction of a growing silhouette —
is a coherent, testable geometric-optics argument, and r_out's growing
curvature-flattening at fixed shell width should if anything sharpen (not
weaken) the predicted direction. P-0's bit-identity check at r=78 is a good
zero-cost sanity gate.

**Sharpest attack:** The entire predicted effect lives in a near-field/
grazing-incidence diffraction regime — T9's cited "~16-cell transparent
annulus" is a single measurement at one geometry (r=78, self-similar), never
independently re-measured for a shell whose thickness is a shrinking
fraction of r_out (idealization 4 admits this). Diffraction-scale rim
effects scale with λ, not with fixed cell counts, yet the proposal tests
exactly one wavelength (600nm), where this shell happens to sit at 2.4λ
thick. At 450nm the identical physical coating (1.44µm, dx=30nm at every λ
per this bench's own convention) is 3.2λ thick; at 750nm it's 1.92λ — a
33% swing in the one dimensionless ratio (thickness/λ) that governs whether
grazing rays see a sharp or a diffuse rim. §8's P-3 states a program-level
T14 verdict ("does NOT reproduce T14's wrong-direction shallowing") without
qualifying it as 600nm-only, despite PANEL.md's own metrics table requiring
wavelength dependence for exactly this class of claim.

**Verdict:** support-with-changes

**Parameter change that would flip verdict:** Add a single confirmatory
run at 450nm or 750nm, r=156 only (cheap relative to the r=156 mandatory
block already scoped) — or, failing that, explicitly downgrade every P-3/T14
claim in §8 to "at 600nm only, not yet shown wavelength-general" rather than
stating it as a program-level resolution of T14.
