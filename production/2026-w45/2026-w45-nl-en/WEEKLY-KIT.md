# WEEKLY KIT — De Lucerna, VOL.2 (Nederlands × English, W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Pairing:** target language **Dutch** × reader native language **English** (matrix cell NL × EN).
- **Masthead:** De Lucerna (article De, per the Dutch convention).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Relation to the core:** built from `files/weekly-report-w45-nl-core/` (VOL.2, masthead De Lucerna). The Dutch core — articles, exercises, images, facts, answer keys — is frozen and identical; only the explanation layer was rewritten, into English. No Discord post, no chat card/PDF dump, no cron, no weekly-git touch, no core/W43 modification (core and W43 dirs read-only throughout; core SVGs re-hashed 8/8 unchanged at the end).
- **Lead topic:** «Nederland in de Klimaatweek» — the national Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov). Facts, trend sources and verification debts are inherited unchanged from the core KIT §4.

## 2. Content per page (identical structure to the core; only the explanation layer differs)

- **P1 — Voorpagina (A2, 10 ex.):** headline «Nederland in de Klimaatweek: bomen, musea en voetbal»; week agenda; numbers box; word of the week «het klimaat»; photo herfstbos; IN HET KORT box; lightning quiz (7–10).
- **P2 — Leven (A2, 18 ex.):** «De Klimaatweek: wat kun jij doen?» — Coevorden giveaway, energy saving, KNMI colour codes; photo kinderdijk; WIST JE DAT facts; EN JIJ box (best entries to VOL.3).
- **P3 — Cultuur (A2→B1, 18 ex.):** «Amsterdam blijft wakker: de Museumnacht» — Museumnacht, Crossing Border, PAN Amsterdam, Mega Snuffelmarkt; photo gracht.
- **P4 — Sport (B1, 18 ex.):** «Europa: drie keer feest, twee keer verlies» — verified European results, matchday-10 results, standings after 10 rounds, full matchday-12 programme; photo elftal1912.
- **P5 — Jongeren (B1, 18 ex.):** «Expeditie Robinson is begonnen!» — Robinson premiere follow-up, ADE (30 years) and DDW closings, youth climate actions; no photo on this page.
- **P6 — Verdieping (B2, 18 ex.):** «Geel, oranje, rood: hoe werken de codes?» — KNMI local-warning deep read, pro/contra local warnings, program-drawn chart explicitly labeled OEFENDATA (practice data, not a real survey: 100 jongeren — thuis 45, eerst tekst 25, toch naar buiten 20, weet niet 10).
- **P7 — Taal (A2/B1/B2, 12 ex.):** A2 klimaatwoorden; B1 scheidbare werkwoorden; B2 mening geven; PAS OP clinic (4 items); word «meedoen»; readers' corner (editor's example + invitation, see §6); 8 golden sentences; VOL.3 preview (Sinterklaas 15 Nov, Sint-Maarten 11 Nov, letters + best P8 texts).
- **P8 — Toets en antwoorden (38 ex.):** A kroniek (8), B algemene vragen (8), C lees en antwoord (4, Daan/Coevorden text), D maak de zinnen (4), E vertaal (4, re-aimed — see §5), F woorden match (4), G dialoog bij de bomen (5), H schrijf zelf (1); all 150 answers with English notes in dash style.

## 3. Measured exercise counts (registry output, identical to the core KIT §3)

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By type (English registry labels): complete 65, choice 44, matching 8, true or false 7, make sentences 8, cloze choice 13, translate 4, writing 1.
- Model essay (P8 H, ex. 150): **87 words** (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).

## 4. Gates — measured values (all builder-run; logs in hidden_files/weekly-report-w45-nl-en-build/)

