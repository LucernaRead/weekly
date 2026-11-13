# PROOF-NOTE — 2026-W47 it-es 重扩散后独立复校（re-proof）

**复校员**：re-proof（独立复校，只读生产：不改生产文件、不 commit、不 push、不重渲染交付的 web PDF；与重扩散员不同人）
**复校日期**：2026-11-11
**复校对象目录**：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/`
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-es/`
**复校对象**：core D-2 fix 后重扩散的新版全量（SOP §8.4），重扩散前为 proof2 (a) 定稿版

## 结论：(a) 零缺陷，可定稿

全量重校一整轮零问题。D-2 回归逐项独立重测全部通过；150 题三源逐题手验、8 页逐页目视、事实/日期/算术重算、8 金句逐字核对、全部机械门独立重跑，全部通过，无新缺陷。

## 0. SHA 核对（开工前，三件与任务给定一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-ES.pdf` | 14,033,619 B | `6c299214601b4936dc5329cc72627919fe3b27b90f742298a2eae8cb03554769` |
| 网页 PDF `La-Lucerna-VOL4-ES-web.pdf` | 1,291,397 B | `c194c3421415c75ed089ced802aae069d6bbd6c3de10c9a4e694cac58c447862` |
| 文本导出 `2026-w47-it-es.text.md` | 56,193 B（1317 行） | `4fd5647e2b7a13812b384963607bd67eda2c2c4fe6bd197b9b08bc08eee21643` |

探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29b…`，RC=0）；goals-side scratch 真实写文件成功；磁盘无配额压力。`TMPDIR=<scratch>/tmp` 全程，未写 /tmp。`PYTHONDONTWRITEBYTECODE=1` 全程。收工重验：三 SHA 与开工值一致；16 个 SVG sha256 与开工前逐字节一致，生产零写入。

## 1. 阅读范围

- SOP.md §1.1、§7、§8、§9、附则一/二/四全文；repo `AGENTS.md`；本版 `WEEKLY-KIT.md` 全文；重扩散报告 `scratch-refanout-it2/FANOUT-REPORT-it2.md`（只作背景，不借用其结论）；proof2 笔记 `scratch-proof2-it-es1/PROOF-NOTE.md`（只作缺陷线索，逐项重测）；D-2 修复记录 `scratch-fix-core-it-d2/FIX-LOG.md`。
- `.text.md` 逐行读完（1317 行，1–1317）。
- 印刷 PDF 8 页逐页目视（200 dpi 渲染，`render/p1.png`…`p8.png`）；网页 PDF P1/P8 渲染目视抽查（`render/web-p1.png`、`web-p8.png`），与印刷版视觉一致、无豆腐块。
- 300 dpi 裁切：P1 顶栏右缘（`render/crop-p1-band-right.png`）；200 dpi 裁切：P7 LETTERE 盒底（`render/crop-p7-lettere-below.png`）；4 处奶油盒盒底像素扫描（`pixel_boxes.py`）。

## 2. 回归 A——D-2 修正逐项独立重测（全部通过，详见 GATE-LOG §1）

- 新串 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` 与 `Il verbo è leggere, regolare al futuro: leggerò.` 在 text.md:775/:777、content7.py:17/:18、p7 SVG、印/网 PDF P7 文字层**各就其位、各 1×**。
- 旧串 `Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在该版 live 文件（content*.py、8 SVG、text.md、两 PDF 全文文字层）**均为 0**。
- 与重扩散前生产版 diff **只许 P7 变化**：text.md 恰 775/777 两行、−21 B（56,214→56,193）；content diff 仅 content7.py 17–18 行；SVG p1–p6/p8 与 cards p1–p6/p8 逐字节一致、仅 p7 不同；两 PDF 因 P7 重建而变。
- p7 文本多重集 diff 仅限 D-2 碎片（旧 8 节点 → 新 3 节点）；位置上 A2 段少一行、Q101–104 整块上移 32.68 px，文本一字未动。

## 3. 回归 B——P7 教学段语义逐句事实核查（D-2 教训：读教学句本身）

- L17 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`——正确：assaggiare（-giare 去 i）、guardare 均为规则 -are 动词未来时；形式拼写正确。
- L18 `Il verbo è leggere, regolare al futuro: leggerò.`——正确：leggere 为规则 -ere 动词，leggerò 恰为规则构形；其不规则处在远过去时（lessi）与过去分词（letto），不在未来时。
- 公开依据（本轮独立检索）：LibreTexts《Indicativo futuro》不规则词干表列 andare → andr-、以 leggere 作规则 -ere 例；FlexiClasses 列 andare → andrò 为不规则未来时；dante-learning 列 andare 入 vowel-drop 组（andrò，非 *anderò*）。
- L17 首句 `andremo a Cremona` 与桥句 `andremo、assaggeremo、guarderemo、leggeremo。` 未作规则性断言，指涉不悬空。**教学句语义正确。**

