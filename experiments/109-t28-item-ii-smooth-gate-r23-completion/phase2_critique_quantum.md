# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full, PLAN.md's Current state, exp-108's own
`phase5_review_quantum.md` (this seat's own prior-cycle finding, the
direct precursor to this proposal's item 4), the Phase 1 proposal, and
its subject code before critiquing — instructed to re-derive its own
prior-cycle hand-check from scratch rather than trust it.

## 1. Steel-man (≤150 words)

The fix is mathematically airtight where it matters: `residual_std ≤
raw_std` is a genuine linear-algebra identity for any OLS fit whose
design matrix carries an intercept column (`A_mat=[1,1/margin]` does),
so falling back to raw std on `smooth=False` cannot manufacture a false
CONFIRM — this is provable, not merely lucky on these two points. I
independently re-derived the fallback exactly (raw std 5.008328×10⁻⁶ at
r=156, 2.124086×10⁻⁶ at r=312, ddof=0, matching the proposal's table to
6 significant figures) and confirmed both clear CONFIRM (2.96×/5.81×
inside the bar). It genuinely discharges R24's forward-elevating clause
— the gate is now wired into the executed classification path, not
merely computed and narrated — reuses the established zero-FDTD
`reclassify_*.py` idiom, and honestly names its own undischarged R18 gap
rather than hiding it.

## 2. Sharpest attack (≤150 words)

Independently re-derived: at r=156, `r_squared=0.6654` — a substantial,
physically plausible fraction of variance explained by the box-radius
convergence trend — falls on the "not smooth" side of an untouched,
un-re-derived `R²≥0.90` cutoff borrowed wholesale from
`classify_item_i`'s different (anisotropy-detection, n/a here) question.
The fallback therefore discards a demonstrably real 1/margin trend and
reverts to the *full* raw std (5.008e-6 vs. 2.897e-6 detrended — a 73%
inflation), reinstating most of the convergence-bias contamination my
own founding Phase-2 attack existed to strip out, precisely where that
contamination is most plausible (r=312's R²=0.021 case has almost
nothing to lose by falling back — 1% difference). "Provably
conservative" holds only for the CONFIRM/REFUTE band ordering, not for
whether raw std is the epistemically correct floor estimate; a binary
cutoff, uncalibrated at n=6/4-df (the still-deferred Tier-1 synthetic
control), treats r=156's partial trend identically to r=312's near-null
one. Non-outcome-reversing this cycle only by margin, not by the gate's
own design.

## 3. Verdict

**support-with-changes**

## 4. Change that would flip to full support

Persist and narrate, in `stat_source` and the Result prose, the
raw/residual ratio whenever the fallback fires (here 1.73× at r=156 vs.
1.01× at r=312) — so a future reader can see the binary cutoff is
discarding a materially different amount of demonstrated trend at each
point, rather than reporting both non-smooth cases as equivalently "not
smooth, falls back to raw."
