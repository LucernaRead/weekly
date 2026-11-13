# PROOF-NOTE — Lucerna Weekly 2026-W47 it-fr（proof1 独立复校）

- **复校员**：proof1（只读复校；不修版、不 commit、不 push、不派 subagent）
- **复校日期**：2026-11-11
- **复校对象**：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-fr/`（对照 core：`~/workspace/weekly-git/production/2026-w47/core-it/`）
- **依据**：`~/workspace/weekly-git/SOP.md` §1.1、§8、§9；`~/workspace/weekly-git/AGENTS.md`；协调员 brief；本版 `WEEKLY-KIT.md`
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-fr1/`

## 0. 三件 SHA 核对（开工前，sha256sum 实测与任务所给一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-FR.pdf` | 14,034,268 B | `5445d1a62f631bb75cafcb20df40c376d44b608254824444166714670f2dc0c7` |
| 网页 PDF `La-Lucerna-VOL4-FR-web.pdf` | 1,258,939 B | `416b11053b82475ad84bcb1badc10d992357a3e0fbde1786c55bee693bb3c0a8` |
| 文本导出 `2026-w47-it-fr.text.md` | 56,616 B | `b3d5c147bb68d58c8b6cb0e2d68b0beaf0fa7782b51c0649e0215473c220de1d` |

探针通过：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）。

## 1. 机械门禁（全部跑完，2026-11-11）

| 门禁 | 结果 |
|---|---|
| `tools/p8.py compare`（显式 `--core-p8 …/core-it/svg/p8-valutazione.svg --edition-p8 …/2026-w47-it-fr/svg/p8-valutazione.svg --total 150`） | **CLEAN**；两版各 150/150 noted；keydiff 仅 [137, 138, 139]（预期的法语重定向键：Q137–139 为"译成法语"题，键为法语句，与 core 中文键不同，属正常） |
| `tools/p8.py extract` | 两版各 150/150 |
| 独立 keycheck（自写脚本：.text.md 150 个 key 对 P8 提取键 + RISPOSTE 表互对） | 150 题 key 全匹配，仅 #150 例外（写作开放题，P8 为 ✓，预期内）；RISPOSTE 149 条与题干 key 0 偏差 |
| `tools/freeze.py diff --core-svg …/core-it/svg` | 每页新增 CJK = 1，全部是 U+3000 全角空格（SOP §1.1 家具分隔符），共 8 个；P1 +30/−46、P2 +34/−29、P3 +33/−30、P4 +29/−26、P5 +42/−41、P6 +30/−25、P7 +42/−40、P8 +163/−629（与 KIT 一致）。已逐项核查 freeze-diff.json：新增串无 U+3000 以外的 CJK；无 CJK 的删除串均为同段意大利文的换行重切碎片（如 P5 "Calabria» a Eurochocolate"、P6 "copertura · scaglione"、P7 "è probabile che / è possibile che / bisogna"），原文仍在法语版中以不同断行出现，无内容丢失 |
| `tools/freeze.py baseline`（重跑本版构建） | **8/8 SVG 字节一致**，core SVG 未被改动 |
| `tools/occlusion_audit.py`（自检通过，六类阳性对照全触发） | **0 flags** |
| 印刷/网页 text layer（`pdftotext`） | 各 106,873 字节、8,028 词，词多重集完全相同；两版均为 8 页、1462.5×2025 pt；网页 PDF < 7 MB |
| P8 最小字号（PyMuPDF 实测渲染 pt） | P8 **9.75pt**（SOP §1.1 下限，KIT 所述 13 SVG px 一致）；其余页最小 11.62pt（P6 为 12.75pt） |
| 印刷文本文本检查 | VOL.4 ×9、VOL.5 ×3（均在 KIT 所述 3 处合法位置：下期预告、LETTERE 声明、P2 交叉引用）；"·" 148 次（KIT 所述数，与 core 一致，仅在选项串/词汇表内）；8 页页脚均为 `La Lucerna　HEBDOMADAIRE ITALIEN VOL.4　TEXTE EN ITALIEN　EXPLICATIONS EN FRANÇAIS` + `Page N sur 8` |
| ABSTRACT.txt（SOP §9） | **通过**：法语单行、无 ASCII 双引号、含真实主题（Serie A 11ª giornata、Lazio 29 分、Torrone、Eurochocolate、Madonna della Salute、BookCity、Torino Film Festival、预算案）、含刊名 La Lucerna、目标语名 italien、A2–B2、150 exercices。.text.md 无摘要节——与 core-it 同样，属既定模式（insert 时写 frontmatter），不算缺陷 |

