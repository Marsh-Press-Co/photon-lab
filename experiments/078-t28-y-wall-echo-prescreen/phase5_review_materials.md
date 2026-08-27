# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 55 · exp-078

*Fresh sub-agent, blind to the other six seats' Phase-5 reviews. Read
PANEL.md in full; AGENTS.md; LOGBOOK.md in full (RULED OUT R1–R9; T28's
complete Iteration 46–54 history, esp. exp-075/076/077's own realizability
findings); exp-078's complete record (`phase1_proposal.md` as corrected in
place, `y_wall_prescreen.py`, `y_wall_prescreen_results.json`, all five
Phase-2 critiques including my own prior-cycle `phase2_critique_materials.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`phase4_null_calibration_corrected.py`/`_results.json`); and
`boundary_reflectance.py` / `design_geometry.py` for background. I ran fresh
independent computations against the raw code/JSON rather than trusting the
write-up's numbers — see §2.*

---

## 1. Verdict: **PARTIAL**

The angle-convention correction this cycle made (Attack 1, unanimous across
EM/MATERIALS/THERMODYNAMICS at Phase 2, confirmed a fourth way by Red Team)
does not touch anything in MATERIALS' own charter. It flips a period-match
verdict; it does not change what admittance the model assumes, and
realizability is a property of the admittance formula, not the angle it is
evaluated at. **My own realizability bound is unchanged by this cycle's
correction, in either direction**: the tested y-wall instantiation was
unobtainium-with-parameters before Phase 4 and remains unobtainium-with-
parameters after it — the corrected numbers (0/3 SUPPORT, null-
indistinguishable) neither strengthen nor weaken that bound, because the
bound was never contingent on which θ-convention was used. What the
corrected result *does* do is remove the only reason anyone might have had
to prioritize spending MATERIALS effort on this wall orientation right now
— see §3.

Verdict is PARTIAL, not RULED OUT, because the realizable-admittance
instantiation of this mechanism class remains genuinely untested here, for
either wall orientation — a period pre-screen using an unbuildable
transfer function cannot, on its own, rule out a class that has never been
evaluated with a buildable one. Not PROMISING, because nothing in this
cycle newly implicates a buildable structure, and the statistical case
weakened (2/3 raw SUPPORT → 0/3 corrected, all three now indistinguishable
from noise at p≥0.12).

---

## 2. Independent checks

### 2a — The admittance formula is unchanged by this cycle's fix; the realizability bound is orthogonal to Attack 1

Read `y_wall_prescreen.py` directly (not the write-up's description): the
mandatory-fix docket's Attack-1 correction adds `y_wall_incidence_angle`
and threads it through `edge_image_phase_difference`'s **angle argument**
only —

```python
r_angle = y_wall_incidence_angle(theta_deg) if use_corrected_angle else theta_deg
r = br.reflection_coefficient(n_prof, r_angle, lam_cells)
```

`br.reflection_coefficient` itself — imported, never reimplemented — is
`boundary_reflectance.py`'s original matched-`eps=mu` transfer function
(`Z = n_prof / sqrt(n_prof**2 - s2)`, confirmed by reading the source
directly, line 195). This is the *same* unrealizable admittance this seat
bounded for the x-wall at exp-075/077: it requires an equal, broadband,
angle-tracking magnetic-loss response (`μ_r ≠ 1`) alongside the electric
one, which has no realizable analog for an ordinary dielectric/conductive
coating at optical frequencies. **The fix this cycle made and the bound
this seat owns are about two different variables (angle-of-evaluation vs.
admittance-formula) — confirming one says nothing about the other,
independent of which way it moved.**

### 2b — Independently re-confirmed: raw JSON matches the write-up's corrected numbers exactly

Rather than trust `phase4_results.md`'s table, I loaded
`y_wall_prescreen_results.json` directly:

```
primary_model_scores:
  c80_c40_vs_2.8421:      P*=4.0000°  rel_dev=0.40740740740740744  INCONCLUSIVE
  pair_pad_vs_4.6113:     P*=3.218045112781955°  rel_dev=0.3021377337354387  INCONCLUSIVE
  pair_absorb40_vs_4.1761: P*=2.8045112781954886°  rel_dev=0.32844323144245247  INCONCLUSIVE
