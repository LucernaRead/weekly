# GATE-LOG — Lucerna Weekly 2026-W47 · ru-it · proof1

复校员：独立子代理 `c3d57066-6877-35e0-660b-f8dec0e7e66d`，2026-11-11。全部机械门均为本人实跑，不信 KIT，只信自跑结果。证据文件均在 scratch 目录（`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-it1/`）。

## §0 身份与探针

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 写探针文件 `probe.txt` 成功。
- `TMPDIR` 全程设为 scratch 下 `tmp/`（系统 /tmp 仅 512M 且常满）。
- 三文件 SHA 与任务一致（见 PROOF-NOTE §0）：印 PDF 21,260,017 字节；网 PDF 3,345,188 字节（< 7 MB 上限）；text.md 63,962 字节。
- creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与任务一致。
- `git status --porcelain`（版目录）：仅 `??` 未跟踪项，无源文件被改动。

## §1 遮挡审计（occlusion audit）

- 工具：`tools/occlusion_audit.py`，对版 `svg/` 目录。
- 自测：6 类 planted 遮挡全部触发，干净对照静默。
- 结果：**42 TEXTX，0 LINEX，0 COVER / FOOTER / EDGE / BOXTITLE**（`occlusion.log`、`occlusion.json`）。
- 独立裁决：`adjudicate2.py`（v2，极性感知；阈值暗核 <120 / 亮底深字 >200；按 `El.idx` 配对；v1 `adjudicate.py` 因配对/阈值缺陷已废弃，v1 把带标题的深绿底误判为墨水）：35/42 CLEAR，7 REAL-TOUCH，0 未决。
- 7 项再测（`gapcheck.py`，逐像素列间隙）：每一项在重叠带内两字形之间都有 ≥1 px 全亮列（flag6/20/21 `Краснодар`+`»`：1 px；flag24：1 px；flag11 `студента`+`.`：1 px；flag30 `Планируйте`+`:`：8 px；flag37 `!» — `+`студента`：3 px），目视裁图均为正常字距。
- **最终：42/42 CLEAR**。审计的墨水盒重叠是字体度量假象：审计用 NotoSerifCJK SC 量西里尔字母，构建器用 NotoSerif-Regular 排版。
- 目视裁图（`crops/flag*.png`）：flag40（P8 `ОТВЕТЫ`）、flag32（P7 `ЯЗЫК`）、flag00（`Зенит`）、flag06、flag20、flag11、flag24、flag30、flag37——全部清晰分离。

## §2 正典 creambox.py 全版扫描

