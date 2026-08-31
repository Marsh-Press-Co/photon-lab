# Phase 2 Critique — THERMODYNAMICS (blind), Iteration 73 / exp-096

## Steel-man

This proposal is thermodynamically inert by design, and correctly proves
it rather than merely asserting it. It reads `Sim.lam`/`source_specs`/
`sources[-1]` between construction and `sim.run()`, and independently
confirms (by reading `lab/materials.py` directly) that none of
`pec_disk`/`graded_black_shell`/etc. touch the fields it inspects. Since
`sim.run()` is never invoked, no field ever propagates, no absorbed power
is ever computable, and `sigma_e` — even where populated — never
translates into a Poynting-monitor reading or a `cell_metrics_r{3,4,5}`
call. Checked directly against `lab/fdtd2d.py`: `Sim.__init__` zero-inits
`sigma_e`, and `full_capture`/`netd_row()` are simply never reached on
this code path. The "computes no thermal/NETD quantity" claim in the
compliance header is not merely stated — it is verifiably true of the
design as written, the correct N/A outcome for a construction-time-only
check, and the right call not to manufacture an R16 sidecar where none is
owed.

## Sharpest attack

§7 claims "8 representative points plus the 4 fault-injection scenarios
of §2b, 12 `Sim` constructions total." This is arithmetically wrong by
the proposal's own §2b/§3 text. The positive control is explicitly
defined as `Sim(cells_per_lambda=40)`, `angle_deg=39.2` — bit-identical
to representative point 1. FI-B injects `angle_deg=38.69` at `cpl=40` —
bit-identical to representative point 4 (`38.69°`, `RANK1C_ANGLES[1]`,
§3 table). Only FI-A (`cpl=30`×`θ=39.2`, a combination absent from the 8)
and FI-C (`angle_deg=−39.2`, also absent) are genuinely new
configurations. True distinct-construction count: **10, not 12** — the
positive control and FI-B are relabeled reruns of already-listed
representative points, not fresh evidence. This is exactly the
double-counted-total shape R4's own lineage exists to catch (see R16's
founding instance, this seat's own prior catch), and it matters here
specifically because §5b treats the positive control as an independent
MUST-NOT-flag test: it isn't independent if it's the same object as a
result already scored under §5a.

## Verdict

**support-with-changes**

## Change that would flip to full support

Correct §7's "12 Sim constructions total" to the accurate 10 (or
disclose explicitly, at Phase 3, whether the positive control and FI-B
reuse the already-constructed representative-point-1/4 objects verbatim
or are deliberately reconstructed as an independent redundancy check) —
a bookkeeping fix, zero change to the design, angles, or predictions.
