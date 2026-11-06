# Round 2 Independent Proofread — Verdict: W46 IT (2026-11-09 – 2026-11-15)

- **Proofreader:** independent Round 2 subagent (did not build or fix these editions). No edition file was edited, re-rendered, pushed, or inserted. No subagents spawned. `~/workspace/weekly-git` untouched; `index.json` untouched; no Discord post; no edition content dumped into chat.
- **Date of verification:** Mon 2026-11-02 (evening EST), on the final shipped artifacts as rendered 2026-11-03 01:25–01:53 (SVG → card → PDF sequence verified by mtime; cards 1950×2700, 8 per edition, all present).
- **Scope:** all 11 IT-target editions — `2026-w46-it-zh-cn` (core, dir `weekly-report-w46-it-core`), `-de`, `-en`, `-es`, `-fr`, `-ja`, `-ko`, `-nl`, `-pt`, `-ru`, `-zh-tw`.
- **Basis of the defect list:** the Round 1 verdict file named in the assignment (`hidden_files/w46/it-proofread-gates/proofreader-verdict-round1.md`) **does not exist** — the Round 1 gate dir contains only gate JSONs/logs/diffs/svgtext, and `hidden_files/w46/it-fix/` contains no separate fix-worker report. The Round 1 defect list below was therefore reconstructed from the fix-record sections appended to all 11 editions' `WEEKLY-KIT.md` files plus `it-fix/apply_fixes.log` (137/137 applied). This limits traceability of Round 1's original wording; if the parent holds the verdict elsewhere, it should be filed alongside this verdict. No defect in this verdict depends on wording that could not be reconstructed from those two sources.

## Final verdict

**ROUND 2 PASS (all 11 shippable)**

Every Round 1 fix claim verified CONFIRMED on the final artifacts (see §2). Q1 resolved CONFIRMED (§3). The RU disclosure trade-off is ACCEPTABLE AS PRINTED (§4). All three shared gates pass on all 11 editions on re-gating by the proofreader (§6). No blocking residual defect was found. Two non-blocking observations (O1, O2, §5) are recorded for a future cycle; neither blocks shipment.

## 1. Per-edition verdicts

| Edition | Verdict | Basis (one line) |
|---|---|---|
| zh-cn (core) | PASS | D1/D2/D3/D5/Q1 CONFIRMED; gates clean; P1/P8 + P2/P4/P6/P7 viewed clean |
| de | PASS | All applicable fixes CONFIRMED; gates clean; P1/P8 viewed clean |
| en | PASS | Strapline/132/44/134 CONFIRMED; gates clean; P1/P8 viewed clean |
| es | PASS | 132/56/117 CONFIRMED; gates clean; P1/P8 viewed clean |
| fr | PASS | 132 CONFIRMED; gates clean; P1/P8 viewed clean |
| ja | PASS | No edition-specific Round 1 items; gates clean; P1/P8 viewed clean |
| ko | PASS | Katakana/full stops/146 CONFIRMED; gates clean; P1/P5/P8 viewed clean |
| nl | PASS | 20/146 CONFIRMED; P8 overflow fixed and verified; gates clean; P1/P8 viewed clean |
| pt | PASS | 132/disclosure CONFIRMED; gates clean; P1/P8 viewed clean |
| ru | PASS | Disclosure qualifier + 38 CONFIRMED; P7 geometry verified on pixels; gates clean; P1/P7/P8 viewed clean |
| zh-tw | PASS | Orphans/將來時/148 CONFIRMED; gates clean; P1/P8 viewed clean |

## 2. Fix-verification table (all defects × all editions)

Adjudication scale: CONFIRMED / PARTIAL / REFUTED. Every cell below was checked independently by the proofreader on the final SVG text layer (own script `verify_round2.py` → `verify-round2.log`, `verify-round2-text.txt`; context dump `dump_context.py` → `dump-context.log` in this dir). The fix worker's gate JSONs/logs were NOT accepted as evidence.

### 2a. Frozen-core defects (all 11 editions)

