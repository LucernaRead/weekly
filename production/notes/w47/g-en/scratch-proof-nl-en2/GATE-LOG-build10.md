# GATE-LOG — W47 nl-en proof1 第 2 棒（build 10，机械门自跑）

- 版：`2026-w47-nl-en`，VOL.4，刊期 2026-11-16–2026-11-22
- 校对员：第 2 棒（独立复校）
- 日期：2026-11-11
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3；全部机械门）
- 对象 SHA（开工实测，与任务登记逐字一致；收工复核未变）：
  - print `De-Lucerna-VOL4-nl-en.pdf` 12,665,899 B `29073788fa2fc7dfd426e6d209251f0919bdbf2cb33f79dbbc10eb15f92b2342`
  - web `De-Lucerna-VOL4-nl-en-web.pdf` 1,610,560 B `6fd0ad3d700d686f9889faecd5e6076a6d9c309372f6871ad0faa4e41a253f98`
  - text `2026-w47-nl-en.text.md` 45,111 B `84ed9f3555e4995de8c4450ca9180019414ad907a63ed384ab632a8293612f91`
- 文件名说明：本 scratch 内已有的 `GATE-LOG.md` 是更早一轮 build-8 proof2-en2 的，本轮 build-10 另存此文件，未覆盖。
- 探针：开工 `git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29b…`，RC=0）；
  scratch 真实写文件成功（`probe.txt`）；工作拷贝在自有 scratch（`work/`），生产只读。
- 自写脚本（本棒新写，存于本 scratch）：`gates2.py`、`geo2.py`（v2 修正版）、`probe2.py`、`p8title2.py`。

## 1. run.py（构建重跑，工作拷贝）

- `run.py` RC=0；TOTAL **150**；by page 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；
  by type complete 65 / choice 44 / matching 8 / true-or-false 7 / make-sentences 8 / cloze-choice 13 / translate 4 / writing 1；
  model words 81。`overflow` / `TOO WIDE` 命中 0（`run.log`）。
- `P4 col3 ends 1229.6`（D11 盒底，与 SVG 一致）。

## 2. SVG 重建 8/8 字节一致

- 工作拷贝重跑 `run.py` 后 8 个 SVG 与交付 `svg/` 逐字节一致（`svg-rebuild-check.log`：8/8 OK）。

## 3. 重渲印 PDF 与交付逐字节相同

- 工作拷贝 `render.py` RC=0；重渲 `De-Lucerna-VOL4-nl-en.pdf` 12,665,899 B，
  sha256 `29073788fa2fc7dfd426e6d209251f0919bdbf2cb33f79dbbc10eb15f92b2342`，`cmp` 逐字节相同（`render.log`）。

## 4. freeze 核心 baseline 8/8

- `tools/freeze.py baseline --build production/2026-w47/core-nl --core-svg core-nl/svg`：**8/8 SVGs byte-identical**，RC=0；
  shipped core SVGs 完整性复核无变化（`freeze-baseline.log`）。

## 5. freeze diff --strict-cjk（RC=1，裁定误报，见 PROOF-NOTE O2）

- `tools/freeze.py diff --core-svg core-nl/svg --edition-svg <edition>/svg --strict-cjk`：RC=1，
  `STRICT-CJK FAIL`，TOTAL added CJK 15。
- 裁定：15 个全部是 U+3000（p1 +1、p2–p8 各 +2）；edition SVG 可见文本行无汉字、无 CJK 标点（逐版 0）；
  U+3000 是 SOP §1.1 强制分隔符，core 每版亦有 12–19 个；工具文档将 strict 规则限定于 zh/ja 版。
  结论：**误报，非缺陷**（`freeze-diff.log`、`freeze-diff.json`、`freeze-diff-adjud.log`、`sanse-check.log`）。

## 6. occlusion 0 flags

- `tools/occlusion_audit.py <edition>/svg`：selftest OK（6 类阳性对照全触发，干净对照静默），**0 flags**，RC=0（`occlusion.log`）。

## 7. 奶油盒 PIL 真墨扫 0 flags（+ 像素复核 0）

