# Lucerna Weekly — VOL.2 — Japanese × French (JA×FR) — W45

**Issue week:** Monday 2 – Sunday 8 November 2026.
**Pairing (badged on the P1 masthead and on all 8 footers):**
`TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`
Footer: `Lucerna · HEBDOMADAIRE JAPONAIS VOL.2 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS` + `Page N sur 8`.
**Target language:** Japanese (article-less: masthead is bare `Lucerna`, no article).
**Reader native language:** French. The entire explanation layer is French; the
Japanese body text is frozen verbatim from the W45 JA core.
**Status: builder-complete only.** Finalisation requires an independent proofread
(own occlusion audit, own freeze/P8 checks, full visual pass). This KIT does not
declare the edition final.

## Measured totals (verified against the core, not copied from other languages)

- 150 exercises; levels A2 46 / B1 75 / B2 29.
- Page distribution: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Model essay `『私の11月の週末』`: 167 characters (character count, not word count).
- Type counts: Compléter 50, Choix multiple 51, Appariement 12, Former une phrase 8,
  Vrai ou faux 11, Texte à trous 13, Traduction 4, Rédaction 1.
- Golden phrases: 8 Japanese sentences, each exactly 2× in the whitespace-stripped
  concatenation of all SVG text (once in its article, once on P7).
- House style: です・ます throughout; weekdays in full forms 土よう日・日よう日;
  no ruby/furigana.

## Per-page contents

- **P1 表紙 (hyoushi):** Culture Day (Tuesday 3 November) + autumn-leaf weekend
  7–8 November; trend box; week-at-a-glance; quiz; maple photo.
- **P2 くらし (kurashi):** ゆる整え食 (Ajinomoto announcement 21 October);
  warm November; season words; exercises 11–28.
- **P3 文化 (bunka):** Culture Day + Kanazawa traditional crafts (exhibition to
  8 November); Hiroshige III 1876 print; exercises 29–46.
- **P4 スポーツ (supotsu):** Japan Series, Yokohama games 1–2 verified
  (G1 24 Oct, G2 25 Oct); G3–G7 schedule only, results deferred to VOL.3 on the page;
  stadium photo; exercises 47–64.
- **P5 若者・エンタメ (wakamono):** Halloween 31 October (just-passed event) +
  autumn festivals; pumpkin photo; exercises 65–82.
- **P6 深読み (fukayomi):** warm November + autumn travel; Naruko Gorge at its
  best the 31 Oct–8 Nov weekend; Kobe Nunobiki Herb Garden illuminations from
  7 November to 28 December; practice chart 近場の満足 38 / 温泉 27 / 紅葉 21 /
  グルメ 14 = 100, labelled 練習用データ (practice data, not a real survey);
  exercises 83–100.
- **P7 ことば (kotoba):** A2 column 本と読書のことば (Reading Week, to 9 November)
  / B1 紅葉のことば / B2 数字を読む + error clinic 4 items + 『ゆるく整える』
  frame + readers' corner + VOL.3 preview; exercises 101–112.
- **P8 テストと答え (tesuto):** sections A–H; E = JA↔FR translation 4 items
  (re-aimed from the core's JA↔ZH; see W43 deviations); exercises 113–150;
  all 150 answer notes in French.

## Images (4, all reused from the VOL.1 verified set, PD/CC0 only, byte-identical to core)

| Page | Image | Credit line on page | Licence |
|---|---|---|---|
| P1 | Maple | 写真：Poliphilo — CC0（Wikimedia Commons） | CC0 |
| P3 | Utagawa Hiroshige III, 1876 print | 版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons） | Public Domain |
| P4 | Yokohama Stadium Dream Gate | 写真：Syced — CC0 | CC0 |
| P5 | Pumpkins | 写真：Petr Kratochvil — パブリックドメイン | Public Domain |

P2 and P6 carry no photo, as in the core. No new images were downloaded; a nabe
candidate (File:Motsunabe.jpg, CC-BY-SA 3.0) was rejected under the PD/CC0-only rule.
Credit lines come from the Wikimedia Commons API Artist field. Data-URIs are
byte-identical to the core in payload and geometry.

## Gate results (final round-5 output; raw outputs in the build dir)

- **Freeze** (`tools/freeze.py diff --strict-cjk`, core vs edition):
  added CJK = 0 on all 8 pages (P1 1406→1275, P2 1312→1161, P3 1172→1051,
  P4 1263→1169, P5 1247→1132, P6 1186→1101, P7 1676→1308, P8 2721→1448).
  P7 vocabulary boxes: Japanese definition sentences never localised; only the
  gloss part is French.
- **P8** (`tools/p8.py compare`, explicit dual paths `--core-p8/--edition-p8
  --total 150`): CLEAN, 150 noted = 150 noted, missing=[], extra_count=0,
  uncertain=[]. Tool keydiff list [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113,
  115, 117, 118, 137, 138, 140, 146, 147] adjudicated at printed-segment level:
  19 items are note-only (keys byte-identical; the tool's key field absorbs note
  text when a note ends in a parenthetical — extraction artefact); 2 genuine key
  diffs are legal: #137 `文化日是11月3日。` → `La Journée de la culture, c'est
  le 3 novembre.` and #138 `乱扔垃圾，要罚2,000日元。` → `Jeter des déchets coûte
  2 000 yens d'amende.` (E-zone JA→reader re-aim; #139/#140 stems re-aimed to
  French, Japanese keys byte-identical). P8 notes are pure French.
