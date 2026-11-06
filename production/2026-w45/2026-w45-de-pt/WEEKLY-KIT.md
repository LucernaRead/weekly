# WEEKLY-KIT — Die Lucerna VOL.2 · DE×PT (W45, 2–8 November 2026)

**Status: fix round complete, NOT finalized, awaiting independent full re-proofread.**
This edition is NOT finalized. No Discord post, no main-chat card/PDF dump, no
repo insert has been made. The independent proofread found 2 blocking issues;
both were fixed in this round and all gates re-run (see §12 item 9 and
build/fix-record.md) — but per SOP §8.4 a render change requires a separate
independent full re-proofread before any finalization claim.

- Pairing: target German × native Portuguese (German body text frozen
  word-for-word; explanation layer rewritten directly in Portuguese for
  Portuguese-native readers; no intermediary language).
- Base: W45 DE core `files/weekly-report-w45-de-core/` (Die Lucerna VOL.2,
  finalized). Reference: W43 shipped DE×PT `files/weekly-report-de-pt/` (VOL.1).
- Build tree: `hidden_files/weekly-report-w45-de-pt-build/` (transform.py,
  transform-log.txt, build-log.txt, render.py, render-log.txt, svg-hashes.txt,
  core-hashes-before.txt, occlusion.json/.txt, p8-compare.txt,
  freeze-diff.json/.txt, rowcheck.py, chartcheck.py, dump_reg.py, reg-dump.json,
  plus fix-round records: fix-record.md, fix-baseline-hashes.txt,
  fix-after-hashes.txt, fix-build-log.txt, fix-render-log.txt,
  fix-freeze-diff.json/.txt, fix-p8-compare.txt, fix-occlusion.json/.txt,
  fix-rowcheck.txt, fix-chartcheck.txt, fix-reg-dump-log.txt).
- Issue week: Mon 2 – Sun 8 November 2026. Pages: 8. Exercises: 150.

## 1. Frozen-text对照 (freeze.py)

- Baseline: `tools/freeze.py baseline` on the pristine copy reproduced the
  shipped core **8/8 SVGs byte-identical**; core hashes re-verified OK after
  all work (before and after values identical — see §2).
- Core CJK totals per page → edition CJK total: P1 168→0, P2 186→0,
  P3 187→0, P4 155→0, P5 193→0, P6 228→0, P7 394→0, P8 1429→0.
  **Added CJK = 0 on all 8 pages.**
- P1–P7 removed strings with no CJK (multiset classification, all explained):
  - (a) P1 subtitle-slot line `DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE
    LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND` — replaced by the pairing badge
    (documented furniture, §6).
  - (b) Lone `。` orphans on P3/P4/P6 — the core's own cosmetic class
    (a gloss sentence-final mark wrapped alone); in PT the mark is inline
    (`.`) at the end of the corresponding gloss item. No content lost.
  - (c) P7 readers box: label `Ein Beispiel der Redaktion!` → PT label
    `Um exemplo da redação!` (explanation-layer furniture, as in DE×EN);
    `……` → ASCII `...` punctuation change.
    CORRECTION (fix round, proof issue 1): the NOCH EIN WORT definition
    was wrongly localized in the first render
    (`«der Tankrabatt» (página 2): o imposto reduzido sobre a gasolina e
    o diesel.`), and the earlier claim that this was "as in DE×EN" was
    FALSE — DE×EN/DE×ES/DE×IT all keep the German sentence verbatim.
    The fix round restored it verbatim in half-width-paren form, as in
    DE×EN: `«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin
    und Diesel.` with the PT gloss line `Desconto no combustível.` kept.
    The transform mapping (transform.py) and content7.py were both
    corrected so the fix cannot regress. Freeze effect: P7 diff
    +61/-54 → +60/-53; `gesenkte Steuer auf Benzin und Diesel.` is now
    in neither the removed nor the added set (frozen, identical in core
    and edition); the only remaining word-box line-1 diff is paren form
    (core full-width `（Seite 2）` vs edition half-width `(Seite 2)`).
- All other added German-looking strings were eyeballed: they are PT
  explanation, PT/German mixed lines (e.g. Zahlen lines, gloss items),
  furniture, or instruction tokens — no new German body text.
- P8 freeze is adjudicated by the p8.py CLEAN verdict (§3): keys identical,
  differences are only the PT separators/headers, the half-width-paren form
  (§4), PT notes, and translation items 137–140/150. P8 removed-noCJK
  fragments are all full-width-paren line fragments (e.g.
  `beschließen → beschlossen） · 17. ...`) whose half-width forms are present
  in the added set — paren-form change only, no German key lost.

