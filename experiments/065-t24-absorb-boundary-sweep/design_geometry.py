"""exp-065 design constants -- the dedicated T24 `ABSORB` boundary sweep on
the ambient-contrast (`C_empty`) channel.
=============================================================================
Panel Iteration 42, PHASE 1 (lead: VISION SCIENCE, by rotation). This file is
the PROPOSAL's arithmetic: every number quoted in `phase1_proposal.md` is
produced by running `python3 design_geometry.py`, never hand-typed (house rule
R4/R5, LOGBOOK.md RULED OUT).

Executes live thread T24's own never-run design (opened Iteration 23, exp-046
Phase-5 docket item 19; designed at Iteration 24 Tier-2 #4; re-ranked at
Iterations 25 (#3), 26 (#2), 28) -- "sweep ABSORB with SRC_X moved clear of the
x-damping band so EM's ABSORB=80 confound does not recur, source span held
fixed, all 3 lambda".

THE ONE CHANGE: `absorb` (the graded-loss band thickness, `lab/fdtd2d.py::
Sim._damping`) becomes a controlled variable instead of an inherited constant.

THE CONSTRUCTION (this cycle's own contribution to the T24 design): rather than
move `SRC_X` alone -- which changes `D_SP` and therefore the whole T21 fringe
geometry -- PAD the domain by exactly `ABSORB - 40` on every side and shift
every scene coordinate by the same amount. Under `PAD = ABSORB - 40`:

  * A  = OBJ_Y - y_lo               = 752  cells, for every ABSORB
  * plane-to-(-x)-band clearance    = 37   cells, for every ABSORB
  * source-to-(+x)-band clearance   = 20   cells, for every ABSORB
  * source-span-end-to-y-band       = 0    cells, for every ABSORB
  * D_SP, LEVER, window geometry    unchanged, for every ABSORB

so the ONLY thing that varies across the CONGRUENT series is the band's own
thickness and graded-loss profile. This is verified below, in code, and it is
verified a second way by the desk propagator: exp-048's committed
`edge_diffraction_c_empty_corrected` (a boundary-FREE Huygens-Fresnel sum)
returns BIT-IDENTICAL C_empty for C40/C60/C80, so any difference the FDTD
returns between them is boundary physics by construction, not geometry.

Configurations:
  C40  ABSORB=40 PAD= 0  -- exp-041's geometry VERBATIM (identity anchor)
  C60  ABSORB=60 PAD=20  -- congruent
  C80  ABSORB=80 PAD=40  -- congruent
  G40  ABSORB=40 PAD=40  -- pad-only control (isolates the padding itself)
  N60  ABSORB=60 PAD= 0  -- the NAIVE protocol: what a same-domain ABSORB
                            bump does. `add_line_source`'s default span is
                            [absorb, ny-absorb], so A drops 752 -> 732 and the
                            plane clearance drops 37 -> 17. Run deliberately,
                            labeled, as the diagnostic that quantifies what the
                            naive sweep adds on top of the boundary change.

Pure geometry + desk arithmetic -- NO FDTD in this file.
"""

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..",
                                                "048-evidentiary-chord-closure")))

import design_geometry as dg048          # noqa: E402  (exp-048's propagator)
from lab import glare_sidecar as gs      # noqa: E402

# --------------------------------------------------------------- base geometry
# Copied VERBATIM from experiments/041-t20-angle-audit/design_geometry.py
# (itself copied verbatim from exp-024). Nothing here is recomputed.
BASE_NX = 360
BASE_NY = 1584
BASE_ABSORB = 40
BASE_SRC_X = 300
BASE_PLANE_X = 77
BASE_OBJ_X = 170
BASE_OBJ_Y = BASE_NY // 2                     # 792
TAPER = 40
R_OUT = 78
W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
CPL = {450: 15, 600: 20, 750: 25}
STEPS = 1400
COURANT_FRAC = 0.99
D_SP = BASE_SRC_X - BASE_PLANE_X              # 223
LEVER = BASE_OBJ_X - BASE_PLANE_X             # 93

FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # exp-024's own N=9
SWEEP_ANGLES = (-40.0, -38.0, -35.0, 35.0, 38.0, 40.0)    # this cycle's 6
ANCHOR_ANGLES = (-40.0, -38.0, 38.0, 40.0)   # the 4 present in exp-041 Block MAIN

# The `off_pass` sigma(I) OFF-state article (exp-032/033/034/056), expressed at
# this bench's own radius under this lab's optical-depth convention
# tau_center = 2*sigma*r_out.
TAU_OFF_PASS = 0.0065
SIGMA_OFF_PASS = TAU_OFF_PASS / (2 * R_OUT)

