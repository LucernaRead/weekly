# W47 es-nl proof2 — 独立复校记录（重建版）

- 版：`production/2026-w47/2026-w47-es-nl/`（西语核心 × 荷兰语读者版，es 全族重建版）
- 日期：2026-11-11；复校员：独立 proof2（与构建者 / fan-out agent 不同人）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-nl2/`（下称 **S**）
- 构建/复核一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 全程 goals 侧 scratch/tmp，未写 /tmp
- **未改任何生产文件、未 commit、未 push**（唯一例外见 §1 web PDF 说明：门禁第 1 步 render.py 按构建者门禁驱动重渲染，印 PDF 字节不变；网 PDF 内容不变但字节变，见 §1.3）

## 结论：(a) — 零缺陷，通过

缺陷清单：**零**。观察项 3 条（§8，均非缺陷，不影响结论）。

## 1. 身份核对（三件 SHA，复核前后各测一次）

| 产物 | 复核前（12:50） | 复核后（13:1x） | 任务给定值 |
|---|---|---|---|
| 印 `La-Lucerna-VOL4-es-nl.pdf` | 3,502,134 B `d5e63a7f…60db68c` | 相同 ✓ | 一致 ✓ |
| 网 `La-Lucerna-VOL4-es-nl-web.pdf` | 887,959 B `54fbf35e…f6a763` | **887,963 B `02873212…6f62b8`** | 见 §1.3 |
| text.md `2026-w47-es-nl.text.md` | 45,284 B `d8d8e007…44b91e`，1,835 行 | 相同 ✓ | 一致 ✓ |

核心 core-es 三件（复核前后各测一次，未变）：印 17,212,955 B `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`；
网 1,410,471 B `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`；
text.md 1,822 行 `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`。与 FANOUT-REPORT §0 一致。

### 1.3 网 PDF 字节变化说明（非版面缺陷，工具链属性）

- 复核前我本人实测网 PDF = 887,959 B / `54fbf35e…`，与任务给定值一致；随后门禁重渲染（render.py → tools/webpdf.py）写出 887,963 B / `02873212…`。
- **内容不变**：印/网文字层逐字节一致（pdftotext -layout，109,833 B，见 §2）；印 PDF 两次渲染字节完全相同（3,502,134 B），证明 SVG 输入稳定。
- **决定性试验**：同一批 SVG 再跑 webpdf.py 到 S 内，得到第三个结果 887,962 B / `005712c0…`。三次运行三个字节数（887959 / 887963 / 887962）。
- 字节差定位：首个差异在内嵌字体子集流（`/FontFile2 … /Length 1976` vs `1977`，Flate 流）；PDF 内无 CreationDate / ModDate / ID。结论：**webpdf.py 字节级不可复现**（字体子集化逐次微差），网 PDF SHA 只能以落盘时刻为准。
- **提请协调员注意**：盘上网 PDF 现为我重渲染的副本（内容与构建者版完全一致，文字层逐字节相同）；入仓时请按 AGENTS.md 从最终网 PDF 重量 pdfBytes / pdfSha256，勿沿用旧 SHA `54fbf35e…`。

## 2. 门禁汇总（独立重跑，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| render（render.py） | rc=0；印 PDF 字节复现 `d5e63a7f…` |
| freeze baseline | **8/8**，core 8 文件重算无变（我方 `nl-freeze.log`） |
| freeze diff / CJK 分类 | added 362 串；新增 CJK **仅 U+3000 ×75**，其余 0（§3） |
| occlusion audit | 0 flags（自检 6 类全触发） |
| p8 extract | **150/150** |
| p8 compare | **CLEAN，keydiff [137, 138]**（已裁决项，见 §4） |
| keycheck（REG vs 抽取） | **149/150**，唯一 mismatch #150 `✓`（已知例外） |
| sweep（box-vs-hline / bridge） | 0 / 20 bridges / 0 orphans / 0 widows |
| boxtitle 真墨 | **0 溢出**；最紧 P1 `EN ESTA EDICIÓN　In dit nummer` +6.0 |
| creambox（canonical + 13 行，两版一致） | 原始扫描 6 条负值，**真墨复核全部为窗外假阳性，0 真溢出**（§5） |
| print = web 文字层 | 逐字节一致，109,833 B |
| P8 最小有效字号 | 10.125 pt，< 9.75pt 计 0 |
| creambox 驱动初值 | 见注：gates.py 首次写 `creambox_rc=2` 为我方 harness 路径错（S 内缺 `creambox.py`，文件名为 `creambox13.py`），**非门禁失败**；已用 canonical + 13 行两版补跑，rc=0（GATE-LOG §注） |

## 3. freeze 首检 8/8；新增 CJK 分类

- 我方 freeze-diff（`nl-freeze-diff.json`）：8 页 added_strings 362，removed 553（core 中文串移除，预期内）；added 串中 CJK 字符 **只有 U+3000（表意空格，分隔符）×75**，非 U+3000 的 CJK **0**。
- text.md 全文：CJK 字符 98 个，**全部为 U+3000**，其余 0。

## 4. 150 题逐题手验（三源交叉，PASS）

脚本 `S/p8_xcheck.py`：(1) 版 P8 keys（我方 p8-extract.json）／(2) text.md 答案区（逐项 key + note 首段）／(3) 核心 P8 keys（我方 core-p8-extract.json）；REG（key+note）由 run.py 进程内读取。

- **VERDICT: PASS 150/150**（`nl-p8-xcheck.log`）。
- [1] REG vs 版抽取：唯一 mismatch #150（REG 长键 vs 抽取 `✓`，已知例外）。
- [2] text.md 答案区：0 问题（150/150 key + note 均在答案区找到；行布局交错导致的初版误报已修解析器并复核）。
- [3] 版 vs 核心：keydiff 仅 **[137, 138]**——E 组中文句答案键译成荷兰语（`137. Maandag is het Internationale Flamencodag. — Vgl. origineel.`／`138. Zaterdag kijken we naar de derby van Sevilla. — Vgl. origineel.`），属已裁决项，不判 (b)。
- 逐题内容已与题干逐一核对（150 条答案的事实与键全对）：P1 测验 1–10、P2 11–28、P3 29–46、P4 47–64、P5 65–82、P6 83–100、P7 101–112、P8 113–150；其中 Q89 B（10 日前仅 laSexta 辩论已确认）、Q87 B（45−30=15）、195 分钟总和（45+45+30+30+15+3×10）、Q60–64 过去时、E 组 137–140 翻译均核实无误。
- MODELO 例文：源串（content8.py:103）实测 **97 词**，与 “97 woorden” 一致；H 题要求 80–100 词，97 在内。
- text.md 全文通读 1,835 行：`hasta el jueves` ×7、`antes del jueves` ×0、`sábado veo el derbi` ×1；无他语导读残留、无内部结构语义；练习小节头（A　理解 等）均为源语言西语（冻结）。

## 5. 奶油盒真墨裁决（6 条负值，全为假阳性）

canonical creambox 与 13 行版结果逐字节一致；creambox_diag 真墨复核（`nl-creambox-diag.log`）：

| # | 盒 | 真墨 clearance | 窗外行判定 |
|---|---|---|---|
| 1 | P1 y=1288 底 1677.2 | OWN 末行 +40.4 | `AHORA TÚ　Nu jij`（+37，下方小节头） |
| 2 | P1 y=588 CINCO CLAVES 底 1308.0 | OWN 末行 `Vijf sleutels — geen verzonnen cijfers.` **+3.2** | `EN ESTA EDICIÓN`（下一盒标题，owner y=1312） |
| 3 | P1 y=1312 底 1652.0 | OWN 末行 `Pág. 8` +10.8 | `LA PALABRA DE LA SEMANA`（+24，下方头） |
| 4 | P1 y=1874 图注盒 底 2194.0 | OWN（无文） | 图注文本在盒下（设计如此） |
| 5 | P2 y=200 底 1188.6 | OWN 末行 +41.3 | `DECIR LA HORA`（+37，下方头） |
| 6 | P3 y=200 底 375.4 | OWN 末行 +47.5 | `LO QUE QUEDA DE NOVIEMBRE`（+37，下方头） |

自有末行墨 clearance 全部 ≥ 0。另两处最紧（观察 O2，§8）：P2 ¿SABÍAS QUE? 盒 +0.1、P5 VOTAR 盒 +0.1——与 core 同盒同末行同值，非回归。

## 6. 必查项 D3–D6（独立实测，非采信 builder 数值）

| 项 | 独立实测（PIL 真墨，`nl-d-measure.log`） | 裁定 |
|---|---|---|
| **D3** P5 ¿Y TÚ? 盒（content56.py:50 eh `+29` 已核源） | 盒 y=1277.5 底 **1583.5**，末行基线 1572.6（fs 19.0），墨底 1577.13，**真墨 clearance +6.42px**；裁图核实末行在盒内 | ✓ 与 builder +6.4 一致，通过 |
| **D4** `EL PLAN DE LA SEMANA　Weekplan`（content56.py:22 已核源） | boxtitle title_w 397.2，右缘 953.7，**clear +7.3**（原 +36.8 溢出）；裁图核实标题在盒内 | ✓ 通过 |
| **D5** `ERRORES TÍPICOS　Fouten`（content7.py:83 已核源） | boxtitle **clear +94.3**；盒自有末行真墨 clearance +37.5；裁图核实 | ✓ 通过 |
| **D6** 横幅（content7.py:134 `…+105+1` 已核源） | 横幅 rect (88.0, **2464.5**, 1774.0, 118.0) **= core exactly**，底缘 2582.5 = core；页脚基线 2624.0，页脚墨顶 **2611.25**，间隙 **28.75px**（builder 称 28.5，差 0.25 为 PIL 舍入）；裁图核实横幅与页脚无触碰 | ✓ 通过 |
| P7 col3 CARTAS 盒 1873.51 | 盒底 1873.5，末行基线 1864.1，墨底 1864.31，**真墨 clearance +9.20**；裁图核实 | ✓ 通过（+9.2 在内，无溢出） |
| P1 C1 CINCO CLAVES 盒（720） | 盒底 1308.0，末行墨底 1304.75，**真墨 clearance +3.25** | ✓ 通过 |

## 7. P8 答案注 5 条缩回 1 行（§3.3 C 复测）

- 5 条注（#3、#9、#22、#65、#123，皆为 `Stemmen per post: uiterlijk op de 19e aanvragen`）在 SVG 答案区逐列实测**各 1 行**（#3 y=1483.7、#9 y=1661.7、#22 y=2079.5、#65 y=2257.5、#123 y=1673.1，下一行即下一题），裁图核实。
- **P8-keys 终 y = 2506**（bottom 2560，keycheck log `flow[P8-keys] ended col 3/3 y=2506`），**0 OVERFLOW**（构建输出无溢出警告）。
- 其余多行答案为先前已有的长注，与本重建无关：#1（`…om middernacht`，2 行）、#44（`…het werkwoord als tweede`，2 行）、#139（`…pedir hasta el jueves 19.`，2 行）——终 y 2506 证明版面已容纳；check_p8keys.py 的跨列合并会把 #36/#84/#141 也算成多行，系合并假象（逐列实测三者皆 1 行）。
- P8 末行 #150 `✓ Zie de voorbeeldtekst in deel H op deze pagina (97 woorden)` 基线 2489.6，距页脚线 70px 以上。

## 8. 观察项（非缺陷，不影响结论）

- **O1 — D5 字体（全周级已知待定项，只记录，不判 (b)）**：拉丁讲解层落在 Noto Sans CJK SC。实测段数（`<text>` 元素计）：**本版 396 段**（P1 46、P2 50、P3 53、P4 49、P5 50、P6 39、P7 52、P8 57）；core-es 同口径 218 段。增量即荷兰语讲解层。附带一例：P6 页眉 `programma's` 中 U+2019 在该字体下 advance 为满 em（18pt 字号下 18.0，Newsreader 同字号 4.6），渲染为可见间距 `programma' s`（全版唯一一处 U+2019，源串正确无空格，文字完整可读、无裁切、无重叠）。此为该已知字体项的直接后果，记入该项，不另判缺陷。
- **O2 — 两处 +0.1px 真墨 clearance**：P2 ¿SABÍAS QUE? 盒（末行 `ley.`，墨底 543.4 / 盒底 543.5）与 P5 VOTAR 盒（末行 `compara precios antes de pagar.`，墨底 1251.4 / 盒底 1251.5）。逐项与 core 对照：**core 同盒、同末行（冻结西语句）、同为 +0.1**，非荷兰语回归；裁图核实墨在盒内、未触下一盒。观察，不判缺陷。
- **O3 — 网 PDF 字节不可复现**：见 §1.3。入仓时须从最终网 PDF 重量 SHA。

## 9. “next Sunday” 指针核对

- 全盘 grep：**core-es 与 es-nl 内 “Sunday” 0 命中**，本版无该串，无可裁决之处。
- 任务所引行号（content12.py:37/:113、content34.py:127）实际指向 **core-zh-tw**（该核心 gloss 句：`The Wei Chuan Dragons' championship parade is set for next Sunday (Nov 22)…`，正在 content12.py:37 与 content34.py:127）；指针核心名有误，行号本身在彼核心无误。已裁决规则（冻结核心英文不是缺陷）在本版不触发。

