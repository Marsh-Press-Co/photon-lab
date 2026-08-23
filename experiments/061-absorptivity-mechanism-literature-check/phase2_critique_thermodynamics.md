# Phase 2 — THERMODYNAMICS blind critique (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other four Phase-2 critiques and to Red
Team. Charter: where absorbed energy goes. Always asks what re-radiates
and whether it would be detectable. Owns the per-proposal energy sidecar.
Expressibility contract: the sidecar is a post-run analytic calculation,
not an FDTD output, and is labeled as such.*

## Verification (run myself, this shift)

`python3 lab/caveat_lint.py` — exit 0. 3 registry entries, 0
required-site failures, several WARN-level candidate sites correctly
surfaced (LOGBOOK.md, run.py, materials.py, lab/caveat_lint.py itself for
`sigma_flat`, plus exp-048/030/061-proposal candidates for
`tau_shell`/e-folding). Matches the proposal's claimed output.

`python3 lab/caveat_lint.py --selftest` — exit 0. PRE-FIX (`d5b4844`):
phrase ABSENT → PASS (expected). POST-FIX (`4f29982`): phrase FOUND →
PASS (expected). Both real commits, both confirmed against live git
history, not fabricated. The tool's claims hold up under my own
execution, not just its prose.

## Steel-man (≤150 words)

Zero-FDTD means zero new absorbed-power measurement to omit — there is no
run this cycle whose ledger row could go missing. Item A properly stays
inside a Beer-Lambert/optical-density literature question (α vs.
published CNT-forest figures), and Idealization 3 honestly flags that
real ultra-black blackness may be structural-scattering-dominated rather
than bulk-absorption-dominated — itself an appropriately humble admission
that "how much gets absorbed" and "where the absorbed energy goes" are
different questions this cycle isn't resourced to answer with real data.
Item B is a pure text-lint tool with no thermal content, correctly scoped
as "not a physics gate" in its own docstring, and its self-test replays
real history rather than a constructed toy — genuinely validated, not
merely asserted.

## Sharpest attack (≤150 words)

"No FDTD run" is not "no THERMO obligation" — it's the exact
rationalization that produced the Iteration-29 defect in my own lane:
THERMODYNAMICS' Phase-1 P-5 sidecar was silently dropped, and Red Team's
own T25 tripwire (LOGBOOK.md Iter. 29) explicitly binds "any future
citation of exp-052 implying a THERMO energy sidecar was computed for it
(none was)." This proposal cites exp-052's α/τ_shell/thickness directly
and pre-commits (MP-5) to a fallback verdict — PLAUSIBLE at 15–100×
thickness — that keeps `graded_black_shell` alive as a real, absorbing,
flashlight-irradiated design candidate. It then says nothing about
absorbed-power density, ΔT, or Wien-peak band for that candidate, even as
a desk estimate the expressibility contract explicitly permits without
FDTD. If Phase 4 lands on MP-5's own predicted outcome, this program will
have a live thermal absorber with zero energy-ledger entry — the
identical omission shape, third occurrence in this lane.

## Verdict: **support-with-changes**

Require a Phase-3 THERMO disposition box (desk-only, `thermo_sidecar.py`
calls, clearly labeled post-run analytic per the expressibility
contract): bound P_abs/ΔT/Wien-peak for the MP-1/MP-2 predicted-band
worst case, using exp-034/057's own witness-irradiance parameters, so
Checkpoint 4 cannot fire retroactively if MP-4 resolves toward
PLAUSIBLE-at-larger-thickness rather than pure UNOBTANIUM.

**Flip to support**: drop the requirement only if MP-4 is pre-committed
to gate strictly on the FALSE branch alone (i.e., the proposal explicitly
states no live design candidate survives Phase 4 under any outcome) —
then there's genuinely nothing for THERMO to ledger.

## Caveat-lint tool, my lane's view

Yes — recommend a sibling registry entry (alongside
`exp052-alpha-60nm-absorptivity-open`) whose `phrase_patterns` require
T25's own disclaimer ("no THERMO energy sidecar was computed") at every
site that cites exp-052/`graded_black_shell`'s α, τ_shell, or thickness
as a live design number. The tool as built only checks phrase-presence,
not computation-presence — it cannot detect that a sidecar was never
computed, only that nobody disclosed the fact. That's still useful: it
converts my lane's recurring failure ("the omission goes unstated") into
the same tractable surface the tool already handles well, and would have
caught Iteration 29's silent-overwrite pattern had it existed then.
