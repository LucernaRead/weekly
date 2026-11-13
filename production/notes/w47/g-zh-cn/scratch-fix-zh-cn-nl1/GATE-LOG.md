# GATE-LOG — 2026-W47 zh-cn × nl · fix1 机械门自跑汇总

- 修复员：fix1；对象 `production/2026-w47/2026-w47-zh-cn-nl/`；核心对照
  `production/2026-w47/core-zh-cn/`；全部命令用 `tools/venv/bin/python`
  （Pillow 13.0.0 / FreeType 2.14.3）跑出，非转述他人结果。
- 工作区：`hidden_files/w47/scratch-fix-zh-cn-nl1/`。开工探针：
  `git hash-object -w /dev/null` 成功 + scratch 写文件成功。
  TMPDIR 全程为本 scratch；`PYTHONDONTWRITEBYTECODE=1` 全程设置。
- 结论：**4 项缺陷全部修复，门禁逐项通过**（但按 SOP §8 仍须一轮
  全量独立校对，本 log 不是定稿结论）。

## 0. 三 SHA 先验与新三 SHA

开工（与任务书一致）：
- 印 `f660072c047e1b5bab5a13956ec871db6976a47ddff49cc855615a8f55b42e4b` / 44,049,080 B
- 网 `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` / 2,703,048 B
- 文 `41aa9a39371ab7dc75f828b24bb038f0f1b4f6e2f1a1fbe04cd9513eff09df2c` / 50,082 B

修复后（生产文件，同步后复测）：
- 印 `3a160cae374c2e713daac7de9f7a0bfba0f77513db31894673c0d40f8344c628` / 44,048,879 B
- 网 `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` / 2,703,048 B（未动）
- 文 `9bc8212fa100631226c03c4debbf31bba96557d1c0cad002076cba0c1d0732b8` / 50,059 B

## 1. 改前重测（生产原文件，自测）—— 4 项全部复现

PIL 真墨横扫（`measure.py`，复用 `tools/occlusion_audit.py` 的
`parse_svg` 真墨盒；全 8 版 40 奶油盒）：
- P5 盒标题 −27.25px；P1 日历盒末行 −2.50px；P2 日历盒标题 −1.75px；
  其余最紧 +13.5px。
交付 PDF 文字层：b1 −21.13pt；b2 −2.85pt；b3 −2.81pt。
交付 PDF 渲染像素：b1 −19.41pt @100dpi；b2 −1.22pt @100dpi；
b3 −1.26pt @300dpi（proof1 为 −1.02pt，阈值差异，方向一致）。
孤儿扫描（全 8 版）：P1 `》gaat in première` 唯一一起。
（注：b2 渲染首次扫描不限窗口误报 −78.98pt，系 col-3 照片墨污染；
限窗盒边 +10pt 后为 −1.22pt，与 PIL/文字层一致。b1 亦同理限窗。）

## 2. 版本重建（scratch 副本）—— PASS

- 整版复制至 `scratch-fix-zh-cn-nl1/work`，5 个 content 文件 OUT 用
  sed 改向 work/svg；`render.py` 未执行；生产 SVG 无写入。
- `run.py` rc=0；TOTAL 150（A2 56 / B1 69 / B2 25；
  分版 10/18/18/18/18/18/12/38）；0 HEAD TOO WIDE；0 FLOW OVERFLOW；
  P7 teaser ends 2586.3；P8 keys flow ends 2491.1。
- SVG 变化页仅 p1/p2/p5；卡片变化页仅 p1/p2/p5；其余一致。
- 印 PDF 由 work SVG 重建（`render_work.py`，复刻生产 `render.py`
  流程）；新印 PDF SHA
  `3a160cae374c2e713daac7de9f7a0bfba0f77513db31894673c0d40f8344c628`，
  44,048,879 B。

## 3. 改后 PIL 真墨横扫（work SVG → 同步后生产 SVG 复测一致）—— PASS

全 8 版 40 奶油盒 **0 负余量**；最紧 +13.5px（P4 旧盒，未动）。
- b1 P5 盒 [538.5, 648.0, 961.0, 816.0]：标题 +118.0px；盒最紧 +64.5px。
- b2 P2 盒 [989.0, 200.0, 1411.5, 447.0]：标题 +44.5px；盒最紧 +31.6px。
- b3 P1 盒 [1439.5, 588.0, 1862.0, 1288.0]：截稿行 +24.0px；盒最紧
  +24.0px（即该行）。
- 其余盒最紧 +13.5px 以上。

## 4. 改后交付 PDF 文字层 + 渲染像素（同步后生产印 PDF）—— PASS

| 项 | 文字层 advance | 渲染像素（裁决） | 标准 |
|---|---|---|---|
| b1 | +88.28pt | **+90.03pt** @100dpi（+125.0px） | ≥ +5px ✓ |
| b2 | +32.26pt | **+33.35pt** @100dpi（+46.3px） | ≥ +5px ✓ |
| b3 | +17.11pt | **+18.66pt** @300dpi（+77.8px） | ≥ +5px ✓ |

