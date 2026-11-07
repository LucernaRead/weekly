# WEEKLY KIT — W45 ZH-TW × IT

**Status: BUILT (NOT finalized).** An independent proofread follows; only a zero-problem proof finalizes this edition.

- Slug: `2026-w45-zh-tw-it`
- Issue week: Nov 2–8, 2026 (VOL.2)
- Pairing: Traditional Chinese target text × Italian reader explanations
- Delivery dir: `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-it/`
- Build dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-tw-it-build/` (core copy + `transform.py`, the operative transform)
- Core: `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core/` (zh-tw × en) and its build dir `.../hidden_files/weekly-report-w45-zhtw-build/`
- W43 same-pairing reference: `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-it/` (hyphenated dir)
- Pages: 8, size 1950×2700. PDFs: print `Lucerna-VOL2-IT.pdf`, web `Lucerna-VOL2-IT-web.pdf`.

## 1. Baseline (before any change)

`freeze.py baseline` on the zh-tw core build: **8/8 SVGs byte-identical**, core integrity re-verified unchanged after the run.

Core SVG SHA-256 (first 16 hex):

| page | core hash |
|---|---|
| p1-front | 4672c972763b0eaf |
| p2-life | 889fb533ef3ff62e |
| p3-culture | 508703c2b3c313c6 |
| p4-sport | e04b62ea6211c9ff |
| p5-youth | 4dfce72d88000fbc |
| p6-deep | 06ba4c6627cb8165 |
| p7-lang | 00ac7f57125fcc09 |
| p8-test | e6e97d02595aef3b |

## 2. Registry (identical counts to core)

**150 exercises. Levels A2 44 · B1 74 · B2 32. Per page P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. Types 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.** Writing topic 《我的旅展計畫》, model 138 characters (band 120–180). Build log: zero `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings.

Registry-dump diff (core build vs this build, run in scratch copies): **keydiff = [150] only** — `#150 (開放題,範文如下)` → `(domanda aperta — modello qui sotto)`; **notediff = 150/150** (every note EN→IT); level/type/page diffs = none. Edition registry notes contain **zero Han characters** (all cited Chinese words are tone-marked pinyin).

## 3. Freeze diff core → edition (`--strict-cjk`)

**TOTAL added CJK = 0 on all 8 pages.** Per-page CJK counts core → edition: p1 952→920, p2 1018→996, p3 1088→1065, p4 831→809, p5 1101→1079, p6 942→921, p7 808→786, p8 1114→1018. Added strings are all Italian/furniture. Removed CJK is confined to old English-note Chinese citations (now pinyin) and the old Latin+Chinese footer string.

## 4. Traditional independence — HARD GATE (passed)

Method: CJK characters extracted from the shipped SVG `<text>` nodes of (a) this edition, (b) the UNION of the W45 zh-tw core shipped SVGs and the W43 zh-tw-it shipped SVGs. No Simplified→Traditional conversion, no OpenCC, no mapping table of my own was used anywhere; all Traditional text comes from the zh-tw core (frozen) plus W43 zh-tw-it precedent furniture.

- Edition distinct CJK characters: 772. Union distinct: 1031.
- **Edition characters outside the union: none (empty set).**
- Zero Simplified-only characters in target text. **Not a build failure.**

## 5. Gates on the final render (all green)

