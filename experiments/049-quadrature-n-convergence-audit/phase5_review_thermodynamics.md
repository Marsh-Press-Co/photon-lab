# PHASE 5 — REVIEW · THERMODYNAMICS (fresh context, blind) · exp-049, Panel Iteration 26

*This cycle has no energy content — no absorption, no material, no FDTD call
(confirmed below, §1.0). My own Phase-2 critique this cycle set the one
substantive gate this review is chartered to check: the 972-record
completeness ledger + profiled wall-clock, adopted verbatim as Red Team's
mandatory-fix item 4. Everything else below is this seat's other established
lane — program-integrity/bookkeeping — applied at the scale this cycle's own
Red Team called "the hardest instance yet to catch by inspection alone."
Every load-bearing number below was independently recomputed by directly
invoking the actual committed `design_geometry.py` functions (verification
log at the end), not read off `NOTES.md`'s prose.*

---

## 1. Was my own Phase-2 requirement actually delivered? Yes, and it under-ran, honestly.

**§1.0 — Zero-FDTD claim, checked, not assumed.** `run.py` imports
`design_geometry` from `experiments/042-t21-magnitude-bridge/` unmodified and
calls only `beam_divergence_incoherent`/`_corrected`/`beam_divergence_coherent`
— pure `numpy` over an already-committed analytic propagator. No
`lab/fdtd2d.py` import, no solver call anywhere in `run.py`. Confirmed.

**Ledger count.** `results.json`'s `meta.n_ledger_records` and top-level
`completeness_ledger_count` both read **972**, matching `run.py`'s own
`assert len(ledger) == 972` (line 142) and the arithmetic 36 cells × 3
functions × (8 `N_SERIES` doublings + 1 `n=401` check) = 972 exactly. I did
not just read this number — I re-derived it from `CELLS`/`FUNCS`/`N_SERIES`
independently and it is correct by construction, not by luck.

**Wall-clock.** `meta.elapsed_s = 2743.2353916168213` = **45m43.2s**. `NOTES.md`
and the results commit message both say "45m44s" — a 1-second rounding
slip, cosmetic, not investigated further. Against my own Phase-2 mandatory
fix and Red Team's independently-measured **~52-minute** benchmark-derived
estimate (Attack 4: 76.9s for a 24-call representative sample, linearly
extrapolated to 972 records ≈ 3113s), the actual run landed at **88% of the
profiled estimate** — *under* budget, not over, and disclosed as such in
`NOTES.md`'s Cost section ("close to Red Team's profiled ≈52min estimate").
This is the correct-direction outcome for the exact risk my own Phase-2
critique named: an unprofiled 1.1M-evaluation run silently truncated or
partially reported. It wasn't. The ledger count is exact, the wall-clock is
honestly reported and lands inside the profiled window, and I found no sign
of a partial or short-circuited sweep anywhere in `results.json`'s
`per_cell_summary` (spot-checked: 108 cell-function rows present, each with
`nstar`, `c41`, `c401`, `converged_value` populated, none null except by the
documented `NOT CONVERGED WITHIN RANGE` convention, which never fires here —
`P_NCONV26_4.n_not_converged_within_range = 0`).

**Verdict on my own docket item: delivered cleanly.** This is the one
genuinely good news item of this review.

---

## 2. Auditing Red Team's 8-item mandatory-fix docket against the actual code, one by one

