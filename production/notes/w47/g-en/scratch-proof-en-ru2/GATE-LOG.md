# GATE-LOG — Lucerna Weekly 2026-W47 en-ru, proof2 (Q73 delta rebuild)

- **Edition:** en-ru, VOL.4
- **Date:** 2026-11-11
- **Probe:** `ls /dev/null` present; scratch dir real-write probe (`.probe`) OK.
  All intermediates in this scratch dir (`scratch-proof-en-ru2/`); production
  read-only — final SHAs re-verified after the round, unchanged.
  Tools: repo venv `tools/venv/bin/python` (Pillow 13.0.0, FreeType 2.14.3);
  repo `tools/` (occlusion_audit.py, p8.py, freeze.py, webpdf.py — webpdf only
  in scratch); fanout scripts copied from the delta scratch and re-run
  (check_s11.py, sweep_titles.py, sweep_svg_titles.py, verify_ed.py,
  keycheck.py repointed at this scratch's own p8-extract); canonical creambox
  from `hidden_files/w47/tools/creambox.py`; own scripts `gates/h-containment.py`
  (copy), `gates/verify_proof2.py` (D1 + 3-source + quotes/banned/orphan/D5/P8 font),
  `gates/keyfit2.py` (copy of the delta's stub re-run).

## Object SHAs (verified on disk before AND after the round)

| File | Size | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf` (print) | 29,241,520 B | `a42edc0e0bd0b7bbcac0163ad70639a1b400cb2cf6df4584db4f544f76c5d594` |
| `The-Lucerna-VOL4-en-ru.web.pdf` (web) | 2,452,562 B | `9e636240016e11c0b3738f9389d66f7b6f6729f1385c2cb0a379fe9f3f873a09` |
| `2026-w47-en-ru.text.md` | 62,381 B | `78c1b137e66571faf5bc51366f05edebfde152e0b30d717b926d1c92505794a4` |

## Gate results

### 0. Delta diff scope — PASS (exactly minimal)
- Registry diff (delta `registry-pre.json` vs `registry-new.json`): exactly 1
  entry, n=73 `speak` → `up`, note unchanged; 149/150 identical.
- text.md diff (delta `text-pre.md` vs shipped): exactly 1 line, 1151,
  `— speak (…)` → `— up (…)`; 62,384 → 62,381 B (−3).
- SVG diff (delta `svg-pre.sha256` vs shipped): only `p8-test.svg` changed
  (`9cd7c8da…` → `873e92fe…`); p1–p7 byte-identical to pre-delta; shipped SVGs
  match delta `svg-post.sha256` exactly.
- Core-en Q73 (read-only): `content56.py:49` key `up`, core registry Q73 `up`.

### 1. Full-text read — PASS (150/150 keys correct)
- text.md read completely (1,305 lines, 62,381 B).
- 150 keys hand-verified against stems: **150/150 correct**; 57 blank/rewrite
  items (keyfit) + 14 direct-reg items all fit their stems, incl. Q73 `up`
  ("Speak up: tell a teacher."). Matching blocks in definition order:
  Q24–27 b/c/a/d, Q38–41 b/a/d/c, Q56–59 b/c/d/a, Q74–77 d/a/b/c,
  Q141–144 b/c/d/a. Weekdays re-verified (`date -d`, America/Toronto):
  Nov 3 Tue, Nov 16 Mon, Nov 20 Fri, Nov 21 Sat, Nov 26 Thu, Nov 27 Fri.
  Arithmetic: 254+162+19=435 ✓; 254−218=36 ✓; MODEL text 82 words (80–100 ✓).
- Files: the text.md itself.

### 2. run.py (scratch copy rebuild) — PASS, rc=0
- Copy of the edition (content*.py, bslib4.py, svglib.py, run.py, render.py,
  dump_reg.py, registry.json, svg/, assets/) in `run-copy/`; `run.py` there:
  **rc=0**, `TOTAL exercises: 150`, `MODEL words: 82`, `ALL DONE`,
  OVERFLOW/TOO WIDE **0** occurrences. Fresh SVGs **8/8 byte-identical** to shipped.
- Note: the first copy attempt failed rc=1 (`FileNotFoundError:
  assets/lucerna-moth.svg` — my copy omitted `assets/`); fixed by copying
  `assets/`; the valid run above is the reported one.
- File: `gates/run-copy.log`, `gates/run-copy-sha.txt`.

### 3. render.py (scratch copy) — PASS, rc=0 + shipped SHA reproduced
- `render.py` in `run-copy/`: rc=0, 8 pages, 1462.5×2025 pt, cards + print PDF.
  Run 1: 29,241,520 B; run 2: 43,372,505 B; run 3: **29,241,520 B, SHA
  `a42edc0e…` = shipped print SHA byte-for-byte**. Run 2's text layer is
  byte-identical to shipped on all 8 pages (see §7) — font-embedding byte
  variance, not a content difference.
- Files: `gates/render-copy.log`, `gates/render-copy2.log`.

### 4. Occlusion audit — PASS, 0 flags
- `tools/occlusion_audit.py` on `svg/` (real audit, no `--selftest`) → rc=0,
  selftest OK (6 planted classes fired, clean controls silent), **0 flags**;
  `occlusion.json`: `flags: []`, `flag_count: 0`.
- Files: `gates/occlusion.json`, `gates/occlusion.log`.

### 5. P8 extract + compare — PASS (CLEAN, expected keydiff)
- Extract: edition 150/150 keys, noted 60/150; core 60/150 noted, same set.
  **Compare CLEAN**, missing=[] extra=[] uncertain=[],
  keydiff **[137, 138, 139, 140, 150]** (expected).
- P8-extracted key 73 = `up`; SVG answer segment `73. up · 74. d · 75. a ·`.
- Files: `gates/p8-extract.json/.log`, `gates/p8-extract-core.json/.log`,
  `gates/p8-compare.json/.log` (json body read, not just the log line).

### 6. Keycheck (registry vs P8 extract; registry vs core) — PASS
- `keycheck.py ru` rc=0: registry-vs-p8extract **exact 149/150, exc=[150],
  mismatch=[]**; registry-vs-core **145/150**, diff only the 5 reader-language
  keys (137–140, 150) — **Q73 now matches core**; noted set == core noted True;
  Q38–41 `['b','a','d','c']`; Q125 A, Q46 A, Q52 hosted, Q55 won; Q82/83/84 B C A;
  extract keys 150, missing none.
- File: `gates/keycheck.py`, `gates/keycheck.log`.

### 7. Print / web text identity — PASS (four-way)
- pdftotext: shipped print 54,726 chars, shipped web 54,726 chars; per-page
  byte-identical **8/8** (5556/6621/5756/6182/5175/6110/7379/11947 B);
  token-multiset diff **0/0**. Scratch re-rendered print and re-rendered web
  PDFs are also per-page byte-identical to the shipped pair (8/8 each,
  token-multiset 0/0).
- File: `gates/printweb.log`; per-page texts in `textcmp/`.

### 8. webpdf (scratch only) — PASS, rc=0
- `tools/webpdf.py` on a scratch copy of `svg/` → `webpdf/out.web.pdf`,
  rc=0, 8 pages, 1462.5×2025 pt, 2,452,554 B (shipped web 2,452,562 B —
  SHA/bytes float per run; text layer identical, §7). Shipped web PDF never
  overwritten (its SHA re-verified after the round).
- File: `gates/webpdf.log`.

### 9. Freeze — PASS, 8/8 both口径
- Standard (`--build` core-en, `--core-svg` core-en/svg, `--out freeze-core`):
  rc=0, **8/8 SVGs byte-identical** (p1 `a9a8deaf76e61cb2`, p2 `979747160de01d67`,
  p3 `efb83ce76688554b`, p4 `aa6f395e4932ef8b`, p5 `a6a515cd5f734d0d`,
  p6 `7692256484f26289`, p7 `da908af644651793`, p8 `1066c475da8afe7e`);
  core integrity: shipped core SVGs unchanged by the run.
- Supplement (`--build` edition, `--core-svg` edition/svg, `--out freeze-final`):
  rc=0, **8/8**, p8 `873e92fe31132a62` (the new delta p8).
- Files: `gates/freeze.log`, `gates/freeze-edition.log`, `freeze-core/`,
  `freeze-final/`.

### 10. Freeze diff — PASS
- `freeze.py diff --core-svg core-en/svg --edition-svg ed/svg` rc=0:
  per-page added CJK 2+1+1+1+1+1+1+1; **TOTAL added CJK 9, all U+3000**.
- Files: `gates/freeze-diff.json`, `gates/freeze-diff.log`.

### 11. check_s11.py (ru) — PASS
- ALL §1.1/P8 CHECKS PASS (badges A2 #5c6e30 / B1 #46581f / B2 #37402f;
  P8 Q113–120 [A2] tags; "Levels: 145–149 [A2]"; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　Письмо [B1]").
- File: `gates/check_s11.log`.

### 12. P8 min font — PASS
- PyMuPDF on print PDF (independent, `verify_proof2.py`): **P8 min 10.12 pt**
  ≥ 9.75 pt floor; P1 min 11.62 pt; all pages min ≥ 10.12 pt.
  Also inside `verify_ed.py` output (see §16).
- File: `gates/verify_proof2.log`.

### 13. D1 regression (triple measurement) — PASS
- SVG advance (`svglib.text_w`): new gloss 339.4 px, ends 1800.9,
  **margin +61.1 px** (box right 1862.0); old gloss re-measured 409.0 px, −8.5 px.
- Print-PDF ink (PyMuPDF): span x[1096.1, 1351.3] pt vs box right 1396.5 pt →
  **margin +45.2 pt**.
- Rendered pixels (150 dpi, `render/print-p-1.png`): rightmost ink 1349.3 pt →
  **margin +47.2 pt**.
- Old string `не точные цифры` 0× in `content12.py`, P1 SVG, map-ru.json value;
  new gloss in all three places (`content12.py:85`, `map-ru.json:228`, P1 SVG).
- Files: `gates/verify_proof2.log`, `gates/pixel.log`.

### 14. Quotes / apostrophes / banned words / orphans — PASS
- text.md U+201C 81 / U+201D 81, SVGs 82/82, U+2019 = 0, U+2018 = 0.
- Banned-word scan (SOP/proofread/cover/TODO/FIXME/XXX/lorem/占位/桥接) = 0.
- Orphan visual-line scan (group `<text>` by y, check line head/tail
  punctuation) = **0**.
- File: `gates/verify_proof2.log`.

### 15. Creambox (canonical scan) — PASS, 0 true-ink overflow
- Canonical `hidden_files/w47/tools/creambox.py` on `svg/*.svg` rc=0.
  Inside-only baseline clearances all positive (min +5.0 px, P2 AND YOU? box);
  P7 toolbox: 7 boxes, min inside clearance +47.7, min desc-clear +41.6.
  The P2 AND YOU? line's DESC=0.30 estimate (−1.0 px) is adjudicated by
  rendered pixels: lowest ink 1157.8 pt vs box bottom 1158.7 pt → **+0.9 pt
  inside** (see PROOF-NOTE §5).
- Files: `gates/creambox.py`, `gates/creambox.log`, `gates/pixel.log`.

### 16. Horizontal / vertical containment (PyMuPDF on print PDF) — PASS
- `gates/h-containment.py`: pages=8, size 1462.5×2025 pt;
  **H-SPILL total: 0**. V-SPILLs: 28, all +6.0/+13.7 next-block headings below
  boxes (design spacing, same pattern as proof1).
- File: `gates/h-containment.py`, `gates/h-containment.log`.

### 17. Boxtitle sweeps — PASS
- Source sweep (`sweep_titles.py ru`) rc=0: 12 titles measured, **0 over budget**
  (tightest: ODD SOCKS 398.3, margin +6.2; SATURDAY 328.9, +75.6).
- SVG sweep (`sweep_svg_titles.py ru`) rc=0: **18 titles checked, 0 overflows**
  (HAYMITCH'S GAMES 309.6, +94.9; SATURDAY, NOV 21 328.9, +75.6).
- Files: `gates/boxtitle.log`, `gates/boxtitle-svg.log`.

### 18. Edition verify (Q39/40, Ashes, SAY IT, P8 font, text.md) — PASS
- `verify_ed.py ru` rc=0, **VERIFY ALL PASS**: Q39 key a, Q40 key d,
  notes mentor=a / arena=d, Q46 key A, Q52 hosted, Q55 won, Q125 key A + 4–1,
  no stale Ashes phrasing, text.md 150 answers, "Arsenal are winning" present,
  no "Perth is winning" / "second week in Perth" / "Ashes begin", Ashes
  retrospective present, P8 min PDF font 10.12 pt, SVG zero real CJK.
- File: `gates/verify.log`.

### 19. Keyfit (stub re-run, key-into-stem) — PASS
- `keyfit2.py` rc=0: stub items 150 = registry 150, **key mismatches: NONE**;
  57 blank/rewrite items printed and hand-adjudicated (PROOF-NOTE §3),
  14 direct-reg items printed and hand-adjudicated.
- File: `gates/keyfit2.py`, `gates/keyfit.log`.

### 20. ABSTRACT / "next Sunday" / registry counts — PASS
- ABSTRACT.txt: 1 line, **659 chars**, Russian, 0 ASCII double quotes (full form).
- "next Sunday": 0 hits in content*.py, text.md, `tools/tables.py`.
- Registry: pages 10/17/18/18/18/18/12/39; levels A2 62 / B1 66 / B2 22.

### 21. D5 font inventory — RECORDED ONLY (not judged)
- 1,798 `<text>` elements; 26 distinct sizes (px): 13.5×75, 15.5×13, 16×1,
  17×34, 18×15, 18.5×2, 19×162, 19.5×71, 20×53, 20.5×166, 21×21, 21.5×183,
  22×167, 22.5×9, 23×147, 23.5×131, 24×465, 25×34, 26×2, 27×3, 28×11,
  32×11, 36×5, 46×15, 53×1, 196×1. Identical to proof1/fix1/delta records.
- File: `gates/verify_proof2.log`.

### 22. Visual checks — PASS (8/8 print + web P1/P8)
- Print pages P1–P8 rendered at 150 dpi (`render/print-p-*.png`) and viewed;
  web P1 + P8 rendered (`render/web-p1-1.png`, `render/web-p8-8.png`) and viewed —
  identical to print. Zoom crops viewed: `render/p8-p5top-zoom.png`
  (answers strip `72. rights · 73. up · 74. d · 75. a`), `render/p8-answers-zoom.png`.
  No overflow/overlap/truncation/footer-intrusion on any page. Footers
  "Страница N из 8" on all pages; masthead/edition line/badge correct.
- P1 D1 gloss in cream with clear right margin; P5 Q73 stem `Speak ___: tell
  a teacher.` in place; P8 cloze/dialogue/writing/model all legible.

## Standing rules honored
- No production writes; no insert.py / lint --write; no commit/push.
  Web PDF re-rendered only in scratch. Core-en read-only (hashes re-verified).
- Every number in PROOF-NOTE.md is reproducible from the files listed above.
