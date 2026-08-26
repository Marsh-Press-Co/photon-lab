# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 51 · exp-074

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md: non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters, or Red Team strikes them). Not the same instance as my own
Phase-2 predecessor on this cycle, nor the exp-072 Phase-5 `L(T)`
originator; everything below is independently re-derived against the
committed code and data. Blind to every other seat's Phase-5 review this
cycle. Task brief: independently re-verify the T2-3-generalized sign-flip
null's centering property, `lev9_Rq`'s correctness and explanatory power,
and whether the circular-shift leg's much-worse failure is diagnostic of
a real second contributor or an R5-shaped trap.*

---

## 0. What I ran

All findings below are backed by scripts I wrote and executed against the
unmodified committed `desk_check_pricing.py`/`fit_and_calibrate.py` and
their own functions (imported directly, not re-typed): (1) an algebraic
check of the row9⊥X8 identity at machine precision, all four pairs; (2) a
200,000-draw empirical check of `E[R_q^surr]=0` on real data; (3) a
from-scratch recomputation of `lev9_Rq` by a second method, matched to six
decimal places against the code's own output; (4) an independent 3,000-
draw-per-pair Monte Carlo re-simulation of the i.i.d. calibration leg,
reproducing the official run's order of magnitude; (5) a weight-
concentration (participation-ratio) diagnostic on `row9`/`row5`; (6) a
from-scratch characterization of the four configs' per-config residuals
(magnitude, lag-1 autocorrelation, cross-config correlation, best-fit
period, variance explained by a quadratic-in-`u` term); (7) a direct
magnitude comparison of the circular-shift leg's synthetic null deltas
against the real, correctly-aligned `delta_ab` and the real, zero-shift
residual difference. `CHECK0 pass=True worst_rel_err=0.00e+00` reproduced
directly, confirming the basis every finding below builds on.

---

## 1. The generalized sign-flip null's centering property — CONFIRMED, exact, correctly generalized

**Claim under test:** does `E[R_q^surr]=0` hold for exp-074's 9-column
generalization (reduced = `X9` minus column 4 = `X8`; full = `X9`;
sign-flip the full model's residual, add back the reduced model's fit,
refit `X9`) the same way it did for exp-073's own `(X5,X4)` construction?

**Yes, and the reason is a general algebraic fact about OLS pseudo-inverse
rows, independent of which columns are dropped or how correlated they
are.** Let `row_k = pinv(X)[k,:]` be the dual row for coefficient `k`.
By construction `pinv(X) @ X = I`, so `row_k · X[:,j] = δ_{kj}` for every
column `j` — in particular `row_k` is exactly orthogonal (dot product
zero) to every OTHER column of `X`, including all columns of any reduced
model formed by deleting column `k`. This holds for `X5`/`X4` (exp-073)
and for `X9`/`X8` (exp-074) alike; nothing about it depends on the number
of columns or their collinearity. Consequently, for a surrogate
`y0(s) = X8·β̂8 + resid9⊙s`:

`R_q^surr(s) = row9·X8·β̂8 + row9·(resid9⊙s) = 0 + Σᵢ row9ᵢ·resid9ᵢ·sᵢ`

and `E_s[R_q^surr] = Σᵢ row9ᵢ·resid9ᵢ·E[sᵢ] = 0` exactly, for **any**
realized data. I verified `row9·X8 = 0` directly, all four pairs, to
`3.9×10⁻¹⁴` (floating-point exact), and confirmed `E[R_q^surr]≈0` to
`<3×10⁻⁵` over 200,000 real-data sign-flip draws per pair (vs. observed
`R_q9` values of `0.007–0.022` — three to four orders of magnitude
smaller than the signal). **This generalizes cleanly; the design-only
correctness of the null's centering is not in question.**

---

## 2. `lev9_Rq` — correctly computed; correctly predicts direction; the record's "exactly as predicted" language overclaims magnitude precision

