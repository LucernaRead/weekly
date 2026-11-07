# Proof record — W45 PT core (VOL.2), builder self-proofread

## Round 1 (build 1 → occlusion1.json, text-p1..p8 v1)
- Build warnings: 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Occlusion audit: 7 flags, all adjudicated TRUE defects and fixed in source:
  P1 LINEX (word note crossed by separator), P1 BOXTITLE (+7.5px), P2 TEXTX (13h30 label),
  P6 TEXTX ×3 (caption/bar, caption/label, source/row), P7 BOXTITLE (+1px).
- Golden-quote program check: one quote hit 3 occurrences (P3 sentence-building answer
  duplicated a quote) → answer key changed to “Finados é um dia de silêncio.” → 2 each.
- p8.py extract: 150/150 noted. Naive regex 154 explained (150 answers + 4 match lefts).
- Full text read P1–P5, clean after checks.

## Round 2 (build 2 → occlusion2.json, 0 flags)
- Rebuild after geometry fixes: 0 warnings; occlusion 0; quotes 2 each; p8 150/150.
- Full text read P6, P7, P8 completed. Defects found and fixed:
  1. P4 “Na semana passada, o domingo 1º” → “Ontem, domingo 1º” (dated Monday issue).
  2. P5 “E depois da prova? … na terça, 3” chronology → “E a semana tem mais: …”.
  3. P7 B1 verb-class muddle (-ir/-er label on -ar verbs) → “E o modelo é simples: …”.
  4. P8 Lucas passage “uma hora antes” → “duas horas antes” (11h vs 13h close);
     dialogue note “投票点” → “考场分区”.

## Round 3 (final build → occlusion3.json)
- Rebuild after the 4 text fixes: 0 warnings; occlusion 0 flags; same-baseline rowcheck 0 flags;
  quotes 8×2; p8 extract 150/150; exercise numbering 1–150 continuous;
  distribution 10/18/18/18/18/18/12/38; levels A2 49 / B1 70 / B2 31; model 93 words.
- Visual inspection of all 8 cards (p1–p8 PNGs): no overflow, no overlap, no footer intrusion,
  photo + caption clean, charts legible, P7 golden block clear of preview box,
  P8 answer block ends well above the footer.
- Print PDF 15,957,851 B; web PDF 3,274,988 B.

## Status
Builder self-proofread: ZERO problems on the final full pass.
Independent (second-reader) proofread per SOP §7 is NOT done by this build — it is owed
by the main line before shipping. Do not claim the SOP independent gate as passed.
