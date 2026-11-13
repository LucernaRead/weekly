# PROOF-NOTE — Lucerna Weekly 2026-W47 it-nl（proof1，独立复校）

- **版次**：2026-W47，意大利目标语 × 荷兰语读者层（it-nl），VOL.4，刊期 2026-11-16（周一）– 2026-11-22（周日）
- **复校员**：proof1（只读复校，未修版、未 commit、未 push）
- **复校日期**：2026-11-11
- **复校对象**：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-nl/`
- **先读**：SOP.md §1.1 / §8 / §9、repo AGENTS.md、协调员 brief、该版 WEEKLY-KIT.md —— 均已读

## 1. SHA 核对（开工前已验，三件全部一致）

| 文件 | 大小 | SHA-256（KIT §7 登记值 = 盘上实测值） |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-NL.pdf` | 14,034,647 B | `9322290029fa8175400a21cf2539346ba767fa8299812c6b7cb1c039d36ea242` |
| 网页 PDF `La-Lucerna-VOL4-NL-web.pdf` | 1,259,635 B | `6c546925c847f034bd1381b435a8cdbb863920f3597f9ae3e994356298655d56` |
| 文本导出 `2026-w47-it-nl.text.md` | 55,590 B，1317 行 | `49a5e6ead7d9b25484354def7e1d03fd5c604670a5f1524d0915edc65afd8597` |

## 2. 复校方法与范围

- 8 页印刷 PDF + 8 页网页 PDF 全部渲染为 PNG（100 dpi）并逐页目视；`2026-w47-it-nl.text.md` 逐行读完（1–1317 行）。
- 意大利语正文与荷兰语讲解层逐句读；150 道练习键逐题与题干语义核对（匹配题键值另行核对，不只比对键值本身）。
- 事实逐条查公开来源核对（见 §5），不只信 KIT。
- 几何：occlusion audit + canonical creambox（+45px 窗口）+ 真墨迹横向扫 + BOXTITLE 真墨迹量 + P8 字号实测；并补查 audit 看不见的四类漫出（盒底、BOXTITLE 出奶油盒、横向漫出、基线定盒高时的下行字母漫出）。
- 门禁：p8 compare（core-it 对 it-nl，显式 `--core-p8` / `--edition-p8`）、freeze（`--core-svg` 指 core-it/svg）、p8 extract、印刷/网页 text layer 字节比对、VOL 计数、masthead band 检查。
- Abstract 按 SOP §9 核 `ABSTRACT.txt`。

## 3. 门禁与计量结果（全部通过，无新发现的问题）

