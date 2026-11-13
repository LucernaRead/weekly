# WEEKLY-KIT — 2026-W47 es-nl (Spaans × Nederlands)

- Editie: `2026-w47-es-nl` — La Lucerna Spanish Weekly VOL.4, 16–22 november 2026.
- Lezerstaal: Nederlands (nl). Doeltaal: Spaans (es), tekst bevroren uit `core-es/`.
- Status: **zelfcontrole klaar, nul bekende gebreken; wacht op onafhankelijke proeflezing.**
- Bouwer: fan-out builder (es-familie), build 3 definitief, 2026-11-11.

## §1 Specificatie (uit core-es, ongewijzigd)

- 8 pagina's, 150 oefeningen (A2 50 / B1 72 / B2 28; per pagina 10/18/18/18/18/18/12/38).
- P8-antwoordletter 13,5 eenheden = 10,125 pt (min. Tm d 106,5, gelijk aan core).
- Papier #fbfaf6; masthead 196 eenheden; VOL.4 ×9 in SVG-tekst, VOL.5 ×3 (alleen
  legitieme vooruitverwijzingen naar volgende week).
- P8-chips: A2 11 / B1 21 / B2 3 = 35 chip-rects + 1 #37402f kopband-rect
  (core heeft dezelfde 4 #37402f rects).
- Q113–150 allemaal met badge; geen ontbrekende chips.

## §2 Inhoud per pagina (Nederlandse laag)

- P1 Portada: gloss «„Debat”: een discussie in het openbaar.» (1 regel, §6.10);
  kopregel «CADA SEMANA EN ESPAÑOL　ELKE WEEK　HET SPAANS VAN SPANJE»;
  pairing line «TEKSTEN IN HET SPAANS　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR
  NEDERLANDSTALIGE LEZERS»; lead-gloss «EERSTE CAMPAGNEWEK　NOG 13 DAGEN TOT DE
  VERKIEZINGEN».
- P2 Vida: band «Leven»; kalenderbox «EL CALENDARIO　De kalender» (294 eenheden,
  geen pt-§6.13-risico); Note «Uitleg — el debate = het debat · el mitin =
  de campagnebijeenkomst · el cartel = de poster · el escaño = de zetel in
  het parlement.»; C-intro «Lees het artikel en kies het juiste antwoord.»
  (1 regel).
- P3 Cultura: band «Cultuur»; Note-flamencowoorden; your-turn 3 regels @19.
- P4 Deporte: band «Sport»; Note «Uitleg — la jornada = de speelronde · el
  derbi = de derby · el liderato = de eerste plaats · el parón = de pauze ·
  la fase liga = de competitiefase.»; your-turn 5 regels @20.
- P5 Juventud: band «Jongeren»; your-turn 3 regels @19 (1715,55 → col3
  1574,55); B-bridge «Vul in met de woorden uit het kader. Let op: sommige
  woorden moet je vervoegen.» 2 regels, als geoogst behouden.
- P6 A fondo: band «Achtergrond»; subtitle «De campagne lezen: debatten,
  programma's en peilingen» (volledige sub in sans 18, 1014,7 eenheden,
  limiet 1684).
- P7 Lengua: band «Taal»; woordbox-gloss «debate = debat: een openbare
  discussie; de verkiezingen zijn op de 29e.» (2 regels); ERRORES-notes
  alle 4 één regel (§6.12); brief met halve haakjes «(ejemplo, escrito por
  la redacción)»; redactionele noot 4 regels @19 (§6.8).
- P8 Ejercicios y respuestas: kop «Oefeningen en antwoorden»; RESPUESTAS-kop
  naar y=1337, keys-flow naar 1363 (zwaan-caption); rechter-nota «Bij elk
  antwoord een korte uitleg in het Nederlands　✓ = met voorbeeldtekst»
  (689,1 eenheden @19,5).

## §3 Gemeten totalen (build 3, definitief)

