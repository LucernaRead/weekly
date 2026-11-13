# WEEKLY-KIT — 2026-W47 · nl → de (German readers)

Dutch weekly newspaper for German readers. Target language Dutch (nl), reader
native language German (de). VOL.4, issue 2026-11-16 – 2026-11-22. Target: 150
exercises (10/18/18/18/18/18/12/38 across pages 1–8); A2 46 / B1 73 / B2 31;
model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in German. No new trend research, no invented reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-de.pdf` — 12,104,245 bytes,
  sha256 `9032021929da68607da8097bd50612aeec93f4b5de76d0e15e8757712172fb19`
- Web PDF: `De-Lucerna-VOL4-nl-de-web.pdf` — 1,536,368 bytes,
  sha256 `fbf0c25a503a8fb532b60dc60d1b95b265a00659df1c69afb334b6bddf299795`
  (via `tools/webpdf.py`, text layer pdftotext 46,678 B)
- Source export: `2026-w47-nl-de.text.md` — 46,247 bytes
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
  sha256 `6825c35db04c62e1bec4f8f6e6a511597a17af0b02b17bc5260a560043575785`
- `ABSTRACT.txt` (German, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 5)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P8-keys] ended col 3/3 y=2565 (bottom 2560)` — flow cursor only; last ink
  baseline 2548.5, ink bottom ~2552, 44px above the footer rule (y=2596).
  Same shape as the en edition (flow 2551, ink ~2540); no overflow warning.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 5): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 834/834 … P8 2255/2255); pdftotext
  print 46,688 B / web 46,690 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  title "MERK ES DIR" 405 px (0.5 px past the 404.5 px box edge, invisible);
  P6 chart head "ÜBUNGSDATEN" fits; P7 BRIEVEN box ends 1927.5, above the
  ZINNEN rule (y=1937); P8 answers 1–150 complete, pen photo with caption.

## Fixes vs the generated fan-out (explanation layer only)

1. P1 subtitle → 36 pt, spacing 6 (W46 de precedent; 1653 px < 1818 px limit).
2. Numbers-box title → "DE WEEK IN CIJFERS　IN ZAHLEN" (373 px).
3. Numbers-box items shortened (items [3,1,2,2], total 384 px, fits col 1):
   item 1 "(16. Nov.: Deutschland–Niederlande)", item 2 "(20:45: Anpfiff)",
   item 3 "(8 Punkte: beide vorn)", item 4 "(5. Dez.: Pakjesavond, in 19 Tagen)".
4. P6 chart head → "DE GRAFIEK　ÜBUNGSDATEN" (344 px).
5. P2 box title → "ZO ONTHOUD JE HET　MERK ES DIR" (W46 de version).
6. P7 BRIEVEN glosses shortened to telegraphic W46 style (g1 2 lines, g2 2 lines;
   VOL.5 reference kept so the §1.1 VOL.5 count stays 5 = core); PAS OP! /
   HET WOORD glosses shortened; box bottom 1927.5.
