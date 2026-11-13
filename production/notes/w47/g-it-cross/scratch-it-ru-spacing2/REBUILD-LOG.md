# REBUILD-LOG — W47 it-ru SECOND spacing fix: Newsreader kerning overrun (P8) — probe GREEN, production rebuilt

Date: 2026-11-11 ~23:31–23:55 UTC. Worker: it-ru spacing fix #2 (mechanism + patch + probe + production rebuild).
Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-it-ru/`
(Soort filenames: text file is `2026-w47-it-ru.text.md`,
print PDF `La-Lucerna-VOL4-RU.pdf`, web PDF `La-Lucerna-VOL4-RU-web.pdf`.)

## VERDICT: PROBE GREEN — production print+web PDFs rebuilt, 0 joins, gates 20/20

The first (Medium) fix cleared P7 but left 4 real joins on P8, all at a
Newsreader-run → Noto-Serif-run boundary where the space is the TRAILING
character of the Newsreader run. This second fix addresses that defect
class at its root: **CairoSVG/Pango renders with NO GPOS kerning, while
PIL's `getlength` DOES kern** — so every PIL-measured run was placed
short, and the next run started too early, eating the trailing-space
advance. The fix measures runs in `Page.text` as the sum of single-char
advances (unkerned), leaving `text_w`/`wrap` untouched so line-breaking
is byte-identical to the shipped layout. Probe census: **0 join tokens,
0 boundaries, print AND web** (was: 6 hits — 4 real P8 joins + 2 P7
false positives). Gates 20/20, freeze reproducibility 8/8, SVG text
content byte-identical to the Medium-fix probe. Production PDFs rebuilt
in place via the `run_build.py` wrapper (`--allow-production`) +
`webpdf.py`; print PDF SHA is byte-identical to the probe build.

## 1. BEFORE state (23:31 UTC; svglib.py already carries the Medium fix)

| File | Bytes | SHA-256 |
|---|---|---|
| `2026-w47-it-ru.text.md` | 67,731 | `47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d` |
| `La-Lucerna-VOL4-RU.pdf` (print) | 14,180,915 | `966a9d10c033ed0297cef6d018b23a548dec2b016bc0eb3ecf61440ac2247666` |
| `La-Lucerna-VOL4-RU-web.pdf` (web) | 1,441,243 | `a34df9b05c6c199800509bfaf335fe896635f623d985030f28ecfa41b2e569bc` |
| `svglib.py` (Medium fix) | 21,625 | md5 `781059e6784b789c1179446e15b8f6ad` — VERIFIED first, matches task |

## 2. Mechanism — confirmed independently, with corrected numbers

### 2a. Reproducing the overrun through the REAL pipeline
`exp1_overrun.py`: the exact run pairs from the probe P8 SVG, rendered
via `cairosvg.svg2pdf` → PyMuPDF char bboxes. The V0 (current code)
gaps reproduce the production PDF gaps EXACTLY (0.029 / 1.394 / 1.248 /
1.063 pt), so the isolated experiment is faithful.

### 2b. The D1 leading-space mirror does NOT fit (tested, not assumed)
V1 — trailing space emitted as its own `<text>` element, next run at the
same x — gives gaps IDENTICAL to V0 (0.029 / 1.394 / 1.248 / 1.063 pt).
A space-only `<text>` produces NO glyph/char in the PDF at all
(CairoSVG drops a whitespace-only element); the visible run renders the
same width and the next run's x is unchanged. The defect is not in the
space handling — it is in the visible run's measured width. The D1
mirror was therefore REJECTED on evidence.

### 2c. Root cause: PIL kerns, Pango does not
PIL `getlength` vs sum-of-single-char advances (Newsreader-Regular, 13 pt):

| Run string | PIL whole | Σ singles | PIL kern |
|---|---|---|---|
| `69. A — Filmmaker Festival` | 161.03 | 164.22 | **−3.19** |
| `114. A — 24` | 69.36 | 70.66 | **−1.30** |
| `91. A — DPB` | 73.31 | 74.86 | **−1.55** |
| `119. A — BookCity` | 110.83 | 112.28 | **−1.45** |
| `65. B — BookCity` (control) | 103.00 | 103.50 | −0.50 |
| `8. B — 24` (control) | 53.73 | 54.08 | −0.34 |

Needed correction from the PDF gaps (nominal space advance − measured
gap): Festival +3.13, 114/24 +1.32, DPB +1.50, BookCity +1.47,
controls +0.48/+0.33. Each matches its PIL kern magnitude to ≤0.06
units (the residual is the last glyph's right side bearing, exactly as
the gap formula predicts). **Pango's advance = the unkerned sum.**

Cross-check on the other faces (same method, fragment renders):
- Noto Serif Cyrillic (Medium): kern = **0.00** for `закрывается`,
  `гола`, `отправлен`, `открывается` — the Medium fix is unaffected.
- Noto Sans Cyrillic (Medium, 19.5 pt): kern −1.56 (`Гаттузо`),
  −1.75 (`Текст`), 0.00 (`Команда`). Fragment `Текст ` → `Text`:
  positioned by PIL-whole → gap 2.501 pt; by singles → **3.817 pt**,
  i.e. the true nominal space advance (5.06u = 3.80 pt). Pango does
  not kern Noto Sans either. (This also explains the two P7 residuals
  staying just under the normal gap range in the Medium probe.)

Corrected vs the first log's §5: the PNG-ink overruns (+5.97 etc.)
overstate the PDF effect; the PDF-pipeline overrun is the kern sum
(+3.19 max). The mechanism (PIL-vs-Pango shaping difference on
Newsreader runs) is confirmed; the precise form is GPOS kerning
applied by PIL and not by the renderer.

## 3. The fix (`svglib.py`, it-ru's own copy — no other edition imports it)

`_run_w(kind, bold, cls, size, t)` = sum of cached single-char
advances; used ONLY inside `Page.text`:
- `total` (anchor middle/end) — was `getlength` per run, now `_run_w`;
- per-run advance `w` — now `_run_w` (was `getlength`);
- leading-space advance `_lw` and the re-measured `w` after stripping
  leading spaces — now `_run_w`.

`text_w` and `wrap` are UNTOUCHED (still kerned `getlength`), so
line-breaking, flow heights, and line counts are byte-identical to the
shipped layout — no reflow anywhere. The only geometry change is a run
boundary's x moving right by that run's kern magnitude, i.e. exactly
the overrun, wherever it occurs; gaps only grow, never shrink. A line
can render at most ~3–6u past its PIL-measured width, inside the 28u
column gutter. `svglib.py` is a per-edition copy (11 W47 editions share
the Medium-fix md5, none imports it-ru's file; verified by md5 survey +
no cross-edition imports), so the change is gated to it-ru by
construction. New md5: `ee3211298f274e02ade2d4ca318ce354`
(`_run_w("69. A — Filmmaker Festival ")` = 167.39 vs PIL 164.20;
`text_w` still 164.2).

## 4. Probe build (scratch only)

- `tools/venv/bin/python tools/run_build.py --build
  production/2026-w47/2026-w47-it-ru --out
  tools/scratch/run-build/it-ru-spacing2 --steps run,render` → RC=0,
  print PDF 14,179,828 B; wrapper integrity: "production unchanged
  (41 files re-hashed)".
- `tools/webpdf.py <scratch>/build-copy/svg
  <scratch>/build-copy/La-Lucerna-VOL4-RU-web.pdf` → 1,440,147 B,
  53,087 text bytes, RC=0.
- Probe SHAs: print
  `7e9a384300a6e77625fecddd3b225f313d8d040e5bb29c91fa9612a6ec7db931`,
  web
  `684afbc4540374e59765408ef8f2647e3ef7f801e48dfa9dce74bf8c1e8c4447`.
- Production SHAs re-verified immediately after the probe: identical
  to BEFORE (§1).
- Second independent rebuild (`--out
  tools/scratch/run-build/it-ru-spacing2b`) → **8/8 SVG SHA match**
  vs first probe build (freeze/reproducibility); the two print PDFs
  are also byte-identical (same SHA `7e9a3843…`), so the PDF build is
  deterministic. The `-2b` dir is kept for the record (its build-copy
  web PDF is the stale copied production file, not a fresh build —
  only its SVGs/print PDF were used for the freeze check).
- SVG text-node multisets probe2 vs probe1 (Medium-only): IDENTICAL
  on all 8 pages (368/335/319/299/351/330/422/1469 nodes) — zero
  content change, positions only. (The gates' pdftotext word count
  moved 7696 → 7718 purely by tokenization of the widened gaps;
  chars_equal=True.)

## 5. Census + gaps on the probe build (print AND web identical)

Naive full census (`census.py`, text.md vocabulary):

| | BEFORE (production) | Medium probe | THIS probe |
|---|---|---|---|
| distinct join tokens | 78 | 6 | **0** |
| total join boundaries | 147 | 6 | **0** |

Separated ink gaps (`gap2.py`, PyMuPDF rawdict), print = web:

| Split | BEFORE gap | PROBE gap | Verdict |
|---|---|---|---|
| P7 `Гаттузо` \| `остаётся` | 0.48 pt | **3.25 pt** | separate (was false-positive at 2.05 in Medium probe) |
| P7 `Текст` \| `ещё` | 0.86 pt | **3.33 pt** | separate (was false-positive at 1.97 in Medium probe) |
| P8 `Festival` \| `закрывается` | 0.03 pt | **2.43 pt** | separate (predicted 2.42) |
| P8 `DPB` \| `отправлен` | 1.25 pt | **2.37 pt** | separate |
| P8 `24` \| `гола` (#114) | 1.39 pt | **2.37 pt** | separate (control #8 also 2.34) |
| P8 `BookCity` \| `открывается` (#119) | 1.06 pt | **2.42 pt** | separate (control #82 also 2.37) |

Visual crops (`p8-festival2.png`, `p8-dpb2.png`, `p8-24gola2.png`,
`p8-bookcity2.png`, 200 dpi from the probe print PDF): all four lines
visibly separated — "69. A — Filmmaker Festival закрывается в Милане",
"91. A — DPB отправлен в Брюссель 15 октября",
"114. A — 24 гола в 11-м туре",
"119. A — BookCity открывается 23 ноября".

## 6. Gates on the probe build — 20/20 PASS

`gates2.py` (copy of the Medium probe's `gates-probe.py`, repointed at
this scratch dir; outputs under this dir, `ru/`): **GATES ALL PASS** —
occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff
[137,138,139]; freeze diff 0 unexplained (P1–7); strict-CJK added =
8×U+3000 only; print/web text multiset identical (7,718 words each,
chars equal); web 1,440,147 B < 7 MB; print 14,179,828 B sane; P8 min
font 13.0 px = 9.75 pt; §1.1 scans pass (paper #fbfaf6, no
gold/near-black, VOL.4×9, VOL.5×3 legitimate, badges OK, no double
frame); textmd validate 0/0; answers 150/150; keys 1–150 match core
(except 137–139 + writing); notes match translations.py.

## 7. Production rebuild (probe green → in place)

- `tools/venv/bin/python tools/run_build.py --build
  production/2026-w47/2026-w47-it-ru --out
  production/2026-w47/2026-w47-it-ru --allow-production --steps
  run,render` → RC=0 (23:51 UTC). The build still ran in
  `<out>/build-copy`, never in the edition dir itself; the build-copy
  was byte-identical to the probe (print SHA `7e9a3843…`, all 8 SVGs
  match).
- Promoted from the build-copy: `svg/*.svg`, `cards/*.png`,
  `La-Lucerna-VOL4-RU.pdf`. Then `tools/webpdf.py
  production/2026-w47/2026-w47-it-ru/svg
  production/2026-w47/2026-w47-it-ru/La-Lucerna-VOL4-RU-web.pdf` →
  1,440,142 B, 53,087 text bytes, RC=0. Build-copy + wrapper
  `run-build.log` removed from the edition dir afterwards.
- Production web PDF SHA (`3ac0fa44…`) differs from the probe web
  build (`684afbc4…`, 1,440,147 B) by 5 bytes in font-subset streams
  only: decompressed comparison shows ONLY font objects differ (39
  objects, same decompressed lengths, first diffs at bytes 34–66 —
  glyph-order inside the subset); page content streams are identical.
  Verified: `pdftotext` output identical, and all 8 pages render
  pixel-identical at 150 dpi. `webpdf.py` font subsetting is
  non-deterministic across processes (hash order); any future web
  rebuild will differ again in the subset bytes only.
- Production final state (23:54 UTC):
  - text.md: 67,731 B, sha256 `47c04715…`, mtime 21:48:13 — UNCHANGED.
  - Print PDF: 14,179,828 B, sha256
    `7e9a384300a6e77625fecddd3b225f313d8d040e5bb29c91fa9612a6ec7db931`
    (= probe SHA), mtime 23:52:06.
  - Web PDF: 1,440,142 B, sha256
    `3ac0fa4421b1d068c164bbafbf186ff45c944c457523db554d7135548add8faa`,
    mtime 23:54:06.
  - svglib.py: 23,011 B, md5 `ee3211298f274e02ade2d4ca318ce354`, mtime 23:31:25.
- Post-rebuild verification ON PRODUCTION: census 0/0 print + web
  (`census-prod-print.json`, `census-prod-web.json`); separated gaps
  identical to the probe (§5); gates `gates3.py` (EDROOT repointed at
  production) **20/20 ALL PASS** (`gates3.log`); print/web text
  multiset identical (7,718 words each, chars equal).
- KIT updated: §7 Deliverables block → new SHAs/bytes; svglib bullet
  notes the fix; new **§14** fix record (mechanism, probe, production
  SHAs, blast radius). Note: the task brief's "§5 SHAs" does not match
  this file — §5 is Images; the SHAs live in §7, which is what was
  updated. No commit, no push, no lint. No other edition touched.

## 9. Severity judgments vs wave-C calibration (parent handoff 2026-11-11 ~23:54 UTC)

Wave C (core-ru / ru-zh-tw / ko, Medium-fix scratch rebuilds) measured
11 second-class joins, identical in core-ru and ru-zh-tw (ko +1),
pre-existing, gaps essentially unchanged by the Medium fix (Δ ≤ 0.08
pt). Judgments, with numbers:

- DATE cases — CONFIRMED joins, same class as this fix. `19ноября`
  P2 2.19→2.11 pt, `20ноября` P4 2.18→2.18 pt, `16ноября` P5
  2.32→2.24 pt, `13ноября` P8 1.50→1.43 pt. Structure: Newsreader
  run `': 19 '` + Noto Serif `ноября`. At body sizes the normal median
  is ~3.46 pt (14.2 pt), so 2.11–2.24 pt is genuinely narrow; at P8
  size (9.75 pt) the normal median is 2.36 pt and `13ноября` at
  1.43–1.50 pt sits below the 1.80 pt separated floor — consistent
  with my sweep verdict (JOIN) and with the Newsreader-kern mechanism
  (digit runs kern too). The same `_run_w` fix corrects them.
- ARROW cases — NOT joins (my call). P8 `→выходят`,
  `→рассказывает`, `→снял`, `→сыграли`, `→играет`, `→победило`,
  `→работаем`, all 2.32–2.41 pt unchanged. That sits AT the normal
  median (2.36 pt at 9.8 pt NotoSerif-Medium) — the ink gap IS a
  normal inter-word space. The only signal is the missing space
  character in text extraction. Mechanism (verified in this task's
  V1 experiment): the space is a whole Newsreader run between a CJK
  SC `→` run and a Cyrillic run; `Page.text` emits it as a space-only
  `<text>` element, and CairoSVG drops whitespace-only elements
  entirely (no glyph in the PDF), so extraction merges the neighbours
  — but the Cyrillic run's x already includes the space advance and
  the rendered gap is normal. This is a text-layer extraction
  artifact, visually fine; fixing it (attaching the space to an
  adjacent run so a glyph is emitted) is a different, text-layer-only
  change, out of this fix's scope — NOT done here. (it-ru itself has
  NO arrow+Cyrillic sequence anywhere: 32 arrows in text.md, 27 in
  the PDF, all followed by Latin/`___`/punctuation — verified by
  SVG-node, text.md, and PDF scans — so the question does not affect
  it-ru's 0-joins verdict.)
- ko's extra token `а는대조를나타냅니다` P8, 2.43→2.44 pt — NOT a
  visual join, and NOT in this fix's scope. Structure: CJK SC run
  `는` + space + CJK SC `대조를` — same family as the ARROW cases
  (space-only Newsreader run → no glyph in the PDF → extraction
  merges), but CJK→CJK, not Latin→Cyrillic. The gap (2.43–2.44 pt)
  is at/above the normal median, so there is no visual defect to
  fix; `_run_w` applies to CJK runs too but changes ~nothing there
  (CJK faces carry ~zero kern and the gap is already normal). The
  extraction-artifact half is the same out-of-scope item as the
  ARROW cases.
- `ГЛАГОЛЫИ` P3, 2.62 pt — NOT chased: known bold-caps PyMuPDF bbox
  artifact from the ru-de probe, not a join (per the handoff).
- Wave-C re-rebuild flag (NOT my job): the wave-C Medium-fix
  rebuilds of core-ru / ru-zh-tw / ko must be re-run from scratch
  after this fix lands, because `_run_w` changes measurement again.
  Separate note, also NOT my job (a layout worker is on it):
  core-ru's P8 Morozko image + caption are LOST in the Medium-fix
  rebuild (keys flow grew 2188.39→2216.58, tripping the
  `content8.py:131–140` conditional) — flagged only so the
  re-rebuild is expected.

## 8. P8 sweep — other Russian-text editions (CURRENT production PDFs, report only)

Method: `sweep_p8.py` — extract P8 of each edition's current production
print PDF, run the shared `census.py` on it, classify each join token by
split shape. LAT->CYR = left part ends Latin/digit, right part starts
Cyrillic (this defect class). Gap-None LAT->CYR hits were adjudicated
individually with `adjudicate.py` (rawdict ink gap + context; one
visual crop for the shared ru-core `13ноября` line). Counts below are
the NAIVE census; CJK/Korean editions carry many false positives
(Korean/CJK words with normal 2.3–2.7 pt gaps flagged as "joins" by
token concatenation, and within-word splits like `ANTWOORDEN` =
ANTWOORD+EN at gap 0.0) — only the LAT->CYR column is this defect
class, and only adjudicated gaps < 1.8 pt count as real joins.

BLAST RADIUS — LAT->CYR real joins on P8 (all verified by ink gap):

| Edition | Token | Gap (pt) | Verdict |
|---|---|---|---|
| 2026-w47-nl-ru | `aankomenтребует` | 1.44 | JOIN — "39. is aangekomen — aankomenтребует zijn: …" |
| 2026-w47-pt-ru | `vencerпрошедшее` | 0.77 | JOIN — "106. venceu — vencerпрошедшее время: venceu" |
| 2026-w47-zh-cn-ru | `IGобыграла` | 1.32 | JOIN — "47. A — IGобыграла TES 3:1 в четвертьфинале." |
| 2026-w47-zh-cn-ru | `GENвышла` | 1.45 | JOIN — "116. A — GENвышла в финал, а IG — нет." |
| 2026-w47-ru-de | `13ноября` | 1.43 | JOIN (same core line in all 10 ru-*; see crop) |
| 2026-w47-ru-en | `13ноября` | 1.50 | JOIN (same core line) |
| 2026-w47-ru-es | `13ноября` | 1.50 | JOIN (same core line) |
| 2026-w47-ru-fr | `13ноября` | 1.50 | JOIN (same core line) |
| 2026-w47-ru-it | `13ноября` | 1.43 | JOIN (same core line) |
| 2026-w47-ru-ja | `13ноября` | 1.43 | JOIN (same core line) |
| 2026-w47-ru-ko | `13ноября` | 1.50 | JOIN (same core line) |
| 2026-w47-ru-nl | `13ноября` | 1.43 | JOIN (same core line) |
| 2026-w47-ru-pt | `13ноября` | 1.43 | JOIN (same core line) |
| 2026-w47-ru-zh-tw | `13ноября` | 1.50 | JOIN (same core line) |

Cleared (census hit, NOT this defect): zh-cn-ru `BLGобыграла` —
already SEPARATE, gap 1.80 pt (census `words()` merged across a normal
gap; false positive).

Note on `13ноября` (gap 1.43–1.50 pt): below the 1.80 pt floor for
separated Latin→Cyrillic boundaries at this size, same Newsreader-kern
mechanism (run "… A. 13 " under-measured); visually tight but legible
— see `sweep-ru-de-13noyabrya.png` ("Когда «чёрная пятница» на Ozon?
A. 13 ноября – 2 декабря ·"). The same `_run_w` fix corrects it.
The ru-* editions share one Russian core, so this is ONE core line
replicated across 10 editions, not 10 independent defects.

Full P8 naive-census counts per edition (context only — includes the
other defect classes and census false positives):

| Edition | P8 joins (naive) | LAT->CYR | Other |
|---|---|---|---|
| de-ru | 1 | 0 | 1 (`Германиюпротив`, gap None) |
| en-ru | 0 | 0 | 0 |
| es-ru | 2 | 0 | 2 (Cyrillic→Cyrillic, gap None) |
| fr-ru | 0 | 0 | 0 |
| ja-ru | 1 | 0 | 1 (Japanese long token, gap None) |
| ko-ru | 91 | 0 | 91 (Korean tokenization FPs; gaps 2.34–4.42) |
| nl-ru | 5 | 1 | 4 (incl. `ANTWOORDEN` within-word FP at 0.0) |
| pt-ru | 1 | 1 | 0 |
| ru-de | 1 | 1 | 0 |
| ru-en | 24 | 1 | 23 (core Cyrillic joins, gaps 1.05–1.88 — the Medium-fix class, NOT this fix) |
| ru-es | 24 | 1 | 23 (same core text as ru-en) |
| ru-fr | 24 | 1 | 23 (same core text) |
| ru-it | 2 | 1 | 1 (`SETTIMANALE` within-word FP at 0.0) |
| ru-ja | 2 | 1 | 1 (CJK+Cyrillic mix, 1.2 pt) |
| ru-ko | 112 | 1 | 111 (Korean FPs + core Cyrillic joins) |
| ru-nl | 1 | 1 | 0 |
| ru-pt | 1 | 1 | 0 |
| ru-zh-tw | 62 | 1 | 61 (CJK FPs + core Cyrillic joins) |
| zh-cn-ru | 24 | 4 (3 real + 1 cleared) | 20 (CJK FPs + Cyrillic joins) |
| zh-tw-ru | 3 | 0 | 3 (`30分鐘` gap −0.3 — CJK/digit overlap class, needs its own look) |

Caveats: (1) the ru-* "other" Cyrillic joins (e.g.
`заказываетподарок` 1.05–1.13 pt) are the Medium-fix defect class —
they belong to the ru-core Cyrillic measurement, not to this fix, and
are listed here only so the coordinator sees the full P8 picture.
(2) The Cyrillic right-hand font in the *-ru editions is
NotoSerifCJKsc-Regular (older svglib variant, no Medium face) — the
`_run_w` fix is face-independent (it corrects whatever PIL measures
for the run's face), but those editions need the patch applied to
THEIR svglib.py copies. (3) Sweep ran on production PDFs as of
2026-11-11 ~23:47 UTC; no edition was rebuilt by this worker.

## Files in this scratch dir

- `REBUILD-LOG.md` (this file), `census.py`, `gap_probe.py`,
  `gap2.py` (separated-gap measurement), `calib.py`, `render_truth.py`,
  `exp1_overrun.py` (V0/V1/V3 pipeline experiment),
  `gates2.py` (+ `gates2.log`, probe gates), `gates3.py` (+
  `gates3.log`, production gates), `translations.py`, `ru/` (gates
  JSONs), `census-probe-print.json`, `census-probe-web.json`,
  `census-prod-print.json`, `census-prod-web.json`,
  `sweep_p8.py` (+ `sweep.log`, `sweep.json`), `adjudicate.py`,
  `p8-festival2.png`, `p8-dpb2.png`, `p8-24gola2.png`,
  `p8-bookcity2.png` (probe visual crops),
  `sweep-ru-de-13noyabrya.png` (sweep visual crop),
  symlink `2026-w47-it-ru` →
  `tools/scratch/run-build/it-ru-spacing2/build-copy/` (probe build).
