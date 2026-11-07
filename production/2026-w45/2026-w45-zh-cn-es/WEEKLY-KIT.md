# WEEKLY-KIT — Lucerna VOL.2 · 简体中文正文 + 西班牙语讲解 (zh-CN × ES)

**Edition:** Simplified Chinese target text (frozen W45 core) · explanations in
Spanish for Spanish-speaking readers · W45 (2026-11-02 → 2026-11-08) · 8 pages,
1950×2700, 4 columns, warm ivory paper. **Status: BUILT, NOT finalized** —
this is a builder handoff; independent proofreading is still owed by the
parent line. No Discord delivery, no main-chat card/PDF delivery, no
weekly-git touch, no insert.py run, no cron was done by this builder.

## 1. Identity and spec

- **Issue week:** Monday 2026-11-02 to Sunday 2026-11-08 (magazine model).
  Issue number: VOL.2, the second Simplified Chinese issue (same as core).
- **Pairing:** zh-cn × es — Simplified Chinese body text with a Spanish
  explanation layer, the edition for Spanish-speaking readers. The pairing
  badge is printed on P1 (see §2).
- **Masthead:** bare `Lucerna` in blackletter (UnifrakturMaguntia). Chinese
  is article-less per the SOP, so there is no “La”/“The”/“Le” article.
  Verified: “The Lucerna” 0, “Le Lucerna” 0 in the final SVGs.
- **Format:** 8 pages (a multiple of 4). One unified numbering sequence,
  1–150, no gaps or duplicates; P8 answer keys are generated from the
  exercise registry (same driver as the core).
