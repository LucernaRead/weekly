# DELTA-LOG — 2026-w47-nl-en: staging build 9 → canonical build 10 (core-nl fix3+fix4+fix5 sync)

- Edition: `production/2026-w47/2026-w47-nl-en/` (Dutch target, English reader), copied
  `cp -a` from staging `production/2026-w47/fanout-nl/2026-w47-nl-en/`; `diff -r`
  verified the copy byte-identical before any edit (only `cp` ownership warnings,
  harmless). Staging copy left untouched as the delta reference.
- Probes (pre-work): `git hash-object -w /dev/null` OK; probe file written in
  `hidden_files/w47/scratch-delta-nl-en/probe.txt`. TMPDIR = own scratch dir.
  Python = repo venv `tools/venv/bin/python`. No commit, no push.
- Pre-work SHA check (staging, build 9): print
  `3352492cf30e965d8249c55638f0ed73d4e07c0a4a97d61f4c9aa55c696a693c` / 12,665,902 B;
  web `2589cac4102d70f9041138f3c67a0176eff726a770cc89034ebd9c8905e39a06` / 1,610,568 B;
  text `05513522b585be936b4bd28654e911c278595afa9ec8a8713e1504ab364623dd` / 45,106 B —
  all three matched disk exactly before any edit.
- Source changes (3 files only): `bslib4.py` (w mechanism), `content8.py` (D9),
  `content34.py` (D11). `content7.py`, `content56.py`, `content12.py` unchanged
  (D6/D7/D8/D10 call sites: no defect pre-existed — see below).

## D6 — content34.py:78 P3 bridge (core fix3) — 预先不存在，无需改

- Core defect: Chinese `。` orphaned alone on its own line (bridge
  `用现在完成时补全，注意助动词 hebben/zijn。`, fix3 narrowed with `w=CW-40`).
- This edition: bridge is English —
  `Complete with the present perfect. Watch the auxiliaries hebben/zijn.`
  Build-9 SVG `p3-cultuur.svg`: 2 lines (`…Watch` / `the auxiliaries hebben/zijn.`),
  no orphan. The string contains **no CJK punctuation at all**, so a `。` orphan
  is impossible at any width.
- Width scan (`wrap()`, sans 20.5, 300–422.5px, 0.5px steps, 246 widths):
  **0 lone-punctuation widths**; line counts 2–3. No `w` applied at the call site.
- Structural sync only: `bslib4.py` `Flow.para`/`Flow.bridge` gained the optional
  `w` parameter (verbatim copy of core's mechanism, default `None` = column width,
  behaviour unchanged when not passed).

## D7 — content7.py:19 P7 A2 vocab bridge (core fix3) — 预先不存在，无需改

- Core defect: `。` alone on its own line (fix3 `w=CW-35`).
- This edition: bridge is English —
  `de wedstrijd match; de groepswinst group win; de kwartfinale quarter-final; scoren to score.`
  Build-9 SVG `p7-taal.svg`: 3 lines, last line `score.` — a word, not a
  punctuation orphan. No CJK punctuation in the string.
- Width scan (sans 20.5, 300–422.5px, 246 widths): **0 lone-punctuation widths**;
  line counts 3–4. No call-site change.

## D8 — content56.py:143 P6 chart caption `capcn` (core fix4) — 预先不存在，无需改

- Core defect: `。` pushed to the start of line 2 (fix4 `capcn_w = CW-25`).
- This edition: caption is English —
  `Practice data: made-up numbers, for practice only, not a real survey. Question: what do you put in your shoe? (100 young people)`
  Build-9 SVG `p6-verdieping.svg`: 4 lines at `CW-44=378.5`
  (`Practice data: made-up numbers, for` / `practice only, not a real survey. Question:`
  / `what do you put in your shoe? (100 young` / `people)`), no orphan.
  No CJK punctuation in the string.
- Width scan (sans 18.5, 300–422.5px, 246 widths): **0 lone-punctuation widths**;
  line counts 3–4. No `capcn_w` added (no defect to fix; the `w` mechanism now
  exists in `bslib4.py` if ever needed).

## D9 — Q140 key missing `kort` (core fix4) — 已修，三处同步

- Before: registry `content8.py:75` key `Ik maak een surprise met een gedicht.`;
  text.md:415 same; P8 node same. Stem (unchanged):
  `I am making a surprise with a little poem.` (already contains "little").
- After (all three): `Ik maak een surprise met een kort gedicht.`
  Only `kort ` added; note `surprise is a fixed expression` unchanged.
- text.md re-exported from source (`export_fanout.py . en`, rc=0): diff vs staging
  is **exactly 1 line** (line 415, `+5` bytes: 45,106 → 45,111 B).
