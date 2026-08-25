# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 50 · exp-073

*Fresh sub-agent, PHOTONICS charter (PANEL.md: surface interaction,
absorption spectra, angular dependence, scattering cross-sections — is the
proposal's optical response coherent as stated, across wavelength and
angle?). Blind to all other Phase-2 critiques this cycle.*

## Steel-man (146 words)

exp-073 does what a clean re-issue should: every design choice is tagged by
evidentiary class (a/b/c, §3) so no threshold traces to exp-072's
contaminated observations, directly closing the gap Red Team's own
contamination ruling named. The sign-bug's root cause is structurally
foreclosed, not patched: `A_q = 2a_cbar·tanχ₀` is re-derived from the exact
two-tone identity rather than assumed small-angle, and `dR_q/dψ̄ ≡ R_i` is
asserted as a hard identity at every synthetic cell, not merely observed
post hoc. `G0-e` is genuinely strengthened before Phase 4: 1,728
recovery-accuracy cells plus a new 24×500×20,000-draw calibration sweep
tests the sign-flip null's own size, not only the point estimator —
directly answering T2-3's own justification with a falsifiable,
pre-registered HALT. Every numeric threshold (Rayleigh floor, wrong-carrier
displacement, Holm structure) derives from window geometry alone. For
instrument-integrity re-verification work, this is disciplined and
appropriately humble about what a `NEITHER` would still mean.

## Sharpest attack (130 words)

`G0-e(i)`'s synthetic pairs are `A = a·cos(2πu/T_A−ψ₀)`,
`B = a·cos(2πu/T_B−ψ₀)`: identical amplitude and identical phase for both
members of every one of the 1,728 cells (verified against exp-072's own
`run.py`: `C_A=a0*cos(w_A*u-psi0)`/`C_B=a0*cos(w_B*u-psi0)`; exp-073 changes
nothing here). So `a_B−a_A=0` and `Δψ=0` identically, always. The tripwire
"`A_i` must match `a_B−a_A` within 1% where `|a_B−a_A|≥1e-4`" can never fire
(`0≥1e-4` is always false): `A_i`, reported throughout P-073-1/6, is never
checked against known ground truth. exp-072's own version instead checked
`A_i` against the directly *measured* real `a_B−a_A` (6.5%/2.8% off) —
exp-073 relabels it "class (c)... not data-derived," contradicting its own
§3 taxonomy. And `χ₀=πΔf·x̄+Δψ/2` names `Δψ` a real contributor, yet `G0-e`
never exercises it: the gate has a structurally unreachable branch on the
channel a real boundary-phase change would most plausibly move.

## Verdict: **support-with-changes**

## Optional — parameter change that would flip to plain support

Make `G0-e(i)`'s synthetic generator carry independent amplitudes
(`a_A ≠ a_B`, e.g. sweep `δa/a ∈ {0, 0.03, 0.10}` alongside the existing
grid) and an independent phase offset for each member of the pair (a true
`Δψ` sweep decoupled from `Δf`, e.g. `Δψ ∈ {0, ±0.3, ±0.8}` rad on top of
the existing `T_A`/`ΔP`/`ψ₀` sweep) — zero new FDTD cost, a handful more
`lstsq` calls, fully consistent with the design's own "sharpen `G0-e`, not
just re-run it" mandate. That restores a live check on the `A_i` channel and
genuinely stress-tests `χ₀`'s two physically distinct sources (period shift
vs. independent phase shift) rather than only the one the current
construction can produce.

---

## Supporting detail — the derivation behind the attack

