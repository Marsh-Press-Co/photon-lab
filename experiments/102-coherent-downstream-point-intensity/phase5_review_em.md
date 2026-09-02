# Phase 5 Review — ELECTROMAGNETISM seat
## Panel Iteration 79 (exp-102), fresh sub-agent, blind, parallel

I am the seat whose Phase-2 critique found the fixed-lab-frame contamination
in the Phase-1 draft's off-axis point, and whose `u(θ)=(-cosθ,sinθ)`
verification the run's Gate C sign-fix now depends on. This review re-derives
everything from source (`lab/fdtd2d.py`, `lab/sections.py`, `run.py`,
`results.json`, `run_output.txt`) rather than trusting NOTES.md's own account
of either outcome — including my own prior Phase-2 finding.

**Verdict: CONFIRM-WITH-GAPS.** The Gate C sign correction is correct — I
re-derived it independently by a Poynting-vector argument, not by re-reading
NOTES.md's derivation, and it agrees with the primary source
(`add_line_source`'s own docstring) and with the recorded numbers to full
float precision. The off-axis point fix is genuinely implemented as a pure
beam-perpendicular offset, verified at the code level and by independent
hand-geometry. Gate B's "honest failure" diagnosis is physically sound in
direction and is corroborated, not merely narrated, by the run's own two
data points — but the specific number it reports is not yet shown to be free
of near-field fringe structure, only consistent with a smooth story. I also
found one small, non-load-bearing numeric restatement defect in Result prose
(R4-lineage), disclosed in full below.

---

## 1. Independent re-derivation of the Gate C sign correction — from scratch

I did not start from NOTES.md's Resolution Note. I started from the physics
and the two governing primary sources, in this order:

**(i) The physical law.** For a locally-plane, lossless TMz wave in vacuum,
the time-averaged Poynting vector is parallel to the wave's propagation
direction: `⟨S⟩ = I₀·û`, where `û` is the unit propagation vector and
`I₀ = |⟨S⟩|` is the (positive, by definition) magnitude. This is not
instrument-specific — it holds for any plane wave, independent of anything
in this codebase.

**(ii) The propagation direction, from the primitive source, not from
NOTES.md.** I read `lab/fdtd2d.py::add_line_source`'s own docstring
directly:

> "The −x-going wave then travels along (−cosθ, +sinθ)..."

confirmed against the surrounding code (the `angle_deg` phase-ramp
construction). This is `add_line_source`'s documented behavior, independent
of exp-102's own text — the same primary source EM's own Phase-2 critique
used last cycle for an unrelated purpose (`P(θ)`'s construction), now reused
for a different one. So for the R4 family (`src_x > obj_x`, confirmed in
`run.py`'s own `downstream_sign()` assertions and in
`design_geometry.py::r4_config()`), `û(θ) = (−cosθ, +sinθ)`, i.e.
`u_x(θ) = −cosθ`.

**(iii) Combine.** `Sx = I₀·u_x(θ) = −I₀·cosθ`, **not** `+I₀·cosθ`. Since
`i_inc` is confirmed directly from `lab/sections.py` to be
`mean_y(−0.5·Re{Ez·conj(Hy)})` — i.e. the raw signed `⟨Sx⟩`, not an unsigned
magnitude — the correct self-consistency identity is
`i_inc ≈ I0_corrected·u_x(θ) = −I0_corrected·cosθ`. The frozen Phase-3
formula's bare `+cosθ` was wrong by a sign, exactly as diagnosed. This
derivation used only (i) a textbook plane-wave identity and (ii) a primary
source-code docstring — it does not depend on, or reuse, NOTES.md's own
Resolution Note 2 argument, though it arrives at the identical conclusion.

**(iv) Numeric check, independently recomputed from `results.json`, not
restated.** Row `C40_R4@37.127246`: `i0_corrected=0.397418...`,
`i_inc=−0.316158...`. Computing `u_x = −cos(37.127246°) = −0.797297`
independently in Python:

```
dev_corrected  = |i0_corrected·u_x   − i_inc| / i0_corrected = 0.17683%
dev_original   = |i0_corrected·cosθ  − i_inc| / i0_corrected = 159.28%
```

Both match `results.json`'s stored `dev`/`dev_original_erroneous_cos_theta`
for this cell to full float precision. I re-ran this same check on the row
with the largest deviation and it also matches to float precision. **The
sign correction is CONFIRMED, independently, by physics and by primary
source, not merely by internal consistency of the write-up.**

This also satisfies R4's addendum in its strongest form: three prior seats
(two Phase-2 critiques, EM and QUANTUM, plus Red Team) verified this
formula's *magnitude* relationship without independently re-deriving its
*sign* (NOTES.md's own Learned item 4 states this candidly) — my check here
re-derives the sign from a source the earlier passes used only for a
different purpose, closing that specific gap for this cycle.

## 2. Off-axis point fix — code-level and geometric confirmation

`run.py`'s `P_off_point()`:

```python
def P_off_point(cfg, theta_deg, standoff, delta_lat, sign=None):
    (px, py), u, v = P_point(cfg, theta_deg, standoff, sign=sign)
    p_off = np.array([px, py], dtype=float) + delta_lat * v
    return (int(round(p_off[0])), int(round(p_off[1])))
```

This is exactly `P_off(θ) = P(θ) + Δ_lat·v(θ)`, with `v(θ)=(sinθ,cosθ)`
already verified orthonormal to `u(θ)` in `_verify_orthonormal()`
(`u·v < 1e-12` at every angle) — the fixed-lab-frame `(0,450)` construction
Phase 1 proposed, and my own Phase-2 critique attacked, is gone; no lab-frame
literal offset survives in the committed code.

I independently hand-computed `P` and `P_off` for `C40_R4@37.127246°`
(`obj_x=340, obj_y=1584, D_STANDOFF=200, Δ_lat=450`) without reading the
code's own arithmetic first:

```
cosθ=0.797297, sinθ=0.603587
P    = (340 − 200·0.797297, 1584 + 200·0.603587) = (180.54, 1704.72) → (181, 1705)
v    = (0.603587, 0.797297)
P_off= (181 + 450·0.603587, 1705 + 450·0.797297) = (452.61, 2063.78) → (453, 2064)
```

Both match `results.json`'s stored `P=[181,1705]`, `P_off=[453,2064]` exactly.
`u·v = (−cosθ)(sinθ)+(sinθ)(cosθ) = 0` by construction — the along-beam
component of `P_off−P` is exactly zero before rounding, so the along-beam
contamination that made the Phase-1 draft's secondary point land 2.4–2.5×
farther downstream than intended (my own Phase-2 finding) cannot recur here
by construction, not merely by disclosure. **CONFIRMED, correctly
implemented.**

`κ_off(θ)` values (1.041–1.077, independently recomputed below in §4) are
consistent with this: a purely lateral offset at 450 cells (≈2.9×`R4_R_OUT`)
samples a region outside the shadow's geometric extent, where mild
constructive redistribution of the diffracted/scattered field (a Fresnel
fringe near the shadow boundary, not a null) is the physically expected
signature — not the "everything got dimmer" failure mode Prediction 3 was
designed to rule out. No along-beam artifact is visible in this range (it is
tight, 1.04–1.08, unlike the order-of-magnitude on-axis spread the near-field
standoff produces at `P(θ)` itself), consistent with 450 cells being far
enough off-axis to sit in comparatively smooth field, not a near-field fringe
zone.

## 3. Gate B "honest failure" — physically sound, but the specific number is not yet fringe-cleared

**Direction: correct, and independently corroborated by the run's own two
data points, not merely narrated.** Fresnel diffraction genuinely fills a
geometric shadow back in with increasing downstream distance — this is
textbook near-field-to-far-field behavior for any finite absorbing/opaque
obstruction, and it predicts exactly the monotonic trend this run shows.
Assembling the three numbers actually in `run_output.txt`, in order of
increasing distance from the object center (`CX=252`, `r_out=78`):

| point | x (cells) | distance/r_out | κ |
|---|---|---|---|
| Gate B corrected point | 352 | 1.28× | 0.163% |
| exp-001 established `BEHIND` window (average) | 357–457 | 1.35×–2.63× | 1.5–1.8% |
| Gate B's original (unrescaled) point | 452 | 2.56× | 5.47% |

This ordering is exactly what "the shadow fills in with distance" predicts:
the near point sits *below* the window's darkest edge, the far point sits
*above* the window's brightest edge, and the window average falls between
both — a self-consistent monotonic sequence spanning the same geometry,
not an isolated number defended only by prose. That is real corroborating
evidence, independently assembled here (this specific three-point ordering
argument does not appear in NOTES.md), not just my agreement with the
diagnosis as written.

**The gap: this is three points, not a swept profile.** The corrected point
(x=352) sits only 5 cells (≈0.06×`r_out`, ≈¼ wavelength at this bench's
`cells_per_lambda=20`) before the established window's near edge (x=357),
yet reads roughly 9–11× darker than the window's own average. VALIDATION.md's
own paid-for lesson is precisely that point-wise near-field readings can be
fringe-limited over scales this small — a genuine, sharp interference null
sitting at x=352 (with the true "smooth" curve passing much closer to the
window's own 1.5–1.8% just a few cells later) is not ruled out by anything
in this run. Two things weigh against that alternative without excluding it:
(a) the ordering above is monotonic with no sign of overshoot/undershoot,
which a narrow destructive null would tend to produce against its
neighbors; (b) the point-vs-region agreement at Gate B's own corrected
point (`κ_point/κ_region ≈ 1.37×`, inside the pre-registered 3× band) shows
the reading is not wildly discordant across an 11-cell block, which a very
narrow (sub-wavelength) null would tend to produce. Neither observation is a
dense standoff sweep, so I rate the mechanism as **plausible and
directionally corroborated, not yet fully characterized** — exactly the gap
NOTES.md's own "Next" item 1 already flags (a properly window-matched Gate
B), and I'd add: a short standoff sweep (4–5 points between x=352 and
x=457) would settle whether the falloff is smooth or fringe-dominated far
more cheaply than redesigning the gate.

No sign of a *different* bug (e.g., a scale or coordinate error): the
rescaling itself is verified correct (`GATEB_D_STANDOFF=100 = 200×(20/40)`,
holding `D_STANDOFF/R4_R_OUT` fixed as documented), and the direction of the
effect (closer → darker, farther → brighter) is the physically required
sign, not the reverse — a genuine coordinate bug would have no particular
reason to reproduce this specific, textbook-consistent monotonic ordering
across three independently-computed points.

## 4. Independent numeric verification — one Result claim recomputed, one defect found

I recomputed `κ(θ)` (region-averaged) directly from `primary_rows` in
`results.json` (`kappa_region = i_region_article / i_region_empty`,
recomputed cell-by-cell, not read off NOTES.md) across all 12
(angle,config) cells:

```
true range:   [3.479968e-3, 7.289772e-3]     (min at C40_R4, θ=41.460901°)
NOTES.md's Result states: "3.68×10⁻³–7.29×10⁻³"
```

**The upper bound matches exactly (7.28977×10⁻³ ≈ 7.29×10⁻³). The lower
bound does not: the true minimum is 3.48×10⁻³, not 3.68×10⁻³** — a ~5.5%
relative error. `run_output.txt` itself prints the true minimum in full
(`C40_R4, θ=41.460901: kappa_region=3.479968e-03`), so this is a genuine
restatement error against the committed log, not a transcription of a
missing number. I checked whether "3.68e-3" is some *other* real quantity
in the row set (e.g., a second-lowest value, a different config's minimum)
— it is: `C40_R4@38.59023` prints `kappa_region=3.681515e-03`, the
second-lowest value overall, suggesting the true minimum was likely
mis-read off a printed table rather than independently computed.

**This is R4-lineage and non-load-bearing**: both the true and the stated
figure are deep inside Prediction 1's `[0,0.10]` band, so no verdict moves.
Flagged per the standing rule (a claimed range in Result prose must be
independently recomputed by any reviewer re-verifying it, which I have now
done) — one isolated instance, does not approach R20's three-defect bar on
its own, and no other Result-section figure I independently rechecked
(`κ_off` range 1.0406–1.0766 vs. stated "1.041–1.077"; point/region ratio
range 1.2301–1.5591 vs. stated "1.23–1.56"; Gate C `dev` range
0.0435%–0.9198% vs. stated "0.04%–0.92%"; Δφ range 0.2092–0.5871 vs. stated
"+0.21 to +0.59"; Gate D `rel_dev` 48.95%/8.24%, exact match) shows a
discrepancy — all five of those reproduce cleanly. Recommend a one-line
Result-prose correction (`3.48×10⁻³` not `3.68×10⁻³`) at the next touch of
this document; not a Checkpoint-4 matter.

## 5. T1 / passivity-reciprocity bookkeeping (charter duty, brief)

T1 route is honestly N/A this cycle: the article is the byte-identical,
unmodified, passive LTI `graded_black_shell` R4 construction — no σ(I),
σ(x,t), gain, or angular-selectivity parameter is touched anywhere in
`run.py`. Both legs of every κ comparison use the same passive medium and
the same source phase convention, so no reciprocity or causality claim is
implicitly smuggled into the coherent ratio (κ is a same-point,
same-launch-phase magnitude-squared ratio; nothing here compares a forward
and a time-reversed or reciprocal path). This bookkeeping is unchanged from
Phase 2's confirmation and remains clean at the executed-code level.

---

## 6. Verdict on the cycle's Combined Verdict candidate

**CONFIRM-WITH-GAPS.**

- The instrument's headline claim ("a genuine, phase-resolved, rotating-frame
  on-axis darkening measurement now exists and is trustworthy") is CONFIRMED
  for the two channels independently validated by gates that can actually
  fail for the right reason: Gate A (trivial identity) and Gate D
  (fault-injection positive control on the novel `P(θ)` construction, which
  I independently re-verified by hand at θ=39.2° for both configs — matches
  to the nearest cell).
- Gate C's sign-corrected self-consistency (Prediction 2) is CONFIRMED by an
  independent from-scratch derivation, not merely re-checked against the
  write-up's own reasoning.
- Gate B's failure is honestly reported and its diagnosis (footprint
  mismatch, not a new bug) is physically sound and corroborated by the
  run's own data — but the specific reading has not yet been shown immune
  to the fringe-scale sensitivity this bench has been burned by before; this
  is a gap in characterization, not a reason to distrust the reported
  number, and NOTES.md itself already states the correct scope limitation
  ("only Gates A and D independently support trusting the primary-channel
  readings this cycle").
- One small, non-load-bearing numeric restatement defect exists in Result
  prose (§4), disclosed above, not previously caught.

None of these gaps changes any scored prediction's verdict; none rises to a
Checkpoint-criterion firing.

## 7. Ranked top-3 candidate directions for Iteration 80

1. **A standoff-swept, footprint-matched Gate B.** Don't just widen the
   sample to match the old window's literal extent (NOTES.md's own Next
   item 1) — first take 4–5 point/region readings between x=352 and x=457
   (zero new FDTD if done on the already-captured Gate B field, since it's
   a single run whose field array covers this whole range) to determine
   whether the near→far transition is smooth (supports the current
   diagnosis outright) or has fringe structure (would mean the specific
   0.163% figure needs a different treatment before Gate B is redesigned
   around it). This closes my own §3 gap directly and is nearly free.
2. **Formally adopt the Learned-item-4 standing rule**: a sign relating two
   vector-valued quantities must be independently re-derived from whatever
   convention already governs that vector elsewhere in the same document,
   not merely magnitude-checked. This is squarely an EM-bookkeeping matter
   (my own §1 re-derivation is a worked instance of exactly this discipline)
   and three independent seats plus Red Team missed the sign in this
   specific case while correctly checking magnitude — worth closing the gap
   as a named rule before it recurs a second time.
3. **Fix the §4 restatement (3.68×10⁻³ → 3.48×10⁻³) at the next touch of
   NOTES.md**, then proceed to the Tier-2 perceptual conversion (constraint
   1's own missing conversion from κ(θ)/I_abs(θ) to a witness-perceived
   `C_thr(L)` judgment) — cheap now, and the natural next step once Gate B's
   footprint question (item 1) is no longer an open trust gap on this
   instrument's on-axis channel.
