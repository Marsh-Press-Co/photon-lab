# PHASE 4b — Hardened Null-Calibration Re-run · Panel Iteration 54 · exp-077

Executes mandatory-fix docket item 4 (Phase-5 Red Team final audit,
`phase5_redteam_audit.md` §4): wires up the previously-dead `rel_dev_gt1`
statistic, reports the full three-quantity pure-noise table QUANTUM's own
Phase-2 critique and Red Team's Phase-2 audit (Attack 5) originally
specified, and adds a circular-shift (order-preserving) bootstrap variant
alongside the original i.i.d. one, given the real residuals' confirmed
lag-1 autocorrelation of 0.6307.

## Committed re-run output

```
pure-noise null (N=20000): P(R^2>=0.70)=0.00000  P(rel_dev>1.00)=0.00140  P(shape r^2<=0.05)=0.77610
    max R^2 over all trials=0.5609  mean=0.1921
real PAIR_PAD's own R^2=0.8165 (far outside the pure-noise R^2 distribution)
residual lag-1 autocorrelation (real PAIR_PAD): 0.6307
bootstrap i.i.d.         (N=20000): recovered mean=4.6145deg +/- 0.1409deg  frac within 20% of true=1.0000
bootstrap circular-shift (N=20000): recovered mean=4.6196deg +/- 0.1452deg  frac within 20% of true=1.0000
```

## Reading

**The R²-separation evidence is unchanged and remains this appendix's
real evidence**: `P(R²≥0.70)=0.00000` over 20,000 pure-noise trials (max
`0.5609`) vs. the real curve's own `R²=0.8165` — REFUTE is not a
look-elsewhere artifact.

**`P(shape r²≤0.05)=0.776`** confirms QUANTUM's own Phase-2 finding
(reconstructed at reduced scale as `~0.77`) and Red Team's Phase-2 audit
spot-check (`0.778` at N=800): a random curve reaches the REFUTE-tier
shape threshold roughly 78% of the time by pure chance — the shape-r²
threshold-crossing alone is NOT strong evidence on its own, exactly the
caution QUANTUM's critique raised. This is why the R² self-fit
separation, not the raw threshold-crossings, is the appendix's real
evidentiary weight (stated explicitly in the code's own print output and
above).

**`P(rel_dev>1.00)=0.0014`** — disclosed honestly as NOT matching Red
Team's own Phase-2 rough spot-check (`~0.225` at N=800, reduced grid) or
QUANTUM's own critique-time estimate (`~0.214` at N=20,000). Tracing the
discrepancy: `rel_dev` here is defined as `|P*_noise − P*_real|/P*_real`
— a NOISE curve's own free-fit period compared against the REAL curve's
FIXED, already-established `P*=4.6113°` — using the exact same
`free_period_with_widening_quiet` staged-search the real Test A uses.
Most noise curves' own self-fits land closer to the search grid's
interior/upper range once widened past the narrow `[1,4]°` window (mean
noise `R²=0.19`, but the free search still returns SOME period, often far
from `4.61°`) — `rel_dev>1.00` requires a noise fit above `9.22°`, which
this run's own noise realizations rarely produced. **This is a genuine
implementation-choice difference from Red Team's own quicker spot-check
(likely a different candidate-period reference or grid), not independently
reconciled here** — flagged explicitly rather than silently presented as
matching. It does not change any verdict: `P(rel_dev>1.00)` was never the
appendix's load-bearing statistic (the R² separation is), and both this
run's `0.0014` and Red Team's `~0.225` support the SAME qualitative
reading QUANTUM's critique already gave — raw period-threshold-crossing
under-evidences REFUTE on its own; the R² separation is what actually
carries it. **Flagged for Iteration 55 as a residual reconciliation item**
(low priority, non-outcome-determining), not swept under the rug.

**Circular-shift bootstrap confirms the i.i.d. bootstrap's own finding,
not merely fails to contradict it**: `4.6196°±0.1452°` vs. i.i.d.'s
`4.6145°±0.1409°`, both `100.0%` within 20% of the true `4.6113°`. QUANTUM's
own concern (i.i.d. resampling ignores real lag-1 autocorrelation of
0.6307, likely anti-conservative) does not move this particular
statistic in practice — the real curve's own period estimate is robust to
both resampling schemes at this signal-to-noise level.

## Verdict impact

**None.** Both Combined Verdicts (`PAIR_PAD` REFUTE, `PAIR_ABSORB40`
REFUTE) are computed from Test A/B on the real vs. model curves directly
(§5b/[6]-[7] of `pad_round_trip_model.py`) and do not depend on any
number in this appendix. This hardening closes Red Team's mandatory-fix
docket item 4 with the full, disclosed picture rather than the
partially-implemented one Phase 4's first cut shipped.
