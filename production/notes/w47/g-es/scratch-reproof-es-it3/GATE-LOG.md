# GATE-LOG — W47 es-it fix2 后独立复校（re-proof-3）机械门逐门记录

- 版：2026-W47 es-it；复校：独立 re-proof-3（与 fix2 agent 不同人，亦与 re-proof ef27d671 不同人）。
- 探针：`ls /dev/null` 存在 + `git -C ~/workspace/weekly-git hash-object -w --stdin` 通 + goals 侧真实写文件成功（`probe/test.txt`），均通后开工。
- 工作区 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-es-it3/`（下称 S）。生产目录只读：未改任何生产文件，未 commit/push；网 PDF 只在 S 内副本重渲。
- 工具均用 `~/workspace/weekly-git/tools/venv/bin/python`。helper 脚本自 `scratch-proof-es-it2/` 原样复制（未改内容，仅 `gates.py` 内 S 路径改为本 scratch）：`creambox.py`、`creambox_diag.py`、`boxtitle_core.py`、`keycheck_core.py`、`minfont.py`、`sweep_de.py`、`gates.py`。
- 驱动：`S/gates.py it --skip-render`（§1–§11；不含现场 render.py，因生产只读；run.py 改在 S/tmp 副本里跑，见 §0b；副本事后已删，日志留存）。freeze baseline 内部在 S 内副本重建，不碰生产。

## 0. SHA 与尺寸核对（任务书 + 盘上 sha256sum，复核前后各测一次，未变）

| 文件 | 尺寸（B） | SHA-256（盘上实测） | 任务书 | refanout |
|---|---|---|---|---|
| `La-Lucerna-VOL4-es-it.pdf` | 3,498,553 | `12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724` | 相符 | 一致（逐字节） |
| `La-Lucerna-VOL4-es-it-web.pdf` | 882,084 | `626e7588389b3c835eec0c8eebde974332ab27a90bca7a0dd2c5ffbdce19f6bd` | 相符（< 7 MB） | SHA 不同（见 §6，文字层一致） |
| `2026-w47-es-it.text.md` | 45,176（1,806 行） | `434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe` | 相符 | 一致（逐字节） |

- `pdfinfo`：印/网各 8 页，1462.5 × 2025 pt，PDF 1.7，未加密。
- SVG 8/8 与 refanout 逐字节一致（vs fix1 的 `svg-BEFORE.sha256`）：p1 `b44f9f83…`、p2 `823d14c8…`、p3 `da00c2fa…`、p4 `b03952ee…`、p5 `5bd0cb6f…`、p6 `6815a76d…`、p7 `143d3fd4…`、p8 `1134c6af…`（见 `svg-now.sha256`）。

## 0b. run.py（scratch 副本，生产只读）— rc=0，TOTAL 150

- 方法：`cp -r` 生产目录至 `S/tmp/runcopy`（删 `__pycache__`），在副本内跑 `tools/venv/bin/python run.py`（日志 `run-copy.log`；副本事后已删除，日志留存）。
- 输出：rc=0；`P8 saved, TOTAL exercises: 150`；`by level {'A2': 50, 'B1': 72, 'B2': 28}`；`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；`by type {'Completare frasi': 48, 'Scelta multipla': 47, 'Abbinare parole': 12, 'Vero o falso': 8, 'Formare frasi': 7, 'Trasformare frasi': 10, 'Cloze (scelta)': 13, 'Traduci': 4, 'Scrivi': 1}`；`MODELO words: 97`；`ALL DONE`。
- 副本重建的 8 个 SVG 与 shipped 逐字节一致（`cmp` 8 行 `identical`）。

## 1. 印/网文字层同一 — 逐字节一致

- 命令：`pdftotext -layout` 印版 → `it-print.txt`，网版 → `it-web.txt`；`cmp`。
- 输出：两文件均为 **108,723 B**，逐字节一致（`it-gates.json`: `print_web_text_equal: true`）。
- 直/弯计数：印版文字层直 28 / 弯 0；网版文字层直 28 / 弯 0；印版 `-bbox` 含直撇号的词 28 个（与 re-proof 28 处表逐词对应）。
- 网版 P1/P3 经 `pdftoppm -r 150` 渲染目视（`renders/web-p1-1.png`、`web-p3-3.png`；裁图 `crops/rp3-WEB-P1.png`、`crops/rp3-WEB-P3.png`），与印版一致；弯版空隙已消除（见 PROOF-NOTE §1）。

