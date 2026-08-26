# PHASE 2 — CRITIQUE · Panel Iteration 51 · exp-074
## THERMODYNAMICS

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md: where absorbed energy
goes; owns the per-proposal energy sidecar, analytic and labeled as such).
Blind to all other seats this cycle. Every number below was independently
re-derived by invoking the actual committed `desk_check_pricing.py` module
and its own functions (`carrier_fit`, `design_matrix`, `tone_cols`), never
taken from prose or hand-typed (LOGBOOK R4).*

---

## 0. Sidecar disposition

**Confirmed genuinely N/A, not by omission.** `grep -in "energy\|power\|joule\|watt\|temperature\|absorb"` on `desk_check_pricing.py` returns only unrelated string matches (`power-up`, `absorb-depth-causal-test` — path components of reused directories). No absorbed-power number, ΔT, emission band, or detectability statement is computed or implied anywhere in the script; `ABSORB`/`PAD` enter only as which already-collected series is loaded, exactly as Idealization 2 states. My own lane's charter engages nothing here.

**Citation-provenance note (checked per this cycle's mandate, non-load-bearing here).** Idealization 9's "(house precedent)" descends from a mislabeled citation already living in the record: exp-072's `phase2_critique_thermodynamics.md` and `phase2_redteam_audit.md` both cite "house precedent, Iteration 5, exp-027" for the "deferral by argument, not omission" rule — but LOGBOOK.md's own section headers show exp-027 is **Iteration 4** (line 3104) and Iteration 5 is exp-028 (line 3450); the actual quoted sentence ("exp-026 carried an explicit one-line deferral clause...") sits at LOGBOOK.md:3206, inside the Iteration-4 entry. The mislabel has now survived three documents (exp-072 Phase 2 critique, Red Team audit, Phase 5 materials review) uncorrected. exp-074 doesn't repeat the wrong number (it just says "house precedent" with no iteration cited), so this isn't a fresh instance chargeable to this cycle — but it is exactly the kind of citation drift R4 exists to catch, and it is still sitting in the record uncorrected. Flagging now per the task's own instruction, before a fourth document inherits it.

---

## 1. Independent re-derivation

Ran `desk_check_pricing.py` directly: `CHECK0 pass=True worst_rel_err=0.00e+00`, and all printed per-pair/widened-window numbers reproduce the proposal's tables to the last digit. The design-only quantities (`cond5`, `cond9`, `VIF_Rq`, `lev_ratio`, `L(T)`) are correctly computed from the stated formulas — I re-implemented `L_of_T`, the leverage ratio, and the VIF from scratch in a second script and matched the committed output exactly.

Then I did the one thing the committed script — and both of its informal Iteration-49 ancestors — never does: **actually fit the real 9-column two-tone design to the real `delta_ab` data**, rather than only pricing its Gram-matrix conditioning. Result, `coef9 = pinv(X9) @ delta_ab`, real residuals, real `sigma9`:

| Pair | `z_ols` (5-col) | `z_joint` (optimistic, proposal's) | `z9` (**actual 9-col fit, this critique**) | `RSS9/RSS5` |
|---|---|---|---|---|
| C40–C60 | 4.90 | 0.81 | **0.84** | 0.50 |
| C60–C70 | 3.04 | 0.54 | **5.03** | 0.19 |
| C70–C80 | 4.25 | 0.76 | **1.63** | 0.06 |
| C40–C80 | 4.66 | 0.78 | 0.35 | 0.35 |

At **3 of 4 pairs the true joint-fit `z` exceeds the "optimistic upper bound"** — at C60–C70 by **9.3×** (5.03 vs. 0.54), blowing through not only the CLOSURE-CONFIRM ceiling (`z_joint<1.5`) but the WIDENED-WINDOW-LICENSES-FURTHER-SPEND floor (`z≥2.0`) that this proposal reserves for a ~51° window not yet run. The mechanism is visible in the RSS column: adding 4 correlated columns at `cond9≈480–529` cuts residual sum-of-squares by 50–94%, i.e. `sigma9` drops far more than the `(n-p)` bookkeeping alone would produce — the two-tone model is absorbing substantial real variance in `delta_ab` that the "optimistic" pricing assumed would stay in the noise floor.

---

## 2. Steel-man (150 words)

This is real instrument engineering, not another informal Phase-5 number. `CHECK0` re-derives the basis at machine precision against exp-072's own committed record before anything is cited, closing exactly the class of defect (hand-typed "precisely recomputed" figures) that R4 exists to prevent. Pricing all four `ABSORB` pairs — not the one EM happened to check informally — and connecting `lev_ratio` to `G0-e(ii)`'s own algebraically-exact `mean diag(M5)=(n−p)/n` genuinely generalizes two disconnected Iteration-49/50 findings into one coherent design-theoretic picture. The widened-window phase-sweep (64 nuisance-phase combinations, `cond5` asserted phase-invariant in-script) is real robustness discipline, not a cherry-picked angle. Idealization 6 already, honestly, flags that `z_joint(optimistic)` "assumes...identical to what the single-carrier fit measured" and that real data "could easily show a worse effective SNR" — the proposal itself names the exact axis my critique below exploits, one direction short of the full statement.

## 3. Sharpest attack (150 words)

`z_joint(optimistic)` is not an upper bound; it is an unvalidated assumption dressed as one, and real data on the committed pipeline refutes it directly. Actually fitting `X9` to real `delta_ab` (§1, above) — never done anywhere in `desk_check_pricing.py` — shows the true joint-fit `z` **exceeds** the "optimistic" figure at 3 of 4 pairs, by 9.3× at C60–C70, crossing both the CLOSURE-CONFIRM ceiling and the WIDENED-WINDOW 2σ floor on the *current, unwidened* window. This is the energy-balance analog my seat exists to catch: a quantity labeled a physical bound that the ledger doesn't actually close in one direction. Whether this is a genuine second physical contributor or `cond9≈500`-driven overfitting is exactly what a null-calibration test (permute/sign-flip the second tone's phase, check the empirical rejection rate) would settle — and the proposal explicitly declines to run one, pricing the design instead of the fit. §6's formal-retirement decision rule cites CLOSURE-CONFIRM as "decisive... independent of which null eventually gates it." It is not: the fit itself, before any null, already disagrees with the bound the decision rests on.

## 4. Verdict

**Oppose** — specifically §5's CLOSURE-CONFIRM framing and §6's pre-committed formal-retirement rule, not the diagnostic machinery itself (CHECK0, `L(T)`, `lev_ratio`, the widened-window pricing all stand and are useful independent of this attack). Retiring a 5-cycle sub-thread on a bound that a two-line extension of the committed script shows does not hold, on this exact data, is exactly the kind of process the panel's own R4/R5/R6 lineage was built to prevent recurring a further time.

## 5. Flip

Add the actual 9-column fit (`coef9`, real `sigma9`, real `z9`) to `desk_check_pricing.py`'s output for all four pairs, alongside `z_joint_optimistic`, and report both. If `z9` stays comparably small at real data (my computation shows it does not, at 3 of 4 pairs) — or if a cheap permutation/sign-flip control on the second tone's phase shows the large `z9` values are exactly what `cond9≈500`-driven overfitting produces under pure noise — then CLOSURE-CONFIRM and §6's retirement rule can stand as originally argued. Absent that check, §6 should be downgraded from a binding formal retirement to a disclosed, provisional finding.
