# PROOF-NOTE — 2026-W47 core-it fix3 独立复校（proof3）

**结论：(a) 零问题可定稿。缺陷数：0。**

复校员：子代理（独立复校，核心层）。复校日期：2026-11-11。
复校对象：`production/2026-w47/core-it/`，fix3 定稿（commit `36bdec2e` 的 5 个源文件 + 两份 PDF）。

## 0. 身份核对（磁盘为准，三 SHA 与任务一致）

| 文件 | SHA-256 | 字节数 | 与任务消息 |
|---|---|---|---|
| `La-Lucerna-VOL4.pdf`（印） | `2ee50d92635ba496d65c09c085a9b70fbebad62a8d6f3b81c41afec4be47a412` | 27,726,350 | 一致 |
| `La-Lucerna-VOL4-web.pdf`（网） | `ab14a5b7bbf532e0633fee0006f5c19f44bc558b9ad475ad523d5bd0aaaecab0` | 1,790,620 | 一致 |
| `2026-w47-it-zh-cn.text.md` | `d0c573b83fa679262c2da0734b08b1f504782829c11d29c9ed1e2c8cac08dbcb` | 52,676（1317 行） | 一致 |

- 本地 commit：`36bdec2e`（完整 `36bdec2ed2b32000e512bfa65e7fb705464d8243`），仅含 5 个源文件（`content12.py`、`content34.py`、`content8.py`、`WEEKLY-KIT.md`、`2026-w47-it-zh-cn.text.md`），与 FIX-LOG §11 一致。两份 PDF 在 git 状态为未追踪文件（`??`），属已知状态，未动。
- 复校期间仓库 HEAD 前进了（当前 `4b688318`，core-pt fix1），`36bdec2e` 仍为 HEAD 祖先；复校结束时三文件 SHA 重新核对，与上表一致，复校期间无人改动目标文件。
- 复校员未改动任何源文件、未重建、未 commit、未 push。freeze baseline 的重建输出只放在 scratch 内，未碰 shipped 文件。

## 1. 缺陷清单

**无。缺陷数 0。** 全文通读（印 PDF 8 页 + text.md 1317 行全文）、150 题逐题手验、全部机械门实跑、必查项 (a)–(g) 逐项核实后，未发现任何达到缺陷严重度的项。

## 2. 未决事项（观察项 O，全部不拦停）

### O1 — P4 成绩表 5 行伸入栏间沟槽（P4，宽表故意跨栏，无碰撞）
- 实测（PIL 真墨，相对网格栏边）：Cagliari–Frosinone 522.0（超 col1 右 510.5，+11.5）；Torino–Lecce 971.0（超 col2 右 961，+10.0）；Genoa–Milan 972.0（+11.0）；Roma–Sassuolo 991.0（+30.0，越过整条沟）；Fiorentina–Juventus 1040.0（+79.0）。数值与 FIX-LOG 在 0.4px 内一致。
- 机制已由 SVG 结构证实：斑马纹奶油带 y=1156/1280/1404 各 h=62、间隔 124px，分别罩第 1/3/5 行；第 2/4/6 行故意在纸面。伸出的 5 行同行下一栏无文字（Monza–Atalanta 同行距 Genoa 墨 21px），零碰撞、读者不可见。建议：维持现状，不改本次定稿。

### O2 — P4-d 为全期最紧的一行（P4，匹配题 d "il primo posto in classifica, la cima"）
- 三法分歧：PIL 真墨 958.5px（版心内 +2.5px）；PDF span advance 框 721.7pt（出栏边 720.75pt 约 +0.95pt）；200dpi 像素墨恰触栏边 961.0px（AA 边缘像素，±0.24px 量化）。
- 以真墨（PIL getbbox）为准判在栏内，不构成缺陷。后续轮次留意即可，不改本次定稿。

### O3 — D7 亚 1pt 痕迹 4 处（方法类，非缺陷）
- PDF span 超边距：P2 副标题 "Una festa, una giornata verde" +1.62pt；P5 Corot 图注 +1.59pt；P8 范文两行 +1.84/+1.93pt；另 P1 dateline "2026" +0.22pt。200dpi 像素墨分别为 +0.7pt、+0.3pt、+1.0/+1.0pt。
- 均在版内 65pt 以上白区，无裁切、无碰撞，读者不可见（0.25–0.35mm）；属渲染器与度量字体 advance 差（约 0.5–0.8%）。FIX-LOG §7 称"三数值在 it-de/it-ja/it-en 已发 PDF 中完全相同"——该断言本轮无法独立核实（本仓无 `issues/2026-w47/` 目录；W46 已发版 PDF 为旧版式，版心不同，绝对 pt 值不可横比——见 GATE-LOG §4）。不拦停。

