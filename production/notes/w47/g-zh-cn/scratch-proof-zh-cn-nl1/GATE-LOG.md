# GATE-LOG — 2026-W47 zh-cn × nl · proof1 机械门自跑汇总

- 校对：proof1；对象 `production/2026-w47/2026-w47-zh-cn-nl/`；核心对照
  `production/2026-w47/core-zh-cn/`；全部命令用 `tools/venv/bin/python`
  （Pillow 13.0.0 / FreeType 2.14.3）跑出，非转述他人结果。
- 工作区：`hidden_files/w47/scratch-proof-zh-cn-nl1/`。开工探针：
  `echo test | git hash-object -w --stdin` 成功 + scratch 写文件成功。

## 0. 三 SHA 先验（开工 / 收工一致）

| 文件 | SHA-256 | 大小 |
|---|---|---|
| `Lucerna-VOL4-NL.pdf` | f660072c047e1b5bab5a13956ec871db6976a47ddff49cc855615a8f55b42e4b | 44,049,080 |
| `Lucerna-VOL4-NL-web.pdf` | 495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac | 2,703,048 |
| `2026-w47-zh-cn-nl.text.md` | 41aa9a39371ab7dc75f828b24bb038f0f1b4f6e2f1a1fbe04cd9513eff09df2c | 50,082 |

## 1. freeze baseline（核心复现）—— PASS

`tools/freeze.py baseline --build production/2026-w47/core-zh-cn
--core-svg production/2026-w47/core-zh-cn/svg
--out scratch-proof-zh-cn-nl1/freeze-baseline`
rc=0；8/8 SVG 字节一致（p1–p8 全 OK）；核心完整性：交付核心 SVG 跑前后重哈希无变。

## 2. freeze diff --strict-cjk（核心冻结差分）—— PASS

`tools/freeze.py diff --core-svg production/2026-w47/core-zh-cn/svg
--edition-svg production/2026-w47/2026-w47-zh-cn-nl/svg
--strict-cjk --json scratch-proof-zh-cn-nl1/freeze-diff.json`
rc=0；每版增减串数 p1 +51/−47、p2 +52/−52、p3 +38/−38、p4 +42/−43、
p5 +36/−37、p6 +43/−41、p7 +101/−97、p8 +199/−202；
**TOTAL added CJK characters: 0**。

## 3. 版本重建（OUT 重定向到 scratch）—— PASS

- 复制整版到 `scratch-proof-zh-cn-nl1/rebuild/`，5 个 content 文件 OUT
  用 sed 改向 `…/scratch-proof-zh-cn-nl1/rebuild/svg`，改向前 grep 核实
  5 处 OUT 均已改向；`render.py` 的 BASE（指向生产目录）未被执行
  （只跑 `run.py` → content 文件），生产 SVG 无写入。
- `run.py` rc=0；TOTAL 150（A2 56 / B1 69 / B2 25；
  分版 10/18/18/18/18/18/12/38）；0 HEAD TOO WIDE；
  P7 teaser ends 2586.3；P8 keys flow ends 2491.1。
- 重建 8/8 SVG sha256 与交付版一致（`rebuild-svg-compare.txt` 全 MATCH）。

## 4. p8.py extract / compare —— PASS

- extract：noted set = 150/150（`p8extract.json`）。
- compare 核心 vs 本版：`CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`，
  rc=0（`p8compare.json`）。

## 5. 150 题 key 手验（自写 keycheck_nl.py，荷兰语前缀实测）—— PASS（1 处预期差异）

- stub_svg/stub_bslib 由同族方法复制进本 scratch；expl.E =
  `{'gloss_prefix': 'Notities｜', 'note_wrap': 'half'}`——前缀取自本版
  `bslib4.py` `gloss()` 内嵌值，P1/P2/P4 SVG 实测亦为 `Notities｜`。
- REG=150，stems=150；REG key 与 p8extract key 仅 1 处不符：
  Q150 REG `(开放题，范文如下)` vs 印出 `✓`（开放写作题截断式印法，预期内；
  范文实测 138 字，在 120–180 内）。
- 其余 149 题 key 与题干逐题手验配对无误（`keycheck-150.txt` 全 150 行已读；
  另见 PROOF-NOTE 手验小结）。Q56 = T1（题干「第一次在全球总决赛的BO5里」）。

## 6. occlusion_audit —— PASS（附空信号说明）

- 自检：planted classes 全触发 {'BOXTITLE':1,'COVER':1,'EDGE':1,'FOOTER':1,
  'LINEX':1,'TEXTX':1}，clean controls silent，rc=0。
- 本版：0 flags；核心：0 flags；NEW vs core：0。
- **空信号说明**：occlusion 只报墨与后画边框/遮盖的相交；纯填充奶油盒无边框，
  标题墨越盒边时不报。本次 3 处越边由第 7 项真墨横扫检出，occlusion 未报。

