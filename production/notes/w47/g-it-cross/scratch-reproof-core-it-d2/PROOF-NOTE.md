# 复校结论：(a) 零缺陷，可定稿 —— core-it D-2 fix 后从头全量核心复校

**版本**：2026-W47 core-it（意大利语目标语 × 简体中文读者，VOL.4），D-2 fix 后完整独立复校（SOP §8.4：修后从头复校）。
**复校员**：独立核心复校（`scratch-reproof-core-it-d2`），与 fix 员不同人。只读生产，未写生产目录任何文件，未 commit、未 push。
**开工探针**：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件通过；`TMPDIR=<scratch>/tmp`，未写 /tmp；解释器全程 `tools/venv/bin/python`（Pillow 13.0.0）。
**已读**：SOP.md §8、§1.1 全文 + core-it `WEEKLY-KIT.md` 全文 + `~/workspace/weekly-git/AGENTS.md` + `scratch-fix-core-it-d2/FIX-LOG.md` 全文 + `scratch-reproof-it-ru1/PROOF-NOTE.md` §D-2。

## SHA 核对（开工前实测，与任务给定值逐字一致；完工时重测不变）

| 文件 | 字节数 | SHA-256（实测，开工与完工两次一致） |
|---|---|---|
| 印 `La-Lucerna-VOL4.pdf` | 27,726,330 | `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d` |
| 网 `La-Lucerna-VOL4-web.pdf` | 1,790,596 | `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef` |
| 文 `2026-w47-it-zh-cn.text.md` | 52,655（1317 行） | `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed` |

## D-2 回归：干净（六项任务指定验证全部通过）

**① 新串各就其位**（`d2-rescan.log` / `d2-rescan2.log` / `d2-svg-pdf-p7.log`）：
- L17 新句 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` 在 `content7.py:17`、p7 SVG（XML 文本节点归一化计数 1）、`text.md:775` 各 1 处；PDF 文字层：整篇 pdftotext 因栏位交错断行、单行 grep 为 0，但 P7 页内词序核查（PyMuPDF 词框，`p7-wordorder.log`）证实全部词在 A2 栏内、按正确栏序出现，`→` 为独立词符。
- L18 新句 `Il verbo è leggere, regolare al futuro: leggerò.` 在 `content7.py:18`、p7 SVG（1 处）、`text.md:777`、印/网 PDF 文字层（归一化后各 1 处）。

**② 旧串全版 0 处**：`Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在 `content*.py`（逐文件 grep 全 0）、8 个 SVG（0 文件）、`.text.md`（0）、印/网 PDF 文字层（归一化后各 0）。唯一残留是 `WEEKLY-KIT.md:89`（§7 条目 18 的 Fix 历史行，引用旧串作记录）——任务指明的唯一合法残留，不作缺陷。

**③ `regolar` 全核心仅两行**：`content*.py` 中 `grep -n regolar` = 2 行（即 `content7.py:17/:18` 修复后文本）；`text.md` 2 处、`svg/` 2 处（均为同一两行），无其他同类规则性断言。

**④ P7 渲染放大目视**：200 dpi 交付印 PDF 的 P7 A2 栏裁图（`crop-p7-a2.png`）——两句在版、干净，无溢出/重叠；桥接句与习题区 intact。

**⑤ Q101–104 修前修后逐题相等**（`keycheck.log`、`p8-pre.json` vs `p8-new.json`）：101 `andremo`、102 `assaggeremo`、103 `guarderemo`、104 `B`，三源（登记表/印刷键/文本导出）全等；Q104 键注 `leggerò 是 leggere 的将来时` 无规则性断言，未动。

**⑥ 仅 P7 变化**：
- SVG：P1–P6/P8 与修前逐字节一致（修前 SHA 见 FIX-LOG `svg-sha-pre.txt`，逐一比对全同）；P7 `3746030a…` → `a7e6afa4…`。
- Cards：P1–P6/P8 与修前逐字节一致（对照 fix1 `freeze-baseline3/build-copy/cards/`，逐一 sha256 全同）；仅 p7 不同。
- 文本导出 diff：以 git HEAD 的修前 `text.md`（SHA `d0c573b8…` 已验）为基准，diff 恰为 775/777 两行（`textmd-prefixed.md`，`diff` 输出见本目录日志）。
- P7 SVG 文本节点级 diff（修前备份 `3746030a…` vs 现版，`lettere-compare.log`）：仅 A2 未来时段落的文本节点不同（166 → 160 个节点，系重排并行），其余节点逐字相同。

## 全量复校结果（从头全量，不只验 D-2）

