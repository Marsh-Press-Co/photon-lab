# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 26 (candidate exp-049)

*Blind parallel critique. Charter: where absorbed energy goes — absorbed
power → temperature rise → emission band → detectability. This proposal has
no absorption, no material, no FDTD call, so that charter has no direct
purchase this cycle; said plainly below rather than manufactured. Per this
program's own precedent, THERMODYNAMICS has repeatedly also served as a
program-integrity/bookkeeping check (e.g. the h_conv/mass_kg length-scale
catch, Iteration 22) — that is the lane this critique works in.*

---

## Steel-man (≤150 words)

No energy-absorption content to assess — conceded, not manufactured. What I
can certify, in this seat's other established lane (bookkeeping): I
independently recomputed every load-bearing number and every one reproduces.
Ceiling derivation: Δθ_req=1.4127/10=0.14127°, n_req=100/0.14127+1=708.87≈709
— correctly bracketed by 641/1281. Sample count: ΣN_SERIES+401=10,609;
×36×3=1,145,772 — both exact. The full samples-per-period table (all four
FWHM rows, all nine λ,θ₀ periods via P=λ_cells/(A·cosθ)) and P-NCONV26-2's
"no crossovers" difficulty ordering both reproduce bit-for-bit from the
cited T21 formula. Best of all: the cited exp-046/exp-042 figures —
4.472688822027389%, −0.004006497410421138 — match `results.json` to the full
printed double, not a rounded retype. That is the *opposite* of this
program's own R4 failure mode, in the document most likely to repeat it.

## Sharpest attack (≤150 words)

Two in-lane findings. **(1) A real, if small, arithmetic slip.** P-NCONV26-5's
"margin ratio 1.2483×" / "24.83% headroom" should be
0.005/0.004006497410421138 = **1.247972852046454× / 24.7973%** — off by
~0.03pp, unshown as a formula, unlike every other number in this document.
Non-load-bearing (bands are 1%/5%) but it is exactly the hand-computed-figure
species R4 exists to catch, recurring one cycle after R4 was adopted. **(2) A
genuine scope/delivery risk.** This cycle commits to 1,145,772 dense
1504×1504 complex-propagator matrix-vector evaluations — roughly two orders
of magnitude more compute than any prior zero-FDTD desk cycle in this
program's history — against a cost estimate §6 itself admits is "not yet
profiled." Given the program's own repeatedly-named fix-docket-delivery
pattern (7+ instances, three straight cycles 23–24–25 alone), an unprofiled
run at this scale is exactly the shape that invites partial computation
quietly reported as complete.

## Verdict

**support-with-changes.**

The proposal is unusually well self-audited — every formula shown its own
work, every cited historical figure verified exact against source
`results.json` files, the 36-cell grid partitioned cleanly across predictions
with no double-counting and no prediction's committed band secretly assuming
another's *outcome* (each is scored against fresh sweep data, not against a
sibling prediction). The "zero FDTD calls" claim is also verified true at the
code level: `lab.ambient.window_means`/`weber`/`incoherent_sum` are pure
`numpy` array arithmetic (checked directly, `lab/ambient.py:26-73`) with no
solver call anywhere in the chain. One caveat on non-circularity, not
disqualifying: P-NCONV26-1a/1c/2/4 are all downstream of the *same* nine
measured period values and the *same* Δrel(41) sweep — a single shared bug in
`_G_for`/`_src_amp` (unlikely, but this proposal reuses that code unmodified
without re-deriving it) would move several predictions together in a way
that could look like independent confirmation but isn't. The one arithmetic
slip found is real but cosmetic. The scope-risk finding is the one that
should gate Phase 3: at 1.1M+ evaluations with no profiled timing, this
program's own history says the failure mode to defend against isn't wrong
physics — it's a "converged, confirmed" NOTES.md claim resting on a partial
or truncated run.

## Flip

Add one mandatory Phase-3 fix: before any P-NCONV26-1/3/4 n\* claim is
trusted, `run.py` must emit a machine-countable completeness ledger — one
record per (cell, function, N_SERIES entry) actually evaluated, expected
count 972 (108 cell-function combinations × 9 n-values including n=401) —
plus the actual profiled wall-clock time, both committed alongside
`results.json`. If that ledger is missing or short, I flip to oppose: not
because the physics would be wrong, but because this program has now named
the claimed-complete-but-not-delivered pattern often enough (Iterations 13,
14, 15, 17, 20, 21, 22, 23, 24, 25) that a 1.1-million-evaluation cycle with
an admittedly unprofiled cost estimate is exactly where it would recur next,
and would be the hardest instance yet to catch by inspection alone.