### O4 — P4 成绩表日标签重复（P4，版式特点）
- SAB 7.11 ×2、DOM 8.11 ×2，因表按日分组分行、每行自带日标签；每行内比分与日期一致，无事实错，略显冗余。非缺陷。

### O5 — text.md H1 为裸 slug `# 2026-w47-it-zh-cn`（管线级，非 fix3 引入）
- "W47"/"SOP"/"proofread"/"cover" 在 text.md 均为 0 命中；"it-zh-cn" 与 "2026-w47" 仅在此首行 H1 各出现 1 次。
- 查证：导出脚本 `export_w47_textmd.py:21` 硬编码 `out_lines = [f"# {slug}", ""]`；W46 已发版 `issues/2026-w46/2026-w46-it-zh-cn/2026-w46-it-zh-cn.text.md` 的 H1 同为 `# 2026-w46-it-zh-cn`。即 it 系既定导出格式，de 系则用正式标题（如 `# Die Lucerna · VOL.3 — 9. bis 15. November 2026`），两系不一致。与 SOP 对外禁内部标签（周次/语言代码）的字面要求有张力，但属管线级事项、非 fix3 引入，不拦停，建议后续统一。

### O6 — 两题设计说明（非缺陷）
- ex.58 "la serata di domenica è la serata ___ del weekend. (bella)" → "più bella"：注释本身已标主观，比较级填空合法。
- ex.82 "BookCity apre il 22 novembre" 判 Falso：有意考查 apertura（周一 23 日）与 anteprima（周日 22 日）的区分，正文两处区分一致。

### O7 — 方法备注：两机械门对纯拉丁改动盲
- `tools/freeze.py` 只有 `baseline`/`diff` 两个子命令，无 `freeze_direct`（任务要求记为方法备注，非缺陷）；freeze diff 只做 CJK 会计，p8 compare 只比键值——纯拉丁行改动对两门皆盲（FIX-LOG §6 已记）。本次由三法实测 + 150 题手验覆盖该盲区。

### O8 — 自查方法误报两例（属复校员脚本，非报纸问题）
- 我方 PIL 脚本曾用 Newsreader 度量刊头，误报 1988px 溢出；已用 PDF span 证伪（刊头实为 UnifrakturMaguntia 147.0pt，bbox x 404.77–1058.04pt，居中在版内）。
- 旧版像素脚本 `pixel3.log` 中 P4-a/b/c 与 P8-a/b/c/d 的 "OVER" 值是未限 x 窗口、误拾同行他栏墨水的假阳性；已由 `pixel3b.py`（`render-scan-proof-it3.txt`）纠正，不得引用旧值。

## 3. 核实摘要

### 3.1 全文通读与 150 题手验
- text.md 1317 行全文读完；印 PDF 8 页 200dpi 渲染件（`render200/p-1.png`…`p-8.png`，4063×5625）逐页目视 + 11 张关键裁图目视（P2 匹配块、P1 D1 段、P3 Torrazzo 段、P3 E TU 盒底、P4 成绩表、P4 匹配块、P7 工具箱、P8 F 块、P1 弯引号、P8 "Fate dolci"、P5 E TU 盒底），全部通过。
- 150 题逐题人工核对题面、原文、键；题号连续 1–150 无缺无重；题干键与文末 RISPOSTE 列表程序比对 0 不一致；P8 打印键三方比对 150/150（唯一"差异"为 ex.150 开放题：登记键为占位、P8 印 "✓"，属预期行为）。
- 分布：每页 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；级别 A2 47 / B1 70 / B2 33；范文实测 99 词（与 KIT 一致）；头条 39 字符（不含空格，≤56）；8 句 P7 金句在 text.md 空白归一化全文中各出现恰好 2 次；MD11 十场比分之和 24 球；图表题 85（13−11=2）、86（6+7=13）算术正确；全部变位/性数/虚拟式手验正确（ex.40 è arrivato、42 sono andati、62 sono arrivati、108 è finita、93–96/109–111 虚拟式 piova/nevichi/controllino/sia/leggano）。

