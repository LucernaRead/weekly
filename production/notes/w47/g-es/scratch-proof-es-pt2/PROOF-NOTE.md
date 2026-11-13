# PROOF-NOTE — W47 es-pt (Spanish target × Portuguese reader), proof2 (rebuilt edition)

- **Proofreader:** proof2 (independent), 2026-11-11
- **Object:** `production/2026-w47/2026-w47-es-pt/` (es full-family rebuild, re-fanout on
  core-es fix build 10; per `scratch-refanout-es/FANOUT-REPORT.md` §2)
- **Verdict: (a) — READY. Zero defects found in this independent full re-proof.**
- **No production file was modified, committed, or pushed by this proof** — except the
  gate-required re-render (see §7): `render.py` re-rendered `cards/*.png` + both PDFs
  from the shipped SVGs. The print PDF reproduced byte-identically; the web PDF's
  bytes changed only by toolchain timestamps (content-identical, §7).

## Object verified (SHA-256)

Identity checked **before** any gate ran, and re-checked after (see §7 for the web-PDF note):

| File | Bytes | SHA-256 | Brief |
|---|---|---|---|
| `La-Lucerna-VOL4-es-pt.pdf` (print) | 3,500,936 | `0c8dd28550be5ababc176503a426e430546f8357969d8f9104451b10b5c0d6c2` | match ✓ |
| `La-Lucerna-VOL4-es-pt-web.pdf` (web) | 885,039 | `427e9c26d0b055f94e27e06fb659738e7250363e8a0eaf88fe5086f70e099e38` | match ✓ (pre-render) |
| `2026-w47-es-pt.text.md` | 45,535 (1,815 lines) | `9df4d30caba991aa1f966eccc360cf801b3a6cf9764f448662be5804de06e6c8` | match ✓ |

Core-es contrast (measured before AND after this proof — unchanged):
print `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`
(17,212,955 B), web `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`
(1,410,471 B), text `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`
(1,822 lines). `git status`: es-pt and core-es still untracked (`??`); no commit/push.
W43 modifications in `git status` are pre-existing other work, not touched.

