# PHASE 5 — BLIND FINAL REVIEW · PHOTONICS · Panel Iteration 61 · exp-084

*Seat: PHOTONICS. Fresh context, no memory of Phase 1 (even though PHOTONICS
led it). Charter: is the proposal's optical response coherent as stated,
across wavelength and angle? Reviewed the complete record — proposal
(including the Phase 3 correction appended to it), `phase1_derivation.py`,
`phase1_output.txt`, all five Phase-2 critiques, the Phase-2 Red Team audit,
`phase3_synthesis.md`, `phase3_fix_docket_checks.py`/`_results.json`,
`NOTES.md` — plus PANEL.md and the relevant LOGBOOK.md sections (RULED OUT
R1–R9, Iterations 58–60, LIVE THREADS/T28). Independently re-ran code and
wrote new stress-test code of my own; findings below are cited to specific
commands and files, not restated from the record.*

## 1. Independent verdict: **PARTIAL**

This matches Phase 3's Combined Verdict, but I did not arrive at it by
reading Phase 3 and agreeing — I re-derived the two decisive numbers myself,
ran a stress test the record does not contain, and read the leg-(b) source
directly before forming this opinion. Where I have nothing to add beyond
confirming Phase 3, I say so below; where I found something new, it is
flagged as mine.

Leg (a): the period-match downgrade to INCONCLUSIVE is correct and I
independently reproduce both routes to it. The shape-correlation finding
(`r=+0.958`) is real, and my own additional control (§2.2) makes it *more*
credible than the record already argues, not merely as-credible. Leg (b)
remains correctly NO-VERDICT; I found a third, untested cause for its
Anchor-2 failure that neither the original write-up nor EM's critique
named (§2.3). One process-hygiene defect, non-load-bearing, found and
corrected in the working tree then reverted so the record is left exactly
as Phase 3 committed it (§2.1).

## 2. What I verified myself

### 2.1 Re-ran `phase3_fix_docket_checks.py` — bit-exact, plus a real committed-artifact defect

Running `python3 experiments/084-.../phase3_fix_docket_checks.py` fresh
reproduces every number Phase 3 cites to full precision:
`leg_a_vs_real_C80 = +0.958186`, `leg_b_own_masked_output_vs_real_C80 =
-0.104597`, linear ramp `-0.334705`, quadratic `-0.553409`; circular-shift
null `15/30 = 50.0%`, `mean=0.4594`, `max=0.7302`, `min=0.2892` — all
matching `phase2_redteam_audit.md` and `phase3_synthesis.md` exactly.

But before I ran it, I *read* the already-committed
`phase3_fix_docket_results.json` (the file these numbers are supposed to
be sourced from, per R4) and it did **not** match what the script produces:
it contained a key `"leg_b_nomask_own_output_vs_real_C80 (control)"` =
`0.9022947333208244` — a different label (`nomask` vs the script's own
`own_masked_output`) and a materially different number (`0.902`, not
`-0.105`) from the value the prose everywhere cites. Running the script
overwrote the file to the correct values (`git diff` confirmed a
one-line change, nothing else); I reverted that write
(`git checkout -- phase3_fix_docket_results.json`) so I leave no footprint
on the record — the finding is reported here, not enacted as a silent fix.

