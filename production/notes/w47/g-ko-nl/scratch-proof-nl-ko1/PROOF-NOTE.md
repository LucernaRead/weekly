# PROOF-NOTE — 2026-W47 · nl → ko（荷兰语目标语 × 韩语读者）· proof1 独立复校

- 版目录：`production/2026-w47/2026-w47-nl-ko/`（规范路径）
- 复校员：独立复校（proof1）· 2026-11-11
- 依据：仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑；讲解层用读者母语；对外内容禁内部标签）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-ko1/`
  （本目录内旧 build-1 轮次文件已归档至 `archive-build1-proof/`，本次全部证据为 build-3 新跑；delta 脚本只作方法参考，盒标题扫描与关键探针均为本版重推导重写）
- 解释器：`tools/venv/bin/python`；TMPDIR 全程指向本 scratch 下 `tmp/`；`PYTHONDONTWRITEBYTECODE=1`；
  全部重建/探针均在 scratch 内完成，生产只读，未改任何生产文件，未 commit/push，未重渲染交付 PDF。
  收尾复核三 SHA 与开工值逐字节相同。

## 结论：(a) 零缺陷可定稿

17 门机械门禁全部通过（实测值见 GATE-LOG.md）；8 页已逐页目视；
150 题 registry vs text.md vs P8 三方 149/149 全合（+ Q150 开放写作例外已核实）；
delta D6–D11 逐项复核通过；P8 标题疑似越边独立裁决为**观察，非缺陷**（见 D-01）。

## 身份核对（开工 / 收尾两次实测一致）

| 件 | SHA-256 | 字节 | KIT |
|---|---|---|---|
| 印 `De-Lucerna-VOL4-nl-ko.pdf` | `c4f446b9adc06c29be6a047abf30c83a445062bc26335a578a9609afb42d537d` | 17,281,343 | 一致 |
| 网 `De-Lucerna-VOL4-nl-ko-web.pdf` | `75f6730e10925f575c4a348e0428cdf6c85be2bb658ed4e9037a85d55ae1176e` | 1,919,772 | 一致 |
| 文 `2026-w47-nl-ko.text.md` | `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9` | 47,585 | 一致 |

## Delta D6–D11 逐项复核（不重复修，只验）

| 项 | 复核结果 |
|---|---|
| D6 P3 桥接 `content34.py:78` `w=414.35` | 本版预先无孤儿；SVG 实测 2 行：`현재완료로 채우세요. 조동사 hebben/zijn에 주` (y=2250.5) / `의하세요.` (y≈2280.2)，末行非标点；p3 SVG 与 build-2 前值 `bbdfd827…` 字节一致 |
| D7 P7 桥接 `content7.py:19` `w=423.65` | 2 行：`de wedstrijd 경기; de groepswinst 조 우승; de` (y=725.66) / `kwartfinale 8강전; scoren 골을 넣다.` (y=755.385)，句末 `.` 附着行末；p7 SVG 与 build-2 前值 `4cfecc9e…` 字节一致 |
| D8 P6 图注 `capcn_w=380.7` (`content56.py:144,157`) | 3 行，基线 635.02/659.44/683.86，末行 `은이 100명)`，无行首标点；p6 SVG 与 build-2 前值 `8a5ff2df…` 字节一致 |
| D9 Q140（三方法） | registry 键 = text.md:415 答案 = P8 节点（y=2143.98）= `Ik maak een surprise met een kort gedicht.`，三源逐字一致；题干 `작은 시가 담긴 깜짝 선물을 만들어요.` 不动（含“小”= kort）；三方比对 Q140 verdict MATCH |
| D10 P7 来信 `dt_zh_w=376.3` (`content7.py:92,101`) | 2 行：`마감까지 편지나 작문이 없어 예시를 실어요.` (y=1754.27) / `약속은 VOL.5로 이어져요.` (y=1782.67)，句末 `.` 均附着；p7 SVG 字节一致（同 D7） |
| D11 P4 HET PROGRAMMA `content34.py:130` 顶留 89 / 盒 638.0（双法） | 盒 `<rect x=1439.5 y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 1209.49，基线余量 **+20.11px**；真墨余量 **+20.60px**（cards 1×）/ **+20.48px**（印 PDF 150dpi）；盒底下 7px 条带双法 0 墨；卡片目视盒内留白清晰 |

## 重点裁决项 D-01 — P8 `A　VUL DE KRONIEK IN`：观察，非缺陷

- **扫描实测（本版自写脚本 `boxtitle_ko.py`，头标题取自本版源码 `.head()`，盒坐标逐版重推导，未复用任何他版坐标）**：
  59 个标题（38 HEAD 出现 + 21 BOX），1 处 OVER：P8 `A　VUL DE KRONIEK IN`，
  cards 1× 真墨右缘 537，栏右缘 510.5，margin **−26.5px**（与 delta 员数字一致；我的计数口径：HEAD 按 SVG 内出现次数计，38 次——源文件 `.head()` 去重后 31 串——故总数 59，非 delta 的 58）。
- **证伪（双法 + 行级拆解）**：该 head 的 `<text>` 元素（x=88.0, y=201, 21pt 700, `#46581f`）
  与核心 core-nl 的 p8 同位元素逐字节相同；PIL bold 实测 advance 234.79px（svglib 234.86px），
  字形实测右缘 x≈320–323（字形行 y=186–198 最右墨点 320.0），栏内余量 **+190.5px**——字形根本没有越边。
  −26.5 的墨点来自扫描带（基线上下 1.3×/0.6× 字号）内与标题无关的元素：
  y=174/178 行横贯窗口的墨（版头带下沿）与第 2 栏 B1 色块（`rect x=538.5 y=180 w=60 h=30 #46581f`）左缘抗锯齿——
  扫描窗向 gutter 伸了 28px，把栏外色块左缘 1px 吃了进来。印 PDF 150dpi 渲染同法重测：字形行最右墨 320.6，
  窗口最右 537.6，结论相同。
