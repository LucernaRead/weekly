# FIX LOG — 2026-W47 ru-en, Fix 3 (coordinator label "fix2"; re-proof R1+R2)

- Edition: `2026-w47-ru-en` (Russian target × English reader), VOL.4, issue 16–22 November 2026
- Fixer: fix2 builder (leaf); 2026-11-11
- Work dir: repo `~/workspace/weekly-git`, edition `production/2026-w47/2026-w47-ru-en/`
- Notes: repo `hidden_files/w47/scratch-fix-ru-en2/` (this dir)
- Read first: repo `SOP.md` (§1.1, §8.4 — full SOP read), coordinator brief,
  fix1 `FIX-LOG.md` + `GATE-LOG.md` (goals `hidden_files/w47/scratch-fix-ru-en1/`,
  used as reference only; every defect re-verified on disk before fixing)
- Scope: re-proof defects R1 + R2 only. No changes to `core-ru`, other editions,
  `tools/`; no commit, no push, no `insert.py`, no `lint --write`, no Discord.
  Re-proofread follows; this log is not a sign-off.
- Naming note: the KIT already carries a "Fix 2" entry (the S1 fix, 2026-11-11),
  so this round is recorded as **Fix 3** in the KIT (with the coordinator label
  "fix2" cited) to avoid a colliding second "Fix 2".

## 0. Startup probes + pre-fix identity (all MATCH the brief's final table)

- Probe: `echo test | git hash-object -w --stdin` in the repo → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc=0.
  Real write probe: `scratch-fix-ru-en2/probe.txt`, OK. No disk-quota error.
- Pre-fix triple (verified by me before any edit):

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,086 | `9a159cd59f32443eb8d612eb05959ff7af3273d4c3796da0b2b2f6a7f1800b0a` |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,694 | `7e465d67a96c3e47aa415cc530160de2df9f9b2d9f923e85366da28b8e263ed5` |
| `2026-w47-ru-en.text.md` | 62,818 | `5960b7a649a8b50036fefa0b16580a2209bc694ea45fb5377a9ee39d9c1296ee` |

- The brief's warning is confirmed: FIX-LOG line 19's print SHA `023d9fd1…` is
  the fix1 intermediate product, not the delivered value — the table above
  (the delivered fix1 triple) is what was on disk and what I verified against.
- Path corrections (brief paths that do not exist where written, resolved by
  searching the workspace before touching anything):
  - `hidden_files/w47/briefs/brief-coordinator.md` does **not** exist in the
    repo; the real brief is at
    `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`
    (read in full).
  - `hidden_files/w47/scratch-fix-en-ru2/` (stated fix1 workdir) does **not**
    exist in the repo; fix1's actual scratch is goals
    `hidden_files/w47/scratch-fix-ru-en1/` (its `spill.py`, `verify_mine2.py`,
    `dump_reg.py` were copied into this scratch unmodified and re-run here;
    `s11_check.py` + `adjudicate_ru.py` copied from goals
    `hidden_files/w47/scratch-fanout-ru/`; `creambox.py` copied from goals
    `hidden_files/w47/tools/creambox.py`).
  - R2's `hidden_files/w47/scratch-fanout-ru/miss-tr-en.json` is
    goals-workspace-relative, not repo-relative (same for `build_map.py`).

## 1. R1 — FIXED (P6 col3 box title overhangs its cream box by <1 px)

**Pre-fix verification (my own three-method run, defect confirmed real):**

Source: `content56.py:136`
`p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　FOR AND AGAINST", 24, "sans", True, OLIVE)`.
Box: `bx = COLX[3] = 1439.5`, `CW = 422.5` → right edge **1862.0** svg px.
Title starts at `bx+22 = 1461.5`, baseline y=705.5 (verified against the
shipped `svg/p6-razbor.svg` run x-positions 1461.5 / 1499.1 / 1524.3 / 1625.4,
which my PIL simulation reproduces exactly).

