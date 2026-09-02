# Phase-5 Review — QUANTUM OPTICS seat, Panel Iteration 78 (exp-101)

Fresh sub-agent, no memory of any other cycle beyond this packet. I am the
same seat that filed `phase2_critique_quantum.md` on this cycle's own
Phase-1 proposal (the C40_R4 `BOX_B`/`BOX_CROSS` under-margin attack) — this
pass checks whether my own mandatory fix actually landed correctly in the
executed run, using real numbers, not pre-registered gates. Every figure
below was recomputed this session directly from `run.py`, `results.json`,
and `run_output.txt` (and, where cited, from `lab/fdtd2d.py`/`lab/
qext_theory.py`/`LOGBOOK.md` source) — nothing is taken on NOTES.md's word.

## Verdict

**The Tier-0 deliverable executed correctly and Fix 4 (my own mandatory
fix) discharged as designed — box margins are real, code-enforced, and
verified ≥90 cells from the raw JSON.** Predictions 1, 2, and 4 are
honestly scored. Prediction 3's falsification is correctly reported as a
falsification, not laundered into a pass. **But NOTES.md's own physical
explanation for Prediction 3 — "extinction efficiency approaches
`Q_ext→2`" — is quantitatively wrong, using a number this bench's own
already-locked machinery (`lab/qext_theory.py`, exp-059, LOGBOOK's T-thread)
already contradicts, and the discrepancy is fully explained by a real,
previously-uncaught R9-commensurability defect this cycle's own Prediction
3 introduces:** `sigma_scat_downstream` (and every other *absolute*
`sc.widths()` output — `sigma_scat`, `sigma_abs`, `sigma_ext`,
`sigma_ext_cross`) is silently inflated by `1/cos(θ)` at these oblique
angles, because `i_inc` measures only the x-projected component of the
incident Poynting flux, not its true magnitude, for a wave launched along
`(−cosθ, +sinθ)` (documented, verbatim, in `lab/fdtd2d.py::
add_line_source`). Predictions 1 and 2 are RATIOS of two such quantities
and cancel this factor exactly, which is exactly why they reproduce T9's
long-established, angle-robust anchor — but Prediction 3 divides one such
absolute, `i_inc`-inflated quantity by a fixed geometric constant
(`2·R4_R_OUT=312`), which does NOT cancel it. Nobody — five Phase-2
critiques (mine included), the Red Team audit, or NOTES.md's own Phase-3/
Result sections — checked this. It does not reverse Prediction 3's
falsification verdict (see below), but it does mean the specific physical
number NOTES cites in its defense is not supported by data already on this
bench, and a materially better, verifiable explanation was sitting
one arithmetic step away in this cycle's own `results.json`.

---

## (a) Box-margin verification — real numbers, not NOTES.md's restatement

`run.py::_verify_box_margins()` (lines 123–145) is a real, executed,
pre-registered gate: it recomputes `box_a`/`box_cross` from
`box_for_r4(cfg, clearance)` for both configs, asserts `margin_a >= 60`,
`margin_cross >= 90` (both left and right faces), and is called at module
load time (`BOX_MARGIN_REPORT = _verify_box_margins()`, line 148) —
**before** `main()`/`run_leg_b_fixed()` runs a single `sim.run()`. This is
correctly a HALT-before-FDTD gate, not a post-hoc reassurance, discharging
the letter of my own Phase-2 demand.

Read directly from the raw `results.json["box_margin_report"]` (not
NOTES.md's prose table):

| key | box_a | box_cross | margin_a_left | margin_cross_left | margin_cross_right |
|---|---|---|---|---|---|
| C40_R4 | (160,520,1404,1764) | (170,510,1414,1754) | 80 | **90** | 130 |
| G40_R4 | (240,600,1484,1844) | (216,624,1460,1868) | 160 | 136 | 176 |

Independently re-derived from raw constants (`R4_R_OUT=156`,
`BOX_CROSS_CLEARANCE={"C40_R4":14,"G40_R4":48}`, `R4_BASE_OBJ_X=340`,
`R4_BASE_ABSORB=80`, both confirmed this session directly in
`experiments/069-.../design_geometry.py`): `r_cross(C40)=156+14=170`,
`x0=340-170=170`, `margin=170-80=90` — matches to the cell. **Confirmed: `≥90`
holds, exactly as designed.**

One residual note, not a defect: the achieved margin is **exactly 90**,
the bare floor of the assert, not comfortably inside a `[90,100]` buffer —
`BOX_CROSS_CLEARANCE["C40_R4"]=14` was reverse-engineered to hit the number,
not to clear it with headroom. Red Team's own attack #5 already flagged
that no R4-specific empirical margin-vs-`box_dev` curve exists on file to
say whether 90 is truly enough or merely a round number restated from my
own critique's lower bound. Part (b) below is the closest this cycle comes
to actually testing that empirically, and — read correctly — it does not
show signs of a margin-driven artifact at 90 cells.

---

## (b) Does C40_R4's `box_dev_scat_downstream` actually run higher/noisier?

**No — it runs systematically LOWER than G40_R4's, at every one of the 6
angles, by a consistent factor.** Raw values (`results.json`, both configs,
all resolved):

| θ (deg) | box_dev C40_R4 | box_dev G40_R4 | ratio G40/C40 |
|---|---|---|---|
| 37.127 | 0.0181 | 0.0454 | 2.51 |
| 38.590 | 0.0150 | 0.0400 | 2.67 |
| 39.200 | 0.0142 | 0.0399 | 2.81 |
| 40.265 | 0.0122 | 0.0348 | 2.85 |
| 41.461 | 0.0095 | 0.0299 | 3.15 |
| 42.961 | 0.0057 | 0.0169 | 2.96 |

This is the literal opposite of "higher/noisier." **But this is not
evidence my Phase-2 concern was wrong — read correctly, it is consistent
with it, for a subtler reason nobody in this packet worked out.** The two
configs' box-size deltas (relative to `BOX_A`, r=180) are `C40_R4`:
`|170−180|/180 = 5.6%` and `G40_R4`: `|204−180|/180 = 13.3%` — a ratio of
**2.4×**. The observed `box_dev` ratio (2.5×–3.15×, mean ≈2.8×) tracks that
2.4× size-delta ratio closely across all 6 angles. That is exactly the
signature of `box_dev` behaving as a **first-order (linear) sensitivity of
`sigma_scat_downstream` to box radius**, scaled by how far apart the two
probed radii are — not as an intrinsic, radius-independent property of the
quantity's "true" box-independence. A smaller `Δr` mechanically produces a
smaller measured deviation almost regardless of whether the underlying
field is well-behaved at that radius, because the check is a weaker
stress test by construction, exactly as my own critique said in the
abstract. **NOTES.md's Result section reads C40_R4's low `box_dev` as
"the derived quantity is genuinely box-independent... despite the
asymmetric independence-check power" — this framing treats a value that
is mechanically expected to be small (given the shorter lever arm) as
independent confirmation of robustness.** It is not: a box-independence
check whose own power scales with the size of the perturbation it applies
cannot, by the same measurement, also certify that a *larger* perturbation
would have passed. Practically: this does not overturn Prediction 4 (both
configs cleared 0.12 by a wide, genuine margin — 2.6×–21×), but the
specific interpretive sentence in NOTES.md overclaims what the C40_R4 side
of that check actually establishes. A cycle that wants an apples-to-apples
box-independence comparison across configs should equalize the *relative*
size delta, not just the absolute margin-from-absorb-boundary threshold.

(Cross-check: `box_dev`'s numerator and denominator, `scat_downstream_a`
and `scat_downstream_cross`, are built from the same single `(key,θ)`
capture pair and share the same `i_inc` — so `box_dev` is a ratio and is
**immune** to the oblique-incidence artifact in part (c) below. These two
findings are independent of each other.)

---

## (c) Prediction 3's falsification and the extinction-paradox explanation

### The specific sanity check asked for: does `sigma_scat` sit close to `sigma_abs`?

Yes. From `results.json`, across all 12 cells: `sigma_scat` ∈
[294.01, 320.30], `sigma_abs` ∈ [310.18, 338.79]; the ratio `sigma_scat/
sigma_abs` is tightly clustered at **0.945–0.951** in every single cell
(e.g. θ=37.127 C40: 294.01/310.93=0.9456; θ=42.961 C40: 320.30/338.79=
0.9454). This is exactly what the extinction-paradox claim (`Q_scat≈Q_abs`,
both ≈half of `Q_ext`) predicts, and it is confirmed directly, not
asserted. **But it is not new evidence** — it is algebraically identical
to Prediction 1's own confirmed ratio (`sigma_abs/sigma_ext∈[0.5129,
0.5145]` ⟺ `sigma_scat/sigma_ext∈[0.4855,0.4871]` ⟺ `sigma_scat/sigma_abs
≈0.945–0.949` by construction, since `sigma_ext=sigma_scat+sigma_abs`).
Citing this as support for Prediction 3's explanation restates an already-
confirmed fact from a different prediction in the same NOTES.md; it is
correct, but it is not independent corroboration.

### The deeper, unflagged problem: the absolute `Q_ext` numbers are inflated

`lab/sections.py`'s own docstring defines the ranking metric as `Q = width
/ (2 · outer radius)`, and `lab/qext_theory.py` (exp-059, LOCKED, trust-
suite stage 21) documents the bench's own already-established value for
this exact article class at normal incidence: **`Q_ext_measured=
1.5385088077964393`**, exactly matching `experiments/002-cross-sections/
results.json::absorber-600.q_ext`, sitting at 72.6% of the theoretical
large-x PEC ceiling (2.1177) — explicitly **not** "approaching 2."

Computing that same ratio (`sigma_ext/(2·R4_R_OUT)=sigma_ext/312`) from
THIS cycle's own `results.json` gives, across the 6 angles (both configs):
**1.936 – 2.113** — i.e. running close to, and at the high end (θ=42.96°)
essentially AT, the theoretical PEC ceiling, nowhere near the bench's own
established 1.5385 for the identical article class. That is a ~26–37%
discrepancy against the bench's own locked anchor, and it grows
monotonically with θ (1.94 at 37.13° → 2.11 at 42.96°) — a real,
9%-across-the-sweep trend, not noise.

The explanation is in `lab/fdtd2d.py::add_line_source`'s own docstring,
verified this session: an oblique source launches a wave that "travels
along `(−cosθ, +sinθ)`." `sc.widths()`'s `i_inc` (and `_face_flux`'s `sx()`
generally) measures only the **x-component** of the Poynting flux density
— at oblique incidence this equals `cos(θ)` times the wave's true
magnitude, not the magnitude itself. Every `sc.widths()` output normalized
by `i_inc` therefore reads a factor `1/cos(θ)` too large at oblique
incidence — **unless** the quantity is itself a ratio of two `i_inc`-
normalized numbers from the same capture, in which case the shared factor
cancels exactly. `sigma_abs/sigma_ext` (Prediction 1) and `back_frac`/
`fwd_frac` (Prediction 2) are such ratios and are correctly immune — which
is exactly why exp-087's own oblique reconfirmation of the T9 anchor
(0.5128–0.5138) held despite oblique incidence, a bench precedent that
(retroactively) supports this finding rather than contradicting it.
`sigma_scat_downstream/(2·R4_R_OUT)` (Prediction 3) is **not** such a
ratio — it divides one `i_inc`-inflated absolute quantity by a fixed
geometric constant — so it is exposed.

Confirming this is the actual mechanism, not a coincidence: multiplying
this cycle's own raw `Q_raw=sigma_ext/312` by `cos(θ)` at each of the 12
cells:

| θ (deg) | Q_raw (C40) | Q_raw·cos θ (C40) | Q_raw (G40) | Q_raw·cos θ (G40) |
|---|---|---|---|---|
| 37.127 | 1.939 | 1.546 | 1.936 | 1.543 |
| 38.590 | 1.983 | 1.550 | 1.991 | 1.556 |
| 39.200 | 1.999 | 1.549 | 2.003 | 1.552 |
| 40.265 | 2.035 | 1.553 | 2.028 | 1.547 |
| 41.461 | 2.063 | 1.546 | 2.073 | 1.554 |
| 42.961 | 2.113 | 1.546 | 2.104 | 1.539 |

All 12 corrected values land in **1.539–1.556** — a spread of ~1%, dead
center on the bench's own independently-derived (closed-form Bessel/Hankel
series, a completely different method) locked anchor of 1.5385. This is a
12-point, two-config, 5.8°-wide-sweep confirmation, far too precise to be
coincidental — the oblique launch geometry is the correct, and now
verified, explanation for the entire apparent 9% "θ-dependent growth" in
the raw `Q_ext` numbers this cycle produced, and that growth is instrument
artifact, not a real angle-dependent extinction efficiency.

### Does this change Prediction 3's verdict?

**No.** Applying the same `cos(θ)` correction to `sigma_scat_downstream`
itself (it shares the identical `i_inc` inflation) gives a corrected
range of roughly **0.40–0.50** (e.g. θ=37.13° C40: 0.6159×cos(37.13°)=
0.490; θ=42.96° C40: 0.5457×cos(42.96°)=0.400) — still **2.7×–3.3× over**
the predicted 0.15 ceiling. Prediction 3 is genuinely falsified either
way; nothing here rescues it, and NOTES.md is right not to try.

### What this does change

NOTES.md's stated *mechanism* for the falsification — "an optically large
absorbing disk's extinction efficiency approaches `Q_ext→2`... because it
must radiate a forward-diffracted wave of cross-section comparable to its
own geometric width" — cites, without saying so, the cycle's own raw,
uncorrected `~2` numbers as if they reflected the article's true
extinction efficiency approaching the geometric-optics ceiling. The
bench's own already-locked figure for this identical article class is
1.5385, not "approaching 2," and the reason this cycle's own numbers
*look* closer to 2 is a `cos(θ)`-artifact in `i_inc`, not a real
optical effect. The qualitative direction of the argument (large,
comparably-sized forward-scattering cross section as the necessary
companion of a real shadow) is correct and the falsification stands, but
the specific magnitude invoked overclaims — ironically, the *correctly
normalized* number is a cleaner, more precise confirmation of internal
consistency (it reproduces a completely independently-derived anchor to
~1%) than what NOTES.md actually wrote, which nobody checked against the
one number on this bench best suited to check it against.

---

## Defect no other document in this packet caught

**An R9 (commensurability) violation in Prediction 3's own construction**:
`sigma_scat_downstream/(2·R4_R_OUT)` divides an `i_inc`-normalized absolute
quantity — inflated by `1/cos(θ)` at oblique incidence, a documented
property of this bench's own oblique-source geometry — by a purely
geometric constant that carries no such inflation. This is exactly the
class of defect R9 exists to catch ("verifying a cited ratio's arithmetic
is not enough — the operands' commensurability... must be independently
confirmed"), and it slipped past five Phase-2 critiques (including my
own), a full Red Team audit, and NOTES.md's own Phase-3/Result sections —
because Prediction 3 is this bench's first-ever use of an *absolute*
`sc.widths()` output (rather than a ratio of two such outputs) compared
against a fixed geometric denominator, at oblique incidence. Every prior
use of `sc.widths()`'s outputs on this bench (T9's anchor, exp-087's
oblique reconfirmation, this cycle's own Predictions 1/2/4) was either a
ratio of two `i_inc`-normalized quantities (cancels) or `box_dev`-style
(also cancels, part (b) above) — so the artifact had no prior surface to
appear on. It does not overturn this cycle's own falsification verdict,
but it does mean the explanation offered for that verdict cites an
inflated number without disclosing why, when the bench's own on-file data
(the qext_theory.py anchor) was one arithmetic step away from resolving it
cleanly.

## Ranked candidate directions (this seat's contribution to the top-3)

1. **Fix `i_inc` for oblique incidence, or explicitly flag every absolute
   (non-ratio) `sc.widths()` output as angle-inflated by `1/cos(θ)`** —
   either correct `i_inc` to measure the true wave magnitude (project onto
   `(−cosθ,+sinθ)`, not just the x-component) or add a code comment/gate at
   the point any FUTURE absolute (not ratio) derived quantity is compared
   against a fixed geometric bound, so this exact defect cannot recur when
   Tier 2's coherent point-intensity instrument (NOTES.md's own top "Next"
   item) is eventually built — that instrument will need a correctly
   normalized incident reference far more than this cycle's box ledger did.
2. **Re-run the `box_dev_scat_downstream` cross-check with a common
   relative `Δr` for both configs** (not a common absolute clearance) —
   part (b) shows the current C40_R4/G40_R4 asymmetry (5.6% vs 13.3%) is
   not merely "weaker," it produces a `box_dev` ratio that tracks the
   `Δr` ratio almost linearly, meaning the current pass is not informative
   about whether C40_R4 would still pass a properly matched stress test.
3. Endorsing NOTES.md's own top queued item (a coherent, phase-resolved
   downstream point-intensity instrument) — unaffected by either finding
   above, and the correct next step for constraint 1 regardless.

## Standing house-rule note

**R9 — flag for future citation, not this cycle's Checkpoint.** No
Checkpoint criterion fires from this review: Prediction 3's falsification
is honestly reported, the mechanism offered is directionally correct even
though its magnitude overclaims, and no constraint (1–4) is touched. But
any future cycle citing this cycle's `Q_ext≈2`/"approaches the geometric-
optics ceiling" language, or reusing `sigma_scat_downstream`-style absolute
metrics at oblique incidence without the `cos(θ)` correction, would be
propagating this defect forward — R20's "restated, not recomputed" pattern
would then apply.
