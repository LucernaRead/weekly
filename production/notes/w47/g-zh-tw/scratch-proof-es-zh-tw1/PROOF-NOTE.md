# PROOF-NOTE — W47 es-zh-tw, proof round 1 (independent)

- **Edition:** `production/2026-w47/2026-w47-es-zh-tw/` (Spanish target, Traditional Chinese reader)
- **Proofreader:** proof1 (independent round)
- **Date:** 2026-11-11
- **Conclusion: (b) — 5 defects.** Not ready for 定稿 as-is. Three are edition-level (fan-out introduced, core text is correct — fix in the fan-out process / per edition, not in core); one is core-level; one is edition-level with a core-level residue. Full detail below, then the known-item verification table.

## Identity verified (KIT §1/§7 + disk)

| File | Bytes | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-es-zh-tw.pdf` (print) | 17,262,202 | `23926bd9729a041142472d066f0be2365d0edb54af3771e35e83e4d870ab8ff6` |
| `La-Lucerna-VOL4-es-zh-tw-web.pdf` | 1,686,124 | `3e96ea85cb5bfe3cdadd1d1ef1b861c26d4954ddca4daf1798738b03dd573920` |
| `2026-w47-es-zh-tw.text.md` | 43,246 (1,786 lines) | `0e6a0fbb89c1a686dd4484e5c2cc8d7cd14bd78627ecef6419987dbab1040fd0` |

All three match KIT. 8 pages, print = web text layer byte-identical (44,169 B each, 7,140 tokens, identical multiset; `-layout` mode differs only in trailing-space padding on line 14).

## Defects

### D1 — EDITION-level (fan-out, systematic) + core residue — P1/P2/P5/P8 — high — «antes del jueves 19» misstates an inclusive deadline and contradicts the issue itself

- **Locations (Spanish, 7 occurrences + 2 keys):**
  - `content12.py:42` — «Tiene que pedirlo antes del jueves 19:»
  - `content12.py:57` — Q3 stem «El voto por correo se pide antes del jueves ___»
  - `content12.py:125` — ballot-box caption «cómo pedir el voto por correo antes del jueves 19»
  - `content12.py:255` — Q9 stem «El voto por correo se pide antes del… A. jueves 19»
  - `content8.py:23` — Q116 stem «El voto por correo se pide antes del ___»
  - `content8.py:74` — Q139 model sentence «El voto por correo se pide antes del jueves 19.»
  - `content8.py:104` — MODELO essay «pido el voto por correo antes del jueves 19»
  - P8 keys, `text.md:1599` — «116. A — el voto por correo se pide antes del jueves 19»;
    `text.md:1705` — «139. El voto por correo se pide antes del jueves 19. — pedir antes del…»
- **Fact:** postal-vote request window is 6 Oct – **Thu 19 Nov inclusive** (Correos; LOREG art. 72; independently confirmed by the es-ja proof). Strictly, «antes del jueves 19» means *before* the 19th — a day early.
- **Self-contradiction within this edition:** P2 ¿SABÍAS? box, P2 Q22 stem, P5 Q65 stem, P5 article, P6 timeline «19 NOV», and the numbers box («19 — jueves, último día para pedir el voto por correo») all say **hasta el jueves 19**. Same-page clashes: P2 Q12 «antes» vs Q22 «hasta»; P8 Q116 «antes» vs Q123 «hasta».
- **Attribution — NOT core (correction of es-ja1's D3):** the core says «hasta el jueves 19» at every corresponding place (`core-es/content12.py:42, 57, 125, 255`; `core-es/content8.py:23, 74, 104`; core `text.md:1584` «116. A — el voto por correo se pide hasta el jueves 19», `:1704` «139. El voto por correo se pide hasta el jueves 19. — pedir hasta el…»). The same «antes» count (content12 ×4, content8 ×3) appears in es-ja and es-nl, so the fan-out process introduced it systematically across editions. Fix belongs in the fan-out, not in core.
- **Core residue (core-level, fix in core):** (a) P2 main text, same in this edition (P2 SVG y=1116.82) and in core: «tiene que pedirlo en Correos o por internet **antes de ese día** (página 5)»; (b) Chinese key notes «郵寄投票須在 19 日前申請» (keys 3, 9, 22, 65, 123 — identical to the core zh-cn text.md notes); (c) `ABSTRACT.txt` «11月19日前申請郵寄投票» (core `ABSTRACT.txt`: «邮寄投票 19 日前申请»).
- **Fix:** restore «hasta el jueves 19» at all 7 Spanish spots + keys 116/139 in the fan-out; in core change «antes de ese día» → «hasta ese día», the Chinese notes «19 日前» → «最遲 19 日/截至 19 日», and the abstract wording likewise; re-fan-out.

### D2 — EDITION-level (fan-out, systematic) — P1 — high — consejo sentence truncated mid-sentence

- **Location:** P1, middle column, consejo box. `content12.py:131`.
- **Rendered text (print + web P1):** «Nuestro consejo para esta semana: escucha el debate entero, no solo el titular. En la página 6 te enseñamos **cómo.**»
- **Problem:** the sentence ends on a lone «cómo.» — «cómo» requires a complement. Core `content12.py:130` has the full sentence: «…te enseñamos cómo **leer un debate sin perderse.**» — the full wording is also used in the caption directly below the box in this edition.
- **Attribution — NOT core (correction of es-ja1's D1):** core has the complete sentence; es-ja, es-nl and es-de editions all carry the truncated line at `content12.py:131`, so the fan-out truncated it systematically. Fix in the fan-out.
- **Fix:** restore the full core sentence.

### D3 — EDITION-level — P1 — high — CINCO CLAVES box: whole Chinese line spills below the cream box

- **Location:** P1, right column, CINCO CLAVES box. Canonical creambox scan (`hidden_files/w47/tools/creambox.py`, +45px window, `creambox.log`).
- **Measurement:** box y=588, **bottom=1288.0**; inside-only last baseline 1266.0 («en esta edición.», clearance +22.0, desc-clear +16.5); **BELOW-WINDOW +12.0 at y=1300.0: whole Chinese line «五大看點，不編數字：全在本期裡講清。」** sitting below the cream edge. Visually confirmed in `png/crop-p1-claves.png` — the line is rendered on white newsprint below the box. The same line sits at the box edge in the web P1 render.
- **Attribution — NOT core:** core P1 same box, **bottom=1308.0** (20 px taller), same Chinese line at baseline 1300.0 **inside** (clearance +8.0, desc-clear +2.3). Core fits; this edition's box is 20 px shorter. Fix in the edition/fan-out.
- **Fix:** shorten the note or enlarge the box (core's +8.0 clearance shows the box needs to be at least ~20 px taller here).

### D4 — CORE-level — P5 — moderate — word bank does not contain two of the six answers

- **Location:** P5, section B (PALABRAS DEL TEXTO). Bridge `text.md:949`: «用方框裡的詞填空。注意：有的詞要變位。» Bank `text.md:950`: «sobre · papeleta · censo · identidad · plazo · urna» (6 words).
- **Blanks and keys:** Q70 «Pido el voto por ___.» → **correo**; Q71 «En casa, relleno la ___.» → papeleta ✓; Q72 «Después ___（原形 enviar）el sobre.» → **envío**; Q73 «…mi documento de ___.» → identidad ✓; Q74 «La Oficina del ___ envía…» → censo ✓; Q75 «El jueves 19 termina el ___ del voto por correo.» → plazo ✓.
- **Problem:** `correo` (Q70) and `envío` (Q72) are **not in the bank**; `sobre` and `urna` fit **no** blank («Pido el voto por sobre/urna», «relleno la sobre», «Después urna el sobre» are all impossible). The bridge instruction — fill the blanks with the words in the box — is false for Q70 and Q72. The exercise is still solvable (Q70 from the article phrase «por correo»; Q72 from the inline infinitive hint «enviar»), so moderate rather than blocking. All other banks in this edition are exact (P3 5/5, P2 set D 4/4, P4 set B 4/4, P6 set D 4/4).
- **Attribution — CORE:** `core-es/content56.py:79` has the identical bank and keys 70/72. Fix in core, re-fan-out. (First reported as es-ja D2; the task brief did not list it, but it is present in this edition.)
- **Fix:** replace `sobre · urna` in the bank with `correo · envío` (or otherwise make the bank exactly the six answers).

### D5 — EDITION-level (fan-out, systematic) — P7 — minor — sample letter puts the derbi on the wrong day

- **Location:** P7, CARTAS DE LOS LECTORES, sample letter by the editors. `content7.py:99`.
- **Text:** «El lunes 16 escucho flamenco y **el viernes veo el derbi**.»
- **Problem:** the derbi (Sevilla–Betis) is **Saturday 21 November, 18:30**, Sánchez-Pizjuán (verified by my own search: orgullobiri.com 2026-11-08, betfair.es, hechoencalifornia1010.com 2026-11-10, vamosmisevillafc.com — all Sat 21 Nov 18:30). Friday 20 is Athletic–Espanyol (San Mamés, 21:00), not a derbi. The issue itself places the derbi on Saturday everywhere else, including this edition's P8 MODELO: «el sábado veo el derbi Sevilla–Betis con mi familia». The letter is explicitly marked as an editor-written example, so minor.
- **Attribution — NOT core (correction of es-ja1's D4):** core `content7.py:99` says «el sábado veo el derbi» (correct); es-ja, es-nl and (this) es-zh-tw all carry «el viernes» — fan-out introduced it systematically. The fixture date itself is correct in this edition (P1/P2/P4/P5/P6/P8).
- **Fix:** «el viernes» → «el sábado» in the fan-out.

## Known-item verification table (from the task brief)

| Item | Present in this edition? | Verdict |
|---|---|---|
| C1 P1 CINCO CLAVES 盒漫出 | Yes | **D3 above** — edition-level (core box fits, +8.0) |
| C2 antes→hasta | Yes (7 Spanish spots + keys 116/139) | **D1 above** — edition-level fan-out; core residue (P2 «antes de ese día», Chinese notes, abstract) core-level |
| D1 consejo 截斷 | Yes | **D2 above** — edition-level; core sentence complete |
| D4 德比日期 | Fixture date correct (Sat 21 Nov 18:30, 4 sources); only the P7 letter is wrong | **D5 above** — edition-level; core letter correct |
| es-nl D1 Atresmedia 日期 | Present (P6: «Atresmedia convoca su propio debate a cuatro para el lunes 23, sin el PSOE confirmado»; timeline 23 NOV; «26 NOV. — El PP propone un debate a cuatro (sin fecha pactada)») | **Not a defect at the 10 Nov cutoff.** Atresmedia MOVED its a-cuatro debate to Mon 23 Nov, announced Mon 9 Nov 2026 (20minutos via radarprensa.com 2026-11-09T15:22; zocalopublico.com 2026-11-09T17:25 «lo anticipa al día 23»; doblelectura.es guide: «Atresmedia convocó su propio debate a cuatro para el lunes 23, sin el PSOE confirmado»). The es-nl D1 evidence (4–6 Nov) predates the move. Per the same guide RTVE keeps a spokesperson debate on 23 Nov and the PP wants the a-cuatro on 26 Nov via the Academia — the paper omits RTVE's 23 Nov event but does not deny it. |
| es-nl D2 兩場已確認辯論與 Q89 鍵 | Present (P1 «Fue el único debate cerrado al cierre de esta edición»; P6 «Al cierre de esta edición, el 10 de noviembre, solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30, con Ana Pastor»; key 89 B, note «截至 11 月 10 日只有 laSexta 辯論已確定») | **Not a proven defect — two sources conflict, latest source supports the paper.** doblelectura.es guide (data 10 Nov 2026) says verbatim «A 10 de noviembre de 2026 solo hay un debate cerrado: el de portavoces de laSexta… Solo está cerrado el debate de laSexta» — «cerrado» = fully locked (time/host/lineup). Counter-source: diariodesantiago.es 2026-11-06, «únicamente están confirmados dos debates sectoriales: uno sobre economía, a cuatro, en La Sexta el próximo 13 de noviembre, y otro sobre vivienda, entre PSOE y PP, en la Cadena SER el día 18». The SER 18 Nov debate has a date/topic/participants but no published time, and the paper never gives it a time — so the paper's wording is self-consistent under the «cerrado» = fully-locked reading (same conclusion as core re-proof, PROOF-NOTE-es2.md observation 3). Residual tension, recorded as an observation (O7): the paper's own P2 calendar and P6 timeline list the SER 18 Nov debate unconditionally, next to the page's «propuesto ≠ cerrado» lesson. |
| C2 RTVE 免費分鐘未定 | Chart present (PSOE 45 / PP 45 / Vox 30 / Frente Amplio 30 / Podemos 15; footnote «Junta Electoral Central: 195 minutos en total, del 13 al 27 de noviembre. Tres formaciones más tienen 10 minutos cada una: Frente Obrero, PCTE y SALF»; 45+45+30+30+15+30=195 ✓; Q83–85 keys consistent) | **未核實 — not a defect.** LOREG art. 64 tiers confirmed (10/15/30/45 min by 2023 vote share; juntaelectoralcentral.es LOREG text). BOE-A-2026-23258 (4 Nov 2026) confirms the distribution was agreed per the Radio & TV Commission proposal and is «publicada en la página web de la Junta Electoral Central» — the table itself is NOT in the BOE text, and appeals ran until 10:00 Tue 10 Nov, so at the 10 Nov close it was published but not yet final. The exact JEC-published table was not directly retrieved (same as es-nl). Values are verified-by-scale only. (canariasenpleno 2026-11-05 figures — PP 38.96%, PSOE 34.67% etc. — are RTVE *informative-block* shares, not free-propaganda minutes; a different allocation, not a contradiction.) |
| es-ja D2 P5 詞庫 (not in the brief, found present) | Yes | **D4 above** — core-level |

## What was checked and cleared

- **Mechanical gates (all in this scratch dir):** `p8.py extract` 150/150; `p8.py compare` (explicit `--core-p8`/`--edition-p8`) **CLEAN except keydiff=[137, 138, 139]** — 137/138 are legitimate reader-language translation keys (Chinese sentences, matching W45/W46 ES×EN ruling); 139 is D1; note p8 compare checks key *values* only, not note text, which is why key 116's changed note (hasta→antes) was caught by hand, not by the tool. `freeze.py diff` (`--core-svg core-es/svg`): string counts balanced, 8/8; Latin-only diffs are the antes change, the P7 letter day, the P8 key 91 quote-style localisation (see resolved non-defects), and the P7 parens change. `occlusion_audit.py`: selftest OK, **0 flags**. Creambox canonical scan: 353-line log; only D3 is a true spill (other BELOW-WINDOW entries are +24/+37 next-heading false positives or the image-caption rect). P7 toolbox: 3 boxes, min inside clearance +8.8, min desc-clear +2.8 — clean. P7 banner geometry: dark rect y=2464.51, h=118, bottom=2582.51; footer rule y=2596; clearance 13.5 px; identical to core — clean (unlike es-nl D6). P8 min font re-measured by pypdf `Tm` parse: 150 ops, min **10.125 pt** (≥ SOP §1.1 floor 9.75 pt). BOXTITLE ink widths fit on all pages (visual + 0-flag audit).
- **150 keys, stem-by-semantics (hand-verified, not just compare):** numbering continuous 1–150; matching sets Q25–28 (c/b/d/a), Q52–55 (c/b/a/d; core §6.2 54/55 swap fix present), Q141–144 (c/d/b/a); Q96 «Aunque» + indicative ✓; Q112 key «tenga» ✓; Q132 key B («Dos ciudades, un sábado») ✓; Q150 model hand-counted **97 words** ✓.
- **Full text read:** `2026-w47-es-zh-tw.text.md` all 1,786 lines; all 8 print pages viewed at 100 dpi; web PDF rendered 8 pages at 100 dpi, P1 and P8 viewed (content identical to print; no web-only defect).
- **Facts verified (this edition):** 29N election Sun 29 Nov, 9:00–20:00; campaign 13–27 Nov (15 days), reflection 28 Nov; LaLiga J13 ten fixtures + J12 Barça 1–2 Atlético, standings 33/30/28; UCL J4/J5; flamenco UNESCO 16 Nov 2010 Nairobi; Santa Cecilia 22 Nov; Bilbao band 22 Nov 12:00 Euskalduna; Black Friday 27 Nov; MiDNI JEC 5 Nov; poll blackout 24–28 Nov = 5 days; Sargent painting (Commons «Spanish Dancer» 1880–81, PD). Weekdays all correct: 13 Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue, 25 Wed, 26 Thu, 27 Fri, 28 Sat, 29 Sun Nov 2026. P7 «FRASES DE LA SEMANA»: all 8 quotes verbatim against P1–P6 with correct page refs.
- **Language layers:** Simplified-character scan (simplified-only set) over text.md and all SVGs: **none**. «12 de noviembre» count in text.md: **0**. VOL.5 ×3 in text.md are forward refs; VOL.4 ×1 in text.md (KIT's «VOL.4 ×9» counts SVG text occurrences — different basis, not a discrepancy).
- **Abstract (SOP §9):** single line, Traditional Chinese, no ASCII `"`, real topics/keywords, masthead, target-language name, A2–B2, 150 exercises; opening «讀西班牙語學西班牙語» mirrors the core abstract's accepted opening (not the banned «讀新聞學» pattern); the «19日前» wording is part of D1's core residue.

