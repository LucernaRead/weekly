# GATE-LOG — 2026-W47 de-en 重建后第二轮独立复校

- 时间：2026-11-11 04:05–05:30 UTC；解释器：`~/workspace/weekly-git/tools/venv/bin/python`，Pillow 13.0.0
  （与 builder 重建 3 所用 venv 一致；系统 python3 无 fitz，未使用）。
- 全部输出写在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-en2/`；
  原版目录、core-de、tools/ 均未写入（verify.py / run.py / render.py 未在原版目录跑）。
- 探针：开工前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` RC=0；
  每批命令前重探一次，全部通过；真实写文件探针通过；全程无 `Disk quota exceeded`。

## 0. 身份核对

```
sha256sum Die-Lucerna-VOL4-de-en.pdf Die-Lucerna-VOL4-de-en-web.pdf 2026-w47-de-en.text.md
47aae035c9531818bce832e25b2aed6ed2557c18229c514bf32443fb6becd429  Die-Lucerna-VOL4-de-en.pdf      (10,966,409 B ✓)
37ba00d4fcf83f7dd78fe6427d5b0c1ae70c9035fbe8dd345dfde8de13d12875  Die-Lucerna-VOL4-de-en-web.pdf  (1,555,605 B ✓)
2eb0363202b8c9eacc8aaaf5008eedab614b8ddb0301082e92eb80cd25d6b7f5  2026-w47-de-en.text.md           (49,665 B ✓)
```
收尾复核：SHA/字节/mtime 与开工时一致，未被改动。

## 1. Q34 / 弯标点专项（自写 inline 检查，venv python）

- Q34：源码 `content34.py` 新 1 / 旧 0；`.text.md` 新 1 / 旧 0；`svg/p3-kultur.svg` 新 1 / 旧 0；
  印刷 PDF 文字层（空白归一化）新 1 / 旧 0；网页 PDF 同新 1 / 旧 0；core-de `content34.py` 新 1 / 旧 0。
- U+2019：8 页 SVG `<text>` 总数 0；text.md 0。U+0027 逐页 1/2/1/1/2/1/3/0，共 11。
- U+201C：逐页 P1 5 / P2 0 / P3 0 / P4 0 / P5 6 / P6 0 / P7 21 / P8 3，共 35；U+201D：P8 2，其余 0，共 2。
  core-de U+201D 全版 0；de-fr/es/it/pt/nl/ru/ja/ko/zh-tw 各版全版 U+201D 均为 0（仅 de-en 为 2）。
- 250 dpi 裁切：`render/crop-p8-hbox2.png`（D1）、`render/crop-p8-key67.png`（D2）、
  `render/crop-p3-boxtitle.png`（P3 标题收进盒内）。
- guillemet «»：P1/P5/P7/P8 共 5 处，全部与 core SVG 同串（冻结原文），渲染紧贴。

## 2. 渲染与文本抽取（render_extract.py，venv python，RC=0）

- 印刷 PDF 8 页 @100 dpi → `render/print-p1.png` … `print-p8.png`（2032×2813）。
- 网页 PDF P1/P8 @100 dpi → `render/web-p1.png`、`render/web-p8.png`。
- `<text>` 抽取 → `text/p1.txt` … `p8.txt`、`text/all.txt`（1771 个元素）。
- P8 最小 span（PyMuPDF，印刷 PDF）：9.94pt；逐页最小 11.62 / 12.75 / 11.62 / 11.62 /
  11.62 / 12.75 / 11.62 / 9.94pt。
- P6 图表 strip：`render/chart-p6-print.png` / `render/chart-p6-web.png`（150 dpi），目视一致；
  图表区 span 坐标印刷/网页逐一相同至 0.1pt（44 % (991.5,1108.9)、33 % (851.2,1147.9)、23 % (723.8,1186.9)）。

## 3. 机械门（mech-gates-1.log）

```
== occlusion == selftest OK: planted classes fired
  {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
  .../2026-w47-de-en/svg: 0 flags / rc=0
== p8 extract (edition) == noted set = 150 of 150 (parse: joined) / rc=0
== p8 extract (core) == noted set = 150 of 150 (parse: joined) / rc=0
== p8 compare == status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150] / rc=0
== freeze diff == p1: +30/-44, CJK core 189 -> edition 18, added 0
  p2: +33/-31, 221 -> 17, added 1 {U+3000}; p3: +47/-46, 208 -> 16, added 1
  p4: +24/-21, 174 -> 15, added 1; p5: +40/-44, 210 -> 16, added 1
  p6: +35/-32, 243 -> 17, added 1; p7: +59/-77, 434 -> 23, added 1
  p8: +148/-137, 1434 -> 24, added 1 / TOTAL added CJK characters: 7 / rc=0
== measure == 24/24 PASS, 0 FAIL / rc=0
  （命令：tools/venv/bin/python scratch-fanout-de/measure.py en <edition-dir>；仅打印，不写版目录）
```

## 4. 扫描（scans.py → gates/scans.json，RC=0）

