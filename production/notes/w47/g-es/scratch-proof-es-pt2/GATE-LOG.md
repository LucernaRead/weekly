# GATE-LOG — W47 es-pt proof2 (rebuilt edition)

- **Proofreader:** proof2 (independent), 2026-11-11
- **Work dir (S2):** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-pt2/`
- **Edition:** `~/workspace/weekly-git/production/2026-w47/2026-w47-es-pt/`
- **Core:** `~/workspace/weekly-git/production/2026-w47/core-es/`
- **Runtime:** `~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0 / FreeType 2.14.3)
- **TMPDIR:** `S2/tmp/` throughout (`/tmp` 512M, routinely full — never used)
- **All logs/artifacts below are in S2** unless noted; `pt-*.log/json` are the
  independent re-runs of the `gates-driver.py` driver (copied from
  `scratch-refanout-es/gates.py`, repointed at S2), run fresh in this proof.
  `creambox-all.log` / `creambox-diag.log` / `boxtitle.log` are additional direct
  runs by this proofer (same tools, same inputs).

## 0. Probe + identity (before any gate)

```
ls /dev/null                       -> -rw-rw---- 0 bytes (regular file, NOT a device)
echo test | git -C ~/workspace/weekly-git hash-object -w --stdin
                                   -> 9daeafb9864cf43055ae93beb0afd6c7d144bfa4
echo probe-ok > .../hidden_files/w47/probe-proof-es-pt2.txt   -> OK
sha256sum (pre-proof, 12:54 UTC):
  La-Lucerna-VOL4-es-pt.pdf      3,500,936  0c8dd28550be5ababc176503a426e430546f8357969d8f9104451b10b5c0d6c2  == brief
  La-Lucerna-VOL4-es-pt-web.pdf    885,039  427e9c26d0b055f94e27e06fb659738e7250363e8a0eaf88fe5086f70e099e38  == brief
  2026-w47-es-pt.text.md          45,535  9df4d30caba991aa1f966eccc360cf801b3a6cf9764f448662be5804de06e6c8  == brief
  core-es print                  17,212,955  2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5
  core-es web                     1,410,471  c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235
  core-es text.md (1,822 lines)            509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb
```
`/dev/null` vanished mid-proof (`fatal: could not open '/dev/null'` on a later git
call); restored with `touch /dev/null` per brief instruction, git worked again
(`9daeafb…` re-verified). Core-es SHAs re-measured post-proof: identical to pre-proof.

## 1. Gate name mapping (brief shorthand → concrete run)

| Brief name | Concrete run in this proof | Log |
|---|---|---|
| run | freeze baseline rebuilds the edition from source (8/8) + `render.py` re-render (rc=0) | `pt-freeze.log`, `pt-render.log` |
| occlusion | `tools/occlusion_audit.py <svg>` (+ `--selftest` implied by log line) | `pt-occlusion.log/.json` |
| p8_extract 150/150 | `tools/p8.py extract --total 150` | `pt-p8-extract.log/.json` |
| p8_compare | `tools/p8.py compare` vs core-es P8 | `pt-p8-compare.log/.json` |
| source_freeze | `tools/freeze.py baseline` (rebuild from source, 8/8 byte-identical) | `pt-freeze.log` |
| string_freeze | `tools/freeze.py diff` (per-page string multiset + CJK accounting) | `pt-freeze-diff.log/.json` |
| text_layer print/web | `pdftotext -layout` print + web, byte compare | `pt-print.txt`, `pt-web.txt`, `pt-gates.json` |
| p8_font | `minfont.py` on print P8 (effective size = font_size × \|Tm[0]\|) | `pt-minfont.log` |
| scans | occlusion scan + canonical creambox full scan | `pt-occlusion.*`, `creambox-all.log`, `pt-creambox.log` |
| chips | P8 chip `<rect>` census by fill (A2/B1/B2) vs core | PROOF-NOTE § Gates (scripted count, §4 below) |
| keycheck | `keycheck_core.py` REG vs P8-extracted | `pt-keycheck.log`, `keycheck-150.json` |
| mcq | hand-verification of all 47 `Escolha múltipla` + 15 P8 text-choice items against stems | `items-150.txt` |
| widths | `boxtitle_core.py` advance widths, all 27 titles | `boxtitle.log`, `pt-boxtitle.log` |
| band_spans | P6 RTVE + mini bar `<rect>` widths vs labelled minutes (6.4 px/min) | §5 below |
| canonical creambox | `hidden_files/w47/tools/creambox.py` (md5 `ee7a55d8b2057cf4ad42a97bb1197383`) | `creambox-all.log`, `creambox-core.log` |
| boxtitle true ink | `creambox_diag.py` PIL true-ink bottoms | `creambox-diag.log` |

