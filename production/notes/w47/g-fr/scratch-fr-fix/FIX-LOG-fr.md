# W47 fr 核心版返修记录（第一轮校对 D1/D2/D3/D5/D6 + O5 顺手 + O2 KIT 注）

- 返修 builder：叶子（与第一轮 builder、第一轮校对员不同的人）
- 日期：2026-11-10（EST 晚间）
- 依据：PROOF-NOTE-fr.md（D1–D6、O1–O5、(a)(b) 裁定）+ 协调员裁定（D4 不修；(a1)(a2) 不改；O1/O3/O4 不处理）
- 工作目录：~/workspace/weekly-git/production/2026-w47/core-fr/

## 修复清单

### D1（P5 事实错误）
- content56.py P5 第 1 段：`cinquante ans avant Katniss` → `vingt-quatre ans avant Katniss`。
- 全刊 grep `cinquante`：仅此一处；其余事实（11 月 18 日、2 h 38、Francis Lawrence、16 岁）未动。

### D2（P6 Q84 无据可答，选修法 (a)）
- content56.py P6 日程图加一行：`26 nov. — Fin du délai de 50 jours (art. 47-1)`（插在 20 nov. 与 9 déc. 之间，按时间顺序）。
- 键 B 不变；Q84 题干/选项未动。P6 深读段未动（flow 余量仅 12px，加句会溢出）。

### D3（§8.1 词表词未进正文，13 词；全部用“写进正文”法，不删词表）
- P3 葡萄酒：`bouteille`（第 2 段：mettre leur vin en bouteille）、`raisin` + `vigne`（第 3 段：couper le raisin dans les vignes）。
- P4 网球：`tennis`（P1 段：dernier grand tournoi de tennis）、`adversaire`（P1 段：son adversaire, Ben Shelton）。
- P5 电影（8 词，含 public）：`salle`（dans les salles de cinéma）、`public`（le public a l'embarras du choix）、`réalisateur` + `scénario`（du réalisateur Francis Lawrence, dont le scénario raconte）、`écran`（sur grand écran）、`acteur`（l'acteur Denis Ménochet）、`actrice`（l'actrice Kristin Scott Thomas）、`séance`（新增句：Six films, six histoires : choisissez votre séance du mercredi soir.）。

### D5（P8 14 题缺徽章）
- content8.py 新增两个不注册的徽章绘制 helper（只画徽章，不动 REG）：
  - 完形 Q109–116：每条选项行行首画 chip（级别按 cloze_defs 登记），选项文字右移 72px；实测 3 行变两行，电池流 +77px。
  - 对话 Q145–149：G 区标题后加徽章条（chip + 题号，每行 3 枚，共 2 行）。
  - 写作 Q150：H 标题行首画 B1 chip，标题文字右移 72px。
- 配对共享一枚（22–25、49–52、73–76、85–88、140–144）不动。修后全刊徽章 120 → 134（= 150 − 16 共享）。
  注：PROOF-NOTE 称 de/ko 为 138 枚（“150 − 16”）算术有误，150 − 16 = 134；ko 的 138 来自另一套逐题 ex 结构，de 实测总数 127（与 fr 同结构，同样缺这 14 枚）。

### D6（P1 与 P2 题干重复 + 空格可填 le，改写 P1 题干）
- content12.py P1 Q2：`Le Sénat vote ___ 18 novembre.` → `C'est ___ que le Sénat vote, le 18 novembre.`
- content12.py P1 Q3：`Le beaujolais nouveau arrive ___ 19 novembre.` → `C'est ___ que le beaujolais nouveau arrive, le 19 novembre.`
- 键不变（mercredi / jeudi）；“le”无法填入（C'est le que… 不合语法）；与 P2 Q11/Q13 题干不再相同。
- 未选“P1 加指示”方案：改写题干同时解决重复与第二答案两个子问题，改动同样小。

### O5（顺手修，零风险才留）
- P7 gp5：`(关系代词) 。` → `(关系代词)。`（去空格，看重建后是否仍孤行；仍孤行则改回）。
- P2 Q18：`Dimanche, vous (regarder) les finales. → ___` → 去掉 `les finales.` 后的句号（`... les finales → ___`），看重建后填空线是否仍孤行；仍孤行则改回。

### O2（KIT 注）
- WEEKLY-KIT.md §三电影条：补“16 部”计数口径说明（filmscinema.fr 同日计数不稳定，未采用；六部点名影片已核实）。

### D4 不修
- 未动任何「第 N 版」「N 月 N 日」空格（协调员裁定）。

