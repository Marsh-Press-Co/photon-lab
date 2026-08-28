# PHASE 3 — SYNTHESIS · Panel Iteration 62 · exp-085 · Director

Director resolves Phase 2 into one testable, corrected, runnable spec.
Red Team's Phase-2 audit (`phase2_redteam_audit.md`) ruled
**PROCEED-WITH-MANDATORY-FIXES, 7 items**, `constraint-#N-violation` N/A
throughout (model-internal desk cycle). Every attack and every one of the
five blind critiques' claims was independently re-derived by Red Team from
primitives before ruling — nothing here is taken further on faith; this
synthesis re-checked Red Team's own two headline numeric claims (the
`center_deg` factor arithmetic and the §4(b) MECE counterexamples) against
the cited source files again, independently, and confirms them.

## Accepted / overridden

**All 7 mandatory fixes accepted. Zero overridden.** Red Team's audit is
itself the second independent layer (after five unanimous blind critiques)
converging on the same defects — there is no live disagreement for this
Director to arbitrate. The 3 non-blocking disclosure items are also
accepted (cheap, and this cycle's own house culture treats a disclosed
caveat as strictly better than a silent one). Below, each fix is restated
as the EXACT change made to the committed spec (superseding
`phase1_proposal.md` §4 and the relevant lines of §2 wherever they
conflict; §§1,2,3,5,6 of the original proposal are otherwise unchanged and
still govern).

## Corrected spec (supersedes `phase1_proposal.md` §4)

**Fix 1 + 2 (circular-shift null, extended to Method C).** Strike the
struck sentence in original §4 ("No circular-shift null is run on the wide
curve — per R10's own explicit carve-out"). Instead:

- Run the SAME circular-shift-on-the-real-curve null exp-084 used (shift
  `c_wide(θ)`'s own sample array by every non-trivial integer offset,
  refit `free_period_with_widening` on each shift, record what fraction of
  shifts meet or exceed the un-shifted fit's own `R²_wide`) on Method A's
  full wide/dense `c_wide(θ)` array. This is a MANDATORY co-gate: no
  STABLE, DRIFTING, or §4(b) band 1–3 verdict may be reported as evidence
  unless this null is run and its result stated. Per R10's own
  deterministic-curve clause, interpret the result as a
  self-similarity/specificity question ("what fraction of this curve's own
  reorderings fit this well"), not a measurement-noise significance test —
  state this interpretation explicitly in the results writeup, not
  silently.
- Extend the identical circular-shift null to a representative sample of
  Method C's 37 sub-window fits: run it on every 4th sub-window center
  (θc ∈ {5°, 13°, 21°, ..., 77°}, 10 of 37, evenly spaced across the full
  domain) rather than all 37 (cost discipline — the point is to establish
  whether the ~50%-of-shifts-clear pattern exp-084 found at the narrow
  window recurs at this sub-window scale generally, not to gate every
  single one individually). If the sampled sub-windows' own circular-shift
  pass rate is ≥40% (i.e., comparable to exp-084's own 50% precedent —
  meaning even a genuinely non-periodic local segment routinely clears
  R²≥0.30 under reshuffling), `frac_recovered` is flagged UNRELIABLE and
  Method C's STABLE/DRIFTING classification is downgraded one tier (STABLE
  → DRIFTING-with-caveat if strong evidence otherwise supports periodicity,
  or → NOT STABLY PERIODIC if it does not) rather than reported at face
  value — matching exp-084's own precedent for exactly this situation.

**Fix 3 (Method C reference-angle bug).** Every one of Method C's 37 (now:
37 fits, 10 of which also get the circular-shift null per Fix 2)
sub-window calls to `_free_period_search`/`free_period_with_widening` MUST
pass `center_deg=θc` (that sub-window's own center), not the hardcoded
`39.0`. This is a one-line change at each call site. Methods A and B keep
`center_deg=39.0` unchanged (matches every existing T28 citation of
`P_model_a`/`P_edge_A`/`P_wide`/`P_fft` — internally consistent, not
broken by this bug per Red Team §1).

**Fix 4 (§4(b) band precedence + MECE closure).** Evaluate outcome bands
in this fixed priority order, first match wins (closes both the overlap
and the gap Red Team/QUANTUM verified):

1. **Method disagreement** (checked FIRST): if
   `|P_wide − P_fft| / mean(P_wide, P_fft) > 0.10`, report
   "method disagreement" — neither number is trusted as "the" wide-window
   period until reconciled. (This subsumes the old band 4 and is now
   checked before bands 1–3, closing the demonstrated overlap case.)
2. **Narrow window undershot** (only reached if methods agree): `rel_dev
   (P_wide, P_edge_A) ≤ 0.10` AND `rel_dev(P_fft, P_edge_A) ≤ 0.10` AND
   `R²_wide ≥ 0.55` (post-null, i.e. only reported if Fix 1's circular-shift
   null also clears — see Fix 1).
3. **Wide fit confirms 2.5338°, P_edge_A excluded**: `rel_dev(P_wide,
   P_model_a) ≤ 0.05` AND `rel_dev(P_fft, P_model_a) ≤ 0.05` AND
   `rel_dev(P_wide, P_edge_A) > 0.20` AND `rel_dev(P_fft, P_edge_A) > 0.20`.
4. **Catch-all — neither target, a third value** (closes the demonstrated
   gap): anything that reaches this point (methods agree, but neither band
   2 nor band 3 fired) is reported as its own new value, with both
   `rel_dev(P_wide, P_model_a)` and `rel_dev(P_wide, P_edge_A)` stated
   plainly, opening a fresh question rather than forcing a false-precision
   classification.

**Fix 5 (§4(a) missing strong-chirp cell).** Extend the three-way Method C
classification to a named fourth outcome: `frac_recovered ≥ 0.80 AND
spread > 0.50 AND |ρ| ≥ 0.5` → **STRONG COHERENT CHIRP** (a distinct,
sharper finding than plain DRIFTING — a large-amplitude, rank-monotone
trend, reported as its own labeled case, not folded silently into
DRIFTING). Evaluation order for §4(a): STABLE → STRONG COHERENT CHIRP →
DRIFTING → NOT STABLY PERIODIC (first match wins; this ordering is
non-overlapping by construction since STABLE requires `spread≤0.15`,
STRONG COHERENT CHIRP requires `spread>0.50`, and plain DRIFTING now means
`0.15<spread≤0.50` — the residual band between the two).

**Fix 6 (Method B taper).** Apply a Hann window to the `sin(θ)`-uniform
samples before the zero-padded FFT. State explicitly in the writeup that
an unwindowed rectangular FFT would itself present sidelobe leakage as a
"broadened/smeared peak" indistinguishable from a genuine chirp signature
— the taper is what makes `FWHM/f_peak` a meaningful chirp diagnostic
rather than a windowing artifact.

**Fix 7 (A/B vs C precedence).** State explicitly, as a pre-registered
rule (not discovered post hoc): Method C's local trend test (`ρ`, `spread`,
`frac_recovered`, now reference-angle-corrected per Fix 3 and
null-checked per Fix 2) is PRIMARY for question (a) — whether
`c_model_a(θ)` is genuinely (quasi-)periodic at all. Methods A and B
corroborate but do not veto a Method C finding when they disagree with it;
a disagreement between (A/B) and C is itself reported (matches
PHOTONICS's/Red Team's finding that A/B are stationarity-assuming
instruments that cannot, on their own, distinguish "no periodicity" from
"genuine broadband chirp too fast for a single-tone fit").

## Non-blocking disclosures adopted (attacks 8–10)

- **Attack 8** (near-field steering-vs-observation-angle): stated in the
  results writeup as an explicit caveat — `θ` here is the source's own
  steering angle at a fixed near-field observation range, and `sin(θ)`-
  uniform sampling is used because it is this sub-thread's own established
  convention (consistent with every `P_model_a`/`P_edge_A`/`P*` citation),
  not because it has been independently re-derived as the exact conjugate
  variable for this specific near-field steering geometry. No better
  alternative was offered by any seat.
- **Attack 9** (the "A" half/full-aperture mnemonic collision): the
  parameter table's `A=752` is explicitly labeled the HALF-aperture (its
  original, exp-084-inherited meaning); the Fraunhofer-fraction
  computation in `phase1_proposal.md` §1 uses the FULL aperture `2A=1504`
  — both values are restated together in the results writeup to close the
  latent trap for future citation.
