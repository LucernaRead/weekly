# 独立校对笔记 — 2026-W47 pt-en（第一轮，叶子）

- 校对员：叶子（第一轮独立复校；与 pt-en builder、pt 核心 builder、pt 各轮复校员不同人）
- 校对时间：2026-11-11 02:28–07:40 EST（约 07:28–12:40 UTC）
- 复校对象：`production/2026-w47/2026-w47-pt-en/`（main clone 内）
- 依据：SOP.md §8（校对闭环，含 §8.1）、§1.1 全文；`AGENTS.md`；`WEEKLY-KIT.md`；`scratch-fanout-pt/FANOUT-REPORT-pt.md`
- 方式：只检查、不改任何源码/成品。版目录未作任何修改（git status 仅显示该目录本身为未入仓新目录，无改动）。
- 工作笔记目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-en1/`

## 0. 开工探针与身份核对

- 探针 1：`echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`da0c4eb8…`）。
- 探针 2：在 `hidden_files/w47/scratch-proof-pt-en1/` 内真实写 `.probe` 成功。
- 印刷 PDF `A-Lucerna-VOL4.pdf`：**12,932,446 字节，8 页，1462.5×2025 pt，sha256 `8d2b58152bc0969151f8a7ab8becb0976221efdc62cac0d3cce877de8f160e4a`**——与 KIT 登记逐字一致。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：**1,102,770 字节，8 页，sha256 `40bc2f444dbc31fbf0ef49643f1f81da13c134cab5ba0ec0a3ea804574a5e49c`**——与 KIT 登记逐字一致。
- 身份相符，继续复校。

## 1. 缺陷清单（本轮共 3 类，均为英文讲解层轻微缺陷）

### D1（轻微）— P1 刊头标语英文歧义：`The Portuguese Brazil is reading`

- 位置：P1 顶部 `TODA SEMANA EM PORTUGUÊS　Every week　The Portuguese Brazil is reading`（SVG `p1-capa.svg` 内同一 `<text>` 元素；印刷 PDF 与网页 PDF P1 均可见）。
- 原文：`The Portuguese Brazil is reading`
- 应为：`The Portuguese that Brazil is reading`（或按中文原文的祈使语气：`Read the Portuguese Brazilians are reading`）。
- 证据：
  - 来源句为核心中文释义 `读巴西人正在读的葡萄牙语`（`tables_en.py:197`），意为“读巴西人正在读的葡萄牙语”；英文版同时丢了祈使动词 `Read` 与关系代词 `that`。
  - 英文省略关系代词后首要 parse 为 `[The Portuguese Brazil] [is reading]`（“葡萄牙语的巴西正在阅读（某物）”），须二次重 parse 才能得到 `[The Portuguese] [Brazil is reading]`；作头版标语属歧义英文。
  - 其余 9 个 W47 pt 姊妹版同一位置一律用显性关系代词，无一省略：de `Das Portugiesisch, das Brasilien liest`、fr `Le portugais que lit le Brésil`、es `El portugués que lee Brasil`、it `Il portoghese che legge il Brasile`、nl `Het Portugees dat Brazilië leest`、ru `Португальский, который читает Бразилия`、ja `ブラジルが読むポルトガル語`、ko `브라질이 읽는 포르투갈어`、zh-tw 沿用中文原文。
- 严重度：轻微（含义可还原，但为头版最显眼英文行，且 9/9 姊妹版均无此问题）。

### D2（轻微）— P4 词表注错译：`o título champion`

- 位置：P4 Note 框：`o agregado aggregate score · os pênaltis penalty shoot-out · a decisão the final · o título champion · a pausa the break · a taça trophy`（SVG `p4-esporte.svg`；印刷/网页 P4 均可见）。
- 原文：`o título champion`
- 应为：`o título title`
- 证据：
  - 葡萄牙语 `título` = title（头衔/冠军头衔）；`champion`（冠军得主）对应的是 `campeão`。正文即用此义：`O Grêmio busca o sexto título`（P4 正文）。
  - 同一期内部已正确使用 `title`：P8 答案注 146 `Grêmio chase a sixth title`、147 `Palmeiras chase a fifth title`。
  - 来源：`tables_en.py:36`：核心中文注 `冠军` 直译为 `champion`；核心中文注本身取了宽泛义，但英文讲解层须对葡萄牙语词义负责，`título = champion` 会教错词义。
