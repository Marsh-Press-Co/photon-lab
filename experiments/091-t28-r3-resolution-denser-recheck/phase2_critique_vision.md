# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 68 · exp-091

## Independent verification performed before writing this critique

Cross-checked the §4 "Carried idealizations banner" against §5's own
numbered list, term by term. The banner's three clauses map to
Idealizations **3** (NETD not a human-eye threshold — matches), **7**
(constraint-1/2/3/4 not tested — matches), and the FLOOR/RMS
mixed-resolution clause — whose text is copied near-verbatim from
**Idealization 6** ("FLOOR/RMS[frac_contrast] are applied, not
recomputed... a disclosed mixed-resolution comparison"), not
Idealization 8 (which is about *not rebuilding* the 31-point window /
R14(b), unrelated content). The banner cites "Idealizations 3/7/8" —
the third number is wrong. Separately traced `frac_contrast`/
`delta_scene` to `lab/ambient.py::contrast_from_runs`, whose own
docstring states its Weber contrast `C` is "scored against the frozen
perceptual thresholds pinned in the experiment's NOTES" — confirmed
against `lab/glare_sidecar.py::C_THR_BASE=0.005` (lab/cued, photopic
reference; sourced to Blackwell 1946/Rose 1948/CIE 19/2/Adrian 1989).

## Steel-man (≤150 words)

The mandatory dual-section banner — this sub-thread's own structural
remedy after the Iteration-65 CHECKPOINT fired on a fourth
disclaimer-erosion instance — is present, correctly worded, and
correctly scoped at the one section that exists in a Phase-1 document:
the top of §4, before any numbered prediction. It cites the escalated
rule by name and quotes its own governing language ("restated here,
not stated once and dropped"), naming the idealizations meant to
travel with every prediction (NETD-not-human-eye, no constraint-1-4
claim, no `REALIZABILITY_MEMO.md` reopen). No prior Phase-1 proposal in
this lineage (exp-088/089/090) opened §4 this way — exp-090's own
Phase-2 VISION critique had to demand it after the fact, one cycle ago.
This is the strongest Phase-1-stage compliance with the escalated rule
this sub-thread has produced and should be credited plainly, not
treated as table stakes.

## Sharpest attack (≤150 words)

The banner's own citation is wrong: it says every finding is governed
by "Idealizations 3/7/8," but the FLOOR/RMS mixed-resolution clause it
quotes is Idealization 6's text, not 8's (8 is the unrelated
R3-rebuild-scope disclosure). A future citation tracing "Idealization
8" for this cycle's mixed-resolution caveat lands on the wrong
disclosure — a fresh, R4/R9-shape mislabeling inside the very artifact
built to end this lineage's erosion pattern. It matters beyond
bookkeeping: Idealization 6 is the one flagging that FLOOR — the gate
(b)'s classification-match prediction depends on — is unverified at
`cpl=30`, and nothing in §4 checks whether (a)'s reused `[0.3,3.0]`/
`[0.1,10]` tolerance (already flagged, T28 Live Thread, Iteration 46,
as an order of magnitude looser than R3's historical ~7% standard)
could swallow the one pinned human-perceptual threshold this channel's
own instrument exists to police (`C_THR_BASE=0.005`, Blackwell 1946).
Separately, weaker: the banner is stated once, not per-item across
(a)-(d), the "self-invented," non-binding convention Red Team named
for a lint safeguard at this exact iteration's board — still undone.

## Verdict: **support-with-changes**

The R3 debt this cycle discharges is real, overdue, and correctly
scoped as pure instrument recalibration; no mechanism claim is made,
no ruled-out ground is re-opened, and the banner's *presence* at the
correct section genuinely satisfies the Iteration-65 rule's letter.
But a mislabeled idealization citation inside the artifact that exists
specifically to prevent citation drift is not a cosmetic nit — it is
this exact defect class one step removed — and it should not ship to
Phase 3 unfixed, alongside a numeric acknowledgment that the reused
tolerance band was never checked against this channel's own pinned
perceptual threshold.

## Parameter change that would flip my verdict to plain support

Fix the banner's citation to "Idealizations 3/6/7," and add one
sentence to §4(a) (or the disclosure gate in §4d) stating, numerically,
whether the `[0.3,3.0]` CONFIRM band's edges — translated to absolute
Weber-contrast units at each of the three angles' own `frac_contrast`
values — sit above or below `C_THR_BASE=0.005`, so the "this cycle does
not test constraint 3" disclaimer is a checked fact rather than an
assumed one.
