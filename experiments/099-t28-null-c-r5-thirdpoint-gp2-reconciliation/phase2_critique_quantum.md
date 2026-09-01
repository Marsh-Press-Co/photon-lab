# Panel Iteration 76 — Phase 2 Blind Critique (QUANTUM OPTICS)

*Independent, blind to all other seats' current-cycle critiques. Charter:
non-classical absorption / state-dependent or coherent interactions;
mechanisms enter the bench only as effective classical parameters or Red
Team strikes them. This cycle proposes no new mechanism (T1: N/A, disclosed
and reasoned in §3) — this seat's contribution is independent from-source
re-verification, per this sub-thread's own established practice
(LOGBOOK Iteration 71–75: R17, FI-G″).*

## 1. Steel-man (≤150 words)

Item (1)'s pre-registered trichotomy (SIGN-CHANGE-FOUND /
VANISHING-AMPLITUDE / INCONCLUSIVE-AT-THIS-WIDTH) is genuine, falsifiable
house discipline, not a "wider bracket will find it" hedge, and its numeric
basis reproduces exactly from source. I independently recomputed the four
filed cpl=40 `delta_scene` values for Null C
(`experiments/098-.../results.json::item_i.C.report`) and rebuilt the
interval-slope-decay ratios from scratch: Δ₁=−9.5918×10⁻⁴,
Δ₂=−9.2727×10⁻⁴, Δ₃=−1.1500×10⁻⁴, giving r₂=0.9667, **r₃=0.12402** — an
**8.063×** drop, matching the proposal's cited "r₃=0.1240... ~8.06×" to four
significant figures, not hand-typed. Null C's own cpl20→cpl30 shift figures
(`experiments/092-.../results.json::rank1.crossing_report`) also reproduce
exactly: `shift_vs_cpl20_upper=+0.32016592°`,
`shift_vs_cpl20_upper_second=+0.37675164°`, both positive — the R17
bracket-direction justification is genuinely self-derived, not borrowed.

## 2. Sharpest attack (≤150 words)

Item (2) is this program's first-ever real FDTD spend at cpl=50 (R5) behind
the registration-readback gate — and I traced that gate's own source
(`experiments/097-.../run.py`) and found its **dynamic** checks have **zero
fault-injection coverage at R5's resolution**. `run_checks_1234_and_7`'s
positive-control and FI-A/B/C/D calls (lines 290–308) are hardcoded
`family="R4"`; Check 6's FI-E/F/H are likewise R3/R4-only. The two R5
points in `REPRESENTATIVE` (41.825°/41.850°) only ever run the "clean, no
fault injected" path — confirming CLEAN reads CLEAN, never that a real
defect at cpl=50 reads DEFECT-FOUND. Only Check 5's static `FI-G`
(hand-arithmetic, no `Sim` built) actually exercises R5. This is precisely
R18's "known, named, ignored" shape one level down: the checks are generic
in `cpl`, so a defect is *unlikely*, but R8 already ruled an unverified
robustness argument insufficient when an affordable named check exists —
and re-running FI-A/B/C/D + FI-E/F/H with `family="R5"` costs zero FDTD.
The proposal never discloses this gap.

## 3. Verdict

**support-with-changes.**

## 4. Parameter change that would flip to outright support

Before Rank 2b's 16-call spend (gate it exactly as Rank 2a already gates on
`settle_band`): re-run `run_checks_1234_and_7`'s positive-control +
FI-A/B/C/D, plus Check 6's FI-E/F/H, with `family="R5"` at cpl=50 (zero
marginal FDTD cost — all pre-`sim.run()`) and report CLEAN/DEFECT-FOUND
alongside the existing R4-only figures. With that single addition I move to
outright support.
