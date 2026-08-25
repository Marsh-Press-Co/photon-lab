# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 50 · exp-073

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat 6): human perceptual limits — contrast thresholds, luminance edge detection, spectral sensitivity, adaptation, temporal sensitivity, saccadic/attentional blindness. Blind to the other seats' Phase-5 reviews this cycle. I found the missing "§5 G-gate table" specification gap at Phase 2 (adopted as Red Team's Attack 5) and am named as T2-1's author (docket items 7–8); I hold that machinery to the same standard I'd hold anyone else's. Everything numerical below was independently computed this phase — re-running `run.py` in full, and separately calling its own functions directly on the real 124-point dataset — not taken from prose.*

**Verdict: PARTIAL, leaning PROMISING-as-process.** The Combined Verdict (`HALT_NULL_MISCALIBRATED`) is genuine and I reproduce it bit-for-bit. `G0-e(ii)` did exactly the job R6 was adopted to do: it caught a real, three-independently-implemented statistical defect before any real pair was scored, which is a clean win for the house discipline this cycle exists to exercise. My own seat's contribution, T2-1 (docket items 7–8), is correctly and completely implemented — I verified this directly, not from the Phase-3 prose — but in the course of checking it I found the same leverage mechanism that sank `G0-e(ii)` also lives, uncharacterized, inside `carrier_q95()`, T2-1's own threshold. No perceptual or T1 claim is made anywhere in this cycle; that part of my charter is correctly disengaged.

---

## 0. Verification performed this phase

| Check | Method | Result |
|---|---|---|
| Official Combined Verdict | Re-ran `python3 run.py` in full (149.7s; official commit reports 128.7s — timing noise, not a defect) | **`HALT_NULL_MISCALIBRATED` reproduced bit-for-bit**: `g0e_i.pass_=True`, `g0e_ii.pass_=False`, both legs 72/72 cell-α combinations outside the calibration band. Restored `results.json` via `git checkout` immediately after (`git status` clean, verified). |
| G0-a/b/c identity gates | Read directly from the reproduced run | PASS, PASS, PASS — as published |
| **T2-1 (docket items 7–8)**, on real data, bypassing the HALT | Called `load_data()` + `analyze_pair()` directly (the same frozen code, same `SEED`, same rng-draw order `score_all()` uses) for all four pairs, without going through `score_all`'s gate sequencing | See §1 — full table below, independently reproduces the Phase-3 "gates stubbed" dev-exercise claim exactly |
| Perceptual-claim scan | `grep -niE` for `visib\|percept\|human eye\|naked eye\|see\|seen\|legib\|glance\|apparent\|weber\|michelson\|observer\|contrast` across `NOTES.md`, `phase4_results.md`, `phase3_synthesis.md`, `run.py` | Clean — see §3 |

---

## 1. T2-1 (docket items 7–8) — correctly and completely implemented; independently verified on real data

The mandate credits me with the ancestor of this gate, and the task singled it out because the officially-scored Phase-4 run never reached it (`per_pair` is empty — `G0-e(ii)` HALTs first, per the pre-registered gate order). The only place the gate's behavior on real data is described anywhere in this cycle's record is `phase3_synthesis.md` §4's "gates stubbed" debug exercise, which is explicitly *not* an official result and whose own `dev_results.json` was deliberately deleted. That claim had never been independently checked by anyone before this review. I checked it.

**Finding 1 — the claim is correct, bit-exact.** Calling `analyze_pair()` directly (frozen `run.py`, real 124-point data, `SEED=20490073`, same draw order as `score_all()`) on all four pairs:

| Pair | `q95` | `wrong_stat` (`T_wrong=1.2591°`) | `wrong_admissible` | `T_delta` stat | `T_delta` admissible | `t21_not_evaluable` | `clause_vi_pass` |
|---|---|---|---|---|---|---|---|
| C40–C60 | 0.0760 | 0.4936 | **False** | 0.1235 | **False** | **True** | False |
| C60–C70 | 0.2288 | 0.5020 | **False** | 0.1622 | **True** | False | **True** |
| C70–C80 | 0.2942 | 0.5028 | **False** | 0.2540 | **True** | False | False (sign mismatch) |
| C40–C80 | 0.2395 | 0.4944 | **False** | 0.1410 | **True** | False | False (sign mismatch) |

`T_wrong` excluded at all four pairs; `T_delta` admitted at exactly three of four (excluded only at C40–C60) — **exactly** the pattern `phase3_synthesis.md` reports, now independently confirmed from a fresh implementation of the call, not merely re-read from the Director's own prose. Both parts of my own Phase-2 remedy work as specified: the self-contained per-carrier admissibility statistic is computable with no forward reference (Attack 5's "§5 G-gate table" gap is closed), and the non-emptiness floor fires correctly at C40–C60 (both non-`T_mean` candidates excluded → `NOT_EVALUABLE`, never a vacuous pass) — the exact failure mode my Phase-2 critique and Red Team's Attack 5 warned against is the one case this floor was built to catch, and it does.

