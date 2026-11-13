# GATE-LOG — 2026-W47 zh-cn-de 独立复校（re-proof / fix1 后）

- 版：`production/2026-w47/2026-w47-zh-cn-de/`；核心：`production/2026-w47/core-zh-cn/`
- 复校：2026-11-11 13:13–13:45 EST；工作区 `hidden_files/w47/scratch-reproof-zh-cn-de1/`
- 工具：`tools/venv/bin/python`（共享工具）；`pdftotext`、`git` 仅读
- 结论：**11/11 门通过；缺陷 (a) 无**

## 0. 开工探针与 SHA（先验值均相符）

- 探针：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 写文件成功。
- 印 PDF `b38ffe40ae07b2502766d553d33e50d414d6210288c852ed961259cc2ee97279` / 44,829,877 B ✓
- 网 PDF `ecd253809c7c4c331a3093dd808fd06337307fb170dc0c0d8a2ab39f79aeaa81` / 2,732,386 B ✓
- 文 `51d6dab11f8b9d857790b8e1c1aba6c5e34259f3eb4b77a19ad77d24106e0a1e` / 50,628 B ✓
- 核心印 `c34f5a54e491a085ea3e19a986748938dda79294b90d154a8e746f54a9eb05aa` / 41,763,115 B ✓
- 核心网 `6b7a12f517749738de2028569556be326aabe00ab556ac3ec8e59cc936a263d9` / 2,632,446 B ✓
- 核心文 `23fb62bd7763c59392c05ba7e03f64ad8f521352d464d6ac293d2190c4d0bf04` / 49,435 B ✓
- 开工快照：87 文件 SHA 存 `snapshot-start.sha256`。

## 1. run.py（`run-rebuild.log`）

- 方法：整版复制至 `scratch-reproof-zh-cn-de1/rebuild/`，5 处 `OUT` sed 重定向进副本 `svg/`（逐行验过；
  `render.py` 生产 BASE 未执行）；`tools/venv/bin/python run.py`。
- 结果：**rc=0，TOTAL 150**；A2 56 / B1 69 / B2 25；按页 10/18/18/18/18/18/12/38；
  类型：完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1；FLOW OVERFLOW / HEAD TOO WIDE 0。

## 2. SVG 重建（`svg-rebuild-compare.log`）

- `cmp` 逐枚：p1–p8 **8/8 IDENTICAL**。

## 3. freeze baseline（`freeze-baseline.log`）

- 命令：`freeze.py baseline --build ../production/2026-w47/core-zh-cn --core-svg ../production/2026-w47/core-zh-cn/svg --out <scratch>/freeze-baseline`
- 结果：rc=0，**8/8 SVGs byte-identical**；`core integrity: shipped core SVGs unchanged by the run`。

## 4. freeze diff --strict-cjk（`freeze-diff.log` / `freeze-diff.json`）

- 命令：`freeze.py diff --core-svg <core>/svg --edition-svg <ed>/svg --strict-cjk`
- 结果：rc=0；p1 +47/−45、p2 +54/−52、p3 +39/−39、p4 +42/−43、p5 +36/−38、p6 +44/−41、p7 +106/−97、p8 +206/−210；
  **TOTAL added CJK characters: 0**。

## 5. occlusion audit（`occlusion.log` / `occlusion.json`）

- 自检：`--selftest` rc=0，6 类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1，clean 对照静默）。
- 版：`0 flags`；core：`0 flags`；NEW vs core：**0**。rc=0。

## 6. p8 extract + compare（`p8extract-ed.log` / `p8extract-core.log` / `p8compare.log`）

- extract `--total 150`：版 150/150、核心 150/150。
- compare `--core-dir … --edition-dir … --target zh-cn --total 150`：rc=0，
  **status: CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**。
  （注：首次 compare 漏 `--total` 得 rc=2 用法错，已补参数重跑，rc=0。）

## 7. 150 题逐题手验（`verify150.py` / `verify150.log` / `verify150.json` / `reg.json`）

