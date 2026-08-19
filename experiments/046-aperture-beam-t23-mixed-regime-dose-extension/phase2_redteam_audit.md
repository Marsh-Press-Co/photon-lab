# PHASE 2 — RED TEAM AUDIT · Panel Iteration 23 · exp-046

*Seventh seat, speaking last, with the Phase-1 proposal and all five blind
critiques. Standard: internal consistency, falsifiability, expressibility,
constraint violations — not textbook compliance. Every load-bearing claim below
was re-derived or re-run from source in this session. Where I checked a seat's
number I say so; where I disagree with a seat I show the work. Scripts used are
listed at the end.*

---

## 0. Headline

The three-way geometry dispute is **not three-way**. EM's and PHOTONICS' closed
forms are **algebraically identical**, and — the thing none of the five seats
found — the **proposal's own §2.1 `w_y` formula is also identical to both**,
*provided* the source `width` is `w₀/cos θ₀`. There is exactly **one** defect in
Block A's geometry, and it is at the **source**, not at the observation plane:
§2.2's FDTD runs 4–9 pass `width = w₀` when the physics the block claims to
build requires `width = w₀/cos θ₀`. §2.1's `w_y` column is *correct as printed*
(bar one transcription slip) and PHOTONICS' verdict that "the sole basis of every
committed Block-A band is wrong and must not be committed to git" is **overturned**.

That good news is bought back with worse news: once the source is fixed,
**P-TH23-A1 and A3 stop being predictions at all**. I prove analytically, and
confirm numerically, that exp-042's `beam_divergence_coherent` **already
synthesises exactly** an along-line Gaussian aperture of 1/e half-width
`w₀/cos θ₀`. So "the aperture-consistent single-mode reading lands on the
coherent column" is an *identity of exp-042's own machinery*, not a physics
claim that could have failed. The proposal's advertised "real, pre-registered
way for this proposal to lose" **cannot fire**.

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** Block A **proceeds this cycle** — the
Iteration-22 hardened rule is satisfied by *running the check*, the geometry
defect is a single-parameter fix I have already derived and FDTD-verified at
zero cost, and the block's real instrument content (gating a never-exercised
engine path; validating the desk propagator at N_F ≈ 0.4–67) survives intact.
Its *headline* must be re-scoped, and bands A1–A5 and A7 rebuilt at Phase 3.

---

## ATTACK 1 — the geometry dispute, resolved from the code [inconsistency]

### 1a. What the code actually implements

Read directly, not via any seat's prose:

- `lab/fdtd2d.py:153-155` — `yc = 0.5*(y_lo+y_hi)`, `yy = np.arange(y_lo,y_hi)`,
  `p = np.exp(-(((yy-yc)/width)**2))`. The Gaussian taper is applied along the
  **fixed vertical line at `x`**. Nothing rotates.
- `lab/fdtd2d.py:158-161` — `if angle_deg:` … `phase = k*np.sin(radians(angle_deg))*(yy - yc)`.
  Steering is a **separate linear phase ramp on that same fixed line**.
- `lab/fdtd2d.py:237` — `self.Ez[s["x"], s["sl"]] += env*np.sin(self.omega*n - s["phase"])*s["profile"]`.
  A real-valued additive soft-source array.

This is a **phased array / leaky-wave aperture** (steer-by-phase-gradient on a
straight aperture), **not** a physically tilted finite aperture. PHOTONICS'
"physically-rotated-aperture" narrative and EM's "phased-array/steered-aperture"
narrative therefore describe the same object; only EM's narrative matches the
code, but as shown below the two happen to agree numerically here.

### 1b. My derivation (angular spectrum, from scratch)

Source field on the line, `Y ≡ y − y_c`:

> `E(Y) = exp(−Y²/w²) · exp(i k sinθ₀ Y)`

Its Fourier transform is a Gaussian recentred on `k_y = k sinθ₀`:

> `A(k_y) ∝ exp(−(k_y − k sinθ₀)² w²/4)`

Far-field intensity in direction θ, via `k_y = k sinθ`:

> `I(θ) ∝ exp(−k²(sinθ − sinθ₀)² w²/2)`

Half-max at `k|sinθ − sinθ₀| w = √(2 ln 2)`. Expanding `sinθ − sinθ₀ ≈ δ cosθ₀`
to first order in `δ = θ − θ₀`:

> **Δθ = 2√(2 ln 2)/(k w cos θ₀) = C·λ/(w cos θ₀), C = 2√(2 ln 2)/2π = 0.374781250**

⇒ to emit divergence `Δθ` you must pass **`width = w₀/cos θ₀`**, `w₀ = C λ/Δθ`.

For the observation plane, expand `k_x = √(k²−k_y²)` about `k_y = k sinθ₀`:
`k_x ≈ k c − tanθ₀·u − u²/(2 k c³)` with `u = k_y − k sinθ₀`, `c = cosθ₀`. The
Gaussian integral then gives, at propagation distance `z` **measured along x**:

> `|E|² ∝ exp(−2(y − z tanθ₀)²/W(z)²)`, **`W(z) = w·√(1 + (z/(z_R,line·cos³θ₀))²)`**,
> `z_R,line = π w²/λ`

Note the `cos³` arises from `d²k_x/dk_y² = −1/(k c³)`; it is **not** a projection
factor, and there is **no** additional `1/cos θ₀` multiplier at the observation
plane. `z` is `D_SP = 223`, not `D_SP/cos θ₀`.

### 1c. The three seats are two seats, and the proposal is the third

- **EM's form** `w₀√(1+(z_eff/(z_R cos²θ₀))²)` with `z_eff = D_SP/cosθ₀` is
  `w₀√(1+(D_SP/(z_R cos³θ₀))²)` — **identical to PHOTONICS' form, term for
  term.** They are the same equation in two vocabularies. QUANTUM measured the
  same effect without committing to a form. There is no three-way disagreement.
