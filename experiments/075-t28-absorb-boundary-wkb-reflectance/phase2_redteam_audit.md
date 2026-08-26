# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 52 · exp-075
## Adjudicating all five blind Phase-2 critiques of the `ABSORB`-boundary transfer-matrix reflectance model

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7, verbatim): "attacks
every proposal, speaks last and hardest. Its standard is NOT
textbook-physics compliance — speculation is permitted. It kills:
internal inconsistency, unfalsifiable claims, mechanisms that cannot be
expressed as simulation parameters, and proposals that quietly violate a
target constraint — especially #3. Red Team never leads a cycle; it has
no proposal of its own to protect." Constraint #3 is N/A this cycle
(instrument-fidelity work, not a phenomenon-mechanism claim — confirmed,
§0 below). Receives everything this cycle produced:
`phase1_proposal.md`, `boundary_reflectance.py` +
`boundary_reflectance_results.json`/`_output.txt`, and all five Phase-2
critiques (`phase2_critique_{photonics,materials,em,quantum,vision}.md`).
Every load-bearing claim below — including claims made **by** the five
critiques — was independently re-derived or re-run from the actual
committed code or from fresh scripts built for this audit, never taken on
any seat's word (house rule R4). No seat's finding is adopted by deferral
("I agree with X") — each is confirmed, refuted, or overridden here with
my own numbers.*

---

## 0. What I ran

1. `python3 experiments/075-.../boundary_reflectance.py`, unmodified —
   bit-exact reproduction of every number in `phase1_proposal.md` and
   `boundary_reflectance_results.json` (`rel_period_dev=4.2778`,
   `shape_r²=0.2586`, `pearson_r=-0.5085`, `COMBINED VERDICT: REFUTE`,
   G-LOSSLESS `2.220e-16`, G-N1 `1.404e-15`, G-PASSIVITY worst
   `|r|=0.006423`).
2. Read `lab/fdtd2d.py` lines 72–264 directly (not the proposal's
   paraphrase) — confirmed the damping-order and E/H-symmetric-loss
   claims, and that both domain edges (`Ez[1:-1,1:-1]` — index `0` and
   `nx-1` never touched by the curl step) are PEC by construction,
   exactly as PHOTONICS' attack requires.
3. Read `experiments/069/run.py::_one_run` — confirmed EM's claim that no
   material object exists in the scene this proposal is tested against
   (`Sim` + `add_line_source` + `.run()` only).
