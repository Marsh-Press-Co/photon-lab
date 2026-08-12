"""
lab.fdtd2d — the shared 2D FDTD engine, grown from exp-000.
===========================================================
Same physics core as experiments/000-hello-maxwell/run.py (TMz Yee grid,
leapfrog, graded-loss absorbing bands), generalized with what exp-001 needs:

  * conductivity (sigma_e) — lossy materials, the absorber family
  * PEC regions — perfect conductors (mirrors, the "ordinary reflector")
  * anisotropic magnetic response (2x2 inverse-mu tensor) — REQUIRED by
    transformation-optics cloaks, which steer light with position-dependent
    anisotropic mu. Implemented as the standard B-then-H scheme:
        curl E  ->  update B      (no material involved)
        H = mu^-1 B               (constitutive step, tensor, staggered)
        curl H  ->  update Ez     (eps + sigma)
    With no tensor set, the engine takes the exp-000 fast path (H updated
    directly) and reproduces exp-000 arithmetic exactly.
  * sources with arbitrary lateral profile (plane line / Gaussian beam)
  * Poynting line monitors — time-averaged directed power through a line,
    the "what comes back to the observer" measurement exp-001 is about

Units: grid units (dx = 1, c = 1). courant_frac scales S below the 2D
stability limit 1/sqrt(2); anisotropic runs with mu^-1 > 1 need extra
headroom (see cloak notes in lab/materials.py).
"""

import numpy as np


def spatial_wavelength(strip):
    """Dominant spatial period (cells) of a 1D field strip. Zero-padded FFT
    + parabolic peak interpolation — a raw N-sample FFT can't resolve
    wavelengths between bins (e.g. 190 samples quantizes 20.0 to 19.0 or
    21.1), which matters at our strip lengths."""
    strip = np.asarray(strip, dtype=float)
    n = strip.size
    padded = np.zeros(8 * n)
    padded[:n] = strip * np.hanning(n)
    amp = np.abs(np.fft.rfft(padded))
    m = int(np.argmax(amp[1:]) + 1)
    if 1 <= m < amp.size - 1:
        a, b, c = amp[m - 1], amp[m], amp[m + 1]
        denom = a - 2 * b + c
        m = m + (0.5 * (a - c) / denom if abs(denom) > 1e-30 else 0.0)
    return (8 * n) / m


class PoyntingLine:
    """Time-averaged x-directed Poynting flux through the vertical line at
    x = x0, y in y_slice.  Sx = -Ez * Hy (TMz).  Accumulates every step
    after start_step; mean_flux() returns the per-step average of the
    line-summed flux (positive = net power flowing toward +x)."""

    def __init__(self, x0, y_slice, start_step):
        self.x0 = x0
        self.y_slice = y_slice
        self.start_step = start_step
        self.total = 0.0
        self.n = 0

    def sample(self, sim, step):
        if step < self.start_step:
            return
        # interpolate Hy (lives at i+1/2) onto the Ez line at x0
        hy = 0.5 * (sim.Hy[self.x0 - 1, self.y_slice] + sim.Hy[self.x0, self.y_slice])
        self.total += float(np.sum(-sim.Ez[self.x0, self.y_slice] * hy))
        self.n += 1

    def mean_flux(self):
        return self.total / max(self.n, 1)


