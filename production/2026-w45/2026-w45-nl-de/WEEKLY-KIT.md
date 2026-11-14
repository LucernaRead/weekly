# WEEKLY KIT — De Lucerna VOL.2, NL × DE (W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026 (same as the W45 NL core).
- **Pairing:** Dutch target text (frozen) × German explanation layer (fully localised).
- **Masthead:** De Lucerna (Dutch article De, per the core).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Lead topic (from the core, unchanged):** «Nederland in de Klimaatweek» — Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov).
- **Build tree:** `hidden_files/weekly-report-w45-nl-de-build/` (copy of the W45 NL core build, OUT repointed to this edition before any run; the core build directory was never imported or run in place, per tools/README #11).
- **Delivery:** this directory — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700), print PDF, web PDF, this KIT, `ABSTRACT.txt` (German, single line, no ASCII double quotes).
- **Status: builder-complete only.** NOT finalised — an independent proofread round is still required. Nothing was posted to Discord, nothing was sent to the main chat, no cron was created, weekly-git was not touched.

## 2. Core measured values (from the W45 NL core WEEKLY-KIT, re-verified in this build)

- **Exercises: 150 total.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- **By level: A2 47, B1 72, B2 31** (build registry output, identical to the core).
- **By type (German labels, counts identical to the core):** ergänzen 65, wählen 44, zuordnen 8, richtig/falsch 7, Sätze bilden 8, Lückentext 13, übersetzen 4, schreiben 1.
- **Model essay (P8 H, ex. 150): 87 words** (registry assertion, unchanged; Dutch text frozen).
- **Numbering continuous 1–150.**

## 3. Furniture — W43 NL × DE measured values (shipped SVG wins over generic tables)

Measured from `files/weekly-report-nl-de/svg/` (W43) and applied verbatim, with VOL.1 → VOL.2:

- **P1 pairing badge (INSERTED, not replacing the strapline):** x=975, y=568, 20pt, weight 700, fill #a4553a (BRICK), centred, text «NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER» (measured width 1025.4px, centred span 462–1487; band bottom 542, headline label baseline 606 — no contact). The Dutch strapline at y=372 («DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS», 19pt) is kept verbatim — unlike the W45 NL × EN build, which replaced it.
- **Footer (all 8 pages):** «De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.2 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH» (measured width 1140.8px at 20pt).
- **Page line (all 8 pages):** «Seite N von 8».
- **Gloss prefix (shipped W43 form):** «Hinweis · » — NOT the tables.json generic «HINWEIS · »; the shipped W43 NL × DE SVG reads «Hinweis · het ezelsbruggetje = …». Recorded here as a W43-measured override.
- **Bridge prefix (shipped W43 form):** «Erklärung · » (W43 P1: «Erklärung · de herfstvakantie = Herbstferien …»).
- **P1 top strip (W43 form):** «ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH» (measured 705.1px, centred span 622.5–1327.5; right-hand week line starts at 1419.8 — 92px clear).
- **P1 subtitle (label localised, topics frozen):** «NIEDERLÄNDISCH · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12» (measured 1644.0px < 1820px inner width — MUSEUMNACHT is kept; the W45 NL × EN build dropped it only because its longer WEEKBLAD label overflowed, which does not apply here).
- **P8 answer separators:** «— PAGINA N —» kept as in both shipped fan-outs (W43 NL × DE and W45 NL × EN); the tables.json DE separator «— SEITE N —» was NOT applied, because both shipped precedents keep the Dutch page reference in the answer apparatus.
- **P8 answer style:** dash style, as the NL core (keys «N. key — note»).

## 4. Gates — measured values (all builder-side; independent proofread still required)

### 4.1 Freeze (tools/freeze.py diff, core vs edition)