- 工具：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`，+45px 窗口 + 逐行 clearance（`creambox.log`，1155 行）。
- **无整行漫出**。全部负的末基线余量（−28 至 −37）都是下一标题的假阳性（+28…+37 类），框内余量健康（+15.9 至 +47.7）。
- P7 toolbox：3 框，框内最小余量 +11.9，降部最小 +5.9。
- P3/P5 奶油框：真墨迹余量 +43 至 +68。
- 唯一边际行：P2 `per Nonno Gelo.` 框内余量 +5.0、降部估算 −1.0（0.30em 估算偏大）——PIL 真墨迹实测见 §6，余量 +0.52 px（O1）。

## §3 p8 compare

- 工具：`tools/p8.py`，显式 `--core-p8` / `--edition-p8`。
- `extract`：core 与版各 150/150 noted，1–150 连续（`p8-extract.log/.json`）。
- `compare`：**CLEAN**，missing=[]，extra_count=0，**keydiff=[137, 138, 139, 140]**（`p8-compare.log/.json`）。
- keydiff 裁决：137–140 为 E 节翻译键，本应为意大利语（core 为俄语），已逐句核对正确，非缺陷。

## §4 freeze

- `freeze.py baseline`（core）：**8/8 SVG 字节一致**，core 完整性未变（`freeze-baseline.log`）。
- `freeze.py baseline --build <版目录> --core-svg <版目录>/svg`（版可重现性）：**8/8 字节一致**（`freeze-edition.log`）。
- `freeze.py diff`（core vs 版；`--core-svg` 指 `core-ru/svg` 目录，绝非版目录）：每页 +19/−21 … +172/−638 字符串；新增 CJK 仅 U+3000（表意空格，SOP §1.1 分隔符），共 6 个——无新增真实 CJK（`freeze-diff.log/.json`）。

## §5 keycheck 150/150

- 文件：`keycheck-150.json`（构建脚本 `build_keycheck.py`；题干与键自 text.md 机械抽取——答案节 150 键、练习节 150 题干，零缺失；逐题 verdict 为手验结果）。
- **149 ok，1 开放题（#150，按设计）**，0 错误。
- 印 P8 答案 vs text.md 答案机械比对（空白不敏感）：149/150 逐字一致；#150 印 `✓`，text.md 为“(Domanda aperta, testo modello qui sotto)”+ 97 词范文。
- 手验依据（按题号段，见 JSON 内 `basis` 字段）：P1 14 轮/积分榜/黑五；P2 节日与天气；P3 五部 19 日首映；P4 14 轮积分表（进球和 21 已重算）；P5 11.11 销售；P6 日历+图表；P7 纠错门诊与词框；P8 A–H 全节；E 节翻译键 137–140 已逐句核对。
- 注：Q101/Q102/Q104 与 Q16/Q17/Q18 题干相同（P7 A2 天气词复习，故意螺旋重复），键相同（оттепель/мокрый/ледяной），均已核对。

## §6 PIL 真墨迹实测（boxtitle / 框标题 / 页边）

- 脚本：`pil_measure.py`（复用 `occlusion_audit.parse_svg` / `ink_box`；`pil-measure.log`）。
- 无墨迹越过任何页边；页脚外 y>2596 无墨迹。
- 各页最大墨迹右缘均为 **1862.0**（仅页脚），**唯 P2 为 1871.2**——即 D2（P2 Q11b，见 PROOF-NOTE）。
- 有边框矩形：仅 P6（7 个），0 墨迹/边框交叉；其余页 0 有边框矩形（无边框奶油框）。
- P1 标题 `ТУР В ЦИФРАХ IN CIFRE`：墨迹右缘 **845.6**（KIT 称 827.8，见 O3）；右邻元素为 x=989 起的第 3 栏，约 143 px 空隙，无 P1 标题/徽章碰撞。KIT 所称“Q6 chip 在 x=989”在 y≈1240 处无独立元素，x=989 的矩形是别处的 quiz 徽章。
- P2 `per Nonno Gelo.`：真墨迹底 **1158.48** vs 框底 1159.0，余量 **+0.52 px**（裁图 `crops/p2-nonnogelo-boxbottom.png` 目视：降部基本贴框边、未跨出）。
- P3/P5 右栏奶油框末行真墨迹余量 **+43.0 至 +68.1**。
- P7 toolbox 真墨迹最小余量 **+6.9**（`распродажа` 框）。

## §7 印/网文字层比对

- 抽取：PyMuPDF（fitz）逐页 `print-pN.txt` / `web-pN.txt`（N=1–8）；`pdftotext` 全文：印 57,602 字节，网 57,648 字节（网 = KIT 所称 57,648）。
- 字符多重集：网 = 印 **+ 241 个空格**（P1 +32、P2 +30、P3 +17、P4 +15、P5 +31、P6 +22、P7 +43、P8 +51），**零字符丢失**。fitz 字符数：印 37,255 / 网 37,496（KIT“各 30,862 字符、完全相同”未能复现，见 O2；但无丢失结论在字符级成立）。
- **斜体**：印 P1 有 3 个斜体 span（`«` Newsreader-Italic、`чёрная пятница` NotoSerif-MediumItalic、`»`）；网 PDF 全部 8 页 **0 个斜体 span**，字体表无斜体面。网 span 文本 `чёрнаяпятница`（丢空格）；印为 `чёрная пятница`。闭引号：印 italic x1=1222.8 vs `»` x0=1220.6（压入）；网文本 x1=1218.9 vs `»` x0=1220.6（1.7 px 间隙，贴合，未脱离）。目视：`crops/p1-wordbox-print.png`（斜体）vs `crops/p1-wordbox-web.png`（正体）。全刊仅此一处斜体。
- P1 200 dpi 右缘条带扫描：印版 106 深色像素位于 x 3880–3885（= 1862 边界抗锯齿），网版 97 像素仅页脚（`p1-print-200dpi.png`、`p1-web-200dpi.png`）。

## §8 P8 最小字号实测

- PyMuPDF 对印 PDF：**最小 9.75 pt**（386 个 span 为 9.75），直方图 9.75 / 9.98 / 10.35 / 10.88 / 11.25 / 12.75 / 13.5 / 14.25——与 KIT 一致，正在 SOP §1.1 下限（≥9.75 pt），可接受。KIT 数字为实测 pt，非配置 px（已按任务要求实测为准）。

## §9 弯引号 U+201C/U+201D/U+2019 全版扫描

- SVG：仅 P7 有一对 U+201C/U+201D——Newsreader 20.5 pt，`на “чёрной пятнице”`，为任务指明的故意保留例外。U+2019：全部 SVG 为 0。
- 直引号均为合法意大利语省音（`l'anno scorso`、`l'ultima`、`l'8 novembre`、`all'83°` 等）。
- text.md：U+201C/U+201D 1 对（同一 P7 句），U+2019 为 0，**0 个 CJK 字符**，无 `翻譯`/`翻译`。

## §10 内部标签 / CJK / ABSTRACT

- 可见 SVG 文本中唯一 CJK：P1 moth `<title>` 元数据内的 `三色蛾`（与 core 相同，非可见文本）。
- 可见文本中无 `2026-w47`、`ru-it`、`W47`、`cover`、`SOP`、`lint`、`proofread`。
- text.md 内 `— СТРАНИЦА? —` 分隔符亦见于 core-ru text.md（导出器格式，非缺陷）。
- text.md 第 E 节标签为意大利语：`Traduzione`、`[Traduci in italiano]`。
- `ABSTRACT.txt`：391 字节（KIT 称 390，相差 1 字节为结尾换行，非缺陷），无 ASCII 双引号，意大利语，点名真实 W47 话题 + VOL.4 + A2–B2 + 150 题。

## §11 外部事实来源（2026-11-11 browser.search 核实）

- **Ozon 11.11 2025 单日 14.4M+ 订单**（引 Retail.ru/Ozon 总结）：https://vc.ru/marketing/3226995-reklama-k-11-11-kak-podgotovitsya-i-ne-pereplatit-za-zakazy
- **黑五日期**：WB 16–30 Nov、Ozon 13 Nov–2 Dec、11.11 22 Oct–12 Nov：https://ptzgovorit.ru/news/marketpleysy-nazvali-daty-chernoy-pyatnicy ；https://360.ru/tekst/obschestvo/kogda-nachnutsja-osennie-rasprodazhi-v-rossii/
- **黑五在俄自 2013 年**（首次 2013 年 12 月 6 日）：https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%80%D0%BD%D0%B0%D1%8F_%D0%BF%D1%8F%D1%82%D0%BD%D0%B8%D1%86%D0%B0_(%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B8) ；https://www.calend.ru/holidays/0/0/3277/
- **Hunger Games（Рассвет жатвы）俄上映 26 Nov 2026**，世界首映 20 Nov（俄发行方推迟一周）：https://cyber.sports.ru/cinema/1117424049-data-vyxoda-filma-golodnye-igry-rassvet-zhatvy-v-rossii.html ；https://www.championat.ru/cybersport/news-6677634-filmu-golodnye-igry-rassvet-zhatvy-predrekayut-start-v-70-mln-bolshe-proshloj-chasti.html ；https://www.sobaka.ru/entertainment/cinema/222988 ；https://riamo.ru/articles/istorii/18-rossijskih-i-zarubezhnyh-filmov-kotorye-vyjdut-na-ekrany-v-nojabre-2026-goda/
- **«Рокки — это я»（Farrelly，Ippolito 饰 Stallone）与 «Бумажный тигр»（James Gray，Cannes 2026）俄上映 19 Nov**：https://riamo.ru/articles/istorii/18-rossijskih-i-zarubezhnyh-filmov-kotorye-vyjdut-na-ekrany-v-nojabre-2026-goda/ ；https://vtomske.ru/details/217134-novyi-begushchii-po-lezviyu-biografiya-rokki-i-pletenyi-muj-glavnye-kinopremery-noyabrya-2026 ；https://www.mk.ru/culture/2026/10/30/novye-filmy-oseni-2026-chto-uzhe-vyshlo-i-chto-pokazhut-do-konca-goda.html ；https://www.sobaka.ru/entertainment/cinema/222988
- **«Увидеть всё»（You Can See Everything）**：A24 纪录片，Nathan Fielder + Lance Oppenheim，讲 Elizabeth Holmes（Theranos 创始人），NYFF 2026 Spotlight，2026 年 11 月 8 日获 5 项 Critics Choice Documentary Awards：https://www.sortiraparis.com/uk/khobi/kinoteatr-festival/articles/355957-you-can-see-everything-dokumental-nij-fil-m-pro-elizabet-golms-u-kinoteatrah-30-grudna ；https://ar.wikipedia.org/wiki/%D9%8A%D9%85%D9%83%D9%86%D9%83_%D8%B1%D8%A4%D9%8A%D8%A9_%D9%83%D9%84_%D8%B4%D9%8A%D8%A1 ；俄 11 月档（19 日起）见：https://www.sobaka.ru/entertainment/cinema/222988 ；https://daily.afisha.ru/cinema/38337-7-filmov-kotorye-stoit-uvidet-v-kino-v-noyabre-2026/
- **Nikita Simonyan 百年诞辰 2026 年 10 月 12 日**（生于 1926 年，2025 年 11 月 23 日去世，享年 99 岁；百年为身后纪念，报纸“100-летию посвящён”表述准确）：https://www.championat.ru/football/article-6653502-100-let-so-dnya-rozhdeniya-nikity-simonyana-legendu-futbola-sssr-i-rossii-vspominayut-cherchesov-syomin-gusev-lovchev.html#comments ；https://sportmail.ru/news/football/72687923/ ；https://www.sovsport.ru/football/news/rfs-izmenil-dizajn-sajta-k-100-letiyu-nikity-simonyana
- **星期核对**（`date`，Europe/Moscow）：2026 年 11 月 6 日周五、7 日周六、8 日周日、12 日周四、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、27 日周五、30 日周一；11 月共 20 工作日 + 10 非工作日（9 个周末日 + 11 月 4 日假日）；母亲节 11 月 29 日为 11 月最后一个周日。

## §12 判为非缺陷的项

- 42 TEXTX 全部裁决 CLEAR（§1：字体度量假象，有逐像素间隙 + 目视裁图）。
- creambox 全部负余量均为下一标题假阳性，框内余量健康（§2）。
- P2 `per Nonno Gelo.` 降部：估算 −1.0 是 0.30em 估算偏大，真墨迹余量 +0.52 px，未跨框（§6；O1）。
- P3 中部大面积空白（第 2–4 栏，y≈1100–1600）：文章短，留白，非缺陷（O4）。
- `— СТРАНИЦА? —`：core 亦有，导出器格式（§10）。
- moth `三色蛾`：仅 P1 `<title>` 元数据，非可见文本（§10）。
- P8 最小字号 9.75 pt：正在 SOP §1.1 下限，可接受（§8）。
- P7 弯引号一对：故意保留的例外（§9）。
- ABSTRACT.txt 391 vs KIT 390 字节：结尾换行之差（§10）。
- KIT 字符数 30,862（O2）与 P1 标题右缘 827.8（O3）：方法差异，实质结论一致，不影响本版。
- P8 «Морозко» 图缺席：build 条件跳过（keys 止于第 3 栏 y=2288.34），与 W46 ru-it 相同，按设计。
- 字面 `___` 空白（87 处）：模板级；`.text.md` 不含变量组装内容；西里尔-拉丁 gloss 交界处 4–6 px 窄词距与 core 相同，正常；无首字下沉非缺陷；P8 词干 10.35 pt 保留核心值——以上均为 KIT §7 已裁决项，本次复核未见反证。

## §13 交付文件（scratch）

- `PROOF-NOTE.md`（结论 (b)，缺陷 D1/D2）
- `GATE-LOG.md`（本文件）
- `keycheck-150.json`（150 题逐题手验；构建脚本 `build_keycheck.py`）
- 证据：`occlusion.log/.json`、`occlusion-adjudication.txt`、`creambox.log`、`p8-extract.log/.json`、`p8-compare.log/.json`、`freeze-baseline.log`、`freeze-edition.log`、`freeze-diff.log/.json`、`pil-measure.log`、`pil_measure.py`、`adjudicate2.py`、`gapcheck.py`、`print-pN.txt` / `web-pN.txt`、`print-pdftotext.txt`、`web-pdftotext.txt`、`p1-print-200dpi.png`、`p1-web-200dpi.png`、`crops/`（flag 裁图、p2-q11b-overshoot、p2-nonnogelo-boxbottom、p1-wordbox-print/web）
