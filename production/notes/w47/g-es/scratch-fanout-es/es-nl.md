# es-nl — Per-edition record (2026-11-11)

Status: **COMPLETE — self-check zero issues; awaiting independent proofreading.**

## Coverage pre-check

- nl-missing 129 items; nl-conflicts 0 lines; nl.json 263 keys.
- All covered by MANUAL + harvest/nl.json + special handling.

## Apply

- `apply_fanout.py nl`: 487 total literal replacements (255 distinct keys in
  the report dict); 2 manual-over-harvest overrides:
  - «Después ___ (原形 enviar) el sobre.» harvest «Después ___ (infinitief
    enviar) el sobre.» → manual «Después ___ (infinitief: enviar) el
    sobre.» (met dubbele punt).
  - «JUVENTUD　青年» harvest «JUVENTUD　Jeugd» → manual «JUVENTUD　Jongeren».
- Leftover zh keys NONE; CJK in .py NONE.
- Band titles verified: VIDA　Leven, CULTURA　Cultuur, JUVENTUD　Jongeren
  (hoofdletter, geen all-caps; harvest had Cultuur/Leven al).
- «EL CALENDARIO　De kalender» — korte gloss, 293,75 eenheden
  (geen pt-§6.13-overlooprisico). P8-kop al «Pagina 8» (harvest de-capped,
  geen manual nodig).

### Apply-rapport-incident

Stdout omleiden met `> 2026-w47-es-nl-apply.json` overschreef het
JSON-rapport dat het script zelf schrijft (regel 132 van apply_fanout.py).
Hersteld: map naar /tmp verplaatst, apply opnieuw ZONDER redirect,
`diff -r` IDENTIEK, temp-kopie verwijderd.
**Les: stdout van apply_fanout.py nooit op de eigen rapportnaam omleiden.**

## Pre-build fixes (alle wrap-gemeten vóór build)

- P1 gloss: «„Debat”: twee of meer mensen discussiëren in het openbaar, om
  de beurt en met vragen.» (2 regels @19) → «„Debat”: mensen discussiëren
  in het openbaar.» — gemeten als 1 regel, maar **fout gemeten** (serif op
  CW i.p.v. sans op gw; zie build 2 / KIT §6.10).
- P7 word-box gloss: «debate = debat: een openbare discussie, om de beurt.
  Dit is debatweek; de verkiezingen zijn op de 29e.» (3 regels @20) →
  «debate = debat: een openbare discussie; de verkiezingen zijn op de
  29e.» (2 regels @20, ook 2 regels op CW−44 ✓).
- P7 F-MAIL editor's note: origineel 6 regels @20 / 5 @19 (CW) → eerste
  versie «Noot van de redactie: er waren bij het sluiten van dit nummer
  nog geen echte brieven of beste teksten binnen; dit nummer drukt een
  voorbeeldbrief. De belofte schuift door naar VOL.5.» gemeten 5 regels
  @19 op CW maar **5 regels @19 op CW−44** → vervangen door ed-A:
  «Noot van de redactie: bij het sluiten geen echte brieven of beste
  teksten; dit nummer drukt een voorbeeldbrief. De belofte schuift door
  naar VOL.5.» (4 regels @19 op CW−44 ✓; behoudt «bij het sluiten» +
  beide feiten).
- P7 ERRORES notes (4): «1 uur is enkelvoud: gebruik es.» 1 regel;
  «mejor is al een vergrotende trap: geen más.» **2 regels op CW−44** →
  ingekort tot «mejor is al een vergrotende trap.» (1 regel @19,5 CW−44);
  «gente is enkelvoud: werkwoord in het enkelvoud.» **2 regels op CW−44**
  → geprobeerd «werkwoord enkelvoud.» (2 regels), «enkelvoudig
  werkwoord.» (2 regels), «gente is enkelvoud.» (1 regel, verliest
  werkwoord-punt) → toegepast «gente is enkelvoud: werkwoord dus ook.»
  (1 regel @19,5 CW−44 ✓, behoudt beide feiten); «creo que bevestigt:
  aantonende wijs es.» 1 regel.
- P5 your-turn: «Stem je per post of in persoon? Wat zou je kopen op Black
  Friday: iets nuttigs of een impuls? Schrijf twee zinnen en stuur ze in.»
  — 3 regels @20 en @19 (CW−44) → gerenderd op 19 (geen woordwijziging).
- P3 your-turn: «Heb je ooit flamenco gehoord? Welke muziek uit jouw land
  heeft duende? Schrijf twee zinnen en stuur ze in.» — 3 regels @20 en
  @19 (CW−44) → gerenderd op 19 voor de 13px-marge.
- P2 your-turn: 5 regels @20, geen fix. P4 your-turn: 5 regels @20,
  box ≈993,5, geen fix.
