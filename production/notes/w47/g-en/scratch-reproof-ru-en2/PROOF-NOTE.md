# PROOF NOTE — 2026-W47 ru-en, re-proof of fix2 (independent, full re-read)

- Edition: `production/2026-w47/2026-w47-ru-en` (Russian target × English reader), VOL.4
- Re-proofer: independent re-proof agent, 2026-11-11. All conclusions below are from my own
  re-runs on disk; fix2's FIX-LOG/GATE-LOG (goals `hidden_files/w47/scratch-fix-ru-en2/`)
  were read as reference only and not copied.
- Work dir (only scratch used): `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-en2/`
- No commit, no push, no production write (snapshot §7), no other week touched.

## Conclusion: (a) 零缺陷，可定稿

R1 and R2 are both fixed and verified by independent re-measurement; all 16 gates
re-run by me pass. One correction to fix2's record (a **method** correction, not an
edition defect — see §4): fix2's "occlusion 42/42 CLEAR" does **not** reproduce under
the correct SX=1.0 scale (37 CLEAR + 5 flags need adjudication). I adjudicated all 5
with independent evidence and they are audit false positives (true-ink gaps
+2.3/+2.4 px, visibly separate, identical geometry in the frozen core). No real
overlap exists anywhere in the edition. Nothing in this note blocks sign-off.

## Identity (measured twice: start and close — identical)

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,270 | `d12fa6a6bb62dd7af36743c7d2f33d96d27def054e5dcd6fdb288ef3577c06a1` |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,903 | `3cd934e01db298f13cd0c492ea14904ce2d5df3860d543818a91b1a4416c1dfe` |
| `2026-w47-ru-en.text.md` | 62,816 | `5ec76132a069d0c1cef7e9abe54d2556ace7419daf308805491b77bb22bfd97d` |

All three match the brief's expected values at start and at close.

## R1 — FIXED, triple-method re-measurement on the DELIVERED PDFs

Source: `content56.py:138` now reads
`p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　FOR & AGAINST", 24, "sans", True, OLIVE)`.
24 pt kept; Russian head untouched. `text.md` L449 is the same short title;
0 occurrences of `FOR AND AGAINST` in text.md, p6 SVG, or either PDF.

| Method (my own re-run) | Right edge | Margin vs box right 1862.0 |
|---|---|---|
| PIL true ink (`ink-post.log`) | 1829.4 svg px | **+32.6 px** |
| Delivered print-PDF vector char boxes (`pdf-title-print.log`, last char `T` bbox x1=1373.09 pt) | 1830.8 svg px | **+31.2 px** |
| Delivered print-PDF 600 dpi render, rightmost dark pixel (`pdf-title-print.log`) | 1829.9 svg px | **+32.1 px** |
| Delivered web-PDF char boxes + 600 dpi render (`pdf-title-web.log`) | 1830.8 / 1829.9 svg px | **+31.2 / +32.1 px** (identical to print) |

All ≥ +5 px requirement; the three methods agree within 1.4 px; print and web
agree exactly. Visual: 300 dpi P6-box crops from the delivered print and web PDFs
(`crops/p6-box-print.png`, `crops/p6-box-web.png`, byte-identical, SHA `f0957d07…`)
read by eye — `ЗА И ПРОТИВ　FOR & AGAINST` ends well inside the cream box.

32-box-title sweep (`titles-sweep.log`): 32 titles, **0 negative clearances**.
Tightest right clearance **+14.1 px** (P1 `В ЭТОМ НОМЕРЕ IN THIS ISSUE`, ink-right
1847.9); R1 title third tightest at +32.6 px; S1 title +95.4 px (ink-right 865.6).
Tightest bottom clearance +47.2 px. (Proof1's "+6.8 px" is a kicker-gap value, not
a title value — not cited here.) Spill sweep (`spill.log`): 32 cream boxes,
**0 ink escapes, 0 bad titles**, 43 spill-below candidates (same by-design set).

## R2 — FIXED, mechanism re-verified

