# WEEKLY-KIT — Lucerna Korean Weekly VOL.3 · Korean × Dutch (2026-W46)

Pairing: Korean text, Dutch explanations. Edition slug: `2026-w46-ko-nl`.
Week: Mon 9 Nov – Sun 15 Nov 2026 (weekStart 2026-11-09, weekEnd 2026-11-15).
VOL: VOL.3. Lead: 「김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날」.

## Build method

- Core text frozen from the W46 Korean core build
  (`hidden_files/weekly-report-w46-ko-build/`); only the explanation layer rewritten.
- Build dir: `hidden_files/weekly-report-w46-ko-nl-build/` — copied from the W45
  ko-nl build (`.py` + `assets/` only), content files overwritten with the frozen
  W46 core content, nl `bslib4.py`/`svglib.py` kept (furniture, `Uitleg — ` gloss
  prefix).
- Transform: filtered W45 operations (harvested `apply_pairs` in `main()`) applied
  first, then `supp_nl.py` (GEOM majority form + 175-string SUPP map — verified by
  set-diff to be the same string set as pt — incl. native type labels, longest-first).
- P1 geometry: majority form — 20pt BRICK badge at y=394, subtitle shifted to 366,
  rules 412/421, dark band 433. Badge:
  `TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`.
  Footer: `Lucerna · KOREAANS WEEKBLAD VOL.3 · TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS`
  / `Pagina N van 8`. Strapline second segment: `Elke week`.
- Right-band line 1 `KIMJANG`; line 2:
  `Kimjangseizoen in volle gang · Nog een week tot het examen`.
- Phrases pitch 124→112 (patched directly in `content7.py`; GEOM scope is P1 only).
- P8 separator edited in W45 to `— Pagina {pg} —` (kept via W45 ops).
- Letters: Korean `lko` kept; `lcn` = `Voorbeeldbrief van de redactie, geen echte
  brief.`; `lcn2` = short Dutch disclosure + solicitation carrying the promise to
  VOL.4 — editor's example + disclosure + solicitation. No real letters arrived;
  nothing fabricated.
- E-zone (P8): W45 precedent — items 137/138 keys become Dutch, 139/140 stems
  become Dutch, keys stay Korean (p8 keydiff [137, 138], expected).
- Type labels in Dutch (deliberate deviation from W45, where nl kept Chinese
  labels; verified against the build sources): 完成句子→`Vul de zin in`,
  单选→`Meerkeuze`, 词汇配对→`Koppel paren`, 完形单选→`Invuloefening`,
  造句→`Bouw zinnen`, 句型转换→`Herschrijf`, 判断→`Juist of onjuist`,
  翻译→`Vertaal`, 写作→`Schrijf`, 填空→`Vul in` — the family's own W45
  instruction vocabulary.

## Contents / counts

8 pages, 150 exercises (registry count): A2 51 / B1 72 / B2 27;
pages 10/18/18/18/18/18/12/38. P8 writing model 158 chars (spaces removed),
inside the printed 150–200자 instruction. P7 golden sentences 8/8 verbatim
from this issue's own articles (whitespace-insensitive, checked against SVGs).

## Gates (2026-11-02)

- `run.py`: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE; P7 teaser ends 2528.7 (<2540).
- `occlusion_audit.py`: selftest OK; final 0 flags (after the P2 box-title fix below).
- `p8.py compare` (core vs nl): CLEAN, missing=[] extra_count=0,
  keydiff=[137, 138] (expected E-zone re-aiming). Extract 150/150.
- `freeze.py diff`: 0 added CJK chars on every page (Latin script; no Hangul added).
- `check_edition.py`: phrases 8/8; orphan scan 1 hit, adjudicated — P4 SHORT-TAIL
  `않아요.` at y=1873, byte-identical wrap in the frozen core SVG (same coordinates);
  the 3-syllable verb-ending tail is the natural wrap point of the frozen stem.
  Kinsoku line-starts 0.
- Letters-box audit (manual): disclosure inside its box, margin +9px.
- Visual: P7 card read — letters box, phrases pitch, teaser clean.
- Full CJK-literal scan after SUPP: only the adjudicated Hanja paragraph remains.

## Fixes during this build

1. P2 box-title TEXTX collision: `김장 장보기 목록 · Boodschappenlijst voor de kimjang`
   overlapped the exercise below (117.5×15.8px, the largest of this defect class) →
   shortened to `김장 장보기 목록 · Boodschappenlijst` in `content12.py` +
   `supp_nl.py`; re-audit 0 flags.
2. P8-keys FLOW OVERFLOW (item 147 note wrapped to 2 lines): the same Chinese
   source string `定期报名11月10日17点截止` serves two roles — the P2 note and the
   P8 key note — and SUPP translated both to the long Dutch form
   `De gewone inschrijving sluit op 10 november om 17.00 uur`. Fixed by unifying
   BOTH occurrences to the short form `Sluiting inschrijving: 10 november, 17.00 uur`
   in `content12.py`, `content8.py`, and `supp_nl.py`. SUPP replaces all
   occurrences in all five content files — one string, one translation everywhere
   (factory lesson recorded).

