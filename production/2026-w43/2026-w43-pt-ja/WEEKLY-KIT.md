# WEEKLY-KIT — A Lucerna VOL.1 · 葡萄牙语正文 × 日语讲解（PT×JA）

- 版次：A Lucerna 葡萄牙语周刊 VOL.1（W43 · 2026-10-19 – 2026-10-25），目标语 = 巴西葡萄牙语，讲解语 = 日语。
- 状态：**PASS**（独立校对一轮零缺陷、零修复，见 §10）。
- 出货目录：`files/weekly-report-pt-ja/`（svg ×8、cards ×8、印刷 PDF、网页 PDF）；建造目录：`hidden_files/weekly-report-pt-ja-build/`（葡语核心 build 的副本，OUT 已改道；scratch 变换脚本与全部扫描输出在其 `scratch/`）。
- 母版：葡萄牙语核心 VOL.1（`files/weekly-report-pt-vol1/`，build `hidden_files/weekly-report-pt-build/`），逐字节冻结，本版只改讲解层。

## 1. 基线链（动工前置，全部实测）

1. `tools/freeze.py baseline`（核心 build 对出货核心 SVG）：**8/8 逐字节复现**（核心 SVG sha256 前缀 p1 082acac0 · p2 c4a853ac · p3 bba9906a · p4 b9941754 · p5 4a1121e8 · p6 0d0ad436 · p7 d3dc772b · p8 8a944c11）。
2. 改道副本（未改内容）复跑：8/8 逐字节复现；OUT 改道覆盖 expanduser 写法，残留 pt-vol1 引用 = 0，首跑前打印 OUT 验证。
3. 讲解流 svglib.py 换为日语核心版（自 `hidden_files/weekly-report-ja-build/` 取，md5 **d73e23b365676c3618d7e060b835eb4d** 验明）；换版后非 CJK 元素 0 差异，仅 CJK 讲解元素重排（scratch/check_swap.py）。
4. 收尾复跑 freeze baseline：仍 8/8，工具自带核心完整性复核（出货核心 SVG 跑后未变）。

## 2. 变换记账

- AST 定位精确替换（scratch/transform_ja.py，仿 EN×JA/ES×JA 法）：CJK 串节点 491 个 / 去重 270 个（定向编辑后 272）= **261 映射 + 9 原样保留 + 2 定向跳过**，实际替换节点 **482**。
- 原样保留 9 条（语言中立）：动词形注 ×7（'conferir：ele → confere'、'abrir：ela → abre'、'levar：nós → levamos'、'digitar：ele → digita'、'fechar：ela → fecha'、'conferir：você → confere'、'começar：ela → começa'）、'66.026 > 66.000：maior'、'CULTURA · 文化'。
- 定向编辑 3 处：(a) P1 徽章替换 y=372 tagline 槽（见 §3）；(b) P8 分隔串 `— PÁGINA {pg} —` → `— {pg} ページ —`；(c) `bridge()` → `expl()` 改名（bslib4 定义 1 + 调用 21，断言通过）。
- 页脚由映射片段拼成：左 'A Lucerna · ポルトガル語週刊 VOL.1 · 本文はポルトガル語 · 解説は日本語'；页码片段 '第 '→''、' 版 / 共 '→' ページ（全 '、' 版'→' ページ）' ⇒ «N ページ（全 8 ページ）»。
- gloss() 前缀 '译注｜' → '解説 — '。
- 数字盒标题缩短为 'A SEMANA EM NÚMEROS · 今週の数字'，避免继承核心自家标题越框化妆项（README 第 15 条：讲解层标题自有文字入框即合规）。
- 题型/指令映射（与 content8 的 type 判定用同一常量）：单选→選択問題、完形单选→穴埋め選択、完成句子→文の完成、词汇配对→語と意味を結ぶ、造句→文を作る、判断对错→正誤判断、判断→正誤、翻译→翻訳、写作→作文、填空→空所補充、把词和释义配对→語と意味を結ぶ。

## 3. 家具（JA 列定式，照 EN×JA KIT §3 登记套用，目标名 ポルトガル語）

