# PROOF-NOTE — 2026-W47 pt-nl（葡萄牙语目标 · 荷兰语读者）re-proof 独立复校

- 复校员：独立复校（re-proof，与重建者/修复者不同人；SOP §8.4）
- 复校日期：2026-11-11
- 版目录：`production/2026-w47/2026-w47-pt-nl/`
- 复校对象：proof1（7849e6e9，结论 (b)，D1–D6）之后约 14:26–14:35 的重建版
- 结论：**(a) 无缺陷，可以定稿** — D1–D6 六项经 PIL 真墨 + PDF 像素双法独立量测，全部修净；全部机械门独立重跑通过；150 题逐题手验通过；P1 顶栏标语独立判定正确、未颠倒；31 个框标题逐一实测全部 clear；未发现新缺陷。

## §0 身份核对（以磁盘为准）

| 文件 | 磁盘 SHA-256 | 任务所给 SHA | 字节数 | 一致 |
|---|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `7404001d519ac57d932fb99a7f73d59c0036a5de8d4ef35c276a8a9bca335029` | 相同 | 12,935,296 | ✓ |
| `A-Lucerna-VOL4-web.pdf`（网） | `f8119356b8032f6720de25567367a53911958fe51c194d2e1d366130bcca9be3` | 相同 | 1,142,955 | ✓ |
| `2026-w47-pt-nl.text.md` | `6f8d4d5960326b69f7ad639dbedc3a15ec8972780e292b2e2c3625001b5532cd` | 相同 | 37,559 | ✓ |

三项 SHA 与任务消息完全一致。text.md `wc -l` 534 行系末行无换行，实为 535 行内容，与任务所记 535 行一致。本组 SHA 与 re-fanout 报告 §1 的旧值（印 5a58050b…/12,935,390 B，即 proof1 所对的版）不同——本次复核的是新版，未混淆。开工探针：`git hash-object -w --stdin` 在 `~/workspace/weekly-git` 内成功；scratch 真实写文件成功。复校全程未改动任何生产文件（43 个文件复校前后 sha256 逐一比对相同，见 GATE-LOG §11）。

## D1–D6 逐项复核（PIL 真墨 + PDF 像素双法；源码行 + 实测值）

| 项 | 修复方式（盘上实测） | PIL 真墨（版内 svglib 同款字体） | PDF 200dpi 像素法 | 结论 |
|---|---|---|---|---|
| D1（核心）P1 KORTOM 末行 `em Brasília. (Página 4)` | 框加高：框底 2310.0 → **2348.0**（+38px）；Quiz 分隔线由 y=2312 下移至 **y=2350.0** | 基线 2327.6，墨迹 2311.6..2332.6，框底 2348.0 → **框内，clear +15.4px**；线在墨底之下 17.4px，不横贯 | 墨底 2331.8，clear **+16.2px**；裁图 `crop-reproof-d1.png`：末行印在奶油底上，无绿线横贯 | **修净** |
| D2（核心）P3 日程末行 `16h30.` | 框加高：框底 525.0 → **551.0**（+26px） | 基线 540.6，墨迹 523.6..540.6 → **框内，clear +10.4px** | 墨底 540.5，clear **+10.5px**；裁图 `crop-reproof-d2.png` | **修净** |
| D3（核心）P6 时间线末行 `Página do Participante.` | 框加高：框底 840.0 → **854.0**（+14px） | 基线 840.8，墨迹 825.8..845.8 → **框内，clear +8.2px** | 墨底 845.8，clear **+8.2px**（与 PIL 逐值相同）；裁图 `crop-reproof-d3.png` | **修净** |
| D4（边缘）P7 `A PALAVRA` 末行 | 改写 E2：`…de herinnering aan de strijd en de cultuur` → `…de memorie aan verzet en cultuur`；末行 `memorie aan verzet en cultuur.` **无降部字母**（g/j/p/q/y 0 个） | 基线 1427.0，墨迹 1410.0..1427.0，框底 1431.5 → **框内，clear +4.5px**（墨底恰为基线） | 墨底 1426.6，clear **+4.9px**；裁图 `crop-reproof-d4.png`：末行在奶油底上 | **修净** |
| D5（本版）P2 `PARA NÃO ERRAR` 框标题 | gloss `Het ezelsbruggetje` → `Ezelsbruggetje`；SVG 源码行：`<text x="556.5" y="642.02" font-family="Noto Sans CJK SC" font-size="23" font-weight="700" …>PARA NÃO ERRAR　Ezelsbruggetje</text>` | 墨迹右缘 941.5，框右 961.0 → **clear +19.5px**（与 KIT 所称 +19.5 逐值相同） | 墨迹右缘 942.7，clear **+18.3px** | **修净** |
| D6（本版）P7 `ERROS COMUNS` 框标题 | gloss `Veelgemaakte fouten` → `Fouten`；SVG 源码行：`<text x="1461.5" y="242" font-family="Noto Sans CJK SC" font-size="23" font-weight="700" …>ERROS COMUNS　Fouten</text>` | 墨迹右缘 1747.5，框右 1862.0 → **clear +114.5px** | 墨迹右缘 1746.7，clear **+115.3px** | **修净** |

