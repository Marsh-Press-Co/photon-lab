"""
exp-000 — Hello Maxwell
=======================
A plane wave hits a dielectric cylinder. Hand-rolled 2D FDTD on a Yee grid —
no solver library, just numpy — so the physics engine itself is the thing we
learn. Renders the scattered field (PNG), the propagation movie (GIF), and a
setup diagram, then runs three quantitative self-checks.

THE PHYSICS ENGINE IN ONE PARAGRAPH
-----------------------------------
Maxwell's curl equations couple E and H: a changing H makes E curl, a changing
E makes H curl. Yee's trick (1966, still the workhorse): stagger E and H in
space by half a cell and in time by half a step, so each field updates from
the freshest copy of the other — leapfrog in time, interlocked grids in space.
We simulate TMz polarization: Ez out of the plane, Hx/Hy in the plane. Three
arrays, two update rules, that's the whole solver.

Units: grid units (dx = 1 cell, c = 1 cell/step / S). Physical mapping:
600 nm wavelength resolved at 20 cells/wavelength -> dx = 30 nm.

Idealizations (stated per lab convention):
  * 2D (infinite cylinder, not a sphere), single CW wavelength
  * lossless, non-dispersive dielectric (eps_r = 4, i.e. n = 2)
  * soft tapered line source, not a TF/SF plane-wave injector -> slight
    wavefront curvature near the domain edges
  * matched graded-loss absorbing bands, not true PML -> ~1% edge reflection
"""

import time
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrow
from PIL import Image

t0 = time.time()
rng_dir = __file__.rsplit("run.py", 1)[0]

# ---------------------------------------------------------------- parameters
LAMBDA_NM = 600.0          # flashlight-ish visible light
CELLS_PER_LAMBDA = 20      # spatial resolution (rule of thumb: >= 15)
DX_NM = LAMBDA_NM / CELLS_PER_LAMBDA          # 30 nm per cell
NX, NY = 720, 440          # domain: 21.6 um x 13.2 um  (36 x 22 wavelengths)
S = 0.99 / np.sqrt(2.0)    # Courant number: 2D stability requires S <= 1/sqrt(2)
N_STEPS = 1400
LAM = float(CELLS_PER_LAMBDA)                 # wavelength in cells
OMEGA = 2.0 * np.pi * S / LAM                 # phase advance per time step

R_CELLS = 40               # cylinder radius = 2 wavelengths = 1.2 um
CX, CY = int(NX * 0.42), NY // 2              # cylinder center
EPS_CYL = 4.0              # relative permittivity -> refractive index n = 2

ABSORB = 36                # absorbing band thickness (cells)
SRC_X = ABSORB + 24        # source line x position
SNAPSHOT_STEP = 1350       # late-time frame used for the hero image

# ------------------------------------------------------------ material grids
# eps_r lives on the Ez grid. One circle of n=2 "glass" in vacuum.
x = np.arange(NX)[:, None]
y = np.arange(NY)[None, :]
eps_r = np.ones((NX, NY))
cyl_mask = (x - CX) ** 2 + (y - CY) ** 2 <= R_CELLS**2
eps_r[cyl_mask] = EPS_CYL

# Absorbing boundaries: conductivity ramps up smoothly (cubic) across a band
# at each edge, applied as a per-step exponential damping of BOTH E and H.
# Matching electric and magnetic loss keeps the band's impedance close to
# vacuum, so the wave enters without bouncing and dies inside.
def damping(nx, ny):
    d = np.zeros((nx, ny))
    ramp = (np.arange(ABSORB, 0, -1) / ABSORB) ** 3   # 1 at wall -> 0 inside
    d[:ABSORB, :] = np.maximum(d[:ABSORB, :], ramp[:, None])
    d[-ABSORB:, :] = np.maximum(d[-ABSORB:, :], ramp[::-1][:, None])
    d[:, :ABSORB] = np.maximum(d[:, :ABSORB], ramp[None, :])
    d[:, -ABSORB:] = np.maximum(d[:, -ABSORB:], ramp[None, ::-1])
    return np.exp(-0.30 * d)

damp_e = damping(NX, NY)
damp_hx = damping(NX, NY - 1)
damp_hy = damping(NX - 1, NY)

# --------------------------------------------------------------- the solver
Ez = np.zeros((NX, NY))
Hx = np.zeros((NX, NY - 1))    # sits between Ez neighbors in y
Hy = np.zeros((NX - 1, NY))    # sits between Ez neighbors in x

# Soft plane-wave line source: drive a vertical line of Ez cells with a
# sinusoid. Raised-cosine turn-on (3 periods) avoids a startup shock; a
# Tukey-style taper at the line's ends softens edge diffraction.
src_y = slice(ABSORB, NY - ABSORB)
n_src = NY - 2 * ABSORB
taper = np.ones(n_src)
edge = 24
win = 0.5 * (1.0 - np.cos(np.pi * np.arange(edge) / edge))
taper[:edge] = win
taper[-edge:] = win[::-1]
RAMP_STEPS = int(3 * LAM / S)

frames = []                  # downsampled field frames for the GIF
FRAME_EVERY = 10
snapshot = None

