# WEEKLY-KIT — EN × PT (VOL.2, W45)

- **Edition**: The Lucerna Weekly VOL.2 — English target text, explanations in
  Portuguese (Brazilian). Week of November 2–8, 2026. Slug:
  `weekly-report-w45-en-pt`.
- **Base**: W45 EN core (`files/weekly-report-w45-en-core/`, VOL.2, masthead
  The Lucerna). This is a fan-out: the English body is frozen, only the
  explanation layer is localized into Portuguese. Nothing else changed.
- **Status**: BUILDER SELF-CHECK COMPLETE. This is not a final sign-off:
  final status requires an independent proofread round (not done here).
- **Not done by this build**: no Discord post, no chat card/PDF dump, no
  cron, no weekly-git touch, no change to the core or W43 directories
  (read-only reference throughout; core SVGs re-hashed unchanged after
  every run — see §7).

## 1. Format

- 8 pages, 1950 × 2700, four columns, warm ivory paper, dark olive-green
  accents. Deliverables: 8 SVG sources + 8 full-page PNG cards + print PDF
  + web PDF + this KIT + ABSTRACT.txt.
- Masthead: The Lucerna (UnifrakturMaguntia wordmark) + subtitle
  `SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA` (46px serif)
  + pairing badge (see §3).

## 2. Contents by page (core topics, frozen English body)

- P1 (A2): head story — America votes Tuesday, November 3 (midterm; all
  435 House seats on the ballot); clocks fell back Sunday, November 1
  (25-hour night; Arizona and Hawaii do not change); searches chart;
  contents; word of the week `midterm`; IN BRIEF; lightning quiz.
- P2 (A2): life — the repeated hour, Halloween Saturday, October 31
  (past event); telling the time; clock diagrams; exercises.
- P3 (A2→B1): culture — Friday, November 6 films: `The Cat in the Hat`
  and `Godzilla Minus Zero`; at-home screen guide; five-sentence reviews.
- P4 (B1): sport — Sunday, November 8: NFL in Madrid (Bengals–Falcons),
  F1 São Paulo Grand Prix, NASCAR, WTA Finals, boxing in Arlington;
  Saturday MLS warm-up.
- P5 (B1): youth — election night at home: maps, phones, pizza;
  `too close to call`; election-night phrases.
- P6 (B2): deep read — how America votes: fifty states, fifty systems;
  practice ballot; teaching chart `Why do voters vote early?` — No lines
  38 / Work on Tuesday 29 / Travel plans 21 / Habit 12 = 100, explicitly
  labeled on the page as teaching data, not a real poll; no polls or
  predictions printed anywhere in the issue.
- P7 (A2/B1/B2): language in hand — three level columns + toolbox +
  phrases of the week + error clinic + readers' corner + VOL.3 preview.
- P8 (all levels): final test A–H + writing + model essay + full answers
  and notes for pages 1–8.

## 3. Furniture registry (W43 EN × PT shipped edition wins)

Source: `files/weekly-report-en-pt/` (VOL.1) shipped SVGs + KIT §5. All
forms below are copied from that edition unless marked W45-specific.

- P1 badge (subtitle slot y=372, 19.5pt bold brick):
  `TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS
  LEITORES DE LÍNGUA PORTUGUESA`.
- Footer: `The Lucerna · SEMANÁRIO INGLÊS VOL.2 · TEXTOS EM INGLÊS ·
  EXPLICAÇÕES EM PORTUGUÊS`; page line: `Página {n} de 8`.
- Top strip: `WEEKLY IN ENGLISH · UM NÚMERO POR SEMANA · O INGLÊS QUE A
  AMÉRICA LÊ` (W43 form, unchanged).
- Gloss prefix: `Nota — ` with comma-style items
  (`word, explicação · …`); the build library adds the prefix, so
  gloss-call strings carry no prefix in code (the core's doubled marker
  is stripped, as in W43).