补充说明：
- D1–D3 的修复几何与 core-pt 逐值相同（creambox 对照：KORTOM 框底 2348.0/末基线 2327.6/clear +20.4；P3 日程框底 551.0/540.6/+10.4；P6 时间线框底 854.0/840.8/+13.2），属核心层修复，非仅本版改动。
- D6 的 KIT 所称 clear +115.0 介于本次两法之间（PIL +114.5，像素 +115.3），差 0.5px 属量测口径（advance 宽 vs 真墨右缘），不影响“修净”结论。
- D4 的 PDF span 框（PyMuPDF）底为 SVG 换算 1432.8，看似越框底 1431.5 达 1.3px——span 框含字体下行空高，非真墨；PIL 真墨底 1427.0 与像素法 1426.6 一致在内，不记缺陷。
- 全部 31 个框标题逐一 PIL 真墨量测：横向扫描 0 处溢出（见 GATE-LOG §8 完整表）；最紧者为 P1 数字框标题 clear +9.5px 与 P1 KORTOM 标题 +8.5px，均在框内；纵向全框扫描（creambox + PIL）0 真溢出。

## P1 顶栏标语独立判定（未颠倒，无缺陷）

- 盘上渲染：`TODA SEMANA EM PORTUGUÊS　Elke week　Het Portugees dat Brazilië leest`；与 `tables_nl.py:201` 的值 `Het Portugees dat Brazilië leest` 逐字相同。
- 中文原意：「读巴西人正在读的葡萄牙语」——巴西人读葡语（巴西人=主语/读者，葡语=宾语/被读物）。
- 荷兰语语法判定：从句为动词尾置结构 `dat Brazilië leest`——`Brazilië` 位于动词 `leest` 之前的主语位，关系代词 `dat`（= Het Portugees）为宾语；即“巴西所读的葡语”。语义选择亦强制此读法（语言不能读人）。与德语版同构（`Das Portugiesisch, das Brasilien liest`，正确）一致。
- 对照：it 版 `Il portoghese che legge il Brasile`、es 版 `El portugués que lee Brasil`、fr 版 `Le portugais que lit le Brésil`——动词紧跟关系代词、国家为宾语，确为颠倒（“读巴西的葡语”）；荷兰语的动词尾置结构与之不同，不可同理推断颠倒。**结论：nl 标语正确，无需改译。**

## KIT 所称 1 个 P1 LINEX flag 的核查（未复现）

- 本次独立重跑 occlusion 真实审计（非 --selftest）：**本版 0 flags、core-pt 0 flags、带 --core 比对 NEW 0**（自检 planted 6 类全部触发，工具正常）。
- 该 flag 所称几何（墨顶 2312.8 vs 线框 [2311, 2313]）在现版已不存在：Quiz 分隔线现为 y=2350.0，D1 末行墨迹为 2311.6..2332.6——线在墨底之下 17.4px，无擦过。flag 随 D1 的框加高+线下移而消失，KIT 的“1 flag”记录与现版盘上状态不符，不采信亦无残留问题。

## 未决事项（沿用 proof1，不记缺陷）