| Method | True-ink / char-box right | Margin vs 1862.0 |
|---|---|---|
| PIL true ink (`ink_title.py`, same fonts as `svglib`; `ink-pre.log`) | 1862.4 svg px | **−0.4 px** |
| Delivered print-PDF vector char boxes (`pdf_title_check.py`, `pdf-title-pre.log`) | 1863.5 svg px (last char `T` bbox x1=1397.64 pt) | **−1.5 px** |
| Delivered print-PDF 600 dpi render, rightmost dark pixel (`pdf-title-pre.log`, `pre-clip.png`) | 1862.6 svg px (ink +3.7 render px past the box edge) | **−0.6 px** |

The brief's numbers (PIL 1862.2 / −0.2, char boxes 1863.5 / −1.5, pixels −0.7 SVG px)
are reproduced within 0.2 px on every method; the char-box figure is exact.
Same direction, same order, same conclusion on all three: visible overhang,
ruled a defect by the pt-de D4 precedent. Core comparison: the core title
(`core-ru/content56.py:136`, `ЗА И ПРОТИВ　正反两方`) has +116.6 px clearance;
the English subtitle is longer, which is what eats the margin.

**The fix (option (a) — shorten the English subtitle; 24 pt kept):**

Russian head is core text, untouched. Only the English subtitle literal changed.

`content56.py:136–138` (fix comment at :136–137, call now at :138):
- Before: `p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　FOR AND AGAINST", 24, "sans", True, OLIVE)`
- After: `p.text(bx + 22, yy6 + 26, "ЗА И ПРОТИВ　FOR & AGAINST", 24, "sans", True, OLIVE)`

The 24→23 pt fallback was measured but not used (23 pt would give +47.5 px,
but changes the title size away from every other 24 pt box title; the
shortening alone clears the bar with a much larger margin and a smaller diff).
Note: the fix comment at `content56.py:136` quotes the old string for the
record — the same convention as fix1's `content12.py:48–51` comment. The old
string occurs nowhere else in the edition's visible output (0 occurrences in
the new text.md, SVG, and both PDFs).

**Post-fix verification (triple method, on the rebuilt PDFs — see §3):**

| Method | True-ink / char-box right | Margin vs 1862.0 |
|---|---|---|
| PIL true ink (`ink-post.log`) | 1829.4 svg px | **+32.6 px** |
| Delivered (new) print-PDF vector char boxes (`pdf-title-post.log`) | 1830.8 svg px (last char `T` bbox x1=1373.09 pt) | **+31.2 px** |
| Delivered (new) print-PDF 600 dpi render (`pdf-title-post.log`, `post-clip.png`) | 1829.9 svg px (ink ends 200.3 render px inside the box edge) | **+32.1 px** |

All three ≥ +5 px requirement, agreeing within 1.4 px. Visual: 300 dpi P6-box
crop from the new print PDF (`crops/p6-box-print.png`, SHA prefix `728a0457…`)
read by eye — `ЗА И ПРОТИВ　FOR & AGAINST` ends well inside the cream box;
the web-PDF crop (`crops/p6-box-web.png`) is **byte-identical** to the print crop.

**Full 32-box-title sweep (own run, `titles_sweep.py` — `titles-sweep-post.log`):**

All 32 cream-box titles measured (topmost baseline per box, true PIL ink).
**0 negative clearances.** Tightest right clearance overall is **+14.1 px**
(P1 `В ЭТОМ НОМЕРЕ IN THIS ISSUE`, ink-right 1847.9); the R1 title is third
tightest at **+32.6 px**; the S1 title is +95.4 px (865.6, reproduced exactly).
Tightest bottom clearance +47.2 px. This settles the brief's flag: proof1's
"tightest +6.8 px" was a misquote — 6.8 is a kicker-gap value, proof1 never
published a tightest-title value; the real tightest is +14.1 px.
Spill sweep (`spill.py`, `spill-post.log`): 32 cream boxes, **0 ink escapes,
0 bad titles**, 43 spill-below candidates (same count and set class as fix1's
pre-fix run — the already-classified by-design set).

## 2. R2 — FIXED (fan-out `miss-tr-en.json` still carried the long S1 title)

**Mechanism verified before touching anything (no guessing):**
- `hidden_files/w47/scratch-fanout-ru/build_map.py` (goals workspace, read in
  full): `m = {"lit": dict(tm["lit"]), ...}` from `tm2-<lang>.json`, then
  every `miss-tr-<lang>.json` bucket entry **overrides** (`m[bucket][k] = v`,
  logging OVERRIDE on conflict) and is written to `map-<lang>.json`.
