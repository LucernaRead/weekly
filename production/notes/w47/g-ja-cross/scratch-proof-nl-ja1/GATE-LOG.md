# GATE-LOG — 2026-W47 nl-ja delta build-6 proof1（独立复校）

版：`2026-w47-nl-ja`，build 6。全部自跑；证据文件均在
`hidden_files/w47/scratch-proof-nl-ja1/` 下（`b6-*` 前缀；旧 build-5 proof 文件已另存为 `b5-PROOF-NOTE.md` / `b5-GATE-LOG.md`）。
规范路径：`production/2026-w47/2026-w47-nl-ja/`。staging 对照：
`production/2026-w47/fanout-nl/2026-w47-nl-ja/`（build-5，未动）。
解释器：`tools/venv/bin/python`（Pillow 13.0.0）。TMPDIR = 自有 scratch（`b6-rebuild/tmp`）。

## 0. 身份与生产零写入

| 项 | 实测 |
|---|---|
| 开工 SHA | 印 `f78ffe32…943b0` / 26,049,309 B；网 `b4d4501b…4762b` / 2,155,389 B；文 `060bfdea…bb93a` / 47,801 B |
| 收工 SHA | 三件与开工逐字节一致（见上表） |
| 生产快照 | 开工/收工 42 文件 SHA-256 逐项一致（`snapshot-start.txt` vs `snapshot-end.txt`，哈希排序比对 0 差异）— 零写入 |
| 探针 | `git hash-object -w /dev/null` = `e69de29b…`；scratch 真实写文件成功 |

## 1. 构建（clean-dir 重建，`b6-rebuild/edition/`）

| 门 | 结果 | 证据 |
|---|---|---|
| run.py | rc=0，TOTAL 150，by page 10/18/18/18/18/18/12/38，A2 46 / B1 73 / B2 31，0 FLOW OVERFLOW / HEAD TOO WIDE；P4 col3 ends 1229.6，P6 chart ends 691，P7 col3 ends 1927.5 | `b6-run.log` |
| SVG 重建 | clean-dir 重跑 `run.py`，8/8 字节一致（与交付 svg/ SHA 逐页比对） | `b6-shipped-svg-sha.txt` / `b6-rebuilt-svg-sha.txt` |
| text.md 重导 | `export_fanout.py <rebuild> ja` rc=0，47,801 B，SHA `060bfdea…bb93a` 与交付逐字节一致；142+2+8=150；8 金句；6 gloss；model words 81 | `b6-export.log` |
| render.py | rc=0，印 PDF 26,049,309 B，SHA `f78ffe32…943b0` 与交付逐字节一致 | `b6-render.log` |
| webpdf.py | rc=0，2,155,386 B（交付 2,155,389 B，−3 B，字体子集化非确定性；网 PDF 字节不可复现属已知），text bytes 47,924 = 交付 | `b6-webpdf.log` |

## 2. SVG 逐页 SHA 比对（staging build-5 → 本版 build-6）

| 页 | staging | 本版 | 变化 |
|---|---|---|---|
| p1-voorpagina | `b1797d8c…` | `b1797d8c…` | 一致 |
| p2-leven | `35914f59…` | `35914f59…` | 一致 |
| p3-cultuur | `2ddeb68f…` | `2ddeb68f…` | 一致（D6 结构同步） |
| p4-sport | `5ed7ac08…` | `0dd0671e…` | 变（D11） |
| p5-jongeren | `314d1983…` | `314d1983…` | 一致 |
| p6-verdieping | `80417217…` | `80417217…` | 一致（D8 结构同步） |
| p7-taal | `4608bb65…` | `4608bb65…` | 一致（D7/D10 结构同步） |
| p8-toets | `1b16e2be…` | `8aa13d85…` | 变（D9） |

## 3. 宽度自测（本版 `svglib.wrap()`，0.1px 步进；`b6-widthscan.py/.log/.json`）

