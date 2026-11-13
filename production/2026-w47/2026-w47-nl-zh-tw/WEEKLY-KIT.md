# WEEKLY-KIT — 2026-W47 · nl → zh-tw (Traditional Chinese readers)

Dutch weekly newspaper for Traditional Chinese readers. Target language Dutch
(nl), reader native language Traditional Chinese (zh-tw). VOL.4, issue
2026-11-16 – 2026-11-22. Target: 150 exercises (10/18/18/18/18/18/12/38
across pages 1–8); A2 46 / B1 73 / B2 31; model essay 81 words.

## Source

Fan-out of the frozen Dutch core `production/2026-w47/core-nl/` (slug
`2026-w47-nl-zh-cn`). Dutch target text, facts, and answer keys are frozen; only
the explanation layer (glosses, notes, section subtitles, exercise type words)
was rewritten in Traditional Chinese. Simplified and Traditional Chinese are
INDEPENDENT editions — no conversion. No new trend research, no invented
reader letters.

## Files delivered

- 8 SVGs (`svg/p1-voorpagina.svg` … `svg/p8-toets.svg`), 8 render cards (`cards/`)
- Print PDF: `De-Lucerna-VOL4-nl-zh-tw.pdf` — 13,887,537 bytes,
  sha256 `3fd293bfef564ea277f4f96495710f7391ad5204da659bdd43dc2ce3edfde693`
  (D5 rebuild 2026-11-12; build 3 was 25,993,186 bytes,
  sha256 `6de893ca2811357c7be524b2b17e78af1c5362abc647e957d8665559466c704a`;
  build 2 was 25,993,150 bytes,
  sha256 `3a81e9cf00ff56378f692af8e951a4d306d0c68eae113332c8bede67d477eb9b`)
- Web PDF: `De-Lucerna-VOL4-nl-zh-tw-web.pdf` — 1,976,266 bytes,
  sha256 `542c6f1bc8e2f71b0cdf558e169dca3d1738e981919433c63182a304a44754ec`
  (D5 rebuild 2026-11-12; build 3 was 2,369,230 bytes,
  sha256 `172c1be81d32d871c323064c685e0918e41b12b29a25a19a50cf4926d217ff20`;
  build 2 was 2,369,193 bytes,
  sha256 `aedb0d6e80fdb95f3279dea8523b09e2130309f82e26fcf940559405cd1cced7`)
  (via `tools/webpdf.py`, text layer pdftotext 44,242 B)
- Source export: `2026-w47-nl-zh-tw.text.md` — 44,308 bytes
  sha256 `bf1f627d1bbf6387cb0f782e6ede2feb3fe18ffb48bd599ce3720be3238b9855` (current);
  (142 single + 2 match headers + 8 match items = 150; 8 golden, 6 gloss)
  (build 3, delta; build 2 was 44,315 bytes,
  sha256 `54d20ccd80af265c3ec62d2db0a08cbd1e7ecc559ea1bdc24557b449d293539e`)
- `ABSTRACT.txt` (Traditional Chinese, one line, no ASCII double quotes)
- This KIT.

## Build record (final = build 1)

- `run.py` exit 0, TOTAL 150, **zero OVERFLOW / TOO WIDE warnings**.
  `flow[P1-headline] ended col 2/2 y=1465` (exactly as the core);
  `flow[P8-keys] ended col 3/3 y=2441 (bottom 2560)`.
- `render.py` exit 0; `webpdf.py` exit 0 (< 7 MB).
- Gates (build 1): **ALL PASS** — occlusion 0 flags; p8 extract 150/150;
  p8 compare CLEAN, 0 key diffs; freeze direct sha256 8/8; print/web text
  posdiff 0 msdiff 0 on all 8 pages (P1 749/749 … P8 1676/1676); pdftotext
  print 44,274 B / web 44,272 B; P8 answer-zone min font 10.12 pt
  (median 10.12); P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit
  clean (off-palette {}, VOL.5 = 5 = core, paper fills 8).
- Visual: all 8 cards viewed, clean. P1 numbers box fits col 1; P2 ZO ONTHOUD
  "口訣" fits and the GEDICHT strip gloss fits its box; P6 chart head
  "圖表（練習數據）" fits; P7 BRIEVEN box ends at 1898, exactly as the core;
  P8 answers 1–150 complete, pen photo in col 4.

## Fixes vs the generated fan-out (explanation layer only)

