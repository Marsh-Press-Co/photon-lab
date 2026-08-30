# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 69 · exp-092

## Independent verification performed before writing this critique

Cross-checked §6's "Carried idealizations banner" (cites "Idealizations
3/6/7") against §8's own ten-item list, term by term: clause 1 (NETD not
a human-eye threshold) = Idealization 3, clause 2 (constraint-1/2/3/4 not
tested) = Idealization 7, clause 3 (FLOOR/RMS applied, not recomputed) =
Idealization 6 — all three numbers correct, content matches verbatim.
Then cross-checked every one of §8's explicit "(exp-091 Idealization N)"
citations (items 1,2,3,4,5,6,7,10) against exp-091's **actually-committed**
list — not its superseded Phase-1 draft, its final `NOTES.md` (items 1–10,
`NOTES.md` lines 186–216, item 10 corrected forward from the Phase-1
draft's own wrong "40.2° is the hardest case" premise). All eight
citations resolve to the correct number and correct content. Then swept
`NOTES.md`'s full ten-item list for anything **not** re-cited here that
remains true of exp-092's own scope, per §7 ("explicitly out of scope this
cycle, named forward").

## Steel-man (≤150 words)

This is the cleanest carried-idealizations banner this T28 desk/instrument
sub-thread has produced. §6 cites "3/6/7" — verified number-for-number
against exp-091's `NOTES.md`-committed list, correctly landing where
exp-091's own Phase-1 draft mislabeled it "3/7/8" one cycle earlier (my
seat's own catch, Iteration 68). Every other explicit exp-091 citation in
§8 (Idealizations 1,2,3,4,5,6,7, and 10→9) reproduces its source
number-for-number too, and the two genuinely new idealizations
(settling-not-rechecked-per-angle; `sigma_max=0.5` deliberately unscaled)
are correctly labeled "New this cycle" rather than force-fit onto an
exp-091 number that doesn't cover them. NETD is explicitly disclaimed as
an instrument/detector threshold, not a human-eye one — exactly where my
seat's own scoring authority lives — and this cycle correctly claims no
constraint-3 verdict. On citation hygiene specifically, this reads as
demonstrated learning from last cycle's catch, not rote restatement.

## Sharpest attack (≤150 words)

`NOTES.md` Idealization 8 — "No full R3-rescaled rebuild of exp-083's
31-point window, and no extension of R14(b)'s still-queued formal
null-controlled period fit — both remain open, separate, standing T28
items" — is silently absent from §8's "cited forward from exp-090/exp-091,
not re-derived" list, despite remaining verifiably true here: exp-092's
own §7 independently carries R14(b) forward as still-queued and
unaffected. Every *other* exp-091 idealization is correctly re-cited,
which makes this one gap harder to read as inattention than as the exact
narrowing the Iteration-65 banner rule exists to stop. Compounding: my own
exp-091 review found `netd_disclaimer`/`scope_note` written to
`results.json` but never `print()`-ed to `run_output.txt` — Red Team named
a structural safeguard for it. §7 Tier 4 explicitly defers that fix to
"whichever future cycle," even though this cycle's own 26 new FDTD calls
are exactly the run that would reproduce the same human-readable gap.

## Verdict: **support-with-changes**

The banner itself is correctly worded and correctly cited at the one
section a Phase-1 document has (§6); the R3/instrument work is properly
scoped and stakes no constraint-3 claim. But a silently dropped, still-true
idealization inside a document whose own header promises complete
inheritance, plus a known print-parity gap deferred rather than fixed
going into a cycle that will generate the exact artifact it recurs in, are
both live instances of this seat's own charge — not fatal to the design,
but not something that should ship to Phase 3 unaddressed either.

## Parameter change that would flip my verdict to plain support

Add exp-091's Idealization 8 (verbatim or restated) to §8's list, and
commit — in `run.py`, before Phase 4, not as a named future board item —
the one-line `print()` fix for `netd_disclaimer`/`scope_note` so this
cycle's own `run_output.txt` does not reproduce exp-091's exact
print-parity defect.
