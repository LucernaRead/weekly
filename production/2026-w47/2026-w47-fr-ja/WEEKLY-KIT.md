# Le Lucerna VOL.4 — Édition française pour lecteurs japonais (2026-W47)

**Edition:** `2026-w47-fr-ja` — French target, Japanese reader (`ja`)
**Week:** 2026-11-16 – 2026-11-22 (VOL.4)
**Status:** DONE — gates 15/15 PASS on run1 (2026-11-11)

## Build

- Core: `production/2026-w47/core-fr/` (reader zh-cn) — `expl.py` only swapped; `bslib4.py`,
  `content*.py`, `svglib.py`, `run.py` byte-identical to core (source_freeze PASS).
- Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PIL 13.0.0, PyMuPDF);
  freeze Direct 8/8 with the same interpreter as the build.
- 150 exercises (P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42);
  levels A2 53 / B1 75 / B2 22; chips 134 [10,12,18,15,14,15,12,38].
- Keys: 318 total — 158 reused from W46 ja / 160 new this week / 15 frozen
  (`band_p3`, `chart_sub`, `head_3dates`, `head_chiffres`, `head_comp6`, `head_foot`,
  `head_opinion`, `head_sortir`, `head_zoom`, `n_e4`, `n_futur2`, `n_futur3`, `n_futur4`,
  `n_neg1`, `outils_intro`). `gloss_prefix` "解説 — ", `note_wrap` "full" (P8 notes print
  as （note）), `page_line` "{n}ページ（全{total}ページ）", `p8_sep` "— {pg} ページ —".
- French golden sentences verbatim from P1–P6 (string_freeze PASS; 1 string excused:
  core `stem_e1` prefix `Traduisez: `, no Japanese counterpart in
  `決勝を見れば、フランス語を学んでいる。`).

## Pre-build work

- `align/ja.json` + `align/ref-ja.txt` (588 lines, read in full); `gen_expl.py ja` first failed
  on extra key `gp8` — gp8 is REUSED in align (W46 ja value identical to the new translation);
  removed from `fresh_ja.json` (154 keys), re-ran OK (318 keys).
- `precheck.py ja` PASS on first run (g1–g6 ≤5 lines; band_r1 calibrated start 1382.2).
- Pre-measured heads: `head_dieppe_ex` 252.2 ≤ 422.5, `head_mots_fetes` 286.7 ≤ 400.5,
  `head_mots_photo` 266.1 ≤ 400.5, `head_chart` 496.4 ≤ 829.0, `agenda_note` 209.0 ≤ 378.5.
- Pre-measured gp1–gp8 at 19.5px sans: only gp4 was 2 lines (445.6px) → shortened to
  `文法 | en beauté：美しく締めくくる。` (337.9px, 1L) before building.
- Diag (`diag-wd/ja/`, `ja/reg-ja.json`): stems match core (1/1/2/1/1 — stem_e3 1L vs core 2L,
  battery under core); keys diff 161px → batch 1 (18 shortenings, 6 reused→fresh moves:
  `n_chart1`, `n_micro6d`, `n_mcq_b8`, `n_cloze6`, `n_e5`, `n_d4`) → diff **101px ≤124**
  (p3 +1, p4 +1, p6 +1, p8 +2). Fresh count 160.

## run1 — GATES 15/15 PASS

- `run.py` exit 0; zero FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150.
- p8_extract 150/150, notes 121/150; p8_compare CLEAN, keydiff `[150]`; keycheck only Q150
  differs (core `开放题` → ja `自由作文`).
- Freeze direct 8/8: `8bf58ae5`, `db490888`, `83ad866a`, `8252ca19`, `cae84c75`, `7fdd8932`,
  `7a37897c`, `66b5fa78`.
