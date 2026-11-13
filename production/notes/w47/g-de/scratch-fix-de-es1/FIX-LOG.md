# FIX-LOG — 2026-W47 de-es fix1 (D1 only)

- Edition: `2026-w47-de-es` (German target × Spanish readers)
- Fixer: de-es fix1 builder (leaf). Date: 2026-11-11.
- Scratch: `hidden_files/w47/scratch-fix-de-es1/` (FIX-LOG.md + GATE-LOG.md + gate outputs + creambox-*.log sweep).
- Scope: ONLY D1 (P7 DER WERKZEUGKASTEN box too short). No other edition, no `tools/`, no commit, no push. Proof2 to be assigned separately by the coordinator.

## 0. Probes + SHA verification (pre-fix)

- Probe (task start, 2026-11-11 09:24 UTC): `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` OK; real test file written + removed in `hidden_files/w47/`. Re-probed OK before every write below.
- Disk: 77G avail (`df -h`, 2026-11-11 ~09:25 UTC). No quota pressure.
- SHA verify (2026-11-11 09:25 UTC) — all three MATCH the brief:

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-es.pdf` | 10,968,803 | `7bc39e1f58b9bb447caf4f69b397eb39723ab2fef1c2bc4cf99d1be4a6e580ed` ✓ |
| `Die-Lucerna-VOL4-de-es-web.pdf` | 1,558,821 | `cd453143111bfad4f7f8a6ada98190f1790d2feccdaf3fd7c762a3a683043b90` ✓ |
| `2026-w47-de-es.text.md` | 50,124 | `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` ✓ |

## 1. Defect D1 (as found, reproduced)

- P7 col-3 rail, toolbox cream box `svg/p7-sprache.svg`: rect y=330 h=453.5 → bottom 783.5; last entry `Es ist fraglich, ob ... = aún dudoso` baseline y=783.9 → clearance **−0.4**; `fraglich` descender ink (~4.7) ends ~y=788.6, on white newsprint below the box.
- Reproduced pre-fix with the proofer's `creambox.py` (copied from `scratch-proof-de-es1/`):
  - toolbox: bottom 783.5, last baseline 783.9, clearance **−0.4**
  - LESERBRIEFE: y=800 bottom 1352.0, last baseline 1341.6, clearance +10.4
  - NOCH EIN WORT: y=1368 bottom 1518.0, last baseline 1475.1, clearance +42.9
- (The creambox −35.0 rows on P7 are the matcher's known false positives: the A2/B1/B2 BEISPIELE boxes matched against exercise numbers sitting below them in the same column, inside the matcher's +45 window. Same pattern in all 10 editions incl. core; occlusion audit 0 flags + visual proofread confirm they are not defects. Only the three col-3 rail boxes are read for this fix.)

## 2. Root cause (measured, edition-local)

`content7.py:76` (all 10 de fan-out editions carry the identical line, only the language comment differs):

```python
tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 90
```

- The real ink advance per entry is `20.5 + n*29.11 + 6` (`Page.para`: first baseline at `y+20.5`, lines at `20.5*1.42 = 29.11`, returns last baseline + 29.11; caller adds 6). The formula counts only `n*29.5 + 6` — it **misses the +20.5 para offset on every entry** (6 entries = +123) and only partly compensates with the 29.5-vs-29.11 line-height overestimate (+0.39/line).
- Exact: last baseline = 398 + 6×26.5 + 9×29.11 − 35.11 = 783.88 (measured 783.9 ✓); box bottom = 330 + 62 + (9×29.5+36) + pad = 723.5 + pad. **Clearance = pad − 90.4** (for es, Σlines=9). Pad 90 → −0.4 ✓ matches measurement.
- Core-de uses pad **110** on the same formula (`core-de/content7.py:76`), giving +18.8 clearance (bottom 744.5, Σlines=7). The fan-out changed 110 → 90 with the comment "validated by en/fr occlusion 0 flags" — that validation was void: the occlusion audit only flags text covered by a *later-drawn* opaque element or crossed by a line; the toolbox text is drawn *after* its own box and nothing covers it, so the audit is blind to this defect class. The −0.4 was present in every fan-out build and invisible to all gates.
- The old line-76 comment ("90 validated by en/fr occlusion 0 flags") is therefore struck with the fix (see §3).

## 3. Fix (edition-local only)

- File changed: `production/2026-w47/2026-w47-de-es/content7.py:76` ONLY (one line + comment). No shared helper touched (`bslib4.py`, `svglib.py`, `tools/*`, `transform.py`, `tr_es.py` all untouched — see §6 helper conclusion).
- Change: pad `+ 90` → `+ 110` (restores the core-de value), comment rewritten with the arithmetic.
- Predicted geometry (from the formula above, verified after rebuild in §5/GATE-LOG):
  - toolbox: tbh 453.5 → 473.5, bottom 783.5 → **803.5**, clearance −0.4 → **+19.6** (same class as core +18.8; covers baseline + descender + ~15 spare)
  - LESERBRIEFE: y 799.5 → **819.5** (16px gap from toolbox bottom preserved; its own +10.4 clearance unchanged, rh formula untouched)
  - NOCH EIN WORT: ends 1518.0 → **1538.0**, i.e. 10px before the Sätze-der-Woche rule at y=1548 (was 30px). Still compliant; no collision (verified visually + occlusion).
  - Nothing else on P7 moves: A2/B1/B2 flows, image, phrases (py=1560 fixed), clinic (ey=2020 fixed), teaser (ty=2400 fixed) all untouched. No text content changed — German/Spanish strings, exercises, keys, Q34 stem all byte-identical by construction (one numeric literal + comment).
- Alternative considered and rejected: pad 105 (+14.6 clearance, NOCH EIN WORT ends 1533, 15px slack). 110 chosen because it exactly undoes the fan-out change that introduced the defect and matches the core's proven-good value; the 10px slack to the 1548 rule is a clear gap (rule is a 2pt line, box ends 10px above it, audit-verified).

## 4. Rebuild (rebuild 5, 2026-11-11 09:27–09:30 UTC)

- Command: `tools/venv/bin/python build_edition.py es` (from `scratch-fanout-de/`; runs run.py → render.py → webpdf → verify → occlusion → p8 → freeze → pdftotext → chips → export; does NOT re-run transform, so the fix survives). Interpreter `tools/venv/bin/python` (PIL 13.0.0).
- Tool versions at build time: `tools/webpdf.py` carries uncommitted changes (90 ins / 17 del at 09:10 UTC, another agent's in-flight D2 patch — same state as the FANOUT-REPORT rebuild-B note; mtime verified UNCHANGED through the build); `freeze.py`/`p8.py`/`occlusion_audit.py` mtimes predate the rebuild wave. Recorded in GATE-LOG; web PDF therefore built with the current working-tree webpdf.py, as the coordinator directed a final-tool rebuild at pre-insert anyway.
- Result: **ALL GATES PASS** (see GATE-LOG.md for per-gate output).
- New deliverables:
  - Print PDF: `Die-Lucerna-VOL4-de-es.pdf` — 10,968,798 bytes (−5 B), sha256 `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e`
  - Web PDF: `Die-Lucerna-VOL4-de-es-web.pdf` — 1,601,888 bytes (+43,067 B — working-tree webpdf.py now embeds the `LucernaNewsreader-Bold` subset, 24,224 B; same effect as pt/ko/zh-tw in the FANOUT-REPORT; < 7 MB, text layer identical to print), sha256 `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e`
  - Text export: `2026-w47-de-es.text.md` — 50,124 bytes, sha256 `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` — **byte-identical to rebuild 4** (zero content change)

## 5. Post-fix verification (summary — detail in GATE-LOG.md)

- creambox.py full-edition: toolbox clearance **+19.6** (bottom 803.5, last baseline 783.9); LESERBRIEFE +10.4, NOCH EIN WORT +42.9 (both unchanged); NOCH EIN WORT ends **1538.0**, 10px before the 1548 Sätze rule. No negative clearances (other creambox rows are the matcher's known false positives, same as pre-fix — see GATE-LOG).
- P7 visual (100 dpi full page + 300 dpi toolbox zoom, print; web zoom pixel-identical): last entry fully inside the cream box (clear cream below the `fraglich` descender), 16px gap to LESERBRIEFE, no collision, no excess whitespace.
- Full gates: occlusion (real run, no --selftest) **0 flags**; p8 extract 150/150 + compare **CLEAN** keydiff [137,138,139,150]; freeze diff RC=0 (added CJK 7, all U+3000); freeze_direct **8/8**, source PASS, all 8 page shas identical to rebuild 4 (incl. P3 fc88f676 Q34, P7 b7aa0771); keycheck **149/150** (Q150 truncation only); boxtitle **7/7**; chips 141; P8 min size **9.94pt**; print/web text-layer compare identical (default 51,011 B each; -raw normalised 49,812 B each); d2scan 58 pairs, 0 web gaps >0.5pt; bent quotes U+201C 66 / U+201D 0 / U+2019 0 (all paired); Q34 new stem 1× / old 0× in all five places; MUSTER 84; ABSTRACT 426 B, 0 ASCII quotes.
- (GATE-LOG.md holds the per-gate outputs.)

## 6. Helper conclusion (for the coordinator — family-level rollout decision, NOT done here)

- The defect is in the **shared formula** (`content7.py:76` `tbh` computation, copied by transform into all 10 de fan-out editions from the core's line, with the pad changed 110 → 90 in the fan-out). The shared `Page.para`/helper code itself is correct — the formula in the *content file* under-counts the advance; no change to `bslib4.py`/`svglib.py`/`tools/` is needed or was made.
- Correct family-level fix (coordinator to decide/roll out; de-en fix1 is running in parallel under the same "edition-local only" rule): restore pad 110 in the shared source the transform copies (i.e. the `tbh` line as generated for each edition), or equivalently fix the formula to count the +20.5/entry para offset. Either way it is a one-line change per edition; the per-edition value needed varies only with Σlines and is already absorbed by pad 110 in every edition (worst case ja/ko/zh-tw Σlines=8 → clearance +19.2 at pad 110; pt/nl/ru Σlines=10 → +20.0).
- **Sweep of the other 9 de fan-out editions' P7 toolbox (creambox.py, read-only, pre-fix state — full logs in `creambox-<lang>.log`):**

| Edition | Σlines | Toolbox bottom | Last baseline | Clearance | Descender spill? |
|---|---|---|---|---|---|
| de-en | 9 | 783.5 | 783.9 | **−0.4** | yes (~4.7) |
| de-fr | 9 | 783.5 | 783.9 | **−0.4** | yes |
| de-es (this fix) | 9 | 783.5 | 783.9 | **−0.4** | yes |
| de-it | 9 | 783.5 | 783.9 | **−0.4** | yes |
| de-pt | 10 | 813.0 | 813.0 | +0.0 | yes — baseline exactly on the box edge, descender ~4.7 below |
| de-nl | 10 | 813.0 | 813.0 | +0.0 | yes (same) |
| de-ru | 10 | 813.0 | 813.0 | +0.0 | yes (same) |
| de-ja | 8 | 754.0 | 754.8 | **−0.8** | yes |
| de-ko | 8 | 754.0 | 754.8 | **−0.8** | yes |
| de-zh-tw | 8 | 754.0 | 754.8 | **−0.8** | yes |
| core-de (reference) | 7 | 744.5 | 725.7 | +18.8 | no |

- Conclusion for the coordinator: **all 9 siblings have the defect in ink terms** (7 negative, 3 at exactly 0.0 where the descender still spills). A family rollout of the pad-110 fix is warranted; per-edition clearance after pad 110 would be +19.2…+20.0 everywhere, with NOCH EIN WORT ending ≤1538 in all (their current ends: en/fr/es/it 1518.0, pt/nl/ru 1547.5*, ja/ko/zh-tw 1488.5 — *pt's 1547.5 is 0.5px before the 1548 rule, so a +20 shift there would cross it; pt/nl/ru need the pad fix PLUS a check of their col-3 stack — see note below).
- ⚠️ pt/nl/ru caveat: their NOCH EIN WORT currently ends at **1547.5** (FANOUT-REPORT rebuild-A note: "1547.5, 0.5px before the 1548 line") — a flat +20 pad shift would push it to 1567.5, past the Sätze rule. Those three editions cannot take the identical +20; they need either a smaller pad (+11…+15 still gives +11…+15 clearance and ends ≤1562.5 — still past 1548!) or a reflow that also shortens something below. Actually any positive Δ pushes their NOCH EIN WORT past 1548 unless the LESERBRIEFE rh or NOCH EIN WORT height is also trimmed. So pt/nl/ru need their own fix design (e.g. pad +11 plus trim the NOCH EIN WORT box or LESERBRIEFE bottom pad) — flagged here, NOT fixed here, for the coordinator + their fix1 builders.
- de-en note: the parallel de-en fix1 builder faces the identical geometry (−0.4, NOCH EIN WORT ends 1518.0, same 30px slack) — pad 110 works cleanly there, same as es.

## 7. Files changed

- `production/2026-w47/2026-w47-de-es/content7.py` (1 line: pad 90 → 110 + comment).
- Rebuilt deliverables in the same edition dir (SVG p7, both PDFs, text.md re-exported — content-identical except SVG P7 geometry; see GATE-LOG for new SHAs).
- `production/2026-w47/2026-w47-de-es/WEEKLY-KIT.md` (§5 rebuild-5 subsection + Status line; numbers only, no content change).
- Notes only: `hidden_files/w47/scratch-fix-de-es1/{FIX-LOG.md, GATE-LOG.md, creambox-*.log, …}`.
- NOT touched: any other edition, `core-de/`, `tools/`, `issues/`, `covers/`, git index (no commit/push).
