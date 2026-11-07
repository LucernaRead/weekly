# Lucerna Weekly — VOL.2 — W45 edition KIT

**Slug:** `2026-w45-zh-tw-ja` · **Issue week:** Nov 2–8, 2026 · **Target:** Traditional
Chinese (zh-tw) · **Reader native language:** Japanese · **Pages:** 8 · **Exercises:** 150
· **Status:** BUILT (NOT finalized — fix round complete, fresh full proofread pending;
coordinator inserts only on ZERO PROBLEMS)

**Delivery dir:**
`~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ja/`
**Build dir:**
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-tw-ja-build/`
(transform.py + verify.py + scans.py + run/render/verify/Gate-10 logs)

## 1. Baseline (before any edit)

`freeze.py baseline` reproduced all 8 zh-tw core SVGs byte-identically, and the shipped
core SVGs were re-hashed unchanged at the end of the build (see §11). Core SHA-256
prefixes: p1-front `4672c972763b0eaf`, p2-life `889fb533ef3ff62e`, p3-culture
`508703c2b3c313c6`, p4-sport `e04b62ea6211c9ff`, p5-youth `4dfce72d88000fbc`,
p6-deep `06ba4c6627cb8165`, p7-lang `00ac7f57125fcc09`, p8-test `e6e97d02595aef3b`.

## 2. Target-text freeze (run level)

- Registry (one-process run, identical to the zh-tw core): total **150**; levels
  A2 44 / B1 74 / B2 32; pages P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 /
  P8 38; types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1. This is the
  zh-tw core's split, NOT the zh-cn core's.
- Source-level verification (`verify.py` sections A1/A2, after the final patch):
  **A1 = 0** transform olds remaining in edition sources;
  **A2 = 0** core literals lost from edition sources (multiset comparison, so the
  folded MODELO constant counts once it is present in both).
- Rendered-string attribution (`verify.py` B1/B2): **B1 = 0** unattributed added
  strings, **B2 = 0** unattributed removed strings — every added/removed rendered
  string is accounted for by a transform replacement, a gloss prefix, a P8 key-line
  prefix, an instantiated f-string page line/separator, or a frozen-MODELO re-wrap.
- `freeze.py diff --strict-cjk` displays **STRICT-CJK FAIL** with TOTAL added CJK
  characters **5992** (per page: p1 395, p2 342, p3 414, p4 353, p5 418, p6 431,
  p7 1140, p8 2499; added/removed string counts p1 +22/−22, p2 +33/−35, p3 +38/−38,
  p4 +33/−33, p5 +37/−40, p6 +37/−37, p7 +88/−90, p8 +192/−191). This FAIL display
  is structurally inevitable for a Japanese explanation layer (kana/kanji exceed
  the core) and is the same situation W43 zh-tw-ja closed by per-string attribution
  (its KIT §7). The close here is the B1/B2 = 0 attribution above, NOT a claim of
  added CJK = 0. Reported honestly for the proofreader.

## 3. Traditional independence (hard gate)

- CJK union test (`verify.py` C): edition CJK set **1029** characters; union of
  (W43 zh-tw-ja shipped SVGs + zh-tw core shipped SVGs) **1288**; outside **57**:
  kana `げ じ ほ ょ ろ ゥ ォ ゴ サ ゼ ャ ョ`, kanji
  `仮 伝 催 写 削 割 募 勤 区 収 団 寒 彫 役 待 応 感 抑 援 撃 映 昼 晩 毎 浴 済 無 独 砂 税 素 荷 菓 装 裏 覧 賃 赤 込 録 除 険`,
  punctuation `－ ／ ～`. All 57 are Japanese explanation-layer characters/punctuation
  (ordinary Japanese words such as 毎日, 保険, 展覧館, 砂, 寒い), not Traditional
  target text. Target-text freeze is proven separately by §2 (A1/A2/B1/B2 = 0).
- Simplified-only spot list over frozen shared strings (`verify.py` D): **0 hits**
  (spot list: 让说国学发对为经时车马龙凤云电动话语读认点头乐尔广厂厅开贝见长门问间队阳阴孙学宝实汉刘关应并复万与发).
- No OpenCC, no mapping table, no conversion logic anywhere in the transform.
  Target text comes only from the frozen zh-tw core + W43 zh-tw-ja precedent furniture.
- svglib kept unchanged: the W45 zh-tw core svglib and the W43 zh-tw-ja build svglib
  are byte-identical (md5 `a269e147529bcb0a1f2dd3aa22fa5658`). Per the W43 KIT §2
  three-way ruling, this edition keeps the core svglib unchanged and renders
  Japanese explanations on the TC face, as W43 did.

## 4. Furniture — three-way measurements (core · W43 zh-tw-ja · this edition)

| Item | zh-tw core | W43 zh-tw-ja (shipped) | This edition |
|---|---|---|---|
| P1 badge slot | x=975, y=378, 21pt, weight 700, fill **#3e4c2a (OLIVE)** | x=975, y=378, 21pt, 700, **#3e4c2a (OLIVE)** | x=975, y=378, 21pt, 700, **#3e4c2a (OLIVE)** |
| P1 badge text | `繁體中文正文 · 英語講解 — Traditional Chinese te…` | `中国語（繁体字）テキスト · 日本語の解説 — 日本語読者のための版` | identical to W43 |
| Footer | `Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations` | `Lucerna · 中国語（繁体字）週刊 VOL.1 · 本文は中国語（繁体字） · 解説は日本語` | `Lucerna · 中国語（繁体字）週刊 VOL.2 · 本文は中国語（繁体字） · 解説は日本語` |
| Page line | `第 N 版 / 共 8 版` | `N ページ（全 8 ページ）` | identical to W43 |
| Gloss prefix | `Notes｜` (bslib4) | `解説 — ` | identical to W43 |
| P8 header | `答案 · Answer keys — in page order, with a short English note for every item` | `答案 · 全解答と解説（1–8ページ）` / right `解説はすべて日本語 · ✓ = 作文の課題` | identical to W43 |
| P8 separators | `— Page N —` | `— N ページ —` (13.3pt, lh 1.16, gap 2 in W43) | `— N ページ —` but W45 core metrics (12.8pt, lh 1.12, gap 1) to avoid reflowing the keys flow |
| P8 style | — | DASH (shipped code parses dash/lines) | DASH (W45 core already prints dash: `N. key — note`, writing `N. ✓ note`) |
| P8 band | `測驗與答案 · Test & keys` | `測驗與答案 · テストと答え` | identical to W43 |
| P8 band sub | — | `第 8 版 · 本週大測驗 + 全部答案 · 今週のテストと全解答` | identical to W43 |

**Badge colour discrepancy — flagged for the proofreader, not resolved by the builder:**
the task brief said BRICK #a4553a, but BOTH shipped references (the W45 zh-tw core
itself and shipped W43 zh-tw-ja's own P1) measure OLIVE #3e4c2a at the same slot.
This build follows the shipped precedent (OLIVE); the transform replaces only the
badge string, never the colour.

Band titles (Traditional · Japanese): 生活 · 暮らし, 文化 · 文化, 體育 · スポーツ,
青年 · 若者, 深讀 · 深く読む, 語言 · ことばの焦点, 測驗與答案 · テストと答え.
Section heads (W43 precedent where it exists): Fill in → 空所補充, Match →
語と意味を結ぶ, Writing → 作文, 讀懂了嗎? → 読めたかな？, 填一填 → 埋めてみよう,
算一算 → 計算してみよう (3 occurrences: P2, P3, P5), 看圖答題 → グラフを読もう,
深讀測驗 → 深読みクイズ, 快速測驗 → クイッククイズ, 標題填空 → 見出しの言葉,
本週大事 → 今週の主な出来事, 本週一詞 → 今週の言葉, 事實框 → 今週のファクト,
你呢? → あなたは？, 練習例子 → 練習の例; P7 heads: 易錯診所 → 間違いクリニック,
本週句式 → 今週の文型, 讀者園地 → 読者の広場, 本週金句 →
今週のフレーズ — 本文から一字一句そのまま; P8 section heads: A → 正しいか間違いか,
B → 総合クイズ, C → 文を完成させよう, D → 読んで答えよう, E → 会話の場面,
F → 書いてみよう. Bylines follow W43 form `本紙スタッフ · 出典：…` (P1/P6 event
press release + FAQ; P4 TSNA sports news). Photo credit lines stay frozen verbatim.

## 5. P8

Invocation (default form resolved the core's p8-test.svg, so no explicit-path form
was needed):
`./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-zhtw-core --edition-dir ../files/weekly-report-w45-zh-tw-ja --target zh-tw`
→ **CLEAN, 150=150, missing=[], extra_count=0, keydiff=[]**.
`p8.py extract --p8 ../files/weekly-report-w45-zh-tw-ja/svg/p8-test.svg --total 150`
→ 150/150, parse lines (dash style). Writing model verbatim (band-checked); P8 keys
flow last-line ink bottom 2538.1 (footer rule 2580).

## 6. P7 golden sentences

All 8 verbatim from this issue's own articles, each exactly **2× issue-wide** after
punctuation normalisation (article + P7; the P7 quote uses full-width ， where the
article uses half-width ,). Page tags in the core's `p. N` form: (p. 1)×2, (p. 2)×1,
(p. 3)×2, (p. 4)×1, (p. 5)×1, (p. 6)×1 — matching the core's p. 1×2, p. 2, p. 3×2, p. 4, p. 5, p. 6.
The 3 error-clinic 「…」 lines are not phrases and count 1× each, as expected.

## 7. Occlusion and geometry gates (all fixed render)

- `occlusion_audit.py selftest`: OK (all planted classes fired, clean controls silent).
- Edition: **0 flags**; core: **0 flags**; NEW vs core **0**.
- Same-baseline ink-collision scan (README #10, furniture bands incl. P1 top band):
  edition **0**, core **0**.
- P4/P6 chart-label graze check (text ink vs later-drawn rects): edition **0**,
  core **0**.
- Stricter border-strike scan (text ink crossing any bordered-box border line, to
  catch cases the audit's centre rule can miss): edition **0**, core **0**.
- Two NEW BOXTITLE flags found on the first render were fixed **in the transform**
  and the build re-run from a fresh copy (see §8); the audit above is on the fixed
  render.
- Kinsoku line-start scan (fix round, §18): 0 lines starting with a closer punctuation
  AND 0 lines starting with a small kana out of 1425 edition nodes (core: 0/1431);
  line-end NO_END scan 0. The original build's scan covered punctuation closers only —
  see §18 for the two small-kana sites it missed and the scan now added to verify.py
  (section H) and scans.py.
- Stray ASCII apostrophes in rendered text: edition **0** (core: 28, all in the
  English notes now replaced).
- Zero FLOW OVERFLOW / HEAD TOO WIDE warnings in both the delivered run and Gate 10.

## 8. Occlusion fixes folded into the transform

- **P2 `你呢?` box** (fixed 230px rect, border bottom 1322.0): the first Japanese
  you-line wrapped to 3 lines, last line `か。` ink bottom 1327.2 > border. Fixed by
  shortening the line in the transform to
  `立冬にはどんな鍋を食べたいですか。ダブルイレブンのカートの中身は何ですか。`
  (measured 2 lines with the build's wrap() at 20pt sans, width 390), preserving
  the original meaning (Double 11 cart contents).
- **P7 readers'-corner box**: the 7-line Japanese disclosure overflowed the computed
  box height (last line ink bottom 1782.0 > border 1774.4). Fixed by shortening the
  disclosure to the 6-line form in §9 AND bumping the box-height formula's bottom
  pad 26 → 42 in the transform (the core formula runs ~8px short of rendered
  last-line ink). After the fix: P7 col3 ends 1761.36; P7 teaser rect bottom
  **2559.36** (20.64px clear of the 2580 footer rule; teaser last-line ink bottom
  2528.11).
- Observation (not used as an adjudication for own flags): the core's own P7
  readers'-corner last line also sits past its box border (baseline 1751.63 vs
  border 1745.4) but audits clean, apparently because the audit's BOXTITLE
  candidate rule (anchor-point or ink-centre inside the rect) does not associate
  that line with its box. This build's own flags were fixed regardless.

## 9. Readers' corner

Traditional letter (lt) and Traditional disclosure (lt2) frozen line-for-line from
the core. English disclosure (lcn) replaced with a Japanese disclosure stating no
genuine letters exist plus a verbatim open invitation. Exact delivered form:
`これは編集部の例文で、本物の投書ではない。VOL.1は今号から本物の手紙と第8版の優秀作文を掲載するとしたが、締切までに掲載できる投書がなく、例文を掲載し、募集は続けている。あなたの手紙を次号でお待ちしています。`
(W43's precedent had a forward promise form, not a separate invitation sentence, so
the W45 JA invitation mirrors the core lt2 closing `你的來信，下一期見`.)

## 10. AI-variant trap

The W43 zh-tw-ja column has NO AI precedent (its content contains no AI note;
verified by grep). This core has three distinct AI forms, all translated separately:
P6 gloss `AI+ (artificial intelligence inside banks, investment and insurance)` →
`AI＋（銀行・投資・保険の中のAI）` (avoids coining 人工知能); P6 note
`AI helps read data, spot risks and answer clients.` →
`AIはデータを見て、リスクを見つけ、顧客の質問に答える手伝いをする。`; P8-key note
`AI inside finance is 人工智慧＋.` → `金融の中のAIは人工智慧＋。` (verbatim target
term kept, as it is already in the core's key; no new target CJK from that note).
Note: full-width parens/＋ in P8 notes count as CJK in freeze.py — part of why the
strict-CJK display FAILs (see §2).

## 11. Gloss / match / images

- Gloss boxes (rendered `解説 — ` vs core `Notes｜` prefix counts): core = edition
  per page p1 2, p2 2, p3 3, p4 2, p5 2, p6 1, p7 0, p8 0 (total **12** gloss calls).
  No core gloss string contains `·`, so gloss items = gloss calls = 12 (NOT zh-cn's 33).
- Match sets: 4 sets × 4 items = **16** 配對, matching the registry; match
  lefts/rights frozen (covered by §2 attribution).
- Image payloads (per-page base64 hash, byte-identical core vs edition):
  p1 `ac4dfe2ad3a43cd3` (harbour.jpg, Wilfredor, CC0),
  p2 `a40e7a2b265beba6` (rain.jpg, CorraleH, CC0), p3 none,
  p4 `18ad8ae06fac2860` (baseball.jpg, Bain News Service, Public domain),
  p5 `bcbada13a5ae19d6` (pumpkin.jpg, Benjamin Balazs, CC0), p6/p7/p8 none.
  Credits verbatim identical on all pages.
- P4 provenance is CLOSED and NOT re-litigated: the core KIT records a binding
  coordinator adjudication dated 2026-10-27 that the P4 baseball photo (Bain News
  Service, Washington team 1908) is verified; placed bytes and credit unchanged
  means provenance is not re-opened.

## 12. Coordinator additional check (rendered-output sweep)

- Full rendered-output sweep of ALL text nodes (verify.py section G) was run on the
  delivered SVGs. Every node containing `[A-Za-z]{2,}` is adjudicated in §13.
- The P3 C34 tail pair `算一算 · Work it out` that the sibling inventory missed:
  **already translated** in this edition — `算一算 · 計算してみよう` appears on
  P2, P3, and P5 (3 occurrences), and `Work it out` occurs 0 times. No late fix was
  needed; the sweep confirmed it, plus 0 occurrences of every other English head
  (`Did you get it`, `Over to you`, `Quick quiz`, `Headline words`, `This week`,
  `Word of the week`, `Practice example`, `Read the chart`, `Deep-read quiz`,
  `True or false`, `The big quiz`, `Read and answer`, `Say it in context`,
  `Test & keys`, `Language focus`, `Fill in`).
- Gate 10 template note: this build did NOT inherit an es Gate 10 template (its
  transform.py was written fresh with whole-line OUT/BASE repointing); no repoint
  fix was applicable, and the Gate 10 run below verified no stray nested tree.

## 13. Residual-Latin adjudication (rendered sweep, section G)

No English explanation prose remains. Every Latin-containing rendered node is one of:
masthead/band/footer `Lucerna`; frozen edition line (VOL.2, dates); Japanese
bylines/glosses retaining `FAQ`, `TSNA`, `ITF`, `C.C.メルセデス`; frozen article
proper names (`StartmeupHK`, `Fintech Nexus: Bridging the World, Building the Future`,
`ITF`, `SUPER STAGE`, `SOLID TIDES`, `Trick or Treat`, `JUMP`, `MVP`); Japanese
gloss citations (`StartmeupHK`, `ITF`, `JUMP`, `MVP（最優秀選手）`); photo credits
(`Photo: … — CC0 / Public domain (Wikimedia Commons)`); P7 `VOL.1` (frozen
disclosure + Japanese disclosure) and teaser `次号予告（VOL.3）`; P8-note
abbreviations `AI`, `MVP`, `SNS` (in the 打卡 note: 写真付きでSNSにチェックイン);
P7 tags `(p. N)`; P8 key letters. All other Latin nodes are the frozen Traditional
article text itself.

## 14. Eyeball review (all 8 cards, 1950×2700 PNG)

P1–P8 each inspected: no overflow, no overlap, no footer collision, image/credit
placement correct, P7 teaser clear of the footer rule (rect bottom 2559.36, ink
2528.11), P8 keys end 2538.1. No missing-glyph boxes; Japanese renders correctly
on the TC face.

## 15. Gate 10 self-run (fresh core copy + transform ALONE + one-process driver)

- Scratch: `hidden_files/weekly-report-w45-zh-tw-ja-build/gate10/` (NOT /tmp, NOT
  inside the delivery/build dirs). Fresh copy of the core build dir; transform.py
  run ALONE against it with the gate edition root
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-tw-ja-build/gate10/edition`
  (whole-`expanduser(...)` repointing verified literally in the copy's content12.py
  and render.py — no temp dir spliced inside the `~/workspace/...` prefix).
