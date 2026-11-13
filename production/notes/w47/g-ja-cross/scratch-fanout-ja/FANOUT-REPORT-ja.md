# FANOUT-REPORT-ja — W47 日文家庭 fan-out（接替棒）

## ✅ 第 6 棒：zh-tw 版完成（2026-11-11 04:48–05:05 UTC）

- **zh-tw 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-ZH-TW.pdf`：26,034,686 字节，sha256 `7b23a2c475c666a6c6fa13b8efc37b8e11b86b994e88e20061ee699346ff83e6`
  - web PDF `Lucerna-VOL4-JA-ZH-TW-web.pdf`：4,788,784 字节（< 7 MB），sha256 `cafe8303f658c2c8e03601ddedcc0f3fa4f503b54794abd5e7221b5919f1b9c1`，文字层与 print 逐字节一致（44,661 B）
  - `2026-w47-ja-zh-tw.text.md`：44,361 字节，1352 行（源稿导出）；`ABSTRACT.txt`（繁体中文一行）；`WEEKLY-KIT.md`（zh-tw 版）。
  - 门禁：run.py exit 0 零溢出（run2 终版，run3/4/5 freeze 复跑）；occlusion 0 flags（selftest OK）；p8 extract 150/150；p8 compare CLEAN，**keydiff 恰为 [139, 140]**（见 F3——zh-tw 的正确值，非缺项）；freeze 直接 sha256 两次构建 8/8 相同（run4==run5）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `第 N 版 / 共 8 版`）；8 版目视全过；残留扫描见 F4。
- **P8 无需缩短**（同 it/ko）：run1 即零溢出，P8-keys 止于 2351（余 189px）；P7 teaser 止于 2442（披露 3 行，余 138px）。P1 gloss 2 行末基线 1865.95 vs 分隔线 1884（余 18px）；P2 卡片 gloss 皆 1 行 y=1752.06，盒底 1768。
- **F0 地图由生成器产**（`gen-map-zh-tw.py`）：OpenCC s2t 逐键转换 + 修表 + 覆盖表 + INSTR/META；221 键逐键核对一致、`·` 0；221 行全表 `/tmp/zh-tw-table.txt` 逐行目视后才 apply。206 键变、15 键不变（逐一核实无误）。s2t 陷阱已修：`爲`→`為`（台湾标准）、`大之裏`→`大之里`（人名）、日文词头还原（この号の内容、前号、紅葉の写真、屋台、千秋楽）、图注 `写真：` 保留（W46 前例）；覆盖：页脚 `Lucerna　日語週報 VOL.4　正文日語　講解繁體中文`、趋势行 `來源與日期見各篇文章`（190px）、页码引用 `第N面`→`N面`（模板加括号成 `(N面)`，与 W46 一致）、`詳見第 4 版`/`答案見第 8 版`/`見第 2 版` 按 W46 带空格写法。
- **F1 apply.py 误报已修**（自有 scratch 工具）：残留检查允许集未含 instr 值，zh-tw instr 值 `把詞和釋義配對` 含共享字 `和`（在 ZH 标记集里），首跑 RC=1 报 3 条残留——替换本身正确。修：`vals` 加 `set(instr_map.values())`；重 apply RC=0（map 221 键，instr 6）。其余语种不受影响（instr 值非汉字）。
- **F2 freeze 重做**：run3 的 SHA 文件被 `sha256sum | tee | head -2` 截断（head 关管道的老陷阱）。重跑 run5，run4 vs run5 完整 8 行比对 8/8 相同。
- **F3 keydiff [139, 140] 是 zh-tw 的正确值**：E 键 137 `二之酉在11月19日。` 与 138 `新酒在11月19日解禁。` 无简体专属字，繁体值与核心逐字节相同，故不 diff。已逐键验过 137–140（`— 對照第2/3/5/6版`）。后人见 [139, 140] 勿当缺项。
- **F4 残留扫描**：text.md 仅 `售`×5、`呢`×3——均为繁简同形字误报（`開始發售`、`你呢？` 皆正确繁体）；真残留 0。`参考答案` 0×、`參考答案` 1×、`吉伊卡哇` 4×（zh-tw 正确读者名）。
- **F5 webpdf 用法**：`webpdf.py svg_dir out_pdf`（由 SVG 建 web PDF，非由 print PDF 转）。首试错传 print PDF 致 argparse RC=2，重跑 RC=0。已记入 KIT §8。
- 构建日志：`gen-map-zh-tw.py`、`map-zh-tw.json`、`apply-zh-tw.log`（RC=1 误报）/`apply-zh-tw2.log`（RC=0）、`build-zh-tw-run1..5.log`、`render-zh-tw.log`、`webpdf-zh-tw.log`、`export-textmd-zh-tw.py`、`zh-tw-occlusion-run2.json`、`zh-tw-p8-run2.json`、`zh-tw-p8compare-run2.json`、`zh-tw-sha-run4/5.txt`（`zh-tw-sha-run3.txt` 已截断，勿用），均在 scratch-fanout-ja/。**第 6 棒分工（ko + zh-tw）至此全部完成。ru 在第 7 棒手中（目录已有 print PDF，报告尚无完成记录），本棒不动。**

## 🔀 分工说明（第 6 棒，2026-11-11 ~04:30 UTC）

- **it 版双重核验通过**（见下文第 7 棒记录 + 本棒复核）：print 29,099,162 B sha `75986cd7…`、web 4,476,984 B sha `b3ea6d18…`，与第 7 棒 KIT 记录逐字节一致；本棒重跑 run.py 两次（run4/run5）freeze 8/8 相同、逐键复核仅 [137–140] 意译、P8 最小字号 9.975pt、print/web 文字层逐字节一致、§1.1/残留 0、8 版目视全过。**it 无缺项。**
- **渲染竞态已查明**：首轮 render.py 被 runtime 重复执行两次（两进程写同一 PDF）致 108MB 臃肿版；第 7 棒已单进程重渲出干净版（`render-it2.log`，29,099,162 B），臃肿版已删。教训：同一版目录绝不双开渲染，重跑前先查 `ps`。
- **分工（防并行冲突）**：pt 版正在第 7 棒手中（apply 04:20、run1 04:22，P8 5 行溢出待修）；**本棒接手 ko 版，其次 zh-tw 版**；nl / ru 留给第 7 棒按序推进。第 7 棒读到此条后勿再开 ko / zh-tw。本棒不动 pt / nl / ru。

## ✅ 第 6 棒：ko 版完成（2026-11-11 04:30–04:48 UTC）

- **ko 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-KO.pdf`：28,189,461 字节，sha256 `fbcfe840f569ff521fb4aed509a441b8375a01b792f329fdc0a0bda2689437bc`
  - web PDF `Lucerna-VOL4-JA-KO-web.pdf`：4,550,459 字节（< 7 MB），sha256 `d52edd4e6be8a2b3fa7c3115155e07e6cde028aa7dceaa723fea34bb365c27ac`，文字层与 print 逐字节一致（47,997 B）
  - `2026-w47-ja-ko.text.md`：47,721 字节，1330 行（源 SVG 导出）；`ABSTRACT.txt`（ko 一行）；`WEEKLY-KIT.md`（ko 版）。
  - 门禁：run.py exit 0 零溢出（run3 终版，run4 freeze 复跑）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为韩译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run3/run4；run1/run2 修前亦 8/8）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `제 N 면 / 총 8 면`）；8 版目视全过；中文残留扫描（吉伊卡哇/参考答案/酉之市/提名 皆 0）。
