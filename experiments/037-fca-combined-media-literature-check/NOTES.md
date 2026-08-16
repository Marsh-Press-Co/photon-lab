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

Full verbatim proposal: this shift's session record. Five top-level rows
(a sixth and seventh item in the numbered parameter table below are
derived analytic add-ons, not scored rows — corrected same-shift, Red
Team audit, docket #17): **TPA-generated/cascade FCA** (Si, GaAs, ZnSe,
CdS — threshold-gated carrier generation riding on a TPA seed event),
**linearly-pumped (photoconductive) FCA** (doped Si, doped Ge — carrier
generation with NO intensity threshold, proportional to absorbed flux at
any intensity, ambient included), **epsilon-near-zero (ENZ) band-filling
nonlinearity** (ITO, AZO, GZO — intraband/Drude nonparabolicity
absorption/index shift at a TCO's ENZ point, per Alam et al. — corrected
same-shift from the original "Burstein-Moss-type" label, Red Team audit
docket #17; Burstein-Moss is the classical interband band-filling
mechanism, distinct from the intraband free-carrier effect the recovered
literature actually attributes this nonlinearity to), **graphene**
(control/boundary case — textbook saturable absorber,
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

**Five rows scored separately (D_req/irradiance/switching-speed/at-rest),
plus two derived analytic add-ons (items 6–7, not scored rows), with the
mandatory-fix corrections folded in before any search runs — the "six
rows" count in the cost note and Hypothesis above referred loosely to the
numbered list below, not five scored rows; corrected same-shift, Red Team
audit docket #17:**

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

## Phase 4 — Results (exp-037, 2026-08-16)

Three parallel WebSearch-grounded search legs (Leg A: linearly-pumped FCA;
Leg B: ENZ + graphene control; Leg C: combined SA+RSA media), run by fresh
sub-agents against the pre-registered predictions above, plus two zero-cost
analytic derivations (TPA-cascade FCA; MATERIALS' field-enhancement
arithmetic) and one capped post-search THERMO estimate, done directly by
the Director using the legs' own extracted numbers.

**⚠ Methodology disclosure, per Red Team's fix — genuinely re-attempted,
not assumed.** All three legs made real WebFetch attempts on promising
primary/secondary sources before falling back to snippet synthesis: Leg A,
11 attempts across 11 domains; Leg B, 10 attempts across 10 domains; Leg C,
18 attempts across 16 domains. **Every single attempt across all three
legs returned `EGRESS_BLOCKED`** — the same total-blockage pattern exp-036
found, now independently re-confirmed rather than inherited as an
assumption, exactly as Red Team's fix required. Every figure below is
WebSearch-snippet synthesis, not independently-read primary-source tables
— the same "sourced-but-unverified" evidentiary tier as exp-036.

### TPA-cascade FCA — derived analytically (Si, GaAs, ZnSe, CdS)

Not searched, per Red Team's cost-discipline recommendation (adopted at
Phase 3): a TPA-generated free-carrier cascade requires the seed two-photon
event to occur before any carrier population — and therefore any FCA tail
absorption — exists at all. Since the seed TPA event's own onset threshold
is already established in this program's record at ~10⁷–10⁸ W/cm²
(exp-036, citing Sheik-Bahae/Van Stryland's foundational semiconductor-TPA
database, He et al. *Opt. Lett.* 20, 435 (1995), and ZnSe/GaAs Z-scan
studies), the cascade's own irradiance gate is bounded below by that same
threshold — no independent, lower-threshold generation channel exists for
this row. The classical "TPA+FCA" semiconductor optical-limiting
literature (the Van-Stryland-group lineage this row's named hosts come
from) uses the free-carrier tail to *extend the temporal duration and
sharpen the roll-over* of an already-triggered limiting response, not to
lower the triggering threshold itself — the carrier population is a
downstream consequence of the TPA event, not a parallel generation
pathway.

