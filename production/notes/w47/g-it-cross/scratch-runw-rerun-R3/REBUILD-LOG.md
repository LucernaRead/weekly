# REBUILD-LOG — W47 CONSOLIDATED re-rebuild R3: nl-ru / pt-ru / zh-cn-ru (`_run_w` fix)

Date: 2026-11-11 ~23:59 UTC → 2026-11-12. Worker: R3 (3 *-ru editions).
Scratch dir (this log's home):
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-runw-rerun-R3/`
Production dir: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
Tools: `tools/run_build.py --steps run,render` + `tools/webpdf.py`; census `census.py`,
gaps `gap_r3.py` (both in this dir; census.py copied unmodified from
`scratch-runw-port/`, gap_r3.py written for this run — rawdict line-char
ink-gap measurement, same method as the probe's `gap_rude.py`).

## VERDICT: ALL THREE GREEN — 0 real joins, all gates pass, print AND web.

- **nl-ru**: census 30/40 → 7/10 (all remaining are known FPs); TOTAL 150;
  p8 150/150, compare CLEAN keydiff [137,138]; occlusion 0; freeze 8/8,
  print PDFs byte-identical; text layers identical (42,642 chars/page-set).
- **pt-ru**: census 15/16 → 9/9; `vencerпрошедшее` cleared; TOTAL 150;
  p8 150/150, compare CLEAN keydiff [137,138]; occlusion 0; freeze 8/8,
  print PDFs byte-identical; text layers identical (41,761).
  Residual: 2 fused `=` match-key tokens are source-format FPs (§4a), not joins.
- **zh-cn-ru**: census 115/152 → 94/121 (all remaining are CJK noise +
  normal-gap junctions); all named joins cleared (`IGобыграла`,
  `GENвышла`, `BLGобыграла` fused ×2, `Культурнаяночь:` ×5,
  `Результатына`, `Толькодля`, all `—X`); TOTAL 150; p8 150/150,
  compare CLEAN keydiff []; occlusion 0; freeze 8/8, print PDFs
  byte-identical; text layers identical (25,208).
- No edition BLOCKED. Nothing synced (per task — scratch only); KIT values
  in §6 for the sync step. Production untouched (§7).
- Two runtime restarts interrupted this run (00:42 and ~01:30 UTC): each
  killed the memory-gate waiter and wave A's `pdf_edge_scan` (PID 11866,
  then PID 2734 at 100/130 outputs). The restarts also freed memory, which
  is how the blocked builds got their windows. Wave A's scan recovery is
  wave A's own work — flagged here only because this task observed it.

## 0. VERIFY FIRST — all three pass, build allowed

| Edition | svglib.py md5 (on disk) | Expected after-md5 | Match |
|---|---|---|---|
| nl-ru | `8630b52f57bc4be209ef6ff4e51797a8` | `8630b52f57bc4be209ef6ff4e51797a8` | YES |
| pt-ru | `f1e0895cebf46c98b864657073004c6c` | `f1e0895cebf46c98b864657073004c6c` | YES |
| zh-cn-ru | `ce693ad4ff1d7ca6e8765c111c524ae0` | `ce693ad4ff1d7ca6e8765c111c524ae0` | YES |

Disk at start: 97G used (df), under the 100G stop line; 98G at end. Memory
gate applied before every render: wait while MemAvailable < 1500 MB
(`wait_build.sh`, 60 s polls). Wave A's `pdf_edge_scan` held ~1.0–1.6 GB
RSS through the run; renders ran in post-restart windows (available
1564–2578 MB) and whenever the gate opened. Production files untouched
throughout — SHAs re-verified at the end (§7). No commit/push/lint; no
other family touched.

## 1. BEFORE state (production PDFs — original builds, pre-`_run_w`)

Web PDFs were rebuilt by the web-rebuild worker from the PRE-`_run_w` print
PDFs (mtime 23:10–23:58 Nov 11), so both print and web carry the defect.

| Edition | File | Bytes | SHA-256 |
|---|---|---|---|
| nl-ru | `2026-w47-nl-ru.text.md` | — | `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` |
| nl-ru | `De-Lucerna-VOL4-nl-ru.pdf` (print) | 12,718,418 | `21b7adf007a15e195756d49b22c824e828f854e11e02a10c916426997c468cc8` |
| nl-ru | `De-Lucerna-VOL4-nl-ru-web.pdf` (web) | 1,661,395 | `df6c3a7cb16cad0fc2b26bd90a8bdc8065c1197598d4f28b8944f705b0b95b6c` |
| pt-ru | `2026-w47-pt-ru.text.md` | — | `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8` |
| pt-ru | `A-Lucerna-VOL4.pdf` (print) | 12,916,388 | `86447421b5a5abff48690ed8ab8e4cd51ce9808e5adcaf24f0d8e30004a0d2f2` |
| pt-ru | `A-Lucerna-VOL4-web.pdf` (web) | 1,188,611 | `c7017796abe91579d6429ae8f571401ef6aab0cd321e1acc593e66014f16c181` |
| zh-cn-ru | `2026-w47-zh-cn-ru.text.md` | — | `de12db587c41005301b221cce52ae0d088ec52f9eaccf2338aa94382f00e8094` |
| zh-cn-ru | `Lucerna-VOL4-RU.pdf` (print) | 33,572,610 | `bcfc550ff96ae87ce46fe1199592f5c7a690b91325dd3d5a410b11d95061305b` |
| zh-cn-ru | `Lucerna-VOL4-RU-web.pdf` (web) | 2,486,429 | `a281456fc27d9036e753cd210d01938a98a7aaf18da604c2b80f46e49553e979` |

## 2. BEFORE census (production print = web, all three)

| Edition | Distinct join tokens | Total join boundaries |
|---|---|---|
| nl-ru | 30 | 40 |
| pt-ru | 15 | 16 |
| zh-cn-ru | 115 | 152 |

Full rows: `census-before-<ed>-print.json` / `-web.json` (identical counts
print vs web for all three).

### 2a. BEFORE ink gaps — named P8 joins (task list) + DATE + other real-join candidates

Measured with `gap_r3.py` on the production print PDFs. Normal reference on
the P8 answer lines: ~2.36–2.48 pt (ru 9.8 pt); CJK body lines ~3.66–3.98 pt.

**nl-ru** (P8 model-answer lines; P8 normal ≈ 2.4–2.5 pt):
- `aankomen|требует` **1.44 pt** (fused in text layer) — CONFIRMED JOIN ✓ task value
- `Германия|проиграла` **1.47 pt ×2** (fused) — CONFIRMED JOIN (same class, not
  in the task's short list but identical defect)
- `Германия|—` 1.47 pt (×4 fused; +1.54 pt spaced instance) — join
- `—|список` 0.83–0.90 pt — join; `—|репортёр` **−0.84 pt** (overlap) — join;
  `—|выпуск` −0.09 pt — join; `—|Традиция` 1.44 pt (fused) / 2.21 pt spaced;
  `—|ботинок` 1.46 pt; `—|морковка` 0.91 pt; `—|время` 1.44 pt — joins
- `=|морковь` 1.14 pt; `=|город-крепость` 1.01 pt; `=|матч` 1.29 pt;
  `=|четвертьфинал` 1.48 pt — joins (glossary `=` connectors, text.md spaced)
- `,|множественное` −0.09 pt (kwartfinale line) / 1.42 pt (kandidaat line) — joins
- `»|опубликован` 1.08 pt — join
- `→|gaan` / `→|gaat` / `→|verandert` **2.47 pt** — NOT joins (normal median, per task)
- `→|Fout:` (P7) 3.75 pt — NOT a join (normal)
- `wij|→` 1.52 pt, `veranderen|→` 0.60 pt, `uur|→` 1.00 pt, `deur|→` 0.65 pt,
  `berlijn|→` 0.70 pt, `wortel|→` 0.48 pt — word→ blank-fill arrows; adjudication
  AFTER (see §4; same shape as the probe's `A2→B1` deliberate-diagram FP class,
  but text.md writes a space before `→` here — the AFTER gap decides)
- `ANTWOORDEN` 0.00 pt — NOT a join: one Dutch word, vocab over-split
  (ANTWOORD+EN); `1912.` (P4) 0.00 pt — NOT a join: one year, vocab over-split
  (19+12)
- DATE (measured directly, all already normal/spaced): P8 `15|ноября` 2.15/2.47 pt,
  `16|ноября` 2.40/2.48 pt, `1|ноября` 2.47 pt; P1 `16|ноября` 3.51 pt — NO DATE
  JOINS in nl-ru before (unlike ru-de; the ru DATE lines live in the ru-core
  target pages, not here).

**pt-ru** (P8 normal ≈ 2.33–2.41 pt):
- `vencer|прошедшее` **0.77 pt** (fused) — CONFIRMED JOIN ✓ task value
- `—|Праздник` 1.44 pt — join
- `folga|=|свободное` 0.00 pt; `consciência|=|знать` 0.00 pt (141.c; the 1.c
  instance is spaced at 2.38 pt) — joins
- `→|abriu/garantiu/saiu/sair/for/tiver` (P7) 3.89–3.98 pt — NOT joins (normal)
- `nacional|→` 1.88 pt (P3) / 1.12 pt (P8); `palmares|→` 0.51 pt (P3);
  `respostas|→` −1.29 pt (P8); `novembro|→` −0.11 pt (P8) — word→ blank-fill
  arrows; adjudication AFTER (same note as nl-ru)
- `✓|Смотри` 2.33 pt — NOT a join (normal median)
- DATE (already normal/spaced): P8 `20|ноября` 2.12–2.41 pt, `27|ноября`
  2.36–2.37 pt, `15|ноября` 2.40 pt; P1/P2 `20|ноября` 3.02–3.24 pt — NO DATE
  JOINS in pt-ru before.

**zh-cn-ru** (P8 ru lines normal ≈ 2.4 pt; CJK lines ≈ 3.66–3.98 pt):
- `IG|обыграла` **1.32 pt** (fused; sibling spaced instances 2.01/2.04 pt) —
  CONFIRMED JOIN ✓ task value
- `GEN|вышла` **1.45 pt** (fused) — CONFIRMED JOIN ✓ task value
- `BLG|обыграла` — MIXED: spaced instances 1.75–2.34 pt (incl. the task's
  1.80 pt question-line instance, already separate) + **2 fused instances
  1.31/1.34 pt** (lines 7.A, 122.A) — the fused two are joins, same class;
  the task's "already separate" refers to the 1.80 pt instance
- `Культурная|ночь` **0.99–1.08 pt ×5** (P8) — CONFIRMED JOINS (same class)
- `—|Финал` mixed: spaced 2.03–2.40 pt (normal) + **fused 1.41–1.44 pt ×4** — joins
- `—|Малый` mixed: spaced 2.15–2.40 pt + **fused 1.43/1.44 pt ×2** — joins
- `—|Первая` **1.43/1.44 pt ×2** — joins
- `》|выходит` **2.39–2.48 pt ×8**, `》|сняли` **2.40 pt**, `》|основан` **2.47 pt**
  — NOT joins (normal ink gap; fused text layer only)
- `—|История` 1.43, `—|Итог` 1.43 (spaced siblings 2.11–2.14),
  `—|Лучший` 1.43 (spaced 2.11–2.18), `—|Посылки` 1.44, `—|Полуфиналы` 1.44,
  `—|Порядок` 1.44, `—|Проверь` 1.44, `—|После` 1.44 (spaced 2.40),
  `—|Прошлогодний` 1.43, `—|Высокоскоростной` 1.43 (spaced 2.15),
  `—|Месяц` 1.43 (spaced 2.11–2.15) — JOINS
- `—|决赛` 1.44 — JOIN; `决赛|означает` 2.40 — NOT a join (only the em-dash
  half is joined); `✓|Открытое` 2.48 — NOT a join
- `Результаты|на` **1.35 pt** (P4, Cyrillic gloss line) — JOIN
- `Только|для` **1.92 pt** (P6, Cyrillic gloss line) — JOIN (below the
  ~2.4 pt normal for Cyrillic answer-size lines)
- `包裹|берёт` **2.40 pt** (fused text layer, normal ink gap) — NOT a join
  (ink already separate; space char absent from the text layer only)
- `凌晨|língchén` **2.48 pt** (fused text layer, normal ink gap) — NOT a join
- CJK `·` / `—` / `(` junctions 3.15–4.06 pt — normal, NOT joins
- CJK 0.00 pt "sentence tokens" (`11月|14`, `决赛|3比0`, `S16|总决赛`,
  `三候|闭塞而成冬`, `半决赛|11月`, `止步|四强`, `11月14日|文化`,
  `快递|没有爆掉`, `中通云仓|预计`) — NOT joins: CJK text has no inter-word
  spaces by design; the census over-fires because text.md tokenisation splits
  CJK strings into vocab pieces. The 0.00 pt is adjacent-CJK-char contact,
  the normal CJK metric, not a collapsed Latin/Cyrillic space.
- DATE (already normal/spaced): P8 `14|ноября` 2.43–2.44 pt ×5 — NO DATE JOINS
  in zh-cn-ru before. (`15/16/1/20/27 ноября` do not occur adjacently on its P8.)

## 3. Builds (scratch only)

Per edition: two independent `run_build.py --steps run,render` builds
(`<ed>` and `<ed>2`, different `--out`), then `webpdf.py` on the first build's
`build-copy/svg`. Serial, one render at a time; memory gate before each build
(MemAvailable ≥ 1500 MB; `wait_build.sh` polls every 60 s).

### nl-ru
- Build 1 (`nl-ru/`): RC=0, ~2 min (00:21–00:23 UTC). run.py TOTAL **150**,
  zero overflow; wrapper integrity "production unchanged (42 files re-hashed)".
  Print `De-Lucerna-VOL4-nl-ru.pdf` 12,718,074 B,
  SHA `b9847bb26eac3011660c767b4ae17857ddeb39014fe8b9ffa7b9ec90b0404933`.
- Web (`webpdf.py` on build-1 `build-copy/svg`, RC=0): 1,661,043 B,
  SHA `cbaac2df7c7acd38f35c9cd9eaba04b3416c290b72e676057f68dccb47b6c7ca`,
  55,022 text bytes.
- Build 2 (`nl-ru2/`, freeze): RC=0, TOTAL **150**, production unchanged.
  Started 00:42 UTC after a runtime restart killed the memory-waiter
  (wait 17 at 00:42, gate never opened 00:26–00:42; the restart also killed
  wave A's `pdf_edge_scan` PID 11866 — wave A's own recovery, flagged to
  parent, not this task's work). The restart freed memory (available
  1699 MB at 00:42:27, 2110 MB by build start) so build 2 ran immediately.
- text.md byte-identical: production SHA `f23da475…` = build-copy SHA ✓

### pt-ru
- Build 1 (`pt-ru/`): RC=0, ~2 min (00:45–00:47 UTC). run.py TOTAL **150**,
  zero overflow; wrapper integrity "production unchanged (43 files re-hashed)".
  Print `A-Lucerna-VOL4.pdf` 12,916,087 B,
  SHA `a3b022bc3dd5097e4c9217e3285d51d634a39672d7a6b6c4a6ee95725da85fee`.
- Web (`webpdf.py` on build-1 `build-copy/svg`, RC=0): 1,188,302 B,
  SHA `0cdf71671e02c7263c3883b5c1d0d324cc24c84c3a380625935c9fdd22849d77`,
  55,001 text bytes.
- Build 2 (`pt-ru2/`, freeze): RC=0, TOTAL **150**, production unchanged.
  Started 01:30 UTC after the second runtime restart killed the
  memory-gate waiter at wait 39 (gate never opened 00:51–01:29; the
  restarted wave-A edge scan, PID 2734, held ~1.3–1.6 GB RSS and died in
  the restart at 100/130 outputs). Restart freed memory (available
  1710 MB at 01:30:19) so build 2 ran immediately.
- text.md byte-identical: production SHA `87871659…` = build-copy SHA ✓

### zh-cn-ru
- Build 1 (`zh-cn-ru/`): RC=0, ~2 min (01:32–01:34 UTC). run.py TOTAL **150**,
  zero overflow; wrapper integrity "production unchanged (39 files re-hashed)".
  Print `Lucerna-VOL4-RU.pdf` 33,572,048 B,
  SHA `f1b2162dc91900e5d5a328d66e325a8d6bcf130f28d61d4ac0404e1e6b6189fe`.
- Web (`webpdf.py` on build-1 `build-copy/svg`, RC=0): 2,485,880 B,
  SHA `dbf960ab1c55eb1e4e14ef25db3a034b43254d6673373a02030f80915d414ee1`,
  52,559 text bytes.
- Build 2 (`zh-cn-ru2/`, freeze): RC=0, TOTAL **150**, production unchanged.
  Started 01:36 UTC (available 2095 MB). Print SHA identical to build 1.
- text.md byte-identical: production SHA `de12db58…` = build-copy SHA ✓

## 4. AFTER census + gaps (print AND web)

### nl-ru — AFTER: **7 tokens / 10 boundaries** (BEFORE 30/40), print = web
Remaining tokens, all previously-adjudicated false positives, **0 real joins**:
- `ANTWOORDEN` 0.0 pt ×2 — one Dutch word, vocab over-split (ANTWOORD+EN)
- `1912.` (P4) — one year, vocab over-split (19+12)
- `→gaan` 2.47 pt ×2, `→gaat` 2.47 pt, `→verandert` 2.40 pt — P8 arrow cases
  at the normal median, NOT joins per task
- `→Fout:` (P7) 3.75 pt — normal
- `35+30+20+15` — P8 arithmetic chain, no-space by design

Cleared (BEFORE → AFTER, print; text layer now spaced in both PDFs):
- `aankomen|требует` 1.44 → spaced, fused form absent; `Германия|проиграла`
  1.47 ×2 → spaced, fused absent
- all `—` junctions (0.83–1.47, incl. `—|репортёр` −0.84 overlap) → gone
  from census; all `=` junctions (0.00–1.48) → gone; `,|множественное`
  (−0.09/1.42) → gone; `»|опубликован` 1.08 → gone
- word→ blank-fill arrows: `uur|→` 1.00 → **2.43 sp**, `deur|→` 0.65 → **2.53 sp**,
  `berlijn|→` 0.70 → **2.50 sp**, `wortel|→` 0.48 → **2.49 sp**,
  `wij|→` 1.52 → **2.49 sp**, `veranderen|→` 0.60 → **2.47 sp** — all at the
  normal median now (the arrows were kern-collapsed joins, not deliberate
  connectors; the `___` blank itself is untouched)
- DATE (still normal): P8 `15|ноября` 2.46/2.48 (was 2.15/2.47),
  `16|ноября` 2.48/2.48, `1|ноября` 2.47 — no DATE joins before or after.

### pt-ru — AFTER: **9 tokens / 9 boundaries** (BEFORE 15/16), print = web
Remaining tokens, adjudicated **0 real joins**:
- `→abriu/garantiu/saiu/sair/for/tiver` (P7) 3.90–3.98 pt — NOT joins (normal)
- `✓Смотри` 2.41 pt — NOT a join (normal median)
- `folga=свободное` 0.00 pt, `consciência=знать` 0.00 pt — NOT joins:
  **source-format false positives** (see §4a below). All 12 match-key
  `word=gloss letter` strings render fused, uniformly, by design.

Cleared (BEFORE → AFTER, print; text layer now spaced in both PDFs):
- `vencer|прошедшее` 0.77 → spaced, fused form absent ✓ task value
- `—|Праздник` 1.44 → gone from census
- word→ blank-fill arrows: `nacional|→` 1.88 (P3) / 1.12 (P8) →
  **3.67 sp / 2.62 sp**; `palmares|→` 0.51 → **3.67 sp**;
  `respostas|→` −1.29 → **2.60 sp**; `novembro|→` −0.11 → **2.66 sp** —
  all at/above the normal median now
- DATE (still normal): P8 `20|ноября` 2.34–2.44 (was 2.12–2.41),
  `27|ноября` 2.36–2.45, `15|ноября` 2.40; P1 `20|ноября` 3.02/3.71,
  P2 3.19 — no DATE joins before or after. (P1 second instance 3.24→3.71 pt
  is the kern correction on that run's width, not a defect.)

#### §4a. The pt-ru `=` junctions — why they are NOT joins (evidence chain)
1. The source strings themselves have no spaces: `content12.py:280`
   `"folga=свободное время без работы b"` (and 3 siblings),
   `content34.py:200` (4 more), `content8.py:85`
   `"consciência=знать и помнить c"` (and 3 siblings) — 12 strings, all
   uniformly `word=gloss letter`. `bslib4.py match_set()` (line 222–224)
   registers each note verbatim as the model-answer note; P8 renders it
   as `26. b — folga=свободное время без работы b`. The P2 exercise itself
   never shows the `=` strings (only numbered words + lettered meanings).
2. No spaced sibling exists anywhere: all 8 checked key strings render
   fused on P8 (`feriadão=длинные/трёхдневные`, `programação=программа`,
   `aproveitar=хорошо`, `gabarito=официальные`, `agregado=общий` — all
   fused; no spaced variant anywhere in the P8 text layer). Every
   kern-defect join cleared in this run HAD a spaced sibling on the same
   page; these have none.
3. The census flag is a global-vocab coincidence: the space-adjacency check
   fires on UNRELATED text.md lines — `5 de folga = 15 dias` (arithmetic,
   line 343) for `folga`, and the glossary `consciência = сознание`
   (line 52) for `consciência` — not on the P8 line's own text (text.md's
   P8 key is the bare `26. b` / `141. c`, lines 522/534).
4. `_run_w` demonstrably applied its correction here: the `свободное` run
   moved x 169.3 → 170.0 (+0.7 pt, exactly the kern) between production
   and build-copy SVGs. The gap stays 0.00 only because there is no space
   glyph in the source to widen — no measurement fix can create one.
5. Precedent in the task's own adjudication: `A2→B1` (0.0 pt, deliberate
   diagram connectors) and nl-ru's `35+30+20+15` (no-space arithmetic
   chain) are accepted as designed no-space notation. The `=` key notation
   is the same class. The task's P8-join list for pt-ru named only
   `vencerпрошедшее`, which cleared.
6. Cross-check: nl-ru's source mixes both forms IN THE SAME LIST
   (`content8.py:85`: `groepswinst=победа в группе c`,
   `schoen = ботинок d`, `gedicht=стихотворение a`) — the authors write
   the key notation both ways, and the census flags it only where text.md
   happens to contain a spaced `word =` elsewhere. Same rendering, flagged
   in pt-ru, unflagged in nl-ru → the flag is a text.md coincidence, not
   a rendering verdict.
RESIDUAL (not a gate failure, flagged for the parent): the two fused `=`
keys are visible as glued text to a reader. Fixing them means editing the
12 match-key source strings (add spaces around `=`) — a CONTENT change to
production sources, outside this spacing-only rebuild (this task forbids
touching production files; text.md must stay byte-identical). Recommend the
sync step take pt-ru as-is and the parent decide whether to open a
separate source-data fix; do NOT hold the _run_w sync on it.

### zh-cn-ru — AFTER: **94 tokens / 121 boundaries** (BEFORE 115/152), print = web
Cleared tokens (23 tokens gone, incl. every real join — full list in the
diff below; verified by ink gaps, not just by census absence):
- `IGобыграла` 1.32 → **2.38–2.44 sp** (3 instances); `GENвышла` 1.45 →
  **2.42 sp**; `BLGобыграла` fused 1.31/1.34 → **2.38–2.43 sp, all 8
  instances** (the task's 1.80 pt instance now 2.38–2.43, still separate);
  `Культурнаяночь:` 0.99–1.08 ×5 → **2.41–2.42 sp** ✓ task values
- `Результатына` (P4) 1.35 → **3.75 sp**; `Толькодля` (P6) 1.92 → **3.81 sp**
- All `—X` dash junctions → spaced at normal (e.g. `—|Финал` 1.41–1.44 fused
  → 2.38–2.45 sp ×11; `—|Малый`, `—|Первая` all 2.38–2.45 sp); `—|决赛`
  1.44 → gone (the `决赛|означает` half remains at 2.40, normal)
- Fused forms absent from BOTH print and web text layers; spaced forms
  present (`IG обыграла`, `GEN вышла`, `Культурная ночь`, `Результаты на`,
  `Только для`) ✓
- DATE (unchanged, normal): P8 `14|ноября` 2.43–2.44 sp ×5 — no DATE joins
  before or after.
- Remaining 94 tokens, all adjudicated NOT joins:
  - CJK `·` / `—` / `(` / `+` junctions at 3.15–4.06 pt (normal CJK metric);
  - CJK whole-sentence tokens with 0.00 pt gaps (14 rows, e.g.
    `决赛3比0。BLG一路打赢了三支韩国`, `S16总决赛，BLG`, `11月|14`) — CJK
    char adjacency, no spaces by design, IDENTICAL before/after (the
    counts and gaps are unchanged; the _run_w fix does not touch CJK
    spacing, as predicted);
  - Normal-gap Cyrillic junctions: `》|выходит` 2.39–2.48 (×8, incl. the
    re-tokenized `《白衣逆行者》сняли` — the `—` half cleared, the `》` half
    was always normal), `》|сняли` 2.40, `》|основан` 2.47, `✓|Открытое`
    2.48, `包裹|берёт` 2.47, `凌晨|língchén` 2.39 (both still fused in the
    text layer but normal ink, as before — no space char by design);
  - No remaining token has a measured gap < 2.0 pt except the CJK
    sentence tokens above (0.00 = CJK adjacency, not a collapsed space).

## 5. Gates per edition

### nl-ru
- run.py TOTAL **150** (both builds), zero overflow
- p8 extract **150/150** ✓
- p8 compare vs core-nl: **CLEAN**, missing=[] extra=0 uncertain=[],
  keydiff=**[137, 138]** (expected native-language model-answer keydiff) ✓
- occlusion audit: selftest OK, **0 flags** ✓
- freeze: **8/8 SVG SHA match** between the two independent builds; print
  PDFs **byte-identical** (SHA `b9847bb26eac3011660c767b4ae17857ddeb39014fe8b9ffa7b9ec90b0404933`) ✓
  (build-2 SVGs p1–p8: 0e5a82e2…, 16aca666…, 1903259f…, 79e8a699…, fab8dff7…,
  d0c6f864…, 5e8b98cc…, 312cf451…)
- print/web text layers: **identical per page, all 8 pages** (42,642 chars each) ✓
- text.md byte-identical ✓

**nl-ru: ALL GATES GREEN — 0 real joins, print AND web.**

### pt-ru
- run.py TOTAL **150** (both builds), zero overflow
- p8 extract **150/150** ✓
- p8 compare vs core-pt: **CLEAN**, missing=[] extra=0 uncertain=[],
  keydiff=**[137, 138]** (expected native-language model-answer keydiff) ✓
- occlusion audit: selftest OK, **0 flags** ✓
- freeze: **8/8 SVG SHA match** between the two independent builds; print
  PDFs **byte-identical** (SHA `a3b022bc3dd5097e4c9217e3285d51d634a39672d7a6b6c4a6ee95725da85fee`) ✓
- print/web text layers: **identical per page, all 8 pages** (41,761 chars each) ✓
- text.md byte-identical ✓

**pt-ru: ALL GATES GREEN — 0 real joins, print AND web** (with the §4a
source-format `=` residual documented, not a gate failure).

### zh-cn-ru
- run.py TOTAL **150** (both builds), zero overflow
- p8 extract **150/150** ✓
- p8 compare vs core-zh-cn: **CLEAN**, missing=[] extra=0 uncertain=[],
  keydiff=**[]** ✓
- occlusion audit: selftest OK, **0 flags** ✓
- freeze: **8/8 SVG SHA match** between the two independent builds; print
  PDFs **byte-identical** (SHA `f1b2162dc91900e5d5a328d66e325a8d6bcf130f28d61d4ac0404e1e6b6189fe`) ✓
- print/web text layers: **identical per page, all 8 pages** (25,208 chars each) ✓
- text.md byte-identical ✓

**zh-cn-ru: ALL GATES GREEN — 0 real joins, print AND web.**

## 6. KIT §5+§7 values (new print/web SHAs + sizes — for the sync step; KIT files NOT edited)

| Edition | File | Bytes | SHA-256 |
|---|---|---|---|
| nl-ru | `De-Lucerna-VOL4-nl-ru.pdf` (print) | 12,718,074 | `b9847bb26eac3011660c767b4ae17857ddeb39014fe8b9ffa7b9ec90b0404933` |
| nl-ru | `De-Lucerna-VOL4-nl-ru-web.pdf` (web) | 1,661,043 | `cbaac2df7c7acd38f35c9cd9eaba04b3416c290b72e676057f68dccb47b6c7ca` |
| pt-ru | `A-Lucerna-VOL4.pdf` (print) | 12,916,087 | `a3b022bc3dd5097e4c9217e3285d51d634a39672d7a6b6c4a6ee95725da85fee` |
| pt-ru | `A-Lucerna-VOL4-web.pdf` (web) | 1,188,302 | `0cdf71671e02c7263c3883b5c1d0d324cc24c84c3a380625935c9fdd22849d77` |
| zh-cn-ru | `Lucerna-VOL4-RU.pdf` (print) | 33,572,048 | `f1b2162dc91900e5d5a328d66e325a8d6bcf130f28d61d4ac0404e1e6b6189fe` |
| zh-cn-ru | `Lucerna-VOL4-RU-web.pdf` (web) | 2,485,880 | `dbf960ab1c55eb1e4e14ef25db3a034b43254d6673373a02030f80915d414ee1` |

text.md SHAs unchanged (byte-identical, §5): nl-ru `f23da475…`, pt-ru
`87871659…`, zh-cn-ru `de12db58…` (full SHAs in §1).
All web PDFs < 7 MB. Print/web SHAs above are from build 1; build 2 print
PDFs are byte-identical (frozen), so the same SHAs hold for both builds.
(Web PDFs were built once, from build 1's SVGs; webpdf font subsetting is
non-deterministic across processes, so a re-run would differ in subset
bytes only.)

## 7. Production untouched verification

Re-hashed at end of work (01:40 UTC) — every production value identical
to §1 before-state:
- nl-ru: text.md `f23da475…`, print `21b7adf0…` (12,718,418 B),
  web `df6c3a7c…` (1,661,395 B), svglib md5 `8630b52f…` ✓
- pt-ru: text.md `87871659…`, print `86447421…` (12,916,388 B),
  web `c7017796…` (1,188,611 B), svglib md5 `f1e0895c…` ✓
- zh-cn-ru: text.md `de12db58…`, print `bcfc550f…` (33,572,610 B),
  web `a281456f…` (2,486,429 B), svglib md5 `ce693ad4…` ✓
- Each of the 6 `run_build.py` runs reported "production unchanged
  (39–43 files re-hashed)". No commit/push/lint. No production file
  touched; all builds, PDFs, SVGs, JSONs and this log live only in this
  scratch dir. Disk: 97G at start → 98G at end (scratch builds), under 100G.

## 8. Files in this scratch dir

- `REBUILD-LOG.md` (this file), `census.py` + `line_gaps.py` (copied
  unmodified from `scratch-runw-port/`), `gap_rude.py` (copied, unused —
  superseded by `gap_r3.py`), `gap_r3.py` (R3 gap probe: census-driven +
  explicit pairs, rawdict ink gaps), `wait_build.sh` (memory-gate waiter).
- `census-before-<ed>-{print,web}.json`, `census-after-<ed>-{print,web}.json`
  (6 + 6), `gaps-before-<ed>-print.json`, `gaps-before-<ed>-dates.json`,
  `gaps-after-<ed>-{print,arrows}.json`, `gaps-after-zh-cn-ru-print.json`.
- `<ed>/` + `<ed>2/` (run_build scratch: `build-copy`, `run-build.log`;
  build-1 dirs also hold `p8-extract.json`, `p8-compare.json`,
  `occlusion.json`), `<ed>-webpdf.log`, `<ed>2-run-build.log`,
  `pt-ru2-wait.log` (waiter 00:51–01:29, gate never opened — build 2 ran
  after the 01:30 restart instead).

## 9. Notes for the sync step + parent

- **GO for sync on all three** (scratch-verified; production untouched).
  Wave A was still running its census on the production PDFs when this
  task started; sync only after wave A reports (per task).
- **pt-ru `=` follow-up (not blocking)**: the 12 match-key strings
  (`content12.py:280`, `content34.py:200`, `content8.py:85`) are written
  `word=gloss letter` with no spaces. If the parent wants them spaced,
  that is a source-data edit + re-export question for a separate step —
  it changes P8 key text, and the spaced siblings in nl-ru's own list
  (`schoen = ботинок`) show the authors mix both forms.
- **Runtime restarts killed two waiters + wave A's edge scan twice.**
  The second restart (at ~01:29–01:30) also killed the restarted edge
  scan (PID 2734) at 100/130 outputs — wave A will need to resume/re-run
  it. Nothing in this task depends on it.
- **zh-cn-ru print PDF is 33.5 MB** (largest of the three; CJK fonts) —
  well within the ≤7 MB web-PDF limit for the web file (2.49 MB); the
  print file is not pushed to `issues/` (only the web PDF is), per the
  repo's layout.
