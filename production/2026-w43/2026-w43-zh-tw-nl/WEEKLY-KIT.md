# WEEKLY-KIT — 2026-W43 zh-TW × NL（繁體中文正文 · 荷兰语讲解）

- 版本：VOL.1（2026 年 10 月 19 日（一）至 10 月 25 日（日）· 台灣 / 香港）
- 配对：繁體中文正文 + 荷兰语讲解（讀者母語 = Nederlands）
- 母版：繁體核心 VOL.1（files/weekly-report-zhtw-vol1/，正文 + 英語講解，台港原生獨立製作）
- 构建目录：hidden_files/weekly-report-zh-tw-nl-build/（由核心 build 复制）
- 状态：**已建成 + 建造者全量自校；独立校对 PASS**（未入仓、未投递）

## 1. 基线（freeze.py baseline）

复制核心 build 后未改动重跑：**8/8 页 SVG 逐字节一致**（sha256 与已发布核心全同：
p1 c37cb10e… / p2 494af3da… / p3 15315e2e… / p4 02d393f9… / p5 fc677f71… /
p6 1367d4f0… / p7 873a21ac… / p8 c532615c…）。收尾复验核心目录 8 页哈希未变，核心完整。

## 2. 方法

- 只改讲解层：定义、语法、指令、双语节头、框题、P7 讲解段与诊所/句型/读者信注、
  P8 全部注释与小节头译为荷兰语；繁體正文、题目、选项、图片、版式几何冻结。
- 一进程重渲染（run.py 单进程跑 content12→34→56→7→8，共享注册表）。
- 答案生成代码逐字节未改（仅注释字符串本身译荷兰语）；核心 P8 为 dash 式
  （`N. key — note`），本版同式，印全 150 条注释。

## 3. 家具（NL 列定式，as shipped）

- P1 徽章（砖红 #a4553a，与已入仓 zh-TW 扇出各版同位同色）：
  «TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
  取舍说明：任务简报字面作 «TEKSTEN IN HET TRADITIONEEL CHINEES…»，而 tools/tables.json
  的 NL 目标名表作 CHINEES TRADITIONEEL、且同列已入仓的 zh-cn-nl 页脚实样为
  «TEKSTEN IN HET CHINEES (VEREENVOUDIGD)»;为列内一致，本版采用 tables/实样形
  «TEKSTEN IN HET CHINEES (TRADITIONEEL)»（徽章与页脚同形），特此登记。
- 页脚（每页）：«Lucerna · CHINEES WEEKBLAD VOL.1 · TEKSTEN IN HET CHINEES (TRADITIONEEL) · UITLEG IN HET NEDERLANDS» / «Pagina N van 8»
  （weekblad 为中性名词，形容词不词尾变化：CHINEES WEEKBLAD。）
- 注释前缀：«Uitleg — »（全版 11 处；核心的 «Notes｜» 0 残留）。
- 指令：Fill in → «Vul in»；Match → «Koppel»；Writing → «Schrijf»。
- P8 分隔符：«— Pagina N —» ×8；答案区头 «Antwoordsleutel»，右注 «Alle noten in het Nederlands · ✓ = het modelantwoord»。

## 4. 总量与分级

练习 **150**（A2 56 · B1 65 · B2 29，与核心逐项一致）；各版题数 10/18/18/18/18/18/12/38；
写作题范文 134 字（与核心同）。

## 5. 键差异登记（key-diff registry）

| # | 核心印刷键/注 | 本版印刷 | 原因 |
|---|---|---|---|
| 150 | ✓ Open task - the model answer is printed in section F above (134 characters) | ✓ (Open opdracht — het modelantwoord staat hierboven in deel F (134 tekens)) | 写作题：读者语言改向（唯一一处） |

其余 149 键与核心逐字节相同（tools/p8.py compare：keydiff 仅此条的注文差异，
工具口径下 status CLEAN）。印刷注释集合按编号与核心 **EQUAL（150 = 150）**。