## 2. 内容事实核查（公开来源逐项核实，2026-11-11）

全部通过，无事实错误。核实要点如下：

- **Serie A 11ª giornata（11 月 6–8 日）**：10 场比分与本版完全一致（Venezia–Udinese 2–1、 Cagliari–Frosinone 1–0、Torino–Lecce 1–1、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2）；24 球；积分榜 Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23（7 胜 2 平 2 负，18:10，+8）/ Udinese 5（多源一致：sportradar 积分表、tuttoudinese.it、tuttomercatoweb.com、antoniogenna.com）；Roma 最佳攻击 31 球；Udinese 垫底；"La Lazio di Gattuso"（多源）；Lazio 与 Roma 保持不败。
- **MD12 预告**：Lazio–Lecce 周六 11 月 21 日 15:00 主场；Atalanta–Inter 周日 11 月 22 日 20:45 于 Bergamo；Monza–Fiorentina 周一 11 月 23 日 20:45 收官（Lega Serie A 赛程，多源一致）。
- **Nations League**：意大利–法国周四 11 月 12 日 20:45 圣西罗；比利时–意大利周日 11 月 15 日 20:45 布鲁塞尔博杜安国王球场（FIGC 官网 figc.it + 多源）。两场均在截稿后，本版未印结果、推迟至 VOL.5，处理正确。
- **Nitto ATP Finals Torino 2026**：11 月 15–22 日、Inalpi Arena；Zverev 世界第一；Alcaraz 为热门；Cobolli 首秀；Sinner 为 2025 冠军、因右膝伤缺席；决赛周日 11 月 22 日、半决赛周六 11 月 21 日；8 人、两组。
- **Festa del Torrone Cremona**：第 29 届，11 月 7–22 日，16 天、3 个周末，主题 «Il Confine»；Torrone d'Oro 于 11 月 22 日 11:00 在 Palatorrone 授予 Cremona 出生的音乐制作人 Davide Simonetta；16:00 Corteo Storico（150+ figuranti）、17:00 Piazza del Comune 婚礼重演（Bianca Maria Visconti–Francesco Sforza）、旗手与火舞至 18:00、18:00 压轴 «Il torrone va in brodo»（官网 festadeltorrone.com 及多源一致）；传说称 torrone 源于 1441 年 10 月 25 日婚礼、形似 Torrazzo；Torrazzo 为意大利最高钟楼。
- **Eurochocolate Perugia**：第 32 届，11 月 13–22 日，口号 «Fate dolci»；Calabria 为首个特邀大区 «Calabria Straordinaria»（bergamotto、cedro、peperoncino、fichi）；«I tesori della Calabria Straordinaria» 于 11 月 20 日周五 18:15 在 LAB-Luisa Annibale Base；Iginio Massari 为 11 月 22 日闭幕嘉宾。
- **BookCity Milano 2026**：11 月 23–29 日、第 15 届、主题 «Il senno sulla Luna»（源自 Ariosto《Orlando furioso》Astolfo 登月取回 Orlando 失去的理智；完整表述 "Il senno sulla Luna · Sette giorni di libri, ragioni e follie"）；开幕 11 月 23 日周一 20:00 Teatro Dal Verme、嘉宾 Colson Whitehead（两次 Pulitzer 奖）；预展 11 月 22 日周日 16:00 Fondazione Luigi Rovati、Edmund de Waal；数字 1,360 eventi / 2,487 protagonisti / 1,164 libri / 443 sedi（milano-business.com、milanofree.it、milanoweekend.it 多源一致）。
- **Torino Film Festival 第 44 届**：11 月 24 日周二–12 月 2 日周三、9 天；开幕 11 月 24 日 18:45 Teatro Regio；闭幕 12 月 2 日 Cinema Massimo；120 部影片；Alba 白松露集市至 12 月 6 日（visitturin.com）。
- **Filmmaker Festival Milano 第 46 届**：11 月 14 日周六–22 日周日、9 天；开幕 11 月 14 日 21:30 Arcobaleno Film Center（Alina Marazzi《La ragazza con la Leica》）；11 月 22 日颁奖 + 闭幕片（官网 filmmakerfest.com 新闻稿及多源一致）。
- **Manovra 2027（Legge di Bilancio 2027）**：DPB 10 月 15 日送布鲁塞尔与议会；2027 增长 +0.8%、赤字 3.4% GDP；总额约 260 亿欧元（CdM 10 月 28 日批准的 DDL 口径；DPB 口径为 235 亿毛额）；法案号 C. 3174-bis（11 月 4 日分拆三条后编号）；听证 11 月 9–12 日（Banca d'Italia 11 月 12 日 14:15、Ufficio parlamentare di bilancio 15:00、部长 Giorgetti 16:00）；修正案截止 11 月 17 日周二 18:00；金融业（银行+保险）约 50 亿覆盖（Relazione tecnica 口径 58 亿；本版"约 50 亿"在公布口径内）；Irpef 第二档 33%（5 万→5.5 万欧元，最高省 500 欧/年，仅限 2027 年）；须 12 月 31 日前表决。
- **Madonna della Salute / 树木日 / Santa Cecilia**：11 月 21 日周六威尼斯 Madonna della Salute（1630 年瘟疫誓愿、Longhena 设计、建于 1631–1687、castradina 为节日传统菜）；同日为 Giornata nazionale degli alberi（1898 年首届 festa dell'albero，Guido Baccelli 发起；2013 年第 10 号法律定为国家日）；11 月 22 日周日 Santa Cecilia（音乐与音乐家主保圣人，庆日 11 月 22 日）。castradina"于 11 月 20 日晚吃"的具体时点未获独立来源证实（见 §7 未核实项；正文以"La tradizione dice che…"作 hedging 表述，不构成缺陷）。
- **内部一致性**：MD11 十场比分求和 24 球；积分榜数字与正文一致；星期已核（2026-11-16 周一…11-22 周日；11-17 周二、11-19 周四、11-20 周五、11-12 周四、11-09 周一）；Torrone 11 月 7–22 日 = 16 天、3 个周末；Torino Film Festival 11 月 24 日–12 月 2 日 = 9 天；P8 范文逐词数过 = 99 词；Q85 13−11=2、Q86 6+7=13 正确。

