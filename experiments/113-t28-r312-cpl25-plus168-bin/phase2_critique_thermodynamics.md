# Phase 2 critique — THERMODYNAMICS (blind)

**Fresh sub-agent, blind context.** I was spawned fresh for this seat only,
with PANEL.md, LOGBOOK.md's RULED OUT registry (including R27–R31, which my
own seat authored/co-authored: R31 founding, exp-112), the T28 live-thread
(sed 3094–3200), the full Iteration 89 entry (sed 24215–24415), and
`experiments/113-.../phase1_proposal.md` + `run113.py` +
`chunk_runner113.py` + `analyze113.py` in full. I have not seen any other
seat's Phase-2 output this cycle and did not invoke
`chunk_runner113.py --control` or any `Sim.run()` — all figures below are
re-derived by hand/inspection from the committed source and the cited
`results.json` files, not run.

## Steel-man (≤150 words)

This cycle honestly implements my own seat's R31 rule rather than
gesturing at it: `cost_gate_check_r31` computes and reports the RAW
(cross-session-as-if-same-speed) and SCALED (same-session-controlled)
gate readings separately, gates only on the scaled one, and
`check_cost_gate_for_r312` hard-`raise`s if no control file exists — no
silent fallback to the stale exp-112 number. Idealizations 1–2 correctly
name the cross-session assumption as provisional rather than asserting it.
Just as importantly for my own charter: no new absorptive mechanism is
proposed — `graded_black_shell`/`pec_disk` are reused unmodified — so this
cycle introduces no new absorbed-power claim requiring a fresh
temperature-rise/emission-band accounting. Declining to sidecar here is
the *correct* behavior, not an omission, given nothing new absorbs
anything.

## Sharpest attack (≤150 words)

I re-derived `r31_control_ratio`/`cost_gate_check_r31` by hand: `speed_ratio
= H/T`; dividing pilot times by `speed_ratio` gives `pilot·(T/H)`. Concrete
check, session 2× slower (`T=0.0559` vs `H=0.0279s/step`): `speed_ratio=0.5`,
scaled total `=670.48/0.5=1340.96s` → projected r=312 total `≈13,607s >
10800s` → correctly REFUSES. **The formula's direction is correct, not
buggy** — I looked for the sign error and it isn't there.

The real gap is upstream of the arithmetic: `run_control`'s single 1000-step
burst (~10s–1min) times a *different, 4× smaller* grid (r=156) than the
sustained ~2–4hr, 4×-larger r=312 job it calibrates. No numba/JIT exists
here (confirmed in `lab/fdtd2d.py` — pure numpy), but CPU turbo-boost decay
under sustained thermal load, and memory-bandwidth saturation that scales
with array size, are real, uncontrolled confounds a short small-grid probe
cannot see — and both bias `speed_ratio` in the *anti-conservative*
direction (short burst reads faster than sustained large-grid reality).
R31 (my own rule) requires *a* control point; it never required the
control be *representative* — the same "necessary, not sufficient" gap
R28 named for gate position, unaddressed here for gate input quality.
Separately: no document in this experiment states the energy sidecar as
N/A (T1 gets this explicitly; the sidecar does not) — a one-line disclosure
gap, not load-bearing.

## Verdict: support-with-changes

The R27–R31 machinery is genuinely, verifiably compliant, and the
formula I was asked to audit hardest checks out. But trusting a
single-burst, wrong-grid-size control to gate a multi-hour, 4×-larger run
is a real, undisclosed risk this document's own Idealization 2 doesn't
reach (it discusses direction, not the control's own representativeness).

## Parameter change that would flip my verdict to support

Run `--control` twice — once at `control_steps=1000` (as now) and once
after a sustained ~5+ minute warm run (e.g. `control_steps=10000`,
comparable in duration to a real production sub-chunk) — and require
`cost_gate_check_r312` to gate on whichever `speed_ratio` is LOWER
(i.e., the more conservative of the two), raising if they disagree by
more than a small, pre-registered tolerance. That converts "a control
point exists" into "a control point demonstrated stable under sustained
load," closing the gap without re-deriving any new physics.
