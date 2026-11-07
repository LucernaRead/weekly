# W45 NL×PT 独立全量复校报告 — ZERO PROBLEMS（可定稿）

- **结论：ZERO PROBLEMS（可定稿）。** 原校对 NOT PASS 的唯一阻塞项 B1 已修复并经从头全量复测通过；其余 11 项 gate 全部通过；无新增阻塞项。
- **复校性质**：SOP §8.4 要求的修复后从头全量复校，不是范围复查。以下每一项均为独立重测，不采信修复员自述（自述仅作为待验证的断言逐项核对）。
- **校对对象**：`files/weekly-report-w45-nl-pt/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **对照**：W45 荷兰语核心 `files/weekly-report-w45-nl-core/`（VOL.2，150 题，页数 10/18/18/18/18/18/12/38，A2 47/B1 72/B2 31，范文 87 词）；W43 同配对版 `files/weekly-report-nl-pt/`（家具以 W43 实测为准）
- **校对合规**：只校对，未改任何源码/交付物/构建树；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）；未清理共享 scratch 目录（本次 scratch 仅用 `/tmp/proof-nl-pt-reproof/`，含自写测量脚本、沙箱 transform 副本与裁图；`tools/scratch/` 未动）。
- **开工查重**：首次检查时无进行中渲染进程（`ps` 无 render/ink/cairo 进程）；交付目录最新写盘为 22:04–22:06（已完成交付的新鲜 mtime）；90 秒后复查零新写盘、两次快照哈希完全一致，判定为安全开工，未 stand down。
- **交付物指纹（校对前后两次实测一致，未被校对改动）**：
  - 印刷 PDF `De-Lucerna-VOL2-PT.pdf`：7,944,272 B，sha256 `5381c70d3214201d85295768474e00e5c5fab911c4df960bd5f90701d67f5c26`，8 页
  - 网页 PDF `De-Lucerna-VOL2-PT-web.pdf`：3,674,752 B，sha256 `ef62e218874351f9003c565de88291f5369adc2c43fea829ffd61910032a9eef`，8 页
  - SVG：p1 `74255a72…`、p2 `f69cbe1c…`、p3 `e8240f62…`、p4 `10ee2009…`、p5 `2ad4c8c0…`、p6 `23d95c54…`、p7 `3c070720…`、p8 `34582529…`（全长见第 2 项）
  - 卡片 8 张均为 1950×2700；p2 卡片 `d2e3f16d…`（余见第 2 项）
- **测量方法说明**：墨迹盒沿用原校对与构建库同一方法——PIL Noto Sans/Serif CJK SC 面，`getbbox` 左右 + `getmetrics` 上下（基线锚定）；另以 `getlength`（advance）复核版式右界。两法差值仅来自 PIL 整数 bbox 与小数 advance 的取整（见第 6 项方法注），不影响任何结论。

## 1. B1 修复验证 — 通过

- **终版 P2 D 节指令实测**（`p2-leven.svg`，与原阻塞位置同一槽位）：
  - 元素：`x=1647, y=1973, font-size=19.5, font-family=Noto Sans CJK SC, text-anchor=start`，文本 `Ligue palavra-significado`（保留 palavra/significado 两关键词）。
  - advance **227.2px**（修复员称 227.2px，分毫不差）；advance 右界 **1874.2px**；基线锚定真墨迹盒 `(l=1647.0, t=1950.0, r=1874.0, b=1979.0)`，真墨迹右界 **1874.0px**（修复员称 1874.0px，分毫不差）。
  - 判定：真墨迹右界 1874.0px ≤ 1885px 栏界（余 11.0px）；距内框 1910.6px 有 **36.6px** 实质间隙（按 advance 右界计为 36.4px，与修复员称 36.4px 一致，差值仅为真墨迹与 advance 的 0.2px 取整差）；距外框 1923.7px 有 49.7px。原阻塞（超内框 22.6px、超外框 9.5px、末字母被框线切断）已消除。
- **P2 卡片 2× 裁图目视**：`Ligue palavra-significado` 全词完整，末字母 `o` 字形完整、与右侧内外两道框线有明显间隙，无任何压框。
- **D 节题目与答案未动**：P2 渲染的 D 节配对项与核心逐项相同（`de Klimaatweek / besparen / de waarschuwing / lokaal`；选项 `a. een bericht dat zegt: let op, gevaarlijk weer` / `b. een week vol acties voor het klimaat` / `c. voor je eigen omgeving, niet overal` / `d. minder energie gebruiken`；答案顺序 `b, d, a, c`）；核心构建目录 `content12.py` 同 `match_set` 仅 instr 与注译不同，荷兰语词表/选项/答案逐字一致。核心冻结内容未动（见第 3 项）。
- **P8 同指令原样保留**（修复员称“故意未改”，实测证实）：
  - P8 元素：`x=1185, y=544.24, font-size=19.5, Noto Sans CJK SC, start`，文本 `Associe a palavra ao significado` 原样存在；advance 286.3px、真墨迹右界 1471.0px，页内无溢出。
  - P8 SVG 与修复前基线逐字节一致（见第 2 项），P8 卡片亦逐字节一致。
  - 修复机理独立验证（沙箱副本，非真实构建目录）：将 `content12.py` 第 278 行反向还原为修复前长指令后，在 `/tmp` 沙箱副本中运行 `transform_pt.py`，输出 `transform ok: 1 replacements across 8 files`；沙箱 `content12.py` 与真实构建目录逐字节相等，`content8.py` 哈希在变换前后不变。证实 FIX5 恰做 1 处替换、仅 P2、P8 不动；`transform_pt2.py` 全局映射第 174 行 `('instr="Match word to meaning"', 'instr="Associe a palavra ao significado"')` 仍在（未被改动）；P8 指令后接 `f.head("G · DIALOOG BIJ DE BOMEN", …)` 而非 `e.end_report()`，故 FIX5 的尾随 `e.end_report()` 锚定确实只匹配 P2。

## 2. 修复范围验证 — 通过

- **对照修复前基线 `fix5-baseline-sha256.txt` 逐项核对**（18 项：8 SVG + 8 卡片 + 2 PDF），变化恰为以下 4 项，别无其他：
  - 变化：`svg/p2-leven.svg`（`f6d002f1…` → `f69cbe1c…`）、`cards/p2-leven.png`（`5a2d3499…` → `d2e3f16d…`）、印刷 PDF（`2c763f65…` → `5381c70d…`）、网页 PDF（`96c3fe71…` → `ef62e218…`）。
  - 不变（逐字节一致）：p1 `74255a72e53abd5ca0722c9d3b243616ad852b96e60b7ea67eb38dd66de7fe37`、p3 `e8240f62c305f0f5b4845d087a4900a05ca7fac2749cbcc1c0267138630638a2`、p4 `10ee20096d6f558a836e693cdb4a049677a81cdd8b180fd49067754ad8387eb3`、p5 `2ad4c8c077653ab8b68964655046c210c3a5e6cd01ba2e1f1bb79865a5d996f9`、p6 `23d95c542f06b6e4765c5787cb931fce08b27e4dfcc8ff3689f2e02b79d0dbb5`、p7 `3c0707202f62c48a8d80c4cce64fb61fa416e30a1ecadf2221e33b60de6a65ba`、p8 `34582529879d5d3a1e35758a2d315f1d19a670ee62966b1488f9258a2344c4b3`；卡片 p1 `0a06a684…`、p3 `9201fb2d…`、p4 `a3191254…`、p5 `32756a43…`、p6 `fa3c4f94…`、p7 `eb1a27e4…`、p8 `c1528f84…`（全长与 `final-sha256.txt` 一致）。
  - 修复员“仅 P2 SVG、P2 卡片、双 PDF 变化，其余 7 页 SVG 与 7 张卡片逐字节不变”的说法逐项属实。
- **核心 8 个 SVG 修复前后不变**：核心哈希与原校对所列及 `freeze-baseline-fix5.txt` 一致（p1 `5424557b…`、p2 `78e6fcd2…`、p3 `5b9854e3…`、p4 `cc227fd9…`、p5 `e58064c9…`、p6 `6583fe28…`、p7 `65cfe2b3…`、p8 `fe22a151…`）；校对前后核心哈希亦不变（见第 3 项）。
- **题量/等级/分页/范文与核心一致**：修复后构建日志 `build-log-fix5.txt`：TOTAL 150，A2 47 / B1 72 / B2 31，分页 10/18/18/18/18/18/12/38，范文 87 词；P8 H 范文实测 87 词且与核心范文逐字相同（见第 5 项附带核查）。

## 3. 冻结 — 通过

- `freeze.py baseline`（核心构建目录 `hidden_files/weekly-report-w45-nl-build`，tools venv，输出至 `/tmp`）：**8/8 SVG 字节复现**（repointed 文件与原校对一致：render.py、content12/34/56/7/8.py）；核心哈希跑前跑后一致；校对前后核心与分版 SVG 哈希均未变。
- `freeze.py diff`（独立重跑）：p1 +31/−29，p2 +39/−33，p3 +32/−27，p4 +29/−25，p5 +39/−33，p6 +37/−32，p7 +47/−45，p8 +189/−175；**每页新增 CJK 均为 0**，分版 CJK 总量每页均为 0（核心 191/212/153/126/214/192/373/1033 → 分版 0）；全 8 页脚本重扫：CJK 0、平假名/片假名 0、韩文 0、西里尔 0。
- **被删非中文串逐项裁定**（全部已删串已过目；非中文串清单与原校对裁定一致，无新增）：
  - P1 `DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS`：核心 P1 y=372 槽位荷兰语 strapline，被同槽位葡语徽章原位替换（见第 10 项），非正文冻结句丢失；
  - P8 `— PAGINA n —` ×8：家具分隔符，替换为 W43 同形 `— PÁGINA n —`；
  - P8 `104. blijf — rood = blijf binnen` → 分版 `104. blijf — rood = ficar em casa`：键 `blijf` 与代码 `rood` 逐字保留，仅注译葡语；
  - P8 `6. planten — veel mensen → planten` → 分版 `6. planten — Sujeito no plural, por isso planten`：键 `planten` 逐字保留，仅注译葡语；
  - 其余被删串均含中文（讲解层中→葡替换）或为中文注换行碎片（如 P6 孤 `）`、P7 `bomen。`/`thuis。`/`zij zette vast。`/`。`），其中 `bomen` 在分版 `«een boom» ou «bomen».` 中保留，`zij zette vast` 在 `= prender: zij zette vast.` 中保留，`thuis` 见非阻塞观察 O1（完整句同页另有两处逐字出现，不构成冻结句丢失）。
  - **结论：无冻结荷兰语句丢失。**

## 4. P7 词框冻结 — 通过

- 定义句在分版 P7 三行逐字保留，拼接后与目标完全一致：`«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.`（行：`«meedoen» betekent: deelnemen,` / `erbij zijn. In de Klimaatweek doet` / `heel Nederland mee.`，与核心逐行相同）。
- 仅 gloss 本地化：分版单行 `meedoen = participar.`（恰 1 处）；定义句未被本地化（无 `meedoen» significa` 之类变体）。
- 诊所荷兰语纠正句逐字保留：`→ «Een» is enkelvoud: «een boom» of` / `«bomen».`；`→ Na «omdat» staat het werkwoord op` / `plaats 2: «... blijf ik thuis.»`（分版 y=891.8/919.68，文本逐字相同）。

## 5. P8 — 通过

- `p8.py compare`（独立重跑，tools venv）：核心 150 noted，分版 150 noted，**status CLEAN，missing=[]，extra_count=0，uncertain=[]**，keydiff `[7, 17, 70, 71, 76, 96, 137, 138, 148]`。EXTRA_ONLY 不适用（集合相等）。
- keydiff 逐项对照印刷 P8 行（分版行含换行续行，已拼接核对）：
  - 伪影类（印刷 key token 与核心逐字节相同，仅注译葡语且行尾以括号结尾）：
    - 7：`B` 不变，`7. B — A Semana do Clima dura 7 dias (2–8 de novembro)`；
    - 17：`wortelen` 不变，`17. wortelen — wortelen = criar raízes (sujeito no plural)`；
    - 70：`eiland` 不变，`70. eiland — eiland = ilha (het)`；
    - 71：`proef` 不变，`71. proef — proef = prova, desafio (de)`；
    - 76：`gaat winnen` 不变，`76. gaat winnen — gaat winnen = vai vencer (só um palpite)`；
    - 96：`advies` 不变，`96. advies — advies = conselho (het)`；
    - 148：`B` 不变，`148. B — zachte = macia (solo)`。
  - 真实重定向类（翻译题按读者语重定向，译文正确）：
    - 137：核心键 `气候周持续七天。` → 分版键 `A Semana do Clima dura sete dias.`（印刷行 `137. A Semana do Clima dura sete dias. — Compare com o título da página 1`）；
    - 138：核心键 `橙色预警意味着：做好准备。` → 分版键 `Código laranja significa: prepare-se.`（印刷行 `138. Código laranja significa: prepare-se. — Da página 2 · bereid je voor = prepare-se`）。
  - 139/140 不在 keydiff 内已证实：`p8.py extract` 键逐字相等——139 核心/分版均为 `Museumnacht duurt van 19:00 uur tot 02:00 uur.`，140 均为 `Ik doe mee aan de Klimaatweek.`；其印刷行仅注由中文译为葡语（139 `— Atenção à expressão de tempo van...tot...`，140 `— meedoen é um verbo separável`）。
- P8 答案注释为纯葡萄牙语：P8 文本层 CJK 0 处；150 条印刷行注层为葡语（荷兰语键、荷兰语例句、语法术语与专名除外）；`Nota em português em cada resposta · ✓ = com modelo` 与实际一致。
- 附带：P8 H 范文（Tekstmodel 段）分版与核心逐字相同，均为 87 词。

## 6. 几何遮挡 — 通过（含 B1 揭示维度的全页右缘扫描）

- `occlusion_audit.py` 独立重跑（自检均通过，6 类 planted 阳性全触发、clean 对照静默）：分版 **0 旗标**，核心 **0 旗标**，`--core` NEW 对比 **0**。
- 自写墨迹碰撞扫描（同基线墨迹法）：同基线碰撞 **8 页全清**；P8 亚阈值 graze（原校对记录：P8 指令与 Tekstmodel 行交叠 20.3×1.1px，高 < 3px 阈值）经 P8 卡片 2× 裁图目视复核：两行分属不同基线、竖向分离清晰，无可见碰撞。
- P6 图表标签覆盖（基线锚定墨迹法重测，逐项对后绘不透明形取最大覆盖）：`Ik blijf thuis/45`（y294）、`Ik kijk eerst naar de tekst/25`（y352）、`Ik ga toch naar buiten/20`（y410）、`Ik weet het niet/10`（y468）均为 **0.0%**，远低于 30% 阈值；P6 卡片目视图表标签清晰、条形未压字。
- **全页右缘扫描**（一切墨迹右界 vs 内框 1910.6px / 外框 1923.7px / 栏界 1885px，逐页）：
  - **无任何一页墨迹超过内框 1910.6px，无任何一页超过外框 1923.7px。** 各页真墨迹右界最高值：P1 1884.8、P2 1901.0（见下）、P3 1884.7、P4 1884.7、P5 1884.7、P6 1884.7、P7 1884.7、P8 1885.1（见方法注）。
  - 按生产版式 advance 法（原校对与构建员 rightedge 扫描所用法）：**唯一超 1885px 栏界的正是修复前已存在、核心继承的 P2 选项 c 行** `c. voor je eigen omgeving, niet overal`（x=1485，advance 右界 1901.5px，框内、未超内框）；其文本与 x 与核心逐字/逐坐标相同（核心同行 x=1485，y 仅因分版流排而异 5px，不影响右界），属原校对 O4，非新增框线压字。
  - **方法注（非阻塞，须披露）**：若改用严格真墨迹（getbbox）法，另有两行以 +0.1–+0.5px 的取整量越过 1885px——P2 `O que significa cada cor?`（真墨迹 1885.5px，advance 右界恰 1885.0px）与 P8 `Nota em português em cada resposta · ✓ = com modelo`（真墨迹 1885.1px，advance 右界恰 1885.0px）。两者均为 `text-anchor=end` 且 x=1885 的右对齐栏界行（版式上即以栏界为右缘），越界量来自 PIL 整数 bbox 大于小数 advance（`?` 尾字 +0.48px、`o` 尾字 +0.11px），距内框仍有 25.1–25.5px，无任何框线接触；且两者均为修复前已存在（P8 SVG 逐字节不变；P2 该行源自 transform 非 FIX5 条目，沙箱证实 FIX5 为唯一改动），不是 Fix5 新增。因此“唯一实质性超栏界”为选项 c 行的结论在版式法下成立，在真墨迹法下仅多出这两处亚像素取整 artifact，均不构成缺陷、不阻塞。

## 7. FIX3 复测 — 通过

- P1 词条注行单行：`«Clima»: o tempo e a natureza a longo prazo.`（x=1451, y=1846.3, fs19），advance **393.1px**（与原校对及构建员说法分毫不差），真墨迹右界 1844.0px。
- 框：rect `(1451, 1874, 434×430)`，墨迹化框顶 1873.3px；注行真墨迹底 1851.3px，**间隙 22.0px**（原校对 22.25px，0.25px 差来自 y 取整，不影响结论），无覆盖、无截断。
- P1 卡片同区域 2× 裁图目视确认：注行完整清晰，框顶线在其下方，`IN HET KORT · Em resumo` 框体完整，修复属实。

## 8. gloss 计数与金句 — 通过

- gloss 计数（按渲染后 gloss() 字符串本身拆 `·` 逐项计数；SVG 渲染 Nota 块按换行拼接后计数与之一致）：
  - P2：核心 6 = 分版 6（het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal）；
  - P3：5 = 5（het museum / de rondleiding / het tijdslot / tweedehands / de beurs）；
  - P4：5 = 5（de balans / gelijkspelen / de speelronde / de topper / de stand）；
  - P5：5 = 5（het eiland / de proef / stemmen / de aflevering / voorbij）；
  - P6：5 = 5（de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander）；
  - 与核心 1:1，分版注均为葡语。
- P7 金句 8 句（荷兰语原文，不含 «»）：每句全页总出现次数恰为 **2**（源文章 1 + P7 «» 行 1），且在其标注页上各实测存在 1 次；页码标签序列 Página 1, 1, 2, 3, 4, 5, 6, 6 与核心 Pagina 序列数字一致（词形按葡语加注音，与 W43 同形）：
  - P1 `Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland`；P1 `De herfst is de beste tijd om te planten`；P2 `Geel betekent: let op, het weer kan gevaarlijk zijn`；P3 `Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts`；P4 `Ajax won donderdag 22 oktober met 2–0 van Atalanta`；P5 `Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur`；P6 `Een code is geen verbod, maar een advies`；P6 `Het weer is van ons allemaal, maar het raakt ons allemaal anders`。

## 9. 读者园地 — 通过，零编造

- P7 BRIEVEN VAN LEZERS 块逐行核对，页上同时具备三事实：1. 截稿时无真实来信；2. 无最佳 P8 作文；3. 示例 + VOL.3 承诺。
- 荷兰语披露句原文保留（4 行拼接）：`Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.`（与核心逐字相同）。
- 葡萄牙语披露句同义：`Ainda não chegaram cartas reais nem os melhores textos da página 8 — por isso este exemplo; a promessa passa para o VOL.3.`
- 显性葡萄牙语邀请（祈使句 + 刊登承诺，已核对为独立邀请行）：`Exemplo da redação — não é real. Envie suas cartas reais e seus melhores textos da página 8: vamos publicá-los no VOL.3!`（`Envie` 祈使 + `vamos publicá-los no VOL.3!` 承诺）。
- 示例标注为编辑部示例：`— Li (voorbeeldbrief van de redactie)` + `Exemplo da redação — não é real.`；示例信本身为核心荷兰语原文（Li 在上海学荷兰语、气候周在阳台种树），未编造新来信。

## 10. 家具（W43 实测对照）— 通过（分隔符字号差异见 O2，不阻塞）

- 徽章（P1）：分版与 W43 逐属性一致——`x=975, y=372, font-size=19.5, font-weight=700, fill=#a4553a（brick）, text-anchor=middle`，文本逐字相同：`TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`。**未用 donor 的 20pt olive 形**。
- P4 栏题：`SPORT · Esporte`，`x=78, y=116, fs36, fw700, fill=#f3edda`，与 W43 逐属性一致。
- 页脚 8/8 标 VOL.2：每页 `De Lucerna · SEMANÁRIO NEERLANDÊS VOL.2 · TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS`（x=65, y=2624, fs20, #57523f）+ `Página N de 8`（x=1885, y=2624）；除 VOL.2（W43 为 VOL.1，属正确卷号）外与 W43 形式一致。
- P8 分隔符：`— PÁGINA 1 —` 至 `— PÁGINA 8 —` 齐全，粗细 700、颜色 #3e4c2a、栏位 x=65/527/989 排布与 W43 一致；字号分版 13.5pt vs W43/核心 14pt（见 O2，形式未变）。
- gloss 前缀：P1–P6 均以 `Nota — ` 起始，P7 无 Nota 块（与 W43 一致）。
- ABSTRACT.txt：单行（strip 后 1 行）、无 ASCII 双引号；含真实主题关键词（Semana do Clima、Noite dos Museus、Crossing Border、Eredivisie、Expeditie Robinson）与学习者搜索短语（`aprender neerlandês lendo`），含 VOL.2、A2–B2、150 练习；全文与原校对所录一致。
- 卡片 8 张逐页目视（本复校看了全部 8 张）：P1、P2、P3、P4、P5、P6、P7、P8 均无重叠、无截断、无压框。P2 除 B1 修复部位外其余正常；P3 D 节指令换行残行 `3.` 可见（见 O5，非缺陷）。

