# GATE-LOG — W47 es-it proof1 机械门逐门记录

- 版：2026-W47 es-it；复校：独立 proof1；探针：`git hash-object` 成功（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）+ scratch 写入成功（2026-11-11T09:55:18Z）。
- TMPDIR 全程用 `hidden_files/w47/scratch-proof-es-it1/tmp`，未写 /tmp，未删他人文件，未改源文件，未 commit/push。
- 工具均用 `~/workspace/weekly-git/tools/venv/bin/python`。

## 0. SHA 与尺寸核对（KIT §7 + 盘上 sha256sum）

| 文件 | 尺寸（B） | SHA-256（盘上实测） | KIT |
|---|---|---|---|
| `La-Lucerna-VOL4-es-it.pdf` | 3,498,408 | `d4eaaf2fd3f955c17140f3a648ccfef538fa21564a5dde28f71e5da1ee96a2a7` | 相符 |
| `La-Lucerna-VOL4-es-it-web.pdf` | 845,673 | `24bd25008151e3dd14d7e2d8769aa541781bd9dc3ffc2a0006aca5ba4e70a435` | 相符（< 7 MB） |
| `2026-w47-es-it.text.md` | 44,644（1,788 行） | `a2c3606482b56d17fd191b5998c76307fb4e696e4b1a5225ea498586e01e5181` | 相符 |

- `pdfinfo`：印/网各 **8 页**，1462.5 × 2025 pt，PDF 1.7，未加密。

## 1. 印/网文字层同一

- `pdftotext` 印版 `print.txt` 45,642 B；网版 `web.txt` 45,642 B；`cmp` **逐字节一致**。
- 网版 P1/P8 经 `pdftoppm -r 72` 渲染目视（`web-p1-1.png`、`web-p8-8.png`），与印版一致，无豆腐块、无缺字。

## 2. occlusion 审计 — 0 flags

- 命令：`tools/occlusion_audit.py production/2026-w47/2026-w47-es-it/svg`（日志 `occlusion.log`）
- 输出：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`production/2026-w47/2026-w47-es-it/svg: 0 flags`
- 结论：几何遮挡/细线穿字/页脚侵入/出页边/文本重叠/框题越界六类均为 0。

## 3. p8 extract — 150/150

- 命令：`tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150 --json p8-extract.json`（日志 `p8-extract.log` / `p8-extract2.log`）
- 输出：`noted set = 150 of 150 (parse: lines)`，集合 [1..150] 连续无缺重。
- 150 键已逐题人工核对题干/原文/图表（见 PROOF-NOTE.md），全部一致。

## 4. p8 compare（vs core-es）— CLEAN，keydiff=[137, 138]

- 命令：`tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 production/2026-w47/2026-w47-es-it/svg/p8-ejercicios.svg --total 150 --json p8-compare.json`（日志 `p8-compare.log`）
- 输出：`core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`
- keydiff 逐项说明：
  - **137**：核心键为中文译句（读者语=中文）；本版键 `Lunedì è la Giornata internazionale del flamenco.`——题干 `El lunes es el Día del Flamenco. → ___`（西→意翻译题），键与题干逐句对应，正确。差异纯因读者语不同，符合 W45/W46 ES×EN 裁定。
  - **138**：同理。核心键中文；本版键 `Sabato guardiamo il derby di Siviglia.`——题干 `El sábado vemos el derbi Sevilla–Betis. → ___`，对应正确。
  - 其余 148 键与核心逐字节一致；139/140 题干为意大利语句、键为西班牙语句，两版一致（`El voto por correo se pide antes del jueves 19.` / `Cada promesa tiene que llevar datos.`）。

## 5. freeze baseline（重建渲染）— 8/8