## 2. Core hashes (before = after, verified OK)

Core shipped SVG sha256, recorded before any work and re-verified after:

- p1: 6cbd48022b5f863d941aa422869639ddc2ad2cbd203169ba87b85ba0d4fade3e
- p2: 9362256dca74f8772f3e45944e1e137c487d68e5a3fca772f93bf47e7b4b6d22
- p3: 3e8a8d16136a46a3781df045944f20eb821e0dba9b872e4f1ecc10758660ae9d
- p4: b787f592599cc4d1f862c16d901766e9775e5eac82330156617a04665cb0199d
- p5: 4dcbeb97c566f4dfb56e5cb7a6e97556f2f97246d97656e0b3f81c173decb77c
- p6: 01b75ad49a54c8037c15b885279aca9fcd530e815633eda7d1e1f79e2233090b
- p7: fbaf8cdd8a90f2994f4ecc4a769f64d717813c38e36acec74507c3aa162f278c
- p8: 299524bd2ad25ec447c0f422166b3db344b3caeba127e061fce37dc1e3c13891

Edition SVG sha256 (final render, pinned in build/svg-hashes.txt):

- p1-front: daf5c2caad6883bc256c70a2b99d7ab5bebb8d7e8853c43c56fd35ec96a4480b
- p2-leben: 05e8bcd74afa162eb3abfd1b74783aa93e55e3dfb2db07de26e77739c5996836
- p3-kultur: a706d043ee5fe797c1e1b8420045575eef4c891ce1d57e944d78602a0dbe5a62
- p4-sport: bca2649988242380befe84270e171eb8fc422e02d9645f9a45260d52c1321b18
- p5-jugend: dd96384fc4691a58e012f7eb6a41a2ff323db85be3981b191818fee5809516ac
- p6-vertiefung: 99e03a38c45a5c867ee8afce77f8af782d6e859e55e9f0018326801fa4365b0f
- p7-sprache: 171e37ce40f4a697068cbfad4129037c31cb2abd4c196fc39f174d3c56f18089
- p8-uebungen: e79f51f4de864d8f496a78f3f4f4ac86bc81338b8b966abb1ae0a8e8904bfc37

## 3. P8 verdict (tools/p8.py compare, core vs edition)

- **CLEAN. Core 150 noted = edition 150 noted, missing=[], extra=0.**
- keydiff = [137, 138, 139, 150] — all adjudicated TRUE changes, not tool
  artifacts (verified against the registry dump, not only the extraction):
  - 137 (A2 Tradução, stem DE `Der Tankrabatt läuft bis Dezember.`):
    key `O desconto no combustível vai até dezembro.` — translation re-aim
    (DE→PT), note `laufen = durar, continuar`.
  - 138 (A2 Tradução, stem DE `Ich schaue am Dienstag Fußball.`):
    key `Vejo futebol na terça-feira.` — translation re-aim, note
    `schauen = ver`.
  - 139 (B1 Tradução, stem DE `Die Schule hat wieder begonnen.`):
    key `A escola recomeçou.` — translation re-aim, note
    `wieder begonnen = recomeçou`.
  - 140 (B1 Tradução) is NOT in keydiff: its key is unchanged German
    `Am Sonntag schlafe ich eine Stunde länger.`; only the STEM is re-aimed
    (PT `Durmo uma hora a mais no domingo.`, instr
    `Traduza para o alemão`) — the reverse direction, verified correct.
  - 150 (B1 Escrita): open-task apparatus translated — key
    `Tarefa aberta — siga os pontos do quadro de escrita; o texto-modelo
    está no quadro desta página`, note `Avaliação pelos pontos indicados`.
