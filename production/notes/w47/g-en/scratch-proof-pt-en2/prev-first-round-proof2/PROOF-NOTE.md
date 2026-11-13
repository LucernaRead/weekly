# 独立校对笔记 — 2026-W47 pt-en（第二轮，proof2）

- 校对员：proof2（第二轮独立复校；与 pt-en builder、pt 核心 builder、第一轮复校员、fix1 返修员不同人）
- 校对时间：2026-11-11 03:07–约 09:30 EST
- 复校对象：`production/2026-w47/2026-w47-pt-en/`（main clone 内）
- 依据：SOP.md §8 / §1.1 全文、`AGENTS.md`、`WEEKLY-KIT.md`、第一轮复校笔记与 fix1 记录（仅作参考，结论全部自己重核）
- 方式：只检查、不改任何源码/成品。版目录未作任何修改；run.py 重跑在 freeze 工具的 build-copy 内进行。
- 工作笔记目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-en2/`

## 0. 开工探针与身份核对

- 探针 1：`echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`8b0b1008…`）。
- 探针 2：在 `hidden_files/w47/` 内真实写 `probe-pt-en2.txt` 成功（已删除）。
- 印刷 PDF `A-Lucerna-VOL4.pdf`：**12,932,451 字节，8 页，1462.5×2025 pt，sha256 `0146a4202b015f44659b4bba067a7411f90891cb640085dee5fec2010bd06af1`**——与任务书逐字一致。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：**1,102,777 字节，8 页，sha256 `a974ef7ccf7c879f58e3626d874d9ce18e3da5f2a35faef43717e81706254c80`**——与任务书逐字一致。
- 身份相符，继续复校。

## 1. 回归核查：fix1 的 6 处全部改对（逐处核实）

| # | 缺陷 | 核实位置 | 结果 |
|---|---|---|---|
| D1 | P1 刊头标语 | `svg/p1-capa.svg` | `The Portuguese that Brazil is reading` 1 处；旧形 `The Portuguese Brazil is reading` 0 处。源表 `tables_en.py:197` 同值；两份机制表（版目录副本 + scratch-fanout-pt）逐字节一致 |
| D2 | P4 词表注 | `svg/p4-esporte.svg` | `o título title` 1 处；旧形 `o título champion` 0 处。源表 `tables_en.py:36`：`"冠军": "title"`；旧值 `champion` 0 处 |
| D3-56 | P8 注 56 | `svg/p8-avaliacao.svg` | `3 &gt; 1: mais`；旧形 `1:mais` 0 处 |
| D3-57 | P8 注 57 | 同上 | `5 &gt; 4: mais`；旧形 `4:mais` 0 处 |
| D3-58 | P8 注 58 | 同上 | `16:30 &lt; 17:00: mais cedo`；旧形 `00:mais cedo` 0 处 |
| D3-102 | P8 注 102 | 同上 | `cair numa sexta-feira: falls on a Friday`；旧形 `-feira:falls` 0 处 |

- 全版冒号复扫（8 个 SVG）：`:` 后直接接字母 0 处；仅有的 5 处 `:i` 命中全部是 base64 图片数据（`data:image/jpeg;base64,…`），非文本。时刻写法 `13:30`/`18:30` 等属数字，已排除。
- D2 同类抽查：P1–P6 词表注 29 项（gates 枚举 6/6/6/6/5）逐项重核，全部正确（feriadão/a three-day holiday、folga/time off、programação/programme、quilombo/a runaway-slave settlement、escravizado/enslaved person、agregado/aggregate score、pênaltis/penalty shoot-out、decisão/the final、pausa/the break、taça/trophy、gabarito/answer key、prazo/deadline、dia útil/working day、chute/a lucky guess 等）；12 条 `词=释义` 配对注（52–55、141–144 及 P8 注 55 等）逐条核对，无单字直译误译。D2 同类误译仅此 1 处，无新增。

## 2. 全量复校（8 页双 PDF 全文重读 + 目视）

渲染自印刷 PDF（`pdftoppm -r 110`，未采信 builder 卡片），见 `render/`：`print-p-1.png`～`print-p-8.png`、`web-p1-1.png`、`web-p8-8.png`；文字层另经 `pdftotext -layout` 全文精读（`pt-en2-p1.txt`～`pt-en2-p8.txt`，/tmp）。

