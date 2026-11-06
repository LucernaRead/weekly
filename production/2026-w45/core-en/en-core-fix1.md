# W45 English core VOL.2 — FIX ROUND 1 (builder fix log, 2026-10-26)

Fixes the 11 problems in the independent proof report
(`hidden_files/w45/en-core-independent-proof.md`). No other content was
changed: no new articles, no new facts, no lead/image/credit/abstract
changes. ABSTRACT.txt is untouched (no fix required a wording change there).
No git push, no Discord, no messages sent. This log does NOT self-certify
finalization — a fresh full independent proof round is still required.

Build code edited (only these files):
`hidden_files/weekly-report-w45-en-build/content12.py`,
`content34.py`, `content56.py`, `content7.py`, `content8.py`.

## The 11 fixes

1. **P2 article, "one weekend apart" (fact error).**
   Was: "Two autumn rituals, one weekend apart — and both are now just
   passed, not coming." Now: "Two autumn rituals, one weekend — and both
   are now just passed, not coming." (Oct 31 Halloween and the Nov 1
   clock change are hours apart on the same weekend.)

2. **P7 B1 comparatives + P8 Q123, "Madrid" vs stadiums (category error).**
   P7 was: "« Madrid is bigger than most stadiums. »" Now: "« The
   Bernabéu is bigger than most stadiums. »" P8 Q123 stem was: "Madrid is
   ___ than most stadiums." Now: "The Bernabéu is ___ than most
   stadiums." Key stays B (bigger); note stays "than → 比较级 bigger".
   (P4 Q54 already used the Bernabéu and is unchanged.)

3. **P7 B1 THE PAST SIMPLE, false claim about the issue's pages.**
   Was: "Sports and election pages are written in this tense — every
   result is past." Now: "Use it for what is already finished — the
   clocks that fell back on November 1, and the « as-if-finished »
   retellings on page 4. The November 3 election and the November 8
   games are still to come at press time, so their results are not past
   yet." No tense fact was changed; the P4 D-section's hypothetical
   framing ("比赛已结束的说法") is unchanged and is now consistent with
   the column. P7 B1 column ends y=1129 (bottom 1150) after the rewrite.

4. **P8 answers, P5 matching keys 76/77 swapped.**
   In `content56.py` P5 match_set, keys were ["c", "d", "a", "b"]; now
   ["c", "d", "b", "a"]. Printed keys now read "76. b · 77. a"
   (a result = the final numbers of a vote; to call = to announce the
   winner). Notes updated to match ("result=结果 b",
   "call=宣布胜者 a"). All other matching groups were already correct
   and are untouched.

5. **P8 answers, Q72/Q73 keys pluralized the article's singulars.**
   Q72 key "maps" → "map"; Q73 key "phones" → "phone", matching the P5
   article ("Every channel has its own map", "hands free for the
   phone"). Stems unchanged. Notes now read "与第 5 版原文一致，单数"
   (long enough that the P8 keys line prints just "72. map · 73. phone").

6. **P8 answer, Q53 key "begins" contradicted the article.**
   Key "begins" → "begin", matching the P4 article's twice-printed
   "the WTA Finals begin". Stem unchanged ("The WTA Finals ___ on
   Sunday."). Note now reads "与第 4 版原文一致，复数动词" (replacing
   the false "begin 三单 begins").

7. **P3 Q36 underdetermined (bigger/darker/louder all correct).**
   Stem was: "Godzilla is ___ than ever this time." Now: "Godzilla is
   bigger, darker, and ___ than ever this time." Only "louder"
   completes the article's triple, so the key (louder) is now uniquely
   correct. Article sentence unchanged.

8. **P8 answer, Q122 note copy-paste error ("比赛").**
   Note was "已发生的比赛用 fell"; now "已发生的事用 fell". Q122 is
   about clocks falling back, not a match. Key stays B (fell).

9. **P8 Q126 past tense for a future event, no framing.**
   Was: "The film ___ on Friday, November 6. A. opened · B. open ·
   C. opens" (key A opened, note "过去的事用过去式 opened") — wrong at
   a Nov 2 issue date. Now: "The film ___ on Friday, November 6.
   A. will open · B. will opened · C. will opens" (key A, note
   "将来时 will + 动词原形"). Only A is grammatical (will + base
   form), and the item is now temporally honest: the Nov 6 opening is
   future at press time. Level stays A2.

