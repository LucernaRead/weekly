# 独立校对报告 — Lucerna Weekly W45 KO×EN（韩语目标 × 英语读者）

**结论：ZERO PROBLEMS**

校对员：独立校对（只校对，不改源码，不宣布上架，未派生下级代理）。
校对对象：`files/weekly-report-w45-ko-en/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt），
对照：`files/weekly-report-w45-ko-core/`（W45 KO 核心）与 W43 同配对版 `files/weekly-report-ko-en/`。
校对时间：2026-10-27（EDT）/ 2026-10-28（UTC）。本报告不宣布上架；是否上架由主线裁定。

## 开工与非目标保证

- 开工前查重：`ps` 无在途进程；交付物最新 mtime（KIT 03:15 UTC）后静默 >120 秒（复查时 176 秒）才开工；
  无属于 ko-en 树的在途写盘，无关分版进程不构成 stand down，故未 stand down。
- 未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 `weekly-git`、未改核心/W43 目录（只读对照）、
  未清理共享 scratch 目录。
- 构建树只拷到本科对 scratch（`hidden_files/w45/ko-en-proof/scratch/build-copy/`）后运行，
  其中 5 个 content 文件的 OUT 已重定向到本科对 scratch 的 `rerun-svg/`，并 grep 确认交付路径残留 0 处；
  原构建树、交付目录、核心目录全程只读。
- 校对前后交付物哈希 diff 为空、核心哈希 diff 为空（`hashes-before.txt` = `hashes-final.txt`；
  `core-hashes-before.txt` = `core-hashes-final.txt`）。

## 逐项门禁（全部独立重测，构建员声称值一律未采信）

### 1. 交付物与 PDF

- 印刷 PDF `Lucerna-VOL2-EN.pdf`：32,378,317 B，sha256
  `d169aff6b8740f66c4aad18c8cdb919df3d922eeae8fe5347c0f71d6f8800254`，8 页，1462.5×2025 pts。
- 网页 PDF `Lucerna-VOL2-EN-web.pdf`：3,502,762 B，sha256
  `20d9d1d5909cb88a331dfd829c6556170346e5194a5c1e532fb2aa5ca3c99e1c`，8 页，1400×1938 pts。
- 与构建员声称值逐字节一致。P1 印刷 PDF 文本抽查含刊头、副标题、徽章原文。

### 2. 冻结

- 核心基线：`core-baseline-sha256.txt` 核对 10/10 OK（8 SVG + 2 PDF；核心 PDF 尺寸
  印刷 33,125,291 B、网页 3,366,637 B，与 KIT §2 一致）。
- 韩语正文零删失：`freeze.py diff` 逐页 added CJK = 0（p1 +20/−19、p2 +39/−36、p3 +30/−28、
  p4 +23/−21、p5 +32/−31、p6 +17/−15、p7 +41/−39、p8 +174/−167；CJK 总量下降只因中文讲解层撤出）。
  韩语音节字符多重集逐页核对：P1–P6、P8 唯一减少的是家具 `제 N 면 / 총 8 면` → `Page N of 8`
 （每页 제×1、면×2、총×1，属分版本地化家具，非正文删失）；P7 的减少来自中文讲解与韩语披露被英语披露
  替代（例信本身逐字冻结，见 §7），无韩语正文丢失；新增韩语音节 0。
- P7 词框目标语定义句逐字冻结：A2/B1/B2 三栏韩语定义散文（核心行 4–11 / 30–36 / 55–61
  对分版行 4–11 / 31–37 / 56–62）去空白后逐字相等；三栏标题韩语部分相等；词框 gloss 全部本地化为英语
  （见 §5）；误诊室韩语源句逐行相等。
- 桥接词：SVG 全文 + 构建代码（含 transform.py）+ KIT + ABSTRACT 中 `桥接`/`bridge` 出现 0 次。
- 刊头：`Lucerna` 无冠词（韩语无冠词，与核心、W43 一致）。

### 3. P8 比较（双版本显式双路径，--total 150）

- 旧版 `tools/p8.py`（sha `67df05f1…`，已恢复的验证版）：**CLEAN**，core 150 = edition 150，
  missing=[]、extra=0、uncertain=[]、**keydiff=[109, 137, 138]**。
- 新版 `hidden_files/w45/p8-dash-fix-verify/p8.py.new`（sha `96fc2cfe…`，未验证版）：
  **CLEAN**，core 150 = edition 150，missing=[]、extra=0、uncertain=[]、**keydiff=[137, 138]**。
- 两版结果不一致处仅 109 项，逐项裁定如下（以印刷行实测为准）：
  - 核心印刷行：`109. 기준 — 日期不同因标准不同（3版）`；分版印刷行：
    `109. 기준 — The dates differ because the criteria differ (page 3)`。
    两行均为破折号式结构，键同为 `기준`，注释一为中文、一为英语，键无差异。
  - 旧版工具因段内同时含破折号与括号组而误入 paren 分支，把注释吞入键（核心键误作
    `기준 — 日期不同因标准不同`，分版键误作 `기준 — The dates differ because the criteria differ`），
    注释语言不同遂误报 keydiff。新版工具（破折号在括号组之前则判 dash 式）对两行均正确析出键 `기준`。
  - **裁定：新版正确，109 不是真实 keydiff；两版 CLEAN 结论在印刷行层面均成立。**
  - 137/138 为真实合法 keydiff（E 区重定向）：核心键为中文句 `11月7日是立冬。` / `离高考还剩 12 天。`，
    分版键为英语句 `Nov 7 is Ipdong.` / `There are 12 days left until the CSAT.`；
    139/140 键两版均为韩语（`특별 조치는 11월 19일에만 적용돼요.` /
    `저는 토요일에 내장산에 단풍을 보러 가요.`）；注释 `From page 1 / 5 / 6 / 3`（137/138/139/140）与印刷行一致。
- P8 全段逐字节相同行：0 条（全部注释均已本地化，无可疑未译行）。
- P8 注释语言纯度：分版 150 条注释中汉字（U+4E00–U+9FFF）0 个；全版 SVG 文本节点汉字 0 个
  （核心为 2136 个，中文讲解层已完全撤出）；ASCII 双引号 0 个。
- 25 条韩语引用注释复核（见非阻塞观察 2）：实际为 **23 条**（25–28、34、43–46、57–64、135–136、141–144），
  逐条核对印刷行：键全部冻结相等，韩语 headword 冻结，环绕全部为英语（例如 34
  `The most beautiful autumn leaves are called 절정`、57 `Past form of 이기다: 이겼어요`、
  135 `보러 가요 = to go to see`、136 `Use 「에서」 for the place of an action`，其中 「」 为引用的韩语助词，
  非中文残留）。无未译中文注释。阻塞项：无。

### 4. 计数 / 登记展开（scratch 重跑，OUT 已重定向）

- 登记展开一进程重跑：TOTAL **150**，连续 1–150；级别 A2 51 / B1 72 / B2 27；
  页分布 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38；类型 fill-in 48、multiple choice 52、matching 16、
  transformation 4、sentence building 8、true/false 4、cloze 13、translation 4、writing 1；与核心声称值一致。
- 重跑 8 张 SVG 与交付 SVG 逐字节相同（8/8），证明分版构建确定性。
- 范文：H 区范文逐字 = 核心；MODELO 原文去空格 **157 字**（`예: ` 标签不计，见非阻塞观察 4）；
  印刷指令 `150–200자`、P8 注 `157자의 예` / `(157 characters)` 一致。

### 5. gloss（渲染 · 切分逐项计数）

- 渲染 gloss 词条（Note—/译注｜块按 `·` 切分 + P7 词框行）：核心 = 分版 = **67 项**，
  headword 逐项对应（多词 headword `겹쳐 입다`、`하나가 되다`、`겁이 나다` 各计 1 项，两版一致），0 缺失。
- 冻结韩语 glossline 指令 17 条（content12 3 条、content34 6 条、content56 8 条，如
  `2면의 글을 읽고 맞는 답을 고르세요.`、`빈칸에 알맞은 말을 넣으세요.`）在分版与核心渲染文本中均逐字存在。
- 67 + 17 = **84**，与构建员声称值一致（其 84 = gloss 对 67 + 指令行 17，非 84 条 gloss 对）。

### 6. 金句

- 8 句全版计数（去空白）：核心 = 分版 = **5 / 2 / 4 / 2 / 2 / 2 / 2 / 2**，
  每句至少出现 2 次（正文 + P7 引用）；P7 引用韩语原文逐字 = 核心，英语译文下页签
  (1면)×3、(2면)、(3면)、(4면)、(5면)、(6면) 齐全。

### 7. 读者来信角（P7）

- 韩语例信逐字冻结（分版行 104–108 = 核心行 102–106）：
  「안녕하세요. 저는 대학생이에요. 토요일에는 내장산에 단풍을 보러 가요. 일요일에는 집에서 김장을 도와요.
  겨울이 와도 따뜻하게 지내고 싶어요.」— 독자 편지의 예。零编造（无新增人名、来信、引言）。
- 英语披露（分版行 109–116，8 行，y=1528.61–1727.41）逐字摘录：
  “Editor's note: this is an example letter from the editors, not a real reader's letter.
  No real reader letters or best page 8 writing had arrived by press time, so the example stands
  and last issue's promise carries to VOL.3. Send us your letter and your page 8 writing —
  write two sentences in Korean and send them in!”
  - 3 事实齐全：(1) 例信非真实来信；(2) 截稿时未收到真实读者来信；(3) 未收到最佳 P8 写作，
    例信保留、上期承诺顺延至 VOL.3。
  - 明确祈使征集：`Send us your letter and your page 8 writing — write two sentences in Korean and send them in!`
    **同时覆盖来信与 P8 写作**；VOL.3 承诺明确。
  - 范围裁定：teaser 行（`다음 주에는 김장이 한창이에요… 여러분의 편지와 8면 쓰기 우수작도 실어요。`）
    不计作征集——征集本身已在披露内满足，无需 teaser 补足（KIT §6 曾讨论的 pt 族范围裁定在本版不适用）。

### 8. 几何（门禁输出未截断，全量见证据文件）

- Canonical `tools/occlusion_audit.py`：自检 OK（6 类各触发 1 次，干净对照静默）；
  分版 **0 flags**、核心 **0 flags**、NEW vs 核心 **0**。
- 构建员 `audit.py` 独立重跑（scratch 副本）：分版与核心 8 页全部
  line-start=0、splits≥3=0、row-overlap=0、right-edge=0（与 round2-audit.txt 逐行一致）。
- 本科对独立扫描（`scratch/myscans.py`，PIL advance/getmetrics，锚点感知）：
  - ADVANCE 全页右缘扫描（阈值 1885）：分版 8 页 0、核心 8 页 0。
  - 全页框线扫描（外框 28/1922/2672、内框 40/1910/2660，半线宽展开）：分版 8 页 0、核心 8 页 0。
  - 同基线墨迹间距扫描（同基线 ±2px，间隙 <4px 即报）：分版 8 页 0、核心 8 页 0。
  - 行首扫描（NO_START 集合）：分版 8 页 0、核心 8 页 0。
- P6 图表标签（getmetrics 基线锚定法，非 getbbox 法）：分版 169 个文本节点、
  核心 167 个，后绘矩形覆盖率最大值均为 **0.0%**（<30% 门禁）；P6 对比表卡面目视标签全部在格内、无截断。
- P7 预告末端：分版末基线 2481.46，字形底 2487.71，流程末端 **2515.46 < 2540**（与构建员声称值一致）；
  预告单行 advance 终点 1817.1 < 1885，无溢出。
- P8 答案流末端：分版末基线 **2530.35**（113 题，第 2 列），字形底 **2534.35 < 2540**
  （与构建员声称的 ≈2534 一致）；页脚规则线 y=2580，页脚基线 2624 豁免在外。
- Round-1 → Round-2 核实：Round-1 运行日志确有 `!! FLOW OVERFLOW [P1-headline] col 2 y=1743 need 99
  bottom 1828`，Round-1 P8 末基线曾达 2624.0、P7 预告标题首行 2539.5；
  Round-2 运行日志 0 条 FLOW OVERFLOW / HEAD TOO WIDE 警告，P1-headline 止于 col 2 y=1413（= 核心值），
  终版上述三项全部清零（见非阻塞观察 3 关于 Round-1 canonical 10 旗清单的存档说明）。

### 9. 家具三方对照（W45 核心 / W43 同配对 / 本版；W43 优先于 README #20）

实测（P1，逐项）：

| 元素 | W45 核心 | W43 KO×EN | 本版 | 裁定 |
|---|---|---|---|---|
| 刊头冠词 | 无 | 无 | 无 | 一致 |
| 副标题 y | 372 | 366 | 366 | 本版 = W43 |
| 徽章 | 无（中文条） | 17pt bold olive #3e4c2a, y=394, 全文 `TEXT IN KOREAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS` | 与 W43 逐字、字号、字重、颜色、y 全部相同 | 本版 = W43，非 #20 的 20pt BRICK |
| 规则线 | 392 / 401 | 412 / 421 | 412 / 421 | 本版 = W43 |
| 暗带 | y=424 | y=433 | y=433 | 本版 = W43 |
| 带内行 | 478 / 531 | 487 / 531 | 487 / 531 | 本版 = W43（首行 487，第二行 531） |
| 顶栏 | VOL 徽记 y=92、中央标语 y=92、右日期 y=92（1885 端锚） | 同左（VOL.1、10 月日期） | 同左（VOL.2、11 月 2–8 日） | 仅期号/日期/主题词合理变化 |
| 刊名/主题行 | Lucerna 168pt y=262；主题行 40pt bold y=330 | 同 | 同 | 一致 |
| 页脚 | 中文讲解 | `KOREAN WEEKLY VOL.1 · Korean text · English explanations` / `Page N of 8` | VOL.2 形式 / `Page N of 8` | 一致 |
| P8 分隔符 | `— 제N면 —` | `— 제N면 —` | `— 제N면 —` | 一致 |
| gloss 前缀 | `译注｜` | `Note — ` | `Note — ` | 一致 |

核心与分版在副标题/规则线/暗带/带内行的数值差（372→366 等）为徽章插入后的整体移位，
与 W43 同配对版完全一致，属既定范式，非缺陷。

### 10. 图片 / 摘要 / 主题

- 图片 payload（解码后 sha256）：P1 1、P2 1、P3 2、P4 1、P5 1、P6 0、P7 0、P8 0，
  逐页与核心完全相同；credit 均在页、逐字 = 核心：
  P1 秋景 lumoplank CC0、P2 ssam wizdata CC0、P3 北汉山 Udonhan1992 CC0 + 苹果 Paul Cézanne PD、
  P4 棒球 Bain News Service PD、P5 学习 Gary Todd CC0；credit 行取 Commons API Artist 字段原文形式，
  与 KIT §2 一致。
- ABSTRACT：英语单行（去空白 294 字，含换行 295 字），无 ASCII 双引号，含真实主题关键词
  （Ipdong week、last autumn foliage weekend、kimjang season opening、CSAT countdown、
  Korean History exam sign-up、autumn baseball news）与学习者检索短语
  （`learn Korean by reading real Korean news`）、级别 A2–B2、150 exercises。
- 主题与日期：刊期 2026-11-02（周一）至 2026-11-08；立冬 2026-11-07（周六）、
  高考 2026-11-19（周四）、韩史考试 2026-11-28（周六），D-17（11 月 2 日）/ D-12（11 月 7 日）
  均指向 11 月 19 日；“高考日措施仅 11 月 19 日”逐处核对：全部措施表述均绑定 11 月 19 日
  （含 `Special measures apply only on November 19.`、`이번 주에는 특별 조치가 없어요` 等反向限定），
  无其他日期的措施表述。国际政治词汇（Ukraine / Russia / war / Putin / Gaza / Israel / Taiwan / China
  等英韩双语）出现 0 次。

### 11. 卡面目视（8/8）

P1–P8 卡面全部目视通过：刊头与徽章、暗带、gloss 盒、照片与 credit、对比表、误诊室、
读者来信角、P7 预告带、P8 A–H 区与 150 条答案流均无遮挡、溢出、截断、错位。
P8 卡面可见 72 题 `…cake and / taffy` 与 136 题 `…place of an / action` 为正常换行（见非阻塞观察 4）。

## 非阻塞观察（纸面正确，KIT/声称文字有误，仅记录，不构成阻塞项）

1. **P8 双路径声称修正**：构建员/KIT §5 称“两版均为 CLEAN、keydiff [137,138]”。
   独立重测：旧版实际为 [109, 137, 138]，新版为 [137, 138]；109 已在印刷行层面裁定为旧版工具解析 artifact，
   新版正确。纸面（分版 P8）无误；声称中“两版均为 [137,138]”一句不准确，KIT §7.4 本身已记录 109 的根因，
   与 §5 的表述不一致。
2. **KIT “25 条”算术错误**：KIT §5/§7 称韩语引用注释“25 items”，但其枚举区间
   （25–28、34、43–46、57–64、135–136、141–144）合计为 **23 条**；独立逐条复核亦为 23 条，
   全部冻结 headword + 英语环绕。纸面无误；KIT 数字应为 23。
3. **Round-1 canonical 10 旗清单存档缺失**：现存构建文件中只有 Round-1 自定义审计
   （`round1-audit.txt`，其 right-edge 旗多为旧版锚点未感知误报）与运行日志，
   未找到 Round-1 canonical 审计的 10 旗逐条清单，故“Round-1 10 旗”本身无法独立再验；
   但 Round-1 的 FLOW OVERFLOW、P8 基线 2624、P7 预告首行 2539.5 均有日志/审计为证，
   且终版经 canonical、自定义审计、本科对独立扫描三法复核均为 0 旗，修复结论不受影响。
4. **测量脚本显示 artifact，非纸面缺陷**：
   - `round2-measurements.txt` 中的 `taffy`（150 题后）实为 72 题注释换行续词（`…glutinous rice cake and / taffy`），
     `action` 实为 136 题注释换行续词（`…place of an / action`）；60 题的
     `바뀌다:action바뀌었어요` 为该脚本按文档顺序拼接的 artifact；SVG 印刷行逐行核对三处均干净。
   - 范文 157 字口径：MODELO 原文去空格 = 157，`예: ` 标签不计；若连标签计入渲染行则为 159。
     纸面 `157자 / (157 characters)` 与源码定义一致。
5. **KIT §5 措辞说明**：`Han characters = 0` 指汉字区间 U+4E00–U+9FFF（中文讲解层），
   非韩语音节——分版韩语正文完整保留（见 §2 多重集核对），该句在 KIT §3 的区间定义下成立。

## 证据文件

- 本报告：`hidden_files/w45/ko-en-proof/REPORT.md`
- 校对前后哈希：`hidden_files/w45/ko-en-proof/hashes-before.txt`、`hashes-final.txt`、
  `core-hashes-before.txt`、`core-hashes-final.txt`
- P8 双路径：`hidden_files/w45/ko-en-proof/scratch/p8-old.json`、`p8-new.json`、
  `core-old.json`、`core-new.json`、`ed-old.json`、`ed-new.json`
- 几何：`hidden_files/w45/ko-en-proof/scratch/occlusion-ed.json`、
  `occlusion-ed-core.json`、`audit-ed-core.txt`、`myscans.json`
- 冻结与登记：`hidden_files/w45/ko-en-proof/scratch/freeze-diff.json`、`rerun.log`、
  `rerun-svg/`（8 张重跑 SVG，与交付逐字节相同）
- 其余中间文件均在 `hidden_files/w45/ko-en-proof/scratch/` 内；交付目录与核心目录未被改动。

## 未做事项（按任务约束）

未宣布上架；未发 Discord；未往主聊天发卡片/PDF；未建 cron；未碰 `weekly-git`；
未改核心/W43 目录；未清理共享 scratch 目录；未派生下级代理。