- P1：头条、数字盒（20/1695/2023/3）、日程、目录、每周一词、快讯、Q1–10 均干净；D1 标语单行居中完整、无溢出；页脚 `A Lucerna VOL.4 … Page 1 of 8`。
- P2：`PARA NÃO ERRAR` 金句原文完整；四格日程英译齐全；Q11–28 题面与徽章无误。「22.Fill」式粘连经查为 pdftotext 断行假象，SVG 内无此串。
- P3：词表 6 词全部真实出现在正文；Zumbi 图注（Parreiras 1927）无误；Q29–46 无误；Q38/Q41 与金句对应。
- P4：`OS FINALISTAS` 数据盒与 6 行足球周表、截稿注（10 November）无误；D2 `o título title` 已入版；Q47–64 无误。
- P5：五步计划括号前有空格、单句号；Gary Todd 图注 CC0 无误；Q65–82 无误（Q76–79 将来时、Q80–82 Verdadeiro/Falso/Verdadeiro）。
- P6：图表算术独立验算无误——16–30 日共 15 天（工作日 10 天：16/17/18/19/23/24/25/26/27/30；周末+假日 5 天：20/21/22/28/29），第 10 个工作日 11 月 30 日、若假日计入则 11 月 27 日，27–30 窗口正确；Q83–100 无误。
- P7：三级语法栏（em+日期/cair/aproveitar；pretérito perfeito；futuro do subjuntivo）葡语变位全部正确；4 条常见错误英译无误；每周一词、读者来信（示例 + 葡/英双语披露，VOL.3→VOL.5 承诺顺延）无误；8 条金句逐条带英译与页码；VOL.5 下期预告无遮挡。
- P8：练习流 Q113–150 题面、徽章、G 对话、H 写作题与范文（88 词，独立程序计数与人工计数一致）、Mané Garrincha 图注均干净；答案流 150 条注逐条核对无误（见 §2.1）。
- 网页 P1/P8 与印刷版内容一致（仅 pdftotext 换行差异，词多重集 diff 0）。

### 2.1 150 题逐题验算（人工逐题对照题面/正文/图表，非仅采信 compare）

- 题量：run.py 重跑 TOTAL 150，分级 A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38——与 KIT 登记一致。
- 徽章：8 版徽章标签（A2/B1/B2 文本元素）逐页提取，与核心版逐页比对，分级分布全同（含分组徽章 P2 `25–28` A2、P4 `52–55` B1、P8 `141–144` B2）。注：P1 `#46581f` 填充计数版比核心多 1（47 vs 46），经定位为家具行 `PORTUGUESE WEEKLY` + 全角空格拆成两个 `<text>` 元素所致，非徽章（见观察项 O7）。
- 答案键：P8 extract 150/150；compare vs 核心 CLEAN，keydiff 仅 [137, 138]（翻译题答案，译文已验正确：137 `Friday 20 November is a national holiday.`、138 `Palmeiras won 5–4 in the shoot-out.`；139/140 为英→葡，答案为葡语原文正确译文）。本轮新 extract JSON 与 fix1 的新 extract JSON 逐字段比对**零差异**。
- 逐题要点：Q131 = A（Rafael 周六看 Palmeiras × Flamengo）；Q150 开放作文、答案流标 `✓ See the model text in section H of this page (88 words)`；比较级 Q56–59、将来时 Q76–79、虚拟式 Q109–112、完成句 Q133–136 均正确；Q148 `na internet`（em+a=na）正确。
- 金句 8 条：gates 验证每条在正文恰好出现 2 次 + 英译 + 页码；人工逐条核对原文与正文逐字一致（P1 标题、P1 导语、P3 `Zumbi nasceu em Palmares`、P3 `sem memória, não há futuro`、P4 `o agregado ficou em 2 a 2`、P5 `a espera pelo gabarito`、P6 `primeiro as fáceis, depois as difíceis`、P2 `Confira o transporte, guarde o documento e aproveite o feriadão`）。
- 讲解词真实性（§8.1）：P1–P6 词表注 29 项逐项核对均出现在正文或当页练习词框（P6 `chute` 见观察项 O5）；未发现注词无出处。
- VOL：VOL.4 全期正确（SVG 内 `VOL.4` 9 次 + 顶条 `VOL. 4` 1 次）；VOL.3 仅 2 次，均在 P7 披露内（所指为承诺期号，允许）；VOL.5 3 次，均在 P7 披露/下期预告内（允许）。
- P8 最小字号：实测 9.75pt（答案区 187 spans、1,543 词），恰为 §1.1 下限。
- §1.1 抽查：纸色 `#fbfaf6` 每页；金色 `#d4af37` 0；`double` 0；可见文本内 TODO/FIXME/XXX 0；徽章三色齐全；无占位符。
- 讲解/界面语言确为英文；渲染文本内中文字符 0；唯一非 U+3000 的 CJK 字符为 P1 冻结蛾标内嵌 `<title>Lucerna 三色蛾</title>`（与核心逐字相同，不渲染）。`.text.md` 内 6 处 U+FF5C 全角竖线为冻结 `Note｜`/`Key words｜` 标签格式（见观察项 O2）。
- U+2019：8 个 SVG 总数 0。英式拼写一致：`programme`、`eleven-metre`、队名复数动词（`Palmeiras go through`、`Grêmio chase a sixth title`）全期一致。

