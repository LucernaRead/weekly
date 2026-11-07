# INDEPENDENT PROOFREAD — Die Lucerna VOL.2 (W45 Deutsch core)

**Edition:** `files/weekly-report-w45-de-core/` (8 SVGs, 8 cards, web + print PDFs, WEEKLY-KIT.md, ABSTRACT.txt)
**Proofreader:** independent (not the builder). Builder's notes and occlusion runs were read but NOT trusted; every check below was re-done.
**Date of proof:** 2026-10-26
**SOP basis:** `files/weekly-report-SOP.md` §§1–8 + occlusion appendix.

## VERDICT: 8 PROBLEMS — NOT FINALIZED

This core is **not** cleared for delivery/insert until the 8 numbered problems are fixed, the issue is re-rendered, and a fresh full proofread round returns zero problems (SOP §8 rule 4). The problems are concentrated in P1 fact wording, P2/P6 sourcing, P7 readers'-corner honesty, and one arithmetic chain. Layout and geometry are clean.

Per-area verdicts:

- **Text (German + explanation layer):** PROBLEMS — P1 gloss word "der Anstoß" never appears in the P1 article (Problem 3); otherwise spelling, agreement, conjugation, case and punctuation read clean across all 8 pages.
- **Numbers:** PROBLEMS — 8,50 € chain mis-derives as 8,35 € (Problem 6); numbering 1–150 continuous and all 150 keys re-derived correct; MUSTER 83 words verified; chart 68+20+12=100 verified; ZEW arithmetic verified.
- **Facts:** PROBLEMS — "Vier Nächte Europa" (Problem 1), "4 deutsche Teams in Europa" (Problem 2), undated present-tense "Hart aber fair" Pflege programme (Problem 4), bare Pflege numbers (Problem 5), missing Klassiker (Problem 8). All printed kickoff times VERIFIED against external sources (see below) — the builder's CET conversion is correct and the old 14:30/15:30 variance is resolved.
- **Layout (visual pass, all 8 cards):** CLEAN — no overflow, overlap, footer intrusion, or image/caption mismatch. Both PD photos carry correct DVIDS credits; captions do not claim Bundesliga/European matches.
- **Geometry (own audit run):** CLEAN — `tools/occlusion_audit.py --selftest` passed (all 6 planted classes fired, clean controls silent); audit on the edition dir returned **0 flags**.

---

## NUMBERED PROBLEMS

### Problem 1 — P1: "Vier Nächte Europa" is factually wrong (headline + lead article)

- **Locations:** P1 headline "Englische Woche in Deutschland: Vier Nächte Europa, dann der 9. Spieltag"; P1 lead article sentence "Vier Nächte Europa, dann ein ganzes Wochenende Liga."
- **Evidence:** European nights in this issue week are exactly three: Tue Nov 3 (UCL), Wed Nov 4 (UCL), Thu Nov 5 (UEL). Friday Nov 6 is the Bundesliga opener (Hamburg–Gladbach), not a European night. The edition's own P4 article states the correct version: "Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga." — and P7 phrase 1 correctly uses "Fußball". So P1 contradicts P4/P7 within the same issue.
- **Fix:** Change "Europa" → "Fußball" in the P1 headline and lead sentence (P7 phrase 1 then still matches P4 verbatim; the P1 headline is not a golden sentence, so no phrase-count impact).

### Problem 2 — P1: "4 deutsche Teams in Europa" is wrong; the edition itself names six

- **Locations:** P1 "DIE WOCHE IN ZAHLEN" box: "4 — deutsche Teams spielen in Europa （4 支德国球队出战欧战）"; P1 photo caption: "In dieser Woche spielen vier deutsche Teams in Europa — und am Wochenende der 9. Spieltag der Bundesliga."
- **Evidence:** The edition names six German teams in Europe this week: Bayern, Stuttgart, Dortmund, Leipzig (UCL, Tue/Wed) + Hoffenheim, Leverkusen (UEL, Thu — P4: "Auch Bayer Leverkusen ist in Europa dabei: Die Werkself spielt um 21.00 Uhr gegen Marseille"). Externally confirmed: Leverkusen–Marseille is a UEL MD4 fixture on Thu Nov 5 (20:00 UTC = 21:00 CET). The "4" counts only the Champions League teams but is printed unqualified as "in Europa".
- **Fix:** Change to 6 / "sechs" in both the Zahlen box and the caption (and check the P1 Zahlen-box line count still fits after the one-character change).

