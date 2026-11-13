# DELTA-LOG — 2026-W47 nl-fr, core fix3 + fix4 + fix5 同步

- 版：`2026-w47-nl-fr`（荷兰语目标 × 法语读者版），VOL.4，8 版，150 题
- 日期：2026-11-11
- 任务：core-nl fix3（D6/D7）+ fix4（D8/D9/D10）+ fix5（D11）同步到本版。
  只改本版自己的源文件，不碰核心、不碰其他版。不 commit、不 push。
  修后由另一位独立校对员 proof1，不要自己定稿。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-fr/`
  （日志、门禁证据、registry、比对 JSON、crops、8 页渲染均在此）
- 工作区：repo 克隆 `~/workspace/weekly-git`；解释器 `tools/venv/bin/python`；
  TMPDIR = 本 scratch 目录
- 核心对照（只读）：`production/2026-w47/core-nl/`，fix5 定稿已核对——
  印 `b7d4a9cd…` / 25,955,578 B，网 `5a47449c…` / 2,104,000 B，
  文 `0b97a48d…` / 44,093 B，三件与任务给出的 SHA 逐字节一致。
  权威记录：core-nl `FIX-LOG.md`（fix3、fix4、fix5 全文），开工前已通读。

## 0. 开工探针与路径问题

- 探针：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；
  `/dev/null` 正常（字符设备）；goals-side probe 文件写入成功。
- **路径问题：任务所称的规范路径 `production/2026-w47/2026-w47-nl-fr/` 在开工时
  不存在。** W47 的 10 个 nl fanout 版只存在于 staging 目录
  `production/2026-w47/fanout-nl/`。处理：把 staging 的 nl-fr 版整目录 `cp -a`
  到规范路径，`diff -r --exclude=__pycache__` 校验**完全一致**（仅两条无害的
  ownership 保留警告），staging 副本全程未动；此后全部 delta 工作都在规范路径做。
- 修前身份核对（三件 SHA，实测 = re-fanout 报告 `scratch-refanout-nl/FANOUT-REPORT-nl.md`
  §1 的 fr 行 build-5 值）：印
  `50d9182b11a9b587f6cb4dd726cb1379387d7c5c7b52a2b36903a6c627aca544` /
  12,656,012 B；网 `9e90d0ab053b8fef4c8c1534294060bb0110aa5e5a395c1d11c572a9881084e4`
  / 1,612,638 B；文 `21888192450ff4f8350ed5c0fd091e4de44e4425fd593103b35358cdef43e7c9`
  / 47,739 B。修前 8 个 SVG SHA 存 `pre/svg-sha-pre.txt`；修前 text.md 存 `pre/text-pre.md`。

## 1. 修前实测：D6/D7/D8/D10 在本版并不存在（关键发现）

法语读者层文字与核心中文桥接文字断行不同——修前 SVG 实测：

| 点 | 修前 SVG 实测 | 结论 |
|---|---|---|
| D6 P3 桥接 | `Complète au passé composé. Attention aux` (y=2303.5) / `auxiliaires hebben/zijn.` (y=2333.225)，2 行，句末 `.` 在行 2 末尾 | 无孤儿 |
| D7 P7 桥接 | 3 行：`de wedstrijd match ; de groepswinst victoire` / `de groupe ; de kwartfinale quart de finale ;` / `scoren marquer.` (y=725.66/755.39/785.11)，句末 `.` 在行末 | 无孤儿 |
| D8 P6 图注 | 4 行：`Données d'exercice : des chiffres inventés,` / `pour l'exercice seulement, pas une vraie` / `enquête. Question : que mets-tu dans ta` / `chaussure ? (100 jeunes)`，基线 635.02/659.44/683.86/708.28 | 无行首标点 |
| D10 P7 来信 | 2 行：`Aucune vraie lettre ni meilleur texte : un` (1783.27) / `exemple ; promesse reportée à VOL.5.` (1811.67) | 无行首标点 |
| D9 Q140 | registry 键、text.md:415 答案、P8 节点三源同错：`Ik maak een surprise met een gedicht.`（缺 `kort`） | **真缺陷** |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=611.0>` 底 1202.6；末行 `18:45 uur.` 基线 y=1209.49，**盒底外 +6.89px** | **真缺陷** |