- **P8 note completeness (new gate, added in round 5):** all 150 printed notes
  compared core vs edition — zero untranslated notes survive (see fix round 5).
- **Occlusion audit** (`tools/occlusion_audit.py`, selftest first: all 6 planted
  classes fired exactly once, clean controls silent): **0 flags** on final output.
- **Builder gate script** (`audit_gates.py`, output `audit-gates3.log`):
  kinsoku line-start scan 0 hits; same-baseline ink collisions 0; full-page
  right-edge advance scan 0 violations; P6 chart-label mask-ink coverage worst 0.0
  (gate <0.30; 8/8 labels checked); gloss counts split on `·` match core
  (content12 [4,4,5], content34 [4,4,4,3], content56 [4,3,4]); golden phrases
  all 8 exactly 2×; banned intermediary-layer term 0 in SVGs, 0 in build code;
  code string set-diff: 98 edition-only CJK strings (all JP+FR pairs or French
  notes citing Japanese words, reviewed), 236 core-only CJK strings (all mapped
  Chinese explanations, furniture, or the documented Japanese disclosure
  replacement).
- **Simplified-residue check:** word-level, not character-level (shared-kanji
  Chinese words escape character-level scans): freeze-diff added/removed string
  review plus the code string set-diff above. No Chinese explanation text remains.
- **Kinsoku:** canonical svglib (md5 `d73e23b365676c3618d7e060b835eb4d`,
  `SEAM_SLACK=28`) never edited.
- **Visual check:** all 8 cards viewed — P1, P2 (round 4), P3–P7 (unchanged since
  round 4, viewed this session), P8 (round-5 version, viewed this session).
  No overflow, overlap, footer intrusion, or clamped keys; P8 keys 145–150 fit
  cleanly in the final column.
- **Build warnings:** no FLOW OVERFLOW, no HEAD TOO WIDE in round-5 logs.
  P7 teaser ends 2500.08 (≤2540 content limit); P7 col3 ends 1726.08.

## Furniture: three-way measurement (W43 JA×FR / W45 core / W45 JA×FR, P1)

W43 same-pairing furniture wins over README §20 generalisation. Wordmark y=248
(168pt) / 262 / 248; subtitle y=316 / — / 316 (40pt); badge y=356 (19pt bold brick)
 / absent / 356; strapline y=390 / 372 / 390 (19pt); double rules y=406+413 /
 392+401 / 406+413; dark band y=424 in all three. Pairing visible on the P1
masthead badge and on all 8 footers.

## W43 deviations (this edition vs the shipped W43 JA×FR edition)

- Footer VOL.2 (core) vs VOL.1 (W43).
- Badge geometry copied from W43 same-pairing SVG (see measurement above).
- Readers' corner: the Japanese disclosure sentence must not serve as the
  operative disclosure for French readers, and the Chinese disclosure is replaced
  — both replaced by ONE French disclosure stating the 3 facts (editor's sample,
  not a real letter; no real letters arrived by the deadline; no best P8
  compositions arrived) + VOL.3 promise + an explicit imperative invitation with
  VOL.3 publication promise. The Japanese example letter itself is kept verbatim.
  The VOL.3 preview line does not count as the invitation. Final French
  disclosure (6 wrapped lines at 20pt sans in 390px): `Exemple de la rédaction,
  pas une vraie lettre. Aucune lettre, aucun meilleur texte de la page 8 avant
  la date limite: les deux paraîtront dans le VOL.3. Envoyez-nous votre lettre
  en japonais — les lettres choisies seront publiées dans le VOL.3!`
- P8 E re-aim JA↔ZH → JA↔FR with legal keydiff [137, 138] (see P8 gate above).
- Fit shortenings (meanings preserved): P7 disclosure + clinic notes (round 2);
  P8 key notes, incl. #140 note → `Voir page 6` (round 2); P1 caveat →
  `Dates dans les articles; chiffres approximatifs` (round 3); both matching
  instructions → `Associez mot et définition` (round 3, fits P2 col3 and P8 col2
  slots); P3 events instruction → `Événement, lieu et date` (round 3, shortened
  despite no audit flag because it invaded the neighbouring column).