## 4. 150 题三源逐题手验（全文 1317 行逐行读完；机械三源比对见 GATE-LOG §12）

- 题号连续 1–150（141 条单行题干 + 25–28 / 52–55 / 141–144 三组组题），无缺号、无重号；分布 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；分级 A2 47 / B1 70 / B2 33，与 KIT 一致。
- 键值逐组人工核对（例）：匹配题 P2 25→c、26→b、27→d、28→a；P4 52→d、53→b、54→c、55→a；P8 141→d、142→c、143→b、144→a——均与渲染页定义栏字母及 P8 RISPOSTE 一致。Q56 più / Q57 meno / Q58 più bella / Q59 meglio / Q64 ha preso；Q82 Falso 正确（BookCity 开幕周一 23 日，预展 22 日）；Q93–96、109–112 虚拟式正确（piova / nevichi / controllino / sia；leggano；Q112 so che + indicativo torna）；Q137–140 双向翻译键正确（137/138/139 西语重定向键，140 意语键 `Ogni cifra deve essere chiara`）。
- 意大利语正文无拼写/重音/性数/变位/标点错误；西班牙语讲解层无拼写/语法错误；术语一致（manovra / deficit / copertura / scaglione 等贯穿 P4/P6/P7/P8）。
- proof1 D1（`翻譯` 标签）复测：text.md:969/971/973/975 为 `[A2 · Traducir]` / `[B1 · Traducir]` ×2 / `[B2 · Traducir]`，全文件 grep「翻譯」/「翻译」= 0，CJK 字符 0。**已修复，无残留。**
- Q125 与 P3 Q33 同一事实、选项顺序不同（125：A.22 nov · B.8 nov · C.6 dic，key C；33：A.22 nov · B.6 dic · C.8 nov，key B），键值均指向 12 月 6 日，一致。
- P8 写作范文实测 **99 词**（text.md:1007 行，`len(split())=99`），在 80–100 词题面要求内。

## 5. 事实核对——全部属实（逐项重算；Torrone 本轮独立检索核实，其余与 proof2 所引来源一致）

