# GATE-LOG — 2026-W47 it-ja proof2（重扩散后独立复校）

- 对象：`production/2026-w47/2026-w47-it-ja/`（重扩散新版）
- 工具链：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`TMPDIR=<scratch>/tmp`；`PYTHONDONTWRITEBYTECODE=1`
- 全部命令的输出文件均在本 scratch 内；生产文件未被有意修改（O1 披露的字节一致重写见 PROOF-NOTE §5）

## 0. 探针与 SHA（开工前）

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0
- scratch 真实写文件：`probe.txt` 写入并读回成功
- 印 PDF `279962b7b3ae203049e1646d81c737228309aff0b864fef94079f4cc81ddb319` / 28,221,039 B ✓
- 网 PDF `4df33c6917da1b4452d8f8aa7574eb47d70161a074c0b30424cbb684ab007a7b` / 1,901,688 B ✓
- 文本 `bf64b304305e5d6e0679a9816c6b95576709c47e30dd69aa4cc6b24bf6def634` / 58,186 B ✓
- 收工时三件 SHA 再验一次，仍一致（见 §9）

## 1. run.py（副本内运行，见 O1）

- RC=0；TOTAL 150；级别 A2 47 / B1 70 / B2 33；页分布 10/18/18/18/18/18/12/38；模范文 99 词
- `FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE` 出现 0 次
- `flow[P8-keys] ended col 3/3 y=2546 (bottom 2552)`；P8-ex 末端 y=870（底边 1332）
- 日志：`run.log`

## 2. SVG 重建 8/8 字节一致

- 副本重建的 8 个 SVG 与交付 `svg/` 逐个 `cmp`：p1–p8 全部 IDENTICAL
- `tools/freeze.py baseline --build <本版副本> --core-svg <本版 svg>`：**8/8 byte-identical**，RC=0（重定向文件：render.py + content12/34/56/7/8；日志 `freeze-baseline.log`，hash deac8b03…/84c1ee1e…/12d90f5a…/bcdc0a85…/da33507d…/aa94f7a1…/d9f8fa3d…/fa82b32e…）
- `tools/freeze.py baseline --build <core-it> --core-svg <core-it svg>`：**8/8 byte-identical**，RC=0（日志 `freeze-baseline-core.log`）；核心完整性自验通过，core-it 0 文件被改动

## 3. 重渲印 PDF 逐字节相同

- 副本内 `render.py` RC=0；重渲印 PDF sha256 `279962b7b3ae203049e1646d81c737228309aff0b864fef94079f4cc81ddb319`，与交付一致（28,221,039 B）
- 日志：`render.log`

## 4. gates.py 19/19 PASS（独立重跑；harness 由 fan-out 的 gates.py 复制、输出路径改到本 scratch）

| # | 门 | 结果 |
|---|---|---|
| 1 | occlusion 0 flags | PASS（0 flags） |
| 2 | p8 extract noted count | PASS（noted=150 rc=0） |
| 3 | p8 compare vs core | PASS（verdict=CLEAN keydiffs=[137, 138, 139]） |
| 4 | freeze diff fragments explained (P1-7) | PASS（unexplained_add=[] unexplained_rem=[]） |
| 5 | freeze diff report present | PASS（pages=['1'..'8']） |
| 6 | print/web text multiset identical | PASS（print_words=6749 web_words=6749 chars_equal=True） |
| 7 | web PDF < 7MB | PASS（1,901,688 bytes） |
| 8 | print PDF size sane | PASS（28,221,039 bytes） |
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

INFO：'·' 总出现 148 次（均在选项串/讲解串/词表内，见 §7）。
首轮误报说明：第一次跑 gates.py 时 3 项 FAIL（p8 extract / p8 compare / freeze diff report），原因是 harness 复制后缺少 `ja/` 输出子目录（p8.py 与 freeze.py 写 JSON 失败 rc=1），与内容无关；建目录后重跑即 19/19 ALL PASS（RC=0）。日志：`gates.log`。
freeze diff 原始输出：P1 +61/−39、P2 +31/−28、P3 +30/−28、P4 +27/−26、P5 +44/−39、P6 +26/−25、P7 +41/−39、P8 +305/−376；新增 CJK 合计 3,054 字（日志 `freeze-diff.json`，本 scratch `ja/` 下）。

