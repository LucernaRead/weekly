# INDEPENDENT PROOFREAD — W45 ZH-TW × ES (Traditional Chinese target · Spanish reader)

## VERDICT: PASS with ZERO PROBLEMS

All 16 gates below were re-run independently from the shipped files
(not trusted from the builder KIT). No blocking item was found.
This report is the finalization evidence for the coordinator's insert step.
This proofreader fixed nothing, touched `~/workspace/weekly-git` never,
ran no `insert.py`, posted nothing to Discord or to the main chat,
created no cron, spawned no subagent, and declares nothing shipped —
insertion is the coordinator's step.

Edition: `files/weekly-report-w45-zh-tw-es/` — svg ×8, cards ×8 (1950×2700),
print PDF, web PDF, `WEEKLY-KIT.md`, `ABSTRACT.txt`.
Core: `files/weekly-report-w45-zhtw-core/` (KIT read first).
Build: `hidden_files/weekly-report-w45-zh-tw-es-build/` +
transform `hidden_files/weekly-report-w45-zh-tw-es-transform.py`.
W43 same-pairing reference: `files/weekly-report-zh-tw-es/` (+ its shipped
build `hidden_files/weekly-report-zhtw-es-build/`).
Tools: `tools/` venv python, `freeze.py`, `p8.py`, `occlusion_audit.py`.
Proof work: this dir (`REPORT.md` + `work/`).

## 0. Pre-flight duplicate check — PASS, proceeded

- (a) No live worker/process was writing to the delivery or build dirs
  at start: `ps` showed only an unrelated sibling snapshot watcher for
  the zh-tw-it proof (different edition, no es-dir writes) and no
  `run.py`/`render.py`/`transform`/`freeze`/`occlusion` process for es.
  The builder session had completed (delivery last written 09:04–09:05,
  KIT status "BUILT, NOT finalized — awaiting independent proofread").
- (b) mtime snapshots of both dirs: `work/mtime1.txt` (09:11),
  `work/mtime2.txt`, `work/mtime3.txt`, `work/mtime-final.txt` —
  diff ZERO across the whole proof (first to final).
- (c) Builder session completed (see above). No stand-down was needed.
- No stray nested tree in or under the delivery/build dirs: only
  `svg/` and `cards/` (delivery) and `__pycache__`/`assets/` (build).
  The builder's Gate-10 replay dir `hidden_files/w45-zh-tw-es-gate10`
  sits outside both dirs and is the final clean replay's residue.

## 1. Freeze baseline + strict-CJK diff — PASS

- `freeze.py baseline` (own scratch `tools/scratch/baseline-w45-zhtw-es-proof`):
  **8/8 byte-identical** to the shipped core SVGs; core re-hashed unchanged
  by the run. Core hashes match the builder KIT §1 pins exactly
  (p1 `4672c972…`, p2 `889fb533…`, p3 `508703c2…`, p4 `e04b62ea…`,
  p5 `4dfce72d…`, p6 `06ba4c66…`, p7 `00ac7f57…`, p8 `e6e97d02…`).
- `freeze.py diff --strict-cjk` (`work/freeze-diff.json`): added CJK = **0**
  on all 8 pages, per-page CJK counts reproducing the builder's §6 exactly
  (P1 952→920, P2 1018→996, P3 1088→1065, P4 831→809, P5 1101→1079,
  P6 942→921, P7 808→788, P8 1114→1092; TOTAL added CJK = 0).
  Decreases are only the old Chinese badge/footer furniture.
- Zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the Gate-10 replay
  (see gate 4).

## 2. Traditional independence — HARD GATE — PASS

- Re-extracted from the shipped SVGs themselves (every `<text>` node,
  CJK range U+4E00–U+9FFF): union of (W43 zh-tw-es shipped SVGs) +
  (W45 zh-tw core shipped SVGs) = **1024** distinct characters;
  this edition = **766**; edition characters outside the union = **NONE**
  — exactly the builder's claimed numbers, independently reproduced.
- Simplified-only spot list over edition text: 邮 说 国 龙 马 发 = 0 hits
  each. (台 occurs 49×, but 台 is a legitimate Taiwan variant present in
  the core and the union, not a Simplified-only character.)