- `run.py` rc=0, 0 OVERFLOW / 0 TOO WIDE, TOTAL 150.
- Kolom-einden: P2 1051,0; P3 1594,75 (13 px boven de y=1608-scheider);
  P4 993,5; P5 1574,55 (33 px boven scheider); P6 1241,55; P7 1873,51
  (§6.6); P8-keys y=2506 (54 px reserve); P8-ex flow y=943.
- Render rc=0: print `La-Lucerna-VOL4-es-nl.pdf` 3.502.220 B,
  SHA-256 `f88a21414c77508b8eb1a26af763e027fb5a1eed657b6fb576097ede8171dab1`;
  web `La-Lucerna-VOL4-es-nl-web.pdf` 850.386 B,
  SHA-256 `85240de829be675577d03467f8697e8bf2f7814fb1de022a20f2290da9a4bcb3`.
- Occlusion-audit: **0 flags**. Bridge-sweep: 0 wezen (20 bridges).
  Box-vs-hline-sweep: 0.
- p8 extract 150/150, compare CLEAN, keydiff=[137, 138] (§6.1).
- Freeze: tool 8 OK + directe sha256 8/8 (build-copy/svg vs verzonden svg/).
- pdftotext print = web, 45.724 B, byte-identiek.
- P8-minimumletter: Tm min d 106,5 (150 entries) = 10,125 pt, gelijk aan core.
- Volledige-breedte leestekens: 0 in .py en in SVG-tekst (118 × U+3000 zijn de
  titel-scheider, zoals in core).
- CJK: alleen de geërfde mottitel «三色蛾» (P1, onzichtbare metadata).
- Glosswoord-tokens (§8.1-methode, per pagina, ≥2 vereist): P1 reflexión 2;
  P2 mitin 2 / cartel 2 / escaño 2; P3 cante 5 / toque 6 / baile 9 / compás 4 /
  duende 6; P4 parón 2 / liderato 3; P5 papeleta 2 / censo 2 / plazo 3.
- `.text.md`: 1.816 regels, volledig gelezen; nummers 1–150 allemaal aanwezig;
  0 CJK; geen «12 de noviembre».
- 150 sleutels: volledig REG-dump gelezen (`scratch-fanout-es/es-nl-keys.txt`);
  matching-sets letter-voor-letter geverifieerd: 25–28 (debate=debat c,
  mitin=bijeenkomst b, cartel=poster d, escaño=zetel in het parlement a),
  52–55 (jornada=speelronde c, derbi=derby b, liderato=eerste plaats a,
  fase liga=competitiefase d), 141–144 (sondeo=peiling c, muestra=steekproef d,
  margen de error=foutmarge b, junta electoral=verkiezingscommissie a).

## §4 Bronnen (hergebruikt uit core-es)

- Volledige core-broncode (bslib4.py, content*.py, render.py, run.py,
  svglib.py + assets/) via `apply_fanout.py nl`; alleen de uitleglaag
  herschreven. Spaanse tekst bevroren; geen nieuwe trendresearch, geen
  feitwijzigingen, geen antwoordwijzigingen.
- W46 es-nl als referentie voor type-namen («Schrijven», «Vertalen»,
  «Zinnen maken», «W/NW») en harvest-conventies.
- nl.json harvest (263 keys), MANUAL/instr-tabellen in `manual_table.py`.

## §5 Bouwcommando's

```
cd ~/workspace/weekly-git
# apply (eenmalig):
python3 scratch-apply... # zie scratch-fanout-es/apply_fanout.py nl
# build:
tools/venv/bin/python run.py                     # in de editie-map
tools/venv/bin/python render.py
tools/venv/bin/python tools/occlusion_audit.py svg
tools/venv/bin/python tools/p8.py extract --p8 svg/p8-ejercicios.svg --total 150 --json <scratch>/es-nl-p8-extract.json
tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 svg/p8-ejercicios.svg --total 150
tools/venv/bin/python tools/freeze.py baseline --build . --core-svg ./svg --out <scratch>/freeze-es-nl-3
python3 <scratch>/sweep_de.py .
python3 <scratch>/extract_text_es_nl.py svg 2026-w47-es-nl.text.md
```

