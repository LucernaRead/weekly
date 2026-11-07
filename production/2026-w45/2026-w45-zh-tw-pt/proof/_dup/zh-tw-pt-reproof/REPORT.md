# INDEPENDENT RE-PROOFREAD — W45 ZH-TW × PT (Traditional Chinese target · Portuguese reader)

**Verdict: PASS — ZERO PROBLEMS.** Full re-proof from scratch after the B-1 fix
round (SOP §8.4). Every gate below was re-verified independently; nothing was
taken from the fix report on trust. This report is the finalization evidence
for the coordinator's insert step. This proof did NOT insert, post to Discord,
dump cards/PDFs to main chat, create crons, spawn subagents, or clean shared
scratch dirs, and did NOT modify the delivered edition (delivery mtimes and
hashes identical at start and end; see Pre-flight and Limitations for one
disclosed build-dir mtime incident with no content effect).

- Edition: `files/weekly-report-w45-zh-tw-pt/` (svg ×8, cards ×8 1950×2700,
  print + web PDFs)
- Core: `files/weekly-report-w45-zhtw-core/` (KIT read first; its counts are
  authoritative — NOT the zh-cn split)
- W43 same-pairing reference: `files/weekly-report-zh-tw-pt/` (KIT §7 and
  zero-problem proof §13 read; pinyin discipline verified from its shipped
  artifacts, not from KIT wording alone)
- Build: `hidden_files/weekly-report-w45-zh-tw-pt-build/`; transform:
  `hidden_files/weekly-report-w45-zh-tw-pt-transform.py` (279 pairs re-counted
  by AST: BSLIB 3, C12 52, C34 60, C56 62, C7 49, C8 53)
- Fix work products consulted (not trusted): `hidden_files/w45-zh-tw-pt-fix/`
  (pre-fix snapshots, pre-fix transform copy, logs, reassembly JSON, registry
  dump); first proof: `hidden_files/w45/zh-tw-pt-proof/REPORT.md` (read in full)
- Proof work: this dir (`REPORT.md` + `work/`). All proof renders ran in fresh
  copies under `work/` — never inside the core build dir, never importing a
  content module inside a core build dir; the one transform invocation that
  touched the real build dir is disclosed under Limitations.

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker/process writing to delivery/build dirs (`ps` clean at
  start; the only other sleeps seen belonged to a sibling edition's reproof
  and never touched these dirs).
- (b) Two mtime snapshots of both dirs ~6 minutes apart (09:35 vs 09:41 UTC):
  ZERO changes (snap1 = snap2).
- (c) Fix session completed (last delivery write 09:33–09:34, before snap1).
- Result: PROCEED.

## Per-gate evidence (all PASS)

### 1. Freeze baseline + freeze diff — PASS
- `tools/freeze.py baseline` against the W45 zh-tw core build
  (`hidden_files/weekly-report-w45-zhtw-build`): **8/8 byte-identical**,
  core shipped SVGs re-hashed unchanged afterwards.
- `tools/freeze.py diff --strict-cjk`: per-page +/− strings 25/22, 38/35,
  43/38, 36/33, 44/40, 42/37, 95/87, **196/187**; **strict-CJK added = 0 on
  all 8 pages**; driver exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE /
  TOO WIDE warnings. The P8 count moved 195 → 196 vs the first proof for
  exactly the wrap reason documented in Gate 6 (one extra wrap fragment,
  CJK accounting still 0).

### 2. Traditional independence — PASS (re-extracted, not trusted)
- Own extraction from shipped SVG text nodes (same method as the first
  proof): core 773 chars, W43 zh-tw-pt 791, union 1031, edition 772,
  **outside union: NONE**; edition set is a subset of the core's own set
  (edition-not-in-core: none). Absolute counts differ from the builder's
  (782/798/1040/780) by extraction method, as in the first proof; judged
  by outside = 0, the gate passes under either method.
- Simplified-only spot list (邮 说 国 龙 马 发 让 认 议 论 贝 财 见 车 红 灯
  无 为 乌 鸟 东 丝) over all edition text nodes: **0 hits**.
- Transform scan: no OpenCC, no s2t/t2s, no mapping table, no conversion
  logic of any kind (688 string literals scanned, 0 containing a
  Simplified-spot character); the only `_fw` mentions are the svglib
  typographic pair-conversion bypass (see Gate 6), not script conversion.

