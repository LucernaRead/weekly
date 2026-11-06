# WEEKLY-KIT — Lucerna Weekly VOL.2 · W45 · Japans × Nederlands (JA×NL)

**Status: builder-complete — NOT finalized.** 本版已通过全部构建门禁，但按 SOP §8.4 仍需一次全新独立校对（fresh full independent proofread）后方可定稿交付。本 KIT 不宣布定稿。

- 刊期：2026 年 11 月 2–8 日（W45，杂志模式：10 月 26 日当周生产，11 月 2 日前完成）
- 配对：目标语 = 日语（文章全部为日语原文）；读者母语 = 荷兰语（讲解层全部为荷兰语）
- 来源：W45 日语核心 `files/weekly-report-w45-ja-core/`（只读参照，未改动）
- 交付目录：`files/weekly-report-w45-ja-nl/`（svg×8、cards×8、印刷 PDF、网页 PDF、本 KIT、ABSTRACT.txt）
- 构建树：`hidden_files/weekly-report-w45-ja-nl-build/`（transform.py、gen_nl.py、run.py、render.py、svglib.py、bslib4.py、content*.py、assets/、各轮 sha256 基线与审计 JSON）
- 交付动作：无。未发 Discord（投递暂停令仍有效）、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git。

## 1. 家具（以 W43 同配对实测为准，优先于 README §20 泛化）

W43 同配对参照：`files/weekly-report-ja-nl/`（VOL.1 已交付版）的 SVG 实测。

- 刊名：Lucerna（无冠词，日语目标族规则）；**刊名 y=248**（W43 同配对实测；README §20 泛化写 262，本版不采纳——见 §10 偏差 1）
- 副标题 y=316：`日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間`
- Badge（P1，19pt sans bold，砖色 #a4553a，y=356，逐字 = W43）：
  `TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`
- 标语 y=390：`日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で`
- 规则线 406/413；暗带 424
- 顶条中段（W43 措辞）：`毎週、日本語で · Elke week · 日本人が読んでいる日本語を読む`
- 页脚（每页，y=2624）：`Lucerna · JAPANS WEEKBLAD VOL.2 · TEKSTEN IN HET JAPANS · UITLEG IN HET NEDERLANDS`（W43 为 VOL.1，本版 VOL.2）
- 页码行：`Pagina N van 8`；gloss 前缀：`Uitleg — `；P8 答案分区隔：`— Pagina N —`
- 章节名荷兰语半句（W43 措辞复用）：トップニュース · Hoofdnieuws；数字で見る今週 · In cijfers；今すぐ練習 · Meteen oefenen；この号の内容 · In dit nummer；今週のことば · Woord van de week；短いニュース · Kort nieuws；クイズ · Bliksemquiz；あなたは？ · En jij?；季節のことば · Seizoenswoorden；日本シリーズの日程 · Schema；グラフを読もう · Lees de grafiek；練習用データ · Oefengegevens；ことば · Taal；言語フォーカス · Drie niveaus, drie thema's；まちがい診療所 · Foutenkliniek；今週のフレーム · De zin van de week；読者の手紙 · Lezershoek；今週のフレーズ · Zinnen van de week (letterlijk uit dit nummer)；テストと答え · Toets en antwoorden；若者・エンタメ · Jongeren；P4 带题 `スポーツ · 体育` 原样保留（体育为日语词，各 JA 分版皆然）
- 练习类型名（W43）：zinnen aanvullen / meerkeuze / gatentekst / combineren / waar of onwaar / zinnen bouwen / vertalen / schrijven
- 指令词（W43）：Vul in；Bouw een zin；Schrijven；Waar of onwaar?；Koppel woorden aan betekenissen；Koppel activiteiten aan plaatsen en tijden；Vertaal
- P8 带右侧（W43 NL 措辞，见 §10 偏差 2）：`Pagina 8 · 週の大きなテスト + 全ての答え`
- 答案区标题：`答え · Antwoorden — gegroepeerd per pagina: zoek je nummer op`
- 答案注脚行：`Bij elk antwoord een korte notitie in het Nederlands · ✓ = de vraag met de voorbeeldtekst`
- 练习区标题：`練習 · Oefeningen van pagina N`，右侧行：`Antwoorden op pagina 8 · Niveaus gemengd: zoek je nummer op`

