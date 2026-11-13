# WEEKLY-KIT — La Lucerna Spanish Weekly VOL.4 — es-ko

Edition: 2026-W47, target language Spanish, reader language Korean.
Issue dates 16–22 November 2026. 8 pages, 150 exercises (A2 50 / B1 72 / B2 28).
Self-check: independent proofreading round 2 (b) found 4 minor defects;
all fixed in §9 (fix1, build 3). No known defects remain.

## §1. Spec (measured, build 3 — fix1, 2026-11-11)

- Print PDF: `La-Lucerna-VOL4-es-ko.pdf` — 5,229,280 B,
  SHA-256 `f059db4ed89c374128875f5b2c1c8b76ea4b402f40c8cc40f863c9b53a9b2040`
- Web PDF: `La-Lucerna-VOL4-es-ko-web.pdf` — 1,097,508 B,
  SHA-256 `a555f282aceb71772ca483664537cb4eab85c9321be9fccdbcda2f616219a33f`
  (built only with `tools/webpdf.py`; pdftotext print = web, 48,239 B,
  byte-identical; both < 7 MB)
- 8 SVG in `svg/`, 8 PNG in `cards/`
- `2026-w47-es-ko.text.md` (1,823 lines, exported from the production
  source with the fixed `extract_text_es_ko.py`; never extracted back
  from the PDF)
- `ABSTRACT.txt` (Korean, one line, no ASCII double quotes)
- Paper #fbfaf6 on all 8 pages; masthead 196 units = 147pt; VOL.4 ×9 in
  SVG text; VOL.5 ×3 (all legitimate forward references to next week's
  issue); badge tricolour A2 #5c6e30 / B1 #46581f / B2 #37402f
- P8 badges: 35 chip rects — A2 11 / B1 21 / B2 3 — plus 1 #37402f header
  band rect (identical to core); Q113–150 all badged, none missing
  (Q113–120, Q145–149 chips present, visually confirmed)
- P8 minimum font 10.125pt (pypdf `Tm` parse, min d 10.125; 15 Tm entries,
  as in ja — CJK runs share fewer Tm operations than Latin)
- No "12 de noviembre" anywhere; no international politics
- The moth `<title>Lucerna 三色蛾</title>` (P1, inherited from core,
  invisible metadata) is left unchanged
- Korean harvest mixes "." (glosses, P8 notes) and "。" (bridges) as
  sentence terminators — cosmetic harvest inconsistency, left as
  harvested (§6.13). Full-width "＝" does not occur in ko; the P7
  word-box gloss uses half-width "=" ("debate = 토론").
- #103's note "a las 21:00(a 전치사와 함께)" lacks a space before the
  parenthesis — harvest style, cosmetic, left as is.

## §2. Per-page contents (frozen Spanish text; Korean explanation layer)

- P1 Portada: lead "La campaña arranca: trece días para el 29-N";
  five-claves box; numbers box; "LA PALABRA DE LA SEMANA « el debate »"
  with 1-line gloss "“토론”: 사람들이 공개적으로 토론해요."; quiz 7–10
- P2 Vida (A2): "La semana, día a día"; EL CALENDARIO "이번 주 일정";
  DECIR LA HORA; LOS DÍAS DE LA SEMANA; exercises 11–28
- P3 Cultura (A2→B1): flamenco + Santa Cecilia; Sargent "Bailaora
  española"; exercises 29–46
- P4 Deporte (B1): La Liga jornada 13; fixture table; exercises 47–64
- P5 Juventud (B1): first-time voting; postal vote; Black Friday;
  exercises 65–82
- P6 A fondo (B2): "Leer la campaña: debates, programas y encuestas"
  — band subtitle completed to "선거운동 읽기: 토론, 공약, 여론조사";
  RTVE minutes chart; poll-ban chart; exercises 83–100