| 点 | 带（同行内容） | 中点 | 选中值 | 断行 | SVG 实测 |
|---|---|---|---|---|---|
| D6 | 412.8–430.0 | 421.4 | 421.4 ✓在带内=中点 | 2 行 | y=2303.5/2333.22，逐字同 |
| D7 | 414.9–430.0 | 422.45 | 422.45 ✓ | 3 行 | y=725.66/755.39/785.11，逐字同 |
| D8 | 369.5–387.7 | 378.6 | capcn_w=378.6 ✓ | 3 行 | y=635.02/659.44/683.86，全不变 |
| D10 | 378.0–397.9 | 387.95 | dt_zh_w=387.95 ✓ | 2 行 | y=1783.77/1812.17，逐字同 |
| D11 | 事实句 wrap 3/3/3/2/3 = 14 行；sh 旧 611.0 → 新 638.0 | — | 顶留 62→89 | — | 盒底 1229.6，末基线 1209.49 |

## 4. D11 双量测（PIL 真墨 + 交付 PDF 渲染像素；`b6-d11.py/.log/.json`）

| 量测 | 值 |
|---|---|
| 盒底（SVG 实测） | 1229.6（y=591.6，h=638.0） |
| 末行基线 `18:45 uur.` | 1209.49，基线余量 **+20.11px** |
| 卡片 1× 最低文字墨行 | y=1209，余量 +20.6px（纸/奶油双底色判定） |
| 卡片 1× 盒底下 7px 条带 | 0 非纸像素（y=1230–1236；y=1228/1229 各 423 像素为盒底行奶油填色本身，像素 (244,243,235) 系分数底边混色，已订正） |
| 印 PDF 150dpi 盒底下 7px 条带 | 0 非纸像素 |
| 印 PDF 150dpi 最低文字墨行 | svg-y 1209.53，余量 +20.07px |
| 习题线 y=1608 间隔 | 378.40px |

## 5. 门禁套件（`b6-gates_delta.py`，9 项，ALL PASS；`b6-gates.log`）

| 门 | 结果 |
|---|---|
| occlusion | rc=0，0 flags（自检 6 类全触发） |
| p8_extract | noted 150/150 |
| p8_compare | rc=0，CLEAN（JSON 本体 keydiff [137, 138]；gates 日志 `keydiffs=0` 为 stdout 文本计数口径，以 JSON 为准） |
| freeze_sha256（版内自比对） | run rc=0，8/8 |
| print_web_text | 8/8 页，posdiff 0，msdiff 0；tokens 745/706/665/661/683/647/734/1600 |
| pdftotext_nonempty | print 47,924 B = web 47,924 B；web 2,155,389 B < 7 MB |
| p8_fontsize | answer-zone min 10.12pt，median 10.12pt，spans 561（≥ 9.75pt） |
| p8_chips | core {A2:8, B1:24, B2:3} = edition |
| s11_svg | off-palette {}，gold/old False，stroked_rects 0，VOL.5=5=core，paper fills 8 |

## 6. 印/网文字层逐页比对（自写 PyMuPDF 位置排序，0.1pt；`b6-textlayer.py/.log/.json`）

| 对比 | posdiff | msdiff | 备注 |
|---|---|---|---|
| 印 vs 交付网 | 1（仅 P1） | 0 | 唯一 token：P1 报头 `De Lucerna`，x 394.00 → 393.80，dx=−0.20pt，dy=0——已知字体子集化微移（核心 fix5 同类：P1 2 token 0.2pt） |
| 印 vs 重建网 | 1（仅 P1，同 token） | 0 | 同上 |
| 交付网 vs 重建网 | 0 | 0 | 文字层全同 |
| pdftotext（PyMuPDF 文本字节） | 印 46,775 = 网 46,775 = 重建网 46,775 | — | 与套件 pdftotext 47,924 B 口径不同，两法各自印=网 |
| P8 全 spans 最小字号 | 印 10.12pt / 网 10.12pt，760 spans | — | ≥ 9.75pt |
| 斜体 span（旧 D1 复核） | 印 1 / 网 1 | — | 均为 P1 `«de groepswinst»` 16.12pt Italic；旧 D1 已消除 |

