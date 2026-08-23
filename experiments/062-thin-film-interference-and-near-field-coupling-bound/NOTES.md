# exp-062 — Thin-Film Interference and Near-Field-Coupling Bounds for the
# MP-3/MP-4 Mechanism-Class Ambiguity

**Panel Iteration 39.** Lead: ELECTROMAGNETISM, by rotation (the slot
deferred since Iteration 36's LOCK chain; resumes here, no new lock fired
at Iteration 38's close). T1 escape route: NONE — zero constraint-1/2/3/4
metric scored this cycle. Full five-phase panel cycle: Phase 1 proposal →
five blind Phase-2 critiques (all support-with-changes) + Red Team audit
(PROCEED-WITH-MANDATORY-FIXES; **Checkpoint criterion 4 FIRES** — see
below) → this Phase-3 synthesis, predictions frozen before Phase 4 →
Phase 4 (WebSearch continuation of exp-061's own search) → Phase 5. Full
process record: `phase1_proposal.md`, `phase2_critique_{photonics,
materials,thermodynamics,quantum,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md` (this cycle's Director synthesis, all in this
directory).

**CHECKPOINT (Iteration 39, criterion 4 — program-integrity drift).** Red
Team's Phase-2 audit ruled the `exp061-t18-evidentiary-tier-propagation`
registry entry's own hardened tripwire (Iteration 38 close: "any further
gap ... discovered at Iteration 39 or later, auto-fires criterion 4, no
further deliberation") fires: VISION SCIENCE's blind critique found that
entry's `required_sites`/`candidate_globs` could not discover this
cycle's own forthcoming NOTES.md/phase4_results.md, despite this cycle's
own Phase-1 proposal already tripping the entry's `trigger_terms`. Per
the tripwire's own text (no phase-based safe harbor, unlike its sibling
`exp060-sigma-flat-*` tripwire) this fires on discovery alone — full
argument in `phase2_redteam_audit.md` §3, accepted without override in
`phase3_synthesis.md` §2. Per unbroken precedent (Iterations 17/36/37/38)
this is a **notification, not a pause**: the registry is widened same-
shift (below), Marsh is convened (this entry + LOGBOOK.md + SESSION_LOG.md
+ PLAN.md), and this cycle proceeds unblocked.

---

## Hypothesis

exp-061 (Iteration 38) closed `REALIZABILITY_MEMO.md` Entry 2's
absorptivity question — `graded_black_shell`'s corrected absorption rate
(α_true≈5.74×10⁴ cm⁻¹, e-fold≈174nm) is UNOBTANIUM-WITH-PARAMETERS,
overdetermined by a 70–350× thickness gap against real CNT-forest/
Vantablack-class coatings. One numeric loose end survived to Iteration 39:
an out-of-class organic LCD black-matrix patent film (`OD≥3.0` at `≤1µm`)
numerically approaches α_true (within ~1.2×) under an unchecked single-pass
Beer–Lambert conversion. Two electromagnetic questions about that number
were never asked: (1) is the reported optical density reflectance-based
(round-trip through a backed film) or transmission-based (single pass) —
a factor-of-~2 geometric ambiguity, not a coherence effect; and (2) is the
figure's apparent blackness bulk absorption at all, or could it be a
tuned thin-film interference effect (a Salisbury-screen-type absorber),
which would make the OD-to-α conversion category-wrong rather than merely
imprecise? A companion question, replacing QUANTUM OPTICS' own Iteration-
38 vocabulary-presence fallback (downgraded CONFIRMED→OPEN): do published
VACNT inter-tube pitch/diameter figures put real CNT forests inside the
classical near-field-coupling regime (`gap ≲ λ/2π`), where a Bruggeman/
effective-medium homogenization is at minimum an incomplete description?

**Hypothesis, stated for falsification:** (a) the R-vs-T ambiguity is a
~2× effect, not an order of magnitude, and does not by itself flip
whether the black-matrix candidate sits within "2× of target"; (b)
genuine coherent multi-beam interference is a small, passivity-bounded
correction (≲10%) in the "optically thick" reading, but the resonant-
absorber alternative cannot be ruled out from available evidence and, if
true, would only reinforce (not threaten) MP-4's existing exclusion of
this candidate; (c) real CNT-forest geometries sit inside the classical
near-field-coupling regime, meaning a bulk-homogenization reading of
their blackness is at minimum incomplete — though this does not by
itself say which direction (enhancing or suppressing) that incompleteness
biases the cited α figures.

---

## Setup

### Item A — the R-vs-T / substrate-interference closed-form analysis

**Model.** Single absorbing layer (`n₂=n₂′+in₂″`, thickness `d`) between
air (`n₁=1`) and a substrate/backing `n₃`, normal incidence, standard Airy
stack:

```
r₁₂ = (n₁−n₂)/(n₁+n₂)          r₂₃ = (n₂−n₃)/(n₂+n₃)
β    = (2π/λ)·n₂·d = φ + iγ      φ = 2π n₂′ d/λ,  γ = 2π n₂″ d/λ
r_stack = (r₁₂ + r₂₃·e^{2iβ}) / (1 + r₁₂ r₂₃ e^{2iβ})       R_stack = |r_stack|²
```

Single-pass power optical depth `τ ≡ 2γ = α d` (this bench's established
`Im(n)`-weighted convention, the same one Red Team's exp-061 Phase-2
adjudication used for `τ_true`).

**R-vs-T geometric factor** (dominant, not interference): a reflectance-
based OD (light traverses the layer twice, in–reflect–out) implies HALF
the single-pass τ a transmission-based OD would; a T-based OD needs no
correction.

```
OD=3.0:  τ_T = OD·ln10 = 6.9078  ->  α_T = 6.908×10⁴ cm⁻¹  (ratio to α_true: 1.20×)
         τ_R = τ_T/2   = 3.4539  ->  α_R = 3.454×10⁴ cm⁻¹  (ratio to α_true: 0.60×)
```

**Coherent-interference bound** (small in both readings, passivity-
derived): expanding `r_stack` for `|r₂₃|e^{-τ}≪1` and using `|r₁₂|,
|r₂₃|≤1` (any passive interface):

```
|ΔR/R₁₂| ≲ 2e^{-τ}   ->   ≤0.20% (T-based, τ=6.91)   ≤6.3% (R-based, τ=3.45)
```

**Resonant-absorber alternative & discriminator.** The bound above assumes
the "optically thick" (τ≳3) regime. An optically thin layer on a
reflective backing, at the right thickness/impedance, can absorb nearly
100% via destructive interference alone (Salisbury-screen/critical
coupling) — in that regime a near-zero R implies a tuned resonance, not a
large bulk α, and the OD-to-α conversion is category-wrong (an upper
bound, not a point estimate). Resonant absorbers are inherently
narrowband (their own interference condition ties them to one design
λ); a genuinely bulk-absorbing coating has no such constraint.
**[Mandatory fix 2, Red Team docket item 2]** The interference condition's
own round-trip phase is angle-dependent (`2β=2(2π/λ)n₂d·cosθ_t`) — an
angle-*integrated* (hemispherical/integrating-sphere) OD measurement can
SMEAR a genuinely narrowband resonant dip into an apparently broadband
reading, the OPPOSITE of what a naive "broadband ⇒ not resonant" reading
would conclude. The discriminator below is therefore conditioned
explicitly on measurement geometry, per the amended falsification
condition (§ Predictions, EM-3).

### Item B — the near-field-coupling numeric threshold (replaces QUANTUM's
vocabulary-presence fallback)

