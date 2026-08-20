# PHASE 2 — CRITIQUE (THERMODYNAMICS) · Panel Iteration 27 · exp-050

**Charter applicability, stated plainly:** T1 escape route is NONE. Zero
FDTD, zero material law, zero absorbed power, zero ΔT, zero emission band.
My literal sidecar duty (absorbed power → temperature rise → emission band
→ detectability) has nothing to attach to this cycle, exactly as it did not
at exp-049. I am not manufacturing a thermal finding that isn't there.
Where my discipline does bite — cost/runtime accounting and reproducibility
provenance — I checked both directly against source, not the proposal's
prose.

**Steel-man (≤150 words).** The §2.3 regression anchor is a genuine
structural fix, not just "extra diligence" as claimed. I verified directly:
exp-049's `results.json.per_cell_summary` really does carry all 108 rows
with `nstar`/`c41`/`c401`/`converged_value` (confirmed by direct
inspection), so the anchor's promised check is actually executable —
unlike exp-049's own P-NCONV26-0, which Red Team caught promising a match
against data that didn't exist at that granularity. Better still, this
isn't cold ground: exp-048's own `run.py` already ran an equivalent
regression gate (`edge_diffraction_c_empty_corrected` at `GEOM_EXP042_OLD`
vs exp-042's hardcoded value, ≤1e-9 relative, 3λ) and it passed — real
precedent that the geometry-dict machinery reproduces the hardcoded
original bit-exactly, at least for the corrected convention. The cost
estimate (§6) is likewise honestly derived: I recomputed 1,145,772 from
scratch (10,609 angle-samples/cell-function × 108 combinations) and it
matches exactly; doubling exp-049's *measured* 2743.2s gives ≈91.5 min,
correctly reported as ≈90 minutes, and the domain-size argument for why
that's conservative rather than optimistic checks out.

**Sharpest attack (≤150 words).** The regression anchor's confidence is not
uniform across its own three target functions, and the proposal's framing
("fully executable exactly as stated") papers over this. Only
`beam_divergence_incoherent_corrected` inherits a working precedent —
exp-048 already proved the geometry-dict machinery (`_geom_derived`,
`field_and_h`) reproduces exp-042's hardcoded corrected-convention output
bit-exactly. `beam_divergence_incoherent` and `beam_divergence_coherent`
use the obliquity-on-E convention, which §2.2 itself admits is "not built
anywhere yet" — their OLD-geometry regression pass would be this program's
*first-ever* check of that convention's geometry-dict generalization, not
a confirmation of already-validated machinery. If the anchor fails on
these two, the proposal has no way to tell "new-code bug" from "real
geometry-transfer effect" apart, because there is no prior bit-exact
checkpoint to triangulate against, unlike the third function. Separately,
minor: §2.1 says "A shrinks 3.73%" (752→724) but the identical fraction is
correctly computed as 3.72% two lines above for the Y-domain (56/1504 =
28/752 exactly) — a small, non-load-bearing rounding inconsistency, the
same class of slip I flagged on exp-049's margin figure.

**Verdict: support-with-changes.**

**The one change that would flip me to plain support:** report the
regression-anchor's pass/fail per function, not as one pooled boolean —
and label `beam_divergence_incoherent`/`beam_divergence_coherent`'s
OLD-geometry match explicitly as this program's first verification of the
obliquity-on-E convention's geometry-dict generalization (new evidence),
distinct from `..._corrected`'s confirmation of already-precedented
machinery (repeat evidence). Fix the 3.72%/3.73% inconsistency for
internal consistency while at it. Neither change touches a prediction,
a falsification band, or the cost estimate — both are executable in the
same Phase-4 run already planned, at zero additional FDTD or wall-clock
cost.
