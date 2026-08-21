# exp-054 Phase 5 Review — VISION SCIENCE (blind, independent)

Panel Iteration 31. Reviewed: `PANEL.md`, `phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json` (re-executed `run.py` directly to
confirm live behavior, not just the committed JSON), and
`lab/thermo_sidecar.py::netd_disposition`/`mixed_length_scale_regime`/
`gas_conduction_h_eff`/`lumped_cube_mass_kg`. Also checked exp-043 and
exp-045's `NOTES.md` SUPERSEDED addenda and grepped the whole repo for
external references to exp-054.

## What this cycle establishes, from my discipline's lens

Nothing, by design, and it says so correctly. This cycle touches zero FDTD
scenes, proposes no σ(I)/σ(x,t)/angular-selectivity/sub-threshold
parameter, and makes no claim about photopic or scotopic ambient
appearance, Weber contrast, or any human observer. It re-derives a
post-run analytic thermal-detectability sidecar figure (instrument-camera
NETD comparison) for two already-existing articles. That is squarely
outside constraint-3/4's territory and the cycle's own T1 disposition
("NONE") is correct. My gatekeeper duty this cycle is therefore entirely
about hygiene: does the NETD-vs-human-eye disclaimer actually travel with
every number it needs to travel with, given this exact conflation has
already recurred three documented times (Iterations 17, 22, 23)?

## Verifying mandatory fix 6 directly

**Grep confirms the scope discipline held for substantive content.**
`grep -i "eye|human|contrast|luminance|photopic|scotopic|constraint-3"`
across every exp-054 file returns matches ONLY inside the disclaimer
boilerplate itself (`NETD_DISCLAIMER` string, `netd_disposition`'s own
`disclaimer` field, the two forward-pointer notices in exp-043/045) — never
as a new substantive claim. Confirmed clean.

**Mandatory fix 6 landed unusually thoroughly, but not at every locus.**
This is the best propagation this program has produced against this
specific failure mode — better than "not done," which is the useful
finding to report, but it is not 100% complete:

1. **`results.json` — thorough, exceeds the docket's own letter.** Every
   individual classification dict returned by `netd_disposition` (the
   ON-endpoint `netd_disposition` block, and both `netd_first`/
   `netd_periodic` at all 8 Block-C grid points — 17 classification
   objects total) carries its own `disclaimer` field, because the fix was
   made structural at the source (`lab/thermo_sidecar.py:318-322`), not
   bolted on per call site. `part_a`, `part_b`, and the `regime` sub-dict
   each additionally carry a top-level `netd_disclaimer` string, plus two
   more `*_ALL_CLAIMS` copies at the file root (lines 439-440). This is
   genuinely load-bearing placement — the disclaimer sits inside the same
   object as the number, not merely "nearby."
2. **`NOTES.md`'s prediction table — done.** P-054-2, P-054-4, and P-054-5's
   rows each carry the disclaimer sentence inline, verbatim, next to the
   band/classification (lines 93, 96, 97).
3. **exp-043 and exp-045's forward-pointer SUPERSEDED notices — done.**
   Both end with "NETD is an instrument/detector threshold, not a human
   perceptual one; this note does not bear on constraint-3/4"
   (`experiments/043-.../NOTES.md:583-584`,
   `experiments/045-.../NOTES.md:508-509`).
4. **`NOTES.md`'s Results/Learned prose — cannot yet be verified, because
   it does not exist.** `NOTES.md` is 107 lines and ends at the frozen
   Phase-3 predictions/idealizations table (this matches the task
   framing — "NOTES.md (the frozen predictions)"). Despite `run.py`
   having been executed and `results.json` fully populated with all
   P-054-1 through P-054-8 passing, no Results/Learned section has been
   appended to `NOTES.md` reporting the actual numbers in prose. Mandatory
   fix 6 explicitly named "NOTES.md's Results/Learned prose" as one of its
   three required loci (`phase2_redteam_audit.md:229-232`,
   `phase3_synthesis.md:47-50`). This locus is presently open, not failed
   — but it is not done, and whoever writes it must not forget the
   disclaimer at that point, since it is exactly the kind of freshly
   drafted prose that has slipped in three prior cycles.
5. **The LOGBOOK Iteration 31 entry — does not exist yet.** Grepped
   `LOGBOOK.md` for "Iteration 31"/"exp-054": no entry. Expected, since
   Phase 5 (this review) is what feeds that entry — flagged here only so
   the Director does not forget this is the third of the fix's three named
   loci and must carry the disclaimer when written.
6. **`run.py`'s own summary print statements — a real, if minor, miss.**
   Lines 266-275 print six lines to stdout reporting P-054-1 through
   P-054-5's numbers and pass/fail status verbatim (`"P-054-2 NETD-lo
   margin(ON)=607.33x  pass=True"`, `"P-054-5 both UNDETECTABLE=True"`,
   etc.) — I re-ran `run.py` directly and confirmed this output live. None
   of the six print lines carries the disclaimer string or even the word
   "NETD" spelled out with its instrument qualifier attached at that
   point. This is a locus "outside `lab/thermo_sidecar.py` itself" where
   P-054-2/4/5's classification is quoted, per the mandatory-fix docket's
   own wording — it just wasn't one of the three loci Red Team enumerated
   by name (`results.json`, `NOTES.md`, LOGBOOK), so it fell through the
   gap between "verbatim at every locus" (the general instruction) and
   "results.json/NOTES.md/LOGBOOK" (the specific enumeration). Console
   output is exactly the kind of place a future interactive session or CI
   log would show a bare "UNDETECTABLE" or a margin number with nothing
   attached warning it isn't an eye-detectability finding.

