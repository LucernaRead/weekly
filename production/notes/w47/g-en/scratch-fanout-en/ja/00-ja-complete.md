# ja — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-ja/` (slug `2026-w47-en-ja`)
- Print PDF: `The-Lucerna-VOL4-en-ja.pdf`, 41,509,526 bytes,
  SHA-256 `5cfb282caa800c343435639ee1b54a325f7d902e4fa6a3c53f2bc4e1374aa63c`
- Web PDF: `The-Lucerna-VOL4-en-ja.web.pdf`, 2,843,624 bytes,
  SHA-256 `f20c1affd5a53ab23dd8619715dfa86f72c3c6322c0faf5f8daf4c0b4cc7eabb`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2205/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  52,982 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Print PDF 41.5 MB is the CJK-font-embedding scale (core-en print PDF is 41.4 MB); web PDF
  2.84 MB < 7 MB. Freeze added CJK 2,096 chars = the Japanese layer itself (hiragana-heavy);
  0 leftover Simplified Chinese strings verified in the SVGs.
- Fix in this round (→ rebuild + re-render + full re-gate): P4 gloss used full-width colons
  ("a Test：…") while every other gloss uses "=" — fixed to "=". Anchor typo also caught by
  build_map at the start (Japanese 勝/輪 in the anchor instead of source 胜/轮) — anchors must be
  copied character-for-character from the source literal.
- Full record: the edition WEEKLY-KIT.md §5/§6.
