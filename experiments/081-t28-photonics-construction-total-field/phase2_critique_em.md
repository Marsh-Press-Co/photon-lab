# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 58 · exp-081

*Fresh sub-agent, blind to the other six seats' Phase-2 critiques this cycle.
Read PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE
THREADS including T28's full Iteration 46–57 history), PLAN.md's Iteration-58
queue, exp-081's `phase1_proposal.md`/`photonics_construction.py`/
`phase1_results.json`/`_output.txt`/`NOTES.md` in full, exp-080's
`phase1_proposal.md`, `validity_precheck.py`, `phase3_synthesis.md`,
`phase5_review_em.md` (my own seat's immediately-prior review this cycle
inherits from), `phase5_redteam_audit.md`, and `lab/validation/run_all.py`'s
gate pattern. Independent verification performed below, not asserted from
memory: I re-ran `photonics_construction.py` myself from the committed repo
state and reproduced every number in this critique bit-exact against
`phase1_results.json`/`_output.txt`.*

---

## 1. Steel-man (≤150 words)

This cycle finally builds and scores what PHOTONICS actually specified —
both terms present — closing a two-cycle-old gap (exp-080's `part_d` omitted
`E_direct` and scored by the wrong method). The cancellation claim is not
merely asserted: item 1a re-verifies PHOTONICS' proof bit-exact (`0.0`
across all 5 configs, all 31 angles — the fourth independent confirmation),
and item 1b honestly reports the `~10⁻¹⁴` residual as a **refutation of the
literal pre-registered "0.0" claim**, then correctly traces it to
floating-point subtraction of two analytically-equal `O(100)` quantities
rather than smoothing it into a pass. That is exactly the right EM
reasoning: a coherent sum of a non-wall-interacting direct term and a small
wall-echo term must cancel exactly in a pair-delta between two configs that
share the direct term, by linear superposition alone — and the write-up
proves this rather than assuming it, then correctly declines to overclaim a
"bit-identical" result it can't literally produce in floating point.

---

## 2. Sharpest attack (≤150 words)

Item 2's three re-run gates (G-LOSSLESS, G-N1, G-PASSIVITY) genuinely PASS
at `[47.5°,54.5°]` — I reproduced `2.220×10⁻¹⁶`/`3.140×10⁻¹⁵`/`0.041413`
bit-exact by re-running the script, and `0.041413` is consistent with Red
Team's own prior `0.038656` at the narrower `[48°,54°]` (monotonic widening,
correct direction). But this exact three-gate battery is what this
program's own **R8** rule (exp-075, Checkpoint-4-fired) proved
**algebraically blind** to the `r→conj(r)` phase-convention ambiguity:
`|conj(r)|=|r|` identically, and a "direct-formula" comparison sharing the
same assumed sign convention as the "loop" formula can't catch a globally
wrong one either. The *only* check that ever resolved that ambiguity —
`phase5_redteam_phase_convention_check.py`'s empirical FDTD tie-breaker —
was calibrated at incidence angles **0°/20°/39°**, nowhere near
`[47.5°,54.5°]`, and was never re-run here. Item 1's entire period-recovery
result is driven by `arg(r)`, not `|r|`, across the sweep — so NOTES.md's
"item 1's own construction can be trusted at this range going forward"
overclaims what a magnitude-only gate can establish; phase-convention
correctness at this new, more-grazing range remains genuinely unverified,
exactly the R8 shape (a named, affordable check, not run).

---

## 3. Verdict: **support-with-changes**

Item 1's actual result (Combined Verdict NEITHER mechanically,
REFUTE-leaning substantively via the T21-proximity diagnostic) is not
reversed by my attack — a convention flip would change *which* period this
construction recovers, not the fact that it has never yet cleanly matched
T28's real data on this or any prior y-wall construction, and the cycle
correctly declines to fire Checkpoint criterion 2 on this result alone. The
work is genuine, honestly self-scored where its own predictions failed
(item 1b), and item 2's gates are real, correctly-executed, magnitude-level
verification — just not the verification NOTES.md's prose claims it is.

Two secondary points, not separately attacked above for space but worth
recording: **(a)** item 1b's finding that `E_direct` cancels to `~10⁻¹⁴` is
energy-*consistent*, not a red flag — no intensity/power quantity anywhere
in this cycle ever combines `E_direct` and `E_image` incoherently (item 1
scores `Re{E_total}` pair-*deltas* only, never `|E_total|²`; item 3 prices
`|r(θ)|²` alone, independent of `E_direct`'s magnitude), so the ~10⁵
`|E_direct|`-vs-`|E_image|` scale gap never gets smuggled into an
energy-budget claim. **(b)** item 3's interception-factor-of-1 upper bound
is a sound EM argument as far as it goes (a genuinely looser-only
assumption, correctly never tightened), but its headline framing
("negligible... under either angle convention") elides that the tight
`~1.3×10⁻⁸` `theta_local`-convention bound prices a construction item 1
never actually built or period-tested — item 1's own tested object uses the
`90°−θ_beam` convention throughout, whose own bound is the far looser
`0.15%`. Both are legitimately small, but citing the tighter number as
covering "this construction family" conflates a bound on the object tested
with a bound on a different, not-yet-built one.

---

## 4. The single parameter change that would flip my verdict

Extend `phase5_redteam_phase_convention_check.py` (or an equivalent
empirical FDTD tie-breaker) to 2–3 angles inside `[47.5°,54.5°]`, exactly as
exp-075's own precedent did at `[0°,20°,39°]`, before NOTES.md's "can be
trusted going forward" language is allowed to stand. If that check is run
and confirms the committed convention (as exp-075's own general-formula
reasoning suggests it likely will, since the sign choice is a property of
`br.reflection_coefficient` itself, not of the angle), I would move to
**support** outright — the substantive REFUTE-leaning finding is solid EM
reasoning either way, and only the specific "fully gated" claim needed
fixing.
