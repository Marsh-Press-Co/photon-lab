# THERMODYNAMICS — Phase 2 Critique · Panel Iteration 56 · exp-079 (T28 y-wall full-aperture sum)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where absorbed
energy goes. Always asks what re-radiates and whether it would be detectable.
Owns the per-proposal energy sidecar: absorbed power -> temperature rise ->
emission band -> detectability. Expressibility contract: the sidecar is a
post-run analytic calculation, not an FDTD output, and is labeled as such."
Blind to all other Phase-2 critiques this cycle. Independently re-ran
`y_wall_aperture_sum.py` end to end (bit-identical to the committed JSON/
`_output.txt`, no diff written) before trusting any printed number, and
hand-recomputed every `rel_dev` and the `ss_tot` ratio directly from the
committed JSON rather than reading them off the prose (R4/R9 discipline).*

---

## Steel-man (≤150 words)

This file closes exactly the gap Red Team's own Iteration-56 Tier-0 item 1
named: it builds the FULL coherent aperture sum instead of stopping at
exp-078's single-edge proxy, re-derives `theta_local(y_s)` from the identical
image-source geometry Red Team's audit validated (generalized correctly from
one point to every aperture point), re-gates the transfer-matrix reflectance
across a genuinely new `[4.77°,15.50°]` envelope before trusting it there, and
validates a performance-only vectorized `r(theta)` bit-exact
(`7.988×10⁻¹⁶`) against the already-gated scalar function before using it at
scale. It runs a real 1x/2x/4x numerical-convergence check before trusting
the integral (`2×10⁻⁵` relative at 2x→4x — genuinely converged, not asserted),
and reports both the `Re{}` and `|·|` proxies symmetrically rather than
keeping only the one that clears SUPPORT. I re-ran the pipeline myself;
every number in `phase1_proposal.md` reproduces bit-exact from the committed
script — nothing here is hand-typed or unverifiable in the sense R4 cares
about, with one exception (below).

## Sharpest attack (≤150 words)

The one exception is load-bearing to my own seat's own arithmetic discipline.
§1/§5.2/§7 each state, verbatim, that this cycle's `ss_tot` ratio
(`9.392×10⁻⁷`) is "**nine orders of magnitude above** exp-078's own
`5.9×10⁻²⁷` ratio" (exp-078's own §2c label: "Ratio (model/real): 5.934e-27").
I recomputed this directly: `log10(9.392e-7) − log10(5.934e-27) = 20.20` —
**twenty orders of magnitude, not nine.** Grepped `y_wall_aperture_sum.py`
and both output files for "orders of magnitude"/"nine": the figure is
hand-typed nowhere in code (an R4 violation on its face). What actually IS
`≈9.78` orders is a *different* comparison the prose never states: this
cycle's own absolute `ss_tot_model` (`6.047×10⁻¹¹`) against
`SS_TOT_DEGENERATE_FLOOR` (`1e-20`, `y_wall_prescreen.py` line 322) — a
ratio-of-ratios conflated with an absolute-vs-floor check, landing on the
wrong one of two real numbers by luck of rounding (9.78→"nine"), then
citing it against the other.

## Verdict

**support-with-changes.**

