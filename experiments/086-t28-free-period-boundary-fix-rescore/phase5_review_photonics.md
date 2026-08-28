# PHASE 5 — PHOTONICS REVIEW · Panel Iteration 63 · exp-086

*Blind, fresh context. Have not seen any other seat's Phase-5 review this
cycle. Charter: surface interaction, absorption spectra, angular dependence,
scattering cross-sections — is the proposal's optical response coherent as
stated, across wavelength and angle? Raised the grazing-incidence
ptp-amplitude-growth concern at this cycle's own Phase 2.*

## Verdict: **PARTIAL**

The R11 repair is correct, source-verified, and reproduces exactly under
independent re-execution. My own Phase-2 mandatory fix was delivered in
full, not merely claimed. One genuine new defect found this cycle (below) —
not structural, doesn't change the classification, but sharpens exactly what
"recovered" is allowed to mean going forward. T28's own substantive
mechanism question is untouched by this cycle, as intended (zero-FDTD
instrument repair; Checkpoint criterion 2 correctly N/A throughout).

## 1. Was my own Phase-2 mandatory fix actually delivered?

**Yes, in full, verified from the artifacts directly, not from NOTES.md's
description of them.**

- `phase4_rescore_results.json::method_c_rescore.sub_results` — all 37
  records carry both `ptp` and `ss_tot_full` (checked programmatically:
  zero missing). `ptp` ranges `2.558×10⁻⁴` (θc=5°) to `1.696` (θc=69°),
  matching Red Team's independently-recomputed `5,444×`–`6,631×` growth
  figure exactly.
- NOTES.md's Idealizations section carries the required caveat verbatim:
  *"The grazing-incidence amplitude blow-up... is disclosed, not resolved:
  it raises an open question about whether
  `edge_diffraction_c_empty_corrected` remains inside its own valid
  near-field regime there."* `phase3_synthesis.md` fix 5 shows this was
  accepted in full, zero override.

This is the correct outcome and closes the loop on my own charter concern
as far as this cycle's scope goes.

## 2. Were the frozen predictions actually reproduced?

**Yes — independently re-run from scratch, not re-read from the committed
JSON.** I executed `phase4_rescore.py` and
`phase4_null_calibration_controlled_comparison.py` myself in this review
session (not merely diffed the files):

- Full 37-window re-run: `frac_recovered=0.5676` (21/37),
  `classification_a="NOT STABLY PERIODIC"`, boundary set
  `{45,59,61,63,71,73}`, and the three-phase Spearman table
  (`ρ=0.8571/p=0.0238` at phase 5°; `0.4286/0.3536` at 7°;
  `0.5357/0.2357` at 9°) — **bit-exact match** to the committed
  `phase4_rescore_results.json` on this independent re-run.
- Controlled null-calibration comparison: re-ran and got
  `max_r2_over_trials=0.5179691995509128` for BOTH the old-buggy and
  corrected quiet variant (identical to the digit), `boundary_pin_rate=
  0.067` (201/3000) — bit-exact match to the committed results.

This is now (at minimum) the fourth independent computation landing on
these exact figures (Phase 1, Red Team's Phase-2 reimplementation, the
committed Phase-4 run, and this review). Prediction 6's headline numbers
fell outside the pre-registered `[0.56,0.78]` band (actual: `0.518`) but
NOTES.md discloses this honestly and correctly diagnoses it as an
N=3000-vs-N=20000 order-statistic artifact, not an effect of the fix — the
matched-N controlled comparison I re-ran confirms that diagnosis is
correct, not a rescue. The pre-registered Checkpoint-relevant falsifier
(`p_r2_ge_070>0.05` or `max_r2_over_trials≥0.7156`) was correctly NOT
triggered.

I also independently re-traced the source fix in both files (not taking
NOTES.md's or the proposal's description on faith): `pad_round_trip_
model.py` lines ~384–440 (`free_period_with_widening` and `_quiet`) and
`y_wall_prescreen.py` lines ~325–379. Both apply the identical `for...else`
correction — `else: chosen = <widest-stage record>; chosen["converged"]=
False; chosen["no_interior_optimum"]=True` — which only fires when the
loop completes without a `break`, i.e. exactly when every stage was
`at_boundary`. This is algebraically the correct, minimal R11 fix at both
sites, matching every seat's Phase-2 claim.

