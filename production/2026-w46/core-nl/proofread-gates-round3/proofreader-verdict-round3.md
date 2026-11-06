# Proofreader Verdict — Round 3 (FULL round, all 11 editions)
## Lucerna Weekly W46 — NL target, dated Mon 2026-11-09 to Sun 2026-11-15, 2026, VOL.3

**Proofreader:** independent, Round 3. Did not build or fix these editions. No edition file was edited, re-rendered, pushed, inserted, or posted; `~/workspace/weekly-git` and `index.json` untouched. All gate artifacts saved under `hidden_files/w46/nl-proofread-gates-round3/` (`run_gates.sh`, `checks.py`, `checks.log`, `counts.json`, `freeze-*.json`, `p8-*.json`, `p8-extract-*.json`, `occlusion-*.json`, `occlusion-*-vs-core.json`, `hashes-now.json`, `residue_sweep.py`, `residue-sweep.log`, `gates-freeze-p8.log`, `gates-occlusion.log`).

**Editions (11):** `2026-w46-nl-de, -en, -es, -fr, -it, -ja, -ko, -pt, -ru, -zh-cn, -zh-tw`. The directory `files/weekly-report-w46-nl-core/` IS the zh-cn edition; it is not a 12th edition. Each edition: 8 SVG pages, `*-web.pdf`, `<slug>.text.md`, `ABSTRACT.txt`, `WEEKLY-KIT.md`.

**Basis:** SOP (`files/weekly-report-SOP.md`, read in full), Round 2 verdict (`hidden_files/w46/nl-proofread-gates-round2/proofreader-verdict-round2.md`), Round 1 fix record (`hidden_files/w46/nl-fix/FIX-REPORT.md`), Round 3 fix record (`hidden_files/w46/nl-fix-round3/FIX-REPORT.md` + `residue-candidates.txt`, read but not relied on unexamined), shared toolkit (`tools/freeze.py`, `tools/p8.py`, `tools/occlusion_audit.py`, `tools/webpdf.py` rules). Every gate below was re-run independently by the proofreader on the final artifacts; no fix-worker JSON was trusted.

---

## 1. Per-edition verdict

| Edition | Verdict |
|---|---|
| 2026-w46-nl-de | **PASS** |
| 2026-w46-nl-en | **PASS** |
| 2026-w46-nl-es | **PASS** |
| 2026-w46-nl-fr | **PASS** |
| 2026-w46-nl-it | **PASS** |
| 2026-w46-nl-ja | **PASS** |
| 2026-w46-nl-ko | **PASS** |
| 2026-w46-nl-pt | **PASS** |
| 2026-w46-nl-ru | **PASS** |
| 2026-w46-nl-zh-cn (core) | **PASS** |
| 2026-w46-nl-zh-tw | **PASS** |

## 2. Fix verification

### N-1 — core (zh-cn) P8 item 103 note — CONFIRMED (fixed)
- Rendered core P8 SVG element, x=989, y=2210.1200000000013, single element, 1 line: `103. B — 入城式是圣诞老人的隆重到来`. Key B correct. No orphan.
- Core `.text.md` diff vs the pre-fix copy (`hidden_files/w46/nl-fix-round3/before/textmd/2026-w46-nl-zh-cn.text.md`): exactly 1 line (line 360), `隆重 arrival` → `隆重到来`, −2 bytes (39,152 bytes / 469 lines now).
- `arrival` occurrences over ALL SVG text of ALL 11 editions: ONLY in EN, 14 occurrences, all legitimate native English (e.g. EN P1 gloss `de intocht = arrival`, P7 `festive arrival`, P8 item 103 `festive arrival`, item 137 `Compare with`). Zero in the core/zh-cn edition outside EN.
- All 10 other editions' item-103 notes verified fully native and unchanged in wording class: de `103. B — Der intocht ist Sinterklaas' festlicher Einzug`; en `103. B — The intocht is Sinterklaas's festive arrival`; es `103. B — La intocht es la llegada festiva de Sinterklaas`; fr `103. B — L'intocht est l'arrivée festive de Sinterklaas`; it `103. B — L'intocht è l'arrivo festoso di Sinterklaas`; ja `103. B — intochtとはシンタクラースの祝祭の到着のこと`; ko `103. B — intocht는 신터클라스의 축제 도착이에요`; pt `103. B — A intocht é a chegada festiva do Sinterklaas`; ru `103. B — Intocht — это праздничное прибытие Синтерклааса`; zh-tw `103. B — intocht 是辛特克拉斯的慶典進城`.

