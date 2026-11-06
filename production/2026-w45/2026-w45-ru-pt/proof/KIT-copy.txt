# WEEKLY-KIT — The Lucerna Weekly VOL.2 · RU × PT (Russian text, Portuguese explanations)

Edition: Russian target text (frozen W45 core, files/weekly-report-w45-ru-core/)
with the complete explanation layer rewritten in Brazilian Portuguese for
Portuguese-speaking readers. Issue week: Monday 2 November – Sunday 8
November 2026. Build code: hidden_files/weekly-report-w45-ru-pt-build/
(copied from the core build, repointed, transformed by the assertive
scratch/transform.py — every replacement asserts its hit count; whole
lines or exact unique literals only, bare text values for f-string parts,
never AST byte offsets, never repr literals). Russian text, images, page
geometry: frozen. Pages: 8 (1950×2700), multiple-of-4 rule kept.

STATUS: builder-complete. NOT finalized, NOT repo-inserted, NOT posted to
Discord, NOT sent to main chat. Awaits independent proofread.

## 1. Baseline fidelity proof (tools/freeze.py)

Before any edit, tools/freeze.py baseline re-ran the unmodified core build
from a scratch copy: all 8 regenerated SVGs byte-identical to the shipped
core SVGs:

| page | sha256 (baseline reproduction = shipped core) |
|---|---|
| p1-pervaya | 8bfcb7e289dc383e79f1797d186ba6912943d3f3991e499d1513b0e478a5f827 |
| p2-zhizn | 5b35f1d7c000759fc5f3422d00d50ed1c1032893a9957e22aee3679f28bca872 |
| p3-kultura | 8be9ba7f8d32ad9b32fccdd7b04c304355c93a9abc29733c32e76c3932e6adad |
| p4-sport | 9d699050f467482a5adc60efc676a824d5dccfbae0e715bdc12b1393efd75278 |
| p5-molodezh | f49d0ed8b09b4ec7742ef6059a570b96377d78d2822c92271a4a6bba2ca04665 |
| p6-razbor | 8559d61d890820e02d5d2a1d1be511765ac9a9d70bdee21d72af10a5d5dbb767 |
| p7-yazyk | 961119d6a19e617bfd576f5354244fe4030882cc1f4b0b331084c37cfc3ec471 |
| p8-test | 2738ae046bda80306ddea411a6b8c27d5031b86f3c87aec3f3062f54f685e436 |

