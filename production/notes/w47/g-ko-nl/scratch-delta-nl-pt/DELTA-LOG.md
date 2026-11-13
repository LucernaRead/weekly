# DELTA-LOG — 2026-W47 nl-pt, core fix3 + fix4 + fix5 同步

- 版：`2026-w47-nl-pt`（荷兰语目标 × 葡萄牙语读者版），VOL.4，8 版，150 题
- 日期：2026-11-11
- 任务：core-nl fix3（D6/D7）+ fix4（D8/D9/D10）+ fix5（D11）同步到本版。
  只改本版自己的源文件，不碰核心、不碰其他版、不碰 staging。不 commit、不 push。
  修后由另一位独立校对员 proof1，不要自己定稿。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-pt/`
  （日志、门禁证据、registry、比对 JSON、crops 均在此）
- 工作区：repo 克隆 `~/workspace/weekly-git`；解释器 `tools/venv/bin/python`；
  TMPDIR = 本 scratch 目录
- 核心对照（只读）：`production/2026-w47/core-nl/`，fix5 定稿已核对——
  印 `b7d4a9cd…` / 25,955,578 B，网 `5a47449c…` / 2,104,000 B，
  文 `0b97a48d…` / 44,093 B，三件与任务给出的 SHA 逐字节一致。
  权威记录：core-nl `FIX-LOG.md`（fix3、fix4、fix5 全文，开工前已通读）。

## 0. 开工探针与路径问题

- 探针：`git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`
  （rc=0）；`/dev/null` 正常；scratch 目录真实写文件成功（probe.txt）。
  磁盘 54G 可用。
- **路径问题：任务所称的规范路径 `production/2026-w47/2026-w47-nl-pt/` 在开工时
  不存在**（与 nl-es/nl-de 试点相同）。处理：把 staging 的 nl-pt 版整目录
  `cp -a` 到规范路径，`diff -r --exclude=__pycache__` 校验**完全一致**
  （diff-rc=0；仅两条无害的 ownership 保留警告），staging 副本全程未动；
  此后全部 delta 工作都在规范路径做。
- 修前身份核对（三件 SHA，实测）：印
  `e85aa1a01bea9c7894546e9e33f45f2c519f202f3404103dff59265f5daac834` /
  12,672,018 B；网 `a0c8c87bd941fc87d945eac257053a482de7b1f1fc8a088070f3d66351146d85`
  / 1,618,472 B；文 `865e659fc2d4a9b1639c3513cd8e3326536feac8ae5fed14dca411d0cc137efc`
  / 47,204 B——与任务给出的三 SHA/字节数逐一一致。修前 8 个 SVG SHA 存
  `pre-svg-sha.txt`。终核时 staging 与 core-nl 三 SHA 复核仍为上述值（未动）。

## 1. 修前实测：D6/D7/D8/D10 在本版预先不存在；D9 未修；D11 是真缺陷

葡萄牙语读者层文字与核心中文桥接文字断行不同——修前 SVG 实测：

| 点 | 修前 SVG 实测 | 结论 |
|---|---|---|
| D6 P3 桥接 | `Completa no pretérito perfeito. Atenção aos` (y=2303.5) / `auxiliares hebben/zijn.` (y=2333.225)，2 行，句末 `.` 在行 2 末尾 | 无孤儿 |
| D7 P7 桥接 | 3 行：`de wedstrijd jogo; de groepswinst vitória do` (725.66) / `grupo; de kwartfinale quartos de final;` (755.385) / `scoren marcar.` (785.11)，句末 `.` 在行末 | 无孤儿 |
| D8 P6 图注 | 4 行：`Dados de prática: números inventados, só` / `para praticar, não um inquérito real.` / `Pergunta: o que pões no teu sapato? (100` / `jovens)`，基线 635.02/659.44/683.86/708.28 | 无行首标点 |
| D10 P7 来信 | 2 行：`Sem cartas reais nem melhores textos:` (1783.27) / `exemplo; promessa passa para VOL.5.` (1811.67) | 无行首标点 |
| D9 Q140 | registry 键、text.md:415 答案、P8 节点三源**同为不含 `kort` 的旧键**：`Ik maak een surprise met een gedicht.`；题干 `Faço uma surprise com um poema curto.` 已含 curto（小） | **未修，需改三处** |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=611.0>` 底 1202.6；末行 `18:45 uur.` 基线 y=1209.49，**盒底外 +6.89px** | **真缺陷** |

