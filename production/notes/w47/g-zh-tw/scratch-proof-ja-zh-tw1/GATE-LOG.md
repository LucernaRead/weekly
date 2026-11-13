# GATE-LOG — 2026-W47 ja × zh-tw 第一轮独立复校（proof1）

- 版：`2026-w47-ja-zh-tw`，VOL.4，刊期 2026-11-16–22；构建解释器：`tools/venv/bin/python`（与构建相同）
- 证据目录：本目录（`hidden_files/w47/scratch-proof-ja-zh-tw1/`）。fix1 证据在 `../scratch-ja-zh-tw-fix1/`（仅参考，未采信其结论）。
- 结论速览：**fix1 回归全过；机械门全过（freeze diff --strict-cjk 的 rc=1 已逐字裁定为误报，见 §3）；
  但全量复校发现 1 个缺陷类 2 处（minor），故本轮结论为 (b) 有缺陷，详见 PROOF-NOTE.md §2。**

## 1. 成品核对

| 交付物 | 字节 | SHA-256 | 与任务值 |
|---|---|---|---|
| Print PDF `Lucerna-VOL4-JA-ZH-TW.pdf` | 26,034,685 | `7f05fd508c90cb0dc7b5be2d3bcc06f01f0c04e4cf399ed6e4076b7fecedb27b` | 一致 |
| Web PDF `Lucerna-VOL4-JA-ZH-TW-web.pdf` | 4,788,782 | `cee0a8b5b373c14b21a467f4a477495e2a59c125095c8b051dbae33b45afa93e` | 一致 |
| `.text.md` `2026-w47-ja-zh-tw.text.md` | 44,361（1352 行） | `3a42eb5b35c98b9b4245ae03eab971c6a0d076bcae66670379027a943478621c` | 一致 |

两 PDF 均为 8 页；`pdftotext` 文字层各 44,661 字节，`cmp` 逐字节一致。

## 2. 构建门（自跑）

| 门 | 证据 | 结果 |
|---|---|---|
| `freeze.py baseline`（--build 版目录 --core-svg 版 svg --out 本目录/freeze-proof1） | `freeze-baseline-proof1.log` | rc=0，**8/8 SVGs byte-identical**（p1 `12de5b88…`、p2 `adaa7b0f…`、p3 `5daac4ba…`、p4 `f89230a5…`、p5 `d742795a…`、p6 `f296e44d…`、p7 `f7494c3f…`、p8 `f0d2ebe5…`，与 fix1 修复后 p8 sha 一致）；core integrity：发货 SVG 跑后重 hash 未变 |
| 自跑 `run.py`（freeze 副本内重跑，同一解释器） | `run-proof1.log` | rc=0，TOTAL **150**（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38；类型 完成句子 50 / 單選 51 / 完形單選 13 / 詞彙配對 12 / 判斷對錯 11 / 造句 8 / 翻譯 4 / 寫作 1；范文 154 字），**0 FLOW OVERFLOW / HEAD TOO WIDE**；重建 8 SVG 与发货 SVG sha256 逐字节一致（`diff` 无输出） |
| P8 最小字号（PyMuPDF，print PDF） | 本日志 §6 | P8 共 371 spans，最小 **9.975pt**，无 <9.75pt |

## 3. freeze diff（core-ja vs 本版，--strict-cjk）—— rc=1，已裁定为误报

- 命令：`freeze.py diff --core-svg production/2026-w47/core-ja/svg --edition-svg <本版>/svg --strict-cjk`
- 结果：`STRICT-CJK FAIL`，TOTAL added CJK 884 字；逐页 added/removed 串数：p1 19/19、p2 18/18、p3 12/12、p4 12/12、p5 15/15、p6 12/12、p7 33/37、p8 165/165。
- 裁定方法：OpenCC s2t 作用于 removed 串多重集，与 added 串多重集逐页比对（脚本 `/tmp/proof-cjk-adjudicate.py`，输出 `/tmp/proof-cjk-adjudicate.txt`）。
  全部残差均为下列三类，无一新增日文正文：
  1. 家具改写（KIT §1）：页脚 `LUCERNA JAPANESE WEEKLY` → `正文日語 講解繁體中文`；
     页行 `第N版／共8版` → `第 N 版 / 共 8 版`；`詳見第 4 版` / `答案見第 8 版` / `見第 2 版` 加空格；
     P8 分隔 `— 第N面 —` → `— 第 N 版 —`；P8 表头 `帶 ✓ 的爲範文題` → `帶 ✓ 的為範文題`（`爲`→`為`，KIT F0 台湾标准）；
     P1 趋势行删 `，非精確統計`。
  2. 日文 headword 原形修复（KIT §1/F0）：`この號の內容`→`この号の内容`、`屋臺`→`屋台`、`前號`→`前号`、
     `寫真`→`写真`、`淺草`→`浅草`、`大之裏`→`大之里`、`兩位橫綱…詳見第4版` 间距。
  3. P7 披露改写（KIT §2 既定 3 行繁体披露）与页码引用 `(第N面)` → `(N面)`（KIT F5）。
- 注意：本 diff 的“core”是 core-ja  shipped SVG，其讲解层为简体中文（页脚 `日语周报`），故 core→本版实为简→繁讲解层转换；
  s2t 下每字繁简异形均计新增 CJK，--strict-cjk 在此配对上必然 rc=1。结论：误报实质，非缺陷。
  （同类先例：ja-it proof1 的 freeze diff 亦 exit 1，净增 15 字逐字裁定为误报。）
- 另：本裁定不覆盖 PROOF-NOTE §2 的 D1/D2——s2t 对 `出来栄え`/`波乱` 的误转与 removed 串逐字相同，
  故 diff 视之为对等转换；D1/D2 由人工逐字扫查检出，与 diff 无关。

