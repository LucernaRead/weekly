# WEEKLY-KIT — Lucerna Weekly VOL.2 · JA×KO (Japanese text · Korean explanation)

**Status: builder-complete — NOT finalized. Pending independent proofread.**
No Discord delivery, no main-chat card/PDF dump, no cron, weekly-git untouched,
core and W43 directories untouched (read-only comparison).

- Pairing: target Japanese (日本語) × reader native Korean (한국어).
- Issue week: 2026-11-02 (Mon) – 2026-11-08 (Sun). VOL.2.
- Masthead: no article (article-less target language). Wordmark "Lucerna".
- Delivery: `files/weekly-report-w45-ja-ko/` — svg×8, cards×8, print PDF,
  web PDF, this KIT, `ABSTRACT.txt`.
- Build: `hidden_files/weekly-report-w45-ja-ko-build/` — `transform.py` (all fixes),
  `run.py`, `render.py`, `svglib.py` (canonical copy), `bslib4.py`, content files,
  assets, `baselines/` (per-round pre/post sha256 archives, never reset),
  `ko_scan.py` (EN×KO scan, window 10–45), `geom_round2.py` (supplemental scans),
  `audit-round1.txt` / `audit-round2.txt`, `diff-round1.json` / `diff-round2.json`,
  `occlusion-round1.json` / `occlusion-round2.json`, `geom-round2.txt`.

## 1. Spec and counts (all = W45 JA core, verified, never copied from another family)

- 150 exercises, continuous numbering 1–150.
- Levels: A2 46 / B1 75 / B2 29.
- Page distribution: P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38.
- Types: 문장 완성 50 / 객관식 51 / 빈칸 객관식 13 / 단어 짝짓기 12 /
  문장 만들기 8 / 읽기 판단 11 / 번역 4 / 쓰기 1.
- Model essay: 『私の11月の週末』, 167 characters (counted by characters),
  byte-identical to the core.
- Topics: 11月3日 Culture Day; 11月7–8 weekend autumn leaves (Naruko Gorge
  peak, Kobe Nunobiki Herb Garden light-up from 11月7日); ゆる整え食 (Ajinomoto,
  10月21日); Reading Week in progress (to 11月9日); 11月7日 立冬; Japan Series
  G1/G2 verified, G3–G7 schedule only with VOL.3 deferral printed on P4;
  10月31日 Halloween as a just-passed event.
- P6 practice chart: 近場の満足 38 / 温泉 27 / 紅葉 21 / グルメ 14 = 100,
  labeled 練習用データ · 연습용 데이터 (practice data).
- P7: A2 本と読書のことば / B1 紅葉のことば / B2 数字を読む + error clinic
  (4 items) + frame box 『ゆるく整える』 + readers' corner + VOL.3 teaser.
- P8 zones A–H; E-zone translation redirected JA↔ZH → JA↔KO (see §4).
- Golden sentences: 8 sentences, each exactly 2× in the full issue
  (whitespace-stripped count; bracketed form 1× is the article occurrence,
  expected); page tags in P7 order: p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6.
- Gloss rendered (· split): 39 total = P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4.
  Source-file grouping 13+15+11+0 is a different measure and is NOT cited as
  the rendered conclusion. Rendered survival verified: every gloss item from
  every `gloss()` call is present in the stripped text of its rendered page
  (P1 4, P2 4+5, P3 4+4, P4 4+3, P5 4+3, P6 4 — no missing items).