- Transform audit: `weekly-report-w45-zh-tw-es-transform.py` imports only
  `os, re, shutil, subprocess, sys, hashlib` — **no OpenCC, no s2t/t2s,
  no mapping table** (the only "convert" mention is a code comment about
  the svglib `_fw` full-width conversion, not a script conversion).
  OpenCC is not installed on this VM (consistent with the builder's note);
  the union cross-check + strict-CJK=0 above are the standing evidence,
  both re-verified here.
- All 288 count-asserted transform pairs audited: 121 contain CJK in the
  old string; only 4 change the CJK sequence, and all 4 are adjudicated
  furniture/registry (footer, page line, badge line, #150 key) — see gate 3.

## 3. Target text zero difference (run level) — PASS

- The transform-pair audit above proves no Chinese string is altered
  except the 4 adjudicated items; the other 117 CJK pairs preserve the
  CJK sequence character-for-character (bilingual heads keep their
  Chinese half; only the English/Spanish half changes).
- Removed-string audit (`work/freeze-diff.json`): every removed
  CJK-containing string is either old furniture (footer/badge/page lines/
  bilingual heads with an English second half) or an English explanation
  string citing Chinese terms (P7 columns, P8 notes — whose Chinese keys
  reappear in the edition with Spanish notes). No article, question,
  option, or key string is removed.
- Registry-dump diff (fresh core copy vs fresh edition copy, one-process
  driver each; `work/reg-core.json`, `work/reg-ed.json`, redo-verified
  identical): the ONLY structural/key change is **#150**
  `(開放題,範文如下)` → `(pregunta abierta — modelo a continuación)`.
  Notediff 150/150 (all notes rewritten in Spanish, as designed).
- Writing model printed verbatim in P8 section F, identical text
  core-vs-edition, **138 characters** (no-space count) both sides;
  only the label changes (`Model answer:` → `Respuesta modelo:`) and
  the wrap point shifts accordingly.

## 4. Gate 10 — REPRODUCTION — PASS (blocking gate, clean)

- Builder's transform `--gate10` mode re-run by this proofreader:
  fresh core copy + transform ALONE + one-process driver →
  **8/8 byte-identical to the delivered SVGs, warnings=0, exit code 0**,
  registry re-confirmed 150 / A2 44 / B1 74 / B2 32 /
  pages 10/18/18/18/18/18/12/38 / types 單選 67 / 完成句子 54 / 配對 16 /
  完形單選 12 / 寫作 1.
- The transform's Gate-10 code replaces the WHOLE `OUT` assignment
  (regex over the full `expanduser(...)` assignment, `assert n == 1`
  per file) — the builder's disclosed first-run doubled-prefix bug is
  fixed in the current script, and no stray nested tree remains in or
  under the delivery/build dirs (see §0).

## 5. p8.py — CLEAN

- Explicit-path form (tables.json's default P8 filename does not match
  this core's `p8-test.svg`, as the builder noted):
  `p8.py compare --core-p8 …/core/svg/p8-test.svg --edition-p8 …/es/svg/p8-test.svg --total 150`
  → **CLEAN, 150 noted = 150 noted, missing=[] extra_count=0,
  uncertain=[], keydiff=[]** (the #150 writing key is excluded from
  keydiff by the tool's writing-item rule; §3 records it).
- `p8.py extract` on the edition P8: noted set = 150/150, items 1–150
  all present.

## 6. P8 paren style + AI-variant trap — PASS (critical family gate)

- Paren verified from the W43 zh-tw-es column's OWN shipped build code
  (`hidden_files/weekly-report-zhtw-es-build/content8.py` lines 114–132:
  key lines only bypass the svglib `_fw` pair rule, restored after the
  keys flow) AND from this edition's shipped build code (identical
  bypass, same `N. key (note)` / `N. ✓ (note)` format, separators
  `— Página N —`) AND from the shipped P8 SVG (all 8 separators
  `— Página 1 —` … `— Página 8 —` present).
- Printed P8 key lines contain **ZERO full-width parentheses**
  (188 numbered key lines scanned). Precision note on the task's wording:
  the P8 SVG as a whole contains 11 full-width paren pairs, but every one
  sits inside frozen Traditional target text (true/false items, passage,
  fill-ins) — the same class as W43 zh-tw-es's 12. No key line, note, or
  explanation string carries a full-width paren. This is NOT a deviation.
- AI TRAP — both forms verified against the core and W43 zh-tw-es:
  - Core P8 key 88 note: `AI helps read data, spot risks and answer clients.`
    → edition P8 key 88: `La IA ayuda a leer datos, detectar riesgos y
    responder a los clientes.` — TRANSLATED.
  - Core P8 key 138 note: `AI inside finance is 人工智慧＋.`
    → edition P8 key 138: `138. 人工智慧 (La IA dentro de las finanzas es 人工智慧＋.)`
    — TRANSLATED, with the Chinese term 人工智慧＋ kept verbatim
    (including full-width ＋).
  - The P6 gloss is likewise fully Spanish (`Tres signos más: Finanzas+…
    IA+ (inteligencia artificial dentro de bancos, inversiones y seguros)…`).
  - No P5 AI form exists (full P5 node scan: no AI string) — nothing to
    translate there.
  - Adjudication vs W43 zh-tw-es (NOT the zh-tw-it pinyin rule):
    W43 zh-tw-es's shipped P8 key 138 is
    `138. 留友 (留友看 — guardarlo para que lo lean los amigos.)` —
    it keeps its Chinese term verbatim in key and note, in half-width
    paren style. The W45 es verbatim-keeping of 人工智慧＋ is therefore
    CONSISTENT with this column's own precedent, adds no new CJK
    (strict-CJK=0, union outside=0), and is NOT blocking.
- No raw `\bAI\b` token remains anywhere in the edition SVGs.

## 7. Occlusion audit + P7 fixes — PASS

- `occlusion_audit.py --selftest`: OK (all 6 planted classes fired,
  clean controls silent) before every run.
- Edition **0 flags**; core **0 flags**; **NEW vs core: 0**
  (`work/occlusion-ed.json`, `work/occlusion-core.json`,
  `work/occlusion-new.json`).
- Chart-label geometry: P4 brick bars (x=280; y=1204 w=120.0 h=28;
  y=1404 w=600.0 h=28) and P6 olive bars (x=280; y=962/1014/1066/1118,
  w=600.0/800.0/800.0/800.0 h=34) are **exactly identical** to the core's
  audited geometry; chart labels and notes render fully on the cards
  (P4 runs-by-inning, P6 hours-by-day) with no graze visible.
- Same-baseline furniture check (targeted, PIL TC metrics): footer
  left/right strings at y=2624 on all 8 pages — gap **604.7px**, no
  collision. (A first hand-rolled same-baseline/graze scan produced
  systematic false flags — e.g. "Completa" instruction labels flagged
  against questions on different baselines — contradicted by direct SVG
  inspection, the canonical audit's 0 flags, and the cards; it was
  discarded as a measurement artifact and is NOT relied on here.)
- P7 teaser fix holds: teaser band rect y=2414.86 h=118 → bottom
  **2532.86**, footer rule 2580 → clear by 47.14px; confirmed on the
  P7 card (band well clear of the footer line).
- P7 readers'-corner box containment holds: box rect x=1451 y=1154.36
  w=434 h=580.5 → bottom 1734.86; last Spanish disclosure line baseline
  y=1721.13 (20pt, ink bottom ≈1727) → inside with margin; confirmed on
  the P7 card (last line `…la invitación sigue abierta.` sits inside
  the box with space below). The +20px pad vs the core's ~11px `lh`
  underestimate is visible and effective; the core's own geometry was
  not reproduced, as the builder disclosed.

## 8. Gloss / match counts + registry — PASS

- Gloss boxes per page, edition = core, item by item: P1 [1,1], P2 [1,1],
  P3 [1,1,1], P4 [1,1], P5 [1,1], P6 [1] — total **12** (rendered
  `Nota —` first-lines per page: ed [2,2,3,2,2,1,0,0] = core
  `Notes｜` first-lines [2,2,3,2,2,1,0,0]; gloss() call counts in the
  build sources also match per file). The zh-cn core's 33 does NOT apply
  here; the zh-tw core's true count is 12.
- Registry (Gate-10 replay + registry dumps): **150**; A2 44 / B1 74 /
  B2 32; types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1;
  pages 10/18/18/18/18/18/12/38; writing model 138 chars (see §3).

## 9. P7 golden sentences — PASS

- All 8 verbatim from this issue's own articles, exactly **2× each**
  issue-wide (article + P7, bare-sentence count over concatenated SVG
  text nodes), in both edition and core: 用手機轉帳…金融科技 (p. 1),
  123個國家及城市、1,600個攤位 (p. 1), 需要才買… (p. 2),
  在高雄，鋼鐵也能變成舞台 (p. 3), 福隆的夏天…10月26日… (p. 3),
  6比0完封兄弟…紅色彩帶 (p. 4), 250家店家一起討糖 (p. 5),
  旅展首日中午12點才開門 (p. 6).
- Page tags on the P7 card: p. 1, 1, 2, 3, 3, 4, 5, 6 — correct.
  No S.-form expected (that is zh-tw-de's form, not this column's).

## 10. Images — PASS

- Per-page payloads byte-identical to the zh-tw core (base64 payload
  hashes): P1 harbour, P2 rain, P4 baseball, P5 pumpkin — 4 payloads;
  P3/P6/P7/P8 carry no photos, as in the core.
- Credits verbatim in the SVGs: `Photo: Wilfredor — CC0 (Wikimedia
  Commons)`, `Photo: CorraleH — CC0 (Wikimedia Commons)`,
  `Photo: Bain News Service — Public domain (Wikimedia Commons)`,
  `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)` — matching the
  core KIT's Commons Artist-field table.
- P4 provenance: NOT re-litigated. Placed bytes and credit line are
  unchanged from the core, so the core KIT's 2026-10-27 CLOSED
  adjudication binds (dual build-record evidence + byte identity to
  the W43 Korean build's verified file). A fresh Commons page text
  fetch for the P4 file was attempted once and returned HTTP 403
  (same as the coordinator's prior attempts) — an ambiguous fetch
  failure, not evidence of absence, and not retried; per the binding
  adjudication it does not block. See Limitations.

## 11. Readers' corner — PASS

- Frozen Traditional disclosure line-for-line identical to the core
  (all 5 wrapped nodes match exactly, including
  `延期披露：VOL.1曾預告本期起刊登真實…你的來信，下一期見。`).
- Spanish disclosure states no genuine letters exist and the invitation
  stays open: `Carta de ejemplo de la redacción, no una carta real.
  Aviso: el VOL.1 prometió cartas reales y la mejor redacción de la
  página 8 desde este número; al cierre no había ninguna publicable,
  así que el ejemplo se mantiene y la invitación sigue abierta.`
  The letter itself is labeled an editor's example in both languages.
- W43 precedent nuance (stated, not a deviation): W43 zh-tw-es's Spanish
  corner reads `¡El VOL.2 publicará cartas reales de lectores y la
  mejor redacción de la página 8!` because W43 (VOL.1) had no deferral
  to report. W45's deferral wording cannot be verbatim-identical to
  W43's forward promise — the situation differs — but it carries the
  same column elements (labeled example + Spanish disclosure + open
  invitation, here as `la invitación sigue abierta`), which is what
  gate 11 requires.

## 12. Furniture three-way — PASS

- Badge MEASURED from the shipped P1 SVG tags (byte-for-byte):
  - Core: `<text x="975" y="378" … font-size="21" font-weight="700"
    fill="#3e4c2a" text-anchor="middle">繁體中文正文 · 英語講解 …`
  - W43 zh-tw-es: same tag with `fill="#a4553a"` and the Spanish badge
    string.
  - This edition: tag **identical to W43** (x=975, y=378, 21pt, 700,
    BRICK #a4553a, middle anchor, same Spanish string).
  - PIL TC Bold widths: core badge 1227.3px, edition/W43 badge 1248.4px —
    confirming the builder's 1227/1248 figures.
  - Ruling confirmed: the zh-tw core HAS a native badge slot at y=378,
    so the badge replaces the core's badge line in place at 21pt BRICK —
    exactly the W43 zh-tw-es precedent, in the core's own slot (OLIVE →
    BRICK). Not the FR/IT inserted-slot case (y=574), not a 19.5pt
    subtitle-slot case. Masthead otherwise frozen (wordmark, edition
    line, strapline y=410).
- Footer (all pages): `Lucerna · SEMANARIO CHINO TRADICIONAL VOL.2 ·
  TEXTO EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL` /
  `Página N de 8` — VOL.2-adapted Spanish form (W43 used VOL.1), correct.
- Gloss prefix `Nota — `; P8 separators `— Página N — `; section heads
  bilingual `中文 · Spanish` throughout; `Completa` (fill-in),
  matching per set (`Une palabra y definición`, `Une nombre y dato`,
  `Une evento y dato`), `Redacción` (writing) — all as claimed.
- Discrepancy rule honored: shipped W43 wins over tables.json;
  tables.json was NOT edited (its P8-filename mismatch is recorded as a
  non-blocking note, §Non-blocking).

## 13. Residual Latin — PASS

- Independent scan: whole-word English-prose word list
  (the/and/with/from/this/that/work/words/baseball/…) over all edition
  text nodes → only hit is `the` ×2 on P1, both inside the frozen theme
  name `Fintech Nexus: Bridging the World, Building the Future`
  (target text, adjudicated). No English explanation prose remains.
- Sweep fixes hold: P3 head is `算一算 · Calcula` (bilingual head form,
  consistent with the edition's bilingual-head rule — the English
  residue `Work it out` is gone); P4 head is `棒球詞卡 · Palabras de
  béisbol` (wraps to 2 lines; clean on the card, see §15).
  No `Work it out` / `Baseball words` string remains anywhere.
- Remaining Latin is only: the Spanish layer; frozen target-text names
  (Fintech Nexus theme, StartmeupHK 2026, ITF, SUPER STAGE, SOLID TIDES,
  JUMP, Trick or Treat, Wei Chuan Dragons, CTBC Brothers, C.C. Mercedes,
  Jurassic World/Shrek/Kung Fu Panda, MVP, Tamagotchi, Halloween);
  credits; masthead `Lucerna`, `VOL.2`, chips `A2/B1/B2`, option/match
  letters, page tags `p. N`, frame variables, `NT$`.

## 14. Web regen — PASS

- Cards re-rendered from the delivered SVGs with CairoSVG
  (1950×2700, render.py settings) → **8/8 byte-identical** to the
  delivered cards (`work/regen-cards/`).
- Print PDF re-rendered (CairoSVG per-page + pypdf merge, render.py
  pipeline) → **byte-identical**: 20,844,689 B,
  sha256 `243110e0…399026` (see Pins).
- Web PDF re-rendered (PIL JPEG q85 @1400px from the delivered cards,
  saved under the same filename) → same size 3,515,785 B, 8 pages,
  same mediabox, page content streams identical; the ONLY differing
  bytes are 6 bytes inside the two timestamp strings
  (`D:20261028090117Z` delivered vs `D:20261028091919Z` regen).
  Web PDF is therefore **content-identical, timestamp bytes excepted**
  (stated explicitly, as required).

## 15. Eyeball all 8 cards — PASS

- All 8 cards viewed in full: layout clean, no overflow, no overlap,
  no missing content, no footer collision on any page.
- P4 title two-line wrap in Spanish (`棒球詞卡 · Palabras de` /
  `béisbol`): clean wrap with clear space to the article text below —
  acceptable, no collision (the English original fit one line).
- P7: readers'-corner box contains its Spanish disclosure with margin;
  teaser band clear of the footer rule; golden-sentence strip complete.
- P8: paren-style keys, separators, model text, and key 138/150 all
  render as specified; no truncated key lines.
- Card SHA-256 prefixes match the builder KIT §9 spot-check
  (p1 `5a228a41…`, p2 `d9adc11a…`, p3 `26f91a30…`, p4 `c7a5e71d…`,
  p5 `69fdd84e…`, p6 `133ca4d5…`, p7 `f8bca7f2…`, p8 `9dec19c9…`).

## 16. ABSTRACT.txt — PASS

- Single line (1 trailing newline), **no ASCII double quotes**,
  written in Spanish.
- Contains: paper name (`Lucerna VOL.2`), target language
  (`chino tradicional`), reader language (`para hispanohablantes`),
  levels (`A2 a B2`), exercise count (`150 ejercicios`), a learner
  search phrase (`aprende chino tradicional leyendo las noticias de
  esta semana en Taiwán y Hong Kong`), and the real topics.
- Topics cross-checked against the zh-tw core KIT's actual content —
  ALL present, none invented: Semana FinTech de Hong Kong, Feria
  Internacional de Viajes de Taipéi, campeonato de los Wei Chuan
  Dragons en la Serie de Taiwán, Lidong/Inicio del Invierno, Festival
  de Escultura en Acero de Kaohsiung, Halloween en Tianmu.

## PDF pins re-verified (final hashes, after all proof runs)

| file | bytes | sha256 |
|---|---|---|
| Lucerna-VOL2-ES.pdf (print, 8 pages) | 20844689 | 243110e0b95bcf868d38e34fa27a8bc8cca8eaf52f9e14c89a8421a1ab399026 |
| Lucerna-VOL2-ES-web.pdf (web, 8 pages) | 3515785 | 7c6f77e053d165a349562ed5c0b4571d310e9dfe5f6b2ed9590890d92efb4595 |
| svg/p1-front.svg | 251290 | c1ec15215fbd54699184e3e79cb093737829eb1d4dfc1c1c7f7bb107ba0267d6 |
| svg/p2-life.svg | 357535 | 2a0fc6522da4c2483d41b70fe5bcdabbeb8573db0fe55d3ac1619885f7111814 |
| svg/p3-culture.svg | 29438 | 4ebd3ea113c6f063bf43d9015a562ccb2c613168a4459e4346327a2a05ccef3e |
| svg/p4-sport.svg | 221863 | 98560a64e4251c6a0893e37e3c82a499f89ae385b58784ec2029f5eb78c47149 |
| svg/p5-youth.svg | 741217 | 93b732d67c4c805a25053275794395f4eceae425449bb18608003e4d32650624 |
| svg/p6-deep.svg | 29410 | 4eaed6620f92050d4d789ba0146a03afcc2a380e57664703ce99fa7538a161fc |
| svg/p7-lang.svg | 30288 | bc54632d07eca7a2df1edd0fe537ce33bfe87bca71e82179be2c7876cafd5fff |
| svg/p8-test.svg | 60018 | 3ac7ac37801ae5a16f62c73ad4c345bb8b7613e7f413c4c39754d92583bb6161 |

All match the coordinator-verified pins and the builder KIT §9.
Delivery + build dirs: mtime-diff zero from first to final snapshot.

## Non-blocking observations (do NOT affect the verdict)

1. **Proofreader's own registry-dump incident (disclosed, no content
   change).** While dumping the core registry, my first reg-core run
   executed with an unrepointed OUT (my repoint helper call failed
   because `apply_all` had already repointed the sibling copy, so the
   script died before repointing the core copy) and rewrote the 8
   shipped core SVGs in place. The rewrite is byte-identical: all 8
   core hashes still match the §1 pins above (verified after the
   incident, and again at the end), and a properly repointed redo dump
   produced an identical registry JSON. Only the core files' mtimes
   changed (09:14). The edition delivery/build dirs were never written
   by any proof run (mtime-diff zero). Lesson recorded here for the
   next proofreader: repoint OUT in the copy *before* running any
   content module, and verify OUT by printing it first (tools README
   #11 pitfall, re-encountered).
2. **Proofreader's stray output, removed.** The same incident's sibling
   reg-ed dump wrote 8 SVGs into an accidental
   `files/w45/zh-tw-es-proof/work/reg-ed/svg/` tree (created by the
   relative-path repoint inside `apply_all`). Those 8 SVGs were verified
   byte-identical to the delivered edition SVGs (extra determinism
   evidence) and the whole stray tree was then deleted; `files/w45/`
   no longer exists. No shared scratch dir was cleaned — only my own
   accidental output.
3. **`tools/tables.json` default P8 filename** does not match this
   core's `p8-test.svg` (builder's note, confirmed): p8.py needed the
   explicit `--core-p8`/`--edition-p8` form. Out of this edition's
   scope; recorded for the parent line, not edited here.
4. **P3 head form.** The shipped P3 head is the bilingual
   `算一算 · Calcula`, not a bare `Calcula` as the builder KIT §8
   shorthand says. This matches the edition's bilingual-head rule and
   removes the English residue; not a defect.
5. **W43 readers'-corner wording differs** from W45's (forward promise
   vs deferral) for the situational reason given in §11; the column
   elements are preserved. Not a defect.

## Limitations (stated honestly)

- Spanish was checked by full reading of every rendered string, not by
  a native speaker; no native-speaker review was available to this
  proofreader.
- Commons API re-query: a single fresh fetch of the P4 Commons file
  page returned HTTP 403 (same as the coordinator's prior attempts) and
  was not retried. Credits were verified against the core KIT's
  Artist-field table, the W43 precedent, and the binding 2026-10-27
  P4-provenance adjudication (placed bytes + credit unchanged), which
  is why the fetch failure does not block.
- The hand-rolled same-baseline/graze scan written for this proof
  produced systematic false flags and was discarded; the geometric
  verdict rests on the canonical `occlusion_audit.py` (0 flags),
  exact bar-geometry identity to the audited core, targeted PIL footer
  measurement, and the 8-card visual pass.
