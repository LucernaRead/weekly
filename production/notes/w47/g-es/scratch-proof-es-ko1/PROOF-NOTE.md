# PROOF-NOTE — W47 es-ko proof1（独立复校）

- 对象：`production/2026-w47/2026-w47-es-ko/`，西班牙语目标 × 韩语读者，VOL.4，
  刊期 2026 年 11 月 16–22 日，8 页，练习 150 题
  （A2 50 / B1 72 / B2 28）。
- 印刷 PDF `La-Lucerna-VOL4-es-ko.pdf` 8,874,275 B，
  SHA-256 `ba1a6e0a23a404c53ba1ad8cdfd9a2c83a3810242c08539715d24aed14949b5e`；
  网页 PDF `La-Lucerna-VOL4-es-ko-web.pdf` 1,199,171 B，
  SHA-256 `9117f3c186ee3aeca2a8e92208f590d0c0c4d8eaaeede6d83be5abee99725417`；
  `2026-w47-es-ko.text.md` 46,843 B，
  SHA-256 `ddf077f538a34bb97a3576051305017dcc9944ae933df9dad64d762e1dcad5f7`。
  三 SHA 动工前实测，均与任务书一致。
- 复校员：proof1（独立）。未修改源文件，未重建，未 commit，未 push。
  全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
- 详细门日志见同目录 `GATE-LOG.md`。

## 结论：(b) 有缺陷，共 2 项，均为轻微（minor）

修完 D-01、D-02 即可定稿。其余全部通过。

## 缺陷清单

### D-01 —— 轻微（minor），本版讲解层：弯引号落入 CJK 字体节点

- 标准：任务书要求弯引号 U+201C / U+201D / U+2019 在 CJK 语境计数 = 0
  （P7 Newsreader 斜体对除外；按 <text> 节点字体逐个核查，en-ko1 口径）。
- 位置与内容：
  - **P1**，词汇注 `<text font-family="Noto Sans CJK SC" font-size="19">`：
    `“토론”: 사람들이 공개적으로 토론해요.` —— U+201C + U+201D 各 1。
  - **P5**，C 节小标题 `<text font-family="Noto Sans CJK SC" font-size="20.5">`：
    `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라…` —— U+2018 + U+2019 各 1。
- 合计：CJK 节点内弯引号 **4 个 ≠ 0**。
- 不属缺陷的部分：P8 Q91 的两对弯引号落在 Newsreader 节点（西班牙语题干），合格；
  P7 无弯引号（任务书所称 P7 斜体对在本版不存在）。
- 来源：P1 一对为构建者 KIT §6.2 缩写时手写（harvest ko.json 无此句，仿中文 “辩论” 式）；
  P5 一对来自 harvest ko.json 值
  `ir a + 동사 원형으로 문장을 바꿔 ‘~할 것’이라는 뜻을 나타내세요.`。
- 修复方向：改 ASCII 引号或去引号，与其他 ko 版一致。

### D-02 —— 轻微（minor），本版讲解层：P8 答案键 #45 韩文注残句

- 位置：P8 RESPUESTAS，PÁGINA 5 节，第 45 条。
- 内容：`45. En Bilbao toca la banda el domingo. — 장소가 앞에, 동사는 두 번째`
  —— 韩文注缺系词，句子未完成（应为 `두 번째예요` 或 `두 번째에 있어요`），
  与平行注 #44、#133 的完整形式 `시간이 앞에, 동사는 두 번째예요` 不一致。
- 来源：content34.py:101 原文即如此（`e.ex("B1", "문장 만들기", "En Bilbao toca la banda el domingo.", "장소가 앞에, 동사는 두 번째", …)`），
  非渲染截断。目视 P8 该行完整呈现，无溢出。
- 修复方向：补 `예요`（与 #44、#133 对齐）。

## 观察（非缺陷）

- **O-1**：P5 框题 `EL PLAN DE LA SEMANA　이번 주 계획` text_w 实测 403.8/404.5，
  余量 +0.7——通过但极紧。目视单行容纳，无溢出。
- **O-2（core 级，已裁定）**：13 日 laSexta 辩论主题——版内（沿 core KIT §5.2 裁定）
  写 13 日场只谈经济、18 日场谈住房；Europa Press 2026-11-06 同文称 13 日场为
  “vivienda y economía”。core 已记录来源冲突并选 diariodesantiago.es 的逐场区分，
  本版冻结继承，不另列缺陷。
- **O-3（KIT 记录误差）**：KIT §3 的 P5 注释词计数偏高——papeleta 称 3 次、实测 2 次；
  plazo 称 4 次、实测 3 次（原始 SVG 两次独立计数一致）。§8.1 门（每页 ≥2 次）
  对两词仍通过（2、3），非内容缺陷。其余 KIT 计数（P1 2、P2 2/2/2、P3 5/6/9/4/5、
  P4 2/3、P5 censo 2）全部与实测一致。
