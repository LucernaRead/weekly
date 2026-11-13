# WEEKLY-KIT — La Lucerna Spanish Weekly VOL.4 — es-zh-tw

Edition: 2026-W47, target language Spanish, reader language Traditional
Chinese (zh-tw, Taiwan usage — an independent edition, never converted
from zh-cn).
Issue dates 16–22 November 2026. 8 pages, 150 exercises (A2 50 / B1 72 /
B2 28).
Self-check: zero known defects. Awaiting independent proofreading.

## §1. Spec (measured, build 1)

- Print PDF: `La-Lucerna-VOL4-es-zh-tw.pdf` — 4,381,574 B,
  SHA-256 `9a60b0786b1cf2f12ff9d2df94a7b28b3d2176ecf9385deb51d4814078555902`
- Web PDF: `La-Lucerna-VOL4-es-zh-tw-web.pdf` — 1,265,855 B,
  SHA-256 `4851fee5b3a41a17ea7bfc6aab26188b6297b1826eaeb7ba61eb8e6125df594a`
  (built only with `tools/webpdf.py`, called from `render.py`;
  pdftotext print = web, 44,594 B, token multiset identical; both < 7 MB)
- 8 SVG in `svg/`, 8 PNG in `cards/`
- `2026-w47-es-zh-tw.text.md` (1,786 lines, exported from the production
  source with the fixed `extract_text_es_zh-tw.py`; never extracted back
  from the PDF)
- `ABSTRACT.txt` (Traditional Chinese, one line, no ASCII double quotes)
- Paper #fbfaf6 on all 8 pages; masthead 196 units = 147pt; VOL.4 ×9 in
  SVG text; VOL.5 ×3 (all legitimate forward references to next week's
  issue); badge tricolour A2 #5c6e30 / B1 #46581f / B2 #37402f
- P8 badges: 35 chip rects — A2 11 / B1 21 / B2 3 — plus 1 #37402f header
  band rect (identical to core); Q113–150 all badged, none missing
  (Q113–120, Q145–149 chips present, visually confirmed)
- P8 minimum font 10.125pt (pypdf `Tm` parse of the page-8 content stream,
  min |a| 10.125 over 150 Tm ops — identical to core-es; §6.10)
- No "12 de noviembre" anywhere; no international politics
- The moth `<title>Lucerna 三色蛾</title>` (P1, inherited from core,
  invisible metadata) is left unchanged
- Traditional Chinese throughout, Taiwan usage: 電台 (not 電臺),
  公布 / 宣布 with 布 (not 佈) — adjudicated correct, §6.1; 身分 (not
  身份); 本週計劃 (not 本周计划). The one genuine simplified leak found
  by the audit was fixed before the build (§6.1).

## §2. Per-page contents (frozen Spanish text; Traditional Chinese explanation layer)

- P1 Portada: lead "La campaña arranca: trece días para el 29-N";
  five-claves box; numbers box; "LA PALABRA DE LA SEMANA « el debate »"
  with 1-line gloss "「辯論」：人們公開討論。"; quiz 7–10
- P2 Vida (A2): "La semana, día a día"; EL CALENDARIO "本週日曆";
  DECIR LA HORA; LOS DÍAS DE LA SEMANA; exercises 11–28
- P3 Cultura (A2→B1): flamenco + Santa Cecilia; Sargent "Bailaora
  española"; exercises 29–46
- P4 Deporte (B1): La Liga jornada 13; fixture table; exercises 47–64
- P5 Juventud (B1): first-time voting; postal vote; Black Friday;
  exercises 65–82
- P6 A fondo (B2): "Leer la campaña: debates, programas y encuestas"
  — band subtitle completed to "讀懂競選：辯論、政綱與民調";
  RTVE minutes chart; poll-ban chart; exercises 83–100
