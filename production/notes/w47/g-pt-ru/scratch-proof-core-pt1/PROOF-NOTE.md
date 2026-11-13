# PROOF-NOTE — W47 core-pt 独立复校（fix1 后，re-proof）

- 复校员：独立复校（与构建者 / fix1 不同人）。日期：2026-11-11。
- 对象：`production/2026-w47/core-pt/`，fix1 本地 commit `4b688318`（未 push）。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-pt1/`（只写 goals 侧；生产文件只读，未 commit、未 push）。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` 通；goals 侧写 `probe-proof-core-pt1.txt` 成功。TMPDIR 全程在 scratch 下 `tmp/`。

## 结论：(b) 有问题 — 1 项轻缺陷（D5），其余全部通过

fix1 的 D1/D2/D3/D7 四处修复全部独立复测通过（PIL 真墨 + 2× 裁切目视双重验证）。
唯一缺陷是 D5：P4 译注 `o título 冠军` 歧义未修，歧义已实证造成 8/11 个 fanout 版取了“人”的义。
修法极小（两处各加“头衔”二字），但须重渲染 P4 并复测该 gloss 盒。**不定稿，需 fix2。**

## §0 三件 SHA（开工前核对，与任务所给一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | 25,311,644 | `98f44af82f82df7c7fec1014fff7098d0448bf775b2aeda484f2e69233235181` ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | 1,608,359 | `d1d26cd70823e83e6165268b055b481981cd5cc3bdcffaec40042f7bf28a521f` ✓ |
| `2026-w47-pt-zh-cn.text.md` | 36,876 | `9dd550b6d7d19703ce6643357e9aad3f5367dfc40379bd41d56db999fd36afbe` ✓（fix1 未动文案） |

附：印 PDF 8 页，1462.5×2025pt；网 PDF 同。印/网文字层逐字一致（见门禁表）。

## §1 fix1 四项逐项复测（PIL 真墨，渲染 PNG cards 1950×2700，与 SVG 坐标 1:1；墨 = 像素均值 <180，奶油盒 #f0eee5 均值 ~236 不计入）

| 缺陷 | 末行 / 位置 | 复测墨底 / 框底 | 墨底 clearance | 判定 |
|---|---|---|---|---|
| D1 | P1 EM POUCAS PALAVRAS 盒，末行 `em Brasília. (Página 4)`（基线 2327.6） | 墨行 2312–2332；框底 2348；2333–2348 无墨（2349–2350 是盒下 quiz 分隔线，不在盒内） | **+16px** | ✅ 通过（≥+5） |
| D2 | P3 schedule 盒，末行 `16h30.`（基线 540.6） | 墨行 526–540；框底 551；552–570 无墨 | **+11px** | ✅ 通过（≥+5） |
| D3 | P6 timeline 盒，末行 `Página do Participante.`（基线 840.8） | 墨行 825–845；框底 854；855–875 无墨（下盒顶 866，不挤压） | **+9px** | ✅ 通过（≥+5） |
| D7 | P8 范文 10 行（15pt，栏右缘 1862） | 10 行墨右缘 1723–1840，最紧行 `Zumbi e Palmares e escrevo duas frases em português.` 墨右 1840；SVG 计 90 词 = 88 + `Texto modelo:` | 距栏边最紧 **+22px**（余量 +22…+139） | ✅ 通过（无行超右缘，语义/词数不变） |

2× 裁切目视（`crop-d1/d2/d3/d7.png`）：D1 末行在盒内、盒底有干净奶油余量、quiz 线不再穿字；D2 `16h30.` 在盒内、下有白空隙；D3 `Página do Participante.` 降部不触边；D7 十行行末距栏边均有明显余白。与 PIL 数值一致。fix1 报告值（+16/+11/+9，D7 最紧 −22px）全部复现（D7 末行实测 1723 vs fix1 1722，1px 渲染舍入，无实质差异）。

## §2 D5 — P4 译注 `o título 冠军` 歧义（轻缺陷，未修）

- 现文案（两处，均未动）：
  - `content34.py:134`：`f.gloss("o agregado 总比分 · os pênaltis 点球大战 · a decisão 决赛 · o título 冠军 · a pausa 休整期 · a taça 奖杯。")`
  - `text.md:215`：`*译注｜o agregado 总比分 · os pênaltis 点球大战 · a decisão 决赛 · o título 冠军 · a pausa 休整期 · a taça 奖杯。*`
