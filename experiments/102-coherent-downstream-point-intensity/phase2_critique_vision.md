# Phase 2 Critique — VISION SCIENCE seat (Panel Iteration 79, exp-102)

## Steel-man (own charter: human perceptual limits — what would make an eye
## fail to register something physically present)

This instrument finally builds the right physical quantity type for my
seat's future work. A witness's percept is a local retinal irradiance
comparison at a point/solid-angle, not power integrated over an arbitrary
closed surface — `sigma_scat_downstream` (exp-101) is provably the wrong
quantity to ever feed a Weber-contrast model, because a coherent shadow and
a coherent refill can carry identical flux. `κ(θ)`, a same-point coherent
`|Ez|²` ratio referenced to a bit-identical-phase empty scene, has the
correct locality and units to eventually become the numerator of any future
`L_article/L_ambient` comparison once adaptation state and geometry are
attached (T2's still-pending Tier-2 conversion). Gate B's reproduction check
against exp-001's already-trusted `beam_behind` figure, and the explicit
`I0_corrected` fix removing the `1/cosθ` leak into any future absolute
citation, are exactly the due diligence a threshold-scoring instrument must
clear before my seat can trust a single number it produces.

## Sharpest attack

Scoping is *mostly* clean — no `C_thr(L)` is invoked or scored, and
Predictions 1–4 are stated as raw ratios. But one sentence crosses the line
it claims to respect. §4 states: "κ(θ) alone answers 'is this point dark
relative to what would be there with nothing in the way,' **which is
constraint 1's witness question**." That is a perceptual claim smuggled
past the disclaimer: "witness question" and "dark" carry human-observation
meaning, but κ(θ) is compared to nothing except itself — no adaptation
state, no ambient level, no C_thr(L). Whether a reduction to κ=0.05 is
something a witness would even register depends entirely on the still-
unbuilt Tier-2 conversion; declaring the raw ratio already "answers" the
witness question presumes the threshold doesn't matter, which is precisely
the unexamined assumption my charter exists to catch before a run scores
against it. Elsewhere the document is properly disciplined — this is the
one leak.

## Verdict

**Support-with-changes.** The instrument design, gates, and predictions are
sound and correctly diagnostic-only. Fix the one line above (§4) and this
is unconditional support.

## Parameter change that would flip to unconditional support

Replace "which is constraint 1's witness question" with "which is
constraint 1's *physical* transmission question — a necessary but not
sufficient input to the witness's actual percept, which additionally
requires the ambient regime, adaptation state, and C_thr(L) that Tier 2
has not yet attached." No numeric or geometric parameter needs to change.

## Re-tread check (RULED OUT registry / closed Live Threads)

No RULED OUT item (R1–R21) is re-proposed, and no genuinely CLOSED Live
Thread claim is re-litigated from my seat's own domain (T2 is not
re-derived or contested; T3's actual scope — temporal-contrast/switching,
constraint 3/4 joint, still unclosed per LOGBOOK — is not touched by this
static, single-snapshot instrument).

**But flagging one citation-accuracy defect, in the R4/R9/R20 family
(a recurrence of an error this program already corrected once, though a
single instance, not yet three):** exp-101's own Phase-5 VISION/Red-Team
finding explicitly corrected a mislabeling — the missing coherent-
downstream-intensity instrument (this cycle's own subject) was first
drafted as "T3," then corrected: *"T3 is specifically LOGBOOK's temporal-
contrast/switching-transient instrument (constraint 3/4 joint), an
unrelated construction; the reference is dropped"* (exp-101 NOTES.md,
Idealizations and Next item 1). exp-102's own Idealizations section
reintroduces exactly this dropped label: *"that conversion (Tier 2 / **the
T3 build**, exp-101's own corrected Next-item framing) is future work."*
exp-101's correction was to drop "T3" entirely, not to rename this
instrument's future conversion step "the T3 build" — the phrase "exp-101's
own corrected Next-item framing" is used here to justify a citation that
is the opposite of what that correction said. This risks a future cycle
building the Weber-contrast conversion under the mistaken impression it
must incorporate T3's own temporal-CSF/relaxation-pole machinery (exp-039,
still contested per T19), when the two are unrelated per exp-101's own
record. Recommend striking "the T3 build" from §Idealizations before Phase
3 freezes — a one-word-phrase fix, not a re-run.
