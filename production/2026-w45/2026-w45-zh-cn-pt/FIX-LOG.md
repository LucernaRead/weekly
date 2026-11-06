# FIX LOG — W45 zh-cn × pt, Gate 10 (B-1) consolidation

Fix agent task: fold the five fix-round edits (which lived only in this
PT build copy) into the standalone transform
`hidden_files/w45-zh-cn-pt-transform.py`, so transform-alone reproduces
the delivered edition 8/8. The paper itself is NOT changed: re-rendered
SVGs/cards/PDFs must be byte-identical to the delivered files below.
This log was written BEFORE any transform edit. A full independent
reproof follows; this log does NOT declare finalization.

## Pre-flight (coordinator ruling: no concurrent writer)

- (a) No live process writing to the delivery dir, this build dir, or
  the transform file at task start (only live worker was a sibling
  zh-cn-nl reproof touching NL dirs only; at snap2, no PT process).
- (b) Two mtime snapshots a few minutes apart: SNAP2-IDENTICAL, zero
  changes (snap1/snap2 in hidden_files/w45/zh-cn-pt-fix/work/).
- (c) Proof session completed: hidden_files/w45/zh-cn-pt-proof/REPORT.md
  filed (verdict NOT PASS, single blocking item B-1, Gate 10 5/8).

## Pre-fix delivered-file hashes (SHA-256, recorded before any change)

=== SVG ===
f1dedefaa88a25d885c731bf941188d4ea9c0ebd2d97aefd058beb1625455a00  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p1-touiban.svg
c45889e4ec04c3376d1db4cadf2b6a71b181d907060d18f496e707cf3610f28d  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p2-shenghuo.svg
d8ac8e615fae57675d6409880a0c1f09c4284d8bd8b060f3e103a3be9b5c5fe3  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p3-wenhua.svg
9cd1c55337cfaa670ddb21de5082c122778e5a905f61a67e22dbfbc5a5e153eb  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p4-tiyu.svg
1aa87a544f297c85bbcee3043a513e4ea7588a2167283a08cc5fff9017053d90  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p5-qingnian.svg
3a8e2d85faa18581c960e5dd9f72be661b01719013b09c0d869af5d3961dc60b  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p6-shendu.svg
601d531d68647f16b344bfa6b55851f6762a185b9ef600527835a1374684c780  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p7-ciyu.svg
fe519c7b61b3f92218f5a8eef2775d6f4913e8e28dea65b5690b048dda0c2e2e  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p8-ceyan.svg
=== CARDS ===
d5e9a0915874816ca9d3a1f6361799f4dc037842e944315581f1721a02cc589b  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p1-touiban.png
563d1e0f9d23a02a8f8befc5e0a6f5ffc76eaf1297aee17298500c47848f8245  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p2-shenghuo.png
32b22c31533ff80e1876e9425398400ba18be02a906846c98dcd527c79d883d8  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p3-wenhua.png
03b5a0fdf70cb33d1644d187552b7cf053bfd5d728d083e5e36ec0198129fc2b  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p4-tiyu.png
bf24d347e6b7504538bcc74f2f9c14259d00de11ee48430f2198ec9ad126f026  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p5-qingnian.png
0304a9a6b6a8f048641beb17fd415db896ba2a839ef533c5dbd13241b063b875  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p6-shendu.png
2b9daf4ce42dbf37d423d98c32a8f568595757a5f3d296d22030cf896ffae3d4  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p7-ciyu.png
603b3a437b6742768a01b90eb270e31d249d739a96b3b3aca4d3358e4c578267  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p8-ceyan.png
=== PDFs ===
0bc2e29083679ec6ce1acaeb27371174b6e4b95e97a560488a3968aba50500aa  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/Lucerna-VOL2-PT-web.pdf
4190684793377b7ac853df3f190e048637323162f9dada01d74d23c613329872  /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/Lucerna-VOL2-PT.pdf
-rw-rw---- 1 root nogroup  3252004 Oct 28 07:31 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/Lucerna-VOL2-PT-web.pdf
-rw-rw---- 1 root nogroup 47047752 Oct 28 07:31 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/Lucerna-VOL2-PT.pdf
-rw-rw---- 1 root nogroup  1150759 Oct 28 07:29 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p1-touiban.png
-rw-rw---- 1 root nogroup  1153978 Oct 28 07:29 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p2-shenghuo.png
-rw-rw---- 1 root nogroup  1009763 Oct 28 07:29 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p3-wenhua.png
-rw-rw---- 1 root nogroup   951849 Oct 28 07:29 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p4-tiyu.png
-rw-rw---- 1 root nogroup   925752 Oct 28 07:29 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p5-qingnian.png
-rw-rw---- 1 root nogroup   836732 Oct 28 07:29 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p6-shendu.png
-rw-rw---- 1 root nogroup   738374 Oct 28 07:30 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p7-ciyu.png
-rw-rw---- 1 root nogroup  1087157 Oct 28 07:30 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/cards/p8-ceyan.png
-rw-rw---- 1 root nogroup   782634 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p1-touiban.svg
-rw-rw---- 1 root nogroup  1174685 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p2-shenghuo.svg
-rw-rw---- 1 root nogroup  2125474 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p3-wenhua.svg
-rw-rw---- 1 root nogroup   804720 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p4-tiyu.svg
-rw-rw---- 1 root nogroup  1059572 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p5-qingnian.svg
-rw-rw---- 1 root nogroup    26075 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p6-shendu.svg
-rw-rw---- 1 root nogroup    26810 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p7-ciyu.svg
-rw-rw---- 1 root nogroup    58531 Oct 28 07:28 /home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg/p8-ceyan.svg

