# PHASE 2 — BLIND CRITIQUE · QUANTUM OPTICS · Panel Iteration 50 · exp-073

*Seat charter: non-classical absorption, state-dependent or coherent
interactions; mechanisms enter the bench only as effective classical
parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or Red Team strikes
them. Fresh sub-agent, blind to the other five Phase-2 critiques. This seat
wrote the exp-071 Rayleigh-resolution argument this whole differential-fit
approach exists to route around, the `L(T)` leakage function, the a-priori
power table this cycle's §2c inherits, and — at exp-072 Phase 5 — proposed
the sign-flip/residual-permutation null exp-073's §3b T2-3 claims to adopt.
Everything numerical below was independently computed, not taken from
prose.*

---

## Disclosure — what was computed, and on what data

**Nothing in this critique uses any real T28 field value** (no `C40`,
`C60`, `C70`, `C80`, no `delta_AB`, no exp-069/071/072 `results.json`
content). Everything below is a **synthetic** stress-test: pure Gaussian
noise (`y = ε`, `ΔP_true ≡ 0`) pushed through the *exact* inherited,
unchanged machinery §3a claims is "settled" — the real 31-point 36.0°–42.0°
θ grid (public window geometry, already load-bearing in every T28 cycle
since exp-069), `CENTER_DEG = 39.0`, and `design_matrix()`'s literal
`T_x = radians(T_deg)·cos(CENTER_DEG)`, `θ_c = (2π/T_x)·u + ψ` construction,
copied verbatim from exp-072's committed `run.py` (§2b/§3a state this basis
is inherited unmodified). This is exactly the class of check the proposal's
own §4 sanctions as data-free (a "forward simulation of the proposal's own
noiseless model," the precedent exp-072's Red Team used for Attack 4) and
is precisely what G0-e(ii) itself is supposed to run. I am previewing that
gate's own result, not scoring the real cycle. Reconstruction fidelity
check: my synthetic design matrix reproduces `cond(X5) ≈ 60`, matching
exp-072's independently-verified 59.9–61.0 exactly — I am not testing a
different design by accident.

## What I found

`T2-3` as literally specified — sign-flip (or permute) the **5-column,
full-model** residual `resid5`, add it to the **4-column, H₀-fit**
prediction `yhat0`, refit, take `|R_q^surr|` — is centered correctly
(`E[R_q^surr]=0` verified to machine precision, `~1e-15`, confirming
`yhat0 ∈ span(X4)⊂span(X5)` as claimed) **but its variance is badly
miscalibrated, in the anti-conservative direction.** Monte Carlo (6,000
independent H₀-noise draws × 4,000-surrogate null each, six carrier
periods/phases spanning the proposal's own G0-e ranges):

| Nominal α | Empirical rejection rate (pure H₀ noise) |
|---|---|
| 0.01 | **0.049 – 0.061** (5–6×) |
| 0.05 | **0.108 – 0.132** (2.2–2.6×) |
| 0.10 | **0.160 – 0.188** (1.6–1.9×) |

Consistent across every carrier/phase tried — this is not seed noise. The
mechanism is a leverage effect, not a sign error: `resid5_i` has variance
`σ²·(M5)_ii` where `M5 = I−X5·pinv(X5)` is the OLS projection matrix; its
diagonal averages `(n−p)/n = 26/31 = 0.839` (matches simulation,
`E[resid5²]=0.835`), but the `R_q`-extraction row of `pinv5` — which reads
off a *ramp* coefficient — weights almost entirely onto the
**highest-leverage points, at the window's edges**, exactly where `(M5)_ii`
is *smallest*. The leverage-weighted ratio `E[Var(R_q^surr)]/Var(R_q^obs)`
is **0.79**, i.e. the surrogate's spread is ~89% of the true sampling SD —
enough, given how concentrated the weighting is, to produce the 2×+
rejection-rate inflation above (confirmed by a closed-form normal
approximation using that exact ratio, independent of the Monte Carlo). I
also checked the two off-the-shelf fixes: leverage-studentizing `resid5`
by `1/√(M5)_ii` before sign-flipping *improves but does not fully close*
the gap (α=0.05 empirical → 0.084); reverting to the **textbook**
Freedman–Lane construction — sign-flip `resid0` (the true H₀-restricted
residual), not `resid5` — also improves but does not fully close it (0.070
at nominal 0.05). At `n=31, p=5` (16% of the sample spent on parameters,
concentrated on a narrow window), this design sits in a regime where
simple residual-based nulls are known to be hard to calibrate exactly; none
of the three constructions I tried lands inside G0-e(ii)'s own tolerance
band.

**Consequence for the design as written.** G0-e(ii)'s own calibration
bands (`α±3√(α(1−α)/K)`, e.g. `[0.021, 0.079]` at α=0.05, `K=500`) are far
too tight to admit a ~0.11–0.13 empirical rate — so *if implemented
faithfully*, the cycle's most likely outcome is **HALT at G0-e(ii), before
any of the four real pairs is ever scored** — not the elaborate
`P-073-2`–`P-073-6` analysis the rest of the document is built to run. That
is the design's safety net working as intended, not a silent
false-positive risk reaching `LOGBOOK.md` — but it means the "corrected"
part of "corrected re-issue" is not yet correct, and the cycle as
pre-registered is very likely to spend its full budget and Phase 1–2
overhead to learn only that fact, extending an already five-cycle T28
instrument-validation thread by another non-advancing round (LOGBOOK
Checkpoint criterion 5's own standing concern).

---

## Steel-man (≤150 words)

The design discipline here is real. `T2-3` correctly diagnoses exp-072's
actual defect (a null built from the H₀-residual `resid0` leaves true
ramp signal in the surrogate pool, biasing conservative) and every other
ported fix — the exact `A_q=2a·tanχ` identity, the design-respecting
bootstrap, the leakage-minimized `T_wrong=1.2591°`, the telescoping-derived
Holm scope, `‖R‖` as disclosure not a second gate — is correctly re-derived
from formulas, not from exp-072's outcomes, exactly satisfying the
mandate's own contamination-retirement condition. Critically, this cycle
does not merely assert its null is calibrated: `G0-e(ii)` is a genuine,
pre-registered, zero-real-data test of that exact claim, with a HALT that
actually binds before any pair is scored. That is the correct epistemic
posture for a cycle whose entire purpose is repairing a prior calibration
failure, and it is stricter self-policing than exp-072 shipped with.

## Sharpest attack (≤150 words)

`T2-3`'s own justification — "`E[R_q^surr]=0` by construction, since
`yhat0∈span(X4)⊂span(X5)`" — proves only that the surrogate is *unbiased in
location*. It says nothing about its *variance*, which is what rejection
rates actually depend on. I verified by direct simulation, on the real
θ-grid geometry and the real inherited `design_matrix()` formula (zero real
field data), that sign-flipping the **full-model** residual `resid5` and
adding it to the **restricted-model** fit `yhat0` is a leverage-driven,
anti-conservative construction: empirical false-positive rates run
2.2–2.6× nominal at α=0.05 and 5–6× at α=0.01, driven by the `R_q` ramp
coefficient's weight concentrating on the window's highest-leverage
(edge) points, exactly where the full-model residual most understates true
noise. This is very likely to trip the cycle's own `G0-e(ii)` HALT — a
safe but wasted outcome — unless the null is fixed before Phase 3 commits
`run.py`.

## Verdict: **support-with-changes**

## Optional — the single change that would flip this to unqualified support

Replace §3b T2-3's literal construction with one of the two variants I
verified moves substantially toward calibration: (a) classical
Freedman–Lane — sign-flip/permute `resid0` (the H₀-restricted residual),
not `resid5`, still added to `yhat0` — which is also what the phrase
"Freedman–Lane-style" in the proposal's own text already claims to be but
is not as literally specified; or (b) leverage-studentize `resid5` by
`1/√(diag(M5))` before sign-flipping. Neither fully closes the gap at this
`n=31,p=5` design in my testing, so whichever is adopted, `G0-e(ii)` must
stay a **binding, non-relaxable HALT** — pre-register it now, not as a
discovery to explain away if it fires on the real (not just synthetic)
calibration sweep.
