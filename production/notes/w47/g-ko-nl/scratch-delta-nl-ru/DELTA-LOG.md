# DELTA-LOG — 2026-W47 nl-ru, core fix3 + fix4 + fix5 同步

- 版：`2026-w47-nl-ru`（荷兰语目标 × 俄语读者版），VOL.4，8 版，150 题
- 日期：2026-11-11
- 任务：core-nl fix3（D6/D7）+ fix4（D8/D9/D10）+ fix5（D11）同步到本版。
  只改本版自己的源文件，不碰核心、不碰其他版、不碰 staging。不 commit、不 push。
  修后由另一位独立校对员 proof1，不要自己定稿。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-ru/`
  （日志、门禁证据、registry、比对 JSON、crops 均在此）
- 工作区：repo 克隆 `~/workspace/weekly-git`；解释器 `tools/venv/bin/python`；
  TMPDIR = 本 scratch 目录
- 核心对照（只读）：`production/2026-w47/core-nl/`，FIX-LOG.md 通读——
  fix3 第 412 行起（D6/D7）、fix4 第 185 行起（D8/D9/D10）、fix5 第 3 行起（D11）。
  机制照搬核心，w 数值一律在本版用 0.1px 步进 width scan 重算（核心数值不抄）。
  另参考 sibling 试点 `scratch-delta-nl-de/DELTA-LOG.md` 与 nl-es/nl-fr 的门禁脚本
  （gates_delta.py、orphan_sweep_delta.py、p8compare_delta.py、check_creambox、
  spill_sweep、probe_cream_d11、boxtitle_inkscan v1/v2——均已按 ru 版改写路径与针）。

## 0. 开工探针与规范路径

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29b…`，
  RC=0；`/dev/null` 正常（字符设备）。goals-side scratch 真实写文件 `probe.txt` OK。
- **规范路径 `production/2026-w47/2026-w47-nl-ru/` 在开工时不存在**（与 nl-de 试点
  相同情况）。处理：把 staging `fanout-nl/2026-w47-nl-ru/` 整目录 `cp -a` 到规范路径，
  `diff -r` 校验**完全一致**（仅两条无害的 ownership 保留警告）；staging 副本全程未动，
  收尾时三 SHA 复核仍为任务给定值（见 §8）。
- 修前身份核对（三件 SHA，实测 = KIT build-5 值 = 任务给定值）：印
  `f945029d3a736dd3d139c555a4693283dc3aa9feba732edc91805b556ff889c2` /
  12,718,382 B；网 `e5e3d5d3fd36b767858c96cafce0b4bf317f7ed2fd62a605aaa7eed327352724`
  / 1,661,354 B；文 `558786fc6247329c319fd1cf965e458ec32cea1daf3d7ae534f02c9804829273`
  / 57,848 B。修前 8 个 SVG SHA 存 `pre-svg-sha.txt`；修前 `run.py` 重跑 8/8 字节一致，
  TOTAL 150，0 溢出——基线可复现。

## 1. 修前实测：D6/D7/D8/D10 在本版并不存在；D9 两处同错；D11 是真缺陷

俄语读者层文字与核心中文桥接文字断行不同——修前 SVG 实测：

