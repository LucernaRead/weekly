# W47 nl 家 §8.4 状态核对报告（VERIFY-REPORT）

- 核对员：§8.4 状态核对员（与建造者、proof1/2/3 校对员、fix 工人均不同）
- 核对时间：2026-11-13 ~05:00–05:30 UTC
- 依据：SOP §8 / §8.4 proofread-until-zero；只核对、不修复、不重建、不 commit、不 push、不跑 lint
- 工作目录：`hidden_files/w47/scratch-verify-nl/`（`mech/` 门禁日志 + JSON；`pages/` 渲染图 p1–p8 + web-p8）
- 磁盘：开工 96G / 150G，收尾 96G，未触 ≥100G 停手门限
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（全程；未用系统 python3）

## 总体结论：nl 家 11/11 VERIFIED CLEAN

- 10 版（core-nl + de/en/es/fr/it/ja/ko/pt/zh-tw）：最后重校为第三轮独立重校
  PROOF-NOTE-3（2026-11-12 18:34–18:50 UTC，结论 (a) 零问题），当前磁盘三 SHA
  与该轮指纹 30/30 一致 → VERIFIED CLEAN，无需重校。
- 1 版（nl-ru）：自 PROOF-NOTE-3 后 SHA 变过（*-ru 重建 + fix-nl-ru2 四处盒题降字号），
  本人作为不同校对员做了全新全量重校（下文 §nl-ru）：结论 (a) 零问题 → VERIFIED CLEAN。
- 内容待修清单：无（0 项）。KIT wave-2 清单：见 §KIT §7 核对（6 项，均为 KIT 记录口径，不改 KIT）。

## 最后重校记录（run-log / PROOF-NOTE-3）

- 第三轮独立重校员，scratch-reproof3-w47-nl/PROOF-NOTE-3.md，2026-11-12 18:34–18:50 UTC。
- 结论 (a) 干净 — 零问题轮次；第二轮 3 项修复全部核实在版；指纹 33/33 与修复记录一致；
  机械门禁全绿（gates 10/10 ALL PASS；boxtitle 11 版 0 DEFECT；spill 11 版 0 SPILL；
  edge 11 版 0 TOUCH/NEAR；core occlusion 0 flags；core p8 150/150；D5 census 11 版 PASS；
  全家 ASCII 直引号 0）。
- run-log L4691–L4695：「nl 三轮重校 CLEAN（第二家定稿）」「proofread-until-zero 达成，内容定稿」。
- 此后 nl 家唯一变动：nl-ru（*-ru 重建 2026-11-12 23:43 UTC，印 5541fc59…；
  扫查发现 boxtitle 4 处 → fix-nl-ru2，2026-11-13 01:12–01:35 UTC，印 d4f08158…；
  run-log L4978–L4982 协调员独立核实通过，门禁全绿）。其余 10 版此后无任何改动
  （mtime 均 ≤ 2026-11-12 18:19 UTC；nl-ru 印/网 mtime 2026-11-13 01:20/01:21 UTC）。

## SHA-12 表（磁盘实测 2026-11-13 ~05:00 UTC；印/网/text.md）

| 版 | 印 PDF（SHA-12 / 字节） | 网 PDF（SHA-12 / 字节） | text.md（SHA-12 / 字节） | vs PROOF-NOTE-3 | 结论 |
|---|---|---|---|---|---|
| core-nl（nl-zh-cn） | `0c5d63b942d2` / 13,830,540 | `2b6f223eaff9` / 1,874,709 | `aa1f470353f9` / 44,087 | 一致 | VERIFIED CLEAN |
| nl-de | `9032021929da` / 12,104,245 | `fbf0c25a503a` / 1,536,368 | `6825c35db04c` / 46,247 | 一致 | VERIFIED CLEAN |
| nl-en | `7e35b073ade0` / 12,102,396 | `c7ffd6676cfa` / 1,534,493 | `e3273f300f42` / 45,136 | 一致 | VERIFIED CLEAN |
| nl-es | `06f0e2e00aec` / 12,107,932 | `7025ce05d975` / 1,540,051 | `672bd4c0080c` / 47,648 | 一致 | VERIFIED CLEAN |
| nl-fr | `08f57ec27d86` / 12,106,421 | `1b429a3ff61e` / 1,538,511 | `f1d1154442c4` / 47,744 | 一致 | VERIFIED CLEAN |
| nl-it | `dc91af0aa78d` / 12,102,273 | `9eff96cf487a` / 1,534,364 | `e9880da2da99` / 47,194 | 一致 | VERIFIED CLEAN |
| nl-ja | `b886a483f641` / 18,803,540 | `2b38c2547606` / 1,967,732 | `b7e5f5dc8b48` / 47,804 | 一致 | VERIFIED CLEAN |
| nl-ko | `e7fa69a263fe` / 13,871,386 | `218aebe12b4b` / 1,791,786 | `e13db87160d1` / 47,576 | 一致 | VERIFIED CLEAN |
| nl-pt | `e2fe3b3a9568` / 12,110,707 | `40c51869695b` / 1,542,854 | `67516e2163c8` / 47,365 | 一致 | VERIFIED CLEAN |
| nl-ru | `d4f081587c7d` / 12,261,013 | `7a06f80d9238` / 1,674,522 | `dd1c0c087c46` / 57,909 | 印/网已变，文不变 | 全新重校 (a) → VERIFIED CLEAN |
| nl-zh-tw | `3fd293bfef56` / 13,887,537 | `542c6f1bc8e2` / 1,976,266 | `bf1f627d1bbf` / 44,308 | 一致 | VERIFIED CLEAN |

