# DELTA-LOG — 2026-W47 nl-zh-tw, core fix3 + fix4 + fix5 同步

- 版：`2026-w47-nl-zh-tw`（荷兰语目标 × 繁體中文读者版），VOL.4，8 版，150 题
- 日期：2026-11-11
- 任务：core-nl fix3（D6/D7）+ fix4（D8/D9/D10）+ fix5（D11）同步到本版。
  只改本版自己的源文件，不碰核心、不碰其他版、不碰 staging 副本。不 commit、不 push。
  修后由另一位独立校对员 proof1，不要自己定稿。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-zh-tw/`
  （日志、门禁证据、registry、比对 JSON、crops 均在此）
- 工作区：repo 克隆 `~/workspace/weekly-git`；解释器 `tools/venv/bin/python`；
  TMPDIR = 本 scratch 目录
- 核心对照（只读）：`production/2026-w47/core-nl/`，fix5 定稿已核对——
  印 `b7d4a9cd…` / 25,955,578 B，网 `5a47449c…` / 2,104,000 B，
  文 `0b97a48d…` / 44,093 B，三件与 nl-de 试点日志给出的 fix5 定稿值一致。
  权威记录：core-nl `FIX-LOG.md`（fix3 第 412 行起、fix4 第 185 行起、
  fix5 第 3 行起），开工前已通读。nl-de 试点 `DELTA-LOG.md` 为方法模板。

## 0. 开工探针与路径

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → rc=0
  （`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`）；`/dev/null` 为字符设备，正常。
  goals-side scratch 探针文件写入成功（`scratch-delta-nl-zh-tw/probe.txt`）。
  磁盘 df：150G 总，96G 已用，54G 空闲——可写。
- **路径：任务所称的规范路径 `production/2026-w47/2026-w47-nl-zh-tw/` 在开工时
  不存在**（与 nl-de 试点相同情况：W47 的 nl fanout 版只存在于 staging 目录
  `production/2026-w47/fanout-nl/`）。处理：把 staging 的 nl-zh-tw 版整目录
  `cp -a` 到规范路径，`diff -r --exclude=__pycache__` 校验**完全一致**
  （仅两条无害的 ownership 保留警告），staging 副本全程未动；此后全部 delta
  工作都在规范路径做。
- 修前身份核对（三件 SHA，实测 = 任务给出的 build-2 值）：印
  `3a81e9cf00ff56378f692af8e951a4d306d0c68eae113332c8bede67d477eb9b` /
  25,993,150 B；网 `aedb0d6e80fdb95f3279dea8523b09e2130309f82e26fcf940559405cd1cced7`
  / 2,369,193 B；文 `54d20ccd80af265c3ec62d2db0a08cbd1e7ecc559ea1bdc24557b449d293539e`
  / 44,315 B。修前 8 个 SVG SHA 存 `pre/svg-sha-pre.txt`。

## 1. 修前实测：D6/D7/D8/D10/D11 全部真实存在（与 nl-de 不同）

修前 SVG 实测（孤儿横扫 PIL + svglib 双 advance，1415 行；brute-force 交叉检查）：

| 点 | 修前 SVG 实测 | 结论 |
|---|---|---|
| D6 P3 桥接 | `用現在完成式填空。注意助動詞 hebben/zijn` (y=2250.5) / `。` 独占一行 (y=2280.225) | class-a **真缺陷** |
| D7 P7 桥接 | `de wedstrijd 比賽；de groepswinst 小組頭名` (725.66) / `；de kwartfinale 八強賽；scoren 進球。` (755.385)，行 2 行首 `；` | class-b **真缺陷**（KIT 称“P7 无孤儿 。”只对独行 。成立） |
| D8 P6 图注 | `練習數據：虛構數字，僅供練習，非真實調查` (635.02) / `。問題：你在鞋裡放什麼？（100 名年輕人）` (659.44)，行 2 行首 `。` | class-b **真缺陷** |
| D9 Q140 | registry 键、text.md:415 答案、P8 节点三源同错：`Ik maak een surprise met een gedicht.`（缺 `kort`）；题干 `我做一個帶小詩的偽裝禮物。` 已含“小” | **真缺陷** |
| D10 P7 来信 | `截稿時未收到真實來信或第 8 版最佳作文` (1754.27) / `，刊登示例信，承諾順延 VOL.5。` (1782.67)，行 2 行首 `，` | class-b **真缺陷** |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=611.0>` 底 1202.6；末行 `18:45 uur.` 基线 y=1209.49，**盒底外 +6.89px** | **真缺陷** |

