# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 64 · exp-087

Charter: non-classical absorption, state-dependent/coherent interactions;
expressibility contract N/A this cycle (Checkpoint criterion 2 is correctly
N/A — no mechanism claim). This review instead applies this seat's
established strength on this sub-thread (statistical/instrument-reliability
findings, R5/R6/R10 lineage, and my own Iteration-64 Phase-2 critique on
this exact cycle) to the §4-P7 classification scheme's own soundness.

## 0. Independent reproduction (before anything else, per this program's
own R4/R9 discipline — nothing below is taken from NOTES.md's own prose)

Recomputed directly from `results.json` and `experiments/083-.../
results.json` (never from NOTES.md's citations of them):

- `ratio_k(36.0)=frac_p_abs/frac_contrast=0.0019654670183146365/
  0.0007438279588304384=2.6424` — matches the filed `2.6423677612294223`.
- `ratio_k(38.6)=0.004000574149370313/7.410062757210442e-05=54.00`
  — matches the filed `53.988397675546146`.
- `ratio_k(41.8)=0.007214161936040001/0.0012633809286846705=5.7107`
  — matches the filed `5.710203290428644`.
- **"Even discounting 38.6°, the remaining two angles are CONSISTENT not
  DECOUPLED" — CONFIRMED independently.** `ratio_k(36.0)=2.64` and
  `ratio_k(41.8)=5.71` both sit inside `[0.1,10]`; excluding 38.6°
  (`n_resolved=2`, `resolved_ratios=[2.64,5.71]`) the pipeline's own
  `classify_resolved()` returns `CONSISTENT`, not `ENERGY-DECOUPLED` — I ran
  this by hand against the committed classification logic in `run.py`
  (`_label`/`classify_resolved`), not merely by re-reading NOTES.md's prose.
  **This holds regardless of anything below**: the pre-registered
  ENERGY-DECOUPLED prediction is cleanly falsified by the two
  non-controversial angles alone. That finding is robust and should not be
  read as contingent on the 38.6° dispute.

The open question is only whether the *overall* classification should be
`ENERGY-DOMINANT` (which requires trusting the 38.6° reading) or whether
that reading is a construction artifact, leaving `CONSISTENT` as the
better-supported label.

## 1. Independent confirmation, from source, of the near-node mechanism
NOTES.md discloses but does not resolve

Pulled `experiments/083-.../results.json::per_theta` directly (not via
NOTES.md's citation) for the dense-grid neighbors of 38.6°:

| θ | `delta_scene(θ)` | `C40_C(θ)` |
|---|---|---|
| 38.0° | +1.9231×10⁻³ | −0.56440 |
| 38.2° | +1.5151×10⁻³ | −0.56389 |
| 38.4° | +8.083×10⁻⁴ | −0.56250 |
| **38.6°** | **−4.151×10⁻⁵** | −0.56023 |
| 38.8° | −8.569×10⁻⁴ | −0.55731 |
| 39.0° | −1.4845×10⁻³ | −0.55413 |

`C40_C(θ)` (the denominator of `frac_contrast`) is smooth and nowhere near
zero anywhere in this window (−0.560 to −0.564) — confirming NOTES.md's own
claim that only `delta_scene`'s **numerator** is anomalous, not
`frac_contrast`'s own denominator. Linear-interpolating the zero-crossing
between 38.4° and 38.6° (slope ≈ −4.25×10⁻³/°, consistent with the
38.6°→38.8° slope of ≈ −4.08×10⁻³/°, i.e. genuinely smooth, not noisy):

θ₀ ≈ 38.4 + (8.083×10⁻⁴)/(8.083×10⁻⁴+4.151×10⁻⁵) × 0.2 ≈ **38.590°**

The sampled point, 38.6°, sits **≈0.01° from the true zero-crossing** —
this is not "near" a node in a loose sense, it is essentially on top of
one. `θ=38.6°` was not picked to dodge this: it is `dg069.DENSE_ANGLES[13]`,
an existing exp-083 dense-grid point chosen for `frac_contrast`'s
independence from the **aliasing lattice** (Phase-2 mandatory fix 2) — a
different property entirely, discussed in §3.

**Corroborating evidence the numerator side (`frac_p_abs`) has no
matching anomaly**: `frac_p_abs(36.0,38.6,41.8) =
(1.965,4.001,7.214)×10⁻³` — smooth, monotonically increasing, roughly
geometric growth (successive ratios 2.04×, 1.80×) with no discontinuity,
kink, or sign change anywhere near 38.6°. If a real energy-domain
phenomenon were switching on specifically at 38.6°, the natural
expectation is *some* signature in `frac_p_abs` itself, independent of
`frac_contrast`; there is none. The anomaly lives entirely on the
denominator side, and specifically at the one operand (`delta_scene`)
independently established (exp-083, `p=0.0` against a 20,000-trial null)
to be a genuine, smooth, periodic curve with real zero-crossings roughly
every half-period (≈1.42–1.47° for `P_edge_A`/`P*`).

## 2. Is `ratio_k` a sound quantity to build a decade classifier on?

**No, not as specified — this is a structural defect in the classification
scheme itself, not merely bad luck at one angle.**

`ratio_k(θ) = frac_p_abs(θ) / frac_contrast(θ)`, and
`frac_contrast(θ) = |delta_scene(θ)| / |C40_C(θ)|`. `delta_scene(θ)` is
cited (never re-derived by this cycle) as a smooth, established, real
oscillatory curve. **Any smooth oscillating function has zero-crossings by
definition, and near a zero-crossing, `|delta_scene(θ)|→0` continuously and
without bound in derivative-normalized terms** — meaning `frac_contrast(θ)`
can be driven arbitrarily small purely by the choice of θ, with zero
dependence on whether the article's absorbed power is actually
θ-anomalous. For **any** nonzero, smooth `frac_p_abs(θ)` (which is exactly
what this cycle measured), `ratio_k(θ)→∞` as θ approaches such a
crossing — this is a property of the ratio's own algebra, not a
measurement of physics. The `ENERGY-DOMINANT` tier (`ratio_k>10` at *any*
resolved angle, with veto priority over the other three labels per §4's
own stated rule) is therefore **not falsifiable against this specific
alternative at any single sampled angle that happens to land near a
`delta_scene` node** — a real, near-zero `frac_p_abs` would read the same
as a real, comparably-sized `frac_p_abs` divided by a coincidentally
vanishing denominator. Nothing in the pipeline distinguishes the two.

Quantified: the local slope of `delta_scene` near 38.6° is ≈−4.2×10⁻³ per
degree. Solving for the θ-width over which `ratio_k` swings by an order of
magnitude around this node (holding `frac_p_abs≈4×10⁻³` and
`|C40_C|≈0.56` fixed, both true locally): `ratio_k` crosses the decade
boundary (`=10`) at `|delta_scene|=frac_p_abs×|C40_C|/10≈2.24×10⁻⁴`,
reached at `|θ−θ₀|≈2.24×10⁻⁴/4.2×10⁻³≈0.053°` — **a quarter of one grid
step**. `ratio_k` is not merely "sensitive" near a node; its label flips
within a fraction of the sampling resolution itself. This is the textbook
signature the task names: a small-denominator instability, here shown
quantitatively, not just qualitatively.

## 3. Did breaking the aliasing lattice (fix 2) walk onto this DIFFERENT
artifact — and is that a new finding, distinct from my own prior critique?

**Yes to both, confirmed.** Two genuinely orthogonal properties of an
angle grid were in play, and only one was checked:

- **Aliasing (PHOTONICS' Phase-2 attack, adopted as fix 2)**: whether the
  *spacing between* sampled angles sits near an integer multiple of a
  known confound period — a **systematic, global** property of the whole
  grid, which biases every sample toward the same relative phase.
- **Node-coincidence (this finding)**: whether an *individual sampled
  angle* happens to sit near a zero-crossing of `delta_scene(θ)`
  specifically — a **local, per-point** property, orthogonal to grid
  spacing. A grid with perfectly non-resonant spacing can still place any
  one of its points arbitrarily close to a node; fixing the gap-vs-period
  relationship does nothing to check individual points against the curve's
  own zeros.

Phase 3's fix-2 diligence (checking `{36.0°,38.6°,41.8°}`'s gaps against
`P_edge_A`/`P_star` — logged in `results.json::aliasing_risk_log`, 8.5–12.6%
from resonance) was real and correctly executed for the property it was
designed to catch. It was never extended to a **zero-FDTD check that would
have caught this**: `delta_scene(θ)`'s own zero-crossings were already
sitting, fully computed, in exp-083's committed `results.json` at Phase-1/
Phase-3 desk-check time — a check of the exact form "does any candidate
angle land within (say) half a grid step of a `delta_scene` zero-crossing"
was affordable, cited-data-only, and not run. This is the same shape this
program's own R8 exists for (an affordable, already-nameable check on a
flagged quantity, not run before a headline verdict is trusted) — though
I do **not** find it fires here: NOTES.md's own Result section disclosed
the coincidence honestly, unprompted, before any Phase-5 review saw it,
which is the R8/Checkpoint-4 "caught before it is defended" exemption this
program applies consistently (Iterations 51/53/55/58's own non-firing
precedent). I record it as a genuine, previously-uncharacterized gap in
the classification scheme's own design discipline, not a violation.

**This is a genuinely new failure mode, not a re-litigation of my own
Iteration-64 Phase-2 critique.** That critique (vacuous classification at
0/1 resolved angles, adopted as the `DEGENERATE` carve-out) is about the
classifier's behavior when **too little data resolves** — an empty-set
quantifier problem, now closed. This finding is about the classifier's
behavior when a fully-resolved, well-powered, noise-floor-clearing angle
(38.6° clears the noise-floor gate comfortably — this is *not* what
`DEGENERATE` or the noise-floor gate exists to catch) still produces a
mathematically-inevitable extreme value because of what the *reference*
curve does, independent of noise or resolution. The existing
noise-floor gate protects only the numerator side (`p_abs_w`'s own
`box_dev`-scaled uncertainty); nothing protects the denominator side
(`frac_contrast`, hence `C40_C`/`delta_scene`) from a real, low-noise,
but geometrically-coincidental near-zero value. These are different
statistics, different failure conditions, and different fixes.

## 4. A cheap, falsifiable way to distinguish "real physics" from
"near-node ratio blowup" — the decisive test not yet run

The single sharpest available discriminator: **the immediately-adjacent
`DENSE_ANGLES` grid points, 38.4° and 38.8°, both already have
`delta_scene`/`C40_C` fully characterized in exp-083's committed data**
(§1 table). Interpolating `frac_p_abs`'s own smooth local trend
(≈4.0×10⁻³ at 38.6°, per §1) onto these neighbors and computing what
`ratio_k` WOULD read there:

- `ratio_k(38.4°) ≈ 4.0×10⁻³ / (8.083×10⁻⁴/0.5625) ≈ 4.0×10⁻³/1.437×10⁻³
  ≈ 2.8` — **CONSISTENT**.
- `ratio_k(38.8°) ≈ 4.0×10⁻³ / (8.569×10⁻⁴/0.5573) ≈ 4.0×10⁻³/1.538×10⁻³
  ≈ 2.6` — **CONSISTENT**.

Both immediate neighbors, using only cited `delta_scene`/`C40_C` data and
a smooth interpolation of the already-measured `frac_p_abs` trend, land
squarely in `CONSISTENT`, an order of magnitude away from
`ENERGY-DOMINANT`. **This is strongly suggestive, not proof** — it uses an
interpolated, not measured, `frac_p_abs` at those two angles — but it is
exactly the pattern a near-node artifact predicts (a narrow, isolated spike
at the node, flat everywhere around it) and exactly the opposite of what a
genuine energy-domain phenomenon turning on near 38.6° would predict (some
persistence in neighboring angles).

**The decisive, falsifiable follow-up** (cheap, disclosed explicitly as
not yet run): 8 new FDTD calls (C40/G40 × {empty,article} at 38.4° and
38.8°, STEPS=2800) to measure real `frac_p_abs` at both neighbors and
compute real (not interpolated) `ratio_k` there. **Falsification
criterion, stated in advance for whoever runs this**: if both real
neighbor `ratio_k` values land in `[0.1,10]` while 38.6° remains far
outside it, that is decisive confirmation of the near-node-artifact
reading (real physics does not explain a discontinuity narrower than the
sampling grid). If either neighbor also reads `ENERGY-DOMINANT`, or if
`frac_p_abs` itself shows a discontinuity at 38.6°, the artifact
explanation is refuted and a genuine, sharply localized energy phenomenon
becomes the leading hypothesis — which would itself be a major, previously
unseen result on this ten-plus-cycle sub-thread and would warrant
immediate, well-resourced follow-up.

**A general, reusable fix for future cycles of this exact instrument**:
add a floor gate directly on the denominator side, symmetric to the
existing noise-floor gate on the numerator side — e.g. require
`|delta_scene(θ)|` to exceed some stated fraction (a house-style
convention, same epistemic status as the existing 3×`box_dev` and
0.1/10 decade choices — disclosed as such, not derived) of the confound
curve's own local peak-to-peak amplitude (computable zero-FDTD from the
already-committed dense sweep) before that angle is treated as
"resolved" for `frac_contrast`'s own denominator-stability purposes,
distinct from and in addition to the existing `p_abs_w` noise-floor gate.
An angle failing this new gate would report a sixth outcome —
`NODE-UNRESOLVABLE` or similar — rather than being silently classified.