- 命令：`tools/freeze.py baseline --build production/2026-w47/2026-w47-es-it --core-svg production/2026-w47/2026-w47-es-it/svg --out scratch-proof-es-it1/freeze-es-it-proof1`（日志 `freeze-baseline.log`）
- 输出：8 行 `OK`（p1–p8，每页 shipped SHA = 重建 SHA）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`；rc=0。

## 6. freeze diff（核心↔本版文本多重集差分）— 西语零丢失

- 命令：`tools/freeze.py diff --core-svg production/2026-w47/core-es/svg --edition-svg production/2026-w47/2026-w47-es-it/svg --json freeze-diff.json`（日志 `freeze-diff.log`）
- 输出：p1 +30/−38、p2 +49/−52、p3 +33/−30、p4 +33/−27、p5 +45/−48、p6 +18/−17、p7 +45/−46、p8 +161/−626；CJK core→edition：205→21、309→17、178→14、197→16、265→15、93→15、399→12、1024→14；**TOTAL added CJK characters: 6**。
- 逐项核实：6 个新增 CJK 码点全为 U+3000（全角空格，SOP §1.1 规定的分隔符，每页 1 个，实为新增的家具分隔）；删除串全部为中文讲解层或西语断行碎片；被删的每个西语单词在新增串中均有对应（词级核对：8 页 `removed-es-words-missing-from-added: NONE`）；新增串无任何 CJK 汉字。可见文本层 CJK 仅剩 U+3000（8 页 SVG `<text>` 元素逐页核查）+ 非渲染的 moth `<title>三色蛾</title>`（与核心一致，KIT §6.12 已记录）。

## 7. creambox 全版扫查 — P7 干净；全版 6 处负余量，5 处假阳性，1 处真缺陷（核心级）

- 工具：`creambox.py`（取自同族 `scratch-proof-es-fr1/creambox.py`，复制到本 scratch 未改动；另用同目录 `creambox_diag.py` 逐项裁定）。命令：`creambox.py production/2026-w47/2026-w47-es-it/svg/*.svg`（日志 `creambox-all.log`；P7 单独 `creambox-p7.log`）。
- **P7（必查项）**：3 盒全部正余量——
  - `y=441 bottom=1064.0` 末行基线 1021.5，余量 **+42.5**（ERRORES TÍPICOS 栏）
  - `y=1080 bottom=1376.0` 末行基线 1349.5，余量 **+26.5**（LA PALABRA 栏）
  - `y=1392 bottom=1865.5` 末行基线 1859.8，余量 **+5.7**（CARTAS 栏，末行 `esempio. La promessa passa al VOL.5.`）
  - 结论：P7 工具盒无墨水漫出盒底。
- **全版其余盒**：26 盒；负余量 6 处，逐项裁定（裁图见本目录 `crop-*.png`）：
  1. P1 `y=1317 bottom=1707.0`，−37.0，末行 `AHORA TÚ　TOCCA A TE`（基线 1744）——**假阳性**：下一栏目标题，字顶在盒底之下约 19 px，盒内末行基线 1661.3 在盒内。裁图 `crop-p1-ahoratutop.png`。
  2. P1 `y=588 bottom=1288.0`，−12.0，末行 `Cinque chiavi, zero numeri inventati.`（基线 1300）——**真缺陷（核心级，PROOF-NOTE C1）**：该行属盒内 gloss 内容，印在盒底之外的白纸上；核心同盒同坐标亦然。裁图 `crop-p1-cincoclaves-bottom.png`。
  3. P1 `y=1312 bottom=1652.0`，−24.0，末行 `LA PALABRA DE LA SEMANA`（基线 1676）——**假阳性**：下一栏目标题，字顶在盒底之下约 8 px。裁图 `crop-p1-lapalabra-top.png`。
  4. P1 `y=1874 bottom=2194.0`，−24.0，末行 `La urna y el sobre: votar por correo…`（基线 2218）——**假阳性**：插图下方的图注，正常在盒外；盒内无末行溢出。裁图 `crop-p1-urna-caption.png`。
  5. P2 `y=200 bottom=1217.1`，−37.0，末行 `DECIR LA HORA`（基线 1254.1）——**假阳性**：下一栏目标题。裁图 `crop-p2-decirlahora-top.png`。
  6. P3 `y=200 bottom=375.4`，−37.0，末行 `LO QUE QUEDA DE NOVIEMBRE`（基线 412.4）——**假阳性**：下一栏目标题。裁图 `crop-p3-loquequeda-top.png`。
  - 其余正余量盒：P1 +44.0；P2 +47.7 / +5.3 / +6.2；P3 +5.3 / +1.9；P4 +47.7 / +110.8 / +6.3；P5 +46.6 / +47.7 / +5.4 / +1.9；P6 +55.7 / +19.4 / +35.2 / +35.2；P8 无奶油盒。
  - 注：es-fr 版同位置亦有相同的 6 处负值（−37/−12/−24/−24/−37/−37），第 2 处数值完全一致，佐证 C1 为核心几何。

## 8. P8 最小字号 — 10.125 pt

- 方法：tools venv 的 pypdf 解析印版 P8 文字矩阵有效字号（`font_size × |Tm[0]|`，日志 `p8-minfont.log`）。
- 结果：P8 有效字号分布 10.125–34.5 pt（n=375）；**最小 10.125 pt**（答案键行），≥ SOP §1.1 下限 9.75 pt；次低 10.5 pt。与 KIT 测值一致。

## 9. boxtitle 宽度 — 0 flags

- occlusion 审计的 BOXTITLE 类（含框题墨迹 vs 自身框界）自检已触发、实测 0 flags（见 §2）。全版无框题越出自身框界。

## 10. 其他机械核查

- 弯引号：«/» 全版各 56 处，逐页成对（P1 2/2、P2 10/10、P3 2/2、P4 0/0、P5 1/1、P6 3/3、P7 31/31、P8 7/7）；直双引号 0。
- 撇号：意大利语省音撇号 28 处，直撇号 27 处、弯撇号 1 处（P2 C 组引言，PROOF-NOTE E1）。
- 禁词：text.md CJK 0；`SOP`/`proofread`/`cover`/`12 de noviembre`/桥接 0；VOL.4 印刷层 9 次 + 刊头 `VOL. 4` 1 次；VOL.5 3 次均为合法下期预告。
- 题量分布：P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38，合计 150；级别 A2 50 / B1 72 / B2 28（与 KIT 一致，由题号区间 1–10 / 11–28 / 29–46 / 47–64 / 65–82 / 83–100 / 101–112 / 113–150 核对）。
- ABSTRACT.txt：意大利语单行，无 ASCII 双引号，含刊名、目标语名、A2–B2、150 esercizi 与本期真实主题词。
- 日期星期：`date`（Europe/Madrid）逐项校验 11 月 9/10/13/16/19/20/21/22/23/24/25/26/27/28/29 日，星期全部吻合；16 日→29 日为 13 天，与头条“trece días”一致。
- 模型范文：P8 H 组范文逐词数过，97 词，在 80–100 词要求内。

## 11. 本日志未覆盖的核查（已在 PROOF-NOTE.md 记录，均有实测）

- 8 页印版全目视（`cards/p1–p8`）+ 网页版 P1/P8 渲染目视；无溢出/重叠/压页脚（occlusion 0 flags 佐证）。
- 外部事实逐项核实：大选日历、邮寄投票、辩论、西甲、欧冠、弗拉门戈、圣塞西莉亚、MiDNI、毕尔巴鄂乐队、Sargent 图、RTVE 分钟数——见 PROOF-NOTE.md“已核实无误的要点”。
- 未独立锁定的两项（不列为缺陷）：RTVE 195 分钟逐项第二来源；Sargent 图年份 1880–81 到年精度。