## 11. KIT 验证 — 通过

- KIT §9 Fix 5 条目：含 B1 修复前墨迹右界 1933.2px（超内框 1910.6px 与外框 1923.7px）、修复后 advance 227.2px / 墨迹右界 1874.2px / 真墨迹 1874.0px / 距内框 36.4px、修复方式（P2 专属 FIX5、尾随 `e.end_report()` 锚定）、P8 不动的原因（全局 MAP2 条目未改、沙箱验证恰 1 处替换、P8 逐字节不变）——以上每一值均与本复校实测一致。
- KIT §9/§10 状态：`Status after Fix 5: fix round complete, still NOT finalized — independent full re-proof required after this render change (SOP §8.4)` 及 §10 交付注“builder-complete, NOT finalized，independent full re-proof pending”——状态表述为“修复轮完成、仍未定稿、待独立全量复校”，与本复校的前提一致（本报告即该复校的结论：ZERO PROBLEMS，可定稿）。
- KIT 所列新 PDF/SVG/卡片哈希（§9 末行 119–122）与磁盘现值逐项一致（18/18，见第 2 项）；KIT 计数（150、A2 47/B1 72/B2 31、分页、范文 87 词）与实测一致。
- **O1–O5 非阻塞观察未被借机改动**（修复轮未扩大范围）：
  - O1：P7 诊所注仍为 `lugar: blijf ik.`（仍省 `thuis`），荷兰语纠正句仍含 `blijf ik thuis`；
  - O2：P8 分隔符仍 13.5pt；
  - O3：P1 副标题仍为 `WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · SPEELRONDE 12`，仍缺 MUSEUMNACHT token；
  - O4：P2 选项 c 行仍在框内（见第 6 项）；
  - O5：P3 D 节指令换行残行 `3.` 仍可见，非一道题，P3 实际题数仍为 18 题。
  - 三者（O1/O2/O3）均为原校对记录状态，修复轮未动；O4/O5 亦未变。

