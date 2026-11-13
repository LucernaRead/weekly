# GATE-LOG — W47 es-it proof2 机械门逐门记录（独立重建版复校）

- 版：2026-W47 es-it；复校：独立 proof2（与构建者/fan-out agent 不同人）。
- 探针：`ls /dev/null`（多次缺失/变为空白普通文件——`mknod` 容器无权限；`touch /dev/null` 垫回）+ `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，每次写盘前重探，均通；goals 侧真实写文件成功后才开工。
- TMPDIR 全程用 `hidden_files/w47/scratch/tmp`，未写 /tmp；工作目录 `hidden_files/w47/scratch-proof-es-it2/`（下称 S）。
- 工具均用 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，freeze 日志首行实测）。脚本复件（自 `scratch-refanout-es/` 原样复制，未改动，md5 见下）仅用于输出落点在本 scratch：`boxtitle_core.py` 34da50e2…、`check_p8keys.py` 50bd6a7c…、`creambox_diag.py` e0657560…、`keycheck_core.py` 5a77b026…、`minfont.py` 465bc46f…、`sweep_de.py` 04e8a620…。creambox 全扫查直接用 canonical `hidden_files/w47/tools/creambox.py`（未复制）。
- 驱动：`S/gates_run.sh`（§0–§15 顺序执行，日志均在 S 内）。

## 0. SHA 与尺寸核对（任务书 + KIT §9 + 盘上 sha256sum，复核前后各测一次）

| 文件 | 尺寸（B） | SHA-256（盘上实测，复核前 = 复核后） |
|---|---|---|
| `La-Lucerna-VOL4-es-it.pdf` | 3,498,553 | `12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724` |
| `La-Lucerna-VOL4-es-it-web.pdf` | 882,077 | `17d4b8efd2b997ce84f260f8dd1def296c145a3ade005a4885d41a4fc35cf4d8` |
| `2026-w47-es-it.text.md` | 45,176（1,806 行） | `434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe` |
| core-es `La-Lucerna-VOL4.pdf` | 17,212,955 | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` |
| core-es `La-Lucerna-VOL4-web.pdf` | 1,410,471 | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235` |
| core-es `2026-w47-es-zh-cn.text.md` | 1,822 行 | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` |

- 复核前后全量哈希：`before-hashes.txt` vs `after-hashes.txt`（es-it 35 文件）逐字节一致；core-es 同法 35 文件逐字节一致。`git status` 仅显示 es-it 目录未追踪（`??`），无任何修改。
- `pdfinfo`：印/网各 **8 页**，1462.5 × 2025 pt，PDF 1.7，未加密（`pdfinfo-print.log` / `pdfinfo-web.log`）。

## 1. run（源码重建，副本内 run.py）— rc=0，TOTAL 150，0 溢出

- 方法：edition 目录拷到 `S/rerun/`（tar，排除 `__pycache__` 与 `cards/`；tar 报 ownership 警告属容器限制，文件已拷全），在副本内跑 `tools/venv/bin/python run.py`（日志 `rerun.log`）。未在原地跑 `render.py`（它会重写 shipped PDF；等效验证见 §14 像素比对）。
- 输出：`TOTAL 150`，`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`，`by level {'A2': 50, 'B1': 72, 'B2': 28}`，`MODELO words: 97`；`FLOW OVERFLOW` 0 处、`HEAD TOO WIDE` 0 处；`flow[P8-keys] ended col 3/3 y=2521 (bottom 2560)`。
- 重建 SVG 与 shipped SVG SHA逐字节一致：`rerun-svg-diff.txt` 空（diff rc=0），8/8 相同。

## 2. occlusion 审计 — 0 flags

- 命令：`tools/occlusion_audit.py production/2026-w47/2026-w47-es-it/svg --json S/occlusion.json`（日志 `occlusion.log`）
- 输出：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`…/svg: 0 flags`；`occlusion.json: {"flag_count": 0, "flags": []}`。
- 结论：几何遮挡/细线穿字/页脚侵入/出页边/文本重叠/框题越界六类均为 0。