- 严重度：轻微（单个词表注错译；不影响任何答案键；但属于教错词义）。

### D3（轻微，4 处）— P8 答案注冒号后缺空格（全角冒号机械转换残留）

- 位置：P8 答案流，4 条注：
  - 56. `mais — 3 > 1:mais`
  - 57. `mais — 5 > 4:mais`
  - 58. `mais — 16:30 < 17:00:mais cedo`
  - 102. `numa — cair numa sexta-feira:falls on a Friday`
- 原文：冒号后直接接英文，无空格。
- 应为：冒号后加一空格，如 `3 > 1: mais`、`5 > 4: mais`、`16:30 < 17:00: mais cedo`、`cair numa sexta-feira: falls on a Friday`。
- 证据：
  - 机制：核心原文用全角冒号且后无空格（中文排版正确），fan-out 转换只把 `：` 换成 `:`、未补空格。核心来源：`core-pt/content34.py:204/206/208`（`3 > 1：mais`、`5 > 4：mais`、`16:30 < 17:00：mais cedo`）、`core-pt/content7.py:22`（`cair numa sexta-feira：落在周五`）；英文版对应 `content34.py:204/206/208`、`content7.py:22`。
  - 同一答案流内不一致：59. `2 days < 7 days: menos`、101. `em + date: em 20 de novembro` 均有空格。
  - 全版 8 个 SVG 冒号扫描：仅此 4 处为冒号后直接接字母（已排除时刻 `16:30` 等时间写法）；双空格 0 处；双句号 `..` 0 处（其余 `...` 均为冻结葡语题干省略号）。
- 严重度：轻微（排版瑕疵；可读，不影响答案）。

## 2. 已验通过（无问题）

### 2.1 全文目视（印刷 PDF 全新渲染 8 版 + 网页 P1/P8）

渲染自印刷 PDF（`pdftoppm -r 110`，未采信 builder 卡片），见 `render/`：`print-p-1.png`～`print-p-8.png`、`web-p1-1.png`、`web-p8-8.png`。

- P1：头条、数字盒（20/1695/2023/3）、日程、目录、每周一词、快讯、Q1–10 均干净；页脚 `A Lucerna VOL.4 … Page 1 of 8`；`O FUTEBOL` 末行 `(Página 4)` 在框底完整可见，occlusion 门 0 flags。
- P2：`PARA NÃO ERRAR` 金句 8 原文完整；E VOCÊ 英译无 `?Write` 粘连；四格日程英译齐全；Q11–28 题面与徽章无误。
- P3：词表 6 词（quilombo/resistência/escravizado/líder/memória/combate）全部真实出现在正文；Zumbi 图注（Parreiras 1927）无误；Q29–46 无误；Q38/Q41 与金句 4/3 对应。
- P4：`OS FINALISTAS` 数据盒与 6 行足球周表、截稿注（10 November）无误；Q47–64 无误（Q56–59 比较级答案 mais/mais/mais/menos 与注 56–59 一致）。
- P5：五步计划括号前有空格、单句号；E VOCÊ 无粘连；Gary Todd 图注 CC0 无误；Q65–82 无误（Q76–79 将来时 sairá/publicarão/decidirá/chegará；Q80–82 Verdadeiro/Falso/Verdadeiro）。
- P6：图表算术独立验算无误——16–30 日共 15 天（工作日 10 天：16/17/18/19/23/24/25/26/27/30；周末+假日 5 天：20/21/22/28/29），第 10 个工作日 11 月 30 日、若假日计入则 11 月 27 日，27–30 窗口正确；Q83–100 无误。
- P7：三级语法栏 + 4 条常见错误英译（含已修 `November.` 单句号）、每周一词、读者来信（示例 + 葡/英双语披露，单 `!`）、8 条金句逐条带英译与页码、VOL.5 下期预告带与末条金句无遮挡（occlusion 0 flags 目视亦清）。
- P8：练习流 Q113–150 题面、徽章、G 对话、H 写作题与范文（88 词，`len(MODELO.split())` 程序计数与人工计数一致）、Mané Garrincha 图注均干净；答案流 150 条注逐条核对无误（见 §2.2）。
- 网页 P1/P8 与印刷版内容一致（仅 pdftotext 换行差异，见观察项 O6）。

### 2.2 150 题逐题验算

