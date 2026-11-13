# GATE-LOG — 2026-W47 it-nl 独立复校（重扩散 2 后全量重校）门禁总表

- 版：`2026-w47-it-nl`（it × nl，VOL.4）
- 结论：**20/20 PASS，0 FAIL**（独立重跑；gates 输出 `logs/gates-reproof.log`，RC=0）
- 三 SHA（开工盘核 + 收尾复核一致）：
  - 印 PDF：14,034,396 B，`a7edbb18d6cde81c3d9454d636ee4412c7f555c2aabc20665fa08c059d2a8a5e`
  - 网 PDF：1,291,725 B，`d57398427d4dc493ea5104b3ab86343d83a5edd9e83093d3335baff4fb66fbb7`
  - text.md：55,488 B，1,317 行，`b13ef7a7abe07928207eedc182106368ac653d8a8fad49af2adf184a2c94906e`
- 工具：`~/workspace/weekly-git/tools/`（venv Python，Pillow 13.0.0）；TMPDIR = 本 scratch `tmp/`；生产区只读，未 commit、未 push，未改任何生产文件。

## A. 构建复现

| # | 门 | 命令/方法 | 结果 |
|---|---|---|---|
| A1 | run.py | 版 build-copy 内 `PYTHONDONTWRITEBYTECODE=1 tools/venv/bin/python run.py`（OUT 已重定向至 scratch，grep 核对无生产路径残留） | RC=0，TOTAL 150，A2 47 / B1 70 / B2 33，页 10/18/18/18/18/18/12/38，范文 99 词；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（`logs/run-rebuild.log`）；P4 col3 末端 1140.45（= 核心）、P7 col3 末端 1673.0、P8-ex 流末 col 3 y=870、P8-keys 流末 2529/2552 |
| A2 | 重建 SVG 8/8 | 重建 SVG 与交付 SVG sha256 逐项比对 | 8/8 MATCH（p1–p8 全等） |
| A3 | freeze baseline（核心） | `tools/freeze.py baseline --build core-it --core-svg core-it/svg --out freeze-base-core`（--core-svg 指核心 svg 子目录；build-copy 核实为核心版——含核心 `2026-w47-it-zh-cn.text.md` SHA `9eb9ee06…` 与核心两 PDF） | **8/8 字节一致**，RC=0（`logs/freeze-baseline-core.log`）；核心 p7 为 D-2 定稿 `a7e6afa4…`；核心 SVG 运行前后无变化 |
| A4 | 重渲印 PDF | 版 build-copy 内 render.py | RC=0，14,034,396 B，SHA-256 与交付**逐字节相同**（`a7edbb18…`，`logs/render-rebuild.log`） |
| A5 | 重建网 PDF | `tools/webpdf.py build/svg → build/La-Lucerna-VOL4-NL-web.pdf` | RC=0，1,291,725 B（与交付**同字节数**）；SHA 不同；文字层逐字节一致（110,119 text bytes，`cmp` 通过）——fontTools 子集化字节序不确定性，内容等价，记观察（PROOF-NOTE §11-1），非门禁失败 |

## B. 机械门禁（gates-reproof.py 独立重跑，20/20）

