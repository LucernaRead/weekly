# INDEPENDENT REPROOF REPORT — W45 zh-cn × nl (Simplified Chinese target · Dutch reader)

## Verdict: ZERO PROBLEMS — PASS

This is the full SOP §8.4 reproof after the fix round. Every mandatory gate
(1–11) was re-verified independently from scratch — not copied from the
first proof's verdicts — and **all pass, including Gate 10**, the gate that
blocked the first proof. The first proof's single blocking item (B1,
transform-solo reproduction 5/8, 6/8 with trim) is **closed**: the full
documented chain now reproduces **8/8 SVGs byte-identical** to the delivered
files. No blocking problem was found. I did not fix anything, did not touch
`weekly-git`, `insert.py`, Discord, main chat, crons, shared scratch dirs,
the core build, the W43 shipped edition, `tools/`, or the delivery dir
(read-only except this report dir + its `work/` scratch below).
**I do not declare the edition shipped — repo insertion is the
coordinator's step.**

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER — rule's intent)

- (a) No live worker writing to the nl delivery/build dirs at start: `ps`
  showed no zh-cn-nl process (only an unrelated zh-cn-it proof process
  working on its own edition).
- (b) Two mtime snapshots of both dirs a few minutes apart
  (`work/mtime1.txt`, `work/mtime2.txt`): **ZERO changes**.
- (c) The fix session had completed before this reproof started: the fix
  log (`hidden_files/weekly-report-w45-zh-cn-nl-build/scratch/fix-round-log.md`)
  and the KIT's fix-round section were on file, and the delivered hashes
  matched the fix log's pre-fix baselines exactly (see below).
- Delivery stability: all 19 delivered files (8 SVGs + 8 cards + 2 PDFs +
  ABSTRACT.txt) hashed at start (`work/delivery-hashes-start.txt`) and
  re-hashed at close — **all still OK**. The target did not move during
  reproofing.
- All tool runs used `tools/venv/bin/python` (Python 3.12.3).

## Per-gate evidence

### Gate 1 — Freeze baseline 8/8 + freeze diff, strict-CJK 0 — PASS
- `freeze.py baseline` (zh-cn core build → scratch): **8/8 byte-identical**
  to shipped core SVGs (p1 `e057bbfc…`, p8 `eaf368f8…`, full hashes in the
  run output); core SVGs re-hashed unchanged afterwards (tool's own
  "core integrity" line + my re-hash).
- `freeze.py diff --strict-cjk` core vs edition (`work/diff.json`): added
  CJK **0 on every page, TOTAL 0**, exit 0. Net CJK per page matches the
  first proof and the KIT exactly: p1 851→820 (−31), p2 1053→1031 (−22),
  p3 812→790 (−22), p4 810→789 (−21), p5 944→921 (−23), p6 1005→983 (−22),
  p7 760→739 (−21), p8 1102→1082 (−20). Added strings containing CJK are
  the frozen paired forms (gloss citations, bilingual furniture with the
  Chinese half frozen, P8 keys with identical Chinese keys); no new
  target text.
- Supporting: `freeze.py baseline` of the edition build itself against the
  delivered SVGs = **8/8 byte-identical**, and a driver run of that
  freeze-repointed copy exits 0 with **zero** `FLOW OVERFLOW` /
  `HEAD TOO WIDE` warnings, registry TOTAL 150, A2 56 / B1 69 / B2 25,
  writing model 172 characters.