- `build_map.py` read in full: merged map starts from `tm2-<lang>.json`, then every
  `miss-tr-<lang>.json` bucket entry **overrides** (`m[bucket][k] = v`); miss-tr is
  the only upstream source for this value because `tm2-en.json` has 4 buckets and
  **no** `ТУР В ЦИФРАХ` key (checked directly).
- `miss-tr-en.json:33` is the short form: `"ТУР В ЦИФРАХ　数字看本轮": "ТУР В ЦИФРАХ　The round"`;
  file SHA `9c301611…`, 123 lit keys, 0 occurrences of `The round in numbers`;
  `map-en.json` lit value is the same short form (SHA `400fcdd2…`).
- Re-run in my own scratch copy (`r2/build-map.log`): `python3 build_map.py en`
  rc=0, `map lit 335 type 8 instr 9 key 8`, "map OK", no PROBLEMS; regenerated
  `map-en.json` **byte-identical** (SHA still `400fcdd2…`). A fan-out re-run cannot
  revive the long form.

## Occlusion — the one correction (method, not a defect)

- Audit selftest OK; real run on the production SVGs: **42 TEXTX, 0 LINEX, 0 COVER,
  0 FOOTER, 0 EDGE, 0 BOXTITLE** (`gates/occlusion.json`, rc=1 = flags found, as designed).
- fix2's adjudication used `adjudicate_ru.py` with hardcoded `SX=1950/1800` (=1.0833).
  The SVG canvas is 1950×2700 and the cards are 1950×2700, so svg px == card px
  and the correct scale is **SX=1.0**. I re-adjudicated with my own script
  (`adjudicate_sx10.py`, same junction-gap logic, SX=1.0) against **both** the
  production cards **and** the delivered print PDF rasterised at 96 dpi
  (=1950×2700, same coordinate mapping): **37 CLEAR, 5 OVERLAP**
  (`gates/adjudication-sx10.log`). The old script re-run edition-pointed still says
  42/42 CLEAR (`gates/adjudication-old-sx.log`) — the wrong scale moves each
  junction J by up to ~150 px and measures background elsewhere. **Do not cite the
  old 42/42 as evidence.**
- The 5 flags (`gates/occ5-measure.log`, `gates/occ5-pdfchar.log`, crops `crops/occ-*.png`):
  P1/P4 `Краснодар` » ×4 and P7 `Кипренского` `, 1827` ×1. Independent evidence:
  - PIL true ink with the renderer's own fonts: real gaps **+2.4 px** (all four
    `Краснодар` junctions) and **+2.3 px** (`Кипренского`) — the glyphs do not touch.
    The audit's ink-box overestimates by ~5.5 px at these serif/quote junctions
    (advance/bearing-inclusive boxes: audit overlap 3.1 px vs true-ink gap 2.4 px).
  - Delivered print-PDF 96 dpi raster: a clear background column exists at all four
    `Краснодар` junctions (gap=1 px); the card render gives 0 px there only because
    antialiased fringes fill the 2 clear columns at 1:1 scale — a limit of the 1:1
    raster test, not touching ink.
  - P7 `Кипренского`: the caption sits over a dark portrait image; the pdf=0 px
    reading counts image highlights as "ink" under the dark-background rule
    (card=7 px). The text reads with normal spacing in the 300 dpi crop.
  - 300 dpi crops from the delivered print PDF read by eye: `«Краснодар»` and
    `Кипренского, 1827 год` are tight but cleanly separated, no merged strokes.
  - All five junctions are **byte-identical in position in frozen core-ru**
    (same run x-positions) — inherited core typesetting, not introduced by fan-out
    or fix2.
  - The two P8 `ОТВЕТЫ` flags are CLEAR on both rasters (card 11/12 px, pdf 13/12 px).
- Verdict: **no real overlap in the edition; the 5 flags are audit false positives.**
  Recommended follow-up for the coordinator (tool, not edition): `occlusion_audit`
  ink-box overestimates at serif/quote junctions, and `adjudicate_ru.py`'s SX must
  be fixed to 1.0 for this family; until then, tight junctions should be adjudicated
  by PIL true-ink + visual crop, as done here.