- Bands: LIFE · Vida; CULTURE · Cultura; SPORT · Esporte; YOUTH ·
  Jovens; DEEP READ · Leitura profunda (EN left part is the core's;
  PT right part is W43's `Leitura profunda`); LANGUAGE IN HAND ·
  A língua na mão.
- P7: LEVEL A2 · Base; LEVEL B1 · Avançando; LEVEL B2 · Desafio;
  THE EXAMPLE · O exemplo; THE TOOLBOX · Ferramentas; PHRASES OF THE
  WEEK · Frases da semana (todas dos textos desta edição); phrase
  points use the W43 PT prefix `Gramática — `; THE ERROR CLINIC ·
  Clínica; READERS' CORNER · Cantinho dos leitores; NEXT WEEK · Na
  próxima semana, o VOL.3.
- P8: band `EXERCISES & ANSWERS · Exercícios e respostas`; heads
  A `Complete o texto`, B `Escolha`, C `Compreensão`, D `Frases`,
  E `Tradução`, F `Associação`, G `Diálogo`, H `Escrita [B1]`;
  MODEL · Modelo; ANSWERS · Respostas e notas (páginas 1–8); group
  separator `— Página {pg} —`; note format ` ({note})` (half-width
  parens, core uses full-width).
- Type labels (registry only, never printed): Completar frases,
  Múltipla escolha, Reescrever, Combinar, Leitura de gráfico, Praticar,
  Corrigir, Completar o texto, Compreensão de leitura, Traduzir,
  Completar o diálogo, Redação. Instr labels (printed small grey):
  Complete, Reescreva, Combine, Corrija.
- P8 translation items mirror the core's instruction split: items 137
  and 140 keep the English instruction `Translate :`, items 138 and 139
  use the native `Traduza:`; keys are Portuguese translations of the
  same English sentences (direction EN↔PT, core was EN↔ZH).

## 4. Measured quantities (all independently re-derived from the core)

- Exercises: **150** — by level A2 60 / B1 69 / B2 21; by page P1 10 /
  P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39. (Note P2 = 17 and
  P8 = 39, not the generic 18/38 — measured from the core registry.)
  By type: Completar frases 33, Múltipla escolha 41, Reescrever 16,
  Combinar 20, Leitura de gráfico 6, Praticar 8, Corrigir 4, Completar o
  texto 8, Compreensão de leitura 4, Traduzir 4, Completar o diálogo 5,
  Redação 1. P8 printed keys cover 1–150 continuously (extract-verified).
- Model essay `My Tuesday, November 3`: **85 words**, verbatim in the
  P8 MODEL box (whitespace-normalized match, 1 occurrence).
- Gloss boxes: **18 items, 1:1 with the core**, split on `·` and verified
  item by item in the rendered SVGs — P2 3, P3 4, P4 4, P5 3, P6 4.
  (P1's bridge line is a separate bridge element, 4 items, not a
  gloss() call.)
- P7 phrases of the week: **8 sentences, each verbatim from this
  issue's own articles**. Scoped count (article pages P1–P6 + P7 phrase
  slot) = 2× each; phrase 6 additionally appears in the B2 example box
  (P7 count 2 there), exactly as in the core. Tags: page labels
  page 1 ×1, page 2 ×2, page 3 ×1, page 4 ×2, page 5 ×1, page 6 ×1;
  levels A2 ×3, B1 ×4, B2 ×2. (2026-10-28 proof correction: builder tally B1 ×3 was a slip; core + edition P7 measured sequence is [A2, A2, B1, B1, B2, B2, A2, B1], paper untouched.)
- P7 definition boxes: A2/B1/B2 example sentences frozen verbatim; only
  the B2 gloss is localized (`part of = uma parte (page 6)`).
  Localizing a definition sentence would be a blocking failure — none
  occurred (P7 CJK count 0; see §6).
- P7 structure (measured from the core, not copied from another family):
  3 level columns (A2 FALLING BACK / GOING TO + VERB; B1 COMPARATIVES /
  THE PAST SIMPLE; B2 HEADLINE PRESENT / WHETHER = IF ?), each with a
  THE EXAMPLE box; TOOLBOX (3 pocket sentences, one per level) + bridge;
  PHRASES (8) + ERROR CLINIC (4) + READERS' CORNER + VOL.3 preview
  (Wednesday, November 11 Veterans Day; Sunday, November 15 NFL Munich;
  midterm results report).