- **P8 无需缩短**（同 it）：run1 即零溢出，P8-keys 止于 2366（余 174px）；P7 teaser 止于 2470.1（披露 4 行，余 110px）。
- **目视发现 1 处修**：P7 易错诊所「こと」注记句点孤悬第二行（378.67px 对 ~378.5px 盒）。修法：map 值缩为 `동사를 명사로 만들 땐 「こと」를 붙이세요.`（360.73px，wrap 事前验算 1 行），写入 map-ko.json + gen-map-ko.py；重 apply + 重跑（run3）+ 重渲 + 全套门禁重验，teaser 止于 2443.58，P8-keys 不变。
- **p8.py 用法纠正**：`compare` 的 `--core-p8`/`--edition-p8` 要传 SVG 路径（非 extract 的 JSON），否则 PARSE_FAIL；且 `extract`/`compare` 均须 flag 形式（`--p8/--total/--json`），位置参数报错。已记入 ko KIT §8。
- 构建日志：`gen-map-ko.py`、`map-ko.json`、`apply-ko.log`/`apply-ko2.log`、`build-ko-run1..4.log`、`render-ko.log`/`render-ko2.log`、`webpdf-ko.log`/`webpdf-ko2.log`、`export-textmd-ko.py`、`ko-occlusion-run3.json`、`ko-p8-run3.json`、`ko-p8compare-run3.json`、`ko-sha-run1..4.txt`，均在 scratch-fanout-ja/。

## ✅ 第 7 棒：ru 版完成（2026-11-11 05:05–05:20 UTC）

- **ru 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-RU.pdf`：25,858,425 字节（比拉丁版小约 3 MB——已查明非缺图：5 张图全在、8 页、嵌入字体与 pt 版同为 33 个，差值纯属字体子集大小，见 KIT §8 注），sha256 `abc44c9c695ddac9df434e93cf51e6eae5604c7f78b663331603dacc425a525f`
  - web PDF `Lucerna-VOL4-JA-RU-web.pdf`：4,396,999 字节（< 7 MB），sha256 `e2fc538241a3d1446ab78dab0acfa411b0f95f126a7c926a82f69fe7d350e94e`，文字层与 print 逐字节一致（53,247 B）
  - `2026-w47-ja-ru.text.md`：52,948 字节，1380 行（源 SVG 导出）；`ABSTRACT.txt`（ru 一行）；`WEEKLY-KIT.md`（ru 版）。
  - 门禁：run.py exit 0 零溢出（run2/run3）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为意译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run2==run3）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Страница N из 8`）；8 版目视全过（西里尔字母无豆腐块，Noto CJK 覆盖已验）；全文读完；中文残留扫描（吉伊卡哇/参考答案/酉之市/提名 皆 0）。
- **P8-keys 曾 2 行溢出**（止于 2585）：流模拟找 19 条包 2 行；9 条 distinct 注记 + `writing_note` meta 各缩为一行（wrap 逐条验算，如 `Кинбоси Фудзирюги: 11-й турнир с дебюта`、`Прогнозы различаются: определение разное`），P8-keys 止于 2428（余 112px）。#39/#133/#134（日语题干长）与 E 键 #139/#140 仍包 2 行无妨；#132 缩后仍 2 行，留作 2 行（余量已足）。
- **P7/P1 未出事**：披露起稿即 5 行（167 字符，wrap 事前验算）、P1 gloss 起稿即 2 行，teaser 止于 2525.62（余 54px，本棒四版中余量最大）。
- map-ru.json 为本棒从零新写（`build-map-ru.py` 按 map-en 键序编号填值，221 键断言与 map-en 逐键一致；仅 `38+24=62` 为 identity 值）；力士名用标准俄语音译（Оносато / Хосёрю / Фудзирюга / Ёсинофудзи / Уми-но-уми；Тори-но-ити / Ни-но-тори / кумадэ 沿用 W46 ru 既定写法），`Чикава` 按裁定。构建日志：`apply-ru.log`/`apply-ru2.log`、`build-ru-run1/2/3.log`、`render-ru.log`、`webpdf-ru.log`、`ru-occlusion.json`、`ru-p8compare.json`、`ru-p8.json`、`ru-sha-run2/3.txt`、`probe-ru-p8short.py`、`export-textmd-ru.py`，均在 scratch-fanout-ja/。

## ✅ 第 7 棒：nl 版完成（2026-11-11 04:50–05:05 UTC）

- **nl 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-NL.pdf`：29,099,171 字节，sha256 `c18c551af2249561000dd50821d4e9646597c5a2cdccf316b02ee38128d40a19`
  - web PDF `Lucerna-VOL4-JA-NL-web.pdf`：4,476,557 字节（< 7 MB），sha256 `e0678a4b892ff07080d48a51b2f8b7c9ee109916752df537849000370ad9cb81`，文字层与 print 逐字节一致（45,989 B）
  - `2026-w47-ja-nl.text.md`：45,685 字节，1379 行（源 SVG 导出）；`ABSTRACT.txt`（nl 一行）；`WEEKLY-KIT.md`（nl 版）。
  - 门禁：run.py exit 0 零溢出（run2/run3）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为意译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run2==run3）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Pagina N van 8`）；8 版目视全过；全文读完；中文残留扫描（吉伊卡哇/参考答案/酉之市/提名 皆 0）。
- **P8-keys 曾 8 行溢出**（止于 2569）：流模拟找 28 条包 2 行；17 条 distinct 注记各缩为一行（wrap 逐条验算，如 `Kinboshi van Fujiryūga: 11e toernooi sinds debuut`、`Voorspellingen verschillen: definitie verschilt`），P8-keys 止于 2428（余 112px）。#39/#133/#134（日语题干长）与 E 键 #139/#140 仍包 2 行无妨。`writing_note` 单独验算为 1 行——模拟器 #150 的 `yokozuna d` 尾巴是段落切分假象，无实溢出。
- **P7/P1 未出事**：披露起稿即 5 行（182 字符，wrap 事前验算）、P1 gloss 起稿即 2 行（wrap 事前验算），teaser 止于 2554.62（余 25px），无需重修（吸取 pt F2 教训，nl 建图前先验 wrap）。
- map-nl.json 为本棒从零新写（`build-map-nl.py` 按 map-en 键序编号填值，221 键断言与 map-en 逐键一致；仅 `38+24=62` 为 identity 值）；荷兰语注记按 W46 教训（Dutch notes run long）起稿即预缩。构建日志：`apply-nl.log`/`apply-nl2.log`、`build-nl-run1/2/3.log`、`render-nl.log`、`webpdf-nl.log`、`nl-occlusion.json`、`nl-p8compare.json`、`nl-p8.json`、`nl-sha-run2/3.txt`、`probe-nl-p8short.py`、`export-textmd-nl.py`，均在 scratch-fanout-ja/。

## ✅ 第 7 棒：pt 版完成（2026-11-11 04:20–04:45 UTC）

- **pt 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-PT.pdf`：29,103,006 字节，sha256 `5e7542bc94e191e418fd49326676523e545aeb3eb2363d48c19c1cc6dcb33e56`
  - web PDF `Lucerna-VOL4-JA-PT-web.pdf`：4,485,027 字节（< 7 MB），sha256 `499149398ebed4848a02b2e8efcaaf9bbbbfe1c97effe651ffde8029d8a6629c`，文字层与 print 逐字节一致（46,976 B）
  - `2026-w47-ja-pt.text.md`：46,703 字节，1376 行（源 SVG 导出）；`ABSTRACT.txt`（pt 一行）；`WEEKLY-KIT.md`（pt 版）。
  - 门禁：run.py exit 0 零溢出（run4/run5）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为意译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run4==run5）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Página N de 8`）；8 版目视全过；全文读完；中文残留扫描（吉伊卡哇/参考答案/酉之市/提名 皆 0）。
- **P8-keys 曾 5 行溢出**（止于 2569.2）：流模拟找 24 条包 2 行；17 条 distinct 注记（+ #26 的 d 变体）各缩为一行（wrap 逐条验算，如 `Kinboshi de Fujiryūga: 11.º torneio desde a estreia`、`Top 10 e grande prémio: 1 de dezembro`），P8-keys 止于 2397（余 143px）。#39/#133（日语题干长）与 E 键 #139/#140 仍包 2 行无妨。
- **P1 遮挡 1 旗**（run2 门禁发现）：本周词 gloss 包 3 行，末行（`que recolhe a boa sorte.`）划过 row-B 分隔线 y=1884——与 en F2 同类。修法：gloss 的 map 值缩为 2 行（`熊手 = ancinho de bambu do Tori-no-ichi, amuleto para negócios prósperos.`，19px sans / 422.5px wrap 事前验算）；重渲后 occlusion 0 flags。P7 不用修——披露起稿即 5 行，teaser 止于 2554.62（余 25px）。
- 构建日志：`apply-pt.log`/`apply-pt2.log`/`apply-pt3.log`、`build-pt-run1/2/3/4/5.log`、`render-pt.log`/`render-pt2.log`、`webpdf-pt.log`/`webpdf-pt2.log`、`pt-occlusion.json`、`pt-p8compare.json`、`pt-p8.json`、`pt-sha-run2/3/4/5.txt`、`probe-pt-p8short.py`、`export-textmd-pt.py`，均在 scratch-fanout-ja/。map-pt.json 221 键与 map-en 逐键核对一致（仅 `38+24=62` 为 identity 值）。

