# PROOF-NOTE — 2026-W47 en-fr 独立复校 proof1（重建版，2026-11-11）

- 版：`production/2026-w47/2026-w47-en-fr/`（en re-fanout #2 重建版，git 未跟踪）。
- 对象（盘上实测 SHA，与任务书/KIT §7 逐字节一致）：
  - 印 `The-Lucerna-VOL4-en-fr.pdf`：29,330,979 B，SHA-256 `76b4522c53a2fcad0a92f9b02180ff353dc73845ce57080cb7c1d2b0d263dd2f`
  - 网 `The-Lucerna-VOL4-en-fr.web.pdf`：2,413,670 B，SHA-256 `dd68f929b86af917626769bb52cad6ba34a0b6fe4e959a43279de4e319f83266`
  - `2026-w47-en-fr.text.md`：53,809 B，SHA-256 `2d832a170a229817af36c1c5378db7ef2030abd54bec54ab5cf019a6f0364855`
  - 两 PDF 各 8 页（印 1462.5×2025 pt；网同）。
- 复校员：独立 proof1，与建版者不是同一人。只复校，未改任何生产文件、未重建（除 scratch 副本内 `run.py` 复跑）、未 commit、未 push、未动 tools/。开工与收工两次 SHA 复核一致。中间件全在 `scratch-proof-en-fr1/`（`TMPDIR=<scratch>/tmp`，解释器一律 `tools/venv/bin/python`，未写 /tmp，未删他人文件；上一轮旧版 proof 文件整体移入 `r1-old-build/` 存档，未删）。
- 探针：`git hash-object -w --stdin` 成功（`c4b82938…`）；scratch 写文件成功（`probe.txt`）；`/dev/null` 正常（开工检查存在，未需垫回）。
- 核心 en 复核：`core-en` 印 PDF `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`（41,407,278 B）、`text.md` `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`（51,405 B），与 core-en KIT §7 记录的 fix1 后定稿值逐字节一致；网 PDF `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`（2,804,271 B，与 fix1 前 `2ee5391f…` 不同）；核心 registry `05d412f9…`，Q39=a、Q40=d。本轮未碰核心。

## 结论：(a) 定稿

**本轮全量复校零缺陷。** 上一轮 proof1 的 D1–D5（D1 Q39/Q40 键互换、D2 P1 SEARCHES 漫出、D3 P2 DID YOU KNOW 漫出、D4 “confirmé” 措辞、D5 P7 “encore”）已全部在核心 fix1 + 本版重建中修复，并经本轮逐项实测证实；重建引入的其余变化全部落在修复集内，无意外变化。缺陷清单：空。

## 必验项逐项结果

### fr fix1 — D5 “encore” 已删 ✓
- 三源一致：`content7.py:99` P7 工具盒 B2 行为 `“Nobody knows whether the count will change.” Personne ne sait si le décompte va changer.`；`text.md:865` 同文；`svg/p7-lang.svg` 同文（`le décompte va changer.`）；印/网两 PDF 文字层同文。
- 全版扫描 `encore changer`：content / SVG / text.md / registry **0 命中**。
- 残留的 `encore` 共 2 处，均合法：Q138 答案注 `continues = continue encore`（`continues` 的正确译法）；P7 读者来信法语注 `aucune vraie lettre n'est encore arrivée`（“尚未收到”，正确法语）。无断行后遗症：B2 行在工具盒内，盒底留白充足（creambox P7 工具盒间隙 +48.5 px）；200 dpi 目视无异常。

### Q39→a / Q40→d — Ashes 回顾口径逐题手验 ✓
- 四方一致（题干、选项、键、注记）：
  - P3 渲染选项（SVG 实测）：a. a person who teaches and guides you · b. a person chosen to take part in the Games · c. a person who lives with you in the jungle camp · d. the place where the Games are fought；词条 38. a tribute / 39. a mentor / 40. the arena / 41. a campmate。
  - 正确键：38→b、**39→a、40→d**、41→c。
  - registry（核心与本版一致）：39 `key='a'`（`mentor = un mentor a`）、40 `key='d'`（`arena = l'arène d`）。
  - `p8.py extract` 键：38=b、39=a、40=d、41=c；印版 P8 答案行实测 `39. a · 40. d · 41. c`（`39. d` / `40. a` 在印版文字层 0 命中）。
  - `text.md` 附录：`39. [A2] Appariement — a (mentor = un mentor a)`、`40. [A2] Appariement — d (arena = l'arène d)`。
