# WEEKLY-KIT — A Lucerna VOL.1 · PT × KO edition

**配对：葡萄牙语正文（巴西葡语）+ 韩语讲解（포르투갈어 텍스트 · 한국어 해설，해요체）· W43（2026-10-19–25）**
**状态：PASS（独立校对完成：另发现并修复 5 处韩语孤行/碎片后整轮重跑，终轮零问题；记录见 §13）**
建造：核心 build 副本 `hidden_files/weekly-report-pt-ko-build/`（一进程 driver `run.py`），讲解层变换 = AST 精确值替换（scratch/extract.py + scratch/mapping.py + scratch/transform.py，483 个字符串节点，覆盖断言全过：未覆盖 0、冗余键 0）。家具列：**KO 列**（照 EN×KO KIT §3 定式，目标名换 포르투갈어、刊头 A Lucerna）。

## 1. 基线与核心完整性

- 动工前 `tools/freeze.py baseline`（--build 核心 build --core-svg 出货核心 svg）：**8/8 逐字节复现**。核心出货 SVG sha256 前缀：p1 082acac0811f1efa · p2 c4a853ac6ba9f623 · p3 bba9906a0115cbbd · p4 b99417547786bd64 · p5 4a1121e8bc76fb8d · p6 0d0ad43604c48a3a · p7 d3dc772b47960626 · p8 8a944c118fde0815。
- 收尾复跑 baseline（两次）：**8/8 仍逐字节一致**，核心零改动。副本 OUT 改道经 expanduser 写法全量核查（6 处 `os.path.expanduser("~/…/weekly-report-pt-ko/…")`，首跑前打印验证）；从未在核心 build 目录内 import 任何模块。
- 核心印刷集以 `tools/p8.py extract` 独立导出：**150 条全量**（见 §4）。

## 2. 总量（与核心逐项一致，注册表双 dump 对照实测）

- 总题数 **150 = A2 44 · B1 75 · B2 31**；分版 10/18/18/18/18/18/12/38（core/KO 两注册表逐条对照：n/page/level 全等）。
- 题型（KO 标签 → 计数）：문장 완성 61 · 객관식 49 · 빈칸 객관식 13 · 단어 짝짓기 12 · 문장 만들기 7 · 번역 4 · 진위 판단 3 · 쓰기 1（合计 150，与核心题型逐项对应：完成句子/单选/完形单选/词汇配对/造句/翻译/判断对错/写作）。
- 范文 92 词（程序计数，与核心一致）。

## 3. KO 列家具定式（照 EN×KO §3，逐项登记）

