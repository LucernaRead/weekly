# 校对笔记 — 2026-W47 ja-de（第二轮独立复校）

- 校对员：叶子（第二轮，与 ja-de builder、ja-de fix1 builder、ja 核心 builder、ja-de 第一轮复校员不同人）
- 日期：2026-11-11（EST 02:44 开工）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-de/`（未入仓，未追踪）
- 依据：SOP.md §8、§1.1；AGENTS.md；KIT（`WEEKLY-KIT.md`，含 §8a 返修节）；第一轮复校 PROOF-NOTE.md（D1/D2/D3）；fix1 FIX-LOG.md；core `2026-w47-ja-zh-cn` 全文逐行对照
- 结论：**(a) 零问题，可定稿**。按 SOP §8.4，本轮为返修后从头全量复校，一整轮零问题。

## 0. 身份复核（先核身份，通过）

| 文件 | 字节 | SHA-256 | 结果 |
|---|---|---|---|
| `Lucerna-VOL4-JA-DE.pdf`（印刷） | 29,102,625 | `2047035bdaa9f9ba82d4f2a6d2b5d7c4461e1442070ed5abacbe86d930001f39` | 与 KIT §8a 登记逐字一致；与 fix1 称的值一致 |
| `Lucerna-VOL4-JA-DE-web.pdf`（网页） | 4,483,728 | `8db59bf122c73d895e9fe0d58da7e9f283f11ed1e76bc45aeb2be9a268a98f26` | 与 KIT §8a 登记逐字一致；与 fix1 称的值一致 |

- 两 PDF 各 8 页，1462.5 × 2025 pt。旧版值（印刷 29,102,629 / `b5d66e17…`、网页 4,483,732 / `c55dd68c…`）已被新版取代，不再出现。
- 开工探针双通：`git hash-object -w --stdin` 成功（`da0c4eb8…`）；`scratch-proof-ja-de2/.probe` 真实写盘成功。
- SVG 身份旁证：原 SVG sha256 中 p1–p6 与第一轮 GATE-LOG 记录逐个一致；p7 `3493886b3c75364682e2b630b821399750d12344b8e40989654757fa6c4bc505`、p8 `021ed40fe1098cc68805757cdd4bac08445771a84b731c34f04c4df382003cb5` 与 KIT §8a 登记的新 p7/p8 值一致——与 fix1 所称“仅 p7/p8 变”一致。

## 1. D1/D2/D3 回归（逐处核实，全部已改对）

全版 grep（svg 8 个 + `2026-w47-ja-de.text.md` + `content*.py`）：

| 串 | 残留 | 改后形式 | 出现位置与次数 |
|---|---|---|---|
| `Fujiryūga`（含属格 `Fujiryūgas`） | **0** | `Fujiryōga` / `Fujiryōgas` | 共 15× = svg p8 5×、text.md 5×、content 文件 5×（content34.py:190/202/224、content7.py:57、content8.py:22） |
| `Umi-no-umi` | **0** | `Churanoumi` | 共 3× = svg p8 1×、text.md 1×、content34.py:188 |
| `im ます-Form` | **0** | `in der ます-Form` | 共 3× = svg p7 1×、text.md 1×、content7.py:69 |

- 5 处 D1 逐处核对：key 49 `Fujiryōga schlug Hōshōryū an Tag 3`、key 54 `Fujiryōgas kinboshi: 11. Turnier seit dem Debüt`、key 63 `Fujiryōga holte an Tag 3 einen kinboshi`、key 111 `Fujiryōgas kinboshi: 11. Turnier seit dem Debüt`、key 116 `Hōshōryū verlor an Tag 3 gegen Fujiryōga`——P8 渲染图目视确认拼写正确。
- D2 key 48：`Churanoumi verlor an Tag 1 gegen Hōshōryū`，P8 渲染图目视确认。
- D3 P7 诊所第 4 条：`Das Verb in der ます-Form beenden.`，P7 渲染图目视确认；全版其余 `im`（`im November` / `im September` / `im Fukuoka Kokusai Center`）仍为阳/中性、正确。
- 新旧 SVG 文本 diff（fix1 称仅 p7/p8 变）：本轮实测 p1–p6 sha 与第一轮记录完全一致，独立佐证。

## 2. P8 注文人名人工逐条核对公开来源（compare 只比键值，不比注文散文）

P8 答案区 150 条注文全部读出（见 GATE-LOG §6），含人名的注文逐条核对如下。键值本身（A/B/C/数字/○×）已由 p8 compare 覆盖，本节只核人名与人名所带事实。

| 人名（注文） | 公开来源核实 | 结论 |
|---|---|---|
| Yoshinofuji（key 47、115）義ノ富士 | tachiai.org 初日战报：`Yoshinofuji defeated Onosato… Tsukiotoshi`；ABEMA 初日 `大の里●－○義ノ富士` | ✓ 初日胜大の里属实；罗马字 Yoshinofuji 正确 |
| Ōnosato（key 47、52、61、115、124）大の里 | 同上；横纲，大の里 | ✓ |
| Churanoumi（key 48）美ノ海 | tachiai.org 初日战报：`Hoshoryu defeated Churanoumi… Oshidashi`；美ノ海●－○豊昇龍；SumoTalk 标题 `Hoshoryu Returns From Three Absences With a Day 1 Win Over Churanoumi` | ✓ 初日败给豊昇龍属实；读法 Churanoumi（ちゅらのうみ）正确 |
| Hōshōryū（key 48、49、53、60、62、116）豊昇龍 | 同上；SumoTalk `Hoshoryu Returns From Three Absences` 佐证 key 60“三场所连续休场后复出”；Sanspo 亦写“3場所連続休場明けの横綱豊昇龍” | ✓ 人名、复出事实均属实 |
| Fujiryōga（key 49、54、63、111、116）藤凌駕 | tachiai.org 3 日目战报：`Fujiryoga (2-1) defeated Hoshoryu (2-1)… Hatsu-kinboshi`；Wikipedia `Fujiryōga Masaharu`：初土俵 2025 年 3 月，生涯表 2025 年 3/5/7/9/11 月 + 2026 年 1/3/5/7/9/11 月 = 2026 年 11 月为第 11 个场所；Sanspo/日刊/報知：`初土俵から11場所3日目での初金星獲得…年6場所制となった1958年以降で史上7位の速さ` | ✓ 3 日目胜豊昇龍首获金星、第 11 场所、第 7 快三项事实全部属实；`Fujiryōga` 拼写正确（凌駕 = Ryōga） |
| Miura Riku / Kihara Ryuichi（key 80） | ISU 选手履历：Miura/Kihara 自 2019 年搭档，首对夺世锦赛/总决赛冠军的日本双人滑组合；Wikipedia `Ryuichi Kihara`：搭档 Riku Miura (since 2019)；二人合称 "Rikuryu"（りくりゅう） | ✓ “ryuuryuu 是 Miura Riku 与 Kihara Ryuichi 的双人滑组合”属实 |
| Hanshin Umeda（key 33、37，店名） | 阪急阪神百貨店 PR Times 2026-11-04：`11月19日(木)、ボージョレ・ヌーヴォ―解禁！約40種類が登場`；并称“時差の関係により世界で一番早く発売されるのが日本” | ✓ 约 40 种、11 月 19 日解禁、日本最早均属实 |
| Weathernews（key 97，机构） | Weathernews 第 3 回紅葉見頃予想（10/29）：高尾山 11/13、宮島 11/21、嵐山 11/23——与 P6 数字栏及 key 83/94/97 逐项一致 | ✓ 预报日期 10 月 29 日及三地日期属实 |
| Japan Meteorological Association（key 86，机构） | P6 正文两处：日本気象株式会社 9 月 2 日预报（东京 11 月 29 日、大阪 12 月 4 日）与日本気象協会预报（嵐山 11 月 13 日）；key 86 题干即“日本気象協会の予想では、嵐山の見頃はいつからですか” | ✓ 所指机构与日期正确（译名见观察项 O4） |
| Fukuoka Kokusai Center（key 59，场馆） | Combat Press 九州场所指南：比赛于福冈 Fukuoka Kokusai Center 举行，11 月 8–22 日 | ✓ |
| Chiikawa（key 67、106、128） | P5 正文：大热漫画『ちいかわ』；德文 `Chiikawa`，中文名 `吉伊卡哇` 全版 0× | ✓ |

## 3. 全量独立复校（与第一轮同一标准）

### 3.1 8 版印刷版逐版目视（从印刷 PDF 重新渲染，非 builder 的图）+ 网页 P1/P8

- P1：头条、导读条、Anm. 注、数字栏、练习 1–10、热搜榜、目录、词卡、枫叶图+出处、快讯、Quiz 7–10——无溢出、无重叠、无压页脚。日期 `2026年11月16日（月）～22日（日）`：16 日周一、22 日周日 ✓。
- P2：生活文、Anm. 注、数字栏、词卡 4 张（首条 gloss `Bambusrechen für florierende Geschäfte` 单行，F3 已修复）、练习 11–28——干净。`D ペアにしましょう` 节头在第 2 栏底、条目在第 3 栏，为与 P2 同构的冻结版式（第一轮 O8），非缺陷。
- P3：文化文、Beaujolais 图+出处 `Foto: Alainauzas — gemeinfrei (Wikimedia Commons)`、练习 29–46——干净。
- P4：相扑文、3 日目记录、练习 47–64——干净。题干 47/48/49 与公开战报一致（47 初日胜大の里者为義ノ富士，48 初日败给豊昇龍者为美ノ海，49 3 日目胜豊昇龍者为藤凌駕）。VOL.3 前号注 1×、VOL.5 次号预告 1× 为冻结内文。
- P5：青年文、Arashiyama 图+出处 `Foto: lumoplank — CC0 (Wikimedia Commons)`、练习 65–82——干净。
- P6：深读文、图表（京都 38% / 浅草 24% / 高尾山 22% / 家 16%，标“練習用データ — 実際の調査ではありません”）、练习 83–100——干净。
- P7：三级专栏、诊所 4 条（D3 已改对，见 §1）、金句 8 条、框架、读者园地 + 德文披露、VOL.5 预告、图+出处 `Foto: Mozzucu — CC0 (Wikimedia Commons)`——干净；teaser 末端 y=2554.62（页脚 2580，25px 余量），col3 末端 1780.62。
- P8：综合评估 113–150、写作范文（154 字）、全部答案 1–150、Arashiyama 图+出处——干净；练习流末端 y=561（底 1252），答案流末端 y=2382（底 2540，158px 余量）。
- 网页 P1/P8：与印刷版同一版式、同一文字，干净。
- 非页脚文字 y>2580：0 处（occlusion 审计亦 0 flags，见 §6）。

### 3.2 150 题逐题验算

- 登记（本次 run.py 重跑）：TOTAL 150；级别 A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；题型 Ausfüllen 50 / Auswahl 51 / Zuordnen 12 / Satz bilden 8 / Richtig/Falsch 11 / Lückentext 13 / Übersetzen 4 / Schreiben 1——与 KIT §1 逐项一致。
- `p8.py extract`：noted set 150/150；`compare` vs core：CLEAN，missing=[]、extra_count=0、uncertain=[]、**keydiff=[137, 138, 139, 140]**（与预期一致）。146 条键值与 core 字节一致。
- keydiff 4 条逐条对照 core 中文原文核实（E 组翻译题答案由中文译成德文，翻译正确）：
  - 137：core `二之酉在11月19日。` → `Ni-no-tori ist am 19. November.` ✓
  - 138：core `新酒在11月19日解禁。` → `Der neue Wein erscheint am 19. November.` ✓（“解禁”译为“上市/发售”，意思无损）
  - 139：core `流行语提名在11月5日发表。` → `Die Schlagwort-Nominierungen wurden am 5. November bekannt gegeben.` ✓
  - 140：core `去看红叶的人应该同时确认预报日期和现在的状况。` → `Wer das Herbstlaub sehen will, sollte sowohl die Prognosedaten als auch die aktuelle Lage prüfen.` ✓
- 算术验算：图表 38/24/22/16 合计 100 ✓；key 91（38−24=14）✓；key 92（38+24=62）✓；key 89/90（38/24）✓；key 93（四数合计 100）✓。
- 配对验算：25–28（熊手→b、手締め→d、一番太鼓→c、小雪→a）✓；43–46（ボジョレー・ヌーヴォー→b、解禁→d、収穫→a、屋台→c）✓；141–144（熊手→c、解禁→a、金星→d、見頃→b）与 P8 F 区选项一致 ✓。
- 题干↔答案逐段核对：1–46（P1–P3 题干与 key 逐项对过，含 21 题 `0` 时、30 题第三个周四、36/38 题 19 日/0 时）、47–64（相扑，见 §2）、65–82（流行语：66 りくりゅう=双人滑、67 ちいかわ=漫画、76 Top 10 未发表 ×、77 りくりゅう非电影名 ×）、83–100（红叶：84 题 11 月 8 日时 2 割已变色、86 题日本気象協会 11 月 13 日、94 高尾山 13 日、95 东京 29 日、96 大阪 12 月 4 日）、101–112（P7：109 题 2–1=2 胜 1 负、111/112 题金星 11 场所/第 7 快）、113–136（P8 综合：115 大の里初日败给義ノ富士、116 豊昇龍 3 日目败给藤凌駕、127 嵐山落叶 12 月 12 日）、145–149（对话补全：行き/買い/19 日/熊手/どういたしまして）——全部与题干一致。
- 范文 154 字：run.py 实数 154 字，与 P8 标注 `(154 Zeichen)` 一致，与 core 字节一致。
- 星期验算（`date -d`，Asia/Tokyo）：11 月 8 日周日、19 日周四、22 日周日、23 日周一、7 日周六、5 日周四、12 月 1 日周二、10 月 29 日周四、11 月 29 日周日、12 月 4 日周五、12 月 12 日周六、13 日周五、21 日周六、26 日周四——与版内全部断言一致。

### 3.3 金句 8 条

逐字比对 core P7：8 条日语句在本版 P7 SVG 中逐字一致；德文 gloss 与页码标注均与句子出处一致：

| 金句 | 页码标注 | 核实 |
|---|---|---|
| 「19日（木よう日）は、酉の市・二の酉です。」 | (S. 1) | ✓ P1 头条句 |
| 「同じ19日（木よう日）は、ボジョレー・ヌーヴォーの解禁日です。」 | (S. 1) | ✓ P1 头条句 |
| 「熊手は、商売繁盛の縁起物です。」 | (S. 2) | ✓ P2 正文句 |
| 「ボジョレー・ヌーヴォーは、フランスのボジョレー地方の新酒です。」 | (S. 3) | ✓ P3 正文句 |
| 「3日目まで、大の里も豊昇龍も2勝1敗です。」 | (S. 4) | ✓ P4 正文句 |
| 「『りくりゅう』は、フィギュアスケートのペアです。」 | (S. 7) | ✓ P7 B1 栏句（gloss `ryuuryuu ist ein Eiskunstlauf-Paar.` 正确） |
| 「紅葉の見頃は、京都へ移っています。」 | (S. 1) | ✓ P1 导读句 |
| 「酉の市は、11月の酉の日に開くお祭りです。」 | (S. 2) | ✓ P2 正文句 |

### 3.4 禁词扫描

- `·` 0×；旧纸色 `#f7f1e2` 0×；纸色 `#fbfaf6` 每版 1×；禁用金色 `#c9a227` 0×；ASCII 撇号 `'` 0×；U+2019 见 §5。
- §8.1 讲解词真实性：全部 `Anm.` 注释头词（解禁/夜通し/二十四節気/収穫/屋台/波乱/前号/暮らし/上げる/平地）均在其所在页正文中出现（机械核查 0 缺失）；P7 术语表 10 词（酉の市/熊手/手締め/一番太鼓/見頃/解禁/りくりゅう/ちいかわ/ノミネート/金星）均在正文中。

