# PHASE 5 — BLIND FINAL REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 61 · exp-084

*Fresh sub-agent, no memory of any prior session including this cycle's own
Phase-2 MATERIALS critique. Independent re-verification from the committed
record, per charter: sub-wavelength structure; what could physically realize
the proposed optical behavior; owns the realizability bound (published /
plausible / unobtainium-with-parameters).*

## 1. Independent verdict: **PARTIAL** — concurring with the Combined Verdict,
reached independently from my own charter's vantage, not by deference.

I decline to call this "promising" or "ruled out" for the same reason the
record itself gives: nothing in this cycle produces a realizability claim to
grade, in either direction. Leg (a)'s downgrade to INCONCLUSIVE and its
surviving shape-correlation finding are both, independently confirmed below,
facts about vacuum source-aperture geometry with zero material content. Leg
(b) is the one leg that touches a real lossy material (the article's
`graded_black_shell` rim) and it returns NO VERDICT — its own instrument
failed its own anchor before any realizability-relevant number could be
trusted. "Partial" is the honest label for a cycle that advanced the
program's instrument fidelity substantially while leaving my own seat's
question exactly where Iteration 59 left it.

## 2. Tracing "zero realizability content" through the corrected verdict

**Does downgrading leg (a) from SUPPORT to INCONCLUSIVE change anything about
the realizability disposition? No — and the reason is structural, not
coincidental.** Leg (a)'s entire construction — the source aperture's two
tapered edges, propagated through vacuum via the exact Huygens–Fresnel sum —
uses only `A`, `TAPER`, `λ`, `D_SP` (confirmed against `phase1_derivation.py`
lines 140-141, sourced to `dg065`, not hand-typed). None of these is a
material parameter: `A`/`TAPER`/`D_SP` are source-aperture geometry (a soft
line-current source and its Hann-window amplitude profile, not a physical
object with permittivity), and `λ` is the illumination wavelength. There is
no `ε(ω)`, no reflection coefficient, no absorbing boundary anywhere in leg
(a)'s code path — confirmed directly: `phase1_derivation.py`'s own
Idealization 4/Section 6 states "no absorbing/lossy medium anywhere," and I
verified this by inspection of `leg_a_curve()` (calls `field_and_h` on bare
vacuum propagation only). A verdict correction on WHETHER this vacuum curve's
best-fit period matches a target angle cannot, by construction, create or
destroy a materials claim that was never encoded in the calculation to begin
with. Confirming SUPPORT would have shown only that empty-scene source
geometry is congruent with `P_edge_A`; the actual result (INCONCLUSIVE) shows
that congruence is not established at this window's statistical power. Either
way, "congruent or not" is a fact about a vacuum diffraction integral, not
about any material. My own Iteration-59 "zero realizability content" framing
rule is unmoved by the correction — it was never contingent on which way the
period-match came out.

**Does the shape-correlation finding (`r=0.958`), if it survives, ever bear
on realizability?** I re-derived it independently from the raw committed
files myself (not trusting the fix-docket script's printed output):
`corrcoef` of `derivation_results.json`'s `leg_a.curve` array against
`experiments/069-.../results.json`'s `block_dense.rows[].C_empty_C80` column,
same 31-point grid — `r = 0.9581856926779434`, exact match to the cited
figure. The finding is genuine (I confirmed it, not merely re-read it). But
it is, categorically, a **vacuum/source-geometry fact regardless of
outcome**: it says a boundary-free, homogeneous-medium Huygens integral over
a soft source's own two edges tracks ~92% of the real FDTD curve's variance
in raw shape. That correlation lives entirely upstream of any lossy material
in the scene — it is evidence about how the source's own finite aperture
diffracts light before it ever reaches the `ABSORB`/`PAD` bands or the
article. A perfect r=1.0 confirmation would say "the founding periodicity is
substantially a source-geometry artifact, not a material-boundary echo" —
which is itself informative for my seat (it would argue AGAINST needing any
exotic material to explain `P_edge_A`, the opposite of a realizability
claim), but it still is not a statement about what any material does. I
concur with Red Team's and Phase 3's disposition: this finding is real,
should be logged and credited exactly as filed, and carries zero
realizability content, for the same structural reason leg (a)'s period-match
did.

**Conclusion on this question**: the zero-realizability-content claim, as
stated in `phase1_proposal.md` Section 6 and reaffirmed at Phase 3, is
confirmed correct for everything this cycle actually delivered, independent
of the period-match verdict.

## 3. Does THERMODYNAMICS' ~41× number bear on realizability?

I recomputed it independently rather than trusting the cited figure:
`0.08209591594490195 / 0.002 = 41.048`. This reproduces THERMODYNAMICS'
Phase-2 figure and Red Team's independent confirmation exactly. I also
confirmed the `graded_black_shell` `R≤0.2%` ceiling is a real, previously
ESTABLISHED bench figure (LOGBOOK.md line 282), not invented for this
comparison.

**From my own charter, this number is a diagnostic about the INSTRUMENT, not
about any material property, and for a specific, checkable reason**: leg
(b)'s construction is a two-stage Huygens propagation through an
**opaque hard-edge mask** (`E→0` for `|y−obj_y|≤R_OUT`) — a Kirchhoff
boundary condition, not any model of `graded_black_shell`'s actual
permittivity/loss profile. The mask has no reflectance, transmittance, or
absorption coefficient at all; it simply zeroes the field. So `ptp_b` is not
"the fringe amplitude a real absorber's imperfect reflection would produce"
— it is the diffraction ringing produced by an idealized razor-edge aperture,
a pure geometric-optics quantity. Comparing it to `R≤0.2%` (a real material's
measured reflectance) is comparing two quantities from different physical
constructions that happen to share units of relative field amplitude. The
~41× gap is legitimately read, as the record does, as evidence AGAINST leg
(b)'s two-stage output being a stand-in for "reflection off the real
absorber" (a real reflection-echo bounded near 0.2% could not produce a
signal this large) — but that is a statement about what the CONSTRUCTION
measures, not a statement bounding or characterizing any material. It does
not, and cannot, tell us whether the article-rim construction — once its
Anchor-2 bug is fixed — would ever be "physically meaningful" for a real
material, because the fixed construction, whatever it turns out to be, is
still slated to be a vacuum/geometric diffraction calculation with a hard or
soft aperture stand-in for the disk's edge, not a boundary-value solution of
Maxwell's equations in the graded-loss medium. **The whole two-stage
propagator question is, and will remain after Anchor 2 is fixed, orthogonal
to any real material property** — it is asking whether finite-aperture
diffraction theory correctly predicts a periodicity in the FDTD curve, a
question about geometric optics and instrument validity, never about what
`graded_black_shell` (or any other real absorber) is made of. The 41× number
is a useful hygiene check (Anchor 3, correctly adopted as mandatory) for
catching a future construction that silently DID conflate "diffraction
ringing" with "material reflection," but it is not itself a realizability
bound and should never be reported as one.