## ✅ 第 7 棒：it 版完成（2026-11-11 03:48–04:20 UTC）

- **it 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-IT.pdf`：29,099,162 字节，sha256 `75986cd7e7b0acc6e3d4887ccb023c577f3612c9a242c3093060cb7f2af200fd`
  - web PDF `Lucerna-VOL4-JA-IT-web.pdf`：4,476,984 字节（< 7 MB），sha256 `b3ea6d183dea6a1c5b64f5ff1a42807462a0f259fc37fea3668f7a239fc353f0`，文字层与 print 逐字节一致（47,000 B）
  - `2026-w47-ja-it.text.md`：46,676 字节，1378 行（源 SVG 导出）；`ABSTRACT.txt`（it 一行）；`WEEKLY-KIT.md`（it 版）。
  - 门禁：run.py exit 0 零溢出（run2/run3）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为意译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run2==run3）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Pagina N di 8`）；8 版目视全过；中文残留扫描（吉伊卡哇/参考答案/酉之市/提名 皆 0）。
- **P8-keys 曾 2 行溢出**（止于 2585）：流模拟找 19 条包 2 行；11 条 distinct 注记（+ writing_note）各缩为一行（wrap 逐条验算，如 `Kinboshi di Fujiryūga: 11° torneo dal debutto`、`Previsione meteo giapponese: Arashiyama 13 nov.`），P8-keys 止于 2442（余 98px）。#39（日语题干长）与 E 键 #139/#140 仍包 2 行无妨。
- **P7 teaser 曾越页脚（2583.62 > 2580）**：意译披露 6 行 + 诊所注记多 1 行。修法：披露缩至 5 行（191 字符，wrap 事前验算，单 VOL.5 提及，同 de 式）；teaser 止于 2528.1（余 52px）。
- **渲染竞态（无内容影响）**：首轮 `render.py` 被 runtime 重复执行两次（相隔 8 秒的两个进程写同一 PDF），合并出的 print PDF 108,387,170 字节、37,537 xrefs（en 为 197）——页数/图片相同但臃肿。已杀重复进程、删臃肿 PDF、单进程重渲（`render-it2.log`）：29,099,162 字节。教训已记入 KIT：同一版目录绝不双开渲染，重跑前先查 `ps`。
- 构建日志：`apply-it.log`/`apply-it2.log`、`build-it-run1/2/3.log`、`render-it.log`、`render-it2.log`、`webpdf-it.log`、`it-occlusion.json`、`it-p8compare.json`、`it-p8.json`、`it-sha-run2/3.txt`、`probe-p8sim.py`（通用版）、`probe-it-p8short.py`、`export-textmd-it.py`，均在 scratch-fanout-ja/。`probe-p8sim.py` 已通用化（`probe-p8sim.py <lang> [hdr-regex]`），后 6 语复用。

## ✅ 第 7 棒审计：en / de / fr 通过，es 在 sibling 手中收尾（2026-11-11 03:35–03:45 UTC）

开工探针双通（PROBE1 `git hash-object -w` OK，PROBE2 scratch 写 probe-7th.txt OK；`df` 49G 可用）。核心 SHA 与任务一致（print `e1782168…`、web `7c21329c…`）。

- **en 通过**：print 27,440,477 B sha `c29f6f98…`、web 4,428,571 B sha `9d10efc5…`，与第 6 棒报告逐字节一致；审计重跑 run.py exit 0 零溢出，8 SVG sha 与 run9 **8/8 相同**（补上了缺失的 `en-sha-run10.txt`——该文件盘上不存在，run10 只有日志；现 `audit7-sha-en.txt` 即第二构建）；P8-keys 止于 2426、teaser 2557.1；occlusion 0；p8 150/150、compare CLEAN、逐键复核仅 [137,138,139,140] 为英译；P8 最小字号 9.975pt；print/web 文字层逐字节一致（46,044 B）；§1.1 grep：纸 8×、旧色 0、禁色 0、`·` 0；KIT/text.md/ABSTRACT 齐全。**无缺项。**
- **de 通过**：print 29,102,629 B sha `b5d66e17…`、web 4,483,732 B sha `c55dd68c…`，与报告一致；审计重跑 exit 0 零溢出，sha 与 run5 **8/8 相同**；P8-keys 止于 2382、teaser 2554.62；occlusion 0；p8 150/150、compare CLEAN、逐键仅 [137–140] 德译；P8 最小字号 9.975pt；print/web 文字层一致（46,834 B）；§1.1 grep 全过；KIT/text.md/ABSTRACT 齐全。VOL.5 出现 3 次（他版 4 次）已核实为披露合并所致（`beides erscheint in VOL.5`），非缺失。**无缺项。**
- **fr 通过**：print 28,347,993 B sha `5903a36b…`、web 4,458,579 B sha `99fd99af…`，与报告一致；审计重跑 exit 0 零溢出，sha 与 run5 **8/8 相同**；P8-keys 止于 2411、teaser 2557.1；occlusion 0；p8 150/150、compare CLEAN、逐键仅 [137–140] 法译；P8 最小字号 9.975pt；print/web 文字层一致（47,208 B）；§1.1 grep 全过；KIT/text.md/ABSTRACT 齐全。**无缺项。**
- **es 已完工并通过收尾审计（2026-11-11 04:20 UTC 补记）**：sibling 于 03:44/03:46 补齐 web PDF（4,482,717 B）、text.md（46,682 B）、WEEKLY-KIT.md；第 7 棒验过：freeze run4 与审计重跑 sha **8/8 相同**（`es-sha-run4.txt` 对 `audit7-sha-es.txt`；p7 差异确系 03:33 重 apply 所致，两次后重 apply 构建一致）；print/web 文字层逐字节一致（47,034 B）；print PDF 29,102,097 B sha `0feb61136c4c9c267a9c84664287c6bb1a897ddb2fc496d79137073542eacb55`，web sha `b274eac2faa2a91cdeefc303092805253b34f3cacfef095cded332cee5e95380`。es 全部交付物齐全，门禁全绿（occlusion 0、p8 150/150、compare CLEAN、逐键仅 [137–140] 西译、P8 最小字号 9.975pt，均见上文审计）。**es 无缺项。**
- **审计日志**：`audit7-run-{en,de,fr,es}.log`、`audit7-sha-{en,de,fr,es}.txt` 在 scratch-fanout-ja/。

## 🔴 停工记录 2（接替棒，2026-11-11 ~01:00 UTC）

**状态：因磁盘配额故障再次停工。en 版做到 run.py 一步，未建成。**