## Gates (all re-run by me; full values in GATE-LOG.md)

- `run.py` rc=0, TOTAL **150** (A2 50 / B1 76 / B2 24; by page 10/18/18/18/18/18/12/38;
  model words 97), **0** FLOW OVERFLOW / HEAD TOO WIDE.
- Scratch rebuild from production sources: SVG **8/8 byte-identical**; rebuilt print
  PDF SHA-identical to production (`d12fa6a6…`); rebuilt text.md SHA-identical
  (`5ec76132…`); rebuilt web PDF 3,380,888 B (15 B short of production's 3,380,903 —
  font-subset randomness, expected) with identical 57,316 text bytes.
- `check_core.py` rc=0: golden BAD **0**, gloss fails **0**, P8 SVG text 10,561 chars;
  1 orphan line-start (P7 y553 `”».`, known benign) + 1 same-baseline collision
  (P1 y1712 `чёрная`, known).
- P8: extract **150/150**; compare vs core-ru **CLEAN**, missing=[], extra=0,
  `keydiff=[137, 138, 139, 140]` (the four E translation keys, as designed).
- Keycheck: **149/150**; only Q150 differs (registry `(Open task; model text below)`
  vs P8 printed `✓`, as designed for the open writing task).
- Freeze: core baseline **8/8** byte-identical, rc=0, core integrity OK (my first
  attempt returned 0/8 because I passed `--build` the rebuild dir instead of core-ru;
  corrected re-run is 8/8 — recorded here so the 0/8 is not mistaken for a finding).
  Freeze diff per-page +/− identical to fix2 (p1 +20/−21 … p8 +173/−627); removed
  distinct 451 (per-page sum 484), added distinct 298 (per-page sum 324); added CJK
  total 8, all U+3000; **Cyrillic-bearing removed exactly 15** (Q46 `можно` ×1 +
  14 Morozko-caption words, all P8, image skipped by design), **added Cyrillic 0**;
  P6 added run `　FOR & AGAINST` present, removed long-title run absent.
- Print/web text layer: plain `pdftotext` **57,316 bytes each, byte-identical**;
  layout **111,873 bytes each, byte-identical**; non-whitespace multiset identical
  overall (**30,352**) and per page; span-pair and char-pair gap diffs max **0.00 pt**;
  D2 7 pinned spots **0.000 pt**; D3 `а`→`»` gap −2.193 pt both; D1 straight quotes
  in both PDFs.
- `verify_mine2.py`: 20 PASS, 1 FAIL — the known D3-space **finder bug** (it looks for
  consecutive `я`,`п` and misses the space char; returns None/None). Corrected direct
  measurement (`d3_space.py`, `gates/d3-space.log`): space bbox
  **[1145.576, 1266.762, 1148.108, 1288.725], byte-identical print/web** — D3 fixed.
  Verdicts identical on rebuild PDFs and on the delivered production PDFs.
- `s11_check.py` on the production edition: rc=0, **FAILURES: none**; 8 SVG; paper
  #fbfaf6; badges; foot VOL.4; masthead 196 px; left margin 88.0; no CJK in visible
  SVG; both PDFs 8 pages; web 3,380,903 B < 7 MB; web text > 0;
  **P8 min font 9.75 pt** (direct PyMuPDF: 9.75 pt, 411 spans < 10 pt) — SOP §1.1
  lower bound met exactly. `tables.py vol 2026-W47` → vol 4.
- `pdffonts`: 72 entries each, all emb/sub/uni; web embeds Lucerna* subsets incl.
  `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`.
- Creambox full 8-page scan: 1,156 lines; the P6 title line is `FOR &amp; AGAINST`.
- Kicker: 9 double-space PIL true-ink gaps **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2,
  9.5, 7.1] px, min 5.0 ≥ 4 — PASS**.

## 150 exercises — hand verification