# --------------------------------------------------------------- decision bars
GATE_HARD = 0.001              # exp-024/041's own committed instrument-floor
                                # gate -- THE bar that scores every empty-scene
                                # row in this experiment (exp-041 mandatory
                                # fix 1: an instrument floor is NOT scored
                                # against a perceptual threshold)
C_THR_LAB = gs.c_thr(3.0, 0.4, bar="lab")      # T2 frozen photopic lab bar
C_THR_FIELD = gs.c_thr(3.0, 0.4, bar="field")  # T2 frozen field bar (context)
MARGINAL_LO, MARGINAL_HI = dg048.MARGINAL_LO, dg048.MARGINAL_HI

# T24's own published beam-channel numbers (exp-046 phase5_redteam_audit.md
# section 7 table) -- the figures Block BEAM must reproduce from committed code.
T24_BEAM = {
    "A-v4": dict(lambda_nm=750, theta0_deg=38.0, fwhm_deg=2.0,
                 desk_C=+0.163673, fdtd_C_absorb40=+0.154376,
                 fdtd_C_absorb60=+0.161333, delta=+0.00696),
    "A-v1": dict(lambda_nm=600, theta0_deg=40.0, fwhm_deg=2.0,
                 desk_C=-0.123345, fdtd_C_absorb40=-0.125698,
                 fdtd_C_absorb60=-0.127896, delta=-0.00220),
}

# ---------------------------------------------------------- measured cost basis
# MEASURED on THIS container, 2026-08-24, pre-freeze, at cpl=20/STEPS=1400/
# full_capture, four calls per domain under ProcessPoolExecutor(max_workers=4)
# -- i.e. WITH the 4-way memory contention the real run will have, not a
# single-process figure extrapolated by cell count (cost scales worse than
# cell count on this box: C80/C40 = 1.39x for a 1.28x cell ratio).
#   360x1584 (C40, N60): 24.48 / 25.53 / 24.26 / 25.33 s  -> 25.0 s used
#   400x1624 (C60)     : 29.48 / 30.95 / 32.58 / 31.30 s  -> 31.1 s used
#   440x1664 (C80, G40): 34.55 / 34.08 / 35.49 / 35.17 s  -> 34.8 s used
# Wall for 4 concurrent calls at 440x1664 = 35.51 s -> parallel efficiency
# 0.981 (nproc = 4; capture footprint 35.1 MB/sim, 14 GB free).
# Cross-check on the smallest domain, single process: 20.651 s, and that call
# reproduced C_empty = -0.010964794540566314, BIT-IDENTICAL to exp-041
# results.json block_main (theta=+40, 600 nm).
CPU_S_PER_CALL = {"C40": 25.0, "N60": 25.0, "C60": 31.1, "C80": 34.8, "G40": 34.8}
BASE_CELLS = BASE_NX * BASE_NY
N_WORKERS = 4
PARALLEL_EFFICIENCY = 0.98
OVERHEAD_FACTOR = 1.15          # phasors/window reduction/JSON, not measured


# --------------------------------------------------------------- constructions
def config(absorb, pad, naive=False):
    """One FDTD configuration. `pad` cells are added on EVERY side and every
    scene coordinate shifts by `pad`.

    `naive=False` (this cycle's construction): the source span is passed
    EXPLICITLY and shifts with the scene, y_lo = BASE_ABSORB + pad, so the
    half-aperture A = OBJ_Y - y_lo = 752 is held for every ABSORB.
    `naive=True`: the span is left to `add_line_source`'s own default,
    y_lo = absorb -- which is what a same-domain ABSORB bump silently does,
    and which drags A with it."""
    nx = BASE_NX + 2 * pad
    ny = BASE_NY + 2 * pad
    src_x = BASE_SRC_X + pad
    plane_x = BASE_PLANE_X + pad
    obj_x = BASE_OBJ_X + pad
    obj_y = BASE_OBJ_Y + pad
    y_lo = absorb if naive else (BASE_ABSORB + pad)
    y_hi = ny - y_lo
    return dict(
        naive=naive,
        absorb=absorb, pad=pad, nx=nx, ny=ny,
        src_x=src_x, plane_x=plane_x, obj_x=obj_x, obj_y=obj_y,
        y_lo=y_lo, y_hi=y_hi,
        A=obj_y - y_lo,
        aperture_cells=y_hi - y_lo,
        clear_plane=plane_x - absorb,
        clear_src=(nx - absorb) - src_x,
        clear_span_y=y_lo - absorb,
        d_sp=src_x - plane_x,
        lever=obj_x - plane_x,
        cells=nx * ny,
    )


