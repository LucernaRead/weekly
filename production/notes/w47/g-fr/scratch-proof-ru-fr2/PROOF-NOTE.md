# PROOF-NOTE — 2026-W47 ru-fr · proof2（re-fanout 重建版独立复校）

**版本：** `production/2026-w47/2026-w47-ru-fr/`（Russian target × French readers），
由 core-ru fix1（`f11854bf`）全量重建
**复校员：** proof2（独立；与 #1 复校员不同 session）
**日期：** 2026-11-11
**范围：** print PDF 8 页 200 dpi 全页目检 + `text.md` 全文 838 行通读 + 150 题 key 逐项手核 +
全部机械门独立重跑（不信任 KIT/重建记录，只作对照）
**工作区：** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-fr2/`
**纪律：** 未修改 production 下任何文件，未 commit/push；开工前与收尾时三件 SHA 均与任务一致。

## 身份核对（磁盘 = 任务，开工前与收尾后两次实测一致）

| 文件 | SHA-256 | 字节数 |
|---|---|---|
| `Lucerna-VOL4-ru-fr.pdf`（print） | `8f09a2703081f12b76ace75331a79b5c4507282894b119298e68b7ce77c83562` | 21,291,969 |
| `Lucerna-VOL4-ru-fr-web.pdf`（web） | `45f6401dc1e20dfc12d596d4d31e49e4803f6a41c442d9e757940ef15d823929` | 3,385,758（< 7 MB ✓） |
| `2026-w47-ru-fr.text.md` | `7a402199542afaf125a8648fe7fd4bcc67766718e0e70b2351e35418b18522ec` | 63,543 |

核心对照 core-ru fix1 亦实测一致：印 `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` /
31,429,147 B；网 `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` /
4,025,834 B；文 `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` /
60,953 B。Edition 目录仍为 untracked（`?? production/2026-w47/2026-w47-ru-fr/`）。

## 结论：(a) — 零缺陷，可定稿

#1 的唯一阻塞缺陷（web PDF 丢斜体，机制问题）已在本重建版中修复，三症状逐项复测归零；
其余全部必查项与全部机械门均通过；回归对照证明 49 处 fr 手工修正无一丢失，
SVG/text.md/content 的全部差异均可归因于 D1/D2/D6/kicker 四项既定改动。
未发现任何须修缺陷。

## #1 缺陷回归：D1 web PDF 斜体三症状——已修复（逐项复测）

#1（PROOF-NOTE.md 结论 (b)）：web PDF 丢失斜体字面（`webpdf.py` 子集化机制），
P1 词条 «чёрная пятница» 三症状。本轮用 span 级 + 渲染视觉双重复测：

| 症状 | #1 旧版实测 | 本重建版实测 | 结论 |
|---|---|---|---|
| 斜体丢失 | web 零斜体字面（仅 Regular/Bold） | web 含 `LucernaNotoSerif-Italic`、`LucernaNewsreader-Italic`；词条 span 为 `LucernaNotoSerif-Italic` 16.12 pt | **已修复** |
| 空格丢失 | web span 存为 `чёрнаяпятница` | web/print 的 `чёрнаяпятница` span 均为 0；词条 span 存为 `чёрная пятница`（带空格） | **已修复** |
| 闭引号脱离 | web 文本层 ` »` 2× vs print 1× | print/web ` »` 均为 1× | **已修复** |

- 附加证据：print/web 非空字符 multiset 全等（30,771 字符，逐页亦全等）；
  空格数 print=web=4,880，换行数 print=web=1,599，差值均为 0（#1 旧版为 +42 空格/+6 换行）；
  pdftotext 字节数 print=web=57,973 B。
- 视觉证据：`crops/crop-wordweek2-web.png` 与 `crops/crop-wordweek2-print.png`
  （P1 СЛОВО НЕДЕЛИ 框 2× 放大）：web 版 «чёрная пятница» 呈斜体、词间空格清晰、
  闭引号贴合，与 print 版视觉一致。
- 机制归因：重建 records 称 web PDF 由已修补的 `webpdf.py`（commit `40963281`）重建；
  本轮只验证结果——斜体已确实嵌回，不再追究机制。

## 必查项 verdicts

1. **D1——全部落地。**4 串均在 SVG（P6 标题 s1、P6 免责声明 s2、P7 副标题 s3、P8 副标题 s4，
   与 `build_map.py` 的 KEEP_AS_IS fr 值逐字比对一致）；免责声明仅 SVG、不在 text.md ✓；
   text.md 三段分别在 L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、
   L596 `Большой тест недели + все ответы`，与任务落点逐行一致。
   fr 手工修正 49 值已保留：新 map = 旧 map + 恰好 4 条 D1 改动（`lit` 桶 changed=4，
   其余桶 0 改动、0 丢失、0 新增），见“回归对照”节。
2. **Kicker——落地。**9 处双空格在 content12.py:18；PIL 真墨间隙
   `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`，最小 5.9 px ≥ 4；
   P1 kicker 行与 core 逐字相同。
3. **D2——落地。**Q25 选项为短式 `День студента`（P2 SVG 选项 b，text.md L187）；
   全称 `Международный день студента` 在 text.md 仍 ×2（P2 正文 + Q11 题干），与 core 计数相等。
4. **D6——落地。**Q20 key `желании`（text.md L173 题干 key 与 L694 答案行均已改）；
   text.md ×2；P8 提取 key 20 = `желании`，与 core `ru-p8.json` 一致。
5. **`___` 空白——87 处，非缺陷。**字面 `___` 在 text.md 共 87 处，与任务数一致；
   为 core 继承的模板缺口（填空题干），按 core-ru 首校裁定不作本版缺陷、不逐版修。
6. **150 键逐项手核——150/150 PASS**（`keycheck-150.json`，自建比对表，非复用 #1  verdict）。
   印刷 P8 key vs text.md key：149/150，仅 Q150 除外（印刷 `✓` vs text.md 括号说明，
   同义的表示差异）；vs core 直接比对 keydiff 恰为 `[137, 138, 139, 140]`。
   20 道 Appariement 的选项单逐一从练习 SVG 核对（P2 D、P3 C、P4 C、P5 C、P8 F 的 a–d 全文提取）；
   Q137–140 法语翻译逐句回译核对；G 对话按 P8 SVG 顺序通读核对（Q147 见观察 OBS-4）；
   Q137 在本版 P8 提取中为完整句，未见任务所注的 em-dash 提取截断（提取值
   `Mardi 17 novembre, Journée des étudiants.` 与 text.md 答案逐字一致）。
   级别 A2 50 / B1 76 / B2 24；题型 Compléter 54 / Choix 55 / Appariement 20 /
   Phrases 12 / Transformer 4 / Traduction 4 / Rédaction 1；按页 10/18/18/18/18/18/12/38。

## 回归对照（与 #1 备份 `backup-old/2026-w47-ru-fr/`）

- **text.md：** 恰好 6 对行差异（L173 D6 key、L187 D2 选项、L459/L504/L596 D1 标题、
  L694 D6 答案行），余无他变；63,489 → 63,543 B。
- **SVG 文本 run：** P3/P4/P5 零差异；其余 5 页的 71 处 (x,y) 差异全部归因于
  D1/D2/D6/kicker（P1 kicker 双空格重排、P2 D2 短式、P6 D1 s1+s2、P7 D1 s3、
  P8 D6 答案注 + D1 s4），无任何其他内容变动。
- **content\*.py：** 仅 4 文件变，且仅为既定改动——content12.py（kicker 双空格 +
  D6 + D2，附修复注释）、content56.py（D1 s1+s2）、content7.py（D1 s3）、
  content8.py（D1 s4）。其余文件全同（`ABSTRACT.txt` 435 B 逐字节同；仅重建产物
  PDF/SVG/cards/KIT 与 `__pycache__` 不同）。
- **KEEP/REVERT 盘点：** 新 surgical map 与首版旧 map 比对：`instr/key/meta/type` 四桶
  0 改动；`lit` 桶 335 条中恰好 4 条改动（即 4 条 D1 KEEP 值），0 条丢失、0 条新增。
  结论：49 处 fr 手工修正全部保留（KEEP），0 处 revert。

## 机械门（全部独立重跑，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| check_core.py | rc=0；golden BAD 0，gloss 0；orphan 1（P7 y553 `”».`，已知良性）；同基线碰撞 1（P1 y1712 `чёрная`，与 core 相同） |
| p8 extract + compare | core 150/150，edition 150/150，**CLEAN**，keydiff `[137, 138, 139, 140]`；vs core `ru-p8.json` 直接比对同为该 4 项 |
| keycheck | 150/150 手核 PASS；印刷 vs text.md 149/150（仅 Q150 表示差异） |
| occlusion audit（真实命令，未加 --selftest） | 42 flags，全 TEXTX，0 LINEX/COVER/FOOTER/EDGE/BOXTITLE；栅格裁决 38/42 CLEAR，余 4（`Краснодар»` ×4）6× 放大裁剪目检 CLEAR——**42/42 CLEAR** |
| creambox（canonical，全 8 页） | 与重建记录扫描、与 #1 扫描均**逐字节相同**；inside-only 负值仅 1 处（OBS-1，见下）；BELOW-WINDOW 95 行（+28.0 ×25、+32.0 ×41、+34.0 ×4、+37.0 ×25），全为既定分类 |
| spill sweep（自写 PIL 真墨扫） | 32 个无描边奶油框逐框扫：盒标题墨框 32/32 在框内（最紧 P6 box2 右缘余 6.8 px）；末行墨底 32/32 在框内（最紧 OBS-1 +1.24 px）；四边穿越 0 处实违规（1 处 EDGE-top 标记已证为框顶上方深绿横条贴合，非穿越）；BELOW-WINDOW 行墨顶均在框底之下，无重叠——**0 违规** |
| freeze baseline（标准口径） | core 构建目录 + core SVG：**8/8 byte-identical**，core 完整性未变；edition-internal 自洽基线（补充证据）亦 8/8 |
| freeze diff | removed distinct 484 / count-sum 850；西里尔删除恰为 15 项（Q46 `можно` ×1 + 14 个 Morozko 图注词，均在 core P8 y≥2450 图注区），unexplained 0；新增 CJK 仅 U+3000 ×8；diff JSON 与重建记录的 `freeze-diff.json` 逐字节内容一致 |
| print/web 文本层 | multiset 全等（总体 + 逐页），30,771 字符；空格/换行差值 0；pdftotext 同为 57,973 B |
| s11_check.py | rc=0，**FAILURES: none**；P8 最小字号 9.75 pt（print/web 同测）；8 页；web 3,385,758 B < 7 MB；SVG 零可见 CJK |
| SVG 零真实 CJK | 8 页 <text> 扫描：真实 CJK 0；U+3000 123 处（分隔符）；text.md / ABSTRACT.txt CJK 0 |
| D5 字体 | 只记录不判定：Newsreader 3426+100 Bold、Noto Serif 2830+83 Bold、Noto Sans CJK SC 433+506 Bold、Noto Sans 219+198 Bold、Noto Serif CJK SC 32+4 Bold、UnifrakturMaguntia ×1（Lucerna 刊名）；SVG 最小字号 13.0 px；P8 PDF 最小 9.75 pt（上行已测） |
| H 范文词数 | 97 词（80–100 ✓） |

## 全书目检（8 页 200 dpi 逐页读）

P1 头版（刊头、kicker、头条、三栏正文、ТУР В ЦИФРАХ 框、СЕЙЧАС ВЫ 1–6、右侧
О ЧЁМ ПИШУТ/В ЭТОМ НОМЕРЕ/СЛОВО НЕДЕЛИ/КОРОТКО 框、照片、СНЕГ БУДЕТ?、Quiz 7–10）；
P2 生活（文章、ЧТО ПОЖЕЛАТЬ?、两 Note 框、ПРАЗДНИКИ НЕДЕЛИ、А ВЫ?、Юон画作、СЛОВА НЕДЕЛИ、
练习 A–D）；P3 文化（文章、А ЧТО УЖЕ В КИНО?、ГЛАВНОЕ/КАК ПРОВЕСТИ ВЕЧЕР 框、练习 A–D，
中段空白为模板留白）；P4 体育（文章、VOL.3 更正、1912 奥运照片、ТОП-5 表、14 轮 8 场比分表、
国家队、15 轮赛程表、练习 A–D）；P5 青年（黑五文章、11.11 段、玉米照片、ДАТЫ 框、练习 A–D）；
P6 大 разбор（文章、НЕДЕЛЯ/ЗА И ПРОТИВ 框、日历条、D1 图表标题+免责声明、练习 A–C）；
P7 语言（A2/B1/B2 三栏、ОШИБКИ 框、СЛОВО 框、ПИСЬМА 框、普希金肖像、ФРАЗЫ НЕДЕЛИ 8 句带页码、
СЛЕДУЮЩАЯ НЕДЕЛЯ）；P8 测试与答案（A–H、G 对话、H 范文、按页答案 1–150）。
8 页均无溢出/重叠/裁切；页脚 `Page N sur 8` 齐全；P4 八场比分与 Q52–55/Q127 一致；
P6 图表 38/26/18/18 合计 100；P7 金句 8/8 原文且页码正确（P1×2、P2×1、P3×1、P4×1、P5×1、P6×2）。

另以 PIL 真墨/advance 复核 5 处低倍下看似连写的接缝（非缺陷）：
P1 `метеорологическая|зима` 间隙 5.55 px、P2 `поздравить|féliciter` 4.62 px、
P1 byline `От редакции|Lucerna` 3.85 px（advance 法；#1 PIL 墨列法为 4.8 px，
与同行 `От|редакции` 3.83 px 同级）、P6 `d’|exercice` 墨间隙 0.25 px、
`D’|EXERCICE` 2.00 px（后两者为 ’ 本身的紧排，非词空格；同字号词空格参比为 5.07/6.76 px）。

## 观察（非缺陷）

- **OBS-1（#1 遗留，复测值完全相同）——P2 “А ВЫ?” 奶油框偏紧。**
  Creambox inside-only：末行基线 1154.0、clearance +5.0、desc-clear −1.0（工具估计）。
  本轮 PIL 真墨复测（新渲染）：末行墨底 1157.8，框底 1159.0，**余 +1.24 SVG px，在框内**，
  与 #1 的 +1.24 完全一致。记为观察项，非缺陷。
- **OBS-2——P3/P5 中段空白。**文章约 y1150 结束、练习约 y1650 开始的大片空白带，
  模板留白，非缺陷（与 #1 同）。
- **OBS-3——P7 普希金肖像。**紧凑居中裁切，头顶近框边；可辨认，非缺陷（与 #1 同）。
- **OBS-4——Q147。**G 对话中卖家说 “Проверьте ___, пожалуйста”（选项 A. посылку · B. промокод），
  key B（промокод）。本轮按 P8 SVG 顺序核对对话：买家买礼物 → 卖家报黑五 → 卖家提醒核对
  （同一卖家回合、店内语境），“核对促销码”连贯；“核对包裹”属收货语境，在此对话中不成立。
  语境较弱但自洽，非缺陷（与 #1 同）。
- **OBS-5——Q62。**`15-й тур ___ 20–22 ноября (быть)` → `будет`，正确俄语、core 冻结措辞，
  非 fan-out 缺陷（与 #1 同）。
- **OBS-6——KIT 若干陈述已过期（仅记录，不构成版本缺陷；KIT 非读者面）。**
  KIT L56 “pdftotext 57,844 B；30,708 字符”——实测 print/web 各 57,973 B、30,771 字符；
  L79 “web 3,346,639 B”——实测 3,385,758 B；L88 “ABSTRACT.txt 434 B”——实测 435 B；
  L76 “freeze 0/8 系已知重定向限制”——#1 已纠：baseline 直接报 8/8，本轮亦然。
  另 KIT L76 行内 freeze 描述与本轮标准口径一致（8/8），唯 “0/8” 说法仍错。

## 未决项（自 #1 原样承接，均为 core 层、非 fan-out 缺陷）

- **O1——P5 Ozon 14,4M 订单数。**“11 ноября 2025 года， на Ozon сделали больше 14,4 миллиона
  заказов за один день”（P5 文章；Q73 key `заказов`）。文章 + Q73 + 答案三处自洽，
  但该精确数字未独立核查公开来源。单源 core 数字；协调员如需溯源属 core 层后续。
- **O2——P3 五部 19 Nov 俄国上映日。**国际日期已核（#1），俄国 19 Nov 本身未独立核查；
  国际日期集中在同一窗口，表述可信。Core 层，非 fan-out 缺陷。

## 交付文件（本 scratch 内）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（机械门证据）
- `keycheck-150.json`（150 项：题干、级别、题型、text.md key、印刷 P8 key、core key、手核 verdict）
- `logs/`（check_core、p8 core/edition/compare、occlusion、creambox、freeze baseline/diff、
  s11、spill_sweep×2、checks2、adjudicate4、print.txt/web.txt、svg-runs-*）
- `render/p-1.png`…`p-8.png`（print 200 dpi）、`render/web-p1-1.png`（web P1 200 dpi）
- `crops/`（`crop-krasnodar-{0,2,3,4}.png` 遮挡裁剪、`crop-p1-boxtop.png`、
  `crop-wordweek2-{web,print}.png` #1 斜体回归对照）
- `checks2.py`、`spill_sweep.py`、`spill_sweep2.py`、`adjudicate4.py`、`build_keycheck2.py`、`run_gates.sh`
