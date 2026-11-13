# GATE-LOG.md — 2026-w47-it-ru 独立复校门禁记录（core D-2 fix 后重扩散，全量复校）

复校 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-ru/`
门禁脚本：`scratch-fanout-it/gates.py` 的逐字副本（`gates-ru.py`，仅把输出目录 SCRATCH 改指本 scratch；另复制 `translations.py`、`validate_edition_textmd.py` 供其导入/调用），用仓库 venv（`tools/venv/bin/python`，Pillow 13.0.0）运行。原始输出：`gates-ru-raw.log`。freeze baseline 用仓库原版 `tools/freeze.py`，未改工具。

## SHA 核对（开工前；收工重验逐字一致）

| 文件 | 字节数 | SHA-256（实测） | 给定值 | 结果 |
|---|---|---|---|---|
| La-Lucerna-VOL4-RU.pdf | 14,180,915 | 966a9d10c033ed0297cef6d018b23a548dec2b016bc0eb3ecf61440ac2247666 | 966a9d10…47666 | 全对 |
| La-Lucerna-VOL4-RU-web.pdf | 1,441,240 | db22fa31244bb4fe0a7649660a621aa15da22cda010eaad4fd0ff9e619ed0505 | db22fa31…0505 | 全对 |
| 2026-w47-it-ru.text.md | 67,731 | 47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d | 47c04715…52b1d | 全对 |

另：`git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0，返回 `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`。

## 门禁结果：20/20 PASS（RC=0，GATES ALL PASS）

```
PASS occlusion 0 flags | /home/hatch/workspace/weekly-git/production/2026-w47/2026-w47-it-ru/svg: 0 flags
PASS p8 extract noted count | noted=150 rc=0
PASS p8 compare vs core | verdict=CLEAN keydiffs=[137, 138, 139]
PASS freeze diff fragments explained by translations/furniture (P1-7) | unexplained_add=[] unexplained_rem=[]
PASS freeze diff report present | pages=['1', '2', '3', '4', '5', '6', '7', '8']
PASS freeze strict-cjk (no added CJK except U+3000) | rc=1 added_cjk={'\u3000': 8} non_space={}
PASS print/web text multiset identical | print_words=7587 web_words=7587 chars_equal=True word_diff=[] []
PASS web PDF < 7MB | 1441240 bytes
PASS print PDF size sane | 14180915 bytes
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
PASS notes match translations.py (except 137-140 + writing) | mismatches=[]
GATES ALL PASS
```

说明：
- keydiff [137, 138, 139] 为预期的重定向读者句键（与 refanout 时一致），非缺陷。
- strict-cjk 的 rc=1 只因 U+3000（SOP §1.1 家具分隔符，豁免）被 freeze.py 计入 CJK；non_space={}，门禁按此通过（与 refanout 的 gates-ru.log 同款）。
- 印/网文字层词数 7,587，较重扩散前 7,590 恰 −3（D-2 删去的 `andare`、`→`、`andrò,` 三词）；`pdftotext` 印/网输出另经 `cmp` 逐字节相同（各 6,112 词按 pdftotext 分词口径，`print.txt` / `web.txt`）。

## freeze baseline 重建：8/8（RC=0）

命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out <scratch>/freeze-baseline`
输出（`freeze-baseline.log`）：`runtime: …/tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3`；`baseline: 8/8 SVGs byte-identical`（p1 d301b886…、p2 a744e5d2…、p3 fe0a0e65…、p4 12ddd86c…、p5 08929554…、p6 621054ee…、p7 a7e6afa4…、p8 779aa98c…）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`；另本轮自验：运行前后 core SVG 重哈希 diff 为空（`core-svg-sha-pre.txt` vs `core-svg-sha-post.txt`）。
build-copy 核实确为 core-it 自身（非 edition 冒充）：`freeze-baseline/build-copy/content7.py` 与 core-it 仅 OUT 路径行不同，L17/L18 为 D-2 新串；与本版 content7.py 的 diff 含 band/bridge 本地化行（`LINGUA　ЯЗЫК`、`Говорите о планах…` 等）。

## D-2 回归实测值（`check_ab*.log`）