## 2. occlusion 审计 — 0 flags

- 命令：`tools/occlusion_audit.py production/2026-w47/2026-w47-es-it/svg --json it-occlusion.json`（日志 `it-occlusion.log`）。
- 输出：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`production/2026-w47/2026-w47-es-it/svg: 0 flags`；`flag_count: 0`。

## 3. p8 extract — 150/150

- 命令：`tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150 --json it-p8-extract.json`（日志 `it-p8-extract.log`）。
- 输出：`noted set = 150 of 150 (parse: lines)`，集合 [1..150] 连续无缺重。

## 4. p8 compare（vs core-es）— CLEAN，keydiff=[137, 138]

- 命令：`tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 …/svg/p8-ejercicios.svg --total 150 --json it-p8-compare.json`（日志 `it-p8-compare.log`）。
- 输出：`core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
- 本轮直接读 `it-p8-compare.json` 本体确认：`"status": "CLEAN", "missing": [], "extra": [], "uncertain": [], "keydiff": [137, 138]`。
- keydiff 裁定（见 PROOF-NOTE §2）：137/138 皆为读者语不同导致的翻译题键差异（核心键中文译句，本版键意大利语译句），键与题干逐句对应，正确；其余 148 键与核心逐字节一致。

## 5. freeze baseline（S 内副本重建）— 8/8

- 命令：`tools/freeze.py baseline --build production/2026-w47/2026-w47-es-it --core-svg …/svg --out S/freeze-es-it`（日志 `it-freeze.log`）。
- 输出：`baseline: 8/8 SVGs byte-identical`（p1–p8，每页 shipped SHA = 重建 SHA，与 §0 的 refanout SHA 一致）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`；rc=0。

## 6. freeze diff（核心↔本版文本多重集差分）— CJK 新增 6，全为 U+3000

- 命令：`tools/freeze.py diff --core-svg production/2026-w47/core-es/svg --edition-svg …/svg --json it-freeze-diff.json`（日志 `it-freeze-diff.log`）。
- 输出：p1 +30/−38、p2 +49/−52、p3 +33/−30、p4 +33/−27、p5 +45/−48、p6 +18/−17、p7 +45/−46、p8 +161/−626；CJK core→edition：205→21、309→17、178→14、197→16、265→15、93→15、399→12、1030→14；**TOTAL added CJK characters: 6**（p1–p6 各 1 个 U+3000，P7/P8 0 个；与 re-proof/fix1 一致，皆为 SOP §1.1 规定的全角空格分隔符）。

## 7. creambox 全版扫查 — 6 处负余量：5 处假阳性 + C1（真墨 +3.8）

- 命令：`S/creambox.py production/2026-w47/2026-w47-es-it/svg/*.svg`（日志 `it-creambox.log`）；逐项裁定用 `S/creambox_diag.py` 同组 SVG（日志 `it-creambox-diag.log`）。
- 全版负余量 6 处（与 re-proof 同值同位置）：
  1. P1 `y=1317 bottom=1707.0`，−37.0，末行 `AHORA TÚ　TOCCA A TE`——**假阳性**：下一栏目标题（diag：owner-rect=NONE，head/caption/outside）。
  2. P1 `y=588 bottom=1308.0`，naive −44.0，末行 `EN ESTA EDICIÓN　IL NUMERO`——**假阳性**：下一栏目标题（diag：owner-rect=['y=1312']）。该盒 OWN 末行 `Cinque chiavi, zero numeri inventati.` 基线 1300.0，余量 +8.0，**真墨余量 +3.8**（见 C1）。
  3. P1 `y=1312 bottom=1652.0`，−24.0，末行 `LA PALABRA DE LA SEMANA`——**假阳性**：下一栏目标题。
  4. P1 `y=1874 bottom=2194.0`，−24.0，末行 `La urna y el sobre: votar por correo…`——**假阳性**：插图下方图注，盒外正常。
  5. P2 `y=200 bottom=1217.1`，−37.0，末行 `DECIR LA HORA`——**假阳性**：下一栏目标题。
  6. P3 `y=200 bottom=375.4`，−37.0，末行 `LO QUE QUEDA DE NOVIEMBRE`——**假阳性**：下一栏目标题。
