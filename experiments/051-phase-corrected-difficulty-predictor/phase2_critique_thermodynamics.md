# PHASE 2 — CRITIQUE (THERMODYNAMICS) · Panel Iteration 28 · exp-051

**Charter applicability, stated plainly.** T1 escape route is NONE. There is
no material law, no absorbed power, no ΔT, no emission band, no
detectability question anywhere in this cycle. **My literal sidecar duty
(absorbed power → temperature rise → emission band → detectability) has
nothing to attach to, exactly as at exp-049 and exp-050 — and I am not
manufacturing a thermal number that does not exist.** Where my seat does
bite on a desk cycle — cost accounting, budget honesty, and whether the
proposal's own accounting of its own work closes — I checked against source
and against the clock, not against the proposal's prose. Every number below
was produced by running committed code, per R4; nothing is hand-typed
arithmetic.

---

## Steel-man (≤150 words)

This proposal is honest about cost in the one place that mattered most last
cycle: it refuses exp-050's understated single-run 6225.3 s and anchors on
the Red-Team-established **≈12,490 s true total** — the exact disclosure my
own seat forced at Iteration 27, adopted one cycle later without being
asked, and correctly labelled as such. It costs bottom-up per line item
instead of by doubling guess, and its two large counts are arithmetically
right: I recomputed 144,036 = 36 × 4001 and 2,916 = 36 × 81 independently,
and confirmed exp-049's cited 1,145,772 = 108 combinations × 10,609
angle-samples exactly from `N_SERIES` + `N_REGRESSION` in
`experiments/049-.../run.py:34-35`. Scope is genuinely bounded — no
doubling series, no FDTD, no `lab/` change, no new suite stage — so the
worst case is a wasted desk afternoon, not a corrupted gate. And §4 names
its own way to lose before running.

## Sharpest attack (≤150 words)

**§6's 5.45 ms/evaluation unit does not transfer to this workload, and I
measured it.** That figure is exp-050's total/total, from a workload where
~85% of angle-samples come from n ≥ 1281 calls that build `_geom_derived`
and `_G_for_g` **once** and amortise them over thousands of matvecs. §2.2a's
`edge_diffraction_c_empty_g` — transcribed verbatim — rebuilds **both per
single angle**. Timed here at all 12 (λ, geometry, convention) points:
**168–269 ms/evaluation** (best-of-4). Normalising this box to the exp-050
runner (its own 3-function equivalent unit measures 26.05 ms here = 4.78×
the disclosed 5.45 ms), that is **≈43 ms/evaluation — 7.9× the assumed
unit**; the zero-crossing search alone lands at **≈103 min, not 13**. This
is load-bearing, not cosmetic: §2.2c explicitly defers `n_grid` to "Phase 3
to set, cost-permitting (§6)", so Phase 3 would size the crux resolution
against a budget that is ~8× wrong.

**Verdict: support-with-changes.**

---

## The single change that would flip me to plain support

**Promote the memoization from §6's optional Phase-4 aside to a mandatory
§2.2a construction**: hoist `_geom_derived(g)` and the propagator matrix
out of the per-angle function, memoized once per `(λ, g, convention)`, and
re-cost §6 at the hoisted unit. This is not a hope — I measured the hoisted
variant on the same box at the same points: **3.96 ms (`incoherent`) /
15.43 ms (`incoherent_corrected`)**, i.e. **0.83 / 3.23 ms
runner-normalised**, which puts the zero-crossing search at ≈5 min and
makes the proposal's own 13-minute headline true rather than 8× optimistic.
It is roughly a five-line change to the §2.2a snippet, and it also closes
the "low priority: cache `_geom_derived`/`_G_for_g` before any future
geometry-parameterized cycle" item Red Team ranked #6 for this very
iteration (LOGBOOK, Iteration 27 close). Absent that, §6 must be restated
at ≈43 ms/evaluation (≈1.7 h, best case) so Phase 3 sets `n_grid` against a
real number.

---

## Measurements (this box, `numpy 2.4.6`, single-threaded)

Propagator matrix at GEOM78: 1448 × 1448 (16.8 MB real `r`, 33.5 MB complex
`G`). Machine-normalisation anchor: reconstructing exp-050's own workload
per-function on this box gives an effective unit of 26.05 ms/evaluation
(59,704 s projected / 2,291,544 evaluations) vs the disclosed 5.45 ms →
**this box is 4.78× slower than the exp-050 runner**; all "runner-norm."
figures below are the measured value ÷ 4.78.

