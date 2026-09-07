# Photon Lab — agent onboarding

Read `HANDOFF.md` first (kickoff runbook), then `README.md` (the honest
frame). Conventions: numbered experiments with a NOTES.md each (hypothesis /
setup / result / learned / next); every writeup states its idealizations; $0
open-source tooling; verify-before-claim, same as the Disclosure culture.
Group project — board channel on `Marsh-Press-Co/co-lab`, asks as standalone
comments with @-mentions.

Before bench work, read `lab/validation/VALIDATION.md` — engine trust
status + the paid-for measurement lessons (FFT wavelength quantization,
reflection-monitor placement, scattered-vs-total field comparisons, PEC
flush at cloak walls). Re-run the suite after any `lab/` engine change.

Phenomenon-program work (exp-020+) runs under `PANEL.md` — the seven-seat
research panel — with `LOGBOOK.md` as its persistent memory. Read both
first; never re-propose a ruled-out idea.

Personal machine bridges go in `CLAUDE.local.md` (gitignored), never here.

## T18 (WebFetch egress block) — allowlist added 2026-08-25

`.claude/settings.json` now carries `WebFetch(domain:...)` allow rules for
the scholarly hosts this program has been blocked on since Iteration 13
(arxiv, doi.org, PNAS, Nature, NCBI/PMC, APS, Optica, ACS, AIP, IOP,
Springer, ScienceDirect, NIST, vantablack.co.jp). Claude Code pre-allows
**no** domains by default, and the repo had no settings file at all — so
every scholarly fetch fell outside an empty allowlist and returned
`EGRESS_BLOCKED`, with no human present in a cloud shift to approve the
prompt. That is the whole of T18's cause; it was never a repo-side bug.

**Do not carry "T18 assumed still standing" forward again.** Re-test it
explicitly with a real fetch and record the outcome, per this program's own
positive-control discipline. If fetches now succeed, `R_contact`'s
`measured_direct` literature search (REALIZABILITY_MEMO Entry 3, UNANSWERED
across five cycles) is unblocked and the T18 evidentiary tier can rise above
WebSearch-snippet-only. If they still fail, the block is enforced above the
project layer (managed settings / cloud egress policy) — record the exact
error and say so, because that distinction is the escalation.
