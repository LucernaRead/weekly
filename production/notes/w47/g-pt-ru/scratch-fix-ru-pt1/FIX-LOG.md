# FIX-LOG — 2026-W47 ru-pt fix1

- 版：`production/2026-w47/2026-w47-ru-pt/`（俄语 × 葡萄牙语读者），VOL.4
- 修复员：ru-pt fix1（subagent），2026-11-11
- scratch（唯一）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-pt1/`
- 仓库：`~/workspace/weekly-git`；Python：`tools/venv/bin/python`
- 未 commit、未 push。只改本版；核心 core-ru 与其他版未碰。

## §0 开工身份核对（与任务一致，磁盘实测）

| 件 | 开工 SHA-256 | 大小 |
|---|---|---|
| 印 `Lucerna-VOL4-ru-pt.pdf` | `59f01012f5c64fdddb73e1b73a50b448e21b8d2c68f59b740b4927a6f1444cdd` | 21,205,597 B |
| 网 `Lucerna-VOL4-ru-pt-web.pdf` | `485a27b6be196e7f7d95c3b2d2e218ba3969ebe8fe084668ec20eea4f7bcff70` | 3,383,529 B |
| 文 `2026-w47-ru-pt.text.md` | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` | 65,155 B |

三 SHA 全部相符后才开工。另先读 repo 根 `SOP.md`（§1.1、§8.4）与
`hidden_files/w47/briefs/brief-coordinator.md`，以及 proof1 的
`scratch-proof-ru-pt1/PROOF-NOTE.md` + `GATE-LOG.md`。

## §0.5 重要前情：开工时树里已有中间重建的 D4/D6 修复（非我所改）

proof1 描述的 D4（P2 选项 `b. Международный день студента`，+6px）与 D6（Q20 键
`желание` 应为 `желании`）在开工时**已在源码与交付件中修好**——它们属于任务所说的
「重建」那一棒，不属于本次三项：

- `content12.py:261-265` 已有 `желании` + `# D6 fix (2026-11-11)` 注释；
  开工态 text.md 第 173/694 行键即 `желании`（磁盘实测）。
- `content12.py:280` 已有 `"День студента"  # D2 fix (2026-11-11)` 注释
  （原 `Международный день студента`，match_set wrap 预算漏 `b. ` 前缀致 +8px）。
- 时间链：源码 `content12.py` 14:24 → 印 PDF 14:28 → 网 PDF 14:30 → text.md 14:31，
  即交付件由已修源码构建。
- 后果：本次重建后 P2 全局光栅扫描**零**越界行（D4 已无）；Q20/Q25/Q73 键复核通过
  （见 GATE-LOG §7）。D4/D6 不在本次改动内，我未动它们。
- 一点未竟核对：开工态网 PDF 的 D4 波段复测渲染在 VM 高负载下 >9 分钟未完成，
  我在确认上述三点证据后终止了该渲染（只读任务，无文件改动），以免阻塞 webpdf 重建。
  D4 已修的结论不依赖这一项复测。

## §1 三项修复（源码行 + 修法 + 实测）

右缘基准：栏右缘 / 内容右缘 = 1862 px（`RIGHT = MX + 4·CW + 3·GUT = 88 + 1690 + 84`；
`bslib4.py` 内联注释写 `# 1885` 是旧错注，未动）。
量测口径：以交付**印 PDF 的 MuPDF 光栅像素**为准（1950 px 宽渲染），PIL 真墨 + PDF span
交叉验证。PIL 真墨按 proof1 修正法：计入行首空白 advance（U+3000 在 22pt = 22px），
降部用 `anchor="ls"`。

### R2-D1 MAJOR — P1 框标题超栏右缘（content12.py:113，旧 109 行）