- **意甲第 11 轮（11 月 6–8 日）**：10 场比分内部一致（Venezia–Udinese 2–1、Torino–Lecce 1–1、Cagliari–Frosinone 1–0、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2）；总进球 3+1+2+3+3+2+3+1+2+4 = **24** ✓；积分 Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Fiorentina 9、Udinese 5 垫底；Roma 最佳攻击 31 球；日程 VEN 6.11 / SAB 7.11 / DOM 8.11 与星期一致（2026-11-06 周五、07 周六、08 周日，`date` 实测）。
- **意甲第 12 轮预告**：Lazio–Lecce 周六 21 日、Atalanta–Inter 周日 22 日 20:45 贝加莫、Monza–Fiorentina 周一 23 日 20:45；与 P1/P4 一致。
- **Festa del Torrone（克雷莫纳）——本轮独立检索核实**（festadeltorrone.com 官网 + lamescolanza / gustoh24 / lentium / foodtour / petitchef / chebello，2026-11-11）：第 29 届，11 月 7–22 日，16 天，三周末（7–8、14–15、21–22），主题《Il Confine》；Torrone d'Oro 授予 Davide Simonetta（周日 22 日 11:00，Palatorrone）；游行 >150 figuranti 16:00、Sforza–Visconti 婚礼重演 17:00、旗手/喷火至 18:00、闭幕《Il torrone va in brodo》18:00——与正文逐项一致；传说婚礼 1441 年 10 月 25 日（`date`：周一）。
- **Eurochocolate（佩鲁贾）**：第 32 届，11 月 13–22 日，主题《Fate dolci》，嘉宾大区卡拉布里亚；Iginio Massari 周日 22 日闭幕。
- **Nitto ATP Finals（都灵）**：11 月 15–22 日，Inalpi Arena；Zverev 世界第一；Alcaraz 夺冠热门；Cobolli 首秀；上届冠军 Sinner 因膝伤缺席（文中明示未参赛）。
- **BookCity Milano**：第 15 届、11 月 23–29 日（7 天）、1,360 活动 / 2,487 主角 / 1,164 书 / 443 场地、主题《Il senno sulla Luna》（阿里奥斯托《Orlando furioso》）、开幕周一 23 日 20:00 Teatro Dal Verme、主宾 Colson Whitehead（两次普利策）、预展周日 22 日 16:00 Fondazione Luigi Rovati、主宾 Edmund de Waal。
- **Torino Film Festival**：第 44 届，周二 11 月 24 日–周三 12 月 2 日，9 天（24–30 日 7 天 + 12 月 1–2 日 2 天）；Filmmaker Festival Milano 11 月 14–22 日，周日 22 日闭幕；Alba 白松露集市至 12 月 6 日（周日）。
- **Manovra 2027**：DPB 10 月 15 日（周四）送交布鲁塞尔；2027 年增长 +0,8%、赤字 3,4%；法案约 €260 亿，10 月 28 日（周三）部长会议通过，编号 C. 3174-bis；听证 11 月 9–12 日（周一–周四，4 天），周四 12 日由 Giorgetti 部长收尾；修正案截止周二 17 日 18:00；Irpef 33% 档上限 €50k→€55k；约 €50 亿来自银行/保险业；最终批准截止 12 月 31 日（周四）。“仍非法律”在 P1、P2、P6 三处明示，P6 另有 «PROPOSTA ≠ LEGGE» 盒。
- **Nations League**：意大利–法国 周四 11 月 12 日、比利时–意大利 周日 11 月 15 日；均在付印之后，正文不印结果、顺延 VOL.5，与刊期 11 月 16 日自洽。
- **其他日期与史实**：Madonna della Salute 11 月 21 日（周六），1630 年瘟疫还愿、Longhena 圆顶 1631–1687 年；全国树木日 11 月 21 日（首届 Festa dell'albero 1898 年，2013 年第 10 号法律）；圣切契利亚 11 月 22 日（周日）；Torrazzo 意大利最高砖砌钟楼。星期全验（Europe/Rome，`date`）：11 月 16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二；12 月 2 日周三、12 月 6 日周日、12 月 31 日周四；10 月 15 日周四、10 月 28 日周三、11 月 9 日周一、11 月 12 日周四、11 月 15 日周日；11 月 6 日周五、7 日周六、8 日周日；11 月 13 日周五、14 日周六；1441-10-25 周一——与正文全部一致。
- **内部一致性**：P6 练习图算术 13−11=2（Q85）、6+7=13（Q86）正确；P2“settimana scorsa”与 P4“si sono giocate prima di questa edizione”自洽；P8 Q125 与 P3 Q33 同一事实一致（见 §4）。
- **8 句 P7 金句在 `.text.md` 中各出现恰好 2 次**（正文 + P7，程序计数）：`La Lazio resta in vetta`、`ventiquattro gol in dieci partite`、`il ponte votivo sul Canal Grande`、`oltre centocinquanta figuranti in costumi rinascimentali`、`la squadra di Gattuso è ancora imbattuta dopo 11 giornate`、`sette giorni di libri, ragioni e follie`、`il testo può ancora cambiare`、`approvato dal governo non vuol dire già legge`——逐句与源页正文逐字核对一致（P1/P1/P2/P3/P4/P5/P6/P6，页码引用正确）。
- IN QUESTO NUMERO 全部 7 条（P2–P8）与 FRASI DELLA SETTIMANA 全部 8 条的页码引用与正文一致；LA PAROLA «la vetta» 页码引用（P1、P4）正确。
- Nota 注释词逐页核实均真实出现在本页正文（词形变化计入，如 `imbattuta`、`candele`、`figuranti`、`gironi`、`chiude/chiudono`；机械核查见 GATE-LOG §3 text.md validate 0/0）。
- P7 ERRORI TIPICI 4 条纠错全部正确；LETTERE 栏为标注的编辑示例 + 披露（无虚构读者），承诺顺延 VOL.5。

## 6. 版式几何（逐页目视 + 工具门禁 + 像素裁定）——全部通过

