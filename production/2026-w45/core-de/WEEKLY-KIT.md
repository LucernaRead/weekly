# WEEKLY-KIT — Die Lucerna · 德语周报 VOL.2 (W45)

Issue week: **Mon 2 – Sun 8 November 2026**. Issue dated **Mon 2 November 2026**.
Edition: **Deutsch core** (target language German, explanation layer Chinese).
Status: **FIX1 (2026-10-26)** — independent-proof fixes applied, re-rendered,
occlusion-audited to zero flags (see §14). **NOT re-finalized**: a fresh full
independent proof round is still required before delivery/insert.
No git push, no Discord post from this build (delivery is the parent line's job).

## 1. Spec

- 8 pages, 1950×2700, 4 columns, warm ivory paper `#f7f1e2`, dark olive-green
  accents, blackletter masthead.
- Masthead: **Die Lucerna** — Latin feminine noun; German cognate image
  *die Laterne*. Footer: `Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY`
  + `第 N 版 / 共 8 版`.
- Ramp: P1 front A2 · P2 life A2 · P3 culture A2→B1 · P4 sport B1 · P5 youth B1 ·
  P6 deep read B2 · P7 language focus (A2/B1/B2 columns) · P8 assessment +
  writing + ALL keys. Levels mix freely; every exercise individually badged.
- Explanation-layer convention (same as the W43 DE core): German core text +
  explanations in Chinese — small gray glosses/notes/answer explanations only;
  gloss prefix `译注｜`; section heads German · Chinese. No “桥接” wording
  anywhere; the explanation layer is 讲解.
- ~150 exercises, continuously numbered 1–150, registration table generating
  the P8 answers. P8 style for the core: full-width parens `（note）` in core
  code (fan-outs use half-width; core keeps its own code path).
- P7 golden sentences are verbatim contiguous excerpts from THIS issue's own
  articles, programmatically verified to occur exactly 2× in rendered SVG text
  (article + P7). See §5.
- Practice charts labeled `ÜBUNGSDATEN / 练习数据` on the page.

## 2. Contents per page

- **P1 Front (A2, 10 ex.)** — Lead: “Englische Woche in Deutschland: Vier
  Nächte Fußball, dann der 9. Spieltag.” (fix1: was “Vier Nächte Europa” —
  only 3 Europe nights exist; Friday is Bundesliga.) Dark band “ENGLISCHE
  WOCHE — DANN DER 9. SPIELTAG!” Top strip `VOL. 2 · ZWEITE AUSGABE` /
  `WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语` / `WOCHE VOM
  2. BIS 8. NOVEMBER 2026`. “DIE WOCHE IN ZAHLEN” box (9 Spiele / 6 Teams in
  Europa / 14,04 Cent — fix1: was 4, but the edition names 6 European teams).
  Fragen der Woche (5 questions, bars only — no invented search volumes).
  Sommaire. Word of the week: `« der Tankrabatt »`. Row B: photo +
  mini-feature “EINE WOCHE, VIER NÄCHTE” + KURZ & GUT. Blitzquiz 4 MC.
  Exercises: 6 JETZT ÜBEN + 4 Blitzquiz = 10.
- **P2 Leben (A2, 18 ex.)** — “Tanken für weniger: Der Tankrabatt läuft bis
  Silvester.” 5 paras: Tankrabatt, 50-Liter saving, pass-through warning,
  Stromsteuer/ZEW, Pflege + ARD “Hart aber fair” pointer. Col 3: 4 hand-rolled
  boxes — AN DER ZAPFSÄULE, WUSSTEN SIE DAS?, UND SIE?, ZEW IN KÜRZE (no
  photo on P2). Wide box “RECHNEN WIR MAL · 算一算” (50 Liter × 14,04 Cent =
  7,02 €; mit Mehrwertsteuer rund 8,35 € — fix1: 50 × 16,7 ct = 8,35 €, not
  8,50 €; Staat rund 2,5 Milliarden €; ADAC note right). Exercises: A WIE VIEL
  SPAREN? (5) + B DAS PERFEKT (5) + C LESEVERSTEHEN (4) + D DIE WÖRTER match
  (4) = 18.
- **P3 Kultur (A2→B1, 18 ex.)** — “Ferienwechsel: Die einen kommen, die
  anderen gehen.” 6 paras: BW back at school / Bayern still on holiday,
  November/Herbst, Rückblick Oct 31 Halloween + Reformationstag + Klassiker
  (Bayern in Dortmund, fixture only, no result — added in fix1) and Nov 1
  Allerheiligen (as reports, never previews), museums/libraries, Bundesliga
  weekend, St. Martin lanterns coming Nov 11. Col 3: FERIENWECHSEL facts +
  HERBSTWÖRTER vocab + UND SIE? + DER TIPP (no photo on P3). Exercises:
  A RICHTIG ODER FALSCH? (5) + B WÖRTER (5) + C LESEVERSTEHEN (4) +
  D SÄTZE BAUEN (4) = 18.
- **P4 Sport (B1, 18 ex.)** — “Englische Woche: Vier Nächte, dann der
  Spieltag.” 6 paras: European week, Tue Bayern/Stuttgart, Wed
  Dortmund/Leipzig, Thu Hoffenheim/Leverkusen, Bundesliga MD9 preview, NFL
  Munich Nov 15 teaser. Col 3: photo + caption + UND SIE?. Full-width fixture
  table “DER 9. SPIELTAG” (8 rows, §4), note that all times are MEZ and the
  Hertha row is 2. Bundesliga. Exercises: A LESEVERSTEHEN (5) + B DIE WÖRTER
  match (4) + C KOMPARATIV (4) + D DIE UHRZEITEN from the table (5) = 18.
  Section D deliberately uses fixture-table times, NOT match results, because
  no W45 match has been played at build time.
- **P5 Jugend (B1, 18 ex.)** — “Zurück in die Schule — und Bayern hat noch
  frei.” 5 paras: BW school restart Nov 2, Bayern still free, first school
  week, libraries/sport halls, Bundesliga weekend. Col 3: FERIENWECHSEL facts
  + SCHULWÖRTER vocab + UND SIE? (no photo on P5). Wide Wochenplan box
  spanning cols 0–2 via `span_x(0, 3)` (note: W43 code comments said “cols
  0-2” but `span_x(0, 2)` is actually 2 columns wide; W45 P5/P6 wide boxes
  deliberately use `span_x(0, 3)` = 65..1423, leaving col 3 clear).
  Exercises: A LESEVERSTEHEN (5) + B WÖRTER (6) + C SÄTZE MIT «WEIL» (4) +
  D RICHTIG ODER FALSCH? (3) = 18.
- **P6 Vertiefung (B2, 18 ex.)** — “Pflege zu Hause: Wer hilft den
  Angehörigen?” 6 paras: ARD Pflege debate, everyday caregiving, policy
  options, Stromsteuer + ZEW, Wambach quote, closing pattern sentence.
  Col 3: DIE ZAHLEN numbers box (6 rows) + DIE DEBATTE IN EINEM SATZ
  paraphrase box (deliberately NOT the verbatim Wambach quote, so the P7
  verbatim check stays at exactly 2 occurrences). Pro & Contra wide box at
  fixed y=1120 (W43 patch position; flow bottom is 1080). Practice chart at
  cy=1420, labeled ÜBUNGSDATEN, bars at scale 17: 68% Angehörige zu Hause /
  20% Pflegedienst / 12% Pflegeheim; Chinese labels at MX+360 (not MX+330, to
  clear the bold 28-char German label). Exercises: A DAS DIAGRAMM LESEN (6) +
  B LESEVERSTEHEN B2 (4) + C GRAMMATIK (4) + D WÖRTER DER DEBATTE (4) = 18.
- **P7 Sprache (12 ex.)** — Intro paras. A2 lesson DIE ZAHLEN & «WERDEN»,
  B1 VERGLEICHE & GRÜNDE, B2 MEINUNG SAGEN — 4 exercises each = 12. Col-3
  rail: toolbox (6 items), readers' corner (labeled editor's example +
  invitation, §6), NOCH EIN WORT `«der Tankrabatt»`. 8 phrases of the week
  (§5). Error clinic (4 fresh items: verb-second, halb acht, Partizip II
  final, ob-clause verb-final). Teaser box at ty=2400 for VOL.3: Sun Nov 15
  Volkstrauertag + NFL Munich game, St. Martin Nov 11 (added in fix1 so P3's
  "Mehr dazu in der nächsten Ausgabe" pointer lands), Europapokal return
  legs, invitation for real letters.
