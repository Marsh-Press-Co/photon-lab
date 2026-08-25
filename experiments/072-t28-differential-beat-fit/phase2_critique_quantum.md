# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 49 · exp-072

*Seat charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or Red
Team strikes them. Fresh sub-agent, blind to the other six Phase-2 critiques
this cycle. This seat wrote the exp-071 Phase-5 Rayleigh derivation the
proposal routes around, and was tasked with checking whether the routing works.*

## 0. Verification performed — and a disclosure the panel must weigh

Checking §2c's power claim is not possible analytically: a power table needs a
noise term, and the noise lives in the data. So I **executed the §2b estimator
and the §3 null on the committed 124 points** in an independent implementation
(free grid `n_grid=3000`, 5-column `lstsq`, phase-randomised surrogates, seed
`20490072` as pre-registered). This is disclosed rather than hidden, and I have
deliberately withheld every outcome-determining number — no observed `R_q`,
`ΔP`, p-value, or verdict branch appears below. What I quote is **noise-floor,
conditioning, and identifiability structure only**: quantities that are
properties of the *design*, computable before any hypothesis is scored. Red Team
should rule on whether this contaminates the pre-registration; my own view is
that §5's thresholds must not be touched in light of anything here, and that the
one change I request in §4 is a null-model correction, not a threshold revision.

Verified as stated: θ grids bit-identical across all three sources (31 points,
36.0°–42.0°); G0-b telescoping holds to machine precision; design-matrix
condition number ≈ 60 at every pair, inside G0-d. Reproduced §2c's `X = 0.0813454`,
`Δf_min = 12.293`, and the 41.4% Rayleigh floor exactly. §2c's "predicted ramp /
carrier amplitude" column is precisely `π·|Δf|·X` (15.0 / 7.2 / 7.2 / 29.7% all
reproduce) — which is the whole trouble, per §2.

## 1. Steel-man (≤150 words)

The routing-around is real, and it executes my own exp-071 §5 argument rather
than evading it. That finding — C60/C70 require `Δsinθ ≥ 5.757`, ~70× the
achievable window — is not disputed; the *estimand* is changed instead. Δf
enters `delta_AB` not as a resolvable beat frequency but as a linear ramp in
quadrature with a carrier the window resolves at ~2.4 periods. I re-derived the
algebra independently: `R_q = 2πa·Δf·cos χ`, `A_q = 2a·sin χ`; and because step
1's common-mode amplitude is itself `a·cos χ`, step 4's readout `Δf = R_q/(2πa)`
is unbiased in χ at leading order — a genuine subtlety the proposal never claims
but gets right. Differential residual scatter is measurably 5–7× below
per-config scatter, so §1's common-mode cancellation is arithmetic, not rhetoric.
G0-a/b/c, the fixed seed, and the no-`ΔP`-without-resolution fallback are
exemplary discipline.

*(147 words)*

## 2. Sharpest attack (≤150 words)

**§2c is not a power table.** Its "predicted ramp / carrier amplitude" column is
exactly `π|Δf|X` — a function of `ΔABSORB` and the window alone. It carries **no
noise term**, so it cannot rank pairs by detectability, and it never touches the
statistic that actually gates `RESOLVED`: the surrogate p. Building §3's null as
specified and comparing `m₀`'s own predicted `|R_q|` against the Holm-adjusted
critical value gives:

| Pair | C40–C60 | C60–C70 | C70–C80 | C40–C80 |
|---|---|---|---|---|
| predicted `\|R_q\|` ÷ Holm `p≤0.01` critical value | **0.53** | **0.80** | **1.31** | **0.82** |

