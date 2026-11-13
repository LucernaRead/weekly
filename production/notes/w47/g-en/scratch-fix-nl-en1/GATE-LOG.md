# GATE-LOG — W47 nl-en fix1（proof1 D12，build 11，机械门自跑）

- 版：`2026-w47-nl-en`，VOL.4，刊期 2026-11-16–2026-11-22
- 修复员：fix1（与 proof1 不同人）
- 日期：2026-11-11
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3；全部机械门）
- 对象：重建 build 11（scratch `work/2026-w47-nl-en/` 构建并驗證後拷回生产；生产三 SHA 见 FIX-LOG 首行）：
  - print `De-Lucerna-VOL4-nl-en.pdf` 12,665,893 B `79fa049b318d94f15f28fe23daefd2513221a77fde6511c694aee109bacf3239`
  - web `De-Lucerna-VOL4-nl-en-web.pdf` 1,610,562 B `d493e11f3c27c7e46e0412c79f1b9208bfe804e39eac2e2203a033fad2818538`
  - text `2026-w47-nl-en.text.md` 45,115 B `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978`
- 旧三 SHA（build 10，已 superseded）：print `29073788fa2fc7dfd426e6d209251f0919bdbf2cb33f79dbbc10eb15f92b2342` / 12,665,899 B；web `6fd0ad3d700d686f9889faecd5e6076a6d9c309372f6871ad0faa4e41a253f98` / 1,610,560 B；text `84ed9f3555e4995de8c4450ca9180019414ad907a63ed384ab632a8293612f91` / 45,111 B。
- 探针：开工 `git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29b…`，RC=0）；scratch 真实写文件成功（`probe.txt`）；TMPDIR = 自有 scratch 下 `tmp/`。
- 自带脚本（本轮，存于本 scratch）：`sweep_eq.py`（`=` 间距重扫）、`p8_width.py`（P8 答案行实测）、`gates.py`（`scratch-fanout-nl/gates.py` 副本）、`geo2.py`（proof1 几何扫副本，ED/S 改指本轮 scratch）。

## 1. run.py（构建重跑，scratch 副本）

- `run.py` RC=0；TOTAL **150**；by page 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；
  by type complete 65 / choice 44 / matching 8 / true or false 7 / make sentences 8 / cloze choice 13 / translate 4 / writing 1；
  model words 81。`overflow` / `TOO WIDE` 命中 0（`en-build11.log`）。
- `P4 col3 ends 1229.6`（D11 在位），`P7 col3 ends 1927.5`，`P3 col3 ends 1106.6`——与 build 10 相同。

## 2. SVG 重建 8/8（仅 p8 变，且仅 2 行）

- 与生产 build 10 逐字节比较：p1–p7 SAME，仅 `p8-toets.svg` DIFF；p8 文本 run 383=383，仅
  `142. c — groepswinst=group win c` → `groepswinst = group win c` 与
  `144. a — gedicht=poem a` → `gedicht = poem a` 两行变。
- `gates.py` freeze repro（clean dir 重跑 `run.py`）：**8/8 字节一致**。

## 3. 重渲印 PDF + 网 PDF + text 导出

- `render.py` RC=0：cards 8 张（仅 `p8-toets.png` 变），印 PDF 12,665,893 B。
- `webpdf.py` RC=0：网 PDF 1,610,562 B，45,438 text bytes。
- `export_fanout.py . en` RC=0：`.text.md` 45,115 B；142 单题行 + 2 match headers + 8 match items = 150；8 golden；6 gloss。
- `.text.md` diff vs build 10：仅 419/421 两行。印/网 PDF 文字层 diff vs build 10：仅 142/144 两行。

## 4. freeze 核心 baseline 8/8

- `tools/freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-baseline11.json`：**8/8 SVGs byte-identical**，RC=0；core integrity：shipped core SVGs unchanged（`freeze-baseline11.log`）。
- 注：首次调用漏了必需的 `--out` 参数（RC=2），补参数后重跑通过；首次失败未写任何文件。

## 5. freeze diff --strict-cjk（RC=1，裁定误报，与 build 10 O2 同案）

- `tools/freeze.py diff --core-svg core-nl/svg --edition-svg <scratch-work>/svg --strict-cjk`：RC=1，
  `STRICT-CJK FAIL`，TOTAL added CJK 15（p1 +1、p2–p8 各 +2）。
- 裁定：15 个全部是 U+3000；重建后全版可见文本 CJK 清单 127 个，全部是 U+3000，零汉字、零 CJK 标点；
  U+3000 是 SOP §1.1 强制分隔符，core 每版亦有 12–19 个；工具文档将 strict 规则限定于 zh/ja 版，
  本版为 en 读者版，不适用。结论：**误报，非缺陷**（`freeze-diff11.log`）。

## 6. occlusion 0 flags

- `tools/occlusion_audit.py <edition>/svg`（经 `gates.py`）：selftest OK，**0 flags**，RC=0（`en-gates11.log`）。

## 7. 奶油盒 PIL 真墨扫 0 flags（geo2.py v2，proof1 同款工具复跑）

- 自写复跑 `geo2.py`（proof1 `geo2.py` 副本，ED/S 改指本轮 scratch）：每奶油 rect（#f0eee5）内文本用 PIL 真墨盒核对右缘/底缘：
  **CREAM FLAGS 0**（`geo2v2-11.log`、`geo2v2.json`）。

