# Proofreader verdict — Lucerna Weekly W46, EN target, round 1

- Issue week: Mon 2026-11-09 – Sun 2026-11-15. VOL.3.
- Scope: 11 editions — `2026-w46-en-de, -es, -fr, -it, -ja, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw`.
  The `files/weekly-report-w46-en-core/` directory IS the zh-cn edition (its KIT: reader language
  Simplified Chinese, slug `2026-w46-en-zh-cn`); there is no separate `weekly-report-w46-en-zh-cn/` folder.
- Role: independent proofreader. No edition file was fixed, re-rendered, or edited.
  No subagents. Nothing pushed, inserted, or posted.
- Gate workdir: `hidden_files/w46/en-proofread-gates/` (freeze/p8/occlusion JSONs + logs,
  `texts/`, `diff-*.txt`, `batch-checks.log`, `checks2.log`, `rowcheck.log`, `koscan-en-ko.log`,
  `leftover-check.log`, `masthead-pixels*.log`, `visual/`).

## Verdict

**ROUND 1 FAIL** — blocking defects in all 11 editions (see §1). No edition is shippable as rendered.

Per-edition verdicts (B = blocking, M = minor; O = observation, not counted):

| Edition | Verdict | Blocking | Minor |
|---|---|---|---|
| en-zh-cn (core) | FAIL | B4, B5 | — |
| en-de | FAIL | B4 | M1, M3 |
| en-es | FAIL | B1, B4 | — |
| en-fr | FAIL | B4 | M1, M2 |
| en-it | FAIL | B4 | — |
| en-ja | FAIL | B4 | — |
| en-ko | FAIL | B2, B3, B4 | M2 |
| en-nl | FAIL | B4 | M4 |
| en-pt | FAIL | B1, B4 | M4 |
| en-ru | FAIL | B1, B4 | — |
| en-zh-tw | FAIL | B4, B5, B6 | M2 |

## 1. Blocking defects

### Frozen-core defects (fix in the core; re-render propagates)

**B4 — Lone closing guillemet `»` alone on a line, P7 toolbox, ALL 11 editions.**
The B1 toolbox sentence wraps so its closing `»` sits by itself on a line.
Evidence (SVG text extraction, identical in all 11 `texts-*.txt`):
`[p7-langue#66 x=1451 y=477.3] »`, between `[p7-langue#65 x=1451 y=443.1] B1 — « Dickens wrote the story in 1843.`
and `[p7-langue#67 x=1451 y=544.0] B2 — « Nobody knows whether this year will be faster. »`.
The sentence is `« Dickens wrote the story in 1843. »`; the closing quote orphaned onto its own
line. Fix: re-break the B1 toolbox sentence in the frozen core so `»` stays with `1843.`
(or the sentence reflows). Kinsoku/orphan class; visible stray glyph.

**B5 — Lone `。` alone on a line, P7 editor's-note paragraph, core (zh-cn) + zh-tw only.**
Evidence (identical coords in both): `[p7-langue#158 x=1013 y=2132.0] 。`, following
`[p7-langue#157 …] 投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.4 起刊登收到的真实来信`
(core) / `…真實來信` (zh-tw). The other 9 editions re-wrap the native note so the period attaches.
Fix: re-break the editor's-note paragraph in the core Chinese source and in the zh-tw source.

### Edition-specific blocking defects

**B1 — "HOW LONG?" glossed as a bare noun phrase (term of office, no question form), P6 box title: es, pt, ru.**
See §3 (HOW LONG verdict) for full evidence. Rendered: es `HOW LONG? · El mandato`,
pt `HOW LONG? · O mandato`, ru `HOW LONG? · Срок полномочий`. The box asks how long each
office's term is; the gloss must be a question. Proposed: es `¿Cuánto dura el mandato?`,
pt `Quanto dura o mandato?`, ru `Каков срок полномочий?`. Fix in the 3 fan-out build sources
(`weekly-report-w46-en-es/pt/ru-build/content56.py:166`); the frozen core is correct.

