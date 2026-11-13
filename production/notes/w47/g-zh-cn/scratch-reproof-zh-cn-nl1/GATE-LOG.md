# GATE-LOG — 2026-W47 zh-cn × nl · reproof 机械门自跑汇总

- 校对：reproof；对象 `production/2026-w47/2026-w47-zh-cn-nl/`；
  核心对照 `production/2026-w47/core-zh-cn/`；全部命令用
  `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）跑出，非转述。
- 工作区：`hidden_files/w47/scratch-reproof-zh-cn-nl1/`。开工探针：
  `git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功 + scratch
  写文件成功。TMPDIR 全程为本 scratch；凡 import 生产源码均设
  `PYTHONDONTWRITEBYTECODE=1`（生产 `__pycache__` 无写入，收工快照 46/46 OK）。

## 0. 三 SHA 先验（开工 / 收工一致）—— PASS

| 文件 | SHA-256 | 大小 |
|---|---|---|
| `Lucerna-VOL4-NL.pdf` | 3a160cae374c2e713daac7de9f7a0bfba0f77513db31894673c0d40f8344c628 | 44,048,879 |
| `Lucerna-VOL4-NL-web.pdf` | 495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac | 2,703,048 |
| `2026-w47-zh-cn-nl.text.md` | 9bc8212fa100631226c03c4debbf31bba96557d1c0cad002076cba0c1d0732b8 | 50,059 |

与任务书开工值一致；与 KIT Artifacts 一致。网 PDF 为 #3 版（未动）。

## 1. run.py scratch 重建 —— PASS

- 整版复制至 `scratch-reproof-zh-cn-nl1/rebuild/`，5 个 content 文件 OUT
  用 sed 改向至 `…/rebuild/svg`（改向前 grep 核实 5 处 OUT 均已改向，
  改向后 `weekly-git` 残留 0 处；`render.py` 未执行，生产 SVG 无写入）。
- `run.py` rc=0；TOTAL 150（A2 56 / B1 69 / B2 25；
  分版 10/18/18/18/18/18/12/38；类型 完成句子 68 / 单选 50 /
  词汇配对 20 / 完形单选 11 / 写作 1）；0 FLOW OVERFLOW；0 HEAD TOO WIDE；
  P7 teaser ends 2586.3；P8 keys flow ends 2491.1（`run-rebuild.log`）。

## 2. SVG 重建 8/8 字节一致 —— PASS

重建 SVG sha256 与交付版逐一比对：p1–p8 全 MATCH。

## 3. 印 PDF 重渲 SHA 逐字节相同 —— PASS（经一次瞬态异常后干净重跑复现）

- `render_work.py`（复刻生产 `render.py` 的 cairosvg svg2pdf + pypdf
  流程，BASE 指 scratch）：8/8 卡片与生产卡片 sha256 一致。
- 干净重跑（`rebuild2/`，`render2.log`）：印 PDF 44,048,879 B，
  SHA `3a160cae374c2e713daac7de9f7a0bfba0f77513db31894673c0d40f8344c628`
  —— 与交付印 PDF 逐字节相同。
- **瞬态异常记录（首跑）**：首跑期间服务重启杀掉一次前台渲染（SIGTERM，
  260 s），随后一次前台调用派发超时、又与后台重跑短暂重叠；该跑产物
  290,435,383 B、67,372 对象、24,921 个 BaseFont 条目（Cairo 逐元素字体
  子集化，1,072 个 distinct 子集前缀；对照：交付 272 对象、85 条目、
  48 distinct），SHA `45f8da0a…` 不符。但该文件与交付印 PDF 的文字层
  8 页全 0 差（msdiff=0、posdiff=0、bbox 最大差 0.00 pt），P1/P5
  100 dpi 渲染像素 100.00% 一致（max|d|=0）——内容等价已证。
  单页对照（核心 p1，现跑）：56 对象、11 BaseFont，行为正常。
  fix1 19:03 的同脚本同 SVG 复现亦为 44,048,879 B / 同 SHA。
  结论：异常为渲染环境瞬态（重启窗口期的并发孪生进程），干净重跑
  未再现，不属版面缺陷。该 290 MB 文件已删除（SHA 与对象数记于此）。

