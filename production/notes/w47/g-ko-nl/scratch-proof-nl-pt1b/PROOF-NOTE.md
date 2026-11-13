# PROOF-NOTE — 2026-W47 · nl → pt（荷兰语目标语 × 葡萄牙语读者）· proof1 独立复校（delta build 4）

- 版目录：`production/2026-w47/2026-w47-nl-pt/`（规范路径；delta 任务称 staging 副本已 `cp -a` 至此）
- 复校员：独立复校（proof1，与 builder / delta 员不同人）· 2026-11-11 19:33–20:00 EST
- 依据：仓库根 `SOP.md`（proofread-until-zero §8；几何遮挡扫描必过；p8 compare 必跑；讲解用读者母语；对外内容禁内部标签）+ 任务简报（delta 背景 D9/D11、box-title 59、STRADDLE 裁定规则）
- 工作区（唯一）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-pt1b/`
  （任务给定的 `scratch-proof-nl-pt1/` 已有上一轮（build 3）的 PROOF-NOTE.md / GATE-LOG.md 及全部证据，
  为保全上一轮证据，本轮用新目录 `scratch-proof-nl-pt1b`；上一轮两份报告及证据原封未动。
  唯一例外：开工探针开头误写了旧目录下的 `probe.txt`（仅探针标记文件，无证据价值），特此说明。）
- 只读生产：未改任何生产文件、未 commit、未 push、未重渲染交付 web PDF；`run.py` 只在 scratch 副本里重跑；
  全部测量均在交付的印 PDF 光栅（150 dpi，必要时 300 dpi）上做，卡片 `cards/` 只作交叉验证。

## 结论：(a) 零缺陷 — 可定稿

全量复校（全文 431 行、150 道题答案三源逐题、8 版逐页目视、事实、全部机械门、§1.1、文字层、盒标题逐一光栅复测）
未发现缺陷。上一轮（build 3 proof1）的 5 项缺陷 D1–D5 在本版逐项验证已修好、无回归；
delta 六处（D6/D7/D8/D9/D10/D11）逐项验证成立；另 4 项观察（O1–O4，不计缺陷，见末节）。

## 身份核对（三 SHA，磁盘实测，与任务一致）

| 文件 | 字节 | SHA-256（实测） | 任务给定 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-pt.pdf`（印） | 12,672,019 | `dd74de0a45556e96fdfcc216a9d249bbae577ace249bfbc256dd564ef6e5113e` | 一致 |
| `De-Lucerna-VOL4-nl-pt-web.pdf`（网） | 1,618,464 | `4e795b31f65273524128656f1a0a6064ba0f18efa93a29c191f15a2f58bf5e6b` | 一致 |
| `2026-w47-nl-pt.text.md`（文） | 47,209 | `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f` | 一致 |

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；
  scratch 真实写文件成功（`probe.txt`）。磁盘 59G 可用。TMPDIR 全程指向本 scratch 下 `tmp/`（系统 /tmp 512M 未用）。

## 上一轮缺陷逐项回归验证（D1–D5，全部修好）

### D1 ✓ 修好 — P6 框标题「VOOR OF TEGEN?　A FAVOR / CONTRA」已在盒内
- 源码 `content56.py` 标题已为 `VOOR OF TEGEN?　A FAVOR / CONTRA`（KIT §Fixes 13）。
- 实测（交付印 PDF 150 dpi 光栅，`boxtitle_scan.py` 自写，本版盒坐标重推导）：标题基线 y=785.0，
  真墨右缘 1852.2 px，盒右缘 1862.0 px，**外缘余量 +9.8 px**（内缘 right−22 余量 −12.2 px，仅为内垫线，
  非缺陷口径）。PIL 交叉：delta 同法 +11.5 px，量级一致、同为在内。
- 目视：P6 渲染图上标题完整落在奶油盒内，右侧有明显留白（`render-p6.png`）。

### D2 ✓ 修好 — P2 D 节选项 c 已缩短、在版心内
- 源码行现为 `c. eten voor Sinterklaas' paard`（`svg/p2-leven.svg` 节点 x=1473.5, y=2233, 23 pt）。
- 实测（交付 PDF 光栅）：真墨右缘 1793.92 px，右版心 1862.0 px，**余量 +68.08 px**。

