# Lucerna Semanario · VOL.2 — Edición W45 zh-TW × ES (繁體中文 × Español)

Fan-out edition of the frozen W45 Traditional Chinese core (VOL.2, issue
week Mon 2026-11-02 to Sun 2026-11-08): Traditional Chinese target text
unchanged; **all** explanation layer rewritten in Spanish for
Spanish-speaking readers. Built 2026-10-28 by the fan-out builder line.
**Status: BUILT, NOT finalized — an independent proofread follows; only a
zero-problem proof finalizes it.**

- Build code: `hidden_files/weekly-report-w45-zh-tw-es-build/` (fresh copy
  of the core build, explanation layer only edited — and every edit lives
  in the transform script
  `hidden_files/weekly-report-w45-zh-tw-es-transform.py`, see §8)
- Deliverables in this directory: `svg/` ×8, `cards/` ×8 (1950×2700),
  `Lucerna-VOL2-ES.pdf` (print), `Lucerna-VOL2-ES-web.pdf` (web),
  `ABSTRACT.txt`, this KIT
- Slug: 2026-w45-zh-tw-es. No repo insert, no Discord post, no edition
  cards/PDFs sent to the main chat, no cron created (per assignment
  scope). `~/workspace/weekly-git` untouched.

## 0. Pre-flight duplicate check (coordinator ruling)

- Delivery dir `files/weekly-report-w45-zh-tw-es/` and build dir
  `hidden_files/weekly-report-w45-zh-tw-es-build/` did not exist when
  this task started (fresh dirs = trivially clear); no live
  process was writing to them (the only concurrent process observed was
  a sibling's core-baseline run into `tools/scratch/baseline-w45-zhtw`,
  not these dirs).
- Two mtime snapshots of the new dirs (snap2 at 08:37, snap3 at 08:40,
  `preflight-snap2/3.txt` in the build dir) differ in exactly one line:
  the build dir's own mtime/size, changed only because snap3 itself was
  written into it. Zero file changes by any other writer. Proceeded.
- No subagent was spawned at any point in this build.

## 1. Baseline proof (core reproduction FIRST)

The core build directory was copied to this edition's build dir and run
**unmodified** through `tools/freeze.py baseline` (own scratch out dir
`scratch/baseline-w45-zhtw-es`, to avoid colliding with the sibling's
concurrent baseline run). All 8 generated SVGs were **byte-identical**
(sha256, 8/8) to the shipped core SVGs, and the core SVGs were re-hashed
unchanged afterwards:

| page | core shipped sha256 (re-hashed from the core delivery dir) |
|---|---|
| p1-front | 4672c972763b0eaf249bff952cd777d9941cc2a801928bfb1edd1e0e4558d047 |
| p2-life | 889fb533ef3ff62ecc820d3d92dc4aed10e353f5dcf9487c9d844fd2dad3cee3 |
| p3-culture | 508703c2b3c313c6853a17e452e2d55629e0933a94905211f5f53425619bab42 |
| p4-sport | e04b62ea6211c9ffabeb90a1a94faa5b3bcea3503b19a7fbd6473546a88f86f1 |
| p5-youth | 4dfce72d88000fbc9d4f43f441a9f7525ec05165e812ab2df0b6a8bac6eea30f |
| p6-deep | 06ba4c6627cb81655e02b8ad7656676e3b258e3b0763dfde7e5ec29e7174c838 |
| p7-lang | 00ac7f57125fcc094ce850712a5d302df891600062fa8cbc0c47bd7a5243192c |
| p8-test | e6e97d02595aef3bb1a3c60dd852d190e387f647a547527cc24153eeea0b41ed |

Only after this proof was the explanation layer edited (via the
transform script).

## 2. Totals (registry, identical to the zh-tw core)