- **Native Simplified Chinese:** inherited from the core, written natively
  from the mainland-China ecosystem. NOT converted or transcoded from any
  Traditional Chinese edition. This edition changes no target text (see
  §4). The explanation layer is entirely in Spanish; remaining Chinese
  strings classify as content (article bodies, stems/options, quoted
  examples, bilingual headers, data labels, captions, answer tokens,
  readers'-corner letter, teaser, pinyin) plus Chinese words cited inside
  Spanish notes/glosses exactly as the core cites them.
- **Build dir:** `hidden_files/weekly-report-w45-zh-cn-es-build/` (copy of
  the core build; only the explanation layer, the pairing furniture and
  the P8 key-line apparatus were changed). Transform script
  (`transform.py`, line-based whole-string replacements with an assertion
  after each) and check scripts (`keylines.py`, `checks.py`) live there.
  The core build dir was never imported from or executed in.

## 2. Pairing badge — slot/size case (TARGET core's family precedent)

**Case that applies: in-place replacement in the core's own badge slot.**
The W45 zh-cn core already carries its badge on its own line below the
double rules at (975, 434), 19.5pt bold sans, centered — the fan-out
replaces the badge TEXT in that slot and moves nothing. This is NOT the
FR/IT insertion case (badge inserted at y=574, 22pt, because y=372 is a
frozen body strapline), NOT the KO shift case (masthead block displaced),
and NOT a subtitle-slot replacement.

**Shipped precedent, measured from shipped SVGs (never from memory):**
W43 `files/weekly-report-zh-cn-es/svg/p1-touiban.svg` badge text node at
(975, 434), 19.5pt: “TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN
ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES”. The W45 core
badge sits at the identical coordinates and size. This edition's P1 badge
is that same string at (975, 434), 19.5pt, verified in the shipped SVG.

## 3. Furniture three-way (core EN · W43 shipped ES · this edition)

All “this edition” strings verified from this edition's shipped SVGs.

| Furniture | W45 core (EN) | W43 shipped zh-cn×es | This edition (W45 ×ES) |
|---|---|---|---|
| P1 badge | 简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers (975, 434, 19.5pt) | TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES (975, 434, 19.5pt) | W43 string verbatim (975, 434, 19.5pt) |
| Footer (all pages) | Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations | Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.1 · TEXTO EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL | Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.2 · TEXTO EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL (VOL.2 follows the target core) |
| Page line | 第 N 版 / 共 8 版 | Página N de 8 | Página N de 8 |
| Gloss prefix (`gloss()`) | Notes｜ | Nota — | Nota — (10 gloss boxes: P1 1, P2 2, P3 2, P4 1, P5 2, P6 2) |
| P8 separators | — Page N — | — Página N — | — Página N — |
| P8 key-line style | N. key — note; writing N. ✓ note (dash) | n. key (note); writing n. ✓ (note) (paren) | DASH, as the W45 core (see §5) |
| P8 header | 答案 · Answer keys — by page, with a note on every answer / All notes in English · ✓ = the writing task | 答案 · Claves — por página, con una nota para cada respuesta / Todas las notas en español · ✓ = la tarea de escritura | W43 strings verbatim |
| P1 strap | 简体中文版 · VOL.2 · 双11 · 立冬 · S16 | SEMANARIO CHINO SIMPLIFICADO · VOL.1 · 双11 · 大闸蟹 · 霜降 | SEMANARIO CHINO SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16 (Chinese topic words kept) |
| P1 strapline | 给学中文的人的周报 — Read the real China, in Chinese | 给学中文的人的周报 — Lee la China real, en chino | W43 second half verbatim |
| Top strip | 每周读中文 · Read real Chinese, every week | 每周读中文 · Lee chino de verdad, cada semana | W43 string verbatim |
| Photo credits | Photo: … — CC0 / Public domain (Wikimedia Commons) | Foto: … — CC0 (Wikimedia Commons) | Foto: … — CC0 (Wikimedia Commons); popcorn: Foto: Based5290 — Dominio público (Wikimedia Commons) |

**Discrepancy recorded:** `tools/tables.json` lists the es p8_separator as
“— PÁGINA {n} —” (all caps), but the W43 shipped same-pairing SVG prints
“— Página N —”. Per the brief (shipped SVG wins), this edition uses the
shipped form. tables.json was NOT edited by this builder; the parent line
may fold the correction in.

**Kept as in the W43 precedent:** contents level tag “全部” for the P8
row, and the mixed headers “Lee la página 1 y elige · 答案见第 8 版” /
“Respuestas en la página 8 · 答案见第 8 版” (Chinese tail kept).

## 4. Baseline proof (frozen core reproduction)

Before any edit, the copied core build was run unmodified (OUT repointed
to this edition dir). Its 8 output SVGs matched the shipped core SVGs
byte-for-byte (sha256 8/8), and the canonical tool agreed:

```
freeze.py baseline: 8/8 SVGs byte-identical
  p1 e057bbfcdfcd6fca · p2 c87aa67eb6785a58 · p3 d50f09e1a72b6fd3
  p4 dd3b1b0fdc80627a · p5 c71ef3153d70701c · p6 b06a85d276db8a53
  p7 f2319cb8997f8d36 · p8 eaf368f8dca48dff
  core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```

Baseline registry: 150 exercises, A2 56 / B1 69 / B2 25, pages
10/18/18/18/18/18/12/38, writing model 172 characters — identical to the
core KIT. Core SVGs re-hashed after the final build: all unchanged
(`core-svg-hashes-before.txt` in the build dir).

## 5. Freeze diff (core vs edition) and P8 style

`freeze.py diff --strict-cjk`: **added CJK = 0 on all 8 pages**
(P1 815 vs core 851; P2 1031 vs 1053; P3 790 vs 812; P4 789 vs 810;
P5 922 vs 944; P6 983 vs 1005; P7 652 vs 760; P8 1082 vs 1102).
Removals are explanation-layer only: furniture (badge/footer/strap/gloss
｜), the P7 readers'-corner disclosure rewritten from Chinese+English to
Spanish, and Chinese words inside core English notes replaced by pinyin
or Spanish. No target text changed; string churn per page is
explanation-layer only (+50/−46, +64/−60, +38/−38, +41/−41, +42/−41,
+40/−38, +91/−88, +198/−198).

**P8 style — dash, verified from the core's code path, not memory:**
the core's `content8.py` answer-generation lines are
`txt = f"{e_['n']}. {e_['key']} — {e_['note']}"` and
`txt = f"{e_['n']}. ✓ {e_['note']}"` for writing items, and the core P8
SVG prints in exactly that form. This edition leaves those two lines
**byte-identical** (diff-verified) and only translates the notes. The
W43 zh-cn×es edition's paren style belongs to the VOL.1 core's family
and was NOT carried over — per the tools README dash-family rule, a
fan-out keeps its own core's style.

**P8 printed-note set gate** (`p8.py compare`, core vs edition):
**CLEAN — core 150 noted, edition 150 noted, missing=[] extra_count=0,
keydiff=[]**. The printed keys are identical; notes differ only by
translation (Chinese citations inside notes kept as in the core, except
the two tightened notes in §8 where pinyin replaced the term).

**Registry key difference (1 item, apparatus only, W43 precedent):**
key 150's registry key is the apparatus line, not an answer:
core “(开放题，范文如下)” → edition “(pregunta abierta — modelo a
continuación)”, exactly as W43 zh-cn×es did (“(pregunta abierta —
modelo a continuación)”). It never prints as a key (the keys area
prints “150. ✓ …”). All other 149 registry keys are byte-identical;
page and level of every item are identical.

## 6. Contents, page by page (target text = core; explanation = Spanish)

| Page | Section | Level | Exercises | Content (inherited from core) |
|---|---|---|---|---|
| 1 | 头版 Top story (A2) | A2 | 10 (1–10) | Double 11 still running × Start of Winter on Saturday; this-week calendar box; contents; word of the week 「立冬」; parcel-locker photo; briefs; quick quiz. |
| 2 | 生活 Life (A2) | A2 15 / B1 3 | 18 (11–28) | Double 11 shopping life + Start-of-Winter life; practice example (sweater 240 + scarf 80 = 320, direct cut 50 → payable 270); shopping word cards 现货 / 直降 / 立减 / 补冬; autumn-valley photo. |
| 3 | 文化 Culture (A2→B1) | A2 15 / B1 3 | 18 (29–46) | Start of Winter feature (19th solar term, 17:52 moment, three micro-seasons, regional food, uneven cooling, Journalists' Day paragraph); frost + dumpling photos. |
| 4 | 体育 Sport (B1) | B1 | 18 (47–64) | S16 feature (AL out, IG/TES/BLG chasing the quarter-finals, Swiss format, fourth-round preview, 2026-10-27 cutoff stated on the page, final Beijing 2026-11-15 03:00); S16 schedule box (no score chart — final Swiss scores were not yet knowable); LAN-party file photo. |
| 5 | 青年 Youth (B1) | A2 1 / B1 17 | 18 (65–82) | AI film 《三星堆：未来往事》 + Start-of-Winter new film 《我们仅有一次的人生》; popcorn photo. |
| 6 | 深读 Deep read (B2) | B2 | 18 (83–100) | Double 11 deep read (why the rules got simpler; “lowest price” claims checked against checkout page, delivery cost, returns rules); practice-data bar chart only. |
| 7 | 词语精讲 Language focus | A2 4 / B1 4 / B2 4 | 12 (101–112) | A2 shopping/winter words; B1 time-and-date order (big → small); B2 reading news; error clinic (的/地/得, measure-word order, date order); frame 先…再…; readers' corner (see §7); 8 phrases; VOL.3 teaser. |
| 8 | 测验与答案 Test & keys | A2 11 / B1 24 / B2 3 | 38 (113–150) | A true/false (8) + B big quiz (10) + C complete-the-sentence (10) + D read-and-answer passage about Xiao Hong in Beijing (6) + E in-conversation (3) + F writing (1); then all 150 answer keys with brief Spanish notes, grouped by page with “— Página N —” headers for pages 1–8. Writing topic 《我的立冬周末》, 120–180 characters; model answer 172 characters (unchanged). |

## 7. Readers' corner (P7) — disclosure + explicit invitation

Inherited from the core: the corner letter itself is the core's Chinese
editor's-example letter, unchanged. The disclosure note is rewritten in
Spanish and satisfies BOTH requirements on the page:

> “Ejemplo de la redacción, no una carta real. VOL.1 prometió cartas
> reales y la mejor redacción de VOL.1 en VOL.2; no ha llegado ninguna
> carta real ni hay ningún texto publicable, así que este rincón sigue
> publicando un ejemplo de la redacción. Aplazado, no cancelado.
> ¡Envíanos tu carta en chino! Escribe dos frases sobre tu semana y la
> publicaremos aquí.”

(a) It discloses on-page that no genuine reader letters exist (labelled
editor's example + the VOL.1 promise deferred, “Aplazado, no
cancelado”); no reader, letter, name, or quotation was invented.
(b) It contains an EXPLICIT open invitation for real letters
(“¡Envíanos tu carta en chino! … la publicaremos aquí”) inside the
corner itself — not a facts-only disclosure, and not borrowed from
another page's exercise prompt (the P2/P3/P5/P6 “¿Y tú?” prompts are
separate and were not counted toward this requirement).

## 8. Measured totals and gates

- **Exercises: 150 total** — A2 56 · B1 69 · B2 25. By page: 10 / 18 / 18 /
  18 / 18 / 18 / 12 / 38. By type (registry labels unchanged):
  完成句子 68 · 单选 50 · 词汇配对 20 · 完形单选 11 · 写作 1.
- **Visible text** (concatenated `<text>` nodes, entities resolved by the
  XML parser): edition 24,811 characters without spaces / 28,747 with
  spaces; core measured the same way 22,990 / 26,717. The edition is
  longer because Spanish explanation is wordier than English; target
  text is identical. (The core KIT's 23,038 / 26,765 counts raw `&amp;`
  as 5 characters; 12 `&` occurrences × 4 = the 48-character offset.)
- **P6 practice chart** (cols 0–2): bars verified in the SVG rects at
  exactly 3.0 px per yuan from zero — widths 810 / 537 / 480 px for
  270 / 179 / 160 yuan, starting at x = 325. Row labels end at x ≤ 206
  (bar starts 325); value labels sit exactly 16 px right of their bar
  ends (1151 / 878 / 821). No label is clipped by any bar.
- **Photos:** 6, payloads byte-identical to the core per page (MD5 of
  embedded data URIs): P1 1 (locker), P2 1 (valley), P3 2 (frost,
  dumplings), P4 1 (lanparty), P5 1 (popcorn), P6 0, P7 0, P8 0.
  Credits identical to the core's `assets/CREDITS.md` (CC0 / public
  domain, Commons API Artist field); only the “Photo:” label became
  “Foto:” (popcorn: “Dominio público”).
