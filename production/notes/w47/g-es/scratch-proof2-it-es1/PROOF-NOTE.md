# PROOF-NOTE — 2026-W47 it-es（意大利目标语 / 西班牙语讲解层）

**复校员**：proof2（独立复校，只读生产：不改生产文件、不 commit、不 push、不重渲染交付的 web PDF）
**复校日期**：2026-11-11
**复校对象目录**：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/`
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-es1/`
**复校对象**：重扩散新版（核心 fix3 commit `36bdec2e`，re-proof (a) 零问题）

## 结论：(a) 零缺陷，可定稿

全量重校（SOP §8.4）一整轮零问题。proof1 唯一缺陷 D1（`.text.md` 翻译题型标签残留中文「翻譯」）已在本版机制修复并逐项实测确认；其余所有门禁与人工精读全部通过，无新缺陷。

## 0. SHA 核对（开工前，三件与任务给定一致；KIT §7/§11 亦一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-ES.pdf` | 14,033,641 B | `8b7547d315a50de4858d6971483f79951c2d497ef28e4f71dc66942bc405411b` |
| 网页 PDF `La-Lucerna-VOL4-ES-web.pdf` | 1,291,428 B | `efc1404b8797a8b133fdafe911c1886a9a2be24158a2e49a4dcaeb657cdb9266` |
| 文本导出 `2026-w47-it-es.text.md` | 56,214 B（1317 行） | `64a8ac2fce4e7063c7bebfcbb5b6cde2f8fe1fbde4f265a510e6abf83d007031` |

探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功；goals-side scratch 真实写文件成功；磁盘 57G 可用。`TMPDIR=<scratch>/tmp` 全程，未写 /tmp。`PYTHONDONTWRITEBYTECODE=1` 全程。

## 1. 阅读范围

- SOP.md §1.1、§7、§8、§9、附则一/二/四全文；repo `AGENTS.md`；本版 `WEEKLY-KIT.md` 全文；重扩散报告 `scratch-refanout-it/FANOUT-REPORT-it.md`（只作背景，不借用其结论）；proof1 笔记 `scratch-proof-it-es1/PROOF-NOTE.md`（只作缺陷线索，逐项重测）。
- `.text.md` 逐行读完（1317 行，1–1317）。
- 印刷 PDF 8 页逐页目视（150 dpi 渲染，`$S/png/full-1.png`…`full-8.png`）；网页 PDF P1/P8 渲染目视抽查（`$S/png/web-1.png`、`web-8.png`），与印刷版视觉一致、无豆腐块。
- 300 dpi 裁切：P1 顶栏右缘（VENEZIA 末字母 A，`crop-p1-band-right.png`）；200 dpi 裁切：P7 LA PAROLA 工具盒盒底（`crop-p7-laparola.png`）；另 4 处奶油盒盒底像素扫描（`pixel_boxes.py`）。

## 2. proof1 D1 复测——已修复（实测）

- `.text.md` 第 969/971/973/975 行（E 节 Q137–140）题型标签现为 `[A2 · Traducir]` / `[B1 · Traducir]` ×2 / `[B2 · Traducir]`，行尾 `[Traducir al español]` / `[Traducir al italiano]` 一致；全文件 grep「翻譯」= 0 处；8 个 SVG grep「翻譯」= 0 处。
- 机制来源：`translations.py`「翻譯」映射 + 导出器生成，与手修备份 4 行逐字节一致的 claim 由 fan-out 报告给出，本轮只验结果：结果一致。

## 3. 事实核对——全部属实（逐项实测，非引 proof1）