- 开工写探针两次均通（PROBE1 `git hash-object -w` OK，PROBE2 scratch 写 probe-resume.txt OK，2026-11-11 00:54 UTC）。核心 SHA 已核对：print `e1782168…`、web `7c21329c…`，与任务一致。
- 01:00 UTC 前后，P8 溢出分析脚本重跑 content8.py 时 `p.save()` 报 `OSError: [Errno 122] Disk quota exceeded`（svg/p8-tesuto.svg）。按硬性规则立即停手，不重试。`df` 仍显示 45G 可用，属间歇性配额故障（与上一棒 00:40/00:47 UTC 两次同症）。
- 现场核查（只读）：8 个 SVG 均完整，均为 run.py 第 1 次构建产物（00:58–00:59，p8 449,335 字节、尾部 `</svg>` 完好）——失败的 save 在 open 即报，未截断文件，无损坏。
- 停工前已完成（均已落盘，可复用）：
  1. **待办 1 完成**，但有一处修正：分类器标记集只加了 `扑/红`，**未加 `移`**——初版三字全加后重跑误伤 5 条纯日文正文（紅葉の見頃は…移っています 等，`移` 为日中共享字），已回退。重跑后 translate-list 216→218（仅 +2 条 band sub），map-keys.json 重算为 **221**（= 218 + 7 后加 − 4 meta 处理的 f-string 碎片）。
  2. **map-en.json 修至对齐**：删 9 条（8 冻结小节头 + `スポーツ　体育`），补 4 条图注英文值；band 2 条值上一棒已写入。现 map **218 条**（报告原文"221 条键"实为 map-keys 总数；精确口径：map 218 + instr-only 3 条 = map-keys 221，逐键对齐无缺漏、无多余）。另：`map-en-new.json` 核实为上一棒未完成的局部复本（125 键、与 map-en.json 零值差），已废弃，不用。
  3. **apply.py 两处修补**（均为自有 scratch 工具，未动共享 tools）：svglib md5 pin 由 `74177544…` 更新为当前核心 `b8bca01f6438b2ba5fc1ab6d2b4cc4bb`——核心重定稿后 svglib 已变，字体仍为 Noto CJK JP、文件本身原样复制未改；残留检查豁免恒等映射 `38+24=62`（中英文同式）。`apply.py en` OK（map 218 键，instr 6）。
  4. **en 版 run.py**：exit 0，150 题（A2 48 / B1 73 / B2 29），**但 P8-keys 有 7 行 FLOW OVERFLOW**（末行 y=2569，底线 2540，超 29px ≈ 2 行）。其余 flow 零溢出；P7 teaser 止于 2557.1（页脚 2580，余 23px，通过）。
- **接替者待办（按顺序）**：
  1. 磁盘恢复后重做两次写探针，两次都通才动手。
  2. 先修 P8 溢出：首选 SOP §1.1 第 2 步——把 wrap 成两行的答案注记缩短为一行（只需省约 2 行；P8 题干 10.35pt 不动，答案 9.975pt 不动）。缩短哪几条须**非破坏式**测算（勿重跑 content 直接写 SVG；可用临时副本或 stub 掉 save 来取 REG 后算 wrap 行数）。备选：答案字号 13.3px→13.0px（9.75pt 下限），约省 28px，偏临界，不首选。修后重跑 run.py en 至**零溢出**。
  3. 再继续 en 版：render.py → webpdf.py → text 导出（仿 scratch-ja/export-textmd.py 的 SVG `<text>` 提取法，新写）→ 门禁（occlusion 0 flags、p8 extract 150/150、compare CLEAN 且 keydiff 恰为 [137,138,139,140]、freeze 两次构建 sha256 8/8、print/web 文字层逐字节一致、P8 最小字号 9.975pt 核查、§1.1 grep 审计）→ 150 键复核 → 8 版目视 → 写 en 版 KIT。
  4. 其余 9 语按 de → fr → es → it → pt → nl → ru → ko → zh-tw，每语同一 221 键写 map、同一全套流程。
- 日志文件：`apply-en.log`、`build-en-run.log`、`probe-resume.txt`、`translate-list-before.json`、`map-keys-before.json`、`map-en-before.json` 均在 scratch-fanout-ja/。

## ✅ 第 6 棒：es 版完成（2026-11-11 03:20–03:55 UTC）

- **es 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-ES.pdf`：29,102,097 字节，sha256 `0feb61136c4c9c267a9c84664287c6bb1a897ddb2fc496d79137073542eacb55`
  - web PDF `Lucerna-VOL4-JA-ES-web.pdf`：4,482,717 字节（< 7 MB），sha256 `b274eac2faa2a91cdeefc303092805253b34f3cacfef095cded332cee5e95380`，文字层与 print 逐字节一致
  - `2026-w47-ja-es.text.md`：46,682 字节，1349 行（源 SVG 导出）；`ABSTRACT.txt`（es 一行）；`WEEKLY-KIT.md`（es 版）。
  - 门禁：run.py exit 0 零溢出；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为西译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run2/run3 与 run4/run5 两对皆 8/8）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Página N de 8`）；8 版目视全过；中文残留扫描（参考答案/酉之市/提名/吉伊卡哇 皆 0）。
- **map 键曾大面积写错**（教训，见 KIT §11 F0）：首版 map-es.json 的中文键凭记忆写，102/221 对不上 en，有两处重复键被 JSON 吞掉、缺 4 键。已用 difflib 对齐 + 显式修正表 + 221 行全表逐目核对重建，最终键集与 en 精确一致。后 6 语一律按 en 键原样抄、不凭记忆写键。
- **P8-keys 曾 7 行溢出**（止于 2569）：流模拟找 26 条包 2 行；19 条 distinct 注记各缩为一行（wrap 前置验算，如 `Asoc. Meteorológica de Japón: Arashiyama desde el 13 nov.`、`Nominaciones: jue. 5 de noviembre`），writing_note 预先缩短；P8-keys 止于约 2397（余 ~143px）。#14/#39/#86/#125/#133/#140 仍包 2 行无妨。
- **P7 金句页码曾双括号** `((pág. 1))`：map 值自带括号而模板又包一层；改为裸 `pág. N` 后 P7 卡与 SVG 文本双重核对干净（后 6 语页码值一律裸写）。
- **P7 无需修**：西译披露（W46 式，VOL.5，6 行）teaser 恰落核心值 2557.1。
- 运行时注：webpdf+门禁的后台命令（proc_4239ef5d9903）被 VM 重启打断在 web PDF 与 text 导出已完成之后；缺失的门禁已从盘上已核实检查点重跑，未盲目重复。
- 构建日志：`build-es-run*.log`（run4 终版，run5 freeze 复跑）、`render-es*.log`、`es-occlusion-run4.json`、`es-p8compare-run4.json`、`es-p8-run4.json`、`es-sha-run2/3/4/5.txt`、`probe-es-p8sim.py`、`export-textmd-es.py`，均在 scratch-fanout-ja/。

## ✅ 第 6 棒：fr 版完成（2026-11-11 03:00–03:20 UTC）

- **fr 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-FR.pdf`：28,347,993 字节，sha256 `5903a36b47668d91c04dafb047f94022299f8f5308647696fe7cff9c47244517`
  - web PDF `Lucerna-VOL4-JA-FR-web.pdf`：4,458,579 字节（< 7 MB），sha256 `99fd99aff8f1a8289ae58435efc0a85e04b36e79d1a09ce7d700493e3658c47c`，文字层与 print 逐字节一致
  - `2026-w47-ja-fr.text.md`：46,880 字节，1350 行（源 SVG 导出）；`ABSTRACT.txt`（fr 一行）；`WEEKLY-KIT.md`（fr 版）。
  - 门禁：run.py exit 0 零溢出；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为法译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同（run3/run4 与 run5/run6 两对皆 8/8）；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Page N sur 8`）；8 版目视全过；中文残留扫描（参考答案/酉之市/提名/吉伊卡哇 皆 0）。
- **P8-keys 曾 4 行溢出**（止于 2585）：流模拟找 23 条包 2 行；12 条 distinct 注记（16 条目）各缩为一行（wrap 逐条验算，如 `Tournoi de Kyushu : 8 novembre (dim.)`、`Nominations des mots à la mode : jeu. 5 novembre`），另 writing_note 缩短；P8-keys 止于 2411（余 129px）。#32/#39/#81/#86/#87/#126/#140 仍包 2 行无妨。
- **P7 无需修**：法译披露（W46 式，VOL.5，6 行）+ 诊所注记恰好落回核心值，teaser 止于 2557.1（与核心/en 相同）。
- **P2 词卡 gloss 曾溢出固定盒**：第 4 卡（小雪）gloss 初版用了忠实长译 `quand un peu de neige commence à tomber`，19px 下包 2 行、出盒（与 de 同类缺陷；写 map 前明明已量出长式为 2 行、短式 `quand la neige commence à tomber` 为 1 行，写 map 时误用了长式——已在 KIT 记为教训：固定盒 gloss 写 map 前逐条量、写完再核对实际值）。修为短式后 P2 卡干净。
- 构建日志：`build-fr-run*.log`（run5 终版，run6 freeze 复跑）、`render-fr*.log`、`fr-occlusion-run5.json`、`fr-p8compare-run5.json`、`fr-p8-run5.json`、`fr-sha-run3/4/5/6.txt`、`probe-fr-p8sim.py`、`export-textmd-fr.py`，均在 scratch-fanout-ja/。

