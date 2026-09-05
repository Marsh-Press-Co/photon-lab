# Phase 5 Review — THERMODYNAMICS (partial self-review: I found Fix 1 at
# this cycle's own Phase 2, blind to every other seat's Phase-5 output)

**Panel Iteration 89, exp-112.** Charter: where absorbed energy goes;
always asks what re-radiates and whether it would be detectable; owns the
per-proposal energy sidecar (post-run analytic, labeled as such). This is
a hybrid review — a fresh Phase-5 pass over the whole cycle, plus an
honest self-audit of my own Phase-2 critique's downstream consequences,
since the Phase-4 record surfaced a second instance of the exact failure
shape I found first. Every number below was independently re-derived or
re-executed this session, from the raw capture data where the raw data
still exists, not read off `NOTES.md`/`results.json` prose.

## Verdict: **PARTIAL, CONFIRM-WITH-ONE-ACTIONABLE-GAP**

Fix 1 (module collision) and Fix 6 (energy ledger) both genuinely,
verifiably land — I reproduced `results.json` **byte-for-byte** from the
raw field captures by re-running the whole committed pipeline myself
(`git diff` on the regenerated file: empty). The named bin's own physics
question stays genuinely open (Check A: AMBIGUOUS; Check B: SURVIVES;
Check C: a striking 0.9994 correlation) — not my charter's call, not
re-litigated here. My own charter's real finding this cycle is elsewhere:
this cycle's own real wall-time data, now that it exists for the first
time, contradicts the cost-gate projection that was used to defer the
r=312 leg — a genuine, actionable, non-blocking finding for Iteration 90.
Separately: I do not believe the second R29 collision fires Checkpoint
criterion 4, for reasons stated in §4, but flag it as a closer call than
R29's own text anticipated. And, asked to be honest about my own Phase-2
critique's thoroughness: it was not exhaustive, in a specific, nameable way
(§5).

## 1. Fix 1 (module collision) — verified by actually re-executing the pipeline end to end, not by re-reading the diff

The raw capture data this cycle produced (`empty`/`hollow`/`peccored`
`done.pkl` files, ~125-141 MB each) is still present in this session's
scratch directory. I used it to re-run the entire Phase-4 pipeline fresh,
independent of anything `NOTES.md` or `results.json` claims:

- `python3 chunk_runner112.py 156 25 {empty,hollow,peccored}` — all three
  correctly report "already DONE," reading back the real wall-time logs
  (221.5s/224.1s/224.9s). No `AttributeError`, no silent misaliasing.
- `python3 run112.py --verify-geometry` → `{"pass_": true, "mismatches":
  []}` at both r, confirmed live, not merely quoted from Phase 1.
- `python3 analyze.py`, run completely fresh (after copying the committed
  `results.json` aside): **reproduces the committed `results.json`
  byte-for-byte** — I wrote a recursive float/string comparator (rel. tol.
  `1e-9`) over the two files and it reports zero differences anywhere,
  including the 48-bin arrays, the resolution-check dict, and both text
  fields. `git diff` on the regenerated file is empty.
