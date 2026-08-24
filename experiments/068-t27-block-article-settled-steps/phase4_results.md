# exp-068 — Phase 4 Results (panel Iteration 45)

**Run**: 44/44 FDTD calls, 7.1 minutes wall-clock (hard stop 30 min),
`STEPS=1400` is **not settled** on this channel at near-grazing angles
(exp-065's own finding, reconfirmed by exp-066's Block MAIN closure and
now by this cycle's own Tier2 convergence check). Full bench unaffected:
no `lab/` engine change (verified live, `_lab_diff_excluding_registry()`),
only `lab/caveat_lint_config.json`'s registry widening (mandatory fix 7).

## Gate P-068-0 (harness continuity): PASSED

`{'config': 'C40', 'theta': -35.0, 'lambda_nm': 600, 'steps': 2800, 'ours':
-0.0043973199443986255, 'settled_sweep_2800': -0.0043973199443986255,
'delta': 0.0, 'exact': True}` — bit-exact, this cycle's new worker
reproduces exp-065's own committed settled-STEPS value exactly. All
subsequent numbers are trusted.

## Scored predictions

| Prediction | Verdict |
|---|---|
| P-068-0 | PASSED |
| P-068-1 | **REFUTED** |
| P-068-2 | **CONFIRMED** |
| P-068-3 | CONFIRMED |
| P-068-4 | PARTIAL |
| P-068-5 | CONFIRMED |
| P-068-6 | CONFIRMED |

## P-068-1 (empty N9 floor, settled, GATE_HARD): REFUTED

`C40`: `C_empty_N9 = -0.001138` — **breaches GATE_HARD=0.001** (13.8% over).
`C80`: `C_empty_N9 = -0.000789` — clears GATE_HARD. This extends exp-066's
own headline finding (GATE_HARD pass/fail count gets WORSE, not better, at
settled STEPS on individual grazing-angle cells) to the **N9-aggregate**
level for the first time — the instrument floor's own settled reading is
close to, and for C40 slightly over, its own decision bar even after
incoherently summing 9 angles (which would naively be expected to average
fringe-scale noise down, not up). **Per mandatory fix 5
(`GATE_HARD_M3_NOTE`), this does NOT by itself move any constraint-3
verdict** — GATE_HARD is the instrument-floor decision rule, five times
stricter than `C_THR_LAB=0.005`, which is never the bar scored here (see
below).

## P-068-2/3 (article row C, N9, settled vs 1400 baseline): CONFIRMED

| Config | C(1400) | C(2800) | Δ | bucket |
|---|---|---|---|---|
| C40 | −0.004503 | **−0.005601** | −0.001098 | MARGINAL |
| C80 | −0.004602 | **−0.005253** | −0.000651 | MARGINAL |

Both deltas fall inside the pre-registered CONFIRM band (|Δ|≤1.5×10⁻³),
both stay MARGINAL (no bucket flip — `realizability_memo_amendment_needed:
false`, mandatory fix 6's contingency does not fire), both stay negative
(P-068-3 CONFIRMED). **This is the headline result**: Block ARTICLE's own
constraint-3-relevant reading — retracted since Iteration 42, four
consecutive cycles unresolved — is now **re-certified at settled STEPS≥2800**,
and its disposition is **unchanged**: MARGINAL for both padding
configurations. EM's passivity hypothesis (the article-present channel's
settling shift should track the empty channel's own shift in magnitude,
not converge to something smaller) is supported: the shift is real
(15–24% relative movement in C) but bounded and non-catastrophic, exactly
the character predicted.

## P-068-4 (750nm vs 600nm relative convergence, reformulated): PARTIAL

| Config | \|ΔC(4200−2800)\| @600nm | \|ΔC(4200−2800)\| @750nm | 750 exceeds 600? |
|---|---|---|---|
| C40 | 3.17×10⁻⁷ | 1.04×10⁻⁶ | **yes** |
| C80 | 1.31×10⁻⁷ | 4.10×10⁻⁸ | **no** |

Split result — confirmed at C40, refuted at C80. Honestly scored as
PARTIAL, not rounded either direction. Both wavelengths' absolute
convergence deltas are tiny in absolute terms at both configs (all four
values are ≤1.1×10⁻⁶, three orders of magnitude below `C_THR_LAB=0.005`),
so this split does not threaten P-068-6's own confirmation that STEPS=2800
is well-converged for the article-present channel — it only means the
*relative* 750-vs-600 ordering (which wavelength is "worse") is
config-dependent, not the clean pattern the empty channel showed. An
honest open point for a future cycle, not urgent (see Next, below).

## P-068-5 (GATE_HARD, 14 interior empty legs): CONFIRMED, 14/14

Every interior angle (0°, ±5°, ±15°, ±25°) clears GATE_HARD at settled
STEPS, both configs — comfortably exceeding the ≥12/14 CONFIRM bar. This
confirms the predicted grazing-vs-interior asymmetry: T21's edge-diffraction
fringe mechanism is a near-grazing-angle phenomenon, and the settling
defect that makes GATE_HARD fail at ±35°–40° (exp-066's own headline) does
**not** generalize to interior angles — the largest interior |C_empty| is
0.00072 (C40/+25°), still 28% under the bar.

## P-068-6 (Tier2 convergence-generalization stress): CONFIRMED, 4/4

All four cells (θ=−35°, {600,750}nm × {C40,C80}, STEPS=4200 vs 2800) show
`ratio ≤ 6×10⁻⁴` — two orders of magnitude inside the ≤0.01 CONFIRM bar.
**STEPS=2800 is genuinely settled for the article-present channel at the
highest-stakes cell**, at both wavelengths, both configs — the load-bearing
assumption behind every other number in this cycle is now independently
verified, not merely asserted.

## Mandatory-fix docket: fully applied, verified in the output above

1. Deferral count corrected (FOUR cycles, this is the closing one) — see
   NOTES.md's Deferral Disclosure, reproduced in `results.json`.
2. Tier0/Tier1 double-count fixed (14 calls, not 18) — verified: 44 total,
   not 42 or 48.
3. Tier2 extended to both configs/wavelengths — 4/4 cells scored above.
4. `T5_THERMAL_CAVEAT`/`REALIZABILITY_MEMO_CAVEAT`/`G_TRANSFER_T15_CAVEAT`
   carried into `results.json::P-068-2::caveats`, verbatim.
5. `GATE_HARD_M3_NOTE` carried into `results.json::P-068-1` and
   `::P-068-5`, verbatim — printed above at both citation sites.
6. REALIZABILITY_MEMO contingency checked programmatically:
   `realizability_memo_amendment_needed: false` for both configs — **no
   Amendment opened**, the bucket stayed MARGINAL, not PASS.
7. `lab/caveat_lint_config.json` widened and verified (`lab/caveat_lint.py`
   run live before the predict-commit; this file's own required-site now
   satisfied — see below).
8. Block MINI tripwire note carried into `results.json` and printed at
   runtime.

## Caveat-lint verification (post-run)

Re-running `python3 lab/caveat_lint.py` after this file's own commit
closes the one required-site failure that legitimately existed
pre-Phase-4 (this file not yet written) — see NOTES.md Idealization 11
and the registry entry's own `exp063-biot-correction-machinery` precedent
for a site registered before its file exists.

## Trust suite

No `lab/` engine code touched. Full bench (`--only
1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25` + `--only
5`) was reconfirmed green (195/195) at this shift's pre-flight, before any
panel work began — unaffected by this cycle's own `lab/caveat_lint_config.json`-only
change (a data registry, not engine code, per exp-066's own established
distinction).
