# W47 KO core — §1.1 re-layout self-check summary (runs 5–6, 2026-11-10)

## Final artifacts (run 6)
- Print PDF Lucerna-VOL4.pdf: 46,231,469 bytes, SHA-256 1201420b304cb470cb8b9e041ad8a0deb53747a009ccd872540df6c1ad9ce02a
- Web PDF Lucerna-VOL4-web.pdf: 4,461,792 bytes, SHA-256 25c77db8d163da243019e7bf25c4c571422447b640091d539c07f04867d65136
- text.md 2026-w47-ko-zh-cn.text.md: 26,014 bytes, 333 items, SHA-256 81ebd0a392266c0762df33fb73a8ce1b9bf1d8f6912891e107d74e9341e6e8c0
- SVG freeze hashes: p1 9bd57ce3f8237dab, p2 48d74902dab44a68, p3 7cf045c86e5c8b30,
  p4 dfd5f01713281915, p5 c11c700c68676061, p6 f144ef88362147b0,
  p7 2bc4281496bc2ee3, p8 5b504b8a121e0f00

## §1.1 nine items — measured on run-6 SVG (all verified)
1. Paper #fbfaf6 on all 8 pages; old #f7f1e2 0.
2. No #2c2822 anywhere; strips/bands/P6 header #37402f (36 uses).
3. No #b3a06a anywhere; GOLD/BRICK/DARK literals 0.
4. No #a4553a anywhere; kicker + B2 badges use olive/cloth.
5. No frame rects (x=28 / x=40: 0); single 2px olive masthead rule.
6. Badges: 138 rects rx=2.7, A2 #5c6e30 (45), B1 #46581f, B2 #37402f.
7. SVG U+00B7 291 -> 174 (content-internal gloss/options/credits only, per W46 FR
   precedent); U+3000 0 -> 117 (all furniture).
8. No spaced Chinese numbers in SVG/text.md ("第N版", "11月16日" forms);
   side colours all on palette (#f0eee5 boxes, #d8d2c4 lines — verified by grep,
   zero old values remain).
9. Drop cap "1" 170px olive on P1; 77 fill-in underlines, 1.47px (=1.1pt) INK
   #302c28 (6/9/9/9/13/4/6/21 per page); masthead 196px (147pt); headline 56px (42pt).

## Mechanical gates (run 6)
- Build: exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150;
  levels A2 51 / B1 72 / B2 27; pages 10/18/18/18/18/18/12/38; model 169 chars.
  P1-headline flow 1814/1828; all other flow ends identical to run 4.
- occlusion_audit.py: 0 flags (selftest OK).
- p8.py extract --total 150: 150/150.
- freeze.py baseline: 8/8 byte-identical.
- check_core.py: gloss fails 0, P7 phrases 8/8 verbatim, orphan issues 0,
  dates correct (11-16 Mon D-3, 11-18 Wed D-1, 11-19 Thu D-day, 11-22 Sun Kimchi Day).
- check_gloss.py: 10 misses, log byte-identical to run 4 (adjudicated debt c).
- P8 answer font (PyMuPDF, region y>=976.5pt): min 9.975pt, 158 spans — same as run 4.
- Print/web pdftotext: 49,378 bytes each, byte-identical.

## Content preserved (freeze diff run 4 -> run 6, all strings classified)
- Added/removed strings only in intended classes: 77 blanks ___ -> NBSP underlines,
  101 mid-dot furniture -> 99 full-width-space + 2 wrapped option tails,
  8 old foot strings -> 8 new foot strings ("第N版／共8版"), P1 re-wrap (drop cap),
  P4 glossline de-parenthesised (-2 chars), de-spaced Chinese numbers (P7 quotes,
  P8 key notes 137/138/139/140/150), ex 41/53/71/146/149 gaining a 2nd line from
  wider blanks. P1 char multiset delta: exactly one "1" relocated into the drop cap.
- Round-1 fixes intact: 웨더아이 5 in print text layer (P3 prose, P3 box, ex 40 key 11,
  match b, P8 key 124 B); 공단 0 in source/SVG/text.md/both PDFs.
- KIT: IMG_2874 -> IMG 2919; Output files -> run 6; fixes log #9/#10/#11;
  Round 5/6 self-check records; "Deliberately retained" note (text.md ___,
  comment dots, 48.75pt margins, no moth).

## New finding during this round (fixed in run 6)
- Run 5 self-check found 1 orphan: P4 C glossline parenthetical tail stranded on
  its own line (exposed by ex 53 wrapping to 2 lines after the blank widening;
  run 4 passed the same scan only by line-interleaving luck). Fixed by removing
  the parentheses (meaning unchanged); run-6 self-check: zero issues.

## Files in this scratch dir (scratch-ko-fix2)
apply_fix.py, build-run5.log, build-run6.log, render-run5.log, render-run6.log,
webpdf-run5.log, webpdf-run6.log, occlusion-run5.log, occlusion-run6.log,
p8-extract-run5.log/.json, p8-extract-run6.log/.json, check-core-run5.log,
check-core-run6.log, check-gloss-run6.log, freeze-run6.log, freeze-diff-run6.log/.json,
svg-text-run6.txt, summary-run6.md (this file).
