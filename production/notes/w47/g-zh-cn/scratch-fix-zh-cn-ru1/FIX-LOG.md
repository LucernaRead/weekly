# FIX-LOG — W47 zh-cn-ru fix1 (proof1 D-01 only)

- **修复员**：fix1（subagent，2026-11-11）
- **对象**：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ru/`
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-ru1/`（唯一 scratch；全部日志、渲染、裁图在此）
- **性质**：只修 proof1 唯一缺陷 D-01；余项全过不碰；未 commit、未 push、未 insert、未跑 lint。
- **解释器**：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；`TMPDIR` 一律指向本 scratch；凡 import 生产源码均设 `PYTHONDONTWRITEBYTECODE=1`。

## 0. 开工探针与身份（三 SHA 自算，与任务书先验一致）

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29…`）；scratch 真实写盘 `probe.txt` 成功。
- 开工三 SHA（收尾已变，见 §5）：

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-RU.pdf`（印） | 33,572,611 | `7cd883dd1b5311e878abc0d8a2a899864c69cdae6b03aed740d738a3a9b19b93` |
| `Lucerna-VOL4-RU-web.pdf`（网） | 2,486,444 | `ab0aaf106dba13e9b329550b560ad59757d71e528793fdceeb75bbf8955634f6` |
| `2026-w47-zh-cn-ru.text.md`（文） | 60,515 | `f722ad0fb0f617bcb54c76afb2163b00f6fc7b9c7af79bc46e3476214717cd3d` |

- 开工 SVG 快照 `svg-sha-before.txt`（8/8）；`__pycache__` 未动（mtime 仍为 2026-11-11 14:30:58）；`ABSTRACT.txt` 未动（426 B，mtime 14:30:57）。

## 1. 缺陷与修法（只动一处）

- **D-01（proof1，中-轻）**：P1 截稿盒（rect x=1439.5 y=588.0 w=422.5 h=700.0，盒右 1862.0）末行俄文越出盒右缘。源码 `content12.py:88`，SVG 元素 x=1461.5 y=1252.0 size=19 `Noto Sans CJK SC`。
- **修前实测（本轮复现 proof1 数值，分毫不差）**：PIL 真墨（NotoSansCJK-Regular.ttc index 2，19 pt）原串 `Время сдачи: 10 нояб. — финал ещё не сыгран` advance 430.2，ink_right **1891.5**，盒右 1862.0，**越 29.5 px**。
- **修法（删词，不加词、不改意、不降字号、不拆行）**：删 `ещё `（一词），得 `Время сдачи: 10 нояб. — финал не сыгран`（仍是“决赛还没踢”，语义成立；与 it 版 D-02/D-03 缩短修法同类）。
- **改动清单（全文）**：
  - `content12.py:88`：仅该行一串。`:86` 长段落（含完整事实：决赛 15 日 03:00 北京、半决赛 8–9 日已出结果）**未动**——修后 SVG 中 `:86` 段的 `ещё` 仍在 1 处（`на момент сдачи ещё / не сыгран`，裁图目视亦在位）。
  - `2026-w47-zh-cn-ru.text.md:127`：导出器（`export_ed.py ru`）重生成，`diff` 对修前文件**仅 127 行一处**变化（60,515 → 60,508 B，恰少 7 字节 = `ещё ` 的 UTF-8 长度）。`:123` 长段落未动。
  - registry / P8：`content34/56/7/8.py` 中无该串（grep 0 处），无需同步。
  - 未动：导出器 `ru_textmd.py:616` 类型检查 bug（与本次无关，批量修复另有安排）——未顺手改。

## 2. D-01 双法重测（修后，交付文件实测）

| 方法 | 墨右 | 盒右 1862.0 | 余量 | 要求 |
|---|---|---|---|---|
| PIL 真墨（新串，19 pt） | **1850.5** | 1862.0 | **+11.5 px** | ≤1862.0 且 ≥+5 px ✓ |
| 交付印 PDF 150 dpi 渲染像素（`render-p1-fix1.png`，3047×4219 px，0.63997 units/px） | **1848.2 units** | 1862.0 | **+13.8 units** | ≤1862.0 且 ≥+5 ✓ |