### D3 ✓ 修好 — text.md「答案：」零残留
- `grep -c "答案" 2026-w47-nl-pt.text.md` = **0**；`— Resposta:` 142 处 + `(Resposta` 8 处，共 150 处，
  与题数一致。印/网 PDF 文字层亦 0 处中文。

### D4 ✓ 修好 — 练习类型标签已本地化
- text.md 内联标签全为葡语：`Completa a frase` 65、`Escolha múltipla` 44、`Cloze` 13、`Forma frases` 8、
  `Verdadeiro ou falso` 7、`Traduzir` 4、`Relaciona as palavras` 2、`Escrita` 1（144 实例覆盖 150 题，配对题共用）。
- 尾标 `[Complete]` ×59 是葡语 vous-命令式（completar），非英文残留：与 es `Completar` ×59、it `Completa` 对位，
  其余尾标均为葡语（`Forme a frase` ×8、`Verdadeiro ou falso?` ×7、`Traduzir para português/neerlandês` 各 ×2、`Escreva` ×1）。
- SVG 可见文本中英文类型词 0 处：`translate` 的 2 处命中均为 `<g transform="translate(512 0)…">` 属性，
  非文本；`choice/matching/writing/true or false` 0 处。

### D5 ✓ 修好 — 网 PDF 斜体已恢复
- PyMuPDF 全书 span 扫描：印版 italic span **1 处**（P1 «de groepswinst»，Newsreader Italic 16.12 pt），
  网版 italic span **1 处**（同词，`LucernaNewsreader-Italic` 16.12 pt）。印版 = 网版 = 1。

## Delta 六处逐项验证（D6/D7/D8/D9/D10/D11）

- **D6**（P3 桥接 `w=464.7`，`content34.py:78`）：p3 SVG 与 build-3 staging **字节一致**；
  桥接仍 2 行逐字相同（`Completa no pretérito perfeito. Atenção aos` / `auxiliares hebben/zijn.`），无孤儿标点。
- **D7**（P7 桥接 `w=423.95`，`content7.py:19`）：p7 SVG 与 build-3 staging **字节一致**；
  桥接仍 3 行逐字相同，末行 `scoren marcar.`。
- **D8**（P6 图注 `capcn_w=378.1`，`content56.py:143–144,159`）：p6 SVG 与 build-3 staging **字节一致**；
  图注仍 4 行，基线 635.02/659.44/683.86/708.28 全不变，无行首标点。
- **D10**（P7 来信 `dt_zh_w=401.45`，`content7.py:91–92,103`）：p7 SVG 字节一致（同上）；
  来信仍 2 行逐字相同，无行首标点。
- **D9**（Q140 键补 `kort`，`content8.py:75`）：**三源逐字一致** —
  registry 键 = text.md:415 答案 = P8 SVG 节点（y=2221.54），均为
  `Ik maak een surprise met een kort gedicht.`；题干 `Faço uma surprise com um poema curto.` 保留 `curto`（“小”未删），
  键/题干一致；其余 149 键未动（三源比对 149/149 MATCH，见机械门 §7）。
  注：`kort` 的语义支撑在正文本身：P2 正文 `DRIE DINGEN` “Twee: schrijf een gedicht — kort is ook goed.”
  （text.md P2 节）与核心 text.md:73 同句。
