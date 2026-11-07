# Independent Proofread Verdict — Round 1
## Lucerna Weekly W46 (2026-11-09 – 2026-11-15), ES-target family, 11 editions

- **Proofreader:** independent, Round 1. The proofreader did NOT build these editions.
- **Scope:** all 11 ES-target editions, one per reader-native language: es-de, es-en, es-fr, es-it, es-ja, es-ko, es-nl, es-pt, es-ru, es-zh-cn, es-zh-tw.
- **Edition folders:** `files/weekly-report-w46-es-*/`. `files/weekly-report-w46-es-core/` is a stale artifact dir and was used only as the frozen-core reference, not as an edition.
- **Gate work dir:** `hidden_files/w46/es-proofread-gates/` (freeze/p8/occlusion JSONs, analysis scripts and outputs, `added/` layer dumps, `masthead-pixel.txt`, `masthead-letters.txt`).
- **Basis:** full SOP read; every edition WEEKLY-KIT.md read; frozen ES core build sources under `hidden_files/` (build dirs used by grep only — no content modules imported or executed); core `.text.md` (3043 lines) read in full; explanation layer of all 11 editions read in full via freeze added-strings dumps plus direct SVG greps; all gates re-run independently with the shared toolkit (`tools/freeze.py`, `tools/p8.py`, `tools/occlusion_audit.py`); P1 + P8 cards viewed full-frame for all 11 editions, plus KO P2/P4/P5 and DE P7; P2–P7 otherwise covered by geometric gates plus spot visual checks.
- **Gate rule:** proofread-until-zero is a hard shipping gate. This round found 5 blocking defects (4 in KO, 1 in DE). No frozen-core blocking defects were found.

---

## Per-edition verdicts

