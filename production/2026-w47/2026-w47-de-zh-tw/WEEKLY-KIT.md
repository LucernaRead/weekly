# WEEKLY-KIT — 2026-W47 · German target, Traditional-Chinese reader

- Edition: `2026-w47-de-zh-tw` — German target text, Traditional-Chinese explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln**
- Status: complete (fix1), all gates green, visual proofread P7 zero findings
  (2026-11-11); fix1 only restores the P7 toolbox pad 90 → 110 (see §8) — no text
  changed anywhere (text.md byte-identical, freeze_direct 8/8 shas identical).
- **D5 font rebuild applied 2026-11-12 (all gates green — see §3b/§9)**

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in the registry.
Chips: 141 total (P1 10, P2 15, P3 18, P4 15, P5 18, P6 18, P7 12, P8 35; P8 A2 22 / B1 13 / B2 0).

## §2 Deliverables (fix-de-round3 rebuild, 2026-11-13; reproof fix round 2 rebuild superseded)

- Print PDF: `Die-Lucerna-VOL4-de-zh-tw.pdf` — 11835999 B, sha256 `8597094b9ad2093862d3e6fe4f5a03b62c62207a3d5fde31853465e184a1398a`
- Web PDF: `Die-Lucerna-VOL4-de-zh-tw-web.pdf` — 1936175 B, sha256 `dd26b2ac11a5cd0ab35b07d6f39b8ac555b84cc0a687bc57d99f959369075122` (50,048 text bytes; < 7 MB)
- Text export: `2026-w47-de-zh-tw.text.md` — 49330 B (42,333 chars, 591 entries, 150 exercises), sha256 `6865f9d835f17082f84bf500fc07211942d01a7c5520c87c298ceac74939ea6b` (changed — see the §12 fix-de-minor1 and §13 fix-de-round3 entries below)
- ABSTRACT.txt: 294 B, Traditional Chinese, one line, no ASCII double quotes
- 8 SVGs in `svg/`; all gates green (D5 round, see §3b)

Print PDF is 11.8 MB (was 23.0 MB): D5 moved the Latin explanation layer out of the CJK faces, so far fewer CJK glyph subsets are embedded. No gate checks print size; web PDF is the size-checked one.
- ABSTRACT.txt: 294 B, Traditional Chinese, one line, no ASCII double quotes
- 8 SVGs in `svg/`; all gates green via `build_edition.py` (copied to the fix1 scratch dir with its `tr_zh-tw.py` / `export_text_lang.py` / stubs; run 09:41–09:46 UTC — see §8)

Print PDF is 23.0 MB: genuine Traditional CJK font subsets (many unique hanzi). No gate checks print size; web PDF is the size-checked one.

**Web PDF tool version (recorded, not a gate):** built with the working-tree
`tools/webpdf.py` as of the run — a file under ACTIVE concurrent edit by another agent
(the italic/weight fix). At 09:04 UTC, pre-run, `git diff tools/webpdf.py` showed only
the fc_match change (`:style=Bold` → `:weight=200`/`:weight=100`, 5 insertions,
1 deletion); the file was saved again at 09:10:13 UTC, during the webpdf step itself,
and the diff has since grown (90 insertions / 17 deletions at 09:14). The exact
in-memory version cannot be pinned beyond the build log: it embedded the
`LucernaNewsreader-Bold` subset (21,596 B), consistent with the `:weight=200` query
resolving to SemiBold. This edition's web PDF was generated with that version. The other
four rebuild-B editions (nl/ru/ja/ko) were built earlier the same morning; ko (08:42) shows
the same Bold subset, nl/ru/ja do not (see the fan-out report's 重建-B section for the
full split). Webpdf output also carries a cosmetic fontTools warning on the
Newsreader-Bold subset (fsSelection/macStyle bold bits) — exit 0, text layer verified
identical (see §3). The other shared tools used in this run were also working-tree
modified but STABLE across the whole wave (freeze.py / occlusion_audit.py / p8.py
mtimes Nov 10 22:59 / Nov 11 05:01 / Nov 10 21:37 — all before the rebuild wave, so all
five B editions used the same versions).

