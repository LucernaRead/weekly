# FIX-LOG — W47 new standing gates: 9 ja boxtitle defects + 1 ko-it spill

**Date:** 2026-11-12 (UTC). **Gates source:** commit `45ca73fc` (three standing pre-insert gates),
130-wide run 2026-11-12 01:54 UTC — report `hidden_files/w47/Reports-preinsert/new-gates-130.md`,
aggregate `hidden_files/w47/scratch-new-gates/aggregate.json`,
per-edition evidence `hidden_files/w47/scratch-new-gates/per-edition/`.
**Scope of this fix:** editions `2026-w47-ja-de`, `ja-es`, `ja-fr`, `ja-it`, `ja-nl` (9 boxtitle defects)
+ `2026-w47-ko-it` (1 spill). Nothing else touched; no `it-ru` / `ru` family / `*-ru` file.
**Work dir:** `~/workspace/weekly-git` (main only, no branch). **No commit / push / lint** (per task).
**Scratch for this fix:** `hidden_files/w47/scratch-gatefix-ja-koit/` (this dir).

## 0. Verification of the reported defects (all 10 reproduced exactly)

Re-ran the gates on the production files **before** any edit:

| Edition | Gate | Result (matches the 130-wide report exactly) |
|---|---|---|
| ja-de | boxtitle | 2 DEFECT: P1 `数字で見る今週　Die Woche in Zahlen` +6.5px; P7 `今週のフレーム　Satzmuster der Woche` +36.5px |
| ja-es | boxtitle | 1 DEFECT: P7 `今週のフレーム　Estructura de la semana` +54.5px |
| ja-fr | boxtitle | 3 DEFECT: P1 `数字で見る今週　La semaine en chiffres` +30.5px; P7 `まちがい診療所　Clinique des erreurs` +9.5px; P7 `今週のフレーム　Structure de la semaine` +50.5px |
| ja-it | boxtitle | 2 DEFECT: P1 `数字で見る今週　La settimana in cifre` +8.5px; P7 `今週のフレーム　Struttura della settimana` +68.5px |
| ja-nl | boxtitle | 1 DEFECT: P7 `今週のフレーム　Structuur van de week` +36.5px |
| ko-it | spill | 1 SPILL: P2 BELOW +8.76px, word `kimchi` (19pt Italian gloss), box `[1439.5, 1618.0, 422.5, 150.0]`, bottom 1768.0, line at 1776.8; 142 OBSERVE |

Note on the task brief: it said "P1 in 4 editions (de/es/fr/it)" — the report files are authoritative and
show **P1 in 3 editions (de/fr/it)**; ja-es P1 (`La semana en cifras`, 405.5px) is +1.0px, i.e. marginal
tolerance, not a defect, and was left untouched. ja-fr carries a 10th-listed-in-report defect the brief
did not name separately (P7 `まちがい診療所`, +9.5px). Total is still 9 boxtitle defects.

## 1. The shared ja cause (one cause, one fix pattern)

Every defective title is a bilingual `JPタイトル　<reader-language gloss>` rendered as **one 23pt line**
in a 422.5px-wide cream box whose inner width (after the 18px pad) is **386.5px**:

| Title | Width at 23pt | JP part | Gloss part |
|---|---|---|---|
| 数字で見る今週　Die Woche in Zahlen (de P1) | 411.2 | 161.0 | 227.2 |
| 数字で見る今週　La semaine en chiffres (fr P1) | 435.2 | 161.0 | 251.2 |
| 数字で見る今週　La settimana in cifre (it P1) | 413.5 | 161.0 | 229.5 |
| 数字で見る今週　La semana en cifras (es P1, NOT a defect) | 405.5 | 161.0 | 221.5 |
| 数字で見る今週　De week in cijfers (nl P1, fits) | 380.5 | 161.0 | — |
| 今週のフレーム　Satzmuster der Woche (de P7) | 436.9 | 160.3 | 253.6 |
| 今週のフレーム　Estructura de la semana (es P7) | 455.3 | 160.3 | 272.0 |
| 今週のフレーム　Structure de la semaine (fr P7) | 450.9 | 160.3 | 267.6 |
| 今週のフレーム　Struttura della settimana (it P7) | 468.8 | 160.3 | 285.5 |
| 今週のフレーム　Structuur van de week (nl P7) | 437.4 | 160.3 | 254.0 |
| まちがい診療所　Clinique des erreurs (fr P7) | 410.3 | 161.0 | 226.3 |