| Defect | Claim | Verdict | Evidence (all 11 editions) |
|---|---|---|---|
| D1 | P1 IN BREVE FESTIVAL cross-ref now `(Pagina 2)`; coverage is on p.2 | **CONFIRMED ×11** | P1 text layer contains `86 film a Firenze. (Pagina 2)` in every edition; `Pagina 2` count = 2, `Pagina 5` count = 0 in P1 of every edition. Other IN BREVE refs already correct (MANOVRA→Pagina 6, RICERCA→Pagina 4). P2 article confirms coverage: Festival dei Popoli, 67th ed., Oct 31–Nov 8, 86 films, Florence. |
| D2 | P4 ex. 56/57 stems negated (NON), keys unchanged (`più tardi` / `più presto`); P8 notes in every edition state BOTH matches at 20:45 + the negation, consistent with P4 article/fixture facts | **CONFIRMED ×11** | P4 `NON cominciano` count = 2 in every edition (stems 56 `Le partite di domenica NON cominciano ___ di quelle di giovedì. (tardi)`, 57 `Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)`). Keys unchanged: `p8.py` keydiff contains no 56/57 in any edition (only [137,138,139], §6). P8 notes 56/57 in every edition's native language state both matches at 20:45 (20.45 / 20:45 / fr `20 h 45` / ko `20시 45분` / ja `20時45分`) PLUS the negation, e.g. core `两场比赛都在 20.45 开始，周日的比赛并不比周四的晚`, en `Both matches kick off at 20:45: Sunday's match is not later than Thursday's`, nl (shortened) `Beide om 20.45 uur: zondag niet later dan donderdag`, ru `Оба матча начинаются в 20.45: воскресный матч не позже матча четверга`. 20:45 facts verified independently from the issue's own text: P1 (`Due notti azzurre, alle 20.45`; cifre `20.45 — l'ora delle due notti azzurre`), P4 article (`Giovedì 12 novembre, alle 20.45… Domenica 15 novembre, alle 20.45…`) + fixture table (both fixtures `ore 20.45`) + P1 week plan. Weekdays independently verified (TZ America/Toronto): Mon 2026-11-09, Wed 11, Thu 12, Fri 13, Sat 14, Sun 15, Sun 22, Sun 8 Nov — all match the issue. |
| D3 | P2 agreement corrected (`si è chiuso` / `si sono aperte`) | **CONFIRMED ×11** | P2 contains `si è chiuso il Forum Cultura` and `si sono aperte la finale del Panettone` in every edition; old forms `si sono chiusi` / `si sono aperti la finale` absent everywhere (full-text grep). Rendered on pixels in core P2 (viewed). |
| D5 | `=` present in core P8 146–148, ko 146, zh-tw 146/147, and worker extension zh-tw 148 | **CONFIRMED ×11** | Core P8: 146 `mandorle = 杏仁`, 147 `quanto costa? = 多少钱`, 148 `pagare con carta = 刷卡`. Ko 146 `mandorle = 아몬드`. Zh-tw 146/147/148 (same three, traditional forms). Item 146 `=` also verified in de/en/es/fr/ja/nl/pt (paren style)/ru. |

### 2b. Family defect F1 — full-width colon U+FF1A in P8 items 16–19 (8 editions + ko P6 header)

| Editions | Verdict | Evidence |
|---|---|---|
| de, en, es, fr, ko, nl, pt, ru | **CONFIRMED ×8** | U+FF1A total = 0 in all 8 editions across all 8 pages. Ko P6 header colon also fixed (0 occurrences). Core retains 32 and ja 41 and zh-tw 32 U+FF1A — native-script colon usage in Chinese/Japanese notes, outside F1 scope, not a defect. |

### 2c. Edition-specific items