7. P8-keys overflow (build 1: FLOW OVERFLOW on col 3, German answer notes longer
   than the core's): shortened 4 answer notes, each measured to drop from 2 lines
   to 1 (13.5 pt serif, width 422.5 px): #88, #89, #11, and #131 (the col-3
   lever — savings must land in col 3's own content, P7/P8 groups). Keys untouched.
8. P1 agenda gloss was a single unwrapped p.text line running off the page edge
   (ink to x=1968.75 > 1950): → "Alle Daten und Zeiten: Artikel Seite 2–5."
   (345.2 px, inside the box). Same defect class pre-fixed in fr/es/it/pt/ru.
9. P7 golden-sentence gloss #2 wrapped to 2 lines and overlapped the next quote:
   → "Nach vier Spielen stehen die Niederlande und Griechenland mit 8 Punkten
   vorn. (Pagina 1)" (1 line, 19.5 pt sans, 884.5 px). Other 8 glosses were
   already 1 line (fr/es/it/pt/ru/ja/ko/zh-tw pre-checked OK).
10. HET WOORD gloss stays 2 lines ("„Gruppensieg“: erster Platz in der Gruppe,
    direkt ins Viertelfinale.") — no faithful 1-line version fits 422.5 px at
    19 pt; it ends above the row-B rule (y=1853) and the occlusion audit is
    clean; accepted.
11. **Re-fanout fix2 (2026-11-11, proof1 D1/D2/O2):** P1 `IN DEZE EDITIE　IN DIESER
    AUSGABE` (+33.5px over) → `IN DEZE EDITIE　AUSGABE` (+89.5 clearance);
    P6 `VOOR OF TEGEN?　DAFÜR ODER DAGEGEN?` (+47.5) → `VOOR OF TEGEN?　DAFÜR /
    DAGEGEN` (+13.5); P2 `ZO ONTHOUD JE HET　MERK ES DIR` (+0.5) → `MERK DIR`
    (+32.5). All verified on the built SVGs (ink) and visually on P1/P2/P6.
12. **Re-fanout fix2 D3:** P2 D-set option c → `"eten voor Sinterklaas' paard"`
    (core fix2 short form); clearance +71.9px.
13. **Re-fanout fix2 D5:** P4 HET PROGRAMMA box gained `"Stand Eredivisie na 12
    ronden: PSV 26, Feyenoord 25, Ajax 25 punten."` (5th fact, after Speelronde
    12, before Speelronde 13); box +73px.

## Notes

- German answer-zone notes are longer than the core's Chinese ones; the P8 flow
  ends tight (see above) — judge by ink, not by the flow cursor.
- The curly apostrophe U+2019 renders with a visible gap before "s" in card PNGs
  (e.g. "Sinterklaas' s") — same quirk as the core, not a defect.
- HET WOORD gloss on P1 ends tight against the row-B rule but does not cross it.

## Re-fanout (core fix2 `5de7492f`, 2026-11-11, build 6)

Rebuilt from the fixed core (D3 + D5 + D4 export + proof1 title fixes §Fixes 11–13). Build only — no commit, no push. Logs: `hidden_files/w47/scratch-refanout-nl/` — `de-build.log`, `de-check.log`, `de-creambox.log`, review `de-review/` (p1–p8 + crops).

- D3 short form in P2, clearance +71.9px (x+adv 1790.1); D5 standings line in P4 box + text.md; D4 142 `— Antwort:` + 8 `(Antwort x)`, 答案 0; italic print=web=1.
- text.md diff vs build 5: exactly 9 changed lines (P1 title 2 + P2 title 2 + D3 2 + D5 1 + P6 title 2) — no unintended changes.
- Gates (build 6): TOTAL 150, by page 10/18/18/18/18/18/12/38, zero OVERFLOW / TOO WIDE; occlusion 0; p8 extract 150/150, compare CLEAN; freeze 8/8; print/web text posdiff 0, msdiff 0, all 8 pages (tokens 832/813/719/720/795/729/890/2255); pdftotext 46,734 B both; P8 font min=median 10.12pt, spans 187; chips core=edition {A2:8, B1:24, B2:3}; §1.1 clean.
- Creambox: 2 CREAM-BOTTOM flags, both pixel-probed 0 dark pixels in the 7px strip below the box bottom → false positives: P2 EN JIJ last line `'und schick sie an die Redaktion.'` (bottom 1474.6 vs rect 1474.8, 2px-margin rule only) and P5 `'Niederländisch und schick sie ein.'` (bottom 1023.2 vs rect 1023.5). 0 true overflow.
- 8-page visual pass: P1–P8 clean (P1 `IN DEZE EDITIE　AUSGABE` in box; P2 `MERK DIR` in box, c. line fits; P4 box with new standings line; P6 `DAFÜR / DAGEGEN` in box; P7 BRIEVEN ends above the ZINNEN rule; P8 answers 1–150 complete).
- Known core item NOT in this build: core-nl re-proof (post-fix2) found D6/D7 — a Chinese full stop `。` orphaned alone on its own line on core P3 and P7. Core fix3 is being done by another agent; this edition gets a separate incremental rebuild then. This build is against core HEAD `5de7492f` only.

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 7)

Incremental rebuild syncing core-nl fix rounds 3–5 (FIX-LOG.md) into this
edition. No commit, no push. Logs + gate evidence:
`hidden_files/w47/scratch-delta-nl-de/` (DELTA-LOG.md, rebuild/, gates/).

- Location note: the canonical edition directory
  `production/2026-w47/2026-w47-nl-de/` did not exist when this delta
  started (only the fan-out staging copy at
  `production/2026-w47/fanout-nl/2026-w47-nl-de/`); it was created by a
  byte-identical copy (`diff -r` clean) of that staging edition, and the
  staging copy was left untouched. All delta work happened in the
  canonical directory.

- Pre-build finding (measured on the build-6 SVGs, before any edit):
  the D6/D7/D8/D10 orphan punctuation of the core does NOT occur in this
  edition — the German reader text reflows differently, and the full
  orphan sweep (both classes, CJK + Latin closers) was already 0/0 on
  all 8 pages. D6 bridge ends `Hilfsverben hebben/zijn.` on line 2 of 2,
  D7 ends `scoren treffen.` on line 3 of 3, D8 caption is 4 clean lines,
  D10 letters are 2 clean lines. The four w-syncs below are therefore
  structural (mechanism + locally scanned widths that reproduce the
  current clean wraps exactly); the rebuilt SVGs prove it — p3/p6/p7 are
  byte-identical to build 6. D9 and D11 were real defects here and are
  fixed for real.

- D6 (`bslib4.py` + `content34.py:78`): `Flow.para` / `Flow.bridge` take
  an optional `w` wrap-width override (default = column width, copied
  mechanism from core fix3); the HET PERFECTUM bridge passes
  `w=368.75` — width scan with this edition's own `wrap()` gives band
  312.0–425.5px for the current 2 lines, mid 368.75. Lines unchanged.
- D7 (`content7.py:19`): A2 VOETBALWOORDEN gloss bridge passes
  `w=412.25` — scan band 394.5–430.0px for the current 3 lines, mid
  412.25. Lines unchanged.
- D8 (`content56.py:143–144, 156`): `capcn_w = 374.25` — scan band
  358.5–390.0px for the current 4 lines, mid 374.25; used in both the
  box-height computation and the `p.para` call. Box height unchanged.
- D9 (`content8.py:75`): Q140 registry key `Ik maak een surprise met
  een gedicht.` → `Ik maak een surprise met een kort gedicht.`
  (Dutch target sentence, same in every edition). Re-exported
  registry + text.md: diff is exactly text.md line 415 (+5 bytes).
  Three-source check: registry key = text.md:415 answer = P8 node.
  `kort` is glossed in-edition by the Dutch article sentence
  (text.md:72: `kort is ook goed.`).
- D10 (`content7.py:91–92, 100`): `dt_zh_w = 353.25` — scan band
  300.0–406.5px for the current 2 lines, mid 353.25; used in both the
  `lh` computation and the `p.para` call. Box height unchanged.
- D11 (`content34.py:130`): HET PROGRAMMA box top reserve `62 → 89`
  (= 16 pad + 52 title block + 21 para y-offset). Facts wrap 3/3/3/2/3
  = 14 lines, as in the core. Box 611.0 → 638.0px, bottom 1202.6 →
  1229.6; last line `18:45 uur.` baseline 1209.49, margin +20.11px
  (was −6.89px). P3's SINTERKLAAS box (`content34.py:37`) untouched.

- Rebuild: `run.py` exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0; export exit 0; `webpdf.py`
  exit 0 (1,617,811 B < 7 MB); zero OVERFLOW / TOO WIDE warnings.
  SVG hashes vs build 6: only `p4-sport.svg` (D11) and `p8-toets.svg`
  (D9) changed; the other 6 are byte-identical.
- Gates (build 7): occlusion real audit 0 flags; p8 extract 150/150;
  p8 compare vs core CLEAN (JSON body: status CLEAN, missing [] extra []
  uncertain [], keydiff [137, 138] — the two translation items whose
  keys are reader-language by design, German here vs Chinese in core;
  pre-build keydiff was [137, 138, 140], D9 removed 140); 3-way
  registry/text.md/P8 compare 149/149 MATCH, only Q150 differs
  (open-writing exception); freeze baseline (core control) 8/8;
  edition self-freeze (clean-dir re-run) 8/8; print/web text posdiff 0
  msdiff 0 all 8 pages (tokens 832/813/719/720/795/729/890/2256);
  pdftotext print 46,739 B = web 46,739 B; P8 answer-zone min font
  10.12pt (≥ 10pt); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG
  audit clean. Orphan sweep (PIL + svglib advances, 1462 lines):
  class (a) 0 / class (b) 0 both methods, brute-force 0 closer-leading
  elements. Creambox: same 2 CREAM-BOTTOM flags as build 6, both
  pixel-probed 0 non-paper pixels in the 7px strip below the box
  bottom (true-ink clearances +6.8 / +7.5px) — false positives.
  Spill sweep: 0 spills; P4 box has no below hit at all.
- Visual: crops `crop-p4-programma.png` (`18:45 uur.` inside the box
  with clear margin), `crop-p8-q140.png` (`... met een kort gedicht.`),
  `crop-p3-d6.png`, `crop-p7-d7.png` all confirmed by eye.

- New SHAs (build 7, lowercase) — old build-6 SHAs kept as history:
  print `26faddf46acd8db2ec36999d5734ccff88835a554447b57526db5062f2c244ef`
  (12,669,889 B; was `f87d3f4d6518a10a42e9ebbc05d55eda09cb1b2ce2786aa695c4fb183341ab59`,
  12,669,890 B); web `74f10eefe797397b8e3e5eacc636208ebba2a73919848a1ad7c698043de97aa0`
  (1,617,811 B; was `44d1550835408e1df9bd414608ad7f507557f49f438ca61c5141ab7a7e0f3ab6`,
  1,617,821 B); text.md `ac56f6f91c644dc0d9a86c9d6d8748bca2721c507c255efd47ff612f2170117c`
  (46,219 B; was `7d6eee03b87a09d9319a999a1842e6252c7bb1959d6f57f6d40b431e967fd873`,
  46,214 B). Web PDF SHA/size are not reproducible run to run — only
  its text layer is compared (identical above).

## U+201C fix2 port (2026-11-11, build 8)

core-de 的 fix2（U+201C 在 Noto Sans CJK SC/TC 中为 1000/1000em 全宽，走 serif
分支改用 Newsreader 窄字形）只落在了 core-de，fan-out 副本从未同步。协调员全量
SVG census 发现 21 版共 44 处缺陷字形；本版 1 处，在 P1（`„Gruppensieg“:
erster Platz in der Gruppe, …`，19pt，`“` 1 处，font-family="Noto Sans CJK SC"）。
本次只 port 该 fix，不改任何内容，只动本版，不 commit、不 push。Logs：
`hidden_files/w47/scratch-gatefix-u201c-nlpt/`。

- **Port（只改 `svglib.py` 两处，md5 `78fdfbb0…90a782` → `ff8bc1f4…59355b6`）：**
  `_char_font` serif 分支后插入 fix2 块，条件扩展为三码点
  `if ch in ("\u201c", "\u201d", "\u2019")`（fontTools hmtx：U+201D/U+2019 在
  SC/TC 中同样 1000/1000em），类名按 fix2 方式推导、不拼字面量；
  `_pil` 前补 `_QUOTE_CLS`/`_PATH[("sans", …)]` 两行。验证：py_compile 通过；
  diff 仅含 port 的两块；反向打补丁精确复现 patch 前 md5。
- **Census（协调员方法：逐 `<text>` font-family × 三码点）：** 修前 1 缺陷
  （P1 `“` ×1，Noto Sans CJK SC）；修后 **0 缺陷**，该处已为 Newsreader；
  全版引号共 1 处。
- **重建 + 门禁（scratch 两独立构建）：** `run_build.py`（run.py exit 0，
  TOTAL 150；render.py exit 0）+ `freeze.py baseline` **8/8 字节一致**；
  `p8.py extract` noted set **150/150**，compare vs core-nl P8 **CLEAN**
  （keydiff [137, 138] — 与已发版实测完全相同，系按 Delta §所记的读者语
  翻译题键，非回归；P8 SVG 与已发版字节一致）；`occlusion_audit.py`
  selftest OK、**0 flags**；`spill_sweep.py` **0 SPILL**（34 OBSERVE）；
  `boxtitle_check.py` **0 DEFECT**。仅 `p1-voorpagina.svg` 变化，其余 7 版
  与 build 7 字节一致；仅 `cards/p1-voorpagina.png` 变化。
- **text.md 不变：** `2026-w47-nl-de.text.md` 46,226 字节，
  SHA-256 `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb`，
  与本轮 patch 前实测完全一致（只改渲染字形，不改字符）。注：本轮前该文件
  已是 46,226 B / 上述 SHA，与上文 build 7 所记（46,219 B）不符——该差异
  在本轮之前已存在，原因未查（非本轮改动）。
- **New SHAs (build 8, lowercase) — 旧 build-7 SHAs 保留于上文：**
  print `8e3ba9155d155db85f2b0c03f1595d920ceb8b3220d7652929f67b489f8b1412`
  （12,669,946 B）；web `0139ab963c4e61f534ef537ee17ff3899c029780577036696776055d35c3c360`
  （1,617,872 B；文字层 46,746 B）。注：本轮前磁盘上的印/网 PDF 实测为
  `4eacaa18…0188bb` / `a4303add…d5b7`，与上文 build 7 所记（`26faddf4…c244ef` /
  `74f10eef…97aa0`，12,669,889 B / 1,617,811 B）均不符——说明 build 7 之后
  印/网 PDF 被重建过而未更新 KIT；该差异在本轮之前已存在，非本轮改动。
  生产侧重哈希核对：印/网 SHA 与 scratch 构建一致，svg 8/8 一致，
  p1 卡片一致。
- **Files changed（本轮未提交）：** `svglib.py`（fix2 port）、`WEEKLY-KIT.md`
  （Files delivered 当前 SHA/尺寸 + 本节）。同步：`svg/*.svg`（8）、
  `De-Lucerna-VOL4-nl-de.pdf`、`De-Lucerna-VOL4-nl-de-web.pdf`、
  `cards/p1-voorpagina.png`。其余源文件未动。

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Noto Sans CJK instead of Newsreader; REDO in top-level production)

