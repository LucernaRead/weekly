# FIX LOG — 2026-W47 ru-en, Fix 1 (build after round-1 proofread)

- Edition: `2026-w47-ru-en` (Russian target × English reader), VOL.4, issue 16–22 November 2026
- Fixer: fix1 builder (leaf); 2026-11-11
- Work dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`
- Notes: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-en1/`
- Read first: `SOP.md` (full), `~/workspace/weekly-git/AGENTS.md`, coordinator brief
  (`hidden_files/w47/briefs/brief-coordinator.md`), round-1 `PROOF-NOTE.md` + `GATE-LOG.md`
  (used as reference only; every defect re-verified on disk before fixing)
- Scope: proof1 defects D1 + D2 only. Observations O1–O10 untouched. No changes to
  core-ru, other families, `tools/` (D2 patch is a proposal in §3 below, never written
  to `tools/`), `issues/`; no `insert.py`, no `lint --write`, no git writes of any kind.
- Startup probes passed: `git hash-object -w` probe + real write probe file
  (`PROBE.txt`, 2026-11-11 07:59 UTC). No disk-quota error at any point.

## 0. Pre-fix identity (matches round-1 proof note exactly)

- Print `Lucerna-VOL4-ru-en.pdf`: 21,245,420 B, SHA-256
  `023d9fd12bdca276751400fb13f7f399d645c267a09ba1897eb0e598d52f2e3a`, 8 pages
- Web `Lucerna-VOL4-ru-en-web.pdf`: 3,341,934 B, SHA-256
  `fab0fc44736ecb169a1cc3932a8e85db2504f694f02e84d45f3063435327493d`, 8 pages
- Pre-fix SVG SHA-256s saved in `exp/svg-before.sha256`.

## 1. D1 — FIXED (P5 band subtitle curly double quotes render full-width)

**Verification before fixing (defect confirmed real on disk):**
- P5 band subtitle is a single span in the print PDF:
  `“Black Friday”: sales from 16 November`, 13.5 pt, `NotoSansCJKsc-Regular`,
  x0=1111.8, x1=1374.6.
- PIL measurement on the actual font file (`NotoSansCJK-Regular.ttc`, SC face, 18 px):
  `“` advance 18.00 px = 13.50 pt, `”` 13.50 pt — exactly 1 em; straight `"` 8.53 px =
  6.40 pt; word space 3.02 pt; widest Latin letter `m` 12.50 pt. Confirms the
  proofer's numbers.
- Source: `content56.py:12` (`p.band(...)` subtitle). `run.py` reads only
  `content*.py` — `scratch-fanout-ru/map-en.json:109` is the fan-out record the
  string came from (W46 TM value; Chinese source used full-width `“黑色星期五”`,
  correct in Chinese; the English translation kept the curly quotes), not an
  input to the build. The live generating source is `content56.py`.
- Full-edition source grep for U+201C/U+201D: only `content56.py:12` (D1) and
  `content7.py:70` (P7 `“чёрной пятнице”`, Newsreader — must stay). `check_core.py:94`
  only holds `”` inside a `CLOSES` punctuation set, not visible text.

**Change (one line, one file):**
- File: `production/2026-w47/2026-w47-ru-en/content56.py`, line 12:
  - Before: `...　“Black Friday”: sales from 16 November")`
  - After: `...　\"Black Friday\": sales from 16 November")  # fix1 D1: straight quotes — U+201C/U+201D render full-width (1em) in Noto Sans CJK SC; P7 “чёрной пятнице” (Newsreader) untouched`
  - (Escaped straight quotes inside the double-quoted Python literal; the evaluated
    string value is `"Black Friday"`. The `.text.md` re-export confirms the value
    comes out as plain `"Black Friday"` — zero backslashes, byte-verified.)
- `map-en.json:109` was NOT edited: it is a scratch record outside the allowed work
  area, and the edition's live source is `content56.py`. The TM value still carries
  the curly quotes — it must be fixed at the fan-out layer before any re-fanout of
  this edition. Flagged to the coordinator (not fixed here by design).

**Rebuild + verification:**
- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150 (A2 50 / B1 76 /
  B2 24; by page 10/18/18/18/18/18/12/38; model words 97). `sha256sum` diff vs
  pre-fix: **only `svg/p5-molodezh.svg` changed** (old `5b66992d…`, new
  `ae19aec96bc1d5ba0caf1cb083ce6ca8bafbe6dca1198ceb8107f4e2c83adb1f`).
- `render.py` + `tools/webpdf.py` re-run (exit 0, web text bytes 57,196).
- New print PDF: **21,245,374 B**, SHA-256
  `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e`, 8 pages.
- New web PDF: **3,341,905 B** (< 7 MB), SHA-256
  `0c7ebd6ad6f808623228a39b56508d46df2e74fbe16eb89392e325c5aaced46e`, 8 pages.
