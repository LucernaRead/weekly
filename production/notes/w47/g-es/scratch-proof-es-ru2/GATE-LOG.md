# GATE-LOG — W47 es-ru, proof2 (independent proofread), 2026-11-11

Probes first: `/dev/null` present; `echo test | git -C ~/workspace/weekly-git
hash-object -w --stdin` RC=0; goals-side real write probe OK (`.probe`).
TMPDIR inside the scratch dir throughout; nothing written to `/tmp` except
one mistyped `pdftotext` probe (`/tmp/x`, failed/ignored — redone cleanly
into the scratch). All Python via `tools/venv/bin/python`
(Pillow 13.0.0 / FreeType 2.14.3). Production dir read-only: the rebuild
(run.py + render.py) ran only on a scratch copy (`ed-copy/`); the shipped
SHAs were re-measured identical afterwards. One background `sha256sum`
sweep over the week was killed after it had already served its purpose
(core-es located independently); its delivered result agrees with the
direct measurement (core-es print SHA `2723a283…`).

## §0 Identity (disk-measured, before AND after)

- print: 3,593,735 B, SHA-256
  `68a761681e7d760174eed1554672b7c3664cfbbef16bc89538543202bc3414b5`
- web: 941,922 B, SHA-256
  `e6281174237fe2bd31fb749fe7bc9bd76055933a632ec8b20d3081556171aaab`
- `text.md`: 52,477 B, 1,893 lines, SHA-256
  `05e7d6c91fa331618985a9d9bfae6564c1d596321227d002e4ff92e26a25c6aa`
- All three match the task + `FANOUT-REPORT.md` §2 exactly, before and
  after. `git status` unchanged: `?? production/2026-w47/2026-w47-es-ru/`.
- Core-es before and after: print 17,212,955 B `2723a283…`;
  web 1,410,471 B `c2473211…`; text.md 43,788 B / 1,822 lines `509c95fa…`
  (matches `FANOUT-REPORT.md` §0).

## §1 Run + render (on the scratch copy)

- `gates2.py`: copy_rc=0, render_rc=0.
- Copy-render print PDF: 3,593,735 B, **SHA identical to shipped**
  (`render_print_sha_match: true`).
- Copy-render web PDF: 941,918 B, SHA differs (`render_web_sha_match:
  false`) — see §11 O-web; text layer identical.
- `run.py` (in-process, copy): rc=0, **0 OVERFLOW / 0 TOO WIDE**,
  TOTAL 150; by level A2 50 / B1 72 / B2 28; by page 10/18/18/18/18/18/12/38;
  column ends: P2 1080.0, P3 1599.75, P4 1022.5, **P5 1606.55**,
  P6 1347.5 (timeline box), P7 1865.51, P8-ex 943, **P8-keys 2537**
  (bottom 2560), P8 image bottom ≈1296.8.
  (KIT §3's P3 1594.75 / P5 1601.55 are stale build-2 values — the rebuild's
  eh +20→+25 moved both boxes +5 px. Current values above.)
- `MODELO words: 97`.

## §2 Occlusion audit (formal)

- `tools/occlusion_audit.py` on the shipped svg/: **0 flags**.
- Selftest: all 6 classes fired (BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX);
  clean controls silent.
- Known limitation (proof1): the audit does not cover cream-box content —
  covered separately by creambox + PIL ink + boxtitle (§5–§7).

## §3 p8 extract + compare

- `tools/p8.py extract --total 150`: **150/150** keys extracted
  (`noted set = 150 of 150`, parse: lines).
- `tools/p8.py compare` vs core-es p8: **status CLEAN**,
  `keydiff=[137, 138]`, missing=[], extra_count=0, uncertain=[].
  (Read from `ru-p8-compare.json` directly — `gates.json`'s p8-extra "?"
  is the known driver key-name misread, per the task.)

## §4 Freeze (reproducibility)

- `tools/freeze.py baseline --build <edition> --core-svg ./svg`:
  **8/8 SVGs byte-identical** (repointed files: none); per-page SHA list
  in `ru-freeze.log` (p1 `2da01962…` … p8 `fab93c00…`); core integrity:
  shipped core SVGs unchanged by the run (8 files re-hashed).