（b1 渲染复测：首次窗口 x>660.75pt 扫不到墨——标题已短至 630.72pt；
改宽窗口后测得 +90.03pt，与文字层 +88.28pt 一致。）

## 5. 孤儿行首扫描（交付印 PDF 文字层，全 8 版）—— PASS

行首闭合标点（`》/」/）/”/、/。/，`）：**NONE**。P1 数字框第 3 行现为
`21 nov., zaterdag — première van de` /
`nieuwe film《试探》`（`》` 行尾、盒内）。

## 6. p8.py extract / compare —— PASS

- extract（新 P8 SVG）：noted set = 150/150（`p8extract.json`）。
- compare 核心 vs 新版：`CLEAN missing=[] extra_count=0 uncertain=[]
  keydiff=[]`，rc=0（`p8compare.json`）。

## 7. freeze diff --strict-cjk —— PASS

核心 vs 新版 SVG：TOTAL added CJK characters: 0（p1 +51/−47、p2 +52/−52、
p3 +38/−38、p4 +42/−43、p5 +36/−37、p6 +43/−41、p7 +101/−97、
p8 +199/−202，与 proof1 的 #3 版串数相同——4 处改动只动荷兰语）。

## 8. occlusion_audit —— PASS（附空信号说明）

- 自检：planted classes 全触发 {'BOXTITLE':1,'COVER':1,'EDGE':1,
  'FOOTER':1,'LINEX':1,'TEXTX':1}，clean controls silent，rc=0。
- 新版 SVG：0 flags。
- **空信号说明**：occlusion 只报墨与后画边框/遮盖的相交；纯填充奶油盒
  无边框，标题墨越盒边时不报。b1–b3 的改前缺陷与改后修复均由 PIL
  真墨横扫 + 交付 PDF 渲染像素检出/验证，occlusion 0 flags 在此不
  作为任何证据（改前它同样是 0 flags）。

## 9. P8 最小字号 / D4/D5 抽查 —— PASS

- P8 未动（SVG 字节一致），proof1 实测 P8 最小 9.98pt（≥ 9.75pt）
  仍成立；P8 keys flow ends 2491.1 未变。
- D4/D5（去空白全文检索）：「第一次在全球总决赛的BO5里打赢T1」、
  「GEN在S16一场没输」、「淘汰赛一局没输」均 FOUND；长截稿段
  「Sluiting: 10 nov. De finale is op 15 nov. …」FOUND。
  （注：`verify_pdf.py` 的原始子串检索曾报 D4 第一句 MISSING，系
  PyMuPDF `get_text()` 在行间插换行所致的检索伪影——P4 SVG 与
  content34.py 均未动，去空白检索已确认 FOUND。）
- 150 题键未动：无 key 串被编辑；p8 compare keydiff [] 亦证。

## 10. .text.md 同步 —— PASS

4 处替换各恰 1 次（Python 断言 count==1 后写入）；
diff 仅 4 行（53/127/271/915）；50,082 → 50,059 B；
P7 `Woorden van de week: ...`（1315 行）未动。

## 11. 目视（交付印 PDF 渲染裁图）—— PASS

`render/b1-title-zoom.png`：`这一周的高频词　Woorden` 在盒内结束。
`render/b2-title-zoom.png`：`本周生活小日历　Data deze week` 在盒内
结束，与右侧照片有间隔。
`render/b3-sluiting-zoom.png`（300dpi）：`Sluiting: 10 nov. — finale
nog niet gespeeld` 的 `d` 完整，行尾距盒边有留白。
`render/b4-box-zoom.png`：`21 nov., zaterdag — première van de` /
`nieuwe film 《试探》`，`》` 行尾盒内。
（b4 首次裁图坐标误用了 SVG 像素当 100dpi 像素，截到 gloss 盒；已按
100dpi 实际尺寸重截并复核。）

## 12. 生产同步比对 —— PASS

开工快照 `opening-snapshot.sha256`（46 文件）：
- 同步后仅 10 个预期文件 FAILED（即变化）：content12.py、
  content56.py、svg/p1-touiban.svg、svg/p2-shenghuo.svg、
  svg/p5-qingnian.svg、cards/p1-touiban.png、cards/p2-shenghuo.png、
  cards/p5-qingnian.png、Lucerna-VOL4-NL.pdf、
  2026-w47-zh-cn-nl.text.md。
- 其余 36 个文件（含 web PDF、ABSTRACT.txt、其余源码/SVG/卡片）
  与开工一致。
- KIT 随后更新（新 SHA + fix1 章节，旧 SHA 保留；#3 KIT 的 b2
  “已修”不成立与 b1 漏检两处错误表述改写），为第 11 个变化文件，
  属任务要求的同步内容。
- 同步后在生产文件上重跑第 3/4/5 项：数值与 work 副本完全一致
  （PIL 最紧 +13.5px；b1 +88.28pt / b2 +32.26pt / b3 +17.11pt；
  渲染 b2 +33.35pt、b3 +18.66pt；孤儿 NONE）。
- 未 commit、未 push；核心与其他版零触碰。