The core (`core-ja`) fits because its gloss is the short Chinese `数字看本周` / `本周句式` — its P1 title
is **exactly 386.5px**, i.e. the box was sized for the core's gloss. The fan-out builder appends the
reader-language gloss onto the same single line with no width check (`Flow.box` draws the title blind,
and the P7 col-3 titles are bare `p.text` calls). Every other `f.box` title in these editions is the
short `九州場所の記録　3日目まで` (289.6px, fits), so the defect class is exactly these bilingual titles.

**Fix pattern (layout only, zero word changes):** split the title onto two lines — JP title at 23pt,
gloss at 19pt. Both lines then fit with 140–190px of margin (worst gloss line 235.9px vs 386.5px inner).
Two sites:

- **P1 (`Flow.box`, `bslib4.py`, edited in ja-de / ja-fr / ja-it only):** `box()` now splits a title on
  `　` into `[(JP, tsize), (gloss, tsize-4)]` **only when** `text_w(title) > iw` (inner width); fitting
  titles (incl. the core pattern) render byte-identically. Box height grows by one title slot
  (+29px: 19pt + 10). The P1 flow has ample slack (ends col 2 y=921, bottom 1828, unchanged after the fix).
- **P7 col-3 boxes (`content7.py`, all 5 editions):** the frame title is two `p.text` lines
  (JP 23pt at `yy3+26`, gloss 19pt at `yy3+53`), box height constant 62→89 (+27), `yy3 += 52` → `79`.
  **Binding constraint:** the P7 teaser sat only 22.9–25.4px above the footer (2580) in de/es/fr/nl, so a
  plain +27px would have pushed the teaser over the footer. The col-3→phrases gap was reclaimed 14px
  (`fy = max(1712, col3_end + 44)` → `+ 30`; the rule line at `fy-14` still clears the box by 16px),
  net teaser shift **+13px** in every edition. ja-it had 51.9px slack and got the same uniform change.
- **ja-fr clinic exception:** the clinic title is only +9.5px over, so it got the minimal fix instead —
  23→21pt single line (374.6px vs 386.5px inner, 11.9px margin), **no height change**. A second two-line
  box in fr would have cost +54px total, which no gap reclaim could absorb.

**ko-it spill (separate cause, same week):** the P2 D-day strip's four gloss lines share one 19pt
`p.para` call in a fixed 150px box. The Kimchi Day gloss `22 nov. — giorno di condivisione del kimchi`
is 379.9px at 19pt — 1.4px over the 378.5px inner width — so it wrapped and `kimchi` landed below the
box. Fix: gloss size **19→18pt, uniform for all four D-day glosses** (one token, `content12.py`); at 18pt
the line is 360.0px, one line, 18.5px margin. No box-height change (the next row sits at dy+228, only
~5px below the box bottom, so growing the box was impossible). No words changed.

**No content change anywhere:** no word added, removed, or substituted in any of the 10 defects, so no
edition needs re-proof on content grounds. `text.md` files are untouched (their title strings are
word-identical; a future re-export from source would render the split titles on two lines — noted here
for the coordinator; ko-it's `textmd.py` exports from source literals, so its text is byte-identical by
construction).

## 2. Source edits (production files only; core-* untouched)

| File | Edit |
|---|---|
| `2026-w47-ja-de/bslib4.py`, `2026-w47-ja-fr/bslib4.py`, `2026-w47-ja-it/bslib4.py` | `Flow.box`: two-line split when title too wide (comment `W47 gatefix (boxtitle)`) |
| `2026-w47-ja-{de,es,fr,it,nl}/content7.py` | P7 frame title → two lines; `wh` 62→89; `yy3 += 52`→`79`; `fy` gap 44→30 |
| `2026-w47-ja-fr/content7.py` | P7 clinic title 23→21pt |
| `2026-w47-ko-it/content12.py` | D-day gloss `cn` 19→18pt |
| `WEEKLY-KIT.md` × 6 | §7 bullet + §8b "Fix round 2 re-gates" + §11 F5 (ja); Fixes-log #3 + gates + output sizes (ko-it). KIT §8 history lines untouched. |
| `Lucerna-VOL4-*.pdf`, `Lucerna-VOL4-*-web.pdf`, `svg/*.svg`, `cards/*.png` × 6 | Synced from the fix1 scratch builds, SHAs verified after copy (see §4). |

## 3. Per-edition results