## 4. freeze baseline（核心）—— PASS

`tools/freeze.py baseline --build production/2026-w47/core-zh-cn
--core-svg production/2026-w47/core-zh-cn/svg --out …/freeze-baseline`
rc=0；8/8 SVG 字节一致；核心完整性：交付核心 SVG 跑前后重哈希无变。

## 5. freeze baseline（本版自身）—— PASS

`tools/freeze.py baseline --build production/2026-w47/2026-w47-zh-cn-nl
--core-svg production/2026-w47/2026-w47-zh-cn-nl/svg
--out …/freeze-baseline-edition` rc=0；8/8 SVG 字节一致
（p1 5fc467e0…、p2 81627f29…、p3 74bf6a17…、p4 4a375b03…、
p5 7db5e916…、p6 9563ddac…、p7 17275063…、p8 66793785…）；
本版 SVG 跑前后重哈希无变。

## 6. freeze diff --strict-cjk —— PASS

`tools/freeze.py diff --core-svg …/core-zh-cn/svg --edition-svg …/zh-cn-nl/svg
--strict-cjk --json …/freeze-diff.json` rc=0；
p1 +48/−46、p2 +52/−52、p3 +38/−38、p4 +42/−43、p5 +36/−37、p6 +43/−41、
p7 +101/−97、p8 +199/−202；**TOTAL added CJK characters: 0**。
与 proof1 的 #3 版 freeze-diff 逐串比对，差异恰为 4 处 fix1 改动
（P1：`21 nov., zaterdag — première van de` / `nieuwe film ` /
`Sluiting: 10 nov. — finale nog niet gespeeld` 新串，旧串
`21 nov., zaterdag — de nieuwe film ` / `gaat in première` /
`《试探` / `》` / `Sluiting: 10 nov. — de finale nog niet gespeeld` /
空格串 消失，另 `《试探》` 从 removed 侧消失；
P2：`本周生活小日历　Data deze week` 换 `Data van deze week`；
P5：`这一周的高频词　Woorden` 换 `Woorden van de week`），无其他串变化；
150 题键未动。

## 7. occlusion_audit —— PASS（附空信号说明）

- 自检：planted classes 全触发 {'BOXTITLE':1,'COVER':1,'EDGE':1,'FOOTER':1,
  'LINEX':1,'TEXTX':1}，clean controls silent，rc=0。
- 本版：0 flags；核心：0 flags；NEW vs core：0。
- **空信号说明**：occlusion 只报墨与后画边框/遮盖的相交；纯填充奶油盒无边框，
  标题墨越盒边时不报。本轮全部越边结论由第 8/9 项真墨横扫 + 渲染像素
  得出，occlusion 0 flags 从不作为修好证据。

## 8. 奶油盒真墨横扫（PIL 真墨，`measure.py`）—— PASS

全 8 版 **35 个**奶油盒（盘上实数，逐页 5/10/5/3/4/5/3/0；核心同数；
proof1/KIT 的“40”系多计）：0 负余量。最紧 8 项：

| 余量 | 页 | 盒 |
|---|---|---|
| +13.50 px | P4 | x=1439.5..1862.0, y=915.4..1171.4（`看比赛的中文　Wedstrijdwoorden`，未动旧盒） |
| +20.25 px | P2 | x=538.5..961.0, y=1286.1..1431.8 |
| +21.00 px | P1 | x=538.5..961.0, y=1110.3..1463.3（数字框；最紧行是第 1 行正文，标题 +45.25 px） |
| +21.00 px | P3 | x=88.0..510.5, y=1265.2..1470.3 |
| +21.80 px | P7 | x=1439.5..1862.0, y=1250.5..1646.5 |
| +21.90 px | P1 | x=1439.5..1862.0, y=1312.0..1652.0 |
| +22.30 px | P1 | x=1439.5..1862.0, y=1874.0..2290.0 |
| +22.50 px | P5 | x=538.5..961.0, y=200.0..405.1 |

修复盒：P5 标题 +118.0 px（盒最紧 +64.5 px）；P2 标题 +44.5 px
（盒最紧 +31.6 px，`BLG` 行）；P1 日历盒最紧 +24.0 px，即 b3 行本身。

