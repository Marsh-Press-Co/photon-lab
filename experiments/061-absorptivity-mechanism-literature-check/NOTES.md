# exp-061 — The `graded_black_shell` Absorptivity Literature Check +
# the Caveat-Propagation-Check Tool

**Panel Iteration 38. Lead: MATERIALS & METAMATERIALS, by UNCONDITIONAL
LOCK** (not rotation — the absorptivity literature check is now eight
cycles deferred, Iteration 29→37, the longest deferral chain this
program has run before a lock fired). Two co-mandatory items, both
delivered. **T1 escape route: NONE — zero constraint-1/2/3/4 metric is
scored this cycle.** This is a realizability-bound + tooling cycle, the
same category as exp-036/037 (literature checks) and exp-038/046/059
(new machinery at Phase 1). Zero FDTD this cycle. Zero network calls for
item (B); item (A)'s search runs this Phase (Phase 4), after predictions
below are frozen to git.

Full panel record: `phase1_proposal.md`, five `phase2_critique_*.md`
files, `phase2_redteam_audit.md`, `phase3_synthesis.md` (this directory).
This file (`NOTES.md`) is the master document — where Phase 3 corrected
a Phase-1 number, THIS file carries the corrected value;
`phase1_proposal.md` is left as-written, a historical record, per house
convention (errata are flagged, never silently rewritten).

---

## Hypothesis

`graded_black_shell`'s fixed-absolute-thickness variant (exp-052,
Iteration 29 — CLOSED on thickness, OPEN on absorptivity) implies a
physical volumetric absorption coefficient this program has never
checked against a real material. exp-060 (Iteration 37) showed the
graded profile does real, separable, measurement-backed suppression work
(Fresnel-reflectance mitigation at the entry, not just bulk loss) — which
makes whether a real coating can supply that same absorption rate within
that same physical thickness *more* consequential to this program's
realizability picture, not less.

**Corrected target (Phase-3 mandatory fix 1 — Red Team's derivation,
`phase3_synthesis.md`; re-verified independently by the Director, R4
compliance — do not trust this number without re-running the
arithmetic):**

```
tau_true = 2 * (2*pi/cpl) * thickness_cells * I_graded
         = 2 * (2*pi/20)  * 48              * 0.273840
         = 8.258819829686677

alpha_true      = tau_true / thickness_nm = 8.2588 / 1440nm
                = 0.0057353 /nm  =  5.7353e4 cm^-1
e-fold length   = 1 / alpha_true = 174.36 nm
optical density = tau_true / ln(10) = 3.587 OD
```

where `I_graded = ∫₀¹ Im(n(σ_graded(d))) dd = 0.273840` is exp-060's own
already-committed, already Red-Team-corrected number for this exact
shell (r_in=30, r_out=78, σ_max=0.5, 48-cell shell) — reused here at zero
marginal cost, not re-derived from scratch (Red Team's own adjudication
of the PHOTONICS/EM Phase-2 disagreement, `phase2_redteam_audit.md` §2).

**This supersedes `phase1_proposal.md`'s own headline figure** (α ≈
1.667×10⁵ cm⁻¹, 60nm e-fold, from `TAU_SHELL=24 =
sigma_max×thickness` — a raw peak-conductivity×thickness product that
neither integrates the graded profile nor accounts for `Im(n)`'s
concavity in σ). The corrected α is **2.90× smaller** than originally
proposed; the corrected e-fold length is **2.90× longer**.

**Question:** is α≈5.74×10⁴ cm⁻¹ (174nm e-folding) over a graded,
always-on, passive coating PUBLISHED, PLAUSIBLE, or UNOBTANIUM for a
real ultra-black coating class, **at this construction's own 1.44µm
physical thickness specifically**?