Transform pre-fix SHA-256 (copy saved at hidden_files/w45/zh-cn-pt-fix/work/transform-pre-fix.py):
3e5e0f34a080179aefec98379d22bba5b95c8e513a4b1bcf604bf10c3a587b41  /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45-zh-cn-pt-transform.py

## Folded edits (19 changes to the transform, exact literals only)

Source-diff evidence: proof transform-solo output (repro-build) vs this
PT build copy differed ONLY in the lines below (plus OUT repointing
lines, which are not content). No extra edits were found, so nothing
was folded blindly. Direction verified against the DELIVERED files:
delivered = new, transform output = old. Method: muse.edit exact
unique literals; no AST byte-offset splicing, no repr literals
(tools README #17/#18). 17 existing pairs had their NEW side changed
to the delivered wording; 2 missing pairs were added.

- 12 shortened P8 notes (fix round 1; P8 notes derive from the exercise
  registry, so the edits sit in the exercise sources):
  JD.com 12 Oct: "As vendas imediatas da JD.com começaram em 12 de
  outubro." -> "Vendas imediatas da JD.com: 12 de outubro." (global
  pair; 3 occurrences in content12, all changed);
  Taobao/Tmall pre-sales 15 Oct -> "Pré-vendas do Taobao e do Tmall:
  15 de outubro."; Taobao/Tmall spot sales 20 Oct -> "Vendas
  imediatas do Taobao e do Tmall: 20 de outubro."; final -> "A final:
  15 de novembro, 03:00, hora de Pequim." (content34 + content8 pairs);
  24-25 Oct screenings -> "24–25 de outubro: média de 2 espectadores
  por sessão."; "「最低价」 é uma afirmação de propaganda, não um
  dado medido." -> "「最低价」 é propaganda, não dado medido.";
  "Primeiro os dados e a página de checkout; a manchete por último."
  -> "Dados e checkout primeiro; a manchete por último."; "As
  mercadorias imediatas despacham sem espera de sinal." ->
  "Mercadorias imediatas: sem espera de sinal."; Journalists Day ->
  "Dia dos Jornalistas: 8 de novembro, não 7."; "shùzì — os
  personagens do filme de IA são imagens digitais." -> "shùzì —
  personagens digitais no filme de IA."; "As mercadorias imediatas
  despacham na hora, sem espera de pré-venda." -> "Mercadorias
  imediatas: despacham na hora."; "A regra da página 6: dados
  primeiro, propaganda por último." -> "Regra da página 6: dados
  primeiro."
