# GATE LOG — 2026-W47 ru-en, re-fanout re-proofread (2026-11-11)

Proofer scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-en2/`
Edition: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`
Core: `~/workspace/weekly-git/production/2026-w47/core-ru/` (fix1 `f11854bf`)
Tools: `~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0); canonical
`tools/` (`p8.py`, `freeze.py`, `occlusion_audit.py`); canonical
`hidden_files/w47/tools/creambox.py`; `scratch-fanout-ru/s11_check.py`;
`scratch-fanout-ru/adjudicate_ru.py`. TMPDIR = scratch `tmp/`.
Startup probes: `git hash-object -w` probe OK (`72117c5e…`); real-write probe
in scratch OK. `/dev/null` present (char device, no touch needed).

## 0. Identity (measured by me at start AND end — unchanged)

| File | Bytes | SHA-256 | Expected | Result |
|---|---|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,251,190 | `b244c56b7575f425e52902f19823f740d46cdafea2afcb1b86cdde24df863406` | same | MATCH, 8 pages |
| `Lucerna-VOL4-ru-en-web.pdf` (web) | 3,380,786 | `d306b3f365c5b4a04022f2a900faee904eb3f838c2f530fe5b4ce667c62d14a9` | same | MATCH, 8 pages, < 7 MB |
| `2026-w47-ru-en.text.md` | 62,829 | `1e06ec55e8ba694224e244e37d81e6bfdfc3c3299e6aeb925308fd08e0b0e2ea` | same | MATCH, 838 lines, 150 ex., 277 blocks |
| core `Lucerna-VOL4.pdf` | 31,429,147 | `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` | same | MATCH |
| core `Lucerna-VOL4-web.pdf` | 4,025,834 | `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` | same | MATCH |
| core `2026-w47-ru-core.text.md` | 60,953 | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` | same | MATCH |

`git status` on `production/2026-w47/2026-w47-ru-en/` + `core-ru/`:
untracked (`??`, never committed) with no modifications; all SHAs above
re-verified after every tool run. No production file edited, no commit, no push.
(Other `production/2026-w47/` modifications in `git status` belong to concurrent
agents on other editions, not this proofread.)

## 1. Full read

- 8 pages re-rendered from SVG by me (CairoSVG via tools venv, 975×1350,
  `fresh/p1..p8.png`) and read page by page; web P1/P5/P8 crops read.
  Result: no overflow/overlap/clipping/missing content except S1 (PROOF-NOTE).
- `2026-w47-ru-en.text.md` read in full (838 lines); all 150 stems/options/keys
  hand-checked against article text; stem keys vs answer-list keys 0 mismatches
  (1–149); model text 97 words. `gates/final-checks2.log`.
- `print.txt` (pdftotext -layout) read in support of the visual read.

## 2. run.py / rerun reproducibility — PASS

Copied edition dir to scratch `rerun/` (no production writes) and ran `run.py`:
rc=0, TOTAL 150, by level A2 50 / B1 76 / B2 24, by page
10/18/18/18/18/18/12/38, 0 FLOW OVERFLOW / HEAD TOO WIDE lines
(`gates/rerun.log`). All 8 rebuilt SVGs byte-identical to shipped
(SHA list in the rerun exec output). Registry dumped (`rerun/registry.json`,
150 entries).

## 3. check_core.py — PASS (rc=0)

`gates/check-core.log`: golden BAD 0, gloss fails 0, P8 SVG text 10,561 chars;
1 orphan line-start (P7 y553 `”».`, known benign) + 1 same-baseline collision
(P1 y1712 `чёрная`, known, same as core).

## 4. p8.py extract + compare — PASS

- extract: noted set = 150 of 150 (`gates/p8-extract.json`, rc=0).
- compare vs core P8 SVG: status CLEAN, missing=[], extra_count=0,
  keydiff=[137, 138, 139, 140] (`gates/p8-compare.json`, rc=0).
- direct keydiff vs core `ru-p8.json` (150 keys): exactly
  [137, 138, 139, 140] (`gates/keycheck.log`).

## 5. keycheck (registry vs P8 extract) — PASS as expected (149/150)

Registry (dumped from the scratch rerun build) vs P8 extract: 149/150 match;
only [150] differs (registry key `(Open task; model text below)`, P8 prints
✓ — expected for the open writing task). Q137 registry key
`Tuesday 17 November, Students' Day.` matches the extract (no em-dash
truncation in this build). Q150 ✓. (`gates/keycheck.log`)

## 6. freeze.py — PASS

