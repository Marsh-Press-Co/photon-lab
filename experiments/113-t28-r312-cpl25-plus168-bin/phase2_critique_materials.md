# Phase 2 Critique — MATERIALS & METAMATERIALS (exp-113, Panel Iteration 90)

*Fresh sub-agent, blind context. I have not seen and did not seek out any
other seat's Phase-2 output this cycle. Charter (verbatim, PANEL.md):
sub-wavelength structure; what could physically realize the proposed
optical behavior; owns the realizability bound (published / plausible /
unobtainium-with-parameters). Read PANEL.md, LOGBOOK.md (RULED OUT
registry, the T28 opening at Iteration 46, and the full Iteration 89
entry/exp-112's Phase 5 record), and this cycle's `phase1_proposal.md`,
`run113.py`, `chunk_runner113.py`, `analyze113.py` in full. Independently
re-ran `python3 run113.py --verify-geometry` and `--predictions-only`
(both reproduce the document's own cited output, `pass_=true` at both
r, `_SPONGE_MARGIN_ORDERS≈4.0`) and re-derived every numeric claim below
directly from `results.json`/`run112.py`/`run113.py` primitives, not from
this document's own prose.*

## Charter-fit note, stated up front

Like VISION last section, I flag that my own charter's substantive
burden — bounding whether a proposed optical behavior is
published/plausible/unobtainium — barely engages here: this cycle
proposes zero new material or mechanism (T1 N/A, confirmed
independently). The PEC-core/graded-black-shell geometry itself was
realizability-scored in earlier phenomenon cycles, not reopened here.
What I *can* independently police under my own charter is exactly what
this cycle's own instructions ask: whether the sub-wavelength boundary
condition (the ABSORB/EDGE sponge, and the PEC/shell geometry it wraps)
actually transfers congruently to the new scale, and whether the
disclosed safety-margin arithmetic is computed against the physically
correct comparator.

## Steel-man (≤150 words)

The geometry-scaling recipe is a genuinely careful reuse, not a sloppy
transplant. I independently computed the sponge's physical clearance
relative to the shell it protects at both radii: `(CX−ABSORB)/R_COAT` =
2.974 at r=156/cpl=25 vs. 3.103 at r=312/cpl=25 — the sponge sits at
essentially the same *relative* distance from the scatterer at both
scales, confirming the "kappa_ratio=2.0 congruent scale-up, not an
independent construction" claim genuinely holds at the boundary-condition
level my charter cares about, not merely in `tau_shell`/`sigma_max`'s
already-proven algebraic invariance. Reusing (not re-deriving) the
cpl-specific log-attenuation figure is correct reasoning: ABSORB/EDGE
depend on cpl alone. And MATERIALS' own prior-cycle finding (F2, exp-112)
that `tau_shell`-invariance holds to <0.01% in real energy-ledger data
is the right precedent to lean on here.

## Sharpest attack (≤150 words)

`_SPONGE_MARGIN_ORDERS` (~4.02, I reproduce `log10(3.3826e-4/3.2489e-8)
=4.018` exactly) compares sponge leakage to `BASELINE_FLOOR` — the
mirror-pooled *noise-floor* of the whole 48-bin pattern, not the named
bin's own signal. The named bin's peccored/hollow magnitudes
(8.740e-5/9.692e-5) sit *below* that floor (why `local_snr=0.258/0.287
<1`), and `|delta|` (9.510e-6, the quantity Check B scores) sits further
below still. Recomputed against what the checks actually test: **~3.43
orders vs. peccored/hollow, only ~2.47 vs. |delta|** — not ~4.0. That's
inside the "3–4 orders → oppose" zone EM's own exp-112 critique
pre-registered. The floor is the wrong comparator — it's the
instrument's detection threshold, not the signal magnitude under test.
(Not the sponge behaving differently at r=312 — its relative clearance
is preserved, 2.97→3.10× R_COAT — it's that the disclosed figure
compares to the wrong of two available quantities, the same
"downstream comparator never independently recomputed" shape MATERIALS'
own F1 caught last cycle.)

## Realizability note (secondary, non-load-bearing)

Named for completeness since the task asks: at cpl=25, `R_COAT=390`
cells ⇒ physical shell radius ≈ 390/25·λ ≈ 15.6λ (≈9.4 µm at 600 nm) — a
scale where sub-wavelength feature control (graded absorptive shells,
PEC cores) is published/plausible with existing metamaterial fabrication
(e-beam/FIB-patterned lossy metasurface shells at tens-of-nm tolerance).
This cycle is not attempting to fabricate anything, and no
mechanism/material claim is scored — so this is background context, not
a finding that bears on this cycle's own verdict.

## Verdict: **support-with-changes**

Not outcome-reversing — T1 stays N/A, `classify_resolution_check`'s own
arithmetic uses `BASELINE_FLOOR` correctly elsewhere (as the K=1 SNR
denominator, its intended role), and the corrected margin (~2.5–3.4
orders) still supports "non-fatal" given the ~10⁻¹-scale relative
deviation actually under test. But the specific `_SPONGE_MARGIN_ORDERS`
figure, as computed, compares sponge leakage to the wrong quantity for a
document whose own stated purpose is disclosure completeness (VISION's
own two additions this cycle), and this program corrected an
arithmetically-identical shape (F1, "6–8" vs "~1.8–4.5 orders") only one
cycle ago. Recommend computing and disclosing the margin against the
named bin's own peccored/hollow magnitude and against `|delta|`
alongside the floor-based figure, before Phase 4 freezes this into the
DISCLAIMER string R23 will assert permanently.

**Single parameter change that would flip my verdict to oppose:** if
Phase 3 ships `_SPONGE_MARGIN_ORDERS` as the *sole* disclosed
sponge-safety figure (comparator = floor only, no peccored/hollow/delta
alternative computed or disclosed) — that would repeat, uncorrected,
within one cycle of its own discovery, the exact "unverified downstream
comparator riding on correctly-verified antecedents" pattern this
program's R4/R9/R30 lineage exists to catch, this time for MATERIALS'
own charter question specifically.