- **O-4（核实边界）**：RTVE 免费宣传分钟逐党明细（Frente Amplio 30 / Podemos 15，
  即 Sumar 遗产分配）未在公开页独立确认；档位（10/15/30/45）与合计 195 分钟
  已核实（BOE-A-2026-23258、LOREG art. 64）。记为“可公开核查范围内一致”。
- **O-5（核实边界）**：laSexta 13 日辩论的细节（21:30、Ana Pastor 主持、现场观众）
  为 core KIT 裁定细节，本轮未独立再验；已确认的部分：13 日经济专场辩论本身、
  四名发言人（Cuerpo/Bravo/Bustinduy/Figaredo）、Atresmedia 四方辩论移至 11-23
  （Feijóo/Abascal/Colau 已确认、PSOE 仍邀而未确认）、PP 坚持 11-26 Atresmedia
  四方辩论提案——均与 2026-11-09/10 来源一致。另：P1/P6 “PSOE 未确认任何日期”
  是套餐级未确认的简写（PSOE 已公开接受 Mediaset 11-16 面对面提案，但整套
  辩论安排未定）；版内已明确标注“esta página no da por cerrado lo que aún se negocia”，
  不构成缺陷。

## 已通过的核查（摘要，实测为准）

- **机械门（全部实跑，不信 KIT 数字）**：occlusion 审计 0 flags；p8 extract 150/150；
  p8 compare vs core-es CLEAN（keydiff=[137, 138]，KIT §6.12 已裁定的翻译键重定向）；
  freeze baseline 8/8 SVG byte-identical；freeze diff 无西班牙文本丢失；
  freeze_direct 渲染层 8/8 PASS（frozen 151/143/141/144/139/159/115/478，均 ≥100），
  源码层严格匹配 FAIL 经逐项裁定 PASS（5 项移除均有出处、126 项新增含 0 个 core 外拉丁词）；
  creambox 严格口径全部 clearance 为正（最小 +1.9；P7 工具盒 +5.7）；
  boxtitle 全标题 25 fit / 0 over；印/网文字层 pdftotext plain 各 47,790 B 字节一致，
  逐页 8 页字符数一致；sweep（bridge orphans 0 / box-vs-hline 0 / widows 0）；
  P8 最小字号 PyMuPDF 实测 **10.125pt**（与 KIT 一致，在 §1.1 让步链内）；
  VOL.4 ×9 / VOL.5 ×3（均为下期预告正当引用）；“12 de noviembre” 0 处；
  三色蛾 title 仅 P1；P8 徽章配色与 KIT 一致；
  §1.1 字体/配色（Newsreader 1507 / Noto Sans CJK SC 622 / Noto Serif CJK SC 622 /
  UnifrakturMaguntia ×1；纸色 #fbfaf6 8 页全有；填充色谱与 core-es 一致）。
- **150 题答案键**：源码顺序提取 REG（content12 Q1–28、content34 Q29–64、
  content56 Q65–100、content7 Q101–112、content8 Q113–150），共 150；
  与 p8extract 对比仅 Q150 一处差异（开放写作题，P8 印 ✓，属预期）；
  逐题语义手验全部通过，匹配题键与题干定义一致（25–28、52–55、141–144 逐一核实）。
  H 范文词数脚本实测 **97**（与版内 “97 단어” 一致）。
- **外部事实（网上逐项复核）**：29-N 大选（Real Decreto 806/2026；竞选 11-13–27 共 15 天；
  投票 11-29 9:00–20:00；邮寄投票至 11-19；禁发民调 11-24–28）；La Liga J13 十场
  赛程（11-20–23）与 J12 后积分（Barça 33、Madrid 30、Atlético 28）全部一致；
  欧冠 J5 对阵（Real Madrid–PSV 11-24；Sabah–Barça 11-25 18:45；Atlético–Viking 11-25）
  与 J4 战绩（Barça 3–0 Aston Villa、Madrid 3–2 AEK、Atlético 0–2 Bayern）全部一致；
  弗拉门戈（UNESCO 2010-11-16 内罗毕列入）、Santa Cecilia（11-22）、
  毕尔巴鄂市立乐队（11-22 12:00 Euskalduna）全部一致；MiDNI（JEC 2026-11-05 解除停用）一致；
  RTVE 分钟档位与 195 合计一致（见 O-4）。
- **全文复读**：text.md 1–1800 行通读；无国际政治内容（仅西班牙国内选举）；
  P7 FRASES 8 句逐句与正文核对逐字一致、韩文译准确；日期星期以 `date -d`
  （Europe/Madrid）逐一核验，全部与版内一致。
- **8 页目视**：cards/*.png（1950×2700）逐页读过。无溢出、无重叠、无页脚侵入；
  P6 图表条长与分钟数成比例；P1 插图为编辑部线描并注明非照片；
  P3/P5/P7 图注均有 PD 来源。
- **KIT 自检复核**：上表各项中 KIT 所称数字除 O-3 两处计数外，全部与独立实测一致。

## 交付文件

- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`
- 支撑数据：`occlusion.json`、`p8extract.json`、`p8compare.json`、
  `freeze-diff.json`、`freeze-direct.json`、`reg.txt`、`logs-*.txt`
  （均在同 scratch 目录）
