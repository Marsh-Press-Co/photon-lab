# PHASE 5 — PHOTONICS REVIEW · Panel Iteration 75 · exp-098

*Blind, fresh context. Charter: surface interaction, absorption spectra,
angular dependence, scattering cross-sections — is the proposal's optical
response coherent as stated, across wavelength and angle? I am the seat
that established the θc≈59°–73°, 5,444×–6,631× exp-086 finding this cycle's
item (v) claims to corroborate.*

## Verdict: **CONCUR-WITH-GAP(S)**

The underlying physics/numerics are sound and every load-bearing number I
independently recomputed matches `results.json` exactly. But the Result
section's characterization of GP2′'s own output overclaims uniformity in a
checkable, falsifiable way, and the cycle stops short of examining a
genuine angular-shape divergence between GP2′ and my own exp-086 measure in
the true-grazing tail (74°–89.5°) — territory GP2′ newly covers that
exp-086 never swept. Neither gap changes item (v)'s bottom-line verdict
(a real, non-vacuous, corroborating instrument), but both are real,
independently-findable defects a photonics reading should not let pass
silently.

## 1. Independent spot-verification (recomputed directly from `results.json`, not read from prose)

**(a) Sign-crossing recomputation, items (i)/(ii) — MATCHES.** I re-ran
`find_sign_change`'s own linear-interpolation formula by hand on the raw
`delta_scene` values in `results.json`:

- Null A: `da=-6.088e-4` at 36.627246°, `db=+8.091e-4` at 36.960546°.
  `frac=0.4293` → crossing = 36.7704°. Filed: **36.770358°**. Match.
- Null B: `da=-8.450e-4` at 39.765420°, `db=+9.592e-4` at 40.098720°.
  `frac=0.4684` → crossing = 39.9215°. Filed: **39.921519°**. Match.
- Item (ii): `da=+4.091e-4` at 38.19°, `db=-2.478e-4` at 38.29°.
  `frac=0.6228` → crossing = 38.2523°. Filed: **38.252279°**. Match.
- Richardson diagnostic (Null B): `shift_20_40 = 39.921519316666235 −
  40.26541960305772 = −0.343900286…`, filed **−0.34390028639148795**
  (match); `observed_ratio = −0.3439/−0.19358 = 1.77652`, filed
  **1.7765163757372424** (match); `naive_order2_ratio = (1/40÷1/20)² /
  (1/30÷1/20)² = 0.25/0.4444 = 0.5625`, filed **0.5625** (match).

All four load-bearing crossing/ratio figures reproduce bit-for-bit from
the raw per-angle data. No arithmetic defect in item (i)/(ii)/Richardson.

**(b) GP1/GP2′ headline numbers — MATCH.** `gp1_min_C = −0.44054321860532486`
is exactly the (negated) `abs_C` value stored at θ=74.5° in `gp2_curve`
(`0.44054321860532486`) — internally consistent, confirms GP1's own
reported minimum is not a typo or stale figure. GP2′'s claimed peak,
**235.4× at θ=66.0°**, is confirmed as the actual maximum of the full
120-point `ratio_to_ref` array (I scanned the neighborhood 63.0°–73.5°:
47.5, 69.2, 99.9, 138.9, 181.8, 218.5, **235.4 (66.0°)**, 224.0, 188.4,
141.5, 94.7, 54.1, 21.1, 24.6, 39.9, 51.6, 60.4, 66.9, 71.7, 75.0, 77.2 —
66.0° is genuinely the global max, not cherry-picked, and NOTES.md's own
disclosed self-correction — catching a draft claim of "peaking near
89.5°" before freezing — is itself borne out: 89.5° reads only 12.2×, two
orders of magnitude below the true peak). `gp2_invalid_thetas: []` also
confirmed directly (zero entries) — "zero INVALID points" is accurate.

**(c) NOTES.md's "flags MARGINAL continuously across θ=50.5°–89.5° — the
ENTIRE upper half of the sweep" — DOES NOT MATCH `results.json`.** I
scanned every one of the 78 points in `[50.5°, 89.5°]` in `gp2_curve` and
found **9 points classified VALID, not MARGINAL**, sitting inside that
nominally "continuous" span: θ=52.0° (9.14×), 52.5° (3.43×), 53.0°
(1.54×), 53.5° (2.04×), 54.0° (0.44×), 54.5° (5.61×), 60.5° (2.98×), 61.0°
(7.40×), and **69.5° (4.71×)** — the last one sitting *inside* the very
θc≈59°–73° band the cycle claims corroboration on. `gp2_flagged_band` is
computed as `[min(flagged), max(flagged)]` — a span, not a contiguity
check — and the code never asserts or reports contiguity. "Continuously"
and "ENTIRE upper half" are prose claims not supported by the array they
cite; the actual behavior is a punctuated, fringe-like sequence of
MARGINAL/VALID points, consistent with the same coherent-sum interference
structure this whole T28 sub-thread's null-hunting has always shown, now
riding on top of the grazing amplitude growth rather than replaced by it.

## 2. Steel-man

