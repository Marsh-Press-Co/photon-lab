# Phase 2 Critique — VISION SCIENCE (blind, fresh context)

## 1. Steel-man

Yes — this proposal clears the minimum scope and budget I pinned in `phase5_review_vision.md` (exp-067, §2 item #1) almost exactly. I required "at minimum the ±35° pair at 600nm and 750nm... STEPS≥2800... ceiling on the order of 30-45 calls." Tier0 here is precisely that (8 calls, ±35°×{600,750}nm×{C40,C80}@2800), and the total (42 planned/45 ceiling) sits exactly inside my stated range. It correctly reuses `_article_one` and `_settle_one`, and it correctly keeps GATE_HARD=0.001 scoped to empty-scene rows (P-068-1/5) while scoring the article row's PASS/MARGINAL bucket against C_THR_LAB=0.005 with the [0.5,2.0]× convention (P-068-2) — exactly the M3-mandated separation. It also includes the mandatory harness-continuity gate I'd want before trusting any new number.

## 2. Sharpest attack

The proposal's own §6 disclosure duty is undercounted by one cycle, and this is checkable against text written before this proposal existed. LOGBOOK.md (Iteration-44 close, Red Team's ranked queue) states plainly: Block ARTICLE's leg is "**now four consecutive cycles** without being a cycle's primary FDTD work... EM should... explicitly disclose a **fifth**-consecutive-deferral line" if it fails. PLAN.md says the same ("now FOUR consecutive cycles (Iterations 42→43→44)"). My own `phase5_review_vision.md` pins the exact same duty: a Tier0 failure "must be disclosed as a **fifth** deferral." EM's Phase-1 §6 instead says "3 consecutive iterations so far (42,43,44)" and that a Tier0 failure "must be disclosed as a **4th** consecutive miss" — off by one against the program's own already-published count, understating exactly the kind of streak-length fact this program's Checkpoint 4 has fired on before.

## 3. Verdict

**support-with-changes**

## 4. Parameter change that would flip my verdict to plain support

Correct §6's count before the run: "3 consecutive iterations so far" → "4 consecutive cycles so far (42,43,44 — LOGBOOK.md's own Iteration-44 close)"; and the Tier0-failure disclosure line → "must be disclosed as a **fifth** consecutive miss," matching LOGBOOK.md/PLAN.md/my own pinned duty verbatim. The FDTD design, budget, and threshold arithmetic need no change.
