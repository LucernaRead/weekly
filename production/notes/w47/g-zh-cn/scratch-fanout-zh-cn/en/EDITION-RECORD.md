# EDITION-RECORD — 2026-w47-zh-cn-en (English explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Identity edition of
the proof3 (a) core. Builder handoff, NOT a finalisation claim:
independent proofreading is still owed by the parent line. No commit,
no push, no insert, no lint run by this builder.

## Identity proof (this edition IS the core, rebuilt)

| Check | Result |
|---|---|
| `run.py` | RC=0, TOTAL 150 (A2 56 / B1 69 / B2 25) |
| SVG vs core SVG | 8/8 byte-identical (cmp) |
| Print PDF vs core print PDF | byte-identical, SHA `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` |
| text.md vs core text.md | byte-identical, SHA `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` |
| Web PDF vs core web PDF | **differs by design** (see below) |
| `freeze.py diff --strict-cjk` | +0 / -0 strings all 8 pages, TOTAL added CJK 0, exit 0 |

Web PDF: `Lucerna-VOL4-EN-web.pdf`, 2,652,440 B, SHA-256
`0e339b6dc2a239856072b0bcf5ce298cf9da1eda060836cf09fefdd33cb25075`.
The core web PDF (2,632,446 B, SHA `6b7a12f5…`) was built with the
pre-patch `webpdf.py` and loses the italic face; this edition's web PDF
was rebuilt with the patched tool (commit 40963281, Newsreader-Italic
subset 24,604 B, 718 distinct chars). The +19,994 B is the italic fix.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-EN.pdf` (print) | 41,763,115 | `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` |
| `Lucerna-VOL4-EN-web.pdf` (web) | 2,652,440 | `0e339b6dc2a239856072b0bcf5ce298cf9da1eda060836cf09fefdd33cb25075` |
| `2026-w47-zh-cn-en.text.md` | 49,435 | `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` |
| `ABSTRACT.txt` | 552 | verbatim copy of the core abstract |

## Gates (final files)

`gates-zhcn.py` (`gates-en.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 384/384 … P8 1817/1817) |
| pdftotext_nonempty | print 43,681 B, web 43,681 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75) |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (`p8-extract-en.json`).
- `p8.py compare` core vs edition: **CLEAN**, missing=[], extra=[],
  uncertain=[], keydiff=[] (`p8compare-en.json`).

## Visual

P1 re-viewed as a render sanity check (SVGs byte-identical to the
proof3 (a) core): badge, headline, calendar, contents, photo, quiz,
footer all clean, zero defects. P2–P8 identical to the proof3 core
renders by construction (same SVG bytes, same renderer).

## Build

`transform-en.py` (identity copy of `core-zh-cn`; no translation table
applies — the core pairing is already zh-cn × en; W46 precedent: the
W46 zh-cn × en grid issue shipped with a text.md byte-identical to the
W46 core text.md). Then run → render → webpdf (patched) → export
(`export_ed.py en`). WEEKLY-KIT.md is the core KIT plus the “Fan-out
build” section appended at the end.

## Logs (this dir)

`run-en.log`, `render-en.log`, `webpdf-en.log`, `export-en.log`,
`gates-en.log`, `gates-en.json`, `freeze-diff-en.log`,
`freeze-diff-en.json`, `p8-extract-en.json`, `p8compare-en.json`.