## 7. 奶油盒真墨横扫（自写 ink_sweep.py，复用 occlusion 的 parse_svg 真墨盒）—— FAIL ×3

全 8 版 40 个奶油盒逐盒测墨右缘到盒右缘余量；核心对照同扫，最紧余量 +10.25px，无负值。

| 页 | 盒 / 行 | 余量（墨−盒边） | 结论 |
|---|---|---|---|
| P5 | 盒标题「这一周的高频词 Woorden van de week」 | **−27.25 px**（PDF 文字层 −21.15pt；渲染像素 −19.4pt；zoom 见 render/p5-title-zoom.png） | FAIL |
| P2 | 盒标题「本周生活小日历 Data van deze week」 | **−1.75 px**（PDF advance −2.9pt；渲染像素 −1.2pt；zoom 见 render/p2-title-zoom.png） | FAIL |
| P1 | 日历盒末行「Sluiting: 10 nov. — de finale nog niet gespeeld」 | **−2.5 px**（300dpi 渲染像素 −1.02pt；zoom 见 render/p1-sluiting-zoom.png） | FAIL |
| P1 | 数字框标题「数字看本周 Deze week in cijfers」 | +21.0 px（盒内最紧行） | PASS |
| P4 | 「体育小日历 Sportdata」/「看比赛的中文 Wedstrijdwoorden」 | +32.2 / +13.5 px | PASS |
| P5 | 「电影小日历 Filmdata」 | +56.8 px | PASS |
| 其余 | 全部奶油盒 | 最紧 +13.5 px 以上（除上述 3 处） | PASS |

KIT 称 P2 标题“ends x = 1413.2, 26.3 px clear”——1413.2 与我实测墨右缘一致，
但 26.3px 是到照片（x=1439.5）的距离；盒边为 1411.5，故仍越边 1.75px。

## 8. 行首孤儿引号扫描（交付 PDF 文字层逐行，全 8 版）—— FAIL ×1（P1）/ P8 通过

- P1 唯一一起：行以 `》` 起首，`》gaat in première`，
  bbox x=417.4–549.5pt, y=1007.4–1029.0pt（数字框第 3 行）；核心 0 起。
- P8：无行以 `》`/`」`/`）`/`”` 起首；范文《试探》均在行中。

## 9. P8 最小字号 / 网 PDF 文字层 —— PASS

- PyMuPDF：印 PDF 8 页；P1 最小 10.50pt，P2–P5/P7 11.62pt，P6 12.75pt，
  **P8 最小 9.98pt**（≥ SOP §1.1 底线 9.75pt）。
- `pdftotext`：网 PDF 44,234 B，印版 44,234 B；去空白后逐字一致；各 8 页。

## 10. 日期 / 事实抽查（公开来源 + `date -d`）—— PASS

- `date -d`：11月1日周日、4日周三、5日周四、6日周五、7日周六、8日周日、
  9日周一、14日周六、15日周日、21日周六、22日周日，与文内全部一致。
- 公开来源核实：S16 赛果（瑞士轮 GEN 2–1 LYON、QF/SF 全部比分、决赛时间地点）、
  小雪 2026-11-22 15:23/农历十月十四/第20节气、深圳读书月第27届七场馆与
  11月7日国际美术馆日、《试探》定档 11月21日与主创剧情——均与正文相符。
  详见 PROOF-NOTE“通过项”。

## 11. 其余自跑核对 —— PASS

- 8 条本周金句在 8 版 SVG 合并文本中各出现恰 2 次。
- U+2019（’）在全部 SVG 与 .text.md 中为 0。
- “Double 11”核心 P6 SVG 亦有 2 处，属继承非泄漏。
- .text.md 第 1 行起为导出体例；ABSTRACT.txt 316 B，荷兰语，含 VOL.4 与本周主题。
- P8 芯片计数：A2 11 / B1 24 / B2 3 = 核心。
- P1 绿带右端 span 最右 1375.8pt < 带边 1396.5pt；全版 8 页已渲染目视
  （render/p-1.png … p-8.png），除第 7 项 3 处越边与第 8 项 1 处孤儿引号外，
  无溢出、重叠、压页脚。

## 12. 生产零写入核对 —— PASS

收工 `sha256sum -c opening-snapshot.sha256`：41/41 OK，0 差异；
三 SHA 与开工值相同；`git status` 在两生产目录下无修改文件
（仅 pre-existing 未跟踪项）。

## 总 verdict

机械门：freeze / 重建 / p8 / keycheck / occlusion / 字号 / 文字层 / 日期事实
全过；**真墨横扫 FAIL ×3 + 孤儿引号 FAIL ×1** → 本版结论 (b)，见 PROOF-NOTE.md。
