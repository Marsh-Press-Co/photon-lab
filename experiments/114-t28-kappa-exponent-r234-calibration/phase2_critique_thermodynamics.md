# Phase 2 critique — THERMODYNAMICS (blind)

Fresh sub-agent, this seat only. Read `PANEL.md` in full; `LOGBOOK.md` in
full (RULED OUT registry R1–R32, including R27/R28/R31, which this seat's
own prior incarnations authored/co-authored, and R30/R32; LIVE THREADS T1,
T5 (the thermo ledger and its own promoted `lab/thermo_sidecar.py`
machinery), T22/T23 (sidecar area-convention/length-scale threads), and
T28's full history from its Iteration-46 opening through the Iteration-90
synthesis); `experiments/114-.../phase1_proposal.md` + `run114.py` +
`chunk_runner114.py` in full; `experiments/113-.../NOTES.md` (Fix 4,
authored by this seat's own prior incarnation) and
`experiments/112-.../results.json` for grounding. I have not seen any other
seat's Phase-2 output this cycle. Every numeric claim below was independently
re-derived by actually executing the committed code (`run114.py` imported
live, `verify_geometry_identity()` re-run, `cost_gate_check_r234`/
`cost_gate_check_r31_r234`/`combine_control_readings` invoked directly with
both the real exp-113 historical control numbers and a synthetic flipped
case) — not by re-reading prose.

## Steel-man (≤150 words)

This cycle correctly declines to fabricate a sidecar where none is owed.
No new absorptive mechanism is proposed — `graded_black_shell`/`pec_disk`
are reused unmodified, `tau_shell` held invariant (verified `==24.0` at
r=156/234/312) — so no NEW absorbed-power claim exists to require a fresh
temperature-rise/emission-band accounting; this mirrors this seat's own
accepted precedent at exp-113. The R31 machinery itself — `r31_control_ratio`/
`combine_control_readings`, reused byte-for-byte from `run113.py`, gated on
whichever of a short/sustained same-session reading has the LOWER (more
conservative) `speed_ratio` — is adapted correctly for the new `r=234`
target: only the one line that must differ (`kappa_ratio`, now 1.5 not
2.0) is duplicated in `cost_gate_check_r234`, and I confirmed by direct
execution that the conservative-direction property (lower `speed_ratio` →
larger, more conservative `projected_234_total_s`) survives that
substitution intact, using both the real exp-113 control numbers and a
flipped synthetic case.

## Sharpest attack (≤150 words)

`chunk_runner114.py`'s `step_budgeted()` will make 3 real `Sim.run()` calls
against `graded_black_shell` — a genuinely absorptive coating
(`tau_shell=24`, not zero) — so real, non-zero absorbed power *is* produced
by this leg, contrary to its own framing as pure instrument-calibration
with no thermal content. Whether that data gets *captured* is separate,
and there the gap is real: this seat established, at exp-112, the standing
practice of persisting `sigma_abs`/`sigma_scat`/`sigma_ext`/`sigma_ext_cross`
("energy_ledger") from every real capture via `sc.widths()`, zero marginal
FDTD cost — carried into `analyze113.py` even though that cycle never got
real data to feed it. `run114.py`/`chunk_runner114.py` contain **zero**
occurrences of `sigma_abs`/`sigma_ext`/`energy_ledger`/`sidecar`/`thermo`
(grep-confirmed); no `analyze114.py` exists. Unlike exp-113 (gate refused
pre-capture, omission moot), exp-114 *will* produce real r=234 captures if
it proceeds — the ledger will be computed in memory inside `sc.widths()`
(called nowhere here) and silently discarded, the exact failure exp-112's
own THERMO review caught once already. Not named among the 5 disclosed
Idealizations.

## Verdict: support-with-changes

The falsifiable cost-exponent question and the R31 gate logic (including
its r=234-specific adaptation) are sound, independently re-derived, and
correctly reasoned about energy content at the *mechanism* level (nothing
new absorbs anything). But this is a real, silently-dropped debt at the
*data-capture* level: real absorbed-power data this seat's own house
practice requires will exist in memory and go unpersisted unless fixed
before Phase 4.

## Parameter change that would flip my verdict to unqualified support

Commit a small `analyze114.py` (or ~10 lines added to `run114.py`) that
calls `sc.widths()` on the real r=234 hollow/peccored captures once they
exist and persists `sigma_scat`/`sigma_abs`/`sigma_ext`/`sigma_ext_cross`
as an `energy_ledger` dict in `results.json`, mirroring `analyze.py`'s/
`analyze113.py`'s own already-committed pattern exactly — before Phase 4
executes the real `Sim.run()` calls, since the captures needed cost nothing
beyond what this leg already plans to spend.

## Verification log (independently executed this session)

- `python3 run114.py --verify-geometry` → `{"pass_": true, "mismatches":
  []}` at r=156, 234, 312 — reproduces the proposal's own §2.0 claim
  bit-exact.
- `KAPPA_COST_EXPONENT = 3.2053299988171697` (imported, not hand-typed).
  `1.5**KAPPA_COST_EXPONENT = 3.6680107109370383`;
  `2.0**KAPPA_COST_EXPONENT = 9.223600318696624`; ratio
  `= 0.39767667550618246` (≈39.8%) — reproduces the document's own R4
  correction of MATERIALS' Iteration-90 citation ("~2.98×"/"~32%") bit-exact.
- Uncontrolled `cost_gate_check_r234(670.4778/3.0, 670.4778)` →
  `projected_234_total_s=2705.2516053872732`, `proceed_to_r234=True` —
  matches §2.0/§5 exactly.
- R31 direction check (the task's specific ask): fed
  `cost_gate_check_r31_r234` the real exp-113 historical short/sustained
  control readings (`speed_ratio=0.439` short, `0.406` sustained) via
  `combine_control_readings` — correctly selects the sustained (lower)
  reading, `used_speed_ratio=0.406`, giving a scaled
  `projected_234_total_s=6663.18s` (still comfortably under the 10800s
  bound at this hypothetical reading, `proceed_to_r234=True`). Then flipped
  the short reading to `speed_ratio=0.30` (now the lower of the two):
  `combine_control_readings` correctly switched to `used_label="short"`,
  and the scaled projection correctly rose to `9017.5s` — confirming the
  "pick the lower, more conservative `speed_ratio`" logic, and its
  monotonic effect on the projected total, both survive the
  `kappa_ratio`-substitution from run113's r=312 gate to run114's own
  `cost_gate_check_r234` (r=234) unchanged. **No defect found in the R31
  control-timing reuse** — the substitution is genuinely, not just
  procedurally, correct.
- Confirmed by grep: zero occurrences of `sigma_abs`/`sigma_ext`/
  `energy_ledger`/`sidecar`/`thermo` (beyond the seat name in the rotation
  line) in `phase1_proposal.md`, `run114.py`, or `chunk_runner114.py`; no
  `analyze114.py` file exists in the experiment directory — the sharpest
  attack above.

## Trust suite

`python3 lab/validation/run_all.py --only 12346789` re-run fresh this
session from repo root: **41/41 green**, zero `lab/` diff. (This is the
141-line consolidated house trust suite, distinct from and not to be
confused with the many-thousand-case per-experiment validation histories
elsewhere in `LOGBOOK.md`; "41/41" is this suite's own current stage count,
matching the figure most recently cited at Iteration 90's own synthesis.)
