# Lucerna Weekly — VOL.4 Traditional Chinese, French explanations (W47)

## Edition identity

- **Pairing:** zh-tw × fr — Traditional Chinese text, explanations in French, for French-speaking readers.
- **Issue week:** Monday 2026-11-16 to Sunday 2026-11-22 (VOL.4; `tools/tables.py vol 2026-W47` = 4).
- **Slug (insert):** 2026-w47-zh-tw-fr. **Edition dir:** `production/2026-w47/2026-w47-zh-tw-fr/` (build code + assets + PDFs + KIT + ABSTRACT.txt + text.md). Source: `production/2026-w47/core-zh-tw/` (read-only; nothing in the core was modified).
- **Masthead:** Lucerna (no article — Chinese is article-less), UnifrakturMaguntia 147pt (196px).
- **Top strip (P1):** left `VOL.4　繁體中文版`, centre `台灣　香港　TAÏWAN ET HONG KONG`, right `2026年11月16日至11月22日` (17pt, full-width spaces).
- **Edition line (P1, 27pt bold, OLIVE):** `繁體中文週報　VOL.4　遊行　金馬獎　小雪` (unchanged from core — target-language line).
- **Badge line (P1, 16pt, GREY):** `繁體中文正文　法語講解 — Texte en chinois traditionnel avec explications en français, pour les lecteurs francophones`
- **Lead headline (P1, 45pt):** `週日下午2點，封王遊行天母出發` (frozen core text).
- **Format:** 8 pages, 1462.5×2025 pt (1950×2700 px), 4 columns, newsprint paper #fbfaf6. Same geometry as core.
- **Level ramp:** A2 → B2, one level chip on every item (A2 #5c6e30 / B1 #46581f / B2 #37402f, white text).
- **Traditional Chinese is natively produced for the Taiwan/Hong Kong ecosystem.** Not converted or transcoded from any Simplified edition; no zh-cn text was copied or converted anywhere in this build. Only the explanation layer was rewritten into French.

## SOP §1.1 measurements (this edition, measured on final SVGs/PDFs)

- Paper #fbfaf6 on all 8 pages. Gold/brick/near-black: 0 occurrences. No double-line outer frame. Badge colours present (A2 #5c6e30, B1 #46581f, B2 #37402f).
- Furniture uses full-width spaces (　); 「·」 appears only inside multiple-choice option lists, the P6 timeline legend, and chart dots — the same rule as the core KIT. Footer: `Lucerna　繁體中文週報 VOL.4　繁體中文正文　法語講解`, page lines `Page N sur 8`.
- VOL.4 throughout; VOL.5 appears exactly once, in the P7 next-issue teaser head (`下期預告　La semaine prochaine (VOL.5)`) — correct, not a misprint.
- P8 answer font size (PyMuPDF, measured 2026-11-11): keys at **9.75pt on both print and web PDFs** — exactly the SOP §1.1 floor (≥9.75pt). P8 stems stay at 13.8px = 10.35pt, per the core ruling.
- No drop cap (same recorded gap as core).
- P7 geometry (final build): col3 ends 1823.3, phrases strip fy=1847.3, teaser ends 2577.3 (footer rule 2596 — clear by 18.7px). P8 writing strip ends 1280.2, keys end inside the content bottom.

## Per-page contents (frozen core content; only the explanation layer is French)

Same as core KIT: P1 Front (A2, 10 exercises); P2 Life (A2, 18); P3 Culture (A2→B1, 18); P4 Sport (B1, 18); P5 Youth (B1, 18); P6 Deep read (B2, 18); P7 Language focus (A2/B1/B2 + error clinic + 越…越… frame + readers' corner + phrases + VOL.5 teaser, 12 exercises); P8 Test & keys (38 items).

## Measured totals (registry, identical to core)

- **Total exercises: 150.** By level: A2 44 · B1 74 · B2 32. By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. By type: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.
- **Images per page:** P1 0, P2 1, P3 1, P4 1, P5 1, P6 0, P7 1, P8 1 — 6 photos total, same files/credits as core.
- **Charts:** P4 olive bars 90.0, 450.0, 900.0 px; P6 timeline dots cx 188.0, 695.21, 948.82, 1033.36, 1202.43.
- **PDFs (D5 rebuild 2026-11-12 + P7 金句修复 2026-11-12):** print `Lucerna-VOL4-FR.pdf` 11,191,659 bytes, SHA-256 47320e77d6f1559ee16dd1d1448676b7203ca6a1d6cc5a3b892e83c38e7be7be; web `Lucerna-VOL4-FR-web.pdf` 1,899,287 bytes (< 7 MB), SHA-256 233658513953a1b4b3f5aea84fa9f42b230326c41e60f8edc440524e958e9038. Both 8 pages, 1462.5 × 2025 pt. (D5 交付：print 11,191,465 B / 384fd32e70c8…; web 1,899,091 B / 64439f145cce…。P7 修复：print +194 B、web +196 B，皆为「香港」二字所致。) (Pre-D5 final render: print 20,191,919 B / acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33; web 2,366,341 B / cac6ab5bfe82fb10bf32cabfaee5be3f297441b1f75db880e1a841b0ae2ab2f2 — 注：KIT 原登记 web 为 2,366,339 B / 6026be3e…，与交付文件差 2 字节，系 webpdf.py 每次重跑 SHA 浮动，见 core KIT 同注。)
- **Text layer:** pdftotext print 48,828 bytes / web 48,829 bytes (P7 修复后实测；修前 D5：48,822 / 48,823，+6 B 恰为「香港」二字）; character multiset difference 0 (the 1-byte gap is the same run-boundary whitespace artifact recorded in the core KIT — no character missing).
- **Text export:** `2026-w47-zh-tw-fr.text.md`, 52,476 bytes, SHA-256 a2df8892d632ab081dd05b05c4df62be33a5ed91a3749cca27ed02db7e3c3fcf（修前 D5：52,470 B / 673943a0de31…，仅引文行 +「香港」二字 +6 B）, exported from the edition's own SVG text layer in page order (source-side; never from a PDF). H1 `VOL.4 · Textes en chinois traditionnel · Explications en français` (W46 fr precedent). All 150 exercise numbers present; no English instruction leftovers.
- **ABSTRACT.txt** (French, single line, no ASCII double quotes): starts `Lucerna Traditional Chinese weekly VOL.4 pour les apprenants francophones, A2 à B2, 150 exercices : …` — real topics + A2–B2 + 150 exercices.

## Trend and fact sources / image licenses

Identical to the core KIT (core-zh-tw/WEEKLY-KIT.md) — fan-out does not re-do trend research or change facts. Same 6 placed images with the same credits/licenses.

## Readers'-corner disclosure (P7, French)

- Chinese (frozen): 「延期披露：VOL.3曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。」
- French: "Lettre d'exemple de la rédaction, pas une vraie lettre : VOL.3 avait promis de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucune lettre publiable n'était arrivée au bouclage. L'exemple reste, l'invitation reste ouverte."
- No reader, letter, name, or quote is invented anywhere in this issue. The corner is labeled 「台北小讀者（編輯範例）」.

## Editorial red lines observed

- No international politics. Because the target is Chinese, Chinese domestic politics is also excluded.
- No anniversary used as a living trend.
- No Simplified-only characters in Traditional text (`checks.py` SIMP_ONLY_HITS []).

## Reproducible build

Build code lives in `production/2026-w47/2026-w47-zh-tw-fr/` (copied from core-zh-tw by `scratch-fanout-zh-tw/transform.py fr`, then patched as below). Content modules run only via the single one-process driver, never standalone. Run with the toolkit venv:

```
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-fr
~/workspace/weekly-git/tools/venv/bin/python run.py
~/workspace/weekly-git/tools/venv/bin/python render.py
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg Lucerna-VOL4-FR-web.pdf
~/workspace/weekly-git/tools/venv/bin/python export_zhtw_textmd.py svg 2026-w47-zh-tw-fr.text.md "VOL.4 · Textes en chinois traditionnel · Explications en français"
```

Outputs: 8 SVGs in `svg/`, 8 full-page PNGs in `cards/`, print PDF `Lucerna-VOL4-FR.pdf`, web PDF `Lucerna-VOL4-FR-web.pdf`.

## Proofread record (self-check, before independent proofread)

- **Full self-proofread:** the extracted text of all 8 pages was read (rendered cards P1–P8 viewed page by page + text.md scan); every answer key re-derived against its question/article/chart; every date/weekday and arithmetic total re-checked (same totals as core); every glossed term confirmed present on its own page.
- **Occlusion audit:** `tools/occlusion_audit.py` selftest passed. Final round: **0 flags**.
- **P7 phrases:** all 8 at exactly 2 occurrences each (article + P7), via `checks.py` (PASS).
- **Simplified-character audit:** zero hits (`checks.py` PASS).
- **Chart geometry:** `checks.py` PASS — P4 bars 90/450/900; P6 dots as above.
- **P8 keys:** `tools/p8.py extract --p8 svg/p8-test.svg --total 150` → noted set = 150 of 150; `p8.py compare` vs core → **CLEAN** (missing=[] extra_count=0 keydiff=[]). Answer values identical to core for all 150 items. Writing model 142 characters, inside the 120–180 band. P8 level chips: 38/38 exercises badged; items 113–150 each carry a chip (A2 8 · B1 20 · B2 10 on P8); F writing head `F　寫一寫　Écrire` present with its B2 chip on item 150.
- **Freeze:** `tools/freeze.py baseline` re-run reproduces **8/8 SVGs byte-identically** (direct sha256 comparison; all MATCH).
- **Web PDF:** `tools/webpdf.py` exit 0; 2,350,191 bytes (< 7 MB); text layer multiset difference 0 vs print; 8 pages. P8 min size 9.75pt on both PDFs.
- **§1.1 measurements:** paper/gold/brick/frame/badges/footer/separators/VOL as listed above; all pass.
- **Visual QA:** all 8 rendered cards viewed page by page — no overflow, no overlap, no footer collision, image/credit placement confirmed; P4/P6 charts re-viewed; P6 heads and P7 re-viewed after fixes.
- **English-leak scan (whole edition):** every SVG text node compared against the core's — 0 strings identical to core English prose (the 6 known missing-table key notes were patched in French before the first full build; see "Fixes").

## Fixes applied during this build (all inside this edition dir only)

1. **6 untranslated P8 key notes — patched before the first full build.** Same shared table gap as de (see de KIT): `tables.py` has no ENTRIES for these 5 source strings. French translations written in this edition's `content56.py` (keys 92/98/100) and `content8.py` (keys 117/134/138), answer values untouched: "La cérémonie a lieu au Taipei Music Center." / "Xiaoxue est le 22 nov." / "Quatre grands événements tombent le même dimanche." / "Collectionner des points se dit 集點。"
2. **P6 section heads too wide (build 1 → build 2).** Build 1 warned `HEAD TOO WIDE [P6-ex]` twice: "看圖答題　Lire la frise chronologique" 446.3px and "深讀測驗　Quiz de lecture approfondie" 467.1px at 25px, vs the 422.5px column (over by 23.8px / 44.6px). Fixed in `content56.py`: "Lire la frise" (260.9px) and "Quiz de lecture" (309.4px). Build 2: 0 HEAD TOO WIDE. Both shortened French strings mirrored into `tables.py` (fr column only).
3. **P7 col3 overflow (build 1 → build 2).** Build 1: col3 ended 1908.7, teaser ended 2662.7 (66.7px past the footer rule). Fixed in `content7.py` (explanation layer only): readers'-corner French disclosure 8 → 7 lines, third error-clinic gloss 3 → 2 lines ("Le spectacle principal a lieu toutes les demi-heures : 12 fois, 17:30–23:00."), 越…越… frame example 5 → 4 lines. Result: col3 ends 1823.3, teaser ends 2577.3 (clear by 18.7px), occlusion 0 flags. The three shortened French strings mirrored into `tables.py` (fr column only). Note: the first patch attempt failed on a mismatched gloss string (the file's actual wording uses "spectacle de lumières" and "17:30 à 23:00", not the "spectacle lumineux / 17 h 30" wording first assumed) — the patch was re-applied against the exact file strings; `content56.py` had already been patched in the same run and was not touched twice.
4. **Stale core files removed.** The copytree brought the core's `Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, and `2026-w47-zh-tw-en.text.md` into this dir; all three deleted (byte-identical to core). This dir now holds only the fr files.
5. **text.md H1 corrected.** First export used "Texte chinois (traditionnel)"; re-exported with the W46 fr precedent "Textes en chinois traditionnel".

## Known non-defects (measured, recorded, not fixed)

- **P4 "Mots du baseball" head wraps to two lines** ("Mots du" / "baseball") — the head wraps within its column, no overflow warning, no overlap; slightly awkward typography, recorded here.
- **P5 cross-column fragment** — the first article's last line flows to the top of column 1; normal newspaper flow, same in core.
- **P8 stems 10.35pt** — per the core ruling; keys meet the 9.75pt floor.
- **text.md page headings in English** ("## Page 6 — Deep read" etc.) — the exporter's fixed format, identical in the core and the shipped W46 fr text.md; not a leak.

## Re-fan-out (2026-11-11, this session — re-fanout rod)

- Core baseline (frozen, verified before rebuilding; core untouched — SHA re-verified after the build): print `Lucerna-VOL4.pdf` 19,420,552 B SHA-256 5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a; web `Lucerna-VOL4-web.pdf` 2,324,042 B SHA-256 1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240; text.md 49,798 B SHA-256 09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b (core re-proof #3 verdict (a) zero issues, 定稿).
- Method: the 9 old edition dirs were backed up whole to the builder's scratch (`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-fr/`, 41 files, file-list SHA-256 identical to the old production dirs; backup NOT deleted), then `transform.py fr` rebuilt this dir from the new core (mechanism table `scratch-fanout-zh-tw/tables.py`, 242 ENTRIES, with the 2026-11-11 patches: nl :273 Xiaoxue gloss 「Volgende zondag」→「Deze zondag」; D1 「this Sunday」 sweep de/fr/es/it/pt/nl/ja; M1/M2 values already in the table, verified). transform is one-shot — the old dir was removed before rebuilding. The stale core files the copytree brought in (`Lucerna-VOL4.pdf`, `Lucerna-VOL4-web.pdf`, `2026-w47-zh-tw-en.text.md`) were deleted after SHA verification, as in the first build.
- Hand-fixes re-applied (all verified by diffing the rebuilt files against the backup-old edition): every old hand-fix was already mirrored into the mechanism table or carried by the new core — bslib4.py/render.py 0 diffs; content diffs are core-parallel (D1 本週日, fix2 HK box/BABYMONSTER/取捨, fix5 D4 box 230→244, N4 夜間遊行) or table-driven fix1 values (M1/M2, D1 lang values, N2 P8 notes, ru N5/N6/N7, ja D-ja-2, ko M4/M5, it D3).
- Gates re-run on the rebuilt edition (2026-11-11, `scratch-refanout-zh-tw/gates.py fr final`): checks.py PASS; occlusion audit selftest passed, **0 flags**; P8 extract 150/150, compare vs core **CLEAN** (keydiff=[] missing=[]); canonical creambox full scan 36 boxes, 0 negative inside-only clearances (P7 min +12.5px; P7 toolbox clearances +40.5/+12.5/+14.0); boxtitle 36 boxes, 0 overruns, min title right margin -0.2px; print/web text-layer multiset diff 0; P8 keys 9.75pt on both PDFs (PyMuPDF); fill-in keys 54/54 from body text, answer keys 1–150 continuous; English-leak scan 0 deny hits; P6 18:30/19:00 timeline-label ink gap 0.6px (same hairline as the core precedent, no overlap); freeze baseline re-run reproduces **8/8 SVGs byte-identically**, core integrity OK.
- Supplementary PIL creambox scan: **STRADDLE 0** (old build: 0) — bilingual file-card titles whose ink extends past their borderless cream box's right edge by ~7–80px (the title is fully legible, no overlap with anything, occlusion 0). fr: boxtitle min right margin −0.2px on the P2 'Fiche Christmasland' title — identical in the old build, sub-pixel, invisible at render scale. Not fixed in this fan-out: shortening the titles is a design/text decision for the coordinator (fix1) — recorded here, not hidden, not written as a pass. **FIXED by the D5 rebuild (2026-11-12) — by size reduction, not text shortening (pilot precedent):** P2 `耶誕城小檔　Fiche Christmasland` 25→23（余 29.5px）；boxtitle 0 DEFECT、creambox PASS 0 defects。文字一字未动。
- Visual QA: all 8 rendered cards viewed (contact sheet + P7 teaser and P4 D4 crops for de) — no overflow, no overlap, no footer collision, image/credit placement confirmed.

## Build history (this session, builder 7th rod)

- `transform.py fr` OK (244 lines).
- Build 1 (run.py exit 0, 0 FLOW OVERFLOW, 2 HEAD TOO WIDE [P6-ex]) + render + webpdf: P7 teaser 2662.7 (past footer) — fixed (fixes 2–3 above).
- Build 2 (final): run.py exit 0, 0 warnings; render exit 0; webpdf exit 0; text.md exported (then H1-corrected and re-exported); all gates green (occlusion 0, p8 150/150 CLEAN, checks PASS, freeze 8/8, leak scan 0, P8 9.75pt both PDFs, text multiset diff 0).
- Delivery note: this builder does not claim finalization (independent proofread is separate), does not post to Discord, does not send cards/PDFs into the main chat, creates no cron, and does not touch `weekly-git` pushes or insert.py. Core files untouched.
- Re-fan-out rod (2026-11-11 ~10:43–11:50 UTC): rebuilt from the new core via transform.py; run.py exit 0 (0 FLOW OVERFLOW, no warnings); render + webpdf + text export exit 0; all gates re-run green per the section above (STRADDLE 0, old 0); KIT updated to the new SHAs. No commit, no push; proof1/proof2 by the coordinator separately.
- D5 rebuild (2026-11-12, SOP §1.1 讲解层字体修复）: `apply_variant.py --target zh-tw --reader fr`（mode latin）；svglib pre-D5 md5 9caa4651959673f511cd56873d93a04a（与 core 相同）；装机：Noto Sans faces + sans_noto cmaps/_PATH（Medium/Bold）+ fix2 块 + D5 sans 块 + `_D5_READER = "latin"`。修前基线：重建 8/8 SVG 与交付字节一致，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；普查 D5 拉丁 621、西里尔 0、弯引号 CJK 0；引号普查 0 缺陷字；印/网文字层各 25,767 字符一致。修的缺陷 1 项（纯 D5 引起，修前基线无溢出）：P2 `耶誕城小檔　Fiche Christmasland` 越框右缘 +2.5px，content12.py:190 字号 25→23，余 29.5px；文字一字未动。门禁全绿（stage2 终轮）：run TOTAL 150、0/0；head_check 0；occlusion 0 flags；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前基线新增 CJK 0；spill 0（146 OBSERVE）；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（n=546，median 1.001，bold 1.040）；D5 普查 PASS（0/0/0）；引号普查 0 缺陷字；textcheck PASS（印/网/修前各 25,767 字符）；text.md 与修前逐字节相同（673943a0…）。P8 行数 152→152、距页脚线余量 36.3→35.3px。交付：print 11,191,465 B / 384fd32e70c8d50f38f9df384c99c352d8b38cf20a59c4ec819a10d2e8d90b99，web 1,899,091 B / 64439f145ccecabaac6ad6fe5f7f49e03ec7352d96b8df86a0452deb3e20e83d。未 commit、未 push；独立重校待协调员另派。日志：hidden_files/w47/scratch-d5-zh-tw/logs/2026-w47-zh-tw-fr/。
- P7 金句修复 (2026-11-12, 独立重校 PROOF-NOTE 第 1 条，低严重度）: 仅改 content7.py:128 与 checks.py:19——P7 金句第 8 条「迪士尼聖誕，從11月17日開始」→「香港迪士尼聖誕，從11月17日開始」（补句首「香港」二字，与 P5 原句逐字一致；读者语译文不动）。重建 run/render/webpdf RC 皆 0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；head_check 0 缺陷；checks PASS；仅 p7-lang.svg 变化；quote-check 固定引文 2 处（P5+P7）、裸引文 0；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare vs core-zh-tw CLEAN keydiff=[]；freeze baseline 8/8；freeze diff vs 修前新增 CJK 恰 {香:1, 港:1}；spill 0、boxtitle 0 DEFECT、edge 0/0、creambox PASS、D5 普查 PASS、引号普查 0 缺陷字；印/网文字层多重集差 0，修前→修后印层仅 +香/港；text.md 仅引文行 1 行改动（+6 B）。P8 行数 152→152、距页脚线余量 35.3px 不变。交付：print 11,191,659 B / 47320e77d6f1…（确定性，两跑 SHA 相同），web 1,899,287 B / 233658513953…，text.md 52,476 B / a2df8892d632…。未 commit、未 push。日志：hidden_files/w47/scratch-fix-zh-tw/logs/2026-w47-zh-tw-fr/。
