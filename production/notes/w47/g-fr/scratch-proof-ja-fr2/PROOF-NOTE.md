# 校对笔记 — 2026-W47 日文→法文版 `2026-w47-ja-fr` · 第二轮独立复校

- 校对员：第二轮独立复校（与第一轮复校员、返修 builder 均不同的人；未改任何源码/成品）
- 日期：2026-11-11
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-fr/`
- 结论：**(a) 零问题 — 全量复校零缺陷，可定稿。** fix1 的 6 处改动全部改对；其余全量检查零问题。
- 依据：SOP.md 全文（仓内正本）+ 协调员 brief 已读；第一轮复校笔记与 fix1 的 FIX-LOG/GATE-LOG 只作参考，所有结论均为本轮独立重核。
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ja-fr2/`（PROOF-NOTE.md、GATE-LOG.md、logs、JSONs、renders）

## 身份复核（先核身份，通过 — 与任务书逐字一致）

| 文件 | 字节 | SHA-256（自行算出，完整串） |
|---|---|---|
| 印刷 PDF `Lucerna-VOL4-JA-FR.pdf` | 28,348,000 | `1f3b28f4eae5b23c57bf6dac67b976d8e167efd09825ebdcdc10fa9bb9f2fdcb` |
| 网页 PDF `Lucerna-VOL4-JA-FR-web.pdf` | 4,458,587 | `4f02e8c8f9dec50844906ec8c43e0e13520aa98897a49a14685468c6f6dd2b8b` |
| text.md `2026-w47-ja-fr.text.md` | 46,882 | （导出重跑字节一致，见 GATE-LOG §9） |

开工探针双通：`git hash-object -w` 成功（`da0c4eb8…`）；goals scratch 写盘成功。
构建解释器：`tools/venv/bin/python`（Python 3.12.3，PyMuPDF 2.1），即 SOP/AGENTS 规定的解释器。
未做任何 git 写操作，未改 core-ja、其他家庭、tools/、issues/；未跑 insert.py、lint --write。工作树中该版目录为 `??` 未跟踪新目录（与开工前状态一致，本轮未动）。

## 回归核查 — fix1 的 6 处（D1/D2），全部改对

### 旧拼写残留

| 范围 | `Fujiryūga` | `Umi-no-umi` |
|---|---|---|
| content*.py（content34/7/8） | 0 | 0 |
| svg/（8 个 SVG） | 0 | 0 |
| `2026-w47-ja-fr.text.md` | 0 | 0 |
| WEEKLY-KIT.md / EDITION-RECORD.md | 有（见 O9） | 有（见 O9） |

KIT 与 EDITION-RECORD 里的命中全部是返修记录中的「改前 → 改后」引文（`Fujiryūga` → `Fujiryōga` 等），属有意记录，非残留。

### 新拼写（P8 SVG 原文逐字抄录）

- `48. B — Chura-no-umi a perdu contre Hōshōryū le jour 1`
- `49. A — Fujiryōga a battu Hōshōryū au jour 3`
- `54. 11 — Kinboshi de Fujiryōga : 11e tournoi depuis le début`
- `63. ○ — Fujiryōga a gagné un kinboshi au jour 3`
- `111. 11 — Kinboshi de Fujiryōga : 11e tournoi depuis le début`
- `116. A — Hōshōryū a perdu contre Fujiryōga au jour 3`

P8 SVG：`Fujiryōga` ×5、`Chura-no-umi` ×1；text.md 同样 5+1。印刷版与网页版 P8 均 200 dpi 放大核实 48/49/54/63/111（116 见整版 + SVG/text.md 原文三重印证）。
答案键（第 3 参）与日文题干未动：新 p8 extract 的 150 个键值与 fix1 的 extract 逐键比对，0 差异。

### 罗马字独立核实（查公开来源，不采信 fix1 的引证）