## 3. p8 extract — 150/150

- 命令：`tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150 --json p8-extract.json`（日志 `p8-extract.log`）
- 输出：`noted set = 150 of 150 (parse: lines)`，集合 [1..150] 连续无缺重。

## 4. p8 compare（vs core-es）— CLEAN，keydiff=[137, 138]

- 命令：`tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 …/svg/p8-ejercicios.svg --total 150 --json p8-compare.json`（日志 `p8-compare.log`；`gates.json` 的 p8 extra 若显示 "?" 是驱动误读键名——本轮直接读 `p8-compare.json`，无此问题）
- 输出：`core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
- keydiff 逐项说明（已裁决项，不得据此判 (b)）：
  - **137**：核心键为中文译句；本版键 `Lunedì è la Giornata internazionale del flamenco.`——题干 `El lunes es el Día del Flamenco. → ___`（西→意翻译题），键与题干逐句对应，正确。
  - **138**：同理。本版键 `Sabato guardiamo il derby di Siviglia.`——题干 `El sábado vemos el derbi Sevilla–Betis. → ___`，对应正确。
  - 其余 148 键与核心逐字节一致；139/140 题干为意大利语句、键为西班牙语句，两版一致。

## 5. source freeze（freeze.py baseline，重建渲染）— 8/8

- 命令：`tools/freeze.py baseline --build production/2026-w47/2026-w47-es-it --core-svg …/svg --out S/freeze-es-it-proof2`（日志 `freeze-baseline.log`）
- 输出：`baseline: 8/8 SVGs byte-identical`，8 行 `OK`（p1–p8，每页 shipped SHA = 重建 SHA）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`；rc=0。

## 6. string freeze（freeze.py diff）— 仅新增 U+3000 ×6，西语零丢失

- 命令：`tools/freeze.py diff --core-svg production/2026-w47/core-es/svg --edition-svg …/svg --json freeze-diff.json`（日志 `freeze-diff.log`）
- 输出：p1 +30/−38、p2 +49/−52、p3 +33/−30、p4 +33/−27、p5 +45/−48、p6 +18/−17、p7 +45/−46、p8 +161/−626；CJK core→edition：205→21、309→17、178→14、197→16、265→15、93→15、399→12、1024→14；**TOTAL added CJK characters: 6**。
- 逐项核实（`freeze-wordcheck.log`）：6 个新增 CJK 码点全为 U+3000（P1–P6 各 1，P7/P8 各 0）；新增串含非 U+3000 的 CJK **0**；`removed-es-words-missing-from-added: NONE`（被删的每个西语单词在新增串中均有对应；被删纯拉丁串 164 条皆为断行碎片，如 p5 `Después ___ (` / `enviar) el sobre.`）。
- SVG 内 CJK 全量分类（`cjk-classify.log`）：`<text>` 内 CJK 字符共 124 个，**全部为 U+3000**（P1 21 / P2 17 / P3 14 / P4 16 / P5 15 / P6 15 / P7 12 / P8 14）；`<text>` 外唯一 CJK 为 P1 moth `<title>三色蛾</title>`（非渲染，与核心一致）。

## 7. creambox 全版扫查（canonical）+ refined + 真墨 diag — 自有墨全部 ≥0