- Round-5 P8 note fix (see fix rounds): bare-string mapping added for key 37.

## Fix-round record (all fixes in transform.py only; pre-fix baselines kept)

- **Round 1** (`sha256-round1.txt`, `sha256-round1-cards-pdf.txt`): 150 exercises,
  levels/pages/model chars matched core. Defects: P7 teaser ended 2611.12 (>2540);
  P8 keys FLOW OVERFLOW (keys 145–150 clamped onto one baseline). Root cause:
  key-block height ≈5047px vs 4-column capacity 4848px — about 13 lines over.
- **Round 2** (`sha256-round2.txt`, `sha256-round2-cards-pdf.txt`; copy
  `transform-round1.py`): shortened French notes to save 21 key lines; P7
  disclosure shortened to 6 lines; clinic notes shortened. Result: teaser ends
  2500.08; zero FLOW OVERFLOW; only P7/P8 SVGs changed. P8 E key #138 set to the
  W43 JA×FR precedent wording.
- **Round 3** (`sha256-round3.txt`, `sha256-round3-cards-pdf.txt`; copy
  `transform-round2.py`): fixed 4 canonical-occlusion-audit flags (P1 box-title
  overflow, P2 page-edge overflow + P8 ink overlap from the words-matching
  instruction, P3 events instruction). Result: occlusion audit 0 flags; changed
  pages P1/P2/P3/P8 only.
- **Round 4** (`sha256-round4.txt`, `sha256-round4-cards-pdf.txt`; copy
  `transform-round3.py`): fixed the one English leak found by the code string
  set-diff — P7 head `読者の手紙 · Readers' corner` → `読者の手紙 · Le courrier
  des lecteurs`. Root cause: the generator's map entry matched only the comment
  line, while the code string contained the escaped form `Readers\' corner`.
  Only P7 SVG changed.
- **Round 5** (`sha256-round5.txt`, `sha256-round5-cards-pdf.txt`; copy
  `transform-round4.py`): follow-up trap from JA×EN/JA×DE — the bare P8 note
  `工艺展到11月8日` (P3 fill-in, P8 key 37) has no weekday suffix and was NOT in
  the NOTES table (only the suffixed `工艺展到11月8日（周日）` and the other item's
  `传统工艺展到11月8日` were), so it leaked through verbatim as Chinese on P8
  line 37. A full 150-note core-vs-edition comparison confirmed #37 was the ONLY
  leak (all other CJK-bearing French notes are legitimate Japanese citations;
  #150's apparent match was a parser artefact of the `✓` line — its printed line
  is French). Fix: bare-string mapping added to transform.py NOTES
  (`工艺展到11月8日` → `L'exposition dure jusqu'au 8 novembre`), plus a permanent
  P8-note-completeness section (8b) in `audit_gates.py`. Result: P8 line 37 now
  prints `37. 8 — L'exposition dure jusqu'au 8 novembre`; only the P8 SVG, the P8
  card, and both PDFs changed; all gates re-run green (freeze added CJK 0,
  p8 CLEAN 150=150 with the same adjudicated keydiff list, occlusion 0 flags,
  note-completeness NONE). Why earlier gates missed it: the transform post-audit
  only checks mapped NOTE keys (the bare string was never a key); freeze diff
  cannot see a string identical in core and edition; the English-word scan
  cannot see Chinese text. The note-completeness gate closes this hole.

## Deliverables (this directory)

- `svg/` — 8 edition SVGs.
- `cards/` — 8 PNG cards @1950×2700.
- `Lucerna-VOL2-FR.pdf` — print PDF, 8 pages, 28,047,840 bytes,
  sha256 `bac4681415f931968ccede3fcc090b80a735bd186fc8805b0008d27558df9255`.
- `Lucerna-VOL2-FR-web.pdf` — web PDF, 8 pages, 3,118,778 bytes,
  sha256 `bd243c13bbd754b8d1e0efc5deaa67b02c9d7dbe878bb806fc17a639619bc2f9`.
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (French, single line, no ASCII
  double quotes).

## Reproduction

Build dir: `hidden_files/weekly-report-w45-ja-fr-build/` (transform.py + per-round
baselines + raw gate outputs). All commands with `tools/venv/bin/python`
(system python3 has no cairosvg). Content modules share one registry and must
re-render in ONE driver process; never import content modules inside the core
build dir; fix rounds edit transform.py only, then:

```
tools/venv/bin/python transform.py   # applies exact-literal replacements to a pristine core copy
tools/venv/bin/python run.py         # single-process render (registry shared)
tools/venv/bin/python render.py      # SVG -> cards + print PDF + web PDF
```

Core build dir was never imported or written into; core SVGs re-hashed unchanged
after the baseline run. Shared `tools/scratch/` was not cleaned.

