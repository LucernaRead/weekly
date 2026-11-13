# GATE-LOG — 2026-W47 it-nl 独立复校（proof2）门禁总表

- 版：`2026-w47-it-nl`（it × nl，VOL.4）
- 结论：**20/20 PASS，0 FAIL**（独立重跑；gates 输出 `logs/gates-proof2.log`，RC=0）
- 三 SHA（开工盘核 + 收尾复核一致）：
  - 印 PDF：14,034,409 B，`2091448cb9155812311ae298e0c2f349d0b2d83ac6fa94f26f79f10b4c4c5a7f`
  - 网 PDF：1,291,738 B，`039ee0bb9cc55f4faeceba85d5e11752abbb6fd2843de2e082c9c4cdf2b88b8f`
  - text.md：55,509 B，1,317 行，`0a044d4b87da3cf281a18dad08cecef6d2842a99f4cb44da36276e35f902f4dd`
- 工具：`~/workspace/weekly-git/tools/`（venv Python，Pillow 13.0.0）；TMPDIR = 本 scratch `tmp/`；生产区只读，未 commit、未 push，未改任何生产文件。

## A. 构建复现

| # | 门 | 命令/方法 | 结果 |
|---|---|---|---|
| A1 | run.py | 版 build-copy 内 `PYTHONDONTWRITEBYTECODE=1 tools/venv/bin/python run.py`（OUT 已重定向至 scratch） | RC=0，TOTAL 150，A2 47 / B1 70 / B2 33，页 10/18/18/18/18/18/12/38，范文 99 词；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（`logs/run-rebuild.log`） |
| A2 | 重建 SVG 8/8 | 重建 SVG 与交付 SVG sha256 逐项比对 | 8/8 MATCH（p1–p8 全等） |
| A3 | freeze baseline（核心） | `tools/freeze.py baseline --build core-it --core-svg core-it/svg --out freeze-base-core`（--core-svg 指核心 svg 子目录；build-copy 核实为核心版） | **8/8 字节一致**，RC=0（`logs/freeze-baseline-core.log`）；核心 SVG 运行前后无变化 |
| A4 | 重渲印 PDF | 版 build-copy 内 render.py | RC=0，14,034,409 B，SHA-256 与交付**逐字节相同**（`logs/render-rebuild.log`） |
| A5 | 重建网 PDF | `tools/webpdf.py freeze-base/svg → freeze-base/La-Lucerna-VOL4-NL-web.pdf` | RC=0，1,291,734 B（交付 1,291,738 B，相差 4 B）；文字层逐字节一致（45,938 text bytes）；19 个子集字体解压后 Length1 相同、cmap 码点集与字形数已比对者 13/13 全等——字节序不确定性，内容等价，记观察（PROOF-NOTE §9-1），非门禁失败 |

注：A3 的另一取向（--build 为版目录、--core-svg 为核心）跑出 0/8 属人为错配（版 ≠ 核心），不作门禁结论；该次运行的产物即 A2 的 8/8（`logs/freeze-baseline.log`）。

## B. 机械门禁（gates-proof2.py 独立重跑，20/20）

| # | 门 | 实测值 |
|---|---|---|
| B1 | occlusion 0 flags | 0 flags（工具自检先行通过） |
| B2 | p8 extract noted count | noted=150，rc=0 |
| B3 | p8 compare vs core | verdict=CLEAN，keydiffs=[137, 138, 139]（重定向的读者语句键，预期内；Q140 意大利语键无差异，正确） |
| B4 | freeze diff fragments explained (P1–7) | unexplained_add=[]，unexplained_rem=[] |
| B5 | freeze diff report present | pages=['1'..'8'] |
| B6 | freeze strict-cjk | rc=1（工具对新增 CJK 的常规返回），added_cjk={'\\u3000': 8}，non_space={}——仅 SOP §1.1 家具分隔符 |
| B7 | print/web text multiset identical | print_words=7888，web_words=7888，chars_equal=True，word_diff=[] |
| B8 | web PDF < 7MB | 1,291,738 bytes |
| B9 | print PDF size sane | 14,034,409 bytes |
| B10 | P8 min font ≥ 13px (9.75pt) | min=13.0（SVG）；PyMuPDF 实测印 PDF P8 最小 9.75 pt，网 PDF 同 9.75 pt；P8 字号谱 9.75–34.5 pt |
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
| P7 | 3,784 | 750 | 全等 |
| P8 | 9,508 | 2,210 | 全等 |
| 合计 | 35,823 | 7,888 | 8/8 全等 |