全版孤儿标点横扫（修前，双类，CJK + 拉丁标点，`orphan_sweep_delta.py`）：
(a) 独行标点 0，(b) 行首标点 0，PIL 与 svglib 双 advance、8 页全 0，
1,458 行；brute-force 以标点开头的 `<text>` 元素 0 个。因此这四处的同步是
**结构性**的：机制照搬 + 本版文字重算 w，选出的 w 必须**精确复现当前干净断行**
（行内容、行数、基线全不变），重建 SVG 以 p3/p6/p7 字节一致为证。D9、D11 是真修。

## 2. Width scan（本版自己的文字 + 本版 `svglib.wrap()`，0.1px 步进定带）

CW = 422.5。取“精确复现当前各行”的 w 区间中点（核心数值一律不抄）：

| 点 | 文字（字体/字号） | 当前 w | 区间（同行内容） | 选中 w |
|---|---|---|---|---|
| D6 桥接 | `Complète au passé composé. Attention aux auxiliaires hebben/zijn.`（sans 20.5） | CW=422.5 | 410.8–450.0（2 行；最长行 advance 410.72） | **430.4**（中点） |
| D7 桥接 | `de wedstrijd match ; … scoren marquer.`（sans 20.5） | CW=422.5 | 419.2–447.7（3 行；最长行 advance 419.12） | **433.45**（中点） |
| D8 图注 | `Données d'exercice : … (100 jeunes)`（sans 18.5） | CW−44=378.5 | 359.7–404.8（4 行；最长行 advance 359.61） | **capcn_w=382.25**（中点） |
| D10 来信 | `Aucune vraie lettre ni meilleur texte : un exemple ; promesse reportée à VOL.5.`（sans 20） | CW−44=378.5 | 367.5–450.0（2 行；最长行 advance 367.45） | **dt_zh_w=408.75**（中点） |

D11 事实句（serif 21.5，CW−44）：5 句断行 3/3/3/2/3 = 14 行，与核心一致；
`sh` 旧 611.0 → 新 638.0（+27）。顶留 89 = 16（pad）+ 52（标题块）+ 21
（para y-offset），本版 `content34.py` 渲染循环形状与核心相同（`yy3 = sy3+16`、
标题后 `yy3 += 52`、事实 `p.para(…, yy3+21, …)`），盒顶 sy3=591.6 不变。
`w` 只进 `wrap()`（`Flow.para` 分行路径渲染用 `self.x` 与行串本身），故区间内
的 w 取值只改断行判定、不改渲染位置——p3/p6/p7 字节一致为证。

## 3. 改动源码行前后对照（仅 5 个源文件 + KIT）

`diff -r`（规范路径 vs staging 副本，排除 svg/cards/PDF）只显示以下 5 文件：

### `bslib4.py` — D6 机制（照搬核心 fix3 的 `w` 机制）
```diff
-    def para(self, s, size=24, kind="serif", bold=False, fill=INK, lh=1.52, gap=10, split=True, italic=False):
+    def para(self, s, size=24, kind="serif", bold=False, fill=INK, lh=1.52, gap=10, split=True, italic=False, w=None):
+        # w: optional wrap-width override (default: column width). Synced
+        # from core-nl fix3 (D6/D7 mechanism); per-edition w values are
+        # recomputed from this edition's own reader text by width scan.
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
-e.bridge("Complète au passé composé. Attention aux auxiliaires hebben/zijn.")
+e.bridge("Complète au passé composé. Attention aux auxiliaires hebben/zijn.", w=430.4)  # delta D6: width-scan band 410.8–450.0px keeps the 2 lines; mid 430.4 (structural sync — no orphan pre-fix)
```

### `content34.py:130` — D11 盒高公式（P4 HET PROGRAMMA；第 37 行的 P3 SINTERKLAAS 盒不动）
```diff
-sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
+sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30  # delta D11: top reserve 62 → 89 = 16 (pad) + 52 (title block) + 21 (para y-offset); last line was 6.89px below the box
```