**⚠ Same-shift correction, Red Team Phase-5 audit docket #1 (independently
caught by both PHOTONICS Phase-5 passes and MATERIALS): this row's own
named host list is not wavelength-self-consistent with this program's
450/600/750nm sweep, and was never checked against it (the exact
wavelength-tagging gap this cycle committed to closing, recurring for a
second consecutive cycle).** Photon energies at the sweep wavelengths are
2.755/2.066/1.653 eV. Si (E_g=1.12eV↔1107nm) and GaAs (E_g=1.42eV↔873nm)
are ABOVE-bandgap — ordinary linear interband absorbers, not TPA-transparent
hosts — at ALL THREE sweep wavelengths; the classic Si/GaAs TPA Z-scan
literature this row's host list is inherited from operates near 800–1550nm,
outside this program's visible test band entirely. ZnSe (E_g≈2.7eV↔459nm)
and CdS (E_g≈2.42eV↔512nm) are genuinely TPA-relevant only at 600/750nm;
at 450nm ZnSe's own photon energy (2.755eV) sits at or above its gap. This
does not change the row's verdict — the irradiance gate is set by the TPA
process itself (9–11 OOM above the ceiling regardless of host), not by
which named host is used — but the row's premise as stated was physically
incoherent for its own named materials. Queued for Iteration 15 (PLAN.md
priority #2, folded in): re-anchor to genuinely below-bandgap-at-sweep
hosts (ZnSe/CdS at the red end; a wider-gap material needed for 450nm), or
explicitly caveat the inherited onset figure as sourced at a different
operating-wavelength regime.

**Dynamic range**: bounded by the same physics — no independent
mechanism exists to clear D_req below the TPA threshold, predicted NO,
confirmed by construction. **Irradiance**: NO, same ~10⁷–10⁸ W/cm² onset
(sourced at near-IR/telecom pump wavelengths in the cited literature, not
independently re-verified at 450/600/750nm — see the host-wavelength
correction above), 9–11 OOM above both the ≤10⁻² W/cm² Checkpoint-2 margin
and the ~10⁻³ W/cm² witness estimate — identical to exp-036's own
established TPA figure, inherited not re-derived. **Switching speed
(electronic clock, provisional pending T3 — stage-10's temporal-contrast
instrument remains unbuilt, so this "clears" verdict is a comparison
against an unsourced band, not a settled perceptual finding)**: YES both
directions — TPA generation is sub-ps (virtual-state process, exp-036's
own established figure), and FCA carrier lifetimes in these specific hosts
(Si, GaAs, ZnSe, CdS) are reported in the ns–µs range in the broader
semiconductor-photonics literature (consistent with, though not
independently re-verified against, this cycle's own Leg A findings for Si
specifically) — clears the 10ms–1s window comfortably, provisional as
above. Lattice-thermal
clock not separately estimated (THERMO's capped estimate reserved for rows
with a genuine ambient/near-threshold absorbed-power question — see below;
this row already fails independently on irradiance by 9–11 OOM, so the
distinction is moot). **Constraint-3-at-rest**: N/A — threshold-gated,
k_f(I_ambient) is the same negligible quantity that already earns
standalone TPA its N/A rating (exp-036). **Absorption-only correction**:
capped/deprioritized per Red Team's split ruling — not computed, does not
gate the verdict. **Row verdict: unobtainium, derived not searched — every
predicted sub-finding confirmed by construction from exp-036's own
already-established TPA figures.**

### Linearly-pumped (photoconductive) FCA — Search Leg A results (doped Si, doped Ge)

Full verbatim leg report: this shift's session record. **Dynamic range
(Si)**: a genuine quantitative anchor recovered — Soref & Bennett, *IEEE
J. Quantum Electron.* QE-23, 123–129 (1987), the field-standard empirical
free-carrier absorption relation (σ_e ≈ 8.5×10⁻¹⁸ cm², σ_h ≈ 6.0×10⁻¹⁸
cm² per carrier). **⚠ Same-shift correction, Red Team Phase-5 audit
docket #2 (independently caught by both PHOTONICS Phase-5 passes and
MATERIALS): these are telecom-wavelength coefficients (fit near 1.3–1.55
µm), applied below unscaled at 600 nm with no wavelength tag** — the
cycle's own committed wavelength-tagging discipline was not executed for
this row's single most load-bearing number. Free-carrier absorption
cross-sections scale with wavelength (Drude-type, roughly σ∝λ^1.5–3), so
using the longer-wavelength figure at 600nm likely OVERESTIMATES the true
visible-band cross-section — a conservative direction for the NO verdict
below (correcting it would make the shortfall worse, not better), but
undisclosed as originally written; disclosed here, not yet corrected with
an actual visible-band figure (queued, PLAN.md priority #2). A
back-of-envelope σ_on/σ_off built from this (uncorrected) figure (own
construction, order-of-magnitude only, every assumption stated) finds
**D_req is NOT cleared across the entire physically reasonable doping
range** — a fast host (τ≈1ns) gives a ~1.1×10⁻⁷ shift (i.e., ~9 orders of
magnitude below the D_req bound); a long-lifetime host (τ≈1ms,
N_D=10¹⁷cm⁻³) gives only ~1.11× (roughly 3 orders of magnitude short of
D_req≥540–600×); even at aggressively low doping (N_D=10¹³–10¹⁴cm⁻³) the
ratio only approaches ~100×, still short. **CONFIRMS the pre-registered
NO**, with the exact shortfall shown to be a genuinely N_D-sensitive open
dependency, not a single fixed number. **MATERIALS realizability tier
(added same-shift, Red Team docket #10 — the original text omitted this
row's tier label though every other row received one): UNOBTANIUM-WITH-
PARAMETERS** — the shortfall (1–9 orders of magnitude depending on doping)
is a quantified, parameter-stated gap against a named, real material
(doped silicon), not a bare assertion.
Germanium: qualitative-only ("significantly stronger than Si," multiply
sourced) — no numeric cross-section recovered, an honest data gap, same
order-of-magnitude shortfall inferred by extrapolation from Si, not
independently sourced. **Absorption-only correction applicability: left
explicitly OPEN**, per QUANTUM's flagged question — no source found either
confirming or ruling out whether the exp-036 molecular correction (÷0.51–
0.61, calibrated for dielectric/bound-electron extinction) applies to
Drude-type free-carrier absorption; neither applied nor silently skipped.

**Irradiance**: **CONFIRMS the pre-registered YES**, clears by many orders
of magnitude — ordinary photoconductive absorption has no intensity
threshold (structurally, and confirmed via commercial Si/Ge photodiode
responsivity figures operating linearly to the shot-noise floor).

**Switching speed, both clocks (provisional pending T3 — stage-10's
temporal-contrast instrument remains unbuilt; the ranges below are
comparisons against an unsourced 10ms–1s band, not settled perceptual
findings)**: electronic/carrier clock — Si spans
~1ns (heavily-doped/defect-engineered, e.g. gold-hyperdoped) to ~1ms
(high-purity/lightly-doped); Ge, a directly-sourced resistivity-dependence
dataset gives ~30ns (0.01 Ω·cm, heavily doped) to ~500µs (40 Ω·cm,
high-purity). **Leg A caught and corrected a real error in this cycle's
own pre-registration**: the parenthetical expectation that "clean
semiconductor→fast, doped/defect-rich→slow" runs backward from what both
sourced datasets show — ordinary Shockley-Read-Hall physics has it the
other way (more recombination centers from doping/defects → SHORTER
lifetime, i.e. FASTER; higher purity → LONGER lifetime, i.e. slower).
Flagged and corrected in the record here, not silently absorbed. Lattice-
thermal clock reserved for THERMO's estimate, below.

**Constraint-3-at-rest, via T17's existing n_ss formula (EM's corrected
framing, applied as committed)**: using I_ambient≈10⁻⁵ W/cm² (sourced
indoor-lighting range, 50–500 lux), α_interband(Si,600nm)≈3.7×10³cm⁻¹ (not
independently WebFetch-verified this session, flagged), N_D=10¹⁷cm⁻³: fast
host (τ=1ns) gives n_ss≈1.1×10⁻⁹; long-lifetime host (τ=1ms)
gives n_ss≈1.1×10⁻³, rising toward ~0.1 at lower, still-plausible doping
(N_D=10¹⁵cm⁻³) — **genuinely open, doping-sensitive, exactly as
pre-registered.** Leg A flagged its own normalization choice (n_ss
referenced to dopant density N_D, since free-carrier photogeneration draws
from an unbounded valence-band reservoir with no natural "1" to saturate
toward, unlike T17's original bounded two-level population) as an open
methodological gap, not an established result. **⚠ Same-shift correction,
Red Team Phase-5 audit docket #14 (VISION's own catch): the word
"negligible," used above for the fast-host figure, is struck** — it is not
on the mandatory cap's literal banned list (only "confirmed"/"risk"/
"non-negligible" were named), but it is the same species of unearned
magnitude-significance judgment on a raw, uncarried number the cap exists
to forbid, just pointed in the reassuring direction instead of the
alarming one. **Reported strictly per VISION's mandatory cap, now
including "negligible"/"small"/"trivial" among the struck terms**: real
chemistry/physics, visual significance unverified, not yet a scored
constraint-3 violation — no unearned magnitude-significance language of
any kind attaches to these raw n_ss values regardless of how small or
large they compute.

**Row verdict: matches the pre-registered structure in full** — D_req NO
(quantitatively confirmed for Si, qualitatively consistent for Ge, upper-
bound-biased per the wavelength-scaling caveat above), YES irradiance, an
electronic clock spanning fast-to-slow hosts (with the fast/slow-host
material-purity direction corrected against the pre-registration's own
unverified assumption), and a genuinely open, doping-sensitive at-rest
finding scored via T17's existing formula and held to VISION's language
cap throughout — not a disqualified-gate claim, exactly as EM's Phase-2
fix required. **⚠ Same-shift addition, Red Team Phase-5 audit docket #7
(EM's own Phase-5 catch): "the SAME formula" is precise only as "the same
formula's small-signal limit."** T17's n_ss=k_f/(k_f+k_r) is a logistic
form derived for a bounded two-state population; doped-Si photoconductive
FCA is properly governed by a linear relaxation ODE (dn/dt=G(I)−n/τ,
n_ss=G·τ, no saturating denominator at all, since carrier generation draws
from an effectively unbounded band reservoir rather than a fixed two-level
system). The linear and logistic forms agree only in the small-signal
limit k_f≪k_r — the regime every n_ss value reported above sits in
(max≈0.1) — so none of the numbers here are compromised, but if a future
cycle's host/doping choice pushes n_ss toward O(1), the two forms diverge
and which one actually governs becomes load-bearing, not cosmetic.

### Epsilon-near-zero (ENZ) band-filling nonlinearity — Search Leg B results (ITO, AZO; GZO data gap)

Full verbatim leg report: this shift's session record. **Δε
disaggregation (QUANTUM's elevated mandatory pre-scoring step)**: the
headline "unity-order permittivity change" is **confirmed dominantly
REFRACTIVE (Δε_real)** — Alam, De Leon & Boyd, *Science* 352, 795–797
(2016), the canonical ENZ-ITO reference: Δn=0.72±0.025 at λ_ENZ=1240nm,
n₂≈0.11 cm²/GW, a Kerr/intraband-nonparabolicity index effect, corroborated
independently on AZO by Caspani et al., *Phys. Rev. Lett.* 116, 233901
(2016). **Per this program's expressibility contract, this dominant effect
does NOT reduce to a σ(I)/D_req absorption-ratio comparison** — ruled, not
assumed, exactly as QUANTUM's fix required. A genuine, SEPARATE Δε_imag
(absorptive) branch was found, not assumed absent: *Photonics Research*
Z-scan work on ITO shows an SA→RSA crossover at 1030nm driven by
three-photon absorption (χ⁽⁵⁾) at high intensity — but no paired on/off
ratio table was recoverable given the WebFetch blockage, so **no D_req
number is forced onto it; reported genuinely OPEN**, with the higher-order
(5th-order) nonlinearity noted as expected to fail irradiance even more
decisively than the refractive branch, though not quantified this cycle.

**Constraint-2 disclosure (Red Team's fix), delivered, strengthened
same-shift (Red Team Phase-5 audit docket #16, independently raised by
both PHOTONICS and EM)**: ENZ ITO/AZO metafilms document anomalous
reflectivity — up to ~15 percentage-point reflectance swings at the ENZ
point, plus generic Brewster/Berreman singular-reflection modes near the
near-zero-index condition. This is not merely an empirical footnote —
it is a first-principles consequence of impedance bookkeeping (EM's
Phase-5 point): as ε→0, wave impedance Z=√(μ/ε)→∞, producing intrinsic,
large impedance mismatch to free space; near-unity reflectance is the
textbook-generic expectation approaching the ENZ point away from any
narrow absorption dip, a stronger risk than the "~15pp swing" figure
alone conveys. A real, sourced, non-verdict-changing disclosure (the row
fails independently on wavelength regardless).

**Wavelength**: ITO's ENZ point sits at λ≈1200–1550nm (tunable via
doping/annealing); AZO's at ~1300nm. **CONFIRMS the predicted
disqualification** — entirely outside this program's 450/600/750nm sweep
and a white flashlight's ~400–700nm visible emission.

**Irradiance**: every demonstration found is femtosecond-pulsed (no CW
figure found or conflated), peak intensities in the GW/cm² range (1.2–140
GW/cm² across cited variants). **CONFIRMS NO** — ~11–14 orders of
magnitude above both bounds, comparable to or worse than TPA's own 9–11
OOM gap, exactly as predicted.

**Switching speed (provisional pending T3 — stage-10's temporal-contrast
instrument remains unbuilt, so this is a comparison against an unsourced
band, not a settled perceptual finding)**: reverse ≈360fs (Alam et al.);
forward tracks the pump envelope (fs-scale). **CONFIRMS YES both
directions**, clears the 10ms–1s window by many orders of magnitude,
provisional as above.

**Row verdict: unobtainium-with-a-wavelength-and-mechanism-class
disqualifier, confirmed, with one item left genuinely open** (the Δε_imag
branch's own magnitude) rather than forced — the row's overall
disqualification does not depend on resolving that open item, since
wavelength alone is decisive. **The mechanism-class disqualification
itself is a new INSTANCE of an already-established program principle, not
a new category** — see the Learned section's same-shift correction, Red
Team Phase-5 audit docket #5 (independently caught by both QUANTUM OPTICS
and ELECTROMAGNETISM).

### Graphene — control case (Search Leg B)

**CONFIRMED wrong-direction, as predicted**: textbook saturable absorber
via Pauli blocking (Bao et al., *Adv. Funct. Mater.* 19, 3077 (2009);
mechanism confirmed in *Phys. Rev. B* 95, 125408 (2017)). One genuine
exception found, not assumed absent: doped graphene at photon energies
below 2×the Fermi level can show two-photon-absorption-driven induced
absorption overpowering the SA effect (*Appl. Phys. Lett.* 114, 091111
(2019)) — but this requires deliberate Fermi-level doping and sits in the
mid-IR, not representative of undoped graphene at this program's visible
operating wavelengths. Cavity-coupled/heterostructure configurations found
this leg all *enhance* the SA effect (lower saturation intensity ~65%),
none reverse its sign. **Standard direction confirmed representative for
this program's regime.**

### Combined saturable/RSA media — Search Leg C results (three named architectures)

Full verbatim leg report: this shift's session record. **Search-order
discipline (Red Team's fix) applied and disclosed per architecture, not
blanketed**: Architectures 1 (tandem/cascaded SA+RSA) and 3
(composite/blended fullerene+CNT/polymer) both found genuine,
multiply-sourced, directly-published composite dynamic-range claims — the
primary evidentiary tier, no fallback needed. Architecture 2
(single-molecule/dyad RSA+TPA) surfaced a genuine THIRD case the
pre-registration did not anticipate: a real, published, energy-transfer-
coupled combined mechanism (Joshi et al., *Opt. Lett.* 23(22), 1742
(1998), AF-380 TPA dye + C60 RSA) and a genuinely single-molecule
RSA+TPA chromophore (meso-(2-thienyl)porphyrin, RSA@532nm/TPA@800nm) —
but no usable composite dynamic-range multiplier recoverable for either,
and no clean fallback pair either (the matched standalone-component
figures needed for algebraic combination were themselves unrecoverable
given the WebFetch blockage). Disclosed as its own evidentiary gap, not
forced into either predicted tier.

**Dynamic range, all three architectures: CONFIRMED NO.** Best composite
figures recovered cluster **~10×–267×** — Architecture 1's graphene+SWNT
cascade (~10× threshold-ratio advantage) and cascaded-focus limiters
("orders of magnitude" qualitative, Van Stryland/Perry-group lineage);
Architecture 3's fullerene+CNT/polymer analogs (~10× device-level
clamp-to-damage ratio); a standalone-reference heavy-atom phthalocyanine
figure (~267× energy-limiting ratio, cited as RSA-class context, not this
row's own combined number). **⚠ Same-shift arithmetic correction, Red
Team Phase-5 audit docket #3 (PHOTONICS Pass 1's own catch, re-verified
here): the shortfall is ~0.65–2.1 orders of magnitude, not "2–4+" as
originally stated** — log₁₀(540–600×/10×)≈1.7–1.8, log₁₀(890–1180×/267×)
≈0.5–0.6. The direction (short of both bounds) and the qualitative
verdict (NO) are unaffected; the magnitude claim is corrected. Whether the
890–1180× absorption-only-corrected bound even applies is itself only
partially settled: **confirmed applicable to the molecular/π-conjugated
components** (phthalocyanines, C60, porphyrins — the same category
exp-036 validated the correction against), **but not re-derived for the
graphene/carbon-nanotube components of Architectures 1 and 3** — same-shift
disclosure, Red Team Phase-5 audit docket #12 (QUANTUM OPTICS' own catch):
graphene and CNTs are band-structure/Dirac-cone absorbers, not
discrete-state molecular chromophores, structurally closer to the carrier-
plasma category this cycle's own FCA/ENZ rows correctly left the
correction's applicability OPEN for. Applying the molecular correction to
these components without re-deriving it is inconsistent with how
carefully the correction was withheld two sections earlier in this same
document — not verdict-changing (the row fails 0.65–2.1 orders short even
uncorrected, before any correction is applied), but a real rigor gap,
queued for Iteration 15.

**Irradiance: genuinely OPEN, for a more basic reason than pre-registered.**
Every figure recovered across all three architectures is pulsed ns
fluence (mJ/cm²–J/cm²) — zero CW W/cm² composite figures found anywhere.
The predicted conditional structure ("clears if long-triplet-RSA-based,
open otherwise") presumed a binary that didn't materialize: **no tandem,
dyad, or blend architecture found in the literature is built on
exp-036's own long-triplet-lifetime RSA subclass (Hirata et al., 1–21+ s
reverse rates) at all** — that subclass appears only as a standalone
material, never yet incorporated into any combined architecture. The
"open otherwise" half of the prediction is confirmed correct, but because
no CW data exists for these architectures in the literature found, not
because a found CW value was ambiguous.

**Switching speed (provisional pending T3, as throughout this cycle's
other rows — stage-10's instrument remains unbuilt)**: every RSA
component identified across all three architectures (C60, phthalocyanines,
porphyrins, graphene/CNT) is drawn from the fast (ns–µs) RSA precedent
exp-036 already established, not the long-triplet subclass — the
classic-fast branch applies by elimination.
Composite-level forward/reverse numbers specifically were a data gap in
all three legs (a genuine, disclosed shortfall, not filled by inference).

**Constraint-3-at-rest: cleanly N/A, not open, not conditional** — per the
protocol's own instruction to state plainly when a computation cannot be
performed and why. No long-triplet-lifetime RSA component was found
embedded in any combined architecture; n_ss is therefore not computed for
this row, consistent with (not a violation of) EM's generalized fix.

**Row verdict: published-partial at best, motivation-mismatch — CONFIRMED
in full.** The literature's own stated purpose for all three architectures
(pulsed-laser-damage protection, dynamic-range/rollover extension against
intense transient events) is real, repeatedly attested, and categorically
different from this program's own question (suppressing a near-
imperceptible CW/ambient-level silhouette at ~10⁻³–10⁻² W/cm²) — exactly
the predicted mismatch.

### MATERIALS' field-enhancement-factor arithmetic (capped, derived — not a new search leg)

Per Red Team's capping ruling: a zero-cost arithmetic step converting bare
"unobtainium" verdicts into "unobtainium-with-parameters," per PANEL.md's
own Latitude rule, for the two rows whose failure is irradiance-dominated
by the largest margins (ENZ, TPA-cascade FCA). Published sub-wavelength
field-enhancement factors for plasmonic hot-spots/nanogap antennas and
cavity-coupled/critically-coupled resonators cluster in the ~10²–10⁴
intensity-enhancement range for robust, reproducible geometries, with
extreme nanogap/hotspot reports occasionally cited up to ~10⁵–10⁶ for
narrow, fragile configurations (order-of-magnitude figures from the
broader plasmonics literature, not independently re-verified this cycle
given the same WebFetch blockage affecting every other row).

**ENZ**: irradiance gap ≈11–14 OOM (GW/cm² demonstrated vs. ≤10⁻²/~10⁻³
W/cm² bounds). Even the most optimistic published enhancement factor
(~10⁵–10⁶) closes only 5–6 of the 11–14 orders — **a residual gap of
~5–9 orders of magnitude survives even under generous, non-robust
enhancement assumptions.** **TPA-cascade FCA**: irradiance gap ≈9–11 OOM
(inherited from TPA), same enhancement-factor ceiling applied — **residual
gap ~3–6 orders of magnitude.** Neither row is closed by any realistically
published field-enhancement figure; both remain unobtainium-with-
parameters in the chartered sense, not merely "unobtainium" by assertion.

**⚠ Same-shift addition, Red Team Phase-5 audit docket #11 (MATERIALS'
own catch): a third reason these rows stay unobtainium even under the
generous enhancement ceiling above, not just "the residual is large."**
Plasmonic hot-spot/nanogap field enhancement is confined to a
sub-wavelength mode volume, orders of magnitude smaller than the
macroscopic beam cross-section this program's mechanism needs to
attenuate — a locally-enhanced nanoscale hot-spot does not translate into
a macroscopically-effective absorption change over the interaction volume
a beam-terminating patch of space requires. It is also characteristically
narrowband (tens of nm FWHM), incompatible with this program's own
broadband 3λ (450/600/750nm) requirement. Both caveats compound, not
substitute for, the OOM residual gap above.

**⚠ Same-shift disclaimer, Red Team Phase-5 audit docket #13 (QUANTUM
OPTICS' own catch): this arithmetic does not re-legitimize ENZ as a σ(I)
candidate.** ENZ's own row above concludes its dominant nonlinearity is
refractive (Δε_real), not absorptive, and does not reduce to a D_req/
σ(I) comparison at all. This section applies the raw demonstrated GW/cm²
irradiance figures — real numbers, independent of what fraction of the
underlying effect is absorptive — purely as an order-of-magnitude
irradiance-gap exercise; it should not be read as reopening ENZ as a
viable σ(I) mechanism once field-enhanced.

**Explicitly capped**: this is order-of-magnitude arithmetic against
generic published enhancement-factor ranges, not a rigorous engineering
feasibility study of any specific plasmonic or cavity structure paired to
either mechanism — no source found or claimed showing these specific FCA/
ENZ subclasses have actually been demonstrated at field-enhanced
intensities; per the capping ruling, this is a negative-result note (no
such demonstration surfaced incidentally in any of the three search legs
run this cycle), not a dedicated new search.

### THERMODYNAMICS' capped analytic estimate (post-search, one estimate per applicable row)

Per Red Team's capping ruling: one back-of-envelope estimate, explicitly
barred from a sidecar rebuild or new FDTD thread, addressing THERMO's
Phase-2 fix (absorbed power → ΔT → emission band → detectability; carrier/
optical clock split from lattice-thermal clock).

**⚠ Same-shift replacement, Red Team Phase-5 audit docket #8 (THERMODYNAMICS'
own self-caught findings, ruled load-bearing not queueable — see the
Director's synthesis below).** The original text here was a qualitative
analogy to exp-036's VO2 estimate, not an actual computation, and
contained a genuine internal inconsistency (describing the same power-ratio
as both "five to six orders of magnitude" and "two further orders of
magnitude" one sentence apart — the correct figure, checked directly, is
two orders: 10⁻³/10⁻⁵ W/cm²). It also compared a TIME (VO2's heating time
to cross a discrete phase-transition threshold) to a TEMPERATURE (FCA's
implied steady-state rise), a category error — those are not the same
physical quantity and do not obey the same power-scaling law. Replaced
below with an actual minimal computation using silicon's own standard
thermal constants, at zero marginal search cost, per Red Team's ruling
that "capped" means less work by design, not skipping the computation
entirely.

**Linearly-pumped FCA's at-rest population (row 2) — actual estimate.**
Using silicon's standard cited thermal constants (ρ≈2330 kg/m³, c_p≈700
J/(kg·K), κ≈148 W/(m·K)) and a simple steady-state surface energy balance
(absorbed power = re-radiated + convected power, P_abs = h·ΔT, with a
generic combined radiative+convective heat-transfer coefficient h≈10–20
W/(m²·K), typical for a small object in ambient air — order-of-magnitude
only, no specific geometry beyond a flat absorbing surface): at Leg A's
own I_ambient≈10⁻⁵ W/cm² = 0.1 W/m² (near-total absorption within ~2.7µm
of the surface, from Leg A's own α_interband figure), **ΔT_ss ≈
0.1/15 ≈ 7 millikelvin.** Emission band: at ΔT~7mK above a ~300K ambient,
the Planck/Wien peak shift from the unperturbed ~9.7µm blackbody peak is
negligible — consistent with, and confirming numerically for the first
time, T5's own standing ~10µm pin. Detectability: state-of-the-art
uncooled microbolometer thermal cameras have a noise-equivalent
temperature difference (NETD) of order 20–50 mK; a 7mK rise sits below
even the best commercial NETD by a factor of ~3–7×, not by orders of
magnitude — a real, quantified, but not overwhelming margin, sharper and
more honest than the original "far below" qualitative language. **No
detectable thermal signature is expected**, now shown by computation, with
an explicit margin rather than asserted by analogy. (For comparison,
at exp-036's own flashlight-level 10⁻³ W/cm²=10 W/m², the identical
formula gives ΔT_ss≈10/15≈0.7K — a genuinely different, non-negligible
steady-state rise at that power level, consistent with VO2's own
conclusion that the flashlight-power regime is thermally consequential,
though VO2's own finding was about crossing a discrete threshold, not
this steady-state figure.)

**ON-state absorption events, TPA-cascade FCA and ENZ-ITO FCA (rows 1, 3)
— reworded, Red Team Phase-5 audit docket #6 (independently caught as an
overclaim by both ELECTROMAGNETISM and QUANTUM OPTICS).** The original
"categorical source-mismatch... independent of and prior to any
ΔT/detectability computation" framing overstated its own epistemic status:
"CW" describes only temporal structure, not spatial concentration — a CW
source, focused and sub-wavelength-field-enhanced (the SAME plasmonic/
cavity enhancement MATERIALS' own section above quantifies), is in
principle a route to high LOCAL instantaneous intensity from a genuinely
CW source; the claim as originally stated is directly in tension with
that same section of this document, not independent of it. **The sound
version is an energy-conservation/sustained-power argument, not a
categorical-and-prior one**: both mechanisms are demonstrated in the
literature (this cycle's own Leg B findings, and exp-036's own established
TPA figures) only under **pulsed** excitation at GW/cm²-class peak
intensities, femtosecond-to-nanosecond durations. Reaching that peak
intensity CONTINUOUSLY (not for fs–ns but indefinitely, since a flashlight
sweep does not pulse) from a ~1W-class total source, at ANY of the field-
enhancement factors MATERIALS' own section finds published (up to
~10⁵–10⁶×), remains arithmetically short by the same 3–9 order-of-magnitude
residual MATERIALS already computed — this is a restatement and
reinforcement of the independently-established irradiance/field-
enhancement bookkeeping above, not a separate, prior finding. If a
pathological, briefly-achieved local concentration were somehow reached
despite that residual gap, it would deposit continuous absorbed power
into a tiny volume and produce a visible hot-spot/damage signature — a
WORSE constraint-3 failure (more conspicuous), not a clean escape. This
reinforces, and is fully reconciled with, both rows' independently-
established irradiance failures — it does not stand as an independent,
prior argument.

## Learned

**Program-level pre-registered prediction CONFIRMED**: no row clears all
bounds simultaneously. **Five structurally distinct failure modes
confirmed**, sharper and more precisely characterized than the
pre-registration itself predicted in several places: TPA-cascade FCA
(irradiance, algebraically inherited from TPA, derived not searched — with
a same-shift-disclosed host-wavelength caveat, see Results); linearly-pumped
FCA (dynamic range, quantitatively confirmed via a real literature
cross-section for the first time this program has attempted this row-type,
with a genuinely open — not disqualified, not assumed — at-rest finding
scored through T17's existing formula exactly as EM's Phase-2 fix
required, now also given an explicit MATERIALS realizability tier and an
actual THERMO thermal estimate); ENZ (a mechanism-class/expressibility
disqualification — the headline nonlinearity is refractive, not
absorptive, and does not reduce to a σ(I) row at all — compounded by, not
merely coincident with, a decisive wavelength disqualification); combined
media (published-partial, motivation-mismatch, with real composite
dynamic-range figures found and scored, shortfall corrected to ~0.65–2.1
orders of magnitude, not "2–4+"). **Graphene's control case holds without
qualification**, with one honestly-disclosed, non-representative exception
(doped/mid-IR TPA-over-SA).

**⚠ Same-shift correction, Red Team Phase-5 audit docket #4 (Red Team's
own direct verification against REALIZABILITY_MEMO.md): "all six named
classes from REALIZABILITY_MEMO.md have now been checked" is FALSE AS
WRITTEN.** Read directly: the memo's own "Idealizations and honest
limits" section evaluates only RSA and TPA and names, as not-yet-evaluated,
exactly three further items — free-carrier absorption, photochromic
switching, and combined saturable/RSA media — five classes total ever
named by the memo, not six. Photothermal/VO2 is a THERMO-driven split of
"photochromic" performed at Iteration 13 (exp-036's own mandatory fix)
that was never folded back into the memo's own taxonomy (itself docket
#9's own finding, below). Neither ENZ nor graphene appears anywhere in the
memo — **ENZ is a genuinely new row this cycle's own Phase-1 proposal
introduced, not a previously-tracked gap being closed.** The accurate,
narrower claim: **this cycle closes the two classes LOGBOOK.md's own
Iteration-13 close explicitly named as remaining untested (free-carrier
absorption, combined saturable/RSA media)**, and additionally introduces
ENZ and graphene as new rows of this cycle's own devising. Even under this
corrected, narrower framing, **Checkpoint criterion 2 still does NOT
fire, for the reason this cycle's own text already gives as sufficient on
its own**: the evidentiary tier across all three legs (39/39 WebFetch
attempts EGRESS_BLOCKED, independently re-confirmed rather than inherited
as assumption) remains WebSearch-snippet synthesis, not primary-source-
verified — the same second reason Red Team named at Iteration 13, now
shown to recur on its own merits. This reason is decisive by itself and
survives the "six classes" correction untouched. **What genuinely changes
this cycle**: LOGBOOK's own two Iteration-13-named remaining gaps are now
closed — a real, if narrower-than-first-claimed, narrowing of the
program's remaining path to a proven-boundary Checkpoint result.

**⚠ Same-shift correction, Red Team Phase-5 audit docket #5 (independently
caught by both QUANTUM OPTICS and ELECTROMAGNETISM): ENZ's disqualification
is NOT "a genuinely new failure mode... never previously seen in this
program's realizability checks."** A dominantly-real Δε (index shift with
negligible absorptive part) cannot terminate a beam under constraint 1 for
exactly the reason LOGBOOK.md's own **R1** (RULED OUT: passive refractive/
transformation-optics cloaking, killed at exp-001 — "the beam *continues*...
do not revisit as a constraint-1 mechanism") already names: a permittivity
change that's mostly phase-modulating routes or bends light rather than
extinguishing it, whether the index shift is static (R1) or
intensity-triggered (ENZ, this row). **This is a new INSTANCE of R1's
already-established principle, not a new CATEGORY of failure** — new
within this program's own realizability-check row-scoring line specifically
(RSA/TPA/photochromic/VO2/FCA all fail on magnitude, not expressibility),
genuinely correctly identified as that, but not new against this program's
full history. Added to R1's own LOGBOOK.md entry as a cross-reference,
per EM's Phase-5 request, so this is citable directly rather than only
inferable.