- **藤凌駕 = ふじりょうが → Fujiryōga ✓**
  - sumo-guide.com 力士名鑑：「藤凌駕 雅治（ふじりょうが まさはる）」
  - ozumo.jp（引日本相扑协会官方 profile）：「藤凌駕雅治（ふじりょうが まさはる）」「藤凌駕は『ふじりょうが まさはる』と読み」
  - 日刊体育 2025-10-01：「五島改め藤凌駕（ふじりょうが、22＝藤島）」
  - 凌駕读 `ryōga`（りょうが），不是 `ryūga`。`Fujiryōga` 正确。
- **美ノ海 = ちゅらのうみ → Chura-no-umi ✓**
  - 日刊体育 2018-05-30：「美ノ海（ちゅらのうみ）」「木崎改め美ノ海（ちゅらのうみ、25＝木瀬）」
  - 日刊体育 2019-09-22：「美ノ海（ちゅらのうみ、26＝木瀬）」
  - 美读 `chura`（ちゅら，冲绳语「美」），从不读 `umi`；`Umi-no-umi` 对应的是「海ノ海」。`Chura-no-umi` 正确（与 es/pt 姊妹版形式一致）。

## 已核实无问题的项目（全量核查，非抽样）

1. **8 版印刷版逐版目视**：印刷 PDF 自渲染（110 dpi，`render-print/p-1.png` … `p-8.png`），8 版全读；网页 P1/P8 自渲染并目视。无溢出、无重叠、无截断、无压页脚；网页版与印刷版版式一致、无豆腐块。P8 答案区另做 200 dpi 放大核实（`p8-ans-col1.png`、`p8-ans-col3.png`、`p8-ans-bottom.png`、`p8-ans-115-121.png`）。
2. **150 题逐题验算**：登记表（两轮独立重跑 `run.py`）150 题，A2 48 / B1 73 / B2 29，分版 10/18/18/18/18/18/12/38，题型 Compléter 50 / Choix multiple 51 / Associer 12 / Former une phrase 8 / Vrai ou faux ? 11 / Texte à trous 13 / Traduire 4 / Rédaction 1，范文实测 154 字（150–200 字区间内）——与 KIT 登记逐项一致；150 个键逐一对照题面与正文验算（相扑 47–64、图表 88–93 含 38−24=14、38+24=62、38+24+22+16=100、红叶 83–100、P8 113–150 全部核对），键值全对；题号 1–150 连续无缺重（p8 extract 150/150 + 登记表 150 + 目视逐题；SVG 题干号扫描 138 个直接命中，缺的 12 个为 Associer 组号 25–28/43–46/141–144，以「25–28.」组头 + 组内分项形式出现，已逐一目视核对）。
3. **金句 8 条**：日文逐字与本期正文一致，页码引用（p.1 ×3、p.2 ×2、p.3、p.4、p.7）逐条核对无误；法文 gloss 忠实。
4. **翻译层专项**：
   - 讲解/界面语言确为法文（页脚、栏头、练习标签、答案头、图注 `Photo :` 全法文）。
   - 核心 1062 行 vs 法文 1082 行：fr-only 293 行、core-only 273 行；fr-only 行含 CJK 的词串经「全核心文本去空白拼接」核对，**新增 CJK 词串 0 个**（初版按行比对曾报 2 个「缺失」——出来栄え、味わう——系 SVG 换行把词切在两行所致的测量伪报，拼接核对后两者均在核心正文里：`今年の出来栄えを確かめながら`、`味わいましょう`）。
   - 无中文残留：`译注` / `参考答案` / `酉之市` / `提名` / `吉伊卡哇` 全部 0×；`Chiikawa` ×8、`ryuuryuu` ×10；其余罗马字人名逐一核对：Ōnosato、Hōshōryū、Yoshinofuji、Miura Riku、Kihara Ryuichi、Tori-no-ichi、Ni-no-tori、Ichi-no-tori、Shōsetsu 全对（svg 中 `Ura` ×12 均为 base64 图数据内的子串，非文本）。
   - E 组答案键 137–140 逐条核实：137 `Ni-no-tori, c'est le 19 novembre.`、138 `Le vin nouveau sort le 19 novembre.`、139 `Nominations des mots à la mode : 5 novembre.`、140 `Qui veut voir les feuilles doit vérifier à la fois les dates prévues et la situation actuelle.`——日期与事实全保留，keydiff 恰为 [137,138,139,140]，status CLEAN。
   - ちいかわ：正文用假名 `ちいかわ`（与核心一致），法文层用 `Chiikawa`；りくりゅう：法文层用 romaji `ryuuryuu`。
   - 日期/星期经日历核验（`date -d`，Asia/Tokyo）：11月5日（木）、7日（土）、8日（日）、13日（金）、16日（月）、19日（木）、21日（土）、22日（日）、23日（月）、12月1日（火）、10月29日（木）全部正确。