| # | Item | Checked against | Result |
|---|---|---|---|
| 1 | Δrel exemption formula (Attack 5) | `run.py:91-101` `delta_step()` | **Implemented exactly as specified** — `if abs(c_2n)>=C_THR: drel=...,exempted=False; else: drel=None, exempted=True`; convergence requires `dabs<=ABS_TOL and (exempted or drel<=REL_TOL)`. Applied uniformly to `find_nstar()` for every cell×function in the main loop (line 134), not restricted to FWHM=20° — matches Phase 3's "applied across the full 36×3 grid" commitment. |
| 2 | P-NCONV26-0 restated to option (ii) (Attack 7) | `run.py:144-175` | **Implemented as chosen.** Only `coherent` function, only the committed-convention worst-move/n_above_1pct/n_above_0p16pct/worst-cell-identity are checked; no `beam_divergence_coherent_corrected` import anywhere in `run.py` (grep-confirmed). Consistent with the Director's stated reasoning for choosing (ii) over (i). |
| 3 | P-NCONV26-2 split into 3 per-function Spearman bars (Attack 2) | `run.py:216-234` | **Implemented.** Three independent `spearmanr` calls, each own `outcome` keyed to `rho>=0.70`/`<0.30`. `results.json` carries three separate blocks (`incoherent`/`incoherent_corrected`/`coherent`), each independently PARTIAL — no pooling anywhere. One disclosed implementation choice not spelled out in `phase3_synthesis.md`'s prose: exempted cells are ranked by `(dabs/ABS_TOL)*REL_TOL` (line 227) rather than by `drel` (undefined for those cells) — a reasonable, code-comment-disclosed choice, not a defect. |
| 4 | Completeness ledger + profiled cost (Attack 4) | `run.py:121-142`, `meta` block | **Implemented, verified in §1 above.** |
| 5 | PLAN.md follow-up trigger for A=724 geometry (Attack 1) | `PLAN.md` (grepped for "exp-049", "A=724", "n-convergence") | **Not yet present.** `PLAN.md` has no post-exp-049 entry. This is *not* a fix-docket-delivery failure at this point in the cycle — per `PANEL.md`, the Director updates `LOGBOOK.md`/`PLAN.md`'s queue at Phase 5 **close-out**, after all seven seats report, which has not happened yet. Flagged as a **watch item**, not a violation: `idealization 7` in `NOTES.md` commits to this trigger explicitly, and given MATERIALS' own citation of the six-iteration T21 geometry-drift precedent this trigger exists to prevent, it should not be allowed to slip past this cycle's own close-out commit. |
| 6 | Inline T24 caveat on P-NCONV26-5 (Attack 6) | `NOTES.md` predictions table | **Present**, attached directly to the P-NCONV26-5 row, not only in idealization 5 — matches the mandatory fix's own "not only idealization 5" requirement. |
| 7 | THERMO's own arithmetic correction (Attack 3) | `results.json` `P_NCONV26_5.margin_ratio`/`margin_headroom_pct` | **Present and independently reproduced by me**: `0.005/0.004006497410421138 = 1.247972852046454`, headroom `24.79728520464539%` — matches to the last printed digit (§3 below). |
| 8 | P-NCONV26-4 aside demoted to descriptive (Attack 8) | `run.py:329-335`, `results.json` `P_NCONV26_4_aside` | **Present**, carries no `outcome` key (not scored), explicit `note` field states "Descriptive only, not scored." |

**7 of 8 fully delivered in code; the 8th (PLAN.md trigger) is legitimately
pending Phase-5 close-out, not dropped.** This is a materially cleaner
delivery record than several recent cycles this program's own LOGBOOK has
logged.

---

## 3. The sharpest test of my own named risk — and a real catch none of the six blind seats above could have made (they don't exist yet at Phase 2)

Task (b) asked me to find *any* claim stated as done that isn't actually
reflected in `run.py`'s logic or `results.json`'s output. I found one, and it
is real, if non-load-bearing:

**`NOTES.md`'s Phase-4 erratum section states:** *"both the buggy and
corrected computations are preserved in `results.json` (`P_NCONV26_2` and
`P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY`), `run.py`'s fix is documented inline at
the point of the bug"* — creating the clear impression that the preserved
buggy-erratum block is, like everything else in this file, traceable to
committed code.

**It is not.** I read `run.py` in full (388 lines) and grepped it for
`ERRATUM`/`BUGGY`: the only hit is the *docstring comment* documenting the
bug (line 70) — there is no code path anywhere in `run.py` that computes or
writes a `P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` key. Yet `results.json` (same
commit, `e5c32b1`) contains exactly that block, with `spearman_rho` values
that are the exact negatives of the corrected ones and *identical p-values*
— mathematically consistent with a genuine reversed-rank Spearman
computation, so I do not believe the numbers were fabricated from nothing.
But **the committed `run.py`, if re-run today, would not reproduce this
block** — `main()`'s `results` dict has no such key, and `json.dump` with
mode `"w"` overwrites the whole file, so a fresh run would silently *drop*
the erratum-preservation block that `NOTES.md` presents as a durable,
code-traceable disclosure. I confirmed via `git diff 7699de5 e5c32b1 --
run.py` that the only code change between the Phase-4-implementation commit
and the results commit was the one-line rank-formula sign fix — no erratum-
preservation logic was ever added, run, and then stripped; it was never
there.