CONFIGS = {
    "C40": config(40, 0),     # exp-041 verbatim -- identity anchor
    "C60": config(60, 20),    # congruent
    "C80": config(80, 40),    # congruent
    "G40": config(40, 40),    # pad-only control (A held at 752, clearances +40)
    "N60": config(60, 0, naive=True),   # naive protocol (A drops to 732)
}


def propagator_geom(cfg):
    """The geometry dict exp-048's committed desk propagator consumes.
    `_geom_derived` uses g["ABSORB"] ONLY to derive the aperture span
    [ABSORB, NY-ABSORB], so the span -- not the band thickness -- is what
    must be handed over (checked by the assert)."""
    assert cfg["y_hi"] == cfg["ny"] - cfg["y_lo"], "span not symmetric"
    return dict(NY=cfg["ny"], OBJ_Y=cfg["obj_y"], D_SP=cfg["d_sp"],
                GUARD_OUT=GUARD_OUT, R_OUT=R_OUT, W_FLANK=W_FLANK,
                PLANE_X=cfg["plane_x"], SRC_X=cfg["src_x"],
                ABSORB=cfg["y_lo"], TAPER=TAPER)


def causal_identity_step(cfg_a, cfg_b):
    """The largest step count at which the observer-plane row of two
    configurations is guaranteed IDENTICAL by causality alone -- i.e. before
    any signal that has touched a region where the two domains differ can have
    reached the plane. Signal speed is the Courant number S = courant/sqrt(2)
    cells/step (the fastest an FDTD update can transport information).

    The gate is read ONLY over the scored windows of the plane row
    (|y - OBJ_Y| <= W_OBJ, and GUARD_OUT..GUARD_OUT+W_FLANK both sides) --
    NOT the whole row, because the y-band difference region sits flush
    against the source-span end and reaches the row's outermost cells early.

    Three round trips must be excluded, per configuration, all measured from
    the source (the only place energy enters):
      (i)   source -> (+x) band inner edge -> back to the plane
              = 2*clear_src + (src_x - plane_x)
      (ii)  source -> plane -> (-x) band inner edge -> back to the plane
              = d_sp + 2*clear_plane
      (iii) source -> (y) band inner edge -> nearest scored window cell
              = max(clear_span_y, 1) + hypot(d_sp, GUARD_OUT - W_OBJ + ...)
            conservatively: 1 + hypot(d_sp, GUARD_OUT)
    The bound is the earliest of the six, minus a 16-step guard."""
    s = COURANT_FRAC / np.sqrt(2.0)
    paths = []
    for c in (cfg_a, cfg_b):
        paths.append(2 * c["clear_src"] + (c["src_x"] - c["plane_x"]))
        paths.append(c["d_sp"] + 2 * c["clear_plane"])
        paths.append(max(c["clear_span_y"], 1)
                     + float(np.hypot(c["d_sp"], GUARD_OUT)))
    return int(np.floor(min(paths) / s)) - 16


def fdtd_budget():
    """Call counts and wall-clock, block by block. Article/empty legs are
    counted explicitly; no leg is double-counted (FALLBACK angles shared with
    Block SWEEP at 600 nm are reused, not re-run)."""
    n_lam = len(CPL)
    n_sweep_ang = len(SWEEP_ANGLES)
    # Block SWEEP: 6 angles x 3 lambda, at C40/C60/C80/N60
    sweep = {k: n_sweep_ang * n_lam for k in ("C40", "C60", "C80", "N60")}
    # Block PAD: G40 at theta in {-35,35,40} x 3 lambda (pad-only control +
    # the causal-identity gate's own pair)
    pad = {"G40": 3 * n_lam}
    # Block ARTICLE: N9 FALLBACK at 600 nm, article + empty, at C40 and C80.
    # +-35 @600nm empty already exist in Block SWEEP -> 7 new empty angles.
    article = {"C40": len(FALLBACK_ANGLES) + 7, "C80": len(FALLBACK_ANGLES) + 7}
    # Block BEAM: 2 T24 cells at C40 / C60 / N60
    beam = {"C40": 2, "C60": 2, "N60": 2}
    per_cfg = {}
    for d in (sweep, pad, article, beam):
        for k, v in d.items():
            per_cfg[k] = per_cfg.get(k, 0) + v
    cpu = sum(n * CPU_S_PER_CALL[k] for k, n in per_cfg.items())
    total_calls = sum(per_cfg.values())
    wall = OVERHEAD_FACTOR * cpu / (N_WORKERS * PARALLEL_EFFICIENCY)
    return dict(sweep=sweep, pad=pad, article=article, beam=beam,
                per_config=per_cfg, total_calls=total_calls,
                cpu_s=cpu, wall_s=wall)


