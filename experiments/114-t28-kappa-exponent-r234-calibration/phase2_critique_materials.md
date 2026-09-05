# Phase 2 Critique — MATERIALS & METAMATERIALS (Panel Iteration 91, exp-114)

**Charter**: sub-wavelength structure; what could physically realize the
proposed optical behavior. Owns the realizability bound (published /
plausible / unobtainium-with-parameters). Blind to all other seats'
current-cycle critiques.

**Scope confirmation, independently checked, not taken on faith**: this
is instrument-calibration work (a wall-time cost-scaling exponent,
`KAPPA_COST_EXPONENT`, re-tested at a second `kappa_ratio`), not a
phenomenon-mechanism proposal. T1 route is genuinely N/A: nothing in
`run114.py`/`chunk_runner114.py` expresses σ(I), σ(x,t), angular
selectivity, or sub-threshold operation — the only things that change
are a geometry-scaling function's evaluation point, a checkpoint/resume
driver, and a cost-gate exponent check. Confirmed by reading both files
in full; no material-realizability content is smuggled in under cover of
"calibration" — the proposal is correct to scope σ_max/tau_shell/
realizability entirely out (§3), and my own charter question here really
does reduce to the narrower one the brief poses: is `r=234` proportioned
like a physically sensible member of the already-validated shell family,
not a new mechanism claim.

## Independent verification performed (re-run, not re-read)

- `python3 run114.py --verify-geometry` (re-run fresh this session):
  `{"pass_": true, "mismatches": []}` — `geom_fixedabs_cpl(r, cpl=20)`
  reduces exactly to `R110.geom_fixedabs(r)` at r=156, 234, **and** 312.
  Independently reproduced.
- Queried `geom_fixedabs_cpl` directly at cpl=20 and cpl=25 for all three
  r: **`tau_shell = 24.0` exactly at every r** (156/234/312, both cpl),
  because `ABS_THICKNESS=48` cells is a fixed absolute-cell constant
  (not scaled by `kappa_of(r)`) — R_CORE = R_COAT − 48·(cpl/20) at every
  r, confirmed by direct query (r=234, cpl=25: R_CORE=232, R_COAT=292,
  matching the proposal's own table exactly). This means the shell's
  physical thickness (48 cells × 30 nm at cpl=20 = 1.44 µm = 2.4 design
  wavelengths at 600 nm) is IDENTICAL at r=156/234/312, not merely
  similar — the `graded_black_shell` docstring's own stated design
  requirement ("thickness ≥ ~1.5 design wavelengths keeps entry
  reflection broadband-small") is met with the same margin at all three
  radii, not a weaker one at the new, larger r=234/312. This is exactly
  the "same material law, proportioned consistently" check my charter
  requires, and it holds.
- Independently recomputed the Fix-1 box_a-clearance-in-wavelengths
  figures from raw geometry (not copied): 3.2λ / 4.8λ / 6.4λ at
  r=156/234/312 — bit-exact to the proposal, and 4.8 is exactly the
  linear midpoint, as claimed.
- Independently recomputed the disputed cost-multiplier arithmetic:
  `1.5**3.2053299988... = 3.6680107...`, `2.0**same = 9.2236003...`,
  ratio `= 0.397677 (39.8%)` — matches `run114.py`'s own printed values
  bit-exact, and confirms the proposal's own R4 correction to MATERIALS'
  prior (exp-113) Phase-5 review is right: hand-checking `1.5**3.2`
  myself gives `3.660`, not the `≈2.98` that review stated — the
  original estimate was not just "imprecise," it was arithmetically
  wrong even at the rounded exponent. The correction is real and
  properly sourced (R4 discipline honored, one level deeper than the
  proposal itself claims).
- Independently grepped `experiments/` for `r=234` outside exp-114: found
  exactly the two citations the proposal names and no others —
  `experiments/106-.../phase5_review_photonics.md:269` (a candidate
  fourth point for the UNRELATED `shape_ratio_fixedabs≡2^n` physics fit)
  and `experiments/113-.../phase5_review_materials.md:200-247` (this
  document's own cost-exponent precedent). Read both in context: the
  "genuinely new, not redundant" and "two different quantities" claims
  both hold up against the actual files, not merely the proposal's
  gloss on them.

## Steel-man (≤150 words)

From this seat's lens, this is the correct way to extend a validated
shell-and-coating family: every geometry-derived quantity that matters
to realizability — `tau_shell`, absolute shell thickness in design
wavelengths, `sigma_max`, the PML-taper depth — is held bit-identically
invariant across r=156/234/312 by construction, independently confirmed
here, not merely asserted. `r=234` sits on the same physical
size-scaling ladder (`kappa_of(r)=r/78`) this program already
established a bridging need for (T8), at a genuinely new intermediate
point, not a repeat. The proposal correctly refuses to let a cost-gate
convenience leak into a materials claim — no σ_max, tau_shell, or
fabrication content is varied, scored, or smuggled in — and it even
catches and corrects a real arithmetic error in MATERIALS' own prior
review before repeating it. That is exactly the "physically sensible,
consistently proportioned" extension my charter asks whether this
program can produce.

## Sharpest attack (≤150 words)

Not a numeric defect — everything I re-ran reproduces bit-exact. The
defect is an omission that is squarely this seat's own charter debt.
LOGBOOK's Iteration-89 and Iteration-90 Reconciled queues both carry,
verbatim, "MATERIALS' own fabrication-tolerance quantitative bound" as
an explicitly still-open Tier-2 item — named "fourth consecutive cycle"
at exp-111, "fifth consecutive cycle" at exp-112/113. I grepped
`phase1_proposal.md` and `run114.py` for "fabrication": zero hits. The
proposal's own §3 names four OTHER declined items as "real, named,
undropped debt" — but never mentions the one debt that is actually
MATERIALS' to carry. If exp-114 proceeds to Phase 3/4 without this line
being re-stated somewhere, that is the sixth consecutive cycle this
specific named item silently disappears from the queue rather than
being carried forward — the exact shape R25 exists to prevent for a
code fix, applied here to a named realizability debt instead.

## Verdict: support-with-changes

## Single change that would flip to full support

Add one sentence to §3 (or the Idealizations) explicitly naming
MATERIALS' own fabrication-tolerance quantitative bound as a declined,
not-silently-dropped item carried forward to Iteration 92 — matching the
treatment already given to the other four declined items in that
section. No code or geometry change needed; this is a documentation
completeness fix only.

## Trust-suite check

Re-ran `python3 lab/validation/run_all.py --only 12346789` from the repo
root this session: **41/41 green**, zero failures. (Confirmed — see
final report for the raw tail of output.)