- P2 C-intro: «Lees het artikel op pagina 2 en kies het juiste antwoord.»
  (2 regels) → «Lees het artikel en kies het juiste antwoord.»
  (1 regel @20,5).
- P5 B-bridge: «Vul in met de woorden uit het kader. Let op: sommige
  woorden moet je vervoegen.» — **al 2 regels @20,5, als geoogst
  behouden** (zoals it; sweep verifieerde later 0 wezen).
- P6 band: «De campagne lezen» → «De campagne lezen: debatten,
  programma's en peilingen» (sans 18: gloss alleen 489,0 eenheden;
  volledige sub «NIVEL B2　Leer la campaña: debates, programas y
  encuestas　De campagne lezen: debatten, programma's en peilingen» =
  1014,7 eenheden, limiet 1684 — past. Let op: `band()` tekent `sub` in
  **sans** 18, end-anchored; de eerdere pt/fr/it «≈950 eenheden @18»-
  cijfers waren serif-metingen en zijn NIET de operatieve bandbreedte —
  meet de volledige sub in sans.)
- P8 header note: «Bij elk antwoord een korte uitleg in het Nederlands　✓
  = met voorbeeldtekst» 689,125 eenheden breed @19,5 → header 1302→1337,
  keys flow 1328→1363.
- Letter haakjes full-width → half-width «(ejemplo, escrito por la
  redacción)» (content7.py:99).

### KRITIEKE LES (nl, 2026-11-11): meet P7-boxteksten op CW−44, NIET op CW

De woordbox-gloss, redactionele noot en ERRORES-notes wrappen op `CW − 44`
(378,5), en de your-turn `eh`-formule wrapt de vertaling op maat 20 —
alleen de multiplier (*29→*27) en de `p.para`-maat wijzigen verandert de
wrap-telling NIET. Mijn eerste nl-edit miste de wrap-maat in de eh-formule,
dus build 1 P5 col3 was 1601,55 (eh berekend met 4 regels @20: nl eh =
324,0 vs pt eh = 297,0) i.p.v. 1574,55. Opgelost in de tweede pass
(content56.py:50 en content34.py:45 wrap-maat 20→19; P3's wrap-telling was
3 bij beide maten, dus alleen P5's getal veranderde, maar beide werden
gecorrigeerd voor consistentie).

## Builds

- **Build 1:** run rc=0, TOTAL 150; P3 col3 1594,75; P5 col3 **1601,55**
  (eh wrap-size bug, 6,45 px boven de scheider — niet kruisend, maar 27 px
  dode ruimte in de box); P7 col3 **1955,55** (+111 vs core; de
  CW/CW−44-meetfout); P8-keys 6 overflows, eind y=2590.
- **Fixes na build 1:** content56.py:50 wrap 20→19; content34.py:45 wrap
  20→19; ed note → ed-A; err2 ingekort; err3 → «werkwoord dus ook.».
- **P8 diagnostic (nl):** 19 multi-line items vs core's 2. Schrijftype
  bevestigd **«Schrijven»** (content8.py:134 — de ✓-vorm; #150's ✓-vorm
  is 1 regel). 16 notes ingekort tot 1 regel elk (wrap-geverifieerd op
  13,5): #29 «Flamencodag, maandag 16 november», #32 «Sint-Cecilia is op
  22 november», #33 «Orkest van Bilbao, zondag 22, 12.00 uur», #41
  «Flamenco ontstond uit vele culturen in Andalusië», #42 «Na Flamencodag:
  de verkiezing van 29 november», #43 «Onderwerp, werkwoord», #45 «De
  plaats vooraan», #68 «MiDNI is de nieuwe manier om je te identificeren»,
  #82 «Dit jaar kun je stemmen met MiDNI», #88 «Alleen gratis zendtijd,
  met bron», #92 «Peiling: foto met foutmarge, op één dag», #133 «Eerst
  de tijd, dan het werkwoord», #137/#138 «Vgl. origineel.» (zelfde nota
  voor beide — #137 blijft 2 regels per adjudicatie omdat de key alleen
  de regel vult; «Vgl. het origineel.» ook 2 regels voor #137, en #138
  met «Vgl. het origineel.» was 2 regels maar met «Vgl. origineel.» is
  1 regel), #148 «het stembiljet in de envelop» (Spaanse uitbreiding
  laten vallen), #149 «Hoe laat sluit het?». 2-regelige wraps behouden
  per adjudicatie: #44/#139 (core-consistent), #1 (bevroren key «13» +
  volledige-zin-nota «De campagne begint op vrijdag 13 november om
  middernacht», zoals de/pt), #137.
