# Lucerna Weekly — VOL.4 Traditional Chinese, German explanations (W47)

## Edition identity

- **Pairing:** zh-tw × de — Traditional Chinese text, explanations in German, for German-speaking readers.
- **Issue week:** Monday 2026-11-16 to Sunday 2026-11-22 (VOL.4; `tools/tables.py vol 2026-W47` = 4).
- **Slug (insert):** 2026-w47-zh-tw-de. **Edition dir:** `production/2026-w47/2026-w47-zh-tw-de/` (build code + assets + PDFs + KIT + ABSTRACT.txt + text.md). Source: `production/2026-w47/core-zh-tw/` (read-only; nothing in the core was modified — verified: core print/web/text SHA unchanged after this build).
- **Masthead:** Lucerna (no article — Chinese is article-less), UnifrakturMaguntia 147pt (196px).
- **Top strip (P1):** left `VOL.4　繁體中文版`, centre `台灣　香港　TAIWAN UND HONGKONG`, right `2026年11月16日至11月22日` (17pt, full-width spaces).
- **Edition line (P1, 27pt bold, OLIVE):** `繁體中文週報　VOL.4　遊行　金馬獎　小雪` (unchanged from core — target-language line).
- **Badge line (P1, 16pt, GREY):** `繁體中文正文　德語講解 — Traditioneller chinesischer Text mit Erklärungen auf Deutsch, für deutschsprachige Leser`
- **Lead headline (P1, 45pt):** `週日下午2點，封王遊行天母出發` (frozen core text).
- **Format:** 8 pages, 1462.5×2025 pt (1950×2700 px), 4 columns, newsprint paper #fbfaf6. Same geometry as core.
- **Level ramp:** A2 → B2, one level chip on every item (A2 #5c6e30 / B1 #46581f / B2 #37402f, white text).
- **Traditional Chinese is natively produced for the Taiwan/Hong Kong ecosystem.** Not converted or transcoded from any Simplified edition; no zh-cn text was copied or converted anywhere in this build. Only the explanation layer was rewritten into German.

## SOP §1.1 measurements (this edition, measured on final SVGs/PDFs)

- Paper #fbfaf6 on all 8 pages. Gold/brick/near-black: 0 occurrences. No double-line outer frame. Badge colours present (A2 #5c6e30, B1 #46581f, B2 #37402f).
- Furniture uses full-width spaces (　); 「·」 appears only inside multiple-choice option lists, the P6 timeline legend, and chart dots — the same rule as the core KIT. Footer: `Lucerna　繁體中文週報 VOL.4　繁體中文正文　德語講解`, page lines `Seite N von 8`.
- VOL.4 throughout; VOL.5 appears exactly once, in the P7 next-issue teaser head (`下期預告　Nächste Woche (VOL.5)`) — correct, not a misprint.
- P8 answer font size (PyMuPDF, measured 2026-11-11): keys at **9.75pt on both print and web PDFs** — exactly the SOP §1.1 floor (≥9.75pt). P8 stems stay at 13.8px = 10.35pt, per the core ruling (38 exercises + writing strip + 150 keys cannot fit 8 pages at 20.5px stems; core Build 13 trial failed with 8 FLOW OVERFLOW + 381 occlusion flags and was rolled back).
- No drop cap (same recorded gap as core: no W43 page implements one; not implemented).
- P7 geometry (final build): col3 ends 1849.8, phrases strip fy=1873.8, teaser ends 2589.8 (footer rule 2596 — clear by 6.2px). P7 three-column Flow ends: A2 1343, B1 1602, B2 1535 (bottom 1560 — see "Known non-defects"). P7 image ends 1570.9. P8 writing strip ends 1280.2, keys end 2373 (column 4, bottom 2560).

## Per-page contents (frozen core content; only the explanation layer is German)

Same as core KIT: P1 Front (A2, 10 exercises) — Dragons parade + Leofoo night-parade finale; P2 Life (A2, 18) — Xiaoxue + Double 11 + Christmasland; P3 Culture (A2→B1, 18) — Golden Horse 63rd + steel festival + Méliès; P4 Sport (B1, 18) — parade deep report + U-Sport points + bar chart; P5 Youth (B1, 18) — HK Disneyland Christmas + jazz festival + Pokémon 30th; P6 Deep read (B2, 18) — Nov 22 timeline; P7 Language focus (A2/B1/B2 + error clinic + 越…越… frame + readers' corner + phrases + VOL.5 teaser, 12 exercises); P8 Test & keys (38 items).

## Measured totals (registry, identical to core)

- **Total exercises: 150.** By level: A2 44 · B1 74 · B2 32. By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. By type: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.
- **Images per page:** P1 0, P2 1, P3 1, P4 1, P5 1, P6 0, P7 1, P8 1 — 6 photos total, all with credits present in the SVGs (same files/credits as core).
- **Charts:** P4 olive bars 90.0, 450.0, 900.0 px (= 10/50/100 points × 9); P6 timeline dots cx 188.0, 695.21, 948.82, 1033.36, 1202.43 (= 14:00/17:00/18:30/19:00/20:00).
- **PDFs (D5 rebuild 2026-11-12 + P7 金句修复 2026-11-12):** print `Lucerna-VOL4-DE.pdf` 11,196,101 bytes, SHA-256 2a22bcdaa8ca3682423ddff8c10e5f3bfcc6ec02f3c11ea79e3c744b310b2184; web `Lucerna-VOL4-DE-web.pdf` 1,903,630 bytes (< 7 MB), SHA-256 a67ffad9183562624bbef7deb112b85d33c1d9717fca95a9c5bcaed7ecf4a838. Both 8 pages, 1462.5 × 2025 pt. (D5 交付：print 11,195,908 B / 1b1f0f0370c1…; web 1,903,427 B / f430e390f495…。P7 修复：print +193 B、web +203 B，皆为「香港」二字所致。) (Pre-D5 final render: print 21,717,594 B / da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e; web 2,452,925 B / 542051ea82eee8a577d69976f93e2ca233cdd4fc7be3f028290a9ec310acbdfd — 注：KIT 原登记 web 为 2,452,914 B / de3a7594…，与交付文件差 11 字节，系 webpdf.py 每次重跑 SHA 浮动，见 core KIT 同注。)
- **Text layer:** pdftotext print 48,161 bytes / web 48,162 bytes (P7 修复后实测；修前 D5：48,155 / 48,156，+6 B 恰为「香港」二字）; character multiset difference 0 (the 1-byte gap is the same run-boundary whitespace artifact recorded in the core KIT — no character missing).
- **Text export:** `2026-w47-zh-tw-de.text.md`, 51,820 bytes, SHA-256 8187f61963262e57627f2ff371e5c7ddb8d5b974fc44763ca4555eb57c1ab83f（修前 D5：51,814 B / 85584db99a9e…，仅引文行 +「香港」二字 +6 B）, exported from the edition's own SVG text layer in page order (source-side; never from a PDF). H1 `VOL.4 · Chinesischer Text (traditionell) · Erklärungen auf Deutsch` (W46 de precedent). All 150 exercise numbers present; no English instruction leftovers.
- **ABSTRACT.txt** (German, single line, no ASCII double quotes): starts `Lucerna Traditional Chinese weekly VOL.4 für deutschsprachige Lernende, A2 bis B2, 150 Übungen: …` — real topics + A2–B2 + 150 Übungen.

## Trend and fact sources / image licenses

Identical to the core KIT (core-zh-tw/WEEKLY-KIT.md) — fan-out does not re-do trend research or change facts. Same 6 placed images with the same credits/licenses.

## Readers'-corner disclosure (P7, German)

- Chinese (frozen): 「延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。」
- German: "Beispielbrief der Redaktion — kein echter Brief. VOL.3 versprach echte Leserbriefe und die besten Seite-8-Texte ab dieser Ausgabe; bis zum Redaktionsschluss ging keiner ein, der druckfähig wäre. Das Beispiel bleibt; die Einladung bleibt offen."
- No reader, letter, name, or quote is invented anywhere in this issue. The corner is labeled 「台北小讀者（編輯範例）」.

## Editorial red lines observed

- No international politics. Because the target is Chinese, Chinese domestic politics is also excluded.
- No anniversary used as a living trend.
- No Simplified-only characters in Traditional text (`checks.py` SIMP_ONLY_HITS []).

## Reproducible build

Build code lives in `production/2026-w47/2026-w47-zh-tw-de/` (copied from core-zh-tw by `scratch-fanout-zh-tw/transform.py de`, then patched as below). Content modules run only via the single one-process driver, never standalone. Run with the toolkit venv:

```
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-de
~/workspace/weekly-git/tools/venv/bin/python run.py
~/workspace/weekly-git/tools/venv/bin/python render.py
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg Lucerna-VOL4-DE-web.pdf
~/workspace/weekly-git/tools/venv/bin/python export_zhtw_textmd.py svg 2026-w47-zh-tw-de.text.md "VOL.4 · Chinesischer Text (traditionell) · Erklärungen auf Deutsch"
```

Outputs: 8 SVGs in `svg/`, 8 full-page PNGs in `cards/`, print PDF `Lucerna-VOL4-DE.pdf`, web PDF `Lucerna-VOL4-DE-web.pdf`.

## Proofread record (self-check, before independent proofread)

- **Full self-proofread:** the extracted text of all 8 pages was read (rendered cards P1–P8 viewed page by page + text.md scan); every answer key re-derived against its question/article/chart; every date/weekday and arithmetic total re-checked (same totals as core); every glossed term confirmed present on its own page.
- **Occlusion audit:** `tools/occlusion_audit.py` selftest passed (all 6 planted classes fired, clean controls silent). Final round after both fixes: **0 flags**.
- **P7 phrases:** all 8 at exactly 2 occurrences each (article + P7), via `checks.py` (PASS).
- **Simplified-character audit:** zero hits (`checks.py` PASS).
- **Chart geometry:** `checks.py` PASS — P4 bars 90/450/900; P6 dots as above.
- **P8 keys:** `tools/p8.py extract --p8 svg/p8-test.svg --total 150` → noted set = 150 of 150; `p8.py compare` vs core → **CLEAN** (missing=[] extra_count=0 keydiff=[]). Answer values identical to core for all 150 items. Writing model 142 characters, inside the 120–180 band. P8 level chips: 38/38 exercises badged; items 113–150 each carry a chip (A2 8 · B1 20 · B2 10 on P8); F writing head `F　寫一寫　Schreiben` present with its B2 chip on item 150.
- **Freeze:** `tools/freeze.py baseline` re-run reproduces **8/8 SVGs byte-identically** (direct sha256 comparison of `build-copy/svg/` vs `svg/`; all MATCH).
- **Web PDF:** `tools/webpdf.py` exit 0; 2,436,311 bytes (< 7 MB); text layer multiset difference 0 vs print; 8 pages. P8 min size 9.75pt on both PDFs.
- **§1.1 measurements:** paper/gold/brick/frame/badges/footer/separators/VOL as listed above; all pass.
- **Visual QA:** all 8 rendered cards viewed page by page (P1–P6 + P8 after the first build; P7 re-viewed after the col3 fix; P8 re-viewed after the key-note fix) — no overflow, no overlap, no footer collision, image/credit placement confirmed; P4/P6 charts re-viewed.
- **English-leak scan (whole edition):** every SVG text node compared against the core's — 0 strings identical to core English prose after the fix (see "Fixes" below).

## Fixes applied during this build (all inside this edition dir only)

1. **P7 col3 overflow (build 1 → build 2).** Build 1: P7 col3 ended 1935.2 (core 1825.4) — German explanations run ~30% longer than English — so the phrases strip started at fy=1959.2 and the VOL.5 teaser box ended 2689.2, 93px past the footer rule: occlusion audit flagged 2 (LINEX + TEXTX, teaser heading ink crossing the footer rule and overlapping the footer text). Fixed in `content7.py` (explanation layer only, no target text touched): shortened the readers'-corner German disclosure (lcn 8 → 7 lines, all facts kept), the third error-clinic gloss (3 → 2 lines: "12-mal, 17:30–23:00 Uhr"), the 越…越… frame example (5 → 4 lines), and the teaser box height 118 → 104px (heading + one-line paragraph fit). Result: col3 ends 1849.8, teaser ends 2589.8 (clear of the footer rule by 6.2px), occlusion 0 flags. The three shortened German strings were mirrored into `scratch-fanout-zh-tw/tables.py` (de column only) so the table stays the source of truth.
2. **6 untranslated P8 key notes (build 2 → build 3).** The leak scan found 6 key notes still in English — `tables.py` has no ENTRIES for these 5 source strings, so the transform never replaced them: keys 92 ("The ceremony is at the Taipei Music Center."), 98/117/138 ("Xiaoxue is Nov 22." ×3), 100 ("Four big events fall on the same Sunday."), 134 ("Collecting points is 集點."). Fixed in `content56.py` (keys 92/98/100) and `content8.py` (keys 117/134/138): "Die Zeremonie ist im Taipei Music Center." / "Xiaoxue ist am 22. Nov." / "Vier große Ereignisse fallen auf denselben Sonntag." / "Punkte sammeln heißt 集點." — answer values untouched. Rebuilt, re-gated: leak scan 0, p8 compare still CLEAN, occlusion 0. **Shared table gap (for the coordinator): these 5 source strings are missing from `tables.py` ENTRIES, so the fr/es/it/pt/nl/ru/ja/ko builders will hit the same 6 leaks in their editions and must patch the same 5 lines in their own dirs. Do not add them to the table without all 9 languages' translations.**
3. **Stale core files removed.** The copytree brought the core's `Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, and `2026-w47-zh-tw-en.text.md` into this dir; all three were deleted (byte-identical to core, verified by SHA before deletion). This dir now holds only the de files.
4. **W46 precedent note:** the P8 D-head warning `HEAD TOO WIDE [P8-ex]: D　讀一讀，答一答　Lesen und antworten` also appears in the shipped W46 de build log. Measured: the head is 423.08px vs the 422.5px column — 0.58px into the 28px gutter, no collision with anything (occlusion 0 flags, visual check clean). Kept as-is, recorded here.

## Known non-defects (measured, recorded, not fixed)

- **P8 D head +0.58px** (above) — same as shipped W46 de; invisible, no collision. **FIXED by the D5 rebuild (2026-11-12):** battery head `D　讀一讀，答一答　Lesen und antworten` size 21→20 (content8.py:72); D5-measured advance 424.2 → 404.0 vs CW 422.5, clears by 18.5px; run.log now 0 HEAD TOO WIDE. Text unchanged.
- **P7 B1 column ends 1602 vs nominal bottom 1560 (+42px)** — German B1 column runs 42px past its nominal bottom (core fix4/fix5 lengthened the P7 B1 content: M1 「終點 (end point)」 and the Memory-trick sentence); the next element (phrases strip) starts at fy−14 = 1859.8, 258px clear; no overlap (occlusion 0 flags, visual check clean).
- **P5 cross-column fragment** — the first article's last line ("…鬧，出門之前，先列好想看的清單。") flows to the top of column 1; normal newspaper flow, same in core.
- **P8 stems 10.35pt** — per the core ruling (see §1.1 note); keys meet the 9.75pt floor.
- **text.md page headings in English** ("## Page 6 — Deep read" etc.) — the exporter's fixed format, identical in the core and the shipped W46 de text.md; not a leak.

## Re-fan-out (2026-11-11, this session — re-fanout rod)

- Core baseline (frozen, verified before rebuilding; core untouched — SHA re-verified after the build): print `Lucerna-VOL4.pdf` 19,420,552 B SHA-256 5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a; web `Lucerna-VOL4-web.pdf` 2,324,042 B SHA-256 1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240; text.md 49,798 B SHA-256 09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b (core re-proof #3 verdict (a) zero issues, 定稿).
- Method: the 9 old edition dirs were backed up whole to the builder's scratch (`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-de/`, 41 files, file-list SHA-256 identical to the old production dirs; backup NOT deleted), then `transform.py de` rebuilt this dir from the new core (mechanism table `scratch-fanout-zh-tw/tables.py`, 242 ENTRIES, with the 2026-11-11 patches: nl :273 Xiaoxue gloss 「Volgende zondag」→「Deze zondag」; D1 「this Sunday」 sweep de/fr/es/it/pt/nl/ja; M1/M2 values already in the table, verified). transform is one-shot — the old dir was removed before rebuilding. The stale core files the copytree brought in (`Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, `2026-w47-zh-tw-en.text.md`) were deleted after SHA verification, as in the first build.
- Hand-fixes re-applied (all verified by diffing the rebuilt files against the backup-old edition): every old hand-fix was already mirrored into the mechanism table or carried by the new core — bslib4.py/render.py 0 diffs; content diffs are core-parallel (D1 本週日, fix2 HK box/BABYMONSTER/取捨, fix5 D4 box 230→244, N4 夜間遊行) or table-driven fix1 values (M1/M2, D1 lang values, N2 P8 notes, ru N5/N6/N7, ja D-ja-2, ko M4/M5, it D3). The one fix that lived only in the old edition file — the de P7 teaser bar press 118→104px — was re-measured after rebuild (teaser ends 2603.82 at 118px, 7.82px past the footer rule) and re-pressed to 104px in `content7.py` (same two lines as the old file); re-run: col3 ends 1849.82, teaser ends 2589.82 (6.18px clear of footer rule 2596).
- Gates re-run on the rebuilt edition (2026-11-11, `scratch-refanout-zh-tw/gates.py de final`): checks.py PASS; occlusion audit selftest passed, **0 flags**; P8 extract 150/150, compare vs core **CLEAN** (keydiff=[] missing=[]); canonical creambox full scan 36 boxes, 0 negative inside-only clearances (P7 min +12.5px; P7 toolbox clearances +40.5/+12.5/+14.0); boxtitle 36 boxes, 0 overruns, min title right margin 23.2px; print/web text-layer multiset diff 0; P8 keys 9.75pt on both PDFs (PyMuPDF); fill-in keys 54/54 from body text, answer keys 1–150 continuous; English-leak scan 0 deny hits; P6 18:30/19:00 timeline-label ink gap 0.6px (same hairline as the core precedent, no overlap); freeze baseline re-run reproduces **8/8 SVGs byte-identically**, core integrity OK.
- Supplementary PIL creambox scan: **STRADDLE 4** (old build: 4) — bilingual file-card titles whose ink extends past their borderless cream box's right edge by ~7–80px (the title is fully legible, no overlap with anything, occlusion 0). The old build carried the identical 4 flags at identical coordinates (verified by running the same scan on the backup-old SVGs) — pre-existing in the proofread build, not a rebuild regression. Not fixed in this fan-out: shortening the titles is a design/text decision for the coordinator (fix1) — recorded here, not hidden, not written as a pass.
- Visual QA: all 8 rendered cards viewed (contact sheet + P7 teaser and P4 D4 crops for de) — no overflow, no overlap, no footer collision, image/credit placement confirmed.

## Build history (this session, builder 7th rod)

- Startup probe (2026-11-11 ~01:30 UTC): `git hash-object -w` rc=0 + real file write rc=0; core SHA verified (print f2764750…, web 9191ef79…, text 4a991109…); df 53G free; memory ~1.7G available. Previous rods 4–6 had stopped at the disk-quota probe / run.py exit 120; this rod ran clean.
- `transform.py de` OK (244 lines, same as rod 3).
- Build 1 (run.py exit 0, 0 FLOW OVERFLOW, 1 HEAD TOO WIDE) + render + webpdf: all gates green except occlusion 2 flags (P7 teaser vs footer) — fixed (fix 1 above).
- Build 2 (run.py exit 0) + render + webpdf: occlusion 0, p8 150/150 CLEAN, freeze 8/8, checks PASS, P8 9.75pt, text multiset diff 0 — then the leak scan found the 6 untranslated key notes (fix 2 above).
- Build 3 (final): run.py exit 0, render exit 0, webpdf exit 0, text.md re-exported; all gates re-run green (occlusion 0, p8 150/150 CLEAN, checks PASS, freeze 8/8, leak scan 0, P8 9.75pt both PDFs).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch `weekly-git` pushes or insert.py. Core files untouched (SHA re-verified).
- Re-fan-out rod (2026-11-11 ~10:43–11:50 UTC): rebuilt from the new core via transform.py; de P7 teaser bar re-pressed 118→104px after re-measurement; run.py exit 0 (0 FLOW OVERFLOW, 1 HEAD TOO WIDE (known P8 D-head +0.58px, see Known non-defects)); render + webpdf + text export exit 0; all gates re-run green per the section above (STRADDLE 4, old 4); KIT updated to the new SHAs. No commit, no push; proof1/proof2 by the coordinator separately.
- D5 rebuild (2026-11-12, SOP §1.1 讲解层字体修复）: `apply_variant.py --target zh-tw --reader de`（mode latin）；svglib pre-D5 md5 9caa4651959673f511cd56873d93a04a（与 core 相同）；装机：Noto Sans faces + sans_noto cmaps/_PATH（Medium/Bold）+ fix2 块 + D5 sans 块 + `_D5_READER = "latin"`。修前基线：重建 8/8 SVG 与交付字节一致，TOTAL 150，0 FLOW OVERFLOW；普查 D5 拉丁 618、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 25,858 字符一致。修的缺陷 5 项（全为标题越框；文字一字未动，只降字号）：(1) 修前已有的 P8-ex 电池头 `D　讀一讀，答一答　Lesen und antworten`（+0.6px，D5 后 +1.7px），content8.py:72 字号 21→20，余 18.5px；(2–5) 4 个奶油框标题 25pt 手绘标题越框右缘（修前已溢出，D5 各加重约 +6px）：P2 `耶誕城小檔　Christmasland-Steckbrief` +64.5→+70.5px，content12.py:190 字号 25→20，余 26.5px；P3 `金馬小表　Golden-Horse-Steckbrief` +30.5→+35.5px，content34.py:76 字号 25→22，余 20.1px；P3 `鋼雕閉幕行程　Letztes Wochenende` +28.5→+26.5px（boxtitle），content34.py:93 字号 25→22，余 24.5px；P5 `迪士尼聖誕小檔　Disney-Steckbrief` +18.5→+24.5px，content56.py:81 字号 25→22，余 29.6px。门禁全绿（stage2 终轮）：run TOTAL 150、0/0；head_check（修后）0 缺陷；occlusion 0 flags；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前基线新增 CJK 0；spill 0（140 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（n=546，median 1.008，bold 1.040）；D5 普查 PASS（0/0/0）；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 25,858 字符）；text.md 与修前逐字节相同（85584db9…）。P8 行数 158→160、距页脚线余量 35.7→36.7px。交付：print 11,195,908 B / 1b1f0f0370c1ffb945f8c329c9f29250f96d710253bd562839e53cc672ae05b0，web 1,903,427 B / f430e390f4958cabf98e1034e6a28c564f8b9788f70e8dc6dc50a9e4d16e47ef。未 commit、未 push；独立重校待协调员另派。日志：hidden_files/w47/scratch-d5-zh-tw/logs/2026-w47-zh-tw-de/。
- P7 金句修复 (2026-11-12, 独立重校 PROOF-NOTE 第 1 条，低严重度）: 仅改 content7.py:128 与 checks.py:19——P7 金句第 8 条「迪士尼聖誕，從11月17日開始」→「香港迪士尼聖誕，從11月17日開始」（补句首「香港」二字，与 P5 原句逐字一致；读者语译文不动）。重建 run/render/webpdf RC 皆 0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；head_check 0 缺陷；checks PASS；仅 p7-lang.svg 变化；quote-check 固定引文 2 处（P5+P7）、裸引文 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前新增 CJK 恰 {香:1, 港:1}；spill 0、boxtitle 0 DEFECT、edge 0/0、creambox PASS、D5 普查 PASS、引号普查 0 缺陷字；印/网文字层多重集差 0，修前→修后印层仅 +香/港；text.md 仅引文行 1 行改动（+6 B）。P8 行数 160→160、距页脚线余量 36.7px 不变。交付：print 11,196,101 B / 2a22bcdaa8ca…（确定性，两跑 SHA 相同），web 1,903,630 B / a67ffad91835…，text.md 51,820 B / 8187f6196326…。未 commit、未 push。日志：hidden_files/w47/scratch-fix-zh-tw/logs/2026-w47-zh-tw-de/。
