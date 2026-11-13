# DELTA-LOG — 2026-W47 nl-es, core fix3 + fix4 + fix5 同步

- 版：`2026-w47-nl-es`（荷兰语目标 × 西班牙语读者版），VOL.4，8 版，150 题
- 日期：2026-11-11
- 任务：core-nl fix3（D6/D7）+ fix4（D8/D9/D10）+ fix5（D11）同步到本版。
  只改本版自己的源文件，不碰核心、不碰其他版、不碰 staging。不 commit、不 push。
  修后由另一位独立校对员 proof1，不要自己定稿。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-es/`
  （日志、门禁证据、registry、比对 JSON、crops 均在此）
- 工作区：repo 克隆 `~/workspace/weekly-git`；解释器 `tools/venv/bin/python`；
  TMPDIR = 本 scratch 目录
- 核心对照（只读）：`production/2026-w47/core-nl/`，fix5 定稿已核对——
  印 `b7d4a9cd…` / 25,955,578 B，网 `5a47449c…` / 2,104,000 B，
  文 `0b97a48d…` / 44,093 B，三件与任务给出的 SHA 逐字节一致。
  权威记录：core-nl `FIX-LOG.md`（fix3、fix4、fix5 全文，开工前已通读）。

## 0. 开工探针与路径问题

- 探针：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；
  `/dev/null` 正常（字符设备）；scratch 目录真实写文件成功（probe.txt）。
- **路径问题：任务所称的规范路径 `production/2026-w47/2026-w47-nl-es/` 在开工时
  不存在**（与 nl-de 试点相同）。W47 的 10 个 nl fanout 版只存在于 staging
  目录 `production/2026-w47/fanout-nl/`。处理：把 staging 的 nl-es 版整目录
  `cp -a` 到规范路径，`diff -r --exclude=__pycache__` 校验**完全一致**
  （diff-rc=0；仅两条无害的 ownership 保留警告），staging 副本全程未动；
  此后全部 delta 工作都在规范路径做。
- 修前身份核对（三件 SHA，实测 = re-fanout 报告 §1 的 build-3 值）：印
  `0388d59c7e7085bbd4a733f235081f26dac901489ebe1f10ee121f391306b771` /
  12,669,541 B；网 `5b4f81621c77233cf9d89fa44eb6a1a249fb943f39d64ca96749e70f39cd7a21`
  / 1,616,172 B；文 `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb`
  / 47,649 B。修前 8 个 SVG SHA 存 `pre-svg-sha.txt`。
  终核时 staging 与 core-nl 三 SHA 复核仍为上述值（未动）。

## 1. 修前实测：D6/D7/D8/D10 在本版并不存在；D9 早已修好；D11 是真缺陷

西班牙语读者层文字与核心中文桥接文字断行不同——修前 SVG 实测：

| 点 | 修前 SVG 实测 | 结论 |
|---|---|---|
| D6 P3 桥接 | `Completa en perfecto. Fíjate en los` (y=2303.5) / `auxiliares hebben/zijn.` (y=2333.225)，2 行，句末 `.` 在行 2 末尾 | 无孤儿 |
| D7 P7 桥接 | 3 行：`de wedstrijd partido; de groepswinst` (725.66) / `victoria de grupo; de kwartfinale cuartos de` (755.39) / `final; scoren marcar.` (785.11)，句末 `.` 在行末 | 无孤儿 |
| D8 P6 图注 | 4 行：`Datos de práctica: cifras inventadas, solo` / `para practicar, no una encuesta real.` / `Pregunta: ¿qué pones en tu zapato? (100` / `jóvenes)`，基线 635.02/659.44/683.86/708.28 | 无行首标点 |
| D10 P7 来信 | 2 行：`Sin cartas reales ni mejores textos:` (1783.27) / `ejemplo; la promesa pasa a VOL.5.` (1811.67) | 无行首标点 |
| D9 Q140 | registry 键、text.md:415 答案、P8 节点三源**同已含 `kort`**：`Ik maak een surprise met een kort gedicht.`（本版在 re-fanout 时已独立修好，见 KIT §13；核心 FIX-LOG fix4 也注明此事） | **已修好，无需改动** |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=611.0>` 底 1202.6；末行 `18:45 uur.` 基线 y=1209.49，**盒底外 +6.89px** | **真缺陷** |

全版孤儿标点横扫（修前，双类，CJK + 拉丁标点，PIL + svglib 双 advance，
1452 行）：(a) 独行标点 0，(b) 行首标点 0，8 页全 0；brute-force 以标点
开头的 `<text>` 元素 0 个。因此 D6/D7/D8/D10 的同步是**结构性**的：
机制照搬 + 本版文字重算 w，选出的 w 必须**精确复现当前干净断行**（行内容、
行数、基线全不变），重建 SVG 以 p3/p6/p7 字节一致为证。D11 是唯一真修；
D9 连结构同步都不需要（源码本就与核心 fix4 后的键一致）。