None needed — this was the only edition that needed no pre-fixes: subtitle
1504 px, numbers-box title 367 px, numbers-box items [2,2,2,2] total 384 px
(box 384 + 12 = 396 ≤ 417, fits col 1), P6 chart head 355 px, ZO ONTHOUD
307 px, agenda gloss 202 px, agenda sub-head 275 px, IN DEZE EDITIE head
296 px — all inside their limits at generation. The bridge is 3 lines at
20.5 pt (ends 1411); the box (384 px) fits col 1 (1411 + 396 = 1807 ≤ 1828).
No P8-keys overflow: Traditional Chinese notes are compact (flow ends 2441,
the same shape as the core's 2457).

## Re-fanout (build 2, core fix2 5de7492f, 2026-11-11)

Rebuilt from the fixed core (fix2: D3 match option c shortened, D4 answer
markers localized, D5 P4 Eredivisie standings line). Core HEAD built against:
`5de7492f` (fix2); core fix3 `f567bcea` landed during this rebuild and is NOT
included — separate incremental rebuild pending.

- `run.py` exit 0, TOTAL 150 (A2 46 / B1 73 / B2 31; by page 10/18/18/18/18/18/
  12/38; 81 model words), zero OVERFLOW / TOO WIDE.
- D3: P2 option c short form `eten voor Sinterklaas' paard` in place,
  clearance +71.9px; long form 0.
- D5: `Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`
  in P4 SVG + text.md.
- D4: 142 `— 答案：` + 8 `(答案 x)`; Chinese markers kept. The fixed exporter
  writes `— 答案： B` (marker + space + answer, uniform with the other
  9 editions' `— Correct: B`); the pre-fix2 export had no space after `：`.
  Total `答案` in text.md is 168 — the extra 18 are instruction/header text
  (選出正確答案 / 答案見第8版 / 按題號找答案 / 無唯一答案), identical in the
  old build; the per-edition check was corrected to count markers (142+8).
- Terminology (proof1 D3): `聖誕老人新聞` ×8, `《荒島遠征》` ×3 in text.md;
  old terms `辛特克拉斯新聞` / `《魯濱遜遠征》` 0 residual.
- Gates: **ALL PASS** — occlusion 0; p8 extract 150/150, compare CLEAN;
  freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages (tokens
  749/705/664/658/685/648/733/1676); pdftotext 44,323 B both; P8 font
  min=median 10.12pt, spans 565; chips core=edition {A2:8, B1:24, B2:3};
  §1.1 clean.
- Creambox: 3 flags, all pixel-probed 0 dark pixels in the 7px strip below
  the box bottom → false positives (P2 EN JIJ gloss, P5 EN JIJ gloss, P6
  chart caption; descent-allowance artifacts). 0 true overflow.
- Horizontal box-title true-ink check (new, `check_titles_h.py`): 56 titles,
  ALL PASS, 0 FAIL. Tightest: P1 numbers-box title +11, P2 `口訣` +13.
- Visual: 8/8 clean (P1 masthead/agenda/numbers box; P2 short option c one
  line, EN JIJ gloss ends inside its box; P3 article + exercises; P4 box
  with the new standings line; P5 `《荒島遠征》` + EN JIJ gloss inside;
  P6 chart + VOOR OF TEGEN in box; P7 BRIEVEN ends above the ZINNEN rule;
  P8 answers 1–150 complete).

**Known, NOT fixed in this build (fix3 territory — separate incremental
rebuild):**
- P3 lone `。` on its own line (x=538, y=2280.22, under the C HET PERFECTUM
  instruction) — core fix3 D6, inherited from the fix2 core. Visually
  confirmed on the P3 crop.
- P6 chart-caption gloss `。` at the start of a line: `。問題：你在鞋裡放什麼？
  （100 名年輕人）` (x=1462, y=659.44) — same line-breaker defect class as
  fix3 D6/D7, but NOT in fix3's scope: it is still present in the current
  core (`f567bcea`) itself. Family-wide sweep 2026-11-11: only zh-tw has
  orphan-。 lines (2); the other 9 editions have 0; the core has 1 (this P6
  line). Flagged for the coordinator — needs a core fix + incremental rebuild.
- P7 has no orphan `。` (fix3 D7 did not reproduce in this edition's wrap).
- Q140 key lacks `kort` (source `我做一個帶小詩的偽裝禮物。→ ___`, key
  `Ik maak een surprise met een gedicht.`): core-level mismatch, recorded
  only — coordinator scope fixed es only.

## Delta (core fix3 + fix4 + fix5, 2026-11-11, build 3)

Core fix3 (D6/D7) + fix4 (D8/D9/D10) + fix5 (D11) synced to this edition.
Only this edition's own source files changed; core, other editions and the
staging copy were not touched. No commit, no push. Full record:
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-zh-tw/DELTA-LOG.md`.

- D6 P3 bridge (`content34.py:78`): `e.bridge("用現在完成式填空。注意助動詞 hebben/zijn。", w=346.55)`.
  Pre-fix the lone `。` sat alone on its own line (y=2280.225, class-a, TRUE defect).
  Width scan (own text + own `svglib.wrap()`, 0.1px step): band 287.0–406.1px
  wraps to the same 2 lines with `。` at the end of line 2; mid 346.55.
  Rebuilt: lines `用現在完成式填空。注意助動詞` (2250.5) / `hebben/zijn。` (2280.225),
  baselines unchanged, p3 SVG changed, no downstream shift.
- D7 P7 gloss bridge (`content7.py:19`): `a.bridge("de wedstrijd 比賽；de groepswinst 小組頭名；de kwartfinale 八強賽；scoren 進球。", w=342.0)`.
  Pre-fix line 2 began with `；` (y=755.385, class-b, TRUE defect — the KIT's
  "P7 has no orphan 。" was true only for lone 。).
  No 2-line band is clean: 395.6–416.0px keeps 2 lines only by splitting
  小組頭名 across lines, 416.1–422.5px keeps the leading ；.
  Chosen band 329.5–354.5px wraps to 3 clean lines (no line-initial closer,
  no split gloss term); mid 342.0. Rebuilt: `de wedstrijd 比賽；de groepswinst` /
  `小組頭名；de kwartfinale 八強賽；` / `scoren 進球。` (725.66/755.385/785.11);
  A2 flow ends y=1252 (bottom 1560), no overflow; p7 SVG changed.
- D8 P6 caption (`content56.py:143–144, 156`): new `capcn_w = 397.7`, used in
  both the box-height computation and the `p.para` call. Pre-fix line 2 began
  with `。` (y=659.44, class-b, TRUE defect). Width scan: band 388.5–406.9px
  keeps the 2 lines with `。` at the end of line 1; mid 397.7. Rebuilt:
  `練習數據：虛構數字，僅供練習，非真實調查。` / `問題：你在鞋裡放什麼？（100 名年輕人）`,
  baselines 635.02/659.44 unchanged, `P6 chart ends 665` unchanged, p6 SVG changed.
- D9 Q140 (`content8.py:75`): registry key `Ik maak een surprise met een gedicht.`
  → `Ik maak een surprise met een kort gedicht.` (Dutch key, ported directly;
  stem `我做一個帶小詩的偽裝禮物。` already contains 小, untouched; note unchanged).
  Three sources agree: registry = text.md:415 answer = P8 node.
  text.md re-export diff is exactly line 415 (+5 B, `kort `).
- D10 P7 readers'-letters box (`content7.py:91–92, 100`): new `dt_zh_w = 390.05`,
  used in both the `lh` height computation and the `p.para` call. Pre-fix line 2
  began with `，` (y=1782.67, class-b, TRUE defect). Width scan: band 380.1–400.0px
  keeps the 2 lines with `，` at the end of line 1; mid 390.05. Rebuilt:
  `截稿時未收到真實來信或第 8 版最佳作文，` / `刊登示例信，承諾順延 VOL.5。`,
  baselines 1754.27/1782.67 unchanged, `P7 col3 ends 1898.0` unchanged.
- D11 P4 HET PROGRAMMA box (`content34.py:130`): top reserve 62 → 89
  (= 16 pad + 52 title block + 21 para y-offset). Facts wrap 3/3/3/2/3 = 14 lines;
  `sh` 611.0 → 638.0. Pre-fix last line `18:45 uur.` baseline 1209.49 was 6.89px
  BELOW the box bottom (1202.6). Rebuilt: box bottom 1229.6, baseline margin
  **+20.11px**; true-ink margin +20.60px (cards 1×) / +20.48px (print PDF 150dpi);
  7px strip below the box bottom 0 non-paper pixels on both renders.
  `P4 col3 ends 1229.6`; P3's same-shape box untouched.
- `bslib4.py`: `Flow.para` / `Flow.bridge` take the optional `w` wrap-width
  override (mechanism from core-nl fix3; this edition's re-fanout predates it).
  Default = column width, all other calls unaffected.
- Gates (build 3, all measured, see DELTA-LOG §6): `run.py` rc=0, TOTAL 150
  (10/18/18/18/18/18/12/38; A2 46 / B1 73 / B2 31), 0 overflow; SVG hashes —
  only p3/p4/p6/p7/p8 changed, p1/p2/p5 byte-identical; occlusion 0 flags;
  p8 extract 150/150; p8 compare CLEAN, keydiff [137, 138] (translation keys,
  by design); 3-way key compare 149/149 MATCH (Q150 open-writing exception);
  freeze core baseline 8/8 + self repro 8/8; print/web text posdiff 0 msdiff 0
  on all 8 pages; pdftotext 44,329 B both; P8 answer-zone min 10.12pt;
  orphan sweep 0/0 both classes (PIL + svglib, 1419 lines); creambox 3 flags,
  all pixel-probed false positives (7px strips 0 ink; true-ink margins
  +7.94/+7.95/+8.81px); spill sweep 0 true spills; boxtitle true-ink scan
  58 items, 1 method artifact adjudicated (P8 head — title glyphs end x≈323,
  margin +187px; the ink at x=537–539 is column 2's B1 chip, identical on
  staging/core/rebuilt cards).
- New SHAs (this build): print `6de893ca…704a` / 25,993,186 B; web
  `172c1be8…ff20` / 2,369,230 B; text `30af89df…60` / 44,320 B.
  Build-2 SHAs retained in "Files delivered" above as history.
  Staging copy `fanout-nl/2026-w47-nl-zh-tw/` untouched (three SHAs re-verified
  identical to build 2 after the delta). Awaiting independent proof1.

## D5 rebuild (2026-11-12, B档 — explanation-layer Latin rendered in Newsreader instead of Noto Sans CJK; REDO in top-level production)

- **Why a redo / who finished it:** the first D5 worker (2026-11-12, `scratch-d5-rebuild-nl/`) never started the CJK reader editions (only empty scratch dirs). The second worker (`scratch-d5-redo-nl/`) did Phase A + D5 install + rebuild-1 in top-level production, then was interrupted during `render.py` of rebuild-1 (0-byte `render.log`, 11:28 UTC). The third worker applied the one defect fix below and ran rebuild-2 to green.
- **Pre-D5 baseline (top-level, verified on disk, `scratch-d5-redo-nl/2026-w47-nl-zh-tw/baseline.txt`):** svglib md5 `d82666126b61cb2ec30583e554b7c887`; print `6de893ca2811357c7be524b2b17e78af1c5362abc647e957d8665559466c704a` / 25,993,186 B; web `9b364507f3c66ae67403fd2604185b5514f5143ea2d3f26887f0c1a62453f16d` / 2,369,238 B (KIT §Files delivered recorded a different web SHA `172c1be8…` / 2,369,230 B — pre-existing drift, web rebuilt after KIT written); text `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60` / 44,320 B. Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 333 Latin-in-CJK-sans. `run.py` pre-run reproduced the on-disk SVGs 8/8 byte-identical.
- **Install:** mechanism `apply_variant.py --target nl --reader zh-tw` (mode cjk — character-script routing, no `_READER_LANG` gate, per CJK-DECISION §1), svglib md5 `d82666126b61cb2ec30583e554b7c887` → `83c4820e35a1e89c010ae57a230fb958`. Routing assert: FAILURES 0.
- **Ported core fix:** P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (pre-D5 spill gate 0 SPILL).
- **Defects found by the gates (rebuild-1):** exactly one — HEAD TOO WIDE [P2-feature]: `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt (`content12.py:175`; core-nl D5 defect, same line). No box-title defect: all 25 titles fit after the install (boxtitle 0 DEFECT, creambox PASS 0 defects).
- **Gates (final rebuild-2, after the 1 fix, all in top-level production):** `run.py` TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`head_check.py` PASS 0 defects); `render.py` / `webpdf.py` RC 0; `p8.py extract` 150/150, `compare` vs core-nl CLEAN, keydiff=[137, 138] (reader-language keys, expected); `freeze.py baseline` 8/8 byte-identical; `freeze.py diff` vs core-nl: added CJK 1051 (Traditional Chinese reader text, expected); vs pre-D5 baseline: added CJK 0, added Latin strings 214 (run-splitting, expected); `occlusion_audit.py` 0 flags; `spill_sweep.py` 0 SPILL (55 OBSERVE); `boxtitle_check.py` 0 DEFECT (25 titles, 312 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` PASS 0 defects (P8 lines 221 → 221, footer slack 53.0px unchanged); `d5_census.py` PASS — D5 Latin 0, Cyrillic 0, curly-in-CJK 0; `census_quotes.py` 0 defective; text layer print = web = 44,254 bytes, word multiset diff 0, de-whitespaced char streams equal; orphan sweep (a) 0, (b) 0.
- **New SHAs (lowercase, verified on production files):** print `90710eae78ae9ddd78f02a8a47041fbb09f322aa5adb351e214034384679e32b` (13,888,370 B); web `1a923a7a42c6c7bdcff8805c3ae0faca314a59cb3f632a7378dd7d4c3e93c954` (1,976,962 B). **text.md unchanged:** 44,320 B, sha256 `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60`, byte-identical to the pre-D5 baseline.
- **Repro check (2026-11-12, third worker):** re-running `render.py` + `webpdf.py` in place reproduced the print PDF byte-identically (SHA unchanged); the web PDF rebuilt with a new SHA `42b892b5c065d18639cb61254286cf016be0a01d41a5320ca6b94aeb5f114b8a` (1,976,958 B) — content-equivalent (pdftotext 44,254 B, identical; `textlayer.py` re-run RC 0, word multiset diff 0). Only embedded-font `head`-table checksums differ (stream-level diff on nl-de: 70 bytes in 18/126 streams). Web PDF SHA is not reproducible run to run (see build-7 note); "Files delivered" above is re-synced to the new production file; the SHA on the "New SHAs" line above is the rebuild's original output, kept as history (was `1a923a7a42c6c7bdcff8805c3ae0faca314a59cb3f632a7378dd7d4c3e93c954`, 1,976,962 B).
- **Fix (2026-11-12, W47 nl repair, second worker):** PROOF-NOTE items 10 + 11. 10: `content12.py:58/155/243/259` four × `禮物之夜` → `收禮夜` (majority form, same as core zh-cn); print full-text count now 禮物之夜 0 / 收禮夜 10. 11: `content8.py:64` Q135 `主語` → `主詞`; `:66` Q136 `主語` → `主詞`、`賓語` → `受詞` (matching Q97/98/133/134); print full-text count now 主語 0 / 賓語 0 / 主詞 6 / 受詞 3. Rebuilt: `run.py` TOTAL 150 RC 0, `render.py` RC 0, export dry-run to /tmp then re-exported (150 exercises, 8 golden, 6 gloss), `webpdf.py` RC 0; final diff vs pre-fix text.md contains ONLY the 6 intended line-pairs (22, 61, 104, 113, 409–410) — exporter trap did not fire this round. Gates (`tools/gates.py`, ALL PASS): occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (reader-language keys, expected); freeze 8/8; print/web text posdiff 0 msdiff 0 all 8 pages; pdftotext print = web = 44,242 B; P8 answer-zone min 10.12pt; P8 chips = core {A2: 8, B1: 24, B2: 3}; §1.1 SVG audit clean. Extras: `boxtitle_check.py` 0 DEFECT, 0 OBSERVE, 0 marginal; `spill_sweep.py` 0 SPILL (55 OBSERVE); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `head_check.py` PASS 0 defects; `d5_creambox_audit.py` PASS 0 defects. **New SHAs (lowercase, verified on production files):** print `3fd293bfef564ea277f4f96495710f7391ad5204da659bdd43dc2ce3edfde693` (13,887,537 B); web `542c6f1bc8e2f71b0cdf558e169dca3d1738e981919433c63182a304a44754ec` (1,976,266 B); text.md `bf1f627d1bbf6387cb0f782e6ede2feb3fe18ffb48bd599ce3720be3238b9855` (44,308 B). Logs: `hidden_files/w47/scratch-fix-nl/nl-zh-tw/`.
- **Size note:** print PDF 25,993,186 → 13,888,370 B (−12.1 MB): fewer CJK glyphs embedded now that the explanation-layer Latin routes to Newsreader (same direction as nl-ja 26.0M → 18.8M and nl-ko 17.3M → 13.9M). Not content loss: text layer verified equal print vs web (44,254 B, word multiset diff 0).
- **Files changed (not committed, not pushed, no `lint.mjs --write`):** `svglib.py` (D5 install, mode cjk), `content12.py` (P2 head 25 → 23pt), `WEEKLY-KIT.md` (sizes + this section). Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-zh-tw/` (`rebuild-1.log` = install + defect discovery, interrupted at render; `rebuild-2.log` = final green; `run.log`, `render.log`, `webpdf.log`, `routing.log`, `post/` gates + `post.txt`, `pre/` pre-D5 gates, `baseline.txt`).