| Edition / item | Claim | Verdict | Evidence |
|---|---|---|---|
| en strapline | Ungrammatical `THE ITALIAN ITALIANS ARE READING` replaced | **CONFIRMED** | P1 top strip: `THE ITALIAN THAT ITALIANS ARE READING` (viewed on pixels; centred, no collision). |
| en 132 | `two cities, two sweets` → `festivals` | **CONFIRMED** | P8 note 132: `The title sums up two cities, two festivals`. |
| en 44/134 | `+ date` added to `Subject + essere + place` pattern | **CONFIRMED** | `Subject + essere + place + date` count = 2 in joined P8 text (notes 44 and 134); DE equivalent count = 2 as control. |
| es 132 | `dos ciudades, dos fiestas` | **CONFIRMED** | P8 note 132: `El mejor título: dos ciudades, dos fiestas`. |
| es 56 | Standard `más tarde` continuation | **CONFIRMED** | P8 note 56: `el partido del domingo no es más tarde que el del jueves: più tardi`. |
| es 117 | `continúa en Cremona` | **CONFIRMED** | P8 note 117: `La Festa del Torrone continúa en Cremona`. |
| fr 132 | `deux villes, deux fêtes` | **CONFIRMED** | P8 note 132: `Le titre résume deux villes, deux fêtes`. |
| ko katakana (6 sites) | Katakana gone; correct `스크리토린치타` | **CONFIRMED** | Katakana characters = 0 in the full edition text; correct `스크리토린치타` count = 6; mixed-script bad form = 0. P8 note 120: `스크리토린치타는 쿠네오에서 열린다` (viewed on pixels, P8). |
| ko full stops (2 sites) | Ideographic full stops gone | **CONFIRMED** | U+3002 count = 0 in the full edition text. |
| ko 146 | `=` present | **CONFIRMED** | P8 note 146: `mandorle = 아몬드` (see D5). |
| nl 20 | Pronoun `(zij)` | **CONFIRMED** | P8 note 20: `dura (zij)` — `durare: l'estate → dura (zij)`. |
| nl 146 | `=` present | **CONFIRMED** | P8 note 146: `mandorle = amandelen`. |
| pt 132 | `duas cidades e duas festas` | **CONFIRMED** | P8 note 132: `O título resume duas cidades e duas festas`. |
| pt disclosure | tu-register `escreve à redação` on P7 | **CONFIRMED** | P7 SVG contains `escreve à redação`; `escrevam` count = 0 in P7. (PT P8 parenthesis style stays as Round 1 adjudicated — non-defect, not re-raised.) |
| ru disclosure | `by press time` qualifier | **CONFIRMED (as printed)** | See §4 — compact `Пока` wording verified in the current artifact; accepted as printed. The fuller wording in the fix worker's `verify_svgtext.log` (`К моменту сдачи номера`) is ABSENT from the current RU P7 SVG (see §5, process note N2) — the log is stale; this verdict rests on the artifact. |
| ru 38 | Plural marker `(мн. ч.)` removed from item 38 | **CONFIRMED** | P8 note 38: `mandorle — mandorle = миндаль`, no `(мн. ч.)` (viewed on pixels). Other true-plural `(мн. ч.)` markers in RU P8 untouched (verified in the added-RU P8 list: items 3, 13, 37, 62, 73, 74, 107 retain the marker). |
| zh-tw orphans | Orphan line-starts gone | **CONFIRMED** | Orphan line-start scan (set `、，。）】」』；：！？`) = 0 across all 8 pages. P1 cifre item 1 reflowed to one line (`11 — 11月11日週三，聖馬丁節`), confirmed on pixels. |
| zh-tw 將來時 | Consistent use; 未來時 0 occurrences | **CONFIRMED** | 未來時 raw = 0 / detagged = 0; 將來時 raw = 10 / detagged = 10 (KIT claim ×10: P5+P7 bridges + P8 76–79, 101–104 — count matches). The fix worker's `verify_svgtext.log` showing `FAIL ZHTW 將來時 x7` is a worker-script artifact, not a real defect (see §5, N2). |

### 2d. Regression sweep on changed pages

- **Changed-page accounting (sha256 vs `it-fix/before.sha256`, 88 SVGs):** exactly the KIT-claimed pages differ — P1/P2/P4/P7/P8 in the 9 non-ko/non-zh-tw editions; all 8 in ko; P1/P2/P4/P5/P7/P8 in zh-tw (P3/P6 byte-identical). 29 unchanged of 88. No unclaimed page moved. (Hash comparison only establishes which pages changed, not what changed; content verification is §§2a–2c + §6 + visual checks.)
- **NL P8 incident (first-pass overflow, fixed by shortening D2 notes):** final artifact verified — NL P8 max non-footer text y = 2548.9, identical to core; footer at y=2624; occlusion 0 flags; P8 viewed at full frame with all keys legible and a clear foot gap. Shortened notes still state the full facts (see D2 row).
- **RU P7 incident (first-pass LINEX overflow, fixed by compact disclosure):** final artifact verified geometrically + on pixels (§4).
- **No new defect introduced by any fix** was found in text-layer, gate, or visual checks (see §5 for the two non-blocking observations, both pre-existing frozen-layer items, neither introduced by the fix round).

