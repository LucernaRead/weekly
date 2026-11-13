# W47 fr 核心版第四轮返修记录（fix4：Q148 法语错 + P4 孤儿句号）

- 返修 builder：叶子（与 builder、第一/二/三轮返修 builder、第一/二/三/四轮校对员均不同的人）
- 日期：2026-11-11（EST）
- 依据：任务简报（Q148 为 6 个 fr proof1 一致记录的 R1；P4 孤儿句号与 fr-ja D1–D3、nl D6/D7 同类）
- 工作目录：`~/workspace/weekly-git/production/2026-w47/core-fr/`
- 工作记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-fr4/`

## 开工核对

- 印刷版 `La-Lucerna-VOL4.pdf`：30,446,982 字节，SHA-256 `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7`（与简报一致）。
- 网页版 `La-Lucerna-VOL4-web.pdf`：2,205,749 字节，SHA-256 `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823`（与简报一致）。
- `2026-w47-fr-zh-cn.text.md`：46,477 字节，SHA-256 `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e`（与简报一致）。
- 写探针 1（`git hash-object -w`）：通过（`d32b752b02e3…`）。
- 写探针 2（真实文件写至本记录目录 `probe.txt`）：通过。
- 开工前 SVG 基线（与 fix3 一致）：p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `37cf3412c3f8`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p7 `75237d672f20`、p8 `ce072a017cd4`（前 12 位）。
- `~/workspace/weekly-git/AGENTS.md` 已读（生产源与工具规则；本次只改核心源、不提交，`tools/venv/bin/python`，无冲突）。

## 缺陷独立核实（动手前）

- Q148：源码 `content8.py:176` 对白行确为 `— On se retrouve (148)___ du cinéma ? —`（f-string 内第 4 个空，`gnums[3]`），键在 `:170` `("A2", "devant", E["n_g4"])`；注记 `expl.py:351` `n_g4 = "电影院门口"`；旧版 `.text.md` 第 1039 行题干与第 1083 行附录「148. devant（电影院门口）」同；旧版 P8 SVG 同。`"devant du cinéma"` 在核心源码中仅此一处。
- P4 孤儿句号：旧版 `svg/p4-sport.svg` 在 y=550.53 有独行 `。`（`<text>` 元素单字）；源 `expl.py:123` `chiffres_note` = `大师赛决赛结果与都灵名单见本版正文。`，经 `content34.py:168` 以 `CW - 44` = 378.5px 栏宽渲染；实测整串宽 387.0px，仅超 8.5px，`wrap()` 断为 `['大师赛决赛结果与都灵名单见本版正文', '。']`。此前该孤儿句号在 §八记为 O8 观察项（裁定不修），本轮任务书改为必修。

## 修复清单（只动两处）

- `content8.py` 第 170、176 行（Q148，唯一改动的对白源码）：
  - 键 → `("A2", "devant le", E["n_g4"])`
  - 题干 → `— On se retrouve ({gnums[3]})___ cinéma ? —`（删 "du"）
  - 对话其余 4 个空与键未动；键注「电影院门口」不变（"devant le cinéma" 仍是电影院门口）。修后源码 grep：`devant du cinéma` 0 处、`___ du cinéma ?` 0 处。
- `expl.py` 第 123 行（P4 注记，唯一改动的 expl 串）：
  - `chiffres_note` → `大师赛结果与都灵名单见本版正文。`（删「决赛」二字）
  - 删字理由：整串只超栏宽 8.5px，删 2 字后实测 344.0px，`wrap()` 单行；信息完整——框内上文已写巴黎决赛比分（`7-6(5), 7-5 : la finale de Paris`），「大师赛结果」仍指大师赛（都灵）决赛结果与名单；未动 `content34.py:168` 的栏宽（无需动）。修后源码 grep：`大师赛决赛结果` 0 处。
- 未动：其余 `.py` 源码（mtime 均为改动前）；各版目录（fr re-fanout #1 的 10 版是旧核心建的，等 re-proof (a) 后由 re-fanout #2 重建）；W43/W45/W46、其他目标语、`tools/`；`final-fr-occlusion.json`（内容不变，flag_count 0）。

## 构建命令

- `tools/venv/bin/python run.py`（`build-fix4.log`）：rc 0，零 `FLOW OVERFLOW` / `TOO WIDE` / `NOSPACE`。流终值与 fix3 完全一致（P4-main 771、P7-phrases 1718/1830、P8-battery 1428 等）；登记表仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42）。
- `tools/venv/bin/python render.py`（`render-fix4.log`）：rc 0，一次成功。cards 8/8；大报版 PDF 30,446,975 B，SHA-256 `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`，8 页 1462.5×2025pt。
- `tools/venv/bin/python tools/webpdf.py svg La-Lucerna-VOL4-web.pdf`（`webpdf-fix4.log`，rc 0）：网页版 PDF 2,241,835 B，SHA-256 `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`，8 页，webpdf 计文字 46,725 字节。文件比上一轮大 36,086 字节：本次嵌了 Newsreader-Bold（21,968 B）与 Newsreader-Italic（24,264 B）两个子集，上一轮跑 webpdf 时这两个子集被 fc-match 判定与已建字体相同而跳过；仍 < 7 MB；文字层与卡面均已核对，网页版 P4/P8 另行渲染（`web-p4-4.png` / `web-p8-8.png`）目视通过。
- `W47_BUILD_DIR=<core-fr> W47_OUT_MD=<core-fr>/2026-w47-fr-zh-cn.text.md tools/venv/bin/python hidden_files/w47/scratch-fr/export47.py`（`export-fix4.log`，rc 0）：`.text.md` 46,471 B，SHA-256 `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`，39,352 字符（上一轮 39,354，−2：注记 −2 字、题干删 "du " −3 字、键加 " le" +3 字），542 条目，150 题齐全。
- `final-fr-freeze.json`：已按本次 freeze 工具 `--json` 输出刷新（ok: 8；见下）。`final-fr-p8.json`：已刷新 Q148 一键（`devant`→`devant le`，其余 149 键与注记集不变，与本次抽出结果逐项相同）。`final-fr-occlusion.json` 内容不变（flag_count: 0）。
- 本轮偶发事件：一次 `exec` 会话在 freeze 第二次运行时中途 aborted（日志 0 字节），重跑即通（rc 0，8/8），非构建问题；无 exit 120、无 Disk quota exceeded。

## 改动范围（核查）

- 源码：仅 `content8.py`、`expl.py` 各一处（其余 `.py` mtime 均为改动前）。
- 生成物：`svg/p4-sport.svg`、`svg/p8-exercices.svg`（仅变的两页）、`cards/*.png`（8/8 重渲）、`La-Lucerna-VOL4.pdf`、`La-Lucerna-VOL4-web.pdf`、`2026-w47-fr-zh-cn.text.md`、`final-fr-freeze.json`、`final-fr-p8.json`（Q148 一键）。
- 文档：`WEEKLY-KIT.md`（首行金句注、§七门禁输出数值、§八第 7 轮记录；§八“返修后观察”中 P4 孤儿句号改为已修）。
- SVG 直接 SHA-256 比对（改前 fix3 基线 → 改后）：p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p7 `75237d672f20`——6 页字节相同；仅 p4 `37cf3412c3f8`→`7e46e630eb6b`、p8 `ce072a017cd4`→`5bee4d4473bf`。
- SVG 文本逐项比对（对 fix3 build-copy 的旧 SVG）：P4 旧 215 行 → 新 214 行，仅去 2 行（注记 17 字行 + 独行 `。`）、入 1 行（单行注记），其余 213 行坐标与内容全同，零位移；P8 旧 323 行 → 新 323 行，仅 4 行换（对白题干行同 y=1353.68、答案区 3 行同 y=1976.25/1996.4/2016.55，仅因 "devant le" 长 3 字使答案区折行点后移一字），其余 319 行全同。

## 门禁结果（2026-11-11 返修后，build-fix4）

### fix4 验证（Q148 三源一致 + P4 单行）
- Q148：源码（键 `devant le`、题干 `___ cinéma ?`，旧措辞 0 处）、`.text.md`（第 1039 行题干、第 1083 行附录「148. devant le（电影院门口）」）、P8 SVG（对白节点 `(148)___ cinéma ?`、答案节点 `148. devant le`）三源一致；填入后 `On se retrouve devant le cinéma ?` 通顺（`verify-fix4.py` §5）。
- P4：注记单行在位（y=520，`大师赛结果与都灵名单见本版正文。`），旧措辞 0 处；`.text.md` 第 515 行同；P4 其余行零位移（见上「改动范围」）。

### 机械门
- `occlusion_audit.py`（`occlusion-fix4.log`）：自检 OK（6 类阳性对照触发，干净对照静默），**0 flags**。
- `p8.py extract --total 150`（`p8-extract-fix4.log` / `p8-fix4.json`）：印出注记集 **121/150**（parse: joined），注记集与 `final-fr-p8.json` 逐项相同；键表唯一差异为 Q148（`devant`→`devant le`，有意修复），其余 149 键相同。
- `p8.py compare`（`p8-compare-fix4.log`，`--core-p8 svg/p8-exercices.svg --edition-p8 svg/p8-exercices.svg --total 150`）：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[]。
- `check_mcq.py`（`check-mcq-fix4.log`）：45 题体，**DEFECTS: 0，UNLOCATED: 0**（渲染行 1,448）。
- `freeze.py baseline`（`freeze-fix4.log` + `freeze-fix4b.log`，从核心目录运行 `--build . --core-svg svg`，跑两次）：工具报告 **`ok: 8`**，直接 SHA-256 比对 8/8（p4 `7e46e630eb6b`、p8 `5bee4d4473bf`，其余与上一轮相同）；core integrity：交付 SVG 未被重建改动。`--json` 输出 `freeze-fix4.json`，已据此刷新核心 `final-fr-freeze.json`。注意：`freeze.py` 的报告输出标志是 `--json`（非 `--json-out`）；build-copy 内附带的 `final-fr-freeze.json` 只是开工前核心文件的复本（含旧 p4/p8 哈希），不能当作本次工具输出。
- 文字层：`pdftotext -layout` 印刷版/网页版各 102,978 字节，**逐字节一致**（`print4.txt` / `web4.txt`）。SVG 文本字节合计 −6（P4 −6、P8 净 0：题干 −3 + 键 +3）。
- P8 最小字号（`tools/venv` PyMuPDF）：469 个 span，最小 **11.62pt**（214 个 span 处此字号）≥ 9.75pt；与上一轮相同。
- 徽章数（SVG chip 矩形 rx="2.7" 统计）：P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38，**总计 134**；分级 A2 #5c6e30 50 · B1 #46581f 65 · B2 #37402f 19 = 150 − 16 配对共享题（与上一轮一致）。
- 登记表：仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42），与基线一致。
- 孤儿标点全扫（自写 `verify-fix4.py` §7，8 页 `<text>` 元素逐项）：独行 。/，/、/：/；/！/？/./:/–/»/”/’/） **全 0**。另有 P4/P6 各 1 处独行 "— "（`« Quelle action ! » — 好球！` 等引用句的折行，坐标与 fix3 基线逐字节相同，非本轮回归），不在任务扫查的标点集内，未动。
- creambox（自写 `verify-fix4.py` §8，#f0eee5 框内文本按元素真实字体计量）：**0 违规**。初版脚本误用 serif 常规计量曾报 3 处，均为计量口径错误（标题实为 sans bold 23px，P4 387.2px / P5 398.5px / P6 383.5px，均在框内宽 404.5px 内）；occlusion 0 flags 亦佐证无出框。

### 150 题逐题复核
- 键表：`p8.py extract --json` 与 `final-fr-p8.json` 逐项相同（121 注记 + 全部键，唯一差为已刷新的 Q148）；compare CLEAN。
- `.text.md` RÉPONSES 区机械比对（自写 `verify-fix4.py`，`verify-fix4.log`）：**150 条解析、0 不符**（Q150 按既定口径：p8 抽出截断为「开放题」，`.text.md` 为「150. 开放题 — 要点见写作框…」，前缀一致）；另用 fix2 的 `keys-verify-fix2.py` 交叉验证亦为 **0 不符**（`keys-verify-fix4.log`，150 数齐全、无缺失/重复）。Q148 键 `devant le`、键位均与 `.text.md` 一致。

### §1.1 重测（`verify-fix4.log`）
- 纸色 #fbfaf6 8/8 有，金色 #b49a4a/#b3a06a 0，旧纸 #f7f1e2 0，「·」8 SVG + .text.md + ABSTRACT 均为 0，「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 182、.text.md 390、ABSTRACT 0——与上一轮逐项一致。
- `font-size="38"` 全刊 0 处；P2–P6 文章标题仍为 32px=24pt（次级标题上限，合规）。

## 8 版卡面目视（2026-11-11，cards/*.png）
- P1：未动，无回归；刊头/议程/目录/快讯/闪电问答、图注、页脚均干净。
- P2：未动，无回归；Q18 已单行；ET VOUS 框注记在框内；D 组标题在页底（上一轮即如此，未动）。
- P3：未动，无回归；词表 10 词可见；Q36/Q37 填空线孤行仍在（O7，裁定不修）。
- P4：**两处改动均到位**——「LES CHIFFRES DU SPORT」框中文注记「大师赛结果与都灵名单见本版正文。」单行在位，独行「。」已无；其余行零位移；Q44–48 选项整组完整；「LES PHRASES DU COMMENTATEUR」框引用句折行如旧；页脚干净。
- P5：未动，无回归；P5 原文首句「seize films sortent dans les salles de cinéma en France.」在位；电影词表 8 词可见；Méliès 图与图注干净。
- P6：未动，无回归；日程图 7 行、Q79–84 选项完整；「APRÈS LE VOTE」栏在右栏末，距页脚有余量。
- P7：未动，无回归；8 金句、诊所、园地、预告、Doré 图均在；页脚干净。
- P8：**Q148 已改到位**——G 对白「— On se retrouve (148)___ cinéma ? —」在位，答案区「148. devant le（电影院门口）」在位，答案区折行干净（Q150 行尾「框」字移至下一行首，同 y 坐标，无压图）；完形 8 枚徽章、对白条 5 枚、写作 B1 1 枚均画出；答案区 1–150 齐全；Hiroshige 图已放置；页脚干净。Q130 填空线孤行仍在（O6，裁定不修）。
- 网页版另行渲染目视：P4/P8（`web-p4-4.png` / `web-p8-8.png`，pdftoppm 自网页版 PDF）：注记单行、对白题干与答案键均如印刷版，无豆腐块、无字体缺失。
- 总体：8 版均无溢出、重叠、压页脚、豆腐块。

## KIT 更新
- 首行金句注：补 fix4 重测仍 8/8。
- §七门禁输出：渲染终值（fix4 重跑一致）、occlusion/p8 门禁改注 fix4、freeze 哈希（仅 P4/P8 变）与刷新说明、print/web PDF 尺寸与 SHA、`.text.md` 尺寸与 SHA/字符数、文字层口径（pdftotext -layout 各 102,978 字节逐字节一致；webpdf 计文字 46,725 字节）、P8 字号（数值不变，改注日期）、渲染说明（fix4 一次成功、无偶发事件）。
- §八：新增第 7 轮记录；“返修后观察”中 P4 孤儿句号改为已修（Q130、P3 Q36/Q37 仍留）。

## 结论
- Q148 两处（键 + 题干）与 P4 注记一处修完；改动范围经核查仅 `content8.py`、`expl.py` 各一处源码 + 生成物 + KIT + 两份 frozen JSON（Q148 一键、P4/P8 哈希）。
- 机械门全套重跑通过；§1.1 逐项重测通过；8 版卡面目视通过；150 题键 0 不符；金句逐字 8/8；孤儿标点全扫 0；creambox 0。
- **结论：(a) 零问题**（本轮返修后）。未跑 insert.py / lint --write / git push / git add / reset / stash；未提交；未碰各版目录（re-fanout #1 的 10 版是旧核心建的，等 re-proof (a) 后由 re-fanout #2 重建）、W43/W45/W46、其他目标语、tools/p8.py 与 tools/freeze.py；未改 core-fr 以外任何文件。待第四轮全量复校。
