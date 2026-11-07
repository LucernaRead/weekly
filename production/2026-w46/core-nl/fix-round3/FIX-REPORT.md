# FIX REPORT — Lucerna Weekly W46 NL family, Round 2 proofread defects (N-1/N-2)

- Fix worker: subagent (depth 2/2), assigned Mon 2026-11-02 23:48 EST.
- Work performed: 2026-11-03 UTC (source edits, re-derivation, full re-render, re-gating, residue sweep, KIT corrections).
- Issue: VOL.3, Mon 2026-11-09 – Sun 2026-11-15, 2026. Target NL × 11 reader natives (no nl-nl edition): de, en, es, fr, it, ja, ko, pt, ru, zh-cn, zh-tw.
- Authority: independent proofreader's Round 2 verdict (`hidden_files/w46/nl-proofread-gates-round2/proofreader-verdict-round2.md`, ROUND 2 FAIL on N-1/N-2; all Round 1 fixes CONFIRMED). This worker fixed ONLY N-1 and N-2 plus the three stale KIT lines the verdict flagged as PARTIAL, and invented no additional changes.
- Method: every change at the source content files, full re-render from source, no SVG/PDF hand-edits. `.text.md` files regenerated from the source manuscript via `hidden_files/w46/export_text.py` (never hand-edited, never extracted from PDF). Web PDFs only via `tools/webpdf.py`. Local work only: `~/workspace/weekly-git` untouched, `index.json` untouched, nothing pushed, nothing inserted, nothing posted to Discord, no edition content dumped into chat.
- **A FULL Round 3 independent proofread of all 11 editions still follows this report. This worker's re-gating does not replace it.**

## 1. Edition directories

The frozen-core directory `files/weekly-report-w46-nl-core/` IS the `2026-w46-nl-zh-cn` edition (per W45 precedent); there is no separate `weekly-report-w46-nl-zh-cn/` directory. Core build sources: `hidden_files/weekly-report-w46-nl-build/`. Fan-out build dirs: `hidden_files/weekly-report-w46-nl-<ed>-build/` (each with `content12/34/56/7/8.py`, `bslib4.py`, `svglib.py`, `run.py`, `render.py`, and a one-off `transform.py` mapping core Chinese explanation strings to the native language). Work dir: `hidden_files/w46/nl-fix-round3/` (before-snapshot, logs, gates, scratch, crops, FIX-REPORT.md, residue-candidates.txt).

## 2. Fixes applied (both blocking defects, as specified)

### N-1 — core (zh-cn) P8, item 103 note: English word `arrival` (BLOCKING)

- Rendered defect: `weekly-report-w46-nl-core/svg/p8-toets.svg`, text element x=989, y=2210.12: `103. B — 入城式是圣诞老人的隆重 arrival`. Also in `2026-w46-nl-zh-cn.text.md` item 103. Key B correct; only the note wording defective.
- Source edit, core `hidden_files/weekly-report-w46-nl-build/content7.py` line 24 (the build source the P8 note is generated from — the P8 answer list is registry-generated from the same `a.ex(...)` entries):
  - Before: `a.ex("A2", "单选", "B", "入城式是圣诞老人的隆重 arrival",`
  - After: `a.ex("A2", "单选", "B", "入城式是圣诞老人的隆重到来",`
- Wording check: `入城式是圣诞老人的隆重到来` reads correctly in Chinese ("the intocht is Sinterklaas's grand arrival") and matches the note style (no final `。`, as in the original). The zh-tw mirror `慶典進城` alternative was not needed.
- Fit measured BEFORE editing with the build's own `svglib.py` (`text_w`/`wrap`, serif, 13.5pt, column width 434): old line 253.5px → new line 233.6px, still exactly 1 line, no re-wrap, no orphan, no overflow. The `庆典进城` alternative measures identically (233.6px) and was not used.
- Verified in the final rendered SVG: single text element `103. B — 入城式是圣诞老人的隆重到来`. Zone crop viewed (`nl-fix-round3/crops/core-p8-item103.png`): one clean line aligned with items 102/104. Full-frame core P8 card viewed: clean, no overflow.

### N-2 — fr P8, item 137 note: English verb `Compare` (BLOCKING)

- Rendered defect: `weekly-report-w46-nl-fr/svg/p8-toets.svg`, text elements x=1451, y=1930.48/1945.04 (two lines): `137. Le journal de Sinterklaas passe chaque jour à 18 h 00. —` / `Compare avec l'article page 3`. Also in `2026-w46-nl-fr.text.md` item 137. The translation key itself was correct; only the note prefix was English (copied from the EN note).
- Source edit, FR one-off `transform.py` line 284 (the FR source/transform new-string — NOT an SVG patch):
  - Before: `rep('content8.py', '"对照第 3 版文章"', '"Compare avec l\'article page 3"')`
  - After: `rep('content8.py', '"对照第 3 版文章"', '"Comparez avec l\'article page 3"')`
- Fit measured BEFORE editing with the FR build's own `svglib.py` (`text_w`/`wrap`, serif, 13.0pt — the FR P8-answers size per the transform — column width 434): still exactly 2 lines with the SAME break point (line 1 `137. Le journal de Sinterklaas passe chaque jour à 18 h 00. —`, 380.8px; line 2 `Comparez avec l'article page 3`, 189.3px ≤ 434), no orphan line, no overflow. The `À comparer avec l'article page 3` alternative was simulated and REJECTED: it re-breaks the lines (`À` moves to line 1).
- Verified in the final rendered SVG: line 1 + line 2 `Comparez avec l'article page 3` (x=1451). Zone crop viewed (`nl-fix-round3/crops/fr-p8-item137.png`): two clean lines, item 138 follows cleanly. Full-frame fr P8 card viewed: clean, no overflow.

### Re-derivation of the fan-outs (N-1 core-source fix requires re-deriving the whole family)

- Method (same as Round 1, `nl-fix-round3/scratch/rederive3.py`): copy the fixed core build + each edition's `transform.py` into staging, run the transform once, diff staging vs the pre-fix build backup, then install the staged sources into the live build dirs and verify `live==staging` (0 diff lines, all 10 editions).
- Transform old-strings updated FIRST: all 10 `transform.py` files, exactly 1 occurrence each — the item-103 rep old-string `"入城式是圣诞老人的隆重 arrival"` → `"入城式是圣诞老人的隆重到来"` (new-strings unchanged). Without this update the rep would have FAILED and the defective Chinese string would have survived into the derived builds.
- All 10 transforms: FAILED: 0, with TOTAL replacement counts IDENTICAL to Round 1 (de 335, en 335, es 292, fr 292, it 330, ja 334, ko 332, pt 334, ru 336, zh-tw 313). JA/JP and ZH-TW TC `svglib.py` overlays re-applied from the shipped builds.
- Diff vs pre-fix build sources: 9 editions byte-identical in all `.py` files; FR exactly 1 line (`content8.py` line 69, the N-2 note). Core source diff vs backup: exactly `content7.py` line 24. Pre-fix build sources backed up at `hidden_files/w46/nl-fix-round3/before/build-before/` (`.py` files; `assets/` dirs excluded from the backup and from the diff).
- No `arrival` residue remains in any build source; no `Compare avec` residue remains in the FR transform (verified by grep over all 11 build dirs). In the rendered SVGs, `arrival` now occurs ONLY in the EN edition (14 occurrences, all legitimate native English strings, e.g. item 103 `The intocht is Sinterklaas's festive arrival`), and `Compare` occurs only as EN `Compare with…` and FR `Comparez…`.

### KIT stale-line rewrites (Round 2 verdict item 5 — non-blocking, recommended; all three applied, each value verified programmatically before writing)

1. Core KIT §1 badge wording — before: `Pairing badge on P1 (subtitle slot) + pairing footer every page (…)`. After (rewritten in §1 itself): `Pairing carried by the P1 subtitle slot + the pairing strip/footer on every page (…) — no distinct badge element, identical to the shipped W45 core precedent (Round 3 KIT correction; see the Round 3 fix record below).` The Round 1 fix-record gloss quoting the old wording is historical and is left in place; the Round 3 core record notes that §1 itself now carries the correction.
2. JA KIT freeze total — before: `added CJK 3,377 chars` (stale, in §7) and the Round 1 record gloss stating the measured total was 3,341. Programmatic re-measurement on the FINAL Round 3 artifacts gives **3,340**, not 3,341: `freeze.py` counts added CJK as the edition-minus-core CJK multiset, and the N-1 fix added 到 to the core P8 multiset, netting one fewer added char for JA (whose item-103 note uses 到着). Both lines were rewritten to 3,340 with this reconciliation stated in-line. The Round 1 re-gate evidence line in the same KIT still states 3,341 — that is the historical Round 1 measurement on the Round 1 artifacts and was deliberately left unchanged. Writing 3,341 into §7 would have been wrong on the current artifacts; the tasked value (3,341) was Round 2's measurement, superseded by re-measurement as the task's own verification rule requires.
3. RU KIT §7 web PDF figures — before: `(809,351 bytes, 55,344 text bytes)`. After (verified programmatically on the final artifacts: `os.path.getsize` + `pdftotext`): `(809,218 bytes, 55,313 text bytes)`. Note: web-PDF file sizes drift by ±1 byte between rebuilds from byte-identical sources (RU: 809,219 in Rounds 1–2 → 809,218 now, with identical extracted text); the text-byte figure (55,313) is the stable measure. RU KIT §9 still states 809,219 bytes — left untouched as out of the tasked scope; flagged here as an observation for Round 3 (same ±1 drift class).

## 3. Residue sweep (mandatory second independent pass — method + complete candidate list)

Scope: ALL 11 editions' rendered SVG text (all 8 pages), all `.text.md` explanations are covered via the same SVG note strings, plus all 11 `ABSTRACT.txt` files. The sweep script is `nl-fix-round3/scratch/residue_sweep3.py` (raw log: `nl-fix-round3/logs/residue-sweep.log`, 1,803 lines); the deduplicated complete candidate list regenerated from the final artifacts is `nl-fix-round3/residue-candidates.txt` (589 lines) and is reproduced as Appendix A of this report. Four passes, all over rendered text (no build-source inference):