| 检查 | 结果 |
|---|---|
| occlusion audit（edition svg 目录，selftest 6 类 planted 缺陷全部触发） | **0 flags** |
| p8 compare core-it vs it-nl（150 题） | **CLEAN**，两边各 150/150 noted；keydiff 仅 [137, 138, 139]（属预期的翻译题重定向键） |
| freeze diff（`--core-svg` = core-it/svg） | rc=0；新增 CJK 仅 8× U+3000（每页 1 个，家具分隔符，SOP §1.1 豁免）；P8 +173/−637 字符串为中文讲解 → 荷兰语讲解（预期） |
| p8 extract（edition P8 SVG） | 150/150 noted |
| P8 RISPOSTE 键 vs text.md RISPOSTE 键 | 1–149 全同；#150 仅记法差异（PDF "✓" vs text.md "✓ Modeltekst in sectie H hieronder (99 woorden)"，同义） |
| 正文练习键 vs RISPOSTE | 正则命中 137 题全同；其余 13 题为匹配题组头（25–28 / 52–55 / 141–144，另种格式），键已人工核对：25=c, 26=b, 27=d, 28=a；52=d, 53=b, 54=c, 55=a；141=d, 142=c, 143=b, 144=a |
| 印刷 vs 网页 text layer | `pdftotext` 各 46,021 字节、7,906 词，词 multiset 完全相同；像素差异仅照片重压缩 + 字体光栅化（P7 但丁像、P8 维梅尔、P1 刊头光栅化），文字内容相同。（注：KIT §7 写 7,905 词，实测 7,906，相差 1 词，微不足道） |
| canonical creambox.py（全部 8 页 SVG，29 个奶油盒） | 全部盒内基线余量为正（最小 +4.5px）。P7 工具盒盒底实测：ERRORI TIPICI +18.1（下行字母余量 +12.2）、LA PAROLA +4.5（下行字母余量 −1.5）、LETTERE +5.1（下行字母余量 −0.9）。原始输出中 6 条负“余量”均为假阳性（+45px 窗口内下一节标题：P1 LA PAROLA 标题、P3 IL TORRAZZO 标题、P6 ESERCIZI 头；P4 白底表格行；P4 表下注）。另有多处下行字母余量 −0.4 ~ −1.5px（P2 LO SAPEVI −1.1、P2 E TU −0.4、P3 IL WEEKEND DOLCE −1.2、P3 E TU −0.9、P4 E TU −1.5、P5 I GIOVANI −1.1、P5 E TU −0.9、P7 LA PAROLA −1.5、P7 LETTERE −0.9）：下行字母超出无边框奶油盒底约 1px，肉眼不可见（无边框可越界，下方 26px+ 内无物），occlusion 0 flags——评估为非缺陷 |
| BOXTITLE 真墨迹量 | 除 D1–D3 外全部 fit（例 P1 IN QUESTO NUMERO 墨 end 1824.2，P7 LA PAROLA end 1853.5） |
| P8 最小字号（SVG 实测） | 13.0 SVG px = **9.75 pt**（186 个 13px 文本节点，RISPOSTE 键），与 KIT 一致，SOP §1.1 下限（concession step 4） |
| 模型文本 | 99 词（text.md 实数），与 KIT 一致 |
| 练习总数 / 分级 | 150 题（P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38；A2 47 / B1 70 / B2 33），与 KIT 一致；150 个编号键在 text.md 中齐全 |
| VOL 计数（SVG） | VOL.4 共 9 个节点（P1 2 个：刊头带 + 页脚；其余每页 1 个页脚），与 KIT 一致；VOL.5 恰 3 个合法节点（P2 E TU 盒、P7 LETTERE 披露、P7 下周预告） |
| 刊头带修复验证 | 首节点 x=10.5，间距 11.0（build1 缺陷为 −2.7px 剪切）；occlusion EDGE 0 flags；渲染图两侧边距干净 |
| Abstract（ABSTRACT.txt，SOP §9） | 一行，荷兰语，无 ASCII 双引号，真实主题，含 Lucerna + Italiaans + A2–B2 + 150 exercises。✓（text.md 内无 abstract 节，与 core-it 模式一致；`tables.json` 无 `abstract_heading` 键；insert.py 从 ABSTRACT.txt 处理 frontmatter） |
| 禁用词 | Ucraina / Russia / Putin：0 命中 ✓ |
| CJK 残留（text.md） | 101× U+3000（家具分隔符，SOP §1.1 豁免）+ 4×「翻译」（见 D8） |
| P7 "FRASI DELLA SETTIMANA" 8 句引文 | 逐句在正文中核实原文与页码引用（P1、P4、P1、P5、P2、P6、P3、P6），全部逐字相符 ✓ |
| P4 赛果表进球总和 | 手工核实：10 场 24 球 ✓ |

## 4. 语言通读小结

- 意大利语正文通读无拼写/语法硬错；荷兰语讲解层通读基本干净，仅 D8–D10 三处小问题。
- 150 题键与题干语义已人工核对（含匹配题组），除 D13 的时态歧义观察外，键与题干一致。
- P7 LA PAROLA 一句措辞略怪（观察，未编号）："Questa settimana vive a pagina 1 e a pagina 4"（"这个词本周住在第 1 页和第 4 页"）——core 冻结文本，可读、带玩笑口吻，仅作风格注记，不列为缺陷。

## 5. 事实核查（逐条查公开来源，2026-11-11）