## 构建命令（与 KIT §五相同）
见下方各节日志。

## 门禁结果（2026-11-10 返修后，build-fix3/4）

### 构建与渲染
- `run.py`（build-fix3）：零 `FLOW OVERFLOW` / `TOO WIDE` / `NOSPACE`。终值：P1-headline 1505/1812，P1-budget 2242/2300，P1-quiz 2491/2560，P2-feature 289/1540，P2-ex 2332/2560，P3-main 565/2560，P4-main 771/2560，P4-micro 2188/2560，P5-main 735/2560，P6-deep 1288/1300，P6-ex 2402/2560，P6-opinion 1190/1300，P6-micro 1985/2560，P7-A2 950/1150，P7-B1 855/1150，P7-B2 1019/1150，P7-outils 949/1150，P7-phrases 1688/1830，P7-clinic 2140/2268，P8-battery 1428/1485，P8-keys 2026/2560，Hiroshige y=2035.55 已放置。
- `render.py`（render-fix1.log，rc 0）：大报版 PDF 30,446,210 B，SHA-256 `3833c9076893cd3be6c478407206d3540a4167d127acfba773be632f622dbcc5`，8 页 1462.5×2025pt；cards 8/8 重渲。
- `webpdf.py`（webpdf-fix1.log，rc 0）：网页版 PDF 2,203,259 B，SHA-256 `59341d013995a0841af8dc2148b5c85a9e8a047674f355e6895cb6f190b131b0`，8 页。
- `export47.py`（export-fix2.log，rc 0）：`.text.md` 46,095 B，SHA-256 `55295b25a5c23f6b1063947885878b8fefc42b8ce3934fece4d3e34dcaf3ed15`，38,989 字符，540 条目（原 538，+2 为 P6 图表新行两条 `p.text`），150 题齐全。旧版 45,758 B / `8c439b03…`。
- 订正 O5 实际修法：gp5 为删一字「……的那一个」→「……的那个」（实测 415.9px ≤ 422.5，单行）；Q18 去句号后 419.4px，单行。两者卡面均已目视确认。

### 机械门
- `occlusion_audit.py`（occlusion-fix1.log）：自检 OK（6 类阳性对照触发，干净对照静默），**0 flags**。`final-fr-occlusion.json` 内容不变（`flag_count: 0`）。
- `p8.py extract --total 150`（p8-extract-fix2.log）：印出注记集 **121/150**（parse: joined），`--json` 与 `final-fr-p8.json` 逐项相同（`new==old True`），注记集与全部键未变。
- `p8.py compare`（p8-compare-fix1.log）：**CLEAN**，121/121，missing=[] extra_count=0 keydiff=[]。
- `check_mcq.py`（check-mcq-fix2.log）：45 题体，1437 渲染行，**DEFECTS: 0，UNLOCATED: 0**（初版 1 个 UNLOCATED 为 `badge_opt` docstring 内引用题体样式的文本，已改写 docstring；重建后 SVG 哈希不变）。
- `freeze.py baseline`（freeze-fix1.log，从核心目录运行 `--build . --core-svg svg`）：工具报告 **`ok: 8`**，直接 SHA-256 比对 8/8（p1 `be2964d5713b`、p2 `5709e000bbd7`、p3 `7828cfe33118`、p4 `785f4561ff32`、p5 `fff2a8d3d7ac`、p6 `8e569290ac8f`、p7 `077ebc44cfe4`、p8 `24ea15398fffc`）。先前 0/8 为 OUT 路径 artifact（复本进 `<out>/build-copy/svg/`，比对却查空的 `<out>/svg/`）。`final-fr-freeze.json` 已刷新为本次工具输出（ok: 8）。
- 文字层：`pdftotext` 大报版与网页版各 46,353 字节、7,240 词，**词级多重集相等 True**。
- P8 最小字号（p8-font-fix1.log，`tools/venv` PyMuPDF）：468 个 span，最小 **11.62pt**（213 个 span 处此字号）≥ 9.75pt。
- 徽章数（SVG chip 矩形 rx="2.7" 统计）：P1 10、P2 12、P3 18、P4 15、P5 14、P6 15、P7 12、P8 38，**总计 134**（原 120，+14）；分级 A2 #5c6e30 50 · B1 #46581f 65 · B2 #37402f 19 = 150 − 16 配对共享题。
- 登记表：仍 150 题（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42），与基线一致。

