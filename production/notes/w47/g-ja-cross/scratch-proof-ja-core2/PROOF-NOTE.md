# PROOF-NOTE — 2026-W47 core-ja 修复后全量复校（第二轮，re-proof）

- 复校员：独立复校（与 core-ja builder / fix1 builder 不同人）
- 日期：2026-11-11（EST 08:19 开工探针，约 08:20–09:00 复校）
- 对象：`production/2026-w47/core-ja/`（`2026-w47-ja-zh-cn`，VOL.4，核心读者 zh-cn）
- 依据：SOP.md 全文（已读）；`hidden_files/w47/briefs/brief-coordinator.md`
  （注：任务所给路径 `~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md`
  不存在，实际位置为 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`，已读）；
  fix1 FIX-LOG.md / GATE-LOG.md 只作参考，结论全部自己重核。
- **结论：(a) 零问题**（SOP §8.4）。fix1 的 1 处改对，无新缺陷。
  观察项 3 条（O1–O3，见 §5），不计缺陷。另案报告 1 项（R1，KIT §3 罗马字，见 §6）。

## 0. 开工探针与成品身份核对

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `hidden_files/w47/scratch-proof-ja-core2/.probe` 真实写盘成功。复校全程未遇
  Disk quota exceeded / EPERM。
- 三份成品实测（与任务给定完全一致）：
  - 印刷 `Lucerna-VOL4.pdf`：26,018,019 B /
    `20b9d50469fbb6ca6470c17becb2790a30f69191d9083520a9270ea7ebbe9ab4`
  - 网页 `Lucerna-VOL4-web.pdf`：4,652,763 B /
    `8722bdfbcec0478a7a60fc86ab0ee7cc9333f957253959476d4f608eed82d5b0`
  - text.md `2026-w47-ja-zh-cn.text.md`：44,432 B /
    `bcfa667da57e2f477b9d825200b98db454ade3c1dde6ec92ea3d446b0bf9926a`

## 1. fix1 回归核查（全部独立重核）

### 1.1 `一之富士` 必须为 0（读者可见交付物）

| 位置 | 计数 |
|---|---|
| content\*.py | 0 |
| text.md | 0 |
| svg/（8 份） | 0 |
| 印刷 PDF 文字层 | 0 |
| 网页 PDF 文字层 | 0 |

注：KIT §11 / FIX-LOG 的修补记录行文里保留旧形作历史记录（KIT §11
"首日战胜大之里的是一之富士"、FIX-LOG §1–§2），不计——那是内部生产
记录，不是读者可见交付物。读者可见交付物（源码、text.md、SVG、双 PDF
文字层）中为 0。

### 1.2 `义之富士` 各处为 2×

| 位置 | 计数 | 位置明细 |
|---|---|---|
| content\*.py | 2 | content34.py:186（key 47 简析，已改）、content8.py:20（key 115 简析，原已正确） |
| text.md | 2 | :1247（key 47）、:1319（key 115） |
| svg/ | 2 | p8-tesuto.svg 2 处 |
| 印刷 PDF 文字层 | 2 | key 47、key 115 答案行 |
| 网页 PDF 文字层 | 2 | 同上 |

### 1.3 key 47 与 key 115 指同一人 ✓

- key 47 题干（content34.py:187）：「初日に大の里に勝ったのはだれですか。
  A. 義ノ富士 B. 美ノ海 C. 藤凌駕」，键 A，简析「首日战胜大之里的是义之富士」。
- key 115 题干（content8.py:21，P8 A 组）：「大の里は初日、義ノ富士に（___）ました。
  (A. 負け B. 勝ち)」，键 A，简析「大之里首日输给了义之富士」。
- 同一事实（初日大の里败给義ノ富士），同一人。公开来源核实见 §4：
  スポニチ / サンスポ / デイリー / スポーツ報知 / 読売均报大の里初日败给小結義ノ富士（突き落とし）。

### 1.4 日文正文确为 義ノ富士 ✓

- content34.py:120（P4 正文）：「2場所連続優勝をねらう大の里が、小結の義ノ富士に
  突き落としで敗れました。」
- content34.py:187（key 47 题干）、:189（key 48 选项 A）均为 義ノ富士。
- content8.py:21（key 115 题干）为 義ノ富士。
- py 内 義ノ富士共 4 处；text.md 内完整字符串 2 处（:449 P4 正文、:1048 key 115 题干；
  key 47 题干在 text.md:509–510 行被导出换行拆为「義ノ / 富士」，故整串计数为 2——
  已逐行核实，非缺失）；SVG 内完整字符串 2 处（P4 正文 1、P8 key 47 题干 1；
  key 115 题干在 SVG 内亦跨 <text> 换行）。PDF 文字层：key 47 题干与 key 115 题干
  均完整呈现 義ノ富士（pdftotext 抽查确认）。
- 「一之酉」（content12.py:261 / text.md:1217，key 19）是一之酉（Ichi-no-tori），
  正确，未动。繁体形「義之富士」全核心 0 处（简体读者版用 义之富士正确）。

### 1.5 fix1「仅 1 处、其余一字未动」独立验证 ✓

- 与 fix1 留下的修前 text.md 副本
  （`scratch-ja-fix-core1/textmd-prefixed.md`）逐行 diff：**仅 1247 行一处差异**
  （一→义），1356 行其余逐字一致。
- freeze 两轮重建的 8 份 SVG 与交付 SVG 逐字节一致（见 §3），其中 p8 哈希
  `f7118644ac8b31a4be2f04c7044afd0a9043592bfd89d1b45c1b0526c08798a2`
  与 fix1 声称的新 p8 哈希一致；P1–P7 哈希与 fix1 记录的修前值一致
  （57fc0095… / d3832914… / 6df4720c… / 55c0a4dc… / d9d2cff9… /
  641d7b67… / 537fd28c…）。

## 2. 全量复校：全文重读（1356 行 text.md + 双 PDF 8 版目视）

- text.md 1356 行逐行重读：P1–P8 正文、译注、图注、练习题干、答案行全部读过。
- 印刷 PDF 8 版 100 dpi 逐版目视（自运 `render-print/p-*.png`），网页版 P8 同
  分辨率目视（`w8-8.png`）；P8 key 47 区另做 300 dpi 放大裁图
  （`p8-key47-crop-proof2b.png`），「47. A — 首日战胜大之里的是义之富士」字形清晰。
- 未发现溢出、重叠、压页脚、图片与出处错位。P2/P3/P4/P6 的特征栏中段空白为
  KIT §7 已披露的 W46 冻结版式，非缺陷。P1 头条流、P7 鸟居图、P8 练习流+
  答案区+寺图均完整，答案流未压页脚。

## 3. 机械门（全部自跑，tools/venv/bin/python）

| 门 | 结果 |
|---|---|
| freeze baseline（第 1 次） | **8/8** SVGs byte-identical；core integrity：运行前后重哈希一致（`freeze1.log`） |
| freeze baseline（第 2 次，同一解释器重跑） | **8/8**，哈希与第 1 次逐个一致（`freeze2.log`） |
| occlusion_audit | 自检通过（6 类 planted 全触发，clean 对照静默）；**0 flags**（`occlusion.json`） |
| p8 extract --total 150 | noted set **150/150**（`p8-extract.json`） |
| p8 compare（core-vs-core 自比） | **CLEAN**，missing=[]、extra_count=0、uncertain=[]、**keydiff=[]** |
| p8 extract vs 修前 extract（`ja-core-p8.json`） | noted 集相等，keys 150/150，**0 key diffs** |
| print/web 文字层（raw pdftotext） | 各 44,818 B，**逐字节一致** |
| print/web 文字层（-layout） | 各 85,061 B，**逐字节一致** |
| text.md validator（SVG 重导出比对） | 重导出（`export-textmd-proof2.py`，fix1 导出器改输出路径版）与交付 text.md **逐字节一致**（1356 行） |
| U+2019 全扫 | SVG 8 份 + text.md + content\*.py 合计 **0** |
| VOL.4 核对 | P1 3×、其余各版 1×（与 GATE-LOG 一致）；刊头 `Lucerna　日语周报 VOL.4` 各版齐全 |
| 徽章计数 | 每题徽章均与登记级别一致（见 §3.1）；P1 目录徽章为版级徽章（A2/B1/B2），与 §4 版级一致 |
| P8 最小字号（PyMuPDF，印刷 PDF） | **9.98pt**（≥9.75pt 门槛）；P8 题干 10.35pt（79 处）；P1–P7 最小 11.62/12.75pt |
| §1.1 grep 审计 | 旧纸色 `#f7f1e2` 0×；禁用金 `#c9a227` 0×；`·`（除图片 base64 外）0×；`第N版／共8版` 1×/版；纸色 `#fbfaf6` 1×/版 |
| 金句 8× 各 2× | 去空白后全文计数，8 条裸句各恰为 2（`ja-core-checks.py` 同口径） |
| 禁忌行首（kinsoku）扫描 | 0 hits |
| ABSTRACT.txt | 323 B，单行、简体中文、无 ASCII 双引号，含刊名/目标语名/A2–B2/150 题与本期真实主题 |

