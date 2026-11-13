# PATCH LOG — W47 webpdf.py weight patch (ru-en D2 fix)

- Task: W47 webpdf.py 权重补丁执行员（共享工具微任务），叶子，不派 subagent
- Date: 2026-11-11 (UTC 08:33–08:50)
- Edition: `2026-w47-ru-en` (Russian target × English reader), VOL.4
- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`
- Notes dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-webpdf-patch1/`
- Read first: `~/workspace/weekly-git/SOP.md` §8 + §1.1, `hidden_files/w47/briefs/brief-coordinator.md`,
  `hidden_files/w47/scratch-fix-ru-en1/FIX-LOG.md` §3 ("D2 patch proposal"), `~/workspace/weekly-git/AGENTS.md`
- Scope: ONE line in `tools/webpdf.py` (`fc_match`) + rebuild ONLY the ru-en web PDF
  + update the web-PDF line in that edition's `WEEKLY-KIT.md`. No other edition, no
  other tool file, no `insert.py`, no `lint --write`, **no git writes of any kind**
  (no commit, no push — the patch commit is the coordinator's to arrange).

## 0. Startup probes — PASSED (2026-11-11 08:33 UTC)

- `df -h ~/workspace`: 45 GB free (150G total, 105G used). No quota pressure.
- `echo probe-test | git hash-object -w --stdin` → `c4b82938c3a39fd8ec5762c339240e6c87d1e1b1`, RC=0
- Real write probe: `scratch-webpdf-patch1/PROBE.txt` written and read back OK.
- No EDQUOT at any point.

## 1. The patch (applied exactly per FIX-LOG §3)

File: `~/workspace/weekly-git/tools/webpdf.py`, function `fc_match` (line ~70).
`git diff` (whole diff — this is the entire change):

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

No other line in the file touched (verified by `git diff -- tools/webpdf.py`:
1 line removed, 5 added — the comment + the query line).

## 2. fc-match抽查 — 改前 / 改后

### 改前（plain `fc-match`, before the patch)

| Query | Resolves to |
|---|---|
| `Newsreader` | `~/.local/share/fonts/Newsreader-Regular.ttf` |
| `Newsreader:style=Bold` | `Newsreader-Regular.ttf` (WRONG — bold collapses to Regular) |
| `Noto Sans` (bare) | `/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf` (WRONG — print uses Medium) |
| `Noto Sans:style=Bold` | `NotoSans-Bold.ttf` |
| `Noto Serif` (bare) | `NotoSerif-Regular.ttf` (WRONG — print uses Medium) |

Control (numeric weights, what the print pipeline actually requests):

| Query | Resolves to |
|---|---|
| `Newsreader:weight=200` | `Newsreader-SemiBold.ttf` |
| `Newsreader:weight=100` | `Newsreader-Regular.ttf` |
| `Noto Sans:weight=100` | `NotoSans-Medium.ttf` |
| `Noto Sans:weight=200` | `NotoSans-Bold.ttf` |
| `Noto Serif:weight=100` | `NotoSerif-Medium.ttf` |
| `Noto Serif:weight=200` | `NotoSerif-Bold.ttf` |

### 改后（patched `webpdf.fc_match`, called directly)

| Family / weight | Resolves to |
|---|---|
| Newsreader bold | `Newsreader-SemiBold.ttf` ✓ (was Regular) |
| Newsreader regular | `Newsreader-Regular.ttf` ✓ (unchanged) |
| Noto Sans regular | `NotoSans-Medium.ttf` ✓ (was Regular) |
| Noto Sans bold | `NotoSans-Bold.ttf` ✓ (unchanged) |
| Noto Serif regular | `NotoSerif-Medium.ttf` ✓ (was Regular) |
| Noto Serif bold | `NotoSerif-Bold.ttf` ✓ (unchanged) |

Matches FIX-LOG §3's verification exactly.

## 3. Web PDF rebuild (only ru-en, patched tool)

Command (in the edition dir, `tools/venv/bin/python`):

```
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg Lucerna-VOL4-ru-en-web.pdf
```

Exit 0. Build log: `webpdf-build.log` (in this notes dir).
- 8 pages from `svg`; 155 distinct chars; families: Newsreader, Noto Sans,
  Noto Sans CJK SC, Noto Serif, Noto Serif CJK SC, UnifrakturMaguntia.
- **`LucernaNewsreader-Bold` subset is now built: 20,468 bytes** (previously
  skipped — the skip rule `bold == regular` fired because both resolved to
  Regular). `LucernaNotoSans-Regular` / `LucernaNotoSerif-Regular` subsets are
  now built from the Medium files (31,132 B / 46,440 B).
- The fontTools `fsSelection bit 5 (bold) and head table macStyle bit 0 (bold)
  should match` warning appears when saving the SemiBold-derived Bold subset —
  same warning FIX-LOG §3 noted; the subset embeds and renders correctly
  (verified by span measurement, §4).
- Output: `WROTE Lucerna-VOL4-ru-en-web.pdf: 3,367,620 bytes, 57,148 text bytes`.

### Identity — NEW web PDF, print PDF untouched

| File | Bytes | SHA-256 | Pages |
|---|---|---|---|
| Print `Lucerna-VOL4-ru-en.pdf` | 21,245,374 (unchanged) | `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e` (unchanged) | 8 |
| Web `Lucerna-VOL4-ru-en-web.pdf` (OLD, fix1) | 3,341,905 | `0c7ebd6ad6f808623228a39b56508d46df2e74fbe16eb89392e325c5aaced46e` | 8 |
| Web `Lucerna-VOL4-ru-en-web.pdf` (**NEW, patched**) | **3,367,620** (+25,715 B, +0.77%) | **`82dfb6eaeff6eaa7d9851c723404dc27536fd41225804921d2071e522bae65ec`** | 8 |

- Web PDF < 7 MB ✓.
- Print SHA verified identical before and after the rebuild (same command run
  both times); no `run.py`/`render.py` re-run was performed, so no print output
  could have changed. `pdffonts` on the new web PDF shows `LucernaNewsreader-Bold`
  subsets embedded (multiple pages), confirming the bold face now exists.

## 4. D2 — 7 处空隙改前 / 改后（逐处实测，精确值）

Method: `d2spots.py` (in this notes dir) — direct span lookup in both PDFs,
gap = following-span x0 − preceding-span x1. Full log: `d2pin.log`
(`d2pin.py`, copied from fix1's `exp/`, read-only against the new PDFs).

| # | Spot | 改前 web gap (fix1, FIX-LOG §2) | 改后 web gap (this run) | 改后 print gap | ≤ 0.5 pt? |
|---|---|---|---|---|---|
| 1 | P1 headline 39.8 pt, `14-` \| `й тур` | 4.33 pt | **0.00 pt** (A x1=133.02, B x0=133.02) | 0.00 pt | ✓ |
| 2 | P4 heading 24 pt, `14-` \| `й тур` | 2.62 pt | **0.00 pt** (106.46 / 106.46) | 0.00 pt | ✓ |
| 3 | P1 contents-1 15 pt, `1. 14-` \| `й тур` | 2.20 pt | **−0.31 pt** (1138.69 / 1138.38; 0.31 pt overlap, invisible) | −0.31 pt | ✓ |
| 4 | P4 band-sub 13.5 pt, ` все восемь результатов` \| `+` | 1.94 pt | **−0.14 pt** (1008.74 / 1008.61) | −0.14 pt | ✓ |
| 5 | P1 contents-3 15 pt, `3. «` \| `Чёрная пятница` | 1.17 pt | **−0.29 pt** (1122.22 / 1121.94) | −0.29 pt | ✓ |
| 6 | P5 title 24 pt, `«` \| `Чёрная пятница` | 0.91 pt | **0.00 pt** (80.11 / 80.11) | 0.00 pt | ✓ |
| 7a | P7 16.12 pt, `«` \| `Поздравляю…` | 0.58 pt | **0.00 pt** (1105.61 / 1105.61) | 0.00 pt | ✓ |
| 7b | P7 16.12 pt, `«` \| `Я покупаю…` | 0.58 pt | **0.00 pt** (1105.61 / 1105.61) | 0.00 pt | ✓ |

All 7 spots now match the print PDF exactly at every boundary (web gap ==
print gap to 0.01 pt). The three negative values are overlaps the PRINT PDF
itself already has — web is now identical to print, not "more overlapped".
All 7 ≤ 0.5 pt ✓. Values match FIX-LOG §3's patched-copy prediction
(0.00 / 0.00 / −0.31 / −0.14 / −0.29 / 0.00 / 0.00) exactly.

## 5. Abutting-span 全版扫描

Method: `d2scan.py` (proofer's line-based method, copied from fix1 `exp/`,
output repointed to this notes dir) + `d2scan-full.py` (same matcher, counts
all abutting pairs and the worst gap). Logs: `d2scan.log`, `d2scan-full.log`,
`d2-scan.json`, `d2-spots.json`.

- Abutting pairs scanned: **1,704**
- Gaps > 0.5 pt: **0**
- Worst web gap overall: **0.05 pt** (P7, 16.12 pt, ` «` | `по данным пресс`)
- No new gaps introduced anywhere. Matches FIX-LOG §3 exactly (1,704 / 0 / 0.05).

## 6. 文字层比对（print vs web，逐页）

- `pdftotext` bytes: print **57,149** / web **57,148** (both > 0). Saved:
  `print.txt`, `web.txt`.
- Non-whitespace chars: **30,293 each**, per-page counts identical
  (P1 3078, P2 3396, P3 2707, P4 3357, P5 2939, P6 2752, P7 3580, P8 8484).
- Character multiset identical **overall AND per page** (PyMuPDF
  `collections.Counter` per page, all 8 pages True).

## 7. KIT 更新

`production/2026-w47/2026-w47-ru-en/WEEKLY-KIT.md` only (this edition's KIT;
no other edition's KIT touched):

- §5 web-PDF line: 3,341,905 B / `0c7ebd…` → **3,367,620 B / `82dfb6…`**;
- §5 web-PDF paragraph: pdftotext 57,196 → 57,148 + added the patched-rebuild
  record line (7 D2 gaps, 1,704-pair scan);
- §7 "§1.1 spot-checks" line: web 3,341,905 → 3,367,620 bytes;
- §7 Fix 1 / D2 bullet: appended the "Webpdf weight patch APPLIED + web PDF
  rebuilt" sub-bullet with the patch, the new SHA, the 7 measured gaps and the
  re-run gates.
- Print-PDF line, `.text.md` line and all other KIT content untouched.

## 8. Git 状态（未提交 — 按任务要求）

- **No git writes performed**: no `git add`, no commit, no push, no stash,
  no reset, no `insert.py`, no `lint --write`.
- `git status --short -- tools/webpdf.py production/2026-w47/2026-w47-ru-en/`
  shows: ` M tools/webpdf.py` and `?? production/2026-w47/2026-w47-ru-en/`
  (the whole edition dir is untracked in this clone — same state as fix1 left
  it; the only files I changed inside it are `Lucerna-VOL4-ru-en-web.pdf`
  and `WEEKLY-KIT.md`; SVGs/content untouched — confirmed by freeze 8/8,
  GATE-LOG §3).
- The wider tree is dirty from other lines' pre-existing W43 work
  (`issues/2026-w43/*`, `production/2026-w43/*`, `tools/freeze.py`,
  `tools/occlusion_audit.py`, `tools/p8.py`); none of it is mine and none was
  touched. The patch commit is left for the coordinator to arrange as a
  standalone commit.

## 9. Files in this notes dir

- `PROBE.txt`, `PATCH-LOG.md` (this file), `GATE-LOG.md`
- `webpdf-build.log` — patched webpdf.py build output
- `d2pin.py` + `d2pin.log` — per-spot span dump (read-only)
- `d2scan.py` + `d2scan.log` + `d2-scan.json` — proofer-method abutting scan
- `d2scan-full.py` + `d2scan-full.log` — full scan (1,704 pairs, worst gap)
- `d2spots.py` + `d2-spots.json` — exact per-spot gap table
- `print.txt`, `web.txt` — pdftotext output, print vs web
- `occlusion.json`, `occlusion.log` — occlusion audit
- `p8-extract.json`, `p8-compare.json`, `p8-compare.log` — P8 gates
- `freeze.log`, `freeze/` — freeze baseline rerun (build copy + SVGs)
