# Proofreader Verdict — Round 2 — Lucerna Weekly W46 (FR target)

- **Issue:** VOL.4, dated Mon 2026-11-09 – Sun 2026-11-15.
- **Scope:** all 11 FR-target editions (one per reader-native language): fr-de, fr-en, fr-es, fr-it, fr-ja, fr-ko, fr-nl, fr-pt, fr-ru, fr-zh-cn, fr-zh-tw. Frozen FR core (`weekly-report-w46-fr-core/`) used as the comparison baseline.
- **Proofreader role:** independent Round 2. The proofreader did NOT build or fix these editions, fixed nothing, re-rendered nothing, and edited no edition file.
- **Round 1 verdict (reference):** `hidden_files/w46/fr-proofread-gates/proofreader-verdict-round1.md` — FAIL all 11 (D1, D2, D3 + F-MAIL flag).
- **Fix record (verified, not trusted):** `hidden_files/w46/fr-fix/FIX-REPORT.md` + the "补记" sections appended to all 12 `WEEKLY-KIT.md` files.
- **Gate outputs (this round, independent re-runs):** `hidden_files/w46/fr-proofread-gates-round2/` — `proofreader-freeze-*.json` + `proofreader-freeze-all.log` + `proofreader-freeze-adjudication.txt`; `proofreader-p8-*.json` + `proofreader-p8-all.log`; `proofreader-occlusion-*.json` (+ `-core`) + `proofreader-occlusion-all.log`; `proofreader-pdfs.log`; `proofreader-residue.log`; `proofreader-visual-round.log`; SVG `<text>` extractions in `text/` (96 pages).
- **Date of verification:** 2026-11-03 (UTC gate logs; cards rendered 2026-11-03 00:41, post-fix).

## Per-edition verdict

| Edition | Verdict |
|---|---|
| 2026-w46-fr-de | **PASS** |
| 2026-w46-fr-en | **PASS** |
| 2026-w46-fr-es | **PASS** |
| 2026-w46-fr-it | **PASS** |
| 2026-w46-fr-ja | **PASS** |
| 2026-w46-fr-ko | **PASS** |
| 2026-w46-fr-nl | **PASS** |
| 2026-w46-fr-pt | **PASS** |
| 2026-w46-fr-ru | **PASS** |
| 2026-w46-fr-zh-cn | **PASS** |
| 2026-w46-fr-zh-tw | **PASS** |

No blocking defect remains. The only residual items are R1 (déjà omission, adjudicated non-blocking — see §3), R2 (internal KIT documentation inaccuracy, non-blocking — see §6), and the open coordinator mailbox check F-MAIL (not a text defect — see §7).

## 1. Fix verification

Adjudication scale: CONFIRMED = fix claim verified verbatim in the final artifacts; PARTIAL = fix present but incomplete; REFUTED = claim contradicted by the artifacts. Every claim below was checked in the final SVGs (via `<text>`-only extractions), the `.text.md` exports, and the rendered cards — not from the fix worker's gate JSONs.

### D1 — P3 item 37: `ne...plus` presupposition (core + all 11 editions)

**CONFIRMED in all 12 directories (core + 11 editions).**

Evidence (identical in every directory; wrap-tolerant counts over the full SVG text, 1 occurrence each):

- P3 stem, item 37: `(pas) La foire est à Paris. → ___` (e.g. `.text.md` line 367 in every edition; SVG text nodes, P3).
- P8 key, item 37: `La foire n'est pas à Paris.` (e.g. `.text.md` line 1035 in every edition; wrapped continuations verified for core/es/ja/ko/nl/ru/zh-cn/zh-tw, single-line in de/en/it/pt).
- `n'est plus`: 0 occurrences; `(plus)`: 0; `ne...plus`: 0 — in every directory's SVG text nodes and `.text.md`. Remaining `plus` tokens are legitimate comparatives (P4 `plus vite`, P7 `plus / moins`, etc.).
- Negation bridge consistent: every P3 rewrite header lists only `ne...jamais / ne...pas` (e.g. core `改写句子（用 ne...jamais / ne...pas）。`, de `Sätze umschreiben (mit ne...jamais / ne...pas).`, ru `Перепиши фразы (с ne...jamais / ne...pas).`). P8 notes show only `ne...jamais` (item 105) and `ne...pas encore` (item 139). No "no longer" sense remains anywhere (native glosses checked: no `nicht mehr`, `no longer`, `ya no`, `non più`, `niet meer`, `não mais`, etc.; French `mais` hits are the conjunction "but").
- Regression sweep on P3: items 35/36/37 read coherently as a set — 35 `(jamais) La flamme s'éteint.`, 36 `(pas) On oublie les morts pour la France.`, 37 `(pas) La foire est à Paris.` — with matching keys 35/36/37 on P8. No new defect introduced on P3. P3 card viewed (core): negation block renders cleanly, no overflow.