## 3. 语言复校

- `2026-w47-it-fr.text.md` 1317 行已逐行读完（P1–P8 + RISPOSTE 全表）。意大利语正文与法语讲解层已逐句读过；练习键与题干语义已核对。
- 150 道题的键已逐题对照题干/原文/图表做语义核对；三个匹配题已在渲染图上核对定义字母：P2 Q25–28（25 salute→c、26 ponte votivo→b、27 candela→d、28 piantare→a，全对）、P4 Q52–55（52 vetta→d、53 imbattuto→b、54 girone→c、55 debutto→a，全对）、P8 Q141–144（141 manovra→d、142 deficit→c、143 copertura→b、144 scaglione→a，全对）。
- P7 八句金句已逐句核对，均逐字出自本期文章（P1/P2/P3/P4/P5/P6 各出处与 KIT 所述一致）。
- Minor 语言备注（见 §7，不列为缺陷）：Q58 答案注 "le plus beau dimanche soir (un jugement)" 而题干为 "la serata di domenica"（意译式改写，可接受）；P5 IL PIANO 第 1 条法语 gloss "(vendredi: le spécial Calabre d'Eurochocolate à Pérouse)" 中 "le spécial Calabre" 不够地道；Q32 干扰项 "Finestrini"、Q148 干扰项 "cosplay" 古怪但明显错误、无歧义。

## 4. 版式几何复校