## 2. 计数（= 核心，全部实测）

- 练习总数 150，连续编号 1–150；级别 A2 46 / B1 75 / B2 29
- 页分布 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38（P1–P8）
- 范文 167 字（按字数）《私の11月の週末》，P8 H 区逐字 = 核心（MODELO 未经 transform 触碰；构建树 content8.py 与核心 build 的 MODELO 字符数同为 167）
- gloss 渲染计数（按 `·` 本身切分，源文件分组 13+15+11+0 是另一口径，不得引用为渲染结论）：**39 = P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4**；核心与本版逐项同数（content12 4+4+5、content34 4+4+4+3、content56 4+3+4）
- P7 词框 gloss：A2 3 / B1 3 / B2 3（日语词头逐字 = 核心，仅荷兰语释义本地化）
- P7 金句 8 句：去空白拼接口径下每句全版恰 2×（文章内 1× + P7 列表 1×），核心与本版同为 [2,2,2,2,2,2,2,2]；页签 `(Pagina N)` 分布：P1×2、P2×2、P3×1、P4×1、P5×1、P6×1
- P8 印刷笔记口径 150 条（核心 P8 本身印 150 条；不得抄 EN 族的 78）

## 3. 改了什么 / 没改什么

改动仅限家具层与讲解层（荷兰语 apparatus + 注释本地化）；日语正文零删失。

- 讲解层：全部中文注释 → 荷兰语；全部中文家具半句 → 荷兰语（W43 措辞）；类型名、指令词、页脚、页码、分隔符、gloss 前缀全部荷兰语化
- P7 词框目标语定义句逐字冻结，仅 gloss 荷兰语化（freeze diff P7 移除项全部为中文讲解层与家具，无一句日语定义句被移除；P7 增加项 38 条，均为荷兰语 apparatus 与已在核心的日词头）
- E 区重定向（JA↔ZH → JA↔NL）：
  - #137 键 → 荷兰语：`Cultuurdag is op 3 november.`（指令 `Vertaal naar het Nederlands`）
  - #138 键 → 荷兰语：`Wie afval op straat gooit, krijgt een boete van 2.000 yen.`（指令 `Vertaal naar het Nederlands`）
  - #139 题干 → 荷兰语提示：`De Leesweek begint op 27 oktober. → ___`，键逐字 = 核心日语 `読書週間は10月27日から始まります。`（指令 `Vertaal naar het Japans`）
  - #140 题干 → 荷兰语提示：`Ik wil naar Kobe om de herfstverlichting te zien. → ___`，键逐字 = 核心日语 `神戸の紅葉のライトアップを見に行きたいです。`（指令 `Vertaal naar het Japans`）
  - 方向指令由 transform.py 主流程后处理实现：扫描 content8.py 中 `instr="Vertaal"` 且含 `→ ___` 的行，题干以拉丁字母开头者（139/140）→ `Vertaal naar het Japans`，题干以日语开头者（137/138）→ `Vertaal naar het Nederlands`，断言恰为 (2, 2)