- 旧：`p.text(gx, my + 24, "СЛОВО НЕДЕЛИ　A PALAVRA DA SEMANA", 22, "sans", True, OLIVE)`，
  gx=1439.5（COLX[3]），框右缘 gx+gw=1862；旧实测 PIL 真墨 1886.5（+24.5）、span 1887.4、
  印 PDF 光栅 1886.9、4x 裁剪光栅 1887.0。
- 修法（缩短葡语副标题，字号 22 不变）：`A PALAVRA DA SEMANA` → `PALAVRA SEMANAL`
  （"weekly word"，同义；俄语头 `СЛОВО НЕДЕЛИ` 不动；其下划线 `p.hline(gx, gx+gw, …)` 不动，
  标题现止于线内）。候选实测（PIL）：仅删 `A ` → 1865.5（−3.5，仍超）；`PALAVRA SEMANAL`
  → 1842.5（+19.5）；降 20pt 原文 → 1843.5。取 `PALAVRA SEMANAL`。
- 无翻译表/登记键：全仓 grep 仅本版两处含 `A PALAVRA DA SEMANA`——本行与
  `content7.py:88` 的 P7 框标题 `"СЛОВО　A PALAVRA DA SEMANA"`（23pt，另一字符串，
  proof1 未报，不动）；KIT、text.md、cover.json 均无此串；text.md 导出器只收
  sans-bold ≥24 标题（本行 22pt），故 text.md 不受影响（§5 验证字节一致）。
- 修后实测（新印 PDF）：**光栅 1844（余量 +18）**；PIL 真墨 1842.5（+19.5）；
  span advance 1844.4（+17.6）；网 PDF span 1846.2。证据裁图 `crop-p1-palavra-fix1.png`。

### R2-D2 minor — P1 y=2348 quiz 桥接行（content12.py:149，旧 145 行）

- 旧：`p.text(RIGHT, qy + 36, "Leia a primeira página e escolha a resposta certa　Respostas na página 8", 20, "sans", False, GREY, anchor="end")`；
  旧实测光栅 1865（+3）、span 1866.9、PIL 1862.5、card 1856。
- **关键发现（实验推翻 proof1 建议修法）**：该行是右锚定（anchor="end"，
  x = 1862 − builder-PIL-advance）。构建器的 PIL advance 比 Cairo/PDF 实际渲染窄约 5px，
  所以渲染墨缘落在 1865。SVG 对照实验（`exp.py`，cairosvg→PDF→MuPDF，与交付管线同法，
  对照 V0 复现 proof1 数值 D1 1886 / D2 1865）：
  - V1 删 `certa`（缩短 51.4px，构建器重锚定）：光栅 1864，仅好 1px——**缩短修不了右锚定行**，
    proof1「缩短约 5px」的建议于此无效；
  - V2 原文、锚点左移 10px：光栅 1855（+7）。
  结论：修法必须是移动锚点。任务「缩短桥接文字或调整行/盒，自定」中取「调整行」。
- 修法：`p.text(NOTE_RIGHT, …)`，`NOTE_RIGHT = RIGHT − 10`（定义见 bslib4.py，§2）；
  **字符串一字未改**（左标题 `БЛИЦ-ВИКТОРИНА　QUIZ RELÂMPAGO` 距新行首约 480px，无碰撞；
  occlusion 审计复核见 GATE-LOG §1）。
- 修后实测（新印 PDF）：**光栅 1855（余量 +7）**；PIL 真墨 1849.5（+12.5）；
  span advance 1857.0（+5.0；尾段 `Respostas na página 8`）；网 PDF 同源。
  证据裁图 `crop-p1-bridge-fix1.png`。
- 注：任务措辞「墨底离盒底」——proof1 四法证据均为横向右缘溢出（+3.1/+5.0/+0.5/+3），
  此行无纵向越盒问题（基线 y=2348，quiz flow 底 2560）；本次按横向右缘修复并复测，
  口径与 proof1 一致。

### R2-D3 minor — P2–P6 页脚说明行，同一行 ×5 页

