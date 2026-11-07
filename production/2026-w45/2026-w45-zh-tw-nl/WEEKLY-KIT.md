# WEEKLY-KIT — 2026-w45-zh-tw-nl

**Pairing:** Traditional Chinese target · Dutch reader (zh-tw × nl).
**Issue week:** Nov 2–8, 2026. **VOL.2.** **Slug:** 2026-w45-zh-tw-nl.
**Status:** BUILT, FIX ROUND APPLIED 2026-10-28 (NOT finalized — full reproof follows; see §11).
**Delivery dir:** `files/weekly-report-w45-zh-tw-nl/` (svg ×8, cards ×8, print + web PDF, ABSTRACT.txt, this KIT).
**Build dir:** `hidden_files/weekly-report-w45-zh-tw-nl-build/` (bslib4.py, svglib.py, run.py, render.py, content12/34/56/7/8.py, assets/, build.log, checks.log, checks2.log).
**Transform script:** `hidden_files/weekly-report-w45-zh-tw-nl-transform.py` (exact-literal replacements with count assertions; repoints OUT/BASE from `weekly-report-w45-zhtw-core` to `weekly-report-w45-zh-tw-nl`; render PDF names repointed to `Lucerna-VOL2-NL.pdf` / `Lucerna-VOL2-NL-web.pdf`).
**Checks script:** `hidden_files/w45-zhtw-nl-checks.py` (same-baseline scan, chart-label check, gloss counts, P7 phrases, image payloads, Traditional union check, Latin inventory).
**Pre-flight (coordinator ruling, NO CONCURRENT WRITER):** delivery/build dirs did not exist at start (fresh = trivially clear); `ps` showed no live weekly/run/render workers writing to them. Recorded before any build step.

## 1. Core baseline (reproduced FIRST, before any change)

`tools/freeze.py` baseline on the pristine core copy: **8/8 byte-identical** to the zh-tw core SVGs; core SVGs re-hashed unchanged afterwards. Core SVG SHA-256:

| page | SHA-256 |
|---|---|
| p1-front | 4672c972763b0eaf249bff952cd777d9941cc2a801928bfb1edd1e0e4558d047 |
| p2-life | 889fb533ef3ff62ecc820d3d92dc4aed10e353f5dcf9487c9d844fd2dad3cee3 |
| p3-culture | 508703c2b3c313c6853a17e452e2d55629e0933a94905211f5f53425619bab42 |
| p4-sport | e04b62ea6211c9ffabeb90a1a94faa5b3bcea3503b19a7fbd6473546a88f86f1 |
| p5-youth | 4dfce72d88000fbc9d4f43f441a9f7525ec05165e812ab2df0b6a8bac6eea30f |
| p6-deep | 06ba4c6627cb81655e02b8ad7656676e3b258e3b0763dfde7e5ec29e7174c838 |
| p7-lang | 00ac7f57125fcc094ce850712a5d302df891600062fa8cbc0c47bd7a5243192c |
| p8-test | e6e97d02595aef3bb1a3c60dd852d190e387f647a547527cc24153eeea0b41ed |

Core counts (authoritative, from the zh-tw core KIT): **150 exercises total** — A2 44 · B1 74 · B2 32; by page P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38; by type 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Core P8 is DASH style (`N. key — note`); fan-out keeps dash style, answer-generation code byte-identical except note strings translated. P8 writing model 138 characters; item 150 key `(開放題,範文如下)` frozen.

## 2. Freeze diff, final render (core → edition, `--strict-cjk`)

| page | +strings / −strings | CJK core → edition | added CJK |
|---|---|---|---|
| p1 | +23 / −22 | 952 → 920 | 0 |
| p2 | +37 / −35 | 1018 → 996 | 0 |
| p3 | +41 / −38 | 1088 → 1065 | 0 |
| p4 | +33 / −32 | 831 → 809 | 0 |
| p5 | +41 / −40 | 1101 → 1079 | 0 |
| p6 | +41 / −37 | 942 → 921 | 0 |
| p7 | +86 / −87 | 808 → 788 | 0 |
| p8 | +194 / −186 | 1114 → 1094 | 0 |
| **TOTAL** | | | **0** |