- **逐页目视**：印刷版 8 页已逐页看过（`pages/print-1.png` … `pages/print-8.png`，100dpi）。网页版 P1 与 P8 已看过（`pages/web-1-1.png`、`pages/web-8-8.png`），与印刷版一致，无豆腐块，同一溢出在网页版同样可见。P2（LO SAPEVI/E TU/练习 A–D）、P3（中部留白为 core 固有结构，KIT 已说明）、P4（积分榜、赛果斑马表、E TU 盒底贴边但盒内）、P5（中部留白为 core 固有）、P6（MINIME 练习图、PROPOSTA ≠ LEGGE 盒）、P7（三栏语法、Dante 图、FRASI、VOL.5 预告）、P8（A–H 八组、RISPOSTE 三栏、范文 99 词、Vermeer 图）均无其他可见溢出/重叠/压页脚问题。
- **creambox 全版扫描**：canonical 工具 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（+45px 窗口 + 逐行表 + P7 汇总），日志 `creambox-all.log`。负 clearance 已逐条裁定，多数为假阳性：P1 IN QUESTO NUMERO 盒（−24）与 P3 Note 盒（−37）：窗下行是下一节标题，非漫出；P4 三个赛果盒窗下行（+29/+40）：斑马纹隔行（奶油行与纸面行交替），赛果表 10 场完整，非漫出；P6 两个盒（−42）：窗下行是 ESERCIZI 标题，非漫出；P7 工具盒：3 盒，最小盒内 clearance +4.5，最小 desc-clear −1.5（0.30em allowance 口径）。
- **真墨迹实测**（照抄 occlusion_audit.py 的 ink_box 法：4× 字体 + getbbox + ascent 换算，PIL）：最紧的末行实测盒底余量——P2 LO SAPEVI +5.05、P2 E TU +4.75、P3 WEEKEND +5.05、P3 E TU **+0.00**、P4 E TU **+0.00**、P5 NUMERI +4.80、P5 E TU +0.10、P7 LA PAROLA **−0.05px**、P7 LETTERE +0.58、P7 ERRORI +13.06、P1 日历盒 +9.50、P6 盒 +27.20。P7 LA PAROLA 的 −0.05px 为舍入级、不可见，不构成缺陷（记为 §7 测量备注）。
- **横向漫出全扫**（自写脚本：全部 #f0eee5 奶油盒 + #37402f 绿条，真墨盒比对）：**仅 4 处溢出**（即 D1–D4），绿条标题 0 溢出。4 处均为法语盒题比 core 中文标题更宽、盒未随之改宽所致。
- **Abutting 扫描**（自写 `abut_scan.py`，PyMuPDF span 间隙法）：印刷与网页各 **34 flags，完全相同**。已逐条裁定，全是设计间距（"→ ___" 空白线前的间隙、P7 ERRORI 箭头分隔、动词变位箭头）或全角冒号 "：" 的 advance-box 伪重叠（P8 冻结注释 16/19/60/61，裁图 `crop-p8-colon.png` 目视确认冒号渲染正常、无墨迹碰撞）。"：" 在法语版 P8 出现 7 次、core 25 次，属继承标点。
- P8 "— PAGINA 8 —" 分隔符落在第 2 栏底部、其内容（113–150）在第 3 栏：与 core 的 SVG 坐标完全相同（x=989, y=2533.76），属 core 级版式，不算本版缺陷。

## 5. 缺陷清单（verdict (b) 的依据）

### D1 — P1「LA SETTIMANA IN CIFRE」标题横向漫出 +173px

- **位置**：P1 左上奶油盒，盒题 `LA SETTIMANA IN CIFRE　LA SEMAINE EN CHIFFRES`（Noto Sans CJK SC 23px 粗体）。
- **证据**：PIL 真墨迹测量：标题墨迹 x=556.5–1133.0（宽 576.5px），奶油盒 x=538–960，右溢 **173px**；core 同标题墨迹 556.5–960.0，恰好贴合盒右缘。裁图 `crop-p1-cifre.png` 目视可见 "LA SEMAINE EN CHIFFRES" 约一半落在盒外纸面上。
- **修法**：缩短法语标题（如拆两行）或加宽盒；并在 fan-out 构建层对盒题做真墨迹宽度校验（盒宽须 ≥ 墨宽），避免同类法语加长标题再次漫出。

### D2 — P1「LA SETTIMANA」日历副标横向漫出 +27.2px

- **位置**：P1 日历盒副标 `Cette semaine　Cosa succede, giorno per giorno`（19px）。
- **证据**：真墨迹右缘 1889.2，盒右缘 1862，溢 **27.2px**，且超出版心右缘 1884（入右边距 5.2px）；core 副标右缘 1839.2 在盒内。裁图 `crop-p1-cal.png` 可见盒边切断末词 "giorno"。
- **修法**：缩短副标或加宽盒；同 D1 的构建层宽度校验。

### D3 — P2「LA FRASE PER RICORDARE」标题横向漫出 +30.8px

- **位置**：P2 奶油盒题 `LA FRASE PER RICORDARE　À RETENIR`（23px 粗体）。
- **证据**：真墨迹右缘 990.8，盒右缘 960，溢 **30.8px**；core 右缘 918.0 在盒内。裁图 `crop-p2-frase.png` 可见末字母 R 被盒边切断。
- **修法**：同 D1（缩短法语段或加宽盒）。