- P1 徽章（y=372 槽，19.5pt bold 砖红，居中）：«ポルトガル語テキスト · 日本語の解説 — 日本語読者のための版»（实测 ×1）。
- 顶部横幅：«毎週一号»（既有槽位随映射转换）。
- 页脚左：«A Lucerna · ポルトガル語週刊 VOL.1 · 本文はポルトガル語 · 解説は日本語»（×8）；页脚右（页码）：«N ページ（全 8 ページ）»（×8）。
- gloss 前缀：«解説 — »；语法前缀随 expl 流为日语行文（«文法ポイント — » 家族式，本版 B1/B2 语法注以行文呈现）。
- P8 页头：«RESPOSTAS · 全解答と解説（1–8ページ）»（×1，RESPOSTAS 随目标语 masthead 语 = 葡语）；P8 分隔：«— N ページ —»（×8）。
- 章节头：葡语原题 · 日语短题（如 «VIDA · 暮らし»、«FRASES DA SEMANA · 今週のフレーズ»）。
- 练习指令五式（本版实测）：空所補充 / 文を作る / 翻訳 / 正誤 / 語と意味を結ぶ。
- 答案式样：PT 家族短横式 «N. key — note»（写作题 «N. ✓ note»），与核心出货 SVG 及 PT 家族扇出代码一致（README 第 8、14 条核自代码）。
- «解説 — » 出现总计 7 = 徽章内 1 + P1 词汇条 1 + gloss 盒 5（P2–P6 各 1），逐项可归因。

## 4. 注册表与键差异（实测）

- 总量 **150 题 = A2 44 · B1 75 · B2 31**；逐页 10/18/18/18/18/18/12/38；范文 92 词。与核心全等。
- 注册表逐字比对（scratch/dump_reg.py + registry_compare.py；核心注册表自 freeze 基线副本导出）：**真键差异恰为 {137, 138, 150}**：
- 137 翻译题键：'周日，巴西重返投票站。' → '日曜日、ブラジルは再び投票に行く。'
- 138 翻译题键：'出门前，核对你的投票地点。' → '家を出る前に、投票場所を確認しなさい。'
- 150 写作装置键：'（开放题，范文如下）' → '（自由作文、模範文は次のとおり）'
- 其余 147 键逐字节同核心。
- 题干改向 {139, 140}（键仍葡语）：139 题干 '「ギター」の検索量は53%増えた。→ ___'；140 题干 '着いたら、投票所を確認してください。→ ___'。
- notediff = 141；逐字节同核心的 9 条注恰为语言中立集 {16, 17, 18, 19, 20, 57, 87, 102, 103}（87 = '900 − 250 = 650'）。typediff = 150（题型标签全数中→日）。
- p8.py compare 原始 keydiff = [3, 8, 58, 98, 137, 138, 146, 147, 148]；其中 {3, 8, 58, 98, 146, 147, 148} 经注册表逐字比对 + P8 印刷行直查双证为提取伪影（7 项的印刷键与核心逐字同：'4.352'、'A'、'melhor'、'votos válidos'、'A'、'B'、'A'），真差异仅 {137, 138} 在 p8 口径内（150 为 ✓ 式行，不入 keydiff 口径）。

## 5. 印刷注释门与 gloss 点数

- PT 核心印全 150 注（p8.py extract 实测 150/150）：本版同集强制，p8.py compare 终值 **CLEAN 150 = 150**（missing=[]、extra=0、uncertain=[]）。
- gloss 盒逐条点数（AST 提取 gloss() 实参，按 ' · ' 计条）：核心 [5, 5, 4, 4, 5]（P2 5 · P3 5 · P4 4 · P5 4 · P6 5）= 本版 [5, 5, 4, 4, 5]，逐条全等，一项不少；P1 词汇条 3 项同数。
- P7 金句：8 条葡语引文逐字同核心（出现次数各 1），页签分布同核心 {Página 1: 2, Página 2: 2, Página 3: 1, Página 4: 1, Página 5: 1, Página 6: 1}；金句 gloss [186]–[193] 为日语译文。

## 6. 自校缺陷与修复（全部限讲解层，每处修复后重渲染验证）

