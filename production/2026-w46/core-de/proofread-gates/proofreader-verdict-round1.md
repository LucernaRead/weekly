# Independent Proofread — Round 1 Verdict: Lucerna Weekly W46, DE family

**Issue:** 2026-W46, Mon 2026-11-09 – Sun 2026-11-15. Target language: German (DE).
**Editions proofread (11):** de-en, de-es, de-fr, de-it, de-ja, de-ko, de-nl, de-pt, de-ru, de-zh-cn, de-zh-tw.
`files/weekly-report-w46-de-core/` is a duplicate of the de-zh-cn edition and is NOT counted as a 12th edition; it is cited below as the frozen core.
**Proofreader:** independent (did not build these editions). Proofreader only: nothing was fixed, re-rendered, or edited.
**Date of verdict:** 2026-11-03. Press time per KITs: 2 November 2026. Target VOL: **VOL.3**.
**Gate rule:** proofread-until-zero. This is the first independent round for this family.

## Final verdict

**ROUND 1 FAIL** — all 11 editions blocked. Blocking defects: D-CORE-1 (factual, all editions), D-ABSTRACT (framing gate, all editions), D-TOOLBOX (wrong grammar gloss, 6 editions), D-IT-1, D-NL-1, D-RU-1. Minor defects listed in §3 must be fixed in the same round; under proofread-until-zero the family does not ship with known defects outstanding. No edition is shippable as-is.

Note on D-ABSTRACT adjudication: the parent task and the 2026-10-28 user rule ban news-learning framing in abstracts, and this verdict applies that gate. SOP §9 (2026-10-22) itself gives "learn French by reading"-type phrasing as an abstract example, which points the other way. If the coordinator rules the SOP example authoritative, D-ABSTRACT downgrades to a style note — but the round still FAILS on D-CORE-1, D-TOOLBOX, D-IT-1, D-NL-1 and D-RU-1. The tension is recorded here for the coordinator; it does not change the verdict.

## Per-edition verdicts

| Edition | Verdict | Blocking defects | Minor / observations |
|---|---|---|---|
| de-en | **FAIL** | D-CORE-1, D-ABSTRACT, D-TOOLBOX | — |
| de-es | **FAIL** | D-CORE-1, D-ABSTRACT, D-TOOLBOX | M-1, M-2, M-3 |
| de-fr | **FAIL** | D-CORE-1, D-ABSTRACT, D-TOOLBOX | M-1, M-2, M-3 |
| de-it | **FAIL** | D-CORE-1, D-ABSTRACT, D-TOOLBOX, D-IT-1 | M-1, M-2, M-3 |
| de-ja | **FAIL** | D-CORE-1, D-ABSTRACT | M-1, M-4, M-5 |
| de-ko | **FAIL** | D-CORE-1, D-ABSTRACT | D-KO-1, M-1, M-4, M-5, M-6 |
| de-nl | **FAIL** | D-CORE-1, D-ABSTRACT, D-NL-1 | M-1, M-2 |
| de-pt | **FAIL** | D-CORE-1, D-ABSTRACT, D-TOOLBOX | M-1, M-2, M-3, D-PT-1 |
| de-ru | **FAIL** | D-CORE-1, D-ABSTRACT, D-TOOLBOX, D-RU-1 | M-1 |
| de-zh-cn | **FAIL** | D-CORE-1, D-ABSTRACT | D-CORE-3, M-5, O-1 |
| de-zh-tw | **FAIL** | D-CORE-1, D-ABSTRACT | M-5, T-1 |

## 1. Blocking defects — frozen core (affect all 11 editions + core dir)

### D-CORE-1 (BLOCKING, factual): P4 photo caption misdates the Berlin game
- **Evidence:** `weekly-report-w46-de-core/svg/p4-sport.svg` (identical in all 11 editions by freeze): joined caption text: `Kopfball im Spiel: So sieht ein Duell in der Luft aus — um jeden Ball wird gekämpft. Die Nationalelf spielt in dieser Woche in Belgrad und Berlin.`
- **Wrong:** the Berlin game (Germany–Netherlands) is Mon 16 November 2026, OUTSIDE the issue week (9–15 Nov). The caption says the team plays in Berlin "in dieser Woche".
- **Contradicted by the issue itself:** P1 caption (fixed in the build): `In dieser Woche spielt die Nationalmannschaft in Belgrad — die Bundesliga pausiert. Am Montag danach kommen die Niederlande nach Berlin.`; P4 article: `Am Montag, dem 16. November … folgt das zweite Spiel`. Core KIT §7 records fixing this same error in the P1 caption; the P4 caption still carries it.
- **Correct text pattern:** `… spielt in dieser Woche in Belgrad — am Montag danach in Berlin.`
- **Not affected:** the P4 credit line is fine (`Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain`; P1 credit names Staff Sgt. Stephanie Jacobs, U.S. Air Force, public domain).