## 6. 拼音规则执行核查（繁體扇出规则）

- 荷兰语注释中引用中文词一律带声调拼音（如 Liánjià、Bǔjià、Shūyùn、Mǎnqiān sòngbǎi、
  Pǐnwèiquàn、Dēnggāo、Liúyǒu kàn）；句首拼音首字母大写。
- 终稿 P8 答案区实测：**全角括号 = 0**（核心为 6）、**括号内汉字段 = 0**；全版答案区汉字引用清零。
- 排版器 _fw 现象登记：含 CJK 的括号对会被转全角、CJK 后逗号转 «，»。
  本版两处主动规避并已修复：P7 诊所条 #2 将拼音式结构改写为 «兩 is 'twee' — zie 兩隻蟹
  (twee krabben)»（括号内纯拉丁，保持半角）；P7 B1 收尾将 «leer eerst 連假, dan…»
  改写为 «leer 連假 eerst, dan…»（逗号落在拉丁词后）。修复后 freeze --strict-cjk 全过。
- 正文内的中文引用（题目、P7 词条）为冻结正文，不在拼音规则范围。

## 7. P7 金句核查

8 句与核心逐字相同（含 _fw 后的全角标点形），每句在 P7 出现次数与核心相等（各 1 次）；
页标签计数与核心相等：(p.1)=1、(p.2)=1、(p.3)=2、(p.4)=1、(p.5)=1、(p.6)=2；
译文为本版新撰荷兰语。

## 8. 缺陷与修复（建造者自校，全为讲解层文字长度问题，正文/几何未动）

1. P8 答案流溢出：荷兰语注总行数初版 182 行 vs 核心 158 行，末栏压页脚带。
   压缩 26 条注（电报式荷兰语、义不变）+ #99 再压缩一条 → 总行数 158 = 核心，
   末栏终点 y=2440 与核心逐值相同。
2. P7 B2 节头过宽：«Plaatselijk taalgebruik» 461.9 > 栏宽 434 → 改 «Lokaal taalgebruik»（416.8）。
3. P7 三栏与右栏过长：teaser 初版终于 2594.66 越页脚线 2580。压缩 A2/B1/B2 讲解段与
   诊所/句型/读者信注共 20 余处 → col3 终点 1678.64、teaser 终点 2508.64，与核心逐值相同。
4. 遮挡审计初跑 2 面 NEW BOXTITLE：P2 «你呢» 框末行墨迹越框底 4.4（问题句 3 行→改写 2 行）；
   P6 票券框灰注 3 行→2 行（«Gewaarderd volgens de officiële uitsplitsing; besparingen:
   onze berekening.»）。修复后审计 0 面。
5. strict-CJK 初跑 P7 +3 字（«，»«（»«）»）：_fw 转换所致，按 §6 两处改写修复 → 0。

## 9. 工具门结果（终稿）

- freeze.py diff --strict-cjk：8 页 added CJK = **0**（讲解层汉字清零；各页 CJK 总量
  下降均为核心英文注中的汉字引用转拼音所致）。
- p8.py compare（--total 150）：**CLEAN** — core 150 noted = edition 150 noted，
  missing=[]、extra=0、uncertain=[]。
- occlusion_audit.py（自检先行通过）：本版 **0 flags**，vs 核心 **0 NEW**。
- 图片：8 页 <image> 数据与核心逐页字节相同（图 1/2/2/1/2/2/0/0 张）。
- 家具：页脚 ×8、«Pagina N van 8» ×8、徽章、分隔符 ×8 均实测在版。
- 日历实证（2026 真实日历）：10/18 日（重陽正日）、10/19 一（香港重陽翌日假期）、
  10/23 五 / 10/24 六（金鐘獎節目/戲劇）、10/25 日、10/29 四（Wine & Dine 開幕）、11/1 日 — 全合。
