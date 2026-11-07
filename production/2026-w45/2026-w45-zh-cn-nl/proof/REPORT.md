# INDEPENDENT PROOFREAD REPORT — W45 zh-cn × nl (Simplified Chinese target · Dutch reader)

## Verdict: NOT PASS (one blocking item — Gate 10 only)

The edition's **delivered files are correct on every content gate** (Gates 1–9 and 11
all pass, listed below), and the delivered SVGs reproduce 8/8 from the edition's own
build directory with zero driver warnings. **But Gate 10, which the task marks
BLOCKING, fails:** a fresh core copy + the build's transform script(s) alone
reproduce only 5/8 SVGs (6/8 with the documented trim script). Two fix-round edits
live only as direct edits in the edition build files, not in any script — so the
script-only rebuild path produces a **defective P6 (HEAD TOO WIDE)** and a
**defective P7 (teaser off-page)**. Per the task's explicit rule ("Reproduction
failure is BLOCKING", "Only a complete round with ZERO problems finalizes it"),
this edition **must not be declared finalized** until the blocking item is closed
and Gate 10 re-verified. I did not fix anything myself, did not touch
`weekly-git`, `insert.py`, Discord, main chat, crons, or the delivery dir
(read-only except this report dir + scratch below).

**Required fix path (for the builder/coordinator, not done by this proofreader):**
fold the two direct edits itemized in §Blocking into an asserted-literal script
(e.g. extend `scratch/trim_notes.py` or add a `scratch/fix_notes.py` in the
edition build, same pattern: exact literals, per-pair assertions, applied after
`transform_nl.py`), re-render through the single driver, confirm the delivered
SVGs are byte-identical to the current delivery, then re-run Gate 10 fresh. No
content rework is needed — the delivered pages themselves are verified correct.

## Pre-flight (stand-down rule)

- At task start (07:22 UTC), delivery/build files showed writes within the last
  ~30 min (builder's final writes 07:05–07:20 UTC: SVGs 07:09, cards 07:10–07:11,
  PDFs 07:13–07:14, KIT 07:20:52). **No zh-cn-nl worker process was live**
  (only unrelated fr/pt renders). I waited, re-checked stability over 5 minutes,
  snapshot-hashed all 18 delivered files (`work/delivery-hashes-start.txt`), and
  re-verified at close: **all 18 hashes still OK** — the target did not move
  during proofreading. Proceeding was therefore safe; a strict "any write <30 min
  ⇒ stand down" reading would have blocked proofreading of any just-finished
  build, which is not the rule's intent (a moving target).
- Proof dir created by this proofreader:
  `hidden_files/w45/zh-cn-nl-proof/` (+ `work/` scratch inside it).
- All tool runs used `tools/venv/bin/python` (Python 3.12.3).

## Blocking item

### B1 — Gate 10 FAILS: transform-solo reproduction is 5/8, not 8/8
(Script-only rebuild path yields two real rendering defects.)

Method (all output redirected to my scratch, delivery never written):
fresh copy of the zh-cn core build (`hidden_files/weekly-report-w45-zhcn-build`)
→ copied the edition build's `scratch/transform_nl.py` into the copy and ran it
("ALL REPLACEMENTS APPLIED", exit 0) → `tools/freeze.py baseline` against the
delivered edition SVGs (freeze repoints OUT into scratch; it never executes the
copy against the real edition dir).

Results:
- **Transform alone: 5/8 byte-identical** (p1–p5 OK; p6, p7, p8 DIFF).
  Hashes: p6 delivered `9dc5ca46…` vs reproduced `0a961c96…`; p7 delivered
  `19cd38d2…` vs reproduced `6327707d…`; p8 delivered `574203a2…` vs
  reproduced `ebd21f9d…`.
- **Transform + `scratch/trim_notes.py`: 6/8** (p8 becomes identical; p6, p7
  still DIFF). The trim script is P8-notes-only (grep for P6/P7 strings: none).
