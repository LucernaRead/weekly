# Le Lucerna VOL.4 — Édition française pour lecteurs coréens (2026-W47)

**Edition:** `2026-w47-fr-ko` — French target, Korean reader (`ko`)
**Week:** 2026-11-16 – 2026-11-22 (VOL.4)
**Status:** DONE — gates 15/15 PASS on run1 (2026-11-11)

## Build

- Core: `production/2026-w47/core-fr/` (reader zh-cn) — `expl.py` only swapped; `bslib4.py`,
  `content*.py`, `svglib.py`, `run.py` byte-identical to core (source_freeze PASS).
- Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PIL 13.0.0, PyMuPDF);
  freeze Direct 8/8 with the same interpreter as the build.
- 150 exercises (P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42);
  levels A2 53 / B1 75 / B2 22; chips 134 [10,12,18,15,14,15,12,38].
- Keys: 318 total — 164 reused from W46 ko / 154 new this week / 14 frozen
  (`chart_sub`, `head_3dates`, `head_chiffres`, `head_comp6`, `head_foot`,
  `head_opinion`, `head_sortir`, `head_zoom`, `n_e4`, `n_futur2`, `n_futur3`, `n_futur4`,
  `n_neg1`, `outils_intro`). `gloss_prefix` "해설 — ", `note_wrap` "full" (P8 notes print
  as （note）), `page_line` "제 {n} 면 / 총 {total} 면", `p8_sep` "— 제 {pg} 면 —".
- French golden sentences verbatim from P1–P6 (string_freeze PASS; 1 string excused:
  core `stem_e1` prefix `Traduisez: `, no Korean counterpart in
  `결승을 보면, 프랑스어를 배우는 것이다.`).

## Pre-build work

- `align/ko.json` + `align/ref-ko.txt` (588 lines, read in full); `gen_expl.py ko` OK on
  first run after one fix: my `bridge_match5` contained U+00B7 (`영화·환경`) — SOP §1.1
  forbids `·` in print; changed to `영화와 환경 단어를 뜻과 연결하세요.` (gen_expl
  asserts no U+00B7/U+2019/`"` in any value). gp8 was REUSED in align (W46 ko value
  identical to the new translation) and was left out of `fresh_ko.json` (154 keys).
- `precheck.py ko` PASS on first run (g1–g6 ≤5 lines; band_r1 calibrated start 1439.9).
- Pre-measured heads: `head_dieppe_ex` 223.9 ≤ 422.5, `head_mots_fetes` 260.0 ≤ 400.5,
  `head_mots_photo` 262.4 ≤ 400.5, `head_chart` 387.8 ≤ 829.0, `agenda_note` 174.2 ≤ 378.5.
- Pre-measured gp1–gp8 at 19.5px sans: only gp4 was 2 lines (430.0px) → shortened to
  `문법 | en beauté: 아름답게 마무리하다.` (1L) before building.
- Diag (`diag-wd/ko/`, `ko/reg-ko.json`): stems match core (1/1/2/1/1 — stem_e3 1L vs core 2L,
  battery under core); keys diff **101px ≤124** (p3 +1, p4 +1, p6 +1, p8 +2) — no
  shortening batch needed (same profile as ja).

## run1 — GATES 15/15 PASS

- `run.py` exit 0; zero FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150.
- p8_extract 150/150, notes 121/150; p8_compare CLEAN, keydiff `[150]`; keycheck only Q150
  differs (core `开放题` → ko `자유 작문`).
- Freeze direct 8/8: `4e1d1ac2`, `c172ea06`, `591b514a`, `5cf88f14`, `946a7778`, `77321a37`,
  `b1769f84`, `b533645f`.
