# Lucerna 周报 · 简体中文正文 + 荷兰语讲解版（zh-CN × NL） — 生产 KIT

- **配对**：目标语 = 简体中文（正文，与简体核心版冻结一致）；读者母语 = 荷兰语（全部讲解：定义、语法、指令、P8 全部注释）。报头 Lucerna（中文版无冠词）。
- **期号/日期**：VOL.1 · 2026 年 10 月 19 日（周一）—25 日（周日），与核心版同一期。
- **源**：简体核心版 files/weekly-report-zhcn-vol1/（英语讲解）冻结扇出；核心 build 复制为 hidden_files/weekly-report-zh-cn-nl-build/ 后只改讲解层。
- **版式**：8 页（1950×2700），暖象牙底；页数 4 的倍数 ✓。
- **校对状态：独立校对 PASS**（2026-10-21，见 §11；建造者全量自校见 §9）。
- **Discord 投递**：暂停中（用户 2026-10-21 指令）——本版未发 Discord、未入仓，等待上层处理。

## §1 基线证明（铁律 1）

- 复制核心 build 后未改动先跑 `tools/freeze.py baseline`：核心自复现 **8/8 SVG 逐字节相同**，且工具复验核心文件未被改动。
- 收尾核心完整性：建造前保存的核心 8 SVG sha256（build 目录 core-svg-hashes-before.txt）收尾 `sha256sum -c` 全部 OK。
- 终稿可复现性：把终稿源码复制到独立 scratch 目录、改指输出后重跑 → 8/8 SVG 与交付件逐字节相同。

## §2 家具（实印样，以 tools/tables.py + NL 列已入仓页脚实样为准）

- P1 徽章（砖红 19.5pt 粗体）：`TEKSTEN IN HET CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`
- 每页页脚：`Lucerna · CHINEES WEEKBLAD VOL.1 · TEKSTEN IN HET CHINEES (VEREENVOUDIGD) · UITLEG IN HET NEDERLANDS` / 右 `Pagina N van 8`（8/8 页核验通过）
- 注释前缀：`Uitleg — `；P8 分隔符：`— Pagina N —`（1–8 全在）
- P1 版次线沿用核心中文串 `简体中文版 · VOL.1 · 双11 · 大闸蟹 · 霜降`（德语扇出先例；法语版单独改过，本版从多数先例）
- 说明：简报给的徽章/页脚字面（CHINEES VEREENVOUDIGD 语序、无括号）与 tables.py 派生式及 NL 列已入仓各版（ru-nl、ja-nl SVG 实样）冲突，按简报自身的冲突条款以实样为准，用 `(VEREENVOUDIGD)` 括号式与 `TEKSTEN` 复数式，与 NL 列全列一致。

## §3 总量与分布

- 总题数 **150**（A2 56 · B1 65 · B2 29），与核心一致。
- 分页 10/18/18/18/18/18/12/38；题型 完成句子 68 · 单选 50 · 词汇配对 20 · 完形单选 11 · 写作 1（注册表实测，与核心逐项相同）。

## §4 键差异登记（完整表）

注册表层逐项比对（核心 reg vs 本版 reg，scratch/dump_reg.py 实测）：**仅 #150 一项**，为写作题按读者语言改向，与全部简体扇出先例一致；其余 149 键与核心逐字节相同。本核心无「中文↔读者语」翻译题，故无其他可改向项。印刷层 tools/p8.py keydiff = []。

| # | 核心键 | 本版键 | 核心注释 | 本版注释 |
|---|---|---|---|---|
| 150 | (开放题，范文如下) | (open vraag — voorbeeldtekst hieronder) | Open task - the model answer is printed in section F above (148 characters) | Open vraag — de voorbeeldtekst staat hierboven in deel F, 148 tekens |

范文正文（148 字中文）冻结未动，仅前缀 «Model answer: » → «Voorbeeldtekst: »。

## §5 拼音规则执行核查（简体扇出定式）