- Standard baseline (`--build core-ru --core-svg core-ru/svg`): rc=0,
  **8/8 SVGs byte-identical**; core integrity: shipped core SVGs unchanged.
  (`gates/freeze-std.log`)
- Edition-internal baseline (`--build <edition> --core-svg <edition>/svg`,
  supplementary): rc=0, **8/8**. (`gates/freeze-int.log`)
- diff (`--core-svg core-ru/svg --edition-svg <edition>/svg`): rc=0,
  removed distinct 484 / count-sum 850; added CJK total 8, all U+3000
  (1 per page). (`gates/freeze-diff.json`, `gates/freeze-diff.log`)
- Cyrillic-bearing removed: exactly **15** = Q46 `можно` ×1 + 14 Morozko
  caption words (Билибин/Билибина/Зимняя/Иван/Ивана/Иллюстрация/Морозко/год/
  достояние/иллюстрация/к/ноябрю/общественное/сказка), all in core P8
  y≥2450 caption block; **unexplained 0**; Morozko image absent from edition
  P8 by design; added Cyrillic-bearing strings 0.
  (`gates/freeze-adjudicate.log`)

## 7. occlusion_audit.py — PASS (42 TEXTX, adjudicated 42/42 CLEAR)

Real run, NO `--selftest` (per brief): `occlusion_audit.py <edition>/svg
--json gates/occlusion.json`, rc=1 (by-design "flags present" signal).
42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE.
Adjudication (`adjudicate_ru.py`): `Counter({'CLEAR': 42})`, rc=0.
Flag set identical to proof1/proof3 except one P6 run re-segmented by the D1
change (`?　PRACTICE DATA` → `?　`, same line). (`gates/occlusion.log`,
`gates/occlusion-compare.log`, `gates/adjudication.log`)

## 8. creambox.py (canonical) — PASS

Full 8-page scan, rc=0 (`gates/creambox.log`): no negative inside-only
clearance; 95 BELOW-WINDOW lines, all classified (offsets +28 ×25, +32 ×41,
+34 ×4, +37 ×25 — next-block titles, P2 weather-word boxes, P6 day-strip
legend, P1 quick-quiz header pointer). Scan byte-identical to the backup-old
scan (normalized path diff: 0 content lines, `gates/creambox-analysis.log`).
P2 А ВЫ box desc-clear −1.0 is pre-existing (same in backup scan).

## 9. Spill sweep (new, my script `spill.py`) — 1 FLAG = DEFECT S1

