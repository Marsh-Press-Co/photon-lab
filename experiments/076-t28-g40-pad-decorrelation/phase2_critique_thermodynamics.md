# THERMODYNAMICS — Phase 2 Critique · Panel Iteration 53 · exp-076 (T28 G40/PAD decorrelation)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md: where absorbed energy goes; owns the per-proposal energy sidecar, analytic and labeled as such). Blind to all other Phase-2 critiques this cycle.*

## Steel-man (≤150 words)

The baseline reuse is R4-clean. I independently re-derived `amp_ratio = √(A_i²+A_q²)/amplitude` from exp-072's own committed `results.json::scored.per_pair` fields and reproduced **0.161063 / 0.040671 / 0.019764 / 0.165873** for C40–C60 / C60–C70 / C70–C80 / C40–C80 — matching the proposal's cited 0.161/0.041/0.020/0.166 to the stated precision, with the pair-labeling convention identical to my own original report of this metric (exp-072's `phase5_review_thermodynamics.md` §5, direction 1). Had this proposal stated an energy-sidecar disposition, it would trivially and correctly resolve N/A: `G40`'s thinner boundary (40 vs 80 cells) changes only where the graded-loss ramp terminates, not its ontological status — it is still a numerical damping construct with no loss tangent standing in for a witness-relevant material, and every scored quantity here is still an empty-scene field ratio with no dissipative volume to integrate over. My own exp-072 argument transfers unchanged.

## Sharpest attack (≤150 words)

The proposal never says so. A full-text search of `phase1_proposal.md` (428 lines) for "sidecar," "thermo," "energy," "absorbed," "re-radiat," or "watt" returns **zero hits** — not even in §5's seven idealizations or §3's T1-route statement. This breaks an unbroken, explicit house convention running through every T28 instrument cycle since exp-071: exp-071 (NOTES.md, "THERMO energy-sidecar metric row does not apply this cycle" + one-sentence reason), exp-072 (Idealization 12, and my own Phase-5 review independently reconfirmed it "by argument, not by omission," citing the Iteration-5/exp-027 house precedent against exactly this failure shape), exp-073 (Idealization 13), exp-074 (Idealization 9), exp-075 (§3 + Idealization 9). Five consecutive cycles stated it in one sentence; this one silently drops it. The underlying determination is correct (see steel-man) — this is a process gap, not a physics defect — but it is precisely the "deferral by omission" pattern this program has caught and fixed before, and it should not survive to Phase 3 freeze uncorrected.

## Verdict

**support-with-changes.**

Mandatory fix: add one idealization sentence stating the energy-sidecar disposition as N/A, with the one-line argument (no article in either `G40`'s or `C80`'s domain; `ABSORB` is a numerical boundary-condition parameter, not a lossy medium with a defined loss tangent; no dissipative volume exists to integrate a Poynting divergence over — identical reasoning to exp-071–075's own stated dispositions). This is a documentation fix, not a design change, and does not touch the FDTD budget, the pre-registered bands, or the R6/`G0-e` disposition.

## Parameter change that would flip the verdict

None. Nothing in the proposal's substance — the geometry table, the reused scoring formula, the pre-registered bands, the R6 ground-truth check — is defective from this seat's charter. The single missing sentence is a one-line fix, not load-bearing enough to warrant oppose, and there is no parameter change (as opposed to a documentation addition) that would move this seat's verdict in either direction.
