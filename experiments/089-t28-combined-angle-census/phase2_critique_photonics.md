# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 66 · exp-089

*Blind critique. Independent numeric re-derivation performed against
`experiments/083-.../results.json` and `experiments/088-.../results.json`
(no other seat's critique read).*

## Independent verification performed

Re-derived from raw primitives, all confirmed exact:
- Zero-crossings by linear interpolation of `delta_scene(θ)` in
  `exp-083/results.json::per_theta`: 37.1272° (between 37.0°/37.2°),
  40.2654° (40.2°/40.4°), 41.4610° (41.4°/41.6°) — matches the cited
  37.127°/40.265°/41.461° to the displayed precision.
- `frac_contrast(θ)=|delta_scene/C40_C|` at all three new angles:
  4.162655×10⁻⁴, 2.830881×10⁻⁴, 2.510967×10⁻⁴ — bit-exact match.
- `FLOOR=0.10×RMS[frac_contrast]`=1.91744×10⁻⁴ (`exp-088/results.json::
  r13_floor_gate`) and all three margins (2.17×, 1.48×, 1.31×) — exact.
- `dg069.DENSE_ANGLES[6]/[21]/[27]` = 37.2/40.2/41.4 — exact (grid is
  `36.0+0.2·i`).
- The "double duty" gap claim: 37.2° is the *exact* midpoint of
  36.0°→38.4° (1.2°/1.2°); 40.2°/41.4° split 38.8°→41.8° into
  1.4°/1.2°/0.4° — arithmetically correct as stated.
- Q4's cited interpolated values (37.2°≈1.63×10⁻³/≈3.05×10⁻³→ratio_k
  ≈3.9/≈7.3; 40.2°≈6.54×10⁻³→ratio_k≈23.1; 41.4°≈7.05×10⁻³→ratio_k
  ≈28.1, using `frac_p_abs` from exp-087/exp-088's own committed data)
  all reproduce, confirming the "20–28" and "≈6.5×10⁻³"/"≈7.05×10⁻³"
  figures cited in §6.

All of this checks out. The defects below are conceptual/framing, not
arithmetic — with one exception noted in the attack.

## Steel-man (146 words)

This is a tightly-scoped, self-critical instrument-fidelity cycle. Every
desk-computable number in §4 — three zero-crossings, three
`frac_contrast` values, `FLOOR`, all three margins, the `DENSE_ANGLES`
indices — independently reproduces exactly from already-committed
exp-083/exp-088 data; I re-derived all of them from primitives above. The
"double duty" combined-census claim is arithmetically correct, not just
asserted. R13/R14 are applied honestly with real, disclosed, uncomfortable
margins (1.31×–2.17×) rather than cherry-picked comfortable angles, and
Q3's bands are deliberately widened rather than narrowed, citing exp-088's
own 38.4° interpolation miss as the reason not to trust a tight number
here. Q4 is explicitly disclaimed as a directional signal, not a formal
period claim, correctly invoking R5/R10's look-elsewhere discipline rather
than smuggling a period claim past it. This is good, disciplined T28
house practice.

## Sharpest attack (150 words)

R14(c)'s half-period bound uses `delta_scene`'s own established
~2.84–2.95° period as the safety yardstick for `frac_p_abs` (numerator)
gaps. But the only direct evidence this sub-thread has about
`frac_p_abs`'s *own* native angular scale is exp-088's 38.4°→38.6° step:
a 3.07× swing across 0.2°, a feature EM already flagged as narrower than
the bracket-width bound could see. Borrowing a different curve's period
as this quantity's own safety margin, then citing the result as "clears
by 0.02–0.075°," is exactly the operand-mismatch R9 exists to catch — the
comparison is dimensionally fine but conceptually the wrong quantity.
Against `frac_p_abs`'s actually-demonstrated (sub-0.4°) scale, the 1.4°
gap isn't a near-miss, it's ~3.5× too wide to guarantee no hidden
feature. Compounding this: §4 itself calls 41.4°'s 1.31× margin "the
thinnest... ever sent to FDTD," two sentences after citing 38.6°'s own
0.39× — sent to FDTD twice already (exp-087, exp-088) — a
self-contradicting superlative inside the same paragraph.

## Verdict: support-with-changes

The FDTD plan itself is sound and cheap (12 calls, reused machinery,
correct grid indices); nothing here blocks running it. But two fixes are
needed before the results are trusted: (1) correct or scope the "thinnest
margin ever sent to FDTD" claim (it is false as written); (2) do not let
Q6's combined classification rest on the 38.8°→40.2° 1.4° gap clearing
R14(c) against the borrowed `delta_scene`-period yardstick alone — report
explicitly, alongside Q6, that this gap is *not* protected against a
feature on `frac_p_abs`'s own demonstrated (sub-0.4°) scale, using the
language already drafted for Idealization 11 but currently undersold by
the "clears by 0.02–0.075°" framing.

## Single parameter change that would flip this to oppose

If `FLOOR_FRAC` were tightened from 0.10 toward the value Q5 itself
proposes testing — say 0.20, which 40.2° (1.48×) and 41.4° (1.31×) would
both fail *before any FDTD runs* — I would oppose sending these two
angles at all until Q5's own antecedent question (is 0.10 adequate near
a crossing) is resolved first. Running the census now and using its own
output to judge the gate that licensed it is a soft circularity the
proposal discloses (§4, Q5) but does not avoid.