- #150 登记行与写作说明荷兰语化：`(open opdracht — voorbeeldtekst hieronder)`；注 `Voorbeeldtekst in deel H van deze pagina (167 tekens)`；说明 `Schrijfopdracht (geen enig juist antwoord); de voorbeeldtekst (167 tekens) staat hieronder.`
- P8 #37 裸串陷阱（JA 族常驻陷阱，本版已显式处理）：核心 content34.py:82 把 #37 提示登记为裸串 `工艺展到11月8日`（无星期后缀；P3 填空题，键为 8），NOTES 表中只有带后缀的 `工艺展到11月8日（周日）` 与另一题的 `传统工艺展到11月8日`。transform.py 显式映射：裸串 → `De tentoonstelling loopt tot 8 november`；带后缀 → `De tentoonstelling loopt tot 8 november (zondag)`；`传统工艺展到11月8日` → `De tentoonstelling loopt tot 8 november`（与裸串同渲染是正确的，因两题答案相同）。事实核对：展览至 11 月 8 日（周日），P3 原文 `展覧会は11月 ___ 日（日）までです。`，2026-11-08 确为周日
- 匹配指令缩短（P2 与 P8）：`Koppel woorden aan betekenissen` → `Combineer`（仅 content12 与 content8；P3 保留完整形 `Koppel activiteiten aan plaatsen en tijden`，W43 先例）
- P8 注释缩短（第 2 轮，见 §8）：气温注（#14 与 #83 两处）→ `Temperaturen november–januari hoger dan gemiddeld`；文化日注（#6）→ `Op Cultuurdag overal culturele activiteiten`；2–0 夺冠率注（#50）→ `Teams met een 2–0-start worden in 73% kampioen`；守って注（#80）→ `守って + 〜しましょう = regels volgen, laten we…`；第 3 轮 #115 注 → `Japan Series wedstrijd 1 was op 24 oktober (zaterdag)`（均无语义损失；备选 #96b 因丢弃“较去年”基线被否决，#88/#66 留作备用未用）
- 读者来信角披露（第 2 轮 v6，5 个换行行，sans 20、宽 390 下以 svglib wrap 实测）：`Voorbeeldbrief, geen echte brief. Er waren nog geen echte brieven of beste P8-opstellen binnen; beide verschijnen in VOL.3. Stuur je Japanse brief op — gekozen brieven komen in VOL.3!`（含 3 事实：示例非真信、无真信、无最佳 P8 作文 + 明确祈使征集 + VOL.3 承诺；teaser 行是内容预告，不计作征集）
- 未改动：全部日语文章、练习题干、选项、范文、图片 payload、核心目录、W43 目录、canonical svglib（md5 见 §6）

## 4. 主题与来源（继承核心，已核实）

- 11 月 3 日文化日（周二）+ 11 月 7–8 日周末红叶（宫城县鸣子峡 10 月 31 日–11 月 8 日周末为高峰、神户布引香草园 11 月 7 日起灯饰至 12 月 28 日）+ ゆる整え食趋势（味之素 10 月 21 日发布）+ 读书周进行中（10 月 27 日–11 月 9 日）+ 11 月 7 日立冬（周六）
- P4 日本系列赛：G1（10 月 24 日周六，横滨，软银 3–1 DeNA，延长 11 回）与 G2（10 月 25 日周日，横滨，软银 4–3 DeNA，延长 10 回）已核实；G3–G7 仅赛程，页上明确延期至 VOL.3 汇总
- 10 月 31 日万圣节为刚过去事件；P6 练习图表 近場の満足 38 / 温泉 27 / 紅葉 21 / グルメ 14 = 100，页上明确标注为练习数据（非真实调查）
- P7 结构：A2 栏 本と読書のことば / B1 紅葉のことば / B2 数字を読む + 诊所 4 项 + 框 『ゆるく整える』 + 读者来信角（编辑示例 + 页上荷兰语披露）+ VOL.3 预告；P8 A–H 区
- 图片 4 张（payload = 核心，见 §6）：P1 红叶（CC0，Poliphilo）、P3 歌川广重三代版画（PD）、P4 球场（CC0，Syced）、P5 南瓜（PD，Petr Kratochvil）；credit 均取自 Wikimedia Commons API Artist 字段且每张已实际放置；P2/P6/P7/P8 无配图（与核心一致）

## 5. 读者来信角裁定

