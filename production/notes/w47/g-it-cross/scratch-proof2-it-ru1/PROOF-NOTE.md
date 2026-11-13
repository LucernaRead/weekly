# PROOF NOTE — 2026-W47 it-ru (Italiano × Русский), independent round 2 (re-fan-out)

**Verdict: (b) — ONE DEFECT. Not shippable as-is.**

One fan-out-introduced mistranslation (`scaglione` → «налоговая ставка», tax *rate*, instead of tax *bracket*), rendered in 5 places from 3 `translations.py` entries. Fix the Russian value(s), re-render the whole edition, and run a full re-proof per SOP §8.4. Everything else verified: all mechanical gates pass, 150-key three-way check 149/150 (the 1 difference is the documented writing-item format), all 8 pages visually read, all facts re-checked on the web.

Proofer: independent proof2 (round 2, full re-proof from scratch, SOP §8). Different person from the re-fan-out builder. Read-only on production: no commit, no push, no re-render of the delivered web PDF. KIT K6/K7 untouched.
Work date: 2026-11-11. Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-ru1/`.

## Identity (verified by me, full SHA-256)

| File | Size | SHA-256 |
|---|---|---|
| Print PDF `La-Lucerna-VOL4-RU.pdf` | 14,180,887 B | `f74bd65735550718a9927adb47047547d6cd3972f9ccfa4164bd467bf257c3fd` |
| Web PDF `La-Lucerna-VOL4-RU-web.pdf` | 1,441,225 B | `c35f390b39e3fe0ef6e95f9a9a292ab94cc356a3955decdcd2dbcd4cf357d1f5` |
| Text `2026-w47-it-ru.text.md` | 67,687 B / 1317 lines | `d1b6ddb1e691f74f7a7ce2960077774987dfd36b99712c8b3b49bb254a8361e2` |

All three match the task values exactly. Production re-verified untouched at the end of work: shipped SVGs `sha256sum -c` 8/8 OK, three deliverable SHAs identical, sizes identical. (The edition directory is still untracked in git — `?? production/2026-w47/2026-w47-it-ru/` — insertion has not happened; not my task, stated here only as observed state.)

## Defects

### D-1 (major) — `scaglione` mistranslated as «налоговая ставка» (tax rate) in the Russian explanation layer

**What is wrong.** Italian `lo scaglione` in the Manovra story is an income **bracket** (ступень шкалы): the P6 article itself says «l'allargamento del secondo scaglione Irpef al 33%, da 50 mila a 55 mila euro» — the second Irpef bracket widens from €50,000 to €55,000; 33% is the *rate* (aliquota). The Russian gloss says «налоговая ставка» — tax *rate*. That is the wrong concept, and it teaches the reader the wrong word for the week's lead economics story.

**Source (fan-out, not core).** Core Chinese is correct: `scaglione = 税级` (tax bracket), `core-it/content56.py:126` (gloss) and `content56.py:229` (Q100 note), `content8.py:85` (`scaglione=税级 a`). Every other fan-out language is correct — en `tax bracket`, de `Steuerstufe`, fr `tranche fiscale`, es `tramo fiscal`, pt `escalão fiscal`, nl `belastingschijf`, ja `税率区分`, ko `세율 구간`. Only ru says «ставка».

**Three `translations.py` entries, five renderings** (line numbers in the builder's `translations.py`, copy in my scratch):

| `translations.py` | Wrong ru value | Rendered at (text.md line → page) |
|---|---|---|
| L798–805 (long P6 gloss string) | `… lo scaglione, налоговая ставка …` | text.md:663 → P6 NOTE gloss «Пояснение — … lo scaglione, налоговая ставка · l'iter, процедура.» |
| L1778–1782 (`'scaglione = 税级'`) | `scaglione = налоговая ставка` | text.md:763 → Q100 note; text.md:1217 → P8 key 100 |
| L2076–2080 (`'scaglione=税级 a'`) | `scaglione = налоговая ставка, a` | text.md:987 → Q144 note; text.md:1305 → P8 key 144 |

**Internal contradiction in the paper itself.** Q144's own stem defines the word correctly — «144. lo scaglione — un livello di reddito del sistema fiscale» (an income level of the tax system) — while its key gloss in the same exercise says «налоговая ставка». The paper contradicts itself within one exercise.

**Rendering evidence.** Visually confirmed in the delivered web PDF P8 render (`pages/web-p8--8.png`, viewed): key 100 reads «100. scaglione — scaglione = налоговая ставка» and key 144 reads «144. a — scaglione = налоговая ставка, a». The Italian stems/keys are correct everywhere; only the Russian gloss is wrong.

**Fix direction (coordinator's call, not a decision).** Change the three ru values to a bracket term (e.g. «ступень налоговой шкалы»), then full re-render + full re-proof per SOP §8.4. The defect is in the explanation layer only — no Italian text, no exercise stem, no key letter changes.

## Re-fan-out report §7 items — adjudicated by measurement (not pre-judged defects)

### R-1 — «英文源 key 未改» (English-source key not changed)
**Not an issue — correct behaviour.** The keydiff measured by `p8.py compare` is exactly **[137, 138, 139]**, as expected for it. Q140's key is the Italian sentence «Ogni cifra deve essere chiara.» in REG, text.md, P8, and core alike — Q140 translates *into* Italian (the target language), so no re-aiming applies; only Q137–139 re-aim to the Russian reader language. Three-way check (REG vs text.md vs P8 printed keys): **149/150 exact matches**; the single difference is Q150, the writing item, whose documented format is `✓` on P8 («150. ✓ Образец текста в разделе H ниже (99 слов)» in text.md vs REG key «(Открытое задание — образец текста ниже)»). `gates.py` skips Q150 the same way. All three re-aimed keys hand-verified: Q137 «В праздник Мадонны делла Салюте люди переходят обетный мост.», Q138 «В воскресенье вечером «Аталанта» играет с «Интером».», Q139 «В субботу «Лацио» играет дома с «Лечче».».

### R-2 — Bilingual box titles STRADDLE the cream-box right edge
**Observation, not a defect** (task STRADDLE rule: a defect only if glyphs are clipped, ink overlaps another object or a visible border, or it is a regression vs the backup first-fan-out version). All three bilingual titles were pixel-measured on the **delivered print PDF 96 dpi renders**; see O-1/O-2 below. P1 overhang ≈104 px, P2 ≈59–60 px, P7 fits (−110.7 px). Neither overhang clips a glyph, overlaps anything, or is a regression — the backup first-fan-out SVGs (`scratch-refanout-it/backup/2026-w47-it-ru/svg/`) carry byte-identical title nodes at identical x/y with the identical cream rect. The overflow class is real and was called a defect in it-en proof2 (P1 +155 px, P2 +39 px, P7 +6 px there); here the task explicitly orders STRADDLE adjudication, and by that rule these two are observations. The web PDF was confirmed identical (see O-1/O-2).

## Observations (not defects)

### O-1 — P1 «LA SETTIMANA IN CIFRE　НЕДЕЛЯ В ЦИФРАХ» overhangs its cream box by ≈104 px
- SVG nodes: x=556.5 «LA SETTIMANA IN CIFRE　», 845.1 «НЕДЕЛЯ», 943.7 «В», 964.3 «ЦИФРАХ»; cream rect x=538.5..961.0, y=1351.5.
- Three measures agree: occlusion-audit OA ink 556.5..1061.8 (+100.8 px); real-font PIL (NotoSans-Bold) «ЦИФРАХ» 101.2 wide → union ≈556.5..1065.5 (≈104.5 px); **pixel on delivered print PDF 96 dpi render: cream ends x=960, dark ink to x=1065 → overhang 104 px**. The whole word «ЦИФРАХ» sits off-box (starts x=964.3, past the edge).
- Not a defect per STRADDLE: (1) no glyph clipped — full word renders; pixel column profile shows the cream edge falls in the inter-word gap between «В» (ink ends ~956) and «Ц» (starts ~967); (2) no overlap — cream rects have NO stroke (markup `fill="#f0eee5"` only); no vertical rule lines at x 955–995; row-level pixels y=1372–1384 show only gloss ink in x 960–1350; nearest col-3 content is «La Festa del Torrone chiude a ___.» at baseline y=1325.8 (above the band) and «Pag. 2» at x=1461.5; (3) not a regression — backup P1 nodes identical.
- Evidence: `pages/crop-p1-cifre.png` (2× crop); also visible in `pages/web-p1--1.png` (web P1, viewed — same overflow, same layout).

### O-2 — P2 «LA FRASE PER RICORDARE　ЗАПОМНИТЕ» overhangs its cream box by ≈59–60 px
- SVG nodes: x=556.5 + 872.1 «ЗАПОМНИТЕ»; box 538.5..961.0, y=1273.5.
- OA ink 872.1..1019.4 (+58.4 px); real-font «ЗАПОМНИТЕ» 150.8 wide → ends ≈1022.9 (≈62 px); **pixel on delivered print PDF: cream ends x=960, ink to x=1020 → overhang 59 px**.
- **Web PDF confirmed identical**: fresh 96 dpi render of the delivered web P2 (`pages/webp2-2.png`, viewed) measured with the same script (`web_p2_title_px.py`): box-top band cream right=960; title band ink right=1020 (same as print re-measured in the same run); column profile shows 0 dark px at x=960–961 — the cream edge falls in the inter-letter gap after «М» (ink 941–959, gap 960–963, ink resumes 964). All letters whole, no clipping, no overlap (col-3 region y 1250–1355 holds only the gloss tail, x 989–1020, y 1294–1309), no stroke, no rule, and not a regression (backup P2 nodes identical at 556.5, 872.1, same box).
- Evidence: `pages/crop-p2-frase.png`; web render `pages/webp2-2.png`.
- Note on OA ink accuracy for Cyrillic (task warning): real NotoSans-Bold vs CJK-SC widths — НЕДЕЛЯ +2.4% over, В +1.6% over, ЦИФРАХ −3.7% under, ЗАПОМНИТЕ −2.3% under, ОШИБКИ −3.2% under — OA within ≈±4%; pixel measurements on the delivered PDF are the verdict basis.

### O-3 — P7 «ERRORI TIPICI　ОШИБКИ» fits its box
Ink 1461.5..1751.3 vs box ending 1862.0 (−110.7 px). No issue. Evidence: `pages/crop-p7-errori.png`.

### O-4 — Word-gap tightness in the Russian layer (measured, not a defect)
At 96 dpi the Russian explanation layer looks like words run together (e.g. «переходилиобетный», «Напишитедва», footer «ИТАЛЬЯНСКИЙЕЖЕНЕДЕЛЬНИК»). This is the KIT §10 documented rendering characteristic (svglib splits Russian into per-word runs; space advance ~4.4–5 px). Independently measured with 200 dpi renders (`pages/hi1/hi2/hi3/hi5/hi7--*.png`) and node-based pixel gaps (`gap_measure*.py`):
- True word-to-word white gaps on Russian lines: **4.3–7.7 SVG px** (P1 cifre 4.8/5.3/5.3/6.7/7.2; P2 E-TU 4.3/4.8/6.7; P7 FRASI 6.2/7.2/7.7; dash/number/quote boundaries 5.3–6.7). Italian single-run control: 6.7–8.6 px.
- Letter gaps within words max 2.9 px — clean separation from word gaps; no two space-separated words touch.
- OA ink gaps ≈0 or negative near «—», ««», «»» are CJK-font artifacts (OA measures Cyrillic punctuation full-width); pixel measurement shows real spaces there (e.g. «29 — » → «очки» = 6.72 SVG px white). Quote/paren attachments (««Лацио», «лидирует)») have 0–1.4 px — normal typesetting, same class as Italian quotes.
- Conclusion: the 96 dpi «joined» appearance is a downsampling artifact. The engine was correctly left untouched (KIT §10 rationale stands; P8 flow has only 23 px spare).

### O-5 — Orphan scan: 4 flags, all adjudicated NOT defects
- P5 `( / «`: false grouping — the line at y=1031.72 is ««Интер»)" (nodes ««» + «Интер» + «»)»), a full line; ««» is just the first per-word run of the line.
- P6 `18.` at (1603.5, 641.6): byte-identical node in core SVG. Inherited.
- P8 `due` at (538.5, 818.98): byte-identical in core. Inherited.
- P8 `___` (Q137 stem blank, line 2): same pattern as core; 7 of 8 «___» nodes at identical positions, 1 x-shifted (RU 1318.1 vs core 1163.3 at y=644.85) explained by the re-aimed Russian stem.

### O-6 — P2 E TU gloss drops the VOL.5 clause — inherited
Matches core Chinese and en glosses exactly; inherited, not a defect. (The same gloss pattern is O-4 in it-en.)

### O-7 — P4 Nations League sentence — core-inherited
«si sono giocate prima di questa edizione… saranno nel prossimo numero» is byte-identical to the core — frozen Italian, inherited wording. The games (Nov 12/15) fall before the Nov 16 issue date but after press time; the deferral promise to VOL.5 is carried.

### O-8 — Spaced guillemets « la vetta » (P1 LA PAROLA box, P7 LA PAROLA) vs unspaced «…» elsewhere — core-inherited.

### O-9 — «de La Lucerna» byline (archaic «de») — core-inherited house style, 7×.

### O-10 — Fullwidth colon ： in 7 frozen P8 notes (16–20, 60–61) — 14 × U+FF1A in text.md; core-inherited.

### O-11 — Matching-key letter echo in P8 keys (25–28, 52–55, 141–144, e.g. «25. c — salute = здоровье, c») — core note format.

### O-12 — Q120 stem truncated with «…» and options without parentheses — core style.

### O-13 — Q58 note «самый лучший (оценка)» for «più bella» — loose but flagged as evaluation; acceptable.

### O-14 — P3/P5 mid-page structural whitespace — core pattern (KIT §10).

### O-15 — «56 titles» is a phantom number
Measured counts for this edition (definition: stripped line all-uppercase, len>3): **98 all-caps lines** in text.md (en edition measured 85 under the same rule — the difference is Russian all-caps gloss lines). Headlines **6/6 present**. String «56» occurs 2× (exercise 56 stem + key). No element of this edition counts 56.

### O-16 — P8 font 13.0 px = 9.75 pt, exactly at the SOP §1.1 floor (not below it).

### O-17 — Two notes checked during the full read
Q70 note «protagonisti = гости (мн. ч.)» is a slight narrowing of «participants» — acceptable. Q113 note «Лацио = Lazio» is the core pattern.

## What was verified (summary)

- **Full read**: all 1317 lines of text.md read; all 8 pages of the delivered print PDF visually read from fresh 96 dpi renders; web P1, P2, P8 visually read (web P2 rendered fresh this session). No overflow, overlap, footer intrusion, or tofu other than the two title observations (O-1/O-2). P1: clean except O-1. P2: clean except O-2. P3: clean (core-pattern mid-page whitespace). P4: clean (E TU box 2 lines + gloss, flush with table; results table clean). P5: clean (core-pattern whitespace). P6: clean except inherited «18.» orphan line. P7: LETTERE disclosure 3 lines, clear of FRASI hline; errori title fits. P8: dense but legible, «Переведите на русский/итальянский» labels correct, model text present, keys flow ends 2529/2552, no footer intrusion.
- **Golden sentences: 8/8 at exactly 2× each** (article + P7 FRASI): «La Lazio resta in vetta», «ventiquattro gol in dieci partite», «il ponte votivo sul Canal Grande», «oltre centocinquanta figuranti in costumi rinascimentali», «la squadra di Gattuso è ancora imbattuta dopo 11 giornate», «sette giorni di libri, ragioni e follie», «il testo può ancora cambiare», «approvato dal governo non vuol dire già legge».
- **Model text: 99 words** (range 80–100). **Headlines 6/6 present.**
- **Dates/weekdays verified with `date -d` (Europe/Rome)**: Nov 6 Fri, 7 Sat, 8 Sun, 9 Mon, 12 Thu, 15 Sun, 16 Mon, 17 Tue, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue, Dec 2 Wed, Dec 31 Thu, Oct 15 Thu, Oct 28 Wed — all match the paper.
- **Arithmetic re-done by hand**: MD11 goals 3+1+2+3+3+2+3+1+2+4 = 24 in 10 matches ✓; Q85 13−11=2 ✓; Q86 6+7=13 ✓; classifica Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Udinese 5 (20th) consistent across P1, P4 table, keys ✓; Torrone Nov 7–22 = 16 days / 3 weekends ✓; Torino Film Festival Nov 24–Dec 2 = 9 days ✓; BookCity Nov 23–29 = 7 days ✓.
- **Character scans**: CJK ideographs 0 in text.md; U+3000 ×101; U+FF1A ×14; U+2019 0; banned terms Ucraina/Russia/Putin/Ukraine/Gaza/Trump/Netanyahu all 0; «Translate» 0 in text.md; «Переведите» 8 (Q137–140 ×2: exercise labels + P8 section-E labels).
- **§8.1 gloss check**: every NOTE-box headword occurs in its article (normal inflection).
- **Facts verified via web search 2026-11-11** (multiple sources each; see GATE-LOG §15):
  - Manovra 2027: hearings Nov 9–12 (Giorgetti Thu 12), amendments deadline Tue Nov 17 18:00, bill C. 3174-bis, approval by Dec 31, ~26 miliardi — confirmed. DPB (Oct 15): growth +0.8% in 2027, deficit 3.4% in 2027 — confirmed. The «circa 5 miliardi dal settore finanziario» figure is hedged in the paper itself as «secondo le prime ricostruzioni» and labelled reported-not-voted; rests on core KIT verification.
  - BookCity Milano 2026: 15th edition Nov 23–29, theme «Il senno sulla Luna», 1,360 events / 2,487 protagonists / 1,164 books / 443 venues, opening Mon Nov 23 20:00 Teatro Dal Verme with Colson Whitehead (two Pulitzers), preview Sun Nov 22 16:00 Fondazione Luigi Rovati with Edmund de Waal — confirmed, including the official bookcitymilano.it press release and de Waal's own site.
  - Torino Film Festival: 44th edition, Tue 24 Nov – Wed 2 Dec 2026, nine days — confirmed from the official regulation (torinofilmfest.org).
  - Eurochocolate 32nd edition / Festa del Torrone 29th edition: rest on it-en proof2's 2026-11-11 verification (not re-litigated).

## Mechanical gates (detail in GATE-LOG.md)

All independently re-run by me, all PASS (20/20 in `gates.py`, `GATES ALL PASS`):
run.py RC=0, TOTAL 150, 0 overflow; SVG rebuild 8/8 byte-identical; print PDF re-render byte-identical (14,180,887 B, same SHA); freeze baseline 8/8 byte-identical (core verified as true core, not self-compared); freeze diff 0 unexplained add/rem P1–P7, strict-CJK only 8 × U+3000; occlusion audit 0 flags (selftest OK); p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139]; print/web text multiset identical (7587 words each, chars equal) and per-page sorted-token diff empty on all 8 pages; web PDF 1,441,225 B < 7 MB; P8 min font 13.0 px = 9.75 pt; paper #fbfaf6; no gold/brick/near-black; VOL.5 in exactly 3 legitimate nodes; VOL.4 ×9; badge colours present; 0 full-page rects; textmd validate forward-miss 0 / reverse-miss 0; answers 150/150; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing).
Cream-box scan (`cream_spill_orphan.py`): 5 flags — 1 CREAM-X (P2, adjudicated O-2) + 4 orphan candidates (adjudicated O-5).