### Problem 3 — P1 gloss: "der Anstoß" is glossed but never appears in the P1 core text

- **Location:** P1 gloss box: "讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · der Anstoß 开球。"
- **Evidence:** `grep -o "Anstoß" p1-front.svg` returns exactly one occurrence — the gloss itself. "die Englische Woche" (headline), "der Spieltag" (article), "empfangen" (as "empfängt") all genuinely occur in P1; "Anstoß" does not occur anywhere else on the page. SOP §8 requires every glossed word to actually appear in the text it annotates. All other pages' gloss boxes were checked and pass (P2: Tankrabatt/Zapfsäule/Energiesteuer/Mehrwertsteuer/Angehörige; P3: Ferienwechsel/Schülerin [as "Schülerinnen"]/Ausflug/Advent/Lesung; P4: Englische Woche/auswärts/empfangen/Favorit/eröffnen; P5: Pausenhof/Klassenarbeit/Referat/ausschlafen/Probe; P6: Angehörige/Pflegeversicherung/Pflegedienst/Stagnation/Aufschwung — all present, inflected forms accepted).
- **Fix:** Replace "der Anstoß" in the gloss with a word that actually appears on P1, or add "Anstoß" to the P1 article (e.g. in the Friday sentence). Do not just delete without checking the gloss-box line count.

### Problem 4 — P2/P6/P8: the "Hart aber fair" Pflege programme is presented as the issue week's Monday programme, but the Pflege episode was Oct 26

- **Locations:** P2 article: "Am Montagabend diskutiert die ARD-Sendung „Hart aber fair“ (21.00 Uhr): „Pflege zu Hause — Lässt die Politik Angehörige allein?“"; P6 lead: "Am Montagabend um 21.00 Uhr diskutiert die ARD-Sendung „Hart aber fair“: …"; P6 Q89 and P8 Q127 ("Was diskutiert „Hart aber fair“ am Montag?") inherit the same undated Monday.
- **Evidence:** Per the builder's own KIT §4 and the trend pool, the Pflege episode of "Hart aber fair" aired Mon Oct 26, 21:00 ("Pflege zu Hause — Lässt die Politik Angehörige allein?"). In an issue dated Mon Nov 2 – Sun Nov 8, undated present-tense "Am Montagabend diskutiert …" reads as the issue week's Monday (Nov 2) — a programme topic that was unknowable at build time (Oct 26) and is not verified for Nov 2. By contrast, P3 handles its just-passed items correctly by labeling them "Rückblick" with explicit dates.
- **Fix:** Date the programme explicitly ("Am Montag, dem 26. Oktober, diskutierte …") and/or reframe the P6 deep read as the continuing debate sparked by that programme. Adjust Q89/Q127 wording to match (e.g. "in der Sendung am 26. Oktober").

### Problem 5 — Pflege numbers are printed as bare facts; the only attribution is programme proximity, and the builder could not re-verify them

- **Locations:** P2 article ("In Deutschland brauchen mehr als sechs Millionen Menschen Pflege. Die meisten … von rund zehn Millionen Angehörigen."); P2 "WUSSTEN SIE DAS?" box (same six-million sentence, no attribution); P6 article (same sentences); P6 "DIE ZAHLEN" box ("6 Mio. … brauchen Pflege." / "10 Mio. Angehörige pflegen zu Hause (rund).", no attribution line); P8 Q90/Q92 keys repeat the numbers as facts.
- **Judgment (scrutiny item b):** This does NOT meet SOP fact-sourcing. SOP §2 requires facts to have a verifiable source. The numbers' only support is the Oct 26 ARD programme as reported second-hand in the trend pool, and the builder's fresh web search on 2026-10-26 could NOT independently re-verify them (KIT §4, "VERIFICATION DEBT"). P6's programme sentence happens to precede the numbers (contextual attribution) but contains no "laut/nach Angaben" wording; the P2/P6 boxes and P8 keys carry no attribution at all. A reader cannot check a TV utterance, and the KIT itself records the debt as unresolved.
- **Fix (softening, not necessarily removal):** Add explicit attribution at every bare presentation — e.g. "Nach Angaben der ARD-Sendung „Hart aber fair“ (26. Oktober) …" in the P2/P6 articles and a small attribution line in the DIE ZAHLEN box ("Quelle: ARD-Sendung …") — or drop the two numbers and keep only the attributed debate framing. Do not leave them as unattributed facts. (Note: the P6 practice chart is NOT part of this problem — it is correctly labeled ÜBUNGSDATEN with an explicit "keine echte Umfrage" disclaimer.)

