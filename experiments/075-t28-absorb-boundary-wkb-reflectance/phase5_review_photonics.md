# PHASE 5 — REVIEW · PHOTONICS seat · Panel Iteration 52 (exp-075)

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat 1: surface interaction,
absorption spectra, angular dependence, scattering cross-sections — is the
proposal's optical response coherent as stated, across wavelength and
angle?). Fresh context — this is NOT a continuation of my own Phase-2
critique from memory; I have re-read the full cycle record from scratch and
judge the result independently. Blind to the other five Phase-5 reviewers
and to Red Team's own Phase-5 final audit.*

---

## Verdict: **PARTIAL**

Both tested boundary-reflectance-echo mechanisms (single-`-x`-wall echo,
`phase1_proposal.md`; the correctly-derived two-wall cavity,
`phase3_synthesis.md`/`two_wall_cavity.py`) are REFUTEd under the model's
committed phase convention, and that process — an exact transfer-matrix
derivation, a passivity-adjudicated sign resolution disclosed in full, three
independent sanity gates, a mandatory look-elsewhere/robustness check on the
cavity variant's nominal Test-B SUPPORT — is genuinely well-executed
PHOTONICS work, the cleanest cycle this six-plus-cycle T28 sub-thread has
produced. I would not overturn REFUTE **for the mechanism as computed under
the convention this cycle adopted.**

But this is not a clean PROMISING-that-REFUTE-closes-the-mechanism-space
result, and not a clean RULED OUT of boundary-reflectance-echo physics as a
class either. My own independent re-verification (below) finds that the
Combined Verdict REFUTE is **not, in fact, independent of the cross-module
phase-convention question** that EM's Phase-2 critique flagged and that
Red Team's audit and Phase 3 both left as "informational, bind forward, not
this cycle" — a disposition that rested on EM's own claim (never actually
tested against Test A by anyone in this cycle's record) that Test A's
REFUTE is "robust to everything." It is not. Under the one concretely-named
alternate convention (`r → conj(r)`, the exact candidate fix EM already
applied to Test B), **Combined Verdict moves from REFUTE to INCONCLUSIVE for
both models** — never to SUPPORT, but genuinely out of REFUTE. This is a
real, load-bearing gap in this cycle's own robustness reasoning, not a
reason to distrust the mechanism finding's substance; it is the reason this
cycle's own "narrows the remaining space" framing needs one more caveat
before it is fully earned. Full derivation below.

---

## Independent re-verification (R4 — recompute, don't restate)

**Reproduction, first.** I ran `boundary_reflectance.py` and
`two_wall_cavity.py` unmodified: both reproduce every number in the
committed record bit-exactly (`rel_period_dev=4.2778`, `shape_r²=0.2586`,
`P_model=15.0000°` for the single-wall model; `rel_period_dev=4.2778`,
`shape_r²=0.3042`, circular-shift `p=0.1953` for the two-wall model; all
three sanity/passivity gates PASS as recorded). I also read `lab/fdtd2d.py`
lines 72–264 directly and confirmed the two claims my own charter cares
about most: (a) `Ez[1:-1,1:-1]` is the only slice the curl step ever
touches — both domain edges are PEC by construction, exactly as both models
assume; (b) `Hx`/`Hy` are damped immediately after their curl update
(before being used to update `Ez`), and `Ez` is damped after source
injection — the symmetric-E/H-loss claim underlying the matched-`ε=μ`
admittance (Idealization 2) is correct, not assumed.

**What I independently tested that no prior step in this cycle's record
did.** EM's Phase-2 critique (§0/§2) tested `r → conj(r)` — "the obvious
candidate fix" for a possible cross-module phase-convention mismatch
between `reflection_coefficient()` and `dg048.field_and_h`'s own
convention — **against Test B only** (single-wall model: `r` goes from
`−0.5085` to `−0.5422`, sign unchanged), and concluded from that one check
alone that "Test A's REFUTE... is set by the fixed, measured geometric
quantity `PLANE_X`, not by any loss-model detail — that part of REFUTE is
robust to everything below." Red Team's audit (§6) adopted this claim
verbatim as one of three pillars supporting "REFUTE... stands — robustly,"
and Phase 3 (§1, item 5; §3.4) accordingly filed the cross-module
phase-convention gap as "informational only this cycle... not required to
ship with [the cavity model]." **Nobody in this cycle's five critiques, the
Red Team audit, Phase 3, or Phase 4 actually ran Test A under `r →
conj(r)`.** G-PASSIVITY cannot substitute for this check — `|conj(r)| =
|r|` identically, so the passivity gate is structurally blind to this exact
ambiguity, which is precisely EM's original point (§2c: "nothing gates
whether the resulting phase is consistent with the separately-authored
exp-048 propagator").

