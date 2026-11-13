# PROOF-NOTE — W47 fr-ja proof1（独立复校）

- 版：`production/2026-w47/2026-w47-fr-ja/`（法语核心 × 日语读者版，fr fan-out #1，未 commit 未 push）
- 复校员：独立复校（与构建者不同人）；只读生产文件，**未改任何生产文件、未 commit、未 push**
- 时间：2026-11-11 07:48–08:05 EST；解释器 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 为 goals 侧 scratch tmp（未用 /tmp）
- 探针：`/dev/null` 存在、`git hash-object -w` 通（`9daeafb9…`）、goals 侧写文件通，探针通过后开工

## 结论：(b) 不定稿

机械门 15/15 + freeze 8/8 + 确定性 8/8 + 150 题三源交叉 + text.md 全文通读 + 8 页逐页目视全部通过，
**唯一未过项为三处孤儿句号 D1–D3（禁则缺陷：句号「。」单独成行，目视确认）**。
修复后重跑全套门禁 + P1/P4/P6 重验。

## 缺陷清单

三处同一缺陷类：日语流式文本换行时句号「。」被甩到下一行独占一行（禁则/kinsoku 违规：句号不可行首）。
均为日语讲解层字符串在 ja 版栏宽下换行所致；三处均已在全分辨率渲染上目视确认（裁切图见 `png/p1-gloss.png`、`png/p4-comp.png`、`png/p6-cal.png`），
SVG 文本元素实测与之一致。修复方向：把三串各缩短 1–2 字（或使流式换行禁则感知），使「。」回到末行行尾；修后重跑全套门禁。

| 编号 | 位置 | SVG 实测 | 字符串（expl.py 键） | 目视 |
|---|---|---|---|---|
| D1 | P1 解説 gloss 盒，x=556.5 | 末行基线 y=1366.65，独行「。」（20.5pt，x=556.5）；前行 y=1336.9 `primeur 新酒　le beaujolais ボジョレー` | g1：`…trancher 決める、裁く　un vin primeur 新酒　le beaujolais ボジョレー。` | `png/p1-gloss.png` 确认：句号独占一行 |
| D2 | P4 比较级小标题下，x=538.5 | 末行基线 y=1722.92，独行「。」（20.5pt，x=538.5）；前行 y=1693.2 `比較級（plus / moins）で文を完成させよう` | bridge_comp4：`比較級（plus / moins）で文を完成させよう。` | `png/p4-comp.png` 确认：句号独占一行 |
| D3 | P6 LIRE LE CALENDRIER 副行，x=88.0 | 末行基线 y=1941.225，独行「。」（20.5pt，x=88.0）；前行 y=1911.5 `上のカレンダーを読んで正しい答えを選ぼう`；该串 text_w 428.2px（20.5pt sans）超出栏宽 | bridge_chart：`上のカレンダーを読んで正しい答えを選ぼう。` | `png/p6-cal.png` 确认：句号独占一行；P6 全页目视亦可见 |

说明：core-fr 同缺陷类仅一处、不同位置（P4 `chiffres_note` 中文串 `大师赛决赛结果与都灵名单见本版正文。`，孤儿「。」基线 y=550.53，x=1461.5）——
属核心既存同类问题，不构成本版新缺陷的豁免理由；本版三处均为 ja 版新串新位置，须修。

## 记录项（只记录，不计入本版判定）

- **R1 — Q148 核心继承问题**：题干 `On se retrouve ___ du cinéma ?` + 键 `devant`。
  核心 `core-fr/content8.py:176` 原文即此对话（`gnums[3]` 占位），本版 `content8.py` 与核心字节相同（source_freeze 通过）。
  三源一致：P8 抽取键 `devant` / text.md 答案区 `148. devant（映画館の前）` / 核心键 `devant`。核心轨道另修，本版不计。
- **R2 — D5 字体（全周级已知待定项）**：拉丁讲解层落在 Noto Sans CJK SC。
  本版实测：全 1,985 spans；Noto Sans CJK SC 980 段（Regular 518 + Bold 462），其中纯拉丁文（无 CJK 字符）559 段（Bold 400 + Regular 159）；
  Noto Serif CJK SC 63 段，其中纯拉丁 17 段；DejaVu Sans 4 段（P7 ✗ 标记）；Newsreader 937 段。
  核心对照：core-fr 全 1,972 spans，CJK 字体中纯拉丁 560 段（Bold 398 + Regular 145 + Serif 17）——本版仅 +16 段，主体系核心继承，不以此判 (b)。