### 3.1 徽章逐题核对

- 按页登记级别 vs 印刷徽章（<text> 元素全匹配计数）：
  P1 登记 10×A2 / 印刷 14（10 题徽 + 目录 4 个版级徽 A2/B1/B1/B2）；
  P2 登记 18×A2 / 印刷 15——25–28 四题共用 1 个组徽章（`25–28.`）；
  P3 登记 A2 7/B1 11 / 印刷 A2 7/B1 8——43–46 四题共用 1 个组徽章；
  P4/P5/P6 各 18 与登记逐题一致；P7 12（A2/B1/B2 各 4）一致；
  P8 登记 A2 9/B1 22/B2 7 / 印刷徽章元素 35——141–144 四题共用 1 个组徽章。
- 文本顺序逐题映射：P1–P7 全部 112 题、P8 全部 38 题，每题就近徽章均与登记
  级别一致，缺徽 0、错徽 0。组徽章（25–28、43–46、141–144）与 W46 同一版式，
  非缺陷。

### 3.2 keydiff [137,138,139,140] 预期的说明

任务所写「keydiff 预期 [137,138,139,140]」是 **fan-out 版 vs 核心** 的预期
（E 组 4 个中文句答案键被译成读者语言，见 scratch-proof-ja-de2/es1/fr1 等）。
本对象是**核心本身**，core-vs-core compare 的正确预期是 keydiff=[]，
实测正是 []。核心 P8 的 E 组键 137–140 本就是中文句（JA→ZH 统一方向，
KIT §2/§7）：
137「二之酉在11月19日。」、138「新酒在11月19日解禁。」、
139「流行语提名在11月5日发表。」、140「去看红叶的人应该同时确认预报日期和现在的状况。」
——已逐条核对题干，日期与事实全保留，无误。

