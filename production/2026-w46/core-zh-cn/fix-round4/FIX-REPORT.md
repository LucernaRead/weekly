# Fix report — W46 ZH-CN family, Round 3 defect D6 (RU P7 footer on the teaser band)

**Issue:** Lucerna Weekly VOL.3, ZH-CN target, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time).
**Scope:** ONE edition only — `2026-w46-zh-cn-ru` (Simplified-Chinese target, Russian reader-native),
folder `files/weekly-report-w46-zh-cn-ru/`. The other 9 ZH-CN editions are Round 3 PASS and were
not touched; no other family was touched.
**Trigger:** Round 3 proofreader verdict D6
(`hidden_files/w46/zh-cn-proofread-gates-round3/proofreader-verdict-round3.md`, §4/§4.6) —
the ONLY residual defect in Round 3 (D5 CONFIRMED fixed; P8-untouched 20/20 CONFIRMED; p8 CLEAN;
9 editions PASS). D6 is pre-existing: it predates the D5 fix (Round 3 geometry comparison pre/post
D5 showed 0 diffs) and is RU-only.
**Worker:** fix worker, 2026-11-03. Worked locally only: no push, no insert, no `index.json` edit,
no Discord post, no chat dump, `~/workspace/weekly-git` never touched. No rendered SVG/PDF was
hand-edited; the change went through the build source + full RU re-render, with `.text.md`
regenerated from the source manuscript.
**Status:** D6 fixed at the source, RU edition re-rendered and re-gated clean. An RU-P7-only
Round 4 independent proofread (per the Round 3 verdict §4.6) follows; this re-gating does not
replace it.

## 1. Defect D6 — RU P7 footer illegible (BLOCKING, RU only)

**Before (measured from the pre-fix RU P7 SVG, `svg/p7-ciyu.svg`, document order):**

```
[183] rect x=65 y=2518.52 w=1820 h=118 fill=#2c2822   — teaser band, y 2518.52–2636.52
[184] text x=93 y=2562.52 fill=#e8dfc8                 — 下期预告 · На следующей неделе (VOL.4)
[185] text x=93 y=2602.52 fill=#f3edda                 — S16总决赛打完了，谁是冠军？包裹都到了吗？还有你们的来信和第8版最佳作文。下周见！
[186] line y1=2580 stroke=#b3a06a                     — footer rule, painted after the band, crossing the band interior
[187] text x=65 y=2624 fill=#57523f                    — Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ
[188] text x=1885 y=2624 fill=#57523f anchor=end        — Страница 7 из 8
```

The footer baseline (2624) lay **12.52 px INSIDE the band** (band bottom 2636.52); the entire
footer ink band (~2606–2629) sat on the dark band. Contrast (WCAG, computed from the SVG fills):
footer `#57523f` on band `#2c2822` = **1.87:1**; the same footer on the paper `#f7f1e2` =
**6.94:1**; the teaser light texts on the band = 11.03:1 / 12.51:1. The footer was effectively
illegible at full frame. RU was the ONLY edition whose band bottom passed the footer baseline
(others: 2514.00–2554.48, NL closest at 2607.52 with footer ink clearing it — acceptable, not
raised). Other RU pages were clean (footer on paper; RU P8 legible). Cause (per the proofreader):
RU P7 content above the band runs ~122 px taller than the core, pushing the flow-placed band down
into the footer zone. The occlusion audit reported 0 flags — correct under its definitions
(footer painted after the band; footer-baseline exemption) but blind to dark-on-dark contrast.

## 2. Where the fix was applied

- **RU build dir only** — `hidden_files/weekly-report-w46-zh-cn-ru-build`: `content7.py`
  teaser `py` line only. Build-source hash diff vs the pre-fix snapshot: exactly this ONE file
  changed; no other `.py` file in the RU build dir changed, and no other build dir was touched.
- **The edit** (with a D6 comment in the source):