## 特别核查：P7 读者园地奶油盒（独立实测裁定，未采信跨版目测）

- 盒：`p7-langue.svg`，`x=989.0 y=1878 w=873.0 h=380`，盒底 2258.0（creambox canonical 扫描一致）。
- 盒内末行：基线 y=2233.3，19.5pt Noto Sans CJK SC，x=1013，`る。VOL.5で実際の投稿の講評という約束を果たす。`（courier_disclosure 末行）。
- **本人 PIL 真墨实测**（`cards/p7-langue.png`，1950×2700，与 SVG 1:1；日志 `p7-measure.log`）：
  奶油底边渲染在 PNG y=2257（SVG 盒底 2258.0）；盒内 x 范围末行真墨至 y=2234（基线下仅 ~0.7px，行 2225–2234 有墨，2235–2269 全页该 x 范围零墨）；
  奶油净边距 **23px**；SVG 全页扫描确认基线 (2233.4, 2310) 内无任何文本；深绿带起于 y≈2270。
- creambox：该盒 naive clearance **+24.7**，inside-only 末基线 2233.3（+24.7），desc-clear +18.8，无 BELOW-WINDOW 行。
- **裁定：不溢出，干净。**与 fr-de 复校员的跨版目测（ja 版 inside-only +24.7）数值一致，但本结论由本人独立测量建立，非采信。
  网页版 P7 目视（`png/web7.png`）同样干净。裁切图 `png/p7-courier.png` 可见末行下有完整奶油边距。

## 身份核对（三件 SHA，复核前后一致）

| 件 | 大小 | SHA-256 | 任务书 |
|---|---|---|---|
| 印 PDF `La-Lucerna-VOL4-fr-ja.pdf` | 30,566,551 B | `b137834de17569ccac619569df1569544a823e868986565852a718315f331b8f` | 一致 |
| 网 PDF `La-Lucerna-VOL4-fr-ja-web.pdf` | 2,310,518 B | `42907782ecdbee6b667bd5bcfe46c7c9e8b5928d23c8895e3fb8313e174c886d` | 一致 |
| text.md `2026-w47-fr-ja.text.md` | 47,551 B（1,087 行） | `1b111aad84bbf1c1101131b13ce85745793b24f59ff88086151c744afed98e60` | 一致 |

core-fr 对照（复核前后各测一次，未变）：
印 `La-Lucerna-VOL4.pdf` `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7`；
网 `La-Lucerna-VOL4-web.pdf` `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823`；
text `2026-w47-fr-zh-cn.text.md` `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e`。

## 1. freeze 首检 8/8

`tools/freeze.py diff --core-svg core-fr/svg --edition-svg 2026-w47-fr-ja/svg`（rc=0，8 页全比对）：
p1 +23/-23，p2 +35/-33，p3 +31/-32，p4 +40/-38，p5 +37/-34，p6 +27/-28，p7 +34/-34，p8 +120/-122。
`--strict-cjk` rc=1 属预期：ja 是读者语（非目标语），核心本身已含 CJK（每页 194–1,220 字符）——strict 门只适用 zh-cn/zh-tw/ja **目标**。
新增 CJK 已逐个分类（见 cjk_classify 门）：净增 2,332 字符（按页多重集差）；新增串中 CJK 毛数 3,445（431 个不同字符），
**未入账 0**——全部对应日语讲解层（expl.py E 值）：平假名 730、片假名 686、汉字 1,298、U+3000 结构空格 289、CJK 标点 105、全角 337。
疑似简体中文残留逐字核对：`来` 4（未来形/来週）、`会` 1（委員会）、`去` 8（過去分詞/過去形）、`由` 1（自由作文）——全部为标准日语用法，**零中文残留**；
国/学等同形字未见误报。日志 `freeze-diff.log` / `freeze-diff.json`（含 `--strict-cjk` 版与非 strict 版）。

## 2. 门禁汇总：15/15 PASS（`gates-proof1.json`，脚本 `proof_gates.py`）

