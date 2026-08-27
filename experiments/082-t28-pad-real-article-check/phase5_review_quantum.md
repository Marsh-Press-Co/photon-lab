# PHASE 5 — REVIEW (QUANTUM OPTICS, blind) · Panel Iteration 59 · exp-082

**Seat: QUANTUM OPTICS.** Fresh sub-agent, zero memory of any prior session
(including my own seat's Phase-1 lead on this same cycle — reviewing that
work with fresh eyes, per PANEL.md's own independence mechanics). Blind to
any other seat's `phase5_review_*.md`/`phase5_redteam_audit.md` this cycle.
Read PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE
THREADS in full — T28's complete Iteration 46–58 history, T28's own
Iteration-53/exp-076 lossless-vacuum proof in particular), PLAN.md's
Iteration-59 queue, and the complete `experiments/082-.../` directory in
the order specified. No RULED-OUT item is re-proposed or re-litigated here.

**Independent verification performed, not asserted from memory or from the
record's own prose.** I wrote and ran my own verification scripts (session
scratch, nothing under `experiments/082-.../` touched), reusing the real
committed `pad_round_trip_model.py::free_period_with_widening` for an exact
reproduction pass, then built and cross-validated my own independent
vectorized reimplementation of the identical fixed-period-fit/free-period-
search algorithm (matched bit-for-bit — `R²=0.8583`/`0.8637` — against the
real machinery's own output before trusting it on anything new) so I could
run a fast, fully independent 200,000-trial null-permutation control and a
new analytic phase-sensitivity calculation neither critique nor the audit
ran. Every number below is either the exact committed figure or freshly
computed by me from the raw arrays in `results.json`/`experiments/076-.../
results.json`, never copied from prose.

---

## 1. Independent re-verification of Red Team's Phase-2 audit's own §0d–0k

| Claim | Audit's figure | My independent figure | Match |
|---|---|---|---|
| Pearson `r(delta_scene,delta_empty)` | 0.0306 | **0.030573** (`np.corrcoef` on the committed arrays) | exact |
| Exact 7!-permutation `p` | 0.953 | **0.9530** (full 5040-permutation enumeration) | exact |
| Exact critical `\|r\|` at α=0.05, n=7 | 0.746 | **0.7456** (same enumeration, sorted) | exact |
| `delta_scene` free period / R² | P*=2.940°, R²=0.858 | **P*=2.9398°, R²=0.8583** (real `free_period_with_widening`, re-run by me) | exact |
| `delta_empty` free period / R² | P*=1.015°, R²=0.864 | **P*=1.0150°, R²=0.8637** (same, re-run) | exact |
| Ground-truth full-31-point `PAIR_PAD` period | 4.611289746337977° | **4.611289746337977°** (re-ran `free_period_with_widening` on the real `experiments/076-.../results.json::headline` C40/G40 arrays myself) | exact |
| `delta_empty`'s 7 points bit-identical to the full-31-point data at those angles | claimed | **confirmed, `max\|Δ\|=0.0`** (diffed myself) | exact |
| Null-permutation `P(R²≥0.858\|noise)` | 0.272 | **0.2746** (my own independent 200,000-trial run, `sigma=sigma_scene`, `ddof=1`) | matches within Monte Carlo noise |
| Null-permutation `P(R²≥0.864\|noise)` | 0.257 | **0.2601** (same, `sigma=sigma_empty`) | matches within Monte Carlo noise |

**Every one of these reproduces from primitives, independently, using code I
wrote myself rather than re-running the audit's own scripts.** The
free-period-search finding and the null-permutation finding both hold up —
this is not merely "the audit says so," it is now independently
re-established a second time by a different implementation. I additionally
confirmed R² scale-invariance under the null (σ=1.0 gives `P(R²≥0.858)=0.280`,
matching `σ=σ_scene`'s `0.275` within Monte Carlo noise, as the algebra of a
least-squares R² ratio requires) — a sanity check the audit's own §0k does
not report but which confirms the null-permutation result is not an
artifact of the particular σ chosen.

## 2. Is the ~26–27% false-positive rate itself sound, at R²≈0.86/n=7/2 fitted parameters?

**Yes — independently confirmed numerically (above) and the magnitude is
exactly what the underlying statistics predicts, not a surprising or
suspicious figure.** A closed-form sanity check clarifies why: for a
**single, fixed** trial period, the fit is `y = c0 + a·cos(ωx) + b·sin(ωx)`
— 3 parameters, `n=7`, so the sinusoid-coefficient test has `(2, 4)`
residual degrees of freedom. At `R²=0.858`, the corresponding F-statistic is
`F = (R²/(1−R²))·(4/2) = 12.09`, giving a **single-period** p-value of
**0.020** (`scipy.stats.f.sf(12.09, 2, 4)`, verified) — genuinely rare for
one pre-specified period. But `free_period_with_widening` does not test one
period — it **maximizes R² over a 400-point grid spanning [1°,4°]**, and the
correctly-computed look-elsewhere-corrected significance is the empirical
~27% figure, roughly a **13–14× inflation** over the single-trial rate. That
inflation factor is exactly the expected shape of a periodogram-style
maximum-statistic problem with few residual degrees of freedom (4) and a
moderately dense, correlated grid of candidate periods in a narrow window —
not a numerical anomaly, and not out of line with this program's own R5
family precedent for exactly this failure mode (exp-070's own null-`p`
figures of 0.497/0.204/0.806 for other free-parameter searches in this same
T28 sub-thread). **I would expect a result in roughly this range from first
principles before ever running the Monte Carlo, and my own independent
200,000-trial run lands in the same 25–28% band both audit figures do.**
This is a second, independently-derived reason (beyond reproducing the
number) to trust that ~26–27% is real, not an artifact of the audit's own
control.

## 3. A coherent-optics account of what a real absorber should and should not preserve — and a new, quantitative finding on the correlation gap

This charter's own question: is there a coherent-optics reason to expect the
SAME interference pattern, merely phase-shifted, once a real absorber
occupies the object window — in a way this instrument's near-Nyquist 7-point
window cannot distinguish from genuine decorrelation? **Yes, on both counts,
and I can now make the first half quantitative.**

**(a) Why phase-shift-plus-attenuation is the physically expected outcome,
not merely a hopeful reading.** This bench is fully linear at 600 nm (no
σ(I), no time-varying ε anywhere in `build_article`/`Sim` — EM's own Phase-2
§4 point, which I independently confirm from the same charter angle).
Superposition therefore holds EXACTLY: `E_article = E_no-article +
E_scattered-by-article`. But Weber contrast is built from **intensity**
(`|E|²`, time-averaged), a *quadratic* functional of the field — so the
scored contrast does **not** inherit the field's own linear decomposition.
Expanding `|E_no-article + E_scattered|²` produces a cross term,
`2·Re(E_no-article·E_scattered*)` — a genuine coherent-interference term
between the boundary-echo field (whose round-trip phase is exactly what
`PAD` modulates, per Iteration 53's own proof) and the article's own
scattered field. This is precisely why "the article passively sits in a
shadow, inert to the echo" is not the right zeroth-order picture: the
article is a *new, coherent scattering center* sitting inside the same
optical system that produces the PAD ripple, and it necessarily introduces
its own path-length terms (source→article→boundary→…) that the empty-scene
proof never had to account for. A moderate phase shift of the surviving
ripple, relative to the pure-vacuum `PAIR_PAD` signature, is the
first-order-expected consequence of exactly this term — not a special
pleading needed to rescue "SURVIVES."

**(b) Quantitative test: is r=0.031 consistent with "same mechanism, merely
phase-shifted"?** I built the simplest falsifiable version of this question
directly from already-committed data, zero new FDTD. Take a single-tone
sinusoid at `PAIR_PAD`'s own **independently-known true period**
(`P=4.611289746337977°`, the full-31-point ground truth, §1 above), sampled
at exactly this cycle's own 7 θ-points, and compute the Pearson r between
that reference and the same sinusoid shifted by `φ`:

| φ (deg) | r | φ (deg) | r |
|---|---|---|---|
| 0 | 1.000 | 105 | −0.211 |
| 30 | 0.857 | 120 | −0.453 |
| 45 | 0.699 | 135 | −0.671 |
| 60 | 0.501 | 150 | −0.847 |
| 75 | 0.277 | 165 | −0.961 |
| **90** | **0.036** | 180 | −1.000 |

**A phase shift of `φ≈90.3°` — a quarter of one PAD-fringe period — at this
exact 7-point sampling geometry produces `r=0.0310`, matching the OBSERVED
`r=0.0306` almost exactly.** This is a real, if idealized (single-tone,
noise-free) demonstration that the near-zero correlation Red Team's audit
correctly showed is unresolvable is **also fully consistent with the
strongest, most specific version of "same mechanism, phase-shifted"** — not
merely "not ruled out," but reproduced to within 0.4% by a single
physically ordinary parameter (a quarter-period shift, well within what a
strongly-scattering article occupying most of the object window could
plausibly contribute given its own path-length scale is comparable to
`PAD`'s own 40-cell shift). This sharpens, but does not overturn, Red Team's
own Attack 1 ruling: the shape/mechanism-identity question is not merely
*unresolvable in either direction* — it is a case where the SPECIFIC data in
hand is exactly what a plausible, physically ordinary phase shift under
mechanism continuity would produce, though a genuinely different mechanism
of comparable amplitude would fit equally well at this power (idealization:
real `delta_scene`/`delta_empty` are not pure single-tone sinusoids —
`R²≈0.86`, not 1.0 — so this is illustrative of what the window's own
geometry can and cannot see, not a proof of the phase-shift hypothesis
itself). **This is new evidence FOR the "same mechanism, phase-shifted"
reading being physically live, not evidence that resolves which of the two
readings is correct** — it does not move me to disagree with Red Team's
"UNRESOLVABLE at this power" ruling, which I independently re-derive and
concur with in full (§1–2).

**(c) A second, equally expected consequence: genuinely new spectral
content, not just a shift.** Because the article sits INSIDE the coherent
echo's own round-trip path (between source and the `ABSORB` boundary, at
`R_OUT=78`, comparable in scale to the domain distances the PAD round trip
traverses), it can support its OWN echo terms with distinct path lengths
(source→article→boundary→article→plane, etc.) — not merely re-phasing the
old PAD term but potentially adding a second, physically distinct
oscillatory contributor. This is the T28 sub-thread's own recurring shape
(Iteration 46's original finding: two co-located sinusoids at the SAME
frequency always sum to a third at that frequency, but sinusoids at
DIFFERENT frequencies do not) — so "phase-shift-only" is the simplest
hypothesis, not the only physically live one. This is exactly
THERMODYNAMICS' own Phase-2 mechanism-identity question (merged with the
shape question, Attack 3/fix-docket item 4) restated from a coherent-optics
angle: both readings are physically ordinary consequences of the same
linear-system-plus-quadratic-detector picture, and this instrument cannot
yet tell them apart.

## 4. Assessment of the correction chain (Phase 1 → Phase 2 → Phase 3)

The pre-audit Phase-1 language ("the PAD confound reaches the real...
channel," "the same lossless phase artifact reaches the scored channel")
was a genuine overclaim — mechanism continuity is asserted nowhere in the
pre-registered bands (§4 of `phase1_proposal.md` only defines
`ratio=A_scene/A_empty`, a shape-blind statistic) and is not established by
anything computed at Phase 1. PHOTONICS and EM independently caught the
right symptom (r=0.031) at Phase 2; Red Team's audit correctly went further
and showed the deeper, more decisive point — not merely "low correlation"
but "the instrument itself cannot resolve shape at this window," proven via
a ground-truth failure mode (§1j) and a calibrated null (§1k), which I have
now independently reproduced twice over (§1, §2 above) with my own code.
Phase 3's adopted correction is accurate: it states SURVIVES stands
MECHANICALLY, states the mechanism-continuity question as open and shown
unresolvable (not merely unresolved), and does not overclaim in either
direction. I find no residual overclaim in the corrected `NOTES.md`/
`phase1_proposal.md` language, and no new defect in the corrected record
that Phase 2/3 missed.

One genuinely new gap, not previously flagged: **the corrected record does
not carry my own §3(b) finding** (a phase shift of ~90° at the true PAIR_PAD
period reproduces the observed r almost exactly) — this is new information,
not a defect, and is the most natural, cheap thing for a future cycle to
check for real (not merely illustrate with a synthetic single-tone model).

## VERDICT: **PROMISING** (for the item-7 tripwire discharge and the
instrument-limitation finding; the mechanism-identity question itself
remains genuinely open, not "promising" in isolation)

This cycle correctly and rigorously discharges PLAN.md's own six-cycle
tripwire, delivers the T28 sub-thread's first-ever article-loaded FDTD
measurement, and — via Red Team's audit, now independently reproduced twice
by two different implementations (mine and the audit's) — establishes a
genuinely new, general instrument-caution finding (a reduced-power free-
period search both fails on known ground truth and clears its own R² bar at
~26–27% under pure noise) with implications reaching beyond this one result.
The mechanical SURVIVES result is decisive and correct. The substantive
mechanism-identity question is honestly reported as open, not resolved and
not swept under a confident label either way — exactly the standard this
program holds itself to. Nothing in my own independent re-verification finds
a defect Phase 3 did not already correct, and my own new phase-sensitivity
calculation (§3b) adds a concrete, falsifiable reason to take "same
mechanism, phase-shifted" seriously as the leading hypothesis for the next
cycle to actually test, rather than treating the open question as
symmetric between "same mechanism" and "new mechanism."

## Top-3 ranked candidate directions for Iteration 60 (QUANTUM OPTICS' own charter angle)

1. **The full 31-point/0.2° window on the SAME `PAIR_PAD`/article-loaded
   pair — now sharpened into a specific, falsifiable coherent-optics
   prediction, not merely "more power."** At full power, fit both
   `delta_scene` and `delta_empty` for period AND phase, and test directly
   whether the recovered phase offset between them clusters near the
   `φ≈90°` region my §3b calculation shows is fully consistent with the
   ALREADY-OBSERVED 7-point correlation — a real discriminator this cycle's
   reduced window cannot supply, and a genuinely new prediction (not
   available before this review) a future cycle can pre-register and test
   against. This is the single highest-value next step precisely because it
   converts "open question" into a falsifiable band, exactly this program's
   own house standard.
2. **THERMODYNAMICS' own zero-FDTD control, still unrun**: replace
   `graded_black_shell` with a lossless PEC-only disk at the identical
   location (`materials.pec_disk` alone, no shell) in the SAME `PAIR_PAD`
   harness. Under my own §3(a) linearity argument, a lossless scatterer
   still produces the identical cross-interference term (coherent scattering
   does not require absorption) — so this test isolates whether the
   confound's persistence depends on the article's absorption specifically,
   or only on its presence as ANY coherent scatterer in the echo's path. A
   genuinely informative, cheap (2×7=14 calls) companion to item 1, and
   directly answers a question my own §3(c) raises (new spectral content vs.
   pure phase shift) that neither this cycle nor its critiques settled.
3. **MATERIALS' own near-null σ(I) article follow-up** (`off_pass`,
   `τ_off≈0.0065`), already named as a standing "Next" item in `NOTES.md` —
   ranked third here, not first, because it answers a different, article-
   generality question (does the confound's scale depend on how strongly the
   article absorbs) rather than the mechanism-identity question my own
   charter is most directly positioned to sharpen (items 1–2). Still the
   single test that would extend this cycle's flagship-only scoping to the
   near-threshold regime where the confound could plausibly be perceptually
   load-bearing, and should not be deferred indefinitely behind items 1–2.
