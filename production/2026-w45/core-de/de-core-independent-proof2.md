# INDEPENDENT PROOFREAD — Die Lucerna VOL.2 (W45 Deutsch core) — ROUND 2

**Edition:** `files/weekly-report-w45-de-core/` (8 SVGs, 8 cards, web + print PDFs, WEEKLY-KIT.md, ABSTRACT.txt)
**Proofreader:** independent (not the builder, not the fix agent). Round-1 proof, fix log 1, SOP, KIT, trend-batch-A DE section and w43-promises DE section were read but NOT trusted; every check below was re-done from the rendered pages.
**Date of proof:** 2026-10-26
**SOP basis:** `files/weekly-report-SOP.md` §§1–8 + occlusion appendix.

## VERDICT: ZERO PROBLEMS — PROOF-FINALIZED

This round finds **zero problems**. All 8 round-1 fixes verify on the rendered pages (evidence per fix below). Per SOP §8.4 this core is finalized on the proof gate.

**Pre-insert open item (NOT a proof-round problem, but insert-blocking — read this):** ABSTRACT.txt is still entirely in German. The W45 ledger's standing correction (parent, 2026-10-26) rules that a non-Chinese target's core edition is its zh-cn edition, so its abstract must be in Simplified Chinese before any repo insert — "fold into each core's next fix round, or run a standalone abstract correction if a core otherwise finalizes first." This core otherwise finalizes here, so the parent line must run that standalone abstract rewrite (German → Simplified Chinese, same topics/keywords) **before** `insert.py`. Do not insert with the German abstract. The abstract's content is otherwise fine (single line, no ASCII double quotes, real topics, "Deutsch lernen mit Fußball", A2–B2, 150 Übungen).

Per-area verdicts:

- **Text (German + explanation layer):** CLEAN — all 8 pages read end to end from rendered SVG text; spelling, umlauts, agreement, conjugation, case, punctuation clean; no repeated words, no truncated sentences; every glossed word genuinely occurs in its page's text.
- **Numbers:** CLEAN — numbering 1–150 continuous, all 150 keys present and re-checked (changed keys re-derived, see below); chart 68+20+12=100; ZEW 34,7−6,6=28,1 and −47,1+11,2=−35,9; tank chain 50×14,04=7,02 €, 14,04×1,19≈16,7 ct/L, 50×16,7 ct=8,35 €; MUSTER recounted at **84 words**, matching the printed "(84 Wörter)" label and inside 80–100.
- **Facts:** CLEAN — all 8 round-1 fact fixes verify; kickoff times unchanged from the round-1 CONFIRMED set (not re-litigated, no new error found); no foreign-affairs items; no Nov 9 anniversary framing; no implied federal election; programme dated and past-tense everywhere; Pflege numbers explicitly attributed at every presentation (judgment below).
- **Layout (visual pass, all 8 cards):** CLEAN — no overflow, overlap, covered text, or footer intrusion; P7 reflow verified visually; both PD photos carry correct DVIDS credits and generic captions.
- **Geometry (own audit run):** CLEAN — `tools/occlusion_audit.py --selftest` passed (all 6 planted classes fired, clean controls silent); audit on the edition dir returned **0 flags**; no flags to adjudicate.

---

## ALL 8 ROUND-1 FIXES VERIFY

### Fix (a) — "Vier Nächte Fußball" — VERIFIED
- P1 headline reads "Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag"; P1 lead sentence reads "Vier Nächte Fußball, dann ein ganzes Wochenende Liga."
- Fixed-string grep: "Vier Nächte Europa" **0× issue-wide**. P4 ("Vier Nächte Fußball hintereinander…") and P7 phrase 1 now consistent with P1.

