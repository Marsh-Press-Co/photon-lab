# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 51 · exp-074

*Fresh sub-agent, PHOTONICS charter (surface interaction, absorption
spectra, angular dependence, scattering cross-sections; owns: is the
proposal's optical response coherent as stated, across wavelength and
angle?). Blind to the other six seats' current-cycle critiques.*

---

## 0. Independent re-derivation performed

Ran `desk_check_pricing.py` unmodified: `CHECK0 pass=True worst_rel_err=0.00e+00`,
and every printed table (cond5≈60 at all 4 pairs, `cond9∈[478,529]`,
`VIF_Rq∈[31,37]`, `z_joint∈[0.54,0.81]`, `lev_ratio≈0.80` baseline →
`0.914` at 51°, `L(1.9608°)∈[27.7,28.1]`, `Lpeak≈35–36` at `3.48–3.54°`)
reproduces the proposal's own tables exactly. `CHECK0`/`G0-a` are real
and pass.

I then extended the script (same reused `design_matrix`/`tone_cols`/
`price_pair` formulas, nothing hand-derived) to test the specific
question my charter owns: is the CLOSURE-CONFIRM verdict — and the
binding §6 "independent of which null eventually gates it" retirement
language — actually independent of *which periodic contaminant* is
chosen for the two-tone model, given `L(T)`'s own table says leakage is
comparable-or-worse across ~1.8°–5.0°, not just at 1.9608°.

**Result: it is not independent.** Scanning the assumed second-tone
period `T` from 1.8° to 5.0° in 0.1° steps (holding everything else —
real fitted carriers, all four pairs, phase-fit convention — identical
to the committed script):

| T (deg) | min VIF_Rq (over 4 pairs) | max z_joint (over 4 pairs) | CLOSURE-CONFIRM (VIF≥15, z_joint<1.5, cond9≥300) holds at all 4 pairs? |
|---|---|---|---|
| 1.9608 (proposal's choice) | 31.1 | 0.81 | **YES** |
| 3.48–3.54 (`L(T)` peak) | 19.9–32.0 | 0.56–1.13 | YES (thinner margin) |
| 3.60 | 15.4 | 1.25 | YES (barely) |
| 3.70 | 13.0 | 1.36 | **NO** |
| 4.00 | 8.9 | 1.64 | **NO — z_joint exceeds the 1.5 "closed" ceiling** |
| 4.60–5.00 | 4.9–5.8 | 2.03–2.20 | **NO — z_joint clears the 2σ bar itself, at some pairs, in the CURRENT window** |

And `L(T)` at 4.0° is 31.3 — *larger* than `L(1.9608°)=28.1* — confirming
this is not a cherry-picked edge case: by the proposal's own leakage
metric, 4.0° is an equally-or-more "dangerous" contaminant than the one
it chose to price against, yet the joint two-tone VIF/z_joint calculation
*reverses* there and breaks the closure conclusion.

The reason is a real distinction my charter is positioned to catch: `L(T)`
measures omitted-variable leakage into an *unmodeled* contaminant (single-
tone fit, contaminant absent from the design), while `cond9`/`VIF_Rq`
measure collinearity when that same contaminant is *explicitly added* as
a modeled two-tone column. These are different linear-algebra objects
computed from the same basis, and they do not covary monotonically with
`T` — high leakage-if-ignored does not imply high collinearity-if-modeled.
The proposal's Idealization 4 correctly *names* this gap ("pricing against
one named contaminant is the best case... not the worst") but §6's binding
decision-rule prose does not carry that hedge forward: it states the route
is closed "independent of which null eventually gates it," which is
falsified by the very `L(T)`-band the proposal's own §2f cites as
justification for generality.

---

## 1. Steel-man (≤150 words)

The core machinery is genuinely sound and an improvement on its
predecessors: `CHECK0` anchors every reused formula to exp-072's own
committed basis at machine precision, the pricing runs on the real fitted
carriers of *all four* `ABSORB` pairs (not the one pair EM's informal
Phase-5 note checked), and it correctly separates a design-time leakage
diagnostic (`L(T)`, no data) from a data-conditioned collinearity
diagnostic (`cond9`/`VIF`, real carriers) rather than conflating them in
code. The widened-window phase-sweep (8×8, reporting min/median/max
rather than a single cherry-picked phase) is the right discipline for a
data-free extrapolation, and I verified independently that adding the
disclosed curvature column (Idealization 7's own caveat) barely moves
`VIF_Rq` (≈1.0–1.1× at every width tested) — a real caveat correctly
flagged but not, on inspection, load-bearing against the widened-window
numbers. Zero FDTD, fully reproducible, honestly idealized.

## 2. Sharpest attack (≤150 words)

**§6's binding, program-wide "formal retirement... independent of which
null eventually gates it" is false as stated.** It rests on pricing the
two-tone model against exactly one contaminant period (T21's 1.9608°
fringe). Re-running the identical, already-committed pricing formulas at
contaminant periods from 3.7°–5.0° — squarely inside `L(T)`'s own claimed
danger band (1.8°–5.0°), and at 4.0° a period `L(T)` itself scores as
*more* dangerous than 1.9608° (31.3 vs 28.1) — makes CLOSURE-CONFIRM's own
pre-registered bar fail: `VIF_Rq` drops as low as 4.9 and `z_joint`
(optimistic) climbs above the proposal's own 1.5 "closed" ceiling, and
above 2σ itself at some pairs (~4.6°–5.0°), in the *current, unwidened*
36°–42° window. A permanent, sixth-cycle-ending retirement of a
five-cycle sub-thread should not ride on a conclusion that reverses under
a same-band, comparably-motivated choice the proposal itself flags as
untested (Idealization 4) but does not scope §6's own language against.

## 3. Verdict

**Oppose** — specifically the §6 pre-committed formal-retirement rule as
written; the underlying `desk_check_pricing.py` machinery, `CHECK0`, and
the per-pair/widened-window tables (§2b–2f) should be kept and are worth
citing on their own, narrower terms.

## 4. Single parameter change that would flip my verdict

Rescope §6's claim from "independent of which null eventually gates it"
to an explicit, contaminant-period-bounded statement — e.g. "closed for
any single named contaminant with period ≤~3.6° at 36°–42°" — and require
the CLOSURE-CONFIRM band to be re-evaluated (as I did above, reusing the
committed script) across the full `L(T)`-claimed danger band before any
formal-retirement language is adopted. If CLOSURE-CONFIRM is re-verified
to hold (or the retirement claim is honestly narrowed) across that full
band, or if the 3.7°–5.0° sub-band is independently argued to be
implausible as a real optical contaminant (distinct from being merely
inside `L(T)`'s abstract linear-algebra table) with cited reason, I would
move to support-with-changes.
