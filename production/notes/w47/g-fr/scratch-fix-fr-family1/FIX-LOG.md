# FIX-LOG — W47 fr 家庭重校 A1/A2/C1–C5 修复（家庭修复工人）

- 日期：2026-11-13（UTC）
- 任务：修复独立重校（工人 13b2bd13）发现的 A1、A2、C1–C5，涉及全部 11 版 fr editions；fr-ru 的门禁缺陷（occlusion 1 + boxtitle 4）与 B1 由另一名修复工人（scratch-fix-fr-ru2/）并行处理，本工人只做 A1/A2/C1–C5，fr-ru 单版重建与门禁由本工人统一做（在其改动基础上）。
- 依据：`~/workspace/weekly-git/SOP.md` §8；协调员 #4 run-log.md 2026-11-13 ~01:16 UTC 条；`scratch-reproof2-w47-fr/PROOF-NOTE-2.md`（第一轮 16 项已验）+ 本轮重校报告（run-log 尾部）。
- 约束遵守：**未 commit、未 push、未跑 lint**；未碰 fr 以外家庭、其他周；未 reset/stash/git add。
- 工具链：`~/workspace/weekly-git/tools/venv/bin/python`；门禁驱动 `scratch-d5-rebuild-fr/run_gates.sh`（run.py + render.py + webpdf.py + textlayer / occlusion / p8 / freeze / boxtitle / creambox / spill / edge / census 全套）；fan-out text.md 导出器 `scratch-fanout-fr/export_lang.py`；core 导出器 `scratch-fr/export47.py`。
- 修前基线（盘上实测，见 `pre-shas.txt`）：core 印 `f36c32f020e4`/网 `ff08e74903d6`/文 `52024e024d32`；en 印 `0503cff0885d`/网 `11e5babac345`/文 `82f53a7aa6af`；de 印 `234a877ebbbb`/网 `68c62c41b596`/文 `de37011a23a0`；es 印 `57d86cd14c5a`/网 `0f89bcd285da`/文 `d348eda26a40`；it 印 `179461e905ff`/网 `be09601e1dcf`/文 `0ca8ff5439bf`；ja 印 `f3f9d526f158`/网 `a1951960b852`/文 `d243033462d4`；ko 印 `acb99672c246`/网 `f7341f1a0a4f`/文 `4929e183f280`；nl 印 `c7e99156a889`/网 `d846793366f5`/文 `a5f5c7ebbfc8`；pt 印 `4a76ddaca94d`/网 `302da684a631`/文 `c7a3f3244476`；ru 印 `1aa7c71d7f2e`/网 `85c45f1cff46`/文 `028cb8c2d4b0`；zh-tw 印 `e6ef33ce2f62`/网 `0d6b19e48c69`/文 `3dc051e14be0`。（注：ja/ko/nl/zh-tw 文与 PROOF-NOTE-2 值不同——D5 重建后盘上值，以上为本次修前实测。）

## §1 逐项修法

### A1（全家共有，实质）—— P2 图注与图片不符
- 源：各版 `content12.py:184`（法语共享内容，11 版同一行）。
- 旧：`Châtillon, dans le Beaujolais : les vignes d'automne, au-dessus des caves où dort le vin nouveau.`
- 新：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- 依据：P2 唯一配图（pdfimages）为中世纪石砌城堡（圆塔、石墙、红绿爬藤），无葡萄园、无酒窖；地点分句保留，描述分句改为城堡，葡萄园语境保留在 `au cœur du vignoble`。