4. Independently recomputed PHOTONICS' cavity-variant arithmetic from
   `experiments/065/.../design_geometry.py::CONFIGS` directly (not from
   the critique's prose).
5. Ran my own 200,000-trial permutation test against the committed
   `predicted_delta`/`real_delta` arrays (independent seed, independent
   script) to check QUANTUM's `p=0.0035` claim.
6. Called `experiments/069/run.py::_fixed_period_fit` myself, in `sin θ`
   space with the `cos(39°)` center-scaling `_free_period_search` uses
   internally, at the six periods QUANTUM cites, plus a degree-2
   polynomial fit in `sin θ` — checking QUANTUM's "boundary-search
   artifact" claim bit-for-bit against QUANTUM's own numbers, not just
   its qualitative direction.
7. Reran `c_empty_with_wall` with `r → conj(r)` end-to-end (not read from
   the critique) to check EM's `-0.542` claim, then ran my own
   supplementary check EM did not attempt: evaluated `reflection_coefficient`
   on lossless (real-`n`) profiles of 1/5/20/40 vacuum cells backed by
   the PEC wall, and confirmed the code reproduces the textbook closed
   form `r = -exp(-2i k_x L)` exactly at every thickness and every angle
   tested (`0°,10°,30°,39°`) — see §4.
8. Independently re-derived the TE admittance algebra behind MATERIALS'
   "matched eps=mu medium" claim from scratch.
9. Recomputed `|r(θ;40)|/|r(θ;80)|` over the full 31-point dense-sweep
   grid (not just the three §2d table angles VISION's estimate was based
   on) to check VISION's "~40–70×" figure.
10. Built and ran a script VISION named as missing but did not itself
    build: the model's own per-config `C_with_wall(ABSORB) −
    C_boundary_free` term (the model's own predicted "echo residual") at
    all four `ABSORB` depths, its amplitude ratios, and its six pairwise
    cross-config shape correlations — the actual ABSORB-depth
    amplitude-scaling cross-check against exp-074's real residual-shape
    finding (LOGBOOK.md, Iteration 51).
11. My own new check, not requested by any of the five critiques: a
    "look-elsewhere" scan of 11 named length scales already present in
    `experiments/065/.../design_geometry.py::CONFIGS` (`nx`, `ny`,
    `src_x`, `plane_x`, `obj_x`, `obj_y`, `d_sp`, `lever`, `clear_plane`,
    `clear_src`, `aperture_cells`), each substituted for `D` in the
    proposal's own closed-form period formula, to test whether landing
    inside the pre-registered 30% SUPPORT band is as informative as
    PHOTONICS' attack implies (§3).

Every load-bearing number below is either bit-exact against the
committed record or comes from a script I ran myself in this audit.

---

## 1. Reproduction — CONFIRMED, exactly, by all six parties (five critics + me)

All five blind critiques independently reran `boundary_reflectance.py`
and reported identical figures; I reran it a sixth time. No R4 issue
here — this is the cleanest reproduction record this sub-thread has
produced across seven cycles (a real contrast with exp-072/073, where
Phase-5 reviewers restated uncomputed figures — see LOGBOOK R4's own
addenda). One minor, non-load-bearing procedural note: PHOTONICS'
critique states "I back-solved... `D_needed≈320`" without naming a
script — a hand computation, technically outside strict R4 discipline
for a *permanent-record* document, though this one is a critique, not a
NOTES.md/results.json citation, and the arithmetic is simple and (§3
below) exactly reproduces to `320.34` when I ran it. Flagged, not
scored — no action needed beyond noting the convention going forward.

---

## 2. Per-critique adjudication

### 2a. PHOTONICS — the two-wall cavity variant

**Claim**: using `nx` (full domain width, 360–440 cells across
`ABSORB`=40–80) instead of `PLANE_X` in the proposal's own closed-form
period formula gives periods of 2.07–2.53° at θ=39°, inside the
proposal's own ≤30%-of-`P*` SUPPORT band, at zero extra cost, and this
variant was never priced.

**CONFIRMED, independently, exactly.** Recomputing directly from
`CONFIGS` (not from PHOTONICS' prose):

| config | `nx` | `P(nx,39°)` | `rel_dev` vs `P*=2.8421°` |
|---|---|---|---|
| C40 | 360 | 2.5290° | 0.110 |
| C60 | 400 | 2.2761° | 0.199 |
| C70 | 420 | 2.1677° | 0.237 |
| C80 | 440 | 2.0692° | 0.272 |

All four sit inside the 0.30 SUPPORT threshold — confirmed to 4 decimal
places, `D_needed = 320.34` cells (the value of `D` that would hit
`P*` exactly) is genuinely close to the tested `nx` range. This is a
real, correctly-computed gap in the proposal's own coverage: Idealization
6 ("single echo only... not a resonant cavity between the band and
anything else in the scene") is named but its own numbers were never
run, despite landing closer to the target than the tested mechanism by a
wide margin. **Adopt as mandatory fix** — see §5/§7.

### 2b. MATERIALS — the matched-eps=mu realizability gap

**Claim**: `Z(x,θ)=n(x)/√(n(x)²−sin²θ)` is the admittance of a matched
(`μ(x)=n(x)`) medium, forced by the code's symmetric E/H damping — not
an ordinary `μ=1` conductive absorber's admittance, and not a class any
optical-frequency metamaterial platform realizes.

**CONFIRMED, by independent derivation.** TE (s-pol) wave impedance is
`Z_TE = ωμ/k_x`. For an ordinary dielectric (`μ=1`, `ε=n²`):
`Z_TE = 1/√(n²−sin²θ)`. For a matched medium (`μ(x)=n(x)`, so
`n²=εμ=n·n` is self-consistent): `Z_TE = n/√(n²−sin²θ)` — exactly the
code's formula. This is not a neutral or generic "effective index"
choice; it is a direct, forced consequence of `lab/fdtd2d.py` damping
`Ez`, `Hx`, `Hy` with the *identical* ramp (verified against the code,
§0.2) — MATERIALS' physical reasoning is sound, not merely plausible.
The proposal's own Idealization list (1–9) never states this
realizability class explicitly. **Adopt as mandatory fix**: a one-line
idealization addition, cheap, that prevents a future LOGBOOK citation of
this REFUTE from being read as ruling out boundary-reflectance mechanisms
for realizable (`μ=1`) absorber coatings generally — exactly the kind of
scope-creep this program's own R1/T9-style precedents exist to prevent.

### 2c. ELECTROMAGNETISM — the untested cross-module phase convention

**Claim**: `r(θ;ABSORB)`'s phase is never checked against exp-048's own
Huygens–Fresnel propagator's phase convention; the `r→conj(r)` test
(the obvious candidate fix) does not flip Test B's sign.

**CONFIRMED exactly** (`r=-0.5422`, `r²=0.2940` on my own independent
re-run — matches EM's `-0.542` to 3 significant figures; no sign flip).

**I went further, per the task's instruction to look for the mismatch
rather than stop at "the obvious fix didn't work."** I tested whether
`reflection_coefficient` itself carries an internal sign/convention bug
by checking it against a case with a known, textbook closed form: a
stack of `N` **lossless** (real, `n=1`) vacuum cells backed by the PEC
wall should reduce exactly to the standard mirror-plus-spacer formula
`r = -exp(-2i k_x L)`. Result:

| `N` (cells) | `θ` | committed `r` | textbook `-exp(-2ik_xL)` |
|---|---|---|---|
| 1 | 0° | `-0.8090+0.5878j` (arg 144.00°) | matches exactly |
| 5 (=λ/4) | 0° | `+1.0000+0.0000j` | matches (`-exp(-iπ)=+1`) |
| 20 (=λ) | 0° | `-1.0000-0.0000j` | matches (`-exp(-4πi)=-1`) |
| 1,5,20,40 | 0°,10°,30°,39° | machine-precision match, all cases | — |

**This is a real, independent finding, not in either the proposal or any
of the five critiques**: `reflection_coefficient`'s sign/phase convention,
taken alone, is *self-consistent with standard EM theory* — it correctly
reproduces the well-known PEC-mirror-with-spacer result at every tested
angle and thickness, including the sign flip a PEC boundary must impose.
This is evidence *against* a simple internal sign bug living in the
transfer-matrix formula itself (the object G-LOSSLESS/G-N1 already gate,
now cross-checked against an *external*, hand-derivable reference rather
than only against the code's own other code paths). It does **not**
resolve EM's actual concern, which is about the *relative* phase
convention between this module and the independently-authored exp-048
propagator it is coherently summed against — that remains genuinely
open. **PARTIALLY CONFIRMED / NARROWED**: EM's attack is correct that no
gate tests cross-module phase consistency, and correct that the obvious
fix doesn't work; my own check narrows where a bug, if any, could live
(not in `r(θ)` taken alone) without finding or ruling one out in the
composition step. **Disposition: adopt as informational-only for this
cycle** — Combined Verdict REFUTE does not depend on it (Test A alone
REFUTEs, and Test A is a purely geometric/phase-independent argument per
EM's own §3 — see §6 below); bind forward as a genuine open item for any
future cycle that builds a second wall-echo/cavity variant using the same
composition (§7's mandatory fix), where it becomes more consequential.

### 2d. QUANTUM OPTICS — Test A's boundary-artifact and Test B's sign-blind band

**Claim 1**: `P_model=15.0000°` is not a calibrated period estimate — `R²`
rises monotonically to whatever grid boundary is set, asymptoting to the
pure quadratic-trend `R²=0.8796`; no interior optimum exists.

**CONFIRMED, exactly, bit-for-bit against QUANTUM's own cited figures.**
Calling `_fixed_period_fit` myself in `sin θ` space (the way
`_free_period_search` actually calls it — a detail neither the proposal
nor I got right on a first, naive attempt using raw-degree `x`, see note
below) at QUANTUM's own six periods:

```
P*=   1°  R²=0.0131
P*=   4°  R²=0.4387
P*=  7.8° R²=0.7542
P*=  15°  R²=0.8587
P*=  60°  R²=0.8785
P*=1000°  R²=0.8796
degree-2 polynomial fit (sin θ):  R²=0.8796055...
```

Matches QUANTUM's `0.0131/0.4387/0.7542/0.8587/0.8785/0.8796` to all four
decimal places, and the polynomial asymptote match confirms the
mechanism QUANTUM names. (Procedural note for future R4 audits of this
sub-thread: calling `_fixed_period_fit` on raw `θ` in degrees instead of
`sin θ` with the `cos(39°)`-scaled period gives visually similar but
NOT bit-identical numbers — `0.0120/0.4220/.../0.8875` — a real trap for
anyone reproducing this cycle's own figures the fast way; I caught this
on my own first attempt, corrected it, and note it here so it isn't
rediscovered as a "discrepancy" by a future seat.) **The qualitative
REFUTE conclusion this feeds is not undermined — if anything it is on
firmer ground stated this way**: the real data has a genuine interior
maximum (`P*=2.8421°`, `R²=0.6272`, well above its own large-`P`
asymptote `R²≈0.41` computed the same way) while the model's curve has
none at any window tested. This is a cleaner, more robust REFUTE argument
than the `rel_dev=4.28` number the write-up leads with, because it
doesn't require treating a boundary-search artifact as a real deviation.

**Claim 2**: `r²=0.2586` is a statistically significant (`p=0.0035`,
200,000-trial permutation) *negative* correlation — the sign-blind band
mischaracterizes it as "close to, but under, the SUPPORT bar."

**CONFIRMED, independently, closely matching.** My own 200,000-trial
permutation test (independent seed, independent script — §0.5):
`percentile=99.669`, two-sided `p=0.00331`, `t=-3.180` (`n=31`), and an
analytic `t`-distribution check gives `p=0.00349` — all three routes
agree with QUANTUM's `p=0.0035` to within Monte-Carlo noise at this `N`.
**The substantive point is correct**: for a zero-free-parameter model
with a definite predicted phase, a significant *anti*-correlation is
real evidence the mechanism runs backward, which is stronger disconfirming
information than "inconclusive," not weaker. **Adopt both findings as
mandatory fixes for the write-up's narrative** (not a re-scoring —
pre-registration integrity means the SUPPORT/REFUTE bands themselves stay
as pre-committed; the fix is to state what actually happened rather than
imply Test A measured a calibrated deviation or that Test B was
ambiguous). Neither finding changes Combined Verdict REFUTE (§6).

### 2e. VISION SCIENCE — the un-run ABSORB-depth cross-check

**Claim**: the model's own §2d table implies `|r|` scales ~40–70× between
`ABSORB=40` and `80`; this is never checked against exp-074's finding
(LOGBOOK Iteration 51) that the four real configs' own residual shapes are
near-identical across depths (cross-config `r=0.992–1.000`) — a
depth-*independent* signature the model's own strongly depth-*dependent*
echo term should be compatible or incompatible with, and the proposal
never does the arithmetic.

**CONFIRMED and SHARPENED — this is the single most consequential finding
in this audit.** First, the raw scaling claim, recomputed over the full
31-point dense sweep (not just the three §2d table angles VISION's
estimate was read off): `|r(θ;40)|/|r(θ;80)|` ranges **54.9× to 99.1×**
across the sweep — same order of magnitude as VISION's "~40–70×" (which
was read off rounded 4-decimal table entries), confirmed in direction and
magnitude, refined in precision.

**Second — I built and ran the cross-check VISION named as missing.**
The model's own per-config predicted echo term (`C_with_wall(ABSORB) −
C_boundary_free`, the ONLY source of `ABSORB`-dependence in the model,
confirmed by the script's own `boundary_free_spread_internal_check=0.0`)
at all four depths:

```
ptp(ABSORB=40) = 7.978e-4
ptp(ABSORB=60) = 1.174e-4   (6.79x smaller than 40)
ptp(ABSORB=70) = 1.927e-5   (41.40x smaller than 40)
ptp(ABSORB=80) = 2.810e-5   (28.39x smaller than 40)

cross-config shape correlations (Pearson r):
  r(40,60) = -0.985
  r(40,70) = -0.203
  r(40,80) = +0.913
  r(60,70) = +0.276
  r(60,80) = -0.924
  r(70,80) = -0.560
```

**This directly and sharply contradicts exp-074's real, established
finding.** Not only does the model's own predicted echo amplitude vary
wildly (not merely scale down) across `ABSORB`, its predicted *shape*
correlates weakly, and at three of six pairs *negatively*, across depths
— the opposite of the real data's near-identical (`r=0.992–1.000`)
residual shapes. This is a **second, independent line of REFUTE
evidence** the proposal computed all the ingredients for and never
assembled — stronger than VISION's own critique anticipated (VISION
flagged the amplitude-scaling tension; the shape-anticorrelation result
is new here). **Adopt as mandatory fix**: this is zero marginal FDTD
cost, already computable from committed code, and materially strengthens
(never weakens) this cycle's own REFUTE — it should enter the permanent
record before this cycle closes, not be left as a hypothetical.

---

## 3. My own finding: the cavity match is suggestive, not yet evidence — an R5-class look-elsewhere risk

PHOTONICS' cavity-variant arithmetic (§2a) is correct, but I ran a check
none of the five critiques did: how many of the *other* named length
scales already sitting in the same `CONFIGS` dictionary would *also* land
in the SUPPORT band if substituted for `D` in the identical formula?

The SUPPORT band (`rel_dev ≤ 0.30`) corresponds to `D ∈ [246.4, 457.6]`
cells around `D_needed=320.34` — a band spanning `0.77×` to `1.43×`
`D_needed`, i.e. a wide swath of the plausible "big length scale" range
in this geometry. Scanning 11 named constants from `CONFIGS` across all
four configs:

| constant | in-band (all 4 configs)? |
|---|---|
| `nx` | **yes** |
| `src_x` | **yes** |
| `ny`, `plane_x`, `obj_x`, `obj_y`, `d_sp`, `lever`, `clear_plane`, `clear_src`, `aperture_cells` | no (9 of 11) |

Two of eleven candidates land in-band — not one, and not most. This is
directly the shape of finding that this program's own house rule (R5's
addendum, LOGBOOK.md, Iteration 47/exp-070: "any future proposal that
searches a named-constant/parameter space... for a match to a target
value MUST include a pre-registered null-permutation... control before a
match counts as evidence") exists to catch, applied here at `n=11`
rather than exp-070's `n=36,680` — smaller, but the same failure
geometry: a formula whose output is a smooth, monotone function of one
free length scale, tested against a loosely-set (30% relative) tolerance
band, against a "search space" of geometric constants that were not
independently, physically nominated in advance as candidate mechanisms
(only `nx`, motivated by PHOTONICS' own two-wall-cavity story, was).
`src_x` landing in-band too has no comparably clean physical story (a
"source-position echo" isn't the two-wall-cavity mechanism PHOTONICS
named) — its presence in the same 2-of-11 set is exactly the kind of
coincidence a null-permutation control is built to separate from a real
signal.

**This does not refute PHOTONICS' attack — it sharpens what disposition
it deserves.** The cavity variant is a genuinely well-motivated,
same-cost, same-machinery candidate that PHOTONICS is right to say was
never priced. But "lands inside a 30%-wide band using a naive `D→nx`
substitution into a formula derived for a *different* mechanism" is
weaker evidence than PHOTONICS' own critique language ("landing far
closer than the tested mechanism") implies on its own — it is exactly
the situation R5 says needs an actual computed model (the real two-wall
transfer-matrix + interference calculation, analogous to what §2e of
`phase1_proposal.md` built for the single-wall case, not a substituted
`D`) plus, given the look-elsewhere risk demonstrated here, some form of
robustness check before its own SUPPORT/REFUTE is trusted either way.

---

## 4. Numbered attacks

1. **[inconsistency]** §5's "narrows the remaining candidate space"
   framing is not earned as written: a same-cost, same-machinery
   two-wall-cavity variant, closed-form-estimated by PHOTONICS and
   independently confirmed here (§2a) to land inside the proposal's own
   pre-registered SUPPORT band, was never priced, computed, or scored.
   The REFUTE for the *specific, tested* single-`-x`-wall-echo mechanism
   is solid (§6); the broader claim that boundary-reflectance mechanisms
   generally are narrowed is not, while this variant sits untested.

2. **[informational, not a live defect]** Idealization 2's realizability
   class (matched `ε=μ` medium, forced by the code's symmetric E/H
   damping) is never named as a physical realizability status in the
   idealization list, risking a future citation reading this REFUTE as
   covering realizable (`μ=1`) absorber coatings generally, which it does
   not test (MATERIALS, §2b, confirmed).

3. **[inexpressible-adjacent, not cleanly any of the four tags]** No
   gate in this proposal tests cross-module phase-convention consistency
   between `r(θ;ABSORB)` and the independently-authored Huygens–Fresnel
   propagator it is coherently summed against (EM, §2c). This is a real
   *verification gap*, not a demonstrated inconsistency (my own §2c
   supplementary check found the transfer-matrix formula's own phase
   convention self-consistent against a hand-derivable textbook
   reference) and not unfalsifiable (Test A stands on its own regardless
   — §6). It does not fit PANEL.md's four tags cleanly; flagging that
   explicitly rather than forcing it into one.

4. **[inconsistency]** Test A's headline number (`rel_dev=4.28`) is
   reported as though it were a calibrated period-mismatch factor; it is
   actually a boundary-search artifact of a curve that never completes a
   third of an oscillation across the tested window (QUANTUM, §2d,
   confirmed bit-exact). The REFUTE conclusion survives on a cleaner
   argument (the real data's confirmed interior maximum vs. the model's
   confirmed absence of one) — but the write-up should not carry the
   `4.28×` figure forward as a measured deviation.

5. **[inconsistency]** Test B's SUPPORT/REFUTE band is sign-blind for a
   model that makes a definite phase prediction; the observed
   `r²=0.2586` is a statistically significant (independently confirmed,
   `p≈0.0033–0.0035`, two methods) *anti*-correlation, mischaracterized
   in §5's prose as an ambiguous "close to, but under, the SUPPORT bar"
   result (QUANTUM, §2d, confirmed). Correct evidence, understated
   framing — Combined Verdict is unaffected (§6).

6. **[inconsistency]** §5 never checks the model's own §2d-table
   `ABSORB`-depth |r| scaling (independently confirmed here at
   54.9×–99.1× across the full sweep, §2e) against exp-074's own
   established, near-identical (`r=0.992–1.000`) real residual-shape
   finding — a check this cycle computed every ingredient for and never
   assembled. Run here (§2e): the model's own predicted echo shapes are
   weakly-to-negatively correlated across depths (three of six pairs
   negative), sharply contradicting the real data's near-identity — a
   second, independent REFUTE line, uncomputed in the committed record.

7. **[informational, forward-looking, not a defect in this cycle]** the
   cavity-variant closed-form match (§2a/attack 1) is itself at risk of
   an R5-class look-elsewhere read: only 2 of 11 named geometric
   constants land inside the 30%-wide SUPPORT band when substituted into
   the same formula (§3), and one of those two (`src_x`) has no
   comparably motivated physical story. Any future test of the cavity
   mechanism should build the actual two-wall transfer-matrix +
   interference calculation (not a `D`-substitution into a formula
   derived for the single-wall case) and, given this look-elsewhere
   exposure, carry some form of robustness/null check before its own
   verdict is trusted — matching this program's own R5 addendum standard.

---

## 5. Disposition table

| Item | Source | My verdict | Disposition |
|---|---|---|---|
| Cavity-variant closed-form match | PHOTONICS | CONFIRMED (§2a) | **Adopt as mandatory fix** — build and score the actual two-wall model before Phase 3 headline framing is finalized |
| Look-elsewhere risk on that match | Red Team, new (§3) | new finding | **Adopt as mandatory fix**, attached to the above — the cavity test must ship with a robustness/null check, not just a point estimate |
| Matched-eps=mu realizability scope | MATERIALS | CONFIRMED (§2b) | **Adopt as mandatory fix** — cheap idealization-list addition |
| Cross-module phase convention untested | EM | PARTIALLY CONFIRMED / NARROWED (§2c) | **Adopt as informational-only** this cycle (Combined Verdict is independent of it, §6); bind forward for any future cavity/echo variant |
| Test A boundary-search artifact | QUANTUM | CONFIRMED, bit-exact (§2d) | **Adopt as mandatory fix** for write-up precision; no rescoring needed |
| Test B sign-blind mischaracterization | QUANTUM | CONFIRMED (§2d) | **Adopt as mandatory fix** for write-up narrative; no rescoring needed |
| ABSORB-depth residual cross-check | VISION | CONFIRMED and SHARPENED (§2e) | **Adopt as mandatory fix** — commit the computed cross-check to the permanent record; strengthens REFUTE |

Nothing here is overridden — every one of the five critiques' load-bearing
claims independently reproduces, several more sharply than as first
written. This is a genuinely well-executed cycle by this program's own
recent standards (contrast with Iterations 49/50's sign bugs, below).

---

## 6. Does the Combined Verdict `REFUTE` survive? Yes — robustly, for the mechanism actually tested

Every item above that could, in principle, threaten the specific
single-`-x`-wall-echo REFUTE turns out not to:

- Test A's REFUTE rests on `PLANE_X`, a fixed, measured geometric
  quantity, independent of the loss-branch choice (§2.b's passivity
  resolution) and independent of the untested cross-module phase
  question (§2c) — EM's own robustness argument, which I did not find
  any reason to overturn. The *sharper* version of Test A (QUANTUM's
  polynomial-degeneracy argument, §2d) makes this REFUTE stronger, not
  weaker.
- The pre-registered combining rule (`REFUTE if EITHER test REFUTEs`)
  means Test A's REFUTE alone determines the Combined Verdict regardless
  of any resolution of Test B's phase-convention uncertainty (§2c) — even
  if a future cross-module phase fix flipped Test B to positive, Combined
  Verdict would still read REFUTE.
- VISION's newly-computed cross-check (§2e) adds a *second*, independent
  REFUTE line (depth-scaling incompatibility) rather than threatening the
  first.

**REFUTE for the single-`-x`-wall-echo mechanism, as tested, stands —
independently reconfirmed by six separate computational routes in this
audit (§0), none of which weakens it.**

What does NOT survive unmodified is §5's own broader reading. The
prompt's own suggested reframing is, on the evidence gathered here,
correct: **"REFUTE of the single-wall-echo mechanism specifically; the
untested cavity variant may fully or partially explain T28, so 'narrows
the remaining space' is not yet earned."** This is not a rejection of the
cycle's physics — it is a scope correction on one sentence, forced by
PHOTONICS' own arithmetic (§2a), which this audit independently confirms
and which no critique (including Red Team's own first pass) can wave
away with "it's probably just a coincidence" (§3 shows it is *not
obviously* a coincidence either — 2 of 11 is not the "everything matches"
pattern that would make dismissal easy).

---

## 7. Standing-rule check

- **R4** (recompute, don't restate): satisfied throughout — see §1. One
  minor procedural note (PHOTONICS' hand-solved `D_needed`, §1) is not
  load-bearing (I independently reproduced it) and not a violation of the
  rule as stated (which governs permanent-record citations, not critique
  prose), but is worth naming so the convention tightens going forward.
- **R6** (synthetic ground-truth recovery gate, mandatory for any
  carrier/phase-conditioned coefficient fit): **does not apply this
  cycle**. This model fits zero free parameters to the real T28 data —
  the only "fit" performed (`_free_period_search`) is applied to the
  *model's own predicted curve*, not to real data, and is a diagnostic,
  not a coefficient estimate gated for a `RESOLVED` claim. Correctly not
  triggered.
- **R7** (a conditioning/pricing-only bound is not sufficient for a
  closure or detection claim — the model must be fit/tested against real
  data): **satisfied, not violated**. Unlike exp-074's Phase-1 draft, this
  proposal does not merely price the model — Test A and Test B are
  genuine tests against the real `block_dense.rows` data. R7's concern is
  correctly avoided here, and should be cited as a positive example of
  R7 compliance, not merely "not triggered."
- **Iteration 49/50 sign-convention-bug pattern, explicitly checked, as
  directed**: this cycle shows the *opposite* failure shape from
  Iterations 49–50. There, a genuine, undetected sign bug shipped,
  survived Phase 3/4, and took three-to-six blind Phase-5 seats plus a
  final audit to catch, in both cycles, on the *same* underlying
  function. Here: (a) a genuine sign/branch ambiguity was found *during
  derivation*, disclosed in full (not smoothed over), and resolved by an
  unambiguous physical principle (passivity) rather than by matching the
  target data (§2c of `phase1_proposal.md`, §2c above) — the correct
  process, not the process that failed twice in Iterations 49–50; (b) my
  own independent lossless-limit check (§2c) found no internal sign bug
  in the resulting formula; (c) EM's attack *did* look for a second,
  undetected sign-convention issue (the cross-module phase question) —
  exactly the discipline Iterations 49–50 established as mandatory
  vigilance — and found a genuine gap in verification coverage, not a
  confirmed bug. This cycle passes the test the LOGBOOK's own T28 history
  was set up to apply: no seat, including this one, found evidence this
  program has walked into the same error species a third time.

---

## 8. Checkpoint check — all five criteria

1. **A configuration passes all constraint metrics** — N/A, not a
   phenomenon-mechanism cycle. Does not fire.
2. **A proven boundary within a mechanism class** — N/A; this REFUTE
   concerns one instrument-fidelity mechanism, not a T1 escape-route
   class. Does not fire.
3. **Synthesis requiring engine physics beyond validated bench classes**
   — no; zero `lab/` diff, pure desk analysis throughout, confirmed at
   §0. Does not fire.
4. **Program-integrity drift** (unfalsifiable claims, a constraint
   quietly dropped) — **does not fire**. Every claim in this proposal is
   falsifiable and was actually tested against pre-registered bands
   (§6); constraint 3's N/A status is stated explicitly and correctly
   (§0 of `phase1_proposal.md`, confirmed against PANEL.md §7); the gaps
   found in this audit (§4) were caught here, at Phase 2, before entering
   the permanent record — the process working as intended, not drift.
5. **Two consecutive non-advancing iterations** — **does not fire**. This
   cycle delivers genuine, independently-confirmed narrowing (a
   previously-untested mechanism class REFUTEd, with two independent
   lines of evidence, §6), the first substantive movement on T28's own
   mechanism question since it opened at Iteration 46 — six cycles of
   the *differential-fit* instrument class narrowed but did not advance
   the mechanism question; this cycle, on a *different* instrument class,
   does.

**No Checkpoint criterion fires.**

---

## 9. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

**Not** a clean PROCEED: the cavity-variant gap (§2a/§3, attacks 1 and 7)
is not a stylistic nitpick — it is a same-cost, same-machinery,
zero-FDTD test that this program's own culture (the "T28 must receive at
least one cheap, desk-only first move" tripwire precedent, Iteration 46;
R5's addendum on unverified close matches, Iteration 47) would not let
stand unaddressed before treating this cycle's finding as closing or
narrowing the boundary-reflectance-echo mechanism space. **Not** a
REJECT or OPPOSE: the REFUTE for the mechanism actually tested is sound,
independently reconfirmed six ways in this audit, and gets *stronger*
(not weaker) once VISION's cross-check (§2e) is folded in.

**Mandatory fixes for Phase 3, in priority order:**

1. **Build and score the actual two-wall-cavity transfer-matrix +
   interference model** (not a `D→nx` substitution into the single-wall
   closed form) against Test A/B, on the same pre-registered-style bands,
   **with a look-elsewhere/robustness check** given §3's finding that a
   naive substitution's "landing in-band" is not yet strong evidence on
   its own. This is the single most important open item — until it
   exists, §5's "narrows the remaining space" cannot be written up as
   this cycle's closing statement; the correct interim language is
   **"REFUTE of the single-wall-echo mechanism specifically; the untested
   two-wall-cavity variant may fully or partially explain T28."**
2. **Commit VISION's ABSORB-depth residual cross-check (§2e) to the
   permanent record** — zero marginal cost, already computed here,
   strengthens REFUTE with a second independent line of evidence.
3. **Add the matched-ε=μ realizability idealization** (MATERIALS, §2b) —
   cheap, prevents future over-reading.
4. **Correct Test A/B narrative precision** (QUANTUM, §2d) — the
   boundary-search-artifact and sign-significance findings, for accurate
   future citation; does not change any verdict.
5. **Informational, bind forward, not this cycle**: the cross-module
   phase-convention gate EM's attack names (§2c) — becomes load-bearing
   the moment a second coherently-summed echo/cavity term (item 1) is
   built; should ship alongside it, not before.

If items 1–2 land and item 1's cavity test *also* REFUTEs (with its own
look-elsewhere check clean), then — and only then — this sub-thread earns
something close to the original "narrows the remaining space" framing,
now on solid ground across two independently-tested mechanism variants.
If item 1 instead lands inside a properly-computed SUPPORT band, that is
this program's first real positive lead on T28's mechanism in seven
cycles, and would itself be a Checkpoint-2-adjacent finding worth
flagging to Marsh at that point — not yet, on the evidence in hand today.

---

## 10. Bottom line

REFUTE, for the single-`-x`-wall-echo mechanism specifically, is real
physics, honestly derived, and survives every attack raised against it,
including two this audit found and confirmed independently (the
polynomial-degeneracy sharpening of Test A, and the depth-scaling
contradiction of Test B/§2e) that make it stronger than as first
written. What does not yet survive is treating this cycle as a complete
answer to "does boundary-reflectance physics explain, or rule out,
T28" — a same-cost sibling mechanism landed inside the SUPPORT band on a
first-pass estimate and was never priced. The seventh-cycle rule that
retired the differential-fit instrument class (Iteration 51) does not
apply here — this is a different instrument class, on its first cycle,
performing well — but this program's own standing discipline against
leaving a cheap, decisive, already-flagged test unrun before declaring a
cycle's headline finding does apply, and should govern how Phase 3
closes this cycle.
