# GATE-LOG — 2026-W47 ja × zh-tw 第一轮返修（叶子 fix1）

- 版：`2026-w47-ja-zh-tw`，VOL.4，2026-11-16–22；构建解释器：`tools/venv/bin/python`（与构建相同）。
- 证据目录：本目录（`hidden_files/w47/scratch-ja-zh-tw-fix1/`）。旧轮次证据在 `../scratch-fanout-ja/`（`zh-tw-*-run2.*`、`build-zh-tw-run*.log`）。
- 结论速览：**全套机械门全部通过；150 键复核通过；8 版目视干净。** 修后待协调员派第一轮全量复校（未做）。

## 1. 构建门

| 门 | 证据 | 结果 |
|---|---|---|
| run.py run1 | `build-zh-tw-fix1-run1.log` | rc=0，TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE |
| run.py run2 | `build-zh-tw-fix1-run2.log` | 0 字节——磁盘配额 EDQUOT 中断（见 FIX-LOG §4），作废，不计 |
| run.py run3 | `build-zh-tw-fix1-run3.log` | rc=0，TOTAL 150（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38；类型 完成句子 50 / 單選 51 / 完形單選 13 / 詞彙配對 12 / 判斷對錯 11 / 造句 8 / 翻譯 4 / 寫作 1；范文 154 字），0 溢出 |
| run.py run4 | `build-zh-tw-fix1-run4.log` | rc=0，同上，0 溢出 |
| render.py | `render-zh-tw-fix1.log` | rc=0，8 cards + print PDF 26,034,685 字节 |
| webpdf.py | `webpdf-zh-tw-fix1.log` | rc=0，8 页，799 字，44,661 text bytes，web PDF 4,788,782 字节 |
| export text.md | `export-zh-tw-fix1.log` | rc=0，44,361 字节，1325 text lines |

## 2. 冻结门（--strict-cjk 语义：CJK 读者版新增 CJK 必须为 0）

- `zh-tw-sha-fix1-run3.txt` vs `zh-tw-sha-fix1-run4.txt`：**8/8 逐字节一致**（`diff` 无输出）。
- 相对修前 `zh-tw-sha-fix1-pre.txt`：**仅 `svg/p8-tesuto.svg` 变化**（`59598a93f2688967af26c038a89c7dee3f02d9ebb23cd21257dc04875dfba666` → `f0d2ebe5e3a37bd1cf91cfcd6a4c64d4aba367adf41d57e4ec163c7c271da656`），其余 7 页 sha 与修前完全一致——与“一字修复只动 P8”一致。
- 本版为 CJK 读者版：新增 CJK 字符数 = 0（修复为既有字的替换 `一`→`義`，非新增；且除 p8 外无任何页变化）。

## 3. 几何遮挡审计（tools/occlusion_audit.py）

- `zh-tw-occlusion-fix1.json` + `occlusion-fix1.log`：自检 OK（6 类阳性对照 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1 触发，干净对照静默），实审 **`svg: 0 flags`**（`flag_count: 0`）。
- 注：首次调用误带 `--selftest`（该 flag 为仅自检模式，只出自检行）；已按旧例改从版目录不带该 flag 重跑实审，两次自检均 OK。

## 4. P8 门（tools/p8.py）

- extract：`zh-tw-p8-fix1.json` + `p8extract-fix1.log`——**noted set = 150 of 150**，题号 1–150 连续无缺重。
- compare（vs core-ja `svg/p8-tesuto.svg`）：`zh-tw-p8compare-fix1.json` + `p8compare-fix1.log`——**CLEAN**，`missing=[] extra_count=0 uncertain=[]`，**keydiff=[139, 140]**。
- keydiff [139, 140] 为本版预期值（KIT §11 F3 已裁定）：137/138 与核心逐字节相同（无简体特有字），故不进入 keydiff；不得当缺陷“修”。

## 5. 文字层门

- `pdftotext` print / web 各 **44,661 字节**，`cmp` **逐字节一致**；两版 8 页均有文字层。
- 两版文字层中 `義之富士` 各 2×（key 47、key 115），`一之富士` 各 **0×**。

## 6. P8 最小字号门（PyMuPDF，tools/venv）

- print PDF 8 页；P8 共 371 spans，最小字号 **9.975pt**（与 KIT 冻结值 9.975 一致），全部 spans **≥ 9.75pt**；次档 10.35pt 不变。
- 附：只取 P8 最小值的方法与旧轮次一致（P8 全 spans 排序取首）。

## 7. U+2019 与 §1.1 / 残留扫描