### ja-de — 2 defects → 0
- **Before:** P1 +6.5px, P7 frame +36.5px. P7 col3 ends 1780.62, teaser 2554.62 (25.38px clear).
- **Fix:** bslib4 `box()` split (P1) + P7 frame two-line + fy gap reclaim.
- **After:** boxtitle 0 DEFECT / 0 OBSERVE; spill 0 SPILL. P1 flow ends col 2 y=921 (unchanged).
  P7 col3 ends **1807.62** (+27), teaser **2567.62** (+13, 12.38px clear). P8-keys ends col 3 y=2382 (unchanged).
  New line widths: P1 161.0 / 187.7; P7 160.3 / 209.5 (inner 386.5).
- **SVG diff vs pre-fix:** p1 + p7 only (p2–p6, p8 byte-identical).
- **PDFs:** print `Lucerna-VOL4-JA-DE.pdf` 29,102,672 B, sha256
  `8e363c770b13d8730886476b4f7826fb2f949dfc9ad9e8eeec7fe3b9e806e3f0`;
  web `Lucerna-VOL4-JA-DE-web.pdf` 4,483,776 B, sha256
  `79bee8c62b0d0cb3b2e2b800008b891b9d8bc6cb1cda7ab18610457f75e0661a`, 46,844 text bytes.
  Text layers: `pdftotext -layout` identical (105,390 B each); plain identical (46,844 B).
- **Standard gates:** run.py TOTAL 150 (A2 48 / B1 73 / B2 29), 0 FLOW OVERFLOW; freeze 8/8;
  p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 140]; occlusion 0 flags, 0 NEW vs core.
- **Visual:** crops `crop-ja-de-p1-title.png`, `crop-ja-de-p7-frame.png` — two-line titles inside the boxes.

### ja-es — 1 defect → 0
- **Before:** P7 frame +54.5px. P7 col3 ends 1783.1, teaser 2557.1 (22.9px clear).
- **Fix:** P7 frame two-line + fy gap reclaim. (`bslib4.py` untouched; P1 is marginal +1.0px, not a defect.)
- **After:** boxtitle 0/0; spill 0. P7 col3 ends **1810.1**, teaser **2570.1** (+13, 9.9px clear). P8-keys 2397.
  New line widths: P7 160.3 / 224.7.
- **SVG diff:** p7 only.
- **PDFs:** print 29,102,118 B, sha256 `3d2dd5ccfaaa1772c51e40e7e641741030c66d444b88dfd73f61fbbbbeb591b8`;
  web 4,482,738 B, sha256 `e90339aff956306c5178a204325a4bab72b483d2c8b8cde38d95cf61fcf54f78`, 47,036 text bytes.
  Text layers identical (-layout 102,060 B; plain 47,036 B).
- **Standard gates:** TOTAL 150, 0 overflow; freeze 8/8; p8 150/150, CLEAN, keydiff [137–140]; occlusion 0.

### ja-fr — 3 defects → 0
- **Before:** P1 +30.5px, P7 clinic +9.5px, P7 frame +50.5px. P7 col3 ends 1783.1, teaser 2557.1.
- **Fix:** bslib4 `box()` split (P1) + clinic 23→21pt + P7 frame two-line + fy gap reclaim.
- **After:** boxtitle 0/0 (24 titles counted — the 21pt clinic title falls below the gate's 22pt TITLE floor
  and is counted as a body line; it is still measured, 0 overflow); spill 0.
  P7 col3 ends **1810.1**, teaser **2570.1** (+13, 9.9px clear). P8-keys 2411.
  New line widths: P1 161.0 / 207.5; clinic 374.6 (single line); P7 160.3 / 221.1.
- **SVG diff:** p1 + p7 only.
- **PDFs:** print 28,348,049 B, sha256 `a7761f35ac590eacd963718ed8780ddf0978fecc8d972a51375b411a4cdc83af`;
  web 4,458,635 B, sha256 `cc50c80d2dafdc09f08d4f543b695af580ec35a11e9ce21bb5c0ddccfcfb19d2`, 47,212 text bytes.
  Text layers identical (-layout 104,271 B; plain 47,212 B).
- **Standard gates:** TOTAL 150, 0 overflow; freeze 8/8; p8 150/150, CLEAN, keydiff [137–140]; occlusion 0.
- **Visual:** crops `crop-ja-fr-p1-title.png`, `crop-ja-fr-p7-clinic.png`, `crop-ja-fr-p7-frame.png` — all clean.