- **The proposal's form** `w₀√(1+(z_eff/z_R)²)/cosθ₀`. Substitute the corrected
  source width `w_line = w₀/c` into *my* form: `z_R,line = z_R/c²`, so
  `W = (w₀/c)√(1+(D_SP c²/(z_R c³))²) = (w₀/c)√(1+(D_SP/(z_R c))²)
  = w₀√(1+(z_eff/z_R)²)/c` — **exactly the proposal's printed formula.**

**So §2.1's `w_y` column is the correct closed form for the corrected
convention.** The proposal made *one* error (source width), and its
observation-plane algebra is the right partner to the *fixed* source. Three seats
diagnosed two errors and mislocated one of them.

### 1d. Numerical verification (`geom_check.py`)

Exact non-paraxial angular-spectrum propagation (`k_x = √(k²−k_y²)`, evanescent
clipped, N = 2²⁰) of the exact aperture over `Δx = 223`, all 36 cells:

| formula | max rel. err vs exact | mean |
|---|---|---|
| proposal, `width = w₀` | **30.41 %** | 17.22 % |
| EM | 7.63 % | 1.70 % |
| PHOTONICS | 7.63 % | 1.70 % |
| my derivation | 7.63 % | 1.70 % |

(The residual 7.6 % is entirely the FWHM = 20° row, where `w₀ = 1.074 λ` and
paraxiality fails; ≤ 0.15 % at FWHM ≤ 5°.)

Emitted-divergence check (`far_field_fwhm`): with `width = w₀/cosθ₀` the measured
FWHM is **2.0003°** at nominal 2° and **20.28–20.34°** at nominal 20° — the
`1/cos θ₀` relation confirmed to 0.02 % where paraxiality holds.

### 1e. Verification in the ACTUAL ENGINE (`fdtd_geom.py`) — the tiebreaker

I ran `lab.fdtd2d.Sim` on exp-041/042's committed geometry (NX 360, NY 1584,
SRC_X 300, STEPS 1400, cpl = 20, θ₀ = 40°), `profile="gauss"`, and measured the
1/e² half-width of `lab.ambient.observer_profile` at `PLANE_X`:

| FWHM | `width` passed | **FDTD measured** | angular spectrum | closed form | proposal §2.1 `w_y` |
|---|---|---|---|---|---|
| 10° | `w₀` = 42.947 | **87.25** | 86.01 | 85.16 (EM/PHOT/mine) | 79.47 ❌ (−8.9 %) |
| 10° | `w₀/c` = 56.063 | **80.47** | 80.56 | 79.47 | **79.47 ✓ (1.3 %)** |
| 5° | `w₀` = 85.894 | **93.26** | 93.81 | 93.43 (EM/PHOT/mine) | 115.61 ❌ (+24 %) |
| 5° | `w₀/c` = 112.126 | **115.23** | 115.73 | 115.61 | **115.61 ✓ (0.3 %)** |

Measured beam peak: y = 978–982 vs ray-optics 979.1 — pointing is fine, as
PHOTONICS said. **The engine confirms: fix the source width, keep `w_y`.**

**Adjudication.** Adopt `width = w₀/cos θ₀` (EM's flip, QUANTUM's flip, and
PHOTONICS' second flip paragraph — all three, unanimously, are right about the
source). Keep §2.1's `w_y` formula unchanged. Reject PHOTONICS' demand that the
envelope model be struck, and reject EM's characterisation that §2.1 "assumes the
reverse" — it does not; it assumes the fix that §2.2 failed to apply.

---

## ATTACK 2 — P-TH23-A1/A3 are algebraic identities, not predictions [unfalsifiable]

Nobody stated this. QUANTUM came closest (steel-manning it as a *correct claim*);
it is worse than correct — it is *unfalsifiable*.

**Analytic proof.** `beam_divergence_coherent` (`042/design_geometry.py:337-355`)
forms `E_tot = Σ_i √w_i · (G @ _src_amp(θ_i))`. By linearity of `G`, the effective
aperture is `P(Y)·Σ_i √w_i e^{i k sinθ_i Y}`. The weights are Gaussian in θ with
`σ_θ = FWHM/2.3548` (`:313`), so `√w` is Gaussian with `σ' = σ_θ√2`. Then

> `Σ_i √w_i e^{i k sinθ_i Y} ≈ e^{i k sinθ₀ Y}∫exp(−(θ−θ₀)²/2σ'²)e^{i k cosθ₀(θ−θ₀)Y}dθ
>   ∝ exp(−k²cos²θ₀ σ'² Y²/2) = exp(−(Y/(1/(k cosθ₀ σ_θ)))²)`

1/e amplitude half-width `= 1/(k cosθ₀ σ_θ)`. And `w₀ = 2√(2ln2)/(k Δθ)
= 2√(2ln2)/(2.3548 k σ_θ) = 1.0000085/(k σ_θ)`. Hence

> **effective aperture half-width = w₀/cos θ₀, to 1 part in 10⁵.**

**Measured** (`block_a_check.py`, part A, all 36 cells): 0.07–1.3 % of `w₀/cosθ₀`
at FWHM ≤ 10°, 3.5–5.7 % at FWHM = 20° (taper truncation). Confirmed.

**Consequence.** exp-042's "coherent" column *is* the diffraction-limited
single-mode reading, already, since Iteration 19. Block A's headline —
"the aperture-consistent reading lands on the coherent column, not the incoherent
one" — is a one-line algebraic fact about `gaussian_angle_weights`, decidable at
the desk, with no run of any kind. §4's closing paragraph ("a real,
pre-registered way for this proposal to lose") is therefore **not true**: the
stated way to lose cannot occur. QUANTUM's Iteration-20 conjecture was not
refuted by evidence; it was mis-posed.

This does **not** kill Block A. It kills Block A's *advertised finding*. See
Docket item 5.

---

## ATTACK 3 — P-TH23-A3 is falsified before the run under BOTH conventions [inconsistency]

I recomputed the full 36-cell grid with exp-042's own propagator
(`block_a_check.py`, `docket.py`), corrected E/H convention, single angle:

| `width` | cells > 3 % vs committed `C_coherent`, FWHM ≤ 10 (27) | worst |
|---|---|---|
| `w₀` (as §2.2 writes it) | **16/27** | 966 % |
| `w₀/cos θ₀` (the fix) | **2/27** | 9.2 % |

I reproduce QUANTUM's 16/27 and EM's "11 of 27 within 3 %" exactly. But the fix
does not save A3, because A3's *second* clause then fires:

> A3 commits "**5–20 %** divergence at the FWHM = 20° cells", hard-falsified if
> "the FWHM = 20 divergence is < 2 %".

Measured under the fix, the nine FWHM = 20° divergences are
**0.11, 0.69, 0.74, 0.79, 0.94, 1.03, 1.12, 1.50, 2.52 %** — **0 of 9 in [5,20]**
and **8 of 9 below 2 %**. A3's hard-falsification clause **fires pre-run**.
(QUANTUM said 7/9; I get 8/9.)

So A3 is falsified with `width = w₀` (clause 1) and falsified with
`width = w₀/cosθ₀` (clause 2). A pre-registered band that fails under every
available convention is not a prediction. **Rewrite or drop.**

**P-TH23-A4 dies with it.** A4 exists only to explain the FWHM = 20° divergence
as 41-point angular aliasing. There is no divergence to explain (0.1–2.5 %, i.e.
*smaller* than several FWHM ≤ 10 residuals), so A4's premise is false and its
"monotone degradation with FWHM" band fails.

**Denominators.** PHOTONICS, EM, QUANTUM and I all confirm independently: the
grid is 3λ × 3θ₀ × 4 FWHM (`042/run.py:89-91`), so the FWHM ≤ 10° / FWHM = 20°
partition is **27/9**, not the committed "24"/"12". Load-bearing — they are the
denominators of a pass/fail band.

---

## ATTACK 4 — P-TH23-A2's primary clause is pre-falsified [inconsistency]

Envelope model `b(y) = exp(−2(y−y_peak)²/w_y²)` vs the actual Block-A reading
(exp-042 propagator, corrected E/H, `width = w₀/cosθ₀`), reduced through
`lab.ambient.window_means`/`weber`, 36 cells (`docket.py`):

- `≤ 5 %` at **26/36** — A2 commits "**≥30/36**". **Fails.**
- `> 10 %` at **3/36** — A2's hard clause needs > 6. **Does not fire.**
- worst 12.0 %, median 1.14 %. Per-FWHM worst: 2° 7.4 %, 5° 1.9 %, 10° 2.1 %,
  **20° 12.0 %**.

The cause is *not* PHOTONICS' misplaced obliquity (that is fixed). It is that the
pure-Gaussian envelope omits (i) the peak shift — exact propagation puts the
FWHM = 20° peak at y ≈ 143–162 off-centre where ray optics says 162–187, a
**26-cell error** at 450 nm/40° (`geom_check.py` Test 2, `peak_y` vs `walk`
columns) — and (ii) the propagator's own `1/√r` and `cos ψ` weighting across a
526-cell scored span. Both are absent from the envelope by construction and
neither is fixable by adjusting `w_y`.

---

## ATTACK 5 — structural ruling: replace the closed form with a numerical desk propagation

The Director's choice is (a) patch the closed form or (b) compute the actual
aperture numerically once and set fresh bands from it. **I rule (b)**, on this
program's own precedent and on cost:

1. **The machinery already exists and is already committed.**
   `042/design_geometry.py:237-265` (`_G0_for`, `field_and_h`) is a
   zero-free-parameter Huygens–Fresnel propagator built at Iteration 19 for
   exactly this purpose. Block A already reduces through it. Substituting the
   Gaussian aperture for `P` is a **one-line change** to `_src_amp`.
2. **Cost is nil.** I evaluated all 36 cells in ≈ 1 s on this box. exp-046's own
   cost note budgets "a few seconds" for 144 propagator evaluations.
3. **The closed form is provably insufficient for the scored observable.** It is
   accurate to ≤ 0.15 % (FWHM ≤ 5°) / ≤ 3.1 % (FWHM = 20°) **as a width**, but
   the scored observable is a Weber contrast between two windows sitting in the
   beam's exponential wing, where a 3 % width error and a 26-cell peak error
   are amplified into the 12 % seen in Attack 4.
4. **T21's own precedent binds.** exp-042 built a numerical propagator rather
   than trusting hand-derived edge-diffraction algebra, and its Phase-5 erratum
   is a record of what happens when a hand-derived convention is trusted
   (obliquity squared into `|E|²`). Repeating the hand-derivation route in the
   very cycle that corrects exp-042 would be a self-inflicted regression.
5. **Pre-registration is not weakened.** The house rule is *predictions committed
   to git before the run*. The FDTD legs remain the genuine test; the desk
   propagator's numbers become the committed prediction they are scored against
   (that is precisely what P-TH23-A5 already does). Nothing falsifiable is lost —
   and as Attacks 2–4 show, the "prediction rather than pre-computed answer"
   framing in §4 is not accurate today anyway: A3's committed bands are the
   residuals of a comparison the proposal already had in hand (PHOTONICS'
   defect 3; I reproduce his 0.1–2.8 % / 5.3–14.2 % figures exactly).

Retain the closed form **as a disclosed sanity anchor** with its measured
accuracy stated (≤ 0.15 % / ≤ 3.1 % in width vs exact angular spectrum; ≤ 1.3 %
vs FDTD at the two points I measured). Do not let it set a band.

---

## ATTACK 6 — idealization 4's truncation numbers are wrong under BOTH conventions [inconsistency]

Nobody got this fully. MATERIALS caught half of it (the aimed 450 nm cells sit at
≈ 3.5 w₀, outside the stated "2.10–2.75 w₀"); I confirm 3.51–3.66 w₀ under the
*unfixed* convention. Under the **fix**, which the Director is about to adopt,
the numbers move the *other* way and get worse (`docket.py`):

