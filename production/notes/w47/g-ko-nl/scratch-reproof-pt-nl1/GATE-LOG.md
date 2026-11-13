# GATE-LOG — 2026-W47 pt-nl re-proof 机械门实跑证据

复校：re-proof（独立复校，SOP §8.4），2026-11-11。工具链：`~/workspace/weekly-git/tools/venv/bin/python`；
正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与 proof1 所用同一文件）。
本目录（scratch）即证据存放处：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-nl1/`。
全程 `TMPDIR` 指向本目录下 `tmp/`，未用系统 /tmp。生产目录零写入（§11）。

## §0 身份核对（磁盘为准）

```
$ sha256sum A-Lucerna-VOL4.pdf A-Lucerna-VOL4-web.pdf 2026-w47-pt-nl.text.md
7404001d519ac57d932fb99a7f73d59c0036a5de8d4ef35c276a8a9bca335029  A-Lucerna-VOL4.pdf
f8119356b8032f6720de25567367a53911958fe51c194d2e1d366130bcca9be3  A-Lucerna-VOL4-web.pdf
6f8d4d5960326b69f7ad639dbedc3a15ec8972780e292b2e2c3625001b5532cd  2026-w47-pt-nl.text.md
A-Lucerna-VOL4.pdf 12935296 bytes / A-Lucerna-VOL4-web.pdf 1142955 bytes / 2026-w47-pt-nl.text.md 37559 bytes
```
三项 SHA 与任务消息完全一致。印/网 PDF 各 8 页（PyMuPDF 计数；页尺寸 1462.5×2025 pt，SVG 1950×2700，比例 0.75）。

## §1 run.py（副本内重跑，不动生产目录）— rc=0，TOTAL 150

`run-reproof.log`：将版目录完整复制到 `tmp/build-copy` 后运行，rc=0，`TOTAL 150`，
分级 A2 48 / B1 71 / B2 31；分页 1:10、2:18、3:18、4:18、5:18、6:18、7:12、8:38；
类型：Maak de zin af 61、Meerkeuze 49、Woordenschat koppelen 12、Zinnen bouwen 7、
Waar of niet waar 3、Cloze 13、Vertaling 4、Schrijven 1；model words 88。
副本重建的 8 页 SVG 与生产版 SVG **逐字节相同**（`cmp` 8/8 SAME）。

## §2 gates.py（原地只读重跑）— 16/16 PASS

`gates-reproof.log`：`[PASS]` ×16，`FAILURES: none`。逐项：
VOL.4 + 周日期；副标题主题；footer + 页码行 8/8；无 VOL.3 刊别残留（VOL.3 仅现于 P7 承诺引述）；
截稿注 + 决赛命名；P1 刊头行 fit 1820（`{330: 300.4, 372: 808.5}`）；同基线墨迹碰撞 0；
页框墨迹穿越 0（最小边距 L/R/T/B = [47.0, 47.5, 35.0, 32.0]——R 由 proof1 的 3.5（D6 标题）回到 47.5，与 D6 修净一致）；
P6 图表标签覆盖 0%；gloss 29 项枚举（P2–P6 各 6/6/6/6/5）；gloss 词头存活 0 缺失；
P7 金句 8 条各 2× + 页签 + 荷兰语；读者园地 5/5；图片 + 出处 5/5；
P7 金句区与预告框无交（末行基线 2351.17）；P1 头条 41 非空字符 ≤56。

## §3 occlusion_audit.py — 真实审计（未用 --selftest），三跑均为 0 flags

- 本版：`occlusion-reproof.log/json`：selftest OK（planted 6 类全部触发），`./svg: 0 flags`，`flag_count: 0`。
- core-pt：`occlusion-core-pt.log/json`：同样 0 flags。
- 本版带 `--core core-pt`：`occlusion-reproof-core.log`：`0 flags / core: 0 flags; NEW vs core: 0`。
- KIT 所称“1 个 P1 LINEX flag”未复现：其所称几何（墨顶 2312.8 vs 线框 [2311, 2313]）已不存在——Quiz 分隔线现为 y=2350.0，D1 末行墨迹 2311.6..2332.6，线在墨底之下 17.4px（见 PROOF-NOTE）。

## §4 正典 creambox.py 全版扫描（31 框）+ core-pt 对照

`creambox-reproof.log`（rc=0）与 `creambox-core-pt-reproof.log`（rc=0）。D1–D4 关键框：

| 页/框 | 框底（现版） | inside-only 末行 | clearance | desc-clear | proof1 旧值 |
|---|---|---|---|---|---|
| P1 KORTOM y=1874 | 2348.0 | 2327.6 `em Brasília. (Página 4)` | +20.4 | +14.4 | 框底 2310.0 / +9.6 |
| P3 日程 y=200 | 551.0 | 540.6 `16h30.` | +10.4 | +3.9 | 框底 525.0 / +14.9 |
| P6 时间线 y=200 | 854.0 | 840.8 `Página do Participante.` | +13.2 | +6.9 | 框底 840.0 / +28.6 |
| P7 A PALAVRA y=1157.5 | 1431.5 | 1427.0 `memorie aan verzet en cultuur.` | +4.5 | −1.5 | 同值（行已改写，无降部） |

其余 27 框 inside-only clearance 均为正（最小为 P2 E VOCÊ +5.0、P3/P4/P5 E VOCÊ +5.1、P5 数字 +5.4）；
BELOW-WINDOW 5 处均为下一栏目标题/注文（假阳性）。D1–D3 三框数值与 core-pt 逐字相同（框底/末基线/clearance 全同），证实为核心层修复。
P7-TOOLBOX 小结：3 框，min inside clearance +4.5，min desc-clear −1.5（即 D4 框，PIL 已证无降部、墨底恰为基线）。

## §5 freeze.py — 核心标准比对 8/8 + 版内自比对 8/8 + diff

- 核心标准比对（`freeze-baseline-core-reproof.log`）：`--build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg`，
  `baseline: 8/8 SVGs byte-identical (repointed files: none)`，8 页哈希逐一匹配；
  `core integrity: shipped core SVGs unchanged by the run`；build-copy 文件清单与 core-pt 目录逐一相同（已验）。
  注：首次以 `--core-svg core-pt`（目录本身）调用时工具中止（`ABORT: core svg dir has 0 SVGs, expected 8`），因 --core-svg 须指 svg 子目录；任务所称“均指 core-pt 目录”即此义，已按正确路径重跑。`freeze-baseline-reproof.log` 为该次中止记录。
- 版内自比对（`freeze-baseline-edition-reproof.log`）：`--build 2026-w47-pt-nl --core-svg 2026-w47-pt-nl/svg`，`8/8 SVGs byte-identical`。
- diff vs core-pt（`freeze-diff-reproof.log/json`）：各页增减字符串为讲解层替换；
  新增 CJK 合计 9 个，全部为 U+3000（P1 ×2、其余各页 ×1）；无新增中文/其他 CJK 实字。

## §6 p8.py — extract 150/150，compare CLEAN

- extract（`p8-extract-reproof.log/json`）：`svg/p8-avaliacao.svg: noted set = 150 of 150`，题号 1–150 连续无缺重。
- compare（`p8-compare-reproof.log/json`）：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
  须用 `--core-p8/--edition-p8` 显式路径：`--core-dir/--edition-dir --target nl` 会误取 `core-pt/svg/p8-toets.svg`（不存在）而 FileNotFoundError——target 决定的是读者语 P8 文件名，不适用于 core-pt（`p8-avaliacao.svg`）。
  - 137/138 为翻译题答案的读者语 rendering：137 `Vrijdag 20 november is een nationale feestdag.`、138 `Palmeiras won met 5–4 na strafschoppen.`，已逐字验为正确荷兰语译文（keycheck-150.json Q137/Q138），非缺陷。
- 印刷键与 text.md 答案对照：150/150 一致（`keycheck-150.json`；Q150 印刷键为 `✓` 标记，text.md 为 `✓ Zie de modeltekst…` 指向句，同一结论）。

## §7 印/网文字层比对、P8 字号、引号扫描、CJK/内部标签扫描、web 重渲染

- 印/网文字层：`pdftotext -layout` 印 111,218 字节、网 111,218 字节；**逐字节相同**（`cmp` 通过）；词多重集差 **0**（各 8,584 词；proof1 记 8,589 词为 pdftotext 参数/计数方法差，不影响差为 0 的结论）。
- web PDF 重渲染（仅 scratch 内）：`webpdf-reproof.log`，rc=0，`tmp/web-reproof.pdf` 1,142,958 字节（生产网 PDF 1,142,955 字节，+3 字节为已知的 fontTools wall-clock 写入 `head.modified`，不可复现）；其文字层与生产网 PDF **逐字节相同**；生产网 PDF 未被覆盖。
- P8 最小字号（PyMuPDF 实测印/网 P8 全部 394 spans）：最小 **9.75pt**（印/网一致），等于 SOP §1.1 下限 9.75pt；SVG 侧最小 font-size 13.0（×0.75 = 9.75pt）。178 个 span 为该字号。
- 斜体：SVG 1 处（P1 `« consciência »`）；印 PDF 斜体 span 1、网 PDF 斜体 span 1——1=1。
- 弯引号：SVG 可见文本中 U+201C/U+201D 各 2 次，仅 P8 E139/E140（荷兰语源句各一对，配对正确）；
  U+2019 全版 0 次；直引号（ASCII `'`）在可见文本中仅 1 处：P7 A2 `cair betekent 'vallen op een dag'`（见 PROOF-NOTE O1）。