## §6 Adjudicaties

- §6.1 keydiff [137, 138]: vertaalitems opnieuw gericht (W45/W46-regel).
  Keys zijn de Nederlandse zinnen «Maandag is het Internationale
  Flamencodag.» / «Zaterdag kijken we naar de derby van Sevilla.»;
  nota «Vgl. origineel.» (beide). Geen gebrek.
- §6.2 #1 blijft 2 regels: bevroren key «13» + volledige zin als nota
  («De campagne begint op vrijdag 13 november om middernacht»); niets
  legitiems in te korten (zelfde als de/pt).
- §6.3 #44 en #139 blijven 2 regels: core-consistente wraps
  («De tijd vooraan, het werkwoord als tweede» / «pedir antes del jueves 19»).
- §6.4 #137 blijft 2 regels: de key alleen vult de regel; elke nota maakt
  er 2 van («Vgl. origineel.» is al minimaal; «Vgl. het origineel.» ook
  2 regels). #138 met dezelfde nota is 1 regel.
- §6.5 P8-keys eindigen y=2506 — ruim binnen de flow (bottom 2560).
- §6.6 P7 col3 1873,51 vs 1865,51 bij de/z/fr/it/pt: +8 px onverklaard
  (geen lijnhoogte-veelvoud van 29/27/26,5/30,5). Banner-inktbodem ≈2582,
  ruim onder de footer-regel 2596,5; occlusion-audit 0 flags. Genoteerd,
  geen gebrek — de audit is de poort, niet de exacte col3-waarde.
- §6.7 Mottitel `<title>Lucerna 三色蛾</title>` (P1): geërfd uit core,
  onzichtbare metadata, ongewijzigd gelaten (zoals alle edities).
- §6.8 CW-44-les (nieuw, 2026-11-11): P7-boxteksten (woordbox-gloss,
  redactionele noot, ERRORES-notes) wrappen op `CW − 44` (378,5), NIET op
  CW (422,5). CW-metingen onderschatten regel-aantallen: noot 5 i.p.v. 4
  regels, err2/err3 2 i.p.v. 1 regel. Definitieve noot (ed-A, 4 regels @19
  op CW-44): «Noot van de redactie: bij het sluiten geen echte brieven of
  beste teksten; dit nummer drukt een voorbeeldbrief. De belofte schuift
  door naar VOL.5.» — «bij het sluiten» + beide feiten behouden.
- §6.9 eh-formule wrap-size-bug (nieuw, 2026-11-11): de your-turn `eh`-
  formule wrapt de vertaling op maat 20 (`len(wrap(..., "sans", False, 20,
  CW - 44))`). Alleen de multiplier (*29→*27) en `p.para`-maat wijzigen
  verandert de wrap-telling NIET. Build 1: P5 col3 1601,55 (eh met 4
  regels @20) i.p.v. 1574,55. Opgelost: wrap-maat 20→19 in de eh-formule
  (content56.py:50, content34.py:45). pt/it deden dit wel; nl build 1
  miste het.
- §6.10 P1-gloss gw-les (nieuw, 2026-11-11): de P1-gloss wordt getekend met
  `p.para(..., gw, ...)` in content12.py:116 — breedte `gw` (≈378,5),
  NIET CW; en in **sans**, niet serif. Mijn eerste meting (serif, CW)
  meldde 1 regel, maar de toegepaste gloss «„Debat”: mensen discussiëren
  in het openbaar.» is 423,4 eenheden in sans 19 → 2 regels bij elke
  breedte 360–422,5; regel 2 («openbaar.») kruiste de y=1844-scheider
  (occlusion LINEX, build 2). Definitieve gloss, 1 regel in sans 19 op
  gw: «„Debat”: een discussie in het openbaar.» (356,0 eenheden).
  Kandidaten die ook pasten: «„Debat”: mensen praten in het openbaar.»
  (371,5), «„Debat”: mensen discussiëren openbaar.» (369,0 — onnatuurlijk
  Nederlands). «debatteren»-variant (411,0) paste niet. Les voor
  ru/ja/ko/zh-tw: meet de P1-gloss ALTIJD in het echte font (sans) op de
  echte `gw`.
