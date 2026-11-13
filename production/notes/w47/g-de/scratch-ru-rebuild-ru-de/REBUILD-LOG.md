# REBUILD LOG — 2026-w47-ru-de (spacing rebuild, wave A)

- Edition: **2026-w47-ru-de** (Russian target, German explanations, VOL.4)
- Date: 2026-11-11 23:16–23:40 UTC
- Verdict: **BLOCKED BY SECOND FIX** (see §Census). Do not treat as clean.
- Method: `tools/run_build.py --build production/2026-w47/2026-w47-ru-de --out <this-dir>/build --steps run,render` (scratch copy; production untouched during build, integrity re-hash clean) + `tools/webpdf.py svg Lucerna-VOL4-ru-de-web.pdf` in production. No commit/push/lint.

## 0. Pre-conditions

- svglib.py md5 verified `781059e6784b789c1179446e15b8f6ad` in all 4 wave-A editions before any rebuild.
- Root cause of the original defect (re-proof F1, 131 boundaries): PIL measured Cyrillic with Regular faces while CairoSVG renders Medium faces (weight=100 → Medium), so rendered ink overran the space. Fix already applied in svglib.py `_PATH` entries for `("serif",False,"noto"/"noto_i")` and `("sans",False,"sans_noto"/"sans_noto_i")` → NotoSerif-Medium/MediumItalic, NotoSans-Medium/MediumItalic.

## 1. SHAs (old → new)

| File | Old SHA-256 | Old bytes | New SHA-256 | New bytes |
|---|---|---|---|---|
| `2026-w47-ru-de.text.md` | `d0f9b48c8fab4df8bb39acfdfebfbc6ad6cf0f09e75891449d13a0f1ce2dcc0f` | 63,471 | UNCHANGED | 63,471 |
| `Lucerna-VOL4-ru-de.pdf` (print) | `872b4f1c05d682f4f8a18749b7d63215a09bc2a151c3ca1601ef454de4019ebd` | 21,231,616 | `80024034da684b62db63a3671866f85fc4c913f56ebcb48ebca1603aa4cc31e3` | 21,230,193 |
| `Lucerna-VOL4-ru-de-web.pdf` (web) | `9aad0067943c7b8cac9263983409b6b5b3e452be249acd0094d675171d6c43b7` | 3,385,861 | `05b0a7abf59aa3617e5e75e94361460a692a144fb883017ba64bdf2198319992` | 3,384,428 |

- Print mtime 2026-11-11 23:26:52 UTC; web mtime 2026-11-11 23:27:28 UTC. Web PDF on disk at end of work is still the file built here (SHA re-verified after all gates; no concurrent rewrite observed).
- Footprint: exactly 18 files changed (8 `svg/*.svg` + 8 `cards/*.png` + print PDF + web PDF), verified by SHA snapshot diff vs before. KIT updated separately (§4 SHAs, §6 record).

## 2. Gates (all green except census)

- `run.py`: exit 0, TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE.
- `p8.py extract`: 150/150. `p8.py compare` vs core-ru: CLEAN, keydiff [137, 138, 139, 140].
- `check_core.py`: exit 0, golden BAD 0, gloss fails 0, 1 orphan line-start (P7 y553 `”».`, same benign class as KIT), same-baseline collisions 0 (the P1 y1712 collision from the KIT is gone).
- `occlusion_audit.py`: selftest OK; final run **0 flags** (was 42 TEXTX — the old Regular-vs-Medium false-positive class vanished).
- `freeze.py baseline`: re-baselined after the rebuild, 8/8 MATCH (direct SHA comparison); shipped SVGs unchanged by the run. (See §6 addendum for the later 0/8 self-report once the second-fix source landed.)
- Print/web text layers: byte-identical per page, 37,514 chars each (PyMuPDF `get_text`).
- Byline: "От редакции Lucerna" space char present P1–P6, ink gap 1.10 → **2.89 pt** (P4 2.82 pt; P4 byline "От спортивной редакции Lucerna").
- "Профессиональные праздники" spaced in text on P2/P6/P7; fused form gone.

## 3. Census (PyMuPDF char gaps, token-split + punctuation-junction method; `census.py` in this dir)

- BEFORE: 169 distinct tokens / 215 boundaries (print = web; fixed census, see §6).
- AFTER: 27 tokens / 30 boundaries (print = web). Proofer-style: 4 fused tokens. 154 before-tokens gone.
- All 131 re-proof Table-B word joins are GONE (checked: every Table-B token absent from the new PDFs; the 2 multi-joins `оттепельTauwetter;мокрыйснег` and `промокодRabattcode;возвратRückgabe.` split into spaced words except their `;` junctions — see below).

### 3a. REAL remaining joins — 15 boundaries (second defect class)

Newsreader (Latin) run renders wider than PIL measures it, so its trailing space overruns and the following Cyrillic word fuses. Gaps identical before/after the Medium fix. A dedicated fix worker is on this class.

