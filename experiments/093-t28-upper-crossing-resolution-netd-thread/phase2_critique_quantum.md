# Phase 2 Critique — QUANTUM OPTICS

*Panel Iteration 70, exp-093, blind parallel critique. Fresh context, no
access to other seats' current-cycle critiques.*

## Steel-man (≤150 words)

From this seat's charter — non-classical absorption enters only as
effective σ(I)/σ(x,t)/ε(ω)/gain parameters — this proposal correctly never
opens that door: T1 N/A, no mechanism claim, pure desk/instrument
calibration reusing exp-090's own vetted statistical machinery
(`find_zero_crossings`/`firth_logistic`/`naive_mle_diverges`/`auc`)
verbatim rather than inventing new fit code, exactly the R4/R8 discipline
this sub-thread's own QUANTUM seat founded R13/R14 to enforce. The
Rank-3-then-Rank-1 sequencing correctly avoids repeating exp-092's own
Red-Team-caught mistake (spending on an article whose `sigma_max` was
still unvalidated). Item 5's NETD backfill closes a real, previously-
flagged gap (discarded `g_cell` fields) by deterministic re-run, not
speculation. Item 4 finally runs a twice-cited, never-run desk check under
an explicit third-citation tripwire. If item 2's §6 arithmetic is
corrected, the remaining design — denser off-grid resolution of the
double-crossing, a localized `sigma_max` check — is proportionate and
faithful to the reconciled queue it executes.

## Sharpest attack (≤150 words)

Item 2's headline claim — the n=8 `cpl=30` margin/Y relationship is
REVERSED (AUC=0.0000) from exp-090's original (AUC=1.0000) — is a
sign-convention artifact, not physics. Re-running exp-090's own `auc()`
exactly as it was called there, `auc(-pos_m,-neg_m)`, on the proposal's
own n=8 table returns AUC=1.0000 — identical direction, not reversed.
exp-090's committed Firth fit is `β=[1.7806,-5.6315]` (`results.json`);
the proposal's "new" `β=[3.7650,-5.6070]` has nearly the same negative
slope — both mean lower margin predicts Y=1, the SAME decision rule, not
the "opposite" claimed. The zone formula (`max(pos),min(neg)`) applied
unmodified, no swap needed, already gives `[4.1083,5.4287]`. AUC=0.0000
arises only by calling `auc(pos_m,neg_m)` without exp-090's own negation —
an inconsistent convention across the two cited numbers, mislabeled as a
finding. Load-bearing: Idealization 15 and the pre-registered Phase-4
bit-exact gate will faithfully certify the wrong headline unless fixed
before freeze.

## Independent recomputation (R4 discipline — actual function invoked, not hand-typed)

Ran exp-090's own `auc()`, byte-for-byte, against the proposal's own §6
n=8 table (`pos={2.3005,4.1083}` at 40.0°/40.2°, `neg={5.4287,9.1877,
11.2790,15.6474,20.6530,23.1785}` at 41.4°/39.8°/37.2°/39.6°/39.4°/39.2°):

```
auc(-pos, -neg)  ->  1.0000   # exp-090's own calling convention
auc( pos,  neg)  ->  0.0000   # the proposal's own reported figure
zone: max(pos)=4.1083, min(neg)=5.4287, not inverted
```