- **意甲第 11 轮（11 月 6–8 日）**：10 场比分与公开记录一致（`sportradar`/`thestatsapi`/`italiansoccerseriea` 2026-11-11 实测）：Venezia–Udinese 2–1、Torino–Lecce 1–1、Cagliari–Frosinone 1–0、Parma–Bologna 1–2、Roma–Sassuolo 3–0、Napoli–Lazio 1–1、Genoa–Milan 1–2、Monza–Atalanta 0–1、Inter–Como 2–0、Fiorentina–Juventus 2–2；总进球 3+1+2+3+3+2+3+1+2+4 = 24；积分 Lazio 29、Inter 28、Roma 27、Milan 24、Como 23、Fiorentina 9、Udinese 5 垫底；Roma 最佳攻击 31 球；日程 VEN 6.11 / SAB 7.11 / DOM 8.11 与星期一致（2026-11-06 周五、07 周六、08 周日，`date` 实测）。
- **意甲第 12 轮预告**：Lazio–Lecce 周六 21 日、Atalanta–Inter 周日 22 日 20:45 贝加莫、Monza–Fiorentina 周一 23 日 20:45；与 P1/P4 一致。
- **Festa del Torrone（克雷莫纳）**：第 29 届，11 月 7–22 日，16 天；Torrone d'Oro 授予 Davide Simonetta（周日 22 日 11:00，Palatorrone）；游行 >150 figuranti 16:00、Sforza–Visconti 婚礼重演 17:00、旗手/喷火至 18:00、闭幕《Il torrone va in brodo》18:00；传说婚礼 1441 年 10 月 25 日（`date`：周一）。
- **Eurochocolate（佩鲁贾）**：第 32 届，11 月 13–22 日，主题《Fate dolci》，嘉宾大区卡拉布里亚；Iginio Massari 周日 22 日闭幕。
- **Nitto ATP Finals（都灵）**：11 月 15–22 日，Inalpi Arena；Zverev 世界第一；Alcaraz 夺冠热门；Cobolli 首秀；上届冠军 Sinner 因膝伤缺席（文中明示未参赛）。
- **BookCity Milano**：第 15 届、11 月 23–29 日、1,360 活动 / 2,487 主角 / 1,164 书 / 443 场地、主题《Il senno sulla Luna》（阿里奥斯托《Orlando furioso》）、开幕周一 23 日 20:00 Teatro Dal Verme、主宾 Colson Whitehead（两次普利策）、预展周日 22 日 16:00 Fondazione Luigi Rovati、主宾 Edmund de Waal——以上全部经意媒独立证实（`libreriamo.it`、`radiolombardia.it`、`illibraio.it`、`milano365.it`，2026-11-11 检索）。
- **Torino Film Festival**：第 44 届，周二 11 月 24 日–周三 12 月 2 日，9 天；Filmmaker Festival Milano 11 月 14–22 日，周日 22 日闭幕；Alba 白松露集市至 12 月 6 日（周日）。
- **Manovra 2027**：DPB 10 月 15 日（周四）送交布鲁塞尔；2027 年增长 +0,8%、赤字 3,4%；法案约 €260 亿，10 月 28 日（周三）部长会议通过，编号 C. 3174-bis；听证 11 月 9–12 日（周一–周四），周四 12 日由 Giorgetti 部长收尾；修正案截止周二 17 日 18:00；Irpef 33% 档上限 €50k→€55k；约 €50 亿来自银行/保险业；最终批准截止 12 月 31 日（周四）。“仍非法律”在 P1、P2、P6 三处明示，P6 另有 «PROPOSTA ≠ LEGGE» 盒。
- **Nations League**：意大利–法国 周四 11 月 12 日、比利时–意大利 周日 11 月 15 日；均在付印之后，正文不印结果、顺延 VOL.5，与刊期 11 月 16 日自洽。
- **其他日期与史实**：Madonna della Salute 11 月 21 日（周六），1630 年瘟疫还愿、Longhena 圆顶 1631–1687 年；全国树木日 11 月 21 日（首届 Festa dell'albero 1898 年，2013 年第 10 号法律）；圣切契利亚 11 月 22 日（周日）；Torrazzo 意大利最高砖砌钟楼。星期全验（Europe/Rome，`date`）：11 月 16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二；12 月 2 日周三、12 月 6 日周日、12 月 31 日周四；10 月 15 日周四、10 月 28 日周三、11 月 9 日周一、11 月 12 日周四、11 月 15 日周日——与正文全部一致。
- **内部一致性**：积分增量与比分一致；P6 练习图算术 13−11=2（Q85）、6+7=13（Q86）正确；P2“settimana scorsa”与 P4“si sono giocate prima di questa edizione”自洽；P8 Q125 与 P3 Q33 同一事实、选项顺序不同（125：A.22 nov · B.8 nov · C.6 dic，key C；33：A.22 nov · B.6 dic · C.8 nov，key B），键值均指向 12 月 6 日，一致。
- **P8 写作范文实测 99 词**（`.text.md:1007` 行，`len(split())=99`），在 80–100 词题面要求内。

