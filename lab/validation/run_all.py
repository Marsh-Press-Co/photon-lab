"""
lab/validation/run_all.py — the bench trust suite.
==================================================
Five stages, each with hard expected numbers. Exit code 0 only if all
selected stages pass.

  1. regression   — exp-000 scene through the lab engine reproduces its
                    committed results (lambda exact, shadow, peak field)
  2. impedance    — half-space reflection vs Fresnel: eps-only R=1/9;
                    impedance-matched (eps=mu) R~0, scalar AND tensor paths
  3. fdtd-lib     — same scene through flaport `fdtd`: SCATTERED-field
                    pattern correlation (scene minus each solver's own
                    vacuum run, so source-profile differences cancel)
  4. ceviche      — same scene through ceviche FDFD, same scattered-field
                    comparison
  5. cloak smoke  — bare PEC vs Schurig-reduced-cloaked PEC: scattered
                    field must drop

Run:  .venv\\Scripts\\python.exe lab\\validation\\run_all.py [--only 1234]
(stage 5 is the heavy one — run it alone with --only 5)

Measurement notes (learned the hard way, first run of this suite):
  * wavelength via raw FFT bins quantizes badly on short strips — use
    lab.fdtd2d.spatial_wavelength (zero-pad + parabolic peak).
  * reflection monitors must sit CLOSE to the interface: beam diffraction
    losses then cancel between reference and scene runs.
  * cross-solver comparisons must compare SCATTERED fields — total fields
    inherit each library's source profile.
"""

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from lab import Sim, materials
from lab.fdtd2d import spatial_wavelength

HERE = os.path.dirname(os.path.abspath(__file__))
BG, INK, MUTED = "#0d1117", "#e6edf3", "#9198a1"
try:
    CMAP = matplotlib.colormaps["berlin"]
except KeyError:
    CMAP = matplotlib.colormaps["seismic"]
plt.rcParams.update({
    "figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
    "text.color": INK, "axes.edgecolor": MUTED, "axes.labelcolor": MUTED,
    "xtick.color": MUTED, "ytick.color": MUTED,
})

RESULTS = []


def check(stage, name, value, ok, expect):
    RESULTS.append((stage, name, value, ok, expect))
    print(f"  [{'PASS' if ok else 'FAIL'}] {stage} · {name}: {value}  (expect {expect})")


def pearson(a, b):
    a = a.ravel() - a.mean()
    b = b.ravel() - b.mean()
    return float(np.sum(a * b) / np.sqrt(np.sum(a**2) * np.sum(b**2)))


# --------------------------------------------------------------- stage 1
def stage1_regression():
    print("stage 1 — exp-000 regression through lab engine")
    sim = Sim(720, 440, cells_per_lambda=20, courant_frac=0.99, absorb=36)
    materials.dielectric_cylinder(sim, 302, 220, 40, 4.0)
    sim.add_line_source(60)
    sim.run(1350)
    lam = sim.measure_lambda(y_line=370, x_lo=80, x_hi=640)
    peak = float(np.max(np.abs(sim.Ez)))
    env = sim.envelope()
    shadow = float(np.mean(env[362:502, 200:240] ** 2) / np.mean(env[362:502, 340:380] ** 2))
    check("regression", "lambda (cells)", f"{lam:.2f}", abs(lam - 20.0) <= 0.2, "20.0±0.2")
    check("regression", "peak |Ez|", f"{peak:.2f}", abs(peak - 2.50) <= 0.15, "2.50±0.15")
    check("regression", "shadow ratio", f"{shadow:.3f}", abs(shadow - 0.48) <= 0.03, "0.48±0.03")

    fig, ax = plt.subplots(figsize=(6.4, 4.0), dpi=140)
    v = 0.9 * np.max(np.abs(sim.Ez[:260, :]))
    ax.imshow(sim.Ez.T, cmap=CMAP, vmin=-v, vmax=v, origin="lower")
    ax.set_title("stage 1 — exp-000 scene via lab engine", loc="left", fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])
    fig.tight_layout(); fig.savefig(os.path.join(HERE, "v1_regression.png")); plt.close(fig)


