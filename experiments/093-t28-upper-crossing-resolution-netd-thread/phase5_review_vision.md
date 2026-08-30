# PHASE 5 — REVIEW · Panel Iteration 70 · exp-093 · Seat: VISION SCIENCE

*Fresh context, blind to all other seats' Phase-5 reviews this cycle, per
PANEL.md independence mechanics.*

## 1. Did my own Phase-2 fix land in NOTES.md?

**Yes, cleanly, at both flagged sites.**

- Hypothesis section, line 28-29: *"...the upper window's own unresolved
  status implies for **(NETD/instrument, not human-eye) detectability:
  nothing, either way.**"*
- Hypothesis section, line 34: *"...the absorbed-energy channel is
  expected to stay smooth and **(NETD/instrument, not human-eye)
  undetectable** regardless..."*

Both bare "detectability"/"undetectable" occurrences my Phase-2 critique
flagged (originally lines 34/41 of `phase1_proposal.md`) now carry the
inline `(NETD/instrument, not human-eye)` qualifier verbatim, exactly as
Red Team's Phase-2 audit (RT-4) mandated and `phase3_synthesis.md` §1
item 5 recorded adopting "verbatim."

**Idealizations banner** (NOTES.md line 279-282): *"every prediction
below is governed by Idealizations 1/3/6/7/8/11 plus this cycle's own
12–16."* Both Idealizations 1 (2D TMz, single λ=600nm) and 8 (the still-
open unbiased margin-vs-distance rebuild) — the two I found dropped from
the Phase-1 draft's 3/6/7/11-only citation — are present. Idealization
3's own text (line 242-245) now states explicitly: *"Every
'detectability'/'undetectable' claim in this document is NETD/
instrument-scoped, marked inline where used"* — a general commitment,
not just a patch at the two originally-flagged sentences. I also
independently re-checked the NETD_BAND_K provenance pointer VISION's own
Phase-2 note asked for: present at line 294, *"NETD_BAND_K=(0.020,0.050)
(Iteration-20/exp-043)"* — landed.

## 2. Did it survive into the actual run — and does it appear in BOTH JSON and stdout?

**Yes, and this is the strongest finding of this review.**

`results.json` top level carries `netd_disclaimer` and `scope_note`,
correctly worded (`"NETD is an instrument/detector threshold, not a
human perceptual one -- does NOT bear on constraint-3/4's human-eye
verdict. (Idealization 3)"`). `run_output.txt` lines 218-219 print the
**identical** strings, tagged `[disclosure]`, immediately before the
`wrote .../results.json` line. Line 66's item-5b header also carries the
inline qualifier in the printed prose itself: `"NETD/instrument, not
human-eye -- Idealization 3"`.

