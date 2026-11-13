# PROOF-NOTE — W47 fr-de (法语核心 × 读者德语) 独立复校 proof2（re-fanout #2）

- 复校员：独立复校（与构建者不同人），2026-11-11 15:00–17:00 EST 左右
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-de2/`
- 结论：**(a) 零缺陷，可定稿** — 全部机械门 + 目视 + 150 题手核通过，无缺陷。#1 的 D1（P7 盒底溢出）已修好并实测验证；#1 的 R1（Q148 核心继承错法语）已由 core fix4 + 本轮重建落地，三重核对通过。另有 3 项记录（不计入本版缺陷）：R1（P6 VOL.5 计数 +1，合法翻译）、R2（D5 字体，全线已知待定）、R3（孤行填空线观察项，核心继承）。
- 生产文件只读：复校期间未改 production 下任何文件，未 commit、未 push。确定性重建用 `tools/freeze.py baseline`（沙盒副本，见 GATE-LOG §3）。收工三件 SHA 与开工一致（见 GATE-LOG §0）。

## 身份核对（开工前实测，与任务书先验值一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-fr-de.pdf`（印刷） | 17,424,223 | `77842fe4dc5d162adc7f2b8694ad92e985fe83a1fcd9a49c2c3e3ae2886d8e7b` |
| `La-Lucerna-VOL4-fr-de-web.pdf`（网页） | 1,706,936 | `df62f6ee61ae8cc6cd57c837a4a2da74187f855b0d71d2c5a07751ebfb9fdf37` |
| `2026-w47-fr-de.text.md` | 46,632 | `d3735ef592bc02fcbe9712c3a184c2c2c963fd3fcfaf3311363ccf2baf95bc18` |

核心 core-fr fix4 复核一致：印 `a30af667…` / 30,446,975 B；网 `56f50ca8…` / 2,241,835 B；文 `52024e02…` / 46,471 B。

## 本轮必查项复核（全部通过）

### 1. P7 披露框（#1 D1 已修复，实测+目视双重确认）

- 位置：P7 右下 `LE COURRIER DES LECTEURS　LESERBRIEFE` 奶油盒（`p7-langue.svg`：`x=989.0 y=1878 w=873.0 h=380`，盒底 `y=2258.0`）。
- 内容：`courrier_disclosure`（`expl.py:182`）德文段已删中句 `diese Ausgabe druckt ein gekennzeichnetes Redaktionsbeispiel.`，现为 2 行（基线 2206.0 / 2233.3）。
- 实测（GATE-LOG §4，`creambox-proof2.log` / `pil_p7-proof2.log`）：
  - creambox 规范扫描：末基线 2233.3，清除 **+24.7**，desc-clear +18.8（#1 为 −2.6）。
  - PIL 真墨（印刷 PDF 200 dpi，字色 `#6f675d`）：真墨末行 svg y **2237.8**，距框底 20.2px；间隙 2258–2270 **零墨**。
  - 200 dpi 盒底裁切（`render/print/p7-box-crop.png`）：末行 `löst das Versprechen ein, echte Einsendungen zu kommentieren.` 完整在盒内，字形无裁切；下方白纸间隙干净，绿带未被侵入。
  - creambox_check 精炼版：**NO OVERFLOW**（`creambox-check-proof2.log`）。

### 2. Q148（#1 R1 已由 core fix4 落地，三重核对）

- 键 `devant le`、题干 `On se retrouve ___ cinéma ?`（无 `du`）：
  - registry 源：`content8.py:170` 键 `"devant le"`；`:176` 题干 `On se retrouve ({gnums[3]})___ cinéma ?`（与 #1 备份 diff 逐行核实，见 GATE-LOG §8）。
  - P8 extract：`p8-proof2.json` 键 148 = `devant le`（150/150）。
  - P8 SVG 文本层：含 `On se retrouve` + `cinéma ?` + `148. devant le`，不含 `du cinéma`。
  - text.md：`148. devant le (Vor dem Kino)`；对话区 `— On se retrouve (148)___ cinéma ? — Oui, à 19 h 30.`（P8 目视亦确认）。
- 填入后成 `On se retrouve devant le cinéma ?`，法语正确。#1 R1 关闭。

### 3. 孤儿标点全扫：新增 0

- 修正后 `check_extra.py`（同基线判定，与重建报告 §5 同法）独立重跑：`orphan_lines_total 0, new 0, inherited 0, remnant 0, shared_baseline 0`（`extra-proof2.log`）。de 版无字体分拆同基线项（拉丁版）。
- 孤行填空线：P3 Q36 (538.5, 1894.4)、Q37 (538.5, 2027.1)、P8 Q130 (989.0, 843.0)；与核心关系为 Q130 分毫不差、Q36/Q37 下移 **+30**（de/it/ru 档），与重建报告一致；观察类，不修核心、不判 (b)（见 R3）。

