# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 62 · exp-085

*Fresh context, blind to any other seat's current-cycle Phase-5 review. Read
in full: PANEL.md, LOGBOOK.md (RULED OUT R1–R10, T28 thread Iterations
58–61 in full), `experiments/084-.../NOTES.md`, and exp-085's full record in
order (`phase1_proposal.md` → all five Phase-2 critiques →
`phase2_redteam_audit.md` → `phase3_synthesis.md` → `phase4_derivation.py`
→ `derivation_results.json` → `NOTES.md`). Every headline number below was
independently re-derived from the committed code and data, not accepted on
citation (R4).*

## 0. Independent verification performed (R4 discipline)

1. **Re-fit Method A's stored `c_wide(θ)` array from scratch**, calling the
   same `free_period_with_widening` used in `phase4_derivation.py`, on the
   3901-point array read directly out of `derivation_results.json`:
   `P_wide=3.255639°, R²_wide=0.012802`, window `narrow[1,4]`, an **interior
   optimum**. Matches the committed figure to the printed digit. Confirmed
   as reported — Method A really does find essentially nothing at global
   scale.
2. **Recomputed Method C's three headline aggregates from the raw 37
   per-sub-window records**, not the pre-aggregated top-level fields:
   `frac_recovered=1.0`, `spread=9.258667605452366`,
   `rho=0.8816974869606448` (Spearman, `p=5.76×10⁻¹³`) — all reproduce
   exactly, and the 10 individual sampled circular-shift-null pass rates
   (`0.867, 0.067, 0.633, 0.033, 0.6, 0.6, 0.0, 0.167, 0.0, 0.0`, at
   `θc=5,13,21,29,37,45,53,61,69,77`) reproduce exactly against
   `derivation_results.json` — confirming both the task's own cited numbers
   and NOTES.md's "4/10 at ≥40%" count.
3. **A genuinely new, independently-discovered defect** (not disclosed
   anywhere in the record): re-executed `free_period_with_widening`'s own
   three-stage widening loop directly for the 6 sub-windows whose raw
   fitted period is exactly `4.000°` (`θc=45,59,61,63,71,73` — all in the
   record, none flagged). At **every one** of these 6, **all three stages
   (`narrow[1,4]`, `wide[1,15]`, `widest[1,60]`) are boundary-pinned** — the
   search never finds an interior optimum anywhere in `[1°,60°]`; R² keeps
   climbing as the search range widens (e.g. `θc=61`: `R²=0.651→0.983→0.987`
   across the three stages) with no peak in sight. The function's own stage-
   selection logic (`y_wall_prescreen.py::free_period_with_widening`,
   `if chosen is None or (chosen["at_boundary"] and not at_boundary)`)
   **never updates past the first stage once every stage is boundary-pinned
   — it silently returns the narrowest, worst-fitting stage's own result**
   (`θc=45`: reported `P=4.00°, R²=0.41`, while the widest stage tried
   reaches `P=60.00°, R²=0.82`, itself still not a real answer). This is a
   real, reproducible bug in shared, multiply-reused T28 machinery, not a
   one-off. Compounding it: `phase4_derivation.py`'s Method C loop builds
   `stages_sub` (the full 3-stage trace, including every `at_boundary`
   flag) but **never writes it to `out["method_c"]`** — the evidence needed
   to detect this failure mode from the committed JSON alone does not
   exist; it required re-running the code.

## 1. Does the optical interpretation of Methods A/B/C cohere?

It does, and once the boundary-pinning defect above is accounted for, it
coheres **more tightly and more specifically** than NOTES.md's own framing
states.

**The FFT's true peak at `P_fft_full=140.07°`, entirely outside `[1°,15°]`.**
A period of 140° against a 78°-wide domain means the dominant spectral
component does not complete even one full cycle across the entire measured
range — this is not a resolved tone at all, it is the spectral signature of
a **slowly-varying broadband envelope**: the aperture's own amplitude
taper, the `1/√r` geometric spread, and the obliquity factor, all of which
vary smoothly and monotonically with `θ` over a wide sweep, with no
periodic content. A near-DC/broad-envelope dominant component is exactly
what you get when a diffraction integral's *envelope* physics (finite-
aperture roll-off, not fringe interference) dominates the curve's total
variance over a domain wide enough to include large excursions in
obliquity — optically unremarkable and, read this way, not itself evidence
against genuine short-period fringe content existing locally.