- P7 Lengua (A2/B1/B2): LA HORA / COMPARATIVOS / EL SUBJUNTIVO;
  ERRORES TÍPICOS; LA PALABRA; CARTAS DE LOS LECTORES (sample letter,
  no real letters had arrived — editor's note, §6.5); FRASES DE LA
  SEMANA; LA PRÓXIMA SEMANA (VOL.5); exercises 101–112
- P8 Ejercicios y respuestas: exercises 113–150; RESPUESTAS with a
  Traditional Chinese note per item; ✓ = model-text item (#150)

## §3. Measured totals

- run.py rc=0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (build 1)
- Flow ends (run1 log): P1-headline col 2/2 y=1371, P1-quiz y=2491;
  P2-feature col 1/2 y=1537, P2-ex y=2356; P3-main y=625, P3-ex y=2436;
  P4-main y=827, P4-ex y=2309; P5-main y=964, P5-ex y=2259;
  P6-main y=523, P6-ex y=2533; P7 a2 1062 / b1 1092 / b2 1092;
  P8-ex y=842 (bottom 1252); P8-keys y=2506 (54px spare)
- Your-turn box bottoms (SVG rects): P2 964.0; P3 1571.75 (36px above
  the 1608 divider); P4 935.5; P5 1580.55 (27px above the divider);
  P7 col3 letter box 1844.51 (exactly the core value)
- Occlusion audit 0 flags; bridge-orphan sweep 0 over 20 bridges;
  box-vs-hline sweep 0; bridge-widow sweep 0
- p8 extract 150/150; compare CLEAN, keydiff=[137, 138] (§6.12)
- Freeze: tool 8 OK + direct sha256 of `build-copy/svg` vs shipped
  `svg/` 8/8
- Gloss-word token counts (core §8.1 method, bare-word, per page):
  P1 campaña electoral 6 / debate 11 / cara a cara 3 / voto por
  correo 6 / jornada de reflexión 2; P2 debate 5 / mitin 2 / cartel 2 /
  escaño 2; P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5;
  P4 jornada 19 / derbi 7 / liderato 3 / parón 2 / fase liga 2;
  P5 sobre 5 / papeleta 2 / censo 3 / plazo 3 / urna 5 — every Note
  word occurs ≥2 times on its page
- P8 multi-line items (diagnostic): 1 — #139 only (core-consistent,
  §6.9); #137/#138 are 1 line each in Traditional Chinese

## §4. Sources reused from core-es (frozen)

All Spanish text, facts, dates, numbers, answer keys, images
(Sargent bailaora, Jebulon ballot box, Book of Hours initial, swan pen),
and the P8 key set are byte-identical to core-es except the explanation
layer and the two re-aimed translation keys (§6.12). No new trend
research; no fact changes; the 12 November decree date was NOT
reintroduced (no second independent source, W45/W46 rule).

## §5. Build commands (all from the repo clone, tools venv)

- Apply: `tools/venv/bin/python scratch-fanout-es/apply_fanout.py zh-tw`
  (487 literal replacements; 0 manual-over-harvest overrides; §6.1)
- Pre-fixes: 6 substitutions with count assertions (§6.2–§6.8), plus
  the one simplified-character fix (§6.1)
- Build: `tools/venv/bin/python run.py` (build 1 only)
- Render: `tools/venv/bin/python render.py` (~175 s; calls
  `tools/webpdf.py` internally for the web PDF)
- Gates: `tools/occlusion_audit.py svg`; `sweep_de.py .` (orphans +
  box-vs-hline + widows); `tools/p8.py extract --p8 svg/p8-ejercicios.svg
  --total 150`; `tools/p8.py compare --edition-p8 svg/p8-ejercicios.svg
  --core-p8 core-es/svg/p8-ejercicios.svg --total 150`;
  `tools/freeze.py baseline --build . --core-svg svg --out
  scratch/freeze-es-zh-tw-1`; pdftotext print vs web; pypdf Tm parse
- Text export: `tools/venv/bin/python scratch-fanout-es/extract_text_es_zh-tw.py
  svg 2026-w47-es-zh-tw.text.md` (fixed extractor copy, §6.11)

## §6. Adjudications

### §6.1 Apply + Traditional-Chinese audit (the one real defect)

487 literal replacements; 0 manual-over-harvest overrides.
The harvest map has 232 keys; 142 items are missing from it, but the
leftover check shows every missing key is identical in Simplified and
Traditional (完成句子, 填空, 造句, 球迷很多, 吉他, 榜首, 德比,
歌唱, 舞蹈, 原形, 期限, 第8版, 投票箱在哪, 第一次投票, VIDA　生活,
CULTURA　文化, JUVENTUD　青年 — verified with opencc s2t, all
IDENTICAL) — except one: the map returned
"EL PLAN DE LA SEMANA　本周计划" unchanged, i.e. simplified 周/计/划.
A full opencc phrase-level audit of every double-quoted string in the
six .py files found 6 strings that differ after s2t; 5 are opencc false
positives — 布 in 公布/宣布 and 台 in 電台 are correct Taiwan
Traditional (公布欄, 宣布, 電視台/廣播電台 all use 布/台; 佈 is for
佈置, 臺 for 臺灣/樓臺) — and 1 is genuine: 本周计划 → 本週計劃
(content56.py:22, the P5 box title), fixed by hand before the build.
No single-quoted CJK strings exist. CJK in .py is expected for zh-tw
(Traditional characters); the apply script's CJK allow-list covers it.
The .text.md was re-audited the same way after export: only the same
5 adjudicated 布/台 occurrences differ after s2t; zero genuine
simplified characters remain.

### §6.2 P1 gloss

Harvest "「辯論」：兩人以上公開討論，有輪次、有提問。" wraps
2 lines at sans 19 (418.0 units at gw; line 2 is just 提問。).
Shortened to "「辯論」：人們公開討論。" (228.0, 1 line) — parallel to
ja "「討論」：人々が公開で話し合う。" and ko
"“토론”: 사람들이 공개적으로 토론해요。" The detail lives in the
Spanish definition above it and in the P7 word box.

### §6.3 P6 band

Harvest gloss was the title only ("讀懂競選"). Completed to the full
subtitle "讀懂競選：辯論、政綱與民調" (full sub sans 18 = 759.7
units against the 1684 limit) — the other five bands all carry the
full subtitle.

### §6.4 P7 — nothing to shorten (Chinese is compact)

Word-box gloss harvested at 2 lines @20 ("debate = 辯論：公開討論，
有輪次。本期是辯論週；大選 29 日。", 576.0 units) — retained.
Editor's note harvested at 3 lines at both 20 and 19
("編輯部說明：截稿時未收到真實來信與最佳作文，本期登載編輯部示例信，
承諾順延至 VOL.5。歡迎來信！") — retained at 20, so P7 col3 lands
exactly on the core value 1844.51. All 4 ERRORES notes are 1 line
at 19.5/CW-44 (ERR1 "一點是單數，動詞用 es。" included).

### §6.5 P8 header

Moved preventively to 1337 / keys flow to 1363 (as in every edition;
the right note is 334.1 units @19.5, the title 493.5 @25 — no
collision either way, but the move is the standing rule).

### §6.6 Your-turn boxes — all retained at 20

Chinese your-turns are short: P2 3 lines @20 and @19, P3 2 lines,
P4 3 lines, P5 3 lines. No size change was needed anywhere (unlike
the Latin editions, which needed @19). Box bottoms: P2 964.0,
P3 1571.75, P4 935.5, P5 1580.55 — all clear of the 1608 divider.
The P3 wrap splits 「魂」 across two lines and the P5 wrap starts
line 3 with "？" — the renderer's character-level CJK breaking,
identical in kind to the core's own Chinese wrapping (cf. ja #44
"動詞は2 / 番目"); not a defect class, left as rendered.

### §6.7 Bridges — none to shorten

Every bridge is 1 line at 20.5 (P2 C "讀第 2 版文章，選出正確答案。",
P5 A, P5 B "用方框裡的詞填空。注意：有的詞要變位。", P5 C
"用 ir a + 原形動詞改寫句子，表示「將要」。", P6 A) except P6 D
(2 lines, content on both). Widow sweep 0, orphan sweep 0 — the
ja-style lone-"。" widow does not occur in zh-tw.

### §6.8 Letter parens

Full-width （ejemplo, escrito por la redacción） → half-width
(ejemplo, escrito por la redacción) (W46 precedent).

### §6.9 P8 keys

Diagnostic (REG run in a /tmp copy of the edition, so the shipped
SVGs were never touched): exactly 1 multi-line item, #139 — the
core-consistent wrap, retained per the standing ruling. #44 is also
2 lines in the render ("時間在前，動詞第 / 二"), core-consistent.
#137/#138 are the translation redirections with reader-language keys
("週一是國際佛朗明哥日。 — 對照原文" /
"週六我們看塞維亞德比。 — 對照原文"), keydiff=[137, 138] adjudicated
as in W45/W46. #150 uses the ✓ form: "✓ 範文見本版 H 區（97 詞）"
(97 words, matches the MODELO count).

### §6.10 P8 font size — Tm regex must allow the minus sign

The page-8 content stream writes Tm as `13.5 0 0 -13.5 x y Tm`
(negative d). A regex without `-?` finds 0 ops. With
`(-?[\d.]+)\s+0\s+0\s+(-?[\d.]+)\s+...Tm`: 150 ops, min |a| =
10.125pt, smallest values [10.125, 10.5, 11.625, 12.0] — identical
to core-es (150 ops, same values). The |a| values are already in
points; do NOT multiply by 0.75. The /x12 form XObject on P8 is the
embedded swan-pen image (binary noise, no text) — ignore it.

### §6.11 Text export

`extract_text_es_zh-tw.py` is a sed copy of the fixed ko extractor
(CJK-aware per-character widths + cross-column splitting, plus the
hangul ranges — harmless for zh-tw). No "282."-style fake key was
observed; the P8 keys extract 150/150 and the .text.md keys are
1–150 with none missing. The full 1,786-line .text.md was read
end to end; the only oddity is the column-interleaved reading order
of the export itself (same as every edition), not a content defect.

## §7. 重建（re-fanout，2026-11-11 — core build 10）

Core baseline: core-es fix build 10 (independent re-proof (a), zero findings) — print 17,212,955 B SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`, web 1,410,471 B SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`, text.md 1,822 lines SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
Method: old edition backed up to `scratch-refanout-es/backup-old/` (verified identical), deleted, re-applied via `scratch-fanout-es/apply_fanout.py`; `classify.py` diffed fresh sources against the backup line by line — KEEP = core build-10 change, REVERT = edition hand fix restored, MERGE = derbi letter line (fresh sábado + backup ASCII parens), INSERT = RTVE debate-a-ocho timeline row. No commit, no push.
Common core changes kept: C1 (P1 CINCO CLAVES box 700→720), C2 (`antes del jueves`→`hasta el jueves`), es-ja D1 (consejo completed) + D4 (derbi sábado 21st), es-nl D1/D2, es-pt C2 (PCTE kept, 195 kept). C3 (P5 vocab `content56.py:79`) left as-is per adjudication.
Gates (all green unless noted): run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; render rc=0; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated — translation items keyed by target-language sentence); freeze 8/8 SVGs byte-identical; freeze-diff CJK accounting clean; canonical creambox.py full scan 0 own-ink overflow (the 6 raw negative lines per edition are the known below-box headings, identical to core); creambox_diag 0 own-ink negatives; boxtitle 0 overflow; keycheck 149/150 (only the #150 open-question `✓` exception); sweep 0 orphans / 0 box-vs-hline; pdftotext print = web bytes; P8 min effective font 10.125pt (≥ 9.75pt floor).
Classify: KEEP 23 / REVERT 6 / MERGE 1 / INSERT 1 / DELETE 0. Build: run1 rc=0, TOTAL 150, P8-keys y=2506. New print 17,263,265 B SHA `ef5f1cde27036e5c810c4f779fd43e743857ab763c77df9b09bf6d885d804365`; web 1,725,936 B SHA `5b7d87967332783dd0314d54ab2b8483e7d0036b4bdc8609ae3226f2c5de6500`; text.md 1,803 lines SHA `930fc2bab9b7f99ad45c1a2d50349a750bb76b52f89bad2dc0f203b62310f36f`; print/web text 106,384 bytes, identical.
Hand fixes: none task-listed for es-zh-tw (all core items resolved by the rebuild; D2 = C3, untouched). `EL PLAN DE LA SEMANA　本週計劃` verified present in text.md (restored via revert). ABSTRACT.txt wording fixed for core build-10 facts: `11月19日前申請郵寄投票` → `最遲11月19日申請郵寄投票`. Freeze-diff CJK accounting: added characters are Traditional Chinese explanations only; no simplified 请 (traditional 請 U+8ACB verified).

## D5 重建記錄（2026-11-12，B檔）

- 安裝：`mechanism/apply_variant.py --svglib <本版>/svglib.py --target es --reader zh-tw`（mode=cjk，按字符文字分流，不加 `_READER_LANG` 門）；`svglib.py` md5 `6a46ee51…` → `04b42710…`（安裝器同時補 port 了 fix2）；路由斷言 10/10（`route_assert.py`，mode cjk）；機制 `test_d5_routing.py` FAILURES: 0；修前基線：印 17,263,265 B `ef5f1cde…`、網 1,725,941 B `9208bd35…`；D5 普查 347 violations（與裁定 §1.1 預期 347 一致）；boxtitle 0 DEFECT；occlusion 0。
- 預修 3 項共用版式（與 core-es 相同西班牙語串、同欄寬）：P1 欄頭 `UNA SEMANA, TRES ESCENARIOS` 25→23pt、P3 欄頭 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt、P3 手工題 `EL FLAMENCO, EN TRES DATOS` 24→23pt。
- 逐項修 2 項（均為 D5 新缺陷，修前基線 0；CJK 類：拉丁頭在 Newsreader SemiBold 下加寬，把繁體尾頂出框；與 core-es P1/P5 副標同源，數值亦相同）：P1 框題 `LA SEMANA EN CIFRAS　數字看本週` +22.5px——該框 `tsize=21`（餘量 14.7px）；P5 框題 `EL PLAN DE LA SEMANA　本週計劃` +13.7px——該框 `tsize=21`（22pt 餘量僅 4.5px，取 21 求穩）。以上文字均未動（`text.md` 內 `本週計劃` 保持原樣）。注：ink=advance（尾字為全角 CJK），框題可用寬 404.5px。
- 門禁全綠：run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0（`head_check.py` PASS 0 defects）；render rc=0；D5 普查 0；U+201C 普查（`census_quotes.py`）0；occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，僅讀者語譯註差異）；boxtitle 0 DEFECT；creambox（倉內 `tools/d5_creambox_audit.py`）PASS 0 defects（P8 241 行、頁腳餘量 38.9px 不變；P1 行數 120→118、P5 121→123 為框題字號改變致框高變化）；spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 955 個——為繁體讀者層相對 core-es 簡體讀者層的正當差異（數字/數字等繁簡字形）；同版 freeze diff（修前基線 vs 新版）新增 CJK 字符僅 1 個 U+3000（run 拆分 artifact）；印/網文字層 37,931 字符、7,268 詞一致。
- 新 PDF：印刷版 4,381,574 B SHA `9a60b0786b1cf2f12ff9d2df94a7b28b3d2176ecf9385deb51d4814078555902`；網頁版 1,265,855 B SHA `4851fee5b3a41a17ea7bfc6aab26188b6297b1826eaeb7ba61eb8e6125df594a`。`text.md` 字節不變（SHA `930fc2ba…`）。日誌：`hidden_files/w47/scratch-d5-rebuild-es/2026-w47-es-zh-tw/`。

## es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）

- 改动：F2（P6 时间轴措辞：`(sin el PSOE)` → `(sin el PSOE confirmado)`，与正文一致）。F1（缺首字下沉）按协调员裁定不修：全刊引擎级缺口，进模板 backlog，见 FIX-LOG。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 更新（core-es 为 D5 工具重导出；其余 10 版手术替换，diff 只含意改行；ru F4 另做词级手术，见 FIX-LOG 陷阱核查节）。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,575 B，SHA-256 `fd3e65ef18402cf3889bfbf16321c451187a94dbc5cc208d90f8db955502bff0`；网页版 `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,861 B（< 7 MB），SHA-256 `8871073245fdb336f634013e365369388196b064a998d7e307b4423a2f9e574e`；text.md `2026-w47-es-zh-tw.text.md` 43,818 B，SHA-256 `d26fdddc0fa69535e3eaf4384272834470f405c30a7c202c37d917e2817a1290`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 26 titles, 328 body lines，0 DEFECT；spill 0 SPILL（27 盒，82 candidates）；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8；印/网 pdftotext 44,605 字节逐字节一致。
- 日志：`hidden_files/w47/scratch-fix-es/`（FIX-LOG.md、build-all.log、build-resume.log、gates-all.log、text-pre/）。

## 第四轮独立重校修复 I1（2026-11-12，PROOF-NOTE-4 §2 返修）

- 改动：I1（text.md 专属，低）：两栏/两块拼接处丢空格致文字粘连；本版共 7 处（与 PROOF-NOTE-4 表列一致）：分版粘连 0 处（无）；目录粘连 7 处（`Pág. 2La semana` … `Pág. 8Ejercicios y respuestas` → 各补空格）。
- 重建：未重建（PDF 未动）；text.md 手术替换 7 处（逐处先断言原文存在再替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 7 行，行数不变（1804 行）。
- 文件：text.md `2026-w47-es-zh-tw.text.md` 43,818 B（I1 前 43,811 B，+7 B）、1804 行，SHA-256 `d26fdddc0fa69535e3eaf4384272834470f405c30a7c202c37d917e2817a1290`（改前 `4795332ea53a4a14bad8c5b558bc6b6ad172f6b1ee42e69423e6f2391ebb25e8`）；印/网 PDF 未动，SHA 不变（印 `fd3e65ef1840`、网 `8871073245fd`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；D5 普查 PASS（弯引号 0/0 在 Newsreader）。
- 日志：`hidden_files/w47/scratch-fix4-w47-es/`（FIX-LOG-4.md、fix.py、fix2.py、fix-report.json、text-pre-*.md、gates4.sh、gates4.log、p8-extract/compare、census）。
