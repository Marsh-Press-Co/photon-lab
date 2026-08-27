# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 59 · exp-082

Fresh sub-agent, zero memory of any prior session. Read PANEL.md, AGENTS.md,
LOGBOOK.md (RULED OUT R1-R9, ESTABLISHED, LIVE THREADS T28 in full,
Iterations 46-58), PLAN.md's Iteration-59 queue, and the complete exp-082
record (`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/`_results.json`,
`x_wall_output.txt`, `phase_convention_extension.py`/`_results.md`/
`_results.json`, `phase_convention_output.txt`), plus exp-081's own
`photonics_construction.py`/`NOTES.md`. Blind to every other seat's own
Phase-2 critique this cycle. No RULED-OUT item (R1-R9) is re-proposed or
re-litigated.

## 0. Verification: did the Tier-0 hygiene bundle (items 2-3) actually land?

**Yes, all three sub-items, correctly, and independently checked against
the underlying JSON rather than trusted from prose.**

- `item3_energy_budget()`'s docstring in `experiments/081-.../
  photonics_construction.py` now opens with `"""POST-RUN ANALYTIC, ZERO
  FDTD (Iteration-59 hygiene label, PLAN.md Tier-0 item 2, exp-081
  phase5_redteam_audit.md Sec 4 item 4)..."` — the exact label item 2
  specified, correctly attributed to its own trigger.
- The docstring also states `"600nm ONLY -- ... no claim is made or
  implied at 450/750nm"`, and `NOTES.md`'s own Item-3 headline sentence
  carries the matching qualifier: `"(600nm ONLY -- not yet checked at
  450/750nm; see the still-deferred wavelength-generality leg, Tier 1 item
  8.)"` — the third sub-item, done.
- The `ABSORB=40-worst-case-across-all-depths` table (`NOTES.md` lines
  128-137, four rows: `ABSORB∈{40,60,70,80}`, three columns: `θ_beam`
  matched / `θ_local` matched / `θ_local` realizable) reproduces
  `phase1_results.json::item3_energy_budget.theta_local_convention.
  per_absorb` bit-for-bit — I re-extracted the raw JSON myself
  (`absorb_40: 1.288558×10⁻⁸` matched / `2.637482×10⁻⁸` realizable;
  `absorb_60/70/80` each strictly smaller, monotonic) rather than trusting
  the markdown table, and it matches to the printed precision. The claim
  "`ABSORB=40` is the worst case... monotonically decreasing... throughout"
  is true of the actual numbers, not merely asserted.

All three sub-items are real, correctly sourced from committed JSON (never
hand-typed — R4 discipline honored), and correctly cite their own PLAN.md
trigger. No further action needed on this bundle.

## 1. Steel-man (≤150 words)

Idealization 7's scoping is sound. THERMODYNAMICS' sidecar contract binds
*proposals* — mechanism candidates engaging T1 — and this cycle explicitly
disclaims that (`T1: N/A`, no scored contrast used as constraint-3
evidence). More decisively: the confound under test, `PAIR_PAD`, is
independently *proven* lossless (exp-076, re-derived from `lab/fdtd2d.py`
primitives: the damping mask is a pure function of `absorb`, zero
dependence on `pad`) — a coherent propagation-phase effect carrying
provably zero absorbed power. Running an energy-budget calculation on a
mechanism already proven to have none would be pointless arithmetic, not
missing rigor; correctly recognizing that and skipping it is the right
call, not a gap. The test is itself a direct FDTD contrast measurement,
matching the sidecar's own "post-run analytic, not an FDTD output"
distinction — there is no analytic step this test's architecture calls
for.

## 2. Sharpest attack (≤150 words)

Idealization 7's premise is unverified in exactly the way this cycle
matters: `PAIR_PAD` was proven lossless in an **empty** scene. This cycle
is the first to interpose a real, strongly-absorbing article between
source and boundary — the flagship absorber, whose whole published
function is intercepting most of the incident field (beam-behind
1.5-1.8%). SURVIVES is read as "the same lossless phase artifact reaches
the scored channel," but nothing here decomposes whether the measured
`delta_scene(θ)` is still that artifact, or a *new*, article-mediated
interaction — the absorber sitting inside the coherent echo's own
round-trip path, converting part of a formerly pure-phase effect into
something absorption-coupled. That distinction is squarely my charter's
question ("where absorbed energy goes... whether it would be detectable")
and idealization 7 declines to touch it, citing only that this is "an FDTD
measurement, not an analytic estimate" — true but non-responsive to
whether the *mechanism* changed character once real absorption entered the
path.

## 3. A related, lower-stakes note (not part of the attack, offered as disclosure)

Item 3 (exp-081)'s own energy bound used `interception_factor_upper_bound
=1.0` — "ALL of the source's radiated power reaches the wall," explicitly
the loosest possible assumption. This cycle's real article intercepts most
of that power before it ever reaches the boundary, so in the specific
scenes exp-082 measures, the true wall interception is well below 1.0 —
item 3's already-negligible `~1.3×10⁻⁸`–`~2.6×10⁻⁸` bound is, if anything,
an *over*-estimate here, not an under-estimate. This reinforces rather than
threatens item 3's conclusion, but nothing in either document states the
connection; a one-sentence cross-reference would close it cheaply.

## 4. Verdict: **support-with-changes**

The Tier-0 hygiene bundle is verified correct. The primary result (SURVIVES,
`ratio=0.6573`) stands on its own falsifiable, pre-registered bands and its
bit-exact reproduction precondition — I have no attack on the measurement
itself. The gap is interpretive: idealization 7 is defensible as a *gating*
matter (no energy-budget precondition should block this test's own bands)
but leaves the mechanism-identity question — is the article-loaded
confound still the proven-lossless `PAIR_PAD` phase effect, or a
qualitatively different absorption-coupled one — genuinely open, not
merely deferred by design the way idealization 7's prose implies.

**Single parameter change that would flip this to full support:** add one
cheap, zero-new-lab/-machinery control — re-run the `C40`/`G40` pair with
the article's `graded_black_shell` absorption replaced by a lossless
PEC-only disk at the identical location (a pure-scatterer, zero-absorption
stand-in) and show `delta_scene(θ)` stays comparable in scale and shape to
this cycle's real-absorber result. If it does, that is direct evidence the
riding-through signal stays phase-dominated regardless of the article's own
absorption, and idealization 7's scoping is fully vindicated, not merely
plausible.