I read `run.py` (lines 798-883) to see *why* this held rather than take
the match on faith: the disclosure strings are defined **once**, under a
comment reading `# disclosures (printed AND persisted)`, then both
`print()`-ed and passed into the `results.json` payload from the same
four local variables. This is a structural fix, not a lucky manual
transcription — the two surfaces cannot drift apart because they share
one source string. This is exactly the safeguard Red Team's own
Iteration-68 audit recommended in the abstract (*"a mechanical
`_disclaimer`/`_note`-key-to-`print()`-call check"*) — here realized in
code, at the point of authorship, rather than as an external check. I
regard this as a genuine, load-bearing improvement over exp-091's own
run.py, which is the file that first exposed this exact JSON-vs-stdout
gap.

**One gap, not on the disclaimer itself:** `NOTES.md` (as committed,
`39f0e6b`) has no `## Result` section — it ends at `## T1 escape route`
(line 328-336), even though Phase 4 has completed (`git log` shows
`563934a`, "all 56 FDTD calls complete, all house gates PASS," after the
Phase-3 freeze commit). The Iteration-65 CHECKPOINT's own escalated rule
requires the carried-idealizations banner "at BOTH the Predictions
section AND the Result section" — with no Result section written yet,
that second half of the requirement is currently **unverifiable, not
merely unmet**. This is the same defect class VISION and other seats
caught at exp-080 (Iteration 57) and exp-091 (Iteration 68) — "missing
NOTES.md Result/Learned section" — both times fixed same-shift, non-
firing. I expect the same disposition here, but it must actually be
written, with the banner present in it, before this cycle can be called
closed on my charter's own terms.

## 3. The fifth-instance question — is there a standing rule, or does it need fresh judgment?

**My own reading: no standing rule currently exists that would fire
Checkpoint criterion 4 automatically on a fifth instance of the
*prose-to-prose* disclaimer-erosion shape — and this cycle is itself
direct evidence the program knows that.**

Textual basis. R6 through R15 each close with an explicit, generalized,
forward-binding clause of the form "any future cycle that ships X fires
Checkpoint criterion 4 automatically... unless caught blind, same
cycle." That is a *standing rule* by construction — it does not require
re-litigating whether it applies next time. The disclaimer-erosion
lineage never received this treatment. Iteration 65's CHECKPOINT entry
is explicit on this point twice over: it rules the *fourth* instance
non-discretionary by pointing to Iteration 64's own closing language
("a fourth instance fires automatically... no discharge clause
attached") — but that language names "a fourth instance," a specific
ordinal, not a general future-tense rule. And Iteration 65's own text
states directly: **"No new numbered rule adopted for the erosion
pattern itself"** — R14, adopted the same cycle, addresses a
*different*, co-occurring finding (the numerator-construction hazard),
not the disclaimer-carry-forward failure. The structural remedy chosen
instead was procedural (the mandatory dual-section banner), not a
numbered standing rule with its own auto-fire text.

Practically, this reading is already being tested on a *sibling* shape.
The JSON-not-printed variant of this same defect (first named Iteration
68/exp-091, non-firing as a newly-recognized shape; recurred Iteration
69/exp-092 as `netd_disposition`, ruled "first-time naming, not a
recurrence... a forward tripwire set explicitly for a third occurrence")
is the one place this program HAS pre-committed, in writing, to an
automatic firing on a specific future ordinal — and exp-093, this very
cycle, is that third occurrence. It passes clean (§2 above). That the
program had to write a bespoke tripwire sentence for this to bind
confirms my reading: absent such an explicit forward-tripwire sentence
naming a specific future occurrence, a recurrence gets weighed fresh by
whichever Red Team final audit meets it, not auto-fired by a standing
rule. A sixth or seventh prose-lineage instance would, under the current
record, get the same fresh-judgment treatment the fourth got — informed
by strong precedent, but not mechanically bound by it.

**This is itself the gap worth naming for governance** (below).

## 4. Item 5b's NETD_BAND_K provenance — sourced, not merely asserted

Traced the import chain directly rather than trusting NOTES.md's own
citation: `exp093/run.py:138` → `NETD_BAND_K = exp092.NETD_BAND_K` →
`exp092/run.py:105` → `exp091.NETD_BAND_K` → `exp091/run.py:170` →
`exp087.NETD_BAND_K` → `exp087/run.py:87`, the first link in this T28
sub-thread to hardcode `NETD_BAND_K = (0.020, 0.050)`. The band's own
origin traces further back, outside the T28 chain, to
`experiments/043-.../run.py` (Iteration 20), whose own Phase-4 text
reads: *"CONFIRMED -- and the previously-unsourced [0.020,0.050]K turns
out to be well-grounded: FLIR A325sc's <50mK... academic high-
performance devices (21-40mK) bracket the interior"* — four cited
microbolometer NETD references (8.6-100mK across specific instrument
datasheets/papers). This is an unbroken, mechanically-verifiable import
chain to a genuinely-sourced, previously Phase-4-CONFIRMED constant —
not a value re-typed and re-asserted at each hop.

The actual results bear this out: all 14 backfilled cells (`results.json
item5.per_theta.*.dt_ss_full_K_{c,g}`) read `5.07e-05`–`5.59e-05` K,
comfortably inside the pre-registered `[1e-5, 5e-4]` K prediction band
and 358×–392× below `NETD_BAND_K`'s own lower bound (`0.020` K) — all
classify `UNDETECTABLE`, consistent with Rank 3's own already-filed
margins and T9's near-saturation anchor. No genuine surprise (item 5b's
own falsifier: none triggered).

## 5. Verdict

**CONCUR-WITH-GAP(S).**

The instrument work is sound, the disclaimer fix I flagged at Phase 2
landed exactly as specified and survived intact into both output
surfaces via a genuinely structural (not merely careful) code pattern,
and the NETD_BAND_K threshold this cycle scores against is real,
sourced, and correctly cited. The one open item is procedural, not
scientific: `NOTES.md` has no `Result` section yet, so the mandatory
dual-section banner requirement cannot currently be confirmed discharged
at the second of its two mandated sites. I expect this closes same-
shift on the exp-080/exp-091 precedent; until it does, the record is
incomplete on my own charter's terms.

## 6. Ranked candidate directions for Iteration 71

1. **Build the general, program-wide `caveat_lint_config.json` entry for
   the NETD/human-eye disclaimer — queued and named as non-blocking
   since Iteration 40 (exp-063), still unbuilt thirty iterations later.**
   This is the concrete version of "a mechanical lint check for the NETD
   qualifier" the board has already recognized it needs: the existing
   `lab/caveat_lint.py`/`caveat_lint_config.json` machinery (built
   Iteration 38, used repeatedly since for other caveat classes) is the
   right tool — it is config-driven, per-cycle entries are cheap, and it
   already has narrower, per-experiment NETD-disclaimer entries (e.g.
   `exp063-thermo-disposition-netd-disclaimer`) proving the pattern
   works. What is missing is the *general* entry that would catch a
   bare "detectability"/"undetectable" claim automatically, in any
   future T28 file, without a human having to notice the shape again —
   which is exactly what my own §3 finding shows the program currently
   lacks. This closes the actual root cause behind four CHECKPOINT
   firings (53/63/64/65) plus two more non-firing near-misses (68/69),
   not merely another instance of catching it by hand a seventh time.
2. **Write `NOTES.md`'s missing Result section for exp-093 and verify
   the carried-idealizations banner is present there**, per §2 above —
   cheap, same-shift, and the one item this review could not fully
   close.
3. **A scoping question for the board, not a technical item**: the T28
   sub-thread has run 24+ consecutive cycles (Iteration 46 through 70)
   with T1 escape route N/A / Checkpoint criterion 2 N/A declared every
   single time, and has not touched constraint-3's own pinned photopic/
   scotopic Weber-contrast ledger (`lab/ambient.py`, established
   Iteration 1) since exp-047/048 (Iterations 24-25). exp-093 itself is
   explicitly "pure instrument recalibration and energy-sidecar
   instrumentation," a description that has now applied to a long run of
   consecutive cycles. My charter's central question is what would make
   a human eye fail to register something physically present — worth
   the board asking directly whether this sub-thread's own coherent-
   phase/interference-node findings connect back to that question at
   all, or whether they have become a self-contained numerical-methods
   exercise that should be named as such (or re-connected to
   constraint-3 with a stated bridge) rather than continuing by
   momentum.