Strict-CJK added = 0 on all 8 pages. CJK decreases are the badge/footer strings replaced by Dutch furniture (see §4).

## 3. Traditional-independence cross-check (HARD GATE — passed)

Method: extract the CJK character set from (a) the edition's 8 SVGs, (b) the zh-tw core's 8 SVGs, (c) the W43 zh-tw-nl shipped SVGs (`files/weekly-report-zh-tw-nl/`), all from the shipped files themselves. No Simplified→Traditional conversion, no OpenCC, no mapping table of any kind was used anywhere in this build.

- Edition CJK chars: 772. Core: 773. W43 zh-tw-nl: 790. Union (core ∪ W43): 1030.
- **Edition chars outside the union: 0.**
- **Edition chars not in core: 0.**
- Core − edition = only `解`, which occurs in core ONLY in the badge/footer strings `英語講解` (P1 badge + every-page footer) — both legitimately replaced by Dutch furniture per the NL precedent. No target-text character lost.
- Any Simplified-only character in target text: none found. Target Traditional text is ZERO difference from the zh-tw core at run level (freeze diff added CJK = 0 corroborates; the only CJK delta is the furniture strings above).

## 4. Furniture three-way (core · W43 zh-tw-nl · this edition)

Badge slot measured from the zh-tw core P1 and the W43 zh-tw-nl P1 (NOT assumed from the zh-cn family):

| element | zh-tw core | W43 zh-tw-nl | this edition |
|---|---|---|---|
| P1 badge slot | y=378, 21pt bold, OLIVE #3e4c2a, centered x=975 | same slot/size, BRICK #a4553a | same slot/size, BRICK #a4553a (in-place replacement) |
| P1 badge string | core EN badge | `TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS` (1256.8 px sans bold 21; core badge 1227.3 px — fits) | identical to W43 string |
| Footer | core EN footer | `Lucerna · CHINEES WEEKBLAD VOL.2 · TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS` / `Pagina N van 8` | identical to W43 footer (VOL updated) |
| Gloss prefix | `Notes — ` (core) | `Uitleg — ` (W43 build code, NOT tables.json generic) | `Uitleg — ` |
| P8 separators | core geometry | `— Pagina N —` | `— Pagina N —` at core's 12.8pt/1.12/gap1 (W43 used 13.3pt; W45 geometry wins) |
| P8 keys header | core EN | W43 NL form | `答案 · Antwoordsleutel — in paginavolgorde, met een korte Nederlandse noot bij elk item` |
| P8 right note | core EN | W43 NL form | `Alle noten in het Nederlands · ✓ = het modelantwoord` |
| P8 note style | DASH (`N. key — note`) | DASH | DASH (unchanged) |
| Masthead | Lucerna, no article (Chinese is article-less) | Lucerna, no article | Lucerna, no article |
| Edition line | `繁體中文版 · VOL.2 · 2026年11月2日(一)至11月8日(日) · 台灣 / 香港` | — | unchanged (frozen core) |