### 4. 150 键逐项手核 key-vs-stem（Q73 教训：三源一致也可能同错，故全文通读）

- `.text.md` 全文 1,089 行（实测 1,088 行）逐行通读 + P8 SVG 文本层对照 + `keycheck-manual.txt`（150 题题干/键/注记对照表）。
- 结论：**150/150 键与题干适配**，无问题。抽查要点：
  - Q1 `gagné`（`a gagné le Masters`）、Q11 `mercredi`（`vote mercredi 18 novembre`）、Q15–18 futur proche 变形、Q26–30 Vrai/Faux 与 P3 正文一致、Q38 `75 ans`、Q39 `minuit`、Q40 `troisième`、Q41 B、Q42 `13`（`dès le 13 août`）、Q44 B / Q45 A / Q46 C / Q47 A / Q48 A（11e journée 20–22 nov）、Q53 `plus vite`、Q54 `plus grand`、Q55 `moins longue`、Q56–61 填空与正文一致、Q62 B / Q63 B / Q64 B Dhont / Q65 A / Q66 A、Q67–72、Q73–76 a/b/c/d、Q77 `des billets` / Q78 `deux`、Q79–84 日历题与 P6 日历一致、Q85–88 a/b/c/d、Q89 `plus long` / Q90 `moins simple` / Q91 `aussi important`、Q92–96 微操、Q97–104 P7 句法题、Q105–108 改错句（107 `examine` 无 -s，虚拟式正确）、Q109 A（16 Nov 2026 确为周一）/ Q110 B / Q111 A / Q112 B / Q113 A（`Le cinéma propose` 单数主语）/ Q114 A（avoir 无配合 `aimé`）/ Q115 B（`jouent`）/ Q116 A（`il l'écrit`）、Q117 A / Q118 A / Q119 B / Q120 B `irais`（si + imparfait → 条件式）/ Q121 A / Q122 B / Q123 A / Q124 C、Q125–129 阅读题、Q130–134 句法改写、Q135–139 德→法翻译（137 `depuis lundi`、138 futur proche、139 `ne...pas encore`）、Q140–144 a/b/c/d/e、Q145 `des billets` / Q146 `deux` / Q147 `quelle heure` / Q148 `devant le` / Q149 `film`、Q150 开放写作题（读者语说明）。
  - 机械 keycheck（`p8_extract` vs core `final-fr-p8.json`）：仅 [150] 不同（写作题键为读者语说明），与预期一致。

### 5. 与 #1 备份回归对照（KEEP/REVERT 盘点，GATE-LOG §8）

- SVG 哈希：P1–P6 与 #1 **逐字节相同**；仅 P7（`4bc0ef75→700bee74`，披露框缩短）与 P8（`7e3269a2→660522e4`，Q148）变化——改动页与修复项一一对应，无多余改动。
- 源文件 diff（旧→新）：恰好 3 行——`expl.py:182` 删披露中句；`content8.py:170` `devant`→`devant le`；`content8.py:176` 删 `du`。其余 7 个 py 文件字节相同。
- KEEP：#1 的全部修复均保留——`Dhont` 在新旧 `expl.py` 各 1 处、`Dont` 0 处；`ABSTRACT.txt` 与 #1 备份字节相同（231 B，德语单行 + 换行）。REVERT：0 处。

## 其余手验（8 页逐页目视，印刷 PDF 150 dpi）

- P1：刊头、标题带（法文标题止 1236.9 / 德文带起 1337.5，净空 100.6）无重叠；HINWEIS 盒、LES DATES 盒、QUIZ 7–10 均正常；Atget 照片说明完整。
- P2：Châtillon 照片、LE SAVIEZ-VOUS / ET VOUS 盒、DIRE LA DATE 表、练习 A–D 均正常，无截断。
- P3：Q36/Q37 填空线独行（观察项 R3，见下）；ZOOM 盒、DATES 盒、BEAUJOLAIS-QUIZ 均正常。
- P4：LES CHIFFRES 盒德文注 2 行在盒内；Q44–61 均正常。
- P5：Méliès 图、LE CINÉMA DU MERCREDI 盒（德文注末行 `2 Std. 38 Min.` 余量 +24.0）在盒内；Q62–78 均正常。
- P6：LE CALENDRIER 盒德文注末行 `…in VOL.5.` 在盒内（余量 +20.0）；Q79–96 均正常。
- P7：见 §1；其余三栏语法区、BOÎTE À OUTILS、CLINIQUE DES ERREURS 均正常；左下空白为版式固有（核心同）。
- P8：见 §2；答案流 150 条完整；Hiroshige 图注完整。
- 网页 PDF 抽查（100 dpi，P1/P7）：与印刷版布局、图片一致；P7 披露框在网页版同样正常。