## ✅ 第 6 棒：de 版完成（2026-11-11 02:25–03:00 UTC）

- **de 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-DE.pdf`：29,102,629 字节，sha256 `b5d66e17d9ac29b6362d934e65a254a1bb63df5ea00ed305ce1b362cea06a239`
  - web PDF `Lucerna-VOL4-JA-DE-web.pdf`：4,483,732 字节（< 7 MB），sha256 `c55dd68cfcd6f0acc4cad79987a7ceb7fbe4c86d83cdf637c86c795497aff26a`，文字层与 print 逐字节一致
  - `2026-w47-ja-de.text.md`：46,516 字节，1349 行（源 SVG 导出）；`ABSTRACT.txt`（de 一行）；`WEEKLY-KIT.md`（de 版）。
  - 门禁：run.py exit 0 零溢出；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]（逐键验过：仅 E 组 4 键为德译，余 146 键与核心逐字节同）；freeze 直接 sha256 两次构建 8/8 相同；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、禁色 0×、`·` 0×、页码行 `Seite N von 8`）；8 版目视全过；中文残留扫描（参考答案/酉之市/提名/吉伊卡哇 皆 0）。
- **P7 teaser 曾越页脚（2612.62 > 2580）**：量算根因——读者园地盒比 en 高 55.52px = 披露德译 7 行 vs 6 行（+29px）+ 诊所注记德译 6 行 vs 5 行（+26.52px）。修法：披露缩至 5 行（191 字符，wrap 事前验算，`ausgewählte Briefe werden abgedruckt` 并入 `beides erscheint in VOL.5`）；teaser 止于 2554.62（余 25px）。
- **P8-keys 曾 6 行溢出**：流模拟与实测完全一致（y=2569.2，25 条包 2 行）；16 条 distinct 注记（21 条目）各缩为一行（wrap 逐条验算，如 `Beaujolais Nouveau: 19. November (Do.)`、`Nominierungen: 5. November`），P8-keys 止于 2382（余 158px）；#39/#86/#139/#140 仍包 2 行无妨（E 组键未动刀）。
- **P2 词卡 gloss 曾溢出固定盒**：首卡盒高 150px（底 1768.0），德译 gloss 包 2 行，第二基线 1776.76，墨迹出盒约 9px（SVG 几何量出，卡片裁剪确认）。修法：去冠词 `Bambusrechen für florierende Geschäfte`（1 行）。P1 gloss 同法量过：末基线 1865.95 vs 分隔线 1884，余 18px。
- **map 优于 en 的做法**：de 全部修复（披露、16 条注记缩写、P2 gloss）都写回了 `map-de.json`，重跑 apply 可完整复现；en 的注记缩写当时只改了内容文件（map-en 仍为长版），另：本次顺手把 map-en.json 里的 13 处 `·` 清掉（与 en 内容文件已修状态对齐）。
- 构建日志：`build-de-run*.log`（run5 终版，run6 freeze 复跑）、`render-de*.log`、`de-occlusion-run5.json`、`de-p8compare-run5.json`、`de-p8.json`、`de-sha-run5/6.txt`、`probe-de-p7.py`、`probe-de-p8sim.py`、`probe-de-p8short.py`、`export-textmd-de.py`，均在 scratch-fanout-ja/。另读过 `~/workspace/weekly-git/AGENTS.md`（运行期项目指引）：其中“入 issues + lint + 提交”流程属协调员事后事，本棒按任务红线未动（未跑 insert/lint、不提交、不移目录）。

## ✅ 第 6 棒：en 版完成（2026-11-11 01:31–02:25 UTC）

- **en 版全部交付物已建成并通过全部硬门禁**（自查零问题；待协调员另派独立复校员复校）：
  - print PDF `Lucerna-VOL4-JA-EN.pdf`：27,440,477 字节，sha256 `c29f6f987ba709082145c4ca71b7a656eb0b6bcc5f5f49d89f22b35a6161bbeb`
  - web PDF `Lucerna-VOL4-JA-EN-web.pdf`：4,428,571 字节（< 7 MB），sha256 `9d10efc5fdc72c1c46194eea25cb5ff7b59f52c316a13fb5564395439396beb1`，文字层与 print 逐字节一致
  - `2026-w47-ja-en.text.md`：45,706 字节，1348 行（源 SVG 导出）；`ABSTRACT.txt`（en 一行）；`WEEKLY-KIT.md`（en 版）。
  - 门禁：run.py exit 0 零溢出；occlusion 0 flags（自检通过）；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137,138,139,140]；freeze 直接 sha256 两次构建 8/8 相同；P8 最小字号 9.975pt；§1.1 grep 审计（纸 1×/页、旧色 0×、`·` 0×、徽章三色、刊头 196px、页码行 `Page N of 8`）；8 版目视全过；150 键逐键比对（仅 E 组 4 键差异，余 146 键与核心逐字节同）。
- **P8 溢出已修（根因已查明）**：`Flow.para(split=False)` 每条目实际推进 `size + 行数×size×lh + gap`（每条 13.3px 基线开销），而 `_fit` 只算 `行数×size×lh + gap`，故无声超填、末栏钳制后 145–150 六条重叠在 y=2553.3。解法（SOP §1.1 第 2 步，只缩注记、不碰键）：12 条注记（19 条目）各缩为一行，wrap() 事前验算 + 全流模拟事后验证；P8-keys 止于 2426（底线 2540，余 114px）。
- **P1 LINEX 已修**：本周词英文 gloss 包 3 行，末行 `fortune.`（基线 1891.6）被 row-B 分隔线（y=1884）划过；缩为 2 行（末基线 1865.9，清约 13px），重审 0 flags。
- **分类器漏网 3 处（其余 9 语建 map 时必补的键）**：根因是分类器 ZH 标记集里没有这些字，且 apply.py 的残留检查豁免一切不在 map 里的核心字面量，故漏网无人拦。
  1. P8 刊头 `答え　参考答案 — 按版面分页排列，找到题号即可` → en `答え　Answers — grouped by page; just find your number`（W46 惯例 + §1.1 全角空格，宽度验过）。
  2. P7 A2 桥 `酉の市 酉之市　熊手 熊手　手締め 拍手` → `酉の市 Tori-no-ichi　熊手 kumade　手締め hand-clapping`。
  3. P7 B1 桥 `ノミネート 提名` → `ノミネート nomination`（之/提/拍皆为日语亦合法汉字，标记集查不出；桥的格式本就是“日语词 + 读者语注释”，W46 同式）。
  - 三键已补入 `map-keys.json` 与 `map-en.json`：现为 **224 键**（map-en：221 map 键 + 6 instr，含 instr-only 3 键 = 224）。其余 9 语 map 按同一 224 键写，不必重查。
  - 另核查：全部 575 条冻结核心字面量（bridge/gloss 参数、`=` 字面量、短 CJK 字面量）已扫过，无更多漏网中文注释；其余未入 map 者皆为冻结日语（小节头、题干、图注、金句等）或 apply.py 结构编辑已处理者（content7 披露、content8 f-string 模板）。
- **另修**：13 处 `·` 分隔符（12 条配对注记 `· 字母` + P8 刊头 `·`）按核心式改为空格 + 字母 / 全角空格，8 版 SVG grep 皆为 0。
- 构建日志：`build-en-run*.log`（run9 为终版内容，run10 为 freeze 复跑）、`en-occlusion-run9.json`、`en-p8compare-run9.json`、`en-p8-final.json`、`en-sha-run9.txt`、`probe-p8wrap.py`、`probe-p8short.py`、`probe-p8sim.py`、`probe-p8cols.py`、`apply-p8short.py`、`export-textmd-en.py`，均在 scratch-fanout-ja/。

## 第 3/4 棒进展（补记，第 6 棒 2026-11-11 01:31 UTC 写入）

**来源：交接 handoff（第 3 棒 7d968e66、第 4 棒 06736ae6 的交接记录），未经盘上复核的部分已在下文标注。第 6 棒开工时盘上报告仍只写到第 2 棒状态，本节为补记，非第 6 棒实测。**

### 第 3 棒（7d968e66）
- 待办 1 已完成，但有一处修正：分类器只加了「扑/红」，**未加「移」**——三字全加会误伤 5 条纯日文正文（因「移」为日中共享字）。【未经盘上复核：误伤 5 条的具体条目未在盘上留存】
- translate-list 216→218；map-keys.json 重算为 **221**；map-en.json **218 + instr-only 3 = 221** 对齐。
- apply.py en 跑通；en 版 run.py exit 0，但 **P8-keys 7 行 FLOW OVERFLOW（末行 y=2569，底线 2540）**；8 个 SVG 完好。
- 停手于 P8 溢出分析脚本 `p.save()` 报 EDQUOT（Disk quota exceeded）。【未经盘上复核：溢出末行 y 值与停手细节取自 handoff，未在盘上重验】

### 第 4 棒（06736ae6）
- 开工两次探针均通过（01:04:23 UTC）；核心 SHA 已核对（print 以 `e1782168` 开头、web 以 `7c21329c` 开头）。
- 01:05 UTC 前后写 P8 溢出探针脚本 `probe-p8wrap.py` 时报 Disk quota exceeded，**停工记录 3 未能落盘**（内容已交接替棒，即本补记所据的 handoff）。
- en 版 SVGs 完好、run.py 结果有效（P8 7 行溢出待修）。【未经盘上复核：en 版 SVG 完好性未在盘上重验，由第 6 棒接续时复核】

## ⚠️ 停工记录（写在开头，按任务要求）

**状态：因磁盘配额故障停工，未完成 10 版成品。**

- 第 1 次：2026-11-10 约 00:40 EST 前后，`sed -i` 改 `classify.py` 时报 `sed: couldn't open temporary file ./sed8sPzrc: Disk quota exceeded`。当时 `df` 显示 /home/hatch 仍有 46G 可用。随后一次 `muse.write` 探针（probe3.txt）成功，判断为偶发，改用 `muse.edit` 继续，未硬锤重试。
- 第 2 次：2026-11-10 约 00:47 EST，`python3` 覆写 `classify.py` 与写 `translate-list.json` 时两次报 `OSError: [Errno 122] Disk quota exceeded`。两次故障间隔约 7 分钟，期间多数写操作正常，属间歇性配额故障。
- 按任务硬性要求（遇 Disk quota 立即停手、不硬锤重试），**已停止全部构建工作**，不做第 3 次尝试。10 版成品一版未建成。磁盘本身 `df -h` 仍有 45G 可用、inode 计数为 0（未提供），故障原因未明，需 parent/运维核查配额或换时段重开。
- 开工时的两次写探针均通过：`git hash-object -w`（PROBE1-OK）、scratch 写 probe2.txt（PROBE2-OK）。核心版 SHA 已核对：print `e1782168d89d06cd080dd7acf62b6dafc69ca7dc5c6c839e698e25c3de2466bd`、web `7c21329c89efcda759e5aeb91fffd7ac47871b36a6a03a29652f7ccf598c5a1c`，与任务一致。