### `content7.py:19` — D7 调用点
```diff
-a.bridge("de wedstrijd match ; de groepswinst victoire de groupe ; de kwartfinale quart de finale ; scoren marquer.")
+a.bridge("de wedstrijd match ; de groepswinst victoire de groupe ; de kwartfinale quart de finale ; scoren marquer.", w=433.45)  # delta D7: width-scan band 419.2–447.7px keeps the 3 lines; mid 433.45 (structural sync — no orphan pre-fix)
```

### `content7.py:91–92, 102` — D10 两处同用 `dt_zh_w`
```diff
 dt_zh = "Aucune vraie lettre ni meilleur texte : un exemple ; promesse reportée à VOL.5."
+# delta D10: dt_zh wrap width 408.75. Width scan (sans 20): identical 2-line band 367.5–450.0px; mid 408.75 (structural sync — no line-initial punctuation pre-fix).
+dt_zh_w = 408.75
-lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + ...
+lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + ...
-yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
+yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
```

### `content56.py:143–144, 158` — D8 两处同用 `capcn_w`
```diff
 capcn = "Données d'exercice : des chiffres inventés, pour l'exercice seulement, pas une vraie enquête. Question : que mets-tu dans ta chaussure ? (100 jeunes)"
+# delta D8: capcn wrap width 382.25. Width scan (sans 18.5): identical 4-line band 359.7–404.8px; mid 382.25 (structural sync — no line-initial punctuation pre-fix).
+capcn_w = 382.25
-ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
+ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
-yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
+yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
```

### `content8.py:75` — D9 键补 kort（目标语荷兰语句，直接照搬核心）
```diff
-f.ex("B2", "Traduction", "Ik maak een surprise met een gedicht.", "surprise est une expression fixe",
+f.ex("B2", "Traduction", "Ik maak een surprise met een kort gedicht.", "surprise est une expression fixe",
```
注记不动。`kort` 在本版内有据：荷兰语文章句 text.md:72
`Twee: schrijf een gedicht — kort is ook goed.`（与核心的论证相同），
法语题干 `Je fais une surprise avec un petit poème.` 含“petit”（小）。
KIT build-5 曾记此项“recorded not fixed”（当时协调员令只改 es 版、等核心
统一修）；核心 fix4 已修，本 delta 随核心同步。

### `WEEKLY-KIT.md`
- “Files delivered”三 SHA 更新为 build-6 新值；文末新增 “Delta
  (core fix3 + fix4 + fix5, 2026-11-11, build 6)” 一节，旧 SHA 全数保留为历史。

## 4. 重建

- `run.py` rc=0、TOTAL 150、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31；
  0 FLOW OVERFLOW / HEAD TOO WIDE。`P4 col3 ends 1229.6`（旧 1202.6）；
  `P6 chart ends 717`、`P6 col3 ends 1052.0`、`P7 col3 ends 1927.0` 与修前一致。
- `render.py` rc=0。SVG 哈希 vs 修前：**仅 `p4-sport.svg`（D11）与
  `p8-toets.svg`（D9）变化**，其余 6 个字节一致。
- text.md 重导（`scratch-fanout-nl/export_fanout.py`，rc=0）：47,739 → 47,744 B，
  diff 恰好 text.md:415 一行（`kort `，+5 B）；142 单题 + 2 配对头 + 8 配对项 = 150；
  8 金句、6 gloss。registry 重导（`dump_reg_delta.py`）：150 条，
  by page / by level 与 build 一致。
- `webpdf.py` rc=0：1,612,639 B（< 7 MB），text layer 46,867 B。

## 5. 六处修复点逐项实测（重建 SVG 证据）