- 工具：canonical `hidden_files/w47/tools/creambox.py`（`creambox-all.log`）、同目录 `creambox_check.py`（refined，OVERFLOW 规则：基线落入 (bottom, bottom+8]，`creambox-check.log` 输出 `NO OVERFLOW`）、`creambox_diag.py` 真墨复核（`creambox-diag.log`）。
- 粗扫查 6 处负余量，逐项裁定（皆为假阳性，下一栏目标题/图注落入 +45px 窗口；自有末行墨 clearance 全部 ≥0）：
  1. P1 `y=1317 bottom=1707.0`，−37.0，`AHORA TÚ　TOCCA A TE`（基线 1744）——下一栏目标题；自有末行基线 1661.3，墨 clearance **+40.7**。
  2. P1 `y=588 bottom=1308.0`，−44.0，`EN ESTA EDICIÓN　IL NUMERO`（基线 1352）——下一盒（y=1312）的标题；**自有末行 `Cinque chiavi, zero numeri inventati.` 基线 1300.0，墨 clearance +3.8（C1 已修，proof1 为 −12.0）**。
  3. P1 `y=1312 bottom=1652.0`，−24.0，`LA PALABRA DE LA SEMANA`（基线 1676）——下一栏目标题；自有墨 clearance **+10.8**。
  4. P1 `y=1874 bottom=2194.0`，−24.0，图注 `La urna y el sobre: votar por correo…`（基线 2218）——插图下方图注；该盒内无文本。
  5. P2 `y=200 bottom=1217.1`，−37.0，`DECIR LA HORA`（基线 1254.1）——下一栏目标题；自有墨 clearance **+43.8**。
  6. P3 `y=200 bottom=375.4`，−37.0，`LO QUE QUEDA DE NOVIEMBRE`（基线 412.4）——下一栏目标题；自有墨 clearance **+47.5**。