## 5. Candidate standing rule (recommend to Red Team/Director; numbering
deferred to whoever adopts it — the next open slot after R12)

**A ratio statistic whose denominator is constructed from a quantity
independently known (or knowable, zero-FDTD, from already-committed data)
to have real zero-crossings must be floor-gated on that quantity's own
absolute or amplitude-normalized size — not merely on the numerator's own
measurement noise — before a decade/threshold classification built on it
is trusted at any single angle or point.** This is a distinct instance
from R5 (a phase-offset regressor's own periodicity assumption) and R10
(order-preserving null-under-noise for a free-period/free-phase fit): R5/
R10 concern whether a *fitted period or phase* is statistically
distinguishable from noise; this concerns whether a *pointwise ratio*
between two independently-sourced curves is well-defined at all near a
point where one curve is known to pass through zero — a problem that
exists even with zero measurement noise, given only that the reference
curve is genuinely oscillatory. Both R5 and R10 are about noise; this is
about algebra.

## 6. Verdict

**Support-with-changes on the Combined Verdict as currently stated.** The
cycle's own execution (P1–P6, P8, the non-negativity fix, the direction-
correction — all independently re-checked here and found sound) is high
quality and the ENERGY-DECOUPLED prediction is genuinely, robustly
falsified by the two non-38.6° angles alone regardless of anything in this
review. But **I do not support carrying "ENERGY-DOMINANT" forward as the
cycle's confident classification** without the §4 follow-up: the specific
mechanism driving it is shown here, quantitatively, to be a small-
denominator instability in a ratio construction that this program's own
established statistical discipline (R5/R10's shared "demonstrate a
threshold classifier's own discriminating power before trusting it"
principle) would not license as-is. The better-supported reading, pending
the 8-call follow-up, is: **`CONSISTENT` at two well-resolved angles, and
`UNRESOLVED-BY-CONSTRUCTION` (not genuinely `ENERGY-DOMINANT`) at 38.6°** —
a real, materially different Combined Verdict than the one currently filed,
though I stop short of asserting REFUTE on the DOMINANT label outright
since the decisive test has not been run.

