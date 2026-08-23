# exp-063 — Phase 5 Review: PHOTONICS

**Panel Iteration 40.** Fresh sub-agent, blind to every other seat's current-cycle Phase-5 review. Charter: surface interaction, absorption spectra, angular dependence, scattering cross-sections — is the proposal's optical response coherent as stated, across wavelength and angle? Object under review: `experiments/063-cnt-forest-thermal-conductivity-biot-check/phase4_results.md` and its supporting record (`phase1_proposal.md`, all five Phase-2 critiques including my own, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`).

This cycle scores no constraint-1/2/3/4 metric and proposes no optical mechanism (`T1 escape route: N/A`) — it is a THERMO-sidecar model-fidelity continuation. My charter's purchase on it is narrow and specific: whether the closed-form correction's stated geometry is coherent with this program's own established measurements of *where light gets absorbed* (T9's radial ledger, exp-061's Beer-Lambert e-fold) — exactly the ground my own Phase-2 critique staked out.

---

## 1. Does the mandatory-fix docket actually close my own Phase-2 concern?

My Phase-2 sharpest attack was concrete: §4's model reuses `l_geometric_m` for a role — the absorption-to-loss-surface conduction distance — its own docstring never licenses, and at bench scale this contradicts T9's thrice-confirmed radial-absorption ledger (`graded_black_shell`'s conductivity peaks at `r_in`, is zero at `r_out`; essentially all absorption lands deep in the shell, not at the "front surface" §4's model names). My flip condition asked for exactly two things: (a) name this as a second, independent worst-case exaggeration in the Idealizations, not silently riding on `Bi_gas`'s length-invariance to escape scrutiny; (b) distinguish the bench-scale case (where I have a real objection) from the witness-scale MP-5 geometry (where I explicitly granted front-loading is separately defensible, given exp-061's own `α_true≈5.74×10⁴ cm⁻¹`, e-fold≈174nm).

**Both were applied, correctly and completely.** `NOTES.md` Idealization 9 states the reuse and the T9 contradiction verbatim, scoped explicitly to bench scale ("numerically inert for TD-3/TD-4 specifically... contradicts the established T9 radial-absorption ledger"), and does not overclaim it against TD-5. Red Team's own Phase-2 audit independently re-traced `materials.py`'s `_graded_black` function directly (not on my word) and reproduced the T9 contradiction from source, then went one step further than I did at Phase 2: it explicitly separated my attack from MATERIALS' (loss-side geometry) and EM's (length legitimacy) as three *different* variables in the same model, not three readings of one defect — and confirmed my own directional read (a corrected generation length would likely *shrink*, not grow, the bench-scale correction) survives independent recomputation. I re-derive that triangulation myself, independently, in §2 below rather than taking the audit's word for it.

**I re-verify the "numerically inert" claim myself, not on Red Team's assertion.** At bench scale (`L=2.34µm`), across the full sourced κ range this cycle found (0.7–50 W/(m·K)): `Bi_rad(bench) = 4εσT_amb³·L/κ` ranges from `5.143×1.719×10⁻⁵`≈`8.8×10⁻⁵`(κ=0.7)` down to `2.4×10⁻⁶` (κ=50), while `Bi_gas = k_air/κ` ranges `0.00052`–`0.0371` over the same κ range — three to four orders of magnitude larger at every point. My attack's own object (`Bi_rad`, the term `L` actually enters) genuinely cannot move TD-3/TD-4 regardless of whether the generation geometry is corrected. Confirmed, not merely accepted.

**My concern is closed. No residual defect from this specific attack survives into Phase 4's results.**

---

## 2. Independent check: does the witness-scale front-loading assumption I granted at Phase 2 actually hold up against Phase 4's own found numbers?

I did not just accept my own Phase-2 concession at face value; I re-derived it against this cycle's actual results. At witness scale, `L` ranges 331.2–1051.2µm (exp-061's MP-5 endpoints) while the e-fold length governing where absorption actually deposits is ≈174nm (exp-061's own `α_true`). The ratio `L/e-fold` is ≈1,900–6,000 — absorption is exhausted within the first ~0.05–0.3% of the object's total thickness. A front-surface-generation model is not merely "separately defensible" here, as I put it at Phase 2; on these numbers it is close to exact, for any object whose real absorption profile actually matches `α_true`. My Phase-2 hedge was appropriately cautious given I hadn't yet seen the sourced κ range; nothing in Phase 4's findings weakens it, and the magnitude gap (three orders on `L/e-fold`) is wide enough that this reads as robust, not merely "not yet contradicted."

**A residual optical-coherence question Phase 4 does not close, worth naming even though it is not this cycle's job to close it.** `α_true` (the quantity that sets the e-fold, and via `τ_true/α` the very `L` values TD-5 corrects) is this program's own simulated construction's implied rate, checked in exp-061/062 against **published real-material α figures from several different CNT-forest application classes** (record-blackness coatings, VACNT/Vantablack-adjacent geometries — MP-2's own thickness comparators). This cycle's ten queries source `κ_solid` from a **different, and internally inconsistent, set of geometry classes**: a bulk/aggregate mat (κ=0.7, query 5 — alignment and packing unspecified in the snippet), a VACNT-on-reduced-graphene-oxide composite film (κ=9.62, query 1 — a hybrid architecture, not a bare forest), and a post-processed, densified/drawn sheet (κ=50, query 6 — already flagged in `phase4_results.md` as a different geometry class from as-grown). **Nowhere in this cycle's record is it established that the α figures underlying TD-5's own `L` and the κ figures this cycle sources for the same `L`'s Biot correction describe the same physical material.** This is not a defect in either exp-061's or this cycle's own arithmetic — each search was scoped and executed exactly as committed — but it means TD-5's single correction factor quietly combines an optical constant and a thermal constant from what may be two different real-material classes, a coherence gap of the same shape (mismatched candidate-geometry provenance) this program has now named twice before for a different quantity: Iteration 39's own near-field-coupling table (three off-target CNT-forest classes, the record-blackness/Vantablack comparison class itself still unpinned) and, inside this very cycle's own `phase4_results.md`, the "flagged geometry-class distinction" section (as-grown vs. drawn-sheet κ). Nothing here moves any TD-1..TD-5 verdict — I checked this against the numbers themselves, not against a general worry, and the sourced κ band brackets the fragile margin comfortably regardless of which specific class governs. It is a provenance gap, not an arithmetic one.