### N-2 — FR P8 item 137 note — CONFIRMED (fixed)
- FR P8, x=1451: line 1 y=1930.48 `137. Le journal de Sinterklaas passe chaque jour à 18 h 00. —`, line 2 y=1945.04 `Comparez avec l'article page 3`. Same 2-line break as claimed. Translation key correct. No orphan.
- FR `.text.md` diff vs pre-fix copy: exactly 1 line (line 455), `Compare avec` → `Comparez avec`, +1 byte (41,119 bytes / 479 lines now). All other 9 non-core editions: ZERO `.text.md` diff lines.
- `Compare` occurrences: only EN `Compare with…` (plus EN P8 `compared directly`) and FR `Comparez…` (plus FR `peut pas les comparer directement`, a legitimate French verb). Zero `Compare avec` remains anywhere.
- All other editions' item-137 answer notes verified native: core `137. 圣诞老人新闻每天 18:00 播出。 — 对照第 3 版文章`; de `… — Mit dem Artikel auf Seite 3 vergleichen` (2 lines); en `… — Compare with the page 3 article` (2 lines); es `… — Compara con el artículo de la página 3`; it `… — Confronta con l'articolo di pagina 3`; ja `… — 3ページの記事と比べよう` (2 lines); ko `… — 3면 기사와 비교해 보세요` (2 lines); pt `… — Compara com o artigo da página 3`; ru `… — Сравни со статьёй на странице 3` (2 lines); zh-tw `… — 對照第 3 版文章`.

### Round 1 fix survival — all CONFIRMED surviving
- **F-1 (abstracts):** all 11 `ABSTRACT.txt` read in full — practice-framed, single-line, 0 ASCII double-quotes, native language, topics + A2–B2 + 150 exercises. Hash-identical to the Round 2 state.
- **F-2a (core P2 lone `。`/`更` deletion, ACCEPTED per Round 2):** core P2 EN JIJ box at x=1473 now exactly 2 lines (`11 月 11 日你会提灯笼挨家唱歌，还是爱看` / `圣诞老人新闻？写两句荷兰语寄给编辑部。`); orphan scan: 0 lone `。`, 0 line-start `。` in all 11 editions. Acceptance stands; not re-raised.
- **F-2b (core + zh-tw P6 gloss, both ACCEPTED per Round 2):** core P6 gloss 3 lines at x=1007 (`译注｜de traditie 传统 · griezelen 吓人 ·` / `de belangstelling 兴趣· de achteruitgang` / `衰退 · de deskundige 专家。`); zh-tw identical in Traditional (`譯注｜de traditie 傳統 · griezelen 嚇人 ·` / `de belangstelling 關注· de achteruitgang` / `衰退 · de deskundige 專家。`). Acceptances stand; not re-raised.
- **E-1 (fr/pt P3 bridge):** fr single line x=989 y=1954.5 `Calcule : réponds par les chiffres de la page 3.`; pt `Calcula: responde com números da página 3.` — CONFIRMED.
- **E-2 (zh-tw P6 caption):** x=1473 y=242 `DE GRAFIEK · 圖表（練習數據）` and y=660.86 `練習數據：虛構數字，僅供練習，非真實調查。` — CONFIRMED.
- **E-3 (zh-tw P8 H-intro):** x=1451 y=562.77 `寫作題（無唯一答案）；範文（89 詞）見下。` — CONFIRMED.
- Survival is additionally bounded by the hash comparison (§5): every P2/P3/P6 SVG and the zh-tw P8 SVG are byte-identical to the Round 2 state in which Round 2 confirmed these fixes. Observation O-R2-1 (tightened separator `兴趣· de`, non-blocking, unchanged bytes) not re-raised.

### Independent residue sweep — NO third candidate; NO new defect
Own method (`residue_sweep.py`, 4 passes over all SVG text + abstracts of all 11 editions; own wordlists, fix worker's script not used):
- **Pass 1** (broad English wordlist over full SVG text of all non-EN editions): 1,534 hits, every distinct word adjudicated clean: `is` (1,050, Dutch verb), `week` (270, Dutch word in frozen furniture), `over` (80, Dutch preposition), `page/pages` (34, French), `am` (25, German), `no` (24, Spanish negation / Portuguese contraction), `do` (20, Portuguese), `we` (10, Dutch pronoun in frozen dialogue stem item 149), `i` (8, Italian article), `arrive` (5, French), `question` (2, French), `all` (1 EN native + IT elisions — EN `See pages 2–4 for all dates and times.`, IT `all'11 novembre`, `all'ordinale 88e`), `also/her/so/was/article` (German/French words in their own editions). Zero `arrival` outside EN, zero `Compare` outside EN/FR-`Comparez`.
- **Pass 2** (edition-only strings, per-page multiset diff vs core, scanned against distinctive function-word lists of every other language): 28 hits, all shared homographs in their own language (DE genitive `des`, ES `se une`, PT `para/está/das`, FR `son`) — clean.
- **Pass 3** (script-leak scan): 0 out-of-script characters in every edition (Cyrillic outside RU 0, kana outside JA 0, Hangul outside KO 0, CJK outside JA/KO/zh-cn/zh-tw 0).
- **Pass 4** (abstracts read in full): see F-1 above — clean.
- Latin tokens in JA/KO/RU/zh-tw added strings: 195–218 distinct tokens each, ALL Dutch (quoted headwords, frozen furniture, P7 grammar quotes) or proper names (`Nations League`, `Halloween`, `RTL`, `PSV`, `LED`, `Stengs`) — no English residue.
- **Candidate list: empty.** No stray English word in a non-English explanation (or vice versa) beyond adjudicated legitimate keeps (proper names, quoted foreign headwords the issue glosses, P7 verbatim foreign quotes, frozen furniture).

## 3. Flagged items (a)–(d) — rulings

**(a) JA KIT freeze total 3,340 vs tasked 3,341 — RULED: 3,340 is CORRECT.** Independent `freeze.py diff` on the final artifacts: JA added CJK 3,340, distinct 327 (hiragana 1005, katakana 1161, han 1041, CJK punctuation/fullwidth 133). Recomputed sum from `freeze-ja.json` `cjk_added_total` = 3,340. Round 2 measured 3,341 (han 1042). The −1 reconciles exactly with N-1: the core P8 gained `到来`, core P8 `到` count is now 5 (JA P8: 10), core all-pages `到` 8 vs JA 17. Writing 3,341 into the JA KIT on current artifacts would be wrong; the fix worker correctly wrote 3,340. The JA KIT §7/record lines stating 3,340 (lines 125–126, 158) are correct. The remaining `3,341` at KIT line 162 sits inside the copied Round 1 fix-record's historical re-gate evidence (Round 1-era measurement, same figure Round 2 measured); it is a historical record, not a live claim — no correction required.

**(b) RU KIT §9 still states 809,219 while §7 states 809,218 — RULED: record-only inconsistency; NO correction required for shipping; do NOT fail.** §7 (KIT line 99) is verified correct: `De-Lucerna-VOL3-RU-web.pdf` (809,218 bytes, 55,313 text bytes) — matches the measured artifact exactly (809,218 B; pdftotext 55,313 bytes). §9 (line 144) still states 809,219 with the same correct 55,313 text bytes: a stale ±1 rebuild-drift figure. The artifact is correct; only the KIT's §9 drift figure is stale. If the KIT is touched again, update §9 to 809,218 for consistency. The KIT's own record-correction line (169) correctly notes the §7 text-bytes figure 55,344 was stale vs measured 55,313.

**(c) Hash-isolation ambiguity ("19 changed" vs "4 KITs changed") — RECONCILED.** My own hash comparison of all 231 files against `hidden_files/w46/nl-fix-round3/before/hashes-before.json` (Round 2 state): **23 files differ total = 19 artifact files + 4 KIT files.** The 19 artifacts are exactly: core (`.text.md`, `svg/p8-toets.svg`, `cards/p8-toets.png`, print PDF, web PDF) and fr (same 5), plus all 9 other editions' web PDFs only. All other 212 files byte-identical, including every P1–P7 SVG/card and all 9 other editions' SVGs and print PDFs. The 9 web PDFs differ by font-subsetting drift ONLY: extracted-text byte counts are identical to the Round 2 values for all 9 (de 46,586; en 45,597; es 46,675; it 46,429; ja 47,973; ko 47,853; pt 46,689; ru 55,313; zh-tw 44,455) AND web==print extracted text is identical in all 11 editions. Pre-fix web PDF bytes were not preserved, so byte-level PDF diffing against Round 2 is impossible; the text-identity evidence is the proof chain. Web PDF sizes now match the Round 3 fix-report inventory exactly (core 1,325,908; de 774,922; en 768,074; es 776,057; fr 772,218; it 768,441; ja 1,375,362; ko 1,083,985; pt 781,803; ru 809,218; zh-tw 1,615,015). The fix worker's `hashes-after.json` matches my current hashes for all files EXCEPT the 4 KITs (core, fr, ja, ru) — consistent with KIT edits landing after that snapshot. KIT content diffs verified line-by-line (§2, §3a–b): core §1 badge wording rewrite + Round 3 record; fr Round 3 record; JA §7/record freeze lines (3,340); RU §7 rewrite (809,218 / 55,313). No other KIT lines changed.

**(d) `.text.md` byte-size mismatch vs Round 1 inventory (core 39,152 vs 32,305) — RULED: pre-existing record inconsistency; content claim CONFIRMED; record-only.** Current sizes/line counts: core 39,152 / 469; de 40,803 / 479; en 40,086 / 479; es 40,920 / 479; fr 41,119 / 479; it 41,504 / 479; ja 42,143 / 481; ko 42,381 / 481; pt 40,849 / 479; ru 50,678 / 481; zh-tw 39,213 / 469. Diffs vs the pre-fix copies at task start: fr exactly 1 line (line 455, see §2 N-2); the other 9 non-core editions ZERO diff lines; core exactly 1 line (line 360, see §2 N-1). The content is verified by the 1-line diffs, not by the Round 1 table; the Round 1 inventory sizes do not describe the pre-fix copies. No artifact issue.

## 4. Full key-letter verification — 150/150 CORRECT

**Core (zh-cn) `.text.md` read in full (469 lines); every key 1–150 verified semantically** against the Dutch articles, grammar, and recomputed arithmetic. Result: **150/150 CORRECT**. Adjudicated points (none is a key error): item 6 `zetten` (plural subject); item 53 `kwartfinales` (plural required); item 60 `zijn gekomen` (perfect of `komen` with `zijn`; exercise targets the perfectum); item 100 `Kiezen hoeft niet: het zijn twee feesten.` (colon acceptable); item 127 repeats item 92's stem/options/key verbatim (design repetition, same correct key B); item 111 `gaat` (verb-first main clause after `als`, separable `gaat…aan`).

**Arithmetic recomputed:** 43: 14−9=5; 44: 15−9=6; 45: 16:00−12:00=4h; 46: 2026−2009=17; 83: 40; 84: 25; 85: 40+20=60; 86: 15; 87: 40+25+20+15=100. All correct.

**Matching blocks (quoted, option-by-option):**
- P2 items 25–28: stems `de lampion`, `delen`, `de mantel`, `het erfgoed`; options a. `licht delen met anderen, eten delen`, b. `een papieren lichtje voor 11 november`, c. `wat een land bewaart uit het verleden`, d. `een lange jas tegen de kou`; keys 25→b, 26→a, 27→d, 28→c; bijection complete.
- P8 items 141–144: stems `het journaal`, `de intocht`, `de lampion`, `delen`; options a. `een papieren lichtje voor 11 november`, b. `een dagelijks nieuwsprogramma op televisie`, c. `licht en eten geven aan anderen`, d. `de feestelijke aankomst van Sinterklaas`; keys 141→b, 142→d, 143→a, 144→c; bijection complete.

**All 11 editions' P8 renderings:** programmatic per-key diff of the `p8-extract-*.json` files against the core keys — in every one of the 10 fan-outs exactly 2 items differ, ONLY 137 and 138 (the legal translation re-aims, adjudicated in Round 2; both translations re-verified correct in every edition, see §2 and the item-138 dump below). All letter keys (A/B/C, matching a/b/c/d, Waar/Niet waar) and all Dutch fill-in keys are identical to core in every edition, including items 139/140. Item-138 notes in all 11 editions read and verified as correct native translations (core `138. 圣马丁节是分享的节日。 — 第 2 版原句 · delen 分享`; de `… — Originalsatz von Seite 2 · delen = teilen`; en `… — Original sentence from page 2 · delen = to share`; es `… — Frase original de la página 2 · delen = compartir`; fr `… — Phrase d'origine, page 2 · delen = partager`; it `… — Frase originale da pagina 2 · delen = condividere`; ja `… — 2ページの原文 · delen = 分け合う`; ko `… — 2면 원문 · delen = 나누다`; pt `… — Frase original da página 2 · delen = partilhar`; ru `… — Оригинальное предложение со страницы 2 · delen — делиться`; zh-tw `… — 第 2 版原句 · delen = 分享`). The rendered core P8 answer list was eyeballed against the `.text.md` keys. **Key verification: 150/150 in the core and 150/150 in each of the 10 fan-outs (modulo the two legal re-aims). No wrong key letter anywhere — no blocking defect.**