- **Phrases of the week (P7):** all 8 verbatim from this issue's own
  articles, each occurring exactly 2× in the final SVGs (article + P7,
  full-width punctuation): 「不用等11月11日」 p. 1; 「下单就能发货」
  p. 2; 「先看结算页，再付款」 p. 2; 「水开始结冰」 p. 3;
  「三场都输了」 p. 4; 「小局一场没赢」 p. 4; 「故事够不够好」
  p. 5; 「别以后，就现在」 p. 5. Page tags in Spanish (“Página N”).
- **Gloss counts** (split each rendered `gloss()` string on `·`
  itself): 33 items total, EQUAL to the core item by item — P1 [4];
  P2 [4, 4]; P3 [3, 3]; P4 [3]; P5 [3, 3]; P6 [3, 3].
- **Gate evidence (final render, build-es-3):**
  - Driver (single process): TOTAL 150, levels A2 56 / B1 69 / B2 25,
    pages 10/18/18/18/18/18/12/38, writing model 172 characters,
    **zero** `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings.
  - P8 test flow ends col 2/3 y=1262 (identical to core); keys flow
    ends col 3/3 y=2411 (identical to core, bottom 2540).
  - P7 col3 ends 1679.1 (core 1708.1); teaser ends 2525.1 (core 2554.1),
    above the 2580 footer line.
  - Geometric occlusion audit (`tools/occlusion_audit.py`, selftest
    first: all 6 planted classes fire, clean controls silent):
    **0 flags** on the final SVGs.
  - Same-baseline ink-collision scan (all pages, all text nodes, PIL
    true-ink boxes incl. the P1 top band, badge line, band subs and
    footers): **0 flags**.
  - P8 top rule: last test-flow baseline sits above the y=1264 rule as
    in the core; eyeballed clean on the P8 card.
  - English-residue scan over all rendered text nodes: **0** — the
    only “Sport” hit is the proper-noun source name “Sina Sports”,
    present once in the core too. Masthead “Lucerna”: 23 occurrences.
  - Politics scan （战争， 地缘， 外交， 政治， 选举， 民调）: all 0.
    Banned intermediary-layer term: 0 occurrences (both forms) in the
    SVGs and in this KIT's prose.
  - Visual check: all 8 cards read in full — no overflow, no overlap,
    no footer intrusion, no clipped chart label.

## 9. Fix rounds (each followed by a full one-process re-render)

- **build-es-1 (pre-fix baseline):** 1 `HEAD TOO WIDE` (P6-ex head
  “C · 练习篮子算一算 · Cuentas de cestas” > 434 px) + 4 `FLOW OVERFLOW`
  in P8-keys (keys flow clamped to y=2585, past the 2540 bottom).
  Fixes: head shortened to “C · 练习篮子算一算 · Cuentas” (the W43
  single-word shortening pattern); 18 P8 notes tightened so each wraps
  in the same number of lines as its core counterpart (per-key line
  counts measured from the rendered P8 SVGs with `keylines.py`).
  Notes are only printed on P8, so tightening them touches no exercise
  page. Result (build-es-2): warnings 0, keys flow ends y=2411 = core.
- **build-es-2 (pre-fix baseline):** `freeze.py diff --strict-cjk`
  reported added CJK = 4 (立 ×2, 冬 ×2, all on P8): two tightened notes
  had cited the word 立冬 where the core note used the English term
  (“Start of Winter”). Fix: both notes reworded to pinyin citations
  (“La nueva película se estrena en lìdōng, 7 de noviembre.”;
  “lìdōng — estreno de la nueva película.”), each still wrapping to
  exactly 1 line (verified with the build's `wrap()` before applying).
  Result (build-es-3, final): added CJK = 0 on all pages, key lines
  0 worse, warnings 0, all gates green. No added CJK remains to be
  adjudicated.
- **Deliberate shortenings (Spanish wording only, no geometry, no
  Chinese, no keys touched):** “本周生活小日历 · This week's dates” →
  “本周生活小日历 · Fechas clave” and “这一周的高频词 · Words of the
  week” → “这一周的高频词 · Palabras clave” (both are the W43
  same-pairing overflow lessons — the longer Spanish titles would cross
  their box borders); “看比赛的中文 · Match words” →
  “看比赛的中文 · Para ver partidos”.
- **Re-aimed explanation (not a key, not target text):** the P7 B1
  glossline “So English «Saturday evening, Nov 7» becomes
  11月7日星期六晚上.” is re-aimed at Spanish readers as “Así, «el
  sábado por la tarde, 7 de noviembre» se convierte en
  11月7日星期六晚上.” The Chinese result string is unchanged.
- **Number localization (W43 precedent):** “1.192 million yuan” →
  “1,192 millones de yuanes” (comma decimal) in the P5/P8 notes; all
  other figures (dates, times, scores, basket maths) are unchanged.

## 10. Trend and fact sources (inherited — translation only)

No new facts were introduced; every fact, date, and figure below is the
core's, translated but not re-sourced. Full sourcing, including the
honesty limits, is in the core KIT
(`files/weekly-report-w45-zhcn-core/WEEKLY-KIT.md`):

- **Double 11 buildup** (not the day itself): JD.com spot sales from
  20:00 on 2026-10-12; Taobao/Tmall presale from 20:00 on 2026-10-15,
  tail-payment + spot sales from 20:00 on 2026-10-20; spot period to
  2026-11-13; peak sale 20:00 on 2026-11-10 (next week, mentioned only
  as such); WeChat shop first Double 11, 2026-10-12 to 2026-11-15
  (35 days); 18th Double 11; spot sales replacing presales, simpler
  rules (官方立减, 直降), AI entry points. All basket arithmetic is
  explicitly labelled practice data.
- **Start of Winter:** Saturday 2026-11-07, 17:52交节 (Beijing time),
  19th of the 24 solar terms, first of winter; three micro-seasons
  一候水始冰, 二候地始冻, 三候雉入大水为蜃; customs regionally varied,
  no single custom national; cooling not simultaneous everywhere.
  Source chain as in the core KIT (trend pool citing jieri8.com and the
  Hong Kong Observatory 2026 almanac; no independent second
  confirmation claimed for 17:52).
- **S16, cutoff honestly dated 2026-10-27:** Swiss stage Allen, Texas;
  quarter-finals 2026-11-04–07 at 06:00, semi-finals 2026-11-08–09 at
  06:00, final Beijing 2026-11-15 03:00 (Barclays Center, New York);
  verified results through the cutoff (LPL 0–4 in round 1; IG beat HLE,
  TES beat G2, BLG beat KC on 2026-10-26, all 2–1; GEN/DK 3–0 through;
  AL/TSW 0–3 out; AL lost to KC, then to TES, then 0–2 to TL on
  2026-10-27); fourth-round draw 2026-10-29–31 (BO3). Later rounds are
  preview, not result. P4 has no score chart for exactly this reason.
- **Films:** 《三星堆：未来往事》 (released 2026-10-23, Bona, 100 min,
  first domestic AI feature with a public screening licence; Maoyan
  4-day figure about 1.192 million yuan by noon 2026-10-26, 2 viewers
  per screening on Oct 24–25) and 《我们仅有一次的人生》 (nationwide
  2026-11-07, Sun Aoqian, Song Jia, Wen Qi, original title 《余烬》,
  Beijing International Film Festival Tiantan Award Best
  Cinematography, 114 min, slogan “别以后，就现在”).
- **Other calendar items:** 中国记者节 Sunday 2026-11-08; some schools'
  mid-term exams in early November on differing dates (not national).
- **Rejected material (as core):** anniversary content, all
  international politics, and Chinese domestic politics (target country
  is China) were excluded; Double 11 day itself (2026-11-11) is outside
  the issue week and appears only as next week's event.
- **W43 promises, as honoured by the core:** 立冬 in-week (lead, P1/P3/
  P7); S16 reported only as far as verifiable at the build cutoff with
  the completed report as a VOL.3 teaser item; 双11 arrivals as a VOL.3
  teaser item; real reader letters + best VOL.1 P8 writing still
  deferred with on-page disclosure (see §7), never fabricated.

## 11. Files and reproduction

**Deliverables** (`files/weekly-report-w45-zh-cn-es/`):

| File | Bytes | sha256 |
|---|---|---|
| `svg/` ×8 | — | (baseline hashes in §4 for the pre-edit run) |
| `cards/` ×8 (1950×2700 PNG) | — | — |
| `Lucerna-VOL2-ES.pdf` (print, 8 pp) | 50,133,157 | e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46 |
| `Lucerna-VOL2-ES-web.pdf` (web, 8 pp, JPEG q85 @1400 px) | 3,242,033 (< 10 MB) | 0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c |
| `WEEKLY-KIT.md` (this file) | — | — |
| `ABSTRACT.txt` (Spanish, single line, no ASCII double quotes) | — | — |

**Reproduction** (build code lives in
`hidden_files/weekly-report-w45-zh-cn-es-build/` — bslib4.py, svglib.py,
run.py, render.py, content12.py, content34.py, content56.py, content7.py,
content8.py, assets/; content modules run only through the single
one-process driver, never standalone and never imported inside a core
build directory):

```bash
cd hidden_files/weekly-report-w45-zh-cn-es-build
../../tools/venv/bin/python run.py        # single-process driver -> svg/
../../tools/venv/bin/python render.py     # svg -> cards PNG -> print + web PDF
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-zh-cn-es
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-zhcn-core/svg \
    --edition-svg ../files/weekly-report-w45-zh-cn-es/svg --strict-cjk
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-zhcn-core \
    --edition-dir ../files/weekly-report-w45-zh-cn-es --target zh-cn
