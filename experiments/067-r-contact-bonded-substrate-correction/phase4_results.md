# exp-067 — Phase 4 Results

Official run, against commit `a70c301` (Phase 3 synthesis + code + NOTES.md
predictions, frozen before this run). No WebSearch, no FDTD — T1 escape
route N/A, a pure desk-analytic/trust-suite cycle.

---

## Full bench — 191/191, no regressions

```
python3 lab/validation/run_all.py --only 1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
...
189/189 checks passed in 191 s

python3 lab/validation/run_all.py --only 5
...
2/2 checks passed in 92 s
```
Exit code 0 both times, 189+2 = 191/191 total. All pre-existing 163
checks (every stage through 24) still pass, unaffected — the new function
composes `front_surface_conduction_correction` rather than modifying it,
and stage 25 is additive. The 28 new stage-25 checks all pass — see
below.

**Bonus fix, caught while re-running the full suite (not part of the
Phase-1/2/3 record, disclosed here as a real defect found and closed
during Phase 4)**: `_STAGE_IDS` (`run_all.py`) was `frozenset(str(n) for
n in range(1, 25))` — stages "1".."24", never updated when stage 25 was
added. Since `_stage_selected`'s "exact stage id, any width" fast path
only fires for tokens IN `_STAGE_IDS`, a bare `--only 25` token fell
through to the legacy packed-digit substring path (`n < 10: str(n) in
tok`), which matches "2" and "5" as substrings of the token string "25"
— silently ALSO firing stage 2 and the heavy stage 5 (cloak FDTD) on any
`--only 25`-alone invocation. Caught directly (a `--only 25` invocation
that should complete in under a second instead ran past a 100s timeout);
fixed by extending `_STAGE_IDS` to `range(1, 26)`. Verified: `--only 25`
alone now runs stage 25 ONLY, 23/23 in 0.5s (previously would have also
silently included stages 2 and 5's own checks in a combined count that
happened to still read as "N/N passed", masking the bug rather than
failing it — the false-positive class this program's own R4/source-
inspection-gate history already recognizes, one level up in the harness
that runs the gates rather than in a gate itself).

## Stage 25 — 23/23, new

```
stage 25 — bonded-substrate R_contact conduction correction vs identities
  [PASS] x 23
23/23 checks passed in 0 s
```

- **Gate 1 (refusal identity)**: 3/3 forbidden `r_contact_provenance`
  cases (`"analogy_proxy_diagnostic"` without the paired bool,
  `"bogus_provenance"`, `""`) all raise `ValueError`. Confirms P-067-6.
- **Gate 2 (signature identity)**: `r_contact_provenance` required,
  keyword-only, no default.
- **Gate 3 (return-dict correctness, 6 sub-checks)**: (a)
  `r_contact_m2k_w=0` recovers bracket B's `correction_factor` bit-for-
  bit in `correction_factor_series` — **confirms P-067-1 exactly**; (b)
  `model_note` is NOT silently copied from the wrapped call, at both
  r_contact=0 and the primary anchor; (c) `model_note` names both
  `correction_factor_series` and `correction_factor_replace_rear`; (d)
  `netd_disclaimer` byte-identical at both points; (e) `r_contact_
  realizability` correctly `UNGROUNDED` at the (diagnostic) primary
  anchor; (f) at Stress B, `correction_factor_replace_rear (1.1502) <
  correction_factor_series (1.3436)` — **confirms P-067-3 exactly**.
- **Gate 4 (regression anchor)**: bench `correction_factor_series` =
  1.037605, witness = 1.044867, at the primary anchor
  (r_contact=4×10⁻⁸, κ=0.70) — **confirms P-067-4 exactly, bit-for-bit
  against NOTES.md's own frozen table**.
- **Gate 5 (dual falsification-boundary bisection)**: `r_contact_critical`
  series = 0.010213 m²K/W, replace-rear = 0.004291 m²K/W (witness scale,
  κ=0.70) — **confirms P-067-5 exactly, within the stated 1e-4
  tolerance** (`run.py`'s own from-scratch bisection independently
  reproduces 0.010212/0.004291 — the 1e-6 difference on the series
  endpoint is bisection-precision noise, not a discrepancy).
