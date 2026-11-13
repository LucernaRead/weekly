# ru — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-ru/` (slug `2026-w47-en-ru`)
- Print PDF: `The-Lucerna-VOL4-en-ru.pdf`, 29,241,566 bytes,
  SHA-256 `788cd0c08ec9b72fd52c8a65b4aadacb05e27980369295d7df0b726eb82efd70`
- Web PDF: `The-Lucerna-VOL4-en-ru.web.pdf`, 2,417,491 bytes,
  SHA-256 `da80486218d001cc6dc09e4107391cf81b15d1dde7f5c3b6d8e0aeb5f2ffe77a`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2460/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  61,835 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round (all pre-emptive, caught before the first build): (1) Q150 colon → dash via
  lit_overrides (es/pt lesson — W46 ru TM value uses a colon); (2) P8 key size pre-set to
  13.5/1.26 (es/it lesson); (3) SENATE title pre-shortened to "Сенат" (nl lesson); (4) SCRATCH
  path verified at sed time (it/nl lesson). No rebuild was needed after the first gates.
- Note kept: "H　WRITING　Письмо [B1]" is the shipped W46 ru head (content8.py:131) — kept as-is.
- Full record: the edition WEEKLY-KIT.md §5/§6.
