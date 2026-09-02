# Phase 5 — Review (PHOTONICS, blind), Panel Iteration 79 (exp-102)

Fresh sub-agent. Read: PANEL.md, LOGBOOK.md in full (RULED OUT R1–R21,
ESTABLISHED, LIVE THREADS T1/T8/T9/T28, the Iteration 76–78 R20-firing
narrative), `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md` (Hypothesis→Next), `run.py`,
`run_output.txt`, `results.json`. No other seat's Phase-5 output this
cycle. All numbers below are recomputed from `results.json`/
`run_output.txt` directly, not restated from NOTES.md prose.

## 1. Is κ(θ)'s optical-response reading coherent with expected
## angular/wavelength behavior for this absorber?

**Yes, in magnitude and mechanism, with one open cross-check and one
angular-pattern observation worth naming.**

- **Magnitude.** κ_region ranges from 3.48×10⁻³ to 7.29×10⁻³ (corrected
  range — see §3 below) at a near-field standoff (D_STANDOFF/R4_R_OUT =
  1.28×). Given this exact article's own already-established Q_ext≈
  1.54–1.56 (exp-101, corrected reading) and T9's σ_abs/σ_ext≈0.51
  Babinet-adjacent extinction-paradox finding, a near-total on-axis
  shadow at this close standoff (κ ≪ 1%) is exactly the expected regime
  — this is a large-extinction-cross-section absorber, not a weak
  scatterer, and Fresnel diffraction has not yet had the propagation
  distance to fill the shadow back in (Learned item 2's own diagnosis,
  which I independently endorse: a point sample close to the object
  reads darker than a farther window average of the same shadow — this
  is ordinary near-field diffraction, not an artifact).
- **One thing worth more scrutiny than NOTES.md gives it**: at the
  *identical* standoff/r_out ratio (1.28×), the R4 family (oblique,
  37–43°, `edge=80` tapered aperture, σ_max=0.25, cpl=40) reads κ≈0.35–
  0.73%, while Gate B's native-scale flagship (normal incidence, no
  `edge=` taper specified — a materially different source aperture, not
  merely a different angle — σ_max=0.5, cpl=20) reads κ=0.163%, roughly
  2–4.5× darker. `graded_black_shell`+`pec_disk` is rotationally
  symmetric, so incidence angle alone should not move the on-axis shadow
  depth by this much at a matched standoff/r_out ratio — the aperture-
  taper difference (an explicit `edge=80` plane-wave taper vs. Gate B's
  unspecified default profile) is the more likely driver, not a hidden
  angle-dependence in the absorber's own optical response. NOTES.md's
  Learned item 2 correctly diagnoses *why* Gate B fails the old-figure
  reproduction (footprint mismatch) but does not flag that Gate B and
  the R4 family are also not a matched-aperture comparison — worth
  controlling explicitly before Gate B's own footprint fix (Next item 1)
  is trusted as isolating standoff alone.
- **κ_off(θ) > 1 (mildly brighter than empty, 1.041–1.077 — confirmed,
  §3): physically expected, not an anomaly.** A pure beam-perpendicular
  offset just outside a hard shadow boundary is exactly where Fresnel/
  edge-diffraction theory predicts a bright overshoot — energy
  redistributed out of the shadow by diffraction at the absorber's edge
  constructively adds just outside it (the same physics as the bright
  fringe flanking a knife-edge shadow), before settling back to unity
  farther out. A 4–8% overshoot at Δ_lat=450 cells (≈2.9×r_out) is a
  modest, physically sane fringe amplitude at this standoff, not a
  red flag — it confirms Prediction 3's own stated purpose (localized
  darkening) more informatively than "diffracted away" alone conveys.