| 门 | 结果 |
|---|---|
| run（builder `ja/build-run1.log` 读检） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150，A2 53 / B1 75 / B2 22，by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42}；注：日志中 `P7 DORE NOSPACE: y0= 1016` 一行系已知良性行（dore caption 事后插入），与 fr-de 复校同口径过滤 |
| occlusion（`tools/occlusion_audit.py`） | PASS：0 flags，selftest OK（`occlusion-proof1.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-proof1.json`） |
| p8_compare（vs core P8 SVG） | PASS：CLEAN，keydiff [150]（writing key only）（`p8compare-proof1.json`） |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免（核心 `stem_e1` 前缀 `Traduisez: `） |
| text_layer | PASS：印/网 pdftotext 逐字节一致（102,274 B）；web 2,310,518 B < 7MB；print 30,566,551 B（`print-proof1.txt` / `web-proof1.txt`） |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 键仅 Q150 不同，核心 150 键 / 抽取 150 键 |
| mcq（`check_mcq.py`） | PASS：bodies 45，rendered lines 1454，DEFECTS: 0，UNLOCATED: 0（`mcq-proof1.log`） |
| widths | PASS：31 单行串全部在预算内；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测） | PASS：FR title ends 1236.9，band_r1 starts 1380.0（gap 143.1），FR sub ends 837.2，band_r2 starts 1430.1 |
| cjk_classify（新增门，见 §1） | PASS：3,445 字符 / 431 不同字，全部入账，未入账 0 |

## 3. 确定性（沙盒副本重建，替代 gates 第 7 门）

版目录完整拷贝至本目录 `rebuild/ed/`（副本已删），删 svg 后重跑 `run.py`（rc=0，TOTAL 150，类型分布与 builder 一致），
8 个 SVG sha256 与在版文件**逐字节一致 8/8**，且与 builder `freeze_direct` 哈希逐一相同：
`8bf58ae5 / db490888 / 83ad866a / 8252ca19 / cae84c75 / 7fdd8932 / 7a37897c / 66b5fa78`（日志 `rebuild-run.log`）。

## 4. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，日志 `creambox-proof1.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一节标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；
  inside-only 清除全部为正，P1 +48.0 / P2 +47.7 / P3 +47.7 / P4 +47.7 / P5 +47.7 / P6 +48.5 / P7-TOOLBOX 最小 +24.7、desc-clear +18.8）。
- 双语小标题越奶油盒右缘：8 页目视 + widths 门 + occlusion 0 flags，未见标题字形被裁、墨叠他元素或可见边框；无回归。
- P7 读者园地盒见上节独立实测裁定：干净。

## 5. 150 题逐题手验（三源交叉 + 全文通读）

- 三源交叉（日志 `keycheck3b.log`）：text.md 答案区解析 150/150 无缺失；**text.md 答案 == P8 抽取键 150/150**；
  核心键 vs 本版键仅 Q150 不同（`开放题` → `自由作文`，写作题 ja 化，预期内）。
- text.md 全文通读 1,087 行：逐题核对题干与答案的事实一致性（含 Q64 `Les Braves` = Lukas Dhont，Q19–21、Q44–48、Q62–72、Q79–96、Q97–108、Q109–149 全部与正文事实相符）；
  Q135/Q138 为松散翻译（键为本期既有法语句），与核心键完全相同，非本版新问题；零中文残留（见 §1）；U+2019=0、U+00B7=0。
- Q148 见 R1（只记录）。

## 6. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png` + 缩览 `png/v1.png`–`v8.png`）：除 D1–D3 外零问题；
  P1 band 无重叠（裁切 `png/p1-band.png`）；各页无溢出/遮挡/截断；P7 读者园地盒干净（见上）。
- 网页 PDF 抽查（`png/web1.png`、`png/web7.png`，100 dpi）：与印刷版布局、图片一致；D1 在网页版同样可见。
- 核心英文 "next Sunday" 为冻结核心（core re-proof #3 (a) 认证），不是缺陷——本版未见该类问题。

## 修复指引（给协调员）

1. 缩短三串（expl.py）：g1 gloss 末段、bridge_comp4、bridge_chart，各减 1–2 字使「。」回到末行行尾；
   或在流式换行中加入禁则处理（工具级修，一劳永逸——核心亦有同类一处）。
2. 修后重跑全套门禁（`proof_gates.py` 同口径）+ P1/P4/P6 重验 + freeze 8/8 重核。
3. R1（Q148）与 R2（D5）不阻塞本版：R1 走核心轨道，R2 为全周级待定项。
