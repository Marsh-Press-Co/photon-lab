# exp-021 — Does exp-020's r2=75 Box-Independence Gate Miss Survive Resolution?

**2026-08-12 · driver: Clyde (cloud shift 10) · status: predictions committed, not yet run**

exp-020 (this shift) found that at r2=75, floor=0.10, 4 of 7 core points
miss the box_dev ≤2% gate (2.55%–3.36%), while every r2=120 point and
every r2=75/floor=0.18 point clears it comfortably (max 1.78%). Rather
than argue about a borderline number or discard it silently, this line
has a standing precedent (exp-004→005, exp-009→010, exp-014→015): rerun
at 1.5× resolution (cpl 20→30), geometry scaled to hold physical size
fixed, and let refinement settle whether it's a real effect or a grid
artifact.

## Setup

exp-015's exact scaling machinery (N, CX/CY, ABSORB, STEPS, SRC_X,
REF_HALF_H, MIN_MARGIN, box halves all × 1.5, courant_frac unchanged —
the eps_z-based CFL ceiling is f-invariant), applied to exp-020's r2=75
sub-sweep instead of exp-014's r2=90 baseline.

**Three of exp-020's seven r2=75 core points**, exp-015's own
minimal-but-decisive three-point idiom (not the full bracket):

| base r1 (cpl=20) | why chosen | scaled r1 (cpl=30) | eps_z (cpl20 → cpl30) |
|---|---|---|---|
| 13 | worst gate miss (box_dev=3.36%) | 20 | 1.4633 → 1.4820 |
| 15 | the shell=3λ target itself (2.55%) | 22 | 1.5625 → 1.5486 |
| 18 | clean flank, control (1.89%, already inside gate) | 27 | 1.7313 → 1.7362 |

r2 scales 75→112 (75 is not a multiple of 2, so this carries the same
small sub-cell rounding exp-015 accepted at its own r1=33→50 point — the
scaled eps_z values above land within 1.3% of their cpl=20 originals,
smaller than the box_dev gate miss being investigated). `check_gates()`
run standalone first: all 3×2=6 combinations clear both CFL (worst
margin: base=13/floor=0.10, ceiling=0.3849 vs courant_frac=0.32) and the
degeneracy threshold (worst margin: base=18/floor=0.18, threshold=0.5760
vs floor=0.18) comfortably — zero exclusions.

6 cloak runs + 1 empty reference = **7 runs total**.

## Idealizations

Same as exp-015/010/005: this checks whether exp-020's specific gate
miss is a cpl=20 grid artifact, not a re-verification of the whole
r2=75 sweep. Only base=13/15/18 are re-run; base=12/14/16/17 (also part
of exp-020's original 7-point bracket, base=12/14 also missed the gate)
are not directly re-checked — the 3 chosen points bracket the worst
miss, the target, and a clean control, following the same "enough to
test whether the anomaly's existence survives, not a full remap"
reasoning exp-015 used.

## Predictions — committed before the run

- **P1 (gates):** box_dev shrinks substantially at cpl=30 relative to
  cpl=20 at all three points — expecting the miss to clear 2% at base=13
  and base=15 (the two currently-failing points in this subset), the
  same qualitative resolution-cures-the-gate pattern exp-005/010/015 all
  found. base=18 (already clean) should stay clean or improve further.
- **P2 (does the discriminator survive?):** the jump magnitude at all
  three points stays strongly positive and within roughly 20% relative
  of its cpl=20 value (exp-005's own resolution shift was 7% relative;
  exp-015's was also ~7%) — i.e., exp-020's r2-specific conclusion (no
  negative jump anywhere near r2=75's own shell=3λ point) is not an
  artifact of under-resolved box-independence. A jump flipping sign or
  moving by an order of magnitude at any of the three points would be
  the actual surprise here, not the expected outcome.
- **P3 (secondary, not scored pass/fail):** box_dev improvement should
  scale roughly with the 1.5× resolution the way exp-005 (7% relative
  jump-value shrink) and exp-010 (order-of-magnitude box_dev drop) did —
  logged for the record, not gated, since this line has seen both a
  modest shrink (exp-005/015) and a dramatic one (exp-010) depending on
  how close the original run was to the noise floor.

## Results

*(not yet run)*

## Next

*(not yet written — depends on results)*
