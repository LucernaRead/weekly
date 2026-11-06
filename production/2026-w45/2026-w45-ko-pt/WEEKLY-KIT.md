# WEEKLY-KIT — Lucerna Weekly VOL.2, KO×PT (Korean target × Portuguese reader)

**Status: builder-complete only — NOT finalized. Finalization is the independent
proofreader's decision; this builder does not declare the edition shippable.**
**Issue week: Mon Nov 2 – Sun Nov 8, 2026. Masthead: `Lucerna` with no article
(Korean takes none).**
**Delivery: `files/weekly-report-w45-ko-pt/` — svg×8, cards×8, print PDF, web PDF,
this KIT, ABSTRACT.txt.**
**Build tree: `hidden_files/weekly-report-w45-ko-pt-build/` — `transform.py` (all
fixes live here), `orig/` (pristine core copies), `baselines/` (per-round pre/post
sha256, never reset), `audit_extra.py`, `spy_wrap.py`, `spy/` (wrap-spy scratch
run), `baseline-check/` (pristine-copy baseline proof).**

## 1. Delivery files

| file | bytes | sha256 |
|---|---|---|
| Lucerna-VOL2.pdf (print, 8 pages) | 32,555,491 | `f315aef01943e344cb145448fafbd43554c04f2781cf33ea3ace070ea34a194e` |
| Lucerna-VOL2-web.pdf (web, 8 pages, < 10 MB SOP target) | 3,549,551 | `de4b0e153d0984f1e19be45025652ddcb922058c1689d9052e648a7d589c8267` |

SVG sha256 (final, round 4):

| page | sha256 |
|---|---|
| p1-pyoji.svg | `509422dfa7796bc5e84687e4d05b2dde84e208e7648696236a70ab76a2c64ea2` |
| p2-saenghwal.svg | `92c6d473a6590845dc20262ad85b64a6c954cd7ebd54d08202f742f70a36b38f` |
| p3-munhwa.svg | `3b3fb3a3d744658cfa0352166f976f00de24c665d6047a5b40a408309ba62aee` |
| p4-seupocheu.svg | `4555177272ef95d3a64f7b93246c3fc405b70c8a527965e7821b98eec7a95efc` |
| p5-cheongnyeon.svg | `047e5b42413112b448f5c52ea35a3ecf98b29e49ff7034136978d368d6baf603` |
| p6-gipi.svg | `c4733fb9b868360d4bc35662d5b0eb707ff0597f40676b6b30ef2926791bbe31` |
| p7-mal.svg | `a8a06609705b4d1eb4868b1d661208fade5af650ae2c49fc5f8111321e3999de` |
| p8-siheom.svg | `93789a30d633831db07ef84dc1a57068a146a9bd458a12682d030ef4411e0240` |

Card PNG sha256 (final): p1 `339ed8ea7d59e653f47263104e1352d667fcacd25dbba1c07b09d1ff86659a43`,
p2 `0917f753fa8ef22ee7cd27f0c8c97605ec38d5541322d63243d1b8ce77d0d26f`,
p3 `f3464c4569dc1dcbb4953e97d2c4b5adc129ee5a5e6c8cbfc9d42954534c7035`,
p4 `65b4cc439307bc7b8f69d29fc19a6102752d73e7939a4f6d61d2e0965a610734`,
p5 `de14cee6765297426da48f87586f52a85767e57c9c12cc6d07fb067199de2a35`,
p6 `fb2ac5bbc9cd477a9e0f6d5437142bf55b8c6b28757b87930b210a32957f0586`,
p7 `28791c19cfc355549374f6e03e549e04a70c775be58ff8d6a56023ec5efa8148`,
p8 `92237aa2efd31b140abea50f922a0513e8f714090321d295bb78be6b5926ceea`.

## 2. Toolchain (both interpreters recorded; audit measurements use the venv)

- `run.py`: tools venv Python 3.12.3, PIL 13.0.0. Verified: a scratch copy of the
  build tree (OUT redirected to scratch) run with the venv reproduces all 8
  delivery SVGs byte-identically.
- `render.py`: tools venv Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1 (system python3
  is 3.12.3 with PIL 10.2.0 and has NO cairosvg — it was NOT used for rendering;
  render.py runs under the venv, always).
