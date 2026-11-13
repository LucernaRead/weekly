# GATE-LOG — 2026-W47 core-ja Fix 1（核心笔误 key 47）

- 对象：`production/2026-w47/core-ja/`（2026-w47-ja-zh-cn，VOL.4）
- 解释器：全部 Python 门均用 `~/workspace/weekly-git/tools/venv/bin/python`
  （与构建同一解释器）；textmd 导出用系统 python3（纯标准库）。
- 旧双 PDF（修前）：印刷 26,018,003 B /
  `e1782168d89d06cd080dd7acf62b6dafc69ca7dc5c6c839e698e25c3de2466bd`；
  网页 4,652,749 B /
  `7c21329c89efcda759e5aeb91fffd7ac47871b36a6a03a29652f7ccf598c5a1c`。
- 新双 PDF（修后）：印刷 26,018,019 B /
  `20b9d50469fbb6ca6470c17becb2790a30f69191d9083520a9270ea7ebbe9ab4`；
  网页 4,652,763 B /
  `8722bdfbcec0478a7a60fc86ab0ee7cc9333f957253959476d4f608eed82d5b0`。

## 1. 身份与探针

| 检查 | 结果 |
|---|---|
| git hash-object 探针 | 通过（`da0c4eb8…`） |
| scratch 真实写盘探针 | 通过（`.probe`） |
| 旧双 PDF 字节 + SHA-256 | 通过，与任务给定一致 |

## 2. 构建

| 步骤 | 结果 |
|---|---|
| `run.py` 第 1 次 | exit 0；FLOW OVERFLOW / HEAD TOO WIDE 0 条；TOTAL 150；A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；题型 完成句子 50 / 单选 51 / 完形单选 13 / 词汇配对 12 / 判断对错 11 / 造句 8 / 翻译 4 / 写作 1 |
| `run.py` 第 2 次 | exit 0；零溢出；登记与第 1 次一致；SVG sha256 与第 1 次逐个一致 |
| `render.py` | exit 0；8 张 cards PNG + 印刷 PDF 26,018,019 B |
| `webpdf.py` 第 1 次 | RC=120 失败（日志止于第 1 支 subset 字体，无 traceback；旧网页 PDF 未被覆盖）——瞬时配额满所致，见 FIX-LOG §8 |
| `webpdf.py` 第 2 次（新 TMPDIR） | exit 0；WROTE 4,652,763 B，44,818 text bytes；844 distinct chars；5 支子集字体 |
| text.md 导出 | 导出器先对修前 SVG 验证：与修前 text.md 逐字节一致；新 text.md 44,432 B，diff vs 修前仅 1247 行 |

## 3. 机械门

| 门 | 结果 |
|---|---|
| freeze baseline（`tools/freeze.py baseline`） | 8/8 SVGs byte-identical；仅 p8-tesuto.svg 变化（`9db7294a…` → `f7118644ac8b31a4be2f04c7044afd0a9043592bfd89d1b45c1b0526c08798a2`）；P1–P7 与修前一致；core 完整性：运行前后重哈希一致 |
| occlusion（`tools/occlusion_audit.py`） | 自检通过（6 类 planted 全触发，clean 对照静默）；0 flags |
| p8 extract（`tools/p8.py extract --total 150`） | noted set 150/150（`ja-core-p8-fix1.json`）；与修前 `ja-core-p8.json` 对比：集合相等，keys 150/150，0 key diffs |
| print/web 文字层 | `pdftotext` 各 44,818 B，`cmp` 逐字节一致；web `-layout` 85,061 B |
| P8 最小字号（PyMuPDF，印刷 PDF） | 全期各版最小 11.62/12.75pt；P8 最小 9.98pt（≥9.75pt 门槛；Round-5 Tm 矩阵值 9.975pt，同一字号）；P8 题干 10.35pt（79 处）未动 |
| U+2019 全扫 | SVG 8 份 + text.md + content*.py/bslib4.py/svglib.py 合计 0 |
| §1.1 grep 审计 | 旧纸色 `#f7f1e2` 0×；禁用金 `#c9a227` 0×；`·` 0×；`第N版／共8版` 1×/版；纸色 `#fbfaf6` 1×/版；VOL.4：P1 3×、其余各版 1× |

## 4. 150 键逐题复核（登记 vs 印刷 P8 答案行）

- 登记 dump（`registry-fix1.json`，freeze build-copy 内运行）：TOTAL 150，
  n 1–150 连续，级别 A2 48 / B1 73 / B2 29。
- 逐字一致：145 条（`{n}. {key} — {note}` 与 P8 SVG 抽取行逐字相等）。
- 余 5 条为冻结版式，与修前逐字节一致，非差异：
  - F 组 141–144：P8 先印题干行（`141. 熊手` …），键行另列
    （`141. c — 熊手＝祈求生意兴隆的竹耙 c` …），两行均在 text.md 1345–1348 行；
  - 写作题 150：登记 key 为「（开放题，范文如下）」，印刷为
    `150. ✓ 范文见本版 H 区（154 字）`（W46 既定版式）。
- 与修前 text.md 166 条答案行逐条对比：仅 1 处差异——key 47
  （`一之富士` → `义之富士`）。键值零差异。
- key 47 印刷行：`47. A — 首日战胜大之里的是义之富士`；
  key 115 印刷行：`115. A — 大之里首日输给了义之富士`。

## 5. 重建后 grep 验证

| 串 | py | text.md | svg |
|---|---|---|---|
| `一之富士` | 0 | 0 | 0 |
| `义之富士` | 2 | 2 | 2（修前 1+1） |
| `一之酉`（正确，应保留） | 1（content12.py:261） | 1（:1217） | — |

## 6. 8 版目视（新印刷 PDF，100 dpi 新渲染）

| 版 | 结果 |
|---|---|
| P1 | 干净；头条、趋势栏、数字栏、快讯、闪电问答、页脚均清晰，无溢出重叠 |
| P2 | 干净（特征栏短栏空白为 KIT §7 已披露的 W46 冻结版式，非缺陷） |
| P3 | 干净；葡萄园图 + 图注 + 文化日历正常 |
| P4 | 干净；ex 47 题干「義ノ富士」正确；记录盒、横纲 3 日栏正常 |
| P5 | 干净；岚山图 + 流行语栏正常 |
| P6 | 干净；图表标签与柱条分离（京都/浅草/高尾山/家），练习区正常 |
| P7 | 干净；诊所栏、金句栏、鸟居图 + 图注、读者园地披露、VOL.5 预告正常 |
| P8 | 干净；练习流、范文、寺图、答案区完整，答案流未压页脚；答案区放大裁图确认 key 47「义之富士」字形清晰；网页版 P8 同区裁图与印刷版逐字节一致（sha256 `82582d5e…`） |

## 7. 未跑 / 未动

- 未跑 insert.py、lint --write；未 git add/commit/push/reset/stash。
- 未碰 W43–W46、其他目标语家庭、tools/、fan-out 版。
- KIT §3 罗马字误拼（Umi-no-umi、Fujiryūga）未动（另案）。
