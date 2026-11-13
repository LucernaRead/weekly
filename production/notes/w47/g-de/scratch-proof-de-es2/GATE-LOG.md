# GATE-LOG — de-es proof2 (rebuild 5, 2026-11-11)

Proofer independent of fix1. No source modified, no rebuild, no commit, no push.
Probe: `git hash-object -w` RC=0 (9daeafb9…); probe file written in this dir.
All outputs in this dir unless noted. Edition dir:
`~/workspace/weekly-git/production/2026-w47/2026-w47-de-es/`.

## SHA verification (2026-11-11 ~09:35 UTC)

- print `Die-Lucerna-VOL4-de-es.pdf` 10,968,798 B sha256
  `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e` MATCH
- web `Die-Lucerna-VOL4-de-es-web.pdf` 1,601,888 B sha256
  `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e` MATCH
- text `2026-w47-de-es.text.md` 50,124 B sha256
  `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` MATCH
  (byte-identical to rebuild 4, as fix1 claimed)

## D1 re-verification (creambox + visual)

- `creambox.py` (copied from scratch-proof-de-es1) on `svg/p7-sprache.svg`
  (`creambox-p7.log`): toolbox bottom 803.5 / last baseline 783.9 /
  clearance **+19.6**; LESERBRIEFE y=820 bottom 1372.0 / last 1361.6 / +10.4;
  NOCH EIN WORT y=1388 bottom **1538.0** / last 1495.1 / +42.9.
  The three −35.0 rows are the matcher's known BEISPIELE false positives.
- Full-edition sweep (`creambox-all.log`, all 8 SVGs, 32 rows): only other
  negative is P1 `DAS WORT DER WOCHE` −24.0 (known FP, following section
  head inside the +45 window; P1 visual clean).
- 300 dpi toolbox zoom: `p7-toolbox-print-300.png` viewed — `fraglich`
  descender has clean cream below it; `p7-toolbox-web-300.png` byte-identical
  (sha256 `8a72ebeb…`). Bottom crop `p7-toolbox-bottom-crop.png` viewed.
- `content7.py:76` read-only: pad 110 with the fix1 comment.

## Gates re-run by proofer

- `tools/occlusion_audit.py svg --json occlusion.json` (NO --selftest):
  RC=0, selftest OK (6 planted classes fired, clean controls silent),
  **0 flags** (`occlusion.json` flag_count=0). Log: `occlusion.log`.
- `tools/p8.py extract --p8 svg/p8-uebungen.svg --total 150 --json p8extract.json`:
  RC=0, noted **150/150** (`p8extract.log/json`).
- `tools/p8.py compare --core-p8 ../core-de/svg/p8-uebungen.svg --edition-p8 svg/p8-uebungen.svg --total 150 --json p8compare.json`:
  RC=0, status **CLEAN**, missing=[] extra_count=0 keydiff=[137, 138, 139, 150]
  (`p8compare.log/json`).
- `tools/freeze.py diff --core-svg ../core-de/svg --edition-svg svg --json freeze.json`:
  RC=0, TOTAL added CJK **7** (all U+3000, 1 per page P2–P8, 0 on P1)
  (`freeze.log/json`).
- `freeze_direct.py es <ED> <S>`:
  RC=0, source PASS, rendered **8/8**, frozen 147/163/195/166/173/175/150/186,
  sha `083e2a2a/689045ad/fc88f676/df1bebf7/86fa4421/2bbe05f9/b7aa0771/57e118e7`
  — identical to rebuild 4 on all 8 pages (`freeze-direct.log/json`).
- `keycheck.py es <ED> <S>` (needs p8extract.json in S):
  RC=0, **149/150 exact**; only Q150 extractor truncation
  (`Tarea libre` vs full key) (`keycheck.log`, `keycheck-150.json`).
- `boxtitle.py es` (from scratch-fanout-de): RC=0, **7/7 fit** — 356.5 /
  387.6 / 227.0 / 341.4 / 358.8 / 248.2 / 380.7, budget 400.5 (`boxtitle.log`).
- `d2scan-de-es.py` (this dir, OUT repointed to this dir): 58 print-abutting
  pairs, **0 web gaps > 0.5 pt** (`d2scan.log`, `d2-scan.json`).
- Chips `rx="2.7"` occurrences: 10/15/18/15/18/18/12/35 = **141**.
- P8 min span (PyMuPDF): **9.94 pt** (351 spans) ≥ 9.75 pt floor.
- §1.1 grep: zero old-palette hexes (no `#c9a227/#d4af37/#8b4513/#a0522d/
  #111111/#1a1a1a/#000000`); non-palette hexes only inside the P1 moth logo.
- pdftotext default: print 51,011 B / web 51,011 B, word multiset identical
  (8,088 words). `-raw` normalised: exactly identical, 49,812 B each
  (`print.txt/web.txt/print-raw.txt/web-raw.txt`).
- Pixel diff print-vs-web @100 dpi: mean |Δ| P1 0.368, P2 0.000, P3 0.121,
  P4 0.213, P5 0.260, P6 0.000, P7 0.096, P8 0.069.
- Web PDF: 8 pages, real text layer, < 7 MB (1,601,888 B).

## Content checks (scripts, in this dir)

- `counts.py` / `counts2.py`: MUSTER token count **84**; answer-key tokens
  cover 1–150 (none missing; P8 option-list duplicates expected).
- Q34: new stem 1× / old stem 0× in content34.py, .text.md, svg/p3-kultur.svg,
  print text layer, web text layer.
- Bent quotes: text.md U+201C 33 / U+201D 0 / U+2019 0 / U+201E 33;
  SVGs U+201C 33 / U+201D 0 / U+2019 0 / U+201E 33.
- P7 golden sentences: 8/8 present verbatim in body text (script check).
- Weekdays: `date` (Europe/Berlin) verified all 18 dates named in text.
- P4 MD9 goal sum: 30 (9 rows). P6 poll: 44+33+23=100, 44+33=77.
- ABSTRACT.txt: 426 B, one line, 0 ASCII double quotes.

## Visual proofread

- Print PDF @100 dpi, all 8 pages viewed (`p1-print.png` … `p8-print.png`):
  zero findings. P7 toolbox fix confirmed visually at 300 dpi.
- Web: P7 toolbox zoom byte-identical to print; full-page pixel diff above.

## Files in this scratch dir

PROOF-NOTE.md, GATE-LOG.md, probe.txt, counts.py, counts2.py,
creambox.py, creambox-p7.log, creambox-all.log, d2scan-de-es.py,
d2-scan.json, d2scan.log, occlusion.json/log, p8extract.json/log,
p8compare.json/log, freeze.json/log, freeze-direct.json/log,
keycheck.log, keycheck-150.json, boxtitle.log, gates-part1.log,
gates-part2.log, print.txt, web.txt, print-raw.txt, web-raw.txt,
p1–p8-print.png, p7-toolbox-print-300.png, p7-toolbox-web-300.png,
p7-toolbox-bottom-crop.png.
