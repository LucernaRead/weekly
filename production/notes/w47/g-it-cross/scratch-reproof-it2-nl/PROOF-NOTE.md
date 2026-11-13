# PROOF-NOTE — 2026-W47 it-nl 独立复校（重扩散 2 后全量重校，SOP §8.4）

**结论：(a) 零缺陷可定稿。** 本轮为 core D-2 fix 后重扩散新版的全量独立复校（与重扩散员不同人），零问题；全部 20 项机械门禁独立重跑全绿，150 题三源逐题一致，8 页逐页 200 dpi 目视干净，D-2 回归项逐项独立重测全过，事实逐项经公开来源重核。

- 版：`2026-w47-it-nl`（目标语 it 意大利语 × 荷兰语读者，VOL.4，重扩散 2 新版，核心 it D-2 定稿）
- 印 PDF：14,034,396 B，SHA-256 `a7edbb18d6cde81c3d9454d636ee4412c7f555c2aabc20665fa08c059d2a8a5e`
- 网 PDF：1,291,725 B，SHA-256 `d57398427d4dc493ea5104b3ab86343d83a5edd9e83093d3335baff4fb66fbb7`
- text.md：55,488 B，1,317 行，SHA-256 `b13ef7a7abe07928207eedc182106368ac653d8a8fad49af2adf184a2c94906e`
- 三 SHA + 三字节数与任务值逐字节一致后才开工；收尾复核三 SHA 仍一致，生产区未改动（本轮只读生产，未 commit、未 push、未改任何生产文件；`git status` 的 core-it 两处 M 与版目录 untracked 均为 D-2 fix / 重扩散前既有状态，见 §13）。
- 复校员工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-nl/`；门禁详见同目录 `GATE-LOG.md` 及 `logs/`。

## 1. 开工探针与 SHA 盘核

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件通过；TMPDIR 全程指向自有 scratch 下 `tmp/`，未写系统 /tmp。
- 解释器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`PYTHONDONTWRITEBYTECODE=1`；重建验证只用自有 scratch build-copy（OUT/BASE 已重定向并 grep 核对无生产路径残留），未直接跑任何生产 `run.py` / `render.py`。
- 三 SHA 与任务值逐字节一致；重扩散前生产三 SHA（`scratch-refanout-it2/shas-pre.txt`）为印 `2091448c…` / 网 `039ee0bb…` / 文 `0a044d4b…`，与任务给出的历史值一致。

## 2. D-2 回归项 A（逐项独立重测，全部通过）

| # | 检查 | 实测 |
|---|---|---|
| A1 | text.md:775 新串 | `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` 在位（:775 逐字） |
| A2 | text.md:777 新串 | `Il verbo è leggere, regolare al futuro: leggerò.` 在位（:777 逐字） |
| A3 | 旧串 text.md | `Le forme sono regolari: andare` 0 处；`irregolare al futuro: leggerò` 0 处（grep -c） |
| A4 | 旧串 content7.py | 两旧串各 0 处；:17/:18 为两条新串（逐字） |
| A5 | 旧串 p7 SVG | 两旧串各 0 处；新句跨换行节点在位（节点 7/8/11/16 拼接核实，`assaggiare → assaggerò` 拼接成立；`leggere, regolare al futuro: leggerò.` 整节点在位） |
| A6 | 印 PDF P7 文字层 | 新串 L17 ×1、L18 ×1（空白归一化 + 箭头归一化后计数，PyMuPDF 第 7 页）；旧串各 0 |
| A7 | 网 PDF P7 文字层 | 同印：新串各 ×1，旧串各 0 |
| A8 | 与重扩散前备份 diff | text.md 恰两行改动（:775/:777，`diff` 仅两处 replace）；SVG 仅 p7 不同、其余 7 页逐字节一致；cards 仅 p7 不同、其余 7 张逐字节一致；content*.py 仅 content7.py :17/:18 两行；text.md 55,509 → 55,488 B，恰 **−21**；两 PDF 因 P7 重建而变 |
| A9 | P7 的 `andare` 残留 | PDF P7 上 `andare` 出现 2 次，皆为合法处——Q101 题干 `(andare)` 与 P7 讲解注 `andare met essere als hulpwerkwoord`；SVG 同为此 2 处；与 D-2 旧串无关 |

- 注：PDF 文字层把 `→` 粘到邻词（`→assaggerò,`、`guardare→`）且句内有换行，故按 `\s*→\s*`→`→` 再 `\s+`→空格归一化后计数；此为检查方法，非内容问题。

## 3. D-2 回归项 B（P7 教学段语义逐句事实核查）

- L17 `Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`——**正确**：assaggiare、guardare 均为规则 -are 动词，未来时 assaggerò / guarderò 恰为规则构形；andare 已不在规则例之列。
- L18 `Il verbo è leggere, regolare al futuro: leggerò.`——**正确**：leggere 未来时规则（不定式去尾 -e + -ò = leggerò）；leggere 的不规则处只在远过去时 io lessi 与过去分词 letto，不在未来时。
- 互换已纠正：andare（andrò，元音脱落型不规则词干 andr-）不再被称规则；leggere 不再被称不规则。动词形式拼写全对（andrò 已随被删的 andare 例一并消失，系定稿最小改法；andremo / assaggeremo / guarderemo / leggeremo 均在原位，桥接句未动）。
- P7 其余教学句重读无误：B1 passato prossimo（essere 参与词配合 è partito / è finita；avere 不变 abbiamo visto / hanno comprato）✓；B2 congiuntivo（piova / nevichi / leggano；so che / scrivono che 后接直陈式 torna）✓。

## 4. 门禁汇总（独立重跑，详见 GATE-LOG.md）

20/20 PASS，RC=0（`logs/gates-reproof.log`；gates 逻辑复用 proof2 `gates-proof2.py` 的拷本，输出写进本 scratch，结论为本次实测）：

| 门 | 实测 |
|---|---|
| occlusion 几何遮挡审计 | 0 flags（工具先过合成阳性对照自检） |
| p8 extract | 150/150 |
| p8 compare vs core-it | CLEAN，keydiff **[137, 138, 139]**（见 §6） |
| freeze diff P1–P7 | 0 未解释片段（added/removed 皆由 translations.py 值/键、NOTE/gloss 复合、"(Pagina N)" 复合或家具解释） |
| freeze strict-cjk | 仅 U+3000 ×8（SOP §1.1 家具分隔符，豁免），其余新增 CJK 为 0 |
| 印/网文字层 | 词多重集一致，7,885 词（修前 7,888，恰 −3 词：删去的 `andare`、`→`、`andrò,`）；逐页比对 8/8：字符与词数逐页全等（见 GATE-LOG §C） |
| 网 PDF < 7MB | 1,291,725 B |
| 印 PDF | 14,034,396 B，8 页，1462.5×2025 pt |
| P8 最小字号 | SVG 最小 13.0 px；PyMuPDF 实测印 PDF P8 最小 **9.75 pt**（SOP §1.1 下限，网 PDF 同为 9.75 pt；字号谱 9.75 pt ×180、10.5 ×8、11.62 ×67……） |
| §1.1 | 纸色 #fbfaf6；无金/红褐/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（下期预告头、LETTERE 披露、P2 交叉引用）；徽章色 A2/B1/B2 齐；全页 rect 0（无双线外框）；字体 Newsreader 963 节点 / Noto Sans CJK SC 643 / Noto Serif CJK SC 37（仅 U+3000 分隔）/ UnifrakturMaguntia 1 |
| text.md validate | forward-miss 0 / reverse-miss 0 |
| 150-key audit vs core text.md | 150/150（137–139 重定向、写作题除外）；notes 与 translations.py 一致（137–140 + 写作题除外），table_gaps 0 |
| run.py | RC=0，TOTAL 150，A2 47 / B1 70 / B2 33，页分布 10/18/18/18/18/18/12/38，范文 99 词，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（`logs/run-rebuild.log`） |

## 5. 复现（重建 SVG 8/8 与重渲印 PDF 逐字节相同）

- `freeze.py baseline`（核心版，`--core-svg` 指核心 `core-it/svg`，build-copy 核实确为核心版——含核心 `2026-w47-it-zh-cn.text.md`，SHA `9eb9ee06…`，与 FIX-LOG 定稿值一致，及核心两 PDF）：**8/8 字节一致**，RC=0（`logs/freeze-baseline-core.log`）；核心 p7 为 D-2 定稿 `a7e6afa4…`；发运核心 SVG 运行前后重哈希无变化。
- 版 build-copy 内 run.py 重跑（OUT 已重定向至 scratch，生产 SVG 未动）：RC=0，SVG 8/8 与交付一致（逐项 sha256 MATCH）；随后 render.py 重渲印 PDF：**14,034,396 B，SHA-256 与交付完全一致**（`a7edbb18…`，`logs/render-rebuild.log`）。
- webpdf.py 重建网 PDF：1,291,725 B（与交付**同字节数**），SHA 不同；文字层 `pdftotext` 逐字节一致（110,119 text bytes，`cmp` 通过）。差异为 fontTools 子集字体的字节序不确定性（与 proof2 同类观察；本次重建字节数恰与交付相等，内容等价），记观察（§11-1），不计缺陷。

## 6. 全文通读（1317 行）与 150 题三源手验

- text.md 1–1317 行逐行读完；登记（run.py REGISTRY，`logs/registry.json`）vs text.md 题面 vs P8 印出键三源逐题核对：编号 1–150 连续无缺重；每题题型/级别/键/注三源一致——REG vs 题面键+注 0 差异（1–149，含 12 道配对题的分组格式；Q150 写作题键为开放题标记）；REG vs Risposte 键+注 0 差异；REG vs P8 印出键 0 差异（150/150，Q150 为 ✓ 标记）。
- 配对题选项序逐版核对：Q25–28（a=piantare、b=ponte votivo、c=salute、d=candela；键 c/b/d/a ✓）；Q52–55（a=debutto、b=imbattuto、c=girone、d=vetta；键 d/b/c/a ✓）；Q141–144（a=scaglione、b=copertura、c=deficit、d=manovra；键 d/c/b/a ✓）。
- keydiff [137, 138, 139]：实测与预期一致。P8 印出键 137/138/139 为荷兰语句子（"Voor de Madonna della Salute steken mensen de geloftebrug over." / "Zondagavond speelt Atalanta tegen Inter." / "Zaterdag speelt Lazio thuis tegen Lecce."），与核心（中文读者句）不同是**正确行为**——E 节 137–139 为"译成读者语"题，键随读者语重定向；Q140 的键在核心与本版都是意大利语 "Ogni cifra deve essere chiara."，无差异是正确行为（Q140 为"译成意大利语"题，源句为荷兰语）。
- E 节标签为 `Vertalen`（`content8.py:69/71/73/75`，text.md L969/971/973/975），"Translate" 全版 0 次；无英文源键。
- 算术逐项重算：MD11 10 场进球 3+1+2+3+3+2+3+1+2+4 = **24** ✓（"ventiquattro gol in dieci partite"）；Q85 13−11=**2** ✓；Q86 6+7=**13** ✓；P6 例图 Torino 5° < Milano 6° < Bologna 7° < Roma 11° < Napoli 13°，柱长单调 ✓；Torrone 11月7–22日 = 16 天、3 个周末（7–8、14–15、21–22）✓；TFF 11月24日–12月2日 = 9 天 ✓；范文实测 **99 词** ✓（80–100 词要求）；Q58 "più bella"、Q59 "meglio"、Q93–96/109–111 虚拟式（piova/nevichi/controllino/sia/leggano）、Q77 "ci sarà"、Q108 "è finita" 等语法键全对。
- 日期/星期（`date -d`，Europe/Rome）：11月6日周五、7日周六、8日周日（MD11 6–8日 ✓）、9日周一、12日周四、15日周日、16日周一、17日周二、19日周四、20日周五、21日周六、22日周日、23日周一、24日周二、29日周日、12月2日周三、12月6日周日、12月31日周四——文中全部星期表述一致（含 "martedì 17"、"giovedì 12"、"sabato 21"、"domenica 22"、"lunedì 23"）。
- 8 金句逐字核对出处：8/8 在 text.md 中恰好各出现 2 次（正文一次 + P7 FRASI 一次），页码标注与实际页一致（P1/P1/P2/P3/P4/P5/P6/P6）。
- 荷兰语层：全文讲解为荷兰语，未见他语残留；CJK 字符 0；"aantonende wijs" 为荷兰语直陈式标准术语，非错字；ERRORI TIPICI 四条纠正全对。
- 无国际政治内容（禁词 Ucraina/Russia/Putin 全版未出现——grep 核实为 0 次）。

## 7. 事实核实（公开来源，本轮 2026-11-11 独立检索）

- **意甲 MD11（11月6–8日）**：10 场比分与积分榜与多家报道逐项一致（Venezia–Udinese 2–1；Cagliari–Frosinone 1–0；Torino–Lecce 1–1；Parma–Bologna 1–2；Roma–Sassuolo 3–0；Napoli–Lazio 1–1；Genoa–Milan 1–2；Monza–Atalanta 0–1；Inter–Como 2–0；Fiorentina–Juventus 2–2；Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Fiorentina 9 / Udinese 5；罗马最佳攻击 31 球；拉齐奥 11 轮不败；MD12：Atalanta–Inter 周日 22 日 20:45，Monza–Fiorentina 周一 23 日 20:45，Lazio–Lecce 周六 21 日）。Gattuso 为拉齐奥主帅亦经核实。
- **Eurochocolate 2026**：第 32 届、11月13–22日、主题 "Fate Dolci"、Calabria 为首个 Regione Ospite（"Calabria straordinaria"，bergamotto/cedro/peperoncino/fichi）、Iginio Massari 周日 22 日闭幕嘉宾、"I tesori della Calabria Straordinaria" 周五 20 日 18.15——官方 Press Area 及多家来源一致。
- **Festa del Torrone 2026**：第 29 届、11月7–22日、16 天、3 个周末、主题 «Il Confine»；Torrone d'Oro 授予 Davide Simonetta（生于 Cremona），周日 22 日 11:00 Palatorrone；历史游行 16:00（150+ figuranti）、Sforza–Visconti 婚礼重演 17:00 Piazza del Comune、旗手与火舞至 18:00、"Il torrone va in brodo" 压轴——与文中时刻逐项一致；1441 年婚礼为当地传说（文中已标 "La leggenda dice"）。
- **BookCity Milano 2026**：第 15 届、11月23–29日、主题 «Il senno sulla Luna»（Ariosto《Orlando furioso》）、1,360 活动 / 2,487 主角 / 1,164 书 / 443 场地；开幕周一 23 日 20:00 Teatro Dal Verme，Colson Whitehead（两届 Pulitzer）；预展周日 22 日 16:00 Fondazione Luigi Rovati，Edmund de Waal（lectio《Come cominciare》）——官方新闻包与多家来源一致。
- **Torino Film Festival 2026**：第 44 届、周二 24 日至 12月2日、9 天（Museo Nazionale del Cinema 官方页一致）。**Filmmaker Festival**：11月14–22 日、周日 22 日闭幕（官方通稿一致）。
- **ATP Finals 2026**：11月15–22日、Torino Inalpi Arena、8 人、两组、半决赛周六 21 日、决赛周日 22 日；Zverev 世界第一，Alcaraz 热门，Cobolli 首秀（意大利唯一单打代表），Sinner 为 2025 冠军（两届卫冕冠军）、因膝伤缺席——逐项核实。
- **Nations League**：意大利–法国 周四 12 日 20:45 圣西罗；比利时–意大利 周日 15 日 20:45 布鲁塞尔（FIGC 官方一致）。
- **Manovra 2027**：DPB 10月13日通过、10月15日送布鲁塞尔；2027 增长 +0,8%、赤字 3,4%（含条款）；CdM 10月28日批准法案，约 26 亿；法案号 **C. 3174-bis**（11月4日删节三条后为 3174-bis）；听证会 11月9–12日（Giorgetti 周四 12 日 16:00 收尾）；修正案截止周二 11月17日 18:00；最终表决须于 12月31日前；IRPEF 第二档 33% 扩至 55,000 欧元（原 50,000）；金融业约 50 亿覆盖（技术报告 5.8 亿口径，文中 "circa 5 miliardi" 已 hedged）——逐项核实。文中三次 "PROPOSTA ≠ LEGGE" 披露与"尚未成为法律"一致。
- 历史/文化：Madonna della Salute 还愿 1630 年（10月22日誓愿）、Longhena 设计、建于 1631–1687 年（1687年11月21日祝圣）；树节 1898 年首办（Baccelli 倡议）、2013 年第 10 号法律定 11月21日为全国树节；Colson Whitehead 两届 Pulitzer——均与公开记录一致。

## 8. 8 页逐页目视（交付印 PDF，200 dpi 渲染，`render/p-1–p-8.png`）

逐页目视：无溢出、无重叠、无压页脚、无豆腐块、无图片缺失；页脚 "Pagina N van 8"（N=1–8）与 "La Lucerna　ITALIAANS WEEKBLAD VOL.4　TEKSTEN IN HET ITALIAANS　UITLEG IN HET NEDERLANDS" 逐页在位；目录页码（P1 IN QUESTO NUMERO）与实际版次一致；P3/P5 中部结构空白为核心既有版式（KIT 已载，非缺陷）；P8 练习区末行 y=870、答案区末行 y=2529（底边 2552，余 23 px），各流末位置均在底边内，无页界 spill、无孤儿行。
- P7 重点：两条 D-2 新句渲染干净（"Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò." / "Il verbo è leggere, regolare al futuro: leggerò."），桥接句与 Q101–112 完好，LA PAROLA 盒标题在盒内，FRASI 8 句与页码标注完好，VOL.5 预告条完好。
- P1 刊头带：ink_box 实测墨左 10.5、右 1873.7（页宽 1950），左余 10.5 px、右余 76.3 px，spacing 11.0 修复在位（`content12.py:18`），无剪裁；与重扩散实测值逐字一致。

## 9. 奶油盒标题（STRADDLE 规则专项，含备份旧版对照）

- 方法：审计同款 PIL 真墨盒（`measure_cream.py`，`logs/cream-measure.log`），对全部 29 个无边框奶油盒（#f0eee5）逐盒实测（标题行 + 盒内全部行，按基线分组聚合拆分 run）；并对重扩散前备份（`scratch-refanout-it2/backup/`）跑同一脚本对照（`logs/cream-measure-backup.log`）。
- **29/29 盒全部在内，无一越右缘**（overhang > +0.5 px 者 0 个）。最紧前三：P1 LA SETTIMANA 盒内行墨右缘 1857.2 vs 盒右 1862.0（余 **4.8 px**）；P7 "LA PAROLA　WOORD VAN DE WEEK" 标题墨右缘 1853.5 vs 盒右 1862.0（余 **8.5 px**）；P1 "LA SETTIMANA IN CIFRE　CIJFERS" 标题余 23.0 px。
- **与备份对照：两份量测日志逐字节相同**——无字形被裁、无墨迹重叠他物、无可见边框被压、无相对旧版的回归。按 STRADDLE 规则（缺陷当且仅当字形被裁 / 墨水与另一元素或可见边框重叠 / 与备份旧版不同即回归）：**不构成缺陷**；最紧 4.8 px 记观察项（§11-3）。
- P8 `VUL DE KRONIEK IN` 类扫描：本版 P8 无此标题；A 节标题为意大利语 "COMPLETA LA CRONACA"，无荷兰语长标题；P8 各节标题均经 EDGE/FOOTER 门禁（0 flags）且目视干净。该类情形在本版不存在。

## 10. KIT §10 两处文档债（入仓前修，不是本版缺陷——本轮核对现状）

- **Q92**：交付文件（text.md:985、p8 SVG、P8 渲染页）印出注实为一词 "**Groeiprognose** voor 2027: +0,8 %"（正确荷兰语复合词）；translations.py nl 值（:1755）同为 "Groeiprognose voor 2027: +0,8 %"；门禁 B20 已验注与 translations.py 一致。KIT §10 称注读作 "Groei Prognose"（两词）与交付不符——KIT 描述 stale，非版面缺陷。
- **Q32**：交付文件印出注用 **«Fate dolci»**（角引号）：text.md:1015、p8 SVG、P3 渲染页（Q32 题面亦为 «Fate dolci»）；p8 SVG 中直引号 “Fate dolci” 出现 0 次。KIT §10 称注用直引号与交付不符——KIT 描述 stale，非版面缺陷。
- 结论：两处均为 KIT 订正项，本版无需改动（与 proof2 O2 相同结论；重扩散未修 KIT §10，本轮复核现状未变）。

## 11. 观察项（单独列，不计缺陷）

1. **网 PDF 重建非逐字节相同**（见 §5）：重建 1,291,725 B（与交付同字节数）但 SHA 不同；文字层逐字节一致（110,119 bytes）。属 fontTools 子集化字节序不确定性，非内容差异；印 PDF 逐字节复现已通过。
2. **KIT §10 两处观察与交付文件不符**（见 §10）：Q92 印出注实为一词 "Groeiprognose"；Q32 注用 «Fate dolci» 角引号。建议 KIT 订正，本版无需改动。
3. **P1 LA SETTIMANA 奶油盒最紧处余 4.8 px**（见 §9）：在盒内、无裁切、无重叠、与备份旧版逐字相同，按 STRADDLE 规则不构成缺陷；下一轮重扩散仍须重测。
4. **"circa 26 miliardi"**：DPB 口径为 23.5 亿，但 CdM 10月28日批准的法案版经多家来源确认为"约 26 亿"（Meloni 口径），且文中已写 "circa" 并注明"根据报纸重建"，P6 另有"数字随辩论更新、引用前核对"的提示。不构成缺陷。
5. P3/P5 中部结构空白、P8 答案字号压至 9.75pt 下限，均为核心既有版式与 SOP §1.1 让步第 4 步（与核心一致），KIT 已载明。
6. 无真实读者来信——编辑示例 + 披露（承诺 VOL.5），与 W46 模式一致，KIT §6 已载明。
7. 标题数（实测定义，不用幻数 "56"）：≥30 px 标题角色文本节点共 **37** 个；标题字符串出现 **27** 次；去重后不同标题字符串 **20** 个（proof2 同法复测一致）。"56 titles" 在本版无对应实测数，不采用。

## 12. 缺陷清单

无。零缺陷，可定稿。

## 13. 生产区未改动证据与方法备注

- 三 SHA 开工盘核与收尾复核逐字一致；`git status` 仅见 core-it `2026-w47-it-zh-cn.text.md` 与 `WEEKLY-KIT.md` 两处 M（D-2 fix 既有改动，FIX-LOG §5 已记）及版/核心目录 untracked 既有状态——本轮未向生产目录写一字节（构建与重建全在自有 scratch；freeze baseline 报告发运核心 SVG 运行前后重哈希无变化）。
- `tools/freeze.py diff` 只做 CJK 会计、纯拉丁改动不可见；`tools/p8.py compare` 只比键——两个门禁都不能发现 frozen 意大利语文本漂移；本次 D-2 回归靠的是旧串全版重扫 + 文本导出 diff + freeze baseline 的 SVG 字节比对 + PDF 文字层检查（与 FIX-LOG §7 同一方法论）。
- 未改任何工具（freeze.py / gates.py / occlusion_audit.py / p8.py / webpdf.py / translations.py 均未动；gates 脚本与 measure_cream.py 为 proof2 脚本的本 scratch 拷本，仅改写输出路径）。

## 14. 证据索引（本 scratch）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（门禁总表）
- `logs/gates-reproof.log`、`logs/run-rebuild.log`、`logs/render-rebuild.log`、`logs/webpdf-rebuild.log`、`logs/freeze-baseline-core.log`、`logs/cream-measure.log`、`logs/cream-measure-backup.log`、`logs/registry.json`
- `gates/gates-reproof.py`、`gates/nl/`（p8-extract.json、p8-compare.json、freeze-diff.json）
- `measure_cream.py`、`measure_cream_backup.py`
- `render/p-1–p-8.png`（交付印 PDF 200 dpi 全页渲染）、`tmp/pw/`（逐页印/网文字层）、`tmp/web-rebuilt.txt` / `tmp/web-delivered.txt`（网 PDF 文字层比对）
- `build/`（版 build-copy 重建 SVG + 重渲印/网 PDF；OUT/BASE 已重定向）、`freeze-base-core/`（核心 freeze baseline build-copy）
- `probe.txt`
