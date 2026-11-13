# WEEKLY-KIT — 2026-W47 fr-nl (Dutch reader)

- Week: 2026-11-16 – 2026-11-22 (VOL.4)
- Core: `2026-w47-fr-zh-cn` (reader = Simplified Chinese); this edition = reader Dutch (nl).
- Expl: 318 keys — 138 reused from W46 nl, 180 new, 14 frozen (French-only heads).
  `gloss_prefix` "Uitleg — ", `note_wrap` "half".
- Build interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PIL 13.0.0, PyMuPDF).
  Freeze re-run with the same interpreter; never system python3.
- Naming (fr family): print `La-Lucerna-VOL4-fr-nl.pdf`, web `La-Lucerna-VOL4-fr-nl-web.pdf` (dash).

## Files

- Print PDF `La-Lucerna-VOL4-fr-nl.pdf` — 17,030,275 B, SHA-256 `bc360a39096c0120c43792c4f6180f666bb068b8e08022a23f9bac22ec24af8a`
- Web PDF `La-Lucerna-VOL4-fr-nl-web.pdf` — 1,621,651 B, SHA-256 `408379aee3776fbfea9e814e32371d7b459abb3c1f157ee2f2f3e1861eab21c3`
- `.text.md` — 46,452 B, SHA-256 `c5ce799c2e4e99350e3286054029e4e05e4595bd300f873bd10d3baf5f9ec44f`, 44,364 chars, 542 entries, 150 exercises (D5 r2 re-export; see D5 rebuild section. Note: `export47.py` writes the first two header lines in core-fr Simplified Chinese — restore the Dutch header after re-export.)
- Text layer: print/web pdftotext byte-equal (99,461 B)
- Freeze (direct, two builds, SHA-256 first 8, D5 r2): [`221e81b8`, `8584b196`, `97e66d66`, `7e787816`, `8cb8b633`, `7737c6a9`, `b57c92e0`, `d17281f2`] — 8/8
- Chips: 134 [10, 12, 18, 15, 14, 15, 12, 38]; P8 min font 11.62pt (D5 r2 re-measured, 250 spans); p8 extract 150/150, notes 121/150; p8 compare CLEAN, keydiff `[150]` (writing key only); MCQ 45 bodies, 1480 lines, 0 defects.
- Source freeze (D5, coordinator approval 2026-11-12): `content8.py`, `bslib4.py`, `run.py`, `content12.py`, `content7.py` byte-identical to core-fr; `svglib.py` differs by exactly the `_D5_READER` line (`"latin"` vs `"cjk"`); `content34.py` 1 Dutch-reader fix (`head_mots_tennis` 23→21), `content56.py` 1 (`head_lire` 25→23); `render.py` differs only in BASE + PDF name.
- U+2019 = 0, U+00B7 = 0, gold = 0, old paper = 0, #fbfaf6 ×8.
## Gates (r2run1, 2026-11-11 — rebuild #2 from core-fr fix4): 15/15 PASS

run exit 0 zero overflow; occlusion 0 flags; p8_extract; p8_compare CLEAN keydiff `[150]`;
source_freeze; string_freeze (1 string excused as translated E value);
freeze_direct 8/8; text_layer; p8_font; scans; chips; keycheck; mcq; widths; band_spans
(FR title ends 1236.9, band_r1 starts 1329.4; FR sub ends 837.2, band_r2 starts 1457.5).
P7 disclosure box (y=1878, bottom 2258.0): 末基线 2233.3，清除 +24.7; creambox BELOW-WINDOW 7 (all +24.0/+37.0 next-heading false positives).
Orphan punctuation: 0 new (core-inherited 0, font-split shared-baseline 0, recorded remnant 0).
Q148 key `devant le`, stem `On se retrouve ___ cinéma ?`; blank lines Q130 (P8) + P3 Q36/Q37 present, same relative positions as core (see FANOUT-REPORT-fr2.md).
## Fix log

