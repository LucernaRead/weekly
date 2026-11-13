# FIX-LOG — 2026-W47 core-it D-2 fix（P7 未来时规则性标签互换）

- 修理工：core-it fix 员（subagent）
- 日期：2026-11-11
- 对象：`~/workspace/weekly-git/production/2026-w47/core-it/`
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-it-d2/`
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0（`probe.txt`）；scratch 真实写文件通过；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。解释器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，见 freeze.log 首行）。
- SOP：已读 `~/workspace/weekly-git/SOP.md` §8（校对闭环）、§1.1（视觉规范）全文 + core-it `WEEKLY-KIT.md` 全文 + `~/workspace/weekly-git/AGENTS.md`。

## 0. 定稿三件（2026-11-11）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4.pdf` | 27,726,330 B | `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d` |
| 网页 PDF `La-Lucerna-VOL4-web.pdf` | 1,790,596 B | `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef` |
| 文本导出 `2026-w47-it-zh-cn.text.md` | 52,655 B，1317 行（文件行数），150 题 | `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed` |

改前（fix3 定稿）对照：印刷 `2ee50d92635ba496d65c09c085a9b70fbebad62a8d6f3b81c41afec4be47a412`（27,726,350 B）/ 网页 `ab14a5b7bbf532e0633fee0006f5c19f44bc558b9ad475ad523d5bd0aaaecab0`（1,790,620 B）/ 文本 `d0c573b83fa679262c2da0734b08b1f504782829c11d29c9ed1e2c8cac08dbcb`（52,676 B）。字节差：印 −20 B / 网 −24 B / 文本 −21 B——与删去的 `andare → andrò, `（14 字符 + 断行重排）及 `irregolare`→`regolare`（等长）一致；文本导出行数 1317 不变（`wc -l`），export 脚本打印的 1318 是 `len(out_lines)`（含末尾一个被 `.strip()` 去掉的空项），与改前一致，不是本次改动引入的差异。
SVG 变化：仅 P7 `3746030a…` → `a7e6afa4…`；P1–P6、P8 SVG 与改前字节一致；8 张 cards 仅 p7 不同（同名文件逐一 sha256 比对，见 §5）。

## 1. 缺陷 D-2 — P7 A2 未来时讲解把 andare 与 leggere 的规则性说反了（core 级，教学事实错误）

### 1.1 改前原文（`content7.py:17/18`，改前已在盘上核实）

- L17：`Le forme sono regolari: andare → andrò, assaggiare → assaggerò, guardare → guarderò.`——错：andare 未来时**不规则**。规则形应为 *anderò*；实际 andrò 是元音脱落型不规则词干 andr-。
- L18：`Il verbo è leggere, irregolare al futuro: leggerò.`——错：leggere 未来时**规则**（leggerò 恰为规则构形：不定式去尾 -e + -ò）。leggere 的不规则处只在远过去时 io lessi 与过去分词 letto，不在未来时。
- 两处标签正好互换。动词形式本身拼写全对（andrò / assaggerò / guarderò / leggerò / andremo 均正确），只有规则性标签错。

### 1.2 公开依据（协调员已检索核实；本轮复核引述，不重复检索）

- LibreTexts《Indicativo futuro》不规则未来时词干表明确列 andare → andr-（https://human.libretexts.org/Bookshelves/Languages/Italian/D'accordo_-_Intermediate_Italian_(Blum_and_Gemmani)/02%3A_Grammatica_II-_accordo_del_verbo/2.08%3A_Indicativo_futuro），并以 leggere 作规则 -ere 动词例（io leggerò）。
- FluentU、Cyber Italian、FlexiClasses 均列 andare → andrò 为不规则未来时。

### 1.3 修复（源字符串，`content7.py:17/18`，只动这两行）

| 行 | 改前 | 改后 |
|---|---|---|
| 17 | `…Le forme sono regolari: andare → andrò, assaggiare → assaggerò, guardare → guarderò.` | `…Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`（删去 `andare → andrò, `） |
| 18 | `Il verbo è leggere, irregolare al futuro: leggerò.` | `Il verbo è leggere, regolare al futuro: leggerò.`（`irregolare` → `regolare`，等长） |

约束核对（任务指定 3 条，逐项实测）：
1. 指涉不悬空：L17 句首仍提 andremo/assaggeremo/guarderemo（第一句一字未动）；L18 前句仍提 `leggeremo a BookCity`（同句前半未动）。桥接句 `用将来时说计划：andremo、assaggeremo、guarderemo、leggeremo。`未动。
2. 动词形式拼写不动：改后 L17 仍含 assaggerò / guarderò，L18 仍含 leggerò；andremo / assaggeremo / guarderemo / leggeremo 均在原位。`andrò` 一词随被删的 andare 例一并消失——这是定稿最小改法的既定内容（L17 不再举 andare 为规则例），不是拼写改动。
3. 只动这两行：`git status` + 全文件 grep 核实见 §5；其余 `content*.py` 行一字未动（P1–P6/P8 SVG 与改前字节一致为旁证）。