- 日语例信逐字冻结，零编造（无人名、信件、引言被发明）
- 核心日语披露行被替换为荷兰语披露作为有效披露（荷兰语读者无法阅读日语披露；核心中文披露已移除），teaser 行不计作征集
- 荷兰语披露 v6 含全部 3 事实 + 祈使征集 + VOL.3 承诺（见 §3），目视确认 5 行完整位于读者来信角框内

## 6. 门禁实测值（全部通过）

- 核心基线：`tools/freeze.py baseline` 8/8 逐字节（开工前与第 3 轮后两次）；交付后核心 SVG 重新哈希无变化
- freeze diff（`--strict-cjk`，`freeze-diff-final.json`）：新增 CJK 0（8 页全部）；CJK 总量核心→本版：P1 1406→1275、P2 1312→1161、P3 1172→1051、P4 1263→1169、P5 1247→1132、P6 1186→1101、P7 1676→1306、P8 2721→1445（减少量 = 被移除的中文讲解层）
- 禁用的中介层术语扫描：SVG + 构建代码 + ABSTRACT 全文 0 命中（以字符转义方式扫描，术语原形未写入任何构建文件；本 KIT 自述亦不含其原形）
- P8 比较（显式双路径 p8.py，`p8-final.json`）：**CLEAN，150 = 150，missing []，extra []**；keydiff 21 项，裁定见 §7
- P8 注释完整性比较（`audit_suppl.py`）：核心与本版 P8 相同独立行 108 条，逐条裁定全部为冻结日语（题干、选项、级别徽标、数字、区标题、范文片段），其中无任何中文注释；150 条答案注释全部本地化（核心与本版完全相同的答案行：0 条）
- 词级中文残留重扫：本版 CJK 连续串（长度 ≥2）中不存在于核心全文者：0 条（字符扫描会漏共享汉字中文词，故以词级重扫为准）
- 几何（canonical `tools/occlusion_audit.py`，自检 6 类全部触发，`occlusion-final.json`）：本版 0 告警、核心 0 告警、NEW（本版相对核心新增）0
- ADVANCE 法全页右缘扫描（限 1885.5）：0 违规；全页框线扫描：0 命中；P1 顶带墨迹间距：左 65–220（VOL. 2 · 第2号）、中 675–1275（顶条行）、右 1530–1885（日期行），无碰撞
- P6 图表标签基线锚定墨迹覆盖：MAX 0.000（门 <0.30；未用 getbbox 法）
- 行首 kinsoku：0 命中（NO_START 取自 svglib.py wrap 函数原文 `"。、，．！？：；）」』】ー…‥・"`）
- P8 答案流末端：#150 于 2530.73（<2540）；P7 预告末端 2524.12（<2540）；构建日志零 `!!` 告警（无 FLOW OVERFLOW、无 HEAD TOO WIDE）
- 图片 payload（解码后 base64 的 sha256 前 12 位，核心 = 本版）：P1 `140f46d9e41b`、P3 `e293b32d5911`、P4 `19990669abb5`、P5 `6242ca640af3`；P2/P6/P7/P8 无内嵌图；credit 行核心 = 本版（逐页相等）
- 家具计数：badge 1（P1 徽章串另在页脚出现一次，故 P1 子串计数为 2，属正常）；页脚 8、页码行 8、P8 分隔符 8、gloss 前缀框 10（P1×1、P2×2、P3×2、P4×2、P5×2、P6×1，与 W43 的 10 框一致；P7 的 `Uitleg:` 框注为另一形式，不计入此 10）
- svglib md5：`d73e23b365676c3618d7e060b835eb4d`（canonical，未编辑）；kinsoku + SEAM_SLACK=28
- 确定性重跑：构建完成后以 venv run.py 重跑，8 张 SVG 逐字节 = 第 3 轮结果（`sha256-rerun-check.txt` 对照干净）
- 目视：全部 8 张卡片逐张目视（p1–p8），无溢出、无重叠、无裁切标签、无错位框；重点复查 P2 匹配指令 `Combineer`、P8 F 区、P7 读者来信角与预告带、P1 刊头/badge/标语几何，均干净