ce = S / eps_r               # Ez update coefficient (curl H -> dE/dt / eps)
for n in range(N_STEPS):
    # H updates from the spatial differences of Ez (curl E -> -dH/dt)
    Hx -= S * (Ez[:, 1:] - Ez[:, :-1])
    Hy += S * (Ez[1:, :] - Ez[:-1, :])
    Hx *= damp_hx
    Hy *= damp_hy

    # Ez interior update from the curl of H
    Ez[1:-1, 1:-1] += ce[1:-1, 1:-1] * (
        (Hy[1:, 1:-1] - Hy[:-1, 1:-1]) - (Hx[1:-1, 1:] - Hx[1:-1, :-1])
    )

    # drive the source line (soft source: add, don't overwrite)
    envelope = 0.5 * (1.0 - np.cos(np.pi * n / RAMP_STEPS)) if n < RAMP_STEPS else 1.0
    Ez[SRC_X, src_y] += envelope * np.sin(OMEGA * n) * taper

    Ez *= damp_e

    if n % FRAME_EVERY == 0:
        frames.append(Ez[::2, ::2].copy())
    if n == SNAPSHOT_STEP:
        snapshot = Ez.copy()

    # shadow-contrast bookkeeping: time-average |Ez|^2 over the final period
    if n == N_STEPS - int(round(LAM / S)) - 1:
        acc_shadow = np.zeros(())
        acc_ref = np.zeros(())
        acc_n = 0
    if n >= N_STEPS - int(round(LAM / S)):
        sh = Ez[CX + R_CELLS + 20 : CX + R_CELLS + 160, CY - 20 : CY + 20]
        rf = Ez[CX + R_CELLS + 20 : CX + R_CELLS + 160, CY + 120 : CY + 160]
        acc_shadow = acc_shadow + np.mean(sh**2)
        acc_ref = acc_ref + np.mean(rf**2)
        acc_n += 1

if snapshot is None:
    snapshot = Ez.copy()

# ------------------------------------------------------------- self checks
report = []

# 1. Stability: fields finite and bounded
assert np.all(np.isfinite(Ez)), "FDTD blew up (NaN/Inf) — Courant violated?"
report.append(f"stability: max|Ez| = {np.max(np.abs(snapshot)):.3f} (finite, bounded)")

# 2. Wavelength: FFT of Ez along x in a quiet strip should peak at 20 cells
strip = snapshot[80:640, CY + 150]
k = np.fft.rfftfreq(strip.size)
amp = np.abs(np.fft.rfft(strip * np.hanning(strip.size)))
k_peak = k[np.argmax(amp[1:]) + 1]
lam_measured = 1.0 / k_peak
report.append(
    f"wavelength: set {LAM:.1f} cells, measured {lam_measured:.1f} cells "
    f"({DX_NM * lam_measured:.0f} nm vs {LAMBDA_NM:.0f} nm set)"
)

# 3. Shadow: intensity behind the cylinder vs an undisturbed strip
shadow_ratio = float(acc_shadow / acc_ref)
report.append(f"shadow: time-avg intensity behind cylinder / reference = {shadow_ratio:.2f}")

# ------------------------------------------------------------ figure styling
BG = "#0d1117"        # GitHub-dark surface — figures blend into the repo page
INK = "#e6edf3"
MUTED = "#9198a1"
try:
    CMAP = matplotlib.colormaps["berlin"]   # Crameri diverging: blue-black-red
except KeyError:
    CMAP = matplotlib.colormaps["seismic"]

plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": BG,
        "savefig.facecolor": BG,
        "text.color": INK,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": MUTED,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "font.family": "DejaVu Sans",
    }
)

UM_X = NX * DX_NM / 1000.0
UM_Y = NY * DX_NM / 1000.0
extent = [0, UM_X, 0, UM_Y]
vmax = 0.9 * np.max(np.abs(snapshot[: CX - R_CELLS - 10, :]))  # scale off incident field

# ---- hero image: the scattered field ---------------------------------------
fig, ax = plt.subplots(figsize=(10.8, 7.0), dpi=200)
im = ax.imshow(
    snapshot.T, cmap=CMAP, vmin=-vmax, vmax=vmax, origin="lower",
    extent=extent, interpolation="bilinear",
)
ax.add_patch(
    Circle(
        (CX * DX_NM / 1000, CY * DX_NM / 1000), R_CELLS * DX_NM / 1000,
        fill=False, ls="--", lw=1.3, ec="#ffffff", alpha=0.65,
    )
)
ax.annotate(
    f"dielectric cylinder\nn = 2, r = {R_CELLS * DX_NM / 1000:.1f} µm",
    xy=((CX + R_CELLS * 0.72) * DX_NM / 1000, (CY + R_CELLS * 0.72) * DX_NM / 1000),
    xytext=(CX * DX_NM / 1000 - 1.8, UM_Y - 2.1),
    color=INK, fontsize=9.5, ha="center",
    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.9),
)
ax.add_patch(
    FancyArrow(
        0.9, UM_Y / 2, 1.6, 0, width=0.055, head_width=0.32, head_length=0.42,
        color=INK, alpha=0.95,
    )
)
ax.text(0.9, UM_Y / 2 + 0.55, "plane wave\nλ = 600 nm", color=INK, fontsize=9.5)
# scale bar
sb_x0, sb_y = 0.9, 0.85
ax.plot([sb_x0, sb_x0 + 3], [sb_y, sb_y], color=INK, lw=2.4)
ax.text(sb_x0 + 1.5, sb_y + 0.28, "3 µm", color=INK, fontsize=9, ha="center")
ax.set_xticks([])
ax.set_yticks([])
for s in ax.spines.values():
    s.set_visible(False)