Bilingual section heads keep Traditional first + Dutch second (W43 pattern, e.g. `本週大事 · Deze week`, `你呢? · Nu jij`, `讀者園地 · Lezershoek`, `本週句式 · Zinspatroon`, P7 B2 head `B2 · 港台說法 · Lokaal taalgebruik`, phrases head `本週金句 · Zinnen van de week — woord voor woord uit de artikelen van dit nummer`).
Instructions: Fill in → `Vul in` (60 occurrences in core sources: 54 instr + 5 `填一填 · Fill in` heads + 1 P8 C head; transform applies the P8 C head in §11 first, then global count 59); Match → `Koppel` (×4); Writing → `Schrijven` (3 total: P8 F head + glossline prefix + instr; transform does head + glossline fragment in §11, then global count 1 for instr only).
Dutch number style in Dutch prose (zh-tw-de precedent): thousands separator `.` (45.000, 1.600, 4.100, 13.433, 2.400, 6.200); Traditional text untouched. Currency code `NT$` kept in Dutch lines.
svglib `_fw` rules (read from svglib.py): comma/semicolon/colon directly adjacent to a CJK char converts to full-width (，；：); `?`/`!` after CJK converts (？！); a paren pair converts to full-width ONLY when the enclosed text contains CJK. Dutch translations preserve the core's CJK-adjacency patterns (e.g. B1 closing `leer 封王 eerst, dan…` puts the comma after a Latin word, per the W43 NL precedent; parens containing CJK keep the same conversion as core).

## 5. Gates on the final render (all green)

- Registry: **150** (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38). **ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings** (run exit 0).
- p8.py compare: **CLEAN** — 150 noted, missing=[] extra_count=0 uncertain=[] keydiff=[].
- Occlusion audit: selftest OK; **edition 0 flags; core 0 flags; NEW vs core 0**.
- Same-baseline ink-collision scan (HTML-unescaped text measurement): **0 collisions** (B1 head ink right 960.8 vs column edge 961 — fits by 0.2 px; A2 head 433.5, B2 head 1405.8, all inside columns).
- Chart-label element check (P4/P6 text ink vs later-drawn rects, chips/frames excluded): **0 overlaps**.
- Gloss counts in render: `Uitleg — ` ×12 (P1 2, P2 2, P3 3, P4 2, P5 2, P6 1, P7 0, P8 0) = core's 12 Notes boxes; `Notes` residual 0. Glossline() 4 = 4 (P7 ×3 + P8 §F ×1, from sources); match_set note items 16 = 16 (4 sets × 4). (The "33" figure from another family's core does not apply.)
- P7 golden sentences: all 8 verbatim from this issue's own articles, exactly **2 occurrences each** (article + P7), page tags `(p. N)` present in the zh-tw core's tag form, all 8 Dutch translations present:
  - 「用手機轉帳、掃碼付款、網上買保險，都是金融科技」(p. 1); 「123個國家及城市、1,600個攤位」(p. 1); 「需要才買，不要為了折扣買一堆用不到的東西」(p. 2); 「在高雄，鋼鐵也能變成舞台」(p. 3); 「福隆的夏天，在10月26日畫下句點」(p. 3); 「6比0完封兄弟，龍隊拋下紅色彩帶」(p. 4); 「250家店家一起討糖」(p. 5); 「旅展首日中午12點才開門」(p. 6).
- Images: payloads byte-identical core vs edition per page with identical placement (P1 1, P2 1, P3 0, P4 1, P5 1, P6 0, P7 0, P8 0). Commons Artist credits verbatim: P1 harbour.jpg (Wilfredor, CC0), P2 rain.jpg (CorraleH, CC0), P4 baseball.jpg (Bain News Service, Public domain, Commons file Washington_team,_Washington_AL_(baseball)_LCCN2014680242.jpg), P5 pumpkin.jpg (Benjamin Balazs, CC0). Credit lines byte-identical (source attributions, not apparatus).
- Readers' corner: frozen Traditional disclosure intact + Dutch disclosure stating no genuine letters exist + explicit open invitation in Dutch (5-line form, see §7).
- Cards: all 8 eyeballed clean (no overflow/overlap/footer collision; badge/footers/gloss boxes/fixed boxes/chart labels/keys clean; P7 teaser clear of footer; P2 boxes; P4 chart).
- P7 geometry (final): columns a2 1529 (= core), b1 1463 (= core), b2 1529 (core 1496; +1 line, ≤1560 nominal bottom, no warning); col3 ends 1687.36; teaser ends 2485.36 (footer rule 2580 — clear). Core P7 col3 geometry for reference: clinic box eh 648.36; frame wh 312.5 (wt 5 lines, wcn 2 lines); letter lh 560.5; col3_end 1745.36; teaser ends 2543.36.

