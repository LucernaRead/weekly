# GATE-LOG — 2026-W47 it-ja reproof（重扩散 2 后独立复校）

- 对象：`production/2026-w47/2026-w47-it-ja/`（重扩散 2 新版，core D-2 fix 后重建）
- 工具链：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`TMPDIR=<scratch>/tmp`；`PYTHONDONTWRITEBYTECODE=1`
- 全部命令的输出文件均在本 scratch 内；生产文件未被修改（build-copy 法，见 §1；收工三 SHA 再验一致）

## 0. 探针与 SHA（开工前）

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0
- scratch 真实写文件：`probe.txt` 写入并读回成功
- 印 PDF `640a355a2943efe35b7c1437e1154a4012aa1ec51f18fff155fc7caa4e1c6666` / 28,221,020 B ✓
- 网 PDF `4f1bac2c12b8762c187a60647fec578f187f9f5150a2b65cfca31b474f00ee3f` / 1,901,668 B ✓
- 文本 `5ac2ecf5abb28bbc9f56c182572a9c7a7e4e93ae8b9c49b5468cc890e0ec16d7` / 58,165 B ✓
- 收工时三件 SHA 再验一次，仍一致（见 §12）

## 0b. 回归 A — D-2 文字层与 P7-only diff（独立重测）