- **Pages:** 8 (multiple of 4). SVGs 8, cards 8 at 1950×2700, print PDF 8 pages, web PDF 8 pages.
- **Core freeze:** `tools/freeze.py baseline` on the W45 NL core build reproduced the core **8/8 byte-identical** (tools venv) and re-hashed the shipped core unchanged; `freeze.py diff` core-vs-edition: added CJK characters **0 on every page**, edition CJK **0** (core CJK counts per page 191 / 212 / 153 / 126 / 214 / 192 / 373 / 1033 → edition 0). Every changed string belongs to the explanation layer, page furniture, the masthead badge/footers, or the re-aimed translation items (§5); no Dutch article, exercise body, option, fact or figure differs.
- **P8 printed-note set:** `tools/p8.py compare` (explicit P8 paths, total 150): core 150 noted, edition 150 noted, status **CLEAN**, missing [] extra 0 uncertain []. Keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148] — adjudicated in §5; no key is missing, no extra key, no SHORT.
- **Geometric occlusion audit:** `tools/occlusion_audit.py` (selftest OK): edition **0 flags**, core **0 flags**, NEW vs core **0**. Supplementary scans (build/rowcheck.py): same-baseline text-ink collisions **CLEAN on all 8 pages**; P6 chart-label ink vs later-drawn rects **0.0% coverage** (below the 30% threshold; an early 78.3% reading was a scan bug — PIL getbbox is ascender-relative, not baseline-relative — fixed by using getmetrics, and the canonical audit independently reads 0).
- **Gloss counts (split on · in the rendered gloss strings):** P2 6 = 6, P3 5 = 5, P4 5 = 5, P5 5 = 5, P6 5 = 5 — core 1:1 in every box. P1 bridge 4 items, P7 bridges 4 / 3 / 3 items, unchanged in count.
- **P7 golden sentences:** all 8 Dutch sentences occur exactly **2×** (source article page + P7), verbatim, with page tags identical to the core: Pagina 1, 1, 2, 3, 4, 5, 6, 6. Each sentence was confirmed on its tagged article page (P1 ×2, P2, P3, P4, P5, P6 ×2).
- **Readers' corner (§6):** no reader, letter, name or quote invented; the only letter on the page is the labeled editor's example.
- **Images:** only clearly public-domain/CC0 images, reused byte-identical from the core build assets (assets diff clean): P1 herfstbos, P2 kinderdijk, P3 gracht, P4 elftal1912. Every credited image is typeset on its page (1 `<image>` element per photo page; P5/P6/P7/P8 carry no photo, as in the core).
- **Image credits (from the Commons API Artist field, per the core KIT §5 / W43 CREDITS.md):** P1 Foto: Vovogov90 — CC0; P2 Foto: Nationaal Archief — CC0; P3 Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein. All four credit lines verified present in the rendered SVGs.
- **Banned-string scan (all 8 SVGs):** the banned intermediary term 0, spaced guillemets (« / ») 0, double spaces 0, CJK characters 0.
- **Footers:** 8/8 carry «De Lucerna · VOL.2 · Dutch text · English explanations · LUCERNA DUTCH WEEKLY» with «Page n of 8» (n = 1–8).
- **Build warnings:** final render log shows **zero FLOW OVERFLOW / HEAD TOO WIDE** warnings.
- **Visual inspection:** all 8 rendered PNG cards viewed page by page: clean, no overlaps, no cut-off text, no defects (including the fixed P1 agenda/word-note area, the P2 match set, the P6 chart, the P7 col-3 stack and the P8 key block foot).

## 5. What changed vs the core — and what did not

Rewritten into English (the whole explanation layer): every word gloss («Note | …» boxes, W43 measured form), every section instruction, the error-clinic notes, the readers'-corner notes, the teaser apparatus, the phrases-of-the-week translations, all 150 answer notes, all bilingual page headers and subtitles, the P1 numbers-box parentheticals, the P2 code-box labels, the P6 chart caption's second line, the readers' prompts (EN JIJ boxes), and the P8 answer-key header lines.

Unchanged: all Dutch articles, headlines, exercise bodies and options, all facts and figures, all images and credits, the chart geometry and values, and the answer keys except §5 items.

### P8 keydiff adjudication (compare output keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148])

- **Genuine re-aims (translation items, as in the W43 NL × EN precedent): 137, 138.** Exercises 137–138 keep their Dutch source sentences and are now translated **into English** (137 «The Climate Week lasts seven days.», 138 «Code orange means: be prepared.»). Exercises 139–140 swap direction — the printed source is now English and the key is the Dutch sentence, byte-identical to the core's keys (139 «Museumnacht duurt van 19:00 uur tot 02:00 uur.», 140 «Ik doe mee aan de Klimaatweek.»); 139/140 are therefore NOT in the keydiff, and 150's printed line is the translated writing-task pointer (apparatus) with the 87-word Dutch model text byte-identical.
- **Extraction artifacts, not key changes: 7, 17, 70, 71, 76, 96, 148.** For these seven, the printed answer token before the dash is byte-identical to the core (7 B, 17 wortelen, 70 eiland, 71 proef, 76 gaat winnen, 96 advies, 148 B); only the translated note differs. p8.py's paren branch swallows the note into its key field exactly when a note ends in a parenthetical (e.g. «wortelen = to take root (plural subject)», «eiland = island (het)», «zachte = soft (soil)») — the same artifact family as README #13. Verified against the printed P8 lines in both SVGs, not just the tool output.