- `p8.py` extract: **150/150** noted. `p8.py compare` (explicit paths): **CLEAN, missing=[], extra_count=0, keydiff=[]**. (The `--target it` form fails for this target because it looks up the IT-target `p8_file` in tables.json; the explicit-path form is the correct invocation. keydiff=[] is expected: the tool normalizes the writing item to ✓, so the #150 key change does not appear there; it is proven by the registry-dump diff above.)
- `occlusion_audit.py --selftest`: OK (all planted classes fired, clean controls silent).
- Occlusion audit, edition: **0 flags**. `--core` NEW-vs-core: **0**. Same-baseline ink-collision scan (furniture bands, all pages): **0 flags**. P4/P6 chart-label graze check (any ink-vs-later-rect overlap): **0 hits** on both chart pages.
- Gloss/match counts item-identical to core: match sets 4+4+4+4 (配對 total 16, split on `·` per README #21 — the core's 16, not 33). Gloss boxes translated in place, counts unchanged.
- P7 golden sentences: **all 8 verbatim from this issue's own articles, exactly 2× each issue-wide (article + P7), correct page tags** p.1,1,2,3,3,4,5,6:
  - 「用手機轉帳、掃碼付款、網上買保險，都是金融科技」(p.1) · 「123個國家及城市、1,600個攤位」(p.1) · 「需要才買，不要為了折扣買一堆用不到的東西」(p.2) · 「在高雄，鋼鐵也能變成舞台」(p.3) · 「福隆的夏天，在10月26日畫下句點」(p.3) · 「6比0完封兄弟，龍隊拋下紅色彩帶」(p.4) · 「250家店家一起討糖」(p.5) · 「旅展首日中午12點才開門」(p.6)
- Images: payloads byte-identical to core per page (SHA-256 first 16: p1 `ac4dfe2ad3a43cd3`, p2 `a40e7a2b265beba6`, p4 `18ad8ae06fac2860` — the adjudicated Washington-team 1908 photo, provenance CLOSED per the core KIT coordinator adjudication 2026-10-27 and unchanged here, p5 `bcbada13a5ae19d6`; p3/p6/p7/p8 have no photos). Commons Artist credits verbatim: p1 `Photo: Wilfredor — CC0 (Wikimedia Commons)`, p2 `Photo: CorraleH — CC0 (Wikimedia Commons)`, p4 `Photo: Bain News Service — Public domain (Wikimedia Commons)`, p5 `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)`.
- Readers' corner: frozen Traditional disclosure `lt2` rendered **line-for-line identical to the core** (same 5 wrapped lines, same baselines); Italian disclosure present — `Lettera di esempio della redazione, non vera. Avviso di rinvio: il VOL.1 aveva promesso lettere vere e i migliori testi di pagina 8 da questo numero; alla chiusura non ne era arrivato nessuno pubblicabile, quindi resta l'esempio. Scrivici!` — states no genuine letters exist + explicit open invitation (`Scrivici!`).
- Cards: **all 8 eyeballed clean** (1950×2700 PNGs) — no overflow, no overlap, no footer collision; P7 teaser/footer clearance confirmed visually; P1 badge legible.

## 6. Furniture three-way (core · W43 zh-tw-it · this edition)

Measured from shipped SVGs/build code, not assumed:

| element | zh-tw core (zh-tw × en) | W43 zh-tw-it | this edition (W45 zh-tw-it) |
|---|---|---|---|
| P1 badge slot | y=378, 21pt, centered x=975, OLIVE | same slot, replaced in place, BRICK | **same slot, replaced in place, BRICK**: `TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI` |
| Footer left | `Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations` | `Lucerna · SETTIMANALE CINESE TRADIZIONALE VOL.1 · TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO` | `Lucerna · SETTIMANALE CINESE TRADIZIONALE VOL.2 · TESTI IN CINESE TRADIZIONALE · SPIEGAZIONI IN ITALIANO` |
| Footer right | `第 {n} 版 / 共 {total} 版` | `Pagina {n} di 8` (20pt sans GREY, baseline 2624) | same as W43 |
| Gloss prefix | `Notes｜` | `Nota — ` | `Nota — ` |
| P8 note style | dash `{n}. {key} — {note}`; writing `150. ✓ {note}`; separator `— Page {n} —`; key 12.8 / lh 1.12 / gap 1 | paren `{n}. {key} ({note})`; writing `150. ✓ ({note})`; separator `— Pagina {n} —`; key 13.0 / lh 1.13 | **paren, core geometry kept** (12.8 / lh 1.12 / gap 1 — paren adds no net length vs dash: ` — ` vs ` ()` are both 3 chars): `{n}. {key} ({note})`, writing `150. ✓ ({note})`, separator `— Pagina {n} —` |
| P8 band / heads | band `測驗與答案 · Test & keys` etc. (EN) | band `測驗與答案 · Test e risposte`, heads A–F in IT | band `測驗與答案 · Test e risposte`, sub `第 8 版 · 本週大測驗 + 全部答案 · Il test della settimana e tutte le risposte`; heads A `判斷對錯 · Vero o falso`, B `本週大測驗 · Il grande quiz`, C `完成句子 · Completa le frasi`, D `讀一讀,答一答 · Leggi e rispondi`, E `情景說話 · Dillo nel contesto`, F `寫一寫 · Scrittura`; keys header `答案 · Risposte — in ordine di pagina, con una breve nota in italiano per ogni esercizio`; right header `Tutte le note in italiano · ✓ = il modello di scrittura` |
| P7 furniture | band sub EN, heads EN | band sub / heads IT | band sub `Tre livelli, tre temi`; heads `Parole della fiera` / `Partite e stagioni` / `Modi di dire locali`; phrase header `Frasi della settimana — parola per parola dagli articoli di questo numero`; teaser `La prossima settimana (VOL.3)`; readers' title `L'angolo dei lettori`; clinic title `Clinica degli errori` |
| Bylines | `Staff report · Source:...` | IT bylines | `Dalla redazione · Fonte:...` (P1/P6: organisers' press release Oct 23 + event FAQ; P4: TSNA sports news, Oct 26) |
| Box titles (W43-overflow fixes kept) | — | `本週句式 · Struttura settimanale` (not `Struttura della settimana`, which crossed the box border in W43); `本週一詞 · Parola settimanale` (not `Parola della settimana`, which overflowed in W43) | same as W43 |
| Match instructions | `Match` (EN) | `Abbina ...` variants by content | all four W45 match sets are word↔definition, so `Abbina parola e definizione` everywhere |
| `Fill in` / `Writing` | EN | IT | `Completa` / `Scrittura` |

Note on README #20: its y=574/22pt inserted badge slot applies to FR/IT *target* cores, which have no free slot — not to the zh-tw target, whose y=372–378 slot is the core's own badge line. The W45 zh-tw-de sibling also replaces in place at y=378, 21pt BRICK. Note on README #14: the P8 paren style follows the zh-tw-it column's own shipped build code (W43 zh-tw-it re-laid the dash core as paren); other W43 zh-tw fan-outs split by native column (es/pt/it = paren; fr/de/nl/ru/ko/ja = dash), and the W45 zh-tw-de sibling keeping dash is consistent with the DE column.

CJK-paren discipline (per the W43 precedent): every Chinese word cited inside an Italian P8 note is written in tone-marked pinyin only; the printed P8 contains no full-width parentheses and no Han characters inside parentheses. Chinese words stay as Chinese in P7 prose/gloss bodies and in match lefts/rights (target text, not P8 notes). The content8:62 AI-variant trap was handled: the P8-key form of the shùzì note is a SEPARATE string from the P5 form and was translated too, as `L'IA nella finanza: réngōng zhìnéng.` — deliberately WITHOUT the full-width `＋`, because `freeze.py`'s CJK regex counts U+FF0B as CJK.

## 7. Fix rounds (all folded into transform.py as made — transform-first discipline)

1. **Round 2:** P6 head `深讀測驗 · Quiz di approfondimento` measured 498.2 units > 434 column → shortened to `深讀測驗 · Quiz avanzato` (346.4). P7 col3 had grown +113.52 vs core (clinic +1 line, letters +3 lines), pushing the teaser to bottom 2656.88 over the footer rule (2580) — clinic explanation #1 shortened by 1 line and the Italian disclosure shortened by 3 lines, restoring core geometry.
2. **Round 3 (strict-CJK +1 on P7):** a B1 memory-trick comma sat directly after 封王, so `svglib._fw()` converted it to a full-width `，` absent from the core. Reworded with `e` instead of the comma. (Same defect class to watch: any Latin punctuation directly adjacent to a Han character in Italian prose gets full-width-converted.)
3. **Round 4 (occlusion NEW flags, 3):** P5 box title ink 1909.2 > border 1885 → `天母時間表 · Programma Tianmu` (dropped `di`); P6 box title ink 1920.5 > border 1885 → `比價提醒 · Confronta i prezzi`; P7 letters box last-line ink bottom 1756.1 > border 1745.4 — the box-height formula under-measures the rendered stack by ~6px (the core escapes the same straddle only because its last line's ink centre sits 0.2px outside the audit's expanded box) — added 14px bottom padding (formula constant 26→40). P7 col3 now ends 1759.36, teaser ends 2557.36, still clear of the 2580 footer rule.
4. **Round 5 (residual-English sweep of rendered SVGs):** P4 word-card title had kept its English half (`棒球詞卡 · Baseball words`) → `棒球詞卡 · Parole del baseball`; `low cost` (P5 gloss + P5 note) → `tariffe economiche`.

## 8. Residual-Latin adjudication

Every Latin string in the rendered SVGs was adjudicated. Categories:

- **Italian explanation layer (the bulk):** all furniture, gloss bodies, notes, instructions, P8 keys notes, band subs — intended, fully Italian.
- **Pinyin citations (per W43 precedent):** `fēng wáng`, `wánfēng`, `jìnbǔ`, `jí zhāng`, `tǎotáng`, `dǎkǎ`, `Lìdōng`, `jiéqì`, `pàotāng`, `rèngōng zhìnéng`, `xiān bǐjià, zài jiézhàng`, etc. — tone-marked pinyin only, never Han characters, so no full-width paren conversion.
- **Frozen target-text Latin (Chinese articles, byte-identical to core):** `Fintech Nexus: Bridging the World, Building the Future` (event theme), `StartmeupHK 2026`, `ITF`, `Trick or Treat` (in the Tianmu article), `SUPER STAGE`, `SOLID TIDES`, `JUMP`, `Tamagotchi`, `MVP` (explained in-article as the English term for 最有價值球員）.
- **Proper names (kept deliberately, same as core gloss usage):** `Wilfredor`, `CorraleH`, `Bain News Service`, `Benjamin Balazs`, `Wikimedia Commons`, `CC0`, `Public domain` (photo credits, frozen); `Hong Kong Convention and Exhibition Centre`, `Nangang Exhibition Center`, `Taipei Dome`, `Tianmu Sports Park`, `Shin Kong Mitsukoshi`, `Dayeh Takashimaya`, `Zhongcheng Road`, `Tamsui-Kavalan`, `Raknus Selu`, `Mountain-to-Sea`, `Centenary`, `Indigenous`, `Sugar-Rail`, `Cathay Pacific`, `Wei Chuan Dragons` / `Dragons` / `CTBC Brothers` / `Brothers` (team names), `C.C. Mercedes`, `TSNA` (news source), `Jurassic World`, `Shrek`, `Kung Fu Panda` (film titles, same in Italian; `Ritorno al futuro` translated to its Italian title), `Taiwan Series` (event name), `6 Greenway` (challenge name), `Halloween` (same in Italian).
- **Established Italian loanwords:** `check-in` (`fare check-in con una foto`), `social` (`sui social`), `fintech` — standard Italian usage, not English residue.
- **English residue found and fixed (round 5):** `Baseball words` → `Parole del baseball`; `low cost` → `economiche`. Post-fix spot-check: `Baseball words`, `low cost`, `Did you get`, `Over to you`, `Quick quiz`, `Fill in`, `True or false`, `Answer keys`, `All notes in English`, `Model answer`, `Open task`, `Word of the week`, `This week`, `Practice`, `Staff report`, `Source:`, `Note: the` — all absent from the rendered SVGs.

## 9. Gate 10 — transform-solo reproducibility (passed)

Fresh copy of the core build into `hidden_files/weekly-report-w45-zh-tw-it-build/scratch-gate10/` (core files + assets + `run.py`), `transform.py` alone, one-process `run.py` with OUT redirected by env var to the scratch dir (the transform script supports `ZH_TW_IT_OUT` overriding the delivery dir; unset = delivery dir, so the shipped script is the tested script):

- **Gate 10 run exit code: 0. Warnings: 0. TOTAL 150.**
- **SVG comparison scratch vs delivered: 8/8 byte-identical** (p1-front, p2-life, p3-culture, p4-sport, p5-youth, p6-deep, p7-lang, p8-test).
- The same final transform re-run into the delivery dir reproduced the delivered SVGs hash-for-hash before Gate 10, confirming the env-override addition did not change default behaviour. Core SVGs untouched (re-hashed; p1 `4672c972763b0eaf...` etc. unchanged).

## 10. Delivered files and pins

SVG SHA-256 (full):

| file | SHA-256 |
|---|---|
| p1-front.svg | 1518337cb789da0f62f9c3b11320c0a9ac52adddff3bef2efde85ad26ea1c2c5 |
| p2-life.svg | ec016d3a99d033deef8500344f2c875f3417487acf21f8daaff2c866f7b33f51 |
| p3-culture.svg | 43366e952d1efed9d4d86fe7fc0a0fdd674c08fd2ae1798eb525fa35acc44a15 |
| p4-sport.svg | d71f5f8b09d862c9de66476510d3beb330b0420470f8df368a2420092085efe0 |
| p5-youth.svg | 79ebc140b5d4e623102dc1907ffe720de7f797544e5a983e6bc2f9c2f51d1bd7 |
| p6-deep.svg | ea4e52346cf2722f9e068f1708bb67b3fb9a1391c6311325d7caacd4a1440961 |
| p7-lang.svg | 335eca8c9aff661c50c02caca9ab927ab39956c149bd7f8e9e4bf6e90ad91065 |
| p8-test.svg | 9c632c151ab56a6939d162bd3015ef69e2a859af11ea843a0100e2e339e01173 |

Cards (1950×2700 PNG): p1 1,056,140 · p2 1,224,313 · p3 1,012,173 · p4 982,255 · p5 1,279,794 · p6 882,977 · p7 878,156 · p8 1,042,311 bytes.

PDFs (8 pages each):

| file | bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL2-IT.pdf` (print) | 20,069,224 | be06fcfa7b27643553af72267e37c8a4f7cdccca779d6c9f4e334d2b05a93e38 |
| `Lucerna-VOL2-IT-web.pdf` (web) | 3,456,580 (< 10 MB) | 5b5c111ed1eca5467b12d4e32412576d20bbbe055302a2e8ababb3bc57a96c15 |

## 11. Per-page contents

- P1 Front: Hong Kong FinTech Week x StartmeupHK 2026 opens Mon + Taipei travel fair opens Fri; word of the week 金融科技； quick quiz 1–4, headline words 5–10. Photo: Hong Kong harbour (Wilfredor, CC0).
- P2 Life: Lidong, hotpot/進補， hot-spring + hiking + 6 Greenway stamp challenge, Double 11 budget. Photo: autumn rain (CorraleH, CC0).
- P3 Culture: Lidong solar term, Kaohsiung steel sculpture festival (SUPER STAGE / SOLID TIDES), Fulong sand sculpture finale. Solar-term table, steel itinerary.
- P4 Sport: Wei Chuan Dragons Taiwan Series championship, 6–0 shutout in Game 6, Mercedes MVP; Game 6 runs-by-inning chart (1, 5); baseball word cards. Photo: Washington team 1908 (Bain News Service, public domain).
- P5 Youth: Tianmu Halloween recap (250 shops, trick-or-treat, pumpkin buckets, Tamagotchi 30th), travel-fair guide + fare comparison, Double 11 cart. Photo: carved pumpkin (Benjamin Balazs, CC0).
- P6 Deep: FinTech Week deep read (Finance+ / AI+ / global expansion), ITF daily opening-hours chart (6, 8, 8, 8; total 30), fare-comparison reminder.
- P7 Language: A2 fair words, B1 games & seasons, B2 local talk; error clinic (完勝/完封， 立冬/冬至， FinTech Week Hong Kong not Taipei); sentence frame 先…再…； readers' corner (editor's example + deferral disclosure + open invitation); 8 golden sentences with page tags; next-week teaser (VOL.3).
- P8 Test: big quiz 113–149 (A–E sections) + writing 150 《我的旅展計畫》 with 138-character model; full paren-style answer key with Italian note per exercise.

## 12. Trend/fact sources (inherited from the core; this fan-out changed no facts)

- Hong Kong FinTech Week x StartmeupHK 2026: organisers' press release Oct 23 + event FAQ (byline P1/P6); main conference Nov 2–3, Hong Kong Convention and Exhibition Centre; 45,000+ expected participants, 120+ economies, 1,000+ speakers, 800+ exhibitors/start-ups, 30+ delegations, 100+ community events.
- 2026 ITF Taiwan International Travel Fair: Taipei Nangang Exhibition Center Hall 1, Nov 6 (Fri, opens 12:00) to Nov 9 (Mon); 123 countries/cities, 1,600 booths; official hours Nov 6: 12:00–18:00, Nov 7–9: 10:00–18:00 (P6 source note); total 30 hours.
- Wei Chuan Dragons Taiwan Series championship: TSNA sports news, Oct 26 (byline P4); Game 6 Oct 26, Taipei Dome, Dragons 6–0 over Brothers, series 4–2, 6th title, first Dragons–Brothers final, first 3 shutouts in one series; C.C. Mercedes 8 innings, 0 runs, series MVP.
- Lidong Nov 7 (Sat); Kaohsiung steel festival Oct 23–Nov 22; Fulong sand sculpture May 29–Oct 26 (19th edition, 40+ sculptures, 15+ artists); Tianmu Halloween Oct 25–26 (typhoon-postponed from Oct 24).

## 13. Non-blocking notes (for the proofreader, not defects)

- P7 columns a2/b2 end at y=1561/1594 vs the 1560 flow bottom — no warning (flows are independent of the phrase strip, which starts at fy ≥1712); eyeballed clean, no overlap.
- P7 letters-box padding (+14px, round 4) is a deliberate divergence from core geometry: it fixes a real last-line/border straddle that the core escapes only via a 0.2px audit-centre artifact. The proofreader should confirm the letters box looks right on the card (it does: last line sits inside the border with clearance).
- The core KIT's P4 provenance adjudication (2026-10-27, CLOSED) is respected: placed bytes and credit line are unchanged, so provenance is not re-flagged here.