- **Why a redo:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) rebuilt the `fanout-nl/` COPY, not this top-level production dir, and deleted its build-copy — production still held pre-D5 PDFs (print `8e3ba915…`, web `0139ab96…`). This redo rebuilt from the current top-level build-8 sources in place. The copy's D5 SHAs (print `dc567b1a…` / 12,104,226 B) are superseded and do NOT describe production.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-de/baseline.txt`):** svglib md5 `ff8bc1f4678c…` (carries the build-8 fix2 port); print `8e3ba9155d155db85f2b0c03f1595d920ceb8b3220d7652929f67b489f8b1412` / 12,669,946 B; web `0139ab963c4e61f534ef537ee17ff3899c029780577036696776055d35c3c360` / 1,617,872 B; text `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb` / 46,226 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by the build-7 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 501 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader de` (mode latin), svglib md5 `ff8bc1f4678c…` → `968d05e480a512853d96d0eee9ec104c`. Installer reported "fix2 already present" (preserved, not re-added). Routing assert: FAILURES 0.
- **Ported core fixes (already in production before this rebuild):** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11). P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt applied in this rebuild (core-nl D5 defect, same line here).
- **Defects found by the gates (all D5-caused, same class: bold-caps box titles widen in Newsreader SemiBold) — conclusions reused from the first worker's copy build, re-verified on the top-level rebuild; all fixed by size only, text unchanged:**
  1. P1 `DE WEEK IN CIJFERS　IN ZAHLEN` +17.2px → `f.box` tsize 23 → 21 (`content12.py:43`).
  2. P1 `Agenda van de week　TERMINE DER WOCHE` +19.2px → 19 → 17pt (`content12.py:70`).
  3. P1 `IN HET KORT　KURZ GEMELDET` +24.7px → 24 → 22pt (`content12.py:132`).
  4. P2 `ZO ONTHOUD JE HET　MERK DIR` +11.0px → `f.box` tsize 23 → 22 (`content12.py:177`).
  5. P6 `VOOR OF TEGEN?　DAFÜR / DAGEGEN` +31.1px → 21 → 19pt (`content56.py:168`).
  6. P7 `HET WOORD　WORT DER WOCHE` +17.1px → 23 → 21pt (`content7.py:84`).