- Canonical tools used: `freeze.py`, `p8.py`, `occlusion_audit.py`, plus the
  supplementary `audit_extra.py` (this build tree) for the advance-edge,
  frame-line, same-baseline, P6-label-coverage and Korean-orphan scans the
  canonical audit does not cover.
- **p8.py version: sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`
  — the adopted new version (dash branch verified TRUSTED).** No file under
  `tools/` was modified by this build (only `tools/scratch/` baseline outputs
  were written, which is the designated scratch area).

## 3. Core measured numbers (measured from the KO core on disk/render, never copied)

- VOL.2; page spec 1950×2700, 4 columns; masthead `Lucerna`, no article.
- Lead theme: Ipdong week — last foliage weekend, kimjang/winter-prep opening,
  CSAT countdown (D-17 on Nov 2 → D-12 on Nov 7; CSAT-day measures dated Nov 19
  only, never this week).
- TOTAL 150 exercises; by page 10/18/18/18/18/18/12/38; by level A2 51 / B1 72 / B2 27;
  by type: sentence completion 48, multiple choice 52, vocabulary matching 16,
  cloze choice 13, sentence building 8, sentence transformation 4, true/false 4,
  translation 4, writing 1.
- P8: 38 items (A 8, B 8, C 4, D 4, E 4, F 4, G 5, H 1); P8 printed-note set 150/150;
  dash style `N. key — note`; group headings in Korean, `— 제N면 —`.
- Writing model: 157 characters with spaces excluded, printed instruction 150–200자.
  Model text begins `나의 겨울 준비는 김장부터 시작해요.` and is frozen verbatim.
- P7 structure: A2 입동의 말 / B1 날짜 세는 말 / B2 예보 읽는 법 columns (4 exercises
  each, 12 total); error clinic ×4; frame `〜부터 〜까지` (산불조심기간 example);
  readers' corner with an editor's example letter plus disclosure; 8 phrases of the
  week, each verified verbatim against its tagged article page; VOL.3 teaser band.
- P7 phrase occurrence counts across the whole issue (including P7 itself):
  5 / 2 / 4 / 2 / 2 / 2 / 2 / 2 (see §8 for the phrases).
- Gloss inventory (rendered `gloss()`/`glossline()` call strings split on `·`,
  tools README #21; per-call counts verified equal core vs edition, §7):
  content12 21, content34 19, content56 20, content7 6 — total 66 items.
  NOTE on the W45 KO×DE KIT's "84" figure: it is NOT reproducible from
  `gloss()`/`glossline()` calls under this definition — the same AST count run on
  the shipped KO×DE build files also gives 21/19/20/6 = 66. This KIT therefore
  reports the reproducible 66 with its definition stated, and does not copy the 84.
- Footers (core, all 8 pages): left `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY`,
  right `제 N 면 / 총 8 면`, baseline y=2624.
- Images per page (payload sha256 prefixes of base64 text; decoded-JPEG prefixes
  also recorded in §12): P1 1 (`535fff46b7ce`), P2 1 (`e66d2b455ec6`),
  P3 2 (`e266b6ee1a87`, `5bea45d1f81e`), P4 1 (`1a7e7d6d5ffc`),
  P5 1 (`6a1bab177d54`), P6 0, P7 0, P8 0.
- svglib line-break rules (unchanged — target language unchanged): `NO_START`
  includes the KO core's own ASCII closer set, `NO_END = "「『（【〈《([{"`;
  greedy wrap, Latin words kept whole where possible, CJK per character,
  word-boundary preference when the fragment after the last space fits within 45%
  of max width, plus kinsoku oidashi (max 8 moves).
- Core SVG sha256 (verified unchanged after every round; final re-check §11):
  p1 `f1e6913d5fbcc0985fcf34f481814bb5756f3efc2aae29c1040ad9c85a1f9b5e`,
  p2 `839dcdd0ae4d603ff6ef4b786c6496f0f8f9263a061ccd2387d86f5e6b6509c1`,
  p3 `7437117949a3da0aad1d3084b6efed963687be1b8379ee93f27fd8991a899b34`,
  p4 `7f0aed9bec64dbb3f6596e1a20e7e815212706f417f565463624f2b9caad0902`,
  p5 `68e6ead94a42ec478633b1499889d8d71a28f03aca54b04264098bc561785ce9`,
  p6 `e7f53e421500d0a3a199b290c97b8fdd6ee7d425e92b1ebdfd8adb85af7ba39a`,
  p7 `ddb4e76cf4e978156e04eb0ca86db7c4c237f3dd07feee36996314ec01db6594`,
  p8 `17031514098198758075ee9654f5cf179fa1767902002c1698c4b95a8b646401`.

## 4. Trend-first check (core theme is living seasonal/calendar heat, not commemoration)

Corroborated by the core KIT's own trend pool (`hidden_files/w45/trend-batch-C.md`,
KO section) and promises register (`hidden_files/w45/w43-promises.md`): 입동 Nov 7,
last foliage weekend, kimjang opening, CSAT countdown — all calendar/seasonal heat
for Nov 2–8, 2026. No anniversary framing, no international politics anywhere
(Korean domestic topics only, as in the core).

## 5. Build method

Copy of the core build to the ko-pt build tree; `transform.py` regenerates all build
files from `orig/` (pristine core copies) every round, repoints OUT/BASE to the PT
edition directory, then applies assertion-checked exact-literal replacements. All
fixes go only into `transform.py`; re-render is always single-process `run.py`
followed by venv `render.py`. Registry `type` arguments stay byte-identical
(internal keys, W45 ES×DE precedent); only rendered strings (instr, notes, heads,
boxes, gloss, band lines) change. P8 answer-generation code is untouched.
Line-based/exact-literal splicing only (never AST byte offsets); f-string fragments
get bare text, never repr literals. No build-tree script was ever run in a way that
writes back to the delivery or core directories; the wrap-spy run lived only in
`spy/` with OUT redirected, and it reproduces the 8 delivery SVGs byte-identically.
No subagents were spawned; no Discord post, no main-chat card/PDF dump, no cron,
no `weekly-git` touch, no W43/core directory modification (read-only对照).

## 6. Furniture three-way comparison (W45 core / W43 ko-pt / this edition)

W43 same-pairing measurements win over README #20 generalization wherever they
differ. All W43 values below were measured from the shipped W43 ko-pt files
(`files/weekly-report-ko-pt/svg/p1-pyoji.svg` et al.), NOT copied from ko-en
(17pt olive) or ko-de/ko-fr (20pt BRICK is shared here, but the string is ko-pt's
own). The W43 ko-pt badge geometry coincides with the README #20 KO-case majority
form; the badge STRING is ko-pt's own.

| slot | W45 core | W43 ko-pt | this edition |
|---|---|---|---|
| subtitle y | 372 | 366 | 366 |
| badge | — | INSERTED y=394, 20pt bold BRICK `#a4553a`, sans | y=394, 20pt, weight 700, `#a4553a`, sans — string verbatim from W43 |
| rules y | 392 / 401 | 412 / 421 | 412 / 421 |
| dark band rect y | 424 | 433 | 433 |
| band texts y | 478 / 522 | 487 / 531 | 487 / 531 |
| everything below y=606 | — | unmoved | unmoved |
| top strip PT segment | — | `Toda semana` | identical |
| footer | `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY` | VOL.1 form | `Lucerna · SEMANÁRIO COREANO VOL.2 · TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS` |
| page line | `제 N 면 / 총 8 면` | `Página N de 8` | `Página N de 8` (all 8 pages, baseline 2624) |
| gloss prefix | — | `Nota — ` | `Nota — ` |
| band titles | 생활 / 문화 / 스포츠 / 청년 / 깊이 읽기 / 말 공부 / 시험과 답 | 생활 · Vida cotidiana etc. | 생활 · Vida cotidiana, 문화 · Cultura, 스포츠 · Esporte, 청년 · Jovens, 깊이 읽기 · Leitura aprofundada, 말 공부 · Língua, 시험과 답 · Teste e respostas |
| exercise heads | 연습 | `연습 · Exercícios pág. N` | `연습 · Exercícios pág. N` |
| exercise right line | — | `Respostas na pág. 8 · Os exercícios misturam os níveis: procure pelo número` | identical |
| P1 quiz right line | — | `Leia a primeira página e escolha a resposta certa · Respostas na pág. 8` | identical |
| P8 header | 답 | `답 · Respostas — ordenadas por página, procure o número` | identical |
| P8 header right line | — | `Cada resposta com uma breve nota em português · ✓ = exercício com modelo` | identical |
| P8 band sub-line | `제8면 · 이번 주의 큰 시험 + 모든 답` | Korean-only | Korean-only (unchanged) |
| contents P8 level | 全部 | `Todos` | `Todos` |
| P7 band sub | — | `Três níveis, três temas` | identical |
| P7 glossline format | — | `=` separator | `=` separator (e.g. `남다 = restar, faltar · 바로 = exatamente`) |
| PT number formats | — | thousands with dots (551.864 / 1.312 / 3.271 / 27.000); decimal comma in prose (415,5 mm) | identical convention |
| instr labels | 填空 / 造句 / 翻译 / 写作 / 改写 / 把词和释义配对 / 把词和说明配对 / 把山和说明配对 | Complete / Monte / Traduza / Escreva / Reescreva / Associe | identical mapping |
| P6 V/F instruction | Korean 맞다/틀리다 wording | `Se for verdade, escreva O; se for falso, X.` (W43 answer-letter convention) | This issue's keys ARE 맞다/틀리다, so the instruction names them: `Se a frase estiver certa, escolha 맞다; se estiver errada, 틀리다.` |

