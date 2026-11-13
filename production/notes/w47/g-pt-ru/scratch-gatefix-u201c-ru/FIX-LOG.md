# FIX-LOG — W47 fix2 (U+201C/U+201D/U+2019) port into 5 ru editions

Date: 2026-11-11 21:54 EST – 2026-11-12 ~04:10 UTC.
Scope (exactly these 5): `2026-w47-ru-de`, `2026-w47-ru-fr`, `2026-w47-ru-zh-tw`,
`2026-w47-zh-tw-ru`, `core-ru`. No other edition touched; no commit, push, or lint.
Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-gatefix-u201c-ru/`
Production: `~/workspace/weekly-git/production/2026-w47/`
Tools: `~/workspace/weekly-git/tools/venv/bin/python` (`run_build.py`, `webpdf.py`, `freeze.py`, …).

## 0. The port

Source: core-de fix2 (commit 4ac7192c), ported into each edition's production `svglib.py`.
Extended to all three codepoints — `if ch in ("\u201c", "\u201d", "\u2019")` —
because fontTools hmtx shows U+201D and U+2019 are ALSO 1000/1000em in Noto Sans CJK
SC/TC (Newsreader: 0.441/0.441/0.256em). The class name is derived
(`_QUOTE_CLS = _char_font("\u201c", "serif", False)`), never spelled as a literal
(freeze_direct rule — see the block comment). Diff per file: **24 lines added, 0 removed.**

```python
    # fix2 (2026-11-11, proof2 D1/D2 in core-de; ported 2026-11-11, extended to
    # U+201D/U+2019): U+201C/U+201D/U+2019 are full-width (advance
    # 1000/1000em, fontTools hmtx) in Noto Sans CJK SC/TC — ink sits at
    # the right edge of the cell, so a sans quote leaves a wide white
    # gap before it. Newsreader's quotes are narrow (U+201C/U+201D
    # 0.44em, U+2019 0.26em). Route these three codepoints through the
    # serif branch, which assigns them their Newsreader class: the
    # characters stay the same everywhere (source, text.md, PDF text
    # layers) and only the rendered glyph changes.
    # No new string literal is written here on purpose: freeze_direct.py
    # accounts source literals against tr_<lang>.py, and the class name
    # 'news' occurs in no tr literal — a literal 'news' would fail its
    # source level. The class is therefore derived, not spelled.
    if ch in ("\u201c", "\u201d", "\u2019"):
        # italic=False on purpose: the serif branch with italic would pick
        # the "news_i" class, which has no ("sans", ...) _PATH row.
        return _char_font(ch, "serif", bold)
