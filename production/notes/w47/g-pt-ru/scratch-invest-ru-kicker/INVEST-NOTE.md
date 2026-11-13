# W47 ru D2 调查：P1 kicker 词距过紧（`ГАЗЕТАДЛЯ` / `ИЗУЧАЮЩИХРУССКИЙ` / `НАСТОЯЩАЯРОССИЯ`）

- 缺陷：ru-zh-tw proof1 (b) D2，Minor，核心级。P1 刊头标语行 y=372，16px，复校员 PIL 实测词间墨迹间隙 1.4 / 1.9 / 2.6px。
- 结论先行：**俄语本地修复存在，且已在 scratch 副本验证通过**——只改 `core-ru/content12.py:18` 一行（kicker 字符串内 9 处单空格改为双空格），不碰任何引擎/共享代码，不影响其余 11 个核心；重建后 P1 全部词间墨迹间隙 ≥4px（KIT §7.2.9 区间），其余版式不变（P2 字节一致，P1 除标语行 20 个 `<text>` 元素外全部一致）。是否落到生产（core + 10 个 ru fan-out 各重建一次）由协调员定夺；本次未改 repo、未 commit、未 push。
- 调查日期：2026-11-11。工作目录（全部写操作只在这里）：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-invest-ru-kicker/`

## 0. 探针（开工前）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → 通过（`9daeafb9…`）。
- goals 侧 `hidden_files/w47/` 真实写文件 → 通过。
- `TMPDIR=~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-tmp`（未用 /tmp）。
- 红线遵守：`~/workspace/weekly-git` 下零写入（该仓内 `git diff` 的 106 个改动文件与 `production/2026-w47/` 的 untracked 目录均为开工前已有的他人工作，与本次无关）；无 commit、无 push；只动 `production/2026-w47/` 与 `hidden_files/w47/`。

## 1. 机制判定：词距由什么控制

### 1.1 调用链（确切文件 + 行号）

| 层 | 文件 | 行 | 内容 |
|---|---|---|---|
| 数据（kicker 字符串本身） | `production/2026-w47/core-ru/content12.py` | **18** | `p.text(975, 372, "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ", 16, "sans", False, GREY, anchor="middle")` |
| 版式库（每版一份拷贝） | `production/2026-w47/core-ru/bslib4.py` | 5 | `from svglib import *`；`BSPage4`（`PW, PH = 1950, 2700`，即 1 SVG 单位 = 1 渲染 px） |
| 布局引擎（逐字字体分配 + x 定位） | `production/2026-w47/core-ru/svglib.py` | 99–119（`_char_font`）、206–262（`Page.text`） | 见 1.2、1.3 |

渲染：`core-ru/render.py` 用 cairosvg 按 1950×2700 出 PNG 卡片，再转 PDF（与本次验证用的渲染参数一致）。

### 1.2 空格为什么是 Noto Sans CJK SC（根因核查）

`svglib.py:113–119`（`_char_font`，`kind="sans"` 分支）：

```python
if italic and cp in _CYR and cp in _CMAP["sans_noto_i"]:
    return "sans_noto_i"
if cp in _CYR and cp in _CMAP["sans_noto_b" if bold else "sans_noto"]:
    return "sans_noto"
if cp in _CMAP["sans_b" if bold else "sans"]:
    return "sans"
