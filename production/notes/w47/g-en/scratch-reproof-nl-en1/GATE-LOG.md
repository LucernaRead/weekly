# GATE-LOG — W47 nl-en reproof（第二轮全量复校，build 11）

- 版：`2026-w47-nl-en`，VOL.4；对象 build 11；日期 2026-11-11
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，freeze 日志所印）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-nl-en1/`
- 原始日志：`gates-run.log`、`p8-compare.log`、`occlusion-core.log`、`freeze-baseline.log`、`freeze-diff.log`、`freeze-diff-strict.log`、`p8-width-delivered.log`、`p8-width-rerender.log`、`rerender.log`、`pdftoppm.log`、`print.txt`、`web.txt`、`gates-en.json`

## 0. 开工探针与身份核验

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0
- scratch 内真实写文件成功（`tmp/probe.txt`）
- SHA 实测（`sha256sum` + 字节数）：
  - 印刷 PDF `De-Lucerna-VOL4-nl-en.pdf`：12,665,893 B / `79fa049b318d94f15f28fe23daefd2513221a77fde6511c694aee109bacf3239` —— 与任务登记逐字节一致
  - 网页 PDF `De-Lucerna-VOL4-nl-en-web.pdf`：1,610,562 B / `d493e11f3c27c7e46e0412c79f1b9208bfe804e39eac2e2203a033fad2818538` —— 逐字节一致
  - text.md `2026-w47-nl-en.text.md`：45,115 B / `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978` —— 逐字节一致
- `tables.py vol 2026-W47` = 4

## 1. gates.py 9/9（`gates-run.log`，RC=0，OVERALL: ALL PASS）

| 门 | 结果 |
|---|---|
| occlusion | PASS rc=0 flags=0 |
| p8_extract | PASS rc=0 noted=150/150 |
| p8_compare | PASS rc=0 verdict=CLEAN（gates.py 的 keydiff 正则未命中行，见 §3 单独全量输出：keydiff=[137, 138]） |
| freeze_sha256（scratch 内重建 run.py，8 SVG sha256 直比） | PASS run rc=0 match=8/8 |
| print_web_text | PASS pages 8/8 posdiff=0 msdiff=0；逐页 token：P1 790/790、P2 828/828、P3 738/738、P4 735/735、P5 807/807、P6 748/748、P7 915/915、P8 2323/2323 |
| pdftotext_nonempty | PASS print=45,438 B web=45,438 B web_size=1,610,562 |
| p8_fontsize | PASS answer-zone min=10.12pt median=10.12pt spans=187（≥ 9.75pt） |
| p8_chips | PASS core={A2:8, B1:24, B2:3} edition={A2:8, B1:24, B2:3} |
| s11_svg | PASS off-palette={} gold/old=False stroked_rects=0 VOL.5=5 (core 5) paper_fills=8 |

## 2. freeze.py（`freeze-baseline.log` / `freeze-diff.log` / `freeze-diff-strict.log`）

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg core-nl/svg --out <scratch>/freeze-baseline`：RC=0，**8/8 SVGs byte-identical**（repointed files: none）；core integrity：shipped core SVGs 复核无变化（8 文件重哈希）。
- `freeze.py diff --core-svg core-nl/svg --edition-svg <edition>/svg`：RC=0。逐页：p1 +25/−48、p2 +42/−36、p3 +30/−27、p4 +29/−26、p5 +41/−43、p6 +36/−30、p7 +47/−44、p8 +182/−677（P8 增减大是中→英讲解层 churn，集合本身 CLEAN，见 §3）；新增 CJK 15，全为 U+3000（p1 +1、p2–p8 各 +2）。
- `freeze.py diff --strict-cjk`：**RC=1，已裁定误报**（与 build 10 同案）：新增 CJK 15 个全为 U+3000；独立 census：全版可见文本 CJK 字符仅 U+3000，零汉字、零 CJK 标点；U+3000 为 SOP §1.1 强制分隔符；strict 规则限定 zh/ja 版，本版为 en 读者版，不适用。