- Gate run: exit 0, zero `!!` warnings, registry identical (150; A2 44 / B1 74 /
  B2 32; 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1).
- Gate render: exit 0; gate PDFs byte-size-identical to delivered (print 17,606,181;
  web 3,308,957).
- Gate SVGs vs delivered SVGs: **8/8 byte-identical**.
- No stray nested tree: gate edition contains only `svg/` + `cards/` + PDFs;
  delivery dir contains only `svg/` + `cards/` + PDFs + ABSTRACT.txt + WEEKLY-KIT.md.
- Transform is single-use on a fresh copy by design: a second run on the same copy
  fails on the first already-replaced string (assertion), which is why Gate 10 uses
  a fresh copy.

## 16. Artifact pins (delivered)

SVG SHA-256:
p1-front `dc36d99206915d076365d95826e664e73a5065b64bed90177d18a51b815eaac5`,
p2-life `45872bce8345bbaf8863e4ff3bd16df40ab069686bd51808826eff1bcc1437bd`,
p3-culture `aa58b266ec10b54a19197f2ba8903a2dd742d920a1c3eb4d9661f4c3a0634ce4`,
p4-sport `701bd92da8f101e3a8d8296bc468c90422d30a56027a35edd2e2275a13b749d1`,
p5-youth `326b641e72cc71c816345ab891457aa6cd3ba1edb97924461727307939fbb9e9`,
p6-deep `9970560b86c78ba1550985495910d203767ba8a77821099a27f590f7c91d2b29`,
p7-lang `e07438a80eccc83423562bbd9155744e2533bdb7d6d077f24d8c78c687ffd9c3`,
p8-test `d0f58c06a5f7cb6b45f9a070932d06031e16d9449ae4192a6c647c0ddccedc1e`.

