# exp-052 — The Fixed-Absolute-Thickness `graded_black_shell` Variant's Own C

*Panel Iteration 29. Lead: THERMODYNAMICS (rotation), executing PLAN.md's
LOCKED, UNCONDITIONAL Iteration-29 trigger (MATERIALS' own idea, first
queued Iteration 7, deferred 21 iterations, granted unconditional status by
Red Team at Iteration 28). Realizability/instrument-construction cycle.
**T1 escape route: NONE.** No constraint-3/4 PASS/MARGINAL/FAIL language is
issued or implied — this is an opaque, τ_shell=24 absorber, not a
near-threshold article.*

**The design below is the Phase-3-corrected design, not the raw Phase-1
proposal.** `phase1_proposal.md` stands unedited as the historical record
per this program's "flag, don't rewrite" convention. Full accepted/
overridden record: `phase3_synthesis.md`. Phase-2 critiques (five blind
seats) and Red Team's audit: `phase2_critique_*.md`, `phase2_redteam_audit.md`.

## Hypothesis

Every `graded_black_shell` reading this program has ever cited — including
the C≈−0.72 anchor underlying T8/T13/T14 — comes from a **self-similar**
construction (`r_in ∝ r_out`) whose absolute shell thickness diverges to
0.31–0.92 m at witness scale (`REALIZABILITY_MEMO.md` Entry 2) — no
macroscopic real-material precedent. Real ultra-black coatings carry a
**fixed absolute thickness independent of substrate size** — the opposite
scaling law, argued but never built in 21 iterations.

**Hypothesis (MATERIALS, Iteration 7; tested here for the first time):** a
fixed-absolute-thickness shell (`r_in(r_out) = r_out − 48` cells,
`sigma_max` held fixed at 0.5, not rescaled) does **not** reproduce T13/
T14's wrong-direction shallowing (`graded_black_shell`'s established C
*shallowing* rather than *deepening* toward −1 as scale grows) at the same
strength as the self-similar family — because a fixed-width rim-leak
channel becomes a shrinking fraction of a growing silhouette, unlike the
self-similar family whose leak channel grows in lockstep with the object.
Falsifiable either direction (P-3, below).

## Setup

**Domain-construction geometry reused verbatim from
`experiments/030-scale-bridge/design_geometry.py::geometry()`** (imported,
not copied) — `PLANE_DX=15`, `ABSORB=TAPER=40`, N9 fallback angle set
(±35°/±25°/±15°/±5°/0°), same `NX/NY/OBJ/PLANE_X/D_SP/STEPS_AMBIENT`
formulas at r∈{78,156,312}. Only the object's material law differs — this
isolates the geometric-law question from any domain confound.

**Material law, fixed-absolute family:** `r_in(r_out) = r_out − 48`,
`sigma_max = 0.5` (fixed), `eps_max = 1.0`. `τ_shell = 24.0` at every r_out
(printed-assertion-verified). **PEC-cored** (`materials.pec_disk(r_in)`
then `materials.graded_black_shell(r_in, r_out, ...)`), a Phase-3
correction — see Accepted Fixes, below.

**Material law, self-similar comparator (re-measured, not inherited):**
`r_in(r_out) = round(30/78 · r_out)`, `sigma_max = 0.5/κ`, also PEC-cored,
τ_shell=24.0 identically. This is `experiments/030-scale-bridge`'s own
established construction, corrected for the core-fill defect described
below and re-run at the N9-ambient level — not read from exp-030's own
`results.json`, which is hollow-core and uncorrected at that level.

**Single wavelength, 600nm, cpl=20** (idealization, scoped explicitly —
see Idealizations). N9 fallback angle set at every r_out.