### ja-it — 2 defects → 0
- **Before:** P1 +8.5px, P7 frame +68.5px (worst of the nine). P7 col3 ends 1754.1, teaser 2528.1 (51.9px clear).
- **Fix:** bslib4 `box()` split (P1) + P7 frame two-line + fy gap reclaim (uniform with the others).
- **After:** boxtitle 0/0; spill 0. P7 col3 ends **1781.1**, teaser **2541.1** (+13, 38.9px clear). P8-keys 2442.
  New line widths: P1 161.0 / 189.6; P7 160.3 / 235.9.
- **SVG diff:** p1 + p7 only.
- **PDFs:** print 29,099,202 B, sha256 `58c74118ae3f79beab02458c9bb1d459048b88567b75dfc6b8b232cba79ec10f`;
  web 4,477,024 B, sha256 `ff47d54a9af1bd5dfa449eb4a2e4b8c3304d49466c18d8d1715256572f725431`, 47,004 text bytes.
  Text layers identical (-layout 106,305 B; plain 47,004 B).
- **Standard gates:** TOTAL 150, 0 overflow; freeze 8/8; p8 150/150, CLEAN, keydiff [137–140]; occlusion 0.
- **Visual:** crops `crop-ja-it-p1-title.png`, `crop-ja-it-p7-frame.png` — clean.

### ja-nl — 1 defect → 0
- **Before:** P7 frame +36.5px. P7 col3 ends 1780.62, teaser 2554.62 (25.38px clear). P1 fits (380.5px).
- **Fix:** P7 frame two-line + fy gap reclaim. (`bslib4.py` untouched.)
- **After:** boxtitle 0/0; spill 0. P7 col3 ends **1807.62**, teaser **2567.62** (+13, 12.38px clear). P8-keys 2428.
  New line widths: P7 160.3 / 209.8.
- **SVG diff:** p7 only.
- **PDFs:** print 29,099,152 B, sha256 `f6623ccc5c7ea2edc808c70d9ccfe474a8c1127c4dd551db4344f33dc3692618`;
  web 4,476,538 B, sha256 `fefa1c02e62d2ef1ab356e32e36463bbbadde3524e437dab19d6afd881841c43`, 45,932 text bytes.
  Text layers: plain `pdftotext` identical (45,932 B). **`pdftotext -layout` differs by ONE space on the P1
  masthead line** (line 7, `Lucerna   VOL.4` vs `Lucerna    VOL.4`) — **proven pre-existing, not a regression:**
  the same 1-space diff appears in the rebuilt pre-fix PDFs (baseline web PDF 4,476,527 B / 45,931 text bytes,
  exactly the pre-fix §8 record), and the masthead SVG text is byte-identical baseline vs fix. It is a
  `-layout` column artifact on an untouched line; the characters are identical.
- **Standard gates:** TOTAL 150, 0 overflow; freeze 8/8; p8 150/150, CLEAN, keydiff [137–140]; occlusion 0.

### ko-it — 1 spill → 0
- **Before:** P2 D-day strip, `kimchi` BELOW +8.76px (box bottom 1768.0, line 1776.8). P2 col3 ends 1197.95,
  P7 teaser 2483.7, P8-keys 2442.
- **Fix:** D-day glosses 19→18pt, uniform (see §1). Wrap-verified first: 360.0px one line.
- **After:** spill 0 SPILL (142 OBSERVE, same count as baseline); boxtitle 0/0. P2 col3 ends 1197.95,
  P7 teaser 2483.7, P8-keys 2442 — **all unchanged**. The 18pt gloss sits one line inside its box.
- **SVG diff:** p2 only (p1, p3–p8 byte-identical).
- **PDFs:** print `Lucerna-VOL4-KO-IT.pdf` 45,676,962 B, sha256
  `3c48b6f4744cd0cf4cafe47fb6ba22d77bca39d1c6f98d1ff164ee85b52f632f`;
  web `Lucerna-VOL4-KO-IT-web.pdf` 4,025,958 B, sha256
  `4d15cd38f0a5b9c8454d115329e9b87b0c077c5816a6b080ee000bdfe16431fd`, 51,894 text bytes.
  Text layers identical (plain 51,894 B; `-layout` 107,337 B).
- **Standard gates:** TOTAL 150 (A2 51 / B1 72 / B2 27), 0 overflow; freeze 8/8; p8 150/150, compare CLEAN,
  keydiff [137, 138] (unchanged from run 1); occlusion 0 flags, 0 NEW vs core.
