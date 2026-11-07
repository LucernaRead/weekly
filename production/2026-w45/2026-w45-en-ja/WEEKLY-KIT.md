# The Lucerna · 英语周报 VOL.2 × 日本語版 — WEEKLY KIT

English core week of **Monday November 2 to Sunday November 8, 2026**
(issue dated Monday, November 2, 2026; slug week 2026-w45).
Fan-out of `files/weekly-report-w45-en-core/` (VOL.2, masthead
The Lucerna): English body frozen, explanation layer fully Japanese.
**Builder state: builder-complete. NOT finalized — independent
proofread still required before any shipping claim.**

## 1. 交付物

`files/weekly-report-w45-en-ja/`：

- `svg/` — 8 pages of SVG sources (p1-front … p8-exercices)
- `cards/` — 8 full-page PNGs, 1950×2700
- `The-Lucerna-VOL2-JA.pdf` — merged 8-page PDF, **31,114,365 bytes**,
  sha256 `943448ee5aff62bb8250546164afe0e606b1a2b92675fdc3e7f1cade55a99cac`
- `The-Lucerna-VOL2-JA-web.pdf` — compressed PDF, **3,943,144 bytes**,
  sha256 `995de98a686023da7dcbb1e5704e5f2ae8c3dd461522f84a7850e0c63bae5478`
  (page JPEGs q85 at 1400 px wide)
- 本文件 + `ABSTRACT.txt`（日语单行、无 ASCII 双引号）

构建树在 `hidden_files/weekly-report-w45-en-ja-build/`：
`transform.py`（唯一事实源：从核心重拷 + 值映射 + 行级编辑 + 断言）、
`run.py`（单进程 driver）、`render.py`（卡片 + 双 PDF）、
`check-cjk.py`（未映射 CJK 常量审计）、`rowcheck.py`、
`rightedge.py`（ADVANCE 法右缘扫描）、`scan_linestart.py`、
`gloss_count.py`、`chartcheck.py`（P6 图表标签覆盖），以及每轮
sha256 基线与门禁输出（`baseline-*.sha256`、`occlusion-*.json`、
`diff-*.json`、`build-*.log`）。

## 2. 规格

- 8 版，1950×2700，四栏，暖象牙底、深橄榄点缀，哥特体刊头
  The Lucerna（英语冠词，核心冻结）。
- 难度坡度与核心一致：P1 A2 · P2 A2 · P3 A2→B1 · P4 B1 · P5 B1 ·
  P6 B2 · P7 精讲（A2/B1/B2 三级专栏 + 本周金句）· P8 综合评估 +
  写作范文 + 全部答案。
- 图片载荷与核心逐页全等（P1/P2/P3/P4/P6 各 1 张，P5/P7/P8 无图；
  5 张图皆 Wikimedia Commons 公版/CC0，署名随核心冻结）。

## 3. 家具登记（与已上架 W43 EN×JA 逐字一致，除注明的核心差异外）

| 部位 | 本版实例 |
|---|---|
| P1 徽章（372 tagline 槽，19.5pt 粗体 BRICK，居中，替换核心英文 strapline——W43 同配对先例） | 英語テキスト · 日本語の解説 — 日本語読者のための版 |
| P1 masthead 衬线行 | 英 語 週 刊 · VOL.2 · 選 票 · フットボール · 映 画 |
| P1 顶带中段 | WEEKLY IN ENGLISH · 毎週一号 · アメリカ人が読んでいる英語を読む |
| 页脚左（每页） | The Lucerna · 英語週刊 VOL.2 · 本文は英語 · 解説は日本語 |
| 页码行（每页右） | N ページ（全 8 ページ） |
| gloss 前缀（bslib4 gloss() 常量；gloss() 调用串值去前缀，单前缀） | 解説 — |
| 语法点前缀 | 文法ポイント — |
| P8 页首 | ANSWERS · 全解答と解説（1–8ページ） |
| P8 分隔行 | — N ページ — |
| P8 答案注包裹（EN 家族式样，半角括号 + 注前空格） | `N. key (note)` |
| 双语章节头 | 英语原题 · 日语短题（如 A · CLOZE · 空所補充 / THE ERROR CLINIC · 誤りクリニック / LEVEL A2 · 基礎 · B1 · 中級 · B2 · 上級） |
| 练习类型（中→日） | 完成句子→文の完成 / 句型转换→文型変換 / 单选→選択 / 图表读数→グラフ読み取り / 改错→誤り直し / 跟练→音読ドリル / 完形填空→穴埋め / 阅读理解→読解 / 翻译→翻訳 / 词汇配对→語彙マッチング / 对话补全→会話補完 / 写作→作文 |
| 练习指令（中→日） | 填空→空所補充 / 改写→書きかえ / 改错→誤り直し / 把词和释义配对→語と意味を結ぶ / 配对→組み合わせ / 选项→選択肢 |