| | proposal claims | actual under `width = w₀/cosθ₀` |
|---|---|---|
| unaimed rim residual, amplitude (750 nm/FWHM 2°) | ≤ 3.90×10⁻⁴ | **9.99×10⁻³** (25× worse) |
| unaimed rim residual, intensity | ≤ 1.52×10⁻⁷ | **9.98×10⁻⁵** (657× worse) |
| aimed-leg truncation | 2.10–2.75 w₀ | **1.61–2.96 w_line** |
| aimed-leg rim amplitude | ≤ 1.19×10⁻² | **≤ 7.43×10⁻²** |

"Four-plus orders below anything `C_THR` can see, so no new hard-edge fringe is
smuggled in" becomes ~1.0×10⁻⁴ in intensity against `C_THR = 0.005` — still
below, but the margin claimed in the idealization is gone, and at 750 nm/FWHM 2°
the *aimed* leg now truncates a 7.4 %-amplitude Gaussian on a hard rim. Restate
idealization 4 with the corrected numbers, and re-justify (or drop) the aimed leg
at the FWHM = 2°/750 nm cells.

---

## ATTACK 7 — P-TH23-A1 is a pointing tautology, not a coherence test [unfalsifiable]

EM and PHOTONICS both found this; I reproduce it independently and confirm
QUANTUM's numbers to the digit (`docket.py`): with `width = w₀/cosθ₀`, unaimed,
**36/36 above `C_THR`**, **35/36 above the 20× clause**, **min |C| = 0.0323**.

The beam axis lands at 792 + 162…187 while the object window is |y−792| ≤ 78 and
the flank windows are 185 ≤ |y−792| ≤ 263 (`lab/ambient.py:42-50`). The object
window sits in the beam's exponential wing and the +flank window sits *under the
beam*. `B_obj ≪ B_flank` forces `C → −1` regardless of coherence, aperture, or
wavelength. A1 measures where the beam points. VISION's related catch is also
right: A1's "≥34/36" band is looser than its own predictor's already-computed
36/36, the RT2 pattern from Iteration 17.

---

## ATTACK 8 — A3's target column is under a superseded convention [inconsistency]

Verified directly against `042/results.json`: `phase5_erratum.block_beam_corrected.rows[i]`
carries **only** `C_incoherent` (keys: `lambda_nm, theta0, fwhm_deg, C_incoherent,
incoherent_above_thr`) — 36 rows, no coherent column. And
`beam_divergence_coherent` (`042/design_geometry.py:349`) calls
`_G_for(lam_cells, True)`, i.e. the **superseded obliquity-on-E** recipe the
erratum itself names "not a methodologically legitimate combination". §6 declares
corrected E/H primary. A3 therefore compares a corrected-convention reading to a
superseded-convention target. I measure the convention shift at up to ~3 % of the
value at 600 nm/38°/2° (E: −0.031295 vs E/H: −0.032270) — the whole of A3's 3 %
band. EM and QUANTUM both flagged this; upheld.

---

## ATTACK 9 — Block C has zero UNOBTANIUM points *and* zero positive controls [constraint-integrity]

MATERIALS' M1, independently verified and sharpened. From
`experiments/038-t17-rate-equation-kernel/run.py:24-46`:

```
HOSTS   = [("A",1e9),("B",1e6),("C",1e3),("D",1e1),("E",1e0)]
RATIOS  = [1e-9,1e-5,1e-3,1e-1,1.0]
realizability_tier: host=="E" -> UNOBTANIUM ; r>=1.0 -> UNOBTANIUM ; ...
```

Block C's C1 grid is Hosts A/B/C × r ∈ {1e-9,1e-5,1e-3,1e-1} — it excludes
**every** UNOBTANIUM point in exp-038's grid (all of Host E, all of r = 1.0).
P-TH23-C4 claims those 12 combos "corroborat[e] `REALIZABILITY_MEMO.md`
Amendment 3", whose finding is memory "*only* at Hosts D **and E**". A grid
without E cannot corroborate a finding about E.

**Sharper than MATERIALS put it:** every one of C1's 24 points is a *negative*
control — P-TH23-C1 itself predicts `|ratio − 1| ≤ 1×10⁻¹²` at **24/24**, because
`D/τ_k ≥ 66.7` everywhere in the grid. The block contains **no cell in which
memory can appear at all**. Host E at r ≤ 1e-3 gives `τ_k ≈ 1 s`, `D/τ_k ≈ 0.067`
— deep inside C2's own memory criterion `D/τ_k < 2.54` — and is the single point
that would exercise the positive branch at a second host. Adding Host E and the
r = 1.0 column (18 extra closed-form points, microseconds) converts C1 from an
all-negative-control grid into a real test **and** brings the Iteration-22
Tier-1 #3 wording ("closing … in full") within reach. **M1 upheld as binding.**

---

## ATTACK 10 — P-TH23-C3 is not implementable as written [inexpressible]

Caught by no seat. `lab/kinetics.py:201-219`:

```
def pulse_train_segments(k_f_ambient, k_r, A, T_pulse, dt_sweep, n_pulses):
    for _ in range(n_pulses):
        segs.append((k_f_ambient, k_r, dt_sweep))     # <- ON dwell
        segs.append((k_f_pulse,   k_r, T_pulse))      # <- OFF gap (A=0.0)
```

exp-045 Block C (`045/run.py:545-549`) passes `T_pulse=dt_gap`,
`dt_sweep=dwell_central` — the **disclosed role inversion**: `T_pulse` **is the
gap**, `dt_sweep` is the ON dwell `D`. exp-046 §2.4 declares the convention held
"**identical** to exp-045 Block C" and then specifies C3 as
"16 host/ratio points × **T_pulse ∈ {1 ms, 10 ms, 66.7 ms, 100 ms, 1 s}** × **2
gaps**". Under exp-045's own inversion, `T_pulse` and "gap" are the **same
slot**, assigned two contradictory value sets. The scan is not executable as
specified.