- CJK：text.md 0 个 CJK 字符；8 页 SVG 可见文本 0 个 CJK 字符（仅 U+3000 分隔符与蛾标 `<title>` 内 3 字 `Lucerna 三色蛾`，非读者可见文本）。
- 内部标签：text.md 仅命中 `VOL.3` ×2（均在 P7 读者园地承诺引述中，gates 允许）；`翻譯/翻译/type/cover/SOP/W47/pt-nl` 均 0 命中；E 节为 `### E · Traduza`，无 type 标签。
- 日期星期：`TZ=America/Sao_Paulo date -d` 核实 2026-11-07 六、08 日、14 六、15 日、16 一、17 二、20 五、21 六、22 日、23 一、27 五、12-06 日，与文中全符。
- 工作日算术（P6）：16–30 日共 15 天；工作日 10 天（16、17、18、19、23、24、25、26、27、30）、周末+假日 5 天（20、21、22、28、29）；10+5=15；第 10 个工作日 = 11 月 30 日；与正文“27–30 日窗口（视 20 日是否计入）”的表述一致。

## §8 PIL 真墨迹专项（D1–D6、31 框标题、排除项）

方法：`ink_measure.py`——解析 SVG `<text>` 元素，以版内 `svglib._pil` 同款 PIL 字体、按元素 font-family/size/weight/italic 取字，`getbbox(anchor='ls')` 得相对基线的墨迹框；同基线多 run 取并集。像素法：`pixel_measure.py`——印 PDF 200dpi 渲染，阈值通道和 <450（墨 #302c28 和 132、灰 #6f675d 和 307；奶油底 690、纸 745），坐标换回 SVG 单位。