| 扫描 | 范围 | 结果 |
|---|---|---|
| U+2019（’） | text.md + 8 SVG + content*.py | **0** |
| 纸色 `#fbfaf6` | SVG | 8×（1×/页） |
| 旧纸 `#f7f1e2` | SVG | **0** |
| `·` | SVG + text.md | **0** |
| 页行 `第 N 版 / 共 8 版` | SVG | 8× |
| 金/红褐 `#c9a227`/`#8b4513` | SVG | **0** |
| 简体残留 `参考答案` | text.md | **0** |
| `參考答案` | text.md | 1×（正确） |
| `吉伊卡哇` | text.md | 4×（正确读者译名） |
| `售` / `呢` | text.md | 5× / 3×——简繁同形字，KIT §11 F4 已裁定为误报（`開始發售` / `你呢？`） |

## 8. 全版 `一之富士` 终验（源码、text.md、SVG、双 PDF 文字层）

| 位置 | `一之富士` | `義之富士` |
|---|---|---|
| `content34.py`（key 47） | 0 | 1 |
| `content8.py`（key 115） | 0 | 1 |
| `2026-w47-ja-zh-tw.text.md` | 0 | 2（:1243 key 47、:1315 key 115） |
| `svg/*.svg`（仅 p8） | 0 | 2 |
| print PDF 文字层 | 0 | 2 |
| web PDF 文字层 | 0 | 2 |
| **合计（源码+text.md+SVG）** | **0** | **6** |

## 9. 150 键逐题复核（`key-review-fix1.txt` 全表）

- text.md P8 区答案行 150 条，题号 1–150 连续、无缺重；P8 SVG 答案行亦 150 条，序列一致；**text.md 与 P8 SVG 逐键值比对差异 0 条**。
- 抽检点（与 KIT §3 记录值逐字比对）全部通过：
  - 47 `A — 首日戰勝大之里的是義之富士`（本次修复，唯一变化）
  - 115 `A — 大之里首日輸給了義之富士`
  - 137 `二之酉在11月19日。 — 對照第2版`
  - 138 `新酒在11月19日解禁。 — 對照第3版`
  - 139 `流行語提名在11月5日發表。 — 對照第5版`
  - 140 `去看紅葉的人應該同時確認預報日期和現在的狀況。 — 對照第6版`
- “除 key 47 注文一字外与上一轮一致”的依据（旧 text.md/PDF 无别处副本可逐字比对，如实说明）：
  1. 本次唯一源码改动为 `content34.py:186` 一字（FIX-LOG §2）；
  2. 构建确定性：冻结 run3==run4 8/8，修前/修后 SVG 仅 p8 一页变化；
  3. text.md 由同一导出脚本从 SVG 确定性导出（44,361 字节与旧同）；
  4. 修前 text.md:1243 已实录为 `47. A — 首日戰勝大之里的是一之富士`，修后该行仅 `一`→`義`一字之差。
- key 47 答案正确性再验：题面问初日战胜大之里者，正文 :120 明写小结義ノ富士勝，选项 A 即 `義ノ富士`，答案 A 与 key 115（同一事件反向提问）互洽。

## 10. 8 版目视（cards/*.png，逐版看图）

| 版 | 结论 |
|---|---|
| P1 头版 | 干净，无溢出/重叠；刊头、头条、热搜榜、目录、快讯、图注齐全 |
| P2 生活 | 干净；词卡 4 条皆 1 行；练习 11–28 齐全 |
| P3 文化 | 干净；配图+出处完整；练习 29–46 齐全 |
| P4 体育 | 干净；Q47 题面选项 `A. 義ノ富士` 正确；栏顶 `5) でお知らせします。` 为核心冻结跨栏续接（EDITION-RECORD 已记，非 fan-out 缺陷） |
| P5 青年 | 干净；流行语 30 条、红叶图、练习 65–82 齐全 |
| P6 深读 | 干净；图表 38/24/22/16 合计 100%；P6 正文末句 `紅葉を見に行く人は、予報の日付と` 为跨栏断句，续句 `今の様子を、両方確かめましょう。…` 在次栏顶（text.md:763–766、print PDF P6 已核），非截断 |
| P7 精讲 | 干净；teaser 未压页脚；披露 3 行繁体；金句 (N面) 引用与读者园地、下期预告齐全 |
| P8 答案 | **重点复核**：答案区 47 题正印 `首日戰勝大之里的是義之富士`；115 题 `大之里首日輸給了義之富士`；E 组 137–140 无误；范文 H 区 154 字；答案末行未侵页脚；页脚 `Lucerna　日語週報 VOL.4　正文日語　講解繁體中文`、`第 8 版 / 共 8 版` 清晰 |

**8 版目视结论：零问题。**

## 11. 待第一轮复校（不由本 builder 做）

- 本修补只做机械门 + 150 键复核 + 目视；第一轮全量复校（目标语精读、讲解层对照、事实日期复核）由协调员另派。
- 遗留观察（非缺陷，供复校员参考，不动）：
  - map 另有 2 条家具键（`Lucerna　日语周报 VOL.4　LUCERNA JAPANESE WEEKLY`、`译注｜`）在 5 个 core 内容文件里带引号未出现——改动前已存在，与本次修复无关，见 FIX-LOG §2(b)。