全版孤儿标点横扫（修前未单跑，修后双法同跑见 §6；修前 D6/D7/D8/D10 四处
的实测行本身即无孤儿/行首标点）。因此 D6/D7/D8/D10 的同步是**结构性**的：
机制照搬 + 本版文字重算 w，选出的 w 必须**精确复现当前干净断行**（行内容、
行数、基线全不变），重建 SVG 以 p3/p6/p7 字节一致为证。D9、D11 是真修。

## 2. Width scan（本版自己的文字 + 本版 `svglib.wrap()`，0.1px 步进）

CW = 422.5。取“精确复现当前各行”的 w 区间中点（核心数值一律不抄）：

| 点 | 文字（字体/字号） | 当前 w | 区间（同行内容） | 选中 w |
|---|---|---|---|---|
| D6 桥接 | `Completa no pretérito perfeito. Atenção aos auxiliares hebben/zijn.`（sans 20.5） | CW=422.5 | 416.7–512.7（2 行） | **464.7**（中点） |
| D7 桥接 | `de wedstrijd jogo; … scoren marcar.`（sans 20.5） | CW=422.5 | 415.7–432.2（3 行） | **423.95**（中点） |
| D8 图注 | `Dados de prática: … (100 jovens)`（sans 18.5） | CW−44=378.5 | 359.6–396.6（4 行） | **capcn_w=378.1**（中点） |
| D10 来信 | `Sem cartas reais nem melhores textos: exemplo; promessa passa para VOL.5.`（sans 20） | CW−44=378.5 | 356.3–446.6（2 行） | **dt_zh_w=401.45**（中点） |

注：D6 区间上沿不在首轮 200–500px 扫描内（500px 处仍同断行），补扫
500–1200px 得真上沿 512.7（512.8 起 `auxiliares` 上移至行 1，600px 起并为
1 行），全区间 416.7–512.7，中点 464.7。w 只进 `wrap()`（断行）与高度计量，
产出字符串逐字相同，故渲染结果与 w 在区间内任意值一致——p3 SVG 字节一致
为证。D8 中点 378.1 与现值 378.5 仅差 0.4px（仍取实测中点）。

D11 事实句（serif 21.5，CW−44）：5 句断行 3/3/3/2/3 = 14 行，与核心一致；
`sh` 旧 611.0 → 新 638.0（+27）。顶留 89 = 16（pad）+ 52（标题块）+ 21
（para y-offset），本版 `content34.py` 渲染循环形状与核心相同（`yy3 = sy3+16`、
标题后 `yy3 += 52`、事实 `p.para(…, yy3+21, …)`），盒顶 sy3=591.6 不变。
实测基线序列与核心 FIX-LOG 一致：首行 680.60 … 末行 1209.49，盒顶偏移 617.89。

## 3. 改动源码行前后对照（仅 5 个源文件 + KIT）

`diff -r`（规范路径 vs staging 副本，排除 svg/cards/PDF）只显示以下 5 文件：

### `bslib4.py` — D6 机制（照搬核心 fix3 的 `w` 机制，与 core-nl 的实现逐字一致）
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
-e.bridge("Completa no pretérito perfeito. Atenção aos auxiliares hebben/zijn.")
+e.bridge("Completa no pretérito perfeito. Atenção aos auxiliares hebben/zijn.", w=464.7)  # delta D6: width-scan band 416.7–512.7px keeps the 2 lines; mid 464.7
```

### `content34.py:130` — D11 盒高公式（P4 HET PROGRAMMA；P3 SINTERKLAAS 盒不动）
```diff
-sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
+# Fix5 D11: top reserve was 62 but box-top -> first baseline is really
+# 16 (pad) + 52 (title block) + 21 (para y-offset) = 89; the 27px shortfall
+# put the last baseline 6.89px below the box bottom. With 89 the last
+# baseline (1209.49) sits 20.11px above the new box bottom (1229.6).
+sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
```

### `content7.py:19` — D7 调用点
```diff
-a.bridge("de wedstrijd jogo; de groepswinst vitória do grupo; de kwartfinale quartos de final; scoren marcar.")
+a.bridge("de wedstrijd jogo; de groepswinst vitória do grupo; de kwartfinale quartos de final; scoren marcar.", w=423.95)  # delta D7: width-scan band 415.7–432.2px keeps the 3 lines; mid 423.95
```

### `content7.py:91–92, 103` — D10 两处同用 `dt_zh_w`
```diff
 dt_zh = "Sem cartas reais nem melhores textos: exemplo; promessa passa para VOL.5."
