# WEEKLY-KIT — De Lucerna · 네덜란드어 주간지 VOL.3 · NL × KO

Edition slug: `2026-w46-nl-ko`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Korean. Built by the W46 NL builder; insert is the coordinator's job.

## 1. Topics and sources

Same verified fact base as the W46 NL core and the NL × EN edition (see
`files/weekly-report-w46-nl-en/WEEKLY-KIT.md` §1): Sinterklaasjournaal
from 9 Nov, national arrival Grave 14 Nov, 88th Amsterdam arrival 15 Nov,
Sint-Maarten 11 Nov, Oranje Nations League vs Greece (13 Nov) and Germany
(16 Nov preview), Heel Nederland Leest (`Het diner`, Herman Koch),
Expeditie Robinson (Sundays 20:00 RTL 4). No invented polls, quotes,
accounts or results; no squad names used. Weekdays verified
`TZ='Europe/Amsterdam'`. Sinterklaas in Korean: 신터클라스; Grave: 흐라버;
Sint-Maarten: 성 마르틴의 날.

## 2. Promises honoured (from W45 NL VOL.2)

Sinterklaas arrival Amsterdam 15 Nov and Sint-Maarten 11 Nov are the lead
topics. Readers' corner: no real letters or best page-8 texts had arrived
at press time — labelled editor's example + on-page disclosure in Dutch
and Korean (`실제 편지와 최고 작문이 없어 예시를 싣고, 약속은 VOL.4로 이어져요。`);
promise carried forward to VOL.4. No fabricated readers, letters, names
or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (연습용 데이터):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × KO measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어`
  (W45 form verbatim; clean gap before the date text, verified visually).
- Subtitle (40pt): `네덜란드어 주간지 · VOL.3 · 신터클라스 · 성 마르틴의 날 · 오라녜`.
- Pairing badge REPLACES the strapline at y=372, 19.5pt bold BRICK:
  `네덜란드어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`.
- Footer: `De Lucerna · 네덜란드어 주간지 VOL.3 · 텍스트는 네덜란드어 · 해설은 한국어`
  + `제 N 면 / 총 8 면`. Gloss prefix `해설 — ` (added by `gloss()` itself;
  bridge strings carry their own `해설 — ` prefix). Glosses: Dutch word +
  space + Korean, items joined by ` · `. P7 bridges use `;` separators and
  `:` for examples. P8 notes use ` = ` with HALF-WIDTH parentheses (),
  and `·` separators for word-order notes. P8 separator `— 제 {pg} 면 —`.
  P7 quote page tags stay Dutch `(Pagina N)`.
- P8 sizes stay at CORE values (Flow bottom 2552, separators 14pt/1.16/2,
  keys 13.5pt/1.16/0.5). `bridge()` KEPT. svglib byte-identical to the
  core svglib (SC face renders Hangul) — no svglib rep.
- Registry labels: type tokens TRANSLATED to Korean (객관식 for both
  完形单选 and 单选 — cloze-first loop order required since 单选 is a
  substring of 完形单选; 문장 완성, 단어 짝짓기, 참/거짓 판단, 문장 만들기,
  번역, 쓰기); instruction words localised (빈칸 채우기, 참 / 거짓, 문장
  만들기, 쓰기, 번역; per-direction `한국어로 번역` / `네덜란드어로 번역`,
  2× each; match instr `단어와 뜻 짝짓기`). The disclosure variable KEEPS
  the name `dt_zh` (W45 KO precedent).
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Korean. Clinic Dutch wrong/right sentences verbatim; notes in
  Korean. Translation items 137/138 re-aimed NL→KO (keys are the Korean
  translations); 139/140 prompts re-aimed KO→NL (keys stay Dutch). Book
  title `Het diner` set in 『』 corner brackets (standard Korean title
  punctuation).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Korean with Dutch `(Pagina N)` page tags kept.

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-ko-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to Korean
(`gen_ko.py`, kept at `hidden_files/w46/gen_ko.py`; 332 replacements,
FAILED: 0; the pairs file `hidden_files/w46/en-reps.txt` was re-extracted
from the shipped EN transform after a /tmp wipe — 265 pairs, exact EN
wording incl. `Translate into English/Dutch` refinements and `True:`/
`False:` forms). Freeze baseline before transform: 8/8 byte-identical,
core untouched. Transform run ONCE per fresh copy. Build: `run.py` (one
process) + `render.py` (cards + print PDF). Web PDF via `tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-KO.pdf` (11,146,265 bytes), web PDF
`De-Lucerna-VOL3-KO-web.pdf` (1,083,986 bytes, 47,853 text bytes),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-ko.text.md` (exported from
the source manuscript via `hidden_files/w46/export_text.py`, never from PDF).

