# W47 nl-en 第三轮独立复校笔记（reproof，第二轮全量复校，SOP §8.4）

# 结论 (a)：零缺陷，可以定稿。

- 版：`2026-w47-nl-en`（荷兰语目标语 × 英语读者），VOL.4，刊期 2026-11-16–2026-11-22
- 校对员：独立复校员（与 builder / fix1 / proof1 / proof2 不同人；先前笔记与 fix 记录只作参考，全部结论自己重核）
- 日期：2026-11-11
- 对象：印刷 PDF `De-Lucerna-VOL4-nl-en.pdf` + 网页 PDF `De-Lucerna-VOL4-nl-en-web.pdf` + `2026-w47-nl-en.text.md`（build 11）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-nl-en1/`（全部中间件与报告只在此；未在 `~/workspace/weekly-git/` 下建 scratch；TMPDIR 全程指向本 scratch 下 `tmp/`；未用系统 /tmp）
- 渲染：全部 8 版均从交付印刷 PDF 用 `pdftoppm -r 100` 重新渲染后目视（`render/p-*.png`），不采信 builder 的图；网页 P8 从网页 PDF 同法渲染目视（`render/w8-8.png`）
- 探针：开工前 `git -C ~/workspace/weekly-git hash-object -w /dev/null` = `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；在本 scratch 内真实写文件成功。生产目录只读，未写生产文件，未 commit、未 push。

## 身份核验（先核身份，通过）

| 文件 | 字节 | SHA-256（实测） | 与任务登记 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷，build 11） | 12,665,893 | `79fa049b318d94f15f28fe23daefd2513221a77fde6511c694aee109bacf3239` | 逐字一致 |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页，build 11） | 1,610,562 | `d493e11f3c27c7e46e0412c79f1b9208bfe804e39eac2e2203a033fad2818538` | 逐字一致 |
| `2026-w47-nl-en.text.md` | 45,115 | `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978` | 逐字一致 |

三 SHA 全部逐字节一致后才开工。VOL 经 `tools/tables.py vol 2026-W47` 核实 = 4。KIT §11 所记 build 11 三 SHA 与本轮实测一致。

## 缺陷清单

**无。** 本轮为零问题（见下全部核实项）。

## D12 回归核查（fix1 两处，逐项独立重核，均改对）

1. **源码**：`content8.py:85` 现为 `["journaal = news programme b", "groepswinst = group win c", "schoen = shoe d", "gedicht = poem a"]`，142/144 两处均已带空格。
2. **text.md**：第 419 行 `142. de groepswinst — de eerste plaats in de groep (Correct c · groepswinst = group win c)`、第 421 行 `144. het gedicht — een klein versje bij een cadeau (Correct a · gedicht = poem a)`，均带空格。
3. **SVG**：`svg/p8-toets.svg` 中 `142. c — groepswinst = group win c`、`144. a — gedicht = poem a`，均带空格。
4. **全版重扫**（自写 sweep 逻辑复用 fix1 `sweep_eq.py`，三源：`content*.py` 字符串字面量 AST + SVG `<text>` 节点 + `.text.md`，逐个 `=` 查左右空格）：**缺空格 `=` 为 0**；` = ` 有空格 127 处（fix1 修前 121 处；+6 = 两处修复 × 三源各 +2：源码、SVG、text.md 各 2，口径一致）。被扫面无 `==` 误报。
5. **P8 卡片实测（双重独立度量，数值与 fix1 逐项一致）**：
   - (a) 交付卡片 `cards/p8-toets.png`（1950×2700）直接量像素墨 + `svglib.text_w` advance；
   - (b) 从交付 `svg/p8-toets.svg` 用 cairosvg 在本 scratch 独立重渲 `rerender/cards/p8-toets.png` —— 与交付卡片 **SHA-256 逐字节相同**（`81a304dc244708b6d24a235e5f739d4ccbd11d9026d00e7cb1465474885b8fbe`），两份度量结果完全相同；
   - (c) 交付印刷 PDF P8 页（`pdftoppm -r 100`）像素复核（1 SVG 单位 = 1.0417 渲染 px）：142 墨右缘 1655.0 单位（卡片 1652，差 +3px，在 ±5px 系统性差内），余量约 207 单位；144 墨右缘 1597.4 单位（卡片 1595，差 +2px），余量约 265 单位。均远在栏内。

   | 行 | advance | 像素墨右缘（卡片） | 栏右余量（栏 [1439.5, 1862.0]，宽 422.5px） |
   |---|---|---|---|
   | 141. b — journaal = news programme b | 238.5px | 1675 | +187.0px |
   | **142. c — groepswinst = group win c** | **215.5px** | **1652** | **+210.0px** |
   | 143. d — schoen = shoe d | 152.4px | 1588 | +274.0px |
   | **144. a — gedicht = poem a** | **158.6px** | **1595** | **+267.0px** |
   | 145. A — schoen = shoe | 142.0px | 1579 | +283.0px |

   基线 [2267.60, 2297.26, 2326.92, 2356.58, 2386.24]，间距均匀 29.66px——无插入换行、无溢出、无换行后顶位移。141–144 配对键仍为 b/c/d/a，正确。