| 事实簇 | 核查结果 |
|---|---|
| Serie A 第 11 轮（11 月 6–8 日）10 场比分 | **已核实**：正文所列 10 场比分全部相符（Venezia–Udinese 2–1、Fiorentina–Juventus 2–2 等）；10 场 24 球 ✓；Lazio 29 / Inter 28 / Roma 27 / Milan 第 4 名 24 / Como 23（第 5）/ Udinese 垫底 5 ✓；Roma 最佳攻击（31 球）✓；Lazio 不败 ✓；Gattuso 为 Lazio 主帅 ✓；第 11 轮 11 月 6–8 日 ✓；第 12 轮 11 月 21 日重启 ✓；Fiorentina 9 分（第 15）✓ |
| 第 12 轮赛程 | **已核实**：Lazio–Lecce 周六 21 日 15:00；Atalanta–Inter 周日 22 日 20:45，Bergamo ✓；Monza–Fiorentina 周一 23 日 20:45 收官 ✓ |
| Nitto ATP Finals 都灵 | **已核实**：11 月 15–22 日，Inalpi Arena；Zverev 世界第 1；Alcaraz 为热门之一；Flavio Cobolli 首次入围；Jannik Sinner 因右膝伤缺席（2024、2025 两届冠军）；8 人、2 组、半决赛周六 21 日、决赛周日 22 日 |
| Manovra 2027 | **已核实**：DPB 10 月 15 日送交布鲁塞尔；2027 增长 +0.8%、赤字占 GDP 3.4%（含欧盟条款；无条款 2.8%）；部长会议 10 月 28 日批准法案，约 260 亿欧元；Irpef 第二档 33% 从 €50,000 扩至 €55,000；银行/保险约 50 亿欧元；两院预算委员会联合听证 11 月 9–12 日，周四 12 日收尾（Bankitalia、UPB、部长 Giorgetti）；法案号 C. 3174-bis（11 月 4 日印为 A.C. 3174，三条拆分后改为 3174-bis）；修正案截止周二 11 月 17 日 18:00；须 12 月 31 日前最终批准 |
| Nations League | **已核实**：Italy–France 周四 11 月 12 日 20:45，San Siro，米兰；Belgium–Italy 周日 11 月 15 日 20:45，King Baudouin Stadium，布鲁塞尔；A1 组（France、Italy、Belgium、Turkey）；正文正确地未印赛果（赛后才踢）、留待 VOL.5 ✓ |
| Festa del Torrone，Cremona | **已核实**：第 29 届，11 月 7–22 日，16 天 / 3 个周末，主题 «Il Confine»；Torrone d'Oro 授予 Davide Simonetta（Cremona 出生的音乐制作人/作者/作曲家），周日 22 日 11:00，Palatorrone；Corteo Storico 16:00，150+ 盛装游行者；Sforza–Visconti 婚礼重演 17:00，Piazza del Comune；旗手与火焰表演至 18:00；压轴 18:00 "Il torrone va in brodo"（肉馅饺配 torrone 汤，Palatorrone）；torrone 传说（Bianca Maria Visconti / Francesco Sforza 婚礼，1441 年 10 月 25 日，torrone 形似 Torrazzo）——正文以 "La leggenda dice che…" 表述，定性正确 ✓ |
| Eurochocolate，Perugia | **已核实**：第 32 届，11 月 13–22 日，主题 «Fate dolci»；Calabria 为首届 "Regione Ospite"（"Calabria Straordinaria"，bergamotto、cedro、peperoncino、fichi 等）；"I tesori della Calabria" 周五 20 日 18:15，LAB-Luisa Annibale Base；Iginio Massari 周日 22 日压轴 ✓ |
| BookCity Milano | **已核实**：第 15 届，11 月 23–29 日，1,360 场活动 / 2,487 位嘉宾 / 1,164 本书 / 443 个场地；主题 «Il senno sulla Luna»（Ariosto《Orlando furioso》）；开幕周一 23 日 20:00，Teatro Dal Verme，Colson Whitehead（两届 Pulitzer 奖得主）；预热周日 22 日 16:00，Fondazione Luigi Rovati，Edmund de Waal ✓ |
| Torino Film Festival | **已核实**：第 44 届，11 月 24 日–12 月 2 日 ✓ |
| Filmmaker Festival，Milano | **已核实**：11 月 14–22 日，周日 22 日闭幕 ✓ |
| Madonna della Salute，Venezia | **已核实**：每年 11 月 21 日；1630 年瘟疫与 10 月 22 日还愿（doge Nicolò Contarini）；Basilica 由 Baldassarre Longhena 设计，1631 年动工、1687 年 11 月 21 日祝圣；还愿桥（船桥，今为浮桥）Santa Maria del Giglio → Salute；castradina（盐渍烟熏羊肉 + verza）传统上在节日前夕、即 11 月 20 日晚食用 ✓；"quasi quattrocento anni"（1630→2026 为 396 年）✓ |
| Giornata nazionale degli alberi | **已核实**：首届 Festa dell'albero 1898 年（公共教育部长 Guido Baccelli 倡议）；2013 年 1 月 14 日第 10 号法律定 11 月 21 日为国家树木日 ✓ |
| Santa Cecilia | **已核实**：11 月 22 日，音乐与音乐家的主保 ✓ |
| Torrazzo di Cremona | **部分不符，见 D11**：112.54 m、"中世纪/砖结构最高"属实；但"全意大利最高 campanile"的说法不成立（Mortegliano campanile 113.20 m 为第一） |
| P1 "GIORNO PER GIORNO" 各日条目 | LUN 16 / MAR 17 / GIO 19 / VEN 20 / SAB 21 / DOM 22 六条内容全部与事实相符（修正案截止、Eurochocolate 活动、ATP、Salute、Serie A、闭幕日）；但 **缺少 MER 18（周三）条目，见 D12** |


