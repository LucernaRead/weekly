# WEEKLY-KIT — La Lucerna · W45 IT×KO (VOL.2)

Issue week: **Mon 2 – Sun 8 November 2026**. Issue dated **Mon 2 November 2026**.
Edition: **Italian text × Korean explanations** (target IT, native KO).
Status: **builder-complete, NOT finalized — awaiting independent proofread.**
No Discord post, no card/PDF dump into main chat, no cron, no weekly-git
touch, no edit to the core or W43 directories — this build only.

## 1. Spec

- 8 pages, 1950×2700, warm ivory paper, dark olive-green accents,
  blackletter masthead **La Lucerna** (core's masthead; target is Italian).
- Only the explanation layer was rewritten, directly into Korean
  (해요체) for Korean-native readers. All Italian body text is frozen,
  word for word.
- The explanation layer contains no Han characters at all in the
  rendered edition (SVG Han = 0 on all 8 pages, see §2/§8); the layer is
  Korean notes (prefix `해설 — `).
- No invented reader letters, names, or quotations: the P7 readers' box
  keeps the core's Italian example letter, labelled as an editors' example
  (see §5).
- The banned intermediary term occurs **0** times in every deliverable
  (SVG text, KIT, ABSTRACT) and in the build code.
- 150 exercises, continuously numbered 1–150; levels A2 47 · B1 70 ·
  B2 33 (identical to the core). Per page: P1 10 · P2 18 · P3 18 · P4 18 ·
  P5 18 · P6 18 · P7 12 · P8 38 (identical to the core).
- By type (registry, unchanged in structure from the core; type tokens
  localised to Korean, never printed in Chinese): 문장 완성 61 ·
  객관식 48 · 빈칸 채우기 13 · 문장 만들기 7 · 단어 짝짓기 12 exercises
  (3 match sets) · 읽기 판단 3 · 문장 전환 1 · 번역 4 · 쓰기 1.
- Writing model text (§H): 81 words, Italian, byte-identical to the core
  (see §9).

## 2. Freeze check (tools/freeze.py)

- Baseline first, before any edit: `freeze.py baseline` on the W45 IT core
  build reproduced **8/8 SVGs byte-identical**, and the shipped core SVGs
  re-hashed unchanged afterwards. Core hashes re-verified at the end of
  this build, still identical (p1 81051bbb…, p2 d42ce9ae…, p3 9e45586d…,
  p4 62f75269…, p5 c907b869…, p6 5545f8dd…, p7 9fc999f4…, p8 3b87e54f…).
- Final diff (core vs this edition, R2 SVGs): per page added/removed
  text-node strings p1 +27/−26, p2 +31/−29, p3 +31/−31, p4 +27/−25,
  p5 +38/−35, p6 +26/−24, p7 +42/−41, p8 +177/−174; **added Han = 0** on
  every page; added CJK total 3274, **100 % Hangul syllables**
  (322 distinct, all in U+AC00–U+D7A3).
- Removed strings containing no Han characters, adjudicated (all other
  removed strings carry explanation-layer Chinese):
  - p6: 1 wrap fragment (`bollettino · modello`) — the words are present
    in the edition, re-wrapped across different line breaks.
  - p7: 1 wrap fragment (`è probabile che / è possibile che / bisogna`)
    — same re-wrap cause.
  - p8: 7 lines differing only in punctuation form (full-width Chinese
    colon `：` → ASCII `:` and full-width parens `（）` → half-width
    `()` in the Korean notes, e.g. `103. nevica — nevicare：nevica` →
    `103. nevica — nevicare: nevica`); content identical.
  - p8: 8 separators `— PAGINA n —` → `— 제 n 면 —` (furniture, §3).
- No Italian body string was removed. Images byte-identical per page
  (same base64 assets as the core); credit lines identical (Italian).

## 3. Furniture — W43 shipped IT×KO wins verbatim

Measured from the shipped W43 SVG, copied exactly (VOL.2 follows the W45
core; everything else identical to W43 IT×KO):

- **Badge adjudication — NO inserted badge line** (W43 IT×KO's own
  adjudication, proofreader-accepted): the y=372 slot carries the frozen
  Italian tagline (`IL GIORNALE SETTIMANALE PER IMPARARE — …`), and the
  only other gap (band bottom 542 → headline head 606) is the headline
  section's own lead-in. Pairing is carried visibly by the top strip,
  serif line and footer on all 8 pages.
- P1 top-strip centre (W43 verbatim):
  `WEEKLY IN ITALIAN · 매주 발행 · 이탈리아가 읽는 이탈리아어`.
- P1 serif line (46 pt, W43 pattern with W45 topics):
  `이탈리아어 주간지 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A`.
- P1 dark-band right lines (gold): `이번 주 첫 추위가 찾아와요` /
  `첫 추위의 주 · 2면 참고`.
- Band titles: `VITA · 생활`, `CULTURA · 문화`, `SPORT · 스포츠`,
  `GIOVANI · 청년`, `APPROFONDIMENTO · 심층`, `LINGUA · 언어`,
  `VALUTAZIONE E RISPOSTE · 연습과 정답`; band subs carry short Korean
  suffixes (e.g. `· 첫 추위와 추모의 날`, `· 디저트와 박물관`,
  `· 세리에 A와 유럽 대회`, `· 루카 이후`, `· 일기예보 읽는 법`,
  P7 sub head `언어 집중 ·`).
- Footer (every page): left
  `La Lucerna · 이탈리아어 주간지 VOL.2 · 텍스트는 이탈리아어 · 해설은 한국어`;
  right `제 {n} 면 / 총 8 면`.
- Gloss prefix (bslib4 `gloss()`): `해설 — ` (code-added; gloss strings
  carry no own prefix — no doubles).
- Explanation lines via the core's small-note mechanism; section heads
  keep the core's Italian head + short Korean suffix
  (`ESERCIZI · 제 N 면 연습`, `LA SETTIMANA DEL CALCIO · 축구 주간`,
  box titles likewise short: §10 lists the three titles shortened after
  audit flags).
- P8: answers header `RISPOSTE · 정답 — 면별로 정리했어요. 번호를 찾으면
  돼요`; right note `문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안
  문제예요`; separators `— 제 {pg} 면 —`; answer lines keep the IT
  family's dash style `{n}. {key} — {note}` (answer-generation code
  byte-identical to the core; writing items print `✓ {note}`).