### 3. Target text zero difference — PASS
- Freeze strict-CJK added = 0 (Gate 1) plus a full per-string added-list
  read: every added string containing CJK is a bilingual head whose
  Chinese half is frozen target text, a P8 key line whose key is frozen
  target text, or lesson/gloss prose citing frozen terms (P4 "Quatro
  palavras" gloss, P7 lesson paragraphs) — no new target sentence
  anywhere. All added CJK characters are inside the core's own set
  (Gate 2).

### 4. Gate 10 reproduction — PASS (mandatory, blocking gate)
- My own replay of the builder's transform `--gate10` (fresh core copy +
  transform ALONE, one-process driver): **8/8 byte-identical, warnings =
  0, exit 0**, registry 150. The gate10 code path was read before running:
  it writes only to `hidden_files/w45-zh-tw-pt-gate10/` (fresh core copy,
  whole-`expanduser(...)` repoint — the es template's nested-junk bug is
  fixed here, not copied).
- No stray nested tree: search for a `.../home/...` path or gate10 SVG
  under delivery/build dirs: empty.

### 5. p8.py — PASS
- Explicit-path invocation (tables.json's default P8 filename does not
  apply here; this core's file is `p8-test.svg`):
  `p8.py compare --core-p8 ../files/weekly-report-w45-zhtw-core/svg/p8-test.svg
  --edition-p8 ../files/weekly-report-w45-zh-tw-pt/svg/p8-test.svg --total 150`
  → **CLEAN, core 150 noted = edition 150 noted, missing=[],
  extra_count=0, uncertain=[], keydiff=[]** (exit 0).
- Registry-dump diff (my own one-process dumps of fresh core and edition
  copies, OUT repointed to scratch, never the core build dir):
  page/level/type diffs = []; **key diff exactly #150** — core
  `(開放題,範文如下)` → PT `(pergunta aberta — modelo abaixo)`; all 150
  notes translated (0 identical to core); 0 notes with Han in the new
  registry. Counts exact: A2 44 / B1 74 / B2 32; pages
  10/18/18/18/18/18/12/38; types 單選 67 / 完成句子 54 / 配對 16 / 完形單選
  12 / 寫作 1. Writing model verbatim: all 5 wrapped model lines
  byte-identical to core, 138 characters (band 120–180).

### 6. B-1 FIX VERIFICATION — PASS (the critical gate, wrap-aware, from the delivered SVG)
- Wrap-aware reassembly of ALL 150 P8 key items from the delivered
  `p8-test.svg` (keys block y ≥ 1328, column-sorted, fragments joined):
  150/150 items, numbers 1–150, none missing.
- (a) **Notes containing Han = 0.** Each of the first proof's 32 items
  (17, 25, 26, 27, 28, 35, 43, 44, 45, 46, 55, 61, 62, 63, 64, 79, 80, 81,
  82, 101, 103, 105, 106, 109, 110, 111, 112, 132, 133, 134, 138, 149) was
  checked individually: every one now carries pinyin in the note prose
  (e.g. 17 `...Lidong: jìnbǔ.`, 35 `...(jiéqì).`, 55/105/132
  `Conquistar o título é fēng wáng.`, 149 `...xiān bǐjià, zài
  jiézhàng.`).
- (b) **Keys UNCHANGED.** Pre-fix → post-fix registry diff (first
  proof's `reg-ed.json` vs my new dump): exactly the 32 note changes,
  **0 key changes, 0 page/level/type changes**. In the 12 items whose
  key is itself Han (17, 35, 55, 101, 103, 105, 110, 112, 132, 133, 134,
  138), the Han key is intact in the render and only the note-prose
  repetition was converted (e.g. 138 `138. 人工智慧 (IA dentro das
  finanças é réngōng zhìnéng＋.)`). Transform-level diff (pre-fix
  transform copy vs current transform): only the 32 note strings
  changed (29 unique strings — 3 forms repeat across items: the
  `Conquistar o título é fēng wáng.` sentence ×3, etc.); OLD core
  strings untouched.
- (c) **Conversion table match + W43 precedent, verified from shipped
  artifacts.** Every one of the 32 reassembled notes contains its KIT
  §13.1 form. W43 precedent verified from W43's SHIPPED P8 SVG (not just
  its KIT): `fēng wáng` — W43 P8-60 `60. 封王 (Conquistar o título é
  fēng wáng.)`, the identical sentence to W45 55/105/132; `tǎotáng` —
  W43 P8-107 `107. 討糖 (Tǎotáng é o jeito taiwanês de dizer «doces
  ou...`, the joined form matching W45 79/110/133 (the KIT cites W43
  content7.py line 41, which is the same sentence's source; the shipped
  P8 confirms the form). All other forms are standard tone-marked
  pinyin matching the table.
- (d) **Answer-block full-width parens = 0** (all 150 reassembled key
  items scanned for （/）).
- (e) **`_fw` bypass disposition — RETAINED, verified content-neutral.**
  Read in the edition build: `content8.py` saves `_orig_fw`, installs
  `_fw_keys` (digit-led lines, i.e. key lines `N. ...`, returned
  unchanged; all other lines through `_orig_fw`), restores `_orig_fw`
  immediately after the keys flow. `svglib._fw` converts a paren PAIR to
  full-width only when the enclosed text contains CJK — so with notes
  now CJK-free, the bypass is strictly unnecessary for paren safety,
  but it provably alters no key line (registry diff 0 key changes;
  rendered keys intact) and no answer-block paren is full-width.
- **ITEM 138 JUDGMENT — ACCEPTED, with reasoning.** (i) No-precedent
  claim VERIFIED by my own grep: zero occurrences of 人工智慧 in the
  whole W43 zh-tw-pt shipped build (build py/svg/md/json/txt + shipped
  SVGs), and W43's global item 138 is a different exercise (shipped
  W43 P8-138: `138. 留友 (Liú yǒu kàn — salve para os amigos lerem.)`).
  One citation slip in the fixer KIT §13.2 (non-blocking, see below):
  the `pǐnwèi quàn` sentence it attributes to W43-138 is actually
  W43-137 (`137. 品味 (Os cupons são as pǐnwèi quàn (fichas de
  degustação).)`); the substance — no 人工智慧 precedent, 138 is a
  different exercise — holds. (ii) The retained form is
  `IA dentro das finanças é réngōng zhìnéng＋.`: the Han citation
  人工智慧 → réngōng zhìnéng satisfies B-1's requirement (Han → pinyin);
  ＋ (U+FF0B) is a symbol, not a Han character — it is outside the CJK
  range, does not appear in the notes-with-Han scan, and does not
  trigger `_fw` pair conversion (which concerns parens only). (iii)
  Retention is consistent with the issue's own P6 gloss theme, verified
  on the P6 card: `Nota — Três sinais de mais: Finanças+ ... IA+ ...`
  ("three plus signs"); dropping ＋ would change "AI+" to plain "AI"
  against that gloss. **Therefore the ＋ retention does not break
  B-1's intent or the column discipline, and item 138 PASSES.**