## Outputs

- `svg/` (8), `cards/` (8)
- Print: `Lucerna-VOL3-NL.pdf` — 32,464,310 bytes,
  SHA-256 `1a3cab8516174866ab7a6b60f7ee3ea55c4a1712377626a5bf0f8bd779d1b855`
- Web: `Lucerna-VOL3-NL-web.pdf` (via `tools/webpdf.py`) — 2,291,082 bytes (<7 MB),
  pdftotext 53,187 bytes, phrase 「김장이 한창이에요」 found 7 times, consistent
  with print text. SHA-256 `6eddae1d206298f51cc683e0ead695ea0f4baa92fdefaa1fca96f84bad542f0f`
- `ABSTRACT.txt` (Dutch, single line, no ASCII double quotes)
- `2026-w46-ko-nl.text.md` — 338 items, 8 pages, exported from the source
  manuscript via `textmd.py` (never from PDF); answer keys/notes excluded.

## Debts / open items

- Korean Series G1–G5 results unknown at the 2 Nov 2026 press time; G6/G7
  (10–11 Nov) conditional. No observed foliage peak for Naejangsan/Wolchulsan at
  press time (forecasts only, attributed by agency). HanNeungGeom details from
  secondaries citing the 19 Oct 2026 notice; cancelled-seat start time conflicts
  across secondaries (dates only printed). No independent reproof round run.
- Image shortfall (carried from W45): no verified PD/CC0 kimjang-making or Korean
  foliage photo; only the verified W45 file set reused with honest captions.
- W45 teaser honoured in full (kimjang / CSAT D-7 / HanNeungGeom / playoffs +
  Korean Series / letters + best P8 writing). VOL.4 teaser printed on P7.

## Fix record — Round 1 proofreader verdict (fix worker, 2026-11-03)

Source-only fixes for the independent proofreader's Round 1 defects (verdict: `hidden_files/w46/ko-proofread-gates/proofreader-verdict-round1.md`); full re-render from source, no hand-edited SVG/PDF. Observations O1–O8 untouched. A Round 2 independent proofread follows; re-gating does not replace it.

- D2 (BLOCKING, frozen core, all 11 editions): P3 gloss line under the "당신은?" prompt. The `가늘다` entry was DELETED from the gloss line in `content34.py` (and mirrored in the `supp_*.py` record pair; core `check_core.py` hand list updated the same way). Before: `겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen` After: `겹치다 = samenvallen · 감사하다 = bedanken · 나누다 = onderscheiden, delen` Post-fix verification: `가늘` occurs 0 times in all 8 SVGs and in `2026-w46-ko-nl.text.md` of every edition; remaining gloss entries intact and correctly punctuated; P3 visually checked at full frame in all 11 editions (shortened gloss inside its box, no overflow/overlap). SVG hash comparison vs the pre-fix inventory: only `p3-munhwa.svg` changed in this edition (zh-tw: P3 + P6).
- ⚠️ DISCREPANCY FLAG for the coordinator / Round 2 proofreader (do not treat the D2 deletion as proof the stem never occurs): pre-fix verification found the attributive inflection `가늰` (가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is False at codepoint level) 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는` and P5 ×2 (body + exercise stem) — which the verdict's stem list (가는, 가늘게, 가느다란, 얇) did not cover. The prescribed deletion was applied exactly as ordered; post-fix `가늰` remains 3× per edition. Adjudication of keep-vs-restore belongs to Round 2.

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 0 (ja 2,662 vs Round 1's 2,664 — the −2 is the deleted gloss entry leaving the core multiset: 3 Hangul syllables + 细; pt +8 Hangul = the adjudicated quoted sentence; zh-tw 903 unchanged: P6 `規` +1, P3 `細` −1).
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 (identical to Round 1). Kinsoku: 0. Koscan reconstruction: CANDIDATES=293 TRUE_SPLITS=0 S3=0 (reconstruction script preserved at `hidden_files/w46/ko-fix/koscan_reconstruct.py`; the Round 1 koscan script itself was not preserved, only its logs).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-NL-web.pdf` 2290981 bytes (< 7 MB), 8 pages, pdftotext 53168 bytes. `Lucerna-VOL3-NL.pdf` 32464167 bytes, 8 pages. `2026-w46-ko-nl.text.md` regenerated from the source manuscript via `textmd.py` (headers byte-identical to pre-fix, 338 items, 28089 bytes; diff vs pre-fix export is only the fixed gloss line(s)).

## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `Uitleg — 겹치다 = samenvallen · 감사하다 = bedanken · 나누다 = onderscheiden, delen`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen`
  - This resolves the Round 1 discrepancy flag in this KIT: the stem DOES occur (as inflected `가늰`); the entry is restored, not deleted.