## 2. Width scan（本版自己的文字 + 本版 `svglib.wrap()`，0.5px 步进）

CW = 422.5。取“精确复现当前各行”的 w 区间中点（核心数值一律不抄）：

| 点 | 文字（字体/字号） | 当前 w | 区间（同行内容） | 选中 w |
|---|---|---|---|---|
| D6 桥接 | `Completa en perfecto. Fíjate en los auxiliares hebben/zijn.`（sans 20.5） | CW=422.5 | 329.5–425.5（2 行） | **377.5**（中点） |
| D7 桥接 | `de wedstrijd partido; … scoren marcar.`（sans 20.5） | CW=422.5 | 414.5–424.5（3 行） | **419.5**（中点） |
| D8 图注 | `Datos de práctica: … (100 jóvenes)`（sans 18.5） | CW−44=378.5 | 349.5–392.0（4 行） | **capcn_w=370.75**（中点） |
| D10 来信 | `Sin cartas reales ni mejores textos: ejemplo; la promesa pasa a VOL.5.`（sans 20） | CW−44=378.5 | 319.5–405.5（2 行） | **dt_zh_w=362.5**（中点） |

D11 事实句（serif 21.5，CW−44）：5 句断行 3/3/3/2/3 = 14 行，与核心一致；
`sh` 旧 611.0 → 新 638.0（+27）。顶留 89 = 16（pad）+ 52（标题块）+ 21
（para y-offset），本版 `content34.py` 渲染循环形状与核心相同（`yy3 = sy3+16`、
标题后 `yy3 += 52`、事实 `p.para(…, yy3+21, …)`），盒顶 sy3=591.6 不变。
实测基线序列与核心 FIX-LOG 一致：首行 680.60 … 末行 1209.49，盒顶偏移 617.89。

## 3. 改动源码行前后对照（仅 5 个源文件 + KIT；`content8.py` 未动）

`diff -r`（规范路径 vs staging 副本，排除 svg/cards/PDF）只显示以下 5 文件：

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
-e.bridge("Completa en perfecto. Fíjate en los auxiliares hebben/zijn.")
+e.bridge("Completa en perfecto. Fíjate en los auxiliares hebben/zijn.", w=377.5)  # delta D6: width-scan band 329.5–425.5px keeps the 2 lines; mid 377.5
```

### `content34.py:130` — D11 盒高公式（P4 HET PROGRAMMA；第 37 行的 P3 SINTERKLAAS 盒不动）
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
-a.bridge("de wedstrijd partido; de groepswinst victoria de grupo; de kwartfinale cuartos de final; scoren marcar.")
+a.bridge("de wedstrijd partido; de groepswinst victoria de grupo; de kwartfinale cuartos de final; scoren marcar.", w=419.5)  # delta D7: width-scan band 414.5–424.5px keeps the 3 lines; mid 419.5
```

### `content7.py:91–92, 103` — D10 两处同用 `dt_zh_w`
```diff
 dt_zh = "Sin cartas reales ni mejores textos: ejemplo; la promesa pasa a VOL.5."
+# delta D10: dt_zh wrap width 362.5. Width scan (sans 20): band
+# 319.5–405.5px wraps to the same 2 lines; 362.5 is the band middle.
+dt_zh_w = 362.5
-lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + ...
+lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + ...
-yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
+yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
```

### `content56.py:143–144, 159` — D8 两处同用 `capcn_w`
```diff
 capcn = "Datos de práctica: cifras inventadas, solo para practicar, no una encuesta real. Pregunta: ¿qué pones en tu zapato? (100 jóvenes)"
+# delta D8: capcn wrap width 370.75. Width scan (sans 18.5): band
+# 349.5–392.0px wraps to the same 4 lines; 370.75 is the band middle.
+capcn_w = 370.75
-ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
+ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
-yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
+yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
```

### `content8.py` — D9 无改动
本版 registry 键（`content8.py:75`）、text.md:415 答案、P8 节点在修前
已同为 `Ik maak een surprise met een kort gedicht.`，注记
`surprise: expresión fija; corto = kort` 不变。`kort` 在本版内有据：
题干 `Hago una sorpresa con un poema corto.`（poema corto = 小诗）及荷兰语
文章句 text.md:238 `maak je liever een surprise met een gedicht?` 对应
核心 text.md:73 `kort is ook goed`。无源码行可改，未虚构缺陷。

