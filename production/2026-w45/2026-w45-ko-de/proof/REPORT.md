# 独立校对报告 — Lucerna Weekly W45 KO×DE（韩语目标 × 德语读者）

**结论：ZERO PROBLEMS**

校对员：独立校对（只校对，不改源码，不宣布上架）。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）、未派生下级代理。构建树脚本一律未在原地运行：登记展开与 wrap-spy 均在本科对 scratch 内重定向 OUT 后重跑。

## 0. 开工查重

- 在途进程仅 1 个：fr-de 构建（cwd 为 `hidden_files/weekly-report-w45-fr-de-build`，`render.py`），与 ko-de 树无关，不构成 stand down。
- ko-de 交付物最后 mtime 03:19:29 UTC，03:22 后复查已静默 >120 秒，安全开工。
- 校对前后哈希 diff 为空：`before.sha256 = after.sha256`（交付物），`core-before.sha256 = core-after.sha256`（核心）。交付物与核心在校对中均未被改动。

## 1. 交付物（独立实测，与构建员声称值一致）

- 印刷 PDF `Lucerna-VOL2.pdf`：32,997,603 B，sha256 `d60a7de2dca8c8e6a49f93095d7c4fc8a928b21ea79a5c9cecb0de0a0a5811c5`，8 页。
- 网页 PDF `Lucerna-VOL2-web.pdf`：3,546,997 B，sha256 `2cbdd6355b613829af47f91118db89e2843bcdc3f3d7e91a01e606c65d316652`，8 页。
- SVG×8、卡片×8 齐全，SHA 与 KIT §1 逐一核对一致；`WEEKLY-KIT.md`、`ABSTRACT.txt` 在位。

## 2. 冻结门禁

- **核心基线 8/8 逐字节**：`freeze.py baseline`（核心构建树 `hidden_files/weekly-report-w45-ko-build`，输出重定向至本科对 scratch）复现核心 SVG 8/8 byte-identical，核心哈希与 KIT §3 逐一相符；运行中核心重哈希无变化。
- **韩语正文零删失**：`freeze.py diff --strict-cjk`（exit 0）逐页新增 CJK 字符均为 0：P1 1462→1339、P2 1612→1360、P3 1524→1346、P4 1232→1074、P5 1433→1234、P6 1276→1136、P7 1365→1037、P8 2496→1238（减少量 = 删去的中文讲解层）。逐页增/删串数（最终版）：P1 +20/−19、P2 +42/−39、P3 +33/−31、P4 +27/−25、P5 +36/−35、P6 +21/−19、P7 +39/−40、P8 +176/−169。
  - 附注：构建树内的 `freeze-diff.json` 是 Round-3 旧版（P1 仍为两行日历行，+21），最终重测与 KIT §7 的 +20 一致；差异恰为 Round-4 日历行合并，非问题。
- **P7 词框目标语定义句逐字冻结**：P7 被删的含韩语串逐条核查，全部是中文讲解行、德语化后的栏目标题/披露句（见 §7）或句式说明的中文部分；A2/B1/B2 三栏韩语定义散文无一被删，仅 gloss 本地化（`=` 式德语 glossline）。P7 词框定义句冻结成立。
- **桥接词 0**：`桥接` 在交付 SVG 全文、构建代码（`*.py`）、KIT、ABSTRACT 中均为 0 命中。

## 3. P8 比较（双版本必做，显式双路径，`--total 150`）

工具版本实测 SHA：旧版 `tools/p8.py` = `67df05f1…`（已恢复的验证版）；新版 `hidden_files/w45/p8-dash-fix-verify/p8.py.new` = `96fc2cfe…`（本科对 scratch 副本同 SHA）。两版各跑一次 `compare`：

| 版本 | 结论 | noted 核心/分版 | missing / extra / uncertain | keydiff |
|---|---|---|---|---|
| 旧版（67df05f1…） | CLEAN | 150 / 150 | [] / 0 / [] | [109, 137, 138] |
| 新版（96fc2cfe…） | CLEAN | 150 / 150 | [] / 0 / [] | [137, 138] |