## 3. p8.py（`p8-compare.log`；extract 见 gates §1）

- `p8.py extract --p8 svg/p8-toets.svg --total 150`：150/150，rc=0
- `p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`：rc=0
  - core 150 noted / edition 150 noted
  - `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`
  - keydiff 137/138 裁定合法：翻译题按读者语重定向（137/138 荷→英为英文键；139/140 英→荷为荷兰语键），工具说明 "key diffs are informational"，与 build 10 相同。

## 4. occlusion_audit.py（`occlusion-core.log`；plain 见 gates §1）

- `occlusion_audit.py svg/`：0 flags，rc=0（自检阳性对照 6 类全过）
- `occlusion_audit.py svg/ --core core-nl/svg/`：**0 flags；core: 0 flags; NEW vs core: 0**，rc=0
- 自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`

## 5. D12 回归（`p8-width-delivered.log` / `p8-width-rerender.log` / `rerender.log`）

- 源码 `content8.py:85`：`groepswinst = group win c`、`gedicht = poem a`（带空格）；text.md 第 419/421 行带空格；SVG 两行带空格；网页 PDF 文字层两行带空格。
- `=` 缺空格全版重扫（`sweep_eq.py`：content*.py AST 字面量 + SVG text 节点 + text.md）：**0 处**；` = ` 有空格 127 处（修前 121，+6 = 2 处 × 3 源）。
- P8 卡片度量（栏 [1439.5, 1862.0]，宽 422.5px；基线均匀 29.66px，无换行）：
  - 交付卡片 `cards/p8-toets.png`：141 adv 238.5 / 墨 [1441,1675] / 余 +187.0px；**142 adv 215.5 / 墨 [1441,1652] / 余 +210.0px**；143 adv 152.4 / 墨 [1441,1588] / 余 +274.0px；**144 adv 158.6 / 墨 [1441,1595] / 余 +267.0px**；145 adv 142.0 / 墨 [1441,1579] / 余 +283.0px
  - 独立重渲卡片（cairosvg 1950×2700，本 scratch）：与交付卡片 **SHA-256 逐字节相同**（`81a304dc244708b6d24a235e5f739d4ccbd11d9026d00e7cb1465474885b8fbe`），度量逐项相同
  - 交付印刷 PDF P8 页像素复核（`pdftoppm -r 100`，1 单位 = 1.0417 px）：142 墨右缘 1655.0 单位（卡片 1652，+3px，在 ±5px 系统性差内），余量约 207 单位；144 墨右缘 1597.4 单位（卡片 1595，+2px），余量约 265 单位。结论不变：两行单行、在栏内、无溢出。
- 配对键 141–144 = b/c/d/a，正确。

## 6. 印/网文字层与文本核查

- `pdftotext` 印=网=45,438 B，逐字节相同（`print.txt` == `web.txt`）；网页 PDF 1,610,562 B < 7 MB。
- 印刷文字层：CJK 字符 0；W47 出现 0；SOP/cover/lint/TODO/placeholder 0；"NAVO" 仅为 `VANAVOND IN BERLIJN!` 横幅内子串（假阳性）。
- text.md：题号 1–150 连续无缺；级别标记 A2 43/B1 73/B2 28（+ D 组共用 A2、F 组共用 B2 → 46/73/31）；弯引号 U+2018/U+2019/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033 均为 0；CJK 字符仅 U+3000 与全角括号 （）；范文 81 词（不计独立短横为 80 词）；头条去空白 38 字符 ≤ 56；VOL.4 标题行 ×1、VOL.5 文中 ×5。
- ABSTRACT.txt：271 B 单行，无 ASCII 双引号。

## 7. 结论

全部机械门通过；唯一 RC=1（freeze diff `--strict-cjk`）为已裁定的 U+3000 误报，与 build 10 同案。D12 回归三源 + 双重卡片度量 + 交付 PDF 像素复核全部通过。**零缺陷，可以定稿（结论 (a)）。**