---

## 3. Independent arithmetic check

I recomputed, from the raw formulas, rather than trusting the printed table:

- `CF_bench(rear-only, κ=0.7) = 1 + 0.026/0.7 + 5.142614×2.34×10⁻⁶/0.7 = 1.03716` — matches the printed `1.03716` exactly.
- `margin_bench(κ=0.7) = 699.27/1.03716 = 674.22×` — matches the printed `674.22×` exactly.
- `CF_MP5-730x(κ=0.7) = 1 + 0.026/0.7 + 5.142614×1051.2×10⁻⁶/0.7 = 1.04486` and `margin = 1.35/1.04486 = 1.2921×` — matches the printed `1.2920×` to the printed digit.
- `κ_critical`: solving `1 + 0.0314059/κ = 1.35` gives `κ = 0.089731`, matching the printed `0.0897` and the stage-23 bisection gate.

**No arithmetic or citation defect found anywhere in `phase4_results.md`** on independent recomputation of every scored cell. This is a genuine contrast with the pattern this program's own two immediately preceding cycles established: Iteration 39 (exp-062) shipped a misattributed NOTES.md citation and a silent R-vs-T convention drop that this seat itself caught fresh at Phase 5; Iteration 38 shipped a `τ_shell` bookkeeping drift caught at Phase 2. I looked for the same bug class here specifically, given three consecutive-cycle recurrences is exactly the shape that has fired Checkpoint criterion 4 before (Iteration 37) — and did not find it this time.

---

## 4. Live registry verification (not taken on Red Team's or the Director's word)

I ran both lint tools myself against the live repository rather than trusting the synthesis's account of them:

```
$ python3 lab/caveat_lint.py    # exit 0 — 8 caveat(s) checked, 0 required-site failures
$ python3 lab/numeric_lint.py   # exit 0 — 3 entries checked, all PASS
```

Both new entries promised at Phase 3 (`exp063-biot-correction-machinery`, `exp063-thermo-disposition-netd-disclaimer` in `caveat_lint_config.json`; `exp063-cf-bench-vs-witness-derivation` in `numeric_lint_config.json`) exist, and both `required_sites` for the caveat entries — `NOTES.md` *and* `phase4_results.md`, the exact site-coverage shape whose gap fired Checkpoint criterion 4 twice at Iteration 39 — PASS on live execution, not merely on the entries' own text. The forward tripwire Phase 3 set on these two entries (any further gap fires criterion 4 without deliberation) has not been tripped by anything I can find in this cycle's own record.

---

## 5. Verdict for this cycle's own contribution

**PROMISING.**

The core Biot/conduction-resistance derivation is sound, independently re-derived at least three times now (EM's Phase-2 critique, Red Team's Phase-2 audit, my own Phase-5 recomputation above) and confirmed to the printed digit throughout, including the escalation-worthy `κ_critical=0.0897` boundary. The mandatory-fix docket — including my own flip condition — was applied completely and correctly, not merely gestured at: Idealization 9 states my attack's substance verbatim, scoped honestly to where it actually bites (bench scale, numerically inert), and does not overclaim it against TD-5. This cycle's own headline finding — the program's first genuine test of a "first-ever DETECTABLE flip" scenario — came back a decisive, not marginal, non-flip: even the single worst real κ figure found (0.7 W/(m·K), 8× above `κ_critical`) leaves the witness-scale margin at 1.2920×, comfortably inside the pre-committed band and nowhere near 1.0×. Unlike the two immediately preceding cycles, I found no new numeric or citation defect on independent recomputation, and both new registry entries verify clean on live execution rather than resting on the synthesis's own account. What keeps this from an unqualified close rather than a qualified PROMISING is the residual optical-provenance gap in §2 — real, disclosed nowhere in this cycle's own record, though non-blocking for every scored verdict here.