Card PNG bytes (all 1950×2700): p1 1,131,378; p2 1,270,402; p3 1,072,967;
p4 1,044,850; p5 1,337,283; p6 945,176; p7 1,088,820; p8 1,291,502.

Print PDF `Lucerna-VOL2.pdf`: **17,606,366 bytes**, 8 pages,
SHA-256 `2a65419a5a206153b2ca8926a6a81c03b3fa8e3a9a72afdf7617d0b62630e945`.
Web PDF `Lucerna-VOL2-web.pdf`: **3,309,173 bytes**, 8 pages (< 10 MB),
SHA-256 `eebf0102e4ad37c39a90d50fce831842b4fcae9b2e22a02bcd7d44c5394b189f`.

Core SVGs re-hashed unchanged at the end (prefixes in §1 all match baseline).

## 17. Notes for the proofreader (non-blocking)

1. Badge colour: brief said BRICK #a4553a; both shipped references measure OLIVE
   #3e4c2a — this build follows shipped precedent (§4). Adjudication requested.
2. Strict-CJK FAIL display + per-string attribution close (§2) and union outside-57
   adjudication (§3) — the correct resolution for a Japanese explanation layer,
   reported exactly, not adjusted to fit the brief's literal wording.
3. P7 teaser margin: rect bottom 2559.36, 20.64px clear of the 2580 footer rule.
4. Core's own P7 readers'-corner last line sits past its box border while auditing
   clean (§8 observation) — context only, not an adjudication for this edition.
