# PHASE 2 — CRITIQUE (THERMODYNAMICS) · Panel Iteration 63 · exp-086

*Fresh context, blind to all other seats' current-cycle critiques. Read
PANEL.md, LOGBOOK.md (RULED OUT R1–R11, LIVE THREADS T28 sub-thread
Iterations 46–62 in full), exp-085's `phase5_redteam_audit.md`, and the
proposal under review in full. Independently re-derived every load-bearing
numeric claim below from the committed `derivation_results.json` and
`phase4_derivation.py` source — not restated from the proposal's own prose
(R4 discipline).*

## Independent re-derivation performed

I re-loaded exp-085's committed `derivation_results.json` directly and
recomputed the proposal's own headline arithmetic from primitives rather
than trusting its prose:

- **The θc=45° subtlety (§4 prediction 1) is real and correctly derived.**
  The as-filed record shows `θc=45.0`: `p_local_reported_at_39=4.0`
  (exact boundary), `p_local_corrected=4.396201…°` — confirmed one of
  exactly 6 exact-boundary pins (`θc∈{45,59,61,63,71,73}`), and confirmed
  it sits *below* the audit's own `>6°` proxy filter purely because the
  wrong (narrowest) stage's value happened to correct to 4.40°, not 6+°.
  Recomputing the exclusion sets by hand: audit's proxy (15 windows >6°)
  → 22/37=0.595; proposal's flag-based criterion (15 ∪ {θc=45}) → 21/37=
  0.568. Both figures reproduce exactly.
- **Prediction (4)'s premise checks out.** `grep -rl
  "free_period_with_widening"` across `experiments/069-076/` returns zero
  files — the function's absence from that span, load-bearing for the
  "no new firings expected" prediction, is genuinely true, not asserted.
- **The "Timing persistence" row is imprecise.** `free_period_with_
  widening` itself contains no `time.time()` call and returns no
  `elapsed_s` field — per-stage timing is *not* "already computed…
  currently discarded" as claimed; instrumenting it is new (trivial)
  code, not mere persistence. Separately, per-null `elapsed_s` is **not**
  uniformly discarded today: it is already written into JSON for Method
  A's null and for all 10 currently-sampled Method C sub-windows (e.g.
  θc=45.0's `circular_shift_null.elapsed_s=3.546`). Minor, non-load-
  bearing — flagged for precision, not for blocking.

## Steel-man (≤150 words)

The proposal earns real credit under this seat's own reproduction
discipline: its one genuinely new claim — that `θc=45°` is a confirmed
boundary-pin whose *coincidentally* sub-6° corrected value defeats the
audit's own proxy filter — is not asserted, it is independently
re-derivable from the exact committed JSON, and I just re-derived it
myself, digit for digit (21/37=0.568 vs. 22/37=0.595). That is precisely
the kind of falsifiable, source-checkable prediction R4/G0-e house
discipline exists to reward, staked honestly on "only the third decimal
is uncertain" rather than smoothed over. Scope discipline is otherwise
clean: zero new FDTD, `FastEval` re-verified bit-identical before reuse,
`free_period_with_widening_quiet` correctly fenced out as a different
function feeding already-gated null distributions rather than silently
touched.

## Sharpest attack (≤150 words)

**The proposal contains zero mentions — literally, `grep` confirms —
of "interception," "Poynting," "energy," or "thermo" anywhere.** The
joint EM/THERMO energy-interception cross-check has now been named at
Iteration 59, tripwired at Iteration 60, and **fired Checkpoint criterion
4 at Iteration 61 (exp-084)** for the *exact same* failure: appearing
"nowhere in exp-084's Phase 1 or any of its five Phase-2 critiques."
exp-085 escaped only because its NOTES.md at least named the item as
deferred-with-reason ("structurally exempt, no scene"); this proposal's
Phase-1 document does not even do that — the identical silent-omission
shape that already fired once in this sub-thread, one cycle prior. A
scene-less instrument-repair cycle cannot run the check, but Red Team's
own §7 item 4 explicitly required either running it or "stat[ing] the
exemption explicitly a third time" — and this document states neither.

## Verdict: support-with-changes

## Flip-to-support parameter

Add one sentence to §5 (Idealizations) or §3 stating explicitly that the
joint EM/THERMO energy-interception cross-check is exempt this cycle
because it has no article-loaded FDTD scene to check against (matching
exp-084/085's own established language) — cheap, non-load-bearing to the
actual repair, but the single addition that forecloses a repeat of
Iteration 61's Checkpoint-4 firing on an identical documentation gap.