- chips：{1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35}，TOTAL 141；P8 A2 22 / B1 13。
- U+2019：逐页 0，总数 0；U+0027 逐页 1/2/1/1/2/1/3/0，共 11。
- CJK 残留：8 页 `<text>` 中唯一 CJK 字符为 U+3000（每页 12–16 个串）。
- 禁词 18 项：全部 0 页命中。VOL.4 出现 9 次；VOL.3/VOL.2 0 次；VOL.5 6 次。页脚精确串逐页 1 枚。
- pdftotext：default print 50,434B / web 50,435B，词多重集相同；raw 均为 49,277B，
  归一化后完全相同（`gates/print.txt`、`gates/web.txt`）。
  逐页词多重集：P1–P8 全部相同；P6 仅 pdftotext 换行归属差 1 字节（词相同，见 §2 坐标比对）。
- freeze 直接 sha256（渲染级冻结交集，sorted + "\n" 连接）：
  P1 147 083e2a2a / P2 163 689045ad / P3 195 fc88f676 / P4 166 df1bebf7 /
  P5 173 86fa4421 / P6 175 2bbe05f9 / P7 150 b7aa0771 / P8 186 57e118e7——
  计数与 sha 前 8 位与 builder 所称逐一吻合，8/8（P3 为新 Q34 指纹）。

## 5. 冻结源码级 + REG 独立复现（freeze_source_reg.py → gates/freeze-source.json、reg-mine.json，RC=0）

- AST 字符串常量：核心 2389 个（含 CJK 320 distinct / 545 处），版内 2397 个。
- 核心无 CJK 常量在版内缺失：仅 5 处，均预期——masthead 副标题、'（'、'）'、' · '、
  PDF 文件名 'Die-Lucerna-VOL4-de.pdf'。
- 版内新增无 CJK 常量 449 处（230 distinct），含非 ASCII 者 61 条，抽查均为德语词+英文释义串。
- REG 副本重跑：总数 150，编号连续；分版 10/18/18/18/18/18/12/38；
  级别 A2 69 / B1 67 / B2 14；题型 MC 52 / fill-in 41 / transformation 11 / true-false 8 /
  cloze 8 / sentence building 8 / matching 12 / translation 4 / dialogue 5 / writing 1。
- 副本 8 个 SVG 与原版 SVG 字节相同（8/8）。
- 我方 REG vs builder `en/keycheck-150.json`：150/150 逐项一致（n/page/level/type/key），差异 0。
- REG 键 vs 我方 P8 抽取键：149/150 精确；唯一差异 Q150（抽取器截断，见 PROOF-NOTE §4）。

## 6. verify.py 只读复现（verify_repro.py → gates/verify-repro.json，RC=0）

- verbatim 8 句各 2 次，OK=True。
- 样式常量 PAPER #fbfaf6 / INK #302c28 / OLIVE #46581f / CLOTH #37402f；旧式色值 0 个。
- MUSTER 标签 (84 words)，实数 84 词，文本在 P8 SVG 内。
- 页脚精确串逐页 1 枚；页码行 Page 1–8 of 8 逐页在位；P1 刊头/副标题/周头在位。
- 头条去空白 40 字符（≤56）。
- SVG 最小字号：P8 13.25 单位 → 9.94 PDF pt，≥9.75pt。
- 图表 44+33+23=100；日期算术 18+11=29、15+7=22、16+6=22 全对；
  星期：16.11 周一、13.11 周五、18.11 周三、20.11 周五、22.11 周日、27.11 周五、29.11 周日。
- P6 橄榄条宽度 748/561/391。

## 7. box-title 独立实测（从已发货 SVG 取串，text_w 量墨水宽）

- P2 `DIE STILLE WOCHE　A quiet week` 24pt 394.6px；P3 `WEIHNACHTSWÖRTER　Words` 24pt 359.9px；
  P3 `DER TIPP　Editor's tip` 24pt 262.5px；P5 `ADVENTSWÖRTER　Advent words` 24pt 397.9px；
  P7 `DER WERKZEUGKASTEN　Toolbox` 23pt 382.9px；P7 `LESERBRIEFE　Readers' letters` 23pt 352.8px；
  P7 `NOCH EIN WORT　One more word` 22pt 366.1px——预算 400.5px，7/7 通过，与 builder 日志逐一吻合。

## 8. text.md 全量比对

- `gates/textmd-core-diff.txt`：core vs edition diff 940 行，235 组改动，逐组读过，全部为讲解层中文→英文。
- core 非 CJK 行 327 行，仅 2 行未入本版（版头 slug 行、masthead 副标题，均为预期）。
- 本版 text.md：汉字/假名/韩字 0 个；U+3000 计 122 处；总 48,034 字符。
- ABSTRACT.txt：356 B，单行，无 ASCII 双引号，内容与 KIT 一致。

## 9. 网页 PDF 字体（工具层，pdffonts）

- 网页 PDF：无 `LucernaNewsreader-Bold`、无 Italic 子集，只有 `LucernaNewsreader-Regular`（旧 webpdf.py，`:style=Bold`）。
  印刷版含 `Newsreader16pt-Italic`。内容与几何不受影响（见 PROOF-NOTE §9 T1）。

## 10. 结论

(b) 2 处缺陷：D1（P8 H 框英文说明 `“My week in November”`）、D2（P8 键 67 注 `“Im Lande des Christkinds”`）——
英文弯双引号 U+201C/U+201D 在英语值里，与重建 2 已修的 U+2019 同一宽体字形缺陷类。
其余全部通过。未改源、未重建、未 commit、未 push。