return "deja"
```

其中 `_CYR = range(0x0400, 0x0530)`（`svglib.py:78`，西里尔字母区）。空格 U+0020 不在 `_CYR` 内，于是跳过 `sans_noto`（= Noto Sans，`svglib.py:33,82`）分支，落入 `sans`（= Noto Sans CJK SC，`svglib.py:23,82`）。这是**有意设计**，文件头注释 `svglib.py:54–57` 原话：sans 是 “Noto Sans（Cyrillic only）→ Noto Sans CJK SC（everything else incl. Latin，fr pilot precedent）”——即 Noto Sans 只查西里尔码点，其余一切（拉丁、数字、标点、空格、符号）都走 CJK SC。实测 SVG 印证：标语行 19 个 `<text>` 元素中，7 个西里尔词用 `Noto Sans`，9 个空格与 `— `、`, `、`-` 均用 `Noto Sans CJK SC`。

### 1.3 根因是否“空格 advance 偏窄”（实测）

用 `tools/venv/bin/python` + PIL 实测（与布局引擎同一批字体文件）：

| 字体（16px） | 空格 advance | 占 em |
|---|---|---|
| Noto Sans CJK SC（SC index 2，`NotoSansCJK-Regular.ttc`） | **3.58px** | 0.224em |
| Noto Sans（`NotoSans-Regular.ttf`） | 4.16px | 0.260em |

- 与 KIT 的记载一致：`core-ru/WEEKLY-KIT.md:94` 第 9 条已裁决 “Noto Sans CJK SC 空格字形窄，约 0.2em，17–19pt 下 4–5px 间隙属正常词距，不修”——本次 D2 的 1.4–2.6px 落在该裁决区间之外。
- 但**只窄 0.58px，不是全部根因**。紧的另一半是相邻字形的负边距（PIL `getbbox` 实测，16px Noto Sans）：词尾 `А`（ГАЗЕТА）墨迹超出 advance **+1.2px**，`Х`（ИЗУЧАЮЩИХ）**+0.8px**，`Я`（НАСТОЯЩАЯ）**+0.4px**；词首字母左承 ≈0。于是墨迹间隙 = 3.58 − 超出量：
  - ГАЗЕТА / ДЛЯ：2.40px（复校员 1.4）
  - ИЗУЧАЮЩИХ / РУССКИЙ：2.80px（复校员 1.9）
  - НАСТОЯЩАЯ / РОССИЯ：3.10px（复校员 2.6）
  - 其余 6 处空格分隔词对：3.10–4.10px（见 §3 表 1），即**除 `,/ПО`（4.10）外全部 <4px**。
- 复校员数字比 PIL 框算法小 0.5–1.0px：同一对词、同一顺序、同一相对大小——应为渲染（CairoSVG 抗锯齿/微调）与阈值口径差异，不是方法错误。本次验证以 PIL 墨迹框算法为主口径（与布局引擎同一测量体系），另用渲染列扫交叉核对（§3）。

### 1.4 是“每语种数据”还是“共享库代码”——判定

**两者都不是单点共享文件；引擎是“每版一份拷贝”，数据是“每版一行”。**

- `svglib.py` 在 12 个核心各有一份，内容**已按语种分化**：ru 版含西里尔路由（`_char_font` 的 `_CYR` / `sans_noto` 分支，en/it 版没有）；md5：ru `c70b49c0…`，en 与 it 同为 `05e25a02…`，de/es/fr/pt/nl/ja/ko/zh-cn/zh-tw 各不相同。SOP.md 全文无 “svglib” 字样，无统一模板/重印脚本的记载。**没有一个改一处就动 12 核心的共享文件。**
- ru 内部 11 个版（core-ru + 10 个 ru-* fan-out）的 `svglib.py` **字节相同**（md5 均为 `c70b49c04e6b1210d93d07d339698a6c`），`content12.py:18` 的 kicker 行也 11 版相同；但每版是独立目录、独立构建（fan-out P1 SVG 的 md5 各不相同，各版自带 `run.py`/`render.py`）。改 `core-ru/svglib.py` 只影响 core-ru 一版的构建，不会传导到其他核心，也不会自动传导到 ru fan-out。
- 关键限制：**改 `svglib.py` 的字体路由仍不达标，且波及整版**。把空格改路由到 Noto Sans 每处只 +0.58px → 三处紧对变为 2.98 / 3.38 / 3.68px，仍 <4px（§1.3），且会改变 core-ru 全书所有 sans 空格（全部正文/标题换行重排），违反“其余版式不变”。因此引擎改法不在考虑之列——不是因为它会动 12 核心（实际不会），而是因为它**修不动 + 动整版**。
- 反之，kicker 字符串是 `content12.py:18` 的**纯数据**，只被 P1 标语行这一处 `p.text` 调用（`grep`：`НАСТОЯЩАЯ РОССИЯ` 在 core-ru 内除 SVG/PDF 外只出现在 `content12.py`；不在 `.text.md`、不在 `ABSTRACT.txt`、不在封面/检查脚本中；`check_core.py` 不检查该行）。改它只动该行。

## 2. ru-local 修复：补丁（已在 scratch 验证，未落生产）

### 2.1 补丁

- 文件：`production/2026-w47/core-ru/content12.py`，**仅第 18 行**。
- 改法：kicker 字符串内 9 处 ASCII 空格全部改为双空格（其余字符、标点、连字符不动；不改字体、字号、字距、锚点）。

```diff
-p.text(975, 372, "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ", 16, "sans", False, GREY, anchor="middle")
+p.text(975, 372, "ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУССКИЙ  ЯЗЫК  —  НАСТОЯЩАЯ  РОССИЯ,  ПО-РУССКИ", 16, "sans", False, GREY, anchor="middle")
```

- 为什么是“9 处全改”而不是“只改 3 处紧对”：任务要求**逐词间隙全部 ≥4px**；基线除 `,/ПО` 外 8 处均 <4px，只改 3 处会留下 5 处 <4px，且造成同一行内 3.5px 与 6.0px 混杂的不均匀词距。全改后全行均匀（§3）。
- 为什么双空格可行：`Page.text`（`svglib.py:206–262`）按 PIL 实测 advance 逐 run 定 x，空格 run 自身就是独立 `<text>`（D1 修正，`svglib.py:233–247`，双空格 run 照样走该分支，advance = 2×3.58 = 7.16px）；`anchor="middle"` 下总宽由 `text_w` 重算、居中自动保持；该行无 wrap、无后续元素依赖其宽度。行总宽 +32.2px（9×3.58），居中后左右各外扩 16.1px：新行起 586.3、止 ≈1363.7，页边距 88–1862 内，无碰撞（上方 y=330 行、下方 y=420 线均不受影响）。

### 2.2 未采用的备选（均已排除，留档）

| 备选 | 为什么不用 |
|---|---|
| `svglib.py` 空格改路由到 Noto Sans | 每处仅 +0.58px，三处紧对仍 <4px；且改动 core-ru 全书 sans 空格、触发全书重排 |
| `p.text(..., spacing=...)` 加字距 | 字距按字符数加在每个 run 边界，紧对增量取决于前词长度（ДЛЯ +1.2px、ИЗУЧАЮЩИХ +3.3px @0.3），不均匀；且改动全行字母间距，属版式变更 |
| U+2002/U+2009 等特殊空白 | 换字符集、增加校对/lint 不确定性；双 ASCII 空格已够用，无需引入 |

## 3. 验证（scratch 副本，`core-ru/`）

流水线复现性：未打补丁的 scratch 副本跑 `content12.py`，P1、P2 SVG 与 repo 原版**字节一致**（`cmp` 通过），证明复现流水线无漂移；随后打补丁再跑。

### 表 1 — 方法一（主口径）：PIL 墨迹框间隙 = （后词 x + 后词墨迹左承）−（前词 x + 前词墨迹右缘），SVG 单位 px

| 词对 | 基线 | 打补丁后 | 增量 | ≥4px |
|---|---|---|---|---|
| ЕЖЕНЕДЕЛЬНАЯ / ГАЗЕТА | 3.60 | **7.20** | +3.60 | ✓ |
| ГАЗЕТА / ДЛЯ（D2 最紧） | 2.40 | **5.90** | +3.50 | ✓ |
| ДЛЯ / ИЗУЧАЮЩИХ | 3.10 | **6.80** | +3.70 | ✓ |
| ИЗУЧАЮЩИХ / РУССКИЙ（D2） | 2.80 | **6.30** | +3.50 | ✓ |
| РУССКИЙ / ЯЗЫК | 3.50 | **7.10** | +3.60 | ✓ |
| ЯЗЫК / — | 3.80 | **7.40** | +3.60 | ✓ |
| — / НАСТОЯЩАЯ | 3.90 | **7.40** | +3.50 | ✓ |
| НАСТОЯЩАЯ / РОССИЯ（D2） | 3.10 | **6.80** | +3.70 | ✓ |
| , / ПО | 4.10 | **7.60** | +3.50 | ✓ |

最小值 5.90px（ГАЗЕТА/ДЛЯ），比 4px 门限高 1.90px；即使按复校员口径比 PIL 小 ~1.0px 折算，最紧处仍 ≈4.9px ≥4px。`РОССИЯ/,`、`ПО/-`、`-/РУССКИ` 是逗号/连字符直连（无空格设计），不计入词距。

### 表 2 — 方法二（交叉核对）：渲染列扫 closest-approach（逐行最小墨迹距，cairosvg 1950×2700 PNG，y 357–374 带）

| 词对 | 基线 thr<128 / <150 / <200 | 打补丁后 thr<128 / <150 / <200 |
|---|---|---|
| ЕЖЕНЕДЕЛЬНАЯ / ГАЗЕТА | 6 / 6 / 4 | **9 / 9 / 9** |
| ГАЗЕТА / ДЛЯ | 3 / 0 / 0（重叠） | **5 / 4 / 3** |
| ДЛЯ / ИЗУЧАЮЩИХ | 6 / 6 / 5 | **10 / 10 / 9** |
| ИЗУЧАЮЩИХ / РУССКИЙ | 3 / 3 / 3 | **7 / 7 / 6** |
| РУССКИЙ / ЯЗЫК | 5 / 5 / 3 | **9 / 8 / 7** |
| ЯЗЫК / — | 8 / 8 / 6 | **11 / 11 / 11** |
| — / НАСТОЯЩАЯ | 6 / 6 / 6 | **10 / 10 / 9** |
| НАСТОЯЩАЯ / РОССИЯ | 6 / 6 / 5 | **10 / 10 / 9** |
| , / ПО | 7 / 6 / 6 | **10 / 10 / 10** |

说明：thr<200 会把浅色抗锯齿晕边计为墨（基线最紧处在该口径下本就重叠），是最严苛口径；打补丁后仅 ГАЗЕТА/ДЛЯ 在该口径为 3px，其余 8 处 ≥6px；实墨口径（thr<128/150）下 9 处全部 ≥4px（最小 4–5px）。与方法一结论一致：**通过**。

### 其余版式不变（diff 证据）

- P2：`p2-zhizn.svg` 打补丁前后**字节一致**。
- P1：971 个 `<text>` 元素中仅 y=372 标语行的 **20 个**不同（19 个 run 全部是该行，另 1 个为同一行空格 run 的文本翻倍）；非 `<text>` 部分**完全一致**；其余 951 个元素逐字节相同。
- 标语行新 x：首词 602.4→586.3、末词 1286.0→1302.1，`anchor="middle"` 居中于 975 不变；行宽 +32.2px，无任何溢出/碰撞。

## 4. 落生产时的波及范围（本次未做，由协调员定夺）

- 同样的一行补丁需在 **11 个文件**各做一次：`production/2026-w47/core-ru/content12.py:18` + 10 个 `production/2026-w47/2026-w47-ru-{de,en,es,fr,it,ja,ko,nl,pt,zh-tw}/content12.py:18`（11 版该行字节相同，`svglib.py` 11 版也字节相同）。
- 每版随后各跑一次 `content12.py`（只重建 P1+P2 SVG）+ P1 重渲染 + web PDF 重建；其余 11 个核心（de/en/es/fr/it/pt/nl/ja/ko/zh-cn/zh-tw）**零影响**——无共享文件可被波及。
- 注意：ru-zh-tw 是本次 D2 的出处版（proof1 (b)）；core-ru 修好不等于 fan-out 修好，fan-out 须各自重建才生效。
- 若协调员决定不修：记为已知轻微外观项即可——三处紧对在 KIT §7.2.9 已裁决的 4–5px 之外（1.4–2.6px），但无重叠、无 0px，属外观级。

## 5. 交付物（本目录）

- `INVEST-NOTE.md`（本文件）
- `core-ru/`：scratch 副本（已打补丁的 `content12.py:18`；`svg/p1-pervaya.svg` 为打补丁后重建，`svg/p2-zhizn.svg` 与原版字节一致）
- `p1-baseline.svg`：未打补丁重建的 P1（与 repo 原版字节一致）
- `p1-patched.svg`：打补丁后重建的 P1（与 `core-ru/svg/p1-pervaya.svg` 相同）
- `p2-baseline.svg`：未打补丁重建的 P2（与 repo 原版字节一致）
- `p1-patched.png`：打补丁后 P1 的 cairosvg 渲染（1950×2700，与 `render.py` 同参数），表 2 的测量源