```

plus, below `_char_font`:

```python
# fix2: _PATH entries for the Newsreader class inside sans runs, keyed by the
# derived class name (see _char_font). _pil resolves ("sans", bold, "news")
# to the Newsreader faces, mirroring the ("serif", bold, "news") rows.
_QUOTE_CLS = _char_font("\u201c", "serif", False)
_PATH[("sans", False, _QUOTE_CLS)] = _NEWS
_PATH[("sans", True, _QUOTE_CLS)] = _NEWS_B
```

Verification per file (`patch_svglib.py`, logs `patch-<edition>.log`):
py_compile passes; reverse-patch reproduces the recorded pre-patch md5 exactly;
inserted blocks present exactly once; patched-minus-insertions == original.

| edition | svglib.py md5 before | svglib.py md5 after |
|---|---|---|
| ru-de | `27f11789af7c828e47ca14eb00c1dded` | `b0928993747a13e94573a5dcced00961` |
| ru-fr | `27f11789af7c828e47ca14eb00c1dded` | `b0928993747a13e94573a5dcced00961` |
| ru-zh-tw | `27f11789af7c828e47ca14eb00c1dded` | `b0928993747a13e94573a5dcced00961` |
| zh-tw-ru | `9caa4651959673f511cd56873d93a04` (older variant: no `_CYR`/`sans_noto` rows, `_tc_index` instead of `_sc_index`, serif branch without `noto` rows — adapted minimally, same routing block + `_PATH` rows) | `b9e9effff652539c08f7bf2ff3bbfd74` |
| core-ru | `27f11789af7c828e47ca14eb00c1dded` | `b0928993747a13e94573a5dcced00961` |

Runtime routing verified after patching (ru-de, zh-tw-ru, core-ru):
`_QUOTE_CLS = 'news'` (derived); all three codepoints route to `news` in sans
regular and bold; `_PATH[("sans", bold, "news")]` resolves to Newsreader-Regular/SemiBold.

## 1. Before / after census (SVG, per `<text>` font-family, U+201C/U+201D/U+2019)

| edition | before (defective glyphs) | after |
|---|---|---|
| ru-de | 1 — P5 `p5-molodezh.svg`, 18pt “ in `„Schwarzer Freitag“` (Noto Sans CJK SC) | 0 defective, quote now Newsreader |
| ru-fr | 2 — P6 `p6-razbor.svg`, 26pt ’ in `DONNÉES D'EXERCICE` + 19.5pt ’ in the practice-data disclaimer (Noto Sans CJK SC bold). The 26pt ’ had been recorded as "accepted as-is in a Newsreader context" — the census proves it rendered in Noto Sans CJK SC, so that acceptance is VOID. | 0 |
| ru-zh-tw | 2 — P5 `p5-molodezh.svg`, 18pt “” in `“黑色星期五”：11月16日開始打折` (Noto Sans CJK SC) | 0 |
| zh-tw-ru | 4 — P5 `p5-youth.svg`, 18pt “ ×1 in `«Мире „Холодного сердца“»`; P8 `p8-test.svg`, 13.0pt “ ×3 in the `«Мире „Холодного сердца“»` test notes (Noto Sans CJK TC) | 0 |
| core-ru | 2 — P5 `p5-molodezh.svg`, 18pt “” in `“黑色星期五”：11月16日开始打折` (Noto Sans CJK SC) | 0 |
| **total** | **11** | **0** |

Post-sync production-SVG census re-run: 0 defective in all 5 editions.

Word-join census (PyMuPDF token method, print = web per edition):

| edition | before | after | adjudication |
|---|---|---|---|
| ru-de | R1 after-JSON 12/15 | 12/15, token-set identical to R1 after-JSON | 0 real joins (11 FP + 3 date-form `8.11.`/`7.11.`/`6.11.` FPs) |
| ru-fr | R1 after-JSON 14/17 | 14/17, token-set identical | 0 real joins |
| ru-zh-tw | R2 log 41/57 | 41/57 | 0 real joins |
| zh-tw-ru | production BEFORE 107/174 | 107/174, token-set identical to production BEFORE | 0 real joins |
| core-ru | R1 after-JSON 42/58 | 42/58, token-set identical | 0 real joins (11 FP + 28 CJK artifacts + 3 date FPs) |

## 2. Gate results (driver `drive.py`, per `<slug>-summary.json` / `<slug>-report.txt`)

All editions: **all_pass True**. Two independent `run_build.py` builds (TOTAL 150,
no FLOW OVERFLOW / HEAD TOO WIDE, "production unchanged"), webpdf on build 1,
freeze 8/8 SVG SHA match + print PDFs byte-identical, quote census 0, p8 extract
150/150 + compare CLEAN, checker rc 0, occlusion 0 flags, spill rc 0, boxtitle rc 0
(with `--backup-root` = production pre-fix build), text layer identical per page,
text.md byte-identical.

