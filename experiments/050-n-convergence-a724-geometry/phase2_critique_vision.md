# PHASE 2 — CRITIQUE (VISION SCIENCE) · Panel Iteration 27 · exp-050

## Steel-man (≤150 words)

The proposal imports VISION's own T2 bar (`C_THR=0.005`) exactly as pinned
— no re-derivation, no silent drift — and cites it consistently with this
thread's own established usage (photopic baseline, same convention as
"0.0237, 4.7× T2 photopic C_thr" at Iteration 18). P-NCONV27-6's caveat
discipline is done right: FDTD-unvalidated status and T24's A=752-specific
provenance are stated **inline in the prediction row itself**, not buried
in an idealization footnote — directly extending exp-049's own
Attack-6/VISION-driven precedent (P-NCONV26-5) one geometry further, with
idealization 6 repeating it for anyone who skips the table. Idealization 9
explicitly refuses any perceptual/constraint-3 verdict while leaving
`C_THR` citable as the pre-existing scoring line a future run would use —
exactly the scope discipline the charter requires. The regression anchor
(§2.3) is fully executable against exp-049's own 108-row table, closing
the exact defect class (P-NCONV26-0) that embarrassed the last cycle.

## Sharpest attack (≤150 words)

P-NCONV27-6's falsification band tests only n-convergence stability
(relative move ≤1% under n-doubling) — it commits **no band on whether the
converged `|C|` value at GEOM78 itself stays under `C_THR=0.005`**, the
only quantity a contamination-risk citation actually needs. `A` shrinks
752→724, so `R_EDGE` shrinks 784.4→757.6 cells (~3.4%); the Huygens
propagator's own `1/√r` amplitude term alone raises this cell's magnitude
~1.8% before any fringe-phase shift is even considered — unaddressed here,
and idealization 5 explicitly disclaims magnitude validity at the new
geometry. So a "P-NCONV27-6 CONFIRMED, no flip" result will report only
that convergence order didn't change with `n`, not that the cell's actual
24.8%-headroom margin against `C_THR` (exp-049's own figure) survived the
geometry shift. A future near-boundary constraint-3 citation reading "no
flip" as "still safe at GEOM78" would be over-reading a claim this
proposal never commits to making.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to unqualified support

Add one more line to P-NCONV27-6 (or a P-NCONV27-6b), in the same
inline-disclosure style as P-NCONV26-5: report the GEOM78 converged `|C|`
value at the sharpest-stakes cell against `C_THR=0.005` and against
exp-049's own 24.8% headroom figure, with an explicit escalation trigger
(e.g., open a new live thread, not a new FDTD run) if the margin shrinks
materially. This costs nothing new to compute — `converged_value` is
already produced by the machinery this proposal reuses unmodified — it
only needs a committed, disclosed home in the prediction table so a bare
"no flip" cannot later be cited as an all-clear this cycle never measured.
