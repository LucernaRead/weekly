# INDEPENDENT PROOFREAD — W45 ZH-TW × IT (Traditional Chinese target · Italian reader)

## VERDICT: PASS with ZERO PROBLEMS

Full round from scratch, all 16 brief gates plus the coordinator's additional
P3 check pass. This report is the finalization evidence. (This proof does NOT
itself declare anything shipped or insert anything — insertion is the
coordinator's step.)

- Edition: `2026-w45-zh-tw-it`, issue week Nov 2–8, 2026 (VOL.2)
- Delivery dir: `files/weekly-report-w45-zh-tw-it/` (svg×8, cards×8, 2 PDFs,
  WEEKLY-KIT.md, ABSTRACT.txt)
- Proof work: `hidden_files/w45/zh-tw-it-proof/work/` (extractions, freeze
  outputs, Gate-10 repro, registry dumps, occlusion JSONs, scans, regen)
- Proof date: 2026-10-28. Builder KIT, zh-tw core KIT, SOP, and tools/README
  were read before starting.

## Pre-flight duplicate check (coordinator ruling: NO CONCURRENT WRITER)

- (a) At start, two live `render.py` processes existed — but both belonged to
  SIBLING builds (cwd `weekly-report-w45-zh-tw-ru-build` and
  `weekly-report-w45-zh-tw-nl-build`), verified via /proc cwd + open fds.
  No process had this edition's delivery or build dir open, and no process
  was writing to them. By the second snapshot no python run/render/transform
  processes remained at all.
- (b) Two mtime snapshots of BOTH dirs (09:07:59 UTC → 09:11:30 UTC):
  ZERO changes (diff empty).
- (c) Builder session completed: delivery mtimes 08:56–09:01 UTC, KIT complete
  through Gate 10, no builder process running.
- Pre-flight PASSED; proof proceeded. No subagent was spawned. `weekly-git`,
  `insert.py`, Discord, main-chat delivery, and cron jobs were not touched.
  No content module was ever imported inside the core build dir — all
  re-runs used fresh copies under this proof dir.

## Per-gate evidence

### 1. Freeze baseline + strict-CJK diff
- `freeze.py baseline` on the zh-tw core build: **8/8 byte-identical**
  (p1 `4672c972763b0eaf` … p8 `e6e97d02595aef3b`), core SVGs re-hashed
  unchanged afterwards.
- `freeze.py diff --strict-cjk` core → edition: **added CJK = 0 on all 8
  pages** (exit 0). Per-page CJK counts match the builder's KIT exactly:
  p1 952→920, p2 1018→996, p3 1088→1065, p4 831→809, p5 1101→1079,
  p6 942→921, p7 808→786, p8 1114→1018.
- Round-3 rewording verified: core P7 `Memory trick: learn 封王 first, then
  the way it was won （完封）…` → edition `Trucco di memoria: impara prima
  封王 e poi il modo in cui è stato vinto （完封）, …` (same baseline
  y=1355.27). The comma directly after 封王 became Italian `e`; no
  full-width ， appears; meaning is preserved, not lost.

### 2. Traditional independence — HARD GATE (re-extracted, not trusted)
- CJK sets extracted from the shipped SVGs themselves: edition distinct
  766 (Han ranges); union of (W45 zh-tw core + W43 zh-tw-it) distinct 1024.
  **Edition characters outside the union: NONE (empty set)** — under the
  narrow Han definition, under freeze.py's regex (780 vs 1040), and under
  narrow+U+3000 block (772 vs 1030): outside = [] in all three.
- Count reconciliation (non-blocking, see §Observations): the builder's 772
  is exactly narrow 766 + the 6 U+3000–303F punctuation marks present
  (、 。 《 》 「 」). The union count reconciles to 1030 vs the builder's
  1031 — a 1-character definitional residue; the gate (outside = []) is
  unaffected.
- Simplified-only spot list (邮 说 国 龙 马 发 对 让 为 这 听 车 门 电 话
  认 识 语 学 习） over ALL edition text nodes: **ZERO hits**.
- Transform inspection: `transform.py` is line/literal replacement with
  asserted occurrence counts only. Grep for opencc/s2t/t2s/mapping/
  conversion logic: no hits (the single "converted" mention is a comment
  about svglib `_fw()` full-width conversion, the round-3 defect class).
  NO conversion/OpenCC/own mapping table was used.

### 3. Target text ZERO difference (run level)
- Pure-CJK text-node multisets core vs edition: identical on P1–P6 except
  the single furniture page line (`第 n 版 / 共 8 版` → `Pagina n di 8`).
  P7/P8 pure-node differences are line-break redistribution only (see below).
- CJK character-SEQUENCE diff (document order, all pages): P1–P7 diff blocks
  are ONLY deletions of the old badge/footer/page-line furniture strings
  (`繁體中文週報 / 繁體中文正文 / 英語講解 / 第 / 版 / 共`). P8 diff blocks
  are ONLY deletions of Chinese words cited in English P8 notes (now
  tone-marked pinyin) plus the same furniture. No article character added,
  removed, or reordered.
- P7/P8 reflow explained: P7 word-list lines and the P8 writing-model
  paragraph break at different points (e.g. core `南港展覽`+`館` vs edition
  `南港展`+`覽館`) because neighbouring Italian flows re-wrapped; the
  character sequences are identical. P8 "added runs" (8) are exactly these
  model-paragraph break-point splits, nothing else.

### 4. Gate 10 — REPRODUCTION (mandatory, blocking): PASS 8/8
- Fresh copy of the core build + the builder's `transform.py` ALONE
  (env `ZH_TW_IT_OUT` → proof scratch; files land in `<out>/svg` because
  the transform replaces the directory prefix, preserving the `/svg`
  suffix — noted after an initial wrong-path comparison that briefly
  reported no files; the files were in `gate10-out/svg/` all along, and
  delivered files were never touched: hashes + mtimes unchanged).
- One-process `run.py`: **exit 0, zero `HEAD TOO WIDE` / `FLOW OVERFLOW`
  warnings, TOTAL 150**, flow ends identical to the builder's log
  (P7 col3 1759.36, teaser 2557.36).
- SVG comparison scratch vs delivered: **8/8 byte-identical**.

### 5. p8.py CLEAN + registry diff (explicit-path form)
- `p8.py extract` (edition): **150/150**; (core): 150/150.
- `p8.py compare --core-p8 … --edition-p8 … --total 150`: **CLEAN,
  missing=[], extra_count=0, keydiff=[]** (the `--target it` form was not
  used, per the builder's note; keydiff=[] is expected because the tool
  normalizes the writing item to ✓).
- Independent registry-dump diff (fresh core copy vs Gate-10 copy, full
  REG JSONs): **keydiff = [150] only** — `(開放題,範文如下)` →
  `(domanda aperta — modello qui sotto)`; **notediff = 150/150**; level /
  type / page diffs = none.
- Edition registry notes contain **ZERO Han characters** (verified over all
  150 notes). All 150 notes were read in full: coherent Italian,
  fact-consistent (day counts 151/31, hours 6+8+8+8=30, 6-0 not 6-3,
  coupon set 4,100/8,200, frame `xiān bǐjià, zài jiézhàng`).

### 6. P8 paren style + CJK-paren discipline (critical family gate)
- Precedent verified from the W43 zh-tw-it column's OWN shipped build code
  AND shipped SVG (not zh-cn-it's or zh-cn-fr's): W43 `content8.py`
  renders `{n}. {key} ({note})`, writing `{n}. ✓ ({note})`, separator
  `— Pagina {pg} —`; W43 shipped P8 shows e.g. `1. B (Jangmi è un tifone
  di categoria severa.)`. This edition follows the same paren form with
  the core geometry the task sanctions (12.8 / lh 1.12 / gap 1; W43's own
  geometry was 13.0 / 1.13 / gap 0.25 — a disclosed, non-blocking
  divergence, see §Observations). Separators verified on the card:
  `— Pagina 1 —` … `— Pagina 8 —`.
- KEY-section-only check (y ≥ 1328, 168 nodes): **zero full-width
  parentheses, zero Han characters inside parentheses of either width**.
  Page-wide full-width parens (10 nodes) are all frozen target-text
  exercise stems identical to the core — except one core key line
  (`35. 節氣 — Lidong is a solar term （節氣）.`) legitimately converted
  to the paren-style Italian note (`35. 節氣 (Lìdōng è un termine solare
  (jiéqì).)`); that is the transformation itself, not a defect.
- content8:62 AI-variant trap: P8 key 138 =
  `人工智慧 (L'IA nella finanza: réngōng zhìnéng.)` — Italian, pinyin
  only, **no full-width ＋** (edition P8 ＋ count = 0; core P8 had 1, in
  that same key line). The P5/P6 AI gloss form is a separate string and
  is also Italian (`Tre segni più: Finance+ … IA+ (intelligenza
  artificiale …)`); `AI inside finance` / `artificial intelligence`
  occur nowhere in the edition. P1/P6 ＋ counts are frozen (1 and 3,
  identical to core).

### 7. Occlusion audit + round-4 fixes
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fired, clean
  controls silent). Edition: **0 flags**. Core: **0 flags**. `--core`
  NEW-vs-core: **0**.
- Same-baseline ink-collision scan (canonical `ink_box` measurement,
  furniture bands, all pages): **0 collisions**.
- P4/P6 chart-label graze check (text ink vs any later-drawn opaque rect):
  **0 hits** on both chart pages.
- Round-4 fixes re-measured: P5 box title `天母時間表 · Programma Tianmu`
  ink-right 1879.8 < border 1885 (5.2px clear); P6 `比價提醒 · Confronta
  i prezzi` ink-right 1827.0 < 1885. P7 letters box rect bottom 1759.36
  (= builder's col3 end), last letters line ink-bottom 1756.13 — inside
  the border. Teaser: last teaser ink-bottom 2526.11 (builder's flow-end
  figure 2557.36); both clear of the 2580 footer rule (33.9px / 22.6px).
  Teaser/footer clearance confirmed visually on the P7 card.

### 8. Gloss / match counts (zh-tw core's true counts, NOT zh-cn's 33)
- Registry: **150 = A2 44 / B1 74 / B2 32; types 單選 67 / 完成句子 54 /
  配對 16 / 完形單選 12 / 寫作 1; pages 10/18/18/18/18/18/12/38** — identical
  core vs edition.
- Match sets: 4 `match_set` calls (content12 ×1, content34 ×2, content56
  ×1), each 4 left + 4 right; registry 配對 per page P2/P3/P4/P5 = **4+4+4+4
  = 16**. Lefts/rights (Chinese target text) identical core vs edition;
  only the notes translated EN→IT with pinyin citations.
- Gloss call sites identical core vs edition per file (gloss 4/5/3/0/0,
  glossline 0/0/0/3/1). Gloss prefix `Nota — ` ×12, `Notes` ×0.
- Writing: topic 《我的旅展計畫》, model **138 characters** (band 120–180;
  registry note confirms `(138 caratteri)`, P8 glossline confirms
  `modello di 138 caratteri`).

### 9. P7 golden sentences
- All 8 verbatim from this issue's own articles, **exactly 2× each
  issue-wide** (article + P7, no-separator join over text nodes):
  p.1 ×2 (`用手機…金融科技`, `123個國家及城市、1,600個攤位`), p.2
  (`需要才買…`), p.3 ×2 (`在高雄…`, `福隆的夏天…`), p.4 (`6比0…`),
  p.5 (`250家店家…`), p.6 (`旅展首日…`).
- Page tags verified on the P7 card: **p.1, 1, 2, 3, 3, 4, 5, 6**
  (the p.2 tag wraps across two lines: `(p.` + `2)` — normal wrapping).
  NOT zh-tw-de's S. form; the form matches this column's own convention.

### 10. Images + credits (P4 provenance NOT re-litigated)
- Per-page image payloads **byte-identical to the zh-tw core**:
  p1 `ac4dfe2ad3a43cd3` (434×300), p2 `a40e7a2b265beba6`, p4
  `18ad8ae06fac2860`, p5 `bcbada13a5ae19d6`; p3/p6/p7/p8 none — exactly
  the core's 4-photo layout, not zh-cn's.
- Credits verbatim from the Commons Artist field, identical incl. line
  wrap to the core: p1 `Photo: Wilfredor — CC0 (Wikimedia Commons)`,
  p2 `Photo: CorraleH — CC0 (Wikimedia Commons)`, p4 `Photo: Bain News
  Service — Public domain (Wikimedia Commons)` (wrapped `Wikimedia` /
  `Commons)`, same y in core and edition), p5 `Photo: Benjamin Balazs —
  CC0 (Wikimedia Commons)`.
- BINDING: the core KIT's P4 provenance adjudication (2026-10-27, CLOSED)
  is respected — placed bytes and credit line are unchanged, so
  provenance is NOT re-flagged. (Limitation: no live Commons re-query
  was performed in this proof; see §Limitations.)

### 11. Readers' corner
- Frozen Traditional disclosure: **all 5 wrapped lines line-for-line
  identical to the core, same baselines**: y 1426.98 / 1457.51 / 1488.04 /
  1518.57 / 1549.1, text identical (incl. `你的來信，下一期見。`).
- Italian disclosure (full text reconstructed from the card + SVG):
  `Lettera di esempio della redazione, non vera. Avviso di rinvio: il
  VOL.1 aveva promesso lettere vere e i migliori testi di pagina 8 da
  questo numero; alla chiusura non ne era arrivato nessuno pubblicabile,
  quindi resta l'esempio. Scrivici!` — states no genuine letters exist
  (`nessuno pubblicabile`) and carries the verbatim open invitation
  **`Scrivici!`** (last line, inside the letters box, visually confirmed).

### 12. Furniture three-way (core · W43 zh-tw-it · this edition)
- P1 badge MEASURED on all three P1 SVGs: core x=975 y=378 21pt OLIVE
  `#3e4c2a`; W43 x=975 y=378 21pt BRICK `#a4553a`; **this edition x=975
  y=378 21pt BRICK `#a4553a`, in place, text identical to W43:
  `TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE
  PER I LETTORI ITALIANI`** — builder's claim CONFIRMED exactly.
- Footer (all 8 pages, 20pt, baseline 2624): `Lucerna · SETTIMANALE
  CINESE TRADIZIONALE VOL.2 · TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI
  IN ITALIANO` + `Pagina {n} di 8` — VOL.2-adapted from W43's VOL.1 form.
- Gloss prefix `Nota — ` (not `Notes｜`); box titles with W43-overflow
  fixes kept: `本週句式 · Struttura settimanale` (P7),
  `本週一詞 · Parola settimanale` (P1) — the exact forms, not the
  overflowing alternatives. P8 band `測驗與答案 · Test e risposte`,
  heads A–F in Italian as claimed, keys header + `Tutte le note in
  italiano · ✓ = il modello di scrittura` present. P7 band sub
  `Tre livelli, tre temi`, heads `Parole della fiera` / `Partite e
  stagioni` / `Modi di dire locali`, phrase header `Frasi della
  settimana — parola per parola dagli articoli di questo numero`,
  teaser `La prossima settimana (VOL.3)`, readers' title
  `L'angolo dei lettori`, clinic title `Clinica degli errori` — all
  present. Bylines `Dalla redazione · Fonte:…` (P1/P4/P6). Match
  instruction `Abbina parola e definizione` ×4 (all four match sets are
  word↔definition). `Completa` / `Scrittura` in place.
- No discrepancy required adjudication against tables.json; tables.json
  was NOT edited. Badge measured against shipped W43 SVG, not the table.

### 13. Residual Latin (re-run from rendered output)
- Banned-string sweep (rendered SVGs): `Baseball words`, `low cost`,
  `Did you get`, `Over to you`, `Quick quiz`, `Fill in`, `True or
  false`, `Answer keys`, `All notes in English`, `Model answer`,
  `Open task`, `Word of the week`, `This week`, `Staff report`,
  `Source:`, `Work it out`, `AI inside finance`, `artificial
  intelligence`, `English`, `Page` — **all ZERO**.
- Round-5 fixes hold: P4 word-card title `棒球詞卡 · Parole del baseball`
  (wrapped over two lines, fully visible); `low cost` → `tariffe
  economiche` in the P5 gloss (wrapped `le tariffe` / `economiche spesso
  escludono il bagaglio…`) and in P8 key 70.
- English-word detector over all Latin nodes (66 hits): every hit
  adjudicated — Italian words coinciding with English (`come`, `all`,
  `stand` = exhibition booth, `festival`, `budget`, `quiz`, `test`,
  `film`, `set`, `start-up`), frozen proper names / event codes
  (`Fintech Nexus: Bridging the World, Building the Future`,
  `Hong Kong Convention and Exhibition Centre`, `FinTech Week`,
  `Jurassic World`, `Bain News Service`, `StartmeupHK`), photo credits,
  venue/team/news/film names, `Halloween` (same in Italian), and
  established Italian loanwords (`check-in`, `social`, `fintech`).
  **Zero English explanation prose. No blocking residue.**
- COORDINATOR ADDITIONAL CHECK (P3 C34 tail pair): rendered-output sweep
  of ALL text nodes — `Work it out` is ABSENT everywhere. The
  `算一算` head is already translated on all three occurrences:
  **`算一算 · Facciamo i conti`** (P2 y=331.125, P3 y=616.5, P5 y=426.25).
  NOT BLOCKING; no builder fix needed for this item.

### 14. Web regen
- From the delivered SVGs alone (repointed render.py in proof scratch):
  cards **8/8 byte-identical**; print PDF **byte-identical**
  (`be06fcfa…`); web PDF **content-identical, timestamp bytes excepted**:
  same size (3,456,580), 8 pages, all 8 page-image hashes identical; the
  ONLY differing bytes (8 bytes) are the `CreationDate`/`ModDate`
  trailer (`D:20261028085729Z` delivered vs `D:20261028091949Z` regen).
  Stated explicitly, as required.

### 15. Eyeball all 8 cards (1950×2700 PNGs)
- P1: badge legible, photo + credit clean, no overflow. P2: match set,
  photo + credit clean. P3: `算一算 · Facciamo i conti` clean, no
  overflow. P4: chart bars 1/5 with clear labels, photo + caption +
  credit fully visible, word-card title fully visible. P5: schedule box
  title inside border, pumpkin photo + credit clean. P6: hours chart
  6/8/8/8 with clear labels, comparison box clean. P7: letters box last
  line inside border with clearance, teaser band clear of footer, golden
  sentences + tags clean. P8: paren keys throughout, writing model fully
  visible, keys end well above footer.
- **Layout clean on all 8; no overflow, overlap, or missing content.**

### 16. ABSTRACT.txt
- **Single line, zero ASCII double quotes** (verified programmatically).
- Italian, names the paper (Lucerna), target language (cinese
  tradizionale), reader (lettori italiani), A2–B2 levels, and 150
  exercises, plus a learner search phrase (`impara il cinese leggendo le
  notizie vere, come si dice in cinese`).
- Every named topic cross-checked against the zh-tw core's actual
  content: Hong Kong FinTech Week ✓, Fiera Internazionale del Turismo di
  Taipei (ITF) ✓, Wei Chuan Dragons / Taiwan Series ✓, Lìdōng ✓,
  festival dell'acciaio di Kaohsiung ✓, finale delle sculture di sabbia
  di Fulong ✓, Halloween a Tianmu ✓. **No topic outside the core —
  nothing blocking.**

## PDF pins re-verified (coordinator pins)

| file | bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL2-IT.pdf` (print) | 20,069,224 | `be06fcfa7b27643553af72267e37c8a4f7cdccca779d6c9f4e334d2b05a93e38` |
| `Lucerna-VOL2-IT-web.pdf` (web) | 3,456,580 | `5b5c111ed1eca5467b12d4e32412576d20bbbe055302a2e8ababb3bc57a96c15` |

Both match the coordinator's pins exactly. SVG pins match the builder
KIT §10 full hashes on all 8 pages; card byte sizes match KIT §10 on all
8 pages.

## Limitations (stated honestly)

- Italian was checked by full reading of the explanation layer (all 150
  P8 notes read in full, plus gloss/furniture skim and the English-word
  detector sweep) — NOT by a native Italian speaker. No Italian defect
  was found; a native-speaker pass could still catch style nuances.
- No live Commons API re-query was performed (prior fetches in the core
  line returned HTTP 403, outcome ambiguous). Image verification rests
  on byte identity with the core, verbatim Artist-field credits, and the
  coordinator's CLOSED P4 adjudication — per the binding rule, P4
  provenance was not re-flagged because bytes and credit are unchanged.
- Sibling builds (zh-tw-ru, zh-tw-nl) were running during preflight;
  they were verified to write only to their own dirs and the mtime diff
  on this edition's dirs was zero. They do not affect this verdict.

## Non-blocking observations (NOT defects, NOT part of the verdict)

1. CJK distinct-count definitions: builder's 772 reconciles exactly as
   narrow-Han 766 + 6 U+3000-block punctuation marks; the union count
   reconciles to 1030 vs the builder's 1031 (1-character definitional
   residue). The hard gate (outside union = ∅) holds under every
   definition tried.
2. W43 zh-tw-it's own P8 geometry was 13.0 / lh 1.13 / gap 0.25; this
   edition keeps the CORE geometry (12.8 / 1.12 / gap 1) with the W43
   paren form — a disclosed divergence the brief sanctions ("core
   geometry kept"), visually clean on the P8 card.
3. P7 a2/b2 flows end at y=1561/1594 vs the 1560 flow bottom with no
   warning; the phrase strip starts lower and the card shows no overlap
   (inherited core geometry, also noted by the builder).
4. P7 letters-box +14px padding (formula constant 26→40) is a deliberate
   divergence from core geometry that fixes a real last-line/border
   straddle; verified correct on the card (last ink 1756.13 < box bottom
   1759.36).
5. Teaser end: builder's flow-end figure 2557.36 vs this proof's ink
   bottom 2526.11 — both clear of the 2580 footer rule; the difference
   is flow-end vs ink measurement, not a defect.
6. The p.2 golden-sentence tag wraps across two lines (`(p.` / `2)`) —
   normal text wrapping, tags otherwise complete and correct.