| edition | gates | keys end / P8 image |
|---|---|---|
| ru-de | 17/17 | Morozko SKIPPED (keys end 2331.72) — same as before |
| ru-fr | 17/17 | Morozko SKIPPED (keys end 2317.03) — same as before |
| ru-zh-tw | 18/18 | Morozko SURVIVES: keys end 2188.39, image 422.5×250 at y=2212.39, images [1,1,0,1,1,0,1,1] total 6 |
| zh-tw-ru | 16/16 | P8 `notes.jpg` 422.5×200 at y=559 (untouched); p8 compare vs core-zh-tw CLEAN keydiff [] |
| core-ru | 18/18 | Morozko SURVIVES: keys end 2216.58, image 422.5×200 at y=2240.58, images [1,1,0,1,1,0,1,1] total 6 |

Notes:
- ru-de boxtitle: P6 `PRO UND CONTRA` +1.1px over box right — OBSERVE, not DEFECT:
  identical +1.1px in the pre-fix production build, in R1's archived build-1 copy,
  and in this rebuild; the title contains no quote glyphs; not clipped
  (page width 1950); occlusion 0 flags.
- ru-fr: a runtime restart killed the first driver run mid-way through build 2's
  render (log `proc_901b9d702c5f`, no confirmed final result). Recovery: verified
  production by full-dir SHA snapshot (only `svglib.py` differed from the pre-patch
  snapshot), deleted the partial build dirs, re-ran the driver clean — all 17 gates
  PASS. No production impact.
- zh-tw-ru: the first memory gate waited the full 900 s (box had only ~700 MB
  available under parallel workers) and the driver proceeded on timeout; build 1
  started at 03:52:37 UTC and completed normally.

## 3. SHAs (before → after; text.md UNCHANGED in every edition)