This is a genuine, if non-load-bearing, R4-family defect: the script and
the JSON were added in the *same* commit (`52dcbb2`), yet the checked-in
JSON does not reproduce from the checked-in script — it reads like output
from an earlier draft (`mask_r_out=0`, i.e. the ANCHOR-2 no-mask
composition-identity curve, not leg (b)'s real masked output) that was
never regenerated after the script was finalized. It does not change any
verdict — every number actually *cited in prose* (`phase1_output.txt`,
both Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`)
already states the correct `-0.10`, so no argument in the record actually
relied on the wrong committed number. But it is exactly the shape of gap
R4's own lineage exists to catch (a "committed, not hand-typed" artifact
that does not itself reproduce), and I flag it for the Director to
regenerate the file properly rather than leave a silently-stale JSON
sitting in the permanent record next to a commit message that claims it
matches.

### 2.2 A sharper specificity control than the proposal's own three: aperture-width sensitivity

The task the seven-seat brief poses to my charter specifically: are leg
(b)/ramp/quadratic the *right* controls for the `r=0.958` shape-correlation
finding, or would a curve from the same diffraction geometry at a nearby
but wrong aperture width also correlate this well — which would make the
finding a generic "two smooth near-field curves over a narrow window
resemble each other" artifact rather than genuine physics?

I wrote an independent script (not reusing `phase1_derivation.py`'s
`leg_a_curve`, only its two upstream primitives, `dg048.field_and_h`/
`edge_diffraction_c_empty_corrected` and `dg065.propagator_geom`) that
recomputes the *identical* source-aperture diffraction integral with the
aperture half-width `A` perturbed away from the true `752` cells, holding
every other parameter (`OBJ_Y`, `D_SP`, `TAPER`, `λ`) fixed, and measures
`corr(curve, real FDTD C80(θ))` at each perturbed `A`:

```
A_target   %dev    r vs real C80
   601.60   -20%   -0.2816
   699.36    -7%    0.3350
   714.40    -5%   -0.5545
   744.48    -1%    0.4527
   752.00     0%    0.9582   <- true A, matches the record exactly
   759.52    +1%    0.8843
   767.04    +2%    0.4327
   774.56    +3%   -0.3353
   789.60    +5%   -0.8410
   902.40   +20%   -0.3716
```

This is the better control the charter asked me to consider, and it
**corroborates rather than undermines** the finding: correlation is not a
flat, generic ~0.9-ish plateau across nearby geometries (which is what a
"any smooth curve over this window resembles any other" artifact would
look like) — it falls to `0.45` at `-1%`, oscillates through
strongly negative values by `±3–5%`, and never returns above `0.88`
anywhere off the true value in this sweep. There is a real, if not
infinitesimally narrow, neighborhood (`±~1%` of `A=752`) where the match
stays strong, consistent with ordinary continuity of a physical model
near its true parameters — not with an artifact of generic curve
smoothness, which would not care about the exact aperture width at all.
**I independently corroborate `r=0.958` as a genuine, structure-sensitive
match**, a stronger statement than the record itself makes (it only
tested three qualitatively different curve shapes, never a
same-geometry/wrong-parameter control).

### 2.3 The causal-attribution question for leg (b)'s Anchor 2: a third possibility

Phase 3 correctly declines to adopt either the original write-up's guess
("missing Rayleigh–Sommerfeld boundary term") or EM's alternative ("missing
phase-carrying obliquity factor from feeding a bare field into a
current-convention `propagate()`") as settled, per Red Team's fix-docket
item 3. I read `leg_b_curve()` and `composition_identity_convergence()`
directly (`phase1_derivation.py` lines ~304–357) to assess whether either
survives my own optical-coherence scrutiny, and found a third candidate
neither considered.

EM's account is coherent as far as it goes, with one refinement: the
`propagate()` function already carries a spatially-varying obliquity term
(`obliquity = dx/r`, weighting the H-channel — this is genuine RS-style
physics, already present, contra the original write-up's "missing RS
term" framing taken literally). A *global* constant phase factor
(e.g. the "90°-rotating normalization constant" EM names) could not by
itself explain a real amplitude change in `Sx = -Re(E·conj(H))`, since a
common phase multiplied onto both `E` and `H` cancels exactly in that
product — only a **spatially-varying** (angle/position-dependent) missing
weighting can. EM's actual claim is exactly this (treating stage-1's bare
field `E1` as a driving current when feeding it to `propagate()`, rather
than converting it through the correct field→secondary-source relation),
so the substance holds; only the "phase-carrying" framing is loose and
could mislead a future reader into chasing a pure-phase fix that cannot
work.

**A third, untested cause**: `leg_b_curve()`'s stage-1 output (`E1`) is
evaluated only over `y_grid = gd1["y_obs"]`, **the same finite span
`[y_lo, y_hi]` as the original source aperture** — and stage 2 re-uses
that identical, unwidened span as its own secondary-source domain. The
dedicated convergence check (`composition_identity_convergence`) only
refines the sampling *density* within this fixed window (`dy=1/factor`,
factors 1×–8×) — it never widens the window itself. A genuine diffracted
field spreads somewhat beyond the geometric aperture edges after
propagating `d1=130` cells; truncating the secondary-source integral to
exactly the original aperture bounds discards that spillover before stage
2 ever sees it. This is a **domain-truncation** defect, not a
phase/obliquity-convention bug and not a "missing boundary term" in the
Rayleigh–Sommerfeld sense — and critically, it produces exactly the
observed signature (a *stable*, non-shrinking mismatch under density
refinement, since refining `dy` inside a fixed-width window can never fix
a fixed-width truncation). The existing convergence test cannot
distinguish this from either of the two hypotheses already on the table.
**This is a real gap in the record's own causal-attribution work**: Phase
3 was right not to adopt either existing guess as settled, but the reason
given (EM's cheaper test vs. the RS-term guess) does not exhaust the
candidate space, and the cheapest test of all — widen the intermediate
window (e.g. `y_lo - Δ` to `y_hi + Δ` for a few values of `Δ`, holding `dy`
fixed) and see whether the Anchor-2 ratio moves toward 1.0 — was not run
and is not yet queued anywhere in `NOTES.md`'s Next section.

### 2.4 R10 — stated correctly

I checked R10's text in `phase3_synthesis.md` against its own two cited
precedents (exp-083's two-tone reversal, this cycle's leg (a) downgrade)
and against Red Team's recommendation it claims to formalize
(`phase2_redteam_audit.md` §3, last bullet). The rule is accurately scoped:
it distinguishes specificity-over-targets from null-under-noise correctly,
states plainly that it does not resolve which null family (circular-shift
vs. AR(1) or other) is correct for which residual structure, and does not
overclaim generality beyond what two data points support. No correction
needed from my charter.

### 2.5 On the general specificity/simplicity question the brief raised

The brief's own hypothetical stress test — leg (b)'s `r=-0.10` control —
is in fact one of the more informative of the three already in the record
(it is a genuine physically-related but geometrically-different
diffraction construction, not an arbitrary curve), and I confirm via §2.2
that a *same-mechanism, wrong-parameter* construction is an even sharper
version of exactly that idea. I found no simpler, non-physical explanation
for `r=0.958` (e.g., a resolution/sample-count coincidence): both curves
are sampled at the identical, already-fixed 31-point grid every T28 cycle
uses, so there is no shared-instrument artifact available to explain the
correlation.

## 3. Ranked top-3 candidate next directions for Iteration 62+ (PHOTONICS' own vantage)

1. **Before any more FDTD is spent on leg (b): run the domain-truncation
   test (§2.3) alongside EM's already-queued obliquity/phase-convention
   test.** Widen the stage-1→stage-2 intermediate secondary-source window
   by a few cell counts beyond `[y_lo, y_hi]`, holding sampling density
   fixed, and see whether the Anchor-2 ratio (currently stable at
   `2.894–2.895`) moves toward 1.0. This is strictly cheaper than EM's
   test (no new physics convention to re-derive, just a wider `arange`),
   discriminates a third real hypothesis the record has not yet ruled
   out, and is a precondition for leg (b) — the one leg with genuine
   realizability content per MATERIALS — ever producing a trustworthy
   SUPPORT/INCONCLUSIVE/REFUTE.
2. **The properly-powered re-test of leg (a)'s own period, at a wider or
   denser angular window** (already named in `NOTES.md` item 4, and now
   better-motivated by my own §2.2 finding that the shape match is
   genuinely structure-sensitive, not generic): since the shape
   correlation is real and demonstrably specific to the true aperture
   geometry, this is the highest-value way to learn whether `P_edge_A`'s
   physical origin can finally be pinned down, rather than merely
   re-confirming (a ninth-plus time) that this sub-thread's period
   questions are underpowered at 31 points.
3. **Once leg (b)'s kernel passes its own Anchor 2 (via #1 above and/or
   EM's fix), replace its 100%-opaque Kirchhoff rim mask with the
   article's actual complex reflection/transmission coefficient**
   (reusing the already-built `d80.reflection_coefficient_vec`/
   `_realizable` machinery from Iteration 58, applied at the rim edge
   instead of a hard cutoff). Every T28 cycle since exp-075 has modeled
   the boundary as *either* a pure reflector *or*, this cycle, a pure
   diffractor with an unphysical fully-opaque edge; a genuine
   diffractor-at-a-partially-reflecting-edge synthesis has never been
   attempted in this nine-plus-cycle sub-thread and is a natural,
   zero-new-FDTD next step directly in my own charter (this is precisely
   a surface-interaction/scattering-cross-section question) once the
   instrument itself is trustworthy.

I do not rank the energy-interception cross-check here even though it is
the program's own top institutional priority (Checkpoint criterion 4 just
fired on it) — that item belongs to EM/THERMODYNAMICS' charter, not mine,
and the record already queues it correctly for Iteration 62 on a cycle
with a real article-loaded scene.