**B2 — en-ko ABSTRACT.txt typo: `댦` for `뮌` (Munich).**
`ABSTRACT.txt`: `… 11월 15일 일요일 NFL 댦헨 경기 …`. Codepoints: rendered `댦` U+B326;
correct `뮌` U+BB8C (`뮌헨` = Munich). The edition body uses correct `뮌헨` everywhere
(P4 title, P8). The abstract feeds frontmatter/SEO via insert.py, so the typo ships to readers.
Fix: one character in `files/weekly-report-w46-en-ko/ABSTRACT.txt`.

**B3 — en-ko mid-word syllable splits (S3, tail ≥ 3 syllables), P8, ×2.**
Koscan (canonical 10–45 window) + source adjudication:
- S3 #1: P8 y=1961.91→1982.06, `솔 | 퍼드에서` (tail 4 syllables). Source
  `content56.py:37` key `갈라쇼는 솔퍼드에서 생방송돼요` (Salford) — one word split.
- S3 #2: P8 y=2143.26→2163.41, `묵 | 념해요)` (tail `념해요` = 3 syllables). Source
  `content8.py:63` key `전교생이 2분간 묵념해요` — one word split.
The other 13 true splits have 1–2-syllable tails (below the S3 ≥3 standard, README lesson #16);
orphan final lines (≤1 syllable): 0. Fix: re-break the two P8 lines in the ko build.

**B6 — Lone `。` alone on a line, P2 bridge, en-zh-tw only.**
Evidence: `[p2-life#161 x=527 y=2067.225] 。` in `texts-zh-tw.txt` only — the final `。` of the
`B · WILL` bridge `用 will + 動詞原形改寫（承諾與將要發生的事）` wrapped alone. The core P2 wraps
the same bridge without the orphan. Fix: re-break the bridge in the zh-tw source.

## 2. Minor defects (fix in the same round)

**M1 — FINAL TEST header keeps the English instruction with no native equivalent: de, fr.**
P8 header, rendered: de `FINAL TEST · Abschlusstest · Answers at the bottom of this page`
(no German); fr `FINAL TEST · Test final · Answers at the bottom of this page` (no French).
The other 9 editions keep the English AND add the native line (es `· Las respuestas están al
final de esta página`, it `· Le risposte sono in fondo a questa pagina`, ja `解答はこのページの下に`,
ko `· 정답은 이 면 아래쪽에`, nl `· Antwoorden onderaan deze pagina`,
pt `· As respostas estão no final desta página`, ru `· Ответы внизу этой страницы`,
zh-cn/zh-tw `答案在本版下方`). Untranslated instruction line; SOP requires native-language
explanations. Fix: add the native tail in de/fr.

**M2 — Doubled gloss prefix on P2–P6 gloss boxes, rendered identically twice: fr, ko, zh-tw.**
- fr: `Note | Note | a silence = …` (P2+; P1 uses single `Note |`). FR KIT §furniture documents
  gloss prefix `Note | ` (single). W45 EN×FR shipped single `Note |` on all pages — regression.
- ko: `해설 — 해설 — a silence …` (P2+; P1 single `해설 —`). KO KIT documents `해설 — ` (single).
  W45 EN×KO shipped single `해설 —` — regression.
- zh-tw: `譯注｜譯注｜a silence …` (P2+; P1 single `譯注｜`). ZH-TW KIT documents `譯注｜`
  (single); W45 EN×ZH-TW shipped the distinct pair `譯注｜講解｜` — the W46 rendering collapses
  both halves to the same word.
Accepted variant: de `Anmerkung | Erklärung |` (two DISTINCT labels, matching the core's
doubled `译注｜讲解｜` convention and the W45 zh-tw distinct-pair precedent).
Single-prefix editions es/it/ja/nl/pt/ru are clean. Fix: drop one half in fr/ko; restore
`譯注｜講解｜` in zh-tw.

**M3 — en-de "call a race" rendered imprecisely, P6 gloss box + P8 note 95.**
Rendered (both places): `call a race = ein Rennen entscheiden` (`texts-de.txt` P6 #74,
P8 #247). "Ein Rennen entscheiden" = to decide (the outcome of) a race; the election term is
to announce/declare the result. The core gloss is `宣布竞选结果` (announce the election result)
and the other 9 editions all render "announce the result" (fr `annoncer le résultat de
l'élection`, es `anunciar el resultado`, it `proclamare il risultato`, nl `de uitslag
bekendmaken`, pt `anunciar o resultado da eleição`, ru `объявить итоги выборов`,
ja `選挙結果を発表すること`, ko `선거 결과를 발표하다`, zh-tw `宣布競選結果`).
Proposed: `das Ergebnis verkünden` / `den Wahlausgang verkünden`. Minor: intelligible in
context, but the odd one out and weaker than the election-specific rendering everywhere else.

**M4 — P3 article title drops the English title entirely: nl, pt.**
Rendered: nl `DE NACHT VAN SCROOGE`, pt `A NOITE DE SCROOGE` (the `SCROOGE'S NIGHT · …`
element replaced wholesale). The other 9 editions keep the English title plus the gloss
(e.g. de `SCROOGE'S NIGHT · Scrooge-Nacht`, ru `SCROOGE'S NIGHT · Ночь Скруджа`).
The translations are correct; the English article title is lost from the header. Minor inconsistency.

## 3. HOW LONG verdict (builder-flagged item — ADJUDICATED)

**Builder claim: REFUTED as stated. The real defect is narrower: 3 editions, not 11; not frozen-core; not P7/P8.**

What the source actually asks (frozen core, `hidden_files/weekly-report-w46-en-build/content56.py:166`):
box `v6.box("HOW LONG? · 任期多长？", ["House: 2 years, all 435 seats each midterm. Senate: 6 years,
about a third each election. President: 4 years. Governor: usually 4 years."])`.
The box is about **length of term per office**. The separate sentence "How long did the last midterm
take?" (`content56.py:110`, chart intro, about counting duration) is different frozen body text
with no gloss. The core gloss `任期多长？` ("How long is the term [of office]?") is a CORRECT
question-form gloss for this box.

Occurrences: `HOW LONG?` appears ONLY as the P6 box title (P6 element, y=703) in every edition.
Grep of all extracted SVG texts found NO P7/P8 occurrence. The KIT flag's "P7/P8 gloss" location is wrong.

Rendered P6 glosses, all 11:
- core 任期多长？ ✓ question | de `Wie lange im Amt?` ✓ | es `El mandato` ✗ noun phrase |
  fr `Quelle durée?` ✓ | it `Quanto dura?` ✓ (kept-it.json's longer `Quanto dura il mandato?`
  is shortened on the page; still a correct question) | ja 任期はどれくらい？ ✓ |
  ko 임기는 얼마나? ✓ | nl `Hoe lang?` ✓ | pt `O mandato` ✗ noun phrase |
  ru `Срок полномочий` ✗ noun phrase | zh-tw 任期多長？ ✓ question.
- 8 of 11 are correct question forms. The core is correct, so this is NOT a frozen-core defect
  and NOT a fix-all-11 item.

The 3 noun-phrase renderings lose the question form: a learner reading `HOW LONG? · El mandato`
learns "how long = the mandate". Proof of the house convention: the sibling question title
`WHY MUNICH?` is rendered as a full question in all three
(`¿Por qué Múnich?`, `Porquê Munique?`, `Почему Мюнхен?`).
Provenance: the noun-phrase strings sit in the fan-out build sources
(`weekly-report-w46-en-es/pt/ru-build/content56.py:166`), NOT in the core source and NOT in
`hidden_files/w46/kept-*.json` or `authored-*.json` (searched) — the exact upstream route is
UNVERIFIABLE; the fix belongs in the 3 editions' sources regardless.
Correct renderings (proofreader proposals): es `¿Cuánto dura el mandato?`;
pt `Quanto dura o mandato?`; ru `Каков срок полномочий?`.

## 4. Masthead pixel check (all 11, cards 1950×2700, same coords as SVG)

Method: dark-ink scan of the masthead band, x restricted to [60,1890] (page-frame rules at x=26/1923
excluded), rule rows dropped, corroborated by per-row glyph analysis and visual crops.
Masthead element: P1 text #4, baseline y=330 (core/de/ja/ko/nl/zh-tw) or y=338 (es/fr/it/pt/ru),
centre-anchored x=975. Content-block edges: 65 / 1885.

| Edition | Size | Ink x-range | Clearance to 65/1885 | Result |
|---|---|---|---|---|
| zh-cn (core) | 46pt | 561–1387 | ~496 | FITS |
| de | 46pt | 134–1815 | ~69 | FITS |
| es | 46pt | 154–1795 | ~89 | FITS |
| fr | 42pt | 89–1861 | ~24 | FITS — reproduces the builder's claimed 89–1861 exactly; real clearance, no overflow. The 42pt reduction is CONFIRMED necessary and sufficient. |
| it | 46pt | 65–1885 (glyph rows 65–1880) | 0–5 | FITS, marginal — flush to the block edges but does NOT cross the frame lines (~26/1923); no clipping in crop. Observation O1, not an overflow defect (no ≥16px clearance rule exists in the SOP). |
| ja | 46pt | 476–1473 | ~411 | FITS |
| ko | 46pt | 580–1369 | ~389 | FITS |
| nl | 46pt | 226–1722 | ~161 | FITS |
| pt | 46pt | 123–1826 | ~58 | FITS |
| ru | 46pt | 136–1814 | ~71 | FITS |
| zh-tw | 46pt | 561–1387 | ~496 | FITS |

No masthead overflow in any edition. Visual: FR P1 and IT P1 viewed full-frame; IT masthead crop
viewed — glyphs stop just inside the frame lines.

## 5. Gate outputs summary

- **Freeze** (`tools/freeze.py diff`, core SVG vs each edition SVG): exit 0, all 11. Added CJK = 0
  for all Latin editions; ja 2,188; ko 2,381; zh-tw 679 — exactly matching KIT claims.
  Latin P8 shows 2 residual CJK-counted chars: U+FF1B fullwidth semicolons inside frozen key
  strings (e.g. de P8 `at 11 a.m.；two minutes of silence`); added CJK = 0, NOT a defect.
- **P8** (`tools/p8.py compare --total 150`): core 70 noted; CLEAN editions (es/it/ja/ko/pt/ru/zh-tw)
  70→70; EXTRA_ONLY editions (de/fr/nl) 70→150 with identical extra lists (80 numbers) and
  keydiff `[137,138,139,140,150]` in all 10 fan-outs — exactly matching KIT claims.
  Keydiff adjudication: 137–140 are translation keys (registry type 翻译; keys are the native
  translations, legitimately re-aimed per reader language in EXTRA_ONLY editions) and 150 is the
  open writing pointer — legitimate redirects, no missing notes. Missing = [], uncertain = [].
  (Note: default `--target en` uses stale total=149; the `--total 150` runs are authoritative.)
- **Occlusion** (`tools/occlusion_audit.py`, selftest OK every run): 0 flags in all 11 editions.
- **Rowcheck** (`hidden_files/w46/rowcheck46.py`): 80 CLEAN (10 editions × 8 pages), 0 COLLIDE;
  P6 chart-label GRAZE coverage 0.0% everywhere (P6 "chart" is text rows, no bars — per core KIT);
  gloss counts OK everywhere.
- **Registry re-measured**: 150 entries, numbers 1–150 unique, no missing/dup; levels A2 60 / B1 69 /
  B2 21; per-page 10/17/18/18/18/18/12/39. Confirms KIT.
- **P7 golden sentences**: all 8 verified verbatim contiguous excerpts from the cited pages:
  (1) P1 "On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens
  across the English-speaking world." (2) P1 "At 11 a.m. on November 11, 1918, the guns of the
  First World War fell silent." (3) P2 "For two minutes, nobody speaks." (4) P3 "Christmas is
  still six weeks away." (5) P4 "One Sunday is not enough — good thing the week has seven days."
  (6) P5 "The total will still be there in the morning — and so will the kindness."
  (7) P6 "Patience is part of the system, not a failure of it." (8) P6 "There were no results to
  print — and this paper invents none." The toolbox/level-example sentences are teaching
  constructs, not part of the 8; their "(page N)" citations denote topic source.
- **P1 Searches bars** (measured rects, all 11 identical): widths 250/218/186/140/108 px, strictly
  decreasing in label order 1–5 (olive #3e4c2a first, tan #b3a06a rest), labelled as relative
  snapshots, not exact volumes.
- **PDFs**: every web PDF 8 pages (`pdfinfo`), ≤7 MB (1.55–2.20 MB), `pdftotext` bytes > 0
  (44,913–50,969), web-extraction byte count equals print-extraction byte count per edition.
  Every `ABSTRACT.txt` single-line, no ASCII double-quote, reader-native, naming real topics +
  masthead + levels + 150 — except B2 (ko typo).
- **Badge/footer**: pairing badge present in P1 and footer on all 8 pages in every edition.
  (FR badge "miss" in an early check was a curly-apostrophe U+2019 artifact in `L'ÉDITION`.)
  Core footer: `The Lucerna · 英语周报 VOL.3 · LUCERNA ENGLISH WEEKLY`.
  The frozen tagline `THE LEARNERS' WEEKLY — …` (core P1 #5, y=372) is replaced in fan-outs by
  the pairing badge in the same slot — adjudicated NOT a defect (badge substitution per SOP;
  the core's pairing is conveyed by its native masthead + top line + footer).
- **Image credits**: all 5 credits (Claude Monet, Horace Nicholls, John Leech, Frank R. Snyder,
  Kenneth C. Zirkel) present in SVG texts of all 11 editions.
- **Script/provenance scans**: Latin editions 0 Han/Hangul/Kana/Cyrillic; ja Han+Hiragana+Katakana
  only; ko Hangul only (0 Han); ru Cyrillic only; zh-tw Han only. zh-tw SC-residue: 0 hits with
  the KIT scan set AND a broader SC-only set, in rendered texts and source literals (early `作`
  hits are shared SC/TC glyphs, not SC-only). ko: 0 new Han literals (1 identical-to-core
  svglib.py alt-text string mentioning 重阳, not rendered); zh-tw: 38 distinct identical-to-core
  literals, all shared-glyph, 0 SC-residue. KIT provenance claims CONFIRMED for both.
- **Dates/weekdays** (verified with `TZ=America/Toronto date -d`): 3 Nov Tue, 5 Nov Thu, 8 Nov Sun,
  9 Nov Mon, 11 Nov Wed, 12 Nov Thu, 13 Nov Fri, 14 Nov Sat, 15 Nov Sun, 16 Nov Mon, 20 Nov Fri,
  21 Nov Sat, 22 Nov Sun, 27 Nov Fri, 1 Dec Tue; 1918-11-11 Mon, 1920-11-11 Thu; 2022 Senate
  decided Sat 12 Nov, House Wed 16 Nov. All core KIT weekday claims correct.
  Spot-verified externally: Mississippi + Georgia general-election runoffs Dec 1, 2026
  (NewsNation; Downballot calendar; Georgia SOS); state certification window Nov 10 – Dec 18
  (earliest ~Nov 10; Georgia runoff certification by Dec 18 — Kalshi); England v Croatia
  Thu Nov 12, 7:45pm, Wembley and Spain v England Sun Nov 15, 7:45pm GMT, Metropolitano, Madrid
  (England Football/FA fixture confirmation).
- **Model text**: P8 MODEL "My Wednesday, November 11" counts 87 whitespace tokens as rendered
  (84 excluding the two numerals `11,`/`26` and the standalone em-dash) — the KIT's "84 words"
  reproduces only under that exclusion; the 80–100-word brief is met under any convention.
  Observation O4, not an edition defect.
- **Counts**: 150 exercises/edition; P6 chart is text rows (no bars to measure — consistent with
  the 0.0% GRAZE result and the core KIT).

## 6. KIT claims adjudication (summary)

- Core KIT (§3 dates, §6 promises, 150 counts, levels, P8 start 112, dialogue 145–149, writing 150,
  8 golden sentences, PD/CC0 images, press time Nov 2, no invented Nov 3 results): CONFIRMED,
  except the model-text count convention (O4) and defects B4/B5 (which the KIT does not mention).
- Fan-out KITs: freeze/P8/occlusion/badge/abstract claims CONFIRMED in all 10, except:
  fr 42pt masthead claim CONFIRMED (89–1861 reproduced); P8 conventions CONFIRMED; ko authored-ko
  provenance CONFIRMED; zh-tw authored-zh-tw provenance CONFIRMED; HOW LONG flag REFUTED as stated
  (see §3); gloss-prefix furniture claims CONTRADICTED by the rendering in fr/ko/zh-tw (M2);
  FINAL TEST translation not claimed in de/fr KITs but the rendering leaves the instruction
  untranslated (M1).
- W45 promises: honoured as disclosed deferrals — Veterans Day ✓ (P1/P2), NFL Munich Sun Nov 15 ✓
  (P4), midterm-results reporting carried to VOL.4 by necessity (press time Nov 2, before the
  Nov 3 vote; P1/P6 state plainly that no results exist and none are invented, and P6/P7 print
  the VOL.4 verified-results promise in all 11 editions), real readers' letters conditional on
  receipt (P7 editor's note in all 11: none arrived, example honestly labelled, no invented
  reader name/city — a tightening vs W45's "M. L., Chicago" persona; VOL.4 will publish real
  letters if received). Other families' W45 promises (DE Volkstrauertag, FR Senate/Dieppe, ES
  Nov 13/29, JA Japan Series, PT Enem, RU RPL, ZHCN S16/Double 11) belong to other targets and
  are correctly NOT imported into the EN editions. The ES Nov 12 negative promise is ES-only.

## 7. Native-language correctness (diffs read in full, all 10 fan-outs + core text)

Every explanation, gloss, note, abstract and footer is in the reader's native language; no
untranslated English strings remain beyond the adjudicated items (M1; the kept English heads,
titles, and the P8 dialogue/frozen body, which are the English being taught).
Per-edition notes (all other strings judged correct/acceptable; terse heads and documented W45
conventions accepted):
- de: doubled prefix is two distinct labels (accepted); `will still = wird weiterhin` correct;
  FINAL TEST untranslated (M1); `#95 call a race` imprecise (M3); P8 `#103 is = ist weiterhin`
  follows the frozen is+still pattern (accepted, P7 note explains).
- es: clean apart from B1; `to call a race = anunciar el resultado` ✓; `will still = todavía
  seguirá` ✓; `challenge yourself = acepta el reto` ✓; FINAL TEST translated ✓.
- fr: clean apart from M1/M2; tu/vous split KIT-adjudicated (vous instructions, tu personal
  address) — accepted; `call a race = annoncer le résultat de l'élection` ✓; level line
  "ta semaine" is a contents label, not flagged.
- it: clean; masthead flush (O1); `call a race = proclamare il risultato` ✓; `fu definito`
  slightly awkward but intelligible — accepted.
- ja: clean; FINAL TEST tail glued to the English with no separator (`…page 解答は…`) — minor
  typographic point, recorded here, not counted; mixed 〜なさい/〜よう forms KIT-adjudicated —
  accepted; `will still = 今でも〜するだろう` ✓; `to call a race 選挙結果を発表すること` ✓.
- ko: clean apart from B2/B3/M2; `challenge yourself = 도전에 응하다` ✓; tight
  `word( gloss)` parenthesis spacing is consistent KO house style — not flagged.
- nl: clean apart from M4; single `Uitleg —` prefix ✓; `call a race = de uitslag bekendmaken` ✓;
  `will still = zal nog steeds` ✓; `challenge yourself = ga de uitdaging aan` ✓.
- pt: clean apart from B1/M4; consistently European Portuguese (tu forms, `cerimónia`,
  `Desporto`, `Macedónia`, mesoclisis) — KIT silent on variety; internal consistency accepted;
  `call a race = anunciar o resultado da eleição` ✓; `will still = ainda continuará` ✓.
- ru: clean apart from B1; consistently informal ты address ✓; `call a race = объявить итоги
  выборов` ✓; `will still = всё ещё будет` ✓; `challenge yourself = прими вызов` ✓;
  `of = родительный падеж` an acceptable explanation of "of" ✓.
- zh-tw: clean apart from B5/B6/M2; conversions fully Traditional with Taiwan usage (`比數`,
  `《飢餓遊戲》`, `搜尋量`, `週`) and 0 SC residue; `will + 動詞原形` clarification is an
  improvement; `收官戰` acceptable (Go-derived term used in Taiwan sports coverage too).
- core (zh-cn): English body correct throughout; dates, fixtures, and election mechanics
  verified as in §5; P5 "two miles a day for two weeks" vs the 26-box "adds up to 26"
  (13 vs 14 days) is hedged by "more or less"/"about" — observation O5.

## 8. Observations (not defects)

- O1: IT masthead flush to block edges (0–5px clearance, no overflow/clipping). See §4.
- O2: P8 key-flow wraps starting with `）`/`；`, and the P8 dialogue wrap starting `! See you
  on…`, are frozen wrap-aware conventions identical in the core — not defects.
- O3: P1 contents line labels p.2 "Silence, poppies & Pudsey" though Pudsey's story is p.5
  (p.2's own header is "Silence, poppies & your week"; p.5 contents correctly lists Pudsey).
  Frozen-core label quirk; not counted.
- O4: Model-text word count convention (see §5).
- O5: P5 arithmetic looseness (see §7, core note).
- O6: FR tu/vous + "ta semaine" — KIT-adjudicated, accepted.
- O7: PT European Portuguese variety — consistent, accepted.
- O8: Tagline/badge substitution — adjudicated, not a defect.
- O9: Frozen-English house spacing before `!`/`:` (e.g. `SILENCE !`, `Reading level : A2`) —
  consistent throughout, accepted as style.
- O10: P4 "The weekend starts on Sunday — and it does not stop" is vague phrasing after the
  Ashes paragraph; intelligible in context, not counted.
- O11: JA FINAL TEST tail has no separator between the English and Japanese (see §7, ja note).

## 9. Visual pass

Cards viewed at full frame (975px reductions of the shipped 1950×2700 `cards/*.png`,
rendered within a minute of their SVGs): P1 of all 11 editions (FR P1 and IT P1 viewed
2026-11-02; core/de/es/ja/ko/nl/pt/ru/zh-tw viewed 2026-11-03) and P8 of all 11 editions.
No overflow, no overlap, no tofu/missing glyphs, no missing image credits on any P1/P8.
The EXTRA_ONLY P8 answer areas (de/fr/nl, all 150 notes) are dense but contained within the
frame. P2–P7 are covered by the geometric gates (0 occlusion flags, 0 rowcheck collisions)
plus the spot visual checks below.

Spot checks (full-resolution crops, `visual/crop-*.png`):
- ZH-TW P2: lone `。` alone on its own line under the B·WILL bridge — B6 CONFIRMED visually.
- ZH-TW P7: lone `。` alone on its own line at the end of the editor's note — B5 CONFIRMED visually.
- Core P7: lone `»` alone on its own line under the B1 toolbox sentence (B2's closing `»`
  correctly stays with its sentence) — B4 CONFIRMED visually.
- FR P2: `Note | Note | a silence = le silence …` — M2 CONFIRMED visually.
- KO P8: `솔 | 퍼드에서` split (S3 #1) and `묵 | 념해요` split (S3 #2) both visible in the
  answer notes — B3 CONFIRMED visually.
- IT masthead crop (2026-11-02): glyphs stop just inside the frame lines — O1.

## 10. What the fix round must change (for the coordinator)

1. Core: re-break the P7 B1 toolbox sentence (B4) and the P7 editor's-note paragraph (B5, core half).
   Re-render all 11 (B4 propagates everywhere).
2. es/pt/ru builds: HOW LONG glosses (B1) — 3 strings, no core change.
3. ko: ABSTRACT.txt one character (B2); re-break two P8 lines (B3); gloss prefix (M2).
4. zh-tw: P7 editor's-note re-break (B5, zh-tw half); P2 bridge re-break (B6); gloss prefix (M2).
5. fr: FINAL TEST tail (M1); gloss prefix (M2).
6. de: FINAL TEST tail (M1); "call a race" wording ×2 (M3).
7. nl/pt: P3 title — restore `SCROOGE'S NIGHT ·` prefix (M4).
8. Re-run freeze/p8/occlusion + this proofread (round 2) after the fix; the B4 core re-break must
   be verified in all 11 (identical coords today — verify the orphan is gone everywhere, not
   just in the core).

**ROUND 1 FAIL**