5. NOT shipped, NOT finalized, NOT inserted, NOT posted anywhere. Awaiting
   independent proofread; coordinator inserts only on ZERO PROBLEMS.

## 18. Fix round (independent proofread NOT PASS → 2 rewordings, full re-render, full re-gate)

First proofread verdict: NOT PASS with exactly two blocking items, one defect
class at two sites — a Japanese line starting with a small kana (sutegana).
Root cause, as the proof established: the renderer's NO_START set covers
punctuation closers only, NOT small kana, and this build's `verify.py` /
`scans.py` had no kinsoku section, so the two sites were missed. Both fixes
live IN THE TRANSFORM (no hand patch to any delivered SVG); the whole issue
was re-rendered from a fresh core copy and re-gated in full. Nothing else
was reworked: only the P5 and P8 SVGs (and their cards/PDFs) differ from the
first build — the other 6 SVGs are byte-identical to the first build.

### 18.1 Rewording 1 — P5 gloss (small ィ at line head)

- Old (transform, content56 gloss): `…韓国のJUMPテコンドー・コメディショー、…`
  rendered as line `花笠舞、韓国のJUMPテコンドー・コメデ` + next line starting
  `ィショー、毎日14時のマスコットパレー…` — コメディショー split with ィ stranded.
- New: `…韓国のJUMPによるテコンドー・コメディショー、…` (added による, purely
  grammatical: "the taekwondo comedy show by Korea's JUMP"). Meaning and the
  gloss's function (travel-fair game plan: watch the shows first) are preserved;
  the target text is untouched; only the Japanese explanation sentence changed.
