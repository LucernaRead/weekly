# Lucerna Weekly W46 — Round 2 Independent Proofread Verdict

- Issue: VOL.3, Mon 2026-11-09 to Sun 2026-11-15, target Traditional Chinese (ZH-TW)
- Role: independent proofreader (Round 2). The proofreader did not build or fix these editions.
- Proofread date: 2026-11-03 (America/Toronto). All checks run on the FINAL artifacts
  (post-fix renders, timestamps 2026-11-03). No edition file was edited, re-rendered, or moved;
  no weekly-git/index.json/push/insert/Discord action was taken.
- Scope: all 10 editions — `2026-w46-zh-tw-en` (core, dir `weekly-report-w46-zhtw-core`),
  `-de`, `-es`, `-fr`, `-it`, `-ja`, `-ko`, `-nl`, `-pt`, `-ru`.
- Gate dir (fresh, Round 2 only):
  `hidden_files/w46/zh-tw-proofread-gates-round2/` — freeze/p8/occlusion JSONs + logs,
  `analysis.py`, `analysis-report.txt`, `added-strings-*.txt`, `strips/` (1:1 P7 pixel strips
  + measurements), `supplementary-scans.txt`, this verdict file.
- Sources read in full before gating: `files/weekly-report-SOP.md`, the fix record
  `hidden_files/w46/zh-tw-fix/FIX-REPORT.md`, all 10 `WEEKLY-KIT.md` files including every
  补记 appendix, and `tools/README.md`. The Round 1 verdict .md does not exist on disk; the
  D1–D6 list was judged against the ARTIFACTS, not the paperwork.
- Method: shared toolkit only for canonical gates (`tools/freeze.py` diff `--strict-cjk`,
  `tools/p8.py` compare, `tools/occlusion_audit.py`), plus independent SVG/PDF parsing
  (geometry, pixel strips, stem counts, chart-bar measurement, SHA/size verification) and
  full-frame visual review of the shipped `cards/*.png`. No build code was imported.

## Per-edition verdict

| Edition | Verdict | Blocking defects |
|---|---|---|
| en (core) | PASS | 0 |
| de | PASS | 0 |
| es | PASS | 0 |
| fr | PASS | 0 |
| it | PASS | 0 |
| ja | PASS | 0 |
| ko | PASS | 0 |
| nl | PASS | 0 |
| pt | PASS | 0 |
| ru | PASS | 0 |

## Fix verification (D1–D6) — every claim adjudicated against artifacts

### D4 — P6 box "3座城市" — CONFIRMED, all 10 editions
- Every edition's P6 SVG (y=397.4) reads `· 抽機票:23張、19天、3座城市`.
- Sweep: `19座城市` = 0 occurrences in all 10 SVG sets AND all 10 `.text.md` files;
  `3座城市` = 1 per edition.
- Independent fact check against the issue's own text: P1 states Oct 26–Nov 13, 19 days,
  23 return tickets, 2 Los Angeles tickets on Nov 11; P5 timetable rows name 11月11日 洛杉磯 /
  11月12日 東京 / 11月13日 首爾 (each 來回機票兩張) — exactly three cities; Oct 26–Nov 13
  inclusive = 19 days. No Simplified forms (洛杉矶/东京/首尔) anywhere. The figure is supported.

### D1 — P5 glossline translated (de/es/fr/it/pt) — CONFIRMED, translations judged correct
The five glosses were authored by the fix worker (not table-sourced) and are judged here
as translations. Each matches the edition's own P2 label/conventions and number formatting:

- de: `Übungszahlen: NT$450 + NT$1.550 = NT$2.000, genau das Budget.` — correct German;
  thousands with `.`, matches the P2 label `Übungszahlen:`.
- es: `Números de práctica: NT$450 + NT$1.550 = NT$2.000, exactamente el presupuesto.` —
  correct Spanish; matches P2 conventions.
- fr: `Chiffres d'entraînement: NT$450 + NT$1 550 = NT$2 000, exactement le budget.` —
  correct French; spaced thousands, space before the colon, matches the P2 label.
