# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 47

Seat charter (verbatim): field/wave behavior, impedance matching, energy
coupling. Owns the reciprocity / passivity / causality bookkeeping —
formalizes what T1 permits and forbids for each proposal.

Reviewing: `experiments/070-t28-mechanism-desk-check-batch/phase1_proposal.md`
(QUANTUM OPTICS lead).

## Steel-man (150 words)

A genuinely disciplined, zero-marginal-cost, R4-compliant reuse of
already-committed data (`exp-069/results.json`) and already-verified
statistics (`_fixed_period_fit`/`_free_period_search`, imported not
re-derived) against already-named geometric constants
(`exp-065/design_geometry.py::CONFIGS`) — nothing hand-typed, no new FDTD
call, closing the standing Red-Team tripwire at literally zero risk. It
correctly declines Checkpoint-2 candidacy, states real falsifiable bands
per sub-item, and is honest where it should be: Idealization 6 explicitly
flags that the beat formula assumes linear two-tone superposition and
would not apply if the true mechanism is a non-additive envelope;
Idealization 4 flags the `R_OUT`/`W_OBJ` degeneracy this batch cannot
break. Item (e) — checking whether (b)'s beat-derived `A_alt` and (d)'s
directly-traced `A_eff` name the *same* combination — is a free,
legitimate corroboration step neither search alone provides. Well-scoped,
honestly bounded.

## Sharpest attack (149 words)

Item (a)'s CONFIRM band — `R²_free(C40)≥0.30 AND R²_free(C80)≥0.30`,
applied to the RAW `C_empty(θ)` curves, not a residual after removing
T21's own established fringe — will almost certainly fire regardless of
whether the ~2.84° family is present at all. This program's own record
(exp-066: fixed-period `r²(c*)` 0.7852→0.8271 at settled STEPS) shows
`C(θ)` individually is already dominated by T21's ~1.96° fringe at R² far
above 0.30. A free search over `[1°,4°]` will lock onto that known,
strong period, not discriminate whether a *distinct* 2.84°-family
component also lives there — the pass/fail table (§9) scores R² alone,
never the recovered period. Item (a) is reordered to run first precisely
because it "sharpens how to read (b)/(d)" (§4) — but as built it cannot
fail to CONFIRM, making the config-invariant-vs-ABSORB-tied discriminator
decorative, not decisive, at the exact step the proposal leans on hardest.

## Verdict: **support-with-changes**

## Parameter change that would flip to unconditional support

Score P-070-1 on the *recovered period*, not bare R²: CONFIRM requires
`|P*_free(C40)−P*_delta|/P*_delta ≤ 20%` AND same for `C80` (matching the
tolerance convention already used in P-070-2/3/4) — or, better, fit each
raw curve as a two-term model (T21's fixed `P(39°,600nm)=1.9608°` term
plus one free secondary term) and score the secondary term's own R²
contribution, not the single-cosine free fit's total R². Either change
makes item (a) capable of REFUTE on real data instead of confirming by
construction.

(Beat-frequency algebra, item b: flagged as a secondary concern, not the
verdict-flipper — `1/P_beat=|1/P_a−1/P_b|` is the correct envelope
relation only when `delta(θ)` is genuinely well-modeled as a difference
of two comparable-amplitude, well-separated-frequency sinusoids in the
*same* metric; at `P_A≈1.96°` and candidate `P_alt` both order-1° over a
6°/~3-period window, "well-separated" is not obviously true, and
Idealization 6 already discloses this — adequately hedged, not a gate.)
