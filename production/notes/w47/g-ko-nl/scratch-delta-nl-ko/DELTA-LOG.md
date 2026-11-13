# DELTA-LOG — 2026-W47 nl-ko, core fix3 + fix4 + fix5 同步

- 版：`2026-w47-nl-ko`（荷兰语目标 × 韩语读者版），VOL.4，8 版，150 题
- 日期：2026-11-11
- 任务：core-nl fix3（D6/D7）+ fix4（D8/D9/D10）+ fix5（D11）同步到本版。
  只改本版自己的源文件，不碰核心、不碰其他版。不 commit、不 push。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-nl-ko/`
  （日志、门禁证据、registry、比对 JSON、crops 均在此）
- 工作区：repo 克隆 `~/workspace/weekly-git`；解释器 `tools/venv/bin/python`；
  TMPDIR = 本 scratch 目录
- 核心对照（只读）：`production/2026-w47/core-nl/`，fix5 定稿已核对——
  印 `b7d4a9cd…` / 25,955,578 B，网 `5a47449c…` / 2,104,000 B，
  文 `0b97a48d…` / 44,093 B，三件与 core-nl `FIX-LOG.md` fix5 定稿值逐字节一致。
  权威记录：core-nl `FIX-LOG.md`（fix3、fix4、fix5 各节），开工前已通读。

## 0. 开工探针与复制

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29b…`，
  rc=0；`/dev/null` 正常；goals-side scratch 真实写文件 `probe.txt` 通过。
- 修前身份核对（三件 SHA，实测 = KIT 登记的 build-2 值）：印
  `aaeeba2cb7f59bb0e8d50d6614b09f3831c4ade3be3cff52f03d8f71e25113bd` /
  17,281,343 B；网 `ed38e32febf217635830d3d6a7d7fa4b0c52f5db37493f78ce4bb8a0204065d5`
  / 1,919,763 B；文 `1d103d29fcbde556646bf5106d812cb358a9f0b3cc14b6b0b9f31030c31fe408`
  / 47,580 B。修前 8 个 SVG SHA 存 `pre/svg-sha-pre.txt`，text.md 存 `pre/text-pre.md`。
- **规范路径开工时不存在**（与 nl-de 试点相同）：W47 的 nl fanout 版只存在于
  staging 目录 `production/2026-w47/fanout-nl/`。处理：把 staging 的 nl-ko 版
  整目录 `cp -a` 到规范路径 `production/2026-w47/2026-w47-nl-ko/`，
  `diff -r` 校验**完全一致**（仅两条无害的 ownership 保留警告），staging 副本全程未动；
  此后全部 delta 工作都在规范路径做。修后复核 staging 三 SHA 仍为修前值（见 §7）。

## 1. 修前实测：D6/D7/D8/D10 在本版预先不存在，D9/D11 是真缺陷

韩语读者层文字与核心中文桥接文字断行不同——修前 SVG 实测：