- New render: line `花笠舞、韓国のJUMPによるテコンドー・` + line
  `コメディショー、毎日14時のマスコットパレード）、…` — the loanword sits whole
  on one line. Gloss line count unchanged (7 lines, last line `と。`).

### 18.2 Rewording 2 — P8 key-2 note (small ョ at line head)

- Old (transform, content12 registry note, rendered only as P8 key 2):
  `メインカンファレンスは香港コンベンション・アンド・エキシビション・センターで開催。`
  rendered as `2. A — メインカンファレンスは香港コンベンション・アンド・エキシビシ`
  + next line `ョン・センターで開催。` — コンベンション split with ョ stranded.
- New: `メインカンファレンスは香港コンベンション・エキシビション・センターで開催。`
  (dropped the conjunction アンド only). Meaning preserved: same subject (the
  main conference), same venue (Hong Kong Convention and Exhibition Centre),
  same key–note correspondence — the proof's shorter suggestion
  (`香港コンベンションセンターで開催。`) was NOT used because it drops the
  main-conference subject. The P1 gloss sentence mentioning the same venue is a
  different string and was not touched.
- New render: `2. A — メインカンファレンスは香港コンベンション・エキシビション・セ`
  + `ンターで開催。` — clean line head. P8 keys end ink unchanged at 2538.1.

