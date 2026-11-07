# INDEPENDENT PROOFREAD — ROUND 2 — De Lucerna VOL.2, Nederlands core, W45 (2–8 Nov 2026)

- Proofreader: independent (not the builder, not the fix agent). Fresh full round, not a
  spot-check. Round 1 report (`nl-core-independent-proof.md`, 3 problems) and fix log 1
  (`nl-core-fix1.md`) were read but NOT trusted; every check below was re-run or re-read
  from the re-rendered edition itself (8 SVGs under `files/weekly-report-w45-nl-core/svg/`,
  8 PNG cards under `cards/`, both PDFs, `WEEKLY-KIT.md`, `ABSTRACT.txt`).
- Method: full text extracted independently from all 8 SVGs and read end to end; all 8 PNG
  cards viewed as images; all dates re-checked with `date -d` (Europe/Amsterdam);
  exercise numbering, all P8 keys against questions/articles/chart, chart sums, model-essay
  word count re-derived; all 8 golden sentences checked verbatim (line-joined) against this
  issue's own articles; gloss anchoring, trend-pool (batch B, NL section) and W43-promise
  compliance re-checked; `tools/occlusion_audit.py --selftest` first, then on the edition
  dir; P7 reflow geometry measured from the SVG coordinates, not only from the PNG.
- Builder/fix-agent files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: ZERO PROBLEMS — FINALIZES THIS CORE (per SOP §8.4)

Per-area verdicts:

- **Text (spelling/grammar/agreement/punctuation): ZERO PROBLEMS.** All 8 pages read end
  to end; no spelling, agreement, or truncation errors found; no repeated words.
- **Numbers: ZERO PROBLEMS.** Numbering continuous 1–150 (P1 1–10, P2 11–28, P3 29–46,
  P4 47–64, P5 65–82, P6 83–100, P7 101–112, P8 113–150); `p8.py extract` on the final P8
  SVG: noted set = 150 of 150; all 150 keys re-derived against questions/articles/chart;
  chart sums 45+25+20+10 = 100, 45+25 = 70; durations Klimaatweek 7 days, Museumnacht
  19:00→02:00 = 7 hours, PAN 1–8 Nov = 8 days, Crossing Border 3–8 Nov = 6 days,
  Snuffelmarkt half of 250 = 125; matchday 12 = 9 matches (Fri 1 + Sat 3 + Sun 5);
  standings "24 ronden te gaan" after 10 of 34 rounds correct; model essay (P8 ex. 150)
  independently counted = 87 words (requirement 80–100).
- **Facts: ZERO PROBLEMS.** All dates/weekdays re-checked with `date -d`
  (Europe/Amsterdam): 2 Nov Monday, 3 Nov Tuesday, 6 Nov Friday, 7 Nov Saturday,
  8 Nov Sunday, 1 Nov Sunday, 25 Oct Sunday, 21 Oct Wednesday, 22 Oct Thursday,
  11 Nov Wednesday, 15 Nov Sunday — every printed weekday matches. European results,
  matchday-10 results, standings, Museumnacht, PAN, Snuffelmarkt, Robinson/ADE/DDW
  closings all internally consistent with the paper's own programme boxes and articles.
- **Layout: ZERO PROBLEMS.** All 8 rendered pages viewed: no overflow, overlap, footer
  intrusion, or edge breach; P7 reflow clean (see below); images match captions
  (P1 autumn forest, P2 Kinderdijk windmills, P3 Amsterdam canal boat, P4 1912
  Netherlands team); credits present on every photo (Vovogov90 CC0; Nationaal Archief
  CC0; W. Punt / Anefo, Nationaal Archief CC0; Spaarnestad Photo, public domain);
  masthead "De Lucerna"; 8 pages, all SVGs 1950×2700; pairing footer
  ("荷兰语周报 VOL.2") and "第 N 版 / 共 8 版" page lines on all pages; PDFs 8 pages
  each (web PDF 3,487,176 bytes, under the 10 MB limit).
