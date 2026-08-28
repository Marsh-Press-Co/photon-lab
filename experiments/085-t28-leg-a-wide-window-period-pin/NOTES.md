# exp-085 — Leg (a) Wide-Window/Dense Period Pin

Panel Iteration 62. Lead: MATERIALS & METAMATERIALS (rotation). Zero-FDTD
desk cycle, executing Iteration-62 queue Tier-1 item 7.

## Hypothesis

exp-084's leg (a) model (`dg048.edge_diffraction_c_empty_corrected`, an
exact non-paraxial Huygens–Fresnel sum over the source aperture's own two
tapered edges) was only ever fit inside a fixed 6°/31-point window
(36°–42°), where its free-period fit (`P_model_a=2.5338°, R²=0.3697`) sat
at the median of its own circular-shift null — INCONCLUSIVE, not because
the model is wrong, but possibly because the window is too narrow to
constrain a period search. Since the model is a deterministic, zero-noise
closed form, it costs nothing to evaluate far more widely and densely.
This cycle asked: does a wide/dense evaluation pin the model's own true
asymptotic period, or does it reveal the curve is not stably periodic at
all (a genuine near-field chirp, motivated by this bench sitting at 0.2%
of its own Fraunhofer distance)?

## Setup

Pure Python desk calculation, zero new FDTD calls. Reused, unchanged:
`dg048.edge_diffraction_c_empty_corrected`'s formula, `dg065.propagator_geom`/
`CONFIGS`, `ywp.free_period_with_widening`/`_free_period_search`,
`run69._fixed_period_fit`, `amb.window_means`/`weber`. Three instruments,
per the corrected, frozen spec (`phase1_proposal.md` + `phase3_synthesis.md`,
7 Red Team mandatory fixes applied): **Method A** (existing period-search
machinery on a 13×-wider/10×-denser θ∈[2°,80°] grid, N=3901, plus a
MANDATORY exhaustive circular-shift null — Fix 1); **Method B** (an
independent, Hann-tapered, zero-padded FFT over a `sin(θ)`-uniform grid,
N=32768 — Fix 6); **Method C** (37 sliding 6°-wide sub-windows, each
individually referenced to its own `θc` — Fix 3 — with a 10/37 sample also
circular-shift-null-tested — Fix 2), stated as PRIMARY for the
periodicity-stability question, A/B corroborating-only (Fix 7). A 4-band
MECE-closed precedence rule (Fix 4) and a named STRONG COHERENT CHIRP cell
(Fix 5) close the two decision-table gaps Red Team's Phase-2 audit found.

Predictions frozen (`phase3_synthesis.md`, commit `0caef17`) strictly
before `phase4_derivation.py` existed. A cached-Green's-function speed
optimization (`FastEval`, ~35× faster than the original per-call function)
was verified bit-identical (0.0 absolute difference) at 7 spot-check angles
before use — the underlying physics/formula is untouched.

## Result

