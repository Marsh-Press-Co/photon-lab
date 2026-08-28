# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 61 · exp-084

## Governance check (git-provenance tripwire, per Iteration 59→60's own forward flag)

**PASS, cleanly.** `git log --oneline` on this directory shows exactly two
commits, in the correct order: `c714ad5` ("PHOTONICS proposal ... pre-registered
before any code exists") touches only `phase1_proposal.md`, 206 insertions;
`git show c714ad5:.../phase1_proposal.md` confirms the file ends at "### 6.
Realizability / cost note" — the "### Phase 1 result (self-scored)" section is
genuinely absent. `4219877` ("PHOTONICS self-scored result") lands 1,097
insertions across `derivation_results.json`, `phase1_derivation.py`,
`phase1_output.txt`, and a +91-line append to `phase1_proposal.md` (the
self-scored section) — strictly after `c714ad5`. `git status`/branch-tracking
confirm both are on `origin/main`, not local-only. This discharges the
two-cycle-old tripwire (exp-081, exp-082) for a **second consecutive cycle**,
matching Iteration 60's own restoration.

## Threshold-pinning duty

**None required, confirmed by direct inspection, not assumed.** T1 route N/A,
no perceptual claim anywhere; `amb.weber()`/`window_means()` are reused only
as the bench's own scoring reduction (matching every prior T28 desk cycle),
never compared to `C_thr` or any adaptation/luminance quantity. No smuggled
threshold language found.

## Independent numeric re-verification (R4)

`rel_dev_a` recomputes exactly from `derivation_results.json` primitives:
`|2.533834586466165 − 2.8421052631578947| / 2.8421052631578947 =
0.10846560846560856` → rounds to the stated `0.1085`. `P_edge_A =
2.8421052631578947` is genuinely present in
`experiments/069-.../results.json` (grep-confirmed), not fabricated.
`rel_dev_b = 0.27551020408163274` also reproduces exactly.

## R9 commensurability

Clean. `rel_dev = |P_model − P_target| / P_target` is applied identically
(same units, degrees; same normalization) to both legs and matches the
sub-thread's own established convention (exp-069/077/083). No
differently-normalized quantities are compared as if commensurable anywhere
in this file.

## Steel-man (147 words)

A genuine methodological advance for T28: nine-plus prior mechanism cycles
(075–081) modeled the `ABSORB` band as a reflector and all were REFUTEd or
foreclosed; this is the first to treat the source's own finite, tapered
aperture as what it actually is — a near-field diffractor — and correctly
diagnoses *why* the far-field grating formula `P_edge_B` missed by 45%: this
aperture sits at 0.197% of its own Fraunhofer distance, a real category
error, independently checkable from the parameter table alone. Governance is
exemplary: the pre-registration commit contains zero of the self-scored
section, restoring house discipline for a second consecutive cycle. R4/R5
are genuinely exercised, not merely invoked: two self-built anchors are run,
one (Anchor 2) FAILS and is honestly withheld rather than smoothed into a
REFUTE, and the R5 specificity control is computed and reported even for the
leg that passes. Zero FDTD, correctly scoped, zero realizability content.

## Sharpest attack (150 words)

Leg (a)'s headline SUPPORT is not fresh evidence. Its free-fit period,
`P_model_a=2.533834586466165°`, is **bit-identical (15 significant figures)**
to a number already on record: `experiments/070-.../results.json`'s real
FDTD-measured `C80(θ)` empty-scene curve's own free-fit period (same value,
same `phase4_results.md` "10.85%" cell). That number was already
adjudicated: Iteration 47's unanimous, Red-Team-confirmed Phase-5 ruling
held this exact gap reflects "a compromise fit between T21's own ~1.96°
fringe and a weaker, imperfectly separated second component" — T21
contamination is on record (`R²_fixed(C80)=0.2645` against T21's own fixed
period) — explicitly **not** a clean independent 2.84° confirmation. This
file's R5 control tests only whether *other target periods* would also
pass; it never tests whether its *own recovered* 2.5338° is this
already-known T21-contaminated artifact rather than the proposed mechanism.
An already-discounted number is re-badged "SUPPORT... with margin" under a
new theoretical framing without reconciling the coincidence.

## Verdict: **support-with-changes**

## Parameter change that would flip to unqualified support

Run the same T21-decorrelation check exp-070 already applied
(`R²_fixed` against `T_SINTHETA_600`, the fixed ~1.96° period) on leg (a)'s
own model curve/residual. If it comes back near-zero (genuinely decorrelated
from T21's fringe), the bit-exact match to exp-070's C80 reading becomes
strong corroborating evidence the desk model IS capturing real, uncontaminated
diffraction physics, and SUPPORT should stand unqualified. If it reproduces
a comparable `R²_fixed`, SUPPORT should downgrade to INCONCLUSIVE, matching
exp-070's own "compromise fit" characterization of this identical number.