- 为什么是缺陷（不是“中文读者能看懂就算了”）：
  1. 文中 `o título` 两处皆指头衔：`O Grêmio busca o sexto título`、`A Mercedes garantiu o título de construtores`；“人”的义在此版无一处成立。
  2. 歧义已实证传播：11 个 fanout 版中，除 en 作 `o título title`（正确）与 zh-tw 沿用同样歧义的 `冠軍` 外，**8 版取了“人”的义**——fr `champion`、de `Meister`、es `campeón`、it `campione`、nl `kampioen`、ru `чемпион`、ja `優勝者`、ko `우승자`（均在各版 `content34.py:134` 实测）。核心 gloss 是共享源头，源头歧义即根因。
  3. 中文读者面理解未破（体育语境下“第六冠/夺得冠军”确可指头衔），故定级为**轻**，且无题键受影响；但按“根因修在源头”的规则，应在核心消歧，而非任由各 fanout 版各自猜。
- 修法：两处 `o título 冠军` → **`o título 冠军头衔`**（只加“头衔”二字；其余“冠军”用法——P8 简析“第六冠”、Q55 `taça=冠军奖杯`——均正确，不动）。修后重渲染，复测 P4 gloss 盒（现盒内余量 +47.7px，多两字仍有充分空间，但须实测确认换行）。
- 附带（非本版可修，需协调员另派）：上述 8 个 fanout 版的 P4 Note 各需一词修正（fr `champion`→`le titre`、de `Meister`→`Titel`、es `campeón`→`título`、it `campione`→`titolo`、nl `kampioen`→`titel`、ru `чемпион`→`титул`、ja `優勝者`→`優勝/タイトル`、ko `우승자`→`우승/타이틀`）；zh-tw 沿用 `冠軍`，同义消歧（`冠軍頭銜`）。

## §3 全文重读 + 150 键逐题语义核对（手验，非仅 p8 compare）

- text.md 全文已通读；150 题逐题对照正文核对题干与键，**零语义错误**。抽样记录（全量核对表见 GATE-LOG §5）：
  - P1：1–10 全对（20 日=周五、决赛 12 月 6 日、decidem，现在时 eles 形）。
  - P2：11–28 全对；25–28 配对与正文 gloss 一致（feriadão/ folga/ programação/ aproveitar）。
  - P3：29–46 全对；31 题关键区分 12.519（创日）vs 14.759（定为假日）；44–46 造句均为正文合法句（45 题省“último grande”不改义）。
  - P4：47–64 全对；52–55 配对正确；56–59 比较级方向正确（16h30 “mais cedo”）；60–64 过去时正确。
  - P5：65–82 全对；68/81/82（TRI、官方答案归属 Inep）与正文一致；76–79 将来时正确。
  - P6：83–100 全对；83–86 算术自洽（16–30 日共 15 天 = 10 工作日 + 5 周末/假日）；94 题“não contam”正确。
  - P7：101–112 全对；108 `saíram`（过去时复数，半决赛已赛完）；109–112 虚拟式将来（sair/for/tiver）正确，112 题排除 sai（陈述式现在时）与 saia（虚拟式现在时）。
  - P8：113–150 全对；120 题第二天 5 小时（13h30–18h30）；125 题“rodada 36”与“35 轮周三/周四结束、21 日周六打 36 轮”自洽；139/140 翻译句与正文 P5 计划句一致；141–144 配对正确；146/147 sexto/quinto 与两队杯赛冠军数一致（见 §4）；148 `na internet` 正确。
- 印 PDF RESPOSTAS 块与 text.md 逐项比对：150/150 一致（脚本 `keycheck.py`，RESPOSTAS-only 解析；Q134 嵌“1 a 1.”致解析器幽灵键，已用顺序解析排除，两侧对称，目视确认全句 `O Grêmio empatou por 1 a 1.` 两处俱全；Q150 `✓ 范文见本版 H 区（88 词）`一致）。
- 读者面内部语扫描：印 PDF 全文无 SOP/proofread/cover/TODO/placeholder；`VOL.3` 仅出现 2 次，均在 P7 读者来信说明内（门禁逐字核对过，允许）。

## §4 外部事实抽查（6 组，全部核实无误；2026-11-11 检索）