- **O1**（排版风格，跨版）：P7 A2 荷兰语释义仍用直引号 `'vallen op een dag'`（U+0027），正文引语用 `« »`、P8 E139/E140 用弯引号。pt-en 版同一位置同样用直引号，属跨版共用写法，**不记为本版缺陷**；是否统一改弯引号请协调员在全周层面定。
- **O2**（事实，未独立核实）：P4 进球者名 `Renan Lodi`（Atlético）与 `Carlos Vinícius`（Grêmio 扳平）——比分/场地/日期/总比分/决赛已用公开来源独立核实无误（同 proof1 来源），进球者名未在检索片段中出现，无矛盾发现。
- **O3**（事实，未独立核实）：Brasileirão 第 35/36 轮对阵与开球时间、国家队友谊赛时间为未来赛程预告（结果见 VOL.5），本次未逐项检索核实，无矛盾发现。注：Q125 称 Palmeiras × Flamengo（21 日周六）属“rodada 36”——与正文“rodada 35 于 18–19 日收尾”一致（第 36 轮为周末轮），非矛盾。
- **O4**（观察，非缺陷）：P2、P3、P5、P6 中部留白属核心版式流，与 core 一致，不记缺陷。

## 核实摘要（全文通读 + 逐题手验）

- **印 PDF 8 页 + text.md 全文（535 行）已通读**：目标语拼写/变位/标点、荷兰语讲解层、数字、日期星期、跨版引用均已核对；除 D1–D6（已修净）外无内容错误。
- **150 题逐题手验 150/150 通过**（`keycheck-150.json`，每题含印刷键、text.md 键、核实依据）：印刷键与 text.md 答案零出入；答案本身已逐题对照题干与原文复核。**Q73 专门手验**：题干分属同一句 `Depois da prova, começa a espera pelo gabarito.`——Q70 填 `gabarito`（`pelo ___`）、Q73 填 `espera`（`começa a ___`），配对各有唯一正确词（词框：gabarito · oficial · extraoficial · espera · nota · pesar），非三源同错。易错点另验：Q56–59 比较级（3>1、5>4、16h30<17h、2 天<1 周）、Q80–82 正误、Q83–92 图表算术（16–30 日=15 天；工作日 10 天 16、17、18、19、23、24、25、26、27、30；休息 5 天 20、21、22、28、29；10+5=15；第 10 个工作日=11 月 30 日）、Q97–100、Q113–132 阅读理解、Q137–140 双向翻译（137 `Vrijdag 20 november is een nationale feestdag.`、138 `Palmeiras won met 5–4 na strafschoppen.` 逐字验为正确荷兰语）、Q141–144 配对、Q145–149 对话补全。模型文实数 88 词（80–100 合格；本次独立计数：含量词 `Texto modelo:` 共 90 词，减去标签 2 词 = 88）。
- **数字/日期**：`date -d` 核实 2026-11-07 六、08 日、14 六、15 日、16 一、17 二、20 五、21 六、22 日、23 一、27 五、12-06 日，与文中星期全符。
- **机械门**：run.py（副本）rc=0、TOTAL 150、8 页 SVG 与生产版逐字节相同；gates.py 16/16；occlusion 真实审计 0 flags（本版/core/带 core 比对三跑）；freeze 核心标准比对 8/8（--build core-pt、--core-svg core-pt/svg，build-copy 文件清单与 core-pt 一致）+ 版内自比对 8/8；freeze diff 新增 CJK 仅 U+3000 ×9；p8 extract 150/150、compare CLEAN（keydiff [137, 138]，两句荷兰语译文已逐字验为正确）；印/网文字层逐字节相同（pdftotext 各 111,218 字节）；web PDF 在本 scratch 内重渲染 1,142,958 字节，文字层与生产网 PDF 逐字节相同（字节差 +3 为已知的 fontTools wall-clock，不可复现）；P8 最小字号 9.75pt（= SOP §1.1 下限，印/网一致）；斜体 1=1（P1 « consciência »）；check_s11（pt 改编）ALL PASS；creambox 全版 31 框 0 真溢出；E 节无 type 标签；text.md CJK 0 字符；SVG 可见文本 CJK 0 字符（仅 U+3000 分隔符与蛾标 `<title>` 内 3 字，非读者可见文本）。

## 跨轮核对小记（非缺陷，仅供协调员参考）

- proof1 GATE-LOG §8 表格中 P3 E VOCÊ 一行所记“框底 854.0”与其实测 creambox（末基线 874.9、clear +5.1 → 框底 880.0）自相矛盾；本次实测框底 880.0、墨底 879.9、clear −0.1px，结论（在框内）不变，属誊抄口径差。
- proof1 词数 8,589 vs 本次 pdftotext -layout 8,584（印/网一致、多重集差 0）为计数方法差，不影响结论。