**(a) Method-C-primary periodicity classification: nominally "STRONG
COHERENT CHIRP"** (`frac_recovered=1.000`, `spread=9.26` — an enormous
9.3× spread in locally-fit period across the domain — `ρ=0.882,
p=5.8×10⁻¹³`, a highly significant monotonic trend of local period against
`θc`). **But this reading is contested by its own reliability check**: of
the 10 sub-windows sampled for the mandatory circular-shift null (Fix 2),
4/10 (40%, at Fix 2's own trigger threshold exactly) show a null pass rate
≥40% — comparable to exp-084's own narrow-window precedent (50%), meaning
those specific local fits cannot be distinguished from curve-smoothness
alone. The pattern is genuinely bimodal, not uniformly contaminated: the
other 6/10 sampled windows show LOW pass rates (0%, 0%, 0%, 3%, 7%, 17%) —
comparably strong local evidence. **A real gap in this cycle's own frozen
spec, discovered here, not silently patched**: `phase3_synthesis.md`'s Fix
2 text specifies a reliability downgrade only for a nominal STABLE
classification ("STABLE → DRIFTING-with-caveat... or → NOT STABLY
PERIODIC"); it never specified what a ≥40% sampled null-contamination rate
should do to a nominal STRONG COHERENT CHIRP or plain DRIFTING outcome.
`phase4_derivation.py`'s classification code, implementing that text
literally, therefore reports "STRONG COHERENT CHIRP" un-downgraded even
though the reliability flag fired — printed as `UNRELIABLE per Fix 2 --
CLASSIFICATION (a) = STRONG COHERENT CHIRP`, the contradiction stated
plainly in the run's own output rather than resolved. This is Phase 5's
first item.

**(b) Period-value classification: METHOD DISAGREEMENT.** `P_wide=
3.2556°` (Method A, `R²_wide=0.0128` — indistinguishable from its own
circular-shift null, 45.4% of 3900 shifts meet or exceed it; R5
specificity control: 0/60 alternative targets clear the SUPPORT band, the
weakest possible reading) vs. `P_fft=8.7544°` (Method B's primary-range
peak; not sharp, `P2/P1=0.799` — a near-equal secondary peak — and the
FFT's own largest peak over the FULL, unrestricted spectrum sits at
`P_fft_full=140.07°`, entirely outside the `[1°,15°]` primary range —
essentially a broad low-frequency/near-DC trend, not a resolved tone).
`rel_dev(P_wide,P_fft)=62.8%` of their mean, far past the 10% disagreement
bar — the two global instruments do not even roughly agree with each
other, let alone with `P_edge_A=2.8421°` or the narrow-window's
`P_model_a=2.5338°`.

**Net reading**: neither global instrument (A, B) finds anything resembling
a clean, sharp, single dominant period anywhere in the wide window — both
read as noise-scale or badly unresolved. This is the honest answer to this
cycle's own §1 dichotomy: scenario (ii) ("the chirp is strong enough that
'the period' is not a well-defined single number at all... the finding IS
the drift, not a number") is the better-supported reading over scenario (i)
("a wide/dense fit converges tightly"). But Method C's own strong,
statistically significant trend — the instrument built specifically to
characterize that drift — is itself only partially cleared of the same
self-similarity confound R10 exists to guard against, in a real, disclosed,
bimodal way. **This cycle does not pin `P_model_a`'s asymptotic value with
certainty** (the queue item's own stated goal) — it establishes, with
reasonable confidence, that no such single value exists to pin, while
leaving the CHIRP characterization itself only partially certified.

## Learned

1. A deterministic, zero-noise model curve is not automatically immune to
   the sparse-window aliasing problem that motivated this cycle — extending
   the window from 6° to 78° did not produce a sharper period, it exposed
   the ABSENCE of one at the global scale (Method A's R² fell from 0.37 to
   0.013).
2. Fix 2's own reliability-downgrade language, written before any real data
   existed, had a genuine gap once a THIRD classification cell (STRONG
   COHERENT CHIRP, added by Fix 5 in the same synthesis) collided with it —
   a small, concrete instance of the program's own repeated lesson that a
   pre-registered decision table's edge cases are best found by trying to
   apply it to real numbers, not by inspection alone.
3. The null-contamination pattern across Method C's 10 sampled sub-windows
   is bimodal (6 low / 4 high), not uniform — a coarser "reliable/
   unreliable" binary undersells what the data actually show. A future
   cycle extending the null to all 37 sub-windows is now known, from this
   cycle's own timing, to be CHEAP (the full 37-window fit + 10-sample null
   pass took 29.8s of a 2353s run dominated entirely by Method A's
   exhaustive 3900-shift null) — flagged for Phase 5, not run here (this
   cycle's own frozen 10/37 sample stands as filed; extending it now, after
   seeing a borderline 40% result, would be exactly the undisclosed
   post-hoc pattern R4/R9 exist to prevent).
4. Performance: `edge_diffraction_c_empty_corrected` recomputes its full
   1504×1504 Green's-function matrix on every call regardless of θ; a
   cached-matrix wrapper (verified bit-identical) cut this cycle's
   evaluation cost by roughly 35×. Worth folding into `dg048` itself as a
   documented optional fast path if a future T28 cycle needs comparable
   evaluation counts again (not done here — out of this cycle's own scope,
   R4 discipline against speculative engine changes).

## Idealizations

Identical to `phase1_proposal.md` §5 (2D scalar Huygens–Fresnel model only,
single λ=600nm, model-internal question — no re-score of leg (a) against
real FDTD data, domain restricted to θ∈[2°,80°]), plus: Method C's
sub-window width (±3°) and its 10/37 null-sample stride are disclosed
design-time choices, not derived optima (§5 items 5 and — new this
cycle — the null-sample stride).

## Next

1. **Phase 5's own first job**: adjudicate the STRONG COHERENT CHIRP /
   reliability-flag contradiction this cycle's own spec left unresolved —
   does the bimodal 6-low/4-high null pattern support a qualified
   "probably real, spatially uneven" reading, or does Fix 2's own intent
   (as a THERMODYNAMICS/QUANTUM/EM/VISION/PHOTONICS-unanimous mandatory
   fix) require a full downgrade regardless of which nominal cell is hit?
2. Extend the circular-shift null to all 37 Method C sub-windows (now known
   cheap, ~1 additional minute) — the natural, low-cost next test.
3. This cycle's own negative global-instrument finding (Method A/B both
   read as noise-scale) may itself be worth folding into the standing
   T28 record as a boundary on how far the edge-diffraction mechanism class
   can be pushed with a single-tone description — a Phase-5/Checkpoint-2
   question, not this Director's to pre-empt.
4. The Tier-2 queue items untouched by this cycle (the joint EM/THERMO
   energy-interception cross-check, the near-null σ(I) article follow-up,
   the nine-cycle-deferred x-wall wavelength-generality leg, etc.) remain
   exactly as ranked in the Iteration-62 queue — this cycle did not touch
   Checkpoint criterion 4's own named cause.