## 9. 盒标题横向真墨扫 + 纵向跨底边扫 + spill 扫 + P1 绿带（`sweep2.py`）—— PASS

- 盒标题：35 盒标题 0 负；最紧 +13.50 px（P4 `Wedstrijdwoorden`），
  其次 +28.00 px（P3 gloss 盒）、+28.25 px（P6 gloss 盒）。
- 纵向：奶油盒底边被跨 0 起。
- spill：墨出页界 0 起（页 1950×2700）。
- P1 绿带（x=88..1862, y=470..588）：11 行字，最紧 +29.95 px
  （`S16决赛×包裹`），其次 +30.15 px。

## 10. fix1 四项双法重测 —— PASS（详见 PROOF-NOTE）

| 项 | 源码行 | PIL 真墨 | 文字层 advance | 渲染像素 | 门限 |
|---|---|---|---|---|---|
| b1 | content56.py:25 | +118.0 px | +88.28 pt | +90.03 pt @100dpi | ✓ |
| b2 | content12.py:187 | +44.5 px | +32.26 pt | +33.35 pt @100dpi | ✓ |
| b3 | content12.py:88 | +24.0 px | +17.11 pt | +18.66 pt @300dpi | ✓ |
| b4 | content12.py:50 | 孤儿 NONE（全 8 版） | 行 1 x=417.4–667.0，行 2 x=417.4–561.5，`》` 行 2 行尾 | 裁图目视 ✓ | ✓ |

渲染像素簇分析：b1 盒边外簇起于 1097 pt（第 3 栏正文），b2 起于
1079.28 pt（第 3 栏照片），均与标题有间隔，非溢出；b3 盒边外无墨。
裁图：`render/b1-title-zoom.png` / `b2-title-zoom.png` /
`render/b3-sluiting-zoom.png`（`d` 完整）/ `render/b4-box-zoom.png`
（`》` 行尾）。锚定核实：`svglib.py:387` 默认 `anchor="start"`；
三处标题/行均无 anchor 参数，左锚定未变。

## 11. 行首孤儿引号扫描（交付 PDF 文字层逐行）—— PASS

- 印 PDF（全 8 版）：NONE；核心印 PDF：NONE；**0 新增**。
- 网 PDF（#3 版）：仅 1 起 P1 `》gaat in première`
  （x=417.4–549.5 pt, y=1007.4–1029.0 pt）——即 fix1 前的 b4 旧串，
  与网 PDF 未重建的已知状态一致，非新缺陷。

## 12. p8.py extract / compare —— PASS

- extract：noted set = 150/150（`p8extract.json`）。
- compare 核心 vs 本版：`CLEAN missing=[] extra_count=0 uncertain=[]
  keydiff=[]`，rc=0（`p8compare.json`）。

## 13. 150 题 keycheck + 三方手验 —— PASS（1 处预期差异）

- `keycheck_run.py`（proof1 脚本改绝对路径；`expl.E =
  {'gloss_prefix': 'Notities｜', 'note_wrap': 'half'}`，前缀取自本版
  `bslib4.py` `gloss()` 内嵌值，P1/P2/P4 SVG 实测亦为 `Notities｜`）：
  REG=150，stems=150；REG key 与 p8extract key 仅 1 处不符：
  Q150 REG `(开放题，范文如下)` vs 印出 `✓`（开放写作题截断式印法，预期内；
  范文实测 138 字，在 120–180 内；星期与日期自洽：周日决赛 15 日、
  周一包裹 16 日、周六电影 21 日、周日小雪 22 日）。
- 三方：150 题干在 `.text.md` 中 0 缺失；`.text.md` 末 150 行答案键与
  p8extract 键 0 差异（Q150 两处同为 `✓`）；5 组配对题逐组核对无误
  （P2 a/b/c/d、P3 b/d/a/c、P4 d/b/c/a、P5 c/b/d/a、P6 c/d/a/b）；
  150 行题干 + 键已逐行读过（`keycheck-150.txt` 全 300 行），键与题干、
  键注、正文事实一致。Q56 = T1（题干「第一次在全球总决赛的BO5里」）。