## 6. 缺陷清单

### D1 — P1 BOXTITLE 漫出奶油盒：LA SETTIMANA IN CIFRE（本版级，严重）

- **位置**：P1 印刷页 / 网页页，"LA SETTIMANA IN CIFRE" 盒标题；SVG 节点 x=556.5，基线 y=1388.5，Noto Sans CJK SC 23px 粗体。
- **证据**：真墨迹实测墨 end x=1074.2；奶油盒右缘 x=961.0 → **超出盒右缘 113.2 px**。截图 `crop-p1-cifre.png`：荷兰语后半 "DE WEEK IN CIJFERS" 完全落在奶油盒外的白纸上，肉眼可见。occlusion audit 报 0 flags（符合任务提示：它看不见 BOXTITLE 漫出奶油盒）。
- **级别**：本版级。core-it 只有意大利语标题，fit；加了荷兰语后半才溢出。
- **修法**：缩短 `translations.py` 中该标题的荷兰语值（或缩小标题字号），重渲染；并核查其余 it-* 版同类双语长标题。

### D2 — P2 BOXTITLE 漫出奶油盒：LA FRASE PER RICORDARE（本版级，严重）

- **位置**：P2，"LA FRASE PER RICORDARE" 盒标题；节点 x=556.5，基线 y=1310.5。
- **证据**：真墨迹墨 end x=1097.8 vs 盒右缘 961.0 → **超出 136.8 px**。截图 `crop-p2-frase.png`："OM TE ONTHOUDEN" 落在盒外白纸上，肉眼可见。同 D1 类别。
- **级别**：本版级（core-it 意大利语单标题 fit）。
- **修法**：同 D1，缩短荷兰语标题值或缩小字号，重渲染。

### D3 — P7 BOXTITLE 漫出奶油盒：ERRORI TIPICI（本版级，严重）

- **位置**：P7 右上 ERRORI TIPICI 工具盒标题；节点 x=1461.5，基线 y=242.0。
- **证据**：真墨迹墨 end x=1921.2 vs 盒右缘 1862.0 → **超出 59.2 px**（仍在页缘 1950 内，余 28.8px）。截图 `crop-p7-errori.png`："FOUTEN" 落在盒外白纸上。同 D1/D2 类别。
- **级别**：本版级。
- **修法**：同 D1/D2。注：其余 boxtitle 实测均 fit（P1 IN QUESTO NUMERO end 1824.2；P7 LA PAROLA end 1853.5）。

### D4 — P2 匹配题选项超出右版心（本版级，中等）

- **位置**：P2 匹配题（Q25–28）选项行。
- **证据**：真墨迹实测 "b. il ponte di barche per la festa del 21" 墨 end 1875.0；"d. la piccola luce di cera che si accende" 墨 end 1877.8；右版心 1862 → **分别超出 13.0 / 15.8 px**。截图 `crop-p2-match.png`："21" 明显探出其余行之外。core-it 对应行 end 1831.0 / 1821.8（在版心内）。
- **级别**：本版级；由 D5 的改写拉长所致。
- **修法**：随 D5 一并处理（改写进 core 后重分发，或改回 core 措辞并缩短）；也可断行。

### D5 — Freeze 违规：Q26/Q27 意大利语选项文本被改，未记录（本版级，严重——流程违规）

