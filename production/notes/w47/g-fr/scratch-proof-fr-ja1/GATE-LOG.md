# GATE-LOG — W47 fr-ja proof1（re-fanout #2 全部门禁独立重跑）

- 时间：2026-11-11（EST）；解释器：仓库 `tools/venv/bin/python`（Pillow 13.0.0）
- 探针：开工前核对三 SHA（印 `291a514f…` / 网 `031684fd…` / 文 `aca65425…`）与任务简报一致；核心 fix4 三 SHA 已核对（`a30af667…` / `56f50ca8…` / `52024e02…`）；核对后开工
- 前轮归档：`GATE-LOG-fanout1.md`（fan-out #1，印 SHA `b137834d…` 已失效）；本文件只针对 re-fanout #2
- 全部实测值均为本轮独立重跑，非采信 builder/协调员/前轮数据；fr 族无现成 check_s11.py/verify_ed.py，本轮在 scratch 内自写 `verify_fr_ja.py`（fr 适配版，en 原版未动）；重建在 scratch 副本 `rebuild/` 内，生产目录零写入

## 1. run.py 重建（①）

- scratch 副本重建：`run.py` rc=0，TOTAL 150（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42），0 FLOW OVERFLOW / 警告。日志 `rebuild-run.log`
- 8 个 SVG 与生产 SVG **8/8 字节一致**（`prod-svg-sha.txt` vs `rebuild-svg-sha.txt`）

## 2. freeze（②）

- baseline：`freeze.py baseline --build production/2026-w47/core-fr --core-svg production/2026-w47/core-fr/svg --out scratch/freeze`，rc=0，**8/8 字节一致**，核心 SVG 跑前跑后未变。日志 `freeze-baseline.log`
- diff：rc=0；每页增/减字符串 p1 +22/-23、p2 +35/-33、p3 +31/-32、p4 +40/-38、p5 +37/-34、p6 +26/-28、p7 +34/-34、p8 +120/-122；新增 CJK 共 **2329** 个字符（359 个不同字：假名 116、汉字 230、日文标点 13）。与 fan-out #1 的 2332 相比少 3 字，与三处句号修复串缩短一致。`freeze-diff.json` / `freeze-diff.log`

## 3. occlusion（③）

- `tools/occlusion_audit.py` 自检 6 类阳性对照全触发，**0 flags**，rc=0。日志 `occlusion.log`，`occlusion.json`
- 注：occlusion 对横向越框/盒标题溢出/盒底溢出有盲区——盒标题与 P7 披露框另由 PIL 真墨 + 交付 PDF 渲染像素核查（见 §7、§8），occlusion 0 未单独作证

## 4. p8（④）

- `p8.py extract --total 150`：核心与版均为 noted 121/150（parse: joined）；`compare` **CLEAN**（121/121，missing=[] extra_count=0），**keydiff=[150]**。`p8-ed.json` / `p8-core.json` / `p8compare.json`
- P8 印出答案逐条比对（本轮解析器，见 §13）：150/150 条目，键 0 差异、注 0 差异、裸键 0 差异（去空格比对）。`p8-notes-compare.json`

## 5. 印/网文字层（⑤）

- pdftotext 各 102,405 B；token 数 7192/7192，多重集与顺序完全一致。`print.txt` / `web.txt`（网 PDF 字节不复现、只比文字层）
- 另：U+FFFD 0 处；`next Sunday` fr 族 0 命中

## 6. P8 最小字号（⑥）

- PyMuPDF 实测 11.625pt（228 个 span 处此字号），≥ SOP §1.1 下限 9.75pt，且高于 11.25pt 目标值

## 7. 盒标题 PIL 真墨（⑦）

- 自写 `verify_fr_ja.py`：474 个盒内文本逐一测量，**0 越边**（A 节）；暗色盒标题 + 芯片 165 个，最小右余量 18.1 SVG px、最小左余量 17.3 SVG px
- 交付 PDF 像素核查（150 dpi 渲染）：134 枚芯片白字最小左右余量各 27 渲染 px（=17.3 SVG px，与 PIL 一致）；全宽带标题左右余量 L 47–54px、R 46px（P1 主带 R 953px，因右标题短）；P7 预告条 L 35px、R 64px
- `verify-fr-ja.log`：ALL PASS（62 PASS）；`boxtitle.json`

