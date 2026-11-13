# 校对笔记 — 2026-W47 日文→法文版 `2026-w47-ja-fr` · 第一轮独立复校

- 校对员：叶子（第一轮，独立复校；未改任何源码/成品）
- 日期：2026-11-11
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-fr/`
- 结论：**(b) 缺陷清单 — 2 条缺陷（D1、D2），均在 P8 法文答案注释里，属同一类：力士四股名罗马字误读。** 其余全量检查零问题。按 SOP §8.4，须修后整期重渲染、再做一轮全量复校至零问题，方可定稿。

## 身份复核（先核身份，通过）

| 文件 | 字节 | SHA-256（自行算出，完整串） | 与 KIT 比对 |
|---|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-FR.pdf` | 28,347,993 | `5903a36b47668d91c04dafb047f94022299f8f5308647696fe7cff9c47244517` | 与 KIT §8 一致 |
| 网页 PDF `Lucerna-VOL4-JA-FR-web.pdf` | 4,458,579 | `99fd99aff8f1a8289ae58435efc0a85e04b36e79d1a09ce7d700493e3658c47c` | 与 KIT §8 一致 |

开工探针双通：`git hash-object -w` 成功；`hidden_files/w47/` 写盘成功。
构建解释器：`tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0），即 SOP/AGENTS 规定的解释器；freeze 重跑即用此解释器。

## 缺陷清单

### D1（中）— P8 答案注释：藤凌駕的罗马字误读，5 处

- 位置：P8 答案区 — 第113–150题答案行，具体为 key 49、54、63、111、116。
- 原文（5 处，均在 P8 SVG `p8-tesuto.svg` 及印刷/网页 PDF 内）：
  - key 49：`49. A — Fujiryūga a battu Hōshōryū au jour 3`
  - key 54：`54. 11 — Kinboshi de Fujiryūga : 11e tournoi depuis le début`
  - key 63：`63. ○ — Fujiryūga a gagné un kinboshi au jour 3`
  - key 111：`111. 11 — Kinboshi de Fujiryūga : 11e tournoi depuis le début`
  - key 116：`116. A — Hōshōryū a perdu contre Fujiryūga au jour 3`
- 应为：`Fujiryūga` → **`Fujiryōga`**（5 处同改）。藤凌駕的官方读法是「ふじりょうが」。
- 证据（公开来源，三方一致）：
  - 日刊体育 2025-10-01：「藤凌駕（ふじりょうが、22＝藤島）」
  - sumo-guide.com 力士名鑑：「藤凌駕 雅治（ふじりょうが まさはる）」
  - ozumo.jp（引日本相扑协会官方 profile）：「藤凌駕雅治（ふじりょうが まさはる）」
  - 注：凌駕读 `ryōga`（りょうが），不是 `ryūga`（りゅうが）。
- 严重度：中。日文正文（藤凌駕）无误，胜负事实（第3日胜豊昇龍、初金星、初土俵起第11场所、年6场所制第7速）全部正确；错在法文注释里真人姓名的罗马字拼写，5 处连带。
- 附：该拼写与 ja-en、ja-de 姊妹版 `text.md` 里的写法逐字相同（各 5 处），疑为上游共用罗马字表带入；修时须核查共用表，勿只改法文一版。

### D2（中）— P8 答案注释：美ノ海的罗马字误读，1 处

- 位置：P8 答案区 key 48。
- 原文：`48. B — Umi-no-umi a perdu contre Hōshōryū le jour 1`
- 应为：`Umi-no-umi` → **`Chura-no-umi`**。美ノ海的官方读法是「ちゅらのうみ」。
- 证据（公开来源，三方一致）：
  - 日刊体育 2018-05-30：「美ノ海（ちゅらのうみ）」
  - sumo-guide.com 力士名鑑：「美ノ海 義久（ちゅらのうみ よしひさ）」
  - rokepan 维基风经歴：「美ノ海義久（ちゅらのうみ よしひさ）」
  - 注：`Umi-no-umi` 对应的是「海ノ海」，美（み/ちゅら）从不读 `umi`。
- 严重度：中。日文正文（美ノ海）与胜负事实（初日负于豊昇龍）无误；错在法文注释里真人姓名的罗马字。
- 附：与 ja-en、ja-de 姊妹版 `text.md` 里的写法逐字相同（各 1 处），疑为上游共用罗马字表带入；同 D1 一并核查。

## 已核实无问题的项目（抽样以外的全量核查均已做）

1. **8 版印刷版逐版目视**：从印刷 PDF 重新渲染（110 dpi，`render-print/p-1.png` … `p-8.png`，非 builder 卡片），8 版全读；网页 P1/P8 从 web PDF 重新渲染并目视。无溢出、无重叠、无截断、无压页脚（机械门 occlusion 0 flags 佐证）。
2. **150 题逐题验算**：登记表（重跑 `run.py`）150 题，A2 48 / B1 73 / B2 29，分版 10/18/18/18/18/18/12/38，题型 Compléter 50 / Choix multiple 51 / Associer 12 / Former une phrase 8 / Vrai ou faux ? 11 / Texte à trous 13 / Traduire 4 / Rédaction 1，范文 154 字——与 KIT 登记逐项一致；150 个键逐一对照题面与正文验算（相扑 47–64、图表 88–93 含 38−24=14、38+24=62、38+24+22+16=100、红叶 83–100、P8 113–150 全部核对），除 D1/D2 的罗马字外键值全对；题号 1–150 连续无缺重（SVG 题干扫描：150 个唯一号，无缺失）。
3. **金句 8 条**：日文逐字与核心一致，并经去空白归一化核对逐条真实出现在正文所标页码（p.1 ×3、p.2 ×2、p.3、p.4、p.7）；法文 gloss 忠实。
4. **禁词/红线**：无国际政治；英文选题规则不适用（本版目标语为日语）；VOL.4 ×10（刊头/标题/页脚），VOL.3 ×1（P4 冻结正文「前号（VOL.3）」），VOL.5 ×4（P4 冻结正文「次号（VOL.5）」+ P7 法文读者园地 ×2 + P7 预告），无 VOL.2；`·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；`Page N sur 8` 每版 1×；刊头 196px 仅 P1。
5. **徽章**：141 枚 chip（A2 45 / B1 70 / B2 26），逐页 P1 10×A2、P2 15×A2、P3 7×A2+8×B1、P4 18×B1、P5 18×B1、P6 18×B2、P7 4+4+4、P8 9×A2+22×B1+4×B2；fill 与文字逐一配对，0 错配；逐页计数与核心版完全一致（见观察 O5）。
6. **P8 字号**：PyMuPDF 实测 P8 最小 9.975pt（≥9.75pt 门槛），次档 10.35pt（题干，79 spans）未动。
7. **翻译层专项**：
   - 讲解/界面语言确为法文（页脚、栏头、练习标签、答案头、图注 `Photo :` 全法文）。
   - 核心 221 键字面量：fr 与 core 的 SVG 文本行全量差分——fr-only 行 379、core-only 行 358；fr-only 行中含 CJK 的 92 行全部是「日文冻结头 + 法文」的混合行，且全部 CJK 词串逐字存在于核心（新增 CJK 词串 0 个）；core-only 行中无 CJK 的仅 1 行（图注换行残片 `Commons）`，属排版断行差异。
   - 无中文残留：`译注` / `参考答案` / `酉之市` / `提名` / `吉伊卡哇` 全部 0×；410 个 distinct CJK 词串逐项过目，均为日语词汇（相扑、酉の市、红叶、ボジョレー等）；`Chiikawa` ×4、`ryuuryuu` ×5。
   - 练习小节头冻结为日语：`A 理解`、`B ことば`、`C 文を作りましょう`、`D ペアにしましょう`、`E 翻訳しましょう` 等（P1–P8）全为日语；题型标签为法文（Compléter、Choix multiple、Texte à trous、Associer、Former une phrase、Vrai ou faux ?、Traduire、Rédaction）。
   - E 组答案键 137–140：已逐条核实——137 `Ni-no-tori, c'est le 19 novembre.` ← 二之酉在11月19日；138 `Le vin nouveau sort le 19 novembre.` ← 新酒在11月19日解禁；139 `Nominations des mots à la mode : 5 novembre.` ← 流行语提名在11月5日发表；140 `Qui veut voir les feuilles doit vérifier à la fois les dates prévues et la situation actuelle.` ← 去看红叶的人应该同时确认预报日期和现在的状况。日期与事实全保留，keydiff 恰为 [137,138,139,140]，status CLEAN。
   - ちいかわ：正文用假名 `ちいかわ`（与核心一致），法文层用 `Chiikawa`，无中文 `吉伊卡哇`；りくりゅう：法文层用 romaji `ryuuryuu`。
   - 日期/星期经日历核验：11月16日（月）、19日（木）、22日（日）、5日（木）、8日（日）、23日（月）、12月1日（火）全部正确；ボジョレー解禁日为 11 月第 3 木曜日 = 19 日，正确；相扑事实与 2026-11-10 当日公开报道（日刊体育、スポーツ報知）一致：藤凌駕第 3 日胜豊昇龍获初金星、初土俵起第 11 场所、年 6 场所制第 7 速。
