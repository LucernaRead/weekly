# SYNC-LOG — Lucerna Weekly 2026-W47 · nl-es fix1 同步

同步员：W47 nl-es fix1 同步员（子代理）。只在
`production/2026-w47/2026-w47-nl-es/` 与
`hidden_files/w47/scratch-fix-nl-es2/` 工作，未碰核心与其他版；不 commit、不 push。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-nl-es2/`
（唯一、专用；未复用 scratch-fix-nl-es1/）。

## 0. 开工探针与核对（2026-11-11 ~19:18 UTC）

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`（rc=0）；
  scratch 内真实写文件成功（probe.txt）。`/dev/null` 存在，无需补建。
  TMPDIR 一律用 `$S/tmp`（`/tmp` 只有 512M）；Python 一律用 repo venv
  `tools/venv/bin/python`（Pillow 13.0.0）；`PYTHONDONTWRITEBYTECODE=1`。
- 生产三 SHA 与任务先验逐字节一致，方动手：

  | 文件 | SHA-256 | 字节 |
  |---|---|---|
  | 印 `De-Lucerna-VOL4-nl-es.pdf` | `45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` | 12,669,539 |
  | 网 `De-Lucerna-VOL4-nl-es-web.pdf` | `47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` | 1,616,177 |
  | 文 `2026-w47-nl-es.text.md` | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` | 47,649 |

- 生产 5 个 .py 的 10 处修复逐行核对，均在位（字符串未动）：
  - `bslib4.py:21` `NOTE_RIGHT = RIGHT - 10`（注释 :13–20，ru-pt 同法说明）。
  - D2（2 处）：`content12.py:147`、`:214` `p.text(NOTE_RIGHT, …)`。
  - D3 家具行（5 处）：`content12.py:235`、`content34.py:50`、`:147`、
    `content56.py:65`、`:183` `p.text(NOTE_RIGHT, …)`，均带
    `# fix1 D3: … (shared furniture, n of 5)`。
  - D3 P8（1 处）：`content8.py:133` `p.text(NOTE_RIGHT, 1302, …)`。
  - D1（1 处）：`content56.py:150–152` 注释 + `:153` 图标题字号 24 → 23，
    字符串 `"DE GRAFIEK　DATOS DE PRÁCTICA"` 不变。
  - **编号出入（已核实，非缺失）**：任务写第 5 处家具行在
    `content56.py:180`，实际在 `:183`（内容与 `# fix1 … 5 of 5` 注释一致）；
    其余 9 处行号与任务一致。范围外 `p.text(RIGHT…)`（刊头日期
    `content12.py:16`、P1 鹅黄头条 `:27/:28`，锚 RIGHT−30）未动。
- 防呆：开工快照 `snapshot-before.sha256`（42 文件，不含 `__pycache__`）；
  复制生产源码到 `$S/rebuild/`（`cp -r`，删副本内 svg/cards/`__pycache__`），
  验 `content*.py` 的 `OUT` 均为 `__file__` 相对路径（→ 副本 `svg/`），
  `render.py` 的 `BASE` 亦为 `__file__` 相对路径，重定向一律用绝对路径、
  目标均为自己的 scratch。同步前复核生产与快照一致（零变化）。

## 1. 重建（全在 scratch 副本内）

- `run.py`：rc=0，TOTAL **150**；by page 10/18/18/18/18/18/12/38；
  A2 46 / B1 73 / B2 31；日志无 OVERFLOW/TOO WIDE/error
  （`run-fix1.log`）。
- `render.py`：rc=0，8 cards；印 PDF 12,669,546 B，SHA
  `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5`——
  **与修复员候选逐字节一致**（构建确定性核对通过）
  （`render-fix1.log`）。
- `webpdf.py`（`tools/webpdf.py rebuild/svg → rebuild web PDF`）：rc=0，
  1,616,170 B，SHA
  `55e8489d18ee3d038c1da5a3c93aea144d2221289c98603c3c808306d577ad0b`，
  46,815 text bytes。候选为 1,616,171 B /
  `48b35efc1b858a143bed01075ca22038123770f31e064e2818caf2db99ba812f`：
  **相差 1 字节，SHA 不同——网 PDF SHA 不可复现是已知现象；文字层
  pdftotext 逐字节一致**（见 §2）。
- SVG 元素级比对（`svg_diff.py`，生产 svg vs 重建 svg；修复员脚本写死
  旧路径跑不起来，在本 scratch 重写了同逻辑参数化版本）：
  8 页元素数一致（229/222/207/204/213/225/203/431）；
  **仅 9 处不同**，恰为本次修复：P1 行 x 1141.9→1131.9；P2 两行
  1200.1→1190.1、1175.3→1165.3；P3/P4/P5 家具行 1175.3→1165.3；
  P6 标题 24→23 + 家具行 −10；P7 0 处不同（字节一致）；P8 行
  1120.8→1110.8。重建 SVG 与修复员候选 SVG 逐字节一致；重建 cards
  与候选 cards 逐字节一致。

## 2. 文字层比对

- 重建网 PDF vs 候选网 PDF（pdftotext）：**0 行差异**，提取文本均为
  106,408 B（`web-mine.txt` vs `web-cand.txt`）。