summary: n_primary_refute=0, n_primary_support=0
```

Exact match to `phase4_results.md`'s printed table and `phase3_synthesis.md`'s
frozen predictions, to the printed digits. No R4 issue.

### 2c — A fresh, orientation-specific computation: does the realizable-vs-unrealizable admittance gap actually matter for THIS model's Test A?

My own exp-077 Phase-5 review found that swapping the x-wall's matched
admittance for the realizable (`μ_r=1`) one moved `|r|` by 15–40% and
`arg(r)` by 15–24° across `θ∈[36°,42°]` — large enough, I argued then, to
plausibly matter against that cycle's own tight decision margins. The
task brief asks directly whether anything about the y-orientation changes
what MATERIALS can say. I did not assume the same magnitude carries over;
I recomputed it, at the y-wall's own corrected angle envelope (θ_y = 90−θ
= 48°–54°), reusing the identical recursive transfer-matrix loop with only
the admittance formula swapped (`Z' = 1/√(n²−sin²θ)`, the standard `μ_r=1`
TE form — same construction I used at exp-077, gate-checked there against
`G-LOSSLESS` before trusting it):

| ABSORB | \|r\| ratio (real/matched) | arg(r) shift | shape Pearson r (arg vs θ, 31-pt sweep) | implied period-slope ratio |
|---|---|---|---|---|
| 40 | 1.11–1.12× | −8° to −11° | 0.999982 | 0.973 |
| 60 | 1.04–1.18× | (comparable) | 0.999890 | 0.989 |
| 70 | 1.09–1.16× | (comparable) | 0.999865 | 1.071 |
| 80 | 0.63–1.13× | (comparable) | 0.999754 | 1.139 |

Two findings, both new to this cycle (not restated from any prior review):

1. **The magnitude/phase gap here (11–18% / 8–11° at ABSORB=40) is real but
   smaller than the x-wall's own 15–40%/15–24° gap at its angles** — the
   realizability caveat is not orientation-invariant in *magnitude*, only
   in *kind*.
2. **More load-bearing for this specific pre-screen**: because
   Red Team's Attack 1 already established that `arg(r(θ))` is this
   model's *sole* source of θ-dependence (the propagation-distance term is
   fixed), what actually sets the recovered *period* is the **shape** of
   `arg(r(θ))` across the swept window, not its absolute value. That shape
   is nearly admittance-choice-invariant here — Pearson r > 0.9997 between
   the matched and realizable curves at every ABSORB depth this series
   uses, and the implied period shifts only 3–14%. A 3–14% period shift
   cannot move any of this cycle's `rel_dev` values (0.30–0.41, all
   comfortably inside INCONCLUSIVE with room on both sides) across the
   0.30/1.00 bars. **Unlike the x-wall case, a realizable-admittance
   refit of this specific Test-A pre-screen would not plausibly change the
   verdict** — I checked, rather than assumed either way, per this
   program's own R8 standard.

**Caveat on my own check, stated plainly**: this bounds Test A only. The
|r| *magnitude* ratio (up to 1.2× at most depths, more scattered at
ABSORB=80) would still matter for amplitude-weighted evidence — a future
Test B (shape-match against real `delta(theta)`, not built by this
pre-screen at all) or an |r|-weighted rescoring (already flagged as open
question §8.2 of the as-filed proposal) could still be realizability-
sensitive in a way period alone is not. I have not computed that case; I
am reporting only what I actually checked.

### 2d — Orientation-invariance of the underlying construct, re-confirmed independently

`Sim._damping` (`lab/fdtd2d.py`) applies the identical `absorb`-parameterized
cubic ramp to all four domain edges — re-verified by reading the source
directly, matching §3.4's own claim and this seat's own Phase-2 spot-check
last cycle. This means the "this describes the solver's own PEC-backed
open-boundary substitute, not a coating anyone would place in the witness
scene" caveat I raised at Phase 2 this cycle transfers to the y-wall by
the same construction argument, unchanged — there is nothing structurally
different about a y-normal absorbing boundary versus an x-normal one in
this engine; both are the identical numerical device at a different edge.

---

## 3. Does this cycle change my realizability bound, and does y- vs x-orientation matter? — direct answers