## 5. 奶油盒 PIL 真墨扫（canonical creambox.py + 窄带交叉）

- canonical `hidden_files/w47/tools/creambox.py`（+45px 窗口 + 逐行表 + P7 汇总）：29 盒；盒内末行基线 clearance 全部 ≥ +4.5 px
  - 最小值：P2 解説盒 +5.3、P3 词表盒 +5.3、P4 E TU 盒 +4.5、P5 E TU 盒 +4.5、P7 LA PAROLA +4.5、P7 LETTERE +5.1
  - P7-TOOLBOX 汇总：3 盒，min inside clearance +4.5，min desc-clear −1.5
  - 7 处 desc-clear 负值（−0.9 ~ −1.5）：末行文字逐一核查均不含下行字母——P2 `della musica e dei musicisti.`、P3 `continua fino al 6 dicembre.`（无 g/j/p/q/y）与 5 处日语句；渲染图确认末行在盒内留有空隙，非真实漫出
  - BELOW-WINDOW 行 12 条：全部为下一区块栏头/表行（P1 +24、P3 +37、P4 +26~+40、P6 +42），已知假阳性形态
- `tools/creambox_check.py`（0–8 px 窄带）：**NO OVERFLOW**
- 日志：`creambox.log`、`creambox-check.log`

## 6. spill 扫查（`spill_sweep.py`，由 scratch-proof-nl-en1 适配，页名改 it-ja）

- RC=0。候选 BELOW/ABOVE/SIDE 全部裁定为非溢出：
  - BELOW +24~+55：下一区块栏头（P1 LA PAROLA、P3 IL TORRAZZO、P6 ESERCIZI）、P4 结果表行、P5 解説行（+50.5，盒外下一区块）
  - ABOVE：各盒上方的图注/上一区块末行（−16 ~ −59）
  - SIDE：P4/P6 双栏图表的另一半盒内文字（PROPOSTA 盒 4 行、MINIME 盒内文字），非溢出
- 真溢出：**0**。日志：`spill-sweep.log`

## 7. 孤儿扫查（`orphan_sweep.py`，由 scratch-proof-nl-en1 适配：页名 it-ja、JP 字体、定向检查改为文本导出面的「翻訳」标签）

- 1439 行：[PIL-advance] class-a=0 class-b=0；[svglib-advance] class-a=0 class-b=0；逐页全 0
- 暴力复核：17 个以闭合标点起首的 `<text>` 元素，行首者（leftmost）**0**（其余为行中续接的 `：`/`）`/`」`元素）
- E 标签定向检查：文本导出 翻訳=4、翻譯=0（Q137–140，L969/971/973/975）
- 日志：`orphan-sweep.log`（JSON：`ja/orphan-sweep-fix5b.json`）

## 8. 列溢出扫查（`colspill_scan.py`，由 scratch-proof-ru-ja1 适配，页名改 it-ja）

- RC=0。原始命中约 40 处，逐项裁定全部为假阳性，见 PROOF-NOTE O6：
  - 双栏通栏元素（P1 头条/导语、P2 跨栏段、P4 表头/预览段、P6 图表带、P7 FRASI 引用、P8 RISPOSTE 带）
  - 栏头带 + 日语讲解（P1 +45、P2 +47.2）
  - `text-anchor=middle` 居中家具（各页 `答えは8ページ…` 行，+450.4 为锚点误读）
  - 表元/指示语伸入 28 px 栏间隙：P4 表格第二列 +10~+30、匹配题指示语 `単語と意味を合わせなさい` +7.5（P2/P4/P6/P8 各一处）、P7 +1.5——目视确认未触及相邻栏内容