```

**Toolchain versions (measured):** `tools/venv/bin/python` = Python
3.12.3; Pillow 13.0.0; CairoSVG 2.9.1; pypdf 6.21.2. (Use
`tools/venv/bin/python` — never the ephemeral `/tmp/wp-venv`.)

## 12. Adjudications and notes for the independent proofreader

- **P8 dash vs W43 paren:** deliberate (see §5). The W45 core family is
  dash; the answer-generation code is byte-identical to the core's.
- **Note-embedded Chinese citations kept:** Spanish notes cite Chinese
  words (e.g. “水始冰 = el agua empieza a helarse, b”) exactly as the
  core's English notes do. They add 0 CJK (every cited character
  already occurs in the core); the two notes that would have added
  立冬 were reworded to pinyin instead (§9), so the final strict-CJK
  count is 0 added, not “0 plus adjudicated citations”.
- **P8 top rule proximity (inherited from core, unchanged):** the P8
  test flow ends at y = 1262 against a bottom of 1252, with the keys
  rule at y = 1264. The canonical occlusion audit reports no flag there
  (the last ink sits above the rule); the P8 card was eyeballed clean.
- **P7 B1 glossline re-aim** (§9) and **P8 separator form**
  (§3, shipped SVG over tables.json) are the only two places where this
  edition knowingly departs from a literal English→Spanish swap or from
  a tool table; both are documented above for adjudication.
- **Start of Winter 17:52 source chain and S16 cutoff:** inherited
  from the core without change (see §10); this builder re-verified
  neither, and claims no new sourcing.
- **Traditional-character audit:** no script conversion of any kind
  was performed; the target text is the core's Simplified text
  byte-for-byte (freeze diff, §5). This is NOT a Traditional edition.

## 13. Gate 10 fix round (2026-10-28) — transform-alone reproduction closed (FIX, NOT finalization)

Independent proof (2026-10-28) passed every content/geometry gate but
blocked on Gate 10: `transform.py` alone reproduced only 5/8 SVGs —
21 post-transform manual edits had never been folded back into it
(P6 head overflow, P7 English frame text, P8 keys overflow to y=2585,
P8 key 135 English). This fix round folded all 21 diff lines into
`transform.py` (20 replacements; the content12 降价 replacement is
replace-all and covers 2 lines): the P6 head `Cuentas de cestas` →
`Cuentas`; the P7 frame translation (new replacement — it was never in
transform.py); 18 P8-note shortenings/rewordings (incl. the 2 pinyin
rewordings); and the content8 shùzì old string corrected to include
"AI" so it translates to `personajes digitales en la película con IA`.
All replacements are exact unique literals with count assertions
(tools README #17). Full record + pre-fix full SHA-256 hashes:
`hidden_files/weekly-report-w45-zh-cn-es-build/FIX-LOG-GATE10.md`;
Gate 10 scratch: `hidden_files/w45/zh-cn-es-fix/work/`.
Toolchain: `tools/venv/bin/python`, Python 3.12.3, PIL 13.0.0.

- **Pre-flight:** no live worker writing to the ES delivery/build dirs;
  three mtime snapshots over ~3 minutes showed zero changes; the proof
  session had completed (REPORT.md filed). Proceeded.
- **Gate 10 re-run (fresh core copy + fixed transform alone, one-process
  driver): 8/8 SVGs byte-identical to the delivered SVGs**, zero
  `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings (P8 keys end y=2411, P7
  teaser 2525.1, as delivered). Transform run: 317/320 replacements —
  the 3 remaining misses are the proof-adjudicated benign byline misses
  (content12 B1, content56 A2, content34 A2→B1), output unaffected.
  Transform-output content files match the delivered build content
  files except the repointed OUT line; bslib4.py identical.
