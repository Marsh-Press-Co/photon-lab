"""
lab.phase_lines — disk-persisted per-angle complex Ez/Hy-line phasors.
=======================================================================
Panel Iteration 35 (QUANTUM OPTICS, LOCKED lead, breaking rotation),
T25's phase-variance redesign. Persists each single-source leg's own
steady-state Ez/Hy phasor, pre-interpolated onto a fixed observation
line x=plane_x, so that ANY relative-phase draw across N angular
components can be reconstructed post-hoc — zero marginal FDTD cost per
draw — via the LTI phasor law derived and independently re-derived
THREE separate ways at Phase 2 (PHOTONICS, ELECTROMAGNETISM, Red Team;
LOGBOOK.md Iteration 35): a constant drive-phase offset delta, injected
as sin(omega*n - phase_geom(y) - delta), multiplies that source's own
steady-state phasor by exp(+i*delta) relative to delta=0 — identically
for Ez AND Hy, since Hy is driven from Ez only through the source's own
delta-independent curl recursion (lab/fdtd2d.py's Sim.run: sources touch
Ez only; Hx/Hy update from Ez differences with no source term).

Bespoke, non-artifact format — deliberately NOT routed through
lab.artifacts / lab/ARTIFACTS.md (hard-limit contract file, human-
governed, never touched; confirmed harmless either way at Panel
Iteration 35 Phase 2 Red Team audit — lab.artifacts' own source-spec
validation only rejects MISSING required keys, never unknown extra
ones, so a `rel_phase` key on Sim.source_specs is a no-op to that
schema regardless).

Line-only scope, deliberate (Panel Iteration 35 Phase 1 idealization
#2): only the ambient-instrument's observation line is persisted, since
that's all lab.ambient's Weber-contrast pipeline ever reads
(sections.flux_profile_x's Hy->Ez-line interpolation is itself a fixed
spatial average, so it commutes with persistence — saved here already
pre-interpolated). No radial-absorbed-power/energy-closure channel
exists at this format; THERMODYNAMICS' own per-leg absorbed-power
anchor (Phase 2 mandatory fix, exp-058) is computed directly from each
leg's live capture BEFORE the line is extracted, not from this saved
format.

Trust gate: suite stage 20 (lab/validation/run_all.py) — a disk round
trip at BOTH zero and an arbitrary nonzero relative phase, each checked
against a real joint many-source Sim call — green before any
reconstructed C(delta) is believed.
"""

import numpy as np


def line_phasor(ph, plane_x, y_lo, y_hi):
    """Extract (ez_line, hy_line) at x=plane_x, y in [y_lo, y_hi), from a
    sections.phasors() dict. hy_line is PRE-INTERPOLATED onto the Ez grid
    location, exactly as sections.flux_profile_x/lab.ambient.observer_profile
    do internally (0.5*(hy[x-1,:]+hy[x,:])) — so flux_from_lines() below
    reproduces their B(y) convention exactly from a persisted line pair."""
    ys = slice(y_lo, y_hi)
    ez_line = np.array(ph["ez"][plane_x, ys], dtype=np.complex128, copy=True)
    hy_line = 0.5 * (ph["hy"][plane_x - 1, ys] + ph["hy"][plane_x, ys])
    hy_line = np.array(hy_line, dtype=np.complex128, copy=True)
    return ez_line, hy_line


def save_leg(path, ez_line, hy_line, **meta):
    """Persist one single-source leg's line phasors + metadata to a
    bespoke, compressed .npz — complex128, never touches lab.artifacts.
    Scalar metadata (angle_deg, plane_x, y_lo, y_hi, article, lam_nm,
    cpl, rel_phase, ...) is stored as 0-d arrays under a `meta_` prefix
    so a plain np.load round-trips it without pickling."""
    arrays = {"ez_line": np.asarray(ez_line, dtype=np.complex128),
              "hy_line": np.asarray(hy_line, dtype=np.complex128)}
    for k, v in meta.items():
        arrays[f"meta_{k}"] = np.asarray(v)
    np.savez_compressed(path, **arrays)


def load_leg(path):
    """Round-trip a leg saved by save_leg(). Returns (ez_line, hy_line,
    meta_dict) — the genuine disk-read half of the round trip suite
    stage 20 gates."""
    with np.load(path) as z:
        ez_line = np.array(z["ez_line"], dtype=np.complex128)
        hy_line = np.array(z["hy_line"], dtype=np.complex128)
        meta = {}
        for k in z.files:
            if k.startswith("meta_"):
                v = z[k]
                meta[k[len("meta_"):]] = v.item() if v.shape == () else v
    return ez_line, hy_line, meta


def reconstruct_profile(ez_lines, hy_lines, rel_phases):
    """ez_lines/hy_lines: dict[angle -> line array] (baseline, rel_phase=0
    captures, loaded or in-memory). rel_phases: dict[angle -> delta,
    radians]. Returns (ez_total, hy_total): the SAME complex factor
    exp(+i*delta) applied to both Ez and Hy per angle, then summed — the
    LTI reconstruction law verified at Panel Iteration 35 Phase 2 (three
    independent derivations: PHOTONICS, ELECTROMAGNETISM, Red Team) and
    gated at suite stage 20 (Q7: delta=0 for all; Q8: an arbitrary
    nonzero draw)."""
    angles = list(ez_lines.keys())
    ez_total = np.zeros_like(ez_lines[angles[0]])
    hy_total = np.zeros_like(hy_lines[angles[0]])
    for ang in angles:
        factor = np.exp(1j * rel_phases[ang])
        ez_total = ez_total + factor * ez_lines[ang]
        hy_total = hy_total + factor * hy_lines[ang]
    return ez_total, hy_total


def flux_from_lines(ez_line, hy_line):
    """B(y) = -0.5*Re{ez * conj(hy)} — exactly lab.ambient.observer_profile's
    own convention (sections.flux_profile_x's -Sx: time-averaged flux
    toward the observer, -x direction), applied to a persisted/
    reconstructed line pair instead of a live full-2D capture. Feeds
    lab.ambient.window_means/weber unmodified."""
    return -0.5 * np.real(ez_line * np.conj(hy_line))
