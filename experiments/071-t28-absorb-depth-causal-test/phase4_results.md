# PHASE 4 — RESULTS · Panel Iteration 48 · exp-071

78 FDTD calls, 925.7s (15.43 min) — well under the 30.64-min predicted
wall-clock and the 100-min hard stop. Zero `lab/` diff (`assert_lab_clean()`
passed at the start of the run; reconfirmed via `git diff --stat -- lab/`
after). Full raw output: `results.json`.

## Gate

**P-071-G1 PASSED, 4/4 exact** — θ∈{39°,40°}×{C40,C80}×600nm×STEPS=2800
reproduce exp-069's committed `block_dense` rows bit-exactly. The reused
exp-069 data is certified trustworthy.

## Binding preconditions — both CONFIRM

- **Block SETTLE-C60C70: CONFIRM.** The 2800-vs-4200 STEPS shift at both
  peak angles, both new configs, is **2–4 orders of magnitude below**
  `GATE_HARD` (relative-to-floor ratios `2.5×10⁻⁴` / `4.3×10⁻⁵` / `1.5×10⁻⁴`
  / `4.0×10⁻⁵` — all far under the 1.0 CONFIRM threshold, nowhere near the
  5.0 REFUTE threshold). EM's Phase-2 concern (an unsettled C60/C70
  transient masquerading as an ABSORB-tracking trend) is **directly
  addressed and closed**: C60/C70 are settled at STEPS=2800 by a wide
  margin, at least as cleanly as C40/C80 were previously.
- **P-071-4 (peak-cell R3, C80−C40): CONFIRM.** Same sign at both peak
  angles, ratios 1.234/1.047 — both cleanly inside `[0.3, 3.0]`. Closes
  exp-069's own residual resolution-scope gap definitively at the actual
  extrema, not the original near-zero-crossing cells.

