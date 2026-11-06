# Lucerna Weekly — 简体中文 × Português (VOL.1) — WEEKLY KIT

Edition: Simplified Chinese target text (frozen VOL.1 core, files/weekly-report-zhcn-vol1/)
with ALL explanations rewritten in Portuguese (Brazilian) for Portuguese-speaking readers.
Build dir: hidden_files/weekly-report-zh-cn-pt-build/ · Deliverables: files/weekly-report-zh-cn-pt/
Method: fan-out per SOP — baseline reproduction first, explanation-layer rewrite only,
byte-exact string transform modelled on the shipped zh×IT sibling (its 317 verified
replacement pairs supplied the OLD strings; Portuguese news written fresh, index-aligned).

## 1. Baseline proof (before any edit)
- The unmodified copy of the core build, run with output pointed at the copy's own
  scratch/baseline-svg, reproduced all 8 shipped core SVGs BYTE-IDENTICALLY (sha256 8/8):
  p1 d75ee1bc… · p2 0addf9e7… · p3 c1fc3eda… · p4 84233560… · p5 db594dd2… ·
  p6 2987188a… · p7 4f598f28… · p8 8ac2807b…
- After the whole build, the core's shipped SVG hashes were re-verified: UNCHANGED 8/8.

## 2. Totals (must equal core — verified from the build registry)
- Exercises: 150 total · A2 56 · B1 65 · B2 29
- Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38
- Types (localized names): Complete a frase 68 · Escolha múltipla 50 · Associação 20 ·
  Escolha no contexto 11 · Escrita 1
- Writing model: 148 characters (identical to core)
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final build;
  P8 answer flow ends at y=2502 (box bottom 2540).

## 3. Key-diff registry (complete)
Keys byte-compared against the core's P8 by exercise number (parser over both rendered
P8 SVGs): differences = #150 ONLY (apparatus, expected — this core has no translation items):
- #150 key: core `(开放题，范文如下)` → PT `(pergunta aberta — texto-modelo a seguir)`
- #150 note: core `Open task - the model answer is printed in section F above (148 characters)`
  → PT `Pergunta aberta — o modelo está na seção F acima (148 caracteres)`
All other 149 keys byte-identical to the core. Arithmetic re-derived from the Chinese:
(77.5−57.5)/77.5 = 25.8% ✓ · 251.928−249.193 = 2.735 ✓ · 260+60=320 · 320−50=270 · 270−30=240 ✓

## 4. Printed-note set verification
Parsed from the rendered P8 SVG by number: PT prints notes for exactly {1..150},
the same set as the core (the core prints all 150). EQUAL ✓
Answer format: `N. key (note)` — space before the parenthesis, half-width parens only;
separators `— Página N —`; writing entry `150. ✓ (note)`.

## 5. PT furniture (as shipped, verbatim)
- Masthead: `Lucerna` (no article, exactly as the core ships)
- P1 strap: `SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.1 · 双11 · 大闸蟹 · 霜降`
- P1 pairing badge: `TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`
- Footer (every page): `Lucerna · SEMANÁRIO CHINÊS SIMPLIFICADO VOL.1 · TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS`
- Footer right: `Página N de 8`
- Gloss prefix (bslib4 gloss()): `Nota — `
- P8 keys head: `答案 · Gabarito — por página, com uma nota em cada resposta` ·
  right line: `Todas as notas em português · ✓ = a tarefa de escrita`
- Section subtitles follow the shipped PT column (EN×PT KIT §5): bare `Complete` for
  word-blank sections, `Associe as palavras` for matching, `Escreva` for writing.
- Number localization in notes: decimal comma (57,5 yuan; 25,8%; 10.100 toneladas; 0,258);
  chart scores keep the point form (251.928 − 249.193 = 2.735); keys byte-identical (key "25.8" stays).

### Deviations from first-choice wording (all wording-only, geometry untouched — recorded per SOP)
1. Section head `B · 词语填空 · Complete os espaços` → `B · 词语填空 · Complete`
   (head ink 534.8px > 434px column on P2–P6; EN×PT shipped the bare `Complete`).