| 点 | 修前 SVG 实测 | 结论 |
|---|---|---|
| D6 P3 桥接 | `현재완료로 채우세요. 조동사 hebben/zijn에 주` (y=2250.5) / `의하세요.` (y=2280.225)，2 行，末行 `의하세요.` 不是标点 | 无孤儿，**预先不存在、无需改** |
| D7 P7 桥接 | `de wedstrijd 경기; de groepswinst 조 우승; de` (y=725.66) / `kwartfinale 8강전; scoren 골을 넣다.` (y=755.385)，2 行，句末 `.` 在行末 | 无孤儿，**预先不存在、无需改** |
| D8 P6 图注 | 3 行：`연습 데이터: 가상의 숫자이며, 연습용일 뿐 실제` / `조사가 아닙니다. 질문: 신발에 무엇을 넣나요? (젊` / `은이 100명)`，基线 635.02/659.44/683.86 | 无行首标点，**预先不存在、无需改** |
| D10 P7 来信 | 2 行：`마감까지 편지나 작문이 없어 예시를 실어요.` (1754.27) / `약속은 VOL.5로 이어져요.` (1782.67)，句末 `.` 均附着行末 | 无行首标点，**预先不存在、无需改** |
| D9 Q140 | registry 键、text.md:415 答案、P8 节点三源同错：`Ik maak een surprise met een gedicht.`（缺 `kort`）；题干 `작은 시가 담긴 깜짝 선물을 만들어요.` 已含“小”（작은） | **真缺陷** |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=611.0>` 底 1202.6；末行 `18:45 uur.` 基线 y=1209.49，**盒底外 +6.89px** | **真缺陷** |

全版孤儿标点横扫（修前，双类，CJK + 拉丁标点，见修后横扫 §6 机器与修前 SVG 同值——
p3/p6/p7 修后字节一致故修前亦 0/0）：(a) 独行标点 0，(b) 行首标点 0。
因此 D6/D7/D8/D10 的同步是**结构性**的：机制照搬 + 本版文字重算 w，选出的 w 必须
**精确复现当前干净断行**（行内容、行数、基线全不变），重建 SVG 以 p3/p6/p7 字节一致为证。
D9、D11 是真修。

## 2. Width scan（本版自己的文字 + 本版 `svglib.wrap()`，0.1px 步进，250–430px）

CW = 422.5。取“精确复现当前各行”的 w 区间中点（核心数值一律不抄）：

| 点 | 文字（字体/字号） | 当前 w | 区间（同行内容） | 选中 w |
|---|---|---|---|---|
| D6 桥接 | `현재완료로 채우세요. 조동사 hebben/zijn에 주의하세요.`（sans 20.5） | CW=422.5 | 405.0–423.7（2 行） | **414.35**（中点） |
| D7 桥接 | `de wedstrijd 경기; de groepswinst 조 우승; de kwartfinale 8강전; scoren 골을 넣다.`（sans 20.5） | CW=422.5 | 417.3–430.0（2 行，窗口内） | **423.65**（中点） |
| D8 图注 | `연습 데이터: … (젊은이 100명)`（sans 18.5） | CW−44=378.5 | 376.6–384.8（3 行） | **capcn_w=380.7**（中点） |
| D10 来信 | `마감까지 편지나 작문이 없어 예시를 실어요. 약속은 VOL.5로 이어져요.`（sans 20） | CW−44=378.5 | 364.9–387.7（2 行） | **dt_zh_w=376.3**（中点） |

区间边界核实（逐点探查带外 0.1px 的断行变化）：
- D6：404.9 时行 1 丢 `주`（`…에` / `주의하세요.`）；423.8 时 `의` 并入行 1
  （`…주의` / `하세요.`）——405.0–423.7 为真区间。行 1 实测 advance 404.94px。
- D7：下沿 417.3 为真（行 1 advance 417.25px，417.2 时 `de` 掉行变 3 行）；
  上沿超出扫描窗口：行 1 + ` kwartfinale` advance 530.14px，即真区间为 417.3–530.1。
  窗口内区间 417.3–430.0 的中点 423.65 距下沿 6.35px、距真上沿 106.5px；
  w 只决定断行，渲染出的仍是同一两行（advance 417.25/327.33px，均在 422.5 栏宽内），
  输出以 p7 SVG 字节一致为证。
- D8：376.5 时 `(` 掉到行 2 末、`(젊은이 100명)` 另起行；384.9 时行 1 多吃 `조`
  （`…실제 조` / `사…`）——376.6–384.8 为真区间。
- D10：364.8 时行 1 丢 `.`，行 2 变成 `. 약속은 VOL.5로 이어져요.`——
  **收窄过头会造出行首句点**，这正是取中点（376.3）而非贴边的原因；
  387.8 时行 1 多吃 `약`（`…실어요. 약` / `속은…`）——364.9–387.7 为真区间。
- D11 事实句（serif 21.5，CW−44）：5 句断行 3/3/3/2/3 = 14 行，与核心一致；
  `sh` 旧 611.0 → 新 638.0（+27）。顶留 89 = 16（pad）+ 52（标题块）+ 21
  （para y-offset），本版 `content34.py` 渲染循环形状与核心相同（`yy3 = sy3+16`、
  标题后 `yy3 += 52`、事实 `p.para(…, yy3+21, …)`），盒顶 sy3=591.6 不变。

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
-e.bridge("현재완료로 채우세요. 조동사 hebben/zijn에 주의하세요.")
+e.bridge("현재완료로 채우세요. 조동사 hebben/zijn에 주의하세요.", w=414.35)  # delta D6: width-scan band 405.0-423.7px keeps the 2 lines; mid 414.35
```

### `content34.py:130` — D11 盒高公式（P4 HET PROGRAMMA；第 37 行的 P3 SINTERKLAAS 盒不动）
```diff
-sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
+sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30  # delta D11: top reserve 62 -> 89 = 16 (pad) + 52 (title block) + 21 (para y-offset); last line was 6.89px below the box
```

### `content7.py:19` — D7 调用点
```diff
-a.bridge("de wedstrijd 경기; de groepswinst 조 우승; de kwartfinale 8강전; scoren 골을 넣다.")
+a.bridge("de wedstrijd 경기; de groepswinst 조 우승; de kwartfinale 8강전; scoren 골을 넣다.", w=423.65)  # delta D7: width-scan window band 417.3-430.0px keeps the 2 lines; mid 423.65 (true upper edge 530.1)
```

### `content7.py:91–92, 100` — D10 两处同用 `dt_zh_w`
```diff
 dt_zh = "마감까지 편지나 작문이 없어 예시를 실어요. 약속은 VOL.5로 이어져요."
+dt_zh_w = 376.3  # delta D10: width-scan band 364.9-387.7px keeps the 2 lines; mid 376.3
-lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, CW - 44)) * 29 + ...
+lh = 62 + ... + len(wrap(dt_zh, "sans", False, 20, dt_zh_w)) * 29 + ...
-yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10
+yy3 = p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, dt_zh_w, 1.42) + 10  # delta D10: dt_zh_w, see above
```

### `content56.py:143–144, 156` — D8 两处同用 `capcn_w`
```diff
 capcn = "연습 데이터: 가상의 숫자이며, 연습용일 뿐 실제 조사가 아닙니다. 질문: 신발에 무엇을 넣나요? (젊은이 100명)"
+capcn_w = 380.7  # delta D8: width-scan band 376.6-384.8px keeps the 3 lines; mid 380.7
-ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
+ch = 62 + ... + len(wrap(capcn, "sans", False, 18.5, capcn_w)) * 26 + 18
-yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
+yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, capcn_w, 1.32) + 6  # delta D8: capcn_w, see above
```

### `content8.py:75` — D9 键补 kort（目标语荷兰语句，直接照搬核心）
```diff
-f.ex("B2", "번역", "Ik maak een surprise met een gedicht.", "surprise는 고정 표현이에요",
+f.ex("B2", "번역", "Ik maak een surprise met een kort gedicht.", "surprise는 고정 표현이에요",
```
注记不动。`kort` 在本版内有据：题干 `작은 시가 담긴…`（“小”）+ text.md:73 前文
`Twee: schrijf een gedicht — kort is ook goed.`（与核心的论证相同）。题干不动。

### `WEEKLY-KIT.md`
- “Files delivered”三 SHA 更新为 build-3 新值；文末新增 “Delta
  (core fix3 + fix4 + fix5, 2026-11-11, build 3)” 一节，旧 SHA 全数保留为历史。

## 4. 重建

- `run.py` rc=0、TOTAL 150、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31、
  model words 81；0 FLOW OVERFLOW / HEAD TOO WIDE。`P4 col3 ends 1229.6`（旧 1202.6）；
  `P6 chart ends 691`、`P7 col3 ends 1927.0` 与修前一致（修前 build-2 日志同值）。
- `render.py` rc=0。SVG 哈希 vs 修前：**仅 `p4-sport.svg`（D11）与
  `p8-toets.svg`（D9）变化**，其余 6 个字节一致——D6/D7/D8/D10 结构同步零位移。
- text.md 重导（`export_fanout.py`，rc=0）：47,580 → 47,585 B，diff 恰好
  text.md:415 一行（`kort `，+5 B）；142 单题 + 2 配对头 + 8 配对项 = 150；
  8 金句、6 gloss。注：导出记录 471 events，修前 ko-export1 为 470——
  多 1 个记录事件（w 形参调用所致），输出 text.md 除 415 行外逐字节一致，无影响。
- registry 重导（`dump_reg_delta.py`）：150 条，by page / by level 与 build 一致。
- `webpdf.py` rc=0：1,919,772 B（< 7 MB），text layer 47,618 B。
  交付的网 PDF 即本次重建产物，未为比对重渲染（字节不可复现，只比文字层）。

## 5. 六处修复点逐项实测（重建 SVG 证据）

| 点 | 实测值（重建后） | 证据 |
|---|---|---|
| D6 | P3 桥接仍 2 行，内容与修前逐字相同：`현재완료로 채우세요. 조동사 hebben/zijn에 주` (2250.5) / `의하세요.` (2280.225)；下游 y 无位移（p3 SVG 字节一致） | `svg/p3-cultuur.svg`、crop `crop-p3-d6.png`（目检） |
| D7 | P7 桥接仍 2 行逐字相同：`de wedstrijd 경기; de groepswinst 조 우승; de` (725.66) / `kwartfinale 8강전; scoren 골을 넣다.` (755.385)；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d7.png`（目检） |
| D8 | P6 图注仍 3 行，基线 635.02/659.44/683.86 全不变；盒高 `ch` 不变（`P6 chart ends 691` 与修前同）；零 y 位移（p6 SVG 字节一致） | `svg/p6-verdieping.svg`、crop `crop-p6-d8.png`（目检） |
| D9 | 三源一致：registry 键 = text.md:415 答案 = P8 节点（y=2143.98），均为 `Ik maak een surprise met een kort gedicht.`；其余 149 键未动（3-way 比对见 §6） | `svg/p8-toets.svg`、crop `crop-p8-q140.png`（目检） |
| D10 | P7 来信仍 2 行逐字相同：`마감까지 편지나 작문이 없어 예시를 실어요.` (1754.27) / `약속은 VOL.5로 이어져요.` (1782.67)；盒高 `lh` 不变（`P7 col3 ends 1927.0` 与修前同）；p7 SVG 字节一致 | `svg/p7-taal.svg`、crop `crop-p7-d10.png`（目检） |
| D11 | 盒 `<rect y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**盒内余量 +20.11px（≥20px）**；`P4 col3 ends 1229.6`；P4 其余内容不动、其余 7 页 SVG 字节一致（D9 的 p8 除外） | `svg/p4-sport.svg`、crop `crop-p4-programma.png`（目检：末行在盒内，下有明显留白） |

D11 双法验证（PIL + 交付 PDF 渲染像素，`inkprobe-d11-delta.log`）：
- SVG：盒底 1229.6，末行基线 1209.49，余量 **+20.11px**。
- cards 1×：末行真墨最低行 y=1209.00（基线下 0.49px），真墨余量 **+20.60px**；
  盒底下 7px 条带 0 非纸像素。
- 交付印 PDF 150dpi 渲染：末行真墨最低行 y=1209.12，真墨余量 **+20.48px**；
  盒底下 7px 条带 0 非纸像素。crop `crop-p4-programma-pdf.png` 目检确认。

## 6. 全部门禁结果

- **Build**：`run.py` rc=0、TOTAL 150、0 溢出（见 §4）。`render.py` rc=0。
- **Occlusion 真实审计**：`tools/occlusion_audit.py svg/` rc=0，**0 flags**。
- **p8 extract**：`p8.py extract --total 150` noted set **150/150**。
- **p8 compare（核心 vs 本版）**：`p8.py compare --json p8-compare.json`，
  `status: CLEAN, total: 150, missing: [], extra: [], uncertain: [],
  keydiff: [137, 138]`。137/138 是翻译题——键本身就是读者语，核心为中文
  （`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），本版为韩文
  （`신터클라스 뉴스는 매일 18:00에 방송해요.` / `상위 두 팀이 8강전에 진출해요.`），
  按设计不同，非缺陷。修前 keydiff 为 [137, 138, 140]——D9 把 140 移出了该表。
  （gates 套件 stdout 计数的 `keydiffs=0` 是另一口径：它数的是 stdout 里
  `key diff` 字样行数，JSON 列表本身即 [137, 138]，与 nl-de 相同口径差异。）
- **Keycheck（三源逐题 verbatim 比对 `p8-compare-3way.json`）**：
  **149/149 MATCH**，DIFF=[]，MISSING=[]；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。Q140 三源 verbatim 一致（含 `kort`）。
  注：初版比对脚本是德语版（找 `— Antwort:`），ko text.md 用 `— 정답：`，
  致 md_answer 全空、0/149——属脚本语言标记 bug，已按韩语标记修正后重跑得 149/149。
- **Freeze 核心 baseline**：`freeze.py baseline --build <core-nl> --core-svg
  <core-nl>/svg --out scratch/freeze-core` rc=0，**8/8 字节一致**；
  核心 shipped SVG 跑前后哈希不变（未碰核心）。
- **版内自比对（补充）**：clean-dir 重跑 `run.py` 再 sha256 比对，
  **8/8**（fanout gates.py `freeze_sha256` 项）。
- **印/网文字层逐页一致**：PyMuPDF 位置排序，8 页 posdiff 0、msdiff 0
  （tokens 733/713/668/667/695/657/754/1640；P8 1640 vs build-2 的 1639，
  +1 = `kort`）；pdftotext 印 47,618 B = 网 47,618 B。
- **P8 最小 PDF 字号**：答案区 min **10.12pt**（median 10.12，613 spans）≥ 9.75pt。
- **全版孤儿标点两类横扫（重建 SVG，PIL + svglib 双 advance，1427 行）**：
  (a) 独行标点 **0**，(b) 行首标点 **0**，两方法 8 页全 0；
  brute-force 交叉检查：以标点开头的 `<text>` 元素 57 个，leftmost-on-baseline **0**。
  （CJK + 拉丁标点均纳入。）
- **Creambox**：TOTAL 3 flags，与修前**完全相同**的三处（P2/P5/P6），均为已知
  假阳性：各盒 7px 条带逐像素探查 **0 非纸像素 / 0 真墨**（新旧两版 card 均同值）：
  P2 EN JIJ `'...편집부에 보내세요.'` (bottom 1417.8 vs rect 1416.8)，
  P5 EN JIJ `'...써서 보내세요.'` (bottom 966.4 vs rect 965.5)，
  P6 `'은이 100명)'` (bottom 689.4 vs rect 691.0，在盒内)。
  P4（D11 盒）0 flags。**真溢出 0。**
  （注：复用的 nl-en `boxtitle_inkscan_delta.py` 内 CREAMSTRIP 一节写死了
  nl-en 的盒坐标（P5 bottom 1023.5），在 ko 图上探到下一版块内容、报出
  `REAL OVERFLOW` 2961 像素——是脚本坐标错位，不是缺陷：staging 旧卡同坐标
  同值 2961，且 p5 SVG 修前修后字节一致；ko 自身三处 flag 的条带重探见上，均为 0。）
- **Spill 横扫**：**0 spills**；P4 HET PROGRAMMA 盒（底 1229.6）无任何 below
  命中；其余 BELOW 命中（+24/+32/+44/+50.5/+60px）均为独立版块（下一节标题、
  提示语、gloss、页脚注），ABOVE/SIDE 均为图注/邻盒标题——与核心 fix5 同类裁决。
- **Fanout 门禁套件**（`gates_delta.py`，即 build-2 同款 9 项）：
  **ALL PASS**（occlusion / p8_extract / p8_compare / freeze_sha256 /
  print_web_text / pdftotext_nonempty / p8_fontsize / p8_chips /
  s11_svg——§1.1 off-palette {}、VOL.5 = 5 = core、paper fills 8）。
- **盒标题横向真墨扫描**（PIL 真墨，`boxtitle-inkscan-delta.log`）：共扫描 58 个标题
  （37 HEAD + 21 BOX），**1 处 OVER**：P8 `A　VUL DE KRONIEK IN`，ink_right=537，
  limit=510.5，margin **−26.5px**。**此为修前已存在、非 delta 引入**：
  该 head 的 `<text>` 元素在 staging 与规范版 p8 SVG 里逐字节相同
  （x=88.0, y=201, 21pt bold），且 nl-en 同版同项数字完全一致（−26.5）；
  delta 未动任何标题（p3/p6/p7 字节一致；p4 标题余量 +173px ok；p8 只改了 Q140 键行）。
  其余 57 个标题全部 ok，最紧的余量 +0.5px（多处 HEAD 贴边，advance 估算下本就贴边）。
  任务所称“56 标题 0 越边”与实测 58 标题 / 1 处修前 OVER 不符——以盘上实测为准，
  该 1 处留待 proof1 / 协调员判定是否立项修（不在 D6–D11 范围内，未动）。
- D3 回归：P2 SVG 字节一致，D3 断行与余量与 build-2 相同，无需重测。

## 7. 新三 SHA（交付）

| 文件 | 字节 | SHA-256（修后，实测） | 旧值（build-2，历史） |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-ko.pdf`（印） | 17,281,343 | `c4f446b9adc06c29be6a047abf30c83a445062bc26335a578a9609afb42d537d` | `aaeeba2c…5113bd` / 17,281,343 |
| `De-Lucerna-VOL4-nl-ko-web.pdf`（网） | 1,919,772 | `75f6730e10925f575c4a348e0428cdf6c85be2bb658ed4e9037a85d55ae1176e` | `ed38e32f…4065d5` / 1,919,763 |
| `2026-w47-nl-ko.text.md`（文） | 47,585 | `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9` | `1d103d29…31fe408` / 47,580 |

注：印 PDF 字节数与修前相同（17,281,343），SHA 不同（p4 盒高 + p8 `kort` 改动；
PDF 字节数相同是压缩后巧合）。网 PDF SHA 与字节大小均不可复现，只比文字层；
交付的网 PDF 由本次重建产生（文字层与印 PDF 逐页一致，见 §6）。

## 8. 改动文件清单与未动确认

- 改动（规范路径 `production/2026-w47/2026-w47-nl-ko/` 内）：`bslib4.py`、
  `content34.py`、`content56.py`、`content7.py`、`content8.py`（§3 对照）、
  `WEEKLY-KIT.md`（新 SHA + delta 节）。
- 重建产物（同目录）：`svg/p4-sport.svg`、`svg/p8-toets.svg`（仅此 2 个 SVG
  变化）、`cards/*.png`、`De-Lucerna-VOL4-nl-ko.pdf`、
  `De-Lucerna-VOL4-nl-ko-web.pdf`、`2026-w47-nl-ko.text.md`。
- 未动：core-nl（只读；三 SHA 复核仍为 fix5 定稿值，freeze-core 证实 shipped
  SVG 未变；`git status` 里 core-nl 的 M 项是核心 fix 轮次未提交的工作，非本 delta）、
  其他版、staging 副本 `fanout-nl/2026-w47-nl-ko/`（三 SHA 复核仍为 build-2 值）、tools/、
  `content12.py`、ABSTRACT.txt。未 commit、未 push。
- 待 proof1（独立校对员）定稿后由协调员统一 commit/push。
- 本 scratch 证据：`pre/`（修前 SHA + text.md）、`width-scan.log`、`rebuild/`
  （run/render/export/dump_reg/webpdf 日志 + 修后 SVG SHA）、`gates/`
  （gates-delta、p8-compare、p8-extract、p8compare-delta、freeze-core、
  orphan-sweep、spill-sweep、creambox、boxtitle-inkscan、inkprobe-d11、
  creamstrip-ko 日志与 JSON）、`render/`（交付印 PDF 150dpi 全页渲染）、
  `width_scan.py` + 各门禁脚本（自 nl-de/nl-en 同族 scratch 复用，路径已改 ko；
  其中 `p8compare_delta.py` 按韩语 `— 정답：` 标记修正）、crops
  （`crop-p3-d6`、`crop-p7-d7`、`crop-p6-d8`、`crop-p7-d10`、`crop-p8-q140`、
  `crop-p4-programma` + `crop-p4-programma-pdf`）。