### Problem 6 — The 8,50 € saving mis-derives from the edition's own numbers (should be 8,35 €)

- **Locations:** P2 article ("Wer 50 Liter tankt, spart rund 8,50 Euro."); P2 "AN DER ZAPFSÄULE" box ("Rund 8,50 Euro — so viel spart, wer 50 Liter tankt."); P2 "RECHNEN WIR MAL" box ("mit Mehrwertsteuer = rund 8,50 € gespart"); P7 phrase 3 ("Wer 50 Liter tankt, spart rund 8,50 Euro."); P7 toolbox ("rund 8,50 Euro = 大约省 8.50 欧元"); P8 MUSTER ("Ich tanke 50 Liter und spare 8,50 Euro." — here WITHOUT "rund").
- **Evidence:** The edition's own chain is 50 × 14,04 ct = 7,02 € (correct, printed) and 14,04 × 1,19 = 16,71 ≈ 16,7 ct/L at the pump (correct, printed as "rund 16,7 Cent"). But 50 × 16,7 ct = 8,35 €, not 8,50 €. The builder's KIT justification ("press-standard rounding, 50 × 17 ct") uses a different rounded input (17 ct) than the figure the edition itself prints (16,7 ct); "rund" does not bridge 8,35 → 8,50 inside a "RECHNEN WIR MAL" calculation box, and the MUSTER states 8,50 with no qualifier at all.
- **Fix:** Change to "rund 8,35 €" everywhere (article, both P2 boxes, P7 phrase 3 — the phrase must then still match the article verbatim, so change both together — toolbox, MUSTER), or print the 17-Cent press chain explicitly ("etwa 17 Cent pro Liter … rund 8,50 €") and remove the conflicting 16,7-Cent chain. The first option is cleaner.

### Problem 7 — P7 readers' corner: the example is labeled, but the deferral of the W43 real-letters promise is NOT disclosed on the page

- **Location:** P7 "LESERBRIEFE · 读者来信" box.
- **Evidence for what IS fine:** The example labeling itself is unambiguous: "Ein Beispiel der Redaktion!" + the example signed "— die Redaktion" + Chinese "编辑部示例，非真实来信。请寄来您的习作，优秀者刊登于 VOL.3。" No fabricated letter is passed off as real.
- **Evidence for the gap:** W43 P7 promised (per the W43-promises register) that VOL.2 would print real reader letters AND the best VOL.1 P8 texts (topic «Mein Sonntag, der 25. Oktober»). VOL.2 prints neither; the P7 box merely invites letters/texts for VOL.3 ("Die besten echten Briefe drucken wir in VOL.3.") without a single word disclosing that the VOL.2 promise is deferred. Under the same standard applied to the EN/ES cores, an invitation for VOL.3 without an on-page deferral disclosure is a problem — the KIT §6 disclosure does not count, because readers only see the page.
- **Fix:** Add one short on-page line in the LESERBRIEFE box (German + Chinese), e.g. that no real letters had arrived in time for VOL.2 so the real-letters feature moves to VOL.3. Keep the "Ein Beispiel der Redaktion!" label.

### Problem 8 — W43 promise gap: the Oct 31 "triple event" is missing its third leg (Klassiker), and the KIT falsely claims it is mentioned

- **Location:** P3 "Rückblick" paragraph (Oct 31 / Nov 1 coverage).
- **Evidence:** W43 P7 previewed for VOL.2: "Samstag, 31. Oktober: Halloween UND Reformationstag UND der Klassiker in Dortmund · Sonntag, 1. November: Allerheiligen …". The W45 P3 Rückblick covers Halloween + Reformationstag (Oct 31) and Allerheiligen (Nov 1) but never mentions the Klassiker: `grep "Klassiker"` over all 8 edition SVGs returns zero occurrences. Meanwhile KIT §4 claims "the W45 Rückblick does NOT invent a score; it mentions the fixture without a result" — that claim is false; there is no fixture mention at all. (Correctly, no score is invented anywhere — that part holds; the gap is the missing mention itself.)
- **Fix:** Add one result-free Klassiker sentence to the P3 Rückblick (e.g. that Bayern played in Dortmund on Oct 31, without a score, since the result was unknowable at build time), and correct KIT §4 to describe what is actually printed. If the parent line instead rules the Klassiker dropped deliberately, the KIT must record the drop and the reason — it cannot keep claiming a mention that does not exist.

---

## VERIFIED CLEAN (evidence, not builder trust)

