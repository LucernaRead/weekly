# GATE-LOG — 2026-W47 ja-it, fix-1 机械门全套（2026-11-11）

构建解释器一律 `tools/venv/bin/python`（Python 3.12.3）。门禁文件在本目录；对照基线为修前 stick-8 实测（`hidden_files/w47/scratch-fanout-ja/it-*.json`）。

## 1. 整期重渲染

| 步骤 | 结果 | 日志 |
|---|---|---|
| `run.py` runA | rc 0；FLOW OVERFLOW / HEAD TOO WIDE 0；登记 150（A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；范文 154 字） | `build-fix1-runA.log` |
| `run.py` runB（freeze 同解释器） | rc 0；0 溢出 | `build-fix1-runB.log` |
| freeze：runA vs runB SVG sha256 | **8/8 相同** | `sha-runA.txt` / `sha-runB.txt` |
| 修前 vs 修后 SVG diff | 仅 `p8-tesuto.svg` 变化 | `pre-sha.txt` 对照 |
| `render.py`（单次） | rc 0；print PDF 29,099,163 B | `render-fix1.log` |
| `webpdf.py` | 首次 rc=120（见 FIX-LOG §3 配额事故）；隔离 TMPDIR 重跑 rc 0；web PDF 4,476,985 B，47,002 text bytes | `webpdf-fix1.log` |
| `export-textmd-it.py` | text.md 46,678 B / 1378 行；修前验证逐字节相同 | — |

## 2. 全套机械门

| 门 | 工具/方法 | 结果 | 文件 |
|---|---|---|---|
| Occlusion | `tools/occlusion_audit.py <edition-dir>` | selftest OK（6 类全触发，干净对照静默）；**0 flags** | `it-occlusion-fix1.json`、`occlusion-fix1.log` |
| P8 extract | `tools/p8.py extract --p8 svg/p8-tesuto.svg --total 150` | **150/150**（parse: lines）；keys 与修前提取逐字节相同 | `it-p8-fix1.json`、`p8extract-fix1.log` |
| P8 compare | `tools/p8.py compare --core-p8 production/2026-w47/core-ja/svg/p8-tesuto.svg --edition-p8 … --total 150` | **CLEAN**；missing=[] extra_count=0 uncertain=[]；keydiff **恰为 [137, 138, 139, 140]** | `it-p8compare-fix1.json`、`p8compare-fix1.log` |
| 文字层双版一致 | `pdftotext` print 与 web 分别提取后 `cmp` | **逐字节一致**，各 47,002 B | `print.txt` / `web.txt` |
| P8 最小字号 | PyMuPDF（tools venv）取 P8 全部 span | **9.975pt**（167 spans）≥ 9.75pt；次档 10.35pt（79 spans，题干冻结值）；与修前相同 | —（见 FIX-LOG 与本表） |
| U+2019 全扫 | `.py` + 8 SVG + text.md + KIT 逐字符计数 | **U+2019 0**（U+0027 共 104 处，均为正常撇号） | — |
| §1.1 grep | 8 SVG | 纸 `#fbfaf6` 1×/页（共 8×）；旧 `#f7f1e2` 0×；`·` 0×；`Pagina N di 8` 1×/页；刊头 196px 1×（P1）；徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f | — |
| 流量位置 | runA log | P8-ex 流止 y=561（底 1252）；P8-keys 流止 y=2442（底 2540，98px 余量）；P7 teaser 止 2528.1（页脚 2580，52px 余量）；与修前相同 | `build-fix1-runA.log` |

## 3. 150 键逐题复核（新版 text.md P8 答案区全读，`p8-section-new.txt`）

- 编号 1–150 连续无缺重；分版 1–10 / 11–28 / 29–46 / 47–64 / 65–82 / 83–100 / 101–112 / 113–150。
- 答案键与修前 `p8.py` 提取逐字节相同（键未动）；E 组 137–140 意大利文译键未变。
- 6 处改动逐项对题干验算：
  - 48（B）：题干「初日に豊昇龍に敗れたのはだれですか。A. 義ノ富士 B. 美ノ海 C. 宇良」→ B 美ノ海 = Chura-no-umi ✓；注「Chura-no-umi ha perso contro Hōshōryū il giorno 1」✓
  - 49（A）：题干「3日目に豊昇龍に勝ったのはだれですか。A. 藤凌駕 B. 大の里 C. 霧島」→ A 藤凌駕 = Fujiryōga ✓
  - 54（11）：题干「藤凌駕の金星は、初土俵から ___ 場所目」→ 11 ✓（公开来源：初金星为初土俵后第 11 场所）
  - 63（○）：题干「藤凌駕は、3日目に金星をあげました」→ ○ ✓
  - 111（11）：与 54 同注 ✓
  - 116（A）：P8 cloze 题干「豊昇龍は3日目、藤凌駕に（___）ました。(A. 負け B. 勝ち)」→ A 負け；注「Hōshōryū ha perso contro Fujiryōga il giorno 3」✓
- 其余人名罗马字逐项复核：Ōnosato、Hōshōryū、Yoshinofuji、Shōsetsu、Miura Riku、Kihara Ryuichi、Miyajima、ryuuryuu、Chiikawa 全对。
- 图表算术：38−24=14（91）、38+24=62（92）、38+24+22+16=100（93）均对。
- 全文新旧 diff = 恰好 6 行（text.md 1263/1264、1269、1278、1332、1338 行）。

## 4. 8 版目视（cards PNG，重点 P8 答案区；另 web PDF P8 渲染对照）

- P1：无溢出/重叠/压页脚；头条、热搜榜、目录、快讯、图片与图注齐全。
- P2 / P3 / P5 / P6 / P7：无溢出/重叠/压页脚；P6 图表柱长与 38/24/22/16 成比例，练习数据标注在位；P7 诊所/框架/披露/预告齐全，teaser 在页脚之上收束。P2/P3/P5/P6/P7 中部空白带与 P4 `(VOL.` 跨栏为继承自已定稿核心版的外观（第一轮 O5），本版内无动作；且修后 P1–P7 SVG 与修前逐字节相同。
- P8：答案区 6 处新拼写均已印出（48 Chura-no-umi；49/54/63/111/116 Fujiryōga），无溢出、无重叠、末行在页脚之上；图片（Arashiyama 寺）与图注/出处齐全；web PDF 渲染的 P8 与 print 卡逐项一致。
- 无 tofu；无新缺陷发现。

## 5. 结论

- 全套机械门全绿；150 键复核全对；8 版目视无缺陷。
- 改动面 = 6 个注文串 + 随之重建的 P8 SVG/PDF/text.md；其余 7 个 SVG 逐字节未变。
- 第一轮 (a) 作废；须第二轮全量复校（协调员派），零问题才算定稿。
