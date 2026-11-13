# PROOF-NOTE — W47 es-ja, proof round 1 (independent)

- **Edition:** `production/2026-w47/2026-w47-es-ja/` (Spanish target, Japanese reader)
- **Proofreader:** proof1 (independent round)
- **Date:** 2026-11-11
- **Conclusion: (b) — 4 defects, all attributed to CORE.** Not ready for 定稿 as-is; the defects live in `core-es` sources shared by all 11 native-language editions of the Spanish target, so the fix belongs in core, followed by a re-proof (or at minimum a targeted re-check of the four spots).

## Identity verified (KIT §7 + disk)

| File | Bytes | SHA-256 (prefix) |
|---|---|---|
| `La-Lucerna-VOL4-es-ja.pdf` (print) | 17,294,297 | `de40fa29ee957b64…` |
| `La-Lucerna-VOL4-es-ja-web.pdf` | 1,503,253 | `859b4421086697da…` |
| `2026-w47-es-ja.text.md` | 46,018 | `e1486c4686b7a0d2…` |

All match KIT. Print/web text layers byte-identical (47,054 B each), 8 pages, 1462.5×2025 pt.

## Defects

### D1 — CORE, P1, moderate — consejo sentence truncated
- **Location:** P1, middle column, consejo box. Source `content12.py:130`, identical in `core-es`.
- **Rendered text:** «Nuestro consejo para esta semana: escucha el debate entero, no solo el titular. En la página 6 te enseñamos cómo.»
- **Problem:** the sentence ends on a lone «cómo.» — «cómo» requires a complement («cómo leer un debate sin perderse», which is the wording used in the caption directly below the box). A Spanish reader sees an unfinished sentence on the front page.
- **Fix suggestion:** «En la página 6 te enseñamos cómo leer un debate sin perderse.»

### D2 — CORE, P5, moderate — word bank does not contain two of the six answers
- **Location:** P5, section B (PALABRAS DEL TEXTO). Source `content56.py:79`, identical in `core-es`.
- **Bank as printed:** `sobre · papeleta · censo · identidad · plazo · urna` (6 words).
- **Blanks and keys:** Q70 «Pido el voto por ___.» → **correo**; Q71 «En casa, relleno la ___.» → papeleta ✓; Q72 «Después ___ (infinitive: enviar) el sobre.» → **envío**; Q73 «Para votar en persona llevo mi documento de ___.» → identidad ✓; Q74 «La Oficina del ___ envía la documentación.» → censo ✓; Q75 «El jueves 19 termina el ___ del voto por correo.» → plazo ✓.
- **Problem:** `correo` (Q70) and `envío` (Q72) are **not in the bank**; `sobre` and `urna` fit **no** blank. The bridge instruction «枠の中の言葉で空所を補おう» (fill the blanks with the words in the box) is false for Q70 and Q72. The exercise is still solvable (Q70 from the article phrase «por correo»; Q72 from the inline infinitive hint «enviar»), which is why this is moderate rather than blocking. The other banks in this edition are exact (P3 5/5, P2 set D 4/4, P4 set B 4/4, P6 set D 4/4).
- **Fix suggestion:** replace `sobre · urna` in the bank with `correo · envío` (or otherwise make the bank exactly the six answers).

### D3 — CORE, P1/P5/P8, minor — «antes del jueves 19» misstates an inclusive deadline
- **Location:** P1 lead («Tiene que pedirlo antes del jueves 19»); Q3 stem («se pide antes del jueves ___»); Q116 stem («El voto por correo se pide antes del ___»); Q139 key («El voto por correo se pide antes del jueves 19.»); H model text («pido el voto por correo antes del jueves 19»). Source in `core-es`.
- **Problem:** the postal-vote request deadline is **Thursday 19 November inclusive** — request window 6 Oct–19 Nov, per Correos and the electoral calendar (LOREG art. 72). Strictly, «antes del jueves 19» means *before* the 19th, which contradicts the issue's own correct statements: P2 article «El voto por correo se pide desde la convocatoria y **hasta el jueves 19** de noviembre»; P5 article «se pide **hasta el jueves 19**»; numbers box «19 — jueves, **último día** para pedir el voto por correo»; Q22, Q65, Q123 all use «hasta». Within one issue the reader is told both «hasta el 19» (correct) and «antes del 19» (a day early). In everyday Spanish «antes del jueves» is often used loosely, so this is minor, but a weekly that teaches dates should not contradict itself on a deadline it repeats five times.
- **Fix suggestion:** change the five «antes del jueves 19» occurrences to «hasta el jueves 19».