| 点 | 判定 | 实测值（重建后） | 证据 |
|---|---|---|---|
| D6 | 结构同步 | P3 桥接仍 2 行，内容与修前逐字相同：`Complète au passé composé. Attention aux` (2303.5) / `auxiliaires hebben/zijn.` (2333.225)，句末 `.` 在行末；下游 y 无位移（p3 SVG 字节一致） | `svg/p3-cultuur.svg`、crop `crop-p3-d6.png`（目检） |
| D7 | 结构同步 | P7 桥接仍 3 行逐字相同，末行 `scoren marquer.` (785.11)；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d7.png`（目检） |
| D8 | 结构同步 | P6 图注仍 4 行，基线 635.02/659.44/683.86/708.28 全不变；盒高 `ch` 不变（`P6 chart ends 717`、`P6 col3 ends 1052.0` 与修前同）；零 y 位移（p6 SVG 字节一致） | `svg/p6-verdieping.svg`、crop `crop-p6-d8.png`（目检） |
| D9 | **真修** | 三源一致：registry 键 = text.md:415 答案 = P8 节点，均为 `Ik maak een surprise met een kort gedicht.`；其余 149 键未动（3-way 比对见 §6） | `svg/p8-toets.svg` (y=2221.54)、crop `crop-p8-q140.png`（目检） |
| D10 | 结构同步 | P7 来信仍 2 行逐字相同：`Aucune vraie lettre ni meilleur texte : un` (1783.27) / `exemple ; promesse reportée à VOL.5.` (1811.67)；盒高 `lh` 不变（`P7 col3 ends 1927.0` 与修前同）；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d10.png`（目检） |
| D11 | **真修** | 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px（≥20px）**；真墨最低行 1209，余量 +20.6px；盒底下 7px 条带 0 非纸像素；`P4 col3 ends 1229.6`；P4 其余内容不动、其余 7 页 SVG 字节一致（D9 的 p8 除外） | `svg/p4-sport.svg`、crop `crop-p4-programma.png`（目检：末行在盒内，下有明显留白） |

## 6. 全部门禁结果

- **Build**：`run.py` rc=0、TOTAL 150、0 溢出（见 §4）。
- **Occlusion 真实审计**：`tools/occlusion_audit.py svg/`（未用 --selftest，
  但自检行照常输出）rc=0，**0 flags**（自检 planted 6 类全触发，干净对照静默）。
