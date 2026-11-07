# WEEKLY-KIT — Lucerna 简体中文周报 VOL.2 × 荷兰语讲解版 (W45 zh-cn × nl)

## Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model).
  Issue number: VOL.2, the second Simplified Chinese issue.
- **Pairing:** zh-cn × nl — Simplified Chinese body text with a Dutch
  explanation layer, the edition for Dutch-speaking readers. Slug:
  `2026-w45-zh-cn-nl`.
- **Masthead:** bare `Lucerna` in blackletter (UnifrakturMaguntia). Chinese
  is article-less per the SOP, so there is no article.
- **Format:** 8 pages (a multiple of 4), 1950×2700 px, 4 columns, warm
  ivory paper `#f7f1e2`, deep olive accents. A2→B2 ramp; every exercise
  individually level-badged. One unified numbering sequence, 1–150, no
  gaps or duplicates; P8 answer keys generated from the exercise registry.
- **Native Simplified Chinese, NOT a Traditional edition:** the target text
  is the W45 zh-cn core's Simplified Chinese, frozen (see freeze diff
  below). Nothing was converted between scripts; this edition is not a
  Traditional edition and contains no Traditional-target text.
- **Status:** builder self-check complete (see "Builder's proof log"
  below). This is a builder handoff, NOT a finalisation claim —
  independent proofreading is still owed by the coordinator. No Discord
  delivery, no main-chat card/PDF delivery, no cron, no repo push, no
  `weekly-git` touch, no `insert.py` run was done by this builder.

## Contents, page by page (inherited from the core; only the explanation layer changed)

