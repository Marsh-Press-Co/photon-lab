# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 82 (exp-105)

*Fresh seat, blind to any other seat's current-cycle Phase-5 review. Read
PANEL.md, LOGBOOK.md in full (RULED OUT R1–R23, Live Threads T1–T28, the
Iteration-65 CHECKPOINT entry), and the full exp-105 record
(`phase1_proposal.md`, all five `phase2_critique_*.md`, `phase2_redteam_
audit.md`, `NOTES.md`, `run.py`, `results.json`) before writing this.*

## Verdict: **CONFIRM-WITH-GAPS**

The extended `DISCLAIMER` string is genuinely present, verbatim, at
execution time, in both text blocks that matter — this cycle's own
mandatory fix 9 (my seat's own Phase-2 flip condition) is substantively
honored. But the code-level *enforcement* of that presence is narrower
than the module's own docstring claims, and narrower than R23's own
founding two-assert pattern — a concrete, checkable gap, not a content
failure. Full detail below.

---

## 1. Did the extended DISCLAIMER actually land? Verified directly, not trusted.

### 1a. Source

`run.py:164-167`:

```python
DISCLAIMER = ("Raw physical intensity/phase ratios only -- no Weber-contrast or "
              "C_thr(L) perceptual scoring is performed this cycle; not a claim "
              "about human visibility. " +
              ts.netd_disposition(0.0, NETD_BAND_K)["disclaimer"] + ".")
```

This reuses `lab/thermo_sidecar.py::netd_disposition()`'s own `disclaimer`
field verbatim (confirmed by direct read, `lab/thermo_sidecar.py:806-810`):
*"NETD is an instrument/detector threshold, not a human perceptual one --
this classification does NOT bear on constraint-3/4's human-eye verdict
(panel Iteration 20, VISION SCIENCE's mandatory fix, Red Team attack 7)."*
Correct load-bearing source, not a hand-typed paraphrase — exactly what my
own Phase-2 flip condition asked for, and this reuses the *original*
Iteration-20 fix (not a fresh restatement of it), the strongest form of
provenance this program's own R4 discipline recognizes.

### 1b. Did it survive into what was actually printed/persisted?

Grepped `results.json::predictions_text` and `::result_text` directly
(not the source template) for the load-bearing NETD sentence:

```
needle in predictions_text: True
needle in result_text: True
```

Both fields carry the disclaimer's opening perceptual-scope sentence *and*
the NETD-specific instrument/detector-threshold sentence, verbatim,
immediately adjacent, exactly as `DISCLAIMER` constructs it. **Confirmed:
this is not merely a source-code intention — it is what the executed run
actually printed to console and wrote to the committed `results.json`.**
This is the exact class of check my own seat's Phase-2 critique and Red
Team's audit (attack 9, elevated to mandatory, citing this sub-thread's
four-instance disclaimer-erosion history) demanded, and it passes on
direct inspection of the executed artifact, not the aspirational template.

### 1c. The gap: code-level enforcement is narrower than claimed and narrower than R23's own founding pattern

`run.py`'s own module docstring (lines 40-45) states the fix was
"asserted present in both PREDICTIONS_TEXT and RESULT_TEXT (R23 pattern)."
Grepping every `assert` in the file:

```
518:        assert lo_x > ABSORB and hi_x < g["N"] - ABSORB, ...
520:        assert lo_y > ABSORB and hi_y < g["N"] - ABSORB
831:    assert DISCLAIMER in result_text, "R23: disclaimer missing from Result block"
```

**There is exactly one `DISCLAIMER`-related assert, on `result_text`. There
is no `assert DISCLAIMER in predictions_text` anywhere in the file.**
R23's own founding implementation (exp-104, LOGBOOK.md's own R23 entry,
verbatim: *"two hard asserts (`assert DISCLAIMER in PREDICTIONS_TEXT`,
`assert DISCLAIMER in RESULT_TEXT`)"*) is the explicit precedent this
cycle's own docstring claims to match — and does not, in the code, fully
match. In practice `build_predictions_text()` embeds `{DISCLAIMER}`
directly in an f-string (line 388), so nothing in this file's *current*
logic can omit it without also breaking the string literally — which is
why §1b's grep against the executed record comes back clean regardless.
But that is a structural accident of how the function happens to be
written today, not a code-enforced guarantee the way `result_text`'s own
assert is (`result_text` is built by string interpolation across many
conditional branches — `r312_committed`, `p4_312 is not None`, etc. —
where an assert earns its keep precisely because the disclaimer's
presence is not otherwise obviously guaranteed by construction;
`predictions_text` has no comparable branching, which is presumably why
no one felt an assert was needed there — but that reasoning is nowhere
stated, and the docstring's claim overstates what the code actually
checks).