## 6. Rendered-output sweep (coordinator additional check — passed)

Sweep of ALL text nodes in the delivered SVGs (1,450 nodes), not just sources — the check that caught the sibling `算一算 · Work it out` miss:

- `算一算 · Work it out`: **0**. `算一算 · Reken uit`: **3** (P2, P3, P5). This edition never had the miss: the transform maps the head ×3 (P2, P3, P5), and the render proves it. P3 card re-verified visually: `算一算 · Reken uit` present, no English head.
- `Baseball words`: 0; `Honkbaltaal`: 1 (P4 title, see §7).
- `Deep-read quiz`: 0; `Diep-leesquiz`: 1 (P6 head, see §7).
- Bilingual-head tails: every `·`-tailed head in the render is Dutch (or frozen Traditional + option letters). Full tail listing was dumped during the sweep and adjudicated.
- English-marker sweep (30 hits on markers like "the", "and", "week", "quiz", "was", "halloween", "festival", "model", "show", "fair", "travel"): every hit adjudicated — Dutch words/loanwords with identical spelling (week, quiz, was, Halloween, festival, model, shows), proper names (Hong Kong FinTech Week, Taipei International Travel Fair (ITF), Hong Kong Convention and Exhibition Centre, Nangang Exhibition Center, Back to the Future), or frozen target text (Fintech Nexus theme line). **Zero real English residue.**
- Residual-English phrase grep (37 phrases incl. `Explanations in English`, `Quick quiz`, `Did you get it`, `Fill in`, `True or false`, `Answer keys`, `Model answer`, `Open task`, `Notes`, `Match`, `Writing`): all 0 in edition SVGs.

## 7. Fix history (all folded into the transform as made — see §8)

1. First full render: registry perfect, but P7 teaser ended 2689.86 (past footer rule 2580) because Dutch col3 ran long. Root cause measured: letter disclosure EN 6 lines → NL 10 lines (+116 px) + frame wt 5→6 lines.
2. P7 shortening fixes (all in transform): frame wt → 5 lines (`…geeft de volgorde aan: eerst X, dan Y. Maak er zelf een: 先比價，再結帳 (vergelijk eerst, betaal dan).`); frame wcn → 1 line (`Frame: 先…再… — eerst X, dan Y.` — "make your own" instruction already lives in wt); A2 para2 → 7 lines (= EN); B2 para2 → 7 lines (= EN); B2 para1 → 5 lines (`…hun eigen zegswijze… en 泡湯 (warmwaterbad).`); B2 closing → 2 lines (`Vier lokale uitdrukkingen volstaan — elk uitje voelt dan dichterbij.`); B1 para2 → 5 lines, B1 closing → 3 lines (both = EN). Result at that stage: P7 columns a2 1529 (= core), b1 1463 (= core), b2 1529, col3/teaser core-exact.
3. Occlusion round 1: 3 NEW BOXTITLE flags → fixed in transform: (a) P2 `你呢?` box overflow — Dutch grey line 3 lines → 2 lines (`Welke hotpot eet jij voor Lidong? Wat zit er in je Double 11-winkelwagen?`); (b) P2 champion-deals title too wide (443.2 px) → `封王優惠 · Kampioensacties` (347.3 px, limit 412); (c) P7 letter-box last line 10.6 px past border.
4. Letter-box investigation: audit's `shape_box` expands rects by half stroke (0.7 px). Core's own last letter line sits at ink center 1746.3 vs expanded border 1746.06 — core escapes flagging by 0.24 px; mine failed by ~0.06 px. The last line's ink genuinely straddles the box border in both, but the gate requires 0 flags. Fix: disclosure shortened to 5 lines (`Voorbeeldbrief — geen echte. Uitstel: VOL.1 beloofde echte brieven en pagina-8-schrijfwerk vanaf dit nummer, maar er kwam niets binnen — voorbeeld blijft, uitnodiging open. Stuur je brief in!`), keeping label + deferral (letters + page-8 writing, from this issue, nothing arrived) + explicit invitation. Result: col3 ends 1687.36, teaser ends 2485.36.
5. Systematic AST audit of transformed sources then found TWO MISSED translations (planned but never added to the transform; everything else audited as Dutch, frozen target text, code, or proper names):
   - content34 P4 title: `棒球詞卡 · Baseball words` → `棒球詞卡 · Honkbaltaal` (measured 379.2 px at 34pt serif bold, limit 434; `Honkbalwoorden` measured 466.6 px — too wide, rejected).
   - content56 P6 head: `深讀測驗 · Deep-read quiz` → `深讀測驗 · Diep-leesquiz` (measured 339.9 px at 28pt sans bold, limit 434).
   - Both `sub()` calls added to the transform; rebuild re-ran all gates (§5, §6) on the fresh render.
