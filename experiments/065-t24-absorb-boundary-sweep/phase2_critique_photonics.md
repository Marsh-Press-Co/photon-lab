# PHASE 2 — CRITIQUE · Panel Iteration 42 · Seat: PHOTONICS

*Critiquing `experiments/065-t24-absorb-boundary-sweep/phase1_proposal.md`.
`design_geometry.py` re-run this shift and diff'd byte-for-byte against the
committed `design_geometry_output.txt`: **identical, zero diff.** No R4/R5
discrepancy found.*

## Steel-man (≤150 words)

The core diagnostic design is optically rigorous. Padding the domain by
ABSORB−40 on every side holds A=752, lever=93, D_SP=223, aperture=1504, and
both clearances bit-identically across ABSORB in {40,60,80} — verified
directly: `design_geometry.py` reproduces the committed
`design_geometry_output.txt` byte for byte on this run. This neutralizes
T24's own confound cleanly: N60, the naive same-domain bump, shrinks A by
2.66%, and the desk propagator predicts that alone rephases the established
fringe (P(θ)=λ/(A·cosθ), correctly reused from exp-042/T21 and verified
against the script's own printed digits) by 0.51–0.86 cycles — comparable to
or larger than T24's entire claimed 0.002–0.007 systematic. Using the
boundary-free desk propagator's exact zero-difference degeneracy as a
control is sound logic: since it has zero representation of the absorbing
region, any nonzero FDTD delta at congruent geometry is attributable to real
boundary optics, not aperture artifact. σ_e is correctly derived from this
lab's own τ_center = 2σr_out convention.

## Sharpest attack (≤150 words)

The headline instrument (P-VIS42-2, the boundary-systematic
characterization) samples ABSORB at only three points — 40, 60, 80 — with
no periodicity model for how boundary reflectivity varies with layer
thickness, unlike θ, which has the established closed form P(θ). This is
exactly the failure mode T16/T21/R5 already taught this program to
distrust: an unmodeled-periodicity systematic under-sampled by a coarse
grid can alias badly. Concretely, at 600nm (cpl=20) all three ABSORB values
are exact integer multiples of λ (2/3/4λ); at 450nm (cpl=15) ABSORB=60 is
also exactly 4λ. Nothing here — no periodicity law, no fourth point, no
ABSORB-density check — rules out that the three sampled points sit at
unrepresentative phases of a non-monotonic dependence. This compounds
badly: 600nm, the one wavelength guaranteed to hit exact-λ ABSORB steps, is
also the ONLY wavelength Block ARTICLE scores (P-VIS42-6/7), the row meant
to bound real constraint-3 verdicts.

## Supporting detail (not counted against the ≤150-word limits above)

**On the specific charter questions:**

- **Wavelength consistency, padded vs. unpadded:** Block SWEEP (the
  diagnostic boundary-systematic channel, P-VIS42-2/3/4/5) is genuinely 3-λ
  across C40/C60/C80/G40/N60 — consistent. Block ARTICLE (the one block
  that actually scores against a perceptual bar, P-VIS42-6/7) is 600nm
  only. §0's framing ("no future constraint-3 run's margin... can be
  believed... until [this systematic] is measured") is stated broadly
  enough to read as resolving the debt across the program's constraint-3
  history — but that history includes 450nm and 750nm citations (T7's own
  established ~1.5–1.9% red-growth chromatic finding lives on this exact
  channel), and this cycle's only loaded-article measurement never touches
  either. Idealization 8 discloses the geometry gap honestly but not this
  specific wavelength-coverage asymmetry between the diagnostic and scored
  blocks.
- **T21 fringe/period law:** verified independently by hand and against
  `ripple_period_deg`'s own docstring (exp-048, citing "EM's own
  Iteration-18/19-established fringe period") — P(θ)=λ/(A·cosθ) is the
  correct, previously Red-Team-vetted law, and it is applied correctly here
  (θ-derivative of the same two-edge phase model). The 0.51–0.86-cycle
  "fringe phase shift at θ=40° from A: 752→732" is a *different* partial
  derivative of the same phase function (Δφ = ΔA·sinθ/λ, confirmed by
  reading `design_geometry.py:319-323` directly — it does not literally
  divide ΔA by P(θ), which would be a unit-mismatched, meaningless
  operation), independently verified by hand to reproduce 0.857/0.643/0.514
  cycles at 450/600/750nm to 3 decimal places. Physically legitimate: same
  two-taper-edge Huygens source, two different control axes (θ vs. A).
  **Not an error** — but the document never states these are two distinct
  formulas sharing one phase model rather than one formula applied twice;
  a reader could easily (wrongly) infer the shift number "follows from" the
  period row directly above it, since no derivation is shown for the shift
  row in the proposal text itself (only in the script).
- **Uniform-σ disk convention:** σ_e = τ_center/(2·r_out) =
  0.0065/156 = 4.1666…e-05, matching the printed value exactly and this
  lab's own established τ_center = 2σr_out convention (LOGBOOK Iteration 5
  erratum). ε_r≡1 (no scattering) is the right idealization for isolating
  extinction≈absorption, consistent with T9/ESTABLISHED. No R1–R5 or
  ESTABLISHED-result violation found anywhere in this proposal.
- **§8.2's "no new machinery" argument:** procedurally defensible (it
  discloses the counter-argument and a concrete Phase-3 fallback), but
  optically it proves less than it's used for. The desk propagator's exact
  zero-degeneracy is a *geometric-congruence* control — it shows any
  FDTD-measured ΔC is not an aperture-diffraction artifact. It says
  **nothing** about whether the graded-loss band's own reflectivity is a
  smooth, monotonic function of ABSORB (the load-bearing assumption behind
  treating a 3-point sweep as adequate) — that question is exactly outside
  what a boundary-free model can address, by the proposal's own
  description of it ("zero free parameters," i.e., zero representation of
  the absorbing region). The mechanism narrative and §8.2 are in mild
  tension: the experiment exists because the boundary optically matters:
  it should not simultaneously be argued that varying it introduces no new
  optical configuration worth a density check.

## Verdict

**support-with-changes.**

## Parameter change that would flip to unqualified support

Add a fourth ABSORB point at a value that is NOT an integer multiple of λ
at any of the three wavelengths (e.g., ABSORB=50 or 70 — check against
cpl∈{15,20,25} first) to Block SWEEP, scored under the same P-VIS42-2/3
bands. Cheap (≈18 more calls, well inside the pre-registered 90-minute
stop) and it directly tests whether the 40/60/80 ladder's own integer-λ
coincidence at 600/450nm is aliasing a non-monotonic boundary-reflectivity
term — the one risk this cycle's own gates (G-1, G-2, both vacuum/causal
identities) do not and cannot cover.
