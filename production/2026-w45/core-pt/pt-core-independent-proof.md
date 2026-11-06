# INDEPENDENT PROOFREAD — W45 Português core, VOL.2 (BRAZIL variant)

**Edition:** `files/weekly-report-w45-pt-core/` (8 SVGs, 8 PNGs, `A-Lucerna-VOL2-web.pdf`, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
**Proofreader:** independent subagent, 2026-10-26 (NOT the builder). Builder's record
(`hidden_files/w45/pt-core/proof-record.md`, `occlusion3.json`) was read but NOT trusted;
every check below was re-run or re-read from the rendered edition itself.
**Method:** SOP §§1–8 + occlusion appendix read first; full visible text extracted
independently from all 8 SVGs and read end to end; all 8 rendered PNGs viewed; all
dates re-checked with `date -d` (America/Sao_Paulo); exercise numbering, P8 keys,
chart sums, model-essay word count, gloss anchoring, golden sentences, trend-pool
compliance, and W43 promises re-verified; `tools/occlusion_audit.py` run with
`--selftest` first, then on the edition dir; `tools/p8.py extract` re-run.
Builder files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: 1 PROBLEM — NOT ZERO-PROBLEM, DO NOT FINALIZE YET

Per-area verdicts:

- **Text (Portuguese): CLEAN.** Full end-to-end read of all 8 pages: spelling, accents,
  agreement, conjugation, punctuation, repeated words, truncated sentences — no defects
  found. Spot-verified grammar points all correct: conferir present (confiro/confere/
  conferimos/conferem), pretérito perfeito (revisei/chegou/dormiu/visitaram/levaram/
  foi/viveu/foram/recebeu/começou/chegaram), futuro do subjuntivo (tiver/for/chegar),
  imperatives (separe/confira, sentence-initial capitals consistent).
- **Numbers: CLEAN.** Numbering 1–150 continuous, no gaps/dupes; per-page counts
  10/18/18/18/18/18/12/38; levels A2 49 / B1 70 / B2 31 (matches KIT). All P8 keys
  re-derived question by question against stems, articles, and charts — all correct,
  including the 7h-vs-5h30 distinction (Q87 total day 7h vs Q119 exam 5h30), minute
  arithmetic (60+30+330=420; 5×60+30=330), and the Lucas 11h→13h = 2h check.
  Model essay counted programmatically: **93 words** (inside the 80–100 brief).
  Exact registration figure 5,055,818 appears **nowhere**; only the vague
  "mais de 5 milhões" is printed (P1, P5, P6).
- **Facts: CLEAN (except the promise item below).** All dates/weekdays re-checked with
  `date -d`: Oct 31 Sat, Nov 1 Sun, Nov 2 Mon, Nov 3 Tue, Nov 6 Fri, Nov 7 Sat,
  Nov 8 Sun, Nov 15 Sun — every printed weekday matches. Enem day 1 (Nov 8: gates
  12h/13h, test 13h30–19h Brasília, redação+Linguagens+Ciências Humanas) and day 2
  (Nov 15: Natureza+Matemática, preview only) correct. Finados Nov 2 + feriadão
  Oct 31–Nov 2 correct. No scores, no standings, no election outcomes, no vote shares,
  no market figures anywhere (see "Checked, not problems").
- **Layout: CLEAN (visual).** All 8 PNGs viewed: no overflow, no overlap, no footer
  intrusion, photo + caption + CC0 credit clean, charts legible, P7 golden block clear
  of the preview box, P8 answer block ends well above the footer. P1 directory
  title/level tight spacing and P3/P5 column whitespace are the builder's disclosed
  retained items; visually readable, not defects.
- **Geometry: CLEAN (independently re-run).** `tools/occlusion_audit.py --selftest`
  passed (all six planted classes fired, clean controls silent); my own run on the
  edition dir returned **0 flags**, matching the builder's `occlusion3.json`.
  No COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE flags to adjudicate.
  My audit output: `/tmp/ptproof/occlusion-independent.json` (0 flags).
- **Golden sentences: CLEAN.** All 8 P7 sentences verified programmatically to occur
  exactly 2× across the 8 SVGs (article + P7), each with the correct source-page label:
  P1 ×2, P2 ×2, P3 ×1, P4 ×1, P5 ×1, P6 ×1 (labels: P1, P1, P2, P3, P4, P5, P6, P2).
- **Explanation layer: CLEAN.** Every glossed word's lemma appears in the core text it
  annotates (incl. plural-form lemmas portão/portões, finalista/finalistas). All P8
  answer notes are in Chinese throughout. Banned term «桥接» absent (0 hits).
- **Images/credits: CLEAN.** Only one reused photo (P1 library students, credited
  "Foto: Gary Todd / Wikimedia Commons — CC0"); all other visuals are original charts
  built from verified facts (Enem times, football calendar). No Brazil-specific photo
  used without a clean license.

## PROBLEM 1 (PROMISE GAP — W43 printed promise not disclosed on the page)

- **Locations:** P7 CARTAS DOS LEITORES box and P7 preview box
  ("Mais: as suas cartas e os melhores textos da página 8"); absence of any
  real-letters or best-P8-texts section anywhere in the issue.
- **Evidence:** W43 VOL.1's printed preview promised, verbatim: "Mais: as suas cartas
  e os melhores textos da página 8. Até segunda!" The promises register
  (`hidden_files/w45/w43-promises.md` §PT) records the W45 action as: "print real
  reader letters and the best VOL.1 P8 texts (overdue)". VOL.2 instead prints an
  editor's example letter and re-promises the same two items for VOL.3, printing no
  real letters and no best P8 texts.
- **Labeling vs. disclosure (distinguished carefully):** the corner's LABELING is
  unambiguous and is NOT the problem — the letter carries "— EXEMPLO DA REDAÇÃO" and
  the Chinese note "编辑部示例，非真实来信。真实来信请寄编辑部，下期见！" No reader
  could mistake it for a real letter, and no name is invented. What is missing is
  the DEFERRAL DISCLOSURE: the page never says that VOL.2 was supposed to carry real
  letters (per the W43 promise) and that none had arrived, so the example stays; it
  merely invites letters and re-promises them for VOL.3 as if on schedule. This is
  the same standard applied to EN (disclosure on the page → debt carried, not a
  problem) and ES (KIT-only disclosure → Problem 2) in this cycle. The KIT does
  record the gap honestly ("读者园地说明（据实登记，与承诺登记的出入）"), but
  KIT-only disclosure does not satisfy the on-page standard.
- **Required fix (one of):** (a) obtain and print real letters + best P8 texts, or
  (b) get an explicit parent decision recording the deferral AND add an on-page
  disclosure in the P7 corner (e.g. the EN wording pattern: no real letters had
  arrived when this issue went to press, so the labeled example stays) — the
  VOL.3 re-promise must not stand alone as if on schedule. I cannot clear this
  unilaterally.
- **Consequence:** per SOP §8.4, after the fix the edition must be re-rendered and
  given a fresh full independent proof round; this report does not pre-approve the
  fixed version.

## Scrutiny items (task §3) — all resolved

- **(a) Nov 7 return-leg time (18h, Arena MRV): INDEPENDENTLY CONFIRMED, not a
  problem.** Sportradar fixture data (independent of the trend pool) lists
  Atlético-MG × Grêmio, Copa do Brasil 2026 Semifinal Leg 2, Saturday 7 Nov 2026,
  1:00 PM PST = 18:00 Brasília, home venue Arena MRV (Atlético-MG's home ground).
  The same source cross-confirms the first leg (Grêmio × Atlético-MG, Sun 1 Nov,
  1:30 PM PST = 18h30 Brasília) and the Nov 8 leg (Vasco × Palmeiras, Sun 8 Nov,
  12:00 PM PST = 17:00 Brasília, Estádio São Januário, confirmed separately by
  footballticket.club's local-time listing). The printed preview times are right
  and stay.
- **(b) No election outcomes / vote shares / market figures: CONFIRMED.** Full-text
  sweep finds only: three question distractors ("votam para presidente" P2 Q12,
  "um dia de votação" P3 Q29, "uma votação" P3 Q33), one chart-question distractor
  ("uma pesquisa eleitoral" P6 Q88), and one calendar fact ("voltam do recesso
  eleitoral" P4 calendar). No winner, no percentages, no market numbers, no
  candidate names anywhere.
- **(c) First legs reported as played WITHOUT scores, results deferred: CONFIRMED.**
  P1 ("o domingo, 1º, teve os jogos de ida"), P4 ("Os jogos de ida foram no domingo,
  1º de novembro", calendar rows marked "(já jogado)") print dates/times/venues
  only; P4's closing note states "Os resultados da volta saem na próxima edição."
  No invented scores anywhere.
- **(d) Nov 15 Enem day 2 only as preview, never as done: CONFIRMED.** Every Nov 15
  mention is preview/factual-schedule: P5 box "(prévia)", P6 "o dia 15 é a prévia da
  próxima semana" + "Dia 15 — a cobertura sai na próxima edição", P7 next-issue
  preview, P8 Q120 (a scheduled-date question, keyed 15). Nov 20 never appears.

## Checked, not problems

- Oct 31 / Nov 1 appear ONLY as just-passed past-tense reports (P1 "foi", P3 "foi",
  P4 "Ontem, domingo 1º, já foi de Copa", P5 "foi Halloween") — never as previews.
- Finados Nov 2 + Enem day 1 Nov 8 honored as the issue's leads (P1 headline, whole
  issue architecture); Nov 15 / Proclamação da República appear only inside the P7
  next-issue preview, never as leads.
- No foreign reactions, no international politics anywhere. Brazil domestic politics
  appears only as the calendar fact of state assemblies returning from recess
  (Nov 3) — no partisan content.
- "No horário de verão desde 2019" (P2) is correct; DST was abolished in Brazil in
  2019.
- P8 Q93 key "começará" (future) is the natural reading for a pre-exam issue dated
  Nov 2; P8 Q100 key "Confira" is the sentence-initial capital of "confira" (the
  note's own form) — consistent, not a mismatch. P8 Q75 "Separe"/"separe" likewise.
- P6 "LER OS NÚMEROS" box and Q88's "pesquisa eleitoral" distractor teach source
  skepticism; they are not printed election data.
- P1 photo caption's "(Página 5)" cross-reference points at the youth/reta-final
  page, whose theme the caption describes — accurate.
- P3 "PALAVRAS DE FINADOS" counts six items (five words + the phrase «descanse em
  paz») — the "seis palavras" label covers the set as printed.

## Independent audit artifacts

- My occlusion run: `/tmp/ptproof/occlusion-independent.json` (0 flags, selftest OK).
- Per-page extracted text used for this proof: `/tmp/ptproof/p1-capa.txt` …
  `/tmp/ptproof/p8-avaliacao.txt` (independent extraction, not the builder's files).
- `tools/p8.py extract --total 150`: noted set = 150 of 150.

## What must happen before finalizing

1. Resolve Problem 1 with the parent (honor the letters/best-texts promise or
   formally disclose the deferral ON the P7 page).
2. Re-render the whole issue, then run a FRESH full independent proof round
   (SOP §8.4) — a fix-and-ship without a new full round does not count.