## 4. 150 键逐题复核（登记 vs 印刷答案）

- 登记 dump（freeze build-copy 内重跑 content 模块，`registry-proof2.json`）：
  TOTAL 150，连续 1–150；A2 48 / B1 73 / B2 29；
  分版 10/18/18/18/18/18/12/38；题型与 KIT 一致；范文 154 字。
- 登记键 vs p8 extract 键：仅 1 处差异——150 题（登记「（开放题，范文如下）」
  vs 印刷「✓」），为 W46 既定冻结版式，与修前逐字节一致，非差异。
- 登记「`{n}. {key} — {note}`」vs text.md 答案行（P8 答案区，末现为准）：
  149/150 逐字一致；仅 150 题同上冻结版式差异。
- 另逐题人工核对键值与题干/正文的正确性（事实、日期、星期、算术）：
  P4 相扑 47–64、P6 图表 88–93（38−24=14、38+24=62、合计 100）、
  P6 日期 94–97、P8 A–G 组 113–149 全部复算无误。
  - 47 A（義ノ富士）、48 B（美ノ海）、49 A（藤凌駕）、50 B（2勝1敗）、
    51 C（22日）、52/53 2、54 11、55 7、56 8、57 A、58 B、59 A、60 B、
    61 ×、62 ○、63 ○、64 ×；115 A（負け）、116 A（負け）。

## 5. 事实核查（公开来源，本轮抽查）

- 相扑九州场所 2026（11月8日开幕、福岡国際センター、22日千秋楽）：
  初日大の里败给義ノ富士（突き落とし，含物言い后军配不变）、豊昇龍勝美ノ海
  （押し出し）、霧島勝宇良、琴櫻败给藤凌駕、安青錦败给朝乃山——
  「大関 3 人中 2 人敗れ」「1 横綱 2 大関敗れ」均与スポニチ/デイリー/サンスポ一致。
  2 日目两横纲+3 大关全胜，大の里胜藤凌駕（寄り切り，初白星）、豊昇龍 2 連勝
  （胜朝乃山）、霧島 2 連勝——与スポニチ一致。
  3 日目豊昇龍败给藤凌駕（押し倒し，初金星）、初土俵から 11 場所、年 6 場所制
  （1958 年）以来 7 番目（付け出し力士中最速并列）——与サンスポ/スポーツ報知/
  日刊スポーツ一致；大の里 2 勝目、两横纲 3 日目 2 勝 1 敗一致。
  豊昇龍 3 場所連続休場明け、7 月下旬右膝手術——与サンスポ一致。
  大の里 2 場所連続優勝・7 度目を目指す——与サンスポ一致。
- 酉の市 2026：一の酉 11月7日（土）、二の酉 11月19日（木）、无三の酉；
  浅草鷲神社 0:00–24:00；熊手店约 150——与鷲神社官网引述的二次来源一致。
  长國寺在鷲神社旁一致。