### Kickoff times — ALL PRINTED TIMES CONFIRMED (scrutiny item a: RESOLVED)

The trend pool's 14:30 vs 15:30 variance is confirmed to be a UTC-vs-CET label difference, and the edition's CET table is correct in full:

- **Bundesliga MD9 (FIFPlay CET table, corroborated by bundesliga.com UTC listings +1h):** Fri Nov 6, 20:30 HSV–Gladbach (bundesliga.com: 2026-11-06T19:30:00Z); Sat Nov 7, 15:30 Dortmund–Elversberg, Paderborn–Frankfurt, Mainz–Bayern, Leipzig–Augsburg (14:30Z); Sat Nov 7, 18:30 Stuttgart–Bremen (17:30Z); Sun Nov 8, 15:30 Köln–Leverkusen (14:30Z), 17:30 Freiburg–Union (16:30Z), 19:30 Hoffenheim–Schalke (18:30Z). Every P4 fixture-table row, every P1/P4/P5 article time, every P4 section-D drill time, and every P8 time reference matches.
- **UCL MD4:** Tue Nov 3, 18:45 CET Galatasaray–Stuttgart (17:45 UK) and 21:00 CET Atlético–Bayern (20:00 UK); Wed Nov 4, 21:00 CET Dortmund–Betis and Leipzig–Man City (20:00 UK). Confirmed via NBC/Vavel UCL MD4 listings.
- **UEL MD4:** Thu Nov 5, 18:45 CET Crystal Palace–Hoffenheim — confirmed by the club itself (cpfc.co.uk: "Thursday, 5th November — 17:45 GMT — Selhurst Park"); 21:00 CET Leverkusen–Marseille (20:00Z). Confirmed.
- **2. Bundesliga MD11:** Sat Nov 7, 20:30 CET Hertha–Wolfsburg (bundesliga.com 2.BL page: 19:30Z; FBref: 20:30). Confirmed, and correctly flagged as 2. Bundesliga in the table note.
- **No invented results anywhere.** No score is printed for any W45 or Oct 31 match. P4 section D drills fixture times, not results, as designed.

### Dates and weekdays (all re-checked with `date -d`, Europe/Berlin)

Nov 2 Mon, Nov 3 Tue, Nov 4 Wed, Nov 5 Thu, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Nov 9 Mon, Nov 15 Sun, Oct 26 Mon, Oct 31 Sat, Nov 1 Sun, Sep 25 Fri, Oct 1 Thu — every printed weekday/date combination matches. No public holiday falls inside Nov 2–8 in Germany. Allerheiligen Nov 1 (Sun) correctly placed just before the issue week; Volkstrauertag Nov 15 (Sun) and NFL Munich Nov 15 correctly placed in the VOL.3 teaser; Oct 31/Nov 1 items appear only as labeled Rückblick reports, never as previews.

### Numbering, keys, counts

- Numbering 1–150 continuous, no gaps or duplicates (P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38).
- All 150 P8 keys re-derived against prompts, options, articles and charts — all correct, including the two builder-flagged suspects (129 = A "um halb acht" matches the Familie Berger passage; 149 = A "gehe", 1st person singular). Matching-letter maps verified on P2 (25–28: b/d/a/c), P4 (52–55: a/b/c/d), P8 (141–144: b/d/a/c).
- MUSTER model text recounted word by word: **83 words**, matching the printed "(83 Wörter)" label and inside the 80–100 requirement.
- Chart arithmetic: 68 + 20 = 88; 68 + 20 + 12 = 100. ZEW: 34,7 − 6,6 = 28,1; −47,1 + 11,2 = −35,9. Tankrabatt: 50 × 14,04 = 7,02 € exact (the 8,50 € step is Problem 6, not the 7,02 step).
- P7 golden sentences: all 8 verified programmatically at exactly 2 occurrences each in rendered SVG text (article + P7, whitespace-normalized), and each is a verbatim contiguous excerpt from this issue's own articles. P6 col-3 debate box correctly uses paraphrase, not the verbatim Wambach quote, so phrase 7 stays at 2×.

### Masthead, furniture, banned terms