- 真溢出：**0**。日志：`colspill.log`

## 9. 渲染字号与文字层（PyMuPDF，交付 PDF）

- 印 PDF 8 页，1462.5×2025 pt；网 PDF 8 页同版面
- 最小字号：P1 11.62 / P2 11.62 / P3 11.62 / P4 11.62 / P5 11.62 / P6 12.75 / P7 11.62 / **P8 9.75 pt**（≥ 9.75 pt 下限）
- tofu U+FFFD：印 0、网 0；字符数印/网各 37,813
- 日志：`pdf-fonts.log`

## 10. 内容核查（程序 + 全文逐行通读）

- 模范文 99 词（80–100 内）；P7 金句 8 条各恰好 2×；题干编号 138 行 + 3 组匹配题 ×4 = 150；答案区 1–150 连续
- 匹配键：P2 c/b/d/a、P4 d/b/c/a、P8 d/c/b/a（SVG 渲染字母逐项核对一致）
- 日期/星期：`date`（Europe/Rome）核验 16 组星期表述全部一致；天数/算术自洽
- 禁词 `Ucraina|Russia|Putin`：0；翻譯残留：0；VOL.5：文本导出 3 处、SVG 3 节点，均为合法节点
- SIMP_ONLY 国/学：Unicode 计数本版 0 次（8 SVG + 文本导出 + 源码）；核心 P1 各 1 次为中文家具
- fix3 B-1~B-9：新措辞各 1 次、旧措辞 0 次；缩短选项首行真墨右缘余量 +17.5 ~ +139.2 px（日志 `fix3-ink.log`）
- 刊头带真墨：左 102.3、右 1778.9（版宽 1950），左右余量 102.3 / 171.1
- 标题数：font-size ≥ 30 px 节点 52 个；独立标题行 16 条（“56 titles”为幻数）
- core vs edition 源码 diff：差异行除 OUT 路径行外全部含 CJK（翻译替换），唯一非 CJK 差异为 P8 家具分隔符 `— PAGINA {pg} —` → `— {pg} ページ —`（读者语家具，预期行为）
- 字体：Newsreader 1141、Noto Sans CJK JP 627、Noto Serif CJK JP 296、UnifrakturMaguntia 1
- 日志：`content-checks.log`、`titles.log`、`fix3-ink.log`

## 11. 目视（交付印刷 PDF 渲染，半尺寸逐页）

- P1–P8 全部看完：无溢出、无重叠、无压页脚、无豆腐块、无横向漫出、无图片与出处错位
- 渲染图：`half-p*.png`（本 scratch）、`contact-sheet.png`
- P5 词表跨栏断行、P7 三工具盒末行、P8 RISPOSTE 末行与页脚关系均目视确认（见 PROOF-NOTE §2）

## 12. 收工 SHA 再验

- 印 PDF `279962b7b3ae203049e1646d81c737228309aff0b864fef94079f4cc81ddb319` / 28,221,039 B ✓
- 网 PDF `4df33c6917da1b4452d8f8aa7574eb47d70161a074c0b30424cbb684ab007a7b` / 1,901,688 B ✓
- 文本 `bf64b304305e5d6e0679a9816c6b95576709c47e30dd69aa4cc6b24bf6def634` / 58,186 B ✓
- core-it：0 文件被改动

## 汇总

- gates.py：**19/19 PASS**
- freeze baseline：本版 8/8 + 核心 8/8
- 重渲印 PDF：逐字节相同
- occlusion：0 flags；creambox：0 溢出；spill：0；孤儿扫：0；列溢出：0（真溢出）
- p8：extract 150/150，compare CLEAN，keydiff [137, 138, 139]
- P8 最小字号 9.75 pt；§1.1 全过；日期星期全验；KIT §1 三 SHA 与盘上一致
- **结论 (a) 零缺陷，可定稿**
