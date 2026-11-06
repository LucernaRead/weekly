# WEEKLY-KIT — Japanese Weekly VOL.2 · JA × PT edition (Japanese text · Portuguese explanations)

The Portuguese-explanations edition of the W45 Japanese Weekly VOL.2: the
same issue as the finalized core edition (Japanese text + Chinese
explanations), with the whole explanation apparatus rewritten in
Portuguese for Portuguese-speaking readers. Japanese content — articles,
exercise stems and options, quoted sentences, the text being taught — is
unchanged, element for element, except for the single coordinator-ruled
readers'-corner change documented in §6.

- Week: Mon 2 – Sun 8 Nov 2026 (W45, VOL.2) · 8 pages · page size 1950×2700
- Files: `svg/` (8 SVG), `cards/` (8 PNG 1950×2700),
  `Lucerna-VOL2-PT.pdf` (print, 28,030,615 B),
  `Lucerna-VOL2-PT-web.pdf` (web, 3,105,903 B — under the ~10 MB server limit)
- Core edition (frozen, untouched): `files/weekly-report-w45-ja-core/`; core build:
  `hidden_files/weekly-report-w45-ja-build/`. This edition's build:
  `hidden_files/weekly-report-w45-ja-pt-build/` (transform.py + run.py +
  render.py + per-round sha256 baselines + gate outputs). The core was never
  modified — final check: all 8 core SVGs still byte-identical to the
  pre-build baseline (hash list `baseline-core-pre.sha256` in the build tree,
  identical before and after this build).
- Status: ROUND 2 COMPLETE. This is NOT a finalization: per SOP §8.4 a fresh
  full independent proofread is still required before any delivery. No
  Discord post, no chat card/PDF dump, no cron, no weekly-repo touch was
  made by this build.

## 1. Pairing badge and footers (W43 JA × PT shipped precedent, measured)

- P1 masthead carries the pairing line, bold brick, centered, 19 pt, at
  y=356, exactly as in the shipped W43 JA × PT SVG:
  **TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA**
  Masthead name stays "Lucerna", no article — Japanese is an article-less
  language. Masthead geometry copied whole from W43 JA × PT, measured
  directly from its shipped P1 SVG: wordmark baseline 262→248, edition line
  330→316, badge inserted at (975, 356) 19 pt, tagline 372→390, rules
  392/401→406/413, dark band stays at y=424. The README §20 JA-target note
  (wordmark stays at 262, from the JA × ZH-TW case) was NOT followed: the
  same-pairing W43 JA × PT geometry (wordmark 248) governs, as it does in
  every shipped W45 JA sibling (EN/DE/FR all measure 248).
- Top strip: "VOL. 2 · 第2号" (core, frozen); middle line "毎週、日本語で ·
  Toda semana · 日本人が読んでいる日本語を読む" (the core's Chinese middle
  segment replaced by "Toda semana", per W43).
- P1 dark band, right side (Portuguese, short form per W43 pattern):
  "Terça-feira é o Dia da Cultura" / "Depois do feriado, chega o fim de
  semana das folhas · Veja a página 3".
- Every page footer: left
  `Lucerna · SEMANÁRIO JAPONÊS VOL.2 · TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS`,
  right `Página n de 8`.
- In-text gloss lines use the prefix `Nota — ` (was the core's Chinese
  prefix). Band subtitles follow the W43 pattern "レベル … · <Japanese
  theme> · <Portuguese theme>".
- Section furniture (Portuguese halves, W43 wording): "Em destaque",
  "Em números", "Pratique agora", "Neste número", "A palavra da semana",
  "Notícias breves", "Quiz-relâmpago", "A sua vez", "Palavras da estação",
  "Exercícios da página N", "Respostas na página 8 · Níveis mistos:
  procure o seu número", "Vamos ler o gráfico", "Dados de prática",
  "Teste e respostas", "A frase modelo", "Cantinho dos leitores",
  "Frases da semana (textuais, deste número)", "Na próxima semana (VOL.3)",
  "Respostas — agrupadas por página: basta procurar o seu número",
  "Uma nota breve em português para cada resposta · ✓ = a pergunta com o
  texto-modelo", separators "— Página N —".
- Registry type names (W43 set, Portuguese): complete a frase, múltipla
  escolha, associação de palavras, construção de frases, verdadeiro/falso,
  cloze, tradução, redação. Instructions: "Complete", "Construa uma frase",
  "Verdadeiro ou falso?", "Ligue palavras e sentidos",
  "Ligue os eventos aos lugares e às datas", "Traduza", "Redação".

