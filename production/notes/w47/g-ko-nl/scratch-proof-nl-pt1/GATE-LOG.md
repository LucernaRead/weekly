# GATE-LOG — 2026-W47 · nl → pt · proof1 机械门实跑证据

复校员独立实跑，不信 KIT，只信自己跑的结果。全部命令用 `tools/venv/bin/python`；
TMPDIR 全程指向本 scratch 下 `tmp/`（系统 /tmp 512M 常满，未用）。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-pt1/`。
源码见 `occlusion.json`、`p8-extract.json`、`p8-compare.json`、`freeze-diff.json`、
`freeze-baseline/`、`creambox-all.log`、`boxtitle.log`、`measure.log`、`pdfspan.log`、
`pixelscan.log`、`pixelscan2.log`、`print.txt`、`web.txt`、`keycheck-150.json`、`render-p1.png`…`render-p8.png`。
自写脚本：`boxtitle_audit.py`（复用 nl-de1 版）、`measure.py`、`pdfspan.py`、`pixelscan.py`、`pixelscan2.py`。

## §0 身份核对（磁盘为准）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；scratch 写入探针文件成功。
- 印 PDF `De-Lucerna-VOL4-nl-pt.pdf`：SHA `d70937d8fb72c5a62969c4a09792a63fc9abc930d2b5f37854013a35e57e4cc5`，12,671,956 字节——**与任务一致**。
- 网 PDF `De-Lucerna-VOL4-nl-pt-web.pdf`：SHA `05faf02640908dd0e31c93cc0b4e105bdb3186945c0841fafc3ad9dc6187658e`，1,582,075 字节——**与任务一致**。
- text.md `2026-w47-nl-pt.text.md`：SHA `5b353380d17479bdde33f9c7b810cec3b9cb4aa9da19d0a2269daefac7de82d5`，46,025 字节——**与任务一致**。
- 任务数字与磁盘无出入，本节无 §0 差异。

## §1 几何遮挡审计（tools/occlusion_audit.py）

- 命令：`./tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --core <core-nl>/svg --json occlusion.json`
- 结果：**0 flags**（edition 与 core 均为 0，NEW vs core 0）；合成自检通过（6 类 planted flags 全触发，clean 对照静默）。RC=0。
- 局限（任务已提示）：该工具只核查带边框盒的 BOXTITLE 类；无边框奶油盒标题横向溢出不在其覆盖内——本版 D1 正属此类，由 §2–§4 的独立实测检出，不得以 occlusion 0 为放过理由。

## §2 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

- 命令：`./tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py <edition>/svg/*.svg` → `creambox-all.log`（310 行）。
- 结果：仅 2 处「last baseline」负值，均为盒下相邻标题的已知假阳性：
  - P1 IN DEZE EDITIE 盒（bottom 1652）：盒内末行 baseline 1636，clearance +16.0，desc-clear +9.7；+45 窗口内下一行「HET WOORD VAN DE WEEK」baseline 1676（+24.0）。
  - P2 四词盒组（bottom 1768）：盒内末行 baseline 1756.6，clearance +11.4，desc-clear +5.7；窗内下一行「Let op: schrijf je gedicht…」baseline 1800（+32.0）。
- **P7 toolbox 实测**：3 个盒，min inside clearance **+13.1**，min desc-clear **+7.1**（末行「de final.」baseline 1327.4，盒底 1340.5）。任务必查项 (d) 通过；像素复核（§4）三盒墨底余量 13.1/13.1/24.1 px。
- **desc-clear 负值 2 处**（0.30×字号降部余量估计为负，须像素裁决，见 §4）：
  - P2 EN JIJ 盒末行「em neerlandês e envia-as à redação.」baseline 1440.2，clearance +5.6，desc-clear **−0.4**——像素：墨底余量 **−0.9 px（在内）**，O1。
  - P5 EN JIJ 盒末行「em neerlandês e envia-as.」baseline 988.8，clearance +5.7，desc-clear **−0.3**——像素：墨底余量 **−5.6 px（在内）**。
- P3 SINTERKLAAS IN CIJFERS 盒末行「november.」baseline 1090.4，clearance +16.2，desc-clear +9.8；像素墨底余量 −16.0 px。任务必查项 (c) 未复现为缺陷。

## §3 框标题 / 版心右缘实测（PIL 真墨水 + 印 PDF span + 200 dpi 像素扫描，三法）

- 自写脚本 `boxtitle_audit.py`（PIL getbbox 真墨水，含 letter-spacing；Noto Sans CJK SC index 2、Newsreader Regular/SemiBold）+ 目标测量 `measure.py` + PyMuPDF span 检查 + 200 dpi 像素扫描（`pixelscan.py`/`pixelscan2.py`，仅裁切右缘/盒底条带渲染，避开大内存）。
- **D1**：P6「VOOR OF TEGEN?　A FAVOR OU CONTRA?」— PIL +21.5 px / PDF span +24.9 px / 像素 +23.4 px。核心同标题本轮 PIL 实测宽 326 px（21 pt），小于 400.5 px 内宽，合规。
- **D2（核心）**：P2 选项 c「c. eten voor het paard van Sinterklaas」— PIL +8.5 px / PDF span +13.1 px / 像素 +11.6 px。核心同文同位，核心亦然（归属核心）。
- **P1 标题在内**：P1「IN DEZE EDITIE　NESTA EDIÇÃO」— PIL −29.5 px / PDF span −27.9 px / 像素 −29.4 px。nl-de D1 在本版未复现。
- **P2 标题在内**：P2「ZO ONTHOUD JE HET　LEMBRA-TE」— PIL −14.5 px（盒右 961.0，左栏盒）。
- **P7 标题在内（像素翻案 span 指标）**：P7「HET WOORD　PALAVRA DA SEMANA」— PDF span 指标称 +1.5 px（1397.6 pt vs 盒右 1396.5 pt），200 dpi 像素真墨水 −0.6 px（1396.1 pt）。以像素为准判在内，O3。PIL 亦未 flag。
- 其余：全版无其他 BOX-RIGHT / PAGE-EDGE / NEAR-EDGE 标记。
- BOX-BOTTOM 标记（boxtitle.log 15 处）为已知假阳性：脚本 `bottom_ink = y + bb[3]` 中 PIL getbbox 默认锚点 "la"（ascender 顶），bb[3] 含整行高而非仅降部，导致每盒末行系统性“溢出”4–29 px；已由 §2 baseline clearance + §4 像素墨底逐盒翻案（除 O1 的 0.9 px 外，全部墨底余量 ≥5.6 px）。
- P1 HET WOORD gloss 次行与分隔线：线 y=1853；首行基线 1846.2、次行基线 1871.85——次行落在线下，线两侧各约 5 px，文字不触线、不跨线（O2，与 nl-de 同几何、同裁决）。

## §4 盒底像素复核（200 dpi 条带）

| 位置 | 盒底 | 最低墨点 | 余量 |
|---|---|---|---|
| P2 EN JIJ 末行 | 1445.8 px | 1444.9 px | **−0.9 px（在内）** |
| P5 EN JIJ 末行 | 994.5 px | 988.9 px | −5.6 px |
| P3 SINTERKLAAS 盒 | 1106.6 px | 1090.6 px | −16.0 px |
| P4 盒 | 1129.6 px | 1115.5 px | −14.1 px |
| P7 toolbox 盒 1 | 1011.5 px | 998.4 px | −13.1 px |
| P7 toolbox 盒 2 | 1340.5 px | 1327.4 px | −13.1 px |
| P7 toolbox 盒 3 | 1927.0 px | 1902.9 px | −24.1 px |
| P6 VOOROFTEGEN 盒 | 1052.0 px | 1041.9 px | −10.1 px |

- P1 IN DEZE EDITIE 盒底条带（1225–1245 pt）最低墨点 1245.2 pt 的 +8.2 px 为下一标题「HET WOORD VAN DE WEEK」（基线 1676）的字顶伸入条带所致，属 §2 已知的窗下标题假阳性，非盒内末行溢出（盒内末行基线 1636，余量 +16.0 px）。

## §5 p8 compare（显式 --core-p8/--edition-p8；--total 150）

- 命令：`p8.py compare --core-p8 <core-nl>/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`
- 结果：**CLEAN**，core 150 noted / edition 150 noted，missing=[]，extra=0，uncertain=[]，**keydiff=[137, 138]**。RC=0。
- keydiff 裁决：137、138 为 E 节翻译题（NL→PT），键合法重定向到读者语；键本身正确（137「As notícias do Sinterklaas passam todos os dias às 18:00.」；138「Os dois primeiros passam aos quartos de final.」）。139、140（PT→NL）键与核心一致。非缺陷。
- `p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150`：**noted set = 150 of 150**。RC=0。
- 另：text.md 键与印刷版 P8 键逐题程序比对 **149/150 逐字一致**（`keycheck-150.json`）；唯一形式差异 #150 为开放写作题——印刷版键「✓」vs text.md「(tarefa aberta, texto modelo abaixo)」，语义相同。范文 81 词（脚本计数，80–100 内）。

## §6 freeze / freeze_direct 8/8

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-baseline`：**8/8 SVG byte-identical**，核心 8 文件重哈希确认未被改动（"core integrity: shipped core SVGs unchanged (8 files re-hashed)"）。RC=0。
- `freeze.py diff --core-svg <core-nl>/svg --edition-svg <edition>/svg`：p1 +27/−48 … p8 +183/−675；**新增 CJK 仅 7 个 U+3000**（p1 为 0，其余每页 1 个）。U+3000 是 SOP §1.1 规定的全角空格分隔符（「不用·做分隔，用全角空格」），非中文文本。RC=0。
- 移除串核查：全部含拉丁字母的移除串，其词元均在同页新增串中重现；惟二例外已裁定：（a）刊头「LUCERNA DUTCH WEEKLY」→ 葡语刊头副标（fan-out 设计）；（b）「perfectum」→ 葡语「perfeito」（P8 答案注 40/42「ontvangen no perfeito」「lezen no perfeito」），讲解层合法翻译，非核心丢失。

## §7 keycheck 150/150（逐题手验）

- `keycheck-150.json`：150 题逐题手验，**150/150 ok，0 不符**。方法：text.md 全文通读 + 印 PDF 8 页目视；配对题字母对照印刷版 a–d 列表（P2 D：a 列表/b 诗/c 食物/d 门口；P8 F：a 诗/b 新闻节目/c 小组头名/d 门口）；算术重算；范文计词。
- 外部核实：Nations League A2 积分榜、PSV 26 分、Heerenveen 5–3、Grave/阿姆斯特丹入城、欧战下期预告、Feyenoord–Ajax 29 Nov（见 §11）；其余键均由文内事实直接支撑。

## §8 印/网文字层比对

- `pdftotext -layout` 印版 104,548 B / 网版 104,624 B；词多重集（`\S+`）**8000 vs 8000，diff 0**；折叠空白后同长 44,319 字符，首处差异仅为刊头行提取词序（"De Lucerna WEEKBLAD…" vs "WEEKBLAD… De Lucerna"），属 pdftotext 版式提取顺序 artifact，非内容差异。
- **D5**：网 PDF 斜体丢失（见 §9）；其余两项（空格丢失、闭引号脱离）未复现。

## §9 斜体 + P8 最小字号实测

- PyMuPDF 全书 span 扫描：印版 italic span **1 处**（P1「«de groepswinst»」，Newsreader Italic 16.12 pt）；网版 italic span **0 处**，同词改用 LucernaNewsreader-Regular（宽 131.1 pt vs 印版 122.2 pt）。→ D5（轻微）。
- P8 最小字号实测（PyMuPDF 逐 span）：**10.12 pt**（387 个 span）；全书最小亦为 10.12 pt（P8）。SOP §1.1 让步阶梯允许降至 9.75 pt，10.12 合规，非缺陷。

## §10 弯引号 + E 节 type 标签本地化 + text.md 残留中文 + ABSTRACT.txt

- SVG 全版：U+201C=0、U+201D=0、U+2019=0、U+201E=0；« U+00AB / » U+00BB 成对（P1 2/2、P2 2/2、P7 30/30、P8 2/2），合法荷兰语引号。text.md：10 处直引号全为 `'s`（'s avonds 等荷兰语属格），与核心一致。无误用。
- **text.md 答案标记未本地化**：CJK 字符共 300 个，全为「答/案」——「— 答案：」142 处 + 配对题「(答案 x · …)」8 处 = 150 处。→ D3（重大）。
- **E 节 type 标签未本地化**：text.md 内联 `[级别 · 类型]` 全部英文（complete 65、choice 44、cloze choice 13、make sentences 8、true or false 7、translate 4、matching 2、writing 1；144 实例覆盖 150 题）；尾标 `[Complete]` ×59 英文，其余尾标均已葡语化（Forme a frase ×8、Verdadeiro ou falso? ×7、Traduzir para português ×2、Traduzir para neerlandês ×2、Escreva ×1）。印刷版 SVG：`Complete` ×59（P2 9、P3 13、P4 9、P5 10、P6 9、P7 9），其余印刷标签均为葡语（Forme a frase ×8、Verdadeiro ou falso? ×7、P8 E 节 Traduzir para…）。→ D4（重大）。
- 横向对照（D4 定性依据）：nl 全家其余 8 版类型标签全部已本地化（nl-es/nl-fr/nl-it/nl-ko/nl-ja/nl-ru/nl-zh-tw）；it-pt 亦为葡语本地化（Completa a frase / Escolha múltipla / Forma frases / Relaciona as palavras）；仅 nl-pt（与 nl-en——英文即读者语）保留英文。
- ABSTRACT.txt：葡语单行 320 字节，含「Lucerna」「VOL.4」、目标语名、A2–B2、150 题；「Semanário neerlandês Lucerna VOL.4」写法与 nl 全家 8 版一致（nl-de「Lucerna Niederländische Wochenzeitung VOL.4」、nl-es「Semanario neerlandés de Lucerna VOL.4」、nl-fr「Journal néerlandais Lucerna VOL.4」等）。pt-zh-tw D4（摘要全文无「A Lucerna」亦无「VOL.4」）未复现——「A Lucerna」是葡语目标语版刊头（core-pt），本版目标语为荷兰语、刊头「De Lucerna」，摘要取全家通行的裸「Lucerna VOL.4」写法。任务必查项 (g) 未复现，非缺陷。

## §11 外部事实来源（2026-11-11 检索）

- **Nations League A2 积分榜**（题 2、3、6、9、48、53、54、114、115 的事实基础）：myfootballfacts / NBC Sports（UEFA 官方数据）：NED 4 战 2-2-0、7–5、8 分；GRE 8 分（5–3）；GER 5 分；SRB 0 分。——与正文「8/8/5/0」「7 tegen 5」及各场比分全部吻合。
- **PSV 26 分**（题 63、126）：PitchLab Eredivisie 2026/27（2026-11-08 更新）：「PSV Eindhoven top the Eredivisie 2026/27 table as of 8 November, with 26 points from 12 games」；VAVEL：「PSV lead the table with 26 points after 12 matches」；Cambuur–PSV 2–5（8 Nov）多源一致；NEC–PSV 21 Nov 15:30 UTC = 16:30 CET（P4「16:30 uur」吻合）。
- **Heerenveen–Feyenoord 5–3**（题 59、64）：Sportradar / Sky Sports：8 Nov 2026，Abe Lenstra Stadion，5–3。
- **Grave 入城**（P1/P3）：vandaagingrave.nl：Landelijke intocht 2026 in Grave，14 november 2026 周六，Maaskade，市长 Marieke Moorman，NPO Zapp (NPO 3) 直播，Merel Westrik 主持，节目 12:00–16:00；mamaliefde.nl：同上 + 约 12:00 靠岸 Maaskade。——全部属实。
- **阿姆斯特丹入城 88 届**（P3；闭合 nl-de O1）：uitamsterdam.com / amsterdam.org：2026-11-15 周日，10:15 De Omval 出发，11:30 Scheepvaartmuseum，13:00 Stopera 骑行出发，经 Rembrandtplein（13:15）/Utrechtsestraat（13:20）至 Leidseplein；88e editie（amsterdaminside + 市政府清单）。——全部属实。
- **下期预告欧战**（P7 VOLGENDE WEEK）：UEFA.com 2026/27 Champions League 赛程：Matchday 5，Tuesday 24 November 2026，Feyenoord vs Porto、Real Madrid vs PSV Eindhoven。——属实。
- **Feyenoord–Ajax 29 Nov**（P7 VOLGENDE WEEK）：FR12.nl / Sportradar：周日 29 November 2026，14:30，De Kuip，Eredivisie 第 14 轮。——属实。
- **日期/星期**：`date -d` 核验（Europe/Amsterdam）：2026-11-14 周六、11-15 周日、11-16 周一、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六——与文中全部星期表述吻合。

## §12 其他核查

- 全文通读：text.md 全文 430 行 + 印 PDF 8 页逐页目视（自渲染 150 dpi，`render-p1.png`…`render-p8.png`）。无溢出/重叠/压页脚/图片问题（除 D1/D2 外）；7 张照片均带目标语图说 + CC0/公有领域出处（Wim van Rossem/Anefo、Anefo、W. Punt/Anefo、Spaarnestad Photo/Wikimedia Commons、Elise lovenko/Unsplash、Cristina Gottardi/Unsplash、Aaron Burden/Unsplash）；P6 为数据图（无照片）。
- P7 金句 8 条逐字出自本期正文，页码标注正确（P1×2、P2、P3、P4、P5、P6×2）；P1「IN DEZE EDITIE」页码 Pag. 2–8 与实际页码一致。
- P8：答案 1–150 齐全，末行基线 2553.7，距页脚线 y=2596 有 42.3 px 余量；范文 81 词（80–100 内）。
- **未改动源文件**：无任何源文件改动/重建/commit/push。

## 附：工具与方法备注

- `freeze.py` 无 `freeze_direct` 子命令（与任务注记一致）——记为方法备注，不当缺陷。
- `boxtitle_audit.py` 的 BOX-BOTTOM 标记为锚点换算错误所致的假阳性（PIL getbbox 默认锚点 "la"，bb[3] 含整行高），已由 §2 baseline clearance + §4 像素墨底逐盒翻案；BOX-RIGHT 标记经三法复核属实者已列为 D1。
- `pixelscan.py` 首次运行在 P3 盒底条带处因条带未含末行墨水（lowest_ink=None）而中断，P3/P7 盒底改由 `pixelscan2.py`（条带自末行基线上方起）完成，见 `pixelscan2.log`。