| Page | Section | Level | Exercises | Content |
|---|---|---|---|---|
| 1 | 头版 Top story (A2) | A2 | 10 (1–10) | Lead: Double 11 still running × Start of Winter on Saturday. This-week calendar box, contents, word of the week 「立冬」, parcel-locker photo, briefs, quick quiz. |
| 2 | 生活 Life (A2) | A2 15 / B1 3 | 18 (11–28) | Double 11 shopping life + Start-of-Winter life. Practice example (sweater 240 + scarf 80 = 320, direct cut 50 → payable 270). Shopping word cards 现货 / 直降 / 立减 / 补冬. Autumn-valley photo. |
| 3 | 文化 Culture (A2→B1) | A2 15 / B1 3 | 18 (29–46) | Start of Winter feature (19th solar term, 17:52 moment, three micro-seasons, regional food differences, Journalists' Day paragraph). Frost + dumpling photos. |
| 4 | 体育 Sport (B1) | B1 | 18 (47–64) | S16 feature (AL out, IG/TES/BLG chasing the quarter-finals, Swiss format, fourth-round preview, 2026-10-27 cutoff stated on the page, final Beijing 2026-11-15 03:00). LAN-party file photo. |
| 5 | 青年 Youth (B1) | A2 1 / B1 17 | 18 (65–82) | AI film 《三星堆：未来往事》 + Start-of-Winter new film 《我们仅有一次的人生》. Popcorn photo. |
| 6 | 深读 Deep read (B2) | B2 | 18 (83–100) | Double 11 deep read (why the rules got simpler; "lowest price" claims checked against checkout page, delivery cost, returns rules). Practice-data bar chart only. |
| 7 | 词语精讲 Language focus (A2/B1/B2 columns + error clinic + sentence frame + readers' corner + phrases + VOL.3 teaser) | A2 4 / B1 4 / B2 4 | 12 (101–112) | A2 shopping/winter words; B1 time-and-date order (big → small); B2 reading news (说法 / 数据 / 广告); error clinic (的/地/得, measure-word order, date order); frame 先…再…; readers' corner (see below); 8 phrases; VOL.3 teaser. |
| 8 | 测验与答案 Test & keys | A2 11 / B1 24 / B2 3 | 38 (113–150) | A true/false (8) + B big quiz (10) + C complete-the-sentence (10) + D read-and-answer passage about Xiao Hong in Beijing (6) + E in-conversation (3) + F writing (1). Then all 150 answer keys with brief Dutch notes, grouped by page with "— Pagina N —" headers for pages 1–8. Writing topic 《我的立冬周末》, 120–180 characters; model answer programmatically counted at 172 characters. |

## Measured totals

- **Exercises: 150 total** — A2 56 · B1 69 · B2 25. By page: 10 / 18 / 18 /
  18 / 18 / 18 / 12 / 38. By type: 完成句子 (fill in) 68 · 单选 (choose) 50 ·
  词语配对 (matching) 20 · 完形单选 (cloze choose) 11 · 写作 (writing) 1.
  All identical to the core registry (single-process driver output).
- **P6 practice chart** (cols 0–2): rows A 毛衣+围巾 270 yuan, B 耳机
  179 yuan, C 书+本子 160 yuan; bars drawn from zero at exactly 3.0 px per
  yuan, i.e. widths 810 / 537 / 480 px, starting at x = 325, verified in
  the edition SVG rects. Row-label ink right edges 203.8 / 142.6 / 180.2
  (all < 325 bar start); value labels start at bar end + 16 px. Chart note
  in Dutch: "De balken zijn vanaf 0 getekend (3 px = 1 yuan). Alleen
  oefendata — geen echte winkelprijzen."
- **Files:** 8 SVGs in `svg/`, 8 full-page PNG cards at 1950×2700 in
  `cards/`, print PDF `Lucerna-VOL2-NL.pdf` (47,427,799 bytes, 8 pages,
  sha256 `1be5629f53595f761d8648d365a200b19e16266f850ed7c580b2dfab2ccfe1cc`),
  web PDF `Lucerna-VOL2-NL-web.pdf` (3,208,683 bytes, 8 pages, JPEG pages
  q85 @1400 px — under the 10 MB Discord ceiling, though this builder
  does not deliver via Discord; sha256
  `6b0c0a2582fb8f6cd0483de5a6e3c409122be8048b928f9ecd300ca9ff99a9fd`).
- **Phrases of the week (P7):** 8 phrases, each verbatim from this issue's
  own articles and each occurring exactly twice in the final SVGs
  (punctuation-stripped count, article + P7): 「不用等11月11日」 p. 1;
  「下单就能发货」 p. 2; 「先看结算页,再付款」 p. 2; 「水开始结冰」 p. 3;
  「三场都输了」 p. 4; 「小局一场没赢」 p. 4; 「故事够不够好」 p. 5;
  「别以后,就现在」 p. 5.
- **Dutch number notation:** Dutch prose uses the Dutch decimal comma
  (e.g. "1,192 miljoen yuan" for the Maoyan 1.192-million-yuan figure,
  "17.52 u." for 17:52). Printed data, keys and arithmetic keep the core
  form (270, 179, 160, 240 + 80 = 320 − 50 = 270). Notation only; no
  number was changed.

## Trend and fact sources

Inherited wholesale from the W45 zh-cn core — no new fact was introduced
by this fan-out (only the explanation language changed). See the core
KIT (`files/weekly-report-w45-zhcn-core/WEEKLY-KIT.md`, "Trend and fact
sources"): Double 11 buildup (JD spot sales from 20:00 2026-10-12;
Taobao/Tmall presale 20:00 2026-10-15, tail-payment + spot sales 20:00
2026-10-20, spot period to 23:59 2026-11-13; peak sale 20:00 2026-11-10
mentioned only as next week's event; WeChat shop first Double 11,
2026-10-12 to 2026-11-15, 35 days); Start of Winter Saturday 2026-11-07,
17:52交节 (Beijing time), 19th solar term, three micro-seasons; S16 with
the honestly dated 2026-10-27 cutoff (AL 0–3 out; IG/TES/BLG 2–1; GEN/DK
3–0 through; fourth round 2026-10-29–31; quarter-finals 2026-11-04–07;
semi-finals 2026-11-08–09; final Beijing 2026-11-15 03:00); films
《三星堆：未来往事》 (released 2026-10-23, 100 minutes, Maoyan 4-day
≈1.192 million yuan at noon 2026-10-26) and 《我们仅有一次的人生》
(nationwide release Saturday 2026-11-07, 114 minutes); Journalists' Day
Sunday 2026-11-08. No international politics, no Chinese domestic
politics (target country is China). The core's honesty limits carry over
unchanged (P4 has no score chart — final Swiss scores were not knowable
at the 2026-10-27 cutoff; all basket maths is labelled practice data).

## W43 promises: how each was handled (inherited from the core)

The core's P7 readers' corner and VOL.3 teaser are carried over with the
disclosure re-written in Dutch (see "Readers' corner" below). VOL.3
promises printed in this issue (P7 teaser, Chinese text frozen):
"双11当天11月11日星期三，包裹到了吗？S16淘汰赛打完了，谁进了决赛？
总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。下周
见！"

## Readers' corner (P7, Dutch disclosure — mandatory invitation included)

Inherited disclosure, translated: the corner prints the labelled editor's
example letter (Chinese letter frozen; Chinese disclosure sentence
frozen: 编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)
刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的
投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。) plus the Dutch
disclosure: "Redactie: VOL.1 beloofde echte brieven in VOL.2. Die zijn er
nog niet, dus een voorbeeldbrief. Uitgesteld, niet afgesteld — stuur ons
je eigen brief in het Chinees!" — i.e. (a) on-page disclosure that no
genuine reader letters exist (labelled editor's example + deferral) AND
(b) an EXPLICIT open invitation for real letters in Dutch. No reader,
letter, name or quotation was invented.

## Image authorisations

6 photos, all CC0 / public domain, credit taken directly from the Commons
API Artist field (core build `assets/CREDITS.md`, verified 2026-10-27).
Placement and image-element counts in the final SVGs: P1 1, P2 1, P3 2,
P4 1, P5 1, P6 0, P7 0, P8 0 — 6 photos total, and every embedded payload
is byte-identical to the core's (MD5-verified per page: locker, valley,
frost, dumplings, lanparty, popcorn — all match). Only the credit label
was translated (Photo: → Foto:; Public domain → Publiek domein);
authors and licences unchanged. File photos are captioned 资料图 and
never presented as this week's event.

## Furniture three-way (core EN · W43 shipped same-pairing · this edition)

W43 shipped same-pairing edition (per `tools/tables.py edition-dir zh-cn
nl`): `files/weekly-report-zh-cn-nl/` (VOL.1; the task brief's
`weekly-report-zhcn-nl` spelling does not exist on disk). All strings
below verified from the shipped W43 SVGs, never from memory.

| Item | Core (zh-cn × en, VOL.2) | W43 shipped (zh-cn × nl, VOL.1) | This edition (VOL.2) |
|---|---|---|---|
| P1 pairing badge | 简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers (975, 434; 19.5pt; OLIVE #3e4c2a) | TEKSTEN IN HET CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS (975, 434; 19.5pt; BRICK #a4553a) | Same string as W43, same slot/size/fill (975, 434; 19.5pt; weight 700; BRICK #a4553a) |
| Footer (every page) | Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations | Lucerna · CHINEES WEEKBLAD VOL.1 · TEKSTEN IN HET CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS | Lucerna · CHINEES WEEKBLAD VOL.2 · TEKSTEN IN HET CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS (VOL.2 per this issue) |
| Page line | 第 N 版 / 共 8 版 | Pagina N van 8 | Pagina N van 8 (8/8 pages verified) |
| Gloss prefix | Notes｜ | Uitleg — | Uitleg — (10 gloss boxes, one per gloss() call) |
| P8 separators | — Page N — | — Pagina N — | — Pagina N — (1–8 all present) |
| P8 answer style | `{n}. {key} — {note}`; writing `{n}. ✓ {note}` (dash style, verified from the core's shipped P8 SVG and content8.py answer-generation code, which was left byte-identical) | same dash style | same dash style (code untouched) |

**Badge slot/size case (applies here):** in-place replacement at the
zh-cn core family's own badge slot. The zh-cn core carries its pairing
badge at (975, 434), 19.5pt — the y=372 line is the frozen bilingual
strapline (给学中文的人的周报 — …), not a free slot — so this edition
replaces the core badge in place at the same coordinates, size and
weight, following the shipped W43 zh-cn-nl precedent exactly (string +
BRICK fill). This is NOT the EN/DE/ES subtitle-slot case (badge at
y≈372) and NOT the FR/IT inserted-badge case (y=574, 22pt); neither
family's slot was applied. The y=372 strapline keeps its frozen Chinese
half and takes the W43 Dutch half: "给学中文的人的周报 — Lees het echte
China, in het Chinees"; the y=92 top strip likewise takes the W43 Dutch
half: "每周读中文 · Lees echt Chinees, elke week". The P1 edition line
(简体中文版 · VOL.2 · 双11 · 立冬 · S16) stays in Chinese, per the W43
precedent of keeping the core's Chinese edition line.

**Other Dutch furniture (W43 wording reused where the element recurs):**
section heads 头条 · Hoofdverhaal / 生活 · Dagelijks leven / 文化 ·
Cultuur / 体育 · Sport / 青年 · Jeugd / 深读 · Diep gelezen / 词语 ·
Taal in de kijker / 测验与答案 · Toets en antwoorden; bylines "Redactie
Lucerna · Leesniveau …"; band subs "Niveau …"; 练习 · Oefeningen;
"Antwoorden op pagina 8 · 答案见第 8 版"; heads Lees en kies / Vul het
woord in / Cijfers en data / Combineer; instr Vul in / Combineer;
说说你自己 · En jij?; 你知道吗 · Wist je dat?; 购物词语卡 ·
Winkelwoorden; 节日小日历 · Feestdata; 体育小日历 · Sportdata;
电影小日历 · Filmdata; 这一周的高频词 · Weekwoorden; 深读要点 ·
Kernpunten; 读新闻三问 · Drie vragen; 易错诊所 · Foutenkliniek;
本周句式 · Zinspatroon; 读者园地 · Lezershoek; 本周金句 · Zinnen van
de week (letterlijk, uit de artikelen van dit nummer); 下期预告 ·
Volgende week (VOL.3); P8 heads Waar of onwaar / De grote quiz / Maak
de zinnen af / Lees en antwoord / In gesprek / Schrijven; keys header
"答案 · Antwoorden — per pagina, met een toelichting bij elk antwoord"
+ "Alle toelichtingen in het Nederlands · ✓ = de schrijfopdracht".

## P8 note style verification (family style, from code — not memory)

The core's P8 answer-generation code (content8.py keys loop) prints
`{n}. {key} — {note}` and, for the writing item, `{n}. ✓ {note}` — the
dash style (tools/README note #8's dash-style family includes the
zh-cn core's fan-out precedent: W43 zh-cn-nl KIT §6 confirms the same
form, and the shipped W45 core P8 SVG shows it). The answer-generation
code was left byte-identical; only registry note strings (and the
writing item's key/note, per the W43 precedent) were translated:
- Writing key: "(开放题，范文如下)" → "(open vraag — voorbeeldtekst
  hieronder)"; note: "Open task - the model answer is printed in
  section F above (172 characters)" → "Open vraag — de voorbeeldtekst
  staat hierboven in deel F, 172 tekens" (trimmed in the fix round to
  "Open vraag — voorbeeldtekst hierboven in deel F, 172 tekens" — facts
  and key unchanged); "Model answer: " → "Voorbeeldtekst: ". The
  172-character model answer text itself is frozen Chinese.
- All other 149 keys are byte-identical to the core (registry-level);
  `tools/p8.py compare` printed-note set: **CLEAN, 150 = 150,
  missing = [], extra = 0, keydiff = []**.

## Builder's proof log (self-check, final render)

- **Pre-flight duplicate check:** at start, the edition build dir
  (`hidden_files/weekly-report-w45-zh-cn-nl-build/`) and delivery dir
  (`files/weekly-report-w45-zh-cn-nl/`) did not exist; no live worker
  was writing to them (only an unrelated `insert.py` for fr-ru was
  running). No stand-down was needed.
- **Baseline (STEP 1):** core build copied to the edition build dir,
  OUT repointed to the edition dir, `tools/freeze.py baseline` run
  BEFORE any change: **8/8 SVGs byte-identical** to the shipped core,
  core SVGs re-hashed unchanged afterwards. Core SVG hashes recorded in
  the build dir (`core-svg-hashes-before.txt`); final re-check
  `sha256sum -c`: 8/8 OK.
- **Transform:** explanation layer EN → NL via exact-literal
  replacements (`scratch/transform_nl.py`, asserted: every source string
  found ≥1× and 0× after; one repoint miss caught by grep — render.py
  BASE had no `/svg` suffix — fixed and re-verified zero `zhcn-core`
  references remain in the edition build). Content modules were never
  imported inside the core build dir and never run standalone; all
  renders went through the single one-process driver (`run.py`).
- **Freeze diff (strict-CJK):** `tools/freeze.py diff --strict-cjk`:
  p1–p8 added CJK characters **0 on every page, TOTAL 0**. CJK net
  decreases per page (p1 −31, p2 −22, p3 −22, p4 −21, p5 −23, p6 −22,
  p7 −21, p8 −20) are all explanation-layer deletions (EN badge/footer
  Chinese strings replaced by Dutch; the writing key's Chinese
  instruction replaced by Dutch). No added CJK item needed adjudication
  (added = 0, so no citation list arises). No new target text: every
  added/removed string pair is explanation-layer churn; the Simplified
  Chinese target text is zero-diff by construction (same source lines).
- **Gloss count (split on `·` itself):** 10 gloss() calls, counts equal
  item by item vs the core (4/4/4/3/3/3/3/3/3/3 in call order;
  `scratch/gloss_count.py`, MISMATCHES: 0).
- **P8 gate:** `tools/p8.py compare`: **CLEAN** (see above).
- **Occlusion audit:** `tools/occlusion_audit.py` selftest OK (all 6
  planted classes fire, clean controls silent); edition audit **0
  flags**; with `--core`: core 0 flags, **NEW vs core: 0**.
- **Same-baseline ink-collision scan** (furniture-band class the
  canonical audit does not cover; `scratch/rowcheck.py`, PIL true-ink
  boxes with the tables.json font table, SC face index 2): **0 flags**
  across all 8 pages, including the P1 top strip.
- **P6 chart-label element check:** bars 810/537/480 px from x = 325 at
  3.0 px/yuan (core geometry preserved); label ink right edges
  203.8/142.6/180.2 < 325; value labels at bar end + 16 px; no
  label/bar/text overlap (audit 0 flags corroborates).
- **Driver warnings (final render):** **zero** `FLOW OVERFLOW` / `HEAD TOO
  WIDE` warnings. Registry: TOTAL 150, levels A2 56 / B1 69 / B2 25, by
  page 10/18/18/18/18/18/12/38, writing model 172 characters — all
  identical to the core.
- **P7 geometry:** col3 ends 1708.1, teaser ends 2554.1 — identical to
  the core's values, above the 2580 footer line.
- **Kinsoku line-start scan:** 0 suspects (no text node starts with a
  true closing punctuation mark). Traditional-only characters: 0.
  English-residue scan over all rendered text nodes (marker phrases +
  function-word grep): 0 real hits (remaining hits are Dutch homographs:
  is/in/was/film/team/stage).
- **Reproducibility:** `tools/freeze.py baseline` re-run against the
  finished edition build with the delivered SVGs as reference: **8/8
  byte-identical** (independent copy + repoint + re-render reproduces
  the delivered files exactly).
- **Visual check:** all 8 final cards read in full by the builder — no
  overflow, overlap, footer intrusion, or missing element found. P8's
  keys flow ends mid-column-4, well above the footer; P7's teaser sits
  above the footer line; P6's chart labels sit clear of the bars.

## Fix rounds during this build (pre-fix baselines)

Three defects in the first render, all fixed in source and fully
re-rendered (never patched in output):

1. **P7 teaser off-page (first render):** Dutch readers'-corner
   disclosure + clinic notes + frame text ran +226 px long (col3 end
   1934.2 vs core 1708.1), pushing the VOL.3 teaser rect to end at
   2780.2 — past the 2700 page bottom and across the footer band.
   Fix: compressed the Dutch clinic notes to core line counts
   (3 lines saved), the frame text (1 line saved), and the readers'
   disclosure to exactly the core's 10 wrapped lines (4 lines saved;
   wording kept the mandatory disclosure + explicit invitation, see
   above). Result: col3 ends 1708.1, teaser ends 2554.1 — identical to
   the core.
2. **P6 exercise head too wide (first render):** "C · 练习篮子算一算 ·
   Reken met de mandjes" measured 542.4 px > 434 px column width (HEAD
   TOO WIDE). Fix: head shortened to "C · 练习篮子算一算 · Reken mee"
   (399.1 px). The glossline "Reken met de oefenmandjes." was kept.
