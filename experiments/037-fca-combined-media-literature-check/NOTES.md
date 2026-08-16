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
pathway. **Dynamic range**: bounded by the same physics — no independent
mechanism exists to clear D_req below the TPA threshold, predicted NO,
confirmed by construction. **Irradiance**: NO, same ~10⁷–10⁸ W/cm² onset,
9–11 OOM above both the ≤10⁻² W/cm² Checkpoint-2 margin and the ~10⁻³
W/cm² witness estimate — identical to exp-036's own established TPA
figure, inherited not re-derived. **Switching speed (electronic clock)**:
YES both directions — TPA generation is sub-ps (virtual-state process,
exp-036's own established figure), and FCA carrier lifetimes in these
specific hosts (Si, GaAs, ZnSe, CdS) are reported in the ns–µs range in the
broader semiconductor-photonics literature (consistent with, though not
independently re-verified against, this cycle's own Leg A findings for Si
specifically) — clears the 10ms–1s window comfortably. Lattice-thermal
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
cm² per carrier). A back-of-envelope σ_on/σ_off built from this figure
(own construction, order-of-magnitude only, every assumption stated) finds
**D_req is NOT cleared across the entire physically reasonable doping
range** — a fast host (τ≈1ns) gives a negligible ~1.1×10⁻⁷ shift; a
long-lifetime host (τ≈1ms, N_D=10¹⁷cm⁻³) gives only ~1.11× (roughly 3
orders of magnitude short of D_req≥540–600×); even at aggressively low
doping (N_D=10¹³–10¹⁴cm⁻³) the ratio only approaches ~100×, still short.
**CONFIRMS the pre-registered NO**, with the exact shortfall shown to be a
genuinely N_D-sensitive open dependency, not a single fixed number.
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