I built an independent script (not a patch to the committed pipeline) that
imports only the individually-vetted primitives — `reflection_coefficient`,
`c_empty_with_wall`, `c_empty_two_wall`, `damp_e_profile`/`nu_profile`/
`n_profile_exact`, and the real `_free_period_search` from
`experiments/069/run.py` — and reruns **both** models' full numeric
interference calculation (not the phase-free closed form) with `r →
conj(r)` substituted everywhere `r(θ;ABSORB)` enters, then re-scores Test A
and Test B on the identical pre-registered bands:

| Model | Convention | `P*` | `R²` | widened-search `P*` | rel. period dev | Test A | Pearson `r` (`r²`) | Test B |
|---|---|---|---|---|---|---|---|---|
| single-wall | committed (as run) | 15.0000° | 0.8587 | 60.00° [boundary] | 4.278 | REFUTE | −0.5085 (0.2586) | INCONCLUSIVE |
| single-wall | `r→conj(r)` | **3.9260°** | 0.5825 | 3.92° [**interior**] | **0.381** | **INCONCLUSIVE** | −0.5422 (0.294) | INCONCLUSIVE |
| two-wall | committed (as run) | 15.0000° | 0.9062 | 60.00° [boundary] | 4.278 | REFUTE | −0.5516 (0.3042) | nominal SUPPORT* |
| two-wall | `r→conj(r)` | **4.1211°** | 0.5823 | 4.12° [**interior**] | **0.450** | **INCONCLUSIVE** | −0.5403 (0.292) | INCONCLUSIVE |

*already shown by the mandatory circular-shift null (p=0.195) not to be
statistically distinguishable from chance — the committed record's own
finding, unaffected by this table.

**Under the committed convention, the model's own predicted curve never
completes even a third of an oscillation across the 6°-wide dense-sweep
window at any period tested (1°–60°) — QUANTUM's/Red Team's own correct
diagnosis of a boundary-search artifact, which I independently confirm.
Under the one concretely-tested alternate convention, this is no longer
true for either model**: the free-period search finds a genuine interior
maximum (confirmed by widening the search window from 15° to 60° and
getting the identical answer both times, ruling out a second boundary
artifact) at `P*≈3.9–4.1°` — 38–45% off `P*=2.8421°`, landing in the
**INCONCLUSIVE** zone of Test A's own pre-registered band (`SUPPORT≤0.30`,
`REFUTE>1.00`), not REFUTE. Test B, under the same alternate convention,
sits at `r²≈0.29` for both models — just under the `0.30` SUPPORT bar,
also INCONCLUSIVE (not REFUTE, not SUPPORT). **Applying the cycle's own
pre-registered combining rule (`REFUTE if EITHER test REFUTEs; SUPPORT only
if BOTH SUPPORT; INCONCLUSIVE otherwise`) under this alternate convention:
Combined Verdict is INCONCLUSIVE for both the single-wall and two-wall
model — not REFUTE.**

**What this does and does not establish.** This is not evidence the
mechanism is real — under neither convention does either model reach
SUPPORT on either test, and the shape correlation stays wrong-signed
(negative) under both conventions throughout, for both models. I am not
overturning REFUTE as the better-supported reading; the committed
convention is the one the model's own passivity gate and this program's own
process actually adopted, and I found no independent physical argument (nor
did EM) for preferring the conjugate over it. What this independently
establishes is narrower and still consequential: **the specific claim that
licensed treating the cross-module phase-convention gap as merely
"informational, bind forward" rather than mandatory-before-REFUTE-is-final
— "Test A's REFUTE... is robust to everything below [the phase-convention
issue]" — is false as stated.** Test A's REFUTE is robust to the
loss-branch (`n`) ambiguity (resolved by passivity, a genuinely different
and correctly-closed question) but is **not** robust to the one concretely
named, structurally-ungated phase-convention alternative. The correct
scope for this cycle's REFUTE is "REFUTE under the model's adopted,
passivity-selected, but externally-unverified phase convention against
`dg048`'s propagator" — a real, honest, still-informative result, but one
notch less final than "REFUTE, full stop" as currently written.