3. **P8 keys overflow (first two renders):** Dutch notes ran to 165
   wrapped key lines vs the core's fit, overflowing the keys flow
   (col 3 y = 2531, need 31, bottom 2540). Fix (`scratch/trim_notes.py`):
   14 note wordings compressed telegram-style (facts and keys
   unchanged), bringing key lines to 151; the trim script's assertion
   caught one miss on the first attempt (the #150 note uses the
   `{NCHARS}` placeholder, not literal "172") and refused to write
   until corrected — no partial trim was ever rendered. Result: zero
   overflow warnings, keys end mid-column-4.
   Two missed English notes found by a registry scan during this round
   and fixed at the same time: #135 ("shùzì — the AI film's characters
   are digital images." → "shùzì — AI-filmpersonages zijn digitaal.")
   and #140 ("lìjiǎn — taken off at checkout." → "lìjiǎn —
   afgetrokken bij het afrekenen."). A post-trim registry re-scan
   found no further English notes.

## Adjudications and shortfalls (for the independent proofreader)

- **P4 has no score chart:** inherited from the core, deliberate (final
  Swiss scores were not knowable at the 2026-10-27 cutoff).
- **6 photos vs W43's 9:** inherited from the core (P6 chart page and
  the two text pages carry no photo, as in the W43 pattern).
