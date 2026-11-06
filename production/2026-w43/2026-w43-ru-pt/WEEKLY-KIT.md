# WEEKLY-KIT — The Lucerna Weekly VOL.1 · RU × PT (Russian text, Portuguese explanations)

Edition: Russian target text (frozen VOL.1 core, files/weekly-report-ru-vol1/) with the
complete explanation layer rewritten in Brazilian Portuguese for Portuguese-speaking
readers. Build code: hidden_files/weekly-report-ru-pt-build/ (copied from the core build).
Russian text, images, page geometry: frozen. Pages: 8 (1950×2700), multiple-of-4 rule kept.

## 1. Baseline fidelity proof (fan-out method step 1)

The core build directory was copied to hidden_files/weekly-report-ru-pt-build/; before any
edit, output paths were repointed to a build-local baseline-out/ and the unmodified code was
run. All 8 regenerated SVGs are byte-identical to the shipped core SVGs (sha256):

| page | sha256 (baseline reproduction = shipped core) |
|---|---|
| p1-pervaya | c808a77d5696156dfc5b75bbb12abc3a9e5f47a83a553e3910869888be8fc865 |
| p2-zhizn | e6040d06337bec9549cdebb989c4142451cd1cba1de17092d161467271addc0a |
| p3-kultura | 21f0a9d716fac63c36065bfd1f10c932dddd2b36b5f2ccb7131c5c5dbcb60d0a |
| p4-sport | 4d6fab86c99d34fe15337c0ae5b547e65aa5ea1b6b94f0dcab3afad5eccec604 |
| p5-molodezh | 534284d6ccf7e401b6d470e67f5ba1ef2fcbbfaea0dd45e36b5224d1a468e498 |
| p6-razbor | 48e6b85a7fb234d790a38f4d1f6644bc780ef8c1f536401f06dec369329a8199 |
| p7-yazyk | 8f9e861823f946bafdd2f6e4e3b74bfa52f6e3d25f09779813d1dfff017f4311 |
| p8-test | fa3f80efe79f72efc7544ac990ec229df1f10f5cd40a4c4dc57b4fa62dfaf39f |

Registry from the unmodified run: 150 exercises (A2 54 · B1 72 · B2 24; per page
10/18/18/18/18/18/12/38; writing model 82 words) — identical to the core KIT.
After all work, the core's shipped SVG hashes were re-verified: 8/8 unchanged (see §11).

## 2. Totals (this edition, from the final build log)

- Exercises: **150** — A2 54 · B1 72 · B2 24 (identical to core).
- Per page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38 (identical to core).
- By type (Portuguese type names): Completar frases 54 · Escolha múltipla 42 ·
  Associação de palavras 20 · Construção de frases 12 · Transformação de frases 4 ·
  Cloze 13 · Tradução 4 · Escrita 1.
