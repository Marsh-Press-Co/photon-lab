# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 62 · exp-085

## Steel-man (150 words)

The physics motivation is genuine, not decorative: this bench sits at
0.197% of its own Fraunhofer distance, and the exact `hypot()` propagator
`edge_diffraction_c_empty_corrected` already uses really does couple angle
and source-point position nonlinearly — a textbook chirp signature, named
qualitatively by EM's own exp-084 Phase-5 review before this proposal
existed; this cycle is the first to quantify it. Method C's 37-sub-window
local-fit sweep is informative on its own terms regardless of Methods A/B's
headline: whether the local period drifts coherently (`|ρ|≥0.5`) is a real,
orthogonal diagnostic that survives even if the wide-window significance
question is contested. R4 discipline is exemplary — `P_model_a`/`P_edge_A`
are read from committed JSON, never hand-typed; `edge_diffraction_c_empty_
corrected` and `free_period_with_widening` are reused verbatim, not
reimplemented; Method B's independence from Method A's bounded
candidate-range search is argued explicitly, not merely asserted. The R5
specificity-over-targets control is at least run, as house rule requires.

## Sharpest attack (150 words)

§4's own disclaimer — "No circular-shift null is run on the wide curve —
per R10's own explicit carve-out... a null-under-noise question does not
apply" — inverts what R10 actually says. R10's deterministic-curve clause
states the test still APPLIES to a noise-free curve, only its READING
changes ("both are legitimate uses of the same test"); it never exempts a
deterministic curve from running it. exp-084's own leg (a) downgrade was
*produced* by circular-shifting this exact model curve and finding 50% of
its own shifts also cleared R²≥0.30 — the worked precedent this very
proposal cites as its "already-published" `P_model_a` is itself proof the
test was mandatory, not skippable, on a deterministic curve. Substituting
only the R5 target-sweep is precisely the "specificity-over-targets sweep
is not a substitute" pattern R10 exists to forbid — applied to the very
curve QUANTUM wrote that carve-out about. Without it, outcome-bands 1/2's
"real tightening" claim (`R²_wide≥0.55`) has no floor: `free_period_with_
widening` may simply fit any long, smooth curve comparably well under
rotation, independent of phase.

## Verdict: support-with-changes

The re-derivation idea itself is sound and cheap, and directly executes
what exp-084's own Red Team ranked the sharpest available next move (Tier
1 #7). But two load-bearing defects must be fixed before Phase 4 runs, not
patched after the fact:

**1. The R10 carve-out is misapplied (the sharpest attack, above).**
Method A's wide/dense fit and Method C's per-sub-window fits all reuse
`free_period_with_widening`'s own 3-parameter LSQ machinery — the same
machinery whose susceptibility to spurious fits on a smooth deterministic
curve is *exactly* what exp-084's circular-shift null measured and found
alarming (50.0% of shifts cleared the SUPPORT bar). A 13×-wider, 10×-denser
window changes the sampling, but says nothing about whether the fitting
procedure itself remains just as promiscuous at that scale — that is an
empirical question, not one settled by asserting the input curve is
noise-free. **Required fix:** run the identical circular-shift-on-the-
model-curve null (as exp-084's own §3/Phase-5 did) on Method A's wide
curve — and, ideally, on a sample of Method C's sub-windows — before any
`R²_wide≥0.55`/`P_wide→P_edge_A` reading is reported as evidence, not
merely as a description.

**2. §4(b)'s four outcome bands are neither mutually exclusive nor
exhaustive** — the identical defect class this exact T28 sub-thread's own
outcome-scheme design has produced before (exp-076, Iteration 53, caught
by Red Team's Phase-2 audit). Checked directly, not by inspection alone:

- *Overlap (bands 1 and 4 co-fire):* `P_wide=2.60°`, `P_fft=3.10°`
  (`R²_wide` assumed ≥0.55). `rel_dev(P_wide,P_edge_A)=0.0852≤0.10` and
  `rel_dev(P_fft,P_edge_A)=0.0908≤0.10` → band 1 ("wide fit moves toward
  `P_edge_A`") fires. But `rel_dev(P_wide,P_fft)` relative to their mean
  `=0.50/2.85=0.175>0.10` → band 4 ("method disagreement — neither number
  is trusted") *also* fires, with the opposite prescription, and §4 states
  no priority rule for which governs.
- *Gap (no band fires):* `P_wide=2.55°`, `P_fft=2.70°`.
  `rel_dev(P_wide,P_model_a)=0.0133≤0.05` but `rel_dev(P_fft,P_model_a)
  =0.0656>0.05` → band 2 fails (needs both ≤0.05).
  `rel_dev(P_wide,P_edge_A)=0.1028>0.10` → band 1 fails.
  `rel_dev(P_wide,P_model_a)=0.0133` is not `>0.05` → band 3 fails (its own
  first condition).
  `rel_dev(P_wide,P_fft)` relative to mean `=0.15/2.625=0.057≤0.10` → band
  4 fails. Every band fails on a physically ordinary pair of fitted
  values — the classification scheme is silent exactly where a real,
  boring "the two methods roughly agree, and roughly agree with the
  narrow-window fit, but neither cleanly resolves against `P_edge_A`"
  result would land.
- A contributing design asymmetry: band 3 is defined on `P_wide` alone
  (never checks `P_fft`), unlike bands 1/2, which require both — this
  asymmetry is *part of* why the gap above is reachable.

**Required fix:** add an explicit precedence rule (e.g., evaluate band 4
first; a band is entered only if no higher-priority band's conditions are
met) and redefine band 3 or add a fifth catch-all so every reachable
`(P_wide, P_fft, R²_wide)` triple lands in exactly one bucket, pre-
registered before Phase 4, not adjudicated after seeing the numbers.

Neither defect touches Method C, which is well-posed on its own and should
proceed regardless of how 1–2 are resolved.

## Parameter change that would flip my verdict

If §4 were rewritten, before any run, to (a) make the circular-shift-on-
the-model-curve null mandatory and reported alongside the R5 specificity
sweep for both Method A's wide fit and Method C's per-window fits, gating
any SUPPORT-flavored band exactly as R10's own worked exp-084 precedent
did, and (b) replace the four-band scheme with an explicitly ordered
(or provably partition-complete) decision procedure closing the
demonstrated overlap and gap — I would move to support outright.
