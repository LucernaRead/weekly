# WEEKLY-KIT — 2026-W47 fr-ru (Russian reader)

- Week: 2026-11-16 – 2026-11-22 (VOL.4)
- Core: `2026-w47-fr-zh-cn` (reader = Simplified Chinese); this edition = reader Russian (ru).
- Expl: 318 keys — 131 reused from W46 ru, 187 new, 14 frozen (French-only heads).
  `gloss_prefix` "Пояснение — ", `note_wrap` "half".
- Build interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PIL 13.0.0, PyMuPDF).
  Freeze re-run with the same interpreter; never system python3.
- Naming (fr family): print `La-Lucerna-VOL4-fr-ru.pdf`, web `La-Lucerna-VOL4-fr-ru-web.pdf` (dash).

## Files

- Print PDF `La-Lucerna-VOL4-fr-ru.pdf` — 17,222,512 B, SHA-256 `ade6694fcd1ac0c8ba76e0ecf4fbbf86a0b01f64f343c45356643ebe4ceffd14` (fixfam1, 2026-11-13; fix-ru2 17,222,281 B `af7d37bc0a56…`; pre-fix 17,222,306 B `1aa7c71d7f2e93e2…`)
- Web PDF `La-Lucerna-VOL4-fr-ru-web.pdf` — 1,774,094 B, SHA-256 `4acb91b39968307ab8b1f47a3f3ed20574668e64ed519743eb2b1fedd896d918` (minor1-revert rebuild 2026-11-13; content identical to fixfam1 — print SHA `ade6694fcd1a…` and text SHA `69d348831b05…` unchanged, text layer 96,948 chars; fixfam1 web 1,774,107 B `9de461db64ed…`; fix-ru2 1,773,854 B `f6e82ee074cf…`; pre-fix 1,773,870 B `85c45f1cff4640c6…`)
- `.text.md` — 50,693 B, SHA-256 `69d348831b05b30a91f6497da0f455324ba4c50145ed7ed3b8ee4e8253cea12b`, 542 entries, 150 exercises
- Text layer: print/web byte-identical (96,948 chars each, multiset diff 0)
- Freeze (D5 r1, direct, two builds, SHA-256 first 8): [`08fa5423`, `bd65bf21`, `e21de010`, `37754b6c`, `efc93cdc`, `ee01d3e6`, `44dae27c`, `10644821`] — 8/8
- Chips: 134 [10, 12, 18, 15, 14, 15, 12, 38]; P8 min font 11.625pt (502 spans, 244 at min); p8 extract 150/150, notes 121/150; p8 compare CLEAN, keydiff `[150]` (writing key only); MCQ 45 bodies, 1477 lines, 0 defects.
- U+2019 = 0, U+00B7 = 0, gold = 0, old paper = 0, #fbfaf6 ×8.
## Gates (r2run1, 2026-11-11 — rebuild #2 from core-fr fix4): 15/15 PASS

run exit 0 zero overflow; occlusion 0 flags; p8_extract; p8_compare CLEAN keydiff `[150]`;
source_freeze; string_freeze (1 string excused as translated E value);
freeze_direct 8/8; text_layer; p8_font; scans; chips; keycheck; mcq; widths; band_spans
(FR title ends 1236.9, band_r1 starts 1284.4; FR sub ends 837.2, band_r2 starts 1479.3).
P7 disclosure box (y=1878, bottom 2258.0): 末基线 2233.3，清除 +24.7; creambox BELOW-WINDOW 7 (all +24.0/+37.0 next-heading false positives).
Orphan punctuation: 0 new (core-inherited 1, font-split shared-baseline 14, recorded remnant 0).
Q148 key `devant le`, stem `On se retrouve ___ cinéma ?`; blank lines Q130 (P8) + P3 Q36/Q37 present, same relative positions as core (see FANOUT-REPORT-fr2.md).
## Fix log

