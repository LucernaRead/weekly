# FIX-LOG — es-ko fix1 (independent proofreading round 2 (b), 2026-11-11)

Edition: 2026-W47 es-ko. Four minor defects, all in the Korean explanation
layer. No Spanish (core) text touched; core-es tree hash unchanged
(`8651a818…`, before = after). No commit, no push.

## D-01 — P8 #45 Korean note truncated

- Source: `content34.py:101` (P8 key note for #45)
- Before: `"장소가 앞에, 동사는 두 번째"`
- After: `"장소가 앞에, 동사는 두 번째예요"`
- Why: same note in full form at #44 (`content34.py:99`,
  `"시간이 앞에, 동사는 두 번째예요"`) and #133 (`text.md:1728`,
  `"El lunes suena el flamenco. — 시간이 앞에, 동사는 두 번째예요"`).
- Four-source check (all full form):
  `content34.py:101` ✓; `2026-w47-es-ko.text.md:1651` (+ continuation
  `예요` on the next exported line) ✓; P8 SVG nodes `두 번째`
  (y=1599.78) + `예요` (y=1615.44) ✓; print + web PDF text layer
  (`45. En Bilbao toca la banda el domingo. — 장소가 앞에, 동사는 두 번째`
  + `예요`) ✓.
- Consequence (recorded, not a defect): with `예요` the #45 key line wraps
  to 2 lines, like the already-accepted #44 (`두 번째예요` tail). P8-keys
  flow end 2506 → 2538 (22 px spare, bottom 2560, no overflow). P8
  multi-line items 6 → 7 (#45 joins #32, #44, #82, #92, #139, #140).

## D-02 — P4 D bridge drops the Latin term

- Source: `content34.py:200` (section `D　EL PRETÉRITO INDEFINIDO`)
- Before: `e.bridge("문장을 과거형으로 바꾸세요.")`
- After: `e.bridge("과거형(pretérito indefinido)으로 바꾸세요.")`
- Why: the only one of the edition's 20 bridges without its Latin term;
  all 9 es sister editions keep it (es-de `Setze die Sätze ins pretérito
  indefinido (Vergangenheit).`, es-fr `Mets les phrases au passé
  (pretérito indefinido).`). Form follows the ja sister
  (`過去形（pretérito indefinido）に直そう。`) and this edition's own
  convention of attaching the parenthesis directly to the word it glosses
  (e.g. `content7.py:20` `es la una(단수)`). 1 line at sans 20.5
  (381.2 units < CW 422.5). The tense name stays in the section title
  directly above; title untouched. The rejected alternative
  (`문장을 과거형(pretérito indefinido)으로 바꾸세요.`) wraps to 2 lines
  with a lone `요.` tail, so the object `문장을` was dropped instead.

## D-03 — P1 numbers box, item "13": lone `)` on its own line

- Source: `content12.py:47` (`LA SEMANA EN CIFRAS`, item 13)
- Before: `13 — días faltan el lunes 16 para las elecciones del domingo 29(선거까지 13일)`
  wrapped 3 lines; line 3 was a lone `)` (SVG y=1414.5).
- After: `13 — días faltan el lunes 16 para las elecciones del domingo 29(선거 13일)`
  (dropped `까지`; sibling item 2 already uses the bare form `(선거운동 15일)`;
  "days remaining until the elections" is already in the Spanish).
  Wraps 2 lines; `)` now closes line 2 (SVG y=1386.84, same baseline as
  `선거 13일`). Re-measured: no lone-`)` node at y=1414.5.
- Wrap math (real `wrap()`, serif 20.5, inner width 386.5): before
  `[331.7, 384.1, 6.4]`; after `[331.7, 350.9]`.

## D-04 — P2 calendar box, Domingo 22: `축일` split across lines

- Source: `content12.py:185` (`EL CALENDARIO`, Domingo 22 item)
- Before: `…; 성녀 체칠리아 축일)` wrapped 4 lines; line 3 ended `축`,
  line 4 was lone `일)` (SVG y=1113.44).
- After: `…; 성 체칠리아 축일)` — `성녀` → `성`, the §6.11 #32 precedent
  (`성녀 체칠리아` → `성 체칠리아`). Wraps 3 lines; `축일)` intact on
  line 3 (SVG y=1084.88). Re-measured: no `일)` node at y=1113.44.
- Wrap math (real `wrap()`, serif 21, inner width 386.5): before
  `[371.2, 382.9, 367.0, 26.9]`; after `[371.2, 382.9, 373.5]`.
- NOT touched: the identical string in `content56.py:27` (P5 `EL PLAN DE
  LA SEMANA` item 5) already wraps cleanly (`축일` intact, P5 SVG
  y=747.28) — its `성녀` stays.

## KIT corrections (same round)

- §1: still quoted the old build-2 SHAs. Replaced with the fix1 build-3
  values (below); `text.md` 1,800 → 1,823 lines; pdftotext print = web
  107,964 B (was 47,790 B in build 2; 109,956 B at refanout).
- §3: gloss-word token counts (core §8.1 method, P5 page text, SVG
  substring count): `papeleta` 3 → 2 (gloss + vocab list; the third
  occurrence counted before, `papeletas de verdad`, is on P6, not P5);
  `plazo` 4 → 3 (title + gloss + vocab list). `censo` stays 2.
  P8-keys y 2506 → 2538; multi-line items 6 → 7 (see D-01).

## Rebuild + gates (build 3, all green)

- `run.py` rc=0, TOTAL 150 (A2 50 / B1 72 / B2 28), 0 OVERFLOW / TOO WIDE.
  Col ends unchanged except P8-keys (2538). `render.py` rc=0.
- Occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN
  (keydiff [137, 138], adjudicated §6.12); freeze baseline 8/8
  byte-identical + freeze-diff CJK accounting clean (3,458 added CJK
  chars, 0 unaccounted); creambox full scan 0 own-ink overflow
  (creambox_diag 0 own-ink negatives; the 6 raw negatives are the known
  below-box headings, unchanged); boxtitle 0 overflow (log identical to
  refanout); keycheck 149/150 exact — only the #150 open-question `✓`
  exception; sweep 0 orphans / 0 box-vs-hline / 0 widows (20 bridges);
  pdftotext print = web, byte-identical, 107,964 B; P8 min font 10.125 pt
  (0 below the 9.75 pt floor).
- Orphan sweeps (whole 8 SVG set, baseline+column segments): lone
  `。`/right-quote/`：`/`–`/`—` = 0; Korean lone `)` / lone-syllable final
  line = 0. Same scan on the rebuild SVGs flags exactly the 2 fixed
  items (P1 y=1414.5 `)`, P2 y=1113.5 `일)`).
- 150-question hand check: `text.md` read end-to-end (1,823 lines);
  keys 1–150 all present, none missing, none > 150. Sorted-line diff vs
  the rebuild `text.md` shows ONLY the 4 fix regions changed (plus
  exporter band separators). 8 pages visually inspected (cards/*.png).
- SVG diff: only P1/P2/P4/P8 changed; P3/P5/P6/P7 byte-identical to the
  rebuild.

## New deliverables (build 3)

- Print PDF: `La-Lucerna-VOL4-es-ko.pdf` — 8,873,692 B,
  SHA-256 `2c98a0f8f49e2e4519acdbe56b54702a315b0eb9777223c166775d88f86fcb43`
- Web PDF: `La-Lucerna-VOL4-es-ko-web.pdf` — 1,236,860 B,
  SHA-256 `2c9a90e05f99fe3a4ed024878bb229fac46042644e1bf57fef4d06e11ec0f008`
- Text: `2026-w47-es-ko.text.md` — 47,385 B, 1,823 lines,
  SHA-256 `a24b79b064896d11b6ba57f5b8f6d0f12047816b78551c76ec93a141787123d6`
- Note: the print SHA is stable across two renders (`2c98a0f8…` both
  times); the web PDF bytes differ run to run (first render
  `e3f25c33…`, gates render `2c9a90e0…`) from identical SVGs — record the
  on-disk SHA above.
- Rebuild baseline for reference: print 8,874,351 B `65e3a399…`,
  web 1,237,415 B `54494cef…`, text 47,369 B `f49dd708…` (1,817 lines).

## Scope

Changed only: `content12.py`, `content34.py`, `WEEKLY-KIT.md`, this file,
plus the rebuilt `svg/` (P1/P2/P4/P8), `cards/`, the two PDFs and
`2026-w47-es-ko.text.md`. Core-es and every other edition untouched.
Gate logs + toolbox copy:
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-es-ko2/`.