- 重建网 PDF vs 重建印 PDF：**0 行差异**。
- 重建印 PDF vs 修前生产印 PDF：仅空白列移位（9 行被修行的位置移动
  + 标题字号变化引起的列宽变化），多重集文字内容一致；plain pdftotext
  均为 46,815 B（修前 46,814 B 相差 1 B 为列对齐空白）。

## 3. 同步进生产

同步文件（17 个，含 KIT）：

- SVG 7 个：`svg/p1-voorpagina.svg`、`p2-leven.svg`、`p3-cultuur.svg`、
  `p4-sport.svg`、`p5-jongeren.svg`、`p6-verdieping.svg`、`p8-toets.svg`
  （`p7-taal.svg` 字节不变，未变）。
- cards 7 个：`cards/p1-voorpagina.png`、`p2-leven.png`、`p3-cultuur.png`、
  `p4-sport.png`、`p5-jongeren.png`、`p6-verdieping.png`、`p8-toets.png`
  （`p7-taal.png` 不变）。
- `De-Lucerna-VOL4-nl-es.pdf`、`De-Lucerna-VOL4-nl-es-web.pdf`。
- `WEEKLY-KIT.md`：Files delivered 写新三 SHA/字节数；追加
  `## Fix round 1 (… build 5)` 一节，旧 SHA 保留在该节。
- 同步后快照比对（`snapshot-before.sha256` vs `snapshot-final.sha256`）：
  **恰 17 文件变化**，即上述 16 交付件 + KIT；`.py` / `.text.md` /
  `ABSTRACT.txt` / `assets/` 字节不变；生产 `__pycache__/` 两个 `.pyc`
  与修复员 `snapshot-after.sha256` 逐字节一致（未写入字节码）。

## 4. 新三 SHA（生产，以同步后实测为准）

| 文件 | SHA-256 | 字节 |
|---|---|---|
| 印 `De-Lucerna-VOL4-nl-es.pdf` | `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5` | 12,669,546 |
| 网 `De-Lucerna-VOL4-nl-es-web.pdf` | `55e8489d18ee3d038c1da5a3c93aea144d2221289c98603c3c808306d577ad0b` | 1,616,170 |
| 文 `2026-w47-nl-es.text.md` | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb`（未变） | 47,649 |

## 5. 门禁（同步后，对生产文件重跑，全部 PASS）

| 门 | 实测值 |
|---|---|
| D1/D2/D3 交付印 PDF 渲染像素（`edge_raster.py`，600 dpi，限 1862） | D1 P6 图标题 **1849.44**（余量 +12.56）；D2 P1 **1856.16**（+5.84）；D2 P2 **1855.68**（+6.32）；D3 P2–P6 **1853.92**（+8.08）；D3 P8 **1854.08**（+7.92）。最小余量 **+5.84px**，与修复员实测逐值一致。整页墨右（不含页脚）：P1 1862.24（刊头日期 + hline 端点 + 满栏照片边，设计边，与修前一致），P2–P8 1861.92；P7 修前修后同为 1861.92。 |
| D1/D2/D3 PIL 真墨（同字体文件 4× 超采样 PIL 渲染逐行量测，`pil-render-sync.json`） | D1 **1845.5**（+16.5）；D2 P1 **1850.75**（+11.25）；D2 P2 **1850.5**（+11.5）；D3 家具行 **1850.5**（+11.5）；D3 P8 **1850.5**（+11.5）。均 ≤1862。另：生产 cards 的 Cairo 渲染同带量测为 D1 1846、D2 1846、D3 1844、P8 1852（`pil-edge-sync.json`），亦全部 ≤1862。注：PIL 法比 PDF 渲染法系统性小约 5px，方向与已知“PIL 低估 Cairo/PDF 排宽”一致；门禁以 PDF 渲染像素为准，最小余量仍为 +5.84px。 |
| freeze 核心 baseline | rc=0，**8/8** SVG 字节一致；核心 SVG 完整性复核无变化（`freeze-baseline-sync.log`）。 |
| freeze diff（core-nl vs 生产） | rc=0；新增 CJK 仅 U+3000 ×7（P2–P8 各 1），与修前一致。 |
| p8 extract | **150/150** noted。 |
| p8 compare | **CLEAN**；keydiff **[137, 138]**（与修前一致）。 |
| occlusion audit | **0 flags**（自检 6 类全触发，干净对照静默；`occlusion-sync.json`）。 |
| 印/网文字层 | 8 页 **posdiff 0 / msdiff 0**；tokens 812/820/727/731/794/743/913/2403；pdftotext 印 46,815 B = 网 46,815 B。 |
| P8 最小字号 | **10.12 pt**（中位 10.12，184 spans；≥ 9.75pt 底线；与修前一致）。 |

## 6. 备注

- `edge_raster.py` 全页 600 dpi 渲染耗时约 12.6 分钟（单页 ~620MB RGB，
  逐页流式）；前两次前台跑分别在 180 秒工具时限被杀（只跑到 P1/P3），
  改后台跑完成，rc=0。
- `hidden_files/w47/briefs/brief-coordinator.md` 不存在（与修复员开工
  发现一致）；本次按任务正文 + SOP + ru-pt fix1 已验做法执行。
- 未 commit、未 push。定稿须另派独立 re-proof。