Badge string (verbatim, W43 ko-pt):
`TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`

## 7. Gates — measured values (final outputs)

### Freeze (core → edition, final run)
P1 +20/−19 strings, CJK 1462→1339; P2 +44/−39, 1612→1360; P3 +34/−31, 1524→1346;
P4 +28/−25, 1232→1074; P5 +38/−35, 1433→1234; P6 +23/−19, 1276→1136; P7 +40/−40,
1365→1046; P8 +176/−169, 2496→1238. **TOTAL added CJK characters: 7, all on P7, all
Hangul syllables cited inside Portuguese notes** (울×1, 에×2, 서×2, 났×1, 만×1 =
`서울에서 만났어요` in clinic note 4 + `에서` in clinic note 1) — adjudicated legal
per tools README #3 (ko fan-outs legitimately add Hangul citations; the gate is
the per-char list, not zero). All other pages: 0.
Baseline proof: `freeze.py baseline` on the pristine `orig/` copies reproduced all
8 core SVGs byte-identically (8/8); the shipped core was re-hashed after every round
and is unchanged (§11). (A baseline run against the already-transformed build tree
returns 0/8 by construction — it is not the proof; the `orig/` run is.)

### P8 compare (explicit dual paths, `--total 150`)
- Path 1 (`--core-dir` / `--edition-dir`): core 150 noted, edition 150 noted,
  status CLEAN, missing=[], extra_count=0, keydiff=[137, 138].