- **150 exercises** — A2 44 · B1 74 · B2 32 (core: 44/74/32 — NOT the
  zh-cn core's 56/69/25 split; the zh-tw core KIT is authoritative)
- Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38 (identical to core)
- Types: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1 (identical)
- Writing model: 138 characters, printed verbatim (unchanged Chinese text)
- Final build log: **zero warnings** (no FLOW OVERFLOW, no HEAD TOO WIDE)
- Flow ends (final render): P1-lead col 0/0 y=1900 (bottom 1935);
  P1-quiz col 3/3 y=2225; P2-main col 2/2 y=1264; P3-main col 2/2 y=1677;
  P4-main col 2/2 y=395 (bottom 1020); P4-ex col 2/2 y=2513;
  P5-main col 2/2 y=1391; P6-main col 2/2 y=663 (bottom 860);
  P6-ex col 2/2 y=2189; P7 col3 ends 1734.86; P7 teaser ends 2532.86
  (content bottom 2540, footer rule 2580); P8-ex col 3/3 y=299
  (bottom 1252); P8-keys col 3/3 y=2413 (bottom 2540)

## 3. Key-diff registry (the ONLY answer-key change)

Registry structure (n/page/level/type) is identical to the core. Exactly
**one** key changes, the open writing task (same pattern as the W43
zh-tw-es precedent, where the key diff was likewise #150 only):

| # | core key | ES key |
|---|---|---|
| 150 | (開放題,範文如下) | (pregunta abierta — modelo a continuación) |

#150's note re-aims accordingly: "Pregunta abierta — el modelo está
impreso arriba, en la sección F (138 caracteres)". Items #137/#138-type
Chinese fill-in keys are target layer and unchanged. All 150 P8 answer
**notes** were rewritten in Spanish; none is identical to its English
core note — including BOTH "AI" forms, which are separate strings and
were translated separately (the known zh-cn-es/it trap):
P6 note "AI helps read data, spot risks and answer clients." →
"La IA ayuda a leer datos, detectar riesgos y responder a los
clientes."; P8 note "AI inside finance is 人工智慧＋." →
"La IA dentro de las finanzas es 人工智慧＋." (visible as P8 key 138).

## 4. Furniture three-way table (core · W43 zh-tw-es · this edition)

Badge slot/size/color were MEASURED from the shipped P1 SVGs
(font-size/fill/anchor/width with PIL, TC face), not assumed from the
zh-cn family or from README #20's EN-instance wording:

| | W45 zh-tw core P1 | W43 zh-tw-es P1 | W45 zh-tw-es P1 (this edition) |
|---|---|---|---|
| badge y | 378 | 378 | 378 |
| badge size | 21pt | 21pt | 21pt |
| badge fill | OLIVE #3e4c2a | BRICK #a4553a | BRICK #a4553a |
| badge anchor | middle (x=975) | middle (x=975) | middle (x=975) |
| badge width | 1227px | 1248px | 1248px |
| strapline y/size/fill | 410 / 30pt / BRICK | 410 / 30pt / BRICK | 410 / 30pt / BRICK |

Ruling: the zh-tw core family HAS a native badge slot at y=378, so the
badge replaces the core's badge line **in place** at 21pt BRICK —
exactly the W43 zh-tw-es family's shipped precedent (its build code
line: `p.text(975, 378, "TEXTOS EN …", 21, "sans", True, BRICK,
anchor="middle")`). This is NOT the FR/IT inserted-slot case (y=574)
and NOT a 19.5pt subtitle-slot case; the masthead block is otherwise
untouched (wordmark 218, edition line 316, strapline 410 all frozen).

- P1 badge (this edition): `TEXTOS EN CHINO TRADICIONAL ·
  EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES
  HISPANOHABLANTES`
- Footer (all pages): `Lucerna · SEMANARIO CHINO TRADICIONAL VOL.2 ·
  TEXTO EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL` /
  `Página N de 8` (VOL.2 follows the W45 core; W43 used VOL.1)
- Masthead: `Lucerna` (no article — Chinese is article-less), as core
- Gloss prefix: `Nota — ` (bslib4 `gloss()`; core used `Notes｜`;
  W43 zh-tw-es shipped code uses `Nota — `)
- P8 note style (verified from the W43 zh-tw-es family's own shipped
  build code AND this edition's shipped P8 SVG, README #14): **paren
  style with a space before the note parenthesis, half-width parens
  only** — `N. key (note)`, writing `N. ✓ (note)` — NOT the core's dash
  style. The core svglib `_fw` pair rule would full-width the parens
  whenever a note contains a Chinese term, so key lines only bypass it
  (W43 precedent, replicated verbatim in content8.py, restored after
  the keys flow). P8 separators: `— Página N —` (NOT the zh-cn-es
  dash-style separator question — the zh-tw-es family precedent, also
  confirmed in this edition's shipped SVG).
- Instructions: `Completa` (fill-in, 54×); matching per set — P2/P3
  `Une palabra y definición`, P4 `Une nombre y dato`, P5
  `Une evento y dato` (W43 precedent pattern); `Redacción` (writing)
- Section heads are bilingual `中文 · Spanish` throughout (band titles,
  box titles, quiz heads, P7 column heads, P8 section heads A–F).
- Spanish conventions: thousands with dot (45.000, 1.600, 4.100),
  amounts as `2.400 NT$` (W43 `258 HK$` pattern), «» quotes inside
  Spanish text, `6.º partido` / `9.ª entrada` ordinals.
- Photo credit lines kept byte-identical English (W43 precedent).

## 5. Traditional independence — HARD GATE (method + outcome)

No Simplified→Traditional conversion was used anywhere: no OpenCC, no
mapping table of my own (the ru-zh-tw lesson: a builder's own table
missed 郵→郵). The edition's Traditional text comes only from the
zh-tw core (via the transform, which replaces English strings only and
never touches a Chinese string) plus the W43 zh-tw-es precedent for
furniture.

Cross-check (script `hidden_files/w45-zh-tw-es-checks.py` §5,
extraction method: every `<text>` node of the shipped SVGs, CJK range
U+4E00–U+9FFF):

- Union of (W43 zh-tw-es shipped SVG text) + (W45 zh-tw core SVG text):
  **1024 distinct characters**
- This edition's SVG text: **766 distinct characters**
- Edition characters outside the union: **0** — every Traditional
  character in this edition already occurs in the union, so none needs
  individual justification and none was removed.
- Simplified-only check: the freeze diff (§6) shows added CJK = 0 on
  every page, and target strings are unchanged (removed CJK is only the
  old Chinese furniture: the core badge line and the Chinese part of
  the core footer). No Simplified-only character appears in target
  text. (OpenCC was not installed on this VM, so the s2t-count
  comparison from the core KIT's 51/26/3/1 pattern could not be
  re-run; the union cross-check + added-CJK=0 gates above cover the
  same property from the shipped files themselves.)
- **Verdict: PASS — no build failure.**

## 6. Gates (all green on the final render)

- Freeze baseline: 8/8 byte-identical (§1).
- Freeze diff `--strict-cjk` (final render,
  `tools/scratch/w45-zh-tw-es-diff3.json`): per-page added CJK = 0 on
  all 8 pages (P1 952→920, P2 1018→996, P3 1088→1065, P4 831→809,
  P5 1101→1079, P6 942→921, P7 808→788, P8 1114→1092; decreases are
  only the old Chinese badge/footer furniture). TOTAL added CJK = 0.
  Added/removed string multisets are explanation layer + furniture
  only; no Chinese target string changed.
- p8.py compare (explicit P8 files, since tables.json's default P8
  filename does not match this core's `p8-test.svg`):
  **CLEAN, 150 noted = 150 noted, missing=[] extra_count=0,
  uncertain=[], keydiff=[]** (the #150 writing key is excluded from
  keydiff by the tool's writing-item rule; §3 records it).
- Occlusion audit (`tools/occlusion_audit.py`, selftest first — all 6
  planted classes fired, clean controls silent): edition **0 flags**;
  core **0 flags**; **NEW vs core: 0**. Same-baseline ink-collision
  scan (PIL TC metrics, all pages): **0 flags**. P4/P6 chart-label
  element check (text ink vs later-drawn rects): **0 overlaps** on
  both chart pages (bars measured in final SVGs: P4 120.0/600.0px,
  P6 600.0/800.0/800.0/800.0px — identical geometry to the core).
- Gloss counts (split each rendered `gloss()` call string on `·`
  itself, README #21): core = edition **item by item, total 12** —
  P1 [1,1], P2 [1,1], P3 [1,1,1], P4 [1,1], P5 [1,1], P6 [1].
  (The zh-tw core's gloss strings are prose sentences, so each counts
  1; the zh-cn core's 33 does NOT apply here — the core's true count
  was read from its own build, not assumed.)
- Registry: 150, ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings (§2).
- P7 golden sentences: all 8 verbatim from this issue's own articles,
  exactly 2× each (article + P7, counted over concatenated SVG text
  nodes), page tags correct: p. 1, p. 1, p. 2, p. 3, p. 3, p. 4, p. 5,
  p. 6. (An earlier check script counted the bracketed form and
  reported 1×; the correct bare-sentence count is 2× — the script bug
  was fixed, not the edition.)
- Images: all 4 payloads byte-identical to the core per page
  (P1 harbour, P2 rain, P4 baseball, P5 pumpkin); credits verbatim
  (Wilfredor — CC0; CorraleH — CC0; Bain News Service — Public
  domain; Benjamin Balazs — CC0, all Wikimedia Commons). P3/P6/P7/P8
  carry no photos (charts/tables instead), as in the core.
- Readers' corner: frozen Traditional disclosure intact
  (延期披露…你的來信，下一期見。) + Spanish disclosure stating no
  genuine letters exist and the invitation stays open
  ("…al cierre no había ninguna publicable, así que el ejemplo se
  mantiene y la invitación sigue abierta.") + the letter itself
  labeled an editor's example in both languages.
- All 8 cards eyeballed: no overflow, no overlap, no footer collision,
  chart bars/labels fully visible, P7 readers'-corner last line fully
  inside its box, P7 teaser clear of the footer rule.

## 7. Residual-Latin adjudication (every Latin string, one by one)

Full Latin-token scan over the final SVGs (767 distinct Latin tokens).
English-residue word scan (whole-word `the/and/with/from/this/that/
work/words/baseball`, excluding frozen theme text): **0 hits**.
Remaining Latin is adjudicated as follows — nothing else remains:

- Spanish explanation layer (the bulk): all glosses, notes, heads,
  furniture, instructions — intended.
- Frozen target text (Chinese articles, byte-identical to core):
  event/theme names `Fintech Nexus: Bridging the World, Building the
  Future`, `StartmeupHK 2026`, `ITF`, `SUPER STAGE`, `SOLID TIDES`,
  show name `JUMP`, shout `Trick or Treat`, team names
  `Wei Chuan Dragons` / `CTBC Brothers`, pitcher `C.C. Mercedes`,
  film names `Jurassic World, Shrek, Kung Fu Panda`, abbreviation
  `MVP` (Chinese text: "英文叫 MVP"), `Tamagotchi` anniversary
  reference, `Halloween` (Spanish loanword, also in Spanish text).
- Credits (byte-identical precedent): `Photo: … — CC0 / Public domain
  (Wikimedia Commons)` with artist names Wilfredor, CorraleH,
  Bain News Service, Benjamin Balazs.
- Structural Latin: masthead `Lucerna`, `VOL.2`, level chips
  `A2/B1/B2`, option letters `A./B./C.` and match letters `a.–d.`,
  page tags `p. 1`–`p. 6`, frame variables `X/Y`, currency `NT$`.
- Two English heads found by this sweep in v1 and FIXED (see §8):
  `算一算 · Work it out` (P3) and `棒球詞卡 · Baseball words` (P4) —
  both now Spanish; re-scan confirms zero.

## 8. Transform-first discipline + Gate 10 (transform-solo)

Every fix-layer edit in this build lives in
`hidden_files/weekly-report-w45-zh-tw-es-transform.py` (count-asserted
literal replacements, whole lines or exact unique matches — never AST
byte offsets, never repr literals in f-strings). No direct build-copy
edit was left standing: each build round re-copied the core fresh and
re-applied the transform.

Fix record (all folded into the transform as they were found):

1. HEAD TOO WIDE ×5 (v1): `讀懂了嗎? · ¿Lo has entendido?` (28pt,
   445px once `_fw` widens 嗎? → 嗎？) → `¿Entendido?` (W43
   precedent); `深讀測驗 · Cuestionario de lectura a fondo` →
   `Preguntas a fondo` (404px); `B1 · 球賽與節氣 · Partidos y
   estaciones` (470px) → `Juegos y estación` (427.6px).
2. P7 teaser past the footer rule (v1: ends 2602.86 > 2580): frame
   text shortened 5→3 lines (wt-a) and the Spanish deferral 7→6
   lines; teaser now ends 2532.86.
3. P7 readers'-corner BOXTITLE (NEW vs core, 11.2px): the letters-box
   `lh` formula underestimates drawn height by ~11px (same latent gap
   in the core, where the audit's center-attribution edge happens not
   to fire); bottom padding 26→46 in the formula. Audit now 0 flags.
4. Strict-CJK +1 on P7 (v1): the comma after 封王 in the B1
   memory-trick sentence was `_fw`-converted to full-width ，;
   reworded with `y` (no comma after the CJK term). Added CJK now 0.
5. Missed heads (§7 sweep): P3 `算一算 · Work it out` →
   `Calcula`; P4 `棒球詞卡 · Baseball words` →
   `Palabras de béisbol` (wraps to 2 lines as a title; P4-main flow
   has ample slack, ends y=395).
6. Gate-10 path bug (script-only, no edition impact): the gate10
   repoint first replaced a path tail and then the tail again,
   doubling the prefix and writing one solo run's SVGs into a stray
   nested tree under the goal dir. Those 8 SVGs were verified
   byte-identical to the delivered SVGs, the stray tree was deleted,
   the script was fixed to replace the whole OUT assignment, and
   Gate 10 was re-run cleanly (see below).

**Gate 10 (self-run, final transform):** fresh core copy + transform
script ALONE + one-process driver → **8/8 byte-identical to the
delivered SVGs, warnings=0, exit code 0**
(`--gate10` mode of the transform script; registry re-confirmed
150 / 44/74/32 / pages 10/18/18/18/18/18/12/38 in that run).

## 9. Deliverable pins

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

Web PDF 3,515,785 B < 10 MB. Cards are the 09:00 render of the final
SVGs (card SHA-256 spot-checked against the eyeballed files: p1
5a228a41…, p2 d9adc11a…, p3 26f91a30…, p4 c7a5e71d…, p5 69fdd84e…,
p6 133ca4d5…, p7 f8bca7f2…, p8 9dec19c9…).

## 10. Status

BUILT, NOT finalized. All builder gates above are green. Awaiting the
independent proofread (full proofread to zero problems, including its
own freeze/p8/occlusion runs) before any repo insert or delivery.
Known non-blocking notes for the proofreader:

- The core's own P7 letters box carries the same ~11px `lh`
  underestimate (its last line straddles the box border by ~6px of
  baseline); this edition pads the box by 20px instead of
  reproducing the core's exact geometry. Flagged here, not hidden.
- OpenCC is not installed on this VM, so the s2t-count comparison
  (core KIT 51/26/3/1) could not be re-run; the union cross-check (§5)
  and strict-CJK=0 (§6) stand in its place.
- `tools/tables.json`'s default P8 filename does not match this
  core's `p8-test.svg`; p8.py was run with explicit `--core-p8` /
  `--edition-p8` paths (recorded for the parent line; a tables.json
  fix is out of this edition's scope).
- The P4 title `棒球詞卡 · Palabras de béisbol` wraps to two lines
  (the English original fit one); layout slack absorbs it with no
  warning and no overlap — proofreader to confirm visually.