- 渲染像素法校准：奶油盒右缘在 y=650 处实测 **1861.7 units**（与 proof1 的 1861.7 一致）；同盒 18.5 pt 段落行最右墨 1836.7 units（proof1：1836.1，0.6 为阈值/舍入噪声，仍余 25.3）。
- SVG 元素复核（`svg-texts.json`）：P1 y=1252.0 单 run，x=1461.5 size=19，新串在位。
- **裁图目视**：`crop-p1-pressline-fix1.png`（交付印 PDF 150 dpi 裁图，2× 放大）——末行 `Время сдачи: 10 нояб. — финал не сыгран` 完整落在奶油盒内，尾部 `сыгран` 距盒右缘有明显空隙；长段落 `ещё` 未动。
- 结论：D-01 已修掉，双法余量均 ≥+11 px。

## 3. 门禁（全部自跑自验）

### 3.1 run.py scratch 重建（OUT 重定向绝对路径，生产 SVG 零写入）

- 方法：复制 `*.py + assets/` 到 `<scratch>/rebuild/`，5 个 `content*.py` 的 `OUT` 在**副本**中重定向为绝对路径 `<scratch>/rebuild/svg`（跑前已验写盘目标；生产文件未动——重建前后生产 SVG sha 与开工快照一致）。
- 结果：**rc=0；TOTAL 150**（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38）；`FLOW OVERFLOW` / `HEAD TOO WIDE` **0 次**；P7 teaser 2588.78；P8 keys 2535.1；P8 测验流 964.8、配图末 1270.6。日志 `run-rebuild.log`。
- **SVG 变化页清单：仅 p1**——重建 SVG vs 修前生产 SVG：p2–p8 字节一致 7/7，p1 唯一变化（`be2231cb…` → `fbe71fe7…`）；p1 文本级 diff 仅一串删/增（旧串出、新串入），其余文本元 0 差异。重建 SVG 已提入生产 `svg/`（8/8 与重建一致，`svg-sha-production-after.txt`）。

### 3.2 gates-zhcn.py 11 门（`gates-fix1.log` / `gates-ru.json`）

**rc=0，OVERALL: ALL PASS。**

| 门 | 结果 |
|---|---|
| occlusion | rc=0，0 flags（selftest OK，另见 §3.3） |
| img_overlap | hits=0 |
| p8_extract | rc=0，noted=150/150 |
| p8_compare | rc=0，CLEAN，keydiffs=0 |
| freeze_sha256（本版自身重建） | run rc=0，match=8/8 |
| print_web_text | 8/8 页，posdiff=0，msdiff=0（P1 355/355、P2 350/350、P3 259/259、P4 336/336、P5 267/267、P6 315/315、P7 478/478、P8 1566/1566；P1 由 356→355，恰为删去的一词） |
| pdftotext_nonempty | print=52,554 B，web=52,554 B，web_size=2,486,423（修前 52,561 B，恰少 7 B） |
| p8_fontsize | answer-zone min=9.98 pt，median=9.98 pt，spans=906 |
| p8_chips | core={'A2': 11, 'B1': 24, 'B2': 3}，edition 相同 |
| u2019 | files_with_U+2019=[] |
| s11_svg | off-palette={}，gold/old=False，stroked_rects=0，VOL.5=1（core 1），paper_fills=8 |

### 3.3 freeze / occlusion / p8（独立重跑）

- `freeze.py baseline`（核心，`--core-svg` 指向核心 `svg/` 子目录）：**rc=0，8/8 SVGs byte-identical**，core integrity：shipped core SVGs unchanged by the run。日志 `freeze-baseline-fix1.log`，产物 `freeze-baseline/`（仅 scratch 内）。
- `freeze.py diff --strict-cjk`（核心 vs 本版）：**rc=0，TOTAL added CJK characters: 0**；逐页 added CJK 均为 0（P1 +91/−45、P2 +71/−52、P3 +40/−39、P4 +117/−43、P5 +39/−38、P6 +114/−41、P7 +338/−105、P8 +1405/−208——与 proof1 逐页计数完全一致）。日志 `freeze-diff-fix1.log` / JSON `freeze-diff-fix1.json`。
- `occlusion_audit.py --selftest`：rc=0，**selftest OK**（planted 6 类全触发，clean 对照静默）。本版 `occlusion_audit.py svg/`（版目录内跑）：rc=0，**0 flags**。
- `p8.py extract`（独立）：rc=0，noted set = **150 of 150**。`p8.py compare`（独立）：rc=0，**CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**。

