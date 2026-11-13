# PROOF-NOTE — W47 de-fr, proof2 (independent re-proofread)

- Proofreader: proof2 (independent; different person from builder / core builder / proof1)
- Date: 2026-11-11
- Object: `production/2026-w47/2026-w47-de-fr/` (repo main, `~/workspace/weekly-git`)
- KIT: `WEEKLY-KIT.md` — rebuild 5 (fix1, D1 only), status "independent proofread pending"
- Core: `production/2026-w47/core-de/` (build15)
- Scope: independent full re-read + all mechanical gates run live. Priority re-tests:
  P7 toolbox (box bottom, last baseline, clearance ≥ +10px, 200dpi crop) and
  P8 H-box instruction line + Q67 answer-key note closing-quote gap (de-en proof2 D1/D2 method:
  200dpi pixel ink-column measurement; this edition's quotes are « », measured per actual glyph).
- Sources read: SOP.md §1.1, §8 (full); repo AGENTS.md; proof1 note
  (`hidden_files/w47/scratch-proof-de-fr1/PROOF-NOTE.md`); family-fix log
  (`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-de-toolbox-family/FIX-LOG.md`);
  de-en proof2 note (D1/D2 method).
- No source files modified, no rebuild, no commit, no push.

## Identity (disk-measured 2026-11-11, matches task prefixes; re-verified unchanged at end)

| File | Bytes | SHA-256 |
|---|---|---|
| Print PDF `Die-Lucerna-VOL4-de-fr.pdf` | 10,932,565 | `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413` |
| Web PDF `Die-Lucerna-VOL4-de-fr-web.pdf` | 1,600,197 | `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167` |
| text.md `2026-w47-de-fr.text.md` | 50,042 (48,164 chars) | `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6` |

Both PDFs 8 pages, 1462.5×2025 pt. Web PDF +43,280 B vs rebuild 4 because the
working-tree webpdf.py now embeds a `LucernaNewsreader-Bold` subset (23,780 B);
text.md byte-identical to rebuild 4 (zero content change).
Disk probes passed before work: `echo test | git hash-object -w --stdin` →
`9daeafb9…`; real scratch write OK; disk 150G total, 74G used, 75G free.
TMPDIR pointed at this scratch dir's `tmp/` throughout; nothing written to /tmp.

## Conclusion

**(a) ZERO DEFECTS — this edition is final.**

Defect list: none. Every mechanical gate passed live, the P7 toolbox re-test
clears +10px by both the nominal and the pixel method, the P8/H-box/Q67 quote
gaps are the literal French spaces in the source (not a wide-glyph defect),
the full text.md (1,185 lines) was read, all 150 answer keys were checked
semantically question by question, all 8 pages were viewed in print and P1/P8
in web, and every external fact checked online is confirmed.

Proof1's (a) is now covered: proof1 did not cover the toolbox defect class;
this round re-tested it explicitly and it passes.

## 1. P7 toolbox — 200dpi pixel re-measurement (PASS)

Scripts: `measure_pixels.py`, `measure_pixels2.py`, `measure_pixels3.py` in this
scratch dir. Renders: `render/print7-200-7.png`, `render/crop-p7-toolbox-200.png`.

- Cream block rows 688..1673px = 330.2..803.0 SVG units (nominal box bottom 803.5;
  0.5 unit edge-threshold tolerance).
- Last-entry lowest ink row 1643px = 788.6 SVG units (baseline 783.9, `fraglich`
  descender 4.7 SVG units — matches FIX-LOG).
- **INK clearance = 30px = 14.4 SVG units; BASELINE clearance = 19.1 SVG units**
  (nominal 19.6). Both ≥ +10. **PASS.**
- 200dpi crop viewed: last entry fully inside the cream box, clear cream below
  the `g` descender.
- creambox.py full scan (family copy, all 8 SVGs): P7 toolbox bottom 803.5,
  last baseline 783.9, clearance **+19.6**; LESERBRIEFE bottom 1372.0 clearance
  +10.4; NOCH EIN WORT bottom 1538.0 clearance +42.9. All other pages' boxes
  positive (min +14.0) except two known matcher false positives (see §7).

## 2. P8 quote-gap test — 200dpi pixel ink-column measurement (NO DEFECT)

Clean method: tight band baseline−0.72em..+0.25em, ink columns within each char's
own advance box, no ±2px bleed. Log: `measure-pixels3.log`. Crops viewed:
`render/crop-h-fr-quote.png`, `render/crop-q67-quote.png`.

Actual glyph forms (no U+201C/U+201D in these lines):
- H-box German line: « » tight (`«Meine Novemberwoche»`, Newsreader 16.12pt).
- H-box French line: « » with French spaces (`« Ma semaine de novembre »`,
  Noto Sans CJK SC 15.00pt).
- Q67 key note: « » with spaces (`« Im Lande des Christkinds »`,
  Noto Sans CJK SC 9.94pt).

Results:
- **H-FR** (15pt, em=41.7px): word-boundary ink gaps 12–17px, median 14px = 0.34em.
  « ink 15px = 0.36em, gap before 14px = 0.34em, gap after 16px = 0.38em.
  **» ink 15px = 0.36em, gap before 14px = 0.34em (= line median word gap),
  gap after 5px = 0.12em** (to following period).
- **Q67** (9.94pt, em=27.6px): word gaps 7–11px, median 9px = 0.33em.
  « ink 10px = 0.36em, gap after 11px = 0.40em.
  **» ink 10px = 0.36em, gap before 9px = 0.33em (= line median word gap),
  gap after 9px = 0.33em.**
- **H-DE control** (Newsreader 16.12pt, em=44.8px): « ink 20px = 0.45em,
  » ink 21px = 0.47em, advance 0.55/0.56em — Newsreader guillemets are actually
  WIDER than the Noto Sans CJK SC ones (0.36em ink / 0.48em advance).
  No full-width (1.00em) glyph anywhere.

Judgment: the gap before closing » equals the line's own median word-space gap
in both cases — it is the literal French space in the source (correct French
« » convention), not a wide-glyph defect. The de-en signature (wide gap with
NO space in source) is absent. The bare ">0.2em" threshold would also flag
every normal word space on these lines (medians 0.33–0.34em), so the
discriminating test is gap-vs-own-line word gaps: equal → NO defect.
An earlier crude run (`measure_pixels.py`, full line-height band) was
contaminated by neighbouring lines' descenders at 9.94pt (merged 52px run);
superseded by the tight-band per-char method (`measure_pixels3.py`).

## 3. Mechanical gates (all run live; see GATE-LOG.md)

| Gate | Result |
|---|---|
| occlusion (formal audit, never --selftest) | exit 0; selftest OK (6 planted classes fired); **0 flags**; core 0; NEW vs core 0 |
| p8 extract | **150/150** |
| p8 compare vs core | CLEAN, missing=[], extra_count=0, keydiff=[137, 138, 139, 150] — all 4 expected (137–139 forward DE→FR translation keys in French; 150 open writing task) |
| freeze.py diff | exit 0; added CJK total **7, all U+3000** (P1 0, P2–P8 1 each) |
| freeze_direct (rebuild-A copy, `--core-svg core-de/svg`) | source PASS (removed 520 / added 528, unaccounted 0/0); rendered **8/8**, frozen counts 147/163/195/166/173/175/150/186, sha8 `083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7` (P3 sha changed with Q34 stem, as in rebuild 4) |
| keycheck-150 (rebuild-A) | **149/150 exact**; only Q150 extractor truncation ("Exercice libre — suivez les points de l'encadré d'écriture" → "Exercice libre"), expected |
| boxtitle.py (rebuild-A) | **7/7 fit**; independent re-measure from shipped SVG strings via core `svglib.text_w` reproduced identical values (max 376.9; budget 400.5; max ink end 1838.4, min spare 23.6px) |
| measure.py (rebuild-A) | **24/24 PASS, 0 FAIL** |
| creambox.py full scan (family copy) | §1 above; all positive except known false positives (§7) |
| d2scan.py | 58 abutting pairs, **0 web gaps >0.5pt** |
| verify.py rerun (in edition dir) | exit 0; TOTAL 150; numbering continuous; **SVGs byte-identical before/after**; §1.1 audit True, old-style hexes []; verbatim OK (8 sentences ×2); 17 forbidden terms all 0; P8 floor True (13.25 SVG units = 9.9375pt); MUSTER 84 words; chart 44+33+23=100; date arithmetic 18.11+11 / 15.11+7 / 16.11+6 all True; zero FLOW OVERFLOW / HEAD TOO WIDE; flow ends match KIT (P8-keys 2426, spare 134px) |
| Print/web text layer | `pdftotext -layout` both 115,769 B, word multiset identical (8,121 words); `-raw` both 49,698 B, normalised text exactly identical; web PDF has real text layer |
| P8 min font (PyMuPDF, both PDFs) | **9.94pt** ≥ 9.75pt floor; P1 min 11.62pt |
| Level chips (rx="2.7" rects) | per page 10/15/18/15/18/18/12/35 = **141**; P8 A2 22 / B1 13 / B2 0 |
| Q34 five places | new stem "Am Montag öffnet in Köln der erste ___." 1× in content34.py, text.md, P3 SVG, print text layer, web text layer; old stem 0× in all five. Proof1 D-01 fixed. |
| Bent quotes | text.md U+201C 33 / U+201D 0 / U+201E 33 / U+2019 0 (33 German „ " pairs); « » 7 pairs; U+0027 42. SVG rendered text: P1 5/0/5, P5 6/0/6, P7 21/0/21, P8 1/0/1 (201C/201D/201E), 2019 0 everywhere. No English curly quotes anywhere (de-en D1/D2 class absent). |
| §1.1 palette | SVG hexes all §1.1 values except inherited core-identical sets — P4 table zebra `#f4efe0/#efe8d2`, moth logo `#34483A/#F1E8D4/#7898CD/#4D72B4/#EDD17F/#D7B257/#84A283/#4F765D`, light text on dark bands `#cac8ba` — byte-identical counts in core-de. Fonts: Newsreader 958, Noto Sans CJK SC 787, Noto Serif CJK SC 25, UnifrakturMaguntia 1. |
| Dates (`date -d`, Europe/Berlin) | Nov 3 Tue, 4 Wed, 5 Thu, 6 Fri, 7 Sat, 8 Sun, 13 Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 22 Sun, 24 Tue, 25 Wed, 26 Thu, 27 Fri, 29 Sun — all match the edition's weekday claims |
| ABSTRACT.txt | French single line, no ASCII double quotes, facts consistent |

## 4. Visual reads (100dpi renders from print PDF `render/print-{1..8}.png`; web P1/P8 `render/web-1-1.png`, `render/web-8-8.png`)

- **P1–P8 all viewed, clean**: zero overflow/overlap/footer pressure; images +
  credits in place (P1 football / Staff Sgt. Stephanie Jacobs; P3 Wilhelm Ritter
  1930 painting; P4 Kopfball / DVIDS 2010; P5 Kepler 1903 calendar; P7 Library of
  Congress / Carol M. Highsmith; P8 Fußball 1905 unknown photographer).
- Web P8 viewed: visually identical to print P8. Web P1 viewed: visually
  identical to print P1 (same masthead, lead, photo, FRAGEN DER WOCHE, sommaire,
  BLITZQUIZ). Web/print parity confirmed on both checked pages.

## 5. Full text.md read (1,185 lines, all read) + 150-key semantic check

All 150 keys checked semantically against stems/article/chart (not just
P8==REG): all correct, including Perfekt Q16–20, comparatives Q56–59, weil
Q76–79, chart Q83–88, cloze Q113–120 (A/B/A/B/A/A/B/A), quiz Q121–132,
sentence-building Q133–136 (verb-second/order correct), translations Q137–140
(Q140 reverse FR→DE key is the German sentence, correctly NOT in keydiff),
matching Q141–144 (c/a/d/b), dialogue Q145–149 (A/B/A/A/A), Q25–28 (d/c/a/b),
Q52–55 (d/b/c/a). German/French spelling, agreement, conjugation: no errors
found in full read. French translations of the 8 Sätze der Woche verified
("Le Bayern s'est imposé 2–1 à Mayence", etc.). Leserbriefe = editor's example +
French disclosure per F-MAIL rule. MUSTER 84 words (verify.py counted).

## 6. External facts verified online (browser.search, 2026-11-11) — ALL CONFIRMED

- **Bundesliga MD9 (6–8 Nov 2026)**: Hamburg–Gladbach 3:1; Mainz–Bayern 1:2
  (Kimmich 14', Karl 57', Tietz 90'+3); Dortmund–Elversberg 2:1; Leipzig–Augsburg
  5:2; Paderborn–Frankfurt 2:2; Stuttgart–Bremen 1:0 (Mittelstädt 7');
  Köln–Leverkusen 1:2 (García 7', Schick 85', El Mala 90'+2); Freiburg–Union
  2:0 (Khedira OG 55', Suzuki 67'); Hoffenheim–Schalke 2:1 (Asllani 10',
  Lemperle 26', Adamu 81'); total 30 goals in 9 games; Bayern top on goal
  difference, level 21 pts with Dortmund.
  Sources: bundesliga.com, stefan-jaekel.de, thesportsscout.com, totalodds.co.uk.
- **UCL MD4 (3–4 Nov 2026)**: Atlético–Bayern 0:2 (Karl 54', Laimer 74' —
  official fcbayern.com); Dortmund–Real Betis 2:1; Leipzig–Man City 2:3;
  Stuttgart–Galatasaray 0:2 (Batrakov 12', 15' — ZDF/dpa).
  Sources: uefa.com, fcbayern.com, zdfheute.de.
- **UEL MD4 / Conference MD3 (Thu 5 Nov 2026)**: Leverkusen–Marseille 0:1
  (Gouiri 77'); Crystal Palace–Hoffenheim 1:1 (Prass 7', Kamada 90');
  Trabzonspor–Freiburg 0:1 (Kübler 14').
  Sources: sportradar.com, fussballnationalmannschaft.net, uefa.com.
- **Serbia–Germany, Fri 13 Nov 2026, 20:45, Rajko Mitić, Belgrade**: UEFA
  spectator ban (racist/discriminatory fan behaviour vs Greece 1:2 and
  Netherlands 1:2; €50,000 fine); exemption allows children under 15 with
  teachers/coaches + 50 German fans; ~5,000 expected. Matches the edition's
  "vor fast leeren Rängen (UEFA-Strafe: nur Kinder und 50 deutsche Fans durften
  ins Stadion)" and the KIT's "~5,000 expected". (One source dated 9 Nov 2026
  reported a full ban; the exemption was confirmed 10 Nov 2026 — the edition
  uses the UPDATED correct version.)
  Sources: fussballnationalmannschaft.net, bundesliga.com, GMX, dpa via FOCUS.
- **Germany–Netherlands, Mon 16 Nov 2026, 20:45, Olympiastadion Berlin, ARD**:
  last group game (MD6, Group A2), decides quarter-final; Germany 5 pts (3rd),
  Netherlands and Greece 8 pts each, Serbia 0; top two reach quarter-finals
  March 2027; away leg in Amsterdam 1:1 (24 Sept). Multiple sources call it
  "Endspiel" ("Endspiel in Berlin") — supports the edition's P1 "Endspiel"
  wording. Sources: fussballnationalmannschaft.net, bundesliga.com, ran.joyn.de.
- **Cologne Cathedral Christmas market 2026**: 16 Nov–23 Dec, Roncalliplatz,
  closed Sun 22 Nov (Totensonntag); official opening Tue 17 Nov 2026 19:00 with
  Kinder- und Jugendchor Lucky Kids; Harbour Market from 13 Nov; Markt der Engel
  16 Nov–23 Dec; entry free. Sources: koelnerweihnachtsmarkt.com,
  colognecathedral.de, nrw-tourism.com.
- **Aachen Christmas market 2026**: 20 Nov–23 Dec (53rd edition), opening
  Fri 20 Nov, daily 11:00–21:00, Totensonntag 22 Nov from 18:00 only.
  Sources: aachenweihnachtsmarkt.de (via europa.tips / pixidia / radicalstorage).
- **Wilhelm Ritter**: born 24 Aug 1860 Nuremberg, died 28 Oct 1948 Eschenbach;
  work "Weihnachtsmarkt auf der vorderen Insel Schütt" (1930). Exact match with
  the P3 caption. Sources: de.wikipedia.org, fr.wikipedia.org, wikidata.
- **Buß- und Bettag**: 2026 = Wed 18 Nov; statutory holiday only in Saxony
  (abolished elsewhere with effect from 1995); SächsSFG §6 (revosax.sachsen.de):
  public dance events banned "von 3.00 Uhr bis 24.00 Uhr" on Buß- und Bettag.
  Saxon employees pay the higher Pflegeversicherung contribution (the known
  1995 trade-off). All as in the edition.
- **Kepler "Im Lande des Christkinds"**: first printed Advent calendar, 1903,
  Reichhold & Lang, Munich; 24 verses by Gerhard Lang, 24 colour images by
  Richard Ernst Kepler; 1903→2026 = 123 years ("über 120 Jahre alt"). Sources:
  de.wikipedia.org (Kepler), skjalden.com, cath.ch. (Note: an earlier 1902
  printed clock exists and some sources date Lang's commercial calendar to
  1908; the 1903 "Im Lande des Christkinds" with Kepler images is consistently
  cited as the first printed Advent calendar — the edition's phrasing matches
  the established claim.)
- **Bundeshaushalt 2027**: adoption planned Fri 27 Nov 2026, final debate
  Tue 24–Fri 27 Nov, third-reading roll-call vote Fri 27 Nov.
  Source: bundestag.de (official).
- **Stromsteuer**: 2.05 ct/kWh for households, unchanged since 2003; EU minimum
  0.1 ct; Merz pushing cut for all (~€5bn cost); Klingbeil sees no room in the
  2027 draft yet; coalition agreement promised cut for all; implemented so far
  only for industry/agriculture. As in the edition. Sources: finanznachrichten.de,
  karlsruhe-insider.de, proplanta.de.
- **MD10 fixtures (20–22 Nov 2026)**: Bayern–Köln Fri 20 Nov 20:30;
  Schalke–Stuttgart Sat 21 Nov 18:30; Augsburg–Mainz Sun 22 Nov 15:30;
  Bremen–Hamburg Sun 22 Nov 17:30. Sources: bundesliga.com, DFB Datencenter,
  fussballdaten.de.
- **UCL MD5 (24–25 Nov 2026)**: Arsenal–Dortmund Tue 24 Nov; Leipzig–Lens
  Tue 24 Nov; Inter–Stuttgart Wed 25 Nov; Lille–Bayern Wed 25 Nov.
  Source: uefa.com (official).
- **UEL MD5 (Thu 26 Nov 2026)**: Dinamo Zagreb–Leverkusen 18:45;
  Hoffenheim–Sturm Graz 21:00. Sources: uefa.com, bundesliga.com.
- **P4 table verified by hand**: 9 MD9 matches, goals 4+3+3+7+4+1+3+2+3=30;
  most-goals game Leipzig–Augsburg 5:2 (7 goals); MD10 counts Fri 1 + Sat 6 +
  Sun 2 = 9.

## 7. Observations (NOT defects)

1. P1 "Endspiel" for Germany–Netherlands: journalistic "decisive match"; P4
   clarifies "das letzte Gruppenspiel der Nations League – und es geht um das
   Viertelfinale". Real German press also calls it "Endspiel". No change needed.
2. P1/P7 creambox false-positive rows (inherited matcher class, proven identical
   in core-de): P1 sommaire box −24.0 (heading `DAS WORT DER WOCHE` at y=1676
   sits BELOW the box; last sommaire line 1636 is inside); P7 −35.0 rows
   (A2/B1/B2 BEISPIELE boxes matched against exercise numbers below them).
   Core-de P1 shows the identical −24.0 row; core toolbox clearance +18.8.
3. '·' (U+00B7) in rendered text is the inherited core class (core P8 also 192;
   fr P1 12 vs core 11, +1 from a French gloss line) — used inside answer
   keys/glosses/options, not as furniture separator (furniture uses U+3000;
   verified footer/pageline/kicker use U+3000).
4. Non-§1.1 hexes all inherited from core (moth logo, table zebra,
   light-on-dark text) with byte-identical counts in core-de.

## 8. Files in this scratch dir

`occlusion.log/.json`, `p8extract.log/.json`, `p8compare.log/.json`,
`freeze.log/.json`, `freeze-direct.log/.json`, `keycheck.log`, `keycheck-150.json`,
`boxtitle.log`, `measure.log`, `creambox-all.log`, `d2scan.log/.json`,
`verify.log`, `svg-sha-before.txt`, `svg-sha-after.txt` (diff empty),
`print.txt`, `web.txt`, `print-raw.txt`, `web-raw.txt`,
`measure-pixels.log`, `measure-pixels2.log`, `measure-pixels3.log`,
`measure_pixels.py`, `measure_pixels2.py`, `measure_pixels3.py`,
`render/print-{1..8}.png`, `render/web-1-1.png`, `render/web-8-8.png`,
`render/print7-200-7.png`, `render/print8-200-8.png`,
`render/crop-p7-toolbox-200.png`, `render/crop-h-fr-quote.png`,
`render/crop-q67-quote.png`, `render/crop-h-de-quote.png`, `tmp/`.

## 9. Path note for the parent

The task brief's FIX-LOG and rebuild-A script paths live under the goals
workspace (`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/…`),
not under weekly-git's `hidden_files/w47/`; the canonical
`hidden_files/w47/tools/creambox.py` does not exist in weekly-git, so the
family-fix copy was used. freeze_direct/boxtitle/keycheck/measure were run
from the rebuild-A copies as instructed (fr/it `scratch-fanout-de/tr_*.py` are
stale and were NOT used).