## D. 几何专项（独立于 B1 的补充量测，审计 BOXTITLE 不覆盖无边框奶油盒）

| # | 项 | 方法 | 结果 |
|---|---|---|---|
| D1 | 奶油盒标题/内容越缘 | `measure_cream.py`：审计同款 PIL 真墨盒，29 个 #f0eee5 盒逐盒、逐行（含基线分组聚合拆分 run） | **29/29 在内，越缘 > +0.5 px 者 0**；最紧：P1 LA SETTIMANA 盒内行余 4.8 px；P7 "LA PAROLA　WOORD VAN DE WEEK" 标题余 8.5 px；P1 cifre 标题余 23.0 px（`logs/cream-measure.log`） |
| D2 | 刊头带 | 同款墨盒逐段量测 + 渲染裁图 | 墨 10.5–1873.7，左余 10.5 px、右余 76.3 px，spacing 11.0 在位，无剪裁（`crops/p1-masthead.png`） |
| D3 | 光栅裁图证据 | 交付 SVG 直渲 PNG 裁图目视 | P7 LA PAROLA 盒、P1 LA SETTIMANA 盒、P1 cifre 盒：标题完整在盒内，右缘可见余白（`crops/`） |
| D4 | 流末/页界 | run log 各流末位置 | 全部在底边内（P8-keys 2529/2552 余 23 px；P1-quiz 2491/2540；P2-ex 2356/2580；P6-ex 2464/2580）；无 spill、无孤儿 |
| D5 | P8 "VUL DE KRONIEK IN" 类 | 全版 grep + 目视 | 本版无此标题；A 节为 "COMPLETA LA CRONACA"，无长荷兰语标题 |

## E. 内容核验（手验，非门禁脚本）

| # | 项 | 结果 |
|---|---|---|
| E1 | 全文通读 | text.md 1,317 行逐行读完 |
| E2 | 150 题三源 | 登记 vs text.md vs P8 印出键逐题一致，编号连续 |
| E3 | 日期/星期 | `date -d` 验 13 个日期，文中星期表述全对 |
| E4 | 算术 | MD11 进球和 24；Q85 13−11=2；Q86 6+7=13；Torrone 16 天/3 周末；TFF 9 天；范文 99 词 |
| E5 | 8 金句 | text.md 中各恰 2 次（正文 + P7），页码标注全对 |
| E6 | 事实外核 | 意甲 MD11 全部比分/积分/MD12 赛程、Eurochocolate 32 届、Torrone 29 届、BookCity 15 届及数字、TFF 44 届、ATP Finals 阵容与排名、Manovra 数字与法案号 C. 3174-bis——均经 2026-11-11 公开检索逐项核实（来源见 PROOF-NOTE §8） |
| E7 | 标题数 | ≥30 px 节点 37 个；标题字符串出现 27 次；去重 20 个（"56" 非本版实测数，不采用） |
| E8 | 8 页目视 | `render/p1–p8.png` 逐页目视：无溢出/重叠/压页脚/豆腐块；页脚逐页在位 |

## F. 观察项（不计缺陷）

1. 网 PDF 重建 4 B 差异（A5）：子集字体字节序不确定性，内容等价。
2. KIT §10 两处观察与交付不符：Q92 印出注为一词 "Groeiprognose"；Q32 注用 «Fate dolci» 角引号。KIT 需订正，版面无需改动。
3. "circa 26 miliardi"：官方公报称约 260 亿，文中已 hedged（"circa"+"根据报纸重建"），不构成缺陷。

## G. 缺陷清单

无。零缺陷，可定稿。

## H. 产物索引

- `PROOF-NOTE.md`、`GATE-LOG.md`（本文件）
- `logs/`：gates-proof2.log、run-rebuild.log、render-rebuild.log、webpdf-rebuild.log、freeze-baseline.log、freeze-baseline-core.log、cream-measure.log、render-png.log
- `measure_cream.py`、`gates/gates-proof2.py`、`gates/nl/`（p8-extract.json、p8-compare.json、freeze-diff.json）
- `render/p1–p8.png`、`crops/*.png`、`freeze-base/`、`freeze-base-core/`、`tmp/pw/`（逐页印/网文字层）