修前孤儿横扫：class-a=1（P3），class-b=3（P6 ×1、P7 ×2），PIL 与 svglib 双方法一致；
brute-force 行首标点元素 12 个，其中行内最左 3 个，即上述 D8/D7/D10 三处（其余 9 个
均为行中片段：P1 `：柏林奧林匹克`、P8 的 4 个 `：`/1 个 `，`/4 个 `）`答案区定位符，均非
行首，排除——与核心 fix4 的处理相同）。**六处全部是真修，没有一处是“预先不存在”。**

## 2. Width scan（本版自己的文字 + 本版 `svglib.wrap()`，0.1px 步进）

CW = 422.5。核心数值一律不抄：

| 点 | 文字（字体/字号） | 当前 w | 目标断行区间（同行内容） | 选中 w |
|---|---|---|---|---|
| D6 桥接 | `用現在完成式填空。注意助動詞 hebben/zijn。`（sans 20.5） | CW=422.5 | 287.0–406.1（2 行，。落行 2 末尾） | **346.55**（中点） |
| D7 桥接 | `de wedstrijd 比賽；… scoren 進球。`（sans 20.5） | CW=422.5 | 329.5–354.5（3 行，全干净） | **342.0**（中点） |
| D8 图注 | `練習數據：…（100 名年輕人）`（sans 18.5） | CW−44=378.5 | 388.5–406.9（2 行，。落行 1 末尾） | **capcn_w=397.7**（中点） |
| D10 来信 | `截稿時未收到真實來信或第 8 版最佳作文，刊登示例信，承諾順延 VOL.5。`（sans 20） | CW−44=378.5 | 380.1–400.0（2 行，。落行 1 末尾） | **dt_zh_w=390.05**（中点） |

D7 特别说明：2 行干净断行不存在——416.1–422.5px 保留行首 `；`；395.6–416.0px
保 2 行但把 `小組頭名` 拆成 `小組頭` / `名；…` 两行（核心 fix4 D10 明确拒绝过
同类拆词：最佳作/文）。329.5–354.5px 的 3 行断行各项完整、无行首标点，选中点
为该区间中点 342.0。代价是行数 2→3，下游 y +29.725px：A2 流结束 y=1252
（bottom 1560），无溢出（见 §4/§6）。另两个 3 行干净区间 324.6–329.4（窄 4.9px）
未选用。
D11 事实句（serif 21.5，CW−44）：5 句断行 3/3/3/2/3 = 14 行，与核心一致；
`sh` 旧 611.0 → 新 638.0（+27）。顶留 89 = 16（pad）+ 52（标题块）+ 21
（para y-offset），本版 `content34.py` 渲染循环形状与核心相同（`yy3 = sy3+16`、
标题后 `yy3 += 52`、事实 `p.para(…, yy3+21, …)`），盒顶 sy3=591.6 不变。

## 3. 改动源码行前后对照（仅 5 个源文件 + KIT）

`diff -r`（规范路径 vs staging 副本，排除 svg/cards/PDF）只显示以下 6 文件
（5 源文件 + text.md；KIT 另见 §7）：

### `bslib4.py` — D6/D7 机制（照搬核心 fix3 的 `w` 机制；本版 re-fanout 早于该机制）
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
-e.bridge("用現在完成式填空。注意助動詞 hebben/zijn。")
+e.bridge("用現在完成式填空。注意助動詞 hebben/zijn。", w=346.55)  # delta D6: width-scan band 287.0–406.1px wraps to the same 2 lines with 。 at line-2 end; mid 346.55
```

### `content34.py:130` — D11 盒高公式（P4 HET PROGRAMMA；第 37 行的 P3 SINTERKLAAS 盒不动）
```diff
-sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
+sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30  # delta D11: top reserve 62 → 89 = 16 (pad) + 52 (title block) + 21 (para y-offset); last line was 6.89px below the box
```

### `content7.py:19` — D7 调用点
```diff
-a.bridge("de wedstrijd 比賽；de groepswinst 小組頭名；de kwartfinale 八強賽；scoren 進球。")
+a.bridge("de wedstrijd 比賽；de groepswinst 小組頭名；de kwartfinale 八強賽；scoren 進球。", w=342.0)  # delta D7: width-scan band 329.5–354.5px wraps to 3 clean lines (no line-initial ；, no split gloss term); mid 342.0; 2-line bands either keep the ； or split 小組頭名
```

### `content7.py:91–92, 100` — D10 两处同用 `dt_zh_w`
```diff
 dt_zh = "截稿時未收到真實來信或第 8 版最佳作文，刊登示例信，承諾順延 VOL.5。"