### D4 — CORE, P7, minor — sample letter puts the derbi on the wrong day
- **Location:** P7, CARTAS DE LOS LECTORES, sample letter by the editors. Source `content7.py:99`, identical in `core-es`.
- **Text:** «El lunes 16 escucho flamenco y **el viernes veo el derbi**.»
- **Problem:** the derbi (Sevilla–Betis) is **Saturday 21 November, 18:30**. Friday 20 is Athletic–Espanyol (San Mamés, 21:00), not a derbi. The issue itself places the derbi on Saturday everywhere else: Q118, Q124, Q134 («El sábado vemos el derbi.»), Q138 key («土曜日にセビージャ・ダービーを見る»), P4 fixtures table. The letter is explicitly marked as an editor-written example, so the damage is small, but it directly contradicts the fixture list the issue teaches.
- **Fix suggestion:** «el sábado veo el derbi».

## Candidates examined and withdrawn (not defects)

- **P1 past tense for the 13 Nov debate** («El primer debate fue también el viernes 13… cuatro portavoces hablaron de economía»). Withdrawn: the issue week is 16–22 Nov, so from the reader's standpoint the Friday 13 debate is already past; P6's «Al cierre de esta edición, el 10 de noviembre… Van… a hablar» is the production-close standpoint. The two are coherent. Q115 on P8 («El debate de laSexta fue a las 21:30») is likewise correct.
- **Q79 key read as «Van a comprar precios»** and **Q86 key read as B** — both were misreadings of the small P8 print by the proofreader; the SVG text and `p8extract.json` confirm «Van a **comparar** precios antes de pagar.» and Q86 = **A** (5 días). No defect.
- **#140 note «〜しなければならな い»** — line-wrap artefact in the PNG; SVG shows «〜しなけれ» / «ばならない» across two lines. No defect.
- **#88 note** — correctly reads «選挙管理委員会が公表した無料放送時間だけを出典付きで載せる». No defect.

## What was checked and cleared