### D3 严格验证（d3-verify-fix2.log）
- 词表框原文与署名「domaine public」精确剔除后，整词匹配：P3 bouteille/raisin/vigne、P4 tennis/adversaire、P5 salle/écran/acteur/actrice/réalisateur/scénario/séance 全部命中同页正文；P5「le public」以观众义命中（le public a l'embarras du choix）。**PASS**。注：第一次验证（fix1）因 pdftotext -layout 把词表框与正文拼在同一行，剔除不彻底，改用精确剔除重测后通过。

### D2 可答性验证
- P6 日程图卡面可见 7 行，含「26 nov. — Fin du délai de 50 jours (art. 47-1)」；Q84 题干「Cinquante jours, jusqu'au...」+ 桥接「读上图日程」→ 读者可从图推出 B（26 nov.）。Q84 题干/选项/键 B 未动。

### §1.1 重测（section11-fix2.log）
- 纸色 #fbfaf6 8/8 有，金色 #b49a4a/#b3a06a 0，旧纸 #f7f1e2 0，近黑 #2a2419/#2c2822 0，边缘 stroke-width≥2 0，「·」0，「　」P1 35/P2 33/P3 19/P4 29/P5 23/P6 24/P7 15/P8 181、.text.md 390、ABSTRACT 0。
- 字体（`<text>` 元素统计）：Newsreader 占拉丁文主体；Noto Serif CJK SC 跨度零拉丁字母（全为中文/「→」/「　」）；P2 band y=72、页脚线 2596、SVG 1950×2700 全 8 版；VOL.4 文本 11 处、VOL.5 9 处（合规的下一期指称）。
- 「　」计数说明：KIT 旧数 37/34/20/30/25/28/193 为另一口径；按 SVG 源码口径对第一轮 build-copy 重数，P1–P7 与返修后完全一致，P8 184→181 系 109/111/113 三条完形选项行折行时行尾分隔符被消耗，内容无缺失（新旧 P8 文本行逐项比对确认）。

### 8 版卡面目视（2026-11-10，cards/*.png）
- P1：Q2/Q3 新题干无误，刊头/议程/目录/快讯/闪电问答、图注、页脚均干净。
- P2：Q18 填空线已单行；Q11/Q13 未动；图与框无溢出。
- P3：bouteille/raisin/vignes 已进正文；词表 10 词可见；Q26/Q42 仍可答（见下）。
- P4：tennis/adversaire 已进正文；网球词表可见；Q44–48 选项整组完整。
- P5：D1 已改（vingt-quatre ans / réalisateur / scénario / grand écran / salles / le public / acteur / actrice / séance）；电影词表 8 词可见；Méliès 图与图注干净。
- P6：日程图 7 行，26 Nov 行居中位置正确；Q79–Q84 选项完整；Q84 可答。
- P7：gp5 单行；8 金句、诊所、园地、预告、Doré 图均在。
- P8：完形 8 枚徽章（级别与登记一致）、对白条 5 枚（A2/A2/B1/A2/A2）、写作 B1 一枚；答案区 1–150 齐全；Hiroshige 图已放置；页脚干净。

### 150 题逐题复核
- 键表：`p8.py extract --json` 与 `final-fr-p8.json` 逐项相同（121 注记 + 全部键）；compare CLEAN。
- 改动题复核：Q2/Q3 新题干只容 mercredi/jeudi（C'est ___ que… 结构，le 无法填入；日子与 P1/P6 事实一致）；Q18 仅去句号，键「Vous allez regarder les finales dimanche.」不变；Q84 键 B 不变，现可从 P6 日程图推出；Q26（1951 年获准提前售酒）与新正文一致；Q42（13 日）与「dès le 13 août」一致；Q62–Q69 与新正文一致（mercredi/prequel/Ménochet 等）；其余题干/键/注记均未动（登记表统计与基线相同）。

### 返修后观察（非缺陷，留待下一轮校对）
- Q130、P3 Q36/Q37、P4「LES CHIFFRES DU SPORT」框中文注记存在与 O5 同类的孤行填空线/标点，均为第一轮已有、非返修回归。Q130 实测 437.8px vs 422.5，删句号省 4.4px、去「→」前空格省 4.8px，均不足 15.3px，无零风险修法，故未动。
- KIT 已更新：§7 门禁输出（徽章 134、freeze 8/8、新 PDF 尺寸/SHA、.text.md 46,095 B、P8 字号 11.62pt、字体/全角空格重测数）、§8 第 4 轮记录；`final-fr-freeze.json` 已刷新（ok: 8）。