### 3.5 VOL、徽章、版式

- VOL.4：每版页脚 1×；P1 另有刊头/版名共 3×。VOL.3 仅 P4 前号注 1×（与 core 一致）；VOL.5 de 计 3×（P4 次号预告、P7 披露、P7 来週），core 计 4×——差 1 处是 core 披露的中文译注行（`未收到真实来信…VOL.5 将刊登…`），德文版披露为单语，无译注行可重复计数，非内容缺失（core 披露日文句 + 中文译注两行各含 1 个 VOL.5，德文版合并为一行）。
- `Seite N von 8` 每版 1×；页脚 `Lucerna　JAPANISCHE WOCHENZEITUNG VOL.4　Japanischer Text　Deutsche Erklärungen` 全 8 版一致。
- 级别徽章（`>A2< / >B1< / >B2<`，本轮独立对 core 计数）：P1 14（11/2/1）、P2 15、P3 15、P4 18、P5 18、P6 18、P7 12（4/4/4）、P8 35——**与 core 逐页完全一致**。
- P8 最小字号 9.98pt（PyMuPDF 实测，≥9.75pt 门槛；分布 9.98×162、10.35×79……与第一轮一致）；P8 题干 10.35pt 未动。各版最小字号：P1 11.62、P2 12.75、P3 11.62、P4 12.75、P5 11.62、P6 12.75、P7 11.62、P8 9.98。
- 图片出处：P1 `Foto: Poliphilo — CC0 (Wikimedia Commons)`、P3 `Foto: Alainauzas — gemeinfrei (Wikimedia Commons)`、P5/P8 `Foto: lumoplank — CC0 (Wikimedia Commons)`、P7 `Foto: Mozzucu — CC0 (Wikimedia Commons)`，均与 core 一致。
- ABSTRACT.txt 为德文单行（311 字节），含 Tori-no-ichi、Beaujolais Nouveau、Sumo、30 Nominierungen、Arashiyama、A2–B2、150 Übungen。