# --------------------------------------------------------------- stage 2
def _reflection(build):
    """Monitor sits at x=230, 30 cells before the x=260 interface: beam
    diffraction losses up to the monitor are identical in reference and
    scene runs and cancel in the ratio."""
    sim = Sim(500, 240, cells_per_lambda=20, courant_frac=0.99, absorb=36)
    if build:
        build(sim)
    sim.add_line_source(60)
    mon = sim.add_poynting_line(230, start_step=1000)
    sim.run(1314)          # 314-step window ≈ 11 full periods
    return mon.mean_flux()


def stage2_impedance():
    print("stage 2 — half-space reflection vs Fresnel")
    f0 = _reflection(None)

    def eps_only(sim):
        sim.eps_r[260:, :] = 4.0

    def matched_scalar(sim):
        sim.eps_r[260:, :] = 4.0
        sim.ensure_inv_mu()
        sim.inv_mu["xx"][260:, :] = 0.25
        sim.inv_mu["yy"][260:, :] = 0.25

    def matched_yy(sim):
        sim.eps_r[260:, :] = 4.0
        sim.ensure_inv_mu()
        sim.inv_mu["yy"][260:, :] = 0.25   # only the component this wave feels

    for name, build, expect, tol in [
        ("eps=4, mu=1 (Fresnel)", eps_only, 1.0 / 9.0, 0.025),
        ("eps=mu=4 matched (scalar path)", matched_scalar, 0.0, 0.02),
        ("mu_yy=4 matched (tensor path)", matched_yy, 0.0, 0.02),
    ]:
        r = (f0 - _reflection(build)) / f0
        check("impedance", name, f"R={r:.4f}", abs(r - expect) <= tol,
              f"{expect:.3f}±{tol}")


# ------------------------------------------------------- stages 3+4 setup
ROI = (slice(70, 260), slice(40, 160))


def _our_small_scene(with_cylinder):
    sim = Sim(300, 200, cells_per_lambda=20, courant_frac=0.99, absorb=30)
    if with_cylinder:
        materials.dielectric_cylinder(sim, 126, 100, 20, 4.0)
    sim.add_line_source(54)
    sim.run(780)
    return sim, sim.envelope()


def stage3_fdtd_lib(ours_scat, ours_shadow):
    print("stage 3 — cross-check vs flaport fdtd (time domain)")
    try:
        import fdtd as flib

        flib.set_backend("numpy")
        c0 = 299792458.0

        def lib_env(with_cylinder):
            grid = flib.Grid(shape=(300, 200, 1), grid_spacing=30e-9)
            grid[0:10, :, :] = flib.PML(name="pml_xlow")
            grid[-10:, :, :] = flib.PML(name="pml_xhigh")
            grid[:, 0:10, :] = flib.PML(name="pml_ylow")
            grid[:, -10:, :] = flib.PML(name="pml_yhigh")
            grid[54, 30:170, 0] = flib.LineSource(period=600e-9 / c0, name="src")
            if with_cylinder:
                x = np.arange(106, 146)[:, None]
                y = np.arange(80, 120)[None, :]
                eps_block = np.where((x - 126) ** 2 + (y - 100) ** 2 <= 400, 4.0, 1.0)
                grid[106:146, 80:120, 0] = flib.Object(
                    permittivity=eps_block[:, :, None], name="cyl")
            grid.run(780, progress_bar=False)
            ez_a = np.asarray(grid.E[:, :, 0, 2]).copy()
            grid.run(7, progress_bar=False)  # ~quarter period at their courant
            ez_b = np.asarray(grid.E[:, :, 0, 2]).copy()
            return ez_a, np.sqrt(ez_a**2 + ez_b**2)

        ez_scene, env_scene = lib_env(True)
        _, env_vac = lib_env(False)
        scat_lib = env_scene - env_vac

        corr = pearson(ours_scat[ROI], scat_lib[ROI])
        lam_lib = spatial_wavelength(ez_scene[70:260, 160])
        sh_lib = float(np.mean(env_scene[156:226, 90:110] ** 2)
                       / np.mean(env_scene[156:226, 140:165] ** 2))

        check("fdtd-lib", "scattered-pattern corr", f"{corr:.3f}", corr >= 0.90, ">=0.90")
        check("fdtd-lib", "lambda (cells)", f"{lam_lib:.2f}", abs(lam_lib - 20.0) <= 0.5, "20.0±0.5")
        check("fdtd-lib", "shadow agreement",
              f"{sh_lib:.3f} vs ours {ours_shadow:.3f}",
              abs(sh_lib - ours_shadow) <= 0.10, "|Δ|<=0.10")
        return env_scene
    except Exception as e:  # keep the suite running; a FAIL here is loud enough
        check("fdtd-lib", "stage ran", f"EXC: {type(e).__name__}: {e}", False, "no exception")
        return None