- P8 全部 150 条注释：荷兰语正文；引用中文词一律带声调拼音（如 Shuāngjiàng、Chóngyáng、dìngjīn、wěikuǎn、mǎnjiǎn、zhōuwǔ、língchén）。
- 实测：注册表 150 条注释含汉字数 = **0**（建造中曾有 6 条 P7 量词题注释直引汉字词 #101–105、#108，已全部改拼音后重印）。
- 终稿答案区：150 条键行中全角括号 = **0**、括号内汉字 = **0**（SVG 实测）。
- 页内生词条保留「拼音 + 汉字 + 荷兰语释义」（先例：页内注释与 P8 注释分开处理）。
- 排版器把紧贴 CJK 的半角标点转全角的资产负债：建造中命中 3 处（P2 满减段冒号、P7 B1 段逗号、P8 注释 #102/#104 逗号），均在讲解层内改写句式/改拼音消除，终稿 strict-cjk 审计 added = 0 关闭（见 §8）。

## §6 P8 印刷

- 核心键式（查核心代码+SVG 实样）：`{n}. {key} — {note}`、写作 `{n}. ✓ {note}`（短横式）。按简报「答案生成代码逐字节不变」——本版保持核心原式未动（与 zh×DE 先例同；zh×FR/PT/IT/ES 改了圆括号式，本版从简报明令）。
- tools/p8.py compare：核心印 150 / 本版印 150，**CLEAN**（missing=[]、extra=0、按编号 EQUAL）。
- 荷兰语注释比英语长：首版 P8 键行折行 174 行 vs 核心 151 行，溢出页脚带；仅压缩 25 条注释措辞（事实与键不变，逐条记录于 build 的 scratch/trim_notes.py 及一处补修）使折行回到 **151 = 151**，键流终于第 3 栏 y=2366（栏底 2540）。

## §7 内容与日历复核（讲解层复核，正文冻结继承核心）

- 尾款：周二 10 月 20 日 20:00 ✓；霜降：周五 10 月 23 日 ✓；重阳：2026 年 10 月 18 日周日，回顾口径 ✓；立冬 11 月 7 日 ✓（真实日历逐项核过）。
- 蟹价：¥77.5 → ¥57.5，便宜 20 元，约 −25.8%（核心标注为计算值，本版讲解沿用「De echte, berekende daling…25,8%」口径）；产量约 1.01 万吨讲解作 10.100 ton。
- 图表：P4 251.928 vs 249.193 条长自 0 起精确比例（冻结几何，仅图注译荷兰语）；P6 6 px = 1 元，图注两行恰排进原位。
- 数字格式：讲解散文用荷兰式小数逗号（57,5；25,8%）与千分点（10.100）；印刷数据与答案键保留核心原形（251.928 等，属正文/键冻结面）。
- 红线：简体版零政治——正文冻结、讲解未引入任何政治内容。

## §8 工具门结果（终稿实测）

- `tools/freeze.py diff --strict-cjk`：8 页 added CJK 字符全 = **0**，TOTAL 0。各页 CJK 净减均有账：徽章/页脚英文串含的汉字（英语讲解等）被荷兰串替换、核心英文注释中直引的汉字词（霜降/重阳等）在本版按拼音规则去掉、P3 etvous 串内 霜降 一词同理。
- `tools/p8.py compare`：CLEAN（见 §6）。
- `tools/occlusion_audit.py`（自检先行通过）：终稿 1 flag = P2 LINEX（«Onthoud de zin: …» 下金线 y=1803–1805）——核心自身同 flag，像素裁定：核心与本版终稿卡片墨迹均终于 1802 行、线带内文字墨迹 0，两版像素剖面一致，属继承的已裁定非缺陷，不改。建造中另有 2 个真 BOXTITLE 溢出已修（见 §9）。
- P7 金句：8 条逐字与核心相同；去标点拼接计数核心 ×2 = 本版 ×2（逐条）；页标签 (p. 1)×2、(p. 2)×1、(p. 3)×1、(p. 4)×2、(p. 5)×1、(p. 6)×1 与核心全同。
- 图片：逐页内嵌图片与核心字节全同（1/1/2/2/1/2/0/0 张）；9 条图片署名全在（«Foto: …»；1896 体操图 «Foto: onbekende maker, 1896 — Publiek domein (Wikimedia Commons)»）。
- kinsoku：行首真闭口标点（，。、；：？！）】」) 两版皆 0；行首 «·» 为分隔符折行，核心自有 7 处、本版 4 处，同类非缺陷。
- 繁体字：终稿 SVG 繁体专有字形 0。
- 英文残留：全卷拉丁文本节点扫描，英语功能词/原版装置串 0 残留（«is» 等为荷兰语同形词）。
- 中间层禁用术语：paper 8 SVG + 本 KIT + operative 代码（build 目录 *.py 非 scratch）中英两形均 0；核心 build 无该类方法名（glossline 命名原样保留，无改名需要）。scratch/transform_nl.py 是变换脚本、含作搜索模式的核心原串，属披露例外，仅存于 scratch/。

