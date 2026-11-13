# FIX-LOG — 2026-W47 de-zh-tw fix1 (D1 only)

- Edition: `2026-w47-de-zh-tw` (German target × Traditional-Chinese readers)
- Fixer: de-zh-tw toolbox fix1 builder (leaf). Date: 2026-11-11.
- Scratch: `hidden_files/w47/scratch-fix-de-zh-tw-toolbox/` (FIX-LOG.md + GATE-LOG.md + gate outputs + creambox-*.log + render/).
- Scope: ONLY D1 (P7 DER WERKZEUGKASTEN box too short). No other edition, no `tools/`, no commit, no push. Proof2 to be assigned separately by the coordinator.

## 0. Probes + SHA verification (pre-fix)

- Probe (task start, 2026-11-11 09:37 UTC): `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` OK; real test file written in the scratch dir. Re-probed OK before every write below. /tmp was 100% full — all intermediates went to the scratch dir with `TMPDIR=<scratch>/tmp`; nothing was written to /tmp and no one else's files were touched.
- SHA verify (2026-11-11 09:37 UTC) — all three MATCH the brief (= proof1, 5a2694d0):

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-zh-tw.pdf` | 23,048,423 | `7cb79dc34363d7cb5456c10a5c1f63b95604fe96b4d65c7c8c339a28df5ad6de` ✓ |
| `Die-Lucerna-VOL4-de-zh-tw-web.pdf` | 2,340,091 | `8bfc56bdad2b69de907d576650903b54292d33ab99f0551370f80327cc2b0da7` ✓ |
| `2026-w47-de-zh-tw.text.md` | 49,092 | `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9` ✓ |

## 1. Defect D1 (as found, reproduced)

- P7 col-3 rail, toolbox cream box `svg/p7-sprache.svg`: rect y=330 h=424 → bottom 754.0; last entry `Es ist fraglich, ob ... = 是否……尚未確定` baseline y=754.8 → clearance **−0.8**; the CJK ink sits on/below the box edge, on white newsprint below the box.
- Reproduced pre-fix with the proofer's `creambox.py` (copied from `scratch-fix-de-es1/`):

| Box | y | bottom | last baseline | clearance |
|---|---|---|---|---|
| DER WERKZEUGKASTEN (toolbox) | 330 | 754.0 | 754.8 | **−0.8** |
| LESERBRIEFE | 770 | 1294.5 | 1284.4 | +10.1 |
| NOCH EIN WORT | 1310 | 1460.5 | 1417.6 | +42.9 |

- (The creambox −35.0 rows on P7 are the matcher's known false positives: the A2/B1/B2 BEISPIELE boxes matched against exercise numbers sitting below them in the same column, inside the matcher's +45 window. Same pattern in all 10 editions incl. core; occlusion audit 0 flags + visual proofread confirm they are not defects. The P1 −37.0 / −24.0 rows are the same class — a following section head inside the matcher's window. Only the three col-3 rail boxes are read for this fix.)

## 2. Root cause + derivation (measured, edition-local)

`content7.py:76` (all 10 de fan-out editions carry the identical line, only the language comment differs):

```python
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 90
```

- The real ink advance per entry is `20.5 + n*29.11 + 6` (`Page.para`: first baseline at `y+20.5`, lines at `20.5*1.42 = 29.11`, returns last baseline + 29.11; caller adds 6). The formula counts only `n*29.5 + 6` — it **misses the +20.5 para offset on every entry** (6 entries = +123) and only partly compensates with the 29.5-vs-29.11 line-height overestimate (+0.39/line).
- This edition, verified numerically (`measure.py`, using the real `wrap` from `bslib4`): entries wrap to **[1, 1, 2, 2, 1, 1] lines, Σlines = 8**. Exact simulation of the para loop gives last baseline **754.77** (measured 754.8 ✓); box bottom = 330 + 62 + (8×29.5 + 36) + pad = 664 + pad. **Clearance = pad − 90.8** (for zh-tw, Σlines=8). Pad 90 → −0.8 ✓ matches measurement.
- Core-de uses pad **110** on the same formula (`core-de/content7.py:76`), giving +18.8 clearance (bottom 744.5, Σlines=7). The fan-out changed 110 → 90 with the comment "validated by en/fr occlusion 0 flags" — that validation was void: the occlusion audit only flags text covered by a *later-drawn* opaque element or crossed by a line; the toolbox text is drawn *after* its own box and nothing covers it, so the audit is blind to this defect class. The −0.8 was present in every fan-out build and invisible to all gates.
- The old line-76 comment ("90 validated by en/fr occlusion 0 flags") is therefore struck with the fix (see §3).
- NOCH EIN WORT headroom check (this edition, pre-fix): box ends **1460.5**, i.e. **87.5px** before the Sätze-der-Woche rule at y=1548. A +20 pad shift ends it at 1480.5 — 67.5px slack. Pad 110 is safe here with no redesign (unlike pt/nl/ru, whose NOCH EIN WORT ends at 1547.5).

## 3. Fix (edition-local only)

- File changed: `production/2026-w47/2026-w47-de-zh-tw/content7.py:76` ONLY (one line + comment). No shared helper touched (`bslib4.py`, `svglib.py`, `tools/*`, `transform.py`, `tr_zh-tw.py` all untouched).
- Change: pad `+ 90` → `+ 110` (restores the core-de value), comment rewritten with the arithmetic.
- Predicted geometry (from the formula above, verified after rebuild in §5/GATE-LOG):
  - toolbox: tbh 424 → 444, bottom 754.0 → **774.0**, clearance −0.8 → **+19.2** (same class as core +18.8; covers baseline + ~19 spare)
  - LESERBRIEFE: y 770 → **790** (16px gap from toolbox bottom preserved; its own +10.1 clearance unchanged, rh formula untouched)
  - NOCH EIN WORT: ends 1460.5 → **1480.5**, i.e. 67.5px before the Sätze rule at y=1548. Still compliant; no collision (verified visually + occlusion).
  - Nothing else on P7 moves: A2/B1/B2 flows, image, phrases (py=1560 fixed), clinic (ey=2020 fixed), teaser (ty=2400 fixed) all untouched. No text content changed — German/Traditional-Chinese strings, exercises, keys, Q34 stem all byte-identical by construction (one numeric literal + comment).
- Alternative considered and rejected: pad 105 (+14.2 clearance, NOCH EIN WORT ends 1475.5, 72.5px slack). 110 chosen because it exactly undoes the fan-out change that introduced the defect and matches the core's proven-good value; the 67.5px slack to the 1548 rule is a clear gap.

## 4. Rebuild (fix1, 2026-11-11 09:41–09:46 UTC)

- Command: `tools/venv/bin/python build_edition.py zh-tw` (from a copy of the fan-out driver in this scratch dir, with `tr_zh-tw.py`, `export_text_lang.py` and the `stub_svg`/`stub_bslib` stubs copied alongside; runs run.py → render.py → webpdf → verify → occlusion → p8 → freeze → pdftotext → chips → export; does NOT re-run transform, so the fix survives). Interpreter `tools/venv/bin/python` (PIL 13.0.0).
- Driver export hiccup (NOT a content problem): the driver's first export failed with `ModuleNotFoundError: stub_svg` — the scratch copy of `export_text_lang.py` was missing its stub modules (my copy omission). The export was re-run twice more: the first re-run used an empty gloss prefix (a shell-quoting failure on the Traditional-Chinese key) and wrote a 49,052 B text.md — that file was discarded. The second re-run, with the correct gloss prefix `註 — ` and NOTE_WRAP `full`, regenerated text.md **byte-identical** to rebuild-B (see §5). All other driver gates passed on the first run.
- Tool versions at build time: `tools/webpdf.py` clean in git (commit 40963281 "webpdf weight + italic face resolution", mtime 2026-11-11 09:10:13 UTC) — this web PDF now embeds the `LucernaNewsreader-Italic` subset (23,908 B; see web-PDF note in §5). `freeze.py` / `p8.py` / `occlusion_audit.py` carry working-tree modifications predating the rebuild wave (mtimes Nov 10 22:59 / 21:37 / Nov 11 05:01 — same versions as rebuild-B).
- Result: **ALL GATES PASS** (see GATE-LOG.md for per-gate output).
- New deliverables:

| File | Bytes | SHA-256 | vs rebuild-B |
|---|---|---|---|
| `Die-Lucerna-VOL4-de-zh-tw.pdf` | 23,048,426 | `74faeb9d898e254cd3f27a675063739701a9e40e387bde4b3622be5b7f240545` | +3 B (P7 geometry only) |
| `Die-Lucerna-VOL4-de-zh-tw-web.pdf` | 2,343,141 | `352ead22cee3fc77c56aa5d036015ba3e309679848cbf722a5e11d22ceb296b9` | +3,050 B (Italic subset, see below) |
| `2026-w47-de-zh-tw.text.md` | 49,092 | `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9` | **IDENTICAL** (zero content change) |

## 5. Post-fix verification (summary — detail in GATE-LOG.md)

- creambox.py full-edition: toolbox clearance **+19.2** (bottom 774.0, last baseline 754.8); LESERBRIEFE +10.1, NOCH EIN WORT +42.9 (both unchanged); NOCH EIN WORT ends **1480.5**, 67.5px before the 1548 Sätze rule. Diff of pre/post full-edition creambox logs = exactly the three col-3 rail rows (all other rows byte-identical, incl. the known false positives).
- P7 visual (100 dpi full page + 300 dpi toolbox zoom, print; web zoom pixel-identical, sha256 `f7960a4d…`): last entry fully inside the cream box (clear cream below the text), 16px gap to LESERBRIEFE, no collision, no excess whitespace.
- Full gates: occlusion (real run, no --selftest) **0 flags**; p8 extract 150/150 + compare **CLEAN** keydiff [137,138,139,150]; freeze diff RC=0 (TOTAL added CJK 1,328, the TC explanation layer); freeze_direct **8/8**, all page sha8 identical to rebuild-B (incl. P3 ad74f280 Q34, P7 9dc31873 — frozen text unchanged, only box geometry moved); keycheck **149/150** (Q150 truncation only); boxtitle **7/7**; chips 141; P8 min size **9.94pt**; print/web text-layer compare identical (default 49,905 B each; -raw normalised 48,777 B each); d2scan 67 pairs, 0 web gaps >0.5pt; bent quotes U+201C 66 / U+201D 0 / U+2019 0 (all paired); Q34 new stem 1× / old 0× in all five places; ABSTRACT 294 B, 0 ASCII quotes.
- Web PDF +3,050 B note: the rebuild-B web PDF embedded Regular + Bold Newsreader only; the fix1 web PDF (built with the committed 40963281 webpdf.py) additionally embeds the `LucernaNewsreader-Italic` subset (23,908 B in the log). The net +3,050 B is subset/compression variation from the current tool; the text layer is verified identical to print (49,905 B, word multiset identical), 8 pages, < 7 MB.

## 6. Files changed

- `production/2026-w47/2026-w47-de-zh-tw/content7.py` (1 line: pad 90 → 110 + comment).
- Rebuilt deliverables in the same edition dir (8 SVGs re-rendered; freeze_direct shas prove only P7 geometry differs — text identical on all 8 pages; 8 cards re-rendered; both PDFs; `2026-w47-de-zh-tw.text.md` rewritten, byte-identical sha; `__pycache__/content7.*.pyc`).
- `production/2026-w47/2026-w47-de-zh-tw/WEEKLY-KIT.md` (§2 fix1 deliverables + Status line + §7 fix1 entry + new §8; numbers only, no content change).
- Notes only: `hidden_files/w47/scratch-fix-de-zh-tw-toolbox/{FIX-LOG.md, GATE-LOG.md, creambox-*.log, measure.log, zh-tw/*, render/*, …}`.
- NOT touched: any other edition, `core-de/`, `tools/`, `issues/`, `covers/`, git index (no commit/push).