全值 SHA-256（小写）：见本报告末尾「附录：SHA-256 全值表」。

## nl-ru 全新全量重校（SOP §8）

重校对象：当前磁盘版（印 `d4f081587c7d…` / 12,261,013 B；网 `7a06f80d9238…` / 1,674,522 B；
文 `dd1c0c087c46…` / 57,909 B，431 行）。修前态（*-ru 重建版，印 `5541fc59…` /
网 `5df8b0d6…`）与 FIX-LOG（scratch-fix-nl-ru2/FIX-LOG.md）已读：4 处均为盒题右溢，
只降字号不改措辞（content12.py:43 P1 23→22pt、:179 P2 23→22pt；content56.py:148 P6
24→22pt、:168 P6 21→20pt）；仅 p1/p2/p6 SVG 变；text.md 不变。

### 总体结论：(a) 干净 — 零问题轮次

**新发现：0 条**（MAJOR 0、MEDIUM 0、low 0、trivial 0）。观察项 1 条（O-1，见下，非缺陷，不阻塞）。

### 1. text.md 全文通读（431 行，P1–P8）

- 荷兰语正文拼写/变位/性数/标点：无问题。俄语讲解层逐项对照正文：词表词均真实出现正文；
  数字/日期/译名与 core 一致。
- 日期/星期经 `date -d`（Europe/Amsterdam）逐一核验：2026-11-13 周五、11-16 周一、
  11-22 周日、11-24 周二、11-29 周日、12-05 周六，与文中全部星期标注一致
  （P1「Vrijdag」= 11-13；P7 VOLGENDE WEEK「Dinsdag 24 november」「Zondag 29 november」均对）。
- 算术复核：16 Nov→5 Dec = 19 天；14→15 Nov = 1 天；12:00–16:00 = 4 小时；
  2009→2026 = 17 年；荷兰进球 7–5（1+2+2+2=7，对手 1+1+2+1=5）；图表 35+30+20+15=100、
  35+30=65；Eredivisie 积分与赛果一致。
- 题号：编号行 142 条（1–150 缺 25–28 与 141–144 两组），加两组共 8 题 = 150 题；
  P8 答案 1–150 逐题复核：题面、选项、答案键、简析全部与正文/图表一致。
  重点核：Q53 `kwartfinales`（复数，题干「De nummers één en twee gaan naar de ___」）；
  Q78 `Zij → gaat maken`（单数 zij）、Q79 `De kinderen → gaan schrijven`（复数）；
  Q97–100 / Q133–136 组句语序正确；Q137/138 译俄、Q139/140 译荷，键与读者语一致
  （p8 keydiff [137, 138] 为预期）；Q139 `De intocht in Amsterdam was de 88e editie.`、
  Q140 `Ik maak een surprise met een kort gedicht.` 与正文一致。
- P7 金句 8 条逐字出自本期文章且页码标注正确（P1×2、P2、P3、P4、P5、P6×2）。
- 范文词数按词计 81 词（「–」不计词），与「80–100 词」及「(81 слов)」标注一致。
- ABSTRACT 齐全：俄语单行、450 B、无 ASCII 双引号、含刊名 + 目标语名 + A2–B2 + 150 练习 + 真实话题。
- 粘连专项（ledger L1406 旧旗标「nl-ru（1.44）」+ 共享 `13ноября`）：当前印 PDF 文字层
  全文 grep——数字+西里尔粘连 0 处；「16 ноября」「5 декабря」等全部带真空格。
  该旗标为 R3 _run_w 移植前的测量，现版已修，不重报。