- **D11**（P4 HET PROGRAMMA 盒，`content34.py:130` 顶留 62→89，`sh` 611.0→638.0）：
  盒 `<rect x=1439.5 y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，**基线余量 +20.11 px**；
  交付 PDF 150 dpi 光栅：末行最低墨迹 y=1209.60，**墨迹余量 +20.00 px（≥20 px）**；
  盒底下 7 px 条带 **0 非纸像素**；裁切图 `crop-p4-d11.png` 目视：末行在盒内、下有明显留白。
  P3 同型盒交叉核查：末行墨迹余量 +16.04 px，无溢出。

## 全量复校（独立重做，非沿用上一轮结论）

1. **全量 proofread**：text.md 全文 431 行逐行精读 + 印 PDF 文字层（`print.txt` 104,925 B）逐页核对。
   荷兰语拼写/变位/性数/标点未见错误；葡萄牙语讲解层无英文/中文残留（CJK 仅 U+3000 全角空格分隔符，
   见 freeze diff）；6 条 gloss 行共 29 个注释词逐词核查，全部真实出现在正文里（`content-verify.log`，
   缺失 0；另 8 条金句行亦一并核查通过）；交叉引用正确（IN HET KORT ORANJE·P.4 / SINTERKLAAS·P.3 / EREDIVISIE·P.4；
   P2 “Meer over de intocht lees je op pagina 3”；P1 目录 7 行与各版真实标题对应，Pag. 2–8 页码正确；
   P2 EN JIJ “VOL.5 (pagina 7, «Brieven van lezers»)”）；级别徽章（P1 A2、P2 A2、P3 A2→B1、P4 B1、P5 B1、
   P6 B2、P7 A2/B1/B2、P8 分级）正确。
2. **150 道题答案逐题复核**：registry 键 × P8 印刷键 × text.md 答案三源程序比对 **149/149 MATCH**
  （`keycheck.py` / `keycheck.log`；Q150 为开放写作题例外：印刷键 `✓`，text.md 载 81 词范文，
   registry 为 `(tarefa aberta, texto modelo abaixo)`，语义相同）；配对键 25–28 = d/c/a/b、
   141–144 = b/c/d/a，与印刷版 a–d 列表逐项核对一致；范文实测 **81 词**（80–100 内）。
   语义逐题手验：算术重算 19 天（16 Nov→5 Dec）、1 天、4 小时、17 年（2009→2026）、65（35+30）、
   100（35+30+20+15）全对；13 天（22 Nov→5 Dec）对；Q131 B（wortel + verlanglijstje）对原文重算正确；
   编号 1–150 连续无缺重；分布 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31。
3. **8 版逐版看图**：交付印 PDF 每页 150 dpi 渲染（`render-p1.png` … `render-p8.png`）逐版目视：
   无溢出、无重叠、无压页脚；7 张照片 + P6 程序图表均在位，图注与出处完整
   （P1 Westertoren / Wim van Rossem–Anefo CC0；P2 sint-oud / Anefo CC0；P3 gracht / W. Punt–Anefo CC0；
   P4 elftal 1912 / Spaarnestad 公版；P5 strand / Elise Iovenko CC0；P7 boeken / Cristina Gottardi CC0；
   P8 pen / Aaron Burden CC0；与 KIT §5 及 `assets/CREDITS.md` 一致）。
   P6 图表明确双语标注为虚构练习数据（OEFENDATA — verzonnen cijfers… / Dados de prática: números inventados…）。
   P1 主头条 “Vanavond in Berlijn: Oranje tegen Duitsland” 去空白 38 字符 ≤ 56 ✓。
   **8 条金句逐字核对**：全部逐字出自本期正文，页码标注全部正确（P1×2、P2、P3、P4、P5、P6×2）。
4. **事实核查**：本周文本与 build-3 staging 逐字节一致的部分（除 P4/P8 SVG 与 text.md:415 外全部相同，
   见 §5）沿用上一轮已验证的事实（2026-11-11 外部核实：Nations League A2 积分榜 NED/GRE 8 分、
   PSV 26 分、Heerenveen–Feyenoord 5–3、Grave/阿姆斯特丹入城 88 届、欧战下期预告 Real Madrid–PSV /
   Feyenoord–FC Porto 24 Nov、Feyenoord–Ajax 29 Nov）；日期/星期复核：14/11 周六、15/11 周日、16/11 周一、
   21/11 周六、22/11 周日、24/11 周二、29/11 周日、5/12 周六——与核心 proof2 的日历核验一致，无矛盾。
   本轮新增事实点（Q140 `kort`）见 D9，语义由正文直接支撑。读者园地：无真实来信，按 F-MAIL 规则刊登
   标注 “voorbeeldbrief van de redactie” 的示例信 + 荷/葡双语截稿说明 + 顺延 VOL.5 承诺，合规。
5. **机械门槛（独立重跑，详见 GATE-LOG.md）**：run.py clean-copy 重跑 exit 0、TOTAL 150、0 溢出警告、
   SVG 8/8 字节一致；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150、compare CLEAN、
   keydiff [137, 138]（翻译题合法重定向，键本身正确）；freeze 核心 baseline 8/8 + diff 新增 CJK 仅 7 个 U+3000；
   印/网文字层逐页 posdiff 0（P1 仅 2 处 0.2 pt 提取舍入，词序相同）、msdiff 0；P8 最小字号 10.12 pt；
   盒标题 59 个逐一光栅复测，仅 O1 一处 ±1 px 边缘（见观察项）。
6. **§1.1 独立核实**：纸色 `#fbfaf6` 全页底 8/8；调色板外 fill 0（仅刊头蛾标品牌色 #34483A/#4D72B4/#D7B257 等，
   SOP §1.1 刊头本身规定）；无金色 `#b3a06a`；无双线外框（stroked rect 0）；无近黑底（最深背景书衣绿 #37402f）；
   拉丁正文 Newsreader 971 节点；刊头/页脚/分隔用全角空格；VOL.5 = 5 = 核心；“VOL. 4” 0 次。