- **C1 回归（本轮独立重测）**：盒 `y=588` 盒底 **1308.0**；OWN 末行基线 1300.0（+8.0）；PIL 真墨底 1304.2，**ink-clearance +3.8**（`it-creambox-diag.log` P1 第 2 行，逐字与 fix2/re-proof 测值一致）。墨水未漫出盒底，C1 不列缺陷。diag 全版：0 负真墨余量（最小 +0.1，为 P2 `y=200 bottom=543.5` / P5 `y=939` 盒）。
- 其余正余量盒：P1 +40.7 / +10.8 / +39.0（真墨）；P2 +43.8 / +42.5 / +0.1 / +5.9；P3 +47.5 / +5.0 / +1.7；P4 +42.5 / +105.8 / +1.3；P5 +41.3 / +47.5 / +0.1 / +1.7；P6 +50.9 / +19.1 / +31.2 / +30.8；P7 +38.0 / +22.0 / +1.5；P8 无奶油盒。

## 8. P8 最小字号 — 10.125 pt

- 命令：`S/minfont.py` 对印版 P8（日志 `it-minfont.log`）。
- 输出：`P8 min effective font size = 10.125 pt (n=375)`；分布 10.125–34.5 pt；`below 9.75pt: 0`。≥ SOP §1.1 下限 9.75 pt。

## 9. boxtitle 宽度 — 0 溢出

- 命令：`S/boxtitle_core.py …/svg`（日志 `it-boxtitle.log`）；occlusion BOXTITLE 类自检已触发、实测 0 flags（见 §2）。
- 输出：全版框题无一越出自身框界；最小余量 **+14.4**（P7 `ERRORES TÍPICOS　ERRORI TIPICI`，墨右缘 1847.6，框右 1862）；其余 +20.1 起。

## 10. keycheck — 149/150，仅 #150 ✓ 例外

- 命令：`S/keycheck_core.py <edition-dir> it-p8-extract.json`（日志 `it-keycheck.log`，结果 `keycheck-150.json`）。
- 输出：`REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；唯一 mismatch：`n=150 page=8 type=Scrivi: key='Domanda aperta — testo modello sotto in questa pagina' extracted='✓'`——开放写作题，✓ 指向范文（97 词，见 PROOF-NOTE §4），为约定例外。

## 11. sweep（桥接/孤儿/寡行）— 0 / 0 / 0

- 命令：`S/sweep_de.py <edition-dir>`（日志 `it-sweep.log`）。
- 输出：`box-vs-hline flags: 0`；`bridges found: 20` / `bridge orphans: 0`；`bridge widows: 0`；`DONE`。

## 12. 孤儿标点全版扫 — 0

- 方法：本轮现场脚本实测（SVG 8 页全部 `<text>` 元素 + text.md 全行）：SVG 纯标点元素 **0**、行首闭标点 **0**；text.md 纯标点行 **0**。无日志文件，方法与 re-proof 相同。

## 13. 直撇号专项（本轮核心，见 PROOF-NOTE §1）

- 三处独立重数：text.md 直 28 / 弯 0；SVG 直 28 / 弯 0（P1 1、P2 1、P3 2、P4 1、P5 2、P6 0、P7 4、P8 17）；印/网文字层直 28 / 弯 0；印版 `-bbox` 含直撇号的词 28 个。
- 内容源：content12.py 直 2 / 弯 0；content34.py 直 5 / 弯 0；content56.py 直 6 / 弯 0；content7.py 直 6 / 弯 0；content8.py 直 19 / 弯 0（9 处正文 + 10 处代码引号）。content8.py:133/135 代码引号 `e_['n']` 未动。
- 渲染实测（本轮自写 `measure3.py`，词坐标取自印版 `pdftotext -bbox` 词框，与 fix2 的裁图盒方法独立；墨 = 亮度 <128，词框内墨迹列轮廓；150 dpi 印版渲染 `renders/p-1.png`～`p-8.png`）：12 处 sans 词内最大白空隙 6–7px（P7 `L'una` 7px、P8 `un'unica` 0px，其余 10 处 6px），弯版为 24–29px；Newsreader 对照 `Dov'è` 3px、`l'urna?` 2px；网版 P1/P3 均为 6px。16 处裁图（`crops/rp3-*.png`，3 倍放大）全部目视紧贴（详见 `crop-measure3.json` / `crop-measure3.log`）。
- 版式变化核实：P1 刊头配文行起始 x=657.5（refanout 值，SVG 实测）；P3 gloss 行 1 以 `l'anima` 结尾、行 2 `del flamenco.`（SVG 实测）。

