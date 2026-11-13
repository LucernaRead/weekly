# GATE-LOG — W47 es-it fix1 后独立复校（re-proof）机械门逐门记录

- 版：2026-W47 es-it；复校：独立 re-proof（与 fix1 agent 6b7c9286 不同人）。
- 探针：`ls /dev/null` 存在 + `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` + goals 侧真实写文件成功（`probe.txt`），均通后开工。
- 工作区 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-it2/`（下称 S）。生产目录只读：未改任何生产文件，未 commit/push；网 PDF 只在 S 内重渲。
- 工具均用 `~/workspace/weekly-git/tools/venv/bin/python`。helper 脚本自 `scratch-fix-es-it2/` 原样复制（未改动，仅 `gates.py` 内 S 路径改为本 scratch）：`creambox.py`、`creambox_diag.py`、`boxtitle_core.py`、`keycheck_core.py`、`minfont.py`、`sweep_de.py`、`gates.py`。
- 前情：S 内原有前一轮 proof2（重建前旧 build）的 `PROOF-NOTE.md` / `GATE-LOG.md` 已归档为 `PROOF-NOTE-pre-fix-build.md` / `GATE-LOG-pre-fix-build.md`；本文件是重建后新 build 的记录。
- 驱动：`S/gates.py --skip-render it`（§1–§11；不含现场 render.py，因生产只读；run.py 改在 S/tmp 副本里跑，见 §0b）。freeze baseline 内部同样在 S 内副本重建，不碰生产。

## 0. SHA 与尺寸核对（任务书 + 盘上 sha256sum，复核前后各测一次，未变）

| 文件 | 尺寸（B） | SHA-256（盘上实测） | 任务书 |
|---|---|---|---|
| `La-Lucerna-VOL4-es-it.pdf` | 3,522,764 | `5af794cbd0454944099ba311597bade7d8eff0b2ede08ee0ba1c14bccd8bcb53` | 相符 |
| `La-Lucerna-VOL4-es-it-web.pdf` | 883,013 | `eb0b2635dfdd46d8d6bc6a392365c59f2582f906958bd2c6b3dbf12ba7694da1` | 相符（< 7 MB） |
| `2026-w47-es-it.text.md` | 45,232（1,806 行） | `81f41695cf1aef7e93152aed8c81f958fa43e57c7faada7bfe76284eb9f4f444` | 相符 |

- `pdfinfo`：印/网各 8 页，1462.5 × 2025 pt，PDF 1.7，未加密。

## 0b. run.py（scratch 副本，生产只读）— rc=0，TOTAL 150

- 方法：`cp -r` 生产目录至 `S/tmp/runcopy`（删 `__pycache__`），在副本内跑 `tools/venv/bin/python run.py`（日志 `run-copy.log`；副本事后已删除，日志留存）。
- 输出：rc=0；`P8 saved, TOTAL exercises: 150`；`by level {'A2': 50, 'B1': 72, 'B2': 28}`；`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；`by type {'Completare frasi': 48, 'Scelta multipla': 47, 'Abbinare parole': 12, 'Vero o falso': 8, 'Formare frasi': 7, 'Trasformare frasi': 10, 'Cloze (scelta)': 13, 'Traduci': 4, 'Scrivi': 1}`；`MODELO words: 97`；`ALL DONE`。
- 副本重建的 8 个 SVG 与 shipped 逐字节一致（`cmp` 8 行 `identical`）。

## 1. 印/网文字层同一 — 逐字节一致

- 命令：`pdftotext -layout` 印版 → `it-print.txt`，网版 → `it-web.txt`；`cmp`。
- 输出：两文件均为 **108,653 B**，逐字节一致（`it-gates.json`: `print_web_text_equal: true`）。
- 网版 P1/P3 经 `pdftoppm -r 150` 渲染目视（`renders/web-p1-1.png`、`web-p3-3.png`；裁图 `crops/web-p1-LEDIZIONE.png`、`crops/web-p3-lanima.png`），与印版一致；弯撇号空隙在网版同样存在（见 PROOF-NOTE E1-空隙 §5）。

## 2. occlusion 审计 — 0 flags

- 命令：`tools/occlusion_audit.py production/2026-w47/2026-w47-es-it/svg --json it-occlusion.json`（日志 `it-occlusion.log`）。
- 输出：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`production/2026-w47/2026-w47-es-it/svg: 0 flags`；`flag_count: 0`。

## 3. p8 extract — 150/150

- 命令：`tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150 --json it-p8-extract.json`（日志 `it-p8-extract.log`）。
- 输出：`noted set = 150 of 150 (parse: lines)`，集合 [1..150] 连续无缺重。

## 4. p8 compare（vs core-es）— CLEAN，keydiff=[137, 138]

