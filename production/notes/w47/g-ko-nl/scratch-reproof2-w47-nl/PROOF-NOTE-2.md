# W47 nl 家庭第二轮独立重校 — PROOF-NOTE-2

- 校对员：第二轮独立重校员（全新工人，与建造者、修复者均不同；SOP §8/§8.4）
- 范围：`production/2026-w47/` 内 nl 家全部 11 版：core-nl（= nl-zh-cn 版）+ nl-de、nl-en、nl-es、nl-fr、nl-it、nl-ja、nl-ko、nl-pt、nl-ru、nl-zh-tw
- 日期：2026-11-12
- 依据：SOP.md 全文（§8 校对闭环、§1.1 视觉规范、附则一几何审计、附则二工具化、附则四 web PDF 文字层）；第一轮 PROOF-NOTE.md（2026-11-12）；修复记录 FIX-LOG.md（2026-11-12）
- 只读生产文件，未改任何生产文件；未 commit、未 push、未跑 lint
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof2-w47-nl/`（门禁 JSON/日志在 `mech/`）

## 总体结论：有问题（仅 low / trivial 级，无 MAJOR、无 MEDIUM）

- 新发现 **3 条**：low 2 条（#1 nl-de BRIEVEN 读者注释缺 "best P8 texts"；#2 nl-es Q140 源句 "sorpresa" 与版内术语 "surprise" 不一致），trivial 1 条（#3 nl-en L45 ASCII 直引号）。
- 第一轮可修项 1–7、10–17 **全部核实已在版**（见下表），无一回退。
- 机械门禁 **全部通过**：10 个 fan-out gates OVERALL: ALL PASS；core occlusion 0 flags、p8 extract 150/150；boxtitle 11 版 defects 0；spill_sweep 11 版 0 SPILL；pdf_edge_scan 11 版 ok（最小边距 ≥53.6pt，touch=0）。
- 目视抽查 6 页（pt P1、it P2、ru P1、ja P8、en P7、core P1）全部干净，修复点目视确认。
- 是否修 3 条新发现、由协调员裁定；本轮不制造决策。

## 一、指纹对照（自修复后无任何变动）

33 个文件 SHA-12 + 字节，与 FIX-LOG 末节总表逐一一致；全部印 PDF 均为 8 页。

| 版 | 印 PDF SHA-12 / 字节 | 网 PDF SHA-12 / 字节 | text.md SHA-12 / 字节 |
|---|---|---|---|
| core-nl | 0c5d63b942d2 / 13830540 | 2b6f223eaff9 / 1874709 | aa1f470353f9 / 44087 |
| nl-de | 97420549c81e / 12104230 | 2361bedfd4d5 / 1536341 | c1342c3fe20d / 46226 |
| nl-en | 1900408aabb9 / 12102278 | 7174a848673f / 1534350 | da6d999d5b51 / 45132 |
| nl-es | 2da02d5b3081 / 12107937 | 249fda66604b / 1540062 | 44fc3d5c4287 / 47649 |
| nl-fr | 08f57ec27d86 / 12106421 | 1b429a3ff61e / 1538511 | f1d1154442c4 / 47744 |
| nl-it | dc91af0aa78d / 12102273 | 9eff96cf487a / 1534364 | e9880da2da99 / 47194 |
| nl-ja | b886a483f641 / 18803540 | 2b38c2547606 / 1967732 | b7e5f5dc8b48 / 47804 |
| nl-ko | e7fa69a263fe / 13871386 | 218aebe12b4b / 1791786 | e13db87160d1 / 47576 |
| nl-pt | e2fe3b3a9568 / 12110707 | 40c51869695b / 1542854 | 67516e2163c8 / 47365 |
| nl-ru | bb407a7b067e / 12368148 | 1c13bb4f7311 / 1780327 | dd1c0c087c46 / 57909 |
| nl-zh-tw | 3fd293bfef56 / 13887537 | 542c6f1bc8e2 / 1976266 | bf1f627d1bbf / 44308 |

WEEKLY-KIT SHA 抽查（ja/it/pt/ru/zh-tw/en/core）与实际文件一致。另：本轮交接摘要中 nl-fr text.md 的 SHA-12 被误抄为 de 版的值（c1342c3fe20d），已当场重验纠正为 f1d1154442c4/47744，与 FIX-LOG 总表一致。

## 二、第一轮修复逐项核实（全部在版）

| # | 修复项 | 核实结果 |
|---|---|---|
| 1 | ja Q140 缺 surprise | 印 PDF 全文「小さな詩つきのサプライズを作ります。」；Q140 在版 |
| 2 | ja Pakjesavond 译名 | 印 PDF 新形 パッケスアーフォント ×7、旧形 パッケスアフォント ×0 |
| 3 | ja Q135 分隔符 | Q133–136 全角 ＋ 一致 |
| 4 | ko Pakjesavond 译名 | 印 PDF 팍예스아폰트 ×5、파크예스아본트 0 |
| 5 | ko Q135 分隔符 | Q133–136 全角 ＋ 一致 |
| 6 | it/pt [B1 · Cloze] 本地化 | "Cloze" 0 命中；"Testo con lacune" ×13、"Texto com lacunas" ×13 |
| 7 | ru P1 数字框截断 | 现为完整 `16 — november: Duitsland – Nederland in Berlijn (16 ноября: Германия – Нидерланды, Берлин)`，三行折行；目视确认 |
| 10 | zh-tw Pakjesavond 分裂 | 印 PDF 收禮夜 ×10、禮物之夜 0 |
| 11 | zh-tw 主詞/受詞分裂 | 印 PDF 主語 0、賓語 0、主詞 ×6、受詞 ×3 |
| 12 | en BRIEVEN 缺 best P8 texts | text.md L366 "No letters or best P8 texts yet — an example; VOL.5 next." 在位；en P7 目视确认 |
| 13 | core text.md 裸 VOL.4 行 | grep 无裸 VOL.4 行（rc=1）；text.md 431 行 |
| 14 | pt P1 kicker 重叠 44.4pt（MEDIUM） | kicker 止于 x=1014.6，日期始于 x=1039.5 → **间隙 24.9pt**；"LEEMWEEK" 合并 span 消失；目视确认 |
| 15 | pt 刊名未本地化 | 新 kicker "TODAS AS SEMANAS EM NEERLANDÊS"；目视确认 |
| 16 | it P2 标题重叠 1.8pt | 标题 "PAKJESAVOND IN 4 PAROLE" 止于 797.1，提问 "Wat hoort bij pakjesavond?" 始于 897.7 → 间隙 100.6pt；目视确认 |
| 17 | it P2 盒标题溢出 0.5pt | "NOTA" 止于 688.4，盒右缘 720.8 → 余 32.4pt；目视确认 |

奶油盒标题 `### ` 前缀（导出器曾三次丢失，已手工回补）——六处全部在位，且印 PDF P6/P7 均已呈现：