- 题量：run.py 重跑（见 §3）：TOTAL 150，分级 A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38——与 KIT 登记一致。
- 徽章：8 版逐题提取徽章色与题号，与核心版逐页比对，分级分布全同（含分组徽章 P2 `25–28` A2、P4 `52–55` B1、P8 `141–144` B2，颜色与核心一致）。
- 答案键：P8 extract 150/150；compare vs 核心 CLEAN，keydiff 仅 [137, 138]（翻译题答案，见 §2.4）。
- 逐题抽验要点：Q131 = A（Rafael 周六看 Palmeiras × Flamengo，核心 D2 修复已在）；Q150 开放作文、答案流标 `✓ See the model text in section H of this page (88 words)`；Q47–51、Q83–92、Q121–128 均与正文/图表一致；比较级 Q56–59、将来时 Q76–79、虚拟式 Q109–112 均正确。
- 金句 8 条：gates 验证每条在正文恰好出现 2 次 + 英译 + 页码（见 §3）；人工逐条核对原文与正文逐字一致（P1 标题、P1 导语、P3 `Zumbi nasceu em Palmares`、P3 `sem memória, não há futuro`、P4 `o agregado ficou em 2 a 2`、P5 `a espera pelo gabarito`、P6 `primeiro as fáceis, depois as difíceis`、P2 `Confira o transporte, guarde o documento e aproveite o feriadão`）。
- 讲解词真实性（§8.1）：P1–P6 词表注 29 项（gates 枚举 6/6/6/6/5）逐项核对均出现在正文或当页练习词框（P6 `chute` 见观察项 O1）；未发现注词无出处。
- VOL：VOL.4 全期正确（P1 顶条 `VOL. 4`、刊头带 `VOL.4`、每页页脚 `VOL.4`）；VOL.3 仅出现在 P7 披露内（葡/英各 1 次，所指为承诺期号，允许）；VOL.5 3 次均在 P7 披露/下期预告内（允许）。
- P8 最小字号：实测 9.75pt（答案区 187 spans、1,539 词），恰为 §1.1 下限。
- §1.1 抽查：纸色 `#fbfaf6` 每页 1 处；金色 `#d4af37` 0；`double` 0；徽章三色齐全；无双线外框残留标记；无 TODO/FIXME/XXX/占位符（`todo` 命中均为葡语词 `todo o país`，非标记）。

### 2.3 翻译层专项

- 讲解/界面语言确为英文（刊头带、页脚、栏目副题、练习指示、答案注、P7 语法讲解、披露、摘要均为英文；葡语仅为目标语正文与有意保留的葡语原文引用）。
- CJK/源语字面量转写：freeze diff 新增 CJK 共 9 个，全部为家具全角空格 U+3000（P1 2 个、其余每页 1 个）；渲染文本（`<text>` 元素）内中文字符 0；唯一非 U+3000 的 CJK 字符为 P1 冻结蛾标内嵌 `<title>Lucerna 三色蛾</title>`（三色蛾 3 字，与核心逐字相同，不渲染）。`.text.md` CJK 字符 0；双空格 0 行。
- E 组翻译题答案键已译成英文：137 `Friday 20 November is a national holiday.`、138 `Palmeiras won 5–4 in the shoot-out.`——译文正确（139/140 为英→葡，答案为葡语原文正确译文）。
- 中文残留：除上述冻结蛾标 `<title>` 与家具 U+3000 外，无中文残留。另：P1 `Key words｜` 中的全角竖线 U+FF5C 为冻结注标签格式（核心 P1 同为 1 处），非中文残留。
- U+2019：8 个 SVG 总数 0（P7 `weekend's`、`Editor's` 等均用直撇号）；目视抽查含撇号行无宽字形断裂。
- 英式拼写一致：`programme`、`eleven-metre`、队名复数动词（`Palmeiras go through`、`Grêmio chase a sixth title`）全期一致。

### 2.4 P8 答案注人名专项（人工逐条核对公开来源）

P8 答案注与题面出现的人名逐条核对，无拼错、无错名（本版无相扑力士等 ja 家庭问题类人名；以下人名均经公开来源核实）：