| 项 | 行/标题 | 框界 | PIL 墨迹 | 像素法 | 溢出 |
|---|---|---|---|---|---|
| D1 P1 | `em Brasília. (Página 4)` 基线 2327.6 | 底 2348.0 | 2311.6..2332.6 | 墨底 2331.8 | **框内 +15.4（PIL）/+16.2（像素）**；Quiz 线 y=2350 在墨底下 17.4px |
| D2 P3 | `16h30.` 基线 540.6 | 底 551.0 | 523.6..540.6 | 墨底 540.5 | **框内 +10.4/+10.5** |
| D3 P6 | `Página do Participante.` 基线 840.8 | 底 854.0 | 825.8..845.8 | 墨底 845.8 | **框内 +8.2/+8.2** |
| D4 P7 | `memorie aan verzet en cultuur.` 基线 1427.0 | 底 1431.5 | 1410.0..1427.0 | 墨底 1426.6 | **框内 +4.5/+4.9** |
| D5 P2 | 标题 `PARA NÃO ERRAR　Ezelsbruggetje` | 右 961.0 | 右缘 941.5 | 右缘 942.7 | **框内 +19.5/+18.3** |
| D6 P7 | 标题 `ERROS COMUNS　Fouten` | 右 1862.0 | 右缘 1747.5 | 右缘 1746.7 | **框内 +114.5/+115.3** |
| 排除 P2 E VOCÊ | `twee zinnen en stuur ze op.` | 底 909.0 | 底 909.0 | — | 0.0（贴边，不越边） |
| 排除 P3 E VOCÊ | `stuur ze op.` | 底 880.0 | 底 879.9 | — | −0.1（在内） |
| 排除 P4 E VOCÊ | `ze op.` | 底 905.0 | 底 904.9 | — | −0.1（在内） |
| 排除 P5 E VOCÊ | `Schrijf twee zinnen en stuur ze op.` | 底 811.5 | 底 811.4 | — | −0.1（在内） |
| 排除 P5 数字 | `2027.` | 底 513.0 | 底 507.6 | — | −5.4（在内；无降部） |

PDF span 法（PyMuPDF，SVG 换算 ×4/3）：D1 span 2312.9..2332.9（框底 2348，在内）；D2 524.8..546.4（框底 551，在内）；
D3 825.3..846.4（框底 854，在内）；D4 span 底 1432.8（span 框含字体下行空高，非真墨；PIL 1427.0/像素 1426.6 在内）；
D5 标题 span 右缘换算 944.4（框右 961，在内）；D6 标题 span 右缘换算 1748.8（框右 1862，在内）。
像素裁图证据：`crop-reproof-d1.png` … `crop-reproof-d6.png`；整版图 `page-reproof-p1.png` … `page-reproof-p8.png`（印 PDF 渲染，110dpi）。

