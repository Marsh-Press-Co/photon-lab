# exp-087 — T28 Energy-Interception Cross-Check: a Purpose-Built Poynting-Box Measurement

Panel Iteration 64. Lead: THERMODYNAMICS (rotation). Discharges the
Iteration-63 forward tripwire (LOGBOOK.md, PLAN.md Tier 2 item 4): the
joint EM/THERMO energy-interception cross-check, named at Iteration 59
(exp-082), deferred/exempt four consecutive cycles (083–086) — a fifth
consecutive deferral without either a purpose-built article-loaded scene
or an explicit retirement of the deferral framing fires Checkpoint
criterion 4 automatically. Full phase record: `phase1_proposal.md` →
five blind Phase-2 critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
QUANTUM OPTICS, VISION SCIENCE, unanimous support-with-changes, zero
overlap) → `phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-FIXES,
10 items, zero overridden) → `phase3_synthesis.md` (this cycle's frozen
spec, all 10 fixes adopted).

## Hypothesis

The cross-check's originally-scoped shape (Iteration 59) was a zero-FDTD
sanity bound reusing T9's broadside `σ_abs/σ_ext=0.51` anchor —
never executed in any form across four subsequent cycles. This experiment
measures it instead: `lab/sections.py`'s already-stage-8-gated Poynting-box
ledger (`widths()`), never before applied to the T28 article-loaded scene,
runs on the same flagship-absorber-loaded C40/G40 (`PAIR_PAD`) geometry
exp-082/083 already built and validated, at a disclosed 3-angle subset of
the established 31-point window — fresh, scene-specific `σ_abs(θ)`/
`σ_ext(θ)` for both PAD configs, at real oblique incidence, for the first
time. Hypothesis: the article's real absorbed-power PAD-sensitivity
(`frac_p_abs`) is decoupled from (much smaller than) the already-measured
Weber-contrast PAD-sensitivity (`frac_contrast`, cited from exp-083) —
consistent with ten-plus cycles of convergent evidence that this
sub-thread's own confound is a phase/interference effect, not an
energy-budget one — but this is a genuine, falsifiable measurement, not a
foregone conclusion, and a CONSISTENT/ENERGY-DOMINANT/MIXED finding would
be a materially new, immediately actionable result.

## Setup

`experiments/087-.../run.py` reuses exp-083's `_load()` idiom to import
`dg069` (→`dg065.CONFIGS["C40"]`/`["G40"]`), `build_article`, `_run_sim`
**verbatim, unmodified** — zero geometry retyped. New code: `BOX_A`/`BOX_B`
Poynting boxes (exp-024's `BOX_CLEARANCE=12` convention, doubled for
`BOX_B`, translated per config's own PAD shift) and `REF` (exp-024's
`REF=(OBJ_X,OBJ_Y,80)` convention); `sc.widths()` calls at both boxes for
every (config, angle, leg); the `xi_ext` extinction-routes-agreement gate
(Phase 2 mandatory fix 1); `ts.absorbed_power_established_ratio` →
`ts.mixed_length_scale_regime` → `ts.netd_disposition` (reusing exp-043's
sourced witness irradiance and exp-057's thermal constants verbatim); a
synthetic classifier-recovery self-test (Phase 2 mandatory fix 4); a
non-negativity assertion (fix 7); and a settling spot-check
(STEPS=1400 vs 2800 at G40/38.6°, fix 5). 14 new FDTD calls total (12 main
+ 2 settling). Angle set: `{36.0°, 38.6°, 41.8°}`
(`dg069.DENSE_ANGLES[0,13,29]`) — non-uniformly spaced (2.6°, 3.2°) per
Phase-2 mandatory fix 2, replacing Phase 1's uniform 3.0° spacing after
Red Team confirmed it sat within 1.8% of exact aliasing against
`P*=2.9474°`, T28's own decisively-resolved dominant confound period.

## Idealizations

1. 3-angle subset (non-uniformly spaced, {36.0°,38.6°,41.8°}), not the
   full 31-point window.
2. Single λ=600nm, matching the rest of the T28 window.
3. `iso_xsec_sq` area convention (thermo_sidecar's own stated
   idealization): the object is treated as compact, not an infinite rod.
4. Silicon thermal constants (ρ, c_p) are ASSUMED, provenance unsourced
   (T18, `REALIZABILITY_MEMO.md`'s standing downgrade), reused verbatim
   from exp-057.
5. WitnessScenario irradiance/distance/candela are WebSearch snippet-tier
   (T18), reused verbatim from exp-043, not re-searched this cycle.
6. The `ratio_k` decade-scale tiers (0.1×/10×) are a deliberately wide,
   first-of-its-kind falsification band, not a rigorously derived
   confidence interval.
7. Settling of the `widths()`-derived channel is spot-checked once
   (one cell, STEPS=1400 vs 2800), not a full R3-grade convergence study —
   disclosed alongside the primary result, not gating it, matching
   exp-083's own precedent for the identical check on the Weber-contrast
   channel.
8. The 3× box-dev noise-floor multiplier is a house-style choice (mirrors
   R3's "survive a resolution change with margin" precedent); the
   synthetic recovery check (Idealization 12) validates the classifier's
   threshold LOGIC, not this specific numeric multiplier.
9. **NETD is an instrument/detector threshold, not a human-eye one** —
   any classification derived from this cycle's `dt_ss_full_K` does NOT
   bear on constraint-3/4's human-eye verdict.
10. **This cross-check bears only on T28's own confound-mechanism question
    and constraint-3's energy-ledger bookkeeping.** It does not test
    constraints 1/2/4, and does not re-open or re-score
    `REALIZABILITY_MEMO.md`'s verdict.
11. Not this cycle's mandate, named but not scored: the near-unanimous #1
    grazing-incidence validity check (`edge_diffraction_c_empty_corrected`,
    PHOTONICS' charter), the x-wall wavelength-generality leg (11 cycles
    deferred), the full-scale null-calibration re-run, and R12-into-
    standard-practice — real, overdue T28 board items for Iteration 65.
12. The synthetic classifier-recovery check (Phase-2 fix 4) validates the
    classification pipeline's own bucket logic at decade boundaries; it is
    NOT a null-permutation test against this run's own real data (R5's
    literal look-elsewhere machinery does not apply to a 3-point ratio
    comparison) and is not represented as one.

## Predictions (frozen, committed BEFORE any Phase-4 code runs — see
`phase3_synthesis.md` for full derivation, falsifiers, and the Phase-2
fix-by-fix mapping)

1. **P1 (vacuum-footprint precondition):** PASS at every `BOX_A`/`BOX_B`
   cell, both configs. HALT if it fails.
2. **P2 (reproduction precondition):** fresh `C_empty(cfg,θ)` at
   θ∈{36.0,38.6,41.8}° reproduces `experiments/083-.../results.json`
   exactly, max|Δ|<1e-9. HALT if it fails.
3. **P3 (box independence):** `box_dev_ext`/`box_dev_abs` reported at all
   6 (cfg,θ) cells, both legs — context, not gating.
4. **P4 (`xi_ext` verification gate, NEW):** predicted PASS (`≤0.12`) at
   every (cfg,θ,box,leg) cell, stated with only moderate confidence — a
   genuinely never-tested combination. HALT before P7 if violated anywhere.
5. **P5 (synthetic classifier-recovery check, NEW):** predicted PASS —
   the pipeline recovers the intended bucket at every decade-boundary
   synthetic test case.
6. **P6 (settling spot-check, NEW, disclosed not gating):** no
   pre-registered band; reported for context alongside P7.
7. **P7 (PRIMARY, pre-registered, falsifiable):** `ratio_k(θ) =
   frac_p_abs(θ)/frac_contrast(θ)` at each resolved angle, classified
   ENERGY-DECOUPLED (`<0.1` at every resolved angle) / CONSISTENT
   (`0.1–10` throughout) / ENERGY-DOMINANT (`>10` anywhere) / MIXED /
   DEGENERATE (<2 resolved angles). **Predicted: ENERGY-DECOUPLED at ≥2 of
   3 angles**, moderate confidence, corroborative not dispositive.
   Falsified by CONSISTENT, ENERGY-DOMINANT, MIXED, or DEGENERATE.
8. **P8 (scene-specific detectability):** `netd_disposition` predicted
   UNDETECTABLE at every (cfg,θ) cell — **NETD is an instrument/detector
   threshold, not a human-eye one; this does NOT bear on constraint-3/4's
   human-eye verdict** (carried inline per Idealization 9/Phase-2 fix 8).
   Pre-committed triage rule: any departure must be checked against this
   program's own already-measured material-identity swing magnitudes
   (~780× Biot, ~116× H_CONV) before being read as new physics.
9. **Non-negativity gate (hard assertion, not a scored prediction):**
   `sigma_abs≥0`, `p_abs_w≥0` everywhere. HALT if violated.

## Result

**Call-count correction, disclosed (cosmetic, non-substantive):** the
frozen plan's own §Frozen-configuration table stated 14 new FDTD calls (12
main + 2 settling). The actual settling spot-check (mirroring exp-083's own
idiom exactly, as stated) needs only ONE extra call — the article leg
re-run at `STEPS=1400`, reusing the main sweep's already-produced empty-leg
capture as the reference in both the 2800- and 1400-step comparisons — so
the correct, and actual, total is **13** (12 + 1). `run.py`'s own
Idealizations-7-citing comment states this reuse explicitly; the frozen
text's "14" double-counted an unneeded second empty-leg call. Verified: the
implemented script performed exactly 13 FDTD calls (`run_output.txt`,
`results.json::total_new_fdtd_calls=13`).

**An instrument finding, found and fixed before any classification was
trusted (not silently patched) — corrected same-shift per Red Team's
Phase-5 final audit §1, a historical-accuracy fix, not a substantive
one:** the first run produced `sigma_abs<0` at every one of 12
(cfg,θ,box) cells — failing the pre-registered non-negativity gate
outright. Traced to source, not worked around: `lab/sections.py::widths()`'s
own `i_inc` is a **signed** +x-direction flux at the reference strip.
T28's `PAIR_PAD` geometry has `src_x>obj_x>plane_x` (confirmed from
`dg069.CONFIGS`) — the wave propagates in **-x** — so `i_inc` is,
correctly, negative, and every `sigma_*` field (each a power divided by
this one signed scalar) flipped sign together. **Corrected wording (this
was NOT the first `widths()` application to this geometry): EM's Phase-5
review, and Red Team's Phase-5 final audit independently from source,
found `experiments/024-ambient-margin-adjudication` has the IDENTICAL
`src_x(300)>obj_x(170)>plane_x(77)` relationship and already defensively
wraps `abs()` around `sigma_abs*i_inc` and `net_box_flux` at its own
gates (`run.py` lines 195-199) — three independent facts (identical
geometry; unchanged `widths()` code since exp-002; a defensive `abs()`
wrap around exactly the two quantities this cycle shows are sign-flipped
together) make "the same defect, present and silently absorbed at
Iteration 2, never diagnosed" the better-supported reading. What IS
genuinely novel this cycle is the diagnosis (naming the hazard, tracing
it to `sections.widths()`'s own `sx()` convention, confirming it via an
independent invariance argument, fixing it with a documented, zero-`lab/`-
diff wrapper) — not the underlying defect's existence.** Confirmed NOT
scattered noise: `sigma_ext` and `sigma_ext_cross` agreed on the same
negative sign to <0.05% (`xi_ext`, already computed, is sign-invariant and
unaffected). Fixed with a caller-side wrapper,
`widths_direction_corrected()`, in `run.py` — **zero `lab/` diff**
(confirmed: `git diff --stat -- lab/` empty throughout): recovers each raw
power and re-normalizes by `abs(i_inc)` (the physically correct choice —
an intensity normalizer must be a magnitude, not a directionally-signed
flux; independently re-derived from `_face_flux`/`_cross_flux`'s own
coordinate-invariance by EM's Phase-5 review and Red Team's final audit —
only `i_inc` needed correcting, confirmed sound, not masking a subtler
defect). Because `xi_ext`/`box_dev_*` are ratios of differences to
magnitudes, both already-computed and already-gated (P3/P4, both PASS,
`xi_ext≤0.00048` everywhere — the extinction-routes-agreement identity
holds cleanly even at this never-before-diagnosed oblique/
`graded_black_shell`/PAD-shifted-box combination, EM's own
moderate-confidence P4 prediction confirmed) are provably invariant to
this correction and were not recomputed.

**A separate, related, non-blocking latent defect, flagged forward, not
fixed this cycle (EM's Phase-5 review, confirmed by Red Team's final
audit):** `sections.py::widths()`'s own `back_frac`/`fwd_frac` fields
carry the same uncorrected +x-propagation assumption (the labels are
inverted for a -x-propagating scene) — `widths_direction_corrected()`
does NOT touch these fields (confirmed from `run.py`: only
`sigma_scat`/`sigma_abs`/`sigma_ext`/`sigma_ext_cross` are reassigned).
This cycle's own scored conclusions (P7, P8) never read `back_frac`/
`fwd_frac` — confirmed by reading `run.py::main()` in full — so nothing
here is corrupted, but any future consumer of this cycle's own
`results.json::widths` fields, especially for a constraint-2-adjacent
"no specular return" question, would get the physically backward answer
if read at face value.

**P1 (vacuum footprint): PASS**, all 4 (cfg,box) cells, both configs.
**P2 (reproduction): PASS**, `max_dev=0.0` exactly (bit-identical, not
merely within tolerance) against `experiments/083-.../results.json`'s own
committed `C_empty` figures at all 3 angles, both configs.
**P4 (`xi_ext`): PASS**, `≤0.00048` everywhere (12 cells) — comfortably
inside the `≤0.12` tolerance, the never-before-tested extinction-routes
identity holds for `graded_black_shell` at oblique incidence.
**P5 (synthetic recovery): PASS**, all 14 decade-boundary/bucket test cases
recovered exactly. **Non-negativity gate: PASS** (after the direction
correction above). **P6 (settling): reported, not gating** —
`rel_dev(sigma_abs)=7.9×10⁻⁵`, `rel_dev(sigma_ext)=9.4×10⁻⁴` at
`G40`/θ=38.6°/`BOX_A` — small, no red flag for the new channel's own
settling at `STEPS=2800`.

**P7 (PRIMARY): FALSIFIED — classification is ENERGY-DOMINANT, not the
predicted ENERGY-DECOUPLED.**

| θ | frac_p_abs | frac_contrast | ratio_k | resolved |
|---|---|---|---|---|
| 36.0° | 1.965×10⁻³ | 7.438×10⁻⁴ | 2.64 | yes |
| 38.6° | 4.001×10⁻³ | 7.410×10⁻⁵ | 53.99 | yes |
| 41.8° | 7.214×10⁻³ | 1.263×10⁻³ | 5.71 | yes |

All 3 angles resolved (the noise-floor gate clears comfortably at every
angle — this is a real, well-powered measurement, not a marginal one).
`θ=38.6°` alone reads `ratio_k=53.99>10` (label X), which under §4's own
stated priority (any resolved angle over `RATIO_HIGH` ⇒ ENERGY-DOMINANT
outright) drives the overall classification, regardless of the other two
angles' own labels.

**A disclosed, independently-checked candidate explanation for the θ=38.6°
outlier specifically — not adopted as settled, flagged for Phase 5.**
Checking `experiments/083-.../results.json::per_theta` around 38.6°
directly (not asserted, read): `delta_scene(θ)` — the Weber-contrast
confound curve `frac_contrast`'s own numerator depends on — crosses zero
almost exactly AT 38.6°: `37.6°→+1.587e-3, 38.0°→+1.923e-3, 38.4°→+8.08e-4,
**38.6°→-4.15e-5**, 38.8°→-8.57e-4, 39.2°→-1.829e-3`. `θ=38.6°` sits within
one 0.2° grid step of this curve's own genuine node — `frac_contrast`'s
denominator (`|C40_C(38.6°)|`, not itself near zero) is fine, but its
*numerator* (`|delta_scene(38.6°)|=4.15×10⁻⁵`) is anomalously small purely
because the confound oscillation happens to cross zero there, which alone
would inflate `ratio_k` regardless of the article's real absorbed-power
behavior. This is a plausible, quantitatively consistent explanation for
the θ=38.6° outlier specifically (a near-zero-crossing denominator
artifact, not a real physical energy-dominant regime at that one angle) —
disclosed as a candidate, independently checked from source, NOT resolved
or adopted as the final reading; Phase 5 should scrutinize it rather than
accept it on this NOTES.md's own say-so.

**This explanation does NOT rescue the pre-registered prediction, even if
fully credited.** Excluding θ=38.6° as a node artifact, the remaining two
angles (36.0°, 41.8°) both read `ratio_k∈{2.64,5.71}` — squarely inside the
**CONSISTENT** band (`0.1–10`), not the predicted **ENERGY-DECOUPLED**
(`<0.1`). The bulk-integrated absorbed-power PAD-sensitivity and the
localized Weber-contrast PAD-sensitivity are, at these two "clean" angles,
comparable in fractional magnitude — a genuine, non-artifactual departure
from ten-plus cycles' own phase/interference-only prior, not merely a
single-point aliasing/node fluke. **Falsified as pre-registered — a
materially new finding warranting immediate follow-up, per this document's
own §Falsifiers language, not a failure of this proposal.**

**P8: predicted UNDETECTABLE, confirmed at all 6 (cfg,θ) cells — NETD is
an instrument/detector threshold, not a human-eye one; does NOT bear on
constraint-3/4's human-eye verdict** (carried inline per Idealization 9/
Phase-2 fix 8) — `dt_ss_full_K` ranges `4.52×10⁻⁵` to `5.35×10⁻⁵` K, NETD
margin (`0.020K/dt_ss`) ranges **≈374×–442×** — comfortably clear, same
order as this flagship absorber's every prior disposition (T5/exp-043/
exp-057). No triage-rule trigger (fix 6 N/A this cycle — P8 did not depart
from UNDETECTABLE). THERMODYNAMICS' Phase-5 review additionally ran a
**swing-specific (differential) NETD recomputation** — whether the
ENERGY-DOMINANT swing itself, not just each cell's absolute `dt_ss`,
carries a detectability consequence — confirming margins of
52,000×–225,000×, even more comfortably UNDETECTABLE; formalized here as a
standing check for any future cycle citing a large fractional
absorbed-power swing. Separately, THERMODYNAMICS' review found the
`iso_xsec_sq`-vs-infinite-rod area convention (Idealization 3) scales
`ratio_k`'s numeric value by roughly 1.5–2× without changing any
classification bucket — disclosed as a standing citable caveat wherever
this cycle's exact `ratio_k` figures are next quoted.

**Aliasing-risk-band log (fix 10):** the actual, non-uniform grid sits
8.5–12.6% from exact integer-cycle resonance against both `P_edge_A` and
`P_star` at both gaps — meaningfully clearer of the aliasing condition than
Phase 1's original uniform 3.0° spacing (1.8% from exact resonance against
`P_star`), though not zero risk; disclosed for any future reviewer citing
this cycle's own angle choice.

**Restored (Phase 5, VISION/MATERIALS; correction to a Phase-3 renumbering
that silently dropped it): the informal T9-anchor comparison Phase 1's own
§4-P4 promised** (`σ_abs(cfg,θ)/σ_ext(cfg,θ)` at `BOX_A`, informally vs.
T9's established broadside anchor `σ_abs/σ_ext=0.51`). Computed for free
from data already in `results.json`: `ratio_abs_ext` measured 0.5128–0.5138
across all 6 (cfg,θ) cells — within 0.55%–0.75% of the broadside anchor.
**A genuine, first-ever, essentially free confirmation that T9's
near-field extinction-paradox ratio generalizes cleanly to 36°–42° oblique
incidence** on this flagship absorber — resolving, in the affirmative, the
"genuine uncertainty" the original proposal's own P4 context section
explicitly left open. Worth logging against T9 in LOGBOOK.

## Learned

**Combined Verdict: PARTIAL** (unanimous across all six blind Phase-5
seats — PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS, VISION
SCIENCE, THERMODYNAMICS — and Red Team's Phase-5 final audit). The
forward tripwire is genuinely discharged, letter and intent: a real,
purpose-built, 13-call, well-powered FDTD measurement was built and run,
not a sixth deferral. Red Team's final audit weighed and adopted the
argument (raised independently by multiple Phase-5 reviews) that a
falsified prediction is, if anything, MORE credible evidence of a genuine
discharge than a confirming one would have been: this cycle's own lead
seat pre-registered its preferred hypothesis (ENERGY-DECOUPLED) with only
moderate confidence, built a genuinely gated instrument (P1/P2/P4/P5/
non-negativity, all HALT points), and reported the opposite of that
preference. The PRIMARY metric (P7) is genuinely FALSIFIED: even crediting
in full the disclosed θ=38.6° denominator-artifact explanation (confirmed
quantitatively sufficient, independently, by PHOTONICS, QUANTUM,
THERMODYNAMICS, and Red Team's own final audit — the true zero-crossing
sits at θ₀≈38.590°, ~0.01° from the sampled point), the remaining two
angles (36.0°, 41.8°) read CONSISTENT (`ratio_k`=2.64, 5.71), not the
predicted ENERGY-DECOUPLED — a materially new, robust finding against
ten-plus cycles' own phase/interference-only prior for this sub-thread.
The filed classification (ENERGY-DOMINANT, driven by θ=38.6° under the
pre-registered "any resolved angle over 10" priority rule) stands as the
official record of what the frozen pipeline computed — Red Team's audit
explicitly declined to retroactively relabel it against a gate that did
not exist in the frozen Phase-3 spec, the same house discipline that
governs every other post-hoc-rationalization risk this program guards
against (R8's lineage). **New standing rule R13 adopted** (LOGBOOK.md RULED
OUT registry, full text there): a ratio classifier whose denominator is
built from a quantity with real, knowable zero-crossings must be
floor-gated on that denominator's own magnitude before a decade-threshold
classification is trusted at a single sampled point — a genuinely new
failure mode (an algebraic instability, present even at zero measurement
noise) distinct from the R5/R10 statistical-look-elsewhere lineage. Does
not fire on its own founding instance (exp-087), matching every prior
rule's own founding-instance precedent. **Checkpoint criterion 2: N/A**,
confirmed independently, matching every T28 desk/instrument cycle since
exp-069. **Checkpoint criterion 4: does NOT fire** on any of five matters
this cycle's own layered review surfaced (the corrected "first-ever"
historical claim; a third instance of the NETD/constraint-3
disclaimer-erosion shape, closed same-shift, with a NEW forward tripwire
set — a fourth instance fires automatically; the vanished T9-comparison,
restored above; a false "reproduced bit-exact this cycle" citation in
Phase 1's own parameter table that survived five blind Phase-2 critiques
and Red Team's own Phase-2 audit, caught only at Phase 5 — logged as
reinforcing R4's existing discipline, not a new rule; the inverted
`back_frac`/`fwd_frac` labels in `lab/sections.py::widths()`, flagged
forward, non-blocking) — every one non-load-bearing to this cycle's own
scored PRIMARY/detectability verdicts, every one caught blind, same
cycle, before this LOGBOOK entry.

## Next

Reconciled Iteration-65 ranking (Red Team's Phase-5 final audit, full
detail `phase5_redteam_audit.md`): **Tier 1, cheap FDTD, near-unanimous
next** — (1) the decisive 8-call bracketing follow-up at θ=38.4°/38.8°
(QUANTUM) — cheapest, fastest, single most decisive resolution of the
node-artifact-vs-genuine-physics question; (2) extend the
energy-interception channel to the full/denser 31-point window, computing
`σ_abs(C40,θ)`/`σ_abs(G40,θ)` individually (not merely their difference) —
MATERIALS' falsifiable "passive transducer, not resonant source" test; (3)
apply R13's new denominator floor gate to this cycle's own already-
collected data and report the corrected classification (zero new FDTD).
**Tier 2** — institutionalize the extinction-routes-agreement identity for
`graded_black_shell` obliquely as a permanent stage-8 suite row; extend the
validated measurement to `PAIR_ABSORB40`/`C80−C40` and to 450/750nm; extend
to the near-null σ(I) article (the class that actually matters for
constraint-3 realizability); a bounded audit of whether any other T28
ratio construction shares R13's hazard. **Tier 3, standing, unaffected by
this cycle** — PHOTONICS' grazing-incidence validity check (still
near-unanimous #1 on the whole T28 board); the x-wall wavelength-
generality leg (now TWELVE consecutive cycles deferred, 076–087, the
single oldest board item); the still-queued full-scale null-calibration
re-run; R12-into-standard-practice; PHOTONICS'/EM's leg-(b) work; QUANTUM's
lossless-PEC-only-disk control; hardening `sections.py::widths()` itself
to normalize by `abs(i_inc)` internally (now TWO independent instances,
exp-024 and exp-087, of the same latent geometry tripping this issue) —
scope as its own small, gated `lab/`-change proposal, not a same-shift
patch; the still-unresolved ritualization governance question (Iteration
61).