## 2. Counts (measured three ways: registry, freeze diff, independent SVG count)

- Exercises: **150** — A2 46 · B1 75 · B2 29; per page
  10/18/18/18/18/18/12/38. Independent SVG count (level chips + number
  labels in document order): P1–P7 = 112, P8 = 38, numbers continuous
  1–150. No FLOW OVERFLOW, no HEAD TOO WIDE in the final round.
- Page 8 writing model 『私の11月の週末』 = **167 characters** (counted
  programmatically by the build, inside the printed 150–200 range),
  byte-identical to the core.
- Gloss items (rendered gloss() strings split on ·, counted item by item,
  Japanese headwords byte-identical core vs edition): feature pages core
  39 = edition 39 — P1 4, P2 9, P3 8, P4 7, P5 7, P6 4. P7 column bridges
  core 9 = edition 9 (A2 3 / B1 3 / B2 3), headwords byte-identical.
- P7 phrases of the week: all 8 verbatim quotes occur exactly 2× in the
  full-issue blank-stripped text concatenation (quote in its article +
  quote in the P7 list). Source-page tags match the core's mapping
  (core 第N面 → edition p.N): p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6.

## 3. What changed vs the core — and what did not

Changed (apparatus only): every gloss/note, exercise instruction,
section-header and band-subtitle Portuguese half, the three "A sua vez"
reader lines, the P2 season-word card glosses, the P7 error-clinic notes,
frame note, the P7 phrase translations, the answers header, the keys'
group headers, the registry type names, and **all 150 answer notes** —
rewritten as full, natural Portuguese.

Re-aimed translation items (E zone, the only key changes; W43 JA × PT
pattern — bodies re-aimed at Portuguese, Japanese keys byte-identical):
- #137 key (JA→PT): `O Dia da Cultura é 3 de novembro.`
- #138 key (JA→PT): `Se jogar lixo na rua, a multa é de 2.000 ienes.`
- #139 body now a Portuguese prompt
  (`A Semana da Leitura começa em 27 de outubro.`); its Japanese key is
  byte-identical to the core.
- #140 body now a Portuguese prompt
  (`Quero ir a Kobe ver as luzes das folhas de outono.`); its Japanese
  key is byte-identical to the core.
- #150's registry line reads `(tarefa aberta — texto-modelo abaixo)` (its
  note is `Texto-modelo na seção H desta página (167 caracteres)`); the
  item itself, an open writing task, is unchanged.

Not changed: every Japanese article, stem, option, letter and figure; all
other keys; the P4 G3–G7 schedule-only treatment with the VOL.3 deferral
note on the page; the P6 practice chart (38/27/21/14 = 100, labelled
practice data); the P8 38-item structure; です・ます style; full-form
weekday spellings (土よう日, 日よう日).

Deliberate deviation from the JA × EN sibling (same-pairing W43 wins):
the P8 band sub-header reads `Página 8 · 週の大きなテスト + 全ての答え`
(W43 JA × PT form). JA × EN kept the core's `第 8 面` tag there; this
edition localizes it, per the W43 same-pairing precedent.

## 4. Images (payload-verified per page vs the core)

- P1 maple (Poliphilo — CC0, Wikimedia Commons), P3 Hiroshige III print
  (歌川広重（三代）, 1876, public domain, Wikimedia Commons), P4 stadium
  (Syced — CC0, Wikimedia Commons), P5 pumpkin (Petr Kratochvil — public
  domain, Wikimedia Commons). Base64 payload hashes per page are identical
  to the core's (P1 92f3f41c7cec, P3 76f4abb34efc, P4 ab8d113ff083,
  P5 f954d75303c8 — first 12 hex chars of sha256). Credits on the pages
  match the core's, character for character.

## 5. Topics and sources (inherited from the core, unchanged)

Culture Day Tue Nov 3 + the Nov 7–8 autumn-leaf peak weekend (Naruko
Gorge peak; Kobe Nunobiki Herb Garden illuminations from Sat Nov 7) +
yuru eating trend (Ajinomoto, Oct 21) + Reading Week in progress (ends
Nov 9) + Ritto Sat Nov 7; Japan Series G1/G2 verified reports (G3–G7
schedule only, results deferred to VOL.3 on the page); Halloween Oct 31
as a just-passed report; JMA Oct 20 three-month forecast; note.com
Oct 22 roundup explicitly marked as not a survey; practice chart data
explicitly marked as practice data.

## 6. P7 structure (measured from the core) and the readers'-corner ruling