### Layout adjudications (apparatus only — the Dutch core was never touched)

1. **P8 answer-key typography** follows the W43 NL × EN measured values: key lines at **13.0 pt / 1.14 leading** (core: 13.5 pt / 1.16), separator 13.5 pt / 1.17, flow bottom 2540. English notes are longer than the Chinese notes they replace; at the original size the key block overflowed (3 overflow warnings in the first render). Final lowest key baseline is well clear of the footer rule (keys flow ends y = 2332).
2. **P2 exercise spacing:** P2 exercise gaps 8 → 4 and section-head gaps 13 → 8 (P2 only). English bridges wrap to two lines where the Chinese bridges took one; without this the P2 match set overflowed its region (first-render overflow). Final P2 exercise flow ends y = 2402 (bottom 2580).
3. **P7 column-3 stack:** the English clinic notes, word gloss, disclosure and invitation were shortened to telegraphic form (W43 NL × EN precedent: short clinic notes) so the three-box stack ends at y = 1867, clear of the phrases rule at 1937 (first render ended 2071.5 and collided with the phrases section). No Dutch text, quote or preview text changed.
4. **P1 agenda note** split into two lines («See the articles on pages 2–4» / «for all dates and times.») and the **P1 word-of-the-week English gloss** shortened to two lines (««Climate»: the weather and nature around us, long-term. Climate Week is about our climate.») — the first render flagged both as occlusion defects (box-title overflow; last gloss line covered by the IN HET KORT box). Final audit: 0 flags.
5. **Masthead subtitle** shortened by one theme word per the W43 NL × EN precedent (the full Dutch topic line measured 1958.8 px against the 1820 px inner width): «WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · SPEELRONDE 12» (1581.9 px). MUSEUMNACHT stays in the headline, contents and P3 coverage.
6. **P6 chart title** shortened to «DE GRAFIEK · PRACTICE DATA» (355.5 px; the longer form measured 459.4 px against the 412 px box inner edge). The OEFENDATA label stays in the Dutch caption («OEFENDATA — verzonnen cijfers…») and the English caption («Practice data: invented numbers…»).

## 6. Readers' corner — honest note

No real reader letter exists for this issue. P7 prints a **clearly labeled editor's example** («Li (voorbeeldbrief van de redactie)», Dutch example letter text kept verbatim from the core) plus an on-page disclosure and invitation. All three facts are on the page, in Dutch and in English: (1) no real letters had arrived at press time, (2) no best page-8 texts had arrived, (3) the example stands with the promise carried to VOL.3. The explicit English public invitation, verbatim:

> Editors' example — not real. Send your real letters and best page-8 texts: we will print them in VOL.3!

