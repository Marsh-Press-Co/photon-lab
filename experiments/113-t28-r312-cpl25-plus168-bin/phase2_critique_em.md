# exp-113 — Phase 2 Critique — ELECTROMAGNETISM (blind)

**Fresh sub-agent, blind context.** I have read PANEL.md in full, LOGBOOK.md's
RULED OUT registry (R27–R31 in full) and the T28/Iteration-89 narrative, and
`phase1_proposal.md`/`run113.py`/`chunk_runner113.py`/`analyze113.py` in full,
independently, before writing anything below. I have not seen any other
seat's Phase-2 output this cycle. All numeric claims below are re-derived
from source (`lab/fdtd2d.py::Sim.run()`, `run113.py`, `chunk_runner113.py`),
not taken from the proposal's own prose.

## Steel-man (147 words)

Under my own charter, this cycle genuinely closes two gaps my seat itself
raised at Iteration 89. (1) R28 positioning: I traced `chunk_runner113.py`'s
`__main__` line-by-line — `check_cost_gate_for_r312(cpl_arg)` is called
*before* `step_budgeted(...)` is even invoked, unconditionally, for **every**
r=312 CLI invocation, fresh-start or resumed. Since STEPS=16000 at
DEFAULT_BUDGET_S=480s forces ~4 resumed calls per scene (most real
`sim.run()` cost happens on resume, exactly exp-111's own flaw shape), and
the gate re-fires on each one, this is a genuinely more robust fix than
exp-110/111's — not merely re-asserted, actually re-verified per call.
(2) `analyze113.py` (lines 86–90) restores `sigma_ext_cross` to the
persisted `energy_ledger`, correctly fixing (not just disclosing) my own
exp-112 Phase-5 F2 finding that the tautological `sigma_ext` check had
silently replaced the genuine optical-theorem cross-check. T1 N/A holds
structurally throughout.

## Sharpest attack (150 words)

Idealization 2 claims per-step FDTD cost is materials-invariant because
`fdtd2d.py` "touches the full grid regardless of contents." False by direct
trace: `Sim.run()`'s per-step body executes `if self.pec.any(): self.Ez[
self.pec] = 0.0` — an operation `pec_disk` scenes alone pay (hollow/empty
never set `self.pec`), roughly +1 extra O(N²) op on top of ~7 baseline ones,
~14% real per-step cost asymmetry. `HISTORICAL_PER_STEP_S` blends all three
scenes (2 cheap + 1 pricier) into one figure used as the "empty" proxy for
`r31_control_ratio`, inflating it by ≈5% versus the true empty-only rate.
Since `speed_ratio = HISTORICAL_PER_STEP_S / this_session_empty_rate`, that
inflation inflates `speed_ratio`, which *deflates* `scaled_total` and hence
`projected_312_total_s` — biasing R31's own correction **anti-conservatively**,
stacking with R28's already-disclosed ~15% anti-conservative kappa-exponent
miss, both pushing toward false approval. Not fatal at this cycle's 37%
margin, but undisclosed and direction-predictable — exactly what R31 exists
to catch.

## Verdict: support-with-changes

T1 route N/A confirmed independently — no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold content anywhere in this leg; zero constraint-1/2/3/4 claim is
scored. Nothing here should block Phase 4 at the currently-computed margin.
But Idealization 2 as written asserts an invariance property that is false
on inspection of the engine it cites, and the false claim happens to matter
in a specific, quantifiable, anti-conservative direction for a safety gate
under my own charter's bookkeeping duty — it should be corrected to state
the true direction and rough magnitude of the bias (not merely "assumed, not
measured") before Phase 4 trusts `proceed_to_r312`, and the compounding with
R28's own already-disclosed ~15% miss should be named explicitly so a future,
thinner-margin cycle (e.g. a future r=624 point) does not inherit two
silently-stacking anti-conservative approximations.

## Parameter change that would flip my verdict to support

Have `run_control()` re-time `control_steps` of the r=156/cpl=25 **peccored**
scene (not "empty") — the one scene whose per-step cost the historical
blend actually inflates the baseline with — instead of, or in addition to,
empty. That removes the mismatch between what `HISTORICAL_PER_STEP_S`
implicitly averages over and what the same-session control actually
measures, closing the bias at its source rather than requiring a disclosure
patch.
