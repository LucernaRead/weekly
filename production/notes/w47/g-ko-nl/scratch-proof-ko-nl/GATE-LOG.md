# GATE-LOG — 2026-W47 ko-nl proof1 (independent)

Work dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-nl/`
Edition (read-only): `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-nl/`
Core (read-only): `~/workspace/weekly-git/production/2026-w47/core-ko/`
Scratch copies: `2026-w47-ko-nl/` (edition), `core-copy/` (core).
Interpreters: system `/usr/bin/python3` (Pillow 10.2.0 / FreeType 2.13.2) for
run.py / freeze / check_core / check_gloss / textmd / measurements;
`tools/venv/bin/python` (Pillow 13.0.0) only for render-adjacent work
(webpdf.py, PyMuPDF p8font, occlusion_audit.py). `TMPDIR` = work dir.
All logs below live in `logs/` (or the named path); page renders in `pages/`.

## 0. Probes + SHA verification (before gates)

- `ls /dev/null` present; `echo test | git -C ~/workspace/weekly-git
  hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc=0.
- Edition SHAs (before): print `2bf68445…77790a7b` (45,473,131 B), web
  `c4ad9cc6…4611eef5` (4,020,321 B), text.md `a51d9fa5…62a048b669d`
  (35,040 B) — all match the task. Core SHAs (before): print `53bf14ed…21a2f27`
  (46,232,227 B), web `9592945a…c6898c43bc7` (4,232,878 B), text.md
  `da1d3a32…f73468181a` (34,606 B) — all match the fan-out baseline.
- After all gates: all six SHAs re-measured, identical (see PROOF-NOTE.md).
- Scratch-copy SVG hashes match builder `sha-nl-run2.txt` exactly (path-prefix
  only difference in the diff output).

## 1. run.py — `logs/run-proof.log` — rc=0

`/usr/bin/python3 run.py` in the scratch copy. 0 FLOW OVERFLOW / HEAD TOO WIDE.
TOTAL 150 (A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38;
types invullen 48 / meerkeuze 52 / combineren 16 / omzetten 4 /
zinnen bouwen 8 / juist of onjuist 4 / gatentekst 13 / vertaling 4 /
schrijven 1; model chars 169). Flow ends (y/bottom/margin):
P1-headline 1814/1828/14, P1-weekend 2094/2290/196, P1-quiz 2491/2540/49,
**P2-feature 1531/1540/9**, P2-ex 2309/2580/271, P3-feature 1168/1560/392,
P3-ex 2113/2580/467, P4-feature 740/1180/440, P4-ex 2053/2580/527,
P5-feature 881/1560/679, P5-ex 2138/2580/442, P6-feature 515/1180/665,
P6-ex 2165/2580/415, P7-a2 1190/1560/370, P7-b1 1124/1560/436,
P7-b2 1151/1560/409, P7 teaser 2512.7 (limit 2580, margin 67.3),
P8-ex 550/1252/702, P8-keys 2487/2540/53.
Post-run SVGs byte-identical to shipped (`logs/svg-hashes-postrun.txt`).
P2 gloss #2 geometry: 2 lines at y=815.5 / 845.225; `geregistreerd worden`
count in shipped P2 SVG = 0.

## 2. freeze baseline — `logs/freeze-base.log`, `logs/freeze-base.json` — 8/8

`/usr/bin/python3 tools/freeze.py baseline --build <scratch>/2026-w47-ko-nl
--core-svg <scratch>/2026-w47-ko-nl/svg --out <scratch>/freeze-base`
→ `runtime: /usr/bin/python3 | Pillow 10.2.0 | FreeType 2.13.2`,
`baseline: 8/8 SVGs byte-identical (repointed files: none)`, per-file OK rows,
`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`.
Build-copy deleted after the pass (`freeze-base/svg` produced SVGs kept).
NOTE: the first attempt from a scratch dir named `edition` aborted rc=2
because no path component matched the ko-family pattern in `tools/freeze.py`
(`is_ko_family_path`); renaming the copy to its true slug `2026-w47-ko-nl`
made the guard recognise it. Guard behaviour itself is correct.

## 3. freeze diff — `logs/freeze-diff.log`, `logs/freeze-diff.json` — rc=0