### 1.4 习题影响：零

- Q101–103 键 andremo / assaggeremo / guarderemo、Q104 键 B：改前/改后 p8 extract 键逐题比对全等（`p8-pref.json` vs `p8-post.json`：noted 集相等、全部键相等；Q101 `andremo`、Q102 `assaggeremo`、Q103 `guarderemo`、Q104 `B` 改前改后一致）。
- Q104 键注 `leggerò 是 leggere 的将来时`无规则性断言，未动。

### 1.5 影响面（只修核心，不碰 11 个 it 版）

同一句逐字出现在 core-it `text.md:775/:777` 及全部 10 个 it fan-out 版 `text.md:775/:777`（de/en/es/fr/ja/ko/nl/pt/ru/zh-tw 各 1 处）——共 11 版。本轮只修核心并重建核心三件；重扩散由协调员在核心复校 (a) 后另派。

## 2. 全核心重扫（修后）

- 旧错串 `Le forme sono regolari: andare`：`content*.py` 0 处（逐文件 grep -c 全 0）、8 个 SVG 0 文件、`.text.md` 0 处、印/网 PDF 文本层各 0 处。
- 旧错串 `irregolare al futuro: leggerò`：同上，全版 0 处（`irregolare al futuro` 在 SVG/文本/PDF 文本层亦 0 处）。
- 新串各就其位：`Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` 在 `content7.py:17`、p7 SVG、`.text.md:775`、印/网 PDF 文本层各 1 处；`regolare al futuro: leggerò` 在 `content7.py:18`、p7 SVG、`.text.md:777`、印/网 PDF 文本层各 1 处。
- `regolar` 在全核心 `content*.py` 中仅出现在这两行（`grep -n regolar content*.py` = 2 行，均为修复后文本）——协调员盘核“无其他同类错误断言”复核成立。

## 3. 构建方式（方法说明：生产 run.py/render.py 未直接跑）

生产 `content*.py` 的 `OUT` 与 `render.py` 的 `BASE` 是硬编码生产绝对路径（`content12.py:6` 等），按任务要求不直接跑。做法：
1. 把 core-it 构建源（`bslib4.py`、`svglib.py`、`content*.py`、`run.py`、`render.py`、`assets/`）整份拷到 `<scratch>/build/`；
2. 拷本中的 5 处 `OUT` 与 `render.py` 的 `BASE` 用 sed 改指 `<scratch>/build/svg` / `<scratch>/build`（改后逐行 grep 核对，见 `build/` 内文件）；
3. 在拷本里跑 `run.py` → `render.py` → `tools/webpdf.py` → 重指 bdir 的 export 脚本拷本（`export_it.py`，bdir → `<scratch>/build`）；
4. 全部门禁先在 scratch 产物上跑过，确认无误后，才把 5 个文件拷回生产目录：`svg/p7-lingua.svg`、`cards/p7-lingua.png`、`La-Lucerna-VOL4.pdf`、`La-Lucerna-VOL4-web.pdf`、`2026-w47-it-zh-cn.text.md`（`content7.py` 早已在生产目录改好；其余生产文件未动）。
5. 回拷后在生产目录上重跑全部门禁（freeze baseline、occlusion、p8、validate、文本层比对、旧串重扫），结果见 §4 与 GATE-LOG.md。

## 4. 门禁全表（最终构建；详见 GATE-LOG.md）

