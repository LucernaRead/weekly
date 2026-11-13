# Le Lucerna VOL.4 — Édition française pour lecteurs de chinois traditionnel (2026-W47)

**Edition:** `2026-w47-fr-zh-tw` — French target, Traditional Chinese reader (`zh-tw`)
**Week:** 2026-11-16 – 2026-11-22 (VOL.4)
**Status:** DONE — gates 15/15 PASS on run2 (2026-11-11)

## Build

- Core: `production/2026-w47/core-fr/` (reader zh-cn) — `expl.py` only swapped; `bslib4.py`,
  `content*.py`, `svglib.py`, `run.py` byte-identical to core (source_freeze PASS).
- Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PIL 13.0.0, PyMuPDF);
  freeze Direct 8/8 with the same interpreter as the build.
- 150 exercises (P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42);
  levels A2 53 / B1 75 / B2 22; chips 134 [10,12,18,15,14,15,12,38].
- Keys: 318 total — 163 reused from W46 zh-tw / 155 new this week / 24 frozen
  (`band_p3`, `band_p5`, `box_action`, `box_allez`, `bridge_micro6`, `chart_sub`,
  `head_3dates`, `head_chiffres`, `head_comp6`, `head_foot`, `head_opinion`,
  `head_outils`, `head_sortir`, `head_zoom`, `instr_fill`, `n_e4`, `n_futur2`,
  `n_futur3`, `n_futur4`, `n_neg1`, `outils_intro`, `p8_cloze`, `p8_sep`, `page_line`).
  `gloss_prefix` "譯注｜", `note_wrap` "full" (P8 notes print as （note）),
  `page_line` "第{n}版／共{total}版", `p8_sep` "— 第{pg}版 —".
- Simplified/Traditional Chinese are INDEPENDENT editions — no conversion of the core's
  Simplified values; every value is native Traditional (Taiwan usage: 杜林 for Turin,
  薄酒萊 for Beaujolais Nouveau, 藍軍 for Les Bleus, 阿爾卡拉斯, 謝爾頓).
- French golden sentences verbatim from P1–P6 (string_freeze PASS; 1 string excused:
  core `stem_e1` prefix `Traduisez: `, no Traditional counterpart in
  `看一場決賽，就是在學法語。`).

## Pre-build work

- `align/zh-tw.json` + `align/ref-zh-tw.txt` (588 lines, read in full); `gen_expl.py zh-tw`
  OK (318 keys). gp8 was REUSED in align (W46 zh-tw value identical) and left out of
  `fresh_zh-tw.json` (154 keys).
- Simplified-residue scan (heuristic Simplified-only char set: 为/说/学/发/头/让/认/识/
  读/听/传/统/华/实/质/义/习/会/还/买/卖/费/贵/动/对/应/开/车/马/门/问/边/过/达/迟/
  选/际/东/进/远/连/这): **NONE** in fresh values, reused values, the full expl, or the
  final `.text.md`. (First scan flagged 定 7× — false positive: 定 is the same glyph in
  both scripts.)
- `precheck.py zh-tw` PASS on first run (g1–g6 ≤5 lines; band_r1 calibrated start 1407.6).
- Pre-measured heads: `head_dieppe_ex` 302.9 ≤ 422.5, `head_mots_fetes` 332.7 ≤ 400.5,
  `head_mots_photo` 312.1 ≤ 400.5, `head_chart` 448.4 ≤ 829.0, `agenda_note` 209.0 ≤ 378.5.
- Pre-measured gp1–gp8 at 19.5px sans: **all 1 line** (gp5 closest at 415.9px of 422.5).
- Diag (`diag-wd/zh-tw/`, `zh-tw/reg-zh-tw.json`): stems match core (1/1/2/1/1 — stem_e3
  1L vs core 2L, battery under core); keys diff **0px** on every page (Traditional
  conversion wraps identically to the Simplified core) — no shortening batch needed.

## run1 — GATES 13/15 (real defect, value-level fix)