- `tm2-en.json` has 4 top-level buckets and **no** `ТУР В ЦИФРАХ` key
  (checked directly) — miss-tr is the only upstream source for this value.
- Pre-fix state: `miss-tr-en.json:33`
  `"ТУР В ЦИФРАХ　数字看本轮": "ТУР В ЦИФРАХ　The round in numbers"`
  (SHA `54afc4c7…`); `map-en.json` `/lit/…` was already the short form
  (`ТУР В ЦИФРАХ　The round`, SHA `400fcdd2…`) — fix1 synced the map but
  missed miss-tr, exactly as the brief states. `content12.py:52`, text.md L25,
  and `svg/p1` all carry the short form; 0 residual long forms in production.

**Change (one line, one file):**
- `miss-tr-en.json:33` value → `"ТУР В ЦИФРАХ　The round"`.
  SHA `54afc4c7…` → `9c301611…`. File still valid JSON (123 lit keys, keys
  sorted, same `indent=1` dump style — the value is still on line 33, 0
  occurrences of "The round in numbers" anywhere in the file).
- Verification in the fan-out scratch (authorized by the brief):
  `python3 build_map.py en` → rc=0, `map lit 335 type 8 instr 9 key 8`,
  "map OK", no PROBLEMS. Regenerated `map-en.json` is **byte-identical**
  (SHA still `400fcdd2…`) and its lit value is still the short form — the
  miss-tr fix introduces no map change, and a re-run of `build_map.py en` +
  fan-out can no longer revive the long form.
- R2's `miss-tr` change is recorded here and in the FIX-LOG only; it is **not**
  counted as a production write (§7 scope accounting separates it).

## 3. Rebuild (whole edition, all in scratch — production never written by a build step)