## 5. Re-gates (independently re-run on final artifacts)

- **Freeze (`tools/freeze.py diff`, all exit 0):** core self-diff +0/−0 all pages, added CJK 0; per-page CJK totals [196, 220, 141, 136, 217, 184, 379, 1146] — P8 1,146 = 1,144+2, reconciling N-1 (`到来`). Latin + RU editions (de/en/es/fr/it/pt/ru) with `--strict-cjk`: added CJK 0, edition CJK total 0. JA added 3,340 (see §3a). KO added 3,581 (3,571 Hangul + 10 CJK punctuation `『』`, distinct 321, 0 Han). zh-tw added 1,238 (distinct 273); simplified-only spot scan: 0 hits (curated simplified-only set; core sanity control 126 hits).
- **P8 (`tools/p8.py`):** core extract 150/150. All 10 fan-out compares CLEAN, missing=[], extra=0, keydiff=[137,138] (legal re-aims, §4).
- **Occlusion (`tools/occlusion_audit.py`):** selftest OK on every run (all 6 planted classes fired, clean controls silent). 0 flags in all 11 edition-alone runs; 0 new flags in all 10 `--core` NEW-vs-core runs. All 21 JSONs verified programmatically (`flag_count=0`, `new_flag_count=0`).
- **Counts:** total 150 in every edition; text.md bracketed items 142 (missing exactly range-header items 25–28, 141–144); levels bracketed 43/72/27 + 4 A2 + 4 B2 = A2 47 / B1 72 / B2 31; per-page totals 10/18/18/18/18/18/12/38; SVG stems 142, no missing, no dupes; SVG per-page [10,14,18,18,18,18,12,34]. Core types: 完成句子 65, 单选 44, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1. Other editions' type labels are native (DE German, EN/PT English, IT Italian, JA Japanese, RU Russian, zh-tw Traditional) except ES/FR text.md files still use Chinese type labels and KO merges choice+cloze as `객관식` 57 = 44+13 — a manuscript-label note from Round 2, not reader-facing; not a defect.
- **Gloss:** 5 gloss blocks per edition; counts 6/5/5/5/5 (core P2 block verified: `de lampion … het ledlampje`, n=6; headwords identical Dutch, same order, in all editions per checks log).
- **P6 chart:** rects in all editions x=1473, y=304/362/420/478, widths 160/100/80/60, height 18, fill `#3e4c2a` (values 40/25/20/15, scale 4 px/person).
- **P7:** golden sentences 8/8 verbatim contiguous excerpts in all 11 editions, body quotes 8/8, tags in order ['1','1','2','3','4','5','6','6'] (Pagina 1,1,2,3,4,5,6,6). Model essay 89 words in all 11 `.text.md` files, same Dutch text beginning `Maandag 9 november begint het Sinterklaasjournaal…`. Kinsoku scan: 0 line-start closers / line-end openers in core/JA/zh-tw. W45 promises present in P7 of all 11: Berlin 16 November, pakjesavond 5 December, VOL.4.
- **PDF text layer:** all 11 web PDFs 8 pages, 1462.5×2025.0 pt, ≤7 MB (largest zh-tw 1,615,015 B), pdftotext bytes >0, web==print extracted text True in every edition. Text bytes: core 44,392; de 46,586; en 45,597; es 46,675; fr 46,877; it 46,429; ja 47,973; ko 47,853; pt 46,689; ru 55,313; zh-tw 44,455. (Core 44,392 vs Round 2's 44,394 and fr 46,877 vs 46,876 reflect exactly the two fixed strings.)
- **Badge/footer/images/masthead:** footer 8/8 and page-line 8/8 in every edition; images per page [1,1,1,1,0,0,0,0]; 4 frozen Dutch `Foto:` credits in every edition (Wim van Rossem / Anefo, Nationaal Archief — CC0; Nationaal Archief — CC0; W. Punt / Anefo, Nationaal Archief — CC0; Spaarnestad Photo / Wikimedia Commons — publiek). Pairing badge visibly carried on P1 in every edition (O-1 accepted — not re-raised); core KIT §1 wording rewritten to describe the P1 subtitle + pairing strip/footer carrying (verified, KIT line 7). Masthead pixel clearance: ink x-range identical 26–1923 in all 11 P1 cards (frame/rule extent only), confirmed visually — no element touches the frame edge. Weekday/date claims independently verified via `TZ='Europe/Amsterdam' date -d`: 2026-11-09 Mon, 11-10 Tue, 11-11 Wed, 11-12 Thu, 11-13 Fri, 11-14 Sat, 11-15 Sun, 11-16 Mon, 12-05 Sat.
- **Orphan scan (independent, all 8 pages × 11 editions):** 0 lone `。`, 0 line-start `。`, exactly 142 exact `N.` at stem x (137/599/1061/1523), 0 stranded numbers. KO 2 accepted `가.`/`요.` orphans per O-2 (p6 x=1007 y=327.68; p7 x=527 y=785.11) — not re-raised.
- **Cards:** P1 and P8 of every edition viewed at full frame (22 cards), plus the changed pages (core P8, fr P8 — the same cards). No overflow, overlap, missing glyphs/tofu, or missing image credits in any card. The F-options/essay column adjacency on P8 (option b line ending near the essay column, e.g. core P8 `b. een dagelijks nieuwsprogramma op` / essay starting x=1451) is the pre-existing layout adjudicated non-defect in Round 2 with identical coordinates and occlusion 0; not re-raised. No other visual defect found.

## 6. Change isolation — see §3(c)

23 files differ vs the Round 2 state: 19 artifacts + 4 KITs, exactly as enumerated in §3(c). No other file changed. The change is isolated to the two fixed strings, their re-renders, font-subsetting drift in the 9 other web PDFs, and the 4 KIT corrections.

## 7. New / residual defects

**None.** Zero blocking defects, zero non-blocking defects found in this round. The only open record items are the two ruled record-only KIT notes in §3(a)–(b) (JA historical 3,341 line inside the Round 1 record; RU §9 809,219 drift figure) — neither is an artifact defect and neither requires correction before shipping.

## 8. Final verdict

**ROUND 3 PASS (all 11 shippable)**

N-1 and N-2 are CONFIRMED fixed at render level and in the `.text.md` exports; all Round 1 fixes survive; the independent residue sweep found no third candidate; keys are 150/150 in the core and in every fan-out; all re-gates pass; change is isolated to exactly the claimed files; all 22 P1/P8 cards are visually clean.