| 检查 | 实测 |
|---|---|
| 新串 L17 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` | content7.py:17 ×1；p7 SVG ×1（节点加空格拼接）；text.md:775 ×1；印/网 PDF P7 文字层各 ×1（空白折叠 + 箭头归一化后计数） |
| 新串 L18 `Il verbo è leggere, regolare al futuro: leggerò.` | content7.py:18 ×1；p7 SVG ×1；text.md:777 ×1；印/网 PDF P7 文字层各 ×1 |
| 旧串 `Le forme sono regolari: andare` / `irregolare al futuro: leggerò` | content7.py、8 SVG、text.md、印/网 PDF 文字层全 0 |
| 与备份旧版 diff | SVG 仅 p7 不同；cards 仅 p7 不同；text.md diff 恰 (774,775)+(776,777) 两处；content diff 恰 content7.py L17/L18；text.md 67,752 → 67,731，恰 −21 字节 |
| content7.py vs core-it | L17/L18 逐字相同 |
| P7 语义 | andare 未来时不规则（FluentU / FlexiClasses / Rosetta Stone / Dolce Vita 四源一致：andare → andr- 元音脱落型不规则词干）、leggere 未来时规则（FlexiClasses 规则表：LEGGERE → io leggerò）、assaggiare / guardare 规则；全文 `regolar` 仅此两处 |

测量口径备注：PDF 文字层箭头粘词（`→assaggerò,`、`guardare→`）且换行断句，直接整串 grep 会误报新串 0（本次初版即因此误报，后以归一化方法重测纠正）；SVG 文本节点按行断开，须加空格拼接后计数。此为提取口径问题，非内容问题。

## D-1 回归实测值

| 检查 | 实测 |
|---|---|
| 旧形 «налоговая ставка» | text.md 0；SVG 8 页 0；印 PDF 文字层 0；网 PDF 文字层 0 |
| 新形 «ступень налоговой шкалы» | text.md 5（:663、:763、:987、:1217、:1305）；SVG p6 ×1、p8 ×2；印/网 PDF 文字层各 3 处（P6 ×1、P8 ×2；pdftotext grep 计 3 行） |
| P6 NOTE 注释盒 | 盒 x=538.5 y=1102.4 w=422.5 h=264.575（SVG）；7 行基线 1140.9–1319.2 全在盒内；PDF 词框最右 708.0 pt = 944.0 SVG，盒右缘 961.0，余 +17.0 SVG px |
| P8 key 100（PDF 词框） | 单行；右缘 1001.1 pt = 1334.8 SVG；栏（col3，右缘 1411.5）余 **+76.7 SVG px** |
| P8 key 144（PDF 词框） | 单行；右缘 1311.3 pt = 1748.4 SVG；栏（col4，右缘 1862.0）余 **+113.6 SVG px** |
| P8 最小字号 | 13.0 px = 9.75 pt（SOP §1.1 下限，恰达下限） |
| P1/P2 标题 vs 备份 | 印 PDF 词框逐字相同（P1 x1=800.0 pt / 1066.6 SVG、P2 x1=767.0 pt / 1022.7 SVG）；越框量 P1 105.6 / P2 61.7 SVG px，观察项（STRADDLE：无边框、无裁切、无重叠、与备份相同） |
| 混合语种空格 | pdftotext 合并词 22 个，备份印 PDF 完全相同——旧有表现，非回归 |

## 全文通读与目视

- text.md 1317 行（`wc -l`）逐行通读：150 题键逐题核对与题干一致（单号 138 项 + 区间头 25–28 / 52–55 / 141–144 = 150）；8 金句各 ×2（正文 + P7 列表）逐字一致；样文 99 词实测 99；星期全验（`TZ=Europe/Rome date -d`：11 月 12 日周四、15 日周日、16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二）；比分表 10 场进球加总 24 ✓。
- 8 页逐页目视交付印 PDF（200 dpi 渲染，`render-p1.png`–`render-p8.png`）：无溢出、无重叠、无裁切、无豆腐、无压页脚；P7 两条 D-2 新句渲染干净。

## 缺陷

无。结论 (a) 零缺陷可定稿。