- **B2 share is 25 of 150:** inherited from the core (ramp is A2-heavy
  by design for this target).
- **P8 top rule proximity:** inherited from the core (test flow ends
  below the keys rule at y = 1264; the canonical audit reports no flag;
  visually checked on the final P8 card: clean).
- **"Swiss stage" kept in Dutch prose:** Dutch esports coverage uses
  "Swiss stage" as the stage name; the Dutch notes therefore say "de
  Swiss stage" rather than a calque ("Zwitserse ronde"). The P1
  calendar note and P4 standings note use the same term consistently.
- **"Peking" for Beijing:** Dutch notes use "Pekingtijd" / "woont in
  Peking" (standard Dutch exonym), matching the W43 NL precedent
  ("Pekingtijd").
- **Dutch decimal comma:** see "Measured totals" — notation only.

## Reproduction

Build code lives in
`hidden_files/weekly-report-w45-zh-cn-nl-build/` (bslib4.py, svglib.py,
run.py, render.py, content12.py, content34.py, content56.py, content7.py,
content8.py, assets/, scratch/transform_nl.py, scratch/trim_notes.py,
scratch/fix_p6p7.py, scratch/gloss_count.py, scratch/rowcheck.py,
scratch/dump_reg.py).
Content modules run only through the single one-process driver; never
run a module standalone and never import one inside a core build
directory (their module-level code executes on import and their OUT
paths point at a shipped edition directory — in this copy, OUT points
at `files/weekly-report-w45-zh-cn-nl/svg`).

