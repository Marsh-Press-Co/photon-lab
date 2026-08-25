# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 48 · exp-071

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat 1). Blind to all other
seats' current-cycle critiques. Verified `design_geometry.py` by running it
directly — every geometry, budget, and peak-angle-verification figure in
`phase1_proposal.md` reproduces bit-for-bit from the committed code (R4
compliant): `A=752` held fixed across `C40/C60/C70/C80`, peak-angle
fractions 0.949/0.984 of window ptp/2, budget 74 calls / 5882.3 CPU-s /
28.76 min wall reproduce exactly.*

## Steel-man (optical-response-coherence angle)

The design is internally coherent across the four `ABSORB` depths by
construction, not by re-derivation: it reuses the *identical*
`_free_period_search` machinery (same `sinθ`-periodic functional form, same
`[1°,4°]` grid, same 31-point/0.2° window) already exercised on `C40`/`C80`,
so no per-config methodological drift can creep in. The peak-cell R3
extension is a genuine optical improvement over exp-069's own resolution
leg: verified in code (not asserted), θ=37.2°/41.4° sit at 94.9%/98.4% of
the dense window's own peak-to-peak amplitude — testing resolution
robustness where the periodic signal's optical content is actually large,
not near the zero-crossing (`|delta|≈1.2–1.7×10⁻⁴`) the original R3 leg
accidentally tested, where a real fringe and pure noise both trivially
read ≈0. The mandatory 6-pair cross-config table is the right instrument
for a 4-point causal series: it forces disclosure of pairwise spread
instead of collapsing everything into one slope statistic.

## Sharpest attack

The entire causal claim (ABSORB-tied vs. shared-geometry) is scored at a
single wavelength, 600nm, with no wavelength leg on the new `C60`/`C70`
manipulation at all — and this is exactly the one check that could
actually adjudicate the mechanism question, not just its statistics.
`ABSORB` is specified in grid cells; at native resolution its physical
depth in wavelengths differs by config *and* by λ: 40/60/70/80 cells at
600nm (cpl=20) is 2.0/3.0/3.5/4.0λ, but the *same* cell counts at 750nm
(cpl=25) are 1.6/2.4/2.8/3.2λ. If `P*(ABSORB)` is a genuine optical
coupling to the graded-loss taper's own optical depth, its trend must
shift characteristically between 600nm and 750nm (a different λ-scaled
optical-depth sequence). If it is instead a discretization/cell-count
artifact, the trend should hold in *cell* units regardless of λ. The
existing R3-PEAK block cannot distinguish these — it rescales geometry and
cpl together at fixed λ=600nm and fixed physical ABSORB depth, testing
grid-coarseness sensitivity, not λ-scaling. So even a clean P-071-2 CONFIRM
this cycle cannot be read as "genuine ABSORB-depth-tied mechanism" in any
optical sense — only as "some 600nm-specific ABSORB-correlated statistic,"
a materially weaker claim than the proposal's own headline framing
promises, on the exact axis (wavelength coherence) this seat owns.

## Verdict: **support-with-changes**

The causal manipulation itself (4 points on the ABSORB axis, reusing
already-validated machinery, zero new `lab/` diff) is sound and worth
running — it is a real improvement over exp-070's 2-point desk check. But
its own Combined-Verdict language ("CONFIRMED — genuine ABSORB-depth-tied
mechanism") overclaims what a 600nm-only result can support, and should be
softened to "ABSORB-correlated at 600nm; wavelength-tied vs. cell-count-tied
undetermined" unless a λ leg is added.

## Single parameter change that would flip to full support

Add one cheap confirmatory-power λ leg (mirroring exp-069's own
under-powered-but-disclosed `LEG750` idiom — even a handful of points at
the two peak angles, 37.2°/41.4°, on `C60`/`C70` at 750nm) so the
CONFIRM/REFUTE verdict can be cross-checked for whether any recovered trend
holds in physical (nm, λ-scaled) or grid (cell-count) units. Absent that,
the verdict should be reported with the wavelength caveat stated above,
not as an unqualified mechanism claim.