`auc(-pos_m,-neg_m)` is the literal call site in `experiments/090-.../
run.py::main()` (`auc_margin = auc(-pos_m, -neg_m)  # lower margin =>
more likely X`) — the convention that produced exp-090's own filed
`AUC=1.0000` (verified directly against `experiments/090-.../
results.json::q1.auc_margin=1.0` and `q4.beta=[1.7805895...,
-5.6315196...]`, `q3.zone=[1.4763877...,2.170947...]`). Applying that
exact same convention to the new n=8 sample gives 1.0000, not 0.0000: the
two datasets have the identical margin→Y direction (lower margin predicts
Y=1) both before and after this cycle's new points. The proposal's
0.0000 figure requires dropping the negation exp-090 used — a genuinely
different question ("does higher margin predict Y=1?", trivially no in
both datasets) silently substituted for the one the "REVERSED" comparison
claims to answer. The Firth slopes corroborate this independently: a
near-identical negative `β₁` in both fits is the actual "algebraic
signature" here, and it signs a relationship that has NOT changed, not
one that has flipped. Every downstream sentence built on "reversed" —
the "roles of max/min swapped to match the reversed direction" language
(no swap is actually needed; the unmodified formula already produces the
reported zone), "the opposite decision rule from the original's own
'above predicts Y=1'" (the original's own committed decision rule is
already "below predicts Y=1" — `m₅₀=2.071013` with 41.4°/40.2° margins of
1.31/1.48 both below it and both Y=1) — is downstream of this same single
sign-convention slip, not independent corroboration of it.

This is not a re-litigation of R13 or R14: it is neither a
zero-crossing-capable denominator (R13) nor a subtractive-cancellation
numerator (R14) — `margin=frac_contrast/FLOOR` has a fixed, non-zero
`FLOOR` denominator and an absolute-value numerator. It is a fresh
instance of the hazard R4's own Iteration-50 addendum names for sign
corrections generally: a comparison across two computed numbers that
"agree" with a narrative only because they were produced by two different
conventions, not independently re-derived by an external method before
being trusted. THERMODYNAMICS' own §6 text states this table was
"pre-verified... against the real house functions, imported unmodified"
— true of the function bodies, false of how consistently they were
*called* across the comparison being drawn.

## Item 5 / R14 discharge claim (§13) — scrutinized as instructed

§13's R14 entry states the NETD backfill "is reported per-cell, not used
to drive any new classification claim this cycle, so R14's own
minimum-discharge conditions are not triggered by it." Narrowly true of
the NETD fields themselves (`dt_ss_full_K`/`netd_classification`, item
5b, explicitly informational/non-gating) — but the sentence sits
immediately downstream of a table (§6) that leans on 40.0° as "the
**only** unambiguous `Y=1` example in this sub-thread's entire native-
`cpl=30` record," and 40.0° is a point item 5's own 28 calls this cycle
physically re-measure. The load-bearing classification value at 40.0° is
asserted, correctly, to be a bit-exact *reproduction* of exp-092's
already-scored `rank1.per_theta` entry, not new information — so the R14
claim survives on that technicality — but the adjacent §6 prose ("using
item 1's and item 3/5's own already-collected `cpl=30` primitives")
blurs exactly this distinction for a reader who has not traced which
specific fields item 5 actually adds versus reproduces. Worth a
one-sentence tightening in Phase 3, not a mandatory fix on its own.

## Verdict: **support-with-changes**

The sequencing, the mandatory dispersion-integral discharge, and the NETD
backfill design are sound and correctly scoped. But item 2's §6 is not a
minor wording slip — it is the proposal's own disclosed "genuinely new
finding," pre-registered for a bit-exact Phase-4 reproduction gate that
will faithfully certify a false directional claim if run as specified.
Because item 2 is desk-only (zero FDTD, §6: "Calls: 0"), this is fully
fixable before Phase 3 freeze at zero cost to the rest of the design: no
new run, no rescheduling, no budget impact on items 1/3/4/5.

**Mandatory fix to flip to plain support:** before Phase 3 freezes
anything, recompute item 2's `AUC(margin)` using exp-090's own
`auc(-pos_m,-neg_m)` calling convention (matching how the number it is
being compared against — the original `AUC=1.0000` — was itself
produced), strike the "REVERSED"/"opposite decision rule"/"roles of
max/min swapped" language, and restate the actual, genuinely disclosable
finding correctly: the n=8 `cpl=30`-only sample preserves the SAME
lower-margin-predicts-`Y=1` relationship as the original n=7 `cpl=20`
sample, with the zone `[4.1083,5.4287]` sitting on a different but
non-contradictory numeric scale (a real, defensible finding on its own —
this proposal does not need a false reversal to be worth reporting).