### D-ABSTRACT (BLOCKING, framing gate, task item 7): every ABSTRACT.txt closes with news-learning framing instead of practice framing
All 12 dirs (11 editions + core duplicate): single-line, 0 ASCII double-quotes, reader-native — format PASS. Framing FAIL. All DO contain the practice facts (A2–B2, 150 exercises) and real topic names; only the closing framing sentence is wrong. The abstract text does not appear on any rendered page (verified: no page hit), so the fix is frontmatter/ABSTRACT-only, no re-render needed.
- en: `…for learners who want to learn German by reading real German news.`
- zh-cn: `…适合学德语的读者通过德国新闻学德语。`
- zh-tw: `…適合學德語的讀者通過德國新聞學德語。`
- es: `para aprender alemán leyendo noticias alemanas reales`
- fr: `pour apprendre l'allemand en lisant les vraies nouvelles allemandes`
- it: `per imparare il tedesco leggendo vere notizie tedesche`
- ja: `本物のドイツのニュースでドイツ語を学ぶ読者のために`
- ko: `진짜 독일 뉴스로 독일어를 배우는 독자를 위해`
- nl: `om Duits te leren door echt Duits nieuws te lezen`
- pt: `para aprender alemão a ler notícias alemãs reais`
- ru: `для тех, кто учит немецкий по настоящим немецким новостям`
- **Required framing (user rule 2026-10-28):** practice product, week's topics only as material — e.g. "以本周话题为素材的 N 道练习" pattern; never "learn German from this week's news" or equivalents.
- **Tension recorded:** SOP §9 sanctions "learn French by reading"-type phrasing as an abstract example. See verdict note above.

### D-CORE-3 (minor, visible stray mark; frozen core → zh-cn, zh-tw): orphan 。 on P2
- **Evidence:** `weekly-report-w46-de-core/svg/p2-leben.svg`, `<text x="1473" y="1175.88" …>。</text>` — a lone 。 on its own rendered line directly under the UND SIE? Chinese translation (`你过狂欢节还是圣马丁节？写两句德语寄来`), inside the right-column box. Identical element in de-zh-cn and de-zh-tw P2. Visually confirmed on the core P2 card (stray dot under the Chinese line). The fan-outs' shorter translations do not inherit it. Fix: re-wrap the invitation line so the 。 stays attached.

## 2. Blocking defects — edition-specific

### D-TOOLBOX (BLOCKING, wrong grammar gloss; EN, ES, FR, IT, PT, RU): P7 DER WERKZEUGKASTEN entry `Es wird gespielt. = …` mistranslated as FUTURE
Standing alone (no time adverbial), `Es wird gespielt` is present passive ("it is [being] played"). The six editions gloss it as future, which collapses the exact distinction the same page teaches: ex. 103 `wird … beginnen` = future (`werden` + infinitive) vs. ex. 104 `Es wird gespielt` = Passiv (exercise 104 asks: `"Es wird gespielt" ist… A. Passiv · B. Perfekt · C. Imperativ`, key A).
- en P7: `Es wird gespielt. = It will be played` (correct: `It is played / A game is being played`)
- es P7: `Es wird gespielt. = Se jugará` (correct: `Se juega`)
- fr P7: `Es wird gespielt. = Il sera joué` (correct: `Il est joué / On joue`)
- it P7: `Es wird gespielt. = Si giocherà` (correct: `Si gioca / Viene giocato`)
- pt P7: `Es wird gespielt. = Vai ser jogado` (correct: `É jogado / Joga-se`)
- ru P7: `Es wird gespielt. = Будет сыграно` (correct: `Играется / Матч проводится`)
- **Control renderings (correct, present passive):** nl `Er wordt gespeeld`, ja `試合が行われる`, ko `경기가 열린다`. Core Chinese `比赛将进行（被动）` is future-leaning but carries the （被动） tag that disambiguates it — recorded as a core observation, not a core defect. ZH-TW inherits the core gloss (`比賽將進行（被動）`) — same observation, not a separate defect.

