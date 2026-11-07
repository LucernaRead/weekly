# W45 PT x IT — build log
Base: fresh copy of hidden_files/weekly-report-w45-pt-en-build, OUT/BASE repointed
weekly-report-w45-pt-en -> weekly-report-w45-pt-it, then transform.py (EN->IT, W43 PT x IT furniture).
Interpreter: tools/venv/bin/python (Python 3.12.3, PIL 13.0.0). Render: run.py then render.py, single process.
## Round 1 (2026-10-27, first render)
- run.py: TOTAL 150; levels A2 49 / B1 70 / B2 31; pages 10/18/18/18/18/18/12/38;
  types Completa la frase 61 / Scelta multipla 49 / Abbinamento lessicale 12 / Forma la frase 7 /
  Vero o falso 3 / Cloze 13 / Traduzione 4 / Scrivi 1; model 93 words. No FLOW OVERFLOW / HEAD TOO WIDE in output.
- render.py: print PDF 3,470,002 B; web PDF 3,476,487 B (< 10 MB).
- FIX applied before render (in transform.py, trailing FIX pairs): P2 gloss order-hazard
  (cemetery/to-check) + P5 bridge Careful-tail; see transform.py FIX comment.
## Round 2 (2026-10-27, FIX2)
- Cause: P7 quote row 4 IT lines at baseline 2441.67 inside VOL.3 preview box (top 2404) — audit COVER 2 + TEXTX 1, all one root cause.
- Fix (in transform.py FIX2): invitation 4 lines -> 3 lines; quote row step 104 -> 92. P7 col3 ends 1949.0 -> 1920.0.
- Result: only P7 SVG/card + 2 PDFs changed; P1-P6, P8 byte-identical to round 1. run.py: FLOW OVERFLOW 0, HEAD TOO WIDE 0; 150 / 49/70/31 / 93 words unchanged.
- Print PDF 3,469,993 B; web PDF 3,483,035 B (< 10 MB).
## Final gates (round-2 output, 2026-10-27)
- occlusion_audit (selftest OK): edition 0, core 0, NEW 0. Same-baseline scan 0; frame/right-edge scan 0 over inner 1910/outer 1922/page 1950.
- Border-straddle scan: 1 flag, pixel-adjudicated NON-defect (P3 calendar-box last line: glyph ink clears the border; coordinates byte-identical to core + EN; frozen core quirk, untouched).
- P6 chart labels (baseline-anchored ink, ascent 24/descent 6, anchor ls): 3 labels 0.00% covered (<30%); value texts 0 overlap.
- freeze diff --strict-cjk: added CJK 0; edition CJK 0 all pages; 14 non-CJK removed strings individually adjudicated (furniture / re-wrap fragments / colon-width notation), PT keys byte-identical.
- p8.py compare: CLEAN 150=150; keydiff 18 = 16 paren-branch extraction artifacts (true key token byte-identical) + 2 genuine re-aims (137, 138); 139/140 keys unchanged, 150 apparatus IT.
- gloss: 26 = core 26 (P2 6, P3 11, P5 5, P6 4); all terms in render.
- P7 quotes: 8 x 2 occurrences, tags (1,1,2,3,4,5,6,2) = core, each on tagged page, IT translations in P7.
- Readers' corner: PT example + PT disclosure verbatim + IT disclosure synonymous + explicit IT invitation (imperative + VOL.3 promise); zero fabrication.
- Images: only estudo.jpg, payload byte-identical to core; credit line on P1.
- Residue: CJK 0/page, Cyrillic/Hangul/kana 0, EN standalone words 0 (COMPLETE x2 = frozen PT heads), Note| 0, Page N of 0, 桥接 0.
- Visual: all 8 cards inspected, no overlap/truncation/frame-press; footers 8/8 VOL.2; badge/headers/footers complete.
- Core integrity re-verified post-build: 8/8 core SVG hashes match freeze baseline.
- NOT done (per task): no Discord, no main-chat cards/PDFs, no cron, no weekly-git touch, no core/W43 modification. No finalization claimed; independent proofread still required.
