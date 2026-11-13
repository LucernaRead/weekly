# GATE-LOG — W47 zh-cn-es re-proof（fix1 后独立全量重校，机械门自跑全记录）

对象：`production/2026-w47/2026-w47-zh-cn-es/`。全部命令均在
`hidden_files/w47/scratch-reproof-zh-cn-es1/` 内执行或以其为输出目录；
`TMPDIR=<scratch>/tmp`。工具栈：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
前置记录 `scratch-fix-zh-cn-es1/` 仅参阅，不照抄结论。

## 开工核对

- 三 SHA 与任务书一致（开工与收工两次实测，全串一致）：
  印 `ba184b75daf1896bf528192e6adfad9d7f847bef57f16c43dc048461697c4182` / 44,799,095 B；
  网 `249ee578617c1c584f11ef2436d2438a41cf8c8b10b3e24baf3ff45b8396d437` / 2,723,559 B；
  文 `edc045da1f0cc5267ec18046a193e055dfbf90e70421d79bcf0ba93f2497f482` / 51,175 B。
  快照 `snapshot-start.sha256`（本版 46 个文件）；收工 `snapshot-end.sha256` 与之 0 差异。
- 源码行核对：`content12.py:187` tsize=22；`content34.py:176` 标题 21；
  `content56.py:25` tsize=21；`content8.py:104` 前缀 `Modelo: `。

## 门 1 — 构建（run.py，scratch 内重建）

- `build-reproof.log`：rc=0，TOTAL 150，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
  分布 A2 56 / B1 69 / B2 25；按页 10/18/18/18/18/18/12/38；
  类型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1。
  P7 teaser 2588.78、P8 test flow 994.5、P8 keys 2475.7，均与修前同。
- `render-reproof.log`：rc=0，8 卡 + 印 PDF 44,799,095 B，
  SHA `ba184b75daf1896bf528192e6adfad9d7f847bef57f16c43dc048461697c4182`——与生产印 PDF 逐字节一致。
- scratch 重建 SVG 与生产 `svg/` 逐字节比对：**8/8 MATCH**
  （p1/p2/p3/p4/p5/p6/p7/p8 全同）。

## 门 2 — 标题横扫 + 双方法量测（D-1/D-2/D-3）

- `title_sweep.py`（PIL 真墨，Noto Sans CJK SC Bold）：D-1 1403.0/+8.5、
  D-2 1853.5/+8.5、D-3 951.5/+9.5（`title-sweep-reproof.log`）。
  26 标题全扫：OVERFLOW/THIN 0；除三项外最小余量 P1 数字盒 +25.5，其余 ≥ +43.5。
- `pdf_right.py`（600 dpi 交付印 PDF 像素）：D-1 1403.4/+8.1、
  D-2 1856.3/+5.7、D-3 954.2/+6.8（`pdf-right-reproof.log`，裁图 `pdf-right-D{1,2,3}.png`）。
  双方法逐值与 fix1 声称相同；三项均 ≥ +5。
- 核心同位 PIL（`title-sweep-core.log`）：D-1 1388.0/+23.5、D-2 1779.5/+82.5、
  D-3 947.5/+13.5（任务书 +22.0/+82.2/+12.5，差 ≤ 1.5px 方法差）。

## 门 3 — 孤儿扫描（D-4）

- `orphan.py`（已适配修后前缀 `Modelo: ` 定位）：生产 P8 全页孤儿 **0 处**；
  核心 P8 0 处。范文 7 行，基线 816.2/840.2/864.3/888.3/912.4/936.4/960.5，
  行首 `》` 0 处（`orphan-reproof.log`）。
- MODELO 正文去前缀拼接后与核心逐字相同，138 字符（两边同）。

## 门 4 — 纵向奶油盒全扫

- `ink_check.py`（35 盒，PIL 墨底 + 生产 cards PNG 实渲）：真盒内溢出 **0**。
  与 fix1 `ink-after.log` 逐行相同（仅 8 个 `==` 路径行不同：fix1 跑 scratch 构建件，
  本次跑生产 svg，同字节）。8 处负余量行为已知误报类（+45px 窗口抓到盒下节标题），
  修前修后同一批。D-1 盒纵向余量 +43.0、D-3 盒 +41.0，修前修后不变
  （`ink-reproof.log`）。