Both mandatory fixes (EM's, QUANTUM's-via-Red-Team's) were load-bearing
checks the design genuinely needed — and both came back clean. The
underlying `C80−C40` signal at the peak angles is real: settled and
resolution-robust.

## P-071-1 — per-config free periods

| Config | ABSORB | P* (deg) | R² |
|---|---|---|---|
| C40 | 40 | 2.4361 | 0.433 |
| C60 | 60 | 2.5188 | 0.448 |
| C70 | 70 | 2.5338 | 0.442 |
| C80 | 80 | 2.5338 | 0.434 |

**C70 and C80 recover the IDENTICAL free-fit period (2.5338°, to all
printed digits).** The free-period grid has `n_grid=400` over `[1°,4°]`,
i.e. a step of 0.0075° — an exact match at this resolution across two
different configs is worth flagging honestly as **plausibly a grid-search
discretization tie, not evidence the two configs share an exactly
identical underlying period** — consistent with, not contradicted by, the
resolution-floor finding below (the search cannot resolve differences at
this scale in the first place, so a tie is unsurprising either way).

## P-071-2 (HEADLINE) — causal trend test

**Linear fit `P*(ABSORB) = 0.0025564·ABSORB + 2.3459`, R² = 0.8664.** The
period rises smoothly and monotonically with `ABSORB` depth across all
four points — a real, well-determined *shape* to the trend. But:

- **`spread_40_80 = 3.90%`** — far below the 30% CONFIRM threshold.
- **`max_pair_spread = 3.93%`** — well below the 15% REFUTE threshold, but
  **R² = 0.8664 sits far above REFUTE's own R² ≤ 0.30 ceiling** — the
  trend is too well-fit-looking (in the narrow curve-fit sense) to count
  as "flat" under the pre-committed REFUTE definition, even though its
  absolute magnitude is tiny.
- **Raw verdict: neither CONFIRM nor REFUTE clears** — genuinely between
  the two pre-committed bands, exactly the disposition the pre-committed
  rule exists to catch rather than paper over.

**Resolution-floor gate (mandatory fix 2) — decisive.**
`trend_resolution_ratio(P*(40), P*(80)) = 0.095`: the 31-point/36–42°
window supplies under **10%** of the frequency resolution needed to
distinguish these two periods. **`trend_resolved = False`.** Every one of
the five non-trivial pairwise comparisons (all except the exact C70–C80
tie) is independently `UNRESOLVED` (`all_pairs_resolved = False`) — see
the full table below. **This is exactly the failure mode Red Team's own
extension of QUANTUM's finding predicted**: a small monotonic trend
across four points, fit with a deceptively high R², sitting entirely
inside the window's own frequency-resolution floor. The mandatory
resolution-floor gate did its job — it prevented this cycle from reporting
either a false CONFIRM (a "genuine ABSORB-tied mechanism" the window
cannot actually establish) or a false REFUTE (a "flat, shared-geometry"
verdict the window cannot rule out either, since it can't resolve periods
this close in the first place).

## P-071-3 — full pairwise table (all 6 pairs, required disclosure)

| Pair | P*_a | P*_b | Spread | Resolution ratio | Resolved? |
|---|---|---|---|---|---|
| C40–C60 | 2.4361 | 2.5188 | 3.34% | 0.081 | NO |
| C40–C70 | 2.4361 | 2.5338 | 3.93% | 0.095 | NO |
| C40–C80 | 2.4361 | 2.5338 | 3.93% | 0.095 | NO |
| C60–C70 | 2.5188 | 2.5338 | 0.60% | 0.014 | NO |
| C60–C80 | 2.5188 | 2.5338 | 0.60% | 0.014 | NO |
| C70–C80 | 2.5338 | 2.5338 | 0.00% | ∞ (exact tie) | trivially YES |

Five of six pairs are unresolved at this window; the sixth is a
discretization tie carrying no independent information (see P-071-1's own
caveat above).

## P-071-5 (disclosed, non-gating) — peak-cell R3, C70−C60

θ=37.2°: same sign, ratio 1.71 (inside CONFIRM band). θ=41.4°: same sign,
ratio 3.55 (**outside** the CONFIRM band's `[0.3,3.0]` upper bound, but
inside REFUTE's `[0.1,10]` band — satisfies neither pre-committed
disposition). Reported as context only, per its own non-gating status; the
interior-of-the-series `C70−C60` delta is smaller in magnitude than
`C80−C40` and correspondingly noisier under resolution refinement — not
surprising given how small the raw `C70−C60` signal already is at native
resolution (0.000188/−0.000241, an order of magnitude below `C80−C40`'s
own 0.0019/−0.0020).

## Combined Verdict: **NEITHER**

Per the pre-committed rule (`run.py::main`, computed in code): G1 PASSED,
both binding preconditions CONFIRM, but P-071-2's raw trend statistic
lands in the gray zone between the CONFIRM and REFUTE bands, **and** the
resolution-floor gate independently confirms the trend test cannot be
trusted in either direction at this window's own resolving power. This is
an **explicit, computed NEITHER — not a silent PARTIAL escape hatch**: the
underlying `C80−C40` signal (settled, resolution-robust at the peaks) is
real, and the four per-config periods do rise smoothly and monotonically
with `ABSORB` depth, but the magnitude of that rise (3.9%) sits entirely
inside the window's own frequency-resolution floor — this causal
manipulation, run properly with both mandatory preconditions passing,
**could not distinguish a genuine small ABSORB-depth dependence from
four noisy period estimates of a single underlying (non-ABSORB-tied)
period**, which is the honest finding, not a null result to be explained
away.

Caveats (mandatory fixes 3/4/5, disclosed unconditionally, printed with
every result regardless of outcome): `ABSORB` is
`lab/fdtd2d.py::Sim._damping`'s own numerical domain-truncation boundary,
not a material — no CONFIRM/REFUTE language here describes a physical
mechanism; the THERMO energy-sidecar metric does not apply (no absorbing
article run); this cycle is 600nm-only (a λ-scaling question remains
open, PHOTONICS' finding).
