# exp-037 — The Free-Carrier-Absorption / Combined Saturable-RSA Media Literature Check

Panel Iteration 14 · Runner: cloud panel shift · Lead: PHOTONICS (rotation)

Full seven-seat cycle: Phase 1 proposal (PHOTONICS) → 5 blind parallel
critiques (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE — unanimous **support-with-changes**, five non-overlapping
fixes) → Red Team last with everything (verdict:
**proceed-with-mandatory-fixes**, 8 numbered attacks, full adjudication of
all five seats' fixes plus 3 of its own additions) → Phase 3 synthesis
(this file) → predictions committed here, before any search runs → Phase 4
literature search. Verbatim panel transcript: this shift's session record
(LOGBOOK.md Iteration 14 carries the full text).

## Hypothesis

Iteration 13 (exp-036) closed with a near-unanimous Phase-5 ranking (three
independently-converging seats — MATERIALS, ELECTROMAGNETISM, QUANTUM
OPTICS): the free-carrier absorption (FCA) and combined saturable/RSA media
literature check is Iteration 14's top priority — the last named-but-untested
mechanism class standing between this program and any legitimate future
Checkpoint-2 attempt, deliberately excluded from exp-036's own scope under
Red Team's capping ruling. Same zero-FDTD-cost, WebSearch-grounded
methodology as exp-036. The pre-registered hypothesis: no FCA sub-class and
no combined-media architecture clears this program's dynamic-range,
irradiance, and switching-speed bounds simultaneously — but (a) FCA is not
one mechanism, it separates into at least three photonically distinct
generation-trigger sub-classes that must be scored separately, not lumped;
and (b) closing this class, even with every row failing, still likely does
NOT fire Checkpoint criterion 2 on its own, for reasons stated honestly
below rather than assumed.

## Phase 1 — Proposal (PHOTONICS, abridged)

Full verbatim proposal: this shift's session record. Six rows scored
separately: **TPA-generated/cascade FCA** (Si, GaAs, ZnSe, CdS — threshold-
gated carrier generation riding on a TPA seed event), **linearly-pumped
(photoconductive) FCA** (doped Si, doped Ge — carrier generation with NO
intensity threshold, proportional to absorbed flux at any intensity,
ambient included), **epsilon-near-zero (ENZ) band-filling nonlinearity**
(ITO, AZO, GZO — Burstein-Moss-type absorption/index shift at a TCO's ENZ
point), **graphene** (control/boundary case — textbook saturable absorber,
the wrong direction, included to confirm not assume), and **combined
saturable/RSA media** in three named architectures: tandem/cascaded SA+RSA
optical limiters, single-molecule/dyad RSA+TPA chromophores, and
composite/blended nanomaterial (fullerene+CNT) limiters. All bounds reused
verbatim from LOGBOOK.md/REALIZABILITY_MEMO.md — none invented: D_req ≥
540–600× (lower bound), absorption-only-corrected effective bar ≥ ~890–
1,180×, irradiance ceiling ≤10⁻² W/cm² (Checkpoint-2 margin) / ~10⁻³ W/cm²
(witness estimate), switching speed ~10ms–1s both directions (unsourced,
flagged provisional pending T3 throughout).

## Phase 2 — Critique (five blind, then Red Team) — summary

All five blind seats independently returned **support-with-changes** — no
verdict conflict, five non-overlapping fixes:

- **MATERIALS** found the proposal's six "unobtainium" verdicts risk
  reading as verdicts about unstructured bulk/molecular material only,
  understating what "plausible" could mean under PANEL.md's own Latitude
  rule (which requires unobtainium **with parameters**, not the bare word).
  Sub-wavelength field concentration (plasmonic hot-spots, cavity coupling)
  is the best-documented published technique for lowering exactly the
  irradiance thresholds three of six rows fail on, and the proposal never
  states the enhancement factor that would be needed.
- **ELECTROMAGNETISM** found the single most consequential catch of the
  cycle: the proposal's own "genuine, previously-unrecognized FOURTH
  kinetics sub-case" / "may not even qualify as a T1 gate" framing for
  linearly-pumped FCA is an overclaim. T17's own formula, n_ss =
  k_f(I_ambient)/(k_f(I_ambient)+k_r), was never restricted to
  threshold-gated k_f — RSA/TPA read N/A because their k_f(I_ambient) is
  *negligible* at low intensity, not because the equation structurally
  excludes thresholdless generation. This is a new magnitude regime, not a
  new equation or escape-route category, and the proposal cannot both
  disqualify the row as "not a real gate" and score it against D_req/
  irradiance bookkeeping built for exactly that case.
- **THERMODYNAMICS** found every row depositing real absorbed power
  thermalizes mostly as non-radiative lattice heat (FCA/Burstein-Moss
  band-filling are canonically non-radiative), and that Section 4's
  "switching speed clears" verdicts score only the electronic/carrier-
  relaxation clock — exp-036's own capped VO2 estimate already proved that
  clock and the lattice thermal-diffusion clock can differ by orders of
  magnitude. The mandated per-run THERMO sidecar (PANEL.md's Metrics
  table) is absent from Section 4 entirely.
- **QUANTUM OPTICS** found the proposal reuses exp-036's absorption-only
  correction (÷0.51–0.61, calibrated for `graded_black_shell`'s dielectric/
  molecular-type extinction) verbatim across three new carrier-plasma rows
  without re-deriving whether it even applies to free-carrier/plasma
  absorption — the same category error QUANTUM's own seat flagged for VO2
  last cycle, still unresolved in PLAN.md's queue. Worse for ENZ
  specifically: the cited "unity-order permittivity change" is, per the
  actual ENZ-ITO literature, dominantly **refractive** (Δε_real), not
  absorptive — scoring it directly against D_req (a σ_on/σ_off ratio) may
  be a category error one step from smuggling a refraction-driven
  mechanism into a σ(I) row.
- **VISION SCIENCE** found the proposal reproduces, before any search runs,
  the exact structure of exp-036's own overclaim — pre-committed scoring
  language ("CONFIRMED as real but SMALL," "genuine, non-negligible risk,"
  "the sharpest, most novel finding") for quantities that are chemistry
  (a population/absorption fraction), not yet perception. T17's own
  corrected status is explicit: not a scored quantity until carried through
  ε, path length, geometry into Weber contrast C and checked against T2's
  frozen C_thr(L) at Tier-W ambient — a conversion this cycle cannot
  perform (zero FDTD, no rate-equation kernel exists yet).

**Red Team (PROCEED-WITH-MANDATORY-FIXES).** Eight numbered attacks (five
adjudicating the blind seats' fixes, three new): (1) struck the Checkpoint-2
"WebFetch-blockage predicted to recur" tooling-guess from the falsifiable-
outcomes table as a self-fulfilling infrastructure assertion masquerading as
a physics prediction — moved to idealizations, replaced with a requirement
that every leg log a genuine WebFetch attempt regardless of prior-cycle
precedent; (2) found the combined-media idealization pre-decides its own
"genuine architecture question" by only ever algebraically combining
single-material numbers, when tandem/composite limiters are published
*specifically* to beat a single component's ceiling and report composite
figures directly — required a primary search for directly-published
composite dynamic-range figures before falling back to algebraic
combination; (3) found ENZ's band-filling nonlinearity was never checked
against constraint 2 (no specular return) despite ENZ media being
well-documented for anomalous reflectivity at the near-zero-index point —
required one disclosure sentence (non-verdict-changing, the row independently
fails on wavelength); (4) confirmed EM's reframing as correct and
load-bearing via direct derivation (T17's formula subsumes, not competes
with, ordinary D_req/irradiance scoring for fast-k_r cases) — ranked ABOVE
the four-seat framing that treated it as a genuine taxonomic discovery;
(5) found the combined-media long-triplet-RSA branch invokes "hysteretic"
language identically to linearly-pumped FCA but must generalize to EM's
corrected formula-based treatment too, not a separately-decreed bucket;
(6) recommended (not required) deriving TPA-cascade FCA's verdict
analytically from exp-036's own already-cited TPA irradiance figures
rather than running a duplicate full search, since the result is an
algebraic consequence of an already-established number; (7) split QUANTUM's
fix — confirmed load-bearing and elevated for ENZ (a threshold expressibility
question, one step from R1), capped/deprioritized for TPA-cascade FCA
(the row fails independently regardless of the correction's exact
magnitude, exp-036's own VO2 precedent for when a correction doesn't gate
a verdict); (8) confirmed MATERIALS' fix load-bearing but capped the
literature search to a negative-result note only (no dedicated new search
leg) to avoid re-opening the "exotic/engineered composite" idealization
exp-036 and Iteration 13 both capped. Sequencing: framing (EM's fix) lands
first since it changes what gets computed; extraction before correction
before disaggregation-gated correction (QUANTUM's ENZ fix sits ahead of any
correction there — cannot correct a quantity for "how much is absorption"
before confirming it is absorption at all); THERMO's and MATERIALS' fixes
are parallel downstream consumers of the same extracted numbers; VISION's
language cap is a terminal write-up gate, independent of the physics fixes.

**Director's synthesis: all mandatory-fix items accepted in full, none
overridden.** Red Team's docket was itself already a sound adjudication of
five non-conflicting seat critiques (cost discipline on MATERIALS'/
QUANTUM's TPA-cascade half; correct resolution of the one genuine framing
conflict, EM vs. the other four seats, via direct derivation rather than a
vote; sequencing that avoids wasted rework) — nothing in it warranted a
Director override. Red Team's recommendation (item 6, deriving TPA-cascade
FCA analytically) is adopted: it is the same cost-discipline this program
has applied every time a row's verdict is algebraically forced by an
already-cited figure (see exp-036's own capping precedents).

## Parameter tables

**Quantitative bounds under test (unchanged from exp-036, reused not
re-derived):**

| Bound | Value | Source |
|---|---|---|
| D_req (σ_on/σ_off) | ≥ 540–600× (LOWER bound, Iteration 12 amendment) | LOGBOOK T1/T16; REALIZABILITY_MEMO.md |
| Absorption-only-corrected effective bar | ≥ ~890–1,180× (molecular/dielectric extinction only — **not assumed applicable to carrier-plasma absorption**, see below) | exp-036 (÷0.51–0.61) |
| Irradiance — witness estimate | ~10⁻³ W/cm² | LOGBOOK T1, Iteration 1 |
| Irradiance — Checkpoint-2 firing margin | ≤ 10⁻² W/cm² | REALIZABILITY_MEMO.md |
| Switching speed, both directions | ~10ms–1s, **unsourced — every verdict flagged provisional pending T3** | exp-036, carried forward |
| T17 at-rest kinetics | n_ss(I) = k_f(I)/(k_f(I)+k_r) — general steady-state solution, valid for ANY nonzero k_f(I), threshold-gated or not (Red Team's Phase-2 derivation) | LOGBOOK T17, this cycle's EM fix |
| T2 perceptual scoring | C_thr(L) frozen ladder — any at-rest/coloration output must be carried through ε, path length, geometry into Weber contrast C before ANY risk/confirmed language attaches | LOGBOOK T2, this cycle's VISION fix |

**Six rows, scored separately, with the mandatory-fix corrections folded
in before any search runs:**

1. **TPA-generated/cascade FCA** (Si, GaAs, ZnSe, CdS) — **scored
   analytically, not via a dedicated search leg** (Red Team's cost-
   discipline recommendation, adopted): its irradiance verdict is an
   algebraic consequence of exp-036's own already-cited TPA onset figures
   (~10⁷–10⁸ W/cm²) — a carrier cascade seeded by a TPA event cannot
   activate below the seed event's own threshold. Absorption-only
   correction: capped/deprioritized per Red Team's split ruling — apply if
   trivial, does not gate the verdict.
2. **Linearly-pumped (photoconductive) FCA** (doped Si, doped Ge) — full
   search leg. **T1 escape-route statement corrected per EM's fix**: scored
   via T17's n_ss formula directly, not framed as a new kinetics sub-case
   or a non-gate. Extract k_f(I_ambient) and k_r (or the closest published
   proxies — generation rate and recombination lifetime) for at least one
   fast-recombination host (clean semiconductor, ns-scale) and, if found,
   one longer-lifetime host (doped/defect-rich). Any resulting n_ss or
   equivalent absorption change must be reported per VISION's cap (below)
   — computed, not assumed either direction.
3. **Epsilon-near-zero (ENZ) band-filling nonlinearity** (ITO; AZO, GZO if
   available) — full search leg. **Mandatory pre-scoring step (QUANTUM's
   elevated fix)**: disaggregate the cited nonlinearity into Δε_real vs.
   Δε_imag BEFORE any D_req comparison; if refraction dominates, rule
   explicitly that the row does not reduce to a σ(I) absorption gate under
   this seat's expressibility contract, and score it as a wavelength/
   mechanism-class disqualification instead of forcing a D_req number onto
   it. **Constraint-2 disclosure required** (Red Team's fix): one sentence
   noting whether the cited reflectivity/phase behavior at the ENZ point
   would risk a specular return, independent of the row's wavelength-based
   disqualification.
4. **Graphene** — control/boundary case, folded into the ENZ/carrier-
   materials search leg (low marginal cost). Confirm (not assume) the
   textbook saturable-absorber (wrong) direction; check for any reported
   induced-absorption/RSA-like configuration before excluding it.
5. **Combined saturable/RSA media** — full search leg, three named
   architectures (tandem/cascaded SA+RSA; single-molecule/dyad RSA+TPA
   dyads; composite/blended fullerene+CNT limiters). **Search order
   corrected per Red Team's fix**: search FIRST for directly-published
   composite/tandem dynamic-range figures (the literature's own stated
   motivation for these architectures is beating a single component's
   ceiling, so composite figures should exist); fall back to algebraically
   combining two separately-published single-material numbers ONLY where
   no composite figure is found, and flag that fallback explicitly,
   per-row, as a weaker evidentiary tier (not just in the idealizations).
   Long-triplet-RSA branch (if the tandem/composite uses exp-036's own
   newly-found long-triplet-lifetime RSA subclass): scored via the SAME
   T17 n_ss formula as row 2, using that subclass's own 1–21+ second
   reverse rate as k_r — not a separately-invented "hysteretic" bucket
   (Red Team's fix #5).
6. **MATERIALS' field-enhancement-factor arithmetic** — derived, not a
   fresh search leg (Red Team's capping). For ENZ and TPA-cascade FCA
   specifically, once D_req/irradiance figures are in hand, compute the
   sub-wavelength field-enhancement factor (×) that would close each row's
   own irradiance gap — a zero-cost arithmetic step, converting a bare
   "unobtainium" into "unobtainium-with-parameters" per PANEL.md's own
   Latitude rule. The literature-demonstration check is capped to a
   negative-result note only: report whether any of the other search legs
   already run happen to have turned up a plasmonic/cavity-coupled
   demonstration of the specific subclass in question; no dedicated new
   search commissioned.
7. **THERMODYNAMICS' capped analytic estimate** — one estimate,
   post-search, using whatever absorbed-power figures the search legs
   return: absorbed power → ΔT → emission band → detectability, for
   linearly-pumped FCA's at-rest population (row 2) and the ON-state
   absorption events of TPA-cascade/ENZ FCA (rows 1, 3). **Switching-speed
   columns split explicitly into carrier/optical relaxation time vs.
   lattice thermal-relaxation time** — exp-036's own VO2 estimate already
   proved these two clocks can differ by orders of magnitude; conflating
   them here would repeat, not extend, that lesson. Explicitly capped: one
   back-of-envelope estimate per applicable row, no FDTD/sidecar rebuild.

**Search methodology (identical discipline to exp-036, with this cycle's
corrections):** review-level sources prioritized, ≥2 independent sources
per figure where the literature supports it; CW-vs-pulsed fluence
discipline explicit for every irradiance figure; forward AND reverse
switching times both required, reported at the electronic/optical clock
AND (per THERMO's fix) checked against a separate lattice-thermal clock
where a real absorbed-power event is involved; every leg must log a
genuine WebFetch attempt regardless of exp-036's own prior-cycle blockage
(Red Team's fix — no self-fulfilling tooling assumption). Wavelength-
tagging applied prospectively to every figure this cycle extracts
(exp-036's own unexecuted fix, applied here going forward — retroactive
application to exp-036's four rows stays PLAN.md's separately-queued
priority #2, named not silently dropped).

## T1 escape-route statement

All six rows bear on **σ(I)**. Applying T17's existing kinetics framework
— corrected this cycle per EM's Phase-2 fix, Red-Team-confirmed via direct
derivation:

- **TPA-cascade FCA, ENZ (band-filling)**: threshold-gated generation,
  k_f(I_ambient) negligible at low intensity — memoryless, N/A for at-rest,
  same structural bucket LOGBOOK already accepts for standalone RSA/TPA.
- **Linearly-pumped FCA**: k_f(I) has no intensity threshold — generation
  proportional to absorbed flux at any intensity, ambient included. This is
  **not** a fourth kinetics category or a claim the mechanism fails to
  qualify as a T1 escape route — it is the SAME n_ss = k_f(I_ambient)/
  (k_f(I_ambient)+k_r) formula T17 already established, evaluated in a
  magnitude regime (non-negligible k_f(I_ambient)) this program has not
  previously computed. For fast recombination (k_r large, ns-scale), the
  formula reduces to ordinary instantaneous σ(I) tracking — ordinary
  memoryless D_req/irradiance scoring, expressed through rate constants
  instead of a phenomenological curve, not a structurally different
  category. For any long-lifetime host found, the formula is evaluated
  directly, not assumed small or dismissed.
- **Combined SA+RSA media**: inherits whichever RSA component is used.
  Fast-triplet component → memoryless, N/A. Long-triplet-lifetime component
  (exp-036's own found subclass, 1–21+ s reverse rates) → scored via the
  identical n_ss formula above, using that subclass's own measured k_r —
  the same formula, not a separately-decreed "hysteretic" bucket.

## Predicted outcomes (falsifiable bands, committed BEFORE any search)

| Row | D_req (≥890–1180× corrected, where the correction is confirmed to apply) | Irradiance (≤10⁻² W/cm²) | Switching speed (carrier/optical clock, then lattice-thermal clock, both provisional vs T3) | Constraint-3-at-rest (n_ss via T17 formula, reported only per VISION's cap) | **Predicted verdict** |
|---|---|---|---|---|---|
| **TPA-cascade FCA** (analytic, not a search leg) | Predict NO, algebraically forced — inherits exp-036's own already-cited TPA figures | Predict NO — same ~10⁷–10⁸ W/cm² onset, 9–11 OOM gap, by construction (a TPA-seeded cascade cannot activate below its own seed threshold) | Predict YES electronic clock (sub-ns/ns–µs); lattice-thermal clock not separately estimated (row already fails independently, THERMO's estimate not spent here) | N/A — threshold-gated | **unobtainium**, derived not searched |
| **Linearly-pumped FCA** (doped Si/Ge) | Predict NO — modest carrier-density-dependent absorption, order-short like RSA, **correction applicability not assumed** (QUANTUM's deprioritized-but-not-waived flag) | Predict YES, clears easily — ordinary photoconductive response well below 10⁻³ W/cm² | Predict fast electronic clock (ns) for clean hosts; **genuinely open** for any longer-lifetime host found — not assumed either direction; lattice-thermal clock estimated by THERMO if a real absorbed-power event is found | Predict n_ss computed as small for fast-recombination hosts (τ_recomb~ns), **reported per VISION's cap**: real chemistry/physics finding, visual significance unverified, not a scored constraint-3 violation, unless carried through T2's C_thr(L) — no "confirmed real risk" language regardless of the computed number | **Structural finding, precisely framed**: this row is scored via T17's existing formula, not disqualified as a non-gate; predicted verdict is memoryless-D_req-style failure (NO) with a genuinely open at-rest question for any long-lifetime host, held to VISION's language cap throughout |
| **ENZ band-filling** (ITO, AZO/GZO) | Predict **the disaggregation step rules this inapplicable or radically reduced** — if the cited "unity-order" figure is dominantly Δε_real (predicted), it does not reduce to a D_req comparison at all; if a genuine Δε_imag component is separately reported, predict it is far below the corrected bar | Predict NO — ultrafast strong-pump demonstrations, comparable to or worse than TPA's gap | Predict YES both directions, clears easily — sub-ps recovery is ENZ ITO's celebrated feature (electronic clock only; no real sustained absorbed-power event predicted, so lattice-thermal clock not separately estimated) | N/A — pump-threshold-gated | **Unobtainium-with-a-wavelength-and-mechanism-class disqualifier**: predict the row fails on wavelength (near-IR ENZ point, outside 450/600/750nm and a white flashlight's visible spectrum) AND, pending the disaggregation step, may not be a σ(I) row at all — a genuinely new failure mode, not previously seen in this program's realizability checks. One-line constraint-2 disclosure required regardless of outcome. |
| **Graphene** (control) | N/A — predict confirmed wrong-direction (saturable, not reverse-saturable) | N/A | N/A | N/A | **Wrong mechanism direction, confirmed not assumed** |
| **Combined SA+RSA media** (tandem, dyad, composite) | Predict NO for directly-published composite figures if found (net ratio bounded by the better standalone component, not multiplied by combination); **explicitly flagged lower-confidence** if the search must fall back to algebraic combination of two separate papers' numbers | Predict conditional — clears if built on exp-036's own low-threshold long-triplet RSA subclass, open otherwise; not a clean class-level YES | Predict inherits the SLOWER component's reset if long-triplet-RSA-based (same tradeoff exp-036 found for standalone RSA); clears if built on classic fast-RSA + fast-SA | Predict CONDITIONAL, scored via the SAME T17 n_ss formula as row 2 if the long-triplet-RSA branch is used (not a separately-decreed bucket); N/A otherwise; **reported per VISION's cap** | **published-partial at best** — predict no published architecture clears this program's four-way bound; real combined-media literature is motivated by roll-over suppression/dynamic-range broadening for laser protection, a different design goal — a "motivation mismatch" finding, evidentiary tier disclosed per-row (composite-figure-found vs. algebraically-combined) |

**Program-level pre-registered prediction:** no row clears all bounds
simultaneously. Five to six structurally distinct failure modes predicted:
TPA-cascade (irradiance, derived); linearly-pumped FCA (dynamic range, with
a genuinely open, T17-formula-scored at-rest question, not a disqualified-
gate claim); ENZ (wavelength, PLUS a possible mechanism-class
disqualification pending the Δε disaggregation — potentially the most
novel finding of the cycle); combined media (published-partial, motivation
mismatch, evidentiary-tier-disclosed). **On Checkpoint criterion 2**: per
Red Team's fix, this cycle makes NO tooling-availability prediction in this
table. The honest, purely physics-grounded statement is: if every row here
fails cleanly and is disclosed as such, this cycle brings the program to
*zero remaining named-but-untested mechanism classes* for the first time —
a genuine, significant threshold, independent of what evidentiary tier this
cycle's own search actually reaches. Whether criterion 2 fires depends on
that evidentiary tier (primary-source-verified vs. snippet-synthesis,
determined honestly at Phase 4, not assumed here) and on whether Phase 5
finds this cycle's own scoping (six named rows) exhaustive enough within
the classes named — both live, undetermined questions this table does not
pre-answer.

## Idealizations

- Proprietary/unpublished materials invisible to this check by
  construction.
- Exotic/engineered composite or metamaterial-hybrid media beyond the
  three named combined-media architectures remain out of scope — a
  materials-engineering-roadmap boundary, not resolved here (unchanged
  from exp-036's own capping, reaffirmed by Red Team against a specific
  attempt to reopen it this cycle).
- The switching-speed band (10ms–1s) remains unsourced; every speed
  verdict flagged provisional pending T3.
- **Combined-media dynamic-range figures are evidentiary-tier-disclosed
  per row**: a directly-published composite/tandem figure is trusted as
  reported; a figure produced by algebraically combining two separately-
  published single-material numbers is explicitly flagged as the weaker
  tier (interface effects, energy transfer between stacked/blended
  components, and fabrication-specific loss are all invisible to a desk
  combination).
- Linearly-pumped FCA's and the long-triplet-RSA combined-media branch's
  n_ss estimates are back-of-envelope k_f/k_r computations from published
  generation/recombination figures, not rigorous rate-equation solves —
  order-of-magnitude only (same discipline as THERMO's exp-036 VO2
  estimate).
- THERMODYNAMICS' capped estimate is one analytic calculation per
  applicable row, explicitly barred from becoming a THERMO-sidecar
  rebuild or a new FDTD thread.
- **This cycle makes no prediction about its own evidentiary tier**
  (Red Team's fix) — whether WebFetch succeeds or every leg falls back to
  WebSearch-snippet synthesis is determined honestly at Phase 4 and
  disclosed there, not assumed here regardless of exp-036's own prior
  blockage.
- This is a search (plus capped analytic estimates), not a lab measurement
  or formal meta-analysis; no extracted number is independently
  re-verified beyond the ≥2-source convergence bar; publication bias could
  bias any row's apparent ceiling upward.
- English-language, freely-accessible-source bias, same as exp-036.
- MATERIALS' field-enhancement-factor arithmetic is a zero-cost derivation
  from this cycle's own extracted figures, not a rigorous engineering
  feasibility study of any specific plasmonic/cavity structure.
- Every at-rest/coloration finding this cycle produces is reported per
  VISION's mandatory pre-registered cap: "real chemistry/physics, visual
  significance unverified — not yet a scored constraint-3 violation,"
  unless actually carried through T2's C_thr(L) at Tier-W ambient first.
  No risk/confirmed/non-negligible language attaches to an uncarried
  population or absorption fraction, regardless of its computed magnitude.
- Wavelength-tagging discipline applied prospectively to this cycle's own
  new figures only; exp-036's own four already-published rows remain
  untagged, explicitly deferred (not silently dropped) to PLAN.md's
  separately-queued Iteration-14 priority #2.

## Cost note

Zero FDTD calls. No `lab/` engine changes; no trust-suite re-run required.
Three dedicated search legs (linearly-pumped FCA; ENZ + graphene control;
combined SA+RSA media), plus two zero-cost analytic derivations
(TPA-cascade FCA; MATERIALS' field-enhancement arithmetic) and one capped
post-search analytic estimate (THERMO). Comparable total search effort to
exp-036 despite six named rows, because two of six are derived rather than
searched (Red Team's cost-discipline recommendation, adopted).
