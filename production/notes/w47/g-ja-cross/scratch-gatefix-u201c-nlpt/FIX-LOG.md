# FIX-LOG — U+201C fix2 port into 5 nl/pt editions (2026-11-11, pre-insert gatefix)

Scope: exactly 5 editions, no other edition touched, no commit, no push, no lint.
- `2026-w47-nl-de`, `core-nl`, `2026-w47-pt-fr`, `2026-w47-pt-it`, `core-pt`
- Scratch: `hidden_files/w47/scratch-gatefix-u201c-nlpt/` (this dir)
- Census method reused verbatim: `census.py` (copied from the es worker's
  `scratch-gatefix-u201c-es/census.py` — per-`<text>` font-family ×
  U+201C/U+201D/U+2019; defective = Noto Sans CJK SC/TC/HK).
- Patch method adapted from the es worker's `patch.py` (same two blocks,
  same verification). `patch.log` + per-edition `*-svglib-pre.py` /
  `*-svglib.diff` in this dir.

## 1. The port (svglib.py, 2 blocks per file)

Source: `core-de/svglib.py` fix2 (commit 4ac7192c, lines 75–105). Ported
**extended to three codepoints** — `if ch in ("\u201c", "\u201d", "\u2019")`
— because fontTools hmtx shows U+201D and U+2019 are also 1000/1000em in
Noto Sans CJK SC/TC (a “-only port would have left the pt-fr/pt-it P1
U+2019 and the core-nl/core-pt U+201D defective). Class derived, not
spelled, per fix2's freeze_direct note; `_QUOTE_CLS` + the two
`_PATH[("sans", …)]` rows below `_pil`. core-de's kinsoku wrap code was
NOT ported (unrelated to this fix). All 5 targets had identical
`_char_font` / `_PATH` / `_NEWS` / `_NEWS_B` structure (verified before
patching); nl-de differs from the other four only by one docstring line.

| edition | svglib.py md5 before → after |
|---|---|
| 2026-w47-nl-de | `78fdfbb037538b1f8a738434ea90a782` → `ff8bc1f4678cf646ce2cf20aa59355b6` |
| core-nl | `4228b7e7fc52caaec9d690f614755b4a` → `152dd0feb7c221d59e778542c890f07b` |
| 2026-w47-pt-fr | `4228b7e7fc52caaec9d690f614755b4a` → `152dd0feb7c221d59e778542c890f07b` |
| 2026-w47-pt-it | `4228b7e7fc52caaec9d690f614755b4a` → `152dd0feb7c221d59e778542c890f07b` |
| core-pt | `4228b7e7fc52caaec9d690f614755b4a` → `152dd0feb7c221d59e778542c890f07b` |

Verification per file (`patch.py`, rc 0, ALL PATCH CHECKS PASS):
py_compile passes; `diff -u` contains ONLY the two ported blocks;
reverse-patch reproduces the pre-patch md5 exactly. Production
svglib.py md5s re-confirmed after sync (same values as above).

## 2. Census before → after (coordinator's method, production svg/)

| edition | before (defective) | after | changed page |
|---|---|---|---|
| 2026-w47-nl-de | 1 defective — P1 U+201C ×1, 19pt, Noto Sans CJK SC (`„Gruppensieg“: erster Platz in der Gruppe, …`) | **0 defective** (1 quote glyph total, now Newsreader) | p1-voorpagina.svg |
| core-nl | 2 defective — P1 U+201C ×1 + U+201D ×1, 19pt, SC (`“小组头名”：小组第一，晋级四分之一决赛。`) | **0 defective** (2 total, Newsreader) | p1-voorpagina.svg |
| 2026-w47-pt-fr | 1 defective — P1 U+2019 ×1, 16pt, SC (masthead `…L’ÉDITION POUR LES LECT…`) + 4 already Newsreader (P8) | **0 defective** (5 total, all Newsreader) | p1-capa.svg |
| 2026-w47-pt-it | 1 defective — P1 U+2019 ×1, 16pt, SC (masthead `…L’EDIZIONE PER I LETTORI…`) + 4 already Newsreader (P8) | **0 defective** (5 total, all Newsreader) | p1-capa.svg |
| core-pt | 2 defective — P7 U+201C ×1 + U+201D ×1, 20.5pt, SC (`、no dia 20；cair 表“落在某日”；…`) + 4 already Newsreader (P8) | **0 defective** (6 total, all Newsreader) | p7-lingua.svg |
| **TOTAL** | **7 defective / 19 quote glyphs** | **0 defective / 19 quote glyphs** | |