## 门 5 — 几何遮挡审计

- `tools/occlusion_audit.py --selftest`：rc=0，六类全触发
  （`occlusion-selftest-reproof.log`）。
- `tools/occlusion_audit.py <生产 svg/>`：**0 flags**（`occlusion-reproof.log`）。
  附注：对 D-1~D-3 是空信号（BOXTITLE 只认描边盒），真墨横扫见门 2/门 4。

## 门 6 — P8（p8.py）

- `extract --total 150`：**150/150**（`p8-extract-reproof.json/.log`）。
- `compare`（core P8 vs edition P8）：**CLEAN**，missing=[] extra=0，
  uncertain=[]，keydiff=[]（`p8-compare-reproof.json/.log`）。
- P8 印键 vs REG：Q1–149 **149/149 一致**；Q150 REG 键 `(开放题，范文如下)`，
  P8 印出 `✓`，核心 P8 印出亦为 `✓`（`p8-extract-core.json`）。

## 门 7 — freeze

- `baseline --build <edition> --core-svg <edition/svg>`：**8/8 逐字节相同**
  （p2 `ebbe0a4e…` 与 fix1 修后基线一致；`freeze-baseline-reproof.log`）。
- `diff --core-svg core-zh-cn/svg --edition-svg <edition/svg> --strict-cjk`：
  rc=0，TOTAL added CJK **0**，`cjk_added_total={}`。逐页计数与 fix1 after 日志一致
  （p1 +45/−45、p2 +52/−52、p3 +39/−39、p4 +42/−42、p5 +38/−37、p6 +42/−41、
  p7 +106/−103、p8 +207/−213）；JSON 仅路径串不同
  （`freeze-diff-reproof.json/.log`）。

## 门 8 — 文字层（印 vs 网）

- `pdftotext`（plain）：新印 45,052 B vs 生产网 45,062 B。
  排序后行多重集差仅 D-4 的 7 行 vs 7 行（新印 `Modelo: …` 7 行新行切；
  网 `Respuesta modelo: …` 7 行旧行切，含孤儿行 `》，故事很有意思。星期日是小雪，天气更冷了，我`）。
  `Fechas de cine` 两边各 1 次，仅提取顺序不同。词集差亦仅 D-4 段。
  结论：网 PDF 文字层仅 D-4 段过期（build #3），入仓前须用已修源码重建网 PDF
  （`print.txt` / `web.txt` / `print-layout.txt` / `web-layout.txt`）。

## 门 9 — 字号与 §1.1（style_check.py）

- PyMuPDF 逐页 span：P1 10.50 / P2 11.62 / P3 11.62 / P4 11.62 /
  P5 11.62 / P6 12.75 / P7 11.62 / **P8 9.98pt**（≥ 9.75 底线）。
- 纸 #fbfaf6 在位；fills 与 fix1 after 日志逐值相同（非调色板色为既有图表/照片色）；
  VOL.4 ×9 / VOL.5 ×1（P7 下期预告，同核心）；CJK 可见字符 591 种。
  本日志与 fix1 `style-after.log` 逐行相同（`style-reproof.log`）。
- 徽章精确核对（本次自写核对，非 style_check.py 的过宽口径）：134 枚 60×30 矩形
  逐枚为 A2/B1/B2，填色与级别对应（A2 #5c6e30 / B1 #46581f / B2 #37402f）；
  P1 报头 `TEXTO CHINO　EXPLICACIONES EN ESPAÑOL` 无汉字；
  P6 另有 1 个 30×30 #37402f 空矩形为图表图例色块（旁 `7.77` / `亿件`），修前既有。
  注意：style_check.py 的 “badge non-ASCII hits” 列出的是橄榄条上的栏目标题，
  非徽章；fix1 GATE-LOG 称其为 none 与自身日志不符——版面本身无徽章问题，
  此条只记脚本口径问题（详见 PROOF-NOTE 记录项 1）。

## 门 10 — SVG 几何差分（修前 → 修后，以 fix1 `freeze-baseline-pre/svg` 为修前参照）

- p1/p3/p6/p7：0 改动（且与 fix1 修前快照 SHA 一致）。
- p2：32 元全在 D-1 盒内（盒高 247→246、标题 23→22、基线 237→236、3 行正文 y−1）。
- p4：1 元（标题字号 24→21）。
- p5：7 元全在 D-3 盒内（盒高 168→166、标题 23→21、基线 714.77→712.77、2 行正文 y−2）。
- p8：16 元全为范文重排 runs（7 行同基线、同字号）。

