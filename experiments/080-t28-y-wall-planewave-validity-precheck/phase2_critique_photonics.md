# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 57 · exp-080

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections). Fresh context, blind to the other
six seats' Phase-2 critiques this cycle.

## Independent verification performed, from primitives

Re-ran the geometry arithmetic (`W=1504`, `λ=CPL[600]=20` → `d_F=W²/λ=
113,100.8` cells — matches). Then, to test the `theta_eff` methodology
itself rather than restate the write-up's own self-assessment, I rebuilt
`single_angle_curve`'s machinery from `y_wall_aperture_sum.py`'s imported
primitives and checked two things it does not check:

1. **Is `r(theta_eff)` (r evaluated at the mean angle) the right single
   constant, or should it be `r_bar` (the mean of `r(theta_local(y_s))`
   itself)?** Computed `r_bar = ∫amp·r(theta_local(y_s))dy / ∫amp dy` per
   config. Result: `R²(Re)` improves only marginally (C40 `0.824→0.849`,
   C70 `0.521→0.546`); `R²(abs)` at C70/C80 stays deeply negative
   (`-7.82→-6.76`, `-8.45→-7.44`). The Jensen gap between "mean-then-r" and
   "r-then-mean" is real but small — not the driver of INCONCLUSIVE.
2. **Since `r_const` is pulled outside the aperture integral in
   `echo_field_curve`/`single_angle_curve`** (`integrand = amp*r_const*
   exp(iφ)`), `E_model(θ_beam) = r_const · E_ablated(θ_beam)` exactly,
   where `E_ablated` is exp-079's own `r≡1` ablation curve. This means
   `|E_model(θ_beam)| = |r_const|·|E_ablated(θ_beam)|` — a **pure scalar
   rescaling** of a fixed, `theta_eff`-independent shape; only `|r_const|`
   moves, never the shape, under `|·|`. I computed the best possible
   least-squares scale `α*` of `|E_ablated|` against the true `|E_echo|`:
   C70 `α*=2.60e-6→R²=-1.65`; C80 `α*=1.37e-6→R²=-2.30` — vs. the
   reported `θ_eff`-based `|r_const|=1.29e-6/6.9e-7`, roughly **half**
   `α*`, giving the reported `-7.82/-8.45`.

## 1. Steel-man (≤150 words)

The two-part design is the right shape for a validity gate: a
first-principles geometric criterion (Fraunhofer margin + `theta_local`
spread) run before any empirical fit, plus an empirical single-angle
reconstruction test scored against pre-registered, non-adjustable bands.
The `d_F`, `theta_local` envelope, and spread-ratio numbers all
independently reproduce from raw geometry. The version-drift guard
(`0.0` max diff against the committed exp-079 curves) means part (b)'s
`R²` numbers are trustworthy as a comparison, not silently drifted. Most
creditably: EM's own directional prediction (SUPPORT) was falsified by
its own numbers and disclosed as such rather than reframed — exactly the
R4 discipline this program claims to run on, and the secondary
negative-`R²` anomaly is flagged rather than buried in the mean.

## 2. Sharpest attack (≤150 words)

The write-up's explanation for the negative `R²(abs)` — a Jensen-type
phase rotation shifting zero-crossings — is an unverified narrative for
what is actually a **one-parameter scale problem**: since `r_const` is
pulled outside the integral, `|E_model(θ)|=|r_const|·|E_ablated(θ)|`
exactly, so `theta_eff`'s only effect on the `|·|` proxy is to rescale a
fixed shape, never reshape it. I fit the best possible scale directly:
`R²(abs)` caps at `-1.65` (C70) / `-2.30` (C80) even optimally chosen —
still a real shape failure, but the reported `-7.82`/`-8.45` are roughly
half that best case because `|r(theta_eff)|` happens to undershoot the
optimal scale by ~2×, a calibration artifact, not new physics. The
write-up's own "primary vs. secondary `theta_eff` agree within 0.02–0.05"
robustness claim for this proxy is near-tautological for the same
algebraic reason (both give nearby `|r_const|`) — it cannot detect a
shape defect and shouldn't be cited as evidence the `abs` finding is
robust.

## 3. Verdict: **support-with-changes**

Both pre-registered verdicts (FORECLOSE / INCONCLUSIVE) stand under my
own re-derivation — the geometric case is solid and the `R²(Re)` verdict
is not moved by fixing the `r_bar`-vs-`r_eff` ambiguity. But the
secondary-proxy negative-`R²` finding, as explained in the write-up,
overstates the failure with an unverified mechanistic story where a
one-line scale-fit check would have separated "avoidable calibration
miscue" from "genuine structural shape mismatch, concentrated at the two
deepest absorbers (ABSORB=70,80)." The ABSORB-depth concentration itself
(clean at 40/60/G40, catastrophic only at 70/80) is left unexplained and
undisclosed as a pattern — a real, checkable optical-response question
(does `r(θ)`'s angular curvature sharpen with boundary loss depth?) that
PHOTONICS' downstream §4 build, which spans this same ABSORB range,
should not inherit silently.

## 4. Single parameter change that would flip my verdict to plain "support"

Replace `|r(theta_eff)|` in the secondary-proxy scoring with the
least-squares-optimal scale `α*` fit of `|E_ablated(θ_beam)|` to the true
`|E_echo(θ_beam)|` (one extra line — `α*=Σ|true|·|ablated|/Σ|ablated|²`),
and report both numbers side by side. That isolates the real,
ABSORB-depth-concentrated shape failure from the calibration artifact and
would make the disclosed negative-`R²` finding fully earned rather than
overstated.
