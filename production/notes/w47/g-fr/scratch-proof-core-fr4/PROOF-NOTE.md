# W47 core-fr 复校笔记（fix4 后独立复校，proof4）

- 复校员：proof4（独立于 fix4 agent 903d964e）
- 日期：2026-11-11
- 对象：`~/workspace/weekly-git/production/2026-w47/core-fr/`（fix4 后）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-fr4/`
- 探针：`/dev/null` 存在；`git hash-object -w` 通；工作区真实写文件成功。开工前、收尾各测一次 SHA，均未变。

## 结论：(a) 定稿零缺陷

fix4 两处改动逐项独立重验全部通过；全部门禁独立重跑全部通过；150 题题干/答案/键注三源逐题核对 0 不符；8 页对 fix3 build-copy 零位移（除两处改动本身）。

## 一、开工 / 收尾 SHA 复核（两次一致，未变）

| 件 | 尺寸 | SHA-256 |
|---|---|---|
| 印 `La-Lucerna-VOL4.pdf` | 30,446,975 B | `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d` |
| 网 `La-Lucerna-VOL4-web.pdf` | 2,241,835 B | `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141` |
| 文 `2026-w47-fr-zh-cn.text.md` | 46,471 B | `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df` |

三件均与任务书给定值逐字节一致；复校期间（run.py / freeze / verify 三次全量重跑）未改动任何一件。

fix3→fix4 哈希变化亦独立核对（`scratch-fr-fix3/freeze-fix3.json` 对照）：仅 P4 `37cf3412c3f8`→`7e46e630eb6b`、P8 `ce072a017cd4`→`5bee4d4473bf`，其余 6 页与 fix3 字节相同。

## 二、fix4 改动 1：Q148（`content8.py:170 / :176`）

- `:170` 键确为 `("A2", "devant le", E["n_g4"])`；`:176` 题干确为 `On se retrouve ({gnums[3]})___ cinéma ?`（“du”已删）。
- 映射核实：`dlg_defs` 顺序 `des billets / deux / quelle heure / devant le / film` = Q145–149，`gnums[3]` 即 Q148；新鲜重跑的 REG 第 148 条 `key='devant le'，type='对话补全'，page=8`。
- 填入后 `On se retrouve devant le cinéma ?` 通顺（在……门口见面）。
- 三源一致：源码 / `.text.md` 第 1039 行题干 `On se retrouve (148)___ cinéma ?` 与第 1083 行附录 `148. devant le（电影院门口）` / P8 SVG 对白节点 `(148)___ cinéma ?` 与答案节点 `148. devant le（电影院门口）`。
- 旧措辞 `devant du cinéma` / `___ du cinéma ?` 全刊 0 处（源码、`.text.md`、8 页 SVG 全扫）。

## 三、fix4 改动 2：P4 孤儿句号（`expl.py:123`）

- `:123` 确为 `"chiffres_note": "大师赛结果与都灵名单见本版正文。"`，“决赛”已删。
- P4 SVG 该句为单个 `<text>` 元素（x=1461.5, y=520，Noto Serif CJK SC 21.5px），实测宽 344.0px < 栏宽 378.5px（旧串 387.0px）；旧注记 0 处；`.text.md` 第 515 行同句。
- 全版孤儿标点 sweep（独行 。/，/、/：/；/！/？/./:/–/闭引号 »/”/’/）/）：8 页合计 **0**。
- P4 其余内容对 fix3 build-copy **零位移**：8 页逐项 `(x, y, 文本)` 集合比对——P1/P2/P3/P5/P6/P7 0 改动；P4 旧 215 行 → 新 214 行，仅去 2 行（注记旧行 y=520、独行 `。` y=550.53）、入 1 行（单行注记，同 y=520）；P8 323 行 → 323 行，仅 4 行换（对白行 y=1353.68、答案区 3 行 y=1976.25/1996.4/2016.55，坐标不变，仅因 `devant le` 长 3 字使答案区折行点后移一字）。

## 四、全部门禁（独立重跑，不沿用 fix4 结论）

| 门禁 | 结果 | 产物 |
|---|---|---|
| `run.py` | rc=0，零警告/溢出；TOTAL 150（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42） | `run-proof4.log` |
| `freeze.py baseline` | rc=0，**8/8** 字节相同；核心 SVG 跑后重哈希未变 | `freeze-proof4.json`、`freeze-proof4.log`、`freeze-proof4/build-copy/svg/`（已删其中冗余 PDF/卡片/素材复本，只留产出 SVG） |
| `occlusion_audit.py` | rc=0，**0 flags**；自检 6 类阳性对照全触发、干净对照静默 | `occlusion-proof4.log` |
| `p8.py extract` | rc=0，注记集 **121/150**（joined 解析） | `p8-extract-proof4.json`、`p8-extract-proof4.log` |
| `p8.py compare`（本次独立重跑并留存逐字 JSON，fix4 未留） | rc=0，**CLEAN**（121/121，missing=[]、extra=0、uncertain=[]、keydiff=[]） | `p8-compare-proof4.json`、`p8-compare-proof4.log` |
| `check_mcq.py` | rc=0，45 题体、1,448 渲染行，**0 缺陷、0 未定位** | `check-mcq-proof4.log` |
| 印/网文字层 | `pdftotext -layout` 各 102,978 字节，**逐字节一致**（`cmp` 通过） | `print-proof4.txt`、`web-proof4.txt` |
| 网 PDF | 2,241,835 B < 7 MB；8 页；含 `LucernaNewsreader-Bold` 与 `LucernaNewsreader-Italic` 子集（均已嵌入+子集化），与 fix4 所述 +36,086 B 原因一致；P4/P8 渲染目视无豆腐块、无字体缺失 | `web-p4-proof4-4.png`、`web-p8-proof4-8.png`、`pdffonts` 见 §六 |
| P8 最小字号 | 469 个 span，最小 **11.62pt**（214 个 span 处此字号），≥ 9.75pt 下限 | `verify-proof4.log` §I |
| creambox | #f0eee5 框内文本按生产字体计量，**0 违规** | `verify-proof4.log` §H |
| 150 题逐题手验 | 键四源（新鲜 REG / `final-fr-p8.json` / `.text.md` RÉPONSES / p8 extract）**150/150 一致**（Q150 按既定口径：REG 与 `.text.md` 均为全称 `开放题 — 要点见写作框，范文在第 8 版写作框内`，frozen/extract 截为 `开放题`）；注记三源（REG.note / `.text.md` 注 / P8 SVG 印出注，去空白比对）**121/121 一致**，29 道无注题确无印出注；题干（`.text.md` 练习体 vs REG 所在页 SVG 合并文本，含配对组词+释义双半、完形/对白段落、翻译句、写作提示）**150/150 在位** | `verify-proof4.py`、`verify-proof4.log`（42 项 PASS，0 FAIL） |
| 金句逐字 | P7 8 条金句对 P1–P6 正文 **8/8 VERBATIM** | 同上 §J |
| §1.1 抽查 | 8 页纸色 #fbfaf6 全有、旧纸 #f7f1e2 0、金色 0、「·」0（SVG+`.text.md`+ABSTRACT）、`font-size="38"` 0；「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 182、`.text.md` 390，与上一轮一致 | 同上 §G |
| 徽章 | 总计 **134**（P1 10/P2 12/P3 18/P4 15/P5 14/P6 15/P7 12/P8 38；A2 50 / B1 65 / B2 19 = 150−16） | 同上 §F |

## 五、“next Sunday”冻结规则

core-fr 全部源码（`content*.py`、`expl.py`、`bslib4.py`、`svglib.py`、`render.py`、`run.py`）及 `tools/tables.py` 中 `next Sunday` 命中 **0**——本轮无适用对象，不硬套旧行号。

## 六、D5 字体（只记录数量，不判）

- 印 PDF：43 个字体对象；去重面：Newsreader16pt-Regular ×16、NotoSansCJKsc-Regular ×8、NotoSansCJKsc-Bold ×8、NotoSerifCJKsc-Regular ×7、UnifrakturMaguntia ×1、NotoSerifCJKsc-Bold ×1、Newsreader16pt-Italic ×1、DejaVuSans ×1。
- 网 PDF：43 个字体对象；去重面：LucernaNotoSansCJKSC-Regular ×8、Bold ×8、LucernaNewsreader-Regular ×8、**LucernaNewsreader-Bold ×8**、LucernaNotoSerifCJKSC-Regular ×7、LucernaUnifrakturMaguntia-Regular ×1、LucernaNotoSerifCJKSC-Bold ×1、LucernaNewsreader-Italic ×1、LucernaDejaVuSans-Regular ×1。

## 七、观察项（非缺陷，不计入结论）

1. P4/P6 各 1 处独行 `— `（P4 x=1007.0 y=623.135；P6 x=1007.0 y=653.69）：与 fix3 基线坐标逐字节相同，为基线即有的引用句折行，不在任务扫查的标点集内，本轮未动。
2. 印 PDF 无 Newsreader-Bold 实体（粗体由渲染器处理），网 PDF 有 `LucernaNewsreader-Bold` ×8 子集：两渲染器粗体解析路径不同；文字层逐字节一致、网页版 P4/P8 目视干净，无影响。
3. 复校脚本自查修正（均已修正并重跑，结论不受影响）：初版 verify 脚本的 RÉPONSES 正则漏掉末条 150（后有非答案信用行）与注记跨元素换行空格——已改分段解析 + 去空白比对；初版 P4 注记宽度误用 sans 15.5px 计 248px——已按元素真实字体（Noto Serif CJK SC 21.5px）重计 344.0px，与 fix4 实测一致。

## 八、缺陷清单

**零缺陷。**无待修项，无修复路由。

## 九、转 re-fanout #2 必查（本轮未核实，仅转述前轮留项）

- fr 各版 P7 披露框等各版遗留问题（任务书提及，本轮只审核心源，未审各版）。
- KIT §八留项：Q130、P3 Q36/Q37（fix4 记录“仍留”，本轮未复核）。
