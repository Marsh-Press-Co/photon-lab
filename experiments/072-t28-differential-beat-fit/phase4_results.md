# PHASE 4 — TEST · Panel Iteration 49 · exp-072
## Official run: `python3 run.py`, seed 20490072, zero new FDTD calls

**Combined Verdict: `NEITHER`** — matches Red Team's own advance forecast
(`phase2_redteam_audit.md` Sec 7), computed independently by the officially
committed code, not copied from that forecast.

Wall-clock: 48.6 s (desk-only; dominated by 4 pairs × 20,000-surrogate
restricted + unrestricted nulls plus a 2,000-surrogate, 300-point-grid
carrier-consistency calibration per pair — well inside the "<60s" original
estimate despite the docket roughly quadrupling the compute per pair).

## Pre-registration contamination disclosure (binding, restated per Red Team's condition 4)

During Phase 2, QUANTUM OPTICS executed the proposed estimator and both
candidate nulls on the real committed data (withholding outcome numbers)
and VISION SCIENCE executed the estimator and published outcome-determining
numbers (ΔP, z, ρ_c at three carriers). Red Team then independently computed
the observed surrogate p-values under both nulls and found the choice
between them is outcome-determining between Combined Verdict REFUTED and
NEITHER. No threshold was set or moved after any number was computed; every
docket item is justified by an argument independent of the observed data.
Per Red Team's ruling, any CONFIRM-shaped result this cycle is coded to emit
as `CONFIRM_UNCERTIFIED`, never `CONFIRMED` — moot on this data (below), but
the override is unconditional in `run.py` regardless.

## Gates

| Gate | Result |
|---|---|
| G0-a (grid identity, 3-way) | **PASS** — bit-identical |
| G0-b (telescoping identity) | **PASS** — `max\|residual\| = 0.0` exactly |
| G0-c (column provenance) | **PASS** — `max\|Δ\| = 0.0` exactly |
| G0-d (conditioning, per pair) | **PASS**, all four: `cond5 ≈ 59.9–61.0` (≪100) |

## P-072-1 — full per-pair table (published regardless of every other outcome)

| Pair | `T_mean` (°) | amp | carrier R² | `R_q` | `SE(R_q)` OLS / bootstrap | `p` unrestricted (Holm) | `p` restricted (Holm) | `cond5` |
|---|---|---|---|---|---|---|---|---|
| C40–C60 | 2.4865 | 0.005276 | 0.439 | −0.02278 | 0.00562 / 0.02151 | 0.351 (0.702) | 0.0122 (**0.0244**) | 60.0 |
| C60–C70 | 2.5285 | 0.005725 | 0.445 | +0.00085 | 0.00116 / 0.00795 | 0.942 (0.942) | 0.463 (0.463) | 60.8 |
| C70–C80 | 2.5325 | 0.005703 | 0.438 | +0.00593 | 0.00083 / 0.00478 | 0.162 (0.485) | 0.0066 (**0.0199**) | 61.0 |
| C40–C80 | 2.4905 | 0.005245 | 0.431 | −0.01487 | 0.00563 / 0.02707 | 0.702 (unadj., *derived*) | 0.0501 (unadj., *derived*) | 59.9 |

*C40–C80's p-values are reported unadjusted and labeled derived — G0-b
proves it is the exact arithmetic sum of the other three (docket item 14);
it is not an independent fifth test.*

**Bootstrap SE is 3.7–4.8× the naive OLS SE at every pair** — the
uncertainty item 7 required be propagated genuinely dominates the naive
figure. No pair's `|R_q|/SE_bootstrap` clears 2 (0.94 / 0.09 / 0.99 / 0.42
respectively for C40-C60/C60-C70/C70-C80/C40-C80) — consistent with, and
explaining, why the restricted-null significance test (which calibrates its
own null empirically rather than assuming the OLS SE) is the one actually
gating `RESOLVED` below.

**Phase/frequency/strain decomposition (P-072-6):**

| Pair | phase channel `\|A_q\|/a` | freq channel `\|R_q\|σ_u/a` | strain channel `\|R_i\|σ_u/a` | strain flag |
|---|---|---|---|---|
| C40–C60 | 0.081 | 0.105 | 0.093 | False |
| C60–C70 | 0.037 | 0.004 | 0.044 | **True** |
| C70–C80 | 0.004 | 0.025 | 0.015 | False |
| C40–C80 | 0.130 | 0.069 | 0.166 | **True** |

`R_i` (nominally ≈0 under the single-carrier model) exceeds the frequency
channel at C60–C70 and C40–C80 — disclosed per docket item 11, a real
model-strain signature the original Phase-1 proposal's table did not carry
a place for.