Core P7, verified by reading the core build: A2 column 本と読書のことば
(Reading Week) / B1 column 紅葉のことば (autumn leaves) / B2 column
数字を読む (reading numbers) + error clinic (4 items: past tense after
昨日, こと nominalization, か所 for places, で for place of action) +
frame box 『ゆるく整える』 breakdown + readers' corner + VOL.3 teaser.
Column definitions and quote originals are verbatim; only glosses and
explanations are localized to Portuguese. Definition-sentence localization
would be a blocking failure — none occurred: P7 Japanese definition
sentences are byte-identical to the core's (B1 definition paragraph and
the sample letter verified present verbatim in the edition build).

Readers' corner (coordinator ruling, executed as ordered): no reader,
letter, name or quotation was invented. The core's sample letter is kept
verbatim. The core's Chinese disclosure is the core reader-native layer
and was replaced by a Portuguese disclosure stating the 3 facts (sample
stands, not a real letter; no real letters received by the deadline; no
best P8 compositions received; both will appear in VOL.3) plus an
explicit imperative invitation with a VOL.3 publication promise. The
core's Japanese disclosure line was NOT kept as the operative disclosure
(Portuguese readers cannot read it, which would violate the
all-explanations-in-the-reader's-language rule). The VOL.3 teaser line is
a contents preview, not an invitation, and is not counted as one.

Verbatim solicitation sentence (the operative invitation, rendered on P7):
"Envie a sua carta em japonês!" — full disclosure line: "Exemplo da
redação, não é carta de verdade. Até o fechamento, não chegaram cartas
nem as melhores redações da página 8; ambas sairão no VOL.3. Envie a sua
carta em japonês!"

Scope ruling (stated, not assumed): the solicitation sentence literally
covers letters only. The combination still satisfies the gate because
(a) the same disclosure sentence defers the best P8 compositions to
VOL.3 ("ambas sairão no VOL.3"), and (b) the VOL.3 teaser band on the
same page names the P8 best texts explicitly ("読者の手紙と第8版の作文の
優秀作も載せます"). Disclosure + teaser together cover both promises;
the teaser line alone is not counted as the invitation.

## 7. Mechanical gates (all measured on the FINAL files, round 2)

- Core baseline (tools/freeze.py baseline, scratch repointed copy):
  **8/8 SVGs byte-identical**; shipped core SVGs re-hashed unchanged.
- Frozen-core diff (tools/freeze.py diff --strict-cjk, final):
  added CJK characters **0 on all 8 pages** (P1 1406→1275, P2 1312→1161,
  P3 1172→1051, P4 1263→1169, P5 1247→1132, P6 1186→1101, P7 1676→1308,
  P8 2721→1446 — reductions are the removed Chinese explanation layer;
  P8 is 1446, not JA × EN's 1448, because this edition also localizes the
  P8 band sub-header `第 8 面` → `Página 8`, removing 2 more CJK chars).
  Added/removed string lists were read in full: removed = Chinese
  explanation strings + the ruled readers'-corner disclosure + page-tag
  furniture; added = Portuguese apparatus + Japanese headwords already in
  the core. No frozen Japanese sentence is removed or altered.
- Banned intermediary-layer term: **0 occurrences** in all SVGs,
  ABSTRACT.txt, this KIT, and the operative build code (checked with an
  escaped-literal scan; the scan script itself carries only the escaped
  form, never the term's own characters).
- Chinese residue, word-level review: every CJK token in the edition's new
  build strings was checked against the core's quoted strings — **0 tokens
  absent from the core** (all are frozen Japanese headwords, section heads,
  or Japanese words quoted inside Portuguese notes/glosses). CJK
  characters present in edition SVGs but absent from core SVGs: **none**.
  A simplified-only codepoint scan finds only shared kanji in frozen
  Japanese; zero simplified-only residue.
- Japanese line-start rule (kinsoku NO_START set from the canonical
  svglib, all 8 pages): core 0 = edition 0 on every page.
- P8 (tools/p8.py compare, explicit dual-path form):
  **CLEAN, 150 = 150, missing [] extra []**.
  Keydiff list [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117,
  118, 137, 138, 140, 146, 147] adjudicated item by item, counted once
  (no double counting):
  17 are note-only translations (printed key byte-identical; the tool's
  extracted key differs only because the translated note text is part of
  the extracted segment); #5 and #101 are parenthesis-branch extraction
  artifacts — printed keys verified byte-for-byte (key 7 and key 27
  identical in core and edition, only the notes differ); #137 and #138
  are the legal E-zone re-aims (§3). #139 is NOT in the keydiff (its
  Japanese key is byte-identical); #140 sits among the 17 note-only
  items — its extracted-key difference comes from the core note's
  full-width parenthetical staying attached in the tool's paren branch
  while the Portuguese note has none (dash branch); the printed Japanese
  key is byte-identical, verified by direct SVG line comparison.
  P8 comment set equality holds with no extras.
- P8 note completeness (the standing JA-family gate): the P8 keys-region
  line comparison core vs edition finds **0 byte-identical lines**
  (edition 158 lines = 150 answers + 8 separators, 0 wrapped continuations;
  core 159 = 158 + 1 wrapped line). Every core Chinese note is localized;
  nothing slipped through untranslated. The JA-family bare-string trap was explicitly
  handled: core content34.py's P8 #37 prompt is registered as the bare
  string for key 8 (no weekday suffix), distinct from #32's suffixed note
  and from the longer exhibition note; the transform maps it explicitly
  to Portuguese ("A exposição vai até 8 de novembro"), and the rendered
  P8 card shows `37. 8 — A exposição vai até 8 de novembro`. Fact check:
  the P3 stem is `展覧会は11月 ___ 日（日）までです。` and 2026-11-08 is
  a Sunday, so the note matches the stem fact.
- Geometry (tools/occlusion_audit.py, selftest green, all 6 classes fire):
  edition **0 flags**, core **0 flags**, NEW vs core **0**.
  Same-baseline ink collisions on furniture bands: 0.
  Right-edge ADVANCE scan (all text elements, advance width, limit
  x=1885.5): 1 line at 1885.7 — the frozen P8 model-text line, byte-identical
  in the core (core measures 1885.7 too); 0.2 px over an internal
  threshold, 64.3 px inside the 1950 page edge, canonical EDGE = 0.
  Adjudicated as inherited frozen geometry, not an edition defect.
  Full-page frame-line scan (later-drawn rect borders / lines vs text
  ink, canonical ink boxes): 0 hits.
  P6 chart-label coverage, baseline-anchored ink method (canonical ink
  boxes, bars as later-drawn rects): max coverage **0.000** (gate <30%).
  Chart labels sit fully clear of the bars.
- Frame/box check: box-title ink vs own borders is covered by the audit
  (0 BOXTITLE); the P7 teaser band ends at y=2524.12, inside the 2540
  content limit and 56 px clear of the 2580 footer line; the P8 keys flow
  ends with last baseline 2514.92 (≈2530 flow end, <2540), 0 wrapped
  continuations.
- Essay: 167 characters, core-identical.
- All 8 cards viewed individually (P1–P8): no overflow, overlap, clipped
  label, or misplaced box found on visual pass.

## 8. Fix rounds (each round's edits went into transform.py first, then a
## single-process re-render; pre-fix sha256 baselines recorded each round)

- Round 1 (baseline): first full build. Counts exact; freeze strict-CJK 0;
  P8 CLEAN 150=150 with the same 21-item keydiff; but 4 NEW occlusion
  flags (P2 EDGE + P8 TEXTX ×2 from the over-long match instruction
  `Ligue as palavras aos significados`, P4 BOXTITLE from the schedule-box
  title), a P8-keys FLOW OVERFLOW (16 wrapped answer lines pushed the
  flow end to 2569, past the 2540 limit), and a P7 teaser band ending at
  2582.12 (past the footer line) because the Portuguese readers'-corner
  disclosure ran longer than the core's two disclosure lines.
- Round 2 (final): all fixes in transform.py only, then single-process
  re-render. Match instruction shortened to `Ligue palavras e sentidos`
  (PIL-measured 227.7 px at 19.5 pt, inside both the P2 slot limit 238 px
  and the P8 slot limit 245 px); P4 schedule-box title shortened to
  `日本シリーズの日程 · Calendário`; 16 P8 notes shortened with
  PIL-verified single-line fits (shared-note edits fix #14/#83 and
  #96/#127 in pairs; #140's note shortened to `Veja a página 6`, dropping
  the parenthetical — the page-6 cross-reference is retained); the
  readers'-corner disclosure shortened to the 5-line form quoted in §6
  (all 3 facts + imperative + VOL.3 promise kept). Pre-fix baseline:
  `sha256-round2-prefix.txt` (build files) +
  `sha256-round2-prefix-deliverables.txt` (round-1 deliverables).
  Changed deliverables (sha256 diff vs round 1): exactly P2, P4, P7, P8
  SVG + cards and the dual PDFs; P1/P3/P5/P6 SVG + cards byte-identical.
  Final gates (§7) all green; no FLOW OVERFLOW, no HEAD TOO WIDE.
  NOTE: this KIT does NOT replace re-proofread — per SOP §8.4 the rendered
  changes require a fresh full independent proofread round before any
  delivery.

## 9. Reproduction

Build directory: `hidden_files/weekly-report-w45-ja-pt-build/`
(transform.py = the single source of the edition build; run.py = the
one-process driver, byte-identical to the core's run.py, sha256
ca45aabf00da011853dd286337e83be8be8f3ae864c2ab9de0f1e2f5780493d3;
render.py = cards + PDFs; svglib.py = canonical JA build, md5
d73e23b365676c3618d7e060b835eb4d, copied verbatim and never edited).

```bash
cd hidden_files/weekly-report-w45-ja-pt-build
../../tools/venv/bin/python transform.py   # core build -> edition build
../../tools/venv/bin/python run.py         # ONE process: content12->34->56->7->8
../../tools/venv/bin/python render.py      # cards + print PDF + web PDF
```

Interpreters (recorded separately, as required):
- run.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0.
  (The frozen-core baseline reproduction, §7, was also run under this
  interpreter through tools/freeze.py; the reproduced 8 SVGs are
  byte-identical to the shipped core SVGs except for intended edition
  changes — the baseline itself is 8/8 identical before any transform.)
- render.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
  cairosvg 2.9.1, pypdf 6.21.2. System python3 (PIL 10.2.0, no cairosvg)
  was NOT used for any render step.
Shared-registry rule honored: content modules run only through the
single driver process, never standalone, never imported inside the core
build directory. No build-tree script was ever run in a way that writes
back into the delivery or core directories; re-runs with expanded scope
were copied to scratch first with OUT redirected (per the task's
standing rule, no such run was needed in this build).

## 10. W43 JA × PT deviations (same pairing, W43 shipped SVG as yardstick)

Furniture deviations: NONE except those forced by the issue itself —
VOL.2 (vs VOL.1), PDF names `Lucerna-VOL2-PT(.pdf/-web.pdf)` (W45
fan-out naming; W43 used `Lucerna-VOL1-PT`), the P8 band sub-header
`Página 8` (kept from W43; the JA × EN sibling instead kept the core's
`第 8 面` tag — see §3), and the readers'-corner disclosure, which
follows the W45 coordinator ruling (§6) rather than W43's shorter form.
Masthead geometry (wordmark 248, not the brief's 262 note — W43 measured
governs), badge text verbatim, footer pattern, gloss prefix, P8
separators/headers, instruction and type-name sets, quote page-tag style
(p.N), band-subtitle pattern, and "A sua vez" wording are all identical
to the W43 JA × PT precedent.

## 11. Delivery record (builder scope only)

- Delivered to: `files/weekly-report-w45-ja-pt/` — svg ×8, cards ×8,
  print PDF, web PDF, WEEKLY-KIT.md (this file), ABSTRACT.txt.
- Print PDF: 28,030,615 B,
  sha256 896535de98dc7b2d87e4b7af41d448edda613b0a7fa70dc45c7fd3d583de3201
- Web PDF: 3,105,903 B,
  sha256 8de2147ee421d3ed48d3eee4aa2b19b3f2660d17b3733c642c313c070d34658e
- SVG sha256 (final): p1 b5c913c99815de0da304642d5a07ae4c76aa9d70dd92c18267aed0f5af6d8963,
  p2 e42295aabaa6b65c4f82906c036beb447f6a5d507f070d2781aea327b664529b,
  p3 34e474fe99dd867ad1be21f540c8dcd060fcfb61ed853121fbbe53360af818b9,
  p4 73a0e918885b5e90a348a45dad2983aece5b13c9d11b368713d2e24032ab84d6,
  p5 a9803512e906aa5ea8ebeb4d2fead8aaf7faf7021648d5d52a7d7abbb20b1ed9,
  p6 2dcf7dd9d921321e3a2baa1ace04cfcf9e8017495770cfce7a9fcd0da698c7ea,
  p7 a9c1dbf0e2cc8205b0a0b43ba11049f29a932ac3816e9282bc16e8c4b2df59cf,
  p8 ceadeff6f2ec49c24c77f0dc2e215d5b17403e5c7ed4d98c14bd0a68d0e34c5c
- NOT done (out of builder scope, awaiting a fresh full independent
  proofread per SOP §8.4 and the main line): finalization announcement,
  Discord delivery (still paused by the user's standing order), repo
  insert, any cron change.