## 2. Driver summary (`pt-gates.json`, re-run in full by this proof)

```json
{"render_rc": 0, "occlusion_rc": 0, "p8extract_rc": 0, "p8compare_rc": 0,
 "freeze_rc": 0, "freezediff_rc": 0, "creambox_rc": 0, "boxtitle_rc": 0,
 "keycheck_rc": 0, "sweep_rc": 0,
 "print_bytes": 3500936, "web_bytes": 885050,
 "print_sha": "0c8dd28550be5ababc176503a426e430546f8357969d8f9104451b10b5c0d6c2",
 "web_sha": "10610da1250af48d158a1410bc111e417a4cc6ce8c06428c76283fd38c19eefa",
 "text_sha": "9df4d30caba991aa1f966eccc360cf801b3a6cf9764f448662be5804de06e6c8",
 "text_lines": 1815, "pdftotext_rc": [0, 0],
 "print_web_text_equal": true, "print_web_text_bytes": 109215, "minfont_rc": 0}
```

- `render_rc=0`: print PDF re-rendered byte-identical to the brief (3,500,936 B,
  SHA `0c8dd285…`). Web PDF re-rendered 885,050 B / SHA `10610da1…` — content-identical,
  bytes differ only by toolchain timestamps (see §6). `web_bytes` differs from the
  brief's 885,039 for that reason alone.
- `p8compare`: `{"status": "CLEAN", "total": 150, "core_count": 150,
  "edition_count": 150, "missing": [], "extra": [], "uncertain": [],
  "keydiff": [137, 138]}` — read directly from `pt-p8-compare.json`
  (the driver `gates.json` shows no `extra` field; the task brief warned the
  driver misreads that key name).
- `freeze` baseline: `8/8 SVGs byte-identical`, per-page hashes
  p1 `214cfa88…`, p2 `22b0c84f…`, p3 `514ad8e7…`, p4 `413ba104…`, p5 `ed98d2fa…`,
  p6 `b246a479…`, p7 `b4144a3b…`, p8 `f22fde91…`; `core integrity: shipped core SVGs
  unchanged by the run`.
- `freeze-diff`: p1 +29/−38, p2 +51/−52, p3 +34/−30, p4 +33/−27, p5 +44/−47,
  p6 +17/−17, p7 +47/−46, p8 +162/−626; **added CJK chars: 0 on every page, TOTAL 0**.
  (Edition residual CJK per page: 20/16/13/15/14/14/12/14 — all U+3000.)
- `keycheck`: `REG entries: 150; p8extract keys: 150; exact match: 149/150;
  MISMATCH n=150 … extracted='✓'`; `flow[P8-keys] ended col 3/3 y=2521 (bottom 2560)`;
  no OVERFLOW; `TOTAL exercises: 150; by level {'A2': 50, 'B1': 72, 'B2': 28};
  by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38};
  MODELO words: 97`; types: Completar 48, Escolha múltipla 47, Associar 12,
  Verdadeiro/Falso 8, Formar frases 7, Reescrever 10, Escolha no texto 13,
  Tradução 4, Escrita 1.
- `minfont`: `P8 min effective font size = 10.125 pt (n=376)`; below 9.75pt: 0.
- `occlusion`: `selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER,
  LINEX, TEXTX}; clean controls silent` / `0 flags`.