**Finding 2 — the admission *pattern* was right, but the proxy Red Team used to justify Ambiguity-1's design choice was not a reliable *magnitude* estimate, and the direction of the miss is not random.** Red Team's Attack 5b (and this cycle's own `carrier_q95()` docstring) used exp-072's phase-randomized-null `q95` as an order-of-magnitude proxy for exp-073's not-yet-computed sign-flip-null `q95` (0.4715/0.2724/0.3853/0.3767 at C40–C60/C60–C70/C70–C80/C40–C80). The real, computed values are 0.076/0.229/0.294/0.240 — smaller at every pair, and **6.2× smaller at C40–C60 specifically**, not merely "similarly-shaped." The qualitative 3-of-4 pattern survived by coincidence of where the real stats happened to fall, not because the proxy was quantitatively sound. This is not a defect in T2-1's implementation — it is a genuine, previously-unstated gap in the audit's own justification for adopting the shared-`q95` reading, worth a line in any future citation of Attack 5b's table as a magnitude estimate rather than a pattern-matching heuristic.

**Finding 3 — `carrier_q95()` inherits the same uncharacterized calibration risk that HALTed `G0-e(ii)`, and nothing in this cycle tests it.** `carrier_q95()` is built from the *identical* `sign_flip_surrogates()` construction that `G0-e(ii)` independently, three-ways, showed is anti-conservative on this exact `n=31, p=5` design (leverage-driven, `mean diag(M5)=0.8387`). `G0-e(ii)` calibrates only the primary gating statistic (`R_q`'s own sign-flip-null rejection rate) — it says nothing about whether the *free-period-recovery* statistic `carrier_q95()` computes off the same surrogate ensemble is itself correctly sized. Finding 2's own result (real `q95` running well under the proxy, most severely at the pair where the leverage effect would bite hardest on a 5-column design with only 26 residual dof) is consistent with — though does not prove — the same mechanism narrowing this statistic's surrogate distribution too. This is not a defect in the current cycle (T2-1 was never scored against real thresholds; the HALT correctly prevented that), but it is a concrete, load-bearing gap for whichever future cycle first reaches a `RESOLVED` clause (vi) test: `carrier_q95()`'s own calibration needs a `G0-e(ii)`-style check before its output is trusted as a real 95th percentile, not merely inherited unexamined because the parent gate happened to pass on a different statistic.

---

## 2. `G0-e(ii)` — reproduced, and the finding is real

I independently re-ran the exact committed pipeline rather than trusting the committed `results.json`. Both legs (i.i.d. Gaussian, real-residual-structure) fail all 144 cell-α combinations, matching `phase4_results.md`'s own table to the percent level (my run: mean rejection rates 0.054/0.114/0.171 at α=0.01/0.05/0.10 on the i.i.d. leg vs. the committed 0.0543/0.1143/0.1709 — the small difference is expected Monte-Carlo noise from a different random seed stream on re-run, not a discrepancy). This is now the **fourth** independent confirmation of the same leverage-driven miscalibration (QUANTUM's Phase-2 critique, Red Team's Phase-2 audit, the officially committed Phase-4 run, and this review's own from-scratch re-execution) — a genuinely over-determined finding, not a fragile one-off. The mechanism (`mean diag(M5) = (n−p)/n = 26/31 = 0.8387`, concentrated on the ramp-coefficient extraction row) is exact algebra, not a modeling assumption, and I have no independent objection to it.

---

## 3. Perceptual-claim scan (charter duty) — clean

Grepped `NOTES.md`, `phase4_results.md`, `phase3_synthesis.md`, and `run.py` for `visib|percept|human eye|naked eye|see|seen|legib|glance|apparent|weber|michelson|observer|contrast`. Every hit is either a pre-registered gate name (`ILL_CONDITIONED`, `HALT`), a document cross-reference, or Idealization 11's correct guard ("`C_empty` is a dimensionless field ratio... not a Michelson/Weber contrast"). **No visibility, detectability, or human-observer claim is made anywhere in this cycle**, and none is at stake in its outcome (a pure gate HALT). My charter's central question — what would make a human eye fail to register something physically present — is not engaged, correctly, and my duty to pin numeric thresholds before a scoring run does not apply this cycle since nothing perceptual is scored. This matches exp-072's own VISION Phase-5 finding for the same reason.

---

## 4. Window-provenance / cross-cycle multiplicity — disclosed accurately, but the newer finding sharpens what it should say next

Idealization 12 (`phase1_proposal.md` §8 and `NOTES.md`, word-for-word consistent) states plainly: the 31-point 36.0°–42.0° grid is inherited from Block MINI (exp-069); statistics on these identical 124 points now span five cycles (exp-069/070/071/072/073); Holm corrects only within this cycle's own three free pairs; nothing corrects across cycles; disclosed, not fixed. This is accurate and I have no correction to it. One precision nit, non-load-bearing: even this HALTed run touches the real per-config series once more — `build_residual_pool()` (`G0-e(ii)`'s residual-structure leg) draws from the real, already-committed exp-069/071 free-period-fit residuals — so "statistics… now span five cycles" is true in substance even though no `p073_2`-style score was produced this time; worth one clarifying word in a future citation, not a fix.