## 4. 翻译层专项

- 讲解/界面语言确为德文：页脚 `JAPANISCHE WOCHENZEITUNG VOL.4　Japanischer Text　Deutsche Erklärungen`；练习类型标签 `Ausfüllen / Auswahl / Lückentext / Zuordnen / Satz bilden / Richtig/Falsch / Übersetzen / Schreiben`；P8 头 `答え　Antworten — nach Seiten geordnet; einfach die Nummer suchen`；P7 披露、框架、来週预告均为德文。
- E 组中文句答案键已译成德文：key 137–140（见 §3.2），其余 146 条键值与 core 字节一致。
- 练习小节头冻结为日语：P1–P8 的 `A 理解 / B ことば / C 数字と日付 / D ペアにしましょう / 文を作りましょう / 正しい・正しくない / 文を完成しましょう / 読んで答えましょう / 週のクロニクル / 一般問題 / 書いてみましょう` 等均未动。
- 中文残留：全量扫描 `参考答案 / 酉之市 / 提名 / 吉伊卡哇 / 中文 / 中国 / 练习 / 答案 / 解释 / 单词 / 语法 / 阅读` 在 SVG 与 text.md 中均为 0×；更强的字符集核查：de 文本引入的汉字集合 − core 汉字集合 = **空集**；`吉伊卡哇` 0×，`Chiikawa` 共 8×（svg 4× + text 4×），`ryuuryuu` 共 10×（svg 5× + text 5×）。
- core↔de 全量 diff：150 个差异块，全部为讲解层（中文→德文）或版式家具；日文正文零改动。假名逐块核查：仅 2 处“丢失”均为讲解层正当翻译——P3 图注 `パブリックドメイン`→德文 `gemeinfrei`；P7 披露日文句+中文译注→单条德文披露（F1 缩短版，KIT §11 有据）。
- 221 键：`map-de.json` 仍缺失（见观察项 O5），无法直接数 map 键；以效果验证代替——150 个差异块已覆盖全部讲解字符串，无一遗漏、无一日文改动、无一中文残留。

