# Proofreader Verdict — Round 4 (RU P7 scope only: D6 fix verification)

**Issue:** Lucerna Weekly VOL.3, ZH-CN target, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time).
**Proofreader:** independent, did not build or fix this edition. No edition file was edited, no re-render was performed on the shipped files, no push/insert/Discord post was made, `~/workspace/weekly-git` was never touched, `index.json` was never touched. The fix worker's gate JSONs were NOT accepted; every gate below was re-run independently in this fresh directory. The fix worker's retained pre-fix evidence (`p7-ciyu-before.svg`, `textmd-before.md`, `kit-before.md`, `pre-fix-edition-hashes.txt`, `pre-fix-build-hashes.txt`) was used only as the comparison baseline — every number in this verdict is this round's own measurement from the final artifacts.
**Gate directory:** `hidden_files/w46/zh-cn-proofread-gates-round4/` (fresh; the fix worker's gate dir `hidden_files/w46/zh-cn-fix-round4/gates/` was never reused).
**Scope (per the Round 3 verdict §4.6):** exactly ONE edition, ONE page — `2026-w46-zh-cn-ru`, P7 only (`svg/p7-ciyu.svg` + `cards/p7-ciyu.png` + PDFs) — plus P8-untouched hash confirmation, the p8/freeze regression gates, and change isolation across the full 10-edition ZH-CN family. The other 9 editions were NOT re-proofread; they were hash-verified untouched only (see §7). No semantic re-verification beyond this scope was performed.

## Final verdict

**ROUND 4 PASS — D6 is fixed. The ZH-CN family is shippable 10/10.**

The RU P7 teaser band now clears the footer rule and the footer ink with clear margins, the footer is restored to paper at its intended contrast and is fully legible, exactly three SVG elements moved (band + 2 teaser lines, y −70.00 only), no text changed anywhere, P8 is byte-identical, and the change footprint is exactly the claimed RU P7 files plus the KIT record append. The 9 other editions remain Round 3 PASS, untouched. RU P7 is now shippable. No blocking defects remain in this scope (residual list: none — see §10).

## 1. Geometry — measured by this round from the final RU P7 SVG (Gate 1: PASS)

Independent SVG element parse (189 elements incl. root, document order; `analyze_r4.py` / `analyze-r4.log`, `geometry-contrast-r4.json`).

Final RU P7, elements [183]–[188]:

| Idx | Element | Final geometry | Pre-fix geometry |
|---|---|---|---|
| [183] | rect, fill `#2c2822` (teaser band) | x=65, **y=2448.52**, w=1820, h=118 → **bottom 2566.52** | y=2518.52, bottom 2636.52 |
| [184] | text, fill `#e8dfc8` (teaser title) | x=93, **y=2492.52**, offset **+44.0** from band top | y=2562.52, offset +44.0 |
| [185] | text, fill `#f3edda` (teaser sentence) | x=93, **y=2532.52**, offset **+84.0** from band top | y=2602.52, offset +84.0 |
| [186] | line (footer rule) | y1=y2=**2580**, stroke `#b3a06a`, width 1.6 | identical |
| [187] | text, fill `#57523f` (footer pairing line) | x=65, y=**2624**, font-size 20 | identical |
| [188] | text, fill `#57523f` (page number) | x=1885 anchor=end, y=**2624**, font-size 20 | identical |

Assertions, all verified:

- **Band bottom 2566.52 ≤ ~2570** ✓ (3.48 px inside the required bound).
- **Band bottom clears the footer rule:** 2580 − 2566.52 = **13.48 px** ✓.
- **Band bottom clears the footer ink top:** font-metric true-ink tops (FreeType `getbbox`, same Noto font files as the canonical audit) are **2605.00** ([187]) and **2609.00** ([188]); gaps to the band bottom are **38.48 px** and **42.48 px**. Rendered-pixel measurement of the card (1:1 with SVG coords, 1950×2700) gives band last row 2565, first footer-ink row 2606 (6 px, cap/diacritic fringe), substantial ink from 2609 — a **40–41 px** pixel gap. The fix report's "~2606.40 / 39.88 px" sits inside this measured range; the ~1 px spread between metric bounds and rendered ink is a measurement-method difference, not a defect. Either way the footer ink is ~38–42 px clear of the band.
- **Teaser lines moved WITH the band:** offsets +44.0 / +84.0 are unchanged vs the pre-fix SVG; both teaser ink boxes lie fully inside the band (title ink 2472.02–2498.02, sentence ink 2514.52–2536.77, band 2448.52–2566.52) ✓.
- **Footer rule / baselines / fills UNCHANGED vs pre-fix** ✓ (elements [186]–[188] identical in the full element diff below).
- **Full element-geometry diff pre-fix vs final:** exactly **3 elements differ** — indices [183], [184], [185] — each differing in **one attribute only, `y −70.00` exactly**, with tag, all other attributes and text strings identical. All other 186 elements (incl. root) are identical. No recolour, no footer move, no other element moved ✓.
- **Last phrase row clears the new band top:** the highest true-ink bottom above the band is **2425.69** (phrase rows at baseline 2421.19, idx [174]/[182]); clearance to the band top is **22.83 px** > 0, no overlap. (The fix report's 21.48 px uses a ~2427.04 ink-bottom estimate from an em-band bound; the 1.35 px spread is a metric-bound difference. The page is clear under either bound — not a defect.)
- **Source mechanism (corroborating, not relied on):** the RU build source carries `py = fy + 66 + 4 * 150 + 18 - 70` (content7.py:128, with a D6 comment), feeding only the band rect + 2 teaser texts; a scratch rebuild from the current source reproduces all 8 shipped RU SVGs **byte-identically** (see §9).

## 2. Contrast + occlusion-audit blindness (Gate 2: PASS; Gate 4: see §4)

WCAG contrast computed by this round from the actual SVG fills (`#57523f`, `#f7f1e2`, `#2c2822`):

| Pair | Contrast | Requirement |
|---|---|---|
| Footer `#57523f` on paper `#f7f1e2` (final state) | **6.94:1** | ≥ 4.5:1 ✓ |
| Footer `#57523f` on band `#2c2822` (pre-fix state) | 1.87:1 | (the defect) |
| Teaser title `#e8dfc8` on band | 11.03:1 | by design ✓ |
| Teaser sentence `#f3edda` on band | 12.51:1 | by design ✓ |

The footer ink is fully on paper, not on the band: SVG geometry puts all footer ink ~38+ px below the band bottom, and the rendered-pixel scan finds **zero** footer ink inside the band rows once teaser-glyph antialiasing is accounted for (see §3 pixel adjudication). **Blindness statement (explicit, as required):** a 0-flag occlusion audit alone does NOT pass this defect — the audit is blind to this class (footer painted after the band, footer-baseline exemption; it measures coverage, not foreground/background contrast). This verdict rests on geometry + contrast + visual evidence, not on the audit. The audit result is reported separately in §4 and is not treated as readability evidence.

## 3. Visual — full frame + band/footer crop, viewed by this round (Gate 3: PASS)

Viewed: the final RU P7 card at full frame (`files/weekly-report-w46-zh-cn-ru/cards/p7-ciyu.png`) and a band/footer-zone crop (y 2380–2700, native + 2×; `ru-p7-band-footer-crop.png`, `ru-p7-band-footer-crop-2x.png` in this gate dir).

What I see, quoted:

- **Crop:** above the band, the last phrase rows read `Три команды в четвертьфинале. (Страница 4)` (left) and `При пожаре не пользуйся лифтом. (Страница 3)` (right), clear of the band top. The dark band carries, in light type, the bold title `下期预告 · На следующей неделе (VOL.4)` and the sentence `S16总决赛打完了，谁是冠军？包裹都到了吗？还有你们的来信和第8版最佳作文。下周见！` — both fully inside the band, clean, no clipping. Below the band is clear cream paper, then the thin gold rule running the full width, then the footer in dark type on paper, fully legible: `Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ` on the left and `Страница 7 из 8` on the right. No dark-on-dark smudge, no rule striking the band, no overlap.
- **Full frame:** the whole P7 page is clean — header band, A2/B1/B2 columns, error clinic, construction box, reader corner, and the 8-phrase row section show no overflow, overlap, missing glyphs, or shift. The stem under `101.` reads `我拿了___包裹。` (the D5 fix, undisturbed — blank gap intact, single line, followed directly by ex. 102). The footer at the bottom of the page is crisp and readable at normal size, unlike the Round 3 pre-fix state.
- **Pixel adjudication (supporting the visual):** band rows at x=1000 span 2449–2565; the gap rows 2566–2605 are pure paper (row 2570 is 1821/1821 paper pixels); the gold rule renders antialiased as (192,176,129) on rows 2579–2580 across the full 1820 px width, 13–14 px below the band's last row (the SVG line itself is y=2580, stroke `#b3a06a` — the exact-fill pixel count is 0 only because the renderer antialiases the 1.6 px stroke; geometry, not the exact-fill count, is authoritative). Of 1,311 footer-colour-range pixels inside band rows, 1,308 fall inside the two teaser ink boxes (antialiased edges of the light teaser glyphs on the dark band) and 3 are 1-px antialias fringe at y=2471 just above the title ink box — **zero** footer ink on the band (`pixel-measurement-r4.json`, `pixel-adjudication-r4.log`).

## 4. Occlusion audit — fresh run, selftest fired (Gate 4: 0 flags, with the §2 caveat)

`tools/occlusion_audit.py` re-run by this round (`run_gates_r4.sh` / `run_gates_r4.out`, `occlusion-ru.json/.log`): selftest OK — planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent (exit 0, standalone run first, then the real run which re-runs the selftest internally and refuses to report on failure). Full RU edition: **0 flags, exit 0** (`flag_count: 0`, `flags: []`). Recorded as a gate result only; per §2 it does not by itself settle readability, and it is not relied on for the D6 verdict.

## 5. Freeze + P8 (Gate 5: PASS)

- **Freeze** (`tools/freeze.py diff --strict-cjk`, core `weekly-report-w46-zh-cn-core/svg` vs RU `svg`; `freeze-ru.json/.log`): **exit 0, TOTAL added CJK characters: 0** on every page (per-page core CJK totals 932/968/877/787/901/1019/739/1084 — P7 739, the Round 3 D5 figure, unchanged). The freeze JSON is page-for-page identical to the Round 3 `freeze-ru.json` (same added/removed string sets, same CJK totals) — the geometry-only fix changed no text set, as expected.
- **P8** (`tools/p8.py extract --total 150` + `compare` vs core; `p8-extract-ru.json/.log`, `p8-ru.json/.log`): extract **150/150**; compare **CLEAN, missing=[], extra_count=0, uncertain=[], keydiff=[]**, exit 0. No keydiff to adjudicate.

## 6. No content change (Gate 6: PASS)

- **SVG-text multiset diff** (pre-fix P7 SVG vs final P7 SVG): 163 text nodes both sides; before-only `[]`, after-only `[]` — **0 changed strings** ✓.
- **`.text.md` diff** vs the pre-fix copy (`textmd-before.md`): `diff` empty, `cmp` clean, **0 lines, byte-identical, 51,674 bytes**, SHA-256 `769f9e9ee27cfd99f9ab91105090d06c14cdfe4917f67701509cab261f191239` both sides (`textmd-diff-r4.txt`) ✓.
- **Stem/key/note-101:** final P7 SVG contains exactly **1×** the exact node `我拿了___包裹。`, **0×** the old stem `我拿了一个___包裹。`, 0× the doubled `我拿了一个个包裹`; `content7.py:19–20` carries key `个` with note `包裹 берёт счётное слово 个 gè.` and the new stem (unchanged); P8 note 101 extracted independently from the final P8 SVG is exactly `101. 个 — 包裹 берёт счётное слово 个 gè.` (single node) ✓. The PDF text layer likewise has the new stem 1× and the old stem 0× (see §8).

## 7. Change isolation (Gate 7: PASS)

**Full ZH-CN family hash diff** (all 210 edition files, current vs the fix worker's pre-fix snapshot `pre-fix-edition-hashes.txt`; `current-edition-hashes.txt`, `hash-diff-pre-vs-current.txt`): exactly **5 files changed, all RU** —

1. `weekly-report-w46-zh-cn-ru/svg/p7-ciyu.svg`
2. `weekly-report-w46-zh-cn-ru/cards/p7-ciyu.png`
3. `weekly-report-w46-zh-cn-ru/Lucerna-VOL3-RU.pdf` (print)
4. `weekly-report-w46-zh-cn-ru/Lucerna-VOL3-RU-web.pdf` (web)
5. `weekly-report-w46-zh-cn-ru/WEEKLY-KIT.md` (fix-record append only — see below)

All other RU files byte-identical (all P1–P6/P8 SVGs and cards, `.text.md`, `ABSTRACT.txt`); **all 9 other editions byte-identical** (189/189 other-edition files unchanged, 0 added, 0 missing). P1–P6 verified untouched by hash, P8 by hash (see §5/§8 scope note in the task: P1–P6 hash-verified, P8 hash-verified).

- **P8 untouched:** RU P8 SVG `cdf804c1c97bc62bc74e9f044a65c568909895df1f5cc94c4353a429e958a116` and card `21daa9b9a25cf9d0477c7e95fe10144031663db85c74b1b6cab7db54bddd4495` — identical to the Round 3 §2.1 hashes ✓.
- **KIT append:** diff vs `kit-before.md` is a pure append — 150 → 160 lines, **0 removed lines**, 10 added lines, single hunk `150a151,160` (the D6 fix record) (`kit-diff-r4.txt`) ✓.
- **Build diff:** RU build-dir hashes now equal the fix worker's post-fix snapshot exactly (`current-ru-build-hashes.txt` == `post-fix-build-hashes.txt`); pre→post build diff is exactly **one file, `content7.py`**, in the RU build dir only. The other 8 build dirs contain no D6 comment and no `- 70`; their teaser `py` lines are all the unshifted `py = fy + 66 + 4 * 150 + 18`, while RU's is `py = fy + 66 + 4 * 150 + 18 - 70` ✓.

## 8. PDF text layer (Gate 8: PASS, +1-byte claim adjudicated CONFIRMED)

Method: plain `pdftotext <pdf> <file>` (no `-layout`), matching Rounds 1–3 — an early `-layout` run in this round produced 100,501-byte extracts and was discarded as method-incomparable; all figures below are from the plain method.

- Web PDF: **2,275,749 bytes, 8 pages** (`pdfinfo-web-ru.txt`), ≤ 7 MB ✓. Print PDF: 30,430,934 bytes, 8 pages (`pdfinfo-print-ru.txt`) ✓.
- **Clarification on "web == print":** the PDF *files* are not byte-identical (web is the compressed build, print is 30.4 MB) — as in Rounds 1–3, byte-identity holds for the **pdftotext extracts**: web extract == print extract, `cmp` clean, **55,435 bytes each**, > 0 ✓.
- **+1-byte adjudication — CONFIRMED as claimed:** 55,435 vs the Round 3 figure 55,434 (+1). The unified diff vs the Round 3 web extract (`pdftotext-diff-r3-vs-r4.txt`) is a **single hunk, one insertion**: `1614a1615 > (blank line)` — exactly one added blank line between the teaser sentence and the footer line (R3 line 1614 `S16总决赛打完了，…下周见！` → R4 line 1615 blank → R4 line 1616 footer line). The character stream with newlines/formfeeds stripped is **identical (53,240 chars both)**, the non-blank line sequences are **identical (1,380 lines each)**, and there are **zero changed text lines**. (A naive line-by-line zip after the insertion shows every later line "differing" by one position — that is purely the shift artifact of the single insertion, not changed content.) The blank line is the expected `pdftotext` paragraph-break behaviour once the teaser/footer baseline gap grew from 21.48 px to 91.48 px. The character content remains −6 bytes vs Round 2 (the D5 two-character removal); the extracted-byte count is −5 only because of this separator newline. **No defect.**

## 9. Counts (Gate 9: PASS, from the final artifacts)

From a scratch rebuild of the *current* RU build source in this gate dir (OUT redirected to scratch, shipped RU files hash-guarded before/after — guard clean, `rebuild-guard-before/after.txt`; scratch copy deleted after comparison per Round 3 precedent, run log + comparison note retained as `rebuild-ru-run.log` / `rebuild-ru-compare-r4.txt`): **TOTAL 150; A2 56 / B1 69 / B2 25; per-page 10/18/18/18/18/18/12/38; writing model 164 characters; `P7 teaser ends 2566.52`; 0 FLOW OVERFLOW / HEAD TOO WIDE.** Independently, p8 extract gives 150/150 (§5) and the shipped `.text.md` is unchanged (§6). The scratch rebuild's 8 SVGs were **byte-identical to the shipped SVGs** (`cmp`, all 8; P7 element sequence 189/189 identical, text multiset diff empty) — proving the shipped P7 comes from the fixed source with no hand-edit.

## 10. Residual defect list

**None.** D6 is fixed (this verdict). D5 was CONFIRMED fixed in Round 3 and is undisturbed (§3/§6). No new defect was found in this RU-P7 + regression scope. The ~1 px spreads noted in §1 (footer ink-top bound, phrase-row clearance) and the antialiased gold-rule pixel colour in §3 are measurement-method reconciliations, explicitly adjudicated — they are not defects and require no action.

## 11. Gate artifacts saved in this directory

`proofreader-verdict-round4.md` (this file), `analyze_r4.py`, `analyze-r4.log`, `geometry-contrast-r4.json`, `pixel-measurement-r4.json`, `pixel-adjudication-r4.log`, `run_gates_r4.sh`, `run_gates_r4.out`, `occlusion-ru.json/.log`, `freeze-ru.json/.log`, `p8-extract-ru.json/.log`, `p8-ru.json/.log`, `current-edition-hashes.txt`, `hash-diff-pre-vs-current.txt`, `current-ru-build-hashes.txt`, `textmd-diff-r4.txt`, `kit-diff-r4.txt`, `pdftotext-web-ru.txt`, `pdftotext-print-ru.txt`, `pdftotext-diff-r3-vs-r4.txt`, `pdfinfo-web-ru.txt`, `pdfinfo-print-ru.txt`, `rebuild-ru-run.log`, `rebuild-ru-compare-r4.txt`, `rebuild-guard-before.txt`, `rebuild-guard-after.txt`, `ru-p7-band-footer-crop.png`, `ru-p7-band-footer-crop-2x.png`.

## Final verdict line

**ROUND 4 PASS (D6 fixed: RU P7 band bottom 2566.52 clears the footer rule by 13.48 px and the footer ink by ~38–42 px at 6.94:1 on paper, exactly 3 SVG elements moved y −70.00, no text changed, P8 untouched, change footprint RU-P7-only; the 9 other editions remain Round 3 PASS untouched and RU P7 is now shippable — ZH-CN family shippable 10/10).**