The substantive point is what this cycle *adds* to the case for retiring or widening that window, beyond what was already known. My own seat's exp-072 Phase-5 review ranked, #1, "retire 36°–42° for every T28 carrier-conditioned discriminator" on Rayleigh-resolution grounds alone, and PLAN.md's Iteration-50 queue already carries that as items 2 and 4, correctly sequenced behind this cycle's own re-issue. This cycle supplies a **second, independent** reason pointing at the same fix: `G0-e(ii)`'s leverage mechanism is a direct function of `n=31` relative to `p=5` parameters (`(n−p)/n`). Widening to my own previously-costed 1.5-Rayleigh target (`θ∈[32.47°,46.20°]`, `n=70`/config, 156 calls) would raise `(n−p)/n` from 0.839 to 0.929 — a substantial reduction in the leverage concentration that drove the 2–6× miscalibration, *in addition to* fixing the resolution problem it was originally proposed for. I flag this as a genuine synergy the current queue ordering doesn't yet state explicitly, not as a claim that widening is guaranteed to fix calibration — that must be verified with a fresh `G0-e(ii)`-style check on the wider design, not assumed by extrapolation (see §5, item 1).

---

## 5. Ranked top-3 candidate directions for Iteration 51

### #1 — Run PLAN's queued window pricing, then extension (items 2+4) — now doubly motivated, and price the calibration fix along with the resolution fix

Item 2 (EM's Cramér–Rao pricing, QUANTUM's leakage budget — zero FDTD) should run first, exactly as queued, but its charge should explicitly include the question §4 raises: does widening to `n≈70` bring `mean diag(M5)` far enough from 1 that a fresh `G0-e(ii)`-style calibration sweep on the wider design is likely to pass, or does the leverage mechanism persist at a smaller but still-disqualifying magnitude? If item 4's window extension (my own 156-call, 1.5-Rayleigh target, or EM's cheaper 40-call two-config version) proceeds, it must ship with its own `G0-e(ii)`-style pre-registered calibration test before any `RESOLVED` clause is trusted there — inheriting `G0-e(ii)`'s PASS from this cycle's different-sized design would repeat exactly the unverified-extrapolation mistake R6 exists to prevent.

### #2 — G40/`PAD` decorrelation (item 3), unchanged ranking

Cheap (~31 calls if the geometry-reuse claim verifies), fully orthogonal to the window problem, and closes a confound that has bound every T28 deliverable under every verdict for three-plus cycles running. Its value does not depend on how items 1 or 4 above resolve.

### #3 — Pre-register a corrected null construction for carrier-conditioned ramp coefficients on this design class, before a sixth cycle re-issues the same instrument

Red Team's own docket item 3(c) already commits any future adoption of a corrected null to its own fresh `G0-e(ii)`-style calibration test "never a hand-picked patch adopted after seeing a failure" — this elevates that to its own queued desk task rather than leaving it as a footnote a future re-issue cycle discovers it needs mid-flight. Candidates worth testing against the calibration bands this cycle already built (zero FDTD, reuses the real residual pool): a parametric wild bootstrap under an explicitly-fit residual covariance, and a leverage-studentized permutation swept more finely than this cycle's two single-point probes. If widening the window (item #1) turns out to fix calibration on its own, this item is subsumed, not wasted — the calibration machinery this cycle built is reusable at any window size.

`R_contact`'s literature search remains orthogonal, tooling-blocked, unchanged ranking — not in this cycle's top-3 but still live backlog.

---

## 6. One standing note from this seat, forward-only

Nothing above changes my exp-072 Phase-5 standing offer: name the cycle that intends to make a visibility or detectability claim from this program's T28 machinery, and I will pin the numeric thresholds — with sources — before its Phase 1, per charter. Five cycles into this thread, `C_empty` is still correctly treated as a dimensionless field ratio, not a contrast, and no cycle has yet needed my seat's actual instrument. That remains true this cycle too.
