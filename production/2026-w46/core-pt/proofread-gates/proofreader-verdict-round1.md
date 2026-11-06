# PROOFREADER VERDICT — ROUND 1 — Lucerna Weekly W46, PT target (VOL.3)

- Issue: 2026-W46, Mon 2026-11-09 – Sun 2026-11-15. Target language: Portuguese (Brazilian).
- Scope: all 11 PT-target editions (one per reader-native language):
  2026-w46-pt-de, -en, -es, -fr, -it, -ja, -ko, -nl, -ru, -zh-cn, -zh-tw.
  `files/weekly-report-w46-pt-core/` is the frozen-core duplicate of the pt-zh-cn
  edition and was NOT counted as a 12th edition; it was used as the freeze
  reference, exactly as the builders did.
- Proofreader role: independent Round 1. Nothing was fixed, re-rendered, edited,
  pushed, inserted, or posted by the proofreader. No subagents were used.
- Date of this verdict: 2026-11-02 (America/Toronto).
- Gate artefacts: all JSONs/logs listed in §6, saved under
  `hidden_files/w46/pt-proofread-gates/`.

## Final verdict

**ROUND 1 FAIL — 9 of 11 editions blocked; 2 editions shippable as-is (pt-ja, pt-zh-tw).**

Blocking defects: F-1 (fullwidth colon in P8, 8 editions), F-2 (fullwidth full
stop in P7, 7 editions), F-3 (orphan full stop line in pt-ko P7), F-4
(news-framed abstracts, pt-en + pt-zh-cn), F-5 (Portuguese header line in the
pt-zh-cn .text.md). All are small, mechanical fixes. No fact, date, count,
geometry, badge, PDF, or P7-verbatim defect was found. After the fixes, a
Round 2 proofread must re-run the affected gates from scratch (per SOP §8.4,
a fix restarts the full round); Round 2 should be short because every other
gate below passed cleanly.

## Per-edition verdicts

| Edition | Verdict | Blocking defects |
|---|---|---|
| 2026-w46-pt-de | FAIL | F-1, F-2 |
| 2026-w46-pt-en | FAIL | F-1, F-2, F-4 |
| 2026-w46-pt-es | FAIL | F-1, F-2 |
| 2026-w46-pt-fr | FAIL | F-1, F-2 |
| 2026-w46-pt-it | FAIL | F-1, F-2 |
| 2026-w46-pt-ja | PASS | — (see observations O-2 only) |
| 2026-w46-pt-ko | FAIL | F-1, F-3 |
| 2026-w46-pt-nl | FAIL | F-1, F-2 |
| 2026-w46-pt-ru | FAIL | F-1, F-2 |
| 2026-w46-pt-zh-cn | FAIL | F-4, F-5 |
| 2026-w46-pt-zh-tw | PASS | — |

## 1. Defect list

### A. Frozen-core defects (fix once in the core; re-derive all fan-outs)

**F-1 — P8 answer notes use a fullwidth colon U+FF1A (：) between Latin words
in 10 lines, while neighbouring notes use an ASCII colon.**
Scope: the 8 Latin-script editions (de, en, es, fr, it, ko, nl, ru). NOT a
defect in pt-ja / pt-zh-cn / pt-zh-tw, where ： is legitimate CJK punctuation
inside CJK glosses (42 lines there, correct).
Evidence (identical in all 8 editions; file `svg/p8-avaliacao.svg`, full
inventory in `punct-inventory.txt`):
- `16. confere — conferir：ele → confere`
- `17. abre — abrir：ele → abre`
- `18. levamos — levar：nós → levamos`
- `19. começa — começar：ela → começa`
- `20. termina — terminar：ela → termina`
- `56. mais — 2 > 0：mais`
- `57. mais — 3 > 2：mais`
- `58. mais — 17 < 18：mais cedo`
- `102. confere — conferir：você → confere`
- `103. termina — terminar：ela → termina`
Contrast, same page (pt-en): `101. confiro — conferir: eu → confiro (irregular)`
with an ASCII colon. The 10 strings are pure Portuguese notes inherited
unchanged from the core register, which is why `freeze.py` reports "added CJK 0"
for these editions — the characters were already in the core. The builder
KITs' broader "zero CJK residue" reading is therefore refuted (see §6).
Correct text: replace ： with `:` in those 10 note strings (per-edition
punctuation: JA/ZH editions keep ： inside their CJK glosses).

