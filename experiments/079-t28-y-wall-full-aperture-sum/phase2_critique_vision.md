# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 56 (exp-079)

*Fresh sub-agent, blind to the other five seats' critiques this cycle.*

**Charter note, stated plainly, matching this sub-thread's own established
precedent (exp-078's own VISION critique):** T28 is instrument/model-fidelity
work — no absorber, no switch, no ambient scene, no constraint-3 claim
anywhere in this file (§2's own "T1 escape route: N/A," correctly stated). My
charter has no perceptual threshold to pin here. What follows is this seat's
other standing duty: auditing whether the numbers this proposal compares are
actually commensurate (R9), and whether the write-up's own framing of what it
found is an accurate, legible characterization of the result — not inflated,
not softened.

## R4 reproduction (independent)

Ran `python3 y_wall_aperture_sum.py` myself from the experiment directory.
`_output.txt` diffs against my run at exactly one line (`elapsed: 2.2s` vs
`2.3s` — timing noise); every printed number and the full JSON are otherwise
identical, and re-running left `y_wall_aperture_sum_results.json` unchanged
(bit-identical on the fields I checked). I did not stop at re-running the
script — I independently recomputed the T21 fringe period from primitives
myself, outside the script: `degrees(CPL[600] / (752·cos(radians(39))))` with
`CPL[600]=20` cells read from `boundary_reflectance.py`, giving
`1.9607950099405438°`, matching the JSON's `t21_fringe_period_A752_600nm_
39deg` to every printed digit. I also hand-verified the `rel_dev` arithmetic
behind the headline "1.6%–3.5% from T21 / 28.6%–56.8% from T28" claim
directly from the JSON's own raw `p_model_deg` values — both ranges
reproduce. I also read `lab/fdtd2d.py::Sim.add_line_source` myself and
confirmed the raised-cosine taper and `k·sinθ·(y−0.5(y_lo+y_hi))` driven-phase
formula the script re-derives (§3.2/§3.3) match that function's actual code,
not a paraphrase of it. No hand-typed number found anywhere in
`phase1_proposal.md`.

## Commensurability audit (R9 lens)

- **`rel_dev` (period vs. period): commensurate**, identically to exp-078's
  own clean finding — both operands are best-fit periods in degrees-of-θ from
  the same imported `_free_period_search`/`free_period_with_widening`
  machinery, applied to real and model curves alike. This holds for both the
  T28-target comparisons (§5.3/§5.4) and the T21-fringe comparison (§5.3's
  right-hand column, §6a) — same statistic, same units, both computed by the
  identical code path. No T16-shaped mismatch anywhere.
- **`ss_tot` ratio (§5.2/§6c): legitimately comparable to exp-078's own
  figure** — both are `sum((y−mean(y))²)` on a proxy curve in that curve's
  own native units, and I confirmed the `SS_TOT_DEGENERATE_FLOOR=1e-20`
  absolute-floor guard is *reused*, not *rescaled*, from `y_wall_prescreen.py`
  unchanged. I checked this is not silently miscalibrated for this file's
  different amplitude scale (its `Re{E_echo}` curves run ~10⁻⁶–10⁻⁵, not
  exp-078's O(1) `cos(Δφ)` proxy): this model's own float-noise floor for a
  genuinely flat curve at this scale would sit near `(10⁻⁶·10⁻¹⁶)²·31 ≈
  10⁻⁴³`, twenty-three orders below the fixed `10⁻²⁰` floor, so the reused
  threshold still cleanly separates noise from the measured `6.05×10⁻¹¹` here
  — correct by a wide margin, though worth flagging for whoever reuses this
  floor on a model whose scale sits closer to it.
- **R²=0.97–0.98 (§5.5, solo per-config curves): consistent with, not
  cherry-picked away from, the pair-delta fits** — I recomputed the
  pair-delta model R² directly from the JSON (`primary_proxy_re.*.r_squared`
  = 0.972/0.968/0.973), which the write-up does not print in §5.3's table but
  which match the cited 0.97–0.98 range closely; nothing is hidden.

## Steel-man (≤150 words)

This is a clean, correctly-scoped generalization of exp-078's single-edge
model to the full coherent aperture sum, exactly as the reconciled ranking's
Tier-0 item 1 asked. Every governing formula (per-point bounce angle,
raised-cosine taper, driven-phase ramp) is re-derived from `add_line_source`'s
actual source, not assumed — I independently checked the taper and phase
formulas against `lab/fdtd2d.py` myself and they match exactly. The
vectorized reflectance re-implementation is validated bit-exact against the
already-gated scalar function before use, gates are re-run at the full,
never-before-sampled 4.77°–15.5° envelope, and a genuine 1x/2x/4x
numerical-convergence check passes cleanly (`<0.002%` at 2x→4x). R4: I reran
the script myself — byte-identical modulo timing — and independently
recomputed the T21 fringe period from primitives, matching to every printed
digit. The self-scored verdict correctly treats its own one marginal SUPPORT
with real skepticism rather than claiming it.

## Sharpest attack (≤150 words)

§4/§7's headline — "neither branch... a third, sharper outcome not named in
either of the ranking's own two branches" — overstates its own novelty. The
ranking's branch (b) was literally: "if it does NOT generalize... that IS the
discovery of genuine θ-dependence... and would justify the full build." This
result matches that premise *and* its first consequence exactly. What
differs is only whether the dependence argues FOR building further —
answered via the SAME "near-identical frequencies difference to a third at
that frequency" logic T28's founding argument used to rule out "T21 fringe,
differently weighted" for the real data. That is branch (b), refined, not a
result outside the framework. A reader skimming §4 takes away more novelty
than the finding earns; §7's own prose is more careful than its label —
exactly the framing-accuracy question this seat exists to catch before it
becomes settled Iteration-56 language.

## Verdict: **support-with-changes**

The derivation, code-reuse, gating, and convergence discipline are all sound
and I could not find an R9-shaped defect anywhere in this file's comparisons
— a genuine improvement in care over some of this sub-thread's earlier
cycles. The physical finding itself (the flat single-edge result does not
survive generalization to the full aperture, but the recovered oscillation is
mechanistically T21's fringe, not a T28 match) is real, well-supported by the
per-config solo-curve diagnostic, and narrows the T28 board honestly. Two
changes before this is cited as settled record:

1. **Retitle the "third, sharper outcome" framing** in §4 and the top of §7
   to state plainly that this is branch (b) of the reconciled ranking's own
   two-way framing, refined by an already-precedented mechanism (T21-fringe
   re-emergence) — not a category outside it. This is a wording fix, not a
   re-run.
2. **The one nominal Test-A SUPPORT (`C80−C40`, `rel_dev=0.2857`, primary
   proxy) should not survive into Phase 3 as informative** without the R5
   null-permutation control the proposal itself already flags as
   outstanding (§4's R5 disclosure, §7's own "read with real skepticism").
   The proposal's own reasoning for discounting it (closer to T21's
   frequency than to its own nominal target, the same "compromise fit"
   shape as this program's Iteration-47 precedent, P-070-1) is sound, but a
   disclosed gap that sits directly under this cycle's only nominal SUPPORT
   should be a stated Phase-3 precondition, not left as a paragraph for a
   future cycle to remember.

Neither issue changes the data or the recommended next step (do not build the
full non-reduced propagator on this evidence); both are about how precisely
this cycle's own language should be trusted once it enters LOGBOOK.

**What would flip this to outright SUPPORT:** wording fix #1 done, and #2
either resolved (null-permutation control run, however it comes out) or
explicitly deferred to Phase 3/4 by name rather than left implicit.

**What would flip this to OPPOSE:** nothing found this cycle — no
incommensurable comparison, no unreproduced number, no failed gate. If a
null-permutation control (item 2) later showed the `C80−C40` SUPPORT clears
at a rate indistinguishable from chance over this comparison space *and* the
write-up's overstated framing were left uncorrected into a future cycle's
citation of this result, that combination would move me to oppose that
future citation — not this proposal as filed.

**Single parameter change that would flip my verdict:** none needed — this
is already support-with-changes, and the changes are textual/procedural
(rephrase §4/§7's framing; name the null-permutation control as a Phase-3
precondition), not a recomputation. Nothing about the underlying `y_lo`,
`y_hi`, `ABSORB`, or grid parameters is in question.
