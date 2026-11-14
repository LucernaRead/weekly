# WEEKLY-KIT — 2026-w43-it-ko (Italian text × Korean explanations)

- **Edition:** La Lucerna VOL.1 W43 (2026-10-19–25) — target **Italiano**,
  reader native **한국어 (Korean, 해요체)**.
- **Status: PASS** (independent proofread complete 2026-10-22 — one
  explanation-layer defect found and fixed, full pass re-run clean;
  see §11. Awaiting repo insert by the parent line).
- **Deliverables (this dir):** `svg/` ×8, `cards/` ×8 (1950×2700 PNG),
  `La-Lucerna-VOL1-KO.pdf` (print), `La-Lucerna-VOL1-KO-web.pdf` (web).
- **Source core:** `files/weekly-report-it-vol1/` (IT core VOL.1, Chinese
  explanations), build `hidden_files/weekly-report-it-build/`.
- **This build:** `hidden_files/weekly-report-it-ko-build/` (copy of the core
  build; OUT repointed — every content module's `os.path.expanduser` line and
  `render.py` BASE now aim at `files/weekly-report-it-ko/`; OUT printed and
  verified before first run; no module was ever imported or run inside the
  core build dir).

## §1 Freeze / baseline evidence

- `tools/freeze.py baseline` on the pristine core build: **8/8 SVGs
  byte-identical** to the shipped core (bd04af2f…, ff75206e…, 9ce43c3d…,
  aac8356c…, 079552c8…, 5d553abe…, 9b4daf76…, 58f37fd4…).
- Core SVG sha256 re-verified **unchanged after all work** (8/8 OK against
  the pre-work snapshot `scratch/core-svg-hashes-before.txt`).
- `freeze.py diff` (final): added strings containing Han characters = **0**;
  added CJK characters total 3,250, **100 % Hangul syllables** (334 distinct,
  all in U+AC00–U+D7A3); removed-side strings = Chinese explanation strings
  only, plus 20 adjudicated exceptions, all non-content:
  - 8 × P8 separators `— PAGINA n —` → `— 제 n 면 —` (furniture, §3);
  - 8 × language-neutral Italian conjugation notes whose only Chinese
    content was full-width punctuation (`：`→`: `, `（）`→`( )`):
    #15, 16, 17, 19, 60, 61, 102, 103 — char-level diff verified;
  - 4 wrap-reflow line fragments of mixed Italian+explanation lines
    (P5 piano rows ×2, P6 expl word-list ×1, P7 B2 expl ×1): the Italian
    segments are byte-identical in the edition code; only the line-break
    positions moved because the Korean segment's length differs.

## §2 Method

- Counted exact-string transform (`scratch/transform.py`): **266 asserted
  (old → new, count) pairs**, sequential simulation (substring-safe order),
  applied to bslib4.py + content12/34/56/7/8.py; then 5 small counted fix
  patches (`scratch/transform2.py`, `transform3.py`, inline patch4–6,
  all recorded in §9). `bridge()` renamed `expl()` (20 call sites + def).
- Only the explanation layer was replaced. Italian body text, exercise
  stems, options, the model essay, image captions and credits are frozen.
- One driver process (`run.py`) for every render (registry in one process).

## §3 Furniture register (KO column standard, target name 이탈리아어)

1. P1 top-strip centre: `WEEKLY IN ITALIAN · 매주 발행 · 이탈리아가 읽는
   이탈리아어`.
2. P1 serif line (46 pt): `이탈리아어 주간지 · VOL.1 · L'ORA SOLARE ·
   IL MALTEMPO · IL CINEMA`.
3. P1 dark-band right lines (gold): `이번 주 일요일, 한 시간 더 자요` /
   `표준시로 바뀌는 밤 · 2면 참고`.