def main():
    print("=" * 78)
    print("exp-065 -- T24 ABSORB boundary sweep: geometry and desk arithmetic")
    print("=" * 78)

    print("\n[1] CONFIGURATIONS (congruence check)")
    hdr = ("cfg", "ABS", "PAD", "NX", "NY", "SRC_X", "PLANE_X", "OBJ_Y",
           "y_lo", "y_hi", "A", "aper", "clrPl", "clrSrc", "clrSpan", "D_SP")
    print("  " + " ".join(f"{h:>7}" for h in hdr))
    for k, c in CONFIGS.items():
        row = (k, c["absorb"], c["pad"], c["nx"], c["ny"], c["src_x"],
               c["plane_x"], c["obj_y"], c["y_lo"], c["y_hi"], c["A"],
               c["aperture_cells"], c["clear_plane"], c["clear_src"],
               c["clear_span_y"], c["d_sp"])
        print("  " + " ".join(f"{v:>7}" for v in row))
    cong = [CONFIGS[k] for k in ("C40", "C60", "C80")]
    for field, want in (("A", 752), ("clear_plane", 37), ("clear_src", 20),
                        ("clear_span_y", 0), ("d_sp", 223), ("lever", 93),
                        ("aperture_cells", 1504)):
        vals = {c[field] for c in cong}
        assert vals == {want}, (field, vals, want)
        print(f"    congruent series holds {field:>15} = {want} across "
              f"ABSORB in (40, 60, 80)  [OK]")
    print(f"    NAIVE N60 breaks it: A={CONFIGS['N60']['A']} "
          f"(-{752 - CONFIGS['N60']['A']} cells, "
          f"{100 * (752 - CONFIGS['N60']['A']) / 752:.2f}%), "
          f"clear_plane={CONFIGS['N60']['clear_plane']}, "
          f"aperture={CONFIGS['N60']['aperture_cells']}")

    print("\n[2] DESK PROPAGATOR (exp-048 `edge_diffraction_c_empty_corrected`,")
    print("    a boundary-FREE Huygens-Fresnel sum -- zero free parameters)")
    desk = {}
    for k in ("C40", "C60", "C80", "G40", "N60"):
        g = propagator_geom(CONFIGS[k])
        for lam, cpl in sorted(CPL.items()):
            for th in (35.0, 38.0, 40.0):
                desk[(k, lam, th)] = dg048.edge_diffraction_c_empty_corrected(
                    th, cpl, g)
    print("    lam  theta |        C40        C60        C80        G40"
          "        N60 |  N60-C40")
    for lam in sorted(CPL):
        for th in (35.0, 38.0, 40.0):
            vals = [desk[(k, lam, th)] for k in ("C40", "C60", "C80", "G40", "N60")]
            print(f"    {lam}  {th:4.0f}  | " +
                  " ".join(f"{v:+10.6f}" for v in vals) +
                  f" | {vals[4] - vals[0]:+9.6f}")
    dmax = max(abs(desk[(k, lam, th)] - desk[("C40", lam, th)])
               for k in ("C60", "C80") for lam in CPL for th in (35.0, 38.0, 40.0))
    print(f"\n    max |desk(C60/C80) - desk(C40)| over all 9 cells = {dmax:.3e}")
    print("      -> the congruent series is EXACTLY degenerate in the")
    print("         boundary-free model: every FDTD difference C60/C80 vs C40")
    print("         is boundary physics by construction.")
    n60 = [abs(desk[("N60", lam, th)] - desk[("C40", lam, th)])
           for lam in CPL for th in (35.0, 38.0, 40.0)]
    print(f"    NAIVE artifact predicted by the SAME model, zero FDTD:")
    print(f"      |desk(N60) - desk(C40)|  min {min(n60):.3e}  "
          f"median {float(np.median(n60)):.3e}  max {max(n60):.3e}")
    print(f"      (compare T24's published beam-channel systematic "
          f"0.0022-0.0070 absolute)")
    print(f"    G40 (pad-only) vs C40 in the desk model: "
          f"{max(abs(desk[('G40', lam, th)] - desk[('C40', lam, th)]) for lam in CPL for th in (35.0, 38.0, 40.0)):.3e}")

    print("\n[3] T21 FRINGE PERIOD at each A (exp-048 `ripple_period_deg`)")
    for lam, cpl in sorted(CPL.items()):
        p752 = dg048.ripple_period_deg(752, cpl, 40.0)
        p732 = dg048.ripple_period_deg(732, cpl, 40.0)
        # fringe phase in cycles accumulated at theta=40 for each aperture
        cyc752 = 752 * np.sin(np.radians(40.0)) / cpl
        cyc732 = 732 * np.sin(np.radians(40.0)) / cpl
        print(f"    {lam}nm: P(A=752)={p752:.3f} deg  P(A=732)={p732:.3f} deg"
              f"   |delta phase| at theta=40 = {abs(cyc752 - cyc732):.3f} cycles")

    print("\n[4] CAUSAL-IDENTITY GATE STEP (pad construction, C40 vs G40)")
    n_causal = causal_identity_step(CONFIGS["C40"], CONFIGS["G40"])
    s = COURANT_FRAC / np.sqrt(2.0)
    print(f"    Courant S = {s:.6f} cells/step")
    print(f"    first-arrival step at the plane (direct, D_SP={D_SP}) = "
          f"{int(np.ceil(D_SP / s))}")
    print(f"    guaranteed-identical up to step n = {n_causal}")
    assert n_causal > int(np.ceil(D_SP / s)), "no causal window exists"
    print(f"    -> a usable window of {n_causal - int(np.ceil(D_SP / s))} steps "
          f"AFTER first light, BEFORE any boundary can matter.")

    print("\n[5] FROZEN PERCEPTUAL BARS (invoked from lab/glare_sidecar.py)")
    print(f"    C_thr lab   (cued,   L=3 cd/m2, p=0.4) = {C_THR_LAB:.6f}")
    print(f"    C_thr field (uncued, L=3 cd/m2, p=0.4) = {C_THR_FIELD:.6f}")
    print(f"    MARGINAL band convention = [{MARGINAL_LO}, {MARGINAL_HI}] x bar")
    for L in (1e-1, 1e-2, 1e-3, 1e-4):
        lo = gs.c_thr(L, 0.4, bar="lab")
        hi = gs.c_thr(L, 0.5, bar="lab")
        print(f"    C_thr(L={L:g} cd/m2, lab) = {lo:.4f} (p=0.4) .. "
              f"{hi:.4f} (p=0.5)")
    print(f"    INSTRUMENT-FLOOR gate (scores every empty row): "
          f"GATE_HARD = {GATE_HARD}")

    print("\n[6] ARTICLE (Block ARTICLE)")
    print(f"    off_pass-equivalent uniform disk: tau_center = {TAU_OFF_PASS}, "
          f"r_out = {R_OUT} -> sigma_e = {SIGMA_OFF_PASS!r}")

    print("\n[7] FDTD BUDGET")
    b = fdtd_budget()
    for name in ("sweep", "pad", "article", "beam"):
        print(f"    Block {name.upper():<8} {b[name]}")
    print(f"    per-configuration totals: {b['per_config']}")
    print(f"    TOTAL FDTD calls = {b['total_calls']}")
    print(f"    measured cost basis (4-way parallel, this container): "
          f"{CPU_S_PER_CALL}")
    print(f"    projected CPU  = {b['cpu_s']:.0f} s = {b['cpu_s'] / 60:.1f} min")
    print(f"    projected WALL = {b['wall_s']:.0f} s = {b['wall_s'] / 60:.1f} min "
          f"({N_WORKERS} workers at {PARALLEL_EFFICIENCY:.0%} efficiency)")
    print(f"    3x safety envelope = {3 * b['wall_s'] / 60:.1f} min")

    print("\n[8] T24's PUBLISHED BEAM-CHANNEL NUMBERS (Block BEAM must reproduce)")
    for k, v in T24_BEAM.items():
        rel = abs(v["delta"]) / abs(v["fdtd_C_absorb40"])
        print(f"    {k}: {v['lambda_nm']}nm theta0={v['theta0_deg']} "
              f"FWHM={v['fwhm_deg']}  C(40)={v['fdtd_C_absorb40']:+.6f}  "
              f"C(60)={v['fdtd_C_absorb60']:+.6f}  dC={v['delta']:+.5f}  "
              f"|dC|/|C| = {rel:.4f}")
    print("    -> T24's systematic is 1.8-4.5% RELATIVE on the beam channel.")
    print("       Whether it transfers to the plane/ambient channel as an")
    print("       ABSOLUTE 0.002-0.007 or as a RELATIVE 2-5% is exactly what")
    print("       this cycle measures -- and the two hypotheses differ by")
    print("       ~30x on a |C_empty| ~ 0.01 row.")


if __name__ == "__main__":
    main()