- §6.11 P2 C-intro 1 regel («Lees het artikel en kies het juiste
  antwoord.»); P5 B-bridge 2 regels als geoogst behouden (zoals it —
  een 2-regelige B-bridge weest niet; alleen inkorten bij 3 regels).
- §6.12 P7 ERRORES: err2 «mejor is al een vergrotende trap.» (was 2
  regels: «mejor is al een vergrotende trap: geen más.»); err3 «gente is
  enkelvoud: werkwoord dus ook.» (was 2 regels; «werkwoord enkelvoud.»
  en «enkelvoudig werkwoord.» waren ook 2 regels; «gente is enkelvoud.»
  verloor het werkwoord-punt). err1 en err4 waren al 1 regel.
- §6.13 Apply-rapport-incident: stdout omleiden met `> 2026-w47-es-nl-
  apply.json` overschreef het JSON-rapport dat `apply_fanout.py` zelf
  schrijft (regel 132). Hersteld: map naar /tmp verplaatst, apply
  opnieuw zonder redirect, `diff -r` IDENTIEK, temp-kopie verwijderd.
  Les: stdout van apply_fanout.py nooit op de eigen rapportnaam omleiden.
- §6.14 P1-gloss eerste meting was fout (serif i.p.v. sans) — zie §6.10.
  De de/fr/it/pt-glosses zijn kort genoeg dat ze ook in sans op gw
  passen (hun audits waren 0 flags); alleen nl trof de grens.

## §7 Zelfproefleesronden

- Ronde 1 (build 1): P5 col3 1601,55 (eh-bug, §6.9); P7 col3 1955,55
  (CW/CW-44-meetfout, §6.8); P8-keys 6 overflows, y=2590.
- Ronde 2 (build 2): alle pre-fixes + 16 P8-notes ingekort; run 0
  overflow; P8-keys y=2506; render ok; **1 occlusion-flag** (P1-gloss
  LINEX, §6.10); sweeps 0/0.
- Ronde 3 (build 3): P1-gloss vervangen (§6.10); run 0 overflow;
  render ok; occlusion **0 flags**; sweeps 0/0; p8 CLEAN; freeze 8/8;
  pdftotext identiek.
- Ronde 4 (finale): 8 PNG's visueel gelezen; 150 sleutels gelezen;
  .text.md 1.816 regels volledig gelezen; §1.1 gemeten; gloss-tokens;
  **nul bevindingen**.

## §8 Leveringen (alle in `production/2026-w47/2026-w47-es-nl/`)

- `La-Lucerna-VOL4-es-nl.pdf` — 3.502.211 B (fix2-port rebuild, 2026-11-11;
  vóór: re-fanout 3.502.134 B),
  SHA-256 `67656a0d5451c3ef37aabd591d8505eda214de6812b019baa5151ee25d7cf174`
- `La-Lucerna-VOL4-es-nl-web.pdf` — 888.054 B,
  SHA-256 `c70a310a7210466736e85330237a7c333d00637988d1b7573b5c9a847247a1a8`
- `La-Lucerna-VOL4-es-nl.pdf` (D5 rebuild, 2026-11-12, see KIT tail D5 record) — 2,915,319 B,
  SHA-256 `7f7e902290987298f091ea9231eb7327b9ba980cfcf867c07e932e3a0c86ec10`
- `La-Lucerna-VOL4-es-nl-web.pdf` (D5 rebuild) — 805,821 B,
  SHA-256 `7d69a9df24051300dedbc69eee44595495c7bea0eefec50b9277e20fd337bef1`; 印/网 pdftotext 44,571 字符、8,373 词，逐字一致。
