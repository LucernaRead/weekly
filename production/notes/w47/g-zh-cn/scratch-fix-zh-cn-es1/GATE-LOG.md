# GATE-LOG — W47 zh-cn-es fix1（机械门自跑全记录）

对象：`production/2026-w47/2026-w47-zh-cn-es/`。全部命令均在
`hidden_files/w47/scratch-fix-zh-cn-es1/` 内执行或以其为输出目录；
`TMPDIR=<scratch>/tmp`。工具栈：`tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3）。

## 开工核对

- 三 SHA 与任务书一致：
  印 `f05d6126a7f55564787be64e370de7ce05ade6abb38b18fbecc9cb2d070a2508` /
  44,799,104 B；网 `249ee578617c1c584f11ef2436d2438a41cf8c8b10b3e24baf3ff45b8396d437` /
  2,723,559 B；文 `edc045da1f0cc5267ec18046a193e055dfbf90e70421d79bcf0ba93f2497f482` /
  51,175 B。快照 `snapshot-before.sha256`（46 文件）。
- `hidden_files/w47/briefs/brief-coordinator.md` 不存在（无 `briefs/`
  目录）——已在 FIX-LOG 注明。

## 门 1 — 构建（run.py）

- 修前（scratch `build/`，OUT 重定向）：`build-pre.log`，rc=0，
  TOTAL 150，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；P2 col3 1167.45、
  P4 col3 1201.95、P5 col3 1241.1、P7 teaser 2588.78、P8 test flow
  994.5、P8 keys 2475.7。
- 修后干净重建（`build-fix1b.log`）：rc=0，TOTAL 150，0/0；全部 flow
  末值与修前相同。`build-fix1.log` 与 `build-fix1b.log` 除事故说明外
  一致（见 FIX-LOG“重建”）。
- `render.py`（`render-fix1.log`）：rc=0，8 卡 + 印 PDF 44,799,095 B，
  SHA `ba184b75daf1896bf528192e6adfad9d7f847bef57f16c43dc048461697c4182`。

## 门 2 — 标题横扫 + 双方法量测（D-1/D-2/D-3）

- `title_sweep.py`（PIL 真墨，Noto Sans CJK SC Bold 实测）：修前
  D-1 1420.0/−8.5、D-2 1910.5/−48.5、D-3 989.5/−28.5；
  修后 D-1 1403.0/+8.5、D-2 1853.5/+8.5、D-3 951.5/+9.5
  （`title-sweep-baseline.log`、`title-sweep-after.log`）。
- `pdf_right.py`（600 dpi 印 PDF 像素）：修前 D-1 1421.5/−10.0、
  D-2 1912.8/−50.8、D-3 991.9/−30.9；修后 D-1 1403.4/+8.1、
  D-2 1856.3/+5.7、D-3 954.2/+6.8（`pdf-right-D*-{pre,post}.png`）。
- 8 页全扫：其余标题修前修后均 ≥ +10；核心同位 PIL 复核
  +23.5/+82.5/+13.5（任务书 +22.0/+82.2/+12.5）。
- 逐档定字号：D-1 22（21 过度）、D-2 21（22 仍 −10.5）、D-3 21
  （22 仍 −10.5）——均为达标的最小降幅。

## 门 3 — 孤儿扫描（D-4）

- `orphan.py`：修前 P8 全页 1 处（y=912.4，`》，故事很有意思。…`）；
  核心 P8 0 处；修后 P8 全页 **0 处**（`orphan-after.log`）。
- `wrap()` 模拟：旧前缀 7 行 1 孤儿；`Modelo: ` 7 行 0 孤儿；
  `Respuesta: ` 7 行 0 孤儿；`Modelo de respuesta: ` 7 行 1 孤儿。
- 修后范文 7 行与模拟逐行一致，基线不变；MODELO 字符不变
  （freeze 差分增量仅重排行，见门 7）。

## 门 4 — 纵向奶油盒全扫

- `ink_check.py`（es-fr 版补 Noto Serif CJK SC）：35 盒。
  真盒内溢出（基线在盒内且余量 < +5）：修前 **0**，修后 **0**
  （`ink-baseline.log`、`ink-after.log`）。
- 8 处“盒下标题”抓取为已知误报类（+45px 窗口抓到盒下节标题），
  修前修后同一批、同值。D-1/D-3 盒纵向余量 43.0/41.0 修前修后不变。

## 门 5 — 几何遮挡审计

- `tools/occlusion_audit.py --selftest`：rc=0，六类全触发
  （`occlusion-selftest-after.log`）。
- `tools/occlusion_audit.py <fixed svg/>`：**0 flags**
  （`occlusion-after.log`）。附注：对 D-1~D-3 是空信号（BOXTITLE
  只认描边盒），真墨横扫见门 2/门 4。

## 门 6 — P8（p8.py）

- `extract --total 150`：**150/150**（`p8-extract-after.json/.log`）。
- `compare`（core P8 vs fixed P8）：**CLEAN**，missing=[] extra=0，
  uncertain=[]，keydiff=[]（`p8-compare-after.json/.log`）。

## 门 7 — freeze

- `baseline --build <edition> --core-svg <edition/svg>`：
  修前 **8/8**（`freeze-baseline-pre.log`），修后同步后 **8/8**
  （`freeze-baseline-post.log`）；核心完整性复核通过。
- `diff --core-svg core-zh-cn/svg --edition-svg <fixed svg/> --strict-cjk`：
  rc=0，TOTAL added CJK **0**（`freeze-diff-after.json/.log`）。
  修前修后差分增量仅 P8（范文重排 runs：前缀 + 行切分），其余 7 页
  差分相同；`cjk_added_total` 修前修后均为 `{}`。

## 门 8 — 文字层（印 vs 网）

- `pdftotext`（plain）：新印 45,052 B vs 生产网 45,062 B。
  词集差仅 D-4 段：新印多 `Modelo:` + 7 个重排行；网多
  `Respuesta`/`modelo:` + 8 个旧行（含 `》，故事很有意思。…`）。
  其余全同（`print.txt`、`web.txt`、`print-layout.txt`、`web-layout.txt`）。
- 结论：网 PDF 文字层仅 D-4 段过期，入仓前须用已修源码重建网 PDF。

## 门 9 — 字号与 §1.1（style_check.py）

- PyMuPDF 逐页 span：P1 10.50 / P2 11.62 / P3 11.62 / P4 11.62 /
  P5 11.62 / P6 12.75 / P7 11.62 / **P8 9.98pt**（≥ 9.75 底线，不变）。
- 纸 #fbfaf6 在位；fills 修前修后相同（非调色板色为既有图表/照片色）。
- VOL.4 ×9 / VOL.5 ×1（P7 下期预告，同核心）。
- 徽章：全部小徽章矩形内文字确为 A2/B1/B2（拉丁-only），8 页。
- CJK 可见字符 591 种（中文目标语版应有）；新增 CJK 0（见门 7）。

## 门 10 — SVG 几何差分（修前 → 修后）

- p1/p3/p6/p7：0 改动。p2：32 元全在 D-1 盒内（盒高 247→246、
  标题 23→22、3 行正文 y−1、文字内容同）。p4：1 元（标题字号
  24→21）。p5：7 元全在 D-3 盒内（盒高 168→166、标题 23→21、
  2 行正文 y−2）。p8：16 元全为范文重排 runs（7 行同基线、同字号）。

## 门 11 — 目视

- `crop-d1.png`（P2 盒）、`crop-d2.png`（P4 盒）、`crop-d3.png`
  （P5 盒）：标题全在奶油盒内、右缘留白清晰。
- `crop-d4.png`（P8 范文）：7 行，无孤儿，`《试探》，故事很有意思`
  收于行尾。

## 门 12 — 存活项复测

- P1 数字盒标题 +25.5（PIL）；P1 截稿行在位（P1 0 改动）。
- P4 gloss 6 行、框底 792.2、基线与核心逐值相同。
- P7 teaser 2588.78、P8 keys 2475.7（run 日志，修前修后同）。
- D4/D5 核心全同（p8 CLEAN，freeze CJK 0）。ABSTRACT.txt 335 B、
  尾换行在位，未动。

## 门 13 — 生产零写入核对

- 收工 `sha256sum -c snapshot-before.sha256`：仅 14 文件不同——
  4 源码、4 SVG（p2/p4/p5/p8）、4 卡片（p2/p4/p5/p8）、印 PDF、
  WEEKLY-KIT.md。其余 32 文件一致；网 PDF 与 text.md SHA 不变。
- 核心、其他版、工具、SOP 未动；未 commit、未 push。
