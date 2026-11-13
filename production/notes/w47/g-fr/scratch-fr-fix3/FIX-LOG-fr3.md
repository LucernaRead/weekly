# W47 fr 核心版第三轮返修记录（第三轮复校 D9）

- 返修 builder：叶子（与 builder、第一/二轮返修 builder、第一/二轮/三轮校对员均不同的人）
- 日期：2026-11-11（EST）
- 依据：`hidden_files/w47/scratch-proof-fr3/PROOF-NOTE.md`（D9，结论 (b)）+ 任务简报
- 工作目录：`~/workspace/weekly-git/production/2026-w47/core-fr/`
- 工作记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fr-fix3/`

## 开工核对

- 印刷版 `La-Lucerna-VOL4.pdf`：30,447,011 字节，SHA-256 `98c8e128a53953e063b28b98fc98e6468c3b72e42a5a9868349a9def1bd2b61c`（与简报一致）。
- 网页版 `La-Lucerna-VOL4-web.pdf`：2,205,780 字节，SHA-256 `e25434430c2b2e0415adf26ef960126665c5c9434a78adf5d03f49c06717250e`（与简报一致）。
- `2026-w47-fr-zh-cn.text.md`：46,445 字节，SHA-256 `3210f6ba62df8407ffec0272fd6e5d055e6d0ac8a4de39774415287f993abe2c`（与简报一致）。
- 写探针 1（`git hash-object -w`）：通过（`0f64ae4741e8…`）。
- 写探针 2（真实文件写至本记录目录 `.probe`）：通过。
- SOP.md §8 与 §1.1 全文、`AGENTS.md`、PROOF-NOTE.md 全文、GATE-LOG.md（proof-fr3）、FIX-LOG-fr2.md 全文、core-fr/WEEKLY-KIT.md 全文已读。

## D9 独立核实（动手前，四处一致）

- 源码 `content7.py:83–84`：金句印为 « Mercredi 18 novembre, seize films sortent **au cinéma** en France. » (page 5)，Q102 题干「Mercredi, seize films ___ (sortir) **au cinéma**.」，键 `sortent`。
- 源码 `content56.py:18`（P5 原文）：「Mercredi 18 novembre, seize films sortent **dans les salles de cinéma** en France.」——「au cinéma」确为缩写改写，非逐字。
- 旧版 P7 SVG：`au cinéma` 1 处（金句）；旧版 `.text.md` 第 903 行（金句）、第 907 行（Q102 题干）同。
- 前两轮「金句 8/8 逐字」之说失实，实为 7/8（第三轮复校 8 条金句机械比对：唯 Q102 NOT-VERBATIM）。

## 修复清单（只动 D9 两处）

- `content7.py` 第 83–84 行（P7 `phrases` 表第 6 条，唯一改动的源码文件）：
  - 金句 → « Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. » (page 5)
  - Q102 题干 → 「Mercredi, seize films ___ (sortir) dans les salles de cinéma.」
  - 键 `sortent` 不动；其余 7 条金句不动。
- 未动：P5 原文（content56.py）；其他「au cinéma」正文句（P5「Et si on ne va pas au cinéma, on peut aller chiner…」、P5 讨论题「Un film au cinéma ou à la maison ?」、P8 对白「— Tu vas au cinéma mercredi ?」）——均非引文，不在 D9 范围内；D7、D8、D3、KIT 文字订正（第三轮复校已独立实测通过）一概未碰；O6–O8、D4 及其他已裁定观察项未动。
- 源码改动后复查：`sortent au cinéma` 全刊源码 0 处；除 `content7.py` 外其余 `.py` 源码 mtime 均为 2026-11-10/11 改动前（见下「改动范围」）。

## 构建命令

- `tools/venv/bin/python run.py`（`build-fix3.log`）：rc 0，零 `FLOW OVERFLOW` / `TOO WIDE` / `NOSPACE`。P7-phrases 流 1688→1718/1830（+30px 为一句折行，余量 112px）；其余流终值与上一轮相同；登记表仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42）。
- `tools/venv/bin/python render.py`（`render-fix3.log`）：rc 0，一次成功，无第一/二轮的 exit 120 瞬态。cards 8/8；大报版 PDF 30,446,982 B，SHA-256 `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7`，8 页 1462.5×2025pt。
- `tools/venv/bin/python tools/webpdf.py svg La-Lucerna-VOL4-web.pdf`（`webpdf-fix3.log`，rc 0）：网页版 PDF 2,205,749 B，SHA-256 `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823`，8 页，webpdf 计文字 46,732 字节。
- `W47_BUILD_DIR=<core-fr> W47_OUT_MD=<core-fr>/2026-w47-fr-zh-cn.text.md tools/venv/bin/python hidden_files/w47/scratch-fr/export47.py`（`export-fix3.log`，rc 0）：`.text.md` 46,477 B，SHA-256 `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e`，39,354 字符，542 条目，150 题齐全。
- `final-fr-freeze.json`：已按本次 freeze 工具 `--json` 输出刷新（ok: 8；见下）。`final-fr-p8.json` 无需刷新（抽出注记集与键表与旧版逐项相同）。`final-fr-occlusion.json` 内容不变（flag_count: 0）。
- 本轮无偶发事件：无 exit 120、无 `Disk quota exceeded`（第二轮返修曾三次偶发，磁盘本身有空闲）。

## 改动范围（核查）

- 源码：仅 `content7.py`（mtime 2026-11-11 03:34；其余 `.py` 均为 2026-11-10/11 改动前）。
- 生成物：`svg/p7-langue.svg`（唯一变化的 SVG）、`cards/*.png`（8/8 重渲）、`La-Lucerna-VOL4.pdf`、`La-Lucerna-VOL4-web.pdf`、`2026-w47-fr-zh-cn.text.md`、`final-fr-freeze.json`（刷新）。
- 文档：`WEEKLY-KIT.md`（首行金句注、§七门禁输出数值、§八第 6 轮记录）。
- SVG 直接 SHA-256 比对（改前 fix2 基线 → 改后）：p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `37cf3412c3f8`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p8 `ce072a017cd4`——7 页字节相同；仅 p7 `629cfe063bbd`→`75237d672f20`。

## 门禁结果（2026-11-11 返修后，build-fix3）

### D9 验证（四处一致）
- P7 SVG（`<text>` 元素拼接）：金句「seize films sortent dans les salles de cinéma en France」1 处、Q102 题干「seize films ___ (sortir) dans les salles de cinéma」1 处；`au cinéma` 0 处、`sortent au cinéma` 0 处（`verify-fix3.py`）。
- 印刷版 + 网页版文字层（PyMuPDF，空白归一化后）：两版 P7 均含金句与题干全文，旧措辞 0 处。
- `.text.md` 第 903 行（金句）、第 907 行（Q102 题干）已改；第 1079 行 RÉPONSES「102. sortent（sortir 上映）」键位不变。
- 8 条金句逐字复核（自写脚本，`content7.py` 金句原文对 P1–P6 SVG 文本归一化检索）：**8/8 VERBATIM**（修前 7/8）。

### 机械门
- `occlusion_audit.py`（`occlusion-fix3.log`）：自检 OK（6 类阳性对照触发，干净对照静默），**0 flags**。
- `p8.py extract --total 150`（`p8-extract-fix3.log` / `p8-fix3.json`）：印出注记集 **121/150**（parse: joined），与 `final-fr-p8.json` 逐项相同（noted_set 121、keys 150、total 150；Q102 键 `sortent`）。
- `p8.py compare`（`p8-compare-fix3.log`，`--core-p8 svg/p8-exercices.svg --edition-p8 svg/p8-exercices.svg --total 150`）：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[]。
- `check_mcq.py`（`check-mcq-fix3.log`）：45 题体，**DEFECTS: 0，UNLOCATED: 0**。
- `freeze.py baseline`（`freeze-fix3.log` + `freeze-fix3b.log`，从核心目录运行 `--build . --core-svg svg`，跑两次）：工具报告 **`ok: 8`**，直接 SHA-256 比对 8/8（p7 `75237d672f20f44b`，其余与上一轮相同）；core integrity：交付 SVG 未被重建改动。`--json` 输出 `freeze-fix3.json`，已据此刷新核心 `final-fr-freeze.json`。注意：`freeze.py` 的报告输出标志是 `--json`（非 `--json-out`）；build-copy 内附带的 `final-fr-freeze.json` 只是开工前核心文件的复本（含旧 p7 哈希），不能当作本次工具输出。
- 文字层：`pdftotext -layout` 印刷版/网页版各 103,001 字节，**逐字节一致**（`print3.txt` / `web3.txt`）。
- P8 最小字号（`tools/venv` PyMuPDF）：469 个 span，最小 **11.62pt**（214 个 span 处此字号）≥ 9.75pt；与上一轮相同。
- 徽章数（SVG chip 矩形 rx="2.7" 统计）：P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38，**总计 134**；分级 A2 #5c6e30 50 · B1 #46581f 65 · B2 #37402f 19 = 150 − 16 配对共享题（与上一轮一致）。
- 登记表：仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42），与基线一致。

### 150 题逐题复核
- 键表：`p8.py extract --json` 与 `final-fr-p8.json` 逐项相同（121 注记 + 全部键）；compare CLEAN。
- `.text.md` RÉPONSES 区机械比对（自写 `verify-fix3.py`，`verify-fix3.log`）：**150 条解析、0 不符**（Q150 按既定口径：p8 抽出截断为「开放题」，`.text.md` 为「150. 开放题 — 要点见写作框…」，前缀一致）；另用 fix2 的 `keys-verify-fix2.py` 交叉验证亦为 **0 不符**（`keys-verify-fix3.log`）。
- 自查脚本初版曾报 15 处不符，均为解析器 artifact（RÉPONSES 区「— 第 N 版 —」分隔行使 lookahead 失效）；修正分隔行剥离 + 行首条目 lookahead 后 0 不符，并经 fix2 脚本交叉确认。Q102 键 `sortent`、键位均不变。

### §1.1 重测（`verify-fix3.log`）
- 纸色 #fbfaf6 8/8 有，金色 #b49a4a/#b3a06a 0，旧纸 #f7f1e2 0，「·」8 SVG + .text.md + ABSTRACT 均为 0，「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 182、.text.md 390、ABSTRACT 0——与上一轮逐项一致。
- `font-size="38"` 全刊 0 处；P2–P6 文章标题仍为 32px=24pt（次级标题上限，合规）。

## 8 版卡面目视（2026-11-11，cards/*.png）
- P1：未动，无回归；刊头/议程/目录/快讯/闪电问答、图注、页脚均干净。
- P2：未动，无回归；Q18 已单行；ET VOUS 框注记在框内。
- P3：未动，无回归；词表 10 词可见；Q36/Q37 填空线孤行仍在（O7，裁定不修）。
- P4：未动，无回归；新句「Un choc remporté en deux sets…」在位；Q44–48 选项整组完整；「LES CHIFFRES DU SPORT」框中文注记「。」孤行仍在（O8，裁定不修）。
- P5：未动，无回归；P5 原文首句「seize films sortent dans les salles de cinéma en France.」在位（D9 的出处句）；电影词表 8 词可见；Méliès 图与图注干净。
- P6：未动，无回归；日程图 7 行、Q79–84 选项完整；「APRÈS LE VOTE」栏在右栏末，距页脚有余量。
- P7：**D9 两处已改到位**——金句第 6 句 « Mercredi 18 novembre, seize films sortent dans les salles de cinéma en France. » (page 5) 三行排布干净；Q102「Mercredi, seize films ___ (sortir) dans les salles de cinéma.」两行排布干净；金句流 1718/1830，未压诊所栏；8 金句、诊所、园地、预告、Doré 图均在；页脚干净。
- P8：未动，无回归；Q100 注「100. beauté（se terminer en beauté 圆满收尾）」在位；完形 8 枚徽章、对白条 5 枚、写作 B1 1 枚均画出；答案区 1–150 齐全（含「102. sortent（sortir 上映）」）；Hiroshige 图已放置；页脚干净。Q130 填空线孤行仍在（O6，裁定不修）。
- 总体：8 版均无溢出、重叠、压页脚、豆腐块。

## KIT 更新
- 首行金句注：补 D9 经过（修前第三轮复校实测 7/8，修后复核 8/8）。
- §七门禁输出：P7 金句流 1688→1718、freeze p7 哈希、print/web PDF 尺寸与 SHA、`.text.md` 尺寸与 SHA/字符数、文字层口径（pdftotext -layout 各 103,001 字节逐字节一致；webpdf 计文字 46,732 字节）、P8 字号（数值不变，改注日期）、渲染说明（render-fix3 一次成功、无偶发事件）、occlusion/p8 门禁改注第三轮返修；另补 freeze `--json` 标志与 build-copy 旧 freeze.json 的注意事项。
- §八：新增第 6 轮记录。

## 结论
- D9 两处修完，键 `sortent` 不动，其余 7 条金句不动；改动范围经核查仅 `content7.py` 一文件源码 + 生成物 + KIT。
- 机械门全套重跑通过；§1.1 逐项重测通过；8 版卡面目视通过；150 题键 0 不符；金句逐字 8/8。
- **结论：(a) 零问题**（本轮返修后）。未跑 insert.py / lint --write / git push / git add / reset / stash；未提交；未碰 W43/W45/W46、其他目标语、tools/p8.py 与 tools/freeze.py；未改 core-fr 以外任何文件。待第四轮全量复校。
