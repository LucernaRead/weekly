# GATE-LOG — W47 ru-zh-tw proof2 (Build 2)
## Independent re-proof gate log. All commands run with TMPDIR=$SCR/tmp, tools/venv/bin/python unless noted.
## $SCR = ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-zh-tw1/
## Edition D = ~/workspace/weekly-git/production/2026-w47/2026-w47-ru-zh-tw/ ; Core C = ~/workspace/weekly-git/production/2026-w47/core-ru/

### 0. Probe + identity
- 2026-11-11 19:39 UTC: `git -C ~/workspace/weekly-git hash-object -w /dev/null` → e69de29bb2d1d6434b8b29ae775ad8c2e48c5391, RC=0. Scratch real-file write `$SCR/probe.txt` OK. Disk: 58G avail (/dev/mapper/rv, 91G used of 150G).
- Disk-measured (sha256sum + stat): print 24,784,766 B / 2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4; web 3,995,314 B / 991b22ab217eaf925aee4c444e71b9c423c5dfa09b6471a8de8459637671d52d; text.md 60,887 B / bc9c425f1c887d4ad70b7f2369671b3d36979b33d40713967977a4febd4a62c4; ABSTRACT.txt 348 B. All match task brief exactly.
- Production SVG snapshot `$SCR/prod-svg-before.sha` (8 hashes, p1 828a6c0e… – p8 5a8154e2…). Re-verified at close: 8/8 OK.
- Close re-verification (2026-11-11 ~20:20 UTC): print/web/text SHAs unchanged; ABSTRACT.txt SHA 602879243337f313a588b59ba3e01da7e2aa6ddb227e1037d27c972f4fc06fde. `git status` shows the edition dir untracked (`?? production/2026-w47/2026-w47-ru-zh-tw/`, pre-insertion state, not mine — I wrote nothing under weekly-git).

### 1. run.py (in $SCR/build-copy/, rsync copy of edition excl. *.pdf, cards/, __pycache__)
- RC=0, TOTAL **150**, 0 FLOW OVERFLOW / HEAD TOO WIDE. Log: `$SCR/run.log`.
- By level A2 50 / B1 76 / B2 24; by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38; by type 完成句子 54 / 單選 55 / 詞彙配對 20 / 造句 12 / 句型轉換 4 / 翻譯 4 / 寫作 1; model words 97.
- Rebuilt SVGs byte-identical to production 8/8 (`$SCR/rebuilt-svg.sha`, diff clean).

### 2. p8.py
- extract RC=0, **150/150** (`$SCR/p8-extract.json`, `$SCR/p8-extract.log`).
- compare RC=0, **CLEAN**, missing=[], extra=0, keydiff **[137, 138, 139, 140]** (`$SCR/p8-compare.json`, `$SCR/p8-compare.log`).
- Keys 137–140 (Traditional, comma form): 137 `11月17日星期二，大學生節。`, 138 `包裹要追蹤、領取並檢查。`, 139 `星期二俄羅斯隊對陣委內瑞拉隊。`, 140 `祝大家大學生節快樂！` — verified identical in text.md stems, text.md answers, and p8-extract.

### 3. freeze.py
- Baseline RC=0, **8/8 SVGs byte-identical**, core SVGs unchanged by the run (`$SCR/freeze-base.log`, `$SCR/freeze/` = core baseline rebuild).
- Diff RC=0 (`$SCR/freeze-diff.json`, `$SCR/freeze-diff.log`): per-page added/removed strings P1 +19/−19, P2 +24/−24, P3 +15/−15, P4 +15/−15, P5 +14/−14, P6 +20/−20, P7 +29/−30, P8 +171/−171 (count-sums; removed distinct per page 19, 23, 14, 15, 13, 17, 30, 122).
- Independent audit (`$SCR/freeze-audit3.txt`): removed **distinct union 231, count-sum 308**; per-page-distinct sum **253**; added CJK total 743.
- **Counting-definition note (NOT a defect):** KIT §3/§9 "removed distinct 253" is the sum of per-page distinct counts. The global union is 231. Both are correct under their definitions; re-fanout's own `gates.json` records `freeze_removed_distinct: 253`, `freeze_removed_total: 308`, and its `freeze-diff.json` decomposes identically. Record both numbers here for transparency.
- Cyrillic-bearing removed strings: exactly one — P8 `можно` ×1 (Q46 note localization, known legal).
- D1 strings (`УЧЕБНЫЕ`, `ДАННЫЕ`, `Три уровня`, `Большой тест`, `Это учебный`) appear in NEITHER removed nor added lists (per-word SVG splitting explains this; D1 verified separately in §9 below).