### D2 — P8 item 135 stems (fr-it, fr-nl, fr-pt, fr-ru, fr-ja, fr-ko)

**CONFIRMED in all 6 fixed editions.** Each new stem was verified for meaning in its native language (not merely "text changed"), and each expresses reading-a-programme → understanding-France. The other 5 editions' accepted stems are **CONFIRMED untouched**.

| Edition | New stem (P8, line after `135.`) | Meaning check |
|---|---|---|
| fr-it | `Leggere un programma è capire la Francia.` | "Reading a programme is understanding France." Equative, correct. |
| fr-nl | `Een programma lezen is Frankrijk kennen.` | "Reading a programme is knowing France." Equative, correct. |
| fr-pt | `Ler um programa é compreender a França.` | "Reading a programme is understanding France." Equative, correct. |
| fr-ru | `Читая программу, понимаешь Францию.` | "Reading a programme, you (= one) understand France." Gerund + generic-you, correct and natural. |
| fr-ja | `番組表を読むとフランスが分かる。` | "When you read the programme listing, you understand France." Conditional と, correct. |
| fr-ko | `프로그램표를 읽으면 프랑스를 이해한다.` | "If/when you read the programme listing, you understand France." Conditional -면, correct. |

Old wrong stems are gone from all six editions: no `Un programma spiega la Francia.`, `Een programma legt Frankrijk uit.`, `Um programa explica a França.`, `Программа объясняет Францию.`, `番組がフランスを説明する。`, or `프로그램이 프랑스를 설명한다。` in any SVG text or `.text.md`.

Untouched accepted stems confirmed present and unchanged (SVG + `.text.md` line 995):

- fr-de: `Programm lesen heißt Frankreich kennen.`
- fr-en: `Reading a programme is knowing France.`
- fr-es: `Leer un programa es conocer Francia.`
- fr-zh-cn: `Traduisez: 读一份日程，本身就是在了解法国。`
- fr-zh-tw: `看一份行程就了解法國。`

Regression sweep on P8: item 135 + dialogue block (145–149, `Merci !`) checked in all 6 fixed editions — text and cards. `Merci !` is fully visible in every edition (see §5). No new defect introduced on P8. The déjà question is adjudicated separately in §3 (R1).

### D3 — P4 `familier` gloss (fr-ja, fr-ko, fr-ru, fr-zh-tw)

**CONFIRMED in all 4 fixed editions.** The text occurrence is `les noms des villes deviennent familiers` ("become familiar") in all editions; the glosses now give the familiar sense:

| Edition | Gloss now | Before (Round 1) |
|---|---|---|
| fr-ja | `familier なじみのある` | `familier くだけた` (colloquial) |
| fr-ko | `familier 친숙한.` | `familier 구어체` (colloquial) |
| fr-ru | `familier знакомый.` | `familier разговорное` (colloquial) |
| fr-zh-tw | `familier 熟悉的。` | `familier 口語` (colloquial) |

No `くだけた / 구어체 / разговорное / 口語` gloss for `familier` remains in the four fixed editions. Untouched correct editions confirmed: de `familier vertraut.`, en `familier familiar.`, es `familier familiar.`, it `familier familiare.`, nl `familier familiair.`, pt `familier familiar.`, core/zh-cn `familier 熟悉的。`. Regression sweep on P4: gloss + surrounding paragraph checked (card viewed for fr-ko: `familier 친숙한` inline, no overflow). No new defect introduced on P4.

### Fix-verification table (summary)

