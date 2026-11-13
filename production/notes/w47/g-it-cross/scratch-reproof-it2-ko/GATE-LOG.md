# GATE-LOG — 2026-W47 it-ko 独立复校（re-proof，重扩散 2 后）

- 版：`2026-w47-it-ko`（Italiano × 한국어，VOL.4）
- 复校员：reproof（独立于重扩散员与 proof2）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-ko/`
- 日期：2026-11-11（America/Toronto）
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`TMPDIR=<scratch>/tmp`；`PYTHONDONTWRITEBYTECODE=1`
- 开工三 SHA（盘上实测，与任务值逐字一致；收工复核仍一致）：
  - 印 `La-Lucerna-VOL4-KO.pdf` 19,296,892 B / `3125d4f36667155d5f10eb3522364513ba31bee72a4445f1e5ac90d74b28f87f`
  - 网 `La-Lucerna-VOL4-KO-web.pdf` 1,607,467 B / `67bda0ac5dfd57c6dce140bc021e420044888d11c63dcb25426bb2e95becfef8`
  - 文 `2026-w47-it-ko.text.md` 57,326 B / `d4d0c6c1a0048b9f2fa3248c0b5868058a3599bf75d253188301f3ad0a5a8fa1`
- 生产文件零写入：全部重建/验证均在 scratch 内完成；收工三 SHA 与开工逐字一致。

## 1. D-2 回归门（逐项独立重测，全过）

| # | 门 | 实测 | 证据 |
|---|---|---|---|
| R1 | 新串 text.md:775/:777 | 两行逐字在位 | `sed -n 775p;777p` |
| R2 | 新串 content7.py:17/:18 | 两行逐字在位 | `sed -n 17p;18p` |
| R3 | 新串 p7 SVG | 换行碎片在位（`'Atalanta–Inter. Le forme sono regolari:'`、`'assaggerò, guardare '`、`'verbo è leggere, regolare al futuro: leggerò.'`） | SVG 节点提取 |
| R4 | 新串印/网 PDF P7 文字层 | 各 ×1（PyMuPDF 自然词序 + 箭头归一化） | 脚本实测（inline） |
| R5 | 旧串 `Le forme sono regolari: andare` / `irregolare al futuro: leggerò` | live 文件 0 处（content7.py、text.md、p7 SVG、两 PDF 文字层）；全版 grep 仅 KIT:98 历史引用行 | grep -c 全 0；KIT:98 为披露 |
| R6 | 与重扩散前生产版 diff | 只许 P7 变化：text.md 恰 :775/:777 两行、57,347→57,326 B（−21）；SVG 仅 p7；cards 仅 p7；content 仅 content7.py:17/:18；两 PDF 变；KIT 变（文档） | `diff` / `cmp` 逐文件；备份两 PDF SHA = 修前历史值 `d5698327…`/`85722a84…` |
| R7 | P7 语义（B） | assaggiare/guardare 规则 -are、leggere 规则 -ere，标签正确；全版 `regolar` 仅两行；Q101–104 无规则性断言 | 全文 grep + 语法核查 |
| R8 | 词数旁证 | pdftotext 7,411 词 vs proof2 旧版 7,414，差恰 −3 | gates 日志 |

## 2. 机械门 19/19（`logs/gates-ko.log`，`gates-proof2.py ko`，rc=0，GATES ALL PASS）

| # | 门 | 结果 | 实测值 |
|---|---|---|---|
| G1 | occlusion 0 flags | PASS | `svg: 0 flags` |
| G2 | p8 extract noted count | PASS | noted=150 rc=0 |
| G3 | p8 compare vs core | PASS | verdict=CLEAN keydiffs=[137, 138, 139] |
| G4 | freeze diff fragments explained (P1–7) | PASS | unexplained_add=[] unexplained_rem=[] |
| G5 | freeze diff report present | PASS | pages=['1'..'8'] |
| G6 | print/web text multiset identical | PASS | print_words=7411 web_words=7411 chars_equal=True |
| G7 | web PDF < 7MB | PASS | 1,607,467 bytes |
| G8 | print PDF size sane | PASS | 19,296,892 bytes |
| G9 | P8 min font ≥ 13px (9.75pt) | PASS | min=13.0（SVG）；印 PDF PyMuPDF 实测 min 9.75pt，520 spans |
| G10 | paper #fbfaf6 present | PASS | — |
| G11 | no gold/brick/near-black | PASS | hits=[] |
| G12 | no VOL.5 in furniture | PASS | VOL.5 text nodes=3（仅预告/披露/交叉引用） |
| G13 | VOL.4 present | PASS | count=9 |
| G14 | badge colours A2/B1/B2 | PASS | #5c6e30 / #46581f / #37402f 齐全 |
| G15 | no double outer frame | PASS | full-page rects=0 |
| G16 | textmd validate | PASS | forward-miss: 0 reverse-miss: 0 |
| G17 | answers count 150 | PASS | edition=150 core=150 |
| G18 | keys 1–150 match core | PASS | mismatches=[]（137–139 重定向、写作题除外） |
| G19 | notes match translations.py | PASS | mismatches=[] table_gaps=[]（137–140 + 写作题除外） |

注：ko 为 ko-READER 版（非 ko-TARGET），不适用 ko 豁免；CJK 3 版分母 19 即本表 19 项（无 strict-CJK 项——strict-cjk 仅适用于拉丁/西里尔版）。

## 3. 重建门（scratch 副本，OUT/BASE 已重定向，生产零写入）

| # | 门 | 结果 | 实测值 |
|---|---|---|---|
| B1 | run.py | rc=0 | TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；P7-a2 末端 y=1124；P7 col3 1673.0；P8-keys 2499（底 2552）；P8-ex col3 y=870（`logs/run.log`） |
| B2 | SVG 重建 vs 生产 | 8/8 逐字节一致 | p1–p8 全部 SAME（`logs/render.log`） |
| B3 | 印 PDF 重渲 vs 交付 | 逐字节相同 | SHA `3125d4f3…`（= 交付值） |
| B4 | 网 PDF 重建 | rc=0 | 1,607,467 B（= 交付字节数），46,935 文字字节；文字层逐字节相同；二进制差异仅字体子集流内（obj 20 FontFile2 /Length 1975 vs 1976；差异字节 878,484 个，均在子集流区段）——见 PROOF-NOTE O6 |
| B5 | freeze baseline（`--core-svg` 指 core-it 自身 `svg/`） | 8/8 逐字节一致 | p1 `d301b886…`、p2 `a744e5d2…`、p3 `fe0a0e65…`、p4 `12ddd86c…`、p5 `08929554…`、p6 `621054ee…`、p7 `a7e6afa4…`（= D-2 定稿值）、p8 `779aa98c…`；core integrity：发货 SVG 运行前后重哈希无变化（`logs/freeze-baseline.log`） |
| B6 | build-copy 核实为 core-it 自身 | 通过 | build-copy content7.py 与 core-it 仅 OUT 重定向行不同；与本版 content7.py 同样仅 OUT 行不同；core content8/12/34 md5 与 KIT §11 一致（`629b5b0a…` / `91cdfbb9…` / `18926942…`）；未用 edition 目录冒充 core |

## 4. 几何与像素门

| # | 门 | 结果 | 实测值 |
|---|---|---|---|
| P1 | h-overflow PIL 真墨扫描（2,213 节点） | 3 旗标，全部澄清 | P1 +0.4/+0.5px、P8 +0.5px；行级像素实测真墨右缘 1860.96（−1.04）、1856.16（−5.84）、1851.84（−10.16），全部在 1862 内（`logs/h-overflow.log`、`logs/pixel-check.log`） |
| P2 | creambox canonical 全版扫描 | 9 处 desc-clear 负值全部澄清 | 真墨余量 +3.24~+5.42px，全部在盒内；其余负 clearance 均为 +45px 窗口假阳性（inside-only 均为正）（`logs/creambox.log`、`logs/pixel-check.log`） |
| P3 | P8 模型文行级实测 | 与核心逐行相同（O2） | 两行真墨右缘 1863.36（+1.36px）；按各自基线对齐：核心同两行右缘同为 1863.44 列、暗像素 34、实色 22（`logs/rowlevel.log`） |
| P4 | P2/P5 毛边行级实测 | 抗锯齿毛边（O3） | 真墨右缘 1862.88（+0.88px），越边像素 17/10、实色 0、最浅灰度 104；旧版新版 P2/P5 整页渲染逐像素相同（差异 0） |
| P5 | 盒标题 STRADDLE sweep（`sweep_box_titles.py`） | 新旧逐字相同；2 处越盒为观察项（O10） | P1 cifre 标题 PIL +72.5px / 像素 +67.6px；P2 frase 标题 PIL +44.5px / 像素 +43.2px；与备份像素逐值相同；越墨区无任何元素；末字完整（`logs/sweep-box-new.log`、`logs/sweep-box-old.log`，diff 空） |
| P6 | 印/网词框位置比对（PyMuPDF，0.1pt） | P2–P8 0 差异 | P1 仅刊头 4 处 x 差 0.4–0.5pt（O7）；词多重集 8 页全同 |

## 5. 内容核对门

| # | 门 | 结果 | 实测值 |
|---|---|---|---|
| C1 | 150 题三源逐题手验 | 150/150，0 差异 | REG=150 body=150 risp=150 p8keys=150；MISMATCHES: 0（`logs/threeway.log`、`out/reg.json`） |
| C2 | 8 金句逐字核对 | 8/8 各 ×2 | 正文 + P7 各 1 次（`«Il governo propone»` 计 3 次系 P6 框 + Q88 + Q127，非金句） |
| C3 | 日期/星期（`date -d`，Europe/Rome） | 20/20 一致 | 11月16日周一…11月22日周日、11月23日周一、11月24日周二、12月2日周三、12月6日周日、12月31日周四、10月15日周四、10月28日周三、11月9日周一、11月12日周四、11月6–8日周五–周日、11月13–14日周五–周六 |
| C4 | 算术重算 | 全过 | 13−11=2、6+7=13、10 场比分复加 24 球、积分榜 29/28/27/24/23/5、TFF 9 天、BookCity 7 天、Torrone 16 天·3 周末、BookCity 1,360/2,487/1,164/443 与 Q70/73/80 一致 |
| C5 | 全文通读 text.md 1,317 行 | 0 问题 | 无拼写/语法/截断/事实错误；韩语讲解层无他语残留 |
| C6 | 8 页逐页目视交付印 PDF（200 dpi） | 0 问题 | 无溢出、重叠、压页脚、豆腐块（`pages/pdf-p-1..8.png`） |
| C7 | 范文词数 | 99 词 | 与“99단어”标注一致 |
| C8 | ABSTRACT.txt | 通过 | 一行韩语，421 B，无 ASCII 双引号 |
| C9 | 禁词扫描 | 0 命中 | Ucraina/Russia/Putin（正文+讲解层） |
| C10 | 标题数实测 | 48 原始节点 / 35 不同（页，基线） | “56”不复现（幻数）；与 proof2 同口径实测逐字相同 |
| C11 | 读者层语言纯净 | 通过 | 可视 `<text>` 节点汉字/假名/西里尔 0 命中；仅有的 3 个汉字在 P1 兽蛾 logo 非渲染 `<title>` 内（核心同款） |

## 6. 结论

**19/19 机械门 + 全部重建门 + 全部内容核对门通过；缺陷 0 项；观察项 11 项（见 PROOF-NOTE §8）。结论 (a) 零缺陷，可定稿。**
