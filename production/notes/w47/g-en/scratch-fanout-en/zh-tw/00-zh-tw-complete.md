# zh-tw — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-zh-tw/` (slug `2026-w47-en-zh-tw`)
- Print PDF: `The-Lucerna-VOL4-en-zh-tw.pdf`, 38,152,082 bytes,
  SHA-256 `d2e919473d70463a00b3be10129bfecbd3c1a9137b0ae4ab0cf8ca2bdea78e07`
- Web PDF: `The-Lucerna-VOL4-en-zh-tw.web.pdf`, 2,927,283 bytes,
  SHA-256 `df41f1fc1a6786b839c63fdd53ecec1fdecba57a19ddf7c274a679762f421545`
- Gates: run exit 0, 0 overflow after the P2 fix (all flows within bottom; P8-keys 2137/2560;
  P2-feature 1528/1540, 12pt spare, visually clean; P2-ex 2532/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff [137, 138, 139, 150] — 140 is script-identical,
  expected); freeze direct sha256 8/8; print/web text diff 0/0; P8 min font 13.5 pt; badges =
  core on all 8 pages; text.md 50,505 bytes, 150/150 keys; 8 cards visually checked after the
  final render, zero issues.
- OpenCC s2t gate (this edition only): registry.json + text.md convert to themselves with
  0 differences — zero Simplified characters in the deliverables.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P2-ex FLOW OVERFLOW
  (y=2946/2560, same as ko's first run) — W46 TM B bridge wrapped to 2 lines; fixed via
  lit_overrides → 1-line bridge; (2) Simplified 布 in the Q2/Q95 registry notes
  ("宣布競選結果", a W46 TM conversion gap) — fixed via lit_overrides → "宣佈競選結果";
  OpenCC re-check clean. Process slip: the first override edit replaced the lit_overrides
  dict instead of merging, dropping the B-bridge fix — the re-run overflowed again (2946) and
  caught it; both overrides verified present in map-zh-tw.json before the final apply.
- zh-tw mechanics: 216 misses (11 more than the other languages — 8 script-identical lit +
  3 script-identical type/instr, all needing identity mappings because the TM stores differing
  pairs only); calendar/numbers box follow the W46 zh-tw English+Traditional-gloss pattern.
- Full record: the edition WEEKLY-KIT.md §5/§10.
