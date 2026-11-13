# it — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-it/` (slug `2026-w47-en-it`)
- Print PDF: `The-Lucerna-VOL4-en-it.pdf`, 29,326,709 bytes,
  SHA-256 `195e155228e63515d3133a32cebbbee71c3dccf973387d4c1c2f614670e3da26`
- Web PDF: `The-Lucerna-VOL4-en-it.web.pdf`, 2,372,517 bytes,
  SHA-256 `995339d48612cc9344a5213e38026a9cda9a1de910efb268308fa9e877064a46`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2443/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  53,373 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P1 bridge size patch
  missed — my #189 used "Nota — " but apply.py's patch looks for the W46 it bridge label
  "Spiegazione | " → bridge would render at default 20.5pt instead of 19.5 → fixed #189 to
  the W46 it convention "Spiegazione | a midterm = …"; (2) text.md exporter SCRATCH path still
  pointed at es/ (same trailing-slash sed trap as es) → fixed, re-ran RC=0; (3) P8 key size
  pre-set to 13.5/1.26 on the es lesson (15.5/1.3 overflows for long-note Romance languages).
- Standing lesson for nl/ru/ja/ko/zh-tw: the P1-bridge label need NOT equal the gloss prefix —
  check the W46 P1-bridge label per language (it "Spiegazione | ", de "Erklärung | ");
  verify the bridge-size patch applied (no WARN in apply output) on the first build.
- Full record: the edition WEEKLY-KIT.md §5/§8.
