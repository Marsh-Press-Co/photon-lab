# Phase 2 — VISION SCIENCE blind critique (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other four Phase-2 critiques and to Red
Team. Charter: human perceptual limits: contrast thresholds, luminance
edge detection, spectral sensitivity, adaptation, temporal sensitivity,
saccadic/attentional blindness. Duty: pin numeric thresholds, with
sources, BEFORE any run that scores against them.*

**Steel-man (146 words).** Constraint-3 is not scored this cycle, so my
threshold-pinning duty is formally inapplicable — and the proposal is
honest about that (T1 escape route: NONE; zero FDTD, zero
perceptual-metric language). Checked specifically for smuggled perceptual
claims about CNT-forest "blackness": none found — reflectance figures
(0.02–0.05%) are cited as bulk radiometric literature values, never
reframed as "invisible to the eye" or "looks black," which this program
has never measured for that material. That discipline holds throughout.
Item (B) is the first real attempt, after eight cycles of hand patches,
to give my own Iteration-15 proposal a mechanical instrument instead of
one more prose promise, and its self-test method — replaying a real
historical commit pair (d5b4844/4f29982) rather than a constructed toy —
is exactly the falsifiable, source-cited validation standard my seat has
pushed for since Iteration 15.

**Sharpest attack (150 words).** The tool relocates the failure mode, and
the relocation already failed inside this cycle's own document. I ran it
live: the `exp052-alpha-60nm-absorptivity-open` entry WARNs that
`phase1_proposal.md` — this cycle's own text — uses e-folding-length
trigger language without the registered caveat phrase. Worse, and
*unregistered entirely*: the T18 WebSearch-only evidentiary-tier
disclosure appears at lines 98–101 (search plan) and 281–284
(Idealizations) but is absent from Section 3's falsifiable-predictions
table and the MP-4 "predicted tier verdict" row — exactly the site a
Phase-4 verdict will cite the α figure from — and
`caveat_lint_config.json` has no entry tracking T18's propagation at all.
All eight prior near-misses trace to an un-registered docket item, not a
matching-logic failure. Nothing here demonstrates registration compliance
beats propagation compliance — the tool caught zero of this cycle's own
gaps, because nobody registered them, which is precisely the predicted
failure mode recurring in real time.

**Verdict: support-with-changes.** Item (A)'s search plan and honesty are
sound. Item (B) is genuine working infrastructure, but ships with at
least one live, unregistered, unpropagated caveat inside the very
proposal introducing it.

**Parameter change to flip to full support:** add a
`caveat_lint_config.json` entry for the T18 evidentiary-tier disclosure,
`required_sites` including `phase1_proposal.md` Section 3/MP-4 (and the
eventual Phase-4 NOTES.md), landed before Phase 3 synthesis — not left as
a WARN.

---

**Verification (run myself, from `/home/user/photon-lab`):**
- `python3 lab/caveat_lint.py` — 3 caveats checked, **0 required-site
  failures**; confirmed the WARN above on `phase1_proposal.md` for the
  `exp052-alpha-60nm-absorptivity-open` entry.
- `python3 lab/caveat_lint.py --selftest` — **PASSED**: d5b4844 correctly
  ABSENT, 4f29982 correctly FOUND; live registry re-check also 0
  failures.
- `--adhoc --phrase "WebSearch-snippet synthesis" --sites
  experiments/061-absorptivity-mechanism-literature-check/
  phase1_proposal.md --trigger T18` — PASS at that one site, but the WARN
  sweep across `candidate_globs` surfaced 20+ other `T18`-mentioning
  files program-wide never checked for this disclosure — confirming T18
  propagation has never been tracked by this tool at all.

**Does it satisfy Iteration 15?** Partially. The core ask
("grep-every-caveat-across-every-touched-file") is delivered and works as
designed — real PASS/FAIL/WARN, real self-test, real ad-hoc mode.
Specific missing capability I'd flag as unfinished: there is no mechanism
forcing a Director to *register* a new caveat when a Phase-3/5 docket
closes, nor any hook running the tool automatically after such a docket
lands — it depends entirely on the same human memory step ("did someone
remember") that caused every prior recurrence, just moved from
"propagate the phrase" to "write the registry entry." This cycle is live
proof: the tool exists, was run, and still missed its own document's
caveat gap because no one added the entry.