- `2026-w47-es-nl.text.md` (1.816 regels)
- `ABSTRACT.txt` (Nederlands, één regel, geen ASCII-dubbele aanhalingstekens)
- `WEEKLY-KIT.md` (dit bestand)
- 8 SVG in `svg/`, 8 PNG in `cards/`

## §9. 重建（re-fanout，2026-11-11 — core build 10）

Core baseline: core-es fix build 10 (independent re-proof (a), zero findings) — print 17,212,955 B SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`, web 1,410,471 B SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`, text.md 1,822 lines SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
Method: old edition backed up to `scratch-refanout-es/backup-old/` (verified identical), deleted, re-applied via `scratch-fanout-es/apply_fanout.py`; `classify.py` diffed fresh sources against the backup line by line — KEEP = core build-10 change, REVERT = edition hand fix restored, MERGE = derbi letter line (fresh sábado + backup ASCII parens), INSERT = RTVE debate-a-ocho timeline row. No commit, no push.
Common core changes kept: C1 (P1 CINCO CLAVES box 700→720), C2 (`antes del jueves`→`hasta el jueves`), es-ja D1 (consejo completed) + D4 (derbi sábado 21st), es-nl D1/D2, es-pt C2 (PCTE kept, 195 kept). C3 (P5 vocab `content56.py:79`) left as-is per adjudication.
Gates (all green unless noted): run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; render rc=0; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated — translation items keyed by target-language sentence); freeze 8/8 SVGs byte-identical; freeze-diff CJK accounting clean; canonical creambox.py full scan 0 own-ink overflow (the 6 raw negative lines per edition are the known below-box headings, identical to core); creambox_diag 0 own-ink negatives; boxtitle 0 overflow; keycheck 149/150 (only the #150 open-question `✓` exception); sweep 0 orphans / 0 box-vs-hline; pdftotext print = web bytes; P8 min effective font 10.125pt (≥ 9.75pt floor).
Classify: KEEP 23 / REVERT 31 / MERGE 1 / INSERT 1 / DELETE 0. Build: run2 rc=0, TOTAL 150, P8-keys y=2506. New print 3,502,134 B SHA `d5e63a7f5ee3c974b345ebdb72ca438082718de970e2469dba7c2f96b60db68c`; web 887,959 B SHA `54fbf35e4f3a0694d1922b5ef158d7ab9212d8908d1cedbecbf23f4465f6a763`; text.md 1,835 lines SHA `d8d8e0078a7a121cf9a68bb22ee8074c6245462ebd86ef768cf87ee88c44b91e`; print/web text 109,833 bytes, identical.
Hand fixes re-applied: D3 — P5 ¿Y TÚ? box +9px (eh +20→+29; true-ink clearance +6.4px; crop verified). D4 — P5 box title `EL PLAN DE LA SEMANA　Het weekplan` → `…　Weekplan` (was +36.8px; crop verified). D5 — P7 box title `ERRORES TÍPICOS　Typische fouten` → `…　Fouten` (was +6.5px; crop verified). D6 — P7 `LA PRÓXIMA SEMANA` banner moved up to core's py 2464.5 (bottom 2582.5 = core exactly; footer ink top 2611, clearance 28.5px; crop verified). C2 follow-up: the 5 P8 answer notes went 1→2 lines at 13.5pt after the C2 wording change, so they were shortened (e.g. `Stemmen per post: uiterlijk op de 19e aanvragen`, wrap-verified 1 line); P8-keys back to 2506, 0 OVERFLOW. P7 col3 ends 1873.51 (as in the old adjudicated note). **proof2 must re-measure D3–D6.**

## 10. Fix2-port rebuild (U+201C/U+201D/U+2019, 2026-11-11 — pre-insert)

Fix: ported the fix2 patch from `core-de/svglib.py` (commit 4ac7192c) into this edition's `svglib.py`, extended from U+201C-only to all three quote codepoints (`if ch in ("\u201c", "\u201d", "\u2019")`, class derived, not spelled, per fix2's freeze_direct note). `svglib.py` md5 `6a46ee51…` → `48c31801…`; py_compile passes; diff contains only the ported block; reverse-patch reproduces the pre-patch md5 exactly.
Census (before → after): **2 → 0 defective glyphs** — P1 `„Debat”: een discussie in het openbaar.` (19pt ” in Noto Sans CJK SC) and P6 `programma's` (18pt ’ in Noto Sans CJK SC), both now Newsreader; 4 quote glyphs total in the edition, all Newsreader after the fix. Note: the P6 ’ was previously recorded as "accepted as-is in a Newsreader context" — the census proves it rendered in Noto Sans CJK SC, so that acceptance is VOID; it is fixed by this port.
Gates (all green): two independent `tools/run_build.py` builds, A-vs-B SVG 8/8 byte-identical; run TOTAL 150, 0 OVERFLOW/TOO WIDE; webpdf rc 0; boxtitle 0 DEFECT; spill sweep 0; p8 extract 150/150, compare vs core CLEAN (keydiff [137, 138], adjudicated §6.1); occlusion 0 flags; `freeze.py diff` rc 0; frozen_check PASS 8/8; text.md byte-identical (SHA `d8d8e007…`, 1,835 lines). Logs: `hidden_files/w47/scratch-gatefix-u201c-es/2026-w47-es-nl/` (driver summary, census, patch log/diff).
New deliverables: print 3,502,211 B SHA `67656a0d…`; web 888,054 B SHA `c70a310a…`; pdftotext print = web 46,231 bytes (before 46,229; +2, whitespace only), -layout 109,822 bytes (before 109,833; −11, whitespace only — the quote run-splits change pdftotext's line grouping). Cards: `p1-portada.png` and `p6-afondo.png` re-rendered and synced (the fixed glyphs are on P1/P6); the other 6 cards byte-identical to before.

## D5 重建记录（2026-11-12，B档）
- 安装：`mechanism/apply_variant.py --svglib <本版>/svglib.py --target es --reader nl`（mode latin）；`svglib.py` md5 `48c31801…` → `da6d8aa3…`（与 core-es D5 后一致）；路由断言 10/10，fix2 保留（普查弯引号在 CJK Sans 0）。
- 预修 3 项共用版式（与 core-es 相同西班牙语串、同栏宽）：P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt、P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt、P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。
- 逐项修 3 项（D5 新缺陷，修前基线 0）：P1 框题 `LA SEMANA EN CIFRAS　De cijfers` +13.5px——该框 `tsize=21`；P1 手工题 `EN ESTA EDICIÓN　In dit nummer` +21.7px——24→22pt；P5 框题 `EL PLAN DE LA SEMANA　Weekplan` +34.7px——该框 `tsize=20`（21pt 余量仅约 3px，取 20 求稳）。以上文字均未动。
- 门禁全绿：run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0（`head_check.py` PASS 0 defects）；render rc=0；D5 普查 0；U+201C 普查（`census_quotes.py`）0；occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，仅读者语译注差异）；boxtitle 0 DEFECT；creambox（仓内 `tools/d5_creambox_audit.py`）PASS 0 defects（P8 249 行、页脚余量 36.4px 不变）；spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es：新增 CJK 字符 1 个，仅为 U+3000 全角空格（run 拆分计数 artifact）；印/网文字层 44,571 字符、8,373 词一致。
- 新 PDF：印刷版 2,915,319 B SHA `7f7e9022…`；网页版 805,821 B SHA `7d69a9df…`。`text.md` 字节不变（SHA `d8d8e007…`）。日志：`hidden_files/w47/scratch-d5-rebuild-es/2026-w47-es-nl/`。

## es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）

- 改动：F2（P6 时间轴措辞：`(sin el PSOE)` → `(sin el PSOE confirmado)`，与正文一致）。F1（缺首字下沉）按协调员裁定不修：全刊引擎级缺口，进模板 backlog，见 FIX-LOG。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 更新（core-es 为 D5 工具重导出；其余 10 版手术替换，diff 只含意改行；ru F4 另做词级手术，见 FIX-LOG 陷阱核查节）。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-nl.pdf` 2,915,320 B，SHA-256 `c716ce60992a4dd70c0debf89636650fa073255d3fad4dd2a83b306e5011d288`；网页版 `La-Lucerna-VOL4-es-nl-web.pdf` 805,809 B（< 7 MB），SHA-256 `8be3118b5080e616f5f92b03a792f56327c2ab3272e5fe7a3daa17a96a6107a3`；text.md `2026-w47-es-nl.text.md` 45,342 B，SHA-256 `d477656f5ef01f954068e4d002e424a16b3a872b911d22c3280c03feda911fd5`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 26 titles, 264 body lines，0 DEFECT；spill 0 SPILL（27 盒，71 candidates）；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8；印/网 pdftotext 46,142 字节逐字节一致。
- 日志：`hidden_files/w47/scratch-fix-es/`（FIX-LOG.md、build-all.log、build-resume.log、gates-all.log、text-pre/）。

## 第四轮独立重校修复 I1（2026-11-12，PROOF-NOTE-4 §2 返修）

- 改动：I1（text.md 专属，低）：两栏/两块拼接处丢空格致文字粘连；本版共 46 处（PROOF-NOTE-4 表列 29+7=36 处；机械穷举+印层逐一核验另得多 10 处同类粘连，见 FIX-LOG-4 §3）：分版粘连 39 处（数字粘连28 处、驼峰粘连3 处、数字→大写粘连2 处、句号→大写粘连2 处、逗号粘连1 处、中点粘连1 处、句号→小写粘连1 处、右括号粘连1 处）；目录粘连 7 处（`Pág. 2La semana` … `Pág. 8Ejercicios y respuestas` → 各补空格）。
- 重建：未重建（PDF 未动）；text.md 手术替换 46 处（逐处先断言原文存在再替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 39 行，行数不变（1836 行）。
- 文件：text.md `2026-w47-es-nl.text.md` 45,341 B（I1 前 45,295 B，+46 B）、1836 行，SHA-256 `2afcdcf2c3094e5c5b9cce14ac4abf9e5d41bb34b0c71f289746345ec7d5b6d0`（改前 `225181a991b53c7d5babfaa277f0b8a847c9ca759a4e359eca95b16efe178034`）；印/网 PDF 未动，SHA 不变（印 `c716ce60992a`、网 `8be3118b5080`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；D5 普查 PASS（弯引号 4/4 在 Newsreader）。
- 日志：`hidden_files/w47/scratch-fix4-w47-es/`（FIX-LOG-4.md、fix.py、fix2.py、fix-report.json、text-pre-*.md、gates4.sh、gates4.log、p8-extract/compare、census）。

## 第五轮独立重校修复 J1（2026-11-12，PROOF-NOTE-5 §3 返修）

- 改动：J1（text.md 专属，低）：小写词与小写词拼接粘连（I1 同类残留，第四轮 9 类模式与修复轮重扫均漏检）；本版共 1 处：`confinal` → `con final`（L1170，P6 Q88 C 尾 `con` + Q92 A 尾 `final`）。
- 重建：未重建（PDF 未动）；text.md 手术替换 1 处（逐处先与同版印 PDF 文字层核对断句、再断言原文存在后替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 1 行，行数不变（1836 行）。
- 文件：text.md `2026-w47-es-nl.text.md` 45,342 B（J1 前 45,341 B，+1 B）、1836 行，SHA-256 `d477656f5ef01f954068e4d002e424a16b3a872b911d22c3280c03feda911fd5`（改前 `2afcdcf2c3094e5c5b9cce14ac4abf9e5d41bb34b0c71f289746345ec7d5b6d0`）；印/网 PDF 未动，SHA 不变（印 `c716ce60992a`、网 `8be3118b5080`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）。
- 日志：`hidden_files/w47/scratch-fix5-w47-es/`（FIX-LOG-5.md、fix5.py、fix-report.json、text-pre-*.md、gates5.sh、gates5.log、p8-extract/compare、rescan.py、rescan.json）。