def stage4_ceviche(ours_scat):
    print("stage 4 — cross-check vs ceviche (FDFD, frequency domain)")
    try:
        from ceviche import fdfd_ez

        c0 = 299792458.0
        omega = 2 * np.pi * c0 / 600e-9

        def solve(with_cylinder):
            eps = np.ones((300, 200))
            if with_cylinder:
                x = np.arange(300)[:, None]
                y = np.arange(200)[None, :]
                eps[(x - 126) ** 2 + (y - 100) ** 2 <= 400] = 4.0
            src = np.zeros((300, 200), dtype=complex)
            src[54, 30:170] = 1.0
            F = fdfd_ez(omega, 30e-9, eps, [20, 20])
            _, _, ez = F.solve(src)
            return ez

        ez_scene = solve(True)
        ez_vac = solve(False)
        scat_c = np.abs(ez_scene) - np.abs(ez_vac)

        corr = pearson(ours_scat[ROI], scat_c[ROI])
        lam_c = spatial_wavelength(np.real(ez_scene)[70:260, 160])

        check("ceviche", "scattered-pattern corr", f"{corr:.3f}", corr >= 0.90, ">=0.90")
        check("ceviche", "lambda (cells)", f"{lam_c:.2f}", abs(lam_c - 20.0) <= 0.5, "20.0±0.5")
        return np.abs(ez_scene)
    except Exception as e:
        check("ceviche", "stage ran", f"EXC: {type(e).__name__}: {e}", False, "no exception")
        return None


