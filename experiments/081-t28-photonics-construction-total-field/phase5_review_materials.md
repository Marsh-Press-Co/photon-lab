# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 58 · exp-081

**Seat: MATERIALS & METAMATERIALS.** Fresh sub-agent, no memory of any prior
session. Own the realizability bound (published / plausible /
unobtainium-with-parameters). I filed this cycle's own Phase-2 critique
(blind, in-cycle) flagging that item 1's headline test ran exclusively under
the matched (unobtainium) admittance family. This review independently
re-verifies, from primitives, whether Phase 3/4 actually closed that gap
correctly — not by re-reading the write-up's prose, but by re-deriving the
admittance-family physics myself — and separately audits the phase-divergence
explanation and the ablation-control finding for what they mean for
realizability specifically, per this cycle's task brief.

Read, in order: `PANEL.md`, `AGENTS.md`, `LOGBOOK.md` (RULED OUT R1–R9,
ESTABLISHED, LIVE THREADS in full, T28's complete Iteration 46–57 history),
`PLAN.md`'s Iteration-58 queue, and the complete `experiments/081-.../`
directory (`phase1_proposal.md`, `photonics_construction.py`,
`phase1_results.json`, `_output.txt`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`/
`.json`, `NOTES.md`). No `phase5_review_*`/`phase5_redteam_audit.md` file
from this cycle was read (none exist yet / correctly excluded).

---

## 0. Independent verification performed (not re-argued from the write-up)

I wrote a from-scratch script
(`/tmp/.../scratchpad/materials_verify_081.py`) that:

1. **Re-typed both admittance-family reflection formulas independently**
   (TE-mode transfer-matrix recursion, `Zi = μ_r,i / sqrt(nᵢ²−sin²θ)` with
   `μ_r=nᵢ` for matched, `μ_r=1` for realizable) — not copied from
   `y_wall_aperture_sum.py::reflection_coefficient_vec` or
   `validity_precheck.py::reflection_coefficient_vec_realizable`, though the
   result must (and does) agree with them.
2. **Recomputed the phase-divergence figure** (matched vs realizable
   `arg(r)`) at ABSORB=40 over both the item-1 range `[48°,54°]` and the
   exp-080 part(b) precedent range `[5°,15°]`, at multiple grid densities.
3. **Recomputed the full realizable-vs-matched period rescore** for all
   three pair-deltas, reusing only already-gated aperture/geometry
   primitives (`dg065.CONFIGS`, `ywas.build_aperture_grid`/
   `aperture_amplitude`/`source_driven_phase`/`dist_image_cells`/`_trapz`/
   `K600`/`free_period_with_widening`) and this cycle's own committed
   `e_direct_curve` (already re-verified bit-exact three times before this),
   but with **my own** admittance function, not `d80`'s.

**Result: bit-exact-to-displayed-precision agreement with every number in
`phase1_results.json`/`phase4_results.json`/`phase2_redteam_audit.md`** —
matched periods `1.8571°`/`2.0301°`/`2.0150°`, realizable periods
`1.8647°`/`2.0301°`/`2.0226°`, shifts `0.007519°`/`0.0°`/`0.007519°`
(reproducing the exact `0.0075188°` figure that triggered the Phase-4
"technically not confirmed, ≤0.0075° threshold" disclosure — a genuine,
reproducible number, not a script-specific artifact), verdicts
INCONCLUSIVE/INCONCLUSIVE/SUPPORT unchanged, Combined Verdict NEITHER under
both families. This is now the **fifth** independent computation of this
result (Phase 1's original run, Red Team's Phase-2 scratch script, the
Phase-3-committed `item1_admittance_family_rescore()`, its own Phase-4
reproduction check, and this review) — as solid as this program's own R4
discipline requires for a claim this consequential.

---

## 1. Did Phase 3/4 correctly fix the admittance-family gap I raised at Phase 2? **Yes — independently re-derived, not merely trusted.**

My own Phase-2 critique this cycle was correct that item 1's Phase-1 build
used the matched (unobtainium) admittance exclusively, and that this was
exactly the shape of gap that flipped exp-080's part(b) from INCONCLUSIVE
(matched) to REFUTE (realizable). Phase 3/4 closed it correctly:

- The fix is **not** a re-argued claim — Red Team's Phase-2 audit,
  Phase 3's committed `item1_admittance_family_rescore()`, and Phase 4's
  fresh re-run all independently compute the realizable rescore, and I have
  now added a fifth, genuinely independent computation (my own admittance
  formula, §0) that agrees to the last reported digit.
- The Combined Verdict, all three per-pair verdicts, and the
  T21-proximity qualitative pattern are **genuinely unchanged** between
  admittance families (max shift `0.0075°`, three orders of magnitude below
  the `rel_dev` bands' own `0.30`/`1.00` gates) — this is not a borderline
  or asserted result, it reproduces from first principles.
- **The one honest wrinkle — the frozen `"≤0.0075°"` prediction technically
  missing by `1.9×10⁻⁵°`** — is correctly characterized as a
  rounding-precision artifact (the bound was copied from a 4-decimal-rounded
  table) rather than a physics discrepancy: my own independent
  from-scratch computation reproduces the identical `0.0075188°` figure, so
  the near-miss is a real, reproducible number, not a fluke of one script's
  floating-point path, exactly as `phase4_results.md` states.

**MATERIALS' own charter conclusion, sharpened by this independent
re-derivation, not merely restated**: this specific ABSORB=40, `[48°,54°]`
result is genuinely admittance-family-independent — a rare case in this
sub-thread's own record where the realizability question (matched vs.
realizable) turns out NOT to be load-bearing. That is itself worth stating
plainly, since every other admittance-family check in this program's T28
history (exp-080 part(b), most sharply) found the opposite.

---

## 2. Is the "8.4–10.6° vs 54–83.6°" phase-divergence explanation sound physics, or hand-waving? **Sound, causally-verified physics — with one genuine caveat about how far it generalizes.**

I independently recomputed the phase divergence at ABSORB=40 from my own
admittance formula: `[48°,54°]` gives `8.36°–10.55°` (matches Red Team's
cited `8.4–10.6°` almost exactly); `[5°,15°]` at a coarse `n=10` grid gives
`54.01°–83.56°` (matches Red Team's cited figure exactly), but the true
maximum over a finer grid grows to `≈89.1°` — independently confirming
`phase4_results.md`'s own disclosed grid-density discrepancy, not merely
trusting its prose.

**I went one step further than the committed record and checked *why* —
the causal mechanism, not just the numbers**: at `[5°,15°]` (near-normal
incidence into the ABSORB=40 graded-loss boundary), `|r|` is tiny
(`8.8×10⁻⁵`–`1.6×10⁻⁴` matched, `2×10⁻⁷`–`1.6×10⁻⁴` realizable) — this
depth/angle combination is near-total absorption. At `[48°,54°]`, `|r|` is
two to three orders of magnitude larger (`0.016`–`0.043`). **A complex
number's phase becomes ill-conditioned as its magnitude approaches zero** —
a small, physically-insignificant perturbation to a near-zero reflection
coefficient (exactly what switching admittance families is, at fixed
`|n|`-profile) produces an arbitrarily large swing in `arg(r)`, while the
same perturbation applied to a reflection coefficient of a few percent
produces a correspondingly modest phase swing. This is a genuine,
first-principles EM/MATERIALS mechanism — the near-total-absorption
condition at near-normal incidence is itself a real, verifiable material
fact about this graded-loss profile — not an unexplained empirical
coincidence dressed up as an explanation.

**Caveat, not raised anywhere in the committed record**: I checked all four
ABSORB depths at both ranges (§0's script, item 5/6). The
"order-of-magnitude-smaller divergence at the more-grazing range" pattern
holds specifically and most dramatically for **ABSORB=40** — the depth
every one of this cycle's three scored pairs actually uses — but does not
generalize as a universal law across ABSORB depths: ABSORB=70's divergence
at `[48°,54°]` (`0.15°–8.1°`) is comparable in *scale* to its own divergence
at `[5°,15°]` (`0.01°–5.3°`), i.e. no dramatic gap at that depth either way,
because ABSORB=70 never drives `|r|` as close to zero at near-normal
incidence as ABSORB=40 does. **The explanation is correct and
independently verified for the comparison this cycle actually needed (why
item 1's own result differs from exp-080 part(b)'s, both at ABSORB=40) — it
is not, and should not be read as, a general "grazing angles are always
admittance-family-robust" claim** across this whole construction's ABSORB
range. This distinction is absent from `NOTES.md`/`phase4_results.md`,
which state the comparison correctly but do not flag that it is
depth-specific. Non-blocking (nothing in this cycle's own record claims the
broader generalization), but worth stating explicitly for Iteration 59, since
a future cycle citing "grazing angles are admittance-robust" as a general
T28 finding would be overclaiming what this cycle actually showed.

---

## 3. Does "the construction needs no wall reflectance for its one SUPPORT" tell us anything new about realizability, or is it purely geometric/EM, outside my charter?

**It is primarily a geometric/kinematic finding (correctly owned by
PHOTONICS/QUANTUM's ablation-control proposal and Red Team's execution of
it) — but it has a genuine, non-trivial MATERIALS corollary that the
committed record does not state explicitly, and that corollary is stronger
than the admittance-family check in §1 above.**

The ablation control replaces `r(90°−θ_beam;ABSORB)` with the constant `1`
— not "zero reflectance," but a perfect, phase-flat, angle-flat,
ABSORB-depth-flat reflector. No causal, passive medium can realize `r≡1`
identically across a 6° angular sweep and all four `ABSORB` depths — it is
a pure null/control value, not a candidate material at all (unlike the
matched-vs-realizable comparison in §1, which compares two *admittance
families*, one unobtainium and one ordinary-dielectric, but both at least
*mathematically* consistent optical response functions of angle and depth).

That the `C80−C40` SUPPORT survives this ablation almost unchanged
(`rel_dev` `0.2937` ablated vs. `0.2910` real) means: **for this pair, the
recovered period carries no information about the wall's material identity
whatsoever — not matched-vs-realizable (§1, already shown non-determining),
not real-vs-trivial-non-physical.** Combined, these two independent checks
this cycle now supports (§1's own admittance-family rescore, and the
ablation control Red Team ran in response to PHOTONICS'/QUANTUM's Phase-2
critiques) jointly establish something my own charter should say plainly
and the committed record currently does not: **no realizability question is
even in play for `C80−C40`'s SUPPORT** — it is not that a real material is
ruled out in favor of an unobtainium one, or vice versa; it is that *no*
material response, real or fictional, drives this particular signal. This
is a stronger, more complete disposition than "REFUTE-leaning" alone
conveys, and belongs explicitly in this cycle's realizability bookkeeping,
not filed as purely outside MATERIALS' charter.

**The other side of the same control is equally informative for
MATERIALS**: `PAIR_ABSORB40`'s ablated signal is *exactly* degenerate
(`ss_tot=0.0`) — meaning that pair's own (non-matching, INCONCLUSIVE)
period genuinely requires *some* wall optical response to exist at all. For
that pair, unlike `C80−C40`, the admittance-family question (§1) is a
live, meaningful question about a real signal component — it merely
happens, per §1's own result, not to move the outcome at ABSORB=40's
specific angle regime. Both halves of this pair-specific finding are
realizability-relevant, in opposite directions, and should be read
together, not just the `C80−C40` half `NOTES.md` foregrounds.

---

## 4. A genuine MATERIALS-charter finding this review adds: the x-wall realizable-admittance refit has silently dropped off the tracked board

Not raised by this cycle's own Phase 1–4 record, and worth surfacing now.
`LOGBOOK.md`'s Iteration 55/56/57 rankings each named, in nearly identical
language, **"the still-unexecuted x-wall realizable-admittance refit — the
single oldest-deferred MATERIALS item on the whole board"** (three
consecutive cycles, 78→80). I checked `experiments/080-.../
phase5_redteam_audit.md` §6 — the document that produced this exact
Iteration-58 queue exp-081 executed — and it contains **zero** mention of
this item anywhere (confirmed by direct grep, not just a read-through); the
Tier-0/1/2/3 list that survived into `PLAN.md`'s active Iteration-58 queue
runs items 1 (total-field construction), 2 (gate re-run), 3 (energy
budget), 4 (MATERIALS docstring hygiene, this cycle's own item 4), 5–7
(wavelength leg, broadband spectroscopy, 750nm x-wall two-wall spot-check —
a *different* item, testing wavelength generality, not admittance family),
8 (PAD-loaded real article), 9–10 (governance). The x-wall
realizable-admittance refit is not among them, and no ruling anywhere
retires it explicitly.

This is not this cycle's own defect (exp-081's own scope was exactly the
four Tier-0 items the queue handed it, correctly executed) and I am not
asserting it is outcome-determining or Checkpoint-4-worthy — the x-wall
single/two-wall coherent-echo models were already REFUTEd by large margins
under the matched admittance (exp-075: period ~4.3–15× off; exp-077:
Test B `r²=0.0001`), margins wide enough that an admittance-family
±2×-scale shift is unlikely to flip either verdict, unlike the y-wall's own
near-boundary case this cycle examined. But a named, three-times-repeated
"oldest-deferred MATERIALS item on the board" disappearing from a
reconciled ranking with no stated disposition is exactly the kind of
silent-drop this program's own R8/R9 discipline exists to catch elsewhere
in the record — it should not happen to my own seat's own item without
comment either. **Recommend**: either execute it (cheap — reuses
`d80.reflection_coefficient_vec_realizable` against the already-built
x-wall model) or explicitly retire it with a stated reason (e.g., "REFUTE
margins too wide for an admittance-family shift to matter") — either is
fine, but silence is not.

---

## VERDICT

**PARTIAL** (matching this sub-thread's own established verdict pattern for
a genuinely informative but non-closing cycle — not RULED OUT, not
PROMISING).

This cycle delivers, independently re-confirmed here from primitives, the
actually-decisive test this nine-cycle T28 y-wall sub-thread has been
missing (total field, real-data free-period fit) — and, once Phase 2's
raised gaps (admittance family, ablation control, phase-convention
sensitivity) are actually run rather than merely argued about, the result
sharpens toward REFUTE-leaning on solid ground: the lone SUPPORT is now
*proven*, not argued, to need no wall reflectance and no admittance-family
commitment at all (§§1,3 above, independently re-verified). This is a real,
cumulative narrowing of the plane-wave/global-steering coherent-echo class
— a third independent negative line of evidence, joining exp-078's and
exp-079's own structural forecloses. It is not RULED OUT because it remains
a single result at one wavelength (600nm), on an empty scene, on the
`90°−θ_beam` construction specifically — the wavelength-generality leg and
the PAD-loaded real-article check (both six consecutive cycles deferred as
of this iteration) are the natural, still-unrun tests of whether this
finding generalizes at all. Checkpoint criterion 2 (mechanism-class
boundary): **not yet ripe**, for the same reason — concur with Phase 3/4's
own ruling, independently re-reasoned, not merely adopted.

---

## Ranked top-3 candidate directions for Iteration 59 (MATERIALS' own ranking)

1. **The real 750/450nm wavelength-generality leg (deferred SIX consecutive
   cycles, 076–081).** From my own charter specifically: every admittance
   family used in this program is a fixed-frequency (600nm) construct; a
   real coating's index profile is inherently dispersive, and this cycle's
   own §1/§2 findings (admittance-family-independence, and the
   ABSORB=40-specific phase-conditioning story) have never been checked at
   a second wavelength. This is the single most information-dense
   still-unrun test on the board, for my discipline as much as for
   PHOTONICS'/VISION's own wavelength-realism metric — six consecutive
   deferrals without this cycle's own explicit reason is no longer
   defensible on inertia alone.
2. **The PAD-loaded real-article check (deferred SIX consecutive cycles,
   076–081).** Every congruent-series config to date is an empty scene;
   whether the `PAD`-sensitivity axis — and, by extension, whether *any* of
   this nine-cycle sub-thread's periodicity has ever had a real absorbing
   material anywhere in the loop rather than free-space domain-boundary
   geometry alone — survives a loaded scene is the only queued item that
   tests real-world relevance at all, a fundamentally different question
   than another period-matching exercise can answer.
3. **Restore or explicitly retire the x-wall realizable-admittance refit**
   (§4 above) — cheap (reuses already-gated `d80`/exp-075/077 machinery),
   and the only item on this list that is purely a docket-hygiene fix
   rather than new physics: either run it and close MATERIALS' own
   three-cycle-old oldest-deferred item, or state explicitly why its REFUTE
   margins make it safe to retire, so it does not continue to silently
   vanish from future rankings.

Also worth carrying forward, not independently ranked above items 1–3:
EM's own named, cheap, disclosed-but-not-yet-run FDTD phase-convention
extension (`r` vs `conj(r)`, 2–3 angles inside `[47.5°,54.5°]`, mirroring
`phase5_redteam_phase_convention_check.py`'s own precedent) — this cycle
showed it is not outcome-determining for the Combined Verdict, but the true
convention at this new, more-grazing angle range remains genuinely open and
is EM's own charter to prioritize, not mine to rank above the two
six-cycle-deferred items above.

No RULED-OUT item (R1–R9) re-proposed anywhere in this review.
