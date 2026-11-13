# W47 ja 核心版 — §1.1 字号阶梯对齐返修记录（Round 6，2026-11-10）

Builder：叶子（返修 builder，与第一轮 builder、第一轮返修 builder、第一/第二轮校对员均不同人）。
对象：`production/2026-w47/core-ja/`（2026-w47-ja-zh-cn，VOL.4，刊期 2026-11-16..22）。
依据：SOP.md §8、§1.1 全文；第二轮校对笔记 `scratch-proof-ja2/PROOF-NOTE.md`（观察 (1) 字号阶梯）。

## 结论：部分对齐 + 一项回退

- **刊头 126pt → 147pt（196px）：对齐完成，零问题。**
- **P1 头条 33pt → 42pt（56px）：对齐完成，零问题。**
- **P8 题干 10.35pt → 15.375pt：回退。** 按回退条款试改后出现硬性版式失败且无法干净解决，已恢复改前 13.8px（10.35pt）。原因见下。
- **边距：已合规，不动。** 左右版心边距实为 66pt（88px），与 SOP 一致。
- 文字内容零改动：`.text.md` 改前改后 sha256 相同（`49d7c1f7…`）；P1 文字元素多重集差分 0；D1–D4 原样保留。

## 三项逐项说明

### 1. 刊头 168px → 196px（147pt）——保留
- 改动：`content12.py:18` `"Lucerna", 168` → `196`，基线 y=262 不变（与 ko 版做法相同：只改字号，不移位置）。
- 验证：印刷版 PDF 实测刊头跨度 147.0pt（PyMuPDF）；SVG 内 `font-size="196"` 唯一 1 处；P1 渲染图目视：刊头与顶行横线（y=112）、副标题行（y=330）均无触碰，三色蛾仍落在橄榄绿线上；P1 头条流 `ended col 2 y=921 (bottom 1828)`，无 FLOW OVERFLOW；遮挡审计 0 flags。
- 回归：§1.1 其余项重测全部通过（见下）。

### 2. P1 头条 44px → 56px（42pt，行高 1.2 → 1.06）——保留
- 改动：`content12.py:34` `44, …, 1388, 1.2` → `56, …, 1388, 1.06`（字号取 ko 版同值 56px；行高取 SOP §1.1 的 1.06；max_w 1388 保留——ja 头条 15 字单行约 840px 宽，无需收窄）。
- 验证：印刷版实测头条跨度 42.0pt，在 SOP 40–45pt 内；渲染图目视单行、无溢出；头条流只下移 6px（915 → 921），余量仍 >900px；其余 7 版 SVG 字节与改前一致。

### 3. P8 题干 13.8px（10.35pt）→ 20.5px（15.375pt）——已回退
- 先量机制：ja 的题干字号机制与 ko/de 相同——`bslib4.ex()` 的 `size` 参数即 SVG px 字号（13.8px = 10.35pt；20.5px = 15.375pt）。`content8.py` 34 处 `size=13.8, gap=0` 全部改为 20.5 后重渲。
- 失败证据（try-1，见 `build-try1.log` / `occlusion-try1.log` / `try1-p8.png`）：
  - 构建：4× `FLOW OVERFLOW [P8-ex]`，练习流 `ended col 3 y=1390 (bottom 1252)`，超底 138px。
  - 遮挡审计：62 flags，全部在 p8（COVER 12、LINEX 7、TEXTX 43）：G 组 ex 145–147 墨迹 100% 被天龙寺图盖住；H 组组头 + ex 149–150 被答案区横线划过；练习文字压住图注与答案键 113–117。
  - 目视：try1-p8.png 上 G 组文字叠在照片上、H 组范文与答案区文字互叠。