- Han citations OUTSIDE P8 notes correctly left alone: P4 "Quatro
  palavras" gloss and P7 lesson paragraphs still cite Han terms, and
  p1–p7 are byte-identical to the pre-fix delivery (Gate 14) — changing
  target-text prose would have been a defect, not a fix.

### 7. P8 paren style — PASS
- Paren form verified from the W43 zh-tw-pt shipped BUILD CODE itself,
  line 118: `f"{e_['n']}. {e_['key']} ({e_['note']})"` — the edition
  uses exactly this form (edition build `content8.py` same pattern).
- Core font/lh/gap kept: core and edition content8.py both run the keys
  flow at 12.8 / lh 1.12 / gap 1, Flow 1328–2540.
- Separators `— Página {pg} —` (not the zh-cn-pt dash style) on all 8
  key pages.

### 8. Occlusion audit — PASS
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fired,
  clean controls silent). Edition **0 flags**; core 0 flags;
  **NEW vs core: 0**.
- Same-baseline ink-collision scan (my own, using the tool's font/ink
  math, all pages, both editions): **0**.
- P4/P6 chart-label element check (text ink vs later-drawn rects, any
  overlap): **0 on both chart pages**, core and edition.
- P4 bars: brick widths 120.0 ×1, 600.0 ×1 (= 1 and 5 runs). P6 bars:
  olive widths 600.0 ×1, 800.0 ×3 (= 6, 8, 8, 8 hours). Identical to
  core (rect-width sets equal, including non-bar rects).