It also breaks C6: C6's committed band is on `D/τ_k`, which under a literal
reading of C3 is *held fixed* at `dwell_central = 0.0667 s` for all 160 points,
so the scan could not move the criterion it is committed to test. Fix: state
explicitly that the scanned duration is **`dt_sweep`** (the ON dwell `D`), gaps
remaining 5τ_k/0.5τ_k. With that reading C3/C6 are coherent — and MATERIALS' M2
also stands: with the reading fixed, the band is *entailed* by C2's algebra, so
C3 is a verification, not a test.

---

## ATTACK 11 — the "eye-invisible" claim [unfalsifiable] · VISION upheld in full

§1 and P-TH23-B3 both carry "eye-invisible" as a scored claim whose entire
falsification band is `NETD_lo/dt_ss ∈ [600,615]` and Wien `∈ [9.87,9.90]` — two
detector/radiometric quantities. There is no perceptual falsifier, so the
perceptual half of the claim cannot fail. `lab/thermo_sidecar.py:193-215` states
in terms that "NETD IS AN INSTRUMENT/DETECTOR THRESHOLD, NOT A HUMAN PERCEPTUAL
ONE … No caller should read 'DETECTABLE' from this function as a constraint-3
finding" — and B3 reads exactly that, in the opposite direction. The §6 deferral
of VISION's sidecar cites the fabricated-PMMA lesson to justify not producing
unsourced perceptual numbers, and §1 then produces an unsourced perceptual
verdict. **Strike "eye-invisible" from §1 and B3.** This is a Checkpoint-4-shaped
defect (a constraint-3 claim smuggled in through a thermal metric) and I am
treating it as mandatory, not advisory.

## ATTACK 12 — idealization 9 hardens the one locus that already works · VISION upheld

Verified: `lab/thermo_sidecar.py:215` already returns a `"disclaimer"` key from
`netd_disposition`, so per-point storage is automatic unless a caller strips it.
Idealization 9 commits to storage and names neither locus that has actually
failed twice (NOTES.md prose; `run.py` console prints) nor point-of-claim
inlining (Iteration 21 mandatory fix 6) — and §1/§4 breach point-of-claim at B3,
B5, C1, C3, C4 in this very document. Upheld.

Related, and also upheld: VISION's item 2. `042/run.py:41` reads in full
`C_THR = 0.005  # VISION's T2 photopic C_thr -- context only, this leg scores no
perceptual pass/fail`. §2.0 imports the value and drops the disclaiming half of
its own source line, then P-TH23-A1 *scores* against it. Carry the comment
verbatim.

---

## ATTACK 13 — the silicon provenance chain terminates unsourced · MATERIALS M3 upheld

Traced myself, not via MATERIALS' prose. `exp-046 §2.3` → "(sourced:
`experiments/037-.../NOTES.md:828-829`)" → that line reads *"Using silicon's
standard **cited** thermal constants (ρ≈2330 kg/m³, c_p≈700 J/(kg·K), κ≈148
W/(m·K))"* → `grep -rn "2330\|148 W\|10.1063\|doi\|DOI\|Handbook\|CRC"` over
`experiments/037-*/` returns **two lines, both that same sentence**. No DOI, no
reference, nothing. The word "cited" points at nothing. The values are correct
for bulk crystalline Si — this is *not* a repeat of the fabricated-PMMA defect —
but idealization 6's standard is a *provenance* standard and it cannot detect a
self-referential chain. **Label ASSUMED — provenance terminates unsourced (T18).**

**MATERIALS' M4 corroborated from a second direction:** `netd_disposition`
carries an explicit `fill_factor` multiplier (`lab/thermo_sidecar.py:190-201`)
that exp-045 and exp-046 both leave silently at 1.0 while `mass = ρ_Si·L³` assigns
100 %-fill crystalline silicon to what the same module calls a dilute
vapour/aerosol host. Since `τ_th ≈ ρ C_P L²/k_air`, §2.3's structural claim that
the "below vs above 25" question "is decided by the conduction length **alone**"
is wrong as stated — it is decided by `ρ C_P L²/(4εσT³L + k_air)`, and the `ρ C_P`
half is the unsourced half. Add the sensitivity row.

---

## ATTACK 14 — confirmed small slips, adjudicated

| slip | ruling |
|---|---|
| §2.1 `w_y(450 nm, FWHM 2°) = 199.33` | **PHOTONICS is exactly right**: it is that formula's **θ₀ = 36°** value in a θ₀ = 40° column (θ₀ = 40° gives 210.54). All 5 seats flagged it; only PHOTONICS diagnosed it. **MATERIALS' reasoning is wrong** — "impossible by construction, below the `w₀/cos40° = 210.24` floor" holds only under the un-fixed convention; under the fix 199.33 is a perfectly legal number, just for the wrong angle. |
| `C = 0.3747808…` | Should be **0.374781250259**. The proposal's 7th significant figure is wrong (rel. 1.2×10⁻⁶). Harmless at A0's 6-s.f. gate but it contradicts §2's own "Nothing is asserted from memory", and the trailing ellipsis asserts precision the digits do not have. MATERIALS right. |
| §1 "N_F falls to 0.32–40.7" vs §2.1's 0.24–39.6 | Confirmed; §1 quotes the FDTD-leg subset. Under the fix **both are superseded** — see Docket 3. |
| idealization 2 "waist is only 1.07–1.34 λ" | `w₀/λ = C/Δθ` is λ-independent: **1.0737 λ, one value**. PHOTONICS/EM/MATERIALS/VISION all right. Also: this means Block A's 3-λ sweep carries **no material wavelength dependence** beyond fixed cell geometry — worth stating rather than presenting as a λ-sweep result (PHOTONICS). |
| §2.4 `ln(21·e^{−0.5}) = 2.5443` | **2.5445224**. MATERIALS/VISION right; immaterial to C6's ±0.05 band. |
| C5's "agreement 2.6×10⁻⁷" | The 5τ points agree to ~2×10⁻¹⁵ (MATERIALS' table, reproduced by VISION); 2.6×10⁻⁷ is an artefact of comparing the proposal's own 7-s.f. rounding. Band still safe. |
| C6's 5τ supremum 1.006784 | That is the `r ≪ 1` value; at `r = 1e-1`, `f = e^{−5/1.1}` gives sup **1.010711** and the 0.5τ threshold **2.590**, at the very edge of the committed 2.54 ± 0.05. PHOTONICS right — widen or scope. |
| EM's cross-platform ≤1×10⁻¹² gate on S16-c | Upheld. A 1400-step FDTD bit-reproducibility claim must name its reference platform or be restated as relative. |
| A7's conditioning | Upheld. My propagator run gives runs 8/9 at `C_empty` = −0.9967 / −0.9866, so `(1+C)` = 3.3×10⁻³ / 1.3×10⁻², amplifying error **77–300×**. EM's "~360×" is right in magnitude. Drop A7 or widen by that factor. |