- D3 — item 54 (P4), stem fix at the core source, key UNCHANGED (`밀렸어요`).
  - Before: `한국시리즈 시작이 하루 ___어요.` → reconstructed `하루 밀렸어요어요` (doubled ending).
  - After: `한국시리즈 시작이 하루 ___.` → reconstructed `한국시리즈 시작이 하루 밀렸어요.` (verified in all 11 renderings).
- D4 — item 103 (P7), stem fix at the core source, key UNCHANGED (`절임배추`).
  - Before: `미리 소금에 절인 배추를 ___이라고 해요.` (ungrammatical: `배추` is vowel-final, quotative must be `라고`).
  - After: `미리 소금에 절인 배추를 ___라고 해요.` → reconstructed `미리 소금에 절인 배추를 절임배추라고 해요.` (verified in all 11 renderings; contrast item 101 `김장이라고`, batchim-final, unchanged).
- Same-class sweep (AST text-read of the build sources, `sweep.py`): all 77 fill-in stems scanned for stem+key doubling — exactly 1 candidate (item 54); all quotative `이라고/라고` usages scanned for final-syllable mismatch — exactly 1 mismatch (item 103) among 3 quotative stems, plus 4 correct prose usages and 1 non-applicable (`'D-7'이라고`, non-Hangul token) reported unscanned-as-defect for Round 3 adjudication. No further candidates; nothing else fixed.
- Keys UNCHANGED: p8.py compare CLEAN 150/150, keydiff [137, 138]; per-edition key-extraction JSONs byte-identical pre-fix vs post-fix (all 150 keys, noted sets identical; keys 54 `밀렸어요` and 103 `절임배추` unchanged everywhere).

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix-round3/gates/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 0. No U+FFFD.
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES=358 TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-NL-web.pdf` 2291086 bytes (< 7 MB), 8 pages, pdftotext 53178 bytes. `Lucerna-VOL3-NL.pdf` 32464313 bytes, 8 pages, pdftotext 53178 bytes. `2026-w46-ko-nl.text.md` regenerated via `textmd.py` (headers byte-identical to pre-fix, 338 items, 28108 bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.

## 补记：D5 字体重建（2026-11-15）

- 安装：移植模板 `tools/mechanism-w47/svglib-ko-d5.py` 原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`（读者 nl）；D1 fix 与 §1.1 样式一次做完（生产 svglib 为 pre-D1 旧样式，D1 fix 0 处、Newsreader 0 处）。
- 路由单元测试 `test_d5_routing.py`：FAILURES: 0。fix2（U+201C/U+201D/U+2019 → Newsreader）保留，`_QUOTE_CLS` 在位。
- 基线普查（`d5_census.py`，修前）：见 builder 报告 §0.4；重建后拉丁/西里尔/弯引号 in CJK 均为 0。
- 修复（只降字号，不改文案）：
- A: P1-headline 流 6×f.para 24→22（行40–45，ja 行39–44）+ 6×f.ex 19.5→18.5 + f.head 25→24: `content12.py:40` para 24 / ex 19.5 / head 25 → para 22 / ex 18.5 / head 24 (over FLOW OVERFLOW need 99px（流止 y=1942，底 1828）; probe margin run2 流止 y=1249，余 579px；G6 7 旗标同清)
- 终轮门禁 run2：18/19（fr 17/19）。唯一未过项 G15a 系模板 SOP §1.1 空白线渲染所致 pdfdiff（仅 `_` 字符缺失，见 builder 报告 §0.5 与 §10）；fr 另有 G2 门禁计数含冻结基线日志 1 项，交付侧为 0（G1 HEAD 0 佐证，见 §10）。G15b 仅记录（D27）。creambox defects 0，ratios n=400 med=1.007，P8 行数 227→228，页脚余量 59.9→59.9px。
- 交付物（run2 实测，builder 原件）：
  - 印 PDF `Lucerna-VOL3-NL.pdf` — 30531643 bytes, SHA-256 `f70a5afd5cc88cb21979fd68e4f5c26952c4db837787e2403afee5c1371b1f36`
  - 网 PDF（render）`Lucerna-VOL3-NL-web.pdf` — 2146787 bytes, SHA-256 `1cfd76b81a9da304b30eca6c7ee35995d238aaef60921b7ead60def0598aea53`
  - 网 PDF（builder）`2026-w46-ko-nl.web.pdf` — 2146777 bytes, SHA-256 `bc3ac3ce84dd99b275e9b0bc7f2163c9c02b5646a13e408234c7624ac0b869b6`
  - text.md `2026-w46-ko-nl.text.md.new` — 27897 bytes, SHA-256 `dafd27b0fb7b748c58521151d0397f2f5810a895861b73d9adb900d5aedd9cea`（与 fanout `.text.md.new` 逐字节相同；原生校验器 ADOPT）
- 本 build 取代旧交付物行（旧印/网 pin 已过期，见 builder 报告 §9）。