- `tools/freeze.py diff` core vs edition:
  - `cjk_added_total: {}` — **zero added CJK on all 8 pages**.
  - Added strings per page (occurrences): p1 62, p2 126, p3 34, p4 34,
    p5 93, p6 18, p7 50, p8 854 — all CJK-bearing 0; U+3000-bearing
    strings: p1 14, p2 9, p3 6, p4 7, p5 7, p6 5, p7 7, p8 5
    (title separators — the only permitted new U+3000).
  - Removed strings are the core's Chinese explanation layer
    (CJK-bearing share: p1 28/36, p2 43/51, p3 30/30, p4 27/27,
    p5 40/45, p6 16/17, p7 40/46, p8 249/392; the non-CJK removed
    occurrences are re-wrapped number/punctuation fragments).
  - No added Cyrillic string lacks an explanation-layer counterpart:
    added Cyrillic = the Russian reader layer, as designed.

## §5 Cream-box scan + PIL true ink

- Canonical `hidden_files/w47/tools/creambox.py` (md5 of the canonical
  file in use: the tool as copied into this scratch), 8 pages: rc=0.
- Raw scan: 6 negative clearances — all the known below-box headings,
  identical to core in coordinates/layout (proof1-adjudicated scanner
  artifacts):
  P1 AHORA TÚ −37.0, EN ESTA EDICIÓN −44.0, LA PALABRA −24.0,
  caption −24.0; P2 DECIR LA HORA −37.0; P3 LO QUE QUEDA −37.0.
- `creambox_diag.py` (PIL true ink): **0 negative own-ink clearances**
  on all boxes. Own last-line ink clearances (selection):
  - P1 CINCO CLAVES (C1, box 700→720): box bottom 1308.0, last baseline
    1300.0, ink bottom 1304.5, **ink-clearance +3.5**.
  - P3 your-turn: box bottom 1599.8, last baseline 1592.8,
    ink bottom 1597.1, **+2.7**.
  - P5 your-turn: box bottom 1606.5, last baseline 1599.6,
    ink bottom 1603.9, **+2.7**; divider y=1608 → 1.5 px gap.
  - P5 blackfri: ink bottom 1251.4, clearance +0.1 (inside).
  - P2 calendar: ink bottom 543.4, clearance +0.1 (inside).
  - P7 ERRORES: box bottom 1064.0, last baseline 1021.49,
    clearance +42.5 baseline / ink −38.
- Full-scale crops viewed: `crop-p3-youturn.png`, `crop-p5-youturn.png`
  (ink inside both boxes; P5 box edge distinct from the divider).

## §6 Boxtitle widths (PIL, Noto Sans CJK SC Bold idx 2)

- `boxtitle_core.py` on the shipped svg/: rc=0, **0 overflow**
  (no `clear=-` in the log; 25 titles with `clear=+`).
- P7 (the old D3): `ERRORES TÍPICOS　Ошибки` fs=23 Bold,
  title_w=323.7, right=1785.2 vs box right 1862, **clear=+76.8**
  (was +44.7 overflow in build 1). `LA PALABRA　Слово недели` +77.9;
  `CARTAS DE LOS LECTORES` +104.6.
- Crop `crop-p7-errores.png` viewed: title well inside the box.

## §7 P7 ERRORES box (required re-measurement)

- Box x=1439.5 y=441.4 w=422.5 h=622.6, bottom=1064.0.
- All four notes wrap to **1 line** (`wrap()` sans 19.5, CW−44=378.5;
  each is a single `<text>` in the SVG):
  err1 «Час — единственное число: es.» y=608.57;
  err2 «mejor уже сравнительная степень.» y=746.21;
  err3 «gente — единственное: глагол — тоже.» y=883.85;
  err4 «creo que утверждает: изъявительное.» y=1021.49.
- Line height 19.5 × 1.36 = **26.52 px**; item pitch 137.64 px;
  last baseline 1021.49 → **+42.5 px** to the box bottom.

## §8 P8 multi-line keys (required re-measurement)

- Definitive count via the build's own `wrap()` on each REG key's exact
  rendered text (`"{n}. {key} — {note}"`, serif 13.5, CW 422.5):
  **5 multi-line keys, all 2 lines: #1, #44, #137, #138, #139**
  (KIT §6.2–§6.4, adjudicated). "33" was the build-1 diagnostic count.
- Flow: `split=False` per key (never splits across columns); 0 OVERFLOW;
  P8-keys end col 3/3 **y=2537** (bottom 2560); max key-line y 2556.6.
- `#137` y=2088.34 → 2104.00; `#138` y=2104.00+ (2 lines each).
- Two SVG line-reconstruction attempts (`p8_multiline.py`,
  `p8_multiline2.py`) miscounted by merging same-y lines across columns
  (7 / 76 "multi-line") and are superseded by the `wrap()` count.