### A2（全家共有，轻微）—— P2 "DIRE LA DATE" 表缺 ven. 20 与 sam. 21 两行
- 源：各版 `content12.py` P2 日期表（加两行）+ 各版 `expl.py`（新增 `date_20`/`date_21` 译注）。
- 措辞照 P1 日记（CETTE SEMAINE JOUR PAR JOUR 议程框）同一两日写法，并与各版既有 `date_16..19/22` 风格及 P8 答案注既定译法一致（儿童节/减废周等）：
  - core：`11 月 20 日星期五　儿童节`／`11 月 21 日星期六　都灵半决赛 + 减废周首日`
  - en：`Friday 20 November: Children's Day`／`Saturday 21 November: Turin semi-finals + Waste Week begins`
  - de：`Freitag, 20. November: Kindertag`／`Samstag, 21. November: Halbfinale in Turin + Abfallwoche beginnt`
  - es：`Viernes 20 de noviembre: Día del Niño`／`Sábado 21 de noviembre: semifinales de Turín + comienza la Semana de residuos`
  - it：`Venerdì 20 novembre　Festa dei bambini`／`Sabato 21 novembre　Semifinali di Torino + inizia la Settimana anti-spreco`
  - ja：`11月20日金曜日　子どもの日`／`11月21日土曜日　トリノ準決勝＋ごみ減量週間初日`
  - ko：`11월 20일 금요일　어린이의 날`／`11월 21일 토요일　토리노 준결승 + 쓰레기 줄이기 주간 첫날`
  - nl：`Vrijdag 20 november　Kinderdag`／`Zaterdag 21 november　Halve finales in Turijn + Anti-verspillingsweek begint`
  - pt：`Sexta-feira 20 de novembro　Dia das Crianças`／`Sábado 21 de novembro　Semifinais de Turim + começa a Semana anti-desperdício`
  - ru：`Пятница 20 ноября　День ребёнка`／`Суббота 21 ноября　Полуфиналы в Турине + Неделя против отходов, 1-й день`
  - zh-tw：`11月20日星期五　兒童節`／`11月21日星期六　杜林準決賽＋減廢週首日`
- 几何（实测后定，见 §4）：行距 40→34；P2 练习区块 `ey = dy + 320` → `dy + 356`（下移 36）。"Exemples" 段与练习题均不删不改。

### C1（core-fr，印刷 PDF，2 处）—— P5 量词错
- 源：`core-fr/expl.py:127` `debat5_note` 一处源头（text.md L625/L665 两处均为此源）。
- 旧：`电影院还是家里？一张旧衣服的新主人，还是垃圾桶？` → 新：`电影院还是家里？一件旧衣服的新主人，还是垃圾桶？`
- zh-tw 已为 `一件舊衣服`，无需改。

### C2（core-fr，印刷 PDF，5 处）—— P8 E 节 135–139 题法语残留
- 源：`core-fr/expl.py:220–224` `stem_e1..e5`，删去 `Traduisez : ` 前缀，只留中文句子。
- zh-tw 无 `Traduisez`，无需改。

### C3（core-fr，印刷 PDF，2 处）—— P8 答案 120、131 术语
- 源：`core-fr/expl.py:328` `n_mcq_b4`、`339` `n_d2`：`半过去时` → `未完成过去时`。
- zh-tw 已为 `未完成過去時`，无需改。

### C4（core-fr，印刷 PDF）—— 三栏目共用 gloss "即学即练"
- 源：`core-fr/expl.py`：`head_avous` → `À VOUS !　轮到你了！`；`head_micro`/`head_micro6` → `MICRO-DRILLS　微练习`；`bridge_dieppe`（BEAUJOLAIS 小节副标题行）→ `博若莱新酒小测　博若莱新酒小题。`（只换 gloss 段，正文 `博若莱新酒小题。` 不动）。
- zh-tw 已区分（輪到你了！/ 微練習 / 薄酒萊小測），无需改。

### C5（core-fr，仅 text.md）—— text.md L3 法语残留
- 源：`scratch-fr/export47.py:54` 头行（core 导出器唯一源头），经重导出实现，未手改 text.md。
- 旧：`Semaine du 16 au 22 novembre 2026　150 exercices　A2–B2　正文法语　讲解简体中文`
- 新：`2026年11月16日至22日当周　150道练习题　A2–B2　正文法语　讲解简体中文`

### C6 观察项
- 不列为缺陷，未改。