## 8. P7 披露框（re-fanout #2 复核点）

- 奶油盒 (989, 1878, 873×380)，底 2258.0；披露文 2 行，末基线 **2233.3**，基线清除 +24.7，desc-clear +18.8；PIL 真墨底 **2236.3**（re-fanout 报告称 2234.4，差 1.9px 为墨迹底口径差，仍清出盒底 21.7px）。裁图 `png-print/crop-p7-disclosure.png` 目视干净

## 9. 孤儿标点全扫 + 三处修复确认

- 全版孤儿标点行 **0**。Q36 (538.5, 1864.7)、Q37 (538.5, 1997.4)、Q130 (989.0, 843.0) 三处孤行填空线存在，坐标与核心全同（ja 版 +0 档），核心继承观察类（O1）
- 三处孤儿日文句号确认消失：P1 g1 `'primeur　le beaujolais ボジョレー。'`(556.5, 1336.9) 句号在行末；P4 `比較級（plus / moins）で文を完成しよう。` 单行 (538.5, 1693.2)；P6 `上のカレンダーを読んで答えを選ぼう。` 单行 (88.0, 1911.5)。裁图 `crop-p1-g1b.png` / `crop-p4-bridge2.png` / `crop-p6-bridge2.png` 均已目视
- 另：P3 (729.8, 1732.0) 与 P8 (1291.4, 1303.0) 的 `___` 节点为行内填空（与题干同基线），非孤行——检测器误报已修（见 §13）

## 10. Q148（re-fanout #2 复核点）

- 登记键 core 与 ja 均为 `devant le`；源码 `content8.py:176` 为 f-string `On se retrouve ({gnums[3]})___ cinéma?`；P8 SVG 联合文本含 `Onseretrouve(148)___cinéma?`；答案区含 `148. devant le（映画館の前）`；对白节点 (1439.5, 1324.7) 为 `(148)___ cinéma? — Oui, à 19 h 30. Bon`。题干无 `du`，落地

## 11. 新增 CJK 审计（日语读者版）

- 新增汉字中简体独用字 **0**（约 150 字简体独用表核查）；`国` 新增 0 个，`学` 新增 1 个（`学校` / `学んでいる`，日文用法）——简报称 SIMP_ONLY 检出 ['国','学'] 是误报（两者皆为日文新字体共用字）
- 25 个无假名语境汉字逐个目视确认皆为标准日文熟语：通算、日常生活、空欄補充、酒蔵、樽、前回優勝者/抽選/上映回、対戦相手、若者、俳優、監督、脚本、観客、基礎、訂正、選択肢、翻訳、一致/無一致、称（3人称）
- .text.md 全文简体独用字扫描 **0**（汉字总计 1219 字）；新增 CJK 皆为日文，无简体中文残留

## 12. §1.1 其余项

- 纸色 `#fbfaf6` rect ×8；颜色集与核心 19 色完全相同，无多无少；VOL.4/VOL.5 计数逐页与核心一致；徽章 134 枚 [10,12,18,15,14,15,12,38]，颜色多重集与核心逐页一致（A2 50 / B1 65 / B2 19）；P8 最小 SVG 字号 attr ≥13；全刊扫描 U+2019=0、U+00B7=0、金色=0
- ABSTRACT.txt（245 B）：日文单行——「アルカラスがパリ・マスターズで優勝し、上院は水曜日に予算を採決、ボジョレー・ヌーヴォーは75周年：日本語話者のためのフランス語週刊——150問、A2–B2、2026年11月16日〜22日。」

## 13. 150 题逐题核验（⑧，机械门禁查不出的键-题干错配，本轮人工覆盖）

