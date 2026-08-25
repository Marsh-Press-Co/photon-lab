# PHASE 2 — RED TEAM AUDIT · Panel Iteration 48 · exp-071

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7). Receives everything:
phase1_proposal.md plus all five blind Phase-2 critiques
(photonics/materials/em/thermodynamics/quantum). Standard is NOT
textbook-physics compliance — it kills internal inconsistency, unfalsifiable
claims, inexpressible mechanisms, and quiet constraint violations. Every
numeric claim below was independently re-derived from code, not taken on
any seat's word — including my own.*

## 0. What was independently re-run

- `python3 experiments/071-t28-absorb-depth-causal-test/design_geometry.py`
  — every printed figure (congruent-series table, `P(39°,600nm)=1.9608°`,
  peak-angle fractions 0.949/0.984, R3-rescaled configs, budget 74 calls /
  5882.3 CPU-s / 28.76 min wall / 86.28 min envelope, de-scope floor 70
  calls / 24.53 min) reproduces bit-for-bit. **No hand-typed figure found
  anywhere in the six documents — R4 clean.**
- `lab/fdtd2d.py::Sim._damping` read directly: cubic ramp
  `(arange(absorb,0,-1)/absorb)**3`, `d = maximum(...)` on all four edges,
  `return np.exp(-0.30*d)`, applied to `Bx/By` (H-update) and `Ez`
  (E-update). Confirms MATERIALS' and THERMODYNAMICS' characterization of
  `ABSORB` exactly: a numerical domain-truncation boundary depth, not a
  material parameter — verbatim, not paraphrase.
- `experiments/065-.../settled_sweep_steps2800_diagnostic.json` read
  directly: `C40|-40.0|600 = -0.003559`, `C60 = -0.003216`, `C70 =
  -0.003147`, `C80 = -0.003368` — confirms EM's non-monotonic-residual
  citation exactly (dip at C70, rise at C80).
- `experiments/065-.../phase4_results.md` read directly: STEPS 1400→2800
  ratios C40=74.4%, C60=68.4% — confirms EM's citation exactly.
- `experiments/069-.../design_geometry.py` and `run.py` read directly:
  confirms `Block SETTLE-C80` exists (C80 only, STEPS 2800-vs-4200 at
  θ∈{39°,40°}) and **no equivalent check has ever been run on C60 or C70,
  at any angle, at any λ** — EM's central claim is real, not a
  misreading.
- `grep` on `experiments/071-.../design_geometry.py`: `_free_period_search`
  appears only in a comment (line 50); it is never imported or called —
  confirms QUANTUM's inheritance-check finding exactly. (Expected at this
  stage — `run.py` doesn't exist yet — but the risk QUANTUM names, that
  "identical methodology" is currently a prose promise not a code fact, is
  real until `run.py` is written and asserts it.)