| 部位 | 定式（逐字） |
|---|---|
| P1 徽章（y=372，19.5pt sans **粗体 BRICK**，居中；取代核心葡语副题行——PT 家族 JA/RU 扇出同槽位先例） | `포르투갈어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판` |
| P1 顶带中行（strapline） | `TODA SEMANA EM PORTUGUÊS · 매주 발행 · 브라질이 읽는 포르투갈어` |
| P1 报头衬线行（y=330，40pt serif 粗体） | `포르투갈어 주간지 · VOL.1 · O SEGUNDO TURNO · O DEBATE FINAL · O ENEM VEM AÍ` |
| P1 黑带右行 1（24pt 粗体 #b3a06a，右锚） | `일요일은 결정의 날` |
| P1 黑带右行 2（21pt #b3a06a，右锚） | `대통령 선거 결선 투표 · 6면 참조` |
| 页脚左（每页，20pt） | `A Lucerna · 포르투갈어 주간지 VOL.1 · 텍스트는 포르투갈어 · 해설은 한국어` |
| 页脚右页码（每页） | `제 {n} 면 / 총 {total} 면` |
| gloss 前缀（bslib4 `gloss()`） | `해설 — `（单前缀；核心 gloss 串内无自带前缀，无叠印） |
| 讲解行方法 | `expl()`（由核心 bridge() 改名；调用点逐文件与核心全等：content12 4 · content34 7 · content56 6 · content7 3 · content8 1，合计 21） |
| P8 页分隔 | `— 제 {pg} 면 —` |
| P8 答案注式样 | **短横式（PT 家族）**：`{n}. {key} — {note}`，写作题 `{n}. ✓ {note}`——答案生成代码与核心逐字同（PT×EN/RU/JA/DE 扇出代码实证同式，README 第 8 条口径以核心 SVG/代码为准） |
| P8 印刷集 | 核心全 150 注皆印（无长度阈值路径），本版同代码路径强制同集（见 §4） |
| 节头双语式 | 葡语原题 · 韩语短名，如 `VIDA · 생활`、`CULTURA · 문화`、`ESPORTE · 스포츠`、`JOVENS · 청년`、`APROFUNDAMENTO · 심층`、`LÍNGUA · 언어`、`AVALIAÇÃO E RESPOSTAS · 평가와 정답` |
| 盒标题韩语后缀 | **从简**：P1 数字盒 `A SEMANA EM NÚMEROS · 숫자`（核心自家标题 `· 数字看本周` 墨迹 968.5 > 框界 961.0 的已知化妆旗为冻结核心项，本版短后缀不继承——终版审计该旗消失，见 §9） |
| 题型标签 | 문장 완성 / 객관식 / 빈칸 객관식 / 단어 짝짓기 / 문장 만들기 / 번역 / 진위 판단 / 쓰기 |
| instr 标签 | 빈칸 채우기 / 문장 만들기 / 번역 / 참 / 거짓 / 쓰기 / 단어와 뜻 짝짓기 |
| P7 页标签 | 逐字保留核心葡语 `(Página N)`（计数门以此为准，见 §6） |
| 讲解语体 | 해요체；注文多用名词句，数字用阿拉伯数字 + 韩语量词（투표소 4.352곳） |

## 4. 印刷注释门（PT 家族硬性项）

- 核心印刷集（p8.py extract 独立导出，短横式解析）= **150**（全题号 1–150）。
- 本版答案生成代码与核心逐字同（短横式、无阈值），故印刷集由构造同集；`tools/p8.py compare`（终版）：**CLEAN，core 150 = edition 150，missing=[]，extra=0，uncertain=[]**。
- compare 报告 keydiff=[3, 8, 58, 98, 101, 137, 138, 146, 147, 148]——按 README 第 13 条裁定：**注册表逐字节对照（权威）证键差异仅 [137, 138, 150]**；其余 8 项逐项以印刷行实证为提取伪影（如核心行 `101. confiro — conferir：eu → confiro（不规则）` 与本版行 `101. confiro — conferir: eu → confiro (불규칙)` 键部逐字同，差异仅注内全角→半角括号触发解析分界漂移；#3/#8/#58/#98/#146/#147/#148 印刷行键部与核心逐字同，已逐条摘录核对）。#150 为 ✓ 装置行，p8 提取口径不入 keydiff，注册表证之（见 §5）。

## 5. 键差异登记（注册表逐字节对照为权威；全表仅 3 条）

| # | 类别 | 核心键 | 本版键 |
|---|---|---|---|
| 137 | 翻译题（葡→读者语） | 周日，巴西重返投票站。 | 일요일, 브라질이 다시 투표소로 가요. |
| 138 | 翻译题（葡→读者语） | 出门前，核对你的投票地点。 | 집에서 나가기 전에 투표 장소를 확인하세요. |
| 150 | 写作装置项（键本身为装置文本） | （开放题，范文如下） | (열린 문제 — 모범 답안은 아래에 있어요) |