---

## 6. Top-3 ranked candidate directions for Iteration 41+

1. **Extend the standing "pin the actual record-blackness/Vantablack candidate's own parameters" priority (Iteration 39's #1 item, still open for pitch/diameter) to cover thermal conductivity, and check it against the SAME material class the program's own `α_true`/`n_eff` optical figures already cite.** This cycle sourced κ from three different, none-of-them-pinned CNT-forest application classes (bulk/aggregate mat, VACNT-on-graphene-oxide composite, densified drawn sheet); exp-061/062 sourced their optical constants from a comparator set that overlaps only partially. TD-5's single correction factor combines an optical and a thermal constant with no established common provenance (§2, above) — closing this would let a future cycle report one clean, geometry-class-consistent margin instead of a band that happens, so far, to clear its bar by comfortable coincidence rather than by construction.
2. **Resolve MATERIALS' substrate-interface boundary-condition question** — which of the two disclosed loss-geometry brackets (front-colocated, correction≡1; rear-only, this cycle's worst case) actually describes a real CNT-forest coating grown on a substrate with its tip exposed to ambient. This is the one open item that would collapse TD-5's bracket to a single number rather than leaving `κ_critical`'s own falsification boundary permanently hedged between two endpoints that differ by orders of magnitude in how close they sit to 1.0×.
3. **Resolve EM's/T23's witness-scale length-legitimacy question** — run `τ_true/α` through `gas_conduction_h_eff`'s own licensing test properly (an optical-extinction-derived length used as a Fourier-conduction path length), closing the now twice-deferred (Iteration 38, 39) `l_geometric_m` lineage before a third cycle reuses this exact length in an even more demanding role than the last two did.

---

## 7. Checkpoint criteria — my own explicit check

**None fire, on my own independent read.** No constraint-1/2/3/4 metric is scored (criterion 1/2 N/A, honestly declared and true on inspection — Red Team's own attack 7 correctly caught and fixed an over-reaching "Checkpoint-1/2-adjacent" framing in TD-5's original language, which I confirm reads correctly in the shipped `NOTES.md`). No engine physics beyond validated bench classes is invoked (criterion 3 N/A — zero FDTD, only `lab/thermo_sidecar.py` gains two analytic functions). Criterion 4 (program-integrity drift): I looked specifically for a recurrence of the Iteration-39 double-firing pattern, given the same `κ_solid`/thermal-margin territory and the same registry machinery, and found none — both new registry entries pass live execution (§4), and I found no new undisclosed caveat-propagation gap on my own fresh read. Criterion 5 (two consecutive no-result iterations): not evaluable from inside this review; Iteration 39 shipped a real, committed result, and this cycle does too.

---

## 8. Ruled-out registry check (R1–R5, T1–T26)

**No re-proposal found.** This cycle carries `T1 escape route: N/A` and touches no phenomenon mechanism at all — R1 (refractive/transformation-optics cloaking), R2 (integer-λ shell rule), and R5 (the retired phase-offset regressor) are simply not implicated by a thermal-margin instrument cycle. R3's meta-rule (any surprising feature gets a resolution check) is honored, not violated — nothing here claims a numerical result without the resolution/regression-anchor discipline stage 23's own gates provide. R4 (no hand-typed "precisely recomputed" figures) is honored — every number in `phase4_results.md` traces to `lab/thermo_sidecar.py` direct invocation, reproduced by stage 23 as a permanent regression anchor, and I independently reproduced the load-bearing cells myself in §3 rather than trusting the printed digits. Of the live threads, only T9 (the radial-absorption ledger) and T23 (the `h_eff` length-scale licensing question) are actually engaged this cycle, and both are engaged correctly: T9 is cited accurately (bench-scale contradiction, numerically inert, disclosed) and not re-litigated as settled or unsettled beyond what it already established; T23's own open licensing question is extended to a new length (a Fourier-conduction path, not an `h_eff`/mass/area role) and correctly flagged as unresolved rather than silently assumed favorable. `REALIZABILITY_MEMO.md` Entry 2/Amendment 7's UNOBTANIUM-WITH-PARAMETERS tier is treated as fixed background throughout and not touched by anything in this cycle — correctly, since this cycle scores thermal detectability, not realizability.