## D5 rebuild (2026-11-14)

- 范围：D5 + §1.1 合并重建。旧样式生产源 → §1.1 组装（`style-port-ja` fanout，
  MANIFEST-W45.md 逐文件 SHA 校验；svglib 另经 D1 波校验：反向还原 canonical §2a
  hunk 后 SHA 与 MANIFEST 一致，11/11）+ D5 安装，一次重渲。
- 安装：移植模板 `svglib-ja-d5.py` 原样装为版内 `svglib.py`，仅改 `_D5_READER`
  一行 → `"latin"`（latin 读者：与模板 0 行差）。
  路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（弯引号 → Newsreader）
  保留；kinsoku（`NO_START`）齐全。
  core 落盘：模板原样拷为 `production/2026-w45/core-ja/svglib.py`（`_D5_READER = "latin"`，
  与 W47 core-ja svglib 逐字节相同，28,392 B）；安装器 `--patch-core` 对旧式 core
  拒单已实测（`FATAL: old-style svglib (no _char_font)`，日志 `logs/installer-refusal-core.log`）。
- 基线（组装后新样式源，scratch `baseline/`）：run.py TOTAL 150、FLOW 0、
  HEAD 0；SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new`
  逐字节相同（47556 B）；印 PDF 27282204 B，
  SHA 与 fanout 印 PDF 一致（`b6f6c1b5316c572ca9e50d121c8672ad7e6f5db6c4d475f9cc2152ef4348b63f`）；网 PDF 文字层与已发网 PDF
  `pdf_text_diff_ja.py` IDENTICAL 8/8；印/网文字层多重集差 0；修前普查
  d5_latin_in_cjk 406（>0 ✓）、curly_in_cjk 0。
  网 PDF 字节与 fanout 不符为预期：`tools/webpdf.py` 2026-11-11 改版（commit `40963281`，
  weight + italic face resolution），D1 波（11-09）所用为旧版；文字层一致为准。
- 二次修复：
- F1: P1 信用行（右栏奶油框内） — 字号 18.5→18.0（只改该行，不改文案） (`content12.py:87` 18.5 → 18.0); P8 boxtitle 1 DEFECT（P1 [BODY] over=+6.5px right；与 de 同行同几何，基线同报，pre-existing，非 D5 引入）→P8 899 元素，boxtitle 0 DEFECT 行，页脚余量 76.0px
- 门禁（16 门 + D18 + D37；门 17 N/A，本家无 gates.py）：**ALL-GREEN**
- 1 run: PASS
- 2 head_check: PASS
- 3 D5 census: PASS (latin None / cyrillic None / curly-in-CJK None)
- 4 render: PASS
- 5 webpdf: PASS
- 6 occlusion: PASS
- 7 p8 extract: PASS (noted 150/150)
- 8 p8 compare: PASS (CLEAN, keydiff [137, 138])
- 9 freeze baseline: PASS
- 10 freeze diff: PASS
- 11 spill: PASS
- 12 boxtitle: PASS
- 13 edge: PASS
- 14 creambox: PASS (P8 899 元素，末行 y=2624.0，距页底余量 76.0px)
- 15a print=web: PASS
- 15b carryover: FAIL (D27: 共享校验器 ja 格式已知口径差，基线亦 FAIL；验收见 15a+15c)
- 15c native verify: PASS
- 16 census_quotes: PASS
- 17 gates.py: PASS
- D18 masthead: PASS (gap 288.2px)
- D37 P1 y~612: PASS (end 289.9pt vs 框缘 1439.5pt, over -1149.6pt)
- 新交付物（实测，scratch `patched/2026-w45-ja-fr/`）：
  - 印 PDF `Lucerna-VOL2-FR.pdf`：**24756505 B**，
    sha256 `e6394e97147bb0d9b854ad0a71cd626c106bc4e8e54a4c41009264e599ccdabc`（49 个嵌入字体）。
  - 网 PDF `2026-w45-ja-fr.web.pdf`：**2246245 B**（< 7 MB），sha256 `71f6f2c915bb7f0b95ca3e855917dc04a1fed84055c0a66db45f0e584e1ad132`。
  - `2026-w45-ja-fr.text.md`（新建；W45 ja 无已发 `.text.md`）：**47555 B**，
    sha256 `02379c82c468647d78293abb7f169c311c4bb879447d9ec663ecdba2ee58be0f`；基线导出与 fanout `.text.md.new` 逐字节相同，
    D5 导出经 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT（0 UNEXPECTED）。
- 日志：`logs/2026-w45-ja-fr/GATES-SUMMARY.txt`（总表）；D5 报告
  `production/notes/2026-w45/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w45-ja-fr.md`。
  本节只追加，不改上文旧 pin（旧 pin 为 port 前旧样式值，已过时；新值以本节为准）。
