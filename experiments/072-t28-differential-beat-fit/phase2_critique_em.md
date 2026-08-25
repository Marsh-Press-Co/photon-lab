# ELECTROMAGNETISM — Phase 2 Critique · Panel Iteration 49 · exp-072

*Fresh sub-agent, EM charter (field/wave behavior, impedance matching, energy coupling; owns reciprocity/passivity/causality bookkeeping). Blind to all other seats this cycle. Critique of PHOTONICS' Phase-1 differential/beat fit of `delta_AB(θ)`.*

---

## Steel-man (≤150 words)

The derivation is correct where it matters, and I checked it rather than assumed it. `cos P − cos Q = −2 sin((P+Q)/2)·sin((P−Q)/2)` reproduces §1's exact form with `χ = πΔf·x̄ + Δψ/2`. The linearization domain is genuinely safe: the worst pair (C40–C80) has `πΔf·|u|max = 0.149` rad, <0.5% error on `sin`. The §2c ramp fractions reproduce exactly as `π|Δf|X` (29.7 / 15.0 / 7.2 / 7.2%), and `ΔP = −(Δf/f̄)·P_mean` is the right first-order map since `T_x = radians(P°)·cos39°` is linear. Most importantly the central physical claim is right: over a finite window a frequency difference is *degenerate with a phase offset* except through its linear-in-`u` leverage, so `R_q` is the only channel carrying `Δf`, and estimating one regression coefficient at a resolvable carrier is strictly better conditioned than differencing two unresolvable absolute frequencies. Zero FDTD cost, honest a-priori power table, pre-registered fallback. Right instrument.

*(147 words)*

---

## Sharpest attack (≤150 words)

**The coefficient table is wrong in the one entry the proposal then interprets.** Expanding to first order about the mean parameters:

`delta ≈ δa·cosΘ − a(Δψ + 2πΔf·x̄)·sinΘ − 2πa·Δf·u·sinΘ`

So in the stated basis `[1, cosθ_c, −sinθ_c, u·cosθ_c, −u·sinθ_c]`, `A_q = a·Δψ + R_q·x̄` — **not** `−a·Δψ`. The sign is flipped, and the frequency difference is the *dominant* contributor to `A_q`, not absent from it. With `x̄ = sin39° = 0.6293` and `σ_u = X/(2√3) = 0.0235`, a pure frequency difference deposits `x̄/σ_u ≈ 27×` more amplitude into `A_q` than into the ramp channel P-072-6 compares it against. P-072-6 will therefore report "the dominant effect is a constant phase offset, not a frequency change" — mandated by §5 to be stated "as a substantive T28 finding" — with probability ≈1, **even when the effect is purely a frequency change.** The proposal's own degeneracy argument forbids the readout it built on top of it.

*(150 words)*

---

## Verdict

**SUPPORT-WITH-CHANGES.** The estimator is sound and the conditioning argument is correct; the pre-registration around it is not yet safe to run. Three required corrections:

**1. Fix the `A_q` mapping.** Table row becomes `A_q = a·Δψ + R_q·x̄` ("phase offset *plus* the window-centre frequency term"). P-072-6's phase channel must be reported as `|A_q − R_q·x̄|/a`, not `|A_q|/a`. `A_i = a_B − a_A` and `R_q = 2πa·Δf` check out unchanged; `R_i = 0` at first order, so its use as a model-strain indicator is right.

**2. P-072-3 (closure) is very nearly vacuous, and it is a conjunct of CONFIRMED.** Step 2 is OLS — linear in `delta_AB` — and G0-b establishes the raw deltas telescope exactly. If the four pairs shared `(T_mean, a, ψ̄)`, then `R_q`, `Δf`, and `ΔP` would all telescope *exactly*, giving `ρ_c ≡ 0` by linear algebra. The four `Cbar` series are averages of the same four configs; their carrier periods differ by ~1–2% and amplitudes by a few percent, so `ρ_c` inherits only second-order basis deviations — order 0.02–0.05, an order of magnitude inside the `ρ_c ≤ 0.25` CONFIRM band. §5's note that closure is "a genuine, non-trivial test ... of the common-mode-cancellation assumption" is not correct: it tests loader integrity and basis stability. Either drop it from the CONFIRMED conjunction, or retain it re-labelled as a basis-stability check with `ρ_c ≤ 0.05`.

**3. Phase-reference error is nowhere propagated.** Step 2's OLS `SE(R_q)` and all 20,000 surrogates hold `T_mean` and `ψ̄` fixed *and exact*. Neither therefore calibrates the one systematic that directly targets `R_q`: a phase-reference error `ε` rotates the ramp plane, mixing `R_i` into `R_q` as `R_i·sin ε`. And `ψ̄` is estimated from a strained fit — `x = sinθ` is not linear in `θ` (local scale varies 8.1% across 36°–42°, giving a common-mode quadratic phase of `(2π/P_x)·(x̄/2cos³39°)·u²max = 0.207` rad ≈ 12° that a pure sinusoid-in-`x` model cannot absorb), on a two-component signal reaching only `R²≈0.43–0.45`. Require a bootstrap of step 1 propagated into `SE(R_q)`, or at minimum report `dR_q/dψ̄` and `R_i/R_q` per pair. Secondary: Fourier-phase surrogates assume circularity; `delta_AB(θ)` has an end-to-end trend, so detrend or taper (or use IAAFT) before phase randomization.

---

## The single parameter change that would flip my verdict

**Promote P-072-5 (wrong-carrier control) from "disclosed, non-gating" to a fourth required clause in P-072-2's `RESOLVED` conjunction:**

> `RESOLVED` additionally requires `|R_q(T = 1.9608°)| ≤ ½·|R_q(T_mean)|` **and** the wrong-carrier Holm-adjusted surrogate `p > 0.01`.

Why this specific gate. T21's established 1.9608° fringe sits at `f₂ = 1/(radians(1.9608)·cos39°) = 37.60`; the carrier sits at `f̄ = 29.67`. Their separation is `7.93`, against the proposal's own Rayleigh width `1/X = 12.29` — **0.645 Rayleigh widths, i.e. the second carrier is not separable from the first in this window, by §2c's own criterion.** A sub-Rayleigh contaminant of amplitude `b` does not sit quietly in the constant terms: across `u ∈ ±X/2` it accumulates `2π(f₂−f̄)·|u|max = 2.03` rad of relative phase, well past linear, so it projects `O(b)` directly into the ramped columns — the target channel.

The proposal names this contaminant twice (§6.4, P-072-5) and then leaves it unguarded. Its two nominal defences both fail against it specifically: the carrier-consistency gate `|T_delta − T_mean|/T_mean ≤ 0.414` spans `[1.456°, 3.514°]`, which **contains 1.9608°** — so a `delta_AB` whose free-period search locks onto T21's fringe outright still passes; and P-072-5 itself is explicitly excluded from the Combined Verdict. As written, a CONFIRM is reachable with the wrong-carrier control screaming.

With that clause added — and corrections 1–3 applied — I support without reservation. The differential framing is the correct move on T28, and I want it run.
