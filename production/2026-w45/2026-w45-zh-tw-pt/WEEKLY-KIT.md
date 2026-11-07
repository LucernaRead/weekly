# WEEKLY-KIT — 2026-w45-zh-tw-pt

**BUILT (NOT finalized).** Traditional Chinese target · Portuguese reader.
Issue week Nov 2–8, 2026 · VOL.2 · 8 pages, 1950×2700 · slug `2026-w45-zh-tw-pt`.
An independent proofread follows; only a zero-problem proof finalizes this edition.

- Delivery dir: `files/weekly-report-w45-zh-tw-pt/` (svg/ + cards/ + PDFs + this KIT + ABSTRACT.txt)
- Build dir: `hidden_files/weekly-report-w45-zh-tw-pt-build/`
- Transform (single source of every fix): `hidden_files/weekly-report-w45-zh-tw-pt-transform.py`
- Checks dir: `hidden_files/w45-zh-tw-pt-checks/` (checks.py, checks.json, dump_reg.py,
  reg-pt.json, reg-core.json, diff.json, occlusion*.json, render logs, gate10 logs)
- Gate 10 temp dir: `hidden_files/w45-zh-tw-pt-gate10/` (removed after each run by fresh_copy)

## 1. Core and topics

Built from the W45 zh-tw core (`files/weekly-report-w45-zhtw-core/`, KIT read first;
its counts — NOT the zh-cn core's split — are authoritative).
Pairing zh-tw × en in the core; masthead `Lucerna` (no article — Chinese is article-less);
edition line every page: `繁體中文版 · VOL.2 · 2026年11月2日(一)至11月8日(日) · 台灣 / 香港`;
strapline: `金融科技週 · 台北旅展 · 味全龍封王——本週台港最熱的三件事`.

Topics: Hong Kong FinTech Week x StartmeupHK 2026 (Nov 2–6); 2026 ITF Taiwan
International Travel Fair (Nov 6–9); CPBL Taiwan Series 2026, Wei Chuan Dragons beat
CTBC Brothers 4–2, Game 6 Oct 26 at Taipei Dome 6–0; Lidong Nov 7; Kaohsiung
International Steel Sculpture Festival (Oct 23–Nov 22); Fulong Sand Sculpture Festival
closing Oct 26; Tianmu Halloween Oct 25–26; Double 11 preview (Nov 11, future only).

## 2. Exercise registry (== core, verified by dump diff)

TOTAL **150** — A2 44 · B1 74 · B2 32.
By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
By type: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1.
Writing model 138 characters (band 120–180).
Registry dump diff (one-process runs of the content modules in my build dir and in the
freeze-baseline copy): page/level/type diffs = []; key diffs = exactly the #150
apparatus item (core `(開放題,範文如下)` → PT `(pergunta aberta — modelo abaixo)`);
PT notes: 0 English-word suspects, 0 identical to core (all 150 translated).

## 3. Baseline

`tools/freeze.py baseline` against the W45 zh-tw core build: **8/8 byte-identical**
before any change. Core shipped SVGs re-hashed unchanged afterwards. The core build dir
itself was never executed (read-only reference); all renders ran in my build dir.

## 4. Freeze diff (final delivered SVGs, `--strict-cjk`)

| page | + strings | − strings | CJK core → edition | added CJK |
|------|-----------|-----------|--------------------|-----------|
| p1 | 25 | 22 | 952 → 920 | 0 |
| p2 | 38 | 35 | 1018 → 996 | 0 |
| p3 | 43 | 38 | 1088 → 1065 | 0 |
| p4 | 36 | 33 | 831 → 809 | 0 |
| p5 | 44 | 40 | 1101 → 1079 | 0 |
| p6 | 42 | 37 | 942 → 921 | 0 |
| p7 | 95 | 87 | 808 → 788 | 0 |
| p8 | 196 | 187 | 1114 → 1019 | 0 |
| TOTAL | | | | **0** |

Target Traditional Chinese text: ZERO difference from the zh-tw core at run level
(strict-CJK added = 0 on all pages; every added string is Portuguese explanation).

## 5. Traditional-independence cross-check (HARD GATE — PASS)

Method: extract the CJK character set from the shipped SVG text nodes of each file
(no conversion tool, no character table of my own — the ru-zh-tw lesson: a builder's
own table missed 郵→郵). Edition set vs UNION of (W43 zh-tw-pt shipped SVG text) and
(W45 zh-tw core SVG text), extracted from those shipped files themselves.

- Core set: 782 chars · W43 zh-tw-pt set: 798 chars · union: 1040 chars.
- Edition set: 780 chars · **outside union: 0**.
- Edition chars not in core but in W43-pt: 0 (the edition's CJK set is a subset of the
  core's own set).
- No Simplified-only character in target text. No Simplified→Traditional conversion,
  no OpenCC, no own mapping table was used anywhere. PASS.

## 6. Three-way furniture table (core · W43 zh-tw-pt · this edition)

Measured from the shipped files, not assumed from the zh-cn family.

| element | W45 zh-tw core | W43 zh-tw-pt | this edition |
|---------|----------------|--------------|--------------|
| P1 badge slot | x=975 y=378, 21pt, weight 700, centred, fill `#3e4c2a` (OLIVE) | SAME slot x=975 y=378, 21pt, 700, centred, fill `#a4553a` (BRICK) | SAME slot/size/centred, **BRICK `#a4553a`** |
| P1 badge text | `繁體中文版 · VOL.2 · …` (edition line) | PT badge per tables.json | tables.json PT verbatim: `TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA` (ink 1274.4 of the 1820 slot) |
| Footer | EN footer | PT footer | `Lucerna · SEMANÁRIO CHINÊS TRADICIONAL VOL.2 · TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS` (1135.9 at 20pt regular; right page line clear) |
| Page line | `第 {n} 頁` | `Página {n} de {total}` | `Página {n} de {total}` |
| Gloss prefix | `Notes｜` (bslib4 `gloss()`) | `Nota — ` | `Nota — ` |
| P8 key style | dash `N. key — note`, 12.8/1.12, gap=1 | **paren `N. key (note)`** (that family's shipped build code, line 118: `f"{e_['n']}. {e_['key']} ({e_['note']})"`) | paren `N. key (note)`, core font/lh/gap kept; key lines bypass svglib `_fw` pair conversion, restored after the keys flow (bypass RETAINED after the fix round — see §13; now strictly unnecessary for paren safety but still correct and content-neutral) |
| P8 separators | `— 第 {pg} 頁 —` | `— Página {pg} —` | `— Página {pg} —` |
| P8 noted set | 150/150 | 150/150 | 150/150 (p8.py CLEAN, see §7) |

Portuguese conventions (Brazilian, following the W43 zh-tw-pt KIT §5): thousands
separator `.` (1.600, 45.000, 4.100); currency NT$ prefix with space (`NT$ 2.400`);
ordinals `1.º` / `8.ª`; Duplo 11; Trilhas Verdes; Taipé (not Taipéi); Esporte;
Foco linguístico; Leitura a fundo; Cantinho do leitor; section heads per W43 pt
precedent (A `Verdadeiro ou falso`, B `O grande quiz`, C `Complete as frases`,
D `Leia e responda`, E `Diga no contexto`, F `Redação`; `Entendeu?`, `Faça as contas`,
`Leia o gráfico`). Match instructions: content12 word↔definition →
`Associe palavra e definição`; content34 in file order P3 → `Associe palavra e definição`,
P4 term↔info → `Associe nome e informação`; content56 word↔definition →
`Associe palavra e definição`.

## 7. Gates (all GREEN on the final delivered SVGs)

- Freeze baseline: 8/8 byte-identical (§3).
- Freeze diff `--strict-cjk`: added CJK = 0 on all 8 pages (§4).
- `p8.py compare`: **CLEAN**, core 150 noted = edition 150 noted, missing=[],
  extra_count=0, uncertain=[], **keydiff=[]**; `p8.py extract` = 150 of 150.
- Occlusion audit: selftest OK (all 6 planted classes fired, clean controls silent);
  edition **0 flags**; core 0 flags; **NEW vs core: 0** (final run, occlusion2.json).
- Same-baseline ink-collision scan (all pages, PIL TC face): **0**.
- P6/P4 chart-label element check (text ink vs later-drawn rects): **0** on both chart
  pages. (First run of the check script reported 2408 false overlaps because
  `overlap()` returns a tuple that is always truthy; fixed to test `overlap(...)[0] > 0`
  and re-ran.)
- Gloss boxes: **12 = 12** (core `gloss()` calls: content12 4, content34 5, content56 3;
  all 12 strings replaced 1:1 in the transform).
- Registry: 150, levels/pages/types exactly as core (§2).
- Render warnings (final driver log, exit 0): **0 FLOW OVERFLOW / HEAD TOO WIDE /
  TOO WIDE**; P7 col3 ends 1745.36, P7 teaser ends 2543.36, P8 keys end y=2328
  (bottom 2540; was 2314 before the fix round — the longer pinyin notes reflow
  the keys block +14px, still 212px clear of the bottom; see §13).
- P7 golden sentences: all 8 inner texts at exactly 2 occurrences each (article page +
  P7), tags correct: p. 1, p. 1, p. 2, p. 3, p. 3, p. 4, p. 5, p. 6 — identical to core.
  (First check-script run counted the bracketed form and reported 1; corrected to
  inner-text count, since P7 prints the quote bracketed and the article prints it bare.)
- Images: embedded payloads byte-identical to core on every page
  (P1 `ac4dfe2ad3a4`, P2 `a40e7a2b265b`, P4 `18ad8ae06fac`, P5 `bcbada13a5ae`,
  truncated SHA-256 prefixes as printed by the check script; P3/P6/P7/P8 no photos).
  Printed credits byte-identical:
  P1 `Photo: Wilfredor — CC0 (Wikimedia Commons)`,
  P2 `Photo: CorraleH — CC0 (Wikimedia Commons)`,
  P4 `Photo: Bain News Service — Public domain (Wikimedia Commons)`,
  P5 `Photo: Benjamin Balazs — CC0 (Wikimedia Commons)`.
  P4 chart bars 120.0/600.0 px; P6 bars 600.0/800.0/800.0/800.0 px (as core).
- Readers' corner: frozen Traditional disclosure intact in the edition; PT disclosure
  present (states no genuine letters arrived + open invitation — see §9 for the
  shortened wording).
- All 8 cards (1950×2700 PNG) eyeballed clean: no overflow, overlap, footer collision,
  or image/credit misplacement on any page.

## 8. Residual-Latin adjudication (full-render sweep, not just added strings)

Two scans of ALL rendered text nodes (the freeze-diff added-strings scan alone would
have missed unchanged English strings — see the P3 catch below):

1. Every bilingual `CHINESE · LATIN` node: exactly ONE English head remained after the
   first build — `算一算 · Work it out` (P3, content34). All other Latin segments are
   Portuguese, frozen proper names/terms (SOLID TIDES, JUMP, VOL.2), option letters,
   or Chinese-led stems. Fixed in the transform (§9); re-scan: 0.
2. English-word blacklist scan of every node: 17 hits, adjudicated one by one —
   `fintech/FinTech` (7 hits: the loanword used in Portuguese press + the event's
   official English theme name `Fintech Nexus: Bridging the World, Building the Future`,
   frozen inside a Chinese sentence); `Photo:` credits (4, frozen Commons credits
   verbatim); `some/Some` (2 hits: the Portuguese verb somar — `some esse custo`,
   `Some as taxas` — not English); `Work it out` (1, the real miss, fixed).
   Remaining English-word suspects after the fix: **0** (plus the adjudicated
   loanword/credit items above).

AI-variant trap (known): the P6 gloss `Three plus signs: Finance+... AI+...` and the
SEPARATE content8 note `AI inside finance is 人工智慧＋.` were translated independently;
the latter → `IA dentro das finanças é réngōng zhìnéng＋.` — visible on P8 as key 138
(fix round §13: the Han citation became tone-marked pinyin; the ＋ is kept, as in
the P6 gloss's `IA+` concept).

## 9. Transform-first record — every fix-layer edit lives in the transform

Transform pair counts: BSLIB 3, C12 52, C34 60, C56 62, C7 49, C8 53 = **279**.
Reconciliation vs the es sibling map (288): the 9 difference is es-internal chained
pairs (4: `讀懂了嗎? · ¿Lo has entendido?` ×3 files + `深讀測驗 · Cuestionario…`)
and es-own C7 texts (5: band title, disclosure, grammar note, memory trick, lh line) —
none is a core string my edition lacks. Verified mechanically by OLD-string set
comparison per file.

Fixes folded into the transform as made:

- **P3 算一算 head (caught by the full-render residual-Latin sweep, §8):**
  `算一算 · Work it out` → `算一算 · Faça as contas` (content34, count 1).
  Root cause of the miss: the sibling inventory extraction (taken from the es
  transform) had missed this C34 tail pair — the es file gained it only in a late
  `Two heads missed in v1` addition after my extraction. Lesson: the sweep of the
  RENDERED output is the backstop, not the inventory. Same sweep also confirmed
  the P4 word-card title miss (below). Flag for the coordinator: sibling W45 zh-tw
  editions built from the same inventory may share the P3 miss if they did not run
  a rendered-output sweep.
- **Extra pair vs both sibling maps:** `棒球詞卡 · Baseball words` →
  `棒球詞卡 · Palavras` (measured 327.9 at 34pt bold, inside CW 434; the fuller
  `Palavras do beisebol` measured 528.9 and would spill into the next column).
  Present as English residue in both the es and it sibling renders at check time.
- **Measured head shortenings (wording, never geometry):**
  `標題填空 · Palavras dos títulos` (391.9 at 26pt, fits);
  `深讀測驗 · Quiz a fundo` (326.0 at 28pt, fits); P7 heads at 24pt all fit
  (390.3 / 416.2 / 413.1 < 434); P8 heads at 21pt all fit.
- **P2 box fix (wording):** the fuller PT question wrapped to 3 lines and its last
  line crossed the fixed 230px `你呢?` box border (audit BOXTITLE, +8.7px). Shortened
  to `Que panela quente você comeria no Lidong? E no seu carrinho do Duplo 11?` =
  2 wrap lines, same as English.
- **P7 disclosure fix (wording):** the fuller PT disclosure wrapped to 7 lines vs
  English 6, last line +5.9px over the readers'-corner box border. Shortened to:
  `Carta de exemplo da redação, não uma carta real. Aviso: o VOL.1 prometeu cartas
  reais e a melhor redação da página 8 desde esta edição; até o fechamento nenhuma
  publicável chegou, por isso o exemplo fica e o convite continua aberto.` = 6 wrap
  lines, same as English. It still states no genuine letters arrived and the
  invitation stays open.
- **P7 readers'-corner gap fix — DELIBERATE DEVIATION, for the proofreader to judge
  (interior-only geometry correction, wording alone provably cannot fix it):**
  after the disclosure shortening, the audit still flagged the last line (+10.7px)
  even though box and baselines were byte-identical to the core. Root cause proven:
  the core's `lh` formula underestimates this box by ~11px — core box y=1184.86
  h=560.5 (audit box bottom 1746.1) and core last-line baseline 1751.63 are identical
  in the core render, whose last line is ALSO struck through by the border on the
  card crop; the core escapes the audit only because its last line's ink CENTRE sits
  0.15px outside the box (1746.25 vs border 1746.1), while the PT line's centre
  (1745.75) falls inside. Wording shortening provably cannot fix it: `lh` is computed
  from the same `wrap()` line count, so one fewer line shrinks the box 29px while the
  text rises only 28.4px (gap ~11px at every line count, verified). Fix in transform
  (`apply7_fix`): the two `+ 10` inter-para gaps after the frozen letter (`lt`) and
  frozen disclosure (`lt2`) paras in content7.py become `+ 0`, moving only that box's
  interior text up 20px inside the UNCHANGED box; `col3_end`, phrases rule, and teaser
  positions do not move (teaser text y=2509.36, same as core; teaser ends 2543.36).
  Post-fix crop viewed: last line fully inside the box with clear space below.
  Sibling context (not a justification): W45 zh-tw-es/it/fr/de each report 0 flags vs
  core — their disclosures escape the same box issue by audit technicalities (e.g.
  IT's last-line centre also falls inside the box geometry but its element-index
  distance exceeds the tool's 80-element window).

## 10. Gate 10 — transform-solo re-render (PASS, final run)

Fresh core copy + the transform script ALONE, one-process driver, then byte-compare
against the delivered SVGs:

- **GATE10: 8/8 byte-identical, warnings=0, exit code 0** (gate10c.log).
- History (kept for auditability): the first gate10 attempt crashed at the comparison
  step (FileNotFoundError) because the es template's gate10 repoint spliced the
  absolute temp dir inside the `~/workspace/...` prefix, writing SVGs to a nested junk
  path `goals/.../home/hatch/.../gate10/svg` (8 files, all 8 pages rendered fine).
  Fixed in MY transform (whole-`expanduser(...)` replacement), the junk tree was
  removed, and no junk path was recreated (verified). The es template's gate10 has
  this latent bug; it is NOT copied here. A second gate10 run read 7/8 because the
  intervening rebuild had run the transform but not the driver before render.py —
  the driver was then run, and the final gate10 run is 8/8. (The earlier
  `GATE10 EXIT: 0` line was `tail`'s exit code through a pipe, not the transform's —
  never treated as a pass.)

## 11. Deliverables and pins

SVG SHA-256 (final):

- p1-front.svg `3d8481de100e9787dce9beffc4f64ed196df8f3f671a29a7023f792675b10a94`
- p2-life.svg `99bcb003f2c4161af63bee1db143d8b03d8df5329c1ac58daa7d876c676b97c2`
- p3-culture.svg `aac1e5fc867795b4b9db53298791026f9714f9e739645f4b738f655ecfd7cdf9`
- p4-sport.svg `cbf88009a967b1ad28cfa1f9b0524ad8f7603ce62bc7b54433dc9afc5c2f9ab6`
- p5-youth.svg `23b7ad0b3b43cdc85a1ad20fa7893adeeab8803ba77e5744226433edf8e2731d`
- p6-deep.svg `2012bf23a67baf1cb2d5492ad0f849244ed41bafa01341d75ea5c9450943184e`
- p7-lang.svg `32799b27dad4ea22af5ddb2b6906904bfc10aea8e78e05d28cb0b632a19c56fd`
- p8-test.svg `236b96ae89ed8529cd8cbb03c7049fb9e23d0b3eef7c0abbc1885bd5925a30b0` (fix round §13; p1–p7 hashes unchanged)

PDF pins (8 pages each, regenerated from the final SVGs):

- Print `Lucerna-VOL2-PT.pdf`: **20,845,651 bytes**,
  SHA-256 `fc85e26f31aa89e92ab0b550af2e8f23e2cff27fc308d4f8808e0369f005d85c` (fix round §13; supersedes the pre-fix pin 20,848,230 B / `18f7ca8f…`)
- Web `Lucerna-VOL2-PT-web.pdf`: **3,510,596 bytes (< 10 MB)**,
  SHA-256 `380e91d19a69082d68ff407762622119ce1e3305a67c3cd0006cbefb8e0c9b0e` (fix round §13; supersedes the pre-fix pin 3,507,192 B / `ca73db6b…`)

Cards: 8 PNGs 1950×2700 in `cards/`, all eyeballed clean (§7).

## 12. Non-blocking notes (separate from the gates)

- The P7 gap fix (§9) is a deliberate interior-geometry deviation from the core, not
  a wording change; the proofreader should judge it visually (post-fix crop: last
  line fully inside the box). Everything else in the edition follows core geometry.
- The es sibling transform's gate10 repoint has the nested-junk-path bug described
  in §10; sibling builders using that template should fix it the same way.
- The P3 `算一算 · Work it out` miss came from a stale sibling-inventory extraction;
  sibling editions built from the same inventory should run the rendered-output
  residual-Latin sweep (§8) before shipping.
- No repo insert, no Discord post, no main-chat card/PDF dump, no cron, no subagent,
  no shared-scratch cleanup was done by this build, per the task iron rules.
  The core build dir and the core delivery dir were not modified.

## 13. Fix round — B-1 pinyin discipline (independent proof NOT PASS → fixed, NOT finalized)

The independent proofread (hidden_files/w45/zh-tw-pt-proof/REPORT.md) returned
NOT PASS on exactly one item, B-1: 32/150 P8 notes cited Chinese terms in Han
characters, breaking the W43 zh-tw-pt column's pinyin discipline (W43 shipped P8
= 0 notes with Han; its KIT §7 and zero-problem proof §13). Everything else
across all 16 proof gates passed. This fix round changes ONLY those 32 note
strings, in the transform (hidden_files/weekly-report-w45-zh-tw-pt-transform.py,
still 279 pairs — verified by AST count and by a before/after diff showing
exactly those 32 NEW strings changed, OLD core strings untouched). No other
passing gate was reworked: badge, footer, gloss counts, golden sentences,
images, the P7 readers'-corner gap fix, and ABSTRACT.txt are untouched
(ABSTRACT.txt mtime still 2026-10-28 09:11, pre-fix).

Pre-flight (coordinator ruling, intent = NO CONCURRENT WRITER): (a) no live
worker writing to the delivery/build dirs — the one process seen mid-check was
insert.py for a different edition (zh-tw-ru → weekly-git), never touching these
dirs, and it had exited by the second snapshot; (b) two mtime snapshots of both
dirs ~4 minutes apart (09:27 vs 09:31) showed ZERO changes; (c) the proof
session had completed (last delivery write 09:11). PROCEED.

Key-vs-note check (done per item from the proof's registry dump): in the 12
items whose KEY is itself a Han term (17, 35, 55, 101, 103, 105, 110, 112, 132,
133, 134, 138), the converted Han was in the NOTE PROSE — a repetition of the
key — not the key itself. NO item was left untouched on key grounds: all 32
notes were converted, and every key is verified unchanged (registry diff vs
the pre-fix edition: exactly 32 note changes, 0 key changes, 0 page/level/type
changes). Han citations elsewhere in the paper (article/lesson prose, e.g. the
P4 "Quatro palavras" gloss and the P7 lesson paragraphs) are NOT P8 notes and
were deliberately left alone — B-1's scope is the P8 answer block only.

### 13.1 Conversion table (item → old Han citation in note → new pinyin form)

Pinyin convention: tone-marked pinyin per W43 zh-tw-pt KIT §7 (lexical words
joined, phrases spaced by word — e.g. W43 `fēng wáng`, `shūyùn`, `mǎn qiān
sòng bǎi`). "W43 precedent" below means the same PT sentence (or the same
term's pinyin form) occurs in the W43 zh-tw-pt shipped build; all other forms
are standard tone-marked pinyin.

| item | old Han citation | new pinyin form | W43 precedent |
|------|------------------|-----------------|---------------|
| 17 | 進補 | jìnbǔ | form per proof remedy example |
| 25 | 立冬 | lìdōng | — (standard) |
| 26 | 進補 | jìnbǔ | form per proof remedy example |
| 27 | 泡湯 | pàotāng | — (standard) |
| 28 | 集章 | jízhāng | — (standard) |
| 35 | 節氣 (in parens) | jiéqì (in parens) | form per proof remedy example |
| 43 | 立冬 | lìdōng | — (standard) |
| 44 | 進補 | jìnbǔ | form per proof remedy example |
| 45 | 鋼雕 | gāngdiāo | — (standard) |
| 46 | 沙雕 | shādiāo | — (standard) |
| 55 | 封王 | fēng wáng | YES — W43 content34: `Conquistar o título é fēng wáng.` verbatim |
| 61 | 完封 | wánfēng | — (standard) |
| 62 | 封王 | fēng wáng | YES — W43 `fēng wáng` form |
| 63 | 全壘打 | quánlěidǎ | — (standard) |
| 64 | 安打 | āndǎ | — (standard) |
| 79 | 討糖 | tǎotáng | YES — W43 content7: `Tǎotáng é …` joined form |
| 80 | 踩街 | cǎijiē | — (standard) |
| 81 | 南瓜桶 | nánguā tǒng | — (standard) |
| 82 | 打卡 | dǎkǎ | — (standard) |
| 101 | 攤位 | tānwèi | — (standard) |
| 103 | 集章 | jízhāng | — (standard) |
| 105 | 封王 | fēng wáng | YES — same sentence as W43 (see 55) |
| 106 | 完封 | wánfēng | — (standard) |
| 109 | 打卡 | dǎkǎ | — (standard) |
| 110 | 討糖 | tǎotáng | YES — W43 joined `tǎotáng` form |
| 111 | 踩街 | cǎijiē | — (standard) |
| 112 | 泡湯 | pàotāng | — (standard) |
| 132 | 封王 | fēng wáng | YES — same sentence as W43 (see 55) |
| 133 | 討糖 | tǎotáng | YES — W43 joined `tǎotáng` form |
| 134 | 集章 | jízhāng | — (standard) |
| 138 | 人工智慧＋ | réngōng zhìnéng＋ | NO W43 precedent exists — see §13.2 |
| 149 | 先比價，再結帳 | xiān bǐjià, zài jiézhàng | form per proof remedy example (full-width ， → ASCII comma) |

Full new notes (spot-checkable against the delivered P8): 17 `Uma refeição de
panela quente marca o Lidong: jìnbǔ.`; 35 `Lidong é um termo solar (jiéqì).`;
138 `IA dentro das finanças é réngōng zhìnéng＋.`; 149 `Compare os preços
primeiro e pague depois: xiān bǐjià, zài jiézhàng.` — the other 28 follow the
table mechanically (term replaced, rest of the note verbatim).

### 13.2 Item 138 — no W43 precedent (reported honestly)

The task brief asked to check W43 zh-tw-pt's P8-138 form for its 人工智慧＋
rendering. That precedent does not exist: a grep of the whole W43 zh-tw-pt
shipped build finds ZERO occurrences of 人工智慧, and W43's global item 138 is
a different exercise (`Os cupons são as pǐnwèi quàn (fichas de degustação).`).
Item 138 therefore follows the proof report's own remedy form
(`人工智慧＋ → réngōng zhìnéng＋`), with the ＋ KEPT: the plus is the concept
itself (the P6 gloss's independently translated `Finanças+ … IA+` theme — "três
sinais de mais"), and dropping it would change the meaning from "AI+" to plain
"AI". The ＋ is a symbol, not a Han character, and it does not trigger the
`_fw` pair conversion (which only full-widths parens enclosing CJK).

### 13.3 `_fw`-bypass disposition — RETAINED, verified correct

The keys-flow `_fw` bypass in content8.py (digit-led key lines returned
unchanged, `_fw` restored after the flow) was NOT deleted. After the conversion
no note contains CJK inside its parens, so the bypass is no longer strictly
necessary for paren safety — svglib `_fw` only full-widths a paren pair whose
enclosed text contains CJK, and keys themselves sit OUTSIDE the parens — but
the bypass remains correct and content-neutral: it returns exactly the key
lines unchanged, restores `_orig_fw` immediately after the flow, and no key
line carries CJK-adjacent punctuation that Chinese typesetting would need to
convert. Verified in the final render: answer-block full-width parens = 0
(wrap-aware reassembly of all 150 key items).

### 13.4 Full re-gate evidence (all on the final delivered SVGs/cards/PDFs)

- Render: one-process driver exit 0, **zero** FLOW OVERFLOW / HEAD TOO WIDE /
  TOO WIDE warnings; registry 150 (A2 44 / B1 74 / B2 32; pages
  10/18/18/18/18/18/12/38; types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 /
  寫作 1 — identical to core). P8 keys end y=2328 (bottom 2540); P7 col3
  1745.36 / teaser 2543.36 unmoved.
- SVG change scope: p1–p7 **byte-identical** to the pre-fix delivery (hashes in
  §11 unchanged); ONLY p8-test.svg changed, to
  `236b96ae89ed8529cd8cbb03c7049fb9e23d0b3eef7c0abbc1885bd5925a30b0`.
- Freeze diff `--strict-cjk`: added CJK = **0 on all 8 pages** (p8 strings
  196/187, CJK 1114 → 1019 — the drop from 1092 is exactly the converted Han
  citations; no target-text character changed). Freeze exit 0.
- `p8.py compare`: **CLEAN, core 150 noted = edition 150 noted, missing=[],
  extra_count=0, uncertain=[], keydiff=[]**.
- Wrap-aware P8 reassembly (proof method, re-run): 150/150 items, notes
  containing Han = **0**, answer-block full-width parens = **0**; all 12
  Han keys intact (17 進補, 35 節氣, 55/105/132 封王, 101 攤位, 103/134 集章,
  110/133 討糖, 112 泡湯, 138 人工智慧).
- Registry dump diff (fresh scratch copy, never the core build dir): exactly
  the 32 note changes above; 0 key changes; 0 notes with Han in the new
  registry.
- Gate 10 (fresh core copy + transform ALONE + one-process driver):
  **8/8 byte-identical, exit 0, zero warnings**.
- Occlusion audit: selftest OK (all 6 planted classes fired, clean controls
  silent); edition **0 flags**; core 0 flags; **NEW vs core: 0**.
- Residual-Latin sweep (rendered output): P3 `算一算 · Faça as contas` holds,
  `Work it out` **0** occurrences anywhere.
- Card eyeball, all 8 (1950×2700): no overflow, overlap, or footer collision
  on any page; P8 reflow clean (item 149 wraps over two lines inside its
  column; keys block ends well above the footer); P7 teaser still clear of
  the 2580 footer rule; P7 readers'-corner gap fix still verified by the
  unchanged P7 geometry (last-line ink bottom 1736.13 vs border 1745.36).
- PDFs re-rendered from the final SVGs (8 pages each): print
  `Lucerna-VOL2-PT.pdf` **20,845,651 bytes**,
  SHA-256 `fc85e26f31aa89e92ab0b550af2e8f23e2cff27fc308d4f8808e0369f005d85c`;
  web `Lucerna-VOL2-PT-web.pdf` **3,510,596 bytes (< 10 MB)**,
  SHA-256 `380e91d19a69082d68ff407762622119ce1e3305a67c3cd0006cbefb8e0c9b0e`.
- Fix work products: hidden_files/w45-zh-tw-pt-fix/ (pre-flight snapshots,
  pre-fix transform copy, apply/driver/gate10/render logs, freeze/p8/
  occlusion logs, reassembly JSON, new registry dump). The core build dir and
  core delivery dir were not modified; no repo insert, Discord post,
  main-chat dump, cron, subagent, or shared-scratch cleanup was done by this
  fix. **Status: FIXED, NOT finalized — a FULL reproof follows, and only a
  zero-problem reproof finalizes this edition.**
