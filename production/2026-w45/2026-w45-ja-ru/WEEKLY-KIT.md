# Lucerna Weekly — VOL.2 — Japanese × Russian (JA×RU) — W45

**Issue week:** Monday 2 – Sunday 8 November 2026.
**Pairing (badged on the P1 masthead and on all 8 footers):**
`ТЕКСТЫ НА ЯПОНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`
Footer: `Lucerna · ЯПОНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ЯПОНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ` + `Страница N из 8`.
**Target language:** Japanese (article-less: masthead is bare `Lucerna`, no article).
**Reader native language:** Russian. The entire explanation layer is Russian; the
Japanese body text is frozen verbatim from the W45 JA core.
**Status: builder-complete only.** Finalisation requires an independent proofread
(own occlusion audit, own freeze/P8 checks, full visual pass). This KIT does not
declare the edition final. Nothing was posted to Discord, nothing was sent to the
main chat, no cron was created, `weekly-git` was not touched, the core and W43
directories were only read (core SVGs re-hashed unchanged at close-out).

## Measured totals (verified against the core, not copied from other languages)

- 150 exercises; levels A2 46 / B1 75 / B2 29.
- Page distribution: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38; numbers continuous 1–150.
- Type counts (Russian registry names): Дополните предложение 50, Выбор ответа 51,
  Соотнесите пары 12, Составьте предложение 8, Верно или неверно 11,
  Текст с пропусками 13, Перевод 4, Сочинение 1.
- Model essay `『私の11月の週末』`: 167 characters (character count, not word count),
  byte-identical to the core.
- Golden phrases: 8 Japanese sentences, each exactly 2× in the whitespace-stripped
  concatenation of all SVG text (once in its article, once on P7).
- P7 phrase page tags (W43 JA×RU form): (Страница 1) ×2, (Страница 2) ×2,
  (Страница 3), (Страница 4), (Страница 5), (Страница 6).
- House style: です・ます throughout; weekdays in full forms 土よう日・日よう日;
  no ruby/furigana.

## Per-page contents

- **P1 表紙 (hyoushi):** Culture Day (Tuesday 3 November) + autumn-leaf weekend
  7–8 November; trend box; week-at-a-glance; quiz; maple photo.
- **P2 くらし (kurashi):** ゆる整え食 (Ajinomoto announcement 21 October);
  warm November; season words; exercises 11–28.
- **P3 文化 (bunka):** Culture Day + Kanazawa traditional crafts (exhibition to
  8 November, Sunday); Hiroshige III 1876 print; exercises 29–46.
- **P4 スポーツ (supotsu):** Japan Series, Yokohama games 1–2 verified
  (G1 24 Oct, G2 25 Oct); G3–G7 schedule only, results deferred to VOL.3 on the page;
  stadium photo; exercises 47–64.
- **P5 若者・エンタメ (wakamono):** Halloween 31 October (just-passed event) +
  autumn festivals; pumpkin photo; exercises 65–82.
- **P6 深読み (fukayomi):** warm November + autumn travel; Naruko Gorge at its
  best the 31 Oct–8 Nov weekend; Kobe Nunobiki Herb Garden illuminations from
  7 November to 28 December; practice chart 近場の満足 38 / 温泉 27 / 紅葉 21 /
  グルメ 14 = 100, labelled 練習用データ · Учебные данные (practice data, not a
  real survey); exercises 83–100.
- **P7 ことば (kotoba):** A2 column 本と読書のことば (Reading Week, to 9 November)
  / B1 紅葉のことば / B2 数字を読む + error clinic 4 items + 『ゆるく整える』
  frame + readers' corner + VOL.3 preview; exercises 101–112.
