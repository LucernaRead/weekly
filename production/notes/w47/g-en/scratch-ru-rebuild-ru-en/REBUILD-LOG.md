# REBUILD LOG — 2026-w47-ru-en (spacing rebuild, wave A)

- Edition: **2026-w47-ru-en** (Russian target, English explanations, VOL.4)
- Date: 2026-11-11 23:44–23:52 UTC
- Verdict: **BLOCKED BY SECOND FIX** (see §Census). Do not treat as clean.
- Method: `tools/run_build.py --build production/2026-w47/2026-w47-ru-en --out <this-dir>/build --steps run,render` (scratch copy; production untouched during build, integrity re-hash clean) + `tools/webpdf.py svg Lucerna-VOL4-ru-en-web.pdf` in production. No commit/push/lint. Same root cause, fix and method as ru-de (see `../scratch-ru-rebuild-ru-de/REBUILD-LOG.md` for the mechanism analysis).

## 1. SHAs (old → new)

| File | Old SHA-256 | Old bytes | New SHA-256 | New bytes |
|---|---|---|---|---|
| `2026-w47-ru-en.text.md` | `5dba645578989ed58673b060b6c67e6df844335f82a1ba351012f66e5c9404df` | 62,786 | UNCHANGED | 62,786 |
| `Lucerna-VOL4-ru-en.pdf` (print) | `d12fa6a6bb62dd7af36743c7d2f33d96d27def054e5dcd6fdb288ef3577c06a1` | 21,251,270 | `1fcc6aa4101b07a89f17cab7d52a974c3acdfdc49712a96f043f66909d468831` | 21,249,828 |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | `0778f40076d6579b6699c9508e886186a2c86500e0216c38c6168d4e270127f4` | 3,380,920 | `7e67d0069ad0bb8ee4d1951a4ebc9cdc30d416a635241468bb0fce0df877b09f` | 3,379,458 |

- Print mtime 2026-11-11 23:48:02 UTC; web mtime 2026-11-11 23:49:25 UTC. Web PDF on disk at end of work is still the file built here (SHA re-verified after all gates; no concurrent rewrite observed).
- Footprint: exactly 19 files changed (8 `svg/*.svg` + 8 `cards/*.png` + print PDF + web PDF + WEEKLY-KIT.md), verified by SHA snapshot diff vs before.

## 2. Gates (all green except census)

- `run.py`: exit 0, TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE.
- `p8.py extract`: 150/150. `p8.py compare` vs core-ru: CLEAN, keydiff [137, 138, 139, 140].
- `check_core.py`: exit 0, golden BAD 0, gloss fails 0, 1 orphan line-start (P7 y553 `”».`, same benign class), same-baseline collisions 0 (P1 y1712 collision gone).
- `occlusion_audit.py`: selftest OK; final run **0 flags**.
- `freeze.py baseline`: re-baselined after the rebuild, 8/8 MATCH (direct SHA comparison); shipped SVGs unchanged by the run. (See §6 addendum for the later 0/8 self-report once the second-fix source landed.)
- Print/web text layers: byte-identical per page, 37,102 chars each (PyMuPDF `get_text`).
- Byline: "От редакции Lucerna" space char present P1–P6, ink gap **2.89 pt** (P4 2.82 pt).
- "Профессиональные праздники" spaced (P2/P6/P7); fused form gone.

## 3. Census (same `../scratch-ru-rebuild-ru-de/census.py` method)

- BEFORE: 171 distinct tokens / 214 boundaries (print = web; fixed census, see §6).
- AFTER: 29 tokens / 32 boundaries (print = web). 154/171 before-tokens gone.

### 3a. REAL remaining joins — 17 boundaries (second defect class)

Newsreader Latin run renders wider than PIL measures; trailing space overruns; following Cyrillic fuses. Gaps identical before/after the Medium fix.

| Token | Page | Gap (pt) | Before gap | Notes |
|---|---|---|---|---|
| `Note:играть` | P8 | **−1.21** | −1.21 | key 139 "Note: играть + с + instrumental"; glyphs OVERLAP |
| `imperative:не` | P8 | 0.92 | 0.84 | "Negative imperative:не спешите" |
| `row:пять` | P8 | 0.54 | 0.46 | gloss "row:пять" |
| `13ноября` | P8 | 1.43 | 1.50 | digit run + `ноября` |
| `20ноября` | P4 | 2.18 | n/m | pre-existing |
| `19ноября` | P2 | 2.11 | ABSENT before | newly exposed in text layer (ink gap unchanged, same as ru-de) |
| `16ноября` | P5 | 2.24 | ABSENT before | newly exposed, same as above |
| `A.на` | P4 | 1.68 | n/m | option label + `на` |
| `A.биография` | P3 | 2.20 | ABSENT before | option label + `биография` |
| `A.снег` | P7 | 2.28 | ABSENT before | option label + `снег` |
| `A.цена` | P7 | 2.29 | ABSENT before | option label + `цена` |
| `A.точно` | P7 | 2.29 | ABSENT before | option label + `точно` |
| `to;может` | P7 | 2.26 | ABSENT before | English gloss "to" + `;` + `может` |
| `результатов+` | P4 | 1.89 | −0.14 (overlap) | trailing `+` junction; improved, still ~2.4 pt short of normal |
| `·середина` | P6 | 1.91 | 1.89–1.94 | middle-dot separator + `середина`; unchanged |
| `—скидка` | P8 | 1.44 | 1.44 | dash run + `скидка`; unchanged |
| `—поздравляю` | P8 | **−0.21** | −0.21 | key 140; glyphs overlap |

### 3b. Cleared as false positives — 15 boundaries

Ink gap ≈ normal space for the size; only the space character is missing from the text layer (same classes as ru-de, verified there by measurement + crops).

- P1 level-map arrows `A2→B1` (2 bounds), `A2→B2` (gap 0.0 — deliberate diagram connector).
- P7 `→После` ×3, `→Родительный` (gap 3.75 pt = normal, measured on ru-de).
- P8 `→выходят/рассказывает/снял/сыграли/играет/победило/работаем` (2.32–2.41 pt vs normal 2.15–2.38 at 9.8 pt).
- P8 `✓See` (2.33 vs 2.37).

## 4. KIT

- §5 SHAs/bytes + build line + web text bytes updated to this rebuild; §7 "Spacing rebuild" record added (blocked status stated). No other KIT content altered.

## 5. Artifacts in this dir

- `census-print-before.json`, `census-web-before.json`, `census-print-after.json`, `census-web-after.json`, `snapshot-before.txt`, `build/` (`build-copy`, `run-build.log`), `gates/` (p8, check_core, occlusion, freeze logs), `freeze-baseline/`.

## 6. Addendum (2026-11-12) — census-tool blind spot + second fix landed

**Census blind spot.** The first census run missed leading/trailing
punctuation junctions: `analyze_token` received the token after
stripping its punctuation, so `результатов+`, `·середина`, `—скидка`
and `—поздравляю` were invisible. Fixed in
`../scratch-ru-rebuild-ru-de/census.py` (analyse the RAW word; only skip
outright when the raw word IS a vocab word with no surrounding
punctuation). All counts in this log and in the KIT §7 record were
corrected to the fixed census: before 171/214, after 29/32 (17 real +
15 FP boundaries). The earlier figures (133/169 → 25/28, 13 real) are
superseded. The before/after JSONs in this dir were regenerated with the
fixed tool (old web PDF as the before proxy). Date/letter gaps measured
for this edition (identical to ru-de): `19ноября` 2.11, `20ноября` 2.18,
`16ноября` 2.24, `A.на` 1.68 pt.

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