**This is exactly the species of finding this cycle's own Red Team ruling
predicted at the highest-risk item (Attack 4) and my own Phase-2 critique
named**: not wrong physics, but a completeness/traceability claim that
outruns what the committed code actually does — the program's own named
fix-docket-delivery pattern, recurring one cycle after R4 was invoked twice
in this same cycle's own Phase 2/Red Team text. **Severity: low.** It does
not touch any scored outcome — `P_NCONV26_2`'s own PARTIAL verdict (ρ=0.45–
0.48, all three functions) is unaffected, the erratum block is disclosure-
only, and the values are internally consistent (exact sign-flip, identical
p-values) rather than arbitrary. But it means this cycle's own results.json
is **not fully bit-reproducible from its own committed run.py** — a real gap
against this program's repeatedly-stressed determinism discipline (LOGBOOK:
"nine FDTD legs reproduced bit-identically... a free determinism check,"
Iteration 23; the R4 rule itself, adopted specifically to stop
"precisely recomputed" claims that don't trace to committed code).

**Recommendation, not a blocking finding:** either (a) add the four-line
erratum-replay path back to `run.py` (trivial: call `spearmanr` once against
the pre-fix rank dict, exactly as the docstring already describes) so a
fresh run reproduces the full committed `results.json`, or (b) if that is
judged not worth the code-cleanliness cost, say explicitly in `NOTES.md`
that this one block is a one-time session artifact, not regenerated by
`run.py` — rather than the current phrasing, which reads as a stronger
reproducibility guarantee than the code delivers.

---

## 4. Independent arithmetic recomputation (task c) — invoked the real functions, not retyped digits