cb = fig.colorbar(im, ax=ax, fraction=0.032, pad=0.015, ticks=[-vmax, 0, vmax])
cb.ax.set_yticklabels(["−1", "0", "+1"])
cb.set_label("Ez (normalized)", color=MUTED, fontsize=9)
cb.ax.tick_params(color=MUTED, labelcolor=MUTED)
cb.outline.set_edgecolor(MUTED)
fig.suptitle(
    "exp-000 · Hello Maxwell", x=0.055, y=0.965, ha="left",
    fontsize=17, fontweight="bold", color=INK,
)
ax.set_title(
    "2D FDTD, hand-rolled Yee grid — steady-state Ez, plane wave scattering off a dielectric cylinder\n"
    f"{NX}×{NY} cells · λ/{CELLS_PER_LAMBDA} resolution · Courant S = {S:.3f} · step {SNAPSHOT_STEP}",
    loc="left", fontsize=9.5, color=MUTED, pad=10,
)
fig.text(
    0.055, 0.018,
    "Marsh-Press-Co · Photon Lab · 2026-08-06 · idealizations: 2D TMz, lossless dielectric, CW single-λ, "
    "graded-loss boundaries",
    fontsize=8, color=MUTED,
)
fig.tight_layout(rect=[0, 0.03, 1, 0.94])
fig.savefig(rng_dir + "field.png", bbox_inches="tight")
plt.close(fig)

# ---- setup diagram ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.6, 5.6), dpi=170)
ax.imshow(
    eps_r.T, cmap="gray", vmin=-0.5, vmax=5.0, origin="lower", extent=extent,
    interpolation="nearest",
)
band_um = ABSORB * DX_NM / 1000
ax.fill_betweenx([0, UM_Y], 0, band_um, color="#9198a1", alpha=0.35)
ax.fill_betweenx([0, UM_Y], UM_X - band_um, UM_X, color="#9198a1", alpha=0.35)
ax.fill_between([0, UM_X], 0, band_um, color="#9198a1", alpha=0.35)
ax.fill_between([0, UM_X], UM_Y - band_um, UM_Y, color="#9198a1", alpha=0.35)
ax.axvline(SRC_X * DX_NM / 1000, color="#58a6ff", lw=2, ls=(0, (4, 3)))
ax.text(SRC_X * DX_NM / 1000 + 0.25, UM_Y - 1.7, "source line\n(soft, tapered)",
        color="#58a6ff", fontsize=9)
ax.text(UM_X - band_um - 0.35, band_um + 0.45, "absorbing bands (all edges)",
        color=INK, fontsize=8.5, ha="right")
ax.annotate(
    "ε_r = 4 (n = 2)",
    xy=(CX * DX_NM / 1000, (CY + R_CELLS * 0.75) * DX_NM / 1000),
    xytext=(CX * DX_NM / 1000, UM_Y - 2.2),
    color=INK, fontsize=10, ha="center", fontweight="bold",
    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.9),
)
ax.set_xlabel("x (µm)")
ax.set_ylabel("y (µm)")
ax.set_title("exp-000 setup — domain, materials, source, boundaries",
             loc="left", fontsize=11, color=INK, pad=8)
fig.tight_layout()
fig.savefig(rng_dir + "setup.png", bbox_inches="tight")
plt.close(fig)

# ---- GIF: the wave crossing the domain -------------------------------------
gif_max = 0.9 * vmax
pil_frames = []
ring = None
for f in frames:
    a = np.clip(f / gif_max, -1, 1)
    rgba = (CMAP((a.T + 1) / 2) * 255).astype(np.uint8)
    if ring is None:
        yy, xx = np.mgrid[0 : f.shape[1], 0 : f.shape[0]]
        rr = np.sqrt((xx - CX / 2) ** 2 + (yy - CY / 2) ** 2)
        ring = np.abs(rr - R_CELLS / 2) < 0.9
    rgba[ring] = [255, 255, 255, 255]
    pil_frames.append(Image.fromarray(rgba[::-1, :, :3]))
pil_frames += [pil_frames[-1]] * 25          # hold the final frame ~1 s
pil_frames[0].save(
    rng_dir + "wave.gif", save_all=True, append_images=pil_frames[1:],
    duration=40, loop=0, optimize=True,
)

# ----------------------------------------------------------------- report
dt = time.time() - t0
print(f"exp-000 complete in {dt:.1f} s")
for line in report:
    print("  CHECK  " + line)
print(f"  wrote  field.png, setup.png, wave.gif ({len(pil_frames)} frames)")