- 旧：`"Respostas na página 8　Os níveis podem misturar-se; procure pelo número do exercício"`，
  20pt，右锚定，5 处：content12.py:233（P2 y=1876）、content34.py:59（P3 y=1648）、
  content34.py:201（P4 y=1939.3）、content56.py:51（P5 y=1648）、content56.py:174（P6 y=1866）。
  旧实测：五页光栅均为 1864（+2）、span 1866.5、PIL 1862.3。
- **任务所称「共享源头」实际不存在**：grep 证实该串是 3 个文件里的 5 处相同字面量，
  无常量、无共享函数。故修复分两步：(1) 在本版 `bslib4.py` 新建单一源头
  `EX_NOTE`（见 §2），5 处全部改用它——以后一处改动即五页同修；
  (2) 与 D2 同理，缩短修不了右锚定行，5 处锚点一律改用 `NOTE_RIGHT`（RIGHT−10）。
  字符串内容本身未改。
- 修后实测（新印 PDF，逐页光栅）：**P2 1854、P3 1854、P4 1854、P5 1854、P6 1854，
  余量全部 +8**；PIL 真墨 1850.3（+11.7）×5 页一致；span advance 1856.3（+5.7）×5 页，
  印/网 PDF 一致。证据裁图 `crop-p2-note-fix1.png`（P2 代表页；其余四页同串同锚点，
  数值一致）。

## §2 源码改动清单（共 7 处，3 个文件 + 本版 lib）

| 文件 | 行 | 改动 |
|---|---|---|
| `bslib4.py` | 12–25 | 新增 `NOTE_RIGHT = RIGHT − 10`（附 D2/D3 机理注释：builder 欠量约 5px、缩短无效的实验证据）与 `EX_NOTE`（D3 五页共享串，附来源注释） |
| `content12.py` | 109–113 | D1：标题 → `"СЛОВО НЕДЕЛИ　PALAVRA SEMANAL"`（附修法注释） |
| `content12.py` | 149 | D2：`RIGHT` → `NOTE_RIGHT`（字符串不动） |
| `content12.py` | 237 | D3：`RIGHT` + 字面量 → `NOTE_RIGHT` + `EX_NOTE` |
| `content34.py` | 59、201 | D3 同上（P3、P4） |
| `content56.py` | 51、174 | D3 同上（P5、P6） |

未动：`content7.py:88` 的 P7 `"СЛОВО　A PALAVRA DA SEMANA"`（另一字符串，未报缺陷）；
地图 D1（text.md L459/504/596）、kicker、Q25/Q20、首轮 pt1-D7 网斜体、O1
`СМИ　O QUE DIZEM OS MEDIA`（约 +1px 抖动带）、D5（P8 y=1302 行，只记录，见 §4）；
`content7.py`、`content8.py`、`svglib.py`、`run.py`、`render.py`、`ru_textmd.py`、
`WEEKLY-KIT.md`、`ABSTRACT.txt` 全未动（mtime 核对见 GATE-LOG §8）。

## §3 重建（全套正常流程，输出重定向一律绝对路径进本 scratch）

1. `tools/venv/bin/python run.py > <scratch>/run.log`：rc=0，**TOTAL 150**
   （A2 50 / B1 76 / B2 24；按页 10+18+18+18+18+18+12+38；与 proof1 分布一致），
   无 FLOW OVERFLOW、无 HEAD TOO WIDE。
2. `check_core.py .`：rc=0，golden BAD 0，gloss fails 0；1 orphan line-start
   （P7 y553 `”».`）与 1 same-baseline collision（P1 y1712 斜体 `«чёрная пятница»`），
   与 KIT 记载的既往两项一致。
3. `tools/venv/bin/python render.py > <scratch>/render.log`：rc=0，8 张 card + 印 PDF。
4. `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-ru-pt-web.pdf`：rc=0，
   3,383,546 B，58,327 text bytes；字体表含 `LucernaNotoSerif-BoldItalic` 子集
   （D7 机制面已由他人落地，本次只确认存在，未重验 D7 渲染——属校对员职责）。
