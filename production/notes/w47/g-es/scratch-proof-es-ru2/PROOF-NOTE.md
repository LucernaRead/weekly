# PROOF-NOTE — W47 es-ru, proof2 (independent proofread, rebuilt edition)

- Edition: `production/2026-w47/2026-w47-es-ru/` (Spanish target × Russian reader,
  es full-family rebuild on core-es fix build 10, uncommitted, unpushed).
- Proofreader: subagent proof2, 2026-11-11. Read-only: no production file
  modified, no commit, no push. Rebuilds ran only on a scratch copy
  (`scratch-proof-es-ru2/ed-copy/`); production SHAs re-verified identical
  after all work (see §0).
- Probes first: `/dev/null` present; `echo test | git -C ~/workspace/weekly-git
  hash-object -w --stdin` RC=0; goals-side real write probe OK; TMPDIR kept
  inside the scratch dir (never `/tmp`). All tools run via
  `tools/venv/bin/python` (Pillow 13.0.0 / FreeType 2.14.3).
- Full text read: all 1,893 lines of `2026-w47-es-ru.text.md`. All 150 answer
  keys verified stem-by-stem by three-source cross-check (REG / text.md
  answers / P8-extracted keys; core P8 keys via p8 compare). All 8 page PNGs
  visually inspected (fresh renders from the shipped SVGs) + 5 full-scale
  crops of the risk areas.
- All mechanical gates re-run independently (driver `gates2.py`, outputs in
  this scratch). Evidence in `GATE-LOG.md`.

## Conclusion: (a) — zero-defect; can be finalized as-is

No defects. Proof1's D1 (P3 your-turn spill), D2 (P5 your-turn spill) and
D3 (P7 ERRORES title overflow) are all fixed and verified by true-ink
measurement + full-scale crops. Proof1's D4 (P5 frame/gap mismatch) is
adjudicated at core level (see §4) and is not re-litigated here.

## §0 Identity (disk-measured, before AND after the proof)

| Item | Bytes | SHA-256 | Lines |
|---|---|---|---|
| print `La-Lucerna-VOL4-es-ru.pdf` | 3,593,735 | `68a761681e7d760174eed1554672b7c3664cfbbef16bc89538543202bc3414b5` | — |
| web `La-Lucerna-VOL4-es-ru-web.pdf` | 941,922 | `e6281174237fe2bd31fb749fe7bc9bd76055933a632ec8b20d3081556171aaab` | — |
| `2026-w47-es-ru.text.md` | 52,477 | `05e7d6c91fa331618985a9d9bfae6564c1d596321227d002e4ff92e26a25c6aa` | 1,893 |

All three match the task + `FANOUT-REPORT.md` §2 exactly, before and after
(this proof changed nothing on disk; `git status` still shows only
`?? production/2026-w47/2026-w47-es-ru/`).

Core-es (before AND after, unchanged): `production/2026-w47/core-es/` —
print 17,212,955 B, SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`;
web 1,410,471 B, SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`;
text.md 43,788 B, 1,822 lines, SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
(NOTE: the `core-zh-cn/` directory is a different core — zh-cn *target*;
core-es is the es-target core. The task's "core-es" = `core-es/`.)

## §1 Defect list

None. Zero defects found.

## §2 Required checks (builder handoff) — all measured, all pass

### P8 multi-line items
- Definitive count by the build's own `wrap()` (key text `"{n}. {key} — {note}"`,
  serif 13.5, CW 422.5, 4-column flow): **exactly 5 multi-line keys, all
  2 lines** — #1, #44, #137, #138, #139. These are exactly KIT §6.2–§6.4
  (adjudicated). The "33" in the handoff was the **build-1** diagnostic count
  (before 27 notes were shortened in build 2); it is not the current count.
- In-column: the P8-keys flow uses `split=False` (a key never splits across
  columns); run 0 OVERFLOW; flow ends col 3/3 y=2537 (bottom 2560, 23 px
  spare); max key-line y measured 2556.6. Full-page P8 render + bottom crop
  viewed: all keys inside their columns, #150 last, no footer contact.