### 2.2 事实抽查（公开来源，本轮独立检索）

- Consciência Negra：Lei nº 12.519/2011 立日（仅纪念日、非假日）、Lei nº 14.759/2023 立为全国假日；2026 年逢周五、连休 20–22 日；Zumbi 死于 1695 年 11 月 20 日；Palmares 在 Alagoas（Serra da Barriga）；星期已验（`date -d`，America/Sao_Paulo）：11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日——与版内全部星期表述一致。
- Enem 2026：两场 11 月 8 日与 11 月 15 日（均为周日）；第 1 场 13h30–19h、第 2 场 13h30–18h30、90 题 5 小时；5,051,345 名报名者→版内 `Mais de 5 milhões` 正确；Edital nº 64/2026 §15.1 `até o 10º dia útil`；个人成绩 2027 年 1 月中旬；gabarito 27–30 日窗口：若 20 日假日不计工作日则第 10 个工作日为 11 月 30 日、若计入则为 11 月 27 日——版内 P6 明写「entre 27 e 30 de novembro, conforme a contagem」，诚实呈现了两种算法，无错。
- Copa do Brasil：半决赛次回合 11 月 7 日 Atlético-MG 1–1 Grêmio（Arena MRV；Renan Lodi 26'、Carlos Vinícius 38'，总比分 3–1）；11 月 8 日 Vasco 2–1 Palmeiras（São Januário；Colidio、Piquerez、Puma Rodríguez），点球 5–4 Palmeiras 晋级；决赛 12 月 6 日单场、Mané Garrincha（Brasília）；Grêmio 第 10 次进决赛、争第 6 冠（1989/1994/1997/2001/2016），Palmeiras 争第 5 冠（1998/2012/2015/2020）——多家 11 月 8–10 日赛报一致。
- Brasileirão 35/36 轮：11 月 18 日 20h30 Cruzeiro × Palmeiras（Mineirão）、Flamengo × Athletico-PR（Maracanã）；11 月 19 日 19h30 Vasco × Internacional（São Januário）、21h30 São Paulo × Fluminense（Morumbis）；11 月 21 日 16h30 Palmeiras × Flamengo 第 36 轮。**「Nubank Parque」核实无误**：Allianz Parque 自 2026 年 5 月 4 日起更名 Nubank Parque（Palmeiras 官网 + 多家来源），版内用新名正确。
- 巴西队：11 月 17 日 7h（Brasília）新加坡 × 巴西，新加坡国家体育场（CBF 官方）；26 人名单。
- F1 2026 圣保罗站（11 月 8 日 Interlagos）：Norris 杆位夺冠、Verstappen 第 21 位发车获第 2、Hadjar 第 3、Russell 第 4、Antonelli 第 5、梅赛德斯锁定车队冠军（FIA/路透等多家 11 月 8–10 日报道一致）。
- 人名：Zumbi dos Palmares、Lando Norris、Max Verstappen、Isack Hadjar、Renan Lodi、Carlos Vinícius、Mané Garrincha、Deodoro da Fonseca、Luís de Camões（Os Lusíadas 1572 年首版）、Antônio Parreiras（Zumbi 画像 1927，巴西国家图书馆 Brasiliana Fotográfica 核实）、Johann Moritz Rugendas（Voyage pittoresque dans le Brésil，Paris，1835）、Gary Todd、Luis Dantas——逐条核对，无拼错、无错名。

## 3. 机械门（自跑，构建解释器 tools/venv/bin/python，Python 3.12.3）

| 门 | 结果 | 日志 |
|---|---|---|
| 身份（字节+SHA-256） | 印刷 12,932,451 B / `0146a420…06af1`；网页 1,102,777 B / `a974ef7c…54c80`；与任务书逐字一致 | 本笔记 §0 |
| gates.py | **16/16 PASS，FAILURES: none**（RC=0） | `gates/gates-pt-en2.log` |
| occlusion_audit.py（venv） | **0 flags**；自检阳性对照 6 类全触发、干净对照静默（RC=0） | `gates/occlusion-pt-en2.log`、`gates/en-occlusion-pt-en2.json` |
| p8.py extract | **150/150**（RC=0） | `gates/p8-extract-pt-en2.log`、`gates/new-p8-extract.json` |
| p8.py compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，keydiff=[137, 138]（仅翻译题答案，已验正确） | `gates/p8-compare-pt-en2.log`、`gates/p8-compare-pt-en2.json` |
| freeze.py baseline | **8/8 SVGs byte-identical**（repointed files: none）；核心 SVG 复核未被改写 | `gates/freeze-pt-en2b.log`（见注） |
| freeze.py diff | 新增 CJK 共 9 个，全部为 U+3000（P1 2、其余每页 1）；新增汉字 0 | `gates/freeze-diff-pt-en2.log`、`gates/en-freeze-diff-pt-en2.json` |
| print/web 文字层 | 词多重集 diff 0（各 8,507 词）；页数 8/8（RC=0） | `gates/check-final-pt-en2.log`、`en-textdiff.json`、`en-p8size.json` |
| P8 答案字号 | 最小 9.75pt（答案区 187 spans、1,543 词），恰为 §1.1 下限 | 同上 |
| run.py 重跑（freeze build-copy 内） | **RC=0，零 FLOW OVERFLOW / 零 HEAD TOO WIDE**；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38） | `gates/freeze-pt-en2b.log`（重跑输出） |
| U+2019 全扫 | 8 个 SVG 总数 0 | 本笔记 §2.1 |
| 徽章逐页计数 | 8 版徽章标签与核心逐页同数同级 | 本笔记 §2.1 |
| ABSTRACT.txt | 英文单段，561 字节，1 行，无 ASCII 双引号，事实与本期一致 | 版目录内原文 |
| .text.md | 534 行（见观察项 O1）、题号 150/150、双空格 0 行；D2 改动在第 215 行；D1 标语不在 .text.md 内（与 fix1 说明一致） | 本笔记 §2.1 |