- **Geometry: ZERO PROBLEMS.** My own run — `occlusion_audit.py --selftest` OK (all 6
  planted classes fired, clean controls silent); full audit on the edition dir: **0 flags**.
  No flag required adjudication because there were none; the P7 reflow was additionally
  measured by hand (see Fix 2 verification).

## Round-1 fix verification — ALL 3 FIXES VERIFY

### Fix (a) — P4 European-week tally: VERIFIED at all 3 spots, old wordings gone

- P4 headline (rendered P4 PNG + SVG text): «Europa: drie keer feest, twee keer
  verlies».
- P4 article ¶1: «De Europese week is voorbij — en de balans is drie keer feest, twee
  keer verlies. … NEC verloor: 2–4 bij Dinamo Zagreb.» — "Alleen" is gone, and
  Feyenoord's loss is stated in the next paragraph (Real Betis 1–0, Isco 59e minuut),
  so the tally now matches the paper's own results list: wins Ajax 2–0 Atalanta,
  Twente 4–1 Lincoln, AZ 4–0 Ararat; losses NEC 2–4 Dinamo, Feyenoord 0–1 Betis
  = 3 wins, 2 losses.
- P4 ex. 52 stem: «De ___ van de Europese week is: drie keer feest, twee keer verlies.»
- P8 key 52 unchanged and still matching: «52. balans — balans = 成绩单、总结».
- Old wordings absent from all 8 SVGs: «vier keer feest» 0 hits, «Alleen NEC» 0 hits.
- KIT §2 headline also reads the corrected tally.

### Fix (b) — P7 readers'-corner on-page disclosure: VERIFIED, Dutch AND Chinese, inside the box

- Disclosure is present INSIDE the P7 BRIEVEN VAN LEZERS box, in both languages:
  - Dutch: «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen —
    daarom dit voorbeeld; belofte naar VOL.3.»
  - Chinese: «截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。»
- It states exactly what round 1 required: no real letters / best P8 texts had arrived by
  press time, so the labeled example stands and the promise carries to VOL.3.
- Labeling still unambiguous: «— Li (voorbeeldbrief van de redactie)» plus
  «编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！»
- The VOL.3 preview box («Verder: jullie brieven en de beste teksten van pagina 8.»)
  now reads as the carried promise, consistent with the disclosure — no longer as if
  VOL.2 were on schedule.
- This also satisfies the W43-promises register's alternative branch for the overdue
  readers'-corner item ("print real letters, or honestly report that none arrived"):
  the page honestly reports that none arrived, for both letters and best P8 texts.

### Fix (c) — P8 key 99: VERIFIED exactly

- P8 ANTWOORDEN key 99 reads exactly: «99. Rood komt weinig voor. — weinig voor =
  很少出现» — no added words. Old form «Rood komt weinig voor in Nederland» 0 hits
  across all 8 SVGs. It matches both the exercise prompt (rood / komt / weinig / voor)
  and the P6 article sentence («Rood komt weinig voor.»).

## P7 reflow check — the disclosure-forced reflow is clean

Viewed the P7 PNG closely, line by line, and measured the SVG geometry:

- BRIEVEN VAN LEZERS box: rect y = 1328.5, height 568.5 → bottom edge 1897.
  Last line inside the box (Chinese invitation) baseline y = 1868.47 → 28.5 px margin
  inside the box. The +50 px correction reported by the fix agent is confirmed by
  measurement: no line sits at or below the box edge, and the 21 px overflow from the
  first re-render is gone.
- ZINNEN VAN DE WEEK section moved down as reported (rule at y = 1937, section title
  y = 1975 — 40 px clear of the letters box); all 8 golden-sentence rows and their
  Chinese translations inside their rows, no overlap.
- VOLGENDE WEEK preview box at y = 2439, footer at y = 2624 — both intact, no intrusion.
- PAS OP, HET WOORD, and all three level columns above the letters box are unchanged
  in position relative to each other and show no overlap.

## Other re-checks (fresh round)