- 方法：AST 解析 content12/34/56/7/8 全部 `ex`/`match_set` 调用（130 + 5 组×4 = 150），
  逐题比对源码 key = REG key = P8 版印 key = P8 核心印 key；题干/选项/配对右项逐一在当页 SVG 文本中定位；
  完成句子验 `___`、单选 key∈A–D、配对 key∈a–d。
- 结果：**150/150**，题干全部在页，仅 1 项说明：
  #150 写作开放题 REG key `(开放题，范文如下)` vs P8 印 `✓`——核心 P8 同样印 `✓`，
  compare CLEAN，属既定渲染惯例，非缺陷。

## 8. 印/网文字层逐页差（`textlayers/diff.log`）

- `pdftotext` 两版各 44,729 字节；去空白逐页比对 8/8 页逐字相同
  （字符数 2377/2411/1828/2224/1880/2254/3109/7648），**差 0**。

## 9. P8 最小字号（`p8-fontsize.log`）

- PyMuPDF 读 P8：印版最小 **9.98pt**、网版 9.98pt、核心印版 9.98pt；
  SOP §1.1 底线 9.75pt，**通过**。

## 10. D1 重测（`d1-svg-geometry.log` / `d1d2-pil.log` / `d1-render-pixels2.log` / `d1-gap-profile.log`）

- 源码 `content12.py:187`：`f.box("本周生活小日历　Wochenkalender", [`，23pt；`Kalender der Woche` 0 次。
- SVG：盒 rect x=989.0 w=422.5 → 右缘 **1411.5**；标题 x=1007.0 y=237 fs=23 Noto Sans CJK SC Bold。
- PIL 真墨（NotoSansCJK-Bold.ttc face SC=2, size 23）：新标题右缘 **1383.0**，余量 **+28.5px**；
  旧标题 1418.0 / −6.5px（复现 fix1 前值）。
- 印 PDF 150dpi 渲染：标题墨最右缘 1381.8 svg px，余量 **+29.7px**；
  盒右缘外间隙条带（render x 2206–2248）暗像素 **0**（x=2249 单列为右侧照片左缘）。
- 裁图 `render/crop-p2-calendar.png` 目视通过。**余量 ≥ +5px，PASS。**

## 11. D2 重测（`d2-geometry.log` / `d2-wrap-sim.log` / `d1d2-render-pixels.log`）

- 源码 `content12.py:50`：`der Film 《试探》 startet`，无 `neue`。
- P1 SVG：y=1339.265 行 `21. Nov., Samstag — der Film 《试探》`（墨右缘 905.3 < 盒右缘 961.0）；
  y=1366.265 行仅 `startet`。渲染像素盒外 0；裁图 `render/crop-p1-filmbox.png` 目视通过。
- `svglib.wrap` 同款模拟：旧串折为 `…《试探` / `》 startet`（旧 `》` 行首属实），
  新串折为 `…《试探》` / `startet`。
- 全期 1205 可视行：行首闭标点 **0**、**`》` 行首 0**、行末开标点 0。
  「31→30」未附计数定义无法复现（唯一恰得 30 的口径为行末接续标点 ，10+、3+—17=30，
  该口径下 D2 改动不产生差值），不列为结论依据；实质缺陷消除已证。**PASS。**

## 附加核查（非门，见 PROOF-NOTE）

- badge：`德语讲解` text.md + 8 SVG = 0 次；仅 P1/P2 变化证据链见 PROOF-NOTE §2
  （content12.py 17:36 唯一修复时段触碰；git 基线不存在，两目录 untracked）。
- 核心 D4/D5：`全球总决赛` 限定在场（text.md:695, :815）；`GEN在S16一场没输`（:37, :697）；
  核心中文 1414 纯 CJK 行与德版多重集一致，71 条 `___` 题干一致。
- 全文通读 2102 行 + 星期/农历/节气/数字自洽 + 范文 138 字 + 金句溯源 + 8 版渲染目视：零问题。
- `brief-coordinator.md` 不存在（无 `briefs/` 目录），SOP 无 §8.4 编号（按 §8 全文执行）——已记录。

## 收工生产零写入核对

- `snapshot-end.sha256` vs `snapshot-start.sha256`：**diff 为空，87/87 文件一致**；
  三交付件 SHA 收工复核与开工相同。