5. **事实抽查（公开来源，逐项独立核实）**：
   - 相扑九州场所 3 日目まで（スポーツ報知/スポニチ/読売/サンスポ/共同/ozumo.jp）：初日 大の里负义ノ富士（突き落とし）、豊昇龍胜美ノ海（押し出し）、琴櫻负藤凌駕、安青錦负朝乃山、霧島胜宇良、大関 3 人中 2 人败；2 日目 大の里胜藤凌駕（寄り切り）初白星、豊昇龍胜朝乃山 2 连胜、3 大関全胜；3 日目 藤凌駕胜豊昇龍（押し倒し）初金星、初土俵起第 11 场所、年 6 场所制第 7 速。全部与本版一致。`3場所連続休場明け`亦有多源佐证。
   - 酉の市 2026：一の酉 11月7日（土）、二の酉 11月19日（木），**三の酉なし**（浅草鷲神社公式「令和8年は、二の酉まで」）；浅草 0–24 时；隣寺長國寺 ✓。
   - ボジョレー：解禁日为 11 月第 3 木曜日 = 2026 年 11 月 19 日 ✓；阪神梅田本店约 40 种类（阪急阪神百貨店 PR Times 2026-11-04 官方发布）✓；日本时差最早 ✓；9 月ごろ收穫（发布称今年成熟早、收穫早）✓。
   - 流行語大賞：ノミネート 30 語 11 月 5 日发表，トップテン + 大賞 12 月 1 日（火）发表 ✓（ORICON/モデルプレス/官方一览）；本版点名的 りくりゅう、ちいかわ（現象）、酷暑日、AI暴走、NISA貧乏、好きすぎて滅！、ボンボンドロップシール（ボンドロ）全部在官方 30 语一览内 ✓；三浦璃来・木原龍一为花滑双人 ✓。
   - 紅葉：ウェザーニューズ第 3 回予想（10月29日）高尾山 11月13日ごろ、宮島 11月21日ごろ、嵐山 11月23日ごろ ✓；嵐山 11月8日時点全体约 2 割色づき、見頃 11月26日ごろ、落葉はじめ 12月12日ごろ ✓（Weathernews 嵐山 spot 页）；日本気象協会（tenki.jp）嵐山見頃 11月13日〜 ✓；日本気象株式会社第 1 回予想（9月2日）東京 11月29日ごろ、大阪 12月4日ごろ、均为平年並み ✓——与本版逐字一致。
   - 小雪 11月22日（日）、勤労感謝の日 11月23日（月・祝日）✓；花園神社熊手写真注「2025年11月24日」——2025 年二の酉确为 11 月 24 日（月），CREDITS.md 已注明非 2026 年照片 ✓；5 张图出处与 CREDITS.md 逐一相符（Poliphilo CC0、Alainauzas PD、lumoplank CC0 ×2、Mozzucu CC0）。