- 自写 `geo2.py`（v2）：每奶油 rect（#f0eee5）内文本用 PIL 真墨盒（canonical 公式 y−ascent+b）核对右缘/底缘：
  **CREAM FLAGS 0**。v1 曾报 14 flags，系 getbbox 未减 ascent 的度量错，已修正并记录（`geo2_v1.py` 保留作对照）。
- 像素复核（`probe2.py`，numpy 暗像素 max<200，1× cards + 交付 150dpi）：
  P2 EN-JIJ 盒底条带 0、P5 盒底 0、P7 BRIEVEN 盒底 0、P4 HET-PROGRAMMA 盒底 0、P3 col3 盒底 0。
  v1 探针的 P2 422px / P1 423px 均为轻色伪影（奶油底边抗锯齿 / y=1853 #d8d2c4 细线），暗像素口径下为 0。

## 8. spill 扫 0（31 候选全裁定）

- 自写 `geo2.py` spill 带（盒上下/左右 60px）：候选 31 条，分属相邻盒盒题 8、页眉/栏目条 5、图注/说明 6、
  上一盒末行 7、下一盒首行/注释 5；无一条为盒内文本出盒（`geo2v2.log`，逐条在列）。

## 9. 孤儿扫 0

- 自写 `geo2.py`：行重建（基线分组、>60px 分段）(a) 独立标点行 **0**、(b) 标点行首 **0**、暴力单元素行首 **0**；
  另查 8 版可见文本行 CJK 标点 0（`d6-d10-svg.log`）。

## 10. p8 extract 150/150

- `tools/p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150`：noted set **150 of 150**，RC=0（`p8-extract.log`）。

## 11. p8 compare CLEAN，keydiff [137, 138]

- `tools/p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`：
  status **CLEAN**，missing=[] extra=[] uncertain=[]，**keydiff=[137, 138]**，RC=0（`p8-compare.log`）。
- 137/138 合法重定向：core 键为中文译文，en 版为英文译文（荷→英）；139/140 键为荷兰语（英→荷），与 text.md 一致。
  配对键再验：25–28 = d/c/a/b，141–144 = b/c/d/a（`keydiff-137-140.log`、P8 节点直查）。

## 12. P8 最小字号 10.12pt ≥ 9.75pt

- PyMuPDF 答案区（delta 同款口径 y≥1328×scale）：min **10.12pt**，median **10.12pt**，187 spans；
  全页最小亦 10.12pt（`printweb-delta-method.log`）。§1.1 底线 9.75pt，通过，无需让步。

## 13. print/web 文字层 8/8 posdiff=0、msdiff=0（词序法）

- delta 同款方法（sorted-text 空白分词）：P1–P8 token 数 790/828/738/735/807/748/915/2319，
  print=web，posdiff=0、msdiff=0（`printweb-delta-method.log`）。
- 坐标法（0.1pt，`gates2.py`）P1 另有 2 处 ≤0.22pt 刊头舍入差（`De Lucerna` Δx 0.21–0.22pt），内容相同，见 PROOF-NOTE O3。
- pdftotext：print 45,434 B / web 45,434 B，RC=0；web PDF 1,610,560 B < 7 MB。
- 徽章：edition A2 8 / B1 24 / B2 3 = core（`gates2.log`）。

## 14. §1.1 SVG 审计

- 描边矩形 0；VOL.5 出现 5 次 = core 5 次；纸色填充 8 版；斜体 span 印 = 网 = 1。
- 出调色板填充：仅蛾标路径内 7 色（P1）与绿底次级文字 #CAC8BA（P1×1、P7×2），与 core-nl 逐项同数；
  金色 #d4af37/#c9a227 无；"gold" 字串命中为 base64 图数据噪声（`gates2.log`、`gates2-followup.log`）。

## 15. 日期星期全验

- `date -d`（Europe/Amsterdam）：2026-11-01 周日、11-11 周三、11-13 周五、11-14 周六、11-15 周日、11-16 周一、
  11-18 周三、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六——文中全部星期表述吻合。

## 16. D4 / D5 措辞在位