## 3. New finding this review: amplitude heterogeneity *inside* the
   "recovered" set itself, not just recovered-vs-boundary-pinned

My own Phase-2 attack was about the boundary between recovered and
not-recovered. Now that `ptp`/`ss_tot_full` are actually persisted (per my
own fix), I checked something nobody in the record yet has: **is the
21-window "recovered" set itself amplitude-homogeneous?** It is not.

```
recovered set: ptp ranges 2.558e-04 (θc=5°) to 1.258e-01 (θc=57°)
ratio: 491.7×
```

Twenty of the 21 recovered windows sit in the near-normal cluster
(θc=5°–43°, `ptp` spanning `2.6×10⁻⁴` to `2.1×10⁻²`, itself an ~80×
internal spread but a contiguous physical regime). One recovered window —
**θc=57°** — sits inside the grazing-incidence region flanked on both
sides by boundary-pinned windows (59°, 61°, 63° are all `converged=False`),
with `ptp=0.126`, three orders of magnitude above the bulk of the
near-normal cluster and comparable in scale to the confirmed
shadow-boundary-adjacent blow-up. The uniform `r2_local≥0.30` bar
(unchanged from Phase 1, correctly not re-litigated this cycle) counts
θc=5° and θc=57° as equally "recovered" evidence feeding the same
`frac_recovered=0.568` headline, even though the physical regime they sit
in is not obviously the same one.

**Mitigating nuance, also newly checked**: the one Spearman phase that
clears significance (θc-start=5°: `ρ=0.857, p=0.024`) draws its 7 points
from `{5°,11°,17°,23°,29°,35°,41°}` — entirely inside the near-normal
cluster, θc≤41°. θc=57° falls in the *9°*-phase stride instead, which does
**not** clear significance (`ρ=0.536, p=0.236`). So the one significant
result this cycle reports is not itself contaminated by the grazing-region
outlier — a fact the record doesn't currently state either way, worth
adding.

This is not a defect that changes `classification_a` (the gate is
`frac_recovered<0.80`, and 0.568 fails it regardless of internal
homogeneity) — it does not overturn anything filed. But it is a genuine,
independently-derived sharpening of exactly the caveat my own Phase-2
critique named: "recovered" is a fit-quality label, not a same-physical-
regime label, and the data now exists (because the fix I asked for
persisted it) to show that gap is real, not hypothetical.

## 4. Grounding the grazing-incidence caveat in the actual model source

Traced `edge_diffraction_c_empty_corrected` to its defining primitives
(`experiments/048-evidentiary-chord-closure/design_geometry.py::
field_and_h`/`_src_amp`/`_geom_derived`): a bare scalar Kirchhoff-Huygens
coherent sum over aperture points, using the free-space 2D cylindrical
Green's function `G0=exp(i(kr−π/4))/√r` and a simple `d_sp/r` obliquity
weight — no Fresnel-transition or UTD-style shadow-boundary correction
term anywhere in the chain. A bare scalar-diffraction sum of this kind is
known to become inaccurate (formally singular in the geometrical-optics
term) exactly at shadow boundaries / grazing incidence, which is
independently consistent with — not merely coincident with — the observed
`5,444×`–`6,631×` amplitude blow-up concentrated at θc≈59°–73°, precisely
where 6/6 boundary-pinned (non-converged) windows also cluster. This
strengthens (does not overturn) the already-disclosed caveat: it is not
just "amplitude happens to be large there," it is the textbook signature
of the specific approximation this model makes running out of validity in
exactly the region the fix correctly declines to certify a period for.

## 5. Minor, non-blocking finding: prior-citation audit's scope silently narrowed