- **Gates (final rebuild, after the 6 fixes, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 7 (all U+3000); vs pre-D5 baseline: added CJK 0, added Latin strings 236 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (38 OBSERVE); `boxtitle_check.py` 0 DEFECT; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 228 → 228, footer slack 43.5px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0 (curly_total 1, in Newsreader); `census_quotes.py` 0 defective; text layer print = web = 46,657 bytes, word multiset diff 0; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `97420549c81ef63a0f77cfa985f84b89a79371f00ab15026e6d8f21ac2c4b4f5` (12,104,230 B); web `15a65413c7f7d5635066ba69c4cdf39c23547366ca364b247fffecfbeba5126a` (1,536,343 B). **text.md unchanged:** 46,226 B, sha256 `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `2361bedfd4d5f869ec193877cb80189a9ff0078fcf7bde71d88b1fbfe5a40abb` (1,536,341 B) — content-equivalent (pdftotext 46,657 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `15a65413c7f7d5635066ba69c4cdf39c23547366ca364b247fffecfbeba5126a`, 1,536,343 B).
- **Fix (2026-11-12, W47 nl repair, round 2):** PROOF-NOTE-2 item 1 (low) — P7 `BRIEVEN VAN LEZERS` German annotation lacked `best P8 texts`. `content7.py:91`: `Keine echten Briefe — Beispiel; Versprechen für VOL.5.` → `Keine echten Briefe oder besten P8-Texte — Beispiel; Versprechen für VOL.5.` (parallel to en `No letters or best P8 texts yet — an example; VOL.5 next.`; cf. fr `ni meilleur texte` / it `né migliori testi`; the Dutch core line `dt_nl` already says `beste pagina-8-teksten`, untouched). Layout: the reader line wraps 2 → 3 lines at `dt_zh_w` 353.25 (20pt sans); the box-height formula adapts, `P7 col3 ends` 1927.5 → 1956.5 — identical to en's shipped value. Print P7 verified (3 lines). Rebuilt: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0. Exporter trap (ru FIX-LOG §7) fired once: the fresh export dropped the `### ` prefix on line 287 (`VOOR OF TEGEN?　DAFÜR / DAGEGEN`) — backfilled by hand; final diff vs pre-fix text.md contains ONLY line 366. Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 46,678 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 0 marginal; `spill_sweep.py` 0 SPILL (38 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects (vs pre-fix baseline rebuilt in /tmp; P8 lines 228 → 228, footer slack 43.5px unchanged). D5 census (self-written SVG font-family direct count): D5_lat 0, curly-in-CJK 0. **New SHAs (lowercase, verified on production files):** print `9032021929da68607da8097bd50612aeec93f4b5de76d0e15e8757712172fb19` (12,104,245 B); web `fbf0c25a503a8fb532b60dc60d1b95b265a00659df1c69afb334b6bddf299795` (1,536,368 B); text.md `6825c35db04c62e1bec4f8f6e6a511597a17af0b02b17bc5260a560043575785` (46,247 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-de/`.
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install), `content12.py` (P2 head 25 → 23pt; 4 title sizes), `content56.py` (P6 title 21 → 19pt), `content7.py` (P7 title 23 → 21pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-de/` (`rebuild-1.log`, `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