- Path 2 (`--core-p8` / `--edition-p8`): identical result, CLEAN, keydiff=[137, 138].
- Adjudication of every keydiff item against the printed line:
  - **137**: genuine E-redirect Portuguese key — printed
    `137. O dia 7 de novembro é Ipdong. — Veja a pág. 1`.
  - **138**: genuine E-redirect Portuguese key — printed
    `138. Faltam 12 dias para o exame. — Veja a pág. 5`.
  - #139/#140: no keydiff (Korean keys byte-identical); #150: apparatus line, not a keydiff.
- P8 note-completeness comparison (core vs edition numbered key lines 1–150):
  every core note is localized to Portuguese; no untranslated note survives.
  Identical non-numbered lines: only the 8 frozen Korean group headings
  (`— 제N면 —`) and frozen Korean stems/keys (including #139/#140 keys) —
  adjudicated individually, all frozen target-language text, not notes.
- Edition P8 key lines containing Han: 0 (Han in rendered PT text is 0 on ALL 8 pages).
- Core P8 notes that mix a Korean headword with a gloss (e.g. `김장=腌过冬泡菜 a`,
  `이기다的过去式이겼어요`) keep the Korean headword with the gloss localized
  (e.g. `김장=kimchi para o inverno a`, `O passado de 이기다 é 이겼어요`).

### Canonical occlusion audit (`occlusion_audit.py`)
Selftest OK (all 6 planted classes fired, clean controls silent).
**Edition 0 flags; core 0 flags; NEW vs core 0** (final round-4 run;
`occlusion-new4.json` in the build tree).

### Supplementary scans (`audit_extra.py`, venv PIL, 4× supersampled baseline-anchored ink)
- ADVANCE right-edge scan (inner frame x=1910): **0 flags**.
- Frame-line scan (every text ink box vs every rect border and line element; footer
  rule y=2580 vs footer baseline 2624 exempt by design): **0 flags**.
- Same-baseline scan (0.6 px tolerance, ink-interval overlap): **0 flags**.
- P6 table-label coverage vs later-drawn rects (true ink, gate <30%): all labels
  **0.0%**, worst 0.0%.
- Korean orphan scan (wrap-spy log, 943 wrap calls, scratch copy only; delivery SVGs
  reproduced 8/8 byte-identically by the spy run): line-start NO_START **0**,
  mid-word splits with ≥3-syllable tails **0**, mid-word splits with 1–2-syllable
  tails (info) **0** — all junctions are word-boundary breaks. Coverage includes
  reflowed Korean text (Portuguese gloss boxes shift subsequent Korean paragraphs
  between columns) and every Korean furniture string; the Portuguese explanation
  layer is not subject to the Korean scan. This edition adds no new Korean
  furniture strings.
- Rendered-line window scan (consecutive rendered lines, spacing window 10–45 px,
  same column): 658 candidate pairs — line-start NO_START (Korean) **0**,
  line-start orphan punctuation **0**. The window covers P8 answer lines
  (~15 px pitch) as well as prose columns.
- P1 brief `(6면)` fragment check: renders on the sentence line
  (`11월 2일은 D-17, 7일은 D-12예요. (6면)`, y=2218.8) — the core round-2 fix is
  preserved; no lone `(6면)` line exists anywhere.

### Geometry / flow (final run log)
Zero FLOW OVERFLOW / HEAD TOO WIDE (grep count 0). Flow ends: P1-headline 1413/1828,
P1-weekend 2094/2290, P1-quiz 2521/2540, P2-feature 1417/1540, P2-ex 2258/2580,
P3-feature 1290/1560, P3-ex 2234/2580, P4-feature 1022/1180, P4-ex 2002/2580,
P5-feature 1268/1560, P5-ex 2256/2580, P6-feature 1119/1180, P6-ex 2195/2580,
P7 columns 1062/1029/1059 (bottom 1560), P7 col3 ends 1746.94, **P7 teaser ends
2520.94 (< 2540)**, P8-ex 463/1252, **P8 key-flow ends col 3 y=2425 (< 2540)**;
P8 key max baselines per column 2530.3 / 2516.7 / 2514.9 / 2408.9 (all < 2540).
(P3/P5/P6-ex and P8-keys flow ends differ from KO×DE's values because Portuguese
notes wrap differently; all are within their bottoms with zero overflow.)

### Counts / images / phrases / gloss survival
- TOTAL 150; levels A2 51 / B1 72 / B2 27; pages 10/18/18/18/18/18/12/38; model 157 chars — all
  = core.
- Image payloads per page = core exactly (1/1/2/1/1/0/0/0 with matching hashes, §3/§12).
- Phrase frequencies = core exactly (5/2/4/2/2/2/2/2).
- Gloss headwords: every Korean headword survives in the render (per-call item counts
  EQUAL core vs edition, §3; headword check 66/66, 0 missing).
- Banned intermediary term: **0 hits** in the rendered SVGs, the build code,
  ABSTRACT.txt, and this KIT (grep-verified after writing, both script forms plus
  the English and Portuguese words).
- Han ideographs in edition SVGs: **0** on all 8 pages.

### Visual inspection
All 8 final cards viewed in full (p1–p8), not a subset. No overlaps, no cut-off text,
no misplaced boxes found. P7 readers'-corner solicitation sits with its second line
(`8!`) below the letters-box border and clear of the phrases rule (see §9 for the
geometry); P8 answer columns read cleanly to the footer rule.

## 8. P7 phrases and Portuguese translations

| Korean phrase (frozen) | Portuguese translation | tag |
|---|---|---|
| 11월 7일은 입동이에요 | O dia 7 de novembro é Ipdong. | 1면 |
| 절정에 가까운 주말이라고만 말할 수 있어요 | Só se pode dizer: um fim de semana perto do auge. | 1면 |
| 김장은 겨울 내내 먹는 김치를 담그는 일이에요 | Kimjang é conservar kimchi para o inverno. | 1면 |
| 수능까지 17일 남았어요. 오늘이 D-17예요 | Faltam 17 dias para o exame. Hoje é D-17. | 2면 |
| 낮은 길은 더 늦게 물들어요 | Os caminhos baixos ficam vermelhos mais tarde. | 3면 |
| KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요 | O KIA venceu o LG Twins com três vitórias seguidas. | 4면 |
| 온 나라가 수험생을 응원해요 | O país inteiro torce pelos candidatos. | 5면 |
| 날짜를 먼저 보세요 | Olhe primeiro a data. | 6면 |

P7 target-language definition prose stays Korean verbatim; only the explanation layer is
localized (glosslines, clinic notes, frame note, letters notes, phrase translations).
P7 word-box definition sentences are NOT localized (KO-family freeze rule: the Korean
definition sentences stay verbatim; only their glosses become Portuguese).

## 9. P7 readers' corner — ruling

- Korean example letter frozen verbatim (begins `안녕하세요. 저는 대학생이에요.`); no
  invented names, letters, or quotations.
- Disclosure apparatus replaced by Portuguese blocks (W43 ko-pt precedent: the
  disclosure apparatus is replaced with reader-language notes):
  - Short note: `Exemplo da redação, não é uma carta de verdade.`
  - Disclosure (contains all 3 facts + the VOL.3 promise):
    `Até o fechamento, não chegaram cartas de verdade nem os melhores textos da pág. 8.
    O exemplo fica; a promessa anterior vale para o VOL.3.`
  - Solicitation (imperative, verbatim):
    `Envie sua carta e seu melhor texto da pág. 8!`
  - Scope ruling: the solicitation literally covers BOTH letters and best P8 texts.
    The teaser line itself is NOT counted as a solicitation; the frozen Korean teaser
    body says `여러분의 편지와 8면 쓰기 우수작도 실어요` (your letters and the p.8
    writing best works) — so the VOL.3 teaser promise and the letters-corner promise
    are consistent, and both must be honored in VOL.3.
- Teaser title: `다음 주 · Na próxima semana (VOL.3)`; teaser body stays Korean.
- Letters-box geometry (documented, not hidden): the core's box-height formula
  undercounts actual render height by ~26 px, so the core's own last disclosure line
  also sits below its box border. For this edition, two real audit flags had to be
  cleared in sequence: (1) the first solicitation wording wrapped `texto da pág. 8!`
  onto the phrases rule (NEW LINEX — baseline only 4.2 px above the rule, and the
  `p` descender crossed it); (2) the reworded first line then straddled the box
  border (NEW BOXTITLE — ink bottom 1741.3 > border 1738.9). Fixes, both in
  `transform.py` only: the solicitation was reworded so its second line is the
  descender-free `8!`, and the box-height formula's trailing constant went +26 → +34,
  threading the border through the inter-line gap (line-1 ink bottom 1741.3 <
  border 1746.9 < line-2 `8!` ink top ~1750.4; phrases rule 11 px below line-2 ink).
  No baseline moved; col3 ends 1746.94, teaser ends 2520.94 (< 2540).

## 10. P8 E-zone redirect (core KO↔ZH → this edition KO↔PT)

| # | stem | key | note |
|---|---|---|---|
| 137 | Korean (frozen) `11월 7일은 입동이에요. → ___` | Portuguese `O dia 7 de novembro é Ipdong.` | `Veja a pág. 1` |
| 138 | Korean (frozen) `수능까지 12일이 남았어요. → ___` | Portuguese `Faltam 12 dias para o exame.` | `Veja a pág. 5` |
| 139 | Portuguese `Medidas especiais valem só no dia 19 de novembro. → ___` | Korean byte-identical | `Veja a pág. 6` |
| 140 | Portuguese `No sábado, vou a Naejangsan ver a folhagem de outono. → ___` | Korean byte-identical | `Veja a pág. 3` |
| 150 | writing prompt (frozen) | `(pergunta aberta — o modelo está abaixo)` | `O modelo está na seção H desta página (157 caracteres)` |

E-zone item numbers verified from the core render (137/138), not copied from
ko-en/ko-de/ko-fr (which coincide here, but the check was done against the core).

## 11. Rounds 1–4 fix log (baselines archived per round, never reset)

- Round 1 (initial render): transform's final Han check caught one missed literal
  (the long P8 variant `青松现场庆典11月4日起`, distinct from the shorter P3 variant
  `现场庆典11月4日起` — the transform had only the short form; the long form was
  added). Round 1 also exposed `!! FLOW OVERFLOW [P1-headline] col 2 y=1743 need 99
  bottom 1828` (the Portuguese P1 gloss wrapped to 4 lines; core: 3) and
  P7 teaser 2594.98 (> 2540; col3 1820.98 vs core 1738.94).
- Round 1 → 2 diff: p1, p7 SVGs changed (plus downstream PDFs/cards). Fixes: P1 gloss
  shortened to exactly 3 wrap lines at 20.5pt/398px
  (`입동 = Ipdong · 절정 = auge · 김장 = kimchi de inverno · 상륙하다 = chegar à costa ·
  온대저기압 = ciclone extratropical.`); P7 col3 shortened by 3 lines (clinic notes 1
  and 3 to one line each, disclosure to 4 lines) → col3 1738.94, teaser 2512.94,
  exactly the core values; zero FLOW OVERFLOW / HEAD TOO WIDE. Round 2 occlusion
  audit found 1 NEW flag: LINEX on P7, solicitation line 2 overprinted by the
  phrases rule (see §9).
- Round 2 → 3 diff: ONLY p7 SVG, p7 card, both PDFs changed. Fix: solicitation
  reworded to `Envie sua carta e seu melhor texto da pág. 8!` (second line `8!`,
  descender-free). Round 3 audit cleared LINEX but found 1 NEW flag: BOXTITLE on P7,
  solicitation line 1 straddling the letters-box border (see §9).
- Round 3 → 4 diff: ONLY p7 SVG, p7 card, both PDFs changed. Fix: letters-box height
  formula trailing constant +26 → +34 (see §9). Round 4: all gates in §7 pass.
- Baselines: `baselines/round-1-post.sha256` (SVGs only — cards/PDFs not yet
  rendered), `round-2-post.sha256` (SVGs + cards + PDFs), `round-3-post.sha256`,
  `round-4-post.sha256` (full set). Each round's pre-fix baseline was recorded in
  full before the fix.
- Core untouched: final core SVG hashes match the §3 record exactly (all 8 pages).
- Two transform pitfalls found and fixed (do not re-introduce): (a) the P8 long/short
  `现场庆典` pair (above); (b) Korean glosslines end with ASCII `.`, not `。`
  (the P7 lines with `。` are genuine and were left alone); (c) substring-order
  hazards in shared note pairs: the longer `特别…` form before the bare `措施…`
  form, the longer `KIA三连胜晋级` before bare `三连胜晋级`, and the parenthesized
  `日期不同因标准不同（3版）` before bare `日期不同因标准不同` — all handled by
  fully-quoted literal matching (a quoted pattern cannot match inside a longer
  quoted string, which is what protects the E-zone stems).

## 12. Image credits (Wikimedia Commons API Artist field, every image actually placed)

No new images were introduced: payloads are byte-identical to the core (base64-text
and decoded-JPEG hashes both match, §3), so the credit lines below are the core's
frozen Artist-field lines, verified placed on their pages:

- P1 autumn.jpg — lumoplank, CC0 (file photo, not Seoraksan). Caption notes it is a
  file photo. Base64 `535fff46b7ce`, JPEG `6f7f33ed8f`.
- P2 ssam.jpg — wizdata, CC0 (ssam vegetables, not a kimjang photo). Caption notes it
  is not a kimjang photo. Base64 `e66d2b455ec6`, JPEG `96a6a19b61`.
- P3 bukhansan-ui.jpg — Udonhan1992, CC0; apples.jpg — Cézanne, public domain.
  Base64 `e266b6ee1a87` / `5bea45d1f81e`, JPEG `158ea3a0e8` / `214cc390ac`.
- P4 baseball.jpg — Bain News Service, public domain (file photo).
  Base64 `1a7e7d6d5ffc`, JPEG `18ad8ae06f`.
- P5 study.jpg — Gary Todd, CC0 (file photo). Base64 `6a1bab177d54`, JPEG `35e7dc69d4`.
- P6/P7/P8 carry no photos. All captions carry the `자료 사진` (file photo) note where
  the image is a file photo.

## 13. Deviations from W43 ko-pt (itemized)

1. VOL.1 → VOL.2 everywhere (footer, top strip, contents, P8 header context).
2. Issue week, dates, theme, phrases, model text, and image set are the W45 Ipdong
   week, not W43's week (all values in §3 are W45 measurements).
3. E-redirect item numbers and key wording are this issue's (137/138 Portuguese keys,
   §10); the redirect pattern itself is identical to W43 ko-pt.