## 8. Fix record (W46 KO)

- Fix 1 — writing-bridge rep gap: the loop converts 写作→쓰기 before the
  literal reps run, so the literal rep's old must be the post-loop form
  `쓰기题`, not `쓰기 문제` (the JA driver's `writing题`→`作文题` pattern
  works because the JA loop produces 作文题; the KO loop produces 쓰기题).
  Driver patched; transform FAILED: 0.
- Fix 2 — P1 BOXTITLE/TEXTX: the numbers-box title `DE WEEK IN CIJFERS ·
  숫자로 보는 이번 주` overflowed its box (ink 996.2 > border 961.0).
  Shortened to `… · 이번 주 숫자` (measured 362.4px at 22pt).
- Fix 3 — P8-keys koscan orphans: notes `주어 + 동사 + 시간` / `주어 +
  동사 + 목적어 + 장소` wrapped with 1-syllable tails ('간', '소').
  Word-order notes rewritten with `·` separators (`주어·동사·시간` etc.,
  applied to the P6 notes too, same strings); orphans gone.
- Fix 4 — P1 koscan orphan: numbers-box parenthetical `(11월 15일: 88회)`
  wrapped with `회)` alone. Shortened to `(15일: 88회)`; P2 four-word
  item `나누기: 외투 절반을 거지에게 주기` shortened to `… 거지에게`
  (orphan `기` gone).
- Fix 5 — P7 stack graze (visual check): the letters-box bottom edge sat
  on the gold rule (1985.5 vs 1937). Disclosure and invitation each
  shortened by one line; stack ends 1927.5, same as core. Crop re-checked
  clean.

## 9. Gates (2026-11-02, recorded in `hidden_files/w46/nl-gates.log`)

- Builder self-check: TOTAL 150, by page 10/18/18/18/18/18/12/38, zero
  FLOW OVERFLOW / HEAD TOO WIDE.
- `occlusion_audit.py`: selftest OK, edition 0 flags, core 0 flags,
  NEW vs core: 0.
- Same-baseline furniture scan (rowcheck.py): all 8 pages CLEAN; P6
  chart-label GRAZE coverage 0.0%; gloss counts core-vs-edition OK
  (6/5/5/5/5).
- `freeze.py diff` (non-strict; strict-CJK is inapplicable — Korean
  legitimately adds Hangul): exit 0; added CJK 3,581 chars adjudicated
  per-char — 319 Hangul syllables + 『』 title brackets, 0 Hanzi.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138]
  (legal re-aims: keys are the Korean translations).
- `koscan.py` (10–45 window): 2 ORPHAN final lines ≤1 syllable (P6
  gloss tail `가.`, P7 bridge tail `요.`) — same count as the shipped W45
  KO edition (2 orphans + 1 lead hit); 0 line-start orphan punctuation
  (W45 KO had 1). Mid-word SPLITs are accepted Korean wrapping, as in W45.
- Web PDF: 1,083,986 bytes (<7 MB), 47,853 text bytes (>0).
- Visual check: P1 viewed clean (badge replaces strapline, top-strip gap,
  numbers box fits, word gloss 1 line); P7 letters-box crop viewed
  (Fix 5 verified: clean gap above the rule).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Korean; Dutch target
text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: `리스전과 독일전. 네덜란드어 본문·한국어 해설, A2~B2 수준, 150개 연습 문제로 네덜란드 뉴스로 네덜란드어를 배웁니다.` After tail: `전. 네덜란드어 본문·한국어 해설, A2~B2 수준, 이번 주 화제를 소재로 한 150개 연습 문제로 네덜란드어를 연습합니다.`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: 0 lines (byte-identical to the pre-fix build sources).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): added CJK 3,581, 0 Han characters; exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 33922 bytes; web PDF 1083984 bytes, pdftotext 47853 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 11146265 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.