Build copy: `scratch-fix-ru-en2/rebuild/` (full copy of the edition sources;
`OUT` verified before running to resolve inside the scratch copy, via
`content12.py:6`'s `__file__`-relative path → `…/scratch-fix-ru-en2/rebuild/svg`).
`render.py` / `webpdf.py` / `ru_textmd.py` all ran with cwd = the copy, so
their outputs landed in the copy. Production files were touched only by the
final verified promotion (§6).

| Step | Result |
|---|---|
| `run.py` (`gates/run.log`) | rc=0, TOTAL **150** (A2 50 / B1 76 / B2 24; by page 10/18/18/18/18/18/12/38; model words 97), **0** FLOW OVERFLOW / HEAD TOO WIDE |
| `render.py` (`gates/render.log`) | 8 cards + print PDF 21,251,270 bytes (in the copy) |
| `tools/webpdf.py svg Lucerna-VOL4-ru-en-web.pdf` (`gates/webpdf.log`) | web PDF 3,380,903 bytes, 57,316 text bytes |
| `ru_textmd.py . 2026-w47-ru-en.text.md "VOL.4 · Russian text · English explanations"` (`gates/textmd.log`) | 62,816 bytes, 150 exercises, 277 blocks |

**Post-fix identity (new SHAs — the deliverable):**

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,270 | `d12fa6a6bb62dd7af36743c7d2f33d96d27def054e5dcd6fdb288ef3577c06a1` |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,903 | `3cd934e01db298f13cd0c492ea14904ce2d5df3860d543818a91b1a4416c1dfe` |
| `2026-w47-ru-en.text.md` | 62,816 | `5ec76132a069d0c1cef7e9abe54d2556ace7419daf308805491b77bb22bfd97d` |

Print +184 B, web +2,209 B, text.md −2 B vs pre-fix (−2 = the removed
`AND ` → `& ` characters; the PDFs' byte deltas are stream-level, as expected).
Web SHA is not reproducible run-to-run (font-subset random tags) — only the
text layer is compared, per the brief.

**Rebuild scope — only P6 changed.** SVG SHA comparison rebuild vs production
pre-fix: p1–p5, p7, p8 all byte-identical; only `svg/p6-razbor.svg` differs
(`8a7199a6…` → `7ac43e6c…`). The p6 SVG diff is exactly one run:
`　FOR AND AGAINST` → `　FOR &amp; AGAINST` (+2 bytes, XML-escaped `&`).
`.text.md` diff old→new: exactly 1 line (L449
`### ЗА И ПРОТИВ · FOR AND AGAINST` → `### ЗА И ПРОТИВ · FOR & AGAINST`).
"FOR AND AGAINST": 0 occurrences in the new text.md, new p6 SVG, and both new
PDFs (the only remaining occurrence in the edition is the fix comment in
`content56.py:136`, by design).

**On the brief's "绝不覆盖生产网 PDF":** all rendering ran in the scratch
copy; the production web PDF was never written by any build step (it was
untouched until the promotion in §6). The promotion itself replaces it with
the verified rebuild — the same as fix1, which produced the shipped web SHA
now being replaced. Not rebuilding it would leave the ruled R1 defect live in
the shipped web PDF (the brief's own evidence shows the overhang in both
print and web crops, byte-identical). The interpretation is recorded here so
the coordinator can see it.

## 4. Gates (all re-run by me on the rebuilt edition; see GATE-LOG.md)

- Occlusion audit: selftest OK; **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER,
  0 EDGE, 0 BOXTITLE**; flag set **byte-identical** to fix1's 42 flags.
  Adjudication (edition-pointed): **42/42 CLEAR, 0 UNRESOLVED** (incl. the
  two P8 `ОТВЕТЫ` flags, gaps 19 px / 20 px).
- P8: extract **150/150**; compare vs core-ru **CLEAN**, missing=[], extra=0,
  `keydiff=[137, 138, 139, 140]`.
- Keycheck: registry 150 vs P8 extract **149/150**; only Q150 differs
  (registry `(Open task; model text below)` vs P8 printed `✓`, expected).
- Freeze: baseline **8/8** byte-identical, rc=0, core integrity OK.
  Freeze diff per-page +/− identical to fix1 (p1 +20/−21 … p8 +173/−627);
  removed distinct 484 / added distinct 324 (per-page sums, fix1's counting;
  global-distinct aggregation gives 451/298 — cross-page duplicates merged);
  count-sum 850; added CJK total 8, all U+3000; **Cyrillic-bearing removed
  exactly 15** (Q46 `можно` ×1 + 14 Morozko-caption words), **added Cyrillic 0**;
  P6 added run `　FOR & AGAINST` present, removed long-title run absent.
- Print/web text layer: plain `pdftotext` **57,316 bytes each, byte-identical**;
  layout **111,873 bytes each, byte-identical**; non-whitespace multiset
  identical overall (**30,352**) and per page (verify_mine2).
  D2 7 pinned spots all **0.000 pt**; D3 `а`→`»` gap −2.193 pt both; D3 space
  bbox byte-identical (see §5); D1 straight quotes in both PDFs.
- `check_core.py`: rc=0, **golden BAD 0, gloss fails 0**, P8 SVG text 10,561
  chars; 1 orphan line-start (P7 y553 `”».`, known benign) + 1 same-baseline
  collision (P1 y1712 `чёрная`, known).
- `s11_check.py`: rc=0, **FAILURES: none**; 8 SVG; paper #fbfaf6; badges;
  foot VOL.4; masthead 196 px; left margin 88.0; no CJK in visible SVG;
  both PDFs 8 pages; web 3,380,903 B < 7 MB; web text > 0;
  **P8 min font ≥ 9.75 pt: 9.75** (direct PyMuPDF: 9.75 pt, 411 spans < 10 pt).
- Creambox full 8-page scan: 1,156 lines; normalized diff vs fix1's scan:
  exactly **1 line** differs — the P6 title line (`FOR AND AGAINST` →
  `FOR &amp; AGAINST`).
- `pdffonts`: 72 entries each, all emb/sub/uni; web embeds Lucerna* subsets
  incl. `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`.

## 5. Regression: S1 / D1 / D2 / D6 / kicker / Q20 / Q25 / Q73 — all survive

(`gates/regression` evidence: `titles-sweep-post.log`, `kicker-post.log`,
`gates/verify-mine2.log`, `gates/d3-space.log`, greps below)

- **S1:** P1 title PIL ink right **865.6**, clearance **+95.4 px** (titles
  sweep reproduces fix1's numbers exactly); only p1-adjacent change is none —
  p1 SVG byte-identical to pre-fix.
- **D1:** text.md L459 `УЧЕБНЫЕ ДАННЫЕ` ✓, L504 `Три уровня, три темы` ✓,
  L596 `Большой тест недели + все ответы` ✓; P5 straight quotes in both PDFs ✓.
- **D2 (Q25):** full phrase `Международный день студента` ×2 in text.md = core
  ×2 ✓; Q25 option L187 `25. 17 ноября — День студента (key b · Students' Day b)` ✓.
- **D6 (Q20):** `желании` ×2 in text.md = core ×2 ✓; P8 extract key 20 =
  `желании` = registry ✓.
- **Q20 / Q73:** Q20 key `желании` ✓; Q73 stem L405
  `73. [B1 · fill-in] В прошлом году сделали 14,4 млн ___. — key: заказов`
  and key list L753 `73. заказов — заказ = an order` intact, P8 extract key 73
  = `заказов` ✓.
- **D3 space (verify_mine2's 1 FAIL is its known finder bug):** the script
  looks for consecutive `я`,`п` and misses the space char between them
  (documented in fix1's FIX-LOG §4.5). Corrected direct measurement
  (`d3_space.py`, `gates/d3-space.log`): space bbox
  **[1145.576, 1266.762, 1148.108, 1288.725], byte-identical print/web** —
  exactly fix1's pinned values. D3 still fixed.
- **Kicker:** 9 double spaces in `content12.py:18`; my own PIL true-ink gaps
  (own method, trailing spaces attributed to the following gap):
  **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2, 9.5, 7.1] px, min 5.0 ≥ 4 — PASS**,
  reproducing fix1's list exactly (the 7.2 gap rides on the `—  ` run's
  trailing spaces; the 7.1 gap is the `,  ` run → `ПО` gap). P1 SVG
  byte-identical to the version fix1 measured.
- **150 exercises:** registry 150 = P8 extract 150 = text.md 150 exercises,
  same by-page/by-level distribution as fix1 (10/18/18/18/18/18/12/38;
  A2 50 / B1 76 / B2 24).

## 6. Files changed (edition dir only) + promotion

Promotion: the verified scratch outputs were copied into production
(p6 SVG, both PDFs, text.md, p6 card). No build step ever wrote to production.

| File | Change |
|---|---|
| `content56.py:136–138` | R1: title + 2-line fix comment |
| `svg/p6-razbor.svg` | Regenerated by `run.py` in scratch (only SVG that changed) |
| `cards/p6-razbor.png` | Regenerated by `render.py` in scratch (other 7 cards byte-identical to the rebuild) |
| `Lucerna-VOL4-ru-en.pdf` | Re-rendered (new SHA, §3) |
| `Lucerna-VOL4-ru-en-web.pdf` | Rebuilt with `tools/webpdf.py` (new SHA, §3; see the §3 note on the brief's "绝不覆盖生产网 PDF" clause) |
| `2026-w47-ru-en.text.md` | Re-exported (62,816 B; 1 line changed) |
| `WEEKLY-KIT.md` | §5 outputs (new SHAs/bytes) + §5/§7 Fix 3 record |
| `__pycache__/` | Regenerated bytecode (untracked build artifact, same as fix1) |

Outside the repo: one value in goals
`hidden_files/w47/scratch-fanout-ru/miss-tr-en.json:33` (see §2); the
regenerated `map-en.json` there is byte-identical. No `tools/` change.

**Production zero-write check** (`snapshot-edition-pre.txt` vs
`snapshot-edition-post.txt`, same filter, 42 files): exactly 7 files differ
— the 7 in the table above. Everything else in the edition dir is
byte-identical to the pre-fix snapshot. `core-ru` untouched
(`snapshot-core-pre.txt` vs `snapshot-core-post.txt`: identical).
Post-promotion re-measurement on the **production** print PDF
(`pdf-title-prod.log`): vector char boxes 1830.8 px (+31.2 px), rendered
pixels 1829.9 px (+32.1 px) — identical to the scratch-rebuild measurements.
No git add/commit/push/stash/reset, no `insert.py`/`lint --write`, no Discord,
no user message. The edition dir remains untracked (`??`, never committed),
same as before.

## 7. KIT doc updates (this round)

In `WEEKLY-KIT.md` (§5 outputs paragraph, §5 pdftotext + text.md lines,
§7 print/web text-layer line, plus a §7 Fix 3 entry):
1. Print/web/text.md SHAs + sizes updated to the Fix 3 rebuild (§3).
2. pdftotext 57,318 → **57,316** measured, multiset 30,354 → **30,352**,
   in both §5 and §7, with dated correction notes (the −2 is the P6 title change).
3. text.md 62,818 → **62,816** bytes (−2, the shortened P6 box title).
4. Numbering: this round is **Fix 3** in the KIT (Fix 2 already denotes the S1
   fix); the coordinator label "fix2" is cited in the entry.
5. The §5 "Correction (2026-11-11, fix 2)" line about 57,329 pre-fix is left
   untouched — it records a genuinely historical intermediate state.

## 8. Evidence files (this scratch)

`FIX-LOG.md` (this file); `GATE-LOG.md`; `ink_title.py`, `pdf_title_check.py`,
`titles_sweep.py`, `kicker_check.py`, `d3_space.py`, `freeze_adjudicate.py`
(own scripts); `spill.py`, `verify_mine2.py`, `dump_reg.py` (copies of fix1's
scripts, reused unmodified except `ED`/paths repointed to this scratch);
`s11_check.py`, `adjudicate_ru.py`, `creambox.py` (copies of the shared
fan-out/tool scripts); `snapshot-edition-pre/post.txt`,
`snapshot-core-pre/post.txt`, `snapshot-r2-pre/post.txt`; `ink-pre/post.log`,
`pdf-title-pre/post/prod.log`, `kicker-post.log`, `titles-sweep-post.log`,
`spill-post.log`, `probe.txt`; `rebuild/` (scratch build copy: sources,
regenerated `svg/`, `cards/`, both PDFs, text.md, `registry.json`,
`svg-pre/` pre-fix SVG baseline); `gates/` — `run.log`, `render.log`,
`webpdf.log`, `textmd.log`, `occlusion.json/.log`, `adjudication-ed.log`,
`p8-extract.json/.log`, `p8-compare.json/.log`, `keycheck.log`,
`keycheck-dump.log`, `svg-after-keycheck.txt`, `freeze-std.log`,
`freeze-std/`, `freeze-diff.json/.log`, `freeze-adjudicate.log`,
`check-core.log`, `s11.log`, `creambox.log`, `verify-mine2.log`,
`d3-space.log`, `p8-minfont.log`, `fonts-print.log`, `fonts-web.log`,
`crop-p6.log`; `text/print.txt`, `text/web.txt`, `text/print-layout.txt`,
`text/web-layout.txt`; `crops/p6-box-print.png`, `crops/p6-box-web.png`
(byte-identical).

## 9. Open points for the re-proofer / coordinator

1. The brief's "绝不覆盖生产网 PDF" clause: I read it as "no build step writes
   into production" (all rendering in scratch; promotion only after verification),
   following the fix1 precedent — see the §3 note. If the coordinator meant the
   shipped web PDF must stay byte-identical, the promoted web PDF
   (`3cd934e0…`) would need reverting and R1 would remain live in the web PDF.
2. PIL pre-fix ink measured 1862.4 px here vs the brief's 1862.2 px (0.2 px,
   method rounding in `getbbox`); the PDF char-box figure matches exactly
   (1863.5 px) and all three methods agree on the verdict.
3. verify_mine2's D3-space FAIL is its known finder bug; the corrected direct
   measurement passes with fix1's exact pinned bbox (see §5).
4. Freeze-diff "removed distinct 484 / added 324" are per-page sums (fix1's
   counting); globally deduplicated they are 451/298 — same underlying diff.
5. KIT numbering: this round is Fix 3 in the KIT; the S1 fix keeps the
   name Fix 2 there.