- **全文通读**：`text.md` 1317 行逐行读完（P1–P8 + Risposte 1–150）。目标语拼写/变位/性数、讲解层对照、注释词均在正文出现；150 题题面与键逐题手验无误。
- **150 题三源 keycheck**（`keycheck.py` / `keycheck.log`）：登记表（content 源）150、P8 印刷键 150、文本导出 Risposte 150，三源键 0 差异、注释 0 差异；无缺号、无重号。写作题 150 为登记表专有键 `（开放题，范文如下）`，印刷与文本均为 `✓`，符合既定设计（KIT §8）。注：登记表与文本导出的注释比对是同一导出器的自洽检查；独立性由 P8 印刷键（p8.py 自 SVG 提取）与目视 P8 承担。
- **事实/日期/算术**（`misc-scans.log`）：
  - 意甲 MD11：10 场比分逐场重算 24 球（3+1+2+3+3+2+3+1+2+4）；积分榜 29/28/27/24/23/5；并以公开来源独立抽查核实（多家意媒：10 场比分、24 球、积分榜、Gattuso 带拉齐奥、拉齐奥不败、罗马最佳进攻，均吻合）。
  - BookCity：15 届、Nov 23–29（7 天）、1,360/2,487/1,164/443、主题 «Il senno sulla Luna»（Ariosto）、开幕周一 23 日 20:00 Teatro Dal Verme、Colson Whitehead（2× Pulitzer）——公开来源抽查吻合。
  - Torino Film Festival：44 届、周二 24 Nov–周三 2 Dec、9 天——官方 regolamento 抽查吻合；`8 dicembre` 0 处；`20 novembre` 4 处均合法（castradina 当晚 + 23/66/120 干扰项）。
  - 图表算术：13−11=2、6+7=13；Torrone 7–22 日 = 16 天、3 个周末；听证会 9–12 日 = 4 天；范文 99 词（脚本实数）；头条 39 非空格字符 ≤56；星期：Nov 16 周一、17 周二、21 周六、22 周日、23 周一、24 周二、Oct 15 周四、Oct 28 周三、Nov 12 周四、Nov 15 周日，均以 `date` 核验无误。
  - 禁词：Ucraina/Russia/Putin 0 处；Torrazzo “campanile medievale in mattoni più alto d'Italia”（D11 定稿措辞）在版。
  - P6 听证会时态：P6 用现在时（«ascoltano»，历史现在时，意语新闻常规）而 P2 用完成时（«hanno ascoltato»）——两种形式均正确，非事实错误，接受。
  - P8 A/B 区复测前面版次的题是综合评估卷的既定设计（复测 113–128 对应前面题号），非重复缺陷。
- **8 金句**：逐字核对，8 句在归一化 `text.md` 中各恰 2 次（正文 + P7），页码标注 P1×2、P2、P3、P4、P5、P6×2 均与正文所在页一致。
- **8 页逐页目视**：交付印 PDF 的 200 dpi 全页渲染（`render200-p1.png` … `render200-p8.png`，4063×5625）逐页看完：无溢出、无重叠、无压页脚、图片与出处齐全；P4 五行赛果表（SAB/DOM 各两行）清晰；P6 图表条形与数据成比例、“DATI INVENTATI” 三处标注在版；P8 全部答案与范文、Vermeer 图在版。
- **P8 最小字号**：SVG 最小 13.0 px = **9.75 pt**（652 个 13 px 节点）；印 PDF P8 实测最小字号 9.75 pt（534 个 span），恰达 SOP §1.1 下限 9.75 pt。
- **§1.1 扫描**：禁用色（`#b3a06a` 等 14 个）0 处；`VOL.4 ·` 家具分隔符 0 处；ABSTRACT.txt 一行、287 B、无 ASCII 双引号；网 PDF 1,790,596 B < 7 MB。

## 门禁汇总（详见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| 独立重建（scratch 拷本，OUT/BASE 重指） | rc=0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；范文 99 词；P7-a2 flow 末端 y=1124（底 1560），P7 col3 末端 1644.0 不变 |
| freeze baseline（core-svg 指 core-it 自身 svg/） | **8/8 字节一致**；build-copy 已核实为 core-it 自身（`content7.py:17/:18` 含修复后新串 + 核心标志）；发运 SVG 运行前后重哈希无变化 |
| occlusion audit（selftest 先过） | selftest OK（6 类阳性全触发、干净对照沉默）；生产 8 页 **0 flags** |
| p8 extract + compare | noted 150/150；与修前 P8 compare **CLEAN**（keydiff=[]）；三源 keycheck 0 差异 |
| text.md 导出与校验 | 自源码重导出的 text.md 与发运版**逐字节一致**（SHA `9eb9ee06…`）；validate forward-miss 0 / reverse-miss 0 |
| 印/网文字层 | pdftotext 各 43,979 B、5,948 词，`cmp` rc=0 字节一致；逐页比对 8/8 一致 |
| 横向漫出（PIL 全 8 页 + 200 dpi 渲染全 8 页） | PIL：越过页面边距 1862 的仅 2 条家具线，均为 +0.0（恰止于边距）；左越边距 0；200 dpi 渲染：P1/P3/P4/P6/P7 无越边距墨迹，P2 +0.7 pt、P5 +0.7 pt、P8 +1.0 pt——与修前 fix3 实测值完全相同，非本次引入 |
| P7 目视 | A2 两句在版干净（`crop-p7-a2.png`） |