1. P6 C 组指令 '意味に合う正しい動詞の形を補ってください。'（折行 1 行，原映射 2 行）。
2. P6 D 组词框行 '枠の語で補う：segundo turno · maioria absoluta · votos válidos · intenção de voto'（2 行，原 3 行）。修复 1+2 使 P6 练习流终点回到核心的 **y=2519** 分毫不差。
3. P7 易错点 en/la 注缩短为 'en/la はスペイン語。em+a が na に。'（1 行，原 2 行）。
4. P7 读者角注 '編集部の作例で実在しません。VOL.2 で本物の投書と8ページの優秀作文を掲載！'（保留「非真实投书」声明 + VOL.2 承诺；该串在 content7.py 出现 2 次——量高与印刷各一）。修复 3+4 使 P7 第 3 栏终点回到核心的 **1722.0**。
5. P1 AS BUSCAS 边栏副题 'ブラジル人が探すもの · as buscas no Google'（墨迹 388.2px ≤ 412 预算；原译墨迹达 x=1981，审计 EDGE+BOXTITLE）。
6. P1 边栏脚注 '第1回前後のGoogleデータ：検索≠投票意向'（377.3px；原译墨迹达 x=2077）。
7. P4 D 组指令禁则修复：'文を過去時制（pretérito perfeito）に直して、補ってください。'（読点后断行，第 2 行以「補」起）——治本版唯一的行首禁则违规（原行首 'ってください。'）。
8. P6 A 组指令孤行修复：'上の二つの図を見て答えを選んでください。'（1 行；原译 2 行，尾行仅 'さい。'）。附带效应：P6 rect 多重集与核心的 4 枚 B2 级别片 +29.7px 位移随之消失，终验 rect 差异 = ∅（见 §7）。

孤行扫描另见 15 处 ≤5 字日语续行（如 'ください。'、'い。'、'る）'）。同口径扫描出货基线：日语核心 51 处（含有单字尾 'す'）、EN×JA 31 处、ES×JA 29 处（含 'さい。' 尾）、FR×JA 28 处——均已过零问题门，属 JA 家族既定排版常态，非缺陷类，不 churn；仅第 8 项 2 字尾 'さい。' 为本版新引入且可顺手收齐，已修。

## 7. 机械门终值（对最终出货工件）

- 构建日志警告 (!!) = 0。
- `tools/occlusion_audit.py`（自检先行 OK）：本版 **0 旗**；核心 1 旗（其自家数字盒标题 BOXTITLE，冻结核心化妆项，本版未继承）；**NEW vs core = 0**（scratch/occl-final.json）。
- 同行墨迹扫描（README 第 10 条，scratch/rowcheck.py 复用审计墨迹盒）：**0 碰撞 / 0 紧贴对**（本版与核心皆然），退出码 0。
- 图表标签元素级检查（第 12 条）：P6 两图组文字墨迹与后绘 rect 重叠 = **0**（任意覆盖率）；条形与标签与核心冻结全等（rect 多重集差异 = ∅）。
- 行首禁则扫描（JA svglib 口径，全禁则集）：**违规 0**。
- 拉丁断词扫描：假名承载行对候选 18 条，逐条裁定为词界折行（如 'seção'|'eleitoral'、'maioria'|'absoluta'），**词中劈开 = 0**。
- freeze diff 终值：added CJK = **2,850 字，全部日语**（假名 + 日语汉字用字，逐字归因表在 scratch/freeze-diff-final.json）；葡语正文文本多重集与核心全等（分项核算 scratch/split_account.py：非 CJK 变动行全部归因于徽章/分隔定向编辑与同词内容折行重排，移除侧仅讲解层）。
- 残留扫描：简体中文特有字 = **0**；' 版' 式中文页脚残段 = 0；荷/俄/西讲解家具 = 0；讲解层「仅汉字」串逐条裁定为日语固有表记（決選投票、投票所、有権者証 等）。操作代码禁用术语：'bridge' = 0（改名完成；scratch/transform_ja.py 中的 '.bridge(' 仅为改名检索模式，限 scratch 子目录，在此披露）；svglib.py 内 1 处 'paper' 为日语核心库自带 docstring（逐字继承的共享库文件，零渲染出现），非本版内容代码。

## 8. 内容红线与日历（America/Sao_Paulo 实测对照）

- 投票百分比：**未新增任何选情数字**；纸面百分比仅核心冻结的 Google 搜索增长数（+900% 等），且两处冻结免责声明（P1 边栏脚注、P6 图注）均在位——搜索 ≠ 投票意向。
- Copa do Brasil 半决赛在 **11 月**（首回合 Sun Nov 1）——正文、赛程表（Dom 1º.11）、P7 预告均作 11 月，未改作 10 月赛事。
- 日历实测：2026-10-25 = Sun（次轮投票）✓；10-31 = Sat（万圣节）✓；11-01 = Sun（半决赛首回合）✓；11-02 = Mon（Finados）✓；Enem Sun 11-08 与 11-15 ✓；辩论 Fri 10-23 ✓。
- 讲解层未引入国际政治；内容为巴西国内选举程序与文化体育，本版新增文字仅日语讲解。

