# FIX-LOG — 2026-W47 zh-cn × nl · fix1（proof1 (b) 4 项修复）

- 修复员：fix1；对象 `production/2026-w47/2026-w47-zh-cn-nl/`；核心对照
  `production/2026-w47/core-zh-cn/`（已定稿，未动）。
- 工作区：`hidden_files/w47/scratch-fix-zh-cn-nl1/`（唯一、专用）。
- 只改本版；不 commit、不 push；核心与其他版零触碰。
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功 +
  scratch 内真实写文件成功后开工（`/dev/null` 存在，无需补建）。
  TMPDIR 全程为本 scratch 目录；Python 一律 `tools/venv/bin/python`
  （Pillow 13.0.0 / FreeType 2.14.3）；凡 import 生产源码均设
  `PYTHONDONTWRITEBYTECODE=1`（生产 `__pycache__/` 无写入）。
- 开工三 SHA 与任务书一致（已核对，见下表）。

## 开工三 SHA（2026-11-11 18:45 UTC 核对）

| 文件 | SHA-256 | 大小 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-NL.pdf` | `f660072c047e1b5bab5a13956ec871db6976a47ddff49cc855615a8f55b42e4b` | 44,049,080 B |
| 网 PDF `Lucerna-VOL4-NL-web.pdf` | `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` | 2,703,048 B |
| 文 `2026-w47-zh-cn-nl.text.md` | `41aa9a39371ab7dc75f828b24bb038f0f1b4f6e2f1a1fbe04cd9513eff09df2c` | 50,082 B |

## 锚定方式核对（每项动手前已确认）

- `svglib.py:387`：`BSPage4.text(..., anchor="start")` 为默认锚定。
- b1/b2：`Flow.box()`（`bslib4.py:187`）标题经 `self.p.text(x + pad, ...)`
  绘制，无 anchor 参数 → 左锚定。
- b3：`content12.py:88` `p.text(gx + 22, gy + 664, ...)` 无 anchor 参数 →
  左锚定（:86 是另一处长段落 `p.para`，未动）。
- b4：数字框行经 `p.para` 左对齐折行（`svglib.py:444` 默认
  `anchor="start"`）。缩短/改写荷兰语措辞可移右缘、改断行。
- 故 b1–b3 全部可用“缩短荷兰语措辞”修复；未用降字号。

## 缺陷逐项：改前实测（自己重测，非转述 proof1）→ 改法 → 改后实测

裁决标准：交付 PDF 渲染像素墨右 ≤ 盒右缘且余量 ≥ +5px；PIL 真墨 +
PDF 文字层 advance 为交叉核对。occlusion 对此 4 项是空信号（纯填色
奶油盒横向越框盲区），绝不以 occlusion 0 flags 为修好证据。

### b1（重）P5 高频词盒标题越盒右缘 27.25px

- 位置：P5 中栏奶油盒 rect x=538.5..961.0, y=648..816；标题
  `这一周的高频词　Woorden van de week`（`content56.py:25`）。
- 改前（自测，与 proof1 一致）：
  - PIL 真墨：墨右缘 x=988.25，越盒边 **27.25px**；advance 测得末端
    988.16，余量 −27.16px。
  - 交付 PDF 文字层：`Woorden van de week` span 右缘 741.88pt，盒边
    720.75pt，越 **21.13pt**。
  - 交付 PDF 100dpi 渲染像素：最右墨点 740.16pt，越 **19.41pt**；
    `week` 的 `k` 全在白纸上（裁图 `render/b1-title-zoom.png` 改前见
    proof1 同名裁图；改后裁图见下）。
- 改法：荷兰语 `Woorden van de week` → `Woorden`。中文 `这一周` 已含
  “this week”，事实与核心 D4/D5 无关，未动；字号 23pt 未动。备选
  `Woorden deze week` 仍越 5.56px、`Woord van de week` 仅余 +0.95px，
  均不达 ≥+5px 标准，故弃用。
- 改后（生产文件上复测）：
  - PIL 真墨：标题余量 **+118.0px**（盒内最紧行 +64.5px）。
  - PDF 文字层：span 右缘 632.47pt，余量 **+88.28pt**。
  - PDF 100dpi 渲染像素：最右墨点 630.72pt，余量 **+90.03pt**
    （+125.0px @100dpi）。裁图 `render/b1-title-zoom.png` 目视：标题
    在盒内结束，右缘大段留白。

### b2（轻）P2 日历标题越盒右缘 1.75px

- 位置：P2 中右栏奶油盒 rect x=989.0..1411.5, y=200..447；标题
  `本周生活小日历　Data van deze week`（`content12.py:187`）。
- 改前（自测）：
  - PIL 真墨：墨右缘 x=1413.25，越盒边 **1.75px**；advance 末端
    1413.17，余量 −1.67px。
  - 交付 PDF 文字层：span 右缘 1061.47pt，盒边 1058.625pt，越 2.85pt。
  - 交付 PDF 100dpi 渲染像素：最右墨点 1059.84pt，越 **1.22pt**
    （窗口限盒边 +10pt 以内，避开 x=1079.6pt 起的 col-3 照片污染；
    不限窗口的首次扫描误报 −78.98pt，即照片墨，已在日志中说明）。
- #3 KIT “已修”不成立：其 “ends x = 1413.2, 26.3px clear” 的 1413.2
  与实测墨右缘一致，但 26.3px 是到照片（x=1439.5）的距离，盒边为
  1411.5。本次修复以盒右缘 1411.5 为准。
- 改法：`Data van deze week` → `Data deze week`（去 `van `，含义不变）。
- 改后（生产文件上复测）：
  - PIL 真墨：标题余量 **+44.5px**（盒内最紧行 +31.6px）。
  - PDF 文字层：span 右缘 1026.37pt，余量 **+32.26pt**。
  - PDF 100dpi 渲染像素：最右墨点 1025.28pt，余量 **+33.35pt**
    （+46.3px @100dpi）。裁图 `render/b2-title-zoom.png` 目视：标题在
    盒内结束，与右侧照片有明显间隔。

### b3（轻）P1 截稿线越日历盒边约 1–2pt

- 位置：P1 右栏日历奶油盒 rect x=1439.5..1862.0, y=588..1288 内末行
  `Sluiting: 10 nov. — de finale nog niet gespeeld`
  （`content12.py:88`；:86 长段落未动）。
- 改前（自测）：
  - PIL 真墨：墨右缘 x=1864.5，越盒边 **2.5px**；advance 末端
    1864.45，余量 −2.45px。
  - 交付 PDF 文字层：行最右 1399.31pt，盒边 1396.5pt，越 2.81pt。
  - 交付 PDF 300dpi 渲染像素：最右墨点 1397.76pt，越 **1.26pt**
    （proof1 300dpi 复测为 1.02pt，阈值差异所致，方向一致）；
    `gespeeld` 的 `d` 被盒边切过。
- 改法：删定冠词 `de ` → `Sluiting: 10 nov. — finale nog niet
  gespeeld`。事实不变（仍是“决赛尚未打”）；长段落 :86 未动。
- 改后（生产文件上复测）：
  - PIL 真墨：该行余量 **+24.0px**（盒内最紧行即该行）。
  - PDF 文字层：行最右 1379.39pt，余量 **+17.11pt**。
  - PDF 300dpi 渲染像素：最右墨点 1377.84pt，余量 **+18.66pt**
    （+77.8px @300dpi）。裁图 `render/b3-sluiting-zoom.png` 目视：
    `gespeeld` 的 `d` 完整，行尾距盒边有明显留白。

### b4（中）P1 数字框 `《试探》` 收尾 `》` 孤儿行首

- 位置：P1 中栏数字框第 3 行
  `21 nov., zaterdag — de nieuwe film 《试探》 gaat in première`
  （`content12.py:50`）；框内宽 386.5px，20pt serif 折行。
- 改前（自测）：交付 PDF 文字层全 8 版逐行扫描唯一一起行首 `》`：
  `》gaat in première`，bbox x=417.4–549.5pt, y=1007.4–1029.0pt；
  100dpi 渲染目视确认；核心 0 起。`.text.md` 该行为完整单行，缺陷
  纯属渲染折行。
- 改法：同词改写、调断行，不删事实词：
  `21 nov., zaterdag — première van de nieuwe film 《试探》`。
  `wrap()` 实测折为两行：`21 nov., zaterdag — première van de` /
  `nieuwe film 《试探》`——`》` 落在第 2 行行尾，无孤儿；仍为 2 行，
  盒高不变；“nieuwe / film / première / 21 nov. / zaterdag” 全部保留。
  备选 `de film`（删 `nieuwe`）亦无孤儿，但丢词，故弃用。
- 改后（生产文件上复测）：
  - 交付 PDF 文字层全 8 版逐行扫描：行首闭合标点 **NONE**（`》/」/）/”/、/。/，`
    均无行首）。
  - P1 该两行实测：`21 nov., zaterdag — première van de`
    （x=417.4–667.0pt, y=993.4–1008.4pt）/
    `nieuwe film《试探》`（x=417.4–561.5pt, y=1007.4–1029.0pt）。
    裁图 `render/b4-box-zoom.png` 目视：`》` 在行尾、盒内。
  - 旧串在 PDF 全文（去空白）中已无，新串已在。

## 重建（scratch 副本内）

- work 副本：整版复制至 `scratch-fix-zh-cn-nl1/work`，5 个 content 文件
  OUT 用 sed 改向至 work/svg（改向前 grep 核实 5 处；`render.py`
  未执行，生产 SVG 无写入）。4 处修复先改在 work 副本，确认后再同步。
- `run.py` rc=0，TOTAL 150（A2 56 / B1 69 / B2 25；分版
  10/18/18/18/18/18/12/38）；0 HEAD TOO WIDE；0 FLOW OVERFLOW；
  P7 teaser ends 2586.3；P8 keys flow ends 2491.1（与 #3 相同）。
- SVG 变化页：仅 p1-touiban、p2-shenghuo、p5-qingnian 变化；
  p3/p4/p6/p7/p8 与交付版 sha256 一致。
- 卡片变化页：仅 p1/p2/p5 变化；其余 5 张一致。
- 印 PDF 由 work SVG 重建（`render_work.py`，复刻生产 `render.py`
  的 cairosvg svg2pdf + pypdf 流程，BASE 指 work 目录）。

## 同步进生产（2026-11-11）

同步前存生产快照 `opening-snapshot.sha256`（46 文件）。同步文件
（10 个）：`content12.py`、`content56.py`、`svg/p1-touiban.svg`、
`svg/p2-shenghuo.svg`、`svg/p5-qingnian.svg`、`cards/p1-touiban.png`、
`cards/p2-shenghuo.png`、`cards/p5-qingnian.png`、`Lucerna-VOL4-NL.pdf`、
`2026-w47-zh-cn-nl.text.md`。同步后逐项比对开工快照：**仅这 10 个
文件变化**，其余 36 个（含 web PDF、ABSTRACT.txt、其余源码/SVG/卡片）
与开工一致。
**网 PDF 按要求不覆盖**：`Lucerna-VOL4-NL-web.pdf` 仍为 #3 版
（SHA `495594dc…eefac`，2,703,048 B），由入仓前全家统一重建时更新；
它仍含 4 处改前荷兰语串，印 PDF 为本次已验证交付物。
KIT 同步更新：新 SHA + fix1 章节记入 `WEEKLY-KIT.md`（旧 SHA 保留）；
#3 KIT 的 b2“已修”不成立与 b1 漏检两处错误表述一并改写（另见 KIT
Adjudications / Build history #4 / Gates fix1 / Artifacts）。
同步前 work 副本的 OUT 已还原为生产路径，再核对 work 与生产源码
diff 仅剩 4 处修复行后才复制，杜绝 OUT 重定向串入生产。

## 新三 SHA + 字节数（生产文件，同步后复测）

| 文件 | SHA-256 | 大小 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-NL.pdf`（新） | `3a160cae374c2e713daac7de9f7a0bfba0f77513db31894673c0d40f8344c628` | 44,048,879 B |
| 网 PDF `Lucerna-VOL4-NL-web.pdf`（未动，#3 版） | `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` | 2,703,048 B |
| 文 `2026-w47-zh-cn-nl.text.md`（新） | `9bc8212fa100631226c03c4debbf31bba96557d1c0cad002076cba0c1d0732b8` | 50,059 B |