### B. Edition-specific defects

**F-2 — P7 "ERROS COMUNS" clinic: the translated final sentence ends with a
fullwidth full stop U+3002 (。) in 7 editions.**
The core sentence is Chinese and legitimately ends with 。; the fan-out
transforms translated the sentence but kept the Chinese terminator.
Evidence (`svg/p7-lingua.svg`, clinic item 4, "O feriado dá folga na segunda."
correction; full contexts in `disclosure-full.txt` / `punct-inventory.txt`):
- pt-de: `Der Feiertag fällt auf einen Sonntag, / montags gibt es keinen Ausgleich。`
- pt-en: `The holiday falls on a Sunday, with no / Monday off。`
- pt-es: `El festivo cae en domingo, el lunes no se / recupera。`
- pt-fr: `Le jour férié tombe un dimanche, pas de / récupération le lundi。`
- pt-it: `La festa cade di domenica, il lunedì non si / recupera。`
- pt-nl: `De feestdag valt op zondag, maandag geen / inhaal。`
- pt-ru: `Праздник выпадает на воскресенье, в / понедельник выходного нет。`
Correct text: replace the trailing 。 with `.` in each edition. (Also visible
on the rendered P7 cards, e.g. pt-de / pt-ru.) JA/ZH-CN/ZH-TW legitimately
use 。 — no defect there. The same 。 residue appears twice in each affected
edition's `.text.md` (timetable gloss line) and must be fixed there too
(`。=2` per Latin `.text.md`; see §2).

**F-3 — pt-ko P7: a standalone 。 text node on its own line.**
Evidence (`svg/p7-lingua.svg`, text nodes 107–108): node 107
`공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요` is followed by node 108 `。`
alone, immediately before the `A PALAVRA · 이번 주 단어` header.
Correct text: delete the orphan 。 node and terminate the Korean sentence
with `.` (`…쉬지 않아요.`). The KO `.text.md` has 。=3 (includes this orphan);
fix there too.

**F-4 — ABSTRACT.txt uses forbidden news-framing in 2 editions (practice
framing required; never "learn Portuguese from this week's news" or
equivalents).**
- pt-en `ABSTRACT.txt` (verbatim tail): `…for English speakers who want to
  learn Portuguese through real Brazilian news.`
- pt-zh-cn `ABSTRACT.txt` (verbatim tail): `…适合学葡萄牙语的读者通过巴西新闻学葡萄牙语。`
  (= "learn Portuguese through Brazilian news").
Correct text: reframe as practice on this week's topics (e.g. EN: "…150
exercises on this week's topics, for English speakers learning Portuguese.";
ZH-CN: "…以本周话题为素材的 150 道练习"). Both files are otherwise valid
(single line, no ASCII double-quote, reader-native, masthead + target +
A2–B2 + 150 present). The other 9 abstracts are neutral topic lists with
levels/counts and do not violate the rule.

**F-5 — pt-zh-cn `.text.md`: header line left in Portuguese (minor).**
Evidence (`2026-w46-pt-zh-cn.text.md`, line 3):
`Semana de 9 a 15 de novembro de 2026 · Textos em português · Explicações em
chinês simplificado · Níveis A2–B2 · 150 exercícios`
Every other edition's header line is in the reader's native language (e.g.
pt-zh-tw line 3: `2026 年 11 月 9–15 日 · 正文葡萄牙語 · 講解繁體中文 · 程度
A2–B2 · 150 道練習題`). This is a consequence of copying the core `.text.md`
byte-for-byte, as the KIT records. Correct text: a Simplified-Chinese header
line with the same facts.

### C. Observations (NOT defects — no action required, recorded for the file)

