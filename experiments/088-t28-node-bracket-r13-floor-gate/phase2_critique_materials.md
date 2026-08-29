# PHASE 2 — BLIND CRITIQUE · MATERIALS & METAMATERIALS · exp-088

## Steel-man (≤150 words)

This is a clean, cheap, well-targeted instrument cycle. It reuses the
bench's *real* physical absorber article — `pec_disk(r=30)` +
`graded_black_shell(r_in=30, r_out=78, sigma_max=0.5, eps_max=1.0)` — bit-
identical to exp-024/082/083/087's, verified against `lab/materials.py`'s
own defaults and `dg065.CONFIGS["C40"]`/`["G40"]`. Unlike exp-075's
matched-`eps=mu` numerical construct (correctly flagged at Iteration 52 as
disjoint from any realizable coating), everything measured here — and in
the R13 floor gate itself — sits on a genuinely buildable graded-loss
dielectric shell, not an abstraction. The floor-gate table's own numbers
(RMS=1.91744×10⁻³, FLOOR=1.91744×10⁻⁴, all five margins) independently
recompute exactly from `experiments/083-.../results.json::per_theta`, and
the `|C40_C|∈[0.52,0.58]` claim checks out across the full 31 points
(actual: 0.5175–0.5764). Idealization 10's realizability disclaimer is
accurate and, on a full-text search, nothing in §6/§7 quietly reopens
constraint-1/2/4 or `REALIZABILITY_MEMO.md`.

## Sharpest attack (≤150 words)

The R13 `FLOOR` this cycle computes and applies — `1.91744×10⁻⁴` — is not
a generic instrument-calibration constant; it is the RMS of
`graded_black_shell`'s own `frac_contrast(θ)` confound curve at 600 nm,
specific to this one material's optical signature. Idealization 8
discloses `FLOOR_FRAC=0.10` as a house-style *fraction*, but nothing in
the proposal flags that the resulting absolute `FLOOR` number is itself
material/wavelength-bound and must be **re-derived from scratch**, never
reused verbatim, against any other absorber article. This is a live risk,
not a hypothetical one: exp-087's own Next section (Tier 2) already
queues extending this exact channel "to the near-null σ(I) article — the
class that actually matters for constraint-3 realizability." A future
cycle building on this one's precedent, under schedule pressure, could
cite `FLOOR=1.91744×10⁻⁴` as "the" R13 floor rather than recomputing RMS
on the new material's own `frac_contrast` curve — exactly the class of
context-stripped-number reuse this program's own R4/R9 history exists to
prevent, just not yet instantiated here.

## Verdict: support-with-changes

## Single change that would flip to support

Add one sentence to Idealization 8 (or a new Idealization 13): *"FLOOR
and RMS are specific to `graded_black_shell`/600 nm and must be
independently recomputed, not reused numerically, for any other absorber
article or wavelength this gate is later applied to."* With that
disclaimer in place, the proposal has no open items in my charter's
lane — recommend support outright.