### 18.3 New small-kana scan (method + counts)

- Method (W43 zh-tw-ja precedent): every `<text>` node's first character is
  checked against (renderer NO_START punctuation set
  `。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;"` PLUS small kana
  `ぁぃぅぇぉっゃゅょゎゕゖァィゥェォッャュョヮヵヶ`), and every node's last
  character against NO_END (`「『（【〈《([{"`). Added as section H in
  `verify.py` and as a KINSOKU section in `scans.py`; both run over ALL 8
  delivered SVGs, not just P5/P8.
- Results on the fixed render: nodes **1425**, NO_START **0**, small-kana
  line starts **0**, NO_END **0** (verify.py H + scans.py KINSOKU agree).
  A rewording that merely moved a stranded kana to another line head would
  have failed this scan; the 0 is the evidence.
- Why the first build's "kinsoku 0/1425" claim was incomplete: it counted
  punctuation closers only. The 1425-node total is unchanged (same node
  counts per page as the first build).

### 18.4 Full re-gate evidence (fixed render)

- Freeze baseline: `freeze.py baseline` on a fresh core-build copy **8/8
  byte-identical**, core SVGs re-hashed unchanged (prefixes §1 all match).
- Attribution (regenerated `tools/scratch/w45-zhtw-ja-freeze-diff-fix.json`;
  `verify.py` now reads it): A1 **0**, A2 **0**, B1 **0**, B2 **0**. The
  literal strict-CJK FAIL display is expected for a Japanese explanation
  layer; total added CJK **5992** (was 5993: P5 415→418 for による, P8
  2503→2499 for the dropped アンド・). Union test unchanged: edition CJK
  set 1029, union 1288, outside 57 (same list). Simplified-only spot hits 0.
