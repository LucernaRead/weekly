# WEEKLY-KIT — Lucerna 简体中文周报 VOL.2 (W45) × Português

## 1. Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model:
  the cycle starting Monday 2026-10-26 produces the issue dated the following
  Monday). Issue number: VOL.2, the second Simplified Chinese issue.
- **Pairing:** zh-cn × pt — Simplified Chinese body text (frozen W45 core,
  `files/weekly-report-w45-zhcn-core/`) with ALL explanations rewritten in
  Portuguese for Portuguese-speaking readers. Fan-out per SOP: baseline
  reproduction first, explanation-layer rewrite only, target text untouched.
- **This is a Simplified Chinese TARGET edition.** The target text stays
  Simplified exactly as in the core. This is NOT a Traditional edition and
  nothing was converted between scripts. Strict-CJK gate: added CJK = 0 on
  all 8 pages (see §7).
- **Masthead:** bare `Lucerna` in blackletter (UnifrakturMaguntia). Chinese
  is article-less per the SOP, so there is no "The"/"Le" article.
- **Format:** 8 pages (a multiple of 4), 1950×2700 px, 4 columns, warm
  ivory paper `#f7f1e2`, deep olive accents. A2→B2 ramp; every exercise is
  individually level-badged. One unified numbering sequence, 1–150, with no
  gaps or duplicates; P8 answer keys are generated from the exercise
  registry.
- **Status:** builder self-check complete (see §8). This is a builder
  handoff, NOT a finalisation claim — independent proofreading is still
  owed by the parent line. No Discord delivery, no main-chat card/PDF
  delivery, no cron, no repo push, no `insert.py` run, no `weekly-git`
  touch was made by this builder.

## 2. Contents, page by page