After all work, the core's shipped SVG hashes were re-verified: 8/8
unchanged. The core build directory was never executed in place and never
edited; all work happened in the copied build dir (the one driver process
run.py, never a standalone content module — README #7/#11).

## 2. Totals (this edition, from the final build log)

- Exercises: **150** — A2 51 · B1 75 · B2 24 (identical to core).
- Per page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
- By type (Portuguese type names): Completar frases 54 · Escolha múltipla
  42 · Associação de palavras 20 · Construção de frases 12 ·
  Transformação de frases 4 · Cloze 13 · Tradução 4 · Escrita 1.
- Writing model (#150): 84 words (registry-counted), frozen Russian.
- Registry meta diff vs core (page, level per item): zero mismatches.
- Final build: zero FLOW OVERFLOW / zero HEAD TOO WIDE warnings.

## 3. Key-diff registry (complete — both registries dumped and diffed)

Keys differ from the core in exactly **3** items; printed exercise bodies
(stems) re-aimed in exactly **2**; all other 147 keys are byte-identical
and all other 148 printed bodies are byte-identical to the core.

| # | kind | core | this edition (PT) |
|---|---|---|---|
| 137 | key | 11 月 4 日星期三放假。 | Na quarta-feira, 4 de novembro, é feriado. (note: Ver a página 3; instr: Traduza para o português; Russian stem frozen) |
| 138 | key | 促销码就是折扣码。 | Um código promocional é um código de desconto. (note: Ver a página 5; instr: Traduza para o português; Russian stem frozen) |
| 139 | stem | 星期六克拉斯诺达尔对阵中央陆军。→ ___ | No sábado, o Krasnodar joga contra o CSKA. → ___ (key unchanged Russian «В субботу «Краснодар» играет с ЦСКА.»; note: Atenção: играть + с + instrumental; instr: Traduza para o russo) |
| 140 | stem | 我祝大家民族团结日快乐！→ ___ | Desejo a todos um feliz Dia da Unidade Nacional! → ___ (key unchanged «Поздравляю с Днём народного единства!»; note: поздравляю + с + instrumental; instr: Traduza para o russo) |
| 150 | key (writing apparatus) | （开放题，范文如下） | (pergunta aberta — texto modelo abaixo) (note: O texto modelo está na seção H desta página (84 palavras); instr: Escreva; type: Escrita; printed as ✓ + note) |

This is exactly the W43 RU×PT precedent class (same numbers 137–140, same
re-aim directions). Notes rewritten in Portuguese: **142 of 150**. The 8
notes byte-identical to the core are pure-Russian form notes, kept as
printed by the core: #34 «устраивать → устраивают», #35 «гулять →
гуляют», #61 «играть → играет», #63 «закрываться → закрывается», #64
«победить → победил», #96 «отдыхать → отдыхаем», #112 «писать →
пишет», #146 «скидка 20%».

## 4. Printed-note set verification (tools/p8.py compare)

- Core P8: 150 noted. Edition P8: 150 noted.
- Verdict: **CLEAN, 150 = 150, missing = [], extra = 0, uncertain = []**.
- Tool-reported keydiff: [83, 137, 138, 148]. Adjudication (README #13:
  suspect the tool first — verified against printed lines + registry):
  - 137, 138: genuine re-aims, see §3.
  - 83, 148: EXTRACTION ARTIFACTS, not edition changes. Both printed keys
    are byte-identical to the core (83: «B» in both; 148: «A» in both;
    registry keys identical too). Cause: p8.py's paren branch — when a
    note ends in a paren group, the extracted “key” becomes
    «key — note-prefix», so the differing Portuguese/Chinese note
    prefixes surface as a false keydiff (core 83 note ends in a
    full-width paren group «（周三、周六、周日）», PT 83 in a half-width
    one «(quarta, sábado, domingo)»; same mechanism for 148). The tool
    was NOT modified; the artifact is documented here for the
    proofreader to re-verify from the printed lines.
  - 139/140: not in keydiff — reverse keys byte-identical, as required.
  - 150: not in keydiff — both editions print it via the ✓ apparatus
    (see §3 for the registry-level change).
- P8 bracket form: the RU core's own dash format «N. key — note» is KEPT
  (README #14: the family's shipped fan-out code is dash style); the
  Russian page separators «— СТРАНИЦА n —» are kept.

## 5. Portuguese furniture (verbatim as shipped; W43 RU×PT precedent)

- Masthead: «Lucerna» (no article), exactly as the core.
- P1 badge (subtitle slot y=372, 20 px bold BRICK, centered — the W43
  shipped form, which governs over the README §20 generic description;
  difference recorded in §9): «TEXTOS EM RUSSO · EXPLICAÇÕES EM
  PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA»
- P1 strap (y=330): «SEMANÁRIO RUSSO · VOL.2 · ПРАЗДНИК · СКИДКИ ·
  ФУТБОЛ» (W43 PT precedent: the «РУССКАЯ ГАЗЕТА» segment rendered as
  «SEMANÁRIO RUSSO», Russian topic words kept; see §9 for the W45
  ru-en divergence note).
- Top strip centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · TODA SEMANA · O RUSSO QUE
  A RÚSSIA LÊ» (W43 PT verbatim).
- Dark-band right (P1): «UMA QUARTA-FEIRA NO MEIO DA SEMANA» / «4 de
  novembro é feriado · ver páginas 2 e 6».
- Footer left (all pages): «Lucerna · SEMANÁRIO RUSSO VOL.2 · TEXTOS EM
  RUSSO · EXPLICAÇÕES EM PORTUGUÊS»; footer right: «Página N de 8».
- Gloss prefix: «Nota — » (library gloss() adds it).
- Section suffix pattern (W43 PT column): «· Em números», «· Sumário»,
  «· A palavra», «· Em resumo», «· Quiz-relâmpago», «· Na mídia», «· Tema
  principal», «· Agora é com você», «· Palavras da semana», «· Prós e
  contras», «· A semana dia a dia», «· Dados de prática», «· Clínica de
  erros», «· Frases da semana (transcritas deste número)», «· Na próxima
  semana (VOL.3)», «· Teste e respostas»; page bands: Vida / Cultura /
  Esporte / Juventude / Análise / Língua.
- Exercise instruction words: Complete · Forme a frase · Reescreva ·
  Associe · Traduza para o português · Traduza para o russo · Escreva.
- Number localization: ordinals 1.º/14.ª, decimal style as in the W43 PT
  column («19h30»/«16h15» for times, «12 de novembro» for dates).

## 6. Freeze check (visible-text diff vs core, tools/freeze.py diff)

Per-page: added CJK = 0 on every page (P1–P8), edition CJK total = 0,
full-width parentheses = 0 in all final SVGs. Every removed string is a
Chinese explanation string of the core; every added string is Portuguese
explanation layer, pairing furniture, or the documented registry items of
§3. Embedded image payloads byte-identical on every page (P1 ×1, P4 ×1,
P5 ×1, all other pages ×0 — the task's P1/P4/P5 ×1 each, confirmed by
SHA-256 of the decoded payloads).

Cyrillic token multisets (independent recount on rendered SVG text):
- P2–P8 EXACTLY equal to the core: P2 443, P3 338, P4 306, P5 316,
  P6 354, P7 397, P8 641 tokens.
- P1: 11 differing tokens, ALL itemized as the two furniture lines —
  badge replacement (y=372, W43 PT verbatim) and strap segment (y=330,
  «РУССКАЯ ГАЗЕТА» → «SEMANÁRIO RUSSO»): РУССКАЯ ×1, ГАЗЕТА ×2,
  ЕЖЕНЕДЕЛЬНАЯ ×1, ДЛЯ ×1, ИЗУЧАЮЩИХ ×1, РУССКИЙ ×1, ЯЗЫК ×1,
  НАСТОЯЩАЯ ×1, РОССИЯ ×1, ПО ×1, РУССКИ ×1. No unlisted Russian token
  loss anywhere.

Gloss check (split on «·» itself, README #21): 9 gloss() calls, 26 items
total, per-call counts equal to the core — P2 3/3/3, P3 3/3, P4 3, P5
3/2, P6 3. Every gloss headword is a frozen Russian word on its own page
(Cyrillic multiset equality, above).

P7 golden sentences: all 8 Russian sentences occur exactly 2× in the
issue (article + P7 «ФРАЗЫ НЕДЕЛИ» list), verified on page-joined SVG
text. P7 page tags (Страница 1/1/2/3/4/5/6/6) unchanged and correct.

## 7. Geometric occlusion audit (mandatory gate, tools/occlusion_audit.py)

Selftest first: all 6 planted classes fired exactly once; clean controls
silent. This edition: **0 flags** over all 8 SVGs. Core comparison:
core 0 flags, **NEW flags vs core = 0**. Same-baseline ink scan
(additional, README #10 — true PIL ink extents per baseline over all 8
pages, furniture bands included): **0 flags**.

P6 chart element check (README #12 blind-spot guard): all 4 bar labels
present with values 34/28/22/16 and proportional widths (600/494/388/282
px); labels sit left of the bars (x=65, bars from x=685) and values right
of the bar ends — no later-drawn rect covers any label or value ink.
The RU P6 chart has no ES-style frozen overlay text; 0 overlaps is the
expected result, confirmed element by element (not by audit flags alone).

## 8. Readers' corner — no fabrication (core example + Russian disclosure)

P7 prints the core's own editor's example («— М. (пример от редакции)»)
and the core's Russian disclosure unchanged; only the explanation-layer
disclosure line is translated to Portuguese: «Sem cartas reais nem
textos: exemplo da redação; promessa para o VOL.3.» No reader, letter,
name or quote is invented. The VOL.3 teaser repeats the call for letters.

Geometry (gate 6, frozen — NOT altered): readers'-corner box bottom =
**1727.58** (build log «P7 col3 ends 1727.58», identical to the core);
disclosure line 1 baseline 1709.88, line 2 baseline **1738.28**,
identical to the core's coordinates. The line-2-below-box-bottom contact
is the coordinator-adjudicated non-blocking frozen-core geometry
(ru-en precedent) — positions are byte-identical to the core, so the
KIT records it and the builder did not touch the box geometry. To hold
that geometry, the PT disclosure was worded to wrap in exactly 2 lines
(core: 2 lines) and the P7 clinic notes were shortened to one line each
(««с» + instrumental: с Днём единства.» / ««с» + genitivo: с 22
октября.», W43 PT clinic precedent) and the word-box line to one line
(«промокод = código promocional.»); with those shortenings the whole
P7 col-3 stack reproduces the core's 1727.58 exactly.

## 9. Differences recorded for the coordinator (furniture vs README)

1. Badge geometry follows the W43 RU×PT SHIPPED SVG (subtitle slot
   y=372, 20 pt bold BRICK, no masthead shift), not the README §20
   generic description — per the tasking rule that shipped artifacts
   govern over generalized descriptions.
2. P1 strap: W43 PT translated the «РУССКАЯ ГАЗЕТА» segment to
   «SEMANÁRIO RUSSO» and this edition does the same. The W45 ru-en
   sibling kept the strap fully Russian; if the coordinator rules the
   strap frozen, the single-segment revert is one literal in
   content12.py and does not affect any other gate (the strap tokens
   are itemized in §6).
3. Method name: the W45 core's explanation helper is already the neutral
   English `bridge()` (unlike the W43 core), so no rename was needed;
   the intermediary-layer term occurs 0 times in the paper, this KIT,
   and the operative build code.
4. The p8.py 83/148 keydiff artifacts (§4) are tool behavior, not
   edition changes; the tool was left unmodified.

## 10. Builder's proofread (full pass, this build)

P1 and P7 read end-to-end from the rendered cards (furniture-heavy
pages); all other pages verified programmatically (gates above) plus a
targeted read of the P6 chart region and the P8 E-section bodies. PT
layer complete on all 8 pages; no Chinese remnants (0 CJK in SVGs and
in all transformed sources); dates/weekdays in the PT layer match the
core's verified calendar (2 Nov Mon – 8 Nov Sun; derby 25 Oct; sale
22 Oct – 12 Nov; round 14 on 6–8 Nov; round 15 on 20 Nov); chart
34+28+22+16 = 100. No invented facts added in translation; the P6
practice-data disclaimer is translated in full («Estes são dados de
prática da redação para os exercícios — não são estatísticas reais.»).

## 11. Deliverables and PDF pins

- files/weekly-report-w45-ru-pt/svg/ ×8, cards/ ×8 (1950×2700 PNG)
- Print PDF: Lucerna-VOL2-PT.pdf — 13,556,944 bytes — 8 pages
- Web PDF: Lucerna-VOL2-PT-web.pdf — 3,203,592 bytes (< 10 MB) — 8 pages
- ABSTRACT.txt (Portuguese, one line, no ASCII double quotes — see §12)
- Build tree: hidden_files/weekly-report-w45-ru-pt-build/ (content
  modules, render.py, run.py, scratch/ with transform.py, build.log,
  freeze-diff.json, occlusion.json, p8 extracts + compare, registry
  dumps + diff, ru-en reference diffs)

## 12. ABSTRACT.txt (verbatim)

Lucerna · Semanário Russo VOL.2 (2 a 8 de novembro de 2026): textos em
russo com explicações em português para ler russo de verdade — a semana
com feriado na quarta-feira, a liquidação 11.11, a 14.ª rodada do
Campeonato Russo e o Dia da Unidade Nacional, com 150 exercícios de
russo do nível A2 ao B2, como se diz feriado no meio da semana em russo
e como usar o caso instrumental depois de с.

## 13. Hygiene / process notes

- Opening check: no in-progress writes existed for this edition (both
  target dirs absent at start); a concurrent ru-en repo-insert process
  was observed running but untouched (different edition).
- One service restart interrupted the first render.py run after the
  print PDF; render.py was re-run to completion and all artifacts were
  re-verified afterwards (cards, both PDFs, hashes) — no partial
  artifact shipped.
- No Discord post, no main-chat card/PDF dump, no cron created, no
  weekly-git contact. Finalized-edition routing is the coordinator's
  call after independent proofread.