4. **Badge adjudication — NO inserted badge line.** Measured from the
   shipped core P1: the y=372 slot carries the frozen Italian tagline
   (`IL GIORNALE SETTIMANALE PER IMPARARE — …`), and the only other gap
   (band bottom 542 → headline head 606) is the headline section's own
   lead-in. This matches the DE×KO precedent on the same bslib4 P1
   architecture (no inserted badge; proofreader-accepted). The pairing is
   carried visibly by items 1–3 above plus the footer on all 8 pages
   (item 6). (FR×KO's inserted badge at y=574 rested on different core
   geometry and does not transfer.)
5. Band left titles: `VITA · 생활`, `CULTURA · 문화`, `SPORT · 스포츠`,
   `GIOVANI · 청년`, `APPROFONDIMENTO · 심층`, `LINGUA · 언어`,
   `VALUTAZIONE E RISPOSTE · 연습과 정답`; band subs carry short Korean
   suffixes (e.g. `· 표준시와 날씨`, `· 2027년 예산안`, P7 sub head
   `언어 집중 ·`).
6. Footer (every page): left `La Lucerna · 이탈리아어 주간지 VOL.1 ·
   텍스트는 이탈리아어 · 해설은 한국어`; right `제 {n} 면 / 총 8 면`.
7. Gloss prefix (bslib4 `gloss()`): `해설 — ` (code-added; gloss strings
   carry no own prefix — no doubles).
8. Explanation lines via `expl()`; section heads keep the core's Italian
   head + short Korean suffix (`ESERCIZI · 제 N 면 연습`,
   `DIRE L'ORA · 시간 말하기`, box titles likewise short: §9 lists the
   three titles shortened after audit flags).
9. P8: answers header `RISPOSTE · 정답 — 면별로 정리했어요. 번호를 찾으면
   돼요`; right note `문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안
   문제예요`; separators `— 제 {pg} 면 —`; answer lines keep the IT
   family's dash style `{n}. {key} — {note}` (answer-generation code
   byte-identical to the core; writing items print `✓ {note}`).
10. Type labels: 문장 완성 60 · 객관식 49 · 빈칸 채우기 13 · 단어 짝짓기
    12 · 문장 만들기 7 · 번역 4 · 읽기 판단 3 · 문장 전환 1 · 쓰기 1.
    Instr labels: 빈칸 채우기 · 판단 · 문장 만들기 · 번역 · 쓰기 ·
    단어와 뜻 짝짓기.

## §4 Manovra honesty disclosure — two spots (family rule)

The DPB chart's components (5,0 + 5,0 + 3,4 = 13,4 mld) are NOT the manovra
total (≈23,5 mld). Both disclosure spots preserved:

1. **P6 chart area** — the frozen Italian caption inside the chart box
   reads verbatim `Tre voci pubblicate nel DPB del 15 ottobre — non è il
   totale della manovra (circa 23,5 miliardi).` (byte-identical to the
   core; verified present in the edition SVG), and the chart's Korean
   explanation layer is in place: title `LE CIFRE DEL DPB · DPB의 숫자
   (Documento programmatico di bilancio, 15 ottobre 2026)`, right box
   `LE PREVISIONI 2027 · 2027년 전망`.