**This is a genuine, independently-verifiable defect: a documentation/code
mismatch, not a content failure.** It does not change any verdict this
cycle (the string is, in fact, present, confirmed twice over — by direct
grep of the template and by direct grep of the persisted execution
record). But given this exact sub-thread's history — the Iteration-65
CHECKPOINT (criterion 4 FIRED, fourth instance, on this identical NETD/
thermal-sidecar disclaimer-erosion pattern) explicitly mandated that *"the
'carried idealizations' banner is now required at BOTH the Predictions
section AND the Result section... since this cycle is direct, first-hand
proof that a banner scoped to one section does not propagate to the
other"* — a future editor of this file who trusts the docstring's claim
("asserted present in both") rather than the actual assert list could
introduce a real, silent regression in `predictions_text` specifically,
with no test to catch it. **Recommend, as a same-shift or Iteration-83
zero-cost fix: add `assert DISCLAIMER in build_predictions_text(g78, g156,
g312)` (or an equivalent check on the `predictions_text` variable actually
persisted at line ~861), restoring R23's own two-assert founding pattern
exactly, and correct the docstring if the two are ever intentionally
allowed to diverge.**

---

## 2. NOTES.md Result/Learned — checked for implied-visibility backslide

Grepped `NOTES.md` for the visual-vocabulary leak class my own seat
flagged at exp-103 Phase 2 ("shadow," "fills in," "floor") and again at
this cycle's own Phase 2 ("darkens," "shadow continuing to deepen"):

```
grep -n -iE "shadow|darken|darker|visible|invisib|perceiv|human eye|
             glimpse|silhouette|glows|fades from view" NOTES.md
360:   ever deeper into the geometric shadow's near zone as r grows), a
```

**One hit, and it is out of scope for what this check is protecting.**
Line 360 sits in the **Next** section (Iteration-83 queue material), not
Result or Learned, and reads in full context: *"is `kappa_window`'s own
~20×/~185× two-step collapse a genuine near-field physical effect (the
fixed-cell window offset representing an ever-shrinking FRACTION of the
object's own growing radius, pushing the measurement ever deeper into the
geometric shadow's near zone as r grows)... ?"* — this is "geometric
shadow" as a standard near-field/ray-optics term of art (the region behind
an object a ray-optics construction would predict is shadowed), posed as
one of several **candidate, untested hypotheses** for a resolution check,
not a claim. It does not describe what a human observer would see, and it
does not appear inside the frozen Result or Learned prose at all.

The Result section's own language for P3 — *"shape_ratio = 19.79... nearly
5× past the linear-law's own already-generous band... kappa_window falls
by ~20.7× from r=78→156, then by ~185× from r=156→312 — accelerating, not
merely failing to fit a power law"* — and the Learned section's — *"this
channel's kappa_window collapses by more than four orders of magnitude
across the same r-family (0.018→0.00089→0.0000048), accelerating rather
than flattening"* — both stay correctly and consistently scoped to the
raw physical intensity ratio itself: numeric values, fold-changes, and
functional-form language ("collapse," "accelerating," "falls by") applied
to `kappa_window` as a number, never to an implied visual appearance
("darkens," "the object becomes hard to see," "the eye would..."). **No
backslide into implied-visibility language in the executed Result/Learned
sections.** This is a real improvement in discipline over the exp-103
instance my own seat caught, and matches this cycle's own DISCLAIMER
staying present throughout (§1).

