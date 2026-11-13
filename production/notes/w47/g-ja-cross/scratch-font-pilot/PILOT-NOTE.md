# W47 字体试点 PILOT-NOTE — svglib 讲解层 sans 分支改 Newsreader/Noto Sans

**试点版**：`2026-w47-pt-fr`（葡目标 × 法读者；调查里实测 503 个拉丁字符落在 CJK Sans 的那版）
**时间**：2026-11-11 12:00–12:30 UTC · **只试点，不批量；不动 repo 生产文件、不 commit、不 push**
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-font-pilot/`
（以下路径均为该目录内相对路径；repo 指 `~/workspace/weekly-git`，只读）

## 0. 探针与方法

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧真实写文件通；TMPDIR = 本目录 `tmp/`（/tmp 只有 512M 且常满）。
- 构建一律 `tools/venv/bin/python`（Pillow 13.0.0 / 内置 FreeType 2.14.3，正典栈；不用系统 python3——调查 Q1 已证实双栈量测漂移）。
- 基线：把生产版目录完整复制为 `baseline/`，venv 重跑 `run.py`，8/8 SVG 与交付字节一致（`delivered-svg.sha256` = `baseline-rebuilt.sha256`），基线干净。
- 补丁版：`baseline/` 再复制为 `patched/`，只改 `patched/svglib.py`，venv 重建，全部对照均以 `baseline/`（= 交付）为修前基线。

## 1. 补丁（确切内容）

**只改一个文件**：版目录 `svglib.py`（正典模板在 `core-en/svglib.py`，pt-fr 的是 fan-out 复制件）。完整 unified diff 见 **`svglib-sans-font-patch.diff`**（由 `apply_patch.py` 生成，逐项断言唯一匹配后才写入；`diff` 共 +25/−3 行）。

| 位置（补丁后行号） | 改法 |
|---|---|
| L9 | `NOTO_DIR = "/usr/share/fonts/truetype/noto"`（core-ru 同款路径） |
| L31–32 | `_SANS_NOTO/_SANS_NOTO_B` = `NotoSans-Regular.ttf` / `-Bold.ttf`（core-ru 已在用的同一文件） |
| L38–41 注释 | sans 顺序改写为 Newsreader（拉丁）→ Noto Sans（西里尔）→ Noto Sans CJK SC（CJK）→ DejaVu |
| L54 `_CMAP` | 加 `"sans_noto" / "sans_noto_b"` 两个 cmap |
| L57 | `_CYR = range(0x0400, 0x0530)`（core-ru 原样） |
| L60 `_FAMILY` | 加 `"sans_noto": "Noto Sans"` |
| L66–67 `_PATH` | 加 `("sans", bold, "news") → _NEWS/_NEWS_B` 与 `("sans", bold, "sans_noto") → _SANS_NOTO/_SANS_NOTO_B`（没有这两行 `_pil` 会 KeyError） |
| **L84–95 `_char_font` 的 sans 分支（唯一行为改动）** | 在原 `sans` 判定之前加两条优先规则：① `cp in _CMAP["news_b" if bold else "news"]` → `"news"`（拉丁字母/数字/常用标点走已加载的 Newsreader Regular 400 / SemiBold 600）；② `cp in _CYR 且在 sans_noto cmap` → `"sans_noto"`；其余保持现有 CJK 路径，最后 `deja` 不变。serif 分支一行未动。 |

设计说明（与调查 §Q2.5 一致，另有两点要登记）：
- 两条规则都是**按字符所属文字**、不是按读者语——与 serif 分支（全版拉丁 → Newsreader，与读者无关）和 core-ru 的 `_CYR` 分支同一手法。pt-fr 是法读者，本次只行使规则①；规则②在 pt-fr 里**完全未被触发**（全版 0 个西里尔字符，grep 8/8 页皆 0），sans_noto 路径未经试点检验——ru 读者版批量前须另做一版试点。
- 空格 U+0020 在 Newsreader cmap 里，所以 sans 空格现在判为 Latin，与 serif 分支早已做的分类一致（D1 fix 注释里写明的同一行为）；`Page.text` 的前导空格分拆逻辑不受影响，`run.py` 全程 0 溢出、0 报错。
- 字重缺口沿用调查结论：Newsreader 只有 400/600，SOP 500/700 只能近似（serif 的 bold 今天已是 600 代 700）；Noto Sans 则有真 500/700。

## 2. 门禁结果（patched 全套，修前基线对照）

| 门禁 | 基线（修前） | 补丁版 | 结论 |
|---|---|---|---|
| `run.py`（venv） | RC=0，REG 150（A2 48/B1 71/B2 31） | RC=0，REG 150，0 溢出 | 通过 |
| `gates.py` | **16/16** | **16/16** | 通过。唯二数值变化：P1 副标线 y=372 宽 797.8→**667.3**（窄了 16%，未超 1820）；页框最小边距 L/R/T/B [43.7, 30.5, 35.0, 32.0]→[43.7, **10.3**, 36.0, 32.0]（R 边只剩 10.3px，见缺陷 #3）；P7 末引文基线 2380.17 不变 |
| `render.py`（cards PNG + 印 PDF） | — | RC=0，印 PDF 12,422,672 B / 8 页（交付 12,934,799 B，−512KB：嵌的 CJK 字形少了） | 通过 |
| `tools/webpdf.py` | — | RC=0，网 PDF 1,060,110 B / 8 页 / 1462.5×2025pt（交付 1,104,302 B）；`pdffonts`：CJK SC 子集对象 14→**4**，其余为 Newsreader/UnifrakturMaguntia/Serif CJK；**无** Noto Sans（非 CJK）——正确，本版无西里尔 | 通过 |
| `tools/occlusion_audit.py` | **0 flags** | **1 flag** `[TEXTX] p2-vida.svg '26. a folga' — ink overlaps 'COMPLETE COM OS NÚMEROS' by 9.5x15.8px` | **不通过——新缺陷，见 §4 缺陷 #1** |
| `tools/p8.py extract --total 150` | —（KIT：150/150） | **150/150** | 通过 |
| `tools/p8.py compare vs core-pt` | CLEAN, keydiff=[137,138] | **CLEAN, keydiff=[137,138]**（仅两条法语翻译答案，与基线一致） | 通过 |
| `tools/freeze.py baseline` | 8/8 | **0/8**（预期内：字体改动本就改写全部 8 页；不是漂移） | 见 freeze diff |
| `tools/freeze.py diff` | — | 每页 +36~+58 strings / −10~−20 strings（run 分拆所致）；**CJK core 数逐页不变**（21→21、17→17、13→13、15→15、14→14、16→16、13→13、15→15）；**added CJK chars: 0** | 只含字体/坐标变化，无内容字符增减 |
| 印/网文字层一致 | KIT：word-multiset diff 0（8,632 词） | 印 8,701 词 vs 网 8,701 词；仅差 2 个 `<`（P8 答案 58/59 "16:30 < 17:00"、"2 jours < 7 jours" 在网 PDF 里抽成 `>`）；**去空白后字符流完全相同、长度同为 35,806**；且 patched 网 PDF vs **交付网 PDF 去空白后字符流完全相同**。`<`→`>` 是交付件就有的 webpdf 文字层旧 quirk（交付网 PDF 里同样是 `>`），与本次补丁无关；8,701 vs 交付抽取的 8,051 只是 pypdf 分词碎片化（run 变多了），字符流证明内容零变化 | 通过 |

## 3. 量化回答（A 档可行性的三个关键问题）

### (a) 多少元素换字体、多少行重排

- **换字体元素**：Noto Sans CJK SC 元素 644 → **124**（−520，−81%）；Newsreader 元素 947 → 1717（+770，+81%）；全部 `<text>` 元素 1619 → **1869**（+250，+15%——同一字符串按字体分 run，run 变多了）。
- **换字体字符**：Newsreader 字符 32,424 → **42,768**（**+10,344**）；CJK SC 字符 10,468 → **125**（−10,343）。剩余 125 个 CJK SC 字符的构成：U+3000 119 个（家具分隔符，无拉丁写法，正确保留）+ `→` 4 个 + `｜` 1 个 + `✓` 1 个（符号，不在 Newsreader cmap，落 CJK 是正确行为）。Serif CJK 27 字符、UnifrakturMaguntia 9 字符零变化（补丁未碰 serif）。
- **行重排**（行字符串多重集对称差，逐行对位会虚增——P5 下游 73 行只因少了 1 行整体上移，字符串本身没变）：全版 1043 行 → **1042 行**；去行 30 条 / 增行 29 条，即 **≈29 行重断行（2.8%）**，净 −1 行。分行：P1 4、P2 5、P3 7、P4 4、P5 5→4、P6 5、**P7 0、P8 0**。重排全在词汇表（gloss）段落与练习说明句（常规 sans），无一处是正文。
- **元素位移**：可配对元素中 156 个 x/y 移动 >0.5px；除 P1 的两个配对假象外（见下），其余各页 max|dx| ≤ 2.1px、max|dy| = 0——即**只在行内左右微移，无上下流动**。P1 的 max|dy|=40 是配对假象："A2→B1" 一行在补丁后拆成 "A2"+"→"+"B1" 三个 run，配对器把新 run 的 "B1" 错配到下一枚徽章；逐枚核对后 P1 全部徽章 y 与基线逐一相同。

### (b) 盒/页顶穿清单（P8 答案流最紧处在内）

**有。共 6 处，同一缺陷类**（见 §4 逐条位置与量）。gates 的页框检查 0 穿（最紧 R 边 10.3px）、同基线碰撞 0——**gates 抓不到这 6 处中的 5 处**，occlusion 只抓到 1 处；本次是用自写的 creambox 差分审计（`analyze.py`：#f0eee5 矩形内锚定文字的墨水盒 + 修前修后逐行对照）扫出来的。另：**无任何一处顶穿页框**，无任何文字墨水越过 40px 页边。
- P8：**零顶穿**（见 (c)）。

### (c) 讲解段落是否普遍变长、P8 是否装得下

**讲解段落没有普遍变长——是两极分化**。对 408 条去重 sans 字符串逐条 `text_w`（基线 svglib vs 补丁 svglib）：
- 全体：中位比 **1.040**、均值 1.032；变长 267 条 / 变短 109 条 / 不变 32 条。
- **常规（bold=False，正文讲解/词汇/说明句）：中位 0.987、均值 0.986，仅 33/151 变长**——常规段落中位变窄 1.4%。最窄：`· nota · pesar` 0.802、`prazo · dia útil · coerência · chute` 0.866（`·` 在 CJK 里宽、在 Newsreader 里窄）。
- **粗体（bold=True，标题/栏目头/徽章/框头）：中位 1.057、均值 1.059，234/257 变长**——粗体变宽是系统性的。大写标题最甚：`A2` +18.4%（23.4→27.7px @19pt）、`A PALAVRA DA SEMANA` +16.9%、`PALAVRAS DA MEMÓRIA` +16.8%、`A SEMANA, DIA A DIA` +15.9%、`O CAMINHO ATÉ O GABARITO` +14.8%。
- 所以段落行数不增反减（P5 词汇表 5 行→4 行，全版净 −1 行）；**风险集中在粗体标题**，不在段落长度。
- **P8 装得下，余量与修前逐像素相同**：P8 行数 245→245、重断行 0、末基线 2545.6 两版相同、最大墨水底 2548.6 两版相同；距页脚线（y=2596）**47.4px**、距页底（2700）**151.4px**——与修前分毫不差。P7 亦 0 重排。

## 4. 缺陷清单（全部已目检/像素验证； pilot 不修，只量）

| # | 位置 | 量 | 性质与证据 |
|---|---|---|---|
| 1 | **P2** 练习 C 组标题 `C　COMPLETE COM OS NÚMEROS`（y=2018.0，第 3 列）vs 练习 `26. a folga`（y=2005，第 4 列）| 标题总宽 409→**459.7px（+50.7，+12.4%）**；墨水 (1032.7,1995.0)–(1448.7,2019.0) 与 `26. a folga` (1439.5,1986.0)–(1552.5,2011.0) 交叠 **9.2px 横 × 16px 纵**（occlusion 报 9.5×15.8，PIL 取整差） | **真碰撞**。渲染裁图目检：末尾 `S` 贴上 `26.` 的 `2`（`crops/crop-p2-textx.png` vs `crop-p2-textx-base.png`，基线有 41.5px 空隙）。成因：全大写粗体标题在 Newsreader SemiBold 里比 CJK 宽 12%+，撞进右列 |
| 2 | **P1** 数字框标题 `A SEMANA EM NÚMEROS　En chiffres`（y=823.18，框 x 989–1411.5）| 越自家框右沿 12.5→**57.5px**；尾部越 x=1439.5 的部分（`res`，29.5px）**被第 4 列奶油框（rect 在 SVG 文档中后于标题，idx 18716 > 13509）盖掉** | **最重的一处**：词被截成目视 `En chiff`。像素验证：补丁卡 (1450,815)/(1455,815)/(1465,815) 皆为纯奶油色 #f0eee5（240,238,229），孤立渲染对照证明该处本应有 `e/s` 墨水；基线 (1420,815) 有墨、补丁同点为空白 |
| 3 | **P1** `EM POUCAS PALAVRAS　EN BREF`（y=1914.0，框 3 x 1439.5–1862）| 法语尾 `EN BREF` 墨水右至 **1899.4**，越框/内容沿 **37.4px**，距页框（1910）仅 **10.6px** | 新增越框，可见、无碰撞（gates R 边最小值即此 Element）。基线右至 1850.5（框内余 11.5px） |
| 4 | **P1** `NESTA EDIÇÃO　Dans ce numéro`（y=1278.35，框 2 x 1439.5–1862）| 越框 **5.1px**（墨水至 1867.1） | 新增、小：基线右至 1844.5（框内余 17.5px） |
| 5 | **P2** `PARA NÃO ERRAR　La règle à retenir`（y=642.02，框 x 538.5–961.0）| 越框 4.5→**30.5px**，墨水至 x=991（进第 3 列边距 2px） | 扩大、无碰撞（像素验证：补丁卡该行墨水至 991，基线至 967） |
| 6 | **P7** `ERROS COMUNS　Erreurs fréquentes`（y=242.0，框 x 1439.5–1862）| 越框 17.5→**37.7px**，墨水至 1899.7，框内仍有余地到页框 | 扩大、无碰撞 |

**统一成因**：6 处全是 `葡语头　法语副标` 的框标题单行——葡语头（粗体大写）在 Newsreader SemiBold 里变宽，把行尾的法语副标推出框外。3 处是修前已 marginal 的旧患被放大（#2、#5、#6），2 处新增（#3、#4），1 处成碰撞（#1）。批量时须**逐标题**修（缩法语副标 / 降标题字号 / 拓宽框），无法只靠全局参数一次解决。

## 5. A 档批量风险判断

**可行，但不是 drop-in。** 机制补丁本身干净（一个函数、零新依赖、全部字体文件已在机上），pt-fr 一版的门禁除 1 处 TEXTX 外全绿、P8 余量分毫不差；但**每拉丁读者版预计带 ~6 处同类框标题问题**（pt-fr 实测 6 处；该标题模式全版通用，调查 §Q2.3 的 8 族同构），78 版 ≈ 数百处须逐处修 + 重建 + 重门禁 + 按 SOP §8.4 重校。调查原估的每版 1.5–2 agent-小时偏紧——标题修补循环未计入；拉丁/ru 读者版按 **2–3 小时/版**更现实。另：

1. **批量前置**：fan-out 变体安装须先收敛（调查 §Q2.5：fr/en/de 脚本无变体段，it 才有；补丁的落盘方式——改 core 模板还是改 fan-out 脚本——须协调员定，否则各族行为再分叉）。本次补丁改的是**已 fan-out 的版内 svglib**，未碰 core 模板。
2. **须另做 ru 读者试点**：sans_noto 路径本次 0 次触发，未验证（字体文件存在、core-ru 有先例，但本补丁里的接线未跑过）。
3. **中日韩读者版是待定项**：本补丁的拉丁规则是按字符文字、无读者门——用在中日韩读者版上也会把其 sans 层里的拉丁片段（标签、数字、`A2` 徽章等）改成 Newsreader。这与 serif 分支既有行为一致，但调查原文写的是「中日韩读者：不动」。A 档开工前须定：保持脚本式（简单、与 serif 一致）还是加 `_READER_LANG` 门由 `build_edition.py` 改写。pt-fr 的数字不受此选择影响。
4. **门禁须加 creambox 审计**：gates 16/16 全绿仍漏 5/6 处、occlusion 漏 5/6——框标题越框须有自己的机械门（`analyze.py` 里的差分审计可直接收敛进工具，#f0eee5 矩形 + 修前对照）。
5. **ja/ko 不在试点内**（任务书注记）：core-ja/core-ko 是旧式单字体 svglib、无 `_char_font` 拆分，调查已注须换代，工作量另计，不在 A 档 78 版的"一版一补丁"口径内。
6. 解释器已定：venv 唯一正典（本次基线 8/8 字节一致即是用 venv 重建的；系统 python3 不准用）。

## 6. 证据文件（本目录内）

- `PILOT-NOTE.md`（本文件）、`svglib-sans-font-patch.diff`（补丁）、`apply_patch.py`（补丁生成器，可重复执行验证）
- `baseline/`（修前重建，SVG = 交付字节）、`patched/`（补丁后重建，含 cards PNG + 印/网 PDF）
- `analysis.json` + `analyze.py` + `analysis.log`（全部差分数字：元素/行/进距比/creambox/P8 余量）
- `delivered-svg.sha256`、`baseline-rebuilt.sha256`、`patched-svg.sha256`
- 日志：`baseline-run.log`、`baseline-gates.log`、`baseline-occlusion.log`、`patched-run.log`、`patched-gates.log`、`patched-render.log`、`patched-webpdf.log`、`patched-occlusion.log` / `.json`、`patched-p8-extract.log`、`patched-p8-compare.log`、`freeze-patched.log`、`freeze-diff.log`、`freeze-patched/`（freeze baseline 产物）
- `crops/`：缺陷目检裁图（P2 TEXTX 修前/修后、P1 En chiffres 修前/修后+宽裁、P1 EN BREF、P1 Dans ce numéro；另 `p1-base-full.png` / `p2-base-full.png` 供像素复核）
- 备注：repo 内 `git status` 的 450 条改动（含 `?? production/2026-w47/2026-w47-pt-fr/`）是其他并行工作的未提交 W47 在制品（pt-fr 文件 mtime 均为 2026-11-11 03:09–03:15 UTC，早于本试点开工）；本试点对 repo 只读，唯一写入是任务书要求的 `hash-object -w` 探针 blob。未动任何已建成的版、未 commit、未 push。