## 12. 其他 — 通过

- 图片：仅公有领域/CC0，每照片页恰 1 个 `<image>`（P1 herfstbos、P2 kinderdijk、P3 gracht、P4 elftal1912；P5–P8 无照片，与核心一致）；署名行与原校对所录一致（P1 `Foto: Vovogov90 — CC0`、P2 `Foto: Nationaal Archief — CC0`、P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`、P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek / domein`）。
- 全文 `桥接` 0 处（讲解层已全为葡语）；英文星期/月份名与 `False:`/`On Thursday` 残留 0 处（FIX2 终态保持）。
- 终态一致性：KIT 计数与核心 KIT 一致；P1 头条流、数字框词头与原校对记录一致；练习行数与核心一致。

## 与修复员自述不符处

1. **无实质性不符。** 修复员关于 B1 的全部数值断言（修复前 286.3px/1933.2px、修复后 227.2px/1874.2px/真墨迹 1874.0px/距内框 36.4px、P8 不动的原因、沙箱恰 1 处替换、范围仅 P2 SVG + P2 卡片 + 双 PDF、其余逐字节不变、核心 SVG 不变）均经独立重测证实，分毫不差（除下述两处纯方法取整差，均已注明，不构成出入）。
2. **方法取整差（非不符）**：
   - P2 选项 c 行：修复员/KIT 称 1901.5px（advance 法），本复校真墨迹法测得 1901.0px——同一行、同一 x/文本，差值来自 advance 小数与 PIL 整数 bbox 的取整，右界结论（框内、未超内框）不变。
   - FIX3 间隙：原校对 22.25px，本复校真墨迹法 22.0px——0.25px 差来自注行 y 取整，advance 393.1px 分毫不差，结论（无覆盖）不变。
   - 右缘扫描方法注见第 6 项：真墨迹法下两处 +0.1/+0.5px 右对齐栏界行取整越界已披露并裁定为非缺陷。

