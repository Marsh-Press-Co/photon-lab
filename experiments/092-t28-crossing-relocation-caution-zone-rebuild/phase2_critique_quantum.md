# PHASE 2 — CRITIQUE · QUANTUM OPTICS · exp-092

## Verification performed (before the deliverable below)

Independently re-derived, from scratch, every numeric/logical claim this
proposal cites as pre-verified — not taken on trust. (1) Imported
`experiments/090-.../run.py`'s actual `auc`/`firth_logistic`/
`naive_mle_diverges`/`find_zero_crossings` unmodified and ran the ORIGINAL/
DROP/RELABEL recipe against exp-090's own committed `results.json::table1`
myself: **every cell of §3's table reproduces bit-exact** (AUC=1.0/1.0/
0.833333..., zone=[1.4764,2.1709]/[1.4764,2.1709]/[1.4764,1.3095] inverted,
Firth β=[1.7806,−5.6315]/[1.1798,−4.5447]/[0.0385,−2.8425], m₅₀=2.071013/
1.818061/1.031717, naive-MLE-diverges=True/True/**False**) — no
discrepancy at 6 significant figures. (2) Recomputed §2a's linear
extrapolations directly from `results.json::a2.per_pair`'s own `v0`/`v1`:
slope(40.2→40.4)=2.7433×10⁻³/°→crossing≈40.041°; slope(41.4→41.6)=
−1.9209×10⁻³/°→crossing≈41.693° — matches to the cited precision. Widening
ratio (1.65/1.1955=1.380→38.0%) reproduces, modulo a sub-0.1%
rounding-cascade in the cited "1.196°" span (full-precision subtraction of
the actual crossing floats gives 1.19548°→1.195° at 3 d.p., not 1.196° —
traceable to rounding the 4-d.p. table entries before subtracting rather
than after; non-load-bearing, does not move the ~38% figure). (3)
Re-derived §4's τ_center arithmetic from `lab/materials.py`'s own
`graded_black_shell(sigma_max=0.5)` default and `design_geometry.py`'s
`R3_R_OUT=117=round(78×1.5)`: τ(native)=2×0.5×78=78, τ(R3,as-filed)=
2×0.5×117=117 (1.5× inflation, confirmed), σ_R3=78/(2×117)=1/3 exactly —
algebraically forced, matches. (4) Read `_run_sim_r3`/`build_article_r3`
source directly: confirmed §4a's empty-leg-reuse claim is exactly right —
`with_article` gates the only `graded_black_shell` call, so the empty
capture is bit-independent of `sigma_max` by construction, not argument.

## Steel-man

This design is the most tightly self-verified Phase-1 proposal this
sub-thread has filed: every headline number in §§2–4 is independently
reproducible from primitives I pulled myself, not restated from the
document's own prose — R4/R8 discipline actually executed, not merely
invoked. Rank 2 is a direct, disciplined completion of my own prior
(exp-091 Phase-5) finding that exp-090's zone needed exactly this
side-by-side DROP/RELABEL rebuild before being cited further; Rank 1's
asymmetric, outward-biased net is grounded in a real, re-derivable
mechanism (opposite-signed crossing shifts + amplitude inflation at a
non-adjacent control angle, ruling out pure translation), not a guessed
pad. Rank 3's τ_center derivation is airtight algebra, and its empty-leg
reuse is verified from the actual gating code, not assumed. Nothing here
outruns its own evidence.

## Sharpest attack

Rank 1 (20 of 26 calls, 77% of this cycle's FDTD spend, 4036.5 of 5247.45
CPU-s) commits to locating cpl=30 crossings using the *uncorrected*
`sigma_max=0.5` article (§2c), while Rank 3 (6 calls, 23% of spend) tests,
on the *same* cycle's own already-collected points, whether that exact
parameter choice materially contaminates this exact channel
(`delta_scene`/`frac_contrast`). Idealization 9 discloses the dependency
qualitatively ("flagged forward... not resolved this cycle") but the
design never prices it: if Rank 3 comes back REFUTE — a live, self-rated
possibility, not a formality — 100% of Rank 1's own located crossing(s)
become uninterpreted-as-filed, and the cheaper, logically prior question
(is this the right article to be searching on at all?) was never used to
gate the 3.3×-more-expensive search. Nothing forced this ordering — both
legs reuse identical geometry/config machinery and could have been
sequenced (or at least budget-contingent) at zero extra cost. This is the
same "price the cheap thing before committing to the expensive one" gap
this program's own R7/R8 lineage exists to catch, applied here to FDTD
budget allocation rather than a statistical test.

## Verdict

**Support-with-changes.** Every re-derivable number in this proposal
checks out exactly; the design is honest about the sigma/crossing
dependency but does not act on its own disclosure where a costless
resequencing was available.

## Parameter change that would flip toward unqualified support

Run Rank 3 (§4) first, as a gating precondition on Rank 1 (§2): if it
REFUTEs, redirect Rank 1's 20-call budget toward a sigma-corrected
(`sigma_max=1/3`) net instead of spending it on the currently-planned
uncorrected one.