- **Baseline before transform: 8/8 byte-identical** — the unmodified copy of the core build re-rendered into this edition dir produced SHA-256-identical SVGs to the shipped core (recorded in `core-sha256-before.txt`); the core SVGs re-hash unchanged afterwards (8/8 OK at the end of the build).
- **Final diff:** per page added/removed strings — P1 +29/−28, P2 +43/−33, P3 +30/−27, P4 +29/−25, P5 +42/−34, P6 +37/−32, P7 +47/−45, P8 +181/−167. **Added CJK characters: 0 on every page; edition CJK total: 0.**
- **Removed-string audit:** every removed string contains Chinese except 8 wrapped-line fragments, each verified as a re-wrap of an intact sentence, not a loss: P5 «1. Kijk zondag om 20:00 uur op RTL» + «4 (am Sonntag …» (same Dutch sentence, break moved by the longer German parenthetical); P6 lone «）» (caption re-wrap); P7 «bomen。/thuis。/zij zette vast。/。» (bridge line tails; full bridges present, e.g. «opruimen = aufräumen: wij hebben / opgeruimd; vastzetten = befestigen: zij zette / vast.»); P8 «6. planten — veel mensen → planten» (note localised to «Plural, also planten», key «planten» unchanged) and «voorgelezen» (wrap fragment of «41. hebben voorgelezen — voorlezen Perfekt: hebben voorgelezen», present verbatim).

### 4.2 P8 printed-note set (tools/p8.py compare, BY NUMBER)

- **Core noted: 150/150. Edition noted: 150/150. Status: CLEAN, missing=[], extra_count=0, uncertain=[].**
- **keydiff=[7, 17, 70, 71, 76, 96, 137, 138, 148]**, adjudicated item by item:
  - **137, 138 — genuine re-aims (NL→reader direction, the only true key changes).** 137 key: «气候周持续七天。» → «Die Klimaatweek dauert sieben Tage.»; 138 key: «橙色预警意味着：做好准备。» → «Code Orange bedeutet: Bereite dich vor.» Notes likewise German. 139 and 140 are NOT in keydiff: their Dutch keys («Museumnacht duurt van 19:00 uur tot 02:00 uur.» / «Ik doe mee aan de Klimaatweek.») are byte-identical to the core; only their prompts were re-aimed to German (reader→NL direction).
  - **7, 17, 70, 71, 76, 96, 148 — p8.py paren-branch extraction artifacts, NOT key changes.** In each case the true printed key before « — » is byte-identical to the core (7: B; 17: wortelen; 70: eiland; 71: proef; 76: gaat winnen; 96: advies; 148: B); only the note was translated to German. The tool inflates its «key» candidate with the note text because the German note ends with an ASCII paren group — «(2.–8. November)», «(Plural)», «(het)», «(de)», «(nur eine Vermutung)», «(het)», «(Boden)» — while the Chinese note used full-width «（）», flipping the tool from its dash branch to its paren branch. Per the standing rule, a key candidate that is not a bare key (here: key + translated note) is not a real key difference; the bare keys match.

### 4.3 Geometric occlusion (tools/occlusion_audit.py, selftest OK each run)

- **Edition: 0 flags. Core: 0 flags. NEW vs core: 0.**
- **Same-baseline ink-collision scan (rowcheck.py, README #10): all 8 pages CLEAN.**
- **P6 chart-label coverage (README #12 GRAZE watch): worst bbox coverage 0.0%** — no chart label is covered by any later-drawn rect at all.
- **P1 word-of-week graze (adjudicated, audit-clean):** the German word para is 2 lines ending at baseline 1871.9, the same geometry as the shipped W45 NL × EN edition; the IN HET KORT box top (1874) sits below the glyph baseline with no struck glyph (visually verified on the P1 card crop: both lines fully legible, box edge below the text). The P1 row-B separator line (y=1853) likewise sits below the first line's descenders, as in the core.

### 4.4 Gloss counts (rendered gloss() strings split on ·, README #21)

- P2 box (content12): core 6 vs edition 6 — OK. P3 box: 5 vs 5 — OK. P4 box: 5 vs 5 — OK. P5 box: 5 vs 5 — OK. P6 box: 5 vs 5 — OK. No gloss string introduces an extra «·».

### 4.5 P7 golden sentences and phrases

- All 8 Dutch golden sentences appear **exactly 2×** in the edition (once in the source article, once on P7), verbatim, with the correct «(Pagina N)» label: P1 ×2, P2 ×1, P3 ×1, P4 ×1, P5 ×1, P6 ×2. Each was also verified present in its source page.
- **P7 word-box freeze (standing ruling):** the Dutch definition sentence ««meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.» is preserved verbatim; only the German gloss line below it was localised («meedoen = teilnehmen, dabei sein.»). All four PAS OP Dutch wrong/correction lines are verbatim. No definition sentence was translated into German. (No unfinalised edition was used as a precedent for any of this; the only precedents cited are shipped editions: W43 NL × DE and W45 NL × EN.)

### 4.6 Readers' corner (P7 BRIEVEN VAN LEZERS — no fabrication)

- The Dutch example letter is frozen verbatim («Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)); no reader, letter, name or quote was invented.
- **All three facts are on the page, in Dutch (frozen) and in German:** no real letters arrived; no best page-8 texts arrived; the printed item is an example with the promise carried to VOL.3. German disclosure verbatim: «Redaktionsschluss: keine echten Briefe, keine besten Seite-8-Texte — darum ein Beispiel; Versprechen für VOL.3.»
- **Explicit German invitation (imperative + print promise), verbatim:** «Beispiel der Redaktion, kein echter Brief. Schicke uns echte Briefe und beste Seite-8-Texte — wir drucken sie in VOL.3!» (Content-preview lines and other pages' exercise prompts are not counted as this invitation; this sentence is inside the BRIEVEN box itself.)
- **P7 column-3 bottom: 1896.5** (core: 1897.0); ZINNEN section headline rule at 1937 — 40.5px clear.

### 4.7 Other gates

- **Flow warnings in the final build: zero FLOW OVERFLOW, zero HEAD TOO WIDE** (final log `build-log-fix2.txt`; flow ends: P1-headline 1401/1828, P2-ex 2402/2580, P3-ex 2465/2580, P4-ex 2406/2580, P5-ex 2406/2580, P6-ex 1895/2580, P7 columns ≤1249/1560, P8-keys 2389/2540).
- **Images (all reused W43/W45-core assets, no new downloads):** P1 herfstbos — Foto: Vovogov90 — CC0; P2 kinderdijk — Foto: Nationaal Archief — CC0; P3 gracht — Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 elftal1912 — Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein. All four credit lines are present in the rendered SVGs (checks_de.py). Image payloads are byte-identical to the core build (same assets dir).
- **Banned strings in rendered SVG text:** «桥接» 0, «讲解» 0, «译注» 0, CJK characters 0 on all 8 pages, ASCII double quotes in SVG texts 0.
- **P6 chart:** values 45/25/20/10 (total 100) unchanged; chart labelled ÜBUNGSDATEN in the title and in the German caption («ÜBUNGSDATEN: erfundene Zahlen, nur zum Üben, keine echte Umfrage. …»); the Dutch OEFENDATA caption line is kept verbatim.
- **Footers:** 8/8 carry VOL.2 (see §3); no page footer reads VOL.1.

## 5. Toolchain

- **run.py and render.py both ran under `tools/venv/bin/python`: Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1.** (System python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg, so it was not used; render.py requires the venv per the task.)
- **Baseline reproduction:** the unmodified core build copy rendered 8/8 byte-identical SVGs under this toolchain (see §4.1), so the toolchain reproduces the family baseline.
- **Single-process rule (README #7):** every render went through the build's single driver `run.py` (content12 → 34 → 56 → 7 → 8 in one process); no content module was ever imported or run standalone, and nothing was imported inside the core build directory (README #11).
- **Line-based splicing only (README #17):** the fan-out transform (`transform_de.py`, plus the fix1/fix2 edit scripts logged in the build dir) replaces whole lines or exact unique literals with an assertion per replacement; no AST byte-offset splicing was used.

## 6. Fix records

### Fix 1 (first-build overflows: P1-headline +490px cascade, P2-ex match_set 39px over, P7 col3 2101, P8-keys clamped)

Pre-fix SVG hashes recorded in `fix1-baseline-sha256.txt` before editing.

- **P1:** bridge shortened to 3 lines («Erklärung · Klimaatweek = Klimawoche · boom planten = Baum pflanzen · besparen = sparen · waarschuwing = Warnung.») and cijfers parentheticals shortened («(Tage der Klimaatweek)», «(Bäume und Sträucher, Samstag)», «(Museen, über 70)», «(12. Spieltag)») — box total 424 → 343px, restoring the core's column-break geometry; headline flow now ends 1401 (core 1452).
- **P2-ex:** exercise-section heads gap 13 → 8 (4 heads) and P2 exercise gaps 8 → 4 (14 items), mirroring the W45 NL × EN fix1 recipe; P2-ex now ends 2402 (was clamped at 3032).
- **P7 col3:** clinic notes made telegraphic following the NL × EN fix1 precedent (Dutch correction lines carry the full meaning): «Langzeitwetter, nicht Wetter heute.», «Klimaatweek ist ein Name, also groß.», «Hauptsatz-Verb an zweiter Stelle: blijf ik.»; word gloss shortened to «meedoen = teilnehmen, dabei sein.»; disclosure and invitation shortened to their final forms in §4.6. Col3 ends 2101 → 1896.5.
- **P8-keys:** font tightening following the NL × EN fix1 / W43 DE family precedent: keys 13.5pt/lh 1.16/gap 0.5 → 13.0pt/lh 1.14/gap 0.3; separators 14pt/lh 1.16/gap 2 → 13.5pt/lh 1.17/gap 1.5; flow bottom 2552 → 2540. Keys now end 2389 (was clamped at 2582). Key/note texts unchanged.

### Fix 2 (first audit: 4 NEW flags)

Pre-fix SVG/card/PDF hashes recorded in `fix2-baseline-sha256.txt` before editing.

- **P1 COVER** (word-of-week 3rd line «von unserem Klima.» fully covered by the IN HET KORT box): German para shortened to 2 lines (««Klima»: Wetter und Natur über lange Zeit. Die Klimaatweek handelt davon.») — same baselines as the shipped NL × EN geometry; audit now 0, crop verified.
- **P2 EDGE** (match_set instruction «Wörter und Bedeutungen zuordnen», 320.4px from x=1647 → ink to 1967.5, past the 1950 page edge): shortened in both content12 and content8 to «Wort und Bedeutung zuordnen» (279.9px → ends 1926.9, 23px inside the page).
- **P6 BOXTITLE** («VOOR OF TEGEN? · DAFÜR ODER DAGEGEN?», ink right 1930.2 > box border 1885): retitled «VOOR OF TEGEN? · PRO UND KONTRA» (395.4px → ink right 1868.4, inside the border; crop verified).
- **P7 TEXTX** (golden row 0 German + «(Pagina 1)» wrapped, leaving a dangling «1)» 14px above the next quote): row-0 German shortened to «Vom 2. bis 8. November ist in den Niederlanden Klimaatweek.» (650.2px < 896px column width, single line); all 8 golden rows now single-line, crop verified.

## 7. Delivery values

| File | Bytes | SHA-256 |
|---|---|---|
| De-Lucerna-VOL2-DE.pdf (print, 8 pages) | 6,938,811 | abf4c90d815aef3a130f8235f78e0d64a5e7e7b75c30915525882c39359dad05 |
| De-Lucerna-VOL2-DE-web.pdf (web, 8 pages, < 10 MB) | 1,017,208 | 04685bce7900bd43177b35bf2cfb3695471057748635bb911e109e913381eaf5 |
| svg/p1-voorpagina.svg | — | db8f3caeb40e7483a7852ca67597737cd35d2493b5d2c00e727ef188e9df3e5d |
| svg/p2-leven.svg | — | 2e45391e5dabb2bdc5d85b2b6632e2e960d852f847ef135a32b5e7a67d0357d4 |
| svg/p3-cultuur.svg | — | 1b39df6ece13fad6f001f3d1a80210696d446fc5ba9dd35e47694ea669717cb3 |
| svg/p4-sport.svg | — | 26fa33f7075856c8a01f2aa9ce09f28556187b8b6ba0c8b2433fbfa4a29b11d0 |
| svg/p5-jongeren.svg | — | 941651b9054e82bb9a9978c5f92298e277eaaa80ba7a9e5354a0f7ecf4b116d8 |
| svg/p6-verdieping.svg | — | 255f3c61ef84d2a12232cf995b546ff92bd295592428cd1aa4649d93bfc6b051 |
| svg/p7-taal.svg | — | bd3cc2376564a3d47d454ca5164b23c0c78cfb86d14e6bb9a4a4e3a3ce574567 |
| svg/p8-toets.svg | — | f477ef170cf790c92a00ac344d655fb39a073f0d874d21e55aa9f62c965bf78f |

Cards: 8 PNGs, each 1950×2700 (SHA-256 in the build log / delivery listing; p1 79c5caf0…, p2 0150f99a…, p3 98923033…, p4 0ac33e42…, p5 73f3d82d…, p6 9ed3e208…, p7 18718f42…, p8 163ca877… — full values in the final build listing).

## 8. Reproduce

```
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-de-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py    # SVGs -> edition svg/ dir
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py  # cards + PDFs
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-nl-de --core ../files/weekly-report-w45-nl-core
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-nl-core --edition-dir ../files/weekly-report-w45-nl-de --target nl
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-nl-core/svg --edition-svg ../files/weekly-report-w45-nl-de/svg
```

Note for a from-scratch rerun: `transform_de.py` records the first transform; the fix1/fix2 edits listed in §6 are applied afterwards (they are also visible as the diff between the transform output and the final content files). The transform script itself is not idempotent on already-transformed sources (its specific replacements assert on the Chinese originals), which is the expected one-off behaviour.

## 9. D5 rebuild (2026-11-14, builder run; not a proofread round)

D5: 讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK（SOP §1.1 字体修复）。D5-only 家族：新样式已在仓，单版施工只装 D5、重渲一次。

- Core 落盘（全家共用一次，v1 执行）：`apply_variant.py --patch-core nl --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-nl/svglib.py` +95/−3 行，`_D5_READER = "latin"`（D24：按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-nl-de/svglib.py --target nl --reader de --week 2026-w45`（先 `--check` dry-run，mode=latin）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（svglib.py 含 fix2 标记 13 处，安装器日志 "added fix2 block"）。
- 基线（修前生产版，venv 重建）：`run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；印 PDF 7,526,971 字节；印/网文字层 vs issues 已发 web PDF 字符多重集差 **0**；修前普查 D5 违规 **拉丁 500**（>0，符合装机前提）。KIT §7 旧 pin 与基线实测不符（de 例：KIT 印 7,918,211 B，基线实测 7,526,971 B）——KIT SHA 滞后（PLAN 修正案：基线永不以 KIT SHA 为准），本次以实测发运值订正。
- 导出器（第 0 步自验）：`scratch-2026-w45-nl/export_text_w45nl.py`（AST 导出，源自 content*.py 字面量，绝不从 PDF 反提；无 hardcode，标题由参数传入）。基线试跑 vs issues 已发 `.text.md` **11/11 BYTE-IDENTICAL**；patched 导出同样 BYTE-IDENTICAL（门 15）。
- 修复（run1 → run2）：共 **9 处**，只动字号，零文字改动。run1 缺陷：栏头超宽 3 处（ru 除外，ru 栏头未超）、occlusion TEXTX 1 处（P7 B1 栏头 'SCHEIDBARE WERKWOORDEN' 与 'B2' 重叠 5.2×17.8px；ru 除外）、boxtitle/creambox 6 处（ru/zh-cn/zh-tw 为 0），ru 另有 spill 1 处（codes 行注 'внимательны' 框底溢出 BELOW +13.34px）。
  - `content12.py:50` 奶油框标题 DE WEEK IN CIJFERS　IN ZAHLEN：tsize — → **tsize=21**（宽 421.6px，超框 17.2px；修后 384.9px，余量 17.5px）。
  - `content12.py:182` 奶油框标题 ZO ONTHOUD JE HET　MERKSATZ：tsize — → **tsize=21**（宽 428.5px，超框 24.0px；修后 391.2px，余量 11.3px）。
  - `content12.py:72` p.text Agenda van de week　TERMINE DER WOCHE：19 → **18**（宽 419.4px，超 19.2px；修后 397.4px，余量 0.8px）。
  - `content12.py:135` p.text IN HET KORT　KURZ GEMELDET：24 → **22**（宽 424.6px，超 24.7px；修后 389.2px，余量 8.7px）。
  - `content56.py:162` p.text VOOR OF TEGEN?　PRO UND KONTRA：21 → **19**（宽 426.9px，超 26.1px；修后 386.2px，余量 12.6px）。
  - `content7.py:84` p.text HET WOORD　WORT DER WOCHE：23 → **21**（宽 416.9px，超 17.1px；修后 380.5px，余量 17.2px）。
  - `content12.py:178` 栏头 DRIE ACTIES VOOR DEZE WEEK：25 → **24**（宽 425.0px（栏 422.5px）；修后 408.0px）。
  - `content34.py:21` 栏头 TWEEDEHANDS IS OOK CULTUUR：25 → **23**（宽 456.7px；修后 420.1px）。
  - `content7.py:32` 栏头 B1　SCHEIDBARE WERKWOORDEN：24 → **22**（宽 455.7px；修后 417.8px）。
- 门禁（run2，全套 16 门 + D18）：**ALL-GREEN**。run TOTAL 150 / head_check 0 defects / d5 census 拉丁 0、西里尔 0、CJK 内花括号 0 / render RC=0 / webpdf RC=0（网 PDF 1,017,208 B < 7 MB）/ occlusion 0 flags（selftest 6 类全触发）/ p8 extract 150/150 / p8 compare CLEAN（missing=[] extra=0，keydiff=[137, 138]，137/138 为读者语重定向真重 aim，已裁定，非缺陷) / freeze baseline 8/8 / freeze diff vs base 新增 CJK 字符 **0**（新增拉丁 strings 474，D5 run 拆分所致；对照是 base 修前生产版，不是 core）/ spill 0（1 OBSERVE）/ boxtitle 0 / edge 0 TOUCH 0 NEAR / creambox 0 defects（P8 219 → 219 行，距页脚线余量 53.8px）/ 文字层 print=web 字符多重集差 **0**（34,749 字符），text.md BYTE-IDENTICAL / census_quotes 0 defective / D18 刊头 gap **68.2px** > 0。
- 补充校验 G15b（carryover，诊断性，不计入 verdict）：共享 `verify_textmd.py` 对 nl 目标家族未标定（表按 pt 目标语格式标定），patched 与基线同态 FAIL（de 例：SVG-only 711 / MD-only 1119，基线 711 / 1121；ru、zh-cn 基线与 patched 残差完全相同）——D27 类已知工具口径差，非 D5 回归；内容不变的证据以门 15（AST 导出器 BYTE-IDENTICAL + print=web 差 0）为准。
- 最终 pin（builder 原件；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）：印 PDF `De-Lucerna-VOL2-DE.pdf` 6,938,811 B，SHA-256 `abf4c90d815aef3a130f8235f78e0d64a5e7e7b75c30915525882c39359dad05`；网 PDF `2026-w45-nl-de.web.pdf` 1,017,208 B，SHA-256 `04685bce7900bd43177b35bf2cfb3695471057748635bb911e109e913381eaf5`；text.md 38,895 B，SHA-256 `502afce83f33b804b36250d1219b3e770e49eea2c0ca649b2d5b4309dc96d203`（与 issues 已发版 BYTE-IDENTICAL）。
- Builder scratch：`hidden_files/d5-redo/scratch-2026-w45-nl/patched/2026-w45-nl-de/`；门禁总表复本（D29）：`production/notes/2026-w45/g-nl/scratch-d5-rebuild-nl/logs/2026-w45-nl-de/GATES-SUMMARY.txt`。