- **位置**：本版 `content12.py:262/264` vs core-it `content12.py:262/264`。
- **证据**：本版写 "il ponte di barche per la festa del 21 novembre" 与 "la piccola luce di cera che si accende in chiesa"；core 写 "il ponte di barche per la festa in novembre" 与 "la piccola luce di cera accesa in chiesa"。该改动**不在** `translations.py` 中（grep 无命中），**不在** KIT §9 记录中，因此 KIT §8 "0 unexplained fragments" 的说法对 P2 不成立。新意大利语本身正确、甚至更好（"per la festa in novembre" 原句别扭），键/含义不变（b、d），但正是这处改写拉长了行文、造成 D4 的版心溢出。
- **级别**：本版级（改动发生在 it-nl 的内容源）。
- **修法**：将改进后的措辞写进 core（`core-it/content12.py:262/264`），使各版一致，再重分发；同时修正 KIT §8 的说法。

### D6 — P4 匹配题选项伸入栏间空白（core 级，继承，轻微）

- **位置**：P4 匹配题选项行。
- **证据**：真墨迹 "b. che non ha mai perso, ancora senza" 墨 end 969.0（+8.0，超出第 2 栏右缘 961）；"c. il gruppo di squadre che giocano tra" 墨 end 973.5（+12.5）。core-it 数值完全相同。行尾落在 28px 栏间空白内（第 3 栏起于 989），无任何重叠（occlusion TEXTX 0）。截图 `crop-p4-match.png`。
- **级别**：core 级，继承；无碰撞，仅版式不洁。
- **修法**：core 中缩短/断行该两行；或接受（建议修，因是所有 it-* 版共有）。

### D7 — P8 F 节匹配题选项伸入栏间空白（core 级，继承，轻微）

- **位置**：P8 F 节（Q141–144）匹配题选项行。
- **证据**：真墨迹 "a. la parte del sistema fiscale, un livello" 墨 end 1430.0（+18.5，超出第 3 栏右缘 1411.5）；"b. i soldi che pagano una misura, la sua" 墨 end 1430.5（+19.0）；"c. la differenza tra spese ed entrate, in" 墨 end 1419.8（+8.2）。core-it 数值完全相同。行尾落在栏间空白内（第 4 栏起于 1439.5），无碰撞。截图 `crop-p8-matchF.png`。
- **级别**：core 级，继承；无碰撞，仅版式不洁。
- **修法**：同 D6，core 中缩短/断行。

### D8 — text.md 翻译题型标签残留中文「翻译」（本版级，轻微，网站可见）

- **位置**：`2026-w47-it-nl.text.md` 第 969 / 971 / 973 / 975 行，E 节 Q137–140 型标签：`[A2 · 翻译]` 等（共 4 处；与 it-es proof1 发现的同类残留相同位置）。
- **证据**：同行已带荷兰语标签 "[Vertaal in het Nederlands/Italiaans]"；渲染的 P8 只显示荷兰语。core-it 的 text.md（`2026-w47-it-zh-cn.text.md`）同样位置带「翻译」——对 zh-cn 版正确，对 nl 版错误。text.md 是网站正文体，荷兰语读者会在网站上看到中文标签。
- **级别**：本版级，仅 text.md（印刷/网页 PDF 不受影响）。
- **修法**：将该 4 处标签改为荷兰语（或删去中文标签，只留已有的荷兰语标签）。注：KIT §8 称之为 "deliberately kept (W46 precedent)"——但对 nl 读者仍是可见的中文残留，建议改。

### D9 — Q92 RISPOSTE 注荷兰语拼写错误（本版级，轻微）

- **位置**：text.md RISPOSTE 第 92 条（约第 1100 行附近）及渲染的 P8："Groei Prognose voor 2027: +0,8 %"。
- **证据**：荷兰语复合词应连写：**Groeiprognose**。KIT §10 已将其列为留待复校员的既有观察。
- **级别**：本版级（讲解层）。
- **修法**：改为 "Groeiprognose voor 2027: +0,8 %"。

### D10 — Q32 注引号风格不一致（轻微）

- **位置**：Q32 注：'Het thema van Eurochocolate dit jaar is "Fate dolci"'。
- **证据**：其余注/标题一律用 «…»（法式引号），此处用了直引号 "..."。KIT §10 已注记。
- **级别**：轻微。
- **修法**：改为 «Fate dolci»，与全书一致。

### D11 — Torrazzo "全意大利最高 campanile" 说法不准确（core 级，轻微，事实）