- Type labels: 문장 완성 · 객관식 · 빈칸 채우기 · 단어 짝짓기 ·
  문장 만들기 · 번역 · 읽기 판단 · 문장 전환 · 쓰기.
  Instr labels: 빈칸 채우기 · 판단 · 문장 만들기 · 번역 · 쓰기 ·
  단어와 뜻 짝짓기.

## 4. P7 word box — definition frozen (hard gate)

- Italian definition sentence, byte-identical to the core (verified on
  the whitespace-normalised rendered text):
  `« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere
  se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`
- Only the gloss note below it was localised to Korean:
  `assaggio = 맛보기예요. 3면 파네토네 결승에서 무료로 맛봐요.`
  (2 lines, same as the core's Chinese note — col3 geometry unchanged
  apart from the §10 shortenings).
- The same freeze rule was applied to every other P7 element: all
  Italian clinic sentences, corrections, and the 8 quotes are
  byte-identical to the core; only Korean notes changed.

## 5. Readers' corner — no fabrication (hard gate)

Page print (P7, LETTERE DEI LETTORI box), Italian original first:

- Italian letter text, byte-identical to the core, including its own
  Italian example label: `«Ciao! Sono Li, studio italiano a Pechino.
  Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone —
  almeno in foto!» — Li (esempio della redazione)`