### D-IT-1 (BLOCKING, wrong part of speech; IT only): P3 gloss `das Geschnatter = starnazzare`
- **Evidence:** `weekly-report-w46-de-it/svg/p3-kultur.svg` note line: `das Geschnatter = starnazzare`.
- **Wrong:** `Geschnatter` is a noun (cackling/chattering); `starnazzare` is a verb infinitive (to cackle). Cf. en `cackling`, es `graznido`, fr `caquètement`, ja `ガーガー鳴くこと`, ko `꽥꽥거림` (all nouns/nominalisations).
- **Correct:** `lo starnazzare` or `il garrito`.

### D-NL-1 (BLOCKING, corrupted gloss; NL only): P6 article gloss missing headwords
- **Evidence:** `weekly-report-w46-de-nl/svg/p6-vertiefung.svg`, elements 59–62 (joined): `Uitleg — gedenken = herdenken · Kranzniederlegung = krans · stille Tag = stille dag · verbondenheid · verzoening.`
- **Wrong:** the last two entries lack German headwords and `=`; two Dutch words (`verbondenheid`, `verzoening`) dangle unexplained. Visually confirmed on the NL P6 card.
- **Correct:** `· die Verbundenheit = verbondenheid · die Versöhnung = verzoening.` (cf. well-formed en/pt/ru/ja/ko equivalents). Likely caused by the documented P6 gloss shortening.

### D-RU-1 (BLOCKING, truncated German definition; RU only): P7 NOCH EIN WORT drops part of the German definition
- **Evidence:** `weekly-report-w46-de-ru/svg/p7-sprache.svg`: `«das Geisterspiel» (Seite 4): Spiel ohne Zuschauer. Матч-призрак.`
- **Wrong:** the German definition lost `ein` and `im Stadion`; as printed it is a fragment (`: Spiel ohne Zuschauer.`). Cf. core/EN: `«das Geisterspiel» (Seite 4): ein Spiel ohne Zuschauer im Stadion.`
- **Correct:** `«das Geisterspiel» (Seite 4): ein Spiel ohne Zuschauer im Stadion. Матч-призрак.` (Russian gloss `Матч-призрак` is fine.)