- **P7 LETTER-BOX DIRECT MEASUREMENT (mandatory — audit blind spot):**
  readers box rect byte-identical to core (x=1451 y=1184.86 w=434
  h=560.5, bottom 1745.36). Edition PT last-line element: baseline
  1731.63, text `exemplo fica e o convite continua aberto.` Pixel scan
  of the delivered P7 card (x 1460–1880): last text ink row 1736, no
  text ink between 1737 and the border — i.e. last-line ink bottom
  ~1736.1, **~9px clear of the 1745.36 border** (reproduces the first
  proof's 1736.13). Card-crop visual: last line fully inside the box
  with clear space below, border intact. Core card confirms the
  diagnosis (its last-line ink rows 1741–1752 straddle the border).
  The P7 gap fix (+10 → +0 inter-para gaps, interior-only) is therefore
  re-verified, not merely accepted. P7 col3 ends 1745.36, teaser ends
  2543.36, unmoved.

### 9. Gloss / match counts — PASS (zh-tw core's true counts)
- `gloss()` calls: core 4 + 5 + 3 = 12; edition 4 + 5 + 3 = 12; rendered
  `Nota — ` prefix nodes 12 = 12 (core `Notes` nodes 12).
- Registry 150 with exact core counts (Gate 5); writing model verbatim,
  138 characters (Gate 5).

### 10. P7 golden sentences — PASS
- All 8 strip sentences verbatim from this issue's own articles, each
  exactly **2× issue-wide** (article page + P7) in BOTH core and edition
  under wrap-safe (unspaced-concatenation) counting — space-joined
  counting undercounts wrapped sentences, as the first proof noted.
  Tags **p. 1, 1, 2, 3, 3, 4, 5, 6** (article pages P1, P1, P2, P3, P3,
  P4, P5, P6). Not the zh-tw-de S. form.

### 11. Images — PASS
- Per-page embedded payloads + geometry byte-identical to the zh-tw
  core: P1 `ac4dfe2ad3a4…` (1451,640,434×300), P2 `a40e7a2b265b…`,
  P4 `18ad8ae06fac…`, P5 `bcbada13a5ae…`; P3/P6/P7/P8 no photos — all
  as core.
- Printed credits verbatim: P1 `Photo: Wilfredor — CC0 (Wikimedia
  Commons)`, P2 `Photo: CorraleH — CC0 (Wikimedia Commons)`,
  P4 `Photo: Bain News Service — Public domain (Wikimedia Commons)`,
  P5 `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)`.
- P4 provenance: placed bytes and credit line unchanged from the core,
  so per the core KIT's binding 2026-10-27 coordinator adjudication
  (CLOSED), provenance is NOT re-flagged. No live Commons re-query was
  treated as evidence either way.

### 12. Readers' corner — PASS
- Frozen Traditional disclosure line-for-line identical to the core:
  all 5 wrapped lines byte-identical
  (`延期披露：VOL.1曾預告本期起刊登真實 / 讀者來信和第8版最佳作文；截至截稿， /
  本報未收到可刊登的真實來信與投稿，因 / 此本期仍刊登編輯範例，並繼續公開徵 /
  集。你的來信，下一期見。`).
- Portuguese disclosure present, 6 lines, stating no genuine letters
  arrived (`até o fechamento nenhuma publicável chegou`) and ending
  exactly `...por isso o exemplo fica e o convite continua aberto.`
  — verified ON THE CARD (crop visual + SVG element + pixel scan,
  Gate 8). The W43 wording differs legitimately (W43 was the promissory
  volume; W45 is the deferral volume, faithfully rendering the core's
  deferral disclosure).

### 13. Furniture three-way — PASS (measured, not assumed)
- P1 badge slot on all three P1s: **x=975 y=378, 21pt, weight 700,
  centred (text-anchor=middle)**: core fill `#3e4c2a` (OLIVE), W43
  zh-tw-pt fill `#a4553a` (BRICK), this edition fill `#a4553a`
  (BRICK). Badge ink measured with the tool's ink math: edition box
  [337.96, 356.75, 1612.21, 383.75], width 1274.25 — **identical to
  W43pt to the pixel**, centred on 975.
- Badge TEXT: edition badge element byte-identical to the W43 zh-tw-pt
  shipped SVG badge element:
  `TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS
  LEITORES DE LÍNGUA PORTUGUESA`. (My first comparison script compared
  badge+footer node lists, where the footer legitimately differs
  VOL.2 vs VOL.1; the badge element itself is identical, and
  tables.json was not edited.) Shipped W43 wins over tables.json per
  the task rule, and they agree on this string.
- Footer on all 8 pages, VOL.2-adapted Portuguese form:
  `Lucerna · SEMANÁRIO CHINÊS TRADICIONAL VOL.2 · TEXTOS EM CHINÊS
  TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS`; page lines
  `Página {n} de 8`; gloss prefix `Nota — `; P8 separators
  `— Página {pg} —`.

### 14. Residual Latin (rendered-output sweep) — PASS
- Bilingual-node scan of ALL text nodes + English-blacklist scan of ALL
  nodes, re-run independently (not just added strings).
- P3 catch HOLDS on the card: `算一算 · Faça as contas`; `Work it out`
  occurs **0 times** anywhere in the edition.
- Every bilingual node's Latin segment is Portuguese (section heads,
  glosses, instructions), a frozen proper name (VOL.2, SOLID TIDES
  forum name inside a frozen Chinese stem, JUMP show title), or frozen
  test option letters (A. 對 · B. 錯) — no English explanation prose.