| Edition | D1 | D2 | D3 |
|---|---|---|---|
| fr-de | CONFIRMED | n/a (stem untouched, confirmed) | n/a (gloss already correct, confirmed) |
| fr-en | CONFIRMED | n/a (stem untouched, confirmed) | n/a (gloss already correct, confirmed) |
| fr-es | CONFIRMED | n/a (stem untouched, confirmed) | n/a (gloss already correct, confirmed) |
| fr-it | CONFIRMED | CONFIRMED | n/a (gloss already correct, confirmed) |
| fr-ja | CONFIRMED | CONFIRMED | CONFIRMED |
| fr-ko | CONFIRMED | CONFIRMED | CONFIRMED |
| fr-nl | CONFIRMED | CONFIRMED | n/a (gloss already correct, confirmed) |
| fr-pt | CONFIRMED | CONFIRMED | n/a (gloss already correct, confirmed) |
| fr-ru | CONFIRMED | CONFIRMED | CONFIRMED |
| fr-zh-cn | CONFIRMED | n/a (stem untouched, confirmed) | n/a (gloss already correct, confirmed) |
| fr-zh-tw | CONFIRMED | n/a (stem untouched, confirmed) | CONFIRMED |

(Core: D1 CONFIRMED; core has no D2/D3 edition layer.)

## 2. Déjà verdict (required explicit adjudication)

**Question (a): does the printed French key contain "déjà"? YES.** In all 12 directories (wrap-tolerant count, exactly 1 occurrence each): `Lire un programme, c'est déjà comprendre la France.` Each edition's key gloss anchors `lire un programme = …` in the reader's native language (e.g. de `lire un programme = ein Programm lesen`, en `lire un programme = to read a programme`, it `lire un programme = leggere un programma`).

**Question (b): the stems omit "déjà" — is the item still fair/solvable as printed, or a residual defect requiring a layout change? VERDICT: fair and solvable as printed. The omission is a NON-BLOCKING residual imperfection (R1), not a defect, and no layout change is required.**

Reasoning:

1. **Déjà carries emphasis, not propositional content.** Agent (the reader), action (reading a programme), and result (understanding France) are all correct in all six new stems. A faithful translation of any of the six stems differs from the printed key only by the emphatic adverb déjà. No stem states anything false, and no learner is misled about the meaning.
2. **The issue itself teaches déjà as emphasis.** The P7 grammar note under golden sentence Q103 glosses it exactly so (EN edition): `Grammar | c'est déjà: already is (emphasis).` The learner meeting the key on P8 has already been told déjà is an emphatic addition.
3. **Family parity.** The five Round-1-accepted stems omit déjà in exactly the same way (EN `Reading a programme is knowing France.`, DE `Programm lesen heißt Frankreich kennen.`, ES `Leer un programa es conocer Francia.`; zh-cn/zh-tw carry only the particles 本身就是 / 就). The six fixed stems now match the family's established pattern exactly. Holding the six to a stricter standard than the five accepted stems would be inconsistent, and "fixing" the omission would mean re-laying-out all 11 P8s, not six.
4. **The key is on the same page.** The learner compares stem and key on P8 itself, with the `lire un programme` gloss beside the key; the only delta visible is déjà. The item remains solvable: the expected answer is the printed French sentence, and any of the six stems leads the learner to it.
5. **Déjà-faithful forms were tried and demonstrably overflowed.** The fix worker's first attempts — IT `Leggere un programma è già capire la Francia.`, NL `Een programma lezen is al Frankrijk begrijpen.`, PT `Ler um programa é já compreender a França.`, RU `Читать программу — это уже понимать Францию.`, JA `番組表を読むことは、すでにフランスを理解することだ。`, KO `프로그램표를 읽는 것은 이미 프랑스를 이해하는 것이다。` — produced an identical COVER flag in all six editions in the intermediate gates (`hidden_files/w46/fr-fix/gates/`, `gates-all.log` lines 171–192): P8 `Merci!` 71% covered by a later rect box `[988.3, 1499.3, 1885.7, 1788.7]`. (The fix report's flow-end measurement y=1502→1552 is taken from that report, not independently re-measured; the occlusion flags themselves were verified in the intermediate gate files.) Re-laying-out all 11 P8s for one emphatic adverb would be disproportionate and would require a fresh full proofread round.
6. **No stem is unnatural in its own language.** IT/NL/PT use the natural equative construction; RU uses a gerund with generic-you; JA/KO use the natural conditional (と / -면, "when/if you read…"). None reads as a mistranslation.

Recorded as residual imperfection R1 (see §6). It does not block shipping.

## 3. Full re-gate (independent; fix worker's JSONs not trusted)

All gates re-run by the proofreader on the final artifacts with the shared toolkit (`tools/venv/bin/python`).

