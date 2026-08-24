# Phase 2 Critique — MATERIALS & METAMATERIALS (blind, fresh context)

**Files checked directly**: `experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md` (lines 10–32, "AMENDMENT (Iteration 12, exp-035...)"), `experiments/065-t24-absorb-boundary-sweep/design_geometry.py` (R_OUT=78 line 124, TAU_OFF_PASS=0.0065 line 159, SIGMA_OFF_PASS line 160, GATE_HARD=0.001 line 205, C_THR_LAB line 210), `lab/glare_sidecar.py::c_thr`, `exp-065/phase4_results.md` §"Phase-5 corrections" item 2, `exp-066/phase4_results.md` closure table + F4 narrowing, LOGBOOK.md T27 thread, PLAN.md Iteration-45 queue.

## 1. Steel-man

τ=0.0065 is `REALIZABILITY_MEMO.md`'s single empirical anchor for D_req (τ_on/τ_off≈600×) — the only reason Amendment 1's "true D_req is a lower bound, larger not smaller" argument has any empirical foothold at all. T27 has now shown the exact same channel and exact same ±35° cells feeding this article's own N9 aggregate are unsettled at STEPS=1400, with sign-flipping empty-floor residuals. A MATERIALS-charter memo built on a number this program itself knows was measured unconverged is indefensible to leave uncorrected. The proposal reuses exp-065/066's already-gated harness verbatim, caps calls hard, and correctly keeps the STEPS=1400 MARGINAL reading labeled RETRACTED rather than quietly re-citing it.

## 2. Sharpest attack

§5 claims "this cycle probes instrument uncertainty only" and "REALIZABILITY_MEMO Amendment stands" — but this is not guaranteed by the proposal's own design, and the proposal doesn't act like it believes it. P-068-2's own REFUTE band explicitly allows a flip to PASS (ΔC≥+0.0020, C past −0.0025), and `exp-065/phase4_results.md`'s Phase-5 correction 2 already showed the exact −35° cells feeding this article's N9 aggregate sign-flip by 0.0055–0.0065 in the *empty* channel alone under this identical STEPS correction — a PASS on the article row is a live outcome, not a remote one. If C40/600nm clears |C|<0.0025, `REALIZABILITY_MEMO.md`'s "0.0065 no longer clears the bar at EITHER geometry... which makes the true D_req larger, not smaller" is directly contradicted, not merely "probed." (The overall UNOBTANIUM-WITH-PARAMETERS *tier* itself would likely survive per exp-066's own F4 finding that the tier rests on RSA/TPA gaps independent of this channel — so this is not a tier-flip risk, but it is a real, numbered-anchor risk the proposal never names.) The proposal pre-commits an FDTD flip rule but no memo-amendment action for that outcome.

## 3. Verdict: support-with-changes

## 4. Parameter change that would flip my verdict to plain support

Add one line committing that if P-068-2 (or the 750nm-new leg) flips article-row C past MARGINAL_LO (|C|<0.0025) at either config, the same-shift close must open a `REALIZABILITY_MEMO.md` Amendment revising the D_req-as-lower-bound language — not just relabel `results.json`/caveat_lint. Without that pre-commitment, a genuinely realizability-relevant number could land this cycle and get absorbed as "instrument uncertainty" in exactly the pattern R4 exists to police.
