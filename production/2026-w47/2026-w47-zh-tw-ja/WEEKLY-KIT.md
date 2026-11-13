# Lucerna Weekly — VOL.4 Traditional Chinese, Japanese explanations (W47)

## Edition identity

- **Pairing:** zh-tw × ja — Traditional Chinese text, explanations in Japanese, for Japanese-speaking readers.
- **Issue week:** Monday 2026-11-16 to Sunday 2026-11-22 (VOL.4).
- **Slug (insert):** 2026-w47-zh-tw-ja. **Edition dir:** `production/2026-w47/2026-w47-zh-tw-ja/` (build code + assets + PDFs + KIT + ABSTRACT.txt + text.md). Source: `production/2026-w47/core-zh-tw/` (read-only; nothing in the core was modified).
- **Masthead:** Lucerna (no article — Chinese is article-less), UnifrakturMaguntia 147pt (196px).
- **Top strip (P1):** left `VOL.4　繁體中文版`, centre `台灣　香港　台湾と香港`, right `2026年11月16日至11月22日` (17pt, full-width spaces).
- **Edition line (P1, 27pt bold, OLIVE):** `繁體中文週報　VOL.4　遊行　金馬獎　小雪` (unchanged from core — target-language line).
- **Badge line (P1, 16pt, GREY):** `繁體中文正文　日本語講解 — 繁体字中国語の本文と日本語の解説、日本語話者の読者のための版`
- **Lead headline (P1, 45pt):** `週日下午2點，封王遊行天母出發` (frozen core text).
- **Format:** 8 pages, 1462.5×2025 pt (1950×2700 px), 4 columns, newsprint paper #fbfaf6. Same geometry as core.
- **Level ramp:** A2 → B2, one level chip on every item (A2 #5c6e30 / B1 #46581f / B2 #37402f, white text).
- **Traditional Chinese is natively produced for the Taiwan/Hong Kong ecosystem.** Not converted or transcoded from any Simplified edition; no zh-cn text was copied or converted anywhere in this build. Only the explanation layer was rewritten into Japanese.

## SOP §1.1 measurements (this edition, measured on final SVGs/PDFs)

- Paper #fbfaf6 on all 8 pages. Gold/brick/near-black: 0 occurrences. No double-line outer frame. Badge colours present (A2 #5c6e30, B1 #46581f, B2 #37402f).
- Furniture uses full-width spaces (　); 「·」 appears only inside multiple-choice option lists, the P6 timeline legend, and chart dots — the same rule as the core KIT. Footer: `Lucerna　繁體中文週報 VOL.4　繁體中文正文　日本語講解`, page lines `第Nページ／全8ページ`.
- VOL.4 throughout; VOL.5 appears exactly once, in the P7 next-issue teaser head (`下期預告　来週 (VOL.5)`) — correct, not a misprint.
- P8 answer font size (PyMuPDF, measured 2026-11-11): keys at **9.75pt on both print and web PDFs** — exactly the SOP §1.1 floor (≥9.75pt). P8 stems stay at 13.8px = 10.35pt, per the core ruling.
- No drop cap (same recorded gap as core).
- P7 geometry (final build): col3 ends 1827.28, phrases strip fy=1851.3, teaser ends 2581.28 (footer rule 2596 — clear by 14.7px). P8 writing strip ends 1280.2, keys end inside the content bottom.

## Per-page contents (frozen core content; only the explanation layer is Japanese)

Same as core KIT: P1 Front (A2, 10 exercises); P2 Life (A2, 18); P3 Culture (A2→B1, 18); P4 Sport (B1, 18); P5 Youth (B1, 18); P6 Deep read (B2, 18); P7 Language focus (A2/B1/B2 + error clinic + 越…越… frame + readers' corner + phrases + VOL.5 teaser, 12 exercises); P8 Test & keys (38 items).

## Measured totals (registry, identical to core)

- **Total exercises: 150.** By level: A2 44 · B1 74 · B2 32. By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. By type: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.
- **Images per page:** P1 0, P2 1, P3 1, P4 1, P5 1, P6 0, P7 1, P8 1 — 6 photos total, same files/credits as core.
- **Charts:** P4 olive bars 90.0, 450.0, 900.0 px; P6 timeline dots cx 188.0, 695.21, 948.82, 1033.36, 1202.43.
- **PDFs (D5 rebuild 2026-11-12 + P7 金句修复 2026-11-12):** print `Lucerna-VOL4-JA.pdf` 16,365,954 bytes, SHA-256 dbbe03ab27b3a1a013647fa7a15e6453afcab416d5e40abfcd42495f7c88944a; web `Lucerna-VOL4-JA-web.pdf` 2,447,388 bytes (< 7 MB), SHA-256 660f93940fe899ab40bc82def399a0cb1b85a0d2d161826c42e97f184fd29b9e. Both 8 pages, 1462.5 × 2025 pt. (D5 交付：print 16,365,732 B / 1f61f431d75e…; web 2,447,140 B / 94b53a518bb0…。P7 修复：print +222 B、web +248 B，皆为「香港」二字所致。) (Pre-D5 final render: print 18,089,964 B / 73f623f8884296f8d23aa54e16b46bc10a40c22df24908047478a975fdd58ef8; web 2,562,633 B / d6fb61050f8485343b9a95e375633e9cc0dc47ca48b39b48755559ba8b0b7707 — 注：KIT 原登记 web 为 2,562,627 B / b5cd6ad0…，与交付文件差 6 字节，系 webpdf.py 每次重跑 SHA 浮动，见 core KIT 同注。)
- **Text layer:** pdftotext print 50,174 bytes / web 50,175 bytes (P7 修复后实测；修前 D5：50,168 / 50,169，+6 B 恰为「香港」二字）; character multiset difference 0 (the 1-byte gap is the same run-boundary whitespace artifact recorded in the core KIT — no character missing).
- **Text export:** `2026-w47-zh-tw-ja.text.md`, 53,759 bytes, SHA-256 6e5b4b81e13159fbcf37b0dc22668f056f69775c021fc7428a67f50fe2c42c51（修前 D5：53,753 B / e03a56ad7254…，仅引文行 +「香港」二字 +6 B）, exported from the edition's own SVG text layer in page order (source-side; never from a PDF). H1 `VOL.4 · 中国語（繁体字）テキスト · 日本語の解説` (W46 ja precedent). All 150 exercise numbers present; no English instruction leftovers.
- **ABSTRACT.txt** (Japanese, single line, no ASCII double quotes): starts `Lucerna Traditional Chinese weekly VOL.4、日本語で学ぶ人のための繁体字中国語週報、A2からB2、150問。今週は味全龍の優勝パレード、…` — real topics + A2からB2 + 150問.

## Trend and fact sources / image licenses

Identical to the core KIT (core-zh-tw/WEEKLY-KIT.md) — fan-out does not re-do trend research or change facts. Same 6 placed images with the same credits/licenses.

## Readers'-corner disclosure (P7, Japanese)

- Chinese (frozen): 「延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。」
- Japanese: "編集部の例文の手紙であり、本物の手紙ではない。延期のお知らせ：VOL.3では今号から本物の読者の手紙と第8版の最優秀作を掲載すると予告したが、締め切りまでに掲載できるものは届かなかった。そのため例文を掲載し、募集は引き続き行う。"
- No reader, letter, name, or quote is invented anywhere in this issue. The corner is labeled 「台北小讀者（編輯範例）」.

## Editorial red lines observed

- No international politics. Because the target is Chinese, Chinese domestic politics is also excluded.
- No anniversary used as a living trend.
- The Traditional Chinese body text contains no Simplified-only characters. See the `checks.py` note below — the SIMP_ONLY hits are Japanese kanji in the explanation layer, not Simplified Chinese in the text.

## Reproducible build

Build code lives in `production/2026-w47/2026-w47-zh-tw-ja/` (copied from core-zh-tw by `scratch-fanout-zh-tw/transform.py ja`, then patched as below). Content modules run only via the single one-process driver, never standalone. Run with the toolkit venv:

```
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ja
~/workspace/weekly-git/tools/venv/bin/python run.py
~/workspace/weekly-git/tools/venv/bin/python render.py
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg Lucerna-VOL4-JA-web.pdf
~/workspace/weekly-git/tools/venv/bin/python export_zhtw_textmd.py svg 2026-w47-zh-tw-ja.text.md "VOL.4 · 中国語（繁体字）テキスト · 日本語の解説"
```

Outputs: 8 SVGs in `svg/`, 8 full-page PNGs in `cards/`, print PDF `Lucerna-VOL4-JA.pdf`, web PDF `Lucerna-VOL4-JA-web.pdf`.

## Proofread record (self-check, before independent proofread)

- **Full self-proofread:** the extracted text of all 8 pages was read (rendered cards P1–P8 viewed page by page + text.md scan); every answer key re-derived against its question/article/chart; every date/weekday and arithmetic total re-checked (same totals as core); every glossed term confirmed present on its own page.
- **Occlusion audit:** `tools/occlusion_audit.py` selftest passed; final round **0 flags**.
- **P7 phrases:** all 8 at exactly 2 occurrences each (article + P7), via `checks.py` (the phrases and chart lines PASS; only the SIMP_ONLY line fails, see below).
- **Chart geometry:** `checks.py` PASS — P4 bars 90/450/900; P6 dots as above.
- **P8 keys:** `tools/p8.py extract --p8 svg/p8-test.svg --total 150` → noted set = 150 of 150; `p8.py compare` vs core → **CLEAN** (missing=[] extra_count=0 keydiff=[]). Answer values identical to core for all 150 items. Writing model 142 characters, inside the 120–180 band. P8 level chips: 38/38 exercises badged; items 113–150 each carry a chip (A2 8 · B1 20 · B2 10 on P8); F writing head `F　寫一寫　書いてみよう` present with its B2 chip on item 150.
- **Freeze:** `tools/freeze.py baseline` re-run reproduces **8/8 SVGs byte-identically** (direct sha256 comparison; all MATCH).
- **Web PDF:** `tools/webpdf.py` exit 0; 2,548,035 bytes (< 7 MB); text layer multiset difference 0 vs print; 8 pages. P8 min size 9.75pt on both PDFs.
- **§1.1 measurements:** paper/gold/brick/frame/badges/footer/separators/VOL as listed above; all pass.
- **Visual QA:** all 8 rendered cards viewed page by page — no overflow, no overlap, no footer collision, image/credit placement confirmed; P4/P6 charts re-viewed; P7 col3 (1827.28) and teaser (2581.28, clear of the 2596 footer rule by 14.7px) confirmed visually.
- **English-leak scan (whole edition):** every SVG text node compared against the core's — 0 strings identical to core English prose (the 6 known key-note leaks were patched in Japanese before the first full build; see "Fixes").

## Fixes applied during this build (all inside this edition dir only)

1. **6 untranslated P8 key notes — patched before the first full build.** Same shared table gap as de/fr/es/it/pt/nl/ru (see de KIT): `tables.py` has no ENTRIES for these 5 source strings. Japanese translations written in this edition's `content56.py` (keys 92/98/100) and `content8.py` (keys 117/134/138), answer values untouched: "式典は台北音楽センターです。" / "小雪は11月22日です。" / "4つの大きなイベントが同じ日曜日に重なります。" / "ポイントを集めることは集點です。"
2. **No P7 or head fixes were needed.** Build 1: run.py exit 0, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; P7 col3 ends 1827.28, teaser ends 2581.28 (clear of the footer rule). Japanese explanations are compact enough that the build passed on the first run — the only edition of the nine to need zero content fixes.
3. **Stale core files removed.** The copytree brought the core's `Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, and `2026-w47-zh-tw-en.text.md` into this dir; all three deleted (byte-identical to core). This dir now holds only the ja files.

## Known non-defects (measured, recorded, not fixed)

- **`checks.py` reports `CHECKS FAIL` on `SIMP_ONLY_HITS ['国', '学']` — this is a false positive by design, not a defect.** The two characters are Japanese kanji (shinjitai), not Simplified Chinese, and they occur in exactly three Japanese explanation strings, verified by context: (1) P1 badge line "繁体字中国語の本文と日本語の解説…" — "中国語" is the Japanese word for the Chinese language; (2) P3 note "高雄国際鋼雕芸術祭" — "国際" is the Japanese word for international, the festival's Japanese name; (3) P7 "パレードからは四つの便利な言葉が学べる" — "学べる" is the Japanese verb "to learn". No 国 or 学 appears in the Traditional Chinese body text. The SIMP_ONLY check cannot distinguish Japanese kanji from Simplified Chinese characters — any future ja edition will trip the same line; the correct reading is to verify the contexts, as done here.
- **P4 "野球のことば" head fits on one line** — unlike the two-line wrap in fr/es/it/pt/nl/ru; recorded, not a defect.
- **P5 cross-column fragment** — the first article's last line flows to the top of column 1; normal newspaper flow, same in core.
- **P8 stems 10.35pt** — per the core ruling; keys meet the 9.75pt floor.
- **text.md page headings in English** ("## Page 6 — Deep read" etc.) — the exporter's fixed format, identical in the core and the shipped W46 ja text.md; not a leak.
- **P7 col3 ends 1827.28** (1.28px past the nominal 1826 target) — teaser ends 2581.28, 14.7px clear of the footer rule; occlusion 0; visually confirmed.

## Re-fan-out (2026-11-11, this session — re-fanout rod)

- Core baseline (frozen, verified before rebuilding; core untouched — SHA re-verified after the build): print `Lucerna-VOL4.pdf` 19,420,552 B SHA-256 5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a; web `Lucerna-VOL4-web.pdf` 2,324,042 B SHA-256 1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240; text.md 49,798 B SHA-256 09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b (core re-proof #3 verdict (a) zero issues, 定稿).
- Method: the 9 old edition dirs were backed up whole to the builder's scratch (`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-ja/`, 41 files, file-list SHA-256 identical to the old production dirs; backup NOT deleted), then `transform.py ja` rebuilt this dir from the new core (mechanism table `scratch-fanout-zh-tw/tables.py`, 242 ENTRIES, with the 2026-11-11 patches: nl :273 Xiaoxue gloss 「Volgende zondag」→「Deze zondag」; D1 「this Sunday」 sweep de/fr/es/it/pt/nl/ja; M1/M2 values already in the table, verified). transform is one-shot — the old dir was removed before rebuilding. The stale core files the copytree brought in (`Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, `2026-w47-zh-tw-en.text.md`) were deleted after SHA verification, as in the first build.
- Hand-fixes re-applied (all verified by diffing the rebuilt files against the backup-old edition): every old hand-fix was already mirrored into the mechanism table or carried by the new core — bslib4.py/render.py 0 diffs; content diffs are core-parallel (D1 本週日, fix2 HK box/BABYMONSTER/取捨, fix5 D4 box 230→244, N4 夜間遊行) or table-driven fix1 values (M1/M2, D1 lang values, N2 P8 notes, ru N5/N6/N7, ja D-ja-2, ko M4/M5, it D3).
- Gates re-run on the rebuilt edition (2026-11-11, `scratch-refanout-zh-tw/gates.py ja final`): checks.py reports CHECKS FAIL only on SIMP_ONLY_HITS ['国', '学'] — verified false positive (see Known non-defects; occurrences are 中国語 ×2, 国際 ×1, 学べる ×1, all standard Japanese kanji); occlusion audit selftest passed, **0 flags**; P8 extract 150/150, compare vs core **CLEAN** (keydiff=[] missing=[]); canonical creambox full scan 36 boxes, 0 negative inside-only clearances (P7 min +12.4px; P7 toolbox clearances +40.5/+12.5/+14.0); boxtitle 36 boxes, 0 overruns, min title right margin 1.2px; print/web text-layer multiset diff 0; P8 keys 9.75pt on both PDFs (PyMuPDF); fill-in keys 54/54 from body text, answer keys 1–150 continuous; English-leak scan 0 deny hits; P6 18:30/19:00 timeline-label ink gap 0.6px (same hairline as the core precedent, no overlap); freeze baseline re-run reproduces **8/8 SVGs byte-identically**, core integrity OK.
- Supplementary PIL creambox scan: **STRADDLE 0** (old build: 0) — bilingual file-card titles whose ink extends past their borderless cream box's right edge by ~7–80px (the title is fully legible, no overlap with anything, occlusion 0). Not fixed in this fan-out: shortening the titles is a design/text decision for the coordinator (fix1) — recorded here, not hidden, not written as a pass.
- Visual QA: all 8 rendered cards viewed (contact sheet + P7 teaser and P4 D4 crops for de) — no overflow, no overlap, no footer collision, image/credit placement confirmed.

## Build history (this session, builder 7th rod)

- `transform.py ja` OK (244 lines).
- Build 1 (run.py exit 0, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE, P7 teaser 2581.28) — no fixes needed.
- Render exit 0; webpdf exit 0; text.md exported; all gates green except the documented `checks.py` SIMP_ONLY false positive (phrases and charts passed).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch `weekly-git` pushes or insert.py. Core files untouched.
- Re-fan-out rod (2026-11-11 ~10:43–11:50 UTC): rebuilt from the new core via transform.py; run.py exit 0 (0 FLOW OVERFLOW, no warnings); render + webpdf + text export exit 0; all gates re-run green per the section above (STRADDLE 0, old 0); KIT updated to the new SHAs. No commit, no push; proof1/proof2 by the coordinator separately.
- D5 rebuild (2026-11-12, SOP §1.1 讲解层字体修复）: `apply_variant.py --target zh-tw --reader ja`（mode cjk，按 CJK-DECISION.md §1 字符分流，不加 `_READER_LANG` 门）；svglib pre-D5 md5 9caa4651959673f511cd56873d93a04a（与 core 相同）；装机：Noto Sans faces + sans_noto cmaps/_PATH（Medium/Bold）+ fix2 块 + D5 sans 块 + `_D5_READER = "cjk"`；CJK index TC→JP，kinsoku 已在版内（skip port）。修前基线：重建 8/8 SVG 与交付字节一致，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；普查 D5 拉丁 276、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 18,668 字符一致。门禁全绿（stage1 一轮）：run TOTAL 150、0/0；head_check 0；occlusion 0 flags；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前基线新增 CJK 0；spill 0（146 OBSERVE）；boxtitle 0 DEFECT（25 titles）；edge 0/0；creambox PASS 0 defects（n=506，median 1.006，bold 1.040）；D5 普查 PASS（0/0/0）；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 18,668 字符）；text.md 与修前逐字节相同（e03a56ad…）。P8 行数 126→126、距页脚线余量 50.3→50.3px，无溢出风险。内容零改动（无新增缺陷可修）。交付：print 16,365,732 B / 1f61f431d75eb60ceb7d130f9e1f8498a812a1f0352d4cba6e50100955f81efc，web 2,447,140 B / 94b53a518bb0954494ef414b57ddbc678e173450d3c91d39ff0deeb8122d968c。未 commit、未 push；独立重校待协调员另派。日志：hidden_files/w47/scratch-d5-zh-tw/logs/2026-w47-zh-tw-ja/。
- P7 金句修复 (2026-11-12, 独立重校 PROOF-NOTE 第 1 条，低严重度）: 仅改 content7.py:128 与 checks.py:19——P7 金句第 8 条「迪士尼聖誕，從11月17日開始」→「香港迪士尼聖誕，從11月17日開始」（补句首「香港」二字，与 P5 原句逐字一致；读者语译文不动）。重建 run/render/webpdf RC 皆 0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；head_check 0 缺陷；checks.py 仅 SIMP_ONLY 一行 FAIL（见本 KIT 已记录的误报：日文汉字 中国語×2/国際×1/学べる×1，修前修后同一组；其余 8 条引文 2× 与两图核对皆 PASS）；仅 p7-lang.svg 变化；quote-check 固定引文 2 处（P5+P7）、裸引文 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前新增 CJK 恰 {香:1, 港:1}；spill 0、boxtitle 0 DEFECT、edge 0/0、creambox PASS、D5 普查 PASS、引号普查 0 缺陷字；印/网文字层多重集差 0，修前→修后印层仅 +香/港；text.md 仅引文行 1 行改动（+6 B）。P8 行数 126→126、距页脚线余量 50.3px 不变。交付：print 16,365,954 B / dbbe03ab27b3…（确定性，两跑 SHA 相同），web 2,447,388 B / 660f93940fe8…，text.md 53,759 B / 6e5b4b81e131…。未 commit、未 push。日志：hidden_files/w47/scratch-fix-zh-tw/logs/2026-w47-zh-tw-ja/。