- 题干改向（键为葡语、逐字节不变，仅题干呈现句改向）：#139 题干中文源句 → `"기타" 검색량이 53% 늘었어요. → ___`；#140 题干中文源句 → `도착하면 투표소를 확인하세요. → ___`。
- #150 注同步译：范文见本版 H 区（92 词）→ `모범 답안은 이 면 H 칸에 있어요 (92 단어)`；H 区讲解行同步：`쓰기 문제예요 (하나의 정답은 없어요); 모범 답안은 아래에 있어요 (92 단어).`
- **语言中立注 9 条逐字未动**（逐条核）：#16 `conferir：ele → confere` · #17 `abrir：ela → abre` · #18 `levar：nós → levamos` · #19 `digitar：ele → digita` · #20 `fechar：ela → fecha` · #57 `66.026 > 66.000：maior` · #87 `900 − 250 = 650` · #102 `conferir：você → confere` · #103 `começar：ela → começa`。
- 其余 141 条注全部译韩（150 − 9 中立 = 141，注册表实测）。

## 6. gloss 与 P7 逐条点数

- `gloss()` 调用逐文件与核心全等：content12 1 · content34 2 · content56 2（P2–P6 各一盒），词条逐条保留、一项不少；渲染串计数 P2–P6 各 1 条 `해설 — ` gloss 串 = 核心各 1 条。`expl()` 调用 21 处全等（§3）。
- P1 讲解行 1 条（해설 — segundo turno …）与核心讲解行一一对应。
- P7 金句 8 条葡语逐字 = 核心（freeze diff 葡语多重集核验，§7；两种拼接计数法下每条计数与核心逐项相等）；页标签计数逐条 = 核心：`(Página 1)` ×2 · `(Página 2)` ×2 · `(Página 3)` ×1 · `(Página 4)` ×1 · `(Página 5)` ×1 · `(Página 6)` ×1（共 8；**独立校对订正**：原登记 ×2/×3/×1/×1/×2/×2=11 与核心、本版 SVG 原文实测均不符，属建造者登记错误，版面无缺陷）。
- P7 读者信（Mei, Xangai）葡语逐字继承核心（编辑部示例信，韩语注 `편집부 예시 편지예요. VOL.2에는 실제 편지와 8면 최고의 글을 실어요!`）。

## 7. 冻结层核验（freeze.py diff，终版）

- **新增汉字 = 0**（含汉字的新增字符串 0 条；新增 CJK 共 3,195 字，全部为韩字音节，属讲解层预期项。注：建造者原报 3,211；独立校对 5 处孤行修复共缩短讲解 16 字，终版实测 3,195，§13）。
- 移除侧非汉字字符串仅 11 条，逐项裁定：P1 葡语副题行 1 条（被韩语徽章取代，§3 定式）；P8 分隔 `— PÁGINA {n} —` 8 条（韩式分隔取代）；折行碎片 2 条（P6 D 组 expl 行葡语词表 `absoluta · votos válidos · intenção de voto` 断行点移动——四词在终版 P6 全部在场；P7 诊所行 `debate。` 标点残片——韩语注句号本地化）。**非讲解项移除 = 0**；葡语正文文本多重集与核心全等。
- 内容红线实测：全期百分比多重集与核心全等（全部为谷歌搜索兴趣数据并如此标注，**无任何选情/投票意向百分比**，讲解层未新增任何选情数字）；Copa do Brasil 半决赛全部刊 **11 月**（1º.11 两场、7.11、8.11，冻结继承 + P4 表格与注「são em novembro」逐字在场）。

## 8. 缺陷与修复（建造者自校全量；均为讲解层，几何/正文冻结）