## 7. Ranked candidate directions for Iteration 65

1. **Run the 8-call bracketing follow-up (§4)** — cheap, decisive,
   directly falsifiable in either direction, the single highest-value next
   step specifically raised by this cycle's own result.
2. **Add the denominator floor-gate (§4, general fix) to the classification
   scheme** and re-classify this cycle's own already-collected data under
   it, zero new FDTD — a permanent instrument improvement independent of
   how item 1 resolves.
3. **Adopt the candidate standing rule (§5)**, closing a genuinely new
   failure shape in the R5/R10 lineage before it recurs — T28's own
   confound machinery is full of ratio constructions (`amp_ratio`,
   `frac_contrast`, `ratio_k` itself), and a bounded audit of whether any
   OTHER cited ratio in this sub-thread's history divides by a quantity
   with known zero-crossings, unguarded, would be cheap and in the spirit
   of R11's own bounded historical scan.
4. **Widen this exact instrument's angle count beyond 3** for any future
   run (5+ points, chosen to include at least one bracketing pair around
   any angle close to a known `delta_scene`/`C_empty` zero-crossing) —
   a design-level fix that makes node-coincidence self-diagnosing rather
   than silent, the direct generalization of item 1's one-off bracket.
5. **Carry forward, unresolved by this review**: the still-standing
   `xi_ext`/oblique-`graded_black_shell` instrument-validity question (EM's
   Phase-2 fix, PASSED cleanly this cycle but only at n=1 configuration
   family) and the near-null σ(I) article follow-up — both real, both
   pre-existing T28 board items, neither displaced by this finding.