- Korean note below it (3 lines, replacing the core's Chinese note):
  `편집부 예시예요. 실제 편지도 8면 우수 작문도 아직 없어요. 편지를 보내
  주세요! VOL.3에 실어요!`
- Three-fact disclosure, mapped:
  1. No real letters — `실제 편지도 … 아직 없어요`, and the letter shown
     is labelled `편집부 예시예요` / `(esempio della redazione)`.
  2. No best P8 writing — `8면 우수 작문도 아직 없어요`.
  3. Example + deferral to VOL.3 — `편집부 예시예요` +
     `VOL.3에 실어요!` (publication in VOL.3, following the
     not-yet-existing items).
- Explicit Korean public invitation (imperative + VOL.3 publication
  promise, inside the box, not the preview line):
  `편지를 보내 주세요! VOL.3에 실어요!`
- The VOL.3 preview band's Italian line (`le vostre lettere vere e i
  testi migliori della pagina 8`) is the Italian original of the
  deferral; it is NOT counted as the invitation (the invitation is the
  Korean box note above).
- No Italian disclosure sentence was newly written: the core's P7 has
  no Italian disclosure sentence to keep (the core disclosure itself is
  Chinese), so the disclosure exists only in Korean — the same structure
  as the shipped W43 IT×KO and W45 IT×DE editions.
- No reader, letter, name, or quote was fabricated as real. The W43
  promise of real letters + best P8 writing is honoured only as this
  invitation + VOL.3 preview, exactly as in the core.

## 6. Gloss distribution (measured from the core, verified in render)

Core gloss() strings split on `·` (README §21 method — split on the
bare separator, never on the spaced form):

- P2: 6 — il cappotto · la sciarpa · i guanti · a strati ·
  il termosifone · il crisantemo
- P3: 5 — il panettone · il torrone · l'assaggio · la bancarella ·
  il cantiere
- P4: 4 — la giornata · la presentazione · gli spalti · la sera
- P5: 4 — il cosplay · gratuito · il documentario · lo schermo
- P6: 5 — la probabilità · la media · il modello · il bollettino ·
  aggiornare
- Total: **24 items, 1:1 with the core** (distribution NOT copied from
  any other family). Every headword was verified present in the rendered
  KO SVGs. The P1 explanation word list (separate from gloss()) carries
  4 items, also 1:1.
- P7 golden sentences: 8 quotes, each occurring exactly 2× in the
  whitespace-normalised joined SVG text (once in its article, once on
  P7), same as the core; the 8 P7 quote nodes are byte-identical to the
  core's, each paired with the same `(Pagina N)` tag
  (1, 1, 2, 2, 3, 4, 5, 6).

## 7. P8 gate (tools/p8.py)

- `p8.py compare` (explicit core/edition P8 paths, total 150):
  **CLEAN, 150 noted = 150 noted, missing=[] extra=[] uncertain=[]**,
  keydiff = [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 137, 138, 139].
- Keydiff adjudication, item by item (printed P8 lines, byte-compared):
  - Paren-branch pseudo-diffs (11): 6, 13, 14, 15, 16, 20, 38, 58, 71,
    74, 77. The core's trailing full-width paren group makes
    detect_note take the paren branch, so its extracted key includes
    the note head; the Korean half-width parens do the same. Printed
    answer keys are byte-identical (e.g. `6. previsioni`,
    `13. guanti`, `58. più bella`, `77. ci sarà`); only the note is
    translated and the brackets switch full-width → half-width (the
    W43 IT×KO family form). Not key changes.
  - True re-aims (3, legal per the W43 precedent): 137, 138, 139 are
    section-E translation items re-aimed Italian → Korean, exactly as
    W43 IT×KO re-aimed its section-E items: core keys were Chinese
    sentences, edition keys are their Korean translations
    (`월요일에 첫 추위가 찾아왔어요.` /
    `관객이 무료로 맛볼 수 있어요.` /
    `일요일 저녁, 피오렌티나–유벤투스 경기가 있어요.`); item 140
    keeps its Italian key with a Korean body, mirroring W43. The
    wrapped-note join artifact is noted: wrapped answer notes rejoin
    with a space (e.g. 139 reads `si gioca = 경기가 열려요`, not
    concatenated).
- P8 notes are pure Korean (no Han characters on P8; SVG Han = 0).
- P8 answer-note set equals the core's set (EXTRA_ONLY would have been
  acceptable; the result is the stronger CLEAN).

## 8. Geometry gates (all measured, R2 = final render)

- `occlusion_audit.py` (selftest OK, all 6 planted classes fired):
  edition **0 flags**, core **0 flags**, NEW **0 flags**, exit 0.
  R0 had 4 NEW flags, R1 had 1 NEW flag, all real, all fixed in fix
  rounds 1–2 (see §10); R2 re-audit is clean.
- Korean-specific scans (`ko_scans.py`, window 10–45, README #16
  W45 extension):
  - Mid-word splits with ≥3-syllable tails: **0** (23 candidates found,
    all tails ≤2 syllables — the largest tails are 2-syllable
    fragments such as `관|중석`, `업데이트|예요`, `실|어요`).
  - Line-start orphan punctuation: **0**.
  - Orphan line-tails (lone final-line fragments): **0** — no block-final
    line is a lone fragment; the scan's final-line candidates coincide
    with the mid-word list above, all tails ≤2.
  - Han characters: **0** on all 8 pages (see §2).
- Right-edge scan (ADVANCE method: PIL advance widths per anchor):
  **0 flags** on all 8 pages against the [40, 1910] frame band.
- Same-baseline collision scan (furniture bands, incl. P1 top band
  y=92 and every footer y=2624): **0 overlaps**. P1 top band, measured
  by advance (left start-anchored at 65, centre middle-anchored at 975,
  date end-anchored at 1885): left ends 392.3 → centre starts 690.9
  (298.6 px gap) → centre ends 1259.2 → date starts 1450.6
  (191.4 px gap). The Korean centre string fits the slot with wide
  margins.
- P6 chart-label coverage, baseline-anchored ink method (PIL getmetrics,
  anchor `ls`, later-drawn rects vs label ink): **max 0.0%** on all chart
  labels (Torino/Milano/Bologna/Roma/Napoli + value labels); threshold
  <30% passes with full margin. Bars sit clear of labels and values.
- Flow ends (final build log): P1-headline 1497 (bottom 1828),
  P2 col3 1025.0, P3 col3 1281.25, P4 col3 875.0, P5 col3 1285.75,
  P6 col3 1096.5, P6-ex 2569 (bottom 2580, same as core),
  P7 col3 **1673.0** (13 px clear of the FRASI rule at 1686, same as
  the core), P8-ex 965 (bottom 1332), P8-keys 2499 (bottom 2552,
  53 px clear of the footer zone).
- Build warnings final: FLOW OVERFLOW 0, HEAD TOO WIDE 0.
- Visual check: all 8 cards in cards/ inspected page by page
  (overflow, overlap, footer clearance, frost drawing, P4 fixture
  table, P6 chart + caption, P7 col3 vs FRASI rule, P8 answers bottom
  vs footer). No defects seen.

## 9. Independent counts (from the rendered SVGs, not the registry)

- Exercise numbers extracted from all 8 SVGs (chip level text followed
  by `N.` / `N–M.` nodes, ranges expanded):
  **150 items, set exactly 1–150, no missing, no duplicates**.
- Levels from the same extraction: **A2 47 · B1 70 · B2 33**;
  per page 10/18/18/18/18/18/12/38 — identical to the core and to §1.
- Model text: extracted from both P8 SVGs, normalised — KO == core
  byte-identical; **81 model words**, matching the core.
- P8 writing item prints `150. ✓ 모범 답안은 이 면 H 구역에 있어요 (81단어)`.

## 10. Build / reproduce

- Build dir: hidden_files/weekly-report-w45-it-ko-build/ (bslib4.py,
  svglib.py, run.py, render.py, assets/ copied from the W45 IT core
  build; content12/34/56/7/8.py transformed by transform.py;
  transform.py + per-round sha256 baselines + raw tool outputs kept).
- Pipeline (core pipeline reused as-is):
  - Transform (from a fresh core-build copy): run transform.py once —
    it performs the base replacements (250 counted pairs), then FIX
    ROUND 1 (6 pairs), then FIX ROUND 2 (1 pair) in order, with count
    assertions; re-runs skip already-applied phases. Final audit
    asserts no Han characters and no full-width CJK punctuation remain
    in the operative files (transform.py itself is excluded: it carries
    the old-side search strings by design).
  - Build (ONE process only — shared-registry rule): `cd
    hidden_files/weekly-report-w45-it-ko-build &&
    ../../tools/venv/bin/python run.py`
  - Render: `../../tools/venv/bin/python render.py` (writes svg/ +
    cards/ + both PDFs into files/weekly-report-w45-it-ko/).
- Interpreters (recorded separately, as required):
  - run.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0.
  - render.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
    cairosvg 2.9.1, pypdf 6.21.2. System python3 has no cairosvg and
    must not be used for render.py.
- Reproducibility note: run.py and render.py were always run in the
  single-driver-process form; no content module was ever imported or
  run standalone, and nothing was ever executed inside the core build
  directory (the core hashes in §2 prove it).
- Fix rounds (each preceded by a full pre-fix sha256 baseline of all
  SVG/card/PDF outputs, kept in the build dir):
  - R0 → R1 (sha256-r0.txt): occlusion audit reported 4 NEW flags, all
    real, plus the orphan scan's 1 blocking ≥3-syllable tail split.
    Fixes, all wording only, all synced into transform.py FIX ROUND 1:
    P1 cifre title to `LA SETTIMANA IN CIFRE · 이번 주 숫자`, P2 frase
    title to `LA FRASE PER RICORDARE · 암기문장`, P7 parola gloss to
    2 lines, P7 errs #4 note to 1 line, P7 letter disclosure to 3 lines
    (same 3 facts + invitation + promise, shorter wording), P6 bridge
    reworded so the ≥3 split disappears (`확인 안 됐어요` form).
    R1: P7 col3 1673.0, occlusion 1 NEW flag left, orphan scan clean.
  - R1 → R2 (sha256-r1base.txt): the 1 remaining flag was the P1 cifre
    title still crossing its box border by 1.8 px (ink 962.8 > border
    961.0). Fix, synced into transform.py FIX ROUND 2: cifre title to
    `LA SETTIMANA IN CIFRE · 이번 주`. R1→R2 changed exactly p1 SVG +
    its card + both PDFs (verified by hash diff); R2: occlusion 0/0/0,
    all other gates re-run green.
- ABSTRACT.txt: Korean single line, no ASCII double quotes, naming the
  week's real topics (first cold snap, 2 November memorial day,
  Panettone World Cup Milan 7–8 November, Torrone festival Cremona,
  Serie A matchday 11) + learner search phrases (learning Italian by
  reading, with Korean explanations) + masthead, target language name,
  A2–B2, 150 exercises.

## 11. W43 deviations (this edition vs shipped W43 IT×KO)

- VOL.2 throughout (core VOL changed since W43); top-strip string,
  serif-line pattern, band titles, footer template, page line, gloss
  prefix, P8 separators, dash answer style, and instruction-word list
  are otherwise identical to W43 IT×KO.
- Counts follow the W45 core, not W43: levels A2 47/B1 70/B2 33
  (W43: A2 46/B1 71/B2 33); model text 81 words (W43 core model text
  differs — 81 is the W45 core's count, verified byte-identical here).
- New wording-only tightenings with no W43 counterpart (all forced by
  Korean length vs the W45 core's tighter boxes): P1 cifre title to
  `이번 주`; P2 frase title to `암기문장`; P7 parola gloss to 2 lines;
  P7 errs #4 note to 1 line; P7 letter disclosure to 3 lines; P6 bridge
  to the `확인 안 됐어요` form.
- P8 note-bracket form: half-width `()` (W43 IT×KO form), not the
  core's full-width `（）` (which only ever wrapped Chinese notes).

## 12. Deliverables

- files/weekly-report-w45-it-ko/ (svg/ 8 SVGs, cards/ 8 PNGs,
  La-Lucerna-VOL2-KO.pdf, La-Lucerna-VOL2-KO-web.pdf, WEEKLY-KIT.md,
  ABSTRACT.txt).
- Print PDF: La-Lucerna-VOL2-KO.pdf — 11,643,953 bytes, sha256
  9a47b3027d918e2ccf88f5f54c3e72197399eb338383049d0da1258f11c8a2a5,
  8 pages.
- Web PDF: La-Lucerna-VOL2-KO-web.pdf — 3,515,696 bytes, sha256
  b1e03e77e1dc38c349c67e0bda48c27cd060a69e448a01afa9fead1700f945ca,
  8 pages, under the 10 MB Discord ceiling.
- SVG sha256 (final R2): p1 19cec1889ed5b3e1ef1d65b2a0e2ef5ad27d3b0eefde25152c1532788a8afabb,
  p2 1f14d5bbc12edf768c84beab3463692d768d3d2a158c9e3c6e37b9a15c0c6521,
  p3 a87d4b59a88d9ee9f36c2a05c7e8573b70d4e24655cd161f157d5ad43ec7a1d3,
  p4 addbece4500380fedd831ebb91fd91c05c50b5d733b66365ba402e6cc08c9338,
  p5 94eb15911c99617f073ad028ff549bc11da3b644c5f0d616dc3aadc1db08587b,
  p6 6ca5ba3a23c775549a1e217bf73765f312935c499295b3a57c934ed7ec844239,
  p7 faae976e92146d3c4b7adc931f2c0c43401d14a579808d55f4d5a4f228af72,
  p8 1e04a7e207efbc9bdb838372b3bb17a2bd5114098f3ed4b33bd794e629e9fe13.
- Card sha256 (final R2): p1 a2ba12d3133c16a186691cc16d782eb6e0b48a60eaa0e8dca617efd78107a0da,
  p2 6c7ddb3f676b670f19e44cd6885df534aca0eed05d4acad44cbc7dc94fccf8fa,
  p3 557c574eb386ad42e21989274fcbd19c1d5f83e5fa11f32d434d0ef754e1810e,
  p4 af701d8c7d6137d5096c44364855eb395e43556761d27d174d7674ba7b535d6f,
  p5 b47b63904ee5eee7fe00c5fad70900ed49cb0aee956324c9b724aad4cb20b135,
  p6 f5bb605a37cd775a854d8ffc743d68d33283f40511753ac80c3a1bb2d0ba413e,
  p7 6ac9fff7cf36d2df2aed2cd07ee980c4dea42a9b313dea1f8a25dd9328f08dd4,
  p8 34d49cdf911761ee89cabbce9b7063657c211b4201d295b06ff8a253a5f61470.

## 13. Delivery

- NOT pushed to git, NOT posted to Discord, NO messages sent (per task).
  Delivery to the LucernaRead/weekly repo is the main line's job.
- NOT self-certified as finalized: a fresh full independent proof round
  is still required before delivery.