- 新串（空白归一化后计数）：`Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` 与 `Il verbo è leggere, regolare al futuro: leggerò.` 在 content7.py:17/:18、text.md:775/:777、p7 SVG（节点拼接）、印/网 PDF P7 文字层各 ×1，全版各 ×1。
- 旧串 `Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在 live 内容文件（content7.py、8 SVG、text.md、两 PDF 文字层）均为 0；唯一命中为 KIT.md:102 记录行。备份旧版 p7 SVG 中旧串各 ×1。
- `andrò` 全版 0 处；`andare` 在 text.md 8 次均为合法（Q42/Q76/Q101 题干原形提示、P2 `Al momento di andare in stampa`、键注、P7 诊所注）。
- 与备份 diff：text.md 恰 :775/:777 两行，58,186 → 58,165 B（−21）；SVG 仅 p7 不同（新 `12f2aeb9…`）；cards 仅 p7 不同；content 仅 content7.py :17/:18；p7 节点 diff 限定于两句碎片（旧 168 → 新 162 节点）。
- 200 dpi 裁图：新 P7 A2 栏两句干净（`render/p7-a2-crop.png`）；备份同区仍为旧错句（`render/p7-a2-crop-backup.png`）。

## 0c. 回归 B — P7 语义（独立检索核实）

- L17 只举 assaggiare/guardare 为规则形：正确；L18 `leggere, regolare al futuro: leggerò`：正确。公开依据：LibreTexts《Indicativo futuro》（leggere 为规则 -ere 例、andare → andr- 不规则词干）、LBCC Pressbooks《IL FUTURO》、FluentU、Lawless Italian、Dolce Vita（andare → andrò 不规则，规则形 *anderò* 不存在）。

## 1. run.py + render.py（scratch build-copy，OUT/BASE 改指 scratch）

- 拷本：`bslib4.py`、`svglib.py`、`content*.py`、`run.py`、`render.py`、`assets/` → `<scratch>/build/`；5 处 `OUT` 与 `render.py` 的 `BASE` 用 sed 改指 `<scratch>/build/svg` / `<scratch>/build`；改后 grep 确认生产路径残留 0 处。
- RC=0；TOTAL 150；级别 A2 47 / B1 70 / B2 33；页分布 10/18/18/18/18/18/12/38；模范文 99 词
- `FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE` 出现 0 次
- `flow[P8-keys] ended col 3/3 y=2546 (bottom 2552)`；P8-ex 末端 y=870（底边 1332）；P7-a2 flow 末端 y=1124（修前 1157）；P7 col3 末端 1673.0；P4 col3 末端 1140.45（= 核心）
- 日志：`run.log`、`render.log`

## 2. SVG 重建 8/8 字节一致

- build-copy 重建的 8 个 SVG 与交付 `svg/` 逐个 `cmp`：p1–p8 全部 IDENTICAL
- `tools/freeze.py baseline --build <本版> --core-svg <本版 svg>`：**8/8 byte-identical**，RC=0（日志 `freeze-edition.log`）
- `tools/freeze.py baseline --build <core-it> --core-svg <core-it svg>`：**8/8 byte-identical**，RC=0（日志 `freeze-core.log`；build-copy 经核实确为 core-it，p7 `a7e6afa4…` 为 D-2 定稿值）；核心完整性自验通过，core-it 0 文件被改动
- 重渲印 PDF：build-copy `render.py` RC=0；重渲印 PDF sha256 `640a355a2943efe35b7c1437e1154a4012aa1ec51f18fff155fc7caa4e1c6666`，与交付一致（28,221,020 B）

## 3. gates.py 19/19 PASS（独立重跑；harness 由 proof2 的 gates.py 复制、输出路径改到本 scratch）

| # | 门 | 结果 |
|---|---|---|
| 1 | occlusion 0 flags | PASS（0 flags） |
| 2 | p8 extract noted count | PASS（noted=150 rc=0） |
| 3 | p8 compare vs core | PASS（verdict=CLEAN keydiffs=[137, 138, 139]） |
| 4 | freeze diff fragments explained (P1-7) | PASS（unexplained_add=[] unexplained_rem=[]） |
| 5 | freeze diff report present | PASS（pages=['1'..'8']） |
| 6 | print/web text multiset identical | PASS（print_words=6746 web_words=6746 chars_equal=True） |
| 7 | web PDF < 7MB | PASS（1,901,668 bytes） |
| 8 | print PDF size sane | PASS（28,221,020 bytes） |
| 9 | P8 min font >= 13px (9.75pt) | PASS（min=13.0） |
| 10 | paper #fbfaf6 present | PASS |
| 11 | no gold/brick/near-black | PASS（hits=[]） |
| 12 | no VOL.5 in furniture | PASS（VOL.5 text nodes=3，均为合法节点） |
| 13 | VOL.4 present | PASS（count=9） |
| 14 | badge colours A2/B1/B2 | PASS |
| 15 | no double outer frame | PASS（full-page rects=0） |
| 16 | textmd validate | PASS（forward-miss: 0 reverse-miss: 0） |
| 17 | answers count 150 | PASS（edition=150 core=150） |
| 18 | keys 1-150 match core | PASS（mismatches=[]；137–139 重定向与写作项除外） |
| 19 | notes match translations.py | PASS（mismatches=[] table_gaps=[]；137–140 与写作项除外） |

INFO：'·' 总出现 148 次（均在选项串/讲解串/词表内）。
freeze diff 原始输出：P1 +61/−39、P2 +31/−28、P3 +30/−28、P4 +27/−26、P5 +44/−39、P6 +26/−25、P7 +41/−39、P8 +305/−376（与 proof2 逐页相同）；新增 CJK 全部为日语讲解层字符（CJK 版无 strict-CJK 项）。日志：`gates.log`，JSON 在 `ja/` 下。

## 4. 奶油盒 PIL 真墨扫（canonical creambox.py + 窄带交叉）

- canonical `hidden_files/w47/tools/creambox.py`（逐页跑，8 页 rc=0）：29 盒；盒内末行基线 clearance 全部 ≥ +4.5 px
  - 最小值：P2 解説盒 +5.3、P3 词表盒 +5.3、P4 E TU 盒 +4.5、P5 E TU 盒 +4.5、P7 LA PAROLA +4.5、P7 LETTERE +5.1
  - P7-TOOLBOX 汇总：3 盒，min inside clearance +4.5，min desc-clear −1.5
  - 7 处 desc-clear 负值（−0.9 ~ −1.5）：末行文字逐一核查均不含下行字母——日语句；渲染图确认末行在盒内留有空隙，非真实漫出
  - BELOW-WINDOW 行 12 条：全部为下一区块栏头/表行（P1 +24、P3 +37、P4 +26~+40、P6 +42），已知假阳性形态
- `tools/creambox_check.py`（0–8 px 窄带）：8 页全部 **NO OVERFLOW**
- 日志：`creambox.log`、`creambox-check.log`

## 5. spill 扫查（`spill_sweep.py`，proof2 同款）

- RC=0。候选 61 处，与 proof2 日志**逐字节相同**，全部为已知假阳性形态（下一区块栏头/表行/双栏图表的另一半）。
- 真溢出：**0**。日志：`spill-sweep.log`

## 6. 孤儿扫查（`orphan_sweep.py`，proof2 同款）

- 1439 行：[PIL-advance] class-a=0 class-b=0；[svglib-advance] class-a=0 class-b=0；逐页全 0
- 暴力复核：以闭合标点起首的 `<text>` 元素，行首者（leftmost）**0**
- E 标签定向检查：文本导出 翻訳=4、翻譯=0（Q137–140，L969/971/973/975）
- 行数说明：proof2 为 1438 行，本轮 1439 行（+1 系 P7 D-2 重排净增；零孤儿结论不变）
- 日志：`orphan-sweep.log`

## 7. 列溢出扫查（`colspill_scan.py`，proof2 同款）

- RC=0。原始命中 43 处，与 proof2 日志**逐字节相同**，逐项裁定全部为假阳性：
  - 双栏通栏元素（P1 头条/导语、P2 跨栏段、P4 表头/预览段、P6 图表带、P7 FRASI 引用、P8 RISPOSTE 带）
  - 栏头带 + 日语讲解（P1 +45、P2 +47.2）
  - `text-anchor=middle` 居中家具（各页 `答えは8ページ…` 行，+450.4 为锚点误读）
  - 表元/指示语伸入 28 px 栏间隙：P4 表格第二列 +10~+30、匹配题指示语 `単語と意味を合わせなさい` +7.5（P2/P4/P6/P8 各一处）、P7 +1.5——目视确认未触及相邻栏内容
- 真溢出：**0**。日志：`colspill.log`

## 8. 盒标题 STRADDLE 专项（备份对照已跑）

- `tools/occlusion_audit.py`（自检先过，BOXTITLE 阳性对照触发）：新版 8 页 **0 flags**；备份旧版 8 页 **0 flags**（日志 `occlusion-new.log` / `occlusion-backup.log`）。
- p7 节点 diff 限定于两句 D-2 句；全部盒标题新旧计数一致、文本一致；其余 7 页 SVG 与备份逐字节一致。
- 200 dpi 全页目视：全部盒标题完整在框内，无字形被裁、无墨水与另一元素或可见边框重叠。
- 结论：无缺陷，无观察项（见 PROOF-NOTE §7）。日志：`p7-nodediff.log`

## 9. 渲染字号与文字层（PyMuPDF，交付 PDF）

- 印 PDF 8 页，1462.5×2025 pt；网 PDF 8 页同版面
- 最小字号：P1 11.62 / P2 11.62 / P3 11.62 / P4 11.62 / P5 11.62 / P6 12.75 / P7 11.62 / **P8 9.75 pt**（≥ 9.75 pt 下限；两 PDF 逐页相同）
- tofu U+FFFD：印 0、网 0；pdftotext 各 47,419 B，`cmp` 逐字节相同
- 日志：`pdf-fonts.log`、`print.txt`、`web.txt`

## 10. 内容核查（程序 + 全文逐行通读）

- 模范文 99 词（80–100 内）；P7 金句 8 条各恰好 2×；题干编号 138 行 + 3 组匹配题 ×4 = 150；答案区 1–150 连续
- 匹配键：P2 c/b/d/a、P4 d/b/c/a、P8 d/c/b/a（SVG 渲染字母逐项核对一致）
- 日期/星期：`date`（Europe/Rome）核验全部星期表述一致；天数/算术自洽（24 球、13−11=2、6+7=13）
- 禁词 `Ucraina|Russia|Putin`：0；翻譯残留：0；VOL.5：文本导出 3 处、SVG 3 节点，均为合法节点
- SIMP_ONLY 国/学：Unicode 计数本版 0 次（8 SVG + 文本导出 + 源码）；核心 P1 各 1 次为中文家具
- fix3 B-1~B-9：新措辞各 1 次（text.md；D1/D2b/D2d/D11/P8a 另经 SVG 节点拼接核实 ×1）、旧措辞 0 次；缩短行首行 PIL 真墨右缘余量重测：P2 b +31.0 / d +40.2、P4 b +139.2 / c +17.5、P8 a +34.0 / b +51.5 / c +24.0 px，全部在栏内（日志 `fix3-check.log`、`fix3-svg.log`）
- 刊头带真墨：左 102.3、右 1778.9（版宽 1950），左右余量 102.3 / 171.1
- 标题数：font-size ≥ 30 px 节点 51 个（P1 22 / P2–P6 各 5 / P7 2 / P8 2），与备份旧版逐页相同；独立标题行 16 条（“56 titles”为幻数）
- core vs edition 源码 diff：差异行除 OUT 路径行外全部含 CJK（翻译替换），唯一非 CJK 差异为 P8 家具分隔符 `— PAGINA {pg} —` → `— {pg} ページ —`（读者语家具，预期行为）
- 字体：Newsreader 1136、Noto Sans CJK JP 627、Noto Serif CJK JP 295、UnifrakturMaguntia 1（较 proof2 少 6 节点 = P7 D-2 重排所致）
- 日志：`content-checks.log`、`titles-matching.log`、`fix3-check.log`、`fix3-svg.log`

## 11. 目视（交付印刷 PDF 渲染，200 dpi 逐页）

- P1–P8 全部看完：无溢出、无重叠、无压页脚、无豆腐块、无横向漫出、无图片与出处错位
- 渲染图：`render/p1.png` … `render/p8.png`（200 dpi 全页）、`render/p7-a2-crop.png`（新版 P7 A2 栏）、`render/p7-a2-crop-backup.png`（备份旧版同区）
- P5 词表跨栏断行、P7 三工具盒末行、P8 RISPOSTE 末行与页脚关系均目视确认（见 PROOF-NOTE §4）

## 12. 收工 SHA 再验

- 印 PDF `640a355a2943efe35b7c1437e1154a4012aa1ec51f18fff155fc7caa4e1c6666` / 28,221,020 B ✓
- 网 PDF `4f1bac2c12b8762c187a60647fec578f187f9f5150a2b65cfca31b474f00ee3f` / 1,901,668 B ✓
- 文本 `5ac2ecf5abb28bbc9f56c182572a9c7a7e4e93ae8b9c49b5468cc890e0ec16d7` / 58,165 B ✓
- core-it：0 文件被改动；生产目录 0 写入（mtime 仍为重扩散建版时间）

## 汇总

- gates.py：**19/19 PASS**
- freeze baseline：本版 8/8 + 核心 8/8
- 重渲印 PDF：逐字节相同
- occlusion：0 flags（新旧两版）；creambox：0 溢出；spill：0；孤儿扫：0；列溢出：0（真溢出）；STRADDLE：无缺陷
- p8：extract 150/150，compare CLEAN，keydiff [137, 138, 139]
- P8 最小字号 9.75 pt；§1.1 全过；日期星期全验；KIT §7/§12 三 SHA 与盘上一致；D-2 回归 A/B 全过
- **结论 (a) 零缺陷，可定稿**