- 真墨 clearance 全表：P1 +40.7/+3.8/+10.8（另两盒无文本）/+39.0；P2 +43.8/+42.5/**+0.1**（`¿SABÍAS QUE…?` 盒，末行 `ley.` 墨底 543.4 vs 盒底 543.5）/+5.9；P3 +47.5/+5.0/**+1.7**（`¿Y TÚ?`）；P4 +42.5/+105.8/**+1.3**（`¿Y TÚ?`）；P5 +41.3/+47.5/**+0.1**（`VOTAR POR PRIMERA VEZ` 盒，末行 `compara precios antes de pagar.` 墨底 1251.4 vs 盒底 1251.5）/**+1.7**（`¿Y TÚ?`）；P6 +50.9/+19.1/+31.2（/+30.8）；P7 +38.0/+22.0/**+1.5**（CARTAS 栏）。P8 无奶油盒。
- 两处 +0.1 与 core-es 同盒同坐标同数值逐字一致（`creambox-diag-core-p2p5.log`：core P2 同盒 `ley.` 墨 clearance +0.1、P5 同盒 `compara precios antes de pagar.` +0.1），属继承的核心几何，墨未出盒，非缺陷；P2/P5 渲染目视确认两行均在盒内。

## 8. boxtitle 宽度（真墨实测）— 25 盒全部正余量，0 溢出

- 命令：`boxtitle_core.py …/svg`（日志 `boxtitle.log`；PIL 4x 真宽，字体按元素 font-family/weight 解析）
- 结果：最紧 P7 `ERRORES TÍPICOS　ERRORI TIPICI` +14.4px；其余：P1 +35.0/+316.2/+41.2/+176.0、P2 +30.0/+22.2/+209.2/+168.0、P3 +20.1/+40.7/+168.0、P4 +65.6/+138.1/+168.0、P5 +20.7/+24.9/+103.9/+168.0、P6 +184.0/+202.4/+431.7/+526.0、P7 +118.5/+104.6。P1 两盒（y=1874 画板、y=1999 画框）盒内无文本，属设计。双语小文件标题越奶油盒右缘问题：0 处。

## 9. keycheck（REG vs 抽取）— 149/150

- 命令：`keycheck_core.py <edition-dir> p8-extract.json`（日志 `keycheck.log`，产物 `keycheck-150.json` 落在本 scratch）
- 输出：`REG entries: 150; p8extract keys: 150; exact match: 149/150`；唯一 mismatch：`n=150 type=Scrivi: key='Domanda aperta — testo modello sotto in questa pagina' extracted='✓'`（开放写作题，抽取器已知例外）。

## 10. p8keys 终 y 与 OVERFLOW — 终 y=2521，0 OVERFLOW

- 命令：`check_p8keys.py …/svg/p8-ejercicios.svg`（日志 `p8keys.log`）
- 输出：keys-area 138 行，130 个答案起始；multi-line 答案 7 个（6/9/23/62/63/27/74，皆为长注换行；另 41/43/44 等行为跨栏同 y 并行所致，无溢出）；与 rerun 的 `flow[P8-keys] ended col 3/3 y=2521 (bottom 2560)` 一致，0 OVERFLOW。

## 11. sweep（bridge/band spans + box-vs-hline）— 0

- 命令：`sweep_de.py <edition-dir>`（日志 `sweep.log`）
- 输出：`box-vs-hline flags: 0`；`bridges found: 20, bridge orphans: 0`；`bridge widows: 0`。

## 12. p8 font（minfont）— 10.125 pt

- 命令：`minfont.py <print-pdf>`（日志 `p8-minfont.log`；pypdf visitor，有效字号 = font_size × |Tm[0]|）
- 输出：`P8 min effective font size = 10.125 pt (n=375)`；分布 10.125–34.5 pt；`below 9.75pt: 0`。

## 13. text layer 印/网逐字节一致 — 108,723 B

- 命令：`pdftotext -layout` 印版 → `print.txt`、网版 → `web.txt`；`cmp`（`gates_run.sh` §15）
- 输出：两文件均为 108,723 B，`cmp` 逐字节一致。文字层撇号：印/网各直 ×28、弯 ×0（见 §17）。

## 14. 像素比对（印 vs 网、印 vs SVG 直接渲染）

- 方法：`pdftoppm -r 96` 印/网各 8 页（`png-print/`、`png-web/`）+ cairosvg 直渲 8 SVG（`png-svg/`，1950×2700），PIL 逐像素 mean|d|（`pixeldiff.log`、`pixeldiff2.log`）。
- 印 vs 网：P1 0.091、P2 0.000、P3 0.129、P4 0.000、P5 0.290、P6 0.000、P7 0.119、P8 0.256（网版图片重压缩所致微差）。
- 印 vs SVG 直渲：P1 4.981、P2 5.382、P3 3.982、P4 4.615、P5 4.659、P6 5.669、P7 5.595、P8 8.905；>100 差异像素遍布全页文字边缘（frac>100 0.014–0.037，bbox 均为 x~88..1885 y~106..2626），无局部内容差异——为 poppler 与 cairosvg 光栅化抗锯齿差异（P8 文字最密故最高）。内容同一由 freeze 8/8 + 文字层逐字节一致保证。

## 15. chips（rx="2.7" level 芯片）— 141 个，全部 fits

- 方法：逐页统计 `rx="2.7"` 矩形 + PIL 真宽复测芯片内文字是否超芯片右缘（`chips-fonts.log`）
- 结果：P1 10（A2 8/B1 2）、P2 15（A2 13/B1 2）、P3 18（A2 11/B1 7）、P4 15（B1）、P5 18（B1）、P6 18（B2）、P7 12（A2/B1/B2 各 4）、P8 35（A2 11/B1 21/B2 3）；**合计 141，bad=0**。

## 16. mcq（选择题键有效性）— 60 项全部合法

- 方法：`keycheck-150.json`（REG）按题型核查键值域（`mcq-check.log`）
- 结果：Scelta multipla 47 + Cloze (scelta) 13 = **60 项，键全部 ∈ {A,B,C}**；Abbinare parole 12 项，键全部 ∈ {a,b,c,d}；Vero o falso 8 项，键全部 ∈ {Verdadero,Falso}；REG≠抽取仅 #150。

## 17. 撇号实测（必查项）— 直 ×28 / 弯 ×0（三处一致）

- 方法：逐字符计数 + 逐处上下文（`apostrophe.txt`）
- text.md：U+0027 **×28**、U+2019 **×0**、U+2018 ×0、U+201C/U+201D ×0、直双引号 ×0；«/» 各 56。
- SVG：直 **×28**（P1 1 / P2 1 / P3 2 / P4 1 / P5 2 / P6 0 / P7 4 / P8 17）、弯 **×0**。
- 印/网文字层：直 ×28、弯 ×0（与 SVG 一致）。
- 28 处全部为意大利语省音（逐处清单与源码位置见 PROOF-NOTE.md E1：`content12.py:21/:275`、`content34.py:22/:61/:87/:93/:168`、`content56.py:29/:66/:86/:107/:218/:237`、`content7.py:20/:21/:27/:52/:69/:124`、`content8.py:44/:67/:70/:72/:86/:91/:93(×2)/:100`）；无一处属于代码或专名原名。KIT §9 称 "text.md shows 4× straight" 与实测 28× 不符（4 仅为 `Leggi l'articolo` 桥接句数）。
- 结论：按本轮标准，直撇号残留即缺陷——**E1，(b)**。

## 18. 字体/D5（只记录，不判 (b)）

- 方法：SVG `<text>` 字体分布 + Noto Sans CJK SC 内纯拉丁字母元素计数（`chips-fonts.log`、`fonts-core.log`）
- 本版：Newsreader 973、Noto Sans CJK SC 632、Noto Serif CJK SC 43、UnifrakturMaguntia 1；Noto Sans CJK SC 中纯拉丁字母元素 **491 段**（P1 62 / P2 62 / P3 63 / P4 61 / P5 62 / P6 51 / P7 60 / P8 70）。
- 对照 core-es：Noto Sans CJK SC 608（纯拉丁 259、CJK 含 208）；**净增 +232 段**。另含 U+3000 的 sans 元素 120 段、仅标点/数字的 sans 元素 21 段（632 = 491 + 120 + 21）。全周级已知待定项，只记录。

## 19. 三源交叉核对（150 题）

- P8-extract vs REG（keycheck）：149/150（仅 #150 例外）；P8-extract vs 核心（p8 compare）：CLEAN [137,138]；P8-extract vs text.md 答案区：`N. <key>` 逐字比对 **150/150**（`triple-check3.log`；初版 `triple-check.log` 的 27 处“不符”为本脚本栏位并行拼接造成的解析假象，经逐字子串复核 + 全文目读确认全部相符）。
- 逐题对题干手验 150/150 通过（见 PROOF-NOTE.md）。

## 20. 其他机械核查

- 弯引号：«/» text.md 56/56；SVG 逐页 2/10/2/0/1/3/31/7 = 56，成对；U+201C/U+201D/直双引号 0。
- 禁词：text.md `SOP`/`proofread`/`cover`/`12 de noviembre` 0；VOL.4 印刷层 9 次 + 刊头 `VOL. 4` 1 次；VOL.5 ×3（P7 下期预告）。
- `hasta el jueves` ×7、`antes del jueves` ×0、`sábado veo el derbi` ×1（text.md）。
- 日期星期（Europe/Madrid `date -d`）：9 日周一、10 日周二、13 日周五、16 日周一、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、25 日周三、26 日周四、27 日周五、28 日周六、29 日周日，全部吻合。
- "next Sunday"：es-it 全版（.py/.svg/.md）0 处；core-es 内 0 处；任务书所引行号（content12.py:37/:113、content34.py:127）按盘上实测属 core-zh-tw 的英文 gloss，不在 core-es 内。本版无此问题。
- ABSTRACT.txt：意大利语单行 471 B，无 ASCII 双引号，事实无误。KIT §9 新 SHA 与盘上实测完全一致。
- 8 页印版逐页渲染目视（`view/p1–p8.png`）+ 网页版 P8 渲染目视：无溢出/重叠/压页脚/缺字/豆腐块。

## 本日志未覆盖的核查（已在 PROOF-NOTE.md 记录，均有实测）

- text.md 全文 1,806 行通读；150 题逐题对题干核对；P7 金句 8/8 逐字核对；跨页引用页码核对；外部事实沿用 proof1 逐项核实结论 + 本轮复核重建新增点（RTVE debate-a-ocho 时间轴行、德比信行）。
- 未独立锁定的两项（沿用 proof1，不列为缺陷）：RTVE 195 分钟逐项第二来源；Sargent 图年份 1880–81 到年精度。