### Fix (b) — "sechs deutsche Teams" — VERIFIED
- P1 Zahlen box: "6 — deutsche Teams spielen in Europa （6 支德国球队出战欧战）"; P1 photo caption: "In dieser Woche spielen sechs deutsche Teams in Europa — und am Wochenende der 9. Spieltag der Bundesliga."
- "vier deutsche Teams" 0× issue-wide. The six named teams (Bayern, Stuttgart, Dortmund, Leipzig + Hoffenheim, Leverkusen) are all in the edition's own fixture coverage.

### Fix (c) — P1 gloss "die Bundesliga", "Anstoß" gone — VERIFIED
- P1 gloss now ends "… · empfangen 主场迎战 · die Bundesliga 德甲。" "die Bundesliga" genuinely occurs in the P1 article (multiple times, incl. "der 9. Spieltag der Bundesliga").
- "Anstoß" **0× issue-wide** (fixed-string grep over all 8 SVGs).

### Fix (d) — "Hart aber fair" dated Oct 26, past tense everywhere — VERIFIED
- P2 article: "Am Montag, dem 26. Oktober, diskutierte die ARD-Sendung „Hart aber fair“ (21.00 Uhr): …"; P6 lead: "Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: …"; P6 Q89: "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober?"; P8 Q127: "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober…".
- "Montagabend diskutiert" 0×; no undated present-tense programme sentence remains anywhere. P6 Q93 generic passive drill ("Die Frage ___ (werden) am Montag diskutiert.") names no programme and was correctly left alone.