1. **Copa 半决赛 + 决赛**：Grêmio 1–1 Atlético-MG（11 月 7 日周六，Arena MRV；首回合 Grêmio 2–0，总比分 3–1）；Renan Lodi 先破门、Carlos Vinícius 扳平（与正文一致）；Vasco 2–1 Palmeiras（11 月 8 日周日，São Januário；首回合 Palmeiras 1–0，总比分 2–2），点球 5–4 帕尔梅拉斯晋级；决赛 12 月 6 日周日、单场、Mané Garrincha（首届单场决赛）；Grêmio 第 10 次进决赛、冲第 6 冠（1989/1994/1997/2001/2016 五冠），Palmeiras 冲第 5 冠（1998/2012/2015/2020 四冠）。来源：sounoticia / estacaolivremt / minutonoticia / edmaisesporte / sportradar / obairrista；brasileirao.com.br（第 5 冠）、mktesportivo（Grêmio 五冠年份）。
2. **F1 圣保罗**：11 月 8 日周日 Interlagos，Norris 杆位夺冠（71 圈 1:35:23.504），Verstappen 第 2（+14.602，自第 21 位发车），Hadjar 第 3（+24.485）；Mercedes 凭 Russell 第 4 + Antonelli 第 5 锁定车队总冠军（第 9 冠，2021 年后首冠）。来源：Reuters 经 businessday / appistos（引 FIA 官方战报）/ racer.com。
3. **Enem**：Edital nº 64/2026；两天 11 月 8/15 日周日，第一天 13h30–19h（redação/Linguagens/Humanas），第二天 13h30–18h30（Natureza + Matemática 各 45 题 = 90 题）；官方答案“até o 10º dia útil após o 2º dia”；自 11 月 16 日起计，扣 11 月 20 日假日与两个周末，10 个工作日 = 11 月 16–30 日共 15 天（10 工作日 + 5 休息日），正文“27–30 日”区间如实覆盖了不同计法（27 日为把 20 日计入的算法）；个人成绩 2027 年 1 月、Página do Participante；TRI 按连贯性与难度计分。来源：focaedu / estacio / centerdrop / techtudo / sisu.pro.br（27 vs 30 日分歧均有据）。
4. **黑人意识日**：Zumbi 1695 年 11 月 20 日身亡；Lei 12.519/2011 设日（非法假日）；Lei 14.759/2023（2023 年 12 月 21 日签署）定为全国假日；2026 年 11 月 20 日确为周五，三天连休。来源：afrocultura / axefinder / ocalendario / pt.wikipedia。
5. **国家队友谊赛**：巴西 × 新加坡，11 月 17 日周二 7h（巴西利亚时间），新加坡国家体育场（CBF 官宣：另对日本 11 月 14 日周六 7h15）。来源：cbf.com.br。
6. **日历骨架**：`date` 核对 13 个日期的星期全部与正文一致（11 月 7 日周六、8 日周日、15 日周日、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、27 日周五、30 日周一、12 月 6 日周日）；11 月 27 日确为周五（Black Friday）；Enem 报名 5,051,345 人已确认（Inep Painel，gov.br）——正文“Mais de 5 milhões de inscritos”属实；“Nubank Parque”为现名（Allianz Parque 于 2026 年 5 月 4 日球迷投票后更名）。

## §5 门禁结果（全过；详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| gates_core.py | 16/16 PASS，FAILURES: none |
| occlusion audit | 0 flags（自检 6 类阳性全触发） |
| creambox.py 全版 | 31 盒，0 真溢出（6 处 BELOW-WINDOW 皆已知假阳性类；6 处 desc-clear 负值皆中文/数字无降部字母，PIL 真墨复测余量 +3.5…+6px） |
| p8 extract | 150/150 |
| p8 compare | CLEAN（missing=[]，keydiff=[]） |
| freeze baseline | 8/8 SVGs byte-identical，core 完整性 8 文件重哈希无改动 |
| freeze diff | +0/−0，新增 CJK 0 |
| 印/网文字层 | 各 104,916 字节、7,262 词，词多重集差 0；弯引号 “ ” 各 3、’ 0、«» 各 40，两版一致 |
| P8 最小字号 | 10.12pt（全版最小亦 10.12pt，仅在 P8）≥ 9.75pt |
| ABSTRACT.txt | 含 masthead “A Lucerna 葡萄牙语周报 VOL.4”（SOP §9）✓ |
| keycheck（印 PDF RESPOSTAS vs text.md） | 150/150 |

## §6 缺陷清单（仅 1 项）

| # | 位置 | 缺陷 | 严重度 | 修法 | 复测 |
|---|---|---|---|---|---|
| D5 | P4 译注，`content34.py:134` + `text.md:215` | `o título 冠军` 歧义：o título 指冠军头衔，中文“冠军”兼指头衔与冠军本人；已致 8 个 fanout 版取“人”义 | 轻 | 两处 `o título 冠军` → `o título 冠军头衔`，重渲染，复测 P4 gloss 盒 | 修后重跑本复校的 D5 项 + P4 盒 PIL |

## §7 备注

- fix1 FIX-LOG 称 D5“曾评估是否顺手修”但未修；本次独立复核的结论不同：歧义已有 8 版实证传播，属根因缺陷，见 §2。
- P6“27–30 日”区间写法是诚实处理（27 日与 30 日两种计法均见于公开报道，见 §4.3），不作缺陷。
- 生产文件只读：除核对 SHA 与渲染 PNG/PDF 读数外，未改 repo 内任何文件；未 commit、未 push。fix1 的本地 commit `4b688318` 状态未动。
- 工具：正典 creambox `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与 fix1 核对一致）；未用窄带版作证据。
