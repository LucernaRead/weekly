# PROOF-NOTE — 2026-W47 ru → pt (proof1，独立校对，重建版）

- 版：`2026-w47-ru-pt`（俄语目标 × 葡萄牙语读者），VOL.4，重建版（re-fanout，基于 core-ru fix1）
- 工作区：`~/workspace/weekly-git`，版目录 `production/2026-w47/2026-w47-ru-pt/`（规范路径）
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-pt2/`（专用，不与任何 agent 共用；全部验证产物在此）
- 方法：全文通读（text.md 838 行）+ 150 题逐题手验 + 全部机械门独立重跑（不信 KIT/重建报告，只信自己跑的结果）+ 首轮 proof1（pt1）7 项缺陷逐项复验 + 8 页 SVG/PDF 逐行实测
- 编号说明：本轮缺陷编号为 **R2-Dn**。首轮 pt1 的 D1/D2/D3 与重建方报告的 D1（地图 4 串）/D2（Q25）/D6（Q20）**编号重叠但所指不同**——下文每项均注明对应关系，避免混淆

## 三 SHA 实测（磁盘实测，与任务预期逐一核对）

| 文件 | 字节 | SHA-256 | 结论 |
|---|---|---|---|
| 印 `Lucerna-VOL4-ru-pt.pdf` | 21,205,597 | `59f01012f5c64fdddb73e1b73a50b448e21b8d2c68f59b740b4927a6f1444cdd` | ✓ 与预期一致 |
| 网 `Lucerna-VOL4-ru-pt-web.pdf` | 3,383,529 | `485a27b6be196e7f7d95c3b2d2e218ba3969ebe8fe084668ec20eea4f7bcff70` | ✓ 与预期一致 |
| 文 `2026-w47-ru-pt.text.md` | 65,155 | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` | ✓ 与预期一致 |
| 核心印 `core-ru/Lucerna-VOL4.pdf` | 31,429,147 | `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` | ✓（前缀 `d60fbd6c…`） |
| 核心网 `core-ru/Lucerna-VOL4-web.pdf` | 4,025,834 | `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` | ✓（前缀 `2f995f1d…`） |
| 核心文 `core-ru/2026-w47-ru-core.text.md` | 60,953 | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` | ✓（前缀 `348511e0…`） |

## 结论：(b) 有缺陷，不能定稿

共 **3 项缺陷**：MAJOR 1 项（R2-D1），minor 2 项（R2-D2、R2-D3）。全部三项均为**首轮已发现、重建未修复的存活缺陷**（重建只改了地图 4 串、Q25 短式、Q20 键，未动这三处）。
另有 1 项按任务指令只记录不判（D5，见“记录项”），2 项观察项（O1、O3）。

修复后须重跑全部机械门并重新复校受影响页（R2-D1 改标题文案/字号，R2-D2/R2-D3 缩短约 3–5px）。

## 缺陷清单

### R2-D1 — MAJOR · 本版 fan-out · P1 栏目标题横向溢出（= 首轮 pt1-D1，存活）

- 位置：P1 右栏「СЛОВО НЕДЕЛИ　A PALAVRA DA SEMANA」，y=1660，22pt 粗体，x=1439.5。源码 `content12.py:109`：`p.text(gx, my + 24, "СЛОВО НЕДЕЛИ　A PALAVRA DA SEMANA", 22, "sans", True, OLIVE)`（gx=COLX[3]=1439.5，栏宽 CW=422.5，栏右缘 1862；其下划线 `p.hline(gx, gx + gw, my + 38, …)` 亦止于 1862）
- 证据（右缘 = 1862，四法一致）：
  - PIL 真墨（本版 `svglib` 字体路由，22pt 粗体，含前导 U+3000 advance 22.0px）：墨右 **1886.5 → +24.5px**
  - PDF span advance（印 PDF，span origin 基线定位）：**1887.4 → +25.4px**
  - 印 PDF 3x 全页光栅（2.25 px/单位，`raster-p1.log`）：墨右 **1886.9 → +24.9px**
  - 印 PDF 4x 裁剪光栅（3.0 px/单位，`clip-D1-p1.png`）：墨右 **1887.0 → +25.0px**
- 存活证据：与首轮备份 `backup-old/2026-w47-ru-pt/svg/p1-pervaya.svg` 该行 runs 逐值相同（run-diff 中 P1 差异仅为 kicker 双空格 20 个 runs）；首轮实测亦为 1886（PDF）/ 1886.5（PIL）/ 1887.5（span）。重建未动此标题
- 原因：葡语 gloss `A PALAVRA DA SEMANA` 使标题总 advance 达 445.8（`svglib.text_w`），超栏宽 422.5
- 同类参照：ru-de 同批 D1 为 +36.6；本版为 +24.5~+25.4，同一缺陷类
- 修复：缩短标题（如减 gloss 或降字号）并重测四法全部 ≤1862。注意：本项与重建报告的 “D1”（地图 4 串，已落地，见下）不是同一缺陷；重建 gate 未覆盖无奶油盒的栏目标题，故漏网

### R2-D2 — minor · 本版 fan-out · P1 底部 quiz 桥接行轻微溢出（= 首轮 pt1-D2，存活）

- 位置：P1 底部 y=2348，`Leia a primeira página e escolha a resposta certa　Respostas na página 8`（行首为 `БЛИЦ-ВИКТОРИНА　QUIZ RELÂMPAGO`）。该行位置在简讯盒下方属设计（creambox 已分类），此处仅论其横向溢出
- 证据（右缘 = 1862）：
  - 印 PDF 3x 全页光栅：墨右 **1865.1 → +3.1px**
  - PDF span advance：**1867.0 → +5.0px**
  - PIL 真墨：1862.5（+0.5px）
  - 首轮印 PDF 渲染：1865（+3px；该行 SVG runs 与首轮备份逐值相同）
- 四法全部为正（+0.5 ~ +5.0），光栅实测 +3.1px 已超出 ±2px 抖动带
- 修复：缩短约 5px（如删 `a resposta certa` 的一个词或减一空格）

### R2-D3 — minor · 本版 fan-out · P2–P6 页脚说明行轻微溢出，5 处同一行（= 首轮 pt1-D3，存活）

- 位置：`Respostas na página 8　Os níveis podem misturar-se; procure pelo número do exercício`——P2 y=1876、P3 y=1648、P4 y=1939.3、P5 y=1648、P6 y=1866（各页 `УПРАЖНЕНИЯ　EXERCÍCIOS DA PÁGINA N` 同行）
- 证据（右缘 = 1862，五页同一数值）：
  - 印 PDF 3x 裁剪光栅（P2，`clip2-D3-P2-y1876.png`，新测）：墨右 **1864.9 → +2.9px**
  - PDF span advance：**1866.3 → +4.3px**（五页一致）
  - PIL 真墨：1862.3（+0.3px，五页一致）
  - 首轮印 PDF 渲染：1864（+2px，五页一致）
- 存活证据：p3/p4/p5 的 SVG 与首轮备份逐字节相同；p2/p6 的 run-diff 中该行无变化（p2 差异仅 Q25 选项、p6 差异仅 D1 免责声明）
- 修复：一处改动、五页同修，缩短约 5px

## 记录项（只记录，不判）

### D5 — 首轮 pt1-D5 · P8 答案说明行（按任务指令：只记录，不判）

- 位置：P8 y=1302，`Cada resposta com uma breve nota em português　✓ = texto modelo`（行首 `ОТВЕТЫ　RESPOSTAS — ORDENADAS POR PÁGINA; PROCURE O NÚMERO DO EXERCÍCIO`）
- 实测（右缘 = 1862）：
  - PIL 真墨：**1861.7（框内 +0.3px）**
  - PDF span advance：**1865.9（−3.9px）**
  - 首轮印 PDF 渲染：1864（+2px；该行 SVG runs 与首轮备份逐值相同）
  - 印 PDF 3x 裁剪光栅（新测，`clip2-D5-P8-y1302.png`）：墨右 **1864.4（+2.4px）**
- 本项不作缺陷判定（任务指令）。仅记录上述三法测量值与首轮值。

## 判为非缺陷的项（证据见 GATE-LOG）

1. **P1 统计框标题**：`ТУР В ЦИФРАХ　EM NÚMEROS`（23pt 粗体，`content12.py:48` box()）：PIL 真墨右 904.6，框右 961，余量 **+56.4px**——ru-de 同类 D1 在本版不存在；全部 28 行盒标题实测均在框内，最紧为 P1 `Стр. 2A2` +22.2px（非标题行）；与首轮备份逐行数值相同，无回归
2. **occlusion 42 TEXTX**： adjudication 42/42 CLEAR；NEW vs 核心 3 项为 U+3000 双语栏标题，ink gap 19–21px；0 LINEX/COVER/FOOTER/EDGE/BOXTITLE
3. **P2 cream box 末行降部（O3）**：`para o Avô Gelo.` 基线 1154.0，盒底 1159.0；PIL 真墨底（anchor="ls"）= **1159.00**，恰贴盒底（余量 +0.00px，未越出）。独立复现首轮 1158.98（+0.02）结论。余量为零，留作观察
4. **P1 `O QUE DIZEM OS MEDIA`（O1）**：四法：光栅 +0.9/+1.0、span +1.4、PIL +2.4、首轮渲染 0（贴边）。约 +1px，属光栅抖动/取整噪声，未见字形被裁；沿用首轮非缺陷结论；建议修 R2-D1 时顺手缩短 2–3px
5. **P7 toolbox**：creambox 最小 desc-clear +5.9，通过
6. **引号/CJK**：«/» 每页平衡（text.md 165/165）；“/” 仅 P7 一对（有意）；SVG 直引号 0；SVG CJK 仅 U+3000；text.md 0 CJK
7. **Morozko 图缺失**：构建条件跳过（run log `P8 morozko SKIPPED: no room`），freeze 移除的 14 个西里尔词确为该图注（核心 p8 y≥2450），+ Q46 `можно`，共 15 项全部有解释
8. **Q140 译注**：`a todos` 为地道问候许可，非缺陷（与首轮结论一致）
9. **Q150**：p8 键 `✓`，text.md 开放题说明，范文 97 词（80–100 内），与核心一致
10. **`___` 87 处**：text.md = 核心 = 87，模板缺口继承，不作缺陷
11. **印/网文字层**：逐页多重集相等，31,107 字符，差 0（空白剥离后的 pdftotext 分段噪声已消除；首轮 O2 同结论）

## 复验：重建已落地的修复（全部存活）

- **地图 D1（重建方编号）**：text.md L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、L596 `Большой тест недели + все ответы`；K1/K2 在 p6 SVG、K2 不在 text.md（SVG-only 设计）、K3 在 p7 SVG、K4 在 p8 SVG——全部落地
- **Kicker**：`content12.py:18` 双空格已落地；独立重测 PIL 间隙 [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]，最小 **5.9px ≥ 4px** ✓
- **Q25 D2（重建方编号）**：`content12.py:276` 选项为 `День студента` ✓；全称 ×2（版/核心一致）；并连带修复首轮 pt1-D4（P2 y=2162 行现真墨右 1663.8，余量 +198.2px）
- **Q20 D6**：`content12.py:257` 键 `желании` ✓；text.md ×2；p8 键 20 = `желании`；p8 SVG 答案行同步更新
- **pt1-D7（网 PDF 斜体，MAJOR）**：**已修复**——网 PDF 现含 `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`；P1 «чёрная пятница» 网/印均为斜体 16.12pt，span bbox 与印版逐值相同，闭引号紧贴，文字层均为 `чёрная пятница»`

## 核实摘要（机械门，全独立重跑，详见 GATE-LOG.md）

- run.py rc=0、TOTAL 150、0 溢出；重建 SVG 8/8 字节一致
- freeze 核心基线 8/8（正确路径：`--build core-ru --core-svg core-ru/svg`）；版内自比对 8/8（补充）；diff 移除 484/848，西里尔移除恰 15 项（Q46 `можно` + 14 图注词），新增 CJK 仅 U+3000 ×8，未解释 0
- occlusion 42 TEXTX / 0 LINEX，adjudication 42/42 CLEAR；p8 抽取 150/150，compare CLEAN，keydiff [137, 138, 139, 140]（四项均为正确葡语翻译键）；直接 keydiff vs 核心 ru-p8.json 相同
- check_core rc=0：golden BAD 0、gloss 0、孤儿 1（与核心相同）、碰撞 1（与核心相同）；s11 FAILURES: none，P8 最小字号 9.75pt
- 印/网文字层逐页一致（31,107 字符，差 0）
- 150 题逐题手验：题干与键逐项适配；五组配对块（20 题）逐组对照 SVG 选项原文；Q20/Q73/图表/日期/叙事/范文均核实；text.md 键 vs p8 键 147/150 逐字一致（3 处为正则解析伪影）
- 盒标题真墨 28 行实测（§6）；creambox 0 负 clearance、95 BELOW-WINDOW 全分类、与首轮扫描 0 差异；矩形横扫无出页/越缘
- 弯引号成对、CJK 仅 U+3000、禁词 0、`___` 87（=核心）