### D-KO-1 (minor, visible stray punctuation; KO only; KIT fix claim REFUTED): three orphan marks
- **Evidence (SVG, all rendered at normal size/fill, visually confirmed on cards):**
  1. `weekly-report-w46-de-ko/svg/p5-jugend.svg`, `<text x="1007" y="628.675" …>。</text>` — lone 。 on its own line under the P5 gloss block.
  2. Same file, `<text x="527" y="2220.225" …>。</text>` — lone 。 under the C-section instruction `두 문장을 weil로 연결하세요（동사는 맨 끝으로）`.
  3. `weekly-report-w46-de-ko/svg/p8-uebungen.svg`, `<text x="989" y="1901.0" …>)</text>` — lone `)` on its own line at the end of the Page-6 answers block (the closing paren of item 100's note `(희생자 추모)` wrapped alone; visible as a dangling `)` on the KO P8 card).
- **KIT adjudication:** KO KIT §4 claims the P5 orphan 。 was fixed by removal. REFUTED — two 。 orphans remain on P5 plus one `)` orphan on P8.

### D-PT-1 (minor, editorial inconsistency; PT only): mixed tu/você address
Headers/invitations in tu-form (`Lê…`, `Escreve…`, `Escolhe…`, `Olha…`, `Usa…`, `Junta…`, P7 `corrige-os`) vs. item instructions in você-form (`Complete`, `Reescreva`, `Monte`, `Enviem-nos…`), including inside P8: `(traduz para português)` (tu) next to `Traduza para o português` (você). Each form is grammatical alone; the mix within one edition is inconsistent. Cf. ES consistently tú. Fix: pick one address form for the whole edition.

## 3. Minor defects / observations (fix in the same round)

- **M-1 — Bare-German furniture headers (minor; 8 editions).** `DER WERKZEUGKASTEN` with no reader-language gloss on P7 in es, fr, it, nl, pt, ru, ja, ko (verified in SVG; en has `· Toolbox`, zh-tw retains the core `· 工具箱`). RU P1 `IN DIESER AUSGABE` is likewise bare (KIT-documented shortening of `IN DIESER AUSGABE · Содержание`). These are layout-driven shortenings, but they leave untranslated German furniture in reader editions. Fix: restore short glosses.
- **M-2 — Bare-noun `Kranzniederlegung` glosses (minor observation; es, fr, it, pt, ru, nl).** P6 notes give `ofrenda`, `gerbe`, `corona`, `coroa`, `венок`, `krans` — the bare "wreath" noun loses the laying/deposition action. Full forms appear in the same editions' P8 key 97 (`una ceremonia de ofrenda floral`, `une cérémonie de dépôt de gerbe`, `una cerimonia di deposizione di corone`, `uma cerimónia de deposição de coroas`, `церемония возложения венков`, `een kransleggingsceremonie`), and en `wreath-laying`, ja `献花`, ko `헌화` are fuller. ES KIT §4 documents the shortening (`ofrenda` for `ofrenda floral`). NL additionally has D-NL-1.
- **M-3 — UND SIE? invitations thinned (minor observation; es, fr, it, nl, pt, ru).** Second prompt question dropped and/or compressed to fragments vs. the full EN wording, e.g. es P3 `¿Hiciste un farolillo? ¡Escribe dos frases en alemán!` vs. core/EN two questions; pt P5 `Uma lanterna em criança? A tua canção? Duas frases!`. The write-two-sentences call survives everywhere. JA/KO/ZH-TW keep fuller invitations.
- **M-4 — E-section translation register mix (minor observation; JA, KO).** P8 translation-model answers mix plain and polite forms: JA 137 plain (`開幕する。`), 138 polite (`作ります。`), 139 plain (`再開した。`); KO 137 plain (`개막한다.`), 138/139 polite (`만듭니다.` / `시작했습니다.`). All translations are correct; the register is inconsistent within the answer set.
- **M-5 — Wrap punctuation at line edges (minor observation; frozen-core pattern + fan-outs).** Wrapped lines beginning/ending with punctuation in dense note/gloss paragraphs — e.g. JA P2 gloss line ending with dangling `（` (`解説 — der Jeck＝カーニバルの浮かれ者（`, visually confirmed); KO P2 gloss line starting with `）`; ZH-CN/ZH-TW P6 `DIE DEBATTE` paragraph line starting with `。` (`。电力税：降多少尚未确定…` / `。電力稅：降多少尚未確定…`, visually confirmed on ZH-TW P6); core ZH-CN P8 note wraps with the same pattern throughout (24 instances in the scan, `orphan-kinsoku-scan.txt`). The core itself carries this class, so it is a frozen-layout wrap wart, not a fan-out regression. JA kinsoku otherwise holds (German text re-wrapped under kinsoku rules, content token-identical — see §4). Fix by re-wrapping the affected paragraphs.
- **M-6 — KO P1 exercise-flow quirk (minor observation; KO only).** On the KO P1 card, exercise 1 sits under `JETZT ÜBEN` at the bottom of the middle column while exercises 2–6 sit in the right column (in all other editions 1–6 are together in the right column). Numbering/content complete, no overlap; visually detached.
- **T-1 — ZH-TW P8 header separator dropped (trivial; ZH-TW only).** P8 header line reads `Alle Antworten unten auf dieser Seite 答案在本版下方` with no `—` separator between the German sentence and the Chinese gloss (all other editions have ` — `). Readable (script change marks the boundary); restore the separator for consistency.
- **O-1 — Core/ZH-CN masthead badge slot (observation, NOT a defect; PASS).** Core + zh-cn retain the German subtitle slot (`DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`, fill `#57523f` grey) with no distinct pairing-badge line; the pairing is still visible via the Chinese edition line (y=330), the Chinese strapline, and the footer. The zh-cn footer carries the English brand lockup `LUCERNA GERMAN WEEKLY`. Recorded, not counted against the editions.
- **Trivial, not a defect (zh-cn/core only):** P8 key note for item 67 reads `（上午狂欢，下午圣马丁）` — St. Martin lanterns are in the evening (Abend), not the afternoon. The German item itself is correct; the note reproduces the core's morning/afternoon simplification, also present in every edition's key 67 note.

## 4. Gate outputs summary (all re-run independently by the proofreader; outputs under `de-proofread-gates/`)

- **Freeze** (`freeze.py diff --strict-cjk`; JSONs in `freeze/`): en/es/fr/it/nl/pt/ru exit 0, added CJK 0; ja exit 1, 3276 added CJK (expected Japanese); ko exit 1, 3196 added CJK (expected Hangul); zh-tw exit 1, 1043 added CJK (expected Traditional); zh-cn exit 0, +0/−0 (identical to core). The ONLY long German-only removed string in every fan-out is the P1 subtitle slot, replaced by the pairing badge (documented furniture). No German article text removed/changed; German-token multiset diff for ja/ko/zh-tw shows zero added German tokens (one KO `A` is the `A매치` gloss). JA/KO/ZH-TW added-string scans show no new German body text. **Verdict: freeze HOLDS** (modulo the KIT staleness note below).
- **Builder freeze archives STALE for en/nl/ru (documentation discrepancy, NOT an edition defect):** builder JSONs predate the final occlusion-fix trims (e.g. builder de-en freeze has `This week's big questions · Die Fragen der Woche`, shipped SVG has `Big questions · Die Fragen der Woche`; nl p7 +62 shipped vs +63 builder; ru p7 +62 vs +63). This proofreader's re-runs are current; the edition files are clean.
- **P8** (`p8.py compare`; JSONs/txt in `p8/`): ALL 11 editions CLEAN — 150 noted = 150 noted, missing=[], extra=0, uncertain=[]. keydiff=[137,138,139,150] in all except zh-cn ([]). **Keydiff adjudication CONFIRMED legitimate:** 137–139 are E-section translation items (core key = Chinese translation, e.g. 137 `狂欢节11 点 11 分在科隆开幕。`; fan-outs = reader-language translation, e.g. en `The carnival opens at 11.11 in Cologne.`, zh-tw `狂歡節 11 點 11 分在科隆開幕。`); 150 is the translated "open task" label (core `开放题`, en `Open task`, etc.). All 150 P8 answers verified correct against their questions in the core read; P8 translated notes read in full for all 10 fan-outs — correct throughout (findings above are the only exceptions).
- **Occlusion** (`occlusion_audit.py`; JSONs/txt in `occlusion/`): 0 flags for core + all 11 editions; synthetic selftest OK on every run (all 6 planted classes fired, clean controls silent). The audit does not cover text-vs-chart-bar overlap; the one suspect case (EN P6 `remembrance` label vs. 20% bar) was pixel-measured: label ink ends x=533, bar starts x=535 — 2px clear, fully visible, no defect.
- **Counts** (`count_exercises.py`, `counts.json`): SVG scan gives 149 numbered items + writing item 150 (no printed number, present in P8 set) = **150 total** in core + all 11 editions; per-page P1 10 · P2–P6 18 each · P7 12 · P8 38; numbering continuous 1–150. Level split verified two ways (chip scan reconciled via registry; static read-only parse of frozen build sources `content12/34/56/7/8.py`): **A2 66 / B1 70 / B2 14**, sum 150. KIT totals CONFIRMED.
- **P6 chart:** bar rect widths 782 / 578 / 340 px at x=535 in core + all 11 editions = exactly 46/34/20 (×17), sum 100; labels `46 %`/`34 %`/`20 %` present; ÜBUNGSDATEN practice-data disclaimer present in every edition.
- **P7 golden sentences (8):** exactly 2× each in every edition; source-page + P7 attribution verified for core/en/ja/zh-tw: (1) `Die Bundesliga pausiert — aber die Nationalmannschaft spielt.` (S.4); (2) `Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.` (S.2); (3) `Sein Gedenktag ist der 11. November.` (S.3); (4) `Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.` (S.5); (5) `Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.` (S.2); (6) `Das Spiel ist ausverkauft, RTL überträgt live.` (S.4); (7) `Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.` (S.6); (8) `Am Sonntag ist es still im Land.` (S.6). Golden-sentence translations read in all 11 editions — accurate.
- **MUSTER:** 84 words by whitespace count in core + all 11 editions; labels translated (core `范文（84 Wörter）` pattern retained in ja/zh-tw — faithful to core, not a defect).
- **Weekdays** verified with `TZ='Europe/Berlin' date -d`: 2026-11-09 Mon, 11-10 Tue, 11-11 Wed, 11-12 Thu, 11-13 Fri, 11-14 Sat, 11-15 Sun, 11-16 Mon, 11-18 Wed, 11-20 Fri, 11-21 Sat, 11-22 Sun, 11-24 Tue, 11-25 Wed, 11-26 Thu, 11-27 Fri, 11-05 Thu — all match KIT claims.
- **Badge/footer (measured from SVG + rendered pixels, `masthead-pixels*.json`):** P1 badge text present, x=975 middle-anchored, in all 11 fan-outs. Rendered fills: de-en `#3e4c2a` (olive); de-es/fr/it/ja/ko/nl/pt/ru/zh-tw `#a4553a` (brick) — pixel-confirmed (olive RGB 62,76,42; brick RGB 164,85,58). Core + zh-cn: grey subtitle slot, no distinct badge line (see O-1). Footers present 8/8 in every edition with correct pairing text; page lines correct 8/8. Masthead pixel check: ink within x 64–1884 / y 71–299 on every P1, clear of the frame; no ink touches any frame edge on any P1/P8 (ink bbox inset = the page border itself at 26px).
- **PDFs:** every web PDF < 7 MB (largest zh-tw 2,038,435 bytes; core 1,670,902; en 1,064,521; ru web 1,105,087 despite a 40,640,945-byte print PDF). pdftotext bytes > 0 for all web + print PDFs. Web/print NORMALISED text EQUAL for all 12 dirs (`pdf-text-equality.txt`). KIT byte claims CONFIRMED exactly.
- **ABSTRACT.txt:** all 12 dirs single-line, 0 ASCII double-quotes, reader-native — format PASS; framing FAIL (D-ABSTRACT).
- **Reader-facing sweep** (SVG text, all pages, all editions): only hits are `VOL.4` in P3/P7/P8 — all legitimate next-issue references (Rückblick promise, disclosure, teaser). No week/language codes, repo links, SOP/proofread/audit wording, or stale terms (VOL.2, Tankrabatt, etc.). CLEAN.
- **Script purity:** Latin editions zero CJK/Cyrillic/fullwidth chars. ru: Cyrillic only, no CJK. ja: han+hiragana+katakana, no Hangul; `国/点/静` verified in context as legitimate Japanese shinjitai; JA section headers `LEBEN · 生活` / `KULTUR · 文化` are shared kanji, legitimate Japanese (KIT-documented identity exemptions — CONFIRMED). ko: Hangul only, zero han/kana. zh-tw: zero Simplified-only chars in curated check; conversion spot-checks pass (`意味着 → 意味著` verified in golden sentence 7; `觀衆/麪/裏/週/與/釋義` correct). zh-cn: zero Traditional-only chars. Simplified vs Traditional independence CONFIRMED (no conversion residue either way).
- **Core German read (full):** core `.text.md` P1–P8 end-to-end + P7/P3/P5/P6 box bodies + P4 SPIELPLAN table + P8 keys region. All 150 P8 answers correct. SPIELPLAN 8 rows + note line verified (weekdays, times, 22 Nov note, no club European games statement). P3 box states processions "oft auch an Abenden vor oder nach dem 11. November" (resolves the exercise-40 concern). P2 Rechnen duplication in `.text.md` is export-only (SVG count = 1), NOT a page defect. D-CORE-1 is the only factual defect in the core German text.
- **Cards/visual:** P1 + P8 viewed at full frame for all 11 editions (22 cards) — no overflow, overlap, missing glyphs/tofu, or missing image credits; all PASS visually (KO P1 flow quirk M-6 noted). Spot checks: EN P6 (chart), EN P7, NL P6 (D-NL-1 confirmed), KO P5 (D-KO-1 confirmed), core P2 (D-CORE-3 confirmed), JA P2 (M-5 confirmed), ZH-TW P6 (M-5 confirmed). NL P1 stray `4.` fragment from the added-string dump resolved: normal FRAGEN list item 4, not a defect. The rejected American-football photo is absent (no DVIDS 52594626900 string in pages).

## 5. W45 promises — verification table

Source: `hidden_files/w46/w45-promises.md` DE section + core KIT §3. All honoured:

| # | W45 promise | Status / evidence |
|---|---|---|
| 1 | 15 Nov Volkstrauertag + NFL Munich as previews, no results | VERIFIED — previews on P1/P4/P6; no results claimed (games are in-week/future at press time) |
| 2 | 11 Nov St. Martin | VERIFIED — P2/P3/P5/P7 |
| 3 | European return legs | VERIFIED — Nations League return legs in-week + club cups 24–26 Nov + explicit "no club European games in this week" (P4 note line) |
| 4 | No fabricated readers/letters | VERIFIED — P7 readers' corner in every edition retains German disclosure `Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.4.` + German invitation + editor's example signed `die Redaktion` + reader-language disclosure; zh-tw keeps German label `Ein Beispiel der Redaktion!` per documented W45 exemption; promise carried to VOL.4 |
| 5 | 3–8 Nov UCL/UEL/Bundesliga MD9 results deferred to VOL.4, no scores invented | VERIFIED — P3 Rückblick paragraph + P7 teaser; no scores invented |
| — | P7 teaser contents (frozen German, identical across editions) | VERIFIED (EN P7 card): Bundesliga return Fri 20 Nov Bayern–Köln, European matchdays 24–26 Nov, Buß- und Bettag, Totensonntag, 3–8 Nov results, real letters in VOL.4 |

## 6. KIT claim adjudications (summary)

- **CONFIRMED:** 150 exercises + level split; 8/8 verbatim golden sentences; MUSTER 84; chart 46+34+20=100; occlusion 0 (final audits); P8 CLEAN + keydiff legitimacy; freeze added-CJK totals; PDF sizes/text equality; badge/footer strings and fills (except O-1); W45-promise record; image credits/PD status (captions generic, no false match claims); KO badge addition (badge present on KO P1); JA kinsoku re-wrap via svglib (content token-identical; 1 dangling-（ exception → M-5); ZH-TW opencc conversion spot-checks; ES `ofrenda` shortening as documented.
- **REFUTED / STALE:** builder freeze JSONs for en/nl/ru predate final occlusion-fix trims (documentation only); KO KIT §4 orphan-。 fix claim REFUTED (D-KO-1: orphans still present, 3 instances).
- **UNVERIFIABLE:** none material. (Builder gate log `de-gates.log` freeze lines for nl/ru reflect the same pre-trim counts as the stale JSONs.)

## 7. Seed record (for the coordinator's insert step)

- **VOL number:** VOL.3.
- **Exercise total + level split (re-measured):** 150 total; A2 66 / B1 70 / B2 14. Per-page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
- **Core P1 article opening sentences verbatim (German):** `Diese Woche spielt die Bundesliga nicht: Es ist Länderspielpause. Die deutsche Nationalmannschaft trifft am Freitagabend in Belgrad auf Serbien — und am Montag danach in Berlin auf die Niederlande. Es geht ums Viertelfinale.` (Next sentence: `Am Freitag (20.45 Uhr) spielt Deutschland in Belgrad — vor leeren Rängen. Am Montag (20.45 Uhr) folgt das Heimspiel gegen die Niederlande in Berlin.`)

## 8. Gate artefacts saved

All under `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/de-proofread-gates/`:
`freeze/` (per-edition freeze JSONs), `p8/` (per-edition compare JSONs/txt), `occlusion/` (per-edition audit JSONs/txt), `added/` (per-edition added-string dumps P1–P7), `p8notes/` (per-edition P8 added/removed dumps), `counts.json`, `pdf-text-equality.txt`, `masthead-pixels.json`, `masthead-pixels2.json`, `orphan-kinsoku-scan.txt`, `count_exercises.py`, `dump_added.py`, and this verdict file.

## 9. Recommended follow-ups (builder/coordinator — proofreader must not fix)

1. Fix D-CORE-1 in the frozen core (P4 caption), re-derive all 11 editions' P4 from the fixed core (caption only; no other P4 change).
2. Rewrite all 11 ABSTRACT.txt closings to practice framing (frontmatter/ABSTRACT-only; no re-render). Resolve the SOP §9 tension explicitly so Round 2 has one rule.
3. Fix D-TOOLBOX glosses (6 editions), D-IT-1, D-NL-1, D-RU-1 (single-line gloss edits; re-render affected pages only: P7 en/es/fr/it/pt/ru; P3 it; P6 nl; P7 ru).
4. Fix D-CORE-3 + D-KO-1 orphans (re-wrap), M-1 header glosses, M-5 wrap punctuation, M-6 KO P1 flow, T-1 separator, D-PT-1 address form; consider M-2/M-3/M-4.
5. Re-run freeze + P8 + occlusion + counts after fixes; Round 2 independent proofread must confirm zero before ship. The stale builder freeze archives for en/nl/ru should be regenerated from the fixed build so the record matches the shipped files.

**ROUND 1 FAIL** — blocking defects: D-CORE-1, D-ABSTRACT, D-TOOLBOX (en/es/fr/it/pt/ru), D-IT-1, D-NL-1, D-RU-1.