### `WEEKLY-KIT.md`
- “Files delivered”三 SHA 更新为 build-4 新值；文末新增 “Delta
  (core fix3 + fix4 + fix5, 2026-11-11, build 4)” 一节，旧 SHA 全数保留为历史。

## 4. 重建

- `run.py` rc=0、TOTAL 150、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31；
  0 FLOW OVERFLOW / HEAD TOO WIDE。`P4 col3 ends 1229.6`（旧 1202.6）；
  `P6 chart ends 717`、`P7 col3 ends 1927.0` 与修前一致。
- `render.py` rc=0，印 PDF 12,669,539 B。SVG 哈希 vs 修前：**仅
  `p4-sport.svg`（D11）变化**，其余 7 个字节一致。
- text.md 重导（`export_fanout.py`，rc=0）：47,649 B，**与修前逐字节一致**
  （D9 已修好、无文字改动）；142 单题 + 2 配对头 + 8 配对项 = 150；
  8 金句、6 gloss。registry 重导（`dump_reg_delta.py`）：150 条，
  by page / by level 与 build 一致。
- `webpdf.py` rc=0：1,616,177 B（< 7 MB），text layer 46,814 B。
  （注：第一次误用 `webpdf.py <print-pdf> <web-pdf>` 调用，rc=2
  `no SVGs in …`——该工具签名的正确用法是 `webpdf.py <svg-dir> <out-pdf>`，
  已按 build_one.sh 的用法重跑，rc=0；误调用未写坏任何文件，旧网 PDF
  当时仍在原位。）

## 5. 六处修复点逐项实测（重建 SVG 证据）

| 点 | 实测值（重建后） | 证据 |
|---|---|---|
| D6 | P3 桥接仍 2 行，内容与修前逐字相同：`Completa en perfecto. Fíjate en los` (2303.5) / `auxiliares hebben/zijn.` (2333.225)；下游 y 无位移（p3 SVG 字节一致） | `svg/p3-cultuur.svg`、crop `crop-p3-d6.png`（目检） |
| D7 | P7 桥接仍 3 行逐字相同，末行 `final; scoren marcar.` (785.11)；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d7.png`（目检） |
| D8 | P6 图注仍 4 行，基线 635.02/659.44/683.86/708.28 全不变；盒高 `ch` 不变（`P6 chart ends 717` 与修前同）；零 y 位移（p6 SVG 字节一致） | `svg/p6-verdieping.svg`、crop `crop-p6-d8.png`（目检） |
| D9 | 三源一致（修前即一致，无改动）：registry 键 = text.md:415 答案 = P8 节点，均为 `Ik maak een surprise met een kort gedicht.`；其余 149 键未动（3-way 比对见 §6） | `svg/p8-toets.svg` (y=2189.3)、crop `crop-p8-q140.png`（目检：`140. Ik maak een surprise met een kort gedicht. — surprise: expresión fija; corto = kort`） |
| D10 | P7 来信仍 2 行逐字相同：`Sin cartas reales ni mejores textos:` (1783.27) / `ejemplo; la promesa pasa a VOL.5.` (1811.67)；盒高 `lh` 不变（`P7 col3 ends 1927.0` 与修前同）；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d10.png`（目检） |
| D11 | 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px（≥20px）**；真墨末行 1209，余量 +20.60px；盒底下 7px 条带 0 非纸像素；`P4 col3 ends 1229.6`；P4 其余内容不动、其余 7 页 SVG 字节一致 | `svg/p4-sport.svg`、crop `crop-p4-programma.png`（目检：末行在盒内，下有明显留白） |

## 6. 全部门禁结果

- **Build**：`run.py` rc=0、TOTAL 150、0 溢出（见 §4）。
- **Occlusion 真实审计**：`tools/occlusion_audit.py svg/`（未用 --selftest，
  但自检行照常输出）rc=0，**0 flags**。
- **p8 extract**：`p8.py extract --p8 svg/p8-toets.svg --total 150` noted set
  **150/150**。
