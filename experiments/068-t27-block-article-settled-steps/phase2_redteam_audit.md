# Phase 2 Red Team Final Audit — exp-068 Proposal (Iteration 45)

Red Team receives the Phase-1 proposal and all five blind Phase-2 critiques (above); no seat saw Red Team's view, Red Team is not blind to theirs.

## 1. Deferral-count adjudication (direct read, not taking either side's word)

**VISION is correct; EM's Phase-1 Section 6 is wrong, off by one cycle.**

- `PLAN.md:2424-2436` (Iteration-44 close, written before this proposal existed): *"VISION's Block-ARTICLE settled-STEPS FDTD leg (T27), now **FOUR consecutive cycles (Iterations 42→43→44)** without being a cycle's primary FDTD work... Iteration 45 is ELECTROMAGNETISM's turn by rotation; EM should either take this as a scoped secondary item with a real call ceiling stated up front, or explicitly disclose a **fifth-consecutive-deferral line**."*
- `LOGBOOK.md:13846-13852` (Iteration-44 close, same text independently confirmed): identical language, "now four consecutive cycles" / "explicitly disclose a fifth-consecutive-deferral line."

EM's Phase-1 Section 6 states "3 consecutive iterations so far (42,43,44)" and "4th consecutive miss." Both program-of-record files, written before this proposal, use "FOUR"/"four" and "fifth." VISION's critique quotes these verbatim and correctly. **Corrected in Phase 3.**

## 2. Numbered attacks

**[inconsistency] Attack 1 — Tier0/Tier1 double-counts 4 FDTD calls, nobody caught it.** Tier0's 8 calls = article-present ±35°×{600,750nm}×{C40,C80}. Tier1's first block = article-present **all 9** `FALLBACK_ANGLES`×{C40,C80}×600nm = 18 calls — but `FALLBACK_ANGLES` *includes* ±35°, so 4 of those 18 calls are bit-identical re-runs of 4 of Tier0's 8 (FDTD is deterministic — a second run adds zero information). None of the six seats caught this. **Fix: Tier1's article-present block should be the 7 interior angles (14 calls, not 18), correcting the total to 8+28+2=38.**

**[inconsistency] Attack 2 — the deferral-count error (§1 above).**

**[constraint-#3-violation risk] Attack 3 — the hidden constraint-3 angle none of the five critiques (or EM) surfaced.** exp-066's own Phase-5 mandatory fix M3 (`phase4_results.md:48-50`) exists *specifically* because a raw "GATE_HARD fails 31/36→34/36" headline is liable to be misread as a constraint-3 finding: *"GATE_HARD is not VISION's own perceptual bar, and this result does not by itself move any constraint-3 verdict."* This sentence has **no mechanical guard** — `lab/caveat_lint_config.json` contains zero phrase_pattern/required_site entry for it. EM's P-068-5 introduces 14 brand-new GATE_HARD tallies (interior angles, empty scene) and nowhere commits to restating M3's scoping sentence at that reporting site. If exp-068 reports "≥12/14 pass" without it, a future citation could silently misreport a GATE_HARD result as bearing on the Tier-A/Tier-W ambient-appearance verdict. **MANDATORY.**

**[inconsistency, in a critique's own flip] Attack 4 — PHOTONICS' flip condition is not mechanically implementable as written.** PHOTONICS writes "both C40 and C80" but the proposal's actual Tier2 is "C40 only, (-35,600nm) and (-35,750nm)" — one config, two wavelengths. PHOTONICS' own text instead specifies one wavelength/two configs — a different 2-call design that silently drops the -35°/600nm/C40 convergence check. Budget-neutral either way (2 calls), but the Director must pick one explicit definition.

**[verified, no defect found] Attack 5 — independent numeric check against committed files.** Cross-checked against `experiments/065.../phase4_results.md:46-47,250-251` and `settled_sweep_steps2800_diagnostic.json`: baseline STEPS=1400 values match exactly; sign-flip table matches exactly (STEPS=2800 value -0.0043973 rounds to the cited -0.00440); `T5_THERMAL_CAVEAT` is real (`design_geometry.py:182-188`) and genuinely absent from EM's reuse list — THERMODYNAMICS' attack is fully grounded; `caveat_lint_config.json` has zero T5/thermal-caveat entry — confirmed by grep.

**[process gap, sharpens Attack 3] Attack 6 — the same required_sites gap-shape that fired Checkpoint criterion 4 twice (Iteration 39) is live again here, unaddressed by any seat.** The `exp065-steps1400-unsettled-plane-channel` entry's `required_sites` is still hardcoded to exp-065's own two files; nothing adds exp-068's forthcoming `NOTES.md`/`phase4_results.md`. Neither EM's proposal nor any of the five critiques plans to widen this entry's `required_sites`.

**[nuance on a critique] Attack 7 — THERMODYNAMICS' flip is correctly grounded but understates why it's now urgent, not merely tidy.** exp-065's own Phase-5 Red Team audit (`phase5_redteam_audit.md:386-391`) explicitly ranked registering a `T5_THERMAL_CAVEAT` lint entry as "Recommended, non-blocking... before any future cycle cites this article's caveats." exp-068 is precisely that "future cycle." This elevates the flip from nice-to-have to **MANDATORY**.

**[verified] Attack 8 — MATERIALS' claim that PASS is a live, non-remote outcome, and the REALIZABILITY_MEMO wording it cites, both check out verbatim.** No defect in MATERIALS' attack.

**No genuine conflict exists between any two of the five critiques' flip conditions.** They touch disjoint sections and are additive — all five (with Attack-4's disambiguation) can be applied simultaneously.

## 3. Reconciled docket for the Director

**MANDATORY before synthesis into a run:**
1. Correct Section 6 to the program's own record: "now FOUR consecutive cycles... fifth consecutive miss if failed."
2. Fix the Tier0/Tier1 double-count (Attack 1): Tier1's article-present block = the 7 interior `FALLBACK_ANGLES` only (14 calls).
3. Resolve PHOTONICS' flip (Attack 4) by explicit Director choice — recommended: extend Tier2 to both configs, both λ (4 calls total), using the margin freed by fix 2.
4. Carry `T5_THERMAL_CAVEAT`, `REALIZABILITY_MEMO_CAVEAT`, `G_TRANSFER_T15_CAVEAT` verbatim into every new site stating Block ARTICLE's C value/bucket.
5. Carry exp-066's M3 GATE_HARD-vs-`C_THR_LAB` sentence verbatim to every site reporting P-068-5's GATE_HARD tally.
6. Pre-commit the REALIZABILITY_MEMO.md Amendment action on a PASS flip.
7. Widen `exp065-steps1400-unsettled-plane-channel`'s `required_sites` to add exp-068's files.

**Nice-to-have:** QUANTUM's Block-MINI citation tripwire — cheap, add the one-line NOTES.md tripwire.

## 4. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.** The mechanism is expressible and falsifiable, T1-N/A classification is correct, numeric claims checked against committed files hold up, and none of the seven mandatory items above are physics changes — all are scope/arithmetic/disclosure corrections landable same-shift with the run, matching this program's own "found-before-close, fixed-same-shift" non-firing precedent.

## Hidden constraint-3 check (explicit, per Director's charge)

Covered by Attack 3 above: the risk is not that this cycle violates constraint 3 itself (instrument-verification class, no constraint-3 claim made), but that a future citation of its GATE_HARD tallies could be *misread* as a constraint-3 finding absent M3's scoping sentence. Mandatory fix 5 closes this.
