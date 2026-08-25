# PHASE 2 — CRITIQUE · Panel Iteration 49 · exp-072
## THERMODYNAMICS on PHOTONICS' differential/beat fit of `delta_AB(θ)` (T28)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md seat: where absorbed energy goes; owns the per-proposal energy sidecar, analytic and labeled as such). Blind to all other seats this cycle.*

---

## Steel-man (≤150 words)

In energy terms the differential is the right instrument. `C_empty` is an **empty-scene** contrast — no object, no dissipative article, no absorbed-power number anywhere in the chain — so the only thing differing between `C_A` and `C_B` is how much power the graded boundary returns into the domain rather than retains. Everything common to both configs — the fixed `A=752` aperture response, T21's fringe, discretization offsets, the whole common-mode power bookkeeping — cancels identically in `C_B − C_A`. That is why `C80−C40` was legible at `ptp/mean=16.2` while the absolute per-config fits sat at `R²≈0.43–0.45`. The proposal then does the two things my seat usually has to demand: Idealization 3 forecloses the physical-medium reading of `ABSORB` *before* anyone can take it, and §2c/Idealization 9 concede the power shortfall a-priori with a fallback that forbids quoting `ΔP` for unresolved pairs. Restraint pre-registered, not discovered post-hoc.

## Sharpest attack (≤150 words)

**P-072-4 smuggles a physical model my seat owns: that boundary power-return falls *linearly* with absorber depth.** A graded absorber's residual return decays quasi-exponentially, so `ΔP` per cell must *shrink* with depth — and exp-071's own numbers do exactly that: per-pair rates **0.004135 / 0.001500 / 0.000000 °/cell** for 40→60 / 60→70 / 70→80. `m₀` (a four-point linear fit, R²=0.8664) is the *worst* description of that sequence, yet it centres both §2c's power table and P-072-4's CONFIRM band `[m₀/3, 3m₀] = [0.000815, 0.007331]`, required of **every** resolved pair. §1 itself bounds C70–C80 at one grid node: `|ΔP| ≤ 0.00752°`, rate `≤ 0.000752 °/cell` — **already below the CONFIRM floor**. If the deep pairs resolve, CONFIRM is unreachable a-priori, and CONFIRMED with it, on grounds unrelated to whether the instrument works. Idealization 9 covers the power consequence (deep-pair ramp ≈4.4% and ≤2.2%, not 7.2%); nothing covers the band.

## Charter checks (the parent-assigned scoping audit, non-gating)

1. **Energy sidecar: correctly out of scope — confirmed.** No absorbed-power number, no ΔT, no emission band, no detectability statement is produced anywhere in this design, and none *could* be: the reused 124 points are empty-scene contrast values with no article in the domain. My sidecar is genuinely N/A this cycle. **One cheap fix, per house precedent** (Iteration 5, exp-027: "exp-026 carried an explicit one-line deferral clause; this proposal has zero sidecar language, a step backward" — deferral by omission ruled worse than deferral by argument): add one sentence to §7 stating that no absorbed-power number is produced and the sidecar is therefore N/A, rather than leaving it silently absent. PANEL.md's metric table is nominally every-run; the exemption should be on the record, not inferred.
2. **No smuggled thermal or detectability claim found.** The nearest live risk — reading "deeper `ABSORB` = more absorption" as a physical energy statement — is pre-blocked by Idealization 3 ("a numerical boundary-condition parameter... a dependence on it is at least as likely to be a boundary artifact as a physical effect"). No VISION-threshold, `C_thr`, watt, or re-radiation language appears. Clean.
3. **PAD-decorrelation (Iteration-49 queue item 2, my own Phase-5 matched-PAD amplitude probe merged with QUANTUM's item (a)): named accurately, not pre-empted — but the caveat rule has a hole.** Idealization 2 is correct and unsoftened, and "A PAD-decorrelated config remains separately queued and is not this cycle's job" is the right characterization. However, the binding sentence — "**Any CONFIRM** from this cycle must be written as `ABSORB`-or-`PAD`-tied" — binds only a CONFIRM. **P-072-6 is non-gating** and will report `|A_i|/a` (an amplitude discriminator on the confounded axis — precisely the confounded arm of queue item 2) under *any* verdict, including the a-priori-most-likely NEITHER, escaping the rule as written. **Mandatory, one line:** extend the `ABSORB`-or-`PAD` writing rule verbatim to P-072-1 and P-072-6, and state that P-072-6 supplies the confounded arm of queue item 2 and does not substitute for it.
4. **Queue item 4 (PHOTONICS' own two-tone joint fit) is unnamed.** P-072-5 fixes `T` to T21's 1.9608° as a single-carrier wrong-carrier control; that is a contamination diagnostic, not a two-tone joint fit, and the proposal never says so. Per the same deferral-by-omission rule, name item 4 and re-defer it with a stated reason.
5. **R5 (null-permutation control): agree it is not triggered**, and the 20,000-surrogate Fourier-phase null with seed fixed in-file and Holm across four pairs is adopted correctly anyway. No ruled-out LOGBOOK R5 item resurfaces.

## Verdict

**support-with-changes.** The scoping is right, the sidecar is correctly absent, and nothing thermal is smuggled. What is smuggled is a *linearity* assumption about boundary power-return, embedded in the one gate that gates the Combined Verdict.

## The single parameter change that would flip me to support

**P-072-4's CONFIRM rate floor: `m₀/3` → `m₀/10` (0.000244 °/cell), with the REFUTE floor following to `m₀/30` to keep the bands nested** — and one sentence in §2c naming *sublinear* `ABSORB`-return as the a-priori physical expectation, so the tabulated ramp/carrier percentages read as upper bounds. That single edit makes a saturating result — the outcome the boundary physics predicts and exp-071's own three rates already display — scoreable as corroboration rather than excluded by construction, without touching any other band, gate, or threshold.
