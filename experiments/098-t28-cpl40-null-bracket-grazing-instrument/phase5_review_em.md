# Panel Iteration 75 — Phase 5 EM Self-Review (exp-098)

*ELECTROMAGNETISM seat, reviewing its own Phase-1/3 cycle. Blind to other
seats' Phase-5 reviews. Adversarial self-audit, not a rubber stamp.*

## 1. Independent spot-verification (numbers recomputed by hand, not trusted from prose)

1. **Total call count (64).** Summed `results.json::item_i.{A,B,C}.n_calls`
   (16+16+16=48) + `item_ii.n_calls` (16) = **64**, matching
   `results.json::fdtd_calls` and `NOTES.md`'s corrected figure. Matches.

2. **Null A crossing (36.770358°).** Recomputed `find_sign_change`'s linear
   interpolation by hand from the two bracketing angles/deltas
   (θ=36.627246°, Δ=−6.087977e-4; θ=36.960546°, Δ=+8.090604e-4):
   `frac = |Δ1|/(|Δ1|+|Δ2|) ≈ 0.42936`, `crossing ≈ 36.627246 + 0.42936×0.333300
   ≈ 36.77034°`. Matches `results.json`'s stored `36.77035821175119` to my
   hand-precision. **Matches.**

3. **Item (ii) crossing (38.252279°).** Same recomputation from the
   38.19°/38.29° bracket (Δ=+4.090528e-4 / −2.477514e-4): `frac≈0.62285`,
   `crossing ≈ 38.19 + 0.062285×... ≈ 38.25228°`. Matches stored
   `38.25227925382004`. **Matches.**

4. **GP2′ peak (235.4× at θ=66.0°).** Recomputed `1.3204688843098367 /
   0.00560956097833041 ≈ 235.396`, matching `ratio_to_ref` stored at
   θ=66.0° exactly, and confirmed by scanning the full 120-point
   `gp2_curve` that no other point exceeds it (nearest neighbors 65.5°/
   66.5° are lower). **Matches** — the "I caught myself drafting 89.5° and
   corrected it" claim in Result is itself verifiable and correct.