- 32 cream (#f0eee5) boxes; every contained run true-ink measured
  (PIL, `occlusion_audit.ink_box`): exactly **1 ink-escape** — P1
  `　The round in numbers`, ink right 998.9 vs box right 961.0 (+37.9 px).
- 32 box titles true-ink measured (horizontal + vertical): **0** with negative
  right/bottom clearance.
- 43 spill-below candidates: all in the already-classified by-design set
  (same lines as creambox BELOW-WINDOW).
- 199 unbordered filled rects (no stroke) scanned as part of the run.
  (`gates/spill.log`, `gates/spill-p1.log`, `crops/p1-roundnumbers*.png`)

## 10. Print/web text layer — PASS

- pdftotext -layout: 111,886 bytes each, byte-identical (`cmp` clean).
- plain pdftotext: 57,329 bytes each, byte-identical.
- fitz multiset: identical overall (30,363 non-whitespace chars) and per page
  (verify_mine2, `gates/verify-mine2.log`).
- span-text multisets identical all 8 pages; abutting span-pair gap diffs
  max 0.00 pt; intra-span char-pair gap diffs max 0.00 pt.
- Web PDF NOT re-rendered onto production files (only scratch renders/crops).

## 11. check_s11.py (s11_check.py) + verify_ed — PASS (with one note)

- `s11_check.py <edition>`: rc=0, **FAILURES: none**; 8 SVG; paper #fbfaf6;
  no #f7f1e2/#c9a227/#8b4513/#000000; badges A2/B1/B2; foot VOL.4 +
  full-width space; VOL.3 only in P4 correction (×1); masthead 196 px;
  band title 46 px; left margin ≥ 87 (88.0); no CJK in visible SVG (Latin
  reader); both PDFs 8 pages; web < 7 MB; web text > 0;
  **P8 min font ≥ 9.75 pt: 9.75**. (`gates/s11.log`)
- `verify_ed.py`: no ru-family `verify_ed.py` exists in the program (searched
  `scratch-fanout-ru/`, `scratch-proof-ru-en*`, `scratch-ru-en-proof2` — the
  only edition verifiers there are the en-family `verify_ed.py` (Ashes/Q39
  specific, not applicable) and proof3's `verify3.py`). I therefore ran my own
  fresh independent print/web verification (`verify_mine2.py`, same checks as
  the en-family verifier's class: multiset, span diffs, abutting/intra-char
  gap scans, pinned D1/D2/D3 spots): **all PASS** after correcting one finder
  bug in my own script (v1 D3 space check looked for consecutive `я`,`п`
  chars and missed the space char between them; corrected measurement:
  space bbox byte-identical [1145.576, 1266.762, 1148.108, 1288.725],
  width 2.532 pt, gap diff 0.00). v1 was killed as too slow (O(n²) rescans);
  v2 (precomputed caches) completed in ~36 s. (`gates/verify-mine2.log`,
  `verify_mine2.py`)

## 12. D1 / D2 / D6 / kicker — PASS

- D1: segments in text.md L459/504/596; all 4 KEEP values in SVG
  (concatenated-`<text>` check); disclaimer SVG-only.
  (`gates/d1d2d6-kicker.log`, `gates/d1-svg.log`)
- D2: full phrase `Международный день студента` ×2 text.md = core ×2;
  Q25 option `День студента` (L187); 7 D2 spots re-pinned, diff 0.000 pt.
- D6: `желании` ×2 text.md = core ×2; P8 extract key 20 = `желании` =
  core `ru-p8.json:177`.
- Kicker: 9 gaps [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6], min 5.9 ≥ 4;
  P1 row element-identical to core. (`gates/kicker.log`)
- `___` literals: 87 in text.md = 87 in core text.md (template matter, not
  an edition defect per brief).

## 13. SVG CJK scan — PASS

Visible `<text>` per page (ElementTree, `<title>` metadata excluded):
real CJK chars 0 on all 8 pages; U+3000 counts 21/16/13/16/13/16/13/15
(total 123; freeze-diff added-CJK accounting is U+3000 ×8 net vs core).
(`gates/d1d2d6-kicker.log`)

## 14. D5 fonts — RECORDED ONLY (not judged)

`gates/fonts-print.log`, `gates/fonts-web.log` (pdffonts): print embeds
NotoSans(CJK sc)/NotoSans/NotoSerif/UnifrakturMaguntia/Newsreader16pt
(+ NotoSerifCJKsc), all emb/sub/uni; web embeds Lucerna*-renamed subsets
incl. `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic` (D3 italic
present). Font entries: 72 print / 72 web (11 distinct base names print,
12 web).

## 15. Regression vs backup-old (#1 voided build) — PASS (KEEP/REVERT盤點)

`diff -r --exclude=__pycache__ --exclude=cards backup-old/2026-w47-ru-en
production/2026-w47/2026-w47-ru-en/` (`gates/regression-diff.log`):
- text.md: exactly **6 line pairs** (L173 D6 key, L187 D2, L459/504/596 D1,
  L694 D6 key list), nothing else.
- Sources changed only: content12.py (kicker double-space + D6 key + D2
  option + fix comments), content56.py (D1 title + disclaimer),
  content7.py (D1 P7 subtitle), content8.py (D1 P8 subtitle),
  WEEKLY-KIT.md (§5/§7 updates).
- SVGs changed only: p1 (kicker), p2 (D2 option), p6/p7/p8 (D1 + D6 key).
- KEEP: proof1 D1 straight-quote fix survives (p5 SVG unchanged vs backup;
  re-measured 0.0 pt gap); proof2 D3 italic fix survives (re-measured above).
  No hand patch lost; no unexplained change. The P1 S1 overhang is identical
  in backup-old (pre-existing, missed by earlier rounds — this sweep is the
  first to check unbordered cream boxes with true ink).

## 16. ABSTRACT.txt — PASS

355 bytes, one English line, no ASCII double quotes; VOL.4 + A2–B2 +
150 exercises + real topics (round 14, Zenit/Dynamo 31 pts, Uzbekistan 12 Nov,
Venezuela 17 Nov, Black Friday, five premieres 19 Nov, Students' Day,
Ded Moroz's birthday). (`gates/final-checks.log`)

## Conclusion

Gates 1–8, 10–16 all pass. Gate 9 (spill sweep) flags exactly one defect,
S1 (PROOF-NOTE), minor, front page, both PDFs. Verdict (b): defects found,
cannot finalize until S1 is fixed and re-proofread.