## 5. U+2019 全扫

- 8 个 SVG 中 U+2019 总数 **0**；text.md 中 0。另查：ASCII 撇号 0×；德文弯引号 „ “（U+201E/U+201C）0×——本版德文注释用日文 「」 引注，无任何撇号/弯引号字符可供渲染出错；目视抽查 P1 Anm.、P7 诊所等含引号的行，无宽字形断裂。

## 6. 机械门（自跑结果，详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| 身份（双 PDF 字节 + SHA-256） | 通过，与 KIT §8a 登记逐字一致 |
| `run.py` 重跑（`tools/venv/bin/python`，拷贝目录中运行，未动原件） | exit 0，FLOW OVERFLOW / HEAD TOO WIDE 0 条；登记与 KIT 一致；P7 col3 1780.62、teaser 2554.62、P8-ex y=561、P8-keys y=2382 |
| freeze（原 SVG vs 重跑 SVG 直接 sha256） | 8/8 字节一致 |
| occlusion（`tools/occlusion_audit.py`，自检通过） | 0 flags |
| p8 extract（`tools/p8.py extract --total 150`） | 150/150 |
| p8 compare（vs core） | CLEAN，keydiff=[137,138,139,140]（4 条原因已逐条核实，见 §3.2） |
| print/web 文字层 | `pdftotext` 各 105,192 字节，逐字节一致 |
| P8 字号（PyMuPDF） | 最小 9.98pt；题干 10.35pt |