**Method C's own numbers, disaggregated by angle, show exactly this
split.** Filtering the 37 sub-windows for `p_local_corrected > 6°` (the sub-
window's own width — i.e. the "period" is longer than the data window used
to measure it, so no full cycle was ever observed) gives **15 of 37**,
concentrated entirely at `θc ≥ 47°`; the 6 stage-selection-bug cases above
are a subset of these, concentrated at `θc ∈ [45°,73°]`. The near-normal
half of the domain (`θc=5°…27°`, plus most of `29°…43°`) reports
consistently modest, plausible, non-boundary-pinned local periods
(`1.2°–3.8°` corrected) — the same order of magnitude as `P_edge_A` and
`P_model_a`. **The optically coherent picture is: genuine, modest-period
diffraction fringe structure plausibly exists only near the aperture's own
near-normal region; the grazing half of this cycle's own domain is not
measuring periodicity at all — it is an increasingly under-constrained fit
to a smooth, non-periodic envelope, which is exactly what floods `spread`
and `ρ` with large, spuriously coherent numbers, and exactly what makes
Method B's global spectrum peak near-DC.** Method A's collapse
(`R²_wide=0.013`, effectively noise-scale) is the single-tone instrument's
correct response to averaging a real ~2–4° near-normal tone against a
non-periodic grazing-incidence envelope across one global fit — not a
contradiction of the other two methods, but the same story from a third
angle.

## 2. Is NOTES.md's headline framing accurate, overclaimed, or underclaimed?

**Underclaimed — the problem is more severe and more specific than "the
classification is contested by its own reliability check."**

NOTES.md correctly flags that Fix 2's reliability language was never
extended to the STRONG COHERENT CHIRP cell, and correctly reports the
disclosed 4/10 (`≥40%`) null-contamination rate honestly, bimodally, rather
than smoothing it into a single number. That much is right, and is itself a
genuine, well-executed piece of self-correction (see §3).