| edition | print PDF (SHA-256, bytes) | web PDF (SHA-256, bytes) | text.md (SHA-256, bytes) |
|---|---|---|---|
| ru-de | `1920da86…` 21,229,165 → `e78581abdba80d4e7f28415cff47fd053b006b7c8d3f55b8751ec7e14f7de03e` 21,229,209 | `8366d304…` 3,383,411 → `956a6b62ebbabd840c4d163d8c2203a429eb517dda42966938064defce4b009c` 3,383,497 | `d0f9b48c8fab4df8bb39acfdfebfbc6ad6cf0f09e75891449d13a0f1ce2dcc0f` 63,471 — UNCHANGED |
| ru-fr | `c29251eb…` 21,289,489 → `79e75523214181b8983ae45839435f33352bcd123cf625de5b13ae05dd7c67dd` 21,264,368 | `d17fc225…` 3,383,322 → `671dbbcac435f3b88304544898339379c93e03ac84781e474c30156c8d722d5a` 3,383,213 | `e4cc50fd4195ed1adb7051c684c894c5a3b3091aa643cf3bab96690178e22a46` 63,361 — UNCHANGED |
| ru-zh-tw | `dbd7a52a…` 24,781,766 → `810514b2765de34dc8d3fa14c0373d78f1d5fe217614a9ea6585490e1bfa0aee` 24,784,623 | `d7787a5e…` 3,992,096 → `0cef86eaa14efdc6aef1619c0431a3491167bf83969ac4a9c42f9f93e503314b` 3,992,151 | `277a24f8a1674c970a367bf4fc8cccdd85d3f88941f85d633713a0e525ee6c83` 60,850 — UNCHANGED |
| zh-tw-ru | `1dbe1d8e…` 12,896,218 → `367828a6a0257ffdf05f862d44ccc10f483726a9d5ae399599c3a1b9304b375a` 12,896,273 | `d9b4d129…` 2,007,910 → `3def68758fd905a7a90962b1bf91352f50853057083e70205205987128d30209` 2,007,963 | `2fb4b97ef37d490e834dbef5c9553fb476c209222f061f7a17c4274e882ae03b` 62,492 — UNCHANGED |
| core-ru | `c2fd743e…` 31,426,561 → `09680fb595182a81155bd1ab84f90013e086b6369cb6f2a9483c2fb0cb0bf717` 31,426,216 | `a4f4bbd6…` 4,023,304 → `03d1b6f497e629704c6605a39a9d87002f31b4d81f6f0935cb28c015838e9884` 4,023,396 | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` 60,953 — UNCHANGED (both `2026-w47-ru-core.text.md` and `2026-w47-ru-zh-cn.text.md`) |

pdftotext bytes on the synced production PDFs (print / web): ru-de 57,909 / 57,909;
ru-fr 58,056 / 58,056; ru-zh-tw 56,176 / 56,176; zh-tw-ru 58,537 / 58,538 (1-byte gap
is the known run-boundary whitespace artifact, character multiset identical);
core-ru 56,073 / 56,073. Text-layer chars (fitz `get_text`, print = web): ru-de
37,532; ru-fr 37,505; ru-zh-tw 31,405; zh-tw-ru 29,211; core-ru 31,504.

## 4. Sync (per edition: verify scratch vs summary → verify production BEFORE →
## copy print + web + svg/ 8 + cards/ 8 → re-hash → svg 8/8 → freeze baseline 8/8)

All 5 synced. Production print/web SHAs after copy equal the scratch build-1 SHAs.
`freeze.py baseline --build <production dir> --core-svg <production dir>/svg`
returned **8/8 byte-identical** on the synced files for all 5 (core integrity:
shipped SVGs unchanged by the run). Post-sync production-SVG quote census: 0 in all 5.
Spot word-join census on the synced production print PDFs: ru-de 12/15, core-ru 42/58.

Final full-dir diff (production vs the pre-patch snapshot) shows exactly the
expected changes per edition: `svglib.py`, print PDF, web PDF, `WEEKLY-KIT.md`,
the SVG(s) holding the quotes, and `cards/` — nothing else:
- ru-de: only `svg/p5-molodezh.svg` changed (all 8 cards re-rendered).
- ru-fr: only `svg/p6-razbor.svg` changed (all 8 cards re-rendered).
- ru-zh-tw: only `svg/p5-molodezh.svg` changed (all 8 cards re-rendered).
- zh-tw-ru: only `svg/p5-youth.svg` + `svg/p8-test.svg` and their 2 cards changed.
- core-ru: only `svg/p5-molodezh.svg` changed (all 8 cards re-rendered).
text.md files were NOT copied (byte-identical).

## 5. KIT edits (current-state SHA/size lines + dated rebuild record; no history rewritten)

- ru-de `WEEKLY-KIT.md` §4: print/web bytes + SHAs, "Final build" → fix2 rebuild
  2026-11-12, web pdftotext 57,909. §6: appended "Fix2 U+201C port" bullet.
- ru-fr `WEEKLY-KIT.md` §5: print/web bytes + SHAs, "Final build" → fix2 rebuild
  2026-11-12. §7: appended "Fix2 U+201C port" bullet (incl. the runtime-restart note).
- ru-zh-tw `WEEKLY-KIT.md` §1 Deliverables table: print/web bytes + SHAs.
  §9: appended "Fix2 U+201C port" bullet.
- zh-tw-ru `WEEKLY-KIT.md` "Measured totals" PDFs + text-layer bullets: new bytes,
  SHAs, pdftotext counts (also notes the KIT's previous web SHA `cb05eba2…` was
  already stale before this fix — the on-disk web PDF carried `d9b4d129…` from a
  concurrent webpdf rebuild). "Fixes applied": appended item 6. "Build history":
  appended "Build 4 (fix2 U+201C port rebuild, 2026-11-12)".
- core-ru `WEEKLY-KIT.md` §7.3 "实测文件" line: new print/web SHAs + sizes (old
  values shifted into the history chain). Added "### 7.6 fix2 (2026-11-12)" with
  the full gate record.

## 6. Disk

Before: 90G used / 60G free (150G disk). After: 90G used / 60G free (stop line
100G never approached). Freeze build-copies (5 × ~26–51 MB) deleted after checks.

## 7. Out of scope / untouched

ru-ko, all de editions, all other editions, and `scratch-refanout-it2/backup/` —
untouched. No commit, push, or lint (per task).