- P5 subtitle in BOTH new PDFs: `"Black Friday": sales from 16 November`, 13.5 pt,
  identical span boxes (x0=1126.0, x1=1374.5). 4× zoom crop (`exp/p5-band-crop.png`,
  rendered from the new print PDF) shows the closing straight quote tight on `:`.
- `.text.md` re-exported with the documented command (`ru_textmd.py . … "VOL.4 ·
  Russian text · English explanations"`): 56,600 B (was 56,604), 150 exercises,
  203 blocks; `diff` vs pre-fix copy shows exactly one line changed (line 264,
  the P5 band subtitle).
- **U+201C/U+201D rescan (visible `<text>` in all 8 SVGs): 0 everywhere EXCEPT P7
  (1 pair: `“` + `”».` — the intended Newsreader pair, explicitly not moved).**
  U+2019: **0** everywhere. CJK in visible text: only U+3000 full-width-space
  separators (121, the §1.1 furniture separators), no CJK ideographs.
  - Note on the brief's wording ("after the fix, U+201C/U+201D in reader-visible
    SVG text should be 0"): that cannot hold literally together with "P7 stays" —
    the P7 pair is visible SVG text. The accurate statement is: 0 in CJK-font
    contexts (the defect class), 1 retained pair in Newsreader (correct rendering).

## 2. D2 — NOT FIXABLE IN-EDITION; root cause proven, tool patch proposed (§3)