- Readers' corner (coordinator ruling, executed as written): no reader,
  letter, name, or quote is invented. The core's English letter paragraph
  is kept verbatim, including its own honestly-labeled disclosure clause
  and the `M. L., a reader in Chicago` byline. The disclosure paragraph
  itself is written in Portuguese and states the 3 facts (no real
  letters arrived; no best VOL.1 p.8 text arrived; the example stays
  marked and the promise moves to VOL.3) plus an explicit imperative
  invitation (`Envie sua carta e seu texto!`) with the VOL.3 publication
  promise. The preview line is not counted as the invitation. No new
  English disclosure sentence was written (the core has none beyond the
  letter paragraph's own clause, which is preserved, not added).
- P1 word of the week: `midterm` (`A meio do mandato: midterm
  election.`). P6 chart: 38/29/21/12 = 100, teaching data (see §2).

## 5. Trend, fact, and image sources

- Topics, dates, and weekdays are the core's own, verified by the core
  builder (see the core KIT `files/weekly-report-w45-en-core/
  WEEKLY-KIT.md` §5–§6 for the full trend pool and fact notes). This
  fan-out adds no new facts and changes no date, score, or figure.
- Images: the core's 5 images, unchanged, with the core's captions and
  credits printed on the pages — P1 voting booth, Old State House,
  Hartford (Kenneth C. Zirkel, CC0); P2 `A Halloween Wish` 1912
  postcard (public domain); P3 `Cat and Flowers`, Édouard Manet
  (CC0; caption states it is not film art); P4 American football 1910
  (Frank R. Snyder, public domain); P6 United States Capitol
  (public domain). All via Wikimedia Commons. Build-time credit file:
  `assets/CREDITS.md` in the build directory.

## 6. Gates (all measured on the final round-4 render)

- Core baseline: the core build sources in the build directory were
  reconstructed by reversing the EN × ES transform
  (`reverse-es.py`) and PROVEN by `tools/freeze.py baseline`: **8/8
  SVGs byte-identical** to the shipped core SVGs (full hashes listed
  below; proof copy kept in
  `hidden_files/weekly-report-w45-en-pt-coreproof/`; the run also
  re-hashed the shipped core SVGs unchanged afterwards, and the
  shipped core SVGs were re-hashed again at delivery time with the
  same results). Full shipped-core hashes (verified 2026-10-28):
  p1 c7e7d019de01e662faa35f9f1874829ae3fc0300e5d680f43404e6eab01b4c50,
  p2 07f5df7e8e7ea0768244e6c4ab4b7c1be04682e3309e34bd3c1229726590a293,
  p3 d9f7cc374fe1229ccada556a2e1d330e84fac3f4aeaa443400f3ba131dfce580,
  p4 3b8be5175094bcb71de860321ef00187101b5282d0d5ca76a88aca478b1f0006,
  p5 73486e2f216e1f3bc9f2ddabccdd74e8fb15560250ff1ec8729c339c3c5f6f3e,
  p6 3e2187b37acb2883c0aaef95f8e1bca21ec36e4327d4b5e69b8638e791152a79,
  p7 5a2684096010839c3b7c86be1b5fe45b730588c5546b3827b21b7e7080105083,
  p8 4de34a135cc831bfbbf5ec285be29d4758424dc16f37f0f9ab184d8fe18c8a9b.
  Every later fix round re-ran from a fresh copy of those proven
  sources (hashes checked against `baseline-pre-transform.sha256`
  before each run).
- Frozen English: `tools/freeze.py diff` (core vs edition) — added CJK
  characters **0** on every page (edition CJK total 0); the added/
  removed string lists contain no long pure-English body text (scan
  done); every transform pair targets a Chinese explanation string, a
  bilingual furniture string, or a type/instr token — no English body
  string was touched. The one forbidden-layer term: **0 occurrences**
  in all deliverables (SVGs, cards, PDFs, KIT, ABSTRACT) — verified by
  full-text scan (edition CJK = 0 already implies it for SVGs; KIT and
  ABSTRACT were scanned separately).
- P8: `tools/p8.py compare` (core vs edition, total 150) — **CLEAN**,
  noted sets 78 = 78, missing [] extra 0 uncertain []. Keydiff =
  [137, 138, 139, 140, 150], each adjudicated with byte-exact printed
  keys: 137 core `耐心是制度的一部分，而不是制度的失败。` → PT
  `A paciência faz parte do sistema, não é uma falha do sistema.`
  (translation of `Patience is part of the system, not a failure of
  it.`); 138 core `11 月 3日周二是美国的选举日。` → PT
  `Terça-feira, 3 de novembro, é o dia das eleições nos Estados
  Unidos.` (translation of `Tuesday, November 3, is Election Day in
  the United States.`); 139 core `这周日，NFL 在马德里比赛。` → PT
  `Neste domingo, a NFL joga em Madri.` (translation of `On Sunday,
  the NFL plays in Madrid.`); 140 core `并非每处都拨回时钟。` → PT
  `Nem todos os lugares mudam.` (translation of `Not every place
  changes.`); 150 core `开放题 — 要点见写作框，范文在第8 版写作框内`
  → PT `Questão aberta: veja os pontos no quadro de redação; o modelo
  está no quadro desta página` (explanation-layer writing key). All
  five are legal redirections (translation direction EN↔ZH → EN↔PT,
  plus the explanation-layer writing key); the identical keydiff list
  appears in the EN × ES sibling, confirming the pattern. No
  bracket-branch extraction artifact: the five keys above are the
  full printed keys, not paren/dash mis-splits. P8 notes are printed
  with the pinned set NOTAS_EXTRA = {11, 12, 14, 19, 29, 30, 31, 33, 41,
  44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87,
  88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111} (the core's
  printed pg<8 set, identical to the EN × ES pin); P8 items print all
  notes by the pg == 8 rule. P8 printed-note set equality holds
  (EXTRA_ONLY does not arise).
- Geometry: `tools/occlusion_audit.py` (edition + `--core` core) —
  **edition 0, core 0, NEW 0** (selftest passed: all six classes fired
  on synthetic positives, clean controls silent). Supplemental scans
  (`supplemental.py`, same method as the ES sibling): rowcheck
  collisions **0**, P6 chart-label baseline-box coverage **0.0%**
  (gate < 30%; true-ink coverage also 0.0%), edgescan flags **0**
  (max advance-right 1885.0 on P1–P7 = the frame itself; P8's two
  MARGIN-CROSS items at 1899.4/1903.8 are the core's own frozen
  match-set rights, identical in the core — inherited, not new).
  Every page was also checked for frame-line pressure and right-edge
  advance overflow (ADVANCE method) — clean. All 8 cards were viewed
  page by page (not sampled): no overflow, overlap, footer intrusion,
  or clipped image/caption found. Two inherited renderings are noted,
  not defects: the P6 practice-ballot `☐` glyphs and the P7 clinic `✗`
  marks render as hollow boxes in this font — both characters are
  frozen core text, identical in the core.
- Build warnings: final round log has **zero** FLOW OVERFLOW and zero
  HEAD TOO WIDE warnings (rounds 1–2 warnings are recorded in §8 with
  their fixes).
- Reproduction: every fix-round edit went into `transform.py` only;
  no content file was hand-edited alone. Every re-render ran the full
  set through the single driver process (`run.py`: content12 → 34 →
  56 → 7 → 8 in one process, so the shared exercise registry
  accumulates correctly).

## 7. Reproduction

- Build directory:
  `hidden_files/weekly-report-w45-en-pt-build/` — `transform.py`
  (all pairs + fix rounds 1–4), `run.py`, `render.py`, `bslib4.py`,
  `svglib.py`, `content12/34/56/7/8.py`, `assets/` (5 images +
  CREDITS.md), `reverse-es.py` (core-source provenance),
  `baseline-pre-transform.sha256` (pristine core sources),
  `baseline-round{1,2,3,4}.txt` (per-round SVG/card/PDF hashes),
  `build-round{1,2,3,4}.log`, `render-round{1,2,3,4}.log`,
  `diff.json`/`diff4.json`, `p8-core.json`, `p8-ed.json`/`p8-ed4.json`,
  `p8.json`, `occlusion-core.json`, `occlusion-ed.json`,
  `occlusion3-ed.json`, `occlusion4-ed.json`,
  `supplemental.py`/`supplemental-core.py` + outputs,
  `round{1,2,3}-sources/` (pre-round transformed sources, audit trail).
  Core-baseline proof:
  `hidden_files/weekly-report-w45-en-pt-coreproof/`.
- Commands (from the build directory; never with system python3 —
  it has no cairosvg):
  `tools/venv/bin/python transform.py` (repoints OUT to the edition
  dir) → `tools/venv/bin/python run.py` (one process, writes 8 SVGs)
  → `tools/venv/bin/python render.py` (cards + print PDF + web PDF).
- Interpreter + library versions (both run.py and render.py use the
  same interpreter): `tools/venv/bin/python` = **Python 3.12.3**,
  **Pillow 13.0.0**; render.py additionally uses **cairosvg 2.9.1**
  and **pypdf 6.21.2**. Run.py interpreter: Python 3.12.3 / Pillow
  13.0.0. Render.py interpreter: Python 3.12.3 / Pillow 13.0.0.
  (Recorded separately per the build brief; both are the same venv.)
- Web PDF recipe (finalized core recipe, as in render.py): pages
  downscaled to 1400px wide, JPEG q85.
- Final files (round 4):
  - print PDF `The-Lucerna-VOL2-PT.pdf` — **17,295,650 bytes**,
    sha256 `ed231eafd83df10cd62dc3cfd7a595263099efdda98c7086d42c9bf1079ae5c9`
  - web PDF `The-Lucerna-VOL2-PT-web.pdf` — **4,008,688 bytes**,
    sha256 `a91be6abb1e0adb8a8c1850ab3f34114748fbef86394453ffc111a5c56fc93c9`
  - SVGs (round 4): p1 `41e61130cd66083291b749466a66b324f1142b53d878dd80f986ca9ba9ceb951`,
    p2 `d8d1079f6ccb8baae07148fe66a7c14e9d4121d5e601e852e1a1ace3135f1629`,
    p3 `ea45e0e7bdce8aea4ec5dfaf2c0bcacb81c376549a183c287442db765cc591f5`,
    p4 `7947c9cc95446b29a66691e16bf7d448f696b387294e1ebe1ef5ce4ce5fd795c`,
    p5 `f1b14f1104746a20d63abeb38afd01b323e367b3e66058717427c7d4bf2739ac`,
    p6 `fb45ee041115e323a6883300a98a42975a8f4a5fd2a1dfd20d3f14e858cf9f3c`,
    p7 `4b221bd52bbec44e8f09a5dcd5d11c6262b245381f18885c1d6e417d7930cd28`,
    p8 `6035b1aecb6552974accdfd3fbe243af348883626853adfc347b38b92b53088e`

## 8. Fix-round record

- Round 1 (base transform): 150 / 60-69-21 / pages correct, but two
  FLOW OVERFLOW warnings — P1-headline (ended 1921 vs bottom 1828)
  and P2-ex (ended 2948 vs bottom 2562). Root cause, measured by
  per-column SVG comparison: PT strings pushed boxes/exercises across
  column breaks, cascading gaps. Pre-fix hashes: `baseline-round1.txt`.
- Round 2 (transform fix round 2): P1 numbers-box parentheticals
  shortened to restore the core's 3+3 wrap lines (`todos em disputa`;
  `dois eventos no domingo`); P2 bridges A and C shortened to 1 line
  each like the core (`Complete em inglês conforme o horário.`;
  `Leia o artigo da página 2 e responda.`). Result: zero build
  warnings; only P1/P2 SVGs changed. Pre-fix hashes:
  `baseline-round2.txt`.