## 7. 观察项（不计缺陷）

- O1（core 侧，非 de 缺陷；第一轮 O1 延续）：core P8 key 47 中文简析写“一之富士”，key 115 写“义之富士”，日文正文为 義ノ富士——key 47 疑为 core 中文笔误（义→一）。de 两处均正确译为 `Yoshinofuji`，fan-out 处理无误；提请 core 侧另行注意，本轮不计 de 缺陷。
- O2（第一轮 O2 延续）：同一词两种德译——P1 Anm. `一番太鼓 = die erste Trommel` vs key 27/102 `一番太鼓 = die Mitternachtstrommel`；两种译法各自成立，只是不一致。
- O3（第一轮 O3 延续）：P7 B2 术语表 `金星 kinboshi` 仅给罗马字、未给德译（同栏其余词均有德译）；但该词在同版正文、P4 注释与答案简析中均有解释，属可接受的术语保留。
- O4（本轮人名核查新发现，非 de 缺陷）：key 86 `Japan Meteorological Association` 是对 日本気象協会 的字面直译；该机构官方英文名为 Japan Weather Association。但该译名与 core 中文简析（“按日本气象协会预报”）及 en 版（`The Japan Meteorological Association forecast`）完全一致，是全家共用的直译，非 de 独有偏差；改动须全家同步，属 core/family 层面事项，不计 de 缺陷。
- O5（资料缺失；第一轮 O5 延续）：`map-de.json`、`apply.py`、构建日志仍随 `hidden_files/w47/scratch-fanout-ja/` 缺失，本轮 221 键计数与构建解释器确认仍只能以 KIT §9 + 全量 diff 效果验证代替。KIT §9 NOTE 已记：若 map 日后恢复，须把 D1/D2/D3 7 处写回 map，否则 fresh apply 会丢修复。
- O6（第一轮 O6 延续）：fan-out 目录在 git 中完全未追踪（`??`），insert 尚未执行——属协调员步骤，非内容问题。
- O7（第一轮 O7 延续）：P8 key 92 简析 `38+24=62`、key 65 `30 Nominierungen am Donnerstag, 5. November` 为 F2 缩短方针下的电报体，算术/事实无误，不计缺陷。
- O8（本轮人名核查新发现，非缺陷）：key 80 `Kihara Ryuichi` 未加长音符（Wikipedia 作 `Kihara Ryūichi`），但与 ISU 官方履历拼写 `Ryuichi KIHARA` 一致；版内其余长音均有长音符（Ōnosato、Hōshōryū、Fujiryōga），此处为与 ISU 一致的例外，不计缺陷。

## 8. 工作文件

- 本笔记：`hidden_files/w47/scratch-proof-ja-de2/PROOF-NOTE.md`
- 门日志：`hidden_files/w47/scratch-proof-ja-de2/GATE-LOG.md`
- 扫描与门输出：`probe.txt`、`sha-orig.txt`、`sha-rerun.txt`、`rerun-log.txt`、`de-occlusion-proof2.json`、`de-p8-proof2.json`、`de-p8compare-proof2.json`、`print.txt`、`web.txt`、`p8-fontsize.txt`、`core-de-diff.txt`
- 重跑拷贝：`rerun/`（构建源码拷贝 + 重跑生成的 SVG，含 `rerun/svg/`）；渲染图：`render-print/p-*.png`（印刷 8 版）、`render-web/w-p1-1.png`、`w-p8-8.png`
- 未改动任何成品、源码或仓库状态；未跑 `insert.py`、`lint --write`；未 git add/commit/push。