6. Count corrections found by grep before running the transform (never hand-patched): `算一算 · Work it out` ×3 (not 2 — P2 also has one); `The mascot parade runs daily at 14:00.` ×3 (P5, P7 A2, P8 B); near-duplicates distinguished — `Ginger duck is a typical Lidong dish.` (P3) vs `Ginger duck is a Lidong dish.` (P7 B1, ×1); `The sand festival closed on Oct 26.` (P3) vs `The sand festival closed Oct 26.` (P8 A, ×1); `FinTech Week opens on Monday, Nov 2.` (P1) vs `FinTech Week opens Monday, Nov 2.` (P8 A, ×1). Two aborted transform runs (count assertions) were recovered by deleting the build dir, re-copying fresh core, fixing the transform, re-running — never by hand-patching.
7. Known trap avoided: the P8-key `AI` note (`AI inside finance is 人工智慧＋.`, content8 line 69) is a SEPARATE string from the P6 gloss `AI+` string — both were translated (P6 gloss + P8 note), confirmed in the AST audit.

## 8. Gate 10 — transform-solo (PASSED: 8/8)

Method: fresh core copy in `hidden_files/weekly-report-w45-zh-tw-nl-gate10-build/` + the transform script ALONE + one-process driver (`run.py`, then `render.py`). The transform's repoint lands OUT/BASE on the edition dir, so the Gate 10 harness repointed the gate10 copy's OUT/BASE from the edition dir name to `weekly-report-w45-zh-tw-nl-gate10-out` by WHOLE dir-name replacement only — the es-template failure mode (splicing an absolute temp dir inside the `~/workspace/...` prefix) was NOT inherited and NOT used; the resulting path is a clean `os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-nl-gate10-out")`. Gate 10 output lives at `hidden_files/weekly-report-w45-zh-tw-nl-gate10-out/` (moved out of `files/` so it cannot be mistaken for an edition dir).

- Gate 10 run exit code: **0**. FLOW OVERFLOW / HEAD TOO WIDE warnings: **0**. Registry TOTAL 150.
- Byte comparison gate10-out SVG vs delivered SVG: **8/8 byte-identical** (p1-front, p2-life, p3-culture, p4-sport, p5-youth, p6-deep, p7-lang, p8-test). Gate 10 PDFs match the delivered PDF byte sizes exactly (20,844,848 / 3,395,927).
- Stray nested-tree check: `find` shows only the flat `hidden_files/weekly-report-w45-zh-tw-nl-gate10-build/` and `hidden_files/weekly-report-w45-zh-tw-nl-gate10-out/` (svg/, cards/) trees; no nested/absolute-path artifact directory exists. The `//` grep hits in gate10 sources are Python `//` integer division and f-string SVG markup, not paths.

## 9. Residual-Latin adjudication (complete list)

