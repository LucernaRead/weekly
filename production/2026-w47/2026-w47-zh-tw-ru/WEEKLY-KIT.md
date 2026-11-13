# Lucerna Weekly — VOL.4 Traditional Chinese, Russian explanations (W47)

## Edition identity

- **Pairing:** zh-tw × ru — Traditional Chinese text, explanations in Russian, for Russian-speaking readers.
- **Issue week:** Monday 2026-11-16 to Sunday 2026-11-22 (VOL.4; `tools/tables.py vol 2026-W47` = 4).
- **Slug (insert):** 2026-w47-zh-tw-ru. **Edition dir:** `production/2026-w47/2026-w47-zh-tw-ru/` (build code + assets + PDFs + KIT + ABSTRACT.txt + text.md). Source: `production/2026-w47/core-zh-tw/` (read-only; nothing in the core was modified).
- **Masthead:** Lucerna (no article — Chinese is article-less), UnifrakturMaguntia 147pt (196px).
- **Top strip (P1):** left `VOL.4　繁體中文版`, centre `台灣　香港　ТАЙВАНЬ И ГОНКОНГ`, right `2026年11月16日至11月22日` (17pt, full-width spaces).
- **Edition line (P1, 27pt bold, OLIVE):** `繁體中文週報　VOL.4　遊行　金馬獎　小雪` (unchanged from core — target-language line).
- **Badge line (P1, 16pt, GREY):** `繁體中文正文　俄語講解 — Текст на традиционном китайском с пояснениями на русском языке, для русскоязычных читателей`
- **Lead headline (P1, 45pt):** `週日下午2點，封王遊行天母出發` (frozen core text).
- **Format:** 8 pages, 1462.5×2025 pt (1950×2700 px), 4 columns, newsprint paper #fbfaf6. Same geometry as core.
- **Level ramp:** A2 → B2, one level chip on every item (A2 #5c6e30 / B1 #46581f / B2 #37402f, white text).
- **Traditional Chinese is natively produced for the Taiwan/Hong Kong ecosystem.** Not converted or transcoded from any Simplified edition; no zh-cn text was copied or converted anywhere in this build. Only the explanation layer was rewritten into Russian.

## SOP §1.1 measurements (this edition, measured on final SVGs/PDFs)

- Paper #fbfaf6 on all 8 pages. Gold/brick/near-black: 0 occurrences. No double-line outer frame. Badge colours present (A2 #5c6e30, B1 #46581f, B2 #37402f).
- Furniture uses full-width spaces (　); 「·」 appears only inside multiple-choice option lists, the P6 timeline legend, and chart dots — the same rule as the core KIT. Footer: `Lucerna　繁體中文週報 VOL.4　繁體中文正文　俄語講解`, page lines `Страница N из 8`.
- VOL.4 throughout; VOL.5 appears exactly once, in the P7 next-issue teaser head (`下期預告　На следующей неделе (VOL.5)`) — correct, not a misprint.
- P8 answer font size (PyMuPDF, measured 2026-11-11): keys at **9.75pt on both print and web PDFs** — exactly the SOP §1.1 floor (≥9.75pt). P8 stems stay at 13.8px = 10.35pt, per the core ruling.
- No drop cap (same recorded gap as core).
- P7 geometry (final build): col3 ends 1823.3, phrases strip fy=1847.3, teaser ends 2577.3 (footer rule 2596 — clear by 18.7px). P8 writing strip ends 1280.2, keys end inside the content bottom.

## Per-page contents (frozen core content; only the explanation layer is Russian)

Same as core KIT: P1 Front (A2, 10 exercises); P2 Life (A2, 18); P3 Culture (A2→B1, 18); P4 Sport (B1, 18); P5 Youth (B1, 18); P6 Deep read (B2, 18); P7 Language focus (A2/B1/B2 + error clinic + 越…越… frame + readers' corner + phrases + VOL.5 teaser, 12 exercises); P8 Test & keys (38 items).

## Measured totals (registry, identical to core)

- **Total exercises: 150.** By level: A2 44 · B1 74 · B2 32. By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. By type: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.
- **Images per page:** P1 0, P2 1, P3 1, P4 1, P5 1, P6 0, P7 1, P8 1 — 6 photos total, same files/credits as core.
- **Charts:** P4 olive bars 90.0, 450.0, 900.0 px; P6 timeline dots cx 188.0, 695.21, 948.82, 1033.36, 1202.43.
- **PDFs (fix-xru rebuild 2026-11-12):** print `Lucerna-VOL4-RU.pdf` 11,291,943 bytes, SHA-256 8c3aca16ea41ed1cd8f5eb6174861c30ce4db1536cbf14427a8bd08aa901e2f5; web `Lucerna-VOL4-RU-web.pdf` 1,997,666 bytes (< 7 MB), SHA-256 04606730a740e008fe427e69859c1e90a911f2872ec6079b8df75a135421afa1. Both 8 pages, 1462.5 × 2025 pt. Note: the print PDF is smaller than the other editions' (~11.2 MB) — the rendered cards are identical in size and the text layer is complete (D5 textcheck: print/web/pre-print multiset diff 0, 24,960 chars each); the difference is image embedding in the PDF, not missing content. Web PDF 1,997,666 bytes (Cyrillic UTF-8 is 2 bytes per letter, hence a larger text layer than Latin editions' ~48k). (D5 交付：print 11,366,251 B / d80b9ee5df60…; web 2,070,745 B / d255e31ad059…。P7 修复：print +220 B、web +249 B，皆为「香港」二字所致。) (Pre-D5 final render: print 12,896,273 B / 367828a6a0257ffdf05f862d44ccc10f483726a9d5ae399599c3a1b9304b375a; web 2,007,963 B / 3def68758fd905a7a90962b1bf91352f50853057083e70205205987128d30209.) (Pre-fix-xru: print 11,366,471 B / eb3fd9aae5e2…; web 2,070,994 B / 16a6d20a755e… — see fix-xru section at the end.)
- **Text layer:** pdftotext print 58,554 bytes / web 58,555 bytes (P7 修复后实测；修前 D5：58,548 / 58,549，+6 B 恰为「香港」二字）; character multiset difference 0 (the 1-byte gap is the same run-boundary whitespace artifact recorded in the core KIT — no character missing).
- **Text export:** `2026-w47-zh-tw-ru.text.md`, 62,498 bytes, SHA-256 ea9c1514df967cd8e8a324d2037c6c15460a33b451318bc07b09d7e764a81c32（修前 D5：62,492 B / 2fb4b97ef37d…，仅引文行 +「香港」二字 +6 B）, exported from the edition's own SVG text layer in page order (source-side; never from a PDF). H1 `VOL.4 · Тексты на китайском (традиционном) · Объяснения на русском` (W46 ru precedent). All 150 exercise numbers present; no English instruction leftovers.
- **ABSTRACT.txt** (Russian, single line, no ASCII double quotes): starts `Lucerna Traditional Chinese weekly VOL.4 для изучающих язык на русском, A2–B2, 150 упражнений: …` — real topics + A2–B2 + 150 упражнений.

## Trend and fact sources / image licenses

Identical to the core KIT (core-zh-tw/WEEKLY-KIT.md) — fan-out does not re-do trend research or change facts. Same 6 placed images with the same credits/licenses.

## Readers'-corner disclosure (P7, Russian)

- Chinese (frozen): 「延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。」
- Russian: "Письмо-образец редакции, не настоящее письмо: VOL.3 обещал письма читателей и лучшие сочинения со страницы 8 с этого номера; к сдаче ни одного пригодного письма не поступило. Образец остаётся, приглашение открыто."
- No reader, letter, name, or quote is invented anywhere in this issue. The corner is labeled 「台北小讀者（編輯範例）」.

## Editorial red lines observed

- No international politics. Because the target is Chinese, Chinese domestic politics is also excluded.
- No anniversary used as a living trend.
- No Simplified-only characters in Traditional text (`checks.py` SIMP_ONLY_HITS []).

## Reproducible build

Build code lives in `production/2026-w47/2026-w47-zh-tw-ru/` (copied from core-zh-tw by `scratch-fanout-zh-tw/transform.py ru`, then patched as below). Content modules run only via the single one-process driver, never standalone. Run with the toolkit venv:

```
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ru
~/workspace/weekly-git/tools/venv/bin/python run.py
~/workspace/weekly-git/tools/venv/bin/python render.py
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg Lucerna-VOL4-RU-web.pdf
~/workspace/weekly-git/tools/venv/bin/python export_zhtw_textmd.py svg 2026-w47-zh-tw-ru.text.md "VOL.4 · Тексты на китайском (традиционном) · Объяснения на русском"
```

Outputs: 8 SVGs in `svg/`, 8 full-page PNGs in `cards/`, print PDF `Lucerna-VOL4-RU.pdf`, web PDF `Lucerna-VOL4-RU-web.pdf`.

## Proofread record (self-check, before independent proofread)

- **Full self-proofread:** the extracted text of all 8 pages was read (rendered cards P1–P8 viewed page by page + text.md scan); every answer key re-derived against its question/article/chart; every date/weekday and arithmetic total re-checked (same totals as core); every glossed term confirmed present on its own page.
- **Occlusion audit:** `tools/occlusion_audit.py` selftest passed. Build 2: **1 flag (P8 TEXTX)** — the answers head overlapped the right-side note; fixed (see "Fixes") and re-audited: final round **0 flags**.
- **P7 phrases:** all 8 at exactly 2 occurrences each (article + P7), via `checks.py` (PASS).
- **Simplified-character audit:** zero hits (`checks.py` PASS).
- **Chart geometry:** `checks.py` PASS — P4 bars 90/450/900; P6 dots as above.
- **P8 keys:** `tools/p8.py extract --p8 svg/p8-test.svg --total 150` → noted set = 150 of 150; `p8.py compare` vs core → **CLEAN** (missing=[] extra_count=0 keydiff=[]). Answer values identical to core for all 150 items. Writing model 142 characters, inside the 120–180 band. P8 level chips: 38/38 exercises badged; items 113–150 each carry a chip (A2 8 · B1 20 · B2 10 on P8); F writing head `F　寫一寫　Письмо` present with its B2 chip on item 150.
- **Freeze:** `tools/freeze.py baseline` re-run reproduces **8/8 SVGs byte-identically** (direct sha256 comparison; all MATCH).
- **Web PDF:** `tools/webpdf.py` exit 0; 1,993,092 bytes (< 7 MB); text layer multiset difference 0 vs print; 8 pages. P8 min size 9.75pt on both PDFs.
- **§1.1 measurements:** paper/gold/brick/frame/badges/footer/separators/VOL as listed above; all pass.
- **Visual QA:** all 8 rendered cards viewed page by page — no overflow, no overlap, no footer collision, image/credit placement confirmed; P4/P6 charts re-viewed; P7/P8 re-viewed after fixes.
- **English-leak scan (whole edition):** every SVG text node compared against the core's — 0 strings identical to core English prose (the 6 known key-note leaks were patched in Russian before the first full build; see "Fixes").

## Fixes applied during this build (all inside this edition dir only)

1. **6 untranslated P8 key notes — patched before the first full build.** Same shared table gap as de/fr/es/it/pt/nl (see de KIT): `tables.py` has no ENTRIES for these 5 source strings. Russian translations written in this edition's `content56.py` (keys 92/98/100) and `content8.py` (keys 117/134/138), answer values untouched: "Церемония — в Тайбэйском музыкальном центре." / "Сяосюэ — 22 ноября." / "Четыре больших события приходятся на одно воскресенье." / "Накапливать баллы — это 集點。"
2. **4 section heads too wide (build 1 → build 2).** Build 1 warned 4 × HEAD TOO WIDE — P4 "看圖答題　Прочитайте диаграмму" 426.2px, P6 "看圖答題　Прочитайте шкалу времени" 484.1px, P6 "深讀測驗　Тест по глубокому чтению" 461.0px, P8 D "Прочитайте и ответьте" 450.7px (at 21px) — all over the 422.5px column. Fixed: "Чтение диаграммы" (370.8px), "Чтение шкалы" (311.8px), "Тест по чтению" (320.3px), "Чтение и ответы" (382.3px). Build 2: 0 HEAD TOO WIDE. All four shortened heads mirrored into `tables.py` (ru column only). Lesson recorded: the P4 head lives in `content34.py`, not `content4.py` — my first patch attempt died on the wrong filename before writing anything, while the tables.py mirror had already been applied, leaving a temporary table/edition divergence; corrected by re-patching with the right filename.
3. **P7 col3 overflow, worst of the family (build 1 → build 2).** Build 1: col3 ended 1968.0, teaser ended 2722.0 (126px past the footer rule) — Russian is the longest language so far: lcn 10 lines, wcn 3 lines, wt 5 lines. Fixed in `content7.py` (explanation layer only): readers'-corner Russian disclosure 10 → 7 lines, 越…越… frame example 5 → 4 lines, wcn 3 → 2 lines ("Составьте фразу."). Result: col3 ends 1823.3, teaser ends 2577.3 (clear by 18.7px), occlusion 0 flags. The three shortened Russian strings mirrored into `tables.py` (ru column only). All candidate strings were measured before applying.
4. **P8 answers-head overlap (build 2 → build 3).** Occlusion found 1 TEXTX flag: the answers head "答案　Ответы — в порядке страниц, с коротким примечанием на русском к каждому пункту" (1171.3px at 25px) overlapped the right-side note "Все примечания на русском　✓ = образец письменного задания" (~654.8px) by 8.5×20.5px. Fixed in `content8.py`: "答案　Ответы — по страницам, с примечанием к каждому пункту" (830.3px). Re-audit: 0 flags. Mirrored into `tables.py` (ru column only). Build 3 (final) re-rendered, re-webpdf'd, re-exported; all gates green.
5. **Stale core files removed.** The copytree brought the core's `Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, and `2026-w47-zh-tw-en.text.md` into this dir; all three deleted (byte-identical to core). This dir now holds only the ru files.
6. **Fix2 U+201C port (2026-11-12; full record in `hidden_files/w47/scratch-gatefix-u201c-ru/FIX-LOG.md`).** Ported the core-de fix2 font-routing patch (commit 4ac7192c) into this edition's `svglib.py` (the older variant without `_CYR`/`sans_noto` rows — adapted minimally, same routing block + `_PATH` rows). U+201C/U+201D/U+2019 now route through the serif branch to Newsreader (their advance in Noto Sans CJK TC is 1.000em; Newsreader's is 0.44/0.44/0.26em). Pre-patch `svglib.py` md5 `9caa4651959673f511cd56873d93a04`; post-patch md5 `b9e9effff652539c08f7bf2ff3bbfd74`; diff is only the ported block (verified: py_compile passes, reverse-patch reproduces the pre-patch md5). SVG census before: 4 defective glyphs (P5 `“` ×1 in `«Мире „Холодного сердца“»`, 18pt, Noto Sans CJK TC; P8 `“` ×3 in the `«Мире „Холодного сердца“»` test notes, 13.0pt); after: 0 defective, quotes now Newsreader. Rebuilt via `tools/run_build.py` (two independent builds) + `tools/webpdf.py`; synced `svg/` + `cards/` + print + web PDFs into production. text.md SHA UNCHANGED (`2fb4b97e…`, 62,492 B). Print PDF `1dbe1d8e…` 12,896,218 B → `367828a6…` 12,896,273 B; web PDF `d9b4d129…` 2,007,910 B → `3def6875…` 2,007,963 B. (Note: the KIT's previous web SHA `cb05eba2…` was already stale before this fix — the on-disk web PDF carried `d9b4d129…` from a concurrent webpdf rebuild; this fix now records the file it built.) Gates green: run.py exit 0 / TOTAL 150, zero overflow; p8 extract 150/150, compare vs core-zh-tw CLEAN (keydiff []); `checks.py` exit 0; occlusion audit 0 flags; freeze 8/8 SVG SHA match between the two builds + print PDFs byte-identical; freeze baseline 8/8 on the synced files; print/web text layers byte-identical per page (29,211 chars; pdftotext 58,537 / 58,538 bytes); word-join census 107/174, token-set identical to the pre-fix production census, 0 real joins; spill 0; boxtitle 0 DEFECT (with the production pre-fix build as baseline); P8 `notes.jpg` image unchanged (422.5×200 at y=559).

## Known non-defects (measured, recorded, not fixed)

- **P3 "金馬小檔 «Золотая лошадь»: коротко" head sits tight against its box's right edge** — within the box, occlusion 0, no overflow warning; recorded here.
- **P4 "Слова бейсбола" head wraps to two lines** ("棒球詞卡" / "Слова бейсбола") — wraps within its column, no overflow warning, no overlap; slightly awkward typography, recorded here.
- **P5 cross-column fragment** — the first article's last line flows to the top of column 1; normal newspaper flow, same in core.
- **P8 stems 10.35pt** — per the core ruling; keys meet the 9.75pt floor.
- **text.md page headings in English** ("## Page 6 — Deep read" etc.) — the exporter's fixed format, identical in the core and the shipped W46 ru text.md; not a leak.
- **Print PDF 12.9 MB vs ~20 MB for the other editions** — cards identical in size, text layer complete; image embedding difference only (see "Measured totals").

## Re-fan-out (2026-11-11, this session — re-fanout rod)

- Core baseline (frozen, verified before rebuilding; core untouched — SHA re-verified after the build): print `Lucerna-VOL4.pdf` 19,420,552 B SHA-256 5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a; web `Lucerna-VOL4-web.pdf` 2,324,042 B SHA-256 1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240; text.md 49,798 B SHA-256 09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b (core re-proof #3 verdict (a) zero issues, 定稿).
- Method: the 9 old edition dirs were backed up whole to the builder's scratch (`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-ru/`, 41 files, file-list SHA-256 identical to the old production dirs; backup NOT deleted), then `transform.py ru` rebuilt this dir from the new core (mechanism table `scratch-fanout-zh-tw/tables.py`, 242 ENTRIES, with the 2026-11-11 patches: nl :273 Xiaoxue gloss 「Volgende zondag」→「Deze zondag」; D1 「this Sunday」 sweep de/fr/es/it/pt/nl/ja; M1/M2 values already in the table, verified). transform is one-shot — the old dir was removed before rebuilding. The stale core files the copytree brought in (`Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, `2026-w47-zh-tw-en.text.md`) were deleted after SHA verification, as in the first build.
- Hand-fixes re-applied (all verified by diffing the rebuilt files against the backup-old edition): every old hand-fix was already mirrored into the mechanism table or carried by the new core — bslib4.py/render.py 0 diffs; content diffs are core-parallel (D1 本週日, fix2 HK box/BABYMONSTER/取捨, fix5 D4 box 230→244, N4 夜間遊行) or table-driven fix1 values (M1/M2, D1 lang values, N2 P8 notes, ru N5/N6/N7, ja D-ja-2, ko M4/M5, it D3).
- Gates re-run on the rebuilt edition (2026-11-11, `scratch-refanout-zh-tw/gates.py ru final`): checks.py PASS; occlusion audit selftest passed, **0 flags**; P8 extract 150/150, compare vs core **CLEAN** (keydiff=[] missing=[]); canonical creambox full scan 36 boxes, 0 negative inside-only clearances (P7 min +12.5px; P7 toolbox clearances +40.5/+12.5/+14.0); boxtitle 36 boxes, 0 overruns, min title right margin 22.5px; print/web text-layer multiset diff 0; P8 keys 9.75pt on both PDFs (PyMuPDF); fill-in keys 54/54 from body text, answer keys 1–150 continuous; English-leak scan 0 deny hits; P6 18:30/19:00 timeline-label ink gap 0.6px (same hairline as the core precedent, no overlap); freeze baseline re-run reproduces **8/8 SVGs byte-identically**, core integrity OK.
- Supplementary PIL creambox scan: **STRADDLE 4** (old build: 5) — bilingual file-card titles whose ink extends past their borderless cream box's right edge by ~7–80px (the title is fully legible, no overlap with anything, occlusion 0). The old build had 5; one (the P4 D4-box bottom-crossing question line) was fixed by the core fix5 D4 box 230→244 — the remaining 4 are identical to the old build. Not fixed in this fan-out: shortening the titles is a design/text decision for the coordinator (fix1) — recorded here, not hidden, not written as a pass. **FIXED by the D5 rebuild (2026-11-12) — by size reduction, not text shortening (pilot precedent):** P2 `耶誕城小檔　Крисмасленд: коротко` 25→21（余 25.8px）、P3 `金馬小表　«Золотая лошадь»: коротко` 25→19（余 27.3px）、P3 `鋼雕閉幕行程　Последние выходные` 25→20（余 31.7px）、P5 `迪士尼聖誕小檔　Дисней: коротко` 25→22（余 31.7px）；boxtitle 0 DEFECT、creambox PASS 0 defects。文字一字未动。
- Visual QA: all 8 rendered cards viewed (contact sheet + P7 teaser and P4 D4 crops for de) — no overflow, no overlap, no footer collision, image/credit placement confirmed.

## Build history (this session, builder 7th rod)

- `transform.py ru` OK (244 lines).
- Build 1 (run.py exit 0, 0 FLOW OVERFLOW, 4 HEAD TOO WIDE, P7 teaser 2722.0) — fixed (fixes 2–3 above).
- Build 2 (run.py exit 0, 0 warnings; render exit 0; webpdf exit 0) — occlusion found 1 P8 TEXTX flag; fixed (fix 4 above). Note: the first render attempt was interrupted by the runtime (returned "aborted", cards written but no PDF); a second attempt timed out at dispatch; the third attempt (plain foreground exec) completed rc=0. No exit 120 / memory error occurred.
- Build 3 (final): run.py exit 0, 0 warnings; render exit 0; webpdf exit 0; text.md re-exported; all gates green (occlusion 0, p8 150/150 CLEAN, checks PASS, freeze 8/8, leak scan 0, P8 9.75pt both PDFs, text multiset diff 0).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch `weekly-git` pushes or insert.py. Core files untouched.
- Re-fan-out rod (2026-11-11 ~10:43–11:50 UTC): rebuilt from the new core via transform.py; run.py exit 0 (0 FLOW OVERFLOW, no warnings); render + webpdf + text export exit 0; all gates re-run green per the section above (STRADDLE 4, old 5); KIT updated to the new SHAs. No commit, no push; proof1/proof2 by the coordinator separately.
- Build 4 (fix2 U+201C port rebuild, 2026-11-12): `svglib.py` ported to route U+201C/U+201D/U+2019 to Newsreader (md5 `9caa4651…` → `b9e9efff…`); run.py exit 0 / TOTAL 150; render + webpdf exit 0; all 17 gates green (see Fixes item 6 for the full record). KIT updated to the new SHAs. No commit, no push.
- D5 rebuild (2026-11-12, SOP §1.1 讲解层字体修复）: `apply_variant.py --target zh-tw --reader ru`（mode ru，`_D5_READER = "ru"`：拉丁+西里尔进 Noto Sans Medium/Bold；fix2 已在版内，installer 未重复装）；svglib pre-D5 md5 `b9e9efff…`（fix2 后；与 core 的 pre-D5 md5 不同，因本版已做 fix2 移植）。修前基线：重建 8/8 SVG 与交付字节一致，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；普查 D5 拉丁 272、西里尔 480、弯引号 CJK 0（弯引号 5 个全在 Newsreader）；引号普查 0 缺陷字；印/网文字层各 24,960 字符一致。修的缺陷 5 项（文字一字未动，只降字号）：(1–4) 4 个 25pt 手绘奶油框标题越框右缘：P2 `耶誕城小檔　Крисмасленд: коротко` +45.5px，content12.py:190 字号 25→21，余 25.8px；P3 `金馬小表　«Золотая лошадь»: коротко` +90.5px（墨水越过页缘，occlusion EDGE + edge P3 TOUCH 同一处），content34.py:76 字号 25→19，余 27.3px；P3 `鋼雕閉幕行程　Последние выходные` +60.5px，content34.py:93 字号 25→20，余 31.7px；P5 `迪士尼聖誕小檔　Дисней: коротко` +18.5px，content56.py:81 字号 25→22，余 31.7px。(5) P7 下期预告越页脚线：D5 后俄文 sans 变宽（常规中位 +3.4%），P7 第 3 栏读者园地盒 lh +28.4px（披露俄文 7→8 行）+ 诊所盒 eh +26.52px（俄文 gloss 1→2 行），col3 1823.3→1878.2，预告盒底 2577.3→2632.2，预告文字 baseline 2598.22、墨水底 2600.5 越过页脚线 2596（occlusion FOOTER/LINEX 各 3 处；修前备份 occlusion 0 flags，确为 D5 引起）；content7.py 诊所俄文 sans 19.5→19（恢复 1 行）、披露俄文 sans 20→19（恢复 7 行），col3/teaser 精确回到基线 1823.3/2577.3。门禁全绿（stage2 终轮）：run TOTAL 150、0/0；head_check 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前基线新增 CJK 0；spill 0（146 OBSERVE）；boxtitle 0 DEFECT；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=557，median 1.029，bold 0.956——西里尔粗体反变窄，符合 ru 读者版方向）；D5 普查 PASS（0/0/0，Noto Sans 元素 1014，ru 路由真实触发）；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 24,960 字符）；text.md 与修前逐字节相同（2fb4b97e…）。P8 行数 174→172、距页脚线余量 38.7→35.7px。交付：print 11,366,251 B / d80b9ee5df60b982eb1ae4fffe026a0cc33703292f589765b5776baa7a6af524，web 2,070,745 B / d255e31ad059a2c4f1595d75b99aba3f140faa2b1fcc138d2b55a0fa80865610。未 commit、未 push；独立重校待协调员另派。日志：hidden_files/w47/scratch-d5-zh-tw/logs/2026-w47-zh-tw-ru/。
- P7 金句修复 (2026-11-12, 独立重校 PROOF-NOTE 第 1 条，低严重度）: 仅改 content7.py:128 与 checks.py:19——P7 金句第 8 条「迪士尼聖誕，從11月17日開始」→「香港迪士尼聖誕，從11月17日開始」（补句首「香港」二字，与 P5 原句逐字一致；读者语译文不动）。重建 run/render/webpdf RC 皆 0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；head_check 0 缺陷；checks PASS；仅 p7-lang.svg 变化；quote-check 固定引文 2 处（P5+P7）、裸引文 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前新增 CJK 恰 {香:1, 港:1}；spill 0、boxtitle 0 DEFECT、edge 0/0、creambox PASS、D5 普查 PASS、引号普查 0 缺陷字；印/网文字层多重集差 0，修前→修后印层仅 +香/港；text.md 仅引文行 1 行改动（+6 B）。P8 行数 172→172、距页脚线余量 35.7px 不变。交付：print 11,366,471 B / eb3fd9aae5e2…（确定性，两跑 SHA 相同），web 2,070,994 B / 16a6d20a755e…，text.md 62,498 B / ea9c1514df96…。未 commit、未 push。日志：hidden_files/w47/scratch-fix-zh-tw/logs/2026-w47-zh-tw-ru/。

## fix-xru (2026-11-12, *-ru font-routing repair)

- **Defect:** `svglib.py` `_D5_READER == "ru"` branch routed Latin text to Noto Sans CJK, violating SOP §1.1 (Latin → Newsreader, Cyrillic → Noto Sans).
- **Fix:** deleted the `_D5_READER == "ru"` branch (marker `[removed 2026-11-12 fix-xru]`); Latin now always takes the else path to Newsreader, Cyrillic stays on Noto Sans. Patch applied by the previous worker; this round only rebuilt.
- **Probe (probe_xru.py):** pre — `runs=3594 LAT@NotoSans=518 LAT@Newsreader=343 CYR@NotoSans=10623 CYR@Newsreader=0`; post — `runs=5705 LAT@NotoSans=0 LAT@Newsreader=861 CYR@NotoSans=10623 CYR@Newsreader=0`. LAT@NotoSans 518 → 0; CYR@NotoSans unchanged (10623).
- **Rebuild:** `driver.sh zh-tw` (`run.py` TOTAL 150 RC 0, 0 HEAD TOO WIDE → probe RC 0 → `render.py` RC 0 → text-layer multiset gate IDENTICAL, 24,962 non-space chars → `webpdf.py` RC 0). Print PDF mtime 2026-11-12 23:52:11 UTC, 8 pages. Web PDF 8 pages, 1,997,666 B. No retry. All 8 SVGs differ from pre-fix (expected — font routing changed).
- **New SHAs (verified on production files):** print `8c3aca16ea41ed1cd8f5eb6174861c30ce4db1536cbf14427a8bd08aa901e2f5` (11,291,943 B); web `04606730a740e008fe427e69859c1e90a911f2872ec6079b8df75a135421afa1` (1,997,666 B); text.md unchanged `ea9c1514df967cd8e8a324d2037c6c15460a33b451318bc07b09d7e764a81c32` (62,498 B).
- **Old SHAs (pre-fix, history):** print `eb3fd9aae5e20a23cec347bee2830e8a867cf2eaaa63fa29a9752b88bdecabb7` (11,366,471 B); web `16a6d20a755eec2e5a39587085469df55bb8d1455234b0203b9121955d7c1c3e` (2,070,994 B).
- Logs: `hidden_files/w47/scratch-fix-xru-w47/` (`build-zh-tw.log`, `summary-zh-tw.txt`, `logs/zh-tw-*.log`, `probe-post-zh-tw.json`).