| 点 | 修前 SVG 实测 | 结论 |
|---|---|---|
| D6 P3 桥接 | 3 行：`Заполни в перфекте. Следи за` (2303.5) / `вспомогательными глаголами` (2333.225) / `hebben/zijn.` (2362.95)，句末 `.` 在行 3 末尾 | 无孤儿 |
| D7 P7 桥接 | 3 行：`de wedstrijd матч; de groepswinst победа в` (725.66) / `группе; de kwartfinale четвертьфинал;` (755.385) / `scoren забивать.` (785.11) | 无孤儿 |
| D8 P6 图注 | 4 行：`Учебные данные: выдуманные числа,` (635.02) / `только для упражнения, не настоящий` (659.44) / `опрос. Вопрос: что ты кладёшь в` (683.86) / `ботинок? (100 молодых людей)` (708.28) | 无行首标点 |
| D10 P7 来信 | 2 行：`Писем и лучших текстов не поступило` (1783.27) / `— образец; обещание на VOL.5.` (1811.67) | 无行首标点 |
| D9 Q140 | registry 键、text.md:415 答案、P8 节点三源同错：键 `Ik maak een surprise met een gedicht.`（缺 `kort`）；题干 `Я делаю сюрприз со стихотворением.`（缺“小”） | **真缺陷，两处同修** |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=611.0>` 底 1202.6；末行 `18:45 uur.` 基线 y=1209.49，**盒底外 +6.89px** | **真缺陷** |

全版孤儿标点横扫（修前，双类，CJK + 拉丁标点，PIL + svglib 双 advance，1464 行）：
(a) 独行标点 0，(b) 行首标点 0，8 页全 0；brute-force 以标点开头的 `<text>` 元素
67 个、leftmost 0 个（均为行中片段：P8 答案区 `:` / `)` / `,` 定位符、P1/P5 `:` 等，
无一居行首）。因此 D6/D7/D8/D10 的同步是**结构性**的：机制照搬 + 本版文字重算 w，
选出的 w 必须**精确复现当前干净断行**（行内容、行数、基线全不变），重建 SVG 以
p3/p6/p7 字节一致为证。D9、D11 是真修。
修前 p8 compare：CLEAN，keydiff [137, 138, 140]。D9 的 140 预期修后移出该表。

## 2. Width scan（本版自己的文字 + 本版 `svglib.wrap()`，0.1px 步进）

CW = 422.5。取“精确复现当前各行”的 w 区间（含当前 w 的连续段）中点
（核心数值一律不抄；`width_scan.py` + `width-scan.log`）：

| 点 | 文字（字体/字号） | 当前 w | 区间（同行内容） | 选中 w |
|---|---|---|---|---|
| D6 桥接 | `Заполни в перфекте. Следи за вспомогательными глаголами hebben/zijn.`（sans 20.5） | CW=422.5 | 304.3–427.8（3 行） | **366.05**（中点） |
| D7 桥接 | `de wedstrijd матч; … scoren забивать.`（sans 20.5） | CW=422.5 | 419.8–451.9（3 行） | **435.85**（中点） |
| D8 图注 | `Учебные данные: … (100 молодых людей)`（sans 18.5） | CW−44=378.5 | 353.1–385.5（4 行） | **capcn_w=369.3**（中点） |
| D10 来信 | `Писем и лучших текстов не поступило — образец; обещание на VOL.5.`（sans 20） | CW−44=378.5 | 373.2–395.4（2 行） | **dt_zh_w=384.3**（中点） |

宽度安全核对（`text_w` 实测行宽，非估算）：
- D7 行 1 `de wedstrijd матч; de groepswinst победа в` 实测 419.78px ≤ CW 422.5——
  w=435.85 只放宽换行阈值，渲染出的行本身仍是 419.78px，栏内余 2.72px，无越栏。
  （区间下沿 419.8 即行 1 行宽；上沿 451.9 之上换行改变。）
- D8 行 1 实测 339.08px，末端 ix+22+339.08=1822.58，盒右沿 1862.0 内 39.4px。
- D10 行 1 实测 373.11px，末端 bx+22+373.11=1856.61，盒右沿 1862.0 内 5.39px
  （与修前渲染相同，w 只改变换行阈值、不改变行内容）。
- D6 行 1 实测 304.22px（区间下沿 304.3 即行 1 行宽）。

D11 事实句（serif 21.5，CW−44）：5 句断行 3/3/3/2/3 = 14 行，与核心一致；
`sh` 旧 611.0 → 新 638.0（+27）。顶留 89 = 16（pad）+ 52（标题块）+ 21
（para y-offset），本版 `content34.py` 渲染循环形状与核心相同（`yy3 = sy3+16`、
标题后 `yy3 += 52`、事实 `p.para(…, yy3+21, …)` + 12）。推导复核：首事实基线
sy3+89=680.6（SVG 实测 680.6 ✓）；fact 间步进 = n×30.53 + 33（+12 循环 gap
+21 下一 para y-offset）；模拟末行基线偏移 617.89，**与 SVG 实测 1209.49−591.6
= 617.89 完全一致**。旧余量 611−617.89 = −6.89px；新余量 638−617.89 = +20.11px。
（注：width_scan.py 第一版模拟只算了 +12 gap，得 533.89，已修正为 +33 并与
SVG 逐行基线 680.60/805.19/929.78/1054.37/1148.43/1209.49 逐一核对——
日志以 SVG 实测为准。）

## 3. 改动源码行前后对照（仅 5 个源文件 + KIT）

`diff -r`（规范路径 vs staging 副本，排除 svg/cards/PDF/text.md）只显示以下 5 文件：

### `bslib4.py` — D6 机制（照搬核心 fix3 的 `w` 机制）
```diff
-    def para(self, s, size=24, kind="serif", bold=False, fill=INK, lh=1.52, gap=10, split=True, italic=False):
+    def para(self, s, size=24, kind="serif", bold=False, fill=INK, lh=1.52, gap=10, split=True, italic=False, w=None):
+        # w: optional wrap-width override (default: column width). Synced
+        # from core-nl fix3 (D6/D7): lets one bridge call pin its wrap
+        # width without touching the column width.
+        w = self.w if w is None else w
         if not split:
-            h = self._ph(s, size, kind, bold, self.w, lh, italic)
+            h = self._ph(s, size, kind, bold, w, lh, italic)
             self._fit(h + gap)
-            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, self.w, lh, italic=italic) + gap
+            self.y = self.p.para(self.x, self.y + size, s, size, kind, bold, fill, w, lh, italic=italic) + gap
             return self.y
-        lines = wrap(s, kind, bold, size, self.w, italic)
+        lines = wrap(s, kind, bold, size, w, italic)
-    def bridge(self, s, size=20.5, gap=9, fill=GREY):
-        return self.para(s, size, "sans", False, fill, 1.45, gap)
+    def bridge(self, s, size=20.5, gap=9, fill=GREY, w=None):
+        return self.para(s, size, "sans", False, fill, 1.45, gap, w=w)
```

### `content34.py:78` — D6 调用点
```diff
-e.bridge("Заполни в перфекте. Следи за вспомогательными глаголами hebben/zijn.")
+e.bridge("Заполни в перфекте. Следи за вспомогательными глаголами hebben/zijn.", w=366.05)  # delta D6: width-scan band 304.3–427.8px keeps the 3 lines; mid 366.05
```

### `content34.py:130` — D11 盒高公式（P4 HET PROGRAMMA；第 37 行的 P3 SINTERKLAAS 盒不动）
```diff
-sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
+sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30  # delta D11: top reserve 62 → 89 = 16 (pad) + 52 (title block) + 21 (para y-offset); last line was 6.89px below the box
```

### `content7.py:19` — D7 调用点
```diff
-a.bridge("de wedstrijd матч; de groepswinst победа в группе; de kwartfinale четвертьфинал; scoren забивать.")
+a.bridge("de wedstrijd матч; de groepswinst победа в группе; de kwartfinale четвертьфинал; scoren забивать.", w=435.85)  # delta D7: width-scan band 419.8–451.9px keeps the 3 lines; mid 435.85 (line 1 measures 419.78px, inside CW 422.5)
```

### `content7.py:91–92, 100` — D10 两处同用 `dt_zh_w`
```diff
 dt_zh = "Писем и лучших текстов не поступило — образец; обещание на VOL.5."
+dt_zh_w = 384.3  # delta D10: width-scan band 373.2–395.4px keeps the 2 lines; mid 384.3
-lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + ...
+lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + ...
-yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
+yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
```

### `content56.py:143–144, 156` — D8 两处同用 `capcn_w`
```diff
 capcn = "Учебные данные: выдуманные числа, только для упражнения, не настоящий опрос. Вопрос: что ты кладёшь в ботинок? (100 молодых людей)"