| Token | Page | Gap (pt) | Before gap | Normal on line | Notes |
|---|---|---|---|---|---|
| `Imperativ:ne` → `Imperativ:не` | P8 | 0.55 | 0.54 | 2.37 | German "Verneinter Imperativ:" + Cyrillic `не`; visually fused (crop `crop-p8-imp.png`) |
| `13ноября` | P8 | 1.43 | 1.50 | ~2.5 | digit Newsreader run + `ноября`; pre-existing |
| `20ноября` | P4 | 2.18 | n/m | ~3.55 | pre-existing |
| `19ноября` | P2 | 2.11 | n/m (ink ~2.16) | 3.48 | newly exposed in TEXT LAYER only — ink gap unchanged before/after; old PDF carried a space char here, new one does not; NOT a visual regression (crop `crop-p2-date.png`) |
| `16ноября` | P5 | 2.24 | n/m | 3.66 | newly exposed, same as above |
| `A.на` | P4 | 1.68 | n/m | ~3.5 | option label "A." + `на`; pre-existing |
| `A.биография` | P3 | 2.20 | — (hidden in bigger token before) | 3.62–3.71 | option label + `биография` |
| `A.снег` | P7 | 2.28 | — | 3.69–3.78 | option label + `снег` |
| `A.цена` | P7 | 2.29 | — | 3.75 | option label + `цена` |
| `A.точно` | P7 | 2.29 | — | 3.44–3.75 | option label + `точно` |
| `Tauwetter;мокрый` | P7 | 1.86 | — (was inside `оттепельTauwetter;мокрыйснег`) | 3.14–3.44 | Latin gloss + `;` + `мокрый` |
| `Rabattcode;возврат` | P7 | 1.97 | — (was inside `промокодRabattcode;возвратRückgabe.`) | ~3.1–3.4 | Latin gloss + `;` + `возврат` |
| `результатов+` | P4 | 1.96 | −0.14 (overlap) | ~4.3 | trailing `+` junction; Medium fix improved it from overlap, still ~2.3 pt short |
| `—скидка` | P8 | 1.44 | 1.44 | 2.37 | dash run + `скидка`; unchanged |
| `—поздравляю` | P8 | 0.46 | 0.46 | 2.37 | key 140; unchanged |

Mechanism note (verified on the `19ноября` line): the digit run is a Newsreader element (`... A. 19 `, trailing space inside the element); PIL under-measures its trailing space (~2.8 SVG units allocated vs ~4.6 rendered), so the following Cyrillic word starts ~1.8 units early. The SVG allocation is identical old vs new (68.3 vs 68.2 units) — the Medium fix did not touch this class. The space CHAR's presence in the text layer is fragile (old web PDF had it for `19 ноября`, new does not); the ink gap never changed (~2.1 pt both).

### 3b. Cleared as false positives — 15 boundaries

Ink gap ≈ normal space for the size; only the space character is missing from the text layer.

- P1 level-map arrows `A2→B1` (2 bounds), `A2→B2` (1 bound): gap 0.0 — the arrow is a deliberate diagram connector; crop `crop-p1-levelmap.png` shows "A2→B1" / "A2→B2" reading as designed.
- P7 `→После` ×3, `→Родительный` ×1: gap **3.75 pt** = normal on the line (crop `crop-p7-afterarrow.png` shows "→ После" clearly spaced).
- P8 `→выходят` 2.33, `→рассказывает` 2.32, `→снял` 2.40, `→сыграли` 2.41, `→играет` 2.40, `→победило` 2.40, `→работаем` 2.40 pt (normal 2.15–2.38 at 9.8 pt).
- P8 `✓Mustertext` 2.33 pt (normal 2.37–2.38 on the same line).

## 4. KIT

- §4 SHAs/bytes + build line updated to this rebuild; §6 "Spacing rebuild" record added (blocked status stated). No other KIT content altered.

## 5. Artifacts in this dir

- `census.py` (the census tool), `line_gaps.py` (line-gap inspector), `census-print-before.json`, `census-web-before.json`, `census-print-after.json`, `census-web-after.json`, `snapshot-before.txt`, `build/` (run_build scratch: `build-copy`, `run-build.log`), `gates/` (p8, check_core, occlusion, freeze logs), `freeze-baseline/`, `crop-*.png` (200–300 dpi visual evidence).

## 6. Addendum (2026-11-12) — census-tool blind spot + second fix landed

**Census blind spot.** The first census run missed leading/trailing
punctuation junctions: `analyze_token` received the token after
stripping its punctuation, so `результатов+`, `—скидка` and
`—поздравляю` were invisible. Fixed in `census.py` (analyse the RAW
word; only skip outright when the raw word IS a vocab word with no
surrounding punctuation). All counts in this log and in the KIT §6 record
were corrected to the fixed census: before 169/215, after 27/30 (15 real
+ 15 FP boundaries). The earlier figures (131/171 → 24/27, 12 real) are
superseded. The before/after JSONs in this dir were regenerated with the
fixed tool (old web PDF as the before proxy).

**Second fix landed.** The dedicated fix worker landed the second
spacing fix in production `svglib.py` during the wave (md5
`ee3211298f274e02ade2d4ca318ce354` — "unkerned run measurement" in
`Page.text`, sums single-char advances to match Pango). This edition was
built with the FIRST fix only and needs a wave-B rebuild with it. The
freeze "8/8" in §2 was a direct SHA comparison made while the
first-fix source was current; a baseline re-run now self-reports 0/8
because the source changed (the build is deterministic given one svglib
— two independent re-runs of ru-fr are byte-identical to each other).

## 7. Addendum (2026-11-12) — second-fix worker's ruling confirms this log

The it-ru ruling (`hidden_files/w47/scratch-it-ru-spacing2/REBUILD-LOG.md`)
confirms every adjudication in §3: the DATE cases (`19ноября` 2.11,
`20ноября` 2.18, `16ноября` 2.24, `13ноября` 1.43 pt) are CONFIRMED
JOINS, narrow against the ~3.46 pt body / 2.36 pt P8 medians — this
edition was correctly NOT synced carrying them. The ARROW cases
(`→` + Cyrillic, 2.32–2.41 pt, at the normal median) are NOT joins —
extraction-only signal, already cleared as false positives in §3b.
`ГЛАГОЛЫИ` (2.62 pt, bold-caps bbox artifact) is not flagged anywhere
in this edition's censuses. No numbers in this log change.