- ① P7 第三栏增高 +29.5px：诊所第 2 条韩语注折 2 行（核心中文 1 行），栏底 1751.5 → 金句区 fy 被推高、末行金句译文压下期预告框（遮挡审计 2 面 COVER 新旗）。修复：注缩短为 `en/la는 스페인어예요; 포르투갈어는 na예요.`（1 行，363.8px；em+a=na 机制在同条葡语改正行内已印），栏底回到 **1722.0 = 核心几何**，审计 0 旗。
- ② P3 E VOCÊ 韩语注折行后行首孤「?」：改写为 `악기를 연주하나요? 배우고 싶은 악기는요? 두 문장을 써서 보내 주세요.`，折行干净（盒高公式同测，eh 不变）。
- ③ P8 孤行音节 2 处：#138 行末 `요` 孤行 → 注改 `Confira = 확인해요`（整行 1 行）；#139 行末 `요` 孤行 → 注改 `cresceram = 늘었다는 뜻이에요`（末行 5 音节）。
- ④ 孤行 `요.` 2 处：P4 D 组 expl `…완성하세요.` 末音节孤行 → 改 `…완성해요.`（1 行）；P7 B1 expl 末行孤 `요.` → 句首精简（`한 주의 일은 과거형(pretérito perfeito)으로 써요; …`），末行完整。
- 终版孤行扫描：孤行标点（韩语语境）= 0、孤行音节（含带标点形）= 0。余留行首 `·`/`—` 均为冻结葡语（对话行、选项续行、P8 分隔）与 gloss 分隔符续行（核心 P6 gloss 自身同式折行，继承式样，非缺陷）。

## 9. 遮挡与几何审计（终版）

- `tools/occlusion_audit.py`（自检先行 OK）：终版全册 **0 旗**；核心 1 旗（P1 数字盒标题 BOXTITLE，墨迹 968.5 > 框界 961.0——任务书登记的冻结核心化妆项），本版短后缀标题不继承该旗，**NEW vs core = 0**。
- 同行墨迹扫描（linescan.py，README 第 10 条）：8 页同基线碰撞 = **0**（P1 顶带重点复核：衬线行韩语段与葡语关键词无碰撞）。
- 图表标签元素级检查（README 第 12 条）：P6 图表区文本元素 19 = 核心 19，5 个数值标签（+900%/+550%/+350%/+350%/+250%）逐字全等、墨迹不被条形遮盖；P1 搜索盒元素 18 = 核心 18，数值标签同集全等。条形几何代码未动。
- 韩语折行后逐行墨迹宽由审计 + linescan + 全页目检覆盖；构建日志零 FLOW OVERFLOW、零 HEAD TOO WIDE；P8 答案流终点 y=2429（底界 2552），P7 第三栏栏底 1722.0 = 核心。

## 10. 日历与红线

- 真实 2026 历法实测（America/Sao_Paulo）：Oct 19 Mon · Oct 21 Wed（Prova do Fazendeiro）· Oct 22 Thu（A Fazenda enquete）· Oct 23 Fri（Globo 末场辩论）· Oct 25 Sun（次轮投票 8h–17h）· Oct 31 Sat（Halloween）· Nov 1 Sun（巴西杯半决赛首回合）· Nov 2 Mon（Finados）· Nov 7 Sat · Nov 8/15 Sun（Enem）——与正文（冻结继承）口径全合。
- 讲解层未引入国际政治；未新增任何选情数字；巴西杯半决赛未被改成 10 月赛事（§7 实测）。

## 11. 交付物与针脚（实测）