### D4 — P7「ERRORI TIPICI」标题横向漫出 +46px

- **位置**：P7 右栏奶油盒题 `ERRORI TIPICI　ERREURS FRÉQUENTES`（23px 粗体）。
- **证据**：真墨迹右缘 1908.0，盒右缘 1862，溢 **46px**，超出版心右缘 1884 达 24px；core 右缘 1735.8 在盒内。裁图 `crop-p7-errori.png` 可见盒边切断 "FRÉQUENTES"（"FRÉQUEN|TES"）。
- **修法**：同 D1（缩短法语段或加宽盒）。

### D5 — 法语讲解层字体违反 SOP §1.1

- **位置**：全版 8 页全部法语讲解文字（注释、盒题、栏目标题、页脚）。
- **证据**：
- SOP §1.1 字体表原文（SOP.md L64）："刊别、讲解层、栏目小字、页眉页脚 | 拉丁读者语言用 Newsreader；俄语读者用 Noto Sans；中日韩读者用 Noto Sans CJK（按字形选） | 500 / 700"。法语为拉丁读者语言，讲解层应用 Newsreader。
- 本版 8 页 SVG 实测：全部法语讲解元素 font-family 均为 `Noto Sans CJK SC`（每页 69–106 个元素；如 P1 69 个、P7 71 个、P8 106 个），无一为 Newsreader。意大利语正文为 Newsreader（正确，符合"拉丁书写的目标语标题、正文用 Newsreader"）。渲染图上法语注释呈无衬线体、与意大利语衬线正文可辨不同。
- 同法在 de-fr 与 en-fr 版 SVG 中亦然，属 W47 fan-out 全家族系统性选择；KIT 称"Visual system per SOP §1.1 (same as core-it)" 与此不符（core-it 讲解层为中文，用 Noto Sans CJK SC 是正确的；fan-out 时未按读者语言重映射字体）。
- SVG 中 `Noto Serif CJK SC` 元素仅为 "→" 箭头符号（字形 fallback），非文字，不属此缺陷。
- **严重度**：中。法语文字本身渲染清晰、无豆腐块，不影响可读性；但违反 SOP 写明的字体系统，破坏全版"衬线正文 + 衬线讲解层"的视觉统一，且 KIT 的合规声称失实。
- **修法**：fan-out 构建层按读者语言映射讲解层字体（拉丁读者 → Newsreader；俄语 → Noto Sans；中日韩读者 → Noto Sans CJK）。本版单修无法根治：需在工具层修正后重渲 8 页 SVG + 两版 PDF。W46 it-fr 无 svg/ 存档，无法以 W46 接受先例对照。

## 6. 观察项（不列为缺陷）

- P7 LA PAROLA 盒末行真墨迹余量 −0.05px（舍入级，不可见）。
- P8 "— PAGINA 8 —" 分隔符孤悬第 2 栏底（与 core 坐标完全相同，core 级版式）。
- P8 冻结注释 16/19/60/61 中的全角冒号 "："（7 处，core 有 25 处；KIT 称这些注释"no CJK"措辞不精确，实为继承的全角标点，渲染无碍）。
- Minor 法语/意语备注（见 §3）：Q58 答案注意译式改写、P5 "le spécial Calabre" 不够地道、Q32 "Finestrini" 与 Q148 "cosplay" 干扰项古怪但明显错误、无歧义。
- P3/P5 中部留白、P4 第 3 栏 Note 盒下白空、P7 Dante 图下白空：均为 core 固有结构，KIT 已说明接受。

## 7. 未核实项

- castradina"于 11 月 20 日晚吃"的具体时点：公开来源证实 castradina 为 Madonna della Salute 节日传统菜（仅在节日前后一周可吃到），但未找到独立来源确认"前一晚（11 月 20 日）家庭晚餐"这一具体时点。正文以"La tradizione dice che…"作 hedging 表述，不构成缺陷。

## 8. VERDICT

**(b) 有问题，不可直接定稿。**

缺陷 5 项：D1（严重）、D2（中）、D3（中）、D4（严重）为法语盒题横向漫出，均属 fan-out 本版级——core 对应标题均恰好放得下，盒未随法语加长重排；D5（中）为法语讲解层字体违反 SOP §1.1，属 fan-out 工具级、全家族系统性问题。内容事实、语言、150 题键、全部机械门禁、abstract 均通过；除上述 5 项外无其他缺陷。