class Sim:
    def __init__(self, nx, ny, cells_per_lambda=20, courant_frac=0.99, absorb=36):
        self.nx, self.ny = nx, ny
        self.lam = float(cells_per_lambda)
        self.cells_per_lambda = cells_per_lambda
        self.courant_frac = courant_frac
        self.S = courant_frac / np.sqrt(2.0)
        self.omega = 2.0 * np.pi * self.S / self.lam  # phase advance per step
        self.absorb = absorb
        # Declarative scene record: materials builders and add_line_source
        # append here, so an emitted manifest mirrors what actually ran
        # (single source of truth — no separate scene bookkeeping).
        self.objects = []
        self.source_specs = []

        self.eps_r = np.ones((nx, ny))
        self.sigma_e = np.zeros((nx, ny))       # electric conductivity
        self.pec = np.zeros((nx, ny), dtype=bool)
        self.inv_mu = None                       # set via ensure_inv_mu()

        self.Ez = np.zeros((nx, ny))
        self.Hx = np.zeros((nx, ny - 1))
        self.Hy = np.zeros((nx - 1, ny))
        self.Bx = None                           # allocated when tensor is used
        self.By = None

        self.damp_e = self._damping(nx, ny)
        self.damp_hx = self._damping(nx, ny - 1)
        self.damp_hy = self._damping(nx - 1, ny)

        self.sources = []
        self.monitors = []
        self.step_count = 0

    # ------------------------------------------------------------ materials
    def ensure_inv_mu(self):
        """Switch on the anisotropic-mu machinery (identity tensor).
        Components live at the staggered H locations:
          xx at Hx points (i, j+1/2), yy at Hy points (i+1/2, j),
          xy evaluated separately at both."""
        if self.inv_mu is None:
            self.inv_mu = {
                "xx": np.ones((self.nx, self.ny - 1)),
                "yy": np.ones((self.nx - 1, self.ny)),
                "xy_hx": np.zeros((self.nx, self.ny - 1)),
                "xy_hy": np.zeros((self.nx - 1, self.ny)),
            }
            self.Bx = np.zeros_like(self.Hx)
            self.By = np.zeros_like(self.Hy)

    def _damping(self, nx, ny):
        d = np.zeros((nx, ny))
        ramp = (np.arange(self.absorb, 0, -1) / self.absorb) ** 3
        d[: self.absorb, :] = np.maximum(d[: self.absorb, :], ramp[:, None])
        d[-self.absorb :, :] = np.maximum(d[-self.absorb :, :], ramp[::-1][:, None])
        d[:, : self.absorb] = np.maximum(d[:, : self.absorb], ramp[None, :])
        d[:, -self.absorb :] = np.maximum(d[:, -self.absorb :], ramp[None, ::-1])
        return np.exp(-0.30 * d)

    # ------------------------------------------------------------- sources
    def add_line_source(self, x, y_lo=None, y_hi=None, profile="plane",
                        width=None, ramp_periods=3.0, amplitude=1.0, edge=24,
                        angle_deg=0.0):
        """Soft source on the vertical line at x.
        profile: 'plane' (tapered top-hat) or 'gauss' (beam, needs width =
        1/e half-width in cells).
        angle_deg: launch angle from the x-axis (a phase ramp k·sinθ along
        the line). The −x-going wave then travels along (−cosθ, +sinθ): for
        positive θ it walks toward +y as it propagates toward the observer
        side — the ambient-instrument convention (suite stage 9 gates the
        sign and the λ/cosθ geometry). angle_deg=0 keeps the original
        scalar-sin arithmetic path bit-exact (stage-1 regression)."""
        y_lo = self.absorb if y_lo is None else y_lo
        y_hi = self.ny - self.absorb if y_hi is None else y_hi
        n = y_hi - y_lo
        if profile == "plane":
            p = np.ones(n)
            win = 0.5 * (1.0 - np.cos(np.pi * np.arange(edge) / edge))
            p[:edge] = win
            p[-edge:] = win[::-1]
        elif profile == "gauss":
            yc = 0.5 * (y_lo + y_hi)
            yy = np.arange(y_lo, y_hi)
            p = np.exp(-(((yy - yc) / width) ** 2))
        else:
            raise ValueError(profile)
        if angle_deg:
            k = 2.0 * np.pi / self.lam
            yy = np.arange(y_lo, y_hi, dtype=float)
            phase = k * np.sin(np.radians(angle_deg)) * (yy - 0.5 * (y_lo + y_hi))
        else:
            phase = None
        self.sources.append(
            dict(x=x, sl=slice(y_lo, y_hi), profile=amplitude * p,
                 ramp=int(ramp_periods * self.lam / self.S), phase=phase)
        )
        spec = dict(profile=profile, x=x, y_lo=y_lo, y_hi=y_hi,
                    ramp_periods=ramp_periods, amplitude=amplitude,
                    angle_deg=angle_deg)
        spec["width" if profile == "gauss" else "edge"] = width if profile == "gauss" else edge
        self.source_specs.append(spec)

    def add_poynting_line(self, x0, start_step, y_lo=None, y_hi=None):
        y_lo = self.absorb if y_lo is None else y_lo
        y_hi = self.ny - self.absorb if y_hi is None else y_hi
        m = PoyntingLine(x0, slice(y_lo, y_hi), start_step)
        self.monitors.append(m)
        return m

    # --------------------------------------------------------------- solver
    @staticmethod
    def _avg_by_at_hx(By, out):
        out[...] = 0.0
        out[1:-1, :] = 0.25 * (By[:-1, :-1] + By[1:, :-1] + By[:-1, 1:] + By[1:, 1:])
        return out

    @staticmethod
    def _avg_bx_at_hy(Bx, out):
        out[...] = 0.0
        out[:, 1:-1] = 0.25 * (Bx[:-1, :-1] + Bx[1:, :-1] + Bx[:-1, 1:] + Bx[1:, 1:])
        return out

    def run(self, n_steps, frame_every=None, frame_slice=(slice(None, None, 2),) * 2):
        """Advance n_steps. Returns list of downsampled Ez frames if
        frame_every is set."""
        S = self.S
        frames = []
        # E-update coefficients with conductivity:
        #   alpha = sigma*dt/(2*eps);  Ez <- ca*Ez + cb*curlH
        alpha = self.sigma_e * S / (2.0 * self.eps_r)
        ca = (1.0 - alpha) / (1.0 + alpha)
        cb = (S / self.eps_r) / (1.0 + alpha)
        aniso = self.inv_mu is not None
        if aniso:
            tmp_hx = np.empty_like(self.Hx)
            tmp_hy = np.empty_like(self.Hy)

        for _ in range(n_steps):
            n = self.step_count
            if aniso:
                self.Bx -= S * (self.Ez[:, 1:] - self.Ez[:, :-1])
                self.By += S * (self.Ez[1:, :] - self.Ez[:-1, :])
                self.Bx *= self.damp_hx
                self.By *= self.damp_hy
                self.Hx = self.inv_mu["xx"] * self.Bx + \
                    self.inv_mu["xy_hx"] * self._avg_by_at_hx(self.By, tmp_hx)
                self.Hy = self.inv_mu["yy"] * self.By + \
                    self.inv_mu["xy_hy"] * self._avg_bx_at_hy(self.Bx, tmp_hy)
            else:
                self.Hx -= S * (self.Ez[:, 1:] - self.Ez[:, :-1])
                self.Hy += S * (self.Ez[1:, :] - self.Ez[:-1, :])
                self.Hx *= self.damp_hx
                self.Hy *= self.damp_hy

            self.Ez[1:-1, 1:-1] = ca[1:-1, 1:-1] * self.Ez[1:-1, 1:-1] + \
                cb[1:-1, 1:-1] * (
                    (self.Hy[1:, 1:-1] - self.Hy[:-1, 1:-1])
                    - (self.Hx[1:-1, 1:] - self.Hx[1:-1, :-1])
                )

            for s in self.sources:
                env = 0.5 * (1.0 - np.cos(np.pi * n / s["ramp"])) if n < s["ramp"] else 1.0
                if s.get("phase") is None:
                    self.Ez[s["x"], s["sl"]] += env * np.sin(self.omega * n) * s["profile"]
                else:
                    self.Ez[s["x"], s["sl"]] += env * np.sin(self.omega * n - s["phase"]) * s["profile"]

            self.Ez *= self.damp_e
            if self.pec.any():
                self.Ez[self.pec] = 0.0

            for m in self.monitors:
                m.sample(self, n)

            if frame_every and n % frame_every == 0:
                frames.append(self.Ez[frame_slice].copy())
            self.step_count += 1

        return frames

    # ------------------------------------------------------------ analysis
    def envelope(self, extra_settle=0):
        """|E| envelope from two snapshots a quarter period apart (run must
        already be at steady state). Advances the sim by T/4 (+extra)."""
        snap_a = self.Ez.copy()
        quarter = max(1, int(round(self.lam / self.S / 4.0)))
        self.run(quarter + extra_settle)
        snap_b = self.Ez.copy()
        return np.sqrt(snap_a**2 + snap_b**2)

    def measure_lambda(self, y_line, x_lo, x_hi):
        """Spatial wavelength (cells) along x at row y_line."""
        return spatial_wavelength(self.Ez[x_lo:x_hi, y_line])