| Edition | Verdict | Blocking defects |
|---|---|---|
| es-de | **FAIL** | D-1 (P7 golden-sentence translation, ungrammatical German) |
| es-en | **PASS** | — |
| es-fr | **PASS** | — (KIT badge-size claim refuted as a minor KIT inaccuracy only; see M-2) |
| es-it | **PASS** | — |
| es-ja | **PASS** | — |
| es-ko | **FAIL** | D-2, D-3, D-4, D-5 (4 mid-word splits, README #16 standard) |
| es-nl | **PASS** | — |
| es-pt | **PASS** | — |
| es-ru | **PASS** | — |
| es-zh-cn | **PASS** | — (KIT "Added CJK = 0" wording misleading; substance confirmed; see M-3) |
| es-zh-tw | **PASS** | — |

## Blocking defects (5)

### Edition-specific

**D-1 — DE, P7 golden sentences (Q6), ungrammatical translation — BLOCKING**
- File: `files/weekly-report-w46-es-de/svg/p7-lengua.svg`, golden-sentences block, Q6.
- Spanish quote (frozen, correct): `«La vivienda preocupa al 86,9 % de los españoles.»`
- Wrong translation printed: `Die Wohnung sorgt 86,9 % der Spanier. (Página 6)` — German `sorgen` is intransitive/reflexive (`sich sorgen um`); the sentence cannot take an accusative object and is ungrammatical.
- Correct, e.g.: `Die Wohnungsfrage bereitet 86,9 % der Spanier Sorgen.` or `86,9 % der Spanier sorgen sich um die Wohnung.`
- Evidence the correct construction is known to the builder: DE P8 answer 127 reads `CIS-Wohnungsbarometer: 86,9 % sorgen sich um die Wohnung` (correct).
- Cross-edition check (grep for `86[,.]9` in all P7 SVGs): all other 10 editions translate Q6 correctly (EN `Housing worries 86.9% of Spaniards.`; FR `Le logement inquiète 86,9 % des Espagnols.`; IT `La casa preoccupa l'86,9 % degli spagnoli.`; JA `住宅はスペイン人の86.9%を悩ませている。`; KO `주택 때문에 스페인 사람의 86.9%가 걱정해요.`; NL `Huisvesting baart 86,9% van de Spanjaarden zorgen.`; PT `A habitação preocupa 86,9% dos espanhóis.`; RU `Жильё беспокоит 86,9% испанцев.`; ZH-CN `住房让 86.9% 的西班牙人担心。`; ZH-TW `住房讓 86.9% 的西班牙人擔心。`). Confirmed visually on the rendered DE P7 card.
- Fix (builder): replace the Q6 translation, re-render, full re-proofread per SOP §8.4.

**D-2 — KO, P1 cifras box, word split `총|파업` — BLOCKING**
- File: `files/weekly-report-w46-es-ko/svg/p1-portada.svg`, cifras box, x=545, 20.5pt.
- Line y=1426.9: `miércoles 11 de noviembre (11월 11일 총` → line y=1454.6: `파업은 24시간이에요)` — `총파업` (general strike) split with a 3-syllable tail (`파업은`). Confirmed visually on the rendered KO P1 card.

**D-3 — KO, P2 calendar, word split `세|스타오` — BLOCKING**
- File: `files/weekly-report-w46-es-ko/svg/p2-vida.svg`, calendar, x=545, 21pt.
- Line y=887.5: `Federación en Sestao, 19:00 (토요일 세` → line y=916.1: `스타오에서 연방컵 결승)` — `세스타오` (Sestao) split with a 3-syllable tail (`스타오`). Confirmed visually on the rendered KO P2 card.

**D-4 — KO, P4 exercise instruction, word split `채|우세요` — BLOCKING**
- File: `files/weekly-report-w46-es-ko/svg/p4-deporte.svg`, exercise instruction, x=527, 20.5pt.
- Line y=2192.5: `괄호 안 단어의 비교급이나 -ísimo 형태로 빈칸을 채` → line y=2222.2: `우세요.` — `채우세요` split with a 3-syllable tail (`우세요`); same class as the README-cited `채|우세요`. Confirmed visually on the rendered KO P4 card.

**D-5 — KO, P5 exercise instruction, word split `나타|내세요` — BLOCKING**
- File: `files/weekly-report-w46-es-ko/svg/p5-juventud.svg`, exercise instruction, x=527, 20.5pt.
- Line y=2363.5: `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’을 나타` → line y=2393.2: `내세요.` — `나타내세요` split with a 3-syllable tail (`내세요`). Confirmed visually on the rendered KO P5 card.

- Common note for D-2…D-5: the builder's `es_ko_orphan.py` reported 0 because it implements only the S1 line-initial punctuation/particle + S2 ≤2-syllable-residue criteria (KO KIT §5 lines 43–45 document this). Under the binding tools README #16 orphan standard (window 10–45, line-initial orphan punctuation/particles AND mid-word splits with ≥3-syllable tails for EVERY prose column), the KO KIT §4–§5 claim "orphan scan 0 reports" is REFUTED as a complete orphan gate — true only under the narrower S1/S2 criteria. The independent scan found 12 candidates; 8 were adjudicated false positives (breaks at word boundaries after particles/words, e.g. `el salario는 | 월급이에요`, `두 | 문장`, `일을 | 멈춰요`). The 4 sites above are the real ones, all verified in full element context (same column, same size, consecutive wrapped lines).
- Fix (builder): reword/restructure these 4 lines so no word breaks with a ≥3-syllable tail, re-render, full re-proofread per SOP §8.4.

### Frozen core

**None.** The core text was read in full and all 150 answer keys were re-derived from stems/articles/charts — all check out. One item is weak but defensible, NOT a defect: P8 answer 132 key B `«Dos miércoles»` with note "标题概括两地对比" — the title does概括 the two people's Wednesdays (Madrid vs Barcelona); recorded here so a later round does not re-litigate it. Model text in P8 section H = exactly 84 words (whitespace-split count, `España–Inglaterra`/`Chequia–España` counted as single tokens as the builder did). P4 `EL DOMINGO 8` box states results unavailable — no invented scores. P5 postal-vote deadlines (apply by Thu 19 Nov, materials from Mon 9 Nov, polling stations 9:00–20:00 Sun 29, reflection day Sat 28) are consistent across article, plan box and exercises. P6 76.3% for both state intervention and the public housing company is consistent between article and chart (source data per KIT). `INFAMIA` 6-episode / Ledicia Costas plot details per KIT sources, not independently web-verified; no red flag, no defect invented.

---

## Minor / observations (non-blocking; coordinator to confirm)

**M-1 — KO P3 gloss separator deviation (not blocking).** The KO `gloss()` string splits on `·` into 4 items, not 5: `... el veranillo는 늦가을 따뜻한 날, la gaita는 백파이프 · el magosto는 밤 축제.` The rendered P3 gloss shows all 5 terms + glosses; only the veranillo/gaita boundary uses a comma. Disclosed in KO KIT §5. Deviation from the literal ·-count rule (tools README #21); no information lost. Do not fail KO on this alone (KO already fails on D-2…D-5).

**M-2 — FR KIT badge-size claim REFUTED (KIT inaccuracy only).** FR KIT line 16 claims a 20pt badge; measured 19.5pt bold, fill `#a4553a`, center-anchored x=975 — identical to the family standard (EN/JA/NL/PT/RU/ZH-CN/ZH-TW). Edition geometry is correct; only the KIT figure is wrong.

**M-3 — DE KIT byte-count claim REFUTED (KIT inaccuracy only).** DE KIT lines 11 and 37 claim 47,074 B; measured 47,056 B for both web and print PDFs, and web-vs-print `pdftotext` output is byte-identical. All other KIT byte figures matched measured values.

**M-4 — ZH-CN KIT wording clarification.** ZH-CN KIT "Added CJK = 0" is misleading under `freeze.py`'s per-page multiset definition (`cjk_added_total` = 134). Substance CONFIRMED: the freeze diff is exactly the 3 claimed deltas (P1 badge+footer replacing subtitle + core footer; P2–P7 footer only; P8 footer + 8 separators `— 第 N 版 —` replacing `— PÁGINA N —`), and added characters novel vs the whole core = 0. KIT line 28 clarifies the intended meaning; adjudicated CONFIRMED in substance.

**M-5 — Disclosure asymmetry, DE/NL/RU (observation for coordinator decision).** DE (`Anmerkung der Redaktion: Keine echten Briefe eingegangen — daher dieser Beispielbrief. Versprechen gilt für VOL.4!`), NL (`Opmerking: geen echte brieven; daarom een voorbeeldbrief. Belofte: VOL.4.`), RU (`Примечание: писем нет; печатаем пример. Обещание — на VOL.4.`) omit the "no best P8 texts" fact in the native note, explicitly relying on the frozen Spanish disclosure directly above in the same letters box (DE precedent cited by NL/RU; KIT claims accurate as stated — CONFIRMED as disclosed). EN/FR/IT/JA/KO/PT/ZH-TW carry the full native disclosure including best-P8-texts (e.g. EN `Editor's note: no real letters, no best page-8 texts; an editor's example is printed and the promise carries to VOL.4.`). The full disclosure IS on the page in Spanish, the native notes convey the operative facts (no real letters, example printed, promise to VOL.4), and letters-box geometry confirms the Spanish disclosure sits directly above each native note (see gate summary). Non-blocking.

**M-6 — Core ABSTRACT.txt framing (observation, core out of scope; do not fail editions).** The core ABSTRACT.txt wording `通过西班牙新闻学西班牙语` is arguably equivalent to the prohibited news-framing phrasing. All 11 editions' own abstracts are practice-framed and pass. Flagged for the coordinator only.

**M-7 — Frozen furniture `De la redacción de La Lucerna · Nivel de lectura: A2/B1` (observation, not a defect).** Occurs 10× identically in core and every edition, in Spanish (plus `De la redacción deportiva...` on P4). Evidence it is frozen core furniture: the ES core build transform log shows it was created by transforming English `Lucerna editors · Reading level A2→B1` into Spanish in the core build — analogous to explicitly frozen `Página N` / `— PÁGINA N —` furniture. Recorded as a family-wide observation for the coordinator; editions were NOT failed on it.

**M-8 — EN ABSTRACT.txt has no trailing newline** (trivial hygiene, not a defect). IT KIT byte counts were absent from the KIT (UNVERIFIABLE from the KIT; verified independently — 46,852 B, web = print, byte-identical).

---

## Gate outputs summary (all re-run independently)

**1. FREEZE — CONFIRMED, all 11** (`freeze-<code>.json`, `gates-run.log`; exit 0 all 11).
- Latin-script editions (de/en/fr/it/nl/pt/ru): added CJK 0 on every page; edition CJK total 0. RU Cyrillic 8273 chars (expected).
- JA: added CJK all Japanese; Simplified-only probe 0 hits except `写` U+5199 ×2 in `写真` (P7, opinion polls) — shared Japanese shinjitai form, NOT a defect. Full-width parens 58/58, no `“”`, no Simplified `说/让/对/为`.
- KO: added CJK all Hangul (3496); Hanzi 0; full-width parens 0.
- ZH-TW: 0 Simplified-only probe characters in absolute counts; Traditional markers present (說 16, 讀 11, 對 16, 國 7, 語 24, 體 14). Per-page CJK totals claimed in ZH-TW KIT line 30 (core 180/295/155/176/238/80/412/964 → edition 216/307/169/188/252/92/424/985) were NOT re-derived — UNVERIFIED; the 0-Simplified-only claim is CONFIRMED.
- ZH-CN: see M-4.
- P6 re-wrap: identical removed-string sets across de/en/fr/it/ja/nl/ru (16 Spanish exercise fragments, e.g. `Construir más vivienda pública lo apoya el...`, `El barómetro se hizo con... A. 6.019 entrevistas`). Non-CJK word-multiset check: lost = {} for all 7; gains are explanation/furniture words only. KO/PT show no such fragments (kept core P6 sizes). ZH-CN/ZH-TW show only subtitle/footer changes. Conclusion: re-wrap from P6 18.5pt reflow, not core-text edits.

**2. P8 — CONFIRMED, all 11** (`p8-<code>.json`): CLEAN, 150 noted = 150, missing=[], extra_count=0, keydiff=[137, 138], except zh-cn keydiff=[]. Keydiff [137,138] adjudicated as legitimate re-aiming: translation keys 137/138 re-aimed to reader language, bodies 139/140 re-aimed likewise; all other keys byte-identical. ZH-CN byte-identical answers (keydiff=[]) CONFIRMS its KIT. P8 answers 60–62/64 notes were already language-neutral in core (`dar → dio` etc.), so their absence from some added-strings dumps is expected, not a gap.

**3. OCCLUSION + CHART + SAME-BASELINE — CONFIRMED, geometric gates** (`occlusion-<code>.json`, `occlusion-core.json`, `occlusion-run.log`, `chart-ink.txt`, `same-baseline.txt`, `masthead-pixel.txt`, `masthead-letters.txt`).
- Canonical `occlusion_audit.py` (selftest passed: all 6 planted classes fired exactly once, clean controls silent): **0 flags for all 11 editions + core.**
- Chart (P6, SVG ink measurement via the tool's own `ink_box`, identical in all 12): bars start x=495 (chart 1) / x=1419 (chart 2); scale 3.2 exact (95.4%→305.28px, 86.9%→278.08px, 13.5%→43.2px). Minimum label-to-bar gaps 91.8px (chart 1 row 1) and 105.0px (chart 2). Value labels inside boxes (chart 1 ends ≤818.3 < 961; chart 2 ends ≤1715.1 < 1885). Rendered core P6 card viewed full-frame: charts legible, no overlap.
- Same-baseline scan (exact-y groups, true ink boxes, gaps <2px or overlap): **0 reports in all 12**. KITs' "7 rowcheck reports, all P1 contents 4.0px gaps" are positive gaps, not overlaps — consistent, no defect. Parse-regex sanity: 166/166 `<text>` elements parsed on DE P1, 0 unparsed.
- Masthead pixel/ink check: wordmark ink x=601.7..1348.4 in ALL 12 (identical, centered, 373px clear each side inside the 65..1885 content area). Top strip: left ends ≤374.2, center ends ≤1379.1, date line starts 1407.9 (gaps ≥28.8px); date ends 1884.9 ≤ 1885. No masthead clearance defect in any edition. RU KIT's own pixel measurement is consistent in substance (center ends 1293.4, date starts 1407.9 — 114.5px gap). Pixel edge scan: all 12 P1 cards 1950×2700, background cream, no ink touching the outer edge (26px clearance = the frame rule).
- P7 letters box: last disclosure baseline ≤1824.2 < box bottom 1833 in core/de/en/fr/ja/ko/nl/pt/ru/zh-cn/zh-tw (per-edition box bottoms: fr 1831, ja/pt 1804, ko 1776, nl 1832, ru 1827 — all inside); IT's box is taller (bottom 1863) and its 4th disclosure line sits at 1852.6, inside. Geometry CONFIRMED for all 11.

**4. COUNTS — CONFIRMED, re-measured** (`counts-p7.txt`, `level-pair.txt`, `level-pair2.txt`).
- Total **150 exercises** in every edition: 138 standalone-numbered stems (elements exactly `N.`) + 3 grouped matching sets of 4 (25–28, 52–55, 141–144) = 150. Stem sequences: P1 1–10; P2 11–24; P3 29–46; P4 47–51 + 56–64; P5 65–82; P6 83–100; P7 101–112; P8 113–140 + 145–150. Per-page: **10/18/18/18/18/18/12/38**.
- Level split via same-baseline chip pairing: standalone stems A2 46 / B1 68 / B2 24. Grouped sets carry section chips: 25–28 under `A2`, 52–55 under `B1`, 141–144 under `B2` (verified in core `.text.md`). Total: **A2 50 / B1 72 / B2 28**. Identical paired counts in all 12 editions. Standalone chip totals (49/72/26=147) include non-stem header/directory chips and must NOT be used as the split.

**5. P7 GOLDEN SENTENCES — CONFIRMED, all 8, all editions** (`quotes-all.txt`). All 8 Spanish quotes occur verbatim in exactly one article page and in P7, in core + all 11. Q8 tag `(Página 1)` correct. Translations 8/8 present per edition (verified in added-strings dumps for all 11). The 8 quotes: Q1 P1 `El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.`; Q2 P2 `El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.`; Q3 P3 `Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío.`; Q4 P4 `España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa.`; Q5 P5 `No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.`; Q6 P6 `La vivienda preocupa al 86,9 % de los españoles.`; Q7 P6 `Una encuesta es una foto con margen de error, tomada en un día concreto.`; Q8 P1 `El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.` — except that DE's Q6 *translation* is defective (D-1); the Spanish quote itself is verbatim and correct.

**6. BADGE + FOOTER — CONFIRMED, fill #a4553a (brick) measured in all 11** (`badge-measure.txt`).
- EN/FR/JA/NL/PT/RU/ZH-CN/ZH-TW: badge replaces y=372 subtitle slot, 19.5pt bold, fill `#a4553a`, center-anchored x=975. (FR KIT's 20pt claim refuted — M-2.)
- DE/IT/KO: badge INSERTED at y=574, 22pt bold, fill `#a4553a`; Spanish tagline retained at y=372 (fill #57523f). Matches KITs.
- RU name line 40pt measured (KIT claim CONFIRMED); all other name lines 46pt. Masthead `La Lucerna` (UnifrakturMaguntia 168pt, y=262) present in all. Footers: exactly one distinct pairing footer string per edition across all 8 pages.

**7. PDF + ABSTRACT — CONFIRMED** (web-vs-print `pdftotext` byte-identity `cmp`: IDENTICAL for all 12).
- All web PDFs: 8 pages, <7 MB (0.49–1.31 MB), `pdftotext` byte counts equal web vs print per edition: core 44826; de 47056; en 46063; fr 47517; it 46852; ja 48185; ko 48417; nl 46760; pt 46836; ru 54733; zh-cn 44933; zh-tw 44914. Print PDF sizes match KITs except DE (M-3). Byte-identity via `cmp` confirms the KIT byte-identity claims for all editions.
- ABSTRACT.txt: all 11 single-line, no ASCII double-quote, reader-native, masthead + VOL.3 + real topics (11 Nov strike, 13 Nov campaign, 29 Nov vote, postal vote, Nations League Spain–England, St Martin) + A2–B2 + 150 exercises + answers. Practice framing in all 11.

**8. READER-FACING SWEEP + DECREE DATE + CREDITS — CONFIRMED.**
- Forbidden internal terms (w46/W46, language-code slugs, github, discord, SOP, proofread, audit, lint, freeze, occlusion, KIT, http, .md, etc.): **0 hits** in SVG text of all 11.
- `12 de noviembre`: **0 occurrences** in any edition (core included) — W45 decree-date negative promise honoured at string level. P4 calendar uses `jueves 12` / fixture dates without that phrase.
- Image credits present in all editions: CC0, Wikimedia Commons, `Ilustración` (editorial ballot-box illustration disclosure), `Infamia`, `castaña`; EN additionally `chestnut`.

**9. WEEKDAYS/DATES — CONFIRMED.** Verified with `TZ=Europe/Madrid date`: 2026-11-09 Monday, 11-10 Tuesday, 11-11 Wednesday, 11-12 Thursday, 11-13 Friday, 11-14 Saturday, 11-15 Sunday, 11-19 Thursday, 11-27 Friday, 11-28 Saturday, 11-29 Sunday, 11-06 Friday, 11-03 Tuesday, 11-08 Sunday. All match KIT claims. Campaign "quince días: del viernes 13 al viernes 27" = 15 days inclusive, consistent.

**10. GLOSS + P1 EXPL LINE — CONFIRMED except M-1.**
- `gloss()` calls: 4 per build, 5/5/5/4 items (P2/P3/P4/P5), Spanish headwords identical item-by-item in all editions (verified from build sources by grep only; no content modules imported or executed).
- P1 `bridge()/expl()` headline line: 4 items in all 12, terms identical, glosses native. IT bridge drops the core `讲解｜` prefix (disclosed in IT KIT as bare style) — observation only.
- DE P4 5th gloss item complete: `el amistoso / Freundschaftsspiel.` CONFIRMED in render.

**11. JA KINSOKU — CONFIRMED.** 0 line-initial forbidden characters (NO_START set incl. `、。,.）］｝」』》〉】〗` + small kana) in JA SVGs; 0 line-initial ASCII closers.

**12. W45 PROMISES — CONFIRMED** (register `hidden_files/w46/w45-promises.md`, from W45 core KITs only).
- P7 teaser: Fri 13 Nov campaign start, Sun 29 Nov vote, readers' letters + best P8 writing; Nov 12 date DELETED from teaser — verified: `12 de noviembre` occurs 0 times anywhere; P7 VOL.4 preview box (campaign first week + Liga matchday 13 + Champions return + letters/best P8 texts) present as frozen Spanish sentence in all editions.
- Disclosure: example signed "Ana", labeled "ejemplo, escrito por la redacción"; Chinese note "编辑部示例信，非真实来信" — present in all editions (letters box verified geometrically, §3 above; native disclosures verified in layer reads).
- Negative promise: 11 Nov 12 "常设委员会法令表决" date removed from P6 timeline and P7 teaser for lack of a second independent source; "VOL.3 不得重新引入该日期，除非获第二独立来源证实" — honoured (no such date anywhere). Real letters only in VOL.3 if received. 8 Nov results not invented (frozen P4 box, inherited identically — verified via freeze).

**13. CARDS (item 10) — viewed full-frame.** P1 + P8 for all 11 editions; KO P2, P4, P5; DE P7; core P6. No overflow, overlap, missing glyphs/tofu, or missing image credits anywhere except the defects already listed (KO splits visible on P1/P2/P4/P5; DE P7 sentence visible). All other cards clean.

**14. EXPLANATION-LAYER CORRECTNESS (item 5).** EN, FR, IT, NL, PT, RU, JA, KO (apart from D-2…D-5/M-1), ZH-TW: native language correct throughout (grammar, agreement, glosses accurate, no untranslated residue beyond frozen furniture). ZH-CN: only the 17 furniture-delta strings; core text already read in full. IT: correct Italian, full disclosure, `Cechia` correct. NL: correct Dutch, `W/NW` (waar/niet waar) for true/false. PT: correct Brazilian-leaning Portuguese (`Chéquia`, `veranico`), full disclosure. RU: correct Russian, `Уманитариос` transliteration reasonable. JA: correct Japanese, full disclosure. KO: correct polite `-요` Korean throughout, full disclosure. ZH-TW P8 answers 57/68/84/87 byte-identical to core — verified as shared-form glyphs only (e.g. `球迷很多`, `Infamia 有 6 集`, `更多公屋支持率`), not Simplified residue; ZH-TW 118 (`el sobre = 信封`), 124 (`magosto 吃烤栗子`), 135 (`在零點`) verified Traditional/shared.

## KIT adjudication summary

- Material gate/furniture/fixup/promise claims: **CONFIRMED** in all 11 KITs, except:
  - **REFUTED (minor, KIT inaccuracy only):** FR badge 20pt (measured 19.5pt); DE 47,074 B (measured 47,056 B).
  - **REFUTED (material, incomplete gate):** KO "orphan scan 0 reports" as a complete orphan gate (true only under the narrower S1/S2 criteria; 4 splits remain under README #16) — see D-2…D-5.
  - **CONFIRMED in substance with wording clarification:** ZH-CN "Added CJK = 0" (M-4).
  - **CONFIRMED as disclosed:** DE/NL/RU disclosure reliance on the frozen Spanish text above (M-5).
  - **UNVERIFIABLE from KIT:** IT byte counts (absent from KIT; verified independently); ZH-TW per-page CJK totals (not re-derived; 0-Simplified-only claim confirmed).

## Seed record (for the coordinator's insert step)

- **Target VOL number: VOL.3** (all 11 editions + core).
- **Re-measured exercise total + level split: 150 total — A2 50 / B1 72 / B2 28**; per page 10/18/18/18/18/18/12/38.
- **Core P1 article opening sentences verbatim** (target language Spanish; headline `Del 11-N a la campaña: España vota en 20 días`):
  > España entra en su semana más intensa antes de las elecciones. El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral. El domingo 29 de noviembre, España vota en elecciones generales.
  (Verified character-for-character from the core P1 SVG text elements, y=797.8–1098.8, joined across line breaks.)

---

## Final verdict

ROUND 1 FAIL — blocking defects: D-1 (DE P7 Q6 ungrammatical translation) and D-2, D-3, D-4, D-5 (KO mid-word splits on P1, P2, P4, P5). The other 9 editions show no blocking defects. No frozen-core blocking defects. After the builder fixes D-1…D-5 and re-renders, a full re-proofread (Round 2) is required per SOP §8.4.
