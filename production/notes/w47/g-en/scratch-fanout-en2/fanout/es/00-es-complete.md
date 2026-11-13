# es — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-es/` (slug `2026-w47-en-es`)
- Print PDF: `The-Lucerna-VOL4-en-es.pdf`, 29,330,745 bytes,
  SHA-256 `e668bc5f40f8c6e3ddc7a1d705cc39bcd004a615a2d9f2f62a0cad68304bc719`
- Web PDF: `The-Lucerna-VOL4-en-es.web.pdf`, 2,377,727 bytes,
  SHA-256 `a0a2f9d6d3035e4df1e05f5cf8c73c3a7fea1e35f1440b4b18e52ca85e68bcd8`
- Gates: run exit 0, 0 overflow (all 17 flows within bottom); occlusion 0 flags; p8 extract
  60/150, compare CLEAN (keydiff 137–140, 150, expected); freeze direct sha256 8/8;
  print/web text diff 0/0; P8 min font 13.5 pt; badges = core on all 8 pages; text.md
  53,837 bytes, 150/150 keys; 8 cards visually checked after the final render, zero issues.
- Fixes in this round (each → rebuild + re-render + full re-gate): (1) P1 COVER — word-of-week
  bridge wrapped to 3 lines into IN BRIEF (57%) → shortened to "Elecciones de medio mandato:
  toda la Cámara y un tercio del Senado."; (2) P8-keys FLOW OVERFLOW — answers block ran to
  y=2907 (bottom 2560), 13 occlusion flags, compare SHORT missing 150 → W46-extracted P8 key
  size 15.5/1.3 too big for W47 Spanish notes (87 answers lines vs fr 73) → key_size 13.5,
  key_lh 1.26 (fr/nl/de values), P8-keys now ends 2443/2560; (3) p8 extract still missed 150
  after the geometry fix — W46 TM Q150 key uses a colon ("Pregunta abierta: …") while core/fr/de
  use dash style, and p8.py detect_note needs " — " before the trailing paren note → lit_override
  to dash form; (4) text.md exporter SCRATCH path still pointed at fr/ (sed miss) → fixed to es/;
  (5) VM restart SIGTERM'd the gates run during webpdf — completed steps verified fresh from logs,
  only webpdf + diff + text.md re-run.
- Run-gate lesson: Flow's end_report prints "ended col N/N y=NNNN (bottom MMMM)" WITHOUT the
  word OVERFLOW — the old TOO WIDE|OVERFLOW grep missed the P8-keys overflow on the first es run.
  The run gate must check every flow's end y against its bottom. fr/de build.logs re-checked the
  same way: all flows within bottom.
- Tool note (NOT fixed — p8.py off-limits): FOOTER_RE `LUCERNA|...` doesn't match the mixed-case
  "The Lucerna" footer, so the footer leaks into the last answer segment (key 150) for every
  edition; masked when key 150 is dash-style, bites when paren-style. Full note in the edition
  WEEKLY-KIT.md §10.
- Full record: `scratch-fanout-en/es/00-es-complete.md` (and the edition WEEKLY-KIT.md §8).
- Standing lessons for the remaining 7: W46-extracted p8 sizes are per-language guesses — verify
  the P8-keys flow end y on the FIRST run (Spanish needed 13.5, not 15.5); Q150 must be dash-style
  in every edition (check the TM value, override via lit_overrides if it uses ":"); the P1
  word-of-week bridge must be 2 lines in every Romance language (shorten pre-emptively, fr/es
  pattern); sed-adapting fr's gates.sh/make_textmd_w47.py misses trailing "/fr" (no trailing slash)
  — grep for leftover "fr" after adapting.