**One finding reworded, not merely re-labeled — Red Team Phase-5 audit
docket #6 (independently caught by both ELECTROMAGNETISM and QUANTUM
OPTICS): the source-mismatch finding for pulsed-pump mechanisms
(TPA-cascade FCA, ENZ) is a reinforcing energy-conservation/sustained-power
argument, not a "categorical... independent of and prior to" claim** — see
the reworded THERMO section in Results, which the original Learned-section
language echoed and has been corrected to match here too. It sharpens,
and is now explicitly reconciled with, the independently-established
irradiance/field-enhancement bookkeeping (MATERIALS' section), not a
separate finding standing prior to it.

**One honest, load-bearing self-correction, caught by the search itself
rather than by Phase 5 review**: Leg A found the pre-registration's own
"clean semiconductor = fast, doped = slow" framing for linearly-pumped
FCA's switching-speed hosts was backward, per ordinary Shockley-Read-Hall
recombination physics and two independently-sourced datasets — corrected
in the record here, in the same cycle it was found, without waiting for a
Phase-5 catch.

**A second self-correction, this one caught at Phase 5 by THERMODYNAMICS'
own re-read of its own work (docket #8, ruled load-bearing not queueable
by Red Team)**: the original capped thermal estimate for linearly-pumped
FCA's at-rest population was a qualitative analogy, not a computation, and
contained an internal inconsistency and a category error (comparing a
time-to-threshold to a steady-state temperature) — replaced same-shift
with an actual numeric estimate (ΔT_ss≈7mK at ambient, ~3–7× below current
microbolometer NETD, not merely "far below") using silicon's own standard
thermal constants, at zero marginal cost.

**Rigor bar, same honest self-assessment as exp-036**: sourced-but-
unverified (real paper titles, authors, years, and mechanisms recovered
for nearly every figure above — a genuine search, not a guess), not
primary-source-verified — WebFetch blockage total and independently
re-confirmed, not inherited as an assumption, across all 39 attempts made
this cycle. **Three consecutive literature-check cycles (36, 37, and this
one's own Phase-5 re-reads) have now hit total WebFetch blockage across
39+ attempts — the "sourced-but-unverified" evidentiary tier is the
ceiling on this whole methodology, not a one-off**, per PHOTONICS' Phase-5
finding; escalating the egress-proxy access question (an alternate access
route, or explicit escalation) is now overdue rather than a routine
disclosure, queued for Iteration 15.

## Phase 5 — Review (seven fresh seats — six discipline seats plus a
second independent PHOTONICS pass, since PHOTONICS was this cycle's own
lead — then Red Team audit) — summary

Full verbatim reviews: this shift's session record; LOGBOOK.md Iteration
14 carries the complete text. All seven reviewers read the committed
Results independently, blind to each other. Three findings converged,
unprompted, across independently-blind seats — this program's own
established load-bearing signal:

- **PHOTONICS (both passes) and MATERIALS independently converged on the
  same wavelength-tagging failure**: TPA-cascade FCA's host list (Si,
  GaAs) is above-bandgap — not TPA-relevant — at every wavelength this
  program tests, and the linearly-pumped-FCA row's load-bearing Soref &
  Bennett cross-sections were applied unscaled from their telecom-
  wavelength source, both instances of the cycle's own committed
  wavelength-tagging discipline going unexecuted for a second consecutive
  cycle. Both corrected same-shift, Results above.