## §9 建造缺陷与修复（建造者自校全量记录）

1. **P8 键行溢出页脚带**（首版）：荷兰注释变长，折行 174 vs 核心 151。修：25 条注释仅压缩措辞（scratch/trim_notes.py + #37/#137 补修），折行回 151，最终一进程重渲染零溢出警告。
2. **P1 BOXTITLE**：热搜框署名 «Bron: spiegel van de Weibo-zoektrends (rddh.cn)» 墨迹右端 1889.5 越框界 1885。修：措辞缩为 «Bron: spiegel Weibo-zoektrends (rddh.cn)》，复审消旗。
3. **P5 BOXTITLE**：双语框题 «这一周的高频词 · Woorden van de week» 墨迹 987.2 越框界 961（荷兰语比法语 «Mots de la semaine» 长）。修：尾段缩为 «Weekwoorden»，复审消旗。
4. **全角标点渗入讲解**（strict-cjk 首跑 3 字）：P2 满减段冒号紧贴 」被排版器转 «：»、P7 B1 例句逗号紧贴 」转 «，»、P8 注释 #102/#104 汉字后逗号转 «，»。修：满减段改破折号、B1 例句句式重排、6 条注释改拼音（§5）；重渲染后 strict-cjk added = 0。
5. **变换脚本自身两处事故**（未污染终稿）：(a) 一条替换误删 P2 季风句后半——自 scratch 逐字恢复后重跑核对；(b) 一条注释压缩把 «Chóngyáng» 误作含元音变体——已按正字法改正。两者均在交付前经注册表/节点级复查关闭。
- 一进程规则：全部重渲染均经 run.py 单进程单跑（共享注册表），零 FLOW OVERFLOW / HEAD TOO WIDE 警告。
- 建造者已逐页读完 8 张终稿卡片全文自校。

## §10 交付物与针脚（实测）

目录 files/weekly-report-zh-cn-nl/：svg/ ×8、cards/ ×8（1950×2700）、WEEKLY-KIT.md（本文件）、
- 印刷 PDF `Lucerna-VOL1-NL.pdf`：**55,558,312 B**，sha256 `94950a0ef36ee18d9faf7b59edc6bec16c841bb2543ea5961fb73327c72926d4`
- 网页 PDF `Lucerna-VOL1-NL-web.pdf`：**2,901,950 B**（< 7 MB ✓），sha256 `15f5301d142c7f3471cd1259d2686401830e92bc57f2c4eb0ba791f6e6358dfb`
- 构建代码：hidden_files/weekly-report-zh-cn-nl-build/（run.py 一进程入口；变换与核查脚本在 scratch/，含 trim_notes.py、dump_reg.py、final_checks.py、cjk-diff.txt 等审计留痕）

**独立校对：PASS**（2026-10-21，见 §11）—— 已过独立校对零问题门，未入仓、未发 Discord（待上层处理）。

## §11 独立校对记录（2026-10-21，校对员独立复跑，scratch 在 hidden_files/proof-zh-cn-nl/scratch/）

一轮完整独立校对零问题，无修复、无重渲染。

