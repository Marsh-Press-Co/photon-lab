# Phase 2 Critique — ELECTROMAGNETISM (exp-097, Panel Iteration 74)

*Seat charter: field/wave behavior, impedance matching, energy coupling;
reciprocity/passivity/causality bookkeeping. T1 is N/A this cycle (zero-FDTD
code verification) — applied instead to whether the phase-ramp/k-vector/
taper-window formulas this cycle independently recomputes are correct,
self-consistent field-theory statements. Independently re-derived from
source, not taken on the proposal's word: `lab/fdtd2d.py:132-186`
(`add_line_source`), `experiments/069-.../design_geometry.py` (R3/R4/R5
blocks), `experiments/095-.../NOTES.md` lines 265/291/304.*

## Steel-man

The two new field-theory recomputations are correct, verified independently
this session. `phase_expected` (Check 4, unchanged, reused) exactly
reproduces `add_line_source`'s own ramp `k=2π/lam · sin(θ)·(y−ȳ) + rel_phase`
— a textbook linear-phase-gradient beam-steering relation, dimensionally
consistent (`lam` is cells/wavelength, so `k` is rightly radians/cell).
Check 7's `taper_expected` is a bit-exact copy of the raised-cosine
apodization at `fdtd2d.py:160-164`, and its predicted CLEAN-under-FI-A/B/C
table is verifiably correct by inspection: `profile` depends only on `edge`
and `n=y_hi−y_lo`, never on `angle_deg` or `cpl` — so a resolution or angle
fault genuinely cannot leak into it. The specificity claims in §5's table are
real, not asserted.

## Sharpest attack

§2b's own "R4 discipline… independently spot-checked against
`design_geometry.py`'s own comments this session (bit-exact)" claim is
false as stated, for both new families. R3: proposal computes `y_hi=2316`
and claims it "matches… `R3_BASE_NY` comments (450/60/**2376**)" —
`design_geometry.py`'s own comment for `R3_BASE_NY` is 2376 (`round(1584·1.5)`),
but `r3_config`'s actual `y_hi = ny − y_lo = 2376 − 60 = 2316` (verified
directly from source). 2316 ≠ 2376. Identical error for R5 (`y_hi=3860`
claimed to match `R5_BASE_NY` comment "3960"; true `y_hi=3960−100=3860`,
also ≠3960). The proposal cited the wrong constant as its own verification
target — twice — for exactly the aperture-midpoint quantity (`y_lo`,`y_hi`)
the phase-ramp formula centers on. Non-load-bearing to Phase 4 (the actual
Check-5 code correctly asserts against `target["y_hi"]`, not `R3_BASE_NY`),
but this is a hand-typed "precisely recomputed" figure that does not
reproduce, in the same document whose entire mandate is closing exactly
this class of unverified claim (R18) — a fresh R4-house-discipline instance,
caught before Phase 3, not after.

## Verdict: support-with-changes

The k-vector/taper formulas and their fault-injection logic are sound and
correctly scoped (Idealizations 41/42 honestly disclose Check 5/7's
formula-restating nature). Fix required before Phase 3 freeze: correct
§2b's two mismatched citations (compare against the config's own `y_hi`,
not `R{3,5}_BASE_NY`) — a one-line prose fix, not a code fix.

**Parameter change that would flip verdict to oppose:** if Check 5's actual
assert code (not just its prose) compared against `R{3,5}_BASE_NY` instead
of `target["y_hi"]` — i.e. if the mismatch were load-bearing rather than
cosmetic — the R3/R5 extension would spuriously report CLEAN or DEFECT
against the wrong ground truth, defeating R18's own purpose for this item.