## §3 Gates (rebuild-B build 1)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (B baton, `zh-tw/build.log` 08:54)
- render.py exit 0; print PDF SHA verified before and after the webpdf run (B baton, `zh-tw/render.log` 08:55)
- probe + precheck 0 FAIL + boxtitle 7/7 + transform RC=0 + measure 24/24 PASS (B baton,
  `zh-tw-precheck.log`, `zh-tw-measure-rblog.log`, `zh-tw-transform-stdout.log`)
- webpdf exit 0 (09:10:35 UTC), web PDF < 7 MB
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150] (expected: the three translate-to-Traditional-Chinese items + Q150)
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 1,328 — the Traditional-Chinese explanation layer itself (see §5; lower than ja/ko because many Traditional hanzi coincide with the core's Simplified ones and do not count as added)
- freeze_direct rendered 8/8 (frozen 151/164/206/166/182/176/170/191; sha8 54c9b51e / 2db0dd83 / ad74f280 / df1bebf7 / b42a8c3d / babfe417 / 9dc31873 / 961dd98a); source level shows exactly 4 unaccounted strings, all the documented TC font switch (see §5)
- print/web text layer identical (default word multiset: print 49,905 B / web 49,905 B; -raw normalised: 48,777 B both)
- P8 min font 9.94pt (≥ 9.75pt floor)
- U+2019 full scan over 8 SVGs = 0 (re-scanned on rebuild-B SVGs)
- Box titles: 7/7 fit (max 363.6px, budget 400.5px; `boxtitle.py zh-tw`, RC 0)
- keycheck 149/150: Q150 PREFIX only (extracted '開放任務' vs REG key '開放任務 — 依寫作框中的要點進行') — same as all Latin editions; the Q150 dash survived the wrap here (unlike ja)
- Visual proofread: P3 + P8 rendered from the NEW web PDF at 100 dpi and viewed
  (`/tmp/zhtw-rb-proof/pg-3.png`, `pg-8.png`), zero findings — Q34 new stem on one clean
  line, Q34 key `34. Weihnachtsmarkt（聖誕市集）` clean in the P8 answers. The other 6 pages
  are byte-identical in text to build 1 (print.txt diff vs build 1 = exactly one line, the
  Q34 stem; web.txt diff = the same stem + a poppler block-grouping line break on the P6
  chart labels, word multiset identical), so build 1's 8/8 visual proofread (zero findings)
  carries for them.

## §3b Gates (D5 font rebuild round, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-zh-tw/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader zh-tw` (mode cjk) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`, adapted for cjk: `_D5_READER == "cjk"`, Latin sans → news — latin/cjk share routing per CJK-DECISION §1). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-zh-tw/baseline/` (SVGs + sources, fix1 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`74faeb9d…`), but the pre-D5 web PDF on disk was sha `b4b82c51…`, NOT the KIT's fix1 record `352ead22…` — the fix1 web PDF had been rebuilt without a KIT sync (same class as de-en/de-fr/de-it/de-nl/de-pt/de-ru/de-ja). The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **463 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run2): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild-B.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 466 = D5 run-splitting).
- `tools/spill_sweep.py`: 32 boxes, 97 candidates, **0 SPILL**, 97 OBSERVE.
- `tools/boxtitle_check.py`: 48 titles, 320 body lines, **0 DEFECT**, 0 OBSERVE, 1 marginal (P7 `　工具箱` +1.0px, within tolerance — the core has the same +1.0 marginal, pre-existing, not a D5 regression; real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-zh-tw`). Coverage note: the fixed P1 box title is at tsize=21, below the tool's 22pt detection floor — it is verified instead by the creambox audit (0 defects across all 32 boxes) and by direct ink measurement (392.8px against a 404.5px budget, 11.7px spare).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=518, median 1.015, bold 1.051 / regular 0.992; P8 lines 232→233, footer slack 34.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **49,821 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 48,759 bytes, identical.
## §4 Language

- Reader: Traditional Chinese (繁體中文), independent edition — never converted from Simplified Chinese.
- ED_SPACING 7.0, NOTE_WRAP "full", KEYS_HALF=false.
- TYPEMAP: 完成句子→填空 / 单选→選擇題 / 句型转换→改寫 / 词汇配对→配對 / 判断对错→是非題 / 完形填空→完形填空 / 造句→造句 / 对话补全→對話補全 / 翻译→翻譯 / 写作→寫作
- Gloss prefix: `註 — ` · Page line: `第 {n} 頁／共 {total} 頁` · P8SEP: `— 第 {pg} 頁 —`
- Edition line: `德文週刊　VOL.4　德甲回歸　寧靜的一週`
- Footer: `Die Lucerna　德文週刊 VOL.4　德文文本　繁體中文解說`
- Chart labels: ['足球', '市集', '寧靜的日子']
- Place names: 科隆, 美因茲, 紐倫堡, 弗萊堡, 萊比錫, 漢堡, 門興, 不來梅, 沙爾克, 斯圖加特, 薩克森, 巴伐利亞, 荷蘭
- ABSTRACT.txt (Traditional Chinese): "Die Lucerna 德文週刊 VOL.4：德甲回歸（拜仁主場迎戰科隆）、對荷蘭的歐國聯關鍵戰、懺悔祈禱日與追思主日、科隆聖誕市集開市、11 月 3–8 日歐戰與德甲賽果；德文文本、繁體中文解說，A2–B2 程度，本週話題 150 道練習。"

## §5 Freeze / CJK handling (read before claiming --strict-cjk)

- `freeze.py diff --strict-cjk` does NOT pass for this edition, by design: the reader-language explanation layer itself adds CJK (1,328 chars, Traditional hanzi). The en-family precedent (en-ja: 2,092) is to record the total and audit the added characters instead.
- Residual audit run on build 1: 2,978 CJK characters in the 8 SVGs; exactly 1 not in tr_zh-tw.py's values — '／' U+FF0F, the pageline separator from PAGELINE_ZH_TW ('第 {n} 頁／共 {total} 頁'), legitimate furniture. Zero leftover Simplified-Chinese strings. The audit carries to rebuild-B: the only string that changed between build 1 and rebuild-B is the German Q34 stem, which contains no CJK.
- freeze_direct.py source level (rebuild-B): removed 450 / added 459 literals. The ONLY unaccounted strings are the documented svglib TC font switch from transform.py (`def _sc_index` → `_tc_index`, `endswith("SC")` → `endswith("TC")`, `"Noto Serif CJK SC"` → `"Noto Serif CJK TC"`, `"Noto Sans CJK SC"` → `"Noto Sans CJK TC"`) — removed 'Noto Serif CJK SC', added 'TC', 'Noto Sans CJK TC', 'Noto Serif CJK TC'. NOTE (rebuild-B): the 07:28 core-side stem pair that build 1 listed as a 4th unaccounted string is GONE — core-de build15 and this edition now carry the same corrected Q34 stem. Rendered P3 sha8 moved 56a81b7d → ad74f280 (the stem); all other frozen counts/sha8 identical: 151/164/206/166/182/176/170/191.
- Interpreter: `tools/venv/bin/python` (PIL 13.0.0) for build and freeze, as required (system python3 PIL 10.2.0 measures 1.1% differently).

## §6 D-01 Q34 stem (core-inherited, RESOLVED by this rebuild)

- At 2026-11-11 07:28:39 UTC — after build 1's transform (07:06:31) and PDFs (07:27:08 / 07:27:51) — core-de/content34.py line 105 was changed: the German exercise stem went from plural `Am Montag öffnen in Köln die ersten ___.` to singular `Am Montag öffnet in Köln der erste ___.` (singular matches key `Weihnachtsmarkt`).
- Core-de build15 (fix4 round, 2026-11-11) adopted the singular stem. This rebuild re-transformed the edition from the new core with unchanged `tr_zh-tw.py`; the stem question is closed for this edition.
- Q34 verified on rebuild-B: new stem 1× / old stem 0× in content34.py, P3 SVG, `.text.md` (line 389), print-PDF text layer and web-PDF text layer; key still `Weihnachtsmarkt` (A2), unchanged in REG, `.text.md` (line 1165) and the P8 answers.

## §7 Build history (3 rounds)

- **Build 1** (2026-11-11 ~07:25–07:28 UTC): ALL GATES PASS on the first run. No rework.
- Transform 1 OK (step-12 identical-key patch in transform.py covers zh-tw's 15 CJK identical keys, e.g. '足球', '巧克力', 'KULTUR　文化', 'LEBEN　生活'); `TR_ZH_TW` hyphen bug was fixed in all 8 scripts before transform (`UP = LANG.upper().replace("-", "_")`); measure1 24/24.
- Flow ends (build 1, identical in rebuild-B — diff of the two build.logs' flow-end lines empty): P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 964, P2-ex 2332, P3-main 886, P3-ex 2333, P4-main 647, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1310 / B2 1306, P8-battery 1409, P8-keys 2379 (bottom 2560, spare 181px).
- Q150 note '（依列出的要點評分）' retained and renders (unlike ja, where the note had to be removed for the extractor).
- **Rebuild-B build 1** (2026-11-11 08:50–09:11 UTC): ALL GATES PASS first run. Two parts: builder B re-ran run.py + render.py from core-de build15 (08:50–08:55) but died twice on disk-quota (EDQUOT) before the webpdf step (08:51 and 08:57); the quota was cleared (78G free) and the continuation baton resumed from webpdf with the working-tree `tools/webpdf.py` (09:05–09:11, `zh-tw-rebuild-B.log`). No content fixes needed; only delta vs build 1 is the Q34 stem (print 23,048,415 → 23,048,423 B, web 2,301,044 → 2,340,091 B, text 49,093 → 49,092 B — one byte/char less, the stem itself; text 42,126 → 42,125 chars). NOTE: the KIT file on disk at rebuild-B start was the core-de copy (the re-transform recopied core files over the edition dir); this file restores the edition KIT from `zh-tw-KIT-prev.md` (build 1) + rebuild-B values.
- **Fix1** (2026-11-11 09:41–09:46 UTC): P7 toolbox pad 90 → 110 only (see §8). ALL GATES PASS; text.md byte-identical to rebuild-B.

## §8 Fix1 — P7 DER WERKZEUGKASTEN box too short (D1, family defect)

- Defect (measured pre-fix with `creambox.py`, full-edition sweep): P7 col-3 toolbox rect y=330 h=424 → bottom 754.0; last entry `Es ist fraglich, ob ... = 是否……尚未確定` baseline 754.8 → clearance **−0.8** (ink spills past the box bottom). Family defect: `content7.py:76` tbh formula counts `n*29.5+6` per entry but real ink advance is `20.5+n*29.11+6` (para first baseline at y+20.5, lines at 20.5*1.42=29.11) — 6 entries under-count 123, minus 8*0.39 line-height overestimate → clearance = pad − 90.8. The fan-out pad 90 (changed from core-de's 110 with the note "validated by en/fr occlusion 0 flags") was void validation: the occlusion audit cannot see text spilling past its own box bottom.
- Fix (edition-local only): `content7.py:76` pad `+ 90` → `+ 110` (restores the core-de value) + comment rewritten with the arithmetic. No shared helper touched; no text string changed.
- Derivation (measured, this edition): entries wrap to [1,1,2,2,1,1] lines, Σlines=8; simulated last baseline 754.77 (measured 754.8 ✓). Pad 110 → tbh 424 → 444, bottom 754.0 → **774.0**, clearance −0.8 → **+19.2**. LESERBRIEFE y 770 → 790 (bottom 1314.5, clearance +10.1 unchanged, 16px gap preserved). NOCH EIN WORT y 1310 → 1330, ends **1480.5** — 67.5px before the Sätze-der-Woche rule at y=1548 (pre-fix 1460.5, 87.5px slack; no redesign needed, unlike pt/nl/ru). Col-3 ends 1460.5 → 1480.5; nothing else on P7 moves (phrases py=1560, clinic ey=2020, teaser ty=2400 fixed).
- Rebuild (fix1, 2026-11-11 09:41–09:46 UTC): `build_edition.py zh-tw` (copy in the fix1 scratch dir) + a corrected re-run of the text export (the driver's first export failed on a missing `stub_svg`/`stub_bslib` in the scratch copy — driver-side copy omission, not a content problem; re-run with the proper gloss prefix `註 — ` and NOTE_WRAP full regenerated text.md byte-identical). Tool state at build: `tools/webpdf.py` clean in git (commit 40963281 "webpdf weight + italic face resolution", mtime 09:10:13 UTC) — this web PDF now embeds the `LucernaNewsreader-Italic` subset (23,908 B; +3,050 B vs rebuild-B, text layer identical); `freeze.py` / `p8.py` / `occlusion_audit.py` carry working-tree modifications predating the rebuild wave (same versions as rebuild-B). Logs + FIX-LOG.md + GATE-LOG.md: `hidden_files/w47/scratch-fix-de-zh-tw-toolbox/`.
- Gates (all green): run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; render.py exit 0; webpdf exit 0, web PDF < 7 MB; verify.py TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent; occlusion 0 flags (real run, selftest OK — all 6 planted classes fired, clean controls silent); p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150]; freeze diff exit 0 (TOTAL added CJK 1,328, the TC explanation layer); freeze_direct rendered 8/8, all page sha8 identical to rebuild-B (54c9b51e / 2db0dd83 / ad74f280 / df1bebf7 / b42a8c3d / babfe417 / 9dc31873 / 961dd98a — incl. P3 ad74f280 Q34 and P7 9dc31873 frozen text unchanged); keycheck 149/150 (Q150 extractor truncation only, expected); boxtitle 7/7; chips 141 (P8 A2 22 / B1 13); print/web text layer identical (default 49,905 B each, word multiset identical; -raw normalised 48,777 B each); d2scan 67 pairs, 0 web gaps > 0.5pt; P8 min font 9.94pt; Q34 new stem 1× / old stem 0× in all five places; bent quotes U+201C 66 / U+201D 0 / U+2019 0 / U+201E 66 (all paired); ABSTRACT 294 B, 0 ASCII quotes.
- Visual: P7 at 100 dpi full page + 300 dpi toolbox zoom (print); last entry fully inside the cream box with clear cream below it, 16px gap to LESERBRIEFE, NOCH EIN WORT ends with a clear gap to the Sätze rule. Web toolbox zoom is pixel-identical to print (sha256 f7960a4d…).
- Changed files: `content7.py` (1 line + comment), 8 SVGs (re-rendered; freeze_direct proves only P7 geometry differs), 8 cards, both PDFs, `text.md` (rewritten, byte-identical sha), `__pycache__/content7.*.pyc`. No commit, no push.

## §9 D5 font rebuild (2026-11-12) — see §3b for the full gate round

- **Cause**: explanation-layer Latin rendered in Noto Sans CJK TC instead of Newsreader (SOP §1.1 font table; CJK-DECISION §1: script-based routing, Latin → Newsreader, no `_READER_LANG` gate). Pre-D5 census: 463 Latin-in-CJK-Sans elements.
- **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` with `_D5_READER = "cjk"` (fix2 included). No German text, fact, or key changed; no wording changed at all.
- **Two D5-caused defects, all fixed in source and rebuilt**: (1) P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column). (2) P1 box title `DIE WOCHE IN ZAHLEN　數字看本週` — +25.8px; `content12.py:43` `f.box(..., tsize=21)` (392.8px fits 404.5; 22pt still overflows by 7.0px). The P1 sommaire, P2–P7 box titles and both P8 battery heads all fit under the D5 routing — the fewest D5 defects of any CJK edition in the de family.
- **Verification**: full gate re-run (§3b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes. The P1 masthead subtitle never collided with the headline in this edition.

## §10 Reproof fix rebuild (2026-11-12)

- **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`. **Fix (in source, then rebuilt)**: F1 — P5 UND SIE prompt gained the advent-calendar question; F5 — P1 DIE WOCHE IN ZAHLEN box regained the three German sentences (+ reader gloss); F6 — `懺悔祈禱` → `懺悔祈禱日` (P7 toolbox, P2 key, P8 answer 25). Gates: build ALL GATES PASS; boxtitle 0 DEFECT (1 marginal, pre-existing); spill 0 SPILL; edge 0/0; census-patched PASS; head_check PASS; text.md dry-run diff 6 lines, 0 dropped. **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`); per-edition entry in `scratch-fix-de/FIX-LOG.md`. New deliverables: print 11,837,604 B sha `6658366039a8…`; web 1,938,383 B sha `9b83129c7472…`; text.md 49,291 B sha `c2d3f679b8c5…`.

## §11 Reproof fix round 2 rebuild (2026-11-12)

- **Cause**: independent second-round reproof found 1 low item (R2-F1) — see `hidden_files/w47/scratch-reproof2-w47-de/PROOF-NOTE-2.md`. No MAJOR/MEDIUM found; first-round F1–F9 all verified still in place.
- **Fix (in source, then rebuilt)**: R2-F1 — P5 UND SIE prompt `content56.py:53,59` `降臨節日曆` → `將臨期日曆` (the edition's own dominant term, ×6 elsewhere: L139/L349/L567/L585/L1185; the F1 fix had copied core-de zh-cn's `降临节日历`). Same character count, so the P5 box height is unchanged. core-de (zh-cn) untouched — its `降临节日历` stands.
- **Gates**: build ALL GATES PASS; p8 compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 48 titles, 0 DEFECT (1 marginal, pre-existing P7 `　工具箱` +1.0px); spill 0 SPILL; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 mechanism census PASS (D5_lat=0, D5_cyr=0, curly_in_cjk=0, curly_total=33 all in Newsreader); census-patched PASS; print/web text layers byte-identical (default 50,009 B, raw 48,959 B); P8 min font 9.94pt; text.md dry-run diff vs pre-fix2 exactly 1 line (L613), 0 dropped, creambox `###` 36 = 36.
- **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix2-w47-de/logs/` and `zh-tw/`); per-edition entry in `scratch-fix2-w47-de/FIX-LOG-2.md`.
- New deliverables: print 11,836,876 B sha `615f0277ac4a…`; web 1,937,775 B sha `6064fe1ae05a…`; text.md 49,291 B sha `7f49d6edac6e…`.

## §12 fix-de-minor1 rebuild (2026-11-13)

- **Cause**: de-family round-2 independent reproof (worker 7877e6e8, §8.4 round 2) — C-1/C-2 (core German text, all 11 editions).
- **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-zh-tw/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 48 titles, 324 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal (P7 `　工具箱` +1.0px, core same +1.0, pre-existing); spill 0 SPILL / 99 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 1,284 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 137; print/web text layers multiset-identical (34,652 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 11,836,909 B sha `7c117f8b5aec…`; web 1,937,821 B sha `3ec331b6a820…`; text.md 49,360 B sha `bb71ccafea9e…`. Not committed / not pushed (coordinator inserts).

## §13 fix-de-round3 rebuild (2026-11-13)

- **Cause**: de-family round-3 independent reproof (§8.4 round 3) — R3-F1 (all 11 editions).
- **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-zh-tw/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 48 titles, 322 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal; spill 0 SPILL / 99 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 1281, added Latin strings 136; print/web text layers multiset-identical (34,636 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 11,835,999 B sha `8597094b9ad2…`; web 1,936,175 B sha `dd26b2ac11a5…`; text.md 49,330 B sha `6865f9d835f1…`. Not committed / not pushed (coordinator inserts).