Legitimate survivals, each adjudicated: frozen target-text proper names/theme strings (`Fintech Nexus: Bridging the World, Building the Future`, `StartmeupHK`, `SUPER STAGE`, `SOLID TIDES`, `JUMP`, `Trick or Treat`, `ITF`, `MVP`, `Nangang Exhibition Center` as venue proper name in Dutch notes, `Fintech`/`AI`/`AI+`/`Finance+` abbreviations, `NT$` currency code, `VOL.2`, level chips A2/B1/B2, option letters); Dutch loanword `Frame:` in the P7 frame note; `體育 · Sport` (Dutch word identical to English, recorded not changed); all 4 Commons credit lines byte-identical; Dutch words with English-identical spelling (week, quiz, was, Halloween, festival, model, shows) per §6. No other Latin string survives in the explanation layer.

## 10. PDF pins (delivered files — SUPERSEDED by §11 fix round; current pins are §11)

| file | bytes | SHA-256 | pages | page size |
|---|---|---|---|---|
| Lucerna-VOL2-NL.pdf (print) | 20,844,848 | 828dcde3b809aea7761f1abad1bca8266841799dbbfa8be35a750f152e760de7 | 8 | 1462.5 x 2025 pts |
| Lucerna-VOL2-NL-web.pdf (web) | 3,395,927 | 3001b65131cdb8b1768d98105790f37e8b005774355179569ce5a5027d753a38 | 8 | 1400 x 1938 pts |

Old web PDF < 10 MB: yes (3,395,927 bytes). Cards: 8 × 1950×2700 PNG in `cards/`.

## 11. Fix round — proof B1 (2026-10-28, transform-only, NOT finalized)

**Blocking item fixed:** P7 readers'-corner letter-box border struck through the last Dutch disclosure line. Independent proofread evidence: letter box rect x=1451, y=1155.86, h=531.5 → bottom 1687.36 (expanded 1688.06); last line node y=1694.23, text `blijft, uitnodiging open. Stuur je brief in!`, ink [1473.0, 1677.98, 1844.5, 1699.23] — 11.87 px past the border. Audit read 0 because the line's ink center (1688.61) sits 0.55 px outside the expanded border, so BOXTITLE never considered it — the audit 0 was a blind spot, not a pass, and is NOT cited as evidence for this box.

**Remedy chosen (in the transform, never a hand patch):** enlarge the letter box — the `lh` formula's bottom pad +26 → +50 (+24 px), via a new `sub()` in `hidden_files/weekly-report-w45-zh-tw-nl-transform.py` §10 targeting `len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26` (count 1). Wording UNCHANGED: all disclosure facts intact (label `Voorbeeldbrief — geen echte.` + deferral: letters + page-8 writing, from this issue, nothing arrived + explicit invitation `Stuur je brief in!`). The 5-line shortening was NOT reworked — it was never the fix; the formula under-budgets laid-out text by ~12 px.

