# PHASE 2 — BLIND CRITIQUE · ELECTROMAGNETISM seat · exp-073 (Panel Iteration 50)

*Charter: field/wave behavior, impedance matching, energy coupling; owns
reciprocity/passivity/causality bookkeeping against T1. Fresh context,
blind to all other Phase-2 seats this cycle.*

## Steel-man (≤150 words)

exp-073 is this program's most disciplined re-issue to date. I independently
re-derived `A_q = 2·a_cbar·tan χ₀` from scratch — not accepted on the
document's word, and not merely re-accepted the way exp-072's own Red Team
Phase-5 audit explicitly declined to ("O-6 … ACCEPTED, DEFERRED. Not
re-derived here"). Writing the two adjacent-frequency carriers as
`C_A=a_A cos(Θ−φ)`, `C_B=a_B cos(Θ+φ)` with `φ=χ₀+πΔf·u`, expanding
`C_B−C_A` and matching to the frozen basis, gives `A_i=δa·cosχ₀`,
`A_q=2a_cbar0·sinχ₀`, `R_q=2π·a_cbar0·Δf·cosχ₀`; since the fitted `a_cbar`
already absorbs the `cosχ₀` factor (`a_cbar≈a_cbar0·cosχ₀`), both
`R_q=2π·a_cbar·Δf` and `A_q=2a_cbar·tanχ₀` fall out exactly. I also verified
the sign-flip null's zero-mean property algebraically (below) — a real,
provable improvement over the phase-randomized null it replaces.

## Sharpest attack (≤150 words)

§3a justifies the `A_q=2a_cbar·tanχ₀` fix as mattering *this cycle* because
§2c's a-priori regime puts `χ₀` at "0.5–1.2 rad at the two wide pairs." I
reconstructed that estimate (`χ₀≈π·Δf_pred·x̄`, `Δf_pred` from the closed
`m₀` and each pair's `T_x`) and it is a genuine, reproducible, data-free
number — 0.58–2.40 rad across the four pairs. But exp-073 reuses the
*identical* 124-point substrate and *identical* carrier-fit/design-matrix
machinery as exp-072, whose already-closed, non-contaminating `A_q`/`a_cbar`
values give the *real* `χ₀`: −0.0197 / −0.0203 / −0.0062 / −0.0434 rad
(C40-C60/C60-C70/C70-C80/C40-C80, computed directly from
`experiments/072-.../results.json`). `tan/sin` there is 1.0002–1.0009 — a
0.02–0.09% correction, not the claimed 2.6×. The "binds hard" framing is an
a-priori prediction falsified 30–100× by the very substrate this cycle
re-fits — exactly the outcome-inconsistency the proposal's own
evidentiary-class discipline (§3, classes a/b/c) exists to catch, and it
missed its own case.

## Verdict

**support-with-changes**

## Optional change that would flip the verdict

Correct §3a's `A_q` bullet to state plainly, with the number: on this
reused substrate the tan-vs-sin correction is expected to remain
numerically inert (`χ₀` realized ≈0.006–0.043 rad, not 0.5–1.2 rad), citing
the already-closed exp-072 `A_q`/`a_cbar` values as the check (this is
class-(b) information — a prior, non-contaminated cycle's closed
result — not a violation of the outcome-independence discipline; it is
exactly the kind of cross-check that discipline is supposed to invite).
Since T2-4 is explicitly non-gating (folded in for §2b.3's table only, no
Combined-Verdict branch reads `A_q`/`χ₀`), this is a one-paragraph text
fix, not a re-design — with it made, I support the cycle as designed.

---

## Supporting detail

### 1. Re-derivation of the exact `A_q`/`R_q` identities (worked from scratch)

Model the two configs as detuned cosines in `u`-space (`u = sinθ − x̄`),
sharing the fitted common carrier `Θ = w̄u + ψ̄`:

```
C_A(u) = a_A·cos(Θ − φ),   C_B(u) = a_B·cos(Θ + φ),   φ(u) = χ₀ + πΔf·u
```

(`φ` is half the instantaneous phase gap; at `u=0` it is `χ₀`, growing
linearly at rate `πΔf` — this *is* the design's own `Θ`/`χ₀` parameterization,
§2b.3.) Expanding with the angle-sum identities:

```
C_B − C_A = (a_B−a_A)·cosφ·cosΘ − (a_B+a_A)·sinφ·sinΘ
Cbar = (C_A+C_B)/2 = a_cbar0·cosφ·cosΘ − (δa/2)·sinφ·sinΘ,  a_cbar0=(a_A+a_B)/2
```

Over the window, `φ(u)` is slowly varying relative to `Θ(u)` (this is
exactly the linearization-gate regime, `|Δf|·X ≤ 0.25`), so a single-frequency
LSQ fit of `Cbar` to `a_cbar·cos(Θ)` recovers, to leading order, the
envelope evaluated near window center: `a_cbar ≈ a_cbar0·cos χ₀` (the
`δa·sinφ·sinΘ` term is orthogonal to `cosΘ` in the fit to leading order and
does not contaminate the recovered amplitude). Linearizing `cosφ` and
`sinφ` to first order in `u` (`φ≈χ₀+πΔf·u`) and matching `C_B−C_A` term by
term onto the frozen basis `[1, cosΘ, −sinΘ, u·cosΘ, −u·sinΘ]`:

```
A_i = δa·cosχ₀
A_q (coeff of −sinΘ) = 2a_cbar0·sinχ₀
R_i (coeff of u·cosΘ) = −δa·πΔf·sinχ₀        (O(δa·Δf), first-order zero)
R_q (coeff of −u·sinΘ) = 2π·a_cbar0·Δf·cosχ₀
```

Substituting `a_cbar0 = a_cbar/cosχ₀`:

```
R_q = 2π·a_cbar·Δf              A_q = 2·a_cbar·(sinχ₀/cosχ₀) = 2·a_cbar·tan χ₀
```

Both of the document's headline formulas fall out exactly, and `R_i`'s
"first-order zero, nonzero = model strain" characterization is confirmed
as a structural (not merely empirical) property. **This settles what
Red Team's O-6 explicitly left open ("not re-derived here"): the formula
is correct, not merely plausible.**

### 2. The a-priori `χ₀` estimate is itself real and reproducible — the problem is inconsistency with known substrate behavior, not fabrication

Using `Δf_pred = −(radians(m₀·ΔABSORB)·cos39°) / T_x²` (the same construction
`injection_recovery`'s `df_pred` already uses in exp-072/`run.py`) and
`χ₀ ≈ π·Δf_pred·x̄` (`x̄ ≈ sin39° = 0.6293`):

| Pair | ΔABSORB | `Δf_pred` | `χ₀` (a-priori) | `χ₀` (exp-072's real `A_q`/`a_cbar`) |
|---|---|---|---|---|
| C40–C60 | 20 | −0.610 | **−1.205 rad** | −0.0197 rad |
| C60–C70 | 10 | −0.295 | **−0.583 rad** | −0.0203 rad |
| C70–C80 | 10 | −0.294 | **−0.581 rad** | −0.0062 rad |
| C40–C80 | 40 | −1.215 | **−2.403 rad** | −0.0434 rad |

The a-priori column is legitimately data-free (`m₀` is class (b), window
geometry class (a)) and roughly matches the document's own claimed
"0.5–1.2 rad" range (C40–C80 runs somewhat past it, but the order of
magnitude and sign are right) — so I do not think this number was invented.
The defect is that this a-priori figure implicitly assumes the *true*
signal is near `m₀`'s predicted size, and the identical substrate this
cycle re-fits has *already*, non-contaminatingly, shown (via exp-072's
closed, published `A_q`/`a_cbar`) that the realized ramp/phase channel is
30–100× smaller than that. Because none of exp-073's three changes (null
construction, sign-invariance admissibility set, wrong-carrier value) touch
the OLS point estimates `A_q`/`a_cbar` — those come from the unchanged
carrier-fit + frozen-basis regression — exp-073 will recover essentially
the same tiny `χ₀` values, and the `tan`-vs-`sin` correction will again be
inert on the real data, as it was at exp-072.

### 3. Algebraic check on `E[R_q^surr]=0` under T2-3's sign-flip null

Worth recording since it is load-bearing and I verified it independently
rather than taking §3b's word for it. `resid5 = δ − X5β̂` is, by the normal
equations, exactly orthogonal to every column of `X5` (`X5ᵀ·resid5 = 0`),
for *any* `δ`, regardless of the true data-generating process — a purely
algebraic fact, not a distributional assumption. `yhat0 = X4γ̂` lies exactly
in `span(X4) ⊂ span(X5)`; since `X5` is full column rank (G0-d), its
representation in the `X5` basis is unique, so the coefficient on the
`R_q` column when `yhat0` is re-expressed in `X5` is exactly `0`. A
surrogate `y* = yhat0 + s∘resid5` (`s`∈{±1} i.i.d.) therefore has
`R_q(y*) = R_q(yhat0) + R_q(s∘resid5) = 0 + [\text{5th row of } pinv5]·(s∘resid5)`,
and `E_s[s∘resid5]=0` pointwise ⇒ `E[R_q^surr]=0` exactly. **Confirmed**:
T2-3's central claim holds algebraically, unconditionally, not merely "in
expectation under an assumed noise model."

One caveat worth flagging (not the sharpest attack, but real): this proves
correct *centering*, not correct *size*. Sign-flipping preserves each
point's residual magnitude but treats residuals as independent across `θ`;
G0-e(ii) only calibrates against i.i.d. Gaussian synthetic noise, which
cannot expose miscalibration from the same structured/correlated FDTD
residuals that elsewhere in this same document (§3a, the design-respecting
bootstrap discussion) are explicitly why a naive resampling scheme was
rejected. If the real `resid5` carries θ-correlated structure, G0-e(ii)'s
own PASS would not detect it. This is a real gap in the calibration gate's
coverage, but it is a design-completeness point, not a demonstrated
miscalibration — I flag it as supporting detail, not the headline attack,
since I cannot quantify its size without the real residuals in hand.

### 4. Reciprocity / passivity / causality bookkeeping

Not engaged this cycle, correctly. `ABSORB` is disclosed (Idealization 3)
as a numerical graded-damping boundary parameter, not a claimed material —
no σ(I)/σ(x,t)/dispersive-ε mechanism is proposed, no T1 escape route is
taken (§6, correctly stated N/A), and no energy/reciprocity claim is made
anywhere in the document. There is nothing here for R1–R6 or T1's
constraint bookkeeping to bind on; this is desk statistics on already-run
FDTD output, and I find no passivity- or causality-adjacent claim smuggled
in under that cover.