| # | 门 | 实测值 |
|---|---|---|
| B1 | occlusion 0 flags | 0 flags（工具自检先行通过） |
| B2 | p8 extract noted count | noted=150，rc=0 |
| B3 | p8 compare vs core | verdict=CLEAN，keydiffs=[137, 138, 139]（重定向的读者语句键，预期内；Q140 意大利语键无差异，正确） |
| B4 | freeze diff fragments explained (P1–7) | unexplained_add=[]，unexplained_rem=[] |
| B5 | freeze diff report present | pages=['1'..'8'] |
| B6 | freeze strict-cjk | rc=1（工具对新增 CJK 的常规返回），added_cjk={'\\u3000': 8}，non_space={}——仅 SOP §1.1 家具分隔符 |
| B7 | print/web text multiset identical | print_words=7885，web_words=7885，chars_equal=True，word_diff=[]（修前 7,888，恰 −3 词） |
| B8 | web PDF < 7MB | 1,291,725 bytes |
| B9 | print PDF size sane | 14,034,396 bytes |
| B10 | P8 min font ≥ 13px (9.75pt) | min=13.0（SVG）；PyMuPDF 实测印 PDF P8 最小 9.75 pt，网 PDF 同 9.75 pt；P8 字号谱 9.75×180、10.5×8、11.62×67、12.0×11、12.38×6、12.75×5…… |
| B11 | paper #fbfaf6 present | PASS |
| B12 | no gold/brick/near-black | hits=[] |
| B13 | no VOL.5 in furniture | VOL.5 text nodes=3（仅下期预告头、LETTERE 披露、P2 交叉引用） |
| B14 | VOL.4 present | count=9 |
| B15 | badge colours A2/B1/B2 | PASS（#5c6e30 / #46581f / #37402f） |
| B16 | no double outer frame | full-page rects=0 |
| B17 | textmd validate | forward-miss: 0，reverse-miss: 0 |
| B18 | answers count 150 | edition=150，core=150 |
| B19 | keys 1–150 match core | mismatches=[]（137–139 重定向、写作题除外） |
| B20 | notes match translations.py | mismatches=[]，table_gaps=[]（137–140 + 写作题除外） |

补充：'·' 在 SVG 中共 148 次（选项串/ gloss 表内，核心既有用法）。

## C. 逐页印/网文字层比对（pdftotext -layout，逐页字符+词多重集）

| 页 | 字符（印=网） | 词（印=网） | 结论 |
|---|---|---|---|
| P1 | 3,779 | 863 | 全等 |
| P2 | 4,157 | 905 | 全等 |
| P3 | 3,512 | 761 | 全等 |
| P4 | 3,475 | 796 | 全等 |
| P5 | 3,559 | 740 | 全等 |
| P6 | 4,049 | 863 | 全等 |
| P7 | 3,769 | 747 | 全等（修前 3,784 字符 / 750 词，恰为 D-2 删去的 15 字符 / 3 词） |
| P8 | 9,508 | 2,210 | 全等 |
| 合计 | 35,808 | 7,885 | 8/8 全等 |

## D. 几何专项（独立于 B1 的补充量测，审计 BOXTITLE 不覆盖无边框奶油盒）

| # | 项 | 方法 | 结果 |
|---|---|---|---|
| D1 | 奶油盒标题/内容越缘 | `measure_cream.py`：审计同款 PIL 真墨盒，29 个 #f0eee5 盒逐盒、逐行（含基线分组聚合拆分 run） | **29/29 在内，越缘 > +0.5 px 者 0**；最紧：P1 LA SETTIMANA 盒内行余 4.8 px；P7 "LA PAROLA　WOORD VAN DE WEEK" 标题余 8.5 px；P1 cifre 标题余 23.0 px（`logs/cream-measure.log`） |
| D2 | 备份旧版对照（STRADDLE 规则） | 同一脚本跑重扩散前备份 `scratch-refanout-it2/backup/2026-w47-it-nl/svg` | 两份量测日志**逐字节相同**（`diff` 无差异）；无裁切、无重叠、无回归（`logs/cream-measure-backup.log`） |
| D3 | 刊头带 | `occlusion_audit.py::ink_box` 逐段量测 + 200 dpi 渲染目视 | 墨 10.5–1873.7，左余 10.5 px、右余 76.3 px，spacing 11.0 在位（`content12.py:18`），无剪裁；与重扩散实测值逐字一致 |
| D4 | 流末/页界 | run log 各流末位置 | 全部在底边内（P8-keys 2529/2552 余 23 px；P8-ex 870/1332；P4 col3 1140.45）；无 spill、无孤儿 |
| D5 | P8 "VUL DE KRONIEK IN" 类 | 全版 grep + 目视 | 本版无此标题；A 节为 "COMPLETA LA CRONACA"，无长荷兰语标题 |

## E. D-2 回归专项（独立重测）