## 10. 8 页逐页渲染目视

印 PDF（`visual/pg-*.png`，60 dpi 全页 + 150 dpi 裁图 16 张）逐页目视：P1–P8 均无重叠、无裁切、无墨出盒、无页脚触碰； tight 点全部裁图核实（§5–§7 所列）。图片均为明确 public-domain（Sargent 舞女、青铜投票箱、 medieval 写本、鹅毛笔），图注完整。

## 11. 交付物（S 内）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- 门禁：`nl-gates.json`、`nl-*.log`（render/occlusion/p8-extract/p8-compare/freeze/freeze-diff/boxtitle/keycheck/sweep/minfont/creambox-canonical/creambox13/creambox-diag/p8keys-multiline）、`nl-p8-compare.json`、`nl-p8-extract.json`、`core-p8-extract.json`、`nl-freeze-diff.json`、`keycheck-150.json`、`freeze-es-nl/`、`nl-p8-xcheck.log`、`nl-d-measure.log`、`nl-font-census.log`、`web-retest.pdf` + `web-retest.log`
- 脚本：`gates.py`、`creambox_canonical.py`、`creambox13.py`、`creambox_diag.py`、`boxtitle_core.py`、`keycheck_core.py`、`minfont.py`、`check_p8keys.py`、`sweep_de.py`、`classify.py`、`d_measure.py`、`font_census.py`、`p8_xcheck.py`
- 目视：`visual/pg-{1..8}.png`、`visual/hi-{1..8}.png`、`visual/c-*.png`（16 张裁图；P6 页眉另加 `c-p6-band2.png`）