- **#109 裁定（以印刷行实测为准，新版正确）**：
  - 核心印刷段：`기준 — 日期不同因标准不同（3版）`；分版印刷段：`109. 기준 — Andere Daten, andere Kriterien (Seite 3)`（P8 卡面亦可见该行）。
  - 破折号式 `N. key — note` 下，键 = 首个 ` — ` 之前，即两版均为 `기준`，逐字节相同。旧版因尾括号组先于破折号规则，把注释吸入键候选（核心键误作 `기준 — 日期不同因标准不同`，分版键误作 `기준 — Andere Daten, andere Kriterien`），制造假 keydiff；新版“破折号在括号组之前则破折号胜”规则修正了这一点，与 NL×DE 先例同类。**#109 为旧版工具伪影，不是真实键差异。CLEAN 结论在印刷行层面成立。**
- **#137 / #138 为真 E 区重定向德语键**：137 `Der 7. November ist Ipdong. — Siehe Seite 1`；138 `Bis zur Suneung sind es noch 12 Tage. — Siehe Seite 5`。#139/#140 键韩语逐字节相同，无 keydiff；#150 键 `✓` 相同。
- **P8 注释完整性**：150 条编号段核心与分版逐段比对，**相同编号段 = 0 条**，即核心每条注释均已本地化，无未译注释残留。相同非编号行仅为 8 个冻结韩语组标题（`— 제1면 —` … `— 제8면 —`）与冻结韩语题干/键（如 #139/#140 键），均属目标语冻结文本，非注释。
- **P8 注释语言纯度**：全部 150 条注释的 Han 表意字（U+4E00–U+9FFF，即中文残留）= 0；全版 8 页交付 SVG 的 Han 表意字总数亦为 0（核心为 2136，全系中文讲解层，已清零）。21 条注释含 Hangul，逐条核查均为**目标语词头 + 德语释义**的既定格式（如 #25 `김장=Kimchi für den Winter a`、#57 `Vergangenheit von 이기다: 이겼어요`、#141 `입동=Winterbeginn a`），与核心同类注释的词头保留规则一致，不是跨族残留，不构成阻塞。

## 4. Gloss（渲染 · 切分逐项重测）

按 tools README #21 方法独立重算（gloss()/glossline() 渲染串按 `·` 切分，并逐项核对词头在渲染中存活）：

| 页 | P1 | P2 | P3 | P4 | P5 | P6 | P7 | 合计 |
|---|---|---|---|---|---|---|---|---|
| 核心 | 5 | 19 | 16 | 10 | 16 | 12 | 6 | 84 |
| 分版 | 5 | 19 | 16 | 10 | 16 | 12 | 6 | 84 |

核心 = 分版，逐页分布一致。唯一核查器假阴性：`하나가 되다`（P4）在渲染中跨行断为 `하나가` / `되다 = eins werden.`，词头实际完整在版，非缺失。（初版计数曾因括号内 glossline 漏计 P4 1 项得 83，修正行解析后为 84，与构建员声称一致。）

## 5. 金句（8 句全版频次，SVG 全文去空白拼接重测）

| 句 | 频次 | 分页 |
|---|---|---|
| 11월 7일은 입동이에요 | 5 | P1×3、P7×1、P8×1 |
| 절정에 가까운 주말이라고만 말할 수 있어요 | 2 | P1、P7 |
| 김장은 겨울 내내 먹는 김치를 담그는 일이에요 | 4 | P1、P2×2、P7 |
| 수능까지 17일 남았어요. 오늘이 D-17예요 | 2 | P2、P7 |
| 낮은 길은 더 늦게 물들어요 | 2 | P3、P7 |
| KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요 | 2 | P4、P7 |
| 온 나라가 수험생을 응원해요 | 2 | P5、P7 |
| 날짜를 먼저 보세요 | 2 | P6、P7 |

频次 = 核心（5/2/4/2/2/2/2/2），每句页签与 KIT §8 标注页相符。

## 6. 几何门禁（输出全文存于证据文件，未截断）