## 已完成的工作（均可复用，不要重做）

### 1. 上一棒准备工作盘点（已核查）
- `w47-inventory.json`：W47 core-ja 全部 CJK 字面量清单（911 条含重复，630 unique）。可用。
- `worklist.txt`：630 条字面量（按文件顺序）。可用。
- `tm*.json` / `tm2*.json` / `miss*.json` / `miss2*.json`：W46 TM，W47 命中率极低（53/630），**基本不可用**（W47 内容几乎全新）。结论：放弃 TM 路线。
- `tm_build_ja.py` / `tm_build_ja2.py`：TM 构建脚本，已跑完，无需重跑。
- `tr-en.json`：**损坏**（写一半被截断，5001 字节，缺收尾）。已用正则抢救出 54 条，与 `tr-en-34.json`（48 条）合并为 `tr-en-merged.json`（102 条，全部是有效 W47 字面量）。`tr-en.json` 原文件保留未动。
- `w47-counts.json`：字面量频次表。可用。

### 2. 分类器（新写，可复用）
- `classify.py`：AST 角色分类 + 简化字标记集，输出 `translate-list.json`（213→216 条，见下）与 `ambiguous.json`。已修正 4 轮误判：
  - `入`/`写` 从标记集删除（日语 `入る`/`写真` 误伤）；
  - `录/快/讯` 加入；
  - `band()` sub、`caption()` credit 下标修正（credit 是 arg5，`第8面` sub 是纯日语，不译）；
  - **未落盘的第 5 轮修正**：`扑/红/移` 应加入标记集（见“待办 1”）。
- 当前 `translate-list.json` = 216 条（对应 `map-keys.json` 219 条，含后加的 7 条：`全部` + `第1/2/3/4/7面` + `译注｜`）。
- 关键分类裁定（均有 W46 `2026-w46-ja-en` 实盘为证）：
  - 练习小节头 `A　理解` / `B　数字` / `C　数字と日付` / `C　ことばと記録` / `C　文を作りましょう` / `D　ペアにしましょう` / `D　正しい・正しくない` / `B　グラフ` / `C　数字と事実` / `D　文を完成しましょう` / `B　ことば` / `B　一般問題`——**一律冻结（日语）**，上一棒 `tr-en` 里对其中 8 条的英文翻译是错的，已废弃。
  - `スポーツ　体育`、`例： `冻结（W46 同样保留）。
  - 练习类型标签要译（W46 惯例）：完成句子→fill-in、单选→multiple choice、完形单选→cloze、词汇配对→matching、造句→sentence building、判断对错→true/false、翻译→translation、写作→writing。
  - E 组 4 个答案键是中文句，**必须译成读者语**（W47 核心已统一 JA→读者语方向；W46 英版 p8compare 为 CLEAN 但 keydiff=[137,138]，即 E 键差异是既定例外；W47 预期 keydiff=[137,138,139,140]，status 仍为 CLEAN）。

### 3. 构建器（新写，可复用）
- `apply.py`：`tools/venv/bin/python apply.py <lang>`，读 `map-<lang>.json`，复制 core-ja 到 `fanout-ja/2026-w47-ja-<lang>/`，做结构编辑 + 按 map 替换 + 校验。【已跑通：en/de/fr/es 四版日志均 OK，见本报告顶部审计节；下文"尚未跑通过"已过时。】结构编辑包括：5 个 content 文件的 OUT 路径、`render.py` 的 BASE 与 PDF 名、`bslib4.py` 的页脚 f-string、content7 的 ld/lcn 披露（ld_<lang> 单段 + 删 lcn + 改 lh 公式与渲染）、content8 的 3 个 f-string 模板（写作桥、范文注记、页分隔符）、`svglib.py` 复制并校验 md5 `74177544422fe677639d769cd80499fb`。校验：全部 map 键须在核心出现、替换后无残留、残留简体中文扫描、py_compile。
- 冲突处理：`instr="翻译/造句/写作"` 先于裸 map 替换（W46 顺序：instr 值与类型值不同，如翻译→Translate vs translation）。
- `apply.py` 尚未跑通过（无 map 完整版时不能跑）。【已过时：第 3/6 棒已跑通 en/de/fr/es。】

