# FIX REPORT — Lucerna Weekly W46 NL family, Round 1 proofread defects

- Fix worker: subagent (depth 2/2), assigned Mon 2026-11-02 22:17:59 EST.
- Work performed: 2026-11-03 UTC (source edits, re-derivation, full re-render, re-gating).
- Issue: VOL.3, Mon 2026-11-09 – Sun 2026-11-15, 2026. Target NL × 11 reader natives (no nl-nl edition): de, en, es, fr, it, ja, ko, pt, ru, zh-cn, zh-tw.
- Authority: independent proofreader's Round 1 verdict (`hidden_files/w46/nl-proofread-gates/proofreader-verdict-round1.md`, ROUND 1 FAIL). This worker fixed ONLY the defects listed there and invented no additional changes.
- Method: every change at the source content files, full re-render from source, no SVG/PDF hand-edits. `.text.md` files regenerated from the source manuscript via `hidden_files/w46/export_text.py` (never hand-edited, never extracted from PDF). Web PDFs only via `tools/webpdf.py`. Local work only: `~/workspace/weekly-git` untouched, `index.json` untouched, nothing pushed, nothing inserted, nothing posted to Discord, no edition content dumped into chat.
- Seed record (delivered by the proofreader, not re-derived): VOL 3, 150 exercises (A2 47 / B1 72 / B2 31).
- **A FULL Round 2 independent proofread of all 11 editions still follows this report. This worker's re-gating does not replace it.**

## 1. Edition directories

The frozen-core directory `files/weekly-report-w46-nl-core/` IS the `2026-w46-nl-zh-cn` edition (per W45 precedent); there is no separate `weekly-report-w46-nl-zh-cn/` directory. Core build sources: `hidden_files/weekly-report-w46-nl-build/`. Fan-out build dirs: `hidden_files/weekly-report-w46-nl-<ed>-build/` (each with `content12/34/56/7/8.py`, `bslib4.py`, `svglib.py`, `run.py`, `render.py`, and a one-off `transform.py` mapping core Chinese explanation strings to the native language).

## 2. Fixes applied (all six defect groups, as specified)

### F-1 — Abstract closings, all 11 editions (BLOCKING)

Every `ABSTRACT.txt` closed with forbidden news framing ("learn Dutch from this week's news"). Each closing was rewritten to practice framing in the reader's native language; the rest of each abstract is verbatim, single-line, 0 ASCII quotes, topics + levels + 150 retained. Pre-fix copies preserved at `hidden_files/w46/nl-fix/before/ABSTRACT-<ed>.txt`. Trailing-newline state preserved (core keeps its trailing newline; the other 10 have none). Re-verified by file read after rewriting (2026-11-03 UTC): all single-line, 0 ASCII quotes, no forbidden framing string present, "150" present. Byte sizes: core 368, de 428, en 382, es 448, fr 454, it 405, ja 440, ko 427, pt 445, ru 667, zh-tw 339.