- **Rebuild #2 (2026-11-11, r2run1)** — rebuilt from core-fr fix4 (Q148 key `devant`→`devant le`, stem drops `du`; P4 `chiffres_note` drops 「决赛」). #1 edition backed up to `scratch-refanout-fr2/backup-old/`.
- P7 读者园地奶油盒溢出修：`courrier_disclosure` 删中句 “в этом номере печатается помеченный редакционный пример.”（该信息已由 P7 法文示例标注句覆盖），3 行→2 行；末基线 2260.6→2233.3、creambox 清除 -2.6→+24.7（desc-clear +18.8）；PIL 真墨实测：披露灰字末行墨至 svg y=2237.3，盒底 2258.0 之下 2258–2270 白纸间隙零墨（仅 P7 哈希变）。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- 孤儿扫检测器修正（本轮）：ru 初扫 14 处“新增”均为西里尔/拉丁字体分拆的同基线行末标点（`:`/`.` 独立 `<text>` 元素，与同行词共享基线，如 Q139 `Итоги ещё неизвестны.` 之句号），非视觉孤儿；检测器已补同基线判定，ru 重扫 0 新增、14 处记为 shared_baseline（旧 ja 3 处真孤儿 。与旧 zh-tw 3 处 。+P4 残留仍原样检出，证明判定未放水）。
- Changed pages vs #1: P7（e825ca39→04f6feb7）、P8（3cdf7e52→a92673d4）; all other pages byte-identical.
- Core fix4 SHAs: print 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`; web 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`; text 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`.

- Pre-build: keys-flow diagnostic diff 383px (need ≤124 — longest of the family so far;
  pt/nl were 282). Batch 1: 45 note shortenings, 12 reused→fresh moves; stem_e1
  2L→1L → diff 242px. Batch 2: 29 further shortenings, 16 moves → 141px.
  Batch 3: 7 shortenings, 4 moves → 121px ✓. Fresh count 187.
  Pre-build head sweep (es/it/pt/nl failure class): head_dieppe_ex `BEAUJOLAIS　ТЕСТ`
  (240.5), head_mots_fetes `LES MOTS DU VIN　ВИНО` (286.0), head_mots_photo
  `MOTS DU CINÉMA　КИНО` (288.6), head_chart (759.6) all within budget from the start.
- Precheck fixes before build: band_r1 `АЛЬКАРАС ПОБЕДИЛ　СЕНАТ ГОЛОСУЕТ В СР.`
  calibrated start 1192.1 <1252 → `АЛЬКАРАС ПОБЕДИЛ　ГОЛОСУЕТ В СР.` (start 1285.1;
  «СЕНАТ» dropped — the adjacent French title supplies it; won + vote + Wednesday kept).
  agenda_note 455.5 > 378.5 → `Торжественное голосование: среда 18.` (361.6).
  gp1–gp8 all 2 lines at 19.5px (core 1 line) → all cut to 1 line before building
  (nl P7-phrases lesson). g6 6 lines with the 12-char prefix `Пояснение — ` →
  `une navette челнок` (prefix counts; measured without it first, wrongly passed).
  gp8 was REUSED in align (W46 value) and had to be moved to fresh to shorten it.
- run1 gates 15/15 PASS on first build (battery 1427.52, keys end 2045.7, Hiroshige 2055.7).
- run1 visual QA found a real defect class in the SERIF renderer (see below):
  3 lost spaces in the whole edition (PyMuPDF span-gap analysis):
  P4 chiffres_note `Итог финалаMasters` and `Турина—`, P8 stem_e1 `Смотреть финал—`.
  Root cause: svglib `Page.text` emits one `<text>` per same-font run; a run that
  STARTS with a space (space is always Newsreader) loses it in CairoSVG, so a
  Cyrillic word + space + Latin word/symbol renders joined. Sans text is immune
  (Noto Sans CJK covers Latin too — one run). W46 ru shipped the IDENTICAL
  chiffres_note artifact (same span bbox [1203.8, 378.1] on its P4) — pre-existing
  renderer limitation, not introduced here; the fix belongs in shared svglib
  (out of builder scope; source_freeze requires svglib byte-identical to core).
- run2 fixes (value level only): chiffres_note → `Итог финала и состав Турина:
  см. текст на этой странице.` (dropped the Latin word; colon attaches correctly);
  stem_e1 → `Смотреть финал: учить французский.` (1L, 390px; colon run `: ` keeps
  its trailing space). Re-ran span-gap analysis on run2: **0 lost-space boundaries**.
  Gates 15/15 PASS again (only P4/P8 freeze shas changed).
- Independent reproof gloss fix (2026-11-12): P1 `sommaire_title` adds `DANS CE NUMÉRO　СОДЕРЖАНИЕ`; `head_cine` adds `LE CINÉMA DU MERCREDI　КИНО`; `head_lire` adds `LIRE LE CALENDRIER　КАЛЕНДАРЬ`; `head_outils` adds `BOÎTE À OUTILS　ИНСТРУМЕНТЫ`; P7 `head_clinic` adds `CLINIQUE DES ERREURS　ОШИБКИ` (glosses from this edition's own wording / standard Russian equivalents). fix1: boxtitle 1 DEFECT (P1 sommaire +10.9px) + 3 HEAD TOO WIDE warnings. fix2 (font sizes only, D5 precedent): `content12.py:93` sommaire 24→22, `content56.py:135` head_lire 25→23, `content7.py:58` head_outils 27→25, `content7.py:99` head_clinic 25→23. fix2 gates all green, 0 warnings: occlusion 0, boxtitle 0 DEFECT, spill 0/107, edge 0/0, census PASS, p8 CLEAN, text layers multiset diff 0 (97,022 chars). Source `expl.py`; text.md re-export diff vs pre-fix exactly 5 lines (L109, L655, L723, L855, L921). SHAs: print 17,332,080 B `038ee398d117…`, web 1,882,292 B `f0e9d27b3934…`, text 50,513 B `3b6f2cf61934…`. Full log: scratch-fix-fr/FIX-LOG.md.
- Second-round reproof fix, r2 (2026-11-12, PROOF-NOTE-2 R2-1): P7 grammar head `gp4` `en beauté` → `se terminer en beauté` (verb restored; cf. de/en/es/it/pt/zh-tw + core), and P8 answer 100 note `n_gp4` aligned the same way (`100. beauté (se terminer en beauté = красиво)`). Source `expl.py:175,292`; text.md re-export diff vs pre-fix exactly 2 lines (L893, L1079; dry-run to /tmp first, no dropped titles). Gates: run 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0, p8 CLEAN keydiff `[150]` (vs pre-fix baseline `[]`), boxtitle 0 DEFECT (43 titles), spill 0/107, edge 0/0, census PASS, print/web text layers byte-identical (97,242 chars); P7 visual crop verified, gp4 wraps to 2 lines, complete, no overflow. Creambox FAIL 3 defects — same adjudicated false positive as r1 (P5 `debat5_note` duplicate matched to its second occurrence; independent spill_sweep 0 SPILL). SHAs: print 17,332,158 B `387991e60727…`, web 1,882,380 B `5fdfbf439848…`, text 50,537 B `1985e95d9be2…`. Full log: scratch-fix2-w47-fr/FIX-LOG-2.md.

## Notes (checked, left as is)

- Bare-French heads (`head_cine` LE CINÉMA DU MERCREDI, `head_outils` BOÎTE À OUTILS,
  `head_3dates`, `head_chiffres`, `head_clinic`, `head_comp6`, `head_foot`, `head_opinion`,
  `head_sortir`, `head_zoom`, `head_lire` LIRE LE CALENDRIER, `sommaire_title`
  DANS CE NUMÉRO) are reused W46 ru values — the ru edition's own pattern. Not defects.
- P3 ZOOM box Russian gloss `Продажа раньше срока с 1951, третий четверг с 1985,
  75-летие в 2026.` is a different E key from P8 note Q26 `Продажа с 1951` —
  different wording is correct, not unified (same as pt/nl).
- P3 `POUR OU CONTRE?` box has no Russian line; P5 `debat5_note` appears twice —
  both match core.
- Person names verified against French article text: Донт (1× Cyrillic in .text.md,
  "Dont" 0×; the French article text keeps Latin "Lukas Dhont"), Меноше, Фис,
  Хеймитч, Francis Lawrence, Mipo O, Alexandre Smia, Mounia Meddour,
  Kristin Scott Thomas, Guillermo Guiz, Méliès, Doré, Hiroshige, Atget, Moreau.
- Q150 note: "Открытый вопрос — баллы в рамке; образец в рамке на с. 8 (По баллам)".

## Visual QA (run2, 8 pages at 100 dpi + 300 dpi P1 band crop + 300 dpi P4 chiffres + P8 E135 crops)

Zero problems. P1 band clean at 300 dpi (FR title / Russian band clearly separated);
P2 Châtillon photo; P3 Moreau painting + `BEAUJOLAIS　ТЕСТ`; P5 Méliès image;
P6 calendar head on one line; P7 Doré image, 8 phrases fit, LE COURRIER box clear;
P8 Hiroshige image + caption, MODÈLE box visible. Span-gap analysis: 0 lost spaces.

## Visual QA — rebuild #2 (r2run1, 8 pages at 100 dpi; changed pages + P7 box-bottom 200 dpi crop)

Zero problems. Changed pages vs #1: P7（e825ca39→04f6feb7）、P8（3cdf7e52→a92673d4）.

## D5 rebuild (2026-11-12, r1)

- D5 installed mode=ru (`apply_variant.py --target fr --reader ru`, 10 changes; `assert_routing.py` ru PASS, `_D5_READER='ru'`). Pre-D5 svglib md5 `f25bfcfc`, byte-identical to core-fr pre-D5; svglib now differs from core-fr by exactly the `_D5_READER` line (`"ru"` vs `"cjk"`). Baseline in `scratch-d5-rebuild-fr/2026-w47-fr-ru/baseline/` (svg ×8 + svglib.py + assets), census-pre Latin 450 + Cyrillic 301.
- r1 all green on first run — no fix loop needed: run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; occlusion 0 flags (selftest OK); boxtitle 0 DEFECT (41 titles, 358 body lines); spill 0 (33 boxes, 106 candidates, 106 OBSERVE); edge 0 TOUCH / 0 NEAR; census PASS (curly 0/0/0); `census_quotes.py` 0 defective; text layers byte-identical (97,297 chars each); p8 compare vs core-fr CLEAN keydiff `[150]`, vs pre-fix baseline CLEAN keydiff `[]`; freeze baseline 8/8; freeze diff vs core added CJK 7 (all U+3000), vs pre-fix base added CJK 0.
- 8 core head-size fixes NOT applied: ru heads already fit at pre-D5 sizes (head_zoom 23, head_cine 23, grammar head 25, head_clinic 25, no P4 `tsize=21`) — r1 0 HEAD TOO WIDE / occlusion 0 / boxtitle 0 DEFECT. content34/56/7.py differ from core-fr only in those head sizes. Forcing core sizes would shrink ru heads for no gate reason.
- Creambox r1 reported FAIL 3 defects — ADJUDICATED measurement false positive (same class as the pilot's retracted P8 `·` TEXTX flags): all 3 are the P5 `debat5_note` (Кино или дома? …) matched to its SECOND occurrence. D5 reflow rewrapped the first occurrence (Cyrillic wider under Noto Sans: line 1 `Кино или дома? Старая вещь обретёт` → `Кино или дома? Старая вещь`), so the baseline strings survive verbatim only in the duplicate at y=2326.6; the audit takes `cands[0]` by exact text and calls it "spilled below box". Verified in the current P5 SVG: first occurrence lines at y=780.6/811.0/841.5, all inside box#1 (bottom 887.9), full sentence present, nothing truncated; second occurrence unchanged from baseline; independent spill_sweep 0 SPILL. No content change made; the audit's exact-text matcher cannot tell a rewrapped duplicate from a spill — defect class noted for the mechanism owner (needs word-coverage matching, not a content edit).
- `.text.md` untouched by r1 (mtime 2026-11-11 18:34 UTC, predates this rebuild); headers verified Russian, Q148 `devant le` ×1, `debat5_note` ×2, band_r1 `АЛЬКАРАС ПОБЕДИЛ　ГОЛОСУЕТ В СР.`. The 35 B difference vs the rebuild-#2 KIT record (50,453 B) predates this rebuild.
- PDF 8 pages, 6 embedded images (P8 Hiroshige present); flow ends P6-deep 1288/1300, P6-ex 2527/2560, P7-phrases 1718/1830, P8-keys 2086/2560 (Hiroshige threshold 2170, margin 84).
- Three-point verification PASS: production print/web SHA = gate-log `shas.txt` = KIT above; production svglib.py contains `_D5_READER` (ru); KIT synced to production actual SHAs. Freeze build-copy deleted after r1; `freeze-r1.json`, baselines and logs kept.

## fix-xru (2026-11-12, SOP §1.1)

- `svglib.py` 的 `_D5_READER == "ru"` 分支把拉丁文路由到 Noto Sans CJK，违反 SOP §1.1；分支已删（标记 `[removed 2026-11-12 fix-xru]`），恒走 else 逻辑——拉丁文 → Newsreader，西里尔文 → Noto Sans。
- 重建：`driver.sh fr`（run.py rc=0，TOTAL 150；render.py rc=0；文字层字符多重集 pre/post 一致，35,438 非空格字符；webpdf.py rc=0，8 页）。
- 探针（SVG runs）：修前 LAT@NotoSans=4485 LAT@Newsreader=19446 CYR@NotoSans=5256；修后 LAT@NotoSans=0 LAT@Newsreader=23931 CYR@NotoSans=5256（不变）。8 个 SVG 全部已变。
- 注意：run.py 现报 7 条 HEAD TOO WIDE（P6-ex、P6-opinion、P6-micro ×2、P7-B2、P7-outils、P7-clinic）——D5 重建时为 0 条，此处未重门禁，仅报协调员。
- 文件：印刷版 `La-Lucerna-VOL4-fr-ru.pdf` 17,222,455 B，SHA-256 `e2c48b75df809f736ebe7b2c0da82f8ef7a08f5f19c6c4a93ad1a18d4456a7fd`（改前 17,332,158 B `387991e60727…`）；网页版 `La-Lucerna-VOL4-fr-ru-web.pdf` 1,774,012 B，SHA-256 `5387c82a986126fb70713880279fd49ed817b30a85f64c40e7d34bed77a6908f`（改前 1,882,380 B `5fdfbf439848…`）；text.md 未变，50,537 B，SHA-256 `1985e95d9be2482a94b0ef2b58f14640f8f82ed8ede3c091a9e274830140fa6a`。无重试。

## fix-ru2 (2026-11-13, coordinator #4 repair — 5 gate regressions + B1 answer 141)

- Cause: the fix-xru reroute (Latin → wider Newsreader) introduced 5 regressions
  vs D5 rebuild r2 (0 flags / 0 DEFECT then); gate-final 2026-11-13 00:50 UTC found
  occlusion 1 flag (P1) + boxtitle 4 DEFECT (P3/P4/P5/P6). Fix: delete exactly one
  word per defect (no meaning change, no font-size change); B1: P8 answer 141 note
  `vainqueur = чемпион` → `vainqueur = победитель`, unifying with P1 gloss
  `un vainqueur победитель` (pair option b = "le joueur qui a gagné le tournoi").
- Edits (source only; pre-fix SHAs print `1aa7c71d7f2e…` / web `85c45f1cff46…` /
  text `028cb8c2d4b0…`):
  1. P1 occlusion: `content12.py:28` headline `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI`
     → `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE` (drop MERCREDI; the day stays in the
     article + date box). Headline ink ends x=1124.0, clearance +178.5px vs the
     audit's gloss start 1302.5.
  2. P3 boxtitle: `expl.py` head_zoom `ZOOM　LES DATES EN CHIFFRES` → `ZOOM　DATES EN CHIFFRES`
     (ink over +7.6 → −44.4px).
  3. P4 boxtitle: `content34.py:158` f.box `LES PHRASES DU COMMENTATEUR`
     → `PHRASES DU COMMENTATEUR` (ink over +36.5 → −15.5px).
  4. P5 boxtitle: `expl.py` head_cine `LE CINÉМА DU MERCREDI　КИНО` → `CINÉМА DU MERCREDI　КИНО`
     (ink over +21.3 → −16.2px; the flagged title is head_cine, not head_mots_photo).
  5. P6 boxtitle: `expl.py` head_3dates `TROIS DATES POUR COMPRENDRE` → `DATES POUR COMPRENDRE`
     (ink over +24.5 → −57.5px).
  6. B1: `expl.py` m_p8b `vainqueur = чемпион　b` → `vainqueur = победитель　b`.
  All widths pre-verified with the edition's own svglib ink math (measure3.py);
  every pre-fix gate number reproduced exactly before editing. (`champion`
  survives only in g4 `действующий чемпион` = tenant du titre — different word.)
- text.md re-export (`export_lang.py ru`): diff vs pre-fix exactly 6 lines
  (L19 headline, L415 head_zoom, L505 P4 box, L655 head_cine, L785 head_3dates,
  L1083 Q141 note); 542 entries / 150 exercises unchanged.
- Rebuild + full gates (`run_gates.sh … fix-ru2`, logs under
  `scratch-d5-rebuild-fr/2026-w47-fr-ru/logs-fix-ru2/`): run.py TOTAL 150,
  0 FLOW OVERFLOW, 1 HEAD TOO WIDE (P7-outils, pre-existing, out of scope);
  render rc=0, webpdf rc=0. p8 extract 150/150, compare vs core-fr CLEAN
  keydiff `[150]` (known writing key), vs pre-fix baseline CLEAN keydiff `[]`;
  occlusion 0 flags; boxtitle 0 DEFECT (53 titles / 549 lines); spill 0 SPILL
  (33 boxes / 151 candidates / 151 OBSERVE); edge 8 pages 0 TOUCH / 0 NEAR;
  D5 census PASS (LAT/CYR in CJK 0, curly 0); text layers print==web
  byte-identical (96,699 chars, multiset diff 0); SVG-vs-PDF multiset diff 0
  (35,395 non-ws chars); p8 keys vs text.md 150/150 (Q25 'd', Q141 'b',
  Q150 'Открытый вопрос'); freeze diff vs core-fr rc=0 (added CJK 10, all U+3000;
  added Latin 208 — wholesale core-vs-edition diff, per tool doc not a FAIL
  criterion). Creambox FAIL 3 defects — SAME adjudicated false positives as r1/r2
  (P5 `debat5_note` duplicate matched to its second occurrence; strings +
  coordinates identical to KIT record); independent spill_sweep 0 SPILL.
- Finished goods: print + web PDFs 8 pages, 1462.5×2025 pts; VOL.4 ×11 + VOL. 4 ×1;
  web 1,773,854 B < 7 MB; text layer 51,025 B. New SHAs: print
  `af7d37bc0a56a786b038561da1a0f049a2d04b5397ba5cc15e8c3f728e9f0510`
  (17,222,281 B); web `f6e82ee074cf7392220f9b4fa52be7ef640070f3d8d2caea68b4994abe95ddc2`
  (1,773,854 B); text `ae0a0429047a1c0f249f38f53ad15f2329b81247f55fcf0bddeb252263e8a410`
  (50,475 B). No commit / no push (insertion is the coordinator's step).
- Coordination: fr-family worker (scratch-fix-fr-family1/) scaffolded 01:20 UTC
  but had not touched fr-ru when fix-ru2 finished (01:27 UTC build is current);
  per coordinator order, family work on fr-ru must build on this post-fix state,
  not overwrite it. Full fix log: scratch-fix-fr-ru2/ (PROGRESS.md, GATE-LOG-fix-ru2.md).

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-ru/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：Пятница 20 ноября　День ребёнка／Суббота 21 ноября　Полуфиналы в Турине + Неделя против отходов, 1-й день），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、1 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（53 titles）；creambox FAIL 3 defects——与 fix-ru2 裁定一致的误报（P5 `debat5_note` 复文按精确文本匹配到第二处；字符串与坐标与 fix-ru2 记录逐位一致），独立 spill 门禁 0 SPILL；spill 0（151 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 104,033 字节，96,948 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 17,222,512 B `ade6694fcd1a…`、网 1,774,107 B `9de461db64ed…`、文 50,693 B `69d348831b05…`。
- 残留警告（修前已存在，fix-ru2 已记录）：1 HEAD TOO WIDE [P7-outils] `BOÎTE À OUTILS　ИНСТРУМЕНТЫ`。
- 接受记录（HEADS-NOTE.md，2026-11-12 裁定，恢复协调员 #4 复核 2026-11-13）：A4 P7 `BOÎTE À OUTILS　ИНСТРУМЕНТЫ` 实测 +14.8u（200dpi 像素实测）；墨迹过规则线但 text_colliders 0、next_span 右侧无内容、距页边 70.9u；裁图确认空 gutter、无碰撞。已接受，未修复。该警告仍会出现在 build 日志与 head_check 中，属已接受项、不是未修项。
- 本次重建以 fix-ru2 修后态为基础（ru2 的 5 处门禁修复 + B1 均在新印 PDF 文字层中核实仍在位：头条去 MERCREDI、`DATES EN CHIFFRES`、`PHRASES DU COMMENTATEUR`、`CINÉMA DU MERCREDI　КИНО`、`DATES POUR COMPRENDRE`、Q141 `победитель`；旧串 `LES DATES EN CHIFFRES`/`LES PHRASES DU COMMENTATEUR`/`TROIS DATES POUR COMPRENDRE` 均为 0；freeze 与 fix-ru2 基线比对仅 p2-vie.svg 变）。未 commit、未 push。

## minor1（2026-11-13，全新一轮重校发现 1 试验 + 回退；工作日志 `hidden_files/w47/scratch-fix-fr-minor1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-ru/logs-minor1/`（溢出试验）与 `logs-minor1-revert/`（回退后））

- 发现 1——P1 kicker 法语行缺 MERCREDI（`content12.py:28`）：按任务书恢复 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI`（37 个非空字符，与其余 10 版一致），重出 text.md（diff 恰 1 行 L19）并重渲。**恢复后超宽，无法放入：**PIL 真墨实测（ru2 `measure3.py` 同款方法）头条墨宽 1293.0px、墨右缘 x=1411.0，俄语 gloss `band_r1`（`АЛЬКАРАС ПОБЕДИЛ　ГОЛОСУЕТ В СР.`）墨左缘 1302.5 → **重叠 108.5px**；occlusion 门禁实测 1 TEXTX flag（`p1-une.svg`，墨重叠 `АЛЬКАРАС` 108.2×19.8px，与 ru2 修前实测值逐位一致）；P1 卡面目视确认 MERCREDI 白字压在金色俄语 gloss 上。其余门禁均绿（boxtitle 0 DEFECT、p8 CLEAN keydiff=[150]、spill 0、edge 0、census PASS、文字层 multiset 0）。其余 10 版能放下的原因：其 gloss 墨左缘均 ≥1450（en 1556.4、core/zh-tw 1450.0、de 1571.6），净空 ≥+39px；唯 ru 的西里尔 gloss 最宽。
- **处理：未硬塞，已回退。**按任务书"超宽须报实测数据由协调员裁定，不许擅自再缩短或改写"，源已恢复为 fixfam1 态（头条仍缺 MERCREDI），并以 `minor1-revert` 全套重建：text.md diff vs 修前 0 行；印 PDF SHA 与 fixfam1 逐字节一致（`ade6694fcd1a…`，17,222,512 B）；text.md SHA 与 fixfam1 一致（`69d348831b05…`，50,693 B）；门禁全绿（occlusion 0、boxtitle 0、p8 CLEAN、spill 0、edge 0、census PASS、文字层 96,948 字符 multiset 0、freeze CJK 12 / Latin 209 与 fixfam1 一致；creambox 3 defects 为 fix-ru2 已裁定误报，坐标逐位一致）。网 PDF 因 webpdf 构建非确定性重出为 1,774,094 B `4acb91b39968…`（内容与 fixfam1 版逐字节一致：文字层与印 PDF 相同，96,948 字符；印 PDF 可逐字节复现，网 PDF 三次构建三次 SHA 不同，见 FIX-LOG）。
- **协调员裁定前备选（发现 1 当时未闭合）：**(a) 接受现状——ru kicker 缺 MERCREDI，但须在 KIT 书面记录缩短理由（本次重校的指控点之二）；(b) 缩短俄语 gloss `band_r1`（如 KIT 预检曾删 `СЕНАТ` 的先例）以腾出 ≥108.5px；(c) 缩小 kicker 字号；(d) 接受重叠。任一选项均须协调员定夺后另行实施；本轮未动其他版。溢出试验件：印/网/text.md SHA 见 `scratch-fix-fr-minor1/ru-overflow-shas.txt`，P1 顶部裁图见 `scratch-fix-fr-minor1/ru-p1-overflow-crop.png`。
- **协调员裁定（2026-11-13，独立重校确认后）：接受 kicker 缩短现状，发现 1 闭合，不恢复 MERCREDI。**裁定依据：37 字符全行与西里尔 gloss 重叠 108.5px（PIL 真墨实测：头条墨宽 1293.0px、墨右缘 x=1411.0，gloss `band_r1` 墨左缘 1302.5；occlusion 门实测 1 TEXTX flag，墨重叠 108.2×19.8px；P1 卡面目视确认 MERCREDI 白字压在金色 gloss 上）；其余 10 版净空 ≥39px，唯 ru 西里尔 gloss 最宽，故仅 ru 缩短。"周三"事实未丢，保留在版：俄语 gloss `АЛЬКАРАС ПОБЕДИЛ　ГОЛОСУЕТ В СР.`（СР. = среда）、主标题 `Alcaraz, roi de Paris : le Sénat tranche mercredi`（text.md L31）、P1 日程 `Le vote solennel du Sénat aura lieu mercredi 18 novembre`。缩短理由书面记录于本 KIT fix-ru2 §1（去 MERCREDI；the day stays in the article + date box；墨右缘 x=1124.0，净空 +178.5px）及本节 minor1 试验记录。独立重校核实：印 PDF SHA `ade6694fcd1a…` / text.md SHA `69d348831b05…` 与修前逐字节一致，text.md diff 0 行；P1 渲染目检 kicker 与 gloss 间净空干净，无重叠。