## 4. 语言（意语正文 + 西语讲解层逐句读完）——无错误

- 意大利语正文无拼写/重音/性数/变位/标点错误；西班牙语讲解层无拼写/语法错误；术语一致（manovra/deficit/copertura/scaglione 等贯穿 P4/P6/P7/P8）。
- 150 题编号连续 1–150（程序核实，无缺号；分组合题 25–28、52–55、141–144 各 4 题齐全）；题量分布与 KIT 一致（P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；A2 47 / B1 70 / B2 33）。
- 键值与题干语义逐组人工核对：匹配题 P2 25→c、26→b、27→d、28→a；P4 52→d、53→b、54→c、55→a；P8 141→d、142→c、143→b、144→a——均与渲染页定义栏字母及 P8 RISPOSTE 一致。Q56 più / Q57 meno / Q58 più bella / Q59 meglio / Q64 ha preso；Q82 Falso 正确（BookCity 开幕周一 23 日，预展 11 月 22 日）；Q93–96、109–112 虚拟式正确（piova/nevichi/controllino/sia; leggano; Q112 so che + indicativo torna）；Q137–140 双向翻译键正确（137/138/139 西语重定向键，140 意语键 `Ogni cifra deve essere chiara`）。
- 8 句 P7 金句在 `.text.md` 中各出现恰好 2 次（正文 + P7，程序计数：`La Lazio resta in vetta`、`ventiquattro gol in dieci partite`、`il ponte votivo sul Canal Grande`、`oltre centocinquanta figuranti in costumi rinascimentali`、`la squadra di Gattuso è ancora imbattuta dopo 11 giornate`、`sette giorni di libri, ragioni e follie`、`il testo può ancora cambiare`、`approvato dal governo non vuol dire già legge` 均为 2×）。
- IN QUESTO NUMERO 全部 7 条（P2–P8）与 FRASI DELLA SETTIMANA 全部 8 条的页码引用与正文一致；LA PAROLA «la vetta» 页码引用（P1、P4）正确。
- Nota 注释词逐页核实均真实出现在本页正文（词形变化计入，如 `imbattuta`、`candele`、`figuranti`、`gironi`、`chiude/chiudono`；机械核查脚本在 GATE-LOG）。
- P7 ERRORI TIPICI 4 条纠错全部正确；LETTERE 栏为标注的编辑示例 + 披露（无虚构读者），承诺顺延 VOL.5。

## 5. 版式几何（逐页目视 + 工具门禁 + 像素裁定）——全部通过

