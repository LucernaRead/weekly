# D5 rebuild report — 2026-w43-nl-ru (Russian reader)

Date: 13 Nov 2026. Builder: W43 nl family builder (D5-only, no §1.1 — this edition was already new-style 11/11 at census). Status: **builder DONE, all 17 gates green after §4 fixes**. No commit, no push by the builder; independent re-proof (SOP §8) and the closer's commit are separate steps.

## 1. Install

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-ru/svglib.py --target nl --reader ru --week 2026-w43` (`--check` dry-run first, RC=0). Installed in the scratch `patched/` copy first; the verified file was then synced into `production/2026-w43/2026-w43-nl-ru/svglib.py` (byte-identical to the patched copy, verified by `cmp`).
- `_D5_READER = "ru"` (verified in the installed `svglib.py`). Routing unit test `test_d5_routing.py`: **FAILURES: 0**. D1 fix2 retained in the installed `svglib.py`.
- Patched `svglib.py` is md5-identical to production core-nl `svglib.py` except one pre-existing docstring line (L343: core `…for 重阳.` vs reader `…for the Double Ninth festival.`).

## 2. Baseline (pre-D5 rebuild, venv, disk-measured)

- `run.py`: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; 8 SVGs. `render.py` RC=0; `webpdf.py` RC=0 (web 1,039,668 B).
- Print `De-Lucerna-VOL1-RU.pdf` 10,329,408 B, sha256 `93a883a26fa18fcce9c26efe2675aa3b0a1d6750c0472e517a0ecb76cc922624` (pre-D5 build, superseded). Web `De-Lucerna-VOL1-RU-web.pdf` 1,039,668 B, sha256 `a4120a88620dbcc2b2cf0bd185d71307aec76e9fe17fed16f25f7c4cbad95792`.
- Text layer (pdftotext, Python `len()`, whitespace-stripped char multiset): print vs shipped web PDF = 0 AND web vs shipped = 0 (print chars == web chars; shipped chars slightly higher — whitespace/newline only, per D5-METHOD §3.7).
- `d5_census.py` pre-rebuild (RC=1 = FAIL as expected): **590 (328 Latin-in-CJK-sans + 262 Cyrillic-in-CJK-sans)** D5 elements. D1 fix present (`# D1 fix` 1/1); fix2 present in 0/11 editions before install (the installer adds it).
- Baseline judged clean in substance. The one exception was the print-PDF-vs-KIT-record leg: the KIT-recorded print/web figures predate the §1.1 style port (`e0922e8c`) and the D1 re-render (`e2a09702`, 2026-11-10) — the KITs were last touched at commit `756bc7c9` (initial add), and the D1 commit `5f6833d3` touched only `issues/`, never the KITs — so the KIT record is stale, not a baseline failure. (nl-en's KIT is internally inconsistent: two print sizes, 10,591,746 vs 10,591,681.) The web PDF +37 KB vs shipped is likewise explained: the shipped PDF was built 2026-11-09 with the old `webpdf.py`; the current tool (commit `40963281`, 2026-11-11, "webpdf weight + italic face resolution") adds Newsreader-Bold ×8 + Italic ×1 (37 font rows vs shipped 29); text/images identical, font families identical. Proceeded past the KIT-record leg with this adjudication recorded; content legs fully green.

## 3. Defects and fixes (§4 — size and line-break only; text unchanged)

Run 1 gates: G2 head_check PASS; G12 boxtitle FAIL (1 item, boxtitle-only); G14 creambox PASS; G6 occlusion PASS; all other gates green. Fix sizes were computed by `measure_fixes.py` (each edition's own patched `svglib.py` `text_w`, 2 px safety margin: largest integer size with `text_w ≤ avail − 2`, where `avail = text_w(current) − over`) and applied by `apply_fixes.py` to `patched/` only, each fix asserted before writing.

- Feature heads `ETEN BESTELLEN WORDT HELDER` (P2) / `EROPUIT IN DE HERFSTVAKANTIE` (P3) already fit at 25 pt (ru mode routes Dutch heads to Noto Sans, narrower than Newsreader; advance 406.7/407.7 px vs column 422.5 px) — no change; head_check passed in run 1. (ru is the only nl edition with 0 HEAD TOO WIDE after install.)
- P1: p.text `IN DEZE EDITIE　В ЭТОМ НОМЕРЕ` — over +1.6 px (right) → size 24 → 23 (`content12.py:91`).
- Exporter note: the `IN DEZE EDITIE …` panel heading shrank 24 → 23 pt, crossing the exporter's ≥24 pt heading heuristic, so the scratch exporter (`export_text_w43nl.py`) gained an explicit heading rule for it (same pattern as the P3b italic-serif fix). The re-export is still byte-identical to the shipped `.text.md`.
- Note: the single defect (+1.6 px) is boxtitle-only — below the creambox tolerance, hence creambox passed in run 1 while boxtitle failed.
- P8: **244 → 244 lines, slack to footer rule 36.5 → 36.5 px** (unchanged by §4; `content8.py` identical pre/post fix, verified by diff).
- After fixes: full rebuild (`run.py` → `render.py` → `webpdf.py` → export) — run RC=0, TOTAL 150, O=0, **H=0**; webpdf RC=0; text.md BYTE-IDENTICAL 11/11 family-wide.

## 4. Gates (full re-run after fixes, run 2)

**ALL-GREEN.** Every gate RC=0: run TOTAL 150 / head_check 0 / d5 census 0 / render RC=0 / webpdf RC=0, web < 7 MB / occlusion 0 flags / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff vs baseline added CJK 0 / spill 0 SPILL / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects / text layer print=web multiset 0, text.md BYTE-IDENTICAL / census_quotes 0 defective / gates.py N/A (nl family has no `gates.py`).

- Spill: 0 SPILL (57 OBSERVE). Freeze diff vs baseline: added CJK 0 (added Latin strings = run-splitting, not regression, per D5-METHOD §3.2 #5). Print chars == web chars: 97,331. Census TOTAL 0 (noto_sans_elements=777).

Master table (`GATES-SUMMARY.txt`, run 2):

```
=== 2026-w43-nl-ru gates 2026-11-13T20:07:04Z ===
G1 run: TOTAL 150 OVERFLOW=0 HEADWIDE=0
G2 head_check RC=0 : HEAD CHECK PASS 0 defects 
G3 d5_census RC=0 : TOTAL: D5_latin_in_cjk=0 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0 curly_in_newsreader=0 noto_sans_elements=777 
G4 render: print_pdf=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ru/De-Lucerna-VOL1-RU.pdf bytes=9966645
G5 webpdf: 2026-w43-nl-ru.web.pdf bytes=1157010 (<7000000: YES)
G6 occlusion RC=0 : selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ru/svg: 0 flags  
G7 p8_extract RC=0 : /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ru/svg/p8-toets.svg: noted set = 150 of 150 (parse: lines)   set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150] 
G8 p8_compare RC=0 : edition /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ru/svg/p8-toets.svg: 150 noted status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138] 
G9 freeze_baseline RC=0 :   OK  p7-taal.svg core 0e26901725132f87 produced 0e26901725132f87   OK  p8-toets.svg core 286aebb859914d6f produced 286aebb859914d6f core integrity: shipped core SVGs unchanged by the run (8 files re-hashed) 
G10 freeze_diff RC=0 : p8: +44 strings / -13 strings; CJK core 15 -> edition 15; added CJK chars: 0 ; added Latin strings: 21 (unexpected 21) TOTAL added CJK characters: 0 TOTAL added Latin strings: 172 (unexpected 172) 
G11 spill RC=0 :    ABOVE -30.45px x=1461.5 y=1359.0 [observe] 'в лес, на фестиваль.' SPILL_SWEEP 2026-w43-nl-ru: 26 boxes, 57 candidates, 0 SPILL, 57 OBSERVE 
G12 boxtitle RC=0 : == 2026-w43-nl-ru  core=None backup=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/scratch-fanout-nl/backup/2026-w43-nl-ru BOXTITLE 2026-w43-nl-ru: 26 titles, 273 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal 
G13 edge RC=0 :   P8: clean min_dist_pt={'top': 54.0, 'bottom': 53.6, 'left': 65.9, 'right': 65.5} EDGE_SCAN 2026-w43-nl-ru: 8 pages, 0 TOUCH, 0 NEAR 
G14 creambox RC=0 : ratios: n=408 median=0.997 boldT=0.956 boldF=1.031 P8 p8-toets.svg: lines 244->244 slack_footer 36.5->36.5 CREAMBOX PASS 0 defects 
G15 textlayer RC=0 : 2026-w43-nl-ru print_chars=97331 web_chars=97331 print_vs_web_multiset=0 textmd_byte_identical=True 
G16 census_quotes RC=0 :   TOTAL defective: 0 GRAND TOTAL defective: 0 
G17 gates.py: N/A (no gates.py in nl family)
=== end 2026-w43-nl-ru ===
```

Gate logs: `logs/2026-w43-nl-ru/` (this directory). Selftests run once, all OK: `occlusion_audit.py --selftest` (6 classes fired), `d5_creambox_audit.py --selftest` (widened title → 1 defect; identical → 0; old-style fallback → 0), `head_check.py --selftest` (dirty log → 2 findings; clean → 0). Boxtitle backup note: `find_backup` requires the backup dir to contain `svg/`; the baseline SVGs were copied into `scratch-fanout-nl/backup/<slug>/svg` (8 files) before run 1 — even so, each boxtitle defect line read `backup=None` (per-item baseline lookup finds no matching baseline element; D5 changed run structure), so boxtitle effectively reports absolute overflow, agreeing 1:1 with creambox except the boxtitle-only items noted above.

## 5. New deliverables and KIT

- Print `De-Lucerna-VOL1-RU.pdf`: **9,966,645 B**, sha256 `fa92236d04aa207cb6767c6c154800bb630ed898a2dcc306bed869d955cfeaeb` (md5 `5fdedf7cc7de42d06d98c64267950726`). Old (pre-D5 build): 10,329,408 B, sha256 `93a883a26fa18fcce9c26efe2675aa3b0a1d6750c0472e517a0ecb76cc922624`.
- Web `De-Lucerna-VOL1-RU-web.pdf`: **3,391,548 B**, sha256 `c374f1f5bea5ef7022ce349b2a5486e7b645485c0a72f528b71854a7f3dc9f4c` (md5 `66c211e4713fd12ff4d801f0f5a2bc01`), < 10 MB. Old: 1,039,668 B, sha256 `a4120a88620dbcc2b2cf0bd185d71307aec76e9fe17fed16f25f7c4cbad95792`.
- Text-layer web `2026-w43-nl-ru.web.pdf`: **1,157,010 B**, sha256 `8474f4cf780a53330734fee99fc7d058763a6a2f600b9ce0a91127e1a3816a4f`, < 7 MB.
- `2026-w43-nl-ru.text.md`: **49,288 B**, sha256 `9e8a4e6e30210abffdf5137a69084e32ca895b8c3981935f86df4789130a7096`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-ru/2026-w43-nl-ru.text.md`. Exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py` (W46 generic AST exporter + W43-nl italic-serif fix for the P1 `«de klok verzetten»` line + `IN DEZE EDITIE` heading fix); verified 11/11 byte-identical family-wide before the rebuild, and again after the §4 fixes.
- KIT: `production/2026-w43/2026-w43-nl-ru/WEEKLY-KIT.md` — pinned print/web lines updated in place to the new values above, and a `## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)` section appended (install / baseline / defects+fixes / gates / new SHAs). Historical fix/verification lines keep their old numbers as history; the D5 section records the supersession.
- Changed source files (production, uncommitted — closer to commit): `svglib.py` + the §4-fixed content files (see family report for the full list). No PDFs/SVGs/text.md/logs/cards/assets were written into `production/` (repo AGENTS.md: content only).