- `check_p8keys.py` (the script's own count) also reports 7 for the same
  merging reason — not used as evidence.
- P8 min effective font 10.125 pt (minfont.py, n=777 runs), 0 below the
  9.75 pt floor.

## §9 keycheck (REG vs P8-extracted keys)

- `keycheck_core.py` on the scratch copy: rc=1 (expected),
  **148/150 exact**; mismatches only:
  - n=137 (Перевод): key `Понедельник — Международный день фламенко.`,
    extracted `Понедельник` — extractor false positive, §10.
  - n=150 (Письмо): key `(открытый вопрос — образец ниже)`,
    extracted `✓` — known open-question exception, all editions.
- `keycheck-150.json` written (150 REG entries).

## §10 #137 false-positive proof (independent)

- SVG: full sentence on one line at y=2088.34 (see PROOF-NOTE §3).
- Print PDF p. 8 text layer: `137. Понедельник — Международный день
  фламенко. — См.` verbatim (pdftotext -layout).
- Rendered crop `crop-p8-key137.png` viewed: full sentence printed,
  `См. оригинал.` on the next line.

## §11 Print vs web text layer + web-PDF byte determinism

- Raw `pdftotext` (no -layout): print = web **byte-identical**,
  53,657 bytes.
- `-layout` mode: print = web **identical** too (proof1's build-2
  P1 1-space diff is gone in the rebuild).
- Render reproducibility (copy): print PDF byte-identical (SHA match);
  web PDF differs (941,918 B vs shipped 941,922 B) — investigated, see
  O-web below.

### O-web — web PDF byte variance is font `head.modified` timestamps
- Four renders, same shipped SVGs: shipped 941,922 B `e6281174…`;
  copy 941,918 B `479e75dc…`; rerun1 941,913 B `a84a2572…`; rerun2
  941,910 B `37c85b32…`. Text layer 53,657 B identical in all four.
- All 98 PDF streams compared after Flate decompression: only the 17
  embedded subset-font streams differ, and only in the sfnt `head`
  table: `head.modified` = the run's wall clock (shipped 2026-11-11
  12:27:41; copy 13:06:00; rerun1 13:12:13; rerun2 13:13:13) with
  `checkSumAdjustment` + directory checksum following it
  (e.g. obj 26: dirsum `2959acd7` → `2959b5d2` → `2959b747` →
  `2959b783`; `created` stays 2020-11-26 12:39:20; decompressed font
  lengths identical; glyph bytes otherwise identical).
- Mechanism: `tools/webpdf.py` subsets fonts with fontTools, which
  stamps `head.modified` with the current time on save. Shared tool →
  affects every edition's web PDF equally; zero reader impact; the web
  PDF was never under the freeze gate. Recorded as a tool observation,
  not an edition defect. (Rerun PDFs kept: `web-rerun1.pdf`,
  `web-rerun2.pdf`.)

## §12 Sweeps

- `sweep_de.py` on the edition: box-vs-hline flags **0**; bridges found
  20, bridge orphans **0**, bridge widows **0**. DONE.

## §13 150-key hand verification (three-source)

- REG keys vs text.md answers: all 150 `N. KEY` found verbatim in the
  P8-exercise + answer region; the 5 split notes verified part by part
  (#1 "полночь", #44 "глагол вторым", #137/#138 "оригинал.",
  #139 "jueves 19" — continuations only, because the text.md export
  interleaves columns). Answer entries 1–150 present, none missing
  (141–144 double only as exercise stems in §F).
- REG vs P8-extract: mismatches exactly [137, 150] (see §9).
- Core vs edition P8: CLEAN [137, 138] (see §3).
- Matching sets: 25–28 c/b/d/a; 52–55 c/b/a/d; 141–144 c/d/b/a.
- Counts: A2 50 / B1 72 / B2 28; pages 10/18/18/18/18/18/12/38.
- Types per REG: insertar 48, opción múltiple 47, relacionar 12, V/F 8,
  construir 7, reescribir 10, elección-en-texto 13, traducción 4,
  escribir 1.
- #150 model text 97 words (content8.py output; proof1 hand-counted 97).

## §14 Visual skim (SOP §8.3) — all 8 pages + 5 crops viewed

Fresh renders from the shipped SVGs (`visual/p1–p8`, 975×1350):

- P1: masthead, lead, CINCO CLAVES (ink +3.5 in box), LA SEMANA EN
  CIFRAS, EN ESTA EDICIÓN, AHORA TÚ, LA PALABRA, UNA SEMANA TRES
  ESCENARIOS, BREVES, urna illustration + caption, QUIZ 7–10. Clean.