6. **网页 PDF**：文字层含 `142. c — groepswinst = group win c` 与 `144. a — gedicht = poem a`（带空格）；网页 P8 渲染目视与印刷 P8 一致。

## 全量复校核实项

1. **150 题全量验算**：题号 1–150 连续、无缺号（text.md 独立重数）；逐页 10/18/18/18/18/18/12/38（P1 1–10，P2 11–28，P3 29–46，P4 47–64，P5 65–82，P6 83–100，P7 101–112，P8 113–150）；级别 A2 46 / B1 73 / B2 31（单题标记 A2 43/B1 73/B2 28，另 D 组 25–28 共用一枚 A2 标记、F 组 141–144 共用一枚 B2 标记，合计 46/73/31，与 KIT 一致）。P8 答案 150/150 齐全（`p8.py extract`），`compare` vs core **CLEAN**，keydiff [137, 138]（见下）。全部答案逐题对照题面/正文/图表复核：完成时助动词 39–42（is/heeft/is/heeft）、图表算术 83–87（35/30/65/15/100，35+30+20+15=100）、日期算术 22/43/44/45/46（19 天/1 天/4 小时/19 天/17 年）、判断题 61–64/80–82、gaan 将来时 76–79（gaat/gaan 人称一致：wie→gaat、wij→gaan、zij 单数→gaat、de kinderen→gaan）、过去时 57–60/105–107（speelde/won/verloor/speelden）均与正文一致。范文 81 词（空白切分；不计独立短横 "–" 为 80 词，仍在 80–100 档内，与 P8 注 "81 words" 一致，见观察项 O2）。
2. **keydiff 137/138 已裁定合法**：核心 P8 的 137/138 答案键为中文，en 版为英文（"The Sinterklaas news is on every day at 18:00." / "The top two go through to the quarter-finals."）——翻译题按读者语重定向，方向正确（137/138 为荷→英；139/140 为英→荷，答案键为荷兰语）。符合工具说明 "key diffs are informational"。与 build 10 相同。
3. **金句 8 条**：P7 `ZINNEN VAN DE WEEK` 8 句逐字比对正文——8/8 逐字出现在正文与 `.text.md` 中；页码标注 (Pagina 1/1/2/3/4/5/6/6) 逐条核对与句子实际所在页一致；英文译文 8 条逐条核对无误。
4. **禁词/红线**：印刷 PDF 文字层扫描：Oekraïne/Ukraine/oorlog/Trump/Amerika/Poetin/Rusland/Gaza/Israël/SOP/cover/lint/TODO/placeholder/Lorem/FIXME/XXX/W47/W46 均为 0；"NAVO" 仅为 P1 横幅 `VANAVOND IN BERLIJN!` 内子串假阳性（与 proof2 同案）；印刷文字层 CJK 字符 0。text.md 唯一的 "W47" 命中是文件首行标题 `# De Lucerna · Dutch Weekly VOL.4 · 2026-W47`（导出元数据行，非版面内容；印刷文字层无 W47）。无国际政治；目标国国内政治仅体现为体育赛事（Nations League，红线允许）。
5. **VOL 与头条**：VOL.4（印刷文字层 ×10：每页页脚 + P1 刊头区 2 处）；VOL.5 ×5（与 core 一致）。头条 `Vanavond in Berlijn: Oranje tegen Duitsland` 去空白 38 字符 ≤ 56。ABSTRACT.txt 为英语单行 271 字节，无 ASCII 双引号，含刊名/目标语/A2–B2/150 题，事实取自本期。
6. **翻译层专项**：
   - 讲解/界面语言全为英文（刊头、栏目条、Note 框、题干说明、P8 答案注文均为英文；荷兰语仅为目标语正文/题面）。
   - 弯引号：U+2018/U+2019/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033 在 `content*.py`、SVG、`.text.md`、双 PDF 文字层中均为 **0**（fix1 D1 仍在位；P7 `Editor's example` 目视直撇号紧贴 s，无断裂；BRIEVEN 框底仍在 ZINNEN 规则线上方）。
   - `«»`（U+00AB/BB，如 P7 `«de groepswinst»`、P8 103 题）为目标语原文引号写法、核心继承，未动，正确。
   - 可见文本 CJK 清单：仅 U+3000（SOP §1.1 强制分隔符）——见观察项 O4（对 proof2 一处表述的纠正，非成品问题）。