## 9. 视觉终检与针脚

- 8 张卡面逐张肉眼核：日文字形渲染完整，无缺字/方框；徽章、边栏副题/脚注、数字盒标题均入框；P6 A 组指令 1 行在位；P4 D 组指令断行干净。
- 印刷 PDF `A-Lucerna-VOL1-JA.pdf`：18,314,710 B，sha256 b74f4f3e90a088866ecaa6e1609a87c44c101e7fb8c4f267b2a7c2d993166a79。
- 网页 PDF `A-Lucerna-VOL1-JA-web.pdf`：3,615,057 B（< 10 MB），sha256 1578e889dbed2169b8d71bc79523ad6a74266df45cf5fbff1c007207299a26de。
- 卡面文件名：p1-capa、p2-vida、p3-cultura、p4-esporte、p5-jovens、p6-aprofundamento、p7-lingua、p8-avaliacao。
- 本 KIT 状态 PENDING：未入仓、未发 Discord。

## 10. 独立校对记录（2026-10-22，校对员独立复跑，未采信建造者自报）

- **结论：PASS，一轮零缺陷、零修复、无重渲染。**
- freeze.py baseline：核心 8/8 逐字节复现（哈希与 §1 登记逐项全合）；另对本版 build 副本跑 freeze baseline，出货 8/8 逐字节复现（构建确定性自证）；开工/收尾核心 SVG 哈希两度全等，核心零触碰。
- freeze.py diff 独立分账：added CJK 恰 **2,850** 字；逐字归因全为日语（假名 + 日语汉字，含 確認・認定・視聴 等日语固有用字）；风险代码点审计（发/语/听/现/实/经/济/观/规/读/过/还/时/这/么/们/为/应/组/长 等简体形）= **0**，日语形（語・聴・現・実・規・読・過・還・時・応・組・続・総・選・題）在版。拉丁 token 多重集逐页比对：差异仅三类——P1 tagline 槽→徽章、页脚 «LUCERNA PORTUGUESE WEEKLY»→页码行、P8 分隔 «— PÁGINA n —»→«— n ページ —»（均定向家具替换），余为折行重分段与讲解层引述（如 P8 注引 Daronco / Palmeiras × Vasco 原名、P5 gloss 引 Enem），葡语正文无增删改。与核心逐字同的含 CJK 串仅 «CULTURA · 文化» 一条（§2 登记保留）。
- p8.py：extract 出货核心独立复证印刷集 = 150；compare **CLEAN 150=150**，keydiff 原始 = [3, 8, 58, 98, 137, 138, 146, 147, 148]。
- 键差异复验（自备 AST 提取双 build 全部 ex/match_set 调用逐项比对）：键差异恰 **{137, 138, 150}**（137/138 译文忠实、150 装置项），题干差异恰 **{139, 140}**，level 差 0、opts 差 0、注差 141、未变注恰 {16, 17, 18, 19, 20, 57, 87, 102, 103}（语言中立集），题型标签 150 全译、instr 82 处中→日映射一致。p8.py 余 7 项 keydiff 逐项双证为伪影：注册表键逐字节同 + P8 印刷行直查键部逐字同（3 '4.352'、8 'A'、58 'melhor'、98 'votos válidos'、146 'A'、147 'B'、148 'A'）。**全部 150 键自葡语正文逐题手工重推导，零分歧**（含 #49 总比分 1–0/1–3 → 3–2 复算、#57 66.026 > 66.000、#86 350+350=700、#87 900−250=650、两组配对映射 d/c/b/a 与 c/b/d/a、b/d/a/c、范文逐词实数 92 词 ∈ 80–100）。总量 150 = A2 44 · B1 75 · B2 31 与核心全等。
- 红线：逐页百分比 token 多重集核心 vs 本版 **8 页全等**——无新增选情百分比；两处免责在位（P1 边栏脚注日语版、P6 冻结葡语图注 «comportamento de busca — não é intenção de voto.» + 日语版）；Copa 半决赛在 P7 预告冻结原文 «Domingo 1º de novembro: as semifinais da Copa do Brasil» 与 #50 键均为 11 月。
- JA 列定式核（对 EN×JA KIT §3 逐字）：徽章 (975, 372) 槽、19.5pt 粗体 #a4553a 居中、文逐字合 ×1；顶带 «TODA SEMANA EM PORTUGUÊS · 毎週一号 · …»；页脚 ×8 逐字合；页码 «N ページ（全 8 ページ）» 1–8 逐页对应；P8 头 «RESPOSTAS · 全解答と解説（1–8ページ）»；分隔 «— N ページ —» ×8、旧形 «PÁGINA» 分隔 = 0；«解説 — » 共 7 处、双前缀 = 0；目标语名 ポルトガル語 与 §3.1 名表一致；核心自家无文法前缀元素，本版同构（非缺失）。
- svglib md5 实测 = **d73e23b365676c3618d7e060b835eb4d**（与日语核心 build 逐字节同）。自备行首禁则扫描（全册全部文本元素）= **0**。自备拉丁断词扫描（假名承载行衔接处）候选 7 条逐条裁定为词界折行（lado|a lado、a|arbitragem、o|levantamento、a|campanha、maioria|absoluta、pretérito|perfeito、as|urnas），**词中劈开 = 0**。
- 遮挡与兜底：occlusion_audit（自检先行）本版 **0 旗**、核心 1 旗 = 其自家数字盒标题 BOXTITLE（已登记核心化妆项，本版标题已缩短入框、未继承），NEW vs core = 0。自备同行墨迹扫描（README 第 10 条，真墨迹盒）碰撞 **0**、紧贴对 0。P6 元素级（第 12 条）：全部文本墨迹 vs 后绘不透明图形任意覆盖率重叠 = **0**；P6 rect 多重集与核心差异 = ∅；两图数值标签全等、两组数据未混。建造者 8 项修复逐项落点实证：P6 练习流最深元素两版基线 2537.08 / 墨底 2538.83 逐值相同；P7 末栏墨底两版同 1705.55（VOL.2 承诺行收尾）；P6 A 组指令单行在位；P4 D 组指令禁则已清（全册扫描 0 佐证）。
- gloss 点数（自备 AST 提取 gloss() 实参逐条）：[5, 5, 4, 4, 5] 与核心逐条同数同序，葡语词头序列逐条全等。P7：8 条金句葡语原文逐字 = 核心且回溯本期原文验真（第 3 条 «o Brasil não tem horário de verão» 在 P2 以折行分段在位）；页签分布 {1:2, 2:2, 3:1, 4:1, 5:1, 6:1} 两版全等；VOL.2 预告与「非真实投书」声明日语完整保留。
- 短尾行裁定复核：以自备统一口径（渲染行块重构）复测基线——日语核心 17、EN×JA 2、ES×JA 5、FR×JA 9、本版 9（口径与建造者 wrap 口径不同，绝对数不可比，结论同向：本版非异常值）；更宽口径下本版 19 处尾行逐处目检全为正常日语句尾段（る。/の。/投票意向。/括注闭合等）。决定性先例在出货版实证：ES×JA 纸面有同形 «さい。» 尾行 ×2（且与本版同为 y=1777.225 的指令行）、FR×JA 有 «い。» 尾行、日语核心有单字尾 «す» 与 «さい。»——均为已过零问题门的家族常态。**裁定成立：非缺陷，不 churn。** 建造者对 P6 一处的事前收齐属顺手整洁，与门无关。
- 日历（TZ America/Sao_Paulo 实测）：10-25 Sun（次轮投票）、10-21 Wed（Prova do Fazendeiro)、10-23 Fri（Globo 辩论）、10-31 Sat、11-01 Sun（Copa 半决赛首回合）、11-02 Mon（Finados)、11-08/11-15 Sun（Enem）——与纸面全合。讲解层无国际政治新增（巴西国内选举程序为核心冻结内容）。
- 残留：简体特有字 = 0、中文讲解残留 = 0、西里尔 = 0、荷/俄/西家具 = 0、纸面禁用术语 = 0（scratch 检索模式引用 confined + §7 已披露；svglib docstring 的 'paper' 为日语核心共享库逐字继承、零渲染出现）。
- 最终针脚（磁盘实测，与 §9 登记逐字全合）：印刷 `A-Lucerna-VOL1-JA.pdf` **18,314,710 B** / sha256 `b74f4f3e90a088866ecaa6e1609a87c44c101e7fb8c4f267b2a7c2d993166a79`，8 页；网页 `A-Lucerna-VOL1-JA-web.pdf` **3,615,057 B** / sha256 `1578e889dbed2169b8d71bc79523ad6a74266df45cf5fbff1c007207299a26de`，8 页。
- D5 rebuild (2026-11-13–14, see D5 rebuild section at the end of this KIT): print master `A-Lucerna-VOL1-pt-ja.pdf` **10080879 B** · sha256 `5ab27aab81c5fa3322dc820a9119ddc00c07ae6453ecfc4f4d17cc579e8f52d8`; render-web `A-Lucerna-VOL1-pt-ja-web.pdf` **3234894 B** · sha256 `9489e9120b733e82b8bb79c0a9e1aee5680d1d1a47a74e865d1adfcb85aa5e67`; web (issues-type) `2026-w43-pt-ja.web.pdf` **1080542 B** · sha256 `cd3f4f275971737bf516daa41d939d761b6c950f729fc8def2ba359d02297e8c` (< 7 MB); text.md byte-identical to the shipped version (sha256 `3d56febcbffaad40514596a606234832335405a4658f1d04ba41ce0902042537`). Pre-D5 KIT pins above (print 18,314,710 B (sha256 `b74f4f3e…`); render-web 3,615,057 B (sha256 `1578e889…`)) are D1-era values, already expired before this rebuild (toolchain drift: Bold/Italic subset split in tools/webpdf.py commit 40963281).
- 校对工件：`hidden_files/proof-pt-ja/`（freeze diff / p8 / occl JSON、AST 注册表比对、自备扫描脚本与裁剪图）。未入仓、未发 Discord。