- Three-way check (`p8compare_delta.py`, registry vs text.md vs P8):
  Q140 **MATCH** on all three sources; overall 149/149 MATCH, 0 DIFF, 0 MISSING
  (+ #150 open-writing exception, P8 key `✓`, text.md 81-word model text).
  Match keys re-verified: 25–28 = d/c/a/b, 141–144 = b/c/d/a.

## D10 — content7.py:91 P7 readers'-letters `dt_zh` (core fix4) — 预先不存在，无需改

- Core defect: `，` at the start of line 2 (fix4 `dt_zh_w = CW-32`).
- This edition: `dt_zh` is English — `No letters yet — an example; VOL.5 next.`
  Build-9 SVG `p7-taal.svg`: **1 line** (`y=1812.77`), no orphan.
  No CJK punctuation in the string.
- Width scan (sans 20, 300–422.5px, 246 widths): **0 lone-punctuation widths**;
  line counts 1–2. No `dt_zh_w` added.

## D11 — content34.py:130 P4 HET PROGRAMMA box last line spills below box (core fix5) — 已修

- Before (build-9 SVG, re-verified): box `x=1439.5 y=591.6 w=422.5 h=611.0`,
  bottom 1202.6; last line `18:45 uur.` baseline y=1209.49 → **−6.89px** below box.
  Same root cause as core: top reserve 62 vs real box-top → first baseline
  16 (pad) + 52 (title block) + 21 (para y-offset) = 89; 27px short.
- Independent re-derivation (`verify-d11.log`, real `wrap()`): facts wrap
  3/3/3/2/3 = 14 lines; simulated baselines 89.00 … 617.89 offset from box top,
  matching the SVG baselines **exactly** (first 680.60, last 1209.49).
- Fix: top reserve **62 → 89** (core's comment block copied), formula otherwise
  untouched; `sh` 611 → **638**; `P4 col3 ends` 1202.6 → **1229.6**;
  exercises hline y=1608, clearance 378.40px (unchanged).
- After (rebuilt SVG): last baseline 1209.49, baseline margin **+20.11px**.
  Dual true-ink verification (`inkprobe-d11-delta.log`):
  cards 1× lowest ink y=1209.00 → margin **+20.60px**;
  print-PDF 150dpi lowest ink y=1209.12 → margin **+20.48px**;
  7px strip below box bottom: **0 non-paper pixels on both renders**.
  150dpi crop `render/p-4.png` viewed: `18:45 uur.` inside the cream box with
  clear margin below.
- P3 same-shape box cross-check: bottom 1106.6, last baseline 1090.40,
  margin **+16.20px**, no spill (identical to core fix5's value).

## Gates (final build 10, all run in `scratch-delta-nl-en/`)

- `run.py` rc=0, **TOTAL 150** (by page 10/18/18/18/18/18/12/38; A2 46 / B1 73 /
  B2 31; model essay 81 words), **0** FLOW OVERFLOW / HEAD TOO WIDE.
- Scratch rebuild SVG: only `p4-sport.svg` and `p8-toets.svg` changed vs build 9;
  other 6 byte-identical (`svg-hashes-before.txt` vs `svg-hashes-after.txt`).
  p4 `37fef7bf…` → `e84dde44…`; p8 `cf3a415a…` → `32a6679b…`.
- Freeze: edition self repro **8/8** (`gates.py` freeze_sha256);
  core baseline **8/8** (`freeze.py baseline --build core-nl --core-svg core-nl/svg`,
  `freeze-core.log`; core p4 hash `6e05d5a0…` = fix5 state; core SVGs unchanged).
- `occlusion_audit.py svg/`: selftest OK, **0 flags**.
- `p8.py extract --total 150`: noted set **150/150**.
- `p8.py compare` vs core P8: **CLEAN**, keydiff **[137, 138]** (translation keys
  re-aimed into the reader language, by design).
- 150-question three-way (registry vs text.md vs P8): **149/149 MATCH** (+ #150
  exception). `p8-compare-delta.json`, `keytable-150.txt`.
- Print/web text layer (PyMuPDF position-sorted): **8/8 pages posdiff=0, msdiff=0**
  (tokens 790/828/738/735/807/748/915/2319); pdftotext print = web = **45,434 B**.
  Web PDF generated once via `tools/webpdf.py` (rc=0); never re-rendered.
- P8 answer font size: **min = median = 10.12pt** (spans 187) ≥ SOP §1.1 floor 9.75pt.
  Chips core = edition {A2:8, B1:24, B2:3}. §1.1 SVG audit: off-palette {}, no gold,
  stroked rects 0, VOL.5 = 5 (core 5), paper fills 8.
- Creambox: **2 CREAM-BOTTOM flags**, both pixel-probed **0 non-paper pixels** in
  the 7px strip below the box bottom → false positives (same adjudication as
  build 9): P2 `'Dutch and send them to the editors.'` (bottom 1446.2 vs rect
  1445.8, no descenders) and P5 `'them in.'` (bottom 1023.2 vs rect 1023.5).
  P4 now **0 flags**. True overflow 0.
- Spill sweep (`spill_sweep_delta.py`, re-proof script): **0 spills** on all 8
  pages. P4 box bottom 1229.6, no BELOW hit at all; nearest BELOW hits anywhere
  +24px (`HET WOORD VAN DE WEEK`, next section head), +32/+50.5/+60px independent
  blocks, adjudicated as in fix5b.
- Orphan sweep (`orphan_sweep_delta.py`, PIL + svglib + brute force):
  **1454 lines; (a)=0/(b)=0 both methods, all pages**; brute-force
  closer-leading fragments 0, leftmost 0.
- Box-title true-ink scan: 59 titles (38 `Flow.head` + 21 cream-box titles),
  PIL true ink (isolated render with the production Noto Sans CJK SC Bold font;
  the card-PNG band scan was contaminated by next-column glyphs starting exactly
  at the neighbouring COLX, e.g. phantom ink at x=537 for P8 head A — see
  `boxtitle-inkscan-delta.log`), **0 over-edge**. Tightest margins: P7 HET WOORD
  +10.5, P1 DE WEEK IN CIJFERS +11.5, P2 ZO ONTHOUD JE HET +14.5, P6 VOOR OF
  TEGEN? +17.5, P1 DRIE DINGEN head +25.5. Cross-check vs PNG-band margins to the
  box edge agrees within ~2.5px (P1 +11, P2 +17, P6 +20, P7 +12).
  **Count note:** the task named 56 titles; no definition tried reproduces 56
  (38 heads / 21 box titles / 30 OLIVE `p.text` titles / 59 combined). This gate
  scanned the full superset (59) with 0 over-edge; the 56-count discrepancy is
  flagged for the coordinator, not papered over.
- Visual: P4 + P8 renders viewed (`render/p-4.png` 150dpi, `render/p8check-8.png`
  100dpi): P4 box fixed as measured; P8 answer 140 shows `…met een kort gedicht.`,
  answers 1–150 complete. Observation (pre-existing, unchanged, out of scope):
  P4 masthead text element reads `SPORT　SPORT` — byte-identical in staging
  build 9 and in this build.

## New SHAs (build 10, lowercase)

- Print `De-Lucerna-VOL4-nl-en.pdf`:
  `29073788fa2fc7dfd426e6d209251f0919bdbf2cb33f79dbbc10eb15f92b2342` / **12,665,899 B**
  (old build 9: `3352492c…a693c` / 12,665,902 B)
- Web `De-Lucerna-VOL4-nl-en-web.pdf`:
  `6fd0ad3d700d686f9889faecd5e6076a6d9c309372f6871ad0faa4e41a253f98` / **1,610,560 B**
  (old build 9: `2589cac4…e39a06` / 1,610,568 B; < 7 MB)
- Text `2026-w47-nl-en.text.md`:
  `84ed9f3555e4995de8c4450ca9180019414ad907a63ed384ab632a8293612f91` / **45,111 B**
  (old build 9: `05513522…4623dd` / 45,106 B; diff vs staging exactly line 415)

## SVG change list vs build 9

- Changed: `p4-sport.svg` (D11, box height 611→638), `p8-toets.svg` (D9, key +kort).
- Unchanged (byte-identical): p1, p2, p3, p5, p6, p7.

## Files / logs

- Edition: `production/2026-w47/2026-w47-nl-en/` (WEEKLY-KIT.md §9 updated).
- Scratch: `hidden_files/w47/scratch-delta-nl-en/` — `probe.txt`, `width-scan-pre.log`,
  `verify-d11.log`, `build-delta.log`, `render-delta.log`, `export-delta.log`,
  `webpdf-delta.log`, `occlusion-delta.log`, `gates-delta.log`, `p8-compare-delta.log`,
  `p8-extract-delta.log`, `p8-extract.json`, `p8compare_delta.py`,
  `p8compare-delta.log`, `p8-compare-delta.json`, `keytable-150.txt`,
  `reg-dump.json`, `freeze-core.log`, `freeze-core/` (core repro),
  `creambox-delta.log`, `orphan-sweep-delta.log`, `spill-sweep-delta.log`,
  `check_creambox_delta.py`, `orphan_sweep_delta.py`, `spill_sweep_delta.py`,
  `inkprobe-d11-delta.py`, `inkprobe-d11-delta.log`, `boxtitle_inkscan_delta.py`,
  `boxtitle-inkscan-delta.log`, `boxtitle_inkscan2_delta.py`,
  `boxtitle-inkscan2-delta.log`, `svg-hashes-before.txt`, `svg-hashes-after.txt`,
  `svg-hashes-postcompare.txt`, `pdftoppm-delta.log`, `render/` (p-4.png 150dpi,
  p8check-8.png 100dpi), this DELTA-LOG.md.
- Staging `fanout-nl/2026-w47-nl-en/` untouched (SHAs re-verified after the build).
- No commit, no push.