7. **ABSTRACT.txt**：320 字节、单行、无 ASCII 双引号、葡萄牙语读者母语，含刊名、目标语名、A2–B2、150 题与
   本期真实主题（Sinterklaas、Pakjesavond、荷兰–德国、Expeditie Robinson）。
8. **.text.md 导出**：47,209 字节、431 行，题号 1–150 连续无缺重，金句 8 条，gloss 6 条，无答案块外家具残留；
   导出头 `# De Lucerna · Semanário neerlandês VOL.4 · 2026-W47` ✓。
   与 build-3 staging text.md 的 diff **仅 415 行**（D9 `kort` 一处），其余 430 行逐字节相同。
   SVG 与 build-3 staging 的 diff **仅 p4-sport.svg（D11）与 p8-toets.svg（D9）**，其余 6 页字节一致。

## 观察事项（不计缺陷）

- **O1**：P7「HET WOORD　PALAVRA DA SEMANA」标题右缘 ±1 px 边缘（基线 y=1071.5，23 pt，
  盒右缘 1862.0，奶油盒为无边框 fill-only）：
  交付 PDF 光栅（MuPDF 150 dpi 与 300 dpi 双法一致）：solid 墨（<128）最右 1862.96 px，**−0.96 px**；
  PIL `getbbox`（Noto Sans CJK SC Bold，`/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc` index 2，
  4× 采样）：墨右 1861.25 px，**+0.75 px**；advance 宽 399.58 px，右缘 1861.08 px。
  两法在 ±1 px 内分歧，属光栅化抗锯齿边缘口径差异。裁决（按任务 STRADDLE 规则）：
  字形**未被裁切**（末字 “A” 完整，`crop-p7-title.png` 目视确认）、墨迹**未与任何元素或可见边框重叠**
  （盒无边框线；右缘外 1 px 处只有白纸）、与备份旧版（build-3 staging）**无不同**——
  两版 P7 在 300 dpi 下光栅**逐像素相同**（`p7-staging-compare.log`），几何与上一轮 proof1 已裁定的 O3 完全相同。
  故记观察项，不判缺陷。建议：下次重排该标题时留 ≥2 px 余量即可消除口径争议（非本次门禁条件）。
- **O2**：P1「HET WOORD VAN DE WEEK」葡语 gloss 次行「direto aos quartos de final.」落在全幅分隔线
  （y=1853）之下（首行基线 1846.2、次行基线 1871.85；线两侧各约 5 px，文字不触线、不跨线）。
  与 build-3 O2 同几何、同裁决，不计缺陷。
- **O3**：P2/P5「EN JIJ?」奶油盒末行紧但在内：P2 末行基线 1440.2，盒底 1447.8，基线余量 +7.6 px、
  desc-clear +1.6，像素墨底余量 **+3.32 px**（build-3 为 +0.9 px；re-fanout fix15 +2 px 底垫已见效），
  盒底下 7 px 条带 0 非纸像素；P5 末行基线 988.8，盒底 994.5，基线余量 +5.7 px、desc-clear −0.3（估计值），
  像素墨底余量 **+5.70 px**，条带 0 非纸像素。均在内，不计缺陷。
  P3 SINTERKLAAS 盒末行墨底余量 +16.04 px；P7 toolbox 三盒墨底余量 +13.10 / +13.14 / +24.92 px，
  条带均为 0 非纸像素。