- 博若莱新酒 2026：解禁 11月19日（木，第 3 木曜，0:00）；日本因时差世界最早；
  阪神梅田本店约 40 种——与阪急阪神 PR（2026-11-04）/サントリー一致。
- 流行语大赏 2026：30 提名 11月5日（木）发表（含 りくりゅう、ちいかわ（現象）、
  酷暑日、NISA貧乏、ボンボンドロップシール、好きすぎて滅！、パンチくん、AI暴走）；
  前十+大奖 12月1日（火）14:00、東京會舘——与 ORICON/モデルプレス一致。
  M!LK 楽曲「好きすぎて滅！」一致。
- 红叶：Weathernews 第 3 回予想（10月29日）高尾山 11月13日ごろ、宮島 11月21日
  ごろ、嵐山 11月23日ごろ、香嵐渓 11月23日ごろ、秋月 11月28日ごろ——与
  Weathernews 官方/共同通信 PR 一致；嵐山 11月8日時点约 2 成色づき、見頃
  11月26日ごろ、落葉はじめ 12月12日ごろ——与 KIT 引用的 yuuekiinfo.com
  （11月8日更新）逐字一致；日本気象株式会社第 1 回予想（9月2日）東京 11月29日
  ごろ、大阪 12月4日ごろ——一致；tenki.jp（日本気象協会）嵐山 11月13日
  から——一致。
- 日期/星期（`date -d`，Asia/Tokyo）：11月7日土、8日日、9日月、10日火、
  16日月、19日木、22日日、23日月、12月1日火——与文中全部星期一致。
- 小雪 11月22日、勤労感謝の日 11月23日（祝日）一致。

## 6. 观察项（不计缺陷）与另案报告

- **O1（观察）**：P7 金句栏第 6 条中文译注与答案 66/77/80/105 把「りくりゅう」
  写作罗马字「ryuuryuu」（如「「ryuuryuu」是花样滑冰双人组合」），而同一版
  P7 B1 桥接行写作「りくりゅう 双人滑」。译法本身无误（罗马字可读），
  仅前后译注口径不一致。 cosmetic，不影响答案判定。
- **O2（观察）**：P7 ex 103 选项 B「寝る」未与 A「食べること」/C「買った時に打つ拍手」
  保持名词化平行。答案 C 唯一明确，不影响判定。
- **O3（观察）**：P2「露店は750店ほど」——KIT §3 称引自鷲神社官方「酉の市豆知識」
  （经二次来源），同一节披露 Time Out 称典型年 800–900 店。数字有来源、
  异口径已在 KIT 披露；本轮未能直读神社官网原文，仅作观察，不列为缺陷。
- **R1（另案报告，按任务要求不列为本轮缺陷）**：core-ja KIT §3 趋势叙述里的
  罗马字误拼（Umi-no-umi、Fujiryūga）现状：**仅存于 WEEKLY-KIT.md §3**
  （第 83–88 行，内部生产记录），读者可见交付物（content\*.py、text.md、
  svg/）中为 0。正确罗马字应为 Uminomi / Fujiryūga（藤凌駕的凌读 ryō）。
  任务要求未动，本轮未动，只报告现状。

## 7. 未动 / 未跑

- 只检查、不改任何源码/成品；工作只在 production/2026-w47/core-ja/（只读）
  与本笔记目录；未碰其他家庭、tools/、issues/；未跑 insert.py、lint --write；
  未做任何 git 写操作（除开工探针 `git hash-object -w` 一个小对象）。
- freeze 两轮的 build-copy 在本 scratch 内（`freeze1/`、`freeze2/`），
  未污染生产目录；freeze 自带 core-integrity 守卫确认交付 SVG 未被改动。

## 8. 工作文件

- 本笔记：`hidden_files/w47/scratch-proof-ja-core2/PROOF-NOTE.md`
- 门日志：`hidden_files/w47/scratch-proof-ja-core2/GATE-LOG.md`
- `freeze1.log` / `freeze2.log` / `freeze1.json` / `freeze2.json`
- `occlusion.log` / `occlusion.json`
- `p8-extract.log` / `p8-extract.json` / `p8-compare-self.log` / `p8-compare-self.json`
- `registry-proof2.json`（登记 dump）、`dump_registry.py`（登记导出脚本，
  原在 freeze1/build-copy 内，复校后已移至本目录根）
- `textmd-reexport.md`（SVG 重导出 text.md）/ `export-textmd-proof2.py`
- `render-print/p-1.png` … `p-8.png`（印刷 PDF 100 dpi）、`w8-8.png`（网页 P8）、
  `p8hi-8.png`（印刷 P8 300 dpi）、`p8-key47-crop-proof2.png` /
  `p8-key47-crop-proof2b.png`（key 47 放大裁图）