- 算术继承复核：品味證 40+200+160=400、省 400−258=142；尊尚 40+400+260+200=900、
  省 900−558=342；2,380−1,580=800；498×2=996；798−498=300；13+13=26；
  5,000÷1,000×100=500；2+1+4+2=9 — 与核心键一致，荷兰语注述同。
- 事实口径继承：強颱薔琵＋東北季風、登陸未定；台灣大賽僅 G1（味全 3:0、四萬人）；
  金鐘 61 在 10/23–24；繁體版零政治。
- 中间层禁用术语（中英两形）：报面 0、operative code 0、KIT 0。
  scratch 例外披露：hidden_files/zh-tw-nl-scratch/transform.py 与 fix1.py 为一次性
  变换脚本，其中引用核心原字符串作搜索模式（该核心无此类方法名，无需改名；
  两脚本实测该术语计数亦为 0）。

## 10. PDF 针脚（终稿实测）

- 印刷版 Lucerna-VOL1-NL.pdf：28,978,377 B，sha256 4fe7944674d99be6e6e9013c1213301b470ccc0da21148171fe58abdd7315ca5
- 网页版 Lucerna-VOL1-NL-web.pdf：3,035,350 B（< 10 MB），sha256 28f65e9130db203b87f9939158f65534b210723c602a8e51772e18b64a614e4a
- 卡片：cards/p1-front.png … p8-test.png ×8，建造者已逐页目检。

## 11. 独立校对记录（2026-10-21，独立校对员）

**结论：PASS** — 完整独立一轮零问题；版面工件无缺陷、无修复、无重渲染。
仅 KIT 登记一处数字不精确（见下），已按实印更正，不影响工件。

**工具门（全部独立复跑，scratch 在 hidden_files/proof-zh-tw-nl/scratch/）**
- freeze.py baseline：pristine 繁體核心 build 副本重跑 **8/8 逐字节复现**核心
  （c37cb10e…、494af3da…、15315e2e…、02d393f9…、fc677f71…、1367d4f0…、
  873a21ac…、c532615c…）；收尾 `sha256sum -c` 核心 8 页全 OK，核心未触碰。
- freeze.py diff --strict-cjk：**全 8 页 added CJK = 0** 独立复跑确认；
  §6 两处 _fw 规避改写实证在位——P7 诊所 #2 «Krabben weeg je in 両 (taels);
  兩 is 'twee' — zie 兩隻蟹 (twee krabben).»（与核心同坐标、同语义）、
  P7 B1 收尾 «Geheugentruc: leer 連假 eerst, dan de»（逗号落拉丁词后，
  与核心同 y=1417.7）；改写均未伤繁體正文语义。
- p8.py compare：独立复跑 **CLEAN — core 150 noted = edition 150 noted，
  missing=[]、extra=0，集合 EQUAL**，keydiff=[]。
- occlusion_audit.py（自检先行通过）：独立复跑本版 **0 flags、0 NEW vs 核心**。
  建造者登记的修复逐项成立：P7 B2 节头 «Lokaal taalgebruik» 在界内；
  P2 你呢框（问题 2 行 + 荷文 2 行）、P6 票券框灰注 2 行
  （«Gewaarderd volgens de officiële uitsplitsing; besparingen:
  onze berekening.»）均在框内；P7 teaser 末行基线 2474.64 与核心逐值相同
  （流终点 2508.64 < 页脚带 2580）；每页非页脚最大 y 本版均不深于核心。

**键差异复验（注册表级双 build 一进程转储 diff）**
- 150 = 150；页/级别/题型元数据零差异（A2 56 · B1 65 · B2 29；
  逐页 10/18/18/18/18/18/12/38）。
- **注册表键 150/150 逐字节相同，键差异 = ∅**；差异只在注文：149 条注译荷，
  唯一未变注为 #44 «HK$498 x 2 = HK$996.»（语言中立算式，正确保留）。