---

## 3. The scope-boundary question: does P3's shape_ratio=19.79 bear on constraint-3 at all?

**No — and my seat is positioned to say so with numbers, not just
assertion, which the task specifically asked for.** Two independent
reasons, first-order and second-order.

**First-order: `kappa_window` and Weber contrast C are not measuring the
same physical scenario, even setting aside their numeric relationship.**
Constraint 3's own dedicated instrument (`lab/ambient.py`, PANEL.md's
metrics table) scores the object's own silhouette under **ambient**
illumination — diffuse/multi-angle, incoherent, broadband in general, read
out AT the object's own location, the way a human observer looking at the
object (not through it) would sample luminance. `kappa_window` is a
single-λ (600nm), single-polarization, fully **coherent**, on-axis
forward-**transmission** measurement, read out in a window *downstream* of
the object (`BEHIND_X_LO/HI`, 27–127 cells beyond `R_COAT`), in the near
field (`z/z_R` spans 0.0158–0.2531 across this cycle's own r-family, per
Red Team's corrected figure — itself 5× *past* T8's own already-shallow
ambient-bench span, not closer to any far-field regime). This is
structurally the beam-transmission/constraint-1 diagnostic family (T11's
own lineage), not the ambient/constraint-3 diagnostic family (T2/T7/T8's
own ambient-bench lineage) — a coherent near-field diffraction pattern
downstream of a point source is not what a broadband, spatially- and
temporally-integrating human eye looking at the object under ambient
light would ever sample. The document's own DISCLAIMER already states
this correctly ("no Weber-contrast or C_thr(L) perceptual scoring is
performed"); P3's dramatic falloff is a fact about a diffraction/
interference-sensitive coherent near-field channel at fixed absolute
window offset, not a fact about the object's own ambient appearance.

**Second-order: even granting the loosest possible identity `C = κ − 1`
(treating κ_window naively as an intensity ratio at "the object" vs.
"background," the closest reading that WOULD connect it to constraint-3),
the result is already saturated at r=78, before any of P3's own dramatic
scale-dependence begins to bite.** Computed directly from this cycle's own
three `kappa_window` values:

| r | κ_window | C = κ−1 | \|C\| |
|---|---|---|---|
| 78 | 0.018337 | −0.981663 | 0.9817 |
| 156 | 0.0008867 | −0.9991133 | 0.9991 |
| 312 | 0.000004793 | −0.999995207 | 0.99999521 |

This program's own pinned, sourced perceptual-threshold function (T2,
exp-020, carried forward unmodified since): `C_thr(L) = 0.005·max[1,
(L/3)^−p]`, p∈[0.4,0.5] — a **photopic floor of 0.005**, orders of
magnitude below all three |C| values above. Under this naive mapping, the
r=78 point is *already* saturated to ~200× past photopic threshold before
the object grows at all — the ~1,100× total collapse in κ_window from
r=78→312 corresponds to a Weber-contrast change of only **ΔC ≈ 0.0183**
(−0.9817 → −0.99999521), a small, saturating, threshold-irrelevant
absolute move, not a dramatic one. Weber contrast is bounded in [−1, 0]
for a darkening target; once κ is already ≪1, further multiplicative
collapse in the raw intensity ratio buys almost nothing in contrast terms
— exactly the compression this program's own C_thr(L) machinery exists to
score against, and exactly why a raw intensity-ratio fold-change is the
wrong unit to reason about visibility in near this regime.