(Imperative + publication promise; the contents-preview line and other pages' exercise prompts are not counted as the invitation.) The Dutch disclosure is kept verbatim: «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.» No reader, letter, name or quote was invented for this edition.

## 7. Furniture — measured attributes and W43 comparison

W43 shipped `files/weekly-report-nl-en/` measured from its SVGs (task rule: W43 measured beats README #20's generic text; tables.json has no established EN-native furniture column — `furniture en --target nl` errors — so the shipped W43 NL × EN SVG is the authority):

- **Pairing badge (P1 masthead, replaces the core's Dutch strapline at y = 372):** «TEXT IN DUTCH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS», centered x = 975, y = 372, 20 pt, bold, olive #3e4c2a, Noto Sans CJK SC; measured width 941.8 px (fits the 1820 px inner width). Identical string, size, weight, colour and slot to W43.
- **Footer (all pages):** «De Lucerna · VOL.2 · Dutch text · English explanations · LUCERNA DUTCH WEEKLY» (20 pt sans, grey, baseline 2624, footer rule y = 2580) with «Page n of 8» right-aligned — the W43 form with VOL.1 → VOL.2.
- **Gloss prefix:** «Note | » (W43 shipped gloss boxes, verified in the W43 SVGs; README #4's «Note — » note concerns the EN × FR KIT, not this family).
- **Page headers:** Dutch + English throughout (e.g. «LEVEN · LIFE», «CULTUUR · CULTURE», «JONGEREN · YOUNG PEOPLE», «VERDIEPING · IN DEPTH», «TAAL · LANGUAGE», «TOETS EN ANTWOORDEN · TEST AND ANSWERS»; «SPORT» is the same word in both languages, as in W43). Band sub-lines give the Dutch description followed by the English one. Section heads follow the W43 short forms («OEFENINGEN · EXERCISES ON PAGE N», «Answers on page 8 · levels are mixed; find your number», «DE WEEK IN CIJFERS · IN NUMBERS», «ZO ONTHOUD JE HET · REMEMBER», «EN JIJ? · AND YOU?», «BLIKSEMQUIZ · LIGHTNING QUIZ», «PAS OP! · ERROR CLINIC», «HET WOORD · WORD OF THE WEEK», «ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)», «VOLGENDE WEEK · NEXT WEEK (VOL.3)», «ANTWOORDEN · ANSWER KEY — grouped by page: find your number»).
- **P8 separator:** «— PAGINA {n} —» kept from the core (as in W43).
- **Top strip:** centre «ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH» (W43 string, 21 pt, measured 629.4 px); left «VOL. 2»; right week dates in Dutch, unchanged.
- **Family case (README #20):** the NL core has a native subtitle slot at y = 330 and a Dutch strapline at y = 372; the W43 NL × EN precedent replaces the strapline in place with the badge at y = 372 (20 pt bold olive) and rewrites the subtitle in Dutch — this edition follows that case exactly (no masthead shift, no inserted badge row; frozen elements below y = 606 unmoved).

## 8. Toolchain

- **run.py interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0 (same venv that reproduced the core baseline 8/8 byte-identical; system python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg, so it was NOT used).
- **render.py (CairoSVG) interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1 (system python3 lacks cairosvg, as the task states).
- **Pipeline:** one-process run.py (content12 → 34 → 56 → 7 → 8, so the exercise registry accumulates — never run modules standalone, never import them inside the core build dir, per README #11) → render.py (SVG → 1950×2700 PNG cards → print PDF via cairosvg+pypdf → web PDF JPEG q85 @1400 px).
- **Transform record:** build/transform.py (line-literal replacements with counts, plus the width fixes of §5) maps the core build to this build; build/rowcheck.py holds the supplementary scans. The core build directory was copied, never modified; repointing covered every OUT spelling (expanduser form) in content12/34/56/7/8 and render.py, verified by grep (no production output path in the build code points at the core dir; the only core-dir references left are read-only: rowcheck.py reads the core SVGs for gloss comparison, and transform.py holds the old strings as replacement sources).

## 9. Build rounds

1. **First render:** counts exact (150; levels/pages/types as §3), but P2 exercise overflow, P8 key overflow (3 warnings) and P7 col-3 collision (ends 2071.5) — fixed per §5 items 1–3.
2. **Fix 1:** zero build warnings; P2 ends 2402, P7 col-3 ends 1867, P8 keys end 2332 — but occlusion audit flagged 2 NEW P1 defects (agenda note box overflow; word-note line covered) — fixed per §5 item 4.
3. **Fix 2:** zero build warnings; occlusion edition 0 / core 0 / NEW 0; all gates in §4 re-run on the final render.
- **Fix-round baselines:** pre-fix sha256 of the edition's SVG/cards/PDFs written to build/fix1-baseline-sha256.txt before each re-render round, per the fix-round baseline rule.

## 10. Delivery note

- This edition is delivered as files only (builder-complete, NOT finalized — finalization needs the independent proofread gate). NOT pushed to git, NOT posted to Discord, NOT messaged anywhere (per task instruction).
- Files: `files/weekly-report-w45-nl-en/` — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700), `De-Lucerna-VOL2-EN.pdf` (print PDF, 8 pages), `De-Lucerna-VOL2-EN-web.pdf` (web PDF, 8 pages, under the 10 MB limit), `WEEKLY-KIT.md`, `ABSTRACT.txt`.
- Build tree: `hidden_files/weekly-report-w45-nl-en-build/` — build code (bslib4/content*/svglib/run/render), transform.py + transform-log.txt, rowcheck.py + rowcheck.txt, build logs (build-log.txt, build-log-fix1.txt, build-log-fix2.txt), freeze-diff.txt/json, p8-compare.txt, p8-core.txt, p8-ed.txt, occlusion-edition2.txt, occlusion-core.txt, occlusion-new2.txt, core-sha256-before.txt, fix1-baseline-sha256.txt.

## 11. Deliverable sizes and hashes (final render)

- `De-Lucerna-VOL2-EN.pdf` — 6,936,236 bytes, sha256 ec16a69816b1fd56ee41697251b4690b4847162dff04afbac0b5ab373857e2e2
- `De-Lucerna-VOL2-EN-web.pdf` — 1,014,608 bytes, sha256 c5b90ff411e2585034347bf5a3f6e6aaadcba0dae352ea6e9bd55f7188ec12e8
- SVGs (sha256): p1-voorpagina d9d99e8bc71cca76126970664ea6faae01c57a70675774d171e1b7cfc1ce6771; p2-leven c782e43df9069e4ddc90d80449910174edc2d1dec096e8c1a05e843c9e4a79eb; p3-cultuur eb758f2b2921b2b44cfa1372142ce2b2252cd3df6439ea27936a8693e46ccc36; p4-sport d1f252147c07a64c752c1ac5f09cac79c23f3cc63ba3e8847ac1d18521f589b0; p5-jongeren 2628a81dbb6140643e85627b2e86ef4bfda7d947082b82c9901caf9ce46cfcb7; p6-verdieping 3ca47d6eae20bf221149cb3210c9e7d6491f6216a9ed8d51119edf7b19516a59; p7-taal 0f2617d52f7896ae8053f58cc244047e4c0c7d94e5e9b1f58b760c9819c8729a; p8-toets 16575da45042063444367e89228e9961472fc08316a338dbc70f4e19c0497482
- Cards (sha256): p1 8909c8a8f53aa65cdbc5235e58bbe7acb6fa8202975ec2c4ca0a6adb3ce8c123; p2 93561cdcb95c67fa037fe3eaac68a256762c5c32a4d5f7f1053ed44ee0ee4e4b; p3 9d33589a17a1e10285c6d24c2b8258eac1eec001535a9071baf5301f0f230a21; p4 bbb31a86558d55d09917cd00148c7fd72342e2dae35cf112bcda41782449b17a; p5 4d1a61c37c94225b49f8df4a289a9006565b4a465e737fdef73b5a0f6ba8760c; p6 839d8e54954739655d5e59597f4e22b5eda6adcdec77595c5086786a49a3c943; p7 9bfe5d47ba84af408fd1dbe5d2f700f16c62894d3b554c55081eb3f4b310e3e6; p8 3a7d68d6d44a94c9700d4e965865a705c2b1de155ba6718db43e289b1ab2fcef

## 12. D5 rebuild (2026-11-14, builder run; not a proofread round)

D5: 讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK（SOP §1.1 字体修复）。D5-only 家族：新样式已在仓，单版施工只装 D5、重渲一次。

- Core 落盘（全家共用一次，v1 执行）：`apply_variant.py --patch-core nl --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-nl/svglib.py` +95/−3 行，`_D5_READER = "latin"`（D24：按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-nl-en/svglib.py --target nl --reader en --week 2026-w45`（先 `--check` dry-run，mode=latin）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（svglib.py 含 fix2 标记 13 处，安装器日志 "added fix2 block"）。
- 基线（修前生产版，venv 重建）：`run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；印 PDF 7,510,185 字节；印/网文字层 vs issues 已发 web PDF 字符多重集差 **0**；修前普查 D5 违规 **拉丁 497**（>0，符合装机前提）。旧 pin 与基线实测不符（de 例：KIT 印 7,918,211 B，基线实测 7,526,971 B）——KIT SHA 滞后（PLAN 修正案：基线永不以 KIT SHA 为准），本节 pin 以实测发运值订正，旧 §11 pin 已同步更新为本次值。
- 导出器（第 0 步自验）：`scratch-2026-w45-nl/export_text_w45nl.py`（AST 导出，源自 content*.py 字面量，绝不从 PDF 反提；无 hardcode，标题由参数传入）。基线试跑 vs issues 已发 `.text.md` **11/11 BYTE-IDENTICAL**；patched 导出同样 BYTE-IDENTICAL（门 15）。
- 修复（run1 → run2）：共 **9 处**，只动字号，零文字改动。run1 缺陷：栏头超宽 3 处（ru 除外，ru 栏头未超）、occlusion TEXTX 1 处（P7 B1 栏头 'SCHEIDBARE WERKWOORDEN' 与 'B2' 重叠 5.2×17.8px；ru 除外）、boxtitle/creambox 6 处（ru/zh-cn/zh-tw 为 0），ru 另有 spill 1 处（codes 行注 'внимательны' 框底溢出 BELOW +13.34px）。
  - `content12.py:48` 奶油框标题 DE WEEK IN CIJFERS　IN NUMBERS：tsize — → **tsize=20**（宽 443.9px，超框 39.2px；修后 385.9px，余量 16.7px）。
  - `content12.py:180` 奶油框标题 ZO ONTHOUD JE HET　REMEMBER：tsize — → **tsize=21**（宽 438.5px，超框 34.0px；修后 400.4px，余量 2.2px）。
  - `content12.py:70` p.text Agenda van de week　THIS WEEK'S EVENTS：19 → **18**（宽 409.9px，超 9.2px；修后 388.4px，余量 10.3px）。
  - `content12.py:91` p.text IN DEZE EDITIE　IN THIS ISSUE：24 → **23**（宽 408.6px，超 8.5px；修后 391.7px，余量 6.5px）。
  - `content56.py:162` p.text VOOR OF TEGEN?　FOR OR AGAINST?：21 → **19**（宽 424.1px，超 24.1px；修后 383.8px，余量 14.3px）。
  - `content7.py:84` p.text HET WOORD　WORD OF THE WEEK：23 → **20**（宽 438.5px，超 38.1px；修后 381.3px，余量 17.1px）。
  - `content12.py:176` 栏头 DRIE ACTIES VOOR DEZE WEEK：25 → **24**（宽 425.0px；修后 408.0px）。
  - `content34.py:21` 栏头 TWEEDEHANDS IS OOK CULTUUR：25 → **23**（宽 456.7px；修后 420.1px）。
  - `content7.py:32` 栏头 B1　SCHEIDBARE WERKWOORDEN：24 → **22**（宽 455.7px；修后 417.8px）。
- 门禁（run2，全套 16 门 + D18）：**ALL-GREEN**。run TOTAL 150 / head_check 0 defects / d5 census 拉丁 0、西里尔 0、CJK 内花括号 0 / render RC=0 / webpdf RC=0（网 PDF 1,014,608 B < 7 MB）/ occlusion 0 flags（selftest 6 类全触发）/ p8 extract 150/150 / p8 compare CLEAN（missing=[] extra=0，keydiff=[137, 138]，137/138 为读者语重定向真重 aim，已裁定，非缺陷) / freeze baseline 8/8 / freeze diff vs base 新增 CJK 字符 **0**（新增拉丁 strings 490，D5 run 拆分所致；对照是 base 修前生产版，不是 core）/ spill 0（1 OBSERVE）/ boxtitle 0 / edge 0 TOUCH 0 NEAR / creambox 0 defects（P8 228 → 228 行，距页脚线余量 46.6px）/ 文字层 print=web 字符多重集差 **0**（33,550 字符），text.md BYTE-IDENTICAL / census_quotes 0 defective / D18 刊头 gap **112.0px** > 0。
- 补充校验 G15b（carryover，诊断性，不计入 verdict）：共享 `verify_textmd.py` 对 nl 目标家族未标定（表按 pt 目标语格式标定），patched 与基线同态 FAIL（de 例：SVG-only 711 / MD-only 1119，基线 711 / 1121；ru、zh-cn 基线与 patched 残差完全相同）——D27 类已知工具口径差，非 D5 回归；内容不变的证据以门 15（AST 导出器 BYTE-IDENTICAL + print=web 差 0）为准。
- 最终 pin（builder 原件；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）：印 PDF `De-Lucerna-VOL2-EN.pdf` 6,936,236 B，SHA-256 `ec16a69816b1fd56ee41697251b4690b4847162dff04afbac0b5ab373857e2e2`；网 PDF `2026-w45-nl-en.web.pdf` 1,014,608 B，SHA-256 `c5b90ff411e2585034347bf5a3f6e6aaadcba0dae352ea6e9bd55f7188ec12e8`；text.md 38,208 B，SHA-256 `01cbf6b6ffa93bfcf66c267b4eab936965a14084728027536a23d09d48966606`（与 issues 已发版 BYTE-IDENTICAL）。
- Builder scratch：`hidden_files/d5-redo/scratch-2026-w45-nl/patched/2026-w45-nl-en/`；门禁总表复本（D29）：`production/notes/2026-w45/g-nl/scratch-d5-rebuild-nl/logs/2026-w45-nl-en/GATES-SUMMARY.txt`。