8. **U+2019 回归**：8 个 SVG 中 U+2019 总数 0；撇号均为 U+0027（×51）；含撇号的行（`Jeudi, c'est Ni-no-tori`、`la fin de l'année`、`des saveurs d'automne` 等）目视无宽字形断裂。法文弯引号 « » 未使用（0×），不混淆。
9. **机械门全套自跑**（详见 GATE-LOG.md）：run.py exit 0 零溢出；freeze 8/8；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150；p8 compare CLEAN；print/web 文字层字节一致（各 47,208 字节）。

## 观察项（单独列，不计缺陷）

- **O1** — P7 诊所第 4 条法文注释：`Le verbe se termine en forme ます.` 措辞略拗（地道写法为 `Le verbe se termine par ます`）；意思清楚，属简注口吻，列为观察。
- **O2** — P7 金句 gloss 第 6 条句首小写：`ryuuryuu est un couple de patinage artistique. (p. 7)`。小写形式本身是 fan-out 规范定的 romaji 写法（KIT §1），句首位置是其附带结果；列为观察。
- **O3** — 日文选择题选项中折行（P1 Q7 选项 B、P2 Q11 选项 B 与 Q14 选项 B、P3 Q29/Q30、P4 Q47 等；SOP §1.1 称选项不在中间折行）：已逐行核对，断行位置与核心版 SVG 文本行**逐字一致**，属核心冻结版式带入，非 fan-out 引入；列为观察（归核心）。
- **O4** — P4 正文句跨栏在词中切断：`千秋楽の結果は、次号（VOL.`（左栏末）/ `5）でお知らせします。`（中栏首）。与核心版逐行一致，属核心冻结版式；列为观察。
- **O5** — 徽章数 141 枚 vs 练习 150 题：每组 Associer（4 题）只画 1 枚 chip（P2/P3/P8 各一组，各 −3），与核心版逐页计数完全一致，属核心实现方式；列为观察。
- **O6** — Builder  scratch 证据缺失：`hidden_files/w47/scratch-fanout-ja/` 内仅有 `.probe-stick8`，任务书要求先读的 `FANOUT-REPORT-ja.md` 及 KIT §8 引用的门文件（`fr-occlusion-run5.json`、`fr-p8-run5.json`、`fr-p8compare-run5.json`、`fr-sha-run5.txt`、`fr-sha-run6.txt`、`build-fr-run6.log`、`map-fr.json`）均不在仓内。本轮全部机械门均为独立重跑，不依赖上述文件；缺失属过程缺口，列为观察。
- **O7** — P5 D 节头（`文を完成しましょう`）落在中栏底部，其题（79–82）在右栏；P2/P3/P6 中栏有大面积留白。均为模板流式排版，与核心版式一致；列为观察。
- **O8** — P2 小雪卡片 gloss（`quand la neige commence à tomber`，KIT §11 F3 的修复）目视确为一行、无溢出，修复已验证。

## 需协调员裁定的事（只报事实，不做定稿决定）

- D1、D2 修复后，须按 SOP §8 循环规则整期重渲染并再做一轮全量复校，至零问题方可定稿。
- D1、D2 的罗马字与 ja-en、ja-de 姊妹版逐字相同，疑为共用罗马字表问题；修时宜一并核查共用表与全部姊妹版，勿只改法文一版。
