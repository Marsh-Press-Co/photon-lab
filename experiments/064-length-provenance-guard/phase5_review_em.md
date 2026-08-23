# Phase 5 — ELECTROMAGNETISM blind review of exp-064 results (Panel Iteration 41)

*Fresh sub-agent, no memory of the cycle that critiqued this proposal at
Phase 2 (a different EM instance wrote `phase2_critique_em.md`, whose
attack 1 became this cycle's own mandatory-fix 1 — gate 4, the
source-inspection gate). Blind to every other seat's own current-cycle
Phase-5 review — no other `phase5_review_*.md` file for this experiment was
read before this one was written (two untracked sibling files exist in the
working tree from other seats; not opened).*

**Read in full**: `PANEL.md` (charter, Phase-5 format); `LOGBOOK.md` in
full (13,115 lines) — the RULED OUT registry, ESTABLISHED section, and every
LIVE THREAD, with T23's own Iteration-22 opening (exp-045), Iteration-23
closing-by-argument (exp-046, the mixed-regime resolution: power on `w_on`
per `RATIO_ON`'s own calibration, conduction/mass/area on `r_out` per Nu=2's
own derivation requirement), and its three subsequent in-the-open
violations at Iterations 38/39/40 read closely; `PLAN.md`'s Current-state
section and the Iteration-41 queue block (Red Team's binding forward
commitment); `lab/thermo_sidecar.py` in full as it now stands; `lab/
validation/run_all.py` stages 18/23/24 in full, gate 4 read line-by-line;
every file in `experiments/064-length-provenance-guard/`: `phase1_
proposal.md`, all five `phase2_critique_*.md` (including my own prior-cycle
instance's), `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`phase4_results.md`.

I did not stop at reading. I ran the actual suite (`python3 lab/validation/
run_all.py --only 24`, 28/28 green, reproduced independently) and then wrote
a standalone script that imports gate 4's *exact* regex
(`r"(front_surface_conduction_correction|mixed_length_scale_regime)\(\s*
(.*?)\)"`, `re.DOTALL`) and runs it against four constructed source snippets
designed to probe exactly the question the task brief asked — see §1.

---

## 1. Independent re-verification of gate 4's robustness — a real,
previously-unnamed failure mode found, plus reproduction of the already-
disclosed one

Gate 4 (`lab/validation/run_all.py:2309–2336`) text-scans `run_all.py`'s own
committed source and cross-checks the tag on every call site mentioning one
of three hardcoded variable names (`L_MP5_730X_M`, `L_BENCH_M`, `R_OUT_M`)
against what that name is supposed to carry. **Confirmed by direct
execution against the current committed source**: 2 witness-scale + 3
bench-scale live call sites, all correctly tagged, 28/28 green.

I then ran the extracted regex, unmodified, against four hand-built call
sites that never touch the real repo (results below are from my own script,
not a hypothetical description):

| Case | Construction | Result |
|---|---|---|
| 1 | A MISTAGGED real call (`L_MP5_730X_M` tagged `bench_construction` — the exact false declaration QP-3/gate 4 exists to catch) with a nested-paren argument (`get_kappa_for_material("CNT_forest")`) placed **before** `L_MP5_730X_M` in the argument list | **Silently SKIPPED — neither branch fires, zero check emitted, no FAIL.** Non-greedy `(.*?)\)` stops at the nested call's own `)`, truncating the capture before it ever reaches `L_MP5_730X_M`. |
| 2 | Same mistagging, but the witness-scale length is assigned to a **new** variable name (`L_SUBSTRATE_CONTACT_M`) not in the hardcoded three | **Silently SKIPPED.** Reproduces `NOTES.md` Idealization 1's own disclosed caveat exactly, now with a concrete constructed reproducer rather than a stated possibility. |
| 3 | A *correctly*-tagged diagnostic call, but with the same nested-paren argument placed **after** `L_MP5_730X_M` | **False FAIL** — the witness branch fires (name is found before the truncation point) but the required marker strings, which sit after the nested `)`, are cut off, so `ok=False` even though the real, untruncated call is honest. |
| 4 | The mistagged witness-scale length passed as a bare literal (`1051.2e-6`), no variable name at all | **Silently SKIPPED.** |

Cases 2 and 4 reproduce what `NOTES.md`'s own Idealization 1 already
discloses ("a genuinely NEW mistagged variable name would still only be
caught by declaration discipline, not detection") — confirmed independently
here, not merely trusted. **Case 1 is new**: it is not a new-variable-name
problem at all — it uses one of the three names the gate already knows to
look for — but the non-greedy, nested-paren-blind regex still fails to see
it, for a different, previously-undisclosed reason (a parsing fragility,
not a naming-coverage gap). Case 3 is the safe-direction mirror of Case 1:
the same fragility can also false-FAIL an honest call, which is merely
annoying (blocks CI) rather than dangerous, but confirms the regex is not
robust to nested parentheses in either direction.

**None of these four cases describe the current committed state** — I
verified separately (`git status --short`, `grep` over every real call
site) that none of the five real call sites in `run_all.py` or the five in
`experiments/{054,057,059,060}/run.py` contains a nested-paren argument or
an unrecognized variable name; every one is a flat `name, NAME_CONST,
literal, ...` keyword list. This is a structural robustness gap in the
checking mechanism, not a live violation — the same status Red Team's own
Phase-2 attack 5 already assigned to a different T23-adjacent gap
("structural blind spot, not a live violation").

**A second, distinct scope boundary, also not a live violation but worth
naming explicitly**: gate 4 scans `open(__file__)` — `run_all.py` only. Five
of the ten real, currently-committed `mixed_length_scale_regime` call sites
in this program live in `experiments/{054,057,059,060}/run.py`, confirmed
correctly retagged this cycle (QP-2, re-verified by me via direct `grep` —
all five carry `length_provenance="bench_construction"` against a real
`R_OUT_M`/`r_out_m`). None of those five files is, or ever will be, scanned
by gate 4 as it is currently written — a *future* experiment's own `run.py`
introducing a new witness-scale call, correctly or incorrectly tagged,
ships with zero automated cross-check from this trust suite either way. The
runtime `_validate_length_provenance` guard still fires on any unlicensed
*tag* everywhere, always — but it cannot, by construction, ever catch a
syntactically-valid tag that is simply the wrong one for the length it
labels, and gate 4's own source-cross-check, the one thing in this program
that CAN catch that specific failure, is scoped to one file.

---

## 2. Does the guard correctly and completely close T23's original
argument? Yes for the operative rule; no, honestly, for the deeper one —
and the record already says so

`mixed_length_scale_regime`'s own docstring correctly implements
Iteration 23's own closed-by-argument mixed regime: `p_abs_w` is passed in
already-computed, untouched, free to rest on `w_on` (its own licensed
optical basis, per `RATIO_ON`'s own calibration) — while `h_eff`, thermal
mass, and area all derive from `l_geometric_m` alone, and it is exactly
`l_geometric_m` — the length in the Nu=2 conduction role T23's own argument
is about — that `_validate_length_provenance` guards. Structurally, the
guard's scope is drawn in the right place: it does not (and should not)
touch `p_abs_w`'s own length basis, and it does gate the one role T23's
argument concerns. On the OPERATIVE question this cycle was chartered to
close — the specific, three-cycle-old, in-the-open violation of
`L=τ_true/α` reaching a conduction-length role unflagged — the guard closes
it, verified two ways I re-ran myself: the runtime refusal (12/12,
reproduced) and the source-cross-check against the real committed file
(2+3 sites, all correct, reproduced), the latter independently confirmed by
a real deliberate-break test (`git diff`/re-run/revert, RT-1) that is not a
narrated description but an actual transcript against commit `b9323bb`,
which I did not need to re-run myself to trust — it names the exact commit
and exit codes, and gate 4's own logic (which I DID re-derive from scratch
in §1) is sufficient to confirm the transcript's claimed behavior is
correct on its face.

On the deeper claim in Phase 1 §0 — "it resolves T23 permanently and
structurally... any future call, with any future material, is
protected" — my own §1 findings say this overclaims. A `length_provenance`
tag is, and can only ever be, a caller's own declaration; `_validate_
length_provenance` checks a string against an allow-list, never the value
the string is attached to. T23's original argument was a claim about
physical fact (`h=k/L` is self-consistent only when `L` truly is a real
geometric length of the conducting solid) — the tag converts "nobody
checked this claim" into "a caller must assert a category for this claim,"
which is real, load-bearing progress (a caller can no longer stay silent),
but it is not the same thing as the physical claim being independently
verified, and cannot be made the same thing by any string-matching
mechanism, however well the mechanism is built. This is not a defect
unique to exp-064 — it is already conceded, correctly and specifically, in
three places in this cycle's own record (`NOTES.md` Idealization 1, "the
guard enforces DECLARATION, not detection"; Red Team's Phase-2 attack 5,
provenance-TIER vs. provenance-ROLE, non-blocking; THERMODYNAMICS' Phase-2
attack 6, buildability vs. provenance-honesty, fixed via the
`geometric_realizability` field). My own contribution here is independent
confirmation that these disclosures are not merely cautious hedging: §1's
Case 1 and Case 3 show the tag-checking mechanism itself, even restricted
to the one file it does scan, has a live parsing fragility that neither
the Phase-1 proposal, the five Phase-2 critiques, nor Red Team's audit
named in this specific form (nested parentheses, not an unrecognized
name). **Verdict on this sub-question: the guard correctly and completely
closes T23's OPERATIVE rule (the specific violation this cycle targeted);
it does not, and structurally cannot, close the FULL h=k/L
self-consistency requirement — that residual is honestly disclosed
elsewhere in the record, and this review adds one concretely-demonstrated
instance (nested-paren truncation) to the disclosed list.**

---

## 3. Minor, non-blocking: a stale cross-reference

`run_all.py:2128`'s own comment inside `stage23_front_surface_biot_
correction` reads "stage 24 gate 5 below source-inspects THIS file" — but
`stage24_length_provenance_guard`'s own docstring enumerates exactly four
gates, with the source-inspection gate numbered 4, not 5. Cosmetic, does
not affect any check outcome (confirmed — nothing keys off this comment's
text), but worth a one-line fix the next time this file is touched, per
this program's own house discipline about internal cross-references
staying accurate.

---

## Verdict: **PROMISING**

The `length_provenance` guard is a real, sound, independently-verified
close of T23's specific operative violation — not a restated disclosure.
QP-1 through QP-5 and RT-1/RT-2 are all independently re-confirmed here
(suite run, `inspect.signature` behavior, and gate-4's own regex logic all
re-derived from scratch, not merely re-read). Nothing I found is a live
defect in the current commit — every real call site in this repo, in
`run_all.py` and in the four experiment `run.py` files, is correctly
tagged, verified by direct read. What keeps this PROMISING rather than
unqualified is entirely forward-looking and already partially disclosed:
Phase 1 §0's "permanently and structurally... any future call... is
protected" framing is not fully earned by the mechanism as built — §1 of
this review demonstrates two concrete, reproducible ways (nested-paren
truncation; file-scope limited to `run_all.py`) a future mistagged
witness-scale call could ship under a still-green stage 24, beyond the
new-variable-name gap the record already names. None of this reopens T23's
operative question or moves any physics number; it sharpens what "closed"
should be read to mean going forward, exactly the kind of finding Phase 5
exists to surface before the next cycle builds on top of it.

---

## Ranked top-3 for Iteration 42

1. **Harden gate 4 against the failure modes this review demonstrates, and
   extend its reach.** Two independent fixes, both cheap, zero-FDTD,
   directly answering this cycle's own remaining exposure: (a) replace the
   non-greedy `\(\s*(.*?)\)` capture with a parse that is robust to nested
   parentheses — a hand-rolled balanced-paren scanner, or (cleaner) Python's
   own `ast` module to parse each call site's keyword arguments exactly,
   which eliminates the Case-1/Case-3 truncation failure by construction
   and generalizes without new regex tuning; (b) extend the source-scan (or
   add a sibling `numeric_lint.py`/`caveat_lint.py` entry) to also cover
   `experiments/{054,057,059,060}/run.py` — the five real call sites that
   motivated QP-2 — so a future edit to any of those files, not just to
   `run_all.py`, gets the same cross-check. This is squarely this seat's
   own follow-through: the original catch that produced gate 4 was mine;
   verifying and hardening its own remedy is the direct next step, not a
   new proposal.
2. **Source, or at minimum formally model as a third disclosed scenario,
   the CNT-forest root-to-substrate thermal contact resistance**
   (PLAN.md's own undisturbed Iteration-41 queue item 2, MATERIALS'
   Iteration-40 finding) — TD-5's own headroom on κ_solid is 7.8×, this
   program's thinnest safety factor of any kind on record, and any new
   contact-resistance model should itself carry an honest
   `length_provenance`-style declaration for whatever characteristic length
   it introduces, extending this cycle's own discipline forward rather than
   creating a fresh un-tagged length outside it.
3. **Pin the record-blackness/Vantablack-class CNT forest's own pitch/
   diameter AND through-thickness thermal conductivity together, in one
   query set** (PLAN.md's own undisturbed queue item 3) — closes the
   standing near-field-coupling question and the optical/thermal
   material-provenance mismatch at once, and is also the natural home for
   this cycle's own struck §6 thickness-realizability question (not
   restated this cycle, per Red Team's ruling — the underlying question is
   undisturbed, not resolved).

Carried, non-blocking, unchanged from this cycle's own record: the
provenance-TIER vs. provenance-ROLE structural gap (Red Team attack 5);
material-identity coherence across `measured_geometric` sources from
different CNT-forest process classes (MATERIALS attack 7); the §3
cosmetic-comment fix named in §3 above.