10. **P2 gloss, "daylight saving" never occurs in the P2 article.**
    The term was dropped from the P2 gloss (SOP §8 anchoring). Gloss
    now reads: "讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 ·
    trick or treat 不给糖就捣蛋。" All three remaining words occur in
    the P2 article. (The P1 search chart's "daylight saving" entry is a
    search term, not a gloss, and is untouched.)

11. **P8, 14 items had no printed level badge (SOP §4).**
    - Cloze 112–119: each options line now carries its badge, e.g.
      "112. [A2] A. Monday · B. Election Day · C. Halloween".
      Levels: 112 A2, 113 A2, 114 B1, 115 A2, 116 A2, 117 A2, 118 B1,
      119 B1 (A2 5 / B1 3).
    - Dialogue 145–149: a "Levels : 145–148 [A2] · 149 [B1]" line now
      follows the dialogue passage (A2 4 / B1 1). The range notation
      names every item's level explicitly.
    - Writing 150: the heading now reads "H · WRITING · 写作 [B1]"
      (B1 1).
    - Newly badged total: A2 9 / B1 5 / B2 0. Added to the previously
      labeled items (A2 51 / B1 64 / B2 21, per the independent report),
      the printed page now verifies the KIT split exactly:
      **A2 60 / B1 69 / B2 21**, total 150. No level in the registry was
      changed; the badges print the already-registered levels.

## Layout consequence of fix 11 (found and fixed in this round)

The first re-render overflowed the P8 battery: the battery flow ended
at y=1538 (bottom 1485) and the dialogue Levels line's second line was
struck through by the writing-strip rule and MODEL box top — a real
overlap, caught on the rendered PNG. Fix, all inside the P8 battery:
the dialogue Levels line was condensed to the single range line above,
and the 7 battery section-head gaps were tightened 13 → 8
(`bf.head(..., gap=8)` in `content8.py` only; no other page touched).
Final battery flow ends at y=1483 (bottom 1485); the Levels line is
visually clear of the rule and the MODEL box. P8 keys flow ends at
y=2535 (bottom 2545), above the footer. No other page's flow ends
changed beyond its own fix (P7 B1 1129/1150, P2 exercises 2532/2562).

## Re-render + gates (final render, all 8 pages)

- Full re-render: 8 SVG + 8 PNG (1950×2700) + `The-Lucerna-VOL2.pdf`
  (8 pages, 31,114,474 bytes) + `The-Lucerna-VOL2-web.pdf` (8 pages,
  3,710,257 bytes).
- Build warnings: **zero FLOW OVERFLOW / HEAD TOO WIDE** (full build
  log grepped; `/tmp/en45-build.log`).
- Exercises: **150** (numbering 1–150, per-page 10/17/18/18/18/18/12/39
  unchanged).
- Builder re-read: every changed page/answer re-read from the rendered
  output — P2 article + gloss, P3 Q36 + article triple, P7 B1 column,
  P8 battery + writing strip + full keys. All 11 fixes verified in
  print by SVG-text extraction (one apparent miss on Q122 was an
  extraction whitespace artifact: raw SVG contains
  "已发生的事用 fell" and zero occurrences of "比赛用 fell").
- Occlusion audit (`tools/occlusion_audit.py`, selftest first):
  selftest OK (all 6 planted classes fired, clean controls silent);
  edition run **0 flags** on the final render (output saved to
  `hidden_files/w45/en-core-fix1-occlusion.txt`).
- Nothing else changed: lead, images, credits, ABSTRACT.txt untouched;
  no git push, no Discord, no messages.

## Not done here (for the parent to order)

Fresh full independent proof round over the re-rendered issue. This
fix log does not certify finalization.