- #150 实印 «150. ✓ (Open opdracht — het modelantwoord staat hierboven in
  deel F (134 tekens))» 与 §5 登记逐字一致；范文逐字点数 **恰 134 字**
  （含标点）且与核心逐字节相同、冻结。
- **150 键全部由校对员对繁體正文/题干逐题手工重推导，逐题无误**
  （含 P6 图表：条长按轴刻度 1.8px/HK$ 成比例、0 点起画；
  算术 40+200+160=400 / 400−258=142、40+400+260+200=900 / 900−558=342、
  498×2=996、798−498=300、2,380−1,580=800、13+13=26、2+1+4+2=9、
  5,000÷1,000×100=500 全部对位）。

**拼音专项**：注册表层本版 150 条注含汉字 = **0**（核心 43 条含汉字引用
已全转带声调拼音）；P8 答案区（y≥1300）实测 **全角括号 = 0**
（核心 = 6)、**括号内汉字 = 0**（核心有 （外圍環流）（蟹乸）（登高）三处）；
如 #149 «Liúyǒu kàn» 对位核心 «留友看»。

**KIT 登记更正（仅文档层）**：§8 第 1 条「总行数 158 = 核心」不精确。
校对员按答案区文本元素实测（除两条页头与 8 条分隔符）：核心答案行
**158**、本版 **157**——唯一差异是 #26 注核心折 2 行、本版荷文较短折 1 行；
150 条注全在、键全同、末栏终点基线两版同为 2424.4（流终点 2440），
无内容与几何影响，非工件缺陷。

**其余逐项**：P7 金句 8 句逐字同核心，全刊出现次数两版各 2 次逐条相等；
页标签计数 (p.1)=1、(p.2)=1、(p.3)=2、(p.4)=1、(p.5)=1、(p.6)=2 全等；
家具逐页核对全对（徽章、页脚 ×8 与 «Pagina N van 8» ×8、
«Uitleg — » ×11、P8 分隔符 «— Pagina N —» ×8），且与已入仓 zh-cn-nl
实样同式（«CHINEES (VEREENVOUDIGD)» ↔ «CHINEES (TRADITIONEEL)»，
§3 取舍登记属实）；图片逐页标签与数据载荷与核心全等（1/1/2/1/2/2/0/0），
9 条署名行与核心逐条相同且对应置入图；日历经 `date`（Asia/Taipei）实测
全对（10-18 周日重陽、10-19 周一港假、10-23 周五 / 10-24 周六金鐘、
10-25 周日、10-29 周四開幕、11-01 周日）；事实口径继承无误
（薔琵登陸未定、台灣大賽僅 G1 味全 3:0 四萬人、金鐘 61 在 10/23–24），
繁體版零政治、讲解未引入政治；中间层禁用术语在成报/KIT/operative code
为 0；卡片 8× 1950×2700。

**最终针脚（磁盘实测，与 §10 登记逐值一致）**：网页版 **3,035,350 B /
28f65e9130db203b87f9939158f65534b210723c602a8e51772e18b64a614e4a**（< 10 MB）；
印刷版 **28,978,377 B /
4fe7944674d99be6e6e9013c1213301b470ccc0da21148171fe58abdd7315ca5**
（巨大系 zh 家族图源所致，只记录）。

核心未触碰；未入仓、未发 Discord。可以入仓 slug `2026-w43-zh-tw-nl`。

## D5 rebuild record (2026-11-14)

D5 font rebuild of this edition (W43 three-week redo, scope B). The installer `apply_variant.py --check` FATALs on this family's face-suffixed engine (`_IDX_TC`, `"sans_TC"`, `face="TC"`), so the D5 install was hand-ported step-by-step (`scripts/d5_port_zhtw.py`, same rep1 exactly-1-match discipline; D5_BLOCK / READER_CONST verbatim; FIX2_BLOCK mechanism verbatim, anchors re-based on this family's census). W47 engine transplant was rejected with evidence (no `_fw()`). Install: `scripts/install_zhtw.sh` (`--check` dry-run first). `_D5_READER = "latin"` (mode latin/TC); routing unit test FAILURES: 0; fix2 markers 5, `_QUOTE_CLS` 4, retained. §1.1 assembly: the port engine (490 lines) was copied into production first (production never held it; 9 `.py` files per edition, SHA-verified vs MANIFEST-W43.md) plus the pilot moth into `assets/` (10 editions).