## 记录项（不计入本版 (a)/(b) 判定）

### R1 — P6 VOL.5 计数 +1（合法翻译，非缺陷）

- `check_s11_fr.py`（en 版脚本的 fr 适配，见 GATE-LOG 方法备注）初报 `p6-politique.svg: VOL.5 count core=0 ed=1`。
- 核查：核心 P6 日历盒中文注为 `本页日程为计划安排，18 日投票结果下期跟进。`（无 VOL.5 字样）；德文译为 `Geplantes Programm; Ergebnis der Abstimmung vom 18. Nov. in VOL.5.`——“下期”译作 “in VOL.5” 准确且符合全书体例（全书他处 “下期/VOL.5” 对应一致：P2 ET VOUS 盒、P4 À SUIVRE 盒均写 VOL.5）。全书 VOL 计数：核心 VOL.4 11 / VOL.5 9，本版 11 / 10，唯一差值即此一处。VOL.4 逐页计数与核心完全一致。定性：翻译等效，不修。

### R2 — D5 字体（全线已知待用户裁定的问题，只记录，不判定）

- 实测（`d5-proof2.log`，可见 `<text>` 段普查）：8 页共 Newsreader 946 段、Noto Sans CJK SC 695 段、Noto Serif CJK SC 17 段、DejaVu Sans 4 段、UnifrakturMaguntia 1 段。
- 其中 Noto Sans CJK SC 695 段中 **570 段含拉丁字母**（德语讲解层）；真实 CJK 字符为 0（仅 U+3000 分隔符；freeze diff 新增 CJK 共 7 个，全为 U+3000）。
- 核心对照：Noto Sans CJK SC 660 段，其中 438 段含拉丁字母。按任务书指示：只记录，不作本版缺陷。

### R3 — 孤行填空线 Q130 / Q36 / Q37（观察项，核心继承）

- P3 Q36/Q37 的 `___` 各独行一行（P3 目视可见，行首 x=538.5，无其他文字同行）；P8 Q130 的 `___` 独行于 D 节（`→ ___` 换行）。
- 坐标与核心关系：Q130 (989.0, 843.0) 与核心分毫不差；Q36/Q37 (538.5, 1894.4/2027.1) 相对核心 (1864.7/1997.4) 下移 +30，属读者语练习流排版所致（de/it/ru 档），与 #1 及重建报告一致。任务书定性为观察类，不修核心、不判 (b)，故本报告仅记录。

## 方法备注（复校员脚本适配，生产文件未动）

- `check_s11.py` / `verify_ed.py` 只有 en-family 版本，无 fr 适配版。本复校将二者适配为 fr 版（`check_s11_fr.py` / `verify_ed_fr.py`，存于本 scratch）：核心改为 core-fr、页名改为 p1-une…p8-exercices、P8 检查改为 fr 结构（完形空为 (109)–(116)，117–119 为独立 MCQ 题干；ÉCRITURE 标题；Q120 芯片为任一等级色）；`verify_ed_fr.py` 的答案解析限定在 RÉPONSES 块内并用前瞻终结符（初版正则因吃掉 U+3000 分隔符而隔项漏解析，143→150 始得全数——漏项为本复校脚本 bug，非版本问题；最终 150/150 且抽查键全部通过）。
- 初版 `check_s11_fr` 另报两项，均已核实为脚本适配假设不成立、非版本问题：(1) VOL.5 逐页相等假设——见 R1；(2) (117)–(119) 为完形空假设——fr 版 117–119 是独立 MCQ（P8 上有 `117.`/`118.`/`119.` 题干），已修正检查。
- fr 版无 `registry.json`（键源为 core `final-fr-p8.json` + P8 提取），且 `content12.py` 无 `phrase_panel` 调用（fr 系数据文件 + `bslib4` 绘图），故 en 版 verify_ed 的 registry / SAY-IT 两项不适用，已在适配版中以等效检查替代（text.md 150 答案解析、P8 最小字号、CJK 卫生）。
- 盒标题真墨扫描（`spill_sweep.py` §2）：初版单阈值在深色标题带上把带底误作字墨，多次误报。终版按每标题带区中位暗比判极性（白字深底用亮墨量），全部标题通过；唯一一处初版旗标（P7 底栏 `LA SEMAINE PROCHAINE…`）经核实为极性误判——亮墨实测止于 1621.7（余 240.3px），`text_w` 609.7 / 可用 849，两法一致通过。spill sweep §1（盒外整行）零候选。
- 构建报告 FANOUT-REPORT-fr2.md 中 fr-it 项提到的 `une actrice` vs 任务原文 `une attrice` 之差，与 fr-de 版无关（de 版 P5 词表为德语释义），本复校不涉及。