- **Visual:** crops `crop-ko-it-p2-dday-strip.png`, `crop-ko-it-p2-kimchi.png` — all four glosses one line,
  inside their boxes; the strip stays uniform.

## 4. Sync (production) + final confirmation

Synced from each edition's `fix1` scratch build-copy into its production dir: `svg/*.svg` (8),
`cards/*.png` (8), print PDF + web PDF. Fix1 is canonical: the `fix2` freeze re-run proved its SVGs
8/8 byte-identical, and fix2 held no fresh renders. Post-copy verification: **all 12 PDF SHAs match fix1
exactly, all 6 SVG sets 8/8 match fix1**.

Final confirmation re-run **on the production files** after sync:
`boxtitle_check.py` on the 5 ja production dirs → **0 DEFECT / 0 OBSERVE in all 5** (with core-ja comparison);
`spill_sweep.py` on ko-it production → **0 SPILL**; spill on the 5 ja production dirs → **0 SPILL** each.
Gate JSONs: `gate-production-boxtitle/`, `gate-production-spill/`, `gate-production-spill-ja/`.

## 5. Build notes / tool gaps found (flag, not fixed — outside this task's scope)

1. **`run_build.py` ko-family render gap:** the wrapper runs ko-family builds (incl. the render step) under
   `/usr/bin/python3`, but `render.py` imports `cairosvg`, which is not installed for that interpreter
   (`ModuleNotFoundError: No module named 'cairosvg'`). The ko-it fix1 wrapper run therefore failed at the
   render step (rc=1) even though the run step was clean (TOTAL 150). The render was re-run by hand with
   `tools/venv/bin/python render.py` on the same build-copy (fresh print PDF 45,676,962 B); the run-step SVGs
   are untouched by that. The wrapper should use the venv interpreter for the render step even for ko-family
   builds (the `/usr/bin/python3` rule exists for the run step's Pillow-10 measurement). Recorded in the ko-it
   KIT (Mechanical gates) as well.
2. **Disk:** 98.6 GiB used at task start, 98.2 GiB after this fix's cleanup. `df -h` showed "100G" mid-task
   (GB rounding); exact bytes were 98.6 GiB, below the 100G stop line, and the sync overwrites in place
   (no net growth). Scratch bulk cleaned: build-copy cards+PDFs deleted after sync verification
   (builds/ 390M → 93M); SVGs, logs, SHA lists, gate JSONs, and crops kept as evidence.
3. **Memory:** renders ran strictly serially, one edition at a time; other agents were active concurrently
   (available memory swung 1.1–2.7 GB), no OOM.

## 6. What was NOT done

- No commit / push / lint (per task — the coordinator owns that).
- No `text.md` changes (no content change; see §1).
- No re-proof assigned (no words changed; the layout changes are verified by gates + visual crops).
- `core-ja` / `core-ko` untouched. No edition outside the six listed was modified
  (verified: F5 appears in exactly ja-de/es/fr/it/nl KITs; ko-it KIT carries fix #3; no other KIT changed).
- ja-es P1 (+1.0px marginal) and ja-nl P1 (fits) deliberately untouched.

## Evidence map (all under `hidden_files/w47/scratch-gatefix-ja-koit/`)

- `gate-baseline-boxtitle/`, `gate-baseline-spill/` — pre-fix gate JSONs (defects reproduced).
- `builds/<edition>-base/` — pre-fix rebuild (run-only) + logs; `builds/<edition>-fix1/` — fixed build
  (run+render + webpdf) + logs; `builds/<edition>-fix2/` — freeze re-run + logs;
  `builds/<edition>-sha-fix1.txt`, `-sha-fix2.txt` — SVG SHA lists.
- `gate-fix1-boxtitle/`, `gate-fix1-spill/` — post-fix gates on fix1 builds.
- `gates-<edition>-fix1-p8.json`, `-p8compare.json`, `-occlusion.json` — standard gates.
- `gate-production-boxtitle/`, `gate-production-spill/`, `gate-production-spill-ja/` — final production gates.
- `crop-*.png` — visual crops (ja-de P1/P7, ja-fr P1/P7-clinic/P7-frame, ja-it P1/P7-frame, ko-it P2 strip + kimchi box).
- `textlayer-*.txt` — print vs web `pdftotext -layout` extracts (+ `textlayer-ja-nl-BASE-*.txt` for the
  pre-existing-diff proof).
- `*.sh`, `apply-kit-updates.py` — the exact scripts used for builds, gates, freeze, and KIT updates.
- This file: `FIX-LOG.md`.
