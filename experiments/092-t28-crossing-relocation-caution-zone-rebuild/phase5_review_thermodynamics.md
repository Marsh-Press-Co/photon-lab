# PHASE 5 — REVIEW · Seat: THERMODYNAMICS · Panel Iteration 69 · exp-092

Fresh sub-agent, blind to any other seat's current-cycle Phase-5 review (per
this cycle's own blind-review instruction, no other `phase5_review_*.md` for
this cycle was sought or read). Read in full: `PANEL.md`; `LOGBOOK.md` in
full, offset-by-offset (RULED OUT R1–R15 with full founding text; ESTABLISHED;
LIVE THREADS, including the complete T28 sub-thread narrative Iteration
46→68); the complete exp-092 record (`phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`run.py`, `results.json`, `run_output.txt`); `lab/thermo_sidecar.py` in full;
cross-checked against `experiments/087,090,091`'s own `run.py`/`results.json`
where a claim needed a primary source this cycle's own record does not
contain. I have zero memory of critiquing this cycle at Phase 2 —
`phase2_critique_thermodynamics.md` is read here as a finished document
belonging to a different, now-closed agent, exactly like any other seat's,
per the task brief's own instruction to check whether it was actually
adopted and correctly executed.

## Verdict: **CONCUR with (the likely) PARTIAL — genuinely load-bearing,
correctly-verified physics, with one real, charter-owned reporting gap and
one imprecise mechanistic citation, neither of which changes any scored
verdict this cycle filed.**

Every load-bearing number I independently re-derived — `sigma_max_R3=1/3`
from `lab/materials.py`'s own `τ_center=2σr_out` convention, the R3b
`p_abs_w` ratios and `ratio_abs_ext` deviations from `results.json`'s own
raw fields, and (via direct execution) the actual NETD classification this
cycle's own sidecar chain computed but never surfaced — reproduces exactly
or confirms the write-up's own claim. My own Phase-2 flip condition (a
pre-registered `p_abs_w`/`ratio_abs_ext` band for Rank 3) was adopted
verbatim, correctly gated as non-gating/co-equal-PRIMARY, and CONFIRMed
cleanly at all three angles — a genuine methodological win, not a rubber
stamp. But two things belong on this cycle's own record that are not on it:
(1) this cycle's own `netd_disposition` chain computes a full detectability
classification for every one of its ten unique (config,θ) cells and reports
**none of them**, anywhere — not a disclaimer-carry-forward failure (the
disclaimer text itself propagated flawlessly), but the inverse: the *data*
the disclaimer exists to qualify is simply missing, a defect I trace to
exp-091's own machinery (not new to this cycle, but silently reproduced a
second consecutive time, still unnamed anywhere in the record until now);
(2) the write-up's own explanation for the (R3b) result's small, tight
~3.8–4.0% magnitude — credited to "near-saturation... almost exactly"
matching my own prior-cycle prediction — both overclaims the precision of
what that prediction actually committed to (a broad `[0.3,3.0]` band, no
magnitude), and reaches for a physical picture (bulk absorption
saturation, à la Beer–Lambert) that this program's own ESTABLISHED record
has repeatedly and explicitly warned is the *wrong* picture for this
near-field regime — a more precise, already-established, and more
falsifiable citation (the extinction paradox, T9) predicts the same
direction more sharply and is cheaply testable on the existing pipeline.

## 1. My own Phase-2 flip condition — adopted and correctly executed (verified from source, not from NOTES.md's own retelling)

`phase2_critique_thermodynamics.md` asked for a pre-registered CONFIRM/
REFUTE band on `p_abs_w` and `ratio_abs_ext` under Rank 3, "mirroring
exp-091's own (b2) convention," with an explicit directional lean (a
*decrease* toward the native value, since T9's flat ~0.51 anchor argues the
effect should track resolution-only staircasing, not scale linearly with a
33% σ cut). Tracing the chain:

- `phase2_redteam_audit.md` §1.3 independently re-derived the same gap from
  primary sources (`phase1_proposal.md` §6 scores only `delta_scene`/
  `frac_contrast`, confirmed) and ruled it **mandatory**, not discretionary
  — item 3 of the seven-item docket.
- `phase3_synthesis.md` §3 item 3 adopted it verbatim as `(R3b) PRIMARY,
  non-gating`, correctly scoping it as *not* feeding the sigma_max branch
  decision (§4 of the same document restricts the gate to `delta_scene`/
  `frac_contrast` only) — the right call: R3b answers a different,
  co-equal question (does the energy channel move?) from R3's own gating
  question (does the interference channel move enough to redirect Rank 1's
  20+ calls?), and conflating the two would have made a small, expected
  energy-channel wobble able to veto an unrelated crossing-search budget
  decision.
- `run.py:374–384` computes `r3b_verdict = ratio_sign_verdict(rank3_pabs_cells)`
  as an independent worst-case-across-three-angles verdict, separate from
  `r3_verdict` — confirmed in code, not merely in `results.json`'s printed
  field.
- The result: `results.json::rank3.r3b_verdict = "CONFIRM"`, with
  `p_abs_w_ratio` = 0.9610213/0.9619166/0.9602062 at 37.2°/40.2°/41.4° and
  `ratio_abs_ext_dev_from_anchor` = 0.77%/0.54%/0.93% — I recomputed both
  directly from the raw fields in the same JSON object
  (`sigma_corrected_p_abs_w_c / filed_p_abs_w_c` and
  `|sigma_corrected_ratio_abs_ext_raw − 0.51| / 0.51`) and both reproduce
  to the printed digit.

**My own flip condition was correctly adopted, correctly scoped as
non-gating, and correctly executed — this is a genuine, verifiable
methodological improvement over exp-091's own (b2) precedent, not
box-checking.** Section 3 below revisits whether the *interpretation*
attached to the CONFIRM result is as sound as its computation.

## 2. NETD/detectability: computed for every cell, reported for none — a real, charter-owned gap, independently verified by direct execution

**The claim, checked at the source, not assumed:** `run.py:188–198`'s
`cell_metrics()` calls `ts.absorbed_power_established_ratio` →
`ts.mixed_length_scale_regime` → `ts.netd_disposition` and builds a
`thermo` dict containing `netd_classification=netd["classification"]` for
**every** `(config, θ)` cell this cycle computes — all 6 Rank-3 cells and
all 14 Rank-1 cells, 20 cells total (line 195 fires once per `cell_metrics`
call; `cell_metrics` is called once per config×angle in both Rank 3 and
Rank 1, `run.py:302` and `run.py:421`). `pair_metrics()`
(`run.py:208–229`) even pulls the C-config's own `netd_classification_c`
into its own returned dict (line 229) — the machinery to report it exists
and is exercised. **Then it is dropped.** `rank3_report` (`run.py:354–364`)
and `rank1_report` (`run.py:438–443`) — the two dicts that become
`results.json::rank3.per_theta`/`rank1.per_theta` — build their own field
lists explicitly and neither one includes `netd_classification` or
`dt_ss_full_K` anywhere. I grepped both `results.json` and
`run_output.txt` for `netd_classification`/`dt_ss_full_K`/`UNDETECTABLE`/
`MARGINAL`/`DETECTABLE`: **zero hits in either file.** The only NETD-related
content anywhere in this cycle's committed record is the generic
`netd_disclaimer` boilerplate string (Idealization 3's own wording),
present in `results.json` and correctly `print()`-ed to `run_output.txt`
line 131 per the mandatory-fix docket's own item 7 — but that string says
*what NETD is*, never *what this cycle's own NETD classification actually
came out to be*.

**Independently computed what the missing classification would have read,**
by executing `ts.netd_disposition` myself against this cycle's own
committed `p_abs_w` values and the same sourced constants `run.py` imports
from `experiments/087/091` (`IRR_CENTRAL_W_CM2=6.584362×10⁻⁶` W/cm²,
`L_GEOMETRIC_M_R3=2.34×10⁻⁶` m, `NETD_BAND_K=(0.020,0.050)` K):

| θ | `p_abs_w` (sigma-corrected) | `dt_ss_full_K` | NETD class | margin below `NETD_BAND_K` floor |
|---|---|---|---|---|
| 37.2° | 2.7965×10⁻¹² W | 4.594×10⁻⁵ K | UNDETECTABLE | 435× |
| 40.2° | 3.0663×10⁻¹² W | 5.038×10⁻⁵ K | UNDETECTABLE | 397× |
| 41.4° | 3.1520×10⁻¹² W | 5.178×10⁻⁵ K | UNDETECTABLE | 386× |

All three UNDETECTABLE, comfortably inside the 374×–442× margin band this
exact article and channel already established at exp-087 (Iteration 64) —
**no surprise, and no reason to suspect this cycle's own findings threaten
that verdict.** That is precisely why this matters as a *reporting* defect
rather than a substantive one: the classification is boring and confirms
the established picture, but "boring and confirms the established picture"
is a conclusion a reader has to independently re-derive from raw `p_abs_w`
values themselves right now, because the write-up never states it.

**This is not new to exp-092 — it is inherited, silently, from exp-091,
also unflagged there.** `experiments/091-.../run.py:390–420` computes and
stores `netd_classification`/`netd_disclaimer` in its own per-cell `thermo`
dict, but its own `pair_metrics()` (lines 429–457) does not propagate
either field into its own returned dict, and I confirmed by direct grep
that `netd_classification` appears **nowhere** in exp-091's own
`results.json` either — only the same generic disclaimer string. Two of
this program's own most recent T28 cycles (091, 092) have now silently
dropped the substantive NETD classification while faithfully carrying the
disclaimer that exists to qualify it — a pattern the established
disclaimer-erosion lineage (R6–R15's own "known, named, ignored" family)
was built to catch, but this is a genuinely *different* shape from every
prior instance in that lineage: those were about a caveat failing to
propagate alongside a number that DID get reported; this is about the
underlying number never being reported at all, while its caveat propagates
perfectly. **Not previously named anywhere in this program's record** (I
checked LOGBOOK's own R-rule text and every T28 Phase-5 review back through
exp-087 for "netd_classification"/"never reported"/"silently dropped" —
no hits), so this does not fire any Checkpoint criterion on its own
founding-instance naming here, matching this program's own R5/R6/.../R15
precedent that a rule's founding cycle establishes the standard rather than
retroactively violating it. **Named here as a forward tripwire**: a third
consecutive T28 cycle that computes but does not report a per-cell NETD
classification, after this review names the gap explicitly, should be read
against the same "known, named, ignored" standard R11's own text
established for `free_period_with_widening`'s silent-fallback defect.

**Fix, cheap, zero marginal FDTD cost for any future cycle reusing this
machinery**: add `netd_classification=c_cell["thermo"]["netd_classification"]`
(and the G-config's own, for completeness) to `pair_metrics()`'s returned
dict, thread it into `rank3_report`/`rank1_report`, and print at least the
worst-case (highest-margin-below-floor, or, if ever DETECTABLE/MARGINAL,
that cell specifically) in `run_output.txt` — the exact shape exp-087's own
NOTES.md ("P8: predicted UNDETECTABLE, confirmed at all 6 cells...
`dt_ss_full_K` ranges 4.52×10⁻⁵ to 5.35×10⁻⁵ K") already demonstrates is
cheap and readable.

## 3. The (R3b) magnitude: correctly classified, imprecisely explained

**Checking the task's own explicit question: does the ~4% decrease actually
match my own predicted directional lean quantitatively, or only
qualitatively?** My own prior-cycle band (`[0.3,3.0]` CONFIRM, directional
lean "a decrease... sub-linearly, not proportionally") was a **broad,
qualitative** falsifiability gate, not a point prediction — I pre-registered
no specific magnitude, and NOTES.md's own §Predictions record confirms this
(`(R3b)` states only the direction and cites the CONFIRM band, no numeric
target). NOTES.md's own §Result then writes: *"a clean, small, consistent
~3.8–4.0% decrease at every angle, matching THERMODYNAMICS' own
pre-registered directional lean... **almost exactly**."* Read charitably,
"almost exactly" describes the direction-plus-sublinearity match, which is
genuinely tight (a factor-of-~8 sub-linearity: 4% observed against a naive
weak-perturbation expectation of ~33% if `p_abs_w` scaled linearly with
`σ_max`). Read literally, "almost exactly" implies a magnitude was predicted
and landed close — **no such magnitude was ever pre-registered anywhere in
this cycle's own frozen `NOTES.md`.** This is a small, non-load-bearing
overclaim of precision (it does not change the CONFIRM verdict, which is
correctly scored against the actual pre-registered band), but it is exactly
the kind of "what was actually predicted vs. what is being credited"
imprecision this program's own R4/R9 lineage exists to keep out of the
permanent record — worth a one-clause correction, not a re-scoring.

**A sharper problem: the mechanism cited (T9's `ratio_abs_ext≈0.51`
"near-saturation" anchor) is not, on inspection, the most precise
already-established explanation this program's own record offers for *why*
`p_abs_w` should move so little.** `ratio_abs_ext≈0.51` is a statement about
the **partition** of extinguished power between absorption and scattering —
it says nothing, by itself, about how the **total extinguished power**
(`σ_ext`, hence `p_abs_w = I·(σ_ext·Δx)²·ratio_abs_ext` per
`thermo_sidecar.py`'s own formula) should respond to a change in the shell's
bulk conductivity. My own prior-cycle framing ("an already-substantially-
saturated absorber... moving sub-linearly") imported a Beer–Lambert-style
bulk-transmission-saturation picture (`1-e^{-τ}`→1 asymptotically) — but
this program's own ESTABLISHED section (LOGBOOK.md, "the extinction paradox,
measured (exp-002)") explicitly documents that `σ_abs/σ_ext=0.51` **exceeds**
the idealized geometric-optics/Beer–Lambert ceiling (`σ_abs/σ_ext≤0.5` for
any perfectly-black object) precisely *because* this bench sits in a
near-field regime where diffraction/shadow-formation, not bulk absorption
depth, sets the extinction cross-section — the textbook "extinction
paradox" (`σ_ext→2×` geometric cross-section for any sufficiently opaque
scatterer, nearly independent of exactly how absorptive its interior is).
That is a **different, more precise, and more falsifiable** mechanism than
"the absorption itself is saturated": it predicts `σ_ext` (not `p_abs_w`
directly) should be nearly insensitive to the 33% `σ_max` cut, with the
small residual `p_abs_w` movement coming almost entirely from `σ_ext`'s
own small residual movement (squared, since `p_abs_w∝σ_ext²` in this
convention), not from `ratio_abs_ext` moving materially.

**A back-of-envelope check, disclosed explicitly as assumption-dependent,
not independently confirmed this cycle:** if `ratio_abs_ext` at the
as-filed (`σ_max=0.5`) article is also close to the ~0.51 anchor (a
plausible but *untested* assumption — exp-091 never persisted its own
`ratio_abs_ext_raw`, see §4 below), then `p_abs_w∝width²` implies
`width_ratio ≈ √(p_abs_w_ratio)`: `√0.9610=0.9803`, `√0.9619=0.9808`,
`√0.9602=0.9799` — i.e. **`σ_ext` itself would have moved by only ~2.0%**
while `σ_max` moved by 33%, an even sharper insensitivity than the ~4%
`p_abs_w` figure alone conveys, and directionally exactly what the
extinction-paradox reading predicts (a size/diffraction-dominated `σ_ext`
should barely notice a bulk-conductivity change once the object is already
well past the opaque threshold). **This is offered as a testable hypothesis,
not a confirmed decomposition** — it rests on an assumption this cycle's
own data cannot verify (see the cheap follow-up in §4/§5). Neither reading
(mine here, or the write-up's "near-saturation") changes the CONFIRM
verdict or any scored number; the difference is which of this program's own
established mechanisms gets credited, and which one correctly predicts
where a future cycle should look if the effect size ever needs explaining
more precisely (e.g. at a different `σ_max` cut, or at witness scale).

## 4. What's missing to settle §3: `ratio_abs_ext_raw` at the as-filed (σ=0.5) article was never captured — by either cycle

Section 3's own decomposition cannot be verified from committed data because
**exp-091 never persisted `sigma_ext_cells`/`ratio_abs_ext_raw`** for its
own filed (`σ_max=0.5`) R3 leg — I grepped exp-091's entire `results.json`
for both fields and found zero hits, confirming this gap exists independent
of exp-092's own choices. Exp-092 correctly began persisting these fields
prospectively, for its own new (`σ_max=1/3`) data (`results.json::rank3.
per_theta.*.sigma_corrected_ratio_abs_ext_raw`) — a real, credit-worthy
completion of the Tier-4 "persist `sigma_ext_cells`/`ratio_abs_ext_raw`"
item both exp-090 and exp-091's own Phase-5 queues named — but it did not,
and was not asked to, retroactively backfill exp-091's own filed value. The
result: nobody in this program's record can currently state whether
`ratio_abs_ext` held flat, or shifted, between `σ_max=0.5` and `σ_max=1/3`
at these three angles — the single fact that would settle whether §3's
extinction-paradox reading or a partition-shift reading is the right one.

**This is cheap to close**: three additional article-leg-only FDTD calls
(`C40_R3` at 37.2°/40.2°/41.4°, `σ_max=0.5`, `cpl=30`, `STEPS=4200` — the
empty legs are already bit-exact-reproducible per this cycle's own verified
determinism, §Result of `NOTES.md`) would recover the missing
`ratio_abs_ext_raw(σ=0.5)` and let a future cycle decompose the observed
~4% `p_abs_w` swing into its `σ_ext`-saturation and `ratio_abs_ext`-shift
components directly, rather than by the assumption-gated estimate in §3.

## 5. The upper-window double-crossing: the energy channel shows no signature of the near-total interference null — a positive finding the write-up computes but does not connect

**Checking the task's own explicit question**: does `p_abs_w`/`frac_p_abs`
do anything unusual near 41.8°, where `delta_scene` reads its smallest
magnitude of the entire cycle (`−1.865×10⁻⁵`, an order of magnitude below
its neighbors) and the pipeline correctly flags `NODE-UNRESOLVABLE`?
Reading `results.json::rank1.per_theta` directly:

| θ | `frac_p_abs` | classification |
|---|---|---|
| 39.6° | 0.003634 | CONSISTENT |
| 39.8° | 0.006767 | CONSISTENT |
| 40.0° | 0.008330 | ENERGY-DOMINANT |
| **41.8°** | **0.006065** | **NODE-UNRESOLVABLE** |
| 42.0° | 0.002447 | NODE-UNRESOLVABLE |

`frac_p_abs(41.8°)` sits squarely inside the same order-of-magnitude range
as its floor-clearing neighbors (39.8°/40.0°), with no spike, dip, or
discontinuity coincident with `delta_scene`'s own near-total null at the
same angle. **This is exactly the outcome R14's own established mechanistic
story (Iterations 65–66: the `ratio_abs_ext(θ)` partition stays T9-flat, so
the numerator-side fractional swing is forced entirely into `σ_ext(θ)`'s
own config-differential term, never into `p_abs_w` behaving erratically)
predicts, now tested for the first time at the single most extreme point on
the `delta_scene(θ)` curve this program has ever measured** — a genuine
near-total coherent-interference null, not merely a near-crossing point.
The energy channel staying smooth exactly where the coherent-phase channel
goes through a near-singularity is a clean, falsifiable confirmation of
this program's own standing "these are two decoupled physical questions"
finding (T28's own established reading since exp-076's lossless-`PAD`
proof and R14's own founding cycle) — at its sharpest test yet. **NOTES.md's
own §Result reports the NODE-UNRESOLVABLE classification and the
double-crossing structure (Learned items 2–3) but never explicitly states
that the energy channel was checked at this point and found unremarkable**
— a genuinely positive, already-computed, zero-marginal-cost finding left
implicit rather than named. Non-load-bearing (it changes no verdict), but
it is exactly the kind of energy-channel corroboration this seat's own
charter exists to surface, and future citations of the double-crossing
finding should be able to say "and the energy channel confirms it is a
pure phase/interference feature" rather than requiring a fresh re-read of
raw JSON to find that out, as I had to here.

## 6. Everything else checked and found sound

- **Resequencing (Rank 3 before Rank 1) and the branch rule**: correctly
  implemented (`run.py`'s own `sigma_branch` logic, `results.json::
  sigma_branch.chosen_sigma_max=0.5`, matching the CONFIRM outcome) and
  correctly disclosed as licensing `sigma_max`, not the net's own
  placement (Idealization 11) — this Director-adjudicated, twice-converged
  (MATERIALS + QUANTUM) fix is exactly the R7/R8-lineage discipline this
  program has repeatedly had to re-learn; here it worked as designed.
- **Empty-leg re-run vs. reuse**: the Director's own §2 catch
  (`phase3_synthesis.md`) — that "reuse" was not actually implementable —
  is a genuine, load-bearing engineering catch (verified: `contrast_from_
  runs` needs the raw profile array, not the scalar `C_empty`), and the
  resulting bit-exact 6/6 empty-leg consistency check
  (`results.json::empty_leg_consistency_all_match=true`) is a clean,
  free validation of this bench's own determinism, correctly reported.
- **Rank 2's DROP/RELABEL table**: I did not re-derive this a sixth
  independent time (five-plus independent reproductions — EM's
  pre-verification, Red Team's Phase-2 audit, QUANTUM's critique, the
  Director twice, and the live `run.py` recomputation itself — already
  establish this as the best-verified single deliverable in this
  sub-thread's history); nothing in my own domain bears on its statistics,
  and I have no reason to doubt it.
- **`xi_ext`/non-negativity/vacuum-footprint gates**: all reported PASS in
  both `results.json` and `run_output.txt`, consistent with every value I
  independently touched.

## 7. Overall soundness verdict

**The cycle's own FDTD results are sound and correctly scored.** R3
CONFIRM, R3b CONFIRM, the sigma-branch decision, R1a's split
NEITHER-with-a-clean-lower-success/genuine-upper-complexity finding, and
R2's CONFIRM are all independently reproducible from committed primitives,
and my own Phase-2 flip condition was adopted, correctly scoped, and
correctly executed — a real, not cosmetic, methodological improvement.
Nothing in this review changes any of this cycle's own filed verdicts. Two
real gaps belong on the forward record: a charter-owned reporting defect
(computed-but-never-surfaced NETD classifications, now a two-cycle-old
silent pattern, named here for the first time) and an imprecise mechanistic
citation for the (R3b) magnitude (a defensible qualitative CONFIRM dressed
in language that overclaims predicted precision and reaches for the wrong
established mechanism). Neither is a Checkpoint-firing matter on its own
founding naming here, matching this program's own standing precedent.

## 8. Ranked top-3 candidate directions for Iteration 70

1. **Re-fit R15's own caution zone using the two newly-located `cpl=30`
   crossings (NOTES.md's own §Next item 1), and, in the same build, densely
   sample `p_abs_w`/`frac_p_abs` — not only `delta_scene` — through the
   upper-window double-crossing region (41.6°–42.2°, finer than the native
   0.2° step).** NOTES.md's own §Next item 2 already asks whether the
   double-crossing is a genuine two-node feature or an under-resolved
   single deep null; as filed it only proposes resolving `delta_scene`
   itself. Adding the energy channel to that same sweep, at zero
   additional angle-selection cost, would extend §5's own finding (the
   energy channel is smooth through the *known* null at 41.8°) to the
   *entire* fine structure of the double-crossing region — the sharpest,
   cheapest test available of whether R14's energy/phase-decoupling
   story holds at arbitrarily fine resolution near a genuine near-total
   interference null, not just at the two points this cycle happened to
   sample.
2. **Recover exp-091's own filed `ratio_abs_ext_raw` at `σ_max=0.5`** (3
   article-leg-only FDTD calls, `C40_R3` at 37.2°/40.2°/41.4°, `cpl=30`,
   `STEPS=4200` — §4 above) to settle whether the (R3b) ~4% `p_abs_w`
   swing decomposes into `σ_ext`-saturation (the extinction-paradox
   reading, §3) or a genuine `ratio_abs_ext` partition shift — currently
   an untested assumption either way, and the single cheapest FDTD-backed
   check that would upgrade §3 from a plausible alternative reading to a
   settled one.
3. **Fix the `netd_classification` silent-drop in `pair_metrics()`/
   `cell_metrics()`** (§2 above) before this shared machinery is reused a
   third time — thread the field through to `results.json` and print the
   worst-case cell in `run_output.txt`, matching exp-087's own
   already-demonstrated, cheap house convention. Zero marginal FDTD cost;
   closes a two-cycle-old gap directly inside this seat's own charter
   before a third silent recurrence makes it a named, ignored pattern
   rather than a freshly-caught one.

Also still open, unrelated to this cycle's own deliverable, carried from
`NOTES.md`'s own §Next and the standing T28 board: PHOTONICS' own
grazing-incidence validity check (still the single most-repeated item on
the whole T28 board); the x-wall wavelength-generality leg (well past
sixteen consecutive cycles deferred); the still-queued R14(b) formal
null-controlled period fit; the Rank-2-in-exp-090's-own-queue unbiased
margin-vs-distance rebuild on the full 31-point window; the ritualization
governance question (Iteration 61), still unresolved.