```bash
cd hidden_files/weekly-report-w45-zh-cn-nl-build
../../tools/venv/bin/python run.py        # single-process driver
../../tools/venv/bin/python render.py     # svg -> cards PNG -> print + web PDF
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zh-cn-nl
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zh-cn-nl --core ../files/weekly-report-w45-zhcn-core
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-zhcn-core --edition-dir ../files/weekly-report-w45-zh-cn-nl --target zh-cn
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-zhcn-core/svg --edition-svg ../files/weekly-report-w45-zh-cn-nl/svg --strict-cjk
```

(Use `tools/venv/bin/python` — never the ephemeral `/tmp/wp-venv`.)

## Toolchain versions (recorded from the actual run)

- Interpreter: `tools/venv/bin/python` — Python 3.12.3 (GCC 13.3.0).
- PIL (Pillow) 13.0.0; CairoSVG 2.9.1; pypdf (via render.py) for PDF merge.
- Canonical tools: `tools/freeze.py` (baseline + diff), `tools/p8.py`
  (compare), `tools/occlusion_audit.py` (selftest + audit + --core).
- Scratch outputs (tool JSONs): `tools/scratch/baseline-w45-zhcn-nl/`,
  `tools/scratch/diff-w45-zhcn-nl.json`,
  `tools/scratch/occlusion-w45-zhcn-nl.json`,
  `tools/scratch/repro-w45-zhcn-nl/`; build scratch: transform, trim,
  gloss-count, rowcheck and registry-dump scripts + `reg-nl.json`
  (post-trim registry re-dump was not re-run; the delivered P8 SVG is
  the authoritative post-trim record and `p8.py compare` CLEAN was run
  on it).