- O-1 — pt-es P2: the instruction `Completa con los números de las páginas 1 y
  2.` wraps with a lone `2.` node at (x=989, y=2094.225). A wrap orphan, not
  an error; the sentence is complete and correct.
- O-2 — pt-ko: short wrap tails below the builder's documented ≥3-syllable
  criterion, explicitly recorded and accepted in the KIT (`요.` alone in P4/P5
  instructions; `15` tail in P5 option C; syllable splits `입|장`, `보|어` in
  P8 notes; 1-syllable tails `벼락치|기`, `끝나|고`, `최|고의` as recorded).
  Korean syllable-unit wrapping is legitimate typography; none of these is a
  language or fact error. The F-3 。 orphan is a different class (wrong-script
  punctuation) and is a defect.
- O-3 — pt-en and pt-zh-cn `ABSTRACT.txt` have no trailing newline (0
  newlines counted). Still a single logical line; cosmetic only.
- O-4 — KIT subtitle-width figures are advance-width estimates; rendered ink
  is slightly wider (e.g. pt-en claimed 1786 px, measured ink 1811 px;
  pt-de claimed 1754 px, measured 1782 px). All subtitles still clear the
  inner frame by ≥26 px (see §4); no defect.

## 2. Gate outputs summary (all re-run independently by the proofreader)

- **Freeze baseline** (`tools/freeze.py baseline`, core build dir
  `hidden_files/weekly-report-w46-pt-build`): **8/8 SVGs byte-identical**,
  core SVGs unchanged by the run (`freeze-baseline.log`).
- **Freeze diff** (`tools/freeze.py diff` vs pt-core, all 11): `freeze-pt-*.json`
  + `freeze-all.log`. Added-CJK multiset = 0 for all 7 Latin-script editions
  (DE/EN/ES/FR/IT/NL/RU); JA/KO/ZH added CJK is legitimate native script.
  Portuguese-body freeze additionally verified independently: 41 of 43 long
  article paragraphs from the core `.text.md` occur verbatim (punctuation-
  insensitive) in ALL 11 editions; the 2 apparent misses are layout
  artefacts (P2 timetable split into cells; P8 model essay split by its
  label), both confirmed word-identical (`pt-paragraph-freeze2.txt`).
  No Portuguese body text was added, changed, or deleted in any fan-out.
- **P8** (`tools/p8.py compare --total 150`, all 11): **CLEAN 150/150** in
  every edition, missing=[] extra=0 uncertain=[] (`p8-all.log`, `p8-pt-*.json`).
  Keydiffs: [137, 138] in all editions except pt-zh-cn (none) — adjudicated
  LEGITIMATE translation re-aims: the keys are the same Portuguese sentences
  (`Domingo, 15 de novembro, é o segundo dia do Enem` / `Confira o cartão…`),
  only the source-language stem changed (e.g. pt-en 137: `Sunday, November 15,
  is the second day of the Enem. — See the…`; pt-zh-cn 137 identical to core).
- **Occlusion** (`tools/occlusion_audit.py`, selftest OK on every run):
  **0 flags in all 11 editions** (88 pages), `occlusion-all.log`,
  `occlusion-pt-*.json`.
- **Masthead pixel check** (P1 re-rendered with CairoSVG at 1950×2700,
  ink bounding boxes measured with PIL): masthead ink identical in all 11
  (x=623..1325, w=703 px; 583 px clearance each side). Subtitle ink widths
  1766–1819 px, clearing the inner frame by 26–53 px; badge ink centred with
  ≥407 px clearance; masthead→subtitle gap 35–36 px, subtitle→badge gap
  17–21 px. No contact anywhere (`masthead-pixels.txt`).
- **Counts** (re-measured from SVG text nodes + build register):
  **150 exercises in every edition**, per-page stems 10/18/18/18/18/18/12/38
  (P1 1–10, P2 11–28, P3 29–46, P4 47–64, P5 65–82, P6 83–100, P7 101–112,
  P8 113–150; apparent extras adjudicated: P5 five-step plan items 1–5,
  pt-de P1 date line `15. Nov.:…`, pt-es P2 wrap orphan `2.`).
  Level split re-derived from the core build register (`ex` 138 + `match_set`
  3×4): **A2 49 / B1 70 / B2 31 = 150**, exactly the KIT claim
  (`counts.txt`, `counts-detail.txt`, `levels.txt`). P8 answer keys 1–150 all
  present (154 raw matches = 150 keys + 4 P8 body stems 141–144, explained).