2. **P8 answer #85** — printed line: `85. B — 5 + 5 + 3,4 = 13,4
   (합계가 아니에요)` ("…(it is not the total)"), with #86
   `86. A — 5 − 3,4 = 1,6` beside it (see §5 for #86's neutrality).

## §5 Registry — totals, printed set, key diffs

- Totals: **150 = A2 46 · B1 71 · B2 33**; per page 10/18/18/18/18/18/12/38
  — identical to the core registry (one-process dump compared field by
  field: levels all equal).
- Printed-note set: `p8.py extract` on the shipped core P8 = **150 of 150**
  (the IT core prints every note); the edition forces the same set.
  `p8.py compare` (final): **CLEAN** — core 150 noted, edition 150 noted,
  missing = [], extra = 0.
- **Registry key diffs (authoritative byte-compare): exactly 3**, all in
  the allowed classes:
  | # | class | core key | IT×KO key |
  |---|-------|----------|-----------|
  | 137 | translation item (IT→reader language) | 周日我们多睡一个小时。 | 일요일에 우리는 한 시간 더 자요. |
  | 138 | translation item (IT→reader language) | 展览一直开放到四月。 | 전시는 4월까지 계속 열려 있어요. |
  | 150 | writing-device item | （开放题，范文如下） | (열린 문제예요. 모범 답안은 아래에 있어요) |
  Translation items #139/#140 keep their Italian keys; their Chinese
  **stems** became Korean (`토요일 18시에 나폴리–로마 경기가 열려요. →
  ___`, `모든 숫자에는 출처가 있어야 해요. → ___`) — stem re-aim class.
- `p8.py compare` also listed keydiff candidates [12, 37, 58, 72, 78,
  101]: **line-level extraction artifacts** (README #13 pattern) — the
  registry byte-compare shows those keys (`mezza`, `castagne`,
  `più bella`, `muti`, `ci saranno`, `Sono`) identical to the core.
- Notes: 149 of 150 translated to Korean; exactly one note is
  byte-identical by design — **#86 `5 − 3,4 = 1,6`**, pure arithmetic,
  language-neutral (checked item-by-item against the core registry).

## §6 Gloss census (brief hard rule: every entry kept)

5 `gloss()` boxes, entry counts identical to the core, item-by-item,
Italian terms identical and in the same order (script-verified):

| page | core entries | IT×KO entries |
|------|----|----|
| P2 | 5 (ora legale, ora solare, tramonto, allagamenti, abituarsi) | 5 |
| P3 | 5 (tartufo, sagra, profumo, arrosto, pittrice) | 5 |
| P4 | 4 (giornata, sfida, presentazione, in trasferta) | 4 |
| P5 | 4 (braccialetto, coda, anteprima, muto) | 4 |
| P6 | 5 (manovra, rinvio, miliardi, deficit, previsione) | 5 |
| **total** | **23** | **23** |

## §7 P7 verbatim check

- The 8 `FRASI DELLA SETTIMANA` quotes are byte-identical Italian to the
  core, each with its Korean translation and the core's own `(Pagina N)`
  tag (tags kept in Italian, as in the core — they are part of the frozen
  quote apparatus; script-compared: quotes equal, tags equal, count 8=8).
- P7 col-3 measured end: **1674.0 — exactly the core's value** (after the
  §9 trims); no contact with the FRASI rule at y=1686.

## §8 Mechanical gates — final measured results

- `freeze.py baseline` 8/8 (§1); `freeze.py diff` adjudicated (§1).
- `p8.py compare` CLEAN (§5).
- `occlusion_audit.py` (selftest OK first): **0 flags** on the edition
  (core also 0). First pass had flagged 4 Korean-introduced items — all
  fixed by shortening the Korean (§9), none by touching Italian or
  geometry constants.
- Same-line ink-collision scan (README #10 method, `scratch/gates.py`):
  **0 collisions** (core 0). Ink outside the page frame: none.
- P6 chart-label element check (README #12): all 3 bar labels end exactly
  18 px before their bar start; all 3 value labels start exactly 18 px
  after their bar end; label coverage by bars = 0 %.
- Orphan punctuation: 0 Korean orphan lines. One rendered line ends with
  `(` (P5 piano row 3) — the parenthesis pair spans the wrap exactly as
  in the shipped core (which ends the same line with `（`); inherited
  core geometry, not a Korean defect.
- Residual scans on the printed paper: Han characters **0**, Cyrillic
  **0**, Dutch furniture (`van`/`Uitleg`) **0**, banned intermediary term
  **0** in the paper and in operative code. (Correction, proofread
  2026-10-22: the §2 rename record quotes the old method name once, in
  backticks, as a code identifier — the same disclosed form as the
  shipped EN×RU/FR×RU/JA×RU KITs; the earlier "0 in KIT" phrasing was
  inaccurate and is corrected here. The one scratch transform script
  quotes the core's original call strings as search patterns — confined
  to `scratch/`, disclosed in §2.) (One Han word survives in an
  unused `svglib.py` illustration docstring — library file byte-identical
  to the shipped core and to the shipped DE×KO/FR×KO builds; never
  printed.)
- Calendar: frozen content follows the core's verified 2026 Europe/Rome
  facts (ora solare Sun Oct 25 03:00→02:00; Manovra 2027; Lucca Oct 28–
  Nov 1). No explanation introduces international politics.
- Flow reports: no FLOW OVERFLOW, no HEAD TOO WIDE on the final run;
  col-3 ends P2 933.5 / P3 1560.9 / P4 905.5 / P5 1572.8 / P6 1096.5 /
  P7 1674.0 — all inside their regions.

## §9 Self-proof — defects found and fixed (all fixes shorten Korean only)

1. **P1 headline flow overflow (21 px)** — Korean growth measured block by
   block against the core: the `expl()` line wrapped 3→4 lines and CIFRE
   box rows 1/2/4 wrapped 2→3 lines. Trimmed (wrap-verified): expl line
   drops `(국가)` and the final `이에요`; row parentheticals shortened to
   `(토요일→일요일 밤 25시간)`, `(일요일 새벽에 변경)`,
   `(이번 주말 세리에 A 8라운드)`. Overflow cleared.
2. **P7 col-3 boxes +117.5 px vs core** (would strike the FRASI rule at
   y=1686) — six Korean glosses trimmed (ERRORI rows 1/3/4, PAROLA and
   LETTERE paragraphs, then ERRORI rows 2/4 once more after line-count
   measurement). Final col-3 end 1674.0 = core exactly.
3. **Occlusion BOXTITLE ×3** (first audit pass): box/section titles whose
   Korean suffix outgrew the box —
   `LA SETTIMANA IN CIFRE · 숫자로 보는 이번 주` → `· 금주 숫자` (two
   steps, final overhang was 1.8 px);
   `화요일 검색어 · Cosa cerca l'Italia (Google Trends)` → `화요 검색 · …`
   (final overhang 6.5 px);
   `LA FRASE PER RICORDARE · 암기 문장` → `· 암기` (overhang 1 px).
   README #15 applied: the explanation layer yields, never the geometry.
4. **Occlusion LINEX ×1**: the P1 PAROLA Korean paragraph wrapped so its
   last line was the orphan `에요.` touching the y=1864 rule (the core's
   own patched rule, KIT §13 of the core). Shortened to one line:
   `'악천후': 강한 비와 바람, 폭풍. 이름은 Adam이에요.`
5. **Citation fidelity**: the P7 B2 `expl()` line initially rendered the
   core's Italian citation separators `/` as commas; restored to the
   core's exact Italian segment (`è possibile che / bisogna che / è
   importante che … so che, scrivono che …`).
6. Full visual proofread of all 8 cards after fixes: Korean glyphs render
   completely (no tofu/missing glyphs; Noto CJK face as in the shipped
   DE×KO/FR×KO editions), 해요체 consistent, no text strikes, boxes,
   bands and footers clean on every page.

## §10 Measured pins (final artifacts)

- Print PDF `The-Lucerna-VOL1-it-ko.pdf`: 9783110 bytes (D5 rebuild),
  sha256 `d8aa2a1bd8cd341986e6d0fd6e307e83ba84eceae36e3438bdfca2b1b4ddaf12`
- Web PDF `2026-w43-it-ko.web.pdf`: **1391994 bytes (< 7 MB)** (D5 rebuild, tools/webpdf.py shipped file),
  sha256 `2ba5a801da277f3b8b572919c349ef9b4b0b7f51633fbd4a5eebe2c0590a0549`
- (Pins superseded by the §11 proofread fix, 2026-10-22; pre-fix pins
  were print 13,551,260 / `93e18b46…`, web 3,536,014 / `76bdf156…`,
  p2 SVG `4a7a2981…`.)
- SVGs (sha256 prefixes): p1 `929adedc19da783b…`, p2 `bf31e5ff6e87339c…`,
  p3 `c034f56a2eee18ed…`, p4 `5eb557519a040383…`, p5 `39f6e7023d67a0a3…`,
  p6 `ab5e8ca6dc7697ea…`, p7 `a83e4fb125de7fc5…`, p8 `0d3d476fccf0bb2a…`
- Cards: 8 PNGs at 1950×2700 in `cards/`.

**Status: PASS** — see §11 for the independent proofread record; not yet
inserted into the repo, no Discord post (parent line handles insert).

## §11 Independent proofread record (2026-10-22)

Independent proofreader; all builder claims re-derived, none taken on
trust. Scratch: `hidden_files/proof-it-ko/` (repointed copies of both
builds; no module ever imported or run inside the core build dir).

- **Tools (all independently re-run):** `freeze.py baseline` on the IT
  core build **8/8 byte-identical**; shipped core SVGs re-hashed
  unchanged at close (8/8). `freeze.py diff`: added CJK 3,250 chars,
  334 distinct, **100 % Hangul syllables, Han added = 0**; removed-side
  strings without Han = 19, adjudicated item-by-item (8 P8 separators,
  8 conjugation notes #15/16/17/19/60/61/102/103 whose only Chinese
  content was full-width punctuation — char-level diff verified against
  the edition, P5 piano rows ×2 + P6 expl word-list ×1 wrap fragments;
  the 4th fragment, P7 B2 expl, carries Chinese and sits in the
  Chinese-removed bucket — consistent with §1's count of 20).
  `p8.py extract` on the shipped core P8 = **150 of 150**; compare
  **CLEAN 150=150**, missing=[], extra=0. `occlusion_audit.py`
  (selftest first): edition **0 flags**, core 0, NEW vs core 0.
- **Registry (byte-compare of one-process dumps from repointed copies):**
  totals **150 = A2 46 · B1 71 · B2 33**, pages 10/18/18/18/18/18/12/38,
  page/level diffs none. **Key diffs exactly {137, 138, 150}** (137/138
  faithful Korean translations of the Chinese translation-item keys;
  150 writing-device, half-width parens). #139/#140 keys byte-identical
  Italian; stems re-aimed to Korean, verified in code and in the shipped
  P8 SVG (faithful renderings of the core stems). **Notes: 149
  translated; the only unchanged note is #86 `5 − 3,4 = 1,6`, pure
  arithmetic** — verified byte-identical. Type labels map 1:1
  (60/49/13/12/7/4/3/1/1, matching §3.10).
- **p8.py line-level keydiffs [12 37 58 72 78 101] all falsified per
  README #13**: registry keys (`mezza`, `castagne`, `più bella`, `muti`,
  `ci saranno`, `Sono`) byte-identical; differences sit inside the
  translated notes only.
- **All 150 keys re-derived by hand from the Italian text** (articles,
  fixture table, DPB chart, reading passage, dialogue): zero
  discrepancies. Chart arithmetic re-computed: 5,0+5,0+3,4=13,4 (#85 B),
  5−3,4=1,6 (#86 A); model essay = 90 words (in the 80–100 brief).
- **Manovra disclosure, both spots verified in the shipped SVG:**
  P6 caption `Tre voci pubblicate nel DPB del 15 ottobre — non è il
  totale della manovra (circa 23,5 miliardi).` byte-identical to the
  core, plus Korean chart furniture in place; P8 line 85 prints
  `85. B — 5 + 5 + 3,4 = 13,4 (합계가 아니에요)`.
- **P6 chart element check:** all 27 filled rects byte-identical to the
  core; the 3 value labels start exactly 18.0 px after their bar ends
  (714.875→732.875, 512.15625→530.15625, 406.396875→424.396875);
  label coverage 0 %.
- **KO column furniture (§3 register vs shipped SVG, verbatim):**
  top strip, 46 pt serif line, dark-band gold lines, footers on all 8
  pages (`La Lucerna · 이탈리아어 주간지 VOL.1 · 텍스트는 이탈리아어 ·
  해설은 한국어` / `제 N 면 / 총 8 면`), P8 header + right note,
  separators `— 제 N 면 —` ×8, gloss prefix `해설 — ` single
  (double-prefix count 0), dash-style P8 (`{n}. {key} — {note}`, writing
  item `✓ note`) confirmed from the core content8.py code (README #8).
  **Pairing visibility adjudication: ACCEPTED without an inserted badge
  line** — the four carriers (top strip, serif line, dark-band lines,
  per-page footers) are all in place and unambiguous; the P1 y=372 slot
  carries the frozen Italian tagline, matching the DE×KO precedent.
  (FR×KO/ES×KO use the inserted-badge form on different core geometry;
  both forms meet the SOP's visible-pairing rule.)
- **Geometry backstops:** same-baseline ink scan (README #10 method,
  tools' true-ink boxes): 0 pairs with gap < 3.0, edition and core.
  Builder self-fixes verified in place: shortened box titles
  (`· 금주 숫자`, `화요 검색 · …`, `· 암기` present; long forms absent);
  P1 PAROLA Korean line single-line at y=1846.3 with no rule contact;
  P7 col-3 lowest baseline 1668.95 = core exactly, FRASI rule at 1686
  clear (ink end ≈1674.0); P5 piano row 3 ends `le code(` — the
  half-width twin of the core's `（`, inherited geometry, accepted.
  P5 word bank reflows (line 2 lands atop column 2) — text verbatim,
  flow mechanics, no overlap.
- **Gloss census (hard rule):** 5 boxes, **23 entries**, Italian term
  sequences identical to the core item-by-item and in order
  (5/5/4/4/5). (One parser artifact: the Korean gloss for `i miliardi`
  begins with the numeral `10억`.)
- **P7:** 8 FRASI quotes verified verbatim-contiguous against the
  issue's own articles; `(Pagina N)` tag counts identical
  {1:2, 2:2, 3:1, 4:1, 5:1, 6:1}; VOL.2 teaser and the readers'-letters
  promise preserved in Korean.
- **Calendar (Europe/Rome, real 2026):** Oct 19 Mon, Oct 24 Sat,
  Oct 25 Sun (ora solare 03:00→02:00), Oct 28 Wed, Nov 1 Sun
  (Ognissanti), 2027-03-28 Sun — all match the paper. No explanation
  introduces international politics (Italian domestic budget story is
  the frozen core's own content).
- **Residuals:** Han = 0 and Cyrillic = 0 in all 8 shipped SVGs; Dutch
  furniture 0; the banned intermediary term 0 in paper and operative
  code (KIT/scratch disclosure per the §8 correction). `svglib.py` is
  byte-identical to the core build's; its unused illustration docstring
  carries the Han word 重阳， which reaches no SVG/PDF text (Han scan
  above) — accepted as disclosed.

### Defect found and fixed (1, explanation layer only)

- **P2 gloss widow:** the P2 `gloss()` box wrapped so its last line was
  the single syllable `요.` (tail of `abituarsi 익숙해지기예요.`) — the
  same orphan class the builder fixed on P1, and §8's "0 Korean orphan
  lines" claim did not hold. Fix (proofreader, in the repointed copy,
  single-driver re-render): `…abituarsi 익숙해지기예요.` →
  `…abituarsi 익숙해지기.` (dictionary-form gloss, consistent with the
  box's noun-style entries). Only p2-vita.svg changed; the other 7 SVGs
  and 7 cards are byte-identical after the fix; registry unchanged.
  Full gate set re-run on the fixed tree: freeze diff clean (added CJK
  now 3,248), occlusion 0 flags, p8 compare CLEAN, same-line scan 0,
  orphan scan clean (remaining ≤3-char lines are type/instr labels and
  P8 answer-flow syllable tails — normal Korean wrapping, as in the
  core's own answer flow). The same one-line edit was applied to the
  build of record (`weekly-report-it-ko-build/content12.py` line 181).
  Final pins are the corrected §10 values above; the fixed P2 card was
  visually verified (gloss closes on its third line, no widow).

**Verdict: PASS** — final full pass after the fix found zero problems.
Slug for insert: `2026-w43-it-ko`.

---

## §12 D5 重建记录（2026-11-13）

D5 + §1.1 合并重建记录（2026-11-13；一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑；不 commit、不 push；独立重校另派他人）。

- 装机：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production`（core-it 落盘 `_D5_READER = "latin"`）；本版 `apply_variant.py --svglib <版>/svglib.py --target it --reader ko --week 2026-w43`，`_D5_READER = "cjk"`；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（U+201C/U+201D/U+2019 → serif）保留。
- 基线：run TOTAL 150、0 警告；SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout SHA 一致（12736868 B）；修前普查 D5 拉丁 340 / 西里尔 0 / 弯引号 CJK 0。
- 二次修复（只动字号，文字零改动；盒修法行号指 tsize 行，D19）：`content34.py:22` P3 头 25→22; `content12.py:48` P1 盒 `LA SETTIMANA IN CIFRE　금주 숫자` tsize 23→21（385.4，余 19.1px；22pt 仅余 0.8px 太薄，不取）; `content12.py:91` P1 `IN QUESTO NUMERO　이번 호 차례` p.text 24→22（381.6，余 18.9px；23pt 仅余 1.5px 太薄，不取）。
- P8：行数 229→229，距页脚线余量 44.3 px；p8 compare CLEAN（keydiff [137, 138]）。
- 新交付物：印 PDF `The-Lucerna-VOL1-it-ko.pdf` `d8aa2a1bd8cd341986e6d0fd6e307e83ba84eceae36e3438bdfca2b1b4ddaf12`（9783110 B；修前 `121a32b854d0e2b6257b710a72afadf8b52ad19ef01538d637314eb612422318`，12736868 B）；网 PDF（tools/webpdf.py）`2ba5a801da277f3b8b572919c349ef9b4b0b7f51633fbd4a5eebe2c0590a0549`（1391994 B；已发版 `6262d77239e789726525bba2aecd83a3c1ca3dd4ff987ebde4e80e02da2d1121`，1564485 B）；text.md 与 fanout `.text.md.new` BYTE-IDENTICAL（57415 B，SHA `a978d3549e9e5b66790b3735e275b468871821fb0a5ef7579d5413fd5d488157`），W43 it issues/ 内无已发 `.text.md`，closer 落仓时新建补入。
- 门禁 run2 ALL-GREEN（18 门：run TOTAL 150 / head_check 0 / d5 census 0/0/0 / render RC=0 / webpdf RC=0 / occlusion 0 / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff 新增 CJK TOTAL 0 / spill 0 / boxtitle 0 DEFECT（38 titles、458 body lines）/ edge 0/0 / creambox PASS 0 defects（n=387）/ 文字层 print=web 多重集差 0 / census_quotes 0 defective / 家族 gates.py N/A / 刊头间距 552.0 px PASS）。日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-ko/GATES-SUMMARY.txt`；D5 报告：`production/notes/2026-w43/g-it/scratch-d5-rebuild-it/D5-REPORT-2026-w43-it-ko.md`。
- 本 KIT 交付物行已更新为以上 D5 新值；旧针脚为旧配方值，已过期，以上实测发运值为准。