# --------------------------------------------------------------- stage 5
def stage5_cloak():
    """Reduced-cloak numbers: r1=30, r2=90 -> eps_z=(90/60)^2=2.25.
    mu_r clamped at 0.05 -> mu^-1 <= 20 -> max wave speed
    sqrt(20/2.25) ~ 2.98c -> S must stay under 1/(2.98*sqrt(2)) = 0.237;
    courant_frac=0.32 gives S=0.226. The clamp band (mu_r at floor) is
    r in [30, 38.7] — 14% of the shell, the price of stability."""
    print("stage 5 — cloak smoke: bare PEC vs Schurig-reduced cloak")
    CXY, R_PEC, R1, R2 = (252, 280), 30, 30, 90   # PEC flush at the inner wall

    def run_case(build):
        sim = Sim(560, 560, cells_per_lambda=20, courant_frac=0.32, absorb=40)
        if build:
            build(sim)
        sim.add_line_source(64)
        sim.run(3000)
        snap = sim.Ez.copy()
        return snap, sim.envelope()

    _, env_vac = run_case(None)

    def bare(sim):
        materials.pec_disk(sim, *CXY, R_PEC)

    def cloaked(sim):
        materials.pec_disk(sim, *CXY, R_PEC)
        materials.schurig_reduced_cloak_tm(sim, *CXY, R1, R2, mu_r_floor=0.05)

    snap_b, env_b = run_case(bare)
    snap_c, env_c = run_case(cloaked)

    xx = np.arange(560)[:, None] - CXY[0]
    yy = np.arange(560)[None, :] - CXY[1]
    rr = np.hypot(xx, yy)
    ann = (rr >= R2 + 10) & (rr <= R2 + 70)
    rms_b = float(np.sqrt(np.mean((env_b - env_vac)[ann] ** 2)))
    rms_c = float(np.sqrt(np.mean((env_c - env_vac)[ann] ** 2)))
    ratio = rms_c / rms_b
    check("cloak", "scattered-field RMS cloaked/bare", f"{ratio:.3f}", ratio <= 0.75, "<=0.75")

    # diagnostic splits (info, no pass/fail) — feed exp-001 design
    xg = np.arange(560)[:, None] - CXY[0]
    back = ann & (xg < 0)
    fwd = ann & (xg > 0)
    for name, m in [("backscatter half", back), ("forward half", fwd)]:
        rb = float(np.sqrt(np.mean((env_b - env_vac)[m] ** 2)))
        rc = float(np.sqrt(np.mean((env_c - env_vac)[m] ** 2)))
        print(f"  [info] cloak · {name} RMS cloaked/bare = {rc / rb:.3f}")
    sh_box = (slice(CXY[0] + R2 + 15, CXY[0] + R2 + 115), slice(CXY[1] - 20, CXY[1] + 20))
    for name, e in [("bare", env_b), ("cloaked", env_c)]:
        restore = float(np.mean(e[sh_box] ** 2) / np.mean(env_vac[sh_box] ** 2))
        print(f"  [info] cloak · beam-behind-object intensity vs vacuum ({name}) = {restore:.3f}")
    stable = np.all(np.isfinite(snap_c)) and float(np.max(np.abs(snap_c))) < 50
    check("cloak", "tensor run stable", f"max|Ez|={np.max(np.abs(snap_c)):.2f}", bool(stable), "finite, <50")

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 5.4), dpi=150)
    v = 0.9 * np.max(np.abs(snap_b[:180, :]))
    for ax, snap, title in [
        (axes[0], snap_b, "bare PEC cylinder"),
        (axes[1], snap_c, f"same PEC + reduced cloak (−{(1-ratio)*100:.0f}% scattered RMS)"),
    ]:
        ax.imshow(snap.T, cmap=CMAP, vmin=-v, vmax=v, origin="lower")
        for r, ls in [(R_PEC, "-"), (R1, ":"), (R2, ":")]:
            ax.add_patch(plt.Circle(CXY, r, fill=False, ls=ls, lw=1.0, ec="#ffffff", alpha=0.7))
        ax.set_title(title, loc="left", fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
    fig.suptitle("stage 5 — first cloak light (engine validation, not exp-001)",
                 x=0.045, ha="left", fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(os.path.join(HERE, "v5_cloak.png")); plt.close(fig)


# ------------------------------------------------------------------ main
if __name__ == "__main__":
    only = "12345"
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    t0 = time.time()

    if "1" in only:
        stage1_regression()
    if "2" in only:
        stage2_impedance()
    if "3" in only or "4" in only:
        sim_scene, env_scene_ours = _our_small_scene(True)
        _, env_vac_ours = _our_small_scene(False)
        ours_scat = env_scene_ours - env_vac_ours
        lam_small = sim_scene.measure_lambda(y_line=160, x_lo=70, x_hi=260)
        shadow_small = float(
            np.mean(env_scene_ours[156:226, 90:110] ** 2)
            / np.mean(env_scene_ours[156:226, 140:165] ** 2))
        check("ours-small", "lambda (cells)", f"{lam_small:.2f}",
              abs(lam_small - 20.0) <= 0.2, "20.0±0.2")
        env_lib = stage3_fdtd_lib(ours_scat, shadow_small) if "3" in only else None
        env_c = stage4_ceviche(ours_scat) if "4" in only else None

        if env_lib is not None and env_c is not None:
            fig, axes = plt.subplots(1, 3, figsize=(12.6, 3.6), dpi=140)
            for ax, e, title in [
                (axes[0], env_scene_ours, "lab engine (time-domain)"),
                (axes[1], env_lib, "flaport fdtd (time-domain)"),
                (axes[2], env_c, "ceviche (FDFD)"),
            ]:
                ax.imshow((e / np.max(e[ROI]))[ROI].T, cmap="magma", vmin=0, vmax=1.1,
                          origin="lower")
                ax.set_title(title, loc="left", fontsize=9)
                ax.set_xticks([]); ax.set_yticks([])
            fig.suptitle("stages 3+4 — one scene, three independent solvers (|E| envelope, ROI)",
                         x=0.04, ha="left", fontsize=11, fontweight="bold")
            fig.tight_layout(rect=[0, 0, 1, 0.9])
            fig.savefig(os.path.join(HERE, "v34_cross.png")); plt.close(fig)

    if "5" in only:
        stage5_cloak()

    n_fail = sum(1 for r in RESULTS if not r[3])
    print(f"\n{len(RESULTS) - n_fail}/{len(RESULTS)} checks passed in {time.time() - t0:.0f} s")
    sys.exit(1 if n_fail else 0)