- Registry 150 = P8 extract 150 = rebuilt text.md 150 exercises (277 blocks);
  same by-page/by-level distribution as fix1.
- My own Cyrillic-string multiset diff, edition vs core (`gates/cyrillic-stems.log`):
  **added Cyrillic strings 0**; removed exactly the 15 known P8 Morozko-caption
  words (all P8, image skipped by design). No stem text was added or altered.
  Edition visible-SVG CJK: only U+3000 (123 occurrences).
- Keys: only Q137–140 (translation keys) and Q150 (open task, by design) differ
  from the core — confirmed by p8 compare + keycheck.
- Spot hand-checks: Q20 stem L173 `… о своём ___ — key: желании`, key list L694
  `20. желании`; Q25 L187 `25. 17 ноября — День студента (key b · Students' Day b)`;
  Q73 stem L405 `… сделали 14,4 млн ___ — key: заказов`, key list L753 `73. заказов`;
  D2 full phrase `Международный день студента` ×2 in text.md = core ×2;
  `желании` ×2 = core ×2. D1: text.md L459 `УЧЕБНЫЕ ДАННЫЕ`, L504
  `Три уровня, три темы`, L596 `Большой тест недели + все ответы`. S1 survives
  (P1 title +95.4 px, p1 SVG byte-identical to the fix1-measured version).

## D5 — recorded only (not a gate, not fixed)

Fonts: all 72 `pdffonts` entries in both delivered PDFs are embedded, subset, and
Unicode (`yes yes yes`); no non-embedded font listed. No D5 finding raised.

## Production zero-write + scope

- Edition-dir snapshot before vs after (44 files, same path form): **identical** —
  no production file was written by any step of this re-proof. Core-ru snapshot
  also identical. All builds ran in the scratch rebuild copy; all measurements read
  the delivered files. No git add/commit/push/stash/reset, no `insert.py`/`lint --write`.
- Startup probes: `git hash-object -w /dev/null` rc=0; real write probe
  `scratch-reproof-ru-en2/probe.txt` OK. TMPDIR was my own scratch throughout.

## Evidence files (this scratch)

`PROOF-NOTE.md` (this file); `GATE-LOG.md`; `ink-post.log`, `pdf-title-print.log`,
`pdf-title-web.log`, `titles-sweep.log`, `kicker.log`, `spill.log`, `probe.txt`;
`gates/` — `run.log`, `render.log`, `webpdf.log`, `textmd.log`, `occlusion.json/.log`,
`occlusion-selftest.log`, `adjudication-sx10.log`, `adjudication-old-sx.log`,
`occ5-measure.log`, `occ5-pdfchar.log`, `p8-extract.json/.log`, `p8-compare.json/.log`,
`keycheck.log`, `dump-reg.log`, `freeze-std.log`, `freeze-std.json`, `freeze-std/`,
`freeze-diff.json/.log`, `freeze-adjudicate.log`, `check-core.log`, `s11.log`,
`creambox.log`, `verify-mine2.log`, `verify-mine2-prod.log`, `d3-space.log`,
`p8-minfont.log`, `fonts-print.log`, `fonts-web.log`, `cyrillic-stems.log`;
`text/print.txt`, `text/web.txt`, `text/print-layout.txt`, `text/web-layout.txt`;
`crops/` — `p6-box-print.png`, `p6-box-web.png` (byte-identical),
`occ-p1-krasnodar.png`, `occ-p4a-krasnodar.png`, `occ-p4b-krasnodar.png`,
`occ-p4c-krasnodar.png`, `occ-p7-kiprenskogo.png`; `rebuild/` (scratch build copy);
`r2/` (build_map rerun inputs + regenerated byte-identical `map-en.json`);
`snapshot-start.txt`, `snapshot-end.txt`, `snapshot-core-start.txt`,
`snapshot-core-end.txt`; scripts `adjudicate_sx10.py` (SX=1.0, card + PDF raster),
plus the fix2 scripts reused with ED repointed to this scratch where applicable.