- P2: calendar (7 entries, dates/events match), DECIR LA HORA,
  LOS DÍAS table, ¿SABÍAS QUE…?, ¿Y TÚ? (7 lines @20), exercises A–D.
  Clean.
- P3: Sargent «Bailaora española» + caption, EL FLAMENCO EN TRES DATOS,
  ¿Y TÚ? box (ink +2.7, divider clear), exercises A–D. Clean.
- P4: LA CHAMPIONS VUELVE, ¿Y TÚ? (6 lines @20), LA JORNADA 13 table
  (6 matches/times), exercises A–D. Clean.
- P5: EL PLAN DE LA SEMANA, urna photo + Jebulon CC0 caption,
  VOTAR POR PRIMERA VEZ, ¿Y TÚ? box (ink +2.7, 1.5 px from divider, no
  contact), frame visible, exercises A–D (70–75). Clean.
- P6: EL CAMINO AL 29N (9 entries incl. RTVE a-ocho 23 Nov), LEER UN
  DEBATE, RTVE chart (45/45/30/30/15 + footnote Frente Obrero/PCTE/SALF,
  195 total), ¿POR QUÉ NO HAY ENCUESTAS? (5/15/1), exercises A–D. Clean.
- P7: three grammar columns, Book of Hours image, ERRORES box (title
  +76.8, notes 1 line each), LA PALABRA, CARTAS (Marta letter + editor's
  note «к сдаче номера»), FRASES (8 golden quotes, full), LA PRÓXIMA
  SEMANA banner. Clean.
- P8: exercises A–H, model text (97 words), swan-quill image, RESPUESTAS
  1–150 in 4 columns ending y=2537, #150 last. Clean.
- Crops: `crop-p3-youturn.png`, `crop-p5-youturn.png`,
  `crop-p7-errores.png`, `crop-p8-key137.png`,
  `crop-p8-keys-bottom.png` — all confirm the measurements above.

## §15 D5 fonts (record only)

- 2,746 `<text>` elements (all with font-family): Noto Sans CJK SC 643,
  Newsreader 1,496, Noto Serif CJK SC 606, UnifrakturMaguntia 1.
- Latin-only on Noto Sans CJK SC: **259** (p1 40, p2 29, p3 30, p4 28,
  p5 28, p6 34, p7 18, p8 52); on Noto Serif CJK SC: 0.

## §16 Text.md full-read notes

- 1,893 lines read in full. `hasta el jueves` ×7; `antes del jueves` ×0;
  `sábado veo el derbi` ×1; `к сдаче номера` ×1 (content7.py, text.md,
  p7 SVG each); `к сдачи номера` 0 in live content (1 hit only in
  WEEKLY-KIT.md §6.8 quoting the fix).
- "next Sunday": 0 hits in core-es + edition (all .py/.svg/.md) — the
  task's cited core lines hold other content; no such string exists here.
- Section headers stay in the source language (Spanish) throughout;
  no reader-language translations of exercise section headers.
- Dates re-checked against the paper: 9 Mon, 10 Tue, 13 Fri, 16 Mon,
  17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue,
  26 Thu, 27 Fri, 28 Sat, 29 Sun; 16→29 = 13 days; 13→27 incl. = 15.

## §17 Lessons / pitfalls recorded during this run

- `render.py`/`run.py` must never run in the production dir during a
  read-only proof: run them on a scratch copy and SHA-compare afterwards.
  The print PDF reproduced byte-identically (safe); the web PDF did not
  (font timestamps — §11), so an in-place render would have silently
  changed the shipped web PDF's SHA.
- `freeze.py baseline` is the safe rebuild path (copies the build dir
  first); `keycheck_core.py` runs `run.py` in the dir it is given, so
  always pass it the copy, never the edition dir.
- Never `pdftotext` into `/tmp` by reflex — route all outputs into the
  scratch dir (one mistyped probe did hit `/tmp/x`; harmless, redone).
- SVG key-line reconstruction by y-grouping is unreliable on P8: runs
  from parallel columns share y values and merge. The build's own
  `wrap()` on the REG texts is the definitive multi-line count.
- KIT §3's column-end numbers are build-2 values; after a rebuild, use
  the fresh run log, not the KIT body (the rebuild's §9 + run log govern).
- Do not trust `gates.json`'s p8-extra "?" for the compare status — read
  `p8-compare.json` directly (CLEAN / keydiff [137, 138]).