## 非阻塞观察（注明：不阻塞）

- **O1 — P7 诊所葡语注尾省略 `thuis`（不阻塞，沿用原校对）**：分版 `Na oração principal, o verbo fica em 2.º lugar: blijf ik.` 对比核心中文注，葡语例证缺 `thuis`；但语义完整，且完整句 `blijf ik thuis` 同页另有两处逐字出现，不构成冻结句丢失。修复轮未动，本复校亦不要求改动。
- **O2 — P8 分隔符字号 13.5pt vs W43/核心 14pt（不阻塞，沿用原校对）**：文本、粗细、颜色、栏位均与 W43 一致，仅字号小 0.5pt；无重叠、无溢出，形式正确，修复轮未动。
- **O3 — P1 副标题 donor 缩短，缺 MUSEUMNACHT token（不阻塞，沿用原校对，KIT 已披露）**：副标题为家具行，MUSEUMNACHT 仍见于头条、目录与 P3 全版，不构成内容丢失，修复轮未动。
- **O4 — P2 选项 c 行超栏界但未出框（非缺陷，沿用原校对）**：见第 6 项，核心继承版式，卡片上完整可见。
- **O5 — P3 题号 naive 计数 19 vs 18 的解释（非缺陷，沿用原校对）**：多出的 `3.` 是 D 节葡语指令换行残行，核心中文指令为单行；不是一道题，P3 实际题数仍为 18 题。
- **N1 — 右缘扫描真墨迹法下的两处亚像素取整越界（非缺陷，本复校新增披露）**：见第 6 项方法注。两行均为右对齐栏界行、修复前已存在、距内框 25px 以上、无框线接触、无目视缺陷；建议后续复校统一以 advance 法报告栏界、以真墨迹法报告框线接触，避免取整 artifact 误读为溢出。

## 过程合规

- 校对全程未清理共享 scratch 目录；未向 weekly-git、Discord、主聊天、cron 做任何写入或投递；核心与 W43 目录仅只读；真实构建目录仅只读（transform 验证在 `/tmp` 沙箱副本中进行）。
- 校对前后交付物与核心哈希均未变（EDITION-FINAL-UNCHANGED、CORE-FINAL-UNCHANGED）。