**r=78: zero new FDTD calls.** `r_in_fixedabs(78) = r_in_selfsim(78) = 30`
and `sigma_max = 0.5` in both families — both constructions coincide
exactly with `experiments/030-scale-bridge/design_geometry.py::
C78_ESTABLISHED['absorber'] = −0.7208684660449545` (sourced from exp-024,
itself PEC-cored — confirmed by Red Team, so this one anchor needs no
correction). **P-0** is this identity, verified in code
(`design_geometry.py`'s own printed assertions), not a measurement.

**r=156: mandatory.** r=312: **cost-gated** — one timing pilot run before
committing to the full leg, exactly `experiments/030-scale-bridge`'s own
precedent (whose r=312 leg cost 3.87h for 37 runs, ~28.6× the r=156 rate —
the largest timing miss in this program's history). If the pilot
extrapolates unfavorably, the r=78→156 result stands alone as this cycle's
committed finding, not a provisional one — same convention as the original
Phase-1 proposal's own §7.

## Accepted Fixes (Phase 2 → Phase 3, Red Team's docket, all 9 items — see `phase3_synthesis.md` for the full accepted/overridden record with each seat's own critique quoted)

1. **[ELECTROMAGNETISM, Red-Team-verified LOAD-BEARING]** Both families
   built **PEC-cored**, not the hollow construction `experiments/030-scale-
   bridge/run.py::build_ambient` silently used. Confirmed directly in code:
   that function's `"absorber"` branch calls only `graded_black_shell`, no
   `pec_disk` — the exact defect `experiments/031-ripple-core-
   reconciliation` diagnosed and fixed for its own θ=0 diagnostic, never
   propagated back into exp-030's own committed `results.json`.
2. **[Red Team, new]** The self-similar comparator is **re-measured here**,
   PEC-cored, at the full N9-ambient instrument, closing the "uncorrected
   comparator" gap on both sides of every P-1/P-2 delta.
3. **[Red Team, new — Director's redesign]** Red Team's own proposal (a
   `radial_absorbed_power` ledger check) is replaced with a cheaper,
   better-targeted test: a **core-fill check using the SAME validated N9
   ambient instrument** — run the fixed-absolute object both PEC-cored and
   HOLLOW at θ=0, r=156 (and r=312 if run), and compare C directly. This
   routes around a known-broken instrument: `experiments/031-ripple-core-
   reconciliation/run.py::run_thermo` is guarded with a live
   `NotImplementedError` because no validated `box`/`ref` convention exists
   for a box-ledger σ_abs/σ_ext measurement on THIS scene class (ambient/
   line-source, not the beam-scene class `radial_absorbed_power`/`widths()`
   were validated on) — reusing that machinery here would risk silently
   reproducing the identical failure. The N9 ambient contrast itself needs
   no such convention and is exactly what this cycle scores anyway.
4. **[Red Team, cosmetic-but-must-fix, house rule R4]** The Phase-1
   proposal's own `C78` citation (−0.7211) is corrected to the actual
   `design_geometry.py::C78_ESTABLISHED` value (−0.7208684660449545,
   rounds to −0.7209) — re-derived here by import, not hand-copied a
   second time.
5. **[PHOTONICS, scope fix]** P-3's T14 verdict is scoped explicitly to
   **600nm only**. The mechanism argument (thickness-in-wavelengths) is
   itself λ-dependent (1.92λ–3.2λ across this program's 3λ sweep at fixed
   1.44µm) — a single-λ result cannot license the program-general claim
   the original wording implied. No new-λ run added (cost discipline, Red
   Team's own offered alternative to a new run).
6. **[MATERIALS, desk-only]** §9's realizability note gets the implied
   absorption e-folding length (`τ_shell/thickness = 1/60nm`, computed in
   `design_geometry.py`) — the PLAUSIBLE-not-PUBLISHED claim is now stated
   honestly as **thickness-only**, absorptivity unchecked (no primary
   CNT-forest absorption-coefficient citation exists in this program; T18's
   WebFetch block, unaddressed this cycle, is why).
7. **[QUANTUM, Director scope call — NOT re-measured this cycle]** The
   coherent-vs-incoherent bridge gate (`experiments/029`'s stage-11 idiom)
   was validated only at shell-fraction 61.5% (r=78, where both families
   coincide); this cycle's r=156 result sits at 30.8%, untested.
   **Correction, added at Phase-5 close (Red Team's audit, §1c/§2a —
   caught by a fresh Phase-5 QUANTUM instance, sharper than this item's own
   pre-freeze framing): the gap is larger than "untested at a new shell
   fraction" states.** `experiments/029/run.py` injects a strong on-axis
   beam (amplitude=1.0) PLUS one weak off-axis probe (amplitude=√2×10⁻⁴)
   simultaneously on a beam-scene object — a structurally different
   configuration from `lab/ambient.py`'s actual instrument, which sums NINE
   separate, EQUAL-amplitude single-source runs post hoc as intensities.
   Exp-029's own small cross-term ceiling (≈2.83%) is a property of that
   specific amplitude asymmetry and bounds nothing about the equal-amplitude
   case. **No geometry this program has ever run — not r=78, not any prior
   cycle — has had the actual ambient-sum instrument's cross-term
   empirically bridge-gated.** This is a program-wide open question, not an
   exp-052-local one; see `LOGBOOK.md`'s new live thread opened at
   Iteration 29 close. Re-implementing a correctly-configured gate for a new
   ambient-scene object under this shift's time budget was judged too
   error-prone to attempt cleanly — **disclosed as an open assumption, not
   silently assumed clean.** Physical argument for low risk (stated, not
   proven): the measured cross-term's smallness (+0.0224% aggregate) is a
   property of the N9 angular-averaging/source geometry, unchanged here —
   not obviously a function of the object's own shell thickness. Queued as
   a named Iteration-30+ follow-up (not this program's Iteration-30 slot,
   which is separately LOCKED to VISION's stage-10 temporal instrument).
8. **[VISION, band widened not re-measured]** P-2's r=312 falsifiable band
   widened to ±0.00156 (2× T16's own measured r=156 angular-quadrature +
   domain-construction uncertainty budget, 7.80×10⁻⁴) rather than a new
   per-angle floor spot-check — Red Team's own offered cheaper alternative.
9. **[Red Team, disclosure-only]** A clean R-gate pass (P-4) bears on
   flat-wall normal-incidence reflectance only — explicitly does **not**
   license any inference about the core-fill (fix 1/3) or comparator
   (fix 2) questions above. Stated here, not left implicit.

**Nothing overridden.** All nine items land as specified or via Red Team's
own offered cheaper alternative (items 5, 8) — no seat's concern was judged
unfounded.

## Idealizations (stated honestly)

1. **Single λ=600nm** — P-3's own claim is scoped to this wavelength only
   (fix 5); the 3λ generalization question stays genuinely open.
2. **r=312 is cost-gated, not committed** — if deferred, T14's own
   asymptotic-shape question (needs a 3rd point for any fit) is only
   partially answered; the r=78→156 direction test stands alone.
3. **δ_C empty-scene floor / settling: inherited from exp-030's own r=156/
   312 domain measurements, not re-verified this cycle** — both are
   properties of the empty domain (independent of object interior), and
   this cycle's domain is bit-identical to exp-030's. Disclosed, not
   silently assumed.
4. **The coherent-vs-incoherent bridge-gate assumption is untested at this
   geometry** (fix 7, above) — argued low-risk, not measured.
5. **The core-fill check (fix 3) is θ=0-only**, not a full N9 sweep — same
   scope T9's own original diagnostic used (exp-027/031 precedent).
6. 2D TMz, single-pass, no coherent beam-divergence interaction (ambient
   incoherent sum only) — same standing idealizations as every other
   `lab/ambient.py` reading.
7. Engine-trust caveats (`VALIDATION.md`) apply as usual and are inert here:
   no spatial-wavelength extraction (FFT quantization moot), no cloak
   object (PEC-flush lesson moot), not a cross-solver comparison
   (scattered-vs-total lesson moot); the reflection-monitor-placement
   lesson is baked into the reused R-gate idiom.

## Predictions — committed BEFORE any run (house discipline)

**P-0 (gate, code-only, verified already in `design_geometry.py`'s own
printed assertions before this file was committed):** `r_in_fixedabs(78) ==
r_in_selfsim(78) == 30` and both `sigma_max(78) == 0.5` — both families
coincide exactly with the established r=78 anchor. **Falsified if any
transcription drift breaks this identity.**

**P-1 (primary, r=156, mandatory).** Established comparator (corrected,
fix 4): `C78 = −0.7208684660449545`. Predicted:
**`C_fixedabs(156) ≤ −0.7255`** — deeper (more negative) than the
re-measured, PEC-cored `C_selfsim(156)` by a margin the cycle's own
mechanism argument requires (fixed-width leak channel shrinking as a
fraction of a growing silhouette). Scored in code as:
- **CONFIRMED** if `C_fixedabs(156) ≤ −0.7255` **and**
  `C_fixedabs(156) < C_selfsim(156)` (deepens, and deepens further than the
  corrected self-similar comparator at the same r_out).
- **PARTIAL** if `C_fixedabs(156) < C78` (deepens from the r=78 anchor at
  all) but either the −0.7255 threshold or the vs.-comparator ordering
  above misses.
- **REFUTED** if `C_fixedabs(156) ≥ C78` (shallows or holds flat) — the
  result that would say removing the self-similar family's growing-
  thickness confound does NOT change the wrong-direction pattern.

**P-2 (conditional on r=312 running).**
`C_fixedabs(312) < C_fixedabs(156)` (continues to deepen) by at least the
widened band **±0.00156** (fix 8): **CONFIRMED** if
`C_fixedabs(156) − C_fixedabs(312) ≥ 0.00156`; **REFUTED** if
`C_fixedabs(312) ≥ C_fixedabs(156)` (flat or reversed, within the same
band — the T14 pattern, undiminished); **PARTIAL** otherwise (a real but
sub-band-width deepening).

**P-3 (T14 verdict, 600nm-only per fix 5, falsifiable either way).**
*The fixed-absolute-thickness construction does NOT reproduce T14's
wrong-direction shallowing, at 600nm, at the same strength as the
self-similar family.* CONFIRMED if P-1 reads CONFIRMED or PARTIAL and P-2
(if run) does not REFUTE; REFUTED if P-1 REFUTES — meaning T14's
shallowing is a property of the absorber's near-field/rim-diffraction
geometry generally at 600nm, not an artifact of the self-similar family's
growing-thickness confound specifically.

**P-4 (R-gate, mandatory pre-run diagnostic).**
`R_coat ≤ 0.002` (established 0.2% flat-coating gate), expected
comfortably inside — same profile shape/steepness as the already-gated
r=78 object. **CONFIRMED** if ≤0.002; **hard-stop, do not trust P-1** if it
fails. **Disclosure (fix 9): a pass says nothing about fixes 1–3.**

**Disclosure, added at Phase-5 close (Red Team's Phase-5 audit, item 1 of
its "must land before this cycle closes" docket — not present in the
pre-freeze text above, added here rather than rewritten into it, per
"flag, don't silently rewrite"):** the Phase-1 proposal's ORIGINAL P-5 was
a THERMO energy sidecar (`ΔT_ss` vs. NETD, `lab/thermo_sidecar.py`) — it
was **never computed this cycle**. The "P-5" label below is Red Team's own
Phase-2 item 3 (a core-fill check), Director-redesigned at Phase 3 and
written under the reused P-5 label — a different prediction entirely, not
a renamed version of the same one. Grep confirms: zero references to
`thermo_sidecar`, `ΔT`, or `NETD` anywhere in this experiment's `run.py`,
`design_geometry.py`, or `results.json`. Red Team's own Phase-2 audit had
recommended (not blocking) relabeling the original P-5 as an expected,
low-information confirmation rather than scoring it as a genuine test —
that recommendation was never explicitly actioned either way; its label
was simply reused for something else. Both gaps are recorded here and in
`LOGBOOK.md`'s Iteration 29 entry, not silently left for a future cycle to
rediscover. THERMODYNAMICS' own Phase-5 review argues the established T22
area-invariance result gives good reason to expect the standing
UNDETECTABLE pattern survives for this object, but its load-bearing input
(`σ_abs/σ_ext=0.51`) is itself unverified at this cycle's own new
`r_in/r_out` ratios (0.692/0.846, both above the only-ever-tested 0.385) —
"probably fine" is not "measured." A real thermo-sidecar run for this
object needs a genuine box-ledger `σ_ext` measurement first (this
experiment deliberately did not build one — see fix 3's own reasoning,
above, for why the box/ref channel was avoided) — queued as a concrete
Iteration-31+ follow-up, not fabricated here under time pressure.

**P-5 (core-fill check, fix 3, θ=0 only).**
`|C_hollow_theta0(156) − C_fixedabs_theta0(156)| ≤ 0.02` — an order-of-
magnitude-loose band (this is a genuinely untested ratio, 0.692, nearly
2× T9's own established point of 0.385; no prior measurement licenses a
tight prediction). **CONFIRMED (T9 generalizes)** if ≤0.02; **REFUTED (T9
does NOT generalize past ratio 0.385 — core content becomes non-incidental
at large r_in/r_out)** if > 0.02, which would be a load-bearing new
finding requiring the P-1/P-2 comparison itself to be redesigned around a
core-dependent effect (Red Team's own "evidence that would change the
verdict" clause). If r=312 runs, the same check repeats there
(ratio 0.846, an even sharper test).

## Cost note

Mandatory (r=156): 28 ambient runs (9 empty + 9 fixedabs + 9 selfsim + 1
hollow-θ0) + 1 R-gate check. By exp-030's own r=156 timing (~40–84s/run),
estimated **≈20–35 minutes**. r=312: pilot first; exp-030's own r=312 leg
took 3.87h for 37 runs — if the pilot extrapolates comparably, defer with
the r=78/156 result standing as this cycle's own committed finding (not
provisional — P-3 is scored on r=78/156/P-1 alone if r=312 does not run).