- **occlusion audit**（repo `tools/occlusion_audit.py`，8 个 SVG，自测先行）：**0 flags**。
- **canonical creambox 扫描**（`hidden_files/w47/tools/creambox.py`，29 个奶油盒，`$S/creambox.log`）：无真溢出。全部“盒内”余量 ≥ +4.5px；负余量皆为 BELOW-WINDOW 假阳性（下一栏目标题/行在盒下方，如 P1 “LA PAROLA DELLA SETTIMANA” −24.0、P3 “IL TORRAZZO E IL TORRONE” −37.0、P4 赛果表行带（SAB/DOM 日期组与比分行）、P6 “ESERCIZI…”标题——每处均核对 inside-only 余量为正：+16.0 / +47.7 / +22.0 / +31.2 / +90.0）。
- **desc-clear 负值 4 处像素裁定**（末行含真实下行字母，`pixel_boxes.py`，交付印 PDF 200 dpi 渲染）：P3 E TU `Escribe dos frases y envíalas.`（y，盒底余量实测 0.84px）、P5 E TU `partido? Escribe dos frases y envíalas.`（0.84px）、P7 LA PAROLA `…con 29 puntos.`（p，0.96px）、P7 LETTERE `…pasa al VOL.5.`（p，1.64px，盒下 11.8px 处才是下一栏内容）——盒底下方 15 渲染 px 内暗像素均为 0，墨迹全部在盒内；P7 裁切目视（`crop-p7-laparola.png`）确认末行完整、盒底留有奶油条。其余 desc-clear 负值（P2 LO SAPEVI +5.3/−1.1、E TU +5.0/−1.0；P3 +5.3/−1.2；P4 +4.5/−1.5；P5 +5.3/−1.1）末行无下行字母，属 0.30em 保守 allowance 假阳性。
- **BOXTITLE 真墨迹**：审计 BOXTITLE 类 0 flags（含最宽标题 P6 “LE MINIME DI ESEMPIO　MÍNIMAS DE EJEMPLO (DATI INVENTATI PER L'ESERCIZIO)”——该标题实际画在盒体上方横条内，不在盒内，渲染目视完整）。
- **横向/页边溢出**（PyMuPDF 逐字符扫描交付印 PDF，`geom_scan.py`）：8 页中仅 P1 一字符超页边——顶栏 VENEZIA 末字母 A，bbox x1=1462.58pt（超 0.08pt，属 advance-box 取整伪影）；300 dpi 裁切目视（`crop-p1-band-right.png`）该 A 完整无裁切，右腿 serif 恰触页边（KIT §10 已披露的边界情形，装饰性，非缺陷）。其余 7 页 0 字符超边；无字符超页底；无非页脚文本跨越 1977pt 版心底边（0 处）。
- **P8 最小字号实测**（PyMuPDF 渲染 pt）：**9.75pt**，恰为 SOP §1.1 下限；P1–P5/P7 最小 11.62pt，P6 最小 12.75pt；网页 PDF 各页字号与印刷版一致。
- **孤儿扫描**（定义：答案题跨栏断裂 + 栏首续行）：P8 逐栏核查——3 栏栏首皆为标题/徽章而非上题续行，栏末题（37./75./150.）均在本栏内结束，跨栏断裂题 0；练习小节标题与首题：P6/P7/P8 均同栏；P2 D、P3 B、P4 B、P5 B 四处小节标题位于栏底、全部题项在下一栏——位置模式与 core-it 相同（P2 D 逐坐标相同 y=2401 col3；P3/P4/P5 因西语行较长下移约 30px，但同样位于栏底），属冻结核心版式、非本版引入，见观察 O1。
- **目视**：8 页印刷版逐页检查，无溢出、重叠、页脚侵入、无豆腐块；11 月 16 日周一刊期、VOL.4 ×9（grep 核实）、VOL.5 仅 3 处（P2 E TU 括号、P7 LETTERE 披露、P7 下期预告，均合法）；无全页外框（0 个全页矩形框）；配图 5 幅（P1 体育场、P2 Canaletto、P3 Torrazzo、P5 Corot、P8 Vermeer）均有图注与来源；P6 图表两行数对齐、条形长度与数值成比例（Torino 5° 最短、Napoli 13° 最长）。
- **标题数实测**（“56 titles”为幻数，本版实测）：奶油盒 `#f0eee5` 共 29 个，其中带标题 23 个、Nota 注释盒（无标题）5 个、P6 图表盒标题画于盒上横条 1 个；全大写文本节点共 116 个（含刊头家具、徽章、日期标签、选项行）。“56”与任一可复现的计数均不对应。

## 6. 门禁全套——全部通过（独立重跑，见 GATE-LOG.md）

- run.py RC=0，150 题，0 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE；SVG 重建 8/8 字节一致（freeze baseline）；重渲印 PDF 与交付逐字节相同（sha256 `8b7547d3…`）。
- freeze 核心 baseline 8/8；freeze diff 342 增 / 526 删碎片逐条解释完毕（0 未解释：增量全为西语讲解层/家具/P8 西语注释，减量全为中文核心层；意大利目标语文本零改动）；strict-CJK 新增仅 8 × U+3000（页脚分隔符，SOP 豁免）。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs core CLEAN，keydiff 实测 **[137, 138, 139]**（预期内的重定向翻译键）。
- 印/网文字层字符多重集一致（各 8001 词）；web PDF 1,291,428 B < 7 MB；P8 最小字号 13.0 SVG px = 9.75pt；§1.1 扫描通过（纸色 #fbfaf6、禁色 0、VOL.4 ×9、VOL.5 仅 3 合法节点、徽章色齐全、无双层外框）；text.md validate 0/0；150 键与注释与核心一致（137–140 重定向 + 写作题除外）；KIT 三 SHA 与盘上一致。
- 残留语言扫描：SVG 非拉丁字符仅 U+3000（125×，家具）、全角冒号 ：（7×，冻结的核心动词范式注释 16–20/60–61）、`<title>Lucerna 三色蛾</title>`（logo 元数据，不可见，core 亦有）。SVG 中无中文词句残留。
- ABSTRACT.txt：西语单行，无 ASCII 双引号，含 La Lucerna、italiano、A2–B2、150 ejercicios——符合 SOP §9。

## 7. KIT §10 披露的短板——已核实属实，非缺陷

无真实读者来信（编辑示例 + 披露，承诺顺延 VOL.5）；Nations League 结果顺延 VOL.5；P8 9.75pt；P3/P5 页中空白（核心版式）；P1 头条无首字下沉；P1 顶栏自 x=0.0 左缘起（A 像素核实完整）；“·”保留在选项串/词汇表内。

## 8. 缺陷清单

无。本轮零缺陷。

## 9. 观察（非缺陷，记录备查）

- **O1——4 处小节标题位于栏底**：P2 `D LE PAROLE DI VENEZIA`（P2 SVG y=2401，col3）、P3 `B LE PAROLE DEL TESTO`（y=2489，col1）、P4 `B LE PAROLE`（y=2391，col1）、P5 `B LE PAROLE DEL TESTO`（y=2431，col1）的全部题项在下一栏。位置模式与 core-it 相同（P2 D 逐坐标相同；P3/P4/P5 在 core 中分别为 y=2459/2361/2401，因西语行较长本版下移约 30px，同样位于栏底），属冻结核心版式且核心 re-proof (a) 已接受；keep-with-next 改进属于核心层改动，不应由 fan-out 版修。渲染证据：`png/full-2.png`、`full-3.png`、`full-4.png`、`full-5.png`。
- **O2——P1 顶栏 VENEZIA 末字母 A**：advance-box 超页边 0.08pt，但 300 dpi 渲染像素核实字形完整、右腿 serif 恰触页边（`crop-p1-band-right.png`）；KIT §10 已披露。注意 KIT 写的“右缘 ≈1881”数字不准，实际墨迹右缘 ≈1950 SVG px（与 proof1 的观察一致）。
- **O3——“56 titles”无实测依据**：见 §5 标题数实测。本版带标题奶油盒 23 个（+ P6 图表盒上横条标题 1 个）；若指全部标题类节点，需先定义口径再计数。

## 10. 未覆盖项

- 网站封面块（cover.json / `.html`）不在本版交付物内，不属本次 proof2 对象（SOP §8.6 / lint 规则 14 由封面生产环节负责）。
- `.md` frontmatter（`issues/` 层）尚未生成，由 `insert.py` 入仓时生成并经 lint 规则 12/13 核对，不属本次 proof2 对象。

## 11. 复校过程事故记录（已修复，内容零影响）

- **经过**：本轮为抓 run.py 日志，在 `$S/run-copy/`（`cp -a` 的版目录副本）里直接跑了 `run.py`，未先重定向写盘目标。事后核查发现 `content12.py:6` 的 `OUT` 为字面量 `~/workspace/weekly-git/production/2026-w47/2026-w47-it-es/svg`（各 content 文件同款写法），该次运行把 8 个交付 SVG 在原路径重写了一遍（mtime 变为 20:19:33–20:20:07，p1→p8 顺序）。
- **影响核实**：内容零变化——重写后 8 个 SVG 的 sha256 与 freeze baseline 开工前记录的“before”哈希逐字节一致（`6f9e1030…/783afdc2…/97e25dc1…/c4de3901…/21bc0fa5…/4c2504d6…/d61e44cb…/a51ed0f2…`）；印 PDF / 网 PDF / `.text.md` 的 SHA 与任务给定值仍一致（其 mtime 未动，12:18/12:19）；`freeze baseline` 的运行前后重哈希亦证实 SVG 未变。
- **修复**：已用 `cp -a` 保留的原始 mtime（12:15:21–12:15:53）将 8 个 SVG 的 mtime 复原，并再次验证 SHA 不变。生产目录现为字节 + mtime 均与接手时一致的状态。
- **教训**：`run.py` 不得在裸副本里直接跑——必须走 `tools/freeze.py baseline`（其 repoint 机制会改写字面量 OUT 路径，本轮 freeze 运行即正确分流、未写生产）；或先手工重定向 `content*.py` 的 OUT 再跑。下次 proof 须先读 `content*.py:6` 的 OUT 定义再动手。