**Criterion**: for a representative CNT packing geometry, gap `g = p − D`
(pitch minus diameter) vs. the reactive near-field radius `λ/2π`:

```
ratio = g / (λ/2π)
```

`ratio ≪ 1` ⇒ neighboring tubes sit inside each other's reactive near
field at visible λ — a bulk-homogenization/Beer–Lambert reading is at
minimum incomplete. `ratio ≳ 1` ⇒ ordinary independent-scatterer
(radiative-coupling) behavior; the effective-medium convention is not
hiding anything this test would catch.

**Illustrative placeholder** (MWCNT `D=20nm`, areal packing `f=5%`, square
lattice `f=(π/4)(D/p)² ⇒ p=D√(π/4f)`, λ=550nm):

```
p=79.27nm  gap=59.27nm  λ/2π=87.54nm  ratio=0.677
```

**[Mandatory fix 5, Red Team docket item 5]** A binary `ratio<1` finding
confirms coupling EXISTS but says nothing about which DIRECTION it biases
the Bruggeman-fitted `n_eff` relative to independent-scatterer truth
(superradiant/enhancing vs. subradiant/suppressing collective response are
both physically live outcomes of dense sub-λ coupling — QUANTUM OPTICS'
Phase-2 finding, confirmed by Red Team). Phase 4 will additionally report,
qualitatively, whatever the coupled-dipole/local-field-correction
literature indicates about direction for this geometry class, or flag it
undecidable from available WebSearch snippets — no new search cost, reuses
queries already committed below.