## D5 rebuild (2026-11-13–14, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-ja/`; per-edition report: `production/notes/2026-w43/g-pt/scratch-d5-rebuild-pt/D5-REPORT-2026-w43-pt-ja.md`.

**Install**: core landed with `apply_variant.py --patch-core pt --week 2026-w43` (production `core-pt/svglib.py`, `_D5_READER = "latin"` — the core template); this edition installed with `apply_variant.py --svglib patched/2026-w43-pt-ja/svglib.py --target pt --reader ja --week 2026-w43`, `_D5_READER = "cjk"` (--check dry-run clean, RC 0); routing unit test `test_d5_routing.py` FAILURES: 0; fix2 block kept (5 occurrences).

**Baseline** (pre-fix production build): run TOTAL 150, 0 warnings; print/web/issued text layers 37,733 = 37,733 = 37,733 chars, multiset diff 0; baseline web PDF 1,297,752 B; print PDF 16,831,278 B (`3709be1b…`); pre-fix census D5 Latin 343, Cyrillic 0, curly in CJK 0; baseline P8 noted 150/150.

**Defects and fixes** (run1: 3 items, sizes only, no wording changed):

- P2-ex head `C　COMPLETE COM OS NÚMEROS`: content12.py:256 `e.head` 25→22
- P3-main head `DOIS INSTRUMENTOS, UM PAÍS`: content34.py:21 `f.head` 25→24
- P1 box: content12.py:47 `f.box` close, `tsize` 23→20

