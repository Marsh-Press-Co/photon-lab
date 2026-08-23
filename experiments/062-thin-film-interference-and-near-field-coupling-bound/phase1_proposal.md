# exp-062 — Phase 1 Proposal: Thin-Film Interference and Near-Field-Coupling
# Bounds for the MP-3/MP-4 Mechanism-Class Ambiguity

**Panel Iteration 39. Lead: ELECTROMAGNETISM, by ROTATION** (VISION→PHOTONICS→
MATERIALS→EM→THERMODYNAMICS→QUANTUM→repeat; the slot deferred since Iteration
36, when `h_eff`'s and `Q_ext(x)`'s LOCKs, then `graded_black_shell`
absorptivity's LOCK, each broke rotation in turn; no new LOCK fired at
Iteration 38's close, so rotation resumes here). **T1 escape route: NONE.**
Zero constraint-1/2/3/4 metric is scored this cycle — a realizability-bound
continuation, the same category as exp-036/037/061. Zero FDTD throughout;
zero network for the closed-form items; a Phase-4 WebSearch continuation for
the mechanism-class item only.

---

## 1. Scope narrative (≤300 words) — why this is an EM question

Iteration 38 (exp-061) closed `REALIZABILITY_MEMO.md` Entry 2's absorptivity
question — UNOBTANIUM-WITH-PARAMETERS, overdetermined by a 70–350× thickness
gap — but left one numeric loose end on the record: an out-of-class organic
black-matrix patent film whose claimed `OD≥3.0 at ≤1µm` numerically
approaches the corrected target α (within ~1.2×). That number was accepted
at face value — divide a claimed optical density by a claimed thickness —
with no check on what "optical density" actually measures in a coated,
supported thin film, and no check on whether the figure is even a bulk-
absorption number at all.

Both of those are electromagnetism, not materials science or photonics.
Whether an "OD" figure means `−log₁₀(T)` (one pass) or `−log₁₀(R)` off a
backed film (a round trip) is a question about beam path length through a
lossy medium bounded by two interfaces — ordinary Fresnel/Airy bookkeeping.
Whether a thin absorbing layer's measured reflectance is set by bulk
Beer–Lambert loss alone, or is being reshaped by coherent multiple
reflection between its two interfaces (constructively enhanced, as in a
Salisbury-screen absorber, or left essentially untouched, as any sufficiently
lossy layer is) is a textbook coherent-interference/energy-coupling
question — and a passive medium's own reflection/transmission coefficients
obey hard bounds (`|r|,|t|≤1`, `R+T+A=1`) that let this be answered with a
ceiling, not a guess. This is exactly my charter's "impedance matching /
coherent interference / energy coupling bookkeeping" clause, and it is the
piece of item 1 that QUANTUM's own exp-061 Phase-5 review named as
"squarely EM's/PHOTONICS' charter, unchecked so far." The companion rider
(near-field coupling vs. visible λ) is the same charter from the other
side — classical evanescent-coupling range, not a quantum-coherence
question, which is why QUANTUM's own review found its own vocabulary-based
fallback test measured the wrong thing.

---

## 2. T1 escape route: NONE

This cycle scores no constraint-1/2/3/4 metric. It sharpens a realizability
bound (`REALIZABILITY_MEMO.md` Entry 2 / Amendment 6) and closes an OPEN
sub-claim from exp-061's own MP-4 finding. Same evidentiary posture as
exp-036/037/061: general-domain-knowledge predictions committed before any
search runs; the search itself (Phase 4) is disclosed in advance as
WebSearch-snippet synthesis, not primary-source reading (T18).

---

## 3. Scope decision: one primary item + one zero-cost rider, item 3 declined

Red Team's Iteration-38 ranked top-3 is: (1) resolve the MP-3/MP-4
mechanism-class ambiguity (R-vs-T OD basis, substrate-interference check,
MATERIALS' missed NiP-black/aerogel query set); (2) replace QUANTUM's
coherence/localization vocabulary-presence fallback with a physical
near-field-coupling numeric threshold; (3) PHOTONICS' numeric-value-
consistency-check tooling gap (extend `lab/caveat_lint.py` to cross-check a
registered NUMBER, not just a phrase).

**I take up (1) and (2) this cycle; I decline (3).** Reasoning, stated for
Red Team to weigh:

- **(1) and (2) share one genuine EM question**, not two unrelated tasks
  bundled for coverage: both ask "does a classical field/wave-coupling
  approximation actually hold in this regime, or is a reported number
  quietly relying on an effect the reporting convention doesn't disclose?"
  (1) asks it of a measured optical density; (2) asks it of an
  effective-medium/homogenization claim. Both are zero-FDTD desk
  calculations; (2) is additionally zero-marginal-search-cost, since it
  either reuses figures already sitting in exp-061's own query-9 transcript
  or needs at most one narrow supplementary query already folded into (1)'s
  own committed list below. This mirrors exp-061's own two-co-mandatory-
  item pattern (a literature item + a companion build), not overreach for
  its own sake — a single Phase-4 dispatch already has to run a search for
  (1); riding (2)'s own confirmation on the same dispatch costs nothing
  additional.
- **(3) is declined, not merely deferred as an afterthought.** A registered-
  NUMBER cross-check across sibling files is a documentation/software-
  tooling design question — exactly the same category `lab/caveat_lint.py`
  itself already occupies, and its own design rationale (Iteration 38,
  Item B) states plainly that this class of tool is deliberately *not* a
  physics gate. Building it teaches nothing about field/wave behavior,
  impedance matching, or energy coupling; it would be scope I annexed for
  cycle-coverage, not scope my charter actually owns. Cramming a third,
  charter-mismatched item into an EM-led cycle is the overreach the
  question in my brief warns against — it would either force me outside my
  discipline (a PANEL.md violation: "not permitted to defer... speak only
  from its own discipline" cuts both ways — I should not annex another
  seat's tooling proposal either) or get a shallow, box-checking treatment
  Red Team would rightly attack. **Recommendation, not a commitment**: (3)
  is best executed either by PHOTONICS (who raised it) at a future
  rotation slot, or directly by the Director as a standing-infrastructure
  patch outside any one seat's Phase-1 proposal, since — like
  `caveat_lint.py` itself — its authorization does not obviously require a
  full seven-seat cycle at all. I flag this for Red Team's own ruling
  rather than deciding it unilaterally.

---

## 4. Item (1): the R-vs-T optical-density basis and the substrate-
interference/near-field bounds — closed-form EM analysis

### 4.1 Setup

The disputed figure (exp-061, MP-3): a Brewer Science organic black-matrix
photoresist patent claims **optical density ≥3.0 at coating thickness
≤1 µm**. exp-061 converted this with the single-pass Beer–Lambert identity
`τ = OD·ln10`, `α = τ/d`, giving `α ≈ 6.91×10⁴ cm⁻¹` at `d=1µm` — **1.20×**
this program's own corrected target `α_true ≈ 5.74×10⁴ cm⁻¹` (LOGBOOK
Iteration 38). That conversion silently assumes (a) OD is a *transmission*
figure (`−log₁₀ T`, one pass through the film) and (b) the film's measured
reflectance/transmittance is governed by bulk absorption alone, with no
coherent contribution from the film's own two bounding interfaces. Neither
assumption was checked (PHOTONICS' own exp-061 Phase-5 flag, T18-blocked to
resolve directly).

**Model.** A single absorbing layer (complex index `n₂=n₂′+in₂″`, thickness
`d`) between an incident medium `n₁` (air, `n₁=1`) and a substrate/backing
`n₃`, normal incidence. Standard single-layer Airy stack:

```
r₁₂ = (n₁−n₂)/(n₁+n₂)          r₂₃ = (n₂−n₃)/(n₂+n₃)
β    = (2π/λ)·n₂·d = φ + iγ      φ = 2π n₂′ d/λ,  γ = 2π n₂″ d/λ
r_stack = (r₁₂ + r₂₃·e^{2iβ}) / (1 + r₁₂ r₂₃ e^{2iβ})
R_stack = |r_stack|²
```

The single-pass **power** optical depth is `τ ≡ 2γ = α d` (this bench's own
established convention, `α=4πn₂″/λ`); the round-trip amplitude factor
`e^{2iβ}` has magnitude `e^{-τ}` — the standard bulk-Beer–Lambert
single-pass power transmittance. This is the same `Im(n)`-weighted
convention Red Team's own exp-061 Phase-2 adjudication used for `τ_true`
(EM's own re-derivation confirmed sound at exp-061 Phase 5) — reused here,
not a new assumption.

### 4.2 The R-vs-T geometric factor (dominant effect, not interference)

If OD is **transmission-based** (`OD=−log₁₀T`, one pass), `τ = OD·ln10`
directly — exp-061's own reading stands.

If OD is **reflectance-based** off a backed/opaque film — the natural
convention for a coating whose product use *is* to look black in reflection
(a display's own viewing condition) — the light traverses the absorbing
layer **twice** (in, reflect at the back, out) before re-emerging. To
leading order (backing near-fully reflective, front-surface loss folded
into the coherent term treated separately below), the ROUND-TRIP power
attenuation is `e^{-2τ}`, so a reflectance-based OD encodes `2τ`, not `τ`:
the correctly-inferred single-pass depth is **half** of the T-based reading.

```
OD = 3.0
τ (T-based)      = OD·ln10          = 6.9078   ->  α = 6.908×10⁴ cm⁻¹  (ratio to target: 1.20×)
τ (R-based, ÷2)  = OD·ln10 / 2      = 3.4539   ->  α = 3.454×10⁴ cm⁻¹  (ratio to target: 0.60×)
```

(computed by direct invocation, not hand-typed — see Section 4.5; target
`α_true=5.74×10⁴ cm⁻¹` per LOGBOOK Iteration 38.)

**This factor of ~2, not an order of magnitude, is the dominant source of
ambiguity in the previously-reported "1.20×" figure** — a plain ray-optics
path-length effect, not a coherence phenomenon. Both endpoints (0.60×,
1.20×) sit inside a "within 2×" window of the target either way — see
EM-4/Falsification below for what this does and does not settle.

### 4.3 The coherent-interference bound (small, passivity-derived, in BOTH
cases)

Expanding `r_stack` for `|r₂₃e^{2iβ}| = |r₂₃|e^{-τ} ≪ 1` (valid at both
candidate τ — see 4.5):

```
r_stack ≈ r₁₂ + r₂₃ e^{2iφ} e^{-τ} (1 − r₁₂²) + O(e^{-2τ})
```

The interference (cross) term's *relative* contribution to `R_stack` is
bounded, using the passivity fact that Fresnel amplitude coefficients at
any passive interface satisfy `|r₁₂|,|r₂₃| ≤ 1` (this is the same
reciprocity/passivity bookkeeping my charter owns generally, applied here
to a realizability question rather than a T1 mechanism):

```
|ΔR / R₁₂| ≲ 2·e^{-τ}          (leading order, self-consistently small since the
                                 neglected O(e^{-2τ}) term is itself only
                                 a further factor e^{-τ} smaller)
```

giving **≤0.2% relative** (T-based, τ=6.91) or **≤6.3% relative** (R-based,
τ=3.45) — see Section 4.5 for the exact numbers. **Genuine coherent
multi-beam interference is a minor correction in BOTH candidate readings**
— an order of magnitude or more below the R-vs-T geometric factor above.
This is the direct answer to the ranked-queue item's "check it for
substrate-interference enhancement": the effect exists, is real, is bounded
by an explicit passivity ceiling, and is small — it does not, by itself,
explain the reported blackness, and it does not materially change either
candidate α figure in Section 4.2.

### 4.4 The resonant-absorber alternative, and a falsifiable spectral
discriminator

The bound in 4.3 assumes the film sits deep in the "optically thick"
regime (`τ≳3`), where interference is a small perturbation on a genuinely
bulk-absorbing medium. The opposite regime is real and well known in EM: an
optically **thin** (`τ≪1`) lossy sheet on a reflective backing, at the
right thickness/impedance, can absorb nearly 100% of incident power via
destructive interference alone (a Salisbury-screen/critically-coupled
absorber) — in that regime, a measured near-zero R does **not** imply a
large bulk α at all; it implies a well-tuned resonance. If that is what the
patent film actually is, dividing its claimed OD by its thickness would be
the wrong calculation entirely, and the "1.20×/0.60×" figures in 4.2 would
be **upper bounds** on the true bulk α, not point estimates — the candidate
would be an even worse match to `graded_black_shell`'s homogeneous,
non-resonant mechanism than currently credited, reinforcing (not
threatening) MP-4's exclusion, exactly the direction the ranked-queue item
flagged.

**A falsifiable, checkable discriminator exists and costs nothing beyond
Phase 4's own search**: resonant/critically-coupled absorbers are
inherently **narrowband** (tied to one design wavelength by their own
interference condition); a genuinely bulk-absorbing, non-resonant coating
is **broadband** by construction (this is exactly `graded_black_shell`'s
own design logic — see EM-3 below). Whether the patent states its OD figure
as a broadband visible-spectrum claim or a narrow spectral band/single
design wavelength is exactly the kind of detail a patent's own claims
language typically states, and directly bears on which regime (4.3's small
correction, or 4.4's resonant alternative) actually governs.

### 4.5 Illustrative numbers, computed by direct invocation (R4)

```
$ python3 -c "
import math
OD=3.0; d_cm=1e-4; alpha_true=5.74e4
tau_T = OD*math.log(10); alpha_T = tau_T/d_cm
tau_R = tau_T/2;         alpha_R = tau_R/d_cm
print('tau_T=%.4f  alpha_T=%.6g  ratio=%.4f' % (tau_T, alpha_T, alpha_T/alpha_true))
print('tau_R=%.4f  alpha_R=%.6g  ratio=%.4f' % (tau_R, alpha_R, alpha_R/alpha_true))
print('bound(T)=%.4g  bound(R)=%.4g' % (2*math.exp(-tau_T), 2*math.exp(-tau_R)))
"
tau_T=6.9078  alpha_T=69077.6  ratio=1.2034
tau_R=3.4539  alpha_R=34538.8  ratio=0.6017
bound(T)=0.002  bound(R)=0.06325
```

**These are Phase-1 illustrative numbers**, using this program's own
already-committed `α_true` anchor and the OD=3.0/d≤1µm figures already on
the record from exp-061 — not yet the outcome of any Phase-4 search. They
will be recomputed (not hand-copied) at Phase 3/4 once the actual patent
methodology (R-based vs. T-based, broadband vs. narrowband) is pinned or
confirmed still-unpinnable.

---

## 5. Rider: a physical near-field-coupling numeric threshold (replaces
QUANTUM's vocabulary-presence fallback)

### 5.1 What it replaces and why

exp-061's own MP-4 carried a "coherence/localization fallback": did the
sourced CNT-forest literature describe blackness using localization/
near-field vocabulary? It did not, and was scored CONFIRMED-not-triggered
at Phase 4 — then downgraded to OPEN at Phase 5 (QUANTUM's own catch,
Red-Team-confirmed): Bruggeman/effective-medium fitting is this subfield's
*universal reporting convention* regardless of true underlying physics, so
the test was closer to a vocabulary screen than a physics screen. VACNT
inter-tube pitches are reported in the tens-of-nm range — deeply
sub-wavelength at visible λ, "a textbook near-field-coupling geometry an
effective-medium fit is silent on" (QUANTUM's own words, exp-061 Phase 5).

That silence is a classical electrodynamics question, not a quantum-optics
one: does a lattice of sub-wavelength conducting scatterers actually behave
as the homogeneous medium `graded_black_shell`'s own `Im(n)` treatment
(and every α figure derived from it) assumes, or does it sit in a regime
where near-field (evanescent, non-radiative) coupling between neighbors
invalidates a simple homogenization? This is squarely mine to formalize:
"field/wave behavior... energy coupling," applied to when a homogenization
approximation is licensed at all.

### 5.2 The criterion

For an electrically small scatterer (radius/diameter ≪ λ), the reactive
near field extends to order `λ/2π` — a standard engineering rule of thumb
for the boundary between near-zone (evanescent, `1/r³`-dominated coupling)
and far-zone (radiative) behavior. The proposed pre-registered check:
compute the inter-tube **gap** `g = p − D` (pitch minus diameter, for a
representative packing geometry) from whatever real, sourced pitch/diameter
figures Phase 4 recovers, and score:

```
ratio = g / (λ/2π)
```

`ratio ≪ 1` ⇒ neighboring tubes sit well inside each other's reactive near
field at every visible wavelength — near-field coupling is real, not a
labeling artifact, and a bulk-homogenization/Beer–Lambert reading of the
forest's blackness is at minimum incomplete. `ratio ≳ 1` ⇒ tubes couple
only radiatively (ordinary independent-scatterer/dilute-medium behavior),
and the effective-medium reporting convention is not hiding anything this
test would have caught.

### 5.3 Illustrative number (Phase-1 placeholder, NOT yet the sourced figure)

exp-061's own query 9 (`carbon nanotube forest packing density volume
fraction optical properties`) was run but its own Phase-4 record states it
only "confirmed Beer-Lambert-Bouguer attenuation methodology," without
extracting a specific pitch/diameter pair — so no sourced number exists yet
to score this against. Using general-domain-knowledge, representative
CNT-forest figures only (MWCNT diameter ~20 nm; areal packing fraction
~5%, the low-middle of exp-061's own "1–10%" reasoning text), for a square
lattice `f = (π/4)(D/p)² ⇒ p = D√(π/4f)`, at λ=550 nm (visible midpoint):

```
$ python3 -c "
import math
D=20.0; f=0.05; lam=550.0
p=D*math.sqrt(math.pi/(4*f)); gap=p-D
print('p=%.2f nm  gap=%.2f nm  gap/lam=%.4f  lam/2pi=%.2f nm  ratio=%.3f'
      % (p, gap, gap/lam, lam/(2*math.pi), gap/(lam/(2*math.pi))))
"
p=79.27 nm  gap=59.27 nm  gap/lam=0.1078  lam/2pi=87.54 nm  ratio=0.677
```

**Illustrative prediction: ratio ≈ 0.68 (< 1)** — comfortably inside the
near-field-coupling regime under representative assumptions. This is
explicitly a placeholder pending Phase 4's own sourced pitch/diameter pull
(either from the existing query-9 transcript, re-read in full, or the
narrow supplementary query in Section 6) — not a claim about the real
forests this program has been citing.

---

## 6. The search plan — exact query list, committed before Phase 4 runs

**Continuation of exp-061's own search, not a restart** — reuses its source
classes and evidentiary-tier discipline (T18: WebFetch blocked 41+
consecutive attempts since Iteration 13, standing; WebSearch-snippet
synthesis only, disclosed at every verdict per the (now-widened)
`exp061-t18-evidentiary-tier-propagation` registry entry's own standard).

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
13. `vertically aligned multi-walled carbon nanotube effective index n_eff 1.04 0.01i original paper title` (re-attempt pinning the standing n_eff citation, carried from exp-061 query 18)

Queries 1–5 target Section 4's R-vs-T/broadband discriminator; 6 is a
fallback for a direct α figure if the OD basis can't be pinned; 7–8 are
MATERIALS' own missed NiP-black query set (Red Team's ranked item 1, run
here as zero-marginal-cost additions to a search this cycle already needs —
their *interpretation* as a realizability comparator is MATERIALS' charter,
not scored by this proposal's own EM-native predictions below); 9–10 are
the companion carbon/graphene-aerogel class; 11–12 target Section 5's
near-field-coupling rider; 13 is the standing, three-times-flagged
n_eff=1.04+0.01i primary-source pin.

---

## 7. Falsifiable predictions — committed BEFORE any search runs

| # | Claim | Predicted outcome | Reasoning |
|---|---|---|---|
| **EM-1** | Coherent multi-beam interference correction to the black-matrix candidate's reflectance, at either τ candidate | **≤0.2% relative at τ=6.91 (T-based); ≤6.3% relative at τ=3.45 (R-based)** — the passivity-derived envelope `2e^{-τ}` | Both τ are large enough that the Airy expansion's neglected term is itself only ~`e^{-τ}` smaller (0.1%/3.2% self-consistency check, Section 4.5) — safely convergent |
| **EM-2** | R-vs-T geometric (double-pass) correction | If Phase 4 finds/argues the OD is **reflectance-based**: implied single-pass α corrects from 6.91×10⁴ to **3.45×10⁴ cm⁻¹**, ratio-to-target from 1.20× to **0.60×**. If **transmission-based**: no correction; 1.20× stands. | Ordinary double-pass ray geometry through a backed absorbing film — the dominant effect, ~2×, not the ~0.2–6.3% interference correction of EM-1 |
| **EM-3** | Spectral bandwidth as a resonance discriminator | Phase 4 will find the patent's OD≥3.0 claim stated as a **broadband** (multi-hundred-nm visible-range) figure, not tied to one design wavelength, and will find **no** mention of a multilayer/quarter-wave/antireflection stack | A resonant/critically-coupled (Salisbury-screen-type) absorber is inherently narrowband by its own interference condition; a genuinely bulk-absorbing coating for a display application has no such constraint |
| **EM-4** | Net effect on MP-3/MP-4's numeric-proximity axis | The corrected ratio-to-target lands in **[0.60×, 1.20×]** — inside a "within 2×" window under EITHER OD convention; this analysis will **not** flip whether the raw numeric-proximity test is cleared, but will replace an unchecked point estimate with a bounded, mechanism-aware range, confirming the mechanism-class exclusion (not the numeric near-miss) is what actually carries MP-4's tier | Matches the ranked-queue item's own framing (QUANTUM's Phase-5 flag: "would only reinforce the existing MP-4 exclusion, not threaten it") — a real prediction, not a foregone conclusion, since a large interference/resonance effect *could* have moved the ratio far outside 2× either direction |
| **EM-5** | Near-field-coupling numeric threshold | Using representative (not yet sourced) CNT dimensions, `gap/(λ/2π) ≈ 0.68 < 1` at 550 nm — inside the reactive near-field regime. Phase 4's actual sourced pitch/diameter figures (queries 11–12, or a re-read of exp-061's own query-9 transcript) are predicted to confirm ratio **< 1** at all three bench wavelengths (450/600/750 nm) | Published CNT diameters (single-digit to a few tens of nm) and packing fractions (order 1–10%, per exp-061's own MP-1 reasoning) are well below any regime where `ratio ≥ 1` would be plausible |

---

## 8. Falsification conditions, pre-registered

- **EM-1 falsified** if a fuller Airy treatment using the *actual* sourced
  front-surface/backing indices (should any secondary source ever supply
  them) yields a coherent correction exceeding ~20% relative — an order of
  magnitude above the passivity envelope — indicating the film is not
  safely in the "optically thick" regime this bound assumes, and Section
  4.4's resonant-absorber alternative would need to move from "flagged
  alternative" to "leading hypothesis."
- **EM-2** does not have a pass/fail falsification in the usual sense (it
  is a conditional identity, not a point prediction) — it is **inconclusive**
  if Phase 4 cannot determine EITHER convention from available sources, in
  which case the standing citation becomes the bounded range [0.60×,1.20×],
  not a point estimate, and that bounded range itself is what gets
  registered going forward.
- **EM-3 falsified** if Phase 4 finds the OD figure reported at or near one
  specific design wavelength only, or finds explicit mention of a
  multilayer/interference/antireflection stack in the patent's own claims
  or a secondary description of it — in which case Section 4.4's resonant-
  absorber reading gains support and MP-3/MP-4's own "1.20×/0.60× ratio
  is a fair characterization of bulk α" premise would need to be revisited,
  a genuinely different and more consequential outcome than EM-4 predicts.
- **EM-4 falsified** if either corrected endpoint (0.60× or 1.20×,
  or any further-corrected value from EM-1/EM-2/EM-3's actual Phase-4
  results) falls outside [0.5×, 2×] of `α_true=5.74×10⁴ cm⁻¹` — i.e., if
  this analysis actually DOES flip whether the numeric-proximity test is
  cleared, contrary to the predicted "reinforces, doesn't threaten" outcome.
- **EM-5 falsified** if Phase 4's actual sourced pitch/diameter figures
  give `gap/(λ/2π) ≥ 1` at any of the bench's three wavelengths — meaning
  the near-field-coupling classification would need to be withdrawn in
  favor of an ordinary independent-scatterer (far-zone/radiative-coupling)
  picture, and the fallback test's OPEN status would resolve toward
  "did not trigger" being the physically correct answer after all, not
  merely an artifact of vocabulary screening.

---

## 9. Idealizations — stated honestly

1. **Normal incidence, single-interface planar Airy stack.** The real
   black-matrix film's actual measurement geometry (angle, polarization,
   any surface texture/graininess in the pigment-loaded photoresist) is
   unknown from available snippets. A textured or diffuse-scattering
   surface would need a fuller (non-specular) treatment this desk analysis
   does not attempt.
2. **The R-based "divide by 2" correction (Section 4.2) is a leading-order,
   illustrative geometric reading, not a full Airy inversion.** It ignores
   the front-surface Fresnel reflectance's own additive contribution to
   the total measured R (i.e., `R_measured ≈ R₁₂ + (1−R₁₂)²R_backing·e^{-2τ}`
   in a more careful non-coherent decomposition, or the full coherent
   `r_stack` of Section 4.1) — a real refinement Phase 3/4 should apply if
   Phase 4's search actually recovers the film's own front-surface index,
   which it has not yet.
3. **The passivity envelope `2e^{-τ}` (Section 4.3) is a ceiling, using
   `|r₁₂|,|r₂₃|→1` — the maximal-contrast case.** For realistic organic-
   photoresist indices (`n≈1.5–1.7`), the actual correction will be smaller
   than this bound. Stated as a ceiling deliberately, per EM's own charter:
   this states what a passive medium *permits*, not what it *does*.
4. **EM-5's illustrative numbers (Section 5.3) use general-domain-knowledge
   CNT dimensions, not exp-061's own sourced figures**, which this proposal
   could not extract from the available Phase-4 record (query 9's own
   summary did not report a pitch/diameter pair). If Phase 4's actual
   sourced numbers differ substantially from `D=20nm, f=5%`, the conclusion
   could change quantitatively — though the well-known range CNT diameters
   and packing fractions span across this literature makes a qualitative
   reversal (ratio crossing above 1) unlikely, not impossible.
5. **The "broadband disfavors resonance" heuristic (EM-3) is necessary, not
   sufficient.** A broadband coating could in principle stack several
   narrowband resonant absorbers to cover the visible range — a real
   metamaterial-absorber design strategy that exists in the literature.
   This alternative is disclosed, not modeled or ruled out here.
6. **A third possible mechanism is not modeled at all**: real pigment-
   loaded organic photoresists have lateral micro/nanostructure (pigment
   particle graininess) that can add diffuse-scattering-based blackness
   enhancement beyond either the coherent-thin-film picture (Section 4) or
   simple bulk Beer–Lambert absorption. Flagged, not swept under.
7. **T18 (WebFetch) is assumed still blocked** (not independently re-tested
   this Phase-1 step; Phase 4 will re-confirm before falling back to
   WebSearch-snippet synthesis, per every prior cycle's own convention).
8. **This proposal registers no new `caveat_lint.py` machinery** (Item 3 is
   declined, Section 3) — but any new corrected numbers this cycle's own
   Phase-4 results produce (e.g., a settled R-vs-T reading, or a sourced
   near-field ratio) that need propagating to sibling sites
   (`REALIZABILITY_MEMO.md`, exp-061's own NOTES.md/phase4_results.md)
   will get a new registry entry in the EXISTING, already-built
   `lab/caveat_lint_config.json` at Phase 3/5, per standing house
   discipline — declining to build NEW tooling is not declining to USE the
   tooling this program already has.