- Writing model (#150): 82 words (registry-counted), frozen Russian, unchanged.
- Registry meta diff vs core (page, level per item): zero mismatches.

## 3. Key-diff registry (complete — derived by dumping both registries and diffing)

Keys differ from the core in exactly **3** items; stems re-aimed in exactly **2**;
all other 145 keys and 148 stems are byte-identical to the core (machine-verified).

| # | kind | core | this edition (PT) |
|---|---|---|---|
| 137 | key | 星期日中央陆军将对阵斯巴达克。 | No domingo, o CSKA joga contra o Spartak. (note: Ver a página 4; instr: Traduza para o português) |
| 138 | key | 预报员预报十月末有雨夹雪。 | Os meteorologistas prometem neve com chuva para o fim de outubro. (note keeps «мокрый снег = neve com chuva»; instr: Traduza para o português) |
| 139 | stem | 假期从星期六开始：一共十二天。→ ___ | As férias começam no sábado: doze dias no total. → ___ (key unchanged Russian «В субботу начинаются каникулы — всего двенадцать дней.»; note: atenção ao caso: двенадцать дней; instr: Traduza para o russo) |
| 140 | stem | 祝爸爸父亲节快乐！→ ___ | Desejo ao papai um feliz Dia dos Pais! → ___ (key unchanged «Поздравляю папу с Днём отца!»; note: поздравляю + с + instrumental; instr: Traduza para o russo) |
| 150 | key (writing apparatus) | （开放题，范文如下） | (pergunta aberta — texto modelo abaixo) (note: O texto modelo está na seção H desta página (82 palavras); instr: Escreva; type: Escrita) |

Notes rewritten in Portuguese: **142 of 150**. The 8 notes byte-identical to the core are
pure-Russian form notes, language-independent, kept as printed by the core (same set as the
RU×IT sibling edition): #17/#104 «выпасть → выпадет», #35 «учиться → учился»,
#36 «написать → написал», #63 «закончиться → закончился», #73 «День бабушек и дедушек»,
#90 «слушать → слушают», #110 «обещать → обещают».

Renderer note (inherited core behaviour, identical in the RU×IT sibling): inside P8
answer-key lines the typesetter drops «» pairs that directly wrap a single cited word inside
a note (e.g. a note drafted as «с» + instrumental prints as «с + instrumental» — compare the
core's own #106 line, which prints «с + 工具格» the same way). Meaning is unaffected; the
standalone «» pairs elsewhere (article text, stems, phrases) render normally (31 pairs on P8).

## 4. Printed-note set verification

The core prints notes for all 150 items on P8 (programme audit). Method: extracted the
answer-key region lines (13.0 px) from both shipped P8 SVGs; number sets are EQUAL
{1..150} = {1..150}; every PT key line carries its note (two notes, #97 and #138, wrap onto a
continuation line — the continuation text was located in the SVG, e.g. #97's
«ligue com и длятся» and #138's «outubro. — мокрый снег = neve com chuva»).
**Printed-note set: EQUAL to the core, 150 = 150.**

## 5. Portuguese furniture (verbatim as shipped)

- Masthead: «Lucerna» (no article), exactly as the core.
- P1 badge (strap slot, 20 px bold brick, centered): «TEXTOS EM RUSSO · EXPLICAÇÕES EM
  PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA»
- P1 strap (y=330): «SEMANÁRIO RUSSO · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ»
- Top strip centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TODA SEMANA · O RUSSO QUE A RÚSSIA LÊ»
- Headline band right: «A PRIMEIRA NEVE — ESTA SEMANA» / «As previsões divergem · ver página 2»
- Footer left (all pages): «Lucerna · SEMANÁRIO RUSSO VOL.1 · TEXTOS EM RUSSO ·
  EXPLICAÇÕES EM PORTUGUÊS»; footer right: «Página N de 8»
- Gloss prefix: «Nota — » (library gloss() adds it; the P1 headline expl carries it in-string,
  as in the core).
- Section suffix pattern (follows the shipped PT column): «· Em números», «· Sumário»,
  «· A palavra», «· Em resumo», «· Quiz-relâmpago», «· Na mídia», «· Tema principal»,
  «· Agora é com você»; page bands: Vida / Cultura / Esporte / Juventude / Análise / Língua.
- Exercise instruction words: Complete · Forme a frase · Reescreva · Associe ·
  Traduza para o português · Traduza para o russo · Escreva.
- Number localization: decimal comma («12,5» style), thousands dot, ordinals 1.º/3.ª/12.ª.
- Answer-key format: the RU core's own dash format «N. key — note» is KEPT (no parenthesis
  style); the Russian page separators «— СТРАНИЦА n —» are kept, as in the core and RU×IT.

### Deviations from the full-form strings (wording only, measured; geometry untouched)

1. P1 word-of-week gloss: full candidate «похолодает = vai esfriar, a temperatura vai cair.»
   measured 351.1 px against its 288.7 px slot; the core's gloss ends at slot x=1761.7 and
   the right column starts at x=1451 anyway, so the shipped short form is
   «похолодает = vai esfriar.» (mirrors the core's own one-line short gloss).
2. P1 contents/numbers suffixes shortened pre-emptively to the core's measured slots:
   «НЕДЕЛЯ В ЦИФРАХ · Em números» (192.4 px vs core 287.5) and «В ЭТОМ НОМЕРЕ · Sumário»
   (234.5 px vs core 267.3) — no overflow risk, no visual difference in layout.
3. P1 media-box source line: «Segundo a mídia russa, 15–20 de outubro de 2026» measured
   ink 438.0 px (19 px sans) against the 412 px available inside the sidebar box (border
   x=1885) — flagged by the geometric audit (§7) and shortened to
   «Segundo a mídia russa, 15–20 out. 2026» (348.4 px).
4. P7 clinic notes (each must stay on ONE line at 19.5 px in 390 px, or the col-3 stack
   overruns the phrases rule at y=1698 — the RU×IT failure mode): «Com 2, 3, 4 → очка;
   com 5 ou mais → очков.» (2 lines) → «2, 3, 4 → очка; 5+ → очков.» (1 line);
   «Genitivo depois de «с» (início): с первого октября.» (2 lines) →
   «Genitivo após «с»: с первого октября.» (1 line).
5. P7 letters-box closing line: 3 lines → «Exemplo da redação. No VOL.2, cartas
   verdadeiras e os melhores textos!» (2 lines). After fixes 4+5 the P7 col-3 stack ends at
   y=1682.96 — exactly the core's own end position (was 1765.0 before the fixes, i.e. past
   the phrases rule at 1698 and the phrases heading baseline at 1736).

## 6. Freeze check (visible-text diff vs core)

Per-page text-multiset diff (core → PT): every removed string is a Chinese explanation
string of the core; every added string is Portuguese explanation layer, pairing furniture,
or the documented registry items of §3. Zero Russian target-text changes outside §3.
Embedded image payloads are byte-identical on every page (P1 ×1, P2 ×1, P3 ×2, P4 ×1,
P5 ×1, P6 ×1, P7/P8 ×0).
P7 phrases: each of the 8 Russian phrases occurs with the same whole-issue count as in the
core (7 phrases ×1 in their article + the Pushkin line ×2 by design — the P3 article quotes
it AND P7 repeats it, identical in both editions); P7 translations are Portuguese;
page tags (Страница 1/2/2/3/4/5/3/6) unchanged and correct.
P6 flow note: the PT explanation line for section A wraps to 2 lines (core: 1), shifting the
exercise columns by one item each; the deepest drawn ink on P6 is baseline 2557.2 — the same
depth as the core's own deepest P6 item — and stays 17 units clear of the footer rule (2580).
Verified in the render and by the audit (§7): no footer-band intrusion.
Zero CJK characters and zero full-width parentheses in the final SVGs.

## 7. Geometric occlusion audit (mandatory gate)

Own implementation of the house method (scratch/audit.py): SVG parsed in paint order;
glyph boxes measured with PIL against the production fonts (Noto Sans/Serif CJK Regular +
Bold TTC, SC face index 2, bold elements included); vertical ink box = baseline −0.88em …
+0.30em (conservative upper bound); line boxes expanded by half the stroke width.
Classes: (a) ≥30% glyph-box coverage by a later opaque shape; (b) footer-band intrusion
(footer rule y=2580); (c) page-edge spill; (d) line-through-ink crossings; (e) text-vs-text
ink overlap; (f) text ink crossing the right border of its containing rect.

Positive control: a synthetic SVG with one covered text, one line-crossed text, one
footer-band text and one edge-spill text — all four classes fired. The control also caught
an over-broad furniture exclusion in the first version of class (b) (it would have exempted
any ≤20.5 px text below the rule); the exclusion was tightened to the exact furniture
signature (baseline 2624, size 20) and the control re-passed before the real run.

Results — this edition: **3 flags**; frozen core (same script): **2 flags**.
1. BORDER-R, P1 (NEW, PT-only): the media-box source line ink ended at x=1911, past the
   sidebar border 1885. REAL defect → fixed by wording (§5.3); re-audit clean.
2. TEXT-TEXT, P1 masthead: title «Lucerna» glyph box vs the strap line box (conservative
   boxes overlap in the band y 294.8–312.4). IDENTICAL flag on the core (same coordinates,
   frozen furniture). Pixel/visual adjudication: rendered card shows a clear gap between
   the title ink and the strap; the overlap is the +0.30em descender allowance of the 92 px
   blackletter title («Lucerna» has no descenders). NON-DEFECT, inherited.
3. LINE, P2: the rule at y=1803–1805 grazes the conservative glyph box of the frozen
   Russian grammar line «Запомните пару: …» (baseline 1795). IDENTICAL flag on the core —
   both the text and the rule are frozen core elements at identical coordinates; the
   rendered cards of both editions are visually identical here (the rule sits under the
   line's descenders as the core's shipped design). INHERITED, non-defect.
Final state: **0 unresolved NEW flags vs the core** (PT flag set = core flag set).

## 8. Builder's proofread (full pass, this build)

All 8 pages read end-to-end from the rendered cards. All 150 keys re-derived from the
Russian text: 145 keys are byte-identical to the independently proofread core (registry
diff, §3), the 5 documented items verified against their articles (derby preview Sun
Oct 25 16:00 — #137 key is the Portuguese translation of the P4 fixture; #138 forecast
«мокрый снег» end of October; #139/#140 keys answer their Portuguese stems; #150 model
82 words). Weekday/date claims in the Portuguese layer verified against the real 2026
calendar: 24 Oct = Saturday, 25 Oct = Sunday, 31 Oct = Saturday, 22 Oct = Thursday,
round 12 opens Friday 23 Oct, last school day Friday 23 Oct — all correct. Standings
arithmetic (Dynamo 25 / Zenit 24 / Spartak 23; «24 очков» occurs exactly once, in the P7
clinic's deliberate wrong example — frozen), chart 34+28+22+16 = 100, 12 days
Oct 24 – Nov 4 — all as the core. Portuguese layer complete on all 8 pages; no Chinese
remnants (0 CJK in SVGs).

## 9. Images (credits from the core KIT §5; license record in the core build's assets/CREDITS.md)

All credits are printed on-page in Russian, frozen from the core; placement of every
credited image verified in this edition's render (payloads byte-identical, §6):
P1 K. Yuon, «Зима. Ростов» (public domain) · P2 W. A. Bentley snowflake micrograph no. 777
(public domain) · P3 O. Kiprensky, Pushkin portrait 1827 (public domain) · P3 I. Bilibin,
«Морозко» illustration 1932 (public domain) · P4 Russia 1912 Olympic football squad
(public domain) · P5 USDA pumpkin photo, Brendan Hoffman for USDA 2016 (public domain) ·
P6 autumn path photo by Toxer427 (CC0).

## 10. Deliverables and PDF pins

- files/weekly-report-ru-pt/svg/ ×8, cards/ ×8 (1950×2700 PNG)
- Print PDF: Lucerna-VOL1-PT.pdf — 22,611,692 bytes —
  sha256 9cfc4973c7c6404b874a62eb6b0efc672d4e703dd8feb63f96667e57f0d2e8db
- Web PDF: Lucerna-VOL1-PT-web.pdf — 3,653,545 bytes (< 10 MB) —
  sha256 1a459019f27d9972caf013f5c9d72882bac1c79d5002aee11407ae63c7ad21e8

## 11. Core untouched

Core shipped SVG sha256 re-verified after all work: 8/8 identical to the table in §1.
The core build directory was never executed in place and never edited; all work happened
in the copied build dir.

## 12. Hygiene disclosures

- The explanation-layer helper keeps the core's method name in operative code under the
  neutral name expl() (1 definition + 20 call sites renamed). The intermediary-layer term
  (either language form) occurs 0 times in the paper, this KIT, and the operative build
  code (grep-verified). The one-off transform script in the build dir's scratch/ subdir
  necessarily quotes the core's original call strings as search patterns for the rename;
  it is not operative code and is confined to scratch/.
- Build scratch (logs, registry dumps, audit script, freeze/audit outputs) lives in the
  build dir's scratch/ subdir, not /tmp.

## 13. Independent proofread — PASS (zero problems)

Independent proofreader, fresh pass on the final rendered artifacts (2026-10-21).
No changes to the paper were needed; the only correction made in this pass is a
KIT documentation fix (§3, disclosed at the end). Scratch:
hidden_files/proof-rupt-2026/ (registry dumps, audit script + flags, copies).

**Baseline & integrity.** My own copy of the unmodified core build reproduced
all 8 shipped core SVGs byte-identically; my copy of this build reproduced all
8 shipped edition SVGs byte-identically. The core's shipped SVG sha256 were
re-verified at the END of the pass and are UNCHANGED (p1 c808a77d…, p2
e6040d06…, p3 21f0a9d7…, p4 4d6fab86…, p5 534284d6…, p6 48e6b85a…, p7
8f9e8618…, p8 fa3f80ef… — identical to the §1 table and to my start values).

**Freeze diff (per-page text multiset, mine).** Every removed string is a core
Chinese explanation string, except three classified items: the P1 strap and
the P1 y=372 reader-tagline slot (both pairing furniture, §5) and the P8
standalone element «Пушкина» (a wrap fragment of #46's note; the full note
text «стихи Пушкина» is present complete in this edition at a different wrap
point). Zero undocumented Russian-text changes. Embedded image payloads are
byte-identical to the core on every page (counts 1/1/2/1/1/1/0/0). **CJK
characters in the final SVGs: 0. Full-width parentheses: 0.**

**Keys — independently re-derived, all 150.** I dumped both registries
myself: page and level metadata have ZERO mismatches; the key diff is EXACTLY
{137, 138, 150} with the §3 strings («No domingo, o CSKA joga contra o
Spartak.» / «Os meteorologistas prometem neve com chuva para o fim de
outubro.» / «(pergunta aberta — texto modelo abaixo)»); stems re-aimed are
EXACTLY {139, 140} and their Russian keys are byte-identical to the core's
(«В субботу начинаются каникулы — всего двенадцать дней.» / «Поздравляю папу
с Днём отца!»); all other 145 keys and 148 stems are byte-identical. I then
read all 8 rendered pages end to end and re-derived every key from the
Russian text: all 150 confirmed (standings «Динамо» 25 / «Зенит» 24 /
«Спартак» 23 consistent across article, table box and keys; chart
34+28+22+16 = 100 with proportional bars; 12 days = Sat 24 Oct – Wed 4 Nov
inclusive; «24 очков» occurs exactly once in the whole edition — the P7
clinic's deliberate wrong example, as frozen). Notes: 142 rewritten in
Portuguese; the 8 unchanged ones are exactly {#17, #35, #36, #63, #73, #90,
#104, #110} and each is a genuine pure-Russian form note in the core's own
apparatus style (verb-form arrows «выпасть → выпадет», «учиться → учился»,
«написать → написал», «закончиться → закончился», «слушать → слушают»,
«обещать → обещают», and #73's holiday-name citation «День бабушек и
дедушек») — no Portuguese residue, no missed translations.

**Printed-note set equality (extracted by me from both shipped P8 SVGs).**
Core set = {1..150}; edition set = {1..150}; EQUAL. Dash style
«N. key — note» and the «— СТРАНИЦА n —» separators are kept. Beyond the
sets, I compared every printed entry's full text (column-reconstructed)
against its own registry: 150/150 exact in this edition; in the core, 149/150
(the core's #80 prints «时 间» with a wrap space — a pre-existing core
artefact, not this edition's). Wrapped-note continuations verified present
and complete (#97, #138, #140). The typesetter's dropped-«» behaviour inside
P8 notes is IDENTICAL in both editions (31 printed « in this edition vs 13
in the core because the Portuguese notes cite more words; e.g. #106's note is
already in the dropped form in BOTH registries; multi-word title citations
keep «») — no Portuguese-only loss.

**Totals.** 150 exercises (A2 54 · B1 72 · B2 24); per page 10/18/18/18/18/
18/12/38; numbering continuous 1–150; writing model 82 words (frozen,
identical). P7 phrases: all 8 Russian phrases byte-identical to the core
with identical page tags (Страница 1/3/2/4/2/5/3/6); whole-issue occurrence
counts EQUAL TO THE CORE for every phrase (article ×1 + P7 ×1), each
verbatim-contiguous on its tagged page (whitespace-stripped search).

**Calendar.** Every weekday/date claim in the Portuguese layer checked
against the real 2026 calendar (Europe/Moscow): Oct 22 Thu, Oct 23 Fri
(round 12 opens, last school day), Oct 24 Sat (holidays begin), Oct 25 Sun
(derby), Oct 28 Wed (Grandparents' Day), Oct 31 Sat (Halloween) — all
correct. The P6 day strip (24 сб … 4 ср) is fully correct, and Father's Day
«18 de outubro» falls on a Sunday as printed.

**Geometric occlusion audit — MY OWN implementation** (paint-order parse;
PIL real-font INK extents including bold; line boxes expanded by half the
stroke width; synthetic positive control run BEFORE the real pass: all five
planted classes — COVER, LINEX, TEXTX, EDGE, TITLEX — fired, and both clean
control texts stayed silent). Results: the EDITION has 4 flags, the CORE has
7 under the same audit; every edition flag is inherited-identical or a
model artefact cleared on pixels:
- P2 LINEX (both editions, identical): the section rule sits at rows
  1803–1804; the frozen grammar line's ink ends at row 1801 — 2 clear rows,
  no contact. Non-defect.
- P1 TITLEX (both, identical): «странице.» ink ends at pixel row 2300 vs
  its box's bottom edge 2304 — 4 clear rows. Non-defect.
- P7 TITLEX (both, identical): VOL.2 teaser ink stays inside its dark band
  (band bottom row 2521; no text ink below it). Non-defect.
- P2 TITLEX (edition only): the closing line «envie à redação.» — model ink
  bottom 1497.07 vs box bottom 1496.75 (0.32 units, driven by the ç
  cedilla); PIXELS: ink ends at row 1491, ≥5 clear rows above the border.
  Non-defect.
The CORE additionally shows 4 TEXTX hairlines in its own P8 (ink-box
overlaps of 0.06 units between adjacent flow lines — sub-raster artefacts
of the frozen core; this edition's P8 has none). No COVER, EDGE or FOOTER
flags in the edition. The builder's conservative advance-box masthead flag
does not reproduce under ink measurement (no ink overlap) — consistent
with their adjudication.
**Pixel verification of the builder's claimed fixes:** ① P1 media-box
source line «Segundo a mídia russa, 15–20 out. 2026»: pixel ink ends at
x=1825 (model 1833.5), ≥51 units inside the sidebar border at 1885 — the
abbreviation fix is real (the core's own Russian line ends at 1851, also
inside). ② P7 col-3 stack: bottom = 1682.96, EXACTLY the core's value,
with the phrases rule at y=1698 — 15 units clear. ③ P6 cascade: deepest
ink row 2561 in BOTH editions (builder's baseline 2557.2), ~30 units above
the footer zone — non-defect, same depth as the core.

**Furniture.** Badge, footers («Lucerna · SEMANÁRIO RUSSO VOL.1 · TEXTOS EM
RUSSO · EXPLICAÇÕES EM PORTUGUÊS» / «Página N de 8»), gloss prefix «Nota —
» and the article-free masthead «Lucerna» all match the KIT prescription
and the shipped PT-column patterns in the EN×PT/FR×PT KITs; the documented
deviations (short word-of-week gloss, abbreviated media source line, P7
clinic one-liners, two-line letters-box closing) are all present as
documented. Portuguese is genuine Brazilian Portuguese throughout
(«borracharia», «dérbi», «fantasias», «1.º de outubro», «12.ª rodada»).

**Credits.** Every printed credit matches a placed image and the core KIT
record: P1 Yuon (PD), P2 Bentley snowflake (PD), P3 Kiprensky portrait +
Bilibin «Морозко» (PD), P4 1912 squad photo (PD), P5 USDA pumpkin photo
(PD), P6 Toxer427 (CC0).

**Banned-term scan.** The intermediary-layer term: 0 occurrences (both
script forms) in the paper, this KIT, and the operative build code — the
explanation method is renamed `expl()` (1 definition, call sites in the
build library); the one-off transform script quoting the core's original
call strings sits in the build dir's scratch/ subdir only (the §12
disclosure; adjudicated hygiene note, not an edition defect).

**KIT documentation correction (this pass, KIT-only).** §3's row for #139
quoted the key as «Каникулы начинаются в субботу, 24 октября, и длятся
двенадцать дней.» — that string is not the key in either edition (it
resembles #97's key). The actual registry and printed key in BOTH editions
is «В субботу начинаются каникулы — всего двенадцать дней.». The §3 quote
has been corrected; the PAPER was always correct and is untouched.

**Final pins (measured by me).** Web PDF: 3,653,545 bytes, sha256
1a459019f27d9972caf013f5c9d72882bac1c79d5002aee11407ae63c7ad21e8 (< 10 MB
Print PDF: 22,611,692 bytes,
sha256 9cfc4973c7c6404b874a62eb6b0efc672d4e703dd8feb63f96667e57f0d2e8db.
Both confirm the builder's pins exactly.

**Verdict: PASS — one complete independent pass, ZERO problems. Ready for
repo insert.**