### 2. 印/网文本层逐字节一致

- `pdftotext` 印 = 网 = 55,036 B，`cmp` 逐字节一致；PyMuPDF 逐字比较 8/8 页
  posdiff 0、msdiff 0（P1 799、P2 805、P3 725、P4 726、P5 783、P6 734、P7 887、P8 2207 tokens）。
- 印/网 PDF 均为 8 页；PyMuPDF 提取文本 SHA 相同（`ed06e6df19c7`，54,014 B）。
- P6 token 734（PROOF-NOTE-3 为 733）：fix-xru 改道后 P6 `?` 独立 run 致分词 +1，
  印/网一致，非内容变化。
- 网 P8 渲染目检：与印 P8 逐项一致，无豆腐块、无缺字。

### 3. P8 150 题机械复核

- `p8.py extract` 150/150；`p8.py compare` vs core-nl CLEAN，keydiff=[137, 138]（预期）；
  印 PDF 文字层中答案编号 1–150 全有、0 缺失。
- P8 答案区最小字号 10.12pt（median 10.12pt，602 spans）；级别徽章 core=edition
  {A2: 8, B1: 24, B2: 3}。

### 4. 8 页逐页看图（印 PDF，100 dpi，`pages/p1–p8.png`）

- P1：干净。修复点 1「DE WEEK IN CIJFERS　В ЦИФРАХ」末词 ЦИФРАХ 已入盒；头条、数字框、
  议程、HET WOORD、BLIKSEMQUIZ 均无溢出/重叠/压页脚；页脚「Страница 1 из 8」。
- P2：干净。修复点 2「ZO ONTHOUD JE HET　ЗАПОМНИ」已入盒；四词卡、练习 11–28 齐全。
- P3：干净。练习 29–46 齐全；词框 `vestingstad · ontvangen · sleutel · editie · leeskring`
  正常折行（leeskring 落第二行），非缺陷。
- P4：干净。练习 47–64 齐全；中栏 gloss 盒下留白为栏末正常收尾（与 core 同形），非缺陷。
- P5：干净。练习 65–82 齐全；图片 + 图注 + 出处齐全。
- P6：干净。修复点 3「DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ」末词 ДАННЫЕ 已入盒，条形 35/30/20/15
  成比例；修复点 4「VOOR OF TEGEN?　ЗА ИЛИ ПРОТИВ?」末尾 `?` 已入盒；练习 83–100 齐全。
- P7：干净。练习 101–112、PAS OP、HET WOORD、BRIEVEN、金句 8 条、VOLGENDE WEEK 带均齐全。
- P8：干净。测试 113–150 + 答案 1–150 全有；答案 137/138 俄语键、139/140 荷兰语键、
  141–144 配对 b/c/d/a、150 范文标注 (81 слов) 均与 text.md 一致。

### 5. 共享工具机械门禁（tools/venv/bin/python，只用仓内共享工具）

| 门禁 | 结果 |
|---|---|
| `tools/gates.py`（occlusion + p8 + freeze + 印/网文字层 + P8 字号/chips + §1.1） | **ALL PASS**：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN keydiff=[137, 138]；freeze 8/8；印/网文字 posdiff 0 msdiff 0，8/8 页；pdftotext 印 = 网 = 55,036 B；P8 答题区最小 10.12pt；chips core=edition {A2: 8, B1: 24, B2: 3}；§1.1 clean（off-palette={}，gold/old=False，stroked_rects=0，VOL.5=5 与 core 一致，paper_fills=8） |
| `boxtitle_check.py` | **0 DEFECT、0 OBSERVE、0 marginal**（34 titles / 483 body lines）；4 处修复点墨余量：P1 +17.0px、P2 +9.1px、P6 +20.6px、P6 `?` +10.1px（与 FIX-LOG §4 一致） |
| `occlusion_audit.py`（单跑） | **0 flags**，selftest OK（6 类 planted flags 全部触发，clean 对照静默） |
| `spill_sweep.py` | **rc=0，0 SPILL**，110 OBSERVE（均为 ABOVE/BELOW 负距离近邻候选，非溢出；与 fix 工人同值） |
| `pdf_edge_scan.py`（印 PDF） | **0 TOUCH、0 NEAR**（8 页） |
| D5 census（`scratch-d5-plan/mechanism/d5_census.py`） | **PASS**：D5 Latin 0、Cyrillic 0、curly-in-CJK 0、curly total 0；noto_sans_elements=829（俄语讲解层按 §1.1 用 Noto Sans，属设计；PROOF-NOTE-3 同口径 780，量级一致） |
| `head_check.py`（fix 工人已跑，本轮复核 run.log） | PASS 0 defects（`run.py` TOTAL 150，0 FLOW OVERFLOW / 0 HEAD TOO WIDE） |