- **Rebuild #2 (2026-11-11, r2run1)** — rebuilt from core-fr fix4 (Q148 key `devant`→`devant le`, stem drops `du`; P4 `chiffres_note` drops 「决赛」). #1 edition backed up to `scratch-refanout-fr2/backup-old/`.
- P7 读者园地奶油盒溢出修：`courrier_disclosure` 删中句 “dit nummer drukt een gemarkeerd redactievoorbeeld.”（该信息已由 P7 法文示例标注句覆盖），3 行→2 行；末基线 2260.6→2233.3、creambox 清除 -2.6→+24.7（desc-clear +18.8）；PIL 真墨实测：披露灰字末行墨至 svg y=2237.8，盒底 2258.0 之下 2258–2270 白纸间隙零墨（仅 P7 哈希变）。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- Changed pages vs #1: P7（037b5c49→4eb69452）、P8（6a9750ef→467885cd）; all other pages byte-identical.
- Core fix4 SHAs: print 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`; web 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`; text 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`.

- Pre-build: keys-flow diagnostic diff 282px (need ≤124). Batch 1: 25 reused→fresh moves,
  54 note shortenings → diff 121px. Precheck PASS (g4 shortened, band_r1
  `ALCARAZ WINT　SENAAT STEMT WO.`).
- Head-width pre-sweep (es/it/pt failure class): `head_mots_photo` 460.2 > 400.5
  (`MOTS DU CINÉMA　BIOSCOOPWOORDEN`) → `MOTS DU CINÉMA　DE FILM` (309.8);
  `head_dieppe_ex` → `BEAUJOLAIS　DE QUIZ` (256.0);
  `head_mots_fetes` → `LES MOTS DU VIN　DE WIJN` (312.4);
  `agenda_sub` → `De week dag voor dag　16–22 nov.` (fresh count 179 after batch 1).
- run1 gates 12/15, three real defects:
  1. `FLOW OVERFLOW [P7-phrases] col 3 y=1806 need 111 bottom 1830` — all 8 Dutch gpN
     wrapped to 2 lines at 19.5px sans (core 1 line each, +28px each). The hand per-phrase
     height model was ~119px off for this flow (para/split baseline offsets + ex
     overhead) — do not trust it for P7-phrases; cut generously and read the real log.
     Occlusion's 3 P7 flags were consequences of this one overflow.
  2. `head_chart` 866.0 > 829.0.
  3. `agenda_note` 400.1 > 378.5.
- run2 fixes (batch 2, gp8 moved reused→fresh; fresh count 180): all 8 gpN shortened to
  1 line (`gp1` …(battu)., `gp2` …(être)., `gp3` voter: stemmen., `gp4` en beauté: mooi
  eindigen., `gp5` celui que: degene die., `gp6` sortir: in première gaan.,
  `gp7` …(rejetée)., `gp8` trois temps: drie tijden.); `head_chart` →
  `LE CALENDRIER　BEGROTINGSKALENDER (STEMMING WO.)` (695.8 ≤ 829.0);
  `agenda_note` → `Plechtige stemming: wo. 18 november` (336.9 ≤ 378.5).
  Rebuilt run2: zero overflow, gates 15/15 PASS.
- Independent reproof gloss fix (2026-11-12): P7 `head_clinic` adds `CLINIQUE DES ERREURS　FOUTEN`; `head_cine` adds `LE CINÉMA DU MERCREDI　FILMS`; `head_outils` adds `BOÎTE À OUTILS　GEREEDSCHAPSKIST` (glosses from this edition's own `bridge_*` wording). fix1 FAILED gates: occlusion 1 EDGE + edge 1 TOUCH — `GEREEDSCHAPSKIST` ink to x=2014.1 past the 1950-wide page (574.6px @27 vs CW 422.5). fix2: gloss shortened to `GEREEDSCHAP` + `content7.py:58` 27→23pt (415.0 ≤ 422.5). fix2 gates all green: occlusion 0, boxtitle 0 DEFECT, spill 0/101, edge 0/0, census PASS, p8 CLEAN keydiff `[150]`; residual warning: clinic FOUTEN 432.6px (~10px past the column into blank margin, same class as en D5 shipped clinic ERRORS 428.6, accepted). Source `expl.py`; text.md re-export diff vs pre-fix exactly 3 lines (L655, L855, L921). SHAs: print 17,030,024 B `45c0b11e87a7…`, web 1,621,399 B `fb98be3aa292…`, text 46,281 B `ad506a852519…`. Full log: scratch-fix-fr/FIX-LOG.md.
- Second-round reproof fix, r2 (2026-11-12, PROOF-NOTE-2 R2-1 + R2-2): P7 grammar head `gp4` `en beauté` → `se terminer en beauté` (verb restored; cf. de/en/es/it/pt/zh-tw + core), P8 answer 100 note `n_gp4` aligned the same way (`100. beauté (se terminer en beauté = mooi eindigen)`), and P4 NOTE `g4` `un vainqueur winnaar` → `un vainqueur een winnaar` (article restored; cf. same edition P1 NOTE `un vainqueur een winnaar`). Source `expl.py:175,292` (R2-1), `expl.py:41` (R2-2); text.md re-export diff vs pre-fix exactly 3 lines (L465, L893, L1079; dry-run to /tmp first, no dropped titles). Gates: run 0 FLOW OVERFLOW; occlusion 0, p8 CLEAN keydiff `[150]` (vs pre-fix baseline `[]`), boxtitle 0 DEFECT (38 titles), spill 0/101, edge 0/0, census PASS, print/web text layers byte-identical (98,218 chars, 99,461 B); P7 visual crop verified, gp4 wraps to 2 lines, complete, no overflow. Residual warning (unchanged from fix2, accepted): 1 HEAD TOO WIDE `[P7-clinic] CLINIQUE DES ERREURS　FOUTEN` (432.6px, into blank margin). SHAs: print 17,030,093 B `c7e99156a889…`, web 1,621,462 B `d846793366f5…`, text 46,309 B `a5f5c7ebbfc8…`. Full log: scratch-fix2-w47-fr/FIX-LOG-2.md.

## Notes (checked, left as is)

- Bare-French heads (`head_cine` LE CINÉMA DU MERCREDI, `head_outils` BOÎTE À OUTILS,
  `head_3dates`, `head_chiffres`, `head_clinic`, `head_comp6`, `head_foot`, `head_opinion`,
  `head_sortir`, `head_zoom`, `head_budget3`) are reused W46 nl values — the nl edition's
  own pattern (en/de translated some, nl did not). Not defects.
- P3 ZOOM box Dutch gloss `Vroege verkoop sinds 1951, derde donderdag sinds 1985, 75e
  jubileum in 2026.` is a different E key from P8 note Q26 `Vroege verkoop in 1951` —
  different wording is correct, not unified (same as pt).
- P3 `POUR OU CONTRE?` box has no Dutch line; P5 `debat5_note` appears twice —
  both match core.
- P8 keys note Q102 `(sortir = uitkomen)` is the generic gloss; P7 grammar line gp6
  `sortir: in première gaan.` is the cinema-specific gloss — both correct in place.
- Person names verified against French article text: Dhont (4× in .text.md, "Dont" 0×),
  Ménochet, Fils, Haymitch, Francis Lawrence, Mipo O, Alexandre Smia, Mounia Meddour,
  Kristin Scott Thomas, Guillermo Guiz, Méliès, Doré, Hiroshige, Atget, Moreau.
- Q150 note: "Open vraag — punten in het kader; model in het kader op pagina 8
  (Beoordeling per punt)".

## Visual QA (run2, 8 pages at 100 dpi + 300 dpi P1 band crop)

Zero problems. P1 band clean at 300 dpi (FR title / Dutch band clearly separated);
P2 Châtillon photo; P3 Moreau painting + `BEAUJOLAIS　DE QUIZ`; P5 Méliès image;
P6 calendar head on one line; P7 Doré image, 8 phrases fit, LE COURRIER box clear of
`et ___.`; P8 Hiroshige image + caption, MODÈLE box visible.

## Visual QA — rebuild #2 (r2run1, 8 pages at 100 dpi; changed pages + P7 box-bottom 200 dpi crop)

Zero problems. Changed pages vs #1: P7（037b5c49→4eb69452）、P8（6a9750ef→467885cd）.

## D5 rebuild (2026-11-12)

- Install: `apply_variant.py --target fr --reader nl` (mode=latin), routing assert 20/20 PASS (incl. fix2 quotes → news); `svglib.py` differs from core-fr by exactly the `_D5_READER` line (coordinator landing approval 2026-11-12).
- r1 gates: 4 HEAD TOO WIDE (P6-ex `LIRE LE CALENDRIER　AGENDA`, P6-opinion + P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`, P6-micro `LE COMPARATIF EN POLITIQUE`), occlusion 1 TEXTX (P1 headline vs `ALCARAZ WINT` 131.0×20.8px), boxtitle/creambox 4 DEFECT (P3 `LES DATES EN CHIFFRES` +7.6, P4 `LES PHRASES DU COMMENTATEUR` +36.5, P4 `WOORDEN` +27.3, P6 `TROIS DATES POUR COMPRENDRE` +24.5); rest green (text layers byte-identical; p8 121/150 CLEAN, keydiff=[150] as pre-D5; freeze 8/8; spill 0; edge 0; census PASS). Note: `head_chart` `LE CALENDRIER　BEGROTINGSKALENDER (STEMMING WO.)` was NOT flagged (fits its box, unlike de/pt/it) — left unchanged.
- Fixes, 11 (r1→r2): the same 8 core fixes synced verbatim (after sync, `content34.py`/`content56.py`/`content7.py` are byte-identical to core-fr except the nl lines below); Dutch-reader-specific 3 (`text_w` measured): `band_r1` drops `ALCARAZ WINT　` (gap −131.0→+127.5px), `head_lire` 25→23 (434.7→399.9 < CW 422.5), `head_mots_tennis` 23→21 (427.8→390.6; 22pt ink ≈381 still marginal).
- r2 full gates (10:18–10:26 UTC) **ALL GREEN**: run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS); render + webpdf rebuilt; occlusion 0 flags; p8 121/150, CLEAN (vs core keydiff=[150], vs pre-fix baseline keydiff=[]); freeze baseline 8/8, diff vs core +0 non-separator CJK (added CJK all U+3000: vs core 9, vs pre-fix baseline 2 — reflow separator-count change); boxtitle 0 DEFECT (38 titles, 285 body lines); creambox PASS 0 defects (n=520, median 1.016, bold 1.056, regular 0.997; P8 198→197 lines, slack 36.6→36.6px); spill 0; edge 0; D5 census PASS (0/0/0); `census_quotes.py` curly-quote defects 0; print/web text layers byte-identical (99,546 B each). Print PDF 17,029,995 B SHA-256 `c0c12aea…`, web PDF 1,621,369 B SHA-256 `36493cef…` (first 8; see Files). PDF 8 pages, 6 embedded images (Hiroshige present; P8-keys ended 2106/2560). P8 min font 11.62pt (250 spans). Flow ends: P6-deep 1288/1300, P6-ex 2527/2560, P7-phrases 1718/1830, P8-keys 2106/2560. Gate logs: `hidden_files/w47/scratch-d5-rebuild-fr/2026-w47-fr-nl/logs-r2/`; work log: `hidden_files/w47/scratch-d5-fr/RUN-LOG.md`.
- Three-point acceptance check (coordinator correction notice): production print/web/text SHA = r2 log `shas.txt` = KIT Files above; production `svglib.py` contains `_D5_READER`. PASS.
- Cleanup: `freeze-r1/r2/build-copy` deleted after the rounds; `freeze-r*.json`, baselines and logs kept.

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-nl/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：Vrijdag 20 november　Kinderdag／Zaterdag 21 november　Halve finales in Turijn + Anti-verspillingsweek begint），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、1 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（38 titles）；creambox PASS 0 defects；spill 0（101 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 99,680 字节，98,436 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 17,030,275 B `bc360a39096c…`、网 1,621,651 B `408379aee377…`、文 46,452 B `c5ce799c2e4e…`。
- 残留警告（修前已接受，见 scratch-fix-fr/FIX-LOG.md §8 与 scratch-fix2-w47-fr/FIX-LOG-2.md）：1 HEAD TOO WIDE [P7-clinic] `CLINIQUE DES ERREURS　FOUTEN`（432.6px，栏外伸入空白边距，无碰撞）。