- **Attack 10** (Idealization 4's unsourced flashlight-beam clause):
  dropped from the θ>80° justification; the vector/polarization-validity
  argument (this scalar model is least trustworthy at grazing incidence)
  already fully justifies the same exclusion on its own, with no witness-
  scene claim needed.

## What is NOT changed

Everything in `phase1_proposal.md` §§1 (mechanism), 2 (parameter table,
except the `center_deg` call-site fix and the "A" disclosure above), 3 (T1
statement — still N/A), 5 (idealizations, except dropping Idealization 4's
unsourced clause), and 6 (cost note) stands as originally proposed and
already committed (`c714ad5`... — actually commit `3912823`, see git log).
`derivation_results.json::leg_a`'s own already-published narrow-window
numbers (`P_model_a=2.533834586466165°`, `R²=0.36965580905914364`,
`P_edge_A=2.8421052631578947°`) are read, never recomputed, per R4.

## Independent re-check of Red Team's two headline numeric claims

Before adopting this synthesis, re-verified directly (not merely trusting
Red Team's own write-up):

- `cos(radians(5))/cos(radians(39)) = 0.99619/0.77715 = 1.2818`;
  `cos(radians(77))/cos(radians(39)) = 0.22495/0.77715 = 0.28948` — matches
  Red Team's cited `1.28`/`0.29` to the stated precision. Confirmed.
- Overlap case `(P_wide=2.60, P_fft=3.10)` against `P_edge_A=2.8421052...`:
  `|2.60-2.8421...|/2.8421...=0.085186`, `|3.10-2.8421...|/2.8421...=
  0.090741` — both `≤0.10`, band 1 (old numbering) fires;
  `|2.60-3.10|/((2.60+3.10)/2)=0.50/2.85=0.175439>0.10` — band 4 (old
  numbering) fires simultaneously. Confirmed exactly.

This synthesis, once committed, is the frozen prediction set. Phase 4 (the
corrected derivation script) is written and run only after this file is
committed to git — house discipline, non-negotiable.