日志：`mech/gates-ru.log` / `mech/gates-ru.json`、`mech/boxtitle-ru.log`、
`mech/spill-ru.log`、`mech/edge-ru.log`、`mech/occl-ru.log`、`mech/d5-census-ru.log`。
（gates.py 由 scratch-reproof3-w47-nl/mech/gates.py 原样复用，仅换工作目录；未改生产文件。）

### 观察项（非缺陷，不阻塞 CLEAN）

- O-1：P3 词表 gloss `de editie — раз`（text.md L~168；P8 答案 37 同文「editie – editie = раз」）。
  「раз」作「第 N 次」解可通，但 `editie` 本义为「期/版」，更贴切的俄语 gloss 为「выпуск」。
  前三轮均未 flag 的既有写法，本轮不升级为缺陷、不派修复；如协调员认为值得改，
  属于 KIT wave-2 之外的措辞微调，需另派 fix + 重校（改一字亦须重校）。
- 不重报项（PROOF-NOTE-3 已裁定，状态未变）：P8 `VUL DE KRONIEK IN` 标题余量为已具名裁定观察、
  非缺陷；Q139 `(88-й)`、Q140 `(surprise (фикс.))` 简略；ru「башмак」vs「ботинок」同义词
  （本版统一用 ботинок）；P8 keydiff [137, 138] 为翻译题读者母语键，预期。

## KIT §7 核对（只记录，不改 KIT → wave-2 清单）

逐版核对 KIT「Files delivered / Deliverables」节记录的 SHA 与磁盘实测：

| 版 | 印 SHA | 网 SHA | text.md SHA | 备注 |
|---|---|---|---|---|
| core-nl | §7 无 SHA（仅尺寸）；§18 "New SHAs" 行三值均与磁盘一致 | — | — | §7 缺 SHA 行，属格式口径（wave-2 W-1） |
| nl-de | ✓ 一致 | ✓ 一致 | ✓ 一致 | — |
| nl-en | ✗ 陈旧 | ✗ 陈旧 | ✗ 陈旧 | §7 Deliverables 行仍为 round-2 fix 前值（印 `d87a5242…`/12,102,271 B、网 `db7a9ace…`/1,534,348 B、文 `9596c4ac…`/45,115 B）；当前值只在 §13 fix 节（印 `7e35b073…`、网 `c7ffd667…`、文 `e3273f30…`，与磁盘一致）。§7 未同步（wave-2 W-2） |
| nl-es | ✓ 一致 | ✓ 一致 | ✓ 一致 | — |
| nl-fr | ✓ 一致 | ✓ 一致 | §7 缺 text SHA 行（仅 47,744 B） | 当前文 SHA 只在 fix/D5 节（wave-2 W-3） |
| nl-it | ✓ 一致 | ✓ 一致 | §7 只有旧值（`f1d9e3f5…` pre-D5 / `62142f93…` 更早） | 当前文 SHA `e9880da2…` 只在 fix 节（wave-2 W-4） |
| nl-ja | ✓ 一致 | ✓ 一致 | §7 缺 text SHA 行（仅 47,804 B） | 当前文 SHA 只在 fix 节（wave-2 W-3 同类） |
| nl-ko | ✓ 一致 | ✓ 一致 | §7 缺 text SHA 行（仅 47,576 B） | 当前文 SHA 只在 fix 节（wave-2 W-3 同类） |
| nl-pt | ✓ 一致 | ✓ 一致 | §7 缺 text SHA 行（仅 47,365 B） | 当前文 SHA 只在 fix 节（wave-2 W-3 同类） |
| nl-ru | ✓ 一致 | ✓ 一致 | §7 缺 text SHA 行（仅 57,909 B） | 当前文 SHA 只在 fix-nl-ru2 节（wave-2 W-3 同类）；印/网已同步到 fix 后值 ✓ |
| nl-zh-tw | ✓ 一致 | ✓ 一致 | §7 只有 build-2 旧值（`54d20ccd…`） | 当前文 SHA `bf1f627d…` 只在 fix 节（wave-2 W-5） |