字体与折行：svglib 整体采用日语核心 build 的规范 JA 版，md5
`d73e23b365676c3618d7e060b835eb4d`（transform.py 每次运行前验 md5，
规范文件本身绝未编辑）。拉丁度量各 CJK 面一致，冻结正文版式不受影响。

## 4. 八版内容（与核心同题，讲解层日语化）

| 版 | 内容 |
|---|---|
| P1 头版 | 头条 « America Votes : Election Day Comes on Tuesday, November 3 »；热搜榜；目录；本周词 midterm；投票亭照片；快讯；闪电问答 4 题。10 题 |
| P2 生活 | 11 月 1 日周日拨回时钟（25 小时之夜；亚利桑那与夏威夷不拨钟）；10 月 31 日周六万圣节（已过去事件）；11 月 6 日电影预告；报时专栏（3 个自绘时钟）；1912 万圣节明信片图。17 题 |
| P3 文化 | 11 月 6 日周五上映 « The Cat in the Hat » 与 « Godzilla Minus Zero »；居家一周 Netflix 档期；五句影评法；Manet 猫插画图（图注说明不是电影剧照）。18 题 |
| P4 体育 | 11 月 8 日周日 NFL 第 9 周马德里赛 + 海豚–雄狮；F1 圣保罗大奖赛；NASCAR；WTA 印第安维尔斯；拳击阿灵顿；11 月 7 日周六 MLS；1910 年橄榄球照片。18 题 |
| P5 青年 | 选举之夜在家（地图、手机第二屏、披萨）；« Too close to call » 教学；11 月 7 日 MLS 预热。18 题 |
| P6 深读 | 美国投票制度；模拟选票（候选人仅代号）；教学图表 « WHY DO VOTERS VOTE EARLY ? »（38/29/21/12，合计 100，版面明确标注为教学数据、非真实民调）；国会大厦图。18 题 |
| P7 精讲 | A2 拨回时钟 + going to / B1 比较级 + 一般过去时 / B2 标题现在时 + whether；本周金句 8 句；易错诊所 4 题；读者园地；VOL.3 预告。12 题 |
| P8 评估 | 完形 8 + 单选 9 + 阅读 4 + 完成句子 4 + 翻译 4（英↔日双向，见 §7）+ 词汇配对 4 + 对话补全 5 + 写作 1（« My Tuesday, November 3 »，范文 85 词）。39 题 + 全部 150 题答案与简析 |

## 5. 实测量化

- **练习总量：150 题**（统一编号 1–150，单进程注册表实测，连续无缺重）。
  - 按难度：**A2 60 · B1 69 · B2 21**（与核心全等）
  - 按版：P1 10 · P2 17 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 39（与核心全等；注意 P2 17、P8 39）
  - 按题型（日语标签）：文の完成 33 · 選択 41 · 文型変換 16 · 語彙マッチング 20（5 组）· グラフ読み取り 6 · 音読ドリル 8 · 誤り直し 4 · 穴埋め 8 · 読解 4 · 翻訳 4 · 会話補完 5 · 作文 1
- gloss：渲染后 gloss() 串按 `·` 拆分逐项计数，**核心 18 = 本版 18**（P2 3 / P3 4 / P4 4 / P5 3 / P6 4，逐串 1:1）。
- P7 金句：8 句原文逐字保留，(page N) 标签与核心全等（page 1/2/3/4/5/6/2/4）；全文归一化计数 8 句裸句核心 = 本版（3/2/2/2/2/4/3/2，含文章/P8 复现）。
- 范文：« My Tuesday, November 3 » 模型文空白分词 **85 词**，与核心一致。
- 构建日志：零 FLOW OVERFLOW、零 HEAD TOO WIDE（两轮皆然）。
- 8 张卡片全部逐页目视（P1–P8 无遗漏）：无溢出、无重叠、无压页脚、无图片与出处问题；P6 图表标签覆盖 0.0%（门限 <30%）。

## 6. 机械门结果（全部用 tools/ canonical 工具 + 本版补充脚本，终轮实测）