### Gate 2 — p8.py compare vs core — PASS (CLEAN, style verified from code)
- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-nl --target zh-cn`:
  **core 150 noted, edition 150 noted, status CLEAN, missing=[],
  extra_count=0, uncertain=[], keydiff=[]**. No keydiff item to verify
  from SVG nodes (none).
- Style verified from build code, not memory: core build `content8.py`
  lines 119/121 generate `f"{e_['n']}. {e_['key']} — {e_['note']}"` and
  writing `f"{e_['n']}. ✓ {e_['note']}"` — dash style; the edition build's
  keys loop is identical except furniture strings (`— Pagina N —`
  separators, Dutch headers). `NCHARS` computation line identical.
  Writing key `(open vraag — voorbeeldtekst hieronder)` / note
  `Open vraag — voorbeeldtekst hierboven in deel F, 172 tekens` /
  label `Voorbeeldtekst: ` match the KIT trimmed form and the delivered
  P8 node #150 verbatim. `bslib4.py` diff vs core build: only the footer
  line + gloss prefix (`Notes｜` → `Uitleg — `). `svglib.py`: md5-identical
  (`59fddd1772244ef5e30c6d413277a52d` both).
- Delivered P8: 150 numbered key lines, max keys y **2530.35** < 2540 flow
  bottom; #135 `135. 数字 — shùzì — AI-filmpersonages zijn digitaal.` and
  #140 `140. 立减 — lìjiǎn — afgetrokken bij het afrekenen.` present
  verbatim; old English/trim wordings absent from P8.

### Gate 3 — Occlusion audit + same-baseline scan + P6 chart-label check — PASS
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire once,
  clean controls silent). Edition audit: **0 flags**. With `--core`:
  core 0 flags, **NEW vs core: 0** (`work/occlusion.json`,
  `work/occlusion-core.json`).
- Same-baseline ink-collision scan (builder's `rowcheck.py` copied to my
  `work/` and run read-only against the edition SVGs, PIL true-ink boxes,
  SC face index 2): **0 flags across all 8 pages, including the P1 top band**.
- P6 chart-label element check: bars x=325, widths **810/537/480** (rows
  A/B/C, 3.0 px/yuan) from SVG rects; row-label ink right edges
  **204.0 / 143.0 / 180.0** (all < 325 bar start; see non-blocking note 3
  for the ≤0.4 px method rounding vs earlier figures); value labels at bar
  end + 16 px exactly (270 at 1151 = 1135+16; 179 at 878 = 862+16; 160 at
  821 = 805+16); **zero later-drawn rects overlap any of the 6 chart-label
  ink boxes** (paint-order intersection test).

### Gate 4 — Gloss counts (split on `·` itself) — PASS
- Source `gloss()` strings, split on `·`: core and edition **identical item
  by item, 10 calls, 4/4/4/3/3/3/3/3/3/3 (total 33)**, with the same Chinese
  heads in the same order (现货/立减/直降/节气; 仓库/评价/尺码/退换货;
  补冬/饺子/糍粑/期中; 候/交替/采访; 厚衣服/热饭/着凉; 淘汰/内战/止步;
  数字形象/公映/票房; 火化/救赎/以后; 结算/运费/广告; 说法/数据/退换货).
- Rendered gloss boxes in the delivered SVGs: edition **10**, every box
  prefixed `Uitleg — `.

### Gate 5 — P7 golden sentences — PASS (all 8 ×2, correct page tags)
Punctuation-stripped contiguous counts in the delivered SVGs (article page
+ P7, each exactly 2×): 「不用等11月11日」 p.1, 「下单就能发货」 p.2,
「先看结算页，再付款」 p.2, 「水开始结冰」 p.3, 「三场都输了」 p.4,
「小局一场没赢」 p.4, 「故事够不够好」 p.5, 「别以后，就现在」 p.5.
P7 renders the full-width-punctuation forms verbatim with the correct
page tags (p.1 / p.2 / p.2 / p.3 / p.4 / p.4 / p.5 / p.5).

### Gate 6 — Images — PASS
- `<image>` (href= data) counts core vs edition identical: **1/1/2/1/1/0/0/0
  = 6 photos**.
- Payload MD5s core == edition on every page and equal to the edition-build
  asset files: locker `420c6150…`, valley `550e463b…`, frost `d0b015bc…`,
  dumplings `e8d75277…`, lanparty `6b8e9037…`, popcorn `a903e35f…`.
- Credit lines in the delivered SVGs match the Commons API Artist field in
  `assets/CREDITS.md` (byte-identical CREDITS file, sha
  `a03a3d26…`, core build vs edition build): `Foto: Map hobby — CC0
  (Wikimedia Commons)`, `Foto: Paul Gilmore — CC0 (Wikimedia Commons)`,
  `Foto: Gerda Arendt — CC0 (Wikimedia Commons)`, `Foto: Syced — CC0
  (Wikimedia Commons)` (×2), `Foto: Based5290 — Publiek domein (Wikimedia
  Commons)`. Only the label was translated (`Photo:` → `Foto:`;
  `Public domain` → `Publiek domein`); authors/licences unchanged. File
  photos stay captioned 资料图; the P4 LAN caption states 2003/France.

### Gate 7 — Readers' corner — PASS (disclosure + explicit invitation, verbatim)
P7 col x=1473, y-identical to the core at every line (35 nodes, y lists
equal):
- Frozen Chinese letter (3 lines, y 1315.6–1376.66) and frozen Chinese
  disclosure sentence (6 lines from y 1437.19, incl. 编辑部示例信,不是真实来信…
  延期不是取消。) — byte-identical nodes.
- Dutch disclosure (5 lines, y 1579.19–1692.79): `Redactie: VOL.1 beloofde
  echte brieven in VOL.2. Die zijn er nog niet, dus een voorbeeldbrief.
  Uitgesteld, niet afgesteld — stuur ons je eigen brief in het Chinees!`
  — states no genuine letters exist (labelled editor's example + deferral)
  AND carries the explicit open invitation **`stuur ons je eigen brief in
  het Chinees!`** verbatim in the corner itself. The fix round's disclosure
  compression did **not** damage it: the whole disclosure block is exactly
  the core's 10 wrapped lines (y 1437.19–1692.79, shared Chinese/Dutch line
  at 1579.19), and the delivered text matches the fix script's pair-6 new
  literal exactly.

### Gate 8 — Furniture three-way + badge-slot re-adjudication — PASS
Re-measured from SVG nodes (x, y, size, weight, fill) in all three, not
inherited from the first proof's adjudication:
- **Badge slot — first proof's adjudication CONFIRMED on fresh evidence.**
  Core badge: (975, 434), 19.5pt, weight 700, OLIVE #3e4c2a,
  Chinese/English string. The y=372 line in the core is the frozen
  bilingual strapline `给学中文的人的周报 — Read the real China, in Chinese`
  (19pt, not a free slot). W43 shipped zh-cn-nl badge: (975, 434), 19.5pt,
  700, BRICK #a4553a, Dutch string. This edition badge: **(975, 434),
  19.5pt, 700, BRICK #a4553a, string byte-identical to W43**
  (`TEKSTEN IN HET CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS —
  DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`). This is an in-place replacement
  at the zh-cn core family's own slot: neither the EN subtitle-slot case
  (372/19.5pt) nor the FR/IT inserted-badge case (574/22pt) applies — no
  badge node exists at y=574 in any of the three, and y=372 remains the
  strapline in all three (core EN half → W43/edition Dutch half
  `Lees het echte China, in het Chinees`; Chinese half frozen). The y=92
  top strip likewise takes W43's Dutch half
  (`Lees echt Chinees, elke week`). The P1 edition line stays Chinese
  (`简体中文版 · VOL.2 · 双11 · 立冬 · S16`), per the W43 precedent.
- Footer (all 8 pages): `Lucerna · CHINEES WEEKBLAD VOL.2 · TEKSTEN IN HET
  CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS` — W43 string with
  the justified pair-varying change VOL.1→VOL.2 (this issue's number).
- Page line: `Pagina N van 8`, 8/8 pages. Gloss prefix: `Uitleg — ` (10
  boxes). P8 separators: `— Pagina N —`, 1–8 all present in order.
- Masthead: bare `Lucerna` blackletter, no article (Chinese is article-less
  per the SOP) — confirmed on the P1 card.

### Gate 9 — Web PDF regeneration — PASS (timestamp-only variance, precisely measured)
- Regenerated in my scratch from the delivered SVGs via the build's
  `render.py` (BASE redirected to scratch only, delivery untouched):
  **cards 8/8 byte-identical** to delivered cards; **print PDF
  byte-identical** to delivered (47,427,799 bytes, sha256
  `1be5629f53595f761d8648d365a200b19e16266f850ed7c580b2dfab2ccfe1cc` =
  KIT pin).
- Web PDF: delivered file verified **8 pages, 3,208,683 bytes (< 10 MB),
  sha256 `6b0c0a2582fb8f6cd0483de5a6e3c409122be8048b928f9ecd300ca9ff99a9fd`
  = KIT pin**. The regenerated web PDF is the same size (3,208,683 bytes)
  and 8 pages but a different SHA (`e8c05d6f…`): byte-diff shows **exactly
  10 differing bytes, all inside PIL's `/CreationDate` / `/ModDate`
  timestamp strings** (delivered `20261028071404Z` = builder's render time;
  regen `20261028080040Z` = my render time; 5 differing digits in each
  field). All image content is identical (cards 8/8 identical). This is
  inherent PIL PDF-writer wall-clock metadata, not a content defect, and
  does not break the KIT pin (which describes the delivered file, verified
  above). Note on counts: the first proof reported 6 differing bytes and
  the fixer 8 for their respective regen times — the count depends on
  which timestamp digits differ; my count is 10 for my timestamps, and
  in every case the difference is timestamp-only.

### Gate 10 — Transform reproduction (THE FIX GATE) — PASS, 8/8
- **Fix script verified, not trusted:** `scratch/fix_p6p7.py` contains
  exactly **6 asserted-literal pairs** (tuple lines counted in the file;
  per-pair code asserts old exactly 1×, 0× after, new exactly 1× after; no
  AST splicing, no repr literals in f-strings). All 6 pairs match the fix
  log's list, including the third clinic-note compression (date order)
  that the first proof's list had missed. New literals are present 1× each
  in the edition build files and old literals 0×.
- **Full documented chain** — fresh core copy + `transform_nl.py` →
  `trim_notes.py` → `fix_p6p7.py` → `freeze.py baseline` vs delivered SVGs:
  **8/8 byte-identical** (p1 `a020b7ed…`, p2 `325a2c2c…`, p3 `43a9d3b4…`,
  p4 `ef1a3ef9…`, p5 `dc47775f…`, p6 `9dc5ca46…`, p7 `19cd38d2…`,
  p8 `574203a2…` — all matching the delivered hashes and the fix log's
  pre-fix baselines). Fix run output: all 6 pairs `OK 1x`, `ALL FIX PAIRS
  APPLIED`. The chained copy's source diff vs the delivered edition build
  is **0 lines on every content/bslib/svglib file**; the only render-file
  difference is the recorded `render.py` BASE residual (see non-blocking
  note 1). The chained copy's driver run exits 0 with zero
  `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings, TOTAL 150, writing 172.