## 4. Independent verification performed

- **Shape correlation** (`r=0.958`): recomputed from scratch directly from
  `derivation_results.json`'s `leg_a.curve` and
  `experiments/069-.../results.json`'s `C_empty_C80` column —
  `0.9581856926779434`, exact match, confirming this is not merely restated
  from the fix-docket script's printed output.
- **THERMODYNAMICS' ~41× ratio**: recomputed `0.08209591594490195/0.002 =
  41.048`, and cross-checked the `graded_black_shell` `R≤0.2%` figure is a
  genuine, previously-ESTABLISHED bench constant (LOGBOOK.md line 282), not
  fabricated for this comparison.
- **Geometry/Fraunhofer-regime arithmetic in the parameter table**:
  independently recomputed `A_full²/λ = 1504²/20 = 113,100.8` cells,
  `D_SP/Fraunhofer = 0.1972%`, `√(λ·D_SP) ≈ 66.78` cells, and the article-rim
  Fresnel number `N_F = (2·78)²/(20·93) ≈ 13.08` — all match the proposal's
  cited figures to stated precision.
- **`R_OUT`/`TAPER` sourcing**: confirmed by direct file inspection that
  `experiments/065-t24-absorb-boundary-sweep/design_geometry.py` (the
  `dg065` module cited throughout) defines `TAPER = 40` and `R_OUT = 78`,
  matching the parameter table's citations — not hand-typed.
- Read `phase1_derivation.py`'s `leg_a_curve()`/`leg_b_curve()` directly to
  confirm leg (a) genuinely contains no lossy-medium code path (supports §2
  above) and that leg (b) is genuinely a hard-edge Kirchhoff mask, not any
  encoding of `graded_black_shell`'s actual material law (supports §3).

No discrepancy found anywhere I checked; every load-bearing number in the
record I re-derived reproduces exactly.

## 5. Ranked top-3 candidate directions for Iteration 62+ (MATERIALS vantage)

1. **Fix leg (b)'s Anchor-2 instrument defect, then re-run it as the FIRST
   cycle to actually engage a real material.** This is the only queued item
   that could move my seat's realizability bound at all. Two competing causal
   hypotheses are open (EM's missing obliquity/phase-factor vs. the original
   missing-Rayleigh–Sommerfeld-term guess) — resolve via EM's own named
   discriminating test before re-scoring against `P*`. Once trustworthy,
   mandatorily apply THERMODYNAMICS' Anchor 3 (fringe amplitude vs. the real
   `graded_black_shell R≤0.2%` ceiling) from the start — not as an
   afterthought — so any future amplitude reading is checked for
   physical plausibility as it's produced, not after the fact.
2. **The near-null σ(I) article follow-up** (queued since Iteration 59,
   still not run, now the single most overdue realizability-adjacent item on
   the board): my own prior-cycle flip condition was that SURVIVES-class
   findings had only ever been tested against the strong flagship absorber,
   never a near-null-absorption article — the class that actually
   discriminates whether any of T28's period-matching results depend on
   having a real, loss-bearing material present at all, as opposed to being
   pure source/domain geometry (which this cycle's leg (a) result now makes
   more, not less, plausible for `P_edge_A` specifically).
3. **A genuinely single-integral (not two-stage-composed) Rayleigh–
   Sommerfeld or Kirchhoff double-diffraction treatment of the article rim**,
   once the causal diagnosis above lands — replacing the currently-idealized
   perfectly-opaque hard mask with an amplitude/phase boundary condition that
   actually encodes the disk's real complex reflection coefficient (already
   measured and on record at `R≤0.2%`, `0.10%@600nm`), rather than a binary
   `E→0` mask. This is the first construction that would let a MATERIALS
   verdict — published / plausible / unobtainium — actually be assigned to
   leg (b)'s question, since it would be diffraction theory that is at least
   dimensionally consistent with the real material's known reflectance,
   instead of an idealization an order of magnitude off it by construction.