## 7. P8 keydiff 裁定（21 项，无歧义计数）

提取器 keydiff 列表：`[1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]`

- **2 项真重定向（键段本身改变，合法）**：#137（键 → 荷兰语 `Cultuurdag is op 3 november.`）、#138（键 → 荷兰语 `Wie afval op straat gooit, krijgt een boete van 2.000 yen.`）
- **19 项仅注释差异或提取伪影（键段逐字 = 核心，差异只在注释段）**：#1、#2、#5、#7、#8、#9、#29、#32、#65、#69、#78、#101、#113、#115、#117、#118、#140、#146、#147。其中 #5 的表面键差异是解析伪影：#66 注释换行续行 `5.00 uur` 被误认成题号；直接查文本元素证实本版 #5 为 `5. 7 — De verlichting in Kobe begint op 7 november (zaterdag)`，键 `7` 与核心 `5. 7 — 神户灯光秀从7日（周六）开始` 一致。#101 属括号分支提取伪影类（与 JA×EN 同类）。
- **#139 的归属（在 keydiff 外）**：#139 不在 keydiff 内；其键段逐字 = 核心（`読書週間は10月27日から始まります。`），题干已重定向为荷兰语提示。提示本地化共 2 项（#139、#140），其中 #139 在 keydiff 外、#140 在 keydiff 内（#140 的键段亦逐字 = 核心，属注释差异类）。
- 计数表述：**21 = 2 真重定向 + 19 注释差异/伪影**；提示本地化共 2 项，#139 在外、#140 在内。不得写成 “2+19” 式双重计数（即不得把 #139 既算在 19 内又单独加一次）。

## 8. 修复轮次（全部改动只进 transform.py，经 gen_nl.py 再生成；每轮 pre-fix 基线单独存档）

- 第 1 轮（首渲染）：计数全对（150；A2 46/B1 75/B2 29；页分布 = 核心；范文 167）；缺陷：P7 预告末端 2553.12（>2540）、P8 答案流末端 2553.3 伴 3 处 FLOW OVERFLOW（#148/#149/#150 同 y 碰撞）、遮挡审计 5 处 NEW（P2 匹配指令墨迹出页至 x=1960.0；P8 溢出 ×4）；freeze strict-CJK 首轮已 0。基线：`sha256-round1.txt`（8 SVG + 8 卡 + 2 PDF）与 `sha256-round1-build.txt`（transform/gen/content/render/run/svglib）。
- 第 2 轮：读者来信角披露缩短为 v6（5 行）；4 条 P8 注释缩短（气温注占 2 题，共省 5 个换行行）；匹配指令缩短为 `Combineer`（仅 P2/P8，P3 保留完整形）。结果：P7 预告 2524.12（<2540 ✓）；P8 仍 1 处 FLOW OVERFLOW（#150 前流量 y 已 2533，差 16px）；改动文件恰为 P2/P7/P8 的 SVG+卡片+PDF。基线：`sha256-round2.txt`。
- 第 3 轮：#115 注释再缩短 1 行（见 §3）。结果：零 FLOW OVERFLOW、零 HEAD TOO WIDE；P8 末端 #150 于 2530.73（<2540 ✓）；改动文件恰为 P8 的 SVG+卡片+2 PDF。基线：`sha256-round3.txt`。
- 构建器结构：以 W45 JA×EN 构建（510 行 transform.py）为脚手架，OLD 侧（中文/冻结串）逐字节复用，NEW 侧（英语）替换为荷兰语；`gen_nl.py` 从只读参照 `transform-en-reference.py` 生成 `transform.py`（JA×DE 的 gen_transform.py 先例），保证 transform.py 为唯一事实源。生成器排障记录：`\uXXXX` 转义须解码为实字符（23 处；`·` 保留单反斜杠转义）；`EN2NL.update(` 第二块缺右括号致 SyntaxError 已修复；`ゴミの罰金は今年6月からです` 系条目属 OLD 侧误键入 NEW 侧已纠正；`Readers\' corner` 与 `Editor\'s sample` 含真实反斜杠，生成器键以 `chr(92)`/`chr(39)` 构造。
- 变换核验：解析 EN/NL 两版 transform 的 GLOBAL（18 对）/NOTES（133 对）/PER_FILE 对照——OLD 侧全部一致（PER_FILE 仅 content8 为 12 对 vs EN 的 11 对，因新增带右侧一对）；NEW 侧未译残留仅为合法相同项（纯几何行、wordmark/tagline/规则线、`lcn → ''` 删除对、数字 `38 + 27 = 65`、EN==NL 同形词 museum/Suginami/budget）；另查出并补上 2 处真遗漏（立冬日期注释）。