- **ELECTROMAGNETISM and QUANTUM OPTICS independently attacked the same
  two claims from different angles**: ENZ's disqualification is a new
  INSTANCE of R1's already-established principle, not a "genuinely new
  failure mode" (both seats, independently reasoned); and THERMO's CW/
  pulsed "categorical... independent of and prior to" argument overstates
  its epistemic status and is in direct tension with MATERIALS' own
  field-enhancement section in the same document (both seats,
  independently). Both corrected same-shift, Results and Learned above.
- **MATERIALS and PHOTONICS (Pass 2) independently found the same
  underlying process gap from different sides**: MATERIALS found its own
  canonical `REALIZABILITY_MEMO.md` has gone three consecutive cycles
  without an update despite being named explicitly at each cycle's close;
  PHOTONICS (Pass 2) independently found the Learned section's "six named
  classes" claim doesn't match the memo's own actual class count (five,
  not six) when read directly. Corrected same-shift (Learned section); the
  memo itself updated same-shift, below.

**THERMODYNAMICS** self-audited its own capped estimate and found it was
not actually a computation (no numeric ΔT, no emission-band statement, no
stated detectability threshold), contained an internal "five to six
orders" vs. "two further orders" inconsistency, and committed a category
error comparing VO2's time-to-threshold to a steady-state temperature —
all self-caught, none requiring another seat's catch. **QUANTUM OPTICS**
additionally found the absorption-only correction was applied to combined
media's graphene/CNT sub-components without the same carrier-vs-molecular
disaggregation discipline required elsewhere in the same cycle. **VISION
SCIENCE** found a real loophole in its own mandatory language cap (the
word "negligible" survived the letter of the ban while violating its
spirit) and a persistent, third-consecutive-cycle gap in restating the
switching-speed provisional-vs-T3 tag at points of claim rather than only
in a table header. **MATERIALS** additionally found linearly-pumped FCA
never received an explicit realizability tier label, and that combined
media's dynamic-range figures may mix device/pulse-fluence metrics with
this program's own cross-section-ratio convention (PHOTONICS
independently, and separately, caught the resulting arithmetic error in
how that shortfall was characterized — corrected to ~0.65–2.1 orders,
not "2–4+"). **PHOTONICS (Pass 2)** additionally found two genuine
taxonomic orphans the search surfaced (ENZ's separate χ⁽⁵⁾/3-photon RSA
branch; the Joshi et al. energy-transfer-coupled dyad) with no clean home
in the original six-item taxonomy, and a "six-row" count that didn't match
its own enumeration.