## §2 每版改前 / 改后（尺寸 + SHA-256 前 12；全 SHA 见各版 WEEKLY-KIT.md）

| 版 | 印 PDF 改前 → 改后 | 网 PDF 改前 → 改后 | text.md 改前 → 改后 | text.md diff（vs 修前） |
|---|---|---|---|---|
| core-fr（zh-cn） | 18,475,436 `f36c32f020e4` → **18,488,281 `45745d5874df`** | 1,985,431 `ff08e74903d6` → **1,989,187 `9b66c0f91a68`** | 46,471 `52024e024d32` → **46,565 `9334d70437d3`** | 仅意改行（L3 C5、L55/341/467/581 C4、L231 A1、+8 行 A2、L375 C4、L539/771 C4、L625/665 C1、L1023–1031 C2、L1083 C3） |
| en | 17,031,641 `0503cff0885d` → **17,031,841 `b227430a9e54`** | 1,622,982 `11e5babac345` → **1,623,184 `167410e0620c`** | 46,146 `82f53a7aa6af` → **46,274 `f03b13d44104`** | 13 行（图注 1 行替换 + 日期表 8 行新增 + 3 行 hunk 头） |
| de | 17,035,304 `234a877ebbbb` → **17,035,455 `6c115f611991`** | 1,626,645 `68c62c41b596` → **1,626,804 `4eb86abfa6ee`** | 46,559 `de37011a23a0` → **46,690 `67148924c68e`** | 13 行（同上） |
| es | 17,031,455 `57d86cd14c5a` → **17,031,624 `b4fb751d7482`** | 1,622,809 `0f89bcd285da` → **1,622,990 `ec297b7cee22`** | 46,655 `d348eda26a40` → **46,808 `53603c0693ec`** | 13 行（同上） |
| it | 17,027,797 `179461e905ff` → **17,027,966 `a8c23cf15874`** | 1,619,126 `be09601e1dcf` → **1,619,307 `0e27ccb79bb9`** | 46,537 `0ca8ff5439bf` → **46,687 `51f32dd4e288`** | 13 行（同上） |
| ja | 20,149,418 `3121d66228dd`（旧记；盘上修前 20,149,490 `f3f9d526f158`）→ **20,150,788 `40fa2fb8bd61`** | 2,019,912 `8c52331f7ce6`（旧记；盘上 2,019,995 `a1951960b852`）→ **2,021,505 `4249702230de`** | 47,524 `354f6b094247`（旧记；盘上 47,548 `d243033462d4`）→ **47,687 `fdf935955f1e`** | 13 行（同上） |
| ko | 20,086,243 `bfeb8970f59f`（旧记；盘上 20,086,280 `acb99672c246`）→ **20,086,951 `827e6bb2d433`** | 1,923,201 `d972b7cbc104`（旧记；盘上 1,923,242 `f7341f1a0a4f`）→ **1,924,132 `00b0f37c9a45`** | 47,332 `fd2dfe488c05`（旧记；盘上 47,356 `4929e183f280`）→ **47,510 `b9e6af86a01e`** | 13 行（同上） |
| nl | 17,030,024 `45c0b11e87a7`（旧记；盘上 17,030,093 `c7e99156a889`）→ **17,030,275 `bc360a39096c`** | 1,621,399 `fb98be3aa292`（旧记；盘上 1,621,462 `d846793366f5`）→ **1,621,651 `408379aee377`** | 46,281 `ad506a852519`（旧记；盘上 46,309 `a5f5c7ebbfc8`）→ **46,452 `c5ce799c2e4e`** | 13 行（同上） |
| pt | 17,031,948 `4a76ddaca94d` → **17,032,129 `6aee0967dcfc`** | 1,623,288 `302da684a631` → **1,623,461 `88ece6e886a9`** | 46,494 `c7a3f3244476` → **46,656 `b61fe3b3189d`** | 13 行（同上） |
| ru | 17,222,281 `af7d37bc0a56`（fix-ru2 修后态）→ **17,222,512 `ade6694fcd1a`** | 1,773,854 `f6e82ee074cf`（fix-ru2）→ **1,774,107 `9de461db64ed`** | 50,475 `ae0a0429047a`（fix-ru2）→ **50,693 `69d348831b05`** | 13 行（vs fix-ru2 修后 text.md；图注 1 行替换 + 日期表 8 行新增 + 3 行 hunk 头） |
| zh-tw | 18,532,970 `3f4f58df81c3`（旧记；盘上 18,532,749 `e6ef33ce2f62`）→ **18,534,108 `cb5588ff6fcc`** | 2,076,083 `6972666e0e72`（旧记；盘上 2,075,855 `0d6b19e48c69`）→ **2,077,328 `3f66ddae87f4`** | 46,011 `e257f1023046`（旧记；盘上 46,008 `3dc051e14be0`）→ **46,129 `659dc0c5d5af`** | 13 行（同上） |