## 缺陷清单

**无。结论 (a) 零缺陷，可定稿。**

## 观察项（不是缺陷，不拦定稿）

- **O1（网 PDF 重建 4 字节差，内容中性）**：独立重建的网 PDF 为 1,790,600 B（SHA `d5bc2d10…`），与发运版 1,790,596 B 差 4 字节；差异局限于一个内嵌字体流（FontFile2，对象 20）的压缩字节，文字层逐页字节一致，100 dpi 全页渲染逐像素一致（8 页 0 差异字节）。印 PDF 与 text.md 均可逐字节重现。属 webpdf 字体子集化的运行间非确定性，非内容差异。
- **O2（P3 E TU / P5 E TU / P7 LETTERE 奶油盒底沿偏紧）**：三盒末行中文（P3 “更喜欢牛轧糖还是巧克力？写两句寄来。”、P5 “更喜欢书、电影还是比赛？写两句寄来。”、P7 LETTERE 披露行）距盒底仅数 px 奶油边，但均在盒内、无裁切、无与可见边框或他元素重叠，occlusion 0 flags；P3/P5 SVG 与修前逐字节一致，P7 LETTERE 盒 rect（1439.5, 1370.0, 422.5, 274.0）与披露行节点（y=1611.12/1639.52）与修前备份（SHA `3746030a…`）逐字相同——按 STRADDLE 规则非回归，仅为观察项。
- **O3（200 dpi 渲染亚 1 pt 痕迹，修前已有）**：P2 +0.7 pt、P5 +0.7 pt、P8 +1.0 pt，与 fix3 §7/§8 的修前值完全相同（PIL 度量与渲染器 advance 差约 0.5–0.8% 的管线系统性特征），P7 干净，本次未引入。
- **O4（P1 图注页码指引）**：P1 体育场照片图注末尾 “(Pagina 4)” 指向第 4 版体育页，其余各版图注无页码指引；属有意的跨版指引，非错误，仅记一笔。
- **O5（方法备注，不修工具）**：PIL 横向扫描的 “into-gutter 156 条” 计数以跨栏同 y 合并伪影与全幅家具线为主，缺陷信号是“越过页边距”（本轮仅 2 条、均为 +0.0）；几何重叠以 occlusion 审计（真墨水盒）为准。另重申 KIT §7 条目 17 的盲区：`freeze.py diff` 只做 CJK 会计、`p8.py compare` 只比键，纯拉丁改动对二者不可见——本轮 D-2 以全核心旧串重扫 + 文本导出 diff + freeze baseline 字节比对三重覆盖，门禁全绿不单独作为修对的证据。

## 范围边界

本结论只针对核心版本身。10 个 it fan-out 版的状态不在本结论内（由协调员在核心复校 (a) 后另派重扩散，不在本报告中写入）。

## 交付文件（本 scratch 内）

- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`（每项门禁结果 + 实测值）
- 证据：`build.log`、`render.log`、`webpdf.log`、`export.log`、`validate.log`、`freeze.log`、`occlusion.log` / `occlusion.json` / `occlusion-selftest.log`、`p8-new.log` / `p8-new.json`、`p8-pre.json` / `p8-compare.log` / `p8-compare.json`、`keycheck.log` / `keycheck.py`、`d2-rescan.log` / `d2-rescan2.log` / `d2-svg-pdf-p7.log`、`p7-wordorder.log`、`h-scan.log` / `gutter-full.log` / `render-scan.log`、`misc-scans.log`、`webpdf-diff.log` / `webpdf-pixels.log`、`lettere-compare.log`、`print-prod.txt` / `web-prod.txt` / `print-p7.txt` / `web-p7.txt`、`textmd-prefixed.md`、`render200-p1.png` … `render200-p8.png`、`crop-p7-a2.png`、`crop-p3-etu.png`、`svg-sha-prod.txt`；独立重建产物在 `build/`（SVG 8/8、cards 8/8、印 PDF 均与发运版逐字节一致）。
