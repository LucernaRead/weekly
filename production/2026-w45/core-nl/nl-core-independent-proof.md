# INDEPENDENT PROOFREAD — De Lucerna VOL.2, Nederlands core, W45 (2–8 Nov 2026)

- Proofreader: independent (not the builder). Builder's record (`hidden_files/w45/nl-core/build-log.txt`,
  `audit-output.txt`, `proofread-notes.txt`, edition `WEEKLY-KIT.md`) was read but NOT trusted;
  every check below was re-run or re-read from the rendered edition itself.
- Method: SOP §§1–8 + occlusion appendix read first; full text extracted independently from all 8 SVGs
  and read end to end; all 8 PNG cards viewed; all dates re-checked with `date -d` (Europe/Amsterdam);
  exercise numbering, all P8 keys, chart sums, model-essay word count, gloss anchoring, golden sentences,
  trend-pool compliance, and W43 promises re-verified; builder scrutiny items (a)–(d) independently
  checked, including fresh web searches; `tools/occlusion_audit.py --selftest` first, then on the edition dir.
- Builder files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: 3 PROBLEMS — NOT ZERO-PROBLEM, DO NOT FINALIZE YET

Per-area verdicts:

- Text (spelling/grammar/punctuation): otherwise clean; PROBLEM 3 is a key/question mismatch, not prose.
- Numbers: clean except PROBLEM 3 (key adds words outside the prompt); all other counts re-derived clean.
- Facts: HARD PROBLEM 1 (P4 tally contradicts the paper's own results). Scrutiny items (a) and (b)
  were INDEPENDENTLY CONFIRMED and are NOT problems (see "Checked, not problems").
- Readers'-corner honesty: labeling unambiguous, but PROBLEM 2 (W43 promise deferral undisclosed on the page).
- Layout: clean on all 8 rendered pages.
- Geometry: clean — 0 flags, selftest passed.

## Problem 1 (HARD — European-week tally contradicts the paper's own results)

- Locations (3 spots, one fix each):
  1. P4 headline: «Europa: vier keer feest, één keer verlies»
  2. P4 article, paragraph 1: «Alleen NEC verloor: 2–4 bij Dinamo Zagreb.»
  3. P4 exercise 52 (stem): «De ___ van de Europese week is goed: vier keer feest.»
- Evidence — the paper's own results list, same page (article + HET PROGRAMMA box):
  Ajax 2–0 Atalanta (win), Twente 4–1 Lincoln Red Imps (win), AZ 4–0 Ararat-Armenia (win),
  NEC 2–4 Dinamo Zagreb (loss), Real Betis 1–0 Feyenoord (loss, "door een doelpunt van Isco in de
  59e minuut", article paragraph 2).
  Count: 3 wins, 2 losses — NOT "vier keer feest, één keer verlies", and NOT "alleen NEC verloor"
  (Feyenoord also lost, in the very next paragraph of the same article).
- Required fix: headline → e.g. «Europa: drie keer feest, twee keer verlies»; article sentence →
  drop "Alleen" (e.g. «NEC verloor: 2–4 bij Dinamo Zagreb.» with Feyenoord's loss acknowledged in
  the tally); ex. 52 stem → "drie keer feest". P8 key 52 ("balans") is unaffected. KIT §2's
  repetition of the wrong headline must be corrected with the edition.

## Problem 2 (PROMISE GAP — W43 printed promise not honored, deferral undisclosed on the page)

- Locations: P7 BRIEVEN VAN LEZERS (example letter signed "Li") and P7 preview box
  (VOLGENDE WEEK · VOL.3: «Verder: jullie brieven en de beste teksten van pagina 8.»);
  absence of any real reader letter or best-P8-texts section anywhere in the issue.
- Evidence: W43 VOL.1's printed preview promised, verbatim (promises register §NL): "en jullie
  brieven en beste teksten van pagina 8. Tot maandag!" with the W45 action "print real reader
  letters and the best VOL.1 P8 texts (overdue)". This issue instead prints an editor's example
  letter and re-promises the same two items for VOL.3, printing no real letters and no best P8 texts.
- Note on labeling vs. promise: the labeling itself is UNAMBIGUOUS and is NOT the problem —
  P7 prints "— Li (voorbeeldbrief van de redactie)" plus the Chinese note "编辑部示例信，非真实来信。
  欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！". No reader could mistake Li for a real reader.
  The problem is the missing on-page disclosure: the page re-promises for VOL.3 as if on schedule
  and never says VOL.2 was supposed to carry real letters and that this is deferred for lack of
  real letters. The deferral is documented only in KIT §6, not on the page. This is the same
  standard applied to ES (ES Problem 2); EN passed this check precisely because its P7 page itself
  disclosed "no real reader letters had arrived when this issue went to press".
- Required fix: either (a) obtain and print real letters + best P8 texts, or (b) get an explicit
  parent/user decision recording the deferral AND disclose the deferral on the P7 page itself
  (e.g. one line: no real letters had arrived by press time, so the labeled example stands and
  real letters move to VOL.3). I cannot clear this one unilaterally.

## Problem 3 (MINOR — P8 key adds words outside the exercise prompt)

- Location: P8 ANTWOORDEN, key 99: «Rood komt weinig voor in Nederland.»
- Evidence: exercise 99's word list is exactly "rood / komt / weinig / voor → ___", and the P6
  article sentence is "Rood komt weinig voor." (no "in Nederland"). The key adds "in Nederland",
  which appears in neither the prompt nor the source sentence. All other sentence-building keys
  (97, 98, 100, 133–136) reproduce their prompts exactly, so this is an inconsistency, not a style.
- Required fix: key 99 → «Rood komt weinig voor.»

## Checked, NOT problems

- Scrutiny (a) Klimaatweek "national" framing — INDEPENDENTLY CONFIRMED, not a problem.
  Fresh search returns multiple independent confirmations of a national 2–8 Nov Klimaatweek:
  Berg en Dal municipal page: "Van 2 tot 8 november 2026 is de landelijke Klimaatweek";
  klimaatweek.nl sixth edition (315 Klimaatburgemeesters, 262 supporters, 156 gemeenten in 2025);
  Den Haag municipal programme for 2–8 Nov. The paper's "heel Nederland mee" / "Gemeenten in
  het hele land" framing is therefore supported beyond the Coevorden citation.
- Scrutiny (b) Crossing Border Festival Tue 3 – Sun 8 Nov, The Hague — INDEPENDENTLY CONFIRMED.
  Radio Bulgaria (bnrnews.bg, 8 Oct 2026): "the Crossing Border festival will run from 3 to 8
  November" in The Hague (Gospodinov appearance 6 Nov). Paper's "van dinsdag tot en met zondag"
  (3 Nov = Tuesday, 8 Nov = Sunday, verified with `date -d`) and ex. 45's 6-day count are correct.
- Scrutiny (c) KNMI 2 Nov switch date — ABSENT, as claimed. Full-edition grep: the paper only
  says warnings are "tegenwoordig lokaal" (P1, P2, P6 "zijn veranderd: vroeger … nu zijn ze
  lokaal") with no 2 Nov switch date printed anywhere. Clean.
- Scrutiny (d) Belastingplan — ABSENT, as claimed (0 hits across all 8 SVGs). Clean.
- Dates/weekdays (all `date -d`, Europe/Amsterdam): 2 Nov Monday, 3 Nov Tuesday, 7 Nov Saturday,
  8 Nov Sunday, 1 Nov Sunday, 25 Oct Sunday, 21 Oct Wednesday, 22 Oct Thursday, 11 Nov Wednesday,
  15 Nov Sunday — every printed weekday matches.
- Museumnacht (extra check): Sat 7 Nov 2026, 19:00–02:00, 26th edition, 70+ museums, one ticket,
  Museumkaart not valid — independently confirmed (events.europa.tips, tipsamsterdam.co.uk,
  artotel calendar). PAN Amsterdam 1–8 Nov, RAI, also confirmed.
- Numbers: numbering continuous 1–150 (P1 1–10, P2 11–28, P3 29–46, P4 47–64, P5 65–82, P6 83–100,
  P7 101–112, P8 113–150); `p8.py extract` on P8 SVG: noted set = 150 of 150; all 150 keys re-derived
  against questions/articles/chart except Problem 3; chart sums 45+25+20+10 = 100, 45+25 = 70;
  durations Klimaatweek 7 days, Museumnacht 19:00→02:00 = 7 hours, PAN 1–8 Nov = 8 days,
  Crossing Border 3–8 Nov = 6 days, Snuffelmarkt half of 250 = 125; matchday 12 = 9 matches
  (Fri 1 + Sat 3 + Sun 5); standings "24 ronden te gaan" after 10 of 34 rounds correct;
  model essay (P8 ex. 150) independently counted = 87 words (requirement 80–100).
- Golden sentences: all 8 verified verbatim (line-joined) against this issue's own articles with
  correct page labels — P1 ×2, P2, P3, P4, P5, P6 ×2. No classic/foreign sentence smuggled in.
- Explanation layer: every glossed word verified present in the text it annotates (P1 Klimaatweek/
  boom/besparen/waarschuwing; P2 klimaat/wortelen/verwarming/lokaal; P3 museum/rondleiding/
  tijdslot/tweedehands/beurs; P4 balans/gelijkspelen/speelronde/topper/stand; P5 eiland/proef/
  stemmen/aflevering/voorbij; P6 meteoroloog/waarschuwingsmoeheid/vastzetten/advies/voorstander;
  P7 klimaatwoorden/scheidbare werkwoorden/mening geven). P8 answer notes match questions except
  Problem 3. Banned term «桥接» 0 hits across all 8 SVGs.
- W43 promises: Robinson premiere (Sun 1 Nov, 20:00, RTL 4, 19 candidates) covered as just-passed
  and ongoing ("De eerste aflevering is geweest — nu begint het echte spel"), with NO eliminations
  or outcomes invented; ADE (30 years, 3,000+ artists, 200+ locations) and DDW (~2,500 designers)
  closings dated Sun 25 Oct; European-week results reported. No EU-budget, foreign-policy,
  Ukraine/Middle East/ICC items anywhere; no Sinterklaas/RDW items as leads (Sinterklaas appears
  only in the VOL.3 preview, correctly dated Sun 15 Nov Amsterdam; Sint-Maarten Wed 11 Nov correct).
- Dutch prose spot-checks accepted (not problems): P7 PAS OP item 4 ("Na «omdat» staat het
  werkwoord op plaats 2") — the Chinese note makes the intended rule unambiguous (main-clause verb
  second after the omdat-clause: "blijf ik thuis"); P5 ex. 72 "De kandidaten stemmen wie naar huis
  moet" — "stemmen" + wie-clause (vote on who) is acceptable usage; P8 ex. 131's answer follows
  the Daan text's own stated reason.
- Layout (all 8 PNGs viewed): no overflow, overlap, footer intrusion, or edge breach; P8 answers
  end above the footer; images match captions (P1 autumn forest, P2 Kinderdijk windmills,
  P3 Amsterdam canal boat, P4 1912 Netherlands team); credits present on every photo
  (Vovogov90 CC0; Nationaal Archief CC0; W. Punt / Anefo, Nationaal Archief CC0; Spaarnestad Photo,
  public domain); masthead "De Lucerna"; 8 pages, all SVGs 1950×2700; pairing footer
  ("荷兰语周报 VOL.2") and "第 N 版 / 共 8 版" page lines on all pages; ABSTRACT.txt present and
  fact-consistent (Klimaatweek, Museumnacht, speelronde 12, A2–B2, 150 oefeningen).
- Geometry: my own run — `occlusion_audit.py --selftest` OK (all 6 planted classes fired, clean
  controls silent); full audit on the edition dir: 0 flags. Builder's 0-flag claim confirmed.

## What must happen before finalizing

Fix Problems 1–3, re-render the whole issue, and submit it for a FRESH full independent proof
round per SOP §8.4 — a fix-and-ship without a new full round does not count. This report does
NOT pre-approve any fix.

## Independent audit artifact

My own occlusion run output: 0 flags on `../files/weekly-report-w45-nl-core/svg` (selftest OK).
This report: `hidden_files/w45/nl-core-independent-proof.md`.