The conflation does not touch anything that gates a verdict: the actual
scored `ss_tot_degenerate` boolean is computed correctly in code (`False`,
independently re-verified: `6.047497e-11 ≥ 1e-20`), and I independently
re-derived all six Test-A `rel_dev` values by hand from the committed
`P*_model`/`P*_real` pairs in `_output.txt` — every one reproduces to the
printed digit (worked below). The document's central, qualitative finding —
a genuine, converged, non-degenerate signal that tracks T21's own
established `A=752` fringe (`rel_dev` `0.016`–`0.035`) rather than any of
T28's three real periods (`rel_dev` `0.29`–`0.57`) — survives this
correction untouched; the mechanism argument in §5.3 (two near-identical
frequencies' difference cannot manufacture a third, independent frequency)
does not depend on which order-of-magnitude figure decorates the degeneracy
check. But "nine orders of magnitude" is repeated three times as rhetorical
weight for exactly how decisively non-degenerate the result is, is wrong by
eleven orders of magnitude on the comparison it explicitly cites, and is the
same hand-typed-comparison-figure failure shape this exact T28 sub-thread
has now caught at exp-076 (Idealization/T5 conflation), exp-077 (a
THERMODYNAMICS arithmetic slip on absorbed-power percentages, caught by Red
Team), and exp-078 (VISION's/my own seat's independent catch of a stale
"≥99.9999%" digit, corrected to "≥99.9996%"). Two changes required:

1. **Fix "nine orders of magnitude" to "twenty" in all three places** (§1,
   §5.2, §7), or — better — replace it with the comparison that IS
   `≈9.78` orders (`ss_tot_model` vs `SS_TOT_DEGENERATE_FLOOR`), computed in
   code and printed, if that is the intended claim; do not silently retarget
   the citation without saying so.
2. **State the THERMO sidecar disposition explicitly, in one sentence.**
   This file computes zero absorbed-power number and belongs to the same
   T1-route-N/A, instrument-fidelity class every T28 cycle since exp-071 has
   carried an explicit N/A disposition for — but the sentence is missing
   here exactly as it was missing in exp-078's own as-filed proposal. I
   flagged this identical gap in exp-078's own Phase-2 critique as one of
   two required changes; Red Team's Phase-2 audit there adopted my
   cancellation-argument/near-total-absorption finding but never adopted
   the "state the sidecar sentence" ask into its mandatory-fix docket, and
   it was not added at any later phase of exp-078 either. This is now a
   second consecutive cycle with the identical one-line omission, after
   being named explicitly once already — worth closing this time, not
   re-discovering a third time.

On the substantive question my own charter is most responsible for this
cycle — does summing `r(theta_local(y_s))` across ~1,504 aperture points
quietly reopen an energy-bookkeeping question the proposal doesn't
address — my independent read is **no, the N/A disposition would be
correct if stated**: every `r(theta_local(y_s))` weight here is reused,
unchanged, from `boundary_reflectance.py`'s already-gated, already-adjudicated
transfer-matrix reflectance (§3.1's own premise, itself resting on exp-078
§3.4's `Sim._damping` verification, not re-verified again here per house
discipline against redundant re-derivation of an already-settled premise).
`|r|` stays deep in the near-total-absorption regime across this file's own
wider angle envelope (per-config `ptp(Re E_echo)` spans `1.8×10⁻⁷`–
`1.7×10⁻⁵`, still tracking the same `C40`/`G40` (`ABSORB=40`) >> `C60`/`C70`/
`C80` ordering exp-078 established) — this construction is a coherent-field
interference calculation built entirely from an already-settled reflectance
model, not a new absorbed-power computation, and does not by itself imply
any new re-radiation/detectability question beyond what exp-075/077/078's
own THERMODYNAMICS reviews already closed for this exact `r(theta;ABSORB)`
object. The gap is a missing *sentence*, not a missing *physics finding*.

## Single change that would flip my verdict

To **oppose**: if my own recomputation of the "nine orders of magnitude"
claim had instead found the correction moved the *absolute* `ss_tot_model`
value itself closer to the `SS_TOT_DEGENERATE_FLOOR` than the document
claims — i.e., if the scored `ss_tot_degenerate=False` gate turned out to
be wrong, not merely the prose decorating it — that would undermine the
"real, resolvable signal" premise the whole §5.2–§7 argument rests on. I
checked this directly and it does not: `6.047497e-11` is comfortably
`9.78` orders above `1e-20` under either framing, so the gate itself is
sound.

To **support** outright (no changes needed): both items above land —
"nine" corrected to the right figure (or the right comparison) in all three
places, and the one-line THERMO N/A disposition added — with zero change to
any scored number, Test-A verdict, or the self-scored §7 characterization.

---

## Independent verification notes (for the record)

- Re-ran `python3 y_wall_aperture_sum.py` end to end: output is bit-identical
  to the committed `y_wall_aperture_sum_results.json`/`_output.txt` (no diff
  written to disk on re-run) — every table in `phase1_proposal.md` traces to
  an actually-invoked computation, not a hand-typed transcription, with the
  one exception above.
- Hand-recomputed all six Test-A `rel_dev` values directly from
  `P*_real`/`P*_model` in `_output.txt` §[6]/[6b]:
  `|2.0301−2.8421|/2.8421=0.2857`; `|1.9925−4.6113|/4.6113=0.5679`;
  `|2.0226−4.1761|/4.1761=0.5157`; `|1.0075−2.8421|/2.8421=0.6455`;
  `|1.0075−4.6113|/4.6113=0.7815`; `|1.0075−4.1761|/4.1761=0.7587` — all six
  match the printed values exactly.
- Hand-recomputed the three vs-T21 `rel_dev` figures in §6a:
  `|2.0301−1.9608|/1.9608=0.0353`; `|1.9925−1.9608|/1.9608=0.0162`;
  `|2.0226−1.9608|/1.9608=0.0315` — all three match, confirming the "1.6%–
  3.5%" and "28.6%–56.8%" figures quoted in §1/§5.3's prose.
- Recomputed the `ss_tot` ratio directly:
  `6.047497e-11/6.439269e-05=9.391589e-07`, matches the printed
  `9.392×10⁻⁷` to the given precision.
- Recomputed the orders-of-magnitude gap two ways: `log10(9.391589e-07) −
  log10(5.934e-27) = 20.20` (the comparison the prose actually cites — NOT
  nine); `log10(6.047497e-11) − log10(1e-20) = 9.78` (the comparison that
  IS approximately nine — a different pair of numbers than the one named).
- `grep -n "orders of magnitude" y_wall_aperture_sum.py _output.txt
  y_wall_aperture_sum_results.json`: zero hits in any of the three — the
  figure exists only as prose in `phase1_proposal.md`, confirming it is
  hand-typed, not invoked.
- Confirmed exp-078's own cited figure is itself labeled a *ratio*, not a
  *floor*: `phase5_redteam_audit.md` §2c reads "Ratio (model/real):
  5.934e-27" — this document's own "5.9×10⁻²⁷ floor" phrasing (§1, §7) is
  imprecise on top of the magnitude error; `SS_TOT_DEGENERATE_FLOOR` is the
  actual, differently-valued (`1e-20`) floor in this program's own code.
- Re-read `lab/fdtd2d.py::Sim._damping` construction and
  `boundary_reflectance.py::reflection_coefficient`'s own gates one more
  time (not re-run — exp-078 §3.4 and this file's own §3.1/§1 already
  settle the premise `r()` is unchanged and reused, not rebuilt) to confirm
  no new absorbed-power computation appears anywhere in
  `y_wall_aperture_sum.py`: confirmed, `grep -n "absorb\|Absorbed\|power\|
  Poynting\|Sx" y_wall_aperture_sum.py` returns only `ABSORB`-the-parameter
  references, never a power/flux computation.