### 3.2 必查项 (a)–(g) 逐项结论
- **(a) D1 通过。** `TZ=Europe/Rome date` 核：2026-11-21 周六、11-22 周日。多源证实意甲第 12 轮 11-21 至 11-23：Lazio–Lecce 周六 11-21 15:00（DAZN，Stadio Olimpico）、Atalanta–Inter 周日 11-22 20:45（DAZN，Gewiss Stadium, Bergamo）、Monza–Fiorentina 周一 11-23 20:45；第 12 轮周六另有 Como–Cagliari 15:00、Parma–Roma 18:00、Napoli–Torino 20:45；周日另有 Juventus–Venezia 12:30、Bologna–Udinese 15:00、Sassuolo–Genoa 15:00、Milan–Frosinone 18:00。P1 "domenica sera"（周日 20:45）无误；与 P4（"riparte sabato 21… lunedì 23"、Lazio 周六、Atalanta–Inter 周日 20:45、Monza–Fiorentina 周一 20:45）及 P1 CIFRE 栏 "20.45 — l'ora di Atalanta–Inter, domenica 22 novembre" 全部一致，无自相矛盾。
- **(b) D2 通过**（未重议长/短措辞方向）。三法实测两行首行在版心内：PIL b 1830.5/d 1821.5px（余 31.5/40.5）；PDF span b 1375.1/d 1367.6pt（余 21.4/28.9）；像素 b 1374.1/d 1366.6pt（余 22.4/29.9）；续行 novembre 1580.5px / chiesa 1539.5px。措辞为正确意大利语（"per la festa in novembre"、"la piccola luce di cera accesa in chiesa"，分词 accesa 与 ex.13 "candele accese" 的已用词汇一致）；键 b/d 与注释不动（text.md 26/b、27/d 与 RISPOSTE 一致）；信息无损（"21" 日在 P2 正文及 ex.23/120 中另有考查）。
- **(c) D11 通过。** it.wikipedia "Torri e campanili più alti d'Italia"：1º Mortegliano 113,20 m、2º Torrazzo 112,12 m（该表数字；Mortegliano 词条正文写 Torrazzo 112,54 m，测量口径差不影响名次）；"Campanile di Mortegliano" 词条："113,20 metri… il primo campanile, precedendo in altezza il più noto Torrazzo di Cremona (112,54 metri)"；Mortegliano 1955–1959 钢筋混凝土、非中世纪砖塔；Torrazzo 为中世纪砖塔，it-wiki 定性 "la torre medievale e la torre in laterizi più alta d'Italia"（wellme.it 亦称 "il campanile medievale in laterizio più elevato d'Europa"，112.54 m）。"campanile medievale in mattoni" 限定正确；欧洲头衔未用（Landshut 砖塔约 140 m 更高），正确。
- **(d) D12 接受记录已核实。** 全源（`content*.py`、text.md、SVG）"18 novembre"/"mercoledì"/"MER 18" 零命中；text.md 中 "18" 命中全部为时间（ore 18）、年份（1898、1868）或题号 18；P6 "LA STRADA DELLA MANOVRA" 四步 28 OTT / 9–12 NOV / MAR 17 NOV / 31 DIC 无 11-18 事；P5 "IL PIANO DELLA SETTIMANA" 五条为周五/周六/周日/周日/周一，无周三。6 天为编辑选择、未编造内容。
- **(e) P4/P8 收紧 5 行通过。** 逐行三法实测在栏内（P4-b PIL 821.5 / span 617.2pt / 像素 615.6pt；P4-c 943.5 / 708.6pt / 707.0pt；P8-a 1377.3px（像素 1034.3pt）/ b 1360.0px（1020.6pt）/ c 1388.0px（1042.2pt）/ d 1394.0px（1045.1pt））；键/注释不动（text.md 53/b、54/c、142/c、143/b、144/a 与 RISPOSTE 一致）；语义不变（"che non ha mai perso" = imbattuto；"il gruppo di squadre in un torneo" 仍唯一指向 girone；"un livello di reddito del sistema fiscale" = 税级；"i soldi che pagano una misura" = 资金来源；"la differenza tra spese ed entrate" = 赤字）。
- **(f) P7 toolbox 与 P3 E TU 盒底通过。** P7 toolbox 3 盒：min inside clearance +4.5，min desc-clear −1.5；像素实测 ERRORI TIPICI 末行墨底距盒底 +17.0px、LA PAROLA +3.4px、LETTERE +3.4px，全部在盒内。P3 E TU 盒底末行中文完整在盒内（像素 +2.6px，裁图目视确认末行 "更喜欢牛轧糖还是巧克力？写两句寄来。" 完整、盒底留白清晰）；desc-clear −2.1 确为计量假阳性。
- **(g) 全文重读与外部事实抽查：无新事实/语言缺陷。** 抽查全部证实（详见 GATE-LOG §2）：MD11 全部 10 场比分与 20 队积分表（24 球；Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Frosinone 20、Juventus 18、Bologna 17、Cagliari 16、Napoli 15、Torino 14、Atalanta 14、Genoa 13、Lecce 10、Fiorentina 9、Parma 8、Sassuolo 8、Monza 7、Venezia 6、Udinese 5；Lazio 不败、Gattuso 执教、Roma 最佳进攻 31 球）；Torrone 29 届 11-07 至 11-22、16 天、主题 «Il Confine»、1441 年 Sforza–Visconti 婚礼传说、闭幕日 11-22 Torrone d'Oro 授予 Davide Simonetta（11:00 Palatorrone，官网）、corteo 16:00（150+ figuranti）、rievocazione 17:00 Piazza del Comune、sbandieratori + 火把艺人、gran finale 18:00 «Il torrone va in brodo»；Eurochocolate 32 届 11-13 至 11-22、主题 «Fate dolci»、Calabria 首个 guest region（bergamotto、cedro、peperoncino、fichi cosentini）、Fri 11-20 18.15 «I tesori della Calabria Straordinaria»（LAB）、Sun 11-22 Iginio Massari 任 gran finale 嘉宾；BookCity Milano 15 届 11-23 至 11-29、主题 «Il senno sulla Luna»（Ariosto《Orlando Furioso》）、1,360 活动 / 2,487 嘉宾 / 1,164 书 / 443 场地、开幕周一 11-23 20:00 Teatro Dal Verme（Colson Whitehead，2 次 Pulitzer）、anteprima 周日 11-22 16:00 Edmund de Waal（Fondazione Luigi Rovati）；Torino Film Festival 44 届 11-24 至 12-02、9 天；ATP Finals 11-15 至 11-22、Inalpi Arena、8 单打（Zverev No.1、Alcaraz、Shelton、Medvedev、Cobolli 首秀、Fils、Tiafoe、Jodar）、Sinner 因膝伤缺席（2024–25 冠军）、抽签周四 11-12、McEnroe/Lendl 分组、决赛周日 11-22、双打 Bolelli/Vavassori；Madonna della Salute 11-21、1630 瘟疫誓愿、Longhena 1631–1687、船桥 ponte votivo、蜡烛、castradina 于 11-20 晚食用、"quasi quattrocento anni"（1630→2026 为 396 年）；Festa dell'albero 1898 年起源、2013 年立法为国家日、Santa Cecilia 11-22 为音乐主保；Manovra：DPB 10-15 送布鲁塞尔、CdM 10-28 批准约 26bn（报章重建口径）、法案号 C. 3174-bis、听证会 11-09 至 11-12（Giorgetti 周四 11-12 约 16:00）、修正案截止周二 11-17 18:00、12-31 前终批、DPB 增长 +0.8%/赤字 3.4%（2027）、金融行业出资约 5bn（报章重建口径）；Sforza–Visconti 婚礼 1441-10-25 属史实；Alba 白松露节 10 月 10 日–12 月 6 日、第 96 届（官网 fieradeltartufo.org + Italia.it）。