| # | 项 | 结果 |
|---|---|---|
| E1 | text.md:775/:777 新串 | 两条新串逐字在位 |
| E2 | 旧串全版重扫 | `Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在 content7.py、p7 SVG、text.md、印/网 PDF P7 文字层均为 0 |
| E3 | 印/网 PDF P7 文字层 | 新串 L17 ×1、L18 ×1（空白+箭头归一化后计数）；旧串各 0 |
| E4 | 与重扩散前备份 diff | text.md 仅 :775/:777 两行；SVG 仅 p7；cards 仅 p7；content 仅 content7.py :17/:18；text.md 恰 −21 B（55,509→55,488）；两 PDF 因 P7 而变 |
| E5 | P7 教学句语义 | L17 规则例只剩 assaggiare/guardare（规则 ✓）；L18 leggere 为 regolare（✓）；andare 已不在规则例中（andrò 不规则 ✓） |

## F. 内容核验（手验，非门禁脚本）

| # | 项 | 结果 |
|---|---|---|
| F1 | 全文通读 | text.md 1,317 行逐行读完 |
| F2 | 150 题三源 | 登记 vs text.md 题面 vs P8 印出键逐题一致（REG vs 题面 0 差异；REG vs Risposte 0 差异；REG vs P8 印出键 0 差异；编号 1–150 连续；Q150 写作题标记一致） |
| F3 | 日期/星期 | `date -d`（Europe/Rome）验 22 个日期，文中星期表述全对 |
| F4 | 算术 | MD11 进球和 24；Q85 13−11=2；Q86 6+7=13；Torrone 16 天/3 周末；TFF 9 天；范文 99 词 |
| F5 | 8 金句 | text.md 中各恰 2 次（正文 + P7），页码标注全对 |
| F6 | 事实外核 | 意甲 MD11 全部比分/积分/MD12 赛程、Eurochocolate 32 届、Torrone 29 届及各时刻、BookCity 15 届及数字/Whitehead/de Waal、TFF 44 届、Filmmaker 14–22 日、ATP Finals 阵容与排名、Nations League 两场、Manovra 数字/法案号 C. 3174-bis/IRPEF/听证与截止日、历史事实（1630/1631–1687/1898/2013）——均经本轮 2026-11-11 公开检索逐项核实（来源见 PROOF-NOTE §7） |
| F7 | 标题数 | ≥30 px 节点 37 个；标题字符串出现 27 次；去重 20 个（"56" 非本版实测数，不采用） |
| F8 | 8 页目视 | `render/p-1–p-8.png`（交付印 PDF，200 dpi）逐页目视：无溢出/重叠/压页脚/豆腐块；页脚逐页在位；P7 两条 D-2 新句渲染干净 |
| F9 | ABSTRACT.txt | 荷兰语单行，含真实主题/刊名/VOL.4/A2–B2/150 题 |

## G. 观察项（不计缺陷）

1. 网 PDF 重建 SHA 不同（A5）：子集字体字节序不确定性，文字层逐字节一致，内容等价。
2. KIT §10 两处观察与交付文件不符：Q92 印出注为一词 "Groeiprognose"；Q32 注用 «Fate dolci» 角引号。KIT 需订正，版面无需改动。
3. P1 LA SETTIMANA 奶油盒最紧处余 4.8 px：STRADDLE 规则下不构成缺陷（在内、无裁切、无重叠、与备份相同），下一轮重扩散仍须重测。
4. "circa 26 miliardi"：CdM 法案版多家来源确认为约 26 亿，文中已 hedged，不构成缺陷。

## H. 缺陷清单

无。零缺陷，可定稿。

## I. 产物索引

- `PROOF-NOTE.md`、`GATE-LOG.md`（本文件）
- `logs/`：gates-reproof.log、run-rebuild.log、render-rebuild.log、webpdf-rebuild.log、freeze-baseline-core.log、cream-measure.log、cream-measure-backup.log、registry.json
- `measure_cream.py`、`measure_cream_backup.py`、`gates/gates-reproof.py`、`gates/nl/`（p8-extract.json、p8-compare.json、freeze-diff.json）
- `render/p-1–p-8.png`、`tmp/pw/`（逐页印/网文字层）
- `build/`（版 build-copy 重建 SVG + 重渲印/网 PDF）、`freeze-base-core/`（核心 freeze baseline）