- D4：text.md `— Correct:` **142**、`（Correct ` **8**；P8 印版短横式 `key — note`：答案区 150 行以题号起行、
  149 行含 ` — `（第 150 题为 `✓`）；`✓ marks the writing task` 在位。
  注：P8 SVG 内无 "Correct" 字样属既定短横排版，非缺失（p8.py 双式兼容，extract 150/150 为证）。
- D5：`content34.py` facts 第 4 条 + SVG P4（x=1461.5, y=1054.37）
  `Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.` 在位。

## 17. D6–D11 逐项（见 PROOF-NOTE 表，证据文件 `d6-d10-svg.log`、`pixelprobe.log`、`probe2.log`）

- D6 ✓ / D7 ✓ / D8 ✓ / D9 ✓（content8.py:75 + text.md:415 + P8 节点 y=2222.28 三处同步）/ D10 ✓。
- D11 ✓：top reserve 89（content34.py:130-138）；盒 rect (1439.5, 591.6, 422.5, 638.0)，底 1229.6；
  末基线 1209.49，基线余量 **+20.11px**；真墨最低 1209.00（cards 1×，+20.60px）/ 1208.91（交付 150dpi，+20.69px）；
  盒底条带暗像素 0；P3 同形盒 +16.20px。

## 18. P8 标题 `A　VUL DE KRONIEK IN` 独立实测（见 PROOF-NOTE O1）

- PIL 真墨右缘 323.00；交付印 PDF 300dpi 紧带实测墨右 **320.63**，栏内余 **+189.87px**（栏右缘 510.5）；
  全行扫描伪影 +28.14px 系第 2 栏 B1 色块（左缘 538.64）；core-nl 同位逐值相同（n=14538 全同）；
  300dpi 裁图目视干净（`p8title2.log`、`p8title-pixels.log`、`p8title-tight.log`、`p8title-crop300.png`）。
  结论：观察，非缺陷。

## 19. 标题实测数

- 大标题行 17 条 + 奶油盒题 21 条 = **38 条**（按 SVG 文本 run 计 46 个）；盒题墨迹扫描 21/21 在盒内，最紧 **+8.5px**，
  0 出边（`geo2v2.log`）。“56 标题”在本版无任何定义可复现，不采用。

## 20. 编号 / 头条 / 范文 / 弯引号

- 编号 1–150 无缺无重（`text.md` 正则重数：missing []、extra []）。
- 头条去空白 38 字符 ≤ 56；范文 81 词（空白切分，含独立短横 `–`；不计为 80，仍在 80–100 档内）。
- 弯引号 U+2018/2019/201C/201D/201A/201E/2032/2033 在 `content*.py`、SVG、`.text.md` 中均为 0。

## 汇总

| 门 | 结果 |
|---|---|
| run.py RC=0 / 150 题 0 溢出 | 通过 |
| SVG 重建 8/8 字节一致 | 通过 |
| 重渲印 PDF 与交付逐字节相同 | 通过 |
| freeze 核心 baseline 8/8 | 通过 |
| freeze diff --strict-cjk | RC=1，裁定误报（15×U+3000，见 O2） |
| occlusion 0 flags | 通过 |
| 奶油盒 PIL 真墨扫 0 flags + 像素条带 0 | 通过 |
| spill 0（31 候选全裁定） | 通过 |
| 孤儿扫 0 / 0 / 0 | 通过 |
| p8 extract 150/150 | 通过 |
| p8 compare CLEAN，keydiff [137,138] 合法 | 通过 |
| P8 最小字号 10.12pt ≥ 9.75pt | 通过 |
| print/web 文字层 8/8 pos0 ms0 | 通过 |
| §1.1 | 通过（蛾标色 core 同数，无金） |
| 日期星期全验 | 通过 |
| D4 / D5 措辞在位 | 通过 |
| D6–D11 逐项 | 通过 |
| P8 标题实测 | 观察，非缺陷 |
| 标题数实测 38 条 / 盒题 21/21 在盒内 | 通过 |
| **D12（F 组 142/144 `=` 缺空格）** | **缺陷，见 PROOF-NOTE-build10.md** |

**总结论：(b) 1 项缺陷（D12），其余全部门禁通过。**