- Masthead "Die Lucerna" confirmed against `tools/tables.json` (de: article "Die", masthead "Die Lucerna"). Every page footer carries "Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY" + "第 N 版 / 共 8 版".
- Banned term «桥接»: 0 occurrences in all 8 SVGs. "Le Lucerna"/"The Lucerna": 0 occurrences.
- ABSTRACT.txt: single line, no ASCII double quotes, names real topics (Champions League, Europa League, 9. Bundesliga-Spieltag, Tankrabatt, Ferienwechsel, Pflege-Debatte) + "Deutsch lernen mit Fußball" + "A2 bis B2" + "150 Übungen". Target-language abstract matches the established W45 core convention (EN/ES/IT/PT cores are likewise in their target languages).

### Trend-pool and red-line compliance

- Lead follows the pool recommendation (football week + everyday-economy second thread). Tankrabatt, ZEW, Stromsteuer, Pflege are all domestic-policy/economy items (allowed). No foreign-affairs items, no Nov 9 anniversary framing (Nov 9 appears only implicitly as "am Montag … die Ferien sind dann vorbei" — a school-holiday statement, no commemorative content), no implied German federal election.
- Reformationstag "in neun Bundesländern" verified by count (Brandenburg, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt, Thüringen + Bremen, Hamburg, Niedersachsen, Schleswig-Holstein = 9). Allerheiligen states list (BW, Bayern, NRW, Rheinland-Pfalz, Saarland) correct.
- BW/Bavaria Ferienwechsel treatment (BW back Nov 2, Bavaria still on holiday in week Nov 2–8, "als einziges Bundesland") is internally consistent across P1/P3/P5 and follows the KIT's cited Le Boat table; it corrects the W43-promises register's "BW in progress" line, which the KIT shows to be wrong for this week. (I could not independently re-fetch the Le Boat table — web search returned only content-farm pages — so this point rests on the KIT's cited source, recorded here as a verification limitation, not as a problem.)

### Layout (visual pass, all 8 rendered cards)

- No overflow, overlap, footer intrusion, or covered text observed on any page. The lone "。" orphans at the ends of the P2/P3/P4/P6 gloss boxes are cosmetic only (same W43-accepted class) and are NOT listed as problems.
- P1 photo (Armed Forces Soccer Championship, Destin 2010) credited "Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain"; P4 header-duel photo credited "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain". Both captions are generic and do NOT claim the photos show Bundesliga/European matches. Both images match the KIT's DVIDS public-domain sourcing.
- P2/P3/P5 carry boxes/infographics instead of photos; issue-level "must have real pictures" is satisfied by P1+P4.

---

## OBSERVATIONS (not problems)

1. **B2 share light (14/150, same as W43)** — noted, not a problem: counted independently (P6: 86, 88, 89, 90, 91, 93, 94, 96, 98, 99; P7: 109–112). No mislabeled levels found in the re-derivation; the B2 load genuinely sits on P6+P7. Do not inflate by re-labeling.
2. **P3 St. Martin pointer vs P7 teaser:** P3 says of the St. Martin lanterns "Mehr dazu in der nächsten Ausgabe", but the P7 VOL.3 teaser names only Volkstrauertag + NFL + Europapokal-Rückspiele + Briefe. The teaser need not be exhaustive, so this is not a defect in this issue — but VOL.3 must actually cover St. Martin (Nov 11 falls in W46) or the P3 pointer breaks. Flag to the VOL.3 builder.
3. **P5 preterite "war" for Nov 2** ("Am Montag, dem 2. November, war es … wieder so weit") in a Nov 2-dated issue reads as within-week retrospection; acceptable magazine narration, not flagged.
4. **KIT inaccuracy beyond Problem 8:** KIT §4's fixture discussion is otherwise accurate (CET conversion, FIFPlay corroboration, no invented results). Only the Klassiker-mention claim is false.

---

## METHOD

1. Read SOP §§1–8 + occlusion appendix; read builder KIT, builder proofread-notes, trend-batch-A DE section, W43-promises DE section, tables.json DE entry.
2. Extracted all visible text from the 8 SVGs (regex over `<text>` elements) and read every page end to end; viewed all 8 rendered 1950px cards.
3. Re-checked every date/weekday with `date -d` (Europe/Berlin); re-derived numbering, all 150 keys, chart sums, ZEW arithmetic, MUSTER word count (83).
4. Verified every printed kickoff time against external sources (bundesliga.com UTC listings, FIFPlay CET table, NBC/Vavel UCL listings, cpfc.co.uk official, sportscafe/sync2cal UEL listings, FBref) — see "Kickoff times" above.
5. Ran `tools/occlusion_audit.py --selftest` (passed) and the audit on the edition dir (0 flags); adjudicated visually — no flags to adjudicate.
6. No edition or build files were edited. No git push, no Discord post, no messages sent.