- **p8 extract**：`p8.py extract --total 150` noted set **150/150**。
- **p8 compare（核心 vs 本版）**：`p8.py compare --json p8-compare.json`，
  直接读本体：`status: CLEAN, total: 150, missing: [], extra: [],
  uncertain: [], keydiff: [137, 138]`。137/138 是翻译题——键本身就是读者语，
  核心为中文（`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），
  本版为法文（`Le journal de Sinterklaas passe chaque jour à 18 h 00.` /
  `Les deux premiers passent en quart de finale.`），按设计不同，非缺陷。
  修前 keydiff 为 [137, 138, 140]——D9 把 140 移出了该表。KIT build-4 所记
  “0 key diffs”是 gates.py 对 stdout 中 `key diff` 行的计数（JSON 列表本身
  当时即 [137, 138, 140]），口径不同，特此说明；build-5 只记 “compare CLEAN”。
- **Keycheck（三源逐题 verbatim 比对 `p8-compare-3way.json`）**：
  **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。
- **Freeze 标准核心比对**：`freeze.py baseline --build <core-nl> --core-svg
  <core-nl>/svg --out scratch/freeze-core` rc=0，**8/8 字节一致**；
  核心 shipped SVG 跑前后哈希不变（未碰核心）。
- **版内自比对（补充）**：clean-dir 重跑 `run.py` 再 sha256 比对，
  **8/8**（fanout gates.py `freeze_sha256` 项）。
- **印/网文字层逐页一致**：PyMuPDF 位置排序，8 页 posdiff 0、msdiff 0
  （tokens 819/824/722/725/799/739/944/2437；P8 2437 vs build-5 的 2436，
  +1 = `kort`）；pdftotext 印 46,867 B = 网 46,867 B。
  印 PDF 文字层前后 diff（vs staging build-5）：恰好 Q140 一行（`kort`），
  D11 不改文字，零其他差异。
- **P8 最小 PDF 字号**：答案区 min **10.12pt**（median 10.12，187 spans）≥ 9.75pt。
- **全版孤儿标点两类横扫（重建 SVG，PIL + svglib 双 advance，1458 行）**：
  (a) 独行标点 **0**，(b) 行首标点 **0**，两方法 8 页全 0；
  brute-force 交叉检查：以标点开头的 `<text>` 元素 **0 个**。
  （CJK + 拉丁标点均纳入；修前横扫亦为 0/0，见 §1。）
- **Creambox**：TOTAL 3 flags，与修前**完全相同**的三处（staging 预建 SVG
  复核一致）：P1 CREAM-RIGHT（`DE WEEK IN CIJFERS　EN CHIFFRES`，几何右
  956.5 vs 盒右 961.0）与 P2/P5 CREAM-BOTTOM（`rédaction.` / `envoie-les.`）。
  像素裁决（卡片 PNG 1:1，`creambox_probe.py`）：盒底下 7px 条带逐像素探查
  **0 非纸像素**；真墨余量 P1 右 +9.0 / P2 +6.8 / P5 +7.5px——三处均为
  已知假阳性（几何余量用拉丁 0.3×size 下行 allowance 量无下行字母的末行；
  P1 是 8px 警告带内的墨，墨本身在盒内）。P4（D11 盒）0 flags。
  **真溢出 0。**
- **Spill 横扫**：**0 spills**；P4 HET PROGRAMMA 盒（底 1229.6）无任何 below
  命中；其余 BELOW 命中（+24/+32/+50.5/+50.5/+60/+60px）均为独立版块（下一节标题、
  提示语、gloss），ABOVE/SIDE 均为图注/邻盒标题——与核心 fix5 同类裁决。
- **Fanout 门禁套件**（`gates_delta.py`，即 build-5 同款 9 项）：
  **ALL PASS**（occlusion / p8_extract / p8_compare / freeze_sha256 /
  print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips /
  s11_svg——§1.1 off-palette {}、VOL.5 = 5 = core、paper fills 8）。
  注：`scratch-refanout-nl/check_one.py` 未用——它硬编码 fanout-nl 路径与
  backup/ 对照，只服务 re-fanout，不适用于 delta 规范路径。
- D3 回归：P2 SVG 字节一致，D3 断行与余量与 build-5 相同，无需重测。
- 8 页全看（150dpi `render/p1–p8.png`）：P1–P8 干净，无新缺陷。

## 7. 新三 SHA（交付）

| 文件 | 字节 | SHA-256（修后，实测） | 旧值（build-5，历史） |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-fr.pdf`（印） | 12,656,006 | `6aedb91fdc857b2ae545795b490c10b95400925ab1f430c658ca34922fd92d47` | `50d9182b…aca544` / 12,656,012 |
| `De-Lucerna-VOL4-nl-fr-web.pdf`（网） | 1,612,639 | `4f78d3a7c804ceb6d57fbde3e94cc91da21cf12c37360d4203238abf21a02f06` | `9e90d0ab…84e4` / 1,612,638 |
| `2026-w47-nl-fr.text.md`（文） | 47,744 | `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` | `21888192…e7c9` / 47,739 |

网 PDF 铁律：SHA 与字节大小均不可复现，只比文字层；交付的网 PDF 由本次
重建产生（文字层与印 PDF 逐页一致，见 §6）。

## 8. 改动文件清单与未动确认

- 改动（规范路径 `production/2026-w47/2026-w47-nl-fr/` 内）：`bslib4.py`、
  `content34.py`、`content56.py`、`content7.py`、`content8.py`（§3 对照）、
  `WEEKLY-KIT.md`（新 SHA + delta 节）。
- 重建产物（同目录）：`svg/p4-sport.svg`、`svg/p8-toets.svg`（仅此 2 个 SVG
  变化）、`cards/*.png`、`De-Lucerna-VOL4-nl-fr.pdf`、
  `De-Lucerna-VOL4-nl-fr-web.pdf`、`2026-w47-nl-fr.text.md`。
- 未动：core-nl（只读；三 SHA 复核仍为 fix5 定稿值）、其他版、staging 副本
  `fanout-nl/2026-w47-nl-fr/`（三 SHA 复核仍为 build-5 值）、tools/、
  `content12.py`、ABSTRACT.txt。未 commit、未 push。
  （git status：规范路径整目录 untracked；其余 `M` 项均为其他并行 agent 的
  活，mtime 均早于本次会话——staging text.md 12:47 UTC、core content34.py
  15:25 UTC，本会话始于 17:09 UTC。）
- 待 proof1（独立校对员）定稿后由协调员统一 commit/push。