- Blacklist hits adjudicated, not copied: `Complete` (60×) = the
  Portuguese instruction word (W43 zh-tw-pt KIT §5 precedent);
  `festival` = the Portuguese word (identical spelling; surrounding
  sentences are Portuguese, e.g. `O festival do aço vai de 23 de
  outubro...`). No other blacklist word occurs.
- Builder's adjudicated residues, each verified: `fintech`/`FinTech` =
  the Portuguese-press loanword + the event's official English theme
  name `Fintech Nexus: Bridging the World, Building the Future` frozen
  inside a Chinese sentence; `Photo:` = frozen Commons credits (4);
  `some`/`Some` = the Portuguese verb somar (`some esse custo`,
  `Some as taxas`); `MVP` = sports abbreviation used in Portuguese
  prose; `ITF` = the fair's acronym, defined in the PT gloss;
  `VOL.2` = volume marker.
- **CHANGE-SCOPE CHECK — confirmed:** p1–p7 SVGs byte-identical to the
  fix snapshots (`sha256sum -c` on
  `hidden_files/w45-zh-tw-pt-fix/svg-before-fix.sha256`: p1–p7 OK,
  only p8-test.svg differs, as the fix requires). No unexpected change.
- **Fixer's non-blocking notes, both confirmed:** (a) Reassembly wrap
  artifact — raw text nodes show item 149's note split as line 1
  `...xiān bǐjià, zài` + line 2 `jiézhàng.)`; the wrap-aware join
  `xiān bǐjià, zài jiézhàng.` is correct, not a content error.
  (b) P8 freeze string count 195 → 196 — the added-string multiset
  diff vs the first proof's freeze JSON shows exactly the 32 converted
  notes (32 old strings → 33 new strings; the +1 is the `jiézhàng.)`
  wrap fragment) with CJK accounting still 0 added.

### 15. Web regen — PASS
- Regen from the delivered SVGs in proof scratch (repointed render.py):
  cards **8/8 byte-identical**; print PDF **byte-identical**
  (20,845,651 B, same SHA); web PDF same size (3,510,596 B) and
  content-identical after stripping timestamp bytes — the SOLE
  difference is `CreationDate`/`ModDate` (delivered
  `D:20261028093331Z` vs regen `D:20261028094634Z`), stated explicitly.

### 16. Eyeball all 8 cards — PASS
- All 8 cards viewed full-page: layout clean, no overflow, overlap,
  footer collision, or missing content on any page. P4 chart +
  photo/caption/credit fully visible; P6 chart labels clear of bars;
  P7 readers box as in Gate 8; P8 reflow clean — item 149 wraps over
  two lines inside its column, keys end y=2328 (driver log), 212px
  clear of the 2540 bottom, footer clear.

### 17. ABSTRACT.txt — PASS
- Portuguese single line (one trailing newline), **no ASCII double
  quotes**. Names the paper (Lucerna), target language (chinês
  tradicional), explanation language (português), A2–B2, 150
  exercícios, plus a learner search phrase (`aprenda chinês
  tradicional lendo as notícias da semana`). mtime still
  2026-10-28 09:11 (pre-fix), as the fixer claimed.