- **核心基线**：开工/修复/收尾三度核对核心 8 SVG sha256，**核心 8/8 未动**。
- **冻结差分**（`freeze.py diff`，终轮）：新增 CJK 2,282 字全为日语讲解层；
  字符多重集核对后，英语残差全部归因闭合：页脚/页码家具替换、P1 徽章
  替换（W43 同配对先例）、日语串内 ASCII 数字与分隔符（2本、50の州、
  文法ポイント — 的 — 等）、答案区换行重排、P8 半角括号式；移除侧
  非讲解项 = 0。英语正文冻结成立。
- **中介术语**：全文扫描，交付物中该词 **0**；讲解层全部日语。
- **P8**（`p8.py compare`，显式双路径形式）：**CLEAN 78=78**，
  missing=[]、extra=0、keydiff=[137, 138, 139, 140, 150]（见 §7 逐项裁定）；
  P8 注释纯日语（共享词裁定见 §8）；印刷笔记集合相等，无 EXTRA_ONLY。
- **几何**（`occlusion_audit.py`，自检先行通过）：**本版 0 / 核心 0 /
  NEW 0**。同行墨迹扫描（P1 顶带重点）**0 碰撞**（核心对照亦 0）；
  同基线碰撞用解码后测量；全 8 页框线压框 + 右缘扫描（ADVANCE 法）：
  右缘仅剩 2 处，皆为核心同坐标同串的 P8 配对右栏选项（advance 1899.4/
  1903.8，页内 1950 以内，墨迹审计 0 旗）——核心继承，非本版缺陷。
- **行首禁则**：日语行 **0**；另有 6 处英语冻结换行行首（`: `×3、
  `? `×1、`, `×1、半角 `)` ×1），皆为核心同坐标继承（核心同口径 12 处；
  其中 P8 半角括号处对应核心的全角括号同位置换行）——冻结英文换行，
  非日语禁则缺陷，不可通过改动冻结正文消除。
- **中文残留（词级复查）**：简体专属字与真中文专属词 **0**；共享汉字
  词逐词裁定为正明日语：生活/文化/体育/青年（栏目标题）、怪物
  （monster=怪物）、原文、原形、投票率、地圖（地図）、得点；简体字
  扫描命中仅上述正明日语词。

## 7. 键差异登记表（注册表与 p8.py 一致，全部为英↔日方向重定向）

| # | 核心键 | 本版键 | 类别 |
|---|---|---|---|
| 137 | 耐心是制度的一部分，而不是制度的失败。 | 忍耐は制度の一部であり、制度の失敗ではない。 | 翻译题：EN→JA（题面 Translate: 英文原句冻结） |
| 138 | 11 月 3 日周二是美国的选举日。 | 11月3日火曜日はアメリカの選挙日です。 | 翻译题：JA 呈现（题面改向为「翻訳：Tuesday, November 3, is Election Day in the United States.」；英语键不在此题） |
| 139 | 这周日，NFL 在马德里比赛。 | 今週の日曜日、NFLはマドリードで試合をします。 | 翻译题：JA 呈现（题面改向为「翻訳：On Sunday, the NFL plays in Madrid.」） |
| 140 | 并非每处都拨回时钟。 | すべての場所が時計を戻すわけではない。 | 翻译题：EN→JA（题面 Translate: 英文原句冻结） |
| 150 | 开放题 — 要点见写作框，范文在第 8 版写作框内 | 自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中 | 写作装置项（注：要点ごとに採点） |

其余 145 键与核心逐字节全等。P8 印刷集 78 项由 `p8.py extract` 对
核心实测后以 PRINT_NOTES 显式固化（日语注较长，核心 len≤10 阈值规则
不再适用），半角括号式。

## 8. P7 结构实测（从核心实测，语言归属逐项登记）

- 三级专栏（A2/B1/B2）：英语定义句与例句逐字冻结；栏目标题日语化
  （基礎/中級/上級）；B2 例句框内 gloss 片段本地化（part of = 一部），
  英语原句不动。定义句本地化 = 0 处。
- 本周金句区：8 句英语原文 + (page N) 标签逐字冻结；语法点行日语化
  （文法ポイント —）；跟练题型日语化（音読ドリル），键与注除 §7 外
  与核心一致。
- 易错诊所：英语错句与正句冻结；指令与注日语化（誤り直し）。
- 读者园地：英语信件、标注、预告承诺逐字不动（见 §9）；披露句本身
  日语（见 §9）；未为核心没有的英语披露句子新写英语披露句。
- VOL.3 预告：英语预告句冻结；日语预告行本地化（退役軍人の日、
  NFLミュンヘン戦、中間選挙の結果報道）。

