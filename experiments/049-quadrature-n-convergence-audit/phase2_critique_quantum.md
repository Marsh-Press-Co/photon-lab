# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 26 (candidate exp-049)

*Blind parallel critique. Charter: non-classical absorption, state-dependent
or coherent interactions; mechanisms enter the bench only as effective
classical parameters. This cycle executes MY OWN three-cycle-deferred queue
item (`gaussian_angle_weights` n-convergence, T21) and re-scores MY OWN
Iteration-22/23 mandatory `beam_divergence_coherent` cross-check — adjudicated
below on the physics, not on gratitude for finally being run.*

---

## Steel-man (≤150 words)

The audit is right that convergence is undecided, and its two-consecutive-
doubling test is the correct fix for exp-046's own single-jump defect (a
41→401 comparison cannot detect a coincidental near-401 zero-crossing of the
aliasing error). I recomputed the §2.1 sample-per-period table independently
from `A=752`, `CPL`, and `linspace`'s own step formula and it is exact to the
printed digit at all nine (λ,θ₀) pairs, including the ceiling derivation
(n≈709, falling between 641 and 1281). I re-ran `beam_divergence_coherent` at
the cited worst cell (450 nm/36°/FWHM=20°) myself: n=41→81 moves C by 4.34%
(matches exp-046's 4.47% to the expected rounding), then stabilizes to
six digits by n=161 — confirming real, bounded aliasing, not runaway
divergence, and confirming idealization 4's core physical claim that
`beam_divergence_coherent` carries phase information the incoherent
functions discard, making it structurally more exposed to undersampling.

## Sharpest attack (≤150 words)

**§2.2's AND(Δabs≤5e-4, Δrel≤1%) criterion is ill-conditioned exactly where
the incoherent functions live, and I reproduced the failure on unmodified
code.** All nine FWHM=20° `beam_divergence_incoherent` cells sit near a zero
crossing (converged |C|≈5e-5–8e-4, two orders below C_THR); at every one,
Δrel(41→81) is 14.5%–9022% while Δabs is ≤8.7e-4 — a relative-error blowup
from dividing by a near-zero denominator, not physical non-convergence
(values stable to <0.01% by n=161–321 in absolute terms). Under §2.2 as
written this almost certainly reads n\*>41 at 9/9, not the predicted ≤4/9
(central 1–3/9) — tripping P-NCONV26-1b's own hard-falsification clause
("comparable severity to coherent, contradicting the mechanism split") for a
metric-artifact reason, not the real one. Not a one-off: it recurs
identically at the FWHM=10° cell I checked. Idealization 4's "two distinct
mechanisms" needs a third, disclosed one — quadrature-metric ill-
conditioning near C≈0 — or P-NCONV26-1b/2/4 will misattribute a bookkeeping
artifact to physics.

## Verdict

**support-with-changes.**

The instrument-fidelity design is sound and overdue in exactly the way Red
Team's Iteration-25 ranking says: I confirm the priority is real (my own
recompute reproduces exp-046's 4.47% figure and shows it survives past
n=161, not a fluke) and I confirm no expressibility-contract issue — §3
correctly states NO mechanism, and nothing here smuggles a quantum/coherent
*claim* past the classical-parameter boundary; `beam_divergence_coherent` was
already licensed as a mathematical upper-bound device, not a physical model,
at its Iteration-19 birth, and this audit doesn't change that scope. But as
written, §2.2's relative-tolerance term will manufacture spurious "not
converged" verdicts across most of the FWHM=20° incoherent grid, which
threatens to invalidate the mechanism-split prediction (P-NCONV26-1b) this
audit was specifically built to test, and by extension muddies P-NCONV26-2's
ranking-correlation falsifier (cells near a sign crossing will show inflated
Δrel(41) unrelated to the T21-period story, distorting the correlation in
either direction depending on which cells happen to cross zero).

## Flip

Floor Δrel's denominator: **Δrel(n) = 100·|C(2n)−C(n)| / max(|C(2n)|,
C_THR)** (C_THR=0.005, already the program's own decision line — using it as
the floor means relative precision is only demanded once a reading is
close enough to the scored threshold to matter; below that, Δabs≤5e-4 alone,
already an order of magnitude under C_THR, is the physically meaningful
bar). Re-run the 9 FWHM=20° incoherent/incoherent_corrected cells under the
corrected criterion before P-NCONV26-1b/2 are scored — a ~5-line change,
zero new evaluations (same cached series, re-graded). With that fix, this
seat's verdict is unqualified support: nothing else in the design, the
regression gate (P-NCONV26-0, which I independently confirmed reproduces
exp-046's `results.json` figures to the last printed digit), or the
Richardson-doubling ceiling logic shows a defect.

---

## Charter-specific notes (not part of the scored steel-man/attack)

**(b) Does this audit preserve or threaten the Iteration-19/22 "mandatory
cross-check" charter?** Preserves it, and does necessary work no prior cycle
did: the cross-check's entire evidentiary value as an "upper bound" rests on
knowing whether its n=41 reading is near its own converged value — until now
that was simply assumed. This audit is the right instrument to close that
gap, and P-NCONV26-6/8 correctly target the two headline claims
(`36/36 above C_THR`, the restored A4 mechanism) that actually depend on it.
One scope gap worth naming for the record, not a defect in this proposal:
convergence of the *quadrature series* is a different question from whether
`beam_divergence_coherent`'s underlying construction — a fixed ~75λ physical
aperture with an imposed angular power spectrum — is the right physical
model for a naturally divergent single-mode emitter, a question Iteration 22
(exp-046) already answered NO at 9/36 cells (the "deliberately beamformed
synthetic array" finding) and left open at the other 27. A fully converged
`beam_divergence_coherent` is a fully converged reading of that same
beamformed object, not a resolution of that separate, still-open question —
worth one sentence in this cycle's own idealizations so a future reader
doesn't conflate "n-converged" with "physically validated."

**(c) Expressibility contract.** Clean. §3 states NONE and means it — no
σ(I), no σ(x,t), no new material law, no mechanism claim of any kind enters
the bench; this is a pure numerical-quadrature characterization of an
already-committed desk function, reusing `lab.ambient` unmodified. Nothing
to strike.