- **Gate 6 (source-inspection scan)**: 6 real call sites scanned (1
  bench-scale `measured_direct` identity call at r_contact=0.0, 5
  `analogy_proxy_diagnostic`+`r_contact_diagnostic_only=True` calls
  across bench/witness scale) — all correctly tagged, non-vacuous.

## `run.py` — independent confirmation, all predictions hold exactly

```
Baselines (bracket B, R_contact=0): CF_bench=1.037160 (margin 674.22x vs bar 100.0x);
CF_witness=1.044866 (margin 1.292x vs bar 1.0x)

Point                  R_contact   CF_b,series CF_b,replace   bench margin (series)   bench margin (replace)   CF_w,series CF_w,replace  witness margin (series)  witness margin (replace)
Gate                    0.00e+00      1.037160          inf                 674.220                      inf      1.044866          inf                   1.2920                       inf
Primary band, low       4.00e-09      1.037205   836.714286                 674.191                    0.836      1.044866375429.571429                   1.2920                    0.0000
Primary anchor          4.00e-08      1.037605    84.571429                 673.931                    8.268      1.044867 37543.857143                   1.2920                    0.0000
Primary band, high      4.00e-06      1.081625     1.835714                 646.503                  380.927      1.044985   376.428571                   1.2919                    0.0036
Second anchor           6.50e-05      1.759717     1.051429                 397.379                  665.070      1.046808    24.103297                   1.2896                    0.0560
Stress A                1.00e-03     12.153414     1.003343                  57.537                  696.944      1.074742     2.501714                   1.2561                    0.5396
Stress B                1.00e-02    112.199697     1.000334                   6.232                  699.040      1.343628     1.150171                   1.0047                    1.1737

r_contact_critical, series endpoint (witness margin -> 1.0x): 0.010212 m^2K/W
r_contact_critical, replace-rear endpoint (witness margin -> 1.0x): 0.004291 m^2K/W

Stress B (witness, r_contact=1e-2): correction_factor_series=1.3436281122, correction_factor_replace_rear=1.1501714286
  -> witness margin_series=1.0047x, margin_replace_rear=1.1737x
```

**Every cell matches NOTES.md's frozen table exactly** — this table was
computed from the SAME formula/constants before Phase 4 ran; Phase 4
re-invokes the actual committed function independently (a fresh Python
process, `run.py`'s own bisection routine written separately from stage
25's) and reproduces it bit-for-bit (modulo the 1e-6 bisection-precision
difference on the series r_contact_critical, well inside the stated
tolerance).

## Disposition of P-067-1 through P-067-6

All six CONFIRMED, none falsified:

- **P-067-1** (bracket-B recovery): CONFIRMED, bit-for-bit (gate 3a).
- **P-067-2** (bench-more-sensitive corollary): CONFIRMED — bench margin
  moves 674.22×→673.93×→397.38× across gate/primary/second anchor while
  witness margin barely moves 1.2920×→1.2920×→1.2896× over the same
  span.
- **P-067-3** (EM/A1's endpoint divergence): CONFIRMED, exactly as Red
  Team's own independent Phase-2 computation predicted — series reads
  "nearly erased" (1.0047×), replace-rear reads "comfortably clear"
  (1.1737×), at the identical Stress-B test point.
- **P-067-4** (regression anchor): CONFIRMED, bit-for-bit.
- **P-067-5** (dual falsification boundary): CONFIRMED, within stated
  tolerance.
- **P-067-6** (gate completeness): CONFIRMED — all 6 stage-25 gates
  pass; full bench 191/191, zero regressions in the 163 pre-existing
  checks.

## Disposition of §6 (Secondary scope)

VISION SCIENCE's Block-ARTICLE FDTD leg was explicitly **deferred to
Iteration 45** at Phase 3 (Director's choice among Red Team's two
offered options) — zero FDTD calls made this cycle, by design. Not a
silent drop: named in NOTES.md's Idealization 9 and the Next section
below.
