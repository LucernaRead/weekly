# GATE-LOG — 2026-W47 de-en 第一轮独立复校（叶子）

- 时间：2026-11-11 03:35–03:55 UTC；解释器：`~/workspace/weekly-git/tools/venv/bin/python`，Pillow 13.0.0
  （与 builder 重建 2 所用 venv 一致；系统 python3 Pillow 10.2.0 未使用）。
- 全部输出写在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-en1/gates/`；
  原版目录、core-de、tools/ 均未写入（verify.py / run.py / render.py 未在原版目录跑）。

## 1. 渲染与文本抽取（render_extract.py）

- 印刷 PDF 8 页 @100 dpi → `render/print-p1.png` … `print-p8.png`（2032×2813）。
- 网页 PDF P1/P8 @100 dpi → `render/web-p1.png`、`render/web-p8.png`。
- `<text>` 抽取 → `text/p1.txt` … `p8.txt`、`text/all.txt`（1771 个元素）。
- P8 最小 span（PyMuPDF，印刷 PDF）：9.94pt；逐页最小 11.62 / 12.75 / 11.62 / 11.62 /
  11.62 / 12.75 / 11.62 / 9.94pt。
- 撇号放大裁切：`render/crop-p2-apos.png`（Let's calculate / This week's dates，250 dpi）、
  `render/crop-p7-learners.png`（Learners' …，250 dpi）。

## 2. 机械门（mech-gates-1.log）

```
== interpreter == /home/hatch/workspace/weekly-git/tools/venv/bin/python / Pillow 13.0.0
== occlusion == selftest OK: planted classes fired
  {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
  .../2026-w47-de-en/svg: 0 flags / rc=0
== p8 extract == noted set = 150 of 150 (parse: joined) / rc=0
== p8 compare == status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150] / rc=0
== freeze diff == p1: +30/-44, CJK core 189 -> edition 18, added 0
  p2: +33/-31, 221 -> 17, added 1 {U+3000}; p3: +47/-46, 208 -> 16, added 1
  p4: +24/-21, 174 -> 15, added 1; p5: +40/-44, 210 -> 16, added 1
  p6: +35/-32, 243 -> 17, added 1; p7: +59/-77, 434 -> 23, added 1
  p8: +148/-137, 1434 -> 24, added 1 / TOTAL added CJK characters: 7 / rc=0
== measure == 24/24 PASS, 0 FAIL / rc=0
```

## 3. 扫描（scans.py → gates/scans.json）

- chips：{1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35}，TOTAL 141；P8 A2 22 / B1 13。
- U+2019：逐页 0，总数 0；U+0027 逐页 1/2/1/1/2/1/3/0，共 11。
- CJK 残留：8 页 `<text>` 中唯一 CJK 字符为 U+3000（每页 12–16 个串）。
- 禁词 18 项：全部 0 页命中。VOL.4 出现 9 次；VOL.3/VOL.2 0 次；VOL.5 6 次（下期预告）。
  页脚精确串逐页 1 枚。
- pdftotext：default print 50,445B / web 50,446B，词多重集相同；raw 均为 49,288B，
  归一化后完全相同（`gates/print.txt`、`gates/web.txt`）。
- freeze 直接 sha256（渲染级冻结交集，sorted + "\n" 连接）：
  P1 147 083e2a2a / P2 163 689045ad / P3 195 093cf378 / P4 166 df1bebf7 /
  P5 173 86fa4421 / P6 175 2bbe05f9 / P7 150 b7aa0771 / P8 186 57e118e7——
  计数与 sha 前 8 位与 builder 所称逐一吻合，8/8。

## 4. 冻结源码级 + REG 独立复现（freeze_source_reg.py → gates/freeze-source.json、reg-mine.json）

- AST 字符串常量：核心 2389 个（含 CJK 514 处），版内 2397 个（含 CJK 仅 2 处不渲染内容）。
- 核心无 CJK 常量在版内缺失：仅 5 处，均预期——masthead 副标题、'（'、'）'、' · '、
  PDF 文件名 'Die-Lucerna-VOL4-de.pdf'。
- 版内新增无 CJK 常量 449 处（230 distinct），含非 ASCII 者 61 条，抽查均为德语词+英文释义串。
- REG 副本重跑：总数 150，编号连续；分版 10/18/18/18/18/18/12/38；
  级别 A2 69 / B1 67 / B2 14；题型 MC 52 / fill-in 41 / transformation 11 / true-false 8 /
  cloze 8 / sentence building 8 / matching 12 / translation 4 / dialogue 5 / writing 1。
- 副本 8 个 SVG 与原版 SVG 字节相同（8/8）。
- 我方 REG vs builder `en/keycheck-150.json`：150/150 逐项一致，差异 0。
- REG 键 vs 我方 P8 抽取键：149/150 精确；唯一差异 Q150（抽取器截断，见 PROOF-NOTE §2）。
- 核心 P8 自跑抽取 → `gates/p8extract-core.json`（150/150），用于 keydiff 逐条核实。

## 5. verify.py 只读复现（verify_repro.py → gates/verify-repro.json）

- verbatim 8 句各 2 次，OK=True。
- 样式常量 PAPER #fbfaf6 / INK #302c28 / OLIVE #46581f / CLOTH #37402f；旧式色值 0 个。
- MUSTER 标签 (84 words)，实数 84 词，文本在 P8 SVG 内。
- 页脚精确串逐页 1 枚；页码行 Page 1–8 of 8 逐页在位；P1 刊头/副标题/周头在位。
- 头条去空白 40 字符（≤56）。
- SVG 最小字号：P8 13.25 单位 → 9.94 PDF pt，≥9.75pt。
- 图表 44+33+23=100；日期算术 18+11=29、15+7=22、16+6=22 全对；
  星期：16.11 周一、13.11 周五、18.11 周三、20.11 周五、22.11 周日、27.11 周五、29.11 周日。
- P6 橄榄条宽度 748/561/391。

## 6. 身份复核（收尾）

- 印刷 PDF 10,966,416 字节，SHA-256 a997c6cefe8467bdd37a71158e0f61ceff16d653039f50159b1608305b3a4b87。
- 网页 PDF 1,555,614 字节，SHA-256 62623cb5996644004ba48a6ed7246cdd0584bec3a2549123174db318384a3a90。
- text.md 49,676 字节，SHA-256 0749ad78f536883f8f3a484d7c93f026d0f7d7f433891861333f7a9a8fbf3830。
- 结论：双 PDF 身份与任务一致，复校前后未变。