- **Full read:** `2026-w47-es-ja.text.md` lines 1–1803 (all 8 pages: articles, exercises, P8 answers); P1–P8 card PNGs viewed.
- **150 keys, stem-by-stem:** every stem verified against its key from `p8extract.json`. No Q39/Q40-style swap (Q39 = B Nairobi, Q40 = A duende — correct; the en-family swap does not occur here). All matching sets verified against their definitions (Q25–28, Q52–55, Q97–100, Q141–144). All 12 P7 grammar keys (Q101–112) and all P8 keys (Q113–150) verified. MODELO essay counted: **97 words** exactly, as claimed. P8 chip count 35 vs 38 exercises: Q25–28 share one chip, Q52–55 share one, and Q141–144 share one (the three matching sets), which accounts for 35 = 38 − 3. ✓
- **External facts, all verified online 2026-11-11:**
  - 29N election real: RD 806/2026; vote Sun 29 Nov 9:00–20:00; campaign 13–27 Nov; reflection 28 Nov; 38,728,356 voters; 350 deputies; 209 senators; constitutive session 23 Dec 10:00. (lamoncloa.gob.es, ine.es)
  - Postal vote: request 6 Oct–Thu 19 Nov inclusive; documentation from Mon 9 Nov; deposit by Wed 25 Nov. (correos.com)
  - La Liga J13 all ten fixtures + times verified; J12 Atlético 1–2 Barça (8 Nov), standings Barça 33 / Madrid 30 / Atlético 28 / Betis 26.
  - UCL J5 (24–25 Nov) and J4 results verified.
  - MiDNI: JEC lifted the suspension 5 Nov 2026; MiDNI authorised for voter ID.
  - Flamenco Day: 16 Nov 2010, Nairobi, UNESCO Representative List.
  - laSexta debate moved Mon 9 → Fri 13 Nov 21:30, Ana Pastor, Cuerpo/Bravo/Bustinduy/Figaredo, vivienda y economía; only closed debate as of 10 Nov. P6 calendar matches the debate guide item by item.
  - SER housing debate Wed 18 Nov: Rodríguez vs Bravo, confirmed.
  - Other debates (cara a cara Mon 16 proposed, Atresmedia 4-way Mon 23, 4-way Thu 26 requested) — paper's hedged framing matches the record as of 10 Nov.
  - Bilbao Municipal Band: Sun 22 Nov 12:00, Palacio Euskalduna, Santa Cecilia concert; Santa Cecilia 22 Nov, patron of musicians.
  - Poll ban: LOREG art. 69.7 — no polls in the 5 days before voting → 24–28 Nov for a 29 Nov vote. ✓
  - Black Friday Fri 27 Nov 2026 (day after US Thanksgiving Thu 26 Nov).
  - **Sargent image:** «Bailaora española» (1880–81) is correct — there is a full-size oil *Spanish Dancer* (1880–1881, private collection) distinct from the *El Jaleo* study (1879–82); the pictured dancer (white dress, black shawl, extended arm) matches it. (Google Arts & Culture / Dallas Museum of Fine Art record.) KIT's Commons-API verification (2026-11-10) is independently confirmed.
  - **RTVE free-minutes chart:** numbers match the LOREG art. 64 baremo exactly (45 min ≥20%, 30 min 5–20%, 15 min <5% with representation, 10 min no representation) applied to the 2023 results, and total 45+45+30+30+15+10+10+10 = 195. The JEC resolution BOE-A-2026-23258 (4 Nov 2026) publishes the distribution via the JEC website; the per-party table itself was not directly retrieved in this pass — a verification limitation, not a defect, since every checkable element (scale, brackets, total) is consistent.
- **Dates/weekdays:** `date -d` (Europe/Madrid) — 13 Nov Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 24–28 Tue–Sat, 27 Fri, 28 Sat, 29 Sun, 10 Nov Tue, 9 Nov Mon. All consistent with the paper.
- **Mechanical gates:** see GATE-LOG.md — all passed (occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN; freeze 8/8 SVG match; freeze_direct rc=0, 0 overflow; print/web text layers identical; cream boxes clear; box titles 25/25 fit; P8 min font 10.125 pt; paper #fbfaf6; masthead 147 pt; VOL.4 ×9 / VOL.5 ×3 all on P7; curly quotes 0; no «12 de noviembre» anywhere; ABSTRACT.txt present, reader-native).
- **P7 FRASES DE LA SEMANA:** all 8 quotes verbatim from this issue's own articles (P1–P6), each with Japanese gloss and page reference. ✓
- **P7 LA PALABRA / ERRORES TÍPICOS / CARTAS:** content verified (grammar rules correct; error corrections correct; editor's note present). Only D4 (letter's «el viernes») is wrong.
- **Fonts:** Newsreader 1096, Noto Sans CJK SC 619, Noto Serif CJK SC 319 — CJK runs split out of serif paragraphs + «→» arrows is renderer design, not a defect. UnifrakturMaguntia 1 (moth/fleuron). Odd fills inside the moth `<svg>` illustration are inherited from core.

## Attribution summary

| Defect | Severity | Page | Attribution |
|---|---|---|---|
| D1 truncated consejo («cómo.») | moderate | P1 | core (`content12.py:130`) |
| D2 word bank missing correo/envío | moderate | P5 | core (`content56.py:79`) |
| D3 «antes del jueves 19» ×5 | minor | P1/P5/P8 | core |
| D4 letter «el viernes veo el derbi» | minor | P7 | core (`content7.py:99`) |

No this-edition (es-ja layer) and no mechanism (renderer/tools) defects found. All four defects are in `core-es` and therefore affect all 11 native-language editions of the Spanish target identically.