**Explicit non-scope:** the RSA/TPA/photochromic/FCA/ENZ/combined-media
*switching* mechanisms (T1's σ(I) escape route) — exhaustively checked
already (`REALIZABILITY_MEMO.md`'s main table, exp-036/037). This is a
different question: the raw absorptivity of a passive, always-on
absorber, not a switchable one.

**Classical-parameter scoping (Phase-2 mandatory fix 3, QUANTUM's
demand):** any "effective α" this check infers from a real CNT-forest's
measured (reflectance, thickness) pair necessarily pools multiple
possible physical origins — dilute bulk absorption, diffuse structural
multiple scattering among tube tips, and (in principle) near-field/
coherent CNT-CNT coupling or localization-type interference, all real,
published phenomena for dense sub-wavelength carbon nanostructures — into
a single classical Beer-Lambert-equivalent scalar, **for this comparison
only**. Per QUANTUM OPTICS' expressibility contract, this pooling is
explicit, not implicit. **Pre-registered fallback:** if Phase 4's search
turns up sources that characterize CNT-forest blackness predominantly in
coherence-length, Anderson-localization, or near-field-coupling terms —
not a reflectance-vs-thickness curve reducible to a scalar α at all —
that is scored as a **scope caveat on MP-4** (the comparison's own
premise doesn't apply cleanly), not silently pooled into the OD-per-
length number, and not silently treated as a null result either.

---

## Setup

Desk-only. No `Sim`, no `lab.fdtd2d` engine call, no new trust-suite
stage (design rationale for staying outside `run_all.py`: see Item (B)
below and `lab/caveat_lint.py`'s own module docstring).

### Item (A): the literature search plan (executes Phase 4, after this
freeze)

**Source classes accepted**, ranked by evidentiary weight:
1. Peer-reviewed optics/nano journals reporting measured CNT-forest
   reflectance/absorptivity vs. forest height or effective optical
   constants (n, k) of vertically-aligned CNT arrays.
2. NASA/GSFC technical reports and papers on carbon-nanotube black
   coatings for stray-light/baffle applications.
3. NIST or other national-metrology-institute black-coating
   characterization reports (reflectance/BRDF with stated thickness).
4. Manufacturer technical data sheets for Vantablack-class products
   (Surrey NanoSystems, Acktar Metal Velvet, or equivalent) stating
   thickness alongside reflectance.
5. A secondary, explicitly-flagged-as-less-comparable class: index-
   grading-dominant broadband absorbers (black silicon nanocones,
   moth-eye AR structures) — accepted only as a bound-widening
   cross-check, labeled and never pooled with the CNT-forest figures
   (a structurally different `eps(r)` shape than `graded_black_shell`
   codes).

**Query list** (exact terms, committed before any search runs):
1. `Vantablack absorption coefficient cm-1`
2. `carbon nanotube forest reflectance vs thickness optical density`
3. `CNT forest ultra-black coating micron reflectance 0.035%`
4. `Surrey NanoSystems Vantablack technical data sheet thickness`
5. `NASA carbon nanotube black coating Hagopian absorptivity thickness`
6. `vertically aligned carbon nanotube array effective refractive index imaginary part visible`
7. `super black carbon nanotube array reflectance forest height micron`
8. `carbon nanotube forest absorption coefficient alpha cm-1 visible wavelength`
9. `carbon nanotube forest packing density volume fraction optical properties`
10. `NIST black coating characterization reflectance report`
11. `single wall carbon nanotube film extinction coefficient k optical constants`
12. `black silicon nanostructure reflectance absorption coefficient broadband`
13. `ultra-black coating optical density per micron thickness`
14. `Acktar metal velvet black coating specular reflectance thickness`
15. `ultra black coating ~1 micron thin film absorption coefficient visible`

**Evidentiary-tier disclosure (T18, standing since Iteration 13, 39+
consecutive blocked WebFetch attempts):** Phase 4 will very likely be
**WebSearch-snippet synthesis, not primary-source PDF/DOI-verified
reading** — the identical evidentiary tier as exp-036/exp-037. Per Red
Team's Iteration-26 ruling (an informal, unsourced desk tier-call for
this exact question was already rejected once), the Phase-4 verdict must
cite specific WebSearch results, not be rendered as an unsourced desk
estimate. **(Phase-2 mandatory fix 2, VISION SCIENCE's own live catch:
this disclosure is repeated at every verdict-bearing site below, not
only here — `lab/caveat_lint.py` now tracks this propagation via registry
entry `exp061-t18-evidentiary-tier-propagation`.)**

### Item (B): the caveat-propagation-check tool

Built, tested, and independently re-verified by all five Phase-2
critics and Red Team (six independent executions of `python3
lab/caveat_lint.py` and `--selftest`, all reproducing the same PASS/FAIL/
WARN output). Full design rationale: `lab/caveat_lint.py`'s own module
docstring (a lint-style, grep-every-caveat-across-every-touched-file
tool; hand-curated JSON registry at `lab/caveat_lint_config.json`;
config-driven, `--only`, `--adhoc`, and `--selftest` modes; deliberately
NOT a `run_all.py` trust-suite stage — a documentation-completeness
check is a categorically different assertion than a physics-measurement
gate). Not repeated in full here to avoid the exact drift-from-source-of-
truth pattern this tool exists to prevent — see the module itself.

**Self-test scope, tightened (Phase-2 mandatory fix 8):** `--selftest`
replays exactly ONE real historical case — one caveat phrase, one file
(`lab/validation/run_all.py`'s stage-22 docstring), two real git
revisions (`d5b4844` pre-fix, `4f29982` post-fix, Iteration 37's own
Checkpoint-4 finding and same-shift fix) — not a statistical sample of
the program's other six near-misses (Iterations 17/24/32/33/34/35/36).
Confirmed PASSED, independently, by six separate executions this cycle
(the Director's own Phase-1 build, and all five Phase-2 critics plus Red
Team, each running it fresh).

**Registry, as of this freeze (5 entries, `lab/caveat_lint_config.json`,
all live-verified 0 required-site failures this shift):**
1. `exp060-p10-fresnel-not-diffraction` — Iteration 37's own headline
   Checkpoint-4 finding (edge/grazing diffraction → Fresnel reflectance).
2. `exp060-sigma-flat-convention-caveat` — the `sigma_flat`/`Im(n(σ))`
   concavity residual's EXISTENCE.
3. `exp052-alpha-60nm-absorptivity-open` — this cycle's own standing
   question (registered before the Phase-4 search that will resolve or
   sharpen it — a deliberate self-application of the tool to its own
   introducing cycle).
4. **`exp061-t18-evidentiary-tier-propagation`** (NEW, Phase-2 mandatory
   fix 2) — the T18 evidentiary-tier disclosure must appear at every
   verdict-bearing site this document states, not only in a general
   methodology section. Required site: this file.
5. **`exp060-sigma-flat-corrected-bias-direction`** (NEW, Phase-2
   mandatory fix 5, QUANTUM's own self-catch) — the specific CORRECTED
   DIRECTION of the `sigma_flat` residual (`b_flat > I_graded`, a true
   match requires LOWERING `sigma_flat`, not raising it) — QUANTUM
   itself got this backwards at its own Iteration-37 Phase 2, fixed only
   at Phase 5; entry #2 above checks only the residual's existence, not
   this specific corrected sign, so a future edit could silently
   reintroduce the reversal undetected without this entry.

**Live registry check, this freeze:**
```
$ python3 lab/caveat_lint.py
5 caveat(s) checked, 0 required-site failure(s).
```
(Entry 4 above targets THIS file, which now exists and carries the
required phrase — see the T18 disclosure above and the Predictions table
below.)

---

## THERMO disposition (Phase-2 mandatory fix 4, THERMODYNAMICS' demand,
Red Team's unconditional ruling — full derivation: `phase3_synthesis.md`)

Desk-only, `lab/thermo_sidecar.py`, post-run analytic (expressibility
contract). Question: under MP-5's own fallback (a real coating supplies
the required optical depth, but only at 15–150µm rather than 1.44µm), is
the resulting object still thermally UNDETECTABLE at witness scale?

**Worst-case, deliberately conservative in every free choice**
(`l_geometric_m`=150µm — MP-2's own predicted upper thickness bound taken
as the object's full outer radius; `ratio_abs_ext`=1.0 — a 100% ceiling,
above the established 0.51–0.61 measured family; silicon thermal
identity, `ASSUMED — provenance terminates unsourced (T18)`, reused
verbatim from Iteration 23's own disclosed convention; two sourced
irradiance points from `WitnessScenario`, docket #7):

| Irradiance | `p_abs` ceiling (W) | `ΔT_ss` (K) | Margin vs NETD-lo (0.020K) | Classification |
|---|---|---|---|---|
| central, 6.58×10⁻⁶ W/cm² | 1.4805×10⁻⁹ | 3.6868×10⁻⁴ | **54.2×** | UNDETECTABLE |
| worst-case, 4.414×10⁻⁵ W/cm² | 9.9315×10⁻⁹ | 2.4732×10⁻³ | **8.1×** | UNDETECTABLE |

**Result: UNDETECTABLE at both points, even stacking a 100%-absorption
ceiling, the worst sourced irradiance, and MP-2's own upper thickness
bound simultaneously.** Wien peak ≈9.88µm (deep thermal-IR), consistent
with every prior UNDETECTABLE finding this program has logged since
Iteration 20. Per `thermo_sidecar.py`'s own standing disclaimer, NETD is
an instrument/detector threshold — this classification does **not** bear
on constraint-3/4's human-eye verdict.

---

## Idealizations

1. **Item (A) predictions below are general-domain-knowledge estimates,
   not search results.** No WebSearch query has been run as of this
   freeze (house discipline — predictions committed before the run). MP-1
   /MP-2's numeric bands are informed, falsifiable guesses about what the
   literature likely shows.
2. **T18's WebFetch block is assumed still standing**, carried forward
   from `REALIZABILITY_MEMO.md`'s own most recent confirmation (39+
   consecutive attempts since Iteration 13) — Phase 4 will re-confirm
   before falling back to WebSearch-snippet synthesis.
3. **The Beer-Lambert framing itself may not be the right lens for real
   CNT forests.** Real blackness is plausibly dominated by structural
   light-trapping/multiple scattering, not homogeneous bulk absorption —
   *why* a naive α comparison is predicted to look unfavorable on the
   thickness axis even where the rate axis may not. If Phase 4's sources
   characterize CNT-forest blackness in genuinely different terms (no
   stated reflectance-vs-thickness curve at all), MP-1/MP-2 may be
   unscoreable as stated and will need a restated comparison — disclosed
   here as a real risk, not discovered later. **(See the classical-
   parameter scoping + coherence/localization fallback in the Hypothesis
   section, Phase-2 mandatory fix 3.)**
4. **The secondary comparator class** (black silicon, moth-eye
   structures) is index-grading-dominant, not conductive-loss-dominant —
   a genuinely different `eps(r)` shape than `graded_black_shell` codes.
   Any figure from that class is a bound-widening cross-check only, never
   pooled into the primary CNT-forest verdict.
5. **τ_true's own derivation is a 1D, `d`-linear WKB-style approximation**
   (`Im(n)` integrated over normalized depth `d`, then mapped linearly to
   physical radius) — not an area-weighted or full-wave radial
   integration. Red Team's own ruling (`phase2_redteam_audit.md` §2):
   this is the correct standard for a realizability-BOUND cycle (T1
   escape route: NONE, no constraint metric scored), not a load-bearing
   physics claim — a fresh full derivation was judged not worth its
   marginal cost given MP-2 (thickness), not MP-1 (α), is this check's
   dominant, anchor-invariant falsification axis (verified: MP-2's own
   15–150µm vs 1.44µm gap does not move under any of the three candidate
   τ anchors considered at Phase 2 — 24, 9.40, or 8.26).
6. **The caveat-lint tool's phrase matching is deliberately loose**
   (whitespace-normalized substring/regex, case-insensitive, ANY-OF a
   list of acceptable paraphrases) — a false negative is possible for a
   caveat whose registry entry was written with too narrow a
   `phrase_patterns` list. This is a lint tool, not a semantic verifier;
   a human still reads the report.
7. **The tool's registry is hand-curated, not automatically populated**
   from Phase-3/Phase-5 dockets — a Director must still read a docket and
   decide to add an entry. **This is not a hypothetical limitation**:
   VISION SCIENCE's own Phase-2 critique demonstrated it live — the
   T18-propagation gap this very document now closes (registry entry 4,
   above) existed, unregistered, inside `phase1_proposal.md` at the
   moment the tool was first run against it. Red Team's ruling
   (`phase2_redteam_audit.md` §3): this does not fire Checkpoint
   criterion 4 (a self-caught, pre-freeze registration gap is a different
   defect species than a docketed propagation promise broken by hand-
   review), but a **binding forward tripwire** is set: a recurrence of
   this exact "never-registered caveat" shape, discovered *after* this
   fix lands, auto-fires criterion 4 under the same no-further-
   deliberation logic as the existing propagation tripwire.
8. Item (B) required no FDTD, no `Sim`/`lab.fdtd2d` engine code, and no
   trust-suite stage — confirmed by inspecting `run_all.py`'s own
   structure before concluding a new stage would be a category error
   (documentation-completeness vs. physics-measurement), not merely
   unnecessary.
9. **THERMO disposition's worst-case construction is deliberately
   pessimistic**, not a physical prediction of what the coating would
   actually look like if built (a real 150µm-thick CNT-forest-class
   coating would almost certainly NOT be a compact square-cross-section
   absorber with 100% extinction efficiency) — it is a ceiling, chosen so
   that an UNDETECTABLE result is robust to every free modeling choice
   pointing the wrong way at once.

---

## Predictions — committed to git BEFORE Phase 4's search runs

| # | Quantity | Predicted band | Reasoning |
|---|---|---|---|
| MP-1 | Literature CNT-forest effective **α**, as OD-per-length inferred from published (reflectance, thickness) pairs | **1×10³ – 3×10⁴ cm⁻¹** (e-fold depth ≈ 0.3–10 µm) | Real CNT forests are dilute (areal/volume packing ~1–10%), and published record-blackness forest heights are consistently tens of microns — a structurally different (light-trapping-dominated) regime than a homogeneous Beer-Lambert medium |
| MP-2 | Published CNT-forest coating thickness reported at genuinely near-total blackness (reflectance ≲0.05%, comparable optical density to real record-holder coatings — an independent, general domain-knowledge estimate, NOT re-derived from τ_true; Red Team's own ruling: this axis is anchor-invariant under any of the 24/9.40/8.26 τ candidates considered at Phase 2) | **15–150 µm** | vs. this program's own 1.44 µm — a ~10–100× thickness gap; this is the dominant, anchor-invariant falsification axis for MP-4 |
| MP-3 | Any single primary source reporting α ≥ 1×10⁵ cm⁻¹ (i.e. within ~2× of the corrected target, 5.74×10⁴ cm⁻¹) at ANY visible wavelength for a genuinely broadband, non-resonant, non-metallic-interface coating, **found via WebSearch-snippet search (T18's evidentiary tier)** | **NOT FOUND via WebSearch-snippet search** (predicted null result) | no mechanism in MP-1's own reasoning supports it; a hit here would be the single most falsifying possible outcome for MP-4 |
| MP-4 | **Predicted tier verdict** for α≈5.74×10⁴ cm⁻¹ / 174nm e-folding, at 1.44 µm physical thickness, sourced via **WebSearch-snippet synthesis only (T18)** | **UNOBTANIUM-WITH-PARAMETERS** (not PUBLISHED; not PLAUSIBLE at THIS specific thickness) — driven primarily by MP-2's thickness gap, not by an implausible absorption rate (the corrected α is only 1.9–57× above MP-1's own predicted literature band, not the 5.6–167× the uncorrected figure implied) | thickness, not rate, is the harder ask for this specific construction |
| MP-5 | **Conditional plausibility restatement** — if MP-1/MP-2 confirm, is τ_true=8.26 achievable AT ALL for this construction class, just not at 1.44 µm? **[T1 escape route: NONE — zero constraint-1/2/3/4 metric is scored by this row or by any resolution of this question (Phase-2 mandatory fix 6).]** | **YES, PLAUSIBLE at ~15–100× the thickness** | reframes the verdict from "impossible" to "the specific thickness-vs-optical-depth combination is the unobtainium part," consistent with Entry 2's own closed thickness-only finding at Iteration 29. **THERMO disposition (above): even under this fallback, at deliberately worst-case assumptions, the object stays thermally UNDETECTABLE (8.1–54.2× margin) — this row does not open a new detectability risk.** |

**Falsification, pre-registered:** MP-4 is falsified toward PLAUSIBLE or
PUBLISHED if Phase 4 turns up a primary-or-best-available source
reporting CNT-forest (or comparable broadband graded near-ε=1 absorber)
effective α within roughly 2× of 5.74×10⁴ cm⁻¹ **at a stated thickness
within roughly 2× of 1.44 µm** — both conditions together, since a high α
at a much larger thickness does not license this program's own specific
construction. MP-1/MP-2 are the primary falsifiable quantities; MP-4 is a
synthesis of them, not independently scored. **Scope caveat (Phase-2
mandatory fix 3):** if Phase 4's sources characterize CNT-forest
blackness predominantly via coherence/localization/near-field-coupling
language rather than a scalar reflectance-vs-thickness curve, MP-4 is
scored as **INCONCLUSIVE ON MECHANISM-CLASS GROUNDS**, not silently
folded into either tier.

---

*Result / Learned / Next sections appended after Phase 4 runs and Phase 5
review completes — not written yet, per house discipline (predictions
frozen before the run).*