- **Build 2:** run rc=0, 0 OVERFLOW/TOO WIDE, TOTAL 150; P2 col3 1051,0;
  P3 col3 1594,75; P4 col3 993,5; P5 col3 1574,55; P6 col3 1241,55;
  P7 col3 **1873,51** (doel 1865,51; +8 onverklaard — GEEN
  lijnhoogte-veelvoud (29/27/26,5/30,5); de occlusion-audit is de poort,
  en +8 zet de banner-inktbodem op ≈2582, nog steeds onder 2596,5);
  P8-keys y=2506 (54 px reserve).
- **Render 2:** rc=0, print 3.502.245 B, web 850.410 B. **Occlusion:
  1 flag** — `[LINEX] p1-portada.svg 'openbaar.' — later line box
  [87.4, 1843.4, 1862.6, 1844.6] crosses ink`. Sweeps: bridge orphans 0;
  box-vs-hline-telling was afgekapt in de command-tail — opnieuw
  gedraaid bij build 3 (0).

### P1-gloss root cause (nl, gediagnosticeerd 2026-11-11)

De gloss wordt getekend door `p.para(gx, my + 108..., "...", 19, "sans",
False, GREY, gw, 1.35)` in content12.py:116, d.w.z. op breedte `gw`
(niet CW). De toegepaste gloss «„Debat”: mensen discussiëren in het
openbaar.» heeft tekstbreedte 423,375 eenheden op 19 sans — hij wrapt
naar **2 regels** bij elke breedte 360–422,5 (direct gemeten). Regel 2
(«openbaar.») landt op de y=1844-scheider (rij-B hline op 1844;
illustratie begint 1874). Kandidaten gemeten 1 regel op breedte 378,5:
«„Debat”: mensen praten in het openbaar.» (371,5 eenheden), «„Debat”:
een openbaar gesprek.» (292,3), «„Debat”: mensen discussiëren openbaar.»
(369,0). De `gw`-waarde zelf werd niet vastgelegd (grep op `gw =` in
content12.py gaf niets in de zichtbare output — de variabele is elders
gedefinieerd; de sweep 360–422,5 dekt het plausibele bereik, dus elk van
de drie kandidaten past bij elke plausibele gw, maar verifieer de gekozen
tekst op de exacte gw na het vinden ervan).
**Extra meting na build 2:** «„Debat”: mensen debatteren in het
openbaar.» = 411,0 → 2 regels op 378,5 (past niet); «„Debat”: een
discussie in het openbaar.» = 356,0 → 1 regel ✓. **Gekozen: «„Debat”:
een discussie in het openbaar.»** — behoudt «discussie» (het
debat/discussie-zelfstandig naamwoord) en «in het openbaar»; de
«twee of meer mensen / om de beurt»-details staan in de Spaanse definitie
erboven en in de P7-woordbox-gloss. Parallel aan de de-gloss «„Debatte”:
Menschen diskutieren öffentlich.» en fr «« Débat »: des personnes
discutent en public.»

- **Build 3 (definitief):** P1-gloss vervangen; run rc=0, 0 overflow,
  TOTAL 150; P3 1594,75; P5 1574,55; P7 1873,51; P8-keys y=2506.
  Render rc=0 (print 3.502.220 B; web 850.386 B); occlusion **0 flags**;
  sweeps 0/0 (bridge orphans 0 over 20 bridges; box-vs-hline 0 —
  opnieuw bevestigd, niet alleen uit de afgeknotte build-2-tail).

## Gates (build 3)

- p8 extract 150/150, compare CLEAN, keydiff=[137, 138] — adjudicated
  (opnieuw gericht: Nederlandse-zin-keys «Maandag is het Internationale
  Flamencodag. — Vgl. origineel.» / «Zaterdag kijken we naar de derby
  van Sevilla. — Vgl. origineel.»).
- Freeze tool 8 OK + directe sha256 8/8 (`freeze-es-nl-3/build-copy/svg`
  vs verzonden `svg/`).
- pdftotext print = web, 45.724 B byte-identiek.
- P8-minimumletter 10,125 pt — pypdf `Tm`-parse van print-PDF P8 gaf
  min d = 106,5 over 150 entries, identiek aan core EN es-en (de eerdere
  edities' «10,125pt» is 106,5 geschaald door de embedded-form-factor;
  gelijk-aan-core is de operatieve check).
- §1.1: papier #fbfaf6 ×8, VOL.4 ×9, VOL.5 ×3, chips A2 11 / B1 21 /
  B2 3 = 35 chip-rects **plus** één #37402f kopband-rect (core heeft
  dezelfde 4 #37402f rects — mijn eerste telling van 4 leek fout tot ik
  core controleerde), Q113–150 allemaal met badge; full-width
  leestekens 0 in .py en SVG-tekst (de 118 U+3000 ideografische spaties
  zijn de titel-scheider, zoals in core); CJK alleen mottitel (P1);
  gloss-tokens allemaal ≥2 (zelfde aantallen als en/de).