- **Pre-D5 census** (baseline): D5_latin_in_cjk=426, D5_cyrillic_in_cjk=0, curly_in_cjk=0; post-D5 census all 0 (gate 3).
- **Build pins (D5 rebuild, final):** print `28,978,377 B`, sha256 `4fe7944674d99be6e6e9013c1213301b470ccc0da21148171fe58abdd7315ca5`; web `3,035,350 B (< 7 MB)`, sha256 `28f65e9130db203b87f9939158f65534b210723c602a8e51772e18b64a614e4a`. Web PDF is the builder original `scratch-2026-w43-zh-tw/patched/2026-w43-zh-tw-nl/2026-w43-zh-tw-nl.web.pdf` — the closer must copy it, never re-run webpdf (web PDFs are byte-nondeterministic across runs). Print PDF `scratch-2026-w43-zh-tw/patched/2026-w43-zh-tw-nl/Lucerna-VOL1-*.pdf`.
- **Cold cache:** print PDF cold-cache explosion in fix1 render: 98,845,804 B; warmed fc-cache and re-rendered from the same source -> 28,978,377 B; full gates re-run after.
- **Step-7 fixes (point sizes only, zero wording changes; full re-render + full gates after each fix):**
  - `content56.py:195` — P6 票券拆解 closing note para: 19.5 -> 19; spill 'berekening.' BELOW +4.67px -> 0 [pre-existing, identical in baseline].
- **P8:** extract 150/150; compare vs baseline en core CLEAN (missing=[], extra=0; [108] present in both core and edition — the zh-cn D28 core-missing-[108] discrepancy does NOT reproduce in this family). P8 lines base -> patched 201 -> 201 (unchanged by all fixes); footer slack 46.2px (>= 40 required).
- **Gates (17 + D18):** 18 GATE PASS, 0 hard FAIL. Gate 15a text.md: REFLOW — D5 reflow moves line breaks only (difflines=38, char-multiset diff 0, native verifier ADOPT all pages); the shipped `.text.md` is the joined patched export (faithful to the delivered PDF); byte-identical vs the baseline export is impossible where reflow moves wraps — REFLOW accepted per D30 (see family report §4). Gate 15a print=web PASS (multiset 0). gate 15b: shared `verify_textmd.py` rc=1 (FAIL, pre-existing verifier calibration gap — the baseline edition fails identically, only-in-MD 1833 tokens baseline vs 1874 patched, only-in-SVG 0 baseline vs 0 patched); accepted per D27 via 15a + native verifier + full read-through. Residuals are furniture the MD legitimately carries (level badges, instruction words, P8 key notes, footer/masthead words) that the verifier drops on the SVG side. Gate 15c native verifier PASS (ADOPT). D18 masthead gap 42.0px PASS. Logs: `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-nl/gates.log` + `GATES-SUMMARY.txt`; D5 report: `production/notes/2026-w43/g-zh-tw/scratch-d5-rebuild-zh-tw/D5-REPORT-2026-w43-zh-tw-nl.md`.
- **text.md provenance:** joined patched export `scratch-2026-w43-zh-tw/logs/2026-w43-zh-tw-nl/2026-w43-zh-tw-nl.text.md.new` (D5-aware joiner `scripts/textexp_zh_tw_d5.py`; the naive exporter fragments D5 run-split lines — see family report §4). issues/ holds no `.text.md` for this edition; this file ships new with the bundle (carry-over exception).