## 14. 印/网文字层 8 页比对 —— 预期 FAIL（仅改动页）/ 其余 PASS

`textlayer.py`（fitz 词级比对，0.6 pt 容差）：

| 页 | print 词 | web 词 | msdiff | posdiff | 结论 |
|---|---|---|---|---|---|
| P1 | 391 | 393 | 6 | —（词数不同） | 预期：b3 删 `de` 1 + b4 重排 5 |
| P2 | 379 | 380 | 1 | — | 预期：b2 删 `van` 1 |
| P3 | 290 | 290 | 0 | 0 | PASS |
| P4 | 354 | 354 | 0 | 0 | PASS |
| P5 | 291 | 294 | 3 | — | 预期：b1 删 `van/de/week` 3 |
| P6 | 356 | 356 | 0 | 0 | PASS |
| P7 | 526 | 526 | 0 | 0 | PASS |
| P8 | 1803 | 1803 | 0 | 0 | PASS |

网 PDF 仍为 #3 版（含 4 处改前荷兰语串），印 ≠ 网文字层为已知待全家
统一重建状态，记为预期项，不作缺陷。P1 ms 明细
`van/film《试探》/de/in/film《试探/》gaat` 各 1，与 b3+b4 逐项对应。

## 15. P8 最小字号 / 芯片 —— PASS

- PyMuPDF 逐页最小字号（印/网一致）：P1 10.50、P2–P5/P7 11.62、
  P6 12.75、**P8 9.98 pt**（≥ SOP §1.1 底线 9.75 pt）。
- P8 芯片：A2 11 / B1 24 / B2 3 = 核心。

## 16. §1.1 视觉规范 —— PASS

- 纸色 `#fbfaf6` ×8；描边 rect 0；VOL.4 全 8 版在位（P1 2 处、其余各 1 处；
  P7 VOL.4 2→1 为 KIT 已载明的 letters-box 删 "in VOL.4" 修复；
  VOL.5 各 1 处为下期预告，核心同）。
- 调色板：P2–P8 无表外色；P1 的 9 个表外色（`#34483a #4d72b4 #4f765d
  #7898cd #84a283 #cac8ba #d7b257 #edd17f #f1e8d4`，插画色）与核心 P1
  色集逐项相同（版−核心色集差 0），为核心继承插画色，非本版新增、
  非家具禁用色。
- U+2019：SVG 合计 0，`.text.md` 0。
- 8 条本周金句：各恰 2 次（正文 + P7），与核心一致。
- "next Sunday"：本版与核心的 SVG、`.text.md`、源码中均无此串，规则空适用。

## 17. 日期 / 事实 / D4-D5 —— PASS

- `date -d`：11月1日周日、4日周三、5日周四、6日周五、7日周六、8日周日、
  9日周一、14日周六、15日周日、16日周一、21日周六、22日周日，与文中全部一致。
- D4：P4 正文「这是中国队第一次在全球总决赛的BO5里打赢T1」、
  Q56 题干、键注 56 全部在位（空白归一化检索；逐行直查的一次 MISSING
  为提取换行断裂假象，已纠正）；D5：P1 `content12.py:42` 与 P4
  `content34.py:131` 均为 S16 限定表述「GEN在S16一场没输，只丢了一小局」，
  全文无「GEN今年一场没输」；「淘汰赛一局没输」在位。
- 目视：8 页 100 dpi 全页渲染逐页目视（`render/p*-small.png`），
  无溢出、重叠、压页脚；P7 teaser 末端 2586.3 距页脚有空隙。

## 18. 生产零写入核对 —— PASS

收工 `sha256sum -c opening-snapshot.sha256`：46/46 OK，0 差异；
三 SHA 与开工值相同；核心 SVG 开工/收工重哈希无变。

## 总 verdict

17 门：freeze / 重建 / 重渲 SHA / p8 / keycheck / occlusion / 真墨横扫 /
盒标题双扫 / 孤儿 / 字号 / 文字层（除预期 3 页）/ §1.1 / 日期事实全过；
**fix1 四项全部独立重测通过；全版无新缺陷** → 结论 (a)，见 PROOF-NOTE.md。
