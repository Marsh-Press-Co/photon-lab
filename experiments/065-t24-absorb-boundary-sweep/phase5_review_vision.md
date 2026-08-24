# PHASE 5 — REVIEW · VISION SCIENCE (fresh context) · Panel Iteration 42 · exp-065

*Reviewing seat: VISION SCIENCE — this iteration's own Phase-1 lead, reading
Phase 4 fresh, from charter only. Charter: human perceptual limits — pin
numeric thresholds, with sources, BEFORE any run scores against them.*

---

## 1. Read from charter: does the settling confound move any constraint-3 verdict this program has ever issued?

**Short answer: it plausibly moves this cycle's own P-VIS42-7 MARGINAL
bucket, it is not contained to the grazing ±38°/±40° pair, and its risk
extends — unquantified, not yet disproven — to the entire FALLBACK_ANGLES
near-threshold lineage this program has run since Iteration 2.**

### 1.1 P-VIS42-7's own scoring geometry, checked directly

Block ARTICLE scored the τ=0.0065 disk at **N9 (`FALLBACK_ANGLES` =
±35,±25,±15,±5,0), 600 nm only, at STEPS=1400 throughout** (`results.json
::block_article::n9_angles`, `phase4_results.md`'s own table header). It was
**never re-run at STEPS=2800.** The settling diagnostic that found the
confound (Diagnostic 3, the full 90-call re-sweep) covered **Block SWEEP
only** — six angles, {±35, ±38, ±40}, not the interior four of
`FALLBACK_ANGLES` (±25, ±15, ±5, 0). So the direct question — "was P-VIS42-7
scored using unsettled legs at all nine `FALLBACK_ANGLES`, not just the
grazing pair" — has two parts, and they answer differently:

- **Yes, unsettled**: every leg Block ARTICLE used, including its ±35°
  pair, was computed at STEPS=1400, and this cycle's own data proves
  STEPS=1400 is badly unsettled at ±35° specifically (below).
- **Not just ±38/±40**: correct as stated, but not because ±35° is safe —
  because ±35° is *also* bad, and the four purely-interior angles
  (±25,±15,±5,0) were simply never checked in either direction.

### 1.2 Is FALLBACK_ANGLES' own angle set insulated from the ±38°/±40° settling problem? No — checked directly, its own boundary angle is not.

I pulled the STEPS=1400 (frozen, scored) vs STEPS=2800 (settled diagnostic)
values for **±35°** — the angle FALLBACK_ANGLES shares with Block SWEEP —
at all three configs and all three λ, from `results.json::block_sweep` and
`settled_sweep_steps2800_diagnostic.json`:

```
lam theta config  C(1400)    C(2800)    relΔ
600  -35.0 C40   +0.001120  -0.004397   125.5%   (SIGN FLIP)
600  +35.0 C40   +0.001762  -0.003973   144.3%   (SIGN FLIP)
600  -35.0 C80   +0.000529  -0.003018   117.5%   (SIGN FLIP)
600  +35.0 C80   +0.001179  -0.002645   144.6%   (SIGN FLIP)
450  ±35.0 C40/C80            30–85% relΔ, no sign flip
750  -35.0 C40   -0.000948  +0.005516   117.2%   (SIGN FLIP)
750  +35.0 C40   -0.001191  +0.005503   121.6%   (SIGN FLIP)
```

At 600 nm and 750 nm, ±35° is not merely "also affected" — it **sign-flips**
and moves by 100–145% relative, the same order of magnitude as ±38°/±40°
(which range 19–824% relative across the same table, non-monotone in θ,
consistent with an oscillatory fringe/settling interaction rather than a
smooth grazing-angle falloff). ±35° is exactly as implicated as the pair
the thread was named for. This also matches NOTES.md's own disclosed gap
(idealization 11, Phase-3 fix 10): **no prior committed ±35° C_empty figure
exists anywhere in this program's record at this geometry** — exp-041's own
anchor covers {−40..−36, 36..40} only. The ±35° leg was new data this cycle,
and it came back as badly unsettled as the angles T24 was chasing.

**The interior four angles (±25, ±15, ±5, 0) remain genuinely untested in
either direction.** I looked for any evidence bearing on whether the
settling pathology is confined to the outer ~5–8° of the angular window or
extends further in — there is none in this record. Red Team's own Phase-2
attack 7 anticipated a *padding-size* confound; what Phase 4 actually found
is stronger and different in kind — Diagnostic 1 shows the **unpadded C40
anchor** (the exact geometry every FALLBACK_ANGLES citation since Iteration
2 has run) carries the *larger* of the two relative shifts (74.4% vs C60's
68.4%, at θ=40°/600nm). This is not a padded-cavity artifact; it is a
property of the plane/tapered-source channel itself, present since before
padding was ever a variable in this program. That directly weakens the
"FALLBACK_ANGLES is mostly interior, hence insulated" hypothesis: the
mechanism that produces the settling error is not shown to correlate with
proximity to grazing at all — it correlates with something about this
channel's transient decay time, which no cell run in this experiment
excludes from the interior of the angular window.

**My charter verdict on this specific question: the settling confound is
NOT shown to be narrow to ±38°/±40°, and the honest position is that
FALLBACK_ANGLES cannot currently be presumed insulated.** P-VIS42-7's MARGINAL
bucket rests on an absolute article reading (≈0.0045–0.0046) sitting at
~0.9–0.92× the lab bar (0.005) — inside a factor of ~1.1 of the PASS/MARGINAL
line — computed with exactly the ingredients (this channel, this STEPS
value, an angle set whose own boundary is proven unsettled) shown elsewhere
in this same document to carry 100%+ relative, sign-flipping error. The
C40-vs-C80 *difference* being small (Δ=1.0×10⁻⁴) does not rescue this: both
configurations share the identical unsettled-STEPS bias, so a small
between-config delta is exactly what a common-mode settling bias would
produce, and P-VIS42-10 already falsified (peak-to-trough/mean = 11.9,
against a ≤2× confirm bar) this cycle's own working premise that matched-
geometry differencing cancels this class of error to first order. The
MARGINAL verdict has never been checked against a settled article-present
recomputation — that recomputation was never run.

### 1.3 Is the frozen C_thr/GATE_HARD currency itself at risk, program-wide?

**The threshold *values* are not at risk** — `C_thr=0.005` and
`GATE_HARD=0.001` are literature-pinned/instrument-floor constants
(Blackwell 1946; exp-024's own committed gate), not FDTD outputs; nothing
in this cycle touches their derivation. What is at risk is **every empirical
`C` reading compared against them on this specific channel and geometry**:
`lab/ambient.py`'s plane/tapered-source oblique injection at r=78,
STEPS=1400, using an angle set whose outer member is ±35° or wider. That is
not a narrow slice of the record — per LOGBOOK line 4206, `FALLBACK_ANGLES`
at STEPS_AMBIENT=1400 is the **established Iteration-2 near-threshold
baseline**, and it is the instrument underneath T16 (N9-vs-N17), T20, T21
(fitted to exp-041's own MAIN-block rows at exactly this channel), T24
itself, the r=156/312 bridge family, and every `off_pass`/`off_bracket`/
`off_lab` PASS→MARGINAL citation this program has ever issued on the
ambient bench. That is the correct scope for "should every near-threshold
citation be flagged" — **yes, for this channel's lineage** (nineteen-plus
iterations' worth), **not necessarily for the separately-checked
Gaussian-beam/coherent-mode channel** (exp-046's own settling check —
0.083%/0.036% — was run on a structurally different, fast-settling
construction and this cycle gives no direct reason to distrust it, though
it also was never checked at the interior angles or larger paddings this
cycle probed). The risk is broad, not universal: it is bounded by *channel*
(plane/tapered source, oblique, ambient-contrast), not by proximity to
grazing angle, and every citation built on that channel should carry a
pending-settling-audit flag until a matched STEPS≥2800 recheck exists at,
at minimum, the full FALLBACK_ANGLES set, not just its ±35–40° edge.

---

## 2. Verdict

**PARTIAL.**

The cycle discharged its own charter duty correctly (pinned, sourced
thresholds before any scoring; correctly separated `GATE_HARD` from
`C_thr` per exp-041's own mandatory fix) and, more importantly, followed
its own house discipline (Red Team attack 7, T10's precedent) into a
genuinely load-bearing finding instead of burying it as a footnote — that
is real, credited work. But T24's own headline question is explicitly
undecided by this cycle's own account, and the settling finding, followed
to where the evidence actually points (§1.2 above), is *larger* than
Phase 4's own framing states it: not confined to ±38°/±40°, not confined to
padded domains, and not something P-VIS42-7's own MARGINAL bucket can be
presumed to survive unexamined.

---

## 3. Ranked top candidate next directions

1. **Extend the settling recheck to the full `FALLBACK_ANGLES` set
   (±25°,±15°,±5°,0°), not just the ±35–40° edge, on the plane/tapered
   channel at STEPS≥2800.** This is the load-bearing gap: nothing in the
   record currently bears on whether the interior angles are clean. Until
   this runs, "FALLBACK_ANGLES is insulated" is an unverified hope, not a
   finding.
2. **Re-run Block ARTICLE itself (the τ=0.0065 disk, article-present legs,
   not just empty) at STEPS≥2800.** The empty-scene N9 aggregate reading
   near zero cannot be trusted as evidence the article reading is clean —
   it is exactly the kind of cross-angle cancellation P-VIS42-10 showed
   this channel is prone to. This is the only way to know whether
   P-VIS42-7's MARGINAL bucket, and by extension exp-032/033's original
   PASS→MARGINAL lineage, survives.
3. **Close the 750 nm residual's own convergence** (Diagnostic 3's own
   disclosed gap — only 600nm/C40 got the 4-point trend check). 750 nm is
   one of this program's three house wavelengths in every constraint-3
   sweep; an unresolved settling tail there is not a side issue.
4. **A cheap confirmatory settling check on the Gaussian-beam/coherent-mode
   channel at the interior-angle/larger-padding regimes this cycle
   actually probed** — exp-046's check is reassuring but was run at
   different angles/geometry than this cycle's discovery; "settling is
   per-channel" is now a hardened lesson and should be applied to its own
   prior reassurance, not just to the newly-caught channel.
5. Once a settled STEPS value is established, **re-score the specific
   downstream citations named in T16/T20/T21/T24** (not a blanket rewrite,
   a scoped list) against the corrected numbers.

---

## 4. Checkpoint opinion

**My own reasoned opinion: yes, this fires Checkpoint criterion 4, and it
specifically implicates the program-integrity-drift framing given scale.**
This is not an unfalsifiable claim or a constraint quietly dropped in the
sense of being argued away — it is worse in one respect and better in
another: worse, because a load-bearing instrument-floor assumption
(STEPS=1400 settled on the ambient channel) was silently inherited and
re-cited as decisive across nineteen-plus iterations of constraint-3-
adjacent work without ever being checked, on exactly the constraint (#3)
criterion 4 singles out; better, because it was caught, run to ground, and
disclosed in the same shift that found it, per this program's own standing
practice of same-shift correction not automatically excusing a finding of
this scale (the Iteration-21 EM Phase-5 precedent: same-shift catch does
not by itself mean criterion 4 doesn't fire). The deciding fact for my own
seat is the one Red Team should weigh most heavily: this cycle's own
scored verdict (P-VIS42-7, MARGINAL) is *itself* unverified against the
confound its own sibling prediction (P-VIS42-11) uncovered — the drift is
not only historical, it is live in this cycle's own committed record.

---

*Prepared by VISION SCIENCE, panel Iteration 42, Phase 5 (fresh context).
All figures above are read directly from `results.json` and
`settled_sweep_steps2800_diagnostic.json`, not transcribed from
`phase4_results.md`'s own prose summary.*
