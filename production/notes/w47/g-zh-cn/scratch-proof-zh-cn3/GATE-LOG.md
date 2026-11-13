# GATE-LOG — W47 zh-cn 核心版 run16 第三轮复校机械门

校对员：叶子（第三轮）。全部机械门由本轮独立自跑，输出存于本目录。
构建解释器确认：`tools/venv/bin/python`，Pillow 13.0.0，PyMuPDF 2.1
（系统 python3 为 Pillow 10.2.0，未用于任何一门）。

## 1. 成品身份（sha256sum，2026-11-11）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4.pdf`（印刷） | 41,763,115 | `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` |
| `Lucerna-VOL4-web.pdf`（网页） | 2,632,446 | `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9` |
| `2026-w47-zh-cn-en.text.md` | 49,435 | `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` |

三者与任务书 run16 终版全串一致。印刷 PDF 8 页，网页 PDF 8 页。

## 2. 几何遮挡审计（tools/occlusion_audit.py，tools venv）

- 自检：`occl-st3.log` — RC 0，`selftest OK: planted classes fired
  {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1};
  clean controls silent`。
- 终版 SVG：`occl3.log` — RC 0，`0 flags`。

## 3. P8 印刷注释门（tools/p8.py，tools venv）

- `extract --p8 svg/p8-ceyan.svg --total 150`：`p8-3.log` — RC 0，
  `noted set = 150 of 150 (parse: lines)`。
- `compare --core-p8 svg/p8-ceyan.svg --edition-p8 svg/p8-ceyan.svg --total 150`：
  `p8-compare3.log` — RC 0，`status: CLEAN missing=[] extra_count=0
  uncertain=[] keydiff=[]`（核心自比；本核心无 fan-out 版可比）。

## 4. 冻结复现（tools/freeze.py baseline，tools venv）

- `freeze3.log` — RC 0，`baseline: 8/8 SVGs byte-identical`；
  8 个 SVG sha256 逐一 OK；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
- 构建副本在 `freeze3/` 内重跑，未动真实核心文件。

## 5. 文字层双版一致（pdftotext -layout + PyMuPDF）

- print/web 非空字符多重集完全一致：各 22,523；print-only 0、web-only 0。
- SVG `<text>` 拼接（ElementTree 精确计数）：22,523（去空格）/ 25,971（含空格），
  与 KIT 一致。（check3.py 初版正则提取误计 22,732，系方法误差，已纠正；
  见 check3.log 注。）
- 原始 `-layout` 字节顺序有别（ReportLab 重排版已知 artifact），非内容差异。

## 6. P8 字号（PyMuPDF，印刷 PDF）

- 键区最小字号 9.98pt（键区 span 尺寸 {9.98, 12.75}，12.75pt 为页脚/页眉），
  ≥ SOP 9.75pt 底线。✓
- 题干区 span 尺寸 {11.62, 13.12, 13.88, 14.25, 14.62, 15.38, 18.0}；
  13.12pt（17.5px）为已裁定项（阶梯 1–4 步已穷尽），本轮重测无变。

## 7. run15→run16 差异门（check3.py）

- 印刷版全文行级 diff：非等价块仅 P1 lead 段、P4 特稿段、Q56 题干、
  P8 键 56 注；P2/P3/P5/P6/P7/P8 试题区零差异。
- P8 键区比对：仅 #56 一条不同（注文“for the first time in a BO5.”→
  “for the first time in a Worlds BO5.”，键 T1 不变）。
- `.text.md` 键区：150 键 1–150 连续、无重复；与印刷版 P8 键逐条比对，
  空格归一化后一致。说明：PyMuPDF 行分组在键 38/76/113 三处
  （各栏首行，y=1036.5pt，略低于筛选阈值 1038pt）及键 37/150 两处
  （相邻行归并）出现 5 处归并假象，目视 P8 图确认三键均在位、
  内容与 `.text.md` 一致；p8.py extract 150/150 为决定性证据。

## 8. 其他独立扫描（check3.py / check3.log）

- D4/D5 字符串计数：旧表述 0；新表述“GEN在S16一场没输”2、
  “只丢了一小局”2、“全球总决赛的BO5”2、“对LYON 2比1”1、
  键注“Worlds BO5”1；“一局没输”全刊仅 1 处（事实框，属实）。
- 金句 8 条：各恰好 2 次。禁词（战争/地缘/外交/政治/选举/民调/台湾/台独/
  香港）：全 0。繁体独用字：0。“·”138（正文内）。“waitfor”0。
  “2003 年”0。“7.6亿件”“1.4亿件”“四分之三”0。“三分之二”1。
  “139.38”24、“7.77”20。VOL.4=10、VOL.3=2（有意）。
- 徽章 rect 计数：芯片 135（A2 50 / B1 63 / B2 22），按题折算
  A2 56 / B1 69 / B2 25，分版 10/18/18/18/18/18/12/38，与 KIT 一致。
- 数字断裂：0 条真实候选（135 条候选全为徽章+题号分行）。
  行首闭合标点：0 条。逐 `<text>` 元素合并拉丁词：未知 token 0 个。
- 超右版心 span：8 个，与 run15 同集合（已裁定保留）。
- 范文字符：138（去空格），与刊内标注一致。
- 日期星期：`date -d`（Asia/Shanghai）复核 15 个日期，全部与刊内断言一致。

## 9. 目视门

- 印刷 P1–P8 从 PDF 全新渲染（`pdftoppm -r 110`，`view/p-*.png`），
  网页 P1/P8 全新渲染（`view/web-p1-1.png`、`view/web-p8-8.png`），
  逐版读过：无溢出、无重叠、无压页脚。P1 徽章与蛾标无遮挡；
  D4/D5 改句在 P1、P4、P8 目视在位。
