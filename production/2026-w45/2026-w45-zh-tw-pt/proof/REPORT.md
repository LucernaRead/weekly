# INDEPENDENT PROOFREAD — W45 ZH-TW × PT (Traditional Chinese target · Portuguese reader)

**Verdict: NOT PASS** — one blocking item (Gate 6: P8-note term form vs the W43 zh-tw-pt
column precedent). Everything else across all 16 gates passes. Nothing is declared
shipped; no repo insert, Discord post, main-chat dump, cron, or shared-scratch
cleanup was done by this proof. The edition was not modified (delivery/build mtimes
verified unchanged after all proof work, snap2 vs snap3 identical).

- Edition: `files/weekly-report-w45-zh-tw-pt/` (svg ×8, cards ×8 1950×2700, print + web PDFs)
- Core: `files/weekly-report-w45-zhtw-core/` (KIT read first; its counts are authoritative)
- W43 same-pairing reference: `files/weekly-report-zh-tw-pt/`
- Build: `hidden_files/weekly-report-w45-zh-tw-pt-build/`; transform:
  `hidden_files/weekly-report-w45-zh-tw-pt-transform.py` (279 pairs, verified by AST:
  BSLIB 3, C12 52, C34 60, C56 62, C7 49, C8 53)
- Proof work: this dir (`REPORT.md` + `work/`). All proof renders ran in fresh copies
  under `work/` — never inside the core build dir, never writing to delivery/build dirs.

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker/process writing to delivery/build dirs (`ps` clean at start and end).
- (b) Two mtime snapshots of both dirs a few minutes apart: ZERO changes (snap1 = snap2).
- (c) Builder session completed (last delivery write 09:11, proof started after; no
  further writes during proof except none at all — final snap3 = snap2).
- Result: PROCEED. (Note: the task text names a transform path inside the build dir;
  the actual transform lives at `hidden_files/weekly-report-w45-zh-tw-pt-transform.py`,
  and the build dir holds the applied `content*.py`/`bslib4.py`/`svglib.py`/`render.py`/
  `run.py` set. The Gate 10 replay used the transform file itself.)

## Per-gate evidence

### 1. Freeze baseline + freeze diff — PASS
- `tools/freeze.py baseline` against the W45 zh-tw core build: **8/8 byte-identical**,
  core shipped SVGs re-hashed unchanged afterwards.
- `tools/freeze.py diff --strict-cjk`: per-page +/− strings 25/22, 38/35, 43/38, 36/33,
  44/40, 42/37, 95/87, 195/187 (identical to builder KIT §4); **strict-CJK added = 0
  on all 8 pages**; driver exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE / TOO WIDE
  warnings (final driver log: P7 col3 ends 1745.36, P7 teaser ends 2543.36, P8 keys
  end y=2314, bottom 2540).

### 2. Traditional independence — PASS (re-extracted, not trusted)
- Own extraction from shipped SVG text nodes: core 773 chars, W43 zh-tw-pt 791,
  union 1031, edition 772, **outside union: NONE**; edition set is a subset of the
  core's own set (edition-not-in-core: none). Absolute counts differ from the
  builder's (782/798/1040/780) by extraction method; judged by outside = 0 as
  instructed, the gate passes under either method.
- Simplified-only spot list (邮 说 国 龙 马 发 让 认 议 论 贝 财 见 车 红 灯 无 为 乌 鸟 东 丝)
  over all edition text nodes: **0 hits**.
- Transform scan: no OpenCC, no s2t/t2s, no mapping table, no conversion logic of any
  kind (only the svglib `_fw` pair-conversion bypass, which is typographic, not
  script conversion); no Simplified-spot character anywhere in the transform file.

### 3. Target text zero difference — PASS
- Freeze strict-CJK added = 0 (Gate 1) plus a full per-string diff read: every added
  string is Portuguese explanation, a bilingual head whose Chinese half is frozen
  target text, or a P8 key line whose key is frozen target text. No new target
  sentence anywhere.

### 4. Gate 10 reproduction — PASS
- My own replay of the builder's transform `--gate10` (fresh core copy + transform
  ALONE, one-process driver): **8/8 byte-identical, warnings = 0, exit 0**,
  registry 150. Separately, my own repointed re-render of the edition build dir
  also reproduced all 8 delivered SVGs byte-identically.