注：freeze baseline 首次调用误将 `--core-svg` 指向 core-pt 的 SVG 目录，得 0/8——该参数的含义是「待比对的已发货 SVG」，对 fan-out 版应指向本版自己的 svg 目录（第一轮与 fix1 的做法）；改指本版 svg 目录后重跑为 **8/8**。两次日志均保留（`freeze-pt-en2.log` 为误指记录，`freeze-pt-en2b.log` 为正确重跑）。

## 4. 观察项（不计缺陷）

- **O1** — KIT 第 58 行与第 94 行称 `.text.md` 为「535 lines」，实测为 534 行（`wc -l` 与 `splitlines()` 一致，文件以单个换行符结尾）。与第一轮观察项 O4 同一问题，属 KIT 行数口径差 1，非版面内容问题。
- **O2** — KIT 称 `.text.md`「CJK 0」，文件内实有 6 处 U+FF5C 全角竖线（冻结 `Note｜`/`Key words｜` 标签格式，与核心同格式，非中文文字）。属 CJK 计数口径差异。
- **O3** — P1 `A SEMANA EM NÚMEROS　In numbers` 标题贴盒右缘、`O FUTEBOL` 末行贴盒底（第一轮 O8，occlusion 0 flags，渲染完整可见）。
- **O4** — P2/P3/P5/P6 中部大空白与 P2/P4 栏尾孤行（第一轮 O2，核心版式，与核心一致，非 fan-out 引入）。
- **O5** — P6 Note 框 `o chute a lucky guess`：`chute` 未出现在 P6 文章正文，但出现在当页 D 组词框与 Q100 题面，且核心中文注同样释 `chute`（第一轮 O1，核心版式、忠实转译）。
- **O6** — P8 注 55 `taça=the champions' trophy` 与 P4 注 `a taça trophy` 对同一词释义宽严不一（第一轮 O7）；含义未错，仅释义不一致。
- **O7** — P1 `#46581f` 填充计数版比核心多 1：家具行 `PORTUGUESE WEEKLY` + 全角空格在版内拆成两个 `<text>` 元素，核心为一个；徽章标签逐页与核心全同，非徽章问题。
- **O8** — fix1 遗留（非本版缺陷）：scratch 机制表 `furniture.py` FURN[en] `badge372` 仍为 `EXPLICATIONS`（stale），版内发货值为正确的 `EXPLANATIONS`；供协调员定夺。

## 5. 结论（报事实，不作定稿决定）

- 本轮独立全量复校发现 **缺陷 0 项**：fix1 的 6 处修复逐处核实全部改对、旧形为 0；8 版全文、150 题答案键、徽章、VOL、字号、全部机械门、事实与人名抽查均通过。
- 按 SOP §8.4，一整轮全量校对零问题；是否定稿由协调员决定。
- 本轮未修改任何成品；全部校对证据在 `scratch-proof-pt-en2/`（`gates/` 日志与 JSON、`render/` 10 张全新渲染图、freeze 重跑副本、`en-textdiff.json`、`en-p8size.json`）。

## 附：双 PDF SHA（完整串）/ 字节复核

- 印刷 PDF `A-Lucerna-VOL4.pdf`：12,932,451 字节；sha256 `0146a4202b015f44659b4bba067a7411f90891cb640085dee5fec2010bd06af1`；8 页；1462.5×2025 pt。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：1,102,777 字节；sha256 `a974ef7ccf7c879f58e3626d874d9ce18e3da5f2a35faef43717e81706254c80`；8 页；文字层 46,073 字节（webpdf 口径；pdftotext -layout 提取 110,380 字节，含版式空白）。