- P8 answer notes are Portuguese throughout; P8 form follows the DE family's
  shipped fan-out code (README #14): half-width parens ` (note)` with a
  space, **13pt / 1.26** — the W43 DE×PT value (W45 DE×EN used 13/1.3; for
  this pairing the W43 DE×PT value was chosen). Full-width parens in the
  rendered edition SVGs: 0.
- P8 reverse item verified: item 140 stem/key pair above; no other reverse
  item is present in this issue's translation set.

## 4. Occlusion verdict (tools/occlusion_audit.py)

- Selftest: OK — all 6 planted classes fired (BOXTITLE, COVER, EDGE, FOOTER,
  LINEX, TEXTX); clean controls silent.
- **Edition 0 flags, core 0 flags, NEW vs core 0** (final render).
- Same-baseline ink scan (README #10 pattern, build/rowcheck.py, venv PIL):
  exactly 1 hit — P1 sommaire row S.3 at y=1436, title ink ends 1804.5 vs
  level-tag ink starts 1799.7 (4.8px). The core P1 SVG has the BYTE-IDENTICAL
  boxes for the same frozen row; visually the glyphs do not touch (clear gap
  on the card). Adjudicated **core-inherited, not a PT defect**; fixing it
  would require moving frozen German text, which is forbidden.
- P6 chart graze check (README #12 blind spot, build/chartcheck.py):
  **chart-band text-vs-later-rect overlaps = 0** for all chart texts
  (German labels, PT keyword labels, `%` texts). Bars unchanged from core:
  68/20/12 = 100; 68+20 = 88 (item 85 key agrees).

## 5. Gloss counts (README #21 — split on `·` itself, never ` · `)

- gloss() calls: 5 (P2, P3, P4, P5, P6), 5 items each.
- **Core 25 items = edition 25 items, 1:1, no additions, deletions, or
  merges.** Every PT gloss item's German headword was verified present in
  the rendered SVG text.
- P1 bridge line (not a gloss() call): 4 items core = 4 items edition.
- Gloss prefix: `Nota — ` (5 gloss boxes, matching the 5 calls; W43's "6
  gloss lines" reflected the W43 core's 6 calls, not this issue).

## 6. Furniture three-way check (this edition vs W43 shipped DE×PT SVG vs README #20)

W43 shipped DE×PT SVG wins verbatim; measured values on this edition:

- P1 pairing badge: string
  `TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES
  DE LÍNGUA PORTUGUESA`, slot y=372, x=975, 20pt, bold (700), anchor middle,
  fill **#a4553a (BRICK)** — byte-identical element to W43's badge
  (the builder's first render used OLIVE by mistake from the DE×EN recipe;
  caught by this check, fixed to BRICK, re-rendered).
- Footer on all 8 pages:
  `Die Lucerna · SEMANÁRIO ALEMÃO VOL.2 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM
  PORTUGUÊS` (VOL.2 substituted for W43's VOL.1; everything else verbatim).
- Page line every page: `Página {n} de 8`.
- Masthead on all 8 pages: the core's **Die Lucerna** (target language
  German; no other article).
- P1 top strip centre (W43 verbatim):
  `WÖCHENTLICH AUF DEUTSCH · TODA SEMANA · O ALEMÃO QUE OS ALEMÃES LEEM`.
- P1 46pt subtitle (issue-specific topics, VOL.2):
  `SEMANÁRIO ALEMÃO · VOL.2 · FUTEBOL · DESCONTO · CUIDADOS`.
- Gloss prefix: `Nota — `; P8 separators: `— Página {n} —` (all 8 present);
  P8 keys header: `ANTWORTEN · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)`.
- Section/box heads: German title + Portuguese part (W43 examples reused
  where applicable: `DIE TOPMELDUNG · Manchete`, `IN DIESER AUSGABE ·
  Sumário`, `DER WERKZEUGKASTEN · Úteis`, `A · LÜCKENTEXT · Texto lacunar`,
  `F · WÖRTER PAAREN · Associe`).
- Type map (matches W43 DE×PT registry names): 完成句子→Completar frases,
  单选→Escolha múltipla, 句型转换→Transformação de frases,
  词汇配对→Correspondência de palavras, 判断对错→Verdadeiro ou falso,
  完形填空→Completar o texto, 造句→Construir frases, 对话补全→Completar o
  diálogo, 翻译→Tradução, 写作→Escrita. Instruction tokens: 填空→Complete,
  改写→Reescreva, 判断→V ou F, 造句→Monte a frase, 翻译→Traduza para o
  português (item 140 fixed to Traduza para o alemão), 把词和释义配对→
  Associe as palavras.
- No frozen German line was altered or deleted to fit #20.

## 7. Toolchain (coordinator ruling)

- Delivered rendered SVG is authoritative.
- run.py: **tools/venv/bin/python — Python 3.12.3, PIL 13.0.0**.
  Baseline byte-reproduction: `freeze.py baseline` on the pristine copy
  reproduced the shipped core 8/8 byte-identical with the venv interpreter,
  so venv was kept for run.py too (system python3 is also 3.12.3 but PIL
  10.2.0; the venv run is what reproduces the baseline).
- render.py (cairosvg): **tools/venv/bin/python — Python 3.12.3, PIL 13.0.0,
  cairosvg 2.9.1** (system python3 lacks cairosvg; venv is mandatory here).
- KIT §7's "metrics must use venv PIL" applies to post-render SVG audit
  measurement (occlusion audit, rowcheck, chartcheck — all run under venv);
  it does NOT constrain run.py's internal wrap decisions.
- Transform: 394 replacements, exit 0; run.py exit 0, TOTAL 150, zero
  `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings on the final run.
  Flow ends match DE×EN exactly on P1–P6 (e.g. P1-headline 1555,
  P3 col3 1583.66, P4 col3 1135.25, P5 col3 1357.54, P6 col3 1320.33);
  P7 col3 ends 1504.5 (3.5px clear of the phrases rule at y=1508).
- Registry dump (one-process driver in the build dir, SVGs re-verified
  unchanged afterwards): TOTAL 150, continuous numbering 1–150, per-page
  10/18/18/18/18/18/12/38, levels A2 66 / B1 70 / B2 14 (identical to core —
  no re-leveling; DE core B2 14 is real), level badges present per item,
  types: Escolha múltipla 52, Completar frases 41, Transformação de frases
  11, Correspondência de palavras 12, Verdadeiro ou falso 8,
  Completar o texto 8, Construir frases 8, Completar o diálogo 5,
  Tradução 4, Escrita 1 (= 150, matching the core's type counts 1:1).

## 8. P7 golden sentences (VERBATIM)

All 8 German quotes are contiguous verbatim excerpts of this issue's own
articles and occur exactly 2× in the rendered SVG text (article + P7 table),
identical in core and edition. Page tags as printed, multiset:
Seite 4 · B1 ×2, Seite 2 · A2 ×2, Seite 5 · B1 ×1, Seite 3 · A2 ×1,
Seite 6 · B2 ×2 (= 8). The phrase-7 PT translation was shortened for layout
(see §11); the GERMAN quote itself is untouched.

## 9. Readers' corner (P7) — mandatory items, all present on the page

- Label (PT): `Um exemplo da redação!`
- German frozen strings untouched: defer
  `Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`;
  example letter
  `„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético. Die
  Fußballwoche ist toll! Viele Grüße — die Redaktion“`; invite
  `Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die besten
  echten Briefe drucken wir in VOL.3.`
- PT note (2 lines, states all three facts — no real letters, no best P8
  writing, promise deferred to VOL.3):
  `Sem cartas reais nem melhores textos da página 8; a promessa passa ao
  VOL.3.`
- PT explicit public invitation (2 lines; counts as the solicitation — the
  VOL.3 teaser's "your letters" line and other pages' write-in prompts do
  NOT count):
  `Escreva-nos! Envie a sua carta real e o seu texto da página 8 para o
  VOL.3.`
- The example is marked as the editors' example (PT label above it); nothing
  fabricated is presented as a real letter. No reader letters, names, or
  quotations were invented anywhere in this edition.

## 10. PDFs and cards

- Print PDF: `Die-Lucerna-VOL2-PT.pdf` — 4,144,470 bytes, 8 pages,
  1462.5×2025 pt, sha256
  313ff7635f3cde5bcef10c08119bdec1d89c7c531d6280bd433f6c7eecd748d2
  (post-fix-round values; pre-fix: 4,144,504 bytes,
  0bc3a3ba9163852befa0287094a99f46163ba629b448a0dfa62319b6f88fa594).
- Web PDF: `Die-Lucerna-VOL2-PT-web.pdf` — 4,167,866 bytes (< 10 MB),
  8 pages, 1400×1938 pt, sha256
  58e7294ca04d4f722cf5664038ac73f31f352de241ab1ba04d8f98cbeac04f42
  (post-fix-round values; pre-fix: 4,167,863 bytes,
  88ab3fedb4ba0adcbc903f1fb365c91382ac977f81d4ed3027a6ab190d5fb23a).
- Cards: 8 PNG, 1950×2700 each (p1-front, p2-leben, p3-kultur, p4-sport,
  p5-jugend, p6-vertiefung, p7-sprache, p8-uebungen). **All 8 viewed end to
  end after the fix round; no defect found** (P7 word box and P8 answer
  area specifically confirmed).
- Residue scans on rendered SVGs: CJK 0, full-width parens 0, full-width
  `｜`/`。`/`……` 0, `桥接` absent, `Le Lucerna`/`The Lucerna` absent,
  `VOL.1` absent, no Dutch/Russian/other-column furniture.
  CORRECTION (fix round, proof issue 2): the earlier "no leftover
  English tokens (expanded list)" assertion was WRONG — the pre-fix
  render contained exactly 1 leftover, P8 item 5's note
  `9 matches on matchday 9`. It was fixed to pure Portuguese
  (`9 jogos na 9ª rodada`, transform.py + content12.py both corrected)
  and the full 8-page expanded-list rescan after the fix is **0 hits**.
  Legitimate scan hits kept: `Quiz-relâmpago` (PT loanword) and German
  proper names (Real Betis, Manchester City, Crystal Palace,
  Champions/Europa League).

## 11. Terseness decisions the proofreader should know (disclosed, not buried)

1. **P7 toolbox items 3–4** (following shipped DE×EN's precedent, whose
   toolbox was hand-shortened to telegraphic 1-line items):
   item 3 `Es wird gespielt. = Será jogado` — dropped `(passiva)`; the A2
   lesson teaches the passive and the example is passive.
   Item 4 `Meiner Meinung nach... = opinião` — keyword gloss; the full
   phrase is taught in the B2 lesson and used in its exercise.
   The proofreader may restore fuller forms only if the P7 rail still ends
   ≤ 1508 (currently 1504.5).
2. **P6 chart keyword labels** (following the same terseness need — the
   full forms overlapped the bars: `cuidado familiar` right 577.2,
   `serviço de cuidados` 609.2 with 40% COVER, `lar de idosos` 543.0):
   `em família` (right 522.8, 12.2px clear), `serviço` (491.5), `em lar`
   (484.0). The fuller forms remain in the P6 article gloss
   (`der Pflegedienst = serviço de cuidados`) and in P6 chart-reading
   exercise notes (e.g. `serviço de cuidados 20% é o segundo`), so meaning
   is preserved; the chart-reading items themselves disambiguate by
   percentage (68% / 20% / 12%).
3. **P7 readers note shortened** (see §9): every version restating the
   "editor's example" wording wrapped to 3 lines and pushed the rail over
   1508; the marking is carried by the PT label `Um exemplo da redação!`
   directly above the box content.
4. **P7 phrase-7 PT translation shortened** to 2 lines:
   `A economia alemã deixa devagar a estagnação, mas a recuperação não se
   sustenta sozinha.` — keeps the "not self-sustaining" sense via
   `não se sustenta sozinha`; the German quote is untouched.

## 12. Self-repair list (fix history; wording-only, geometry never touched)

1. P1 headline overflow (first run): PT Zahlen box measured 361.9px vs EN
   306.5px (items 1 and 3 wrapped to 3 lines), cascading the headline flow
   past the page bottom. Shortened parentheticals:
   `(9 jogos na 9ª rodada da Bundesliga)` → `(9 jogos na 9ª rodada)`;
   `(14,04 centavos a menos de imposto por litro)` → `(14,04 centavos por
   litro)`. Box back to 306.5px, flow ends 1555.
2. P7 readers-box rh duplication: DE×EN's transform replaces only the first
   line of the multi-line `rh` assignment, leaving stale continuation lines
   (DE×EN's builder hand-fixed this afterwards). This build replaces the
   WHOLE rh assignment in transform.py (trailing `+40+32` = fix1's +16 plus
   another +16 for the second Portuguese para, as in DE×EN) and updates the
   fix1 comment's `last Chinese line` → `last Portuguese line`.
3. Four UND SIE paragraphs wrapped to 3 lines vs EN 2: P2 →
   `Você dirige? Quanto custa a gasolina aí? Escreva duas frases em
   alemão!`; P3 →
   `No outono você lê mais? Que livro está na sua cabeceira? Escreva duas
   frases!`; P4 →
   `Para quem você torce? Quem vence no sábado? Escreva duas frases!`;
   P5 →
   `Quando você voltou? Qual foi a sua primeira aula? Escreva duas
   frases!`. Safe because each German `etvous` question above already ends
   `Schreiben Sie zwei Sätze auf Deutsch!` (P4's also contains
   `in dieser Woche`). Restored P3 col3 ends to 1583.66 and P2/P4/P5 col3
   ends to EN values.
4. P7 rail over height (1591.5 vs phrases rule 1508): toolbox + readers
   paras — see §11 items 1 and 3. Result: P7 col3 ends 1504.5.
5. Occlusion round 1: 11 NEW flags → all fixed by wording:
   P1 Fragen bottom line → `As cinco perguntas mais debatidas.`
   (audit-measured right 1783.5 < border 1885);
   P2 col3 box title → `AN DER ZAPFSÄULE · Na bomba` (1841.0; the long form
   ran to 1996.5, past the 1950 page edge);
   P3/P5 facts titles (SHARED pair) → `FERIENWECHSEL · Férias` (1766.5);
   P3 vocab → `HERBSTWÖRTER · Outono` (1780.5);
   P5 vocab → `SCHULWÖRTER · Escola` (1752.5);
   P6 numbers box → `DIE ZAHLEN · Números` (1743.5);
   P6 ÜBUNGSDATEN caption ran to x=2067.2 (off-page) → tail shortened to
   `(Exemplo de prática da redação, não uma pesquisa real.)` (right 1860.2);
   P6 chart labels overlapped bars → keyword glosses (§11 item 2);
   P7 phrase-7 translation wrapped to 3 lines, pushing its tag into the
   error-clinic rule → shortened (§11 item 4);
   P8 section B head warned `HEAD TOO WIDE` → `B · WISSENSFRAGEN ·
   Perguntas`.
6. English leftovers found by rendered-SVG token scan and fixed:
   bars third label `care home` (adapt mapped `care home 12%` but not bare
   `care home`) → `em lar`;
   P5/P8 notes `ist/muss/liegen goes to the end` → `ist/muss/liegen vai
   para o fim` (adapt script lacked mappings for the three verb-specific
   notes);
   chain-dependency lesson: core P6 note `专业上门 20% 第二` becomes
   `serviço 20% 第二` AFTER the chart-label rep, so its note-pair old string
   had to be updated to `serviço 20% 第二` (new kept as
   `serviço de cuidados 20% é o segundo`) when the chart label changed from
   `serviço de cuidados` to `serviço`.
   A mid-fix transform failure once left a mixed-language build (content12/34
   PT, content56 partial, content7/8 still Chinese) while run.py still
   exited 0 with TOTAL 150 — that render was discarded as invalid.
   **Lesson: always check transform.py's exit code (must be 0) before
   running run.py; run.py exit 0 alone does not prove a clean build.**
   Two adapt misses also fixed: `This week's big questions` →
   `As grandes perguntas da semana`, `Germany's five hot questions.` →
   `As cinco perguntas mais debatidas na Alemanha.` (later shortened per
   fix 5). Legitimate scan hits kept: `Quiz-relâmpago` (PT loanword) and
   German proper names (Real Betis, Manchester City, Crystal Palace,
   Champions/Europa League).
7. P2 title patch was missed in one patch round (occlusion stayed at 2 NEW
   flags for one cycle); patched afterwards and re-verified to 0.
8. **Badge color (final fix, caught by the §6 three-way check):** first
   renders used OLIVE (#3e4c2a) copied from the DE×EN recipe; W43 shipped
   DE×PT measures BRICK (#a4553a). Fixed in transform.py, full single-process
   re-render, all gates re-run (occlusion 0/0/0, p8 CLEAN, flow ends
   unchanged, P7 col3 1504.5). Only P1's badge element changed.
9. **Fix round (independent proof, 2 blocking issues; NOT a finalization):**
   (a) P7 NOCH EIN WORT definition restored verbatim to German
   (`«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und
   Diesel.`, gloss `Desconto no combustível.` kept) — transform.py
   mapping + content7.py both corrected; the §1(c) "as in DE×EN"
   claim for the localized version was false and is corrected above.
   (b) P8 item 5 note `9 matches on matchday 9` → pure Portuguese
   `9 jogos na 9ª rodada` (key `neun` unchanged, matches the P1 Zahlen
   parenthetical) — transform.py mapping + content12.py both corrected.
   Full single-process re-render (tools venv run.py + render.py, exit 0,
   TOTAL 150, zero warnings; P8 keys flow end 2369 → 2352, P7 col3
   still 1504.5); all gates re-run: freeze P7 +60/-53 with added CJK 0
   all pages, p8 CLEAN 150=150 with keydiff still [137, 138, 139, 150],
   occlusion 0/0/0, gloss 25=25, P7 golden 8×2, P7 rail ink bottom
   1490.97 (17.0 px above the y=1508 rule), English-residue rescan 0,
   8 cards re-viewed. Change scope verified by hash diff: ONLY p7/p8
   SVGs, p7/p8 cards, and both PDFs changed; p1–p6 SVG/card bytes
   identical. Full record: build/fix-record.md. Still NOT finalized —
   awaits an independent full re-proofread per SOP §8.4.