`phase1_proposal.md`'s own table (§2) committed to scanning **21 files**
across **experiments 069–085**, with a two-track method: read explicit
`at_boundary` keys where present, else flag any period-like numeric field
near a stage boundary as a candidate. The actually-executed
`phase4_prior_citation_audit.py` scans **18 files**, **experiments 077–085
only**, and uses **only** the `{"window","at_boundary"}`-key structural
detector — the proxy-numeric-field fallback described in the frozen
proposal was never implemented. THERMODYNAMICS' Phase-2 grep
(`free_period_with_widening` absent from `069-076/`) gives real cover for
dropping 069–076 specifically, but nothing in the record states the method
itself was narrowed (proxy-matching dropped) or reconciles "21 files" vs.
"18 files scanned" anywhere I can find in `phase2_redteam_audit.md`,
`phase3_synthesis.md`, or `NOTES.md`. Separately: the detector's own
`STAGE_KEYS={"window","at_boundary"}` requirement structurally cannot
match `free_period_with_widening_quiet`'s own per-stage `rec` shape (which
carries `at_boundary` but never a `"window"` key) — so the script's own
docstring claim to cover "the 2-stage quiet order" is not actually true of
its implementation. Very likely inert in practice (quiet-variant
trial-level stage records are not persisted anywhere in the 18 scanned
files — Monte Carlo loops of this size don't get archived per-trial), but
it is a real precision gap between what was promised and what shipped,
in the spirit of this program's own R4 discipline, and should be logged
rather than left silent.

## 6. Everything else — independently spot-checked, no new defect

- MATERIALS'/Red Team's quiet-variant call-count correction (60,001, not
  40,000) and the 6.70%-firing-rate finding: independently re-derived by
  re-running `phase4_null_calibration_controlled_comparison.py` myself,
  confirmed bit-exact.
- QUANTUM's stride-phase researcher-degree-of-freedom finding: the fix
  (report all three phases, headline "phase-dependent") is correctly
  implemented and reproduces exactly; I agree with Red Team's ruling this
  was the correct discipline rather than reporting one arbitrary phase.
- VISION's instrument-reliability-caveat-carry-forward fix: present
  verbatim in NOTES.md's Result section next to the `classification_a`
  citation, correctly worded.
- THERMODYNAMICS' energy-interception exemption sentence: present in
  NOTES.md's Idealizations, correctly worded, matching exp-084/085's own
  established language — no Checkpoint-4-adjacent gap this cycle.
- Title correction (Red Team's own finding): NOTES.md's own header now
  reads "items 1–3 of its flat, un-Tiered six-item list, folded with two
  cosmetic fixes" — corrected, matches the actual scope.

I found no defect among these six that changes any classification or
requires further correction.

## Ranked next steps for the T28 sub-thread

*(None of the below re-proposes anything in LOGBOOK's RULED OUT registry,
R1–R11 — items 1–2 build forward on R11's newly-established rule rather
than reopening it.)*

1. **A dedicated, cheap, zero-FDTD validity check of
   `edge_diffraction_c_empty_corrected` at grazing incidence
   (θc≳45°)** — e.g. compare the bare Kirchhoff sum against a
   Fresnel-transition/UTD-corrected version at 2–3 spot angles, or check
   whether the derived `Sx`/Weber-contrast quantity stays passive there.
   This is the single most consequential open item this cycle's own data
   surfaces: 6/37 windows are confirmed boundary-pinned and 15/37 in the
   broader unresolvable category, concentrated exactly where this
   scalar-diffraction approximation is expected on first-principles
   grounds to be least trustworthy — before any future cycle treats a
   nominally "converged" fit in that region (θc=57°, 65°, 67°, 69°, 75°,
   77° all show `converged=True`) as physically meaningful rather than an
   artifact of a formula outside its own valid regime.

2. **Make amplitude-scale homogeneity a standard check on any future
   "recovered" set**, not just a per-window disclosure. This cycle's own
   persisted `ptp`/`ss_tot_full` data (delivered by my own Phase-2 fix)
   shows a 492× spread even among windows that all pass the SAME
   `r2_local≥0.30` bar — a natural, cheap, zero-new-computation extension
   of the fix already shipped, worth adopting as house discipline for any
   sub-window-style aggregate statistic on this instrument going forward.

3. **Complete the still-queued full-scale (60,001-call)
   `null_calibration_appendix` re-run** on the corrected quiet variant.
   The N=3000 controlled comparison substantially de-risks this (bug and
   fix bit-identical at matched N) but does not replace it — already named
   in NOTES.md's own Next section; restated here as the most concrete
   unfinished item with a known, bounded cost.

4. **(Low priority, cheap)** Close the prior-citation audit's own coverage
   gap for the quiet-variant's stage shape (§5, above) — drop the
   `"window"`-key requirement or add a dedicated quiet-variant detector —
   and reconcile the "21 files, 069–085" vs. "18 files, 077–085" scope
   discrepancy in the record. Likely inert given no quiet-variant
   trial-level record is currently persisted anywhere, but cheap to close
   and in the spirit of this program's own R4 self-citation discipline.
