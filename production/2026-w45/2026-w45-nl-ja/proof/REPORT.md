# W45 NL×JA 分版独立校对报告

- **对象**：`files/weekly-report-w45-nl-ja/`（VOL.2，NL×JA）
- **校对员**：独立校对（只校对、不改源码、不宣布上架、未派生下级代理）
- **结论：ZERO PROBLEMS（可定稿）**
- **校对时间**：2026-10-27（UTC）晚间；交付物终态 mtime 22:04:16 前已冻结，校对全程交付目录零新写盘

## 开工查重（stand down 检查）

- 22:05 首次检查：`files/weekly-report-w45-nl-ja/` 与 `hidden_files/weekly-report-w45-nl-ja-build/` 最新 mtime 为 22:04:16（WEEKLY-KIT.md），无 nl-ja 相关进行中进程。
- 90 秒后复查（22:06:59）：两目录 mtime 零变化；唯一运行中的同类进程属于 nl-pt 分版，与本分版无关，未触碰。
- 结论：已完成交付的新鲜 mtime + 90 秒零新写盘 = 安全开工，未 stand down。
- 校对全程：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录（只读对照）、未清理共享 scratch 目录。所有中间证据写在本科对目录与 /tmp（自用），源码与交付物零改动。

## 交付物终态指纹（校对前后一致）

| 文件 | 大小 | sha256 |
|---|---|---|
| De-Lucerna-VOL2-JA.pdf（印刷） | 20,540,632 B | `64fb9b6d95ca844d0bc98fbfe85db96ec53c791dd54cfd574fec1da214f17b40` |
| De-Lucerna-VOL2-JA-web.pdf（网页） | 3,584,046 B | `3b18ca1a9ca6b76114b8cccd3f40999c41cf5eff829829287b0af170870cbbf4` |
| svg/p1–p8 | — | 与 `hidden_files/weekly-report-w45-nl-ja-build/final-sha256.txt` 逐项一致 |
| PDF 页数（/Type /Page 计数） | 印刷 8 页 / 网页 8 页 | — |

与任务书给出的两 PDF 哈希逐字节一致。校对前后核心 SVG 哈希不变（见 §1）。

---

## 1. 冻结：核心复现 + 新增 CJK + 纯荷兰语删串

### 1a. freeze.py baseline（tools/venv/bin/python 独立重跑）

```
baseline: 8/8 SVGs byte-identical
  OK p1 5424557b… / p2 78e6fcd2… / p3 5b9854e3… / p4 cc227fd9…
  OK p5 e58064c9… / p6 6583fe28… / p7 65cfe2b3… / p8 fe22a151…
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```

校对前后核心哈希逐项比对：**不变**（`core-before.txt` = `core-after.txt`）。

### 1b. 新增 CJK（freeze.py diff 独立重跑，与构建员自述逐页一致）

| 页 | 核心 CJK → 分版 CJK | 新增 CJK 字符数 | 构建员称 | 核实 |
|---|---|---|---|---|
| p1 | 191 → 299 | 246 | 246 | ✓ |
| p2 | 212 → 319 | 267 | 267 | ✓ |
| p3 | 153 → 259 | 211 | 211 | ✓ |
| p4 | 126 → 211 | 178 | 178 | ✓ |
| p5 | 214 → 311 | 258 | 258 | ✓ |
| p6 | 192 → 305 | 253 | 253 | ✓ |
| p7 | 373 → 522 | 403 | 403 | ✓ |
| p8 | 1033 → 1571 | 1271 | 1271 | ✓ |
| **合计** | | **3087** | **3087** | ✓ |

新增 CJK 共 332 个不同字符：假名 + 标点（、。、「」『』・ー（）？～ 等）+ 标准日语汉字（如 毎週号、気候週間、植樹、節約、警報、博物館、見本市、成績、注目、順位表、島、競技、試練、投票、気象学者、警報疲れ、固定、助言、賛成者）。全新增字符串已通读：无简体中文特有字形；全刊严格简体字扫描为空（说/话/让/这/那/汉/认/识/读/词/语/译/个/们/发 全部 0 处）；中文全角逗号 ，0 处。新增汉字均出现在标准日语词形中，无中文词形混入（词语级排查见 §4）。