**1. Why `a_B−a_A=0` and `Δψ=0` are baked into `G0-e(i)`'s construction, not
incidental.** §4's own text: *"Synthetic ground truth: congruent pairs
`A=a·cos(2πu/T_A−ψ₀)`, `B=a·cos(2πu/T_B−ψ₀)` on the real 31-point θ grid."*
Both series share the same `a` and the same `ψ₀` symbol by construction —
the only free difference between them is period (via `T_A` vs. the implied
`T_B` from `ΔP`). This is not a paraphrase; it reproduces exp-072's own
committed generator verbatim (`experiments/072-t28-differential-beat-fit/
run.py`, function `ground_truth_recovery_check`: `C_A = a0 * np.cos(w_A * u
- psi0)`, `C_B = a0 * np.cos(w_B * u - psi0)` — one `a0`, one `psi0`, for
every one of the sweep's cells). exp-073's stated "widened coverage"
(§4 G0-e(i): more `T_A`, `a`, `ΔP`, `ψ₀` values) widens the *marginal*
ranges of these shared parameters; it does not add a `δa` or `Δψ` axis. No
cell in the 1,728-cell sweep — old or widened — has ever had `a_B≠a_A` or an
independent phase between the two members of a pair.

**2. Why this makes one of the document's own named tripwires dead code.**
§4 G0-e(i): *"Two cheap assertion tripwires, carried forward from exp-072's
own T1-2 (both class (c), formula-derived, not data-derived): `dR_q/dψ̄`
must equal `R_i` to within 1e-6 at every synthetic cell...; `A_i` must match
the directly-constructed `a_B−a_A` to within 1% at every cell where
`|a_B−a_A|≥1e-4`."* Since `a_B−a_A≡0` in every synthetic cell by
construction (point 1), the qualifying condition `|a_B−a_A|≥1e-4` is false
everywhere in the sweep, so this clause can never evaluate on a nonzero
target — it is written as an active check but is unreachable as written.
This is exactly the class of thing this program's own R4/verify-before-claim
discipline exists to catch: a check *described* as running is not the same
as a check that *can* run.

**3. This is a real regression from exp-072's own version of the same
tripwire, not merely an unchanged inherited gap.** exp-072's redteam audit
(`experiments/072-t28-differential-beat-fit/phase5_redteam_audit.md`,
T1-2) specifies this tripwire differently: *"`A_i` must match the directly
**measured** `a_B − a_A` within 10% at pairs where `|a_B − a_A| ≥ 1e−4`
(C40–C60 and C40–C80: measured 6.5% and 2.8%..."* — a check against the
**real, measured** amplitude difference in the actual FDTD curves (nonzero
by measurement, not by construction), reported as a genuine cross-check
result (6.5%/2.8%). exp-073's rewrite ("directly-**constructed** `a_B−a_A`,"
tolerance tightened from 10% to 1%, moved under the *synthetic* `G0-e(i)`
heading, and explicitly reclassified "not data-derived") reads as an
attempt to fold this into the pure-synthetic sweep. If that reading is
right, the check is now vacuous (point 2). If instead the intent was to
keep it as the real-data check, then its class label — "(c)... not
data-derived" — directly contradicts §3's own a/b/c taxonomy, since a check
against measured `a_B−a_A` on real FDTD output is data-derived by
definition. Either reading is a defect; the document does not disambiguate
which one was intended, and Phase 3 needs to settle it explicitly, in code,
before this gate is trusted to have covered what it claims.

**4. Why this is a PHOTONICS-lens issue, not a bookkeeping nit.** `χ₀ =
πΔf·x̄ + Δψ/2` is the model's own statement that the phase offset between two
angularly-resolved fringes at window centre has two physically distinct
sources: a spatial period difference projected onto the window centre
(`πΔf·x̄`) and an independent phase offset (`Δψ`) that carries no
period/frequency information at all. A boundary whose graded-absorption
depth changes (the actual physical knob varied between `C40`/`C60`/`C70`/
`C80`) is at least as likely, on ordinary boundary-optics grounds, to shift
the **reflection phase** at the graded interface as it is to shift the
**spatial period** of the angular interference pattern — a longer graded
taper changes the effective admittance profile the field sees, which is a
phase effect, not inherently a periodicity effect. `A_q = 2a_cbar·tanχ₀`
(the phase-difference readout) and the `R_q→Δf` mapping this cycle relies on
both depend on `χ₀`, but `G0-e` can only ever generate `χ₀` through the
`Δf·x̄` route (since `Δψ≡0` throughout the sweep) — meaning the pipeline has
never been certified accurate in the regime where a real config-to-config
difference is phase-dominated rather than period-dominated. That is exactly
the regime a graded-absorption-depth boundary is most likely to produce, and
exactly the gate `R6`/`G0-e` was created to close before any real pair is
scored.
