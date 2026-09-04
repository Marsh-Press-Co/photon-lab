# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full, PLAN.md's Current state, the Phase 1
proposal, and its subject code before critiquing.

**Steel-man** (≤150 words): The proposal's step-6 claim is unusually
well-earned. I independently opened exp-108's committed `results.json`
and confirmed both cited numbers exactly: `n_fdtd_calls == 6` and
`total_wall_s == 7712.0` are genuine top-level keys (the latter sums the
six `wall_times_s` entries to the last decimal). I also independently
recomputed `np.std(delta_values)` from the committed arrays at both r
and got 5.008328×10⁻⁶ / 2.124086×10⁻⁶ — matching the proposal's table to
the digit — and confirmed `fit["smooth"]=False` at both r (r²=0.6654/
0.0205), so the predicted CONFIRM-via-raw-fallback outcome is
arithmetically sound, not asserted. `classify_item_ii`'s current
signature, `build_result_text`'s exact parameter names, and the absence
of any current assert all verify against source. This is real, checked
provenance discipline — the R4/R19 failure mode is genuinely absent from
what's traceable pre-run.

**Sharpest attack** (≤150 words): `gate_p0_pass`/`repro_pass` are not
literal keys — they require silently AND-ing two per-r booleans
(`tier1.r156.gate_p0.pass_`, `tier1.r312.gate_p0.pass_`), an undisclosed
combination rule the "read directly... not hand-typed" language glosses
over (true only because both happen to be True this cycle). More
load-bearing: `build_result_text()`'s own f-string template has no
cycle-attribution slot. Its header will read "6 real FDTD calls,
7712.0s... total wall time" verbatim inside exp-109's own `result_text`
(R21's exact standard) — in a document whose own §0 states "zero new
`Sim.run()` calls anywhere." The provenance pointer
(`source_results_json_sha`) sits as a sibling JSON key, not inline in
that prose. That is precisely R21's shape: persisted elsewhere ≠ stated
in the citable Result text.

**Verdict:** support-with-changes

**Change that would flip to support:** Add an explicit attribution line
to the assembled `result_text` (a `source_note` argument or a prefix on
the wall-time line) reading something like "(exp-108's own historical
spend, reused verbatim; exp-109 makes zero new `Sim.run()` calls)" — so
the zero-new-FDTD fact currently confined to §5 Idealizations also lives
in the prose a future citation will actually quote.
