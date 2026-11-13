# W47 fr 核心版第二轮返修记录（第二轮校对 D7/D8 + KIT 文字订正）

- 返修 builder：叶子（与第一轮 builder、第一/第二轮复校员、第一轮返修 builder 均不同的人）
- 日期：2026-11-11（EST）
- 依据：`hidden_files/w47/scratch-proof-fr2/PROOF-NOTE-fr2.md`（D7、D8、KIT 小误、F-MAIL）+ 任务简报（O6–O8、D4 均不修）
- 工作目录：`~/workspace/weekly-git/production/2026-w47/core-fr/`
- 工作记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fr-fix2/`

## 开工核对

- 印刷版 `La-Lucerna-VOL4.pdf`：30,446,210 字节，SHA-256 `3833c9076893cd3be6c478407206d3540a4167d127acfba773be632f622dbcc5`（与简报一致）。
- 网页版 `La-Lucerna-VOL4-web.pdf`：2,203,259 字节，SHA-256 `59341d013995a0841af8dc2148b5c85a9e8a047674f355e6895cb6f190b131b0`（与简报一致）。
- `2026-w47-fr-zh-cn.text.md`：46,095 字节，SHA-256 `55295b25a5c23f6b1063947885878b8fefc42b8ce3934fece4d3e34dcaf3ed15`（与简报一致）。
- 写探针 1（`git hash-object -w`）：通过（`f30b2a09…`）。
- 写探针 2（真实文件写至本记录目录 `.probe`）：通过。
- ffmpeg：`/usr/bin/ffmpeg` 8.1.2 可用。
- SOP.md §8 与 §1.1 全文、`AGENTS.md`、PROOF-NOTE-fr2.md 全文、FIX-LOG-fr.md 全文已读。

## 修复清单

### D7（§8.1 译注词只在译注框内出现，4 词；全部用“写进同版正文”法，不删译注）

- **P1 `un vainqueur`**（`content12.py` 头条首段）：`Premier titre à Paris, neuvième en Masters 1000.` → `Le vainqueur remporte son premier titre à Paris, le neuvième en Masters 1000.` 事实不变（巴黎首冠、第 9 个大师赛冠军；ATP 官方 + 美联社已核）。P1-headline 流 1505→1556/1812。
- **P4 `un choc`**（`content34.py` 第 2 段末句）：`Une victoire en deux sets, sans tie-break dans le deuxième.` → `Un choc remporté en deux sets, sans tie-break dans le deuxième.` 事实不变（两盘获胜、第二盘无抢七）。P4-main 流仍 771/2560。
- **P6 `une navette` + `paritaire`**（`content56.py` P6 微练流末，新增「APRÈS LE VOTE」栏）：深读流余量仅 12px，加句会溢出，故置于微练流末（P6-micro 1985→2355/2560）：
  > Après le vote du Sénat, le texte repartira vers l'Assemblée : c'est la navette parlementaire, les allers-retours entre les deux chambres. Si le désaccord persiste, une commission mixte paritaire — sept députés et sept sénateurs — cherchera un texte commun.
  事实来源（逐句核实，不编造）：navette = 法案在两院间往返直至通过同一文本（《宪法》第 45 条第 1 款）；commission mixte paritaire = 7 名国民议会议员 + 7 名参议员，意见持续不一致时就仍在讨论的条款提出共同文本（《宪法》第 45 条第 2 款）。来源：senat.fr《La participation des chambres hautes à l'élaboration de la loi》（https://www.senat.fr/lc/lc95/lc955.html）+ Assemblée parlementaire de la Francophonie《La procédure législative》（art. 45）。表述用将来时/条件式（repartira、si le désaccord persiste），不预断本期法案的具体后续。
- **验证**（`d7-verify-fix2.py`，第二轮复校方法：SVG 文本枚举、剔除译注字符串后重数，屈折形式计为出现）：`vainqueur` 正文 1 次（「le vainqueur remporte son premier titre à Paris」）、`choc` 正文 1 次（「un choc remporté en deux sets」）、`navette` 正文 1 次（「c'est la navette parlementaire」）、`paritaire` 正文 1 次（「une commission mixte paritaire — sept députés et sept sénateurs」）。**OVERALL: PASS**。`.text.md` 剔除译注行后复核亦通过（每词正文 1 次）。
- **回归**：D3 13 词重测 13/13 PASS（`d3-verify-fix2.py`；注：第二轮复校原脚本 `d3-verify2.py` 在本 build 上报 `public FAIL`，系脚本 artifact——其剔除表含裸词 `le public`，会把正文句「le public a l'embarras du choix」一并剔掉；按词表行原文「le public — 观众」精确剔除后正文命中 1 次；P5 SVG 与上一轮字节相同，未动）。

### D8（P7 Q100 语法点 `avoir lieu` 与所注金句不符）

- `expl.py`：`gp4`「语法点｜avoir lieu：举行、发生。」→「语法点｜se terminer en beauté：圆满收尾。」；`n_gp4`「avoir lieu 举行」→「se terminer en beauté 圆满收尾」。
- Q100 题干「La semaine se termine en ___ (beau).」与键 `beauté` 不动（金句「Et dimanche 22 novembre, la semaine se termine en beauté …」逐字出自 P2 正文）。
- 验证：P7 SVG `lieu` 0 处（原仅 gp4 一处），P8 SVG `lieu` 0 处（原仅答案注一处）；P7 卡面语法点行、P8 答案区「100. beauté（se terminer en beauté 圆满收尾）」目视确认。P1「ont lieu」/「aura lieu」为正文正确用法，不在 D8 范围内，未动。

### KIT 文字订正（只改文字，不动成品）

- (a) §7「未改动」段与 §九第 4 条：「P2–P6 文章标题 Flow.title 38px=28.5pt（规范上限高 4.5pt）」与 SVG 实测不符——8 个 SVG 中 `font-size="38"` 为 0 处，P2–P6 文章标题均为 **32px=24pt，恰为次级标题范围（22.5–24pt）上限，合规**。已订正为实测值。
- (b) §九第 1 条与 §二.4：删去「入仓前须核实邮箱状态」表述，改写为 F-MAIL 规则准确表述——**投稿只认用户直接发来的；用户未直接发来投稿即无来信，不查邮箱、不核实邮箱状态**；本期 P7 读者园地为标注明确的编辑部示例。
- 另：§一 P6 条补充新增「APRÈS LE VOTE」栏说明；§三补 navette/CMP 机制事实来源行；§七门禁输出、§八校对记录同步更新至本轮新 build 号（见下）。

### 不修的项（第二轮复校已裁定为观察，不构成缺陷）

- O6（P8 Q130 填空线孤行）、O7（P3 Q36/Q37 填空线孤行）、O8（P4 体育数字框中文注记「。」孤行）：SOP §1.1 无“填空线不得孤行”规则，内容完整、无溢出。**未动**。
- D4（中文数字带空格）：已全周裁定不修。**未动**。
- 头条 39.75pt、无首字下沉、中文数字带空格、P8 题干字号、刊头 196px、头条字号：均已裁定可接受或不动。**未动**。

## 构建命令

- `tools/venv/bin/python run.py`（核心目录，`build-fix2.log`）：rc 0，零 `FLOW OVERFLOW` / `TOO WIDE` / `NOSPACE`。终值：P1-headline 1556/1812，P1-budget 2242/2300，P1-quiz 2491/2560，P2-feature 289/1540，P2-ex 2332/2560，P3-main 565/2560，P4-main 771/2560，P4-micro 2188/2560，P5-main 735/2560，P6-deep 1288/1300，P6-ex 2402/2560，P6-opinion 1190/1300，P6-micro 2355/2560，P7-A2 950/1150，P7-B1 855/1150，P7-B2 1019/1150，P7-outils 949/1150，P7-phrases 1688/1830，P7-clinic 2140/2268，P8-battery 1428/1485，P8-keys 2046/2560，Hiroshige y=2055.7 已放置；REG 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42），与基线一致。
- `tools/venv/bin/python render.py`（`render-fix2.log` 首次跑 exit 120、P1 卡片后异常退出，无 traceback 输出，与第一轮 render4 同类瞬态；重跑 `render-fix2b.log` rc 0）：大报版 PDF 30,447,011 B，SHA-256 `98c8e128a53953e063b28b98fc98e6468c3b72e42a5a9868349a9def1bd2b61c`，8 页 1462.5×2025pt；cards 8/8 重渲。
- `tools/venv/bin/python tools/webpdf.py svg La-Lucerna-VOL4-web.pdf`（`webpdf-fix2.log`，rc 0）：网页版 PDF 2,205,780 B，SHA-256 `e25434430c2b2e0415adf26ef960126665c5c9434a78adf5d03f49c06717250e`，8 页，46,695 text bytes。
- `W47_BUILD_DIR=<core-fr> W47_OUT_MD=<core-fr>/2026-w47-fr-zh-cn.text.md tools/venv/bin/python hidden_files/w47/scratch-fr/export47.py`（`export-fix2.log`，rc 0）：`.text.md` 46,445 B，SHA-256 `3210f6ba62df8407ffec0272fd6e5d055e6d0ac8a4de39774415287f993abe2c`，39,322 字符，542 条目（+2 为 P6「APRÈS LE VOTE」标题与段落），150 题齐全。
- 偶发事件：本轮三次写盘时偶发 `Disk quota exceeded`（一次为 render-fix2.log 的 shell 重定向、一次为 p8-font-fix2.log 的 shell 重定向、一次为 `cp` 写 keys-verify-fix2.log）。写探针两次均通过；磁盘本身 46G 空闲（`df` 70%）；同时段小文件写（`muse.write`、其余重定向）与重跑均成功，无数据丢失；属瞬态，未硬锤重试。

## 门禁结果（2026-11-11 返修后，build-fix2）

### 构建与渲染
- 见上。`final-fr-freeze.json` 已刷新为本次工具输出（ok: 8）；`final-fr-p8.json` 无需刷新（抽出注记集与键表与旧版逐项相同）。

### 机械门
- `occlusion_audit.py`（`occlusion-fix2.log`）：自检 OK（6 类阳性对照触发，干净对照静默），**0 flags**。`final-fr-occlusion.json` 内容不变（`flag_count: 0`）。
- `p8.py extract --total 150`（`p8-extract-fix2.log`）：印出注记集 **121/150**（parse: joined），`--json`（`p8-fix2.json`）与 `final-fr-p8.json` 逐项相同（noted_set 121、keys 150、total 150；仅 `p8` 路径字段写法不同）。
- `p8.py compare`（`p8-compare-fix2.log`）：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[]。
- `check_mcq.py`（`check-mcq-fix2.log`）：45 题体，1,448 渲染行，**DEFECTS: 0，UNLOCATED: 0**。
- `freeze.py baseline`（`freeze-fix2.log`，从核心目录运行 `--build . --core-svg svg`）：工具报告 **`ok: 8`**，直接 SHA-256 比对 8/8（p1 `6aad8b4bcdfb`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `37cf3412c3f8`、p5 `fff2a8d3d7ac`、p6 `7af7cf3c240f`、p7 `629cfe063bbd`、p8 `ce072a017cd4`）。未改动页 P2/P3/P5 哈希与上一轮完全一致；P1/P4/P6/P7/P8 哈希变化与本轮 4 处改动一一对应。`render.py` 未被 freeze 改动（mtime 仍为 2026-11-10；“repointed files: render.py”指工具 build-copy 内的重定向）。
- 文字层：`pdftotext` 大报版与网页版各 46,695 字节、7,292 词，**逐字节一致**（词级多重集相等 True）。
- P8 最小字号（`p8-font-fix2.log`，`tools/venv` PyMuPDF）：469 个 span，最小 **11.62pt**（214 个 span 处此字号）≥ 9.75pt；较上一轮 +1 span，系 Q100 注记改长所致。
- 徽章数（SVG chip 矩形 rx="2.7" 统计）：P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38，**总计 134**；分级 A2 #5c6e30 50 · B1 #46581f 65 · B2 #37402f 19 = 150 − 16 配对共享题（与上一轮一致）。
- 登记表：仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42），与基线一致。

### D7 严格验证（`d7-verify-fix2.log`）
- SVG 文本枚举、剔除译注字符串后整词匹配：P1 `vainqueur` 正文 1 次、P4 `choc` 正文 1 次、P6 `navette` 正文 1 次、`paritaire` 正文 1 次，上下文逐条可见。**OVERALL: PASS**。
- `.text.md` 剔除译注行后复核：P1 `vainqueur` 1 次、P4 `choc` 1 次、P6 `navette`/`paritaire` 各 1 次。**PASS**。

### D8 验证
- P7 SVG `lieu` 0 处；P8 SVG `lieu` 0 处；P7 语法点「se terminer en beauté：圆满收尾。」、P8「100. beauté（se terminer en beauté 圆满收尾）」均在卡面确认。

### D3 回归验证（`d3-verify-fix2.log`）
- 13 词全部在同版正文段内（词表行原文精确剔除后整词匹配）：P3 bouteille/raisin/vigne、P4 tennis/adversaire、P5 salle/public/réalisateur/scénario/écran/acteur/actrice/séance。**OVERALL: PASS**。

## 150 题逐题复核
- 键表：`p8.py extract --json` 与 `final-fr-p8.json` 逐项相同（121 注记 + 全部键）；compare CLEAN。
- `.text.md` RÉPONSES 区机械比对（`keys-verify-fix2.py`，`keys-verify-fix2.log`）：**150 条解析、0 不符**（Q150 按前缀一致计：p8.py 抽出将长写作键截断为「开放题」，`.text.md` 为全句，系旧 artifact，与上一轮 `final-fr-p8.json` 一致）。
- 改动题复核：Q100 题干与键 `beauté` 不动（金句逐字出自 P2 正文）；D7 改动的 4 词不涉任何题干/键/注记（P6 新增栏为正文说明，非练习）；其余题干/键/注记均未动（登记表统计与基线相同）。

## §1.1 重测（`section11-fix2.log`）
- 纸色 #fbfaf6 8/8 有，金色 #b49a4a/#b3a06a 0，旧纸 #f7f1e2 0，近黑 #2a2419/#2c2822 0，边缘 stroke-width≥2 0，「·」0，「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 182、.text.md 390、ABSTRACT 0。
- 字体（`<text>` 元素统计）：P1 103 Newsreader / 76 Noto Sans CJK SC / 10 Noto Serif CJK SC / 1 UnifrakturMaguntia；P6 131 / 70 / 14；P8 108 / 192 / 23；Noto Serif CJK SC 跨度内拉丁词 0。P1 Newsreader 102→103（头条首段改写）、P6 123→131/69→70（新增栏）、P8 Sans 191→192（Q100 注记改长）。
- P2 band y=72、页脚线 2596、SVG 1950×2700 全 8 版；VOL.4 文本 11 处、VOL.5 9 处（合规的下一期指称）。
- P2–P6 文章标题字号：SVG 实测均为 32px=24pt（`font-size="38"` 全刊 0 处），恰为次级标题范围上限，合规。
- P8「　」181→182 系 Q100 注记改长后折行变化所致，150 题键比对 0 不符，内容无缺失。

## 8 版卡面目视（2026-11-11，cards/*.png）
- P1：新句「Le vainqueur remporte son premier titre à Paris, le neuvième en Masters 1000.」在位，头条段重排干净；刊头/议程/目录/快讯/闪电问答、图注、页脚均干净。
- P2：未动，无回归；Q18 已单行；ET VOUS 框注记在框内。
- P3：未动，无回归；词表 10 词可见；Q36/Q37 填空线孤行仍在（O7，裁定不修）。
- P4：新句「Un choc remporté en deux sets, sans tie-break dans le deuxième.」在位；Q44–48 选项整组完整；「LES CHIFFRES DU SPORT」框中文注记「。」孤行仍在（O8，裁定不修）。
- P5：未动，无回归；D1 已改句与 8 电影词均在；Méliès 图与图注干净。
- P6：新增「APRÈS LE VOTE」栏在右栏末，距页脚有余量；日程图 7 行、Q79–Q84 选项完整；Q84 可答。
- P7：gp4 已为「se terminer en beauté：圆满收尾。」；8 金句、诊所、园地、预告、Doré 图均在。
- P8：Q100 注「100. beauté（se terminer en beauté 圆满收尾）」在位；完形 8 枚徽章、对白条 5 枚、写作 B1 1 枚均画出；答案区 1–150 齐全；Hiroshige 图已放置；页脚干净。Q130 填空线孤行仍在（O6，裁定不修）。
- 总体：8 版均无溢出、重叠、压页脚、豆腐块。

## 结论
- D7、D8 全部修完并通过第二轮复校方法的复核；KIT 文字订正 (a)(b) 已做；O6–O8、D4 及其他已裁定不动项均未动。
- 机械门全套重跑通过；§1.1 逐项重测通过；8 版卡面目视通过；150 题键 0 不符。
- **结论：(a) 零问题**（本轮返修后）。未跑 insert.py / lint --write / git push / git add / reset / stash；未提交；未碰 W43/W45/W46 与其他目标语文件；未改 tools/p8.py 与 tools/freeze.py（工作树中该两文件的修改为返修前已有状态，mtime 2026-11-10，未动）。
