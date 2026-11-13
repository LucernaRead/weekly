# pt — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-pt/` (slug `2026-w47-en-pt`)
- Print PDF: `The-Lucerna-VOL4-en-pt.pdf`, 29,345,286 bytes,
  SHA-256 `50484ca9c0ef23231977066164281455491180ef7843efc8d266805cdcc5ce0e`
- Web PDF: `The-Lucerna-VOL4-en-pt.web.pdf`, 2,381,728 bytes,
  SHA-256 `c150c65509fa722ef17d54f0c823878c7f958fcca6aaaae879e10c36e7430071`
- Gates: run exit 0, 0 overflow (all flows within bottom; P8-keys 2443/2560); occlusion 0 flags;
  p8 extract 60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  53,549 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round: (1) Q150 colon → dash via lit_overrides (caught before the first build —
  the W46 pt TM value uses a colon, the es Q150 trap); (2) P8 key size pre-set to 13.5/1.26
  (es/it lesson); (3) SCRATCH path fixed at sed time (it lesson) — no text.md failure.
- Notes kept: "SPORT · Desporto" is the shipped W46 pt head (content34.py:96), not a defect;
  Q13 TM note "Segunda volta a 1 de dezembro" (European form) coexists with fresh "segundo turno"
  (Q21) — two source literals, both correct, kept like the fr/es Q136/Q105 pattern.
- Box-title widths measured (23pt, CW 422.5): SENATE 408.4, HOW LONG 379.6, ODD SOCKS 397.2,
  SATURDAY 379.4, HAYMITCH 332.8, CALENDAR 305.0, ERROR CLINIC 230.4, READERS' CORNER 292.8,
  EXAMPLE LETTER 338.2, TOOLBOX 312.1 — all fit.
- Full record: the edition WEEKLY-KIT.md §5/§6.
