# Lucerna Weekly — VOL.4 Traditional Chinese, Dutch explanations (W47)

## Edition identity

- **Pairing:** zh-tw × nl — Traditional Chinese text, explanations in Dutch, for Dutch-speaking readers.
- **Issue week:** Monday 2026-11-16 to Sunday 2026-11-22 (VOL.4; `tools/tables.py vol 2026-W47` = 4).
- **Slug (insert):** 2026-w47-zh-tw-nl. **Edition dir:** `production/2026-w47/2026-w47-zh-tw-nl/` (build code + assets + PDFs + KIT + ABSTRACT.txt + text.md). Source: `production/2026-w47/core-zh-tw/` (read-only; nothing in the core was modified).
- **Masthead:** Lucerna (no article — Chinese is article-less), UnifrakturMaguntia 147pt (196px).
- **Top strip (P1):** left `VOL.4　繁體中文版`, centre `台灣　香港　TAIWAN EN HONGKONG`, right `2026年11月16日至11月22日` (17pt, full-width spaces).
- **Edition line (P1, 27pt bold, OLIVE):** `繁體中文週報　VOL.4　遊行　金馬獎　小雪` (unchanged from core — target-language line).
- **Badge line (P1, 16pt, GREY):** `繁體中文正文　荷蘭語講解 — Tekst in traditioneel Chinees met uitleg in het Nederlands, voor Nederlandstalige lezers`
- **Lead headline (P1, 45pt):** `週日下午2點，封王遊行天母出發` (frozen core text).
- **Format:** 8 pages, 1462.5×2025 pt (1950×2700 px), 4 columns, newsprint paper #fbfaf6. Same geometry as core.
- **Level ramp:** A2 → B2, one level chip on every item (A2 #5c6e30 / B1 #46581f / B2 #37402f, white text).
- **Traditional Chinese is natively produced for the Taiwan/Hong Kong ecosystem.** Not converted or transcoded from any Simplified edition; no zh-cn text was copied or converted anywhere in this build. Only the explanation layer was rewritten into Dutch.

## SOP §1.1 measurements (this edition, measured on final SVGs/PDFs)

- Paper #fbfaf6 on all 8 pages. Gold/brick/near-black: 0 occurrences. No double-line outer frame. Badge colours present (A2 #5c6e30, B1 #46581f, B2 #37402f).
- Furniture uses full-width spaces (　); 「·」 appears only inside multiple-choice option lists, the P6 timeline legend, and chart dots — the same rule as the core KIT. Footer: `Lucerna　繁體中文週報 VOL.4　繁體中文正文　荷蘭語講解`, page lines `Pagina N van 8`.
- VOL.4 throughout; VOL.5 appears exactly once, in the P7 next-issue teaser head (`下期預告　Volgende week (VOL.5)`) — correct, not a misprint.
- P8 answer font size (PyMuPDF, measured 2026-11-11): keys at **9.75pt on both print and web PDFs** — exactly the SOP §1.1 floor (≥9.75pt). P8 stems stay at 13.8px = 10.35pt, per the core ruling.
- No drop cap (same recorded gap as core).
- P7 geometry (final build): col3 ends 1823.3, phrases strip fy=1847.3, teaser ends 2577.3 (footer rule 2596 — clear by 18.7px). P8 writing strip ends 1280.2, keys end inside the content bottom.

## Per-page contents (frozen core content; only the explanation layer is Dutch)

Same as core KIT: P1 Front (A2, 10 exercises); P2 Life (A2, 18); P3 Culture (A2→B1, 18); P4 Sport (B1, 18); P5 Youth (B1, 18); P6 Deep read (B2, 18); P7 Language focus (A2/B1/B2 + error clinic + 越…越… frame + readers' corner + phrases + VOL.5 teaser, 12 exercises); P8 Test & keys (38 items).

## Measured totals (registry, identical to core)

- **Total exercises: 150.** By level: A2 44 · B1 74 · B2 32. By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. By type: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.
- **Images per page:** P1 0, P2 1, P3 1, P4 1, P5 1, P6 0, P7 1, P8 1 — 6 photos total, same files/credits as core.
- **Charts:** P4 olive bars 90.0, 450.0, 900.0 px; P6 timeline dots cx 188.0, 695.21, 948.82, 1033.36, 1202.43.
- **PDFs (D5 rebuild 2026-11-12 + P7 金句修复 2026-11-12):** print `Lucerna-VOL4-NL.pdf` 11,189,718 bytes, SHA-256 20ad418b233c3827f96e30a07f402f319d4305b6b4479d7acb0bc1d0e4c8fc1f; web `Lucerna-VOL4-NL-web.pdf` 1,898,763 bytes (< 7 MB), SHA-256 d28897aea142e157ac3710ad5eb923642097f362c5d9de1bdc77cb30b1284550. Both 8 pages, 1462.5 × 2025 pt. (D5 交付：print 11,189,525 B / 1e24a8deb37b…; web 1,898,551 B / 9461e8bad39b…。P7 修复：print +193 B、web +212 B，皆为「香港」二字所致。) (Pre-D5 final render: print 20,939,172 B / 730e15c9e70631a990d021e16e11f80de018683219c3beba08c897abf90c8832; web 2,409,978 B / 0d4eb88a254f8ca1472a30ee6e226b59ca499a4fb6d0d95c09c38137d142fbd1 — 注：KIT 原登记 web 为 2,409,973 B / 1c8dc05b…，与交付文件差 5 字节，系 webpdf.py 每次重跑 SHA 浮动，见 core KIT 同注。)
- **Text layer:** pdftotext print 46,943 bytes / web 46,944 bytes (P7 修复后实测；修前 D5：46,937 / 46,938，+6 B 恰为「香港」二字）; character multiset difference 0 (the 1-byte gap is the same run-boundary whitespace artifact recorded in the core KIT — no character missing).
- **Text export:** `2026-w47-zh-tw-nl.text.md`, 50,602 bytes, SHA-256 487127dd7d72bbe9bc803b921b65d919b7fc53fedf3a70920579c05ec23a57a0（修前 D5：50,596 B / a3662561fff3…，仅引文行 +「香港」二字 +6 B）, exported from the edition's own SVG text layer in page order (source-side; never from a PDF). H1 `VOL.4 · Teksten in het Chinees (traditioneel) · Uitleg in het Nederlands` (W46 nl precedent). All 150 exercise numbers present; no English instruction leftovers.
- **ABSTRACT.txt** (Dutch, single line, no ASCII double quotes): starts `Lucerna Traditional Chinese weekly VOL.4 voor Nederlandstalige leerders, A2 tot B2, 150 oefeningen: …` — real topics + A2–B2 + 150 oefeningen.

## Trend and fact sources / image licenses

Identical to the core KIT (core-zh-tw/WEEKLY-KIT.md) — fan-out does not re-do trend research or change facts. Same 6 placed images with the same credits/licenses.

## Readers'-corner disclosure (P7, Dutch)

- Chinese (frozen): 「延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。」
- Dutch: "Voorbeeldbrief van de redactie, geen echte brief: VOL.3 beloofde echte lezersbrieven en de beste pagina-8-teksten vanaf dit nummer; tot de deadline was er geen publiceerbare brief binnen. Het voorbeeld blijft en de uitnodiging blijft open."
- No reader, letter, name, or quote is invented anywhere in this issue. The corner is labeled 「台北小讀者（編輯範例）」.

## Editorial red lines observed

- No international politics. Because the target is Chinese, Chinese domestic politics is also excluded.
- No anniversary used as a living trend.
- No Simplified-only characters in Traditional text (`checks.py` SIMP_ONLY_HITS []).

## Reproducible build

Build code lives in `production/2026-w47/2026-w47-zh-tw-nl/` (copied from core-zh-tw by `scratch-fanout-zh-tw/transform.py nl`, then patched as below). Content modules run only via the single one-process driver, never standalone. Run with the toolkit venv:

```
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-nl
~/workspace/weekly-git/tools/venv/bin/python run.py
~/workspace/weekly-git/tools/venv/bin/python render.py
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg Lucerna-VOL4-NL-web.pdf
~/workspace/weekly-git/tools/venv/bin/python export_zhtw_textmd.py svg 2026-w47-zh-tw-nl.text.md "VOL.4 · Teksten in het Chinees (traditioneel) · Uitleg in het Nederlands"
```

Outputs: 8 SVGs in `svg/`, 8 full-page PNGs in `cards/`, print PDF `Lucerna-VOL4-NL.pdf`, web PDF `Lucerna-VOL4-NL-web.pdf`.

## Proofread record (self-check, before independent proofread)

- **Full self-proofread:** the extracted text of all 8 pages was read (rendered cards P1–P8 viewed page by page + text.md scan); every answer key re-derived against its question/article/chart; every date/weekday and arithmetic total re-checked (same totals as core); every glossed term confirmed present on its own page.
- **Occlusion audit:** `tools/occlusion_audit.py` selftest passed. Final round: **0 flags**.
- **P7 phrases:** all 8 at exactly 2 occurrences each (article + P7), via `checks.py` (PASS).
- **Simplified-character audit:** zero hits (`checks.py` PASS).
- **Chart geometry:** `checks.py` PASS — P4 bars 90/450/900; P6 dots as above.
- **P8 keys:** `tools/p8.py extract --p8 svg/p8-test.svg --total 150` → noted set = 150 of 150; `p8.py compare` vs core → **CLEAN** (missing=[] extra_count=0 keydiff=[]). Answer values identical to core for all 150 items. Writing model 142 characters, inside the 120–180 band. P8 level chips: 38/38 exercises badged; items 113–150 each carry a chip (A2 8 · B1 20 · B2 10 on P8); F writing head `F　寫一寫　Schrijven` present with its B2 chip on item 150.
- **Freeze:** `tools/freeze.py baseline` re-run reproduces **8/8 SVGs byte-identically** (direct sha256 comparison; all MATCH). (First freeze attempt exited 127 only because it was run with a relative `tools/venv/bin/python` from inside the edition dir; re-run from the repo root was rc=0, 8/8.)
- **Web PDF:** `tools/webpdf.py` exit 0; 2,393,503 bytes (< 7 MB); text layer multiset difference 0 vs print; 8 pages. P8 min size 9.75pt on both PDFs.
- **§1.1 measurements:** paper/gold/brick/frame/badges/footer/separators/VOL as listed above; all pass.
- **Visual QA:** all 8 rendered cards viewed page by page — no overflow, no overlap, no footer collision, image/credit placement confirmed; P4/P6 charts re-viewed; P7 re-viewed after fixes.
- **English-leak scan (whole edition):** every SVG text node compared against the core's — 0 strings identical to core English prose (the 6 known key-note leaks were patched in Dutch before the first full build; see "Fixes").

## Fixes applied during this build (all inside this edition dir only)

1. **6 untranslated P8 key notes — patched before the first full build.** Same shared table gap as de/fr/es/it/pt (see de KIT): `tables.py` has no ENTRIES for these 5 source strings. Dutch translations written in this edition's `content56.py` (keys 92/98/100) and `content8.py` (keys 117/134/138), answer values untouched: "De ceremonie is in het Taipei Music Center." / "Xiaoxue is op 22 nov." / "Vier grote evenementen vallen op dezelfde zondag." / "Punten sparen is 集點。"
2. **P7 col3 overflow (build 1 → build 2).** Build 1: run 0 warnings, col3 ended 1908.7, teaser ended 2662.7 (66.7px past the footer rule). Dutch differs from fr/es/it/pt: its third error-clinic gloss was already 2 lines, so the saving had to come from elsewhere. Fixed in `content7.py` (explanation layer only): readers'-corner Dutch disclosure 8 → 7 lines, second error-clinic gloss 2 → 1 line ("De parade vertrekt om 14:00 (niet 02:00)."), 越…越… frame example 5 → 4 lines. Result: col3 ends 1823.3, teaser ends 2577.3 (clear by 18.7px), occlusion 0 flags. The three shortened Dutch strings mirrored into `tables.py` (nl column only). All candidate strings were measured before applying.
3. **text.md H1 corrected to the W46 nl precedent.** First export used "VOL.4 · Teksten in traditioneel Chinees · Uitleg in het Nederlands"; W46 nl's H1 is "VOL.3 · Teksten in het Chinees (traditioneel) · Uitleg in het Nederlands". Re-exported as "VOL.4 · Teksten in het Chinees (traditioneel) · Uitleg in het Nederlands".
4. **Stale core files removed.** The copytree brought the core's `Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, and `2026-w47-zh-tw-en.text.md` into this dir; all three deleted (byte-identical to core). This dir now holds only the nl files.

## Known non-defects (measured, recorded, not fixed)

- **P4 "Honkbalwoorden" head wraps to two lines** ("棒球詞卡" / "Honkbalwoorden") — wraps within its column, no overflow warning, no overlap; slightly awkward typography, recorded here.
- **P5 cross-column fragment** — the first article's last line flows to the top of column 1; normal newspaper flow, same in core.
- **P8 stems 10.35pt** — per the core ruling; keys meet the 9.75pt floor.
- **text.md page headings in English** ("## Page 6 — Deep read" etc.) — the exporter's fixed format, identical in the core and the shipped W46 nl text.md; not a leak.

## Re-fan-out (2026-11-11, this session — re-fanout rod)

- Core baseline (frozen, verified before rebuilding; core untouched — SHA re-verified after the build): print `Lucerna-VOL4.pdf` 19,420,552 B SHA-256 5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a; web `Lucerna-VOL4-web.pdf` 2,324,042 B SHA-256 1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240; text.md 49,798 B SHA-256 09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b (core re-proof #3 verdict (a) zero issues, 定稿).
- Method: the 9 old edition dirs were backed up whole to the builder's scratch (`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-nl/`, 41 files, file-list SHA-256 identical to the old production dirs; backup NOT deleted), then `transform.py nl` rebuilt this dir from the new core (mechanism table `scratch-fanout-zh-tw/tables.py`, 242 ENTRIES, with the 2026-11-11 patches: nl :273 Xiaoxue gloss 「Volgende zondag」→「Deze zondag」; D1 「this Sunday」 sweep de/fr/es/it/pt/nl/ja; M1/M2 values already in the table, verified). transform is one-shot — the old dir was removed before rebuilding. The stale core files the copytree brought in (`Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, `2026-w47-zh-tw-en.text.md`) were deleted after SHA verification, as in the first build.
- Hand-fixes re-applied (all verified by diffing the rebuilt files against the backup-old edition): every old hand-fix was already mirrored into the mechanism table or carried by the new core — bslib4.py/render.py 0 diffs; content diffs are core-parallel (D1 本週日, fix2 HK box/BABYMONSTER/取捨, fix5 D4 box 230→244, N4 夜間遊行) or table-driven fix1 values (M1/M2, D1 lang values, N2 P8 notes, ru N5/N6/N7, ja D-ja-2, ko M4/M5, it D3).
- Gates re-run on the rebuilt edition (2026-11-11, `scratch-refanout-zh-tw/gates.py nl final`): checks.py PASS; occlusion audit selftest passed, **0 flags**; P8 extract 150/150, compare vs core **CLEAN** (keydiff=[] missing=[]); canonical creambox full scan 36 boxes, 0 negative inside-only clearances (P7 min +12.5px; P7 toolbox clearances +40.5/+12.5/+14.0); boxtitle 36 boxes, 0 overruns, min title right margin 1.5px; print/web text-layer multiset diff 0; P8 keys 9.75pt on both PDFs (PyMuPDF); fill-in keys 54/54 from body text, answer keys 1–150 continuous; English-leak scan 0 deny hits; P6 18:30/19:00 timeline-label ink gap 0.6px (same hairline as the core precedent, no overlap); freeze baseline re-run reproduces **8/8 SVGs byte-identically**, core integrity OK.
- Supplementary PIL creambox scan: **STRADDLE 0** (old build: 0) — bilingual file-card titles whose ink extends past their borderless cream box's right edge by ~7–80px (the title is fully legible, no overlap with anything, occlusion 0). Not fixed in this fan-out: shortening the titles is a design/text decision for the coordinator (fix1) — recorded here, not hidden, not written as a pass.
- Visual QA: all 8 rendered cards viewed (contact sheet + P7 teaser and P4 D4 crops for de) — no overflow, no overlap, no footer collision, image/credit placement confirmed.

## Build history (this session, builder 7th rod)

- `transform.py nl` OK (244 lines).
- Build 1 (run.py exit 0, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE) + P7 teaser 2662.7 (past footer) — fixed (fix 2 above).
- Build 2 (final): run.py exit 0, 0 warnings; render exit 0; webpdf exit 0; text.md exported and re-exported with the W46 H1; all gates green (occlusion 0, p8 150/150 CLEAN, checks PASS, freeze 8/8, leak scan 0, P8 9.75pt both PDFs, text multiset diff 0).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch `weekly-git` pushes or insert.py. Core files untouched.
- Re-fan-out rod (2026-11-11 ~10:43–11:50 UTC): rebuilt from the new core via transform.py; run.py exit 0 (0 FLOW OVERFLOW, no warnings); render + webpdf + text export exit 0; all gates re-run green per the section above (STRADDLE 0, old 0); KIT updated to the new SHAs. No commit, no push; proof1/proof2 by the coordinator separately.
- D5 rebuild (2026-11-12, SOP §1.1 讲解层字体修复）: `apply_variant.py --target zh-tw --reader nl`（mode latin）；svglib pre-D5 md5 9caa4651959673f511cd56873d93a04a（与 core 相同）；装机：Noto Sans faces + sans_noto cmaps/_PATH（Medium/Bold）+ fix2 块 + D5 sans 块 + `_D5_READER = "latin"`。修前基线：重建 8/8 SVG 与交付字节一致，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；普查 D5 拉丁 607、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 24,793 字符一致。门禁全绿（stage1 一轮）：run TOTAL 150、0/0；head_check 0；occlusion 0 flags；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前基线新增 CJK 0；spill 0（134 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（n=535，median 1.003，bold 1.040）；D5 普查 PASS（0/0/0）；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 24,793 字符）；text.md 与修前逐字节相同（a3662561…）。P8 行数 158→158、距页脚线余量 36.3→36.3px，无溢出风险。内容零改动（无新增缺陷可修）。交付：print 11,189,525 B / 1e24a8deb37bfcba3ef7ac6cff92f26a21a545b7533dc3de1fa9557e3d265f0b，web 1,898,551 B / 9461e8bad39b96c04dd34d57453fc2bbbc5d6f1faf46535c58489a92b44d56d5。未 commit、未 push；独立重校待协调员另派。日志：hidden_files/w47/scratch-d5-zh-tw/logs/2026-w47-zh-tw-nl/。
- P7 金句修复 (2026-11-12, 独立重校 PROOF-NOTE 第 1 条，低严重度）: 仅改 content7.py:128 与 checks.py:19——P7 金句第 8 条「迪士尼聖誕，從11月17日開始」→「香港迪士尼聖誕，從11月17日開始」（补句首「香港」二字，与 P5 原句逐字一致；读者语译文不动）。重建 run/render/webpdf RC 皆 0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；head_check 0 缺陷；checks PASS；仅 p7-lang.svg 变化；quote-check 固定引文 2 处（P5+P7）、裸引文 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前新增 CJK 恰 {香:1, 港:1}；spill 0、boxtitle 0 DEFECT、edge 0/0、creambox PASS、D5 普查 PASS、引号普查 0 缺陷字；印/网文字层多重集差 0，修前→修后印层仅 +香/港；text.md 仅引文行 1 行改动（+6 B）。P8 行数 158→158、距页脚线余量 36.3px 不变。交付：print 11,189,718 B / 20ad418b233c…（确定性，两跑 SHA 相同），web 1,898,763 B / d28897aea142…，text.md 50,602 B / 487127dd7d72…。未 commit、未 push。日志：hidden_files/w47/scratch-fix-zh-tw/logs/2026-w47-zh-tw-nl/。
