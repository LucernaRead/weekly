# GATE-LOG — 2026-W47 it-pt, independent round 3 (re-fan-out 2, core D-2 fix)

Proofer scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-pt/`
Edition: `~/workspace/weekly-git/production/2026-w47/2026-w47-it-pt/`
Environment (every run): `TMPDIR=<scratch>/tmp`, interpreter
`~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0, FreeType 2.14.3),
`PYTHONDONTWRITEBYTECODE=1` where production sources were imported.
Probe (first, passed): `git -C ~/workspace/weekly-git hash-object -w /dev/null`
→ `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`, RC=0; scratch write `probe.txt` OK.
No run.py / rebuild was executed directly against production; all rebuild
verification went through `tools/freeze.py baseline` (which copies sources into
scratch and repoints outputs). Production untouched: 41 files re-hashed before and
after all work — identical (`prod-shas-before.txt` vs `prod-shas-after.txt`, diff empty).

## §1 Identity — on-disk SHA-256 (before any work)

| File | Bytes | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-PT.pdf` | 14,036,607 | `9910d536048ae4975c6e1657827f299abab0d274819f881b648a56d513b65135` |
| `La-Lucerna-VOL4-PT-web.pdf` | 1,294,373 | `f2e390f31fc30d14ff08803244cc66749abafd2acdeb41763ba3800fc5f0d85e` |
| `2026-w47-it-pt.text.md` | 55,718 (1317 lines) | `e01360ae9c401d014a9e0a51779646845a112aac4e8afe912090269c6ffa7302` |

Matches the task brief, FANOUT-REPORT-it2 §1 and WEEKLY-KIT.md §7 exactly.
Pre-refan-out values (backup, for the record): print
`6f74ee92c72d4ca545fb763c268231b05b6970a5e170b943cdc2882a3ce4a477`
(14,036,628 B) / web `f28a563544bcac8998097fc418c94b47f92a650b351518339c9be864a1ada1c4`
(1,294,408 B) / text `2ce7bfe9bb1f58d72b6249c4a2d2cd2bf5d97e028e10d2e3acfc480797627cb8`
(55,739 B).

## §2 D-2 regression (A) — method + values

- `text.md:775/:777`: new sentences exact (see PROOF-NOTE §Regression A).
- Old strings `Le forme sono regolari: andare` / `irregolare al futuro: leggerò`:
  0 in content7.py, text.md, all 8 SVGs, both PDF text layers (whole-document,
  whitespace/arrow-normalised). Only hits in the edition dir are inside
  `WEEKLY-KIT.md:93` (D-2 history quotation).
- New strings in PDF text layers (PyMuPDF, normalised `\s*→\s*`→`→`, whitespace
  collapsed): print P7 L17 ×1 / L18 ×1; web P7 L17 ×1 / L18 ×1; whole-doc ×1 each.
  Raw (un-normalised) exact search returns 0 — the layer breaks the sentences
  across lines (`regolari:\nassaggiare →assaggerò, guardare→\nguarderò.`); see
  PROOF-NOTE O-10.
- New strings in p7 SVG node sequence: L18 ×1 as a single node; L17 across nodes
  7–13; space-stripped concatenation ×1 each; old strings 0.
- Diff vs backup (`scratch-refanout-it2/backup/2026-w47-it-pt/`):
  text.md −21 bytes (55,739→55,718), diff exactly lines 775/777;
  SVG p1–p6/p8 byte-identical, only p7 differs (node diff: 4 opcodes, all inside
  the two D-2 sentences; backup 168 nodes → new 162);
  cards p1–p6/p8 byte-identical, only p7 differs;
  content only content7.py differs (lines 17/18); content12/34/56/8, run.py,
  render.py, bslib4.py, svglib.py byte-identical.

## §3 gates.py (copied from proof2 scratch, SCRATCH + paths repointed to this scratch) — 20/20

Command: `tools/venv/bin/python gates.py pt` → RC=0, log `gates-pt.log`.
Full output (`GATES ALL PASS`):

| # | Gate | Result |
|---|---|---|
| 1 | occlusion 0 flags | PASS — `…/svg: 0 flags` |
| 2 | p8 extract noted count | PASS — noted=150 rc=0 |
| 3 | p8 compare vs core | PASS — verdict=CLEAN keydiffs=[137, 138, 139] |
| 4 | freeze diff fragments explained by translations/furniture (P1–7) | PASS — unexplained_add=[] unexplained_rem=[] |
| 5 | freeze diff report present | PASS — pages=['1'..'8'] |
| 6 | freeze strict-cjk (no added CJK except U+3000) | PASS — rc=1 (strict-cjk exit code), added_cjk={'\\u3000': 8}, non_space={} |
| 7 | print/web text multiset identical | PASS — print_words=7962 web_words=7962 chars_equal=True |
| 8 | web PDF < 7 MB | PASS — 1,294,373 bytes |
| 9 | print PDF size sane | PASS — 14,036,607 bytes |
| 10 | P8 min font ≥ 13 px (9.75 pt) | PASS — min=13.0 |
| 11 | paper #fbfaf6 present | PASS |
| 12 | no gold/brick/near-black | PASS — hits=[] |
| 13 | no VOL.5 in furniture (only preview/disclosure) | PASS — VOL.5 text nodes=3 |
| 14 | VOL.4 present | PASS — count=9 |
| 15 | badge colours A2/B1/B2 | PASS |
| 16 | no double outer frame | PASS — full-page rects=0 |
| 17 | textmd validate | PASS — forward-miss: 0 reverse-miss: 0 |
| 18 | answers count 150 | PASS — edition=150 core=150 |
| 19 | keys 1–150 match core (except 137–139 re-aimed, writing) | PASS — mismatches=[] |
| 20 | notes match translations.py (except 137–140 + writing) | PASS — mismatches=[] table_gaps=[] |

INFO: '·' total occurrences in SVGs: 148 (core had them only in options/gloss lists).
Note: print/web words 7,962 — down 3 from proof2's 7,965, exactly the D-2 deletion
(`andare`, `→`, `andrò,`).

## §4 freeze.py baseline — core AND edition, both 8/8

### Core (as tasked: `--core-svg` → core-it svg; build-copy verified as core-it itself)

Command: `tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out <scratch>/freeze-core`
→ RC=0, log `freeze-core.log`:
`baseline: 8/8 SVGs byte-identical` (repointed: render.py, content12/34/56/7/8.py);
p7 `a7e6afa4473aad5a` — matches FIX-LOG's post-fix p7 hash;
`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`.
Build-copy identity verified: contains `2026-w47-it-zh-cn.text.md` (the core's own
export), `content7.py` grep `regolare al futuro: leggerò` = 1,
build-copy p7 sha256 == shipped core-it p7 sha256 (`a7e6afa4…`). The edition
directory was NOT used as the core — build-copy is core-it itself.

### Edition

Command: `tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-it-pt --core-svg production/2026-w47/2026-w47-it-pt/svg --out <scratch>/freeze-baseline`
→ RC=0, log `freeze-baseline.log`:
`baseline: 8/8 SVGs byte-identical`; p1 0362f854092ef632, p2 decb2052a0f1b027,
p3 c4eb93fb1bb970c1, p4 fe8e81abd24dc9fe, p5 2f4677ba6c80ace3, p6 c9d02d589eda82aa,
p7 5014a4c43bfce9a3 (new D-2 p7; proof2's old p7 was 6b26a3d1…),
p8 c7b5373e4a4da707. `core integrity: shipped core SVGs unchanged` (8 files re-hashed).
Build-copy identity: contains `2026-w47-it-pt.text.md`, D-2 string ×1 in content7.py.

## §5 occlusion_audit.py

- Self-test: `occlusion_audit.py --selftest` → RC=0, `selftest OK: planted classes
  fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1};
  clean controls silent` (`occlusion-selftest.log`).
- Production: `occlusion_audit.py <edition>/svg` → RC=0, `0 flags` (`occlusion-prod.log`).

## §6 p8.py

- `p8.py extract --p8 svg/p8-valutazione.svg --total 150 --json pt/p8-extract.json`
  → RC=0, noted_set = 1..150 (150), keys dict 150 entries (`pt/p8-extract.json`).
- `p8.py compare --core-p8 core-it/svg/p8-valutazione.svg --edition-p8 svg/p8-valutazione.svg --total 150 --json pt/p8-compare.json`
  → RC=0, `status: CLEAN`, core_count=150, edition_count=150, keydiff=[137,138,139]
  (expected re-aimed keys; Q140's key is the Italian sentence in both, so no diff —
  correct behaviour).
- Third-source check (my script, §6 of the run): SVG-printed P8 keys vs
  `text.md` RISPOSTE — 149/150 key-parts exact, zero "key differ" entries;
  Q150 printed key is `✓` by design (text answer: "Texto modelo na secção H abaixo
  (99 palavras)"). The printed key strings carry no note suffix; the full printed
  answer lines (key — note) were verified visually on the 200 dpi P8 render.
- Builder log cross-check: `scratch-fanout-it/pt/build1.log`:
  `flow[P8-keys] ended col 3/3 y=2529 (bottom 2552)`.

## §7 Print PDF re-render from shipped SVGs (rerender.py, read-only)

Command: `tools/venv/bin/python rerender.py` → RC=0, log `rerender.log`:
`rerender-print.pdf` 14,036,607 bytes, sha256
`9910d536048ae4975c6e1657827f299abab0d274819f881b648a56d513b65135` — `cmp` with the
delivered print PDF: **BYTE IDENTICAL**.

## §8 Box-title raster sweep + cream/spill/orphan scan

- `raster_titles2.py` (96 dpi renders of the DELIVERED print PDF in `pages96/`)
  → RC=0, log `raster-titles2.log`: 38 bold ≥21 px box titles measured,
  **37 fit, 1 apparent overflow** — P6 `MINIME DI ESEMPIO　gradi, dati inventati`
  (raster right 1110 vs box right 961) adjudicated NOT an overflow: PIL true ink
  ends 538.2 (422.8 px spare); the raster band catches the twin box's title
  `PROPOSTA ≠ LEGGE` (starts x=1011, same baseline y=1634).
  Tightest: P7 `LA PAROLA　PALAVRA DA SEMANA` fits by 17.0 px (PIL 1845.0 vs 1862.0).
  P1 cifre fits by 36.5 px; P2 frase by 27.0 px; P7 errori by 140.5 px;
  P4 classifica by 29.0 px; P1 índice by 53.8 px.
- Backup对照 for MINIME (required before judging): backup print PDF P6 rendered
  at 96 dpi (`pages96-backup/p-6.png`); same band y1615–1650: ink x-range 112..1222
  and left-box rightmost ink 538 in BOTH new and backup — identical, no regression.
  p6 SVG is byte-identical to the backup file.
- `cream_spill_orphan.py` → RC=1 (exit 1 = orphan flags exist; cream/spill flags 0),
  log `cream-spill-orphan.log`: 29 cream rects scanned, **0 CREAM-X, 0 CREAM-Y,
  0 spill flags**; 3 ORPHAN flags, all byte-identical to core-it nodes (P6 "18.",
  P8 Q129 "due", P8 Q137 "___") — inherited, not defects (PROOF-NOTE O-9).

## §9 Text-layer / web PDF

- `pdftotext` (plain): print 45,787 bytes; web 45,787 bytes — identical, matches KIT §7.
- `pdftotext -layout`: print 106,585 bytes; web 105,156 bytes.
- Gates §3 #7: print/web word multiset identical (7,962 words each, chars equal).
- Web PDF 8 pages, rendered P1 + P8 at 150 dpi (`pages/web-p1.png`, `pages/web-p8.png`)
  — visually identical to print, no tofu.

## §10 Content counts (re-measured, not copied)

- Model text: 99 words (regex word split on the `Testo modello:` line).
- Levels: A2 47 / B1 70 / B2 33 (range items 25–28, 52–55, 141–144 = 4 each); per-page
  Q ranges 1–10 / 11–28 / 29–46 / 47–64 / 65–82 / 83–100 / 101–112 / 113–150
  = 10/18/18/18/18/18/12/38; total 150.
- 8 golden sentences: ×2 occurrences each in text.md.
- NOTE gloss headwords: 32 parsed, 0 missing from articles.
- Chart bars (SVG rect widths): 170 / 204 / 238 / 374 / 442 px = 34 px/° for
  5° / 6° / 7° / 11° / 13°.
- Banned terms (Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu): 0 in text.md.
- U+2019: 0 in text.md and all 8 SVGs. U+FF1A: 14 in text.md, 7 in P8 SVG, 0 in
  P1–P7 SVGs (identical in backup). U+201C/U+201D: 0 everywhere (both builds).
- English function-word scan of text.md (" the ", " and ", " Sunday ", " people ",
  " bridge ", " evening ", " against "): 0 hits. CJK ideographs in SVG text nodes: 0
  on all 8 pages.
- P7 col 3 content end 1667.92 (baseline; builder log 1673.0); P4 col 3 content end
  1135.91 (builder log 1140.45).

## §11 Visual inspection

- Delivered print PDF rendered at 200 dpi, all 8 pages (`pages/p-1.png` … `p-8.png`,
  4063×5625 px each), viewed page by page: no overflow, no overlap, no clipping,
  no tofu, no footer collision. P7 D-2 sentences render cleanly in the A2 column.
- Web PDF P1 + P8 rendered at 150 dpi and viewed: identical to print.

## §12 Evidence files in this scratch

`PROOF-NOTE.md` (this round's verdict), `GATE-LOG.md` (this file),
`gates-pt.log`, `gates.py`, `translations.py`, `validate_edition_textmd.py`,
`raster_titles2.py` / `raster-titles2.log`, `cream_spill_orphan.py` /
`cream-spill-orphan.log`, `rerender.py` / `rerender.log` / `rerender-print.pdf`,
`freeze-core.log` + `freeze-core/` (core baseline build-copy + svg),
`freeze-baseline.log` + `freeze-baseline/` (edition baseline build-copy + svg),
`occlusion-selftest.log`, `occlusion-prod.log`,
`pt/p8-extract.json`, `pt/p8-compare.json`, `pt/freeze-diff.json` (from gates.py),
`pages/p-1.png` … `pages/p-8.png` (200 dpi print renders),
`pages/web-p1.png`, `pages/web-p8.png` (150 dpi web renders),
`pages96/` (96 dpi print renders for the raster sweep),
`pages96-backup/p-6.png` (96 dpi backup P6 render for the MINIME对照),
`prod-shas-before.txt`, `prod-shas-after.txt` (identical — production untouched),
`probe.txt`.