7. **事实与日期星期（本轮独立核验，`date` + 公开来源抽查与 proof2 结论逐项对过）**：
   - 全部日期星期用 `date` 核验：1 Nov 2026 周日、11 Nov 周三、13 Nov 周五、14 Nov 周六、15 Nov 周日、16 Nov 周一、21 Nov 周六、22 Nov 周日、24 Nov 周二、29 Nov 周日、5 Dec 周六——与文中全部星期表述一致（含 Q92 "Sint-Maarten was vorige week woensdag" = 11 Nov 周三）。
   - Nations League A2 组、Eredivisie 第 12/13 轮、Sinterklaas intocht（Grave 14 Nov / Amsterdam 15 Nov 第 88 届）、Expeditie Robinson 2026（19 人、34 天、11 月 1 日周日首播）、Heel Nederland Leest 2026（Herman Koch《Het diner》2009）、下期预告（11 月 24 日周二 Real Madrid–PSV、Feyenoord–FC Porto；11 月 29 日周日 Feyenoord–Ajax）——与 proof2 所引公开来源结论一致，本轮未发现反证；未就同一事实重复做全套来源检索（两轮独立核验已覆盖）。
8. **P8 注文人名**：proof2 已逐条核对公开来源（Herman Koch、Merel Westrik、Marieke Moorman、Ozosnel、Nicolette Kluijver / Edson da Graça、Camille Vanuxem、Wim van Rossem、Aaron Burden、Cristina Gottardi、Elise Iovenko），本轮复核拼写全部正确、与正文引用一致；未发现反证。P3 照片署名 "W. Punt / Anefo" 沿用 proof2 观察项 O3（核心 KIT 记载经 Commons API 核验，本轮未独立再验）。
9. **版面目视**：P1–P8 逐版目视——P1 副标题/数字框/P6 图表头/P2 `ZO ONTHOUD JE HET` 框、P7 BRIEVEN 框（底边在 ZINNEN 规则线上方）均无溢出/重叠/压线；P8 练习 113–150 连续、答案 1–150 齐全；P8 答案区实测最小字号 10.12pt ≥ 9.75pt（中位数 10.12pt，187 spans）；照片 7 张 + P6 图表均带出处/授权标注；§1.1 调色板：家具无金色，描边矩形 0。
10. **网页 PDF**：P8 目视与印刷版一致；文字层与印刷版逐字节相同（`pdftotext` 印=网=45,438 B）；逐页 token 数一致（790/828/738/735/807/748/915/2323），位置差分 0、多重集差分 0；网页 PDF 1,610,562 B < 7 MB。
11. **P1 栏断句核查**：P1 第 1 栏末 "…aan de Maas in" 在第 2 栏顶以 "Noord-Brabant: rond 12:00 uur…" 续接，非截断句（`.text.md` 第 9 行全文一致）。
12. **KIT 一致性**：`WEEKLY-KIT.md` §11（Fix round 1）所记 build 11 三 SHA、改动范围（仅 `content8.py:85` 两处 + 5 个重建输出 + KIT §11）、门禁汇总与本轮自跑结果一致；§6 仍记 build-10 SHA（fix1 按任务要求只追加一节，以 §11 新 SHA 为准，属记录约定非成品问题）。
13. **P8 VUL 标题**：按任务裁决规则，STRADDLE 仅当字形被裁 / 墨水重叠 / 与备份旧版不同时为缺陷；本轮未测出与旧版不同的新回归，维持观察项（见 O6），不重判为缺陷。
14. **「next Sunday」**：本版与 core-nl 源码中均无该字符串（grep 0），无可裁决项；按任务规则，冻结核心永不是缺陷。

## 观察项（不计缺陷）