| Page | Section | Level | Exercises | Content |
|---|---|---|---|---|
| 1 | 头版 Top story (A2) | A2 | 10 (1–10) | Lead: Double 11 still running × Start of Winter on Saturday. This-week calendar box, contents, word of the week 「立冬」, parcel-locker photo, briefs, quick quiz. PT: badge, strap, calendar, contents, quiz furniture all in Portuguese; Chinese text frozen. |
| 2 | 生活 Life (A2) | A2 15 / B1 3 | 18 (11–28) | Double 11 shopping life + Start-of-Winter life. Practice example (sweater 240 + scarf 80 = 320, direct cut 50 → payable 270). Shopping word cards 现货 / 直降 / 立减 / 补冬. Autumn-valley photo. |
| 3 | 文化 Culture (A2→B1) | A2 15 / B1 3 | 18 (29–46) | Start of Winter feature (19th solar term, 17:52 moment, three micro-seasons, regional food differences, uneven cooling, Journalists' Day paragraph). Frost + dumpling photos. Festival-dates box. |
| 4 | 体育 Sport (B1) | B1 | 18 (47–64) | S16 feature (AL out, IG/TES/BLG chasing the quarter-finals, Swiss format, fourth-round preview, 2026-10-27 cutoff stated on the page, final Beijing 2026-11-15 03:00). S16 schedule box (no score chart — final Swiss scores were not yet knowable). LAN-party file photo. Sports-dates box. Match-words box. |
| 5 | 青年 Youth (B1) | A2 1 / B1 17 | 18 (65–82) | AI film 《三星堆：未来往事》 + Start-of-Winter new film 《我们仅有一次的人生》. Popcorn photo. Film-dates box. |
| 6 | 深读 Deep read (B2) | B2 | 18 (83–100) | Double 11 deep read (why the rules got simpler; "lowest price" claims must be checked against the checkout page, delivery cost, and returns rules). Practice-data bar chart only. Key-points box. "Three questions for reading news" box. |
| 7 | 词语精讲 Language focus (A2/B1/B2 columns + error clinic + sentence frame + readers' corner + phrases + VOL.3 teaser) | A2 4 / B1 4 / B2 4 | 12 (101–112) | A2 shopping/winter words; B1 time-and-date order (big → small); B2 reading news (说法 / 数据 / 广告); error clinic (的/地/得, measure-word order, date order); frame 先…再…; readers' corner (labelled editor's example + on-page PT disclosure + EXPLICIT open invitation, see §5); 8 phrases; VOL.3 teaser. |
| 8 | 测验与答案 Test & keys | A2 11 / B1 24 / B2 3 | 38 (113–150) | A true/false (8) + B big quiz (10) + C complete-the-sentence (10) + D read-and-answer passage about Xiao Hong in Beijing (6) + E in-conversation (3) + F writing (1). Then all 150 answer keys with brief Portuguese notes, generated from the registry, grouped by page with "— Página N —" headers for pages 1–8. Writing topic 《我的立冬周末》, 120–180 characters; model answer programmatically counted at 172 characters. |

## 3. Measured totals

- **Exercises: 150 total** — A2 56 · B1 69 · B2 25. By page: 10 / 18 / 18 /
  18 / 18 / 18 / 12 / 38. Identical to the core.
- **By type (Portuguese registry names, VOL.1 PT column mapping):**
  Complete a frase 68 · Escolha múltipla 50 · Associação 20 ·
  Escolha no contexto 11 · Escrita 1. Counts identical to the core's
  完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1.
- **Writing model: 172 characters** (identical to core).
- **Gloss: 10 gloss() calls, 33 items** — counted by splitting the rendered
  gloss string on `·` itself (tools README note #21): per-call
  4/4/4/3/3/3/3/3/3/3, exactly equal to the core item by item.
- **Visible text** (concatenated `<text>` nodes of the final SVGs):
  24,500 characters without spaces / 28,431 characters with spaces
  (core: 23,038 / 26,765 — the increase is the Portuguese explanation
  layer, which runs longer than English; target text unchanged).
- **Phrases of the week (P7):** 8 phrases, each verbatim from this issue's
  own articles, with Portuguese translations and "(Página N)" references.
- **P6 practice chart** (cols 0–2, unchanged from core): rows A 毛衣+围巾
  270 yuan, B 耳机 179 yuan, C 书+本子 160 yuan; bars drawn from zero at
  exactly 3.0 px per yuan, i.e. widths 810 / 537 / 480 px, starting at
  x = 325, verified in the SVG rects. Chart note in Portuguese:
  "As barras partem de 0 (3 px = 1 yuan). Apenas dados de prática — não
  são preços reais de loja. As contas das cestas estão no artigo acima."
- **Files:** 8 SVGs in `svg/`, 8 full-page PNG cards at 1950×2700 in
  `cards/`, print PDF `Lucerna-VOL2-PT.pdf` (47,047,752 bytes, 8 pages),
  web PDF `Lucerna-VOL2-PT-web.pdf` (3,252,004 bytes, 8 pages, JPEG pages
  q85 @1400 px — under the 10 MB Discord ceiling, though this builder
  does not deliver via Discord).
  - Print PDF SHA-256:
    `4190684793377b7ac853df3f190e048637323162f9dada01d74d23c613329872`
  - Web PDF SHA-256:
    `0bc2e29083679ec6ce1acaeb27371174b6e4b95e97a560488a3968aba50500aa`
- **Images:** 6 photos, same files and placements as the core — P1 1, P2 1,
  P3 2, P4 1, P5 1, P6 0, P7 0, P8 0. Credits translated to the PT column
  form ("Foto: … — CC0 (Wikimedia Commons)"; Based5290:
  "Foto: Based5290 — Domínio público (Wikimedia Commons)").
  Authorisations: see the core KIT and
  `hidden_files/weekly-report-w45-zhcn-build/assets/CREDITS.md`
  (all CC0 / public domain, credit from the Commons API Artist field).

## 4. Furniture three-way (core EN vs W43 same-pairing PT vs this edition)

All PT strings below were verified against the SHIPPED W43 same-pairing
edition's SVGs (`files/weekly-report-zh-cn-pt/svg/`, VOL.1), never from
memory. VOL.2 differs from VOL.1 only in the volume number and the W45
topic words; every other furniture string is byte-identical to VOL.1.

| Item | W45 core (zh-cn × en) | W43 zh-cn × pt (VOL.1, shipped) | This edition (W45 zh-cn × pt, VOL.2) |
|---|---|---|---|
| Masthead | `Lucerna` (no article) | `Lucerna` (no article) | `Lucerna` (no article) |
| P1 subtitle (y=330) | `简体中文版 · VOL.2 · 双11 · 立冬 · S16` | `SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.1 · 双11 · 大闸蟹 · 霜降` | `SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16` |
| P1 strapline (y=372) | `给学中文的人的周报 — Read the real China, in Chinese` | `给学中文的人的周报 — Leia a China de verdade, em chinês` | `给学中文的人的周报 — Leia a China de verdade, em chinês` |
| P1 pairing badge (y=434, 19.5pt) | `简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers` | `TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA` | Same as VOL.1 PT, verbatim |
| P1 top strip centre | `每周读中文 · Read real Chinese, every week` | `每周读中文 · Leia chinês de verdade, toda semana` | Same as VOL.1 PT, verbatim |
| Footer (every page) | `Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations` | `Lucerna · SEMANÁRIO CHINÊS SIMPLIFICADO VOL.1 · TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS` | `Lucerna · SEMANÁRIO CHINÊS SIMPLIFICADO VOL.2 · TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS` |
| Page line | `第 N 版 / 共 8 版` | `Página N de 8` | `Página N de 8` |
| Gloss prefix (bslib4 gloss()) | `Notes｜` | `Nota — ` | `Nota — ` |
| P8 separators | `— Page N —` | `— Página N —` | `— Página N —` |
| P8 keys head | `答案 · Answer keys — by page, with a note on every answer` | `答案 · Gabarito — por página, com uma nota em cada resposta` | Same as VOL.1 PT, verbatim |
| P8 keys right line | `All notes in English · ✓ = the writing task` | `Todas as notas em português · ✓ = a tarefa de escrita` | Same as VOL.1 PT, verbatim |
| P8 answer-note style | **DASH**: `N. key — note`, writing `N. ✓ note` (verified from the core's shipped build code `content8.py`, not from memory) | PAREN (VOL.1 core's own style): `N. key (note)` | **DASH, kept from the W45 core family**: `N. key — note`, writing `N. ✓ note`. The VOL.1 paren form was NOT carried over — the family style follows the core being fanned out. |
| Section-head pattern | EN heads (`Read & choose`, `Word blanks`, …) | PT column (`Leia e escolha`, bare `Complete`, `Associação`, `Escreva`, …) | Same PT column forms as VOL.1 (incl. bare `Complete` for word-blank sections, `Associe as palavras` for matching instr, `Escreva` for writing instr) |

**Badge slot/size case (tools README note #20):** the zh-cn family carries
its own badge IN PLACE at y=434, 19.5pt, bold, centred — the W45 core
itself prints its badge there, and the shipped VOL.1 zh-cn×pt edition
uses exactly that slot and size. This edition follows that precedent
(it is NOT the EN×ZH-TW subtitle-slot case and NOT the FR/IT inserted-
at-y=574 case). No masthead element moved; body elements below y=606
are untouched.

## 5. Readers' corner (P7) — disclosure + invitation

The core's corner prints a labelled editor's example plus an on-page
deferral disclosure (VOL.1 promised real reader letters and the best
VOL.1 writing in VOL.2; none have arrived; "延期不是取消 / Deferred, not
cancelled"). This edition inherits that disclosure in content and
renders it in Portuguese, self-contained (the core's Chinese disclosure
sentence is replaced by the Portuguese text below, not silently
dropped — see §8, fix-round note on removed CJK):

> "Exemplo da redação — não é uma carta de verdade. O VOL.1 prometeu
> cartas verdadeiras dos leitores e o melhor texto do VOL.1 neste VOL.2;
> até agora nenhuma carta chegou e não há texto publicável, por isso
> este cantinho ainda traz um exemplo da redação. Adiado, não cancelado.
> Escreva-nos! Envie a sua carta em chinês — duas frases já bastam — e
> ela pode sair no próximo número."

This satisfies both proof requirements: (a) it discloses on-page that no
genuine reader letters exist (labelled editor's example, no fabrication
— the letter itself remains the frozen Chinese editor's example); (b)
it contains an EXPLICIT open invitation for real letters
("Escreva-nos! Envie a sua carta em chinês …"). The VOL.3 teaser line
and the P2/P3/P5/P6 "E você?" prompts are NOT relied on as the
invitation. The disclosure text measures exactly 10 wrapped lines at
sans 20pt, identical to the core's disclosure, so P7 col3 ends at
1708.1 and the teaser ends at 2554.1 — byte-identical geometry to the
core (see §8).

## 6. Trend and fact sources

Inherited wholesale from the core — no new facts were introduced by
this fan-out (explanation-layer translation only). The core KIT's
"Trend and fact sources" section is the authority: Double 11 buildup
(JD spot sales from 2026-10-12 20:00; Taobao/Tmall presale from
2026-10-15 20:00, tail-payment + spot sales from 2026-10-20 20:00, spot
period to 2026-11-13; peak sale 2026-11-10 20:00 as next week's event;
WeChat shop first Double 11, 2026-10-12 to 2026-11-15, 35 days; 18th
Double 11); Start of Winter Saturday 2026-11-07 17:52 (19th solar term,
three micro-seasons, regional customs, uneven cooling); S16 with the
2026-10-27 cutoff honestly stated (AL 0–3 out; IG/TES/BLG 2–1; GEN/DK
3–0 through; fourth round 2026-10-29–31; quarter-finals 2026-11-04–07
06:00; semi-finals 2026-11-08–09 06:00; final Beijing 2026-11-15 03:00);
films 《三星堆：未来往事》 (2026-10-23, 100 min, Maoyan 4-day
~1.192 million yuan at noon 2026-10-26) and 《我们仅有一次的人生》
(2026-11-07, 114 min); Journalists' Day Sunday 2026-11-08. No
international politics, no Chinese domestic politics, no anniversary
material (see the core KIT's "Explicitly rejected material").

## 7. Reproduction build

Build code lives in `hidden_files/weekly-report-w45-zh-cn-pt-build/`
(bslib4.py, svglib.py, run.py, render.py, content12.py, content34.py,
content56.py, content7.py, content8.py, assets/). Content modules run
only through the single one-process driver; never run a module
standalone and never import one inside a core build directory (their
module-level code executes on import and their OUT paths point at a
shipped edition directory). This build's OUT paths were repointed to
`files/weekly-report-w45-zh-cn-pt/svg` before any run; the core build
directory was never imported from and its shipped SVGs were re-hashed
unchanged after the baseline run.

```bash
cd hidden_files/weekly-report-w45-zh-cn-pt-build
../../tools/venv/bin/python run.py        # single-process driver
../../tools/venv/bin/python render.py     # svg -> cards PNG -> print + web PDF
cd ../../tools
./venv/bin/python freeze.py baseline --build ../hidden_files/weekly-report-w45-zhcn-build \
    --core-svg ../files/weekly-report-w45-zhcn-core/svg --out scratch/baseline-w45-zhcn
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-zhcn-core/svg \
    --edition-svg ../files/weekly-report-w45-zh-cn-pt/svg --strict-cjk
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-zhcn-core \
    --edition-dir ../files/weekly-report-w45-zh-cn-pt --target zh-cn
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zh-cn-pt \
    --core ../files/weekly-report-w45-zhcn-core
```

Transform record: `hidden_files/w45-zh-cn-pt-transform.py` (536
exact-literal replacements, each asserted ≥1 hit before writing; the
script is atomic — a failed assertion writes nothing). One string was
caught afterwards by the leftover-English scan (the P4 feature gloss)
and fixed with an asserted one-off replacement before the first
render. The transform source is the W45 core build; the VOL.1 PT
edition supplied only furniture/label precedents, not content.

**Toolchain versions (recorded from the actual run):**
`tools/venv/bin/python` = Python 3.12.3 · Pillow 13.0.0 · CairoSVG 2.9.1
· pypdf 6.21.2. (Use `tools/venv/bin/python` — never the ephemeral
`/tmp/wp-venv`.)

## 8. Proof log (builder self-check, final render)

- **Baseline (before any edit):** `freeze.py baseline` on the pristine
  core build reproduced all 8 shipped core SVGs BYTE-IDENTICALLY
  (8/8 sha256: p1 e057bbfc… · p2 c87aa67e… · p3 d50f09e1… ·
  p4 dd3b1b0f… · p5 c71ef315… · p6 b06a85d2… · p7 f2319cb8… ·
  p8 eaf368f8…); the core's shipped SVGs re-hashed unchanged
  afterwards. The builder's own copy re-ran to the same 8/8 before
  transformation.
- **Freeze diff vs core (`--strict-cjk`, final files):** added CJK = 0
  on every page (p1–p8 all 0; TOTAL 0). Per-page string churn is
  explanation-layer only: p1 +51/−46 · p2 +63/−60 · p3 +38/−38 ·
  p4 +40/−41 · p5 +42/−41 · p6 +39/−38 · p7 +91/−88 · p8 +191/−191.
  Every removed string containing CJK was inspected: each is a
  bilingual label, gloss item, P8 key line (key kept, note translated),
  furniture line, or the P7 disclosure sentence — no article body,
  stem, option, caption, or other target text was removed. Removed-CJK
  totals (e.g. P7 760→652) are the furniture/badge/subtitle Chinese
  replaced by Portuguese column forms plus the P7 disclosure sentence
  rendered in Portuguese instead of Chinese.
- **P8 (`p8.py compare`, final files):** CLEAN — core 150 noted,
  edition 150 noted, missing=[] extra_count=0 uncertain=[]
  keydiff=[]. All 150 keys byte-identical to the core, including #150
  (writing key `(开放题，范文如下)`; note in Portuguese).
  P8 style kept from the core family: dash `N. key — note`, writing
  `N. ✓ note`, separators `— Página N —`.
- **Occlusion audit (final files):** selftest OK (all 6 planted classes
  fire, clean controls silent); edition 0 flags; core 0 flags;
  NEW vs core 0.
- **Same-baseline ink-collision scan** (furniture-band class the
  canonical audit does not cover; adapted from the W45 es-en rowcheck):
  0 collisions across all 8 pages — including the P1 top band, where
  the Portuguese centre strap is longer than the English one.
- **P6 chart-label element check:** bars identical to core
  (y/width 1282/810, 1340/537, 1398/480); row-name and value-label ink
  identical; chart note on one line with no bar clash.
- **Gloss counts:** 10 calls, 33 items, per-call identical to core
  (see §3).
- **Build warnings (final run):** zero `FLOW OVERFLOW` / `HEAD TOO WIDE`
  warnings. Registry: TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 172 characters.
- **Column-end geometry:** P2 col3 ends 1103.9 · P3 1348.8 · P4 1258.1 ·
  P5 1216.9 · P6 1038.5 — all far above their exercise rules. P7 col3
  ends 1708.1, teaser ends 2554.1 — identical to the core (footer line
  2580 untouched).
- **Visual check:** all 8 cards eyeballed in full (P1–P8), plus a 2× crop
  of the P5 popcorn caption after the credit fix — no overflow,
  overlap, footer intrusion, or clipped box found. P8 test flow ends
  well above the keys rule; keys end above the footer band.

**Fix rounds (each followed by a full one-process re-render, never
patched in output; pre-fix baselines recorded here):**

1. **P8 keys overflow (build1):** `FLOW OVERFLOW [P8-keys]` — the
   Portuguese notes wrapped to 15 extra lines vs the core (179 vs 164
   key lines), pushing the tail to y=2585 past the 2540 content bottom.
   Fixed by shortening 12 note wordings (shared strings covered all 15
   extra-line keys: 1/9/11, 2, 12, 51/130, 77, 109, 111, 115, 120, 135,
   147, 149) to single-line forms with identical meaning and keys.
   Post-fix: no P8 overflow; keys end above the footer band.
2. **Two HEAD TOO WIDE heads (build1–build3):** P6
   `C · 练习篮子算一算 · Contas das cestas` (479.8 px > 434) →
   `C · 练习篮子算一算 · Cálculos` (368.0 px, VOL.1's bare-`Cálculos`
   precedent); P5 `C · 时间与数字 · Horários e números` (455.0 px) →
   first tried `Tempos e números` (445.2 px, still wide) →
   `C · 时间与数字 · Datas e horas` (378.2 px). Final run: 0 warnings.
3. **Strict-CJK +3 (first diff):** three added `，` on P8 — the renderer
   (svglib lines 40–41) converts ASCII commas adjacent to CJK into
   full-width `，`, and three Portuguese notes had added a comma after
   a cited Chinese word where the English original had none (keys 14,
   84, 142). Fixed by restructuring those three notes to avoid
   comma-after-CJK ("O tempo fica mais frio dia a dia depois do 立冬.",
   "Com o 直降 o preço do checkout é o que você paga.",
   "No 立冬 ela fez bolinhos com a mãe."). Re-diff: added CJK = 0.
4. **Leftover-English sweep:** the post-transform source scan caught one
   untranslated gloss (P4 feature gloss) and, on the rendered cards,
   one leftover credit ("Public domain" on P5) → "Domínio público".
   Final rendered-SVG English-word scan: only Portuguese words, proper
   names (Sina Sports, Maoyan, Xiao Hong, …), codes (S16, CC0, VOL.2),
   pinyin, and established loanwords (checkout, quiz, on-line) remain.

## 9. Adjudications and notes for the independent proofreader

- **P8 dash style is deliberate.** The VOL.1 zh-cn×pt edition used paren
  style because the VOL.1 core did; the W45 core prints dash style, so
  this fan-out keeps dash. A proofreader comparing against VOL.1's
  paren form should adjudicate against the W45 core, not VOL.1.
- **Type names are localised in the registry only** (Complete a frase /
  Escolha múltipla / Associação / Escolha no contexto / Escrita). They
  are never printed on pages; the P8 writing-type check in content8.py
  was updated to match (`== "Escrita"`), verified by the 150. ✓ render
  and the CLEAN p8 compare.
- **P7 B1 glossline adapts the comparison language:** the core contrasts
  Chinese order with an English example ("So English «Saturday evening,
  Nov 7» becomes …"); the PT edition contrasts with Portuguese
  ("Assim, «sábado à noite, 7 de novembro» vira …"). This is
  explanation-layer adaptation, not target-text change.
- **"checkout" / "quiz" / "on-line"** are used as loanwords in the
  Portuguese text, matching the shipped VOL.1 PT column's own usage
  ("descontado no checkout", "O grande quiz").
- **No new facts, dates, or quotations** were introduced; every number,
  date, and weekday is the core's (core KIT dates were verified with
  `date -d` Asia/Shanghai: 2026-11-02 Mon … 2026-11-08 Sun,
  2026-11-10 Tue, 2026-11-11 Wed, 2026-11-15 Sun).
- **Sibling builds in progress at build time** (W45 zh-cn × de/fr/it/nl
  build dirs, active 2026-10-28 ~07:01) touch different directories and
  did not interfere; this builder's dirs showed no foreign writes.
- **Pre-flight duplicate check:** at task start, the builder's build and
  edition dirs did not exist yet and no live worker was writing to
  them; the core build dir had no writes in the preceding 30 minutes.

## 10. Fix record — Gate 10 (B-1) transform consolidation (fix agent, NOT a finalisation claim)

The independent proof (hidden_files/w45/zh-cn-pt-proof/REPORT.md,
verdict NOT PASS) found exactly one blocking item: the standalone
transform `hidden_files/w45-zh-cn-pt-transform.py` (mtime 2026-10-28
07:09) predated the fix rounds, so transform-alone reproduced only 5/8
pages (P4, P5, P6, P8 differed). The delivered paper itself passed every
other gate. The fix folded all five fix-round edits into the transform
(19 changes, exact literals only; full list + pre/post hashes in
`hidden_files/weekly-report-w45-zh-cn-pt-build/FIX-LOG.md`):
12 shortened P8 notes, 3 comma restructurings (keys 14/84/142), the P4
feature gloss, the P5 head ("Datas e horas") + credit ("Domínio
público"), and the P6 head ("Cálculos"). No paper content, furniture,
or ABSTRACT.txt was changed.

Gate 10 self-run after the fold: fresh core copy + fixed standalone
transform alone (transform exit code 0, TOTAL replacements 538) through
the single one-process driver (exit code 0, registry TOTAL 150,
HEAD TOO WIDE 0, FLOW OVERFLOW 0) yields SVGs 8/8 byte-identical to the
delivered files. Scratch re-render: cards 8/8 byte-identical, print PDF
byte-identical (47,047,752 B, sha 41906847…); the delivered web PDF was
not regenerated in place and keeps sha 0bc2e290… (scratch web PDF
differs in 6 timestamp bytes only). Mechanical gates re-run: occlusion
edition 0 / core 0 / NEW 0, p8 compare CLEAN (150=150, keydiff []),
gloss 10 calls / 33 items = core. A full independent reproof follows;
this record does NOT declare the edition finalized.