## 门 11 — 目视

- `crop-d1.png`（P2 日历盒）：标题全在盒内、右缘留白清晰。
- `crop-d2.png`（P4「看比赛」盒）：标题全在盒内、右缘留白清晰。
- `crop-d3.png`（P5 高频词盒）：标题全在盒内、右缘留白清晰。
- `crop-d4.png`（P8 范文）：7 行无孤儿，`《试探》，故事很有` 收于行尾。
  （裁图均取自生产 cards/，即交付渲染件。）

## 门 12 — 150 题手验

- `dump_reg.py`：edition 与 core 各导 150 项（n/page/level/type/key/note/body/opts）。
  比对：n、page、level、type、key、题干（全文与 CJK-only）、选项（全文与 CJK-only）
  **0 差异**（`reg-edition.json` / `reg-core.json`）。
- 语义搭配逐题读过：单选/完形单选键字母均在选项内；事实键逐条对过正文与注文；
  词汇配对 5 组键序 P2 a/b/c/d、P3 b/d/a/c、P4 d/b/c/a、P5 c/b/d/a、P6 c/d/a/b；
  Q150 开放题范文 138 字与核心逐字一致。
- 注文：仅 Q80 与核心相同（`悬疑 = suspense, b`），其余 149 条为西班牙语译文。

## 门 13 — 存活项复测

- D4/D5 措辞：`全球总决赛的BO5` 2/2、`GEN在S16一场没输` 2/2、
  `只丢了一小局` SVG 计 P1 1 + P4 1（两边同）、`淘汰赛一局没输` 1/1；
  旧措辞 `第一次在BO5里打赢` / `GEN今年一局没输` 均为 0。
- P1 数字盒标题 PIL +25.5；截稿行 `content12.py:86` 在位。
- P4 gloss 6 行、框底 792.2、基线 595.86…744.49 与核心逐值相同（`gloss-fonts.log`）。
- 字体族集合与核心同一（Noto Sans/Serif CJK SC、Newsreader、UnifrakturMaguntia ×1）；
  D5 句分段复查：拉丁 `GEN`/`S16`/`BO5` 走 Newsreader、中文走 Noto Serif CJK SC，
  与核心逐项同一，无异常字形——D5 只记录（`d4d5-notes.log`）。
- ABSTRACT.txt 335 B、尾换行在位；KIT 含新 SHA（两处）。

## 门 14 — 生产零写入核对

- 收工 `sha256sum -c snapshot-start.sha256`：**46/46 一致，0 文件不同**。
  本次复校未写生产任何文件；未 commit、未 push。

## 遗留文件（本 scratch 内）

`probe.txt`、`snapshot-start.sha256`、`snapshot-end.sha256`、`PROOF-NOTE.md`、`GATE-LOG.md`、
`title_sweep.py`、`pdf_right.py`、`orphan.py`、`ink_check.py`、`style_check.py`、`dump_reg.py`、
`build/`（scratch 构建副本 + SVG + 卡片 + 重建印 PDF）、`core-build/`（核心登记导出副本）、
`build-reproof.log`、`render-reproof.log`、`title-sweep-reproof.log`、`title-sweep-core.log`、
`pdf-right-reproof.log`、`pdf-right-D{1,2,3}.png`、`orphan-reproof.log`、`orphan-core.log`、
`ink-reproof.log`、`style-reproof.log`、`gloss-fonts.log`、`d4d5-notes.log`、
`p8-extract-reproof.json/.log`、`p8-compare-reproof.json/.log`、`p8-extract-core.json/.log`、
`reg-edition.json`、`reg-core.json`、`dump-edition.log`、`dump-core.log`、
`freeze-baseline-reproof/`、`freeze-baseline-reproof.log`、
`freeze-diff-reproof.json/.log`、`occlusion-selftest-reproof.log`、`occlusion-reproof.log`、
`print.txt`、`web.txt`、`print-layout.txt`、`web-layout.txt`、`print-sorted.txt`、`web-sorted.txt`、
`crop-d1.png`、`crop-d2.png`、`crop-d3.png`、`crop-d4.png`、`tmp/`。