## 14. 网 PDF 重渲（scratch 副本，绝不覆盖交付件）

- 方法：`cp -r` 生产目录至 `S/tmp/webrerun/ed`，在副本内跑 `tools/webpdf.py svg <out>`（日志 `webrerun.log`；副本目录事后已删，重渲 PDF 与日志留存）。
- 过程记录：第一次调用因缺参数 rc=2（`webpdf.py` 需 `svg_dir out_pdf` 两参数，未写任何文件）；按正确用法重跑 rc=0。
- 输出：重渲网 PDF `tmp/webrerun/rerun-web.pdf`，**882,091 B**，SHA `8acd881de948e4bb57af8f22d2bb22a716391ce6ac8f771308ccb07fe618caea`——与交付网 PDF（882,084 B，`626e7588…`）SHA 不同、字节数差 7 B，属已知的 webpdf 字体流非确定性（fix2 实测连跑两次 882,086 vs 882,083 B）；**不以 SHA 不等判 (b)**。
- 文字层：`pdftotext -layout` 重渲网 PDF → `webrerun-web.txt`，与交付网 PDF 文字层 `it-web.txt` **`cmp` 逐字节一致，108,723 B**；重渲文字层直 28 / 弯 0。8 页，1462.5 × 2025 pt。
- 交付网 PDF 复核末 SHA 仍为 `626e7588…`，未被覆盖。

## 15. C2 回归 — 已修

- text.md 中 `antes del jueves` **0 处**，`hasta el jueves 19` **5 处**。C2 不复现。

## 16. D5 字体（只记录，不判 (b)）

- SVG `<text>` 字体分布：Newsreader 973、Noto Sans CJK SC 632、Noto Serif CJK SC 43、UnifrakturMaguntia 1（与 re-proof/fix2 实测分布逐数一致）。D5 全周级已知待定项，只记录。

## 17. gates 汇总（`it-gates.json`，全部 rc=0）

```json
{"occlusion_rc": 0, "p8extract_rc": 0, "p8compare_rc": 0, "freeze_rc": 0,
 "freezediff_rc": 0, "creambox_rc": 0, "boxtitle_rc": 0, "keycheck_rc": 0,
 "sweep_rc": 0, "print_bytes": 3498553, "web_bytes": 882084,
 "print_sha": "12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724",
 "web_sha": "626e7588389b3c835eec0c8eebde974332ab27a90bca7a0dd2c5ffbdce19f6bd",
 "text_sha": "434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe",
 "text_lines": 1806, "pdftotext_rc": [0, 0], "print_web_text_equal": true,
 "print_web_text_bytes": 108723, "minfont_rc": 0}
```

## 本日志未覆盖的核查（已在 PROOF-NOTE.md 记录，均有实测）

- text.md 全文 1,806 行通读；150 题逐题三源手验 150/150（含 Q73 与 146/147 键—题干适配重点核）；范文 97 词（P8 SVG 实数）；P6 全页渲染目视干净；8 页逐页渲染目视；外部事实沿用 proof1 已核实结论，本轮通读无矛盾新表述。