### 31 框标题逐一 PIL 真墨量测（`ink-reproof.json`；title = 框内最小基线行；clearR = 框右 − 墨右，clearL = 墨左 − 框左）

| 页/框底 y | 框首行（标题/首行） | 墨右 | clearR | clearL |
|---|---|---|---|---|
| P1 数字框 786.2 | A SEMANA EM NÚMEROS　In cijfers | 1402.0 | +9.5 | +17.0 |
| P1 日历框 588.0 | A SEMANA, DIA A DIA | 1732.5 | +129.5 | +21.0 |
| P1 目录框 1238.4 | NESTA EDIÇÃO　In dit nummer | 1825.5 | +36.5 | +22.0 |
| P1 KORTOM 1874.0 | EM POUCAS PALAVRAS　KORTOM | 1853.5 | +8.5 | +22.0 |
| P2 PARA NÃO ERRAR 605.0 | PARA NÃO ERRAR　Ezelsbruggetje | 941.5 | **+19.5** | +18.0 |
| P2 gloss 858.0 | Uitleg — o feriadão een driedaags… | 868.5 | +92.5 | +18.0 |
| P2 VOCÊ SABIA 200.0 | VOCÊ SABIA? | 1611.5 | +250.5 | +21.0 |
| P2 E VOCÊ 545.0 | E VOCÊ?　Vertel over jezelf | 1780.5 | +81.5 | +22.0 |
| P2 日程格1 1618.0 | o feriado começa | 412.0 | +98.5 | +152.0 |
| P2 日程格2 1618.0 | Palmeiras × Flamengo, às | 944.5 | +16.5 | +152.0 |
| P2 日程格3 1618.0 | o fim do feriadão | 1313.0 | +98.5 | +152.0 |
| P2 日程格4 1618.0 | tudo volta ao normal | 1802.5 | +59.5 | +152.0 |
| P3 gloss 200.0 | Uitleg — o quilombo een dorp van… | 872.5 | +88.5 | +18.0 |
| P3 日程 200.0 | A SEMANA, DIA A DIA | 1702.5 | +159.5 | +21.0 |
| P3 E VOCÊ 577.0 | E VOCÊ?　Vertel over jezelf | 1780.5 | +81.5 | +22.0 |
| P3 记忆词 906.0 | PALAVRAS DA MEMÓRIA | 1716.5 | +145.5 | +22.0 |
| P4 gloss 270.5 | Uitleg — o agregado totaalscore · os… | 1352.0 | +59.5 | +18.0 |
| P4 finalistas 200.0 | OS FINALISTAS | 1628.5 | +233.5 | +22.0 |
| P4 E VOCÊ 602.0 | E VOCÊ?　Vertel over jezelf | 1780.5 | +81.5 | +22.0 |
| P5 计划 200.0 | O PLANO DA ESPERA | 787.5 | +173.5 | +18.0 |
| P5 gloss 891.5 | Uitleg — o gabarito antwoordmodel · … | 913.5 | +47.5 | +18.0 |
| P5 数字 200.0 | OS JOVENS EM NÚMEROS | 1761.5 | +100.5 | +22.0 |
| P5 E VOCÊ 539.0 | E VOCÊ?　Vertel over jezelf | 1780.5 | +81.5 | +22.0 |
| P6 gloss 343.4 | Uitleg — o prazo deadline · o dia útil… | 903.5 | +57.5 | +18.0 |
| P6 时间线 200.0 | O CAMINHO ATÉ O GABARITO | 1770.5 | +91.5 | +22.0 |
| P6 读数 866.0 | LER OS NÚMEROS | 1671.5 | +190.5 | +22.0 |
| P6 图表左 1594.0 | A CONTAGEM　do dia 16 ao dia 30 | 456.0 | +505.0 | +21.0 |
| P6 图表右 1594.0 | DOIS GABARITOS　um exame | 1314.0 | +548.0 | +22.0 |
| P7 工具箱 200.0 | ERROS COMUNS　Fouten | 1747.5 | **+114.5** | +22.0 |
| P7 词语 1157.5 | A PALAVRA　Woord van de week | 1824.5 | +37.5 | +21.0 |
| P7 读者园地 1453.5 | CARTAS DOS LEITORES | 1718.5 | +143.5 | +22.0 |