**Net assessment on fix 6: substantially landed, not a fourth full
recurrence, but not fully closed.** The prior three instances were cases
of the disclaimer being absent everywhere it mattered. This cycle is the
opposite failure shape — present almost everywhere, structurally baked
into the source function so it is very hard to accidentally omit from any
future `netd_disposition` call site — with one genuine but low-stakes gap
(stdout prints) and two loci not yet reached because the artifacts they'd
live in (NOTES.md prose, LOGBOOK entry) haven't been written yet. This is
real progress against the base-rate pattern, and the fix should not be
read as failed. But "propagate verbatim at every locus" was not achieved
literally, and I want that stated plainly rather than rounded up to "done."

## A structural risk beyond fix 6's letter: field names carry no NETD qualifier

The task asked whether anything in this cycle's own language risks being
misread by a future cycle as a constraint-3/4 finding even with the
disclaimer present nearby. One real risk: `results.json`'s field NAMES are
bare — `p_054_5_both_undetectable`, `all_points_undetectable`,
`netd_lo_margin`, `all_c_undetectable` — none embeds "NETD" or "instrument"
in the name itself (only `netd_lo_margin` partially does). A future cycle
or script that reads `results["p_054_5_both_undetectable"]`
programmatically (e.g., to populate a LOGBOOK summary table or a PLAN.md
queue line) and does not also deserialize the sibling `netd_disclaimer`
string could legitimately produce a sentence like "exp-054 confirms both
articles are undetectable" with no instrument qualifier — technically
consistent with the field's literal name, and exactly the phrasing that
triggered the Iteration 17/22/23 recurrences. The disclaimer being present
as *data* next to the number is good; it is not *enforced* by the field's
own name or by any schema that would make omitting it during re-use an
error rather than a convenience. I recommend (not mandatory, since it
costs a rename in a still-live results structure): prefix or suffix the
three headline boolean/numeric keys with `_netd_instrument_only` (or
similar) so a bare key name alone still carries the disclaimer's substance,
independent of whether the sibling string gets copied forward.

## Load-bearing defects found (ranked)

1. **(Minor, real) `run.py` console prints omit the disclaimer** — lines
   266-275, all six P-054-1..5 summary lines. Fix: append a fixed
   one-line disclaimer after the print block, or append `" [NETD,
   instrument-only]"` to each classification-bearing line.
2. **(Not yet failed, but open) NOTES.md Results/Learned section is
   unwritten** despite `results.json` being fully populated — one of
   mandatory fix 6's three named loci is not yet checkable. Flag for
   whoever closes Phase 4→5: the disclaimer must appear there when
   written, not just the numbers.
3. **(Recommendation, non-blocking) Bare field names in `results.json`**
   carry no NETD/instrument qualifier in the key itself, only in adjacent
   sibling string values — a re-use risk for a future cycle's summarizing
   code, not a defect in this cycle's own text.

None of these threaten this cycle's own reported numbers or its T1/scope
discipline, which is otherwise the cleanest instance of this specific
propagation problem this program has produced.

## Ranked candidate next directions for Iteration 32+ (from my seat only)

1. **Close the two open loci of mandatory fix 6** — append NOTES.md's
   Results/Learned prose (with disclaimer) and, when the Director writes
   the LOGBOOK Iteration 31 entry, confirm the disclaimer sentence lands
   there too. Cheap, closes the loop fully rather than leaving it at
   "substantially done."
2. **Fix the `run.py` print-statement gap** described above — trivial,
   one line, but exactly the kind of place a fourth recurrence would
   actually originate from in a future copy-paste of this script's
   pattern into a later sidecar cycle.
3. **This program's actual constraint-3 instrument (`lab/ambient.py`,
   stage 9) is still not built**, per `PANEL.md`'s own metrics table
   ("to be built"). Every cycle since Iteration 20 that has touched the
   thermal sidecar, including this one, has been instrument-fidelity work
   on the NETD side-channel while the program's one human-eye metric —
   photopic AND scotopic Weber contrast — remains uninstrumented. This is
   not a criticism of exp-054 (T1: NONE, correctly scoped), but from my
   seat's charter it is the standing gap: nothing in this program can yet
   be scored against constraint-3 at all, five sidecar-focused cycles in.
   I flag this as the highest-value next VISION-relevant direction,
   independent of anything in exp-054 itself.
4. Not a VISION finding, but worth noting since it recurred across two
   other seats' Phase-2 critiques and Red Team's own attack log: EM's
   Block-C re-run request (mandatory fix 2) and PHOTONICS' Q_ext(x)
   closed-form check (non-mandatory) are both resolved/deferred cleanly in
   this cycle's record — no action needed from my seat, noted only for
   completeness of the review.

## Verdict

**PROMISING** — with a qualification. The underlying physics correction
(mixed r_out/w_on chain) is out of my discipline's scope to judge, but from
my seat's own duty — the NETD/human-eye disclaimer propagation this cycle
was specifically built to fix — the work is the strongest instance this
program has produced: structurally embedded at the source function so it
is hard to omit going forward, present in results.json far beyond the
letter of the docket, and present in both forward-pointer notices. It is
not, however, complete: the `run.py` print statements are a genuine miss,
and two of the fix's three named loci (NOTES.md prose, LOGBOOK entry) are
simply not yet written and so remain unverified rather than confirmed.
Calling this a full "fourth recurrence" would overstate the case — the
disclaimer did not fail to travel, it traveled almost everywhere. Calling
it "fully landed" would understate the two gaps above. My verdict is
PROMISING on the specific gatekeeper question I own, conditioned on the
two follow-ups in my ranked list being closed before this cycle's LOGBOOK
entry is written as "mandatory fix 6: done."