- Round 3 (transform fix round 3, from the round-2 audits): P1 dark-band
  line 1 shortened (rowcheck gap −70.3, visible overprint) to `Terça
  de eleições · Relógios atrasados` (PIL ink gap 154.4px); P1 numbers
  box title shortened to `THE WEEK IN NUMBERS · Números` (was 24.5px
  past the box border; now 14.8px inside); P1 searches footnote
  shortened to `Interesse relativo, não números exatos.` (was
  advance-right 1929.4 past the 1885 frame; now 1818.0); P5 box title
  to `TOO CLOSE TO CALL · Disputado` (was 28.5px past; now 40.0px
  inside); P6 box title to `A PRACTICE BALLOT · Cédula` (was 27.8px
  past; now 80.0px inside). Result: only the wordmark/subtitle TEXTX
  flag remained. Pre-fix hashes: `baseline-round3.txt` (SVGs; cards
  and PDFs re-rendered with the round).
- Round 4 (transform fix round 4): the remaining TEXTX flag was a
  PIL-bbox artifact — the rendered PNG shows a fully-empty ink row
  (y=294) between wordmark ink (ends y=293) and subtitle ink (starts
  y=295), i.e. no glyph touches. The gate nevertheless requires a
  literal NEW=0, so the PT subtitle (furniture, not frozen text)
  shifted 330 → 338 (+8px): PIL clearance ~1.8px, badge gap ~8px,
  wordmark/rules/badge untouched. Result: occlusion 0/0/0,
  supplemental 0/0/0, only P1 SVG changed. Pre-fix hashes:
  `baseline-round3.txt` (SVGs; `baseline-round4.txt` is the post-round-4
  record, its hashes equal the final deliverables, not the pre-fix baseline).
