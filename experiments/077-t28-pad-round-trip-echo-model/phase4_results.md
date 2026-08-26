# PHASE 4 — TEST · Panel Iteration 54 · exp-077

Corrected `pad_round_trip_model.py` (all 5 mandatory fixes from
`phase2_redteam_audit.md` implemented) re-run end-to-end from repo root.
**Zero new FDTD calls, zero `lab/` diff** — matching the cycle's original
scope. Full stdout: `pad_round_trip_output.txt`; full numeric record:
`pad_round_trip_results.json`.

## Frozen-prediction check (all CONFIRMED, no deviation beyond rounding)

| Prediction (`phase3_synthesis.md` §3) | Observed | Status |
|---|---|---|
| `PAIR_PAD` two-wall `P*_model ≈ 8.6677°` | `8.6677°` | **CONFIRMED, exact** |
| `PAIR_PAD` two-wall Test A `rel_dev ≈ 0.8797` → INCONCLUSIVE | `0.8797` → INCONCLUSIVE | **CONFIRMED, exact** |
| `PAIR_PAD` two-wall Test B `r² ≈ 0.0001` → REFUTE | `0.0001` (r=+0.0097) → REFUTE | **CONFIRMED, exact** |
| `PAIR_PAD` two-wall Combined: REFUTE (via Test B) | REFUTE (via Test B) | **CONFIRMED** |
| `PAIR_ABSORB40` two-wall `P*_model ≈ 7.0372°` | `7.0372°` | **CONFIRMED, exact** |
| `PAIR_ABSORB40` two-wall Test A `rel_dev ≈ 0.6851` → INCONCLUSIVE | `0.6851` → INCONCLUSIVE | **CONFIRMED, exact** |
| `PAIR_ABSORB40` two-wall Test B `r² ≈ 0.0418` → REFUTE | `0.0418` (r=+0.2043) → REFUTE | **CONFIRMED, exact** |
| `PAIR_ABSORB40` two-wall Combined: REFUTE (flipped) | REFUTE (flipped from single-wall's INCONCLUSIVE) | **CONFIRMED** |
| Gates pass identically to single-wall run | G-LOSSLESS `2.220e-16`, G-N1 `1.404e-15`, G-PASSIVITY worst `|r|=0.006423` — bit-identical | **CONFIRMED** |
| Null-calibration appendix strengthens, not threatens, REFUTE | `P(R²≥0.70)=0.00000` over 20,000 pure-noise trials (max `0.5609`); real `R²=0.8165` far outside; bootstrap recovery: `100.0%` of 20,000 resamples land within 20% of the true fitted period | **CONFIRMED** |

**A fourth independent computation (this Phase-4 run itself) now agrees
with the three Phase-2 from-scratch implementations (PHOTONICS,
ELECTROMAGNETISM, Red Team) to four decimal places.** No disagreement
arose — per `phase3_synthesis.md` §3's own stated stakes, this means the
frozen numbers, not a fresh finding, are this cycle's headline.

## New code-level confirmations (fixes 3, 4)

- **Fix 3** (`verify_symmetric_damping`): the `+x` wall's `damp_e` column
  is bit-identical (worst diff `0.000e+00`) to the `-x` wall's — confirms
  MATERIALS' claim in code, not citation: both walls are the same
  unrealizable matched-`eps=mu` admittance class.
- **Fix 4** (`thermo_sidecar_check`): `ABSORB=40` absorbed fraction
  `99.9959%–99.9992%`; `ABSORB=80` `100.0000%` (rounds up at 4 decimal
  places — `|r|≈0.0001`); `PAIR_ABSORB40`'s real, non-common-mode
  `Δ(absorbed fraction) = 8.4098×10⁻⁶`–`4.1247×10⁻⁵` — matches Red Team's
  Attack-4 recomputation exactly, confirming THERMODYNAMICS' own cited
  range contained the arithmetic slip Red Team found, not this code.

## Combined verdict, corrected (supersedes the single-wall-only headline)

**`PAIR_PAD` (T28's dominant signal, this cycle's primary target):
Combined REFUTE, robust across single- and two-wall cuts — but via
DIFFERENT tests.** Single-wall: period test REFUTEs (`rel_dev=1.88`),
shape test REFUTEs (`r²=0.044`, already weak). Two-wall: period test
actually IMPROVES to INCONCLUSIVE (`rel_dev=0.88`) — adding the far-wall
echo brings the model's period closer to the real data's — but the shape
test gets four orders of magnitude WORSE (`r²=0.0001`) and alone carries
the REFUTE. **This is not "REFUTE, same failure shape" (the single-wall
proposal's original language, now corrected) — it is REFUTE on both
cuts, for materially different reasons, which is a STRONGER result than
one REFUTE repeated twice: two structurally different ways of scoring
this mechanism class both kill it, on different grounds.**

**`PAIR_ABSORB40` (the geometry-fixed control): Combined REFUTE — NOT
robust across cuts.** Single-wall scored INCONCLUSIVE; adding the
far-wall term flips it to REFUTE (shape `r²` drops `0.1997→0.0418`). This
means the single-wall proposal's secondary reading was an artifact of
its own incompleteness, not a real, milder signal — the complete
(two-wall) instrument says this pair is a REFUTE too.

**Bottom line for T28: with the far-wall term correctly included, BOTH
pairs this cycle set out to explain now REFUTE.** The single coherent
echo mechanism class — the only one exp-076's own lossless-vacuum proof
left physically permitted for a `PAD`-tied signal — is REFUTEd,
completely, not partially, once tested on its own most complete
(two-wall) instantiation. This is a cleaner, harder negative result than
the single-wall proposal alone would have supported.

## Gates and sanity re-verified

- G-LOSSLESS, G-N1, G-PASSIVITY: all PASS, bit-identical to the Phase-1
  single-wall run (the gates test the transfer-matrix code, not which
  wall(s) the propagator sums — expected and confirmed).
- Geometry congruence assertions: re-verified.
- `boundary_free_spread_internal_check = 0.000e+00`: the boundary-free
  (no-wall) term is exactly config-independent, as exp-065 established.

## No Checkpoint criterion fires

Matching `phase3_synthesis.md` §4's own stated condition: Phase 4
reproduced every frozen number exactly, and the corrected write-up (see
`phase1_proposal.md`'s revision, this commit) no longer states "same
failure shape" — the specific condition that would have fired Criterion 4
did not occur.