### 1c. 纯荷兰语删串逐项裁定（无冻结荷兰语句丢失）

对“不含任何 CJK 的核心字符串”做多重集差分，全部删串均有合法归属：

| 页 | 核心独有（纯荷兰语） | 裁定 |
|---|---|---|
| p1 | `DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS`（1 条） | strapline → P1 徽章（见 §9），构建员称属实 |
| p4/p5/p6 | `Van de redactie van De Lucerna · Leesniveau:` + 单独的 `B1`/`B1`/`B2` | 署名/说明换行碎片合并：分版为单条 `Van de redactie van De Lucerna · Leesniveau: B1（/B2）`，文本拼接后逐字同，构建员称属实 |
| p7 | `。`、`zij zette vast。`、`bomen。`、`thuis。`（4 条） | 仅为换行切点移动：荷兰语词全部在分版对应行中保留（`een は単数、複数は bomen。`、`vastzetten 固定する：zij zette vast。`、`目：blijf ik thuis。`），无丢失 |
| p8 | 8 条 `— PAGINA n —` 分隔符 + `104. blijf — rood = blijf binnen` | 分隔符 → `— n ページ —`（W43 同式，见 §9）；#104 注由荷兰语译为日语 `104. blijf — rood = 屋内にいよう`，构建员称属实 |
| p2/p3 | 无 | — |

其余所有删串均为含中文的说明层字符串，分版均有对应的日语说明（已按 freeze-diff 全量逐条对照，见本科对目录 `freeze-full.txt`）。**无冻结荷兰语句丢失。**

---

## 2. P7 词框冻结：定义句逐字保留，仅 gloss 本地化

词框（HET WOORD，x=1473）三行定义句文本**逐字同**：

| 核心元素 | 分版元素 | 文本 |
|---|---|---|
| core[118] | ed[119] | `«meedoen» betekent: deelnemen,` |
| core[119] | ed[120] | `erbij zijn. In de Klimaatweek doet` |
| core[120] | ed[121] | `heel Nederland mee.` |

gloss 行（分版 ed[122–123] 拼接）：`meedoen = 参加する：気候週間にはオランダ中が参加する。`——与构建员称的 gloss **逐字一致**；荷兰语词头 `meedoen` 保留，仅释义本地化为日语。**定义句本地化 0 处。**

> 与构建员自述不符处（非阻塞，见文末 §12-1）：构建员称“元素 119–121 = 核心 118–120 逐字节同”。实测整元素字节并不相同：字体由 `Noto Serif CJK SC` 换为 `Noto Serif CJK JP`（日语版应有之换），y 各 −10.0（1138/1168.53/1199.06 vs 1148/1178.53/1209.06）。文本内容逐字同，实质要求通过；“逐字节”措辞不准确。

---

## 3. P8：compare CLEAN + 双口径 keydiff 逐项核实

### 3a. tools/p8.py compare（--total 150，独立重跑）

```
core    …/weekly-report-w45-nl-core/svg/p8-toets.svg: 150 noted
edition …/weekly-report-w45-nl-ja/svg/p8-toets.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[3, 7, 17, 29, 70, 71, 76, 96, 137, 138, 148]
```

150=150，无缺失无多余，**无需 EXTRA_ONLY  adjudication**。

### 3b. 口径一：p8.py keydiff 11 项逐项对照（印刷 P8 行已逐行核对）