**Red Team (audit, verdict: PARTIAL).** Independently re-derived the
physics behind every convergent finding above rather than trusting the
reviewing seats' characterizations (re-computed Si/GaAs bandgap-vs-sweep-
wavelength arithmetic; re-read R1 and REALIZABILITY_MEMO.md directly;
re-checked the "2–4+ orders" claim's own arithmetic). Found the CW/pulsed
claim not merely overstated but directly self-contradicted by another
section of the same document — elevated to HIGH severity above what
either reviewing seat assigned it. Ruled THERMODYNAMICS' self-assessed gap
genuinely load-bearing, not queueable, since Si's thermal constants are
free and the estimate was a specifically pre-committed Phase-3 deliverable
not executed as committed. Ruled Checkpoint criterion 2 does NOT fire —
independently confirming the evidentiary-tier reason survives even after
correcting the "six classes" overclaim (the corrected, narrower framing
still leaves the reason decisive on its own). Ruled Checkpoint criterion 4
exercised, not fired — both overclaims (the "six classes" and "genuinely
new failure mode" language) are the same self-correcting species as
Iteration 13's spiropyran correction, corrected same-shift, not requiring
a program pause. Issued a 17-item same-shift mandatory-fix docket (all
applied above and in REALIZABILITY_MEMO.md) plus six items queued for
Iteration 15.

**Director's synthesis: all 17 same-shift docket items accepted in full
and applied; none overridden.** Every item was independently re-verified
by Red Team against the primary text before being ruled load-bearing (not
merely asserted by a reviewing seat) — the same discipline this program
has applied at every Phase-5 close since Iteration 5. Nothing in the
docket warranted a Director override: the convergent findings were real
on direct inspection, THERMODYNAMICS' self-caught gap genuinely rose to
load-bearing per Red Team's own reasoning (zero marginal cost, a specific
unmet Phase-3 commitment), and the two Learned-section overclaims were
real, checkable errors, not matters of interpretation.