- **freeze baseline**：核心 build 副本未改动重跑 **8/8 逐字节复现**；收尾复核核心 8 SVG sha256 与基线记录逐一相同，核心未触碰。
- **freeze diff --strict-cjk**：全 8 页 added CJK = **0**。另做全页 CJK 字符流 diff：第 1–7 页差异只有删除、且全部为家具（页脚/徽章中文串、第 N 版/共 8 版）与讲解引用（P3 etvous 的霜降、P7 金句注的重阳改拼音），正文字句零增删改；P8 删除为键注内英文直引汉字（转拼音）+ 家具，键本体保留。
- **注册表独立转储**（两 build 各一进程）：150 = 150，页/级/题型元数据零差异（A2 56 · B1 65 · B2 29；分页 10/18/18/18/18/18/12/38）；**键差异恰为 {150}**，与 §4 登记逐字一致；范文从两版 P8 SVG 提取拼接 = **148 字逐字节相同**（算术链 260+60+40=360、−50=310、定金 30+尾款 280=310 自洽）。手工重推导抽验 P5/P6 共 36 题 + 跨页 10 题，全对。
- **p8.py compare**：**CLEAN** — 150 noted = 150 noted，集合 EQUAL，印刷层 keydiff = []。P8 键式短横式经核心代码 + SVG 实样确认，答案代码未动。
- **拼音专项**：注册表 150 条荷兰注含汉字 = **0**；#101–105、#108 六条量词注逐条定位，全转拼音且语义正确（wàitào/wéijīn/jīn/jiàn-gè-tiáo/língchén/zhōuwǔ）；终稿 P8 共 150 个键行节点，全角括号 = **0**、半角括号内汉字 = **0**（核心仅有的 2 处全角括号键行 #53（铜牌）、#147（尾款）已消除）；其余全角括号均为测验题干冻结内容、与核心逐组相同。Chóngyáng 全刊 9 处拼写全正，§9(b) 误写无残留。
- **遮挡审计**（自检通过）：终稿 1 flag = P2 LINEX，独立像素裁定为**继承非缺陷**——核心与本版卡片文字墨迹均止于 1802 行，1803–1805 线带内只有金线色 (179,160,106) + 底色 + 页框竖线、零文字墨迹，两版剖面同构（工具按字符串匹配报 NEW，不成立）。§9 的 P1/P5 两处 BOXTITLE 修复在终稿审计中消旗、缩短串在位。P8 答案区元素数两版同为 163、最大基线 y 同为 2514.92，键流无溢出（FOOTER 类 0 flag）。
- **其余**：家具逐页核实（徽章、页脚 ×8、「Pagina N van 8」×8、分隔符「— Pagina N —」×8、「Uitleg — 」页内 11 处），与任务书字面逐字一致，§2 的冲突说明与实测相符；P7 八条金句逐字同核心、页标签 (p.1)×2 (p.2)×1 (p.3)×1 (p.4)×2 (p.5)×1 (p.6)×1、全刊出现次数逐条与核心相等 [2,2,2,2,2,2,3,2]；kinsoku 行首真闭口标点两版皆 0（行首「·」核心 7 / 本版 4，同类分隔符折行）；繁体专有字形 0；英文装置串残留 0（Notes｜/Photo:/Model answer 等全无）；图片逐页张数 1/1/2/2/1/2/0/0 且载荷哈希与核心逐页相同，9 条 Foto 署名与核心 Photo 署名逐条对应（作者/许可不变、仅标签译荷）；P6 条形 465/345 与 77.5/57.5 精确同比、自 0 起，−25.8% 为计算值（20÷77.5=25.8%）；P4 图注数字 251.928−249.193=2.735 两版保留；日历实测 2026-10-20 周二、10-23 周五、10-18 周日、11-07 周六全对；trim 25 条（含 #37/#137 补修）逐条核对为电报式压缩、键与事实不变；禁用术语在 paper/KIT/operative 代码 = 0，scratch/final_checks.py 唯一命中是断言检查行本身、transform 脚本为已披露例外；零政治（正文冻结、荷兰注通读）。
- **最终针脚（磁盘实测，与 §10 一致）**：网页版 **2,901,950 B / 15f5301d142c7f3471cd1259d2686401830e92bc57f2c4eb0ba791f6e6358dfb**（< 7 MB）；印刷版 **55,558,312 B / 94950a0ef36ee18d9faf7b59edc6bec16c841bb2543ea5961fb73327c72926d4**。
- 备注：§9(a) 所称「P2 季风句」在核心 build 与核心 SVG 全文检索无此词，措辞无从核对；但终稿经字符流 diff 证明 P2 正文与核心逐字一致（仅家具删除），该事故无残留，不构成缺陷。

## D5 重建记录（2026-11-14，D5-only）

SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader（ru 读者版 Latin AND Cyrillic → Noto Sans，D26 旧分支）。
施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：
`hidden_files/d5-redo/scratch-2026-w43-zh-cn/logs/2026-w43-zh-cn-nl/`；
逐版报告：`production/notes/2026-w43/g-zh-cn/scratch-d5-rebuild-zh-cn/D5-REPORT-2026-w43-zh-cn-nl.md`。

