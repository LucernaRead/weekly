# W47 zh-cn-it re-proof 门禁日志（fix1 后，17 门）

- 校对员：独立复校员；对象：`production/2026-w47/2026-w47-zh-cn-it/`（fix1 后）
- 日期：2026-11-11；解释器：`tools/venv/bin/python`（Pillow 13.0.0）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-cn-it1/`
- 原始日志：`run-rebuild.log`、`render.log`、`gates-it.log`、`freeze-diff.log`、
  `freeze-baseline.log`、`occlusion.log`、`p8extract.log`、`p8compare.log`、
  `keycheck.log`、`measure-final.log`、`render-check-new.log`、
  `spill-orphan.log`、`threeway.log`、`regdump.log`

## 身份核对

| 文件 | 字节 | SHA-256 | 与先验 |
|---|---|---|---|
| `Lucerna-VOL4-IT.pdf`（印） | 41,730,133 | `440490c4a389e22edc2c93f5b99fdb5bec857dafceeb1256e0f3af007598a69d` | 一致 |
| `Lucerna-VOL4-IT-web.pdf`（网） | 2,641,804 | `75dec91ac806b884bdd4b7cdbdccc39e2c445ff7f668d24ff4365f21f233a512` | 一致 |
| `2026-w47-zh-cn-it.text.md`（文） | 50,916 | `afc9b2c02a319ab1d20227d3c0826942fc969aa577f61caea56b3845d664544f` | 一致 |

## 17 门逐项实测

| # | 门 | 实测值 | 结论 |
|---|---|---|---|
| 1 | 磁盘探针 | `git hash-object -w /dev/null` → `e69de29b…`，RC=0；scratch 真实写盘 `probe.txt` 成功 | PASS |
| 2 | 三 SHA/尺寸核对 | 见上表，三 SHA 全符、三尺寸全符；KIT 所载三 SHA 一致 | PASS |
| 3 | `run.py` scratch 重建 | RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38；题型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1），0 FLOW OVERFLOW / 0 HEAD TOO WIDE；P8 keys 终 2506.4；范文 138 字 | PASS |
| 4 | SVG 重建 8/8 字节一致 | 重建 svg vs 交付 svg，sha256 逐页比对：p1–p8 全部 MATCH | PASS |
| 5 | 印 PDF 重渲 SHA 逐字节相同 | scratch `render.py` 重渲：41,730,133 B，SHA `440490c4a389e22edc2c93f5b99fdb5bec857dafceeb1256e0f3af007598a69d`，与交付逐字节相同（中途服务重启打断首跑一次，重跑 RC=0） | PASS |
| 6 | freeze 核心 baseline 8/8 | `freeze.py baseline --build core-zh-cn --core-svg core-zh-cn/svg`，RC=0，8/8 OK；核心完整性确认（交付核心 SVG 跑前后重哈希未变） | PASS |
| 7 | freeze 本版自身 8/8 | `gates-zhcn.py` freeze_sha256：run rc=0，match 8/8 | PASS |
| 8 | `freeze.py diff --strict-cjk` | RC=0，TOTAL added CJK **0**（逐页 added 0；CJK core→edition 仅因英文串换意语而减） | PASS |
| 9 | occlusion 审计 | RC=0，**0 flags**；自检六类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1，clean 对照静默）。注：BOXTITLE 对无边框奶油盒仍全盲（已知工具缺口），由门 10 的奶油盒横扫补位 | PASS（工具缺口见 PROOF-NOTE） |
| 10 | 奶油盒横扫 + 纵扫 | 横扫：521 个盒内文本元 PIL 真墨，溢出 0；仅 1 紧贴：P4 `Parole delle partite` +6.5 px（proof1 同值）。纵扫：P5 行实墨止于 svg y=2536.3（PIL 框底 2560.2 为 em 框 artifact，2560–2590 带 0 暗像素）；P7 teaser 实墨止于 2560.7，离页脚线 2596 有 35 px 以上净空（记观察 O-1） | PASS |
| 11 | spill 扫 | 全部 `<text>` PIL 真墨框 vs 1950×2700 版面：出界 **0**（UnifrakturMaguntia 以更宽的 Noto Serif CJK Bold 代算，保守上界） | PASS |
| 12 | 孤儿扫（vs 核心集逐项比对） | 本版行首闭合标点孤儿 **0**；核心同法 **0**；**0 新增**。Q36/Q37/Q130 式填空行与核心 (x, y) 逐项同位，核心继承 | PASS |
| 13 | p8 extract | 150/150 noted（`p8.py extract --total 150`，RC=0） | PASS |
| 14 | p8 compare | vs 核心 P8：**CLEAN**，missing=[]，extra=0，keydiff=[]（RC=0） | PASS |
| 15 | keycheck 150 | REG 150 vs P8 抽取键：**149/150 精确**；唯一非精确 Q150 印刷键 `✓`（REG 键为内部开放题标签；核心同位置亦印 `✓`，`p8extract.json` keys['150']='✓'，非截断；实印 `150. ✓ Esercizio aperto — modello sopra, sezione F (138 caratteri).` 已重组核实，见 PROOF-NOTE） | PASS（预期内） |
| 16 | 印/网文字层 8 页 | **预期 FAIL**：P1 pos212/ms8、P2 pos356/ms1、P5 pos205/ms1；P3/P4/P6/P7/P8 posdiff/msdiff **均为 0**。token 差分恰为 5 处旧串（P1 web-only `ancora/in/numeri/nuovo`；P2 web-only `della/settimana`；P5 同前），+ 断行 token 化 artifact；余者逐字相同。网 PDF 仍为 #3 版，全家统一重建前预期如此，**不作缺陷**（E-1） | FAIL（预期项） |
| 17 | P8 最小字号 | 印 PDF 答案区最小 **9.98pt**（median 9.98pt，369 spans）≥ 9.75pt 底线 | PASS |

## 配套复核（门外实测值，见 PROOF-NOTE）

- `gates-zhcn.py` 11 门：10/11 PASS（仅 print_web_text 为门 16 的预期 FAIL）；
  img_overlap 0 hits；p8 chips A2 11 / B1 24 / B2 3 = 核心；U+2019 0；
  §1.1 SVG 审计 clean（paper #fbfaf6 ×8，无离谱色，无描边页框，VOL.5=1=核心）。
- fix1 五项双法重测：D-01 PIL +67.5 / 渲染 +67.6；D-02 +68.5 / +68.4；
  D-03 +46.5 / +46.4；D-04 +117.5 / +118.5；D-05 单行、孤儿 `》`→0
  （渲染像素确认孤儿行无墨、原行有墨）。门限 ≥+5 px，全部大幅通过。
- P1 截稿行全扫：日历盒 8 行全部清盒，最紧 +36.5 px（段末行），D-03 行 +46.5 px。
- 150 题三方：130 道非配对题题干 text.md + 当页 SVG 全命中、键全一致；
  20 道配对题逐组核对（Q25–28 a/b/c/d、Q43–46 b/d/a/c、Q61–64 d/b/c/a、
  Q79–82 c/b/d/a、Q97–100 c/d/a/b），键与印出释义逐一相符；单题语义抽查 11 题全符。
- D4/D5：`全球总决赛的BO5` ×2、Q56 键注 ×1、`GEN在S16一场没输` ×2、
  `只丢了一小局` ×2、`对LYON 2比1` ×1、保留 `淘汰赛一局没输` ×1；旧措辞 0。
- text.md diff：5 处反向替换逐字节还原 fix1 前文件（50,958 B，
  SHA `f954151f…`），diff 恰好 5 行。
- 金句 8 条各 2×；日期 `date -d` 17 项全符；目视 P1–P8 零溢出/重叠/压页脚。
- 旧串 5 项去空白复核：`Questa settimana in numeri` 0、`Date della settimana` 0、
  `esce il nuovo film` 0、`la finale non ancora giocata` 0；
  `Parole della settimana` 1× 仅 P7 词表头（合法），`non ancora giocata` 1×
  仅 :86 段内另一句（合法）。

## 总计

- 17 门：16 PASS + 1 预期 FAIL（门 16，网 PDF #3 旧串，全家统一重建前预期）。
- 新缺陷 R-01…：**0 条**。结论 (a) 零缺陷，可定稿（见 PROOF-NOTE.md）。