+capcn_w = 369.3  # delta D8: width-scan band 353.1–385.5px keeps the 4 lines; mid 369.3
-ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
+ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
-yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
+yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
```

### `content8.py:75–76` — D9 两处同修（键 + 题干，缺一不可）
```diff
-f.ex("B2", "Перевод", "Ik maak een surprise met een gedicht.", "surprise (фикс.)",
-     "Я делаю сюрприз со стихотворением. → ___", instr="Переведите на голландский", size=13.8, gap=0)
+f.ex("B2", "Перевод", "Ik maak een surprise met een kort gedicht.", "surprise (фикс.)",
+     "Я делаю сюрприз с небольшим стихотворением. → ___", instr="Переведите на голландский", size=13.8, gap=0)
```
注记 `surprise (фикс.)` 不动（对新键仍成立）。`kort` 在本版内有据：荷兰语文章句
text.md:72 `Twee: schrijf een gedicht — kort is ook goed.`（与核心的论证相同）。
只改键会留下 nl-de D12 类缺陷（读者只看题干推不出 kort），只改题干会留下键不同步——
两处都改。另：KIT build-5 末尾曾记“ru Q140 无缺陷”（谓题干无限定词故键自洽）——
该判断已被本次任务的盘核推翻：核心题干 `我做一个带小诗的伪装礼物` 含“小”，
读者须从题干导出 `kort`，俄语题干缺“小”即为缺陷；见 KIT Delta 一节。

### `WEEKLY-KIT.md`
- “Files delivered”三 SHA 更新为 build-6 新值；文末新增 “Delta
  (core fix3 + fix4 + fix5, 2026-11-11, build 6)” 一节，旧 SHA 全数保留为历史。

## 4. 重建

- `run.py` rc=0、TOTAL 150、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31；
  0 FLOW OVERFLOW / HEAD TOO WIDE。`P4 col3 ends 1229.6`（旧 1202.6）；
  `P6 chart ends 717`、`P7 col3 ends 1927.0` 与修前一致。
- `render.py` rc=0，印 PDF 12,718,418 B。SVG 哈希 vs 修前：**仅 `p4-sport.svg`（D11）与
  `p8-toets.svg`（D9）变化**，其余 6 个字节一致。
- text.md 重导（`export_fanout.py`，rc=0）：57,848 → 57,870 B（+22 B），diff 恰好
  text.md:415 一行（键 `kort ` +5 B；题干 `с небольшим ` − `со ` +17 B）；
  142 单题 + 2 配对头 + 8 配对项 = 150；8 金句、6 gloss。registry 重导
  （`dump_reg_delta.py`）：150 条，by page / by level 与 build 一致。
- `webpdf.py` rc=0：1,661,392 B（< 7 MB），text layer 55,000 B。

## 5. 六处修复点逐项实测（重建 SVG 证据）

| 点 | 实测值（重建后） | 证据 |
|---|---|---|
| D6 | P3 桥接仍 3 行，内容与修前逐字相同：`Заполни в перфекте. Следи за` (2303.5) / `вспомогательными глаголами` (2333.225) / `hebben/zijn.` (2362.95)，句末 `.` 在行末；下游 y 无位移（p3 SVG 字节一致） | `svg/p3-cultuur.svg`、crop `crop-p3-d6.png`（目检） |
| D7 | P7 桥接仍 3 行逐字相同：`de wedstrijd матч; de groepswinst победа в` (725.66) / `группе; de kwartfinale четвертьфинал;` (755.385) / `scoren забивать.` (785.11)；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d7.png`（目检） |
| D8 | P6 图注仍 4 行，基线 635.02/659.44/683.86/708.28 全不变；盒高 `ch` 不变（`P6 chart ends 717`、`P6 col3 ends 1052.0` 与修前同）；零 y 位移（p6 SVG 字节一致） | `svg/p6-verdieping.svg`、crop `crop-p6-d8.png`（目检） |
| D9 | 三源一致：registry 键 = text.md:415 答案 = P8 节点，均为 `Ik maak een surprise met een kort gedicht.`；题干同步为 `Я делаю сюрприз с небольшим стихотворением.`（text.md:415 + content8.py）；其余 149 键未动（3-way 比对见 §6） | `svg/p8-toets.svg` (y=2173.64)、crop `crop-p8-q140.png`（目检） |
| D10 | P7 来信仍 2 行逐字相同：`Писем и лучших текстов не поступило` (1783.27) / `— образец; обещание на VOL.5.` (1811.67)；盒高 `lh` 不变（`P7 col3 ends 1927.0` 与修前同）；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d10.png`（目检） |
| D11 | 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px（≥20px）**；卡片真墨最低行 1209，余量 +20.60px；印 PDF 150dpi 真墨最低行 1209.55，余量 +20.05px；盒底下 7px 条带双法均为 0 墨像素；`P4 col3 ends 1229.6`；P4 其余内容不动、其余 7 页 SVG 字节一致（D9 的 p8 除外） | `svg/p4-sport.svg`、crop `crop-p4-programma.png`（目检：末行在盒内，下有明显留白） |

## 6. 全部门禁结果

- **Build**：`run.py` rc=0、TOTAL 150、0 溢出（见 §4）。
- **Occlusion 真实审计**：`tools/occlusion_audit.py svg/` rc=0，**0 flags**（自检 planted
  6 类全触发，干净对照静默）。
- **p8 extract**：`p8.py extract --total 150` noted set **150/150**。
- **p8 compare（核心 vs 本版）**：`p8.py compare --json p8-compare.json`，
  直接读本体：`status: CLEAN, total: 150, missing: [], extra: [],
  uncertain: [], keydiff: [137, 138]`。137/138 是翻译题——键本身就是读者语，
  核心为中文（`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），
  本版为俄文（`Новости Синтерклааса идут каждый день в 18:00.` /
  `Двое первых выходят в четвертьфинал.`），按设计不同，非缺陷。
  修前 keydiff 为 [137, 138, 140]——D9 把 140 移出了该表。KIT build-4/5 所记
  “0 key diffs”是 gates.py 对 stdout 中 `key diff` 行的计数（JSON 列表本身
  当时即 [137, 138, 140]），口径不同，特此说明。
