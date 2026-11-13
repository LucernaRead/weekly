# RECORD — 2026-w47-ru-zh-tw (reader: Traditional Chinese)

**Status: DONE, zero issues. Build 1 = final (no rebuild).** Completed 2026-11-11.

## 1. Deliverables (final)

- Print PDF: `Lucerna-VOL4-ru-zh-tw.pdf` — **24,785,168 bytes**, SHA-256 `69239a09d74a478e975893b8ee7866facd8ed16fb8bcfe7b14f78307b03469d7`
- Web PDF: `Lucerna-VOL4-ru-zh-tw-web.pdf` — **3,963,820 bytes**, SHA-256 `543ce70dd628ee47313da3ffe667f2ef40df44841b299095a40bb9774200bfbd`, 55,950 text bytes
- `.text.md`: 54,642 bytes, 150 exercises, 203 blocks
- `ABSTRACT.txt`: 348 bytes, no ASCII double quotes
- `WEEKLY-KIT.md` in the edition dir; 8 SVG in `svg/`

## 2. Gates (all PASS, build 1)

- run.py exit 0, TOTAL 150, 0 overflow; render.py exit 0; print 24,785,168 bytes, **72 font xrefs** (CJK band; ja lesson: ~71 norm)
- check_core.py exit 0: golden BAD 0, gloss 0; orphans 5 — ALL false positives (P7 end-line `。` ×3, mid-line `：` ×1, benign `”».` ×1); same-baseline collision 1 (P1 y1712 `чёрная`, same as core)
- Occlusion: **42 TEXTX, 0 LINEX**; adjudicated **42/42 CLEAR**
- p8 extract **150/150**; compare **CLEAN**, keydiff [137,138,139,140]
- Freeze direct sha256 **8/8**
- Print/web char multiset identical: **25,752 chars each**
- P8 min font **9.75pt**; §1.1 `s11_check.py` FAILURES: none (after fixing the script's zh-tw lang-parse bug, §6)
- `.text.md` recheck: 150 ex + 150 answers, contiguous 1–150, 0 missing; types 完成句子 54 / 單選 55 / 造句 12 / 句型轉換 4 / 翻譯 4 / 寫作 1 (+20 untagged matching)
- P8 chips: A 113–120 ×8, G 145–149 ×5, H head + 150 ✓
- Visual: 8/8 cards read, 0 defects

## 3. Translation / build history

- TM zh-tw: 135 lit / 6 type / 5 instr / 5 key. Miss-tr: 154 lit + 4 type + 4 instr + 3 key + meta.
- Map: lit 286 / type 8 / instr 9 / key 8. build_map exit 1 with exactly **4 deliberate overrides** (tripwire, not a refusal):
  1. `задают ритм…` (P6 gloss) — strip W46-baked `講解｜` (else `譯注｜講解｜…` double prefix, mixed Simplified/Traditional)
  2. `синоптики обещают…` (P7 B2 bridge) — same strip; bridge renders bare like A2/B1 bridges
  3. `（开放题，范文如下）` → `（開放題，範文如下）` — W46 TM shipped Simplified `范文`; W47 uses proper Traditional `範文`
  4. `每题附一句中文简析　带 ✓ 的为范文题` → `每題附一句簡析　帶 ✓ 的為範文題` — same `範文` correction
- **7 dead overrides removed** (W46-only strings, not in W47 core, reported UNUSED): `закончился…`, `на момент сдачи…` (gloss form), `отследить…`, `плед…`, `посылка…`, `предзимье…`, `садится…`. Only 2 of the 9 `講解｜` TM values exist in W47 (P6 gloss + P7 B2 bridge). **Lesson: simulate wraps only on strings that actually exist in the W47 core** — the first sim ran on the W46 P4 gloss instead of the real W47 P4 gloss (#69); the real P4 gloss needed no fix (2 clean lines, L2 ends `處於降級區。`).
- Pre-build wrap sim (real `svglib.wrap()`): P1 gloss 397.3px 1 line; head `數字看本輪` ends ≈x865 (124px clear of chip); P1 bridge `截|至` split = normal Chinese char-level breaking, not a defect; P7 disc FULL form 2 lines — kept, no shortening; all 5 errs 1 line. **1 real pre-build fix:** P7 word gloss `要計劃，不要著急。` → `要計劃，別急。` (was 1 line + lone `急。`, 0.6px over; now 1 line, 359.1px).
- Simplified-character sweep of applied sources + `.text.md`: 0 hits except `干` in `塔什干` (transliteration, not residue).
- P8 image: **Morozko PRESENT** — keys end col 3 y=2173.2, core condition (`img_y+250+90<2560`) fires by design (other 9 fan-outs skipped it). Image + Bilibin caption fit cleanly.
- Names: Ded Moroz = 嚴寒老人; `ледяной дождь` = 凍雨, `мокрый снег` = 濕雪; P2 band `第2版練習` (no `題`, matches TM P3–P6); P5 keeps core's `“黑色星期五”` quotes; A/B/C bridges 1 line each.
- Keys 137–140 (comma form): 137 `11月17日星期二，大學生節。` · 138 `包裹要追蹤、領取並檢查。` · 139 `星期二俄羅斯隊對陣委內瑞拉隊。` · 140 `祝大家大學生節快樂！`
- Writing bridge `寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。` / note `範文見本版 H 區（{NWORDS} 詞）`.

## 4. Tool fix (this edition)

`s11_check.py` lang parsing: `rsplit("-",1)` cut `zh-tw` to `tw`, so the Latin-reader CJK check misfired (FAIL on a correct edition). Fixed to detect the `-zh-tw` suffix; re-run: FAILURES none. ja/ko unaffected (codes have no hyphen).

## 5. Logs

`build_map.log`, `build_map2.log`, `build_map3.log`, `apply.log`, `apply2.log`, `apply3.log`, `run.log`, `render.log`, `webpdf.log`, `check_core.log`, `occlusion.log`, `ru-zh-tw-occlusion.json`, `adjudication.log`, `p8-extract.log`, `p8-compare.log`, `ru-zh-tw-p8.json`, `ru-zh-tw-p8-compare.json`, `freeze.log`, `freeze/`, `textmd.log`.