- No stray nested tree: precise search for a `.../home/...` path under delivery/build
  dirs before and after the replay: empty. The builder's disclosed repoint bug
  (whole-`expanduser(...)` replacement in the transform) is present and correct in
  the transform source; the final replay wrote only to the builder's gate10 temp
  dir and the delivered SVGs. (That gate10 temp dir still exists after the run
  despite the KIT's "removed after each run" wording — a housekeeping imprecision,
  not a delivery defect; see Non-blocking.)

### 5. p8.py — PASS
- Explicit-path invocation (tables.json's default P8 filename does not apply here;
  this core's file is `p8-test.svg`):
  `p8.py compare --core-p8 ../files/weekly-report-w45-zhtw-core/svg/p8-test.svg
  --edition-p8 ../files/weekly-report-w45-zh-tw-pt/svg/p8-test.svg --total 150`
  → **CLEAN, core 150 noted = edition 150 noted, missing=[], extra_count=0,
  uncertain=[], keydiff=[]** (printed keys; #150 prints as `✓` in both).
- Registry-dump diff (my own one-process dumps of fresh core and edition copies):
  page/level/type diffs = []; **key diff exactly #150** —
  core `(開放題,範文如下)` → PT `(pergunta aberta — modelo abaixo)`; all 150 notes
  translated (0 identical to core); 0 English-word suspects in PT notes.

### 6. P8 paren style + AI-variant trap — NOT PASS (blocking; see Blocking list)
What passes inside this gate:
- Paren style verified from the W43 zh-tw-pt shipped build code itself, line 118:
  `f"{e_['n']}. {e_['key']} ({e_['note']})"` — the edition uses exactly this form.
- Core font/lh/gap kept: core and edition content8.py both run the keys flow at
  12.8 / lh 1.12 / gap 1, Flow 1328–2540.
- Separators `— Página {pg} —` (not the zh-cn-pt dash style) on all 8 key pages.
- Printed P8 **answer block contains NO full-width parentheses** (wrap-aware
  reassembly of all 150 key items: 0 items with （/）). The full-width parens that
  exist on the P8 page are the frozen test questions themselves (section A stems,
  D passage, E dialogues), byte-identical to the core — not the answer block.
- AI-variant trap, language part: the P6 gloss is independently translated
  Portuguese in the final render (`Nota — Três sinais de mais: Finanças+
  (finanças mais tecnologia), IA+ ...`), and the separate content8 note is
  independently translated Portuguese (`138. 人工智慧 (IA dentro das finanças é
  人工智慧＋.)`). Both forms verified on the card/SVG. Strict-CJK added stays 0.
What fails: the **term form** inside P8 notes (blocking item B-1 below).

### 7. Occlusion audit — PASS
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fired, clean controls
  silent). Edition **0 flags**; core 0 flags; **NEW vs core: 0**.
- Same-baseline ink-collision scan (my own PIL true-ink, any-overlap criterion over
  all pages, plus the tool's TEXTX class): 0.
- P4/P6 chart-label element check (text ink vs later-drawn rects, any overlap):
  **0 on both chart pages**, core and edition.
- P4 bars: brick widths 120.0 ×1, 600.0 ×1 (= 1 and 5 runs). P6 bars: olive widths
  600.0 ×1, 800.0 ×3 (= 6, 8, 8, 8 hours). Identical to core.

### 8. Gloss / match counts — PASS
- `gloss()` calls: core 4 + 5 + 3 = 12; edition 4 + 5 + 3 = 12; rendered
  `Nota — ` prefix nodes 12 = 12 (core `Notes` nodes 12).
- Registry 150: A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38;
  types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1 — all exactly the
  zh-tw core's counts (not zh-cn's). Writing model verbatim: edition model text
  byte-identical to core's, 138 characters (band 120–180).

### 9. P7 golden sentences — PASS
- All 8 strip sentences verbatim from this issue's own articles, each exactly **2×
  issue-wide** (article page + P7) in both core and edition, tags
  **p. 1, 1, 2, 3, 3, 4, 5, 6** (article pages P1, P1, P2, P3, P3, P4, P5, P6).
  (Naive space-joined counting undercounts wrapped sentences; wrap-safe
  concatenation counting was used.) Not the zh-tw-de S. form; tags are the
  `p.` form as claimed.

### 10. Images — PASS
- Per-page embedded payloads + geometry byte-identical to the zh-tw core:
  P1 `ac4dfe2ad3a4…` (1451,640,434×300), P2 `a40e7a2b265b…`, P4 `18ad8ae06fac…`,
  P5 `bcbada13a5ae…`; P3/P6/P7/P8 no photos — all as core.
- Printed credits verbatim: P1 `Photo: Wilfredor — CC0 (Wikimedia Commons)`,
  P2 `Photo: CorraleH — CC0 (Wikimedia Commons)`,
  P4 `Photo: Bain News Service — Public domain (Wikimedia Commons)`,
  P5 `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)`.
- P4 provenance: placed bytes and credit line unchanged from the core, so per the
  core KIT's binding 2026-10-27 coordinator adjudication (CLOSED), provenance is
  NOT re-flagged. No live Commons re-query was treated as evidence either way.

### 11. Readers' corner — PASS (including the judgment item)
- Frozen Traditional disclosure line-for-line identical to the core (wrapped lines
  [145–149] = core [138–142], byte-identical, 21.5pt).
- Portuguese disclosure present, 6 lines, stating no genuine letters arrived
  (`até o fechamento nenhuma publicável chegou`) and ending with the open
  invitation exactly as cited: `...por isso o exemplo fica e o convite continua
  aberto.` The W43 zh-tw-pt precedent wording differs legitimately: W43 was the
  promissory volume (`O VOL.2 vai publicar cartas reais...`); W45 is the deferral
  volume, and its PT disclosure faithfully renders the core's deferral disclosure
  (`the invitation stays open`), as the core's own English text does.
- Gap fix (KIT §9 judgment item): VERIFIED, not merely accepted. The only
  geometry change in content7.py vs core is the two `+ 10` → `+ 0` inter-para gaps
  (letter para, disclosure para); the readers box rect is byte-identical
  (x=1451 y=1184.86 w=434 h=560.5). Measured: edition PT last-line baseline
  1731.63, ink bottom 1736.13, i.e. ~9.2px clear of the 1745.36 box bottom.
  Card-crop visual: edition last line fully inside the box with clear space below;
  core crop confirms the diagnosis — the core's own last line (`invitation stays
  open.`, baseline 1751.63) is struck through by the border. The fix is
  interior-only and correct. P7 col3/teaser positions unmoved (1745.36 / 2543.36).

### 12. Furniture three-way — PASS (measured, not assumed)
- P1 badge slot on all three P1s: **x=975 y=378, 21pt, weight 700, centred
  (text-anchor=middle)**: core fill `#3e4c2a` (OLIVE), W43 zh-tw-pt fill `#a4553a`
  (BRICK), this edition fill `#a4553a` (BRICK). Badge ink measured 1274.25px at
  21pt bold TC (builder's 1274.4 within rounding), centred 337.9–1612.1.
- Badge TEXT: edition byte-identical to the W43 zh-tw-pt shipped SVG (and to the
  tables.json PT string — shipped W43 wins, and they agree):
  `TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS
  LEITORES DE LÍNGUA PORTUGUESA`. tables.json was not edited (not checked for
  edits beyond reading; no furniture string in the edition contradicts it).
- Footer on all 8 pages, VOL.2-adapted Portuguese form:
  `Lucerna · SEMANÁRIO CHINÊS TRADICIONAL VOL.2 · TEXTOS EM CHINÊS TRADICIONAL ·
  EXPLICAÇÕES EM PORTUGUÊS`; page lines `Página {n} de 8`; gloss prefix
  `Nota — `; P8 separators `— Página {pg} —`.

### 13. Residual Latin (rendered-output sweep) — PASS
- Bilingual-node scan of ALL text nodes + English-blacklist scan of ALL nodes,
  re-run independently (not just added strings).
- P3 catch HOLDS on the card: `算一算 · Faça as contas`; `Work it out` occurs
  **0 times** anywhere in the edition.
- Adjudicated residues, each verified (not copied): `fintech`/`FinTech` = the
  Portuguese-press loanword and event name (`Semana FinTech`), plus the official
  theme name `Fintech Nexus: Bridging the World, Building the Future` frozen
  inside a Chinese target sentence; `Photo:` = frozen Commons credits (4);
  `some`/`Some` = the Portuguese verb somar (`some esse custo`, `Some as taxas`);
  `SOLID TIDES` = the forum's English name inside a frozen Chinese stem;
  `JUMP` = the show title (frozen + PT gloss uses the same title); `MVP` = sports
  abbreviation used in Portuguese prose too; `ITF` = the fair's acronym, defined
  in the PT gloss; `VOL.2` = volume marker; `Complete` = the PT instruction word
  (W43 zh-tw-pt KIT §5 precedent). No English explanation prose remains.

### 14. Web regen — PASS
- Regen from the delivered SVGs in proof scratch: cards **8/8 byte-identical**;
  print PDF **byte-identical** (20,848,230 B, same SHA); web PDF same size
  (3,507,192 B) and content-identical, differing ONLY in `CreationDate`/`ModDate`
  timestamp bytes (regen `D:20261028092024Z` vs delivered `D:20261028091013Z`) —
  stated explicitly as the sole difference.

### 15. Eyeball all 8 cards — PASS
- All 8 cards viewed full-page: layout clean, no overflow, overlap, footer
  collision, or missing content on any page. P4 chart + photo/caption/credit fully
  visible; P6 chart labels clear of bars; P7 readers box as in Gate 11; P8 keys
  block ends well above the footer.

### 16. ABSTRACT.txt — PASS
- Portuguese single line (one trailing newline), **no ASCII double quotes**.
  Names the paper (Lucerna), target language (chinês tradicional), explanation
  language (português), A2–B2, 150 exercícios, plus a learner search phrase
  (`aprenda chinês tradicional lendo as notícias da semana`).
- Every named topic cross-checked against the zh-tw core's actual content:
  Semana FinTech de Hong Kong ✓, Feira Internacional de Viagens de Taipé ✓,
  Dragons campeões da Série de Taiwan ✓, Lidong e o Início do Inverno ✓,
  Festival de Escultura em Aço de Kaohsiung ✓, Halloween de Tianmu ✓.
  No topic outside the core.

## Blocking list (1 item)

### B-1 — P8 notes cite Chinese terms in Han characters (32/150), breaking the
W43 zh-tw-pt column's pinyin discipline — Gate 6
- **Column precedent (this column's own shipped artifact, not a sibling rule):**
  wrap-aware reassembly of all 150 key notes in the shipped W43 zh-tw-pt P8
  (`files/weekly-report-zh-tw-pt/svg/p8-test.svg`) → **0 notes contain any Han
  character**; Chinese terms cited in notes are tone-marked pinyin (e.g. W43
  content8.py: `As fêmeas (xiè nǎ) estão no auge no 9.º mês lunar.`,
  `Gaste 1.000, receba 100: mǎn qiān sòng bǎi.`). This is documented as a
  verified property of that column's zero-problem pass (W43 KIT §7 "Pinyin
  discipline"; W43 proof §13: "parenthesis groups containing Han = 0",
  "all 150 notes rewritten, none contains a CJK character"). The zh-tw-it
  pinyin-only rule and the zh-tw-es verbatim rule were NOT imported; the
  adjudication rests on W43 zh-tw-pt alone, and it says pinyin.
- **This edition:** the same wrap-aware reassembly of the shipped W45 P8
  (`files/weekly-report-w45-zh-tw-pt/svg/p8-test.svg`) → **32 notes contain Han
  characters**. Items: 17, 25, 26, 27, 28, 35, 43, 44, 45, 46, 55, 61, 62, 63, 64,
  79, 80, 81, 82, 101, 103, 105, 106, 109, 110, 111, 112, 132, 133, 134, 138, 149.
  Examples (printed P8): `17. 進補 (Uma refeição de panela quente marca o Lidong:
  進補.)`; `35. 節氣 (Lidong é um termo solar (節氣).)`;
  `138. 人工智慧 (IA dentro das finanças é 人工智慧＋.)`;
  `149. A (Compare os preços primeiro e pague depois: 先比價，再結帳.)`.
  Source: `hidden_files/weekly-report-w45-zh-tw-pt-build/content8.py`, e.g. line 69:
  `f.ex("B2", "完成句子", "人工智慧", "IA dentro das finanças é 人工智慧＋.", ...)`.
  The builder's KIT never discloses this as a deviation from W43 zh-tw-pt; the
  `_fw` bypass (§6) exists only because the notes cite Han — in W43 zh-tw-pt no
  bypass was needed, because pinyin notes never trigger pair conversion.
- **Why blocking, not cosmetic:** the answer-key apparatus is the part readers
  use to learn, and the column changed its note language silently between VOL.1
  and VOL.2 (32 items, systematic, not one slip). The typographic half of the
  gate passes (parens stay half-width), but the term-form half fails against the
  column's own shipped precedent. A series convention break of this size is a
  proof problem, not a preference: had the same reassembly check been run as in
  the W43 proof, it would have failed there too.
- **Remedy (concrete):** in the transform's C8 pairs (and any other file whose PT
  notes cite Han — the 32 items above are all P8 notes, so C8), convert every Han
  citation inside PT note prose to tone-marked pinyin following W43 zh-tw-pt
  (e.g. 進補 → jìnbǔ, 立冬 → lìdōng, 封王 → fēng wáng, 完封 → wánfēng,
  節氣 → jiéqì, 人工智慧＋ → réngōng zhìnéng＋ with the ＋ form as the
  coordinator adjudicates, 先比價，再結帳 → xiān bǐjià, zài jiézhàng).
  Keys themselves (frozen Traditional target text before the parenthesis) MUST NOT
  change. The `_fw` bypass may then be removed (pinyin notes cannot trigger pair
  conversion) or retained — either way the reproof must verify answer-block
  full-width parens stay 0. Then re-run freeze diff (`--strict-cjk` must stay 0;
  removing Han from notes only lowers the edition CJK count further), `p8.py
  compare`, Gate 10, and occlusion, and submit the edition for a FULL reproof
  (this verdict's reproof must re-verify the complete note set, since P8 text
  changes).

## Non-blocking observations (separate from the verdict)
- N-1. Builder KIT §6 wording "the printed P8 contains NO full-width parentheses"
  is true only for the answer block; the P8 page as a whole contains full-width
  parens in the frozen test questions, byte-identical to the core. Scoping
  imprecision in the KIT, not an edition defect.
- N-2. CJK absolute counts differ by extraction method (mine: core 773 / W43 791 /
  union 1031 / edition 772; builder's: 782 / 798 / 1040 / 780). Outside-union = 0
  under both methods; no action needed.
- N-3. The builder's gate10 temp dir (`hidden_files/w45-zh-tw-pt-gate10/`) still
  exists after the final run despite the KIT's "removed after each run" wording.
  It is outside delivery/build dirs and my replay overwrote it cleanly; no
  delivery impact. Housekeeping only.
- N-4. Badge ink measured 1274.25px vs builder's 1274.4px — supersampling rounding
  only; slot, size, weight, anchor, fill, and text all confirmed.

## Limitations (stated honestly)
- Portuguese was checked by full reading of every rendered string, not by a native
  speaker; no Portuguese grammar claim beyond that reading is made.
- Commons Artist fields were NOT re-queried live in this proof (credits verified
  byte-identical to the core KIT's recorded Artist-field values; P4 provenance
  rests on the binding coordinator adjudication, not a fresh fetch).
- No live web source was consulted for facts; all topic/date claims were checked
  against the zh-tw core KIT and the frozen target text, which this fan-out must
  not alter.

## PDF pins re-verified (coordinator pins confirmed)
- Print `Lucerna-VOL2-PT.pdf`: **20,848,230 bytes**,
  SHA-256 `18f7ca8ff040042c6671bf83a8aef14bca829413f4b2be03a31a38323ceb0408`
- Web `Lucerna-VOL2-PT-web.pdf`: **3,507,192 bytes (< 10 MB)**,
  SHA-256 `ca73db6b10a909614d59ca3788f7eeca62d72e2a46be2820d623d8a9d42e3907`
- SVG SHA-256 (final, re-verified): p1 `3d8481de…b10a94`, p2 `99bcb003…676b97c2`,
  p3 `aac1e5fc…fd7cdf9`, p4 `cbf88009…c2f9ab6`, p5 `23b7ad0b…8e2731d`,
  p6 `2012bf23…0943184e`, p7 `32799b27…a19c56fd`, p8 `efdec8a2…7f20e89f5`
  (full hashes match builder KIT §11 exactly; see work logs).