| # | p8.py 提取 key（核心 → 分版） | 机制 | 印刷 key（— 之前） |
|---|---|---|---|
| 3 | `7` → `7 — ミュージアムナハトは11月7日` | dash→paren 翻转：日语注尾新增 `（土）`，使工具改走 paren 分支 | `7` = `7` ✓ 伪影 |
| 7 | `B — 气候周共 7 天` → `B — 気候週間は全7日間` | paren 分支，工具 key 含注文语言 | `B` = `B` ✓ 伪影 |
| 17 | `wortelen — wortelen = 生根` → `wortelen — wortelen = 根付く` | 同上 | `wortelen` = `wortelen` ✓ 伪影 |
| 29 | `B` → `B — ミュージアムナハトは11月7日` | **新出现项**：与 #3 同机制——核心注 `博物馆之夜在 11 月 7 日周六` 无括号（dash 分支），分版注尾 `（土）` 翻转为 paren 分支 | `B` = `B` ✓ 伪影，确为伪影 |
| 70 | `eiland — eiland = 岛` → `eiland — eiland = 島` | paren 分支，注文语言差 | `eiland` = `eiland` ✓ 伪影 |
| 71 | `proef — proef = 比赛项目、考验` → `proef — proef = 競技・試練` | 同上 | `proef` = `proef` ✓ 伪影 |
| 76 | `gaat winnen — gaat winnen = 会赢` → `gaat winnen — gaat winnen = 勝つだろう` | 同上 | `gaat winnen` = `gaat winnen` ✓ 伪影 |
| 96 | `advies — advies = 建议` → `advies — advies = 助言` | 同上 | `advies` = `advies` ✓ 伪影 |
| 137 | `气候周持续七天。` → `気候週間は7日間続く。` | **真重定向**：翻译题范文译文由中文改向日语（题型本身要求读者语译文） | —（重定向，合法） |
| 138 | `橙色预警意味着：做好准备。` → `オレンジ警報は「備えよ」という意味だ。` | **真重定向**：同上 | —（重定向，合法） |
| 148 | `B — zachte = 柔软的` → `B — zachte = 柔らかい` | paren 分支，注文语言差 | `B` = `B` ✓ 伪影 |

9 项伪影的印刷 key 与核心**逐字节同**；新出现的 3/29 两项确为括号分支伪影（均因日语注尾 `（土）` 触发 dash→paren 翻转），不在 NL 家族常见集合内是合理的——核心对应注无括号，分版注有 `（土）`。

### 3c. 口径二：全 150 key-token diff（段首 ` — ` 之前 token，150 无 dash 故取整段）

实测 diff **恰为 [137, 138, 150]**，与构建员称一致：

- 137：`气候周持续七天。` → `気候週間は7日間続く。`（翻译重定向）
- 138：`橙色预警意味着：做好准备。` → `オレンジ警報は「備えよ」という意味だ。`（翻译重定向）
- 150：`✓ 范文见本版 H 区（87 词）` → `✓ 模範文はこのページの H 欄（87語）`（范文指针装置，✓ 本体同，指针语本地化）

其余 147 项 token 逐字节同。两口径互相印证，无隐藏 key 变更。

### 3d. P8 注释括号形式（按 README #14，从构建代码核实，非仅看核心 SVG）

- 分版 P8 答案行（`^\d+\.` 行）统计：全角 `（` **16 处**、半角 `(` **0 处**——与构建员称一致。
- 页内其余括号不属于注释括号：全角另有 4 处（题头 `全解答と解説（1–8ページ）`、作文说明 2 处、页脚 `（全 8 ページ）`），合计全角 20 处；半角 13 处全部是冻结的荷兰语题目选项 `(A. … · B. …)`，与核心的 13 条选项行逐行同。核心第 14 处半角是 #79 `zij (复数)`，分版已转为全角 `zij（複数）`——即半角注释括号确为 0。
- 代码核实（README #14 要求）：P8 答案由 `content8.py` 末段 `txt = f"{n}. {key} — {note}"` 逐字打印，**无括号转换**；note 文本本身写在 W45 构建代码的 `f.ex(..., note)` 参数中，全部使用全角形式，如 `eiland = 島（het）`、`wortelen = 根付く（複数主語）`、`ミュージアムナハトは11月7日（土）`。W43 同配对版构建代码结构相同（note 全角；其 bslib4.py 与 W45 版除 VOL.1/VOL.2 页脚与引号写法外一致），形式一致。所谓“排版器自动转换”之说不成立亦无必要——形式直接来自代码。

---

## 4. 词语级中文残留重扫（阻塞门）