- **Canonical `occlusion_audit.py`**（自检 6 类全触发）：分版 0 flags、核心 0 flags、**NEW vs 核心 0**。
- **ADVANCE 全页右缘扫描**（内框 x=1910）：0 flags。**全页框线扫描**（墨迹 vs 全部 rect 边框/横线，页脚规则豁免）：0 flags。**同基线墨迹碰撞**（0.6px 容差）：0 flags。
- **P6 图表标签基线锚定墨迹覆盖**（getmetrics 基线锚定法，非 getbbox 法）：12 标签全部 0.0%，门禁 <30% 通过。
- **韩语孤儿扫描**（本科对 scratch 内 wrap-spy 重跑；窗口 10–45、≥3 音节尾标准，全部散文栏）：去重后 535 条 wrap 记录、422 条含韩语、818 行、396 个接合，与构建员声称一致；行首 NO_START 0、≥3 音节分裂 0、1–2 音节分裂 0，396 个接合全部词界。本科对 spy 日志与构建员 `spy-wrap.log` 逐字节相同。
- **P8 答案流末端**：键流末端 col3 y=2396（<2540）；4 列最大基线 2514.92 / 2530.48 / 2530.35 / 2379.71（均 <2540）。
- **P7 预告末端**：2483.94（<2540；核心为 2512.94，分版因披露德语化而前移，余量更大）。
- **Round-4 修复核实**：终版 P1 日历行确为单行德语 `Diese fünf Daten sind das Gerüst.`，卡面与 SVG 均无第二行 `Ausgabe.`；终版 canonical 审计 TEXTX 0，无残留遮挡旗。

## 7. 家具三方对照（W45 核心 / W43 同配对 / 本版，SVG 实测；W43 优先于 README #20）

| 槽位 | W45 核心 | W43 ko-de | 本版（实测） |
|---|---|---|---|
| 副标题（韩语行）y | 372 | 366 | 366 ✓ |
| badge | — | y=394、20pt bold BRICK `#a4553a` | y=394、20pt、weight 700、`#a4553a`、advance 971.90625px；串逐字 = W43 ✓ |
| 规则线 y | 392 / 401 | 412 / 421 | 412 / 421 ✓ |
| 暗带 rect y | 424 | 433 | 433 ✓ |
| 带文本 y | 478 / 522 | 487 / 531 | 487 / 531 ✓ |
| 页脚 | `Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY` | VOL.1 式 | `Lucerna · KOREANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF KOREANISCH · ERKLÄRUNGEN AUF DEUTSCH`，8 页全有，基线 2624 ✓ |
| 页码行 | `제 N 면 / 총 8 면` | `Seite N von 8` | `Seite N von 8`，8 页全有 ✓ |

- W43 独立佐证：W43 PDF 为纯光栅（无文本层），故以光栅实测：W43 P1 砖红像素带 272–282 行 → 换算 SVG 约 379–393（20pt badge 基线 394 的字帽/降部区间）；暗带实测顶 311 行 → SVG 433.3；粗规则线 295 行 → SVG 411（≈412）；另目视 W43 P1 顶部裁切，badge 串与本版逐字相同。细规则线 421 在光栅尺度下不可分辨，此为 W43 侧唯一测量局限；W45 核心→本版的 SVG 实测是精确的，且与 W43 可分辨项全部吻合。ko-en 的 17pt olive badge 与本配对无关，未采用。
- 其余家具（KIT §6）：顶条德语段 `Jede Woche eine neue Ausgabe`、gloss 前缀 `HINWEIS · `、带标题 `생활 · Leben` 等 7 式、练习头 `연습 · Übungen Seite N`、P8 头及右线、目录 P8 级 `Alle`、P7 带副 `Drei Niveaus, drei Themen`、glossline `=` 式、德语数字格式、instr 标签映射，逐项与 W43 ko-de 一致。

## 8. 读者来信角（逐字摘录，范围裁定）

- 韩语例信逐字冻结（与核心同串，仅 y 位移）：`「안녕하세요. 저는 대학생이에요. 토요일에는 내장산에 단풍을 보러 가요. 일요일에는 집에서 김장을 도와요. 겨울이 와도 따뜻하게 지내고 싶어요.」 — 독자 편지의 예`。无编造人名、信件、引文。
- 短注：`Beispiel der Redaktion, kein echter Brief.`
- 德语披露（含 3 事实 + VOL.3 承诺）：`Bis Redaktionsschluss kamen keine echten Briefe und keine besten Texte von Seite 8 an. Darum steht hier das Beispiel; unser Versprechen aus dem letzten Heft gilt für VOL.3.`（事实：①截稿时止；②无真实来信；③无 P8 最佳文本；示例刊登；上期承诺顺延至 VOL.3。）
- 征集句（明确祈使，卡面位于来信框内、距金句规则线有空隙）：`Schreiben Sie uns Ihren Brief — und Ihren besten Text von Seite 8!`
- **范围裁定**：征集句字面同时覆盖来信与最佳 P8 文本，超出 pt 族组合先例（来信征集 + 披露顺延 + 预告提及 P8 佳作即判充分）。本版因征集句本身已双覆盖，裁定为充分且更强；预告行（`다음 주 · Nächste Woche (VOL.3)` + 韩语预告体，内含 `여러분의 편지와 8면 쓰기 우수작도 실어요`）**不计作征集**，仅作预告。