### 4. 英文 map（已完成 219/219 键，待最后一次校验）
- `map-en.json`：meta（含页脚 `Lucerna　JAPANESE WEEKLY VOL.4　Japanese text　English explanations`、披露、P8 模板、PDF 后缀 `JA-EN`、abstract）+ instr（6 条）+ map（219 条，其中 92 条复用 `tr-en-merged` 并逐条抽查过，127 条新写）。
- **待办 1（小修，未做）**：【已过时：第 3 棒已做、第 6 棒复核，见本报告"第 3/4 棒进展（补记）"与顶部审计节。】`map-keys.json` 需补 2 条 band sub（分类器漏网：`レベル B1　相撲3日目まで　相扑前三天`、`レベル B2　紅葉は京都へ　红叶移向京都`——漏因是 `扑/红/移` 不在标记集）；`map-en.json` 需相应补 2 条英文值（已拟好，见下）并删 9 条多余键（8 条冻结小节头 + `スポーツ　体育`，系 tr-en 误带）、补 4 条图注（见下）。修完后 map 应为 221 条键，与 `map-keys.json` 逐键对齐。
  - 补：`レベル B1　相撲3日目まで　相扑前三天` → `レベル B1　相撲3日目まで　Sumo: the first three days`；`レベル B2　紅葉は京都へ　红叶移向京都` → `レベル B2　紅葉は京都へ　Leaves move to Kyoto`。
  - 删：`A　理解`、`B　ことば`、`B　数字`、`C　ことばと記録`、`C　数字と日付`、`C　文を作りましょう`、`D　ペアにしましょう`、`D　正しい・正しくない`、`スポーツ　体育`。
  - 补图注：`写真：Poliphilo — CC0（Wikimedia Commons）` → `Photo: Poliphilo — CC0 (Wikimedia Commons)`；`写真：Alainauzas — パブリックドメイン（Wikimedia Commons）` → `Photo: Alainauzas — public domain (Wikimedia Commons)`；`写真：lumoplank — CC0（Wikimedia Commons）` → `Photo: lumoplank — CC0 (Wikimedia Commons)`；`写真：Mozzucu — CC0（Wikimedia Commons）` → `Photo: Mozzucu — CC0 (Wikimedia Commons)`。
- 其余 9 语 map 均未开始（须按同一 221 键逐语写；zh-tw 可先由简转繁再人工校对）。

## 待办（第 7 棒 2026-11-11 03:45 UTC 订正：下述旧待办已过时，以此为准）

1. ~~待磁盘恢复后，先重做一次写探针~~——已做（第 7 棒开工探针双通，见本报告顶部审计节）。
2. ~~完成待办 1（classifier 加 `扑/红/移` 后重跑、重算 `map-keys.json`、修 `map-en.json` 至 221 键对齐），再跑 `apply.py en`~~——已完成（第 3/6 棒；en/de/fr/es 的 apply 日志均 OK，map-en 218 键、map-de/fr/es 221 键）。
3. en、de、fr 三版已完成并通过第 7 棒审计（见顶部）；es 由 sibling 收尾，第 7 棒已验（见顶部审计节）：es print 29,102,097 B sha `0feb6113…`、web 4,482,717 B sha `b274eac2…`，门禁全过，无缺项。
4. 其余 7 语分工（第 6 棒 04:30 UTC 定）：**第 7 棒的 it、pt、nl、ru 均已完成并通过自查**（见顶部逐版记录）；**ko、zh-tw 由第 6 棒接手，第 7 棒勿碰**（fanout-ja/ 下已有 2026-w47-ja-ko 与 2026-w47-ja-zh-tw 目录，属第 6 棒在建）。第 7 棒本棒收尾。
5. 每版自查零问题才算完成；独立复校由协调员另派。

## 关键裁定备忘（勿忘）
- P8 题干 10.35pt 不动；刊头 147pt、头条 42pt、边距 66pt 与核心一致；无首字下沉可接受；中文数字带空格按全周口径不修（ko 除外）。
- りくりゅう：P7 gloss 与 P8 答案用 romaji `ryuuryuu`（各版通用，不改写）；ちいかわ：中文读者版用 `吉伊卡哇`，其他读者语用本语译名（EN `Chiikawa`、ko `치이카와`、ru `Чикава`、拉丁语系 `Chiikawa`）——`吉伊卡哇`是中文译名，不得原样塞进英文等他语版（属他语残留）。
- 趋势盒来源行（P1 `来源与日期见各篇文章，非精确统计`）是单行 `p.text`，无折行：各版译文须短到能塞进 400px 盒（EN 已定为 `Sources and dates are in the articles`；de/ru 等须实测 `text_w`，超了就缩短）。
- `match_set` 的 instr 位于 x+196，译文须短（EN `Match words to meanings` 已是上限；de 用 `Zuordnen`、fr `Associer`、es/it/pt `Relacionar/Abbinare`、nl `Koppelen`、ru `Соотнесите`、ko `짝 맞추기`、zh-tw `配對`）。
- P7 披露盒：译文行数变化会顶 P7 teaser（核心 teaser 止于 2542.58、页脚 2580，仅 37px 余量），每版须看 `P7 teaser ends` 打印值与卡片图，超了就缩短披露。
- F-MAIL：各版只印编辑部示例 + 双语延期披露（披露译成读者语），不编造、不查邮箱。
- 成品目录：`~/workspace/weekly-git/production/2026-w47/fanout-ja/2026-w47-ja-<lang>/`（任务指定只在此目录与 scratch-fanout-ja/ 工作；`fanout-ja/` 尚不存在，需新建；协调员后续是否移入 `production/2026-w47/` 直属目录由其定）。
- 命名：print PDF `Lucerna-VOL4-JA-<LANG>.pdf`（如 `Lucerna-VOL4-JA-EN.pdf`），web PDF `Lucerna-VOL4-JA-<LANG>-web.pdf`（仿本周 en-de/de-en 的 `The-Lucerna-VOL4-en-de.pdf` 惯例，刊名 Lucerna 不变）。
- 字体：沿用核心 `svglib.py`（Noto CJK，md5 已校验），不改字体；每版目视查豆腐块。
- 禁止：insert.py / lint --write / git push / add / reset / stash；不改核心、不碰 W43/W45/W46、不改 tools/p8.py 与 freeze.py。

## 第 3/4 棒停工记录（重建补记，接替员 2026-11-11 14:26 EST 写入）

**来源：据协调员 run-log（`hidden_files/w47/run-log.md`）L655 / L691 / L724 / L855 重建；#3/#4 handoff 原文不在盘上。** 本棒只追加、不改写已有内容。本节与报告既有「第 3/4 棒进展（补记，第 6 棒 2026-11-11 01:31 UTC 写入）」（第 168 行起）部分重叠：既有补记已记 7d968e66 / 06736ae6 两棒，本节补上 d59b4b29 的拦停记录、两条已裁定规则与证据缺口，并标明口径冲突。

**棒次编号口径冲突（以 agent id 为准，不作裁断）：** 本补记所据任务书称 d59b4b29 为 #3、7d968e66 为 #4；报告既有补记称 7d968e66 为「第 3 棒」、06736ae6 为「第 4 棒」；run-log L711 又称 cdeea8be 为「第四棒」。三者互斥。下文一律以 agent id 指代，棒次仅作原文引用。

### d59b4b29 拦停时状态（run-log L655，2026-11-10 21:15–21:50 EST / 00:39–00:52 UTC EDQUOT 波次）

- **0/10**，一版未建成。
- `map-en.json` **219/219 已完成**（见本报告「已完成的工作 §4」）。
- **待办 1 未做**：分类器加 `扑/红/移`、map 补 2 删 9 补 4 图注 → 221 键对齐（补 2 条 band sub、删 9 条多余键、补 4 条图注英文值，见 §4 待办 1）。
- `apply.py` **已写未跑**；其余 9 语 map 未开始。
- **已派接替 7d968e66**（先做待办 1，再 apply.py en 起逐版做；成品在 `production/2026-w47/fanout-ja/2026-w47-ja-<lang>/`，事后是否移入直属目录由协调员定）。

### #3/#4 往前推的一步（只存于 handoff，run-log L691 / L724）