- `不定式` 全刊 **0 处**；已改为 `不定詞`，出现 2 处：P5 练习说明 `gaan + 不定詞で未来を表してください。` 与 P8 #77 `gaan kijken — wij → gaan + 不定詞 kijken`。构建员 fix 3 教训已落实。
- 词语级排查（约 90 个中文词形候选 + 第二批 24 个）：仅命中 6 个共有汉字词，逐条核对语境后**全部是标准日语词**，非中文残留：
  - `非常` 3 处：`非常に危険`（副词 非常に）；
  - `作文` 4 处：`優秀作文`、`作文問題`（日语 さくぶん）；
  - `注意` 9 处：`注意してください`、`に注意` 等（日语 ちゅうい）；
  - `参加` 8 处：`参加する`、`参加者`（日语 さんか）；
  - `禁止` 1 处：`警報コードは禁止ではなく助言だ`（日语 きんし）；
  - `助言` 3 处：`助言（het）` 等（日语 じょげん）；
  - 第二批另命中 `文章` 2 处：`警報の文章を読む`、`コードの横の文章を見よ`（日语 ぶんしょう）。
- 其余中文词形（学习/意思/语法/练习/答案/树木/灌木/节约/预警/本地/发放/种树/生根/柔软/土壤/比赛/考验/猜测/复数/主语/过去时/分词/将来/句子/动词/宾语/地点/对手/方式/祈使句/建议/忠告/成绩单/总结/焦点战/积分榜/进球/获胜/市场/展会/导览/时间段/二手/长期/今天/天气自然/禁止类等）**全部 0 处**。
- 仅做字符扫描不算通过——本项为词语级重扫，**通过**。

---

## 5. 日语排版：孤儿标点/小假名 + svglib

- 行首孤儿扫描（全部 8 页 SVG、全部 1549 个 text 元素）：NO_START 集 `。、，．！？：；）」』】ー…‥・` + 小假名集 + ASCII 闭合符集 `)]}.,!?%:;"'` 三重口径，**命中 0**。
- canonical 日语 svglib：构建树 `svglib.py` md5 = **`d73e23b365676c3618d7e060b835eb4d`**，与 README 记载的 canonical 值一致，且与 W43 同配对版构建树 `svglib.py` **逐字节相同（diff 0 行）**。
- 差异裁定：构建树与 canonical 的差异为零——即**未做任何改动**，更无 README #19 之外的改动。#19 的 NO_START 扩展是“允许的偏差”而非“必须的改动”；本期荷兰语正文在宽口径 ASCII 扫描下亦无行首孤儿，故无需扩展、亦未扩展，符合“差异仅为已记录的 NO_START 扩展”（此处为空集）。

---

## 6. 几何遮挡 + 页框压线 + 右缘扫描

### 6a. tools/occlusion_audit.py（独立重跑，含自检）

```
分版：0 flags（自检 planted 6 类全部触发，clean 对照静默）
核心：0 flags
分版 --core（NEW）：0 flags
```

分版 0、核心 0、NEW 0，三项全清。

### 6b. 同基线墨迹碰撞

occlusion TEXTX/COVER/LINEX/BOXTITLE/FOOTER/EDGE 全类 0 旗；独立逐行墨迹盒复算未发现同行文本相交。8 页全清。

### 6c. P6 图表标签覆盖（基线锚定墨迹法：PIL getbbox + getmetrics ascent，anchor start/end 对应 ls）

| 标签/数值 | 墨迹盒 | 与 4 条柱体重叠 |
|---|---|---|
| DE GRAFIEK · グラフ（練習データ） | (1473.0, 221.0)–(1877.5, 244.5) | 0.00% |
| Ik blijf thuis / 45 | (1473.0, 277.8)–(1595.8, 299.2) / (1840.0, 279.5)–(1863.0, 294.2) | 0.00% |
| Ik kijk eerst naar de tekst / 25 | (1473.0, 335.8)–(1724.8, 357.2) / … | 0.00% |
| Ik ga toch naar buiten / 20 | (1473.0, 393.8)–(1691.2, 415.0) / … | 0.00% |
| Ik weet het niet / 10 | (1473.0, 451.8)–(1626.5, 468.2) / … | 0.00% |