+dt_zh_w = 390.05  # delta D10: width-scan band 380.1–400.0px keeps the 2 lines with ， at line-1 end; mid 390.05
-lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + ...
+lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + ...
-yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
+yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
```

### `content56.py:143–144, 156` — D8 两处同用 `capcn_w`
```diff
 capcn = "練習數據：虛構數字，僅供練習，非真實調查。問題：你在鞋裡放什麼？（100 名年輕人）"
+capcn_w = 397.7  # delta D8: width-scan band 388.5–406.9px keeps the 2 lines with 。 at line-1 end; mid 397.7
-ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
+ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
-yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
+yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
```

### `content8.py:75` — D9 键补 kort（目标语荷兰语句，直接照搬核心）
```diff
-f.ex("B2", "翻譯", "Ik maak een surprise met een gedicht.", "surprise 是固定搭配",
+f.ex("B2", "翻譯", "Ik maak een surprise met een kort gedicht.", "surprise 是固定搭配",
```
注记不动。`kort` 在本版内有据：荷兰语文章句 text.md:73（与核心的论证相同，
本版 text.md 同样载有 `Twee: schrijf een gedicht — kort is ook goed.`）。
繁體题干 `我做一個帶小詩的偽裝禮物。` 不动（已含“小”）；未动任何中文繁簡。

### `WEEKLY-KIT.md`
- “Files delivered”三 SHA 更新为 build-3 新值；旧 SHA 保留为历史；文末新增
  “Delta (core fix3 + fix4 + fix5, 2026-11-11, build 3)” 一节，逐处写清改动。

## 4. 重建

- `run.py` rc=0、TOTAL 150、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31；
  0 FLOW OVERFLOW / HEAD TOO WIDE。`P4 col3 ends 1229.6`（旧 1202.6）；
  `P6 chart ends 665`、`P7 col3 ends 1898.0` 与修前一致；`flow[P7-a2] ends y=1252`
 （bottom 1560，D7 多一行后仍有 308px 余量）。
- `render.py` rc=0。SVG 哈希 vs 修前：**仅 `p3-cultuur.svg`（D6）、`p4-sport.svg`
  （D11）、`p6-verdieping.svg`（D8）、`p7-taal.svg`（D7+D10）、`p8-toets.svg`
  （D9）变化**，p1/p2/p5 字节一致。
- text.md 重导（`export_fanout.py`，rc=0）：44,315 → 44,320 B，diff 恰好
  text.md:415 一行（`kort `，+5 B）；142 单题 + 2 配对头 + 8 配对项 = 150；
  8 金句、6 gloss。注：核心 fix3 记载的导出 stub `w` 兼容问题本版未遇到——
  fanout exporter 的 `stub_bslib47.py` 已带 `w=None` 透传（fix3 时已补）。
- `webpdf.py` rc=0：2,369,230 B（< 7 MB），text layer 44,329 B。

## 5. 六处修复点逐项实测（重建 SVG 证据）

| 点 | 实测值（重建后） | 证据 |
|---|---|---|
| D6 | P3 桥接仍 2 行：`用現在完成式填空。注意助動詞` (2250.5) / `hebben/zijn。` (2280.225)，句末 `。` 在行末，基线与修前相同；下游 y 无位移（p3 除该两行外余无变化） | `svg/p3-cultuur.svg`、crop `crop-p3-d6.png`（目检） |
| D7 | P7 桥接现 3 行干净：`de wedstrijd 比賽；de groepswinst` / `小組頭名；de kwartfinale 八強賽；` / `scoren 進球。` (725.66/755.385/785.11)；术语完整、无行首标点；A2 流结束 1252，无溢出 | `svg/p7-taal.svg`、crop `crop-p7-d7.png`（目检） |
| D8 | P6 图注仍 2 行，基线 635.02/659.44 全不变：`練習數據：虛構數字，僅供練習，非真實調查。` / `問題：你在鞋裡放什麼？（100 名年輕人）`；盒高 `ch` 不变（`P6 chart ends 665`、`P6 col3 ends 1000.0` 与修前同）；行 1 末端 x=1850.0，盒右缘内 12px | `svg/p6-verdieping.svg`、crop `crop-p6-d8.png`（目检） |
| D9 | 三源一致：registry 键 = text.md:415 答案 = P8 节点，均为 `Ik maak een surprise met een kort gedicht.`；其余 149 键未动（3-way 比对见 §6） | `svg/p8-toets.svg` (y=2128.32)、crop `crop-p8-q140.png`（目检） |
| D10 | P7 来信仍 2 行，基线 1754.27/1782.67 全不变：`截稿時未收到真實來信或第 8 版最佳作文，` / `刊登示例信，承諾順延 VOL.5。`；盒高 `lh` 不变（`P7 col3 ends 1898.0` 与修前同）；行 1 末端 x=1841.6，盒右缘内 20px | `svg/p7-taal.svg`、crop `crop-p7-d10.png`（目检） |
| D11 | 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px（≥20px）**；真墨余量 +20.60px（cards 1×）/ +20.48px（印 PDF 150dpi 渲染）；盒底下 7px 条带 0 非纸像素（双渲染）；`P4 col3 ends 1229.6`；P4 其余内容不动（spill 扫 P4 盒无 BELOW 命中） | `svg/p4-sport.svg`、crop `crop-p4-d11.png`（目检：末行在盒内，下有明显留白）、`inkprobe-d11-delta.log` |

## 6. 全部门禁结果

- **Build**：`run.py` rc=0、TOTAL 150、0 溢出（见 §4）。
- **Occlusion 真实审计**：`tools/occlusion_audit.py svg/` rc=0，**0 flags**。
- **p8 extract**：`p8.py extract --total 150` noted set **150/150**。
- **p8 compare（核心 vs 本版）**：`p8.py compare --json p8-compare-delta.json`，
  直接读本体：`status: CLEAN, total: 150, missing: [], extra: [],
  uncertain: [], keydiff: [137, 138]`。137/138 是翻译题——键本身就是读者语，
  核心为简体中文（`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），
  本版为繁體中文（`聖誕老人新聞每天 18:00 播出。` / `前兩名晉級八強賽。`），
  按设计不同，非缺陷。修前 keydiff 为 [137, 138, 140]——D9 把 140 移出了该表。
  （KIT build-2 所记“0 key diffs”是 gates.py 对 stdout 中 `key diff` 行的计数，
  口径不同，特此说明——与 nl-de 试点相同。）
- **Keycheck（三源逐题 verbatim 比对 `p8-compare-3way.json`）**：
  **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。
  手验抽样：Q137/Q138/Q140 三源逐字核对——text.md:412/413/415 答案与 registry、
  P8 键逐字一致（137/138 的核心差异是读者语译法不同，按设计）。
- **Freeze 标准核心比对**：`freeze.py baseline --build <core-nl> --core-svg
  <core-nl>/svg --out scratch/freeze-core` rc=0，**8/8 字节一致**；
  核心 shipped SVG 跑前后哈希不变（未碰核心，`core integrity` 行确认）。
- **版内自比对（补充）**：clean-dir 重跑 `run.py` 再 sha256 比对，
  **8/8**（fanout gates.py `freeze_sha256` 项）。
- **印/网文字层逐页一致**：PyMuPDF 位置排序，8 页 posdiff 0、msdiff 0
  （tokens 749/705/664/658/685/648/735/1677；P8 1677 vs build-2 的 1676，
  +1 = `kort`）；pdftotext 印 44,329 B = 网 44,329 B。
- **P8 最小 PDF 字号**：答案区 min **10.12pt**（median 10.12，566 spans）≥ 9.75pt。
- **全版孤儿标点两类横扫（重建 SVG，PIL + svglib 双 advance，1419 行）**：
  (a) 独行标点 **0**，(b) 行首标点 **0**，两方法 8 页全 0；
  brute-force 交叉检查：行首标点 `<text>` 元素 **0 个**
  （剩余 8 个行首标点片段均为行中定位符/冒号，非行首，已裁决）。
  修前为 1/3，见 §1。
- **Creambox**：TOTAL 3 flags，与 build-2 **完全相同**的三处（P2/P5/P6），均为已知
  假阳性：盒底下 7px 条带逐像素探查 **0 非纸像素**，PIL 4× 真墨余量
  +7.94 / +7.95 / +8.81px。P4（D11 盒）0 flags。**真溢出 0。**
- **Spill 横扫**：**0 spills**；P4 HET PROGRAMMA 盒（底 1229.6）无任何 BELOW
  命中；其余 BELOW 命中（+32/+50.5/+60px）均为独立版块（下一节标题、
  提示语、gloss），ABOVE/SIDE 均为图注/邻盒标题——与核心 fix5 同类裁决。
- **盒标题横向真墨扫描**：58 项（32 个 Flow head + 26 个奶油盒标题），PIL 真墨。
  57 项通过；1 项方法伪旗已裁决：P8 head `A　VUL DE KRONIEK IN` 扫描值
  ink_right=537、limit=510.5（-26.5）。核实：标题本身 PIL advance 仅 234.86px，
  真墨止于 x≈323（余量 +187.5px）；x=537–539 的墨是右侧邻栏的 B1 徽章
  （扫描窗向限外扩了 28px 把邻栏墨算了进来），另 x=500–537 的墨是标题自带的
  下划线（合规地铺满栏宽）；三张卡（staging 修前 / 重建 / 核心）同带同值，
  修前修后完全一致——**非本 delta 引入，非标题越边**，与 nl-en 试点同值
  （其日志亦有同一 -26.5）。注：fanout build-1 KIT 称“56 标题 ALL PASS”所用的
  `check_titles_h.py` 未能在 scratch 区找到原脚本，本次按 nl-en 的
  `boxtitle_inkscan_delta.py` 方法（58 项）重测并如实记录，未沿用无法复现的
  56 项口径。
- **Fanout 门禁套件**（`gates_delta.py`，即 build-2 同款 9 项）：
  **ALL PASS**（occlusion / p8_extract / p8_compare / freeze_sha256 /
  print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips /
  s11_svg——§1.1 off-palette {}、VOL.5 = 5 = core、paper fills 8）。
- D3 回归：P2 SVG 字节一致，D3 断行与余量与 build-2 相同，无需重测。
  （P2 option c 短式仍在位；P2 字节一致即证。）

## 7. 新三 SHA（交付）

| 文件 | 字节 | SHA-256（修后，实测） | 旧值（build-2，历史） |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-zh-tw.pdf`（印） | 25,993,186 | `6de893ca2811357c7be524b2b17e78af1c5362abc647e957d8665559466c704a` | `3a81e9cf…7eb9b` / 25,993,150 |
| `De-Lucerna-VOL4-nl-zh-tw-web.pdf`（网） | 2,369,230 | `172c1be81d32d871c323064c685e0918e41b12b29a25a19a50cf4926d217ff20` | `aedb0d6e…cced7` / 2,369,193 |
| `2026-w47-nl-zh-tw.text.md`（文） | 44,320 | `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60` | `54d20ccd…39539e` / 44,315 |

网 PDF 铁律：SHA 与字节大小均不可复现，只比文字层；交付的网 PDF 由本次
重建产生（文字层与印 PDF 逐页一致，见 §6）。

## 8. 改动文件清单与未动确认

- 改动（规范路径 `production/2026-w47/2026-w47-nl-zh-tw/` 内）：`bslib4.py`、
  `content34.py`、`content56.py`、`content7.py`、`content8.py`（§3 对照）、
  `WEEKLY-KIT.md`（新 SHA + delta 节）。
- 重建产物（同目录）：`svg/p3-cultuur.svg`、`svg/p4-sport.svg`、
  `svg/p6-verdieping.svg`、`svg/p7-taal.svg`、`svg/p8-toets.svg`（仅此 5 个 SVG
  变化；p1/p2/p5 字节一致）、`cards/*.png`、
  `De-Lucerna-VOL4-nl-zh-tw.pdf`、`De-Lucerna-VOL4-nl-zh-tw-web.pdf`、
  `2026-w47-nl-zh-tw.text.md`。
- 未动：core-nl（只读；freeze 基线 8/8 且 integrity 行确认未变）、其他版、
  staging 副本 `fanout-nl/2026-w47-nl-zh-tw/`（三 SHA 复核仍为 build-2 值：
  印 `3a81e9cf…7eb9b`、网 `aedb0d6e…cced7`、文 `54d20ccd…39539e`）、tools/、
  `content12.py`、ABSTRACT.txt。未 commit、未 push。
- 待 proof1（独立校对员）定稿后由协调员统一 commit/push。