```
# D6 fix (Round 4, RU P7 only): move the teaser band + its two lines UP 70px
# so the band bottom (2566.52) clears the footer rule (y=2580) and the footer
# ink top (~2606), restoring the footer to paper. Footer unmoved, no text
# changed; every other P7 element keeps its geometry (band top was 2518.52).
py = fy + 66 + 4 * 150 + 18 - 70
```

  `py` feeds ONLY the band rect, the teaser title text, and the teaser sentence para
  (plus the `P7 teaser ends` print) — so by construction no other element can move.
  The 70 px shift was chosen against the measured headroom: the last phrase row's ink bottom
  is ~2427.04, leaving 91.48 px to the old band top; after the shift the gap is 21.48 px
  (clear, no overlap), while the band bottom (2566.52) clears the footer rule by 13.48 px
  and the footer ink top by 39.88 px, inside the family range.
- **NOT done, as specified:** the footer was NOT recoloured (fill `#57523f` unchanged);
  the footer was NOT moved (rule y=2580, baseline y=2624, unchanged); NO text was changed
  (no stem/key/note/clinic/glossline edit); no SVG-only patch was made.

**After (measured from the final RU P7 SVG):**

```
[183] rect x=65 y=2448.52 w=1820 h=118 fill=#2c2822   — band bottom 2566.52
[184] text x=93 y=2492.52 fill=#e8dfc8                 — title, offset +44.0 from band top (unchanged)
[185] text x=93 y=2532.52 fill=#f3edda                 — sentence, offset +84.0 from band top (unchanged)
[186] line y1=2580                                     — footer rule, 13.48 px below the band bottom, clear
[187]/[188] text y=2624 fill=#57523f                   — footer, fully on paper, ink top ~2606.40, 39.88 px below the band bottom
```

## 3. Re-render

RU edition only, from source with the family's own drivers (the same ones the Round 3 fix
worker used — `render_ru.sh` in this directory, the RU branch of `zh-cn-fix-round3/render_all.sh`
only, output path adapted): per edition `run.py` → `render.py` → `tools/webpdf.py` (web PDF
ONLY via `tools/webpdf.py`, per SOP 附则四) → `textmd.py`. Driver log: `P7 teaser ends 2566.52`,
TOTAL 150, levels A2 56 / B1 69 / B2 25, per-page 10/18/18/18/18/18/12/38, writing model 164,
**zero** FLOW OVERFLOW / HEAD TOO WIDE. Render logs: `render-ru-{run,render,webpdf,textmd}.log`.

`.text.md` regenerated from the source manuscript; diff vs the pre-fix copy
(`textmd-before.md`) is **0 lines — byte-identical** (51674 bytes, `cmp` clean, `diff` empty).
Headers preserved verbatim (the file is unchanged, so trivially so).

## 4. Verification — geometry, contrast, no content change

**Geometry (full P7 element comparison, pre-fix SVG vs final SVG, 189 elements incl. root /
188 excl. root — `geometry-diff.log`):** exactly **3 elements differ**, each `y −70.00` exactly
and nothing else: `[183]` rect `2518.52 → 2448.52` (x/w/h/fill identical), `[184]` text
`2562.52 → 2492.52` (all other attributes + string identical), `[185]` text `2602.52 → 2532.52`
(all other attributes + string identical). Every other element — all 186 remaining, including
the footer rule `[186]` and footer texts `[187]/[188]` — is identical. Teaser relative offsets
identical to pre-fix (title +44.0, sentence +84.0). Band fill `#2c2822` unchanged; footer fill
`#57523f` unchanged. Footer rule line (y=2580) clear of the band; footer ink top (~2606.40)
below the band bottom (2566.52); footer fully on paper.

**Contrast/readability:** footer contrast restored to **6.94:1** (paper background, computed from
the actual fills `#57523f` on `#f7f1e2`; pre-fix on-band value 1.87:1). Visual: RU P7 card at
full frame + band/footer zone crop (`ru-p7-band-footer-crop.png`, y 2400–2700) viewed — footer
fully legible on paper, gold rule clear of the band, band + both teaser lines clean, no overlap
with the footer rule or any other element, no overflow; the last phrase row clears the band top
by 21.48 px. At full frame the stem `我拿了___包裹。` reads cleanly under `101.` and the page
shows no other defect (scope note: this worker did not proofread beyond verifying this fix).

**No content change:** SVG-text multiset diff (pre-fix vs final P7) = **0 changed strings**
(163 text nodes both sides, before-only [] / after-only []). `.text.md` byte-identical
(§3). Stem in the final P7 SVG: exactly 1× `我拿了___包裹。`, old stem 0×. Key `个`
(`content7.py:19`) unchanged; P8 note 101 unchanged:
`101. 个 — 包裹 берёт счётное слово 个 gè.` Error clinic + A2 column untouched (no source
edit reaches them; multiset diff = 0 confirms it). P8 SVG + card byte-identical — re-confirmed
against the Round 3 hashes (§6).

