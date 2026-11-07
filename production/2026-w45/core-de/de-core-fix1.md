# FIX ROUND 1 — Die Lucerna VOL.2 (W45 Deutsch core)

**Source:** independent proof `hidden_files/w45/de-core-independent-proof.md` (2026-10-26, 8 problems, verdict NOT FINALIZED).
**Fix agent:** 2026-10-26. Build code: `hidden_files/weekly-report-w45-de-build/` (`content12/34/56/7/8.py`, run via `run.py` in one process).
**Scope kept:** only the 8 fixes (+ the P7 VOL.3-teaser St. Martin pointer alignment) and the geometry compensation each fix forced. No new articles, no new facts, no lead/image/credit/ABSTRACT changes. Kickoff times untouched (proofreader-confirmed). No git push, no Discord post, no messages sent.
**Status after this round:** all 8 fixed and re-rendered; **NOT self-certified as finalized** — a fresh full independent proof round is still required (parent's next step).

## Fix 1 — P1 "Vier Nächte Europa" → "Vier Nächte Fußball"
- Headline: "Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag".
- Lead sentence: "Vier Nächte Fußball, dann ein ganzes Wochenende Liga."
- Verified: "Vier Nächte Europa" now 0× issue-wide (SVG grep). P4 ("Vier Nächte Fußball hintereinander…") and P7 phrase 1 unchanged and now consistent with P1.

## Fix 2 — P1 "4 deutsche Teams in Europa" → 6
- Zahlen box: "6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）".
- Photo caption: "In dieser Woche spielen sechs deutsche Teams in Europa — …".
- Team lists untouched (Bayern, Stuttgart, Dortmund, Leipzig + Hoffenheim, Leverkusen). "vier deutsche Teams" now 0× issue-wide.

## Fix 3 — P1 gloss "der Anstoß" replaced
- Gloss now ends "… · empfangen 主场迎战 · die Bundesliga 德甲。" — "die Bundesliga" genuinely occurs in the P1 article (multiple times).
- "Anstoß" now 0× on P1 and issue-wide. All other pages' glosses were left alone (proofreader passed them).

## Fix 4 — "Hart aber fair" Pflege programme dated Oct 26 everywhere
- P2 article: "Am Montag, dem 26. Oktober, diskutierte die ARD-Sendung „Hart aber fair“ (21.00 Uhr): …" (present → past, dated).
- P6 lead: "Am Montag, dem 26. Oktober, um 21.00 Uhr diskutierte die ARD-Sendung „Hart aber fair“: …".
- P6 Q89: "Was diskutierte „Hart aber fair“ in der Sendung am 26. Oktober?" (key B unchanged; note now "10 月 26 日节目讨论居家护理").
- P8 Q127: "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober…" (key B unchanged; note likewise updated).
- Verified: no undated present-tense programme sentence remains in SVG text ("Montagabend diskutiert" 0×).
- Intentionally unchanged: P6 grammar drill Q93 "Die Frage ___ (werden) am Montag diskutiert." — a generic passive drill that never names the programme; the proofreader did not flag it.

## Fix 5 — Pflege numbers attributed at every bare presentation
- P2 article: "Nach Angaben der ARD-Sendung „Hart aber fair“ (26. Oktober) brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. … von rund zehn Millionen Angehörigen."
- P2 WUSSTEN box, item 3: "Mehr als sechs Millionen Menschen in Deutschland brauchen Pflege (ARD „Hart aber fair“, 26. Oktober)."
- P6 article: "Nach Angaben der Sendung brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. …" — "der Sendung" here refers to the ARD-Sendung „Hart aber fair“ named and dated (26. Oktober) in the immediately preceding sentence; full programme name + date is therefore present in the same paragraph.
- P6 DIE ZAHLEN box: "Menschen in Deutschland brauchen Pflege (ARD „Hart aber fair“, 26. Okt.)." and "Angehörige pflegen zu Hause (rund; ARD „Hart aber fair“, 26. Okt.)."
- P8 keys: Q90 note "据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理"; Q92 note "据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属".
- NOT changed: P6 practice chart (correctly labeled ÜBUNGSDATEN with "keine echte Umfrage" disclaimer) and the KIT's honest note that the numbers are still not independently re-verified — attribution is now explicit everywhere, the verification limitation remains recorded in KIT §4/§13.
- Geometry compensation (P2 col 3): the attributed WUSSTEN item grew 2→3 lines (+30.53 px), which would have pushed the ZEW box past the RECHNEN rule (box4 ended 1550.66 vs rule at 1554). Offset by tightening the AN DER ZAPFSÄULE item 2 from "16,7 Cent pro Liter — so viel weniger an der Zapfsäule (mit Mehrwertsteuer)." to "16,7 Cent pro Liter an der Zapfsäule (mit Mehrwertsteuer)." (3→2 lines, same facts). Result: P2 col3 box4 ends exactly 1550.66 again, unchanged.

## Fix 6 — 8,50 € → rund 8,35 € everywhere (50 × 16,7 ct = 8,35 €)
Changed in every occurrence, not just the four spots named in the proof:
- P2 article ("spart rund 8,35 Euro."), P2 AN DER ZAPFSÄULE box ("Rund 8,35 Euro — …"), P2 RECHNEN box ("= rund 8,35 € gespart"), P2 exercise A Q12 (key "8,35", note "50 升省约 8.35 欧元" — the key follows the article, otherwise it would have gone wrong).
- P7 A2 lesson paragraph ("rund 8,35 Euro für 50 Liter"), P7 toolbox ("rund 8,35 Euro = 大约省 8.35 欧元"), P7 phrase 3 ("Wer 50 Liter tankt, spart rund 8,35 Euro." / "加 50 升油，大约省 8.35 欧元。") — changed together with the P2 article sentence so the verbatim pair still matches exactly (verify.py verbatim check: phrase 3 exactly 2×).
- P8 MUSTER: "Ich tanke 50 Liter und spare rund 8,35 Euro." (added "rund" as instructed).
- Consequence handled: MUSTER word count rises 83 → **84** (recounted by split); the MUSTER title now reads "（84 Wörter）" and KIT §2/§5 references updated accordingly. Still inside the 80–100 requirement.
- Left alone (correct): 50 × 14,04 ct = 7,02 € and 14,04 × 1,19 ≈ 16,7 ct/L.
- Verified: "8,50" and "8.50" now 0× issue-wide (SVG grep).

## Fix 7 — P7 readers'-corner deferral disclosed ON THE PAGE
Printed in the LESERBRIEFE box (existing "Ein Beispiel der Redaktion!" label kept):
- German deferral line: "Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3."
- Chinese note merged into the box's Chinese line: "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"
- This discloses both halves of the deferred W43 promise (real reader letters AND best VOL.1 P8 texts) and carries the promise to VOL.3. KIT §6 updated with the printed wording.
- Geometry note (real defect caught and fixed during this round): the first fix1 render put the Chinese deferral on its own paragraph and the occlusion audit flagged it COVER (61% of ink covered by the NOCH EIN WORT box below — the readers-box height formula undercounts one line height per paragraph transition). Fixed by (a) merging the Chinese deferral into the existing Chinese line (removing one paragraph transition), (b) shortening the German deferral to 2 lines, and (c) adding a +16 px correction constant to the readers-box height formula (commented in content7.py). Final: P7 rail ends 1479.0, 29 px clear of the phrases rule at 1508; audit re-run 0 flags.

## Fix 8 — W43 promise gap: Klassiker mentioned (result-free) + KIT §4 corrected
- P3 Rückblick now reads: "… Reformationstag in neun Bundesländern. Ebenfalls am 31. Oktober spielte Bayern in Dortmund — der Klassiker. Einen Tag später, am Sonntag, dem 1. November, war Allerheiligen: …"
- Fixture only: NO result, NO score, NO winner (none verified in the report). "Klassiker" now 1× issue-wide (P3 only).
- P3-dependent items checked: no P3 exercise asks about the Klassiker; P3 A4 ("Am 31. Oktober war nur Halloween, kein Feiertag. Falsch") is unaffected (Reformationstag remains a Feiertag in nine states); P8 contains no Klassiker item. No key changed.
- KIT §4 false claim corrected: it no longer claims a pre-existing mention; it now records that the mention was added in this fix round with the exact printed wording. KIT §2 P3 description updated likewise.
- Pointer alignment (proofreader observation): P7 VOL.3 teaser now reads "… dazu St. Martin am 11. November, die Europapokal-Rückspiele und Ihre Briefe: …" so P3's "Mehr dazu in der nächsten Ausgabe" (St. Martin lanterns) points at a teaser that actually names St. Martin (Nov 11 only, no invented detail). Teaser still wraps to 2 lines inside its 130 px dark box.

## Re-render + gates (final render, after the P7 readers-box correction)
- Build: `tools/venv/bin/python run.py` — zero FLOW OVERFLOW / HEAD TOO WIDE warnings. Flow ends: P1-headline 1555/1828, P2-feature 1442/1540, P2 col3 box4 1550.66 (rule 1554), P3-main 1553/1560, P6-main 1054/1080 (unchanged — the P6 para-1 growth was offset by trimming the closing sentence to "Zwei Debatten, ein Muster: Beide kosten Geld und betreffen fast jeden Haushalt."), P6 col3 1264.95 (chart rule 1408), P7 col3 1479.0 (phrases rule 1508), P8-battery 1500/1505, P8-keys 2326/2560.
- Verify (`hidden_files/w45/de-core/verify.py`, phrase-3 expectation updated 8,50 → 8,35 in the tool itself): TOTAL 150; by page 10/18/18/18/18/18/12/38; numbering continuous 1–150; SVGs byte-identical after verify re-run; all 8 P7 phrases exactly 2× (verbatim OK); forbidden terms ("桥接", "Le Lucerna", "The Lucerna") absent; P1 top band no overlap; P6 chart bars clear of labels.
- Render: all 8 cards (PNG @1950), print PDF `Die-Lucerna-VOL2.pdf` 17,030,165 bytes / 8 pages, web PDF `Die-Lucerna-VOL2-web.pdf` 3,994,642 bytes / 8 pages (< 10 MB insert limit).
- Occlusion: `tools/occlusion_audit.py --selftest` passed (all 6 planted classes fired, clean controls silent); audit on the final edition dir: **0 flags** (first fix1 render had 1 COVER flag on P7, fixed as described above; the final audit is the 0-flag run).
- Own re-read: every changed page (P1, P2, P3, P6, P7, P8) read in full from rendered SVG text and visually from the 1950 px cards (P1, P2, P3, P6, P7, P8 viewed); changed answers re-checked (P2 Q12 = 8,35; P6 Q89/Q90/Q92; P8 Q127 = B; MUSTER 84 words).
- Untouched as instructed: lead (except fix 1's Europa→Fußball), images, credits, ABSTRACT.txt, kickoff times, P6 practice chart, P6 grammar drill Q93, all other pages' glosses.

## Files
- Fix log (this file): `hidden_files/w45/de-core-fix1.md`
- Build logs: `hidden_files/w45/de-core/build-log-fix1.txt` (first fix1 build), `build-log-fix1-final.txt` (final build), `verify-fix1.txt`, `render-fix1.txt`, `occlusion-fix1.txt` (final 0-flag audit; the intermediate 1-flag run is superseded by it and described above).
- Edition dir (re-rendered in place): `files/weekly-report-w45-de-core/` (8 SVGs, 8 cards, web + print PDFs, WEEKLY-KIT.md with §14 appended and §§2/4/5/6/13 corrected).