5. `tools/venv/bin/python ru_textmd.py . 2026-w47-ru-pt.text.md "VOL.4 · Russian text · Portuguese explanations"`：
   rc=0，65,155 B，150 题，277 blocks；**与开工态字节一致**（SHA 不变，见 §5）。

## §4 未修项的现状（只记录，不修）

- D5（P8 y=1302 答案说明行 `Cada resposta com uma breve nota em português　✓ = texto modelo`）：
  新印 PDF 全局扫描唯一越界组：行 1293–1299，最大墨 1863（+1；proof1 为 1864，
  1px 为光栅阈值抖动）。按任务只记录、不修。
- D4：已如 §0.5 所述在开工态即修好；新印 PDF P2 全局扫描零越界（旧 proof1 值为 1868）。
- O1（P1 `СМИ　O QUE DIZEM OS MEDIA`）：未动；新印 PDF 全局扫描 P1 零越界行。

## §5 新三 SHA（交付件）

| 件 | 新 SHA-256 | 大小 | 变化 |
|---|---|---|---|
| 印 `Lucerna-VOL4-ru-pt.pdf` | `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed` | 21,205,591 B | 变（−6 B） |
| 网 `Lucerna-VOL4-ru-pt-web.pdf` | `f21ed9285a7fcca0a3515e2daa2af2518b0e11fb83752280ea448cf80b7864df` | 3,383,546 B | 变（+17 B） |
| 文 `2026-w47-ru-pt.text.md` | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` | 65,155 B | **不变**（字节一致） |

## §6 SVG 变化清单（前后 SHA，`svg-before.sha256` / `svg-after.sha256`）

| 页 | 开工 SHA（前 12） | 重建 SHA（前 12） | 变化 |
|---|---|---|---|
| p1-pervaya.svg | `ea785eec1194…` | `e35cb1452439…` | 变（D1 + D2） |
| p2-zhizn.svg | `79ab42a2cd8d…` | `526d2373e4b3…` | 变（D3） |
| p3-kultura.svg | `eff3677b8464…` | `ae8c30f921a2…` | 变（D3） |
| p4-sport.svg | `a8e3a13d0697…` | `265abc267279…` | 变（D3） |
| p5-molodezh.svg | `4615aa6ec63c…` | `7ea6387283a3…` | 变（D3） |
| p6-razbor.svg | `d6448a6949e5…` | `14e0de301e7d…` | 变（D3） |
| p7-yazyk.svg | `ff92faf74921…` | `ff92faf74921…` | **不变** |
| p8-test.svg | `31442544a588…` | `31442544a588…` | **不变** |

只应变的 P1、P2–P6 变了，其余页字节不变。完整 SHA 见 scratch 内两文件。
另：副本重建复现性——将版目录拷至 `rebuild-copy/ed`（删 svg/cards 后跑 run.py），
8/8 SVG 与线上重建字节一致（`rebuild-copy/run.log`）。

## §7 给协调员的提示

- `WEEKLY-KIT.md` 内记载的旧三 SHA 已过期（印/网已变，text.md 不变），入仓时请随
  `insert.py` 流程刷新；KIT 正文其余数字（题量、门禁）本次复核一致，无需重写。
- proof1 建议的「缩短右锚定行」修法经实验证伪（§1 D2），请勿将其写入 SOP/工具
  作为通用修法；右锚定溢出的根因是构建器 PIL advance 比 Cairo 渲染窄约 5px，
  通用修法应是锚点内收或修正量测，而非删词。
- 本版无新增西里尔串；freeze diff 仅 U+3000（见 GATE-LOG §4）。自主校对未做全量
  通读（任务只修三项 + 门禁复核）；请校对员按 round-2 全量复校受影响页（P1、P2–P6），
  重点为三行新几何与 P1 框标题语义。