- **In-place re-render** (`run.py`, log `build-es-fix.log` in the build
  dir): exit 0, zero warnings, registry 150 — and all 18 delivered
  files (8 SVGs, 8 cards, 2 PDFs) byte-identical to their pre-fix
  hashes (print PDF 50,133,157 B, web PDF 3,242,033 B, SHAs unchanged).
  Cards/PDFs were hash-verified, not regenerated (web-PDF regeneration
  would change timestamps and its SHA).
- **Mechanical gates re-run:** occlusion audit 0 flags, NEW vs core 0;
  p8 compare CLEAN (150/150, keydiff=[]); gloss counts 33, equal core
  vs edition; registry 150; 0 warnings.
- **Unchanged:** paper content, furniture, `ABSTRACT.txt`, and
  `tools/tables.json` (the all-caps separator discrepancy vs the
  shipped `— Página N —` form stays recorded for the parent line).
- **Status:** FIX DONE, NOT finalized — a full independent reproof
  follows per SOP §8.4.

## Micro-fix record (Gate 10 transform-miss cleanup; NOT finalization)

Coordinator decision was to clean up the 3 Gate 10 transform misses so
the reproduction chain exits 0. Outcome: **2 deleted, 1 held — exit 0
NOT achieved.** Full record:
`hidden_files/weekly-report-w45-zh-cn-es-build/MICROFIX-LOG.md`;
scratch: `hidden_files/w45/zh-cn-es-fix/work/microfix/` (gate10b).