Post-sync census rerun on production svg/ (`census-after-production.json`):
0 defective across all 5 editions. Quote glyph count unchanged (19) —
only the rendered font-family changed, no character added or removed.

## 3. Rebuild + gates (per edition, two independent builds)

Build 1: `tools/run_build.py --build production/2026-w47/<ed> --out
<scratch>/<ed>/build1` (run.py + render.py; the wrapper does NOT run
webpdf — the web PDF was built separately with `tools/webpdf.py` on the
build-copy svg/, overwriting the stale copy carried over from production).
Build 2: `tools/freeze.py baseline --build production/… --core-svg
<build1>/svg --out <scratch>/<ed>/freeze` (freeze build-copy deleted
after the check). All 5 editions, identical gate pattern:

| gate | 2026-w47-nl-de | core-nl | 2026-w47-pt-fr | 2026-w47-pt-it | core-pt |
|---|---|---|---|---|---|
| run.py TOTAL | 150 | 150 | 150 | 150 | 150 |
| render.py | exit 0 | exit 0 | exit 0 | exit 0 | exit 0 |
| freeze baseline | 8/8 | 8/8 | 8/8 | 8/8 | 8/8 |
| p8 extract | 150/150 | 150/150 | 150/150 | 150/150 | 150/150 |
| p8 compare | CLEAN, keydiff [137, 138]† | CLEAN, keydiff [] | CLEAN, keydiff [137, 138]† | CLEAN, keydiff [137, 138]† | CLEAN, keydiff [] |
| occlusion | 0 flags, selftest OK | 0 flags, selftest OK | 0 flags, selftest OK | 0 flags, selftest OK | 0 flags, selftest OK |
| spill_sweep | 0 SPILL (34 OBSERVE) | 0 SPILL (35 OBSERVE) | 0 SPILL (59 OBSERVE) | 0 SPILL (60 OBSERVE) | 0 SPILL (61 OBSERVE) |
| boxtitle_check | 0 DEFECT (16 titles, 236 body) | 0 DEFECT (16 titles, 242 body) | 0 DEFECT (20 titles, 258 body) | 0 DEFECT (20 titles, 255 body) | 0 DEFECT (20 titles, 265 body) |
| changed SVG | p1 only | p1 only | p1 only | p1 only | p7 only |
| changed card | p1 only | p1 only | p1 only | p1 only | p7 only |
| print/web pdftotext | 46,746 B, identical | 44,197 B, identical | 47,554 B, identical | 46,833 B, identical | 44,486 B, identical |

† keydiff [137, 138] is PRE-EXISTING, not a regression: comparing the
shipped (pre-patch, P8-byte-identical) edition P8 vs the core P8 gives
the identical `[137, 138]` (`*-p8-compare-shipped.log`). These are the
reader-language translation answers (documented in the nl-de Delta §
and the pt KITs §6). P8 SVGs are byte-identical to the shipped files in
all 5 editions.

## 4. SHAs (lowercase) + sizes — before (disk, pre-state) → after (synced, verified)

text.md is byte-identical in all 5 editions (only the rendered glyph
changed). "Before" sizes are the KIT-recorded values for the pre-round
build; where the disk file's sha differed from the KIT record, see §6.

| edition | print PDF before → after | web PDF before → after | text.md (unchanged) |
|---|---|---|---|
| 2026-w47-nl-de | `4eacaa18…0188bb` → `8e3ba9155d155db85f2b0c03f1595d920ceb8b3220d7652929f67b489f8b1412` (12,669,946 B) | `a4303add…d5b7` → `0139ab963c4e61f534ef537ee17ff3899c029780577036696776055d35c3c360` (1,617,872 B) | `c1342c3f…08aeb`, 46,226 B |
| core-nl | `b7d4a9cd…ce47` → `4f66c7931f8885ddc88c43ad11b40069ea98713e82ccd4b17cfc41388cd5b154` (25,955,680 B) | `3fcd4248…06e0035` → `34273bb871280bbc954600e783307ee7767768f0f64e3cca19fcde52b7ff69e8` (2,104,068 B) | `0b97a48d…7050c`, 44,093 B |
| 2026-w47-pt-fr | `4b9f4147…7653` → `d37d96f19f5ace989a6a234f5da7980466fd70c0b328836a1a2fac5628463926` (12,934,670 B) | `494ff621…db3dce` → `6dcf92f864917874ebbffb28445050d92a2c6a08f85c756dff80be66920b533f` (1,141,326 B) | `39d06879…0a8e2`, 37,699 B |
| 2026-w47-pt-it | `75fd3847…ff67c` → `f9f892d1e36b9545533b7fa6468f9efbcab9de6906bda618c02c9acc0752d55d` (12,930,844 B) | `adcb2934…615f4` → `62c987726bbf87543bfb987f4982f2609c4c3c8eb69269a8bd95300515d92737` (1,137,090 B) | `37c1980c…5209`, 37,419 B |
| core-pt | `4b58f4df…41b6` → `a4f148a5bc9fc82a16986ebf26c28e6eac8609c4fe79376c7d2016e0ad9615a9` (25,312,264 B) | `5b41a94b…5b92c3` → `16fbb7b72bd419f05a5541d48258b4b3f0239c63f2aa0a5cd7d958e9e9dd6649` (1,609,034 B) | `3cd3793f…fbce2`, 36,882 B |