- **Pass A — English-wordlist scan (full text).** Every SVG text element in every edition was tokenised and matched against a curated list of English words that are NOT Dutch words (plus the two known residue tokens). Raw hits: 1,212. Of these, 615 are the EN edition's own native layer (expected). The remaining hits were reduced to the **A-remainder**: strings present in a non-EN edition but absent from the core (68 distinct strings; core itself contributes 29 distinct frozen-Dutch strings). Adjudication of every A-remainder string: ALL are (i) frozen Dutch furniture containing `week`/`of` (e.g. `De grote toets van de week`, `Agenda van de week`), (ii) native-language homographs — DE `also`/`so` (German), FR `arrive`/`arrivée` (French verb/noun: `Sinterklaas arrive`, `l'arrivée festive`), IT `all'ordinale`/`all'11` (tokeniser splitting Italian elisions `all'…`), or (iii) the fixed N-2 string itself (`Comparez avec l'article page 3`, now correct French). NO further English residue. The EN edition's remainder (197 distinct strings) is its own English explanation layer; its vice-versa check is Pass B3.
- **Pass B — Added-string scan (core-vs-edition multiset diff).** Per page, the edition-only strings (= the native explanation layer + furniture) were checked against the EN edition's added-string vocabulary (minus an allowlist of Dutch/proper-name/furniture tokens and minus every token attested in the core). Raw hits: 259 → **240 distinct strings** (de 50, es 21, fr 94, it 19, pt 56; ja/ko/ru/zh-tw: 0 — their added strings contain no Latin-script EN-vocab tokens). Adjudication of every distinct string: ALL are native-language words, proper names, quoted Dutch headwords/terms the issue itself glosses, or established loanwords — grouped: DE `Lies` (read!), `Was`, `an`, `her`, `so`, `Name/Verb/Plural/Tradition/Reporter`, `TEXT/TEST` (German furniture spellings), `Nov.`, `Martin`, `Malaysia`; ES `no`, `real`, `original`, `ordinal`, `plural`, `club`, `QUIZ`, `final`, `Serbia`; FR `page`, `article`, `Note`, `Attention`, `tradition`, `expert`, `phrase`, `condition`, `question`, `section`, `expression`, `festive`, `programme`, `match`, `international`, `reporter`, `points`, `maritime`, `on` (French pronoun), `Martin`, `CULTURE/TEST/PHRASES` (French furniture); IT `QUIZ`, `reporter`, `Focus`, `Serbia`, `I/i` (Italian articles), `all` (elision artifact), `TEST`; PT `do` (de+o), `no` (em+o), `Complete` (Portuguese imperative — Round 1 precedent), `final`, `real`, `original`, `ordinal`, `plural`, `WEEKBLAD` (frozen Dutch masthead word). NO further residue. (The full 240 strings are in Appendix A.)
- **Pass B2/B3 — Cross-language function-word scan.** Distinctive function-word lists for FR/DE/ES/IT/PT/EN were run over added strings of every other edition (238 deduplicated hits), and over the EN edition's added strings for non-English words (10 hits). Adjudication: ALL are shared homographs or quoted Dutch — `als` (Dutch conjunction in P7 grammar content, 9–10 per edition), `alle`/`week` (frozen Dutch furniture `alle antwoorden` / `van de week`), `des` (German genitive in DE), `pas` (Dutch clinic heading `PAS OP!`, all 11 editions), `para/por/esta/está/mais/quando/con/una/son/qui/das` (Iberian/Romance shared words used in their own language), `une` (Spanish verb form `se une`), `also` (German), `festive/programme` (French, in FR), `alle` (Dutch furniture, in EN). B3 (EN): only Dutch quoted grammar terms (`als`, `als-clause`), the `PAS OP!` clinic heading, and Dutch page furniture. NO further residue.
- **Pass C — Script-leak scan (full text).** Cyrillic outside RU: 0. Kana outside JA: 0. Hangul outside KO: 0. CJK outside JA/KO/zh-cn/zh-tw: 0. zh-tw simplified-only spot-list scan (`simp_check.py`): 0 hits, Traditional counterparts present. KO Han characters: 0 (freeze breakdown: 3,571 Hangul + 10 CJK punctuation).
- **Pass D — ABSTRACT.txt scan.** All 11 abstracts read in full; no English-word flags in non-EN abstracts and no non-native function-word flags in the EN abstract. The 4 script flags are all legitimate: JA (kana), KO (Hangul), RU (Cyrillic) abstracts in their native scripts, and zh-tw's use of the shared CJK separator `・` (U+30FB).
- **Result: NO third same-class candidate was found. Nothing further was fixed.** The two Round 2 defects were the only native-language residue in the family. (For the avoidance of doubt: the Round 2 proofreader's adjudicated keeps — FR `festive`/`article`/`attention`, ES/PT `original`, PT `Complete`, Dutch body words `is`/`in`/`of`/`over`, Dutch `week` — were all re-found by this sweep and re-adjudicated clean on the same grounds.)

## 4. Re-render

Driver `nl-fix-round3/scratch/build_all3.py` (adapted from the Round 1 driver: same commands, outputs repointed); per-edition logs `nl-fix-round3/logs/build-<ed>.log` (run.py + render.py + webpdf.py + export_text.py; H1 titles preserved verbatim from each existing `.text.md`).

Every edition: TOTAL 150; by level A2 47 / B1 72 / B2 31; by page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings in any build log.

## 5. Re-gate results

### Freeze (`tools/freeze.py diff`; JSONs `nl-fix-round3/gates/freeze-*.json`)

| Edition | Result |
|---|---|
| core (self) | +0/−0 all pages, added CJK 0, exit 0. Per-page CJK totals [196, 220, 141, 136, 217, 184, 379, 1146]. P8 1146 (was 1144: N-1 added `到来`, +2 CJK) reconciles exactly with the fix. |
| de, en, es, fr, it, pt, ru | strict-CJK: exit 0, added CJK 0, edition CJK total 0 |
| ja | exit 0, added CJK 3,340 (327 distinct; kana/kanji + Japanese punctuation; no other scripts). −1 vs Round 2's 3,341 reconciles with N-1 (core multiset gained 到; see §2 KIT item 2). |
| ko | exit 0, added CJK 3,581, 0 Han characters (Hangul + CJK punctuation only). Matches Round 1/2 (3,581). |
| zh-tw | exit 0, added CJK 1,238 (matches Round 2), 0 simplified-only characters (spot-list scan). |

### P8 (`tools/p8.py`; JSONs `nl-fix-round3/gates/p8-*.json`)

- Core extract: noted set 150/150.
- All 10 fan-out compares: **CLEAN, core 150 = edition 150, missing=[], extra=0, keydiff=[137, 138]** (legal re-aims, adjudicated in Round 2). Keys 150/150 unchanged — notes only, as specified (p8.py set-equality is the cross-check; semantic key verification was Round 2's, and no key string was touched by these fixes).

### Occlusion (`tools/occlusion_audit.py`; JSONs `nl-fix-round3/gates/occlusion-*.json`, `occlusion-*-vs-core.json`)

- Selftest OK on every run (all 6 planted classes fired, clean controls silent). Edition-alone runs: 0 flags in all 11. `--core` NEW-vs-core runs: 0 new flags in all 10 fan-outs. All 21 JSONs verified programmatically (`flag_count=0`, `new_flag_count=0`). Exit 0 throughout.

### Counts, orphan scan, gloss, chart, P7, essay, PDF

- Counts (`count_check_fix3.py`, `counts.json`/`counts.log`): identical in all 11 editions — text.md 142 bracketed items + 8 range-header items (25–28, 141–144) = 150; per-page standalone [10, 14, 18, 18, 18, 18, 12, 34] + ranges = [10, 18, 18, 18, 18, 18, 12, 38]; levels from text.md 43/72/27 + 4 A2 + 4 B2 from the range headers = A2 47 / B1 72 / B2 31; SVG stems 142, no missing, no dupes.
- Orphan scan (`scan_orphans3.py`, `orphan-scan.json`): **0 lone-`。` elements, 0 line-start-`。` elements, exactly 142 exact `N.` elements in every edition**, all at stem x-coordinates (137/599/1061/1523) — 0 stranded numbers. KO retains the 2 accepted `가.`/`요.` orphans per ruling O-2.
- Gloss (`gloss_check_fix3.py`, `gloss.json`/`gloss.log`): counts P2–P6 = 6/5/5/5/5 in every edition; identical Dutch headwords in identical order. Core and zh-tw P6 glosses remain 3 lines (Round 1 F-2b state, intact).
- Chart + P7 + essay + furniture (`checks3.py`, adapted from the Round 2 proofreader's `checks.py`, `logs/checks3.log`): P6 chart bars measured from SVG rects in all editions — x=1473, y=304/362/420/478, widths 160/100/80/60, height 18, fill `#3e4c2a` (values 40/25/20/15). P7: 8/8 golden sentences verbatim (whitespace-normalised) on P7 AND in their source pages in all 11 editions; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay: 89 words in all 11 text.md files, same Dutch text. Kinsoku scan: clean. Footers 8/8 pages and page lines 8/8 in all editions; images per page [1,1,1,1,0,0,0,0]; all 4 photo credits present and identical frozen Dutch `Foto: …` lines. (Note: an earlier adapted chart script returned 0 bars because its rect regex assumed `fill` immediately follows `height`; the SVGs carry `rx="0"` between them. The bars were re-measured with the Round 2 ET-based method — values above — and confirmed present. Script artifact, not a defect.)
- PDFs (web vs print; `chart-p7-pdf.log` + direct measurement): all 11 web PDFs 8 pages, 1462.5×2025 pts, ≤7 MB (largest zh-tw 1,615,015 B), pdftotext bytes > 0; web-vs-print extracted text **0 diff tokens in all 11 editions**. Card dimensions 88/88 at 1950×2700.

### Visual checks (changed pages at full frame + spot checks)

| Page | Check | Result |
|---|---|---|
| P8 core | full frame + item-103 zone crop | Clean: single-line note `103. B — 入城式是圣诞老人的隆重到来`, no overflow, neighbours aligned |
| P8 fr | full frame + item-137 zone crop | Clean: two lines ending `Comparez avec l'article page 3`, no orphan, item 138 follows cleanly |
| P1 core | full frame (spot) | Clean: masthead, subtitle-slot pairing furniture, photo + credit, no overflow/overlap |
| P1 fr | full frame (spot) | Clean: badge at y=568 under the band, strapline kept, no overflow/overlap |
| P8 other editions | not re-viewed | SVGs/cards byte-identical to the Round 2 PASS artifacts (see §6); re-viewing would add nothing |

Checked-and-clear (not a defect): the core P8 F-options/model-essay column adjacency noted in Round 2 is unchanged (pre-existing layout, identical coordinates — the core P8 SVG changed in exactly one text element).

## 6. Change isolation (hash + SVG-text multiset diff + Round 1 fix survival)