---

## Ranked top-3 Iteration-53 candidates (PHOTONICS charter)

**1. Close the cross-module phase-convention gap directly, now that it is
shown outcome-determining, not merely a documented loose end.** This is
what my own finding demands as the next move, and it sits squarely inside
this seat's charter (is the optical response — a reflectance phase,
specifically — coherent as stated?). The right test is not another
closed-form substitution or another candidate-fix guess: build a small,
genuinely independent measurement of `r(θ;ABSORB)`'s own phase from the
real engine — a short, few-angle `Sim.run()` (cheap: a handful of steady-
state CW runs at the `-x`-wall geometry alone, no full ambient-contrast
pipeline needed) that extracts the reflected wave's phase directly from the
standing-wave pattern in the vacuum region between source and band, and
compares it against `reflection_coefficient()`'s own predicted phase at the
same angles. This resolves, from first principles rather than by
elimination, whether the committed convention, its conjugate, or neither is
correct — closing the exact gap Red Team's own audit (§2c) named as
"genuinely open" and this review shows is not safely deferrable. I rank
this #1 over PLAN.md's own queued items because it is the one item that
changes what this cycle's own headline finding is allowed to say, and it
is cheap (a handful of FDTD calls at most, not a new instrument class).

**2. PLAN.md's queued G40/`PAD` decorrelation (~31 calls) — still the right
#2, unchanged by this cycle's result.** This item is orthogonal to
everything the boundary-reflectance-echo work (exp-075) or the retired
differential-fit work (exp-072–074) touched: it relieves, rather than
merely discloses, the standing `PAD = ABSORB − 40` confound that has sat
underneath every congruent-series causal claim since Iteration 48 (LOGBOOK,
Iteration 48/exp-071). Nothing in this cycle's REFUTE (either reading)
narrows or widens the case for running it — it remains the only queued item
that actually builds new, decorrelated data rather than re-analyzing what
exists, and T28's mechanism question is still open regardless of how item
1 above resolves.

**3. Record-hygiene bundling (PLAN.md queue item 3), expanded to include
this review's own finding.** Before either mandatory-fix docket from this
cycle (Phase 2's five items, already applied) or a future cycle's citation
of "T28: two boundary-reflectance-echo mechanisms REFUTEd" gets reused,
the permanent record should carry the convention-dependence caveat this
review establishes — not as a retraction (the committed-convention REFUTE
stands, and no one has shown the conjugate convention is the correct one),
but so a future LOGBOOK citation does not read this cycle's REFUTE as more
convention-independent than it is. This is a same-cost bundle with the
already-queued hygiene item, not a new workstream.

---

## Seat-specific finding a general-purpose read would miss

The single clearest domain-specific catch here is optical, not
statistical: **a reflected wave's own angle-dependent phase, `arg(r(θ))`,
is exactly the kind of quantity that can set an effective fringe period in
a coherent two-path interference measurement — this is ordinary thin-film/
Fabry–Pérot optics, not an exotic effect.** `arg(r(θ;ABSORB=40))` swings
from `−78.1°` at `θ=36°` to `−1.2°` at `θ=42°` in the committed record's
own §2d table — a ~77° swing across the same 6° window whose *geometric*
phase term (`2k·cos(θ)·PLANE_X`) swings by a comparable ~180°. These two
angle-dependent phase contributions are the same order of magnitude, not
one dominant and one negligible. EM's Phase-2 critique tested the
`r→conj(r)` question only against Test B and, from that single check,
generalized to a claim about Test A ("independent of... any loss-model
detail") that a photonics-trained check of the interference formula itself
would have flagged as needing direct verification before being relied
upon — precisely because reflected-phase dispersion contributing to a
fringe's effective period, alongside the geometric path-length term, is
first-semester interferometry, not a subtle effect a general-purpose
statistical read would think to distrust. This cycle's process caught the
loss-branch sign ambiguity correctly (passivity, not curve-fitting) and
disclosed it in full — genuinely good practice — but let an analogous,
still-open phase question get filed as a footnote on the strength of a
claim that was never checked against the test it was invoked to protect.