- 命令：`tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 …/svg/p8-ejercicios.svg --total 150 --json it-p8-compare.json`（日志 `it-p8-compare.log`）。
- 输出：`core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
- keydiff 裁定（见 PROOF-NOTE §2）：137/138 皆为读者语不同导致的翻译题键差异，键与题干逐句对应，正确；其余 148 键与核心逐字节一致。

## 5. freeze baseline（S 内副本重建）— 8/8

- 命令：`tools/freeze.py baseline --build production/2026-w47/2026-w47-es-it --core-svg …/svg --out S/freeze-es-it`（日志 `it-freeze.log`）。
- 输出：8 行 `OK`（p1–p8，每页 shipped SHA = 重建 SHA：p1 `34e4382a…`、p2 `ebb5b030…`、p3 `48b6a117…`、p4 `5b64351f…`、p5 `bd784983…`、p6 `6815a76d…`、p7 `8a2699b4…`、p8 `5d24dcb2…`）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`；rc=0。

## 6. freeze diff（核心↔本版文本多重集差分）— CJK 新增 6，全为 U+3000

- 命令：`tools/freeze.py diff --core-svg production/2026-w47/core-es/svg --edition-svg …/svg --json it-freeze-diff.json`（日志 `it-freeze-diff.log`）。
- 输出：p1 +30/−38、p2 +49/−52、p3 +33/−30、p4 +33/−27、p5 +45/−48、p6 +18/−17、p7 +45/−46、p8 +161/−626；CJK core→edition：205→21、309→17、178→14、197→16、265→15、93→15、399→12、1030→14；**TOTAL added CJK characters: 6**（p1–p6 各 1 个 U+3000，P7/P8 0 个；与 proof1/fix1 一致，皆为 SOP §1.1 规定的全角空格分隔符）。

## 7. creambox 全版扫查 — 6 处负余量：5 处假阳性 + C1（真墨 +3.8）

- 命令：`S/creambox.py production/2026-w47/2026-w47-es-it/svg/*.svg`（日志 `it-creambox.log`）；逐项裁定用 `S/creambox_diag.py` 同组 SVG（日志 `it-creambox-diag.log`）。
- 全版负余量 6 处（与 proof1/fix1 同值同位置）：
  1. P1 `y=1317 bottom=1707.0`，−37.0，末行 `AHORA TÚ　TOCCA A TE`——**假阳性**：下一栏目标题（diag：owner-rect=NONE，head/caption/outside）。
  2. P1 `y=588 bottom=1308.0`，naive −44.0，末行 `EN ESTA EDICIÓN　IL NUMERO`——**假阳性**：下一栏目标题（diag：owner-rect=['y=1312']）。该盒 OWN 末行 `Cinque chiavi, zero numeri inventati.` 基线 1300.0，余量 +8.0，**真墨余量 +3.8**（见 C1）。
  3. P1 `y=1312 bottom=1652.0`，−24.0，末行 `LA PALABRA DE LA SEMANA`——**假阳性**：下一栏目标题。
  4. P1 `y=1874 bottom=2194.0`，−24.0，末行 `La urna y el sobre: votar por correo…`——**假阳性**：插图下方图注，盒外正常。
  5. P2 `y=200 bottom=1217.1`，−37.0，末行 `DECIR LA HORA`——**假阳性**：下一栏目标题。
  6. P3 `y=200 bottom=375.4`，−37.0，末行 `LO QUE QUEDA DE NOVIEMBRE`——**假阳性**：下一栏目标题。
- **C1 回归（proof2 的 C1 +3.8px，本轮独立重测）**：盒 `y=588` 高已由核心层 700→720（KIT 记载），盒底 **1308.0**（proof1 时为 1288.0）；OWN 末行基线 1300.0（+8.0）；PIL 真墨底 1304.2，**ink-clearance +3.8**（`it-creambox-diag.log` P1 第 4 行，逐字与 fix1 测值一致）。墨水未漫出盒底，C1 不列缺陷。diag 全版：0 负真墨余量（其余正余量见 `it-creambox-diag.log`，最小 +0.1 为 P5 `y=939` 盒）。
- 其余正余量盒：P1 +45.7（OWN）；P2 +47.7 / +5.3 / +6.2；P3 +5.3 / +1.9；P4 +47.7 / +110.8 / +6.3；P5 +46.6 / +47.7 / +5.4 / +1.9；P6 +55.7 / +19.4 / +35.2 / +35.2；P7 +42.5 / +26.5 / +5.7；P8 无奶油盒。

## 8. P8 最小字号 — 10.125 pt

- 命令：`S/minfont.py` 对印版 P8（日志 `it-minfont.log`）。
- 输出：`P8 min effective font size = 10.125 pt (n=375)`；分布 10.125–34.5 pt；`below 9.75pt: 0`。≥ SOP §1.1 下限 9.75 pt。

## 9. boxtitle 宽度 — 0 溢出

- 命令：`S/boxtitle_core.py …/svg`（日志 `it-boxtitle.log`）；occlusion BOXTITLE 类自检已触发、实测 0 flags（见 §2）。
- 输出：全版框题无一越出自身框界；最小余量 **+14.4**（P7 `ERRORES TÍPICOS　ERRORI TIPICI`，墨右缘 1847.6，框右 1862）；其余 +104.6 起。