- Zumbi dos Palmares（1645–1695，11 月 20 日死）：注 22/29/114 均正确；日期与 KIT 来源一致。
- Lando Norris / Max Verstappen / Isack Hadjar（F1 2026 圣保罗站）：注 51/124 与 P4 正文一致；公开报道核实——2026 年 11 月 8 日 Interlagos，Norris 杆位夺冠、Verstappen 第 21 位发车获第 2、Hadjar 第 3、Russell 第 4、Antonelli 第 5、梅赛德斯锁定车队冠军（多家 11 月 9–10 日报道一致）。
- Renan Lodi / Carlos Vinícius（Copa 半决赛次回合进球者）：公开赛报核实——11 月 7 日 Atlético-MG 1–1 Grêmio（Arena MRV），Renan Lodi 26'、Carlos Vinícius 38'、Vitão 87' 红牌；总比分 3–1 Grêmio 晋级（首回合 2–0）。
- Vasco 2–1 Palmeiras（11 月 8 日，São Januário），总比分 2–2、点球 5–4 Palmeiras 晋级；决赛 12 月 6 日单场、Mané Garrincha（Brasília），Grêmio 第 10 次进决赛——公开赛果核实一致。
- Mané Garrincha（Q145/G 图注/注 145、注 50）：球场以巴西球员 Mané Garrincha 命名，注文 `The Mané Garrincha stadium` 正确。
- Deodoro da Fonseca（Q114 干扰项）：巴西第一任总统、1889 年宣布共和者，名字正确。
- Luís de Camões（P7 图注，Os Lusíadas 1572 年首版）：正确。
- Antônio Parreiras（P3 图注，1927 年 Zumbi 画像）：正确。
- Johann Moritz Rugendas（P1 图注，Voyage pittoresque dans le Brésil，Paris，1835）：正确。
- Gary Todd（P5 图注，CC0）：正确；Luis Dantas（P8 图注）：正确。
- Rafael（P8 C 组阅读主角）：虚构人名，无来源问题。
- 星期核验（`date -d`，America/Sao_Paulo）：2026-11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日——与版内全部星期表述一致。

### 2.5 事实抽查（公开来源）

- Consciência Negra 11 月 20 日全国假日（Lei nº 14.759/2023，2024 年起施行；2026 年逢周五、连休 20–22 日）：与 KIT 来源一致；星期已验。
- Enem 2026：两场分别为 11 月 8 日与 11 月 15 日（均为周日，已验）；第 2 场 13h30–18h30（5 小时，Q120 答案 5 小时一致）；Edital nº 64/2026 §15.1 `até o 10º dia útil`；工作日算术已独立验算（见 §2.1 P6）。
- 11 月 17 日 7h 新加坡 × 巴西（KIT 11 月 10 日修正 D1 后的正确时间）：P1 日程与 P3 日程一致，均为 7h。
- 5,051,345 名 Enem 报名者→版内 `Mais de 5 milhões` 表述正确。
- 26 人国家队名单、Ancelotti 姓名未出现在版内正文（仅 KIT 来源说明），无核对项。

## 3. 机械门（自跑，构建解释器 tools/venv/bin/python，Python 3.12.3 / Pillow 13.0.0）

| 门 | 结果 | 日志 |
|---|---|---|
| 身份（字节+SHA-256） | 印刷 12,932,446 B / `8d2b5815…160e4a`；网页 1,102,770 B / `40bc2f44…a5e49c`；与 KIT 逐字一致 | 本笔记 §0 |
| gates.py | **16/16 PASS，FAILURES: none**（RC=0） | `gates/gates-pt-en1.log` |
| occlusion_audit.py（venv） | **0 flags**；自检阳性对照全触发、干净对照静默（RC=0） | `gates/occlusion-pt-en1.log`、`gates/en-occlusion-pt-en1.json` |
| p8.py extract | **150/150**（RC=0） | `gates/p8-extract-pt-en1.log` |
| p8.py compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，keydiff=[137, 138]（仅翻译题答案，已验正确） | `gates/p8-compare-pt-en1.log` |
| freeze.py baseline | **8/8 SVGs byte-identical**（repointed files: none）；核心 SVG 未被改写 | `gates/freeze-pt-en1.log` |
| freeze.py diff | 新增 CJK 共 9 个，全部为 U+3000 家具分隔符（P1 2、其余每页 1）；新增汉字 0 | `gates/freeze-diff-pt-en1.log`、`gates/en-freeze-diff-pt-en1.json` |
| print/web 文字层一致 | 词多重集 diff 0（各 8,502 词）；页数 8/8（RC=0） | `gates/check-final-pt-en1.log`、`en-textdiff.json`、`en-p8size.json` |
| P8 答案字号 | 最小 9.75pt（答案区 187 spans、1,539 词），恰为 §1.1 下限 | 同上 |
| run.py 重跑（scratch 副本内跑，未碰原版） | **RC=0，零 FLOW OVERFLOW / 零 HEAD TOO WIDE**；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38）；重建 8 个 SVG 与 shipped 版**逐字节一致 8/8** | `gates/run-rerun-pt-en1.log`、`rerun/` |
| U+2019 全扫 | 8 个 SVG 总数 0 | 本笔记 §2.3 |
| 徽章逐页计数 | 8 版与核心逐页同数同级（含 3 个分组徽章） | 本笔记 §2.2 |
| ABSTRACT.txt | 英文单段，561 字节，无 ASCII 双引号，事实与本期一致 | 版目录内原文 |