全框体横向扫描（8 页全部奶油框、全部行，墨迹右缘 vs 框右缘、左缘 vs 框左缘）：**0 处溢出**（`ink-reproof.json` 的 `horizontal_scan_flags` 为空）。
P1 框标题/副标题无横向溢出（KORTOM 标题墨迹右缘 1853.5 < 框 1862；刊头行 fit 1820 通过；顶栏三行墨迹右缘见 §2 gates）。
PDF span 实测全版文字最右为 P8 的 `✓markeert de modeltekst`（右缘 1864.7，页右余量 85.3px），无文字出页边。

## §9 check_s11（pt 改编，en 同一检查项）— ALL PASS

`check_s11_pt.py`（改编自 `scratch-fanout-en/check_s11.py`；页名/核心目录改为 core-pt/pt-nl；
en 专属字符串检查改为 pt P8 结构；P8 字号按 SVG 13.0 ×0.75 = 9.75pt 换算；Q150 号码文本有 2 个实例——练习题本体（带 B1 chip）与答案流重复 token（无 chip，与 core 相同），按“任一实例有 chip”判定）。
`check-s11-reproof.log`：colour set core 21 = edition 21（extra/missing 均为 none）；badge 颜色 A2/B1/B2 均在版内；
P8 min font-size SVG 13.0 → PDF 9.75pt；Q113–120、Q145–150 chip 全部 B1 OK；ESCREVA 写作头在；`Schrijven` 桥接在；
`ALL §1.1/P8 CHECKS PASS`，rc=0。
（首版脚本误将 Q150 的答案流重复 token 当作唯一实例报 MISSING，已修正判定逻辑并重跑通过——该 token 在 core-pt 同位置亦无 chip，见 KIT §53。）

## §10 150 题逐题手验

`keycheck-150.json`（`build_keycheck.py` 由 proof1 脚本改编，印刷键取自本次新鲜 `p8-extract-reproof.json`，text.md 键重新解析；
与 proof1 的 keycheck-150.json 逐题比对：**0 处不同**）+ `stems-reproof.txt`（8 页 SVG 可见文本按文档顺序）逐题对照题干。
每题 verdict 均为 pass；印刷键与 text.md 键 150/150 一致；答案本身已逐题对照题干与原文复核（方法与结论见 PROOF-NOTE 核实摘要）。
Q73 专门手验：题干与 Q70 同属一句 `Depois da prova, começa a espera pelo gabarito.`，Q70 填 `gabarito`、Q73 填 `espera`，配对唯一正确。
模型文：run.py 记 88 词；本次独立计数：SVG 模型文段（含 `Texto modelo:` 标签）90 词，减标签 2 词 = **88 词**，在 80–100 范围内。

## §11 未改动声明

复校全程只读版源文件；未改动、未重建、未 commit、未 push 任何版文件。
`pre-hashes.txt` 与 `post-hashes.txt`：版目录 43 个文件（不含 `__pycache__`）sha256 逐一相同。
run.py、freeze baseline、webpdf 重渲染均在 scratch 副本内进行（`tmp/build-copy`、`freeze-core`、`freeze-edition`、`tmp/web-reproof.pdf`）；
freeze 校验 shipped 核心 SVG 前后哈希未变（`core integrity: shipped core SVGs unchanged`）。
（注：复校结束后按用户本地存储规矩清理了可复现的中间副本——`tmp/build-copy`、`freeze-core/build-copy`、`freeze-edition/build-copy`；
日志/JSON/裁图/整版图/脚本保留在本目录。）
本目录新增文件：`PROOF-NOTE.md`、`GATE-LOG.md`、`keycheck-150.json`、`build_keycheck.py`、`keys-compact.txt`、
`ink_measure.py`、`ink-reproof.json`、`pixel_measure.py`、`pixel-reproof.json`、`check_s11_pt.py`、`reg-reproof.json`、
`stems-reproof.txt`、各门日志/JSON（`run-reproof.log`、`gates-reproof.log`、`occlusion-reproof.log/json`、
`occlusion-core-pt.log/json`、`occlusion-reproof-core.log/json`、`creambox-reproof.log`、`creambox-core-pt-reproof.log`、
`freeze-baseline-core-reproof.log`、`freeze-baseline-edition-reproof.log`、`freeze-diff-reproof.log/json`、
`p8-extract-reproof.log/json`、`p8-compare-reproof.log/json`、`check-s11-reproof.log`、`webpdf-reproof.log`、
`web-rerender.txt`）、裁图与整版图（`crop-reproof-*.png`、`page-reproof-p*.png`）、`print.txt`、`web.txt`、`probe.txt`、`pre-hashes.txt`、`post-hashes.txt`。