| Edition | Before (closing) | After (closing) |
|---|---|---|
| zh-cn (core) | `，150 道练习，适合学荷兰语的读者通过荷兰新闻学荷兰语。` | `，150 道以本周话题为素材的练习，适合学荷兰语的读者。` |
| de | `150 Übungen für Leser, die Niederländisch durch niederländische Nachrichten lernen.` | `150 Übungen zu den Themen dieser Woche für Leser, die Niederländisch lernen.` |
| en | `150 exercises for readers learning Dutch through Dutch news.` | `150 practice exercises on this week's topics for readers learning Dutch.` |
| es | `150 ejercicios para aprender neerlandés con las noticias neerlandesas.` | `150 ejercicios de práctica sobre los temas de esta semana para aprender neerlandés.` |
| fr | `150 exercices pour apprendre le néerlandais par les nouvelles néerlandaises.` | `150 exercices d'entraînement sur les thèmes de cette semaine pour apprendre le néerlandais.` (ASCII apostrophe, matching file style) |
| it | `150 esercizi per imparare l'olandese con le notizie olandesi.` | `150 esercizi di pratica sui temi di questa settimana per imparare l'olandese.` |
| ja | `150問の練習でオランダのニュースからオランダ語を学ぶ。` | `今週の話題を素材にした150問の練習。` |
| ko | `150개 연습 문제로 네덜란드 뉴스로 네덜란드어를 배웁니다.` | `이번 주 화제를 소재로 한 150개 연습 문제로 네덜란드어를 연습합니다.` |
| pt | `150 exercícios para aprender neerlandês com as notícias neerlandesas.` | `150 exercícios de prática sobre os temas desta semana para aprender neerlandês.` |
| ru | `150 упражнений для изучения голландского по голландским новостям.` | `150 практических упражнений по темам этой недели для изучающих голландский.` |
| zh-tw | `150 道練習題，用荷蘭新聞學荷蘭語。` | `150 道以本週話題為素材的練習題。` |

### F-2a — P2 EN JIJ box lone `。`, frozen-core source (BLOCKING)

- Rendered defect: `weekly-report-w46-nl-core/svg/p2-leven.svg`, element x=1473, y=1416.64, content exactly `。`, alone below `…寄给编辑部`.
- Source edit, core `hidden_files/weekly-report-w46-nl-build/content12.py` (2 occurrences: wrap-measure line 200 + paragraph line 206):
  - Before: `还是更爱看圣诞老人新闻`
  - After: `还是爱看圣诞老人新闻` (dropped `更`)