- Every named topic cross-checked against the zh-tw core's actual
  content: Semana FinTech de Hong Kong ✓, Feira Internacional de
  Viagens de Taipé ✓, Dragons campeões da Série de Taiwan ✓, Lidong e
  o Início do Inverno ✓, Festival de Escultura em Aço de Kaohsiung ✓,
  Halloween de Tianmu ✓. No topic outside the core.

## Non-blocking observations (separate from the verdict)
- N-1. Fixer KIT §13.2 citation slip: the `pǐnwèi quàn` sentence is
  W43 P8-137, not W43-138 (W43-138 is `留友 / Liú yǒu kàn`). Substance
  unaffected — no 人工智慧 precedent exists either way — but the
  number should be corrected if the KIT is ever re-edited. Not an
  edition defect.
- N-2. CJK absolute counts differ by extraction method (mine: core 773
  / W43 791 / union 1031 / edition 772; builder's: 782 / 798 / 1040 /
  780). Outside-union = 0 under both methods; no action needed.
- N-3. The gate10 temp dir (`hidden_files/w45-zh-tw-pt-gate10/`) still
  exists after runs despite the KIT's "removed after each run" wording
  (also noted in the first proof). Housekeeping only; it is outside
  delivery/build dirs and my replay overwrote it cleanly.
- N-4. A `render.py` process belonging to another (sibling) task was
  visible in `ps` at the end of this proof; delivery mtimes and hashes
  prove it did not touch this edition.

## Limitations (stated honestly)
- Portuguese was checked by full reading of every rendered string, not
  by a native speaker; no Portuguese grammar claim beyond that reading
  is made.
- Commons Artist fields were NOT re-queried live in this proof (credits
  verified byte-identical to the core KIT's recorded Artist-field
  values; P4 provenance rests on the binding coordinator adjudication,
  not a fresh fetch).
- No live web source was consulted for facts; all topic/date claims
  were checked against the zh-tw core KIT and the frozen target text,
  which this fan-out must not alter.
- **Disclosed proof-process incident:** while checking the transform's
  CLI, I ran it with `--help`, which (the script has no help branch)
  executed the default apply path and rewrote the edition build dir's
  `.py` files (mtimes changed; the delivery dir was untouched). Content
  effect verified nil: delivered SVG/PDF hashes are unchanged from the
  coordinator pins before and after, and Gate 10 (fresh core copy +
  transform alone) reproduces the delivered SVGs 8/8 byte-identically
  from the current state. No proof conclusion depends on the rewritten
  mtimes. The delivery dir was never written by this proof.

## PDF pins re-verified (coordinator pins confirmed)
- Print `Lucerna-VOL2-PT.pdf`: **20,845,651 bytes**,
  SHA-256 `fc85e26f31aa89e92ab0b550af2e8f23e2cff27fc308d4f8808e0369f005d85c`
- Web `Lucerna-VOL2-PT-web.pdf`: **3,510,596 bytes (< 10 MB)**,
  SHA-256 `380e91d19a69082d68ff407762622119ce1e3305a67c3cd0006cbefb8e0c9b0e`
- SVG SHA-256 (final, re-verified): p1 `3d8481de100e9787dce9beffc4f64ed196df8f3f671a29a7023f792675b10a94`,
  p2 `99bcb003f2c4161af63bee1db143d8b03d8df5329c1ac58daa7d876c676b97c2`,
  p3 `aac1e5fc867795b4b9db53298791026f9714f9e739645f4b738f655ecfd7cdf9`,
  p4 `cbf88009a967b1ad28cfa1f9b0524ad8f7603ce62bc7b54433dc9afc5c2f9ab6`,
  p5 `23b7ad0b3b43cdc85a1ad20fa7893adeeab8803ba77e5744226433edf8e2731d`,
  p6 `2012bf23a67baf1cb2d5492ad0f849244ed41bafa01341d75ea5c9450943184e`,
  p7 `32799b27dad4ea22af5ddb2b6906904bfc10aea8e78e05d28cb0b632a19c56fd`,
  p8 `236b96ae89ed8529cd8cbb03c7049fb9e23d0b3eef7c0abbc1885bd5925a30b0`
- ABSTRACT.txt mtime 2026-10-28 09:11 (pre-fix, unchanged).

## Blocking list
None. ZERO PROBLEMS across all 17 gates.