2. Section head `C · 数字与计算 · Números e cálculos` → `C · 数字与计算 · Cálculos` (542.6px > column, P6).
3. P1 hot-box title `大家在搜什么 · O que as pessoas buscam` → `… · O que se busca`
   (audit: ink crossed the box's right border and the page frame; ends ≈1803 after fix).
4. P1 source line `Fonte: espelho das buscas em alta do Weibo (rddh.cn)` →
   `Fonte: espelho das buscas do Weibo (rddh.cn)` (ink reached x=1935, past the frame).
5. P2 红包 card definition `dinheiro num envelope vermelho, para dar sorte` →
   `dinheiro em envelope vermelho da sorte` (one line; the long form wrapped onto the card's bottom border —
   the same defect class the IT sibling's proofread caught on its 定金 card; the PT 定金 definition
   `parte pequena do preço, paga antes` is one line from the start).
6. P5 box title `这一周的高频词 · Palavras da semana` → `这一周的高频词 · Palavras-chave`
   (ink crossed its box's right border by ~2–4px; mirrors the IT sibling's `Parole chiave` solution).
7. P7 structure-box title: `本周句式 · Estrutura da semana` chosen short from the start
   (the IT sibling's longer first choice failed its proofread at ink 1886.6 vs border 1885).
8. Sixteen P8 notes lightly trimmed (facts unchanged) so the answer flow fits its box —
   the flow advances 13.3px more per entry than its fit check predicts; trims listed in
   scratch (build-run logs + transform history). Final flow end y=2502 < 2540.
9. P7 expl notes for entries 101/102/104: Han citations converted to pinyin
   (`jiàn`, `tiáo: coisas longas e macias`, `jiàn, não gè nem tiáo`) — mirrors the IT
   sibling's shipped notes; required for §6's final state (their Han forms made the
   typesetter convert the entries' note parens to full-width).

## 6. Pinyin-discipline verification (rendered P8 answer block)
- Chinese words cited inside Portuguese notes are tone-marked PINYIN only
  (dìngjīn, wěikuǎn, Chóngyáng, Shuāngjiàng, biàn chā zhūyú shǎo yì rén, …),
  including the matching-list glosses and the P7 expl notes (see §5.9).
- FINAL STATE, measured on the rendered P8 SVG keys zone: full-width parens = 0 · Han inside parens = 0 ✓
- Only English retained: the frozen source name `(The Beijing News)` on P4, identical to the core.
  P6 source names （新浪财经 (Sina Finance), 华龙网， 中华网） kept exactly as the core prints them.
- On-page glosses keep the core's "pinyin 汉字 — definition" format (target text, not citations).

## 7. Freeze check (Chinese target text)
- CJK character stream per page, core vs PT (difflib over the concatenated stream):
  CJK ADDED = 0 runs on all 8 pages. Every removed run is documented: the strap/footer
  furniture strings (replaced per §5), the `Notes｜` gloss prefix (→ `Nota — `), and
  pinyin conversions inside reader-language notes/lists (§6). P8 stems region CJK
  stream byte-identical (938 chars).
- P7 phrases: 8 phrases, verbatim contiguous, tags (Página 1, 1, 2, 3, 4, 4, 5, 6);
  issue-wide occurrence counts identical to the core per phrase (2,1,2,1,2,2,1,1 —
  the 1s are phrases split across wrapped text elements in the articles, exactly as in the core).
- Images: byte-identical to the core on every page (1/1/2/2/1/2/0/0 per page).
- Zero politics (zh-edition rule): no political vocabulary in the PT layer; content frozen from the core.
- The intermediary-layer term occurs 0 times in the paper, this KIT, and the operative
  build code. The one-off scratch transform scripts (scratch/transform_pt.py, pt_new.py,
  it-pairs.json) necessarily quote the core's original strings as search patterns during
  the rewrite; they are confined to the build's scratch/ subdir and are not operative code.

## 8. Geometric occlusion audit (mandatory gate)
Own implementation (scratch/audit.py): paint-order parsing, PIL real-font INK extents
(SC index, ascender-corrected), line boxes expanded by half stroke width.
Validated FIRST on a synthetic positive control: planted COVER and LINE defects both
caught, clean text unflagged.
- Core run: 1 flag (LINE graze, P2 remember-sentence line vs the rule below it).
- PT first run: 9 flags → 4 REAL defects fixed by wording only (§5.3–5.6), 1 TT graze, 1 LINE graze.
- PT final run: 2 flags, both pixel-adjudicated NON-defects on the rendered cards:
  (a) P2 LINE — same geometry as the core's flag: glyph ink ends at row 1802, the rule
      sits at 1803–1805, no ink contact;
  (b) P8 TT — adjacent wrapped lines of entry 148: ink rows 2386–2399 and 2401–2415,
      row 2400 is clear background; bbox overlap 0.6px only.
- Result: 0 unresolved NEW flags vs the core ✓

## 9. Image credits (from the core KIT; Commons API Artist field)
- P1 parcel locker — Map hobby, CC0 · P2 autumn valley — Paul Gilmore, CC0
- P3 chrysanthemum — PushpaKhan, CC0 · P3 frosted leaves — Gerda Arendt, CC0
- P4 basketball — noahsilliman, CC0 · P4 gymnastics 1896 — unknown author, 1896, public domain
- P5 LAN party — Syced, CC0 · P6 crab — Fumikas Sagisavas, CC0
Printed in PT as `Foto: <artist> — CC0 (Wikimedia Commons)`; the 1896 image as
`Foto: autor desconhecido, 1896 — Domínio público (Wikimedia Commons)`.

## 10. Deliverables
- svg/ ×8 · cards/ ×8 (1950×2700 PNG)
- Print PDF: Lucerna-VOL1-PT.pdf — 67,307,684 bytes · sha256 78c33cb80955221f8b50437f1ece0e4799385bb7cd0a75a6d81e49c18a1fa5c1
- Web PDF: Lucerna-VOL1-PT-web.pdf — 3,263,463 bytes (< 10 MB ✓) · sha256 3fb977b1f73079fbbd874eaf1515eb820e0054ccb02f63e3e44f0fab792382f4

## 11. Proofread status
- Builder's full proofread: DONE — all 8 pages read end-to-end from the rendered cards;
  all 150 keys re-derived/verified against the Chinese (§3); every weekday/date claim
  checked against the real 2026 calendar （重阳 Sun Oct 18 · fashion show Mon Oct 19 ·
  tail payments Tue Oct 20 20:00 · 霜降 Fri Oct 23 · 立冬 Nov 7); totals = core (§2);
  gates §4/§6/§7/§8 green.
- Independent proofread: **PASS — ZERO PROBLEMS** (2026-10-21, independent proofreader;
  one complete pass over the final rendered artifacts; no fixes required, no re-render;
  the edition's shipped files are byte-identical before and after the pass).
  - Freeze/CJK: per-page CJK multiset accounting (rendered SVGs) — CJK ADDED = 0 on all
    8 pages; the edition's CJK is a strict sub-multiset of the core's per page, which
    excludes drift and any script conversion. Every removed CJK run classified:
    strap/badge/footer furniture, the `｜` gloss separators, and pinyin conversions of
    Chinese citations inside reader-language notes (P3 reader-box `Shuāngjiàng?`,
    P7 `(Página 3)` gloss `Chóngyáng`, the P8 notes block). P8 stems region identical.
  - Keys: re-derived from the Chinese and machine-compared against the rendered core P8 —
    keys 1–149 byte-identical; #150 apparatus-only difference exactly as §3 documents
    (rendered core line `150. ✓ Open task - …` vs PT `150. ✓ (Pergunta aberta — …)`).
    Arithmetic re-derived: (77.5−57.5)/77.5 = 25.8% · 251.928−249.193 = 2.735 ·
    320−50 = 270 · 270−30 = 240 · #124 key A against the P6 article （约1.01万吨 =
    10,100 t) · model-text sums 260+60+40 = 360, 360−50 = 310, 30+280 = 310.
  - Printed-note sets (extracted BY NUMBER from both rendered P8 SVGs):
    core = {1..150}, edition = {1..150} — EQUAL; every edition entry carries a Portuguese
    note; separators `— Página N —`; format `N. key (note)`, space before the parenthesis.
  - Pinyin discipline: rendered P8 keys zone — full-width parens = 0, Han inside
    parens = 0. P7-exercise notes #101/#102/#104 verified in pinyin (`jiàn`,
    `tiáo: coisas longas e macias`, `jiàn, não gè nem tiáo`); matching-list glosses in
    pinyin. Full-width parens elsewhere occur only inside frozen Chinese target text;
    P7 vocabulary glosses keep the core's own `word （汉字）` format, identical to the core.
    Only retained English: the frozen `(The Beijing News)` source name on P4, as §6 says.
  - Totals: 150 exercises, numbering continuous 1–150 with complete per-page ranges
    (10/18/18/18/18/18/12/38) in both versions; standalone level badges identical
    (A2 51 · B1 61 · B2 27 elements; registry totals A2 56 · B1 65 · B2 29 per core KIT).
    Writing model: 148 characters, byte-identical string in both versions.
  - P7 phrases: the 8 phrase heads byte-identical to the core; tags
    (Página 1, 1, 2, 3, 4, 4, 5, 6); occurrence counts equal to the core's per phrase.
  - Calendar (verified against the real 2026 calendar): 重阳 Sun Oct 18 (retrospective),
    fashion show Mon Oct 19, tail payments Tue Oct 20 20:00, 霜降 Fri Oct 23, 立冬 Sat
    Nov 7 — all PT-layer weekday claims correct. Zero politics (PT layer scan 0 hits;
    Chinese political vocabulary 0 in both versions).
  - Geometric occlusion audit (proofreader's OWN implementation: paint-order parse,
    PIL real-font INK extents incl. bold, line boxes expanded by half stroke width;
    validated FIRST on a synthetic positive control — all six planted classes COVER /
    LINE / FOOTER / EDGE / TT / BOX-X fired, isolated clean text silent):
    edition flags = core flags in structure (per page: the two designed footer lines,
    ink bottom 2629 in both; plus the one P2 LINE item) — 0 NEW flags vs the core.
    Builder's four wording fixes pixel/SVG-verified: P1 hot-box title ink ends x=1797
    vs box border 1885; P1 source line ink ends x=1856 vs frame 1922 (was 1935);
    P2 红包 card definition one line, ink bottom 1757.1 vs card bottom 1768 (10.9px
    clear); P5 box title `Palavras-chave` ink ends x=911 vs box right 961. P7 structure
    title ink ends x=1833 vs border 1885 (the sibling edition's defect does not recur).
    Builder's two adjudications pixel-verified: P2 sentence glyph ink bottom = row 1802,
    rule top = row 1803 — identical in the core's and the edition's cards (non-defect);
    P8 entry-148 wrapped lines — ink x-disjoint at the shared projection rows (line-1
    descender tips at x≥1541, rows ≤2400; line-2 ascenders at x≤1537, rows ≥2401) and
    visually clean on the crop (non-defect; tight wrapped-line leading as elsewhere).
    Answer flow ends at entry #150 (baseline y=2470.6), clear of the footer band.
  - Images: embedded payloads byte-identical to the core per page (1/1/2/2/1/2/0/0);
    every printed credit matches a placed image and the core KIT (incl. P6's two
    Fumikas Sagisavas credits, identical in both versions).
  - Furniture: badge, footers, `Página N de 8`, gloss prefix `Nota — `, masthead
    `Lucerna` verified verbatim on all pages against §5. The intermediary-layer term:
    0 occurrences in the paper, this KIT, and the operative build code.
  - PDFs (measured by the proofreader): web 3,263,463 bytes (< 10 MB ✓) sha256
    3fb977b1f73079fbbd874eaf1515eb820e0054ccb02f63e3e44f0fab792382f4; print
    67,307,684 bytes sha256 78c33cb80955221f8b50437f1ece0e4799385bb7cd0a75a6d81e49c18a1fa5c1.
  - Core integrity: the frozen core's 8 shipped SVG sha256 re-verified at the end of
    the pass — all unchanged (d75ee1bc… / 0addf9e7… / c1fc3eda… / 84233560… /
    db594dd2… / 2987188a… / 4f598f28… / 8ac2807b…), matching §1's baseline values.