注：ja/ko/nl/zh-tw 的“修前”栏第一值为 PROOF-NOTE-2/FIX-LOG 记载值，括号内为本次修前盘上实测值（D5 重建后的盘上值，两者不同——本次修前基线以盘上实测为准，见本 FIX-LOG 顶部修前基线表）；§2 改后值均为本次修后盘上实测。ru 的修前基准为 fix-ru2 修后态（门禁修复工人 01:27 UTC 构建）。

## §3 门禁复核结果（逐版；日志在 `scratch-d5-rebuild-fr/<版>/logs-fixfam1/`）

注：`run_gates.sh` 的 FAILFLAG 只反映 run/render/webpdf 返回码，不代表门禁——以下结论以各工具日志为准。

- **core-fr — 全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心与 vs 修前基线，keydiff=[]）；boxtitle 0 DEFECT（40 titles）；creambox PASS 0 defects；spill 0（102 OBSERVE，均为已知 below-box 提示）；edge 0 TOUCH / 0 NEAR；census PASS（0/0/0）；freeze diff +0 CJK / +0 Latin；印/网文字层逐字节一致（各 100,873 字节，multiset 0）；P8 最小字号 11.62pt（858 spans）。text.md diff：L3（C5）、L55/341/467/581（C4 head_avous）、L231（A1）、+8 行（A2 ven.20/sam.21）、L375（C4 bridge）、L539/771（C4 head_micro）、L625/665（C1×2）、L1023–1031（C2×5）、L1083（C3×2，120/131 在同一长行内）——仅意改行。
- **en — 全绿**：run 0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0；p8 CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（34 titles）；creambox PASS；spill 0/102；edge 0/0；census PASS；印/网文字层逐字节一致（各 101,481 字节，100,259 字符）；freeze baseline ok:8（diff vs 核心为跨版 wholesale 值，非 FAIL 判据，见 ru2 GATE-LOG 同款说明）；逐页 SVG 哈希：仅 p2 变。
- **de — 全绿**：同 en（boxtitle 34 titles；spill 0/102；文字层各 101,133 字节，99,792 字符；仅 p2 变）。
- **es — 全绿，1 残留警告（修前已接受）**：boxtitle 0 DEFECT（38 titles）；spill 0/100；文字层各 101,067 字节，99,617 字符；仅 p2 变（vs freeze-fix1 基线；vs freeze-r2 的 p7 差异为 fix1 的 clinic 补译注态，非本轮所致）。1 HEAD TOO WIDE [P7-clinic] `CLINIQUE DES ERREURS　ERRORES` 445.2px——fix1 已接受（FIX-LOG §8：栏外伸入空白边距，无碰撞），本轮未动 P7。
- **it — 全绿，1 残留警告（修前已接受）**：boxtitle 0 DEFECT（38 titles）；spill 0/107；文字层各 103,150 字节，101,860 字符；仅 p2 变（vs freeze-fix1 基线）。1 HEAD TOO WIDE [P7-clinic] `CLINIQUE DES ERREURS　ERRORI` 423.4px——fix1 已接受（仅 0.9px 过栏）。
- **ja — 全绿，零警告**：boxtitle 0 DEFECT（41 titles）；spill 0/104；文字层各 101,179 字节，93,589 字符；仅 p2 变。
- **ko — 全绿，零警告**：boxtitle 0 DEFECT（47 titles）；spill 0/136；文字层各 101,987 字节，95,117 字符；仅 p2 变。
- **nl — 全绿，1 残留警告（修前已接受）**：boxtitle 0 DEFECT（38 titles）；spill 0/101；文字层各 99,680 字节，98,436 字符；仅 p2 变。1 HEAD TOO WIDE [P7-clinic] `CLINIQUE DES ERREURS　FOUTEN` 432.6px——fix2 已接受。
- **pt — 全绿，零警告**：boxtitle 0 DEFECT（36 titles）；spill 0/103；文字层各 101,013 字节，99,502 字符；仅 p2 变（vs freeze-fix1 基线）。
- **zh-tw — 全绿，零警告**：boxtitle 0 DEFECT（40 titles）；spill 0/104；文字层各 100,023 字节，93,565 字符；仅 p2 变。
- **fr-ru — 全绿（在 fix-ru2 修后态上重建）**：run 0 FLOW OVERFLOW、1 HEAD TOO WIDE（[P7-outils]，fix-ru2 已记录的修前已存在项）；occlusion 0 flags（ru2 的 P1 撞 gloss 回归未复现）；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（53 titles）；spill 0/151；edge 0/0；census PASS；印/网文字层逐字节一致（各 104,033 字节，96,948 字符；vs fix-ru2 的 +249 字符全在 P2，其余 7 页逐页长度不变）；freeze baseline ok:8，diff vs fix-ru2 基线仅 p2-vie.svg 变；creambox FAIL 3 defects——与 fix-ru2 裁定逐位相同的误报（P5 `debat5_note` 复文按精确文本匹配到第二处；字符串与坐标 y_base 780.6/811.0/841.5、y_patch 2326.6/2354.6/2382.6、box_bottom 887.9 与 fix-ru2 记录一致），独立 spill 门禁 0 SPILL。ru2 的 6 处改动在新印 PDF 文字层中逐项核实仍在位（头条去 MERCREDI、`DATES EN CHIFFRES`、`PHRASES DU COMMENTATEUR`、`CINÉMA DU MERCREDI　КИНО`、`DATES POUR COMPRENDRE`、Q141 `победитель`；旧串 `LES DATES EN CHIFFRES`/`LES PHRASES DU COMMENTATEUR`/`TROIS DATES POUR COMPRENDRE` 均为 0；`les vignes` 仅剩 P3 正文 1 处“dans les vignes dès le 13 août”，旧图注已无；`чемпион` 仅剩 g4 `действующий чемпион`，与 ru2 记录一致）。text.md diff vs fix-ru2 修后态 13 行（图注 1 行替换 + 日期表 8 行新增 + 3 行 hunk 头）。