`.text.md` 恰 4 行改动（53 / 127 / 271 / 915 行各一处）；P7
`Woorden van de week: ...`（1315 行）是另一处独立段落，未动。

## 门禁逐项（GATE-LOG.md 详见）

- run.py：rc=0，TOTAL 150，分级/分版与 #3 一致，0 溢出。
- PIL 真墨横扫（全 8 版 40 奶油盒）：0 负余量；最紧 +13.5px（P4
  旧盒，未动）。3 处修复盒：+118.0 / +44.5 / +24.0px。
- 渲染像素（交付印 PDF）：b1 +90.03pt @100dpi、b2 +33.35pt @100dpi、
  b3 +18.66pt @300dpi；均 ≥ +5px 标准。
- 文字层 advance：b1 +88.28pt、b2 +32.26pt、b3 +17.11pt。
- 孤儿行首扫描（全 8 版）：NONE。
- p8 extract 150/150；compare vs 核心 CLEAN，keydiff []。
- freeze diff --strict-cjk：TOTAL added CJK 0。
- occlusion：自检 OK；本版 0 flags（空信号说明见 GATE-LOG——
  不作为修好证据）。
- D4/D5 抽查：全球总决赛限定、S16 措辞、淘汰赛一局没输均在；
  150 题键未动（无 key 串被编辑）。
- 生产快照比对：同步后仅预期 10 文件 + KIT 变化。

## 待后续（非本 fix 范围）

- 网 PDF 待入仓前全家统一重建（含本次 4 处荷兰语改动）。
- 按 SOP §8，本版修后须从头再做一轮全量独立校对，零问题方能定稿
  （本 fix 只修 proof1 (b) 的 4 项，不代校对结论）。
