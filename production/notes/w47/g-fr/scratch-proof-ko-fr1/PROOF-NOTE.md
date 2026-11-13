# PROOF-NOTE — 2026-W47 · ko → fr（韩语目标语 × 法语读者）· proof1 独立复校

- 版目录：`production/2026-w47/2026-w47-ko-fr/`（fan-out #3 重建版，未提交）
- 复校员：独立复校（proof1）· 2026-11-11
- 依据：仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑；讲解/导读用读者母语；对外内容禁内部标签/周次/语言代码），任务书所列全套门禁
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-fr1/`（全部工作在 goals 侧 scratch；生产文件只读，未改动、未 commit、未 push）

## 结论：(a) 定稿

**零缺陷。**150 题逐题手验全部通过（三源：源文件 REG → P8 印刷键 → 题干/正文事实）；8 页逐页目视无溢出/重叠/压页脚/图片问题；机械门全部通过；#3 承接项逐一重验全部成立。

## 缺陷清单

无。

## 承接项逐项重验（fan-out #3）

1. **curly Frame 缺陷已在盘上修好（「」）**——通过。8 个 SVG + text.md 的 U+201C/U+201D/U+2019/U+201E 全部为 0；P7 Frame 盒为核心式 「」 形：`Cadre : 「après ~」. Demandez : 「〜 후에 뭐 해요?」`（P7 渲染目视确认；text.md 第 761 行同文）。与 ko-es 同类缺陷的修法一致。
2. **P1/P4/P7 变（核心 D2/D3/D4）+ Frame；P2/P3/P5/P6/P8 须字节一致**——实质通过，附一处记录限制。直接验证新内容已全部落盘：P1 quiz #10 题干为 `한국시리즈에서 우승한 팀은 어느 팀이에요?`；P4 #47 同题干，#48 为 `한국시리즈 전적은 어떻게 돼요?`（无重复 `시리즈`）；P7 frame 例句 + 金句 #7 为新句 `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`（check_core phrases 8/8 verbatim 含该句；P7 渲染目视确认）。freeze diff（核心 run 11 vs 本版）亦证：全部 8 页新增内容只属于法语讲解层，韩文串无新增（新增 CJK 仅 7 个 U+3000 页脚分隔符），即 P2/P3/P5/P6/P8 不含任何旧核心残留。**记录限制**：#2 版的 SVG 哈希未留存（ko3 apply 做 rmtree 时 wiped），“P2/P3/P5/P6/P8 与 #2 字节一致”无法从现存记录独立复算；KIT 的该断言与本轮 freeze diff 结论一致，但本轮只独立证实了“无旧核心残留”这一实质项。
3. **网 PDF −2,439 B = 字体子集重生成**——算术核对通过：KIT 记载旧 #2 网 PDF 4,024,760 B，今 4,022,321 B，差正好 −2,439；印/网文字层（plain pdftotext）各 52,304 B 字节一致，词多重集一致。网 PDF 只核落盘 SHA，未重渲染（遵守网 PDF 铁律）。
4. **text.md 52,232→52,304 B（+72：核心新长句）**——算术与内容双核对通过：52,304 − 52,232 = +72；本轮 textmd.py 重导出与交付 text.md 字节一致（449 items）；新增字节对应核心 D2/D3/D4 的新长句（P1 #10、P4 #47/#48、P7 frame/金句）。
5. **记录项 `Tout` is_prose quirk（332 vs 333 → 今 449 vs 452）**——已说明，非缺陷。fr text.md 449 项 vs 核心 452 项，净差 3，逐项对账成立：(a) `Tout`（P1 目录 8면 行的级别标签）在 P1 SVG 中存在（x=1840.0, y=1600.0, 18px, anchor=end，右缘正好 1840，在 1862 版心内；P1 渲染目视可见），但 `is_prose` 丢弃 3 字母裸拉丁词，故 text.md 无此项——核心 text.md 的平行项为中文 `全部`（CJK 通过 is_prose，得以保留），所以这 1 项差是导出器行为，不是内容缺失；(b)(c) P7 读者来信 disclosure：核心 2 行（`lko` 韩语行 + `lcn2`）按设计移除，本版只留 1 行法语 disclosure（P7 渲染目视确认；style11 的 P7 VOL.5 计数 3→2 亦证）。集合差分复核：核心独有 90 项 vs 本版独有 87 项，净 −3，与三项对账吻合。`Tout` 在印 PDF/网 PDF 中均正常渲染。

## 判为非缺陷的项（摘要，详见 GATE-LOG）

- **D5 字体（生产级待定项，仅记录，不计入判定）**：ledger 2026-11-11 记“D5 字体范围待用户定（A 78 版 / B 390 版）”。本版未发现 ko-fr 特有的 D5 字体缺陷；范围待定，不计入本次判定。实测补充：印/网全书 italic span 均为 0（印版自身无斜体，网版无丢失——与 nl-ko 的 D5 斜体丢失不同类）；P8 最小字号 9.98 pt（≥9.75，合规）。
- **三处 Et vous ? 盒 desc-clear −0.3**：P2/P3/P5 的 `envoyez-les-nous.` 末行，creambox 公式（0.30×字号假设降部）报 desc-clear −0.3。PIL 真墨水复核：该行 Noto Sans CJK KR 20px 的 `y` 实际降部 5px，三盒真墨水底缘分别为盒底内 +0.66/+0.71/+0.66 px；300 dpi 像素裁图目视确认降部在盒内、盒下留有奶油空隙。为紧配合、非缺陷（符合 ko-es 先例标准：真墨 ≥ +0.1 即在盒内；未来该盒文案加长须重测）。
- **creambox +45 窗口负值**：20 条 BELOW-WINDOW 行全部为盒下相邻标题/表行/表注（+26..+44），逐条裁定假阳性；49 个盒 inside-only clearance 全为正（最小 +5.7），P7 toolbox min inside +12.5、min desc-clear +6.5。
- **P2/P3 重复题干**：#12=#8、#13=#9、#18=#22、#74=#37 等题干在两处逐字重复——与核心 ko 源文件逐字相同（本轮逐项比对核心 content12/34/56/7/8.py），为核心原文设计（P1 闪电问答与 P2 练习复现、跨页复现），非本版引入；text.md 导出按去重规则只列一次，census（166 项）0 缺失。
- **P8 #150 键为 `✓`**：核心与本版一致（extract #150 == `'✓'`）；`(tâche libre — texte modèle ci-dessous)` 是题干，范文在 H 区（169 字，150–200 内，已逐字计数）。
- **配对题注末尾重复选项字母**（如 `25. d — … 199 456 wons d`）：核心原文惯例（源注字面自带字母），非缺陷。
- **KIT 笔误（非版面缺陷）**：KIT Adjudicated 称 text.md 含 `___` “23 处”，实测 75 处，与核心 text.md 的 75 处逐字相同；23 为 KIT 数字错误，版面本身与核心一致。
- **P7 金句页码标注**：8 条逐字出自本期正文，页码标注逐一核实正确（2면/1면/4면/2면/3면/6면/1면/6면）。
- **韩文双句号 `..`**：ko-es 观察项在本版未复现——SVG 文本行与 text.md 的 `..` 均为 0（含核心）。

## 核实摘要

- **身份核对**：印 PDF SHA `e4db2a54a97f2d4a0c5f949617d7760055832e3096076599d15c16e40d98bdc2`、45,468,252 B；网 PDF SHA `a5f712d25aa52a65d967bba45966bffe22d39b231098b37924cd0f0458c0cbc9`、4,022,321 B；text.md SHA `4e5487a69ec8c6584f90d9674f16775696daf55cb892af88203c700f6c59f378`、35,275 B——开工与收尾两次核对均与任务一致，未变。
- **核心未变**：核心 ko（run 11）8 个 SVG 开工/收尾哈希一致（P1 `00227ca1…`、P2 `faf9e3c5…`、P3 `b447a559…`、P4 `d997631e…`、P5 `09f7fc23…`、P6 `d45b0355…`、P7 `14b7cf13…`、P8 `e88f7d42…`，11 月 11 日 08:40 落盘，run 10 之后 P1/P4/P7 三处为 fix1 D2/D3/D4）；核心 text.md SHA `da1d3a32…` 与核心 KIT 一致。核心只读核查，未重建核心。
- **150 题手验**：源文件 REG（AST 解析 content*.py 的 `.ex`/`.match_set`）150 项 vs P8 SVG 提取键 149 项精确一致 + #150 `✓`（预期）= **150/150**（`keycheck-150.json`）；p8 compare vs 核心 **CLEAN**（missing=[]、extra=0、keydiff=[137, 138]，两项为 E 节翻译题合法法语重定向，键本身逐字核对正确）；每键均按题干+正文重推（算术重算：19 天、1 天、4 小时、17 年、65、100；配对题字母对照印刷版 a–d 列表：P2 D 25-d/26-a/27-c/28-b、P3 43-b/44-a/45-d/46-c、P4 61-c/62-d/63-a/64-b、P8 F 141-b/142-c/143-a/144-d；范文 169 字）。
- **全文通读**：text.md 全文 917 行 + 印 PDF 8 页逐页目视（150 dpi 自渲染，另网 P1/P8 目视与印版一致）；日期/星期全部用日历核验（11-16 周一、11-18 周三、11-19 周四、11-20 周五、11-21 周六、11-22 周日、11-28 周六、12-05 周六、12-11 周五，全部吻合）。
- **E 节 type 标签已本地化**：Compléter / Choix multiple / Apparier / Transformer / Faire des phrases / Vrai ou faux / Texte à trous / Traduire / Écrire；无中文标签；text.md 与全部 SVG 的 Han 字符均为 0。
- **ABSTRACT.txt**：378 字节、单行（1 个尾换行）、无 ASCII 双引号、法语，含 `Lucerna Korean Weekly VOL.4`、CSAT、Jour du kimchi、Samsung 首冠、examen d'histoire、feuillages、A2 à B2、150 exercices。
- **8 张图片**均带目标语图说 + CC0/PD 出处（lumoplank、wizdata、Udonhan1992、Paul Cézanne、Bain News Service、Gary Todd、Anattadairy ×2），图说诚实（P1 秋日为资料照片、P2 明确“不是 김장 사진”、P3 Cézanne 为画作）。
- **源文件未动**：未改动、未重建、未 commit、未 push 任何生产文件；run.py/render.py/textmd.py 均在 goals 侧 scratch 副本上跑；网 PDF 未重渲染。
