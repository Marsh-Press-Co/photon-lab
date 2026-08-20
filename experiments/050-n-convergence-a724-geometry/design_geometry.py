"""exp-050 design geometry -- geometry-parameterized `beam_divergence_*`
functions, generalizing exp-042's three module-global-geometry functions
(`experiments/042-t21-magnitude-bridge/design_geometry.py:279-355`) to take
a geometry dict `g`, following exp-048 Block B's own `_geom_derived(g)` /
`_src_amp(theta_deg,k,gd)` precedent
(`experiments/048-evidentiary-chord-closure/design_geometry.py:179-219`).

Panel Iteration 27 (lead: MATERIALS & METAMATERIALS, rotation). Phase-4
implementation of the design frozen in `NOTES.md` (Phase-3-synthesized,
Red Team's mandatory-fix docket applied at `phase3_synthesis.md`).

Both source modules are loaded via `importlib.util` under private module
names (NOT `sys.path.insert` + `import design_geometry`) because
`experiments/042-.../design_geometry.py` and
`experiments/048-.../design_geometry.py` share the same basename --
importing both under the default module name would silently alias one to
the other. This module reuses, unmodified: `gaussian_angle_weights` and
`CPL` (exp-042), `aperture_profile`, `_geom_derived`, `_src_amp`,
`GEOM78`, `GEOM_EXP042_OLD` (exp-048, Block B). Nothing from either source
file is copied or re-derived -- every quantity below is the actual
committed function, invoked, per this program's own R4 house rule.

Two NEW functions this module adds (flagged in `phase1_proposal.md` S2.2 as
a genuine gap -- exp-048 Block B never built the obliquity-on-E convention
because it only ever needed the corrected obliquity-on-H one):
`_G_for_g` and the geometry-parameterized `beam_divergence_incoherent`/
`beam_divergence_coherent`, both using the ORIGINAL/committed
obliquity-on-E convention (`_G_for(lam,True)` in exp-042's own module,
`:197-212`) evaluated on `_geom_derived`'s own `r`/`obliquity` output
instead of exp-042's module-global `_R`/`_OBLIQUITY`. Algebraically
identical formula, new only in that it now accepts any geometry dict.
"""

import importlib.util
import sys
from pathlib import Path

import numpy as np

_REPO_ROOT = Path(__file__).resolve().parents[2]