- **P6 chart** (core + all editions): bars w=90/45/450 px for 60/30/300 min
  (1.5 px/min, exact proportions); caption `60 + 30 + 300 = 390` correct;
  12h→13h = 60, 13h→13h30 = 30, 13h30→18h30 = 300, 12h→18h30 = 390 min, all
  consistent. Bar rects byte-identical in all 11 editions; other differing
  P6 rects are only translated-text box heights/chip shifts (`p6-rect-diff.txt`).
- **P7 quotes** (SOP: verbatim from this issue's own articles): all 8 quotes
  occur exactly 2× in the core joined text (incl. lowercase #3 `o feriado não
  muda o relógio`); all 8 appear in the P7 block of every edition with a
  correct native translation and a correct `(Página N)` label
  (P1,P1,P2,P3,P4,P5,P6,P2) (`p7-keydiff-kinsoku.txt`).
- **Dates/weekdays** (independent calendar check): 2026-11-09 Monday,
  2026-11-15 Sunday, 11-08 Sunday, 11-07 Saturday, 11-11 Wednesday,
  11-14 Saturday, 11-20 Friday, 11-27 Friday, 11-06 Friday — all match the
  issue's claims. 2026−1889 = 137 years. Enem arithmetic 45+45=90, 5h=300 min.
- **Register**: Portuguese body uses `você` throughout (P1 `AGORA VOCÊ`,
  P2 `E você?`, P7 `você confere`, P8 `ESCREVA VOCÊ`, ex. 102); **no `tu`
  forms anywhere in the Portuguese text** — no tu/você mismatch. The PT
  disclosure (`Nota da redação…`) uses no second person. Native-layer
  instruction registers are internally consistent per edition (e.g. FR tu:
  `Lis…`, `Vérifie ta carte`; DE du: `Lies…`, `JETZT DU`).
- **Badge + footer**: pairing badge present in the P1 masthead (y=372,
  centre-anchored) and pairing footer on all 8 pages of every edition.
  Measured badge fill colours: pt-en `#3e4c2a` (OLIVE); pt-ru `#57523f`
  (GREY, non-bold); all other 9 editions `#a4553a` (BRICK) — all matching
  the KIT claims. Gloss prefixes verified as used, matching KITs
  (DE `HINWEIS ·`, EN `Note |`, ES/FR/IT `Nota/Note —`, JA `解説 —`,
  KO `해설 —`, NL `Uitleg —`, RU `Пояснение —`, ZH-CN `译注｜`,
  ZH-TW `譯注｜`).
- **PDFs**: every `*-web.pdf` < 7 MB (884,629–1,614,344 bytes) with a real
  text layer (pdftotext 43,019–53,270 bytes), byte counts matching
  `pt-gates.log` exactly. Print PDFs present in every edition dir.
- **ABSTRACT.txt**: all 11 single logical line, 0 ASCII double-quotes,
  reader-native, with masthead + target language + A2–B2 + 150 + real topics
  — except F-4 framing (EN, ZH-CN). Full texts in `abstract-audit.txt`.
- **Native-language correctness / script residue**: no untranslated Chinese
  words in any Latin edition (only the F-1/F-2 punctuation); no English-word
  residue in non-EN editions (only PT verb `for` and French `page`/`Note`
  false positives); no Cyrillic/Hangul/kana outside their own editions;
  no U+FFFD anywhere; JA kinsoku line-start check 0 violations; KO Hangul
  present, 0 Hanja; zh-cn shows 0 traditional-only probe characters,
  zh-tw shows 0 simplified-only probe characters (probe sets in
  `ko-fffd-residue.txt`). ZH-TW manual overrides corroborated
  (複習/詞組/分區/毛里西奧 present in zh-tw, absent in zh-cn; 覆習/片語/
  分割槽/檔案/支援 absent in zh-tw). zh-tw vs zh-cn: identical text-node
  counts on all 8 pages and identical pure-Latin node sets — pure conversion,
  no extra paragraph (W45 extra-invitation paragraph correctly NOT carried
  over).
- **Reader-facing sweep**: all rendered SVG text scanned for week/language
  codes, repo/SOP/proofread/audit/lint/Discord/transform/internal markers:
  **0 real hits** (only Portuguese `todo(s)`, `transformar`, Italian `sopra`,
  French `repos`, and legitimate `VOL.2`/`VOL.4` cross-references).
- **W45 promises** (from core KIT §4): (a) Enem day 2 + Proclamation holiday
  as headline/main thread — honoured (P1 headline in all editions).
  (b) No fabricated letters/names; editorial example + bilingual disclosure —
  honoured (PT disclosure verbatim + native translation in all 11; example
  labelled in every edition). (c) Second-leg football results: deadline note
  present (`Nota: esta edição fechou em 2 de novembro…`, verified in all
  editions via the paragraph freeze), first-leg scores printed, second-leg
  schedule + promotion arithmetic + VOL.4 carryover — honoured as recorded.
  (d) P4 open update slot for post-8-Nov scores — recorded in KIT, still
  open by design (insert-time decision, not a proofread defect).
- **Images/credits**: P1 photo credit `Gary Todd / Wikimedia Commons — CC0`
  present in all 11 P1s; no other photos (known limitation, recorded in the
  core KIT, not a defect).
- **Cards viewed at full frame**: P1 + P8 of all 11 editions (22 cards) +
  spot checks P7 (de/ja/ko/ru) + P6 (en): no overflow, overlap, missing
  glyphs/tofu, or footer intrusion; no missing credits. Thumbnails saved in
  `card-thumbs/` (proofreader working copies; shipped cards untouched).
- **.text.md**: present in all 11 editions, 480 lines each, correct pairing
  header (except F-5), `150.` + `VOL.3` + `2026` present; Latin editions
  contain only the F-2 。 residue (。=2 each; ：=0 — the derive step
  normalised colons); KO 。=3 (incl. F-3).

## 3. KIT-claim adjudication (per edition KIT + pt-gates.log)

- `gates.py` 17/17 PASS (builder self-check): UNVERIFIABLE as a run — the
  proofreader does not re-run build scripts (that would re-render). The
  underlying assertions (badge, footers 8/8, P7 clearance, disclosure
  verbatim, quote 2×) were independently verified and are CONFIRMED except
  where F-1/F-2/F-4/F-5 bite.
- `occlusion_audit.py` 0 flags: CONFIRMED (re-run, selftest OK).
- `p8.py compare` CLEAN 150/150, keydiff 137/138: CONFIRMED; keydiffs
  adjudicated legitimate.
- `freeze.py diff` "explanation-only, added CJK 0": the freeze.py numbers are
  CONFIRMED; the KITs' broader "zero CJK residue" claims are REFUTED by F-1/F-2
  (the residue characters pre-exist in the core, so the tool's added-CJK
  multiset is 0 while the shipped pages still carry them).
- pt-ja churn "320 removed / 335 added": REFUTED as stated — shipped SVGs
  measure 394 added / 379 removed; substance ("0 PT-body changes, added CJK
  is legitimate Japanese") CONFIRMED.
- pt-zh-tw "276/276 pure conversion": count REFUTED — shipped SVGs measure
  281 added / 281 removed; substance (pure conversion, 0 PT-body changes)
  CONFIRMED.
- pt-zh-cn "+1/−1 (badge+footer only)": CONFIRMED in substance — per page
  +1/−1 except P1 +2/−2 (badge + footer); +9/−9 total, all furniture.
- Web-PDF sizes / pdftotext bytes: CONFIRMED exactly (see §2).
- `.text.md` "zero CJK": REFUTED literally (F-2 。 residue, 2 per Latin
  edition); no Chinese words remain — substance CONFIRMED.
- pt-ja "kinsoku 0 violations": CONFIRMED. pt-ko "orphan scan 0 defects
  ≥3-syllable": CONFIRMED within its stated criterion (see O-2).
- pt-ja "no Chinese source residue (REPL check)": CONFIRMED within probe
  scope (only shared kanji 国/学/会 etc.; no 说/让/读/对/这/们/为/间/认).
- Badge colours / sizes / furniture strings in every KIT: CONFIRMED as
  measured (fills, sizes, texts — see §2).
- "No SOP §8 independent second-person proofread — builder self-check only":
  CONFIRMED as stated in every KIT; this Round 1 verdict is that missing
  independent round. It is not itself a defect in the editions.
- Core KIT facts (scores, dates, sources, 88-word model essay, 137 years,
  chart arithmetic): independently re-checked where checkable from the
  artefacts; no contradiction found. External-source truth of the cited
  2026 results could not be re-verified from the VM (scenario date
  2026-11-02; sources cited in the KIT); internal consistency across all
  pages/editions is exact.

## 4. Seed record (for the coordinator's insert step)

- Target VOL number: **VOL.3**.
- Re-measured exercise total + level split: **150 exercises — A2 49 / B1 70 /
  B2 31**; per-page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Core P1 article opening, verbatim (target language, Portuguese, first 3
  sentences):
  > Domingo, 15 de novembro, é o segundo dia do Enem 2026 — e é também o
  > feriado da Proclamação da República. A prova e o feriado chegam no mesmo
  > dia: de manhã, o país acorda para a história; à tarde, mais de 5 milhões
  > de estudantes fazem Ciências da Natureza e Matemática.

## 5. Required fix list for the builder (Round 2 input)

1. Core register: replace ： with `:` in the 10 pure-Portuguese P8 note
   strings (F-1); re-derive fan-outs; keep ： inside JA/ZH CJK glosses.
2. Fan-out transforms: replace trailing 。 with `.` in the P7 clinic sentence
   (F-2, 7 editions); delete the KO orphan 。 node and end that sentence
   with `.` (F-3); fix the same 。 in the affected `.text.md` files.
3. Rewrite pt-en + pt-zh-cn ABSTRACT.txt closing clauses to practice
   framing (F-4).
4. Translate the pt-zh-cn `.text.md` header line into Simplified Chinese (F-5).
5. Re-run freeze diff, p8 compare, occlusion audit, web-PDF text-layer check
   on the rebuilt editions; then request Round 2 proofread (full round per
   SOP §8.4, expected to be short given §2).

## 6. Files saved under hidden_files/w46/pt-proofread-gates/

`proofreader-verdict-round1.md` (this file); `occlusion-pt-*.json`,
`occlusion-all.log`; `p8-pt-*.json`, `p8-all.log`; `freeze-pt-*.json`,
`freeze-all.log`, `freeze-baseline.log`, `freeze-baseline/` (reproduction
scratch); `freeze-analysis.txt`, `freeze-purept.txt`,
`pt-paragraph-freeze.txt`, `pt-paragraph-freeze2.txt`; `counts.txt`,
`counts-detail.txt`, `levels.txt`; `punct-inventory.txt`,
`residue-register.txt`, `disclosure-full.txt`, `ko-fffd-residue.txt`,
`ko-orphan-gloss.txt`, `p7-keydiff-kinsoku.txt`, `p6-rect-diff.txt`,
`badge-pdf-abstract.txt`, `abstract-audit.txt`, `reader-sweep.txt`,
`textmd-check.txt`, `preview-textmd-cjk.txt`, `masthead-pixels.txt`,
`masthead-renders/` (P1 re-renders), `card-thumbs/` (working thumbnails of
shipped cards + spot checks). No edition files were touched; no files were
written outside this gate directory (plus the frozen `freeze-baseline/`
scratch inside it).

## 7. Final verdict line

**ROUND 1 FAIL (list of blocking defects: F-1, F-2, F-3, F-4, F-5 above;
pt-ja and pt-zh-tw PASS as-is).**