柱体（y=304/362/420/478，高 18）均在标签基线下方，**最大重叠 0.00% < 30%，通过**。

### 6d. 全部 8 页页框压线与右缘扫描（墨迹右界 vs 内外框线）

页框：外框 rect x=28（右界 1922）、内框 rect x=40（右界 1910）、内容右界 1885；页内无 x=1885 竖线。扫描结论：

- 墨迹右界 >1885 的分版文本共 5 条：其中 4 条为 0.05–0.09px 的 PIL 量化尾数（页脚/题头 end-anchor 落在 1885.05–1885.09），非压线；
- 唯一超 1885 逾 1px 者为 P2 匹配项 `c. voor je eigen omgeving, niet overal`，墨迹右界 **1901.50**——但**核心同条同墨迹右界 1901.50**（冻结荷兰语匹配项，逐字节继承），且仍在内框 1910 / 外框 1922 之内，卡片目视位于页框内、无截断（见 §12 观察 b，非阻塞）；
- 竖向/横向框线穿越：仅 P3 一处 0.43px（见 §12 观察 a，核心同值继承，亚像素，卡片不可见）；
- 其余：墨迹左界最小 63.2–64.8 均为 x=65 栏起点的 PIL 字形 bearing（−0.2px 级），远在内框 40 之内，非压框。

### 6e. 重点复测修复部位

- **Fix 1 · P2 末行**：渲染日志 `flow[P2-ex] ended col 3/3 y=2402 (bottom 2580)` 已复现（构建员称 2402 属实，系 flow 日志值）；渲染后末体基线 2519.2（第 14 题换行尾），仍在页脚规则线 2580 之上，遮挡 0。见 §12-4 对数值口径的说明。
- **Fix 1 · P7 右栏末行**：渲染日志 `P7 col3 ends 1906.0` 已复现；右栏（x=1473）末文本基线 1876.87（邀请句末行），金句分隔线 y=1937 上下最近文本分别为 1876.87 与金句题头 1975，**标线未越任何文本**，遮挡 0。
- **Fix 2 · P1 词注区**：词注现为 2 行（y=1846.30、1871.95），末行基线在 IN HET KORT 框顶 1874 之上 2.05px；遮挡 0；卡片目视（P1 右下）词注完整、框题 `IN HET KORT · 速報` 无覆盖（旧 3 行版曾覆盖 `だ。` 的缺陷已消除）。

---

## 7. gloss 计数 + 金句

### 7a. gloss（按渲染后 gloss 字符串拆 `·`，并与构建代码 gloss() 串交叉核对）

| 页 | 渲染后计数 | 核心计数 | 1:1 |
|---|---|---|---|
| P2 | 6（het klimaat 気候 · wortelen 根付く · besparen 節約する · de verwarming 暖房 · de waarschuwing 警報 · lokaal 地元の） | 6 | ✓ |
| P3 | 5（het museum 博物館 · de rondleiding ガイドツアー · het tijdslot 時間枠 · tweedehands 中古の · de beurs 見本市・市場） | 5 | ✓ |
| P4 | 5（de balans 成績のまとめ · gelijkspelen 引き分ける · de speelronde 節 · de topper 注目の一戦 · de stand 順位表） | 5 | ✓ |
| P5 | 5（het eiland 島 · de proef 競技・試練 · stemmen 投票する · de aflevering （1）話 · voorbij 終わった） | 5 | ✓ |
| P6 | 5（de meteoroloog 気象学者 · waarschuwingsmoeheid 警報疲れ · vastzetten 固定する · het advies 助言 · de voorstander 賛成者） | 5 | ✓ |

（注：校对脚本的 naive 拼接在换行处丢空格，如 `根付く· besparen`，属拼接 artifact，不影响计数与卡片实测间距。）

### 7b. P7 金句 8 句

8 句荷兰语句（去 «» 后）在**源文章页 + P7 各出现 1 次，共 2×**（空白归一化拼接后计数，分版与核心均为 2×）：