4. P8 keydiff is exactly [137, 138]; W43's run also had exactly {137, 138, 150-as-
   apparatus} with the same structure. No paren-group artifact surfaced here (unlike
   W45 KO×DE's #109).
5. P1 gloss box is 3 lines in Portuguese (round-2 fix, §11); the W43 gloss box needed
   no re-shortening.
6. P1 calendar line shortened to one Portuguese line
   (`Estas cinco datas sustentam a edição.`, 18.5pt/390px); W43 ko-pt's calendar line
   needed no such fix (the DE build's round-3 TEXTX precedent motivated the
   one-line form).
7. P7 letters-box height formula +26 → +34 (§9); W43 ko-pt needed no formula change
   (its last line was CJK-free of descender issues in the same way the W45 core is).
8. P7 readers'-corner solicitation is a single imperative covering letters AND best
   P8 texts (§9); W43 ko-pt's letters box promised VOL.2 publication of real letters
   + best P8 text in its teaser, and this issue's disclosure carries that promise to
   VOL.3 instead.
9. P6 V/F instruction names 맞다/틀리다 explicitly (§6); W43 ko-pt's P6 used the O/X
   answer-letter convention because that issue's keys were O/X.
10. NOT deviations (verified identical to W43 ko-pt): badge string and geometry,
    subtitle/rules/band geometry, footer/page-line wording pattern, gloss prefix,
    band-title pattern, exercise heads and right lines, P8 header and right line,
    contents P8 level `Todos`, P7 band sub, P7 glossline `=` format, Portuguese
    number formats, instr-label mapping, P8 band sub-line kept Korean-only.

## 14. Open items (for the parent line, not this builder)

- Independent proofread has not happened; this edition is builder-complete only.
- Repo insertion is the parent line's serialized step; this builder did not insert,
  push, or post to Discord.
- Nothing was sent into the main chat; no cron was created; `weekly-git` was not
  touched; the W43 directories and the core directory were read only.
- Unresolved observations (carried, not invented):
  - (a) The letters-box height formula undercounts render height by ~26 px in the
    core itself; this edition threads its border through an inter-line gap (§9).
    A future core revision could fix the formula properly (account for the
    para-return pitch), which would move the border and the phrases rule together.
  - (b) The KO×DE KIT's gloss figure "84" is not reproducible from
    `gloss()`/`glossline()` calls (both builds give 66); if the programme wants a
    single gloss definition, it should be fixed in tools/README #21 explicitly.
  - (c) Core open debts carry over unchanged (Korean Series G1 Nov 2 start may shift;
    playoff G1 Oct 26 result unknown at cutoff; Champi record claim omitted; 입동/소설
    from calendar blogs; 한능검 details from secondaries; Commons image shortfall) —
    see the core KIT.