## 4. 观察项（不计缺陷）

- **O1** — P6 Note 框 `o chute a lucky guess`：`chute` 未出现在 P6 文章正文，但出现在当页 D 组词框与 Q100 题面，且核心中文注同样释 `chute`（`chute 碰运气的猜测`），为核心版式、忠实转译，非 §8.1 违规。
- **O2** — P2 `D AS PALAVRAS` 栏尾孤行（栏 3 底）与 P4 `B AS PALAVRAS` 栏尾孤行（栏 1 底）、P3 中部大空白：均为核心版式，与核心一致，非 fan-out 引入。
- **O3** — `.text.md` 第 8 行 `O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL`：该行在 fan-out PDF 中不存在（P1 y=372 槽位由家具行 `TEXT IN PORTUGUESE　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS` 占据，属家具替换）；但该行同样出现在核心 `.text.md`（其 PDF 内有此行）与全部 9 个姊妹版 `.text.md` 中，属全版系统性导出行为，非本版特有问题。
- **O4** — `.text.md` 行数实测 534 行（awk NR / wc -l / splitlines 三者一致，末行 `(88 words)` 后单换行符），KIT 登记为 535 行，差 1 行（KIT 计数口径差异）。
- **O5** — VOL.4 计数口径：按 `VOL. ?4` 计为 10 次（含 P1 顶条 `VOL. 4` 带空格写法），按 `VOL.4` 精确计为 9 次，与 KIT 登记一致；无错印期号。
- **O6** — pdftotext 字节：印刷版 46,043 字节 vs 网页版 46,049 字节，差 6 字节仅为提取换行差异（刊头带在两版断行不同），词多重集 diff 0。
- **O7** — P8 注 55 `taça=the champions' trophy` 与 P4 注 `a taça trophy` 对同一词释义宽严不一（源 SEG `冠军奖杯`）；含义未错（奖杯即冠军奖杯），仅释义不一致。
- **O8** — P1 `A SEMANA EM NÚMEROS In numbers` 英译贴框边、`O FUTEBOL` 末行贴框底：渲染完整可见，occlusion 0 flags。
- **O9** — 选项分隔符 `·`（U+00B7）：P1–P7 数量与核心逐页相等、P8 少 3 个（E 组翻译键所致），均为冻结葡语题干格式，非 fan-out 引入。

## 5. 结论（报事实，不作定稿决定）

- 本轮独立复校发现 **3 类轻微缺陷（D1–D3，共 6 处）**：P1 刊头标语歧义 1 处、P4 词表注错译 1 处、P8 答案注冒号缺空格 4 处。
- 其余复校项（8 版目视、150 题验算、金句、徽章、VOL、字号、全部机械门、事实抽查、人名核对）均通过，机械门结果与 KIT 登记一致。
- 按 SOP §8.4，fan-out 版定稿须经独立复校零问题；本轮非零问题。是否返修、如何返修，由协调员决定。
- 本轮未修改任何成品；全部校对证据在 `scratch-proof-pt-en1/`（`gates/` 日志与 JSON、`render/` 10 张全新渲染图、`rerun/` 重建副本、`en-textdiff.json`、`en-p8size.json`）。

## 附：双 PDF SHA（完整串）/ 字节复核

- 印刷 PDF `A-Lucerna-VOL4.pdf`：12,932,446 字节；sha256 `8d2b58152bc0969151f8a7ab8becb0976221efdc62cac0d3cce877de8f160e4a`；8 页；1462.5×2025 pt。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：1,102,770 字节；sha256 `40bc2f444dbc31fbf0ef49643f1f81da13c134cab5ba0ec0a3ea804574a5e49c`；8 页；文字层 pdftotext 46,049 字节。
- 两串与 WEEKLY-KIT.md §6 登记逐字一致。