- **Keycheck（三源逐题 verbatim 比对 `p8-compare-3way.json`）**：
  **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位
  `(открытое задание, образцовый текст ниже)`）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。
  （注：复用的 `p8compare_delta.py` 原先只认西语标记 `— Respuesta:`，
  致初版比对 md_answer 全空；已按俄语标记 `— Ответ：` / `(Ответ x ·` 改写后重跑，
  149/149——初版空结果未采用。）
- **Freeze 标准核心比对**：`freeze.py baseline --build <core-nl> --core-svg
  <core-nl>/svg --out scratch/freeze-core` rc=0，**8/8 字节一致**；
  核心 shipped SVG 跑前后哈希不变（未碰核心）。
- **版内自比对（补充）**：clean-dir 重跑 `run.py` 再 sha256 比对（gates_delta
  `freeze_sha256` 项），**8/8**。
- **印/网文字层逐页一致**：PyMuPDF 位置排序，8 页 posdiff 0、msdiff 0
  （tokens 797/802/722/727/783/730/885/2151；P8 2151 vs build-5 的 2149，
  +2 = `kort` + `небольшим`）；pdftotext 印 55,000 B = 网 55,000 B。
- **P8 最小 PDF 字号**：答案区 min **10.12pt**（median 10.12，598 spans）≥ 9.75pt。
- **全版孤儿标点两类横扫（重建 SVG，PIL + svglib 双 advance，1464 行）**：
  (a) 独行标点 **0**，(b) 行首标点 **0**，两方法 8 页全 0；
  brute-force 交叉检查：以标点开头的 `<text>` 元素 67 个、leftmost 0 个。
  （CJK + 拉丁标点均纳入；修前横扫亦为 0/0，见 §1。）
- **Creambox**：TOTAL 3 flags，与修前**完全相同**的三处，均为已知假阳性：
  P2 CREAM-BOTTOM `'редакцию.'`（bottom 1503.0 vs rect 1503.8）、P5
  CREAM-BOTTOM `'отправь их.'`（1051.6 vs 1052.5）——盒底下 7px 条带逐像素探查
  **0 非纸像素**；P6 CREAM-RIGHT `DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ`（advance 右 1855.6
  vs 盒右沿 1862.0，内 6.4px）——8px 警告带内，真墨（v2 隔离渲染）391px、盒内
  余量 +9.5px；P6 标题右沿外 x1862–1875 条带 0 非纸像素。
  P4（D11 盒）0 flags。**真溢出 0。**
