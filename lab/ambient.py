"""
lab.ambient — the ambient-appearance instrument (panel Iteration 1).
====================================================================
Constraint 3 of the phenomenon program ("not a black silhouette under
ambient light") as a number: back-light the scene with N incoherent
plane-wave components at distributed angles — one CW run per (θ, λ) —
and read the observer-directed flux profile B(y) on a pre-registered
near plane. Weber contrast of the object window against flanking
background windows is the silhouette metric, scored against the frozen
perceptual thresholds pinned in the experiment's NOTES (PANEL.md).

LINEAR-MEDIA IDIOM, stated per the quantum seat's Iteration-1 critique:
per-component normalization and post-hoc intensity summation assume
superposition. Any intensity-dependent medium (σ(I) — the program's
flagged front-runner) responds to the instantaneous TOTAL field, so this
instrument's ambient sum cannot be reused for gated objects as-is; the
nonlinear replacement (simultaneous multi-angle injection, ensemble-
averaged random phases) must reproduce THIS instrument's numbers on
linear articles as its bridge gate.

Trust gates: suite stage 9 (empty identity, oblique wavelength, mirror
symmetry, Beer–Lambert slab anchor, oblique lossless-cylinder energy
identity) — green before any object number is believed.
"""

import numpy as np

from . import sections


def ambient_angles(n=9, span_deg=40.0):
    """Symmetric angle set over ±span_deg, n odd keeps θ=0 in the set."""
    return [float(t) for t in np.linspace(-span_deg, span_deg, n)]


def observer_profile(ph, plane_x, y_lo, y_hi):
    """B(y): time-averaged flux toward the observer (−x) per cell on the
    plane — the shadowgraph row. ph = sections.phasors(full_capture)."""
    return -sections.flux_profile_x(ph, plane_x, y_lo, y_hi)


def window_means(b, y_lo, y0, w_obj, guard_out, w_flank):
    """(object-window mean, flank mean) of a profile whose first sample
    sits at absolute y = y_lo. Flanks are BOTH sides, averaged together.
    Window geometry is pre-registered per experiment — never post-hoc."""
    y = np.arange(y_lo, y_lo + b.size)
    rel = np.abs(y - y0)
    obj = float(b[rel <= w_obj].mean())
    fl = (rel >= guard_out) & (rel <= guard_out + w_flank)
    return obj, float(b[fl].mean())


def weber(b_obj, b_flank):
    """C = (B_obj − B_flank)/B_flank: −1 pure silhouette, 0 invisible,
    > 0 glint."""
    return (b_obj - b_flank) / b_flank


def incoherent_sum(scene_profiles, empty_flank_means, weights):
    """Weighted incoherent sum of per-(θ,λ) profiles, each first divided
    by ITS OWN empty-run flank mean (per-component normalization: kills
    source-profile ambiguity; the empty sum's flank mean is then 1 by
    construction, so the empty OBJECT-window deviation is the honest
    instrument-floor reading, not a normalization echo)."""
    total = np.zeros_like(scene_profiles[0])
    wsum = 0.0
    for b, f, w in zip(scene_profiles, empty_flank_means, weights):
        total += w * (b / f)
        wsum += w
    return total / wsum


def contrast_from_runs(scene_profiles, empty_profiles, weights,
                       y_lo, y0, w_obj, guard_out, w_flank):
    """The full pipeline for one (article, λ): per-angle profiles in, a
    dict of summed profiles and Weber contrasts out (scene C, empty C —
    the latter is the decision-floor sample δ_C for this λ)."""
    e_flanks = [window_means(b, y_lo, y0, w_obj, guard_out, w_flank)[1]
                for b in empty_profiles]
    s_sum = incoherent_sum(scene_profiles, e_flanks, weights)
    e_sum = incoherent_sum(empty_profiles, e_flanks, weights)
    so, sf = window_means(s_sum, y_lo, y0, w_obj, guard_out, w_flank)
    eo, ef = window_means(e_sum, y_lo, y0, w_obj, guard_out, w_flank)
    return {"scene_sum": s_sum, "empty_sum": e_sum,
            "C": weber(so, sf), "C_empty": weber(eo, ef),
            "b_obj": so, "b_flank": sf}