def _load(name, relpath):
    spec = importlib.util.spec_from_file_location(name, _REPO_ROOT / relpath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


dg042 = _load("_exp042_design_geometry", "experiments/042-t21-magnitude-bridge/design_geometry.py")
dg048 = _load("_exp048_design_geometry", "experiments/048-evidentiary-chord-closure/design_geometry.py")

# ------------------------------------------------------------- reused as-is
gaussian_angle_weights = dg042.gaussian_angle_weights   # geometry-independent
CPL = dg042.CPL                                          # identical in both source modules (verified, phase1_proposal.md S2.1 point 1)
aperture_profile = dg048.aperture_profile
_geom_derived = dg048._geom_derived
_src_amp = dg048._src_amp
GEOM78 = dg048.GEOM78
GEOM_EXP042_OLD = dg048.GEOM_EXP042_OLD

if _REPO_ROOT not in [Path(p) for p in sys.path]:
    sys.path.insert(0, str(_REPO_ROOT))


# --------------------------------------------------- new: obliquity-on-E, generalized
def _G_for_g(lam_cells, gd, obliquity=True):
    """Geometry-parameterized reproduction of exp-042's own `_G_for`
    (`:197-212`) -- the ORIGINAL/committed obliquity-ON-E convention
    (obliquity folded into the propagator matrix itself, then squared into
    `|E|^2` downstream), evaluated on `_geom_derived`'s own `r`/`obliquity`
    instead of exp-042's module-global `_R`/`_OBLIQUITY`. No caching (unlike
    exp-042's own `_Gcache`).

    CORRECTION (Phase 5, Red Team mandatory-fix 2, THERMODYNAMICS' catch):
    this docstring originally claimed the omission was justified because
    this module "is called far fewer times per geometry than exp-042's own
    dense theta sweep needed" -- FALSE, verified against exp-049's own
    `run.py`: call counts are identical (36 cells x 3 functions x 9
    N_SERIES-including-401 entries = 972 calls per geometry, both cycles).
    The real reason caching was skipped is simply that it was not built --
    a genuine, disclosed performance gap (contributing to this cycle's own
    understated wall-clock, see NOTES.md Results), not a call-count
    argument. Queued as a low-priority fix for any future geometry-
    parameterized cycle, not applied here (Iteration 27's own Checkpoint
    disposition: non-load-bearing to any scored prediction)."""
    k = 2.0 * np.pi / lam_cells
    G = np.exp(1j * (k * gd["r"] - np.pi / 4)) / np.sqrt(gd["r"])
    if obliquity:
        G = G * gd["obliquity"]
    return k, G


def _window_means(profile, gd, g):
    from lab import ambient as amb
    return amb.window_means(profile, gd["y_lo"], gd["obj_y"], g["R_OUT"], g["GUARD_OUT"], g["W_FLANK"])


def beam_divergence_incoherent_corrected(theta0_deg, fwhm_deg, lam_cells, g, n=41):
    """Geometry-parameterized reproduction of exp-042's own
    `beam_divergence_incoherent_corrected` (`:279-295`) -- single-
    obliquity-via-H (erratum/corrected) convention. Already has a
    precedented building block (exp-048 Block B's `field_and_h`); this
    function inlines the same two-field construction per angle so it can
    reuse `_geom_derived` once per call instead of once per angle."""
    from lab import ambient as amb
    thetas, w = gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    gd = _geom_derived(g)
    k = 2.0 * np.pi / lam_cells
    G0 = np.exp(1j * (k * gd["r"] - np.pi / 4)) / np.sqrt(gd["r"])
    profiles = []
    for th in thetas:
        amp = _src_amp(th, k, gd)
        E = G0 @ amp
        H = (G0 * gd["obliquity"]) @ amp
        profiles.append(-np.real(E * np.conj(H)))
    flanks = [_window_means(b, gd, g)[1] for b in profiles]
    s = amb.incoherent_sum(profiles, flanks, list(w))
    bo, bf = _window_means(s, gd, g)
    return amb.weber(bo, bf)


def beam_divergence_incoherent(theta0_deg, fwhm_deg, lam_cells, g, n=41):
    """Geometry-parameterized reproduction of exp-042's own
    `beam_divergence_incoherent` (`:321-334`) -- the ORIGINAL/committed
    obliquity-on-E convention (`_G_for(lam,True)`), generalized via
    `_G_for_g` (new, this module)."""
    from lab import ambient as amb
    thetas, w = gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    gd = _geom_derived(g)
    k, G = _G_for_g(lam_cells, gd, obliquity=True)
    profiles = [np.abs(G @ _src_amp(th, k, gd)) ** 2 for th in thetas]
    flanks = [_window_means(b, gd, g)[1] for b in profiles]
    s = amb.incoherent_sum(profiles, flanks, list(w))
    bo, bf = _window_means(s, gd, g)
    return amb.weber(bo, bf)


def beam_divergence_coherent(theta0_deg, fwhm_deg, lam_cells, g, n=41):
    """Geometry-parameterized reproduction of exp-042's own
    `beam_divergence_coherent` (`:337-355`) -- QUANTUM's mandatory
    coherent cross-check, obliquity-on-E convention, generalized via
    `_G_for_g`."""
    from lab import ambient as amb
    thetas, w = gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    gd = _geom_derived(g)
    k, G = _G_for_g(lam_cells, gd, obliquity=True)
    E_tot = np.zeros(gd["y_obs"].size, dtype=complex)
    for th, wt in zip(thetas, w):
        E_tot = E_tot + np.sqrt(wt) * (G @ _src_amp(th, k, gd))
    b = np.abs(E_tot) ** 2
    bo, bf = _window_means(b, gd, g)
    return amb.weber(bo, bf)


def main():
    # Self-check: the regression anchor's own single-point sanity test --
    # full statistical scoring lives in run.py, this just confirms the
    # module loads and both source modules resolved without a name clash.
    print("GEOM_EXP042_OLD:", GEOM_EXP042_OLD)
    print("GEOM78:", GEOM78)
    c = beam_divergence_incoherent_corrected(38, 2, CPL[750], GEOM_EXP042_OLD, n=41)
    print(f"sanity: incoherent_corrected(38,2,750nm,GEOM_EXP042_OLD,n=41) = {c!r}")


if __name__ == "__main__":
    main()