- Pre-fix snapshot: SHA-256 of all 231 edition files (8 SVGs + 8 cards + print/web PDFs + `.text.md` + `WEEKLY-KIT.md` + `ABSTRACT.txt` per edition) in `nl-fix-round3/before/hashes-before.json`, taken before any edit. Post-render snapshot: `hashes-after.json`.
- Changed artifact files: **exactly 19 of 231** — core (`.text.md`, `svg/p8-toets.svg`, `cards/p8-toets.png`, print PDF, web PDF) and fr (same 5), plus all 9 other editions' **web PDFs only** (hash-only changes: extracted text byte counts identical to Rounds 1–2 for all 9 — de 46,586, en 45,597, es 46,675, it 46,429, ja 47,973, ko 47,853, pt 46,689, ru 55,313, zh-tw 44,455 — with byte-identical SVGs and print PDFs; the ±1-byte web-PDF drift is `webpdf.py` font-subsetting nondeterminism, not a content change; no other string changed). All other 212 files byte-identical, including every P1–P7 SVG and card in every edition.
- Rendered-output multiset diff: with only 2 SVGs changed in the whole family and both changes confined to the single fixed note element in each (verified by direct SVG text extraction: core P8 contains the new note once and `arrival` zero times outside EN; fr P8 contains the new 2-line note once and `Compare avec` zero times), the rendered-text multiset diff vs pre-fix contains ONLY the two intended strings. (No full pre-fix SVG text dump existed on disk to diff against mechanically; the proof chain is: exact source diffs (§2) + file hashes (this section) + direct extraction of the changed elements + the 1-line `.text.md` diffs below.)
- `.text.md` diffs vs the pre-fix copies (`before/textmd/`): core exactly 1 line (item 103, −2 bytes: the space before `arrival` also goes); fr exactly 1 line (item 137, +1 byte); the other 9 editions ZERO diff lines. All 11 headers verbatim (first-line comparison).
- Round 1 fixes survive intact: F-1 abstracts byte-identical to the pre-fix snapshot (and re-verified practice-framed in Pass D); F-2a (core P2, no lone `。`, 2-line EN JIJ box — P2 SVG byte-identical); F-2b (core/zh-tw P6 gloss 3 lines — P6 SVGs byte-identical); E-1 (fr/pt P3 single-line bridges — P3 SVGs byte-identical); E-2 (zh-tw P6 caption — P6 SVG byte-identical); E-3 (zh-tw P8 H-intro single line — P8 zh-tw SVG byte-identical). The F-2b tight-separator observation O-R2-1 is unchanged (same bytes).
- KIT files: after the artifact snapshot, exactly 4 KITs changed as specified in §2 (core: §1 rewrite + Round 3 record; fr: Round 3 record; ja: 2 freeze-value lines; ru: §7 parenthetical). No other KIT, ABSTRACT, or build file was touched beyond the source edits listed in §2. (Note: the `.text.md` byte sizes in this report's inventory differ from the Round 1 FIX-REPORT inventory table — e.g. core 39,152 vs 32,305 — but the pre-fix copies taken at the start of THIS task already had the larger sizes with identical 469-line content; the Round 1 table figures do not match the files as they stood at Round 3 start. Pre-existing record inconsistency, verified via the pre-fix copies; content diffs are the 1-line changes above. Reported, not chased.)

## 7. Final per-edition file inventory

Sizes in bytes, measured on the final artifacts. `.text.md` from `stat`; web/print PDF sizes and pdftotext bytes from the chart/PDF check (web-vs-print text identical in every edition).

| Edition | `.text.md` | Web PDF | Web pdftotext | Print PDF |
|---|---|---|---|---|
| zh-cn (core) | 39,152 | 1,325,908 | 44,392 | 18,472,780 |
| de | 40,803 | 774,922 | 46,586 | 6,644,100 |
| en | 40,086 | 768,074 | 45,597 | 6,604,762 |
| es | 40,920 | 776,057 | 46,675 | 6,642,975 |
| fr | 41,119 | 772,218 | 46,877 | 6,626,782 |
| it | 41,504 | 768,441 | 46,429 | 6,641,175 |
| ja | 42,143 | 1,375,362 | 47,973 | 19,287,942 |
| ko | 42,381 | 1,083,985 | 47,853 | 11,146,265 |
| pt | 40,849 | 781,803 | 46,689 | 6,668,637 |
| ru | 50,678 | 809,218 | 55,313 | 6,567,209 |
| zh-tw | 39,213 | 1,615,015 | 44,455 | 18,512,823 |

File names: print `De-Lucerna-VOL3[-<SUFFIX>].pdf`, web `De-Lucerna-VOL3[-<SUFFIX>]-web.pdf` (suffixes DE/EN/ES/FR/IT/JA/KO/PT/RU/ZH-TW; core has none), text `2026-w46-nl-<ed>.text.md` (core: `2026-w46-nl-zh-cn.text.md`), plus `svg/` (8 SVGs), `cards/` (8 PNGs), `WEEKLY-KIT.md`, `ABSTRACT.txt` in each edition dir.

## 8. Records written

- Fix record appended to the core KIT (`files/weekly-report-w46-nl-core/WEEKLY-KIT.md`, section "Fix record — Round 2 proofread defects N-1/N-2") and to the FR KIT (`files/weekly-report-w46-nl-fr/WEEKLY-KIT.md`, section "Fix record — Round 2 proofread defect N-2"), each with defect/fix quotes and re-gate evidence.
- Stale-line rewrites in the core (§1), JA (§7 + record gloss), and RU (§7) KITs as listed in §2.
- This report: `hidden_files/w46/nl-fix-round3/FIX-REPORT.md` (with Appendix A below).
- Evidence under `hidden_files/w46/nl-fix-round3/`: `before/` (hash snapshots, pre-fix `.text.md` copies, pre-fix build sources), `logs/` (build, transform, re-derivation diffs, gates, counts, gloss, chart/P7/PDF, residue sweep, checks3), `gates/` (freeze/p8/occlusion JSONs + gate logs + counts.json + checks.log), `crops/` (item-103/item-137 zone crops), `scratch/` (rederive3.py, build_all3.py, run_gates3.sh, residue_sweep3.py, candidates_dump.py, count/gloss/orphan/chart/checks adaptations), `residue-candidates.txt`.

## 9. Fixes NOT applied / open items

- None of the two defects was left unapplied. No third residue candidate was found, so nothing was held back for adjudication — there is no un-fixed same-class item to report.
- ONE tasked value was NOT written literally: the JA KIT freeze total was tasked as 3,341 but measured 3,340 on the final artifacts (reconciliation in §2); 3,340 was written, per the task's own verify-before-writing rule. Round 3 must confirm this reading.
- ONE out-of-scope observation, not fixed: RU KIT §9 still states web-PDF size 809,219 bytes while the final artifact measures 809,218 (±1 rebuild drift; text bytes 55,313 stable and now consistent everywhere). Left untouched per the fix-only scope; Round 3 may rewrite it or accept the drift.
- The `.text.md` byte-size mismatch vs the Round 1 inventory table (§6) is a pre-existing record inconsistency; content is verified by the 1-line diffs.
- Round 3 independent proofread of all 11 editions is still required before shipping (proofread-until-zero gate). Nothing was pushed, inserted, or posted. The coordinator inserts serially per SOP.

## Appendix A — Complete residue-sweep candidate list (deduplicated, regenerated from the final artifacts)

Format: `section | edition | page | token(s) | string`. Sections: `A-rem` = English-wordlist hits in non-EN editions beyond the core's own frozen strings; `A-core` = the core's own frozen-Dutch strings that trip the same list (reference); `B` = added-string hits against the EN vocabulary; `B2` = cross-language function-word hits in added strings; `B3` = non-English hits in the EN edition's added strings; `C` = script leaks (none found — no C lines); `D` = abstract flags (4 script lines, all legitimate native scripts / shared punctuation). Adjudication for every line: §3 of this report — all clean (frozen Dutch layer, native homograph, proper name, quoted Dutch term, established loanword, or native script). No line in this appendix is an unfixed defect.

```
A-core | core | * | live | en is live te zien op NPO Zapp (NPO
A-core | core | * | live | intocht is live te zien op NPO 3.
A-core | core | * | week | Agenda van de week · 本周大事
A-core | core | * | week | DE WEEK IN CIJFERS · 数字看本周
A-core | core | * | week | DEZE WEEK
A-core | core | * | week | De Eredivisie ligt deze week stil:
A-core | core | * | week | De woorden van deze week horen bij
A-core | core | * | week | Deze week is zondag 15 november
A-core | core | * | week | ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语
A-core | core | * | week | Eerder in de week, op woensdag 11
A-core | core | * | week | F · WOORDEN VAN DE WEEK
A-core | core | * | week | HET WOORD VAN DE WEEK
A-core | core | * | week | Maandag 16 november speelt Oranje in Berlijn tegen Duitsland — de uitslag lees je volgende week. Zaterdag 5 december is het pakjesavond. Verder: jullie brieven en de beste
A-core | core | * | week | Na deze week is er geen ___ meer tot maart.
A-core | core | * | week | Oranje: beslissende week
A-core | core | * | week | Speelronde 13 is deze week. Waar of niet
A-core | core | * | week | Twee feesten in één week: 's avonds
A-core | core | * | week | VOLGENDE WEEK · 下期预告 (VOL.4)
A-core | core | * | week | WEEK VAN 9 TOT EN MET 15 NOVEMBER 2026
A-core | core | * | week | Woorden van de week
A-core | core | * | week | ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）
A-core | core | * | week | deze week, loop jij met een lampion, kijk jij naar het
A-core | core | * | week | deze week.
A-core | core | * | week | een week vol licht!
A-core | core | * | week | geven, in één week.
A-core | core | * | week | november — en elke week wordt
A-core | core | * | week | week, in speelronde 11, won PSV
A-core | core | * | week | «Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij
A-core | core | * | week | 第 8 版 · De grote toets van de week + alle antwoorden
A-rem | de | p1-voorpagina.svg | week | Agenda van de week · TERMINE
A-rem | de | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · IN ZAHLEN
A-rem | de | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH
A-rem | de | p7-taal.svg | week | VOLGENDE WEEK · NÄCHSTE WOCHE (VOL.4)
A-rem | de | p7-taal.svg | week | ZINNEN VAN DE WEEK · SÄTZE DER WOCHE (WÖRTLICH AUS DIESER AUSGABE)
A-rem | de | p8-toets.svg | also | 6. zetten — Mehrere Kinder, also zetten.
A-rem | de | p8-toets.svg | her | 46. 17 — Het diner ist von 2009: 17 Jahre her im Jahr 2026
A-rem | de | p8-toets.svg | so | 90. C — Das Interesse am Martinstag nahm zu, so Stengs 2025
A-rem | de | p8-toets.svg | week | Seite 8 · De grote toets van de week + alle antwoorden
A-rem | es | p1-voorpagina.svg | week | Agenda van de week · AGENDA
A-rem | es | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · EN CIFRAS
A-rem | es | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS
A-rem | es | p7-taal.svg | week | VOLGENDE WEEK · LA SEMANA QUE VIENE (VOL.4)
A-rem | es | p7-taal.svg | week | ZINNEN VAN DE WEEK · FRASES DE LA SEMANA (LITERALES DE ESTE NÚMERO)
A-rem | es | p8-toets.svg | week | Página 8 · De grote toets van de week + alle antwoorden
A-rem | fr | p1-voorpagina.svg | arrive | Cette semaine : Sinterklaas arrive aux Pays-Bas · voir page 3
A-rem | fr | p1-voorpagina.svg | arrive | SINTERKLAAS ARRIVE
A-rem | fr | p1-voorpagina.svg | arrive | «L'intocht» : Sinterklaas arrive en ville en bateau,
A-rem | fr | p1-voorpagina.svg | week | Agenda van de week · LES ÉVÉNEMENTS
A-rem | fr | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · EN CHIFFRES
A-rem | fr | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · CHAQUE SEMAINE EN NÉERLANDAIS
A-rem | fr | p7-taal.svg | arrive | Samedi 14 novembre, Sinterklaas arrive officiellement à Grave. (Pagina 3)
A-rem | fr | p7-taal.svg | arrive | quand Sinterklaas arrive.
A-rem | fr | p7-taal.svg | festive | intocht : l'arrivée festive ; de schoen zetten :
A-rem | fr | p7-taal.svg | week | VOLGENDE WEEK · LA SEMAINE PROCHAINE (VOL.4)
A-rem | fr | p7-taal.svg | week | ZINNEN VAN DE WEEK · PHRASES DE LA SEMAINE (MOT POUR MOT DANS CE NUMÉRO)
A-rem | fr | p8-toets.svg | comparez | Comparez avec l'article page 3
A-rem | fr | p8-toets.svg | festive | 103. B — L'intocht est l'arrivée festive de Sinterklaas
A-rem | fr | p8-toets.svg | festive | 142. d — intocht = arrivée festive d
A-rem | fr | p8-toets.svg | programme | 45. 4 — Le programme de Grave, de 12 h 00 à 16 h 00, dure 4 heures
A-rem | fr | p8-toets.svg | week | Page 8 · De grote toets van de week + alle antwoorden
A-rem | it | p1-voorpagina.svg | week | Agenda van de week · GLI APPUNTAMENTI
A-rem | it | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · IN CIFRE
A-rem | it | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE
A-rem | it | p6-verdieping.svg | all | intorno all'11 novembre? (100 giovani)
A-rem | it | p7-taal.svg | week | VOLGENDE WEEK · LA PROSSIMA SETTIMANA (VOL.4)
A-rem | it | p7-taal.svg | week | ZINNEN VAN DE WEEK · FRASI DELLA SETTIMANA (LETTERALI DA QUESTO NUMERO)
A-rem | it | p8-toets.svg | all | all'ordinale 88e
A-rem | it | p8-toets.svg | week | Pagina 8 · De grote toets van de week + alle antwoorden
A-rem | ja | p1-voorpagina.svg | week | Agenda van de week · 今週の出来事
A-rem | ja | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · 数字で見る今週
A-rem | ja | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む
A-rem | ja | p7-taal.svg | week | VOLGENDE WEEK · 来週（VOL.4）
A-rem | ja | p7-taal.svg | week | ZINNEN VAN DE WEEK · 今週の名文（本号の記事から逐語引用）
A-rem | ja | p8-toets.svg | week | 8ページ · De grote toets van de week + alle antwoorden
A-rem | ko | p1-voorpagina.svg | week | Agenda van de week · 이번 주 일정
A-rem | ko | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · 이번 주 숫자
A-rem | ko | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어
A-rem | ko | p7-taal.svg | week | VOLGENDE WEEK · 다음 호 예고 (VOL.4)
A-rem | ko | p7-taal.svg | week | ZINNEN VAN DE WEEK · 이번 주 금문장(본문에서 그대로 가져왔어요)
A-rem | ko | p8-toets.svg | week | 8면 · De grote toets van de week + alle antwoorden
A-rem | pt | p1-voorpagina.svg | week | Agenda van de week · ACONTECIMENTOS
A-rem | pt | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · NÚMEROS
A-rem | pt | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS NEERLANDESES LEEM
A-rem | pt | p7-taal.svg | week | VOLGENDE WEEK · PRÓXIMA SEMANA (VOL.4)
A-rem | pt | p7-taal.svg | week | ZINNEN VAN DE WEEK · FRASES DA SEMANA (LITERAIS DESTE NÚMERO)
A-rem | pt | p8-toets.svg | week | Página 8 · De grote toets van de week + alle antwoorden
A-rem | ru | p1-voorpagina.svg | week | Agenda van de week · СОБЫТИЯ НЕДЕЛИ
A-rem | ru | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · В ЦИФРАХ
A-rem | ru | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · ЧИТАЕМ ПО-ГОЛЛАНДСКИ
A-rem | ru | p7-taal.svg | week | VOLGENDE WEEK · СЛЕДУЮЩАЯ НЕДЕЛЯ (VOL.4)
A-rem | ru | p7-taal.svg | week | ZINNEN VAN DE WEEK · ФРАЗЫ НЕДЕЛИ (ДОСЛОВНО ИЗ ЭТОГО НОМЕРА)
A-rem | ru | p8-toets.svg | week | Страница 8 · De grote toets van de week + alle antwoorden
A-rem | zh-tw | p1-voorpagina.svg | week | Agenda van de week · 本週大事
A-rem | zh-tw | p1-voorpagina.svg | week | DE WEEK IN CIJFERS · 數字看本週
A-rem | zh-tw | p1-voorpagina.svg | week | ELKE WEEK IN HET NEDERLANDS · 每週一期 · 讀荷蘭人正在讀的荷蘭語
A-rem | zh-tw | p7-taal.svg | week | VOLGENDE WEEK · 下期預告 (VOL.4)
A-rem | zh-tw | p7-taal.svg | week | ZINNEN VAN DE WEEK · 本週金句（逐字摘自本期文章）
B | de | p1-voorpagina.svg | lies | Lies Seite 1 und wähle die richtige Antwort · Antworten auf Seite 8
B | de | p1-voorpagina.svg | nov | Amsterdam, de 88e editie (15. Nov.: 88.
B | de | p1-voorpagina.svg | nov | Grave (14. Nov.: Einzug in Grave)
B | de | p1-voorpagina.svg | nov | begint (9. Nov.: Sinterklaasjournaal)
B | de | p1-voorpagina.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p1-voorpagina.svg | text | NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER
B | de | p2-leven.svg | an | auf Niederländisch und schicke sie an die
B | de | p2-leven.svg | lies | Lies den Artikel auf Seite 2 und wähle die
B | de | p2-leven.svg | martin | Martin, Kulturerbe
B | de | p2-leven.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p3-cultuur.svg | lies | Lies den Artikel auf Seite 3 und wähle die
B | de | p3-cultuur.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p4-sport.svg | lies | Lies den Artikel auf Seite 4 und wähle die
B | de | p4-sport.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p5-jongeren.svg | lies | Lies den Artikel auf Seite 5 und wähle die
B | de | p5-jongeren.svg | reporter | Reporter · de proef = Prüfung ·
B | de | p5-jongeren.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p6-verdieping.svg | lies | Lies den Artikel auf Seite 6 und wähle die
B | de | p6-verdieping.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p6-verdieping.svg | tradition | Hinweis · de traditie = Tradition ·
B | de | p6-verdieping.svg | was | Umfrage. Frage: Was machst du um den 11.
B | de | p7-taal.svg | an | Am Samstag, 14. November, kommt Sinterklaas offiziell in Grave an. (Pagina 3)
B | de | p7-taal.svg | name | Sinterklaas ist ein Name, ohne Artikel.
B | de | p7-taal.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p7-taal.svg | tradition | Eine Tradition lebt, wenn Menschen sie weiter feiern. (Pagina 6)
B | de | p7-taal.svg | tradition | Martinstag ist eine alte Tradition in den Niederlanden. (Pagina 6)
B | de | p7-taal.svg | verb | Verb zuerst: ben ik blij.
B | de | p8-toets.svg | an | 122. B — Grave liegt an der Maas
B | de | p8-toets.svg | her | 46. 17 — Het diner ist von 2009: 17 Jahre her im Jahr 2026
B | de | p8-toets.svg | malaysia | 67. C — Die Sendung wird auf einer unbewohnten Insel in Malaysia
B | de | p8-toets.svg | malaysia | 81. Niet waar — Falsch: Die Sendung wird in Malaysia gedreht
B | de | p8-toets.svg | martin | 14. B — Utrecht ist die Stadt des heiligen Martin
B | de | p8-toets.svg | martin | 20. Utrecht — Die Stadt des heiligen Martin ist Utrecht
B | de | p8-toets.svg | plural | 53. kwartfinales — kwartfinale, Plural: kwartfinales
B | de | p8-toets.svg | plural | 75. kandidaten — kandidaat, Plural: kandidaten
B | de | p8-toets.svg | plural | 79. gaan schrijven — zij (Plural) → gaan schrijven
B | de | p8-toets.svg | reporter | 71. verslaggever — verslaggever = Reporter, de-Wort
B | de | p8-toets.svg | so | 90. C — Das Interesse am Martinstag nahm zu, so Stengs 2025
B | de | p8-toets.svg | test | TOETS EN ANTWOORDEN · TEST UND ANTWORTEN
B | de | p8-toets.svg | text | De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH
B | de | p8-toets.svg | tradition | 127. B — Eine Tradition lebt, wenn Menschen sie weiter feiern
B | de | p8-toets.svg | tradition | 92. B — Eine Tradition lebt, wenn Menschen sie weiter feiern
B | de | p8-toets.svg | tradition | 93. traditie — traditie = Tradition, de-Wort
B | de | p8-toets.svg | verb | 111. gaat — Das Verb steht im Hauptsatz vorn: gaat de lampion aan
B | de | p8-toets.svg | verb | 133. Het Sinterklaasjournaal begint op maandag. — Subjekt + Verb +
B | de | p8-toets.svg | verb | 134. Wij zetten onze schoen bij de deur. — Subjekt + Verb + Objekt +
B | de | p8-toets.svg | verb | 135. Oranje speelt vrijdag tegen Griekenland. — Subjekt + Verb + Zeit
B | de | p8-toets.svg | verb | 136. Ik loop met een lampion langs de deuren. — Subjekt + Verb +
B | de | p8-toets.svg | verb | 97. Sint-Maarten is een oude traditie in Nederland. — Subjekt + Verb
B | de | p8-toets.svg | verb | Verb + Art und Weise + Ort
B | es | p1-voorpagina.svg | nov | Amsterdam, de 88e editie (15 nov.: 88.ª
B | es | p1-voorpagina.svg | nov | Grave (14 nov.: llegada en Grave)
B | es | p1-voorpagina.svg | nov | begint (9 nov.: noticiario de Sinterklaas)
B | es | p1-voorpagina.svg | quiz | BLIKSEMQUIZ · QUIZ RELÁMPAGO
B | es | p3-cultuur.svg | club | desfile · de leeskring: el club de lectura.
B | es | p4-sport.svg | final | · de kwartfinale: los cuartos de final ·
B | es | p6-verdieping.svg | no | Datos de práctica: cifras inventadas, no una
B | es | p6-verdieping.svg | real | encuesta real. Pregunta: ¿qué haces
B | es | p8-toets.svg | club | 38. leeskring — leeskring = club de lectura
B | es | p8-toets.svg | final | con als va al final
B | es | p8-toets.svg | no | 108. B — -je significa pequeño y cariñoso, no siempre realmente
B | es | p8-toets.svg | no | 110. B — Una cláusula con als es una condición, no una pregunta
B | es | p8-toets.svg | no | 15. B — Un farolillo lleva luz LED, no una vela
B | es | p8-toets.svg | no | 89. B — Las dos encuestas usan definiciones distintas, no se pueden
B | es | p8-toets.svg | ordinal | 139. De intocht in Amsterdam is de 88e editie. — Fíjate en el ordinal
B | es | p8-toets.svg | original | 138. San Martín es la fiesta de compartir. — Frase original de la
B | es | p8-toets.svg | plural | 53. kwartfinales — kwartfinale, plural: kwartfinales
B | es | p8-toets.svg | plural | 6. zetten — Sujeto plural, así que zetten.
B | es | p8-toets.svg | plural | 75. kandidaten — kandidaat, plural: kandidaten
B | es | p8-toets.svg | plural | 79. gaan schrijven — zij (plural) → gaan schrijven
B | es | p8-toets.svg | serbia | 62. Niet waar — Falso: Serbia es colista con 0 puntos
B | fr | p1-voorpagina.svg | dates,pages | Toutes les dates et heures, pages 2–4.
B | fr | p1-voorpagina.svg | nov | Amsterdam, de 88e editie (15 nov. : 88e
B | fr | p1-voorpagina.svg | nov | Grave (14 nov. : arrivée à Grave)
B | fr | p1-voorpagina.svg | nov | begint (9 nov. : journal de Sinterklaas)
B | fr | p1-voorpagina.svg | page | Cette semaine : Sinterklaas arrive aux Pays-Bas · voir page 3
B | fr | p1-voorpagina.svg | page | Lis la page 1, choisis la bonne réponse · réponses page 8
B | fr | p1-voorpagina.svg | page | Page 1 sur 8
B | fr | p1-voorpagina.svg | quiz | BLIKSEMQUIZ · QUIZ ÉCLAIR
B | fr | p2-leven.svg | article,page | Lis l'article page 2 et choisis la bonne
B | fr | p2-leven.svg | martin | NIVEAU A2 · Sint-Maarten: lichtjes en liedjes · Saint-Martin : lanternes et chansons
B | fr | p2-leven.svg | martin | Saint-Martin de porte en
B | fr | p2-leven.svg | martin | la ville de saint Martin,
B | fr | p2-leven.svg | note | Note — de lampion : la lanterne · delen :
B | fr | p2-leven.svg | page | Complète avec les mots de la page 2.
B | fr | p2-leven.svg | page | OEFENINGEN · EXERCICES PAGE 2
B | fr | p2-leven.svg | page | Page 2 sur 8
B | fr | p2-leven.svg | page | Réponses page 8 · niveaux mélangés ; cherche ton numéro
B | fr | p2-leven.svg | phrases | Sinterklaas ? Écris deux phrases en
B | fr | p3-cultuur.svg | article,page | Lis l'article page 3 et choisis la bonne
B | fr | p3-cultuur.svg | attention | Complète au passé composé. Attention aux
B | fr | p3-cultuur.svg | culture | CULTUUR · CULTURE
B | fr | p3-cultuur.svg | note | Note — het journaal : le journal télévisé ·
B | fr | p3-cultuur.svg | page | Calcule : réponds par les chiffres de la page 3.
B | fr | p3-cultuur.svg | page | OEFENINGEN · EXERCICES PAGE 3
B | fr | p3-cultuur.svg | page | Page 3 sur 8
B | fr | p3-cultuur.svg | page | Réponses page 8 · niveaux mélangés ; cherche ton numéro
B | fr | p4-sport.svg | article,page | Lis l'article page 4 et choisis la bonne
B | fr | p4-sport.svg | attention | Attention aux formes verbales.
B | fr | p4-sport.svg | international,match | interland : le match international · de
B | fr | p4-sport.svg | note | Note — de groepsfase : la phase de
B | fr | p4-sport.svg | page | OEFENINGEN · EXERCICES PAGE 4
B | fr | p4-sport.svg | page | Page 4 sur 8
B | fr | p4-sport.svg | page | Réponses page 8 · niveaux mélangés ; cherche ton numéro
B | fr | p5-jongeren.svg | article,page | Lis l'article page 5 et choisis la bonne
B | fr | p5-jongeren.svg | note | Note — het verlanglijstje : la liste de
B | fr | p5-jongeren.svg | page | OEFENINGEN · EXERCICES PAGE 5
B | fr | p5-jongeren.svg | page | Page 5 sur 8
B | fr | p5-jongeren.svg | page | Réponses page 8 · niveaux mélangés ; cherche ton numéro
B | fr | p5-jongeren.svg | phrases | Écris deux phrases en néerlandais et
B | fr | p5-jongeren.svg | points | : les points se jouent là)
B | fr | p5-jongeren.svg | reporter | souhaits · de verslaggever : le reporter
B | fr | p6-verdieping.svg | article,page | Lis l'article page 6 et choisis la bonne
B | fr | p6-verdieping.svg | expert | de deskundige : l'expert.
B | fr | p6-verdieping.svg | martin | NIVEAU B2 · Sint-Maarten of Halloween? · Saint-Martin ou Halloween ?
B | fr | p6-verdieping.svg | note,tradition | Note — de traditie : la tradition ·
B | fr | p6-verdieping.svg | page | OEFENINGEN · EXERCICES PAGE 6
B | fr | p6-verdieping.svg | page | Page 6 sur 8
B | fr | p6-verdieping.svg | page | Réponds avec le graphique page 6 (données
B | fr | p6-verdieping.svg | page | Réponses page 8 · niveaux mélangés ; cherche ton numéro
B | fr | p6-verdieping.svg | phrase | Former la phrase
B | fr | p6-verdieping.svg | phrases | des phrases.
B | fr | p6-verdieping.svg | question | vraie enquête. Question : que fais-tu autour
B | fr | p7-taal.svg | article | Sinterklaas est un nom, sans article.
B | fr | p7-taal.svg | attention,martin | La Saint-Martin est la fête du partage : partager la lumière, la nourriture, l'attention. (Pagina 2)
B | fr | p7-taal.svg | expression | Expression fixe : langs de deuren.
B | fr | p7-taal.svg | festive | intocht : l'arrivée festive ; de schoen zetten :
B | fr | p7-taal.svg | martin,tradition | La Saint-Martin est une vieille tradition aux Pays-Bas. (Pagina 6)
B | fr | p7-taal.svg | page | Page 7 sur 8
B | fr | p7-taal.svg | phrases | ZINNEN VAN DE WEEK · PHRASES DE LA SEMAINE (MOT POUR MOT DANS CE NUMÉRO)
B | fr | p7-taal.svg | tradition | Une tradition vit quand les gens continuent de la fêter. (Pagina 6)
B | fr | p8-toets.svg | article,page | Comparez avec l'article page 3
B | fr | p8-toets.svg | attention,ordinal | 139. De intocht in Amsterdam is de 88e editie. — Attention à l'ordinal
B | fr | p8-toets.svg | condition,question | 110. B — Une proposition en als est une condition, pas une question
B | fr | p8-toets.svg | expression | une expression fixe
B | fr | p8-toets.svg | festive | 103. B — L'intocht est l'arrivée festive de Sinterklaas
B | fr | p8-toets.svg | festive | 142. d — intocht = arrivée festive d
B | fr | p8-toets.svg | international,match | 56. interland — interland = match international
B | fr | p8-toets.svg | maritime | 123. B — Sinterklaas reçoit la clé de la ville au musée maritime
B | fr | p8-toets.svg | martin | 11. B — La Saint-Martin tombe mercredi 11 novembre
B | fr | p8-toets.svg | martin | 117. A — La Saint-Martin tombe le 11 novembre
B | fr | p8-toets.svg | martin | 119. B — La Saint-Martin est la fête du partage
B | fr | p8-toets.svg | martin | 130. B — Mercredi, elle rejoint le défilé de la Saint-Martin
B | fr | p8-toets.svg | martin | 14. B — Utrecht est la ville de saint Martin
B | fr | p8-toets.svg | martin | 16. 11 — La Saint-Martin tombe le 11 novembre
B | fr | p8-toets.svg | martin | 20. Utrecht — La ville de saint Martin est Utrecht
B | fr | p8-toets.svg | martin | 4. 11 — La Saint-Martin tombe mercredi 11 novembre
B | fr | p8-toets.svg | martin | 90. C — L'intérêt pour la Saint-Martin a augmenté, selon Stengs 2025
B | fr | p8-toets.svg | martin | 91. A — Halloween, c'est faire peur ; la Saint-Martin, c'est partager
B | fr | p8-toets.svg | martin,page,phrase | 138. La Saint-Martin est la fête du partage. — Phrase d'origine, page 2
B | fr | p8-toets.svg | note | Chaque réponse avec une courte note en français · ✓ marque la tâche d'écriture
B | fr | p8-toets.svg | on | 89. B — Les deux enquêtes utilisent des définitions différentes, on ne
B | fr | p8-toets.svg | page | ANTWOORDEN · CORRIGÉ — classé par page : trouve ton numéro
B | fr | p8-toets.svg | page | Page 8 sur 8
B | fr | p8-toets.svg | page | Page 8 · De grote toets van de week + alle antwoorden
B | fr | p8-toets.svg | phrase | Former la phrase
B | fr | p8-toets.svg | points | 125. B — Les Pays-Bas et la Grèce ont tous les deux 8 points
B | fr | p8-toets.svg | points | 48. C — Les Pays-Bas et la Grèce ont tous les deux 8 points
B | fr | p8-toets.svg | programme | 45. 4 — Le programme de Grave, de 12 h 00 à 16 h 00, dure 4 heures
B | fr | p8-toets.svg | reporter | 71. verslaggever — verslaggever = reporter, mot en de
B | fr | p8-toets.svg | section | 150. ✓ Voir le texte modèle, section H (89 mots)
B | fr | p8-toets.svg | test | TOETS EN ANTWOORDEN · TEST ET RÉPONSES
B | fr | p8-toets.svg | tradition | 127. B — Une tradition vit quand les gens continuent de la fêter
B | fr | p8-toets.svg | tradition | 92. B — Une tradition vit quand les gens continuent de la fêter
B | fr | p8-toets.svg | tradition | 93. traditie — traditie = tradition, mot en de
B | it | p1-voorpagina.svg | i | TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI
B | it | p1-voorpagina.svg | nov | Amsterdam, de 88e editie (15 nov.: 88ª)
B | it | p1-voorpagina.svg | nov | Grave (14 nov.: Grave)
B | it | p1-voorpagina.svg | nov | begint (9 nov.: notiziario)
B | it | p1-voorpagina.svg | quiz | BLIKSEMQUIZ · QUIZ LAMPO
B | it | p3-cultuur.svg | i | Calcola: rispondi con i numeri di pagina 3.
B | it | p4-sport.svg | i | de kwartfinale = i quarti di finale ·
B | it | p5-jongeren.svg | i | punten verdeeld (guarda le prove: i
B | it | p5-jongeren.svg | reporter | desideri · de verslaggever = il reporter ·
B | it | p6-verdieping.svg | all | intorno all'11 novembre? (100 giovani)
B | it | p7-taal.svg | focus | Focus sulla lingua · Drie niveaus, drie gereedschappen · Tre livelli, tre strumenti
B | it | p8-toets.svg | all | all'ordinale 88e
B | it | p8-toets.svg | i | 12. B — I bambini vanno di porta in porta con le lanterne
B | it | p8-toets.svg | i | 49. A — I Paesi Bassi hanno segnato più gol nel girone: 7 a 5
B | it | p8-toets.svg | i | 68. B — I concorrenti passano 34 giorni sull'isola
B | it | p8-toets.svg | i | 89. B — I due sondaggi usano definizioni diverse, non si possono
B | it | p8-toets.svg | reporter | 71. verslaggever — verslaggever = reporter (de)
B | it | p8-toets.svg | serbia | 62. Niet waar — Falso: la Serbia è ultima con 0 punti
B | it | p8-toets.svg | test | TOETS EN ANTWOORDEN · TEST E RISPOSTE
B | pt | p1-voorpagina.svg | do,nov | begint (9 nov.: notícias do Sinterklaas)
B | pt | p1-voorpagina.svg | nov | Amsterdam, de 88e editie (15 nov.: 88.ª
B | pt | p1-voorpagina.svg | nov | Grave (14 nov.: chegada nacional, Grave)
B | pt | p1-voorpagina.svg | quiz | BLIKSEMQUIZ · QUIZ RELÂMPAGO
B | pt | p1-voorpagina.svg | weekblad | WEEKBLAD IN HET NEDERLANDS · VOL.3 · SINTERKLAAS · SINT-MAARTEN · ORANJE
B | pt | p2-leven.svg | complete | Complete
B | pt | p2-leven.svg | do | partilhar: dar metade do
B | pt | p2-leven.svg | do | ver as notícias do Sinterklaas? Escreve
B | pt | p3-cultuur.svg | complete | Complete
B | pt | p3-cultuur.svg | do | Completa com as palavras do quadro.
B | pt | p3-cultuur.svg | do | NIVEAU A2 → B1 · Sinterklaasjournaal en Het diner · As notícias do Sinterklaas e Het diner
B | pt | p3-cultuur.svg | no | Completa no pretérito perfeito. Atenção aos
B | pt | p4-sport.svg | complete | Complete
B | pt | p4-sport.svg | do | Completa com as palavras do quadro.
B | pt | p4-sport.svg | final | · de kwartfinale = os quartos de final ·
B | pt | p4-sport.svg | no | Completa no passado ou no perfeito.
B | pt | p5-jongeren.svg | complete | Complete
B | pt | p5-jongeren.svg | do | Completa com as palavras do quadro.
B | pt | p5-jongeren.svg | do | Fala do futuro com gaan + infinitivo.
B | pt | p5-jongeren.svg | no | No domingo, vês o Expeditie Robinson ou
B | pt | p6-verdieping.svg | complete | Complete
B | pt | p6-verdieping.svg | do | Completa com as palavras do quadro.
B | pt | p6-verdieping.svg | real | um inquérito real. Pergunta: o que fazes por
B | pt | p7-taal.svg | complete | Complete
B | pt | p7-taal.svg | do | Na segunda-feira, 9 de novembro, as notícias do Sinterklaas começam na televisão. (Pagina 1)
B | pt | p7-taal.svg | no | No sábado, 14 de novembro, o Sinterklaas chega oficialmente a Grave. (Pagina 3)
B | pt | p8-toets.svg | do | 1. 9 — As notícias do Sinterklaas começam a 9 de novembro
B | pt | p8-toets.svg | do | 103. B — A intocht é a chegada festiva do Sinterklaas
B | pt | p8-toets.svg | do | 113. B — As notícias do Sinterklaas começam a 9 de novembro
B | pt | p8-toets.svg | do | 121. A — As notícias do Sinterklaas passam todos os dias às 18:00
B | pt | p8-toets.svg | do | 13. C — Martinus deu metade do seu manto a um mendigo
B | pt | p8-toets.svg | do | 132. B — Ela vê as notícias do Sinterklaas todos os dias às 18:00
B | pt | p8-toets.svg | do | 137. As notícias do Sinterklaas passam todos os dias às 18:00. —
B | pt | p8-toets.svg | do | 149. A — 18:00 = a hora das notícias do Sinterklaas
B | pt | p8-toets.svg | do | 29. B — As notícias do Sinterklaas passam todos os dias às 18:00
B | pt | p8-toets.svg | do | 7. B — As notícias do Sinterklaas começam na segunda-feira, 9 de
B | pt | p8-toets.svg | no | 122. B — Grave fica no rio Maas
B | pt | p8-toets.svg | no | 123. B — O Sinterklaas recebe a chave da cidade no Museu Marítimo
B | pt | p8-toets.svg | no | 128. C — O Pakjesavond é no sábado, 5 de dezembro
B | pt | p8-toets.svg | no | 131. B — Ela põe uma cenoura e uma lista de desejos no seu sapato
B | pt | p8-toets.svg | no | 3. 15 — A chegada a Amesterdão é no domingo, 15 de novembro
B | pt | p8-toets.svg | no | 40. heeft gevonden — vinden no perfeito: heeft gevonden
B | pt | p8-toets.svg | no | 42. hebben gelezen — lezen no perfeito: hebben gelezen
B | pt | p8-toets.svg | no | 49. A — Os Países Baixos marcaram mais golos no grupo: 7 a 5
B | pt | p8-toets.svg | no | 57. speelde — spelen no passado: speelde
B | pt | p8-toets.svg | no | 58. won — winnen no passado: won
B | pt | p8-toets.svg | no | 59. maakte — maken no passado: maakte
B | pt | p8-toets.svg | no | 60. zijn gekomen — komen no perfeito leva zijn
B | pt | p8-toets.svg | no | 82. Niet waar — Falso: a cenoura no sapato é para o cavalo
B | pt | p8-toets.svg | no | als vem no fim
B | pt | p8-toets.svg | ordinal | 139. De intocht in Amsterdam is de 88e editie. — Atenção ao ordinal
B | pt | p8-toets.svg | original | 138. O São Martinho é a festa da partilha. — Frase original da página
B | pt | p8-toets.svg | plural | 53. kwartfinales — kwartfinale, plural: kwartfinales
B | pt | p8-toets.svg | plural | 6. zetten — Plural → zetten.
B | pt | p8-toets.svg | plural | 75. kandidaten — kandidaat, plural: kandidaten
B | pt | p8-toets.svg | plural | 79. gaan schrijven — zij (plural) → gaan schrijven
B2 | de | p1-voorpagina.svg | lang=en week | Agenda van de week · TERMINE
B2 | de | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · IN ZAHLEN
B2 | de | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH
B2 | de | p2-leven.svg | lang=fr des | Die Stadt des heiligen
B2 | de | p7-taal.svg | lang=en week | VOLGENDE WEEK · NÄCHSTE WOCHE (VOL.4)
B2 | de | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · SÄTZE DER WOCHE (WÖRTLICH AUS DIESER AUSGABE)
B2 | de | p7-taal.svg | lang=fr des | Martinstag ist das Fest des Teilens: Licht teilen, Essen teilen, Aufmerksamkeit teilen. (Pagina 2)
B2 | de | p7-taal.svg | lang=fr pas | PAS OP! · FEHLERKLINIK
B2 | de | p8-toets.svg | lang=en also | 6. zetten — Mehrere Kinder, also zetten.
B2 | de | p8-toets.svg | lang=en week | Seite 8 · De grote toets van de week + alle antwoorden
B2 | de | p8-toets.svg | lang=fr des | 119. B — Martinstag ist das Fest des Teilens
B2 | de | p8-toets.svg | lang=fr des | 138. Martinstag ist das Fest des Teilens. — Originalsatz von Seite 2 ·
B2 | de | p8-toets.svg | lang=fr des | 14. B — Utrecht ist die Stadt des heiligen Martin
B2 | de | p8-toets.svg | lang=fr des | 20. Utrecht — Die Stadt des heiligen Martin ist Utrecht
B2 | en | p7-taal.svg | lang=de als | Als… = If… / When…; als het donker wordt =
B2 | en | p7-taal.svg | lang=de als | Verb first after the als-clause: ben ik blij.
B2 | en | p7-taal.svg | lang=de als | when it gets dark; als Sinterklaas komt =
B2 | en | p7-taal.svg | lang=fr pas | PAS OP! · ERROR CLINIC
B2 | en | p8-toets.svg | lang=de alle | Page 8 · De grote toets van de week + alle antwoorden
B2 | en | p8-toets.svg | lang=de als | 109. Als — Als… = If… / When…
B2 | en | p8-toets.svg | lang=de als | 110. B — An als-clause is a condition, not a question
B2 | en | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… = If Oranje win…
B2 | en | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — The
B2 | en | p8-toets.svg | lang=de als | als-clause comes last
B2 | es | p1-voorpagina.svg | lang=en week | Agenda van de week · AGENDA
B2 | es | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · EN CIFRAS
B2 | es | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS
B2 | es | p1-voorpagina.svg | lang=pt para | TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES
B2 | es | p6-verdieping.svg | lang=pt para | Pon las palabras en el orden correcto para
B2 | es | p7-taal.svg | lang=de als | Als…: si… / cuando…; als het donker wordt:
B2 | es | p7-taal.svg | lang=de als | cuando oscurece; als Sinterklaas komt:
B2 | es | p7-taal.svg | lang=en week | VOLGENDE WEEK · LA SEMANA QUE VIENE (VOL.4)
B2 | es | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · FRASES DE LA SEMANA (LITERALES DE ESTE NÚMERO)
B2 | es | p7-taal.svg | lang=fr pas | PAS OP! · CLÍNICA DE ERRORES
B2 | es | p7-taal.svg | lang=pt para | ejemplo; promesa para el VOL.4.
B2 | es | p7-taal.svg | lang=pt para | y textos para el VOL.4!
B2 | es | p8-toets.svg | lang=de alle | Página 8 · De grote toets van de week + alle antwoorden
B2 | es | p8-toets.svg | lang=de als | 109. Als — Als…: si… / cuando…
B2 | es | p8-toets.svg | lang=de als | 110. B — Una cláusula con als es una condición, no una pregunta
B2 | es | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint…: si Oranje gana…
B2 | es | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — La cláusula
B2 | es | p8-toets.svg | lang=de als | con als va al final
B2 | es | p8-toets.svg | lang=en week | Página 8 · De grote toets van de week + alle antwoorden
B2 | es | p8-toets.svg | lang=fr une | 130. B — El miércoles se une al desfile de San Martín
B2 | es | p8-toets.svg | lang=pt para | 146. A — wortel = zanahoria para el caballo
B2 | es | p8-toets.svg | lang=pt para | 82. Niet waar — Falso: la zanahoria del zapato es para el caballo
B2 | fr | p1-voorpagina.svg | lang=en week | Agenda van de week · LES ÉVÉNEMENTS
B2 | fr | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · EN CHIFFRES
B2 | fr | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · CHAQUE SEMAINE EN NÉERLANDAIS
B2 | fr | p5-jongeren.svg | lang=it qui | blijft (devine entre amis qui restera le
B2 | fr | p7-taal.svg | lang=de als | Als… : si… / quand… ; als het donker wordt :
B2 | fr | p7-taal.svg | lang=de als | quand il fait noir ; als Sinterklaas komt :
B2 | fr | p7-taal.svg | lang=en festive | intocht : l'arrivée festive ; de schoen zetten :
B2 | fr | p7-taal.svg | lang=en week | VOLGENDE WEEK · LA SEMAINE PROCHAINE (VOL.4)
B2 | fr | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · PHRASES DE LA SEMAINE (MOT POUR MOT DANS CE NUMÉRO)
B2 | fr | p8-toets.svg | lang=de alle | Page 8 · De grote toets van de week + alle antwoorden
B2 | fr | p8-toets.svg | lang=de als | 109. Als — Als… : si… / quand…
B2 | fr | p8-toets.svg | lang=de als | 110. B — Une proposition en als est une condition, pas une question
B2 | fr | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… : si Oranje gagne…
B2 | fr | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — La
B2 | fr | p8-toets.svg | lang=de als | proposition en als vient en dernier
B2 | fr | p8-toets.svg | lang=en festive | 103. B — L'intocht est l'arrivée festive de Sinterklaas
B2 | fr | p8-toets.svg | lang=en festive | 142. d — intocht = arrivée festive d
B2 | fr | p8-toets.svg | lang=en programme | 45. 4 — Le programme de Grave, de 12 h 00 à 16 h 00, dure 4 heures
B2 | fr | p8-toets.svg | lang=en week | Page 8 · De grote toets van de week + alle antwoorden
B2 | fr | p8-toets.svg | lang=es son | 13. C — Martinus a donné la moitié de son manteau à un mendiant
B2 | it | p1-voorpagina.svg | lang=en week | Agenda van de week · GLI APPUNTAMENTI
B2 | it | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · IN CIFRE
B2 | it | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE
B2 | it | p2-leven.svg | lang=es con | Completa con le parole della canzone e il
B2 | it | p2-leven.svg | lang=es con | Completa con le parole di pagina 2.
B2 | it | p2-leven.svg | lang=es con | Wat hoort bij het feest? · Quali parole vanno con la festa?
B2 | it | p2-leven.svg | lang=es con,una | con una luce LED dentro
B2 | it | p2-leven.svg | lang=es con,una | in porta con una lanterna, o preferirai
B2 | it | p2-leven.svg | lang=es una | una lanterna di carta,
B2 | it | p3-cultuur.svg | lang=es con | Calcola: rispondi con i numeri di pagina 3.
B2 | it | p3-cultuur.svg | lang=es con | Completa con le parole del riquadro.
B2 | it | p4-sport.svg | lang=de alle | Attenzione alle forme verbali.
B2 | it | p4-sport.svg | lang=es con | Completa con le parole del riquadro.
B2 | it | p5-jongeren.svg | lang=es con | Completa con le parole del riquadro.
B2 | it | p5-jongeren.svg | lang=es con | Parla del futuro con gaan + infinito.
B2 | it | p5-jongeren.svg | lang=es con | blijft (indovina con gli amici chi resta
B2 | it | p5-jongeren.svg | lang=es con | preferisci mettere fuori la scarpa con la
B2 | it | p5-jongeren.svg | lang=es con | scarpa, con la lista dentro)
B2 | it | p6-verdieping.svg | lang=es con | Completa con le parole del riquadro.
B2 | it | p6-verdieping.svg | lang=es con | Rispondi con il grafico a pagina 6 (dati di
B2 | it | p7-taal.svg | lang=de alle | Ogni domenica alle 20:00, Expeditie Robinson va in onda su RTL 4. (Pagina 5)
B2 | it | p7-taal.svg | lang=de als | Als… = Se… / Quando…; als het donker
B2 | it | p7-taal.svg | lang=de als | wordt = quando fa buio; als Sinterklaas komt
B2 | it | p7-taal.svg | lang=en week | VOLGENDE WEEK · LA PROSSIMA SETTIMANA (VOL.4)
B2 | it | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · FRASI DELLA SETTIMANA (LETTERALI DA QUESTO NUMERO)
B2 | it | p7-taal.svg | lang=es con,una | con una carota e un disegno dentro.
B2 | it | p7-taal.svg | lang=es una | San Martino è una vecchia tradizione nei Paesi Bassi. (Pagina 6)
B2 | it | p7-taal.svg | lang=es una | Una tradizione vive quando la gente continua a festeggiarla. (Pagina 6)
B2 | it | p7-taal.svg | lang=fr pas | PAS OP! · CLINICA DEGLI ERRORI
B2 | it | p7-taal.svg | lang=pt quando | = quando arriva Sinterklaas.
B2 | it | p7-taal.svg | lang=pt quando | Als… = Se… / Quando…; als het donker
B2 | it | p7-taal.svg | lang=pt quando | Una tradizione vive quando la gente continua a festeggiarla. (Pagina 6)
B2 | it | p7-taal.svg | lang=pt quando | wordt = quando fa buio; als Sinterklaas komt
B2 | it | p8-toets.svg | lang=de alle | 10. B — Paesi Bassi–Grecia, calcio d'inizio venerdì alle 20:45
B2 | it | p8-toets.svg | lang=de alle | 116. B — Paesi Bassi–Grecia, calcio d'inizio alle 20:45
B2 | it | p8-toets.svg | lang=de alle | 121. A — Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00
B2 | it | p8-toets.svg | lang=de alle | 132. B — Guarda il notiziario di Sinterklaas ogni giorno alle 18:00
B2 | it | p8-toets.svg | lang=de alle | 137. Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00. —
B2 | it | p8-toets.svg | lang=de alle | 29. B — Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00
B2 | it | p8-toets.svg | lang=de alle | 31. C — Il battello di Amsterdam parte da De Omval alle 10:15
B2 | it | p8-toets.svg | lang=de alle | 5. 20:45 — Paesi Bassi–Grecia, calcio d'inizio alle 20:45
B2 | it | p8-toets.svg | lang=de alle | 65. B — Robinson va in onda ogni domenica alle 20:00 su RTL 4
B2 | it | p8-toets.svg | lang=de alle | Pagina 8 · De grote toets van de week + alle antwoorden
B2 | it | p8-toets.svg | lang=de als | 109. Als — Als… = Se… / Quando…
B2 | it | p8-toets.svg | lang=de als | 110. B — Una frase con als è una condizione, non una domanda
B2 | it | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… = Se Oranje vince…
B2 | it | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — La frase con
B2 | it | p8-toets.svg | lang=de als | als va alla fine
B2 | it | p8-toets.svg | lang=en week | Pagina 8 · De grote toets van de week + alle antwoorden
B2 | it | p8-toets.svg | lang=es con | 12. B — I bambini vanno di porta in porta con le lanterne
B2 | it | p8-toets.svg | lang=es con | 62. Niet waar — Falso: la Serbia è ultima con 0 punti
B2 | it | p8-toets.svg | lang=es con | 99. Een traditie leeft als mensen haar blijven vieren. — La frase con
B2 | it | p8-toets.svg | lang=es con | Confronta con l'articolo di pagina 3
B2 | it | p8-toets.svg | lang=es con,una | 110. B — Una frase con als è una condizione, non una domanda
B2 | it | p8-toets.svg | lang=es con,una | 83. 40 — 40 giovani camminano con una lanterna
B2 | it | p8-toets.svg | lang=es con,una | Metto fuori la scarpa, con una lista dei desideri dentro. → ___
B2 | it | p8-toets.svg | lang=es con,una | Ogni risposta con una breve nota in italiano · ✓ segna il compito di scrittura
B2 | it | p8-toets.svg | lang=es una | 127. B — Una tradizione vive quando la gente continua a festeggiarla
B2 | it | p8-toets.svg | lang=es una | 131. B — Mette una carota e una lista dei desideri nella sua scarpa
B2 | it | p8-toets.svg | lang=es una | 15. B — Una lanterna ha una luce LED, non una candela
B2 | it | p8-toets.svg | lang=es una | 23. ledlampje — Una luce LED è sicura
B2 | it | p8-toets.svg | lang=es una | 69. A — Una lista dei desideri va nella scarpa
B2 | it | p8-toets.svg | lang=es una | 92. B — Una tradizione vive quando la gente continua a festeggiarla
B2 | it | p8-toets.svg | lang=pt quando | 109. Als — Als… = Se… / Quando…
B2 | it | p8-toets.svg | lang=pt quando | 127. B — Una tradizione vive quando la gente continua a festeggiarla
B2 | it | p8-toets.svg | lang=pt quando | 22. donker — Le lanterne brillano di più quando è buio
B2 | it | p8-toets.svg | lang=pt quando | 92. B — Una tradizione vive quando la gente continua a festeggiarla
B2 | ja | p1-voorpagina.svg | lang=en week | Agenda van de week · 今週の出来事
B2 | ja | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · 数字で見る今週
B2 | ja | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む
B2 | ja | p7-taal.svg | lang=de als | Als… もし…／～のとき；als het donker
B2 | ja | p7-taal.svg | lang=de als | als節の後では動詞が先頭：ben ik blij。
B2 | ja | p7-taal.svg | lang=de als | wordt 暗くなるとき；als Sinterklaas komt シ
B2 | ja | p7-taal.svg | lang=en week | VOLGENDE WEEK · 来週（VOL.4）
B2 | ja | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · 今週の名文（本号の記事から逐語引用）
B2 | ja | p7-taal.svg | lang=fr pas | PAS OP! · 間違いクリニック
B2 | ja | p8-toets.svg | lang=de alle | 8ページ · De grote toets van de week + alle antwoorden
B2 | ja | p8-toets.svg | lang=de als | 109. Als — Als… もし…／～のとき
B2 | ja | p8-toets.svg | lang=de als | 110. B — als節は条件であって、疑問ではない
B2 | ja | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… オラニエが勝てば…
B2 | ja | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — als節は文末
B2 | ja | p8-toets.svg | lang=en week | 8ページ · De grote toets van de week + alle antwoorden
B2 | ko | p1-voorpagina.svg | lang=en week | Agenda van de week · 이번 주 일정
B2 | ko | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · 이번 주 숫자
B2 | ko | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어
B2 | ko | p7-taal.svg | lang=de als | Als… = 만약… / ~할 때; als het donker wordt =
B2 | ko | p7-taal.svg | lang=de als | als 절 뒤에서는 동사가 먼저 와요: ben ik blij.
B2 | ko | p7-taal.svg | lang=de als | 어두워지면; als Sinterklaas komt = 신터클라스가
B2 | ko | p7-taal.svg | lang=en week | VOLGENDE WEEK · 다음 호 예고 (VOL.4)
B2 | ko | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · 이번 주 금문장(본문에서 그대로 가져왔어요)
B2 | ko | p7-taal.svg | lang=fr pas | PAS OP! · 실수 클리닉
B2 | ko | p8-toets.svg | lang=de alle | 8면 · De grote toets van de week + alle antwoorden
B2 | ko | p8-toets.svg | lang=de als | 109. Als — Als… = 만약… / ~할 때
B2 | ko | p8-toets.svg | lang=de als | 110. B — als 절은 조건이지, 질문이 아니에요
B2 | ko | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… = 오라녜가 이기면…
B2 | ko | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — als 절은 마
B2 | ko | p8-toets.svg | lang=en week | 8면 · De grote toets van de week + alle antwoorden
B2 | pt | p1-voorpagina.svg | lang=en week | Agenda van de week · ACONTECIMENTOS
B2 | pt | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · NÚMEROS
B2 | pt | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS NEERLANDESES LEEM
B2 | pt | p1-voorpagina.svg | lang=es esta | Esta semana: o Sinterklaas chega aos Países Baixos · ver página 3
B2 | pt | p1-voorpagina.svg | lang=es esta | · ESTA SEMANA
B2 | pt | p1-voorpagina.svg | lang=es está | O SINTERKLAAS ESTÁ A CHEGAR
B2 | pt | p1-voorpagina.svg | lang=es para | TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA
B2 | pt | p4-sport.svg | lang=de das | NIVEAU B1 · Oranje en de Nations League · Oranje e a Liga das Nações
B2 | pt | p5-jongeren.svg | lang=fr mais | mais tempo)
B2 | pt | p6-verdieping.svg | lang=es para | Põe as palavras na ordem certa para formar
B2 | pt | p6-verdieping.svg | lang=es por | um inquérito real. Pergunta: o que fazes por
B2 | pt | p7-taal.svg | lang=de als | Als… = Se… / Quando…; als het donker
B2 | pt | p7-taal.svg | lang=de als | wordt = quando escurece; als Sinterklaas
B2 | pt | p7-taal.svg | lang=en week | VOLGENDE WEEK · PRÓXIMA SEMANA (VOL.4)
B2 | pt | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · FRASES DA SEMANA (LITERAIS DESTE NÚMERO)
B2 | pt | p7-taal.svg | lang=es para | exemplo; promessa para o VOL.4.
B2 | pt | p7-taal.svg | lang=es para | para o VOL.4!
B2 | pt | p7-taal.svg | lang=fr pas | PAS OP! · CLÍNICA DE ERROS
B2 | pt | p7-taal.svg | lang=it quando | Als… = Se… / Quando…; als het donker
B2 | pt | p7-taal.svg | lang=it quando | Uma tradição vive quando as pessoas continuam a celebrá-la. (Pagina 6)
B2 | pt | p7-taal.svg | lang=it quando | komt = quando o Sinterklaas chega.
B2 | pt | p7-taal.svg | lang=it quando | wordt = quando escurece; als Sinterklaas
B2 | pt | p8-toets.svg | lang=de alle | Página 8 · De grote toets van de week + alle antwoorden
B2 | pt | p8-toets.svg | lang=de als | 109. Als — Als… = Se… / Quando…
B2 | pt | p8-toets.svg | lang=de als | 110. B — Uma oração com als é uma condição, não uma pergunta
B2 | pt | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… = Se o Oranje ganhar…
B2 | pt | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — A oração com
B2 | pt | p8-toets.svg | lang=de als | als vem no fim
B2 | pt | p8-toets.svg | lang=de das | 149. A — 18:00 = a hora das notícias do Sinterklaas
B2 | pt | p8-toets.svg | lang=en week | Página 8 · De grote toets van de week + alle antwoorden
B2 | pt | p8-toets.svg | lang=es está | 22. donker — As lanternas brilham mais quando está escuro
B2 | pt | p8-toets.svg | lang=es para | 146. A — wortel = cenoura (para o cavalo)
B2 | pt | p8-toets.svg | lang=es para | 69. A — Uma lista de desejos vai para o sapato
B2 | pt | p8-toets.svg | lang=es para | 82. Niet waar — Falso: a cenoura no sapato é para o cavalo
B2 | pt | p8-toets.svg | lang=es para | Traduza para o neerlandês
B2 | pt | p8-toets.svg | lang=es para | Traduza para o português
B2 | pt | p8-toets.svg | lang=es por | 32. A — Het diner foi escrito por Herman Koch
B2 | pt | p8-toets.svg | lang=es por | 64. Waar — Verdadeiro: o PSV bateu o Willem II por 7–0
B2 | pt | p8-toets.svg | lang=es por | 89. B — Os dois inquéritos usam definições diferentes, por isso não
B2 | pt | p8-toets.svg | lang=es por | ANTWOORDEN · CHAVE DE RESPOSTAS — agrupadas por página: encontra o teu número
B2 | pt | p8-toets.svg | lang=fr mais | 22. donker — As lanternas brilham mais quando está escuro
B2 | pt | p8-toets.svg | lang=fr mais | 49. A — Os Países Baixos marcaram mais golos no grupo: 7 a 5
B2 | pt | p8-toets.svg | lang=it quando | 109. Als — Als… = Se… / Quando…
B2 | pt | p8-toets.svg | lang=it quando | 127. B — Uma tradição vive quando as pessoas continuam a
B2 | pt | p8-toets.svg | lang=it quando | 22. donker — As lanternas brilham mais quando está escuro
B2 | pt | p8-toets.svg | lang=it quando | 92. B — Uma tradição vive quando as pessoas continuam a celebrá-la
B2 | ru | p1-voorpagina.svg | lang=en week | Agenda van de week · СОБЫТИЯ НЕДЕЛИ
B2 | ru | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · В ЦИФРАХ
B2 | ru | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · ЧИТАЕМ ПО-ГОЛЛАНДСКИ
B2 | ru | p7-taal.svg | lang=de als | Als… — если… / когда…; als het donker
B2 | ru | p7-taal.svg | lang=de als | wordt — когда темнеет; als Sinterklaas komt
B2 | ru | p7-taal.svg | lang=de als | Глагол первым после als: ben ik blij.
B2 | ru | p7-taal.svg | lang=en week | VOLGENDE WEEK · СЛЕДУЮЩАЯ НЕДЕЛЯ (VOL.4)
B2 | ru | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · ФРАЗЫ НЕДЕЛИ (ДОСЛОВНО ИЗ ЭТОГО НОМЕРА)
B2 | ru | p7-taal.svg | lang=fr pas | PAS OP! · КЛИНИКА ОШИБОК
B2 | ru | p8-toets.svg | lang=de alle | Страница 8 · De grote toets van de week + alle antwoorden
B2 | ru | p8-toets.svg | lang=de als | 109. Als — Als… — если… / когда…
B2 | ru | p8-toets.svg | lang=de als | 110. B — Придаточное с als — условие, а не вопрос
B2 | ru | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… — если Оранье выиграет…
B2 | ru | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. —
B2 | ru | p8-toets.svg | lang=de als | Придаточное с als стоит в конце
B2 | ru | p8-toets.svg | lang=en week | Страница 8 · De grote toets van de week + alle antwoorden
B2 | zh-tw | p1-voorpagina.svg | lang=en week | Agenda van de week · 本週大事
B2 | zh-tw | p1-voorpagina.svg | lang=en week | DE WEEK IN CIJFERS · 數字看本週
B2 | zh-tw | p1-voorpagina.svg | lang=en week | ELKE WEEK IN HET NEDERLANDS · 每週一期 · 讀荷蘭人正在讀的荷蘭語
B2 | zh-tw | p7-taal.svg | lang=de als | Als… = 如果…／當…；als het donker wordt =
B2 | zh-tw | p7-taal.svg | lang=de als | als 子句之後動詞在前：ben ik blij。
B2 | zh-tw | p7-taal.svg | lang=de als | 天黑時；als Sinterklaas komt = 辛特克拉斯來
B2 | zh-tw | p7-taal.svg | lang=en week | VOLGENDE WEEK · 下期預告 (VOL.4)
B2 | zh-tw | p7-taal.svg | lang=en week | ZINNEN VAN DE WEEK · 本週金句（逐字摘自本期文章）
B2 | zh-tw | p7-taal.svg | lang=fr pas | PAS OP! · 易錯診所
B2 | zh-tw | p8-toets.svg | lang=de als | 109. Als — Als… = 如果…／當…
B2 | zh-tw | p8-toets.svg | lang=de als | 110. B — als 子句是條件，不是疑問
B2 | zh-tw | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… = 荷蘭隊贏了…
B2 | zh-tw | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — als 子句放
B3 | en | p7-taal.svg | lang=de als | Als… = If… / When…; als het donker wordt =
B3 | en | p7-taal.svg | lang=de als | Verb first after the als-clause: ben ik blij.
B3 | en | p7-taal.svg | lang=de als | when it gets dark; als Sinterklaas komt =
B3 | en | p7-taal.svg | lang=fr pas | PAS OP! · ERROR CLINIC
B3 | en | p8-toets.svg | lang=de alle | Page 8 · De grote toets van de week + alle antwoorden
B3 | en | p8-toets.svg | lang=de als | 109. Als — Als… = If… / When…
B3 | en | p8-toets.svg | lang=de als | 110. B — An als-clause is a condition, not a question
B3 | en | p8-toets.svg | lang=de als | 112. wint — Als Oranje wint… = If Oranje win…
B3 | en | p8-toets.svg | lang=de als | 99. Een traditie leeft als mensen haar blijven vieren. — The
B3 | en | p8-toets.svg | lang=de als | als-clause comes last
D-script | ja | ABSTRACT | script | De Lucerna オランダ語週刊 VOL.3：11月9日からのシンタクラース・ニュース、11月14日のグラーフェ全国到着、11月15日のアムステルダム第88…
D-script | ko | ABSTRACT | script | De Lucerna 네덜란드어 주간지 VOL.3: 11월 9일부터 시작하는 신터클라스 뉴스, 11월 14일 흐라버 전국 도착, 11월 15일 암…
D-script | ru | ABSTRACT | script | De Lucerna голландский еженедельник VOL.3: новости Синтерклааса с 9 ноября, наци…
D-script | zh-tw | ABSTRACT | script | De Lucerna 荷語週報 VOL.3：11 月 9 日起的辛特克拉斯新聞、11 月 14 日赫拉弗全國進城、11 月 15 日阿姆斯特丹第 88 屆進城、…
```