+# delta D10: dt_zh wrap width 401.45. Width scan (sans 20): band
+# 356.3–446.6px wraps to the same 2 lines; 401.45 is the band middle.
+dt_zh_w = 401.45
-lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + ...
+lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + ...
-yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
+yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
```

### `content56.py:143–144, 159` — D8 两处同用 `capcn_w`
```diff
 capcn = "Dados de prática: números inventados, só para praticar, não um inquérito real. Pergunta: o que pões no teu sapato? (100 jovens)"
+# delta D8: capcn wrap width 378.1. Width scan (sans 18.5): band
+# 359.6–396.6px wraps to the same 4 lines; 378.1 is the band middle.
+capcn_w = 378.1
-ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
+ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
-yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
+yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
```

### `content8.py:75` — D9 键补 `kort`（本版三处同步中的源码一处）
```diff
-f.ex("B2", "Traduzir", "Ik maak een surprise met een gedicht.", "surprise é uma expressão fixa",
+f.ex("B2", "Traduzir", "Ik maak een surprise met een kort gedicht.", "surprise é uma expressão fixa",
```
注记 `surprise é uma expressão fixa` 不变（新答案下仍真；`kort` 已由题干
`um poema curto` 与正文 text.md:238 `maak je liever een surprise met een
gedicht?` 对应核心 text.md:73 `kort is ook goed`  gloss，无需加注）。
其余两处由重建 + 重导自然同步：text.md:415 答案、P8 SVG 节点（§5）。

### `WEEKLY-KIT.md`
- “Files delivered”三 SHA 更新为 build-4 新值；文末新增 “Delta
  (core fix3 + fix4 + fix5, 2026-11-11, build 4)” 一节，旧 SHA 全数保留为历史。

## 4. 重建

- `run.py` rc=0、TOTAL 150、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31；
  0 FLOW OVERFLOW / HEAD TOO WIDE。`P4 col3 ends 1229.6`（旧 1202.6）；
  `P3 col3 ends 1106.6`、`P6 chart ends 717`、`P7 col3 ends 1927.0` 与修前一致。
- `render.py` rc=0，印 PDF 12,672,019 B。SVG 哈希 vs 修前：**仅
  `p4-sport.svg`（D11）与 `p8-toets.svg`（D9）变化**，其余 6 个字节一致。
- text.md 重导（`export_fanout.py`，rc=0）：47,209 B（修前 47,204，+5 =
  `kort `）；diff vs 修前**仅 415 行**；142 单题 + 2 配对头 + 8 配对项 = 150；
  8 金句、6 gloss、模型文 81 词。registry 重导（`dump_reg_delta.py`）：150 条，
  by page / by level 与 build 一致。导出器 stub（`stub_bslib47.py`）已含
  `w=None` 透传（fix3 时补的），重导无 TypeError；导出后 SVG 哈希复核与
  重建后一致（导出器未 touch SVG）。
- `webpdf.py` rc=0：1,618,464 B（< 7 MB），text layer 46,698 B。

## 5. 六处修复点逐项实测（重建 SVG 证据）

| 点 | 实测值（重建后） | 证据 |
|---|---|---|
| D6 | P3 桥接仍 2 行，内容与修前逐字相同：`Completa no pretérito perfeito. Atenção aos` (2303.5) / `auxiliares hebben/zijn.` (2333.225)；下游 y 无位移（p3 SVG 字节一致） | `svg/p3-cultuur.svg`、crop `crop-p3-d6.png`（目检） |
| D7 | P7 桥接仍 3 行逐字相同，末行 `scoren marcar.` (785.11)；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d7.png`（目检） |
| D8 | P6 图注仍 4 行，基线 635.02/659.44/683.86/708.28 全不变；盒高 `ch` 不变（`P6 chart ends 717` 与修前同）；零 y 位移（p6 SVG 字节一致） | `svg/p6-verdieping.svg`、crop `crop-p6-d8.png`（目检） |
| D9 | 三源一致：registry 键 = text.md:415 答案 = P8 节点（y=2221.54），均为 `Ik maak een surprise met een kort gedicht.`；其余 149 键未动（3-way 比对见 §6） | `svg/p8-toets.svg`、crop `crop-p8-q140.png`（目检：`140. Ik maak een surprise met een kort gedicht. — surprise é uma expressão fixa`） |
| D10 | P7 来信仍 2 行逐字相同：`Sem cartas reais nem melhores textos:` (1783.27) / `exemplo; promessa passa para VOL.5.` (1811.67)；盒高 `lh` 不变（`P7 col3 ends 1927.0` 与修前同）；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d10.png`（目检） |
| D11 | 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px（≥20px）**；真墨末行 1209.00（卡片 1×）/ 1209.12（印 PDF 150dpi），余量 +20.60/+20.48px；盒底下 7px 条带双法均为 0 非纸像素；`P4 col3 ends 1229.6`；P4 其余内容不动、其余 7 页 SVG 除 p8 外字节一致 | `svg/p4-sport.svg`、crop `crop-p4-programma.png`（目检：末行在盒内，下有明显留白） |

## 6. 全部门禁结果

- **Build**：`run.py` rc=0、TOTAL 150、0 溢出（见 §4）。
- **Occlusion 真实审计**：`tools/occlusion_audit.py svg/` rc=0，**0 flags**。
- **p8 extract**：`p8.py extract --p8 svg/p8-toets.svg --total 150` noted set
  **150/150**。
- **p8 compare（核心 vs 本版，直接读 `p8-compare-delta.json` 本体）**：
  `status: CLEAN, total: 150, missing: [], extra_count: 0, uncertain: [],
  keydiff: [137, 138]`。137/138 是翻译题——键本身就是读者语，
  核心为中文（`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），
  本版为葡萄牙文（`As notícias do Sinterklaas passam todos os dias às 18:00.` /
  `Os dois primeiros passam aos quartos de final.`），按设计不同，非缺陷。
  修前 keydiff 同为 [137, 138]——但 P8 token 数 2372 → 2373（+1 = `kort`）；
  KIT build-3 所记“0 key diffs”是 gates.py 对 stdout 中 `key diff` 行的计数
  （JSON 列表本身当时即 [137, 138]），口径不同，特此说明。
- **Keycheck（三源逐题 verbatim 比对 `p8-compare-3way.json`）**：
  **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。Q140 三源 MATCH。
  （注：首轮比对 0/149 是脚本 bug——复用的 es 版脚本 regex 仍搜
  `— Respuesta:`，本版标记为 `— Resposta:`；修正标记后重跑得 149/149，
  修正只动了 scratch 脚本，未动任何版内文件。）
- **Freeze 标准核心比对**：`freeze.py baseline --build <core-nl> --core-svg
  <core-nl>/svg --out scratch/freeze-core` rc=0，**8/8 字节一致**；
  核心 shipped SVG 跑前后哈希不变（未碰核心）。
- **版内自比对（补充）**：clean-dir 重跑 `run.py` 再 sha256 比对，
  **8/8**（fanout gates.py `freeze_sha256` 项）；registry 导出重跑后
  SVG 哈希复核亦一致。
- **印/网文字层逐页一致**：PyMuPDF 位置排序，8 页 posdiff 0、msdiff 0
  （tokens 815/817/721/728/792/741/913/2373；P8 +1 vs build-3 的 2372，
  即 `kort`，其余 7 页逐页相同）；pdftotext 印 46,698 B = 网 46,698 B。
- **P8 最小 PDF 字号**：答案区 min **10.12pt**（median 10.12，184 spans）≥ 9.75pt。
- **全版孤儿标点两类横扫（重建 SVG，PIL + svglib 双 advance，1453 行）**：
  (a) 独行标点 **0**，(b) 行首标点 **0**，两方法 8 页全 0；
  brute-force 交叉检查：以标点开头的 `<text>` 元素 **0 个**。
  （CJK + 拉丁标点均纳入。）
- **Creambox**：TOTAL 4 flags，与修前**逐值相同**（P2 CREAM-BOTTOM、
  P2 PAGE-EDGE、P5 CREAM-BOTTOM、P7 CREAM-RIGHT），均为已知假阳性：
  P2/P5 盒底下 7px 条带逐像素探查 **0 非纸像素**；P6 标题右带
  x1862..1875 **0 非纸像素**；P2 `Ligue palavra-significado`（advance 右
  1862.7）实墨最右 1861（max<150  solid ink），在 1862 内容边内 1px——
  与 build-3 KIT 的裁决逐字一致；P7 `HET WOORD　PALAVRA DA SEMANA`
  实墨最右 1861，盒边 1862 内 1px（t=200 阈值在 1862 抓到 1 个抗锯齿
  边缘像素，solid ink 阈值为 1861）。P4（D11 盒）0 flags。**真溢出 0。**
- **Spill 横扫**：**0 spills**；P4 HET PROGRAMMA 盒（底 1229.6）无任何 below
  命中（仅 ABOVE 图注）；其余 BELOW 命中（+50.5/+60px）均为独立版块
  （gloss 框、下一盒标题），ABOVE/SIDE 均为图注/邻盒标题——与核心
  fix5 同类裁决；最近的 BELOW 命中为 +50.5px，未见任何 SIDE 命中。
- **盒标题横向真墨扫描**：共扫 59 个标题（38 次 Flow.head + 21 个奶油盒
  标题，PIL 真墨，卡片 1×）。按“盒/栏外边”计 **0 越边**：
  扫描器内垫线（盒右 −22px）报 4 个 OVER，经逐项裁决均为非溢出——
  P8 `A　VUL DE KRONIEK IN` 是扫描带（基线 −27.3px）误触 y≈177 整页横线
  （该行实墨 x 88..1861），标题本身 advance 234.9px、墨止约 x=323，
  其下划线按设计止于栏边 510.5；P2 `ZO ONTHOUD JE HET　LEMBRA-TE`
  实墨最右 945、盒外边 961，内 16px；P6 `VOOR OF TEGEN?　A FAVOR / CONTRA`
  实墨 1850、盒外边 1862，内 12px（即 KIT fix13 的 +11.5 clearance）；
  P7 `HET WOORD　PALAVRA DA SEMANA` solid ink 1861、盒外边 1862，内 1px。
  （任务所称 56 系估算，实测 59——nl-en 同款扫描亦为 59。）
- **Fanout 门禁套件**（`gates_delta.py`，即 build-3 同款 9 项）：
  **ALL PASS**（occlusion / p8_extract / p8_compare / freeze_sha256 /
  print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips /
  s11_svg——§1.1 off-palette {}、VOL.5 = 5 = core、paper fills 8）。
- D3 回归：P2 SVG 字节一致，D3 断行与余量与 build-3 相同，无需重测。

## 7. 新三 SHA（交付）

| 文件 | 字节 | SHA-256（修后，实测） | 旧值（build-3，历史） |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-pt.pdf`（印） | 12,672,019 | `dd74de0a45556e96fdfcc216a9d249bbae577ace249bfbc256dd564ef6e5113e` | `e85aa1a0…daac834` / 12,672,018 |
| `De-Lucerna-VOL4-nl-pt-web.pdf`（网） | 1,618,464 | `4e795b31f65273524128656f1a0a6064ba0f18efa93a29c191f15a2f58bf5e6b` | `a0c8c87b…146d85` / 1,618,472 |
| `2026-w47-nl-pt.text.md`（文） | 47,209 | `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f` | `865e659f…137efc` / 47,204 |

网 PDF 铁律：SHA 与字节大小均不可复现，只比文字层；交付的网 PDF 由本次
重建产生（文字层与印 PDF 逐页一致，见 §6）。

## 8. 改动文件清单与未动确认

- 改动（规范路径 `production/2026-w47/2026-w47-nl-pt/` 内）：`bslib4.py`、
  `content34.py`、`content56.py`、`content7.py`、`content8.py`（§3 对照）、
  `WEEKLY-KIT.md`（新 SHA + delta 节）。
- 未改动源码：`content12.py`、ABSTRACT.txt。
- 重建产物（同目录）：`svg/p4-sport.svg`、`svg/p8-toets.svg`（仅此 2 个 SVG
  变化）、`cards/*.png`、`De-Lucerna-VOL4-nl-pt.pdf`、
  `De-Lucerna-VOL4-nl-pt-web.pdf`；`2026-w47-nl-pt.text.md` 重导后仅 415 行变。
- 未动：core-nl（只读；三 SHA 复核仍为 fix5 定稿值）、其他版、staging 副本
  `fanout-nl/2026-w47-nl-pt/`（三 SHA 复核仍为 build-3 值）、tools/。
  未 commit、未 push。
- 待 proof1（独立校对员）定稿后由协调员统一 commit/push。