P8: 226→226 lines, footer slack 42.7→42.7 px.

**Gates run2** (16 gates; no family gates.py for pt) — **15/16 gates — textmd FAIL only (see note below)**: run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0 (curly_total=0); render RC=0; webpdf RC=0 (1,080,542 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 240, run splits); spill 0; boxtitle 0 DEFECT (28 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web 96,792 chars, multiset diff 0; textmd carryover **FAIL 10/14** (svg 5646 vs md 5650 tokens) — see note below; masthead gap (D18) 56.6 px PASS; census_quotes 0 defective.

**New deliverables**: print master `A-Lucerna-VOL1-pt-ja.pdf` 10,080,879 B (`5ab27aab…`); render-web `A-Lucerna-VOL1-pt-ja-web.pdf` 3,234,894 B (`9489e912…`); web (issues-type) `2026-w43-pt-ja.web.pdf` 1,080,542 B (`cd3f4f27…`); text.md byte-identical to the shipped version (`3d56febc…`). Still 150 exercises.

**Exporter note**: pt has no `.text.md` exporter (verified: the `ru_textmd.py` trial differed by 757 lines). The issued `issues/2026-w43/2026-w43-pt-ja/2026-w43-pt-ja.text.md` is carried over BYTE-IDENTICAL; content identity is verified by `verify_textmd.py` carryover jointly with gate 15 (print=web text layer diff 0).

**textmd residual (frozen-tool limit, not a content defect)**: under the frozen `tools/verify_textmd.py` (additive pt calibration only — see family report §5.0b), this edition's carryover residual is 10/14 tokens. Clearing it needs generic-rule changes the coordinator has frozen; whether to allow them is pending the coordinator's decision. The print=web text layer (gate 15, 96,792 chars, multiset diff 0) independently confirms the content is unchanged.
