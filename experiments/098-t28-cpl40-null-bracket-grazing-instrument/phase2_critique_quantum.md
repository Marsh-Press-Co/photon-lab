# Phase 2 Critique — QUANTUM OPTICS seat, Panel Iteration 75

## 1. Steel-man (≤150 words)

Item (v) is well-scoped, zero-marginal-cost validity bookkeeping on an
already-committed *classical* closed-form function, explicitly disclaiming
new physics (Idealization 49). I independently re-derived GP1: `weber(bo,bf)
= bo/bf − 1`, so `C(θ) ≥ −1` follows exactly from `bo ≥ 0` — the claimed
math is right, not asserted. Item (iv)(a)'s correction to Idealization 40 is
independently verifiable and I confirmed it algebraically: `CPL` is
injective over `{R3:30, R4:40, R5:50}`, so `cpl_ok = (CPL[pt["family"]] ==
cpl_frozen)` is mathematically *equivalent* to `family_ok`, not merely
"safe because gated behind it" — my own exp-097 echo was wrong, the
correction is right. FI-G′ (`native_absorb`=41) genuinely catches all three
families' `y_lo`/`y_hi` branch — I hand-verified no rounding collision
(R3: 60→62, R4: 80→82, R5: 100→102). Nothing here smuggles quantum/coherent
-state language into classical wave superposition.

## 2. Sharpest attack (≤150 words)

GP3's stated dichotomy — "symmetrized in source↔observer exchange, or
single-sided (tied only to the observer-side normal)" — is not well-posed
for this geometry. I traced `_geom_derived`: `y_src` and `y_obs` are the
*identical* array, `dy[i,j] = y_obs[i]−y_src[j]`, and `obliquity[i,j] =
d_sp/r[i,j]` with `r=√(d_sp²+dy²)`. Swapping `i,j` flips `dy`'s sign, which
squares away — `obliquity` is symmetric *by construction*, trivially,
because there is only ONE `d_sp` in the whole model: source and observer
planes share one normal direction, so "source-side" and "observer-side"
obliquity were never separately defined in the first place. GP3's code-read
will report "symmetric" — true, but not because a genuine two-sided
inclination factor was checked and found equal; it's a degenerate
consequence of the parallel-aperture setup. The proposal states GP3 as an
open question about *which* construction is used; it doesn't disclose that
the two candidate answers coincide identically here, so the check has less
diagnostic reach than its own framing implies.

## 3. Verdict

**support-with-changes**

## 4. Parameter change that would flip my verdict

None of the above is disqualifying — GP1/GP2/GP3 are zero-cost, non-load-
bearing, and I verified their premises hold. The one change I'd insist on
before this closes: GP3's report must state explicitly that
`_geom_derived`'s single shared `d_sp` makes source-side and observer-side
obliquity identical by construction in this parallel-plane geometry — not
just report "symmetrized" as if a genuine two-sided inclination factor was
tested and passed. Absent that one sentence, a future cycle could cite
GP3's "reciprocity: confirmed" as stronger evidence than the code actually
supports — precisely the R18-class scope-precision failure this cycle's own
item (iv) exists to police, and the one my discipline is asked to watch for
by charter. This is a documentation fix, not a blocking defect; it would
not change my verdict to oppose even if unaddressed, but I would not sign
off on GP3 as "done" without it.