- (My first two SVG line-reconstruction scripts miscounted — cross-column
  line merging at shared y — and are superseded by the `wrap()` count, which
  agrees with the extractor's 150/150 and the flow's own end-y. Scripts kept
  as `p8_multiline.py` / `p8_multiline2.py` for the record; do not reuse
  their counts.)

### ERRORES — 4 notes
- **Measured: each note is 1 line, not 2.** `wrap()` (sans 19.5, CW−44=378.5)
  returns 1 line for all four; the SVG holds each as a single `<text>`.
  The handoff's "全是 2 行" describes the **harvest** state (KIT §6.9:
  "в harvest были по 2 строки") — the shortened forms now fit in 1 line.
  This is better than the premise, not a defect.
- Line height measured: 19.5 × 1.36 = **26.52 px** (the "+26.5 px" in the
  handoff). Box y=441.4, bottom=1064.0; last note baseline 1021.49;
  **baseline clearance +42.5 px**, ink −38 px. Column 3 ends 1865.51
  (identical to de/fr/it/pt/nl). Full-scale crop `crop-p7-errores.png`
  viewed: all four notes on one line each, comfortable margins.

### P5 your-turn (adjudicated — verified no line contact, not re-argued)
- 4 lines @19, Russian text complete ("…Напишите два предложения и
  пришлите их."). **Current measured values (rebuild): box bottom 1606.5,
  ink bottom 1603.9, true-ink clearance +2.7 px, gap to the y=1608
  divider 1.5 px — no contact.** The handoff's "col3 1601.55 / 6.45 px"
  is the **pre-rebuild build-2** value (KIT §3, stale: eh was +20; the
  rebuild's D2 fix moved eh to +25, +5 px). Full-scale crop
  `crop-p5-youturn.png` viewed: box edge and divider are distinct, ink
  inside. P3 same fix: box bottom 1599.8, ink bottom 1597.1, +2.7 px,
  8.2 px above the divider (crop viewed).

### Grammar fix «к сдачи номера» → «к сдаче номера»
- Fixed and in place: correct form ×1 in `content7.py`, ×1 in text.md,
  ×1 in `svg/p7-lengua.svg` (editor's note, 4 lines @19). Old form 0 in
  all live content (`.py`, `.md`, `svg/*.svg`, `ABSTRACT.txt`). The single
  remaining old-form hit is in `WEEKLY-KIT.md` §6.8, which quotes the fix
  itself ("«к сдачи номера» → «к сдаче номера»") — a historical record,
  not live content.

### P8-comment batch-edit rollbacks
- (a) P7 FRASES golden sentence NOT shortened: full quote
  «Una encuesta es una foto con margen de error, tomada en un día
  concreto.» + full Russian gloss «Опрос — это фото с погрешностью,
  сделанное в конкретный день.» present verbatim in `p7-lengua.svg`
  (and all 8 golden quotes full; P7 render viewed).
- (b) #44 note restored to the original: «Время впереди, глагол вторым»
  (2 lines, in the SVG at y=1554.5 + continuation "глагол вторым"),
  matching KIT §6.14(b); #133 alone was shortened, as specified.

### P8-keys end y / overflow
- **P8-keys end y=2537** (flow col 3/3, bottom 2560), confirmed in two
  independent rebuild runs (keycheck log + wrap-count run). **0 OVERFLOW /
  0 TOO WIDE** in all run logs. TOTAL 150.

## §3 keycheck #137 — extractor false positive, confirmed independently (not a defect)

- keycheck 148/150; the two mismatches are #137 and #150 only.
  #150 is the known open-question `✓` exception (all editions).
- #137: the extractor returns `Понедельник` for the key
  `Понедельник — Международный день фламенко.` because `p8.py` splits the
  key—note pair on the first ` — `, and here the em-dash is the Russian
  copula ("Monday IS International Flamenco Day"), not a separator.
- Independent confirmation (not the builder's crop):
  - Edition SVG `p8-ejercicios.svg`: full sentence on one visual line at
    **y=2088.34** (`137. ` + `Понедельник` + ` — ` + `Международный` +
    ` день` + ` фламенко` + `. — ` + `См` + `.`), continuation
    `оригинал.` at y=2104.00 (2 lines, KIT §6.4).
  - Print PDF text layer (p. 8): `137. Понедельник — Международный день
    фламенко. — См.` present verbatim.
  - Full-scale crop `crop-p8-key137.png` viewed: the whole sentence is
    printed, followed by `См. оригинал.` on the next line.
- This is the same adjudicated item as p8-compare keydiff [137, 138]
  (translation keys in the reader language + `См. оригинал.` note).

## §4 Adjudicated non-defects (not re-litigated)

- **p8 compare keydiff [137, 138]**: CLEAN, keydiff exactly [137, 138]
  (W45/W46 rule: translation items keyed by the reader-language sentence).
- **P5 frame / D4 (proof1)**: core-level adjudication. Core re-proof
  (scratch-proof-core-es3, §(f) C3 — "已裁定接受现状，禁改") examined
  Q70–75 keys (correo/papeleta/envío/identidad/censo/plazo), found all six
  unambiguous and consistent with the keys, and accepted the frame
  (`sobre · papeleta · censo · identidad · plazo · urna`) as-is. Measured
  here: frame words used by 4 of 6 gaps (papeleta, identidad, censo,
  plazo); unused sobre/urna are the designed distractors; 70 correo is a
  set phrase from the article, 72 envío derives from the infinitive given
  in the gap itself. The core is certified (a) with this in place; a
  fan-out proof does not re-open a core adjudication.
- **PCTE / 195 total (proof1 O1)**: core-level adjudication C2 (PCTE kept,
  195 kept) in core build 10, certified (a) by core re-proof. Not re-opened
  here (fan-out cannot change core text).
- **"next Sunday" (frozen core English)**: not present anywhere in this
  edition or core-es (grep for `sunday`, case-insensitive, over all
  `.py`/`.svg`/`.md` in both dirs: 0 hits). The task's cited locations
  (core `content12.py:37/:113`, `content34.py:127`) currently hold the P1
  headline flow, the LA PALABRA gloss and the Champions box — the pointer
  is stale, and there is nothing to verify or flag.
- **P1 caption page refs, creambox negative clearances (6), «el 1 como
  «el uno»», laSexta economy narrowing, Marta letter as labelled filler,
  middle-column white space**: as proof1 §14, re-confirmed by this read;
  the 6 raw creambox negatives are the known below-box headings, identical
  to core in coordinates and layout (proof1-adjudicated scanner artifacts).
- **Section headers frozen in the source language** (A　理解 etc. in
  Spanish): untouched; no reader-language translation of exercise section
  headers anywhere in the text.md read.

## §5 150 keys — hand verification (three-source)

- REG (in-process build) vs text.md answers: all 150 `N. KEY` strings found
  verbatim; the 5 split notes (#1, #44, #137, #138, #139) verified part by
  part (their continuations — "полночь", "глагол вторым", "оригинал.",
  "jueves 19" — are separate lines only because the text.md export
  interleaves columns). All 150 answer entries present exactly once
  (141–144 appear twice only because they are also exercise stems in §F).
- REG vs P8-extracted keys: 148/150; mismatches only #137 (false positive,
  §3) and #150 (`✓` exception).
- Core P8 keys vs edition P8 keys: CLEAN, keydiff [137, 138] (adjudicated).
- Matching sets letter-by-letter: 25–28 c/b/d/a; 52–55 c/b/a/d;
  141–144 c/d/b/a — all match the answer block and the stems.
- Counts: A2 50 / B1 72 / B2 28; pages 10/18/18/18/18/18/12/38; types:
  insertar 48, opción múltiple 47, relacionar 12, V/F 8, construir 7,
  reescribir 10, elección-en-texto 13, traducción 4, escribir 1.
  (The MC count 47 vs proof1's 60 reflects the builder's type naming:
  13 MC-in-text items are typed «Выбор в тексте»; stems and keys verified
  individually either way.)
- #150 model text: 97 words (content8.py prints `MODELO words: 97`;
  proof1 hand-counted 97; model text read in full).
- Text.md spot-checks against content: `hasta el jueves` ×7,
  `antes del jueves` ×0; `sábado veo el derbi` ×1; `hasta el jueves 19`
  consistent in Q3/Q12/Q139; 13-day and 15-day counts consistent
  (16→29 = 13 days; 13→27 inclusive = 15 days); dates re-checked
  (16 Mon, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 29 Sun — all match the paper).

## §6 D5 fonts (week-level known pending item — recorded only, not a (b) criterion)

- SVG `<text>` elements: 2,746 total (all carry font-family).
  Noto Sans CJK SC 643, Newsreader 1,496, Noto Serif CJK SC 606,
  UnifrakturMaguntia 1.
- **Latin-only text on Noto Sans CJK SC: 259 segments**
  (p1 40, p2 29, p3 30, p4 28, p5 28, p6 34, p7 18, p8 52).
  Latin-only on Noto Serif CJK SC: 0.
- Method: same as es-fr2 proof2 (font-family of the element; a segment
  counts when it holds ASCII letters and no Cyrillic/CJK). The sans CJK
  face carries all sans Latin text in this edition (titles, labels, the
  Russian explanation layer's Latin words) — a week-level item, recorded.

## §7 Observations (not defects — for the coordinator / tool owners)

- **O-web — web PDF is not byte-reproducible across renders (shared tool
  property, zero reader impact).** Four renders of the same shipped SVGs
  gave four different files: shipped 941,922 B (`e6281174…`), copy-render
  941,918 B (`479e75dc…`), rerun1 941,913 B (`a84a2572…`), rerun2 941,910 B
  (`37c85b32…`). Text layer identical in all four (53,657 bytes, raw
  pdftotext byte-identical to print). Root cause isolated: the embedded
  fontTools-subset fonts differ only in the sfnt `head` table — `modified`
  is stamped with each run's wall clock (shipped 12:27:41, copy 13:06:00,
  rerun1 13:12:13, rerun2 13:13:13) and the checksums follow it; glyph data
  is otherwise identical (17 font streams, same decompressed lengths).
  The print PDF re-renders byte-identically (SHA match). The web PDF was
  never part of the freeze gate (freeze covers SVGs 8/8; the KIT records
  the shipped file's SHA, which is intact on disk). No edition change can
  fix this; it would need `webpdf.py` to pin/zero `head.modified`. It
  applies to every edition's web PDF (shared tool), so it is recorded
  here as a tool observation, not an edition defect.
- Proof1 O2 (laSexta 13 Nov "public in the studio" — confirmed only for
  the 2/9 Nov encounters of the same strand): unchanged, still a reasonable
  inference, not a defect. O3 (image credits not independently verified):
  unchanged.

## Files (this scratch: `hidden_files/w47/scratch-proof-es-ru2/`)

- `PROOF-NOTE.md` (this file), `GATE-LOG.md` — full gate evidence.
- `ru-gates.json` — gate summary (all rc + SHAs).
- `ru-*.log`, `ru-occlusion.json`, `ru-p8-extract.json`,
  `ru-p8-compare.json`, `ru-freeze-diff.json`, `ru-freeze.log`,
  `ru-print.txt`, `ru-web.txt`, `ru-print-layout.txt`, `ru-web-layout.txt`,
  `ru-keycheck.log`, `keycheck-150.json`, `reg-dump.json`, `ru-minfont.log`,
  `ru-sweep.log`, `ru-p8keys.log`, `ru-render.log`.
- `gates2.py` (driver), `creambox.py` (canonical), `creambox_diag.py`,
  `boxtitle_core.py`, `keycheck_core.py`, `sweep_de.py`, `minfont.py`,
  `check_p8keys.py`, `p8_multiline.py`, `p8_multiline2.py` (superseded
  counters — see §2), `build-keycheck.py` (proof1's, not re-run).
- `visual/` — fresh renders p1–p8 (975×1350) + full-scale crops
  `crop-p3-youturn.png`, `crop-p5-youturn.png`, `crop-p7-errores.png`,
  `crop-p8-key137.png`, `crop-p8-keys-bottom.png`.
- `ed-copy/` — the rebuild copy (sources + SVGs; rendered cards/PDFs
  removed after the gates — reproducible; evidence in `ru-render.log` +
  `ru-gates.json`); `web-rerun1.pdf` / `web-rerun2.pdf` — the two extra
  webpdf.py runs for O-web; `freeze-es-ru/` (log only; build-copy removed,
  reproducible via `freeze.py`).