`files/weekly-report-pt-ko/`：
- `svg/` ×8（sha256 前缀，**独立校对修复后终版**）：p1 340d0f9d1af74cc3 · p2 5488a2c7b8bd34b9 · p3 f8a1ff613b9aea62 · p4 d1ab731b6f23e895 · p5 b91745da2df38eef · p6 eee7c31f752b0fa2 · p7 71d408943b4f3221 · p8 8cf9e8d002ec96d5（p3/p6/p7 与建造者交付版逐字节同；p1/p2/p4/p5/p8 为 §13 五处讲解层修复页）
- `cards/` ×8 PNG（1950×2700）
- 印刷 PDF `A-Lucerna-VOL1-KO.pdf`：**11,187,883 B**，sha256 `ea6583c4990d212b47864e7492d582b41849379a7d51ca8f4d85c859097148d6`（8 页）
- 网页 PDF `A-Lucerna-VOL1-KO-web.pdf`：**3,567,693 B < 10 MB**，sha256 `716dbf2929db8fb83c5936983519fb070108f5c7830014f0b21ee4e1d2ffeb37`（8 页，1400px 宽 JPEG q85，核心配方）
- D5 rebuild (2026-11-13–14, see D5 rebuild section at the end of this KIT): print master `A-Lucerna-VOL1-pt-ko.pdf` **6659462 B** · sha256 `9e9c60c4743ec2cd5f6fc6b2fa69a35a4276a03e378fa65f8747b57bec79b71a`; render-web `A-Lucerna-VOL1-pt-ko-web.pdf` **3188341 B** · sha256 `f8c8a09781c5c394ad8ce00dac68d34a6fcefc8446e467cd1867a5cefe172d64`; web (issues-type) `2026-w43-pt-ko.web.pdf` **882668 B** · sha256 `7fa3fbf8bbc5cedeba8ed0e990303d517762399c3d6e3500aa6f5c1c1f7315db` (< 7 MB); text.md byte-identical to the shipped version (sha256 `fc6a0743ab225e9d80fec6247b280de40ac04febac21df77e05ac18cc5a3681e`). Pre-D5 KIT pins above (print 11,187,883 B (sha256 `ea6583c4…`); render-web 3,567,693 B (sha256 `716dbf29…`)) are D1-era values, already expired before this rebuild (toolchain drift: Bold/Italic subset split in tools/webpdf.py commit 40963281).
- （建造者原报针脚——网页 3,570,221 B / 72bc884b…、印刷 11,188,187 B / 490e9813…——经校对者实测属实，已被上列终版针脚取代。）
- `WEEKLY-KIT.md`（本文件）

## 12. 纪律声明与披露

- 一进程 driver 构建；副本中从未单独跑任何 content 模块（注册表 dump 亦为一进程全序导入，核心侧 dump 在 freeze baseline 的改道 scratch 副本内完成，从未在核心 build 目录 import）。
- 变换纪律：AST 精确值替换 483 节点，覆盖断言全过（未覆盖 0、冗余键 0）；结构编辑仅四项（expl 改名、P1 徽章行改式、P8 韩式分隔、render 输出 PDF 名加 -KO 后缀，PT×JA/RU 先例）。
- 残留扫描（终版 SVG 文本）：汉字 = 0、西里尔字母 = 0、荷/俄家具串 = 0；禁用中间层术语在成品 SVG = 0、operative code（build *.py）= 0。**披露**：共享库 `svglib.py` docstring 含核心原样继承的「重阳」二字（图片提示词）与 "weekly-paper" 词样——核心 build 原样继承、不渲染、非讲解层（各扇出副本同）；`scratch/residual.py` 的扫描词表本身含被扫术语字样，confined 于 scratch/、不入 operative code。
- 字体：tables.json 口径（Noto CJK 分割 TTC，svglib 按核心同管线选面）——8 页 cards 全页目检，韩文字形无缺字/方框，✓/«»/— 等符号与核心同款渲染。
- 未入仓、未发 Discord、未向用户发消息（按派工口径，待独立校对 PASS 后由主线 insert）。

## 13. 校对状态