---

## ATTACK 15 — the corrected-convention analytic profile is globally negative [latent trap]

Found by no seat. `edge_diffraction_c_empty_corrected` uses
`Sx = -np.real(E*np.conj(H))` (`042/design_geometry.py:274`) and calls it "the
time-averaged Poynting flux". I ran it: at θ = 0° the profile spans
**[−25.54, −2.01]** and at θ = 40° **[−34.90, −2.2×10⁻⁴]** — **negative at every
cell**, while its FDTD counterpart `lab/ambient.py:36-39`
(`observer_profile = −flux_profile_x`) is positive.

**No committed number is wrong**: `weber` is invariant under a global sign flip
of `b`, since `(−a+b)/(−b) = (a−b)/b`. But it is a live trap for exp-046
specifically, because §4's envelope model `b(y) = exp(−2(…)²/w_y²)` is
*positive* and P-TH23-A2/A5 compare envelope, propagator and FDTD readings.
**Mandatory guard:** Block A compares only `weber`-reduced scalars; it must never
compare `B(y)` profiles cell-by-cell, take a ratio of two `B`s, or feed the
analytic `B` into `incoherent_sum` alongside an FDTD `B`. Recommend a one-line
docstring correction in exp-042's propagator at Phase 3 (documentation only, no
number moves).

---

## ATTACK 16 — the corrected §2.1 table (handed to the Director)

`width_line = w₀/cos θ₀`, θ₀ = 40° column, `z_R,line = π w_line²/λ`,
`N_F = (2 w_line)²/(λ z_eff)` (`docket.py`):

| λ (nm) | FWHM° | w₀ | **w_line** | 2w_line | 1504/(2w_line) | z_R,line | **w_y** | **N_F** (was) |
|---|---|---|---|---|---|---|---|---|
| 450 | 2 | 161.05 | **210.24** | 420.47 | 3.58× | 9257.1 | 210.54 | **40.49** (23.76) |
| 450 | 5 | 64.42 | **84.09** | 168.19 | 8.94× | 1481.1 | 88.69 | **6.48** (3.80) |
| 450 | 10 | 32.21 | **42.05** | 84.09 | 17.88× | 370.3 | 70.29 | **1.62** (0.95) |
| 450 | 20 | 16.11 | **21.02** | 42.05 | 35.77× | 92.6 | 114.61 | **0.40** (0.24) |
| 600 | 2 | 214.73 | **280.32** | 560.63 | 2.68× | 12342.8 | 280.54 | **53.98** (31.68) |
| 600 | 5 | 85.89 | **112.13** | 224.25 | 6.71× | 1974.8 | 115.61 | **8.64** (5.07) |
| 600 | 10 | 42.95 | **56.06** | 112.13 | 13.41× | 493.7 | 79.47 | **2.16** (1.27) |
| 600 | 20 | 21.47 | **28.03** | 56.06 | 26.83× | 123.4 | 116.10 | **0.54** (0.32) |
| 750 | 2 | 268.42 | **350.39** | 700.79 | 2.15× | 15428.5 | 350.57 | **67.48** (39.60) |
| 750 | 5 | 107.37 | **140.16** | 280.32 | 5.37× | 2468.6 | 142.96 | **10.80** (6.34) |
| 750 | 10 | 53.68 | **70.08** | 140.16 | 10.73× | 617.1 | 89.91 | **2.70** (1.58) |
| 750 | 20 | 26.84 | **35.04** | 70.08 | 21.46× | 154.3 | 117.98 | **0.67** (0.40) |

Consequences the Director must carry through:

- `z_R` is now **θ₀-dependent** and can no longer be a single column.
- The N_F range becomes **0.40 – 67.5** at θ₀ = 40°, not 0.24 – 39.6 (and not
  §1's 0.32 – 40.7). The FDTD legs' labels all move.
- The aperture-narrowing span becomes **2.15× – 35.8×** at θ₀ = 40°, not
  2.80× – 46.69×. §2.1's boast that this "brackets LOGBOOK's T21 3–30× citation"
  must be restated: 2.15× is now further outside 3× at the low end. (The T21
  source, `LOGBOOK.md:1045`, says "3–30× smaller".)
- `w_y` is **unchanged** — the one column that survives.

---

## OVERALL RULING

# PROCEED-WITH-MANDATORY-FIXES

**Why Block A proceeds rather than being cut.** The Iteration-22 close's hardened
rule (`LOGBOOK.md:8324-8329`) is that QUANTUM's aperture-consistent
single-coherent-mode beam check "**MUST run** at Iteration 23, by any lead seat",
with criterion 4 firing automatically otherwise. The rule binds *the running of
the check*, not the survival of any particular predicted band. The defect I found
is a **single mis-set argument** — `width = w₀` where the physics requires
`w₀/cos θ₀` — which I have derived from the code, verified against exact
angular-spectrum propagation, and verified in the **actual FDTD engine** at two
parameter points. It costs nothing to fix and it leaves the check's physical
content wholly intact: a genuine aperture-consistent single-mode beam, correctly
built. Cutting Block A over a fixed-at-Phase-3 parameter would fire criterion 4
for a defect that was found and repaired inside the process the panel exists to
run. That would be the wrong lesson.

**Why it does not proceed unchanged.** Its headline (A1/A3) is an identity, three
of its seven bands (A2, A3, A4) are falsified before the run, one (A1) is a
pointing tautology, and one (A7) is ill-conditioned by ~300×. Those are rebuilt
at Phase 3, not deferred to Phase 5.

**Scope re-statement Block A must adopt.** Block A's honest deliverable this cycle
is **instrument work, not a coherence finding**: (i) first-ever trust-gating of
`profile="gauss"`, an engine path with zero call sites repo-wide (I re-confirmed
the grep); (ii) validation of exp-042's desk Huygens–Fresnel propagator against
FDTD at Fresnel numbers 0.4–67 where it has never been checked; (iii) a
desk-computed, correctly-apertured single-mode reading of the 36-cell grid. The
claim "the aperture-consistent reading lands on the coherent, not the incoherent,
column" is recorded as an **algebraic identity of `beam_divergence_coherent`
(Attack 2), demonstrated at the desk**, not as an experimental result — and
QUANTUM's Iteration-20 conjecture is recorded as **mis-posed**, not as refuted.

**Constraint check.** No target constraint is violated or quietly dropped: §3's
"T1 escape route NONE" is honest (verified — `add_line_source` only appends to
`Sim.sources`; no material law, no update coefficient, no σ moves), and no
constraint-3/4 verdict is issued. The one constraint-3-shaped leak is Attack 11's
"eye-invisible", which the docket strikes. **Criterion 4 is NOT fired by this
audit** — but Attack 11 is the kind of leak that fires it if it recurs, and
Attack 9 is a realizability claim the proposed data cannot support.

---

## MANDATORY-FIX DOCKET (adoptable verbatim at Phase 3)

**Block A — geometry (the adjudicated dispute)**

1. **Source width.** Every oblique Block-A call — §2.2 runs 4–9 and every
   analytic cell — passes
   **`width = w₀/cos θ₀ = 0.374781250·λ_cells/(Δθ_rad·cos θ₀)`**.
   Derivation: Attack 1b. Verified: exact angular spectrum (emitted FWHM 2.0003°
   at nominal 2°) and FDTD (Attack 1e). Runs 4–9's `width` args become
   280.32 / 56.06 / 28.03 / 350.39 (750 nm/38° uses cos 38°: 340.63).
2. **Observation-plane width.** **Keep §2.1's `w_y = w₀√(1+(z_eff/z_R)²)/cos θ₀`
   unchanged** — it is exactly EM's form, exactly PHOTONICS' form, and exactly my
   derivation, once fix 1 is applied (Attack 1c). Correct the single transcription
   slip: `w_y(450 nm, FWHM 2°, θ₀ = 40°) = **210.54**`, not 199.33 (199.33 is the
   θ₀ = 36° value). Overrule PHOTONICS' demand to strike the envelope formula.
3. **Re-issue §2.1's table** per Attack 16: `w_line`, θ₀-dependent `z_R,line`,
   `N_F` = 0.40–67.5, aperture ratio 2.15×–35.8×. Restate the T21 "3–30×"
   comparison against the new span. Reconcile §1's 0.32–40.7 with the table.
4. **Replace the closed-form envelope as band-setter** with a desk evaluation of
   the ACTUAL complex aperture `exp(−(Y/w_line)²)·exp(i k sinθ₀ Y)` through
   exp-042's own committed propagator (`_G0_for` + `field_and_h`, corrected E/H),
   reduced through `lab.ambient.window_means`/`weber` — computed once, committed
   to git, and used to set fresh A1–A5/A7 bands. Cost ≈ 1 s for all 36 cells.
   Retain the closed form as a disclosed anchor with its measured accuracy
   (≤ 0.15 % FWHM ≤ 5°, ≤ 3.1 % FWHM = 20° vs exact; ≤ 1.3 % vs FDTD).
   Rationale: Attack 5.

**Block A — predictions**

5. **Re-scope P-TH23-A1 and A3.** A1 is restated as a *pointing/estimator*
   reading, explicitly not a coherence adjudication (Attack 7), with
   `042/run.py:41`'s "context only, this leg scores no perceptual pass/fail"
   comment carried verbatim. A3 is restated as a **desk-verifiable identity check**
   with a numerical tolerance (Attack 2), or dropped. Record in LOGBOOK that
   `beam_divergence_coherent` synthesises a Gaussian aperture of half-width
   `w₀/cos θ₀` — a permanent T21 fact, derived and measured here.
6. **Fix the denominators**: FWHM ≤ 10° is **27** cells, FWHM = 20° is **9**.
7. **Drop or rewrite P-TH23-A3's FWHM = 20° clause and P-TH23-A4 entirely** —
   under the fix the FWHM = 20° divergence is 0.11–2.52 %, so A3's
   hard-falsification clause fires pre-run and A4 has no premise (Attack 3).
8. **Re-band P-TH23-A2** from the numerical propagation of fix 4; as written its
   ≥30/36 clause already fails at 26/36 (Attack 4).
9. **Drop P-TH23-A7**, or widen its band by the measured 77–300× conditioning
   factor and label it EXPLORATORY-NON-SCORING (Attack 14).
10. **Disclose A3's convention mismatch** (`C_coherent` exists only under the
    superseded obliquity-on-E recipe; `block_beam_corrected` has no coherent
    column — verified) and either compare at matched convention or generate a
    corrected coherent column first (Attack 8).
11. **Restate idealization 4** with the corrected truncation numbers (unaimed rim
    9.99×10⁻³ amplitude / 9.98×10⁻⁵ intensity; aimed 1.61–2.96 w_line, rim
    ≤ 7.43×10⁻²) and re-justify or drop the aimed leg at 750 nm/FWHM 2° (Attack 6).
12. **Restate idealization 2**: the waist is **1.0737 λ at all three wavelengths**,
    a single value; and state that Block A's 3-λ sweep carries no material
    wavelength dependence beyond fixed cell geometry.

**Block A — gates**