- p8_extract 150/150 but notes **120/150**; p8_compare SHORT (core 121, edition 120).
  Missing note: **Q150 only**.
- Root cause (diagnosed in `tools/p8.py`): Q150's segment ends with the Hiroshige caption
  after the note, so `last_paren_group` (which requires the paren group to be trailing)
  finds nothing; and the dash path needs `" — "` (spaced). The core's Q150 key uses
  spaced `' — '`, the en/la editions' keys too — but the reused W46 zh-tw `writing_key`
  used unspaced `'——'` (`開放題——評分點在方框內；範文在第8版方框內`), so neither path
  fired. The note itself (`按點評分`) was printed correctly; only the extractor missed it.
- Fix (value level, matches the core's own Q150 typography): moved `writing_key` from
  reused to fresh with `開放題 — 評分點在方框內；範文在第8版方框內` (only the dash
  changed). Fresh count 155.
- All other 13 gates passed on run1 (freeze 8/8, text layer byte-equal, band_spans
  FR title ends 1236.9 / band_r1 starts 1405.0).

## run2 — GATES 15/15 PASS

- `run.py` exit 0; zero FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150.
- p8_extract 150/150, notes 121/150; p8_compare CLEAN, keydiff `[150]`; keycheck only Q150
  differs (core `开放题` → zh-tw `開放題`).
- Freeze direct 8/8: `bc9050c8`, `7e372c72`, `f3280832`, `5af79c73`, `a1981b77`, `81a3f8ff`,
  `087855db`, `86da3308` (only P8 changed vs run1).
- Text layer print/web byte-equal, 101,806 B; web PDF 2,558,076 B < 7MB; print PDF
  30,551,968 B (CJK fonts embed larger than Latin editions' ~17.4 MB).
- P8 min font 11.625pt ≥ 9.75pt; scans U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 ×8;
  string_freeze 0 unaccounted CJK chars (no Simplified residue);
  MCQ 45 bodies, 1,445 lines, 0 defects; widths 31 within budget.
- band_spans: FR title ends 1236.9, band_r1 starts 1405.0 (gap 168.1), FR sub ends 837.2,
  band_r2 starts 1571.4.


## Rebuild #2 — GATES 15/15 PASS (r2run1, 2026-11-11)

Rebuilt from core-fr fix4. Same 15 gates as #1, all PASS.

run exit 0 zero overflow; occlusion 0 flags; p8_extract; p8_compare CLEAN keydiff `[150]`;
source_freeze; string_freeze (1 string excused as translated E value);
freeze_direct 8/8; text_layer; p8_font; scans; chips; keycheck; mcq; widths; band_spans
(FR title ends 1236.9, band_r1 starts 1405.0; FR sub ends 837.2, band_r2 starts 1571.4).
P7 disclosure box (y=1878, bottom 2258.0): 末基线 2233.3，清除 +24.7; creambox BELOW-WINDOW 7 (all +24.0/+37.0 next-heading false positives).
Orphan punctuation: 0 new (core-inherited 2, font-split shared-baseline 0, recorded remnant 1).
Q148 key `devant le`, stem `On se retrouve ___ cinéma ?`; blank lines Q130 (P8) + P3 Q36/Q37 present, same relative positions as core (see FANOUT-REPORT-fr2.md).
## Files delivered

- Print PDF `La-Lucerna-VOL4-fr-zh-tw.pdf` — 18,534,108 B, SHA-256 `cb5588ff6fcc942c00983313d6b4db5a5751583b346988f57503f4834ec6ec46`
- Web PDF `La-Lucerna-VOL4-fr-zh-tw-web.pdf` — 2,077,328 B, SHA-256 `3f66ddae87f4d5c726b38d67dff27962761d04a1b02a15c7a3d802476a9e9875`
- `.text.md` — 46,129 B, SHA-256 `659dc0c5d5afbfbbfda0a2e36867329eaac648d765c39247d0a9e2dd9ee63ff7`, 542 entries, 150 exercises
- Text layer: print/web byte-identical (93,502 chars each, multiset diff 0)
- Freeze (D5 r2, direct, two builds, SHA-256 first 8): [`4b48d178`, `a078ab99`, `5cbffbd7`, `294acd2c`, `eaaca5e8`, `e4266b64`, `76d84860`, `a234e5e7`] — 8/8
- Chips: 134 [10, 12, 18, 15, 14, 15, 12, 38]; P8 min font 11.625pt (828 spans, 532 at min); p8 extract 150/150, notes 121/150; p8 compare CLEAN, keydiff `[150]` (writing key only); MCQ 45 bodies, 1442 lines, 0 defects.
- U+2019 = 0, U+00B7 = 0, gold = 0, old paper = 0, #fbfaf6 ×8.
## Visual QA (run2, 8 pages at 100 dpi + 300 dpi P1 band crop)

- **Zero problems.** P1 band clean at 300 dpi (168.1-unit gap); subtitle
  `法語週報　VOL.4　巴黎與參議院的一週` fits; agenda, DANS CE NUMÉRO, LE MOT DE LA SEMAINE,
  Atget photo, LE VOTE EN TROIS PHRASES, EN BREF, QUIZ ÉCLAIR all clean.
- P2 Châtillon photo; P3 Moreau painting + `BEAUJOLAIS　薄酒萊小測` head fits;
  P5 Méliès image; P6 calendar head `LE CALENDRIER　行事曆（表決在週三）` on one line;
  P7 Doré image, 8 phrases fit (gpN all 1 line), LE COURRIER box clear of `et ___.`;
  P8 Hiroshige image + caption, MODÈLE box visible; Q150 now reads
  `150. 開放題 — 評分點在方框內；範文在第8版方框內（按點評分）`.
- P3 `POUR OU CONTRE?` box has no Traditional line, P5 `debat5_note` appears twice — both
  match core.
- Span-gap analysis (serif lost-space class, ru lesson): **0 lost-space boundaries** on
  the print PDF (Traditional word + space + Latin/symbol).
- `.text.md` read through in full (1,087 lines): all Traditional, no Simplified residue,
  no typos spotted; answers consistent (Q41 B, Q45 A, Q79 B, Q80 B, Q120 B, Q121 A,
  Q122 B, Q135 "Regarder une finale, c'est déjà apprendre le français.").
- Person names checked one by one against the French article text: Dhont (東特, 4× in
  .text.md; "Dont" 0×), Ménochet (梅諾謝), Fils (菲斯), Haymitch (海米奇),
  Francis Lawrence (勞倫斯), Mipo O, Alexandre Smia (斯米亞), Mounia Meddour
  (梅杜爾), Kristin Scott Thomas, Guillermo Guiz (吉茲), Méliès (梅里愛), Doré (多雷),
  Hiroshige (廣重 — caption stays French), Atget (阿特熱), Moreau (莫羅).
  All Taiwan transliterations standard.
- Checked and left as is (reused W46 zh-tw values, verified by grep): `bridge_dieppe`
  `微練習　薄酒萊小測。`; `head_lire` `LIRE LE CALENDRIER　行事曆`;
  P3 ZOOM box gloss `1951年獲准提前售酒、1985年定為11月第三個星期四、2026年是這場約會的75週年。`
  is a different E key from P8 note Q26 `1951年獲准提前售酒` — correct, not unified
  (same as pt/nl/ru/ja/ko). Q102 note `(sortir 上映)` is the generic gloss; P7 gp6
  `sortir：上映、出版（動詞變化）。` is the grammar form — both correct.
  Q150 note `按點評分` is a reused W46 zh-tw value.

## Fix log

- **Rebuild #2 (2026-11-11, r2run1)** — rebuilt from core-fr fix4 (Q148 key `devant`→`devant le`, stem drops `du`; P4 `chiffres_note` drops 「决赛」). #1 edition backed up to `scratch-refanout-fr2/backup-old/`.
- D1 簡體殘留「准」→「準」（翻譯映射 准→準；`zoom_note` 與 `n_vf1` 各一處，現 expl.py 准 0 個、準 2 個；核心本身正確簡體，未動核心）。
- D2 孤兒 。×3 修（均縮短使句號不獨行，重掃 0 新增）：
  (1) P2 gloss 框 `bridge_valise`：`註｜virgule 逗號　voter 投票　fêter 慶祝　une valise 行李箱。` 刪 `une `（1 行）；
  (2) P2 ET VOUS 框 `etvous_note`：`說說話你的11月19日：用法語寫兩句寄來。` 刪 `話`（1 行）；
  (3) P3 ZOOM 框 `zoom_note`：刪 `這場約會的`（2 行，句號落於第 2 行行末）。
  改動頁：P2、P3（另 P8 為核心 fix4 之 Q148）。
- P4 殘留（只記錄，不修）：`chiffres_note` 繁體釋義 `大師賽決賽結果與杜林名單見本版正文。` 仍 387.0px、折 2 行，句號獨行於 P4 y=550.53（該基線僅此一元素，確為視覺孤兒）。核心 fix4 刪的是法文注裡的「決賽」，讀者語釋義未同步——按任務“只記錄”留給 proof2 定奪。
- P7 披露框：zh-tw 版原先即 2 行、末基線 2233.3、清除 +24.7，重建後 creambox 重測仍干净；PIL 真墨末行至 svg y=2235.4，間隙零墨。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- Changed pages vs #1: P2（7e372c72→b46154cf）、P3（f3280832→22af3699）、P8（86da3308→7b8c6116）; all other pages byte-identical.
- Core fix4 SHAs: print 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`; web 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`; text 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`.

- run0 (pre-build): no shortening batch (diag diff 0px); gpN all 1 line.
- run1 13/15 → run2 15/15: `writing_key` `——` → ` — ` (see above). Only P8 changed.
- Independent reproof gloss fix, fix1 (2026-11-12): P2 note `virgule 逗號` → `une virgule 逗號` (article restored; all other 10 editions have `une`); P7 `head_clinic` adds `CLINIQUE DES ERREURS　易錯診所` (Traditional form of core `易错诊所`). Source `expl.py`; text.md re-export diff vs pre-fix exactly 2 lines (L229, L921). Gates: occlusion 0, p8 CLEAN, boxtitle 0 DEFECT (40 titles), spill 0, edge 0/0, census PASS, print/web text layers byte-identical (93,502 chars); zero warnings. SHAs: print 18,532,970 B `3f4f58df81c3…`, web 2,076,083 B `6972666e0e72…`, text 46,011 B `e257f1023046…`. Full log: scratch-fix-fr/FIX-LOG.md.
- Second-round reproof fix, r2 (2026-11-12, PROOF-NOTE-2 R2-3): P8 answer 93 note `93. ont rejeté（眾議員否決收入部分）` → `93. ont rejeté（議員否決收入部分）` (aligned with core-fr `议员否决收入部分`; answer key `ont rejeté` unchanged). Source `expl.py:285` (`n_micro6b`); text.md re-export diff vs pre-fix exactly 1 line (L1075; dry-run to /tmp first, no dropped titles). Gates: run 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0, p8 CLEAN keydiff `[150]` (vs pre-fix baseline `[]`), boxtitle 0 DEFECT (40 titles), spill 0/104, edge 0/0, census PASS, print/web text layers byte-identical (93,502 chars); zero warnings. SHAs: print 18,532,749 B `e6ef33ce2f62…`, web 2,075,855 B `0d6b19e48c69…`, text 46,008 B `3dc051e14be0…`. Full log: scratch-fix2-w47-fr/FIX-LOG-2.md.

## Visual QA — rebuild #2 (r2run1, 8 pages at 100 dpi; changed pages + P7 box-bottom 200 dpi crop)

Zero problems. Changed pages vs #1: P2（7e372c72→b46154cf）、P3（f3280832→22af3699）、P8（86da3308→7b8c6116）.

## D5 rebuild (2026-11-12, r2)

- D5 installed mode=cjk (`apply_variant.py --target fr --reader zh-tw`; `assert_routing.py` cjk PASS, `_D5_READER='cjk'`). Pre-D5 svglib md5 `f25bfcfc`, byte-identical to core-fr pre-D5. Baseline in `scratch-d5-rebuild-fr/2026-w47-fr-zh-tw/baseline/` (svg ×8 + svglib.py + assets), census-pre 439.
- NOTE on source_freeze: installed zh-tw svglib is byte-identical to core-fr svglib (still SC faces / `_sc_index`) — the installer does not switch reader zh-tw to TC faces; TC faces belong to the core-zh-tw TARGET, while the fr-zh-tw reader edition used SC faces pre-D5 as well (md5 matched all fan-outs). D5 changed no face variant here; do not hand-switch to TC.
- r1 defects (3 HEAD TOO WIDE, 3 boxtitle / 3 creambox): P6-opinion + P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`, P6-micro `LE COMPARATIF EN POLITIQUE`; boxtitle P3 `LES DATES EN CHIFFRES` +7.6, P4 `LES PHRASES DU COMMENTATEUR` +36.5, P6 `TROIS DATES POUR COMPRENDRE` +24.5. head_lire (`LIRE LE CALENDRIER　行事曆`) and band_r1 (`阿爾卡拉斯奪冠　參議院週三表決`) NOT flagged — occlusion 0 — so no zh-tw-specific content changes.
- Fixes (r1→r2): the 8 core fixes verbatim (head_zoom 23→22, P4 box title `tsize=21`; head_cine 23→20, grammar head 25→23, head_comp6 25→24, P6 box title `tsize=21`; grammar head 24→23, head_clinic 25→23). `.text.md` untouched by r1/r2 (size-only fixes); its 6 B difference vs the rebuild-#2 KIT record (45,998 B) predates this rebuild, headers verified Traditional Chinese.
- r2 first attempt was killed by a runtime restart during render.py (render.log 0 bytes, production PDFs still the r1 versions); verified no residual processes and re-ran r2 in full. Results below are from the completed re-run.
- r2 all green: run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0 flags (selftest OK); boxtitle 0 DEFECT (40 titles, 380 body lines); creambox PASS 0 defects (n=486, median 1.017, bold 1.049, regular 1.000; P8 188→188 lines, slack 36.1→36.1); spill 0 (33 boxes, 104 candidates); edge 0 TOUCH / 0 NEAR; census PASS (0/0/0); `census_quotes.py` 0 defective; text layers byte-identical (93,337 chars each); p8 compare vs core-fr CLEAN keydiff `[150]`, vs pre-fix baseline CLEAN keydiff `[]`; freeze baseline 8/8; freeze diff vs core added CJK 970, vs pre-fix base added CJK 0.
- PDF 8 pages, 6 embedded images (P8 Hiroshige present); flow ends P6-deep 1258/1300, P6-ex 2402/2560, P7-phrases 1718/1830, P8-keys 2026/2560 (Hiroshige threshold 2170, margin 144 — widest in the family).
- Three-point verification PASS: production print/web/text SHA = r2 gate-log `shas.txt` = KIT above; production svglib.py contains `_D5_READER = "cjk"`; KIT synced to production actual SHAs. Freeze build-copies (r1, r2) deleted after r2; `freeze-r*.json`, baselines and logs kept.

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-zh-tw/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：11月20日星期五　兒童節／11月21日星期六　杜林準決賽＋減廢週首日），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（40 titles）；creambox PASS 0 defects；spill 0（104 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 100,023 字节，93,565 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 18,534,108 B `cb5588ff6fcc…`、网 2,077,328 B `3f66ddae87f4…`、文 46,129 B `659dc0c5d5af…`。
