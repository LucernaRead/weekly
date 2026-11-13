# FIX-LOG — Lucerna Weekly 2026-W47 · nl-es fix1

修复员：nl-es fix1（子代理）。只改 `production/2026-w47/2026-w47-nl-es/`，未碰核心与其它版；不 commit、不 push。
工作区：`hidden_files/w47/scratch-fix-nl-es1/`（独占新目录；全部脚本、日志、渲染件在此）。
核心对照：`production/2026-w47/core-nl/`（fix5 已定稿），仅作只读对照。

## 0. 开工核对（2026-11-11 ~18:20 UTC）

- 探针：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`（仓内成功）；scratch 内真实写文件成功（probe.txt），方动手。
- 三 SHA 与任务所给先验值逐字节一致，方动手：
  - 印 PDF `De-Lucerna-VOL4-nl-es.pdf`：`45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` / 12,669,539 B
  - 网 PDF `De-Lucerna-VOL4-nl-es-web.pdf`：`47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` / 1,616,177 B
  - 文 `2026-w47-nl-es.text.md`：`44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` / 47,649 B
- 注意：任务所指 `hidden_files/w47/briefs/brief-coordinator.md` 在仓内不存在（`find` 无此文件，`hidden_files/w47/` 下无 briefs/ 目录）；改按任务正文本身 + 仓内 SOP.md（§1.1、§8.4）+ ru-pt fix1 已验做法执行。
- 读 SOP.md §1.1（P8 最小字号底线 9.75pt）与 repo AGENTS.md（工具一律用 `tools/venv/bin/python`）。

## 1. 缺陷与根因（proof1 eaeb630c 结论 (b)，修前复测确认）

根因：西班牙语（拉丁）字符串以 Noto Sans CJK SC 排版，Cairo 实际排宽比 PIL/svglib 单字体实测宽 1.4–4.1px。Occlusion 审计（PIL 计度）与 1:1 卡片扫描对此类越框均盲区；裁定以交付 PDF 渲染像素为准。
修前量测方法：自写 `edge_raster.py`（PyMuPDF 600 dpi 渲染，墨 = max(R,G,B)<180；SVG px = 光栅 px/6.25；流式逐页渲完即释放——首版缓存 8 页写法 OOM 被杀后改流式）。修前值与 proof1 偏差 ≤0.44px，复现成立。

| 缺陷 | 位置 | 源码行 | 修前交付印 PDF 光栅墨右（SVG px） | proof1 值 |
|---|---|---|---|---|
| D1 | P6 统计图盒标题越框 | content56.py:150 | **1866.24**（限 1862，+4.24） | 1866.08 |
| D2 | P1 桥接行 | content12.py:147 | **1866.24**（+4.24） | 1865.8 |
| D2 | P2 栏目标题行 | content12.py:214 | **1865.76**（+3.76） | 1865.4 |
| D3 | 家具行 P2–P6（同一串，五页） | content12.py:235、content34.py:50/:147、content56.py:65/:180 | **1864.00**（+2.00） | 1863.8 |
| D3 | P8 答案头行 | content8.py:133 | **1864.00**（+2.00） | 1863.8 |

SVG 核查（布局方式逐行确认）：
- D2/D3 全部 8 行均为 `anchor="end"` 右锚定行：svglib 按 PIL 预算 x 写 SVG（如 P1 行 `x="1141.9"`、家具行 `x="1175.3"`、P8 行 `x="1120.8"`），右缘由锚点决定——删词缩短不移动右缘（ru-pt fix1 对照实验已证实），故一律移锚点，不动字符串。
- D1 为左起盒标题（SVG `x="1461.5" text-anchor="start"`，盒右缘 1862），缩短串或降字号均可；取降字号，保全文字。

## 2. 修复（生产源码 5 文件，共 10 处；文字内容零改动）

- `bslib4.py:20-21` 新增：`NOTE_RIGHT = RIGHT - 10`（附 ru-pt 同法注释；RIGHT = 1885）。
- D2（2 处）：`content12.py:147`、`:214` 的 `p.text(RIGHT, …)` → `p.text(NOTE_RIGHT, …)`，字符串不变。
- D3 家具行（5 处）：`content12.py:235`、`content34.py:50`、`:147`、`content56.py:65`、`:180` 的 `p.text(RIGHT, …)` → `NOTE_RIGHT`，字符串不变（一处改一行，五页同修）。
- D3 P8（1 处）：`content8.py:133` 的 `p.text(RIGHT, 1302, …)` → `NOTE_RIGHT`，字符串不变。
- D1（1 处）：`content56.py:150` 图标题字号 24 → 23，字符串 `"DE GRAFIEK　DATOS DE PRÁCTICA"` 不变（24→23 预计 Cairo 墨右 ~1849，余量 ~13px）。
- 范围外未动：`content12.py:16`（刊头日期）、`:27/:28`（P1 鹅黄头条，锚 RIGHT−30）等其余 RIGHT 锚定行，proof1 未标记，一律不动。

## 3. 重建（全在 scratch 副本内，生产 SVG/PDF 绝未重写）

- `rebuild.sh`：复制已修生产源码到 `scratch-fix-nl-es1/rebuild/`，验 OUT 确在 scratch 内（`content*.py` 的 OUT 为 `__file__` 相对路径 → 副本 `svg/`），再跑 `run.py` + `render.py`（事故教训：首版 `cp -a` 因保不住所有权失败、set -e 中止且管道盖住返回值；改 `cp -r`、日志落文件后重跑成功）。
- `run.py`：rc=0，TOTAL **150** 题；by page 10/18/18/18/18/18/12/38；by level A2 46 / B1 73 / B2 31。
- 印 PDF（scratch）：`De-Lucerna-VOL4-nl-es.pdf` 12,669,546 B，SHA `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5`。
- 网 PDF（scratch，`tools/webpdf.py` 重建）：`De-Lucerna-VOL4-nl-es-web.pdf` 1,616,171 B，SHA `48b35efc1b858a143bed01075ca22038123770f31e064e2818caf2db99ba812f`，46,815 text bytes。
- SVG 元素级比对（`svg_diff.py`，逐元素 difflib）：8 页元素数与生产一致；**仅 9 处不同**，恰为本次 9 处修复（P1 行 x 1141.9→1131.9；P2 两行 1200.1→1190.1、1175.3→1165.3；P3/P4/P5 家具行 1175.3→1165.3；P6 标题 24→23 + 家具行 −10；P7 0 处不同；P8 行 1120.8→1110.8）。其余文字、版式、题量零变化——Delta D6–D11 及旧版已修项的非回退证据。
- 视觉裁切：`crop-D1-before/after.png`（P6 图标题）：修前末字母 A 贴/越奶油盒右缘，修后缩进留白；`crop-D2P1-before/after.png`（P1 桥接行）：文字无损、字号不变、整体左移 10px。

## 4. 修后量测（同一 edge_raster.py，交付印 PDF 光栅，限 1862）

| 缺陷 | 修前 | 修后 | 变化 | 余量 |
|---|---|---|---|---|
| D1 P6 图标题 | 1866.24 | **1849.44** | −16.80 | +12.56 |
| D2 P1 桥接行 | 1866.24 | **1856.16** | −10.08 | +5.84 |
| D2 P2 栏目标题 | 1865.76 | **1855.68** | −10.08 | +6.32 |
| D3 家具行 P2–P6 | 1864.00 | **1853.92** | −10.08 | +8.08 |
| D3 P8 答案头行 | 1864.00 | **1854.08** | −9.92 | +7.92 |

**全部 ≤1862，最小余量 5.84px ≥ 要求的 1px。D1/D2/D3 修讫。**
整页墨右（不含页脚带 y>2550，供参考）：修前 P1 1866.24 / P2 1865.76 / P3–P5 1864.00 / P6 1866.24 / P7 1861.92 / P8 1864.00；修后 P1 1862.24 / P2–P8 1861.92。P1 修后 1862.24 经 600 dpi 逐行定位，成分为：刊头日期行（y 79.7–91.2，锚 RIGHT=1885 的页眉元素，1862 限不适用）、hline 端点（y 419/1689/2311，SVG 规定 x2=1862.0）、P1 右栏照片边（y 469.9–587.8，满栏图至 1862）、页脚（y>2613，已排除）——均非缺陷文本行；D2 行所在 y 2334–2346 带修后已不在 x>1861 之列。P2–P8 的 1861.92 同为满栏图/hline 的设计边。

## 5. 修后三 SHA（定稿候选，皆在 scratch rebuild/ 内；生产 PDF 未覆盖）

- 印 PDF：`e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5` / 12,669,546 B
- 网 PDF：`48b35efc1b858a143bed01075ca22038123770f31e064e2818caf2db99ba812f` / 1,616,171 B（注：网 PDF SHA 不可重现，仅比文字层——见 §6）
- 文：`44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` / 47,649 B（未变，与修前同一）

## 6. 其余已验证存活（修后逐项复测，见 GATE-LOG.md）

- freeze diff（core-nl svg vs 重建 svg）：rc=0；新增 CJK 仅 U+3000 全角空格 ×7（P2–P8 各 1，双语分隔符，fan-out 正常）。
- freeze baseline（core-nl）：**8/8 SVG 字节一致**，核心 SVG 完整性复核无变化。
- p8 compare：**CLEAN**，核心与本版各 150 noted，keydiff [137, 138]（与修前一致，已裁定）。
- occlusion audit：自检 6 类全触发 + 干净对照静默；重建 SVG **0 flags**。
- P8 最小字号：**10.12pt**（不变，≥ SOP §1.1 底线 9.75pt）。
- 题量：150/150（run.py TOTAL 150；by page 与修前一致）。
- 文字层：重建网 PDF vs 重建印 PDF 的 pdftotext **0 行差异**（各 46,815 字节）；修前网 PDF vs 修后网 PDF 多重集一致（仅 1 空行 + 137–139 行 pdftotext 读序抖动，内容无差）；修前印 PDF vs 修后印 PDF 多重集一致（仅 1 空行差）。文字内容零改动。
- 元素级 SVG 比对：除 9 处修复外零差异（§3）——D6–D11（w 值、D9 kort 契合、D11 P4 盒基线余量等）所在元素均未动。

## 7. 生产零写入核对

- 开工快照 `snapshot-before.sha256`（44 文件）vs 收工 `snapshot-after.sha256`：**仅 5 个 .py 文件 SHA 变化**（bslib4.py、content12.py、content34.py、content56.py、content8.py，即本次修复）；全部 PDF、SVG、.text.md、ABSTRACT.txt、WEEKLY-KIT.md、assets、cards 均与开工一致。生产网 PDF 未覆盖。
- 核心未碰：core-nl 全部操作只读（freeze diff / p8 compare / freeze baseline 的 copy 在 scratch 内跑；baseline 报告核心 SVG 完整性无变化）。另：`git status` 显示 core-nl 有 3 文件 M（.text.md、FIX-LOG.md、WEEKLY-KIT.md），mtime 为 15:58–16:28 UTC，**早于本次开工（~18:20 UTC）**，为他人在先的未提交工作，非本次写入。
- 未 commit、未 push。定稿须另派独立 re-proof（本修复员不管复校）。