- Text layer print/web byte-equal, 102,735 B; web PDF 2,048,862 B < 7MB; print PDF
  23,103,417 B (CJK fonts embed larger than Latin editions' ~17.4 MB).
- P8 min font 11.625pt ≥ 9.75pt; scans U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 ×8;
  string_freeze 0 unaccounted CJK chars (no Simplified Chinese residue);
  MCQ 45 bodies, 1,449 lines, 0 defects; widths 31 within budget.
- band_spans: FR title ends 1236.9, band_r1 starts 1436.9 (gap 200.0), FR sub ends 837.2,
  band_r2 starts 1563.3.


## Rebuild #2 — GATES 15/15 PASS (r2run1, 2026-11-11)

Rebuilt from core-fr fix4. Same 15 gates as #1, all PASS.

run exit 0 zero overflow; occlusion 0 flags; p8_extract; p8_compare CLEAN keydiff `[150]`;
source_freeze; string_freeze (1 string excused as translated E value);
freeze_direct 8/8; text_layer; p8_font; scans; chips; keycheck; mcq; widths; band_spans
(FR title ends 1236.9, band_r1 starts 1436.9; FR sub ends 837.2, band_r2 starts 1563.3).
P7 disclosure box (y=1878, bottom 2258.0): 末基线 2233.3，清除 +24.7; creambox BELOW-WINDOW 7 (all +24.0/+37.0 next-heading false positives).
Orphan punctuation: 0 new (core-inherited 2, font-split shared-baseline 13, recorded remnant 0).
Q148 key `devant le`, stem `On se retrouve ___ cinéma ?`; blank lines Q130 (P8) + P3 Q36/Q37 present, same relative positions as core (see FANOUT-REPORT-fr2.md).
## Files delivered

- Print PDF `La-Lucerna-VOL4-fr-ko.pdf` — 20,086,951 B, SHA-256 `827e6bb2d43352e46f369ba89386dcd9d1fd83354e3206c96d162709483438e9`
- Web PDF `La-Lucerna-VOL4-fr-ko-web.pdf` — 1,924,132 B, SHA-256 `00b0f37c9a4571da76e00cecce776ed05d06c42821567945290accfb0b9a3b9a`
- `.text.md` — 47,510 B, SHA-256 `b9e6af86a01eb23a1a4bf726d134f29fae80d43da83ff86df88ca079b62f601d`, 542 entries, 150 exercises
- Text layer: print/web byte-identical (95,023 chars each, multiset diff 0)
- Freeze (D5 r2, direct, two builds, SHA-256 first 8): [`84b79449`, `ed0efa63`, `97989738`, `87d7745e`, `f9e6dee0`, `a625b622`, `82f17174`, `788f7c60`] — 8/8
- Chips: 134 [10, 12, 18, 15, 14, 15, 12, 38]; P8 min font 11.625pt (881 spans, 554 at min); p8 extract 150/150, notes 121/150; p8 compare CLEAN, keydiff `[150]` (writing key only); MCQ 45 bodies, 1449 lines, 0 defects.
- U+2019 = 0, U+00B7 = 0, gold = 0, old paper = 0, #fbfaf6 ×8.
## Visual QA (run1, 8 pages at 100 dpi + 300 dpi P1 band crop)

- **Zero problems.** P1 band clean at 300 dpi (200-unit gap); subtitle
  `프랑스어 주간지　VOL.4　파리와 상원` fits; agenda, DANS CE NUMÉRO, LE MOT DE LA SEMAINE,
  Atget photo, LE VOTE EN TROIS PHRASES, EN BREF, QUIZ ÉCLAIR all clean.
- P2 Châtillon photo; P3 Moreau painting + `BEAUJOLAIS　퀴즈` head fits;
  P5 Méliès image; P6 calendar head `LE CALENDRIER　달력(수요일 표결)` on one line;
  P7 Doré image, 8 phrases fit (gp4 wraps to 2 lines after the R2-1 fix, all fit), LE COURRIER box clear of `et ___.`;
  P8 Hiroshige image + caption, MODÈLE box visible.
- P3 `POUR OU CONTRE?` box has no Korean line, P5 `debat5_note` appears twice — both
  match core.
- Span-gap analysis (serif lost-space class, ru lesson): **0 lost-space boundaries** on
  the print PDF (Hangul word + space + Latin/symbol).
- `.text.md` read through in full (1,087 lines): no Chinese residue, no typos spotted;
  answers consistent (Q41 B, Q45 A, Q79 B, Q80 B, Q120 B, Q121 A, Q122 B, Q135
  "Regarder une finale, c'est déjà apprendre le français.").
- Person names checked one by one against the French article text: Dhont (돈트, 4× in
  .text.md; "Dont" 0×), Ménochet (메노셰), Fils (피스), Haymitch (헤이미치),
  Francis Lawrence (로렌스), Mipo O, Alexandre Smia (스미아), Mounia Meddour
  (메두르), Kristin Scott Thomas, Guillermo Guiz (기즈), Méliès, Doré, Hiroshige,
  Atget, Moreau. All Hangul transliterations standard.
- Checked and left as is (reused W46 ko values, verified by grep): `bridge_dieppe`
  `미니 드릴　보졸레 퀴즈.`; `head_lire` `LIRE LE CALENDRIER　달력`;
  P3 ZOOM box gloss `1951년부터 조기 판매, 1985년부터 세 번째 목요일, 2026년은 75주년.`
  is a different E key from P8 note Q26 `1951년부터 조기 판매` — correct, not unified
  (same as pt/nl/ru/ja). Q102 note `(sortir = 개봉하다)` is the generic gloss; P7 gp6
  `sortir: 개봉하다(동사 형태).` is the same gloss in grammar form — both correct.
  Q150 note `자유 작문 — 채점 포인트는 상자 안. 모범 답안은 8면 상자 안（포인트 채점）`
  is a reused W46 ko value.

## Fix log

- **Rebuild #2 (2026-11-11, r2run1)** — rebuilt from core-fr fix4 (Q148 key `devant`→`devant le`, stem drops `du`; P4 `chiffres_note` drops 「决赛」). #1 edition backed up to `scratch-refanout-fr2/backup-old/`.
- 本版无 proof1 遗留修复项；仅核心 fix4 变化落地（Q148，见下）。
- P7 披露框：ko 版原先即 2 行、末基线 2233.3、清除 +24.7，重建后 creambox 重测仍干净；PIL 真墨末行至 svg y=2234.4，间隙零墨。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- 孤儿扫：2 处字体分拆同基线标点（P8 `.` 与 `）`，与同行词共享基线，非视觉孤儿，记为 shared_baseline；新增真孤儿 0。
- Changed pages vs #1: P8（b533645f→fc7999be）; all other pages byte-identical.
- Core fix4 SHAs: print 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`; web 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`; text 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`.

- run0 (pre-build): `bridge_match5` U+00B7 → `와`; gp4 2L → 1L. No shortening batch.
- run1 gates first ran 14/15: `string_freeze` flagged the fullwidth parens `（`/`）`
  as unaccounted CJK — they are emitted structurally by the renderer (`fmt_note`,
  note_wrap="full") around every P8 note, not translation content; ja passed only
  incidentally because its gp values contain them. Fixed in `gates.py` (the two chars
  are now always allowed in the CJK audit, with a comment); re-ran gates on the
  unchanged run1 build → **15/15 PASS**. No rebuild needed. This fix also covers
  zh-tw (same note_wrap="full").
- Independent reproof gloss fix, fix1 (2026-11-12): P7 `head_clinic` adds `CLINIQUE DES ERREURS　오류` (gloss from this edition's own `bridge_clinic`). Source `expl.py`; text.md re-export diff vs pre-fix exactly 1 line (L921). Gates: occlusion 0, p8 CLEAN, boxtitle 0 DEFECT (47 titles), spill 0, edge 0/0, census PASS, print/web text layers byte-identical (94,860 chars); zero warnings. SHAs: print 20,086,243 B `bfeb8970f59f…`, web 1,923,201 B `d972b7cbc104…`, text 47,332 B `fd2dfe488c05…`. Full log: scratch-fix-fr/FIX-LOG.md.
- Second-round reproof fix, r2 (2026-11-12, PROOF-NOTE-2 R2-1): P7 grammar head `gp4` `en beauté` → `se terminer en beauté` (verb restored; cf. de/en/es/it/pt/zh-tw + core), and P8 answer 100 note `n_gp4` aligned the same way (`100. beauté (se terminer en beauté = 아름답게 마무리하다)`). Source `expl.py:175,292`; text.md re-export diff vs pre-fix exactly 2 lines (L893, L1079; dry-run to /tmp first, no dropped titles). Gates: run 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0, p8 CLEAN keydiff `[150]` (vs pre-fix baseline `[]`), boxtitle 0 DEFECT (47 titles), spill 0/136, edge 0/0, census PASS, print/web text layers byte-identical (95,023 chars); P7 visual crop verified, gp4 wraps to 2 lines, complete, no overflow. SHAs: print 20,086,280 B `acb99672c246…`, web 1,923,242 B `f7341f1a0a4f…`, text 47,356 B `4929e183f280…`. Full log: scratch-fix2-w47-fr/FIX-LOG-2.md.

## Visual QA — rebuild #2 (r2run1, 8 pages at 100 dpi; changed pages + P7 box-bottom 200 dpi crop)

Zero problems. Changed pages vs #1: P8（b533645f→fc7999be）.

## D5 rebuild (2026-11-12, r2)

- D5 installed mode=cjk (`apply_variant.py --target fr --reader ko`; `assert_routing.py` cjk PASS, `_D5_READER='cjk'`). Pre-D5 svglib md5 `f25bfcfc`, byte-identical to core-fr pre-D5. Baseline in `scratch-d5-rebuild-fr/2026-w47-fr-ko/baseline/` (svg ×8 + svglib.py + assets), census-pre 442. NOTE: installer ports the kinsoku block for ja only — ko svglib has no kinsoku block (by design); ko freeze ran fine under the venv (8/8 + diff), so the Pillow-10 system-python3 exception did NOT trigger and was not used.
- NOTE on source_freeze: ko svglib differs from core-fr by design under CJK (KR index `_kr_index`, "Noto Serif/Sans CJK KR" faces), not just the `_D5_READER` line. The "only `_D5_READER` differs" landing approval applies to Latin/Russian editions; CJK editions follow CJK-DECISION §1. Do not revert to core to satisfy the old gate.
- r1 defects (3 HEAD TOO WIDE, 3 boxtitle / 3 creambox, p8 SHORT missing=[150]): P6-opinion + P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`, P6-micro `LE COMPARATIF EN POLITIQUE`; boxtitle P3 `LES DATES EN CHIFFRES` +7.6, P4 `LES PHRASES DU COMMENTATEUR` +36.5, P6 `TROIS DATES POUR COMPRENDRE` +24.5; p8 SHORT — Q150 note present in the P8 SVG at the right place but p8.py failed to extract it (see tool fix below). head_lire (`LIRE LE CALENDRIER　달력`, 2-char gloss) and band_r1 (`알카라스 우승　상원 수요일 표결`) were NOT flagged — occlusion 0 — so no ko-specific content changes.
- Fixes (r1→r2): the 8 core fixes verbatim (head_zoom 23→22, P4 box title `tsize=21`; head_cine 23→20, grammar head 25→23, head_comp6 25→24, P6 box title `tsize=21`; grammar head 24→23, head_clinic 25→23). `.text.md` untouched (size-only fixes; SHA unchanged from pre-fix).
- Tool fix (shared `tools/p8.py`, `detect_note`): D5 splits a CJK sans line into per-script runs and a run starting with a space loses it at a line break, so the Q150 note joined as `자유 작문 —채점…` (space after `—` gone); the `" — "` dash test missed, the segment fell through to paren style, and `last_paren_group()` took the `(1797-1858)` from the Hiroshige caption swallowed into the last entry — key 150 lost. Fix restores the space when `—` is directly followed by a CJK char (source E values always write the dash with spaces; only the D5 lost-space artifact produces `—`+CJK). Regression-verified: fr-ko extract 120→121 noted (key150=`자유 작문`), fr-ko baseline / fr-ja / fr-ru / core-fr extracts unchanged (all 121). The rendered page was always correct (all Q150 words at y=2036.7/2056.8); the PDF text layer still drops inter-word spaces in that note (same known svglib limitation as fr-ru's lost spaces — visual spacing correct by run positioning).
- r2 all green: run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0 flags (selftest OK); boxtitle 0 DEFECT (47 titles, 546 body lines); creambox PASS 0 defects (n=493, median 1.014, bold 1.053, regular 0.999; P8 189→189 lines, slack 45.7→45.7); spill 0 (33 boxes, 136 candidates); edge 0 TOUCH / 0 NEAR; census PASS (0/0/0); `census_quotes.py` 0 defective; text layers byte-identical (94,860 chars each); p8 compare vs core-fr CLEAN keydiff `[150]`, vs pre-fix baseline CLEAN keydiff `[]`; freeze baseline 8/8; freeze diff vs core added CJK 2560, vs pre-fix base added CJK 1 (one U+3000 reflow separator, acceptable).
- PDF 8 pages, 6 embedded images (P8 Hiroshige present); flow ends P6-deep 1258/1300, P6-ex 2402/2560, P7-phrases 1718/1830, P8-keys 2086/2560 (Hiroshige threshold 2170, margin 84).
- Three-point verification PASS: production print/web/text SHA = r2 gate-log `shas.txt` = KIT above; production svglib.py contains `_D5_READER = "cjk"`; KIT synced to production actual SHAs. Freeze build-copies (r1, r2) deleted after r2; `freeze-r*.json`, baselines and logs kept.

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-ko/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：11월 20일 금요일　어린이의 날／11월 21일 토요일　토리노 준결승 + 쓰레기 줄이기 주간 첫날），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（47 titles）；creambox PASS 0 defects；spill 0（136 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 101,987 字节，95,117 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 20,086,951 B `827e6bb2d433…`、网 1,924,132 B `00b0f37c9a45…`、文 47,510 B `b9e6af86a01e…`。
