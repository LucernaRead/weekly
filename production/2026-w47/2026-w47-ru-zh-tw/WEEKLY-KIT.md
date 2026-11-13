# WEEKLY-KIT — 2026-W47 · ru → zh-tw (Fan-out edition)

**Edition:** `2026-w47-ru-zh-tw` · **Reader:** Traditional Chinese · **Source:** `core-ru/` (read-only, frozen)
**Issue:** 2026-11-16 – 2026-11-22 · **VOL.4** · 8 pages · 150 exercises (A2 50 / B1 76 / B2 24)
**Status: DONE — zero open issues (self-check). Re-fanout 2026-11-11 (core fix1 + D1 map fix) = Build 2, final. D5 rebuild 2026-11-12 (see §10) = Build 3, current. Re-proofread follows; this self-check does not replace it.**

---

## 1. Deliverables

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ru-zh-tw.pdf` (print) | 24,763,427 | `0c4bffc78bdc7aaf8285519d94816124b8ffbc3fe936ae1bc4f0a69a93a1748d` |
| `Lucerna-VOL4-ru-zh-tw-web.pdf` (web) | 3,975,999 | `cc348ad4ae16b6f3989b6d7c3966e7f543b658838d1ec3a71817793620ecb462` |
| `2026-w47-ru-zh-tw.text.md` | 60,855 | `948538470d3cbfb3b0110300daf89c382ce4f555e08567bd1b961c8fcff52e0e` |
| `ABSTRACT.txt` | 348 | — |
| `svg/*.svg` | 8 files | freeze-verified (see §3) |

Abstract (Traditional Chinese, one line, no ASCII double quotes): `Lucerna俄語週報VOL.4：第14輪八場賽果，澤尼特與迪納摩同積31分，俄羅斯11月12日客戰烏茲別克斯坦、11月17日主場迎戰委內瑞拉，黑色星期五，11月19日五部電影首映，大學生節與嚴寒老人生日，A2到B2，適合想學俄語的繁體中文讀者做以本週話題為素材的150道練習。`

---

## 2. Build chain

- `build_map.py zh-tw` → map lit 286 / type 8 / instr 9 / key 8, exit 1 with **exactly 4 deliberate overrides** (see §6).
- `apply_ru.py zh-tw` → exit 0, "apply OK, no unmapped literals".
- `run.py` → exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE.
- `render.py` → exit 0. Print PDF 24,784,766 bytes, **72 distinct font xrefs** (CJK band; ja lesson: ~71 norm, 6,485 = bad merge — 72 is clean).
- `tools/webpdf.py` → 3,995,314 bytes, 56,095 text bytes, < 7 MB.
- **Re-fanout 2026-11-11** (core fix1 + D1 map fix; see §9): surgical map (old `map-zh-tw.json` + 4 KEEP_AS_IS values, byte-identical to the regenerated `scratch-fix-ru-d1/maps/map-zh-tw.json`); `apply_ru.py zh-tw` → exit 0, "apply OK, no unmapped literals"; `run.py` → exit 0, TOTAL 150, 0 overflow; `.text.md` re-exported (60,850 bytes, 150 exercises, 277 blocks). **Fix 1 (2026-11-11): 60,887 → 60,856 bytes (−31, the L836 Q150 appendix line, long form → ✓ form; see §9 "Fix 1"). Fix 2 (2026-11-11): 60,856 → 60,850 bytes (−6, the F1 typo fix: one 輔 deleted in two places, Q58 exercise line + appendix 58; see §9 "Fix 2").** Correction: this table previously read text.md 54,642 bytes — stale; the shipped file was already 60,815 bytes / 277 blocks (re-running `ru_textmd.py` on the pre-refanout sources reproduces it byte-identically).

---

## 3. Gate results (all PASS)

| Gate | Result |
|---|---|
| `run.py` exit 0 / TOTAL 150 / 0 overflow | PASS |
| `check_core.py` exit 0, golden BAD 0, gloss fails 0 | PASS |
| Orphan line-starts | 5, all **false positives** (P7 end-of-line `。` ×3, mid-line `：` ×1, benign `”».` ×1 — same class as core/ja) |
| Same-baseline collision | 1 (P1 y1712 `чёрная`) — same as core |
| Occlusion audit | **42 TEXTX, 0 LINEX**; adjudicated **42/42 CLEAR** |
| `p8.py extract` | **150/150** |
| `p8.py compare` | **CLEAN**, missing=[] extra=0, keydiff **[137, 138, 139, 140]** (translated keys, by design) |
| Freeze direct sha256 | **8/8** (tool self-report 0/8 is the known redirect limitation — not used) |
| Print/web text layer | char multiset identical, **25,845 chars each** |
| Freeze diff core→rebuilt | removed distinct **253** / count-sum **308**; Cyrillic-bearing removed ONLY p8 `можно` ×1 (Q46, known legal); **Morozko image present, no caption removed** (the only edition with the image) |
| P8 min font | **9.75pt** |
| §1.1 spot-check (`s11_check.py`) | **FAILURES: none** |
| `.text.md` 150-question recheck | 150 exercises + 150 answers, both contiguous 1–150, 0 missing; types 完成句子 54 / 單選 55 / 造句 12 / 句型轉換 4 / 翻譯 4 / 寫作 1 (+ 20 untagged matching) |
| P8 chips | A 113–120 ×8, G 145–149 ×5, H head (`寫作題…；範文（97 詞）見下。`) + 150 ✓ |

---

## 4. Visual check — 8/8 cards read, 0 defects

- **P1:** head `ТУР В ЦИФРАХ　數字看本輪` clear of Q6 chip (ends ≈x865, 124px gap); gloss `чёрная пятница = 黑色星期五（年末大促）。` 1 line; bridge 2 lines with `截|至` split — **normal Chinese character-level breaking, not a defect**; foot `Lucerna　俄語週報 VOL.4　正文俄語　講解繁體中文`, `第1版／共8版`.
- **P2:** gloss boxes each carry a **single** `譯注｜` prefix; word box `оттепель 解凍、回暖 / мокрый снег 濕雪 / ледяной дождь 凍雨 / гололедица 路面結冰`; band `УПРАЖНЕНИЯ　第2版練習`.
- **P3:** glosses single `譯注｜`, 2 lines each, final `。` attached (`童話的。`, `觀眾。`); `КУЛЬТУРА　文化`.
- **P4:** real W47 gloss `сравняли счёт 扳平比分 · поправка 更正 · в зоне вылета 處於降級區。` 2 clean lines, L2 ends `處於降級區。` — **no dangling 。** (the earlier dangling-。 finding applied only to a W46-only string and is void).
- **P5:** glosses single `譯注｜`, 2 lines each; band `МОЛОДЁЖЬ　青年`; `“黑色星期五”` keeps the core's `“”` quotes.
- **P6:** gloss `譯注｜задают ритм 奠定節奏 · честные 名副其實的 · середина 中間。` — **single prefix; the `講解｜` strip worked**. L2 ends `中間。`.
- **P7:** A-bridge 2 lines (`濕|雪` char break, normal); B-bridge 2 lines; **B2 bridge bare** (`синоптики обещают 氣象學家預報；по данным 官方數據；может быть 可能。`, 2 lines, L1 ends `…по`); all 5 clinic notes 1 line; word gloss `распродажа = 大促銷，要計劃，別急。` **1 line** (fix verified); full disc kept, 2 lines, clear of the 1802 divider.
- **P8:** chips all present; keys 137–140 in Traditional, comma form; **`Морозко` image PRESENT** — the keys end at col 3 y=2173.2, so the core's condition (`img_y + 250 + 90 < 2560`) fires **by design** (unlike the other 9 fan-outs, where it was skipped). Image + Bilibin caption fit cleanly, no overlap.

---

## 5. Non-defects (established, do not re-flag)

- 5 P7 orphan line-starts: end/mid-line punctuation false positives (same class as core + ja).
- P1/P7 Chinese character-level line breaks (`截|至`, `濕|雪`, `名副|其實`): normal typography.
- P1 y1712 same-baseline collision `чёрная`: same as core.
- Core rulings carried over: P8 stem 10.35pt, literal `___` blanks, body `#302c28`, `.text.md` exclusions, `— СТРАНИЦА? —` exporter artifact, trailing «Морозко» credit line.
- `塔什干` (Tashkent transliteration): the `干` is part of a proper-name transliteration, not Simplified residue.

---

## 6. Translation decisions (zh-tw)

**Sources:** W46 `2026-w46-ru-zh-tw` TM (135 lit / 6 type / 5 instr / 5 key) + 154 lit + 4 type + 4 instr + 3 key authored fresh in `miss-tr-zh-tw.json`. Map: lit 286 / type 8 / instr 9 / key 8.

**4 deliberate overrides** (build_map exit 1 is the tripwire, not a refusal):
1. `задают ритм…` (P6 gloss): strip W46-baked `講解｜` — otherwise `譯注｜講解｜…` double prefix, mixed Simplified/Traditional.
2. `синоптики обещают…` (P7 B2 bridge): same strip — the bridge must render bare, like the A2/B1 bridges.
3. `（开放题，范文如下）` → `（開放題，範文如下）`: W46 TM shipped Simplified `范文`; W47 uses proper Traditional `範文`.
4. `每题附一句中文简析　带 ✓ 的为范文题` → `每題附一句簡析　帶 ✓ 的為範文題`: same `範文` correction (value also drops `中文` per W46's choice).

**7 dead overrides removed** (W46-only strings, not in the W47 core — reported as UNUSED by build_map): `закончился…`, `на момент сдачи…` (gloss form), `отследить…`, `плед…`, `посылка…`, `предзимье…`, `садится…`. Only 2 of the 9 `講解｜` TM values exist in W47 (the P6 gloss + P7 B2 bridge above). Lesson: simulate wraps only on strings that actually exist in the W47 core.

**Pre-build fixes:** P7 word gloss `要計劃，不要著急。` → `要計劃，別急。` (was 1 line + lone `急。`, 0.6px over the limit; now 1 line, 359.1px). P1 gloss `чёрная пятница = 黑色星期五（年末大促）。` 397.3px = 1 line. P1 head `數字看本輪` ends ≈x865. Full disc kept, 2 lines.

**Simplified-character sweep** of applied sources and `.text.md`: 0 Simplified-only chars except `干` in `塔什干` (transliteration, §5).

**Names/terms:** Ded Moroz = 嚴寒老人 (as in the W47 Chinese strings); `ледяной дождь` = 凍雨, `мокрый снег` = 濕雪; `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ` strip matches the foot wording exactly (`正文俄語　講解繁體中文`); P2 band `第2版練習` (no `題` suffix — matches TM P3–P6 `第3/4/5/6版練習`); P5 band keeps core's `“黑色星期五”` quotes.

**Type names:** 完成句子 / 單選 (both 单选 and 完形单选) / 詞彙配對 / 造句 / 句型轉換 / 翻譯 / 寫作.

**Keys 137–140 (comma form, no ` — `):**
137 `11月17日星期二，大學生節。` · 138 `包裹要追蹤、領取並檢查。` · 139 `星期二俄羅斯隊對陣委內瑞拉隊。` · 140 `祝大家大學生節快樂！`
Writing bridge: `寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。` · note: `範文見本版 H 區（{NWORDS} 詞）`.

**Tool fix made during this edition:** `s11_check.py` lang parsing — `rsplit("-",1)` cut `zh-tw` to `tw`, so the Latin-reader CJK check misfired. Fixed to detect the `-zh-tw` suffix; re-run: FAILURES none. (ja/ko were unaffected: their codes have no hyphen.)

---

## 7. Known core items (not fixed here)

Core KIT §7.1 §1.1 gaps (a)–(e) and §7.3 benign findings carry over unchanged — see `core-ru/WEEKLY-KIT.md`. Nothing new.

---

## 8. Files

- Edition: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-zh-tw/` (8 SVG, print + web PDF, `.text.md`, `ABSTRACT.txt`, this KIT).
- Build records: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-ru/zh-tw/` — `build_map.log`, `build_map2.log`, `build_map3.log`, `apply.log`, `apply2.log`, `apply3.log`, `run.log`, `render.log`, `webpdf.log`, `check_core.log`, `occlusion.log`, `ru-zh-tw-occlusion.json`, `adjudication.log`, `p8-extract.log`, `p8-compare.log`, `ru-zh-tw-p8.json`, `ru-zh-tw-p8-compare.json`, `freeze.log`, `freeze/`, `textmd.log`, `RECORD.md`.
- Translation: `miss-tr-zh-tw.json`, `map-zh-tw.json` (scratch root).
- Pre-build wrap simulation: real `svglib.wrap()` (see RECORD.md §2).

---

## 9. Re-fanout (2026-11-11, core fix1 + D1 map fix)

Full record: `hidden_files/w47/scratch-refanout-ru/records/zh-tw/RECORD.md`. Rebuilt whole from finalized core-ru (fix1 f11854bf; core SHAs re-verified before/after, unchanged) with the surgical D1 map (old `map-zh-tw.json` + 4 KEEP_AS_IS values, byte-identical to the regenerated `scratch-fix-ru-d1/maps/map-zh-tw.json`).

- **D1** — P6 chart title + `УЧЕБНЫЕ ДАННЫЕ`, P6 disclaimer full Russian sentence, P7 subtitle + `Три уровня, три темы`, P8 subtitle + `Большой тест недели + все ответы` (text.md L459/L504/L596; disclaimer SVG-only by design); freeze diff core→rebuilt: removed distinct 253 / count-sum 308, Cyrillic-bearing removed ONLY Q46 `можно` ×1, unexplained 0. **Number correction:** the task brief/FIX-NOTE quoted distinct 256 / count-sum 317 for the rebuild — that was the FIX-NOTE verification's number, computed when the core SVG still lacked the fix1 kicker double spaces; with the kicker landed in the edition (required by the same task), the 3 P1 kicker runs (`'  '` ×7, `',  '` ×1, `'—  '` ×1) are no longer removed: 253/308. Decomposed the two freeze-diff JSONs — the ONLY delta is those 3 kicker strings; the Cyrillic conclusion (only `можно`) is identical. The broken first build's control numbers were distinct 287 / count-sum 360, Cyrillic 23.
- **D2** — Q25 option `День студента` (was `Международный день студента`); full phrase still ×2 in text.md (article + Q11 stem), same as core.
- **D6** — Q20 key `желании` (was `желание`); p8 extract key 20 = core `ru-p8.json:177`.
- **Kicker** — 9 double spaces landed; PIL ink gaps [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6] px, min 5.9 ≥ 4, exactly the INVEST-NOTE Table 1 values.
- **`.text.md` diff old→new:** exactly 6 line pairs, nothing else (60,815 → 60,887 bytes).
- **Gates re-run all green:** run exit 0 / TOTAL 150; p8 extract 150/150 + compare CLEAN (keydiff [137, 138, 139, 140]; direct JSON keydiff vs core identical); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR; freeze baseline 8/8; print/web text multiset identical overall and per page (25,845 chars); P8 min font 9.75 pt; §1.1 all pass; creambox full scan byte-identical to the first build's scan (96 BELOW-WINDOW lines: +28.0 ×25, +32.0 ×41, +34.0 ×4, +37.0 ×25, +44.0 ×1 — the +44.0 is the P1 quick-quiz header pointer row y=2348.0, below the brief-news box by design, same element as in the other editions; all classified pre-existing). Morozko image PRESENT by design (keys end col 3 y≈2173.2). Round 2 independent proofread follows; this self-check does not replace it.
- **Fix 1 (2026-11-11, text.md L836 exporter bug — same one-line patch as ru-ko Fix 1; full record in `hidden_files/w47/scratch-ru-textmd-616.md` + apply report `hidden_files/w47/Reports-preinsert/ru-textmd-616-apply.md`):** text.md L836 printed the long form `150. （開放題，範文如下） — 範文見本版 H 區（97 詞）` instead of the P8 ✓ form. Root cause: `ru_textmd.py:616` special-cased only the Chinese type label `e["type"] == "写作"`; this edition's Q150 type is Traditional Chinese `寫作` (content8.py:110), so it fell through to the generic `key — note` format. The print P8 was already correct (content8.py:127 writes the ✓ form directly). Fix: `do_appendix` now detects the writing exercise by its parenthesised key (`e["key"].startswith(("(", "（"))`) — type-agnostic, verified unique (exactly 1 of 150 in the live registry of core-ru + all 10 ru fan-outs, always n=150, page 8). All 11 `ru_textmd.py` copies carry the same patch (md5 `0f093296ffd8487d5d5b7bf2225bb191`). Regenerated text.md only (60,887 → 60,856 bytes, SHA-256 `bc9c425f1c887d4ad70b7f2369671b3d36979b33d40713967977a4febd4a62c4` → `76d599d5f6d51014bc9dca019c683f9d41bb4f34c13ca81ea7771c0503b120be`); diff vs pre-fix text.md is exactly 1 line (L836 → `150. ✓ 範文見本版 H 區（97 詞）`). Guard: the fixed exporter regenerates core-ru text.md byte-identically (SHA `348511e0…`, 60,953 bytes), core untouched. Print/web PDFs NOT rebuilt by this fix (no render.py/webpdf.py run). Gates re-run on the new text.md: p8 extract 150/150 + compare CLEAN (keydiff [137, 138, 139, 140]); appendix keys 1–150 all match the printed P8 keys; print-PDF P8 text contains the ✓ Q150 line; L836 note text equals the P8 SVG's Q150 note text. Print PDF SHA verified on disk, unchanged by this fix (`2d19ad64…`, matches §1). Note (apply-time, 2026-11-11): the web PDF on disk (SHA `91ded018…`, 3,995,346 B) differs from the §1 line (`991b22ab…`, 3,995,314 B) because concurrent webpdf rebuild jobs (`scratch-webpdf-ko-zh`, started 22:19 UTC) rewrote all 9 ru web PDFs during this apply; coordinator to reconcile the KIT web SHA. A full independent re-proof of this edition follows; this fix record does not replace it.

- **Fix 2 (2026-11-11, re-proof (b) finding F1 — one-character typo fix; full record in `hidden_files/w47/scratch-ru-zh-tw-f1/`):** print P8 answer key 58 and text.md (Q58 exercise line L335 + appendix 58 L736) misspelled Krasnodar as `克拉斯諾輔達爾` (extra 輔). Root cause: the Q58 options list in `content34.py:235` carried the typo; the correct form `克拉斯諾達爾` is used everywhere else in this edition (P4 section head, keys 48/51/124, `content8.py:39`). The answer letter `a` was correct (Krasnodar beat CSKA 4:2) — only the Chinese team-name note was wrong. Fix: delete exactly one character (輔) in `content34.py:235`, `克拉斯諾輔達爾 a` → `克拉斯諾達爾 a`; nothing else in any source file changed. Re-exported text.md with the patched `ru_textmd.py` (KIT command form, title `VOL.4 · Russian text · Traditional Chinese explanations`): 60,856 → 60,850 bytes, SHA-256 `76d599d5f6d51014bc9dca019c683f9d41bb4f34c13ca81ea7771c0503b120be` → `277a24f8a1674c970a367bf4fc8cccdd85d3f88941f85d633713a0e525ee6c83`; diff vs pre-fix text.md is exactly 2 lines (L335 + L736), L836 stays `150. ✓ 範文見本版 H 區（97 詞）`. Rebuilt P8 SVG + print PDF + web PDF via `tools/run_build.py` (run,render; production untouched during build, integrity re-hash clean) + `tools/webpdf.py`: P1–P7 SVGs byte-identical to the previous build; P8 SVG differs by exactly the one deleted character (length −1); print PDF 24,784,766 → 24,784,332 bytes, SHA-256 `2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4` → `094b6a3b17cb34d7b0760a2bc1775cd9e59aadedb5f906ce51e103254ad537ca`; web PDF 3,995,346 → 3,994,661 bytes, SHA-256 `91ded0180e2287d7ff9311d329453c1a557be8db9a4009908ab5e24eb7163bab` → `eba60ec2f70f220cecf42d633976ce146c1276603000b046c1f23ff0dd07c3c2` (this also resolves the §1 web-SHA drift the re-proof flagged: the §1 line `991b22ab…` was the pre-rebuild web PDF). Gates re-run all green: run.py exit 0 / TOTAL 150; render.py exit 0; p8 extract 150/150 + compare CLEAN (keydiff [137, 138, 139, 140]); freeze diff core→rebuilt unchanged from the pre-fix baseline (removed distinct 253 / count-sum 308, Cyrillic-bearing removed ONLY Q46 `можно` ×1; the only delta vs the pre-fix freeze-diff is P8 added strings: `克拉斯諾輔達爾` gone, `克拉斯諾達爾` count 4 → 5); check_core.py exit 0, golden BAD 0, gloss fails 0 (orphans 5 + P1 y1712 collision, same as before); print/web text layers byte-identical (104,490 bytes each); web PDF 3,994,661 bytes < 7 MB, 56,092 text bytes; text.md appendix 150 keys contiguous 1–150, agreeing with the P8 extract keys (Q150 in the established ✓ note form); grep for `輔達爾` over the whole edition dir returns ZERO hits. Note: a pre-insert web-PDF rebuild job may rewrite this edition's web PDF after this fix; the SHA above is the file this fix built — coordinator's KIT-sync wave to record finals. Round-2 re-proof follows; this fix record does not replace it.

- **Fix2 U+201C port (2026-11-12; full record in `hidden_files/w47/scratch-gatefix-u201c-ru/FIX-LOG.md`):** ported the core-de fix2 font-routing patch (commit 4ac7192c) into this edition's `svglib.py`: U+201C/U+201D/U+2019 now route through the serif branch to Newsreader (their advance in Noto Sans CJK SC is 1.000em; Newsreader's is 0.44/0.44/0.26em). Pre-patch `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (the _run_w Hangul-fix file); post-patch md5 `b0928993747a13e94573a5dcced00961`; diff is only the ported block (verified: py_compile passes, reverse-patch reproduces the pre-patch md5). SVG census before: 2 defective glyphs (P5 `“”` in `“黑色星期五”：11月16日開始打折`, 18pt, Noto Sans CJK SC); after: 0 defective, quotes now Newsreader. Rebuilt via `tools/run_build.py` (two independent builds) + `tools/webpdf.py`; synced `svg/` + `cards/` + print + web PDFs into production. text.md SHA UNCHANGED (`277a24f8…`, 60,850 B). Print PDF `dbd7a52a…` 24,781,766 B → `810514b2…` 24,784,623 B; web PDF `d7787a5e…` 3,992,096 B → `0cef86ea…` 3,992,151 B. Gates green: run.py exit 0 / TOTAL 150, zero overflow; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 140]; check_core.py exit 0, golden BAD 0, gloss fails 0 (orphans 5 + P1 y1712 collision, same as before); occlusion audit 0 flags; freeze 8/8 SVG SHA match between the two builds + print PDFs byte-identical; freeze baseline 8/8 on the synced files; print/web text layers byte-identical per page (31,405 chars; pdftotext 56,176 bytes each); word-join census 41/57, identical to the _run_w after-census, 0 real joins; spill 0; boxtitle 0 DEFECT (with the production pre-fix build as baseline); Morozko SURVIVES (P8 keys end 2188.39, image 422.5×250 at y=2212.39, images per page [1,1,0,1,1,0,1,1] total 6).

*Self-check complete 2026-11-11. Coordinator's independent proofread is the next step; this edition is in `production/` only (no insertion/lint/push/commit performed).*

---

## 10. D5 (2026-11-12; SOP §1.1; B档)

- `mechanism/apply_variant.py --target ru --reader zh-tw` (mode **cjk**; `_D5_READER = "cjk"`): 按字符文字分流、不加 `_READER_LANG` 门（裁定 §1）：拉丁/数字/标点 → Newsreader，西里尔 → `sans_noto`（Noto Sans Medium/Bold），繁體中文 → CJK TC（讀者 zh-tw 用 core-zh-tw 基底）。`svglib.py` md5 `b0928993747a13e94573a5dcced00961` → `d6e0a93d27c8366de20a16fa4a38cc20`（與 core-ru 的 D5 svglib 同 md5；fix2 已在、安裝器未重加；TC 引號不擴展，裁定 §3）；路由斷言 `assert_routing.py`（latin→news，CJK 模式同參）全過。基線核實：修復前 `run.py` 重建 8/8 SVG 與交付字節一致；普查修復前拉丁在 CJK Sans **207** → 修復後 **0**，西里爾 0，彎引號在 CJK 0（4 個全在 Newsreader）；引號普查 `census_quotes.py` 0 缺陷（修復前後皆 0）。`tools/venv/bin/python` 全程構建：`run.py` RC=0，TOTAL 150，0 FLOW OVERFLOW，**0 HEAD TOO WIDE**（`head_check.py` vs 修復前 run.log：PASS 0 defects）；`render.py` RC=0（首遍即正常 24,763,703 B，無字體子集爆炸）；`webpdf.py` RC=0，3,976,325 B（<7 MB），文本層 56,175 字節。text.md 字節不變（SHA-256 `277a24f8…`，60,850 B）。印版 `810514b2…` 24,784,623 B → `a6c1b4cf…` 24,763,703 B；網版 `0cef86ea…` 3,992,151 B → `8eb6f61c…` 3,976,325 B。**重建全部在生產目錄原地進行**（`production/2026-w47/2026-w47-ru-zh-tw/`；build-copy 僅為門禁的 freeze 重建輸出，驗後已刪；§1 的 SHA 與生產文件逐一核對一致）。
- **D5 引起的新缺陷 0 處**（首輪門禁即全綠）。P8 鍵行無互撞（修復後 occlusion 審計 0 flags；PILOT-REPORT §5.4 的 P8 鍵行互撞已證實為測量誤報、不修）。
- **D5 全部門禁（2026-11-12，`gates-summary.txt`，GATES_OVERALL_FAIL=0）**：D5 普查 PASS（拉丁 0、西里爾 0、彎引號 0）；引號普查 0；`p8.py extract` **150/150**，`compare` vs core-ru **CLEAN**（keydiff=[137, 138, 139, 140]，預期讀者語鍵）；`freeze.py baseline` **8/8 SVG 字節一致**；freeze-diff vs 修復前基線新增 CJK 字符 0（新增 Latin strings 67 個為 D5 分 run 的直接結果）；occlusion 審計 **0 flags**（修復後 `occlusion_audit.py`）；boxtitle **0 DEFECT**（57 標題、703 正文行）；creambox **PASS 0 defects**（P8 行數 225→225、距頁腳線余量 33.2px→33.2px，無重排；寬度比 n=393，中位 1.026，粗體中位 1.040）；spill **0**；edge **0 TOUCH、0 NEAR**；印/網文字層**字節一致**（各 32,556 字符）。Morozko SURVIVES as before（見 §9 Fix2 條；P8 keys end 2188.39）。獨立重校由協調員另派，本節只記自查門禁。
- 全記錄見 `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-zh-tw/`，報告 `D5-REPORT-ru-2026-w47-ru-zh-tw.md`。本版為 ru 家 D5 最後一版（core-ru + 10 fan-out，11/11 完成）。

## 11. F-2 附錄頁碼佔位符修復（2026-11-12，獨立重校 F-2；完整記錄見 `hidden_files/w47/scratch-fix-ru/FIX-LOG.md`）

text.md 附錄行 `— СТРАНИЦА ? —` 是導出器 `ru_textmd.py` do_appendix 的硬編碼佔位符；附錄（`## Answers`）在 P8（本版印 PDF 逐頁核實：8 頁，P8 含 `— СТРАНИЦА 1 —` 至 `— СТРАНИЦА 8 —`）。源頭已修（上一任：do_appendix `— СТРАНИЦА ? —` → `— СТРАНИЦА 8 —`，11 份 `ru_textmd.py` 副本字節一致）。本版 text.md 用已修導出器重導出（`ru_textmd.py . 2026-w47-ru-zh-tw.text.md "VOL.4 · Russian text · Traditional Chinese explanations"`）。重導出無附帶差異（除附錄行外與修前文件完全一致）。最終與修前文件 diff 僅附錄行 1 行（`?`→`8`），字節數/行數/塊數不變。text.md SHA-256 `277a24f8…` → `fa1040dd81ca9517b908904bcaa4d68f445327cb8f27a03a141cd93c0aa44462`（60,850 B）。§1 文件表行的 text.md SHA 已同步更新；印/網 PDF 未重渲染、SHA 核對不變（印 `a6c1b4cf…`，網 `8eb6f61c…`）。門禁：`p8.py compare --core-dir core-ru --edition-dir 2026-w47-ru-zh-tw --target ru --total 150` **CLEAN**（150/150，missing=[]，keydiff=[137, 138, 139, 140] 翻譯題，預期）；occlusion 未重跑（PDF 未變）。F-1（P8 key 右餘量）按協調員裁定接受現狀、不修；F-3（Morozko 圖注行）按設計、不修。


## 12. 第二輪修復（2026-11-12，第二輪獨立重校 G-6；完整記錄見 `hidden_files/w47/scratch-fix-ru/FIX-LOG.md` §8）

G-6：`content7.py:48` 小結 `по данным 官方數據` → `по данным = 據……數據`（по данным=據……數據，無「官方」之意；與本版 L543 及 core 一致）。text.md 最終 diff 僅 1 行（L538）；重導出無丟行。SVG 只變 p7。印 PDF `a6c1b4cffbef…` 24,763,703 B → `7db5bece16d6…` 24,763,429 B；網 PDF `8eb6f61cef46…` 3,976,325 B → `31a07aa54b5a…` 3,976,005 B（56,180 text bytes）；text.md `fa1040dd81ca…` 60,850 B → `bc0a26a5267f…` 60,855 B。門禁：p8.py compare **CLEAN**（150/150，missing=[]，keydiff=[137, 138, 139, 140] 翻译题，预期）；occlusion **0 flags**；boxtitle **0 DEFECT**；spill rc=0；edge **0 TOUCH、0 NEAR**；head_check **PASS 0 defects**；run.py TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE；D5 普查 CJK+Latin=0、CJK+Cyrillic=0；弯引号全部 Newsreader（boxtitle 57 標題/703 正文行；彎引號 4 處）。

## 13. 第四輪修復（2026-11-12，第四輪獨立重校 J-6；完整記錄見 `hidden_files/w47/scratch-fix4-w47-ru/FIX-LOG-4.md`）

J-6：Q77 配對選項 a 標 `促銷碼` 與全版 gloss `折扣碼` 不一致（其餘 9 處皆為 `折扣碼`）。源頭 `content56.py:85` 配對選項表 `["大促銷 d", "退貨 b", "促銷碼 a", "折扣 c"]` → `["大促銷 d", "退貨 b", "折扣碼 a", "折扣 c"]`（僅改該一字；其餘三項選項標本就與 gloss 一致）。SVG 只變 p8。印 PDF `7db5bece16d6…` 24,763,429 B → `0c4bffc78bdc…` 24,763,427 B；網 PDF `31a07aa54b5a…` 3,976,005 B → `cc348ad4ae16…` 3,975,999 B；text.md diff 恰 2 行（L413、L757），SHA `bc0a26a5267f…`（60,855 B）→ `948538470d3c…`（60,855 B，字節不變：`促銷碼`→`折扣碼` 等長）；導出器幹跑無丟行。印/網 PDF 各 8 頁、文字層歸一化一致（31,407 字符）；印 PDF 文字層 `折扣碼` ×6、`促銷碼` ×0，網 PDF 同。門禁：p8.py compare **CLEAN**（150/150，missing=[]，keydiff=[137, 138, 139, 140] 翻譯題，預期）；occlusion **0 flags**；boxtitle **0 DEFECT**（57 標題/703 正文行）；spill rc=0（1 條既有 `[observe]` Black Friday gloss 行）；edge **0 TOUCH、0 NEAR**；head_check **PASS 0 defects**；D5 普查 CJK+Latin=0、CJK+Cyrillic=0（11 版全量）；彎引號全部 Newsreader（4 處）。J-6 另半在 core-ru（`促销码` → `折扣码`，見 core-ru KIT §7.9）；其餘 8 版 Q77 選項 a 標均與其版內規範形一致，不動。