| 金句（荷兰语） | 源页 | P7 日译 + 页码标签 |
|---|---|---|
| Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland | p1 | 11月2日（月）から8日（日）まで、オランダは気候週間だ。 (Pagina 1) ✓ |
| De herfst is de beste tijd om te planten | p1 | 秋は植樹に最適の季節だ。 (Pagina 1) ✓ |
| Geel betekent: let op, het weer kan gevaarlijk zijn | p2 | 黄色は「注意、危険な天気になるおそれ」という意味だ。 (Pagina 2) ✓ |
| Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts | p3 | 70を超える美術館・博物館が夜19時から深夜2時まで開いている。 (Pagina 3) ✓ |
| Ajax won donderdag 22 oktober met 2–0 van Atalanta | p4 | アヤックスは10月22日（木）にアタランタに2–0で勝った。 (Pagina 4) ✓ |
| Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur | p5 | 11月1日（日）、『エクスペディティ・ロビンソン』がRTL 4で20時に始まった。 (Pagina 5) ✓ |
| Een code is geen verbod, maar een advies | p6 | 警報コードは禁止ではなく助言だ。 (Pagina 6) ✓ |
| Het weer is van ons allemaal, maar het raakt ons allemaal anders | p6 | 天気は私たちみんなのものだが、影響は人それぞれ違う。 (Pagina 6) ✓ |

页码标签与核心一致，且每句在其标注页上实测存在（源页正文含该句）。

---

## 8. 读者园地（P7 BRIEVEN VAN LEZERS，零编造）

页上四要素齐全：

1. **截稿时无真实来信**（荷兰语披露句原文保留）：`Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.`
2. **无最佳 P8 作文**：同上句 `beste pagina-8-teksten` 覆盖；日语披露句亦含 `8ページの優秀作文はなく`。
3. **示例 + VOL.3 承诺**：示例信 `«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)`，明确标注为编辑部示例（`voorbeeldbrief van de redactie`）；日语披露句：`締切時に本物の手紙と8ページの優秀作文はなく、編集部の例文を掲載。約束はVOL.3へ。`——与荷兰语披露句同义。
4. **显性日语邀请（祈使句 + 刊登承诺；内容预告行不算）**，逐字摘录并独立判定：
   > `あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！`
   
   判定：`送ってください` 为祈使句，`VOL.3に掲載します` 为明确刊登承诺，**邀请成立**。页底 `VOLGENDE WEEK` 预告行（`Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!`）未计入邀请，仅作旁证。示例信标注 + 披露句俱在，**零编造**。

---

## 9. 家具（以 W43 同配对版 SVG 实测为准，逐属性对照）

| 家具 | 分版实测 | W43 对照 | 结论 |
|---|---|---|---|
| 花线（P1 间隔大标题） | `オ ラ ン ダ 語 週 刊 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12`，墨迹宽 **1598.8px**（构建员称 1598.9，0.1px 为 PIL 量化差），居中边距左右各 110.6px，< 1820 内宽；主题词 KLIMAATWEEK / MUSEUMNACHT / SPEELRONDE 12 齐全 | W43 同式标题宽 1759.8px（VOL.1 主题词不同）；与 NL×EN 被迫删 MUSEUMNACHT 的 1958.8px 情形不同——本版**保留全长** | ✓ |
| 图表题（P6） | `DE GRAFIEK · グラフ（練習データ）`，墨迹宽 **404.5px**，右界 1877.5，距 1885 内界 7.5px，< 412 盒边（1473→1885） | 与 NL×EN 缩短形不同——本版**保留全长**，无溢出 | ✓ |
| SPORT 带（P4） | `SPORT · スポーツ`，x=78 y=116，36pt bold JP 字体 | W43 P4 同文、同坐标、同字号字体，逐属性同 | ✓ |
| 徽章（P1 y=372） | `オランダ語テキスト · 日本語の解説 — 日本語読者のための版`，19.5pt bold BRICK（#a4553a），x=975 middle | W43 徽章元素逐属性同（同文、同坐标、同字号、同颜色） | ✓ |
| 顶栏 | `ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む` + `WEEK VAN 2 TOT EN MET 8 NOVEMBER 2026` + `VOL. 2` | W43 同式（VOL.1 / W43 周次不同，结构同） | ✓ |
| 页脚 8/8 | 全部 `De Lucerna · オランダ語週刊 VOL.2 · 本文はオランダ語 · 解説は日本語` | W43 同式（VOL.1） | ✓ |
| 页码行 8/8 | `n ページ（全 8 ページ）`（n=1–8） | 同式 | ✓ |
| P8 题头 | `TOETS EN ANTWOORDEN · テストと解答` + `ANTWOORDEN · 全解答と解説（1–8ページ）` | W43 同文 | ✓ |
| P8 分隔符 8 个 | `— 1 ページ —` … `— 8 ページ —` | W43 同式 8 个 | ✓ |
| P4 署名行 | 分版单条 `Van de redactie van De Lucerna · Leesniveau: B1`（x=65 y=355.28），卡片目视完整 present | 核心为两元素（355.28 + 379.98 `B1`），拼接文本同；W43 亦为单行同式 | ✓（行数口径见 §12-2） |