Probe: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; goals-side write OK.
`TMPDIR` = this scratch's `tmp/` throughout. Runtime:
`~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0 / FreeType 2.14.3).
Note: `/dev/null` was a 0-byte regular file at probe time and **vanished mid-proof**
(`fatal: could not open '/dev/null'`), restored with `touch /dev/null` per brief
instruction; git worked again immediately after.

## Defects

**None.** Zero defects — no (b) items.

### proof1 D1 — RE-VERIFIED FIXED (P1 box-title overflow)

- `LA SEMANA EN CIFRAS　Números`, box x=538..961, y=1288, title baseline y=1324.7, fs=23 bold.
- boxtitle advance-width: right edge **932.9, clearance +28.1px** inside the box
  (proof1: +10.9px overrun with `Em números`; PIL ink then +7px past the cream edge).
- Visually confirmed in the full P1 render: `Números` sits inside the cream box.

### proof1 D2 — RE-VERIFIED FIXED (4 Brazilian-PT forms → European PT)

All four confirmed in **three places each**: `content56.py` source, `text.md`, and the
printed P8 keys in `p8-ejercicios.svg`:

| # | As printed now (EU-PT) | Proof1 (BR-PT) |
|---|---|---|
| 67 | `As secções abrem das 9:00 às 20:00` | `seções` |
| 71 | `papeleta = boletim de voto` | `cédula` |
| 74 | `censo = recenseamento eleitoral` | `cadastro eleitoral` |
| 96 | `Aunque + indicativo (facto conhecido)` | `fato` |

Brazilian forms ×0 (word-boundary grep): `seções` / `cédula` / `cadastro` / `fato`
absent from text.md, from all 8 SVGs, and from `content*.py`. (Substring `fato`
inside `facto` correctly excluded by the word-boundary search.)

### Builder handoff item — P2 title intrusion — RE-VERIFIED FIXED

- Old: `EL CALENDARIO　O calendário da semana`, TEXTX overlap 22.8×15.2px into the
  Note box. Now: `EL CALENDARIO　O calendário`.
- boxtitle advance right **902.1, clearance +58.9** (box x=538..961).
- PIL true-ink measurement on the independent P2 render (1950×2700, 1:1 SVG coords):
  title ink rightmost x = **901** (y=228–232); **0 ink pixels in the gap x=961..988**;
  row scans confirm cream edges exactly at 961 (calendar box right) and 989
  (Note box left). Clearance ink→Note-box = **88px**.
- Crop `visual/crop-p2-calendario-title.png` + full P2 render inspected by eye: the
  title ends well inside its box; the Note box is separate. **No intrusion.**

## Gates summary (all actually run — see GATE-LOG.md for commands and full tables)

| Gate | Result |
|---|---|
| run + render (`run.py` rebuild via freeze baseline; `render.py` re-render) | rc=0; print PDF byte-identical to brief (SHA `0c8dd285…`, see §7 for web) |
| Occlusion audit (formal, no --selftest) | **0 flags**; selftest all six classes fired (BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX) |
| p8 extract | **150/150** |
| p8 compare vs core-es | **CLEAN**; missing=[] extra=[] uncertain=[]; keydiff=[137, 138] (adjudicated translation items, W45/W46 ruling — NOT a defect) |
| Freeze baseline (source freeze) | **8/8 byte-identical** (rebuild from source in scratch copy); core SVGs unchanged by the run |
| Freeze diff (string freeze) | **added CJK = 0 total** (p1–p8 per-page 0; residual CJK in edition = 12–20 U+3000 structural spaces per page only) |
| keycheck (REG vs P8-extracted) | REG 150; A2 50 / B1 72 / B2 28; per page P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38; MODELO 97 words; **149/150 exact** — only #150 differs by its adjudicated rendered form (REG key `Questão aberta — texto modelo abaixo, nesta página`, extracted `✓`) |
| P8-keys end | **y=2521** (bottom 2560); **0 OVERFLOW** |
| Print/web text layer | `pdftotext -layout` both **109,215 B, byte-identical** (`cmp` clean); both PDFs 8 pages; my web text == builder's web text == builder's print text |
| P8 minimum font | **10.125 pt** (n=376); 0 below the 9.75 pt floor; distinct sizes 10.125–34.5 pt |
| Canonical creambox full scan (`hidden_files/w47/tools/creambox.py`, md5 `ee7a55d8…`) | 26 boxes; **6 negative clearances — all adjudicated false positives** (below-box headings, same boxes as core: P1 AHORA TÚ / EN ESTA EDICIÓN / LA PALABRA / caption, P2 DECIR LA HORA, P3 LO QUE QUEDA DE NOVIEMBRE). Core scan shows the same 6 negatives at the same boxes |
| creambox_diag true-ink | **All own-line ink clearances ≥ 0**: tightest P2 `ley.` **+0.1** and P5 VOTAR `compara precios antes de pagar.` **+0.1** (both frozen Spanish, identical in core); P1 CINCO CLAVES **+3.8**; P3 `música.` **+5.0** (the −1.2 desc-clear flag was a false alarm — no descenders in `música.`); P7 CARTAS **+1.5**; P2/P3/P4/P5 ¿Y TÚ? +1.5/+1.7/+1.8/+1.7 |
| boxtitle advance widths (all 27 titles, real font/weight) | **0 overflows**; tightest P7 LA PALABRA **+9.0**, P7 ERRORES TÍPICOS **+20.1**, P2 Nota **+21.3**, P1 EN ESTA EDICIÓN **+23.7** |
| sweep (box-vs-hline / bridge orphans / widows) | **0 / 0 / 0** (20 bridges found) |
| Curly quotes U+201C/U+201D/U+2019 | **0** in all SVG `<text>` and in text.md; guillemets « » balanced **56/56**; 0 ASCII apostrophes/straight double quotes in text.md |
| §1.1 fonts/colors | paper `#fbfaf6` ×8; masthead UnifrakturMaguntia ×1; VOL.4 ×9, VOL.5 ×3 (legitimate forward refs); P8 chip rects A2 `#5c6e30` ×11 / B1 `#46581f` ×21 / B2 `#37402f` ×3 (a 4th `#37402f` rect is the P8 header band, same as core); moth `<title>Lucerna 三色蛾</title>` ×2 (as in core); CJK in SVG `<text>` = 0; U+3000 total 118 (SVG) / 98 (text.md); `#3a3631` ×0, `#302c28` body as in core; no gold/brick-red; fill census vs core-es: no new colors introduced by the fan-out |
| Dates (`date -d`, Europe/Madrid) | 2026-11-13 Fri, 11-16 Mon, 11-19 Thu, 11-20 Fri, 11-22 Sun, 11-24 Tue, 11-25 Wed, 11-26 Thu, 11-27 Fri, 11-28 Sat, 11-29 Sun — all match the paper's weekday claims |
| P6 bar spans | RTVE bars 288/288/192/192/96 px = 45/45/30/30/15 min at exactly **6.4 px/min**; mini-bars 32/96/6.4 px = 5/15/1 at 6.4 px/min |