## 9. 读者园地（协调员裁定执行实录）

- 保留核心已有的英语元素逐字不动：信件 « On Sunday, I slept one hour
  more — and I still woke up late ! » — M. L., a reader in Chicago
  (editor's example : no real reader letters had arrived when this issue
  went to press, so the example stays, honestly labeled)；无任何编造的
  读者/来信/姓名/引言。
- 披露句（日语，园地框内 4 行，框底界内；末行基线 2160，墨迹底 2162.3 < 框底 2178）：「編集部より｜VOL.1では
  VOL.2に本物の読者の手紙を載せると約束しましたが、締め切りまでに
  本物の手紙も、VOL.1の作文投稿の最優秀作も届きませんでした。そこで
  本号は見本を見本と明示して載せ、約束はVOL.3へ先送りします。あなたの
  手紙と作文を送ってください。VOL.3に届いた本物の手紙を載せます。」
  3 事实：无真实来信、无最佳 P8 作文（VOL.1 作文投稿最優秀作）、
  示例 + 承诺顺延至 VOL.3；显性日语公开征集邀请：祈使句（送ってください）
  + VOL.3 刊登承诺（内容预告行不算邀请，邀请句独立在披露句内）。

## 10. W43 同配对偏差清单（偏离皆有原因，非家具登记漂移）

1. 印刷笔记集 **78**（W43 为 62）：W45 核心实测值，非照搬；W45 核心
   P8 正式评估 39 题 + P1–P7 短注规则所致。
2. keydiff **5 项**（W43 为 3 项）：W45 翻译题 4 项（137–140，含 2 项
   JA 呈现改向）+ 写作装置项 150；W43 仅 2 项翻译 + 1 项写作。
3. 园地披露句文案不同：W45 核心情境为 VOL.1 承诺落空（无来信 + 无
   最佳作文，顺延 VOL.3），W43 为 VOL.2 承诺，两期事实不同。
4. 四处日语标题因几何门缩短（W43 同类缩短先例）：P1 热搜副题
   （今週の急上昇 · Google Trends）、P1 相对热度注（人気の目安で、
   正確な検索数ではありません。）、P3 在家框题（AT HOME THIS WEEK ·
   おうち時間）、P4 周日赛程框题（SUNDAY, NOVEMBER 8 · 日曜の試合）。
5. 行首扫描：本版英语冻结换行继承 6 处（核心 12 处）；W43 版为 0 处——
   两期核心英文换行位置不同所致，日语行两版皆 0。
6. 其余家具（徽章、页脚、页码行、gloss/语法前缀、P8 分隔行与括号式、
   题型/指令映射、svglib 规范版）与 W43 EN×JA 逐字一致，无漂移。

## 11. 修复轮记录

- **首轮**：构建 0 警告，150 题分布全等；门禁查出遮挡 NEW 5 旗
  （P1 热搜副题出页 + 压框、P3 在家框题出框 + 连带 TEXTX、P4 周日
  框题出框）与右缘 1 处新增（P1 相对热度注 1946.7）。修复前已记录
  首轮 SVG/card/PDF 全部 sha256 基线（`baseline-round1-*.sha256`）。
- **第二轮**：4 处缩短全部写入 `transform.py` 值映射（非仅改 content
  文件），重跑变换 → 单进程重渲染 → 终轮门禁：遮挡 0/0/0、同行 0、
  右缘仅剩 2 处核心继承、图表 0.0%、P8 CLEAN、行首日语 0。
  变化的 SVG 仅 p1/p3/p4，卡片与 PDF 同步仅此三页变化；其余五页
  卡片 sha256 与首轮全等。
- 未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、
  未改核心与 W43 目录（核心/W43 仅只读对照）。

## 12. 复现构建

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-en-ja-build
PY=~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python
$PY transform.py   # 从核心重拷 + 值映射 + 行级编辑 + 断言（含 svglib md5 门）
$PY run.py         # 单进程：content12 -> 34 -> 56 -> 7 -> 8（注册表累积）
$PY render.py      # svg -> cards PNG -> 印刷 PDF -> 网页 PDF
```

- run.py 解释器：`tools/venv/bin/python`，Python 3.12.3，PIL 13.0.0
- render.py 解释器：`tools/venv/bin/python`，Python 3.12.3，PIL 13.0.0，
  cairosvg 2.9.1，pypdf 6.21.2（系统 python3 无 cairosvg，不可用）
- run.py 解释器/PIL 选择自由，但须字节复现同族基线 SVG（除有意改动外）；
  本版 SVG 由上述 venv 产出。