I ran the actual committed `experiments/042-t21-magnitude-bridge/design_geometry.py`
functions directly (not `run.py`, to keep the check independent of this
cycle's own scoring code):

**(i) `P_NCONV26_5` margin/headroom** — `0.005 / 0.004006497410421138 =
1.247972852046454`, `24.79728520464539%` headroom. Matches `results.json`
exactly. Confirms Attack 3's correction was actually applied, not just
promised.

**(ii) The regression-gate worst cell (`P_NCONV26_0`/`P_NCONV26_8`)** —
called `beam_divergence_coherent(36, 20, 15, n=41)` and `n=401` directly:
got `c41=-0.965320384302972`, `c401=-0.9239930504205042`, giving
`100·|c401−c41|/|c401| = 4.472688822027389%` — matches `results.json` to
every printed digit, and matches exp-046's own cited figure exactly (the
regression gate's whole point).

**(iii) The full n* determination at that same cell** — computed all 8
`N_SERIES` values by direct function call and ran the two-consecutive-pass
logic by hand: step 41→81 fails (`Δrel=4.4747%`), but 81→161 and 161→321
both converge cleanly (`Δrel=0.0019%`, `0.0000021%`) — so `n*=81`, matching
`results.json`'s `per_cell_summary` entry exactly (`nstar: 81`,
`converged_value: -0.9239752489621912`, reproduced bit-for-bit). This also
independently confirms `P_NCONV26_8`'s reported `worst_coherent_move_pct =
4.474701609942433%` (a *different* quantity from (ii) — measured against
`c[n*]` not `c401` — correctly not conflated in either `run.py` or `NOTES.md`).

**(iv) `P_NCONV26_5`'s own cell** — called
`beam_divergence_incoherent_corrected(38, 2, 25, n=41)` and `n=401` directly:
`c41=-0.004006497410421138`, `c401=-0.00400649743780568` — both match
`results.json` exactly, confirming the sharpest-stakes cell really is
converged to ~10⁻⁹% as claimed, not asserted.

**Zero arithmetic defects found in anything I checked.** Every figure I
recomputed traces to a genuine invocation of the actual committed function —
the opposite of R4's failure mode, everywhere except the one gap in §3.

---

## 5. Constraint / expressibility / REALIZABILITY_MEMO check

Independently re-confirmed MATERIALS' and Red Team's own finding:
`gaussian_angle_weights`/`beam_divergence_*` feed only the T21
contamination-risk channel, never `REALIZABILITY_MEMO.md`'s σ(I) tables or
Entry 2's `C=−0.7209` anchor (a different code path, `edge_diffraction_c_empty
[_corrected]` at a single fixed θ). No T1 escape route is claimed or implied
(grep-confirmed, as Red Team already did); no constraint-3/4 verdict issued.
This cycle cannot move a Checkpoint criterion 1 or 2 finding, and does not
attempt to.

---

## Verdict

**PROMISING.**

The central hypothesis this audit was built to test (P-NCONV26-1a: n=41 is
genuinely under-converged for the coherent function at FWHM=20°) held
cleanly, all 8 of Red Team's mandatory fixes are — with one legitimately-
pending, non-code item — delivered in the actual committed code, my own
Phase-2 completeness/wall-clock gate was met and undershot honestly, and
every figure I independently recomputed by invoking real code matched to the
printed digit. The one real defect I found (§3) is a genuine, if
non-load-bearing, instance of this program's own repeatedly-named pattern —
worth fixing before it is cited as a model of clean erratum disclosure, but
not a threat to any scored outcome, and cheap to close. This is a materially
cleaner cycle than the last several Phase-5 audits on record.

## Top-3 ranked candidate next steps for the program

1. **[Cheapest, this seat's own lane.]** Close the `P_NCONV26_2_ERRATUM_
   ORIGINAL_BUGGY` reproducibility gap (§3): either restore the four-line
   replay path in `run.py` so the committed `results.json` is fully
   regenerable, or explicitly downgrade `NOTES.md`'s claim to "a one-time
   session computation, not regenerated by `run.py`." A same-shift, zero-cost
   fix that closes a real gap before a future cycle cites this one as a
   clean-disclosure precedent.
2. **[Follow-through on Attack 1 / idealization 7.]** Land MATERIALS' A=724/
   NY=1528 follow-up trigger in `PLAN.md`'s queue at this cycle's own
   close-out — or better, spend a fraction of this cycle's own budget
   re-running just the FWHM∈{10°,20°} subset (the only cells this audit found
   sensitive to `n`, ~17 of 108 combinations) at exp-048's fallback geometry
   directly, closing the citation-scope gap with data rather than a second
   promise, before this program pays a second multi-iteration price for the
   same class of geometry drift T21 already cost it once.
3. **[Standing THERMODYNAMICS-charter item, overdue since Iteration 25
   close.]** Resume the queued `h_eff` re-derivation for this program's two
   thinnest surviving detectability margins (exp-043's ON-endpoint,
   ~5.1×→~2.6× under the T8/T13/T14 correction; exp-045's dose-accumulation
   figure, ~27,080×→~38–42×) — a genuine energy-budget question, unlike this
   cycle, and the next substantive item on THERMODYNAMICS' own rotation slot
   before a fresh T1 mechanism proposal is due.

---

## Verification log — what I actually did

**Files read in full:** `PANEL.md`; `LOGBOOK.md` in full (9413 lines,
including RULED OUT R1–R4, the LIVE THREADS index, and Iterations 22–25 in
full for the fix-docket-delivery pattern's own history and the R4 rule's
adoption); `experiments/049-.../phase1_proposal.md`,
`phase2_critique_thermodynamics.md` (my own prior critique this cycle),
`phase2_critique_materials.md`, `phase2_critique_em.md`,
`phase2_critique_quantum.md`, `phase2_critique_vision.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`
(388 lines), `results.json` (1331 lines, `meta`/`predictions`/`per_cell_summary`
all read).

**Commands run:** `lab/validation/run_all.py --only 12346789` → **41/41
passed, 79s** — independently reconfirms `NOTES.md`'s "trust suite
re-verified 41/41 immediately before the run" claim. `git log --oneline` and
`git diff 7699de5 e5c32b1 -- run.py` (confirms the only code change between
the Phase-4-implementation and results commits is the one-line rank-sign
fix — no erratum-preservation code was ever present). `git show e5c32b1
--stat` (confirms `results.json` and the erratum block landed in the same
commit as the unchanged-in-that-respect `run.py`). `grep -n "ERRATUM|BUGGY"
run.py` (one hit, a docstring, no code). `grep -n "exp-049|A=724|n-convergence"
PLAN.md` (no post-cycle entry yet — expected, pending close-out).

**Python executed directly against the real code** (not `run.py`): imported
`experiments/042-t21-magnitude-bridge/design_geometry.py` and called
`beam_divergence_coherent`/`beam_divergence_incoherent_corrected` at the
cited cells and every `N_SERIES` order, reproducing `c41`, `c401`, the
two-consecutive-pass `n*` determination, `worst_move_pct`, and the P-NCONV26-5
margin/headroom figures — all matched `results.json` to the last printed
digit (§4).

**Ruled-out check:** nothing in this cycle or this review resurrects R1, R2,
or R3 — no mechanism, no cloaking, no shell-thickness claim anywhere in
`phase1_proposal.md`, `phase3_synthesis.md`, `NOTES.md`, or `run.py`.