- **A genuine angular-dependence observation, disclosed cautiously
  because of R5/R10's own look-elsewhere discipline.** κ_off(θ) is
  *not* monotonic across the 6 angles — both configs show the same
  qualitative up-down-up-down-up pattern (peaks near 38.59°/42.96°,
  dips near 39.2°/41.46°, C40_R4 and G40_R4 tracking each other closely
  at every angle). Six non-uniformly-spaced points cannot support a
  period fit (that is precisely the R5/R17 hazard this program has
  already paid for twice), so I am **not** claiming a periodicity here —
  but the qualitative shape recurring identically across both congruent
  configs is more consistent with a real, shared diffractive structure
  than with independent per-cell noise, and it sits in the same 5.8°
  angular window T28's ~2.84° oscillation and T21's ~1.96°–2.53° fringe
  periods already occupy. Flagged as a candidate direction (§6), not a
  finding.

## 2. Gate C sign-correction — independent re-derivation from my own
## discipline (surface/propagation bookkeeping)

**Confirmed correct, and confirmed to be a genuine independent
re-derivation, not a fit-to-agree — checked against R4's own standing
rule (LOGBOOK: "a sign correction... must itself be independently
re-derived... never adopted merely because it makes two numbers
agree").**

The chain of reasoning is sound from a propagation/surface-bookkeeping
standpoint: `u(θ)=(-cosθ, sinθ)` is `add_line_source`'s own documented
launch convention — established for an *unrelated* purpose (`P(θ)`'s
construction), independently verified against source by EM's Phase-2
critique before Gate C ever used it. For a locally plane wave, the
time-averaged Poynting vector is parallel to the propagation direction:
**S ≈ I0·u(θ)**, so `Sx ≈ I0_corrected·u_x(θ)` with `u_x(θ)=-cosθ` for
this family's own geometry (src_x > obj_x, confirmed by `downstream_
sign()`'s runtime assertion). That is a structurally different
derivation path than "flip the sign until Gate C passes" — it reuses an
already-independently-verified vector convention from a different part
of the same instrument, exactly the standard R4's addendum requires.

**I independently re-derived the algebraic size of the original error
as a check on the diagnosis, not just trusted the disclosure**: if
`i_inc ≈ -I0_corrected·cosθ` (a pure sign flip against the erroneous
`I0_corrected·cosθ` comparator), the original deviation should be
`|I0·cosθ-(-I0·cosθ)|/I0 = 2·cosθ`. At θ=37.127246°, cosθ≈0.7973 ⇒
2cosθ≈159.5%; at θ=42.960901°, cosθ≈0.7318 ⇒ 2cosθ≈146.4%. This matches
the reported original-erroneous deviations almost exactly (`results.
json`: 159.78%/159.28% at 37.13°, 145.44%/145.84% at 42.96° — see §3) —
independent confirmation, by a route neither NOTES.md nor `run.py`'s own
disclosure computes explicitly, that the observed ~145–160% figure is
*exactly* the signature of a pure sign error scaled by `cosθ`, not a
coincidentally-similar magnitude bug. This is the strongest form of
verification available for a sign correction: the diagnostic's own
predicted shape (`2cosθ`, angle-dependent) matches the measured shape
across all 6 angles, not merely the average size.

The R4-lineage physical reasoning also holds for a second, independent
reason worth naming from my own charter: `i_inc` (a raw signed Poynting
x-component) coming out **negative** for a wave whose propagation has a
genuine −x component is not a bug to be "corrected" — it is what a
correctly-oriented incident wave *should* produce, and Gate C's role is
checking a convention (does the assumed local-plane-wave direction match
the raw measured flux?), not asserting a physical law that could fail.
Learned item 4's own self-critique (three independent Phase-2 checks
verified magnitude/averaging-order but none re-derived the sign) is an
honest and correctly-scoped finding — I confirm it stands.

## 3. Independent numeric verification (recomputed from `results.json`/
## `run_output.txt`, not restated)

1. **κ_region(θ) range — DEFECT FOUND.** NOTES.md's Result states
   "κ(θ) (region-averaged) ranges 3.68×10⁻³–7.29×10⁻³ across all 12
   (angle,config) cells." I recomputed min/max over all 12
   `primary_rows[*].kappa_region` values directly: sorted, the true
   minimum is **3.479968×10⁻³** (`C40_R4@41.460901`), not 3.68×10⁻³.
   3.68×10⁻³ (`0.003681515158129401`, `C40_R4@38.59023`) is real but is
   the **third**-smallest of the 12 values, not the smallest. The
   maximum, 7.289772×10⁻³ (`C40_R4@42.960901`), is correctly cited. This
   is a genuine, single-instance, checkable R4-class citation defect in
   the Result section — non-load-bearing (both 3.48×10⁻³ and 3.68×10⁻³
   sit well inside Prediction 1's `[0,0.10]` band, so the verdict does
   not move), but it is exactly the shape R20 tracks (a headline range
   in Result, caught only at Phase 5, not earlier — no Phase-2 critique
   or the Red Team Phase-2 audit had reason to check it, since Predictions
   were only scored at Phase 4). Flagged for the Director's cross-seat
   tally, not adjudicated here — see §5.
2. **κ_off_region(θ) range — confirmed correct.** Recomputed min/max
   over all 12 `kappa_off_region` values: min 1.0405807 (`C40_R4@39.2`,
   rounds to 1.041), max 1.0766458 (`C40_R4@38.59023`, rounds to 1.077).
   Matches NOTES.md's stated "1.041–1.077" exactly.
3. **Gate C corrected/original-erroneous max deviations — confirmed
   correct.** `gate_c_max_dev`=0.009197942611745866 (0.92%, matches "max
   deviation 0.92%"); `max_dev_original_erroneous`=1.597792277617666
   (159.78%, matches the cited figure exactly, at `G40_R4@37.127246`).
   Range of the corrected `dev` column recomputed directly: min
   0.0004355 (0.04%, `G40_R4@40.26542`), max 0.0091979 (0.92%,
   `G40_R4@42.960901`) — matches "0.04%–0.92%" exactly.
4. **Gate D perturbation deviations — confirmed correct.**
   `rel_dev_region`=0.489510797213029 (C40_R4, matches "48.95%") and
   0.08241717646410686 (G40_R4, matches "8.24%"), both recomputed
   directly from `results.json`'s `gates.D.report`.
5. **Gate B kappa_region and geometry — confirmed correct.**
   `kappa_region`=0.0016268958479245203 (matches "1.627×10⁻³"), `P`=
   [352,280], established window x∈[357,457) ⇒ P.x=352 sits *before*
   the window (357>352), matching "BEFORE that established window."
6. **Point-vs-region ratio range — confirmed correct.** Recomputed
   min/max over `p4_point_vs_region` ratios: min 1.230098
   (`G40_R4@42.960901`), max 1.559110 (`G40_R4@39.2`) — matches "1.23–
   1.56×" exactly.
7. **Shell-thickness/outer-radius physical-unit identity (MATERIALS'
   steel-man, restated by Red Team) — independently recomputed and
   confirmed:** `(156-60)·15nm=1440nm`, `(78-30)·30nm=1440nm`;
   `156·15nm=2340nm`, `78·30nm=2340nm`. Both identities hold exactly.

Seven independent recomputations, one genuine defect found (item 1).

## 4. Citation/restatement defect flag (R4/R20 lineage)

**One instance found, this seat, this cycle**: the κ_region(θ) Result
range (§3 item 1). It is a single, isolated instance from my own
domain's check — I found no second or third instance in Result/Learned
from my own re-reading (Gate C's own disclosed original-vs-corrected
figures, Gate D's percentages, and the point-vs-region ratios all
reproduce exactly, per §3). Per LOGBOOK's own R20 text and its own
precedent (exp-101's own "T3" single-instance ruling one cycle ago), one
isolated, non-load-bearing Result-section citation defect, caught blind
at Phase 5, does **not** by itself approach R20's "three or more" bar —
but it is a real instance for the Director's own cross-seat tally
against whatever the other five blind Phase-5 seats find this cycle,
since R20 counts across the *whole* document, not per-reviewer.

## 5. Verdict on the cycle's Combined Verdict candidate

**CONFIRM-WITH-GAPS** (my seat's read; the Director's call governs).

The instrument itself is sound: κ(θ) is the physically correct
successor to `sigma_scat_downstream` (a same-point coherent-phasor ratio
is exactly what constraint 1's physical-transmission question needs),
the Gate C sign fix is independently well-grounded (§2), Gate D
genuinely exercises the one class of bug Gates A/B cannot see, and the
on-axis darkening / off-axis brightening are both coherent with
established anchors and ordinary diffraction physics (§1). The R4
sign-correction and R21 thermal-sidecar disciplines were both honored
correctly, and Gate B's honest, disclosed FAILURE (not forced to pass)
is good practice, not a defect.

The gaps are real, not cosmetic: (a) Gate B's failure means the
instrument's *absolute* κ magnitude has no independent cross-validation
against this bench's own pre-existing trusted `beam_behind` figure this
cycle — only the self-consistency gates (A, D) support trust, which
validate construction correctness, not absolute-magnitude sanity
against prior data; (b) the aperture/profile mismatch between the R4
family and Gate B's flagship (§1) means Learned item 2's "near-field
fills back in" explanation, while directionally correct, is not yet
cleanly isolated from a confounding taper difference; (c) this review's
own §3 item 1 finding is a genuine, if non-load-bearing, citation defect
surviving Phase 3 into Result. None of these move any of the five scored
Predictions off CONFIRMED — the underlying numbers are sound — but they
are open items a future citation of κ(θ)'s absolute value should carry
forward, not treat as fully closed.

## 6. Top-3 candidate directions for Iteration 80 (PHOTONICS' lens)

1. **A matched-aperture, matched-footprint Gate B re-run** (combining
   NOTES.md's own Next item 1 — replace the point/region sample with
   the literal `BEHIND`-window footprint — with the aperture-taper
   control this review adds in §1: apply the *same* `profile="plane",
   edge=80` source construction to the Gate B flagship, not its own
   unspecified default profile, so a Gate B PASS/FAIL genuinely isolates
   standoff/footprint from aperture-shape). This is the single item that
   would let a future cycle trust κ(θ)'s *absolute* magnitude, not only
   its qualitative darkness, against this bench's own most-established
   figure.
2. **A dense, uniform-step angular resweep of κ_off(θ) (zero new
   mechanism, reuses the already-gated readout code, cheap relative to
   the 24-call R4 sweep since only the empty/article phasors at new
   angles are needed) to test the non-monotonic angular pattern named
   in §1** — with a pre-registered null-permutation or circular-shift
   control (R5/R10 discipline, mandatory given this program's own two
   prior "small-sample apparent periodicity" false-positive precedents)
   before any period is fit. This is squarely my own charter (angular
   dependence of a coherent optical measurement) and uses a genuinely
   different, cleaner instrument (a point phasor ratio, not a box-flux
   integral) than every prior T21/T28 periodicity measurement on this
   bench — a real chance to either corroborate or rule out that
   periodicity's existence from an independent measurement class.
3. **Tier 1's own R3-vs-R4 `delta_scene`-realizability split
   (PHOTONICS' zero-FDTD physical-hypothesis check, already commissioned
   to this seat by exp-100/101's own Reconciled queue and deferred
   through this cycle by design)** — the single most-overdue item
   specifically assigned to this discipline; ranked third here only
   because it is unrelated to this cycle's own instrument and I have
   nothing new to add to its scoping beyond confirming (per NOTES.md's
   own accounting) that exp-102 correctly left it untouched.
