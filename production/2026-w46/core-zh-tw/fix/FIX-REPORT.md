# W46 ZH-TW family — Round 1 fix report (fix worker)

- Issue: 2026-W46, Mon 2026-11-09 to Sun 2026-11-15, VOL.3, target Traditional Chinese.
- Family: 10 editions — 2026-w46-zh-tw-en (core dir `files/weekly-report-w46-zhtw-core/`), -de, -es, -fr, -it, -ja, -ko, -nl, -pt, -ru (`files/weekly-report-w46-zh-tw-*/`).
- Fix date: 2026-11-03 (America/Toronto). Fix worker only: defects D1–D6 as specified in the Round 1 verdict tasking. No other changes were invented.
- NOTE ON THE VERDICT FILE: the path named in the tasking
  (`hidden_files/w46/zh-tw-proofread-gates/proofreader-verdict-round1.md`) does not exist on disk
  (the gates dir holds the proofreader's gate outputs — freeze/p8/occlusion JSONs, textdiffs,
  per-page text extracts, english-residue-scan.txt — but no verdict .md; a filesystem-wide
  search found only the FR family's verdict). Every defect below was therefore re-verified
  independently against the shipped artifacts and build sources before fixing; the before/after
  quotes are taken verbatim from those sources. The tasking's quoted defect specs matched the
  artifacts in every checkable detail (see per-defect evidence). A Round 2 independent
  proofread still follows; this report's re-gating does not replace it.

## Method

- All changes went through the source content files in the build dirs
  (`hidden_files/weekly-report-w46-zhtw-build/` for the core,
  `hidden_files/weekly-report-w46-zh-tw-<lang>-build/` for fan-outs). No SVG/PDF was hand-edited.
- D4 was fixed in the CORE source first, then fanned out as the identical frozen-string
  correction to all 9 fan-out build dirs (no edition was edited directly for D4 in any other way).
- Full re-render from source for all 10 (run.py + render.py, tools venv), then web PDFs via
  `tools/webpdf.py` only, then `<slug>.text.md` regenerated with
  `hidden_files/w46/export_zhtw_textmd.py` from each edition's own SVG text layer with the
  existing H1 preserved verbatim.
- Work was local only: nothing touched `~/workspace/weekly-git`, `index.json` was not edited,
  nothing was pushed/inserted/posted to Discord, and no edition content was dumped into chat.

## D4 — FROZEN CORE, all 10 editions: unsupported "19座城市"

- Location: core `content56.py` line 198, P6 "數字一覽 · By the numbers" box (frozen core text,
  byte-identical in all 10 build dirs).
- Before: `抽機票:23張、19天、19座城市`
- After: `抽機票:23張、19天、3座城市`
- Evidence against the issue's own facts: P1 (content12.py) — "從10月26日到11月13日,連續19天抽出23張來回機票,11月11日當天抽出洛杉磯來回機票兩張";
  P5 article (content56.py) — "11月11日當天抽出洛杉磯來回機票兩張,11月12、13日再抽東京、首爾來回機票";
  P5 timetable box — three rows: 11月11日 洛杉磯 / 11月12日 東京 / 11月13日 首爾. The draw
  covers exactly three cities; "19座城市" appears nowhere else in the issue as a supported fact.
  The correction changes only the city count (19 → 3); "23張" and "19天" are supported and unchanged.
- Fan-out: the identical one-line correction was applied to content56.py:198 in all 9 fan-out
  build dirs after the core fix. Freeze diffs after re-render confirm no other frozen-string
  change (see gates).
- Post-fix sweep: "19座城市" occurs 0 times in all 10 build dirs, 0 times in all 10 final
  P6 SVGs, and 0 times in all 10 regenerated text.md files (verified by grep; see gate log).

## D1 — P5 practice-example glossline untranslated (de/es/fr/it/pt)

- Location: each edition's `content56.py` line 30, P5 "練習例子" box, second (grey sans) line.
  The core (EN) line is legitimately English and was NOT changed.
- Before (all 5): `Practice numbers: NT$450 + NT$1,550 = NT$2,000, exactly his budget.`
- Reference renderings already translated in the family (verbatim from ja/ko/nl/ru build dirs):
  ja `練習の数字：NT$450 + NT$1,550 = NT$2,000、ちょうど予算通りです。`;
  ko `연습 숫자: NT$450 + NT$1,550 = NT$2,000, 예산과 정확히 같아요.`;
  nl `Oefengetallen: NT$ 450 + NT$ 1.550 = NT$ 2.000, precies het budget.`;
  ru `Числа для практики: NT$450 + NT$1 550 = NT$2 000 — ровно бюджет。`
  (No de/es/fr/it/pt rendering existed in the translation tables — pair 254 in
  `zhtw-translations-e.json` covers only ja/ko/nl/ru — so the five translations below were
  authored to match each edition's own P2 glossline label and 算一算 gloss conventions.)
- After:
  - de: `Übungszahlen: NT$450 + NT$1.550 = NT$2.000, genau das Budget.`
    (P2 label "Übungszahlen:"; 算一算 gloss "450 + 1.550 = 2.000, genau das Budget.")
  - es: `Números de práctica: NT$450 + NT$1.550 = NT$2.000, exactamente el presupuesto.`
    (P2 label "Números de práctica:"; 算一算 gloss "450 + 1.550 = 2.000, exactamente el presupuesto.")
  - fr: `Chiffres d'entraînement : NT$450 + NT$1 550 = NT$2 000, exactement le budget.`
    (P2 label "Chiffres d'entraînement :"; 算一算 gloss "450 + 1 550 = 2 000, exactement le budget.")
  - it: `Numeri di pratica: NT$450 + NT$1.550 = NT$2.000, esattamente il budget.`
    (P2 label "Numeri di pratica:"; 算一算 gloss "450 + 1.550 = 2.000, esattamente il budget.")
  - pt: `Números de prática: NT$ 450 + NT$ 1.550 = NT$ 2.000, exatamente o orçamento.`
    (P2 label "Números de prática:" with PT "NT$ 3.000" spacing; 算一算 gloss
    "450 + 1.550 = 2.000, exatamente o orçamento.")
- The P2 practice glossline (content12.py:118) was verified translated and left untouched in all 5.

## D2 — P8 answer note 134 untranslated (de/fr)

- Location: each edition's `content8.py` line 61, the 完成句子 exercise with key 集點
  (P8 printed note "134. 集點 — …"). Neighbours 133 (遊行) and 135 (嘉年華) and the
  renderings in es/it/pt/ja/ko/nl/ru were already translated; only de/fr kept the English gloss.
- Before (de and fr): `Collecting points is 集點.`
- After:
  - de: `Punkte sammeln heißt 集點.` (house wording: content34 gloss "集點 (Punkte sammeln)";
    neighbours "Ein Festzug heißt 遊行." / "Ein Karneval heißt 嘉年華.")
  - fr: `Collecter des points, c'est 集點.` (house wording: content34 gloss
    "集點 (collecter des points)"; neighbours "Une marche de fête, c'est 遊行." /
    "Un carnaval, c'est 嘉年華.")
- Reference renderings in other editions (verbatim): es `Acumular puntos es 集點.`;
  it `Raccogliere punti è jídiǎn.`; pt `Acumular pontos é jídiǎn.`;
  ja `ポイントをためることとは、集點のことです。`; ko `포인트 모으기가 바로 集點이에요。`;
  nl `Punten sparen is 集點.`; ru `Накопление баллов — это 集點。`
- Rendered P8 notes now read (de) `134. 集點 — Punkte sammeln heißt 集點.` and
  (fr) `134. 集點 — Collecter des points, c'est 集點.` (verified in final SVGs; p8.py compare
  still CLEAN 150/150 — see gates).

## D3 — FR P4 note mid-word wrap (fr only)

- Location: FR `content34.py` line 113, the P4 gloss ("Note — …") rendered in the P4 flow box.
- Before (rendered SVG lines): `… à Tianm` / `u: concert sur l'herbe et camping la nuit d` /
  `u21, … La vill` / `ede Taipei double …` — "Tianmu", "du", "ville" split mid-word.
  Cause: the shared `wrap()` post-kinsoku width repair pushes single characters to the next
  line when a near-full line is pushed over max width; the shared wrapper was NOT changed.
- Fix (source re-wrap, two minimal meaning-preserving changes in the gloss string only):
  - `pour les supporters a lieu les 21-22 nov. à Tianmu` →
    `pour les supporters se tient les 21-22 nov. à Tianmu`
  - `La ville de Taipei double les points U-Sport` → `Taipei double les points U-Sport`
- After (full gloss): `Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain
  (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de
  remerciement de deux jours pour les supporters se tient les 21-22 nov. à Tianmu :
  concert sur l'herbe et camping la nuit du 21, activités avec les joueurs le 22.
  Taipei double les points U-Sport tout le mois de novembre : 10 points par visite
  au lieu de 5, dans 267 lieux.`
  Every fact is preserved (dates, times, places, 10/5 points, 267 venues, whole-month doubling).
- Verification: offline `wrap()` simulation on the edited string gives 11 lines (same as before),
  0 mid-word splits, max line width 395.8px ≤ 398px; the rendered FR P4 card was visually
  checked at full frame (see gates/visual QA).

## D5 — P7 teaser box crosses the footer rule (es/fr/nl)

- Before (SVG geometry, DARK teaser rect y+height, footer rule y=2580):
  es 2469.86 + 118 = 2587.86; fr 2469.86 + 118 = 2587.86; nl 2468.36 + 118 = 2586.36;
  core 2455.86 + 118 = 2573.86 (clear by 6.14px).
  Cause: `fy = max(1712, col3_end + 44)` — the readers'-corner box is taller in these three
  editions (longer disclosure text + the +40 bottom padding from the BOXTITLE fix), pushing
  `py` and the teaser rect down. The readers'-corner padding was NOT touched.
- Fix (each edition's `content7.py` line 129, geometry only — teaser text, wording and
  position relative to its box are unchanged):
  - Before: `py = fy + 66 + 4 * 138 + 18`
  - After: `py = fy + 66 + 4 * 138 + 4  # fix 2026-11-03: was +18; teaser bottom crossed the footer rule (2587.86 > 2580)` (nl comment cites 2586.36)
  The whole teaser block (rect + title + text) shifts up 14px; no text ink was reworded,
  resized, or reflowed.
- After (SVG geometry): es 2573.86, fr 2573.86 (exactly the core's bottom), nl 2572.36 —
  all clear of the 2580 footer rule. Verified by SVG geometry AND 1:1 pixel strips of the
  rendered P7 cards (see gates/visual QA). No other edition's teaser moved (all others were
  already ≤ 2562.84).

## D6 — Abstract closings, news framing (en/de/es/fr/ja/ko/nl/ru; it/pt CLEAN, untouched)

- Location: `ABSTRACT.txt` in each edition dir (the abstract is not rendered on any page;
  it lives only in ABSTRACT.txt / future frontmatter). it/pt abstracts already used practice
  framing and were NOT touched.
- Before → After (closing clause only; topic lists, VOL.3, A2–B2 and 150-exercise statements unchanged):
  - en: `learn Traditional Chinese by reading this week's Taiwan and Hong Kong news.` →
    `150 exercises using this week's topics as material.`
  - de: `Traditionelles Chinesisch lernen mit den Nachrichten der Woche aus Taiwan und Hongkong.` →
    `150 Übungen mit den Themen der Woche als Material.`
  - es: `aprende chino tradicional con las noticias de la semana de Taiwán y Hong Kong.` →
    `150 ejercicios con los temas de esta semana como material.`
  - fr: `apprendre le chinois traditionnel avec les nouvelles de la semaine de Taïwan et Hong Kong.` →
    `150 exercices avec les sujets de la semaine comme matériau.`
  - ja: `台湾と香港の今週のニュースで繁体字中国語を学ぶ。` → `今週の話題を素材にした150問の練習。`
  - ko: `대만과 홍콩의 이번 주 뉴스로 번체 중국어를 배워요.` → `이번 주 주제를 소재로 한 연습 문제 150개.`
  - nl: `leer traditioneel Chinees met het nieuws van deze week uit Taiwan en Hongkong.` →
    `150 oefeningen met de thema's van deze week als materiaal.`
  - ru: `изучайте традиционный китайский по новостям недели из Тайваня и Гонконга.` →
    `150 упражнений с темами этой недели в качестве материала.`
- All 8 reworded abstracts remain valid single-line files with no ASCII double-quote, and still
  name the real topics (Double 11, ITF travel fair, Golden Horse, Kaohsiung steel sculpture,
  Dragons parade, Arts in the Park), A2–B2, and 150 exercises (verified programmatically).

## Adjudicated non-defects / confirmed truths — NOT changed

- Badge colour: OLIVE #3e4c2a is the rendered truth in ALL 10 editions (P1 badge text,
  y=378, 21pt bold, fill #3e4c2a, verified in every final P1 SVG). No badge colour was changed.
  The KIT records in de/es/fr/it/pt that claimed "BRICK #a4553a" were corrected in the fix
  records below to state the rendered truth (OLIVE #3e4c2a); ja/ko/nl/ru KITs already said
  OLIVE and the core KIT says OLIVE. (The core KIT's lesson-20 parenthetical about W45
  badges in other targets was left untouched — it describes a different case.)
- P7 letter salutation 「編輯好： was left exactly as frozen core text.
- All §5 adjudicated non-defects were left alone (P8 notes 99/127 numerals, P7 "Group the words"
  shorthand, ES P3 "587 candidaturas", and the DE/FR/IT/KO/PT items listed in the verdict tasking).
- The RU pair-185 bracket fix and the P7 deferral-disclosure wording were not touched.

## Re-render + re-gate results

Re-render: `hidden_files/w46/zh-tw-fix/render_all.sh` (run.py + render.py, tools venv),
2026-11-03, exit 0 for all 10 editions. Every edition: TOTAL 150; levels A2 44 / B1 74 /
B2 32; pages 10/18/18/18/18/18/12/38; types 單選 67 / 完成句子 54 / 配對 16 /
完形單選 12 / 寫作 1. Zero FLOW OVERFLOW / HEAD TOO WIDE / WRAP WIDTH warnings in all
10 logs (`render-<code>.log`, `render-all-summary.log`). Web PDFs rebuilt with
`tools/webpdf.py` only and text.md regenerated from each edition's own SVG text layer
with the existing H1 preserved verbatim (`webpdf_textmd.sh`, `webpdf-textmd.log`, all rc=0).

Gates: `hidden_files/w46/zh-tw-fix/gates_all.sh` + `gates_rest.sh` (the first driver was
killed mid-run by the runtime after the nl occlusion step; the remainder was re-run as a
fresh job — no gate was skipped or re-run to a different result). Gate JSONs/txt under
`hidden_files/w46/zh-tw-fix/gates/`; combined log `gates/gates.log`.

- **Freeze baseline (core):** `freeze.py baseline` — 8/8 SVGs byte-identical
  (`freeze-baseline.log`); shipped core SVGs unchanged by the run.
- **Freeze diff (`--strict-cjk`) per edition:**
  de/es/fr/it/nl/pt/ru rc=0, TOTAL added CJK characters 0. ja rc=1, total 6445;
  ko rc=1, total 5267 — both outputs byte-identical to the Round 1 freeze files
  (verified by diff), i.e. the adjudicated Round 1 state: the added characters are
  reader-native Japanese/Korean script plus quoted CJK terms, not new target text. No
  fix added CJK to ja/ko (D4 is a digit change; D1/D2/D3/D5 do not apply to ja/ko).
- **p8.py:** core extract 150/150; all 9 compares CLEAN, 150 noted both, missing=[],
  extra_count=0, uncertain=[], keydiff=[] (`p8-<code>.json/txt`).
- **Occlusion audit:** selftest OK in every run (all 6 planted classes fired, clean
  controls silent); 0 flags in every edition; 0 NEW vs core in every edition
  (`occlusion-<code>.json/txt`, `occlusion-new-<code>.json/txt`).
- **Counts re-measured:** 150 in every render log (per-page and level splits above).
  P7 phrases: all 8 quoted phrases at exactly 2 occurrences in all 10 editions
  (concatenated SVG text nodes, full-width rendered forms).
- **Simplified-residue scan:** spot list (邮 说 国 龙 马 发 观 欢 对 让 认 识 语 学 读 书
  报 纸 电 话 车 门 问 间 见 风 云 气 头) — 0 hits in the core CJK set; the Latin
  editions add 0 CJK (freeze) so they are clean by subset; ja/ko freeze output is
  identical to Round 1.
- **Final-artifact sweeps (SVG + text.md):** badge fill #3e4c2a in all 10 P1 SVGs;
  "19座城市" 0 / "3座城市" 1 in every final SVG set and text.md; the D1 English
  glossline survives only in the core (0 in de/es/fr/it/pt); the D2 English note
  survives only in the core (0 in de/fr); FR P4 gloss lines contain whole "Tianmu"
  (no split fragments); text.md H1s preserved verbatim in all 10.
- **D5 geometry + pixels:** SVG teaser bottoms en 2573.86 / de 2530.84 / es 2573.86 /
  fr 2573.86 / it 2557.36 / ja 2529.86 / ko 2529.86 / nl 2572.36 / pt 2557.36 /
  ru 2562.84 — all clear of the 2580 footer rule. 1:1 pixel strips
  (`strips/p7-teaser-{en,es,fr,nl}.png`, `strips/STRIP-MEASUREMENT.txt`): last
  full-dark row 2572 (en/es/fr) / 2571 (nl), 0 dark pixels at footer-rule row 2580.
- **Visual QA at full frame (21 cards viewed):** P6 ×10 (D4 line correct, no overflow);
  P5 ×5 (D1 translated glossline in each reader language, no English residue, no
  overflow); P8 ×2 (D2 translated note 134, neighbours intact); P4 fr (D3 gloss reads
  whole words, no splits); P7 ×3 (D5 teaser clear of the footer rule, no text ink
  touched). No other visual defect was found on these pages; nothing else was changed.
- **Web PDFs:** every web PDF ≤ 7 MB; pdftotext bytes > 0 on every web PDF and
  byte-identical to the print PDF's extracted text (see inventory below).

## Final per-edition file inventory

| ed | text.md (bytes) | web PDF (bytes) | pdftotext (bytes, print = web) | print PDF (bytes) | print SHA-256 (first 16) | web SHA-256 (first 16) |
|----|----------------|----------------|--------------------------------|-------------------|--------------------------|------------------------|
| en | 46,350 | 2,008,249 | 45,561 | 14,116,006 | 68d7f9d4d34a7fd6 | d54c2e57db1be0d5 |
| de | 47,681 | 2,133,642 | 46,879 | 16,798,216 | 7384659c67522cdf | e0c8ea5a73b349e87 |
| es | 47,926 | 2,116,602 | 47,147 | 16,402,001 | f2a9a6d3fe6d0fbe | d787f1670f40185d |
| fr | 48,653 | 2,073,427 | 47,899 | 15,630,984 | e884c9e5e81ef25b | 93cd034644f28aaf |
| it | 47,324 | 1,982,279 | 46,541 | 14,083,148 | e3c4edbe526aa0d7 | ceb15c347595475e |
| ja | 51,992 | 2,208,932 | 51,271 | 12,005,689 | 37674a87b94a1212 | e8c2d34519a20686 |
| ko | 50,130 | 1,891,878 | 49,384 | 10,063,572 | ef3a2547e59eafaf | 7e1542719e8510d8 |
| nl | 46,800 | 1,990,345 | 45,996 | 14,476,823 | 295271cb313dade0 | b2b5de57e11a3053 |
| pt | 47,298 | 2,075,639 | 46,523 | 15,632,996 | ad62003b7e54ed1b | 776c892766c7a806 |
| ru | 59,161 | 1,700,024 | 58,354 | 8,837,523 | 745e8668ddb5eaab | b67a80292092313c |

Full SHA-256 values are recorded in each edition's KIT fix record (补记, 2026-11-03).
Note: core pdftotext is 45,561 bytes vs the pre-fix KIT's 45,562 — exactly the one
byte removed by the D4 digit change ("19" → "3").

## KIT fix records

A 补记 fix record (defects, before/after quotes, re-gate evidence, final file
sizes/SHAs) was appended to all 10 KITs (core + 9 fan-outs). In the same pass the
false badge lines in the de/es/fr/it/pt KITs ("BRICK #a4553a") were corrected to
the rendered truth (OLIVE #3e4c2a). The RU pair-185 history, the deferral-disclosure
wording, and the core KIT's lesson-20 parenthetical were not touched.

## What was NOT applied as specified

Nothing was left unapplied. Two specification gaps are recorded honestly:

1. The verdict file itself (`hidden_files/w46/zh-tw-proofread-gates/proofreader-verdict-round1.md`)
   does not exist on disk; the work proceeded from the tasking's quoted defect specs, each
   re-verified against artifacts and sources before fixing (see the note at the top).
2. D1 had no approved de/es/fr/it/pt translations in the translation tables (pair 254
   covers only ja/ko/nl/ru); the five translations were authored to match each edition's
   own P2 glossline label and 算一算 gloss conventions, and are quoted verbatim above
   for Round 2 to judge.