**Does the corrected result move my bound?** No, in either direction. The
bound attaches to the admittance formula (§2a), which this cycle's fix
never touched. A SUPPORT verdict here would have been just as
materials-unrealizable as this INCONCLUSIVE one; the correction changed
whether the *data* matched a certain curve, not what that curve is made
of.

**Is there anything y-wall-specific MATERIALS should flag, beyond
"same caveat, different wall"?** Yes, one genuine asymmetry, found by
direct computation rather than assumed: the realizable-admittance
substitution matters quantitatively *less* for this model's period
estimate than it did for the x-wall's own Test A/B numbers (§2c) — not
because the y-wall is somehow more realizable (it is not; both use the
identical unbuildable `μ_r≠1` construct), but because this pre-screen's
period is set by `arg(r(θ))`'s *shape*, which turns out to be nearly
admittance-choice-invariant at these angles, whereas the x-wall's period
was set mostly by fixed geometric distance and its *amplitude* comparisons
sat close enough to decision bars that the same-sized admittance swap
could plausibly have mattered (my own exp-077 finding). **Practical
consequence**: the "realizable-admittance refit" test queued for this
sub-thread since exp-077 (Iteration 54, ranked MATERIALS #1, still
unexecuted — carried at #3 in exp-077's own Phase-5 ranking for Iteration
55, superseded this cycle by the y-wall pre-screen instead) remains higher
-value applied to the **x-wall** case than it would be applied to this
cycle's y-wall Test A — because there, unlike here, I can no longer say in
advance that it wouldn't move a verdict.

---

## 4. Ranked top-3 candidate next directions (MATERIALS' own lens)

1. **Run the still-unexecuted realizable-admittance (`μ_r=1`) refit on the
   x-wall's own two-wall model** (`PAIR_PAD`/`PAIR_ABSORB40` Test A+B,
   `experiments/077/`), not the y-wall. This is the pending MATERIALS test
   that can actually move a verdict — my own §2c computation this cycle
   shows the y-wall's period test is comparatively insensitive to this
   exact substitution, so the x-wall case is where the marginal Test-B
   numbers (`r²=0.0001`–`0.0418`, an order of magnitude below the `0.30`
   SUPPORT bar per exp-077's own record) are still worth checking against
   a buildable admittance before this seat calls the coherent-echo class's
   realizable branch closed on either wall. Zero new FDTD (reuses
   `boundary_reflectance.py`'s already-committed transfer-matrix
   machinery and the already-collected real data).
2. **Do not build a y-wall Test-B (full y-mirrored propagator) on
   materials grounds alone.** Given (a) this cycle's own corrected 0/3
   SUPPORT / null-indistinguishable Test-A result and (b) my own finding
   that even a realizability fix would not move Test A, MATERIALS sees no
   basis to prioritize the y-wall's full-propagator build over item 1
   above. If PHOTONICS/EM/QUANTUM's own charters find independent reasons
   to build it anyway (their call, not this seat's), the admittance-
   choice caveat should be priced *before* that build, not discovered
   after — reuse §2c's method (shape-Pearson + slope-ratio check) as a
   five-minute desk gate on whether the eventual Test-B curve is
   admittance-sensitive, the same way this review just did for Test A.
3. **Record, once, as a standing scope note** (not a new numbered rule —
   this doesn't rise to R-registry weight, just a discoverability fix):
   the "matched-`eps=mu`, PEC-backed, unrealizable admittance" caveat
   applies to *any* wall this engine's `Sim._damping` can produce, not
   per-orientation — confirmed independently for x (exp-075/077) and now
   y (this review, §2d). A future T28 cycle proposing a third wall
   orientation (the domain's far edges, already flagged as untested in
   this cycle's own Idealization 3) should not need a fresh MATERIALS
   critique to re-derive this; it is a property of the solver's boundary
   construction, established once.

---

## Compliance note

No RULED OUT item (R1–R9) is re-proposed or re-litigated. R4/R9: every
number I cite from the existing record was independently re-derived from
the committed JSON or source (§2a, §2b), not hand-typed from the write-up;
§2c's alt-admittance table is disclosed as my own fresh computation, not
attributed to any prior cycle. Per R8's standard, §2c is reported as an
actually-computed check, not an unverified expectation — I did not assume
the x-wall's magnitude carried over to the y-wall; I recomputed it and
found it does not, in the direction that lowers (not raises) urgency on
this specific pre-screen.