- 无法干净解决的原因：P8 练习流改前已用 3567/4288px 栏高，第 3 栏在图片上方仅余 ~179px（流止 y=531，图顶 y=710）；20.5px 题干需约 +850px 栏高（事前预测 4416px，实测溢出 138px）。能腾空间的手段（移图、移答案横线、压其他字号）都是版面手术，超出本次授权的“只改字号”范围，属回退条款所指的“硬修”，故不做。
- 回退：`content8.py` 用改前备份原样恢复（与备份 diff 为空）；重渲后 P8 SVG 与改前字节一致（`9db7294a…`），练习流回到 y=531，遮挡审计回到 0 flags。
- 附注：任务书称“ko 版 P8 题干改 20.5”与磁盘实况不符——ko `content8.py` 至今仍为 `size=13.8`，ko 印刷版实测 P8 题干 10.35pt ×60 跨度；已验证的 20.5 先例是 de 版，且 de 为此把 P8 电池流底边从 1505 扩到 1555（`core-de/content8.py:13` 注释）。ja 的 P8 没有同等可扩空间（答案横线在 1264，答案键流已占到 2351/2540）。

### 附加：边距核查——已合规，不动
- `bslib4.py:8` `MX = 88`，`RIGHT = 1862`；8 版 band 矩形均为 `x=88 width=1774`；印刷版文字 min-x = 66.0pt。左右边距各 66pt（88px），与 SOP §1.1 一致。ko 版的 65px 问题 ja 不存在。

### KIT §11 文字修正
- `WEEKLY-KIT.md` §11 D1：“body `#3a3631`”的表述改为准确表述（正文实际用墨色 `#302c28` 渲染，`#3a3631` 只是 §1.1 表值、构建中未使用，与 core-en 相同）。另同步更新了因本次返修失效的 KIT 数字：§7 P1 头条流终点 915 → 921；§8 两份 PDF 字节数（print 26,018,004 → 26,018,003；web 4,652,750 → 4,652,749；文字层 85,389/44,819 → 85,061/44,818）；§11 补 Round 6 记录。

## 机械门（终版，全部重跑）

- 构建：`run.py` exit 0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150；级别 A2 48 / B1 73 / B2 29；按版 10/18/18/18/18/18/12/38（与定稿一致）。
- `tools/occlusion_audit.py`：自检 OK（6 类全触发，干净对照静默），**0 flags**（`occlusion-final.log`）。
- `tools/p8.py extract --total 150`：noted set **150/150**；与登记表 `ja-core-p8.json` 逐键比对 **0 处不符**（`p8-final.log/.json`）。
- `tools/freeze.py baseline`：**8/8 SVG 字节一致**（直接输出逐页 sha256；`freeze-final.log`）。另直接比对：P2–P8 SVG 与改前逐字节一致，仅 P1 变（字号多重集只差 44→56、168→196 两行；文字元素多重集差分 0）。
- 文字层：print 与 web 两份 `pdftotext -layout` 各 85,061 字节、raw 各 44,818 字节，**逐字节一致**；词级多重集差分 0。
- P8 字号（PyMuPDF，印刷版第 8 页）：最小 **9.975pt**（158 处，答案区），0 处 <9.75pt；次小 10.35pt（79 处，保留的题干）。
- 终版成品：print `Lucerna-VOL4.pdf` 26,018,003 B，sha256 `e1782168d89d06cd080dd7acf62b6dafc69ca7dc5c6c839e698e25c3de2466bd`；web `Lucerna-VOL4-web.pdf` 4,652,749 B，sha256 `7c21329c89efcda759e5aeb91fffd7ac47871b36a6a03a29652f7ccf598c5a1c`；`.text.md` 44,432 B，与改前同哈希。

## §1.1 逐项实测（终版 SVG + 印刷版 PDF）

| 项 | 结果 |
|---|---|
| 纸 `#fbfaf6` | 8 版各 1 处；旧 `#f7f1e2` 0 |
| 禁用色 `#b3a06a/#a4553a/#2c2822/#3e4c2a` | 0 |
| 刊头 147pt / 头条 42pt | 实测 147.0pt / 42.0pt，均在 SOP 范围 |
| 双线外框 | 0；页脚 `第N版／共8版` 8/8，全角／，ASCII `/` 版 0 |
| 刊头蛾 | 三色路径俱在（`#4F765D/#84A283/#4D72B4`），目视落在线上 |
| 徽章 | A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f`（与第二轮结论一致，未动） |
| 字体 | 日文 `Noto Serif CJK JP`、讲解层 `Noto Sans CJK JP`、刊头 `UnifrakturMaguntia`（web 字体列表同） |
| 正文色 | `#3a3631` 0 次（裁定保留：正文用 `#302c28`，与 core-en 相同；只改 KIT 文字） |
| 版心边距 | 左右各 66pt（88px），8 版 band 矩形同证 |
| P8 答案字号 | 最小 9.975pt ≥ 9.75pt 下限 |
| 无首字下沉 | 与 de/fr/it/zh-tw 同一框架，不算缺陷，未加 |