- P8: `p8.py compare` **CLEAN, 150=150, missing=[], extra_count=0,
  keydiff=[]**; `p8.py extract` noted set **150/150** (dash style).
- Gate 10 self-run (fresh core copy + UPDATED transform ALONE + one-process
  driver, scratch `build/gate10-fix/`): transform exit 0, run exit 0 with
  zero `!!` warnings and registry 150 (A2 44 / B1 74 / B2 32), render exit 0;
  gate SVGs **8/8 byte-identical** to delivered, gate cards **8/8
  byte-identical**, gate print PDF same size 17,606,366.
- Occlusion: `occlusion_audit.py --selftest` OK; edition **0 flags**, core
  **0 flags**, NEW vs core **0**. Same-baseline ink scan edition **0**,
  core **0**; chart-graze **0/0**; border-strike **0/0**.
- P7 letter-box DIRECT measurement (not audit-0 alone): SVG box
  (1450.3, 1184.16)–(1885.7, 1762.06), last disclosure ink bottom 1753.63 →
  **8.43px clearance, fully inside**; card pixels: last ink row 1752,
  stroke row 1761 (light #d8cfb4 border) → **9px clearance, fully inside**.
  P7 teaser rect bottom 2559.36 (**20.64px** clear of the 2580 footer rule),
  last teaser ink 2528.11.
- Residual-Latin sweep: `算一算 · 計算してみよう` present on P2, P3, P5
  (1 node each); `Work it out` **0**; every other English head **0**.
- Card eyeball, all 8 (1950×2700): P5 gloss and P8 key-2 areas visually clean
  with no stranded kana; P7 teaser clear of the footer rule; no overflow,
  overlap, missing content, footer collision, or missing-glyph boxes anywhere.
- New pins (§16 updated): print PDF **17,606,366 bytes**,
  SHA-256 `2a65419a5a206153b2ca8926a6a81c03b3fa8e3a9a72afdf7617d0b62630e945`;
  web PDF **3,309,173 bytes** (< 10 MB),
  SHA-256 `eebf0102e4ad37c39a90d50fce831842b4fcae9b2e22a02bcd7d44c5394b189f`;
  SVG p5 `326b641e72cc71c816345ab891457aa6cd3ba1edb97924461727307939fbb9e9`,
  SVG p8 `d0f58c06a5f7cb6b45f9a070932d06031e16d9449ae4192a6c647c0ddccedc1e`
  (other 6 SVG pins unchanged); cards p5 1,337,283, p8 1,291,502 (others unchanged).
- Doc corrections in this round (no edition content change beyond §18.1–18.2):
  §6 trailing tag list corrected to p. 1×2, p. 2, p. 3×2, p. 4, p. 5, p. 6;
  §16 p3 pin completed to its true 64-character hash
  `aa58b266ec10b54a19197f2ba8903a2dd742d920a1c3eb4d9661f4c3a0634ce4`
  (delivered file and Gate 10 replay agree).
- Untouched per the task: badge (OLIVE, shipped precedent), footer, gloss
  counts (12), golden sentences, images, readers'-corner, P8 dash style,
  AI handling (verbatim 人工智慧＋), ABSTRACT.txt.
- NOT finalized, NOT shipped, NOT inserted, NOT posted anywhere. Awaiting a
  FULL fresh proofread; the coordinator inserts only on ZERO PROBLEMS.