- 登记表 REG（`dump_reg.py` 从两边构建副本进程内导出）：逐字段比对，**唯一差异 Q150 键**（core `開放題 — 要点見写作框，范文在第 8 版写作框内` → ja `自由作文 — 採点ポイントは枠内。モデルは8ページの枠内`，设计内读者语差异）；级别/分版/题型分布完全一致。`reg-core.json` / `reg-ja.json`
- 题干：.text.md 123 条题干逐字与核心相同；唯一 5 条差异 Q135–139 为翻译题题干本身（读者语提示句，设计使然），逐条手验键-题干契合（`verify_stems.py`，`stem-compare.json/log`）
- 答案：.text.md RÉPONSES 答案键剥离注记后与 REG 键 0 不符（Q150 除外）；P8 印出键 vs 登记键只允许设计内差异——p8.py keydiff 仅 [150]
- 注：150 条日语注记逐条读过（`reg-notes.txt`），键-注契合；D7 四词皆在法语正文出现（P1/P4/P6，见 PROOF-NOTE）；D8 `avoir lieu` 全版 0 处，P7 Q100 为 `en beauté：美しく締めくくる。`

## 14. 全页目视（⑨）

- 交付印 PDF 150 dpi 渲染 `png-print/p1.png`–`p8.png` 全部看完：P1 刊头/主带/Atget 照片+图注/QUIZ ÉCLAIR/页脚干净；P2 日常、Châtillon 照片、Q11–Q25 干净；P3 Moreau 画、Q26–Q43、ZOOM 框、Q36/Q37 孤行填空可见（继承观察）；P4 LES CHIFFRES 框、Q44–Q61、Q53–55 比较级、APRÈS LE VOTE 框干净；P5 Méliès 图、Q62–Q78 干净；P6 日程图 7 行（含 26 nov. 50 天期限）、Q79–Q96、APRÈS LE VOTE 框干净；P7 语法三栏、Doré 图、金句 Q97–Q104、诊所 Q105–Q108、LE COURRIER 框 + 披露 2 行、预告条干净；P8 完形 Q109–116、MCQ、阅读、短语、翻译、配对、对话 Q145–Q149（含 `(148)___ cinéma?`）、写作 + MODÈLE、RÉPONSES 全解答、Hiroshige 图 + 图注干净
- P1 照片白色小方块已排除：SVG 里无白色 rect 与照片区 (88,1874,873×320) 重叠；渲染照片区近纯白像素 0 个；200 dpi 裁图 `crop-p1-photo.png` 目视确认为 Atget 原照片内的白色墙牌/招牌内容，非版式缺陷

## 15. 检测器误报修复记录（非版面缺陷）

1. PIL `getbbox` 默认锚点 `la`（上行线）把墨迹盒整体下移一个 ascent（19px 字约 23px）→ 首版误报 154 处徽章越边（margin_B 统一 −15.0）与 P7 披露框超盒底；改 anchor=`ls` 后重跑：474 框内文本 0 越边，披露框真墨底 2236.3
2. 孤儿填空判定须看同基线有无其他文本；只看节点文本 `___` 会把 P3 (729.8, 1732.0) 与 P8 (1291.4, 1303.0) 两处行内填空误报为孤行
3. 跨行/跨节点 SVG 句子须拼接全文后查（Q148 对白、答案 `148. devant le`、多行键）；拼接时节点间空格常被断行吞掉，比对须用去空格归一化
4. P8 注记解析：`joined.find('RÉPONSES')` 会命中 P8 带标题 `EXERCICES & RÉPONSES`，改找 `全解答と短い注`；条目分隔符 `　`（U+3000）在注记内也会出现、换行处分隔符/空格会被吞掉（`22.a`、`vote100.`、`5. 12,7` 数字键）；最终分段用数字边界（前非数字、后接字母/假名/汉字/数字）+ 截断末尾图注后，150/150 0 差异

## 结论

全部 9 项门禁 + re-fanout #2 全部复核点 + 150 题手验均通过；**零缺陷，可定稿（a）**。观察项：O1 核心继承孤行填空（Q130/Q36/Q37，不修）；O2 D5 只记录、不修（本版无字体缺陷，见 PROOF-NOTE）。