- **P6 delta = exactly one string** (string-multiset diff, repro vs delivered):
  repro `C · 练习篮子算一算 · Reken met de mandjes` vs delivered
  `C · 练习篮子算一算 · Reken mee`. The repro driver's own log emits
  `!! HEAD TOO WIDE [P6-ex]: C · 练习篮子算一算 · Reken met de mandjes`
  (builder's measured 542.4 px > 434 px column). The delivered head measures
  399.1 px per the KIT and fits (visually confirmed on the P6 card).
- **P7 delta = exactly the builder's documented fix-round #1 compressions**
  (string-multiset diff; no other strings differ):
  clinic notes (`地 (de) markeert hoe een handeling wordt gedaan.` →
  `地 (de) markeert de manier van handelen.`; `得 (de) verbindt een werkwoord
  met een graadcomplement: 跑得快.` → `得 (de): werkwoord + graad, bijv.
  跑得快.`), frame text (`「先看评价，再下单。」(Controleer eerst de
  beoordelingen, bestel daarna.) Het patroon 先…再… geeft de volgorde van
  handelingen.` → compressed form ending `…geeft de volgorde aan.`), and the
  readers'-corner disclosure (long version ending `…publiceren wij graag in
  een volgend nummer!` → compressed 10-line version ending `…stuur ons je
  eigen brief in het Chinees!`). Geometry consequence measured directly:
  repro P7 teaser rect y=2662.16 + 118 = **ends 2780.16 — past the 2700 page
  bottom and across the footer band** (builder's first-render figure was
  2780.2); delivered teaser rect y=2436.1 + 118 = ends 2554.1, above the 2580
  footer line. Repro col3 max text y 1916.45 vs delivered 1692.79.
- **Why this is a script gap, not a content error:** `transform_nl.py` still
  contains the pre-fix strings (P6 head pair line 243 maps to
  `Reken met de mandjes`; P7 disclosure pair line 294 is the long version),
  and `trim_notes.py` contains only P8-note pairs. The P6/P7 fixes exist only
  as direct edits in the edition build's `content56.py` (line 217 `Reken mee`)
  and `content7.py` (line 91 compressed disclosure). The brief's filename
  `transform.py` does not exist; the actual scripts are
  `scratch/transform_nl.py` + `scratch/trim_notes.py`.
- **Counter-evidence that the DELIVERED files are not hand-patched:**
  `freeze.py baseline` of the edition build itself against the delivered SVGs
  = **8/8 byte-identical**, and a direct driver run of the freeze-repointed
  edition-build copy emits **zero** `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings
  with registry TOTAL 150, A2 56 / B1 69 / B2 25, pages 10/18/18/18/18/18/12/38.
  So the failure is confined to the core→edition script path, and the fix is
  scripting-only (no page needs re-editing).

## Per-gate evidence (all other gates PASS)

### Gate 1 — Freeze baseline 8/8 + freeze diff, strict-CJK 0 — PASS
- `freeze.py baseline` (core build → scratch): **8/8 byte-identical** to shipped
  core SVGs; core SVGs re-hashed unchanged afterwards (hashes match the
  builder's `core-svg-hashes-before.txt` exactly, e.g. p1
  `e057bbfc…`, p8 `eaf368f8…`).
- `freeze.py diff --strict-cjk` core vs edition: added CJK **0 on every page,
  TOTAL 0**, exit 0. Net CJK per page matches the builder's figures exactly:
  p1 851→820 (−31), p2 1053→1031 (−22), p3 812→790 (−22), p4 810→789 (−21),
  p5 944→921 (−23), p6 1005→983 (−22), p7 760→739 (−21), p8 1102→1082 (−20).
- Added/removed-string audit (full `work/diff.json` read): every added string
  containing CJK is paired 1:1 with a removed counterpart carrying the same
  Chinese head/word (gloss citations, bilingual furniture with the Chinese half
  frozen, P8 keys with identical Chinese keys, quoted examples) — only the
  explanation language changed EN→NL. No new target text. Added strings without
  CJK are Dutch prose/furniture. No added-CJK item needed adjudication.

### Gate 2 — p8.py compare vs core — PASS (CLEAN, style verified from code)
- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-nl --target zh-cn`:
  **core 150 noted, edition 150 noted, status CLEAN, missing=[], extra_count=0,
  uncertain=[], keydiff=[]**. No keydiff item to verify from SVG nodes (none).
- Style verified from the core's shipped fan-out BUILD CODE, not memory: core
  build `content8.py` lines 119/121 generate `f"{e_['n']}. {e_['key']} — {e_['note']}"`
  and writing `f"{e_['n']}. ✓ {e_['note']}"` — dash style. Edition build keys
  loop is identical except furniture strings (headers, `— Pagina N —`
  separators, writing gloss/key/note translations). `MODELO`/`NCHARS`
  computation line is identical; writing key
  `(open vraag — voorbeeldtekst hieronder)` / note `Open vraag —
  voorbeeldtekst hierboven in deel F, {NCHARS} tekens` / label
  `Voorbeeldtekst: ` match the KIT (trimmed form). `bslib4.py` diff vs core
  build: only footer line + gloss prefix (`Notes｜` → `Uitleg — `) changed.
  `svglib.py`: byte-identical. No paren/dash conversion excuse was invoked or
  needed (README notes #8/#14 complied with by code inspection).
- P8 post-trim state verified from the delivered SVG: **151 wrapped key lines**
  (159 keys-area text nodes − 8 `— Pagina N —` separators), max keys y
  2530.35 < 2540 flow bottom — overflow gone; #135
  `135. 数字 — shùzì — AI-filmpersonages zijn digitaal.` and #140
  `140. 立减 — lìjiǎn — afgetrokken bij het afrekenen.` present verbatim;
  8/8 sampled trim NEW wordings present in the delivered P8 text, OLD wordings
  absent (incl. the #150 `{NCHARS}` placeholder form). Keys unchanged:
  `p8.py` keydiff=[] proves it for all 150.

### Gate 3 — Occlusion audit + same-baseline scan + P6 chart-label check — PASS
- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire once, clean
  controls silent). Edition audit: **0 flags**. With `--core`: core 0 flags,
  **NEW vs core: 0**.
- Same-baseline ink-collision scan (builder's `rowcheck.py` copied to my
  `work/` and re-run read-only against the edition SVGs, PIL true-ink boxes,
  SC face index 2): **0 flags across all 8 pages, including the P1 top band**.
- P6 chart-label element check (README note #12 graze class): bars x=325,
  widths 810/537/480 (rows A/B/C, 3.0 px/yuan) confirmed from SVG rects;
  row-label ink right edges 204.0/142.6/180.2 (builder claimed 203.8/142.6/180.2;
  ≤0.2 px rounding from integer-size font measurement — all < 325 bar start);
  value labels at bar end + 16 px exactly (270 at 1151 = 1135+16; 179 at 878 =
  862+16; 160 at 821 = 805+16); **zero later-drawn rects overlap any of the 6
  chart-label ink boxes** (paint-order intersection test). No clipped label,
  including below the 30% COVER threshold.

### Gate 4 — Gloss counts (split on `·` itself) — PASS
- Source `f.gloss("…")` strings, split on `·`: core
  [4,4,4,3,3,3,3,3,3,3] (total 33), edition identical item by item, with the
  same Chinese heads in the same order (现货/立减/直降/节气; 仓库/评价/尺码/
  退换货; 补冬/饺子/糍粑/期中; 候/交替/采访; 厚衣服/热饭/着凉; 淘汰/内战/止步;
  数字形象/公映/票房; 火化/救赎/以后; 结算/运费/广告; 说法/数据/退换货).
- Rendered gloss boxes in the SVGs: core 1/2/2/1/2/2 = 10, edition 1/2/2/1/2/2 =
  10, prefix `Uitleg — ` on every edition box. (An early `grep -c` read of 6
  was a multi-node-line artifact; the node-level count is 10.)

### Gate 5 — P7 golden sentences — PASS (all 8 ×2, correct page tags)
Punctuation-stripped contiguous counts in the delivered SVGs (article page +
P7, matching the core's totals exactly): 「不用等11月11日」 p.1, 「下单就能发货」
p.2, 「先看结算页，再付款」 p.2, 「水开始结冰」 p.3, 「三场都输了」 p.4,
「小局一场没赢」 p.4, 「故事够不够好」 p.5, 「别以后，就现在」 p.5 — each
exactly 2×. P7 renders the full-width-punctuation forms verbatim. Core
adjudications inherited only where frozen text is byte-identical (it is — see
Gate 1); the P7 phrase block itself is frozen Chinese.

### Gate 6 — Images — PASS
- `<image>` counts core vs edition identical: **1/1/2/1/1/0/0/0 = 6 photos**.
- Payload MD5s core == edition on every page and equal to the edition-build
  asset files: locker `420c6150…`, valley `550e463b…`, frost `d0b015bc…`,
  dumplings `e8d75277…`, lanparty `6b8e9037…`, popcorn `a903e35f…`.
- Credit lines in the delivered SVGs match the Commons API Artist field in
  `assets/CREDITS.md` (byte-identical CREDITS file core build vs edition
  build): `Foto: Map hobby — CC0`, `Foto: Paul Gilmore — CC0`,
  `Foto: Gerda Arendt — CC0`, `Foto: Syced — CC0` (×2), `Foto: Based5290 —
  Publiek domein`. Only the label was translated (`Photo:` → `Foto:`;
  `Public domain` → `Publiek domein`); authors/licences unchanged. ("Map hobby"
  is the genuine Commons Artist value for the locker photo, not an error.)
  File photos stay captioned 资料图 and are never presented as this week's
  event; the P4 LAN caption states 2003/France.

### Gate 7 — Readers' corner — PASS (disclosure + explicit invitation, verbatim)
P7 col x=1473, y-identical to the core at every line:
- Frozen Chinese letter (3 lines, y 1315.6–1376.66) and frozen Chinese
  disclosure sentence (6 lines from y 1437.19, incl. 编辑部示例信,不是真实来信…
  延期不是取消。) — byte-identical nodes.
- Dutch disclosure (5 lines, y 1579.19–1692.79): `Redactie: VOL.1 beloofde
  echte brieven in VOL.2. Die zijn er nog niet, dus een voorbeeldbrief.
  Uitgesteld, niet afgesteld — stuur ons je eigen brief in het Chinees!`
  — states no genuine letters exist (labelled editor's example + deferral)
  AND carries the explicit open invitation **`stuur ons je eigen brief in het
  Chinees!`** verbatim on P7. The whole disclosure block is exactly the core's
  10 wrapped lines (y 1437.19–1692.79, shared Chinese/Dutch line at 1579.19);
  the builder's P7 teaser fix did not damage it. A teaser line or another
  page's exercise prompt was not counted (none needed — the invitation is in
  the corner itself).

### Gate 8 — Furniture three-way + badge-slot adjudication — PASS
Measured from SVG nodes (x, y, size, weight, fill), not from memory:
- **Badge slot — builder's case RULED CORRECT on evidence.** Core badge:
  (975, 434), 19.5pt, weight 700, OLIVE #3e4c2a, Chinese/English string. The
  y=372 line in the core is the frozen bilingual strapline
  `给学中文的人的周报 — Read the real China, in Chinese` (19pt, not a free
  slot). W43 shipped zh-cn-nl badge: (975, 434), 19.5pt, 700, BRICK #a4553a,
  Dutch string. This edition badge: **(975, 434), 19.5pt, 700, BRICK #a4553a,
  string byte-identical to W43** (`TEKSTEN IN HET CHINEES (VEREENVOUDIGD) ·
  UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`). This
  is an in-place replacement at the zh-cn core family's own slot: neither the
  EN subtitle-slot case (372/19.5pt) nor the FR/IT inserted-badge case
  (574/22pt) applies — no badge node exists at y=574, and y=372 remains the
  strapline in all three (core EN half → W43/edition Dutch half
  `Lees het echte China, in het Chinees`; Chinese half frozen). The y=92 top
  strip likewise takes W43's Dutch half (`Lees echt Chinees, elke week`).
  The P1 edition line stays Chinese (`简体中文版 · VOL.2 · 双11 · 立冬 · S16`),
  per the W43 precedent.
- Footer (all 8 pages): `Lucerna · CHINEES WEEKBLAD VOL.2 · TEKSTEN IN HET
  CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS` — W43 string with the
  justified pair-varying change VOL.1→VOL.2 (this issue's number).
- Page line: `Pagina N van 8`, 8/8 pages. Gloss prefix: `Uitleg — ` (10
  boxes). P8 separators: `— Pagina N —`, 1–8 all present in order.
- Masthead: bare `Lucerna` blackletter, no article (Chinese is article-less
  per the SOP) — confirmed on the P1 card.

### Gate 9 — Web PDF regeneration — PASS (with one documented timestamp variance)
- Regenerated in my scratch from the delivered SVGs via the build's `render.py`
  (BASE repointed to scratch only): **cards 8/8 byte-identical** to delivered
  cards; **print PDF byte-identical** to delivered (47,427,799 bytes, sha256
  `1be5629f53595f761d8648d365a200b19e16266f850ed7c580b2dfab2ccfe1cc` =
  KIT pin).
- Web PDF: delivered file verified **8 pages, 3,208,683 bytes (< 10 MB),
  sha256 `6b0c0a2582fb8f6cd0483de5a6e3c409122be8048b928f9ecd300ca9ff99a9fd`
  = KIT pin**. The regenerated web PDF is the same size (3,208,683 bytes) and
  8 pages but a different SHA (`af16fcd1…`): byte-diff shows **exactly 6
  differing bytes, all inside PIL's `/CreationDate` / `/ModDate` timestamps**
  (delivered `20261028071404Z` = builder's render time; regen
  `20261028073413Z` = my render time). All image content is identical. This
  is inherent PIL PDF-writer wall-clock metadata, not a content defect, and
  does not break the KIT pin (which describes the delivered file, verified
  above). (An earlier failed regen attempt was my own sed mangling of the
  BASE line; it wrote nothing to delivery and was redone cleanly.)

### Gate 11 — All 8 cards visual — PASS
Every delivered card read in full (1950×2700 PNGs): furniture, boxes, flows,
answer blocks all present; no overflow, overlap, or missing content on any
page. Spot notes: P1 masthead/badge/footer/photo+credit clean; P4 has no score
chart by design with the 2003 LAN file photo captioned; P6 chart labels clear
of bars with the shortened `Reken mee` head fitting its column; P7 clinic/
frame/corner/phrases/teaser all above the footer; P8 test flow + keys flow end
mid-column-4 well above the footer. Mid-page white space on P3/P5 is the core's
inherited column layout, not missing content.

## Builder claims verified (beyond the gates)
- P7 geometry: col3 max text y 1692.79 identical core vs edition; teaser rect
  2436.1 + 118 = ends **2554.1** identical core vs edition, above the 2580
  footer line. (Absolute "col3 ends 1708.1" = 1692.79 + font descent; equality
  is what was verified, plus the teaser end itself.)
- P8 post-trim: 151 wrapped key lines, overflow gone (see Gate 2); #135/#140
  Dutch notes present/correct; 14 compressed notes keep facts/keys unchanged
  (keys proven by keydiff=[]; 8/8 sampled NEW wordings present, OLD absent).
- Dutch adjudications — both ACCEPTED, not errors:
  - `de Swiss stage`: the official LoL stage name, used 10× in the core's own
    English layer and 12× consistently in this edition; Benelux LoL coverage
    (Leaguepedia Road of Legends, a Dutch/Benelux league) likewise uses
    "Swiss Stage" as the stage name. A calque ("Zwitserse ronde") would be
    wrong for the official name. (No W43 precedent exists — W43's topic was
    not esports — so this rests on core usage + public usage, stated plainly.)
  - `Peking` / `Pekingtijd`: standard Dutch exonym; W43 shipped same-pairing
    precedent uses `Pekingtijd` (10 `Peking` occurrences in the W43 shipped
    SVGs, incl. `Reken de tijden om naar Pekingtijd.`). Edition usage is
    consistent (11× `Peking`, 9× `Pekingtijd`, incl. `Xiao Hong woont in
    Peking.` for the frozen key 北京).
- Inherited core traits confirmed against the core (not introduced here): P4
  has no score chart (wide-rect lists identical core vs edition — boxes only);
  6 photos (see Gate 6); B2 share 25/150 (registry below); P8 top-rule
  proximity — test flow ends y 1225.14 (core 1232.70), both below the keys
  rule at y=1264 with the keys header at 1302; the edition is marginally less
  tight than the core, and the canonical audit reports no flag.
- Registry (edition `reg-nl.json`, pre-trim dump — levels/pages/types/keys are
  trim-invariant; delivered P8 is authoritative for notes): TOTAL **150**,
  A2 **56** / B1 **69** / B2 **25**, pages **10/18/18/18/18/18/12/38**, types
  完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1 (note: the task
  brief's "词语配对" vs the registry's "词汇配对" is a wording variant for the
  same matching type — counts match the core KIT), numbers contiguous 1–150,
  writing model **172 characters** (recounted from the delivered P8 SVG model
  nodes, spaces stripped). Matches the core KIT exactly.
- Final-render warnings: the delivered edition-build driver run emits **zero**
  `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings (see Blocking counter-evidence).
  The script-only rebuild run emits the P6 HEAD TOO WIDE warning — that is
  part of the blocking item, not a delivered-file defect.
- Kinsoku: true closing-punctuation line starts = **0** in both core and
  edition. Two edition nodes start with `·` (p2/p3 gloss-wrap continuations);
  these are separator continuations, not closers (core has 4 of the same
  form) — adjudicated non-defects. Traditional-only characters: 0 in the
  edition text (and freeze added-CJK = 0 already proves no new Chinese chars).
- English-residue marker scan over all edition text nodes (Start of Winter /
  Beijing time / the price itself drops / goods in stock / Read page /
  Answers on page / True or false / Model answer / Editor's note / the AI
  film): **0 hits**. Remaining English-looking tokens are Dutch homographs
  (is/in/was/film/team/stage) or frozen Chinese-context tokens (S16, JD.com).
- ABSTRACT.txt: 1 line, 443 bytes, 0 ASCII double quotes, Dutch, names the
  real topics (Double 11-voorraadverkoop, Begin van de winter 7 nov., Worlds
  S16-kwartfinales, Sanxingdui AI-film, winterfilm), levels A2–B2, 150 vragen,
  and a learner search phrase (`leer Chinees door echt Chinees nieuws te
  lezen`). Matches the KIT description.

## Non-blocking observations (separate from the blocking item — none of these block shipping)
1. Web-PDF regeneration SHA variance is timestamp-only (see Gate 9). No action.
2. The brief's Gate-10 filename `transform.py` does not exist; the real scripts
   are `scratch/transform_nl.py` + `scratch/trim_notes.py`. The coordinator may
   want the brief corrected, but this alone would not block anything — the
   blocking item is the missing P6/P7 script pairs, not the filename.
3. P2 gloss keeps the loanword `dumplings` for 饺子 (also the core EN wording);
   standard in Dutch food vocabulary. No change.
4. P6 keeps the glossline `Reken met de oefenmandjes.` alongside the shortened
   head `Reken mee` — intentional per the KIT (only the head was too wide).
5. The task brief's registry line "A2 56/B1 75…" self-corrects mid-sentence to
   B1 69; verified B1 = 69. No action.

## Limitations (stated plainly)
- I did not re-verify the core's own trend/fact sourcing (Double 11 dates, S16
  cutoff/scores, film figures) beyond confirming the explanation layer preserves
  them: that was the core proofread's scope, and Gate 1 proves the target text
  is unchanged. Where Dutch notes restate facts (dates, 270/179/160 basket
  maths, 1,192 miljoen yuan with Dutch decimal comma), I checked them against
  the core's numbers and found notation-only differences.