- `sweep`: `box-vs-hline flags: 0; bridges found: 20; bridge orphans: 0;
  bridge widows: 0`.
- `print_web_text_equal: true`, 109,215 B; additionally verified in this proof:
  `cmp` my `pt-web.txt` == builder's `pt-web.txt` == builder's `pt-print.txt`
  == my `pt-print.txt` (all 109,215 B).

## 3. Canonical creambox (`creambox-all.log`, direct run) + core comparison

- es-pt: 26 boxes, 6 negatives (all below-box headings):
  P1 box y=1288 bottom=1677.2 → BELOW +37 `AHORA TÚ　Agora você` (inside-only +45.7);
  P1 box y=588 bottom=1308.0 → BELOW +44 `EN ESTA EDICIÓN　Nesta edição`
  (inside-only +8.0, desc-clear +2.3);
  P1 box y=1312 bottom=1652.0 → BELOW +24 `LA PALABRA DE LA SEMANA` (inside-only +16.0);
  P1 box y=1874 bottom=2194.0 → empty box, BELOW +24 caption line (image area);
  P2 box y=200 bottom=1245.7 → BELOW +37 `DECIR LA HORA` (inside-only +46.6);
  P3 box y=200 bottom=375.4 → BELOW +37 `LO QUE QUEDA DE NOVIEMBRE` (inside-only +47.7).
- core-es (`creambox-core.log`): same 6 negatives at the same boxes/headings
  (P1 cifras-box y=1258 vs es-pt 1288 — the C1 700→720 height change; P2/P3 boxes
  taller in es-pt because PT glosses wrap more). Design false positives, same as core.
- P3 `EL FLAMENCO, EN TRES DATOS` box: inside-only +5.3, desc-clear −1.2 in BOTH
  es-pt and core (frozen Spanish `música.`, no descenders) — see diag §4.

## 4. True-ink diag (`creambox-diag.log`) + boxtitle (`boxtitle.log`)

- Diag, all own-line ink clearances ≥ 0 (tightest): P1 CINCO CLAVES +3.8
  (`Nada inventado: tudo explicado aqui.`, ink bottom 1304.2 vs box 1308.0);
  P2 `ley.` +0.1; P2 ¿Y TÚ? +1.5; P3 `música.` +5.0; P3 ¿Y TÚ? +1.7;
  P4 ¿Y TÚ? +1.8; P5 VOTAR +0.1 (`compara precios antes de pagar.`,
  ink bottom 1251.4 vs box 1251.5); P5 ¿Y TÚ? +1.7; P7 CARTAS +1.5; P1 cifras +40.7.
- Boxtitle (27 titles): 0 overflows. `LA SEMANA EN CIFRAS　Números` right=932.9
  clear **+28.1** (D1 fixed). Tightest: P7 `LA PALABRA　A palavra da semana` +9.0;
  P7 `ERRORES TÍPICOS　Erros comuns` +20.1; P2 Nota +21.3; P1 `EN ESTA EDICIÓN` +23.7.
- P2 title ink (independent render → `visual/p2-vida.png`, 1:1 coords):
  rightmost title ink x=**901** (y=228–232); **0 ink pixels in gap 961..988**;
  cream edges at 961 / 989 confirmed by row scan → 88px clear of the Note box.
  Crop: `visual/crop-p2-calendario-title.png`.

## 5. P6 bar spans + P8 chips + D5 census (scripted checks)

- RTVE bars (y 1668–1792): widths 288.0 / 288.0 / 192.0 / 192.0 / 96.0 px for
  45/45/30/30/15 min → exactly **6.4 px/min**. Mini-bars: 32.0 / 96.0 / 6.4 px for
  5/15/1 → 6.4 px/min. Proportional, labels match.
- P8 `<rect>` fills: `#5c6e30` ×11, `#46581f` ×21, `#37402f` ×4 — the 4th `#37402f`
  rect is the P8 header band (x=88 y=72 w=1774 h=110); B2 chips are ×3, same as core.