6. **禁词/红线**：无国际政治；英文选题规则不适用（本版目标语为日语）；VOL.4 ×10（刊头/标题/页脚），VOL.3 ×1（P4 冻结正文「前号（VOL.3）」），VOL.5 ×4（P4 冻结正文「次号（VOL.5）」+ P7 法文读者园地 ×2 + P7 预告），无 VOL.2；`·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；`Page N sur 8` 每版 1×；刊头 196px 仅 P1。
7. **徽章**：141 枚 chip（A2 45 / B1 70 / B2 26），逐页 P1 10×A2、P2 15×A2、P3 7×A2+8×B1、P4 18×B1、P5 18×B1、P6 18×B2、P7 4+4+4、P8 9×A2+22×B1+4×B2；fill 与文字逐一配对，0 错配。
8. **P8 字号**：PyMuPDF 实测 P8 最小 9.98pt（≥9.75pt 门槛），次档 10.35pt（题干）未动；尺寸分布与 fix1 逐项一致。
9. **U+2019 回归**：8 个 SVG + content*.py + text.md + KIT 全扫 U+2019 总数 0；撇号均为 U+0027（SVG 内 ×51）。
10. **ABSTRACT.txt**：法文单行 330 B，无 ASCII 双引号，含真实主题关键词（Tori-no-ichi、Ni-no-tori、Beaujolais Nouveau 19 novembre、sumo Fukuoka、30 nominations、Arashiyama Kyoto）+ A2–B2 + 150 exercices ✓。
11. **机械门全套自跑**（详见 GATE-LOG.md）：run.py 双轮 rc 0 零溢出；freeze 8/8（且与交付 SVG 字节一致）；occlusion 0 flags（自检 6 类全触发）；p8 extract 150/150；p8 compare CLEAN；print/web 文字层字节一致（`pdftotext -layout` 各 104,269 字节）；text.md 重导出字节一致。

## 缺陷清单

**无。** 本轮全量复校零缺陷。

## 观察项（单独列，不计缺陷）

- **O1** — P7 诊所第 4 条法文注释：`Le verbe se termine en forme ます.` 措辞略拗（地道写法为 `Le verbe se termine par ます`）；意思清楚，属简注口吻。列为观察（与第一轮 O1 相同，独立判断一致）。
- **O2** — P7 金句 gloss 第 6 条句首小写：`ryuuryuu est un couple de patinage artistique. (p. 7)`。小写形式本身是 fan-out 规范定的 romaji 写法（KIT §1），句首位置是其附带结果。列为观察（与第一轮 O2 相同）。
- **O3** — 日文选择题选项中折行（P1 Q7 选项 B、P2 Q11 选项 B 与 Q14 选项 B、P3 Q29/Q30、P4 Q47 等；SOP §1.1 称选项不在中间折行）：断行位置与核心版逐行一致，属核心冻结版式带入，非 fan-out 引入。列为观察（归核心）。
- **O4** — P4 正文句跨栏在词中切断：`千秋楽の結果は、次号（VOL.`（左栏末）/ `5）でお知らせします。`（中栏首）。与核心版逐行一致，属核心冻结版式；文字完整可读。列为观察。
- **O5** — 徽章数 141 枚 vs 练习 150 题：每组 Associer（4 题）只画 1 枚 chip（P2/P3/P8 各一组，各 −3），与核心版逐页计数完全一致，属核心实现方式。列为观察。
- **O6** — P5 D 节头（`文を完成しましょう`）落在中栏底部，其题（79–82）在右栏；P2/P3/P5/P6 中栏有大面积留白。均为模板流式排版，与核心版式一致。列为观察。
- **O7** — key 139 答案注为压缩译法（`Nominations des mots à la mode : 5 novembre.`，未写全 `ont été annoncées le 5 novembre`）：KIT §11 F1 已注明为限一行而批准的缩短，意思与日期完整保留。列为观察。
- **O8** — 旧拼写只以「改前 → 改后」引文形式留在 WEEKLY-KIT.md（§7、§11 F4）与 EDITION-RECORD.md 的返修记录里：有意记录，非残留。列为观察。
- **O9** — 上游：core-ja 的 WEEKLY-KIT.md §3 英文注里仍有错罗马字（`Umi-no-umi`、`Fujiryūga`）；core-ja 已冻结，不在本版范围，只报告、不改（fix1 已同报）。

## 结论

按 SOP §8.4，本轮为**一整轮全量复校零问题**，fix1 的 6 处改动全部改对且罗马字本身经独立公开来源核实正确；150 键、8 版、全部机械门、核心事实均已复核无误。**结论 (a)，可定稿。**