- Ashes 回顾相关题四方一致（题干/选项/键/注记）：
  - Q46 A（首 Test：2025 年 11 月 21 日周五，珀斯；B 为 2026 年 11 月 21 日周六、珀斯，C 为 11 月 19 日周四、休斯顿——三项互斥唯一）、Q47 C（Cummins 背伤；A 膝伤、B 腿筋为干扰项）、Q48 B（Smith 顶替领队）、Q49 A（英格兰上次在澳赢系列 2010–11）、Q50 C（曼城–富勒姆 12:30；A 10:20 为旧 Ashes 首球时间、B 16:30 为利物浦–曼联时间）、Q51 B（Sinner 膝伤）、Q52 hosted、Q53 lasts、Q54 eight、Q55 won、Q56–59 b/c/d/a、Q60–63 lost/lost/ended/beat、Q125 A（澳大利亚 4–1）。
  - 外部事实复核（2026-11-11 网上检索，cricbuzz / cricket.com.au / Sky Sports / TNT Sports 等）：首 Test 珀斯 2 天、8 wicket、847 球——Ashes 史上第三少，自 1888 年以来最少（仅 1888 年 Old Trafford 788 球、Lord's 792 球更少），正文“shortest … since 1888”准确；系列 2025-11-21 至 2026-01-08；澳大利亚先赢三场（珀斯、布里斯班、阿德莱德）后保住 Ashes；英格兰第四场墨尔本 4 wicket、2 天取胜、为 2011 年悉尼以来首场在澳 Test 胜利（“almost fifteen years”准确）；第五场悉尼 5 wicket；总比分 4–1。Cummins 背伤、Hazlewood 腿筋缺席、Smith 队长、Boland、Doggett 首秀与 r1 核实一致；印度 2024 年 11 月在珀斯赢 295 分与 r1 核实一致。
- 其余 Ashes 措辞：正文、P1 IN BRIEF（“A year ago: Australia beat England 4–1 in the 2025–26 Ashes.”）、P2（“page 4 looks back at the Ashes”）、P5 THE JUNGLE, TOO（“the football is back on Saturday”）、P7 Try-it（“the next series is in England, in June 2027. About last year: ‘Australia won the first Test.’”）、NEXT WEEK（“England's rematch waits until June 2027”）全部为回顾口径一致；`Perth is winning!` / `second week in Perth` / `Ashes begin` 全版 0 命中。

## 全量门禁（逐门重跑，详见 GATE-LOG）

| 门 | 结果 |
|---|---|
| run.py（scratch 副本复跑） | RC=0，0 OVERFLOW / TOO WIDE，TOTAL 150，MODEL 82 |
| occlusion 审计 | **0 flags**，自检 OK（6 类阳性对照全触发，干净对照静默） |
| p8 extract | **150/150**，noted set 60/150（与核心 noted 集相同） |
| p8 compare | **CLEAN**，missing=[] extra_count=0 uncertain=[]；keydiff=[137, 138, 139, 140, 150]（读者语法人键，预期内） |
| p8 extract vs registry | 150/150；仅 Q150 短标差异（与核心同 pattern） |
| freeze baseline | **8/8 SVGs byte-identical**，core integrity 8 文件未变 |
| freeze diff vs core | 新增 CJK 共 9 个，全为 U+3000；新增串均为法语讲解/家具，删去串均为中文讲解层/W46 惯例词表行/重排 P8 键行/家具；英文正文未动 |
| 印/网文字层 | pdftotext 印=网（-layout 108,899 B；无 layout 49,439 B），token 多重集差 0/0，逐页 byte-identical 8/8；网 < 7 MB |
| P8 最小字号 | PDF 有效最小 **10.12 pt**（P8 答案键块，0.75 缩放组内；其余页最小 11.62 pt）；SVG 属性最小 13.5 pt；均 ≥ §1.1 下限 9.75 pt |
| keycheck | 机械 150/150 + 人工逐题 150/150（见下） |
| creambox（原版 +45 px 窗口） | P1 SEARCHES 末基线 **+12.0**（旧 -18.0，已修）；P2 DID YOU KNOW 末基线 **+14.3**（旧 -12.7，已修）；其余 23 行负值全部逐行裁定为下块标题/盒后流文（-35.5…-37.0，约 36 px 正常块间距），与核心同 pattern |
| creambox_check（精炼版 0–8 px 带） | **NO OVERFLOW，RC=0**（本版与核心同）；P7 工具盒间隙 +48.5 px；P2 AND YOU? 盒 +5.0（盒内，紧但未出）；P8 MODEL 盒 +92.4 |
| boxtitle | occlusion BOXTITLE 类 0 flags；`check_s11.py fr` RC=0，ALL PASS；P7 三处旧 HEAD TOO WIDE 节头（ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER）渲染中均在栏宽内 |
| 孤儿标点 | SVG `<text>` 独行 。/独行右引号/独行 ：/– **0**；text.md 独行标点行 **0**；印版文字层独行标点行 **0**；无 `<text>` 以 ”/。开头 |
| 字符/引号 | “ 82 / ” 82 成对；U+2019 0；ASCII 撇号 73；U+00B7 282（与核心完全一致）；U+3000 141；可见文字真实 CJK 0（仅蛾标非可见 `<title>Lucerna 三色蛾</title>`，与核心共有）；“Note \| Note \|” 0；禁词（TODO/FIXME/Lorem/占位/SOP/proofread/cover/bridge/XXXX/TBD）0 |
| VOL 计数 | VOL.4 12、VOL.5 8、VOL.3 3，逐页与核心完全一致 |
| ABSTRACT.txt | 一行 + 结尾换行，775 B，法语，无 ASCII 双引号 |