### Item C — MATERIALS' own missed query set (NiP black, carbon/graphene
aerogel) — now with falsifiable bands

**[Mandatory fix 3, Red Team docket item 3]** exp-061 never searched
electroless nickel-phosphorus "NiP black" coatings or carbon/graphene-
aerogel absorbers (MATERIALS' own Iteration-38 Phase-5 flag) — genuinely
graded-porosity real materials, arguably closer in spirit to
`graded_black_shell`'s coded mechanism (homogeneous, near-ε=1, radially
graded loss) than either class exp-061 actually searched. Predictions
EM-6/EM-7 below give this class the same MP-style falsifiable-band
treatment exp-061 gave CNT forests, so Phase 4 cannot return real numbers
with zero realizability verdict. **Whose charter renders the tier
interpretation**: Phase 4 reports the raw (α, thickness) findings scored
against EM-6/EM-7's bands; MATERIALS' own tier judgment (does this class
change MP-4's UNOBTANIUM-WITH-PARAMETERS verdict) is explicitly owed at
Phase 5, not assumed or rendered here — this is a MATERIALS-charter
question and this is an EM-led cycle.

---

## The search plan — 14 queries, committed before Phase 4 runs

Continuation of exp-061's own search (not a restart); same T18
evidentiary-tier discipline (WebFetch blocked 41+ consecutive attempts
since Iteration 13, standing — re-confirmed at Phase 4 before any
WebSearch fallback, per every prior cycle's convention).

1. `Brewer Science black matrix organic photoresist optical density measurement method reflectance or transmission`
2. `LCD black matrix optical density OD measurement convention reflection transmission display`
3. `high optical density ultra thin organic black matrix patent reflective backplane substrate metal layer`
4. `black matrix photoresist optical density visible spectrum wavelength range broadband narrowband`
5. `black matrix coating interference stack quarter wave antireflection display panel`
6. `carbon black pigment loaded photoresist absorption coefficient thin film optical density`
7. `electroless nickel phosphorus NiP black coating reflectance absorptance optical properties`
8. `NiP black coating optical density thickness micron space stray light baffle`
9. `graphene aerogel optical absorption coefficient broadband visible reflectance`
10. `carbon aerogel ultra-black coating reflectance thickness absorption coefficient`
11. `vertically aligned carbon nanotube forest inter-tube spacing pitch diameter nanometer`
12. `carbon nanotube forest areal packing density tube diameter gap nanometer`
13. `vertically aligned multi-walled carbon nanotube effective index n_eff 1.04 0.01i original paper title`
14. `black matrix optical density measurement specular near-normal vs diffuse integrating sphere hemispherical` **[added, mandatory fix 2]**

Queries 1–5,14 target the R-vs-T/measurement-geometry discriminator; 6 is
a direct-α fallback; 7–8 are the NiP-black set (Item C); 9–10 are the
carbon/graphene-aerogel set (Item C); 11–12 target the near-field-coupling
rider (Item B); 13 re-attempts the standing n_eff primary-source pin.

---

## Idealizations

1. Normal incidence, single-interface planar Airy stack — the real film's
   measurement angle/polarization/surface texture is unknown from
   available snippets.
2. The R-based "÷2" correction is a leading-order geometric reading, not a
   full Airy inversion (ignores the front-surface's own additive
   contribution to total measured R) — a refinement for a future cycle if
   the film's own front-surface index is ever recovered.
3. The passivity envelope `2e^{-τ}` uses `|r₁₂|,|r₂₃|→1` (maximal
   contrast) — a ceiling, not the realistic (smaller) correction for
   organic-photoresist indices (`n≈1.5–1.7`).
4. Item B's illustrative numbers use general-domain-knowledge CNT
   dimensions (`D=20nm, f=5%`), not exp-061's own sourced figures (its
   query 9 never extracted a pitch/diameter pair). A CONFIRMED finding at
   Phase 4 confirms a placeholder-consistent result, not a validation of
   these specific assumptions — Phase 4/5 must say so explicitly, not let
   "CONFIRMED" imply the placeholder assumptions themselves were checked.
5. "Broadband disfavors resonance" is necessary, not sufficient — a
   broadband coating could stack several narrowband resonant absorbers, a
   real metamaterial-absorber strategy this analysis does not model or
   rule out.
6. Pigment-loaded organic photoresists have lateral micro/nanostructure
   (pigment graininess) that can add diffuse-scattering-based blackness
   enhancement beyond either the coherent-thin-film picture or simple
   bulk Beer–Lambert absorption — flagged, not modeled.
7. T18 (WebFetch) assumed still blocked; Phase 4 re-confirms before
   falling back to WebSearch-snippet synthesis.
8. This cycle registers no new `lab/caveat_lint.py` machinery beyond the
   registry widening already applied (Phase 3, above) — any further new
   numbers needing propagation get a new registry entry at Phase 3/5, per
   standing house discipline.
9. **[Mandatory fix 4, Red Team docket item 4 — THERMODYNAMICS' finding,
   sharpened by Red Team's own tracing]** The standing THERMO disposition
   (`exp061-thermo-length-scale-staleness`, margin 1.35×–3.79×) computes
   `l_geometric_m` as `τ_true/α` at MP-1's own best in-band α figure
   (`n_eff=1.04+0.01i`-derived, 2.28×10³ cm⁻¹) — the SAME Bruggeman/
   effective-medium fit Item B above is interrogating for near-field-
   coupling validity. If Item B's near-field test is CONFIRMED, the α
   figure `l_geometric_m` is built from is exactly the kind of number
   whose homogenization-validity this cycle calls into question. Flagged
   for Phase 5 review; no new margin computation is owed this cycle (zero
   FDTD, no new absorbed-power measurement). Separately, and independently
   of Item B's outcome: `l_geometric_m`'s own construction (a real
   hypothetical-solid thickness implied by a real material's α, NOT a
   simulation-grid proxy) sits textually adjacent to — though on
   inspection does not violate — `lab/thermo_sidecar.py::gas_conduction_
   h_eff`'s own docstring prohibition on "an optical/extinction-derived
   length... NEVER" in place of "a real geometric length of the...
   SOLID body." This closeness is named here so a future reader does not
   have to rediscover it.

---

## Predictions — committed to git BEFORE Phase 4's search runs

| # | Claim | Predicted outcome | Falsification condition |
|---|---|---|---|
| **EM-1** | Coherent multi-beam interference correction | ≤0.2% relative (T-based, τ=6.91); ≤6.3% relative (R-based, τ=3.45) — the passivity envelope `2e^{-τ}` | Falsified if a fuller Airy treatment with actual sourced indices yields a correction exceeding ~20% relative (an order of magnitude above the envelope) — would promote the resonant-absorber alternative from flagged to leading hypothesis |
| **EM-2** | R-vs-T geometric correction | If reflectance-based: α corrects 6.91×10⁴→3.45×10⁴ cm⁻¹ (ratio 1.20×→0.60×). If transmission-based: no correction (1.20× stands) | Inconclusive, not falsified, if Phase 4 cannot determine either convention — the citation becomes the bounded range [0.60×,1.20×], not a point estimate |
| **EM-3** | Spectral bandwidth as a resonance discriminator, **conditioned on measurement geometry (mandatory fix 2)** | If the patent's OD is reported as **specular/near-normal**: a broadband reading is a genuine (though not conclusive) discriminator against resonance, per the original reasoning. If reported as **angle-integrated/hemispherical**, OR if geometry cannot be determined: a "broadband" finding is **NOT** evidence against the resonant-absorber alternative — at best uninformative, plausibly its expected signature under angle-averaging | Falsified (specular case) if Phase 4 finds the OD tied to one design λ or an explicit interference/antireflection stack. The angle-integrated/undetermined case has no falsification condition of its own — it is a scope narrowing, not a claim |
| **EM-4** | Net effect on MP-3/MP-4's numeric-proximity axis | Corrected ratio lands in [0.60×,1.20×] either OD convention — reinforces, does not threaten, the existing mechanism-class exclusion | Falsified if any corrected value (EM-1/EM-2/EM-3 combined) falls outside [0.5×,2×] of α_true — i.e. if this analysis actually flips the numeric-proximity test |
| **EM-5** | Near-field-coupling existence | `gap/(λ/2π)≈0.68<1` at 550nm (illustrative); Phase 4's sourced figures predicted to confirm ratio<1 at all three bench λ (450/600/750nm) | Falsified if sourced pitch/diameter give ratio≥1 at any bench λ — near-field classification withdrawn, ordinary independent-scatterer picture stands |
| **EM-5b** | Near-field-coupling **direction** (new, mandatory fix 5) | Predicted UNDECIDABLE from available WebSearch snippets (a qualitative literature judgment, not previously searched by this program) | Not falsifiable in the usual sense — scored as DECIDED (state which direction) or UNDECIDABLE at Phase 4; either outcome is informative and neither is a failure |
| **EM-6** | NiP-black coating effective α / thickness at near-total blackness (new, mandatory fix 3) | **Predicted band: thickness 10–200µm, α similar order to CNT-forest figures (10²–10⁴ cm⁻¹)** — reasoning: electroless NiP-black is a rough, graded-porosity metal-oxide surface, structurally closer to a diffuse/multiple-scattering absorber than a homogeneous bulk medium, similar mechanism class to CNT forests | Falsified toward PLAUSIBLE/PUBLISHED for `graded_black_shell` if a source reports NiP-black effective α within ~2× of α_true AND thickness within ~2× of 1.44µm, both together |
| **EM-7** | Carbon/graphene-aerogel effective α / thickness (new, mandatory fix 3) | **Predicted band: thickness 5–500µm, α order 10²–10⁴ cm⁻¹** — reasoning: aerogels are extremely low-density, porous, light-trapping-dominated structures, mechanistically similar to CNT forests (dilute + multiple scattering), not a homogeneous Beer–Lambert medium | Same falsification form as EM-6 |

**Net prediction**: this cycle sharpens, but does not flip, exp-061's
UNOBTANIUM-WITH-PARAMETERS tier — MP-2's thickness axis (70–350×) remains
independently sufficient regardless of how EM-1..EM-7 resolve. A genuine
surprise (any EM-6/EM-7 figure landing within 2× of α_true AND thickness,
or EM-4 falsifying) would be the first result in this program's
realizability-bound line since Iteration 29 to require re-opening a tier
that has already been formally closed — a real, not foreclosed,
possibility this table is built to catch.

---

## Result (Phase 4 — full record: `phase4_results.md`, this directory)

EM-1/EM-2/EM-3/EM-4 CONFIRMED (EM-3 more decisively than predicted); EM-5
FALSIFIED as a universal claim (read literally against its own
pre-registered condition — 2 of 3 sourced geometries give ratio≥1 at
every bench λ), reported as PARTIAL/geometry-class-dependent as the more
informative characterization; EM-5b CONFIRMED UNDECIDABLE (as executed,
not as a dedicated search); EM-6/EM-7 CONFIRMED-band/PARTIAL-band-miss
respectively, falsification NOT triggered by either. 0 constraint-1/2/3/4
metric scored throughout (T1 escape route: NONE, as declared).

## Learned

1. **Both open MP-3/MP-4 sub-claims from exp-061 close in the direction
   that reinforces, not threatens, the UNOBTANIUM-WITH-PARAMETERS
   tier — more decisively than predicted.** The black-matrix OD is
   transmission-based (two independent sourced conventions) and its
   measurement geometry (transmission through an unbacked substrate)
   rules out the strong-resonance/Salisbury-screen mechanism specifically
   — not merely disfavors it by a broadband reading. `REALIZABILITY_MEMO.md`
   Amendment 7 records this and the two new comparator classes below.
2. **EM-6/EM-7 (NiP-black, carbon/graphene aerogel) both fail the joint
   2×/2× falsification bar decisively, at opposite ends of the gap range
   this program has ever measured** — NiP-black is now the CLOSEST real
   comparator by thickness (6.9×–31×) this program has found, but its
   rate gap (11×–56×) is comparable, breaking the "thickness dominates,
   rate is fine" pattern CNT-forest set; carbon/graphene aerogel is the
   WORST comparator found on either axis (694×–3472× thickness). Four
   independently-sourced real-material classes now checked; zero clear
   the bar — the tier is more robustly overdetermined than at any prior
   point in this program's history.
3. **EM-5's near-field-coupling question is genuinely, honestly left
   open — not resolved, sharpened.** Confirmed for one real CNT-forest
   application class (spin-capable/yarn-precursor forests, directly-
   sourced gap 47–64nm) and refuted for two others (a general
   characterization study and a directly co-sourced density figure) —
   but none of the three sourced geometries this cycle or exp-061's own
   query 9 ever found belongs to the record-blackness/Vantablack-class
   literature this program's own α_true/n_eff figures actually cite. The
   standing homogenization-validity question every one of THERMODYNAMICS',
   QUANTUM's, and EM's own Phase-5 reviews traces back to this exact
   unpinned geometry remains open, now measured more precisely at
   adjacent-but-wrong geometries rather than closed.
4. **A genuine, useful, tier-independent deliverable**: the standing
   `n_eff=1.04+0.01i` citation — flagged un-pinnable across three-plus
   cycles (MATERIALS/QUANTUM/VISION, Iteration 38 and earlier) — is
   pinned to a specific title/journal/volume/year (*Carbon*, 2018, vol.
   129, pp. 8–14), making a targeted follow-up search against the actual
   comparison class tractable for the first time.
5. **This cycle's own review process caught real, self-referential
   process defects a third and fourth time, at Phase 2 and Phase 5
   both** — a false internal citation (EM-5's "see Phase 1/3's own
   NOTES.md table," which does not contain the cited row); a silent
   R-vs-T conversion-convention drop between Item A's own methodology and
   Item C's application of it (EM-6/EM-7 used the undivided, T-based τ
   formula on reflectance-sourced figures); and — the most consequential
   — **Checkpoint criterion 4 fired TWICE in this single iteration**, an
   unprecedented event in this program's history: once at Phase 2 (the
   `exp061-t18-evidentiary-tier-propagation` registry entry's
   `required_sites` couldn't discover this cycle's own forthcoming
   verdict-bearing files) and again at Phase 5, on the SAME entry, after
   its own same-shift Phase-3 widening was itself shown incomplete (its
   `candidate_globs` still couldn't discover any `phase2_critique_*`/
   `phase5_review_*`/`phase5_redteam_audit.md` file, for any experiment
   — demonstrated live on a pre-existing, already-merged exp-061 file
   that had been silently non-compliant since Iteration 38). Both firings
   are notifications, not pauses, per unbroken program precedent; both
   are remediated same-shift (see `phase5_redteam_audit.md`'s 10-item
   mandatory-fix docket, all applied). This is the strongest evidence yet
   that the caveat-propagation-check tool's own registry needs
   systemic, not per-entry, hardening — see Next #3.

## Next

Ranked per Red Team's Phase-5 reconciliation of all six reviews
(`phase5_redteam_audit.md` §5):

1. **Pin the record-blackness/Vantablack-class CNT forest's own
   inter-tube pitch/diameter** — every one of the six Phase-5 reviews
   independently names this as a top priority. Query 13's own success
   this cycle (pinning the n_eff citation to *Carbon* 2018, vol. 129, pp.
   8–14) makes a targeted follow-up search against that specific paper's
   own reported density/pitch figures the natural, highest-yield next
   step — it would close (not merely sharpen) the standing
   `l_geometric_m` homogenization-validity question every one of
   THERMODYNAMICS', QUANTUM's, and EM's own Phase-5 dispositions traces
   back to this exact geometry.
2. **Resolve EM-5b's near-field-coupling direction with an actually
   dedicated query set** (`coupled dipole near field correction
   absorption cross section carbon nanotube array`, `subradiant
   superradiant collective absorption sub-wavelength scatterer array`)
   — QUANTUM's own Phase-5 review found none of this cycle's 18 queries
   ever targeted this specific question; "CONFIRMED UNDECIDABLE" is an
   honestly-disclosed null result, not yet a genuine search for it.
3. **Build the numeric/derivation-consistency-check tooling**, already
   re-filed with a named owner (the Director, mandatory zero-cost rider
   at Iteration 40, per Red Team's Iteration-38 mandatory-fix item 6) —
   widened per EM's own Phase-5 recommendation to catch not just a NUMBER
   drifting unreconciled across sibling files (`τ_shell=24` vs. 9.4026;
   the stale 150µm vs. the found range) but the SAME derivation
   methodology applied two inconsistent ways within one document (this
   cycle's own EM-6/EM-7 R-vs-T drop). This cycle's own two fresh
   instances are ready-made regression test cases.
4. **Registry-wide `candidate_globs` hardening**, applied same-shift this
   cycle (a generic `experiments/*/phase*.md` pattern added to both
   affected entries and to `lab/caveat_lint.py`'s own
   `DEFAULT_CANDIDATE_GLOBS`) — re-verify at Iteration 40's own pre-flight
   that every registry entry, not just the two found this cycle, is
   covered by a broad per-experiment glob rather than a named-filename
   list, per the systemic (not per-entry) root cause Red Team's audit
   identified.

**Carried, lower priority**: EM's `sim.omega` historical registry entry;
THERMO's T25 sidecar-absence entry (bundle-candidate with the
length-scale-staleness entries); MATERIALS' own follow-up on whether a
NiP-black-style graded-porosity homogenization-validity check is owed
the same scrutiny this cycle gave VACNT forests, if a future cycle
elevates NiP-black's own standing further.