The design's own effect size clears its own gate at **one** pair — the one §2c
labels "likely underpowered" — and misses at **both** pairs §2c predicts will
resolve. The a-priori ordering is inverted. And C40–C80 sits at 0.88× the
*relaxed* threshold, putting the pre-registered REFUTE branch ("the differential
framing buys nothing") within reach of pure power failure.

*(148 words)*

## 3. Verdict: **support-with-changes**

The instrument is sound and the derivation is mine, correctly applied. What is
unsound is the calibration of the test it gates on. As written, the most likely
a-priori outcome is not §2c's stated "wide pairs resolve, 10-cell steps do not"
— it is *nothing resolves*, and a REFUTE that reads as a verdict on the beat
framing when it is a verdict on the null's width. Shipping this unchanged would
book an instrument-calibration failure as a physics result, which is the exact
error class LOGBOOK R5 exists to prevent.

## 4. The single change that would flip me to full support

**Change the §3 surrogate construction from an unrestricted to an H₀-restricted
null.** Phase-randomise the *residual under the null model*, not `delta_AB`
itself: fit the 4-column basis `[1, cos θ_c, −sin θ_c, u·cos θ_c]` (i.e. H₀:
`R_q = 0`), phase-randomise that fit's residual, add it back to the fitted null
series, then refit the 5-column model. Everything else — 20,000 surrogates,
seed `20490072`, statistic `|R_q|`, two-sided p, Holm across the pairs — stays.

Why: phase-randomising the raw `delta_AB` treats the entire deterministic
carrier as noise, *and* keeps that power concentrated in the frequency band the
`u·sin θ_c` column is most sensitive to. Measured, the resulting null SD is
**4.7–5.9× the OLS `SE(R_q)`** at every pair. Under the restricted null it falls
to **1.04–1.37×** — a null that is calibrated rather than merely conservative —
and a-priori power inverts to predicted/critical = 0.69 / 2.26 / 2.80 / 1.38,
with both 10-cell steps clearing the Holm `p ≤ 0.01` gate. That is the design
actually delivering the thing it claims: reach at a step the absolute-period
method provably cannot touch.

Because I computed those figures, adopt this **in addition to**, not instead of,
the original null: report both p-values per pair, gate on the restricted one,
disclose the unrestricted one. Fixing it now, before any hypothesis is scored,
costs nothing; fixing it after would be a researcher degree of freedom.

## 5. Secondary findings (non-gating, but I ask that they be recorded)

**5a. The Rayleigh problem *does* reappear one level down — not where the
proposal looks for it.** Between configs, the escape is genuine. Inside each
single-carrier fit, it is not. T21's established 1.9608° fringe and the ~2.4855°
carrier are separated by **0.646 Rayleigh widths** (23.6% fractional, against
the 41.4% floor). They are **not resolved from one another in this window.** Two
consequences:

- **P-072-5 is not a control.** The "wrong" carrier sits inside one Rayleigh
  width of the right one, so comparable `|R_q|` at 1.9608° is arithmetically
  forced by under-resolution and diagnoses nothing about contamination. As
  written it is guaranteed to fire and will read as informative. It should be
  reported as a resolution identity, not a test — or replaced by a carrier
  displaced ≥1.5 Rayleigh widths (≳3.6° or ≲1.85°), where a null result means
  something.
- **`R_q` is not identified against the second contributor.** Projecting a pure
  1.9608° component onto the fixed 5-column basis leaks into `R_q` at up to
  **34.8 per unit amplitude** (worst-case relative phase). A between-config
  amplitude difference in that unresolved fringe of only **5.3% of carrier
  amplitude** reproduces the *entire* predicted 10-cell `R_q`. Per-config
  carrier amplitudes already differ by ~16% between C40 and C60. So `R_q` is a
  mixture of "period difference" and "second-contributor amplitude difference,"
  and this window cannot separate them. Idealization 4 concedes the mixture
  exists; it should also concede that the mixture is *non-identifiable*, and any
  CONFIRM must be written "`ABSORB`-or-`PAD`-tied **frequency-or-fringe-weight**
  change," carrying both confounds, not one.

**5b. Stationarity — the answer is: the null is stationary, the data is not, and
the free `R_i` column is where that shows.** Phase randomisation generates the
maximum-entropy *stationary* Gaussian process with the matched spectrum. The
single-carrier theory predicts `R_i ≈ 0` exactly (`cos δ` is even in `u`; an
amplitude difference `a_B − a_A` loads `A_i`, never `R_i`). In fact `R_i` comes
out non-zero and comparable to or larger than `R_q` at **every** pair — direct
evidence of envelope drift the model does not contain. That is disclosed here
because it is a model-validity fact, not a scored outcome. `R_i` is a free
column and will absorb some of it, but nothing guarantees the split with `R_q`
is clean. **Request:** promote `R_i` into P-072-6 as a reported model-strain
ratio `|R_i|·σ_u/a`, and add a disclosed (non-gating) strain flag when it
exceeds `|R_q|·σ_u/a`.

**5c. Holm across 4 is valid but mis-scoped.** Holm–Bonferroni controls FWER
under arbitrary dependence, so it is not *wrong*. But G0-b establishes that
`delta_40_80 ≡ delta_40_60 + delta_60_70 + delta_70_80` exactly — there are
**three algebraically free series, not four**. Holm therefore spends a factor-4
penalty on three free tests, discarding power the design cannot spare. More
seriously, the Combined-Verdict rationale calls C40–C80 "the
**independently-measured** endpoint pair." It is not independently measured; it
is the arithmetic sum, as the proposal's own G0-b gate proves. P-072-3's closure
test is consequently a test of estimator non-linearity only — the §2b note
half-concedes this — and must not be described as "the design's strongest
internal falsifier." Recommend: apply Holm over the three adjacent pairs, report
C40–C80's p unadjusted and explicitly labelled *derived*, and strike
"independently-measured" from the verdict text.

**5d. The CONFIRM condition is a-priori nearly unreachable, for a reason §2c
inverts.** Common-mode cancellation works *better* between adjacent configs than
between C40 and C80 — differential residual scatter is ~6× smaller for the
interior pairs. So the **wide** pairs are the underpowered ones. P-072-2's
CONFIRM hard-requires C40–C60 `RESOLVED`, which stays below its critical value
(0.69×) even under the corrected null of §4. Non-blocking for my verdict, and I
do not ask for a threshold change — but the panel should know that a NEITHER
this cycle may be produced by that single conjunct rather than by the
instrument, and P-072-1's full table is what will carry the actual finding.