- **Transform + fix WITHOUT trim: 7/8** (p1–p7 OK; only p8 differs,
  produced `ebd21f9d…` — the untrimmed P8, exactly as the fixer claimed
  and exactly as the first proof's transform-alone run produced).
- **Ruling on the Gate 10 standard, stated explicitly:** the documented
  chain (which includes `trim_notes.py`) is the correct Gate 10 standard.
  `trim_notes.py` is a pre-existing, separately documented P8-only script
  (KIT Reproduction section; first proof's 6/8 baseline used it); neither
  `transform_nl.py` nor `fix_p6p7.py` claims P8-trim scope, so the 7/8
  without-trim result is expected and is **not** a reproduction failure.
  Any future re-run must include `trim_notes.py`. On the documented chain,
  the first proof's blocking item is closed with zero remaining gap.

### Gate 11 — All 8 cards visual — PASS
Every delivered card read in full (1950×2700 PNGs): furniture, boxes,
flows, answer blocks all present; no overflow, overlap, or missing content
on any page. Spot notes: P1 masthead/badge/footer/photo+credit clean; P2
gloss boxes + valley photo clean; P3 frost + dumpling photos clean,
mid-page white space is the core's inherited column layout; P4 2003 LAN
file photo captioned, no score chart by design; P5 popcorn photo clean;
P6 chart labels clear of bars with the shortened `Reken mee` head fitting
its column and the `Reken met de oefenmandjes.` glossline kept; P7
clinic/frame/corner/phrases/teaser all above the footer, teaser visibly
inside the page; P8 test flow + keys flow end mid-column-4 well above the
footer. P7 geometry re-measured: col3 max text baseline **1692.79**
identical core vs edition (KIT's "col3 ends 1708.1" = baseline + font
descent, consistent); teaser rect **2436.1 + 118 = ends 2554.1** identical
core vs edition, above the 2580 footer line.

## Builder/fixer claims verified (beyond the gates)
- Fix log's pre-fix baselines: my start hashes match them exactly for all
  8 SVGs, 8 cards, both PDFs, and ABSTRACT.txt (sha `2de29ed8…`).
- Post-fix byte-identity claim is corroborated independently: my
  edition-build freeze (8/8) and full-chain freeze (8/8) both reproduce
  the same hashes, so the delivered files are the fix round's files
  unchanged.
- Registry (own count of the edition build's registry dump; levels/pages/
  types/keys are trim-invariant, delivered P8 authoritative for notes):
  TOTAL **150**, A2 **56** / B1 **69** / B2 **25**, pages
  **10/18/18/18/18/18/12/38**, types 完成句子 68 / 单选 50 / 词汇配对 20 /
  完形单选 11 / 写作 1, numbers contiguous 1–150, writing model **172
  characters** (driver recount). Matches the core KIT exactly.
- Kinsoku: true closing-punctuation line starts = **0** in both core and
  edition. Traditional-only characters (raw scan set): 0 in the edition.
- English-residue marker scan over all edition text (Start of Winter /
  Beijing time / the price itself drops / goods in stock / Read page /
  Answers on page / True or false / Model answer / Editor's note / the AI
  film): **0 hits**. Remaining English-looking tokens are Dutch homographs
  (is/in/was/film/team/stage) or frozen Chinese-context tokens (S16, JD.com).
- ABSTRACT.txt: 1 line, 443 bytes, 0 ASCII double quotes, Dutch, names the
  real topics (Double 11-voorraadverkoop, Begin van de winter 7 nov., Worlds
  S16-kwartfinales, Sanxingdui AI-film, winterfilm), levels A2–B2, 150
  vragen, and a learner search phrase
  (`leer Chinees door echt Chinees nieuws te lezen`). Matches the KIT
  description; sha unchanged vs the fix log.
- Dutch adjudications from the first proof stand (not re-litigated; the
  delivered text is unchanged): `de Swiss stage` (official stage name,
  core EN usage + W43-adjacent precedent) and `Peking` / `Pekingtijd`
  (standard Dutch exonym, W43 shipped same-pairing precedent).

## Non-blocking observations (separate from the verdict — none of these block shipping)
1. `render.py` BASE residual (fixer note, confirmed): the edition build's
   `render.py` BASE was hand-repointed from the core dir to the edition
   dir (line 9), while a chained fresh copy's `render.py` BASE still points
   at the core dir (transform's OUT pair needs the `/svg` suffix, which
   `render.py` BASE lacks). Confirmed it does **not** affect Gate 10:
   `freeze.py` does not use `render.py`, and my Gate 9 regen used a scratch
   copy of `render.py` with BASE redirected. No action needed for shipping;
   a future builder may fold the BASE repoint into `transform_nl.py` for
   tidiness, but it is not required for reproduction.
2. Web-PDF regeneration SHA variance is timestamp-only (see Gate 9). No action.
3. P6 chart-label ink right edges measured here as 204.0 / 143.0 / 180.0 vs
   the builder's 203.8 / 142.6 / 180.2 and the first proof's 204.0 / 142.6 /
   180.2 — ≤0.4 px differences from integer-size font measurement. All are
   far below the 325 bar start; no label is anywhere near a bar. No action.
4. The W43 shipped edition's gloss-prefix startswith count is 11 by my node
   scan vs this edition's 10 — a W43 artifact (one extra prefixed node),
   not an edition defect: this edition's 10 matches its own 10 `gloss()`
   calls item by item (Gate 4). No action.
5. P2 gloss keeps the loanword `dumplings` for 饺子 (also the core EN
   wording); standard in Dutch food vocabulary. No change.
6. P6 keeps the glossline `Reken met de oefenmandjes.` alongside the
   shortened head `Reken mee` — intentional per the KIT (only the head was
   too wide). No change.

## Limitations (stated plainly)
- I did not re-verify the core's own trend/fact sourcing (Double 11 dates,
  S16 cutoff/scores, film figures) beyond confirming the explanation layer
  preserves them: that was the core proofread's scope, and Gate 1 proves
  the target text is unchanged (added CJK = 0). Where Dutch notes restate
  facts (dates, 270/179/160 basket maths, 1,192 miljoen yuan with Dutch
  decimal comma), I checked them against the core's numbers and found
  notation-only differences.
- Dutch adjudications rest on W43 precedent, core usage, and the first
  proof's public-usage check; I did not consult a Dutch language authority
  or style guide.
- The visual check used the delivered 1950×2700 PNG cards (the same artifacts
  that ship in the web PDF); SVG node measurements back the geometry claims.
- I did not run `insert.py`, touch `weekly-git`, or post anywhere, per the
  task's read-only constraints — repo insertion remains the coordinator's
  step after this PASS verdict.

## Files produced by this reproof
- Report (this file):
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-nl-reproof/REPORT.md`
- Scratch (all under the reproof dir, delivery untouched):
  `work/mtime1.txt`, `work/mtime2.txt`, `work/delivery-hashes-start.txt`,
  `work/baseline-core/`, `work/diff.json`, `work/occlusion.json`,
  `work/occlusion-core.json`, `work/rowcheck.py`, `work/rowcheck-out.txt`,
  `work/svg-analysis.txt`, `work/svg-analysis2.txt`,
  `work/repro-full/` + `work/repro-notrim/` (fresh core copies + scripts),
  `work/fix-run-full.txt`, `work/fix-run-notrim.txt`,
  `work/freeze-full/`, `work/freeze-notrim/`, `work/freeze-edbuild/`,
  `work/repro-full-driver.log`, `work/edbuild-driver.log`,
  `work/webregen/` (regen cards + PDFs + render log).

## PDF pins (delivered files, verified)
- Print `Lucerna-VOL2-NL.pdf`: 47,427,799 bytes, 8 pages, sha256
  `1be5629f53595f761d8648d365a200b19e16266f850ed7c580b2dfab2ccfe1cc`
- Web `Lucerna-VOL2-NL-web.pdf`: 3,208,683 bytes, 8 pages, sha256
  `6b0c0a2582fb8f6cd0483de5a6e3c409122be8048b928f9ecd300ca9ff99a9fd`
- Both match the edition KIT pins exactly and match the fix log's pre-fix
  baselines exactly. No delivery file moved during this reproof (19/19
  hashes OK at close).