| Quantity | This box (best) | Runner-norm. |
|---|---|---|
| `_geom_derived(GEOM78)` | 23.8 ms | 5.0 ms |
| `_G_for_g(600 nm, gd)` | 110.9 ms | 23.2 ms |
| one matvec `G @ amp` | 6.9 ms | 1.4 ms |
| **§2.2a as written, mean of 12 (λ,g,convention) pts** | **205.6 ms** | **43.0 ms** |
| §2.2a as written, range over those 12 pts | 167.1–268.9 ms | 35.0–56.3 ms |
| §2.2a **hoisted/memoized**, `incoherent` | 3.96 ms | 0.83 ms |
| §2.2a **hoisted/memoized**, `incoherent_corrected` | 15.43 ms | 3.23 ms |
| `beam_divergence_incoherent(38,20,600,G78,n=81)` | 1.392 s | 0.291 s |
| `beam_divergence_incoherent_corrected(…,n=81)` | 4.308 s | 0.901 s |

**Corrected §6 budget, as the proposal is currently written** (best-case
timings, runner-normalised, single-threaded):

| §6 line item | Proposal | Measured-basis |
|---|---|---|
| Zero-crossing search (144,036 evals) | 785 s | **≈6,200 s** |
| `\|C(n=81)\|/ABS_TOL` (36 calls) | 15.9 s | **≈21.5 s** |
| Slope + regression anchor | ~0.5 s | ~4 s |
| **Total** | **≈13 min** | **≈1.7 h** (avg-case timings: 3–4 h) |

Note the accidental resonance: the corrected best case, ≈104 min, is
exp-050's own disclosed clean-run figure — the cycle this proposal claims
to be "order of magnitude below."

---

## Further bookkeeping findings (secondary, all checkable, none flip my verdict)

1. **P-PCDP-0's spot-check count does not close.** §2.3 asserts "9×3 = 27
   (θ₀,λ) spot-check points"; §2.1 defines exactly **9** (θ₀,λ) cells (3 θ₀
   × 3 λ), so λ is counted twice. §6 inherits it ("27 spot points × 2
   conventions ≈ 54"); the true figure is 9 × 2 = **18**. Non-load-bearing
   to cost (both are negligible), but it is a hand-typed figure inside the
   one prediction the proposal designates as "checked first, gates
   everything else" — precisely the R4 shape this program has now carried
   for three consecutive cycles (23/24/25 → 25/26), and the hardened
   tripwire adopted at Iteration 26 is one instance from firing.
2. **P-PCDP-5's N does not exist under §2.2e/§6's own costing.** A slope
   *ratio* `|slope_corrected|/|slope_incoherent|` is defined per **cell**,
   not per combination (P-PCDP-4 says so itself: "at ≥3 of 4 **cells**").
   §2.2e costs 18 GEOM78 *combinations* = 9 cells × 2 conventions, which
   yields **9** ratios — but P-PCDP-5 scores "the **18** per-combination
   slope ratios" with an IQR and a median split. Either the prediction's N
   is wrong (and an IQR at N=9 is thinner than P-PCDP-5's band assumes), or
   18 A=752 slope evaluations are missing from §6. Freeze this before
   Phase 3, not after.
3. **The `NOT_FOUND` retry is uncosted.** §5 idealization 5 commits to
   widening the search window to 1.5·P "once before giving up". At an
   unchanged `n_grid` that is a **second full 4001-point scan** for every
   combination that fails — up to +100% on the single dominant line item,
   with no contingency anywhere in §6. Commit the retry's own evaluation
   count to the completeness ledger.
4. **No completeness-ledger total is committed.** exp-049 asserted
   `len(ledger) == 972` in code; exp-050 committed 1944 records. This
   proposal commits only `n_not_found`/`n_widened` counts (§5.5) and no
   total record count, so Phase 4 has no absolute bookkeeping identity to
   fail on. Commit the expected record count as an assertion, this
   program's own idiom.
5. **exp-050's forward guidance is cited for its runtime figure but not
   adopted as practice.** exp-050's NOTES.md Results carries my own
   Iteration-27 recommendation verbatim — "persist a partial/crash-state
   timing record from process start, not only the final successful run's
   `elapsed_s`". §6 borrows that cycle's *corrected number* and leaves the
   *fix that produced it* on the floor. One `time.time()` at import and a
   flushed timing file makes the next understated-runtime disclosure
   impossible instead of merely embarrassing.
6. **For balance, the one place §6 over-counts:** 18 of the 36
   `|C(n=81)|/ABS_TOL` calls are at GEOM_EXP042_OLD, but P-PCDP-1's
   classifier is scored at GEOM78 only and P-PCDP-3 reuses P-PCDP-2's
   `|offset|`-only threshold — so no committed prediction consumes the
   A=752 half of §2.2d. ~16 s of the corrected budget is dead work, and
   dropping it is free.

---

## Reproduction

Timing script: `/tmp/claude-0/-home-user-photon-lab/3f566c8d-1309-5c26-a429-8ae6c0875c6b/scratchpad/{timecheck,t2,t3}.py`
(scratch, outside the repo). It imports
`experiments/050-n-convergence-a724-geometry/design_geometry.py` unmodified
and transcribes §2.2a's snippet verbatim; no repo file was touched, no
`lab/` code was read into the timing path beyond `lab.ambient`'s own
committed `window_means`/`weber`.