| 版 | L287 | L360 |
|---|---|---|
| it | `### VOOR OF TEGEN?　PRO O CONTRO?` | `### HET WOORD　PAROLA` |
| pt | `### VOOR OF TEGEN?　A FAVOR / CONTRA` | `### HET WOORD　PALAVRA DA SEMANA` |
| en | `### VOOR OF TEGEN?　FOR OR AGAINST?` | `### HET WOORD　WORD OF THE WEEK` |

## 三、文本全量通读

- core `2026-w47-nl-zh-cn.text.md` 全文 431 行通读（P1–P8）：事实、日期星期、算术（16 Nov→5 Dec=19 天、14→15 Nov=1 天、12:00–16:00=4 小时、2009→2026=17 年、荷兰进球 7–5、德国 5 分、图表 35+30+20+15=100、35+30=65）、动词形、P7 金句 8 条逐字出自本期且页码标注正确、Q137–Q140、范文实测 **81 词**、Q 编号连续（142 条编号行 + "25–28."/"141–144." 两组共 8 题 = 150 题）。无新问题。
- 10 版讲解层：`diff core-nl vs 各版`（每版 616 行）抽 `>` 行（每版 241 行）**全部通读**：de、en、es、fr、it、ja、ko、pt、ru、zh-tw。
- ABSTRACT.txt 11 版全部复核：读者母语、单行、无 ASCII 双引号、含刊名 + 目标语名 + A2–B2 + 150 练习 + 真实话题。ja 用 パッケスアーフォント、ko 用 팍예스아폰트（已统一）。
- 答案标记：11 版 text.md 本地化答案标记（— 答案：/— Antwort:/— Correct:/— Respuesta:/— Réponse:/— Risposta:/— 答え：/— 정답：/— Resposta:/— Ответ:）均为 **142** 条；pt 版无中文 "答案" 残留。
- KIT SHA 抽查：ja/it/pt/ru/zh-tw/en/core 的 WEEKLY-KIT.md 所载 SHA 与实际文件一致。
- text.md 与 PDF 一致性抽查：it/pt/en 奶油盒标题在印 PDF P6/P7 呈现；zh-tw P8 Q137–140 方向标注正确；ja P8 答案区译名统一。

