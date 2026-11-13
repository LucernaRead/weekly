# WEEKLY-KIT — La Lucerna Spanish Weekly VOL.4 — es-ja

Edition: 2026-W47, target language Spanish, reader language Japanese.
Issue dates 16–22 November 2026. 8 pages, 150 exercises (A2 50 / B1 72 / B2 28).
Self-check: zero known defects. Awaiting independent proofreading.

## §1. Spec (measured, build 3)

- Print PDF: `La-Lucerna-VOL4-es-ja.pdf` — 8,530,855 B,
  SHA-256 `9a5338c3e29eefc4c42adc3c50c39f3acc1c3ab8f7326b52d6940f78beb76422`
- Web PDF: `La-Lucerna-VOL4-es-ja-web.pdf` — 1,280,435 B,
  SHA-256 `5f496c566aa337d3604527f4fe6f13fbae9443e4025e8f2525422b6c8eb08570`
  (built only with `tools/webpdf.py`; pdftotext print = web, 47,468 B,
  byte-identical; both < 7 MB)
- 8 SVG in `svg/`, 8 PNG in `cards/`
- `2026-w47-es-ja.text.md` (1,803 lines, exported from the production
  source with `extract_text_es_ja.py`; never extracted back from the PDF)
- `ABSTRACT.txt` (Japanese, one line, no ASCII double quotes)
- Paper #fbfaf6 on all 8 pages; masthead 196 units = 147pt; VOL.4 ×9 in
  SVG text; VOL.5 ×3 (all legitimate forward references to next week's
  issue); badge tricolour A2 #5c6e30 / B1 #46581f / B2 #37402f
- P8 badges: 35 chip rects — A2 11 / B1 21 / B2 3 — plus 1 #37402f header
  band rect (identical to core); Q113–150 all badged, none missing
  (Q113–120, Q145–149 chips present, visually confirmed)
- P8 minimum font 10.125pt (pypdf `Tm` parse, min d 10.125; 15 Tm entries
  — CJK runs share fewer Tm operations than Latin, the min is the gate)
- No "12 de noviembre" anywhere; no international politics
- The moth `<title>Lucerna 三色蛾</title>` (P1, inherited from core,
  invisible metadata) is left unchanged
- Japanese full-width punctuation (。、：（）＝) inside Japanese text is
  correct Japanese usage, not a defect; the Spanish letter's parens were
  normalised to half-width () per the W46 precedent (§6.10)