## 8. spill 扫 31 候选，与 build 10 集合逐项相同

- `geo2.py` spill 带（盒上下/左右 60px）：候选 **31 条**，与 proof1 `geo2v2.json` 的 31 条逐项相同（页/类/文本全同）；
  分属相邻盒盒题、页眉/栏目条、图注/说明、上一盒末行、下一盒首行/注释，无一条为盒内文本出盒。

## 9. 孤儿扫 0

- `geo2.py`：行重建 (a) 独立标点行 **0**、(b) 标点行首 **0**、暴力单元素行首 **0**。

## 10. p8 extract 150/150

- `tools/p8.py extract --p8 <scratch-work>/svg/p8-toets.svg --total 150`：noted set **150 of 150**，RC=0（`p8-extract11.log`）。

## 11. p8 compare CLEAN，keydiff [137, 138]

- `tools/p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 <scratch-work>/svg/p8-toets.svg --total 150`：
  status **CLEAN**，missing=[] extra_count=0 uncertain=[]，**keydiff=[137, 138]**，RC=0（`p8-compare11.log`）。
- 137/138 与 build 10 相同：合法重定向（core 键为中文译文，en 版为英文译文；荷→英）。
  配对键再验：141–144 = b/c/d/a（源码 + text.md + SVG 三处一致）。

## 12. P8 最小字号 10.12pt ≥ 9.75pt

- PyMuPDF 答案区（gates.py 同款口径 y≥1328×scale）：min **10.12pt**，median **10.12pt**，187 spans；
  §1.1 底线 9.75pt，通过，无需让步。

## 13. print/web 文字层 8/8 posdiff=0、msdiff=0（词序法）

- gates.py 同款方法（sorted-text 空白分词）：P1–P8 token 数 790/828/738/735/807/748/915/2323，
  print=web，posdiff=0、msdiff=0（`en-gates11.log`）。
- P8 token 数 2323（build 10 为 2319）：+4 = 2 个新增空格各把 `groepswinst=group` / `gedicht=poem` 一个 token 拆成三个，
  与修复一致，非异常。
- pdftotext：print 45,438 B / web 45,438 B，RC=0；web PDF 1,610,562 B < 7 MB。
- 徽章：edition A2 8 / B1 24 / B2 3 = core。

## 14. §1.1 SVG 审计

- 描边矩形 0；VOL.5 = 5 = core 5；纸色填充 8 版；off-palette {}；无金色。

## 15. D12 修后实测（`p8_width.py`，`p8-width11.log`）

- 重建 P8 卡片（1950×2700，1:1 SVG 单位）像素墨 + `svglib.text_w` advance 双重度量，栏 [1439.5, 1862.0]（422.5px）：
  141 adv 238.5px / 墨右 1675 / 余 +187.0px；**142 adv 215.5px / 墨右 1652 / 余 +210.0px**；
  143 adv 152.4px / 墨右 1588 / 余 +274.0px；**144 adv 158.6px / 墨右 1595 / 余 +267.0px**；
  145 adv 142.0px / 墨右 1579 / 余 +283.0px。
- 141–145 基线均匀间距 29.66px——无换行插入、无溢出。P8 标题未动。

## 16. `=` 间距重扫（修后 0）

- `sweep_eq.py`（源码字面量 + SVG 文本节点 + `.text.md`）：**MISSING-SPACE `=` 0**，有空格 ` = ` 127 处
  （修前 121 处 +6 = 2 行 × 3 层）；生产盘上复扫同样 0（`eq-sweep-post-production.log`）。

## 17. gates.py 总汇（9/9 ALL PASS）

- `gates.py`（副本，EDITION=scratch work）：occlusion PASS、p8_extract PASS、p8_compare PASS、
  freeze_sha256 PASS、print_web_text PASS、pdftotext_nonempty PASS、p8_fontsize PASS、
  p8_chips PASS、s11_svg PASS。**OVERALL: ALL PASS**，RC=0（`en-gates11.log`、`gates-en.json`）。

## 汇总

| 门 | 结果 |
|---|---|
| run.py RC=0 / 150 题 0 溢出 | 通过 |
| SVG 重建 8/8（仅 p8 变 2 行） | 通过 |
| freeze 核心 baseline 8/8 | 通过 |
| freeze diff --strict-cjk | RC=1，裁定误报（15×U+3000，见 §5） |
| occlusion 0 flags | 通过 |
| 奶油盒 PIL 真墨扫 0 flags | 通过 |
| spill 31（与 build 10 集合相同） | 通过 |
| 孤儿扫 0 / 0 / 0 | 通过 |
| p8 extract 150/150 | 通过 |
| p8 compare CLEAN，keydiff [137,138] | 通过 |
| P8 最小字号 10.12pt ≥ 9.75pt | 通过 |
| print/web 文字层 8/8 pos0 ms0 | 通过 |
| §1.1 | 通过 |
| D12 修后实测（142/144 在栏内、无换行） | 通过 |
| `=` 缺空格重扫 0 | 通过 |

**总结论：D12 已修；全部机械门通过（仅 strict-CJK 为已裁定的 U+3000 误报）。**