## 四、新发现（共 3 条）

| # | 严重度 | 版 / 位置 | 发现 | 证据原文 |
|---|---|---|---|---|
| 1 | low | nl-de / BRIEVEN 读者注释（text.md L366） | 读者注释未提 "best P8 texts"，与 en 版（刚修好）及 es/fr/it/pt/ja/ko/ru/zh-tw 均含此句不一致 | de: "Keine echten Briefe — Beispiel; Versprechen für VOL.5."；en: "No letters or best P8 texts yet — an example; VOL.5 next."；同框荷兰语核心行 "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.5." 在 11 版中均在位，信息未丢失，仅读者注释层缩写不一致。第一轮问题 12 曾称 de 含此句（实指荷兰语行）；FIX-LOG 亦已注明 de 读者行同样未提但未派修 |
| 2 | low | nl-es / Q140 源句 | 源句用 "sorpresa"，而版内术语为荷兰语借词 "surprise" | es Q140: "Hago una sorpresa con un poema corto."；Q14 答案注释: "Un surprise es un regalo disfrazado"；词表: "regalo disfrazado"。答案附注 "(surprise: expresión fija; corto = kort)" 起了桥接作用，学习者仍可推出答案。fr "Je fais une surprise" 因法语词形与荷兰语借词相同、无此可见差异 |
| 3 | trivial | nl-en / text.md L45、印版 P1 SVG | ASCII 直引号，与其余 10 版同行的排版引号不一致 | en: `"Group win": first in the group.`（text.md 与印版 P1 SVG、Newsreader 字体均为直引号）；其余 10 版同行均用排版引号（core “小组头名”、de „Gruppensieg“、es/fr/it/pt/ru «…»、ja/ko/zh-tw 「…」）。内容正确，仅排版不一致。直引号 " 全家仅 en 有 2 处（即 L45 一对） |

## 五、观察项（非发现，不派修）

- core ABSTRACT.txt 仍未写明 "16–22日" 周次（第一轮已记的 minor，未变；其余 10 版均写明）。
- it boxtitle P6 标题 "DATI INVENTATI"：MARGINAL，右缘超框 0.6px（工具容差 1.0px 内，core_over −22.0），亚像素级，目视不可见。
- nl-ru 拉丁标题字体问题（第一轮问题 8 MEDIUM、问题 9 low：拉丁文用了 Noto Sans 而非 Newsreader、P8 答案用 Noto Serif CJK SC）——已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py；本轮 D5 census 自写 SVG font-family 直计：除 ru 外全部版纯拉丁文本落入 Noto Sans = 0、弯引号落入 CJK 字体 = 0；ru 为 329（第一轮方法计 338，方法口径差异）。**不作新发现**。

## 六、逐版门禁结果

gates.py（10 个 fan-out，串行，`mech/gates-<lang>.log`）：**全部 OVERALL: ALL PASS**，无一 FAIL。每版均含：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiffs=2，即 137/138，翻译题答案本就应用读者母语）；freeze 8/8；印/网文字 posdiff 0、msdiff 0，8 页；pdftotext 印=网（字节相等）；P8 答案区最小 10.12pt；chips = core {A2:8, B1:24, B2:3}；§1.1 clean。