- **位置**：P3 边栏 "IL TORRAZZO E IL TORRONE"；text.md 第 317 行："Il Torrazzo di Cremona è il campanile più alto d'Italia."
- **证据**：Torrazzo 高 112.54 m；Mortegliano（UD）Duomo campanile 高 113.20 m（1955–1959，Pietro Zanini 设计），在 "Torri e campanili più alti d'Italia" 排名中列第 1，Torrazzo 第 2（it.wikipedia；fr/de/es 维基同）。Torrazzo 正确的最高头衔是 "la torre medievale / in laterizi più alta d'Italia"（全意最高中世纪/砖结构塔）。注：法语维基 Torrazzo 条目本身也重复了 "plus haut campanile d'Italie" 的流行说法，故属广泛流传的简化表述，但按实测高度排名不成立。
- **级别**：**core 级**——core-it text.md 第 317 行原句相同，且全部 it-* 版 text.md 第 317 行一致；修 core 才能根治。
- **修法**：core 中改为 "Il Torrazzo di Cremona è la torre medievale in laterizi più alta d'Italia."（或 "il campanile in mattoni più alto d'Italia"），重分发。

### D12 — P1 "GIORNO PER GIORNO" 缺少周三 18 日条目（core 级，轻微–中等，内容缺口）

- **位置**：P1 "GIORNO PER GIORNO" 日程条；text.md 第 71–85 行；P1 SVG（`p1-prima.svg`）。
- **证据**：条目只有 6 行——LUN 16、MAR 17、GIO 19、VEN 20、SAB 21、DOM 22；**MER 18（周三）完全缺失**。text.md、core-it text.md、core-it P1 SVG、it-nl P1 SVG 四处一致缺失（SVG 文本节点枚举确认：无任何 "MER" 节点）。其余 6 条内容本身全部核实无误（见 §5）。封面日程条自称 "Cosa succede, giorno per giorno"，一周 7 天缺 1 天，读者可见。
- **级别**：**core 级**，继承。
- **修法**：core 中补一行 MER 18（如 Filmmaker Festival 大师课 / ATP 小组赛进行中），重分发。

### D13 — 观察（不列为硬缺陷）：passato prossimo + "domenica" 的时态歧义（core 级，低）

- **位置**：Q40 "Il corteo ___ (arrivare) in piazza domenica" → "è arrivato"；Q43 "Perugia ___ (chiudere) Eurochocolate domenica" → "ha chiuso"；P7 Q105 "Il corteo ___ (partire) alle 16" → "è partito"；Q106 "Domenica noi ___ (vedere) gli sbandieratori" → "abbiamo visto"；Q108 "La Festa del Torrone ___ domenica" → "è finita"。
- **证据**：所涉事件为周日 2026-11-22，付印时在未来；但 P7 B1 盒明确把 passato prossimo 框定为 "per raccontare il weekend"（讲述周末），读者在周末之后做题时可把 "domenica" 读作过去。形式全部正确，歧义真实但可辩护。
- **级别**：core 级；低严重度，仅作观察，不要求改。若要消除歧义，可在题干加时间状语（如 "domenica scorsa"）或在 P7 盒中说明。

## 7. 未核实项

无。§5 所列事实簇已全部核实或明确标注（D11/D12 为已核实的反例）。其余未逐条核查的次要细节（如各场馆具体地址）未写入正文主张，不列入。

## 8. Verdict

**(b) 有问题，不可直接定稿。**

共 13 项：D1–D13。其中须修后重渲染的有：D1、D2、D3（三处 BOXTITLE 漫出奶油盒，渲染页肉眼可见）、D4+D5（P2 版心溢出 + freeze 违规）、D8（网站正文中文残留）；建议同批修的有：D9、D10（荷兰语小错）、D12（封面缺周三）；core 级修法后重分发的：D11（Torrazzo 最高头衔）、D12、D6/D7（栏间空白，可接受暂缓）；D13 仅为观察，不要求改。

其余全部通过：事实（除 D11 外）逐条核实无误；150 题键语义核对无误；门禁全绿（occlusion 0、p8 compare CLEAN、freeze 除 D5 外干净、creambox 盒内余量全正、P8 9.75 pt、印刷/网页 text layer 一致）；abstract 合规。

---

**证据截图**（均在 `scratch-proof-it-nl1/` 目录内）：`crop-p1-cifre.png`（D1）、`crop-p2-frase.png`（D2）、`crop-p7-errori.png`（D3）、`crop-p2-match.png`（D4）、`crop-p4-match.png`（D6）、`crop-p8-matchF.png`（D7）。