- D5: es-pt Noto Sans CJK SC `<text>` = 634 (P1 71, P2 78, P3 82, P4 76, P5 80, P6 68,
  P7 74, P8 105; 398 bold + 236 regular) vs core 608; Newsreader 975 vs core 1200;
  Noto Serif CJK SC 43 vs core 310. Recorded only.
- Curly quotes: 0/0/0 in SVG `<text>` (core has 5/5/0); text.md curly 0, ASCII
  quotes 0, guillemets 56/56; text.md CJK = U+3000 ×98 only.
- `next Sunday`: case-insensitive search over core-es `*.py`, es-pt `*.py`,
  `tools/tables.py` → **0 occurrences**; brief's cited core lines
  (`content12.py:37/:113`, `content34.py:127`) do not contain it in the current files.

## 6. Web-PDF SHA nondeterminism — isolation log (all artifacts in `tmp/`)

Three `webpdf.py` runs → three SHAs/sizes (885,050 / 885,057 / 885,047 B).
Isolation:
- `subset_test.py`: fontTools subset of Unifraktur twice → identical SHA
  (`c2c30e54…`), size 31,296 → fontTools subsetting is deterministic.
- `cairo_test.py`: CairoSVG `svg2pdf` on p1 twice → same size 124,047 B, different
  SHA. Decompressed-stream diff: ONLY obj 47 differs, and only in
  `/CreationDate (D:20261111131037Z)` vs `(...1039Z)` — cairo stamps the current
  UTC second into every rendered page PDF; pypdf's merge strips the Info dict,
  which is why the print PDF is byte-stable.
- `web-a.pdf` vs `web-b.pdf` obj 19 (FontFile2, LucernaUnifrakturMaguntia-Regular):
  decompressed TTFs differ in exactly 3 bytes, all in `head`: `checkSumAdjustment`
  last byte (…fc vs …a8) and `head.modified` last byte. `head_times` check:
  source font modified 2026-11-07 → fontTools subset modified 2026-11-11T13:10:15
  (save time) → cairo-embedded font modified 2026-11-11T13:06:10 (that run's
  subset-save time). So fontTools rewrites `head.modified` to save time, and cairo
  copies it into the embedded re-subset → every `webpdf.py` run differs.
- Text layers unaffected: `cmp` my web txt == builder's web txt == builder's print txt.
- Current on-disk web PDF: 885,050 B, SHA `10610da1250af48d158a1410bc111e417a4cc6ce8c06428c76283fd38c19eefa`.

## 7. 150-item hand verification files

- `items-150.txt` (138 stems + keys, from current SVGs + my fresh `pt-p8-extract.json`
  + `keycheck-150.json`; extraction script `extract_items2.py` repointed from
  proof1's stale build-4 paths — the first run accidentally used proof1's old
  keys and was discarded). Missing from extraction: 12 matching items
  (25–28, 52–55, 141–144), verified separately: REG == P8-extracted == core ==
  text.md answers (25=c, 26=b, 27=d, 28=a; 52=c, 53=b, 54=a, 55=d;
  141=c, 142=d, 143=b, 144=a).
- `core-p8-extract.json`: core P8 keys; only #137/#138/#150 differ from PT keys.
- Golden sentences: SVG-direct check, 8/8 on article page + P7 (see PROOF-NOTE).
- MODELO: 97 words counted from `content8.py` source.
- `visual/`: independent CairoSVG renders p1–p8 (1950×2700) + `crop-p2-calendario-title.png`.

## 8. Files changed by this proof

- Production: only the gate-required re-render — `cards/*.png` + both PDFs rewritten
  from shipped SVGs; SVGs and sources untouched; print PDF byte-identical to brief;
  web PDF content-identical, new SHA (see §6). No commit, no push.
- Goals side: this scratch dir (`scratch-proof-es-pt2/`) + `probe-proof-es-pt2.txt`.
- `/dev/null` recreated with `touch` after it vanished mid-proof (see §0).