- **O1（沿用 proof2 O1）**：P3 阿姆斯特丹 intocht："de boot vertrok om 10:15 uur bij De Omval"；组织方时刻表记 10:15 为到达 De Omval 的时间（另有来源记首见约 10:20），各家对 10:15/10:30 表述不一且组织方自称 "richttijden"。属 KIT §8 已登记的核心核验债范畴，不作新缺陷。
- **O2（沿用 proof2 O2）**：范文 "81 words" 按空白切分计得 81 词（含独立短横 "–" 一词）；不计短横为 80 词，仍在 80–100 档内。计数口径差异，非成品问题。
- **O3（沿用 proof2 O3）**：P3 照片署名 "W. Punt / Anefo" 未独立再验（核心 KIT 记载经 Commons API 核验；Wim van Rossem 已由 proof2 独立证实为真实 Anefo 摄影师）。无反证，列此备查。
- **O4（本轮纠正 proof2 表述，非成品问题）**：proof2 称 ".text.md 的 CJK 仅 `答案`×150"；本轮独立 census：text.md 中 `答案` 二字出现 **0** 次，可见 CJK 字符仅为 U+3000（标题分隔符）与全角括号 （）——后者是答案注文 `（...）` 的既定分隔符（核心继承）。无汉字、无 CJK 标点外字符。属前轮记录口径有误，成品无问题。
- **O5（本轮新观察，非缺陷）**：P3 B 组词盒 "vestingstad · ontvangen · sleutel · editie · leeskring" 在栏间自然换行——第 1 栏底 "vestingstad · ontvangen · sleutel ·"，第 2 栏顶续 "editie · leeskring"。五词齐全、无重叠、无截断（occlusion 0 flags），为正常多栏流排，非溢出。
- **O6（沿用，五次独立确认）**：P8 VUL 标题越过无边框 cream 框右缘为观察项（非缺陷）；本轮未测出与旧版不同的新回归，不重判。
- **O7（已裁定误报）**：`freeze.py diff --strict-cjk` RC=1——新增 CJK 15 个，全为 U+3000（p1 +1、p2–p8 各 +2）；全版可见文本 CJK 清单仅 U+3000，零汉字、零 CJK 标点。U+3000 为 SOP §1.1 强制分隔符，core 每版亦有；strict 规则限定 zh/ja 版，本版为 en 读者版，不适用。与 build 10 同案。
- **O8**：text.md 首行标题含 "2026-W47"（导出元数据行）；印刷文字层 W47 = 0。非成品问题。

## 机械门结果（自跑，tools/venv 解释器；详见 `GATE-LOG.md`）

| 门 | 结果 |
|---|---|
| SHA 身份核验（三件） | 逐字节一致（见上表） |
| gates.py 9/9 | ALL PASS（occlusion 0；p8 extract 150/150；p8 compare CLEAN keydiff [137,138]；freeze repro 8/8；print/web posdiff 0 msdiff 0；pdftotext 45,438 B；P8 字号 min 10.12pt；chips = core {A2:8, B1:24, B2:3}；§1.1 clean） |
| freeze baseline（core-nl） | 8/8 SVGs byte-identical，rc=0；shipped core SVGs 复核无变化 |
| freeze diff（core vs edition） | rc=0；逐页增减字符串均为讲解层 churn；新增 CJK 15，全 U+3000（O7） |
| freeze diff `--strict-cjk` | RC=1，已裁定误报（O7） |
| occlusion（edition svg/） | 0 flags，rc=0（自检阳性对照全过） |
| occlusion `--core core-nl/svg` | 0 flags；NEW vs core: 0 |
| p8 extract / compare | 150/150；CLEAN，keydiff [137, 138]（合法重定向） |
| D12 回归 | 源码/SVG/text.md 三源带空格；`=` 缺空格全版 0；P8 卡片双重度量 + 交付 PDF 像素复核均在栏内（142 余 +210.0px、144 余 +267.0px） |
| P8 字号 | 最小 10.12pt ≥ 9.75pt |
| VOL 核对 | `tables.py vol 2026-W47` = 4；印刷文字层 VOL.4 ×10、VOL.5 ×5 |
| 徽章计数 | A2 46 / B1 73 / B2 31，与 KIT 一致 |
| §1.1 SVG 审计 | off-palette {}，无金，描边矩形 0，VOL.5=5=core，纸色填充 8 |

## 结论

**(a) 零问题。本轮全量复校零缺陷，可以定稿。**

D12 已修对并经三源 + 双重卡片度量 + 交付 PDF 像素复核证实；其余内容未动（变更范围与 KIT §11 一致）；全部机械门通过（仅 strict-CJK 为已裁定的 U+3000 误报，与 build 10 同案）；核心事实经核验无误。