---

## 10. 其他

- **图片**：全刊 `<image>` 共 4 张（P1–P4 各 1 张），与核心一致；署名行全部排版且与核心逐字同（冻结）：
  - P1 `Foto: Vovogov90 — CC0`
  - P2 `Foto: Nationaal Archief — CC0`
  - P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`
  - P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein`（两行排版，见 §12 观察 d）
  - 全部为公有领域/CC0 署名；署名来自核心冻结的 Commons API Artist 字段文本，分版未改动。
- **桥接**：全文 `桥接` 0 处；另查 `译注` 0、`讲解` 0、`练习与答案` 0、`参考答案` 0、`中文简析` 0、`本周` 0、`第 8 版` 0、西里尔字母 0、韩文 0、其他读者语家具残留（DE/EN/PT/FR 式）0 处；`解説 — 解説` 双前缀 0 处。
- **ABSTRACT.txt**：日语单行（149 字，1 个换行符为文件末尾换行），ASCII 双引号 0 个，含真实主题关键词（全国気候週間、ミュージアムナハト、クロッシング・ボーダー、エールディヴィジ第12節）+ 学习者搜索短语（`オランダ語 気候週間 ミュージアムナハト 単語 勉強法`）。
- **WEEKLY-KIT.md**：VOL.2、NL×JA 配对、2026-11-02–08 期次、8 页规格齐全。
- **题量核对**（独立计数）：P1–P7 题号芯片 10/14+匹配组/18/18/18/18/12，P8 34 芯片 + 匹配组；按匹配组展开（P2 `25–28`、P8 `141–144` 各 1 芯片计 4 题）后为 **10/18/18/18/18/18/12/38 = 150 题**，与核心一致；渲染日志级别分布 A2 47 / B1 72 / B2 31、范文 87 词，与任务书核心数据一致。
- **卡片目视**：8 张卡片（1950×2700）已全部逐页目视：P1–P8 无重叠、无截断、无压框（P1 词注/IN HET KORT、P2 末题与右缘匹配项、P3 tinted 框底、P4 署名与署名行、P5 不定詞说明、P6 图表、P7 词框/读者园地/金句分隔线、P8 答案区末行 150 均确认）。
- **修复轮**：只验收终态；fix1/fix2/fix3 日志的渲染统计（150 题、级别分布、范文 87 词）与终态 SVG 一致。

---

## 11. 与构建员自述不符处（全部非阻塞）