- **盒标题横向真墨扫描**：v1 卡片带扫 59 标题、3 OVER——全部是邻栏墨污染
  （与 nl-en 同类裁决）：P8 HEAD `A　VUL DE KRONIEK IN` 的 x=537 幻影墨来自
  col-2 内容（起于 COLX 538.5）；P6 两盒标题的 OVER 只越过“盒沿−22”内限，
  未越盒沿。v2 隔离渲染（每标题 PIL 单独渲染、NotoSansCJK-Bold 真墨 bbox）：
  **59 标题、OVER-EDGE 0**；最紧余量 P6 DE GRAFIEK +9.5、P6 VOOR OF TEGEN?
  +18.5、P2 DRIE DINGEN head +25.5、P2 ZO ONTHOUD +26.5、P1 DE WEEK IN CIJFERS
  +35.5、P7 HET WOORD +55.5。任务所称 56 标题无一定义能复现（38 heads / 21 盒标题
  是 en 版的数；本版实测为 38 head 出现 + 21 盒标题 = 59）——按 nl-en 的处理，
  扫全集 59、0 越边，计数差异留协调员定，不粉饰。
- **Spill 横扫**：P4 HET PROGRAMMA 盒（底 1229.6）无任何 below 命中；其余 BELOW
  命中（P1 +24、P2 +50.5/+32、P5 +50.5、P7 +60/+60px）均为独立版块（下一节标题、
  提示语、gloss），ABOVE/SIDE 均为图注/邻盒标题/刊头——与核心 fix5 同类裁决。真溢出 0。
- **Fanout 门禁套件**（`gates_delta.py`，即 build-5 同款 9 项）：
  **ALL PASS**（occlusion / p8_extract / p8_compare / freeze_sha256 /
  print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips /
  s11_svg——§1.1 off-palette {}、VOL.5 = 5 = core、paper fills 8）。
- D3 回归：P2 SVG 字节一致，D3 断行与余量与 build-5 相同，无需重测。

## 7. 新三 SHA（交付）

| 文件 | 字节 | SHA-256（修后，实测） | 旧值（build-5，历史） |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-ru.pdf`（印） | 12,718,418 | `21b7adf007a15e195756d49b22c824e828f854e11e02a10c916426997c468cc8` | `f945029d…ff889c2` / 12,718,382 |
| `De-Lucerna-VOL4-nl-ru-web.pdf`（网） | 1,661,392 | `1a17474368591008dcefb73661be58a17edc38c5dcc98f674fc0afe6ea6cc9bf` | `e5e3d5d3…352724` / 1,661,354 |
| `2026-w47-nl-ru.text.md`（文） | 57,870 | `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` | `558786fc…4829273` / 57,848 |

网 PDF 铁律：SHA 与字节大小均不可复现，只比文字层；交付的网 PDF 由本次
重建产生（文字层与印 PDF 逐页一致，见 §6）。

## 8. 改动文件清单与未动确认

- 改动（规范路径 `production/2026-w47/2026-w47-nl-ru/` 内）：`bslib4.py`、
  `content34.py`、`content56.py`、`content7.py`、`content8.py`（§3 对照）、
  `WEEKLY-KIT.md`（新 SHA + delta 节）。
- 重建产物（同目录）：`svg/p4-sport.svg`、`svg/p8-toets.svg`（仅此 2 个 SVG
  变化）、`cards/*.png`、`De-Lucerna-VOL4-nl-ru.pdf`、
  `De-Lucerna-VOL4-nl-ru-web.pdf`、`2026-w47-nl-ru.text.md`。
- 未动：core-nl（只读；freeze 8/8 + 核心 shipped SVG 哈希不变）、其他版、
  staging 副本 `fanout-nl/2026-w47-nl-ru/`（三 SHA 复核仍为任务给定值：
  印 `f945029d…` / 12,718,382 B，网 `e5e3d5d3…` / 1,661,354 B，
  文 `558786fc…` / 57,848 B）、tools/、`content12.py`、ABSTRACT.txt。未 commit、未 push。
- 待 proof1（独立校对员）定稿后由协调员统一 commit/push。