## Deliverables in this edition dir

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG), `Lucerna-VOL2-NL.pdf`
  (print, 8 pp), `Lucerna-VOL2-NL-web.pdf` (web, 8 pp, <10 MB),
  `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Dutch single line, no
  ASCII double quotes).

## Fix round (2026-10-28): Gate 10 script gap closed — NOT a finalisation claim

The independent proof (`hidden_files/w45/zh-cn-nl-proof/REPORT.md`) passed
every content/geometry gate but BLOCKED on Gate 10: a fresh core copy +
`transform_nl.py` alone reproduced only 5/8 SVGs (6/8 with `trim_notes.py`),
because two fix-round edits lived only as direct edits in the edition build
files. This round folded both edits into a script; no page content,
furniture, or `ABSTRACT.txt` was changed, and a full independent reproof
still follows (this section is a fix record, not finalisation).

- **Pre-flight:** no live worker on the nl dirs; two mtime snapshots
  07:40:58Z and 07:45:03Z showed zero changes; the proof session had completed.
- **Pre-fix baselines** (recorded before any re-render; full hashes in the
  build dir fix log `scratch/fix-round-log.md`): SVGs p1 `a020b7ed…`,
  p2 `325a2c2c…`, p3 `43a9d3b4…`, p4 `ef1a3ef9…`, p5 `dc47775f…`,
  p6 `9dc5ca46…`, p7 `19cd38d2…`, p8 `574203a2…`; print PDF 47,427,799 bytes
  `1be5629f…`; web PDF 3,208,683 bytes `6b0c0a25…`.
- **New script:** `scratch/fix_p6p7.py` (asserted-literal, tools README #17:
  each old literal exactly 1×, 0× after, new exactly 1× after; no AST
  splicing, no repr literals). Apply ONLY to a fresh core copy AFTER
  `transform_nl.py` (+ `trim_notes.py`; trim/fix order irrelevant).
  Six pairs, located by file-level diff of a transform+trim copy vs the
  delivered build (not from the proof's paraphrase — the proof's list quotes
  only two clinic notes, but the diff shows a third, which is included):
  (1) P6 head `C · 练习篮子算一算 · Reken met de mandjes` →
  `C · 练习篮子算一算 · Reken mee`; (2) P7 clinic 地 `…markeert hoe een
  handeling wordt gedaan.` → `…markeert de manier van handelen.`;
  (3) P7 clinic 得 `…verbindt een werkwoord met een graadcomplement:
  跑得快.` → `…: werkwoord + graad, bijv. 跑得快.`; (4) P7 clinic date
  order `Tijden gaan van groot naar klein: de weekdag het laatst.` →
  `Tijden: groot → klein, weekdag het laatst.`; (5) P7 frame
  `…(Controleer eerst de beoordelingen, bestel daarna.) Het patroon
  先…再… geeft de volgorde van handelingen. …` → `…(Eerst beoordelingen
  checken, dan bestellen.) 先…再… geeft de volgorde aan. …`;
  (6) P7 disclosure Dutch half (frozen Chinese prefix untouched) from the
  long version ending `…publiceren wij graag in een volgend nummer!` to
  `Redactie: VOL.1 beloofde echte brieven in VOL.2. Die zijn er nog niet,
  dus een voorbeeldbrief. Uitgesteld, niet afgesteld — stuur ons je eigen
  brief in het Chinees!` (disclosure + explicit invitation kept).
- **Post-fix byte-identity:** re-render via the single one-process driver
  (`run.py`, exit 0, 0 warnings, registry TOTAL 150, A2 56 / B1 69 / B2 25)
  produced SVGs 8/8 BYTE-IDENTICAL to pre-fix; cards 8/8 byte-identical;
  both PDFs unchanged in size AND SHA; `ABSTRACT.txt` unchanged.
  Scratch regen from post-fix SVGs: cards 8/8 identical, print PDF
  byte-identical, web PDF same size with only PIL timestamp bytes differing.
- **Gate re-runs:** occlusion selftest OK, edition 0 flags, `--core` NEW 0;
  `p8.py compare` CLEAN (150 = 150, keydiff = []); gloss counts match item
  by item (MISMATCHES: 0).
- **Gate 10 re-run:** full chain transform → trim → fix → `freeze.py
  baseline` = **8/8 SVGs byte-identical**. Transform + fix WITHOUT trim =
  7/8 (only P8 differs — the untrimmed P8 — because P8 trims live in the
  separate `trim_notes.py`); any re-run must include `trim_notes.py`.
- **Residual, not folded:** `render.py` BASE was hand-repointed from the
  core dir to the edition dir (the transform OUT pair needs the `/svg`
  suffix, which `render.py` BASE lacks). It does not affect SVG
  reproduction (freeze does not use `render.py`); recorded here for the
  coordinator. Toolchain this round: `tools/venv/bin/python` Python 3.12.3,
  PIL 13.0.0, CairoSVG 2.9.1.