- **P8 (38 ex.)** — Battery Flow 194→1505: A LÜCKENTEXT Lena football week
  (8 cloze) + B WISSENSFRAGEN (8 MC) + C LESEVERSTEHEN Familie Berger (4) +
  D SÄTZE BAUEN (4) + E ÜBERSETZEN DE↔ZH (4) + F WÖRTER PAAREN match (4) +
  G DIALOG Lena football dialogue (5) = 37, plus H SCHREIBEN (1, registered
  directly) = 38. Writing task: «Meine Fußballwoche», 80–100 words; MUSTER
  model counted at **84 words** (fix1: was 83; adding "rund" before 8,35 €
  adds one word; recount verified, still inside 80–100). MUSTER box height 300
  (W43 used 276); keys start ky = wy+320 = 1840; keys Flow 1888→2560.

## 3. Measured totals

- **150 exercises**: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 ·
  P8 38. Numbering continuous 1–150 (verified from REG).
- By level: **A2 66 · B1 70 · B2 14**. B2 is light (same as W43's 14) — the
  B2 load sits on P6 + P7; noted honestly, not inflated by re-labeling B1
  items.
- By type: 单选 52 · 完成句子 41 · 句型转换 11 · 词汇配对 12 · 判断对错 8 ·
  完形填空 8 · 造句 8 · 对话补全 5 · 翻译 4 · 写作 1 = 150.
- Text volume: **38,533 chars** (SVG text elements summed, no separators;
  original build was 38,043; W43 was 40,036).
- Files (fix1 final render): print PDF `Die-Lucerna-VOL2.pdf` 17,030,165
  bytes, 8 pages, 1462.5×2025 pt; web PDF `Die-Lucerna-VOL2-web.pdf`
  3,994,642 bytes, 8 pages, 1400×1938 pt (JPEG pages q85 @1400px; under the
  10 MB insert limit). Cards: 8 PNGs @1950px in `cards/`.

## 4. Trend/fact sources and verification notes

- **Dates/weekdays** verified with `date -d` (Europe/Berlin): Nov 2 Mon,
  Nov 3 Tue, Nov 4 Wed, Nov 5 Thu, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Nov 9
  Mon, Nov 15 Sun, 2026; Oct 26 Mon, Oct 31 Sat, Nov 1 Sun, 2026. No public
  holiday falls inside Nov 2–8 in Germany. Allerheiligen Nov 1 is just
  before; Volkstrauertag Nov 15 and Buß- und Bettag Nov 18 are after.
  Oct 26 / Oct 31 / Nov 1 items are just-passed W44 items — covered as
  reports, never as previews.
- **Football — kickoff-time debt RESOLVED.** The trend pool's 14:30 vs
  15:30 variance was a UTC-vs-CET label difference. Official bundesliga.com
  listings are UTC; Germany in November is CET = UTC+1. Print **CET
  consistently**. Bundesliga matchday 9: Fri Nov 6, **20:30** Hamburger SV –
  Borussia Mönchengladbach; Sat Nov 7, **15:30** Borussia Dortmund –
  Elversberg, Paderborn – Eintracht Frankfurt, Mainz 05 – Bayern München,
  RB Leipzig – FC Augsburg; Sat Nov 7, **18:30** VfB Stuttgart – Werder
  Bremen; Sun Nov 8, **15:30** FC Köln – Bayer 04 Leverkusen; Sun Nov 8,
  **17:30** SC Freiburg – FC Union Berlin; Sun Nov 8, **19:30** TSG
  Hoffenheim – Schalke 04. FIFPlay CET table corroborates all nine.
  UCL matchday 4 (UEFA.com, 21:00 CET unless stated): Tue Nov 3, 18:45
  Galatasaray – Stuttgart; Tue Nov 3, 21:00 Atlético Madrid – Bayern
  München; Wed Nov 4, 21:00 Borussia Dortmund – Real Betis Sevilla and RB
  Leipzig – Manchester City. UEL matchday 4: Thu Nov 5, **18:45 CET** Crystal
  Palace – TSG Hoffenheim at Selhurst Park (17:45 GMT per Crystal Palace
  official site + Radio Times); Thu Nov 5, 21:00 CET Bayer Leverkusen –
  Marseille. 2. Bundesliga matchday 11 (per pool): Hertha BSC – VfL Wolfsburg
  Sat Nov 7, 20:30.
- **No invented results.** Oct 31 Klassiker (Bayern in Dortmund) result is
  not knowable at build time (built Oct 26) — the W45 Rückblick does NOT
  invent a score. CORRECTION (fix1): the original KIT claim that the
  Rückblick "mentions the fixture without a result" was FALSE — the shipped
  W45 text never mentioned the Klassiker at all ("Klassiker" 0×). Fix1 added
  one result-free sentence to the P3 Rückblick: "Ebenfalls am 31. Oktober
  spielte Bayern in Dortmund — der Klassiker." Same rule for all W45
  matches: previews only, no invented results. This is why P4 section D
  drills fixture times, not results. UEFA MD3 results now stale —
  NOT reported as fresh: Bayern 2–2 Arsenal, Real Madrid 4–1 Leipzig on
  Oct 21.
- **Tankrabatt:** Bundestag + Bundesrat approved Fri Sep 25, 2026;
  Energiesteuer on petrol/diesel cut **14.04 cents/litre Oct 1 – Dec 31,
  2026**, ≈16.7 cents/litre at the pump including VAT; ≈€2.5bn revenue cost
  split roughly half federal / half Länder; stations NOT legally required to
  pass on the full cut (Bundeskartellamt: ~78–82% pass-through in past
  rounds; Oct 1 morning prices fell ~14–15 cents, noon hikes erased much of
  it per ADAC). No war-related cause is mentioned (international-politics
  red line). Arithmetic note (CORRECTED in fix1): 50 × 14.04 = 7.02 € exact;
  with 19% VAT that is 50 × 16,7 ct = **8,35 €**, printed as “rund 8,35 €”.
  The original “rund 8,50 €” (press-standard 50 × 17 ct rounding) was wrong
  against the edition's own printed 16,7 ct chain and has been replaced
  everywhere (article, boxes, P7 phrase 3 + toolbox, P8 MUSTER, P2 exercise
  key).
- **ZEW October 2026** (verified against ZEW release reporting, Oct 20,
  2026): Konjunkturerwartungen fell 6.6 points to **28.1** (from 34.7);
  Lageindikator rose 11.2 points to **−35.9** (from −47.1); president Achim
  Wambach: “Die deutsche Wirtschaft kommt langsam aus der Stagnation
  heraus, doch der Aufschwung trägt sich nicht selbst.”
- **IMF / Bundesregierung (per pool):** IMF raised 2026 Germany forecast 0.7%
  → 1.3% (Oct 13 outlook); Bundesregierung autumn forecast Oct 8: 1.3% for
  2026, 1.1% for 2027. Not printed in W45 articles except where noted.
- **Pflege debate — VERIFICATION DEBT (attribution now explicit
  everywhere, fix1):** per pool, attributed to ARD “Hart aber fair”
  Oct 26, 21:00, “Pflege zu Hause — Lässt die Politik Angehörige
  allein?”: over 6 million people in need of care in Germany, most cared
  for at home by ~10 million relatives. A fresh web search on 2026-10-26 did
  NOT independently re-verify these two numbers — that limitation still
  stands. What fix1 changed: the numbers are no longer bare facts anywhere.
  Every presentation now carries the programme attribution — P2/P6 articles
  ("Nach Angaben der ARD-Sendung …" / "Nach Angaben der Sendung …" after
  the dated programme sentence), P2 WUSSTEN box and P6 DIE ZAHLEN box
  (programme + date parentheticals), P8 keys Q90/Q92 (Chinese attribution
  notes) — and every programme mention is dated Oct 26 in past tense.
- **Stromsteuer debate** (per pool, Tagesschau Oct 26 digest): Union and SPD
  “weiter weit auseinander”; also Gebäudetyp E for faster/cheaper building;
  Wärmepumpe uptake with months-long waits.
- **Other pool items:** Digitales Führungszeugnis as PDF via BundID from
  Oct 1, 2026 (€13); Deutsche Bahn alcohol ban at ~5,400 stations from
  Oct 15, 2026. Not headlined in W45.
- **School holidays (Ferienwechsel angle):** Baden-Württemberg Herbstferien =
  week of Oct 26 (Le Boat European school-vacation table: BW listed in week
  26/10–01/11, NOT in week 02/11–08/11). In W45, BW pupils are **back at
  school from Mon Nov 2**; Bavaria still has Herbstferien in week Nov 2–8
  (Le Boat lists only Bavaria for 02/11–08/11; standard KMK pattern Nov
  2–6). **Register correction:** the W43-promises register's claim that BW
  holidays were “in progress” during W45 appears wrong — W45 treatment is
  “BW zurück in der Schule, Bayern noch in den Ferien.” No Bavarian end date
  more precise than “in dieser Woche” is printed unless re-verified. P1
  mini-feature wording “am Montag... geht es überall wieder los” (Mon Nov 9)
  is used because by Nov 9 all states are back (BW back Nov 2; Bavaria last
  in week Nov 2–8).
- **Rejected material (not used):** foreign-affairs feed items; Nov 9
  anniversary framing (an anniversary is commemorative marketing, NOT a
  living trend — user verdict 2026-10-20, FINAL); any implied German federal
  election (none exists this week). Trend rule: material selection starts
  from the target-language ecosystem's ACTUAL current heat.

## 5. P7 phrases of the week (each verified exactly 2× in rendered SVG text)

1. “Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.” —
   Seite 4 · B1 — “连续四个足球之夜，然后是整周末联赛。”
2. “Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.” —
   Seite 2 · A2 — “汽油和柴油的能源税每升降低 14.04 欧分。”
3. “Wer 50 Liter tankt, spart rund 8,35 Euro.” — Seite 2 · A2 — “加 50 升油，
   大约省 8.35 欧元。” (fix1: was 8,50/8.50; see §4 arithmetic note.)
4. “Die Schule hat nach den Herbstferien wieder begonnen.” — Seite 5 · B1 —
   “秋假过后，学校又开学了。”
5. “Die Tage sind kurz, die Abende lang.” — Seite 3 · A2 — “白天短，夜晚长。”
6. “Zwei schwere Auswärtsspiele für die deutschen Teams.” — Seite 4 · B1 —
   “德国球队的两场艰难客场之战。”
7. “Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der
   Aufschwung trägt sich nicht selbst.” — Seite 6 · B2 — “德国经济正在缓慢走出
   停滞，但复苏还不能自我维持。”
8. “Es geht langsam aufwärts — aber von allein geht es nicht.” — Seite 6 ·
   B2 — “缓慢向好——但不会自动变好。”
- Construction rules: each phrase is its own sentence (or a clean substring)
  in its article. Phrase 2 required splitting the P2 sentence: “…sinkt um
  14,04 Cent pro Liter. Das gilt bis zum 31. Dezember 2026.” Phrase 7 must
  NOT also appear in the P6 col-3 box (that box uses paraphrase instead).
  P1 para 1 uses “Vier Nächte Fußball, dann ein ganzes Wochenende Liga.” —
  now the same wording family as phrase 1 (fix1: was "Europa"); phrase 1
  itself is the P4 sentence and is unchanged.

## 6. Readers' corner — honest note

W43 P7 had promised “VOL.2 druckt Ihre Briefe!” — but no real letters were
available for VOL.2, so W45 carries a **clearly labeled editor's example**
instead of a fabricated letter. P7 prints: label “Ein Beispiel der
Redaktion!”, example “„Liebe Lucerna, am Dienstag schaue ich Bayern bei
Atlético. Die Fußballwoche ist toll! Viele Grüße — die Redaktion“”,
invitation “Schreiben Sie uns Ihre Sätze und Ihre Texte von Seite 8! Die
besten echten Briefe drucken wir in VOL.3.”, Chinese “编辑部示例，非真实来信：
截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。”
**Deferral disclosure (fix1, ON THE PAGE, not only here):** "Bis
Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3." —
no real reader letters or best VOL.1 P8 texts had arrived by press time, so
this issue prints the labeled editor's example and the promise carries to
VOL.3. P7 teaser and P8 writing prompt both invite real letters/texts for
VOL.3; neither claims any real letter exists. W43 promises honored where
they fall in Nov 2–8: VOL.3 teaser covers Nov 15 Volkstrauertag + NFL
Munich game (both in W46, Nov 9–15) plus St. Martin Nov 11 (fix1). Oct 31 /
Nov 1 items are treated as Rückblick reports on P3, not previews.

## 7. Images

Both public domain, in build `assets/`:

- **P1 `fussball.jpg`** (1000×665 JPEG, quality 92, converted from served
  WebP with PIL from `tools/venv`): U.S. Air Force photo by Staff Sgt.
  Stephanie Jacobs, Armed Forces Men's Soccer Championship, Morgan Sports
  Complex, Destin, Fla., Oct 24, 2010. DVIDS page marks it PUBLIC DOMAIN;
  Commons file `File:Armed_Forces_Soccer_Tournament_DVIDS333458.jpg`.
  Download URL used verbatim from the DVIDS page Images footnote:
  `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/1010/333458/1000w_q95.jpg`
  (preflighted 200 OK). Printed credit: “Foto: Staff Sgt. Stephanie Jacobs,
  U.S. Air Force — public domain”.
- **P4 `kopfball.jpg`** (1000×665 JPEG, quality 92): header duel, Navy
  (yellow) vs Army (white), Armed Forces Men's Soccer Championship Round
  Robin, Morgan Sports Complex, Destin, Fla., Oct 18, 2010. DVIDS Photo ID
  333408, VIRIN 101018-F-7705D-151, 4256×2832, PUBLIC DOMAIN. Source page
  verbatim: `https://www.dvidshub.net/image/333408/armed-forces-soccer-team`.
  Download URL used verbatim from that page's Images footnote:
  `https://d1ldvf68ux039x.cloudfront.net/thumbs/photos/1010/333408/1000w_q95.jpg`.
  Printed credit: “Foto: DVIDS (Armed Forces Soccer Championship, Destin,
  Florida, 2010) — public domain”. Caption describes the scene generically;
  it does NOT claim the photo shows a Bundesliga or European match.
- Paper-level image decision: P1 + P4 carry real photos; P2/P3/P5 use
  hand-rolled boxes, vocab boxes, and infographics (P2 price graphic, P6
  practice chart). W43 had 4 photos; the SOP “must have real pictures” rule
  is satisfied at issue level.
- Rejected (do NOT use): Margolies “Old gas station, Wichita, Kansas
  LCCN2017707667.tif” — Commons page shows NO PD license tag (“A normal
  copyright tag is still required”). “Gas station in Plain City, Ohio” — Ben
  Shahn (1898–1969), FSA, 1938, Library of Congress via PICRYL
  (`https://picryl.com/media/gas-station-in-plain-city-ohio`, PICRYL states
  “No known restrictions”) — only a 320×224 thumbnail download was exposed,
  too small for a 434px column slot. Do NOT rewrite URL dimensions. “2011
  Fall Colors (6214881545).jpg” (Bitterroot National Forest, Forest Service
  – Northern Region, Commons
  `https://commons.wikimedia.org/wiki/File:2011_Fall_Colors_(6214881545).jpg`)
  — CC-BY 2.0 only, no PD tag; SOP requires PD/CC0. `/opt/hatch/bin/image-search`
  CLI — returns unlicensed junk (Shutterstock/Pinterest/blog images); not
  usable for PD verification. Working method: Commons/DVIDS/PICRYL/LOC file
  page via search → verify license + Author → download via Images-footnote
  URL with curl preflight. W43 images (frost.jpg / atomuhr.jpg / luther.jpg /
  kuerbis.jpg) are off-theme for W45; do not reuse.

## 8. Build commands (reproduction)

- Build dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-de-build/`
  (`bslib4.py`, `svglib.py`, `run.py`, `content12/34/56/7/8.py`, `assets/`).
  Never run content modules standalone or import them inside the build dir —
  module-level code executes on import and OUT paths point at the shipped
  edition dir. Always run via the copy's single-process driver `run.py`
  (`content12 → 34 → 56 → 7 → 8` in one process so the bslib4 exercise
  registry accumulates).
- Build: `tools/venv/bin/python run.py` in the build dir (one process).
- Render: `tools/venv/bin/python hidden_files/w45/de-core/render.py`
  (cairosvg svg2png @1950 → `cards/`; svg2pdf + pypdf merge → print PDF;
  JPEG pages q85 @1400px → web PDF via PIL).
- Verify: `tools/venv/bin/python hidden_files/w45/de-core/verify.py`
  (REG stats + P7 verbatim + furniture scan + chart graze; re-runs the build
  and confirms SVGs byte-identical).
- Do NOT use `/tmp/wp-venv` — ephemeral. Scratch goes to `tools/scratch/`
  or goal `hidden_files/`, never `/tmp`.

## 9. Self-proofread record (builder's pass, 2026-10-26)

- Full visual pass over all 8 rendered cards (1950px PNGs) + text extraction
  pass over all 8 SVGs.
- All 150 keys re-derived against their prompts, including matching letter
  maps against printed options on P2/P4/P8, chart arithmetic 68+20=88 and
  68+20+12=100, cloze/dialogue option letters, numbering continuity 1–150,
  dates/weekdays, fixture table vs articles, chart arithmetic, same-baseline
  furniture collisions, MUSTER word count (83, recount verified).
- Two suspect keys investigated and cleared from source: 129 = A (halb acht,
  matches the Familie Berger passage) and 149 = A (gehe, first person
  singular, matches “Ich ___ wieder in die Schule”).
- P7 verbatim check: all 8 phrases exactly 2× (programmatic, whitespace
  normalized). Forbidden wording scan: no “桥接”, no “Le Lucerna”, no
  “The Lucerna”.
- Final build: zero FLOW OVERFLOW / HEAD TOO WIDE warnings; total 150.
- Cosmetic-only items kept (same class as W43's lone 。): lone “。” wrapping
  to its own line at the end of the P2/P3/P4/P6 gloss boxes. Content-correct,
  layout-safe.

## 10. Occlusion audit

- Tool: `tools/occlusion_audit.py` (selftest first — passed, all planted
  classes fired, clean controls silent).
- Run 1 on the edition dir: 5 flags — 1 real TEXTX (P1 dark-band title ran
  into the right-side Chinese text), 1 real TEXTX (P2 wide-box value grazed
  its label), 3 BOXTITLE (box titles crossing right borders on P1 Fragen,
  P3 TIPP, P6 ZAHLEN). All 5 fixed by shortening titles/labels and moving
  the P2 value x from lx+330 to lx+360.
- Run 2: **0 flags**. Run 3 (after the final P1 Zahlen shortening):
  **0 flags**. Selftest OK on every run.
- Manual scans (audit blind spots): P1 top-band same-baseline intervals
  65..367 / 651..1299 / 1476..1885 — no overlap; P6 chart labels end at x≤425,
  bars start at x=535, “%” texts sit after bar ends — no graze.
- Audit outputs: `hidden_files/w45/de-core/occlusion-1.txt` (5 flags),
  `occlusion-2.txt` (0 flags), `occlusion-3.txt` (0 flags, final).

## 11. Defects found and fixed during this build

1. **P6-main FLOW OVERFLOW (real):** gloss box drew past the 1080 flow
   bottom and under the fixed Pro & Contra box at y=1120 (painted later,
   opaque fill) — article text would have been covered. Fixed by trimming
   P6 paras (para 1 shortened, para 2 tightened, para 4 shortened, para 6
   second sentence deleted). Phrases 7 and 8 sentences and all ZEW numbers
   untouched. Final: P6-main ends col 2 y=1054 (bottom 1080).
2. **P3 col-3 TIPP box crossed the exercises rule (minor visual):** box ended
   1614.19 vs exercises hline at 1608 — the gold rule would draw through
   the bottom 6px of the box. Fixed by shortening the TIPP text twice
   (final: “Tipp: An einem grauen Nachmittag ins Museum — dort ist es
   warm.”, 2 lines). Final: ends 1583.66, 24px clear.
3. **P7 col-3 rail crossed the phrases rule (real):** rail ended 1603.0 vs
   phrases hline at 1508. Root cause: three toolbox items wrapped to 2 lines
   (mixed Latin+CJK widths) and the readers' box strings were longer than
   estimated. Fixed by shortening toolbox items to guarantee 1 line each
   and shortening the readers' strings (§6 versions). Final: rail ends
   1368.0.
4. **P1 dark-band title overlapped right Chinese text (audit TEXTX):**
   shortened to “ENGLISCHE WOCHE — DANN DER 9. SPIELTAG!”.
5. **P2 wide-box value grazed its label (audit TEXTX):** value x moved
   lx+330 → lx+360.
6. **Three box titles crossed right borders (audit BOXTITLE):** P1 Fragen
   subtitle shortened, P3 TIPP title shortened to “DER TIPP · 编辑部建议”,
   P6 ZAHLEN title shortened to “DIE ZAHLEN · 本周数字”.
7. **P1 Zahlen box orphan paren (cosmetic):** item 2 shortened (dropped “in
   dieser Woche”); box now ends cleanly on 2 lines.
8. **P4 comparative fix (made during writing, before first build):** P4 C-ex
   4 changed from “früher als die anderen Europaspiele” (false —
   Hoffenheim also plays 18:45) to “früher als das Bayern-Spiel” (18:45 <
   21:00, true).
9. **P4 section D design:** deliberately avoids Präteritum drills on unplayed
   matches (would assert results); it drills fixture times instead.

## 12. Geometry lesson (record for future cycles)

- W43's hand-rolled facts-box formula under-counts by ≈21px per item (the
  +21 per-item baseline offset and the +52 header zone vs the formula's
  62). Exact content bottom for a facts-style box = 30.47 + 33k + 30.53×Σn,
  where k = item count and Σn = total wrapped lines (21.5px serif, lh 1.42).
  W45 uses sh = 45 + 33k + 30.53×Σn (≈14.5px slack).
- UND SIE boxes (German 21.5px + Chinese 20px): eh = 140 + 30.53×n_de +
  29×(n_zh−1).
- P6 numbers box (timeline style, text at ix+130, width CW−152):
  tlh = 45 + 30.5k + 29.11×Σn.
- P6 debate box (German 21px + Chinese 19.5px): hh = 140 + 29.82×n_de +
  27.69×(n_zh−1).
- P7 toolbox/readers formulas from the W43 post-patch code are proven:
  toolbox gap 6, trailing pad 110; readers' formula over-estimates (safe
  direction). P7 word box (150 high) fits 3 lines at 20.5px (last glyph
  bottom ≈wy3+141 < 150) with the shortened Tankrabatt text.
- `Flow.box()` itself measures exactly; prefer it where possible.
- `Page.para(x, y,...)` draws first line AT y and returns y + n×size×lh;
  last baseline = return − size×lh. Box-height formulas must account for
  this. Flow end reports include line height + gap after the last baseline,
  so a flow end a few px past a conservative bottom is benign if the last
  glyph bottom clears the next rule/footer (P1-fussball y=2298 vs bottom
  2290, last glyph bottom ≈2259, quiz hline at 2312; P1-quiz y=2552 vs
  bottom 2540, last glyph bottom ≈2516, footer line at 2580).
- Mixed Latin+CJK title widths are systematically underestimated by
  char-count heuristics — measure with `text_w` or shorten titles until the
  audit is silent; the audit's BOXTITLE class catches this reliably.

## 13. Honest shortfalls / remaining verification debt

- Pflege numbers (6 million in need of care, ~10 million relatives) carry
  explicit ARD-programme attribution at every presentation (fix1) — still
  not independently re-verified (§4).
- B2 level count is 14/150 (same light spot as W43) — not inflated.
- 2 photos, not 4 (W43 had 4); P2/P3/P5 use boxes/infographics instead of
  photos. SOP “must have real pictures” satisfied at issue level.
- P2/P3 feature columns leave the third feature column partly empty (white
  space, not a defect — the lower page is dense with boxes + exercises).
- Lone “。” orphans at the end of four gloss boxes (cosmetic only, same
  class as W43's accepted lone 。).
- No git push, no Discord post made by this build — delivery is the parent
  line's job; the edition dir is complete and lint-ready (ABSTRACT.txt
  present, web PDF 3.96 MB < 10 MB).

## 14. Fix round 1 (independent proof, 2026-10-26) — appended, §§9–11 above untouched

Independent proof (`hidden_files/w45/de-core-independent-proof.md`) found
8 problems; all 8 were fixed in `hidden_files/weekly-report-w45-de-build/`,
the issue was fully re-rendered, and the gates were re-run. Full record:
`hidden_files/w45/de-core-fix1.md` (per-problem fixes, geometry notes,
re-render + audit results).

1. P1 "Vier Nächte Europa" → "Vier Nächte Fußball" (headline + lead).
2. P1 "4 deutsche Teams in Europa" → 6 (Zahlen box + caption).
3. P1 gloss "der Anstoß" → "die Bundesliga" (genuinely occurs in P1).
4. "Hart aber fair" dated Oct 26, past tense, in P2 article, P6 lead,
   P6 Q89, P8 Q127.
5. Pflege numbers attributed everywhere (P2/P6 articles, P2 WUSSTEN box,
   P6 DIE ZAHLEN box, P8 keys Q90/Q92); chart untouched.
6. 8,50 € → rund 8,35 € everywhere (article, boxes, P7 phrase 3 + toolbox +
   A2 lesson, P2 exercise key, P8 MUSTER); MUSTER 83 → 84 words.
7. P7 readers' corner: on-page deferral line (German + Chinese) — no real
   letters/texts by press time, promise carries to VOL.3.
8. P3 Rückblick: result-free Klassiker sentence added ("Ebenfalls am
   31. Oktober spielte Bayern in Dortmund — der Klassiker."); this §4
   claim corrected accordingly. P7 VOL.3 teaser now names St. Martin
   (Nov 11) so P3's pointer lands.
- Geometry forced by the fixes: P2 col-3 compensation (Zapfsäule item
  tightened so box4 still ends 1550.66); P6 closing sentence trimmed so
  P6-main still ends 1054/1080; P7 readers-box formula +16 px correction
  after a first-render COVER flag (see fix log).
- Final gates: build zero FLOW OVERFLOW / HEAD TOO WIDE warnings; verify
  150 exercises, numbering continuous, all 8 phrases exactly 2×, forbidden
  terms absent; occlusion selftest passed, audit on final render **0
  flags**; print PDF 17,030,165 bytes, web PDF 3,994,642 bytes.
- NOT re-finalized: this round fixes the 8 known problems only. A fresh
  full independent proof round must still return zero problems before
  delivery/insert.