| 门禁 | 结果 | 日志 |
|---|---|---|
| 构建（scratch run.py + render.py + webpdf + export） | rc=0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；范文 99 词；P7-a2 flow 末端 y=1124（改前 1157，短一行，底 1560），P7 col3 末端 1644.0 不变 | build.log、render.log、webpdf.log、export.log |
| freeze baseline（生产目录，`--core-svg` 指 core-it 自身 `svg/`） | **8/8 字节一致**——比的是 freeze 的 build-copy（从修复后源码重建）与已发核心 SVG：P7 `a7e6afa4…` 精确复现，其余 7 页与改前字节一致；发运核心 SVG 在运行前后重哈希无变化 | freeze.log |
| occlusion audit（selftest 先过） | selftest OK（6 类阳性全触发、干净对照沉默）；生产 8 页 **0 flags** | occlusion-selftest.log、occlusion-prod.log/.json |
| p8 extract + 三源 keycheck | noted 150/150；新旧 P8 compare CLEAN（keydiff=[]）；印刷键 vs 文本导出 150/150（0 差异）；Q101–104 不变 | p8-pref/-new/-post.log/.json、p8-compare.log/.json |
| 印/网 text layer | `pdftotext` 字节相同（各 43,979 B，5,948 词），`cmp` rc=0；相对改前 −22 B，恰为删去的 `andare → andrò, ` 文本 | print-prod.txt、web-prod.txt、print-plain.txt、web-plain.txt |
| 文本导出校验 | forward-miss 0 / reverse-miss 0；与改前文本导出的 diff 恰为 775/777 两行 | validate.log、validate-prod.log |
| 横向漫出（PIL 全 8 页 + 200 dpi 渲染全 8 页） | PIL：无行越过页面边距（仅两条家具线恰止于 1862.0 px，改前已有）；P7 在 200 dpi 渲染扫描中无越边距墨迹；P2 +0.7 pt、P5 +0.7 pt、P8 +1.0 pt 痕迹与 fix3 §7/§8 的改前值完全相同，非本次引入 | h-scan.txt、render-scan.txt |
| 目视裁图（200 dpi） | P7 A2 栏两句修复句在版、干净，无溢出/重叠；桥接句与习题区 intact | crop-p7-a2.png、p7-full-half.png |
| P8 最小字号 | P8 SVG 与改前字节一致，9.75 pt 下限不受影响（KIT §8 原值保留，未重测） | — |

## 5. 改动面核对（生产目录）

- 改动文件（生产目录共 7 个）：`content7.py`（L17/L18 两行）、`svg/p7-lingua.svg`、`cards/p7-lingua.png`、`La-Lucerna-VOL4.pdf`、`La-Lucerna-VOL4-web.pdf`、`2026-w47-it-zh-cn.text.md`、`WEEKLY-KIT.md`（§6）。
- 未动旁证：P1–P6/P8 SVG sha256 与改前（`svg-sha-pre.txt`）逐一比对全同；7 张 cards 逐一 sha256 比对全同（仅 p7 不同）。
- `git status --porcelain production/2026-w47/core-it/`：仅 `2026-w47-it-zh-cn.text.md` 显示 M，其余为该克隆下本就未跟踪的文件（与本轮无关）；**未 commit、未 push**（按任务要求）。

## 6. KIT 更新

- `WEEKLY-KIT.md` §7：新增条目 18（D-2，含新旧三 SHA + 修前/修后 + 候选记录：改法即任务建议的最小改法；等效候选“L18 改举 andare 为不规则例”未采纳——L18 前句已提 leggeremo a BookCity，改举 andare 会让指涉悬空，且改动面更大）。
- §8：印刷/网页 PDF 尺寸与 pdftotext 字节更新为新值（27,726,330 B / 1,790,596 B / 43,979 B）；新增 D-2 fix-round 自检段落。
- §9：三件尺寸更新；构建日志索引加 `hidden_files/w47/scratch-fix-core-it-d2/`。
- 其余旧值一字未动（旧三 SHA 只保留在 §7 条目 18 的历史行）。

## 7. 方法备注（不修工具，只记录）

- `tools/freeze.py diff` 只做 CJK 会计、纯拉丁改动不可见；`tools/p8.py compare` 只比键——两个门禁都不能发现 frozen 意大利语文本漂移（fix3 §6 已记，本轮复现：本次两处改动若只跑 diff/compare 均不可见，靠的是全核心旧串重扫 + 文本导出 diff + freeze baseline 的 SVG 字节比对）。
- 200 dpi 渲染扫描的 P2/P5/P8 亚 1 pt 痕迹与 fix3 实测值完全相同，属管线系统性特征（PIL 度量与渲染器 advance 差约 0.5–0.8%），本次不修。
- 渲染扫描脚本 `scan_render.py` 复用 fix1 的拷本（只改指了 PDF 路径）；`scan_h.py` / `scan_common.py` 同样复用（`scan_common` 仍从生产 core-it 只读 import `svglib` 度量，属 builder 一致度量）。

## 8. 给协调员的重 fan-out 清单

- 11 个 it 母语版（de/en/es/fr/ja/ko/nl/pt/ru/zh-tw）须从本定稿 core 重 fan-out，带上 D-2 定稿措辞（`text.md:775/:777` 两句）；本轮只修了核心，未碰任何版。
- 核心复校 (a) 通过后即可重扩散；重校时覆盖：L17 规则例只剩 assaggiare/guardare、L18 leggere 为 regolare。
- 本轮未发现其他同类错误（全核心 `regolar` 仅两行）；P7 其余内容未动。