**Curvature column (item 15, disclosed, non-gating):** 6-column condition
numbers 3184–3326 (vs. 5-column's ~60) — the curvature column is much more
poorly conditioned by construction, as expected for a quadratic term over
this narrow a window; its coefficients (−1.058 / −0.177 / +0.025 / −1.231)
are non-negligible at three of four pairs and are recorded, not
interpreted further this cycle (MATERIALS' own framing: this is
zero-cost partial information on the standing PAD confound's curvature,
not a load-bearing result on its own).

**ΔP at all four carriers (item 12, mandatory disclosure — VISION's
finding, reproduced by the officially committed code):**

| Pair | `T_mean` | `T_delta` (pair's own) | `T_wrong` = 3.60° (displaced) | `T_wrong` = 1.9608° (T21 fringe, disclosure only) |
|---|---|---|---|---|
| C40–C60 | **+0.0576°** | −0.0007° | −0.1080° | +0.0539° |
| C60–C70 | −0.0020° | +0.0120° | −0.0443° | +0.0107° |
| C70–C80 | −0.0144° | +0.0046° | −0.0005° | +0.0022° |
| C40–C80 | **+0.0380°** | −0.0153° | −0.1615° | +0.0671° |

VISION's finding reproduces under the fixed, officially-committed pipeline:
**sign is not invariant across carriers admitted by the design.** C40–C60
and C40–C80 flip sign between `T_mean` and `T_delta`; C60–C70 and C70–C80
flip sign between `T_mean` and every other carrier tested. This is not
treated as a gate (per Red Team's override of VISION's original proposal —
`phase3_synthesis.md`), but it is the honest headline of what this
instrument's reach looks like in this window, and it is reported in full
rather than only at the one carrier the Combined Verdict happens to gate on.

## P-072-2 — does the differential instrument resolve structure?

`RESOLVED` requires: `cond5 ≤ 100` **and** restricted-null Holm-adjusted
`p ≤ 0.01` **and** the linearization gate **and** the recalibrated
carrier-consistency gate **and** the displaced-wrong-carrier gate.

| Pair | cond OK | `p` restr. Holm ≤ 0.01 | linearization | carrier (obs vs. `q95`) | wrong-carrier (3.60°) | **RESOLVED** |
|---|---|---|---|---|---|---|
| C40–C60 | ✓ | 0.0244 — **fails** | ✓ | 0.1235 ≤ 0.4473 ✓ | `p=0.0195` — **fails** | **No** |
| C60–C70 | ✓ | 0.4634 — fails | ✓ | 0.1622 ≤ 0.2804 ✓ | `p=0.0071` — fails | **No** |
| C70–C80 | ✓ | 0.0199 — **fails** | ✓ | 0.2540 ≤ 0.4013 ✓ | ✓ (only pair to pass) | **No** |
| C40–C80 | ✓ | 0.0501 — fails | ✓ | 0.1410 ≤ 0.3525 ✓ | `p=0.0125` — fails | **No** |

**Zero pairs `RESOLVED`.** No pair clears the `p ≤ 0.01` bar even before the
wrong-carrier gate is applied; C70–C80 is the only pair that would have
passed the wrong-carrier check, and it fails on significance instead.

Not CONFIRM (requires C40–C80 and C40–C60 `RESOLVED` plus at least one of
{C60–C70, C70–C80} — none resolved). Not the REFUTE branch either:
`n_resolved_holm10_restricted = 3` (C40–C60, C70–C80, C40–C80 all clear the
*relaxed* `p ≤ 0.10` bar under the restricted null) — REFUTE requires
**zero** pairs at `p ≤ 0.10` under *both* nulls, and three pairs clear it
under the restricted one. **P-072-2 = `NEITHER`.**

## Injection-recovery power test (item 4)

| Pair | `R_q` predicted (from committed `m₀`) | `R_q` recovered | `p` recovered | Passes `p ≤ 0.01`? |
|---|---|---|---|---|
| C40–C60 | −0.02021 | −0.04299 | 0.0039 | ✓ |
| C60–C70 | −0.01060 | −0.00975 | 0.0082 | ✓ |
| C70–C80 | −0.01053 | −0.00460 | **0.0146** | **✗** |

**`power_demonstrated = False`** — C70–C80's injection test misses the
`p ≤ 0.01` bar by a small margin (0.0146 vs 0.01). Per docket item 3, this
means the REFUTE branch was never reachable regardless of the null count
above; had it been reachable, the design's own honest branch would have
been `UNDERPOWERED_NOT_EVALUABLE`, not REFUTE — the power precondition did
its job of preventing exactly the "REFUTE fires on pure power failure"
defect Red Team's Attack 2 identified, even though in this instance the
null-count condition (three pairs clear 0.10) meant the branch was moot.

## P-072-3 — relabeled basis-stability check (item 8, disclosed, non-gating)

Requires all three adjacent pairs `RESOLVED`; none are. **`NOT_EVALUABLE`.**
(No basis-stability statistic is computed — correctly, since the check is
only meaningful once independent adjacent estimates exist to sum.)

## P-072-4 — consistency with Iteration 48's `ABSORB`-depth trend, or new structure?

Evaluated over `RESOLVED` pairs only; none resolved. **`NEITHER`** (fewer
than 2 resolved pairs — the design's own pre-registered fallback for
insufficient data, not a sign-reversal finding).

**Disclosed only (docket item 9, non-gating), for completeness:** the
committed linear `m₀ = 0.0025564°/cell` and an engine-derived saturating
model (decay fixed at `_damping`'s own 0.075/cell) were both fit to the
four per-config free periods **recomputed at this cycle's own `n_grid=3000`**
(2.43748° / 2.52051° / 2.53551° / 2.53051° for C40/C60/C70/C80 — note C70 >
C80 at this resolution, the order-reversal VISION's Phase-2 critique found
and Idealization 6 discloses):

| Model | Params | R² |
|---|---|---|
| Linear in `ABSORB` | 2 (intercept, slope) | 0.8328 |
| Saturating, `L=0.075/cell` fixed | 2 (`P_∞`, amplitude) | **0.9901** |

The saturating model still fits materially better at the refined
resolution — MATERIALS' and THERMODYNAMICS' finding survives the tie-break
VISION's critique forced, though this remains disclosed context, not a
gating result, and the confounded `ABSORB`/`PAD` axis (Idealization 2)
means neither model licenses a mechanism claim on its own.

## Combined Verdict — branch trace

1. G0 gates: **PASS** (all four).
2. P-072-2 = `NEITHER`, P-072-4 = `NEITHER` → neither REFUTE condition
   (`P-072-2 REFUTE` nor `P-072-4 REFUTE`) fires.
3. CONFIRM requires P-072-2 CONFIRM AND P-072-4 CONFIRM — neither holds.
4. → **`NEITHER`.**

The contamination-ruling override (`CONFIRM_UNCERTIFIED`) never engages —
verified inert on this data, exactly as Red Team predicted in advance.

## Bottom line

The fixed, officially pre-registered design resolves **zero of four**
`ABSORB` pairs in this window, including the founding C40–C80 pair where
T28 was first discovered at `ptp/mean=16.2` (that statistic measures
something different from what P-072-2 gates on — see caveats below). The
substantive finding is not "nothing happened" — it is **why** nothing
resolved, measured rather than merely argued: `R_q`'s sign and magnitude
are not stable across carriers the design's own gates admit as consistent
(the ΔP table above), the bootstrap-propagated uncertainty is 4–5× the
naive OLS estimate at every pair, and the one pair whose displaced-carrier
control passes (C70–C80) is exactly the pair whose significance and
injection-recovery power both fail. The differential/beat-fit instrument
is real and better-conditioned than the absolute-period route it replaces
(the carrier itself resolves cleanly, R²≈0.43–0.45, at every pair, matching
Iteration 48's own per-config fits) — but its reach in this specific
36°–42° window is bounded by non-identifiability against the window's own
second, unresolved contributor (T21's 1.9608° fringe, sitting only 0.65
Rayleigh widths from the carrier) and by the carrier's own residual
uncertainty, not by the noise floor the Phase-1 proposal's a-priori power
table anticipated. That is a genuine, load-bearing advance on Iteration
48's NEITHER: it identifies the specific mechanism of the resolution
failure rather than only its raw thresholds.

## Caveats (binding, per Idealizations above and Red Team's docket item 13)

- **600nm only** — no wavelength-general claim.
- **`ABSORB`/`PAD` compound-axis confound not relieved.** Any future
  CONFIRM-shaped language on this series must read `ABSORB`-or-`PAD`-or-
  frequency-or-fringe-weight-tied, never cleanly `ABSORB`-tied. This binds
  every table above, under every verdict, not only a hypothetical CONFIRM.
- **`ABSORB` is not a material** — no realizability claim licensed.
- **Window provenance**: inherited from Block MINI; T28 was discovered
  inside it; no cross-cycle multiplicity correction applied across the
  roughly dozen statistics now computed on these same 31 points.
- **`ptp/mean`-style figures are fit-conditioning statistics, not
  perceptual or photometric contrasts.**
- Energy sidecar: N/A this cycle, no absorbed-power number produced.
- Pre-registration contamination: see disclosure above — this cycle's
  p-values should be read as design-verification numbers computed under a
  fully-specified, Red-Team-audited design, not as a first, blind look.