Wave-2 清单汇总（KIT 记录口径，不改 KIT；不影响内容定稿）：
- W-1：core-nl §7 无 SHA 行（当前值在 §18，与磁盘一致）。
- W-2：nl-en §7 三 SHA 全陈旧（round-2 fix 后未同步 Deliverables 行）。
- W-3：nl-fr / nl-ja / nl-ko / nl-pt / nl-ru §7 缺 text.md SHA 行（仅尺寸）。
- W-4：nl-it §7 text SHA 只有旧值（pre-D5 `f1d9e3f5…`）。
- W-5：nl-zh-tw §7 text SHA 只有 build-2 旧值（`54d20ccd…`）。
- 另：PROOF-NOTE-3 附注提及的 de/es/en KIT 内旧 SHA 各 1 处（历史修复记录行所引），
  本轮复核仍为历史行引用，非当前交付值，不另列。

## 待修清单

- 内容待修：无。nl 家 11/11 内容定稿（proofread-until-zero 达成）。
- KIT wave-2：上表 W-1～W-5（记录口径，待 wave-2 统一处理）。
- 观察项 O-1（`de editie — раз` gloss）：非缺陷，不派修；是否微调由协调员定。

## 附录：SHA-256 全值表（磁盘实测）

| 版 | 印 PDF | 网 PDF | text.md |
|---|---|---|---|
| core-nl | `0c5d63b942d2a024694e87ba27b85b3eff0b3d411e78f9956094b5f2a4383be4` | `2b6f223eaff9afa7445c54b385213e8131eeddf11b9ae9a139388b32da7f940d` | `aa1f470353f9fa24bdec29028e596dd924387fe7d05956f208a57006025e2327` |
| nl-de | `9032021929da68607da8097bd50612aeec93f4b5de76d0e15e8757712172fb19` | `fbf0c25a503a8fb532b60dc60d1b95b265a00659df1c69afb334b6bddf299795` | `6825c35db04c62e1bec4f8f6e6a511597a17af0b02b17bc5260a560043575785` |
| nl-en | `7e35b073ade00c564981bfee31526d1f6306c86e9c9ff3ae58199a278f9426af` | `c7ffd6676cfa31798994f11af35a469485e6fefd1fa3a8e079c47c7aae3b0d95` | `e3273f300f42236a06faaddd3302b5be1a4a340adca285efdff19f2b23f3f316` |
| nl-es | `06f0e2e00aece0d687edf0540098e4cc8b6e4e4c62b451792a1be6cb11608874` | `7025ce05d97599d1910ab4e27f1e1c583ae86d43ef5d64a169b22bdb77ef0721` | `672bd4c0080c14ab11026a13ccdecf826bd759cc3f348c5751852386efe4684b` |
| nl-fr | `08f57ec27d8698c54be0ef79024048fec737ed4aabbfa8be68c1bb04b26c5fad` | `1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc` | `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` |
| nl-it | `dc91af0aa78da597d0f3025087cd8695ccda1cb9ca454fc5445924e12bbe0059` | `9eff96cf487a6beb5e26413ac9683bf771aac12f0ef9d6c2eca1de5b399fbf93` | `e9880da2da990ad87348c650cc4f82637a108284d7929de2ed901019ef77ac0a` |
| nl-ja | `b886a483f64181624efef8f17c4d1a6d2e421571cf26c2de576f72b5682399b6` | `2b38c2547606d2a33b436cea4337acf4a93ddfbe4acdd93ef5533781d2755b7b` | `b7e5f5dc8b484da52b0a22493149d93f0bbd3a0aeb79deb56b2f28e017a80084` |
| nl-ko | `e7fa69a263fe85ef08205ac654e55e2333f590de5f6bd6f1ea73103150746bff` | `218aebe12b4ba140a0180cfdd3fcb2719547737f1e7c59682aca83a57fed231a` | `e13db87160d1477972824431d9f4e194f90f53a53b7954e659cc74484801f537` |
| nl-pt | `e2fe3b3a95686bd48e01a7975f62ee33bb821dd6a8a743c1a188bb8e6f119d37` | `40c51869695b80e165661c6adb9309c70341342d56d632c472a7ba18f9ace508` | `67516e2163c8c769ab9574b60b472c7d97706b3c4d89182bb95faa221513727a` |
| nl-ru | `d4f081587c7d85e155734d4008d191e8b6f009f50738b3370f966c311053002e` | `7a06f80d9238669ae1c8c1bfc848a2b814d9f0999e3e9f4c79b942dd17747dff` | `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228` |
| nl-zh-tw | `3fd293bfef564ea277f4f96495710f7391ad5204da659bdd43dc2ce3edfde693` | `542c6f1bc8e2f71b0cdf558e169dca3d1738e981919433c63182a304a44754ec` | `bf1f627d1bbf6387cb0f782e6ede2feb3fe18ffb48bd599ce3720be3238b9855` |