- Harvest note separators mix "=" and "＝" (e.g. #70 "correo = 郵便局／
  郵便の" vs #25 "debate＝討論") — inconsistent harvest style, cosmetic
  only, left as harvested (§6.15)

## §2. Per-page contents (frozen Spanish text; Japanese explanation layer)

- P1 Portada: lead "La campaña arranca: trece días para el 29-N";
  five-claves box; numbers box; "LA PALABRA DE LA SEMANA « el debate »"
  with 1-line gloss "「討論」：人々が公開で話し合う。"; quiz 7–10
- P2 Vida (A2): "La semana, día a día"; EL CALENDARIO "今週の予定";
  DECIR LA HORA; LOS DÍAS DE LA SEMANA; exercises 11–28
- P3 Cultura (A2→B1): flamenco + Santa Cecilia; Sargent "Bailaora
  española"; exercises 29–46
- P4 Deporte (B1): La Liga jornada 13; fixture table; exercises 47–64
- P5 Juventud (B1): first-time voting; postal vote; Black Friday;
  exercises 65–82
- P6 A fondo (B2): "Leer la campaña: debates, programas y encuestas"
  — band subtitle completed to "選挙戦を読む：討論・政策・世論調査";
  RTVE minutes chart; poll-ban chart; exercises 83–100
- P7 Lengua (A2/B1/B2): LA HORA / COMPARATIVOS / EL SUBJUNTIVO;
  ERRORES TÍPICOS; LA PALABRA; CARTAS DE LOS LECTORES (sample letter,
  no real letters had arrived — editor's note, §6.5); FRASES DE LA
  SEMANA; LA PRÓXIMA SEMANA (VOL.5); exercises 101–112
- P8 Ejercicios y respuestas: exercises 113–150; RESPUESTAS with a
  Japanese note per item; ✓ = model-text item (#150)

## §3. Measured totals

- run.py rc=0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- P2 col3 1022.0; P3 col3 1594.75 (13px above the 1608 divider);
  P4 col3 964.5; P5 col3 1601.55 (6.45px above divider, §6.11);
  P6 col3 1241.55; P7 col3 1865.51 (exactly the Latin target);
  P8-keys y=2521 (39px spare); P8-ex flow y=872 (bottom 1252)
- Occlusion audit 0 flags; bridge-orphan sweep 0 over 20 bridges;
  box-vs-hline sweep 0; bridge-widow sweep 0 (§6.13)
- p8 extract 150/150; compare CLEAN, keydiff=[137, 138] (§6.12)
- Freeze: tool 8 OK + direct sha256 of `build-copy/svg` vs shipped
  `svg/` 8/8
- Gloss-word token counts (core §8.1 method, per page): P1 reflexión 2;
  P2 mitin 2 / cartel 2 / escaño 2; P3 cante 5 / toque 6 / baile 9 /
  compás 4 / duende 5; P4 parón 2 / liderato 3; P5 papeleta 3 / censo 2 /
  plazo 4 — every Note word occurs ≥2 times on its page
- P8 multi-line items (diagnostic): only 5 — #31, #44, #88, #139, #140
  (§6.14); #137/#138 are 1 line each in Japanese

## §4. Sources reused from core-es (frozen)

All Spanish text, facts, dates, numbers, answer keys, images
(Sargent bailaora, Jebulon ballot box, Book of Hours initial, swan pen),
and the P8 key set are byte-identical to core-es except the explanation
layer and the two re-aimed translation keys (§6.12). No new trend
research; no fact changes; the 12 November decree date was NOT
reintroduced (no second independent source, W45/W46 rule).

## §5. Build commands (all from the repo clone, tools venv)

- Apply: `tools/venv/bin/python scratch-fanout-es/apply_fanout.py ja`
  (485 literal replacements; 2 manual-over-harvest overrides)
- Pre-fixes: 14 substitutions with count assertions (see §6.1–§6.10)
- Build: `tools/venv/bin/python run.py` (builds 1–3)
- Render: `tools/venv/bin/python render.py` (~180–240 s)
- Gates: `tools/occlusion_audit.py svg`; `sweep_de.py .` (orphans +
  box-vs-hline + widows); `tools/p8.py extract --p8 svg/p8-ejercicios.svg
  --total 150`; `tools/p8.py compare --edition-p8 svg/p8-ejercicios.svg
  --core-p8 core-es/svg/p8-ejercicios.svg --total 150`;
  `tools/freeze.py baseline --build . --core-svg svg --out
  scratch/freeze-es-ja-3`; pdftotext print vs web; pypdf Tm parse
- Text export: `tools/venv/bin/python scratch-fanout-es/extract_text_es_ja.py
  svg 2026-w47-es-ja.text.md`

## §6. Adjudications

### §6.1 Apply "leftovers" are false positives
`apply_fanout.py ja` reports leftover zh keys `VIDA　生活`
(content12.py) and `CULTURA　文化` (content34.py). Both are key==value:
the Chinese source string and the correct Japanese rendering are the
same shared kanji (生活 = life, 文化 = culture), and the apply report
shows each replaced 1×. Band titles verified: VIDA　生活,
CULTURA　文化, JUVENTUD　若者. No real leftover. CJK in .py is
expected for a Japanese edition (the script only reports it).

### §6.2 P1 gloss
Harvest "「討論」：2人以上が公開で話し合い、順番に発言し質問する。"
wraps 2 lines at sans 19 (542.5 units at gw). Shortened to
"「討論」：人々が公開で話し合う。" (302.9, 1 line) — parallel to
de "„Debatte“: Menschen diskutieren öffentlich." and fr
"« Débat »: des personnes discutent en public." The "two or more /
turns" detail survives in the Spanish definition above and the P7
word-box gloss. Measured in SANS at gw from the start (nl lesson).

### §6.3 P7 word-box gloss
Harvest "debate＝討論：順番に話す公開討論。今週は討論の週；選挙は29日。"
is already 2 lines at 20 (627.0 units at CW-44) — kept as harvested.

### §6.4 P7 ERRORES notes
All four are 1 line at 19.5 units at CW-44 (ERR1 210.6, ERR2 315.0,
ERR3 348.1, ERR4 283.2) — unlike fr/nl/ru, no shortening was needed.

### §6.5 P7 F-MAIL editor's note
Harvest "編集部より：締め切りまでに本物の手紙も最優秀作文も届かなかった
ため、今号は編集部の見本の手紙を掲載します。約束は VOL.5 に持ち越し
です。お便りをお待ちしています！" is 5 lines at both 20 and 19.
Shortened to "編集部より：締め切りまでに本物の手紙も最優秀作文も届か
なかったため、今号は編集部の見本の手紙を掲載します。約束は VOL.5 に
持ち越しです。" (4 lines at 19, CW-44; drops the "Write us!" closer,
as pt did with "Escrevam-nos!"). ldcn wrap 20→19, multiplier *29→*27,
para 20→19. P7 col3 lands 1865.51.

### §6.6 P5 your-turn kept at 4 lines @19
"郵便投票にする？　それとも直接行く？　ブラックフライデーでは何を買う？
実用的なもの、それとも衝動買い？　2文書いて送ろう。" is 4 lines at
both 20 and 19 (1168.0 units). Rendered at 19 (eh wrap 20→19, *29→*27,
para 20→19); P5 col3 1601.55, 6.45px above the divider — the same legal
margin as ru's P5, adjudicated identically. The only 3-line variant cut
the useful/whim choice that every edition's P5 keeps or adjudicates.

### §6.7 P3 your-turn rendered at 19
"フラメンコを聞いたことがある？　あなたの国の音楽で、魂を感じるものは？
2文書いて送ろう。" is 3 lines at both 20 and 19; rendered at 19 for
the 13px margin (box 1594.75). P4 your-turn (4 lines @20, box 964.5)
and P2 your-turn (6 lines @20, col3 1022.0) need no fix.

### §6.8 P2 C-intro shortened to 1 line
"2ページの記事を読んで、正しい答えを選ぼう。" wraps 2 lines with the
second line a lone "。" — shortened to "記事を読んで正しい答えを選ぼう。"
(325.7, 1 line at 20.5).

### §6.9 P5 B-bridge kept as harvested
"枠の中の言葉で空所を補おう。注意：活用が必要な言葉もある。" is 2
lines at 20.5 with both lines together in column 1 (sweep 0 orphans).

### §6.10 P6 band, P8 header, letter parens
Band subtitle completed to "選挙戦を読む：討論・政策・世論調査"
(full sub 831.7 units in sans 18, limit 1684) — the harvest's
"選挙戦の読み方" was the title only, not the subtitle. P8 header moved
1302→1337, keys flow 1328→1363 (right note 427.2 units wide at 19.5).
Letter parens full-width → half-width "(ejemplo, escrito por la
redacción)". Box titles all measured against their boxes — no pt-§6.13
overflow (widest: "LA SEMANA EN CIFRAS　今週の数字" 415.7/422.5;
"LOS MINUTOS GRATIS EN RTVE　minutos de propaganda por partido" is
core's own Spanish subtitle, identical in core-es, not a harvest gap).

### §6.11 P5 col3 1601.55
Adjudicated (§6.6): 6.45px above the y=1608 divider, audit 0 flags,
box-vs-hline sweep 0. Same legal margin as ru's P5.

### §6.12 keydiff [137, 138]
Re-aimed translation keys, W45/W46 ruling (keys are the Japanese
sentences "月曜日は国際フラメンコの日。 — 原文と比べよう。" /
"土曜日にセビージャ・ダービーを見る。 — 原文と比べよう。"), not a
defect. Note "原文と比べよう。" ("compare with the original").

### §6.13 Bridge widows (new defect class, found visually + by sweep)
Seven .bridge() strings wrapped with a lone "。" on its own line — visible
in the build-1 render, invisible to occlusion (0 flags) and to the
orphan sweep (the widow sits in the SAME column as the rest of the
bridge). One (P2 C) was shortened pre-build (§6.8); the other six were
found in rounds 1–2. Fixed to 1 line each (wrap-verified):
- P2 C (build 0): "2ページの記事を読んで、正しい答えを選ぼう。" →
  "記事を読んで正しい答えを選ぼう。" (§6.8)
- P4 A: "4ページの記事を読んで、正しい答えを選ぼう。" → same 1-line form
- P5 A: "5ページの記事を読んで、正しい答えを選ぼう。" → same 1-line form
- P5 C: "ir a + 不定詞で文を書きかえよう（近い未来）。" →
  "ir a + 不定詞で書きかえよう。" (keeps the volitional form; drops
  "文を" and "（近い未来）")
- P6 A: "上の2つのグラフを見て、正しい答えを選ぼう。" →
  "グラフを見て正しい答えを選ぼう。" (keeps "正しい答え")
- P4 C: "かっこ内の言葉の比較級か -ísimo 形で補おう。" →
  "比較級か -ísimo 形で補おう。" ("かっこ内" is redundant — the items
  already show "(malo)" / "(bueno)" / "(importante)")
- P4 D: "文を過去形（pretérito indefinido）に直そう。" →
  "過去形（pretérito indefinido）に直そう。" (keeps the tense name)
The widow check was added to `sweep_de.py` as a third check (it caught
the P4 C/D widows the visual pass missed). Lesson for ko/zh-tw: any
bridge ending in "。" whose text is just over one line (430–440 units
at 20.5) wraps with a lone "。" — measure every bridge, not just the
cross-column orphans.

### §6.14 P8 multi-line items
Only 5 of 150 wrap 2 lines: #31 ("Falso — フラメンコは踊りだけじゃない。
歌とギターと踊りの三位一体。"), #44 (core-consistent), #88, #139
(core-consistent), #140. #44/#139 are core-consistent wraps (as in
every edition). #31/#88/#140 are benign — the flow fits with 39px
spare and zero overflow; no tightening (the notes are accurate and
complete). #137/#138 are 1 line each in Japanese. #1 is 1 line.
#44's note wraps with the digit separated: "時間が先、動詞は2" /
"番目" — the renderer's character-level CJK break of "2番目"; the
wrap itself is core-consistent, the split point is a rendering detail.
#150 ✓ form: "模範文はこのページのHを参照（97語）" — matches the
W46 es-ja ruling ("模範文はこのページのH区（84語）"); the modelo
section H is on P8 itself (core P8 bridge: "范文（97 词）见下").

### §6.15 Harvest "=" / "＝" mixing (cosmetic)
P8 notes mix half-width "=" and full-width "＝" (#70 "=" vs #25 "＝").
Harvest inconsistency, rendered fine, left as harvested.

### §6.16 Exporter fix (extract_text_es_ja.py)
The build-1 .text.md showed key #82 as "282." — an exporter artifact,
NOT a render defect (the SVG element is exactly "82. Verdadero — ";
p8 extract 150/150 CLEAN). Cause: the renderer's CJK wrap splits
#44's note "動詞は2番目" as "2" (own Latin run, x=950.2, col 1) +
"番目" (next line); the extractor's flat 9 px/char width model
under-counted the CJK predecessor run ("時間が先、動詞は", true end
950.2), computed a 36px gap, split the "2" off, and glued it onto the
next column's key ("82.", x=989 — 29.8px away, under the 30px split
threshold). Fix, in the scratch copy only: per-char width model
(CJK/full-width → 1 em, Latin → 9 px flat, as the export was tuned)
plus a column-boundary split (a segment never spans two columns).
Re-exported: "282." → "82.", all 150 keys present, no numbers >150;
the full diff vs the first export is re-flow only (character multiset
identical ignoring whitespace; +2 recovered U+3000 separators).
Core's own .text.md has no such line (its #44 note breaks elsewhere),
so the bug is latent in the shared extractor and bites only when a
CJK note wraps with a digit at the break — ko/zh-tw must use the
fixed extractor copy, not the flat-9 original.

## §7. Self-proofread record

- Round 1 (build 1, all gates + full .text.md read + 8-page visual):
  6 lone-"。" bridge widows found (P4 A, P5 A, P5 C, P6 A visually;
  P4 C, P4 D by the new sweep check). All other gates green on build 1
  (0 overflow, P8-keys 2521, occlusion 0, p8 CLEAN, freeze 8/8).
- Round 2 (build 2, after the first 4 bridge fixes): gates green;
  sweep found the remaining 2 widows (P4 C, P4 D).
- Round 3 (build 3, final): run rc=0, 0 overflow, TOTAL 150;
  render rc=0; occlusion 0 flags; sweeps 0/0/0; p8 150/150 CLEAN;
  freeze tool 8 OK + direct sha256 8/8; pdftotext print = web 47,054 B
  byte-identical; P8 min font 10.125pt; §1.1 measured; .text.md
  re-exported (1,803 lines) and key-number verified (1–150 all present);
  P4/P5/P6 re-inspected visually — all bridges 1 line, no widows.
  Zero findings.

## §8. 重建（re-fanout，2026-11-11 — core build 10）

Core baseline: core-es fix build 10 (independent re-proof (a), zero findings) — print 17,212,955 B SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`, web 1,410,471 B SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`, text.md 1,822 lines SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
Method: old edition backed up to `scratch-refanout-es/backup-old/` (verified identical), deleted, re-applied via `scratch-fanout-es/apply_fanout.py`; `classify.py` diffed fresh sources against the backup line by line — KEEP = core build-10 change, REVERT = edition hand fix restored, MERGE = derbi letter line (fresh sábado + backup ASCII parens), INSERT = RTVE debate-a-ocho timeline row. No commit, no push.
Common core changes kept: C1 (P1 CINCO CLAVES box 700→720), C2 (`antes del jueves`→`hasta el jueves`), es-ja D1 (consejo completed) + D4 (derbi sábado 21st), es-nl D1/D2, es-pt C2 (PCTE kept, 195 kept). C3 (P5 vocab `content56.py:79`) left as-is per adjudication.
Gates (all green unless noted): run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; render rc=0; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated — translation items keyed by target-language sentence); freeze 8/8 SVGs byte-identical; freeze-diff CJK accounting clean; canonical creambox.py full scan 0 own-ink overflow (the 6 raw negative lines per edition are the known below-box headings, identical to core); creambox_diag 0 own-ink negatives; boxtitle 0 overflow; keycheck 149/150 (only the #150 open-question `✓` exception); sweep 0 orphans / 0 box-vs-hline; pdftotext print = web bytes; P8 min effective font 10.125pt (≥ 9.75pt floor).
Classify: KEEP 17 / REVERT 19 / MERGE 1 / INSERT 1 / DELETE 0. Build: run1 rc=0, TOTAL 150, P8-keys y=2521. New print 17,294,448 B SHA `459d570a294a14a3b170e7bf99ca4db3bc91560603dc21c43d371977e55da12f`; web 1,540,831 B SHA `5895fce90fffd07cccf1909f8de1aa481572751e8caa9bc3a0d80be00845f71f`; text.md 1,820 lines SHA `7479077861f46c27c4d69ae265d43bab40e14cdc2e09bec48d53772142b3e9ea`; print/web text 109,951 bytes, identical.
Hand fixes: none task-listed for es-ja (all core items resolved by the rebuild; D2 = C3, untouched). Freeze-diff CJK accounting: added characters are Japanese explanations only. Boxtitle gate: 2 known key==value false positives (`VIDA　生活`, `CULTURA　文化`) — counted as leftovers by the checker, not overflows.

## D5 重建记录（2026-11-12，B档）

- 安装：`mechanism/apply_variant.py --svglib <本版>/svglib.py --target es --reader ja`（mode=cjk，按字符文字分流，不加 `_READER_LANG` 门）；`svglib.py` md5 `6a46ee51…` → `091da842…`（安装器同时补 port 了 fix2，CJK 索引 SC→JP，kinsoku 块自 core-zh-tw 移植）；路由断言 10/10（`route_assert.py`，mode cjk）；机制 `test_d5_routing.py` FAILURES: 0；修前基线：印 17,294,448 B `459d570a…`、网 1,540,820 B `6c6a273d…`；D5 普查 346 violations（与裁定 §1.1 预期一致）；boxtitle 0 DEFECT；occlusion 0。
- 预修 3 项共用版式（与 core-es 相同西班牙语串、同栏宽）：P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt、P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt、P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。
- 逐项修 3 项（均为 D5 新缺陷，修前基线 0；CJK 类：拉丁头在 Newsreader SemiBold 下加宽，把日语尾顶出框）：P1 框题 `LA SEMANA EN CIFRAS　今週の数字` +22.5px——该框 `tsize=21`（21pt advance 389.8，余量 14.7px）；P5 框题 `EL PLAN DE LA SEMANA　今週の計画` +36.7px——该框 `tsize=20`（21pt 余量仅 1.7px，取 20 求稳）；P7 手工题 `ERRORES TÍPICOS　よくある間違い` +8.7px——23→22pt（余量 9.2px）。以上文字均未动。注：ink=advance（尾字为全角 CJK），框题可用宽 404.5px、手工题 400.5px。
- 门禁全绿：run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0（`head_check.py` PASS 0 defects）；render rc=0；D5 普查 0；U+201C 普查（`census_quotes.py`）0（KR 引号不扩展，裁定 §3）；occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，仅读者语译注差异）；boxtitle 0 DEFECT（注：修后标题数 30→26——tsize 降至 21/20pt 的两框题与 22pt 手工题被工具归入 body 行计数，属分类口径，非缺陷；creambox 几何审计确认无越框）；creambox（仓内 `tools/d5_creambox_audit.py`）PASS 0 defects（P8 220 行、页脚余量 36.4px 不变；P1 行数 121→118、P5 118→120 为框题字号改变致框高变化）；spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 2,946 个——为日语读者层相对 core-es 中文读者层的正当差异；同版 freeze diff（修前基线 vs 新版）新增 CJK 字符仅 1 个 U+3000（run 拆分 artifact）；印/网文字层 38,692 字符、6,991 词一致。
- 新 PDF：印刷版 8,530,855 B SHA `9a5338c3e29eefc4c42adc3c50c39f3acc1c3ab8f7326b52d6940f78beb76422`；网页版 1,280,435 B SHA `5f496c566aa337d3604527f4fe6f13fbae9443e4025e8f2525422b6c8eb08570`。`text.md` 字节不变（SHA `74790778…`）。日志：`hidden_files/w47/scratch-d5-rebuild-es/2026-w47-es-ja/`。

## es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）

- 改动：F2（P6 时间轴措辞：`(sin el PSOE)` → `(sin el PSOE confirmado)`，与正文一致）。F1（缺首字下沉）按协调员裁定不修：全刊引擎级缺口，进模板 backlog，见 FIX-LOG。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 更新（core-es 为 D5 工具重导出；其余 10 版手术替换，diff 只含意改行；ru F4 另做词级手术，见 FIX-LOG 陷阱核查节）。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 B，SHA-256 `6d89a8ddf67bc83b48c1c9650bc7daf0c1247e3eec8b943fb71bf60ec5fb726e`；网页版 `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,428 B（< 7 MB），SHA-256 `c2e0230bac8c17b7e06be61dfa981818ca433c73171f0de0af1eb705701bfae2`；text.md `2026-w47-es-ja.text.md` 46,565 B，SHA-256 `998a9ac325003cde55ed13facad56b3b98e6802a5f64985da1211298c50fe4c6`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 26 titles, 346 body lines，0 DEFECT；spill 0 SPILL（27 盒，84 candidates）；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8；印/网 pdftotext 47,479 字节逐字节一致。
- 日志：`hidden_files/w47/scratch-fix-es/`（FIX-LOG.md、build-all.log、build-resume.log、gates-all.log、text-pre/）。

## 第二轮独立重校修复 G1（2026-11-12，PROOF-NOTE-2 (b) 返修）

- 改动：G1（es-ja P8 第 30 题答案简析）：`content34.py:64`「ユネスコが2010年にフラメンコを世界遺産に登録」→「ユネスコが2010年にフラメンコを無形文化遺産に登録」（佛朗明哥 2010 年列入的是 UNESCO 人类非物质文化遗产代表作名录，非世界遗产名录）。答案字母 Verdadero 不动。改后全版「世界遺産」0 残留、「無形文化遺産」在 P8-30 在位。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 手术替换 1 行（L1772，断言原文后替换；D5 导出器干跑重分段 1112 行且首行误标为 core-es slug，故不直接落盘重导出，见 FIX-LOG-2 陷阱核查节）。diff 只含本轮 1 行。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ja.pdf` 8,530,586 B，SHA-256 `cbb3efedd9a2e9df2ade256bf5a7141a8ffd896412c59522e4b65c82fc7e6a85`；网页版 `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,143 B（< 7 MB），SHA-256 `70d46e27721f49dcca24fc6b12bd6d27d5582d16ea46031e1c97c2674639ebf5`；text.md `2026-w47-es-ja.text.md` 46,578 B，SHA-256 `bab03d4d6c8af7dc4d160aafd89a0367f3132ffaade336b0666125ae0bf52cfb`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 26 titles, 346 body lines，0 DEFECT，0 OBSERVE，0 marginal；spill 0 SPILL（27 盒，84 candidates，84 OBSERVE）；edge 8 页 0 TOUCH / 0 NEAR；D5 census PASS（弯引号 U+201C/U+201D 全版 0）；freeze baseline 8/8；印/网 pdftotext 47,487 字节逐字节一致；P8 答案 1–150 全有。
- 日志：`hidden_files/w47/scratch-fix2-w47-es/`（FIX-LOG-2.md、build2.log、gates2.log、text-pre/）。

## 第四轮独立重校修复 I1（2026-11-12，PROOF-NOTE-4 §2 返修）

- 改动：I1（text.md 专属，低）：两栏/两块拼接处丢空格致文字粘连；本版共 7 处（与 PROOF-NOTE-4 表列一致）：分版粘连 0 处（无）；目录粘连 7 处（`Pág. 2La semana` … `Pág. 8Ejercicios y respuestas` → 各补空格）。
- 重建：未重建（PDF 未动）；text.md 手术替换 7 处（逐处先断言原文存在再替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 7 行，行数不变（1821 行）。
- 文件：text.md `2026-w47-es-ja.text.md` 46,578 B（I1 前 46,571 B，+7 B）、1821 行，SHA-256 `bab03d4d6c8af7dc4d160aafd89a0367f3132ffaade336b0666125ae0bf52cfb`（改前 `29961f6fbc19d80121664353f90843b76ce759d16b1c9354bd9487ce2d19e9f1`）；印/网 PDF 未动，SHA 不变（印 `cbb3efedd9a2`、网 `70d46e27721f`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；D5 普查 PASS（弯引号 0/0 在 Newsreader）。
- 日志：`hidden_files/w47/scratch-fix4-w47-es/`（FIX-LOG-4.md、fix.py、fix2.py、fix-report.json、text-pre-*.md、gates4.sh、gates4.log、p8-extract/compare、census）。
