# Round 2 Independent Proofread Verdict — Lucerna Weekly W46, ES editions (es-de, es-ko)

- **Issue:** VOL.3, Mon 2026-11-09 – Sun 2026-11-15.
- **Scope:** TWO editions only — `2026-w46-es-de` and `2026-w46-es-ko`. The other 9 ES editions passed Round 1 and are out of scope.
- **Proofreader role:** Independent; did not build or fix these editions. No edition file was edited, re-rendered, pushed, or inserted. No weekly-git touch, no Discord post, no chat dump.
- **Gate work dir:** `hidden_files/w46/es-proofread-gates-round2/` (fresh; Round 1 dir not reused).
- **Basis:** Full SOP re-read; Round 1 verdict; fix record (FIX-REPORT.md + §8 of both WEEKLY-KIT.md files); shared toolkit (`tools/freeze.py`, `tools/p8.py`, `tools/occlusion_audit.py`, `tools/README.md` incl. #16 orphan standard, #21 gloss counting); full core `.text.md` (3,043 lines); full explanation-layer reads (DE 398 / KO 345 added strings); all 16 rendered cards viewed at full frame; all gates re-run independently on final artifacts (fix worker's gate JSONs NOT accepted).

## Per-edition verdicts

| Edition | Verdict | Reason |
|---|---|---|
| `2026-w46-es-de` | **FAIL** | One new blocking defect **D-6** (ungrammatical German, P2 ¿Y TÚ? box — same defect class as Round 1 D-1, missed in Round 1, present in the current artifacts). All five Round 1 fixes verified; keys 150/150; all gates clean; cards clean apart from D-6. |
| `2026-w46-es-ko` | **PASS** | All four Round 1 defects fixed and verified; keys 150/150; orphan scan 0 true splits; all gates clean; all 8 cards clean. Shippable as-is. |

## 1. Fix verification (Round 1 defects D-1–D-5)

| ID | Edition / page | Fix claim | Adjudication | Evidence |
|---|---|---|---|---|
| D-1 | DE P7 Q6 | `86,9 % der Spanier sorgen sich um die Wohnung. (Página 6)`; frozen quote + label unchanged | **CONFIRMED** | SVG element x=989 y=2133.25 (19.5pt) carries the fixed sentence; frozen quote `«La vivienda preocupa al 86,9 % de los españoles.»` present at x=989 y=2083.58 (21.5pt); defective string `Die Wohnung sorgt` = 0 elements in all DE SVGs and 0 occurrences in `t_de2.py`/`t_de.py`; visually confirmed on the DE P7 card. Grammatical `sich sorgen um` construction; matches DE P8 answer 127 wording. |
| D-2 | KO P1 cifras | `(11월 11일, 총파업 24시간이에요)`, `총파업` whole | **CONFIRMED** | Elements x=545 y=1426.9 `miércoles 11 de noviembre (11월 11일,` → y=1454.6 `총파업 24시간이에요)` (20.5pt). Date/strike/24h preserved. Source `t_ko.py` line 49. Visually confirmed on KO P1 card. |
| D-3 | KO P2 calendar | `(토요일에 세스타오에서 열리는 연방컵 결승)`, `세스타오` whole | **CONFIRMED** (incl. false-positive adjudication verified independently) | Elements x=545 y=887.5 `Federación en Sestao, 19:00 (토요일에` → y=916.1 `세스타오에서 열리는 연방컵 결승)` (21pt). Source string verified by grep in `t_ko.py` line 71: space between complete words `토요일에` and `세스타오에서` — a word-boundary wrap, NOT a mid-word split. Visually confirmed on KO P2 card. |
| D-4 | KO P4 bridge | `빈칸을 채우세요. 괄호 안 단어의 비교급이나 -ísimo 형태를 쓰세요.` | **CONFIRMED** | Elements x=527 y=2192.5 → y=2222.2 (20.5pt); `채우세요` whole on line 1. Semantics preserved. Source `t_ko.py` line 159. Visually confirmed on KO P4 card. |
| D-5 | KO P5 bridge | `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는 뜻을 나타내세요.` | **CONFIRMED** | Elements x=527 y=2363.5 → y=2393.2 (20.5pt); `나타내세요` whole on line 2. Source `t_ko2.py` line 37. Visually confirmed on KO P5 card. |

**Change-isolation check (regression sweep):** pre-fix freeze JSONs (`hidden_files/w46/es-fix/prefix/es-de-diff2.json`, `es-ko-diff.json`) compared against fresh Round 2 freeze JSONs. DE differs ONLY on P7 added_strings — exactly 1 string swapped (defective → fixed); all other pages identical. KO differs ONLY on P1/P2/P4/P5 added_strings — exactly the 4 fixed passages (rewrapped lines); all other pages identical. KO CJK-count deltas match the rewordings exactly (e.g. P1 `은` 6→5; P2 +`열리는`; P4/P5 +`쓰세요`/`이라는 뜻을`). No regression from the fixes at string level. Caveat, stated honestly: no pre-fix SVG hashes were stored anywhere, so isolation was proven by freeze multiset comparison, not by hash. The fixes introduced no defect on any page; D-6 (below) predates the fix — P2 was untouched by it (see §2).

## 2. New blocking defect (found in Round 2)

### D-6 — DE P2, ¿Y TÚ? box: ungrammatical transitive `sorgen` (BLOCKING)

- **Wrong text (rendered, joined across two SVG lines):** `Was machst du am Mittwoch, 11. November: streiken, arbeiten oder zu Hause bleiben? Was sorgt dich am meisten: Löhne, Wohnungen oder Preise? Schreib zwei Sätze auf Spanisch an die Redaktion.`
- **Evidence — file + element:** `files/weekly-report-w46-es-de/svg/p2-vida.svg`, elements x=1473 y=932.74 / 961.14 / 989.54 (`Hause bleiben? Was sorgt dich am`) / 1017.94 (`meisten: Löhne, Wohnungen oder Preise?`); visually confirmed on the DE P2 card. Source: `hidden_files/w46/t_de.py` line 68 (exact string, transform pair C12).
- **Why it is wrong:** German `sorgen` is intransitive/reflexive — it takes no accusative object. The correct constructions are `sich sorgen um` (as the fixed D-1 sentence and P8 answer 127 correctly use) or `für etwas sorgen`. `Was sorgt dich` puts the accusative pronoun `dich` as direct object of `sorgen`, exactly the construction Round 1 ruled ungrammatical in D-1 (`Die Wohnung sorgt 86,9 % der Spanier`). Transitive `sorgen` survives only as archaic usage and must not be taught to A2 learners.
- **Correct text (any one):** `Was beunruhigt dich am meisten: Löhne, Wohnungen oder Preise?` — or `Worüber machst du dir am meisten Sorgen: Löhne, Wohnungen oder Preise?` — or `Was bereitet dir am meisten Sorgen: Löhne, Wohnungen oder Preise?` (Fixer to choose; proofreader does not fix.)
- **Cross-edition check (DE is the outlier):** the same Spanish prompt `¿Qué te preocupa más?` is rendered EN `What worries you most`, FR `qui t'inquiète le plus`, IT `Cosa ti preoccupa di più`, PT `O que mais preocupa você`, RU `Что беспокоит вас больше всего`, JA `一番心配なのは何ですか`, KO `가장 걱정되는 건 뭐예요?` — all correct worry-verbs; only DE uses transitive `sorgen`.
- **History:** present since the original build; missed in Round 1 (Round 1 passed DE's explanation layer except D-1). Not a fix regression: the fix touched only DE P7, and the freeze-diff comparison shows P2 identical pre/post fix.
- **Disposition:** BLOCKING. DE cannot ship until D-6 is fixed; per SOP §8.4 the fix restarts a FULL proofread round for the DE edition.

**No other new defects found.** A full re-read of both explanation layers found no further ungrammatical German or Korean, no untranslated residue beyond frozen Spanish furniture, and no wrong-script residue. (Borderline non-defect noted and NOT raised: DE P8 answers 32/41 `Der veranillo sind ein paar … Tage` — definitional copula agreeing with the plural definiens; acceptable, consistent in both occurrences.)

## 3. Full key verification — 150/150 CONFIRMED (both editions)

Method: every key re-derived semantically from the core `.text.md` (all articles, stems, options, P8 answers) — matching blocks option-by-option, cloze/fill against grammar and article facts, choice keys against the articles, arithmetic recomputed from the issue's own data — then DE/KO P8 renderings extracted from the P8 SVG text layer and compared against the core RESPUESTAS sections. p8.py set-equality was NOT treated as sufficient.

**Result: 150/150 keys correct in the core and in both editions' P8 renderings.** Keys 1–136 and 139–150 byte-identical across core/DE/KO. Only differences: 137/138 re-aimed translations + 139/140 notes re-aimed + translated notes — all semantically correct (see below). The Round 1 fixes touched only a DE translation and KO explanation strings; no key moved. Round 1's 150/150 result still holds.

### Matching blocks (stem + options + key, quoted and verified option-by-option)

**Items 25–28 (P2, A2) — key: 25=c, 26=b, 27=a, 28=d**

| # | Stem | a | b | c | d | Key |
|---|---|---|---|---|---|---|
| 25 | la huelga | lo que se paga por trabajar | una organización de trabajadores | **un paro de todos los trabajadores** | lo que se paga por vivir en un piso | c |
| 26 | el sindicato | lo que se paga por trabajar | **una organización de trabajadores** | un paro de todos los trabajadores | lo que se paga por vivir en un piso | b |
| 27 | el salario | **lo que se paga por trabajar** | una organización de trabajadores | un paro de todos los trabajadores | lo que se paga por vivir en un piso | a |
| 28 | el alquiler | lo que se paga por trabajar | una organización de trabajadores | un paro de todos los trabajadores | **lo que se paga por vivir en un piso** | d |

**Items 52–55 (P4, B1) — key: 52=b, 53=c, 54=d, 55=a**

| # | Stem | a | b | c | d | Key |
|---|---|---|---|---|---|---|
| 52 | la fase de grupos | un partido sin puntos en juego | **la primera parte de un torneo, en grupos** | quien elige a los jugadores | los jugadores convocados | b |
| 53 | el seleccionador | un partido sin puntos en juego | la primera parte de un torneo, en grupos | **quien elige a los jugadores** | los jugadores convocados | c |
| 54 | la lista | un partido sin puntos en juego | la primera parte de un torneo, en grupos | quien elige a los jugadores | **los jugadores convocados** | d |
| 55 | el amistoso | **un partido sin puntos en juego** | la primera parte de un torneo, en grupos | quien elige a los jugadores | los jugadores convocados | a |

**Items 141–144 (P8, B2) — key: 141=c, 142=d, 143=b, 144=a**

| # | Stem | a | b | c | d | Key |
|---|---|---|---|---|---|---|
| 141 | el sondeo | quien organiza las elecciones | el error posible de un sondeo | **una encuesta de opinión** | las personas entrevistadas | c |
| 142 | la muestra | quien organiza las elecciones | el error posible de un sondeo | una encuesta de opinión | **las personas entrevistadas** | d |
| 143 | el margen de error | quien organiza las elecciones | **el error posible de un sondeo** | una encuesta de opinión | las personas entrevistadas | b |
| 144 | la junta electoral | **quien organiza las elecciones** | el error posible de un sondeo | una encuesta de opinión | las personas entrevistadas | a |

### Re-aimed P8 translations (137/138) and notes (139/140) — legitimate, semantically correct

- 137 — core `El miércoles hay huelga general en toda España.` → DE `Am Mittwoch gibt es in ganz Spanien einen Generalstreik.`; KO `수요일 스페인 전역에서 총파업이 있어요.` Both correct.
- 138 — core `El domingo vemos el España–Inglaterra.` → DE `Am Sonntag sehen wir Spanien–England.`; KO `일요일에 우리는 스페인–잉글랜드를 봐요.` Both correct.
- 139/140 — Spanish sentences byte-identical in all three; notes re-aimed correctly (DE `nach Hause` / `müssen`; KO `집으로 와요` / `반드시 ~`).
- 150 — ✓ model-text pointer in all three; model text = exactly 84 words by whitespace-split count (hyphenated `España–Inglaterra` / `Chequia–España` single tokens), re-counted independently from the `.text.md` paragraph.

### Arithmetic / numerical keys recomputed from issue data

- Q6 campaign duration: 13→27 Nov inclusive = 15 days (27−13+1). Key `15` correct.
- Q87: 95.4 − 91.4 = 4.0 points (key B). Correct.
- Q86: 6,019 interviews (3,532 is the study number — correctly discriminated). Correct.
- Chart values: 95.4 / 91.4 / 76.3 / 75.6 / 70.6 and 86.9 / 79.0 / 13.5 — match article text and measured bar widths (§5).

### Notable keys checked and confirmed

14 `uno`, 15 `noviembre`, 57 `muchísimos`, 58 `peor`, 59 `mejor`, 72 `envío`, 77 `Va a estrenarse «Infamia».`, 96 `Aunque` (indicative, factual concession), 103 `domingo`, 119 A (España–Inglaterra Sun 15; the derbi was Sun 8), 122 A (11 Nov), 132 B (adjudicated defensible in Round 1 — title概括 two people's Wednesdays, Madrid vs Barcelona; not re-litigated), 149 A `mudanza` (campaign does not start Wed 11, so B is incoherent). **No wrong key letter found anywhere.**

Freeze removed-string check: DE/KO P1–P5/P7/P8 removed sets = Chinese explanation/furniture only, no Spanish body text removed. DE P6 removed includes the known 16 Spanish exercise fragments (re-wrap/reflow, re-joined in added strings; identical pre/post fix). KO P6 removed = furniture/Chinese only. P8 answers 60–62/64/87 absent from both added and removed in both editions = byte-identical shared strings (language-neutral notes), not a gap; all 150 answers present per `.text.md` extraction and `p8.py`.

## 4. KO orphan scan — 0 TRUE SPLITS (binding README #16 standard)

Standard: window 10–45, line-initial orphan punctuation/particles AND mid-word splits with ≥3-syllable tails, for EVERY prose column. Three implementations agree: Round 1's script (re-run fresh), the fix worker's scan, and Round 2's own implementation (`ko_orphan_round2.py`, column clustering by x with gap ≤25px, S1 punctuation/particle + TAIL≥3 criteria).

- Own scan: 17 candidates = 9 TAIL≥3 (identical to Round 1 / fix-worker lists) + 8 S1-PUNCT hits that are all P8 separators `— 제 N 면 —` (standalone furniture blocks, not wrapped continuations — false positives of the broader S1 set). No S1-PARTICLE hits, no additional TAIL candidates.
- All 9 TAIL candidates adjudicated FALSE POSITIVES (word-boundary breaks, each verified from source/rendered nodes):
  1. P2 y=887.5→916.1 (D-3 site): `토요일에` | `세스타오에서…` — source space, complete words.
  2. P2 y=268.2→298.0: `el salario는` | `월급이에요` — particle boundary.
  3. P3 y=387.5→417.2: `el mendigo는` | `거지예요` — particle boundary.
  4. P3 y=1472.3→1500.7: `두` | `문장을…` — complete word.
  5. P4 y=843.1→871.5: `스페인 대` | `잉글랜드` — complete word.
  6. P5 y=885.8→915.5: `la papeleta는` | `투표용지예요` — particle boundary.
  7. P7 y=1191.2→1219.6: `일을` | `멈춰요.` — complete word.
  8. P8 y=2328.0→2343.7: `갈리시아가` | `아니에요` — complete word.
  9. P8 y=2403.0→2418.7: `panchón이` | `나와요` — particle boundary.
- Defect sites clean: D-2 (P1 cifras), D-4 (P4 bridge), D-5 (P5 bridge) produce NO candidates in any scan. D-3 produces only candidate #1 above.
- **Observation O-1 (NOT a defect, do not move the gate post-hoc):** a supplementary all-pairs scan found 1–2 syllable mid-word syllable-breaks (e.g. P1 `선거까|지`, `주|택`; P2 `월|요일`, `마지|막`, `스|페인`; P5 `스페|인`, `필|요한`; P7 `라|고`). These are BELOW the binding ≥3-syllable-tail threshold, inherent to the wrapper's syllable-level wrapping, and were not counted by Round 1 either. Recorded as a non-blocking observation only.
- DE added CJK 0 on every page (edition CJK total 0). KO added CJK 3,506 total, 318 distinct, ALL Hangul (U+AC00–U+D7A3); Hanzi 0 on every page; kana 0. Direct SVG scan: DE Hanzi 0, KO Hanzi 0.

## 5. Full re-gate on final artifacts (all re-run independently)

| Gate | DE | KO | Evidence file |
|---|---|---|---|
| Freeze (`tools/freeze.py diff` vs core) | exit 0, added CJK 0 | exit 0, added CJK 3,506 all Hangul, Hanzi 0 | `freeze-de.json`, `freeze-ko.json` |
| P8 (`tools/p8.py compare`) | CLEAN, 150 noted = 150, missing=[], extra=0, keydiff=[137,138] adjudicated | same | `p8-de.txt`, `p8-ko.txt`, extracts + line dumps |
| Occlusion (canonical `occlusion_audit.py`) | 0 flags | 0 flags | `occlusion-de.json`, `occlusion-ko.json`, `occlusion-core.json` (0 flags); selftest OK (all 6 planted classes fired exactly once, clean controls silent): `occlusion-selftest.txt` |
| Same-baseline scan (exact-y groups, true ink boxes, gaps <2px) | 0 reports (1,589 `<text>` parsed) | 0 reports (1,544 parsed) | `same-baseline-r2.txt`, `same_baseline_r2.py` |
| Counts | 150; standalone 138 + 3×4 grouped; per-page 10/18/18/18/18/18/12/38; no gaps/duplicates; A2 50 / B1 72 / B2 28 | identical | `level-pair-de.txt`, `level-pair-ko.txt` |
| P6 chart bars (SVG rects) | widths 305.28/292.48/244.16/241.92/225.92 and 278.08/252.8/43.2 = values ×3.2 exact; bars inside boxes | identical to core/DE | `chart-bars-r2.txt` |
| P7 golden sentences | 8/8 Spanish quotes verbatim in P7 + verbatim on source article pages; 8/8 translations with correct `(Página N)` tags (Q8 tag `(Página 1)` correct); DE Q6 fixed translation confirmed | 8/8 + 8/8 | `quotes-r2.txt` |
| Masthead pixel clearance (PIL, 1950×2700 P1 cards) | wordmark ink x=605..1344, clearance 540 L / 541 R; top-strip clusters clear of date (gap ≥38px); outer frame clean | identical | `masthead-gloss-abstract-r2.txt` |
| Badge + footer | Badge INSERTED y=574, 22pt bold, `#a4553a`, center x=975: `SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`; Spanish tagline retained y=372; one distinct pairing footer, page numbers correct (`Seite N von 8`) | Badge: `스페인어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`; footer `제 N 면 / 총 8 면` | SVG inspection |
| PDF + text layer | web 527,663 B (<7 MB), print 4,641,037 B; 8 pages; pdftotext 47,065 B web = print, byte-identical (`cmp`) | web 854,202 B (<7 MB), print 9,349,457 B; 8 pages; pdftotext 48,448 B web = print, byte-identical | `de-web.txt`, `de-print.txt`, `ko-web.txt`, `ko-print.txt` |
| Weekday/date claims | All verified with `TZ=Europe/Madrid date`: 9 Nov Mon, 10 Tue, 11 Wed, 12 Thu, 13 Fri, 14 Sat, 15 Sun, 19 Thu, 27 Fri, 28 Sat, 29 Sun, 6 Fri, 3 Tue, 8 Sun — all match issue claims; campaign 15 days inclusive consistent | same | — |
| ABSTRACT.txt | German, 279 B, single line + trailing newline, no ASCII `"`, practice-framed, real topics + masthead + VOL.3 + A2–B2 + 150 | Korean, 309 B, same formal checks | `masthead-gloss-abstract-r2.txt` |
| Reader-facing sweep (SVG text) | Forbidden internal terms (w46/W46, github, discord, SOP, proofread, audit, lint, freeze, occlusion, KIT, http, .md, slugs, frontmatter, insert.py, webpdf): 0 hits. Credits present (CC0, Wikimedia Commons, `Ilustración`, `Infamia`, `castaña`). | 0 hits; credits present | — |
| Glosses (README #21, split on `·`) | P2 5 / P3 5 / P4 5 / P5 4 items; Spanish headwords identical item-by-item to core; every headword occurs in its own page's article text (incl. `la papeleta` on P5) | P2 5 / P3 5 / P4 5 / P5 4; same headwords; M-1 separator deviation visible (veranillo/gaita boundary uses comma — all 5 terms present, adjudicated non-defect) | `gloss-r2.txt` |
| Kinsoku | N/A — ES-target Latin body; no Japanese text in either edition | N/A (KO equivalent = §4 orphan scan) | — |
| W45 promises | Teaser (Fri 13 campaign, Sun 29 vote, letters + best P8 texts), VOL.4 preview box, Ana example letter + disclosures present in both P7s; P6 timeline has no 12 Nov entry; P4 `EL DOMINGO 8` box states results unavailable — no invented scores | same | card review |
| Cards (all 8 + 8, full frame) | No overflow, overlap, missing glyphs/tofu, or missing credits, except D-6 text itself (content defect, not layout) | No overflow, overlap, tofu, or missing credits | card review (§6) |

**Correction to the Round 1 record (observation, NOT a defect):** Round 1 §8/§12 claimed "`12 de noviembre`: 0 occurrences in any edition (core included)". That string-level claim is REFUTED: the phrase occurs exactly once per edition (core, DE, KO identically) as distractor option B in frozen P8 item 122 (`San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre`), wrapped across two SVG elements, which is why line-based PDF/text greps miss it (confirmed in document-order SVG element join). The substance of the W45 promise HOLDS: item 122 asserts nothing about any decree/vote/committee; it is a wrong-date option for San Martín (key A, 11 Nov, correct). No decree-date claim exists anywhere: P6 timeline mentions decrees only for 2 OCT; P7 teaser has no 12 Nov. Frozen-core inheritance, semantically harmless. Do NOT fail either edition on it.

**Adjudications carried (do not re-raise):** M-1 KO gloss separator (non-defect); M-5 disclosure asymmetry ACCEPTABLE per coordinator ruling (DE/NL/RU letters-box notes omit the "no best P8 texts" fact, relying on the frozen Spanish disclosure directly above in the same box — DE confirmed in this form on the P7 card); M-7 frozen furniture (`De la redacción de La Lucerna · Nivel de lectura: A2/B1`, Spanish, 10×) not a defect. M-6 core-dir finding CONFIRMED by verification (core dir is a stale frozen-core reference: KIT self-identifies as core版, PDFs named `La-Lucerna-VOL3.pdf` without native suffix, ABSTRACT.txt retains the `通过西班牙新闻学西班牙语` wording — correctly left untouched; shippable Chinese edition exists separately as es-zh-cn). M-2/M-3/M-4 are KIT inaccuracies only (FR badge 19.5pt vs 20pt claim; DE KIT text-layer figure 47,074 B vs measured 47,065 B pre-fix — KIT not rewritten, record-only; ZH-CN wording). M-8 (EN ABSTRACT trailing newline) is another edition, out of scope.

## 6. Card review (all 16 viewed at full frame)

- **DE P1–P8:** clean layout throughout — no overflow, overlap, tofu, or missing credits. P7 fixed Q6 line renders cleanly on one line. P6 charts legible, labels clear of bars. P8 all 150 answers legible. The only content defect visible is D-6 on P2.
- **KO P1–P8:** clean layout throughout — no overflow, overlap, tofu, or missing credits. P1 cifras box shows `총파업` whole; P2 calendar shows `세스타오` whole; P4/P5 bridge lines whole; P3 gloss shows all 5 terms (comma boundary per M-1); P6 charts identical to DE/core; P7 letters box carries the full Korean disclosure; P8 separators and all answers legible. The P1 `선거까|지` wrap (O-1) is visible at full frame and reads acceptably under syllable-wrap convention; below the binding threshold.

## 7. Residual / new defect list (complete)

**Blocking:**
1. **D-6 (DE only)** — P2 ¿Y TÚ? box: `Was sorgt dich am meisten` — ungrammatical transitive `sorgen` + accusative. Evidence and correct text in §2. Must be fixed; fix restarts a full proofread round for DE per SOP §8.4.

**Non-blocking observations (do NOT gate shipment):**
- O-1 — sub-threshold (1–2 syllable) KO syllable-breaks, inherent to the wrapper; outside the binding ≥3-tail standard (§4).
- Round 1 "`12 de noviembre` 0 occurrences" string claim refuted at string level; promise substance holds (§5).
- KIT inaccuracies M-2/M-3/M-4 (record-only; KITs not rewritten).

**KO residual defects: none. DE residual defects apart from D-6: none.**

## Final verdict

**ROUND 2 FAIL — blocking defect D-6 (DE P2, `Was sorgt dich am meisten`). KO PASSES and is shippable as-is; DE is NOT shippable until D-6 is fixed and DE passes a fresh full proofread round per SOP §8.4.**

*Proofreader-only role honored: no fixes made, no edition files edited, no re-renders, no pushes, no inserts, no weekly-git touches, no Discord posts. Gate outputs saved under `hidden_files/w46/es-proofread-gates-round2/`.*