## 5. Band geometry vs the other editions (post-fix, all 10 P7 editions)

Band bottom vs footer baseline (2624) / footer rule (2580) / footer ink top (~2606.40).
RU is now inside the family range; no other edition needs the fix.

| Edition | Band y | Band bottom | vs baseline | vs rule | vs ink top |
|---|---|---|---|---|---|
| en (core) | 2396.00 | 2514.00 | +110.00 | +66.00 | +92.40 |
| de | 2436.48 | 2554.48 | +69.52 | +25.52 | +51.92 |
| es | 2409.96 | 2527.96 | +96.04 | +52.04 | +78.44 |
| fr | 2396.00 | 2514.00 | +110.00 | +66.00 | +92.40 |
| it | 2396.00 | 2514.00 | +110.00 | +66.00 | +92.40 |
| ja | 2396.00 | 2514.00 | +110.00 | +66.00 | +92.40 |
| ko | 2396.00 | 2514.00 | +110.00 | +66.00 | +92.40 |
| nl | 2489.52 | 2607.52 | +16.48 | −27.52 | −1.12 |
| pt | 2405.98 | 2523.98 | +100.02 | +56.02 | +82.42 |
| **ru (fixed)** | **2448.52** | **2566.52** | **+57.48** | **+13.48** | **+39.88** |

(NL's −1.12 vs the nominal ink top uses the −0.88em ascender bound; NL was adjudicated
acceptable in Round 3 §4.5 — footer ink clears the band in the rendered crop — and was not
touched. Pre-fix RU bottom was 2636.52, −12.52 vs the baseline.)

## 6. Re-gate results (final artifacts, RU edition only)

Gate scripts: `run_gates_ru.sh` (RU-only adaptation of the Round 3 gate scripts).
Evidence: `gates/` (occlusion / freeze / p8 JSONs + logs, `occlusion-selftest.log`,
`pdftotext-web/print-ru.txt`, `gates-run.log`). Note on tool names: the task named
`tools/freeze_check.py`; no such file exists in `tools/` — the canonical freeze tool is
`tools/freeze.py` (SOP 附则二, used by Rounds 1–3), and that is what was run.