- The **second**, previously-undiscovered collision `NOTES.md` discloses
  (`analyze.py`'s own `import chunk_runner as CR` resolving to exp-110's
  `chunk_runner.py`, not this directory's own) is also confirmed fixed:
  `chunk_runner112.py` exists, `analyze.py`'s own
  `assert EXP110_DIR_NAME not in os.path.dirname(CR.__file__)` is present
  and — confirmed by my own fresh run completing to `results.json` without
  raising — fires correctly.

This is the strongest form of verification available to a Phase-5 seat:
not re-reading source, not re-invoking a function in isolation, but
regenerating the entire scored artifact from the same raw inputs Phase 4
used and diffing the result. **Fix 1 is genuinely, fully closed, for both
the disclosed and the undisclosed-until-Phase-4 instance of the
collision.**

## 2. Fix 6 (energy ledger) — genuine, but the "internal consistency" check my own Phase-2 critique invited is a tautology; I supply the real one

`results.json["energy_ledger"]` persists `sigma_scat`/`sigma_abs`/
`sigma_ext` for both captures, exactly as my own Phase-2 critique (Docket
Fix 6) asked. I re-derived every one of these eight numbers **myself**,
directly from the raw `.pkl` captures, by calling `lab.sections.widths()`
fresh — bit-exact match to the committed ledger.

**But**: my own Phase-2 critique's framing ("confirm internal
consistency: `sigma_scat+sigma_abs` vs `sigma_ext`") is not a real check.
I read `lab/sections.py` line 150 directly: `"sigma_ext": (p_scat +
p_abs) / i_inc` — `sigma_ext` is **defined** as the sum, not independently
measured. `sigma_scat + sigma_abs == sigma_ext` is a code-level identity
that holds by construction for *any* input, correct or corrupted; it
cannot fail, so it provides zero evidence the two components were
computed from real, correctly-wired field data. If I had stopped here (as
the phrasing I used at Phase 2 invites a future reader to), I would have
been citing a tautology as a physical check — precisely the kind of
"confirmed the arithmetic, never asked whether the operands are the right
quantities" gap R9 (LOGBOOK RULED OUT registry) exists to warn against,
here one level removed (a formula-level identity rather than a unit
mismatch).

I supplied the actual independent check instead: `lab/sections.py` also
computes `sigma_ext_cross` (`p_ext_cross = -_cross_flux(pi, ps, box)`), a
**genuinely different** measurement route — the optical-theorem
interference term between the incident and scattered fields, not a sum of
the other two channels. Re-derived from the raw captures myself:

| config | `sigma_scat+sigma_abs` | `sigma_ext_cross` | rel. dev. |
|---|---|---|---|
| peccored | 700.1082897642503 | 700.1129451080386 | 6.65×10⁻⁶ |
| hollow | 700.1233206386078 | 700.1279759823958 | 6.65×10⁻⁶ |

Two structurally independent routes to the same extinction cross-section,
computed from the raw field data by two different formulas, agree to
6.6 parts per million at both configs. **This is the real evidence the
energy-ledger numbers are genuine, physically self-consistent field
measurements, not miswired or copy-pasted values** — the check my own
Phase-2 language should have named, not the tautological one. Recommend
any future document citing this ledger's own genuineness cite
`sigma_ext_cross`, not the scat+abs=ext identity.

## 3. A physically substantive reading of the new ledger (my own charter's actual question)

Beyond "is Fix 6 wired correctly," the ledger answers a real question my
own Phase-2 critique posed: does the PEC-core-vs-hollow difference in
*absorbed power* track the same signature the −146.25° bin's scattering
pattern shows? **No** — and that is itself informative. `sigma_abs`
differs between peccored (349.5371) and hollow (349.5228) by only
**0.004%**; `sigma_ext` differs by only **0.002%** (700.1083 vs 700.1233).
Both configs' *total* interaction with the field is, to within a few parts
in 10⁴, identical — exactly as physically expected (the PEC core cannot
absorb; only the shell, present in both configs, does). This independently
reaffirms, at a **new** resolution point (`cpl=25`, not previously
checked), the mechanistic account this program established at Iteration
65 (R14, LOGBOOK RULED OUT registry, THERMODYNAMICS' own contribution
there): the named bin's comparatively large local angular deviation
(9.88%→14.3% between `cpl=20`→`cpl=25`) is forced, by this now-twice-
confirmed total-cross-section flatness, to live entirely in the **angular
redistribution** of an essentially-conserved total power — not in a
genuine difference in how much power the two configs intercept overall.
Whatever Check A/B/C's own eventual verdict on the named bin turns out to
be, it will be a claim about *shape*, never about *total budget* — a
constraint a future cycle interpreting this bin should carry forward
explicitly.

## 4. The second R29 instance — does it fire Checkpoint criterion 4?

`NOTES.md`'s own Phase-4 section discloses a second manifestation of the
identical collision shape (`chunk_runner.py`/`chunk_runner.py`, this time
in `analyze.py`'s own `import chunk_runner as CR`), found only when
Phase 4 execution got far enough to reach it — Phase 2's blind critiques
(mine included) never got past the *first* collision's crash point to
exercise this line. It explicitly declines to self-adjudicate the
Checkpoint question and asks Phase 5 to do so. My reasoned view, checked
directly against R29's own ratified text (LOGBOOK RULED OUT registry) and
this program's own precedent for every prior forward-firing rule:

**Does not fire.** R29's own text names its founding instance as
"exp-112 (this cycle)" — the whole cycle, not a single file-level event —
and every prior single-instance-ratified rule in this registry (most
directly R16 and R18) reserves its forward-firing clause for a **reuse of
an already-fixed, already-known defect** by an author who had the
opportunity to know and decline the rule — not a second symptom of one
not-yet-fully-diagnosed root cause, discovered progressively within the
very cycle that first named it. Both collisions were written in the same
Phase-1 sitting, **before R29 existed as a rule at all** (it was only
proposed by Red Team's Phase-2 audit and ratified at Phase 3 — after both
collisions were already committed). Nobody had the chance to consult R29
and ignore it when `analyze.py`'s `import chunk_runner as CR` line was
written. Both instances were fixed same-shift, before any result was
scored, with zero live self-contradiction surviving to a frozen verdict —
matching this registry's own "does not fire on its own founding instance"
precedent cleanly.

That said, I flag this as a **closer call than R29's own founding text
anticipated**: unlike R16/R18's clean prior-cycle-vs-current-cycle
boundary, here the rule was *textually* ratified (Phase 3) a few phases
before the second manifestation surfaced (Phase 4), purely as an artifact
of how far the crash-driven discovery process happened to reach at each
phase. A future case where a second manifestation surfaces after a
same-cycle ratification, but under less clearly-shared authorship-timing
facts than this one, could go the other way. **Recommend**: the Director
or Red Team add a short addendum to R29's own text, disambiguating
"second instance" as meaning a *future cycle's* reuse of the
collision-prone idiom after R29 could actually have been consulted — not
a second manifestation of one root cause discovered progressively within
its own founding cycle — so this exact ambiguity doesn't have to be
re-litigated from scratch next time it recurs.

## 5. Honest self-audit: did my own Phase-2 critique's thoroughness actually close this?

Asked directly, and I looked for the failure mode rather than assuming it
away. **No, not fully** — and the gap is nameable. My Phase-2 critique
caught the `run.py`/`run.py` collision by *executing* the code and
observing the crash (`python3 chunk_runner.py 156 25 empty` →
`AttributeError`). That is real, valuable verification — but it verifies
"does this specific invocation crash," not "is this cycle's own import
graph free of same-basename collisions anywhere." The second collision
(`chunk_runner.py`/`chunk_runner.py`, inside `analyze.py`) was **equally
present and equally discoverable at Phase 2**, by a strictly more general,
still zero-marginal-cost check I did not perform: statically list every
bare `import <name>` in the Phase-1 files, and check whether `<name>.py`
exists in more than one directory those same files add to `sys.path` —
independent of whether execution ever gets far enough to crash on it.
That check requires no FDTD data, no captures, nothing Phase 2 lacked; it
is a pure source-and-filesystem read. I performed the narrower "run it and
see" check, which was sufficient to justify a support-with-changes verdict
on the instance I found, but not sufficient to rule out a sibling instance
of the identical authoring pattern sitting one crash-point further down
the same file. This is the same general shape this registry has already
named elsewhere (R13/R14's "check the general instability shape, not just
the one point that happened to trigger it") — recurring here in a code-
hygiene check rather than a numerical one. It did not reach a frozen
record uncorrected (Phase 4 caught and fixed it, same-shift, before any
verdict was scored), so I do not think it demotes my own critique's
verdict retroactively — but I would score my own Phase-2 critique as
**adequate, not maximally thorough**, on this specific axis, and recommend
R29's own mandatory-verification text be tightened to require the general
static duplicate-basename sweep (not merely "re-run and confirm it no
longer crashes") for any future cycle that imports more than one
same-basename module.

## 6. Wall-time accounting — a genuine, previously-undisclosed cross-session confound, my own charter's headline finding

`NOTES.md` discloses the mismatch in passing ("well under the 1469.19s
projection... the extrapolation was a projection, not a promise") but does
not pursue why, or what it implies for future cost-gate decisions. I did.

**The numbers.** `cpl_cost_table.py`'s own `ratio**3` extrapolation
(`ratio=1.25`, applied to exp-110's own real `cpl=20`/r=156 baseline,
752.22s total, 250.6/250.1/251.5s per scene) predicted **1469.19s**
total / **489.7s** per scene for this cycle's `cpl=25`/r=156 leg. The real
measured total was **670.48s** / **221.5–224.9s per scene** — the real
figure is **45.6%** of the projection, a **>2× miss**, in the safe
(over-conservative) direction this time — the opposite direction from
R28's own founding ~15% *anti*-conservative miss on the `kappa_ratio`
(r=312/r=156) axis.

**Why this matters beyond "the estimate was loose."** The projected
figure was not cosmetic — it was fed directly into the real, executed
`R.cost_gate_check()` to decide this cycle's own scope (§2.0 of the
proposal), and that decision REFUSED an r=312 expansion
(`proceed_to_r312=False`, projected 14906.3s > the 10800s bound). I
re-invoked the same, real, unmodified `R.cost_gate_check()` myself, this
time with the actual measured pilot now that it exists:

```
Real pilot (670.48s total, 221.53s empty):
  projected_312_total_s = 6802.64s
  total_pass = True, proceed_to_r312 = True
Projected pilot (1469.19s total, as actually used by the proposal):
  projected_312_total_s = 14906.30s
  total_pass = False, proceed_to_r312 = False
```

**The gate's own decision flips.** By the real numbers now in hand, an
r=312/`cpl=25` expansion would very likely clear the existing
`COST_GATE_TOTAL_S` bound with room to spare (6802.6s vs. 10800s) — the
opposite of the conclusion the proposal's own scope decision (§3, "very
likely the ONLY option this cycle's own gate would currently clear")
reached using the best information available *before* Phase 4. This is
not a criticism of that scope decision, which was the only reasonable
call given a projection, not real data — it is a finding for Iteration 90:
**do not treat the r=312 deferral as still gate-bound; re-run the real
gate with the real pilot before deciding whether to defer it a third
time.**

**Root cause, independently traced, not merely observed.** Why did the
projection miss by 2.2×, when `cpl_cost_table.py`'s own `ratio**3` law is
the geometrically-motivated one (cell count scales `ratio²`, step count
scales `ratio` to hold optical-period count fixed — verified directly:
`STEPS·S/lam=320·S` at both `cpl`, so total cell-steps genuinely scale as
`ratio³=1.953×`)? The real per-scene wall time **decreased** from `cpl=20`
(exp-110, a prior session: ~250.7s/scene) to `cpl=25` (this session,
~223.5s/scene) — a genuine 11% *drop* in wall time despite 1.953× more
raw numerical work. The only accounting that fits: **this session's
underlying compute throughput is roughly 2.2× that of exp-110's own
session** (0.0279s/step at `cpl=25` here vs. an implied 0.0391s/step
scaled 1.5625× for cell count would predict 0.0611s/step if throughput had
been unchanged — the actual figure is well under half that). Both
sessions' own chunking behavior is internally consistent (4 chunks of
2200/2200/2200/1400 steps this cycle, matching `STEPS=8000`; no anomalous
single-chunk outlier) — this is not a chunking or I/O artifact, it is a
genuine session-to-session machine-speed difference roughly the same
order of magnitude as, or larger than, the geometric law itself.

**Why this is a standing concern, not just this cycle's own footnote.**
`cpl_cost_table.py`'s `ratio**3` heuristic and `cost_gate_check()`'s own
`KAPPA_COST_EXPONENT=3.2053` (R28, Iteration 87) both implicitly assume a
stable "wall-seconds per unit of numerical work" that transfers when a
NEW session's own pilot is combined with an OLD session's own baseline or
exponent. `KAPPA_COST_EXPONENT` itself was derived from a single-session
pair (exp-110's own r=156/r=312, same sitting) so it is not directly
undermined here — but `cpl_cost_table.py`'s own projection, and any future
cycle that reuses either constant against a **cross-session** pilot (as
this cycle did, combining exp-110's `cpl=20` baseline with this session's
own `cpl=25` execution), inherits an unquantified, previously undisclosed
machine-speed factor that this one data point shows can exceed 2× — larger
than the ~15% miss R28 was created to fix. No prior LOGBOOK entry names
this axis (checked: no hit for "cross-session," "machine speed," or
"hardware" anywhere in the registry). **Recommend** (Iteration 90, cheap,
zero new FDTD): before trusting any wall-time-based cost projection that
combines pilot data from two different sessions, add a one-scene,
same-session control point — re-time one already-completed, cheap scene
(e.g., a fresh `cpl=20`/r=156/empty run, ~250s) at the start of the new
session, and scale the cross-session baseline by the ratio of that control
time to its own historical figure, before combining it with the new
session's own pilot in any gate decision.

## 7. Ranked next-step recommendation for Iteration 90

1. **Re-invoke `R.cost_gate_check()` with the real measured `cpl=25`/r=156
   pilot (670.48s total / 221.53s empty) before treating the r=312
   expansion as still deferred.** Zero new FDTD, one function call — by
   the real numbers this clears the existing bound with ~37% margin
   (6802.6s vs 10800s), directly unblocking PHOTONICS' own twice-deferred
   `+168.75°` companion bin, the single highest-value item this sub-thread
   has queued.
2. **Add a same-session control point to any future cross-session
   wall-time-based cost projection** (§6) — the single largest, previously
   undisclosed source of cost-gate error this program has found to date,
   larger than R28's own founding ~15% miss, on this one data point.
3. **If item 1 clears the gate for real**, run the `+168.75°` bin at
   r=312/`cpl=25` with the SAME three-check (A/B/C) instrument used here —
   the genuinely next-most-informative physics step, and the only way to
   learn whether Check C's striking 0.9994 correlation at −146.25° is a
   general property of this near-null angular region or specific to one
   bin.
4. (Governance, cheap) Ask the Director/Red Team to add the R29 timing
   addendum named in §4, and tighten R29's own mandatory-verification text
   to require the general static duplicate-import-basename sweep named in
   §5, not merely "re-run and confirm no crash."
5. (Non-blocking, documentation) Any future citation of the `energy_ledger`
   field's own genuineness should point to `sigma_ext_cross` vs.
   `sigma_scat+sigma_abs` (§2, agree to 6.6 ppm) — not the tautological
   scat+abs=ext identity my own Phase-2 critique's phrasing invited.

## Independently reproduced artifacts

`chunk_runner112.py` (all 3 scenes), `run112.py --verify-geometry`, and
`analyze.py` all re-run fresh this review directly against the raw capture
data still present in this session's scratch directory; regenerated
`results.json` diffed byte-for-byte against the committed file (zero
differences). `energy_ledger`'s four cross-sections independently
re-derived via `lab.sections.widths()` from the raw captures (bit-exact)
plus the additional `sigma_ext_cross` cross-check (not itself persisted,
computed fresh this review). House trust suite re-run fresh: 43/43 green,
110s. `git log`/`git diff --stat` used directly to confirm Predictions
(`19c4ac8`, 03:44:37 UTC) committed ~17 minutes before Phase-4 results
(`e2d660f`, 04:01:23 UTC), and zero `lab/` diff across the full cycle.