**Code correctness:** `lev9_Rq = Σ row9ᵢ²·(1−h9ᵢᵢ) / Σ row9ᵢ²` matches
`fit_and_calibrate.py`'s implementation exactly — I recomputed it by an
independent method (separately building `H9`, `row9`, and the weighted
sum) and matched the code's output to six decimal places at all four
pairs (e.g. C60–C70: `0.593247` both ways). `trace(H9)=9.0000=p9` at every
pair, confirming the hat matrix itself is sane.

**Why this quantity is the right one, and what it predicts.** For pure
i.i.d. noise of variance `σ²`, `Var(R̂_q) = σ²·Σrow9ᵢ²` (the true
null-sampling variance), while the sign-flip surrogate distribution's
expected variance is `E[Var_s(R_q^surr)] = σ²·Σrow9ᵢ²·(1−h9ᵢᵢ)` (using
`E[resid9ᵢ²]=σ²(1−h9ᵢᵢ)` exactly, an OLS identity). Their ratio is
`lev9_Rq` itself — so `lev9_Rq<1` means the surrogate reference
distribution is narrower than the true null distribution of `R̂_q`, which
is exactly the mechanism that makes a sign-flip test anti-conservative.
**Direction: confirmed, exactly, by construction — a lower `lev9_Rq`
must produce more anti-conservative bias, not merely correlates with it.**
This is also why `lev9_Rq≈0.586–0.596 < 0.79–0.80` (exp-073) correctly
predicts exp-074's failure is *worse*, not merely different.

**Magnitude: partially, not "exactly," predicted — I found and quantify a
consistent, previously-undisclosed gap.** Translating `lev9_Rq` into a
predicted rejection-rate inflation via the natural Gaussian-quantile
model (`ratio(α) = 2·(1−Φ(z_{α/2}·√lev)) / α`) gives, at `α=0.01`:
`~1.8–2.2×` for exp-073's `lev≈0.79–0.84` and `~4.7–4.9×` for exp-074's
`lev≈0.586–0.596`. **Actual observed inflation is `5.4–5.7×` (exp-073)
and `8.7–11.2×` (exp-074, official run) — both roughly `1.6×–2.7×` larger
than the naive Gaussian translation predicts, at both cycles, in the same
direction and comparable ratio.** I traced this to real, quantifiable
leverage-weight concentration: a participation-ratio diagnostic
(`(Σwᵢ²)²/Σwᵢ⁴` on `row9ᵢ²`/`row5ᵢ²`) shows the sign-flip sum's
"effective" number of contributing points is only `~10` (9-col) / `~12`
(5-col) out of `n=31` — far short of full-CLT territory — so the
surrogate distribution is more leptokurtic (heavier-tailed at fixed
variance) than a normal approximation predicts, inflating tail rejection
rates beyond what a variance-ratio-only argument captures. I independently
re-simulated the i.i.d. leg (3,000 draws/pair, own RNG, `σ=0.002`) and
reproduced the official run's order of magnitude (`7.5–9.0×` at `α=0.01`
vs. the official `8.7–11.2×` worst-case-across-σ figure — consistent,
since my run used one mid-range σ rather than the worst σ=0.0005 cell).

**Finding, for the record:** `phase4_results.md`'s phrase "exactly as
predicted from the lower `lev9_Rq`" is accurate for **direction** and
reasonably accurate for the **relative jump between cycles** (naive model
predicts a `~2.2×` worsening from exp-073 to exp-074; observed is
`~1.6×–2.1×` — same order, slightly overpredicted), but is **not**
accurate as a claim about `lev9_Rq` alone predicting the **absolute**
inflation magnitude, which it underpredicts by a consistent `~1.6–2.7×`
factor in both cycles via any natural translation I could construct. This
is not a new defect — `NOTES.md`'s own "Learned" section already says
`lev9_Rq` "correctly predicted the DIRECTION... but could not have
predicted its MAGNITUDE" — but `phase4_results.md`'s "exactly as
predicted" phrasing sits in tension with that more careful statement
elsewhere in the same cycle's own record and should be reconciled (R4-
shaped, minor, non-outcome-determining: the Combined Verdict does not
change either way).