- **p8 compare（核心 vs 本版，直接读 `p8-compare.json` 本体）**：
  `status: CLEAN, total: 150, missing: [], extra_count: 0, uncertain: [],
  keydiff: [137, 138]`。137/138 是翻译题——键本身就是读者语，
  核心为中文（`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），
  本版为西班牙文（`El noticiario de Sinterklaas se emite cada día a las 18:00.` /
  `Los dos primeros pasan a cuartos de final.`），按设计不同，非缺陷。
  修前 keydiff 同为 [137, 138]——D9 在本版修前即已一致，无 140 可移；
  KIT build-3 所记“0 key diffs”是 gates.py 对 stdout 中 `key diff` 行的计数
  （JSON 列表本身当时即 [137, 138]），口径不同，特此说明。
- **Keycheck（三源逐题 verbatim 比对 `p8-compare-3way.json`）**：
  **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。Q140 三源 MATCH。
- **Freeze 标准核心比对**：`freeze.py baseline --build <core-nl> --core-svg
  <core-nl>/svg --out scratch/freeze-core` rc=0，**8/8 字节一致**；
  核心 shipped SVG 跑前后哈希不变（未碰核心）。
- **版内自比对（补充）**：clean-dir 重跑 `run.py` 再 sha256 比对，
  **8/8**（fanout gates.py `freeze_sha256` 项）。
- **印/网文字层逐页一致**：PyMuPDF 位置排序，8 页 posdiff 0、msdiff 0
  （tokens 812/820/727/731/794/743/913/2403；与 build-3 逐页相同——D9
  无改动故 P8 token 数不变）；pdftotext 印 46,814 B = 网 46,814 B，
  且印 PDF 文字层与 build-3 **逐字节一致**（无一字改动）。
- **P8 最小 PDF 字号**：答案区 min **10.12pt**（median 10.12，184 spans）≥ 9.75pt。
- **全版孤儿标点两类横扫（重建 SVG，PIL + svglib 双 advance，1452 行）**：
  (a) 独行标点 **0**，(b) 行首标点 **0**，两方法 8 页全 0；
  brute-force 交叉检查：以标点开头的 `<text>` 元素 **0 个**。
  （CJK + 拉丁标点均纳入；修前横扫亦为 0/0，见 §1。）
- **Creambox**：TOTAL 3 flags，与修前**逐值相同**（P2/P5 CREAM-BOTTOM、
  P6 CREAM-RIGHT），均为已知假阳性：P2/P5 盒底下 7px 条带逐像素探查
  **0 非纸像素**；P6 标题实墨最右 1861（lum<90  solid ink），在盒内 1px，
  仅 1px 抗锯齿边缘触 1862 线——与 re-fanout §6 的裁决逐字一致（且新旧
  两版卡片该处像素逐个相同）。P4（D11 盒）0 flags。**真溢出 0。**
- **Spill 横扫**：**0 spills**；P4 HET PROGRAMMA 盒（底 1229.6）无任何 below
  命中（仅 ABOVE 图注）；其余 BELOW 命中（+24/+32/+50.5/+60px）均为独立版块
  （下一节标题、提示语、gloss），ABOVE/SIDE 均为图注/邻盒标题——与核心
  fix5 同类裁决。
- **Fanout 门禁套件**（`gates_delta.py`，即 build-3 同款 9 项）：
  **ALL PASS**（occlusion / p8_extract / p8_compare / freeze_sha256 /
  print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips /
  s11_svg——§1.1 off-palette {}、VOL.5 = 5 = core、paper fills 8）。
- D3 回归：P2 SVG 字节一致，D3 断行与余量与 build-3 相同，无需重测。

## 7. 新三 SHA（交付）

| 文件 | 字节 | SHA-256（修后，实测） | 旧值（build-3，历史） |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-es.pdf`（印） | 12,669,539 | `45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` | `0388d59c…306b771` / 12,669,541 |
| `De-Lucerna-VOL4-nl-es-web.pdf`（网） | 1,616,177 | `47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` | `5b4f8162…9cd7a21` / 1,616,172 |
| `2026-w47-nl-es.text.md`（文） | 47,649 | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` | 同值（未变） / 47,649 |

网 PDF 铁律：SHA 与字节大小均不可复现，只比文字层；交付的网 PDF 由本次
重建产生（文字层与印 PDF 逐页一致，见 §6）。

## 8. 改动文件清单与未动确认

- 改动（规范路径 `production/2026-w47/2026-w47-nl-es/` 内）：`bslib4.py`、
  `content34.py`、`content56.py`、`content7.py`（§3 对照）、
  `WEEKLY-KIT.md`（新 SHA + delta 节）。
- 未改动源码：`content8.py`（D9 修前即一致）、`content12.py`、ABSTRACT.txt。
- 重建产物（同目录）：`svg/p4-sport.svg`（仅此 1 个 SVG 变化）、
  `cards/*.png`、`De-Lucerna-VOL4-nl-es.pdf`、
  `De-Lucerna-VOL4-nl-es-web.pdf`；`2026-w47-nl-es.text.md` 重导后逐字节一致。
- 未动：core-nl（只读；三 SHA 复核仍为 fix5 定稿值）、其他版、staging 副本
  `fanout-nl/2026-w47-nl-es/`（三 SHA 复核仍为 build-3 值）、tools/。
  未 commit、未 push。
- 待 proof1（独立校对员）定稿后由协调员统一 commit/push。