## 9. 复现

- 解释器（run.py 与 render.py 分别记录）：均为 `tools/venv/bin/python`，Python 3.12.3，PIL 13.0.0，含 cairosvg。系统 python3 同为 3.12.3 但 PIL 10.2.0 且无 cairosvg，**不能**跑 render.py。
- 审计测量以渲染 SVG 为准，用 venv PIL。
- 复现命令（构建树内）：`../../tools/venv/bin/python transform.py`（由 gen_nl.py 再生成时）→ `../../tools/venv/bin/python run.py`（单进程，content12→34→56→7→8）→ `../../tools/venv/bin/python render.py`（卡片与双 PDF）。**绝不在原地运行会把 SVG 写回交付目录/核心目录的构建树脚本**；登记展开类重跑先拷到 scratch 并重定向 OUT。
- 一进程规则：run.py 单进程跑全部 content（共享 bslib4 登记表），不得分进程。

## 10. W43 偏差清单（逐项）

1. 刊名 y=248（W43 同配对实测）vs README §20 泛化 262 → 采纳 W43 的 248。
2. P8 带右侧用荷兰语 `Pagina 8`（W43 NL）vs JA×EN 保留冻结日语 `第 8 面` → 采纳 W43 NL。
3. E 区指令为方向性（`Vertaal naar het Nederlands` ×2、`Vertaal naar het Japans` ×2，W43 NL）vs JA×EN 的无方向 `Translate` → 采纳 W43 NL。
4. 匹配指令 P2/P8 缩短为 `Combineer`（W43 先例），P3 保留完整形 `Koppel activiteiten aan plaatsen en tijden`。
5. 读者来信角披露为全新荷兰语 v6 措辞（VOL.2 事实：无真信、无最佳 P8 作文、VOL.3 承诺），非 W43 VOL.1 措辞的复制。
6. 其余家具（badge 串、副标题 316、badge 356 19pt、标语 390、规则线 406/413、暗带 424、页脚、页码、分隔符、gloss 前缀、章节名、类型名、指令词）均逐字 = W43 同配对。

## 11. PDF 钉点

- 印刷 PDF `Lucerna-VOL2-NL.pdf`：28,025,932 字节；sha256 `1dd58de4cbc9a42756c59692b616c13ce440f8458c0300ec48556206e4aa4aba`
- 网页 PDF `Lucerna-VOL2-NL-web.pdf`：3,105,024 字节（<10 MB 服务端上限）；sha256 `464129c079e704334e450147813982dacc2a31ad9afd18b08c18042de5ff3aa0`
- 两 PDF 均于第 3 轮渲染后未再变动（第 3 轮后仅 SVG 确定性重跑，PDF 字节数与第 3 轮基线一致）

## 12. 待独立校对（非构建缺陷）

- 本 KIT 记录的全部为构建侧门禁；按 SOP §8.4，定稿前仍需一次全新独立校对（内容事实、荷兰语译文质量、日语冻结完整性），校对员不得复用本构建员的结论。
- 校对时建议重点：E 区方向性（#137/#138 译入荷兰语、#139/#140 译入日语）、P8 #37 裸串已荷兰语化、P7 诊所 4 项荷兰语注释、P2/P8 `Combineer` 缩短后的可读性。