- **Pre-flight:** no live writer on the ES dirs; two mtime snapshots
  ~3 minutes apart, zero changes; Gate 10 fix session completed.
- **Deleted (verified 0 hits in the fresh core, grep -F):**
  content12 B1 byline (`Lucerna editors · Reading level B1` — core has
  A2 ×2 only) and content56 A2 byline (`Lucerna editors · Reading
  level A2` — core has B1 + B2 only). Implemented by splitting the
  shared byline loop in `transform.py` (build dir only); all hitting
  byline instances preserved with identical counts. `py_compile` OK.
- **HELD, not deleted (task STOP rule):** content34 A2→B1 byline
  (`Lucerna editors · Reading level A2→B1`) — its old string IS present
  in raw core (content34.py line 16), so the literal 0-hit test fails.
  Mechanism: it still MISSES in sequence because the earlier loop A2
  replacement consumes it as a prefix substring and already produces
  its exact target string (`Redacción Lucerna · Nivel de lectura
  A2→B1`); it is a no-op in sequence but not absent from raw core.
  Coordinator decision still owed: accept the 1 remaining miss, or
  explicitly authorize the sequence-aware deletion of that line.
- **Gate 10 re-run (gate10b, fresh core copy + fixed transform alone,
  one-process driver): transform 317/318, exit 1** (sole miss: the held
  content34 A2→B1); driver exit 0, zero `HEAD TOO WIDE` /
  `FLOW OVERFLOW` warnings, registry 150 as delivered; **8/8 SVGs
  byte-identical to the delivered SVGs**; transform-output content
  files identical to the delivered build files except the repointed
  OUT line; bslib4.py identical.
