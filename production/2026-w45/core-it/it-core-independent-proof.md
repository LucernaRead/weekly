# INDEPENDENT PROOFREAD — Lucerna Weekly W45 Italiano core, VOL.2

**Role:** independent proofreader (fresh eyes, skeptical stance) — NOT the builder.
**Edition:** `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-core/`
(8 SVGs, 8 cards PNGs, `La-Lucerna-VOL2-web.pdf`, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
**Method:** SOP `weekly-report-SOP.md` §§1–8 + occlusion appendix, read in full.
Fresh SVG text extraction of the CURRENT SVGs (the builder's archived
`hidden_files/w45/it-core/proof-text.txt` is STALE — timestamped before the final
rebuild, it still shows the pre-fix wordings; every finding below was verified
against the current SVGs and the rendered PNGs, not against that file).
All 8 rendered pages viewed as images. Dates re-checked with `date -d`
(Europe/Rome). Geometric audit run independently (see §6).

## VERDICT: 7 PROBLEMS — NOT FINALIZED

The core does NOT pass the SOP §8 zero-problem gate. It must be fixed,
re-rendered, and re-proofed from scratch before delivery. The single most
serious defect is Problem 1 (wrong printed answers); Problems 2–7 are each
independently real but smaller.

---

## Numbered problem list

### Problem 1 (HARD — wrong answers printed): P8 keys for Q54/Q55 are swapped

- **Location:** P8 `RISPOSTE — PAGINA 4`: "54. d — spalti=看台 d" and
  "55. a — sera=晚上 a".
- **Evidence:** P4 exercise B (Q52–55) prints the options in this order,
  confirmed both in the SVG and on the rendered P4 image:
  a. "il posto del pubblico allo stadio, con le gradinate" (= the stands);
  b. "il racconto prima della partita, senza risultati";
  c. "ciascuna delle parti del campionato, una dopo l'altra";
  d. "la parte del giorno dopo il tramonto, con le luci accese" (= evening).
  Questions: 52. la giornata, 53. la presentazione, 54. gli spalti, 55. la sera.
  Correct mapping is therefore 52=c, 53=b, **54=a, 55=d**.
  The P8 key prints 54=d and 55=a — exactly swapped. A learner who answers
  correctly is marked wrong, and vice versa.
- **Fix:** P8 keys 54→a, 55→d (and the KIT's claim "P4 matching keys checked"
  is false for this item).

### Problem 2 (SOP §8 gloss rule): P1 gloss word «la degustazione» does not occur in the P1 core text

- **Location:** P1, gloss box under the lead article:
  "讲解｜il primo freddo … · la degustazione 品尝。"
- **Evidence:** Full-text search of p1-prima.svg: `degustazione` occurs exactly
  once — inside the gloss itself. P1's article contains no `degustazione`,
  no `degustazioni`, no `assaggio`, no `assaggiare`. The tasting word P1's own
  text actually uses is "assaggi" ("un weekend di assaggi"). SOP §8 requires
  every glossed word to actually appear in the core text it annotates, and the
  KIT's claim "every gloss word checked against body text" is false for this
  item. (`degustazioni` does occur on P3, but that does not annotate P1.)
- **Fix:** gloss "l'assaggio" (the word P1 uses) or drop the item.
- **Checked clean for contrast:** all other gloss boxes are attested on their
  own page (P2 cappotto/sciarpa/guanti/a strati/termosifone/crisantemo;
  P3 panettone/torrone/assaggio-verb/bancarelle/cantiere; P4 giornata/
  presentazione/spalti/sera; P5 cosplay/gratuito/documentario/schermo;
  P6 probabilità/media/modello/bollettino/aggiornare).

### Problem 3 (Manovra 2027 temporal/disclosure failure — scrutiny item)

- **Location:** P2 "E LA SETTIMANA SCORSA?" paragraph and P6 "E la manovra?"
  sidebar.
- **Actual printed wording (current SVGs, verified on the rendered pages):**
  P2: "Anche la manovra, la legge di bilancio, era attesa al voto intorno al
  28 ottobre: il punto difficile resta il contributo chiesto a banche e
  assicurazioni. Ne parliamo a pagina 6, con i numeri del documento ufficiale."
  P6: "il voto era atteso intorno al 28 ottobre, e il punto difficile resta il
  contributo chiesto a banche e assicurazioni."
- **Judgment:** No vote outcome is printed anywhere (grep: `esito` 0,
  `Stabilicum` 0 — no fabrication, and the verb is past-tense "era attesa",
  so the vote is NOT presented as still upcoming). That passes the
  fabrication test. It FAILS the honesty test the task sets: the wording is
  not framed as "outcome not yet confirmed at press time" — it says nothing
  at all about the outcome. This issue is dated Monday Nov 2, five days AFTER
  Oct 28, and it reports the vote only as a past expectation, leaving the
  reader with an unresolved story and no disclosure. The earlier draft's one
  disclosure sentence ("senza inventare l'esito") was removed by the
  builder's fix #2, which weakened rather than strengthened the page.
  The W43 promise of a vote-outcome report is therefore unfulfilled (the KIT
  §6 admits this only as "partially honored" — the page itself does not say
  so). DPB figures printed (sent to Brussels Oct 15; growth +0.8%; deficit
  3.4% of PIL; bank/insurance contribution dispute) are consistent with the
  trend pool and no outcome is invented — the defect is omission/disclosure,
  not invention.
- **Fix:** add one honest on-page clause, e.g. that the outcome was not
  confirmed at press time, or report the outcome once verified. Do not leave
  a Nov 2 reader with a dangling "was expected around Oct 28".

### Problem 4 (completeness): P1 "day by day" box omits Friday Nov 6 entirely

- **Location:** P1, "LA SETTIMANA GIORNO PER GIORNO / 本周日程 ·
  Cosa succede, giorno per giorno".
- **Evidence:** the box lists LUN 2, MAR 3, MER–GIO 4–5, SAB 7, DOM 8 — no VEN 6
  entry, although Friday Nov 6 is the day Serie A matchday 11 begins (P4's own
  fixture table: "Ven–Dom, Serie A, 11ª giornata"). A box headed "day by
  day" that skips one day of the week misleads learners counting the days.
- **Fix:** add a VEN 6 line (e.g. Serie A MD11 opens) or retitle the box so
  it does not promise every day.

### Problem 5 (model-language defect): P7 reader's letter drops the articles

- **Location:** P7, "LETTERE DEI LETTORI": "Lunedì metto cappotto e sciarpa,
  sabato assaggio il panettone — almeno in foto!"
- **Evidence:** standard Italian requires "metto il cappotto e la sciarpa"
  — the edition's own P2 article writes exactly that ("il cappotto, la
  sciarpa e i guanti"). The article-less "metto cappotto e sciarpa" is a
  side-effect of the geometry shortening and models nonstandard usage in a
  teaching paper's model letter.
- **Fix:** restore "il cappotto e la sciarpa" (re-flow the letter box;
  do not sacrifice correctness for fit).

### Problem 6 (SOP §9 + house convention): ABSTRACT.txt is in Italian, not the reader's native language

- **Location:** `files/weekly-report-w45-it-core/ABSTRACT.txt`:
  "La Lucerna VOL.2, settimana 2–8 novembre 2026: il primo freddo, il Forum
  Cultura di Milano, … 150 esercizi con risposte."
- **Evidence:** SOP §9 requires the abstract to be written in the reader's
  native language. This core's explanation layer is Simplified Chinese
  (zh-CN), and the W43 precedent proves the convention: the shipped
  `2026-w43-it-zh-cn` entry in `weekly-git/index.json` carries a Chinese
  abstract, and `2026-w43-it-en` carries an English one. An Italian abstract
  for a zh-CN-reader edition would be copied verbatim into the repo
  frontmatter/index.json by insert.py.
- **Fix:** rewrite ABSTRACT.txt in Simplified Chinese (same facts: first
  cold, Forum Cultura, Panettone final, Torrone, Serie A MD11, A2–B2,
  150 exercises), before any repo insert.

### Problem 7 (KIT vs edition mismatch): level tally off by one

- **Location:** KIT §1 claims "By level: A2 47, B1 70, B2 33".
- **Evidence:** counting the level badge printed before every question number
  in the current SVGs gives A2 46, B1 71, B2 33 (per page: P1 9/1/0;
  P2 16/2/0; P3 8/10/0; P4 0/16/2; P5 0/15/3; P6 0/0/18; P7 4/4/4;
  P8 9/23/6; total 150, B2 agrees). Either one printed badge has the wrong
  level or the KIT tally is miscounted by one. The pair cannot both be right.
- **Fix:** reconcile badge-by-badge against the exercise registration table;
  correct whichever side is wrong and re-verify the tally.

---

## What passed (verified independently, not taken from the KIT)

- **Numbering:** questions 1–150 continuous, no gaps or duplicates, on every
  page (P1 1–10, P2 11–28, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38) and
  answers 1–150 complete on P8.
- **P8 keys otherwise:** every other key re-checked against its question,
  article text, or chart — including P2 matching (25c/26d/27a/28b), P3
  passato prossimo (40 è arrivato, 41 abbiamo assaggiato, 42 sono andati,
  43 ha aperto), P4 comparatives/passato (56 più tardi, 57 più presto,
  58 più bella, 59 meglio, 60–64 ha vinto/ha pareggiato/sono arrivati/
  abbiamo guardato/ha preso), P5 futuro (76 andremo, 77 ci sarà,
  78 guarderemo, 79 durerà; 80 Vero, 81 Vero, 82 Falso), P6 chart
  (83 Torino, 84 Napoli, 85 12−9=3, 86 4+5=9, 87 invented data), P6/P7
  congiuntivo (93/109 piova, 94/110 nevichi, 95 controllino, 96/111 sia),
  P7 (101 piove, 102 fa, 103 nevica, 104 B, 105 è arrivato, 106 abbiamo
  assaggiato, 107 sono andati, 108 B ha aperto, 112 B arriva), P8 F matching
  (141d/142a/143b/144c), P8 G dialogue and H model.
- **Writing model:** 81 words counted by hand from the printed text —
  inside the 80–100 brief. P8 H label "(81 词)" is correct.
- **Golden sentences:** all 8 P7 quotes occur exactly 2× in the joined SVG
  text (once in their article, once on P7), with correct page attributions
  (P1, P1, P2, P2, P3, P4, P5, P6). All are verbatim from this issue's own
  articles.
- **Dates/weekdays** (`date -d`, Europe/Rome): Nov 2 Mon, Nov 1 Sun,
  Nov 3 Tue, Nov 4 Wed, Nov 5 Thu, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun,
  Nov 9 Mon, Nov 22 Sun, Dec 6 Sun, Oct 28 Wed, Oct 30 Fri, Oct 15 Thu,
  Oct 10 Sat — every printed weekday/date pairing in the edition is correct.
  Serie A MD11 Nov 6–8 and European MD4 Nov 3–5 are printed as previews with
  explicit "senza risultati" notes; no results are printed or invented.
  Panettone World Cup final Nov 7–8, Torrone Nov 7–22, Forum Cultura
  Nov 3–8, Festival dei Popoli Nov 3–9 (closes Mon Nov 9, as the VOL.3
  preview states) all agree with the trend pool. Alba White Truffle Fair
  Oct 10–Dec 6 was additionally web-verified (three sources agree).
  Lucca Comics 60th Oct 28–Nov 1 and Ognissanti Sun Nov 1 "niente ponte"
  are correctly reported as just-passed and match the W43 VOL.1 preview.
- **Trend/red-line compliance:** lead is «Il primo freddo» from the IT trend
  pool, not a commemoration; Nov 4 appears only as a European-cup day, with
  no Giorno dell'Unità Nazionale / Forze Armate lead; no Ecofin framing;
  no geopolitical framing; no international politics (grep: Ucraina,
  Putin, Russia, guerra, Ecofin, Stabilicum all 0). Banned term «桥接» absent
  (0). Weather wording is forecast/probability language throughout
  ("Le previsioni parlano di…", "Non è una certezza, è una probabilità"),
  and P6 explicitly teaches the forecast-vs-fact distinction; the practice
  chart is labeled "DATI INVENTATI PER L'ESERCIZIO" in its title, box
  header, caption, and Q87.
- **Readers' corner honesty (item 8 — PASSES):** the P7 letter is labeled
  in BOTH languages on the page — Italian "— Li (esempio della redazione)"
  and Chinese "这是编辑部示例信，非真实来信" — and the deferral IS disclosed
  on the page, not only in the KIT: "来信请寄编辑部，VOL.3 刊登真实来信与第 8 版
  最佳作文！" plus the VOL.3 preview ("le vostre lettere vere e i testi
  migliori della pagina 8") and the P2 invitation for VOL.3. No reader,
  letter, or quote is fabricated as real. (The W43 promise itself remains
  unfulfilled — real letters and best P8 texts are deferred to VOL.3 — but
  the deferral is honestly disclosed on the page, which is the standard set
  for this check.)
- **Images/captions:** P1 frost is a programmatic drawing captioned
  "Disegno della redazione" (not presented as a photo) ✓; P3 truffle photo
  captioned "Foto: Wikimedia Commons — dominio pubblico" and the image
  matches its caption ✓; P5 chestnut photo captioned "Foto: Wikimedia
  Commons — CC0" and matches ✓. No CC BY panettone photo was used, per the
  SOP's PD/CC0-only rule. P2 clocks and P6 chart are programmatic drawings.
- **Masthead/pairing:** "La Lucerna" (correct Italian feminine article),
  VOL.2, issue week Nov 2–8 2026, Italian-weekly + Chinese furniture and
  page footers throughout ✓. 8 pages (multiple of 4) ✓.
- **Italian language (otherwise):** no spelling, accent, agreement,
  conjugation, or punctuation errors found in a full end-to-end read of all
  8 pages — passato prossimo auxiliaries, congiuntivo and futuro forms,
  comparatives, and the P7 grammar columns are all correct, apart from
  Problem 5. No truncated sentences or repeated words found. The P2
  "come avevamo previsto nel VOL.1" claim is true (W43 preview did say
  Ognissanti falls on Sunday with no ponte).

## Geometry (§6, independent run)

- `tools/occlusion_audit.py --selftest`: OK (all 6 planted classes fired,
  clean controls silent).
- Independent audit run on the edition dir: **0 flags, exit 0**
  (output: `/tmp/itcore-occlusion-mine.json`; builder's
  `hidden_files/w45/it-core/occlusion.json` also reports 0 — agreed).
- Visual check of all 8 rendered PNGs: no overflow, overlap, footer
  intrusion, or edge breach. The builder's flagged tight spots are clean on
  the image: P4 main flow ends above its box bottom, P6 exercises end above
  the footer, and the P7 gold rule sits clear below the letter box
  (col3 ends y=1673 vs rule y=1686). P8 answers end well above the footer.
  (P5's middle column has generous white space below the gloss box — air,
  not a defect.)

## Process notes (not counted as edition problems)

- The builder's archived `proof-text.txt` predates the final rebuild and
  still shows pre-fix wordings (e.g. the old P2 "senza inventare l'esito"
  sentence, the old P1–P7 gloss/bridge strings). The current SVGs DO contain
  the 8 KIT-claimed fixes. The scratch proof record should be refreshed so
  the next proofreader does not audit a stale text.
- The KIT's self-proof claims "P4 matching keys checked" and "every gloss
  word checked" are contradicted by Problems 1 and 2 above; the KIT should
  not repeat those claims after the fix round.
- Not verified as false, noted only: P5's "molti eventi sono gratuiti"
  (Forum Cultura) is not stated in the trend-pool excerpt; no contradiction
  was found, so it is not flagged.
- No files were edited. Nothing was pushed to git, posted to Discord, or
  messaged to anyone. Delivery remains the main line's job after a fix round
  and a fresh full proofread.