- **occlusion audit**（repo `tools/occlusion_audit.py`，8 个 SVG，自测先行）：**0 flags**。
- **奶油盒扫描**（29 盒）：无真溢出。盒内余量 ≥ +4.5 px；7 处负余量皆 BELOW-WINDOW 假阳性（inside-only 余量 +16.0/+47.7/+22.0×3/+31.2/+90.0）；4 处 desc-clear 负值 200 dpi 像素裁定：P3 E TU 盒底余量 0.84 px、P5 E TU 0.84 px、P7 LA PAROLA 0.48 px、P7 LETTERE 盒下 15 渲染 px 内暗像素 0（+40 px 带内的暗像素为盒下 13.2 px 处的橄榄绿分隔线，裁图目视确认末行完整在盒内）。
- **横向/页边溢出**（PyMuPDF 逐字符扫描交付印 PDF）：0.5 pt 容差下 8 页超页边字符 0；无字符超页底；无非页脚文本跨越 1977 pt 版心底边（0 处）。
- **盒标题 STRADDLE 判定**：P7 全部 14 个标题节点与备份旧版逐字逐坐标一致；p1–p6/p8 SVG 与备份逐字节一致→标题无任何变化；occlusion BOXTITLE 类 0 flags；P6 图表盒标题画于盒上横条、渲染目视完整。**0 缺陷**（无字形被裁、无墨水重叠、无备份差异）。
- **P8 最小字号实测**（PyMuPDF 渲染 pt）：**9.75 pt**，恰为 SOP §1.1 下限；P1–P5/P7 最小 11.62 pt，P6 最小 12.75 pt；网页 PDF 各页字号与印刷版一致。
- **孤儿扫描**（按实际 4 栏流重算；旧 3 栏脚本报“40 跨栏断裂”为分组伪影）：RISPOSTE col1 1–37、col2 38–75、col3 76–112、col4 113–150，各栏连续、栏首均为新题号、栏末题 37/75/112/150 均在本栏内结束；练习 col1 113–124、col2 125–134、col3 135–146、col4 147–150；5 处栏内大间距逐行裁定皆为栏界伪影（RISPOSTE 标题/页脚行/节标题/范文后配图说明）。**跨栏断裂题 0；栏首续行 0。**
- **目视**：8 页印刷版逐页检查，无溢出、重叠、页脚侵入、无豆腐块；11 月 16 日周一刊期、VOL.4 ×9（grep 核实）、VOL.5 仅 3 处（P2 E TU 括号、P7 LETTERE 披露、P7 下期预告，均合法）；无全页外框（0 个全页矩形框）；配图 5 幅（P1 体育场、P2 Canaletto、P3 Torrazzo、P5 Corot、P8 Vermeer）均有图注与来源；P6 图表两行数对齐、条形长度与数值成比例（Torino 5° 最短、Napoli 13° 最长）；P7 两条 D-2 新句渲染干净，Q101–104 完好。
- **标题数实测**（“56 titles”为幻数，本版实测与 proof2 一致）：奶油盒 `#f0eee5` 共 29 个，其中带标题 23 个、Nota 注释盒（无标题）5 个、P6 图表盒标题画于盒上横条 1 个；全大写文本节点共 116 个。“56”与任一可复现的计数均不对应。

## 7. 门禁全套——全部通过（独立重跑，见 GATE-LOG.md）

- gates.py es **20/20 ALL PASS**（初版 4 FAIL 为本人改写脚本路径的错误，已修正重跑，与内容无关）。
- freeze 核心 baseline 8/8（`--core-svg` 指 core-it 自身 svg，build-copy 核实为 core-it）；freeze 本版 baseline 8/8；重建印 PDF 与交付**逐字节相同**（sha256 `6c299214…`）。
- freeze diff 0 未解释；strict-CJK 新增仅 8 × U+3000（页脚分隔符，SOP 豁免）。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs core CLEAN，keydiff 实测 **[137, 138, 139]**（预期内的重定向翻译键）。
- 印/网文字层字符多重集一致（各 7,998 词；`pdftotext` 无 -layout 各 46,032 B，与 KIT §7 相符）；web PDF 1,291,397 B < 7 MB；P8 最小字号 13.0 SVG px = 9.75 pt；§1.1 扫描通过（纸色 #fbfaf6、禁色 0、VOL.4 ×9、VOL.5 仅 3 合法节点、徽章色齐全、无双层外框）；text.md validate 0/0；150 键与注释与核心一致（137–140 重定向 + 写作题除外）；KIT §7/§12 三 SHA 与盘上一致。
- 残留语言扫描：SVG 非拉丁字符仅 U+3000（125×，家具）、全角冒号 ：（7×，冻结的核心动词范式注释）、`<title>Lucerna 三色蛾</title>`（logo 元数据，不可见，core 亦有）。SVG 中无中文词句残留。
- ABSTRACT.txt：西语单行，无 ASCII 双引号，含 La Lucerna、italiano、A2–B2、150 ejercicios——符合 SOP §9。

## 8. KIT §10 披露的短板——已核实属实，非缺陷