- **Delivered files unchanged:** all 18 files (8 SVGs, 8 cards,
  2 PDFs) byte-identical to pre-cleanup baselines; `ABSTRACT.txt`
  unchanged; paper content, furniture, and `tools/tables.json`
  untouched. No weekly-git, insert.py, Discord, main-chat delivery,
  cron, or subagent activity.
- **Status:** MICRO-FIX PARTIAL, NOT finalized — a full independent
  reproof follows per SOP §8.4.

## Micro-fix round 2 (coordinator-authorized single-line deletion; NOT finalization)
- **Authorization:** coordinator explicitly overrode round 1's STOP rule
  for this ONE line only — delete the content34 A2→B1 replacement, on
  the documented evidence that the loop A2 replacement runs first,
  consumes the A2→B1 string as a prefix, and produces exactly the
  target string, so the A2→B1 replacement always misses in sequence
  and deleting it is provably output-identical. Nothing else was
  deleted or changed.
- **Pre-flight (NO CONCURRENT WRITER):** no live worker in the ES
  dirs (live workers were RU/IT/JA, then JA/FR only); two mtime
  snapshots ~3 minutes apart, zero changes; round 1 complete.
- **Pre-round-2 baselines:** all 18 delivered files matched round 1's
  post-fix baselines exactly; transform.py pre-edit SHA matched round
  1's post-edit SHA (`35dfbb95b…`), no drift.