- 3 comma restructurings (fix round 3, keys 14/84/142):
  key 14 "Depois do 立冬, o tempo fica mais frio dia a dia." -> "O
  tempo fica mais frio dia a dia depois do 立冬.";
  key 84 "Com o 直降, o preço do checkout é o que você paga." ->
  "Com o 直降 o preço do checkout é o que você paga.";
  key 142 "No 立冬, ela fez bolinhos com a mãe." -> "No 立冬 ela
  fez bolinhos com a mãe."
- P4 feature gloss (fix round 4 one-off, ADDED pair): English gloss
  "tǎotài 淘汰 — to knock out, to eliminate · nèizhàn 内战 — a match
  between two teams from the same region · zhǐbù 止步 — to stop here,
  to go no further." -> Portuguese gloss "tǎotài 淘汰 — eliminar,
  tirar do torneio · nèizhàn 内战 — um jogo entre dois times da mesma
  região · zhǐbù 止步 — parar aqui, não ir adiante."
- P5 head (fix round 2): "Horários e números" -> "Datas e horas".
- P5 credit (fix round 4, ADDED pair, post-global "Foto: " form):
  "Foto: Based5290 — Public domain (Wikimedia Commons)" -> "Foto:
  Based5290 — Domínio público (Wikimedia Commons)".
- P6 head (fix round 2): "Contas das cestas" -> "Cálculos".

Transform post-fix SHA-256:
2e9e5d482636ab3b8f9ee8613aee1fdd74c270ed8153b0f5850bb43acea8982e  /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45-zh-cn-pt-transform.py

## Gate 10 self-run (fresh core copy + fixed standalone transform alone)

- Transform copy (only BUILD repointed to the fresh core copy): exit
  code 0, "TOTAL replacements: 538" (536 + the 2 added pairs).
- One-process driver run.py: exit code 0, registry TOTAL 150
  (A2 56 / B1 69 / B2 25; pages 10/18/18/18/18/18/12/38; types Complete
  a frase 68 / Escolha múltipla 50 / Associação 20 / Escolha no
  contexto 11 / Escrita 1), HEAD TOO WIDE 0, FLOW OVERFLOW 0.
- Re-rendered SVGs vs delivered SVGs: 8/8 BYTE-IDENTICAL.
- Post-transform sources vs this PT build copy: identical except the
  OUT repointing lines (5 files) — the fold is complete and exact.
- PT-build-copy rerun (cross-check): also 8/8 byte-identical,
  0 warnings, TOTAL 150.

## Re-render / hash verification (paper unchanged)

- Scratch render from the Gate 10 SVGs: cards 8/8 byte-identical to
  delivered; print PDF byte-identical (47,047,752 B, sha
  4190684793377b7ac853df3f190e048637323162f9dada01d74d23c613329872).
- Web PDF was NOT regenerated in place: delivered file keeps sha
  0bc2e29083679ec6ce1acaeb27371174b6e4b95e97a560488a3968aba50500aa.
  Scratch web PDF is the same size (3,252,004 B, 8 pages) and differs
  in exactly 6 bytes, all inside PIL CreationDate/ModDate timestamps
  (delivered 20261028073114Z vs regen 20261028081014Z) — the known
  timestamp artifact, not a content difference.
- Delivered SVGs/cards/PDFs re-hashed after this fix: identical to
  the pre-fix hashes above. No paper content, furniture, or
  ABSTRACT.txt was changed.

## Mechanical gates re-run on the re-render

- Occlusion audit: selftest OK (all 6 planted classes fire, clean
  controls silent); edition 0 flags; core 0 flags; NEW vs core 0.
- p8.py compare: CLEAN — core 150 noted, edition 150 noted,
  missing=[] extra_count=0 uncertain=[] keydiff=[].
- Gloss counts: 10 calls, per-call [4, 4, 4, 3, 3, 3, 3, 3, 3, 3],
  total 33 — exactly equal to the core.
- Registry: TOTAL 150, 0 warnings (see Gate 10 run above).

## Scratch

All fix work (snapshots, pre-fix transform copy, source diff, Gate 10
build/out/logs, PT-build rerun, render scratch) under
hidden_files/w45/zh-cn-pt-fix/work/. This fix does NOT declare
finalization — a full independent reproof follows.