## 7. Occlusion / Freeze（`tools/`，`b6-occlusion*.log` / `b6-freeze-core.log`）

- `occlusion_audit.py --selftest` rc=0，6 类全触发，干净对照静默；`occlusion_audit.py svg/` rc=0，**0 flags**。
- `freeze.py baseline --build core-nl --core-svg core-nl/svg` rc=0，**8/8 SVGs byte-identical**，core shipped SVG 跑前后哈希不变。

## 8. p8 extract / compare（`tools/p8.py`，`b6-p8-*.log/.json`）

- extract：noted set **150/150**。
- compare（核心 vs 本版）：`status: CLEAN, total: 150, missing: [], extra: [], uncertain: [], keydiff: [137, 138]`。137/138 为翻译题，键本身即读者语（核心中文 vs 本版日文），按设计不同，非缺陷。修前 keydiff 为 [137, 138, 140]——D9 把 140 移出。

## 9. 三源逐题比对（registry / text.md / P8；`b6-keycheck.py/.log`，表见 `b6-keycheck-table.txt`）

- **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
- Q140 三源同为 `Ik maak een surprise met een kort gedicht.`（MATCH）。
- 配对键 25–28 = d/c/a/b（与 P2 印出选项 a 列表/b 小诗/c 马食/d 门边逐项核对一致），141–144 = b/c/d/a（与 P8 F 区印出选项逐项核对一致）。
- 语义手验：150 题题干–键逐题读过，全部搭配正确（Q73 `In vier regels schrijf ik een ___.` → `gedicht`；Q78 单数 `gaat maken` / Q79 复数 `gaan schrijven`；图表题 35+30+20+15=100 与 P6 图表原文一致；Q107 单数 `speelde` vs Q60 复数 `speelden` 对照正确）。

## 10. 孤儿标点横扫（自写；`b6-orphan.py/.log/.json`）

| | 结果 |
|---|---|
| `<text>` 元素总数 | 2069（P1 210 / P2 183 / P3 173 / P4 171 / P5 185 / P6 187 / P7 178 / P8 782） |
| (a) 独行标点（视觉行内唯一元素） | **0**（12 个纯标点片段均为行内片段：`–`（德国–荷兰连词）与 `）`（`（de）`/`（het）`闭括号），均有同行邻元，非独行） |
| (b) 行首标点（leftmost 判定） | **0**，8 页全 0 |
| brute-force 以标点开头的 `<text>` | 13 个，leftmost 0 个（均为行中片段：P1 `：`、P8 `』`/`）`/`、`答案区内联定位符） |

## 11. Creambox（`b6-creambox.py/.log`，PIL advance 法）

修后 TOTAL **6 flags**，与修前逐项相同：P2 CREAM-RIGHT（`ZO ONTHOUD JE HET　こう覚えよう`，右缘内 5.4px，8px 警告带而已）+ CREAM-BOTTOM 1.0px、P5 CREAM-BOTTOM 0.9px、P6 PAGE-EDGE + CREAM-RIGHT（`DE GRAFIEK　グラフ（練習データ）` advance 右缘 1864.8）+ CREAM-BOTTOM（底 689.4 vs 盒 691.0，盒内 1.6px）——均为已知假阳性（见 §12 PDF 像素裁决）。P4（D11 盒）0 flags。**真溢出 0。**

## 12. 盒标题横向真墨扫描（PIL 全量 + 交付印 PDF 300dpi 裁决；`b6-boxtitle.py/.log/.json`）