- Dutch adjudications rest on W43 precedent, core usage, and one public web
  search (Benelux LoL "Swiss Stage" usage); I did not consult a Dutch language
  authority or style guide.
- The visual check used the delivered 1950×2700 PNG cards (the same artifacts
  that ship in the web PDF); SVG node measurements back the geometry claims.
- I did not run `insert.py`, touch `weekly-git`, or post anywhere, per the
  task's read-only constraints — repo insertion remains the coordinator's step
  after a PASS verdict.

## Files produced by this proofread
- Report (this file):
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-nl-proof/REPORT.md`
- Scratch (all under the proof dir, delivery untouched):
  `work/delivery-hashes-start.txt`, `work/baseline.json`, `work/diff.json`,
  `work/occlusion.json`, `work/occlusion-core.json`, `work/rowcheck.py`,
  `work/webregen/` (regen cards + PDFs), `work/repro/` (fresh core copy +
  transform, then trim), `work/reproA.json` (transform-alone 5/8),
  `work/reproB.json` (transform+trim 6/8), `work/reproA/` + `work/reproB/` +
  `work/edbuild/` (freeze outputs), `work/edbuild-driver.log` (0 warnings),
  `work/reproB-driver.log` (P6 HEAD TOO WIDE line).

## PDF pins (delivered files, verified)
- Print `Lucerna-VOL2-NL.pdf`: 47,427,799 bytes, 8 pages, sha256
  `1be5629f53595f761d8648d365a200b19e16266f850ed7c580b2dfab2ccfe1cc`
- Web `Lucerna-VOL2-NL-web.pdf`: 3,208,683 bytes, 8 pages, sha256
  `6b0c0a2582fb8f6cd0483de5a6e3c409122be8048b928f9ecd300ca9ff99a9fd`
- Both match the edition KIT pins exactly. The coordinator must NOT insert
  until the blocking item is closed and Gate 10 re-verified — the pins above
  describe the current delivery, which will be unchanged if the fix is
  scripting-only (re-verify hashes after any rebuild).
