# FIX ROUND 1 — Lucerna Weekly W45 Italiano core, VOL.2

Fix agent response to the independent proofread
(`hidden_files/w45/it-core-independent-proof.md`, 7 problems, verdict NOT FINALIZED).
All 7 problems fixed in the build code, full issue re-rendered, gates re-run.
Nothing pushed to git, nothing posted to Discord, nobody messaged.
Finalization is NOT self-certified: a fresh full independent proof round is still required.

## Fix 1 (HARD — P8 keys Q54/Q55 swapped)
- Cause: `content34.py` P4 match_set registered keys `["c","b","d","a"]` with
  notes `spalti=看台 d`, `sera=晚上 a`. P8 keys are generated from that registry,
  so the swap propagated to P8.
- Fix (`content34.py` only): keys → `["c","b","a","d"]`; notes →
  `spalti=看台 a`, `sera=晚上 d`.
- Re-verified from fresh SVGs, full P4 matching set: options in printed order
  a = il posto del pubblico allo stadio, con le gradinate (stands);
  b = il racconto prima della partita, senza risultati (pre-match story);
  c = ciascuna delle parti del campionato, una dopo l'altra (round);
  d = la parte del giorno dopo il tramonto, con le luci accese (evening).
  Questions 52 la giornata, 53 la presentazione, 54 gli spalti, 55 la sera.
  Correct mapping 52=c, 53=b, 54=a, 55=d — P8 now prints exactly that
  (52. c, 53. b, 54. a, 55. d), confirmed in the rendered P8 PNG answer block.

## Fix 2 (P1 gloss «la degustazione» unattested)
- Fix (`content12.py`): P1 gloss item `la degustazione 品尝` → `assaggi 品尝`.
- Anchoring verified in fresh P1 SVG: `degustazione` count 0; `assaggi`
  occurs twice — once in the P1 body ("un weekend di assaggi") and once in
  the gloss itself. No other gloss touched.

## Fix 3 (Manovra Oct 28 — omission, NOT invention)
- Parent decision followed exactly: past-tense wording kept outcome-free
  ("era attesa / era atteso intorno al 28 ottobre"); NO outcome invented.
- Disclosure added in BOTH Manovra mentions, Italian + matching Chinese:
  - P2 (`content12.py`): para now ends "...il punto difficile resta il
    contributo di banche e assicurazioni. Al momento di andare in stampa,
    l'esito non era ancora confermato: ne parliamo a pagina 6." + bridge
    "发稿时表决结果尚未确认，详见第 6 版。" (Same line count as before:
    the para still wraps to 7 lines; P2-feature flow ends y=1519, bottom 1540.)
  - P6 (`content56.py`): sidebar para extended with "Al momento di andare
    in stampa, l'esito del voto non era ancora confermato: qui riportiamo
    solo la data attesa, il punto difficile e i numeri del DPB, senza
    indicare alcun esito." + bridge "发稿时 10 月 28 日表决结果尚未确认：
    本期只写预期日期、争议点和 DPB 数字，不写结果。" (P6-main flow ends
    y=1353, bottom 1520.)
  - Implementation note: the first P6 bridge draft ended with a lone "。"
    on its own line (the orphan-punctuation class the builder's earlier
    proofread had eliminated elsewhere); it was shortened by two characters
    ("不写表决结果" → "不写结果") so the note wraps to 2 lines with no
    orphan. Fresh orphan-punctuation scan: 0 lone-punctuation lines on all
    8 pages.
- DPB figures, expected date, and dispute wording otherwise unchanged.

## Fix 4 (P1 day-by-day box omits Friday Nov 6)
- Fix (`content12.py`): added "VEN 6 — Apre l'11ª giornata di Serie A."
  between MER–GIO 4–5 and SAB 7. Content is already in the issue (P4:
  Serie A MD11 runs Fri Nov 6 – Sun Nov 8); no new event invented.
- Reflow, P1 only: the day-box entry loop spacing was tightened
  (offset +22 → +16, gap +10 → +6 per entry) so the 6-entry box ends at
  the same height as before. Verified in fresh P1 SVG: VEN 6 baseline
  y=975.2; box footer last line baseline y=1237.2, inside the box
  (580–1280); sommario untouched. Rendered P1 PNG inspected: all 7 days
  listed, footer inside the box, no overlap.