### 3.3 机械门总览（全部自跑，详见 GATE-LOG）
| 门 | 结果 |
|---|---|
| occlusion 审计 + selftest | 8 页 **0 flags**；selftest 6 类阳性全触发、干净对照沉默 |
| creambox 全版扫描 | 29 盒；负窗 8 处均为已知假阳性（逐项裁定，见 GATE-LOG） |
| P7 toolbox clearance | 实测通过（min inside +4.5；墨底余量 +3.4…+17.0px） |
| freeze baseline 8/8 | 字节一致，SVG SHA 与 FIX-LOG §0 逐一吻合 |
| p8 extract / compare | 150/150；CLEAN，missing=[]、extra_count=0、uncertain=[]、keydiff=[] |
| keycheck | 150/150（题干键 vs RISPOSTE vs P8 打印键三方一致） |
| boxtitle 逐个实测 | 84 行，最大真墨 1831.9px（余 30.1px），无溢出 |
| 印/网文字层比对 | 各 44,001 B，`cmp` 字节相同；网 PDF 8 页 |
| P8 最小字号实测 | **9.75 pt**（534 个 span），全局最小亦 9.75 pt，符合 SOP §1.1 下限 |
| 弯引号扫描 | U+201C/U+201D 各 3 对（text.md），SVG 中 P1/P8 各 1 对，渲染正常；U+2019 全版 0；意大利语撇号统一 ASCII |
| 内部标签扫描 | "W47"/"SOP"/"proofread"/"cover" 均为 0；仅 H1 slug 含周次/语言代码（见 O5） |
| 三法横向实测 | P2 b/d、P4 a–d、P8 a–d 全部在版心内（P4-d 见 O2） |
| 盒底像素实测 | 9 处 desc-clear 负值全部证伪，最紧 +2.6px |

## 4. 交付文件（scratch）
- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`（全部机械门实跑证据 + 外部事实来源 + 判为非缺陷的项）
- `keycheck-150.json`（150 题逐题手验结果：题号、级别、题型、键、RISPOSTE 键、P8 打印键、核实依据、结论；150/150 pass）

## 5. 结论重申
**结论 (a)：零问题可定稿。** 缺陷 0 项；观察项 O1–O8 均不拦停。三个 SHA 与任务消息一致。