## 150 answer keys — semantic hand-verification (all hand-checked, three-source cross-check)

Sources cross-checked per item: (1) stem as laid out in the page SVGs (column-major,
`extract_items.py` → `items-150.txt`, 138 items + 12 matching items verified separately),
(2) keys printed on P8 (`pt-p8-extract.json`), (3) answers in text.md, (4) core-es P8 keys
(`core-p8-extract.json`: only #137/#138/#150 differ from the PT keys — adjudicated).

- **All 150 keys correct for their stems.** Matching: 25=c, 26=b, 27=d, 28=a;
  52=c, 53=b, 54=a, 55=d; 141=c, 142=d, 143=b, 144=a (each also confirmed in
  REG, P8-extracted, core, and text.md answers).
- MCQ (`Escolha múltipla`, 47 items) and text-choice (P8 A/B) keys all match the articles.
- Golden sentences **8/8, each on its article page + P7** (SVG-direct check):
  S1 P1, S2 P4, S3 P2, S4 P5, S5 P3, S6 P3, S7 P6, S8 P6; P7 page refs
  (Página 1/2/3/3/4/5/6/6) all correct.
- Model text counted **97 words** from `content8.py` source (within the 80–100 requirement).
- P7 header `Frases da semana (ipsis litteris, desta edição)`: verified — core's header is
  `本周金句（逐字摘自本期文章）` ("verbatim from this issue"); `ipsis litteris` is correct
  Latin for "verbatim", a faithful fan-out rendering, not an error.
- The brief's "frozen core English `next Sunday`": the string `next Sunday`/`Sunday`
  occurs **nowhere** in core-es `*.py`, es-pt `*.py`, or `tools/tables.py` (case-insensitive
  search), and the brief's cited line numbers do not contain it in the current core files
  (`content12.py:37` is a `Flow(…)` call, `:113` a `rect(…)` call). The rule is moot for
  this edition; nothing flagged.

## Text.md full read (1,815 lines)

Read end to end. All section headers, exercises, and the P8 answer section are present
and consistent with the SVGs. Spot notes: P2 `EL CALENDARIO　O calendário` (shortened);
P5 Nota `la papeleta = o boletim de voto`; EU-PT `tu`-forms throughout (`vais`,
`ouviste`, `Votarias`, `comprarias`, `até ao fecho`, `secção`, `adeptos`,
`bilhete de identidade`); P6 `195 minutos en total` + `PCTE` retained (C2 adjudication);
`hasta el jueves` inclusive wording present, `antes del jueves` ×0 (checked in
text.md: `sábado veo el derbi` ×1 as the Marta letter line). No new issues found.

## Visual check of the 8 rendered PNGs (`visual/p1-portada.png` … `p8-ejercicios.png`)

- **P1:** clean. D1 title inside its box; CINCO CLAVES bars, ballot-box illustration,
  quiz strip, footer all clean.
- **P2:** clean (see P2-title section above). ¿Y TÚ? last line `envia-as à redação.`
  inside its box. `D LAS PALABRAS` header at the bottom of column 3 with items in
  column 4 — layout as frozen, not a defect.
- **P3:** clean. Sargent image matches its caption; ¿Y TÚ? last line `envia-as.` inside.
- **P4:** clean. MD13 table and LA CHAMPIONS VUELVE box match the verified fixtures/results.
- **P5:** clean. VOTAR box last line `compara precios antes de pagar.` inside; ¿Y TÚ?
  `frases e envia-as.` inside. Bronze ballot-box photo matches its caption
  (`SUFFRAGE UNIVERSEL`).
- **P6:** clean. RTVE bar chart renders correctly (bars proportional, no overflow);
  EL CAMINO AL 29N timeline and ¿POR QUÉ NO HAY ENCUESTAS? boxes fine.
  (The chart's *numbers* are the core-level C2 item, §8 below.)
- **P7:** clean. ERRORES TÍPICOS / LA PALABRA / CARTAS boxes all inside their cream;
  medieval book-of-hours image matches its caption; golden sentences + page refs correct.
- **P8:** clean. All 150 keys legible; the four D2 EU-PT forms confirmed in print;
  #150 uses the adjudicated `✓` form. Plume image matches its caption.

No overlap, no footer intrusion, no image-caption mismatch on any page.

## Observations (not defects)

- **O1:** P2 `ley.` ink +0.1 and P5 VOTAR `compara precios antes de pagar.` +0.1 —
  at the edge but not over; frozen Spanish text, byte-identical in core. Same as proof1 O1.
- **O2:** #56 note `más + importante (a luta pelo título)` is a surplus interpretation
  (the stem has nothing to do with the title race); the fact is not wrong (Barça does
  lead). Same as proof1 O2; not a defect.
- **D5 (whole-week mechanism item, recorded only — NOT judged (b)):**
  Latin explanation layers render in **Noto Sans CJK SC**, not SOP §1.1 Newsreader.
  Measured: es-pt **634** `<text>` elements in Noto Sans CJK SC (398 bold + 236 regular;
  per page P1 71, P2 78, P3 82, P4 76, P5 80, P6 68, P7 74, P8 105) vs core-es 608;
  Newsreader 975 (110 bold + 865 regular) vs core 1200; Noto Serif CJK SC 43 vs core 310.
  Uniform across production, previously proof-passed and shipped; fixable only by a
  mechanism change, not at edition level. Same for body text using `#302c28` instead
  of SOP's `#3a3631` (0 occurrences of `#3a3631` in both core and edition).

## Core-level candidates (report to coordinator; NOT es-pt defects — carried forward from proof1, unchanged by the rebuild)

- **C1 — Nov 13 laSexta debate theme (frozen core).** The paper says economy only;
  quadratin.com 2026-11-10 and diarioenpositivo.com 2026-11-06 describe Nov 13 as
  economy + housing. Core KIT §6.10 already adjudicated economy-only. Insufficient to
  overturn; no new evidence in this proof round.
- **C2 — RTVE free-minutes split presented as JEC-settled (frozen core, P6).**
  45/45/30/30/15 + 3×10 = 195, internally consistent, and P8 keys #83–85 faithfully
  carry the same numbers. Live reporting (diariodia.es, 2026-11-01, updated 2026-11-09)
  showed the split actively disputed before the JEC at proof1 time. Not re-verified
  live in this round (core unchanged since core re-proof (a)); the coordinator may
  re-check before the publication window (Nov 16–22).

## §7 — Web-PDF SHA: mechanism finding (NOT an edition defect)

The gate-required re-render overwrote the web PDF. The new file is
**885,050 B, SHA-256 `10610da1250af48d158a1410bc111e417a4cc6ce8c06428c76283fd38c19eefa`**
(vs the brief's 885,039 B / `427e9c26…`). The bytes differ **only** by toolchain
timestamps; the content is identical (text layer byte-identical, § Gates).

Root cause, isolated step by step (all in `tmp/`):
1. `fontTools` subsetting is deterministic (same font+chars → same SHA twice).
2. `webpdf.py` subsets fonts with `fontTools`, and `fontTools` **rewrites
   `head.modified` to the save time** (source Unifraktur modified 2026-11-07 →
   subset modified 2026-11-11T13:10:15, the save moment; `head.created` preserved).
3. Cairo, when embedding a font in PDF, **copies `head.modified` from the source
   font** into its re-subset (web-a embedded font modified = 2026-11-11T13:06:10 =
   that run's subset-save time). The embedded TTF differs between runs in exactly
   3 bytes: `head.modified` low byte + `head.checkSumAdjustment` (derived).
4. Cairo additionally stamps `/CreationDate` (current UTC second) into each rendered
   page PDF (proven: two identical CairoSVG renders differed ONLY in
   `/CreationDate (D:20261111131037Z)` vs `(...1039Z)`); pypdf's merge strips the
   Info dict, so this alone does not change the merged output.
5. Three consecutive `webpdf.py` runs produced three SHAs/sizes
   (885,050 / 885,057 / 885,047 B) — the web PDF SHA is **inherently unreproducible**;
   no re-render can ever reproduce the brief's `427e9c26…`.

Consequences: the print PDF (system fonts with fixed timestamps) reproduces exactly,
which is why its SHA matched. The web PDF on disk now is content-identical to the
brief's file; the KIT's recorded web SHA is a snapshot of one render. At insertion
time lint re-measures `pdfBytes`/`pdfSha256` from the final file (repo AGENTS.md),
so the coordinator should record the current SHA `10610da1…` (885,050 B).

## Conclusion

**(a) — Ready.** Zero defects. proof1 D1 + D2 fixed and independently re-measured;
P2 title intrusion fixed and independently re-measured (ink 88px clear of the Note box);
full mechanical gates green; 150/150 keys hand-verified against stems, P8 print,
text.md, and core keys; 8/8 pages visually clean. No source files were modified,
committed, or pushed by this proof (only the gate-required re-render, §7).