- it: `Numeri di pratica: NT$450 + NT$1.550 = NT$2.000, esattamente il budget.` — correct
  Italian; `budget` is an established loanword.
- pt: `Números de prática: NT$ 450 + NT$ 1.550 = NT$ 2.000, exatamente o orçamento.` —
  correct Portuguese; matches the PT `NT$ 3.000` spacing convention.
- ja/ko/nl/ru renderings unchanged and correct (ja `練習の数字：…ちょうど予算通りです。`;
  ko `연습 숫자: …예산과 정확히 같아요.`; nl `Oefengetallen: …precies het budget.`;
  ru `Числа для практики: … — ровно бюджет。`); en native line unchanged; P2 glosslines
  untouched in all 5 (verified, e.g. de `Übungszahlen: Mantel für 3.000 NT$…`,
  fr `Chiffres d'entraînement: manteau à 3 000 NT$…`). No `Practice numbers` survives outside
  the core; the English-residue scan's hits were all false positives (proper names
  `Arts in the Park`, `Standard Chartered`, `The Celestial Bookhouse`; loanwords
  budget/cashback; French `points`; German `Was`; Dutch `is`).

### D2 — P8 note 134 translated (de/fr) — CONFIRMED, neighbours intact
- de: `134. 集點 — Punkte sammeln heißt 集點.` between 133 `Ein Festzug heißt 遊行.` and
  135 `Ein Karneval heißt 嘉年華.`
- fr: `134. 集點 — Collecter des points, c'est 集點.` between 133 `Une marche de fête,
  c'est 遊行.` and 135 `Un carnaval, c'est 嘉年華.`
- Both match house wording; no English `Collecting points is 集點.` survives outside the core.

### D3 — FR P4 note re-wrapped, rewording acceptable — CONFIRMED
- Re-measured independently (PIL, Noto Sans CJK TC Regular idx 3): 11 gloss lines at x=545,
  y=246.5–543.8, 20.5pt; max advance width 386.2px, fits the ~398px box.
- No mid-word splits: `Tianmu` whole (twice), `du` whole (`la nuit du 21…`); `ville` no
  longer appears — it was removed by the rewording (`La ville de Taipei double…` →
  `Taipei double…`), not kept whole (the fix record's "ville whole" phrasing is imprecise;
  the underlying no-split claim holds).
- Wording judgment: `a lieu` → `se tient` is fully idiomatic (both "takes place");
  `La ville de Taipei` → `Taipei` shortens the subject but the actor (the city) is unambiguous
  from context. Facts preserved: 21–22 nov., 14h00, Tianmu → Taipei Dome, grass concert +
  overnight camping night of the 21st, player activities on the 22nd, doubling all November,
  10 vs 5 points, 267 venues. ACCEPTABLE — no fidelity or fact loss.