- 建造者自校：全量一轮完成（8 页逐页目检 + 全部机械门），缺陷 4 类已修并复验（§8）。
- **独立校对：PASS（2026-10-22，校对者 fresh pass，scratch 在 `hidden_files/proof-pt-ko/`）**。建造者 §8 四类修复逐项在版实证（P7 诊所注一行化、栏底矩形与核心全等 1722.7；P3 注无行首孤「?」；P8 #138/#139 注无孤行；P4 D 组 expl 与 P7 B1 expl 无孤行「요.」），P4/P7 卡面像素目检通过。
- **校对者另发现并修复 5 处韩语孤行/碎片（建造者「孤行 = 0」自报不实 — 其扫描漏了带 `)` 的碎片元素与 P4/P8 两处）**，均为讲解层措辞、一进程 driver 重渲、未修复页（p3/p6/p7）逐字节不变：
  1. P4 E VOCÊ 注末行碎片 `세요.`（`보내 주/세요.` 词中折断）→ 注改写 `응원하는 팀을 두 문장으로 써서 보내 주세요.`（一行放下，盒高 −29，其余元素同文同位）；
  2. P8 #134 注末行孤词 `장소` → 注改 `S + V + O + 장소`（一行放下）；
  3. P1 数字盒注末行碎片 `소)`（`투표/소)`）→ `(주소가 바뀐 곳)`（注缩为 2 行）；
  4. P2 gloss 末行碎片 `적인 것.`（`의무/적인 것.`）→ `justificar 사유 설명`（gloss 缩为 3 行，末行完整词条）；
  5. P5 贴士注末行碎片 `이)`（`없/이)`）→ `(조금씩 복습, 벼락치기 없이)`（一行放下）。
  裁定非缺陷 2 处：P3 gloss 末行 `lado 나란히.`（词界断行、完整词条尾）；P5 指示行末 `있어요.`（完整谓语）。韩语正文按音节折行属本列常态，不作缺陷。
- 终轮全门实测（修复后整轮重跑）：freeze baseline 核心 **8/8**（首尾各跑，核心零改动）；freeze diff 新增汉字 0、新增 CJK 3,195 全韩字、移除侧非汉字恰 11 条与 §7 登记逐项合、葡语正文多重集全等；p8 extract 核心印刷集 150 独立复证，compare **CLEAN 150=150**；注册表双 dump 逐字段对照——键差异恰 {137, 138, 150} 与 §5 登记逐字合、题干差异 {139, 140} 印刷实证、注差异 141 条（全含韩字）、中立注 9 条逐字未动、150 键自正文手工重推导全对（含算式 982+514+431+312=2,239、350+350=700、900−250=650、总比分 3–2、66.026>66.000）；p8.py keydiff 余 8 项 {3, 8, 58, 98, 101, 146, 147, 148} 逐项证伪为提取伪影（注册表键逐字节同 + 印刷行键部同）；答案生成代码与核心 token 级同构（仅 expl 改名 21 处 = 逐文件 4/7/6/3/1、徽章 19→19.5pt 粗体、分隔/页码 f-string 译韩），短横式无阈值由构造同集。
- 红线：百分比多重集与核心逐项全等（900%×9 · 550%×4 · 350%×11 · 250%×7 · 75%×8 · 74%×6 · 53%×8 · 40%×4 · 100%×1 · 300%×1，全为搜索兴趣数据，讲解层零新增）；Copa 半决赛全刊 11 月（1º.11×2、7.11、8.11 + 明示句在版），novembro 计数 18=18；日历 America/Sao_Paulo 实测全合（Oct 25 Sun 次轮、Nov 1 Sun 半决赛、Nov 2 Mon Finados、Nov 8/15 Sun Enem）。
- KO 列定式逐项核（照 EN×KO §3）：徽章 (975, 372) 19.5pt 粗体 BRICK 逐字 `포르투갈어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`；顶带/衬线行逐字合；页脚 ×8 逐字、页码 `제 N 면 / 총 8 면` ×8；gloss `해설 — ` 单前缀（双前缀 0），gloss 调用 1/2/2 与词条逐条同数同序（5 盒 5/5/5/5/5 词头全等，含 content34 第二盒 5 条——校对者首轮切分误报已以原文证伪）；expl() 21 处逐文件全等；P8 分隔 `— 제 N 면 —` ×8。
- 几何兜底：occlusion_audit（自检先行）终版 **0 旗**、NEW vs core 0（核心唯一旗 = P1 数字盒标题 BOXTITLE 968.5>961.0 冻结化妆项，本版短后缀不继承，实证）；同行墨迹扫描 0 碰撞（含近失 <2px 亦 0）；图表元素级任意覆盖 0（P6 区 22 元素、P1 区 62 元素与核心同数，5 个数值标签基线与核心全等）；P7 矩形集与核心仅 4 枚级别签因译文长度流移、其余全等；孤行宽网终扫：碎片元素 0、行首孤标点 0，余 ≤3 音节元素全为家具/标签/已裁定项；P8 答案流最大基线实测 2535.6 < 2552（建造者 §9 的 2429 一数校对者未能复现，以实测为准，无版面影响）。
- 残留全扫：成品 SVG 汉字 0、西里尔 0、他列家具 0、禁用术语 0（operative code `bridge` 0——token 核查证改名彻底）；svglib docstring 披露项与 §12 同（核心继承、不渲染）。
- 未入仓、未发 Discord（按派工口径，待主线 insert）。

