# exp-054 Phase 5 Review — PHOTONICS (blind, independent, fresh context)

Panel Iteration 31. Reviewing `phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`run.py`, `results.json`, `lab/thermo_sidecar.py`, and
`lab/validation/run_all.py::stage18_length_scale_chain`, from the
PHOTONICS charter only: is the proposal's optical response coherent as
stated, across wavelength and angle?

## What this cycle establishes, from this discipline's lens

This is a thermal-chain bookkeeping fix, not an optical-response change,
and it correctly stays that way. No σ_abs/σ_ext ratio, no σ_ext value, no
irradiance, and no angular quantity is touched or re-derived here —
`absorbed_power_established_ratio` (the one function that owns anything
optical in `lab/thermo_sidecar.py`) is verified unchanged (`run.py`
imports `P_ABS_W_ON_CENTRAL = 2.0044347652689456e-12` verbatim from
exp-043, `run.py:81`; `RATIOS`/`K_R_D` verbatim from exp-045, `run.py:86-88`).
That is the correct scope boundary for a sidecar cycle, and it is stated
plainly (T1 escape route "NONE"; "P_abs itself is measurement-locked, not
re-derived," `NOTES.md:156-158`).

**Arithmetic verification (independently re-run, not trusted from prose):**
- **P-054-1**: ran `lab/thermo_sidecar.py::mixed_length_scale_regime` myself
  with the committed inputs (`p_abs_w=2.0044347652689456e-12`,
  `l_geometric_m=2.34e-6`, `k_air=0.026`, `density=2330`, `c_p=700`,
  `emissivity=0.9`). Output `dt_ss_full_K = 3.293076054169135e-05` —
  matches the claimed `3.293076e-5 K` LOGBOOK-Iteration-23 reproduction to
  the disclosed precision, inside band `[2.8e-5, 3.6e-5]`. **CONFIRMED.**
  `results.json::part_a_on_endpoint_mixed_regime.regime` carries the
  identical value; `p_054_1_pass=True` is not a mislabeled fail.
- **P-054-3a**: `results.json::part_b_block_c_rerun.worst_exact_vs_decoupled_ratio
  = 0.9987161823580124`, inside the committed band `[0.98, 1.000]`, and
  `all_decoupled_conservative=True`. **CONFIRMED** — `exact ≤ decoupled`
  really does hold at all 8 re-run points at the shorter, mixed-chain
  `τ_thermal` (3.433×10⁻⁴s), the specific untested corner EM's Phase-2
  attack named.
- `stage18_length_scale_chain` (`lab/validation/run_all.py:1563-1611`) does
  what Red Team's audit demanded of it: gates 1–2 are tautological formula
  self-checks (any `L` passes), gate 3 is the one genuinely discriminating
  check — it pins the literal `R_OUT_M = 78 × 30nm` product and requires
  `mixed_length_scale_regime`'s output to reproduce `3.293076e-5 K` to
  `1e-9` absolute tolerance. This matches Red Team attack 4's own
  characterization exactly; nothing oversold here.

So the two numbers this cycle is proudest of are real, and the module
promotion is real code, not a hand-typed side-computation. That much is
solid.

## Load-bearing defects found (photonics lens specifically)

**1. NOTES.md's own frozen hypothesis restates the contested "diffraction-
inflated" framing with no caveat, even though this discipline's own
Phase-2 attack, and Red Team's independent re-verification of it, found
that framing asserted-not-established and left it downgraded but
undisclosed at the point that matters.**

`NOTES.md:18` (the pre-registered, git-committed hypothesis — the document
Marsh's own house discipline requires predictions be committed *from*):

> "w_on (the ON-endpoint's measured, **diffraction-inflated** extinction-
> cross-section width)"

This is verbatim the same unqualified phrase from `phase1_proposal.md:23`.
My own Phase-2 critique (`phase2_critique_photonics.md`) attacked exactly
this: `w_on` is `sigma_ext_cells` run through the `iso_xsec_sq` convention,
which "already encodes an arbitrary shape choice... adopted to fix an AREA
for a watts computation, not to characterize a diffraction-broadened linear
extent," and no bound separates genuine extinction-paradox diffraction
(`Q_ext = w_on/(2·r_out) ≈ 1.51`, plausible but never checked against a
closed form) from a convention artifact. Red Team's audit (attack 6)
independently re-derived the same `Q_ext≈1.51` number, confirmed the
critique accurate, and explicitly ruled: "does **not** change the
mixed-chain's conclusion... it holds whether the excess is 100% diffraction
or partly a convention artifact" — correctly downgrading the underlying
*argument's* dependence on the word. But the *word itself* survived into
the frozen NOTES.md unqualified. `phase3_synthesis.md:64-66` disposes of
this by deferring the actual check ("Q_ext(x) closed-form check — **NOT**
attempted this cycle... queued for Iteration 32+'s ranked list instead,
**stated in the LOGBOOK close-out**") — but as of this review no Iteration
31 LOGBOOK entry exists yet (`grep "^## Iteration 31" LOGBOOK.md` returns
nothing; Phase 5 writes that entry). Checked directly: neither `NOTES.md`'s
idealizations list nor any `results.json` key anywhere flags "diffraction-
inflated" as an assumption rather than a measurement. A reader who cites
`NOTES.md` alone (the document this program's own house discipline treats
as the authoritative frozen record) inherits the unqualified claim with no
caveat trail unless they separately dig up `phase2_critique_photonics.md`
and `phase2_redteam_audit.md`. This is a real gap between "downgraded to
non-mandatory" (fine, Red Team's call to make) and "disclosed" (not done
at the locus that will actually get cited going forward).

**2. The achromatic (600nm-only) scope-limit disclosure cites the wrong
prior precedent and skips a check that was already cheap and sitting in
the record — I did it myself and it is reassuring, but the cycle didn't do
it, so nobody reading `NOTES.md` can tell.**

`NOTES.md:64` idealization bullet: "no per-λ dependence re-examined this
cycle; exp-045's own Phase-5 finding that `dwell/τ_thermal` stays in-band
across all 3 swept wavelengths for the `w_on`-consistent regime is not
re-verified for the mixed regime here." That cited precedent is a
**kinetics-timescale-ratio** flatness finding, not a **thermal-magnitude**
one — the wrong analog for whether `dt_ss_full`/the 607×/~8,954× margins
would hold at 450/750nm. The directly relevant data was already committed
one cycle earlier, at Iteration 21 (exp-044's own PHOTONICS-mandated Block
C, `experiments/044-.../results.json::block_c_3lambda_achromatic_check`):
`sigma_abs/sigma_ext` flat to 0.45% relative across 450/600/750nm, **and**
(checked directly against `experiments/026-.../results.json::beam_scene`,
which exp-044 itself reads from) `sigma_ext_cells` itself is flat to ~1%
relative — `238.22 / 235.97 / 241.13` cells at 450/600/750nm respectively.
Since the mixed chain's `h_eff`/mass/area are purely geometric
(`r_out`-only, λ-independent by construction) and `P_abs_w ∝
sigma_ext_cells² · ratio_abs_ext`, propagating that ~1%/0.45% flatness
through the mixed chain gives at most a **~4% shift** in `dt_ss_full` at
750nm relative to 600nm — comfortably inside P-054-1's own stated
discrepancy tolerance and negligible against the 500×–750× margin band's
width. The substance is very likely fine. But this is a ~3-line
computation using two already-committed, zero-cost datasets (matching this
program's own "zero-cost, already-committed data" precedent — the exact
move exp-044's Block C itself made one cycle earlier), and exp-054 neither
performs it nor cites the data that would let a reader perform it. The
disclosure that exists is honest about *scope* but not informative about
*risk* — it doesn't tell a reader whether skipping the 3λ sweep this time
is a real gap or a formality, when the record already contained the
answer.

**3. (Minor, correctly scoped-out, worth restating explicitly) — all of
this cycle's absolute margins still ride on `P_abs_w`'s own unaudited area
convention.** `absorbed_power_established_ratio`'s own docstring
(`lab/thermo_sidecar.py:112-118`) states `iso_xsec_sq` treats the object as
"compact... a finite-rod-length convention would scale `P_abs` linearly
instead" — a comparably strong idealization to the one exp-054 goes to
considerable trouble to correct on the `r_out` side (idealization bullet
2, cube-vs-disk). exp-054 correctly declines to re-open this ("`P_abs`
itself is measurement-locked, not re-derived") and that's the right call
for this cycle's scope — but the NOTES.md idealizations list never
restates that the headline margins inherit this un-re-examined convention
on the *other* half of the chain, even while devoting real attention to
the analogous idealization on the `r_out` half. Not a defect in what was
computed; a completeness gap in the "what this cycle does and doesn't
settle" accounting.

## What I did NOT find

- No arithmetic or sign error in the two figures I independently
  reproduced.
- No wavelength- or angle-dependence claim is smuggled in anywhere — the
  cycle correctly makes zero optical claims of its own.
- `ratio_abs_ext=0.6075` and the derived `Q_ext≈1.51` remain physically
  unremarkable for a near-resonant absorbing/scattering body at size
  parameter `x≈19.6–32.7` (between the geometric-shadow ceiling Q_ext→1 and
  the diffraction-paradox ceiling Q_ext→2) — consistent with, not
  contradicted by, anything this cycle touches.
- Red Team's own audit (attack 6) already correctly downgraded my Phase-2
  attack to non-load-bearing for *this cycle's numbers specifically*; I
  have no new arithmetic disagreement with that call. My finding here is
  about where that downgrade's caveat trail terminates, not about
  re-litigating the downgrade itself.

## Ranked candidate directions for Iteration 32+ (this seat's priorities)

1. **The desk closed-form Q_ext(x) cylinder/disk check** (already queued,
   non-mandatory this cycle, Phase-2/Red-Team attack 6) — bound how much
   of `w_on`'s ~3.0× excess over `r_out` is genuine diffraction vs. the
   `iso_xsec_sq` convention artifact. Zero new FDTD, closed-form only. This
   is the one open item that would convert "asserted, not established"
   into a bounded number for the load-bearing premise the whole
   `r_out`-vs-`w_on` split rests on.
2. **Run the mixed-chain ON-endpoint and Block C dose-accumulation grid
   across the program's standard 450/600/750nm sweep**, reusing exp-026's
   already-committed `sigma_ext`/`sigma_abs` per-λ values (exactly exp-044
   Block C's own zero-cost move, one cycle earlier). Converts finding #2
   above from a plausibility argument into a real, checked number, and
   closes the disclosure gap at the source rather than leaving it as an
   unqualified idealization bullet.
3. **A closed-form or literature cross-check of `ratio_abs_ext≈0.6075`**
   against a published absorption-efficiency curve for a silicon
   sphere/cylinder near this size parameter — independently bounds whether
   the *absolute* `P_abs_w` this cycle treats as measurement-locked is
   physically reasonable, not merely self-consistent within this
   codebase's own established-ratio convention.
4. **Angular dependence of the length-scale question**, deferred/lower
   priority: no angular-selectivity mechanism is currently active in the
   program's queue, so this is not urgent, but if/when one is proposed,
   whether `r_out` remains the correct conducting-solid length at oblique
   incidence (vs. an angle-dependent effective radiating/absorbing
   footprint) should be re-examined before the mixed chain is reused there.

## Verdict: PARTIAL

The core arithmetic is verified correct, the code promotion is real (not
hand-typed), the trust-suite stage does what it claims to do (one
genuinely discriminating gate, two tautological-but-honestly-labeled
ones), and the cycle's optical scope boundary (touch nothing photonics
owns) is the right call, correctly executed. But from this discipline's
lens the cycle does not close clean: a phrase my own Phase-2 critique
flagged as unestablished ("diffraction-inflated") survives unqualified
into the git-committed, pre-registered `NOTES.md` hypothesis with no
caveat at the point future citations will actually read; and the
achromatic-scope disclosure, while present, cites a less-relevant prior
finding and skips a cheap, already-possible check that would have replaced
an idealization-bullet assertion with a real number — the same category of
"claimed-scoped, not fully delivered" gap this program's own Red Team has
flagged as a recurring pattern in prior sidecar cycles (Iteration 21's
own PARTIAL verdict for a structurally similar reason: robust physics
conclusion, real but non-fatal disclosure/process gaps). Neither finding
here threatens P-054-1 through P-054-8's numeric passes; both are cheap to
close next cycle.