## Observations (not defects)

- **O1** — P2 «D LAS PALABRAS» orphaned heading (bottom of col 3, items 25–28 in col 4); also P4 «B LAS PALABRAS», P5 «B PALABRAS DEL TEXTO». Inherited core layout; core proofers (es2 obs. 1, es-nl O1) ruled it a non-defect infelicity.
- **O2** — P8 key notes (inherited core, answers correct): key 103 note «a las 21:00（介詞 a）» vs stem 18:30; key 56 note «榜首之爭更重要» vs amistoso context (es2 obs. 2).
- **O3** — P6 timeline order: 26 NOV entry printed after the 24–28 range. Typographic only.
- **O4** — P7 clinic correction ««Es la una.»» drops «en punto» (core text; Q101 key «Es» unaffected).
- **O5** — P5/P6 large middle-column white gaps (same as core).
- **O6** — KIT wording: §6.9 claim «#139 core-consistent» is false (compare says keydiff includes 139 — it is D1); §3 keydiff=[137,138] understates the same. KIT §1 paper colour #fbfaf6 is correct in this KIT.
- **O7** — «solo hay un debate cerrado» residual tension (see table, es-nl D2 row): timeline lists the SER 18 Nov debate unconditionally beside the «propuesto ≠ cerrado» lesson.
- **O8** — Attribution correction for the coordinator: es-ja1's D1/D3/D4 claim the wording is «identical in core-es» — it is not, for the current core (core `content12.py:130` full consejo; core `content12.py:42/57/125/255` + `content8.py:23/74/104` «hasta»; core `content7.py:99` «el sábado»). D1/D2/D5 fixes belong in the fan-out; only D4 and D1's residue belong in core.