5. **Cross-consistency between GP1 and GP2′ (not asked for, found while
   checking #4).** `gp1_min_C = −0.44054321860532486`. The *only*
   `gp2_curve` entry whose `abs_C` matches that magnitude is θ=74.5°
   (`abs_C=0.44054321860532486`). This independently confirms NOTES.md's
   claim that GP1 and GP2′ read "the same `C(θ)` values... viewed a second
   way" — they are not two independently-computed quantities that happen
   to agree, they are the literal same array. **Matches**, and is a useful
   internal-consistency check nobody explicitly asked for in Predictions.

6. **R13 floor gate.** `floor/rms = 0.00019174375118374476 /
   0.0019174375118374476 = 0.1` exactly, consistent with the documented
   `FLOOR_FRAC=0.10` convention. **Matches.**

No load-bearing number I checked was wrong. The arithmetic in `run.py` and
`results.json` is sound wherever I probed it.

## 2. Steel-man and sharpest finding

**Steel-man of this cycle's own work first, honestly:** the redesign of
GP2 into GP2′ is real, not cosmetic — Red Team's Attacks 1–2 correctly
diagnosed a deterministic non-test, and the replacement genuinely reuses
`_src_amp(θ,...)`'s actual θ-dependence rather than the θ-invariant
`gd["r"]`. It found something (a MARGINAL band from 50.5°–89.5° peaking at
66.0°, 235.4×) that overlaps the independently-sourced exp-086 blow-up
band and lands its peak *inside* that band, not merely near its edge. The
netd_row() assert is genuinely enforced in two independent places (per-row
inside `run_r4_batch`, and again at aggregation in `main()`), both firing
strictly before `json.dump`. That is real, disciplined work.

**Sharpest finding — GP1's "hard passivity floor" framing overstates what
the check actually establishes, and this is squarely my own charter's
gap.** `GP1` is `weber(bo, bf) = (bo−bf)/bf ≥ −1` where `bo,bf` are
`window_means()` of `Sx = −Re(E·H*)` over an "object" window and a "flank"
window (`lab/ambient.py::window_means`/`weber`) — **the identical
Weber-contrast machinery used everywhere else in this program for
ambient-scene silhouette contrast**, here applied to a Poynting-vector
component instead of an intensity. Two things follow that NOTES.md's
"hard passivity floor for this lossless, source-driven field
superposition (no gain anywhere)" language does not surface:

- When `weber()` is applied to a manifestly non-negative quantity
  (intensity, as everywhere else in this program), `C≥−1` is a **trivial
  identity** — it can never be violated, because `b_obj≥0` always. The
  check only has teeth here because `Sx` (unlike intensity) is *signed*,
  so `bo<0` is arithmetically possible. That's a legitimate reason to run
  it — but it means GP1 is not a rediscovered EM law, it's the same
  metric formula pointed at a variable that happens to make its floor
  non-vacuous for once.
- More importantly: **local windowed non-negativity of one Cartesian
  component of the time-averaged Poynting vector is not what passivity/
  energy conservation actually requires.** Passivity theorems bound *net*
  power through a closed surface (or total radiated power vs. source
  power); they say nothing about a spatial sub-window's averaged flux
  component in an interference/diffraction pattern, where local backflow
  (negative `Sx` in a bounded region) is a completely ordinary, physical
  consequence of coherent superposition near an edge or shadow boundary —
  not evidence of gain. A `bo<0` reading below the `−1` floor would be a
  real numerical anomaly worth flagging, but calling the check itself a
  "hard passivity floor" claims a field-theoretic guarantee (Poynting's
  theorem applied to *this* windowed quantity) that was never actually
  derived — it was asserted by analogy to the ratio's algebra. This is
  exactly the kind of reciprocity/passivity bookkeeping subtlety my
  charter exists to catch, and Phase 1/3 (my own text) did not catch it
  under deadline pressure. It doesn't invalidate the PASS result (`min
  C=−0.44`, nowhere near the floor either way), but the write-up's
  physics claim is stronger than its derivation supports.

  A related, smaller point: **GP3's own name is a slight misnomer**, which
  the cycle's own text already substantially defuses (Idealization/GP3
  note) but is worth restating precisely under this charter: `y_src==
  y_obs` is a code-construction fact, not a reciprocity test — Lorentz
  reciprocity would require an independently-built swapped-role
  observation to compare against, which never existed in this geometry.
  NOTES.md already says this correctly ("there was never a second,
  independently-defined observer-side obliquity") — my only addition is
  that "GP3 (reciprocity, code-read + assertion)" as a *label* invites a
  future citation to read more into it than a tautology check supports;
  a future NOTES.md citing "reciprocity: CONFIRMED" without re-reading the
  caveat is a foreseeable misreading this program's own R-rule discipline
  (R4/T10) would want flagged now, not later.

**Secondary finding — GP2′'s reference band is not as clean as
"comfortably inside the model's own narrow-window fit range" suggests.**
Reading the `gp2_curve` entries actually inside `[30°,50°]`: `abs_C` spans
from 7.15e-6 (θ=38.5°, near a null) up to 0.04426 (θ=48.5°) — roughly
6,200× internal spread — and the four points immediately preceding the
reference band's right edge (θ=47.5°–49.5°) already sit at 3.8×–7.9× the
band's own median, i.e. within a factor of ~1.3 of the 10× MARGINAL
threshold, *inside* the band being used to define "clean." The first
MARGINAL point (θ=50.5°, ratio=10.41×) is barely across that line. This
doesn't overturn the finding (the flagged band from 50.5°–89.5° is broad,
monotonic-ish in its ramp, and the 66.0° peak is two orders of magnitude
above the reference band's own worst excursion, so the qualitative
conclusion is robust) — but the precise *location* of the VALID/MARGINAL
boundary at "50.5°, not 50.0° or 51.0°" is only weakly resolved against
the reference band's own oscillatory noise floor, on a 0.5°-step grid
whose phase relative to the underlying interference fringes was not
varied. Idealization 51 discloses the thresholds as new and
uncross-validated; it does not disclose that the reference band's own
internal variability already approaches the lower threshold near its
edge. Worth a sentence in a future cycle, not a blocking defect this one.

**Tertiary, ironic finding.** NOTES.md's own Result section states the
netd_row() assert "held for all 64 real-FDTD report rows (item (i) 48 +
item (ii) 16...)". 48 and 16 are **call counts** (matching `n_calls`),
not row counts — the actual number of angle-level dicts carrying the
10-key sidecar is 18 (12 from item i + 6 from item ii, of which only 16
total angle-points are call-backed this cycle and 2 are reused). The
underlying code enforces coverage correctly (verified in §3 below); this
is a units conflation in prose only. It's mentioned here because it is
the same *class* of error (a parameter-table/count arithmetic slip) that
the cycle's own Learned §1 just spent a paragraph diagnosing as this
program's demonstrated blind spot — recurring, at smaller scale, in the
very paragraph asserting the fix for a different mandatory item. Neither
seat, including this one now, is assigned to catch this class of error;
Learned/Next item 4 (assign call-count arithmetic verification) is
under-scoped if it only covers the top-level call-count and not any
count embedded in supporting prose.

## 3. Verification of Red Team mandatory fix #2 (netd_row() build-time assert)

Read `run.py` end-to-end. The assert is implemented in **two** places,
not one:

- Inside `run_r4_batch()` (called by both item (i) and item (ii)), the
  assert fires **per angle**, immediately after building `row` and before
  it is returned into the caller's `report` dict — i.e., before that
  data ever reaches `main()`'s aggregation step.
- Again in `main()`, over the aggregated `all_netd_rows` list, immediately
  before `total_wall`/`results.json` are computed/written.
- The two *reused* rows (38.49°/38.69°, exp-095's own data) are checked
  at **module import time** (`for th_str, row in RANK1C_FILED.items():
  assert NETD_ROW_KEYS <= set(row.keys())`, lines ~119–120) — earlier than
  any of the above, and unconditionally on import.

`main()` is a single straight-line function with no `try/except` around
the write and no early-return branch between any of these asserts and
`json.dump`. **I could not find a code path that reaches `results.json`
without passing through at least one, and in practice all three, of these
checks.** Red Team's mandatory fix #2 is implemented as specified, with
redundancy beyond what was strictly required (defense-in-depth: deleting
the `main()`-level aggregate assert in a future edit would not silently
reopen the gap, because the per-row assert inside `run_r4_batch` would
still fire first). I consider this fix **fully and robustly discharged**.

## 4. T1 escape-route mapping, revisited with real data

Phase 1 §3 (`phase1_proposal.md`) said only that "a validity boundary θ*
found in (v) bounds every future claim this line makes near grazing
incidence" — a placeholder, no number. With real data:

- The committed angular-selectivity window this program actually argues
  from (36°–42°) sits **entirely inside GP2′'s VALID region** — every
  `gp2_curve` point in that span (36.0°→1.85×, 40.0°→0.83×, 42.0°→0.46×,
  etc.) reads VALID. This cycle's finding does **not** retroactively put
  any existing `delta_scene` claim in the 36°–42° window at risk.
- The concrete new fact for the T1 mapping is: **the closed-form model's
  own self-diagnosed departure from "clean" now has a number, θ*≈50.5°**
  — more conservative than the previously-known exp-086 blow-up band
  (θc≈59°–73°). Any future proposal on this escape route that wants to
  extend evidence toward larger incidence angles (e.g., to claim a wider
  angular-selectivity band, or to push contrast measurements past ~45°–
  50°) now inherits an explicit, quantified line it must either stay
  clear of or address with a corrected (UTD/shadow-boundary) model before
  citing this instrument's machinery in support.
- This should be stated as an update to §3, not left implicit in §Result:
  the escape route's *current* evidentiary base is unaffected, but its
  *future* extensibility toward grazing incidence is now bounded by a
  specific number for the first time in 11 cycles of deferral, and that
  number belongs in any future Phase-1 proposal that cites this line.

## 5. Verdict

**CONCUR-WITH-GAPS.**

The 64-call spend, the crossing-finding arithmetic, the netd_row()
enforcement, and the GP2′ redesign's mechanics all check out under
independent recomputation — no numerical or logical defect that would
change item (i)/(ii)/(iii)/(iv)'s verdicts. The gaps are all in
*characterization*, squarely inside this seat's own charter, and none
are load-bearing to the frozen Result: (a) GP1's "hard passivity floor"
framing claims more field-theoretic backing than its construction
(a Weber-contrast formula borrowed from the scene-contrast toolkit,
applied to a signed Poynting component) actually supports; (b) GP2′'s
reference band is internally noisier near its own edge than "comfortably
inside the fit range" implies, so the exact 50.5° boundary is
weakly-resolved even though the qualitative flagged-band finding is
robust; (c) a prose units-conflation ("64 report rows" vs. 64 calls) in
the very paragraph documenting the netd_row() fix, of the same species as
this cycle's own headlined arithmetic blind spot. None of these should
reopen Phase 4; all three are one-sentence fixes for whoever drafts the
next cycle citing this one, and (a) in particular should be corrected in
language the next proposal that cites GP1 will actually read.

## 6. My own ranked top-3 candidate next directions

1. **Reframe GP1 in the next T28 cycle that touches it** (even a
   documentation-only patch, zero FDTD): replace "hard passivity floor"
   with an accurate description — "non-negativity check on a windowed
   Poynting-flux component, motivated by the absence of any gain
   mechanism in this source-driven construction, not a direct corollary
   of Poynting's theorem applied to this specific window." Cheap, closes
   a real charter-owned gap before a future cycle cites GP1 as a settled
   physical law.
2. **Null C re-test at a wider/asymmetric bracket** (NOTES.md's own Next
   item 1) — this is the most consequential open physics question left
   standing: item (ii) just proved a same-sized bracket can miss a real
   crossing when mis-centered, and Null C's NO-SIGN-CHANGE verdict rests
   on exactly the bracket geometry that failure mode targets. Directly
   load-bearing to the family-verdict (MIXED vs. a fourth reproducing
   null).
3. **The cpl=50/R5 third resolution point** (NOTES.md's own Next item 2)
   at Null B and/or θ₀≈38.590230° — the Richardson-style diagnostic's own
   surprising >2nd-order-looking growth (1.78× observed vs. 0.5625×
   naive) is the most scientifically interesting loose thread this cycle
   produced, and a third resolution point is the only way to tell
   migration from non-monotonic discretization apart, per MATERIALS'
   own already-adopted finding.