## 3. Q1 verdict — CONFIRMED (the fix worker's resolution was correct)

**Q1:** P7 B2 sentence `la finale è a Perugia` — referent unclear; the fix worker resolved it as an ERROR and replaced it with `la Festa del Torrone è a Cremona`.

**Verdict: CONFIRMED.** The replacement is correct, and the original was indeed unsupported. Reasoning, each leg verified independently from the issue's own text:

- **(a) The original sentence is unsupported/erroneous.** `la finale è a Perugia` occurs 0× in all 11 editions as printed. A full `finale`/`Perugia` inventory of the issue's own text shows only three finale-related facts: (i) P2 Panettone finale — no location stated anywhere; (ii) P4 `quarti di finale` — Nations League quarter-finals, March 2027, no location; (iii) P7 B2 itself. Perugia appears in the issue only as Eurochocolate's opening city (`apre a Perugia`, `è aperta`, ex. 134 `Eurochocolate / è a Perugia / dal 13 novembre`). There is no finale in Perugia anywhere in the issue. The original sentence asserted a fact the issue never states, in the indicative, inside an exercise teaching exactly that facts take the indicative.
- **(b) The replacement is factually supported by the issue.** `la Festa del Torrone è a Cremona` appears in P7 of all 11 editions. It is supported by: P3 title `Due feste dolci: il torrone a Cremona, il cioccolato a Perugia`; P1 `a Cremona continua la [Festa del Torrone]` and exercise 6 `A Cremona continua la Festa del ___.`; P3 `Torrone è a Cremona, sabato 14 e…`. No referent was invented; the replacement restates a fact the issue states three times.
- **(c) The pedagogical point is preserved.** The P7 B2 column contrasts the subjunctive after `è probabile che / è possibile che / bisogna che` with the indicative after `so che / scrivono che`, using FACT examples. Context in all editions: `Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il sole torna, la Festa del Torrone è a Cremona. Opinioni sì, fatti con l'indicativo.` The replacement is a verifiable fact stated with the indicative — exactly the contrast being taught. The exercise's grammar point, level (B2), and answer key (P8 note 112: `so che + indicative: torna`) are unaffected.
- **Pixels:** the replacement sentence was viewed rendered in core P7 and RU P7 at full frame, legible, no overflow.

## 4. RU trade-off verdict — ACCEPTABLE AS PRINTED (not a residual defect)

**Question:** the RU P7 letters-box disclosure uses compact `Пока` ("as yet / so far") instead of the fuller `by press time` wording used (in explicit form) by the other 10 editions, because the fuller wording overflowed the fixed P7 geometry.

**Current RU P7 disclosure (3 lines, x=1473, verified on the SVG text layer and on pixels):**
`Пример от редакции, а не письмо. Пока писем и лучших сочинений нет; обещание — VOL.4. Пишите нам.`
("Editor's example, not a letter. As yet there are no letters or best essays; the promise [carries to] VOL.4. Write to us.")

**Verdict: ACCEPTABLE AS PRINTED.** Reasoning:

1. **Meaning preserved.** `Пока` is a temporal bound on the claim: it scopes "no letters or best essays [have arrived]" to the present moment. The disclosure's function — (i) the letter is an editorial example, not a real letter; (ii) no real letters/best P8 essays exist yet; (iii) the promise carries to VOL.4; (iv) write in — is fully carried in the three printed lines.
2. **A qualifier is present.** Unlike a bare categorical `писем нет`, `Пока` explicitly marks the claim as time-bounded — the same semantic work the other editions' press-time phrasings do, in the compact form Russian allows. No Russian reader is misled into thinking letters will never arrive; the very next clause (`обещание — VOL.4`) implies futurity.
3. **Geometry verified independently (not taken from the worker's numbers).** Last disclosure baseline y=1667.0; the FRASI gold rule line is y=1686 (the only `<line>` in y 1400–1900); ink bottom ≈1673, ≈13 px clear of the rule. (The KIT's "box bottom 14 px clear (1672 vs 1686)" is consistent within 1 px of measurement definition.) Occlusion audit: 0 flags (LINEX included). A 2× crop-zoom of the rendered card (`crop-ru-p7-letters.png` in this dir) shows the box bottom border clearly above the gold rule with a clean gap; all three disclosure lines are fully legible with no strike-through. Forcing the fuller wording would reintroduce the overflow the fix round already demonstrated; no layout change is required or justified.
4. **Comparison (other editions' explicit phrasings, all verified):** de `Bis Redaktionsschluss`, fr `reçus à la mise sous presse`, nl `Bij het ter perse gaan`, es `Al cierre no había…`, en `No real letters or best page-8 essays had arrived by press time`, ja `締め切り時に`, ko `마감 당시`, core/zh-tw `截稿时`. RU's form is the weakest/most compact of the eleven, but the difference is stylistic explicitness, not factual content. Recorded here so the difference is visible, not hidden: a future cycle may prefer the fuller `К моменту сдачи номера` if geometry allows, but that is a polish preference, not a Round 3 fix requirement.

## 5. Residual / new defects and observations

**Blocking defects: NONE.**

- **O1 — Line-end opening bracket `（` (non-blocking observation, pre-existing frozen-layer wrap).** In core P5 week-plan item 5, ja P5 week-plan item 5, zh-tw P5 week-plan item 5, and ja P1 cifre line 1, a line ends with the opening bracket `（`, with its content continuing on the next line. Evidence (SVG text geometry): line-END opening brackets found at those 4 sites; line-START closing punctuation = 0 in core/ja/zh-tw/ko (the issue's stated kinsoku gate, which counts line starts, passes). Disposition: NOT a ship-blocker. The bracket pairs correctly across the wrap, no meaning is lost, no line starts with stranded punctuation, and the pattern is pre-existing frozen text that Round 1's kinsoku scan did not flag. Strict kinsoku would prefer a reflow of these 4 boxes in a future cycle; inventing a retroactive gate for it in Round 2 would misstate the issue's own gate. Recorded transparently so the parent can overrule.
- **O2 — P6 chart bar left-edge stagger (non-blocking observation, pre-existing frozen geometry).** Measured fill-`#3e4c2a` bar x-starts in core P6: 172.9 / 176.8 / 188.4 / 164.0 / 171.9 px (spread ≤ ~24 px over 1950 px width). Bar widths are exactly 34 px/° (204/238/272/408/476 px for 6°/7°/8°/12°/14°, correct order; exercise arithmetic 14−12=2, 7+8=15 confirmed). On pixels the chart reads correctly with the invented-data disclaimer visible. Not a defect; no action.
- **N1 — Missing Round 1 verdict file (process note, not an edition defect).** See header. The defect list was reconstructed from KIT fix records + `apply_fixes.log`. Recommend filing the Round 1 verdict (if it exists elsewhere) with this verdict.
- **N2 — Fix-worker verification log is stale on two points (process note, not an edition defect).** `it-fix/verify_svgtext.log` (a) shows PASS for the RU disclosure checking `К моменту сдачи номера`, which was REVERTED and is absent from the current artifact; (b) shows `FAIL ZHTW 將來時 x7` / `FAILURES: 1`, while the independent count is 10, matching the KIT claim. Neither affects the artifacts; both were caught because this proofread re-verified from the artifacts, not the log. Recommend the fix worker's verify script not be reused unmodified.
- **Round 1 adjudicated non-defects re-checked and NOT re-raised:** ko no-P1-badge (pairing carried by footer, top strip, week-plan subtitle — verified), pt P8 parenthesis style, P4 list omissions (P4 list is a preview list, not an omission), sweep false positives. No new adjudicated non-defect was needed this round.
- **PT abstract phrasing** (`para aprender italiano a ler notícias…`) is slightly awkward but acceptable European Portuguese; not raised as a defect.

## 6. Gate outputs summary (proofreader's own re-gate, final artifacts)

All gate JSONs/logs saved in this dir (`freeze-*.json/.log`, `p8-*.json/.log`, `occlusion-*.json/.log`, `gates-all.log`, runner `run_gates.sh`). Tools: `tools/freeze.py` (canonical; the assignment named `freeze_check.py`, which does not exist — `tools/README.md` names `freeze.py`), `tools/p8.py`, `tools/occlusion_audit.py` (selftest OK on every run). Build `content*.py` modules were read/grepped as text only, never imported or executed (SOP import hazard); no freeze baseline was re-run.

- **Freeze (`freeze.py diff` vs frozen IT core):** added CJK characters 0 for all Latin-script editions; ja 3036, ko 3235, zh-tw 968 (native-script explanation layers — expected); core self-diff 0/0 on all pages. No level-tag churn except ja (one `A2` p.2 + one `B1` p.5 added/removed pair — frozen-head re-rendering, not drift).
- **P8 (`p8.py compare`):** all CLEAN — 150 noted = 150 noted, missing=[], extra_count=0, uncertain=[] in all 11 editions. keydiff=[137,138,139] for all 10 fan-outs, keydiff=[] for the core self-compare. **Adjudication of keydiff [137,138,139]:** pre-existing E-section translation re-aims (Italian stems re-aimed at the reader; recorded in KIT §6 of each edition; keys 137–139 verified per edition in the explanation-layer read). Expected and accepted — not a defect, not a fix regression.
- **Occlusion (`occlusion_audit.py`):** 0 flags on all 8 SVGs of all 11 editions (88 SVGs). Plus a proofreader same-baseline scan of the P1 top band (estimated ink widths): 0 overlap flags in all 11 editions.
- **Counts (re-measured):** 150 exercises total; per-page 10/18/18/18/18/18/12/38 confirmed via stem-number sets (P1 1–10, P2 11–28, P3 29–46, P4 47–64, P5 65–82, P6 83–100, P7 101–112, P8 113–150 via `p8.py`; P5 extras 1–5 are frozen week-plan day numbers, same in core; DE P1 extras 29/32 are cifre gloss fragments). Levels re-added from the registry source text (read-only grep of `ex()` calls + three `match_set` group registrations of 4 items each: A2 43+4=47, B1 66+4=70, B2 29+4=33) — **A2 47 / B1 70 / B2 33 CONFIRMED**.
- **P7 golden sentences:** all 8 occur exactly 2× in every edition (whitespace-normalized joined SVG text); per-page attribution checked in core — each occurs once on its article page (P1/P2/P3/P4/P5/P6) and once on P7, as verbatim contiguous excerpts.
- **P6 chart bars:** measured (core) — see O2. Values, order, disclaimer, and exercise arithmetic all correct.
- **PDFs:** all 11 web PDFs 8 pages, `pdftotext` 44,258–53,115 bytes (>0), file sizes 662,676–1,463,313 bytes (all <7 MB). Print PDFs (7–21 MB) are not subject to the web-PDF ≤7 MB limit. **Limit stated honestly:** print/web PDF text byte-identity was not re-verified by the proofreader (only web-PDF text presence/size/pages); the KITs' identity claim was not independently re-checked. `.text.md` exports present and substantive in all 11 editions (44–54k chars, `San Martino` present).
- **ABSTRACT.txt:** all 11 single-line, 0 ASCII double quotes, written in the reader's native language, naming masthead + real topics (San Martino, Nations League matches, Torrone/Cremona, Eurochocolate/Perugia, manovra 2027) + A2–B2 + 150 exercises.
- **Script residue:** Han/Hangul/Kana/Cyrillic counts exactly as expected (Latin editions 0/0/0/0; ja Han 1460 + Kana 1969; ko Hangul 3229, Han 0, Kana 0; ru Cyrillic 7421; core Han 2170; zh-tw Han 2312). Simplified-char suspects in zh-tw = 0; traditional-char suspects in core = 0.
- **Badge/footer:** pairing badge present in the P1 masthead area in 10 editions (y=574, or y=372 subtitle slot in es/ja/nl) plus native-language footer labels (y=2624) in all 11, verified on P1. KO has no P1 badge (family's built variant; pairing carried by footer/top strip/week-plan subtitle) — Round 1 adjudicated non-defect. Core has no badge (zh-cn masthead/footer carry the pairing) — same treatment.
- **Kinsoku:** line-start closing punctuation = 0 in core/ja/zh-tw/ko (all 8 pages each). Line-end `（` sites: see O1.
- **W45 promises honoured (per KITs, verified):** Festival dei Popoli date correction (67th ed., Oct 31–Nov 8, closed Sun 8 Nov) on P1/P2; Torrone promise (P1/P3); manovra "not yet law" disclosures (P1/P2/P4/P6 + P7 gloss); no real reader letters (editor's example + disclosure on P7 in all editions, promise carries to VOL.4); VOL.4 promises — Serie A MD11 results + classifica (P4 `risultati e la classifica li leggiamo nel prossimo numero` + P7 preview), Torrone closing Sun 22 Nov (P7 preview), real letters + best P8 writing (P7 preview).
- **Image credits:** P3 tartufo PD credit (`Foto: Wikimedia Commons — dominio pubblico`) and P5 chestnut CC0 credit (`Foto: Wikimedia Commons — CC0`) present in all 11 editions (frozen layer); ko P5 credit also confirmed on pixels.

## 7. Explanation-layer read coverage (honest record)

- **Read in full (every added string, all pages):** `added-en.txt`, `added-de.txt`. All clean: correct native grammar, correct facts/dates, no untranslated strings, no TODO/2025 residue.
- **Read in full (P7+P8):** `added-p78-latin.txt` (es/fr/nl/pt/ru, 1048 lines) and `added-p78-cjk.txt` (ja/ko/zh-tw, 573 lines). All clean.
- **Pattern + residue scan (P1–P6, es/fr/nl/pt/ru/ja/ko/zh-tw):** TODO/XXX/lorem/2025/TBD = 0; wrong-script residue = 0; `Pagina` refs only correct ones (incl. NL footer `Pagina N van 8`); digit inventory exactly the issue's numbers (11, 13, 20.45, 29, 32 + ordinals); the only repeated-word hit (es P2 `l'oca oca`) is the family's gloss format, as in de/en. Spot reads of cifre/bridge lines in all editions during the freeze-diff review. This is a scan basis, not a line-by-line read of those pages; the full-read pages above plus the gates and the visual checks are the basis for the PASS on those pages.
- **Native correctness spot findings:** none adverse. FR item 74 `marrons grillés` (Round 1-accepted) left alone. EN item 134 pattern and all P8 notes read in the full en read. All P7 bridges (future/subjunctive/indicative explanations) read in P7+P8 sets for all 11 editions.

## 8. Visual checks (rendered cards, no re-render by the proofreader)

- **P1 and P8, all 11 editions, full frame:** viewed. No overflow, overlap, missing glyphs/tofu, or missing credits. All fix sites visible where applicable (D1 ref, EN strapline, NL P8 foot, RU P8 item 38, ZH-TW P8 keys).
- **Changed-page spots:** core P2 (D3 on pixels), core P4 (D2 stems + fixture table + standings), core P7 (Q1 sentence + letters disclosure), RU P7 (disclosure + FRASI clearance, full frame + 2× crop-zoom), core P6 chart (crop-zoom, O2), core P5 plan box (crop), ko P5 (photo credit + plan box), zh-tw P1 cifre reflow.
- **Cards freshness:** SVG → card (+0–1 min) → PDF (+~15 min) mtime sequence verified per edition; cards render the final SVGs.

## 9. Artifacts in this directory

`run_gates.sh`, `gates-all.log`, `freeze-{de,en,es,fr,ja,ko,nl,pt,ru,zh-cn,zh-tw}.json/.log`, `p8-*.json/.log`, `occlusion-*.json/.log`, `verify_round2.py`, `verify-round2.log`, `verify-round2-text.txt`, `dump_context.py`, `dump-context.log`, `added-{de,en,es,fr,ja,ko,nl,pt,ru,zh-tw}.txt`, `added-p78-latin.txt`, `added-p78-cjk.txt`, `crop-ru-p7-letters.png`, `crop-core-p5-plan.png`, `crop-core-p6-chart{,2,3}.png`, and this verdict file. (`freeze-added-review.txt` contains only a traceback from an early exploratory command — disregard it.)

**ROUND 2 PASS (all 11 shippable)**
