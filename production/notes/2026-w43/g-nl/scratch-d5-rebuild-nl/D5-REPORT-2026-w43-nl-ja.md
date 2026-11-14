# D5 rebuild report — 2026-w43-nl-ja (Japanese reader)

Date: 13 Nov 2026. Builder: W43 nl family builder (D5-only, no §1.1 — this edition was already new-style 11/11 at census). Status: **builder DONE, all 17 gates green after §4 fixes**. No commit, no push by the builder; independent re-proof (SOP §8) and the closer's commit are separate steps.

## 1. Install

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-ja/svglib.py --target nl --reader cjk --week 2026-w43` (`--check` dry-run first, RC=0). Installed in the scratch `patched/` copy first; the verified file was then synced into `production/2026-w43/2026-w43-nl-ja/svglib.py` (byte-identical to the patched copy, verified by `cmp`).
- `_D5_READER = "cjk"` (verified in the installed `svglib.py`). Routing unit test `test_d5_routing.py`: **FAILURES: 0**. D1 fix2 retained in the installed `svglib.py`.
- CJK install notes: CJK index SC → JP; kinsoku already present in the shipped `svglib.py` (port skipped).

## 2. Baseline (pre-D5 rebuild, venv, disk-measured)

- `run.py`: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; 8 SVGs. `render.py` RC=0; `webpdf.py` RC=0 (web 1,554,398 B).
- Print `De-Lucerna-VOL1-JA.pdf` 22,776,469 B, sha256 `64ae450a5c7aa1e491fbf67183e7b2bb483227c68a8912aa30684f4bc154a14b` (pre-D5 build, superseded). Web `De-Lucerna-VOL1-JA-web.pdf` 1,554,398 B, sha256 `b15f281f6de0bf14341e731c756c213bee8fd0edf60ebfeee1d822c427dbb821`.
- Text layer (pdftotext, Python `len()`, whitespace-stripped char multiset): print vs shipped web PDF = 0 AND web vs shipped = 0 (print chars == web chars; shipped chars slightly higher — whitespace/newline only, per D5-METHOD §3.7).
- `d5_census.py` pre-rebuild (RC=1 = FAIL as expected): **325** D5 elements. D1 fix present (`# D1 fix` 1/1); fix2 present in 0/11 editions before install (the installer adds it).
- Baseline judged clean in substance. The one exception was the print-PDF-vs-KIT-record leg: the KIT-recorded print/web figures predate the §1.1 style port (`e0922e8c`) and the D1 re-render (`e2a09702`, 2026-11-10) — the KITs were last touched at commit `756bc7c9` (initial add), and the D1 commit `5f6833d3` touched only `issues/`, never the KITs — so the KIT record is stale, not a baseline failure. (nl-en's KIT is internally inconsistent: two print sizes, 10,591,746 vs 10,591,681.) The web PDF +37 KB vs shipped is likewise explained: the shipped PDF was built 2026-11-09 with the old `webpdf.py`; the current tool (commit `40963281`, 2026-11-11, "webpdf weight + italic face resolution") adds Newsreader-Bold ×8 + Italic ×1 (37 font rows vs shipped 29); text/images identical, font families identical. Proceeded past the KIT-record leg with this adjudication recorded; content legs fully green.

## 3. Defects and fixes (§4 — size and line-break only; text unchanged)

Run 1 gates: G2 head_check FAIL (2 heads); G12 boxtitle FAIL (2 items); G14 creambox FAIL (2 items); G6 occlusion FAIL (1 flag: TEXTX); all other gates green. Fix sizes were computed by `measure_fixes.py` (each edition's own patched `svglib.py` `text_w`, 2 px safety margin: largest integer size with `text_w ≤ avail − 2`, where `avail = text_w(current) − over`) and applied by `apply_fixes.py` to `patched/` only, each fix asserted before writing.

- Feature heads `ETEN BESTELLEN WORDT HELDER` (P2) / `EROPUIT IN DE HERFSTVAKANTIE` (P3), both `f.head(..., 25)` (`content12.py` P2 head, `content34.py:20`): HEAD TOO WIDE at 25 pt (advance 472.2/466.0 px vs column 422.5 px) → head size **25 → 22** in both files.
- P1: box title `DE WEEK IN CIJFERS　数字で見る今週` — over +38.2 px (right) → f.box tsize 23 → 20 (`content12.py:48`).
- P6: p.text `AFSCHAFFEN OF NIET?　廃止か継続か` — over +11.6 px (right) → size 21 → 20 (`content56.py:166`).
- Occlusion TEXTX: P1 `数字で見る今週` title ink overlapped `De Dutch Design Week is in ___.` by 10.2×13.0 px — resolved by the P1 box-title fix above. (ja baseline was clean: 0 flags; the TEXTX appeared only after D5.)
- P8: **212 → 212 lines, slack to footer rule 56.4 → 56.4 px** (unchanged by §4; `content8.py` identical pre/post fix, verified by diff).
- After fixes: full rebuild (`run.py` → `render.py` → `webpdf.py` → export) — run RC=0, TOTAL 150, O=0, **H=0**; webpdf RC=0; text.md BYTE-IDENTICAL 11/11 family-wide.

## 4. Gates (full re-run after fixes, run 2)

**ALL-GREEN.** Every gate RC=0: run TOTAL 150 / head_check 0 / d5 census 0 / render RC=0 / webpdf RC=0, web < 7 MB / occlusion 0 flags / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff vs baseline added CJK 0 / spill 0 SPILL / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects / text layer print=web multiset 0, text.md BYTE-IDENTICAL / census_quotes 0 defective / gates.py N/A (nl family has no `gates.py`).

- Spill: 0 SPILL (81 OBSERVE). Freeze diff vs baseline: added CJK 0 (added Latin strings = run-splitting, not regression, per D5-METHOD §3.2 #5). Print chars == web chars: 89,266. Census TOTAL 0.

Master table (`GATES-SUMMARY.txt`, run 2):

```
=== 2026-w43-nl-ja gates 2026-11-13T20:02:03Z ===
G1 run: TOTAL 150 OVERFLOW=0 HEADWIDE=0
G2 head_check RC=0 : HEAD CHECK PASS 0 defects 
G3 d5_census RC=0 : TOTAL: D5_latin_in_cjk=0 D5_cyrillic_in_cjk=0 curly_in_cjk=0 curly_total=0 curly_in_newsreader=0 noto_sans_elements=0 
G4 render: print_pdf=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ja/De-Lucerna-VOL1-JA.pdf bytes=17268607
G5 webpdf: 2026-w43-nl-ja.web.pdf bytes=1372523 (<7000000: YES)
G6 occlusion RC=0 : selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ja/svg: 0 flags  
G7 p8_extract RC=0 : /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ja/svg/p8-toets.svg: noted set = 150 of 150 (parse: lines)   set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150] 
G8 p8_compare RC=0 : edition /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/patched/2026-w43-nl-ja/svg/p8-toets.svg: 150 noted status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138] 
G9 freeze_baseline RC=0 :   OK  p7-taal.svg core c49fbc94e9ae83a9 produced c49fbc94e9ae83a9   OK  p8-toets.svg core cb1163f02bb15b8e produced cb1163f02bb15b8e core integrity: shipped core SVGs unchanged by the run (8 files re-hashed) 
G10 freeze_diff RC=0 : p8: +80 strings / -23 strings; CJK core 1359 -> edition 1359; added CJK chars: 0 ; added Latin strings: 21 (unexpected 21) TOTAL added CJK characters: 0 TOTAL added Latin strings: 217 (unexpected 217) 
G11 spill RC=0 :    ABOVE -30.45px x=1461.5 y=1329.5 [observe] 'などへ出かけること。' SPILL_SWEEP 2026-w43-nl-ja: 26 boxes, 81 candidates, 0 SPILL, 81 OBSERVE 
G12 boxtitle RC=0 : == 2026-w43-nl-ja  core=None backup=/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w43-nl/scratch-fanout-nl/backup/2026-w43-nl-ja BOXTITLE 2026-w43-nl-ja: 25 titles, 319 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal 
G13 edge RC=0 :   P8: clean min_dist_pt={'top': 54.0, 'bottom': 55.8, 'left': 65.9, 'right': 65.5} EDGE_SCAN 2026-w43-nl-ja: 8 pages, 0 TOUCH, 0 NEAR 
G14 creambox RC=0 : ratios: n=386 median=1.04 boldT=1.05 boldF=1.0 P8 p8-toets.svg: lines 212->212 slack_footer 56.4->56.4 CREAMBOX PASS 0 defects 
G15 textlayer RC=0 : 2026-w43-nl-ja print_chars=89266 web_chars=89266 print_vs_web_multiset=0 textmd_byte_identical=True 
G16 census_quotes RC=0 :   TOTAL defective: 0 GRAND TOTAL defective: 0 
G17 gates.py: N/A (no gates.py in nl family)
=== end 2026-w43-nl-ja ===
```

Gate logs: `logs/2026-w43-nl-ja/` (this directory). Selftests run once, all OK: `occlusion_audit.py --selftest` (6 classes fired), `d5_creambox_audit.py --selftest` (widened title → 1 defect; identical → 0; old-style fallback → 0), `head_check.py --selftest` (dirty log → 2 findings; clean → 0). Boxtitle backup note: `find_backup` requires the backup dir to contain `svg/`; the baseline SVGs were copied into `scratch-fanout-nl/backup/<slug>/svg` (8 files) before run 1 — even so, each boxtitle defect line read `backup=None` (per-item baseline lookup finds no matching baseline element; D5 changed run structure), so boxtitle effectively reports absolute overflow, agreeing 1:1 with creambox except the boxtitle-only items noted above.

## 5. New deliverables and KIT

- Print `De-Lucerna-VOL1-JA.pdf`: **17,268,607 B**, sha256 `f0e5545b6162fc03a44c42d4abea1c7a58a30395831fedf9c72ec9f10a9d8d27` (md5 `042536188daed413955d5b4fad209125`). Old (pre-D5 build): 22,776,469 B, sha256 `64ae450a5c7aa1e491fbf67183e7b2bb483227c68a8912aa30684f4bc154a14b`.
- Web `De-Lucerna-VOL1-JA-web.pdf`: **3,247,158 B**, sha256 `205b8050a49ba6dd3b90f655002bccba33c0ecb077ca758872917d92055936c9` (md5 `5ed2b418adf02039f12da06f13d089e2`), < 10 MB. Old: 1,554,398 B, sha256 `b15f281f6de0bf14341e731c756c213bee8fd0edf60ebfeee1d822c427dbb821`.
- Text-layer web `2026-w43-nl-ja.web.pdf`: **1,372,523 B**, sha256 `025369496dc148f21b99202c492cc0a1655f84946e14f4cfd46ef126b6f5fcd4`, < 7 MB.
- `2026-w43-nl-ja.text.md`: **40,337 B**, sha256 `1c302aaeb0ecc17fa1edef11dcb5d267ac584a025b33f4a170be3a8e83fe5fc5`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-ja/2026-w43-nl-ja.text.md`. Exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py` (W46 generic AST exporter + W43-nl italic-serif fix for the P1 `«de klok verzetten»` line + `IN DEZE EDITIE` heading fix); verified 11/11 byte-identical family-wide before the rebuild, and again after the §4 fixes.
- KIT: `production/2026-w43/2026-w43-nl-ja/WEEKLY-KIT.md` — pinned print/web lines updated in place to the new values above, and a `## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)` section appended (install / baseline / defects+fixes / gates / new SHAs). Historical fix/verification lines keep their old numbers as history; the D5 section records the supersession.
- Changed source files (production, uncommitted — closer to commit): `svglib.py` + the §4-fixed content files (see family report for the full list). No PDFs/SVGs/text.md/logs/cards/assets were written into `production/` (repo AGENTS.md: content only).