- P8 printed-note measure: 150 (core P8 itself prints 150 items; not the EN
  family's 78).
- Images (4, payload = core, credits from the Commons API Artist field, each
  placed): P1 maple (Poliphilo, CC0), P3 Utagawa Hiroshige III print (public
  domain), P4 stadium (Syced, CC0), P5 pumpkin (Petr Kratochvil, public
  domain). Base64 payload sha256 (first 12 hex) equal to core per page;
  P2/P6/P7/P8 have zero images, as in the core.

## 2. Furniture three-way comparison (W45 core / W43 same pairing / this edition)

W43 same pairing measured first; README #20 generalization only where W43
agrees. Measured from the rendered P1 SVG (y, pt, fill):

| Slot | W45 core | W43 JA×KO (VOL.1) | This edition |
|---|---|---|---|
| Wordmark baseline | 262, 168pt | 248, 168pt | 248, 168pt — W43 same-pairing precedent (outranks the README #20 generalization; the #20 JA-family wordmark note was written for JA×ZH-TW, not this pairing; see §8 fix round + §10 item 2) |
| Subtitle | 330 | 316, 40pt bold | 316, 40pt bold |
| Badge | — (no badge) | 356, 19pt bold, BRICK #a4553a | 356, 19pt bold, BRICK #a4553a, text verbatim = W43: `일본어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` |
| Strapline | 372 | 390, 19pt | 390, 19pt |
| Double rules | 392 / 401 | 406 / 413 | 406 / 413 |
| Dark band rect | — | 424 | 424 |
| Footer | core Chinese apparatus | `Lucerna · 일본어 주간지 VOL.1 · 텍스트는 일본어 · 해설은 한국어` | `Lucerna · 일본어 주간지 VOL.2 · 텍스트는 일본어 · 해설은 한국어` (all 8 pages) |
| Page line | `第 N 版 / 共 8 版` | `제 N 면 / 총 8 면` | `제 N 면 / 총 8 면` |
| Gloss prefix | `译注｜` | `해설 — ` | `해설 — ` |
| P8 separator | `— 第N面 —` | `— 제 N 면 —` | `— 제 N 면 —` |
| P8 answers head | core Chinese | `答え · 정답 — 면별로 나누어 실었어요. 번호를 찾으세요` | same as W43 |
| P8 right note | core Chinese | `답마다 한국어 한 줄 해설 · ✓ 표시는 모범 답안 문제예요` | same as W43 |
| Exercise head | `練習 · N版练习` | `練習 · N면 연습` | same as W43 |
| Exercise right note | core Chinese | `정답은 8면 · 레벨이 섞인 문제예요. 번호로 찾으세요` | same as W43 |
| Top center | core Japanese only | `毎週、日本語で · 매주 발행 · 日本人が読んでいる日本語を読む` | same as W43 |
| あなたは？ head | core Japanese only | `あなたは？ · 여러분은요?` | same as W43 |
| Reader prompt pattern | core Chinese | `여러분은요? … 일본어로 두 문장 써서 보내 주세요.` | same pattern (P5 wording adjusted for clean wrapping, §8) |
| Section bilingual heads | core Chinese halves | トップニュース · 헤드라인; 数字で見る今週 · 한 주의 숫자; 今すぐ練習 · 바로 연습; 短いニュース · 짧은 소식; クイズ · 번개 퀴즈; 季節のことば · 계절의 말; スポーツ · 체육; 若者・エンタメ · 청년; グラフを読もう · 그래프 읽기; ことば · 말 공부; まちがい診療所 · 실수 병원; 今週のフレーム · 이번 주의 틀; 読者の手紙 · 독자의 편지; テストと答え · 시험과 정답 | same as W43 (P4 head `スポーツ · 체육` per W43, not the core's `体育`) |
| Registry type names | core Chinese | 문장 완성 / 객관식 / 빈칸 객관식 / 단어 짝짓기 / 읽기 판단 / 문장 만들기 / 번역 / 쓰기 | same as W43 |
| Instr chips | core Chinese | 빈칸 채우기 / 장소와 날짜 짝짓기 / 행사와 장소·시간 짝짓기 / 단어와 뜻 짝짓기 / 참 / 거짓 / 문장 만들기 / 번역 / 쓰기 | same as W43 |

P1 top band same-baseline ink collision scan (venv PIL, JP faces): left
`VOL. 2 · 第2号` ends 219.8; center strapline 681.8–1268.2; right date starts
1529.9 — no collisions. Badge width 422.0, spans 764.0–1186.0, inside margins.

## 3. What changed and what did not

- Japanese main text: zero deletion. Only furniture and explanation-layer
  replacements (gloss, notes, prompts, heads, footers, E-zone keys/prompts).
- P7 word-box target-language definition sentences: frozen verbatim; only the
  gloss line under each box was localized.
- Readers' corner: Japanese example letter frozen verbatim, zero fabrication
  (no invented names, letters, or quotes). The Japanese disclosure does NOT
  serve as the operative disclosure for Korean readers; the Korean disclosure
  below replaces both the Japanese and Chinese disclosures (single disclosure,
  `lh` recomputed from the Korean text):
  `편집부의 예시 편지예요, 실제 편지가 아니에요. 마감까지 실제 편지도 8면의
  우수 작품도 도착하지 않았어요. 둘 다 VOL.3에 실을게요. 여러분의 편지를
  일본어로 보내 주세요 — 뽑힌 편지는 VOL.3에 실어요!`
  It carries all 3 facts (example is not a real letter; no real letters
  arrived; no best P8 compositions arrived) + an explicit imperative
  invitation + a VOL.3 promise. The teaser line is NOT counted as the
  invitation. Best-P8-composition scope is adjudicated by submission category
  overall, distinct from the VOL.2 writing preview.
- P2/P3/P5 あなたは？ boxes: the `eh` height formula wraps the reader-language
  literal itself, so the transform replaces that literal in BOTH the `eh`
  call and the printed paragraph (intentional deviation from JA×EN, which
  left `eh` on the Chinese string — keeps box height honest for the Korean
  line count).
- P1 trend box: fixed-position single lines; the Korean band-right line was
  shortened to `날짜는 기사 참조 · 정확한 통계 아님` (verified on the P1 card:
  fits inside the box, no overflow).
- P8 typography: dash style (`N. key — note`) kept exactly as the core.

## 4. P8 comparison (explicit dual-path `p8.py`, `--total 150`)

- `p8.py compare` (explicit `--core-p8` / `--edition-p8` paths; the directory
  form fails because tables.json maps the ko target to `p8-siheom.svg`):
  status CLEAN, core 150 noted = edition 150 noted, missing = [], extra = 0.
- Keydiff (round 2): [1, 2, 7, 8, 9, 29, 32, 65, 69, 78, 113, 115, 117, 118,
  137, 138, 140, 146, 147] — 19 items.
  Adjudication: **19 = 2 true redirections + 1 prompt localization inside
  keydiff + 16 extraction artifacts** (paren-branch folding of translated
  note stems into extracted keys; the true printed keys are byte-identical).
  Prompt localizations total **2**: #139 (outside keydiff) and #140 (inside
  keydiff). #140 must NOT be double-counted — "2+19" style counting is wrong.
- True key changes, only #137 and #138:
  - #137: `文化日是11月3日。` → `문화의 날은 11월 3일이에요.`
  - #138: `乱扔垃圾，要罚2,000日元。` → `쓰레기를 버리면 벌금 2,000엔이에요.`
- #139: key identical; note `对照第7版` → `7면 참조`.
- #140: key identical (Japanese); note `对照第6版（神户的灯光秀）` →
  `6면 참조(고베 라이트업)`.
- #150: writing-apparatus NOTE change only (`✓ 范文见本版 H 区（167 字）` →
  `✓ 모범 답안은 이 면 H 구역에 있어요(167자)`), not a key change, not in keydiff.
- P8 note completeness (dual-path audit, wrapped-joined, whitespace-stripped):
  items 150 = 150, missing/extra none; fully identical P8 lines (raw join,
  footer y≥2580 excluded) = [] — no pass-through Chinese note survives.
  (Round-1 false flag on #92 was a whitespace artifact: `38+27=65` vs
  `38 + 27 = 65` spacing localization, raw strings differ, not a pass-through;
  footer text swallowed into #150 was fixed by the y≥2580 exclusion.)
- JA-family P8 #37 bare-string trap — CHECKED AND MAPPED: core
  `content34.py:82` registers #37's prompt as the bare string `工艺展到11月8日`
  (no weekday suffix; P3 fill-in item, key 8). It is NOT the suffixed NOTES
  entry `工艺展到11月8日（周日）` and NOT `传统工艺展到11月8日`. The transform
  maps the bare string explicitly → `전시는 11월 8일까지예요`. Verified on the
  rendered P8: `37. 8 — 전시는 11월 8일까지예요`. The Sunday fact is verified
  (2026-11-08 is a Sunday in Asia/Tokyo; P3 stem: 展覧会は11月 ___ 日（日）
  までです。) but the bare note itself carries no weekday, mirroring the
  JA×EN fix-5 rendering.

## 5. Geometry

- Canonical `tools/occlusion_audit.py`: selftest OK (all 6 classes fire once,
  clean controls silent); edition 0 flags, core 0 flags, NEW vs core 0
  (round 1 and round 2 identical).
- ADVANCE-method full-page right-edge scan (venv PIL, every text element,
  limit x=1885.5): edition 0 violations, core 0.
- Full-page frame-line scan (supplemental; canonical audit does not catch
  frame lines pressing text): 1 flag, IDENTICAL in core and edition — P2 line
  y=1804 vs text baseline y=1800 (`文で覚えましょう：『ゆる整え食で、体を
  整えましょう。』`). Adjudicated FALSE POSITIVE: baseline-anchored PIL ink
  box for that string is [1781.55, 1802.05]; the line at 1804 clears the ink
  bottom by ~2px. Inherited core geometry, not edition-introduced; canonical
  audit reports 0 LINEX for the same pair.
- P6 chart-label ink coverage, baseline-anchored ink method (NOT getbbox):
  max label ink coverage 0.000 for both edition and core — well under 30%.
- Kinsoku line-start scan (canonical NO_START set): edition 0 hits, core 0.
- P7 teaser: rect ends 2442.08 (< 2540); core teaser rect ends 2512.
- P8 answer flow: final-column cursor 2366; max answer baseline 2514.92
  (< 2540; = core — the earlier KIT figure 2530.35 was a round-1 stale
  value; round-2 audit and the independent proofread both measure
  2514.92, identical to the core).
- Build log: 0 FLOW OVERFLOW / HEAD TOO WIDE (both rounds).
- Inherited maxima (frozen Japanese exercise lines, byte-identical to core,
  not edition-introduced; the <2540 gates apply specifically to the P7 teaser
  end and the P8 answer-flow end): P1 2449.45, P2 2538.9, P3 2497.675,
  P4 2555.85, P5 2551.4, P6 2539.975 — all byte-identical to the core.

## 6. Korean scan (window 10–45, all prose columns)

- Round 2: S1 (line-start orphan punctuation) 0; S3 (corpus-verified mid-word
  split, ≥3-syllable tail, incl. paren-fragment coverage) 0; S4 (tight-leading
  gap 10–20 with ≤2 syllables) 0. The retired "first segment ≤1 syllable"
  criterion was not used.
- Round 2 S2: 1 — P6 y=493.225 gloss continuation `いかける 쫓다.` (gloss
  `予算 예산 · 満足 만족 · 観測 관측 · 追いかける 쫓다.`; the core wraps the
  same gloss box to 2 lines with the full headword on line 2). Adjudicated
  NON-DEFECT, left for the independent proofreader to re-check: the Korean
  gloss word `쫓다` is complete (2 syllables, not a fragment); the Japanese
  headword split 追|いかける is normal per-character CJK wrapping; the gate
  standard is ≥3-syllable tails + line-start punctuation 0, and this is
  neither (2-syllable complete-word tail, no line-start punctuation).
  Deliberately not distorted to chase the heuristic.
- G flags (gloss continuations starting with `·`: P1 y=887.025, P2 y=1171.205
  and y=607.225, P5 y=1854.5) are family format, not defects. L flags
  (standalone instr `번역`×4, `쓰기`×1 on P8) are by design, not defects.
- P8 answer flow checked line by line (dual-path audit, §4) and confirmed on
  the P8 card: all 150 lines present, no overflow, footer line clear.

## 7. Residue and apparatus checks

- Freeze: core baseline 8/8 byte-identical; shipped core SVGs unchanged on
  re-hash (hashes match `baselines/core-pre.txt`; re-verified at close-out).
- `freeze.py diff` (round 2): P7 +38/−40, P8 +179/−178 strings; total added
  CJK characters 3118, all Hangul except one 「 and one 」 (Korean notes
  citing Japanese quoted words — adjudicated legitimate; bracket-added
  strings: P7 clinic notes citing 「昨日」「こと」「で」「か所」, phrase note
  citing 「ゆる」, P8 notes citing 「静かだけど、冒険中。」, 「紅葉の本」,
  and the Korean quotation 「4번 이기는 싸움」).
- Removed-string audit: every removed string explained — furniture/footer
  rendered f-string forms (`第 N 版 / 共 8 版`, separators `— 第N面 —`),
  gloss fragments (rendered `译注｜…` lines; the prefix old value is a code
  fragment), P7 phrase translations combined with their tags, P8 key+note
  lines (note parts are old notes, proven by the dual-path P8 comparison).
  No Japanese prose removed.
- Old-string leak sweep (every transform old string against edition SVG
  lines, adjudicated against the same page's core lines): 0 leaks.
- Han/punct inventories (all-page SVG text): core Han 5410 → edition 3424;
  edition Han charset ⊆ core charset (no new Han characters); removed Han
  characters are Chinese apparatus characters. 。 core 383 → edition 343
  (Δ−40 = removed Chinese note punctuation; remaining 343 all frozen
  Japanese). （） core 260 → edition 214 (Δ−46; remaining all frozen
  Japanese). ｜ core 10 → edition 0 (gloss prefix `译注｜`×10 replaced by
  `해설 — `). Half-width () core 44 → edition 90 (Korean weekday/reading
  parens + frozen). Note: the EN×KO precedent shorthand (。 0 / （） 0 /
  ｜ as core-inherited separator) does NOT transfer to JA×KO — Japanese body
  text legitimately uses full-width punctuation; the measured values above
  are this edition's precise statement.
- Han-bearing edition strings absent from the core were all adjudicated as
  Korean furniture/gloss/note strings citing Japanese headwords (祝日, 見頃,
  暦, 市場, 工芸, 陶器, 漆器, 染物, 金箔, 延長, 逆転, 同点, 優勝率, 総括,
  締め切り, 罰金, 像, 仮装, 守る, 祭り, 週末, 話題, 予算, 満足, 観測,
  追いかける, etc.) or Japanese furniture text — no Chinese words.
- Word-level Chinese residue rescan: the leak sweep above is word-level
  (old strings, not single characters); character scanning alone was not
  relied on.
- SOP-dropped-term gate (the two-character Chinese term for intermediary
  explanation-linking, named as dropped in SOP §3; its original form is
  deliberately not written anywhere in this KIT, in `transform.py`, or in
  `ABSTRACT.txt`): count 0 in edition SVG + build code + ABSTRACT. Verified
  by a one-off grep (not saved to any file). Note: `transform.py` legitimately
  contains core Chinese source strings as replacement keys (sibling
  precedent, disclosed here) — that is not a violation of this gate.
- svglib: canonical md5 `d73e23b365676c3618d7e060b835eb4d` verified;
  kinsoku + SEAM_SLACK=28; the canonical file was never edited (build copy
  md5 = canonical md5). For this JA×KO build the canonical JA svglib is used
  verbatim (Japanese is the body language).

## 8. Fix rounds (all fixes into `transform.py` only; baselines archived per round)

- Round 1: transform passed all asserts on the first run. Gates passed
  except two Korean-scan findings (below). Round-1 post hashes in
  `baselines/round1-post.txt`; round-2 pre hashes in `baselines/round2-pre.txt`
  (identical to round-1 post — nothing changed between rounds except the two
  fixes below). Round-1 baselines were never reset or overwritten.
- Round-1 finding S1 (real defect): P5 reader prompt wrapped as
  `여러분은요? 가을 축제에서 무엇을 하고 싶어요` / `? 일본어로 두 문장 써서
  보내 주세요.` — the second `?` stranded at line start (wrap tokenizes `?`
  as a separate Latin token). Fix: wording changed to
  `여러분은요? 이번 가을 축제에서 무엇을 하고 싶어요? 일본어로 두 문장 써서
  보내 주세요.` — verified with `svglib.wrap` (sans 20, width 390) to break
  CLEAN at a space (line 1 ends `하고`, line 2 starts `싶어요?`), and
  confirmed on the round-2 P5 card. P2/P3 prompts were not flagged and were
  not changed. Rejected candidates (all failed S1 or S3): `…하고 싶은 것을/
  일을 일본어로 두 문장 써 주세요.` (mid-word tail `본어로`, 3 syllables);
  `…하고 싶나요? …` (break before `?`); `…써서 보내 주세요!` (tail
  `본어로`, 3 syllables); `…일은 무엇인가요? …` (tail `엇인가요?`, 4
  syllables); `…것을 알려 주세요. …` (mid-word 알|려 — passes the gates but
  is a worse break than the chosen CLEAN break).
- Round-1 finding S4 (lone tail line): P8 #88 wrapped as
  `88. 近場の満足 — 그래프에서 가장 인기 있는 것은 가까운 곳에서의 만족이` /
  `에요` (2-syllable tail — passes S3 but a lone tail line). Fix: note
  shortened to `그래프 1위는 가까운 곳에서의 만족이에요` — verified with
  serif 13.3 wrap (P8 answers render in serif; an earlier sans test gave a
  misleading break) to render on ONE line, and confirmed on the round-2 P8
  card: `88. 近場の満足 — 그래프 1위는 가까운 곳에서의 만족이에요`. Meaning
  preserved (the chart's No. 1 is nearby satisfaction). Only P8 rendering
  changed (notes print only on P8; the P6 stem is unaffected; registry key
  近場の満足 unchanged).
- Round 2 changed files only: P5/P8 SVGs, P5/P8 cards, both PDFs. All other
  pages byte-identical to round 1.
- Fix round (wordmark, post-proof B-1): P1 wordmark baseline 262 → 248
  ONLY, in `transform.py` (new PER_FILE replacement in `content12.py` +
  docstring correction); subtitle 316, badge 356, slogan 390, rules
  406/413, band 424 verified already at W43 positions and NOT moved.
  Rebuilt via `transform.py` → one-process `run.py` → `render.py`
  (tools/venv/bin/python). Pre-fix baseline archived in
  `hidden_files/weekly-report-w45-ja-ko-build/fix-round-wordmark.sha256`
  (18 deliverables + build files; post-render hashes appended in the
  same file, never reset). Changed deliverables, exactly: P1 SVG, P1
  card, both PDFs; the other 7 pages' SVGs/cards byte-identical to
  pre-fix (verified against the pre-fix baseline). Gates re-run after
  the fix: freeze core baseline 8/8; P8 CLEAN 150 = 150 (explicit
  dual-path, keydiff unchanged, 19 items); occlusion edition 0 / core 0
  / NEW vs core 0 (selftest OK); Korean scan window 10–45: S1 0, S2 1
  (same adjudicated P6 gloss non-defect), S3 0, S4 0; wordmark→subtitle
  ink gap 28.75px by canonical `occlusion_audit.ink_box` (wordmark ink
  bottom 253.0, subtitle ink top 281.75; proof's quoted 29.25px differs
  by 0.5px of subtitle-top measurement, gap positive, no collision);
  P1 card visually clean (wordmark/subtitle/badge/slogan/rules/band
  relative positions correct). KIT-only text corrections in this round
  (§2 wordmark row, §5 P8 max baseline 2514.92, §10 item 2) touched no
  SVG/card/PDF — post-KIT-edit PDF hashes re-verified identical to the
  post-render baseline. Status remains builder-complete, NOT finalized:
  per SOP §8.4 a fresh full independent proofread is still required.

## 9. Visual inspection

All 8 cards viewed individually (P1–P8): no overflow, overlap, or clipping.
Spot-checked in particular: P1 masthead/badge/trend box, P2 season-words
strip and the 1804 rule (clear of the model sentence, §5), P3 Hiroshige
print and #37 stem, P4 schedule box and 73% box, P5 fixed prompt box,
P6 gloss box and chart bars, P7 letters box + teaser band, P8 #37/#88/#92/
#137–#140/#150 lines and the answer-flow end.

## 10. W43 same-pairing deviations (W43 JA×KO VOL.1 → this edition VOL.2)

1. Volume: VOL.1 → VOL.2 (footer, P1 top line, masthead subtitle).
2. Wordmark baseline: W43 248 → this edition 248 (= W43 same-pairing
   precedent; the earlier 262 followed the README #20 generalization,
   which does NOT override this pairing's own shipped precedent — the
   #20 JA-family wordmark note was written for JA×ZH-TW. Corrected in
   the §8 wordmark fix round; all furniture slots now match W43 exactly
   — 248/316/356/390/406/413/424).
3. Exercise mix follows the W45 core (A2 46 / B1 75 / B2 29, 150 total),
   not any W43 mix.
4. Writing model: W45 『私の11月の週末』 167 characters (W43 was
   『私の秋の週末』 150 characters).
5. P8 typography follows the W45 core dash style.
6. Readers' corner follows the W45 honest-disclosure situation (no real
   letters / no best P8 compositions by press time, promise carried to
   VOL.3); the Korean disclosure text is new for this issue's situation.
7. Phrase page tags: p.N (W45 JA-family convention per the task fixed spec;
   W43 JA×KO used (N면) tags).
8. Content, topics, figures, and promises are all W45 core — no W43 fact,
   figure, or sentence carried over.
9. Badge string verbatim = W43; badge color BRICK #a4553a per W43 measurement
   (JA×EN/JA×FR used OLIVE — not followed here).
10. P4 head `スポーツ · 체육` per W43 (core's `体育` not used).

## 11. Reproduction

- `transform.py` (asserts: every GLOBAL source occurs in ≥1 core file; every
  NOTE key occurs as an exact quoted string; post-run: no GLOBAL source
  survives, no NOTE key remains as an exact quoted string) →
  one-process `run.py` → `render.py`.
- Interpreters: `run.py` — `tools/venv/bin/python` (Python 3.12.3, PIL
  13.0.0). `render.py` — `tools/venv/bin/python` (Python 3.12.3, PIL 13.0.0;
  venv required because system python3 has no cairosvg). System python3
  (3.12.3, PIL 10.2.0) was NOT used for either. Audit measurements use venv
  PIL. `run.py` byte-reproduces the family baseline SVG (freeze baseline
  8/8 byte-identical) except for intended changes.
- `tools/freeze.py baseline` scratch: `tools/scratch/baseline-w45-ja-ko/`
  (shared scratch not cleaned).
- Never run a build-tree script in place that writes SVG back into the
  delivery or core directory; registration expansions were copied to scratch
  with OUT redirected.

## 12. For the independent proofreader

- Re-check the P6 gloss S2 adjudication (§6) and the P2 1804-rule clearance
  (§5) — both are adjudicated non-defects with reasoning above, not hidden.
- Re-check P8 #139/#140 attribution (§4) and the #37 bare-note mapping (§4).
- Re-check that no P8 note is a pass-through (dual-path audit says 0
  identical lines; the #92 spacing case is documented in §4).
- Inherited P4/P5 maxima (§5) are core geometry, not edition defects.