- **Freeze** (`tools/freeze.py diff` vs frozen FR core; `proofreader-freeze-all.log`, 2026-11-03T01:44:13Z; `proofreader-freeze-<native>.json`; `proofreader-freeze-adjudication.txt`): **PASS as adjudicated, all 11.** P1–P7 removed-noCJK = 0 in all 11 (under the tool's CJK definition, which counts fullwidth/CJK punctuation such as 。/）。 as CJK-range; Round 1's two punctuation-only fragments therefore do not appear separately). P8 removed-noCJK are only re-wrap fragments (`24. c · 25. d`; `36. On n'oublie pas les morts pour la France. · 37. La foire`; `Paris Photo jeudi. · 17. Tu vas raconter ton mercredi férié.`). Added CJK: de/en/es/it/nl/pt/ru = 0; ja = 2,281; ko = 2,460; zh-tw = 1,010; zh-cn = 0 differences on all 8 pages. Strengthening check: every core long pure-French text node (length ≥ 20, no CJK) on P1–P7 appears verbatim in every edition (0 missing); P8 absences (6–8 per edition) are re-wraps, settled by p8.
- **P8** (`tools/p8.py compare`; `proofreader-p8-all.log`; `proofreader-p8-<native>.json`): **CLEAN for all 11.** Core and edition both 116 noted; missing = [], extra_count = 0, uncertain = []; keydiff = [145] for all except fr-zh-cn keydiff = []. Core noted set 121/150. Keydiff [145] adjudicated: the key word is identical (`145. samedi`); only the parenthesised native date gloss differs (core `11 月 14 日星期六` vs e.g. de `Samstag, 14. November`) — legitimate re-aim, same as Round 1. Keys 37 and 135 are NOT in any keydiff list. (Discrepancy with the fix record's keydiff=[150] claim: see R2, §6.)
- **Occlusion** (`tools/occlusion_audit.py`; `proofreader-occlusion-all.log`; `proofreader-occlusion-*.json` incl. `-core`): selftest OK on every run; **0 flags for core + all 11 editions** (96 pages).
- **Counts — 150 exercises, re-measured:** answer keys 1–150 complete (missing = []) in all 12 `.text.md` exports (answers section after the last `RÉPONSES` header; section-first keys 1/11/26/44/62/79/97/109 accounted for). Stems 1–149 (line stems + grouped ranges 22–25, 49–52, 73–76, 85–88, 140–144 + dialogue blanks 145–149); item 150 is the unnumbered writing prompt (`Écrivez un petit texte… « Mon mercredi 11 novembre »`, 80–100 words) with key 150 present as an open-question note. Per-page distribution: P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42 = 150 (P8 = 41 numbered stems 109–149 + item 150). Matches the core KIT claim.
  - Level totals NOT independently reproducible (same conclusion as Round 1; not a defect): standalone A2/B1/B2 badge tokens in SVG text are 41/62/21 (total 124) identically in core/en/zh-tw; the KIT's `A2 52 · B1 75 · B2 23` cannot be re-added from the printed artifact without the builder's registry (shared/group badges for matching and dialogue blocks). The measured numbers are recorded here; 52/75/23 is NOT presented as verified.
- **P6 "chart":** P6 has no bar chart; it is a calendar/timeline graphic (`LE CALENDRIER · 预算日程`). Quantitative claims verified consistent across all editions: `115–1` (P6 twice + `115` on P1) and `404–1` (P6, last year's rejection) in every edition's P1/P6/P8 text. Weekday claims verified: 9 Nov 2026 = Monday, 11 Nov = Wednesday, 14 Nov = Saturday, 15 Nov = Sunday — matching `lundi 9`, `mercredi 11`, `samedi 14`, `dimanche 15`. The P6 self-correction box (W45 calendar promise) is present in all editions.
- **P7 verbatim quotes:** all 8 golden sentences in `LES PHRASES DE LA SEMAINE` verified as verbatim contiguous excerpts from the issue's own articles with correct page attributions (Q97 p.1 Senate; Q98 p.3 Armistice; Q99 p.2 flame; Q100 p.1 three tempos; Q101 p.3 herring/scallop; Q102 p.4 VOL.5 results; Q103 p.2 déjà/lire; Q104 p.6 government text). Grammar-column constructed examples (futur proche, B2 `Il est prévu que…`) and the SI excerpt are teaching transformations/truncations, not 金句 defects. Clinic errors 105–108 are intentionally wrong, marked ✗. Toolbox three phrases are verbatim.

## 4. Native-language correctness / residue sweep

- **Script residue** (`proofreader-residue.log` §5): Latin editions (de/en/es/it/nl/pt) — 0 Han, 0 Hangul, 0 Kana, 0 Cyrillic. RU — 6,028 Cyrillic, 0 Han. KO — 2,456 Hangul, 0 Han (no Hanja). JA — Han 1,288 + Kana 1,401; simplified-only scan: the only hits under a broad simplified set are 点 (5) and 学 (2), all legitimate Japanese jōyō kanji in context (要点, 不明, 締切, 学校, ポイント) — no simplified-Chinese residue. ZH-TW — 0 simplified-only hits under a broad set (incl. 学/点/习/观/听/见/头/后/里/万/与/从/众/买卖/劳/显/亲/双/发/干/余/愿/怀/坏/态/惊/旧/归/备/复/声/处/尽/岁/异/弃/张/弹/当/录/忧/忆/护/报/担/拣/拥/拨/择/敌/斋/暂/权/杆/树/样/梦/检/楼/欢/汤/沟/没/泪/浅/浇/测/浏/涨/涂/润/渔/点/烂/烟/烧/热/爱/犹/独/献/现); ZH-CN — 0 traditional-only hits. Simplified and Traditional Chinese remain independent editions, never converted.
- **Cross-language contamination markers:** word-boundary scans for other natives' function words in each Latin/RU edition found only one hit class — Spanish `dos` inside the ES edition (correct Spanish). No German/English/Spanish/Italian/Dutch/Portuguese residue in any other edition.
- **Badge/footer:** pairing badge line present and visible under the P1 masthead in all 11 editions, in the reader's native language (e.g. de `FRANZÖSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`; ja `フランス語テキスト · 日本語の解説 — 日本語読者のための版`; zh-tw `法語正文 · 繁體中文講解 — 給繁體中文讀者的版本`), confirmed visually on all 11 P1 cards. Footer line (`Le Lucerna · … VOL.4 · TEXT … · EXPLANATIONS …`) present on all 8 pages of all 11 editions (96/96 pages).
- **Explanations/glosses/notes/footers** are in the reader's native language throughout (spot-read across P1–P8 in all editions; freeze added-string totals consistent). No untranslated strings, no wrong-script residue found.

## 5. Cards (visual round)

Viewed at full frame: **P1 and P8 of every edition (22 cards)**, plus spots — P2 (en), P3 (core), P4 (ko), P5 (ja), P6 (core), P7 (en). Log: `proofreader-visual-round.log`. **Visual defects: none.** In particular:

- P8 in the 6 D2 editions (it/nl/pt/ru/ja/ko): `Merci !` fully visible in the dialogue block; no box covers it; writing strip + model text clear of the answers block; no overflow, overlap, or tofu.
- P3 (core): negation block 35–37 renders cleanly; botanical plate with Flora de Filipinas credit visible.
- P4 (ko): D3 gloss `familier 친숙한` inline and fully visible.
- P6 (core): timeline + self-correction box + figures + source line clean.
- P7 (en): golden sentences, clinic, readers'-letters box (FR label + FR note + EN note), hedged next-week box — all clean.
- P1 (all 11): badge visible, footer correct, Atget photo + credit visible, no overflow/overlap/tofu.
- P2 (en): Hiroshige print + LACMA credit visible. P5 (ja): CJK-dense, no tofu.
- Image credits present: Eugène Atget (P1), Utagawa Hiroshige (P2), Flora de Filipinas botanical plate (P3) — all public-domain, credited in every edition.

## 6. PDFs, ABSTRACT.txt, KIT fix record, W45 promises

- **PDFs** (`proofreader-pdfs.log`, independent pypdf + `pdftotext` run): every edition 8 pages; every web PDF has a real text layer (pdftotext bytes > 0) and is ≤ 7 MB (largest: zh-tw web 2,400,946 B; smallest: it web 1,341,501 B). Web-PDF extracted text is **hash-identical** to the print-PDF extracted text in every edition (SHA-256 prefix match, e.g. core/zh-cn `1b50208d651bc3a1`, de `e3e05b11971c025c`, ru `7dc26f49edecec28`). Print PDFs are large (up to 23.7 MB, ja) but the ≤ 7 MB rule applies to the web PDFs, which all satisfy it.
- **ABSTRACT.txt** (all 12 files): single line (0 newlines, no trailing newline), no ASCII double-quote, written in the reader's native language, naming the real topics (Senate debate 9 Nov, Armistice 11 Nov, Dieppe 56th herring/scallop fair 14–15 Nov, Paris Masters results pending, Turin Finals, Nations League/Les Bleus, Paris Photo) plus masthead, target-language name, A2–B2, and 150 exercises. Core ABSTRACT is byte-identical in content to zh-cn (expected; core is zh-cn-based). JA/KO/RU abstracts explicitly mark Masters results as pending at press time.
- **KIT fix record ("补记"):** present in all 12 `WEEKLY-KIT.md` files (2026-11-03), with defect/fix before-after quotes, source files changed, re-render numbers, and re-gate evidence, plus the F-MAIL flag carried forward as still open. Spot-read in full for fr-it (D1/D2 + re-gates) and fr-ja (D3). Content is substantive and matches the artifacts.
- **W45 promises honoured:** Paris Masters results deferred, never invented (Sinner appears only as withdrawal/absence: `Sinner n'a pas joué`, `Turin sans Sinner`; winner deferred: `avec le nom du vainqueur`, `les résultats… seront dans le VOL.5`); budget-vote self-correction box present (P6); 18 Nov solemn vote hedged (`est prévu`, P7 next-week box); reader's-corner example labelled as editorial example (P7). No invented winner anywhere in P4/P5/P7 text.
- **R2 — internal documentation discrepancy (non-blocking):** the KITs (original build § + fix 补记) and FIX-REPORT state `p8.py compare` keydiff = `[150]`. The proofreader's independent Round 1 and Round 2 runs both measure keydiff = `[145]` (all editions except fr-zh-cn, which is `[]`), adjudicated legitimate (identical key word `samedi`; only the native date gloss differs). The artifact itself passes p8 CLEAN under both rounds; the `[150]` figure describes some other comparison (presumably against the build registry) and is wrong as a description of the core-vs-edition comparison. Internal documentation only; reader-facing artifacts unaffected; does not block shipping. Flagged here so the record is accurate.

## 7. F-MAIL wording check (coordinator check — wording only)

**Wording present and consistent in all 11 editions + core.** In every edition's P7 (SVG text, 1 occurrence each):

- French label: `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`
- French note: `Note de la rédaction: aucun texte du VOL.3 n'était arrivé au moment de mettre sous presse. Le VOL.5 reprendra la promesse.`
- Native-language note to the same effect (de `Anmerkung der Redaktion…`, en `Editor's note…`, es `Nota de la redacción…`, it `Nota della redazione…`, ja `編集部注…`, ko `편집부 알림…`, nl `Opmerking van de redactie…`, pt `Nota da redação…`, ru `Заметка редакции…`, zh-cn `编辑部说明…`, zh-tw `編輯部說明…`). Visually confirmed on the EN P7 card (all three elements visible in the readers'-letters box).

The underlying no-submissions premise is unverifiable without mailbox access and is NOT the proofreader's to clear. **The mailbox check remains OPEN for the coordinator before insert** — covering submissions of any vintage (the wording's "VOL.3" scope does not by itself settle whether anything arrived). This is not a text defect and does not block the proofread verdict; it is a pre-insert coordinator action. The fix worker correctly did not touch this wording.

## 8. New / residual defects

**No new defects were found. No blocking defect remains.**

Residual list (complete):

- **R1 — Déjà omission in item 135 stems (all 11 editions, including the 5 Round-1-accepted stems).** Adjudicated in §2: non-blocking residual imperfection. The printed key contains déjà; the stems omit it; the item is fair/solvable as printed; no layout change required.
- **R2 — KIT/FIX-REPORT p8 keydiff figure `[150]` vs independently measured `[145]`.** Internal documentation inaccuracy only; artifact passes p8 CLEAN. Non-blocking.
- **F-MAIL (open coordinator action, not a defect):** mailbox premise unverified; wording present and consistent (§7). The coordinator must check the mailbox before insert.
- **Level totals (unverified metadata, not a defect):** KIT claim A2 52 / B1 75 / B2 23 is not reproducible from the printed artifact (measured standalone badge tokens 41/62/21). Same standing as Round 1.

## Final verdict

**ROUND 2 PASS (all 11 shippable)**

All three Round 1 defects are CONFIRMED fixed in the final artifacts with no regressions; all gates pass independently (freeze PASS as adjudicated, p8 CLEAN, occlusion 0 flags, PDFs text-layered and within size, counts 150/150, badge/footer/abstract/F-MAIL wording verified, 22 P1/P8 cards + 6 spot cards visually clean). The déjà omission is adjudicated a non-blocking imperfection with full reasoning in §2. The F-MAIL mailbox check remains open for the coordinator as a pre-insert action, not a proofread block.