## 10. keycheck — 149/150，仅 #150 ✓ 例外

- 命令：`S/keycheck_core.py <edition-dir> it-p8-extract.json`（日志 `it-keycheck.log`，结果 `keycheck-150.json`）。
- 输出：`REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；唯一 mismatch：`n=150 page=8 type=Scrivi: key='Domanda aperta — testo modello sotto in questa pagina' extracted='✓'`——开放写作题，✓ 指向范文（97 词，见 PROOF-NOTE §4），为约定例外。

## 11. sweep（桥接/孤儿/寡行）— 0 / 0 / 0

- 命令：`S/sweep_de.py <edition-dir>`（日志 `it-sweep.log`）。
- 输出：`box-vs-hline flags: 0`；`bridges found: 20` / `bridge orphans: 0`；`bridge widows: 0`；`DONE`。

## 12. 孤儿标点全版扫 — 0

- 方法：SVG 8 页全部 `<text>` 元素：纯标点元素 0、行首闭标点 0；text.md 纯标点行 0（均现场脚本实测，无日志文件，方法见 PROOF-NOTE §5）。

## 13. 弯撇号专项（本轮核心，见 PROOF-NOTE E1-空隙）

- 字体度量（fontTools 自测，`/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc` SC face idx 2，upm=1000）：U+2019 advance **1000**（1.000 em），U+0027 **278**，空格 224；对照 Newsreader-Regular（upm=2000）：U+2019 **512**（0.256 em），U+0027 432，空格 487。
- 28 处归类：sans 12 处（P1 ×1、P2 ×1、P3 ×2、P4 ×1、P5 ×2、P7 ×4、P8 ×1）+ Newsreader 16 处（P8 键）。
- 渲染证据：150 dpi 印版渲染（`renders/p-1.png`～`p-8.png`），12 处 sans 裁图全部目视有空隙（`crops/new-p*.png`，见 PROOF-NOTE 表）；Newsreader 对照 `crops/new-p8-Dove-lurna-newsreader.png` 紧贴；直撇号旧版对照 `crops/old-p1-LEDIZIONE-straight.png`、`crops/old-p3-lanima-straight.png` 紧贴。
- 墨迹间隙像素实测（150 dpi，亮度 <128 为墨）：新印 P1 最大白空隙 **24px**（旧直版 6px）；新印 P3 **28px**（旧直版 10px）；新网 P1/P3 同样 24px/28px。
- 字符核对：content 源弯 28（2/5/6/6/9）+ content8.py 直 10 处皆为代码引号（L133/L135 `e_['n']` 等）；text.md 弯 28 / 直 0；印版文字层含弯撇号的词 28 个；`diff` vs fix1 前 text.md 仅 28 字符 + 1 重排。

## 14. C2 回归 — 已修

- text.md 中 `antes del jueves` **0 处**，`hasta el jueves 19` **5 处**；WEEKLY-KIT.md:100 确认核心层共改。C2 不复现。

## 15. D5 字体（只记录，不判 (b)）

- SVG `<text>` 字体分布：Newsreader 973、Noto Sans CJK SC 632、Noto Serif CJK SC 43、UnifrakturMaguntia 1（与前一轮 proof2 一致）。sans 632 段按本轮口径：纯拉丁字母段 392、含 U+3000 段 99、仅标点/数字段 141（前一轮口径数值为 491/120/21，分布总数一致，仅分类边界不同）。D5 全周级已知待定项，只记录。

## 16. gates 汇总（`it-gates.json`，全部 rc=0）

```json
{"occlusion_rc": 0, "p8extract_rc": 0, "p8compare_rc": 0, "freeze_rc": 0,
 "freezediff_rc": 0, "creambox_rc": 0, "boxtitle_rc": 0, "keycheck_rc": 0,
 "sweep_rc": 0, "print_bytes": 3522764, "web_bytes": 883013,
 "print_sha": "5af794cbd0454944099ba311597bade7d8eff0b2ede08ee0ba1c14bccd8bcb53",
 "web_sha": "eb0b2635dfdd46d8d6bc6a392365c59f2582f906958bd2c6b3dbf12ba7694da1",
 "text_sha": "81f41695cf1aef7e93152aed8c81f958fa43e57c7faada7bfe76284eb9f4f444",
 "text_lines": 1806, "pdftotext_rc": [0, 0], "print_web_text_equal": true,
 "print_web_text_bytes": 108653, "minfont_rc": 0}
```

## 本日志未覆盖的核查（已在 PROOF-NOTE.md 记录，均有实测）

- text.md 全文 1,806 行通读；150 题逐题三源手验 150/150；范文 97 词（SVG 实数）；P6 全页渲染目视干净；外部事实沿用 proof1 已核实结论，本轮通读无矛盾新表述。