**装机**：installer 无法在 face= 引擎上运行（`cmap: pattern found 0x, expected 1`），改由手 port
脚本 `scripts/d5_port_zhcn.py`（`scripts/install_zhcn.sh`，`logs/install.log`，`INSTALL DONE fail=0`）；
本版 port RC=0，路由单元测试 `scripts/test_d5_routing_zhcn.py` **FAILURES: 0**（66 PASS）；
fix2 块保留（5 处）+ `_QUOTE_CLS` 4 处；装后 `_D5_READER = "latin"`（mode=latin variant=SC），
svglib.py 与基线差 99 行。

**基线**（修前生产版）：run TOTAL 150，0 警告；印 PDF 65,334,695 字节（SHA-match）；
印/网文字层差 0（24,236 字符）；残差 {·:164, —:1}；修前普查 D5 拉丁 468、西里尔 0、
弯引号在 CJK 0；基线 P8 noted 150/150。

**缺陷与修法**（run1 → run2；修法只动字号/内容侧几何常数，未动任何文字内容；每处修复后全量重渲 + 全部门禁重跑）：

| # | 门 | 位置 / 内容 | 实测 | 修法 | P8 |
|---|---|---|---|---|---|
| F1 | G6 occlusion | P1 版行 `TEKSTEN IN HET CHINEES (VEREENVOUDIGD)　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`（content12.py:23，16pt sans，anchor middle x=975，y=612） | Newsreader 荷兰语 run x=850.0，墨水右缘 1499.2；`本周热搜`标题墨水起于 1461.5 → 重叠 37.8×6.0px。基线（单 CJK run）总宽 926.5px，右缘 1438.3，occlusion 0 flags——D5 引起（整行 926.5→1048.5px）。PIL 实测：15pt → 右缘 1466.5（仍盖 −5.0px）；**14.5pt → 右缘 1450.2，余量 11.3px**；14pt → 1433.8（27.7px） | `content12.py:23` 16→**14.5**（15pt 不够——实测，非假设） |

**门禁 run2（全套 17 门 + D18，ALL-GREEN）**：run TOTAL 150、0 警告；head_check 0；d5 census lat 0 / cyr 0 / curly_cjk 0 / noto 0；
render RC=0；webpdf RC=0（2,901,950 B < 7 MB）；occlusion 0 flags；p8 extract noted 150/150；
p8 compare **CLEAN**（core 150 vs 本版 150，missing=[] extra_count=0 keydiff=[]；[108] 两边都在，无 EXTRA_ONLY、无 SHORT）；
freeze baseline 8/8；freeze diff 新增 CJK 字符 0（新增拉丁 strings 275，run 拆分所致）；
spill 0；boxtitle 0 DEFECT（41 titles，457 body lines，1 marginal）；
edge 0/0；creambox PASS 0 defects；文字层 print=web 差 0（各 24,236 字符）；
text.md BYTE-IDENTICAL（41,871 B）；15b CARRYOVER FAIL（241/2463；基线对照亦 FAIL 219/2445），按 D27 口径验收。
native verifier 907/907 UNEXPECTED 0；census_quotes 0 defective；本家无 gates.py；
D18 刊头 slogan/date 间隙 333.6px PASS。P8：834 节点，距页脚线余量 35.85px（正，无溢出）。

**新交付物**：印 `Lucerna-VOL1-NL.pdf` 55,558,312 字节（SHA-256 `94950a0ef36ee18d9faf7b59edc6bec16c841bb2543ea5961fb73327c72926d4`）；网 `Lucerna-VOL1-NL-web.pdf` 2,901,950 字节（SHA-256 `15f5301d142c7f3471cd1259d2686401830e92bc57f2c4eb0ba791f6e6358dfb`，< 7 MB）；
text.md 与 fanout BYTE-IDENTICAL（SHA-256 `a52d3cd4e3c7506d10a1bb3563aa41dc15c1f55fcd433b2611419aca68b68afe`）。D5 前值：印 67,300,871 字节、网 3,222,500 字节（`075d90fe…`，issues 已发版）。
练习仍为 150 题。
