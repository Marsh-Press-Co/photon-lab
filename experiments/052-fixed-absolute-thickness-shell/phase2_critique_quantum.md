# QUANTUM OPTICS — Phase 2 Critique, Iteration 29

**Steel-man:** The proposal correctly stays out of QUANTUM's normal
territory and says so up front, not by omission: no σ(I), σ(x,t),
dispersive ε(ω), or gain is proposed anywhere — `graded_black_shell` stays
static/passive/LTI in both intensity and time, exactly as established.
§4's "None" T1-escape disclaim is honest, not evasive: it neither drops
constraint 3 quietly nor smuggles a state-dependent absorption model in
through the back door, and it correctly declines to invoke VISION's
`C_thr` PASS/FAIL ladder against an opaque τ_shell=24 object. Holding
`sigma_max` literally fixed at the r=78-gated value (not rescaled by κ) is
exactly the concrete, falsifiable materials claim PANEL.md's latitude
rule demands — "one real coating, reused at any size" — and the
τ_shell=24 confound control plus the P-0 code-only r=78 identity check
are genuinely clean, well-precedented bookkeeping.

**Sharpest attack:** The mechanism disclaim is correct, but the
*instrument* this cycle reuses carries its own coherence assumption that
is never re-checked here. `lab/ambient.py`'s N9 ambient sum adds per-angle
*intensities* incoherently; the only empirical license this program has
ever produced for that approximation is exp-029's coherent-superposition
bridge gate (suite stage 11), measured once, at the self-similar r=78
geometry (shell = 61.5% of r_out) — a small but real field cross-term
(+0.0224% aggregate, 5.02× locally bin-wise, ~99.3% washed out by
angular averaging). This cycle's mandatory P-1 result is scored at
r=156, where the fixed 48-cell shell is now only 30.8% of r_out — a
thin, near-field-diffracting rim (T9/T12/T14's own open territory) on a
disk twice the radius. §5 re-verifies only the flat-coating R-gate and
explicitly does NOT rerun the coherent-vs-incoherent bridge check at
this new thickness-fraction regime — an *inherited*, untested assumption
on exactly the one channel QUANTUM has ever validated, and validated at
a geometry this proposal deliberately abandons.

**Verdict:** support-with-changes

**Parameter change that would flip verdict (optional):** Add one cheap
bridge-gate rerun (stage-11's existing joint-vs-summed-phasor identity,
already validated machinery, no new code) at r=156 on the fixed-absolute
shell before P-1 is trusted as licensing the incoherent-sum `C` — if the
cross-term stays comparably small (not order-of-magnitude larger than
exp-029's 0.0224%/5.02×), the instrument transfers and this becomes a
clean support.