- **O4**（排版一致性，极轻微）：P8 答案区配对题注 142/144 用紧凑写法 `groepswinst=vitória do grupo c` /
  `gedicht=poema a`，而 141/143 用 spaced 写法 `journaal = noticiário b` / `schoen = sapato d`。
  紧凑写法继承自核心 `content8.py:85`（`["journaal=新闻节目 b", "groepswinst=小组头名 c", …]`）的既定记法，
  两种写法均无歧义、无错误，不计缺陷；建议下次统一为空格写法（非本次门禁条件）。

## 判为非缺陷的项（摘要，详见 GATE-LOG）

- 几何遮挡审计 0 flags（自检通过）；creambox 全版扫描仅 2 处负 clearance，均为盒下相邻标题的已知假阳性
  （+24/+32 px 窗口内下一标题）；P7 toolbox min clearance +13.1、min desc-clear +7.1。
- P8「A　VUL DE KRONIEK IN」标题（`content8.py:15`，21 pt，基线 y=201）：交付 PDF 光栅实测墨迹 x 87.7–320.6，
  外缘余量 **+189.9 px**（栏边 510.5）；下划线 y=214 按设计止于栏边；刊头带底 182 与字顶无交叠
  （`crop-p8-ahead.png` 目视确认）；与 nl-ko 版同标题的 −26.5 px 情形在本版**未复现**。
  （注：扫描带若取基线 −27.3 px 会误触 y≈177 的刊头带——本轮扫描已按 `bslib4.py:72` 下划线几何与刊头带底
  182 px 修正带区，误报已排除。）
- freeze diff 新增 CJK 仅 7 个 U+3000（SOP §1.1 规定的全角空格分隔符，非中文）；移除串孤儿仅两项，
  均已裁定：（a）刊头「LUCERNA DUTCH WEEKLY」→ 葡语刊头副标（fan-out 设计）；（b）「perfectum」→ 葡语
  「perfeito」（P8 答案注 40/42），讲解层合法翻译。
- p8 compare CLEAN，keydiff [137, 138] 为翻译题合法重定向（137「As notícias do Sinterklaas passam
  todos os dias às 18:00.」；138「Os dois primeiros passam aos quartos de final.」）；139、140（葡→荷）
  键与核心一致。P8 extract 150/150。
- P8 最小字号实测 10.12 pt（SOP §1.1 让步阶梯允许 ≥9.75 pt），合规，非缺陷。
- 弯引号：SVG 全版 « » 成对（P1 2/2、P2 2/2、P7 30/30、P8 2/2）；text.md 直引号全为荷兰语 `'s` 属格，
  与核心一致。孤儿标点横扫：1618 个文本节点，独行标点 0、行首标点 0。

## 未改动声明

全程只读生产：未修改 `production/2026-w47/2026-w47-nl-pt/` 内任何文件与 `tools/`；未跑 insert.py、
lint --write、git push/add/reset/stash；未提交任何东西；未碰 W43/W45/W46 与其他版。
`run.py` 与 registry 导出只在 scratch 副本 `work/ed/` 里跑。校对产物仅在
`hidden_files/w47/scratch-proof-nl-pt1b/`（`PROOF-NOTE.md`、`GATE-LOG.md`、`probe.txt`、
`delivered-svg-sha.txt`、`core-svg-sha.txt`、`repro-run.log`、`repro-compare.txt`、`occlusion.log`、
`occlusion.json`、`p8-extract.log`、`p8-extract.json`、`p8-compare.log`、`p8-compare.json`、
`freeze-baseline/`、`freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`、`print.txt`、`web.txt`、
`textlayer.log`、`p1-posdiff.log`、`boxtitle_scan.py`、`boxtitle.log`、`boxtitle2.log`、
`p7-adjudicate.log`、`p7-staging-compare.log`、`raster-checks.log`、`strip-probe.log`、
`creambox-all.log`、`orphan.log`、`style11.log`、`content-verify.log`、`keycheck.py`、`keycheck.log`、
`reg-dump.json`、`reg-run.log`、`render-p1.png`…`render-p8.png`、`render-p7-300dpi.png`、
`cur-p7-300dpi.png`、`stg-p7-300dpi.png`、`crop-p7-title.png`、`crop-p4-d11.png`、`crop-p8-ahead.png`、
`work/`、`tmp/`）。写文件过程无 EPERM/EDQUOT 失败。
注：工作树本身有 506 处他人在跑的线的未提交改动（W43 风格线、nl 家族等），与本轮无关，本轮未新增任何改动。