But the circular-shift null — the only reliability instrument this cycle
actually ran — **does not catch, and in one demonstrated case (`θc=61`,
sampled, null pass rate `0.167`, nominally "reliable" by Fix 2's own
`<0.40` bar) actively misses**, the boundary-pinning defect in §0.3. A
circular roll of a short window that is dominated by a smooth, non-periodic
envelope tends to *break* whatever monotonic structure is there for nearly
every shift too, so the null test can read "significant" (a low pass rate)
for a fit that is not measuring periodicity at all — a different failure
mode than the self-similarity risk R10 was written to catch, and one this
cycle's own instrument has no way to see. Once this is accounted for,
**6 of 37 (16%) of Method C's "recovered" (`r2_local≥0.30`) sub-windows are
not period measurements — they are unconverged boundary artifacts of the
shared widening machinery**, concentrated exactly in the high-`θc` region
that also drives most of the reported `spread=9.26` and a large share of
the `ρ=0.882` rank correlation (both statistics are dominated by the range
`[1.2°, 35.0°]`, and the 34.96° extreme at `θc=77°` is itself one of these
boundary artifacts). A cleaned re-classification, excluding these 6
sub-windows (and probably re-examining the other 9 boundary-pinned-but-not-
exactly-4.000° cases, `47°–75°`, on the same grounds), would very likely
**not** clear STABLE, STRONG COHERENT CHIRP, or DRIFTING's own `frac_
recovered≥0.80` gate at all — the honest, most likely reading is closer to
"genuine, modest, T28-family-scale local periodicity confined to the
near-normal quarter of the domain; no periodicity, of any kind, measurable
at grazing incidence with this instrument," which is a materially
different and more specific finding than "STRONG COHERENT CHIRP, nominally,
contested by its own reliability check."

## 3. Steel-man of this cycle's own execution

This is a well-run, honestly self-critical desk cycle by this program's own
demanding standard. Phase 2's five blind critiques converged, independently,
on the same R10 misreading (all five, not four of five as the assignment
briefed — Red Team caught that headcount error too), and Red Team's own
audit independently re-derived every numeric claim from primitives before
ruling, rather than trusting any critique's paraphrase — including
re-deriving the `center_deg=39.0` bug's exact `cos(θc)/cos(39°)` factor and
both of QUANTUM's MECE counterexamples from scratch. All 7 mandatory fixes
were implemented, verifiably: the `FastEval` speed optimization was gated
behind a mandatory bit-identical spot-check before use; the exhaustive
3900-shift circular-shift null on Method A actually ran (2260s of real
compute, not skipped or subsampled where the spec called for exhaustive);
and — most creditably — when the frozen spec's own Fix 2 language turned
out to have a real gap once real numbers hit it (no downgrade rule for
STRONG COHERENT CHIRP), the Director disclosed this in the run's own
printed output and in NOTES.md rather than quietly patching the code to
produce a cleaner-looking headline. That is exactly the house discipline
this program asks for.

## 4. Sharpest critique of this cycle's own execution

The self-disclosed gap (§3) is real but not the deepest problem in this
run. The deeper problem is that **the reliability instrument this cycle
built (circular-shift null, sampled 10/37) is not well-matched to the
failure mode that actually dominates this cycle's own result** — a
widening-stage-selection bug in reused, shared machinery that silently
discards better (still-uninformative) fits in favor of the worst available
one, with the diagnostic trace needed to detect it (`stages_sub`) computed
and then thrown away before it reached `derivation_results.json`. Nobody
across five Phase-2 critiques, the Red Team audit, or the Director's own
Phase-3 synthesis inspected the intermediate per-stage widening trace for
Method C's own sub-windows, even though Fix 3 (the `center_deg` bug) was
found by exactly this kind of primitive-level tracing applied to a
different part of the same function. This is not a criticism of any one
seat — it is a genuine blind spot the whole cycle shared, and it means a
defect in machinery reused across many prior T28 cycles (`y_wall_
prescreen.py::free_period_with_widening`, in service since exp-078) has now
been shown, for the first time, to produce a materially wrong "chosen"
period under a specific, reproducible condition (every stage boundary-
pinned) — worth checking whether it silently affected any earlier cycle's
own reported number.

## 5. Verdict: **PARTIAL**

Matches this T28 desk-cycle sub-thread's own unbroken precedent (Checkpoint
criterion 2 is N/A — no mechanism-class or constraint-bearing claim is made
anywhere in this cycle). The queue item's own stated goal ("pin `P_model_
a`'s asymptotic value with certainty") is **not met**, and this review's own
independent finding sharpens, rather than merely confirms, NOTES.md's own
"no single value exists to pin" reading — while also showing the STRONG
COHERENT CHIRP characterization itself needs a real downgrade, not just a
disclosed contradiction, once the boundary-pinning artifact is accounted
for. Not RULED OUT: nothing here forecloses genuine near-field diffraction
structure near the aperture's own near-normal region, and this cycle
sharpens where to look for it. Not PROMISING: the net result is a
methodology finding about the program's own shared instrument, not forward
motion on any phenomenon constraint.

## 6. Ranked top-3 candidate directions for Iteration 63

1. **Fix `free_period_with_widening`'s all-stages-boundary case** and audit
   whether it silently affected any prior T28 citation. The fix is cheap
   and precise: when every stage is boundary-pinned, either (a) return the
   *widest* stage tried with an explicit `no_interior_optimum=True` flag
   (rather than silently the narrowest/worst), or (b) return `None`/a
   named "UNRESOLVED — no interior optimum in [1°,60°]" sentinel instead of
   a numeric period at all. This is shared, reused machinery (exp-078
   onward) — a defect here is exactly the class of finding this program's
   R4/R9 house rules exist to catch and log, and it is now independently,
   reproducibly demonstrated (6/6 confirmed at `θc=45,59,61,63,71,73`, all
   three stages, exact numeric factors reproduced from source). Cheapest,
   most consequential, zero new FDTD.
2. **Re-classify Method C excluding the 6 (or, conservatively, all 15)
   boundary-pinned/period-exceeds-window sub-windows**, reusing this
   cycle's own already-computed data (no new evaluations needed) plus the
   fix from (1), and re-score `frac_recovered`/`spread`/`ρ` on the cleaned
   set. This directly answers whether "STRONG COHERENT CHIRP" survives
   once the artifact is removed, or whether the honest reading is "genuine
   modest periodicity confined to the near-normal quarter, nothing
   measurable at grazing incidence" — the specific, falsifiable version of
   this review's own §2 finding.
3. **Extend the circular-shift null to all 37 Method C sub-windows**
   (already named in NOTES.md's own "Next," confirmed cheap, ~30s of the
   2353s run) — combined with (1)+(2), this would give the first fully
   trustworthy picture of leg (a)'s own local-periodicity structure this
   nine-plus-cycle sub-thread has produced, at essentially zero marginal
   cost.

Standing Tier-2/Tier-3 items (joint EM/THERMO energy-interception
cross-check, near-null σ(I) article follow-up, nine-cycle-deferred x-wall
wavelength leg, the ritualization governance question) are untouched by
this cycle and remain exactly as ranked at Iteration 62's close — this
review does not re-rank them; they are outside a model-internal desk
cycle's own scope and this seat's charter this round.