## Fix 5 (P7 letter drops articles)
- Fix (`content7.py`): "Lunedì metto cappotto e sciarpa" →
  "Lunedì metto il cappotto e la sciarpa" (guanti is not mentioned in the
  letter, so no third article applies). No other letter wording shortened:
  the letter still wraps to 5 lines, so P7 col3 still ends y=1673.0,
  13 px clear of the FRASI rule at y=1686. Rendered P7 PNG inspected:
  letter box clear of the rule, no overflow.

## Fix 6 (ABSTRACT.txt language)
- Rewrote `files/weekly-report-w45-it-core/ABSTRACT.txt` in Simplified
  Chinese (reader-native language for this core, per the verified W43
  precedent: W43 it-zh-cn abstract is Chinese).
- New text, one single line, no ASCII double quotes:
  "La Lucerna VOL.2，2026年11月2–8日一周：第一场寒冷、米兰文化论坛、
  潘妮托尼世界杯决赛、克雷莫纳牛轧糖节、意甲第11轮——读真实的意大利，
  学意大利语，A2–B2，150道练习附答案。"
- Verified: 1 line (`wc -l` = 1), 0 ASCII `"` characters; topics match the
  printed issue (il primo freddo, Forum Cultura, Panettone World Cup final,
  Festa del Torrone, Serie A MD11); masthead La Lucerna VOL.2, A2–B2,
  and 150 exercises all present. No page content changed for this fix.

## Fix 7 (Level tally mismatch — badge vs KIT)
- Investigation: fresh registry count before the fix was A2 46 / B1 71 /
  B2 33, matching the independent proof's printed-badge count exactly;
  KIT §1 claimed A2 47 / B1 70 / B2 33. B2 agreed on both sides, so the
  single wrong item had to be an A2↔B1 item.
- Identification: P2 Q18 "portare: loro → portano" was labeled B1 while its
  immediate neighbour Q19 "guardare: loro → guardano" — same exercise head
  (B · IL PRESENTE), same regular -are verb class, same person (loro),
  same task — was labeled A2, as were Q17 (mettere, io) and Q20 (restare,
  lei) in the same head. No principled distinction supports B1 for Q18;
  regular present-tense conjugation is A2 material under the edition's own
  convention (and the W43 VOL.1 split, A2 46 / B1 71 / B2 33, is a different
  issue's count, not evidence for this one). Q18 was therefore the
  mislabeled badge, not the KIT tally.
- Fix (`content12.py`): Q18 level B1 → A2. The KIT §1 tally was NOT edited:
  it now matches the printed badges exactly.
- Re-verified: fresh registry + printed-badge count both A2 47 / B1 70 /
  B2 33 (total 150); P2 chip sequence in fresh SVG shows Q18 with an A2
  chip and Q24 still B1; rendered P2 PNG inspected (A2 18. visible).

## Re-render + gates (final render, after all 7 fixes)
- Build: `run.py` — FLOW OVERFLOW 0, HEAD TOO WIDE 0.
- Render: `render.py` — all 8 SVGs + 8 cards PNGs + both PDFs regenerated:
  print PDF La-Lucerna-VOL2.pdf (21,037,777 bytes),
  web PDF La-Lucerna-VOL2-web.pdf (3,440,887 bytes).
- Counts: 8 pages; 150 exercises (by page 10/18/18/18/18/18/12/38);
  levels as printed A2 47 / B1 70 / B2 33; model text 81 words (unchanged).
- Own re-read: every changed page re-read in fresh SVG text and on the
  rendered PNG (P1 gloss + day box, P2 Manovra + Q18 chip, P4 matching set
  in full, P6 Manovra sidebar, P7 letter, P8 keys 52–55) — no new defects
  found in the changed regions.
- Occlusion audit: `tools/venv/bin/python occlusion_audit.py --selftest`
  OK (all 6 planted classes fired, clean controls silent); final run on
  the edition dir: 0 flags, exit 0
  (output: `hidden_files/w45/it-core/occlusion.json`, refreshed).
- Builder scratch proof record refreshed: `hidden_files/w45/it-core/proof-text.txt`
  re-extracted from the current SVGs (1531 lines) so the next proofreader
  does not audit the stale pre-rebuild text.
- Tight-but-clean spots carried over unchanged: P4-main flow ends y=1079
  (bottom 1080); P6-ex ends y=2569 (bottom 2580); P7 col3 ends y=1673
  (rule 1686); P2-feature now ends y=1519 (bottom 1540, 21 px clear).
- Changed nothing else: no new articles, no new facts, no lead/image/credit
  changes (ABSTRACT.txt excepted per fix 6). No git push, no Discord post,
  no messages sent.