| # | 构建员自述 | 独立实测 | 裁定 |
|---|---|---|---|
| 1 | P7 词框“SVG 元素 119–121 = 核心 118–120 逐字节同” | 文本逐字同，但整元素字节不同：字体 SC→JP、y 各 −10.0 | 非阻塞：字体为日语版应有之换；实质（定义句逐字保留、仅 gloss 本地化）通过 |
| 2 | P4 署名行“日语面折 2 行、核心 1 行” | 实测相反：分版 1 行（单元素 y=355.28），核心 2 元素（355.28 + 379.98 `B1`）；W43 亦为单行 | 非阻塞：文本拼接逐字同，卡片目视署名完整 present；行数口径以实测为准 |
| 3 | P8 括号“全角 16 处、半角 0 处” | 仅在“答案注释括号”口径下成立；页内全角共 20 处（注释 16 + 题头/说明/页脚 4），半角 13 处全为冻结荷兰语选项括号 | 非阻塞：注释括号口径验证通过；此处明确口径以免误读 |
| 4 | Fix 1 “P2 落 2402” | 2402 为渲染日志 flow 终值（已复现）；渲染后末体基线为 2519.2 | 非阻塞：末体仍在页脚规则线 2580 之上，遮挡 0，安全条件通过 |

---

## 12. 非阻塞观察（注明不阻塞）

- **a. P3 tinted 框底 0.43px 触线**：`met zondag 8 november.` 墨迹底 941.03 vs 框底 940.6（框 x=1451 y=597.1 h=343.5，fill #fdfaf0）。核心同框、同文、同墨迹底 941.03——**逐字节继承**，亚像素，卡片上不可见，非分版引入。
- **b. P2 匹配项右缘 1901.50**：`c. voor je eigen omgeving, niet overal` 超内容右界 1885 共 16.5px，但核心同条同值 1901.50（冻结继承），且在内框 1910 / 外框 1922 之内，页内无 x=1885 竖线，卡片目视位于页框内、无截断。
- **c. 框线扫描 0.1–0.2px 量化尾数**：多处墨迹左界 64.8（栏 x=65 的 PIL bearing）与 end-anchor 文本右界 1885.05–1885.09，均为测量粒度，非压框；全部墨迹在 28/40 外内框与 1950 页边之内。
- **d. P4 署名换行**：`Foto: Spaarnestad Photo / Wikimedia Commons — publiek` + 次行 `domein`，拼接后全句 `… — publiek domein` 与核心一致；按原始字符串搜索全句会因换行而漏检，属排版换行非缺失。
- **e. svglib 未扩展**：构建树 svglib 与 canonical 逐字节同（md5 d73e…），未应用 NO_START 扩展；宽口径孤儿扫描亦为 0，故无需扩展。
- **f. gloss 拼接 artifact**：校对脚本 naive 拼接在换行处丢空格（如 `根付く· besparen`），属脚本拼接方式，不影响计数与卡片实测。
- **g. 题号芯片计数口径**：P2 独立芯片 14 个、P8 34 个，皆因匹配组（`25–28`、`141–144`）1 芯片计 4 题；展开后与 150 题一致。
- **h. P1 词注与框顶间距**：末行基线 1871.95 距 IN HET KORT 框顶 1874 仅 2.05px，视觉上贴近但无覆盖、无压线（遮挡 0，卡片确认）；属紧凑排版，非缺陷。

---

## 结论

**ZERO PROBLEMS（可定稿）。** 冻结 8/8 字节复现、新增 CJK 3087 逐页吻合且全为假名/标准日语汉字、纯荷兰语删串逐项合法、P7 定义句逐字保留、P8 CLEAN 且双口径 keydiff 逐项成立（含新出现 3/29 伪影）、词语级中文残留 0（不定式 0 处）、日语排版孤儿 0、遮挡 0/0/0、P6 图表标签重叠 0%、gloss 与金句 1:1/2×、读者园地零编造且邀请成立、家具与 W43 实测一致、图片与署名冻结、桥接 0、ABSTRACT 合规、8 张卡片逐页目视通过。§11–§12 所列均为措辞口径或继承性亚像素/量化事项，无一构成阻塞。

*证据文件（本科对目录）：`freeze-baseline.txt`、`freeze-diff.json`、`freeze-diff.txt`、`freeze-full.txt`、`p8-compare.txt`、`p8-detail.txt`、`occ-edition.txt`、`occ-core.txt`、`occ-new.txt`、`core-before.txt`、`core-after.txt`、`proof2.txt`、`proof5.txt`、`proof7.txt`。*