- 分类器只加了 `扑/红`（未加 `移`——三字全加误伤 5 条纯日文正文，已回退；见既有补记与「停工记录 2」）。
- map **218 + 3 = 221 对齐**（map 218 条 + instr-only 3 条 = map-keys 221，逐键对齐无缺漏、无多余）。
- `apply.py` en 跑通。
- en 版 `run.py` exit 0，但 **P8-keys 7 行 FLOW OVERFLOW**（末行 y=2569，底线 2540）。
- 上述四点与既有补记（第 168 行起）及「停工记录 2」（~01:00 UTC，7d968e66 停于 P8 溢出分析脚本 `p.save()` 报 EDQUOT）一致；06736ae6 随后停于 01:05 UTC 写 `probe-p8wrap.py` 时 EDQUOT，停工记录 3 未能落盘（内容已交接替棒，即既有补记所据的 handoff）。

### 已裁定的两条规则（写入报告备查；原文已见本报告「已完成的工作 §2 关键分类裁定」，此处重述为准）

1. **练习小节头一律冻结为日语**（`A　理解` 等 8 条 + `スポーツ　体育` 等）：`tr-en` 里对其中 8 条的英译是错的、**已废弃**。
2. **E 组 4 个中文句答案键必须译成读者语**：预期 p8 compare **keydiff 恰为 [137,138,139,140]**，status 仍为 **CLEAN**。例外：zh-tw 的 137/138 无简体专属字、繁体值与核心逐字节相同，故 zh-tw 正确值为 [139,140]（见本报告第 6 棒 zh-tw F3）。

### 证据缺口（run-log L855，2026-11-11 ~07:35 UTC 批量回报）

- `FANOUT-REPORT-ja.md` 与 `map-*.json`、`apply.py`、`gen-map-*.py` 在 **#8 开工时盘上不存在**（疑 VM 重启丢失）；#8 新建报告只写本棒实测。
- **221 键对齐无法从 map 文件直接重验**——间接证据成立（freeze 8/8 + p8 CLEAN + 目视干净 + 残留扫查 0）。ja 各 proof1 复校员亦全部独立重跑门禁，结论不依赖缺失文件。**记为证据缺口，非待办。**
- **本棒核查时现状（2026-11-11 14:26 EST，只读核查）：** 上述文件现已在盘上，与 #8 开工时缺失的状态不同——`map-*.json` 10 语齐全且每份 map 均为 **221 键**（meta 8、instr 6；`map-keys.json` 为 list、共 224 条 = 221 map 键 + instr-only 3 条 `判断`/`填空`/`把词和释义配对`；`map-en.json` 含第 6 棒补入的 3 条分类器漏网键）；`apply.py` 在位（9,666 B）。`gen-map-*.py` / `build-map-*.py` 仅存 5 份：`gen-map-it.py`、`gen-map-ko.py`、`gen-map-zh-tw.py`、`build-map-nl.py`、`build-map-ru.py`；en/de/fr/es/pt 的生成脚本仍不在盘上。本段现状不推翻 L855 的历史记录——缺失发生于 #8 开工时，之后的文件由 #6/#7 及后续重建波次写回。

## 收尾审计附录（接替员 2026-11-11 14:26 EST 实测，只读核对，未重建、未重跑门禁）

- **生产目录：** 10 版目录全部在位，但位于 `production/2026-w47/fanout-ja/2026-w47-ja-<lang>/`；`production/2026-w47/` 直属目录下**没有** `2026-w47-ja-*`（移入直属目录一事协调员未定，本棒不动）。
- **印/网/文三件 + ABSTRACT + KIT：** 10/10 齐全（每版均有 print PDF、web PDF、`.text.md`、`ABSTRACT.txt`、`WEEKLY-KIT.md`）。
- **KIT 齐全性：** 10 份 KIT 全部在位，且每份 KIT 内均含本版当前磁盘 print/web PDF 的 SHA 前缀（逐份 grep 实测命中）——KIT 与磁盘一致。
- **报告 SHA 已过期（10/10）：** 本报告各版 SHA/字节写于 05:11 UTC 前，与磁盘现状（07:32–08:51 UTC 重建波次后的文件）**全部不一致**。磁盘实测表如下（`sha256sum` + 字节，2026-11-11 14:26 EST）：

| 版 | print PDF（字节 / sha256 前 12） | web PDF（字节 / sha256 前 12） | text.md（字节 / sha256 前 12） | 报告称 print（字节 / sha 前 8） |
|---|---|---|---|---|
| ja-de | 29,102,625 / 2047035bdaa9 | 4,483,728 / 8db59bf122c7 | 46,520 / 6323cd14109c | 29,102,629 / b5d66e17 |
| ja-en | 27,440,481 / 38b0d3ab8db7 | 4,428,575 / 95cf9e66f51a | 45,706 / 8374230f772c | 27,440,477 / c29f6f98 |
| ja-es | 29,102,102 / 9947b70c00a3 | 4,482,721 / 49665374de81 | 46,684 / 81993361c31f | 29,102,097 / 0feb6113 |
| ja-fr | 28,348,000 / 1f3b28f4eae5 | 4,458,587 / 4f02e8c8f9de | 46,882 / 420616e6b601 | 28,347,993 / 5903a36b |
| ja-it | 29,099,163 / 8ed65a83d179 | 4,476,985 / d8af211a19b8 | 46,678 / 71a2d7d21e57 | 29,099,162 / 75986cd7 |
| ja-ko | 28,189,450 / 8c6b7566e6ef | 4,550,444 / 133f57264a82 | 47,722 / b20d5bc686ff | 28,189,461 / fbcfe840 |
| ja-nl | 29,099,141 / c8b82a8491a0 | 4,476,527 / 7a7f5fc96730 | 45,627 / f823709e214d | 29,099,171 / c18c551a |
| ja-pt | 29,103,009 / 9591f16cb82a | 4,485,030 / f0cdce302756 | 46,696 / 53bc548ba01c | 29,103,006 / 5e7542bc |
| ja-ru | 25,858,387 / 86af0bb5bd5f | 4,396,966 / dd5fdc63020f | 53,029 / 4f6b2fc05e78 | 25,858,425 / abc44c9c |
| ja-zh-tw | 26,034,639 / a2640e158bf5 | 4,788,063 / 00575aa26837 | 44,361 / 8c18a0e9fb47 | 26,034,686 / 7b23a2c4 |

  完整 sha256 见本棒 handoff 回报。磁盘值与 run-log L1294 的 ja-ru proof2 记录一致（印 25,858,387 B、SHA 86af0bb5…），属 07:27 UTC 后 fix1/重建波次的产物，非报告笔误。本棒未重跑门禁，不对门禁结论再背书。
- **报告内未闭合的待办项（清单，待协调员定，本棒不自行开工）：**
  1. **待办第 5 项**（第 228 行起「待办」一节末条）：「每版自查零问题才算完成；独立复校由协调员另派。」——报告内未记录各版 proof1/proof2 结果。run-log L1294 称 ja-ru proof2 (a) 09:24 UTC、ja 家庭 10/10 定稿，但本棒未逐版核实 proof 记录，是否已闭合**待协调员定**。
  2. 其余待办项均已闭合或标注已过时：第 1 项（写探针）已做；第 2 项（待办 1 + apply en）已完成；第 3 项（en/de/fr 审计 + es 收尾）已完成；第 4 项（it/pt/nl/ru + ko/zh-tw 分工）已完成。「停工记录 2」末的「接替者待办」四条亦已由 #6/#7 做完（P8 溢出已修、10 版已建成并通过自查），属历史记录，无新增动作。
  3. 报告内已过时但未清理的陈述（非待办，仅备查）：§4「其余 9 语 map 均未开始」（现 10 语 map 齐全，221 键）；zh-tw 节「ru 在第 7 棒手中，报告尚无完成记录」（ru 完成节已在报告顶部）；待办第 2 项称「map-en 218 键」（现 `map-en.json` 为 221 键，含第 6 棒补入的 3 条漏网键）。
- **是否还有需做的 ja fan-out 工作：没有。** 10 版已建成、三件 + KIT 齐全；剩余事项（独立复校是否闭合、成品是否移入直属目录、报告 SHA 表是否更新）均属协调员定夺，不在本棒分工内。等协调员派单。
