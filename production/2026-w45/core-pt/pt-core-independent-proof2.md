# INDEPENDENT PROOFREAD — ROUND 2 — W45 Português core, VOL.2 (BRAZIL variant)

**Edition:** `files/weekly-report-w45-pt-core/` (8 SVGs, 8 PNGs, `A-Lucerna-VOL2-web.pdf`
+ `A-Lucerna-VOL2.pdf`, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
**Proofreader:** independent subagent, 2026-10-26 (NOT the builder, NOT the fix agent).
Round 1 report (`hidden_files/w45/pt-core-independent-proof.md`, 1 problem) and fix log
(`hidden_files/w45/pt-core-fix1.md`) were read but NOT trusted; every check below was
re-run or re-read from the rendered edition itself, in full — this is a complete fresh
round, not a spot-check of the fix.
**Method:** SOP §§1–8 + occlusion appendix read; all visible text extracted
independently from all 8 SVGs and read end to end; all 8 rendered PNGs viewed as
images; all dates re-checked with `date -d` (America/Sao_Paulo); numbering, P8 keys,
chart sums, model-essay word count, golden sentences, gloss anchoring, trend-pool and
W43-promise compliance re-verified programmatically where possible;
`tools/occlusion_audit.py` run with `--selftest` first, then on the edition dir.
Builder/fix files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: ZERO PROBLEMS — FINALIZES THIS CORE

Per-area verdicts (each stated separately, per task):

- **Text (Portuguese): ZERO PROBLEMS.** Full end-to-end read of all 8 pages:
  spelling, accents, agreement, conjugation, punctuation, repeated words, truncated
  sentences — no defects. Grammar points re-verified: conferir present
  (confiro/confere/conferimos/conferem), pretérito perfeito (revisei/chegou/dormiu/
  visitaram/levaram/foi/viveu/foram/recebeu/começou/chegaram), futuro do subjuntivo
  (tiver/for/chegar), imperatives (separe/confira; sentence-initial capitals
  consistent in Q75 "Separe" and Q100 "Confira"). No duplicated or cut-off sentences.
- **Numbers: ZERO PROBLEMS.** Numbering 1–150 continuous: standalone stems plus the
  three range groups (25–28, 52–55, 141–144) cover every integer 1–150 with no gap
  and no dupe; per-page counts 10/18/18/18/18/18/12/38. All P8 keys re-derived
  question by question against stems, articles, and charts — all correct, including
  the deliberate distinctions: Q87 total day 7h (noon→19h) vs Q119 exam 5h30;
  minute arithmetic 60+30+330=420 and 5×60+30=330; Lucas 11h→13h = 2h; Q58 "mais
  cedo" (17h < 18h); Q59 "mais" (round 34, Mon–Fri, vs 2 Copa games). Model essay
  counted programmatically: **93 words** (inside the 80–100 brief). Exact figure
  5,055,818 appears **nowhere**; only the vague "mais de 5 milhões" is printed.
  `tools/p8.py extract --total 150`: noted set = **150 of 150**.
- **Facts: ZERO PROBLEMS.** All dates/weekdays re-checked with `date -d`: Oct 31 Sat,
  Nov 1 Sun, Nov 2 Mon, Nov 3 Tue, Nov 7 Sat, Nov 8 Sun, Nov 15 Sun — every printed
  weekday matches. Enem day 1 (Nov 8: gates 12h/13h, test 13h30–19h Brasília,
  redação+Linguagens+Ciências Humanas) and day 2 (Nov 15: Natureza+Matemática,
  preview only) correct. Finados Nov 2 + feriadão Oct 31–Nov 2 correct. First legs
  reported without scores (P1, P4, calendar rows marked "(já jogado)"); return legs
  Nov 7 18h Arena MRV / Nov 8 17h São Januário as previews, results deferred to the
  next issue ("Os resultados da volta saem na próxima edição"). No scores, no
  standings, no election outcomes, no vote shares, no market figures anywhere:
  full-text sweep finds only question distractors ("votam para presidente" Q12,
  "um dia de votação" Q29, "uma votação" Q33, "uma pesquisa eleitoral" Q88) and
  calendar facts ("voltam do recesso eleitoral" P3/P4/P5) — no winner, no percentages,
  no candidate names, no market numbers. Nov 15 appears only as preview/scheduled
  date in every occurrence; Nov 20 never appears. No international politics.
- **Layout: ZERO PROBLEMS (visual).** All 8 PNGs viewed: no overflow, no overlap, no
  footer intrusion, photo + caption + CC0 credit clean, charts legible, P8 answer
  block ends well above the footer. P1 directory tight spacing and P3/P5 column
  whitespace are the builder's disclosed retained items; visually readable, not
  defects. Both PDFs verified at 8 pages each.
- **Geometry: ZERO PROBLEMS (independently re-run).** `tools/occlusion_audit.py
  --selftest` passed (all six planted classes fired, clean controls silent); my own
  run on the edition dir returned **0 flags** — nothing to adjudicate. No
  COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE flags.
- **Golden sentences: ZERO PROBLEMS.** All 8 P7 sentences verified programmatically
  to occur exactly 2× across the 8 SVGs (article + P7), each with the correct
  source-page label (P1 ×2, P2 ×2, P3 ×1, P4 ×1, P5 ×1, P6 ×1).
- **Explanation layer: ZERO PROBLEMS.** Glossed headwords checked present in the
  core text they annotate (feriadão, portão/portões, túmulo, ida/volta, reta final,
  véspera, segunda chamada, flor). All P8 answer notes are in Chinese throughout.
  Banned term «桥接» absent (0 hits across all 8 SVGs).
- **Images/credits: ZERO PROBLEMS.** Only one reused photo (P1 library students,
  credited "Foto: Gary Todd / Wikimedia Commons — CC0"); all other visuals are
  original charts built from verified facts. No Brazil-specific photo used without a
  clean license.
- **Trend-pool + W43-promise compliance: ZERO PROBLEMS.** Edition follows the
  trend-batch-B PT-BR lead (Enem week, Finados feriadão, Copa return legs, round 34
  Mon–Fri) and correctly withholds trend-pool extras that were not independently
  verified: exact 5,055,818, title-race/relegation standings, tourism +20% /
  R$ 28.5 bn, accessibility/school counts — none printed. W43 promises honored:
  Finados + Enem day 1 as the main line; Oct 31 Halloween and Nov 1 first legs as
  just-passed reports; Nov 15 as preview only; readers'-corner promise now disclosed
  on the page (see fix verification below).

## ROUND-1 FIX VERIFICATION — EXPLICITLY VERIFIED, NOT ASSUMED

Round 1's single problem (P7 readers'-corner promise gap) is **fixed and verified on
the rendered page**, in both languages, inside the box:

- **PT disclosure, present verbatim in the CARTAS DOS LEITORES box (P7):**
  "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não
  chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
- **CN disclosure, present verbatim in the same box, directly below the PT text:**
  "编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。"
- **Original labeling unchanged and unambiguous:** the example letter still carries
  "— EXEMPLO DA REDAÇÃO" and "编辑部示例，非真实来信。真实来信请寄编辑部，下期见！"
  — no fabricated reader, letter, name, or quote anywhere in the issue.
- **Reflow verified geometrically and visually:** letters box y 1304.5, height 489.0
  → bottom 1793.5; disclosure last baseline 1772.23, i.e. 21.3 px of padding fully
  inside the box, no border contact, no overlap. Golden-sentences last baseline
  2358.17 vs preview box top 2404 → clear. Preview box and footer intact on the
  rendered P7 PNG; the VOL.3 re-promise in the preview box no longer stands alone
  as if on schedule, because the deferral disclosure now sits in the corner itself.

## Readers'-corner honesty (task §6) — CONFIRMED

The corner is a labeled editor's example plus an explicit deferral disclosure stating
the real letters + best texts promised in VOL.1 did not arrive by press time and the
promise carries to VOL.3. No real letter is claimed, no reader invented, no quote
fabricated.

## Independent audit artifacts

- My occlusion run: edition dir → 0 flags, selftest OK (this round's run; output not
  persisted beyond this report's statement, per the audit tool's stdout).
- Per-page extracted text used for this proof: `/tmp/ptproof2/p1-capa.txt` …
  `/tmp/ptproof2/p8-avaliacao.txt` (independent extraction, not the builder's files).
- `tools/p8.py extract --total 150`: noted set = 150 of 150.

## Conclusion

This round finds **zero problems** across text, numbers, facts, layout, and geometry,
and the round-1 fix verifies on the rendered page. Per SOP §8.4, this full round
finalizes the W45 Português core, VOL.2 (BRAZIL variant). No further proof round is
required for this core on the basis of the round-1 item; any future change to the
edition would need its own fresh round.