| 版 | gates | occlusion | boxtitle | spill | edge | 逐版结论 |
|---|---|---|---|---|---|---|
| core-nl | —（PDF 命名不同，gates.py 不适用） | 0 flags | defects 0 | 0 SPILL | ok（min 54.0pt，touch 0） | 通过（无新发现） |
| nl-de | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 54.0pt，touch 0） | 通过（新发现 #1 low） |
| nl-en | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 53.6pt，touch 0） | 通过（新发现 #3 trivial） |
| nl-es | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 53.6pt，touch 0） | 通过（新发现 #2 low） |
| nl-fr | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 53.6pt，touch 0） | 通过（无新发现） |
| nl-it | ALL PASS | 0 flags | defects 0（1 MARGINAL 0.6px，见观察项） | 0 SPILL | ok（min 53.6pt，touch 0） | 通过（无新发现） |
| nl-ja | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 54.0pt，touch 0） | 通过（无新发现） |
| nl-ko | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 54.0pt，touch 0） | 通过（无新发现） |
| nl-pt | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 53.6pt，touch 0） | 通过（无新发现） |
| nl-ru | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 53.6pt，touch 0） | 通过（无新发现；字体问题属已知跨家 D5，不重报） |
| nl-zh-tw | ALL PASS | 0 flags | defects 0 | 0 SPILL | ok（min 54.0pt，touch 0） | 通过（无新发现） |

补充：core p8 extract 150/150；core occlusion 自测通过（6 类 planted flags 全触发，clean controls 静默）；D5 census（自写 SVG font-family 直计）：弯引号总数 core 2、de 1、其余 0，全部在 Newsreader 内；引号普查（text.md）：直引号 " 仅 en 有 2 处（即 #3），其余版 0；«» 每版 70–72，ru 92。head_check 无可扫描内容（本轮无重渲染、无 run.py 日志留存；第一轮同样记过跳过）。d5_creambox_audit 需 pre-fix baseline，本轮无 baseline，未跑（第一轮同样）。

## 七、已排除（不要重报，核实无问题）

- FIX-LOG 已裁定不修：18/19/20（正余量偏紧：pt P2 余 2.0pt、es P7 余 2.6pt、pt P6 余 2.4pt）、21（观察项）、ko 括号前缺空格的系统性习惯。
- 第一轮已核查为非问题的项（本轮未再发现反证）：ru "башмак" vs "ботинок" 同义词、ru Q139 "(88-й)"、Q140 "(surprise (фикс.))" 简略、fr Q136 缺 "+ manner"、pt Q122 保留荷兰语河名 "Maas"、it Q134 "(S + V + C + luogo)"、de Q31 "legt um 10:15 Uhr in De Omval ab" 略别扭、en "de intocht arrival"、P3 图注 "voer"、P5 全角括号、fr Q139 "L'arrivée à Amsterdam"、P4 词库跨栏断行、fr 刊名短名/全名、ru P1/P2 疑似粘连（测量假象）、es/pt P2 间隙 0.0（尾随空格假象）、CJK/俄语版碰撞扫描假象、ja P1 kicker 间隙 4.5pt、P8 keydiff 137/138（翻译题答案本就应用读者母语，非失败）。

## 八、目视抽查

100 dpi 渲染 6 页（已按磁盘纪律清理，见末节）：pt P1（顶行间隙、刊名本地化 ✓）、it P2（标题间隙、NOTA 盒内 ✓）、ru P1（数字框三行完整 ✓）、ja P8（Q140 サプライズ、译名统一 ✓）、en P7（BRIEVEN 含 best P8 texts ✓）、core P1（顶行间隙 ✓）。6 页均无溢出、重叠、截断。

## 九、磁盘

开工 94G/150G；结束 95G/150G（<100G 门限）。渲染图 `pages/`（6 张，约 6.5MB）已清理；`mech/`（门禁 JSON/日志、diff、expl）保留。
