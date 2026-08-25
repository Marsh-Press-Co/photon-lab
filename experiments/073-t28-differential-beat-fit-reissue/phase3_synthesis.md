# PHASE 3 — SYNTHESIZE · Panel Iteration 50 · exp-073
## Director's synthesis: Red Team's 12-item docket accepted in full; four self-caught implementation issues disclosed

## 1. Accept/override statement (PANEL.md, non-negotiable)

Red Team's Phase-2 audit verdict: **PROCEED-WITH-MANDATORY-FIXES, 12 items**
(`phase2_redteam_audit.md`). The audit itself overrode **nothing** from the
five blind critiques — every diagnosis, and every offered remedy except one,
was independently re-verified and adopted verbatim (§2 of the audit: "No
finding from any seat is overruled"). The one partial exception is QUANTUM's
own two candidate null-construction fixes (Freedman–Lane on `resid0`;
leverage-studentized `resid5`) — the audit does not mandate either (neither
reliably clears G0-e(ii)'s own calibration bands in the audit's own
independent testing), which QUANTUM's own critique had already hedged as
acceptable ("whichever is adopted, G0-e(ii) must stay a binding,
non-relaxable HALT"). This is a **refinement** of QUANTUM's own position,
not a reversal, and the audit itself frames it that way.

**The Director accepts Red Team's audit in full, verbatim, with zero
overrides of the docket itself.** This matches the posture the task's own
framing anticipated ("the expected posture is: accept the docket in full").
What follows is not an override of anything in the docket — it is disclosure
of four implementation-level problems the docket did not, and could not,
anticipate, because they only surface once the 12 items are actually coded
against the real 31-point design matrix and the real inherited machinery.
Per the task's own instruction ("if you do, disclose it explicitly... Do not
silently patch around a docket item"), each is recorded below, in the open,
with the resolution chosen and why.

## 2. Docket items 1–12: how each was implemented

**A. `G0-e` completeness and reporting**

1. **Independent `δa`/`Δψ` axes added to `G0-e(i)`.** Implemented as two
   additional sweep legs (`leg_delta_a`, `leg_delta_psi` in
   `ground_truth_recovery_check`), each holding `T_A=2.49°`, `a0=0.005`
   (the primary grid's own mid-point — "alongside," not fully crossed, per
   PHOTONICS' own "zero new FDTD cost, a handful more `lstsq` calls"
   framing) while sweeping `δa/a ∈ {0.03, 0.10}` (768 cells) and
   `Δψ ∈ {±0.3, ±0.8}` rad (1,536 cells) respectively, each still crossed
   against the full `ΔP` (12 signed values) and `ψ_bar` (32 phases) axes for
   genuine coverage. Total G0-e(i): 5,760 cells (3,456 primary + 768 + 1,536).
2. **`A_i` tripwire disambiguated as option (a)**: kept purely synthetic,
   labelled class (c), now genuinely live (768 cells qualify at
   `|target_A_i| ≥ 1e-4` once `δa≠0`; dev-run: 0 failures at 1% tolerance).
   Option (b) — a real-data cross-check at 10% tolerance, as exp-072's own
   `T1-2` had it — was not additionally implemented; option (a) alone
   satisfies the docket's own "do not leave the current draft's
   self-contradicting label standing" requirement, and adding a second,
   real-data-touching tripwire inside a gate whose entire point is to run
   *before* any real data is scored would be a strange thing to bolt on
   without the docket asking for it.
3. **`G0-e(ii)` kept as a binding, non-relaxable HALT, construction
   unmodified.** Neither QUANTUM's candidate fix is adopted. The full
   24-cell × 3-α calibration table is persisted for **both** legs
   (`g0e_ii.iid_leg.table`, `g0e_ii.residual_structure_leg.table`)
   regardless of outcome, and the Combined Verdict emits the named branch
   `HALT_NULL_MISCALIBRATED` (not a generic `HALT`) when it fires.
   **Independently re-reproduced this cycle**: a dev run (see §4) gives
   empirical rejection rates 2–6× nominal on the i.i.d. leg — matching
   Red Team's own Attack 4 figures almost exactly — confirming both that
   the docket's prediction (§6: "the most likely Phase-4 outcome... is
   `HALT_NULL_MISCALIBRATED`") is realistic and that this file's own
   sign-flip-null implementation is faithful to the audit's specification
   (a bug in my own construction could just as easily have hidden the
   miscalibration rather than reproduce it).
4. **Residual-structure robustness leg added**, drawing from a pooled
   124-point residual distribution (the four configs' own already-committed
   `_fixed_period_fit` residuals at each config's native `n_grid=400`
   `p_star_deg`, from `experiments/069-.../results.json` and
   `experiments/071-.../results.json`), bootstrap-resampled and rescaled to
   match each cell's own nominal `σ` so the two legs' tables are directly
   comparable side by side (see Ambiguity 2, below, for the disclosed
   judgment call this required). Both legs must pass for `G0-e(ii)` to
   clear — Attack 7's own "can only be as bad or worse" argument is read
   here as a **conjunctive** requirement, not an independent, optional
   second look.

**B. Estimator, coefficient-table, and gate corrections**

5. **`A_q="binds hard"` prose corrected.** `run.py` now loads exp-072's own
   real, already-closed `A_q`/`amplitude` values at runtime
   (`load_data()`'s `exp072_disclosure` dict) and derives `χ0_real` and the
   `tan/sin` ratio programmatically (never hand-typed — the R4 lesson
   applied a second time in this same file, since item 6 needed it too).
   `a_priori_disclosure()` reports both the naive a-priori estimate and the
   real, class-(b) expected value side by side, with an explicit note that
   the correction is expected to remain numerically inert on this exact
   substrate. **T2-4 required no code change** — `A_q` is, and always was,
   the OLS-fitted coefficient; whether one calls it `2a·sinχ` or `2a·tanχ`
   is a matter of which trigonometric identity is exact, not a different
   number. The fix is entirely in the documentation layer (this file,
   `NOTES.md`, and `run.py`'s own comments).
6. **Power table and P-073-4 rate reference re-anchored** to
   `saturating_vs_linear.linear.slope` loaded at runtime from
   `experiments/072-.../results.json` (`m0_resolved =
   0.002463678368980155`, R²=0.8328), with `m0_native` (exp-071's own
   `n_grid=400` slope, `0.0025563909774436134`) carried alongside only as
   the historical/Iteration-48-native anchor. `injection_recovery()` now
   takes `m0_resolved` as its predicted-effect basis. `saturating_vs_linear()`
   is still computed fresh in `run.py` (a **regression check**, permitted
   under the contamination ruling) and asserts `matches_exp072_slope` —
   confirmed bit-close in the dev run (§4).
7. **T2-1 clause (vi) implemented self-contained, no forward reference.**
   `carrier_q95()` computes one q95 per pair, in-run, from that pair's own
   sign-flip surrogate ensemble (built at the pair's own fitted `(T_x,
   ψ̄)`) — see Ambiguity 1, below, for the disclosed judgment call in how
   "that candidate's own" is read. The non-emptiness floor is implemented
   exactly as specified: `t21_not_evaluable=True` (and therefore
   `resolved=False`) whenever both `T_delta` and `T_wrong=1.2591°` fail
   their own admissibility test against that shared q95 — never vacuously
   passed.
8. **Admission/exclusion outcome for `1.2591°` disclosed at every pair.**
   `wrong_admissible`, `wrong_admissibility_stat`, and
   `t21_admitted_carriers` are reported in every pair's dict unconditionally
   (P-073-1/P-073-5). In the forced-pass dev exercise (§4, gates stubbed to
   validate the scoring path only — **not** an official result), `1.2591°`
   was excluded at all four pairs and `T_delta` admitted at three of four —
   the exact pattern Red Team's own Attack 5b quantitative estimate
   predicted from exp-072's published `q95` figures as a proxy.

**C. Contamination disclosure**

9–11. Implemented as `_contamination_block()`, computed unconditionally in
   `score_all()` and attached to every run's output as
   `results["scored"]["contamination"]`: the extended disclosure paragraph
   (item 9), the forward-lock statement (item 10), and a
   `confirm_disclosure_required`/`confirm_disclosure_text` pair that
   evaluates to `True`/the full required text automatically whenever the
   Combined Verdict is `CONFIRMED`, `p073_2=="CONFIRM"`, or any individual
   pair reaches `resolved=True` (item 11 — "wired into `phase4_results.md`
   generation logic" is read here as: the data a future Phase-4 report
   generator needs is computed and flagged automatically in `results.json`,
   so the disclosure cannot be omitted by oversight when that file is
   written; see §5.3 of the task's own instructions, which explicitly
   defers `phase4_results.md` itself to the next step). Verified this
   toggles correctly both ways in isolation (§4).

**D. Minor / documentation**

12. **Idealization 13's citation corrected** from "Iteration 5" to
    "Iteration 2" in `NOTES.md` (see NOTES.md Idealization 13).

## 3. Four self-caught implementation issues, disclosed (not docket items)

None of these are overrides of the docket — they are places where coding
the docket's own text against the real machinery required a decision the
docket did not make, or surfaced a defect in my own first-draft
implementation that I found and fixed before this commit, in the open, the
way exp-072's own Director found and disclosed `_amp_phase_at`'s missing
`w·x̄` shift.

**Ambiguity 1 — what does "that candidate's own sign-flip surrogate
ensemble" mean for `T_wrong=1.2591°` (docket item 7)?** Two readings exist.
(A) Each candidate (`T_delta`, `T_wrong`) gets a *separately re-anchored*
null — rebuild `X5`/`X4` at that candidate's own `(T_x, ψ)`, generate its
own sign-flip surrogates, run a fresh free-period search on each, and derive
a candidate-specific `q95`. (B) One shared `q95`, calibrated once per pair
from the sign-flip null anchored at the pair's own fitted `(T_mean, ψ̄)`
(exactly exp-072's own clause-(iv) construction), reused as the threshold
for *every* candidate's admissibility test (`|Tx_candidate − T_x|/T_x ≤
q95`). I adopted **(B)**, for three reasons, stated here rather than
silently chosen: (i) it is what Red Team's own Attack 5b used as its
quantitative proxy (`phase2_redteam_audit.md` §1 Attack 5b's table compares
both `T_delta` and `1.2591°`'s ratios against the *same* `q95` column); (ii)
it is the direct, minimal generalization of exp-072's own already-verified
clause-(iv) code, which only ever had one candidate and one q95; (iii)
reading (A) would multiply `G0-e`-adjacent compute by a full free-period
search per surrogate per candidate per pair, well beyond anything the
docket's own §9 budget ("a few minutes single-core, dominated by G0-e(ii)")
contemplates, for a distinction the docket's own text does not clearly
require. This is a genuine ambiguity in item 7's own phrasing, not
adjudicated by the audit (VISION's original critique did not run the real
estimator and explicitly did not compute `q95`); reading (B) is disclosed
here as the implementation's actual behavior, verified to reproduce Attack
5b's own qualitative pattern (§4).

**Ambiguity 2 — does the residual-structure leg (item 4) share G0-e(ii)'s
`σ`-grid, or drop it?** The proposal's own §4 G0-e(ii) text defines the
grid (`σ ∈ {0.0005,0.002,0.008}`, `ψ0` over 8 phases) only for the i.i.d.
leg; item 4's own text ("Repeat the calibration sweep using resampled real
per-config residuals... instead of i.i.d. Gaussian noise") does not say
whether the resampled residuals should be used raw (one leg, no `σ` axis)
or *rescaled* to each nominal `σ` (24 cells, directly comparable to the
i.i.d. table). I implemented the latter — bootstrap-resample the pooled
124-point residual set, then rescale by `σ/std(pool)` — because item 3(a)'s
own instruction ("Report both legs' calibration tables side by side")
reads most naturally as a like-for-like, cell-for-cell comparison, which
only a matched grid supports. Disclosed here since the alternative (one
un-rescaled leg, no `σ` axis) is an equally defensible reading of the
literal text.

**Ambiguity 3, a genuine bug caught in development — G0-e(i)'s own
generator's `χ0` baseline.** My first-draft synthetic generator for
`G0-e(i)` set `χ0 = π·Δf·x̄ + Δψ/2` unconditionally, copying
`phase1_proposal.md` §2b.3's *real-data-interpretation* formula (itself an
`x=0`-extrapolation convention EM's own critique derived for the actual
analysis pipeline, `analyze_pair`, untouched by this cycle). This gave the
**primary** leg (`δa=0, Δψ=0`) a nonzero baked-in `χ0` that exp-072's own
already-validated generator does not have — verified directly: exp-072's
generator shares one `psi0` between both tones (`C_A=a0·cos(w_A·u−ψ0)`,
`C_B=a0·cos(w_B·u−ψ0)`), which forces the window-centre (`u=0`) phase gap
to be *exactly* zero, not `π·Δf·x̄`. Running the widened generator with the
inherited formula gave a worst-cell recovery error of **78%** on the
primary leg — a HALT, and a wrong one, since it would have HALTed the cycle
on a defect in this file's own new synthetic machinery, not on anything the
docket's estimator actually does. Caught by regression-testing the
widened generator's primary leg (`δa=0`, `Δψ=0`) against a standalone
reimplementation of exp-072's own original, already-Phase-5-verified
generator (worst-cell 0.15%) before trusting the new code — the same
discipline the task's own instructions describe for exp-072's
`_amp_phase_at` catch. **Fixed** by defining `χ0` for this synthetic-only
generator directly as `Δψ/2` (the window-centre phase gap, swept as an
independent parameter on its own terms), decoupled from the
`x=0`-extrapolation convention that governs the real pipeline's own,
untouched, `A_q`/`χ0` interpretation. Post-fix: primary-leg worst-cell
error 0.35%, `δa`-leg 0.28%, `Δψ`-leg 1.10% — all comfortably inside the 2%
bar. This choice is disclosed in `run.py`'s own inline comment at the point
`χ0` is defined, not only here.

**Ambiguity 4, a second bug caught in development — the sign of
`dR_q/dψ̄` in `G0-e(i)`'s own identity tripwire.** LOGBOOK/`phase5_
redteam_audit.md` (exp-072, item K/C19) states `dR_q/dψ̄ ≡ R_i` "to 5
decimals," and `run.py` (inherited, unchanged) aliases `dRq_dpsi = R_i`
directly. Building a genuine finite-difference check for `G0-e(i)`, my
first attempt perturbed this file's own generative nuisance parameter
(`ψ_bar`, regenerating the synthetic data and refitting `(T_x, ψ)` at each
perturbation) — giving a *systematic* ~3×10⁻⁴ discrepancy against `R_i`,
too large for the 1e-6 bar and, on inspection, not even a clean derivative
(since `_amp_phase_at`'s own fit on a genuinely two-tone `C̄` only
approximates the driving phase, the perturbation conflates two different
effects). Switching to the construction that actually matches what
exp-072's own audit verified — hold the **data** fixed, perturb
**`design_matrix`'s own `psi` argument** directly — gave a clean,
`O(ε²)`-limited numerical derivative, but with the **opposite sign** from
`R_i`: independently re-verified against exp-072's own four real, published
`(T_x, ψ, R_i)` triples, `dR_q/d(design_matrix psi) = −R_i` to 10 decimals
at all four pairs, not `+R_i`. Reconciled: `_amp_phase_at`'s own docstring
already states `psi = -atan2(fit["b"], fit["a"])` — i.e., `design_matrix`'s
code-level `psi` is the *negative* of the `φ=atan2(b,a)` symbol the
write-up's own trigonometric derivations use as "`ψ̄`." So
`dR_q/dψ̄_symbol = −dR_q/d(psi_code) = −(−R_i) = +R_i`, exactly matching
exp-072's own audit finding once the sign convention is made explicit
rather than assumed. **Fixed** by negating the finite-difference formula to
match the write-up's own `ψ̄` convention; post-fix worst-cell identity error
is `9.4×10⁻¹¹` (dev run), five orders of magnitude inside the 1e-6 bar. Both
this and Ambiguity 3 are disclosed in `run.py`'s own comments at the
tripwire's definition, in addition to here.

## 4. Development validation (permitted per house discipline; NOT the official Phase-4 result)

Per the task's own instructions, `run.py` was run repeatedly during
development, including on the real 124-point data, to debug and to
regression-check against exp-072's own already-published numbers. This
section discloses exactly what was checked and confirms no threshold was
touched as a result (docket items 9–10's own requirement).

- **Regression check against exp-072's real numbers (permitted, per the
  contamination ruling §3):** `load_data()`'s `exp072_disclosure` dict
  reproduces exp-072's own published `A_q`, `amplitude`, and the derived
  `χ0 = arctan(A_q/2a)` bit-exact from `experiments/072-.../results.json`
  for all four pairs (`−0.0197 / −0.0203 / −0.0062 / −0.0434` rad,
  matching `phase2_critique_em.md` and `phase2_redteam_audit.md` Attack 2
  to the printed digit). `saturating_vs_linear()`'s own fresh re-derivation
  of the `n_grid=3000` slope matches the loaded `m0_resolved` value to
  better than `1×10⁻⁹` (`matches_exp072_slope=True`). **No threshold was
  set, moved, or tuned as a result of any of these checks** — they exist
  purely to confirm this file's own re-derivations agree with the
  already-closed, non-contaminating record, exactly as the contamination
  ruling (`phase2_redteam_audit.md` §3) permits and exp-072's own Director
  did to catch `_amp_phase_at`'s bug.
- **Full official-shaped dev run (real data, real gates, unmodified
  thresholds):** `python3 run.py`, ~125 seconds. `G0-a/b/c` all PASS.
  `G0-e(i)` PASSES (worst recovery-ratio error 1.1%, both tripwires clean —
  see §3's two disclosed fixes, above, for what it took to get there).
  `G0-e(ii)` **HALTs** — both legs fail badly (empirical rejection rates
  2–6× nominal on the i.i.d. leg, independently reproducing Red Team's own
  Attack 4 figures to within simulation noise), so **Combined Verdict:
  `HALT_NULL_MISCALIBRATED`**, exactly matching §6 of the audit's own
  forecast ("the most likely Phase-4 outcome... is
  `HALT_NULL_MISCALIBRATED`"). This is expected, correctly-triggered
  behavior, not a defect — it is `G0-e(ii)` doing the job R6 and the
  docket's own item 3 built it to do. Because the gate fires, **no real
  pair was scored in this dev run**, and this run's own `dev_results.json`
  was deleted after inspection — it is not part of the committed
  deliverable and no number from it is reported as this cycle's result.
- **Downstream-pipeline validation (gates stubbed to `pass`, real data,
  otherwise unmodified thresholds — explicitly a debug exercise, not a
  scored run):** confirmed `analyze_pair`, the Holm adjustment, `RESOLVED`'s
  six-clause conjunction, `P-073-2/3/4`, injection-recovery's H0-clean
  identity (`Rq_recovered == Rq_pred` exactly, matching exp-072's own
  post-fix identity), and the Combined-Verdict decision tree all execute
  without error and produce internally consistent output (e.g., `T_wrong`
  excluded at all four pairs, `T_delta` admitted at three of four — the
  exact pattern Red Team's Attack 5b predicted from exp-072's own published
  `q95` figures). Combined Verdict under this stub: `NEITHER`. **This
  number is explicitly not a result** — it used stubbed gates and exists
  only to confirm the scoring code path is free of crashes and gross logic
  errors before commit.

## 5. Disclosed reading of an internal inconsistency in `phase1_proposal.md` §7

The Combined-Verdict text ("1. HALT ⟺ any of G0-a/b/c/e(i)/e(ii) FAIL, **or
any pair exceeds G0-d**. Nothing is scored.") conflicts with G0-d's own row
definition two paragraphs earlier ("`cond>100` → that pair `ILL_CONDITIONED`,
**excluded from every downstream gate**" — a per-pair exclusion, not a
global halt). `run.py` implements the **row's** semantics (a failing pair is
excluded via RESOLVED clause (i), never a global HALT), matching exp-072's
own precedent (`ill_conditioned` there is per-pair, not gating the whole
run) and avoiding an undesirable asymmetry where one badly-conditioned pair
would silently discard three good ones. Disclosed here as required rather
than silently resolved; not a docket item, since G0-d is unchanged
machinery the docket did not touch.

## 6. Contamination discipline (docket items 9–11, restated in one place)

**What was checked against exp-072's real numbers, and why it's permitted:**
`load_data()` and `saturating_vs_linear()` both load and/or re-derive
exp-072's own already-published, non-contaminating figures (`A_q`,
`amplitude`, the resolved slope) — regression checks on unchanged machinery,
exactly the class the contamination ruling (`phase2_redteam_audit.md` §3)
names as expected and necessary, the same way exp-072's own Director used
`T_mean` agreement to isolate the `ΔP` sign bug. **What was never done:** no
gate, band, or threshold anywhere in `run.py` was set, moved, or tuned with
reference to any of exp-072's real per-pair `A_q`, `a_cbar`, `A_i`, `R_i`,
`R_q`, `ΔP`, or their signs — `T_WRONG_DISPLACED`, `SAT_DECAY_L`,
`N_GRID_CARRIER`, `HOLM_PAIRS`, every `G0-e` sweep range, and every
Combined-Verdict threshold are all inherited unmodified from data-free
derivations, and the four disclosed implementation fixes in §3 above were
each corrected against a data-free or already-independently-verified
target (a formula, a sign-convention cross-check against exp-072's own
`R_i`, exp-072's own already-Phase-5-verified generator), never against
this cycle's own outcome. The full disclosure paragraph and forward-lock
statement are implemented in code (`_contamination_block()`) and reproduced
in `NOTES.md`.