### 3.4 奶油盒横向真墨全扫（proof1 同法，`cream-sweep-fix1.log`）

- 全刊 599 个奶油盒内文本元逐个量右缘——**溢出 0 处**（proof1：仅 D-01 一处）；贴边（<8 px）**0 处**。**0 新增溢出**，D-01 为唯一变化。

### 3.5 字号（PyMuPDF 独立实测，印/网一致）

- P8 最小 **9.98 pt** ≥ 9.75 pt；各页最小：P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、P8 9.98 pt——与 proof1 分毫不差。

## 4. 双 PDF 重建与同步（fixer 规则；印/网均重建并同步）

- `render.py`（印 PDF）：rc=0，8 张 cards 全重渲；印 PDF 33,572,610 B（修前 33,572,611 B，少 1 B）。**披露**：第一次 `render.py` 前台执行在约 1 分钟时被 runtime 中断（`aborted`；当时仅 cards p1–p4 已写、印 PDF 仍为旧 SHA），改后台重跑完整一次 rc=0——cards 与印 PDF 均为同一次完整重建产物，无半截状态。
- `webpdf.py`（网 PDF，patched 版）：rc=0，`WROTE … 2,486,423 bytes, 52,554 text bytes`；774 distinct chars；各 subset 字体字节数与修前一致（Newsreader-Italic 22,548 B）。**印/网双 PDF 均已同步到生产目录**（nl-es fix1 只建不 sync 的教训已避开）。
- `export_ed.py ru`（文）：rc=0，recorded strings 1050，registry 150；仅 text.md:127 变化（见 §1）。

## 5. 收尾三 SHA（新，实测）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-RU.pdf`（印） | 33,572,610 | `bcfc550ff96ae87ce46fe1199592f5c7a690b91325dd3d5a410b11d95061305b` |
| `Lucerna-VOL4-RU-web.pdf`（网） | 2,486,423 | `8d3f72d35d4ac78cb0c9f52f56a930dae1c9251fc3a4527841bc30dd0ac888d3` |
| `2026-w47-zh-cn-ru.text.md`（文） | 60,508 | `de12db587c41005301b221cce52ae0d088ec52f9eaccf2338aa94382f00e8094` |

- 旧三 SHA 见 §0（已保留于 WEEKLY-KIT.md Fix round 1 一节）。
- SVG 变化页：仅 p1（`fbe71fe70b527054d85ec6390aba3810dea88b0b3d46f86684c3dbd1c18ec104`）；p2–p8 与修前逐字节一致。
- 本轮未改动核心与其他任何版（`git status` 中他版的 M 项为并行他 agent 的工作，与本轮无关）。

## 交付物（本 scratch）

- 本文件 `FIX-LOG.md`；`run-rebuild.log`、`render-fix1.log`、`webpdf-fix1.log`、`export-fix1.log`、`gates-fix1.log`、`gates-ru.json`、`freeze-baseline-fix1.log`、`freeze-diff-fix1.log`、`freeze-diff-fix1.json`、`occlusion-selftest-fix1.log`、`occlusion-fix1.log`、`p8extract-fix1.log`、`p8compare-fix1.log`、`svgtexts-fix1.log`、`svg-texts.json`、`cream-sweep-fix1.log`、`cream-sweep.json`、`measure-fix1.log`、`measure_fix1.py`、`render-p1-fix1.png`、`crop-p1-pressline-fix1.png`、`svg-sha-before.txt`、`svg-sha-rebuild.txt`、`svg-sha-production-after.txt`、`sha-before.txt`、`sha-after.txt`、`textmd-before.md`、`probe.txt`、`rebuild/`（scratch 重建副本）。
- 生产目录更新：`WEEKLY-KIT.md`（Fix round 1 一节 + 新三 SHA；旧 SHA 保留）。