- AGENTS.md (weekly-git) opnieuw gelezen 2026-11-11 (runtime house-rules
  note): geen nieuwe beperkingen voor dit productie-werk; insert/lint/
  push blijven de coördinator.

## Visual (8 PNG's, allemaal schoon)

- P1 gloss 1 regel, vrij van de scheider; masthead, pairing line,
  1-regelige gloss, cijfers-box, quiz.
- P2 titel «EL CALENDARIO　De kalender» past, Note-box vrij, C-intro
  1 regel onderaan kol 2, ¿Y TÚ?-box 5 regels binnen de box.
- P3 ¿Y TÚ?-box boven de scheider; B-bridge 2 regels samen in kol 2.
- P4 ¿Y TÚ?-box 5 regels boven de wedstrijdtabel; A-bridge 2 regels samen.
- P5 ¿Y TÚ?-box boven de scheider; B-bridge 2 regels samen in kol 1,
  woordenlijst bovenaan kol 2; C-bridge 2 regels samen in kol 2.
- P6 band-subtitle volledig; A-bridge 2 regels samen in kol 1; D-bridge
  2 regels samen in kol 4.
- P7 woordbox-gloss 2 regels; brief halve haakjes; redactionele noot
  4 regels binnen de box; banner ruim boven footer; ERRORES-notes 1
  regel elk.
- P8 RESPUESTAS-kop + nota vrij van zwaan-caption; keys eindigen ruim
  boven footer; alle 150 keys zichtbaar; Q113–120, Q145–149 chips
  aanwezig; #1 2 regels, #44 en #139 2 regels, #137 2 regels (alle
  geadjudificeerd); #150 ✓-vorm.

## 150-key verification

Volledige REG-dump gelezen (`es-nl-keys.txt`, 150 regels); matching-sets
letter-voor-letter geverifieerd: 25–28 (debate=debat c, mitin=bijeenkomst b,
cartel=poster d, escaño=zetel in het parlement a), 52–55
(jornada=speelronde c, derbi=derby b, liderato=eerste plaats a, fase
liga=competitiefase d), 141–144 (sondeo=peiling c, muestra=steekproef d,
margen de error=foutmarge b, junta electoral=verkiezingscommissie a).

## `.text.md`

1.816 regels, volledig gelezen (Nederlandse laag regel voor regel;
Spaans bevroren zoals in core); nummers 1–150 allemaal aanwezig; 0 CJK;
geen «12 de noviembre». Geëxporteerd met `extract_text_es_nl.py`
(gekopieerd van `extract_text_es_pt.py`, sed es-pt→es-nl, grep-geverifieerd
geen residu).

## es-nl deliverables (alle in `~/workspace/weekly-git/production/2026-w47/2026-w47-es-nl/`)

- `La-Lucerna-VOL4-es-nl.pdf` — 3.502.220 B,
  SHA-256 `f88a21414c77508b8eb1a26af763e027fb5a1eed657b6fb576097ede8171dab1`
- `La-Lucerna-VOL4-es-nl-web.pdf` — 850.386 B,
  SHA-256 `85240de829be675577d03467f8697e8bf2f7814fb1de022a20f2290da9a4bcb3`
- `2026-w47-es-nl.text.md` (1.816 regels)
- `ABSTRACT.txt` (Nederlands, één regel, geen ASCII-dubbele
  aanhalingstekens, 455 bytes): «La Lucerna Spanish Weekly VOL.4 — Spaans
  leren door te lezen: de eerste week van de Spaanse verkiezingscampagne,
  het laSexta-debat op 13 november, de algemene verkiezingen op 29
  november, stemmen per post tot 19 november, de Internationale
  Flamencodag op 16 november, Sint-Cecilia op 22 november, speelronde 13
  van La Liga en de Champions League; Spaanse teksten met Nederlandse
  uitleg, niveaus A2–B2, 150 oefeningen over de onderwerpen van deze week.»
- `WEEKLY-KIT.md` (adjudicaties §6.1–§6.14; 4-ronden zelfproefleesrecord;
  laatste ronde nul bevindingen)
- 8 SVG in `svg/`, 8 PNG in `cards/`

**Self-check conclusion: zero known defects; awaiting independent proofreading.**

## Records

`scratch-fanout-es/es-nl.md` (dit bestand), `es-nl-build1/2/3.log`,
`es-nl-render2/3.log`, `es-nl-freeze.log`, `freeze-es-nl-3/`,
`es-nl-keys.txt`, `extract_text_es_nl.py`, `2026-w47-es-nl-apply.json`;
`FANOUT-REPORT-es.md` updated (es-nl line added, checklist checked).