- Text layer print/web byte-equal, 102,274 B; web PDF 2,310,518 B < 7MB; print PDF
  30,566,551 B (CJK fonts embed larger than Latin editions' ~17.4 MB).
- P8 min font 11.625pt ≥ 9.75pt; scans U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 ×8;
  string_freeze 0 unaccounted CJK chars (no Simplified Chinese residue);
  MCQ 45 bodies, 1,454 lines, 0 defects; widths 31 within budget.
- band_spans: FR title ends 1236.9, band_r1 starts 1380.0 (gap 143.1), FR sub ends 837.2,
  band_r2 starts 1430.1.


## Rebuild #2 — GATES 15/15 PASS (r2run1, 2026-11-11)

Rebuilt from core-fr fix4. Same 15 gates as #1, all PASS.

run exit 0 zero overflow; occlusion 0 flags; p8_extract; p8_compare CLEAN keydiff `[150]`;
source_freeze; string_freeze (1 string excused as translated E value);
freeze_direct 8/8; text_layer; p8_font; scans; chips; keycheck; mcq; widths; band_spans
(FR title ends 1236.9, band_r1 starts 1380.0; FR sub ends 837.2, band_r2 starts 1430.1).
P7 disclosure box (y=1878, bottom 2258.0): 末基线 2233.3，清除 +24.7; creambox BELOW-WINDOW 7 (all +24.0/+37.0 next-heading false positives).
Orphan punctuation: 0 new (core-inherited 1, font-split shared-baseline 0, recorded remnant 0).
Q148 key `devant le`, stem `On se retrouve ___ cinéma ?`; blank lines Q130 (P8) + P3 Q36/Q37 present, same relative positions as core (see FANOUT-REPORT-fr2.md).
## Files delivered

- Print PDF `La-Lucerna-VOL4-fr-ja.pdf` — 20,150,788 B, SHA-256 `40fa2fb8bd61497451148f9bedcd16b8b09e080c57f686de09f8078e290201ca`
- Web PDF `La-Lucerna-VOL4-fr-ja-web.pdf` — 2,021,505 B, SHA-256 `4249702230de8a3448d51aad3fa69fb080087543439688e7b9f2fdcd29d734ef`
- `.text.md` — 47,687 B, SHA-256 `fdf935955f1e3d6e67f4a4b8b64f4091a016ce59a2ae25959b3bce9645a69573`, 542 entries, 150 exercises
- Text layer: print/web byte-identical (93,507 chars each, multiset diff 0)
- Freeze (D5 r2, direct, two builds, SHA-256 first 8): [`0afa9c6a`, `21be28bf`, `7b93df4b`, `77b198c9`, `1fae947b`, `0f3a0e99`, `f1a9c6bc`, `bdde8366`] — 8/8
- Chips: 134 [10, 12, 18, 15, 14, 15, 12, 38]; P8 min font 11.625pt (834 spans, 551 at min); p8 extract 150/150, notes 121/150; p8 compare CLEAN, keydiff `[150]` (writing key only); MCQ 45 bodies, 1451 lines, 0 defects.
- U+2019 = 0, U+00B7 = 0, gold = 0, old paper = 0, #fbfaf6 ×8.
## Visual QA (run1, 8 pages at 100 dpi + 300 dpi P1 band crop)

- **Zero problems.** P1 band clean at 300 dpi (143-unit gap); subtitle
  `フランス語週刊　VOL.4　パリと上院` fits; agenda, DANS CE NUMÉRO, LE MOT DE LA SEMAINE,
  Atget photo, LE VOTE EN TROIS PHRASES, EN BREF, QUIZ ÉCLAIR all clean.
- P2 Châtillon photo; P3 Moreau painting + `BEAUJOLAIS　クイズ` head fits;
  P5 Méliès image; P6 calendar head `LE CALENDRIER　カレンダー（水曜に採決）` on one line;
  P7 Doré image, 8 phrases fit (gp4 wraps to 2 lines after the R2-1 fix, all fit), LE COURRIER box clear of `et ___.`;
  P8 Hiroshige image + caption, MODÈLE box visible.
- P3 `POUR OU CONTRE?` box has no Japanese line, P5 `debat5_note` appears twice — both
  match core.
- Span-gap analysis (serif lost-space class, ru lesson): **0 lost-space boundaries** on
  the print PDF (Japanese word + space + Latin/symbol).
- `.text.md` read through in full (1,087 lines): no Chinese residue, no typos spotted;
  answers consistent (Q41 B, Q45 A, Q79 B, Q80 B, Q120 B, Q121 A, Q122 B, Q135
  "Regarder une finale, c'est déjà apprendre le français.").
- Person names checked one by one against the French article text: Dhont (ドント, 4× in
  .text.md; "Dont" 0×), Ménochet (メノシェ), Fils (フィス), Haymitch (ヘイミッチ),
  Francis Lawrence (ローレンス), Mipo O, Alexandre Smia (スミア), Mounia Meddour
  (メドゥール), Kristin Scott Thomas, Guillermo Guiz (ギズ), Méliès, Doré, Hiroshige,
  Atget, Moreau. All katakana transliterations standard.
- Checked and left as is (reused W46 ja values, verified by grep): `bridge_dieppe`
  `ミニドリル　ボジョレー・クイズ。`; `head_lire` `LIRE LE CALENDRIER　カレンダー`;
  P3 ZOOM box gloss `1951年から早期販売、1985年から第3木曜日、2026年は75周年。` is a
  different E key from P8 note Q26 `1951年から早期販売` — correct, not unified (same as
  pt/nl/ru). Q102 note `(sortir = 公開される)` is the generic gloss; P7 gp6
  `sortir：公開される（動詞の形）。` is the same gloss in grammar form — both correct.
  Q150 note `自由作文 — 採点ポイントは枠内。モデルは8ページの枠内（ポイント制で採点）`
  is a reused W46 ja value.

## Fix log

- **Rebuild #2 (2026-11-11, r2run1)** — rebuilt from core-fr fix4 (Q148 key `devant`→`devant le`, stem drops `du`; P4 `chiffres_note` drops 「决赛」). #1 edition backed up to `scratch-refanout-fr2/backup-old/`.
- 孤儿日文句号 。×3 修（均缩短 1–2 字使句号不独行，重扫 0 新增）：
  (1) P1 g1：`un vin primeur　le beaujolais ボジョレー 新酒。` 删 `新酒`（释义仍存于 g2 与 m_p8d/m_primeur2 `primeur = 新酒`）；
  (2) P4 bridge_comp4：`比較級（plus / moins）で文を完成させよう。`→`比較級（plus / moins）で文を完成しよう。`（1 行）；
  (3) P6 bridge_chart：`上のカレンダーを読んで正しい答えを選ぼう。`→`上のカレンダーを読んで答えを選ぼう。`（1 行）。
  改动页：P1、P4、P6（另 P8 为核心 fix4 之 Q148）。
- P7 披露框：ja 版原先即 2 行、末基线 2233.3、清除 +24.7，重建后 creambox 重测仍干净；PIL 真墨末行至 svg y=2234.4，间隙零墨。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- Changed pages vs #1: P1（8bf58ae5→0111ee1c）、P4（8252ca19→2b64f954）、P6（7fdd8932→11f2a3c3）、P8（66b5fa78→bf40c3c0）; all other pages byte-identical.
- Core fix4 SHAs: print 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`; web 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`; text 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`.

- run0 (pre-build): gp4 2L → 1L; keys-diff batch 1 (18 shortenings). No rebuild needed after
  run1 — run1 passed 15/15 and visual QA was clean.
- Independent reproof gloss fix, fix1 (2026-11-12): P1 NOTE `g1` adds 日语译注 `un vin primeur 新酒` (same gloss already in P2 g2; cf. fr-en `a new wine`, core `新酒`); P7 `head_clinic` adds `CLINIQUE DES ERREURS　誤り` (gloss from this edition's own `bridge_clinic`). Note: the P1 gloss had been deliberately dropped in rebuild #2 to fix an orphaned 。— re-adding it reflows the NOTE; gates green and visual crop verified, no orphan reintroduced. Source `expl.py`; text.md re-export diff vs pre-fix exactly 2 lines (L45, L921). Gates: occlusion 0, p8 CLEAN, boxtitle 0 DEFECT (41 titles), spill 0, edge 0/0, census PASS, print/web text layers byte-identical (93,346 chars); zero warnings. SHAs: print 20,149,418 B `3121d66228dd…`, web 2,019,912 B `8c52331f7ce6…`, text 47,524 B `354f6b094247…`. Full log: scratch-fix-fr/FIX-LOG.md.
- Second-round reproof fix, r2 (2026-11-12, PROOF-NOTE-2 R2-1): P7 grammar head `gp4` `en beauté` → `se terminer en beauté` (verb restored; cf. de/en/es/it/pt/zh-tw + core), and P8 answer 100 note `n_gp4` aligned the same way (`100. beauté (se terminer en beauté = 美しく締めくくる)`). Source `expl.py:175,292`; text.md re-export diff vs pre-fix exactly 2 lines (L893, L1079; dry-run to /tmp first, no dropped titles). Gates: run 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0, p8 CLEAN keydiff `[150]` (vs pre-fix baseline `[]`), boxtitle 0 DEFECT (41 titles), spill 0/104, edge 0/0, census PASS, print/web text layers byte-identical (93,507 chars); P7 visual crop verified, gp4 wraps to 2 lines, complete, no overflow. SHAs: print 20,149,490 B `f3f9d526f158…`, web 2,019,995 B `a1951960b852…`, text 47,548 B `d243033462d4…`. Full log: scratch-fix2-w47-fr/FIX-LOG-2.md.

## Visual QA — rebuild #2 (r2run1, 8 pages at 100 dpi; changed pages + P7 box-bottom 200 dpi crop)

Zero problems. Changed pages vs #1: P1（8bf58ae5→0111ee1c）、P4（8252ca19→2b64f954）、P6（7fdd8932→11f2a3c3）、P8（66b5fa78→bf40c3c0）.

## D5 rebuild (2026-11-12, r2)

- D5 installed mode=cjk (`apply_variant.py --target fr --reader ja`; `assert_routing.py` cjk PASS, `_D5_READER='cjk'`). Pre-D5 svglib md5 `f25bfcfc`, byte-identical to core-fr pre-D5. Baseline in `scratch-d5-rebuild-fr/2026-w47-fr-ja/baseline/` (svg ×8 + svglib.py + assets), census-pre 445.
- NOTE on source_freeze: ja svglib differs from core-fr by design under CJK, not just the `_D5_READER` line — JP index (`_jp_index` vs `_sc_index`), "Noto Serif/Sans CJK JP" faces, and a kinsoku block (lines 244–386) ported from core-zh-tw by the installer. The "only `_D5_READER` differs" landing approval applies to Latin/Russian editions; CJK editions follow CJK-DECISION §1 (script-based routing). Do not revert to core to satisfy the old gate.
- r1 defects (4 HEAD TOO WIDE, 1 TEXTX, 3 boxtitle / 3 creambox): P6-ex `LIRE LE CALENDRIER　カレンダー`, P6-opinion + P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`, P6-micro `LE COMPARATIF EN POLITIQUE`; P1 TEXTX French headline vs `アルカラス優勝　上院は水曜に採決` 9.2×26.0px; boxtitle P3 `LES DATES EN CHIFFRES` +7.6, P4 `LES PHRASES DU COMMENTATEUR` +36.5, P6 `TROIS DATES POUR COMPRENDRE` +24.5.
- Fixes (r1→r2, 10): the 8 core fixes verbatim (head_zoom 23→22, P4 box title `tsize=21`; head_cine 23→20, grammar head 25→23, head_comp6 25→24, P6 box title `tsize=21`; grammar head 24→23, head_clinic 25→23) + ja-specific: `band_r1` drops `アルカラス優勝　` (→`上院は水曜に採決`), `head_lire` 25→23 (measured 441.5→406.2px < CW 422.5). `.text.md` re-exported (export47.py) + Japanese headers restored from pre-fix copy; diff vs pre-fix exactly 1 line (band_r1). New `.text.md` SHA `df028d09d5db…` (47,508 B, 542 entries, 150 exercises).
- r2 all green: run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0 flags (selftest OK); boxtitle 0 DEFECT (41 titles, 394 body lines); creambox PASS 0 defects (n=495, median 1.014, bold 1.049, regular 1.002; P8 191→191 lines, slack 37.1→37.1); spill 0 (33 boxes, 105 candidates); edge 0 TOUCH / 0 NEAR; census PASS (0/0/0); `census_quotes.py` 0 defective; text layers byte-identical (93,208 chars each); p8 compare vs core-fr CLEAN keydiff `[150]`, vs pre-fix baseline CLEAN keydiff `[]`; freeze baseline 8/8; freeze diff vs core added CJK 2323, vs pre-fix base added CJK 1 (one U+3000 reflow separator, acceptable).
- PDF 8 pages, 6 embedded images (P8 Hiroshige present); flow ends P6-deep 1258/1300, P6-ex 2402/2560, P7-phrases 1718/1830, P8-keys 2106/2560 (Hiroshige threshold 2170, margin 64).
- Three-point verification PASS: production print/web SHA = r2 gate-log `shas.txt` = KIT above (text SHA from the re-export, `df028d09d5db…`); production svglib.py contains `_D5_READER` (cjk); KIT synced to production actual SHAs. Freeze build-copies (r1, r2) deleted after r2; `freeze-r*.json`, baselines and logs kept.

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-ja/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：11月20日金曜日　子どもの日／11月21日土曜日　トリノ準決勝＋ごみ減量週間初日），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（41 titles）；creambox PASS 0 defects；spill 0（104 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 101,179 字节，93,589 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 20,150,788 B `40fa2fb8bd61…`、网 2,021,505 B `4249702230de…`、文 47,687 B `fdf935955f1e…`。
