# GATE-LOG.md — 2026-w47-it-ru 独立复校门禁记录（fix1 后第二轮）

复校 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it-ru1/`
门禁脚本：`scratch-fanout-it/gates.py` 的逐字副本（`gates-ru-copy.py`，仅把输出目录 SCRATCH 改指本 scratch；另复制 `translations.py`、`validate_edition_textmd.py` 供其导入/调用），用仓库 venv（`tools/venv/bin/python`，Pillow 13.0.0）运行。原始输出：`gates-ru-raw.log`。

## SHA 核对（开工前）

| 文件 | 字节数 | SHA-256（实测） | 给定值 | 结果 |
|---|---|---|---|---|
| La-Lucerna-VOL4-RU.pdf | 14,180,929 | af980e26fcb124773e0e3a5824e3ff742e6a72f8da50c8e53ab017418adf6200 | af980e26…df6200 | 全对 |
| La-Lucerna-VOL4-RU-web.pdf | 1,441,248 | 3e10d785bd1eab5318ef175a52bdebef89649622d1a7f53ea891b54b4f652cc9 | 3e10d785…52cc9 | 全对 |
| 2026-w47-it-ru.text.md | 67,752 | 8a49ce37cc7df3ba92569243cd28b0286bee6651547f526c8cacdf112c5c895c | 8a49ce37…c895c | 全对 |

另：`git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0。

## 门禁结果：20/20 PASS（RC=0，GATES ALL PASS）

```
PASS occlusion 0 flags | /home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-it-ru/svg: 0 flags
PASS p8 extract noted count | noted=150 rc=0
PASS p8 compare vs core | verdict=CLEAN keydiffs=[137, 138, 139]
PASS freeze diff fragments explained by translations/furniture (P1-7) | unexplained_add=[] unexplained_rem=[]
PASS freeze diff report present | pages=['1', '2', '3', '4', '5', '6', '7', '8']
PASS freeze strict-cjk (no added CJK except U+3000) | rc=1 added_cjk={'\u3000': 8} non_space={}
PASS print/web text multiset identical | print_words=7590 web_words=7590 chars_equal=True word_diff=[] []
PASS web PDF < 7MB | 1441248 bytes
PASS print PDF size sane | 14180929 bytes
PASS P8 min font >= 13px (9.75pt) | min=13.0
PASS paper #fbfaf6 present
PASS no gold/brick/near-black | hits=[]
PASS no VOL.5 in furniture (only preview/disclosure) | VOL.5 text nodes=3
PASS VOL.4 present | count=9
PASS badge colours A2/B1/B2
PASS no double outer frame | full-page rects=0
INFO '·' total occurrences in SVGs: 148 (core had them only in options/gloss lists)
PASS textmd validate | 2026-w47-it-ru forward-miss: 0 reverse-miss: 0
PASS answers count 150 | edition=150 core=150
PASS keys 1-150 match core (except 137-139 re-aimed, writing) | mismatches=[]
PASS notes match translations.py (except 137-140 + writing) | mismatches=[] table_gaps=[]
GATES ALL PASS
```

说明：
- keydiff [137, 138, 139] 为预期的重定向读者句键（与 refanout 时一致），非缺陷。
- strict-cjk 的 rc=1 只因 U+3000（SOP §1.1 家具分隔符，豁免）被 freeze.py 计入 CJK；non_space={}，门禁按此通过（与 refanout 的 gates-ru.log 同款）。

## freeze baseline 重建：8/8（RC=0）

命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out <scratch>/freeze-baseline`
输出（`freeze-baseline.log`）：`runtime: …/tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3`；`baseline: 8/8 SVGs byte-identical`（p1 d301b886…、p2 a744e5d2…、p3 fe0a0e65…、p4 12ddd86c…、p5 08929554…、p6 621054ee…、p7 3746030a…、p8 779aa98c…）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。

## D-1 回归实测值

| 检查 | 实测 |
|---|---|
| 旧形 «налоговая ставка» | text.md 0；SVG 8 页 0；印 PDF 文字层 0；网 PDF 文字层 0 |
| 新形 «ступень налоговой шкалы» | text.md 5（:663、:763、:987、:1217、:1305）；SVG p6 ×1、p8 ×2、p7 ×0（注为 text.md-only，属设计）；印/网 PDF 文字层 P6 «ступень» ×1、P8 新形 ×2 |
| translations.py 三处 ru 值 | L805、L1782、L2080 皆为新形 |
| P6 NOTE 注释盒（PDF 渲染像素） | 盒 x=538.5 y=1102.4 w=422.5 h=264.575（SVG）；7 行全在盒内：上余 11.0 pt、下余 31.3 pt、右最小余 12.7 pt |
| P8 key 100（PDF 词框） | 单行；右缘 1334.8 SVG 单位；栏右余 76.7 SVG px（fix1 称 77.9） |
| P8 key 144（PDF 词框） | 单行；右缘 1748.4 SVG 单位；栏右余 113.6 SVG px（fix1 称 112.8） |
| P8 最小字号 | 13.0 px = 9.75 pt（SOP §1.1 下限） |
| P1/P2 标题 vs 备份 | text.md:45/:205 相同；SVG 节点相同；印 PDF 词框相同（P1 x1=800.0 pt、P2 x1=767.0 pt，新旧一致）；越框量 P1 105.6 / P2 61.7 SVG px，观察项（STRADDLE 规则：无边框、无裁切、无重叠、与备份相同） |
| 混合语种空格 | pdftotext 合并词 22 个（13 去重），备份印 PDF 完全相同——旧有表现，非回归 |

## 全文通读

text.md 1317 行逐行通读（P1–P8）：150 题键与题干逐题核对一致；事实/数字自洽；样文 99 词与所称一致。除 PROOF-NOTE.md 的 D-2 外无其他缺陷。

## 缺陷（见 PROOF-NOTE.md）

- **D-2（新，高严重度）**：P7 未来时讲解规则性标签说反——`content7.py` L17「Le forme sono regolari: andare → andrò…」（andare 未来时不规则）与 L18「Il verbo è leggere, irregolare al futuro: leggerò.」（leggere 未来时规则）。冻结核心句，全 12 版 it-* 共有；须 core 改后重 fan-out。