## §4 A2 几何实测

- 修前实测（core 印 PDF 文字层，SVG 坐标）：日期表行墨高 30.8（基线间距 40）；"Exemples" 段单行，墨底 1865.4；下一分隔线 y=1878（间距 12.6）；P2 练习流内容底 2516（流限 2560）。
- 修后方案：行距 34（行间墨隙 3.2）；练习区块下移 36（`ey = dy + 356`）；"Exemples" 墨底 → 1903.4，距分隔线（1914）10.6；练习流内容底 → 2552，距流限 8。
- core 试点实测（印 PDF 文字层，SVG 坐标）：7 行日期表墨块 1635.6–1870.4；"Exemples" 墨 1882.9–1903.4（与预测逐值一致）；下一栏头 "EXERCICES" 墨顶 1921.5（距 "Exemples" 墨底 18.1）；门禁全绿（occlusion 0、spill 0、edge 0）；P2 卡面目视通过（见 §5）。方案确认可行，已推广至其余 10 版。

## §5 目视复核

- core-fr P2（`/tmp/fixfam1-core-p2.png`，150dpi 印 PDF 渲染）：图注 `Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.` 与城堡照片相符；DIRE LA DATE 表 7 行齐全、字迹干净、无溢出、无重叠；"Exemples" 行与 EXERCICES 栏头间距正常；右栏 LE SAVIEZ-VOUS / ET VOUS 框无位移。
- fr-ja P2（`/tmp/fixfam1-fr-ja-p2.png`，150dpi）：图注与城堡图相符；7 行日期表（日语译注）干净无溢出；"Exemples" 行与练习栏头间距正常。
- fr-ru P2（`/tmp/fixfam1-fr-ru-p2.png`，150dpi）：图注与城堡图相符；7 行日期表（俄语译注：ven. 20 `День ребёнка`、sam. 21 `Полуфиналы в Турине + Неделя против отходов, 1-й день`）干净无溢出；其余栏目无位移。
- 其余 7 版 P2 未逐版渲染目视：门禁全绿 + 逐页 SVG 哈希仅 p2 变 + text.md diff 仅意改行 + 三版抽查（core/ja/ru）均干净；几何方案三版实测一致（行墨隙、段间距、流底余量）。