## 4. 几何遮挡审计（tools/occlusion_audit.py）

- `occlusion-proof1.log` + `occlusion-proof1.json`：自检 OK（6 类阳性对照 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1 触发，干净对照静默），实审 **`svg: 0 flags`**，rc=0。

## 5. P8 门（tools/p8.py）

- extract：`p8-extract-proof1.json` + `p8extract-proof1.log`——**noted set = 150 of 150**，题号 1–150 连续无缺重，rc=0。
- compare（vs core-ja `svg/p8-tesuto.svg`）：`p8compare-proof1.json` + `p8compare-proof1.log`——**CLEAN**，
  `missing=[] extra_count=0 uncertain=[]`，**keydiff=[139, 140]**，rc=0。
  keydiff [139, 140] 为本版预期值（KIT §11 F3）：137/138 与核心逐字节相同，故不进入 keydiff；已复核 137 `二之酉在11月19日。 — 對照第2版`、
  138 `新酒在11月19日解禁。 — 對照第3版`、139、140 全与 text.md 一致。

## 6. 文字层与回归门

- `pdftotext` print / web 各 **44,661 字节**，`cmp` **逐字节一致**；两版 8 页均有文字层。
- `一之富士`：content*.py 0、text.md 0、svg/*.svg 0、print 文字层 0、web 文字层 0（grep -o 逐文件计数）。
- `義之富士`：content34.py 1、content8.py 1、text.md 2、svg/p8 2、print 文字层 2、web 文字层 2；源码+text.md+SVG 合计 **6×**（与任务预期一致）。
- map-zh-tw.json：221 条；`一之富士` 0 条；`義之富士` 值 2 条，键均为现行核心简体 `义之富士`。
- key 47/115 同人：日文正文 `義ノ富士`（core content34.py:120/187/189、content8.py:21）与本版一致；外部核实见 PROOF-NOTE §4。
- U+2019（’）：text.md + content*.py + 8 SVG 全扫 **0**。
- VOL：页脚 `日語週報 VOL.4` 8×；刊头 VOL.4；VOL.3 仅 `前号（VOL.3）`、VOL.5 仅 `次号（VOL.5）`/披露/下期預告。
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×，`參考答案` 1× / `参考答案` 0×，`吉伊卡哇` 4×，`售`×5/`呢`×3 为简繁同形字（KIT §11 F4 已裁定）。
- P8 最小字号：PyMuPDF 取 print PDF P8 全部 371 spans，最小 **9.975pt**（key 1 行），次档 10.35pt；无 <9.75pt。

## 7. 150 键复核（text.md P8 答案区 vs P8 SVG 提取值）

- text.md P8 答案行 150 条，题号 1–150 连续、无缺重；与 `p8-extract-proof1.json` 的 keys 逐值比对：
  实质差异 **0 条**。唯一形式差异：key 150（text.md `✓ 範文見本版 H 區（154 字）` vs extract 仅取 `✓` 标记；SVG 原文含全句，P8 卡片已目视确认）。
- key 47 `A — 首日戰勝大之里的是義之富士`、key 115 `A — 大之里首日輸給了義之富士` 与 SVG 提取值一致。
- 范文字数：范文正文实数 **154 字**，与登记一致。

## 8. 8 版目视（cards/*.png，逐版看图）

| 版 | 结论 |
|---|---|
| P1 头版 | 干净，无溢出/重叠；刊头、头条、热搜榜、目录、快讯、图注（Poliphilo CC0）齐全 |
| P2 生活 | 干净；词卡 4 条、练习 11–28 齐全；中栏下半留白为版式（O6） |
| P3 文化 | 练习 29–46、配图+出处齐全；惟缺陷 **D1**（注文 `出來栄え`，PROOF-NOTE §2） |
| P4 体育 | 练习 47–64、星取表齐全；栏顶 `5) でお知らせします。` 为核心冻结跨栏续接（O3）；惟缺陷 **D2**（注文 `波亂`，PROOF-NOTE §2） |
| P5 青年 | 干净；流行语 30 条、红叶图（lumoplank CC0）、练习 65–82 齐全 |
| P6 深读 | 干净；图表 38/24/22/16 合计 100%，已标練習用數據；练习 83–100 齐全 |
| P7 精讲 | 干净；金句 8 条逐字出自本期文章；披露 3 行繁体；下期預告齐全；teaser 未压页脚 |
| P8 答案 | 答案区 150 条齐全，key 47 印 `首日戰勝大之里的是義之富士`、key 115 印 `大之里首日輸給了義之富士`；E 组 137–140 无误；范文 H 区 154 字 + 天龍寺图；答案末行未侵页脚 |

## 9. 缺陷与观察（汇总；详见 PROOF-NOTE.md）

- 缺陷（minor，1 类 2 处）：D1 P3 注文 `出來栄え` 应为 `出来栄え`（content34.py:20）；D2 P4 注文 `波亂` 应为 `波乱`（content34.py:124）。
  同源：map-zh-tw.json 两词条值亦含错字，须与版源码同步改（与 fix1 同模式），重建后重验。
- 观察（不计缺陷）：O1 key 80 `三浦璃來`（中文释义句内人名繁体写法，KIT 专名规则未覆盖）；O2 嵐山 23 日/26 日/13 日三数各有出处；
  O3 跨栏断句（核心冻结）；O4 fix1 GATE-LOG 行数笔误（1325 vs 实测 1352）；O5 text.md 裸级别行 147 vs 150 道（多键共用级别行）；
  O6 中栏留白；O7 `千秋樂`（KIT 已认可）、`長國寺`（正式写法）均无误。