无真实读者来信（编辑示例 + 披露，承诺顺延 VOL.5）；Nations League 结果顺延 VOL.5；P8 9.75 pt；P3/P5 页中空白（核心版式）；P1 头条无首字下沉；P1 顶栏自 x=0.0 左缘起（A 像素核实完整，见 O2）；“·”保留在选项串/词汇表内。

## 9. 缺陷清单

无。本轮零缺陷。

## 10. 观察（非缺陷，记录备查）

- **O1——4 处小节标题位于栏底**（proof2 O1，复核属实）：P2 `D LE PAROLE DI VENEZIA`（P2 SVG y=2401，col3）、P3 `B LE PAROLE DEL TESTO`（y=2489，col1）、P4 `B LE PAROLE`（y=2391，col1）、P5 `B LE PAROLE DEL TESTO`（y=2431，col1）的全部题项在下一栏。位置模式与 core-it 相同，属冻结核心版式且核心 re-proof (a) 已接受；keep-with-next 改进属于核心层改动，不应由 fan-out 版修。渲染证据：`render/p2.png`、`p3.png`、`p4.png`、`p5.png`。
- **O2——P1 顶栏 VENEZIA 末字母 A**（proof2 O2，复核属实）：本轮 300 dpi 裁图 + 像素测量：最右墨 x=1462.32 pt（页宽 1462.5），字形完整、右腿 serif 恰触页边（`render/crop-p1-band-right.png`）；KIT §10 已披露。advance-box 超页边 0.08 pt 属取整伪影。
- **O3——“56 titles”无实测依据**（proof2 O3，复核属实）：见 §6 标题数实测。带标题奶油盒 23 个（+ P6 图表盒上横条标题 1 个）；若指全部标题类节点，需先定义口径再计数。
- **O4——fanout 报告“P7 andare 出现一次”少计一处**（本轮新发现，非缺陷）：P7 文字层 `andare` 实为 2 处——Q101 题干 `(andare)` 与 ERRORI TIPICI `Andare vuole essere, non avere. andare lleva essere como auxiliar.`。后者是正确的助动词教学句，与 D-2 旧串无关；两处均合法。仅更正 fanout 报告的计数口径。
- **O5——P7 A2 栏重排后栏底留白变大**（本轮新发现，非缺陷）：D-2 改动使 A2 段少一行，Q101–104 整块上移 32.68 px（101. y 751.75→719.07；104. 末行 y 1117.38→1084.70），栏 1 在 FRASI 通栏上方留出更大空白。这是已批准的最小改法的直接后果，B1/B2 栏与 col3 盒未动；渲染证据 `render/p7.png`。
- **O6——KIT §12 行 94 措辞不精确**（本轮新发现，非内容缺陷）：“p7 SVG 文本节点 diff 仅限 2 条 D-2 句”按文本内容成立（多重集 diff 仅 D-2 碎片），但位置上 Q101–104 同文本节点上移 32.68 px。建议后轮 KIT 写清“文本内容仅限 D-2 两句；A2 练习块随段落缩短整体上移”。
- **O7——P7 LA PAROLA 盒底余量实测 0.48 px**（proof2 报 0.96 px）：相差 1 渲染 px（200 dpi 下 1 px = 0.48 svg px），墨迹仍在盒内、盒下 15 渲染 px 内暗像素 0。非缺陷，属渲染取整差异。

## 11. 未覆盖项

- 网站封面块（cover.json / `.html`）不在本版交付物内，不属本次复校对象（SOP §8.6 / lint 规则 14 由封面生产环节负责）。
- `.md` frontmatter（`issues/` 层）尚未生成，由 `insert.py` 入仓时生成并经 lint 规则 12/13 核对，不属本次复校对象。

## 12. 复校过程记录

- 未直接跑 run.py / render.py：其 OUT/BASE 为硬编码生产绝对路径（proof2 §11 同一教训）；重建验证只用 `tools/freeze.py baseline`（自带 repoint 机制）+ freeze build-copy 重建 PDF。本轮生产目录零写入（收工 SVG 重哈希与开工前逐字节一致）。
- gates.py 首次运行 4 FAIL 为本人改写脚本路径的错误（`$S/es/` 目录未建；`validate_edition_textmd.py` 路径被 sed 写成双重前缀），修正后重跑 20/20；详见 GATE-LOG §3/§13。
- PDF 文字层新串计数：直接计数为 0 是提取形态问题（PyMuPDF 行尾换行 + 箭头粘词），空白+箭头归一化后新串各 1×、旧串 0；详见 GATE-LOG §1。