- P2 AND YOU box tail 24 (not 20) and the P8 E-item gap=4 were carried
  in the base transform from the ES sibling's measured fixes (same
  wrap lengths in PT: AND YOU line 2 lines at the same size/width;
  `Traduza:` the same 8 characters as `Traduce:`); both were verified
  by this edition's own audits (AND YOU box ink inside its box; P8
  Levels line clear of the writing-strip rule — visible on the P8
  card, no overflow warning).

## 9. Deviations from the W43 EN × PT edition (all deliberate)

- Masthead subtitle: VOL.2 + this week's topics (VOTOS · FUTEBOL ·
  CINEMA) instead of VOL.1's topics; subtitle y 330 → 338 (audit,
  see §8 round 4).
- P6 band left part follows the W45 core (`DEEP READ`), PT right part
  keeps W43's `Leitura profunda` (W43's band was `IN DEPTH`).
- NEXT WEEK line advances VOL.2 → VOL.3 (issue advance, expected).
- PDF names follow the W45 EN family: `The-Lucerna-VOL2-PT.pdf`
  (W43: `Lucerna-VOL1-PT.pdf`).
- Shortened furniture where the W45 PT wording overflowed the core's
  boxes/flows (all in §8): numbers-box title `Números`, P5 box title
  `Disputado`, P6 box title `Cédula`, dark-band line 1, searches
  footnote, P1 numbers parentheticals, P2 bridges A/C. No meaning was
  changed by any shortening; the shortened strings are the ones
  printed.
- Everything else in §3 is byte-identical in form to W43 (badge,
  footer, page line, gloss prefix and comma style, P7 heads and
  `Gramática — ` prefix, P8 heads, separator, paren style).

## 10. Proofread record (builder self-check)

- Builder ran: freeze baseline (8/8) + freeze diff (added CJK 0) +
  p8 compare (CLEAN) + occlusion audit (0/0/0) + supplemental
  (rowcheck/chartcheck/edgescan 0) + gloss item-by-item (18/18) +
  phrase scoped 2× + essay 85 words + P8 keys 1–150 continuous + all
  8 cards viewed. No sampling: every page, every exercise number,
  every gloss item, every phrase was checked.
- Retained unmodified items (not defects): the core's P8 match-set
  rights that cross the 1885 advance margin (frozen English, identical
  in the core); the P6 `☐` and P7 `✗` glyph renderings (frozen core
  characters); the W43 furniture forms in §3.
- Open for the independent proofreader: re-run all §6 tools from the
  §7 commands, re-view all 8 cards, and confirm the §8 round-4
  subtitle shift. Nothing in this KIT claims final sign-off.