13. **Add an oblique-width stage-16 gate** (EM's flip, upheld and specified):
    600 nm, θ₀ = 40°, `profile="gauss"`, `width = 56.063`, gate the 1/e² half-width
    of `observer_profile` at `PLANE_X` against **79.47 cells to ≤ 5 %**. My own
    FDTD run of exactly this configuration measured **80.47 cells** (1.3 % high),
    peak y = 981 vs ray-optics 979.1 — the gate is achievable and it is the only
    gate that can fail on this cycle's actual defect. S16-a (θ = 0°) and S16-b
    (centroid only) cannot.
14. **Restate S16-c's ≤1×10⁻¹² band** as platform-relative, naming the reference
    platform (EM, upheld).
15. **Guard the sign convention**: Block A compares `weber`-reduced scalars only;
    never `B(y)` profiles cell-by-cell, never a ratio of two `B`s, never analytic
    `B` mixed into `incoherent_sum` with FDTD `B` (Attack 15).

**Blocks B and C**

16. **Add Host E and the r = 1.0 column** to Block C (25-point grid, +18
    closed-form points, microseconds) — MATERIALS' M1, upheld as **binding**.
    Without them C1 is an all-negative-control grid and P-TH23-C4's
    Amendment-3 corroboration claim is structurally impossible (Attack 9).
    Strike "corroborating Amendment 3" from C4 unless E is added.
17. **Specify C3's scanned parameter as `dt_sweep` (the ON dwell D)**, gaps
    remaining 5τ_k/0.5τ_k. As written the scan collides with exp-045's own
    disclosed role inversion and is not implementable (Attack 10). Then relabel
    C3 *verification*, not *test* (MATERIALS M2).
18. **Label the silicon identity `ASSUMED — provenance terminates unsourced
    (T18)`** in `results.json`, not "sourced" (Attack 13, MATERIALS M3).
19. **Disclose the fill-factor idealization** and add a ρC_P sensitivity row;
    correct §2.3's "decided by the conduction length **alone**" to
    `ρ C_P L²/(4εσT³L + k_air)` (MATERIALS M4).
20. **Strike "eye-invisible"** from §1 and from P-TH23-B3's prediction text
    (Attack 11) — treat as non-negotiable, it is constraint-3-shaped.
21. **Harden idealization 9 at the loci that have actually failed**: NOTES.md
    prose, `run.py` console prints, and point-of-claim inlining at B3, B5, C1,
    C3, C4 — not storage, which `lab/thermo_sidecar.py:215` already auto-fills
    (Attack 12, VISION).
22. **Commit Amendment 5** to `experiments/034-.../REALIZABILITY_MEMO.md`
    recording C2's collapse of the memory axis to a dimensionless-dwell criterion
    and item 18's provenance downgrade; and cite the memo by its real path
    (MATERIALS M5 — Amendment 4's own header records the last time a cycle
    claimed an amendment it had not delivered).
23. **Fix the small slips** of Attack 14: `C = 0.374781250`, `ln(21e^{−0.5}) =
    2.5445224`, C5's floor ~2×10⁻¹⁵, C6's r = 1e-1 supremum 1.010711 /
    threshold 2.590.

**Program-integrity note (not a work item)**

24. VISION's item 3 is correct on the record: the Iteration-23 tripwire on the
    glare/adaptation sidecar has **tripped**, and §6 re-issues it as prose rather
    than in the hardened form Iteration 22 adopted for its sibling. I do **not**
    contest the deferral — T18 EGRESS_BLOCKED at eleven consecutive confirmations
    is dispositive, and manufacturing thresholds from seat memory is the exact
    defect this docket is elsewhere punishing. But the Director should carry it
    in the **hardened** form (automatic criterion-4 firing if Iteration 24 closes
    without it), not in prose. A cycle that takes the hard form for the item it
    delivers and the soft form for the item it drops is how the fix-docket
    pattern reproduces itself.

---

## Verification appendix — what I actually ran

- `geom_check.py` — exact non-paraxial angular-spectrum propagation (N = 2²⁰,
  evanescent clipped) of `exp(−(Y/w)²)exp(ik sinθ₀ Y)` over Δx = 223, all 36
  cells; far-field FWHM via `k_y = k sinθ` mapping. Produced Attack 1d and the
  peak-shift figures in Attack 4.
- `block_a_check.py` — exp-042's own `design_geometry` + `lab.ambient`: effective
  1/e half-width of `beam_divergence_coherent`'s synthesised aperture (36 cells);
  single-angle Gaussian `C_empty` at `width = w₀` and `w₀/cosθ₀`, in both the
  committed (obliquity-on-E) and corrected (E/H) conventions, vs committed
  `C_coherent`. Reproduces QUANTUM's 16/27 and min |C| = 0.0323, EM's 11/27, and
  PHOTONICS' 0.1–2.8 % / 5.3–14.2 % envelope residuals.
- `fdtd_geom.py` — **four full 1400-step FDTD runs** on the committed geometry
  (`lab.fdtd2d.Sim`, `profile="gauss"`, θ₀ = 40°, cpl = 20), 1/e² half-width of
  `lab.ambient.observer_profile` at `PLANE_X`. Attack 1e. ≈ 15 s per run on this
  box (the cost note's 3.05 s/run is exp-041's parallel figure).
- `docket.py` — corrected §2.1 table; A2/A3 status under the fix; aimed-leg
  truncation.
- Direct reads: `lab/fdtd2d.py:132-172,225-240`; `lab/ambient.py:36-56`;
  `lab/kinetics.py:195-219`; `lab/thermo_sidecar.py:190-220`;
  `lab/validation/run_all.py` (15 stages — stage 16 is the correct next index);
  `042/design_geometry.py:110-355`; `042/run.py:41,89-93`;
  `042/results.json` (`block_beam.rows`, `phase5_erratum.block_beam_corrected`);
  `038/run.py:20-46`; `037/NOTES.md:824-832`; `045/run.py:528-575`;
  `LOGBOOK.md:1040-1050, 7612-7630, 8320-8380`; `PANEL.md` in full.
- Ruled-out check: nothing in this docket resurrects R1, R2 or R3.