`/usr/bin/python3 tools/freeze.py diff --core-svg <core-ko>/svg
--edition-svg <scratch>/2026-w47-ko-nl/svg` → TOTAL added CJK **7**
(p1 0, p2–p8 1 each, all U+3000). Per-page added/removed strings:
p1 +18/−17, p2 +37/−35, p3 +30/−28, p4 +23/−22, p5 +33/−31, p6 +18/−15,
p7 +41/−39, p8 +176/−167; CJK totals fall core→edition on every page
(footer separator only).

## 4. venv freeze control — `logs/freeze-venv-control.log` — rc=2 ABORT (expected)

`tools/venv/bin/python tools/freeze.py baseline …` → `ABORT: ko family builds
on system python3 (Pillow 10.x) — core-ko WEEKLY-KIT.md fix #15 … Got Pillow
13.0.0 …; re-run with /usr/bin/python3.` Recorded control, not a failure.

## 5. p8.py — `logs/p8-extract.log`, `logs/p8-nl.json`, `logs/p8-compare.log`, `logs/p8-compare.json`

- extract (edition P8 SVG, total 150): `noted set = 150 of 150 (parse: lines)`.
- compare (core-dir vs edition-dir, target ko, total 150): `status: CLEAN
  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`.
- Core P8 extract (`logs/p8-core-extract.log`, `logs/p8-core.json`): 150/150;
  core #150 key `'✓'` (== edition), core #137 `'11月22日是泡菜日。'`,
  core #138 `'三星时隔12年夺冠。'`.

## 6. occlusion audit — `logs/occlusion.log`, `logs/occlusion.json` — rc=0

`tools/venv/bin/python tools/occlusion_audit.py <scratch-edition> --core
<core-ko>` → `selftest OK: planted classes fired {BOXTITLE: 1, COVER: 1,
EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}; clean controls silent`;
`<edition>/svg: 0 flags; core: 0 flags; NEW vs core: 0`.

## 7. check_core / check_gloss — `logs/check-core-gloss.log`, scripts in `checks/` — rc=0