- **Explanation-layer anchoring:** every glossed word verified present in the text it
  annotates (P1 Klimaatweek/boom/besparen/waarschuwing; P2 klimaat/wortelen/verwarming/
  lokaal; P3 museum/rondleiding/tijdslot/tweedehands/beurs; P4 balans/gelijkspelen/
  speelronde/topper/stand; P5 eiland/proef/stemmen/aflevering/voorbij; P6 meteoroloog/
  waarschuwingsmoeheid/vastzetten/advies/voorstander; P7 klimaatwoorden/scheidbare
  werkwoorden/mening geven). P8 answer notes match questions.
- **Golden sentences:** all 8 verified verbatim (line-joined) against this issue's own
  articles with correct page labels — P1 ×2, P2, P3, P4, P5, P6 ×2. No classic/foreign
  sentence smuggled in.
- **Trend-pool + W43 promises:** lead follows batch-B NL recommendation (Klimaatweek
  2–8 Nov as the exact-week peg, Museumnacht 7 Nov, matchday 12). W43 promises honored:
  Robinson premiere (Sun 1 Nov, 20:00, RTL 4, 19 candidates) covered as just-passed
  and ongoing ("De eerste aflevering is geweest — nu begint het echte spel"), with NO
  eliminations or outcomes invented; ADE (30 years, 3,000+ artists, 200+ locations) and
  DDW (~2,500 designers) closings dated Sun 25 Oct; European-week results reported.
  Sinterklaas appears only in the VOL.3 preview (Sun 15 Nov Amsterdam) and Sint-Maarten
  Wed 11 Nov — both correctly dated, both inside the VOL.3 week, not W45 leads.
- **Red lines:** no EU-budget/foreign-policy/Ukraine/Middle East/ICC items anywhere;
  no Belastingplan (0 hits); banned term «桥接» 0 hits across all 8 SVGs.
- **KNMI 2 Nov date:** NOT printed anywhere. The paper only says warnings are
  "tegenwoordig lokaal" (P1, P2, P6 "zijn veranderd: vroeger … nu zijn ze lokaal");
  no KNMI mention carries a 2 Nov switch date. (The 2 Nov dates printed elsewhere are
  Klimaatweek dates, not KNMI dates.)
- **Readers'-corner honesty:** no fabricated reader, letter, or quote anywhere. The only
  letter is the labeled editor's example (Li); the P2 EN JIJ box invitation ("de mooiste
  komen in VOL.3") is consistent with the P7 disclosure.
- **ABSTRACT.txt:** present and fact-consistent (Klimaatweek, Museumnacht, speelronde 12,
  A2–B2, 150 oefeningen). Untouched by the fixes, as reported.

## Checked, NOT problems (considered and accepted, same standard as round 1)

- P7 PAS OP item 4 ("Na «omdat» staat het werkwoord op plaats 2") — the Chinese note
  makes the intended rule unambiguous (main-clause verb second after the omdat-clause:
  "blijf ik thuis"). Accepted.
- P5 ex. 72 "De kandidaten stemmen wie naar huis moet" — "stemmen" + wie-clause (vote
  on who) is acceptable usage. Accepted.
- P8 ex. 131's answer follows the Daan text's own stated reason (Sunday Twente–Ajax).
  Accepted.
- Perfectum / gaan-future exercise blanks (e.g. P3 ex. 39–42, P5 ex. 76–79) place the
  verb-form blank in finite-verb position while the key gives the full verb cluster
  (e.g. "hebben gekocht", "gaat winnen"). This is the paper's standard workbook-blank
  convention — the blank stands for the verb form being tested, and the keys name the
  correct forms — not a spelling, fact, or key-mismatch error. It was also passed in
  round 1 and is unchanged by the fixes; it is not counted as a problem in this round.

## Problem list

None. Numbered problems: 0.

## Conclusion

This is a full fresh round finding **ZERO PROBLEMS**. All 3 round-1 fixes verify on the
rendered pages, and the text, numbers, facts, layout, and geometry areas are each
separately clean. Per SOP §8.4 this core is finalized by this round. This report does
not approve any other edition, and no fix by this proofreader was needed or made.