### 4. occlusion_audit.py
- Command: `tools/occlusion_audit.py $D --core $C/svg --json $SCR/occlusion.json` → RC=1 (flags present), **42 TEXTX, 0 LINEX** (`$SCR/occlusion.json`, `$SCR/occlusion.log`). Core also 42.
- NEW vs core = **3**: (1) P7 `'\u3000語言'` vs `ЯЗЫК` 3.8px; (2) P8 `'\u3000練習與答案'` vs `ОТВЕТЫ` 8.0px; (3) P8 `'\u3000參考答案 — 按版面分頁排列，找到題號即可'` vs `ОТВЕТЫ` 4.5px. (Not proof1's 4 — the P6 chart-head NEW disappeared when D1 restored the disclaimer.)
- Adjudication: **42/42 CLEAR**, 0 unadjudicated. Method + per-flag numbers in `$SCR/adjudication.json` (final, real-font); 6× crops `$SCR/crops/occ-01..42-*.png`; montages `$SCR/montage-1.png`–`montage-6.png` (all 42 viewed).
- Final correct-font PIL ink gaps: −0.25 to +9.45px (28 flags ≥ 0; 14 flags −0.05…−0.25px sub-pixel punctuation-kerning touch, no visible contact). Per-row median raster gaps 0.0–7.67px. NEW flags: +8.50 / +6.05 / +3.25px.
- Mechanism (verified): `occlusion_audit.py resolve_font` maps Noto Serif/Sans → NotoSansCJK SC subfont (index 2), inflating Cyrillic widths ~3% → fabricates the 3.0–8.0px "overlaps". U+3000-leading title elements get `getbbox` left=0, widening the box ~46px leftward (the 3 NEW flags).
- Discarded method iterations (do not reuse): adjudicate.py 16/26 (tool-box-edge scan, wrong direction), adjudicate2.py 10/32 (band included adjacent descenders), adjudicate4.py (crashed at flag 33), adjudicate5.py 29/13 (OR-column profile fabricates continuity — #10 per-row debug proved real gap ≥2.5px at every row 2404–2419), adjudicate6.py (ink_box4 divided getbbox by font size S instead of supersample factor 4 → nonsense 55–216px gaps). Newsreader→NotoSerif substitution understates Newsreader advances ~18% on underscores (phantom −7.15px P8 blank overlap); real Newsreader font gives −0.10…+0.10px for all 13 P8 blank pairs. Logs: `$SCR/adjudication*.log`, `$SCR/pilgap-realfont*.log`, `$SCR/pilgap-final.log`.

### 5. check_core.py (run from $SCR/build-copy, read-only)
- RC=0, golden BAD 0, gloss fails 0, orphans 5 (P7: `。`×3, `”».`×1, `：`×1), same-baseline collision 1 (P1 y1712 `чёрная`). Matches KIT §3/§5. Log: `$SCR/check_core.log`.

### 6. creambox.py (canonical, all 8 SVGs)
- RC=0, 32 boxes; **96 BELOW-WINDOW lines: +28.0 ×25, +32.0 ×41, +34.0 ×4, +37.0 ×25, +44.0 ×1** — exactly KIT §9; log byte-identical to re-fanout's creambox.log (md5 9f941e6a196afdeadac8ddc2a749104c). Log: `$SCR/creambox.log`.
- Only negative inside-only value: P2 `А ВЫ?` box, last baseline 1125.6, clearance +4.4, desc-clear **−1.6** (same as proof1). Pixel re-verification: lowest text ink SVG y=1127.33 vs box bottom 1130.0 → clearance **+2.67px**, no overflow (`$SCR/box-verify.log`). P7-TOOLBOX: min inside clearance +11.9, min desc-clear +5.9.

### 7. Print vs web text layer (PyMuPDF)
- 8 pages each; page rect 1462.5×2025 pt both; **25,845 non-whitespace chars each, multiset identical overall AND per page** (P1 2864, P2 2934, P3 2401, P4 3009, P5 2619, P6 2413, P7 3089, P8 6516); whitespace-normalized line diff opcodes = **0** (1584 lines each). Log: `$SCR/textcompare.log`.
- `pdftotext` byte counts: web 56,095 (KIT §2 ✓), print 56,095.

### 8. P8 min font + s11_check.py
- P8 min font **9.75pt** exactly at SOP §1.1 floor (1268 spans; min spans at y 1083–1411pt); other pages min P1/P2/P4/P5/P7 11.62pt, P3/P6 12.75pt. P8 span sizes include 10.35pt ×255 (KIT §5 "P8 stem 10.35pt" ✓).
- `s11_check.py $D` → RC=0: PASS web < 7MB 3995314; PASS web text > 0; PASS print 8 pages; PASS P8 min font ≥ 9.75pt 9.75; **FAILURES: none**. Log: `$SCR/s11.log`.

### 9. Focus items D1 / D2 / D6 (independent)
- D1: 4/4 PRESENT — (1) P6 `УЧЕБНЫЕ ДАННЫЕ` (text.md L459; SVG p6 y=1552); (2) P6 disclaimer `Это учебный опрос редакции для упражнений — не настоящая статистика.` (content56.py:159; SVG p6 y=1582; web P6 text layer; absent from text.md by design); (3) P7 `Три уровня, три темы` (text.md L504; content7.py:12; SVG p7 y=168; punctuation-aware join required — `,` is a separate element); (4) P8 `Большой тест недели + все ответы` (text.md L596; content8.py:12). Evidence: `$SCR/d1-d2.log`, `d1-debug.log`, `d1-d2b.log`, `d1-final.log`, `crop-p6-chart-6x.png`.
- D2: kicker y=372, 16px (content12.py:18). PIL gaps [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6] min 5.9 (independently recomputed, exactly RECORD's values — cross-check only). Pixel column scan on delivered print PDF at 6×: [8.5, 4.0, 9.67, 6.5, 7.67, 7.17, 9.33, 8.5, 9.5] min **4.0px**. Crop `$SCR/crop-p1-kicker-6x.png` viewed — spacing even. Both methods ≥4px (core KIT §7.2.9: 4–5px = non-defect). PASS.
- D6: Q20 `желании` (content12.py:257; text.md L173 + L694; p8 key `желании`); Q25 `День студента` (content12.py:276; text.md L187; p8 key `b`; P2 SVG ×4, D-option y=2234.3). Evidence: `$SCR/d6.log`.

### 10. text.md full mechanical recheck (838 lines)
- 150 stems contiguous 1–150, all with keys; 150 answers contiguous 1–150 (from L666 `### ОТВЕТЫ` heading); stem-vs-answer key mismatches **0**; p8-extract-vs-answers mismatches **1** (Q150 only: p8 key `✓` vs answer `（開放題，範文如下）` — checked-mark convention for the open writing task, CLEAN vs core, not a defect).
- Per-page counts match run.py exactly: 10/18/18/18/18/18/12/38. Levels A2 50 / B1 76 / B2 24 (incl. 20 match-set items: headers L186 A2 25–28, L260 B1 39–42, L333 B1 57–60, L410 B1 75–78, L645 B2 141–144). Types 完成句子 54 / 單選 55 / 詞彙配對 20 / 造句 12 / 句型轉換 4 / 翻譯 4 / 寫作 1.
- Core diff (non-CJK): 8 opcodes, all expected (VOL.4 header, 2 gloss localizations, Q46 note, 2 writing-note localizations, Q150 answer form).
- Simplified sweep: 0 simplified-only chars; `干` ×1 only inside `塔什干`.
- Old→new diff vs backup-old: exactly 6 changed lines (L173, L187, L459, L504, L596, L694; 60,815 → 60,887 B).
- Logs: `$SCR/textmd-check.log` (first attempt, regex missed B1 levels — my bug, fixed), `$SCR/textmd-check2.log`, `$SCR/textmd-check3.log` (final).

### 11. Box-title raster retest (all 8 pages)
- Correct-font PIL ink vs container edges (≥28px elements): narrowest true clearance = `Lucerna` wordmark **+32.45px** vs 1862 (all pages).
- Three apparent negatives were full-width rows misassigned to the 961 edge, verified structurally: P1 y=330 masthead tags, P1 y=682 lead headline, P6 y=1392 chart day labels 16–22.
- Whole-page 8× raster scan (delivered print PDF): rightmost ink 1861.8–1863.3 (page edge 1950: +86.7px min), leftmost 88.0, bottom 2625.2 (page 2700: +74.8px). P1 1863.3 = masthead date line `…2026 ГОДА` (y=92); core P1 measures exactly the same 1863.33 — house-identical.
- Logs: `$SCR/boxtitle.log`, `boxtitle-verify.log`, `boxtitle-verify2.log`, `rightedge.log`, `rightedge2.log`, `rightedge3.log`, `p1-dateright-8x.png`.

### 12. Apparent word joins (full-page 130dpi views) — resolved
- `От редакцииLucerna` / `криминальнаядрама` / `возвращается20` / `Календарнаядата`: space elements exist between the words; true ink gaps +3.90 / +5.75 / +5.80px. Downscale antialiasing artifacts, not defects. Logs: `$SCR/wordgap.log`, `$SCR/byline-gap.log`.

### 13. Visual review
- `$SCR/png/p1.png`–`p8.png` (130dpi, delivered print PDF) all read; P6 chart 6× crop and P1 kicker 6× crop viewed. 0 defects. P8 Morozko image + Bilibin caption present on render; 1 image in print P8 (xref 337, bbox 1079.6–1396.5 × 1555.6–1950.5pt).
- KIT §4 spot values verified: P1 head `數字看本輪` inkR 864.6 ≈ x865; P6 gloss single `譯注｜`; P7 B2 bridge bare; P7 word gloss 1 line.

### 14. KIT verification summary
- §1 SHA/bytes: all match disk (re-verified at close). §2: 72 font xrefs ✓; 56,095 text bytes ✓ (pdftotext). §3: all gate values match this log. §4: 8/8 pages read, 0 defects. §5: all non-defect claims verified (orphans 5, P1 y1712 collision, 塔什干, P8 stem 10.35pt). §6: spot checks pass. §9: D1/D2/D6, 6-line diff, creambox 96, Morozko — all verified. **KIT document defects: 0.**
- One counting-definition note (§3): "removed distinct 253" = per-page-distinct sum; global union 231; count-sum 308. Not a defect.

### 15. Defects
**Zero confirmed defects. Conclusion (a).**
Observation (non-defect): Q150 p8 key `✓` vs answer text — open writing task convention, CLEAN vs core.