- Independently re-derived QUANTUM's Rayleigh/Fourier resolution-floor
  arithmetic from scratch (own script, not copying theirs): window
  `Δ(sinθ) = sin(42°)−sin(36°) = 0.081345`; required `Δ(sinθ)` to resolve
  T21's 1.9608° from `P*_delta=2.8421°` is 0.08577 (window supplies
  **0.948×** — matches QUANTUM exactly); from C40's 2.4361° is 0.13631
  (**0.597×** — matches exactly); to resolve C40's 2.4361° from C80's
  2.5338° is 0.85694 (window supplies **0.0949×**, i.e. **10.5× more
  window needed than exists** — matches QUANTUM's "10.5×" exactly).
  **QUANTUM's math is correct in every digit I could check.**

## 1. An independent finding none of the five critiques caught

I extended QUANTUM's own resolution-floor calculation to the **CONFIRM**
band, not just the REFUTE band they flagged. QUANTUM correctly showed the
15%-pairwise-spread REFUTE criterion can fire on pure under-resolution. I
computed the break-even spread fraction — the pairwise spread at which the
window (0.0813 in `Δ(sinθ)`) *fully* Rayleigh-resolves two periods near the
observed cluster (mean `P*≈2.45°`):

```
spread=30.0% (the CONFIRM band's own minimum): window/required = 0.751
spread=39.3%: window/required = 1.000  (break-even)
```

**The CONFIRM band's own 30% minimum threshold sits at only 75% of full
Rayleigh resolving power at this window size and period scale — below the
resolution floor, not above it.** This means P-071-2 could fire CONFIRM
not only from a genuine ABSORB-depth trend, but from four independent
noisy period-recovery fits of a *single* underlying (non-ABSORB-tied)
period, spread apart by estimation noise on the order of the window's own
frequency-resolution floor — which is comparable to or larger than the
30% CONFIRM bar itself. The conjunctive `R²≥0.50` requirement does not
independently rescue this: the linear-trend R² is computed **on the same
four noisy P* point estimates**, so it is correlated with, not orthogonal
to, the same underlying resolution-floor noise source. **Both directions
of the Combined Verdict — CONFIRM and REFUTE — are compromised by the
identical fixed-window resolution floor, not just the REFUTE direction
QUANTUM named.** This is the single most consequential number in this
audit and I could not find it stated anywhere across all five critiques or
the proposal itself.

## 2. Numbered attacks

1. **[constraint-#N/A — no phenomenon constraint applies; program-integrity
   attack] Settling-closure gap on C60/C70 (EM's finding, independently
   verified real and load-bearing).** `STEPS_SETTLED=2800` is imported and
   applied to C60/C70 with zero settling-closure evidence specific to
   either config, at any angle, any λ. The only settling evidence that
   exists for C60/C70 is a 1400→2800 ratio (68.4%/comparable-to-74.4%)
   that shows movement, not convergence. `Block SETTLE-C80` (exp-069)
   checked only C80; the 4-point asymptotic series (1400/2800/4200/5600)
   that established 2800 as a floor ran only on C40 (exp-065). This
   program's own Learned note from that experiment states plainly that
   settling does not transfer across geometry changes — and `ABSORB`
   changes `NX`/`NY`/the damping profile, i.e. the geometry, for exactly
   the two new configs. The non-monotonic C40→C60→C70→C80 residual at a
   single already-measured angle (verified above, real data) is a
   plausible signature of exactly this failure mode: an unsettled,
   config-specific transient masquerading as an ABSORB-tracking trend —
   which is precisely what P-071-2 is built to detect. **This is not
   merely an EM nicety; it directly threatens the causal read of the
   headline result in either direction.**

2. **[unfalsifiable-adjacent / resolution-floor risk — both directions,
   my own extension of QUANTUM's finding] The CONFIRM and REFUTE bands
   both sit at or below the window's own Rayleigh resolution floor.**
   Verified in §1 above, independently derived: REFUTE's 15% band fires on
   pure under-resolution (window supplies as little as 9.5% of what's
   needed to separate adjacent-ABSORB periods); CONFIRM's 30% band sits at
   75% of full resolving power — under, not over, the line. As stated,
   neither branch of P-071-2's Combined Verdict can currently be trusted
   to mean what its own label claims ("genuine ABSORB-depth-tied
   mechanism" / "shared-geometry, NOT ABSORB-tied") without a computed,
   disclosed resolution floor gating the interpretation. Left unaddressed,
   whatever P-071-2 reports risks becoming this program's third instance
   of "a dense/underpowered search finds something regardless of ground
   truth" (R5, R5-addendum) — a *new* instance, via resolution rather than
   combinatorics, exactly QUANTUM's own framing.

3. **[inconsistency, minor] The proposal's own null-permutation-control
   section correctly rules out R5/R5-addendum's *combinatorial*
   look-elsewhere risk, then treats that as ruling out look-elsewhere risk
   generally.** It is right that this is not a combinatorial search — but
   attacks 1 and 2 above show a different, real look-elsewhere-shaped risk
   (resolution-floor and settling-transient false positives/negatives)
   sits directly underneath the one statistical safeguard the proposal
   does name (idealization 5, "a power concern, not a look-elsewhere
   one"). That characterization is now shown to understate what it is.

4. **[constraint-#N/A — house-discipline regression, MATERIALS' finding,
   independently verified real] The Combined Verdict's CONFIRM branch is
   titled "genuine ABSORB-depth-tied mechanism," and the narrative claims
   "direct physical coupling between the graded-loss boundary's own
   thickness and the observed periodicity," with zero disclosure that
   `ABSORB` is `lab/fdtd2d.py::Sim._damping`'s own numerical
   domain-truncation device** (verified directly above: cubic ramp,
   `exp(-0.30·d)`, applied to all four box edges — no material referent,
   real or hypothetical). exp-070's own Phase-3 synthesis made exactly
   this caveat a **required** disclosure on every future citation of
   `ABSORB`-derived numbers (mandatory fix 5, one cycle ago). This
   proposal is the *direct* causal follow-up on that exact parameter and
   drops the caveat while moving its own labeling language in the
   overclaiming direction. A one-cycle-old house rule regressing in the
   cycle that most directly implicates it is a real, load-bearing defect
   of language, not physics — but if CONFIRM fires this run, that
   labeling will read downstream, skimmed, as a materials finding about a
   real absorbing boundary. Cheap to fix; not cheap to leave unfixed once
   the result is committed to LOGBOOK.

5. **[inexpressible-adjacent, minor / scope gap, THERMODYNAMICS' finding,
   independently verified real] Nowhere does the proposal state why the
   THERMO energy-ledger metric row does not apply this cycle.** Verified
   independently (not deferring to THERMO's say-so): with no PEC/absorbing
   *article* run (idealization 4/8, Block ARTICLE not re-run), and with
   all four congruent configs being near-total absorbers at their boundary
   by construction (that's what makes them "congruent" — A/clearances/
   D_SP held fixed), there is no absorbed-energy trend for a sidecar to
   characterize, and no witness-scene material for power to re-radiate
   from. THERMODYNAMICS is right that the sidecar genuinely does not
   apply — but the proposal never says so, breaking CLAUDE.md's own
   "every writeup states its idealizations" convention in a case where the
   omitted sentence is exactly the one a skimming future reader would need
   to avoid misreading an ABSORB-CONFIRM as evidence about a physical
   absorbing mechanism's thermal behavior.

6. **[optical-scope gap, PHOTONICS' finding, independently verified real
   but lower severity than 1/2] Single-wavelength (600nm) scope on the new
   C60/C70 legs means the same cell count corresponds to a different
   optical depth at 750nm** (verified: 40/60/70/80 cells at cpl=20 is
   2.0/3.0/3.5/4.0λ; at cpl=25 is 1.6/2.4/2.8/3.2λ — exact arithmetic,
   both check out). A clean P-071-2 CONFIRM at 600nm alone cannot
   distinguish "physically real, λ-scaled optical coupling to the graded
   boundary" from "a cell-count/discretization artifact" — a materially
   weaker claim than "genuine ABSORB-depth-tied mechanism" implies, on
   exactly the axis this seat owns. This compounds attack 4 (both push
   toward softening the CONFIRM label) but is analytically separable
   from it — it is about wavelength-scaling, not about the
   numerical-vs-physical identity of `ABSORB` itself.

7. **[cost-accounting gap, my own finding] The de-scope docket's own
   "Never de-scoped" list omits the two fixes above.** If EM's Block
   SETTLE-C60C70 and QUANTUM's resolution-floor computation are adopted as
   mandatory (§3 below), the proposal's own pre-declared de-scope order
   (§ "De-scope order if breached") does not mention them at all — an
   omission that would let a future budget-pressured shift silently drop a
   just-adopted mandatory fix under the existing "retract R3-PEAK first"
   logic, since that logic was frozen before these fixes existed. Phase 3
   synthesis must explicitly place the new items on the "never de-scoped"
   list, not just the FDTD Block DENSE-CAUSAL and Block G1 named there
   today.

8. **[not a defect — checked and cleared] The `A=752` congruence assertion
   and G1 identity-gate construction are sound and correctly gate every
   reused number.** Checked directly in code: the assertion fires at
   import time if any of the four configs' `A` differ, and G1 reruns two
   already-committed cells bit-exact before any exp-069 data is trusted.
   No attack found here across all five critiques or my own read.

## 3. Independent verification of all five critiques — summary table

| Critique | Core claim | Verified? | Load-bearing? |
|---|---|---|---|
| PHOTONICS | 600nm-only scope can't discriminate λ-scaled optical coupling from cell-count artifact; cited cell-to-λ arithmetic | **Confirmed, arithmetic exact** | Real but secondary — softens a label, doesn't invalidate the causal test itself |
| MATERIALS | `ABSORB` is PML-analog numerical bookkeeping, not a material; CONFIRM-branch language overclaims, regressing exp-070's own mandatory fix 5 | **Confirmed — `_damping` code matches description exactly; exp-070 mandatory-fix-5 text confirmed to exist and require exactly this caveat** | Real, cheap, mandatory (language only) |
| ELECTROMAGNETISM | No settling-closure check exists for C60/C70 at any angle/λ; non-monotonic per-cell residual is a plausible unsettled-transient signature | **Confirmed — both the absence of any C60/C70 settling check and the cited −0.003559/−0.003216/−0.003147/−0.003368 figures verified against exp-065's own committed JSON** | **One of the two most severe findings in this audit** |
| THERMODYNAMICS | THERMO sidecar genuinely inapplicable, but the proposal never states why | **Confirmed — independently re-derived the "why," not deferred; `T5_THERMAL_CAVEAT`/NETD citation verified against exp-065's own file** | Real, cheap, mandatory (one sentence) |
| QUANTUM OPTICS | REFUTE band (15% pairwise spread) can fire on pure under-resolution; Rayleigh-floor arithmetic | **Confirmed exactly, every cited ratio reproduced independently (0.948/0.597/10.5×)**; extended by Red Team (§1) to show the CONFIRM band has the identical problem | **The other of the two most severe findings — and worse than its own author stated** |

No critique contains a fabricated or unverifiable number. No critique's
attack is spurious. All five earn their verdicts.

## 4. Weighing the two most load-bearing critiques explicitly

**EM's settling-closure gap (attack 1).** This is a genuine internal-
consistency defect: the proposal imports a floor ("settled") certified on
different configs and applies the label to two configs that have never
independently earned it, while this program's own prior finding (from the
exact experiment that discovered STEPS=1400 was unsettled) says explicitly
that this does not transfer. The plausibility case (non-monotonic residual
dipping at C70) is real data, not speculation. **Severity: high, but
narrowly fixable.** The fix (`Block SETTLE-C60C70`, 4 calls, mirroring
`Block SETTLE-C80`'s already-proven construction) is cheap, uses zero new
machinery, and slots in as a binding precondition on P-071-2 exactly as
P-071-4 already is. This does **not** require redesign before any FDTD
call — it requires one more Block, added before Phase 3 freeze, with the
Combined Verdict's HALT/CONFIRM/REFUTE logic extended to depend on it.

**QUANTUM's resolution-floor risk (attack 2), extended by my own finding
in §1.** This is the more structurally serious of the two: it is not a
missing check that can be added post-hoc to the *already-collected* data
in the way a settling check can (settling can be probed with 4 new FDTD
calls; resolution cannot be improved after the fact by more calls at the
*same* window — the window itself is the limiting factor, and the window
is fixed by the mandate's own requirement to reuse exp-069's committed
36–42° dataset at zero cost). However — critically — **the fix does not
require a wider window or more FDTD calls at all.** It requires computing
the Rayleigh/Fourier resolution floor **in code, from the already-planned
data**, for every P-071-3 pairwise comparison and for the CONFIRM/REFUTE
trend test itself, and re-classifying any comparison that falls below its
own resolution floor as **UNRESOLVED** rather than letting it silently
support CONFIRM or REFUTE. This is desk arithmetic — the same kind of
zero-FDTD-cost fix this program has repeatedly and successfully folded in
same-shift (R5-addendum's own null-permutation control, exp-070). **Severity: high, but fixable without touching the FDTD plan.**

**Verdict on redesign vs. fold-in: neither finding requires halting
before any FDTD call.** Both fixes are additive (EM: +4 calls of new FDTD
data; QUANTUM: a code-only reclassification layer on data already being
collected) and neither invalidates the DENSE-CAUSAL block's own reason for
existing — running C60/C70 at all is still the correct, indeed necessary,
step regardless of how the resolution floor and settling gap are handled,
because without that raw data neither gap can even be characterized.
**HALT-AND-REDESIGN is not warranted; PROCEED-WITH-MANDATORY-FIXES is.**

## 5. Budget check — do the fixes fit?

Computed directly from `design_geometry.py`'s own `_cost()` function and
`CPU_S_PER_CALL` table (not estimated by hand, per R4):

| Item | Calls | CPU-s |
|---|---|---|
| Base design (as submitted) | 74 | 5882.3 |
| **EM fix** — Block SETTLE-C60C70: {C60,C70} × {37.2°,41.4°} × 600nm × STEPS=4200, native geometry | +4 | +384.3 |
| **QUANTUM fix** — resolution-floor computation | +0 | +0 (desk arithmetic) |
| **PHOTONICS fix** (recommended, not mandatory this cycle — see §6) — {C60,C70} × {37.2°,41.4°} × 750nm × STEPS=2800 | +4 | +256.2 |
| **New total (mandatory fixes only, EM+QUANTUM)** | **78** | **6266.6** |
| **New total (mandatory + recommended PHOTONICS leg)** | **82** | **6522.8** |

Wall-clock (mandatory-only, 78 calls): `1.15 × 6266.6 / (4×0.98) / 60 =
30.65 min`. 3× envelope = 91.96 min.

Wall-clock (mandatory + recommended, 82 calls): `31.89 min`. 3× envelope =
95.68 min.

**Either way, actual expected wall-clock (≈31–32 min) sits comfortably
inside the proposal's own stated 90-minute hard stop** — the fixes cost
single-digit minutes, not a budget crisis. The only number that needs a
housekeeping correction is the **stated hard stop itself**: at 78 calls the
3× envelope (91.96 min) already exceeds the proposal's declared 90-min hard
stop; with the recommended λ leg it reaches 95.68 min. Per this program's
own convention (exp-069: hard stop set a few minutes past the computed
envelope), **the hard stop should be restated to 100 min** to preserve
that margin under the fixed budget — a one-line text change, not a
capacity problem. Item 7 above (the de-scope docket must name the new
fixes as never-de-scoped) still applies regardless of which hard-stop
figure is adopted.

## 6. Mandatory-fix docket for Phase 3

**MANDATORY (blocking Phase 3 freeze):**

1. **Add Block SETTLE-C60C70** (EM). `C60`/`C70` at θ∈{37.2°,41.4°}
   (the peak angles, not the zero-crossing angles — stronger test than
   mirroring P-069-4's original {39°,40°} choice), 600nm, STEPS=4200 vs.
   the already-planned STEPS=2800 reading at the same cells, native
   geometry (`cell_ratio=1.0`). Score against the identical bands as
   P-069-4/P-071-4 (`rel ≤ 1%` CONFIRM-settled, `rel ≥ 5%` REFUTE-
   unsettled). **Make this a binding precondition on P-071-2** exactly as
   P-071-4 already is — the Combined Verdict's CONFIRM and REFUTE branches
   both require it to CONFIRM-settled, alongside P-071-4. 4 calls, ≈384
   CPU-s.
2. **Compute and disclose, in code, the Rayleigh/Fourier resolution floor**
   for (a) every one of P-071-3's 6 pairwise comparisons, and (b) the
   overall CONFIRM/REFUTE trend bands themselves — not only the REFUTE
   side (QUANTUM's own proposed fix undersold its own reach; extend it to
   both directions per §1 above). Formula: window `Δ(sinθ)` (fixed at
   0.081345 for the 36–42° window) vs. required `Δ(sinθ) =
   1/|1/T(P_a)−1/T(P_b)|` for each pair, with `T(P) = radians(P)·cos(39°)`
   matching `_free_period_search`'s own convention exactly. Any pairwise
   comparison, or the overall trend test, whose observed separation falls
   below its own computed resolution floor must be reported as
   **UNRESOLVED**, folded into the existing NEITHER/gray-zone branch, not
   silently counted toward either CONFIRM or REFUTE. Zero FDTD cost.
3. **Reinstate the `ABSORB`-is-not-a-material caveat** (MATERIALS),
   verbatim or by direct cross-reference to
   `experiments/070-.../phase3_synthesis.md` mandatory-fix 5, and rename
   the CONFIRM branch's parenthetical from "genuine ABSORB-depth-tied
   mechanism" to **"ABSORB-depth-tied numerical-boundary-construction
   effect (not a material/physical mechanism; wavelength-scaling
   undetermined at 600nm-only scope — see idealization on PHOTONICS'
   finding)"**. Zero cost, text only.
4. **Add THERMODYNAMICS' idealization line** verbatim or equivalent: THERMO
   sidecar inapplicable because `ABSORB` is `Sim._damping`'s own
   domain-truncation boundary, no article is run this cycle, and all four
   congruent configs are near-total absorbers at their boundary by
   construction regardless of depth — nothing here re-radiates because
   nothing here is a physical material. Zero cost, text only.
5. **When `run.py` is written, import `_free_period_search` by reference**
   from exp-069's `run.py` exactly as exp-070 did (not re-derived), and
   assert its `(lo_deg, hi_deg, n_grid)` defaults equal `(1.0, 4.0, 400)`
   in code before use (QUANTUM). Zero FDTD cost.
6. **Update the de-scope docket** to name items 1–2 above as never-
   de-scoped, alongside Block G1 and Block DENSE-CAUSAL (Red Team, attack
   7). Zero cost, text only.
7. **Restate the hard stop to 100 min** (from 90 min) to preserve this
   program's own "a few minutes past the 3× envelope" convention under the
   revised budget (Red Team, §5). Zero cost, text only.

**RECOMMENDED, not mandatory this cycle (queue for a fast-follow, not a
blocker):**

8. **PHOTONICS' confirmatory 750nm leg** — {C60,C70} × {37.2°,41.4°} ×
   750nm × STEPS=2800, 4 calls, ≈256 CPU-s. Genuinely strengthens the
   physical-vs-artifact read (attack 6) and fits easily inside budget even
   stacked on top of items 1–7 (82 calls total, ≈32 min wall — see §5) —
   but the mandate (PLAN.md Iteration-48 queue item 1, LOCKED) scopes this
   cycle to the ABSORB-depth causal question at 600nm specifically, and
   the proposal's own idealization 2 already disclosed the 750nm leg as
   "a separate, unranked item, not required by the mandate." Adding it
   would broaden scope beyond what was locked. If capacity allows within
   the (now 100-min) hard stop after items 1–7, run it; if not, defer to
   Iteration 49's queue rather than blocking this cycle's close.

## 7. Checkpoint determination

None of the five criteria in PANEL.md fire. This is not a proven boundary
(criterion 2 — nothing here bounds a mechanism class; T1 is N/A
throughout), not a passing configuration (criterion 1 — constraint 3 is
not engaged), no engine-physics build is implied (criterion 3 — zero
`lab/` diff), and this is not program-integrity drift in the sense
criterion 4 targets (criterion 4) — the two severe findings (settling gap,
resolution floor) were caught within this cycle's own Phase 2, by the
process built to catch exactly this, before any FDTD call was spent on
trusting an uncorrected result. That is the discipline working, not
failing. Two consecutive non-advancing iterations (criterion 5) does not
apply either: Iterations 46/47 both delivered real, verified process
progress against T28 even while PARTIAL, and this cycle is positioned to
narrow T28 further, not repeat a null result.

## 8. Verdict

**PROCEED-WITH-MANDATORY-FIXES.**

The causal design itself — four congruent points on one physical axis,
reusing already-validated machinery, a bit-exact identity gate, an honest
peak-cell resolution extension unprompted beyond the literal mandate — is
sound and worth running; no critique, including my own adversarial read,
found a defect in the underlying experimental logic serious enough to
warrant HALT-AND-REDESIGN. What is not yet safe to trust is the
**interpretation** of P-071-2 without items 1–2 of the mandatory docket:
without a settling-closure check on the two genuinely new configs, and
without a computed resolution floor gating both the CONFIRM and REFUTE
branches (not only REFUTE, as originally proposed by QUANTUM), a clean-
looking CONFIRM or REFUTE this cycle would not be trustworthy — it could
equally be an unsettled transient or a resolution-floor artifact wearing
the shape of a real result, the identical risk shape (R5/R5-addendum) this
program has now caught three times. All seven fixes are cheap (a few
FDTD calls plus text), fit comfortably inside the existing 90-minute
budget once restated to 100 minutes, and require no new `lab/` machinery.
**None of the mandatory fixes are overridden.**