## Director's close of Iteration 14

**Verdict: PARTIAL.** A genuine, citation-sharpened boundary-mapping
result survives every correction applied this shift: TPA-cascade FCA,
linearly-pumped FCA, ENZ, and combined saturable/RSA media each fail via a
distinct, now more precisely characterized gap (an inherited quantum-
irradiance threshold; a quantitatively-confirmed dynamic-range shortfall,
now with an explicit realizability tier and a real thermal estimate; a
mechanism-class/expressibility disqualification correctly reframed as a
new instance of R1's established principle rather than a new category;
and a motivation-mismatch with a corrected shortfall magnitude). This
closes the two mechanism classes LOGBOOK's own Iteration-13 record named
as the program's last explicitly-tracked untested scope. But Checkpoint
criterion 2 does not fire — for the same evidentiary-tier reason Iteration
13 gave, now independently reconfirmed rather than assumed, and standing
on its own even after this cycle's "six classes" overclaim is corrected to
the narrower, accurate claim. Checkpoint criterion 4 is exercised, not
fired: three independently-converging Phase-5 findings (wavelength
discipline unexecuted a second cycle; two Learned-section overclaims,
one of them directly self-contradicted by another section of the same
document) were caught and corrected same-shift, exactly the program-
integrity discipline criterion 4 exists to enforce without needing to
pause the program. One specifically pre-committed Phase-3 deliverable
(THERMO's capped estimate) was not executed as committed and required a
genuine same-shift replacement, not merely a wording fix — a real gap,
now closed. No Checkpoint criterion requires convening Marsh this cycle.
Next lead per rotation: **MATERIALS** (Iteration 15).

Open questions carried forward: retroactive wavelength-tagging and
primary-source re-verification of exp-036's own four rows (RSA ~40×
figure, spiropyran at-rest figure) AND now exp-037's own two newly-flagged
instances (TPA-cascade FCA's host list, the Soref & Bennett cross-sections)
— PLAN.md priority #2, now carrying twice the load; a real escalation of
the WebFetch egress-proxy blockage, now confirmed across three consecutive
literature-check cycles and 39+ attempts, rather than a routine per-cycle
disclosure (PHOTONICS' Phase-5 finding); taxonomic homes for ENZ's χ⁽⁵⁾/
3-photon RSA branch and the Joshi et al. energy-transfer dyad (PHOTONICS
Pass 2); the carrier-vs-molecular absorption-correction question extended
to graphene/CNT sub-components (QUANTUM OPTICS); the intrinsic cross-
section-ratio-extraction discipline as a mandatory companion to the
composite-figure search-order fix for any future combined-media check
(MATERIALS); building the T17 rate-equation kernel in-engine (now raised
independently by QUANTUM OPTICS, VISION SCIENCE, and ELECTROMAGNETISM
across this cycle and the last); stage-10's T3 temporal-contrast
instrument (now flagged by VISION SCIENCE as the single most overdue item
on the program's books by cycle-count — three consecutive cycles producing
provisional switching-speed verdicts against it); patching the perceptual-
scoring cap itself to ban unearned magnitude-significance language in
either direction, and to require the T3-provisional tag restated at each
point-of-claim, not only in a table header (VISION SCIENCE); and a small
reusable THERMO-sidecar utility (ΔT_ss/heating-time/diffusion-reset-time
as a function of ρ, c_p, κ, P_absorbed, L) to replace hand-derived,
analogy-prone estimates each cycle (THERMODYNAMICS).