## Resolved non-defects

- **P8 key 91:** core '91. C — “提议的”不等于“确定的”' vs edition '91. C — 「提議的」不等於「確定的」' — legitimate Traditional Chinese quote-style localisation; key letter C identical; compare does not flag it.
- **P7 parens change** (KIT §6.8): full-width （）→ half-width () in the letter — adjudicated, fine.
- **P1 wrap artifacts** in the freeze diff are consequences of D1, not separate defects.
- **Tight creambox last lines** (desc-clear −0.9..−1.5): P2 ¿SABÍAS? and P5 VOTAR visually checked at 200 dpi (`crop-p2-sabias.png`, `crop-p5-votar.png`) — ink inside, clean; the other tight last lines are Chinese-only (no descenders) → inside.

## Evidence files (this scratch dir)

`probe.txt`, `print.txt`, `web.txt`, `print-plain.txt`, `web-plain.txt`, `occlusion.json`, `freeze-diff.json`, `creambox.log` (353 lines), `keys137.py`, `svgtext.py`, `freeze_lat.py`, `freeze_lat2.py`, `key91.py`, `key91b.py`, `p7geom.py`, `png/p-1.png` … `png/p-8.png` (print, 100 dpi), `png/p200-1.png`, `png/p200b-2.png`, `png/p200c-5.png`, `png/crop-p1-claves.png` (D3 spill), `png/crop-p1-consejo.png`, `png/crop-p2-sabias.png`, `png/crop-p5-votar.png`, `png/w-1.png` … `png/w-8.png` (web, 100 dpi).

## Verdict

**(b) 有問題 — 5 defects (D1–D5).** D1/D2/D3 high, D4 moderate, D5 minor. D1, D2, D5 are edition-level (fan-out introduced; core already correct — do not fix by editing core). D3 is edition-level (core box fits). D4 is core-level. D1 also has a core-level residue (P2 «antes de ese día», Chinese key notes, abstract «19日前»). Fix routing is stated per defect above.