**DIRECT measurement (audit parser's own ink measurement, not the audit flag count):**
- New letter box: x=1451, y=1155.86, w=434, h=555.5 → bottom **1711.36** (expanded 1712.06).
- Last Dutch line unchanged: node y=1694.23, ink bottom **1699.23**, ink center 1688.61 (now 23.45 px inside the expanded border).
- **Clearance: 12.13 px raw (12.83 px vs expanded border)** — meets the ≥ ~10 px requirement.
- **Card crop evidence:** `hidden_files/w45-zh-tw-nl-fix/p7-letterbox-crop.png` (from the new P7 card) shows the last line fully inside the box with clear space below it; the border touches no glyph. Full P7 card re-eyeballed: columns, clinic, frame, letter box, phrases strip, teaser, footer all clean.
- **No new collision below:** phrases strip shifts down with col3_end by design (fy = max(1712, col3_end+44) = 1755.36; gold rule at 1741.36, 30 px below the new box bottom); teaser ends **2509.36** (was 2485.36), footer rule 2580 → **70.64 px clear**.

**Re-gate evidence (all on the fixed render, one-process run.py + render.py, exit 0, TOTAL 150, ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings):**
- (a) Occlusion audit: selftest OK (all 6 classes); edition **0 flags**, core 0, **NEW vs core 0** — required but NOT sufficient evidence for this box; the direct measurement above is the evidence.
- (b) Freeze diff `--strict-cjk`: counts identical to the pre-fix render on all 8 pages (p1 +23/−22 … p7 +86/−87, p8 +194/−186); **strict-CJK added = 0 on all 8 pages**.
- (c) p8.py compare: **CLEAN — 150=150, missing=[], extra=0, uncertain=[], keydiff=[]**.
- (d) Gate 10 self-run from the UPDATED transform (fresh core copy + transform ALONE + one-process driver, evidence `hidden_files/w45-zh-tw-nl-fix/gate10-out/` + `gate10-run.log`): exit 0, zero warnings, **8/8 SVGs byte-identical to the delivered SVGs**. Note: a first Gate 10 attempt repointed the temp output under `files/` by mistake; it was deleted immediately and `files/` verified clean of it, then the run was redone with output under `hidden_files/` — the 8/8 result above is the redone run.
- (e) Rendered-output residual-Latin sweep (1,450 text nodes): `算一算 · Reken uit` = **3**, `算一算 · Work it out` = 0, `Baseball words` = 0 / `Honkbaltaal` = 1, `Deep-read quiz` = 0 / `Diep-leesquiz` = 1; 37-phrase English grep all 0.
- (f) Card eyeball: P7 fully re-eyeballed (above); cards P1–P6, P8 are **byte-identical** to the proof-passed cards (only P7's SVG changed — verified: SVGs P1–P6, P8 byte-identical to the pre-fix delivery, P7 the sole change), so their passed eyeball verdicts carry over pixel-for-pixel. Builder checks script (`hidden_files/w45-zhtw-nl-checks.py`) exit 0.
- (g) PDFs re-rendered — **NEW pins (current delivery)**:

| file | bytes | SHA-256 |
|---|---|---|
| Lucerna-VOL2-NL.pdf (print) | 20,844,849 | b6e3a207b89626786a66e448b3badfb251691366e3c607c8d93057a5b1b97b8f |
| Lucerna-VOL2-NL-web.pdf (web) | 3,395,098 | 590e04aabf9f3724c54266d5ee89448b98e3caa9e6267316a51999193665ba90 |

- Delivery dir remains flat (svg/, cards/, 2 PDFs, KIT, ABSTRACT.txt); ABSTRACT.txt untouched (351 B, unchanged mtime). Nothing else was touched: badge, footer, gloss counts, golden sentences, images, P8 dash style, AI handling (verbatim 人工智慧＋), or any other passing gate. Canonical build dir's `content7.py` now carries the +50 line (the only .py difference vs the pre-fix build); fix logs saved as `build-fix.log` / `render-fix.log` there.

**Status: FIXED, NOT finalized — full reproof of this render follows; nothing is shipped by this fix.**

## 12. Non-blocking notes

- P7 b2 column ends at 1529 vs core 1496 (+1 line). Within the 1560 nominal bottom, no warning, phrase rule far below — not a defect, recorded for the proofreader.
- P7 B1 head ink right 960.8 vs column edge 961 (fits by 0.2 px) — measured, not assumed; same-baseline scan passes at 0.
- P7 letter-box: the core's own last line also straddles the expanded box border by 0.24 px of slack. ~~This edition's 5-line disclosure sits comfortably inside~~ — CORRECTION (§11): that claim was FALSE. The 5-line shortening did not fix the geometry; the independent proofread measured the edition's last Dutch line 11.87 px past the border (ink bottom 1699.23 vs border 1687.36). Fixed in the transform by enlarging the box (§11); the occlusion audit's 0 flags never covered this line (blind spot: ink center 0.55 px outside the expanded border).