## 150 题逐题复核（独立验算）

- 方法：从源码 AST 按登记顺序抽出全部 150 道题的题干与印出键（`verify-150.txt`），逐题对照题面/原文/图表独立推导，**不采信登记表**；P8 113–150 逐题验算，星期用 `date -d`（Asia/Tokyo）核实：11/5 木、11/19 木、11/22 日、11/23 月。
- 结果：**150/150 键全部正确**，含易错点：ex 79 選ばれ、ex 83 B（宮島 11/21）、ex 85 B（12月12日）、ex 86 A（tenki.jp 11/13）、ex 91 14（38−24）、ex 92 62（38+24）、ex 93 100、配对 25–28（b/d/c/a）、43–46（b/d/a/c）、141–144（c/a/d/b）、造句 133–136 语序、翻译 137–140（E 组统一 JA→ZH）、145 行き、146 買います、147 A（19）、范文 154 字（150–200 内）。
- D1–D4 复核无回归（终版 SVG 联合文本计数）：12月12日 6 处、11月26日 1 处、12月9日干扰项 2 处、大ヒットした漫画 6 处、大ヒット映画 0、150店/750店各 1 处。

## 8 版逐版目视（终版 cards/ + web 抽查）

- P1–P8 逐版看图：无溢出、无重叠、无压页脚；图片与出处齐全；页脚完整。P1 刊头/头条放大后比例协调（见 `try1-p1.png`，与终版 P1 SVG 同哈希）。P8 终版：练习止于 149、图片与图注清晰、答案区 1–150 完整。
- 网页版抽查 P1/P8（`web-p1-1.png` / `web-p8-8.png`）：无豆腐块，版式与印刷版一致。

## 改动清单（相对改前）

- `content12.py`：2 行（刊头 168→196；头条 44→56、行高 1.2→1.06）。
- `WEEKLY-KIT.md`：§11 D1 措辞修正 + §7/§8 数字同步 + §11 Round 6 记录。
- `svg/p1-hyoushi.svg`、`Lucerna-VOL4.pdf`、`Lucerna-VOL4-web.pdf`：重渲产物。
- 未动：`content34/56/7/8.py`、`bslib4.py`、`svglib.py`、`run.py`、`render.py`、`tools/p8.py`、`.text.md`、`ABSTRACT.txt`、`svg/p2–p8`、W43/W45/W46 任何文件；未跑 insert.py / lint --write / git 写操作；未提交。

## 本目录文件

- `SUMMARY.md`（本文件）、`pre-change-manifest.txt`、`post-change-manifest.txt`、`build-try1.log`、`build-final.log`、`render-final.log`、`webpdf-final.log`、`occlusion-try1.log/.json`（62 flags，P8 回退证据）、`occlusion-final.log/.json`（0 flags）、`p8-final.log/.json`（150/150）、`freeze-baseline-pre.log`（改前 8/8）、`freeze-final.log`（终版 8/8）、`freeze-baseline-pre/`、`freeze-final/`、`try1-svg/`、`try1-p1.png`、`try1-p8.png`（P8 失败目视证据）、`web-p1-1.png`、`web-p8-8.png`、`print-layout.txt`、`web-layout.txt`、`print-raw.txt`、`web-raw.txt`、`predict_p8.py`（事前预测：20.5px 需 4416px 栏高 vs 容量 4288px）、`verify-150.txt`（150 题干+键清单）、`stem-key-pairs.txt`（废弃的中间提取）、`p1-fontsizes-pre/post.txt`、`content12.py`、`content8.py`（改前备份）。
