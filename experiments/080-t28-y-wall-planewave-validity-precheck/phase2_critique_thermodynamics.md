# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 57 · exp-080

**Seat: THERMODYNAMICS** (where absorbed energy goes; owns the per-proposal
energy sidecar — absorbed power → temperature rise → emission band →
detectability; always asks what re-radiates and whether it would be
detectable). Blind to other seats' Phase-2 critiques this cycle.

---

## 0. Independent verification (numbers computed fresh, not asserted)

Squaring the already-committed `r_theta_eff_primary`/`r_theta_eff_secondary`
values in `validity_precheck_results.json` gives the reflected-power
fraction `|r(theta_eff)|²` this pre-check's own machinery already implies,
at its own `theta_eff` (~8°, the amplitude-weighted geometric bounce-angle
summary of the 5.3°–15.0° `theta_local` envelope):

| cfg | `|r|` (primary) | `|r|²` (primary) | `|r|` (secondary) | `|r|²` (secondary) |
|---|---|---|---|---|
| C40 | 9.925e-05 | 9.851e-09 | 1.022e-04 | 1.045e-08 |
| C60 | 2.544e-06 | 6.474e-12 | 2.439e-06 | 5.951e-12 |
| C70 | 1.287e-06 | 1.656e-12 | 1.135e-06 | 1.288e-12 |
| C80 | 6.883e-07 | 4.737e-13 | 6.008e-07 | 3.610e-13 |
| G40 | 1.0146e-04 | 1.0294e-08 | 1.0395e-04 | 1.0806e-08 |

This alone would say: negligible, 8–13 orders of magnitude below unity,
nowhere near mattering to constraint 3's energy budget or to any Weber-
contrast detection floor (~1%). But `theta_eff` is a purely geometric
quantity — `theta_local(y_s)=atan(D_SP/(OBJ_Y+y_s))` — with **zero
`theta_beam` dependence** (confirmed directly in `y_wall_aperture_sum.py`,
`theta_local_deg`'s own docstring line 163–165 and `echo_field_curve`'s
`r_vec_cache` comment line 258–259: *"r(theta_local(y_s)) does NOT depend on
theta_beam"*). PHOTONICS' own not-yet-built §4 construction, and Red Team's
original standing suggestion (exp-079 §7 Tier-0 item 1), price
`r(90°−θ_beam)` — a **structurally different angle argument**, evaluated at
the *swept beam angle*, not this pre-check's static geometric summary.

I recomputed `|r|²` at that actual argument, same `br.reflection_coefficient`
call, same per-`ABSORB` index profiles, over the θ_beam range this whole T28
sub-thread's own committed curves already use (`36°–42°`, `results.json`
`headline.theta`, 31-point grid — the same array `validity_precheck.py`
itself imports for part (b)):

| ABSORB | θ_beam=36° → arg=54° | θ_beam=39° → arg=51° | θ_beam=42° → arg=48° |
|---|---|---|---|
| 40 | `\|r\|²=1.494e-03` | `\|r\|²=6.200e-04` | `\|r\|²=2.482e-04` |
| 60 | `\|r\|²=5.115e-05` | `\|r\|²=1.741e-05` | `\|r\|²=6.358e-06` |
| 70 | `\|r\|²=1.316e-05` | `\|r\|²=4.089e-06` | `\|r\|²=9.372e-07` |
| 80 | `\|r\|²=3.569e-06` | `\|r\|²=6.034e-07` | `\|r\|²=4.099e-08` |

Two to five orders of magnitude larger than the pre-check's own reported
numbers, still sub-1% at every point checked (worst case `0.149%`, ABSORB=40
at θ_beam=36°), and growing monotonically as `ABSORB` thins and as `θ_beam`
moves toward grazing (spot-check at `θ_beam=0°→arg=90°`... not evaluated,
but the 30°→60° sweep from-normal I ran separately shows `|r|²` climbing to
`0.73%` (ABSORB=40) by 60° from normal and continuing upward toward grazing
— the eventual full flashlight-sweep phenomenon is NOT confined to
36°–42°).

## 1. Steel-man (≤150 words)