### D5 — P7 teaser clears the footer rule (es/fr/nl) — CONFIRMED by geometry AND pixels
- SVG geometry: teaser rect (`fill #2c2822`, h=118) bottoms — en/es/fr 2573.86, nl 2572.36,
  de 2530.84, it/pt 2557.36, ja/ko 2529.86, ru 2562.84 — all clear of the footer rule y=2580
  (line x 65–1885, stroke #b3a06a, width 1.6).
- 1:1 pixel strips (P7 SVGs rasterized at 1950×2700 via cairosvg, `strips/`): last row with
  >100 dark pixels = 2573 (en/es/fr), 2571 (nl); row 2580 has only 12 dark pixels in 4 corner
  runs (x 26–29, 39–40, 1909–1910, 1920–1923 — outside the content columns, not teaser ink).
- Teaser text is the identical frozen Chinese line in all three (VOL.4 teaser: parade/Golden
  Horse/steel close/Xiaoxue/letters/best writing); content multiset unchanged vs Round 1
  (only y positions shifted −14px). No text ink touched.

### D6 — Abstracts reworded (8), it/pt untouched — CONFIRMED
- All 10 `ABSTRACT.txt`: single line, no ASCII double-quote, topics (Double 11, ITF,
  Golden Horse, Kaohsiung steel, Dragons parade, Arts in the Park) + A2–B2 + 150 intact.
- Reworded closings use practice framing in each language (en `150 exercises using this
  week's topics as material.`; de `150 Übungen mit den Themen der Woche als Material.`;
  es `150 ejercicios con los temas de esta semana como material.`; fr `150 exercices avec
  les sujets de la semaine comme matériau.`; ja `今週の話題を素材にした150問の練習。`;
  ko `이번 주 주제를 소재로 한 연습 문제 150개.`; nl `150 oefeningen met de thema's van
  deze week als materiaal.`; ru `150 упражнений с темами этой недели в качестве материала.`).
- Programmatic checks (line count/quote/150/A2–B2/learn-by-news wording) all clean;
  it/pt abstracts were already practice-framed and untouched.

## Gate outputs summary (independent re-gate, final artifacts)

- **Freeze** (`freeze.py diff --strict-cjk`, core vs each edition): en/de/es/fr/it/nl/pt/ru
  exit 0, added CJK = 0 on all 8 pages each. ja exit 1 (total added CJK 6445), ko exit 1
  (5267) — byte-identical to the Round 1 files; adjudicated state = reader-native
  Japanese/Korean script + quoted CJK terms, no new target text. R2-vs-R1 freeze diffs:
  ja/ko/nl/ru JSONs identical to Round 1; de/es/fr/it/pt differ in EXACTLY the D1/D2/D3
  strings and nothing else. R2-vs-fix-gate JSONs differ only in path spelling.
  (The `freeze.py baseline` reproduction was not re-run; the strict-CJK diff requirement is
  satisfied by the diff runs.)
- **P8** (`p8.py compare`, 150 items): all 9 fan-outs CLEAN — 150 noted both, missing=[],
  extra_count=0, uncertain=[], keydiff=[]. Core extract: noted set = 150 of 150 (1–150).
  All 9 `p8-*.json` byte-identical to the fix worker's.
- **Occlusion** (`occlusion_audit.py`, selftest OK in every run — all 6 planted classes fired,
  clean controls silent): 0 flags standalone AND 0 NEW vs core in all 10 editions, all 8 pages.
- **Counts** (independently re-measured): exercise stems per page 10/18/18/18/18/18/12/38
  = 150, continuous 1–150, no gaps/dupes (P8 key section 1–150 present). Level chips: 138
  glyphs — the four matching groups (25–28, 43–46, 61–64, 79–82) share one chip per group
  of 4 (confirmed visually, e.g. EN P2 "A2 25–28. Match"), so 138 glyphs ≠ 150 exercises;
  the registry split A2 44 / B1 74 / B2 32 is not contradicted. Types per KIT
  (單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1) consistent with the P8 key.
- **Charts** (measured): P4 brick bars 90.0/450.0/900.0 px (= 10/50/100 pts × 9); P6 olive
  bars 220/300/400/800 px. Both match KIT claims exactly.
- **P7 phrases**: all 8 verbatim Traditional Chinese phrases occur exactly 2× per edition
  (article + P7), quoted form `「…」` exactly 1× on P7.
- **Weekdays/dates** verified with `TZ=Asia/Taipei date`: 2026-11-09 Mon … 11-15 Sun;
  11-22 Sun; 2026-10-26 Mon. All claims correct.
- **Arithmetic re-derived**: 17 days Nov 6–22; 3 hours 14:00→17:00; 450+1,550=2,000;
  3,000−220=2,780; 5,000−800=4,200; 27−20=7; 17:00−10:00=7h — all consistent with the core.
- **Badge colour**: all 10 P1 badges — text node y=378.0, 21pt bold, fill `#3e4c2a` (OLIVE),
  in the core's subtitle slot, wording per KIT, confirmed visually on all 10 P1 cards.
  The `#a4553a` brick is the strapline's fill, not the badge's; the KIT 补记 corrections
  match the artifacts.
- **Footers**: present on all 8 pages of all 10 editions in the reader's native language
  (e.g. de `Seite N von 8`; ja `N ページ（全 8 ページ）`; ru `Страница N из 8`), plus P8
  page separators; confirmed in text and on cards.
- **Native-language layers**: full explanation layer of all 9 fan-outs read via freeze-diff
  added-strings dumps (~425–490 entries each). Correct native language throughout; no
  untranslated English strings; no Simplified residue (see below); no wrong-script
  characters. IT/PT P8 pinyin glosses verified with correct tone marks. JA shinjitai
  (塩埕, 国, 学, 与 in 授与) and KO readings (소설（小雪）) are legitimate Japanese/Korean,
  not Simplified residue — the simplified-candidate scan's only hits were these JA
  characters, all adjudicated legitimate; the other 9 editions had zero candidate hits.
- **Reader-facing sweep**: only `VOL.3`/`VOL.4` (legitimate volume labels + next-issue
  teaser). Zero week/language codes, structure labels, repo links, or SOP/proofread wording.
- **W45 promises**: ITF final-day + Double 11 coverage present on P1 (lead + second story +
  rails); deferral disclosure present in Chinese on P7 in every edition plus the
  native-language disclosure beside it (wordings match KIT quotes); VOL.4 teaser carries
  the letters/best-writing invitation forward and the steel-festival closing stretch is
  P3's feature — all verified.
- **PDFs**: every web PDF has a real text layer (pdftotext bytes > 0), size ≤ 7 MB
  (largest: ja 2,208,932 B), print==web extracted text byte-identical in all 10.
  File sizes and SHA-256 (first 16) match the fix record's inventory exactly for all 10
  editions (text.md, web PDF, print PDF) — see `supplementary-scans.txt`.
- **text.md**: H1 preserved verbatim per edition (e.g. en `# VOL.3 · Traditional Chinese text ·
  English explanations`); sizes match inventory.
- **Supplementary geometric scans** (tools README requirement): same-baseline ink-collision
  scan on P1 bands — 0 collisions in all 10 editions; chart-label graze scan fired at the
  same 3 header sites in every edition and was adjudicated FALSE POSITIVE by full-frame
  card review (headers visibly clear of bars; canonical audit agrees). Image credits
  present in all 10 editions, both photos (P2 CorraleH CC0; P4 Bain News Service PD).
- **Visual QA**: full-frame review of the shipped cards — P1 ×10, P8 ×10, P6 ×10, P5 ×5,
  P4 fr, P7 ×3 (39 cards), plus spots P2 (en, ru), P3 (en), P4 (nl). No overflow, overlap,
  missing glyphs/tofu, or missing credits; no fix-introduced regression on any changed page.

## Residual defects

**None. Zero blocking defects, zero new defects.**

## Non-blocking observations (recorded, do NOT block shipping)

1. FR P1 gloss: `1 600` wraps across lines (`…123 pays et villes, 1` / `600 stands…`).
   Digits complete and unambiguous; French thousands separator is a breakable space.
2. PT and IT P8 item 70: `Los Angeles` wraps across lines (`Los` / `Angeles.`). Name
   complete and unambiguous.
3. NL P8 item 119: `De beurs is aan zijn 34e editie.` — idiomatic Dutch would be
   `…aan zijn 34e editie toe` / `beleeft zijn 34e editie`; meaning fully clear.
4. JA/KO P6 three-questions gloss: `条件はいくらですか` / `조건은 얼마예요?` ("how much is
   the condition") for the spending threshold; understandable in context
   (DE: `Wie hoch ist die Schwelle?`).
5. RU P7 disclosure is condensed vs. the Chinese (`…но ничего не пришло`); practical
   meaning identical, and the full Chinese disclosure is printed alongside.
6. NL P4 box title is two text nodes (`棒球詞卡 ·` + `Honkbalwoorden`); renders cleanly
   as one title on the card — resolved, not an issue.

## Adjudicated Round 1 NON-defects — honored, not re-raised

P8 notes 99/127 numerals; P7 "Group the words" shorthand; ES P3 "587 candidaturas";
DE/FR/IT/KO/PT items in the fix record's non-defect section; P7 letter salutation as
colloquial voice; RU pair-185 fix.

## Final verdict

ROUND 2 PASS (all 10 shippable)