## 9. 计数 / 范文 / 图片 / 摘要

- 登记展开（本科对 scratch 重跑，8/8 逐字节复现交付 SVG）：150 题连续；级别 A2 51 / B1 72 / B2 27；页分布 10/18/18/18/18/18/12/38；题型 完成句子 48、单选 52、词汇配对 16、完形 13、造句 8、变换 4、判断 4、翻译 4、写作 1——全部 = 核心。P7：A2/B1/B2 栏各 4 题、诊所 4 项、框 `〜부터 〜까지`（산불조심기간 例）；P8：38 项（A 8、B 8、C 4、D 4、E 4、F 4（141–144 配对）、G 5、H 1）。
- 范文逐字 = 核心：`나의 겨울 준비는 김장부터 시작해요. … 겨울 준비가 끝나면 마음이 든든해져요.`，去空格 157 字（核心与分版构建串逐字节相同；P8 印刷注 `157 Zeichen` 相符；指令 150–200자 区间内）。
- 图片 payload 逐页 = 核心（base64 文本 SHA 前缀）：P1 1（`535fff46b7ce`）、P2 1（`e66d2b455ec6`）、P3 2（`e266b6ee1a87`、`5bea45d1f81e`）、P4 1（`1a7e7d6d5ffc`）、P5 1（`6a1bab177d54`）、P6/P7/P8 0。credit 均在页、取 Commons API Artist 字段原文：P1 lumoplank CC0、P2 wizdata CC0、P3 Udonhan1992 CC0 + Cézanne PD、P4 Bain News Service PD、P5 Gary Todd CC0；资料照片注记在位。
- ABSTRACT：德语单行（1 行）、ASCII 双引号 0 个；真实主题关键词（Ipdong-Woche、Herbstlaub-Finale、Kimjang-Beginn、Suneung-Countdown、Haneunggeom-Anmeldung、Herbst-Baseball）+ 学习者检索短语（`Koreanisch lesen lernen mit echten Nachrichten`）+ Lucerna Koreanisch VOL.2、A2–B2、150 Übungen。

## 10. 目视（全 8 卡，非抽查）

p1–p8 全部整幅目视：无重叠、无截断、无错位框。P1 日历单行、P4 括号表、P6 对照表、P7 来信框与预告带、P8 四列答案流至页脚规则线均干净。

## 11. KIT 文字观察（非阻塞；纸面正确）

- 构建树 `freeze-diff.json` 为 Round-3 旧版（见 §2 附注），KIT §7 的终版数字与本科对重测一致，非纸面错误。
- KIT §7 “Han 0”指 Han 表意字（中文字符），非 Hangul；21 条含韩语词头的注释属目标语词头保留规则（§3 已裁定），KIT 同节亦载明该规则，无矛盾。

## 证据文件

- 本报告：`hidden_files/w45/ko-de-proof/REPORT.md`
- 校对前/后哈希：`hidden_files/w45/ko-de-proof/before.sha256`、`after.sha256`、`core-before.sha256`、`core-after.sha256`（diff 均为空）
- 冻结重测：`hidden_files/w45/ko-de-proof/scratch/freeze-diff-rerun.txt`、`.json`；基线：`scratch/baseline.txt`、`.json`
- P8 双版本：`scratch/p8-old.txt`、`.json`、`p8-new.txt`、`.json`、`p8segs-old.txt`、`p8segs-new.txt`
- 几何：`scratch/occlusion-ed.txt`、`.json`、`audit-extra.txt`、`spy-wrap.log`（与构建员日志逐字节相同）
- 登记/分析：`scratch/reg-run.log`、`analyze.txt`、`analyze2.txt`、`gloss.txt`、`pdfbbox/`、`w43img/`、`w43-badge-crop.png`

**不宣布上架。** 是否入库由父线定夺。