- **The edit (build-dir `transform.py` ONLY):** deleted exactly one
  line (diff `153d152`, nothing else; `py_compile` OK):
  `add("content34.py", "Lucerna editors · Reading level A2→B1",
  "Redacción Lucerna · Nivel de lectura A2→B1")`. Post-edit SHA
  `b2dda203bf…`. NOTE: the comment block at transform.py lines 28–32
  still says this line is "HELD, not deleted … it stays" — now stale,
  left untouched per the one-line-only authorization and flagged to
  the coordinator/parent line.
- **Gate 10 re-run (gate10c, fresh core copy + fixed transform alone,
  one-process driver): transform 317/317, EXIT 0, zero MISS/FAILED**
  (count note: the task text asked for "318/318", but round 1 had 318
  entries and deleting one entry leaves 317 — 317/317 + exit 0 is the
  correct measured result); driver exit 0, zero `HEAD TOO WIDE` /
  `FLOW OVERFLOW` warnings, registry 150 as delivered; **8/8 SVGs
  byte-identical to the delivered SVGs**; output-identity proof:
  gate10c content34.py line 16 is exactly
  `Redacción Lucerna · Nivel de lectura A2→B1`, the deleted line's
  target string, produced by the loop A2 replacement.
- **Delivered files unchanged:** all 18 files (8 SVGs, 8 cards,
  2 PDFs) byte-identical to pre-round-2 baselines; `ABSTRACT.txt`
  unchanged; paper content and furniture untouched. Cards/PDFs
  hash-verified, NOT regenerated. No weekly-git, insert.py, Discord,
  main-chat delivery, cron, or subagent activity.
- **Status:** MICRO-FIX ROUND 2 DONE, NOT finalized — a full
  independent reproof follows per SOP §8.4.