The pre-check's scope discipline is defensible on its own terms. Parts (a)
and (b) fully answer the two questions frozen in `phase1_proposal.md` §4,
and neither question is an energy-budget question — this cycle's own
charter (ELECTROMAGNETISM, lead) owns reciprocity/passivity/causality
bookkeeping, not the THERMODYNAMICS sidecar. The `r_theta_eff` values in
the JSON are a byproduct of the reproduction test, not offered as a priced
energy number, and treating them as such risks answering the standing
suggestion at the wrong angle (exactly what §0 above shows). Deferring the
actual `1−|r(90°−θ_beam)|²` pricing to PHOTONICS' own build — where
`θ_beam` is a real, swept, load-bearing variable rather than a borrowed
static proxy — is arguably the *more* rigorous sequencing, not a dropped
obligation, since pricing it here would price the wrong argument.

## 2. Sharpest attack (≤150 words)

The write-up should not have been silent on this. `1−|r(θ_beam)|²` costs
nothing beyond what's already computed (`br.reflection_coefficient`,
already imported, already gated) and the ingredients — per-`ABSORB` index
profiles and the sub-thread's own `36°–42°` θ_beam grid — are already
sitting in this file's own dependency tree. Computed at the argument the
suggestion and PHOTONICS' §4 actually target (`90°−θ_beam`, not
`theta_eff`), `|r|²` runs `2.5e-4` to `1.5e-3` for ABSORB=40 (§0 table) —
still sub-1%, but **5 orders of magnitude larger** than the `~1e-8`
`theta_eff`-based number this pre-check's own JSON contains. A reader who
sees "negligible" numbers already sitting in `validity_precheck_results.json`
and concludes the standing power-budget question is answered would be
wrong: it's answered at a different angle, by ~5 decades.

## 3. Verdict: **support-with-changes**

Parts (a) and (b) are sound: I found no defect in the Fraunhofer/spread
arithmetic or the R² scoring, and the FORECLOSE/INCONCLUSIVE verdicts stand
up. The change I ask for is an addition, not a retraction: append the
`|r(90°−θ_beam)|²` table above (or equivalent, computed the same cheap
way) to this file before Phase 3, labeled explicitly as evaluated at the
swept-beam argument PHOTONICS' construction will actually use, distinct
from `theta_eff`'s geometric summary. Substantively this *strengthens* the
recommendation to proceed (worst case found, `0.15%` at the sub-thread's own
established θ_beam window, is still two orders of magnitude under a Weber-
contrast floor), but it should be said in those terms, with those numbers,
rather than left to be inferred from a JSON field computed for an unrelated
purpose. This is a one-paragraph, zero-FDTD addition — cheap enough that
deferring it costs more in future confusion than doing it now.

**On the C70/C80 negative `R²(abs)` — a partial thermodynamic reading,
not purely a curve-fitting artifact.** The write-up's algebraic explanation
(a fixed complex multiplier can shift zero-crossings, and `|·|` amplifies
that) is correct but incomplete. I checked how much `|r(theta_local(y_s))|`
itself varies across each config's own `[5.3°,15.0°]` envelope (same
`br.reflection_coefficient`, sampled at 5°/8°/10°/15°): for ABSORB=40/G40 it
is nearly flat (`9.3e-5`→`1.1e-4`, a `1.2×` swing); for ABSORB=70/80 — the
two configs with the pathological `R²(abs)` — it swings **7.5×–9×**
(`5.7e-7`→`4.3e-6` at ABSORB=70; `2.7e-7`→`2.5e-6` at ABSORB=80) across the
*same* aperture the fixed-angle model is asked to summarize with one
number. That is a real, angle-dependent energy-coupling effect distinct
from the phase-algebra point: precisely the two configs whose true
per-point *reflected-power* fraction varies by close to an order of
magnitude across the aperture are the two where a single frozen `r` fails
worst. No non-conservation is implied (`|r|≤1` holds throughout, G-PASSIVITY
untouched), but "zero energy content" oversells the algebra-only account —
recommend one added sentence noting this correlation.

## 4. Parameter change that would flip this verdict

None found that would flip it to **oppose**. It would flip to plain
**support** (no changes requested) if `phase1_proposal.md` already stated,
anywhere, that its `r_theta_eff` values are evaluated at a geometric angle
structurally distinct from PHOTONICS' `90°−θ_beam` argument and are
therefore not a substitute for pricing the latter — i.e., if the
distinction in §0/§2 above were already on the record rather than left
implicit in Idealization 2's more abstract framing. It is very close to
already being there; this critique asks for the numbers, not a new idea.