- PIL 全量 2015 个 `<text>`（advance 修正版度量）：超出版心右缘 1862 者 6 个（P4 图注 1873.5、P6 标题 1864.5、P8 三处 1862.5–1873.8）；超自身奶油盒右缘者 1 个（P6 标题）。
- 交付印 PDF 300dpi 逐项裁决 30 个近边文本（PIL 右缘距限值 ≤10px 者，敏感阈值、纸/奶油双底色）：**0 越边**。关键值：P6 `DE GRAFIEK　グラフ（練習データ）` PDF 真墨最右 1848.88（内 13.12px；PIL 高估）；P4 图注 `Foto: Spaarnestad Photo…` 1861.04（内 0.96px）；P8 `ANTWOORDEN` 注行 1861.04（内 0.96px）；P2 `Wat hoort bij pakjesavond?…` 1853.36（内 8.64px）；P8 `主語＋動詞＋時` / `方法` 1860.4（内 1.6px）。
- 口径说明：任务“56 标题”在本版可枚举集合中未能复现（奶油盒首行 26、双语标题 ≥20pt 60、双语标题全部 82）；本次全量扫描 2015 文本为其超集，结论不受口径影响。
- 目检裁图：`b6-crop-p6-title.png`（P6 标题在盒内，右缘留白清晰）、`b6-crop-p4-credit.png`（图注两行在版心内）。

## 13. Spill 横扫（`b6-spill.py/.log`）

**0 spills**。P4 HET PROGRAMMA 盒（底 1229.6）无任何 below 命中（仅 ABOVE −44.15px 图注 `domein`）；其余 BELOW 命中 6 处（+24/+32/+50.5 ×2/+60 ×2）均为独立版块（下一节标题、quiz 提示语、gloss 解説）——与核心 fix5 同类裁决。ABOVE/SIDE 均为图注/邻盒标题。

## 14. 目检裁图（交付印 PDF，200dpi）

`b6-crop-p3-d6.png`（桥接 2 行，`。` 在行末）、`b6-crop-p7-d7.png`（3 行，末行 `する。`）、`b6-crop-p8-q140.png`（Q140 印出 `kort gedicht`）、`b6-crop-p4-d11.png`（`18:45 uur.` 在盒内，下有明显留白）、`b6-crop-p6-title.png`、`b6-crop-p4-credit.png`——六张均目检通过。

## 15. 旧缺陷复核

| 旧缺陷 | 复核 |
|---|---|
| 旧 D1（中）网 PDF 失斜体 | **已消除**：交付网 PDF 斜体 span 1 个（P1 `«de groepswinst»` LucernaNewsreader-Italic 16.12pt），与印 PDF 一致（§6） |
| 旧 D2（低）ABSTRACT 缺 `De` | **未消除**：`grep -c "De Lucerna" ABSTRACT.txt` = **0**；见 PROOF-NOTE D2'（唯一未过项） |
| 旧 O1（Q78 Zij 歧义） | 观察非缺陷：P8 注消歧已在位，核心同文，见 PROOF-NOTE |
| 旧 O2（freeze.py 无 freeze_direct） | 方法备注：本次以 `freeze.py baseline`（核心重建 8/8）+ 版内自比对 8/8 代替 |
| nl-de D3/D4 家族项 | 本版无：text.md `答案` 0 命中（标记已本地化为 `答え`）；P2 SVG 与 build-5 字节一致，D3 断行与余量不变 |

## 16. D5 字体（只记录，不作门、不修）

- 印 PDF 字体计数：NotoSansCJKsc-Bold 463 / Regular 312、NotoSerifCJKsc-Regular 297 / Bold 1、Newsreader16pt-Regular 1072 / Italic 1、UnifrakturMaguntia 1。
- 网 PDF：LucernaNotoSansCJKSC-Bol 463 / Reg 312、LucernaNotoSerifCJKSC-Re 297 / Bo 1、LucernaNewsreader-Regula 1032 / Bold 40 / Italic 1、LucernaUnifrakturMagunti 1。
- CJK 字体上的纯拉丁 span：378（span 口径；核心 fix5 的 245 为分段口径，不可直接比）。