---

## 3. The circular-shift leg's 5× additional failure — mechanistically explained, and it is NOT evidence of a genuine second (T28-relevant) contributor

This is the most substantive new finding in this review, not previously
in the record.

**3a. What the per-config residuals actually look like.** I characterized
the four configs' own real per-config carrier-fit residuals
(`per_config_residuals`, the calibration leg's own raw material):

| Config | std | lag-1 autocorr | best-fit period (deg) | R² of that fit |
|---|---|---|---|---|
| C40 | 3.96e-3 | 0.936 | 6.72 | 0.757 |
| C60 | 4.44e-3 | 0.933 | 6.38 | 0.734 |
| C70 | 4.51e-3 | 0.926 | 6.34 | 0.701 |
| C80 | 4.53e-3 | 0.922 | 6.28 | 0.679 |

Cross-config correlation (same θ-index): **C40×C60=0.997, C40×C70=0.995,
C40×C80=0.992, C60×C70=0.999, C60×C80=0.997, C70×C80=1.000.** These
residuals are not four independent noisy series — they are, to within
0.3–0.8%, **the same shape**, shared across all four `ABSORB` depths. A
quadratic-in-`u` fit removes 57–67% of each config's residual variance
(coefficients −5.0 to −5.5, consistent sign and magnitude across configs)
but leaves the cross-config correlation at 0.99+ even after detrending —
this is real, common-mode, θ-dependent structure whose own best-fit
"period" (6.3–6.7°) is essentially the window's own span (~6°), i.e. it
is a smooth, roughly one-hump-per-window trend, not a sub-window
periodicity. **This is Idealization 7's own already-disclosed curvature
gap and QUANTUM's own exp-072 Phase-5 finding ("large curvature
coefficients... model misspecified") — not a new discovery — but nobody
in this cycle's Phases 1–4 actually looked at what the calibration leg's
residual pool contains, and it matters for how that leg's result should
be read.**

**3b. Why the circular-shift leg blows up: destroying real cancellation,
not exposing real difference-signal.** Because the four configs' residuals
are near-identical, in the REAL, correctly-aligned data they very largely
CANCEL in `resid_A − resid_B`. I measured this directly:

| Pair | std(real `delta_ab`) | std(real, zero-shift `resid_A−resid_B`) | mean std(independent-random-shift null delta) | ratio (null vs. real-aligned) |
|---|---|---|---|---|
| C40–C60 | 9.16e-4 | 5.86e-4 | 5.58e-3 | **9.5×** |
| C60–C70 | 2.74e-4 | 2.06e-4 | 5.96e-3 | **28.9×** |
| C70–C80 | 1.58e-4 | 1.40e-4 | 6.04e-3 | **43.2×** |

The circular-shift leg draws `sA, sB` **independently** for each of
`K_CAL=1000` synthetic H0 datasets. Because the shared systematic is a
smooth, non-periodic (window-bounded) hump rather than a genuinely cyclic
process, an independent re-anchoring of each config's copy of it does not
preserve anything physically meaningful about the *pair* — it manufactures
a synthetic `delta_ab_null` with **6–43× more variance than the real,
correctly-aligned residual difference actually has**, purely because two
near-identical curves, once shifted relative to each other by an
arbitrary random offset, stop cancelling. This is the direct, quantified
mechanism behind the leg's 38.9×–46.1× nominal rejection rate: it is not
that real θ-correlated noise of the kind actually present in the data
would produce a false positive at that rate — the real, unshifted,
correctly-paired noise is *smaller* than the observed `delta_ab` signal
itself, not 6–43× larger. The leg is "genuinely order-preserving" in the
narrow, literal sense claimed (every pairwise lag within one 31-point
vector survives a circular shift), but that guarantee says nothing about
preserving the cross-config alignment that determines `delta_ab`, and
independent shifting destroys exactly that.

**3c. Answer to the task's specific question.** Does this suggest a
genuine second contributor to T28's mechanism, visible via an
uncontaminated route? **No — this should be killed immediately per R5's
look-elsewhere discipline, for four independent reasons, not one:**

1. **Wrong signature.** A real `ABSORB`-tied (config-specific) mechanism
   must show up in the *difference* between configs. What's actually
   driving this failure is the opposite — a *shared, common-mode*
   component (r=0.992–1.000) that is nearly orthogonal to what a
   differential test could ever attribute to one config over another.
2. **Wrong scale.** Its own characteristic length (6.3–6.7°, ≈ the window
   span) matches neither T21's 1.9608° fringe nor the ~2.5° T28 family —
   it is ordinary window-scale curvature, already named (Idealization 7),
   not a new resonant feature.
3. **Manufactured, not exposed, by construction.** §3b shows quantitatively
   that the "signal" driving the 38.9×–46.1× figure is 6–43× larger than
   what genuinely exists in the real, correctly-aligned data — an artifact
   of the leg's own independent-shift choice, not a faithful stress test of
   realistic between-config noise.
4. **Textbook R5 shape.** `K_CAL=1000` draws × independent `(sA,sB)` pairs
   (961 possible combinations) × `N_SURR_CAL=4000` sign-flip surrogates is
   an enormous, unregistered search space with no target period, no R3
   resolution check ever run on this specific residual pool, and no
   pre-registered claim this leg was meant to test anything beyond
   calibration. Treating its failure rate as evidence *for* a mechanism,
   rather than *about* the null construction, is precisely the dense-
   search-finds-something trap R5's addendum and this cycle's own new R7
   both exist to police, one instrument class further along.

**The one legitimate, narrow, already-known takeaway:** this independently
reconfirms, via a new computational route, that the single-carrier-plus-
ramp model's curvature misspecification (Idealization 7) is real and
substantial (57–67% of per-config residual variance) — not new physics,
but a solid additional data point supporting PHOTONICS' already-queued
WKB/adiabatic boundary-reflectance model (Iteration-51 queue item 4),
which is exactly the kind of common-mode, θ-dependent boundary effect this
residual shape would predict.

**3d. A methodological flag for future reuse of this null idiom.** The
circular-shift leg's billing — "the harder, more realistic case," "the
first test... to genuinely expose θ-correlated real-residual structure" —
should be softened. What it actually demonstrates is that *independently*
circular-shifting two highly-correlated, non-periodic residual vectors is
a poor proxy for realistic between-config noise (§3b). A future reuse of
this construction elsewhere in the program (any carrier/phase-conditioned
fit with a similarly common-mode systematic between the two series being
differenced) should use a **synchronized** shift (same `s` for both
series, or shift only the *difference* vector) if the intent is to
probe realistic residual correlation without this artifact. This does not
change exp-074's own Combined Verdict — the i.i.d. leg alone already fails
every cell, decisively, exactly as exp-073's own precedent established —
but the "5× worse, first genuine exposure of correlated structure"
framing overstates what was actually shown.

---

## 4. R6/`G0-e`, R7, and Checkpoint scope — no new firing

The script never scores a p-value against a constructed null before the
calibration gate is checked, and `combined_verdict` is correctly computed
in the gate-first order specified in `phase3_synthesis.md`. R7 (adopted
this cycle) is applied consistently: the design-only `lev9_Rq` pricing is
explicitly *not* treated as sufficient on its own (§2 above shows exactly
why it should not be — direction yes, magnitude only approximately). I
find no Checkpoint-4-shaped defect in this cycle's own record: the
"exactly as predicted" overclaim (§2) is minor, non-outcome-determining,
and sits in tension with a more careful statement elsewhere in the same
document rather than being defended against contradicting evidence — the
R4-shaped pattern, not the R6-Iteration-50 pattern. My §3 finding is new
information, not a correction of a claim someone already made and
defended; it does not retroactively fire Checkpoint criterion 4 either.

---

## 5. Verdict

**PARTIAL.** The underlying instrument (`CHECK0`, the `X9`/`X8` fit, the
generalized sign-flip null, `lev9_Rq`, both calibration legs) is correctly
built and I independently confirm every load-bearing computational claim
in `phase4_results.md`: `E[R_q^surr]=0` exactly by a general algebraic
property (not merely re-verified numerically); `lev9_Rq` is coded
correctly and correctly predicts the *direction* and *approximate relative
size* of exp-074's worse-than-exp-073 failure, though not its absolute
magnitude via any simple translation (a real, quantifiable, previously
undisclosed ~1.6–2.7× gap, traced to leverage-weight concentration/
non-Gaussian tails); and the circular-shift leg's much larger failure is
real and reproducible but is best explained as an artifact of applying
independent shifts to two near-identical, common-mode, non-periodic
residual curves, not as evidence of a genuine second T28-relevant
contributor — that specific reading should be killed, not chased, per R5.
T28's own mechanism question (what produces the ~2.5° family) remains
exactly where exp-072 left it: unresolved, and this is confirmed as the
sixth consecutive non-decisive cycle on the differential/two-tone
sub-thread, with the pre-committed forward-lock (`phase3_synthesis.md`
§6) correctly stated and, in my independent judgment, correctly binding.

---

## 6. Ranked top-3 candidate directions for Iteration 52

1. **PHOTONICS' WKB/adiabatic boundary-reflectance analytic model for the
   graded `ABSORB` boundary** (already-queued Iteration-51 item 4, zero
   FDTD, queued and dropped twice before). My own §3a finding
   independently strengthens the case for running it now rather than a
   third time deferring it: the per-config residuals left over after the
   single-carrier fit are dominated (57–67% of variance) by a
   near-identical, common-mode, θ-dependent systematic across all four
   `ABSORB` depths — exactly the class of boundary-admittance effect this
   model would predict analytically. Modeling it out properly (rather than
   letting it leak into every future differential fit's residual pool, as
   it has been doing silently since at least exp-072) is now independently
   motivated by data, not just by charter rotation.
2. **A cheap, disclosed R3-style resolution/provenance check on the
   per-config residual's own ~6.3–6.7° common-mode shape**, before it is
   used to justify or falsify item 1: is it real boundary curvature, or a
   Yee-grid/window-taper artifact at the dense-sweep's own edges? This
   reuses already-collected multi-`cpl` data from exp-069/071 (no new
   FDTD), and gates whether item 1's model is explaining a real feature or
   chasing a discretization artifact — the same R3 discipline this program
   has applied to every other "surprising feature" for six years running,
   not yet applied to this specific residual.
3. **G40/`PAD` decorrelation** (already-queued item 2, ~31 calls) — the
   only queued item that actually relieves, rather than discloses, the
   `ABSORB`-or-`PAD` confound; orthogonal to items 1–2 and the cheapest
   FDTD relief on the board.

**Explicitly not recommended:** any further attempt to fit `R_q` (single-
or multi-tone) on this exact ramped-quadrature-OLS basis via a sign-flip
or permutation null, at any window. This cycle's own pre-committed
forward-lock already says so; my own §3 finding adds an independent reason
to hold that line — even this cycle's good-faith attempt to build a
"genuinely order-preserving" fix (per Red Team's own docket item 7)
surfaced a *new*, previously unrecognized construction-specific artifact
(§3b–d) rather than closing the class. Three consecutive attempts at this
instrument class (exp-072's phase-randomization, exp-073's pooled
bootstrap, exp-074's circular shift) have each individually failed for a
*different* reason discovered only after building it — that pattern itself
is evidence the family, not just any one member of it, needs retiring in
favor of a qualitatively different approach, exactly as already decided.