- **核心对照**：core-nl cards 同位测量逐值相同（87..529 / 530..544 / 87..537，各行最右墨点完全相同）——
  该几何是冻结核心设计，非本版回归。
- **300dpi 裁图目视**（`crop-p8-headA-300dpi.png`，印 PDF 300dpi；另有 `crop-p8-top-300dpi.png`）：
  `A　VUL DE KRONIEK IN` 字形完整（末字 N 无裁切），下划线止于栏缘，与第 2 栏 B1 色块之间有清晰空白，
  无任何重叠、无裁切。
- **STRADDLE 裁定**：越边 = 缺陷当且仅当字形被裁 / 墨迹与他元素或可见边框重叠 / 与有备份的旧版相比为回归。
  三者皆无：字形完整、零重叠、核心同位相同。记**观察**，不报缺陷。
- **跨版影响**：nl-en 同项亦为 −26.5（其 59 标题扫描报 0 越边，应为计数口径/扫描窗差异，并非本版独有）；
  建议协调员决定是否立项 sweep 全家：统一盒标题扫描口径（以字形行实测墨右为准、扫描窗不伸入 gutter、
  或排除栏外色块），并复核各版同位 head。**本版不定稿不受此影响**。

## 其他观察（非缺陷，不修不报）

- 孤儿填空行（Q130/Q36/Q37 式 `___` 行）：属观察类、核心继承；全版孤儿扫 (a)/(b) 均为 0，
  与核心集逐项比对 0 新增。
- `next Sunday`：冻结核心，永不作缺陷。
- 奶油盒 3 处 CREAM-BOTTOM 报警（P2 EN JIJ 1417.8 vs 1416.8；P5 EN JIJ 966.4 vs 965.5；P6 图注 689.4 vs 691.0 内）：
  均为 descent-allowance 假阳性，PIL + 交付 PDF 渲染像素双法 7px 条带 0 墨（见 GATE-LOG 门 7）。
- 盒标题扫描其余 58 标题全部 ok；最紧余量除 D-01 外为 +0.5px（多处 head 下划线止于栏缘−0.5px，属设计）；
  P8 `H　SCHRIJF ZELF` 余量 +1.0px。

## 150 题三方手验与语义抽查

- 机械三方（registry-new.json ← scratch 重建 dump；text.md 韩语标记 `— 정답：` 142 处 + `(정답 x` 8 处；
  P8 `p8.py extract --json`）：**149/149 MATCH，DIFF=[] MISSING=[]**；
  Q150 例外已重组核实：P8 键 `✓`，text.md Tekstmodel 81 词，REG 为开放写作占位符，三者自洽。
- p8 compare vs core：CLEAN，keydiff [137, 138]——翻译题键即读者语（韩语），属设计。
- 语义抽查（逐组核对配对题 + 单题 ≥8 题，键–干逐项核对，防三方一致也查不出的错配）：
  Q1/Q7 20:45（正文 "begint om 20:45 uur in het Olympiastadion" 有据）；Q2/Q113 Berlijn（互证一致）；
  Q15/Q23/Q149/Q137 Sinterklaasjournaal 18:00（正文 "elke dag om 18:00 uur op NPO Zapp" 有据）；
  Q20 Pakjesavond 5 december；Q22 11월16일→12월5일 = 19일（验算 14+5）；Q25–28 配对逐组核对：
  a. een lijst met wensen voor→verlanglijstje、b. een klein versje→gedicht、c. eten voor Sinterklaas' paard→wortel、
  d. die staat 's avonds bij de deur→schoen，P2 选项与 P8 键 25.d/26.c/27.a/28.b 完全一致；
  Q32/Q37/Q139 88e editie（正文 "de 88e intocht in Amsterdam" 有据）；Q126 PSV 26 分（D5 积分行 "PSV 26, Feyenoord 25, Ajax 25" 有据）；
  Q137 荷→韩 "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien." → "신터클라스 뉴스는 매일 18:00에 방송해요." 译法对；
  Q138 "De nummers één en twee gaan naar de kwartfinales." → "상위 두 팀이 8강전에 진출해요." 译法对；
  Q141–144 配对逐组核对：a. een klein versje→gedicht (144.a)、b. een dagelijks nieuwsprogramma→journaal (141.b)、
  c. de eerste plaats in de groep→groepswinst (142.c)、d. die staat 's avonds bij de deur→schoen (143.d)，与 P8 键一致；
  Q145 schoen→A；Q87 图表合计 35+30+20+15=100。**抽查 0 错配**。
- text.md 审计：Han 字符 0；`答案` 残留 0；行数 431；Tekstmodel 81 词；
  ABSTRACT 韩语一行，无 ASCII 双引号。
- 日期：`date -d` 验 2026-11-16 星期一、2026-11-22 星期日；P1 刊头 `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026`；
  P7 下周预告 "Dinsdag 24 november … Zondag 29 november" 与日历一致（24 日星期二、29 日星期日）；VOL.4 每页 1 处，共 8 处。
- 目视 8 页：P1 头条/数字盒/BLIKSEMQUIZ；P2 EN JIJ 句点附着、D 选项短式；P3 桥接 2 行；
  P4 HET PROGRAMMA 盒内留白；P5 EN JIJ 句点附着；P6 图表+图注 3 行；P7 BRIEVEN 盒止于 ZINNEN 线上；
  P8 答案 1–150 齐全、钢笔图。**目视 0 缺陷**。