- P7 Lengua (A2/B1/B2): LA HORA / COMPARATIVOS / EL SUBJUNTIVO;
  ERRORES TÍPICOS; LA PALABRA; CARTAS DE LOS LECTORES (sample letter,
  no real letters had arrived — editor's note, §6.5); FRASES DE LA
  SEMANA; LA PRÓXIMA SEMANA (VOL.5); exercises 101–112
- P8 Ejercicios y respuestas: exercises 113–150; RESPUESTAS with a
  Korean note per item; ✓ = model-text item (#150)

## §3. Measured totals

- run.py rc=0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- P2 col3 993.0; P3 col3 1594.75 (13px above the 1608 divider);
  P4 col3 964.5; P5 col3 1574.55 (33px above the divider);
  P6 col3 1241.55; P7 col3 1865.51 (exactly the Latin target);
  P8-keys y=2538 (22px spare); P8-ex flow y=872 (bottom 1252)
- Occlusion audit 0 flags; bridge-orphan sweep 0 over 20 bridges;
  box-vs-hline sweep 0; bridge-widow sweep 0
- p8 extract 150/150; compare CLEAN, keydiff=[137, 138] (§6.12)
- Freeze: tool 8 OK + direct sha256 of `build-copy/svg` vs shipped
  `svg/` 8/8
- Gloss-word token counts (core §8.1 method, per page): P1 reflexión 2;
  P2 mitin 2 / cartel 2 / escaño 2; P3 cante 5 / toque 6 / baile 9 /
  compás 4 / duende 5; P4 parón 2 / liderato 3; P5 papeleta 2 / censo 2 /
  plazo 3 — every Note word occurs ≥2 times on its page
- P8 multi-line items (diagnostic): 7 — #32, #44, #45, #82, #92, #139, #140
  (§6.11; §9: #45 became 2-line when its note was completed to
  `두 번째예요`); #137/#138 are 1 line each in Korean

## §4. Sources reused from core-es (frozen)

All Spanish text, facts, dates, numbers, answer keys, images
(Sargent bailaora, Jebulon ballot box, Book of Hours initial, swan pen),
and the P8 key set are byte-identical to core-es except the explanation
layer and the two re-aimed translation keys (§6.12). No new trend
research; no fact changes; the 12 November decree date was NOT
reintroduced (no second independent source, W45/W46 rule).

## §5. Build commands (all from the repo clone, tools venv)

- Apply: `tools/venv/bin/python scratch-fanout-es/apply_fanout.py ko`
  (476 literal replacements; 3 manual-over-harvest overrides)
- Pre-fixes: 12 substitutions with count assertions (see §6.1–§6.10)
- Build: `tools/venv/bin/python run.py` (builds 1–2)
- Render: `tools/venv/bin/python render.py` (~180 s)
- Gates: `tools/occlusion_audit.py svg`; `sweep_de.py .` (orphans +
  box-vs-hline + widows); `tools/p8.py extract --p8 svg/p8-ejercicios.svg
  --total 150`; `tools/p8.py compare --edition-p8 svg/p8-ejercicios.svg
  --core-p8 core-es/svg/p8-ejercicios.svg --total 150`;
  `tools/freeze.py baseline --build . --core-svg svg --out
  scratch/freeze-es-ko-2`; pdftotext print vs web; pypdf Tm parse
- Text export: `tools/venv/bin/python scratch-fanout-es/extract_text_es_ko.py
  svg 2026-w47-es-ko.text.md` (fixed extractor copy, §6.14)

## §6. Adjudications

### §6.1 Apply
476 literal replacements; 3 manual-over-harvest overrides:
"Después ___ (원형 enviar) el sobre." → "Después ___(원형: enviar)
el sobre." (manual drops the space before "("); "JUVENTUD　청소년" →
"JUVENTUD　청년" (청년 = young adult; 청소년 = teenager);
"muchísimos aficionados = 아주 많은 팬" → "= 아주 많은 팬들"
(plural marker 들). Leftover zh keys NONE; CJK in .py NONE (hangul
is outside the script's CJK U+4E00–U+9FFF scan range).

### §6.2 P1 gloss
Harvest "“토론”: 두 사람 이상이 차례대로 공개 토론하고 질문해요."
wraps 2 lines at sans 19 (469.3 units at gw). Shortened to
"“토론”: 사람들이 공개적으로 토론해요." (325.7, 1 line) — parallel to
de "„Debatte“: Menschen diskutieren öffentlich." and ja
"「討論」：人々が公開で話し合う。" The file's gloss ends with ASCII ".",
not "。" — the first substitution attempt failed on that (count 0);
the fix uses "." to match the file's gloss convention. The "two or
more / turns" detail survives in the Spanish definition above and the
P7 word-box gloss.

### §6.3 P7 word-box gloss
Harvest "debate = 토론: 차례대로 하는 공개 토론. 이번 주는 토론 주간;
선거는 29일이에요." is already 2 lines at 20 (677.8 units at CW-44) —
kept as harvested.

### §6.4 P7 ERRORES notes
All four are 1 line at 19.5 units at CW-44 — no fix needed (unlike
fr/nl/ru). Caution: my first measurement used retyped strings, not the
file's — the file's actual notes are "1시는 단수라서 동사는 es를 써요.",
"mejor 자체가 비교급이에요. más는 없어요.", "gente는 단수 집합 명사예요.
동사도 단수예요.", "creo que는 확신해요. 직설법 es를 써요." Always
extract strings from the file (ru/fr/pt lesson); the retyped versions
were wrong and briefly suggested a phantom 2-line ERR2.

### §6.5 P7 F-MAIL editor's note
"편집부 알림: 마감 때까지 실제 독자 편지와 우수 작문이 도착하지 않아서,
이번 호에는 편집부가 쓴 예시 편지를 실어요. 약속은 VOL.5로 미뤄요.
편지를 보내 주세요!" is 4 lines at both 20 and 19 — no shortening
needed, only wrap+para 20→19 for the col3 math (Δ+21 → 1865.51).
Unlike ja/pt, the "Write us!" closer ("편지를 보내 주세요!") is KEPT —
it fits in 4 lines.

### §6.6 P5 your-turn rendered at 19
"우편 투표를 할까요, 직접 가서 투표할까요? 블랙프라이데이에는 무엇을
살 거예요? 실용적인 것, 아니면 충동적인 것? 두 문장을 써서 보내세요."
is 4 lines at 20 but 3 lines at 19 (1112.3 units). Rendered at 19
(eh wrap 20→19, *29→*27, para 20→19); P5 col3 1574.55 — the clean
value, not the 1601.55 adjudicated one (unlike ja/ru, Korean fits in
3 lines at 19).

### §6.7 P3 your-turn rendered at 19; P2/P4 need no fix
P3 "플라멩코를 들어 본 적 있어요? 여러분 나라 음악 중에 두엔데가
느껴지는 음악은 무엇인가요? 두 문장을 써서 보내세요." is 3 lines at
both 20 and 19; rendered at 19 for the 13px margin (box 1594.75).
P4 your-turn 4 lines @20 (box 964.5, fixture table 1140); P2
your-turn 4 lines @20 (col3 993.0) — no fix.

### §6.8 Bridges already 1 line
Unlike ja, every Korean bridge that could orphan is already 1 line:
P2 C-intro "2면 글을 읽고 정답을 고르세요。" (266.3 @20.5), P5 A
"5면 글을 읽고 정답을 고르세요。" (266.3), P6 A "위 두 그래프를 보고
정답을 고르세요。" (317.3). P5 B/C and P6 D are 2 lines with content
on both lines (no lone punctuation — widow sweep 0). No bridge
shortening was needed at all for ko.

### §6.9 P6 band, P8 header, letter parens
Band subtitle completed to "선거운동 읽기: 토론, 공약, 여론조사"
(full sub 789.7 units in sans 18, limit 1684) — the harvest's
"선거운동 읽기" was the title only, as in ja. P8 header moved
1302→1337, keys flow 1328→1363 (right note 470.0 units wide at 19.5;
header title 681.5 units at 25 — no title/note collision).
Letter parens full-width → half-width "(ejemplo, escrito por la
redacción)". Box titles all measured against their boxes — no
pt-§6.13 overflow ("EL CALENDARIO　이번 주 일정" 271.5/422.5).

### §6.10 P8-keys 2554 on build 1
Build 1 ended y=2554 (6px spare, no OVERFLOW warning). Tightened 4
notes to 1 line each (§6.11); build 2 ends y=2506 (54px spare).

### §6.11 P8 note tightenings (build 1 → 2)
Wrap-verified at 13.5, each replaced only in its DEFINING file (ru
lesson — the #92 text also occurs in the P7 FRASES quote translation,
which keeps the long form):
- #32 (content34.py): "성녀 체칠리아 축일은 11월 22일이에요. 음악가들의
  수호성인이에요." → "성 체칠리아 축일은 11월 22일이에요." (the
  patron-saint fact is in the stem itself)
- #82 (content56.py): "올해는 MiDNI 앱으로 신분을 확인하고 투표할 수
  있어요" → "올해는 MiDNI로 투표할 수 있어요"
- #92 (content56.py only): "여론조사는 오차가 있는 사진이에요, 어느
  하루에 찍은 사진이에요" → "여론조사는 오차 있는 하루의 사진이에요"
  (keeps both "오차" and "하루"); content7.py FRASES keeps the long form
- #140 (content8.py): "tener que = 반드시 ~해야 해요" → "tener que =
  ~해야 해요"
Kept 2-line wraps: #44/#139 (core-consistent).

### §6.12 keydiff [137, 138]
Re-aimed translation keys, W45/W46 ruling (keys are the Korean
sentences "월요일은 세계 플라멩코의 날이에요. — 원문과 대조해 보세요." /
"토요일에 세비야 더비를 봐요. — 원문과 대조해 보세요."), not a defect.
Note "원문과 대조해 보세요." ("compare with the original").

### §6.13 Punctuation mixing (cosmetic)
Korean harvest mixes "." (glosses, P8 notes, P7 word-box gloss) and
"。" (bridges, some notes) as sentence terminators, and "=" vs "＝"
does not occur in ko. Left as harvested. #103's note lacks a space
before "(" — harvest style, left as is.

### §6.14 Exporter (fixed copy, hangul ranges)
`extract_text_es_ko.py` is copied from the FIXED ja extractor (§6.16
of the ja KIT — CJK-aware width + column-boundary split), with hangul
ranges U+AC00–U+D7AF and U+1100–U+11FF added to `run_w` (hangul
syllables are ~1 em wide, like CJK; the ja copy's ranges did not cover
them). Export verified: keys 1–150 all present, none >150. The
`.text.md` was read end-to-end (1,800 lines).

## §7. Self-proofread record

- Round 1 (build 1, all gates + full .text.md read + 8-page visual):
  P8-keys 2554 (6px spare) — tightened 4 notes (§6.11). All other
  gates green on build 1 (0 overflow, occlusion 0, sweeps 0/0/0,
  p8 CLEAN, freeze 8/8).
- Round 2 (build 2, final): run rc=0, 0 overflow, TOTAL 150;
  render rc=0; occlusion 0 flags; sweeps 0/0/0; p8 150/150 CLEAN;
  freeze tool 8 OK + direct sha256 8/8; pdftotext print = web 47,790 B
  byte-identical; P8 min font 10.125pt; §1.1 measured; .text.md
  1,800 lines read end-to-end; 8 pages visually inspected — all clean.
  Zero findings.

## §8. 重建（re-fanout，2026-11-11 — core build 10）

Core baseline: core-es fix build 10 (independent re-proof (a), zero findings) — print 17,212,955 B SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`, web 1,410,471 B SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`, text.md 1,822 lines SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
Method: old edition backed up to `scratch-refanout-es/backup-old/` (verified identical), deleted, re-applied via `scratch-fanout-es/apply_fanout.py`; `classify.py` diffed fresh sources against the backup line by line — KEEP = core build-10 change, REVERT = edition hand fix restored, MERGE = derbi letter line (fresh sábado + backup ASCII parens), INSERT = RTVE debate-a-ocho timeline row. No commit, no push.
Common core changes kept: C1 (P1 CINCO CLAVES box 700→720), C2 (`antes del jueves`→`hasta el jueves`), es-ja D1 (consejo completed) + D4 (derbi sábado 21st), es-nl D1/D2, es-pt C2 (PCTE kept, 195 kept). C3 (P5 vocab `content56.py:79`) left as-is per adjudication.
Gates (all green unless noted): run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; render rc=0; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated — translation items keyed by target-language sentence); freeze 8/8 SVGs byte-identical; freeze-diff CJK accounting clean; canonical creambox.py full scan 0 own-ink overflow (the 6 raw negative lines per edition are the known below-box headings, identical to core); creambox_diag 0 own-ink negatives; boxtitle 0 overflow; keycheck 149/150 (only the #150 open-question `✓` exception); sweep 0 orphans / 0 box-vs-hline; pdftotext print = web bytes; P8 min effective font 10.125pt (≥ 9.75pt floor).
Classify: KEEP 18 / REVERT 15 / MERGE 1 / INSERT 1 / DELETE 0. Build: run1 rc=0, TOTAL 150, P8-keys y=2506. New print 8,874,351 B SHA `65e3a3993f2f315f9a89c316788f6f93ed79ef69212c4b32f08f52a9976cb0f7`; web 1,237,415 B SHA `54494cef95ba3a7b98dc70aba67bd8a5cd03676106f14b6c928f38f417715351`; text.md 1,817 lines SHA `f49dd7088c16f7a40c14618019a05800b45418be8a9a137c8f83ddb8554dbc3e`; print/web text 109,956 bytes, identical.
Hand fixes re-applied: D-01 — P1 vocab note `“토론”` → `"토론"` (ASCII double quotes) and P5 C-section subtitle `‘~할 것’` → `'~할 것'` (ASCII single quotes); text.md shows 0 curly quotes; rendered crops verified straight quotes in the Latin font. D-02 — P8 #45 `두 번째예요` restored via revert (already present in the backup). P8 Q91 curly pair untouched, per proof.

## §9. fix1 (independent proofreading round 2 (b), 2026-11-11 — build 3)

Full record in `FIX-LOG.md`. Four minor defects, all in the Korean layer:

- D-01 — P8 #45 note truncated: `content34.py:101`
  `"장소가 앞에, 동사는 두 번째"` → `"장소가 앞에, 동사는 두 번째예요"`
  (full form as #44 `:99` and #133). Four-source check: source, text.md:1651,
  P8 SVG nodes (`두 번째` y=1599.78 + `예요` y=1615.44), print + web PDF text
  layer — all full form. Side effect: #45 key line now wraps to 2 lines
  (tail `예요` alone, same wrap class as accepted #44); P8-keys 2506→2538.
- D-02 — P4 D bridge dropped the Latin term: `content34.py:200`
  `e.bridge("문장을 과거형으로 바꾸세요.")` →
  `e.bridge("과거형(pretérito indefinido)으로 바꾸세요.")` (ja-parallel;
  1 line at 20.5, 381.2 units). Section title untouched.
- D-03 — P1 numbers item 13, lone `)`: `content12.py:47`
  `(선거까지 13일)` → `(선거 13일)` (sibling item 2 already bare);
  3 lines → 2, `)` back on line 2. SVG re-measured: no lone `)` at y=1414.5.
- D-04 — P2 calendar Domingo 22, `축일` split: `content12.py:185`
  `성녀 체칠리아 축일` → `성 체칠리아 축일` (§6.11 #32 precedent);
  4 lines → 3, `축일)` intact. SVG re-measured: no `일)` at y=1113.44.
  P5 plan-box item 5 (`content56.py:27`) keeps `성녀` — it wraps cleanly.
- KIT corrections: §1 build-2 SHAs → build-3 values above; §3 P5
  `papeleta` 3→2, `plazo` 4→3 (SVG count; `papeletas de verdad` is P6,
  not P5).
- Gates (all green): run rc=0 TOTAL 150; render rc=0; occlusion 0;
  p8 extract 150/150, compare CLEAN (keydiff [137, 138]); freeze 8/8;
  freeze-diff CJK clean (3,458 added); creambox 0 own-ink overflow,
  creambox_diag 0 own-ink negatives; boxtitle 0 (log identical to
  refanout); keycheck 149/150 (only #150 `✓` exception); sweep 0/0/0
  (20 bridges); pdftotext print = web, 107,964 B; P8 min font 10.125 pt.
  Orphan scan (8 SVGs): lone `。`/quote/`：`/`–` = 0, Korean lone `)` /
  lone-syllable final line = 0 (same scan on rebuild SVGs: exactly the 2
  fixed items). text.md read end-to-end (1,823 lines), keys 1–150 complete;
  8 pages visually inspected; SVG diff: only P1/P2/P4/P8 changed.
- New deliverables: print 8,873,692 B
  SHA `2c98a0f8f49e2e4519acdbe56b54702a315b0eb9777223c166775d88f86fcb43`;
  web 1,236,860 B
  SHA `2c9a90e05f99fe3a4ed024878bb229fac46042644e1bf57fef4d06e11ec0f008`;
  text.md 1,823 lines / 47,385 B
  SHA `a24b79b064896d11b6ba57f5b8f6d0f12047816b78551c76ec93a141787123d6`.
  Print SHA stable across two renders; web PDF bytes vary run to run
  (first render `e3f25c33…`) — record the on-disk SHA.
- Core-es untouched (tree hash `8651a818…` before = after). No commit, no push.

## D5 重建记录（2026-11-12，B档）

- 安装：`mechanism/apply_variant.py --svglib <本版>/svglib.py --target es --reader ko`（mode=cjk，按字符文字分流，不加 `_READER_LANG` 门）；`svglib.py` md5 `6a46ee51…` → `4010cae9…`（安装器同时补 port 了 fix2，CJK 索引 SC→KR）；路由断言 10/10（`route_assert.py`，mode cjk）；机制 `test_d5_routing.py` FAILURES: 0；修前基线：印 8,873,692 B `2c98a0f8…`、网 1,236,854 B `39f6a7e9…`；D5 普查 347 violations（与裁定 §1.1 预期 347 一致）；boxtitle 0 DEFECT；occlusion 0。
- 预修 3 项共用版式（与 core-es 相同西班牙语串、同栏宽）：P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt、P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt、P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。
- 逐项修 2 项（均为 D5 新缺陷，修前基线 0；CJK 类：拉丁头在 Newsreader SemiBold 下加宽，把韩语尾顶出框）：P1 框题 `LA SEMANA EN CIFRAS　이번 주 숫자` +23.7px——该框 `tsize=21`（余量 13.3px）；P5 框题 `EL PLAN DE LA SEMANA　이번 주 계획` +37.9px——该框 `tsize=20`（21pt 余量仅 0.3px，取 20 求稳）。以上文字均未动。注：ink=advance（尾字为全角 CJK），框题可用宽 404.5px。另：首建 run.py 在服务重启中完成（TOTAL 150，日志核实无溢出），render.py 重启后补跑，产物均为原地重建。
- 门禁全绿：run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0（`head_check.py` PASS 0 defects）；render rc=0；D5 普查 0（弯引号 4 个全在 Newsreader 内，合规）；U+201C 普查（`census_quotes.py`）0（KR 引号不扩展，裁定 §3）；occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，仅读者语译注差异）；boxtitle 0 DEFECT；creambox（仓内 `tools/d5_creambox_audit.py`）PASS 0 defects（P8 191 行、页脚余量 52.0px 不变）；spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8（venv 下通过，未触发 ko Pillow 10 例外——本版为 es-target × ko-reader；系统 python3 已核实有 Pillow 10.2.0 备用）；freeze diff vs core-es 新增 CJK 字符 3,458 个——为韩语读者层相对 core-es 中文读者层的正当差异；同版 freeze diff（修前基线 vs 新版）新增 CJK 字符仅 1 个 U+3000（run 拆分 artifact）；印/网文字层 39,805 字符、7,949 词一致。
- 新 PDF：印刷版 5,229,280 B SHA `f059db4ed89c374128875f5b2c1c8b76ea4b402f40c8cc40f863c9b53a9b2040`；网页版 1,097,508 B SHA `a555f282aceb71772ca483664537cb4eab85c9321be9fccdbcda2f616219a33f`。`text.md` 字节不变（SHA `a24b79b0…`）。日志：`hidden_files/w47/scratch-d5-rebuild-es/2026-w47-es-ko/`。

## es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）

- 改动：F2（P6 时间轴措辞：`(sin el PSOE)` → `(sin el PSOE confirmado)`，与正文一致）。F1（缺首字下沉）按协调员裁定不修：全刊引擎级缺口，进模板 backlog，见 FIX-LOG。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 更新（core-es 为 D5 工具重导出；其余 10 版手术替换，diff 只含意改行；ru F4 另做词级手术，见 FIX-LOG 陷阱核查节）。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ko.pdf` 5,229,281 B，SHA-256 `e2ae545b1462d436c68e9715a03e9fd2b3ec65f8a451a04f42d5423302466f34`；网页版 `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,497 B（< 7 MB），SHA-256 `fad91509e34fdd2b2c41ac51737d728e328f2688a95064a8fdba6c39d28e7804`；text.md `2026-w47-es-ko.text.md` 47,403 B，SHA-256 `8407be401bb75e89cadb678c40845ee38715dcdb00a912c9ffbacb6b7eac70cf`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 38 titles, 604 body lines，0 DEFECT；spill 0 SPILL（27 盒，149 candidates）；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8；印/网 pdftotext 48,250 字节逐字节一致。
- 日志：`hidden_files/w47/scratch-fix-es/`（FIX-LOG.md、build-all.log、build-resume.log、gates-all.log、text-pre/）。

## 第四轮独立重校修复 I1（2026-11-12，PROOF-NOTE-4 §2 返修）

- 改动：I1（text.md 专属，低）：两栏/两块拼接处丢空格致文字粘连；本版共 7 处（与 PROOF-NOTE-4 表列一致）：分版粘连 0 处（无）；目录粘连 7 处（`Pág. 2La semana` … `Pág. 8Ejercicios y respuestas` → 各补空格）。
- 重建：未重建（PDF 未动）；text.md 手术替换 7 处（逐处先断言原文存在再替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 7 行，行数不变（1824 行）。
- 文件：text.md `2026-w47-es-ko.text.md` 47,403 B（I1 前 47,396 B，+7 B）、1824 行，SHA-256 `8407be401bb75e89cadb678c40845ee38715dcdb00a912c9ffbacb6b7eac70cf`（改前 `981d43e9183762028d62283832c69866ec963ba7f8a94b1b0152a2da8b57d581`）；印/网 PDF 未动，SHA 不变（印 `e2ae545b1462`、网 `fad91509e34f`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；D5 普查 PASS（弯引号 4/4 在 Newsreader）。
- 日志：`hidden_files/w47/scratch-fix4-w47-es/`（FIX-LOG-4.md、fix.py、fix2.py、fix-report.json、text-pre-*.md、gates4.sh、gates4.log、p8-extract/compare、census）。