**Switching speed, both clocks**: electronic/carrier clock — Si spans
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
host (τ=1ns) gives n_ss≈1.1×10⁻⁹ — negligible; long-lifetime host (τ=1ms)
gives n_ss≈1.1×10⁻³, rising toward ~0.1 at lower, still-plausible doping
(N_D=10¹⁵cm⁻³) — **genuinely open, doping-sensitive, exactly as
pre-registered.** Leg A flagged its own normalization choice (n_ss
referenced to dopant density N_D, since free-carrier photogeneration draws
from an unbounded valence-band reservoir with no natural "1" to saturate
toward, unlike T17's original bounded two-level population) as an open
methodological gap, not an established result. **Reported strictly per
VISION's mandatory cap**: real chemistry/physics, visual significance
unverified, not yet a scored constraint-3 violation — no "confirmed,"
"risk," or "non-negligible" language attached regardless of the computed
magnitude's range.

**Row verdict: matches the pre-registered structure in full** — D_req NO
(quantitatively confirmed for Si, qualitatively consistent for Ge), YES
irradiance, an electronic clock spanning fast-to-slow hosts (with the
fast/slow-host material-purity direction corrected against the
pre-registration's own unverified assumption), and a genuinely open,
doping-sensitive at-rest finding scored via T17's existing formula and
held to VISION's language cap throughout — not a disqualified-gate claim,
exactly as EM's Phase-2 fix required.

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

**Constraint-2 disclosure (Red Team's fix), delivered**: ENZ ITO/AZO
metafilms document anomalous reflectivity — up to ~15 percentage-point
reflectance swings at the ENZ point, plus generic Brewster/Berreman
singular-reflection modes near the near-zero-index condition — a real,
sourced, non-verdict-changing disclosure (the row fails independently on
wavelength regardless).

**Wavelength**: ITO's ENZ point sits at λ≈1200–1550nm (tunable via
doping/annealing); AZO's at ~1300nm. **CONFIRMS the predicted
disqualification** — entirely outside this program's 450/600/750nm sweep
and a white flashlight's ~400–700nm visible emission.

**Irradiance**: every demonstration found is femtosecond-pulsed (no CW
figure found or conflated), peak intensities in the GW/cm² range (1.2–140
GW/cm² across cited variants). **CONFIRMS NO** — ~11–14 orders of
magnitude above both bounds, comparable to or worse than TPA's own 9–11
OOM gap, exactly as predicted.

**Switching speed**: reverse ≈360fs (Alam et al.); forward tracks the
pump envelope (fs-scale). **CONFIRMS YES both directions**, clears the
10ms–1s window by many orders of magnitude.

**Row verdict: unobtainium-with-a-wavelength-and-mechanism-class
disqualifier, confirmed, with one item left genuinely open** (the Δε_imag
branch's own magnitude) rather than forced — the row's overall
disqualification does not depend on resolving that open item, since
wavelength alone is decisive.

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
row's own combined number). All 2–4+ orders of magnitude short of the
540–600× lower bound, and further short of the 890–1180× absorption-
only-corrected bound — **confirmed applicable here** (molecular/π-
conjugated-carbon absorbers, the same category exp-036 validated the
correction against, unlike the FCA/ENZ carrier-plasma rows above where
applicability stayed open).

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

**Switching speed**: every RSA component identified across all three
architectures (C60, phthalocyanines, porphyrins, graphene/CNT) is drawn
from the fast (ns–µs) RSA precedent exp-036 already established, not the
long-triplet subclass — the classic-fast branch applies by elimination.
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

**Linearly-pumped FCA's at-rest population (row 2).** Leg A's own
extracted absorbed-power figure at ambient illumination (I_ambient≈10⁻⁵
W/cm², interband absorption near-complete within a few µm of the Si
surface) is itself five to six orders of magnitude below the ~10⁻³ W/cm²
flashlight-level absorbed-power figure exp-036's own capped VO2 estimate
already showed produces, at best, a 15–45 second heating time at the most
favorable (µm-scale, latent-heat-corrected) geometry — and that VO2
estimate concluded heating alone is fatal (too slow, or requiring
unrealistic power density) at every length scale from µm to m. At two
further orders of magnitude down in absorbed power density, and with no
phase-transition threshold to cross at all (linearly-pumped FCA's
absorption is graded and continuous, unlike VO2's discrete transition),
any steady-state temperature rise above ambient scales down proportionally
with absorbed power for a fixed geometry and cooling pathway — **the
resulting ΔT is expected to be a small fraction of VO2's own
already-negligible-at-this-power-level rise, with re-radiation at any such
ΔT sitting far below realistic IR-detectability thresholds.** This is a
qualitative, order-of-magnitude conclusion, explicitly not a quantitative
ΔT figure — the honest, capped answer given the estimate's own stated
scope: **no detectable thermal signature is expected for linearly-pumped
FCA's ambient-driven population**, independent of, and consistent with,
the negligible-to-small n_ss values Leg A itself computed.

**ON-state absorption events, TPA-cascade FCA and ENZ-ITO FCA (rows 1, 3).**
A more basic, and arguably more decisive, finding than a ΔT estimate:
both mechanisms are demonstrated in the literature (this cycle's own Leg B
findings, and exp-036's own established TPA figures) using **pulsed**
excitation at GW/cm²-class peak intensities and femtosecond-to-nanosecond
pulse durations — never CW. A flashlight is a CW source, by construction,
at ~10⁻³ W/cm². **The carrier/optical relaxation clock and the lattice-
thermal clock are therefore both moot for these two rows in the witness
scenario**: no realistic flashlight can supply the peak power density
these mechanisms require even for a single pulse, let alone sustain it —
a categorical source-mismatch finding, independent of and prior to any
ΔT/detectability computation, and consistent with (sharpens, not
contradicts) both rows' independently-established irradiance failures.

## Learned

**Program-level pre-registered prediction CONFIRMED**: no row clears all
bounds simultaneously. **Five structurally distinct failure modes
confirmed**, sharper and more precisely characterized than the
pre-registration itself predicted in several places: TPA-cascade FCA
(irradiance, algebraically inherited from TPA, derived not searched);
linearly-pumped FCA (dynamic range, quantitatively confirmed via a real
literature cross-section for the first time this program has attempted
this row-type, with a genuinely open — not disqualified, not assumed —
at-rest finding scored through T17's existing formula exactly as EM's
Phase-2 fix required); ENZ (a **genuinely new failure mode for this
program**: a mechanism-class/expressibility disqualification — the
headline nonlinearity is refractive, not absorptive, and does not reduce
to a σ(I) row at all — compounded by, not merely coincident with, a
decisive wavelength disqualification); combined media (published-partial,
motivation-mismatch, with real composite dynamic-range figures found and
scored, not merely gestured at). **Graphene's control case holds without
qualification**, with one honestly-disclosed, non-representative exception
(doped/mid-IR TPA-over-SA).

**This cycle closes the program's last named-but-untested mechanism class
scope** — combined with exp-036, all six named classes from
REALIZABILITY_MEMO.md (RSA, TPA, photochromic, photothermal/VO2, FCA,
combined saturable/RSA media) have now been checked, each failing via a
distinct, literature-grounded gap. **Checkpoint criterion 2 does not
fire this cycle either**, for the reason honestly determined at Phase 4
rather than assumed at Phase 1 (per Red Team's fix, striking the
tooling-guess from the predictions table): the evidentiary tier is,
independently re-confirmed across all three legs (39 total WebFetch
attempts, zero successes), WebSearch-snippet synthesis, not primary-
source-verified figures — the same second reason Red Team named at
Iteration 13, now shown to recur on its own merits rather than assumed to
recur. **What changes this cycle, honestly stated**: the FIRST reason
Iteration 13 gave (a named class remaining untested) is now GONE — this
program has, for the first time, run out of named mechanism classes to
check. Only the evidentiary-tier gap keeps criterion 2 from firing. This
is a genuine, significant narrowing of the program's own remaining path to
a proven-boundary Checkpoint result, not a repeat of exp-036's finding —
whether it is enough, and whether Phase 5 finds this cycle's own six-row
scoping exhaustive within the classes named (the honest open question the
predictions table itself flagged rather than pre-answered), is for Phase 5
to determine.

**Two genuinely new findings, neither previously seen in this program's
realizability-check line:** (1) ENZ's mechanism-class disqualification —
the first row in this program's history to fail not on dynamic range,
irradiance, or switching speed, but on failing to reduce to a σ(I) row at
all; (2) the source-mismatch finding for pulsed-pump mechanisms
(TPA-cascade FCA, ENZ) — a flashlight, being CW by construction, cannot
in principle drive a mechanism demonstrated only under pulsed excitation,
a categorical argument independent of and prior to any irradiance-
magnitude comparison, though this cycle treats it as reinforcing rather
than replacing the magnitude-based irradiance verdicts already established.

**One honest, load-bearing self-correction, caught by the search itself
rather than by Phase 5 review**: Leg A found the pre-registration's own
"clean semiconductor = fast, doped = slow" framing for linearly-pumped
FCA's switching-speed hosts was backward, per ordinary Shockley-Read-Hall
recombination physics and two independently-sourced datasets — corrected
in the record here, in the same cycle it was found, without waiting for a
Phase-5 catch.

**Rigor bar, same honest self-assessment as exp-036**: sourced-but-
unverified (real paper titles, authors, years, and mechanisms recovered
for nearly every figure above — a genuine search, not a guess), not
primary-source-verified — WebFetch blockage total and independently
re-confirmed, not inherited as an assumption, across all 39 attempts made
this cycle.