**Conclusion, stated plainly per this seat's own duty: P3's own headline
result — a genuinely striking finding on its own coherent-intensity
channel, and a real, disclosed non-replication of T8's ambient-channel
finding worth keeping on the record — carries approximately zero
information about constraint-3, under either the correct (structurally
different measurement) or the loosest-possible (naive C=κ−1) reading. Any
future citation of "shape_ratio=19.79" or "kappa_window collapses by four
orders of magnitude" as evidence bearing on how dark the object looks to
a human observer would be a unit/scope conflation this seat's own charter
exists to catch — flagging it now, before any such citation is written,
per PANEL.md's own "pin numeric thresholds... BEFORE any run that scores
against them" duty applied retroactively to a result that already ran.**

---

## 4. Other checks performed

- **P5's scored claims** ((a) UNDETECTABLE at every r, (b) margin
  monotonically non-increasing) are, per `netd_disposition`'s own
  docstring, instrument/detector-threshold findings — correctly kept
  separate from any constraint-3/4 verdict throughout `NOTES.md`'s Result
  and Learned sections (grep-confirmed, no paragraph attaches P5's
  classification to a human-visibility claim).
- **Gate P0/P1 rescoping** (Red Team mandatory fix 3, correctly applied):
  `NOTES.md` states Gate P1 as a "rescoped self-consistency check," not an
  independent physics reproduction — matches the corrected framing, no
  overclaim recurrence.
- **R23's own founding scope note** ("covers only ONE of at least three
  disclaimers... the THERMODYNAMICS thermal-sidecar-N/A sentence...
  remain[s] manual prose") is the exact gap my own Phase-2 critique
  flagged for this cycle specifically. This cycle's mandatory fix 9 closes
  it for content (§1b) but, per §1c, not quite for code-enforcement
  parity with the P5/thermal channel now being *live* rather than N/A —
  a half-closed instance of R23's own scope note, not a reopening of it.

---

## Top-3 ranked candidate directions for Iteration 83, from this seat's own discipline

1. **Restore R23's two-assert founding pattern**: add an explicit
   `assert DISCLAIMER in predictions_text` (or equivalent) alongside the
   existing `result_text` assert, and correct the module docstring's
   overclaim. Zero FDTD cost, one line, closes §1c cleanly before it can
   ever become a fifth instance on this exact disclaimer-erosion lineage
   (Iteration 53/T16, Iteration 63/exp-086, Iteration 64/exp-087,
   Iteration 65/exp-088 CHECKPOINT-firing, this cycle's own half-gap) —
   the cheapest possible preventive action against a pattern this program
   has already paid a CHECKPOINT for once.
2. **Pin the κ↔C scope-boundary finding (§3) as a standing, cited note**,
   not just this review's own one-off arithmetic — either a short
   addendum to this sub-thread's own Idealizations/DISCLAIMER language
   ("kappa_window's own scale-dependence, however dramatic, is bounded in
   Weber-contrast terms once κ≪1; see [this review] for the C=κ−1
   saturation calculation") or a LOGBOOK Live-Thread cross-reference from
   T13/T14 (the C(z/z_R)-extrapolation threads) noting that this
   channel's own near-field scale-dependence is NOT informative for that
   still-open question. Prevents exactly the retroactive misreading named
   in §3's own conclusion, at zero FDTD cost, before any future cycle
   cites "shape_ratio=19.79" out of context.
3. **NOTES.md's own top Next item — P3's accelerating-collapse resolution
   check (genuine near-field effect vs. floor/dynamic-range artifact)** —
   I rank this third, not first, from my own seat specifically because
   §3 already shows the answer is low-stakes for constraint-3 either way
   (both readings stay far past any perceptual threshold); it remains
   genuinely important for THIS channel's own internal validity and for
   T12's unresolved non-monotonicity question, just not for the
   witness-visibility program this panel ultimately serves. Endorsed as
   next physics work, ranked behind the two zero-cost integrity/scope
   items above that this seat is specifically chartered to catch.