Fresh `run-checks.py` (same tool approach as the W46 precedent): patches ED /
BUILD paths and gloss prefix `译注` → `Uitleg — ` (strip `gstr[3:]` →
`gstr[len(prefix):]`). check_core: gloss fails 0, P7 phrases 8/8 verbatim
(incl. new phrase #7 with (1면)), orphan issues 0, dates correct
(D-3 Mon Nov 16, D-1 Wed Nov 18, D-day Thu Nov 19, Kimchi Day Sun Nov 22,
Sat Nov 28). check_gloss: gloss fails 0.

## 8. textmd re-export — `logs/textmd.log`, `logs/textmd-reexport.md` — byte-identical

`/usr/bin/python3 textmd.py . 2026-w47-ko-nl <out> "<title>"` in the scratch
copy → `wrote … pages: [1..8] items: 449`; `cmp` rc=0 vs shipped text.md;
re-export SHA `a51d9fa51f86c3ca3b10475ea9701326aef55bd1afb99f2c58d2b62a048b669d`
(35,040 B).

## 9. print/web text layers — `logs/print.txt`, `logs/web.txt` — byte-identical

`pdftotext -layout` on the shipped print and web PDFs: both 108,414 bytes,
`cmp` rc=0. Both 8 pages, 1462.5×2025 pts (pdfinfo).

## 10. web PDF re-render (scratch only) — `logs/webpdf-rerender.log`, `rerender/` — content identical

`tools/venv/bin/python tools/webpdf.py svg <scratch>/rerender/Lucerna-VOL4-KO-NL-web.pdf`
→ rc=0, wrote 4,020,321 bytes, 51,630 text bytes. Extracted text layer
(`logs/web-rerender.txt`) byte-identical to the shipped web PDF's layer
(108,414 B). Re-render SHA `e5fba1b9…` differs from shipped `c4ad9cc6…`
(expected: fontTools wall-clock). Shipped web PDF untouched (SHA re-verified).

## 11. P8 min font — `logs/p8font.log` — 9.975pt PASS

Calibrated rule (builder `p8font.py`, bbox top ≥ 976.5): 172 region spans,
min 9.975pt, at-min 167, PASS ≥ 9.75pt. (My first origin-based count gave 176
spans with the same min/at-min; the calibrated bbox rule reproduces the
builder's 172 exactly.)

## 12. boxtitle — `logs/boxtitle.log` — 8/8

Fresh `measure.py boxtitle` (AST `box()` literals + P7 col-3 p.text titles,
measured with the edition's own `svglib.text_w`, system python3; budget
386.5px): 304.5 / 267.3 / 350.3 / 335.4 / 258.7 / 269.4 / 291.5 / 262.6 px —
all OK; widest 350.3px `김장 장보기 목록　Boodschappen`.

## 13. sweeps — `logs/sweeps.log` — all 0

Fresh `measure.py sweeps`: U+2019=0, U+201C=0, U+201D=0, true-Han-in-`<text>`=0
across 8 SVGs + text.md. (First run used the broad range `[\u2e80-\u9fff]`
and counted 177 CJK-punctuation hits: U+3000 ×124, 「」 ×25 each, 〜 ×3 —
legitimate Korean punctuation/space; the script was corrected to the true-Han
range `[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]` and re-run → 0.)

## 14. §1.1 grep audit — `logs/style11.log` — OK

Fresh `style11.py` (core vs edition, per page): paper/VOL.4/middot identical
(p1: 1/2/13, p2: 1/1/21, p3: 1/1/20, p4: 4/1/14, p5: 1/1/20, p6: 4/1/31,
p7: 1/1/17, p8: 1/1/38); hanzi 0 on the edition side; U+2019 0; P7 VOL.5
core 3 → ed 2 by design; unknown colours identical to core (p1 set only).

## 15. census — `logs/census.log` — 0 missing

`census.py <text.md> <edition-dir>`: ex/match items total 166, missing 0;
D6 missing 0.

## 16. creambox + orphan sweep — `logs/cream-orphan.log` — OK

Fresh `cream_orphan.py`: 55 cream rects (excl. page bg), 0 empty; orphan
punctuation 0.

## 17. D5 font census (record only) — no log file (commands in PROOF-NOTE.md)

`pdffonts` print PDF: only `*NotoSansCJKkr-*`, `*NotoSerifCJKkr-*`,
`UnifrakturMaguntia` — **Noto Sans CJK SC: 0**. Web PDF: only
`LucernaNotoSansCJKKR-*` — **SC: 0**. PyMuPDF span census (print PDF):
Latin-only spans 486 (Sans Regular 157, Sans Bold 212, Serif Regular 104,
Serif Bold 12, UnifrakturMaguntia 1). SVG font-family counts:
Noto Serif CJK KR 882, Noto Sans CJK KR 620, UnifrakturMaguntia 1.

## 18. "next Sunday" — 0 hits

`grep -rn "next Sunday"` + case-insensitive `sunday` over core-ko,
ko-nl, `tools/tables.py`: no hits. Dutch text uses `zondag 22 nov.`.

## 19. 150-item three-source verification — `logs/three-source.log` — BAD 0/150

Fresh `three_source.py` (REG via AST from core + edition `content*.py`;
keys from `logs/p8-nl.json`; cross-check vs builder EDITION-RECORD table):
147 fully OK; #137/#138 KEY-REAIM(nl-expected); #150
KEY-STEM-TRANSLATED(expected) + SVG-150-checkmark; record cross-check BAD 0/150.
All 150 rows hand-read (core-note vs nl-note) — see PROOF-NOTE.md.

## 20. Visual read — `pages/p-1.png` … `pages/p-8.png` (100dpi, pdftoppm)

All 8 pages read, zero issues (see PROOF-NOTE.md for per-page notes).

## 21. text.md self-read + old-version check

- Read head + P7 + P8 sections of the shipped text.md (917 lines); sweeps:
  no TODO/XXX/lorem/placeholder, no stray English furniture, no double spaces.
  Frame line 761, disclosure line 767. Single `1면` phrase citation (line 781)
  identical to core (line 787) — textmd dedupe behaviour, inherited.
- No prior ko-nl edition: `git log --all -- "*ko-nl*"` shows only W46/W45/W43
  ko bundles; no `2026-w47-ko-nl` under `issues/2026-w47/` — no old version
  to compare against.
- ABSTRACT.txt (339 B): Dutch, consistent with the issue (verified by reading).

## 22. Cleanup

`freeze-base/build-copy` deleted after the freeze pass; `freeze-venv-control/`
never created (abort before any output). No commit, no push, no insert.py,
no lint --write. Production dir untouched (SHAs re-verified after all gates).