## §6 KIT 更新记录

- core-fr：已更新（§一 P2 日期说法 16/17/18/19/20/21/22 日；§1.1 第 6 项「　」计数 P2 33→35、P5 23→22、P6 24→25、P8 182→180、text.md 390→392 + 成因注；§七印/网/text.md 字节+SHA、pdftotext 100,873 B、webpdf 文字 46,608 B、P8 最小字号 11.62pt/858 spans；§八追加 fixfam1 条目）。
- 9 个 fan-out 版 + fr-ru：已更新（各版 KIT 现值行：印/网/text.md 字节+SHA、pdftotext 字节数、text.md 字符数；文末追加 fixfam1 条目，含门禁逐项结果与三件新 SHA；历史条目未动）。fr-ru 的 Files 区括号已改为 fixfam1（注明 fix-ru2 值备查），文字层字符数更新为 96,948。

## §7 与 fr-ru 门禁修复工人的协调

- ru2 工人（scratch-fix-fr-ru2/）先行：01:25 UTC 开工，源改 6 处已完成（P1 标题去 MERCREDI、head_zoom/head_cine/head_3dates 去首词、m_p8b 141 改 победитель）+ text.md 重导出（恰 6 行）+ 重建门禁（01:27 UTC 构建）+ KIT 更新（01:35 UTC，GATE-LOG-fix-ru2.md）；本工人在其完成前未动 fr-ru 任何生产文件（01:20 UTC 只搭了空架目录 + 快照了修前 text.md）。
- 本工人 01:52 UTC 在其修后态上补 A1/A2：改动前核对 ru2 的 6 处源改均在位（content12.py:28、expl.py head_zoom/head_3dates/m_p8b）；text.md 差分基线重定为 ru2 修后 text.md（`ae0a0429047a`，原修前副本存为 `pre-textmd/2026-w47-fr-ru.text.md.pre-ru2`）；统一重建 fr-ru 一次（含 ru2 改动 + A1/A2），全套门禁重跑（见 §3 fr-ru 条），KIT 更新新 SHA + fixfam1 条目。无两个进程同时写同一版生产文件的时段。

## §7 与 fr-ru 门禁修复工人的协调

- ru2 工人（scratch-fix-fr-ru2/）先行：01:25 UTC 开工，源改 6 处已完成（P1 标题去 MERCREDI、head_zoom/head_cine/head_3dates 去首词、m_p8b 141 改 победитель）+ text.md 重导出（恰 6 行）+ 重建门禁进行中；本工人未动 fr-ru 任何生产文件。
- （待填：ru2 完成后，本工人在其改动基础上补 A1/A2、统一重建 fr-ru、跑全套门禁、更新 KIT。）

## §8 备注

- 未做：commit / push / lint（按任务约束）。