### Fix (e) — Pflege numbers attributed at EVERY bare presentation — VERIFIED, and judged sufficient
Presentations checked one by one:
- P2 article: "Nach Angaben der ARD-Sendung „Hart aber fair“ (26. Oktober) brauchen in Deutschland mehr als sechs Millionen Menschen Pflege." — the "rund zehn Millionen Angehörigen" figure follows in the same paragraph under that attribution.
- P2 WUSSTEN box item 3: "… brauchen Pflege (ARD „Hart aber fair“, 26. Oktober)."
- P6 article: "Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege." — "der Sendung" refers to the ARD-Sendung „Hart aber fair“ named and dated (26. Oktober) in the immediately preceding sentence of the same paragraph; the "rund zehn Millionen Angehörigen" figure follows in the next sentence under the same attribution.
- P6 DIE ZAHLEN box: both rows carry "(ARD „Hart aber fair“, 26. Okt.)".
- P8 keys Q90/Q92: both notes carry "据 ARD《Hart aber fair》10 月 26 日节目…".
- P6 practice chart untouched and correctly labeled ÜBUNGSDATEN with an explicit "keine echte Umfrage" disclaimer.
- **Judgment (as instructed, on the printed attribution, not the fix log's honesty note):** the printed attribution meets SOP fact-sourcing for these claims. SOP §2 requires facts to have a verifiable source; the numbers are no longer asserted as bare facts anywhere — every presentation names the specific, dated, checkable broadcast they come from (ARD "Hart aber fair", 26. Oktober, a real programme whose topic line is independently on record). That is exactly the fix round 1 prescribed ("explicit attribution at every bare presentation"). The residual limitation — the two numbers themselves are not independently re-verified — remains honestly recorded in KIT §4/§13 and is NOT hidden from the reader, because the page itself says "according to the programme". A reader is not misled about the numbers' status. Not a problem.

### Fix (f) — "rund 8,35 €" everywhere, verbatim pair intact — VERIFIED
- "rund 8,35 Euro/€" confirmed at: P2 article, P2 AN DER ZAPFSÄULE box, P2 RECHNEN box ("= rund 8,35 € gespart"), P2 key Q12 ("8,35"), P7 A2 lesson ("rund 8,35 Euro für 50 Liter"), P7 toolbox ("rund 8,35 Euro = 大约省 8.35 欧元"), P7 phrase 3, P8 MUSTER ("spare rund 8,35 Euro." — "rund" present, as instructed).
- Fixed-string grep: "8,50" **0×**, "8.50" **0×** issue-wide. (An earlier unescaped-regex count of "8.50" was a regex artifact matching time strings such as 18.30; literal fixed-string checks are 0.)
- P7 phrase 3 "Wer 50 Liter tankt, spart rund 8,35 Euro." occurs **exactly 2×** whitespace-normalized (P2 article + P7), so the verbatim pair still matches. All 8 P7 golden sentences verified at exactly 2× each (article + P7).

### Fix (g) — P7 readers'-corner on-page deferral, both languages — VERIFIED
- P7 LESERBRIEFE box prints, in German: "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3." and in Chinese (merged into the existing Chinese line): "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。" (line-wrapped in the SVG, hence a naive single-line grep misses it; extracted text confirms both halves.)
- Both halves of the deferred W43 promise are disclosed (real reader letters AND best VOL.1 P8 texts); the promise carries to VOL.3. The "Ein Beispiel der Redaktion!" label is unchanged and unambiguous, the example is signed "— die Redaktion", and no fabricated reader, letter, or quote appears anywhere. Readers'-corner honesty: PASS.

### Fix (h) — P3 Rückblick Klassiker, result-free; KIT corrected — VERIFIED
- P3 Rückblick now reads: "Ebenfalls am 31. Oktober spielte Bayern in Dortmund — der Klassiker." "Klassiker" occurs **exactly 1× issue-wide** (P3 only). No score, no winner, no result attached anywhere; no P3 exercise and no P8 item references the Klassiker.
- KIT §4 no longer claims a pre-existing mention: it now records the correction ("the original KIT claim … was FALSE … Fix1 added one result-free sentence") with the exact printed wording, and KIT §2's P3 description matches. KIT §6 deferral wording matches the printed P7 box; KIT MUSTER count updated to 84.

---

## P7 REFLOW (fix-7 geometry) — VERIFIED VISUALLY
- P7 card viewed at full size: the readers' box is fully legible with clear space below it; the NOCH EIN WORT box below is uncovered; the SÄTZE DER WOCHE rule, FEHLERKLINIK, VOL.3 teaser box and footer are all intact with no intrusion.
- The P7 VOL.3 teaser names "St. Martin am 11. November", so P3's "Mehr dazu in der nächsten Ausgabe" (St. Martin lanterns) lands on a teaser that actually names St. Martin.
- Fix log's geometry (P7 rail ends 1479 vs phrases rule 1508) is consistent with the clean visual and the 0-flag audit; the +16 px readers-box correction did its job — no reflow defect remains.

## FRESH FULL-ROUND CHECKS (beyond the 8 fixes)

- **All pages read end to end** from extracted SVG text (P1 169, P2 189, P3 195, P4 188, P5 187, P6 209, P7 181, P8 293 text lines) plus all 8 cards viewed. No German spelling/umlaut/agreement/conjugation/case/punctuation error, no repeated word, no truncated sentence found.
- **Dates/weekdays re-checked with `date -d` (Europe/Berlin):** Nov 2 Mon, Nov 3 Tue, Nov 4 Wed, Nov 5 Thu, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Nov 9 Mon, Nov 11 Wed, Nov 15 Sun, Oct 26 Mon, Oct 31 Sat, Nov 1 Sun, Sep 25 Fri, Oct 1 Thu — every printed weekday/date combination matches. No public holiday falls inside Nov 2–8 in Germany.
- **Kickoff times:** unchanged from the round-1 CONFIRMED set; spot-checked against the P4 fixture table (all 9 Bundesliga rows + the flagged 2. Bundesliga Hertha row) — no new error found, not re-litigated.
- **Numbering/keys:** all 150 key numbers present in the P8 answers block (no missing numbers); changed keys re-derived correct (Q12 = 8,35; Q89 = B; Q90 = A; Q92 = B; Q127 = B); matching-letter maps on P2 (25–28: b/d/a/c), P4 (52–55: a/b/c/d), P8 (141–144: b/d/a/c) re-checked against printed options; round-1 suspects Q129 = A and Q149 = A still correct against their passages.
- **Explanation-layer anchoring:** P1 gloss words all occur in P1 (Englische Woche, Spieltag, empfangen as "empfängt", Bundesliga); P2–P6 gloss boxes re-checked and pass (inflected forms accepted, same standard as round 1); P7 toolbox phrases all occur in the issue's own articles.
- **Trend-pool + W43-promise compliance:** lead follows trend-batch-A DE recommendation (football week + everyday-economy second thread: Tankrabatt, ZEW, Stromsteuer, Pflege — all domestic-policy/economy, allowed). Foreign-affairs scan of all 8 SVGs: no Ukraine/Krieg/Wahl/election items; no Nov 9 anniversary framing (Nov 9 appears only as the P1 mini-feature's school-restart Monday); no implied federal election. W43 DE promises: Oct 31 triple event (Halloween + Reformationstag + Klassiker) and Nov 1 Allerheiligen all covered as labeled Rückblick; BW/Bavaria Ferienwechsel treatment internally consistent across P1/P3/P5 (BW back Nov 2, Bavaria still on holiday — the KIT's Le Boat-based correction of the promises register, already accepted in round 1); real-letters promise deferred with on-page disclosure (fix g).
- **Masthead/furniture/banned terms:** "Die Lucerna" masthead and "Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY" + "第 N 版 / 共 8 版" footer on all 8 pages; "桥接" 0×, "Le Lucerna" 0×, "The Lucerna" 0×.
- **Images/credits:** P1 photo (Armed Forces Soccer Championship, Destin 2010) credited "Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain"; P4 header-duel photo credited "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain". Both captions generic; neither claims the photos show Bundesliga/European matches. Issue-level real-pictures rule satisfied by P1+P4.
- **Files:** web PDF `Die-Lucerna-VOL2-web.pdf` 3,994,642 bytes / 8 pages (< 10 MB insert limit); print PDF 17,030,165 bytes / 8 pages.
- **KIT accuracy:** §§2/4/5/6/13/14 checked against the printed pages — all corrected claims match what is printed (Klassiker correction, MUSTER 84, deferral wording, St. Martin teaser, Pflege attribution note).

## OBSERVATIONS (not problems)

1. **B2 share light (14/150, same as W43)** — noted, not a problem; no mislabeled levels found.
2. **Lone "。" orphans** at the ends of the P2/P3/P4/P6 gloss boxes — cosmetic only, same W43-accepted class, not listed as problems.
3. **P5 preterite "war" for Nov 2** ("Am Montag, dem 2. November, war es … wieder so weit") — acceptable magazine narration in a Nov 2-dated issue, as in round 1.
4. **VOL.3 must actually deliver** what VOL.2 now promises on-page: real reader letters/texts, St. Martin (Nov 11) coverage, Volkstrauertag + NFL Munich (Nov 15). The P3 pointer and P7 teaser both point at VOL.3; a VOL.3 miss would break them.
5. **ABSTRACT rewrite (see verdict box)** is the only outstanding pre-insert item; it is owned by the parent line's ledger standing correction, not by this proof round.

## METHOD

1. Read SOP §§1–8 + occlusion appendix; round-1 proof; fix log 1; KIT; trend-batch-A DE section; w43-promises DE section; W45 ledger standing correction.
2. Extracted all visible text from the 8 SVGs and read every page end to end; viewed all 8 rendered 1950px cards.
3. Re-checked every date/weekday with `date -d` (Europe/Berlin); re-derived numbering, all 150 key numbers, chart sums, ZEW arithmetic, tank chain, MUSTER word count (84).
4. Verified each of the 8 round-1 fixes on the rendered pages with fixed-string greps + visual confirmation; re-derived all changed keys; verified all 8 P7 phrases at exactly 2× whitespace-normalized.
5. Ran `tools/occlusion_audit.py --selftest` (passed) and the audit on the edition dir (0 flags); adjudicated visually — no flags to adjudicate.
6. No edition or build files were edited. No git push, no Discord post, no messages sent.