**Reproduction on the shipped PDFs (proofer's numbers confirmed independently):**
- P1 headline 39.8 pt: `14-` print x1=133.0 vs web x1=128.6 → **4.4 pt gap**;
  next span `й тур` x0=133.0 both. P4 heading 24 pt: 106.5 vs 103.8 → **2.6 pt**.
  P1 contents `1. 14-` 15 pt: gap 2.2 pt. P4 band subtitle
  ` все восемь результатов`|`+` 13.5 pt: print x1=1008.7, web x1=1006.7, `+` at
  1008.6 → 1.9 pt. P1 contents `3. «` 15 pt: 1.1 pt. P5 title `«` 24 pt: 0.9 pt.
  P7 `«` 16.12 pt ×2: 0.6 pt each.
- Line-based abutting-span scan on shipped PDFs (proofer's method): 7 spots
  > 0.5 pt (my own scan implementation finds 4 of them — the P1 headline pair has
  different bbox y0 and the two P1-contents / one P4-subtitle pairs fall out of
  my line-key matcher; all 7 were verified individually by direct span lookup).

**Root cause (proven by measurement, not guessed):**
- The print render (CairoSVG → Pango → fontconfig) and the web render
  (`tools/webpdf.py` → fontTools subset → CairoSVG under an isolated fontconfig)
  resolve the SAME family/weight request to DIFFERENT font faces:
  - **Bold Newsreader (weight 700):** print uses **Newsreader-SemiBold**; web uses
    **Newsreader-Regular**. Proof: PIL SemiBold−Regular advance for `14-` at 53 px
    = 5.80 px = 4.35 pt vs the measured 4.4 pt headline gap; at 32 px = 2.62 pt vs
    2.6 pt measured; `«` at 32 px = 0.91 pt vs 0.9 measured; `«` at 21.5 px =
    0.61 pt vs 0.6 measured. `pdffonts`: shipped web PDF embeds only
    `LucernaNewsreader-Regular` — no bold Newsreader subset exists.
  - **Regular Noto Sans / Noto Serif:** print uses **Medium**; web uses **Regular**.
    Proof: P4 band subtitle ` все восемь результатов` (18 px, Noto Sans): PIL
    Regular 161.06 pt, Medium 164.58 pt; print span 162.7 pt, web span 160.7 pt
    (both ≈ PIL + Pango's ~+1 pt layout offset; the 2.0 pt print−web difference
    is the face difference). `pdffonts` on print shows `NotoSans-Medium` /
    `NotoSerif-Medium` for these spans.
- Why the faces differ — `FC_DEBUG=1` on a CairoSVG render shows CairoSVG's match
  pattern requests **`weight: 100`** for SVG text with no `font-weight` and
  **`weight: 200`** for `font-weight="700"` (fontconfig's 0–210 scale). But
  `tools/webpdf.py` `fc_match` queries `':style=Bold'` for bold and a bare family
  for regular:
  - `fc-match 'Newsreader:style=Bold'` → Newsreader-Regular.ttf (same file as
    regular) → the bold subset is skipped (`if bold and match == fc_match(fam,
    bold=False): continue`) → no `LucernaNewsreader-Bold` ever exists → the
    isolated fontconfig serves Regular for all weight-700 Newsreader text.
  - `fc-match 'Noto Sans'` (bare) → Regular, while the print pipeline's
    weight-100 request → Medium.
  - Numeric-weight queries behave exactly as the print pipeline:
    `:weight=200` → Newsreader-SemiBold / NotoSerif-Bold / NotoSans-Bold;
    `:weight=100` → NotoSans-Medium / NotoSerif-Medium / Newsreader-Regular /
    NotoSansCJKSC-Regular / NotoSerifCJKSC-Regular (CJK faces have no Medium
    TTC installed, so Regular is correctly returned).

**In-edition candidates tried and REJECTED (each with evidence):**
1. **Rename bold Newsreader runs to family `Newsreader SemiBold`** (in edition-local
   `svglib.py`): probe render (`exp/probe.svg` → `probe-print.pdf` /
   `probe-web.pdf`) shows BOTH pipelines fail to resolve that family name and fall
   back to Noto Sans Bold — `14-` at 53 px renders 58.3 pt wide in a sans face,
   worse than the defect. Dead end.
2. **Rename `Noto Sans` → `Noto Sans Regular`**: probe shows print resolves it to
   Medium anyway (162.1 pt both spellings) — no-op. Dead end.
3. **Merge the abutting runs into one `<text>`**: only relocates the deficit to the
   next run boundary (the merged run is still 4.4 pt narrower in web); the gap
   would open after `й тур` instead of after `14-`. Dead end (except at line end,
   which does not apply here).
4. **Whole-line single `<text>` with `<tspan>`s** (rewrite `Page.text` emission):
   would touch every text element in all 8 SVGs; print glyph positions would move
   from PIL-computed to Pango-computed (probe shows Pango widths exceed PIL by
   ~1 pt on Noto Sans lines) — perturbing the currently-correct print PDF; and
   web bold text would STILL render in the wrong weight (Regular instead of
   SemiBold), which is a real visual difference beyond the 7 gaps. Rejected as
   invasive and root-cause-blind.
5. **Content rewording** (avoid `14-й` at bold boundaries): the pattern is correct
   Russian that must appear (headlines, contents, headings, band subtitle); the
   font boundary is inherent to the per-glyph fallback architecture
   (`svglib.py` `_char_font`: digits/hyphen → Newsreader, Cyrillic → Noto Serif).
   Rejected.
6. **Measure bold Newsreader with Regular in PIL** (make layout match web): would
   make the PRINT PDF wrong (it renders SemiBold; text would overflow measured
   boxes). Rejected.
- Conclusion: **no in-edition fix exists that fixes D2 without relocating it or
  invasively rewriting the shared emission architecture / breaking correct print
  output. The fix belongs in `tools/webpdf.py`.** Per the brief, `tools/` was NOT
  modified; the verified minimal patch is in §3.
- D2 status in the SHIPPED (new) web PDF: **unchanged** — same 7 spots, same sizes
  (re-measured after the D1 rebuild: P1 headline 4.33 pt, P4 heading 2.62 pt, P1
  contents-1 2.20 pt, P4 band-sub 1.94 pt, P1 contents-3 1.17 pt, P5 title
  0.91 pt, P7 0.58 pt ×2). The D1 change does not touch any D2 span. The web PDF
  still needs a rebuild with the patched tool once the coordinator approves it.

## 3. D2 patch proposal for `tools/webpdf.py` (NOT applied — coordinator decision)

**Minimal diff (one line in `fc_match`, plus comment):**
```diff
 def fc_match(family, bold=False):
     """Resolve a family to (file, index) via fontconfig, or None."""
-    query = family + (':style=Bold' if bold else '')
+    # CairoSVG requests weight=100 for SVG text with no font-weight and
+    # weight=200 for font-weight=700 (proven by FC_DEBUG on a CairoSVG
+    # render); ':style=Bold' resolves Newsreader-Bold to the Regular file
+    # and bare 'Noto Sans' to Regular while print uses Medium.
+    query = family + (':weight=200' if bold else ':weight=100')
```
- The existing skip rule (`if bold and match == fc_match(fam, bold=False): continue`)
  still works: with numeric weights the bold and regular queries now return
  different files wherever a real bold face exists, so the bold subset is built.
- One cosmetic note from the experiment: fontTools prints `fsSelection bit 5 (bold)
  and head table macStyle bit 0 (bold) should match` when saving the SemiBold-derived
  subset renamed as Bold — the subset still embeds and renders correctly (verified
  by span measurement); the warning is about the source file's flag bits, not a
  failure.

**Verification of the patch (run on a COPY at `exp/webpdf-weight2.py`, never on
`tools/`; inputs = the new fix1 SVGs; outputs in `exp/`):**
- `LucernaNewsreader-Bold` subset is now built (20,468 B); `LucernaNotoSans-Regular`
  / `LucernaNotoSerif-Regular` subsets are now built from the Medium files (the
  subset file names are unchanged — only the source face changes).
- All 7 D2 spots (shipped → patched): P1 headline 4.33 → **0.00**; P4 heading
  2.62 → **0.00**; P1 contents-1 2.20 → **−0.31** (invisible 0.3 pt overlap);
  P4 band-sub 1.94 → **−0.14**; P1 contents-3 1.17 → **−0.29**; P5 title 0.91 →
  **0.00**; P7 0.58 → **0.00**.
- Full abutting-span scan (1,704 pairs) on the patched web PDF: **0 gaps > 0.5 pt**;
  worst gap overall 0.05 pt. No new gaps introduced anywhere.
- Text layer: patched web PDF text multiset == print multiset; `pdftotext` 57,148
  bytes (> 0). Size 3,367,618 B vs shipped web 3,341,905 B (+25,713 B, +0.77%).
- An earlier variant (regular `:weight=80`, bold `:weight=200`) fixed 6/7 spots
  but left the P4 band-sub at 1.94 pt — that is what pinned the regular query to
  `:weight=100` (matching CairoSVG's actual request). Both experiment PDFs are in
  `exp/` (`web-weight.pdf` = v1, `web-weight2.pdf` = v2).

**Cross-edition check (same patch copy, core-ru SVGs — read-only input, output in
`exp/`; core-ru itself untouched):**
- Shipped core-ru web PDF: 4 gaps > 0.5 pt, worst 2.62 pt (P4 `14-`) — the same
  defect class. Patched web PDF: **0 gaps > 0.5 pt**, worst 0.05 pt; text multiset
  still == print; size 3,992,881 → 4,018,430 B (+0.64%).

**Impact assessment (for the coordinator):**
- What changes: only the face-resolution step of `build_subsets`. Per family:
  Newsreader regular → Regular (unchanged), bold → SemiBold (was Regular);
  Noto Serif regular → Medium (was Regular), bold → Bold (unchanged); Noto Sans
  regular → Medium (was Regular), bold → Bold (unchanged); Noto Sans/Serif CJK SC
  regular → Regular TTC (unchanged), bold → Bold TTC (unchanged); UnifrakturMaguntia
  / DejaVu Sans → unchanged (single-weight families; the skip rule still applies).
- Effect on all editions: every web PDF rebuilt with the patched tool will render
  text in the SAME faces as its print PDF (correct weights, matching advances) —
  print/web consistency improves everywhere; the web PDFs grow ~0.6–0.8%.
- Risk: low. The patch touches one function, no image handling, no subsetting logic,
  no verification logic. The only behavioral change is which source file is subset
  for three (family, weight) pairs, each verified above to be the face the print
  pipeline already uses. Recommended rollout: apply the patch, rebuild the affected
  web PDFs (ru-en fix1 + any other editions whose shipped web PDFs carry the same
  gaps — at minimum the ru family), re-run the abutting-gap scan per edition.
  `tools/` itself is untouched by this fix; applying the patch is the coordinator's
  call.

## 4. Files changed (edition dir only)

| File | Change |
|---|---|
| `content56.py:12` | D1: curly → straight quotes in P5 band subtitle (+ comment) |
| `svg/p5-molodezh.svg` | Regenerated by `run.py` (only SVG that changed) |
| `cards/*.png` | Regenerated by `render.py` (reproducible cache) |
| `Lucerna-VOL4-ru-en.pdf` | Re-rendered (new SHA, §1) |
| `Lucerna-VOL4-ru-en-web.pdf` | Rebuilt with unpatched `tools/webpdf.py` (new SHA, §1; D2 still present) |
| `2026-w47-ru-en.text.md` | Re-exported (56,600 B; 1 line changed) |
| `WEEKLY-KIT.md` | §5 outputs (new SHAs/bytes) + §7 fix1 record |
| `__pycache__/` | Regenerated bytecode (untracked build artifact) |

- `tools/` untouched by this fix (verified: the `M` flags on `tools/freeze.py`,
  `tools/occlusion_audit.py`, `tools/p8.py` pre-date this session — mtimes
  2026-11-10 22:59 UTC, 2026-11-11 05:01 UTC, 2026-11-10 21:37 UTC vs session
  start 2026-11-11 07:59 UTC — other lines' work; `tools/webpdf.py` itself is
  unmodified, mtime 2026-11-06). The D2 experiment used copies in `exp/` only.
- No git operations performed (no commit, no push, no stash, no reset).
- `EDITION-RECORD.md` does not exist in the edition dir or anywhere nearby
  (searched `production/2026-w47/2026-w47-ru-en/` and `hidden_files/w47/`); the
  KIT (`WEEKLY-KIT.md`) is the edition record and was updated instead.
- Unrelated external change noted during this fix (no action): the system
  file-watcher flagged an edit to `~/MEMORY.md` (cover-motion note trimmed:
  secondary-motion 113/144 summary shortened). Same class as round-1 O10; not
  part of this task.

## 5. Handoff to round-2 proofread

- D1 is fixed and verified (code + both PDFs + crop + rescans).
- D2 is **still present in the shipped web PDF** (worst 4.4 pt, P1 headline) pending
  the coordinator's decision on the §3 tool patch. If the patch is approved, the
  web PDF must be rebuilt with the patched tool and re-scanned before round 2
  signs off D2; the print PDF needs no rebuild for D2 (it is already correct).
- Round 2 should re-verify: the P5 subtitle quotes, the full mechanical gates
  (GATE-LOG.md), and — if the tool patch lands — the 7 D2 spots in the rebuilt
  web PDF.


---

# FIX LOG — 2026-W47 ru-en, Fix 2 (proof1 S1)

- Edition: `2026-w47-ru-en` (Russian target × English readers), Lucerna Weekly VOL.4, issue 16–22 Nov 2026.
- Fixer: fix1. Date: 2026-11-11. Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-en1/` (same dir as the Fix 1 log above; this section is appended, the Fix 1 record above is untouched).
- Defect: proof1 (b) S1 — P1 stats-box title overhangs its cream box. Source `content12.py:48`.
- Scope kept: only this edition's title source (+ the fan-out map value that generates it) and KIT doc fixes below. No other edition, no core, no commit, no push. Re-proofread follows; this log is not a sign-off.

## 0. Pre-fix identity (verified by me before any edit — all MATCH the brief)

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,190 | `b244c56b7575f425e52902f19823f740d46cdafea2afcb1b86cdde24df863406` |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,786 | `d306b3f365c5b4a04022f2a900faee904eb3f838c2f530fe5b4ce667c62d14a9` |
| `2026-w47-ru-en.text.md` | 62,829 | `1e06ec55e8ba694224e244e37d81e6bfdfc3c3299e6aeb925308fd08e0b0e2ea` |

Startup probe: `echo test | git hash-object -w --stdin` in the repo → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc=0 (run inside `~/workspace/weekly-git`; a bare call outside the repo fails with "not a git repository", which is not a probe failure). `/dev/null` present as a char device, no touch needed. TMPDIR = this scratch dir. Interpreter: repo `tools/venv/bin/python`.

Pre-fix independent re-measurement (my own run of proof's `spill.py`, copied to this scratch as `spill.py` → `gates/spill-prefix.log`): exactly 1 ink-escape among 32 cream boxes — P1 `　The round in numbers`, ink right **998.9** vs box right 961.0 (+37.9); 0 bad box titles; 43 spill-below candidates (all in the already-classified by-design set). Title run in `svg/p1-pervaya.svg`: `　The round in numbers`, x=726.6, baseline y=1240.735, Noto Sans CJK SC 23pt bold; cream rect x=538.5, w=422.5 → right edge 961.0.

## 1. The fix (option (a) — shorten the English subtitle)

Russian head `ТУР В ЦИФРАХ` is core text, untouched. Only the English subtitle literal changed.

**`content12.py:48` (now :52, with a fix comment at :48–51)**
- Before: `f.box("ТУР В ЦИФРАХ　The round in numbers", [`
- After: `f.box("ТУР В ЦИФРАХ　The round", [`

**Fan-out map — the literal IS table-generated, so both were changed.**
`hidden_files/w47/scratch-fanout-ru/map-en.json`, key `/lit/ТУР В ЦИФРАХ　数字看本轮` (the core Chinese literal):
- Before: `'ТУР В ЦИФРАХ　The round in numbers'`
- After: `'ТУР В ЦИФРАХ　The round'`
- Verified: exactly 1 occurrence of the long form in the map before the edit, 0 after; file still valid JSON; rendering literal == map value, so a re-fanout reproduces the short title. Changing the map alone would have been an empty fix; changing the source alone would have let a re-fanout revive the long form.

No other title, no other text, no core file touched. `content34/56/7/8.py` untouched; `core-ru/` read-only (see §7).

## 2. Rebuild (KIT §5 commands, whole edition)

| Step | Result |
|---|---|
| `run.py` | rc=0, TOTAL **150** (A2 50 / B1 76 / B2 24; by page 10/18/18/18/18/18/12/38; model words 97), **0** FLOW OVERFLOW / HEAD TOO WIDE (`gates/run.log`) |
| `render.py` | print PDF 21,251,086 bytes (`gates/render.log`) |
| `tools/webpdf.py svg Lucerna-VOL4-ru-en-web.pdf` | web PDF 3,380,694 bytes, 57,318 text bytes (`gates/webpdf.log`) |
| `ru_textmd.py . 2026-w47-ru-en.text.md "VOL.4 · Russian text · English explanations"` | 62,818 bytes, 150 exercises, 277 blocks (`gates/textmd.log`) |

**Post-fix identity (new SHAs — the deliverable; web PDF is the fresh rebuild, not the old file):**

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,086 | `9a159cd59f32443eb8d612eb05959ff7af3273d4c3796da0b2b2f6a7f1800b0a` |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,694 | `7e465d67a96c3e47aa415cc530160de2df9f9b2d9f923e85366da28b8e263ed5` |
| `2026-w47-ru-en.text.md` | 62,818 | `5960b7a649a8b50036fefa0b16580a2209bc694ea45fb5377a9ee39d9c1296ee` |

Print −104 B, web −92 B, text.md −11 B (exactly ` in numbers`, 11 chars) vs pre-fix.

**Rebuild scope — only P1 changed.** SVG SHA comparison vs proof's pre-fix rerun copy (`scratch-proof-ru-en2/rerun/svg/`): p1 DIFF, p2–p8 all byte-identical. `diff` of the `p1-pervaya.svg` element stream old→new: exactly 1 line (the title run). `diff` of `.text.md` old→new: exactly 1 line pair (L25 `### ТУР В ЦИФРАХ · The round in numbers` → `### ТУР В ЦИФРАХ · The round`). "The round in numbers": 0 occurrences in the new text.md, `content12.py`, and `svg/p1-pervaya.svg`.

## 3. S1 re-measurement (my own, post-fix — not copied from proof1)

`gates/d3-p1-title2.log` (PIL `occlusion_audit.ink_box`, same fonts as the canonical audit), title runs on baseline y=1240.735:

| Run | Ink box (l, t, r, b) |
|---|---|
| `ТУР` (Noto Sans 23 bold, x=556.5) | 556.5, 1223.7, 600.5, 1241.0 |
| `В` (x=604.7) | 604.7, 1223.7, 620.5, 1240.7 |
| `ЦИФРАХ` (x=625.4) | 625.4, 1223.5, 722.9, 1245.7 |
| `　The round` (Noto Sans CJK SC 23 bold, x=726.6) | 726.6, 1222.2, **865.6**, 1241.0 |

Full title `'ТУР В ЦИФРАХ　The round'`: ink left 556.5, **ink right 865.6**, box right 961.0, **clearance 95.4 px**. Requirement ink right ≤ 957: **PASS with 91.4 px to spare** (was 998.9, −133.3 px).

Visual: 3× crop from the print PDF (`crops/p1-roundnumbers-print.png`, SHA prefix `a9aca3f71fd1b2dd`) — read by eye: `ТУР В ЦИФРАХ　The round` ends well inside the cream box, box right edge visible with clear margin. Web crop (`crops/p1-roundnumbers-web.png`) is byte-identical to the print crop (same SHA).

Spill sweep re-run post-fix (`gates/spill-postfix.log`): 32 cream boxes, **0 ink escapes, 0 bad titles, RESULT: PASS**.

## 4. Gates (all re-run by me on the rebuilt edition)

### 4.1 Occlusion audit — real run, no `--selftest`
`tools/occlusion_audit.py <edition>/svg --json gates/occlusion.json` → rc=1 (by-design "flags present" signal, not a failure). **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE** (`gates/occlusion.log`, `gates/occlusion.json`). Flag set **byte-identical (full dicts) to proof's** `scratch-proof-ru-en2/gates/occlusion.json`.

Adjudication (`adjudicate_ru.py`, `gates/adjudication-ed.log`): **42/42 CLEAR, 0 UNRESOLVED** — including the two P8 `ОТВЕТЫ` flags (gaps 19 px / 20 px vs their English neighbours). Note on method: the adjudicator resolves runs/cards from the directory passed as argv[2]. Pointed at `core-ru` it leaves those 2 flags UNRESOLVED, because the `b` runs (`TEST AND ANSWERS`, `ANSWER KEY — …`) are edition-only English and do not exist in core (`gates/adjudication.log`, 40 CLEAR + 2 UNRESOLVED) — an adjudicator artifact, not a real overlap. Pointed at the **edition** dir (its own SVG + cards, the correct assets for edition flags) all 42 resolve CLEAR, matching proof's 42/42.

### 4.2 P8 compare — CLEAN
`tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150` → noted set **150/150**, rc=0 (`gates/p8-extract.json`). Read directly (not via the log's summary): `gates/p8-compare.json` — `status: CLEAN`, `total: 150`, `missing: []`, `extra: []`, `uncertain: []`, **`keydiff: [137, 138, 139, 140]`** (the four E translation keys, correctly in English), all other 146 keys byte-identical to core. rc=0.

### 4.3 Keycheck — only Q150 differs
Registry dumped from a scratch copy of the rebuilt sources (`rebuild-copy/registry.json`, 150 entries; the copy's rebuilt `p1-pervaya.svg` is byte-identical to production). Registry vs P8 extract (`gates/keycheck.log`): **149/150 match**; only mismatch is **Q150** — registry key `(Open task; model text below)` vs P8 printed `✓` (expected for the open writing task). Q137 `Tuesday 17 November, Students' Day.` matches on both sides.

### 4.4 Freeze — standard core baseline 8/8
`tools/freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg --out gates/freeze-std` → **rc=0, 8/8 SVGs byte-identical**; "core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)" (`gates/freeze-std.log`).

Freeze diff (`--core-svg core-ru/svg --edition-svg <edition>/svg`, rc=0, `gates/freeze-diff.json` + `gates/freeze-adjudicate.log`): per-page +/− strings p1 +20/−21, p2 +39/−36, p3 +26/−28, p4 +28/−28, p5 +29/−27, p6 +34/−32, p7 +49/−51, p8 +173/−627; **removed distinct 484, count-sum 850** (identical to proof's numbers); added CJK total 8, all U+3000 (1 per page); **added Cyrillic-bearing strings 0**; **Cyrillic-bearing removed exactly 15** = Q46 `можно` ×1 + 14 Morozko-caption words (Билибин, Билибина, Зимняя, Иван, Ивана, Иллюстрация, Морозко, год, достояние, иллюстрация, к, ноябрю, общественное, сказка — all P8, image skipped by design), unexplained 0. P1 added string `　The round` present.

### 4.5 Print/web text layer — identical per page
- Plain `pdftotext`: **57,318 bytes each, byte-identical** (`cmp` clean, `text/print.txt`, `text/web.txt`). Layout `pdftotext -layout`: 111,875 bytes each, byte-identical.
- `verify_mine2.py` (proof's script, copied to this scratch; `gates/verify-mine2.log`): page counts 8/8; text multiset identical overall (**30,354** non-whitespace chars) and per page; span-text multisets identical all 8 pages; abutting span-pair gap diff max **0.00 pt**; intra-span char-pair gap diff max **0.00 pt**; D2 6 pinned spots diff **0.000 pt** each; D3 `а`→`»` gap −2.193 pt both; web embeds both italic faces; P1 italic chars 16 = print; D1 straight quotes, no curly quotes, both PDFs.
- verify_mine2 reports **1 FAIL: `D3 space 'я'->'п' identical print/web — print None web None`**. This is the script's **known finder bug** (documented in proof's own PROOF-NOTE: it looks for consecutive `я`,`п` and misses the space char between them). Corrected direct measurement by me (`gates/d3-p1-title2.log`, space char in the WORD OF THE WEEK gloss band, PDF y 1260–1295): space bbox **[1145.576, 1266.762, 1148.108, 1288.725]**, width 2.532 pt, **byte-identical print/web** — exactly proof2's pinned values. D3 still fixed; the FAIL is the checker, not the PDFs.

### 4.6 check_core + s11 + creambox
- `check_core.py` (`gates/check-core.log`): rc=0, **golden BAD 0, gloss fails 0**, P8 SVG text 10,561 chars; 1 orphan line-start (P7 y553 `”».`, known benign) + 1 same-baseline collision (P1 y1712 `чёрная`, known, same as core).
- `s11_check.py` (`gates/s11.log`): rc=0, **FAILURES: none**; 8 SVG; paper #fbfaf6; no #f7f1e2/#c9a227/#8b4513/#000000; badges A2/B1/B2; foot VOL.4 + full-width space; VOL.3 only in P4 correction (×1); masthead 196 px; band 46 px; left margin 88.0; no CJK in visible SVG; both PDFs 8 pages; web 3,380,694 B < 7 MB; web text > 0; **P8 min font ≥ 9.75 pt: 9.75**.
- P8 min font, direct PyMuPDF on the print PDF: **9.75 pt** (411 spans < 10 pt) — agrees with s11.
- `creambox.py` full 8-page scan (`gates/creambox.log`): rc=0; **95 BELOW-WINDOW lines**, same count as proof; normalized diff vs proof's `creambox.log`: exactly **1 line** differs — the P1 title line now reads `'The round'` instead of `'The round in numbers'`. No negative inside-only clearance beyond the classified set.

### 4.7 D5 fonts — recorded only, not judged
`pdffonts` (`gates/fonts-print.log`, `gates/fonts-web.log`): 72 entries each, all emb/sub/uni; print embeds NotoSerif/NotoSans/Newsreader/UnifrakturMaguntia (+ CJK variants); web embeds Lucerna*-renamed subsets including `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`.

## 5. Regression: D1 / D2 / D6 / kicker / Q20 / Q73 — all survive

(`gates/regression.log`, `gates/kicker-final.log`)

- **D1 (core fix1):** text.md L459 `УЧЕБНЫЕ ДАННЫЕ` ✓, L504 `Три уровня, три темы` ✓, L596 `Большой тест недели + все ответы` ✓; all 3 present in the P6/P7/P8 SVGs (concatenated-`<text>` check) ✓; disclaimer in P6 SVG ✓, absent from text.md by design ✓.
- **D2 (Q25):** full phrase `Международный день студента` ×2 in text.md = core ×2 ✓; Q25 option L187 `25. 17 ноября — День студента (key b · Students' Day b)` ✓; 7 D2 spots re-pinned, diff 0.000 pt (see §4.5) ✓.
- **D6 (Q20):** `желании` ×2 in text.md = core ×2 ✓ (L173 stem + L694 key list); P8 extract key 20 = `желании` = registry ✓.
- **Q20 / Q73:** Q20 key `желании` (registry = P8 extract) ✓; Q73 stem L405 `73. [B1 · fill-in] В прошлом году сделали 14,4 млн ___. — key: заказов` and key list L753 `73. заказов — заказ = an order` intact, P8 extract key 73 = `заказов` ✓.
- **Kicker:** 9 double spaces still in `content12.py:18`; PIL true-ink gaps at the 9 double-space boundaries (my measurement, trailing spaces stripped before `ink_box` — PIL `getbbox` counts trailing-space advance in the right edge, e.g. `getbbox('—  ')` right 86 vs 57 for `—` alone at SCALE 4, which produced a spurious −0.1 in the first naive pass): **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2, 9.5, 7.1] px, min 5.0 ≥ 4 — PASS**. Note: proof1's list was [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6], min 5.9 — I could **not** reproduce those exact numbers with `ink_box` on the SVG runs (neither ink gaps nor advance gaps match them); the kicker SVG itself is **byte-identical** to the version proof measured (the p1 SVG diff is the title line only), so the geometry proof passed is unchanged, and my own independent measurement also passes the ≥4 px bar. The method difference is flagged here for the re-proofer rather than glossed over.

## 6. KIT doc fixes (proof1 records, §5 + §7)

In `WEEKLY-KIT.md` (§5 outputs paragraph, §5 text-layer line, §5 text.md line, §7 print/web line, plus a §7 Fix 2 entry following the fix-1 precedent):
1. **§5 text.md SHA added** (was missing): `5960b7a649a8b50036fefa0b16580a2209bc694ea45fb5377a9ee39d9c1296ee`, 62,818 bytes; print/web SHAs + sizes updated to the new rebuild.
2. **pdftotext bytes 57,149 → measured value.** The brief said 57,329 (measured on the **pre-fix** PDFs — I re-verified: pre-fix plain pdftotext was 57,329 on both). The **post-fix** PDFs measure **57,318 bytes on both**, byte-identical — exactly −11 for the removed ` in numbers`. KIT now records 57,318 with a dated correction note explaining the 57,329 → 57,318 step, not the brief's 57,329 (which would be stale the moment this rebuild lands).
3. Same staleness class, same lines: the "character multiset (35,198 chars each)" figures (already stale pre-fix — measured non-whitespace multiset is 30,354 post-fix, 30,363 pre-fix; total chars incl. whitespace are 38,114) were updated to **30,354 non-whitespace chars each (fitz)** in both §5 and §7.
4. Patch-history paragraphs (weight patch 57,149/57,148; italic patch 57,149/57,149) left untouched — they record genuinely historical intermediate states.

## 7. Integrity / scope

- `core-ru` untouched: core print PDF `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`, web `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`, core text.md `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` — all match proof §0; freeze baseline re-hashed the 8 core SVGs before/after and reported them unchanged.
- Production writes limited to this edition dir: `content12.py` (title + comment), `WEEKLY-KIT.md` (doc fixes), rebuild products (`svg/p1-pervaya.svg`, `cards/`, both PDFs, `.text.md`). p2–p8 SVGs byte-identical to pre-fix; no other source file edited.
- Outside the repo: one value in `hidden_files/w47/scratch-fanout-ru/map-en.json` (see §1). No `tools/` change.
- No git add/commit/push/stash/reset, no `insert.py`/`lint --write`, no Discord, no user message. The edition dir remains untracked (`??`, never committed), same as before.

## 8. Evidence files (this scratch)

`FIX-LOG.md` (this file — Fix 1 log above + this Fix 2 section); `spill.py`, `verify_mine2.py`, `dump_reg.py` (copies of proof's scripts, reused unmodified); `gates/` — `run.log`, `render.log`, `webpdf.log`, `textmd.log`, `spill-prefix.log`, `spill-postfix.log`, `occlusion.json/.log`, `adjudication.log` (core-pointed, 40C+2U — artifact, see §4.1), `adjudication-ed.log` (edition-pointed, 42 CLEAR), `check-core.log`, `p8-extract.json/.log`, `p8-compare.json/.log`, `keycheck.log`, `freeze-std.log`, `freeze-diff.json/.log`, `freeze-adjudicate.log`, `s11.log`, `creambox.log`, `verify-mine2.log`, `d3-p1-title.log` (first pass — crashed on a whitespace-only run; superseded), `d3-p1-title2.log`, `kicker.log` (naive pass, superseded), `kicker2.log` (crashed on bounds indexing, superseded), `kicker3.log` (PNG pixel pass), `kicker4.log` (method probe), `kicker-final.log`, `regression.log`, `fonts-print.log`, `fonts-web.log`; `crops/p1-roundnumbers-print.png` + `-web.png` (byte-identical); `text/print.txt`, `text/web.txt`, `text/print-layout.txt`, `text/web-layout.txt`; `rebuild-copy/` (registry dump source copy + `registry.json`).

## 9. Open points for the re-proofer / coordinator

1. Kicker gap numbers: proof1's 9 values could not be reproduced by my `ink_box` method (see §5); my own list passes the ≥4 px bar and the kicker is byte-identical to proof's passing version. Worth one independent re-measurement in re-proof.
2. verify_mine2's D3-space FAIL is its known finder bug; my corrected direct measurement passes (see §4.5).
3. The brief's KIT number 57,329 was pre-fix; KIT now carries the post-fix measured 57,318 — confirm the coordinator agrees this is the intended reading.
4. D5 fonts recorded only, not judged, per brief.