| Gate | Result (RU) |
|---|---|
| Occlusion audit (`occlusion_audit.py`, selftest OK: planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent) | **0 flags**, exit 0. Stated explicitly: the audit is blind to this contrast class (footer painted after the band; footer-baseline exemption) — this verdict rests on geometry + contrast + visual, NOT on the audit. |
| Freeze (`freeze.py diff --strict-cjk`, core vs RU) | Exit 0, TOTAL added CJK characters: 0 (per-page core CJK totals unchanged from Round 3, P7 739). |
| p8.py extract + compare | Extract 150/150; compare **CLEAN, missing=[], extra_count=0, keydiff=[]**, exit 0. |
| Counts (run.py registry stats) | 150; A2 56 / B1 69 / B2 25; per-page 10/18/18/18/18/18/12/38; writing model 164. |
| P8-untouched (hash re-confirmation) | RU P8 SVG `cdf804c1c97bc62bc74e9f044a65c568909895df1f5cc94c4353a429e958a116`, card `21daa9b9a25cf9d0477c7e95fe10144031663db85c74b1b6cab7db54bddd4495` — identical to the Round 3 §2.1 hashes. (All 10 editions' P8 hashes are unchanged per the §7 hash diff; the other 9 editions were not re-rendered.) |
| PDF text layer | Web == print byte-identical (55435 bytes each), 8 pages each, web PDF ≤ 7 MB (see §8). See the +1-byte note below. |
| Visual | P7 full frame + band/footer crop viewed (§4). |

**PDF text-layer +1-byte note (stated, not hidden):** `pdftotext` bytes are 55,435, i.e. +1 vs
the Round 3 figure 55,434. The diff vs the Round 3 web-PDF extract is exactly ONE added blank
line between the teaser sentence and the footer line: `pdftotext` inserts a paragraph break
once the teaser/footer baseline gap grows from 21.48 to 91.48 px. Non-blank lines are identical
and the character stream (newlines/formfeeds stripped) is identical — zero changed text lines.
The task's "−6 bytes vs Round 2 preserved" expectation therefore does NOT hold literally at the
byte level: the character content is −6 vs Round 2 (the 2 removed CJK characters from D5), but
the extracted-byte count is −5 because of this separator newline. Web == print still holds
exactly, and the text layer is non-empty on all 8 pages.

## 7. Change isolation

- **Hash diff** (210 edition files, pre-fix snapshot `pre-fix-edition-hashes.txt` vs post-fix,
  before KIT append): exactly **4 files changed, all RU** — `svg/p7-ciyu.svg`,
  `cards/p7-ciyu.png`, print PDF, web PDF. `.text.md` byte-identical (not changed). All other
  RU files byte-identical (all P1–P6/P8 SVGs and cards) and all 9 other editions byte-identical
  (189/189 other-edition files unchanged). After the KIT append: 5 files changed total (the
  same 4 + `WEEKLY-KIT.md`); no other file changed (`post-fix-edition-hashes-final.txt`).
- **Build diff:** exactly `content7.py` in the RU build dir (§2).
- **SVG-text multiset diff:** 0 changed strings (§4). **`.text.md` diff:** 0 lines (§3).
- **D5 fix undisturbed:** stem/key/P8 note 101 verified byte-identical to the Round 3 state
  (§4); the D5 record in the RU KIT is untouched (KIT append-only, 0 removed lines — verified
  by diff vs `kit-before.md`, 150 → 160 lines).

## 8. Final inventory (RU edition)

| File | Bytes |
|---|---:|
| `.text.md` (`2026-w46-zh-cn-ru.text.md`) | 51,674 (unchanged) |
| Web PDF (`Lucerna-VOL3-RU-web.pdf`) | 2,275,749 (≤ 7 MB, 8 pages) |
| Print PDF (`Lucerna-VOL3-RU.pdf`) | 30,430,934 (8 pages) |
| `pdftotext` bytes (web == print, byte-identical) | 55,435 (see §6 +1-byte note) |

## 9. Records

- Fix record appended to the RU KIT only (`WEEKLY-KIT.md` in the RU edition dir, as the
  third post-proof fix record following the D3/D4 and D5 records). Append-only: diff vs the
  pre-append copy (`kit-before.md`) shows 0 removed lines; earlier sections untouched. The new
  record states the before/after geometry + quotes, the gate summary, and this edition's
  inventory figures (which supersede the KIT's earlier PDF figures; the `.text.md` figure is
  unchanged).
- This report: `hidden_files/w46/zh-cn-fix-round4/FIX-REPORT.md`.
- Evidence under `hidden_files/w46/zh-cn-fix-round4/`: pre/post hash snapshots
  (`pre-fix-edition-hashes.txt`, `pre-fix-build-hashes.txt`, `post-fix-edition-hashes.txt`,
  `post-fix-build-hashes.txt`, `post-fix-edition-hashes-final.txt`), pre-fix P7 SVG +
  `.text.md` + KIT copies (`p7-ciyu-before.svg`, `textmd-before.md`, `kit-before.md`),
  render script + logs (`render_ru.sh`, `render-ru-{run,render,webpdf,textmd}.log`),
  gate script + JSONs/logs (`run_gates_ru.sh`, `gates/`, `gates-run.log`),
  geometry proof (`geometry-diff.log`, `band-geometry-all-editions.txt`, `contrast.txt`),
  visual crops (`ru-p7-band-footer-crop.png`, `ru-p7-band-footer-crop-2x.png`,
  `ru-p7-footer-strip.png`).

## 10. Unapplied work

**Nothing specified in the task could not be applied.** D6 is fixed in the RU edition only,
at the source, re-rendered, re-gated, and recorded as specified. Two deviations from the
task's literal wording are recorded, not hidden: (1) the task named `tools/freeze_check.py`,
which does not exist — the canonical `tools/freeze.py` was run instead (§6); (2) the
`pdftotext` byte count is 55,435, not the Round 3 figure 55,434 — exactly one added blank-line
separator from the widened teaser/footer gap, with identical text content (§6). No other
edition, family, stem, key, note, or footer was touched; no recolouring and no footer move
was performed.
