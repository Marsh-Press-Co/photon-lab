# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 60 · exp-083
## Verifying the corrected record holds, and a charter-native proposal for what a genuine near-field derivation of `P_edge_A` would require

**Seat: PHOTONICS.** Fresh sub-agent, zero memory of any prior session.
Charter: surface interaction, absorption spectra, angular dependence,
scattering cross-sections — is the proposal's optical response coherent as
stated, across wavelength and angle? Read, in order: `PANEL.md`, `AGENTS.md`,
`LOGBOOK.md` (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS in full, T28's
complete Iteration 46–59 history), `PLAN.md`'s Iteration-60 queue, and the
complete `experiments/083-.../` record — `phase1_proposal.md`, `NOTES.md`,
`run.py`, `results.json` (spot-checked), `run_output.txt`,
`null_permutation_control.json`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`. Blind to any Phase-5 review
this cycle, per instruction.

**Independent verification performed, not taken on faith.** Pulled
`results.json::primary_period_discriminator` and `secondary_correlation`
directly: `P*=2.9473684210526314°`, `R²=0.858195125110302`, branch
`B_ARTICLE_EDGE...`, `r=0.39494101490407624, p=0.02806` — bit-exact against
every citation in `NOTES.md`/`phase1_proposal.md`. Confirmed
`null_permutation_control.json`'s two entries (`delta_scene`:
`p=0.0, null_max=0.6324`; `em_pair`: `p=0.00185, null_max=0.5599`) match the
prose exactly, including the fact that the EM-pair observed value does *not*
exceed its own null max (only the stronger, correctly-stated `p=0.00185`
claim is actually made — no loose "exceeds the null" language applies to
that series). Independently recomputed PHOTONICS' predecessor's own
back-of-envelope estimate from the raw geometry cited in the record
(`R_OUT=78` cells, `λ=20` cells at 600nm/cpl20, `lever=93` cells,
`θ=39°`): far-field `Δθ = λ/(2·R_OUT·cosθ) = 20/(156·cos39°) = 9.4520°`
(ratio to `P_edge_A=2.8421°` = 3.326×) and Fresnel number
`N_F = (2R_OUT)²/(λ·lever) = 156²/(20·93) = 13.08` — both reproduce Red
Team's own §0c/§0d figures exactly. Confirmed the four record-preconditions
(`reproduction_precondition.max_dev=0.0`,
`settling_precondition.rel_dev=9.8127×10⁻⁵`) directly from `results.json`.

---

## 1. Verdict on the corrected record itself (the task's own primary question)

**Yes — the causal-label downgrade is stated clearly everywhere it matters,
and consistently.** I grepped both `NOTES.md` and `phase1_proposal.md` for
every remaining use of "confirmed"/"resolved" near the article-edge or
two-tone claims; none survive uncorrected. The headline in `NOTES.md`'s own
"Result" section reads exactly as Red Team's Attack 1 mandated: *"matches
T28's own long-standing, unexplained `P_edge_A` family — period-family
membership, statistically decisive and null-controlled... NOT yet
demonstrated to be article-intrinsic."* The same correction appears in
`phase1_proposal.md`'s "PHASE 1 RESULTS" primary-discriminator section, its
"Combined self-score," and `NOTES.md`'s "Learned" item 1. Nowhere did I find
a residual "ARTICLE-EDGE DIFFRACTION, confirmed" sentence that escaped the
fix. The 3.3× far-field miss and the `N_F≈13` near-field caveat are both
present at every place the causal label is asserted, not just once in an
appendix.

**Yes — the two-tone reversal is correctly presented as open, not
resolved, and consistently so.** Both `NOTES.md`'s "Result"/"Learned" and
`phase1_proposal.md`'s "PHASE 2/3 UPDATE" section state, side by side: the
naive Freedman–Lane full-permutation reading (`p<0.001`, three baselines,
corroborated `p=0.00018` in EM's field companion) *and* the order-preserving
circular-shift reversal (`p=0.581` primary, `p=0.097` EM companion), name
the lag-1 autocorrelation (`r≈0.93–0.95`) as the reason neither reading is
trusted as final, and explicitly queue a pre-registered null-calibration
test for Iteration 61 rather than adjudicating a winner. This is the correct
disposition — I checked for a stray "genuine partial admixture" sentence
inherited from QUANTUM's or EM's own Phase-2 language and found none; every
instance is either struck or immediately paired with the reversal.

Both corrections are, in substance, real physics-adjacent findings and not
mere prose hygiene: they change what a future cycle is licensed to build on
top of (a period-family fact, not a mechanism; a real methodological caution
about permutation nulls on autocorrelated small-n angular sweeps, not a
second confirmed physical channel).

---

## 2. From this seat's own charter: what the Fresnel-regime finding actually implies, and what it doesn't

Red Team's own `N_F≈13` finding is correct and load-bearing, but I want to
sharpen what it does and does not license, because "far-field formula wrong,
therefore inconclusive" is where the record currently stops, and that
understates how much the near-field regime actually constrains the story.

**A genuinely new observation this review adds: `P_edge_A` was established
on a scene with no article in it at all.** `P_edge_A=2.8421°` is
`experiments/069-.../results.json::scored.p3.p_star_deg` — the *empty-scene*
`C80−C40` `ABSORB`-boundary-depth delta from Block MINI (LOGBOOK Iteration
46), a measurement in which no absorbing article, and therefore no article
rim, was present in the domain at all. If Branch B's plain-language name
("article-edge diffraction") were literally true — a *new* physical channel
introduced by the article's own rim — it would need to be a striking
coincidence that this brand-new channel's period lands, to 3.7% relative
deviation, on a number that a completely different experiment, with no
article present, already produced from an unrelated geometric axis
(`ABSORB` depth, not article radius). That is not impossible, but it is the
less economical explanation. The "inherited pre-existing artifact" reading
Red Team's audit already favors is not merely the more cautious of two
symmetric options — the empty-scene provenance of `P_edge_A` is itself
independent charter-relevant evidence *against* a genuine article-rim
origin, on top of (not merely alongside) the 3.3× far-field miss. This
belongs explicitly in the record's own reasoning for why MATERIALS'
article-radius discriminator's "period stays pinned" outcome should be
treated as the directionally-favored prediction, not a coin flip, when that
test is pre-registered at Iteration 61.

**What the Fresnel-regime finding does NOT do**: it does not tell you what
the *correct* calculation is — only that a specific wrong one was used.
Every prior T28 cycle that modeled a domain boundary (the x-wall, the
y-wall, PHOTONICS' own total-field construction, exp-075/077/078/079/080/
081) treated it as a **reflector**: an image source plus a reflection
coefficient `r(θ)`, evaluated at a rigorously-derived incidence angle. That
machinery is a *near-field-correct specular-reflection* model — it is not a
diffraction-integral model. None of those nine-plus cycles, as far as this
record shows, ever modeled a boundary or an edge as a **diffractor** in the
Fresnel/Kirchhoff sense (a secondary point-source with the correct quadratic
near-field phase, not the linear far-field phase the naive `Δθ=λ/(Δy·cosθ)`
formula assumes). That is a genuinely different, still-untried mechanism
class for this whole sub-thread, and it is the class this cycle's own two
candidate stories (article rim, domain echo) both actually need if either is
to be *derived* rather than *pattern-matched*.

### 2.1 A concrete, zero-FDTD, pre-registerable construction for Iteration 61

Build a genuine near-field edge-diffraction sum — not the linear two-point
far-field formula, not a specular-reflection image-source model — reusing
this sub-thread's own already-validated per-point exact-geometry machinery
(`y_wall_aperture_sum.py`'s `theta_local(y_s)`-style rigorous angle/distance
calculation, proven sound at exp-079/080) but retargeted at a genuine
diffraction integral:

1. For each candidate edge (a point or line singularity — e.g. the article's
   own rim points `(obj_x, obj_y±R_OUT)`, or, see below, a domain/source
   edge on the empty scene), compute the **exact** path length from the
   effective source through the edge to the observer at each swept angle
   `θ` — no `sinθ`/paraxial linearization, the same discipline EM's own
   validity pre-check (exp-080) demanded before trusting any far-field
   substitution here.
2. Weight each edge's contribution with the standard Fresnel/Huygens
   diffracted-wave amplitude (`∝1/√r`) and the *quadratic* near-field phase
   term (`kr ≈ k(r₀ + y²/2r₀ + ...)`), not the linear term the naive
   `Δθ=λ/(Δy cosθ)` formula silently assumes — the correct treatment at
   `N_F≈13`, where the quadratic term is not negligible.
3. Coherently sum the edge contributions (a two-point Fresnel construction
   for a first pass; the full-aperture Kirchhoff integral, mirroring
   exp-079's own non-edge-reduced generalization, as the natural follow-up
   if the two-point version is inconclusive).
4. Pre-register the predicted `P*` (and, since Fresnel fringes are not
   generally uniformly spaced, a predicted *local* period/shape over
   `[36°,42°]` specifically, not just a single number) BEFORE comparing to
   `delta_scene`.

**Run this FIRST on the empty-scene `C80−C40` geometry — where `P_edge_A`
actually originates and no article is required — not only on the article's
own rim.** This is the test nine-plus prior mechanism-search cycles never
ran: every one of them modeled a boundary as a reflector. If a genuine
Fresnel edge-diffraction treatment of some already-existing domain or source
edge (the `ABSORB`/`PAD` boundary's own edge, or the source aperture's own
hard edge — both present with zero article) reproduces `2.8421°` from
geometry alone, that would be the first true first-principles derivation of
T28's founding periodicity in this program's history, and it would settle
this cycle's own causal question as a corollary, for free: the article-loaded
channel would simply be inheriting an already-explained artifact, not a new
one. Only as a second, cheap follow-up should the identical construction be
re-run against the article's own rim coordinates (MATERIALS' own physical
substrate, but with a first-principles predicted period this time, not just
an empirical direction-of-shift test) — turning MATERIALS' `R_OUT` sweep
from a qualitative pinned-vs-tracking test into a quantitative
prediction-vs-measurement one.

This is real charter work, not a restatement of Red Team's caution: it names
the specific mechanism class (Fresnel/Kirchhoff edge diffraction) this
sub-thread has never tried, explains concretely why the near-field finding
makes it the right next tool (not just a reason for caution about the wrong
one), and targets it first at the place `P_edge_A` actually came from.

---

## 3. Two smaller record-fidelity notes (not outcome-determining)

- `NOTES.md`'s own "Next" section (item 3) cites `phase5_review_photonics.md
  §2` as an existing document — that citation resolves to *this* file,
  written after `NOTES.md` was finalized. Not a defect in this cycle's own
  physics (the underlying idea — a coherent rim-edge construction — was
  already named at Phase 2 by this seat's own predecessor and restated at
  Phase 2 this cycle), but a forward citation to a not-yet-written document
  should not be treated as an already-discharged reference by any later
  reader; flagging so Iteration 61 does not assume this section pre-existed
  in a form more concrete than the Phase-2 sketch it actually was.
- EM's own field-difference companion (§4b) is a genuinely valuable,
  charter-adjacent instrument (a linear, reciprocity-clean channel free of
  the Weber-contrast cross-term) and its independent corroboration of Branch
  B (`P*=2.5865°`, own null-controlled `p=0.00185`) is real evidence the
  period-family finding is not an artifact of the nonlinear contrast metric
  specifically — worth keeping in mind that any future near-field
  diffraction construction (§2.1) should be scored against *both*
  `delta_scene` and `ΔΔE_obj_article_PAD`, not just the former, exactly as
  this cycle's own primary test was.

---

## Verdict: **PARTIAL**

The period-family question is genuinely, decisively resolved for the first
time in this nine-cycle-plus sub-thread, doubly instrument-corroborated and
null-controlled — real, charter-relevant progress on "is the optical
response coherent across angle," answered with statistical confidence for
the first time. But the causal question — what actually produces this
angular structure — remains open, and this review's own empty-scene-
provenance point sharpens rather than resolves the ambiguity: it now leans
the record's own prior toward "inherited pre-existing artifact" over
"genuine article-rim mechanism," without yet proving either. The two-tone
admixture question is correctly left open, not settled. T1: N/A throughout
— no constraint-3 claim is made or implied anywhere in this cycle's record,
so this cannot be scored PROMISING against the phenomenon program; it is not
RULED OUT either, since nothing here forecloses a mechanism — real,
verified, null-controlled statistical progress, with the causal
attribution and the admixture question both correctly and honestly left for
Iteration 61. PARTIAL matches Phase 3's own self-assessment, and I concur
with it from this seat's own independent read.

## Ranked top-3 candidate directions for Iteration 61

1. **A genuine near-field/Fresnel edge-diffraction derivation (zero-FDTD,
   desk-only), applied FIRST to the empty-scene `C80−C40`/domain-or-source-
   edge geometry where `P_edge_A` actually originates, then to the
   article's own rim as a second, cheap comparison.** (§2.1, this review.)
   The single test that could finally derive T28's founding periodicity
   from first principles — something nine-plus prior cycles, all modeling
   boundaries as reflectors rather than diffractors, have never attempted —
   and settles this cycle's own causal-label question as a corollary if it
   succeeds on the empty scene.
2. **MATERIALS' article-radius (`R_OUT`) discriminator**, endorsed as the
   record's own correctly-identified top empirical item — but pre-register
   its directional prediction using this review's own empty-scene-
   provenance argument (period-pinned is the charter-favored prior, not a
   50/50 split), and, if item 1 is built first, score the sweep against
   item 1's own quantitative `P*(R_OUT)` prediction rather than a bare
   qualitative direction.
3. **A properly pre-registered null-calibration test for the two-tone
   admixture question** (Red Team's Attack 2, R6-Iteration-50-addendum
   standard) — not primarily this seat's own charter territory, but the
   open item most likely to interact with item 1's own results: if a
   genuine Fresnel construction predicts a mixed-tone (superposition)
   signal rather than a single clean period, the two-tone question and the
   causal-derivation question become the same test, and should be designed
   together rather than sequentially.