- **P8 テストと答え (tesuto):** sections A–H; E = JA↔RU translation 4 items
  (re-aimed from the core's JA↔ZH; see P8 gate); exercises 113–150;
  all 150 answer notes in Russian.

## Images (4, all reused from the VOL.1 verified set, PD/CC0 only, payload byte-identical to core)

| Page | Image | Credit line on page | Licence |
|---|---|---|---|
| P1 | Maple | 写真：Poliphilo — CC0（Wikimedia Commons） | CC0 |
| P3 | Utagawa Hiroshige III, 1876 print | 版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons） | Public Domain |
| P4 | Yokohama Stadium Dream Gate | 写真：Syced — CC0 | CC0 |
| P5 | Pumpkins | 写真：Petr Kratochvil — パブリックドメイン | Public Domain |

P2 and P6 carry no photo, as in the core. No new images were downloaded.
Credit lines come from the Wikimedia Commons API Artist field. `<image>`
elements are byte-identical to the core on every page (counts 1/0/1/1/1/0/0/0).

## Gate results (final round-2 output; raw outputs in the build dir)

- **Freeze** (`tools/freeze.py baseline` on the pristine core build, then
  `diff --strict-cjk`, core vs edition): baseline **8/8 byte-identical**
  (record: `tools/scratch/baseline-w45-ja-core/`; core prefixes p1 4abe63d2,
  p2 08439072, p3 48a1fe94, p4 11b592b5, p5 3035b928, p6 a8095c47,
  p7 08060a28, p8 9e733a42; shipped core SVGs re-hashed afterwards, unchanged).
  Diff: **added CJK = 0 on all 8 pages** (P1 1406→1275, P2 1312→1161,
  P3 1172→1051, P4 1263→1169, P5 1247→1132, P6 1186→1101, P7 1676→1308,
  P8 2721→1448). P7 vocabulary boxes: Japanese definition sentences never
  localised; only the gloss part is Russian.
- **Japanese freeze proof (code string set-diff, word-level):** edition-only
  kana-bearing strings without Cyrillic = 0 — every new Japanese-bearing
  string is a JP+RU pair or a Russian note citing a Japanese word. Core-only
  strings longer than 40 characters are only the footer furniture, the OUT
  repoint paths, the Japanese disclosure sentence (replaced per the ruling
  below), one gloss line (JP headwords + Chinese glosses → JP+RU), and the
  Chinese disclosure. No Japanese article, stem, option, letter, or figure
  string was removed or added.
- **P8** (`tools/p8.py compare`, explicit dual paths `--core-p8/--edition-p8
  --total 150`): **CLEAN, 150 noted = 150 noted, missing=[], extra=0,
  uncertain=[]**, keydiff [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113,
  115, 117, 118, 137, 138, 140, 146, 147] (21 items, adjudicated at
  printed-line level with no double counting):
  - **True re-aims (2, legal — direction change JA↔ZH → JA↔RU):** #137
    `文化日是11月3日。` → `День культуры — 3 ноября.` (body Japanese
    `文化の日は11月3日です。 → ___` frozen); #138 `乱扔垃圾，要罚2,000日元。` →
    `За брошенный мусор — штраф 2 000 иен.` (body Japanese frozen; this
    wording coincides with the W43 JA×RU precedent, the fact being identical).
  - **Prompt localisation landing in keydiff (1):** #140 — true key frozen
    Japanese `神戸の紅葉のライトアップを見に行きたいです。`, note localised
    `对照第6版（神户的灯光秀）` → `См. страницу 6`; the tool's paren branch
    folds the note stem into the extracted key, so it appears in keydiff
    although the true key did not change.
  - **Extraction artifacts (18, not real key changes):** #1, #2, #5, #7, #8,
    #9, #29, #32, #65, #69, #78, #101, #113, #115, #117, #118, #146, #147 —
    the tool's paren-branch truncates each printed key at the last
    parenthesis group, so the compared "key" is really (true key +
    translated note stem). The true printed keys (3, 9, 7, B, C, A, 27,
    ○, × …) were verified byte-identical to the core in every case; only
    the note language differs, which is the fan-out's job.
  - **Prompt localisation NOT in keydiff (1):** #139 — body
    `读书周从10月27日开始。→ ___` → `Неделя чтения начинается 27 октября. → ___`,
    key `読書週間は10月27日から始まります。` byte-identical (no parenthesis,
    dash-branch keys equal). Prompt localisations total 2 (#139, #140);
    the unambiguous count is **21 = 2 true re-aims + 1 prompt-localisation
    in keydiff + 18 artifacts**.
- **P8 note completeness (the standing JA-family gate):** all 150 printed
  notes compared core vs edition by two independent methods — (a) the
  transform's 130 NOTE keys scanned against the P8 keys region: the only
  surviving key is the language-neutral arithmetic note `38+27=65`
  (printed `38 + 27 = 65`, spaces stripped by the scan); (b) full item
  reconstruction core vs edition: 150/150 items present on both sides,
  **0 byte-identical items** (every item differs by its localised note,
  including the E-zone re-aims). Untranslated-note leaks: NONE.
  - **Bare-string trap (JA×EN/JA×DE/JA×FR precedent, checked explicitly):**
    core `content34.py` registers the P8 #37 note as the bare string
    `工艺展到11月8日` (no weekday suffix; the P3 fill-in stem, key 8),
    distinct from the NOTES-table entries `工艺展到11月8日（周日）` and
    `传统工艺展到11月8日`. The transform maps the bare string explicitly →
    `Выставка — до 8 ноября`. Printed P8 line 37 reads
    `37. 8 — Выставка — до 8 ноября`. Fact check: the P3 stem reads
    `展覧会は11月 ___ 日（日）までです。` and 2026-11-08 is a Sunday.
- **Occlusion audit** (`tools/occlusion_audit.py`, selftest first: all 6
  planted classes fired exactly once, clean controls silent): **0 flags**
  on the edition, **0 flags** on the core, **NEW vs core = 0**.
- **Builder gate script** (`audit_gates.py`, `audit_geo.py`, `frame_scan.py`,
  `p8_compare_items.py` — outputs `audit-gates-round1.log`,
  `audit-geo-round1.log`, `frame-scan-round2.log`):
  kinsoku line-start scan 0 hits; same-baseline ink collisions 0 (P1 top
  band measured with the build's own text widths: left ends 213.8, centre
  strapline 640.4–1309.6, right date starts 1529.9 — gaps 426.6 / 220.3);
  full-page right-edge advance scan 0 violations; full-page frame-line
  scan (stroked boxes + rule lines, PIL mask ink) 0 flags — the first
  naive pass flagged 239 pill-adjacency cases (exercise stems starting
  exactly at a number pill's right edge), which are adjacency, not
  border-pressing text, and were excluded by restricting the scan to
  stroked boxes; P6 chart-label mask-ink coverage worst 0.0 (gate <0.30;
  8/8 labels checked); gloss counts split on `·` match core
  (content12 [4,4,5], content34 [4,4,4,3], content56 [4,3,4]); golden
  phrases all 8 exactly 2×; SOP-banned term 0 in SVGs, 0 in build code,
  0 in ABSTRACT (audit scripts carry it only as escape sequences so the
  scripts themselves stay clean).
- **Word-level residue check:** freeze-diff added/removed review plus the
  code string set-diff above. The only Chinese-word hits in the edition
  SVGs are three shared-kanji Japanese words in frozen body text, each
  verified in context: 池袋 (Ikebukuro, P5 Japanese sentences/stems),
  漆器 (lacquerware, P3 Japanese feature + gloss headword), 金箔 (gold
  leaf, P3 Japanese feature + gloss headword + P8 key 38). No Chinese
  explanation text remains.
- **Kinsoku:** canonical svglib (md5 `d73e23b365676c3618d7e060b835eb4d`,
  `SEAM_SLACK=28`) copied verbatim, never edited (md5 re-verified in this
  build copy at close-out).
- **Flow limits:** no FLOW OVERFLOW, no HEAD TOO WIDE in the round-2 run
  log. P8 key flow ends col 3/3 y=2471 (limit 2540). P7 teaser band rect
  ends 2471.08 (limit 2540; round 1 ended 2553.12 — see fix rounds).
- **Visual check:** all 8 cards viewed (round-2 versions) — no overflow,
  overlap, footer intrusion, or clamped keys; P8 keys 145–150 fit cleanly
  in the final column; P7 phrases show no orphan tag split after the
  round-2 shortening.

## Readers' corner (verbatim, with scope ruling)

- The Japanese example letter is frozen verbatim from the core; nothing
  was invented (no fabricated names, letters, or quotations).
- The operative Russian disclosure (replacing both the Japanese disclosure
  sentence — which must not serve as the operative disclosure for Russian
  readers — and the core's Chinese disclosure, per the coordinator ruling
  applied by the JA×FR/JA×DE siblings) reads verbatim:
  `Пример от редакции, а не настоящее письмо. Настоящих писем и лучших
  сочинений со страницы 8 к сроку не пришло: всё появится в VOL.3.
  Пришлите своё письмо на японском — лучшие письма выйдут в VOL.3!`
- It states all 3 facts (the item is an editor's sample, not a real letter;
  no real letters arrived by the deadline; no best P8 compositions
  arrived) + an explicit imperative invitation + the VOL.3 promise.
- Scope ruling (quoted verbatim, range stated, not assumed): the
  invitation sentence literally covers letters
  (`Пришлите своё письмо на японском — лучшие письма выйдут в VOL.3!`);
  the same-page disclosure sentence defers the best P8 texts to VOL.3
  (`всё появится в VOL.3`), and the VOL.3 teaser line names the P8 best
  texts for VOL.3. Combined, the gate is satisfied under the pt-family
  range ruling (invitation + disclosure + teaser read together). The
  teaser line alone is not counted as the invitation.

## Furniture: three-way measurement (W45 core / W43 JA×RU / W45 JA×RU, P1)

W43 same-pairing furniture wins over README §20 generalisation. Wordmark
y=262 / 248 / 248; subtitle y=330 / 316 / 316 (40pt); badge y=— / 356 / 356
(19pt bold BRICK, centred at x=975); strapline y=372 / 390 / 390 (19pt);
double rules y=392+401 / 406+413 / 406+413; dark band y=424 in all three.
Note: the brief's JA-family reference list gave wordmark 262 — that is the
W45 core position; the W43 same-pairing SVG measures 248, and W43 wins per
the task rule, so this edition (like all W45 JA× siblings) uses 248.
Badge string is verbatim the W43 string; badge colour is BRICK per the W43
build code (the W45 JA×FR sibling's olive badge is that sibling's outlier,
not the RU precedent). Pairing visible on the P1 masthead badge and on all
8 footers. Other RU furniture (W43 JA×RU precedent, VOL.2): page line
`Страница N из 8`; gloss prefix `Пояснение — `; P8 separators
`— СТРАНИЦА N —`; P7 phrase tags `(Страница N)`; bilingual section heads
= Japanese original · Russian short form (P4 band title `スポーツ · 体育`
kept, 体育 being Japanese).

## W43 deviations (this edition vs the shipped W43 JA×RU edition)

- Footer VOL.2 (core) vs VOL.1 (W43).
- Contents table level word `全部` kept as in the core: all 10 W45 JA×
  siblings keep it; the W43 `ВСЕ` rendering was not carried into the W45
  JA family, and changing it alone would break family consistency.
- P8 E-zone re-aim JA↔ZH → JA↔RU (same pattern as W43; #138's wording
  coincides with the W43 precedent, #137 is a fresh translation of the
  W45 content).
- Fit shortenings (meanings preserved, round 2): P8/P2 match instruction →
  `Соотнесите пары` (W43 RU match precedent); clinic notes 1–2 → single
  lines; frame note → `Разбор: мягко навести порядок в себе.`; phrase #8
  translation shortened so its page tag no longer splits across lines.
- Round-2 teaser recovery (see fix rounds).

## Fix-round record (all fixes in transform.py only; pre-fix baselines kept, never reset)

- **Round 1** (`sha256-round1.txt`): 150 exercises, levels/pages/model
  chars matched core. Defects: canonical audit 2 NEW TEXTX flags (P8
  F-zone match instruction `Соотнесите слово и значение` overprinted the
  H-zone model text in the next column, 18.0px, twice); P7 teaser band
  ended 2553.12 (>2540), caused by Russian clinic notes wrapping to 2
  lines each (+53.04 in the clinic box height) — the phrases section
  itself is fixed-pitch and did not move the teaser.
- **Round 2** (`sha256-round2.txt`; `transform.py` edited, `gen_transform.py`
  mirrored so regeneration reproduces it): match instruction →
  `Соотнесите пары`; clinic notes 1–2 shortened to 1 line each; frame
  note shortened to 1 line; phrase #8 shortened. Result: occlusion audit
  0 flags (NEW vs core 0); teaser band ends 2471.08; only P2, P7, P8 SVGs
  + cards + both PDFs changed vs round 1 (P1, P3, P4, P5, P6 byte-identical).
  All gates re-run green on round-2 output (freeze added CJK 0, p8 CLEAN
  150=150 with the same adjudicated keydiff list, note-completeness NONE,
  frame scan 0, full visual pass).

## Deliverables (this directory)

- `svg/` — 8 edition SVGs.
- `cards/` — 8 PNG cards @1950×2700.
- `Lucerna-VOL2-RU.pdf` — print PDF, 8 pages, 24,786,676 bytes,
  sha256 `5eb838c079f5fce7baeb70e2071ebdcd4415d11e8b0188c29d75d568758ba46b`.
- `Lucerna-VOL2-RU-web.pdf` — web PDF, 8 pages, 3,127,591 bytes
  (under the ~10 MB server limit),
  sha256 `6ce9110d2ed9649cdccb12b0ac82bd740936f0983fab0c55d1233db9d5ae2987`.
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Russian, single line, no ASCII
  double quotes).

## Reproduction

Build dir: `hidden_files/weekly-report-w45-ja-ru-build/` (transform.py +
gen_transform.py + per-round baselines + raw gate outputs + audit scripts).
`transform.py` was generated from the proven JA×FR table for this exact core
by `gen_transform.py` (every French new-string translated to Russian; any
untranslated string aborts the generator), then fix rounds edited
`transform.py` directly. Content modules share one registry and must
re-render in ONE driver process; never import content modules inside the
core build dir; fix rounds edit transform.py only, then:

```
tools/venv/bin/python transform.py   # applies exact-literal replacements to a pristine core copy
tools/venv/bin/python run.py         # single-process render (registry shared)
tools/venv/bin/python render.py      # SVG -> cards + print PDF + web PDF
```

Interpreter record: `run.py` and `render.py` were both run with
`tools/venv/bin/python` — Python 3.12.3, Pillow 13.0.0 (all audit
measurements use the venv Pillow rendering of the SVGs). System python3 is
also 3.12.3 but has no cairosvg, so `render.py` must use the venv.
Determinism check: a scratch copy of the build (OUT repointed to a scratch
edition dir, `tools/scratch/rerun-ja-ru`) re-rendered all 8 SVGs
byte-identically to the delivered round-2 files. The shared scratch copy
was left in place (not cleaned, per standing rule); the scratch output
directory itself was my own temp output and was removed. Core build dir
was never imported or written into; core SVGs re-hashed unchanged after
every run.