## 150 题逐题手验（text.md 1305 行全文通读 + SVG 题面核对 + registry 对照）

- 编号连续 1–150；每页 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22；text.md 附录 150/150 与 registry 一致（137–140 为键句 + 注记括号形式，键句本身一致）。
- 五组配对题逐组对 SVG 渲染核对：P2（24b/25c/26a/27d ✓）、P3（38b、**39a、40d**、41c ✓）、P4（56b/57c/58d/59a ✓）、P5（74d/75a/76b/77c ✓）、P8（141b/142c/143d/144a ✓）。
- 逐题核对题面、原文、图表、算术：全部正确。要点：Q7 B 254、Q9 C 218（254−218=36）、Q49 A 2010–11、Q52 hosted、Q55 won、Q83 C 19、Q84 A 33/35、Q87 C 435（254+162+19=435）、Q97 takes、Q100–107 演练（won/more/lost/will/published/whether/chose/win）、Q108–111 改错、Q112–119 完形（Tuesday/call/continues/will meet/writes/will certify/wears/will watch）、Q120–132 选择/阅读、Q133–136 句型、Q137–140 翻译（法译准确）、Q145–149 对话（row/film/popcorn/show/Friday）、Q150 开放写作；模型文 “My Monday, November 16” 82 词（字母数字 token 计，与核心一致）。
- 金句：P7 8 句逐字出自本期正文，页码标注（P1/P2/P3/P4/P5/P6）正确。

## 8 页逐页目视（印版 P1–P8 全页 + 网版 P1/P8，72 dpi；D2/D3 盒另有 200 dpi 裁图）

- 除修复处外无溢出、重叠、压页脚、图片与出处问题；页脚 `Page N sur 8` 全 8 页正确；刊头/徽章/栏目条齐全；P8 答案块在页内，未压页脚；网版与印版视觉一致。
- P1：SEARCHES 盒末行在盒内，下方留白（200 dpi 裁图证实）；IN BRIEF Ashes 行为回顾口径；LIGHTNING QUIZ Q7–10 齐全。
- P2：DID YOU KNOW 盒末行 `November 3.` 在盒内，下方留白（200 dpi 裁图证实）；SENATE IN NUMBERS 短标题贴合；SAY IT 中栏 `Le nouveau Congrès se réunit en janvier.` 在栏内。
- P3：与旧版像素 **0 差异**；配对题 a–d 选项齐全；Rousseau 图 + 出处齐全。
- P4：回顾版全文 + W.G. Grace 图 + `SATURDAY, NOV 21` 短标题 + `Arsenal are winning!` 均正常；栏底留白为模板流行为（与核心同）。
- P5：SPEAK UP / FRIDAY'S WORDS / THE JUNGLE, TOO 正常；D 节头在栏底、题在下栏为模板流行为（与核心同）。
- P6：READ THE CHART（`chiffres annoncés`）+ 练习选票 ☐ + 投票亭图 + 出处齐全。
- P7：工具盒 B2 无 encore；三处旧超宽节头在栏内；NEXT WEEK 为 June 2027 口径；Johnson 图 + 出处齐全。
- P8：答案键块 1–150 齐全，`39. a · 40. d`、`125. A (4–1)` 正确；模型文 82 词在框内。

