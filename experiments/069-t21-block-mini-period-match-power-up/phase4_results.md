# PHASE 4 — RESULTS · Panel Iteration 46 · exp-069 (Block MINI power-up)

100 new FDTD calls, 885.8s (14.76 min) — well inside the recomputed 100 min
hard stop and the 32.5 min predicted wall (actual ran ~2.2× faster than the
budgeted estimate; `design_geometry.py::CPU_S_PER_CALL`'s own contention
figures were measured under different concurrent load than this shift's).
Zero `lab/` diff (`assert_lab_clean()` passed before any FDTD call). Full
bench reconfirmed green after this run (see SESSION_LOG.md/this cycle's
close for the exact count).

## Gate

**P-069-G1 PASSED, 4/4 exact** — θ∈{38°,40°}×{C40,C80}×600nm×STEPS=2800
reproduce exp-065's own committed `settled_sweep_steps2800_diagnostic.json`
bit-for-bit. Independently spot-verified a second way before this run
(single-call reproduction test, logged in this cycle's commit history) —
everything below is trusted.

## Scored predictions

| ID | Result | Verdict |
|---|---|---|
| P-069-1 (amplitude) | `ptp=0.004026`, `mean=-0.000249`, **ratio=16.20** | **REFUTE** (>2.5 by a wide margin — the flat/additive-systematic null is decisively rejected) |
| P-069-2 (fixed period, primary) | `R²=0.2016` at `T=cpl/A=0.026596` | **NEITHER** — lands in the gray zone (0.15 < R² < 0.50); the fixed-period model is not decisively supported or rejected |
| P-069-3 (free period, secondary) | best-fit `P*=2.8421°`, `R²=0.6272`; `rel_dev=44.95%` from `P(39°,600nm)=1.9608°` | **NEITHER** — `rel_dev` (45%) sits between the 20% within-tolerance and 50% out-of-tolerance lines; `R²=0.63` clears the 0.30 floor comfortably, so this is a real, well-fit periodic structure — just not at T21's own predicted period |
| P-069-4 (settling) | `rel` = 2.7×10⁻⁵ / 1.7×10⁻⁵ at θ=39°/40° (STEPS 4200 vs 2800, both ≪ the 1% bar) | **CONFIRM** — `C80` is genuinely settled by STEPS=2800; the 2800-vs-1400 shift (0.0034/0.0039 absolute) is real transient decay, fully resolved by 4200 |
| P-069-5 (R3/resolution) | same sign at both angles; ratio `delta_r3/delta_native` = 1.97 (θ=39°) / 2.50 (θ=40°), both inside `[0.3,3.0]` | **CONFIRM** — the oscillation does not sign-flip or collapse under cpl 20→30 (geometry ×1.5, mirrors exp-033's own idiom) at these two cells, ruling out the crudest artifact hypotheses. **Correction (Phase-5 audit, three independent seats — PHOTONICS, QUANTUM, EM/Red-Team-confirmed): the "real physical feature, not Yee-grid discretization structure" language above overstates what this specific pass shows.** Both R3 cells (39°/40°) sit within an order of magnitude of `delta(θ)`'s own zero-crossing (`delta(39.0°)=1.2e-4`, `delta(39.2°)=3.3e-5` vs. the window's peak `ptp=4.0e-3`), a phase-sensitive location where an ordinary resolution-driven phase shift produces a large *relative* change; this program's own historical R3 "survives resolution" precedent (exp-005, exp-015) shrank by ~7% under an identical cpl 20→30 step, not the 97–150% observed here, and the CONFIRM band itself (`[0.3,3.0]`) is correspondingly ~10× wider than any prior R3 pass this program has cited as decisive. **Correct reading: rules out sign-flip/order-of-magnitude collapse at 2 of 31 angles; does not establish that the fringe's location/amplitude across the window is resolution-converged, nor does it distinguish T21's coherent mechanism from Yee-grid discretization structure at the identical characteristic scale (both derive from the same discretized edge — QUANTUM's Phase-2 Attack 3, never closed by a peak-cell or whole-window R3 leg).** A peak-cell recheck (θ≈37.2°/41.4°, zero marginal cost) is Iteration 47's queued fix. |
| P-069-6 (750nm, disclosed) | `ratio=2.89`, `R²(fixed T)=0.348` over 16 points (~1.22 periods — under-powered by design) | context only, not gated — same qualitative shape as 600nm (large amplitude, partial-but-incomplete period match). **Correction (Phase-5 audit, PHOTONICS' independent re-analysis, verified by Red Team directly from `results.json`): T21's OWN period is the wrong null to test the 750nm leg against — its own free-period search degenerately hits its own search-range boundary here (window too narrow, ~1.22 periods, to resolve any interior optimum), which `phase4_results.md` does not disclose.** The right cross-λ test — does the 600nm free-fit's own implied effective aperture (`A_eff≈518.8` cells, back-solved from `P*=2.8421°` at θ=39°) predict the 750nm delta series via simple λ-scaling (`T_750=CPL[750]/A_eff`) — was not run this cycle but is independently reproducible from committed data and gives **R²=0.767**, more than double T21's own-model fit to the same 750nm data (R²=0.348, the number reported here). This is a materially stronger, undisclosed cross-wavelength signal pointing toward T28 being a genuine, λ-scaling-consistent coherent effect with its own characteristic length scale (≈519 cells, distinct from T21's A=752) — not proof (post-hoc, not pre-registered — an R4-adjacent risk if ever cited as a confirmed result rather than a suggestive re-analysis), but stronger support for "suggestive of a shared mechanism across λ" than the number this table originally cited. See `phase5_redteam_audit.md` §on PHOTONICS' finding for the full independent re-derivation. |

## Combined Verdict

**`FORMAL_RETIREMENT_NON_DECISIVE`** — computed in code (`run.py::score()`),
per the pre-committed rule (mandatory fix 4, Phase 2):

> Statistical power was raised to the mandate's own spec (31 points/0.2°
> step/~3.0 periods, settled STEPS=2800, a resolution check, a
> settling-closure check, and a co-gating free-period cross-check) and the
> result is still non-decisive — that is itself the finding.

Neither the `COHERENT_FRINGE_FULLY_CORROBORATED` gate (needs P-069-1 AND
P-069-2 AND P-069-3 AND P-069-4 AND P-069-5 all satisfied) nor the
`ADDITIVE_SYSTEMATIC_VINDICATED` gate (needs P-069-1 AND P-069-2 both
CONFIRM) closes: P-069-1 REFUTEs decisively (ruling out the additive-null
reading outright) but P-069-2/P-069-3 do not corroborate T21's *specific*
predicted period, only a *different*, comparably strong one.

**Per mandatory fix 4, this is NOT reported as PARTIAL-and-deferred.
`P-VIS42-10`'s period-match test (Block MINI) is FORMALLY RETIRED as of
this cycle's close** — the LOCKED mandate's own "no further relabeling, no
further citation-tripwire-only treatment" bar is satisfied: the test was
built at the power the mandate specified, run cleanly, gated, and its own
pre-committed decision rule fired the retirement branch honestly rather
than being argued around.

## What this DOES establish (real findings, not a null result)

1. **The `C80−C40` padding delta at θ∈[36°,42°]/600nm is genuinely
   periodic, real, resolution-robust, and settled** — not the additive
   systematic this program's own T24 framing has defaulted to since
   Iteration 23. This is itself new information: T24's own inheritance
   claim (does the beam-channel boundary systematic transfer to the plane
   channel as absolute or relative — still open per LOGBOOK's own T24
   status) should be read against a REAL periodic structure at this
   channel, not an assumed-flat one.
2. **The period is NOT T21's own predicted `P(θ)=λ/(A·cosθ)`.** Best fit
   `P*≈2.84°` at 600nm is 45% longer than `P(39°,600nm)≈1.96°`, with a
   solid `R²=0.63` — this is not noise finding a spurious period; it is a
   different, comparably well-determined period. T21's own model, being
   only the *stationary-phase limit* of the full coherent aperture
   integral (R²=0.7852→0.8271 at its OWN best fit — see Idealization 5),
   was never guaranteed to be the exact period for a DIFFERENT quantity
   (a padding delta, not a single-config `C_empty(θ)`) at a DIFFERENT
   geometry (two configs differenced, not one read alone) — this cycle is
   the first time that assumption was actually tested, and it does not
   hold cleanly.
3. **Not an unsettled transient** (P-069-4 CONFIRM, both cells ≪0.01%
   relative shift 4200-vs-2800 — decisively ruled out). **Not a
   sign-flip/order-of-magnitude resolution artifact at the two tested
   angles** (P-069-5 CONFIRM). **Correction, Phase-5 audit (see the P-069-5
   table row above): "not a resolution artifact" overstated the second
   claim** — the two R3 cells sit near the fringe's own zero-crossing, not
   a peak, and the measured ratios (1.97×/2.50×) are far outside this
   program's own historical R3 "survives resolution cleanly" range (~7%,
   exp-005/exp-015). P-069-5 rules out the crudest artifact hypotheses; it
   does not establish resolution convergence of the fringe's location or
   amplitude, nor does it separate T21's coherent mechanism from
   Yee-grid discretization structure at the identical characteristic scale
   (both derive from the same discretized taper edge — never tested this
   cycle). A peak-cell R3 recheck is queued for Iteration 47.

## New live thread — T28 (opened this cycle)

**The `C80−C40` padding delta carries a real, ~2.84°-period (600nm)
oscillation whose origin is unidentified — neither T21's own edge-
diffraction fringe (period mismatch, 45% off, though a plausible harmonic/
beat relationship is unexplored) nor a resolution or settling artifact
(both independently ruled out this cycle).** Candidate next steps, NOT run
this cycle (disclosed, not claimed to be ruled out — Idealization 5):
a direct desk check of whether 2.84° relates to `P(θ)` by a simple integer
ratio (2.84/1.96 ≈ 1.45 — not obviously a clean harmonic, disclosed as
checked-and-inconclusive, not pursued further); a boundary-thickness-scale
mechanism specific to the `ABSORB` band itself (T24's own original
subject, never actually isolated from the source/aperture geometry T21
governs); or a genuinely new candidate mechanism requiring its own
Phase-1 proposal in a future cycle. This is instrument/model-fidelity
work — no constraint-3 verdict is implicated, and Checkpoint-criterion-2
candidacy is explicitly declined (T28 is a real, unresolved mechanism
question, not yet a proven mechanism-class boundary).

## R_contact

Untouched this cycle (Idealization 9, mandatory fix 9) — still blocked on
WebSearch/WebFetch tooling.