- Wrap simulation (cached-width simulator using the build's own `svglib.py` fonts, `hidden_files/w46/nl-fix/scratch/wrapsim.py`) verified before editing: 3 lines with lone `。` → 2 lines ending `…寄给编辑部。`.
- Verified in the final rendered SVG (all 11 editions, via re-derivation): no lone `。` at this spot; core P2 crop viewed (`nl-fix/crops/core-p2-enjij.png`): two clean lines ending `寄给编辑部。`. Full-frame core P2 card viewed: clean, no overflow.

### F-2b — P6 gloss lone `。`, frozen-core source (BLOCKING)

- Rendered defect: `svg/p6-verdieping.svg` in core and zh-tw, element x=1007, y=327.675, content exactly `。`, alone after `…de deskundige 专家/專家`. The core KIT §8(7) claim that this was fixed in the builder's pass is REFUTED — the orphan was still present in the shipped SVG. (Recorded in the core KIT fix record.)
- Source edit, core `hidden_files/weekly-report-w46-nl-build/content56.py` line 126 (gloss line):
  - Before: `de traditie 传统 · griezelen 扮鬼吓人 · de belangstelling 兴趣 · de achteruitgang 衰退 · de deskundige 专家。`
  - After: `de traditie 传统 · griezelen 吓人 · de belangstelling 兴趣· de achteruitgang 衰退 · de deskundige 专家。`
  - Two changes, both deliberate and disclosed: (a) the `griezelen` gloss shortened to `吓人` — the wording the zh-tw edition of this family already used (a precedent within this family); (b) one separator space tightened (`兴趣· de`). Shortening the gloss alone was simulated and does NOT fix the wrap (line 3 stays 393.6px, `。` still orphaned). Single-character glosses (`衰`/`趣`) were rejected as weak glosses; dropping the `de` article was rejected as it would change the Dutch headword.
- Result: gloss wraps to 3 lines ending `衰退 · de deskundige 专家。`. Verified in final SVGs of core and zh-tw, and that no other edition shows the orphan. Core P6 gloss crop viewed (`nl-fix/crops/core-p6-gloss.png`): 3 lines ending `专家。`, tight `兴趣·` middot visible. Full-frame core P6 and zh-tw P6 cards viewed: clean.

### E-1 — P3 bridge stranded `3.`, fr + pt (BLOCKING)

- Rendered defect: element x=989, y=1984.225, content exactly `3.`, alone on line 2. FR: `Calcule: réponds avec les chiffres de la page` / `3.`; PT: `Calcula: responde com os números da página` / `3.`.
- Fix in each edition's one-off `transform.py` (new-string), re-derived from the fixed core:
  - FR before: `Calcule: réponds avec les chiffres de la page 3.` → after: `Calcule: réponds par les chiffres de la page 3.` (simulated one line, 430.7px ≤ 434).
  - PT before: `Calcula: responde com os números da página 3.` → after: `Calcula: responde com números da página 3.` (simulated one line, 427.3px ≤ 434).
- Verified: bridge is a single line in the final SVGs (FR x=989, y=1954.5; PT single line) and visually on both P3 cards (full frame + crops `nl-fix/crops/fr-p3-bridge.png`, `pt-p3-bridge.png`): single line, exercises 43/44 follow with normal spacing, no overlap.

### E-2 — P6 chart explanation line starts with `。`, zh-tw only (BLOCKING)

- Rendered defect: element x=1473, y=685.28: `。問題：11 月 11 日前後你做什麼？（100 位年…`.
- Fix in zh-tw `transform.py` (chart caption `capcn` new-string), exact Traditional mirror of the core caption:
  - Before: `練習數據：僅供練習的虛構數字，不是真實調查。問題：…`
  - After: `練習數據：虛構數字，僅供練習，非真實調查。問題：…`
- Simulated wrap: line 1 ends with `。`, line 2 starts `問題：`. Verified in the final SVG (lines: `練習數據：虛構數字，僅供練習，非真實調查。` / `問題：11 月 11 日前後你做什麼？（100 位年輕` / `人）`) and visually (full-frame zh-tw P6 + crop `nl-fix/crops/zhtw-p6-chart.png`): no line starts with `。`.

### E-3 — P8 H-intro lone `。`, zh-tw only (BLOCKING)

- Rendered defect: `svg/p8-toets.svg`, element x=1451, y=592.495, content exactly `。`, alone after `寫作題（沒有唯一答案）；範文（89 詞）見下` (core fits one line).
- Fix in zh-tw `transform.py` (H-intro `expl` new-string):
  - Before: `寫作題（沒有唯一答案）；範文（{NWORDS} 詞）見下。`
  - After: `寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。`
- Simulated one line, 416.8px. Verified in the final SVG (single line `寫作題（無唯一答案）；範文（89 詞）見下。`, x=1451, y=562.77) and visually (full-frame zh-tw P8 + crop `nl-fix/crops/zhtw-p8-h.png`): single line, item 150 follows cleanly.

### Re-derivation of the fan-outs (F-2 core-source fixes require re-deriving the whole family)

- Reproducibility was proven first (2026-11-03 UTC, `hidden_files/w46/nl-fix/scratch/derive-test/`): copying the (then unfixed) core build + an edition's `transform.py` and running it reproduces the shipped build byte-identically for EN and FR (FAILED: 0), and for zh-tw except the expected TC `svglib.py` overlay. Fan-out `transform.py` files are one-shot, run-once scripts (re-running doubles the badge insert).
- Method: fix core sources → update all 10 `transform.py` old-strings to the new core strings (F-2a: 1 occurrence each; F-2b gloss: 1 occurrence each, gloss-line only — the separate P8 note `"griezelen = 扮鬼吓人"` reps were deliberately NOT changed) → re-derive all 10 from the fixed core (`hidden_files/w46/nl-fix/scratch/rederive.py`; logs `transform-<ed>.log`, diffs `rederive-diff-<ed>.txt`). All 10 transforms: FAILED: 0 (de 335, en 335, es 292, fr 292, it 330, ja 334, ko 332, pt 334, ru 336, zh-tw 313 replacements). JA/JP and ZH-TW TC `svglib.py` overlays re-applied from the shipped builds.
- Diff vs pre-fix build sources: 7 editions byte-identical (de, en, es, it, ja, ko, ru); FR exactly 1 line (bridge); PT exactly 1 line (bridge); zh-tw exactly 3 lines (gloss, capcn, E-3 expl). Re-derived sources installed into the live build dirs and verified `live==staging` for all 10. Core source diff vs backup is exactly `content12.py` (2 lines) + `content56.py` (1 line). Pre-fix build dirs backed up at `hidden_files/w46/nl-fix/scratch/build-before/`.

### Coordinator rulings applied

- O-1 (core badge): ACCEPTED as non-defect. The core carries the pairing via subtitle/strip/footers, identical to the shipped W45 core precedent. No badge element added. The core KIT §1 badge-claim wording is corrected in the core KIT fix record to describe the actual furniture (subtitle/strip/footers), noting the W45 precedent.
- O-2 (KO single-syllable orphans `가.`/`요.`): precedent-matched, non-blocking — no action. (The 2 accepted orphans remain in the final KO SVGs.)
- O-3/O-4/O-5 (JA typographic artifacts; deliberate P1 bridge shortening; PT/RU Dutch `(Pagina N)` tags): NOT defects — no action.
- Record-only KIT inaccuracies: JA freeze total 3,377 → measured 3,341 (corrected in the JA KIT fix record); RU web-PDF text bytes 55,344 (stale) → 55,313 measured (corrected in the RU KIT fix record; that KIT's §9 already stated 55,313). No KIT was churned for numbers alone beyond the KITs already touched.

## 3. Re-render

Driver `hidden_files/w46/nl-fix/scratch/build_all.py`; per-edition logs `hidden_files/w46/nl-fix/build-<ed>.log` (run.py + render.py + webpdf.py + export_text.py; H1 titles preserved verbatim from each existing `.text.md`). Builds ran 2026-11-03 ~03:27–04:17 UTC (slowed by concurrent other-family renders on the same VM; those were not interfered with).

Every edition: TOTAL 150; by level A2 47 / B1 72 / B2 31; by page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.

## 4. Lone-`。` / stranded-number scan (all pages, all editions)

Script `hidden_files/w46/nl-fix/scratch/scan_orphans.py`, results `hidden_files/w46/nl-fix/orphan-scan.json` (2026-11-03 UTC, final SVGs, all 8 pages, all 11 editions):

- **0 lone-`。` elements** in every edition.
- **0 line-start-`。` elements** in every edition.
- **Exactly 142 exact `N.` elements in every edition**, all at stem x-coordinates (137/599/1061/1523) — **0 stranded numbers** (FR/PT previously had 143, with one at x=989; that element is gone).
- KO retains the 2 accepted `가.`/`요.` orphans per ruling O-2 (not `。` orphans, not counted above).

## 5. Re-gate results

### Freeze (`tools/freeze.py diff`; JSONs `hidden_files/w46/nl-fix/freeze-*.json`)

| Edition | Result |
|---|---|
| core (self) | +0/−0 all pages, added CJK 0, exit 0. Per-page CJK totals [196, 220, 141, 136, 217, 184, 379, 1144]. P2 220 (was 221: F-2a removed one char) and P6 184 (was 186: F-2b removed two) reconcile exactly with the fixes. |
| de, en, es, fr, it, pt, ru | strict-CJK: exit 0, added CJK 0, edition CJK total 0 |
| ja | exit 0, added CJK 3,341 — all kana/kanji + Japanese punctuation (327 distinct chars; no other scripts). Matches the proofreader's Round 1 measurement (3,341), not the KIT's stale 3,377. |
| ko | exit 0, added CJK 3,581, 0 Han characters (319 Hangul + `『』` brackets only). Matches Round 1 (3,581). |
| zh-tw | exit 0, added CJK 1,238 (Round 1: 1,241; −3 reconciles: caption −2, H-intro −1), 0 simplified-only characters (curated simplified-only spot-list scan of all SVG texts: 0 hits; Traditional counterparts present). |

### P8 (`tools/p8.py`; JSONs `hidden_files/w46/nl-fix/p8-*.json`)

- Core extract: noted set 150/150.
- All 10 fan-out compares: **CLEAN, core 150 = edition 150, missing=[], extra=0, keydiff=[137, 138]** (legal re-aims). (First compare attempt failed with FileNotFoundError because `--target` means the TARGET language (nl), not the reader native; re-ran with explicit `--core-p8`/`--edition-p8` paths.)

### Occlusion (`tools/occlusion_audit.py`; JSONs `hidden_files/w46/nl-fix/occlusion-*.json`, `occlusion-*-vs-core.json`)

- Selftest OK (all 6 planted classes fired, clean controls silent). Edition-alone runs: 0 flags in all 11. `--core` NEW-vs-core runs: 0 new flags in all 10 fan-outs. Exit 0 throughout.

### Counts re-measured (`count_check_fix.py`, adapted from the proofreader's `count_check.py` with outputs repointed to `nl-fix/`; `counts.json`/`counts.log`)

Identical in all 11 editions: text.md 142 bracketed items + 8 range-header items = 150; per-page standalone [10, 14, 18, 18, 18, 18, 12, 34] + ranges = [10, 18, 18, 18, 18, 18, 12, 38]; levels from text.md 43/72/27 + 4 A2 + 4 B2 from the range headers = A2 47 / B1 72 / B2 31; SVG stems 142, no missing, no dupes (the "missing" [25–28, 141–144] in the raw script output are the range-header items, as in Round 1).

### Gloss, chart, P7, essay (supplementary; `gloss.json`/`gloss.log`, `chart-p7-pdf.log`)

- Gloss counts P2–P6 = 6/5/5/5/5 in every edition; identical Dutch headwords in order. Core and zh-tw P6 glosses now 3 lines (were 4).
- P6 chart bars measured from SVG rects: widths 160/100/80/60 (values 40/25/20/15), height 18, fill `#3e4c2a`, at x=1473, y=304/362/420/478 — identical in every edition.
- P7: 8/8 golden sentences verbatim (whitespace-normalized) on P7 in all 11 editions; page tags in order Pagina 1,1,2,3,4,5,6,6 in all 11. (IT also carries a pre-existing footer `Pagina 7 di 8` — page furniture, not a quote tag.)
- Model essay: 89 words (90 tokens including the `Tekstmodel:` label) in core, zh-tw, en — untouched by the fixes, verified as specified.
- Chart-answer arithmetic spot-verified from the P8 answers block: 83. 40 / 84. 25 / 85. 60 = 40+20 / 86. 15 / 87. 100 = 40+25+20+15.

### PDFs (web vs print; `chart-p7-pdf.log`)

- All 11 web PDFs: 8 pages, 1462.5×2025 pts, ≤7 MB, pdftotext bytes > 0.
- Web-vs-print extracted text: **0 diff tokens in all 11 editions** (identical text byte counts).
- Card dimensions: 88/88 cards at 1950×2700.

### Visual checks (every changed page at full frame)

| Page | Check | Result |
|---|---|---|
| P2 core | full frame + EN JIJ crop | Clean: 2 lines ending `寄给编辑部。`, no overflow |
| P6 core | full frame + gloss crop | Clean: gloss 3 lines ending `专家。`, chart intact |
| P6 zh-tw | full frame + chart + gloss crops | Clean: caption line 1 ends `。`, line 2 starts `問題：`; gloss 3 lines ending `專家。` |
| P3 fr | full frame + bridge crop | Clean: single-line bridge, exercises 43/44 normal spacing |
| P3 pt | full frame + bridge crop | Clean: single-line bridge, exercises 43/44 normal spacing |
| P8 zh-tw | full frame + H crop | Clean: H-intro single line ending `見下。`, item 150 follows cleanly |

Checked-and-clear (not a defect): on zh-tw P8, the F-options column and the model-essay column abut closely in downscaled views. SVG coordinates measured: F option b at x=1023, y=878.05 (23pt, ends ≈x1383); essay line at x=1451, y=872.6 (14.5pt). No overlap; identical coordinates in core — pre-existing layout, not caused by any fix. Occlusion audit 0 flags confirms.

## 6. Final per-edition file inventory

Sizes in bytes. `.text.md` from build logs; web/print PDF sizes and pdftotext bytes measured 2026-11-03 UTC on the final artifacts.

| Edition | `.text.md` | Web PDF | Web pdftotext | Print PDF |
|---|---|---|---|---|
| zh-cn (core) | 32,305 | 1,325,912 | 44,394 | 18,472,783 |
| de | 38,262 | 774,922 | 46,586 | 6,644,100 |
| en | 37,739 | 768,075 | 45,597 | 6,604,762 |
| es | 37,510 | 776,057 | 46,675 | 6,642,975 |
| fr | 37,630 | 772,213 | 46,876 | 6,626,777 |
| it | 39,093 | 768,440 | 46,429 | 6,641,175 |
| ja | 33,220 | 1,375,362 | 47,973 | 19,287,942 |
| ko | 33,922 | 1,083,984 | 47,853 | 11,146,265 |
| pt | 38,265 | 781,803 | 46,689 | 6,668,637 |
| ru | 39,651 | 809,219 | 55,313 | 6,567,209 |
| zh-tw | 32,320 | 1,615,015 | 44,455 | 18,512,823 |

File names: print `De-Lucerna-VOL3[-<SUFFIX>].pdf`, web `De-Lucerna-VOL3[-<SUFFIX>]-web.pdf` (suffixes DE/EN/ES/FR/IT/JA/KO/PT/RU/ZH-TW; core has none), text `2026-w46-nl-<ed>.text.md` (core: `2026-w46-nl-zh-cn.text.md`), plus `svg/` (8 SVGs), `cards/` (8 PNGs), `WEEKLY-KIT.md`, `ABSTRACT.txt` in each edition dir.

## 7. Records written

- Fix record appended to all 11 KITs (`files/weekly-report-w46-nl-*/WEEKLY-KIT.md`, section "Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)") with defect/fix quotes and re-gate evidence, including the core §1 badge-claim correction, the §8(7) refutation, and the JA/RU record corrections.
- This report: `hidden_files/w46/nl-fix/FIX-REPORT.md`.
- Evidence under `hidden_files/w46/nl-fix/`: `build-*.log`, `transform-*.log`, `rederive-diff-*.txt`, `freeze-*.json`, `p8-*.json`, `occlusion-*.json`, `occlusion-*-vs-core.json`, `orphan-scan.json`, `counts.json`/`counts.log`, `gloss.json`/`gloss.log`, `chart-p7-pdf.log`, `before/` (pre-fix abstracts + SVG text dumps), `crops/` (zone crops), `scratch/` (build backups, re-derivation staging, `wrapsim.py`, `build_all.py`, `run_gates.py`, `scan_orphans.py`, `rederive.py`, adapted check scripts).

## 8. Fixes NOT applied as specified

None. All six defect groups (F-1, F-2a, F-2b, E-1, E-2, E-3) were applied as specified, with the wording choices documented in §2 (F-2b gloss shortening + separator tightening; E-1 bridge rewordings; E-2/E-3 zh-tw rewordings). No new defects were found by this worker's own checks (occlusion 0, p8 CLEAN, orphan scan clean) — but this worker is not the proofreader, and Round 2 must still adjudicate.

## 9. Open items for the coordinator / Round 2 proofreader

- Round 2 independent proofread of all 11 editions is still required before shipping (proofread-until-zero gate).
- Nothing was pushed, inserted, or posted. The coordinator inserts serially per SOP.