## 与旧版逐页对比（旧版 = 上轮 proof1 的建版，印 SHA `14da9810…`）

- 文字层 token 多重集差：全部差异落在修复集内——Ashes 预告→回顾重写（`2025–26` / `4–1` / `Brisbane` / `Adelaide` / `Melbourne` / `Sydney` / `hosted` / `won` 等新增；`Perth is winning` / `begin` / `1st` / `2:20` 等旧词消失）、`confirmé`→`annoncé`（Q7/Q82/Q83/Q84 注、P1 条头 `Résultats annoncés`、P6 桥句 `chiffres annoncés`）、Q39/Q40 键、Q52/Q55 词干与键、Q125 改写（旧键 C→新键 A）、P1 SEARCHES 第 2 项 `ashes`→`thanksgiving`、`encore` −1（仅 P7 工具盒一处删除；Q138 注与读者来信注的合法 `encore` 保留）、SENATE/SATURDAY 短标题。单 token 差异已逐项定位：`19` 17→16 为旧 Q125 词干 `Thu, Nov 19` 消失；`Turin` 7→6 为旧 Q46 干扰项 `Sunday, November 22, in Turin` 消失；`Day` 12→10 为旧 Q55 词干 `Day one is already sold out` 消失；`1st` 1→0 为旧 `1st Test` 消失；其余为 pdftotext 块重排假象（token 多重集已证内容同一）。
- 像素差（72 dpi，旧版渲染 vs 新版渲染）：P1 33,905（SEARCHES 榜、条头措辞、IN BRIEF Ashes 行）、P2 53,846（SENATE 标题、周六导语、DID YOU KNOW 盒高 325.5→352.5 致 AND YOU? 盒下移）、P3 **0**、P4 587,776（Ashes 重写）、P5 6,275（仅 THE JUNGLE, TOO 一段 `the Ashes begin on Saturday morning in Perth`→`the football is back on Saturday`）、P6 536（仅 P6 桥句 `confirmés`→`annoncés` 一行）、P7 294,029（NEXT WEEK 重写、B2 encore 删除、A2 Try-it 段因 June 2027 口径变长致左栏下移）、P8 17,366（键 39/40、125 与注记 7/46/52/55/82/83/84）。每处差异均已对图定位，无修复集之外的变化。

## 仅记录、不计入判定

- **D5 字体（生产级待定项）**：P8 渲染有效最小字号 10.12 pt，对应 SVG 属性值 13.5 pt（KIT “13.5 pt” 写的是属性值而非渲染有效值，因答案键块在 0.75 缩放组内）；10.12 pt 仍 ≥ §1.1 下限 9.75 pt，无违规。仅记录，不计入本轮判定。

## 已核对无问题（要点）

- 外部事实：选举数（众院 254/162/19、参院 20/13、2 未定 AK/MS、7 翻转州、5 州长翻转、选前 218–214/53–47、Johnson 不竞选共和党领袖、众院共和党 11 月 10 日/民主党 11 月 18–19 日选领袖）与 r1 核实一致，无改动；Hunger Games、I'm a Celebrity、Anti-Bullying Week、ATP 总决赛、英超第 11 轮、NFL 第 11 周与 r1 核实一致，无改动；Ashes 回顾见上（本轮新核实）。
- 读者来信：P7 读者来信栏明示截稿时无来信、VOL.5 起登真实来信，与 F-MAIL 规则一致，未编造来信。
- 保留的模板行为（与核心同，非缺陷）：P4/P5/P6 栏底留白；P5 D 节头栏底、题下栏；P7 “Irregular verbs in this issue: win →” 跨栏接续；P1 数字盒英文术语 + 法语括号注释（W46 fr 惯例）；Q90 答案注 `Deux sièges du Sénat restent à confirmer`（核心 `两个参议院选区尚未确认` 的忠实翻译，此处 “confirmer” 指待确认的未宣布选区，与 D4 所指“把已宣布数称作已确认”不同义）。

## 未独立再核实（核心层、低风险，沿用 r1 结论，内容未改动）

- 世界儿童日 2026 主题措辞 `My day. My rights. My future.`（日期 11 月 20 日与 1989 年《儿童权利公约》已核实）；Hunger Games 原声专辑 11 月 13 日；ATP 决赛“不早于 18:00”；各州认证窗口 11 月 10 日–12 月 18 日（区间表述）；Lawrence 儿童照片日期 1912 年 2 月 19 日；投票亭图片说明细节。