GP2′ is a legitimate repair of a previously-vacuous check: `_src_amp`
genuinely enters `E`/`H` as a function of θ (unlike `gd["r"]`, confirmed
scale-blind by algebra in Phase 2), so `C(θ)` is a real θ-dependent
quantity and GP2′'s classification is not a dressed-up constant. The
"different quantity than exp-086's ptp" disclaimer holds up under direct
source inspection, not just narrative: I traced `phase4_rescore.py` lines
178–192 and confirmed exp-086's `ptp` is `np.ptp` of `C(θ)` evaluated over
a **local 6°-wide sliding window** (`thc±3°`, 0.2° steps) around each of
37 window centers — a measure of *local curve roughness/range*, feeding a
periodicity-fit stability diagnostic. GP2′ is a **single-point |C(θ)|
divided by a fixed 30°–50° reference-band median** — a measure of
*global amplitude departure from a baseline regime*. These are genuinely
different constructs derived from the same `C(θ)` values, not two labels
for the same computation with a rationalized excuse bolted on. The
severity-gap explanation (6,631× ptp-ratio vs. 235× amplitude-ratio) is
methodologically coherent, not a dodge.

## 3. Sharpest finding

**GP2′ and exp-086's ptp diverge in shape exactly where GP2′ newly extends
coverage — the tail from 74° to 89.5° — and NOTES.md never surfaces it.**
Pulling exp-086's own `phase4_rescore_results.json::sub_results` directly:
`ptp` **falls back down** to 0.0796 at θc=75° and 0.1589 at θc=77° — below
even the 53°–57° pre-peak shoulder (0.126–0.209) — after peaking at 1.696
(θc=69°). That is a local measure recovering as you move away from the
θc≈59°–73° region. GP2′, over the *same underlying model*, does **not**
recover on its own terms: `ratio_to_ref` stays in the 12×–78× MARGINAL
band continuously (no VALID points at all) from θ=74.0° all the way to
89.5°, the true-grazing edge of the sweep — territory exp-086's own
37-window design (window centers only run 5°–77°) never reached at all.
Idealization 50 correctly flags that GP2′ can't itself distinguish "model
invalid near grazing" from "mechanism genuinely changes near grazing," but
that's a generic caveat — it doesn't register that the *specific new
region GP2′ opened up* shows qualitatively different behavior (elevated
but smoothed-out vs. exp-086's own measure's recovery pattern one
instrument-width earlier). Whether the closed-form model's absolute
amplitude genuinely stays anomalously elevated all the way to 90°
incidence (physically plausible for a bare Kirchhoff sum lacking a
grazing-transition term) or whether the 30°–50° reference band is simply
not representative once you're 40°+ away from it is exactly the open
question this cycle's own governance ask exists to surface — and it is
left unexamined.

**Secondary finding, item (i):** Null C's four `delta_scene` values
(40.960901°→41.960901°: `+2.47e-3, +1.51e-3, +5.85e-4, +4.70e-4`) do not
decline linearly toward a nearby crossing — the decline rate from point 2
to point 3 (`Δ=-9.3e-4`/0.333°) is roughly 8× the rate from point 3 to
point 4 (`Δ=-1.15e-4`/0.333°), a sharp deceleration, not a steady approach
to zero. `frac_contrast` at Null C (0.00458→0.00091) is also uniformly
smaller than at A/B across their own comparable windows. This curve shape
is at least as consistent with a **vanishing/weakening feature** at
cpl=40 (a third outcome distinct from both "genuine migration" and
"unconverged discretization," and distinct from "crossing just outside a
mis-sized bracket") as it is with NOTES.md's own Next-item-1 framing
("wider bracket will find it"). A naive wider-and-recentered bracket in
the same spirit as item (ii) could easily reproduce another
NO-SIGN-CHANGE if the feature is actually attenuating rather than merely
relocating.

## 4. Ranked next directions

1. **Reconcile GP2′ against exp-086's own ptp measure over the FULL GP2′
   range, not just the originally-swept 59°–73° band** — extend NOTES.md's
   own queued item 3 (already proposed, zero-FDTD, reuses exp-086's
   method verbatim) to window centers through ~86°–87° so it actually
   covers the 74°–89.5° tail where I found the two instruments disagree in
   shape. Correct the Result section's "continuously"/"ENTIRE upper half"
   language to state the actual punctuated pattern (9 VALID exceptions
   named above) in the same pass — cheap, and this program's own R4/T10
   discipline (disclose, don't silently smooth over a prose/data mismatch)
   applies directly.
2. **Re-test Null C with the vanishing-amplitude hypothesis explicitly in
   scope**, not only a wider/re-centered bracket. At minimum, report
   `frac_contrast`'s trend (not just `delta_scene`'s sign) across any new
   angles, and treat "amplitude keeps shrinking with no crossing found
   even at wider span" as its own reportable outcome distinct from
   NOTES.md's current MIXED/FAIL-family-wide dichotomy.
3. **The queued cpl=50/R5 third point at Null B** (NOTES.md's Next item 2)
   — I agree this is the right next real-FDTD spend: it's the only
   feature with two resolution points on file, and the Richardson-style
   diagnostic's surprising >1st-order-scaling growth (1.78× observed vs.
   0.5625× naive) is exactly the kind of near-null curvature sensitivity
   (R15) a third point would help disambiguate from genuine super-linear
   migration.
