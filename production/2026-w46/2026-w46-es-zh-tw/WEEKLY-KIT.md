# WEEKLY-KIT · 2026-w46-es-zh-tw — La Lucerna, Spanish Weekly VOL.3, explanations in Traditional Chinese

Slug: `2026-w46-es-zh-tw`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Traditional Chinese (Taiwan/HK usage), written natively — NOT mechanically converted from Simplified.
Build dir: `hidden_files/weekly-report-w46-es-zh-tw-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_zhtw.py` + `t_zhtw2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-zh-tw.pdf` 4,935,582 B; web PDF `2026-w46-es-zh-tw.web.pdf` 850,025 B (<7 MB), text layer 44,612 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Face + furniture (W45 ES×ZH-TW KIT §2, VOL.1→VOL.3 only)

- TC face: 4 `svglib.py` changes (`_sc_index`→`_tc_index`, suffix `SC`→`TC`, `_IDX` call, family names `Noto Serif/Sans CJK SC`→`TC`) + docstring `重阳`→`重陽` (verified present in the W46 core `svglib.py`).
- Badge occupies the y=372 slot, 19.5pt sans bold BRICK: `西班牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本`.
- P1 name line: `西 班 牙 語 週 報 · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `CADA SEMANA EN ESPAÑOL · 每週一期 · 讀西班牙人正在讀的西班牙語`.
- Footer: `La Lucerna · 西班牙語週報 VOL.3 · 正文西班牙語 · 講解繁體中文`; page line `第 {n} 版 / 共 8 版` (unchanged from core).
- Band titles: VIDA · 生活 / CULTURA · 文化 / DEPORTE · 體育 / JUVENTUD · 青年 / A FONDO · 深讀 / LENGUA · 語言 (right subtitles in Traditional).
- Gloss prefix `譯注｜` (bslib4 gloss prefix pair + P1 explanation line, which also becomes `譯注｜`).
- `bridge()` → `expl()`; P8 header left `RESPUESTAS · 全部答案與簡析（第 1–8 版）` / right `每題附一句中文簡析 · 帶 ✓ 的為範本題` (already the core's strings); P8 separator `— 第 {pg} 版 —`.
- Explanation-layer quotation marks “” → 「」 (W43 ruling; W46 occurrences: P1 word note `「大罷工」`, P6 `「將要」`).
- Type names in Traditional: 單選 / 詞彙配對 / 判斷對錯 / 句型轉換 / 完形單選 / 翻譯 / 寫作 (完成句子 / 造句 unchanged in form); P8 check `== "寫作"`.
- Disclosure (Traditional): `編輯部說明：截至本期截稿，未收到真實讀者來信與第 8 版最佳作文，故本期登載編輯部示例信，承諾順延至 VOL.4。歡迎來信！`

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Traditional Chinese; all other keys byte-identical. `freeze.py diff` vs core SVGs: removed CJK = Simplified-only characters, added CJK = Traditional-only characters, shared characters stay; no Simplified-only character appears in the added set (verified programmatically: 0 hits against a Simplified-only probe set). Per-page CJK totals: core 180/295/155/176/238/80/412/964 → edition 216/307/169/188/252/92/424/985.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-zh-tw-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 44,914 B, identical to print text; <7 MB.
- Visual + text check: P1, P7 inspected — TC face renders throughout with no missing glyphs, Traditional forms verified in the `.text.md` export (0 Simplified-only characters; 讀/說/這/讓/議 present), top strip clear of the date line, letters box with disclosure inside, preview band clear of the footer rule. No P6/P8 size reductions were needed.

## 5. Fixups

None beyond the furniture/face transform. Core letters-box fix inherited via the build from the fixed core build.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py zh-tw t_zhtw` (copies the fixed core build, applies `t_zhtw.py` + `t_zhtw2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-zh-tw-diff.json`, `es-zh-tw-p8-compare.json`, `es-zh-tw-occlusion.json`, `es-zh-tw-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader zh-tw --week 2026-w46` (`--check` dry-run clean first). Mode cjk; `_D5_READER = "zh-tw"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 339, D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 0 all Newsreader; Noto Sans 0.
- run1 gates 18/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- `content12.py:49` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 5.3px)
- `content56.py:28` — P5 plan f.box tsize added 22 (was default 23) (margin 4.5px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 221 (run-split). G12 28 titles, 350 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 200 rows, slack 57.4px. G15a text-layer diff 0; text.md DIFF 78 lines, native verifier ADOPT (REWRAP 21, 0 UNEXPECTED). G15b CARRYOVER FAIL svg=5918 md=7969 (record-only, D27).
- D18 gap 103.0px; D37 N/A (no badge line in the box zone; strapline y=372 above box top 588); D39(4) P7 band bottom vs footer 2596: +4.6px (pre-existing, baseline identical).
- Old (baseline build) print `La-Lucerna-VOL3-es-zh-tw.pdf` 16,148,875 B SHA256 `2f448e203c6d8fecf2368c2468dfef8bf8886a98cf9c9b4a0bcc6d60e438697e`; web 1,230,209 B SHA256 `09a12a4bc35e275daab8cbdf2d2a9c85baa719e8939ce1fc86b75756fa9de14f`.
- New (run2) print `La-Lucerna-VOL3-es-zh-tw.pdf` 4,935,582 B SHA256 `bbddea054c40fabeb16a98fc4954cabb1f20206c6fc9b4823639b0b5de225775`; web `2026-w46-es-zh-tw.web.pdf` 850,025 B SHA256 `49d5ca8c851cc44bbfd96d0fb716fbd5fedb272a41f30d7b8b3b0e0d0623a2ec`; text.md 44,689 B SHA256 `08ddaf09ccda73c80be05db0e1327b8847cd13841bf63c7025f87d929577597e` (textexp output, `logs/2026-w46-es-zh-tw/2026-w46-es-zh-tw.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-zh-tw/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-zh-tw/g*-run2.log`, `logs/2026-w46-es-zh-tw/census-run2.json`, `logs/2026-w46-es-zh-tw/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-zh-tw-D5-REPORT.md`.