## D5 rebuild (2026-11-13–14, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-ko/`; per-edition report: `production/notes/2026-w43/g-pt/scratch-d5-rebuild-pt/D5-REPORT-2026-w43-pt-ko.md`.

**Install**: core landed with `apply_variant.py --patch-core pt --week 2026-w43` (production `core-pt/svglib.py`, `_D5_READER = "latin"` — the core template); this edition installed with `apply_variant.py --svglib patched/2026-w43-pt-ko/svglib.py --target pt --reader ko --week 2026-w43`, `_D5_READER = "cjk"` (--check dry-run clean, RC 0); routing unit test `test_d5_routing.py` FAILURES: 0; fix2 block kept (5 occurrences).

**Baseline** (pre-fix production build): run TOTAL 150, 0 warnings; print/web/issued text layers 37,657 = 37,657 = 37,657 chars, multiset diff 0; baseline web PDF 994,962 B; print PDF 9,380,654 B (`e4da4c27…`); pre-fix census D5 Latin 343, Cyrillic 0, curly in CJK 0; baseline P8 noted 150/150.

**Defects and fixes** (run1: 2 items, sizes only, no wording changed):

- P2-ex head `C　COMPLETE COM OS NÚMEROS`: content12.py:256 `e.head` 25→22
- P3-main head `DOIS INSTRUMENTOS, UM PAÍS`: content34.py:21 `f.head` 25→24

P8: 206→206 lines, footer slack 57.4→57.4 px.

**Gates run2** (16 gates; no family gates.py for pt) — **15/16 gates — textmd FAIL only (see note below)**: run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0 (curly_total=0); render RC=0; webpdf RC=0 (882,668 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 231, run splits); spill 0; boxtitle 0 DEFECT (39 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web 93,692 chars, multiset diff 0; textmd carryover **FAIL 83/68** (svg 5618 vs md 5603 tokens) — see note below; masthead gap (D18) 141.6 px PASS; census_quotes 0 defective.

**New deliverables**: print master `A-Lucerna-VOL1-pt-ko.pdf` 6,659,462 B (`9e9c60c4…`); render-web `A-Lucerna-VOL1-pt-ko-web.pdf` 3,188,341 B (`f8c8a097…`); web (issues-type) `2026-w43-pt-ko.web.pdf` 882,668 B (`7fa3fbf8…`); text.md byte-identical to the shipped version (`fc6a0743…`). Still 150 exercises.

**Exporter note**: pt has no `.text.md` exporter (verified: the `ru_textmd.py` trial differed by 757 lines). The issued `issues/2026-w43/2026-w43-pt-ko/2026-w43-pt-ko.text.md` is carried over BYTE-IDENTICAL; content identity is verified by `verify_textmd.py` carryover jointly with gate 15 (print=web text layer diff 0).

**textmd residual (frozen-tool limit, not a content defect)**: under the frozen `tools/verify_textmd.py` (additive pt calibration only — see family report §5.0b), this edition's carryover residual is 83/68 tokens. Clearing it needs generic-rule changes the coordinator has frozen; whether to allow them is pending the coordinator's decision. The print=web text layer (gate 15, 93,692 chars, multiset diff 0) independently confirms the content is unchanged.