Full SHAs in `pre-state-sha256.txt` / `post-state-sha256.txt`. Post-sync
verification per edition: print/web SHAs equal the scratch build SHAs,
svg/ 8/8 equal, the one changed card equal. Pre/post comparison over all
pre-state files: only the 4 expected files per edition changed
(svglib.py, 1 SVG, print PDF, web PDF); every other pre-state file
byte-identical. KIT files edited separately (see §5).

## 5. KIT edits

Per edition: the current-deliverables SHA/size line(s) updated to the new
values + a dated rebuild-record section appended (history untouched):
- 2026-w47-nl-de: "Files delivered" + new `## U+201C fix2 port (2026-11-11, build 8)`.
- core-nl: §7 Deliverables line + new `## 17. Fix round 6 (2026-11-11, fix2 … port from core-de)`.
- 2026-w47-pt-fr: §6 print/web line + new `## U+201C fix2 port (2026-11-11)`.
- 2026-w47-pt-it: §6 print/web line + new `## U+201C fix2 port (2026-11-11)`.
- core-pt: §6 web/print lines + new `## 8d. fix2 port（第 7 轮，2026-11-11；…)`.

## 6. Pre-existing discrepancies found (NOT caused by this round)

While verifying "old" SHAs, the disk files repeatedly differed from the
KIT-recorded SHAs — i.e. PDFs were rebuilt after the last KIT update
without the KIT being updated. All predate this round; each KIT section
now notes the specific case. Summary (disk sha vs KIT-recorded sha):
- 2026-w47-nl-de: print `4eacaa18…` vs build-7 `26faddf4…`; web `a4303add…`
  vs build-7 `74f10eef…`. (text.md also: disk `c1342c3f…`, 46,226 B vs
  build-7 `ac56f6f9…`, 46,219 B.)
- core-nl: web `3fcd4248…` vs FIX-LOG fix5 `5a47449c…` (print matches).
- 2026-w47-pt-fr: web `494ff621…` vs re-fanout `1f5cc5ad…` (print matches).
- 2026-w47-pt-it: print `75fd3847…` vs re-fanout `6c8a5f3d…`; web
  `adcb2934…` vs re-fanout `5ebf28b4…`.
- core-pt: web `5b41a94b…` vs §6 fix2 `9f2d70e5…` (print matches).
Pattern: webpdf SHAs are non-deterministic run to run (noted in the KITs
themselves), so a webpdf re-run silently invalidates the recorded sha.
Worth a standing rule: whoever rebuilds a PDF updates the KIT sha in the
same step, or the KIT stops recording web SHAs.

## 7. Other notes

- The pt-fr/pt-it KITs §6 recorded the P1 `L’ÉDITION`/`L’EDIZIONE`
  apostrophe gap as a "font rendering quirk, not a defect" — it was this
  U+2019 full-width defect; the port fixes it (both KIT sections say so).
- The pt-it KIT §6 recorded a P1 LINEX graze (quiz rule vs `em Brasília.
  (Página 4)`) as core-carried and deterministic; this rebuild's
  occlusion audit reports 0 flags — core fix1 moved the quiz rule
  2312→2350, so the graze is gone (noted in the pt-it KIT section).
- No de edition, no other edition, and no `scratch-refanout-it2/backup/`
  touched. No commit, no push, no lint (per task).
- `run_build.py` steps are run+render only: the web PDF in the build
  copy is the stale production copy until `tools/webpdf.py` is run on
  the rebuilt SVGs — done explicitly for each edition before sync.

## 8. Disk

- Before: `/dev/mapper/rv 150G, 93G used, 56G free` (`disk-before.txt`).
- After: `150G, 90G used, 60G free` (`disk-after.txt`). Quota cap ~105G
  never approached; no stop was needed.
- Scratch dir total: 160M (5 build-copies + logs + jsons). All 5 freeze
  build-copies deleted after their 8/8 checks.
