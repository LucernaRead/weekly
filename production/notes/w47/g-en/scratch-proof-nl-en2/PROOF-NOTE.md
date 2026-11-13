# W47 nl-en 第二轮独立校对笔记（proof2，全量）

- 版：`2026-w47-nl-en`（荷兰语目标语 × 英语读者），VOL.4，刊期 2026-11-16–2026-11-22
- 校对员：第二轮独立复校（与 builder / fix1 / proof1 不同人；proof1 笔记与 fix1 记录只作参考，全部结论自己重核）
- 日期：2026-11-11
- 对象：印刷 PDF `De-Lucerna-VOL4-nl-en.pdf` + 网页 PDF `De-Lucerna-VOL4-nl-en-web.pdf` + `2026-w47-nl-en.text.md`
- 工作目录：`~/workspace/weekly-git`（只读本版目录；未碰 core-nl、其他家庭、tools/、issues/；未跑 insert.py / lint --write；无任何 git 写操作）
- 渲染：全部 8 版均从印刷 PDF 用 `pdftoppm -r 100` 重新渲染后目视（`render/p-*.png`），不采信 builder 的图；网页 P1/P8 从网页 PDF 同法渲染目视（`render/w1-1.png`、`render/w8-8.png`）
- 探针：开工前 `git hash-object -w` 小文件成功（`da0c4eb8…`）；在 `hidden_files/w47/` 真实写文件成功（`probe-nl-en2.txt`）；无 EDQUOT/EPERM。

## 身份核验（先核身份，通过）

| 文件 | 字节 | SHA-256（实测） | 与任务登记 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷，build 8） | 12,665,899 | `2cc431f2572abad8790d1b99d6211d3aa87a5278a4052f3f0810dd6d764b0b58` | 逐字一致 |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页，build 8） | 1,574,228 | `0fc6232bbe2bd8d3794169d83b4c233df519845f07eef1f9f35e2fdada2f6d18` | 逐字一致 |
| `2026-w47-nl-en.text.md` | 45,074 | `1d69f5edc43e217bfa5d9e032d3c8c6666460a37ee163d0f0db18b1bebeba45b` | 逐字一致 |

身份相符后才开始复校。VOL 经 `tools/tables.py vol 2026-W47` 核实 = 4。

## 缺陷清单

**无。** 本轮为零问题（见下全部核实项）。

## 回归核查（fix1 两处，逐项重核，均改对）

1. **D1（P7 BRIEVEN 框 `Editor's example`）**：U+2019 在 `content*.py`、`svg/*.svg`、`.text.md`、双 PDF 文字层中均为 **0**；另扫 U+2018/U+201C/U+201D/U+201A/U+201E/U+2032/U+2033 在上述全部位置均为 **0**。放大裁图（`render/p7-editors-crop2.png`，按 PDF 文字层 bbox 定位）：`Editor's example, not a real letter. Send yours — we print them in VOL.5!` 直撇号紧贴 s，无 "Editor' s" 断裂；BRIEVEN 框底仍在 ZINNEN 规则线上方。改对。
2. **同类残留（P1 本周一词 `"Group win"`）**：放大裁图（`render/p1-groupwin-crop3.png`，按 PDF 文字层 bbox 定位）：`"Group win": first place in the group, straight to the quarter-finals.` 直双引号紧贴，冒号前无宽空隙。改对。
3. `«»`（U+00AB/BB，如 P7 `«de groepswinst»`、P8 103 题）为目标语原文引号写法、核心继承，未动，正确。

## 全量复校核实项

1. **150 题全量验算**：逐页题数 10/18/18/18/18/18/12/38（P1 1–10，P2 11–28，P3 29–46，P4 47–64，P5 65–82，P6 83–100，P7 101–112，P8 113–150）；级别 A2 46 / B1 73 / B2 31（`.text.md` 标记独立重数：单题标记 A2 43/B1 73/B2 28，另 D 组 25–28 共用一枚 A2 标记、F 组 141–144 共用一枚 B2 标记，合计 46/73/31，与 KIT 一致）。P8 答案 150/150 齐全（`p8.py extract`），`compare` vs core **CLEAN**，keydiff [137, 138]（见下）。全部答案逐题对照题面/正文/图表复核：完成时助动词 39–42、图表算术 83–87（35/30/65/15/100，35+30+20+15=100）、日期算术 22/43/44/45/46（19 天/1 天/4 小时/19 天/17 年）、判断题 61–64/80–82、gaan 将来时 76–79（gaat/gaan 人称一致）、过去时 57–60/105–107 均与正文一致。范文空白切分 81 词（含独立短横 "–" 为一 token；不计短横为 80 词，仍在 80–100 档内，与 P8 注 "81 words" 一致，见观察项 O2）。
2. **keydiff 137/138 已裁定合法**：核心 P8 的 137/138 答案键为中文（"圣诞老人新闻每天 18:00 播出。/ 前两名晋级四分之一决赛。"），en 版为英文（"The Sinterklaas news is on every day at 18:00." / "The top two go through to the quarter-finals."）——翻译题按读者语重定向，方向正确（137/138 为荷→英；139/140 为英→荷，答案键为荷兰语）。符合工具说明"key diffs are informational"。
3. **金句 8 条**：P7 `ZINNEN VAN DE WEEK` 8 句逐字比对正文——8/8 逐字出现在正文与 `.text.md` 中；页码标注 (Pagina 1/1/2/3/4/5/6/6) 逐条核对与句子实际所在页一致；英文译文 8 条逐条核对无误。
4. **禁词/红线**：印刷全文扫描：Oekraïne/Ukraine/oorlog/Trump/Amerika/Poetin/Rusland/Gaza/Israël/SOP/cover/lint/TODO/placeholder/Lorem/FIXME/XXX/W47/W46 均为 0；"NAVO" 命中 1 次是 P1 横幅 `VANAVOND IN BERLIJN!` 内子串假阳性。无国际政治；目标国国内政治仅体现为体育赛事（Nations League，红线允许）。
5. **VOL 与头条**：VOL.4（印刷文字层 ×10：每页页脚 + P1 刊头区 2 处）；VOL.5 ×5（P2 读者园地承诺、P7 BRIEVEN 框 ×2、P7 下期预告 ×1、P8 113–150 答案区？实测共 5 处，与核心一致）。头条 `Vanavond in Berlijn: Oranje tegen Duitsland` 去空白 38 字符 ≤ 56。ABSTRACT.txt 为英语单行 271 字节，无 ASCII 双引号，含刊名/目标语/A2–B2/150 题，事实取自本期。
6. **翻译层专项**：
   - 讲解/界面语言全为英文（刊头、栏目条、Note 框、题干说明、P8 答案注文均为英文；荷兰语仅为目标语正文/题面）。
   - 印刷 PDF 文字层 CJK 字符 0；`.text.md` 的 CJK 仅 `答案`×150；SVG 的 CJK 仅 P1 moth 标记 `<title>Lucerna 三色蛾</title>` 内 3 字（核心继承、不可见，见 proof1 O4，本轮重核同状）。
7. **事实与日期星期（公开来源抽查，本轮独立核验）**：
   - 全部日期星期用 `date` 核验：1 Nov 2026 周日、13 Nov 周五、14 Nov 周六、15 Nov 周日、16 Nov 周一、21 Nov 周六、22 Nov 周日、5 Dec 周六、24 Nov 周二、29 Nov 周日——与文中全部星期表述一致。
   - Nations League A2 组：荷兰 8 分（7:5）、希腊 8 分、德国 5 分、塞尔维亚 0 分；荷兰四场 1–1 德国（主）、2–1 塞尔维亚（客）、2–2 希腊（客）、2–1 塞尔维亚（主）；德国 0–1 负希腊（主）、2–0 胜塞尔维亚、0–0 平希腊（客）；11 月 13 日周五 荷兰–希腊（阿姆斯特丹 Johan Cruijff ArenA，20:45）+ 塞尔维亚–德国（贝尔格莱德）；11 月 16 日周一 德国–荷兰（柏林 Olympiastadion，20:45）——与 DFB 官网、sportradar、NOS 转述（archynewsy/nogomania）一致；"top two to quarter-finals in March" 一致。
   - Eredivisie 第 12 轮：Heerenveen–Feyenoord 5–3、Twente–Ajax 2–2、Cambuur–PSV 2–5；PSV 12 轮 26 分榜首（Feyenoord/Ajax 25，Twente 24）——与 1908.nl / soccernews / FR12 / KNVB 赛程一致；第 13 轮 NEC–PSV 周六 16:30、Feyenoord–Excelsior 周六 18:45、Twente–Willem II 周日 12:15、Ajax–ADO 周日 14:30——与 KNVB 官方赛程（competitieprogramma najaar）一致。
   - Sinterklaas：全国 intocht 2026 年 11 月 14 日周六 Grave（Maaskade 约 12:00 靠岸，节目 12:00–16:00，NPO Zapp/NPO 3 直播）；阿姆斯特丹 11 月 15 日周日第 88 届（De Omval 10:15、Scheepvaartmuseum 11:30、Stopera 13:00 起步、经 Rembrandtplein/Utrechtsestraat 至 Leidseplein）——与组织方时刻表（sintinamsterdam.nl 转述）及多家媒体一致；"10:15 出发/到达" 的措辞见观察项 O1。
   - Expeditie Robinson 2026：19 名选手（10 荷 + 9 弗拉芒）、马来西亚（兰卡威）、34 天、11 月 1 日周日 20:00 RTL 4 首播、Nicolette Kluijver + Edson da Graça 主持、Camille Vanuxem 任记者——与 nl/en 维基及多家荷兰媒体一致。
   - Heel Nederland Leest 2026：书为 Herman Koch《Het diner》（2009），11 月全月图书馆免费取（无需会员，含大字本/Makkelijk Lezen/电子书/有声书）——与 CPNB 及多家图书馆来源一致。
   - 下期预告（P7 VOLGENDE WEEK）：11 月 24 日周二 Real Madrid–PSV、Feyenoord–FC Porto（欧冠第 5 轮），11 月 29 日周日 Feyenoord–Ajax 14:30（De Klassieker）——与 UEFA.com 及 KNVB 赛程一致。
8. **P8 注文人名逐条核对（公开来源）**：Herman Koch（《Het diner》2009，Heel Nederland Leest 2026 campaign book，CPNB/维基证实）、Merel Westrik（Sinterklaasjournaal/intocht 主持，NTR 通稿与多家媒体证实）、Marieke Moorman（Land van Cuijk 市长、在 Grave 迎接 Sinterklaas，多家来源证实）、Ozosnel（Sinterklaas 的马，多家 intocht 报道证实）、Nicolette Kluijver / Edson da Graça（Expeditie Robinson 2026 主持）、Camille Vanuxem（弗拉芒记者，2026 年新加入）、Daan（P8 阅读短文虚构人物，非真人）、Wim van Rossem（Anefo 摄影师 1929–2000，Wikimedia Commons Creator 页与多张 Anefo 底片署名证实）、Aaron Burden / Cristina Gottardi（Unsplash 照片署名，核心 KIT 引 exact Commons 文件名）、Elise Iovenko（Unsplash 摄影师名存在；核心 KIT 引 exact Commons 文件 `Nagtabon Beach, Puerto Princesa (Unsplash).jpg`；照片本身为示意性热带海湾，图注写 "net als" 非断言为马来西亚实景）。拼写全部正确。W. Punt（P3 Anefo 署名）为核心 KIT 记载、经 Commons API 核验，本轮未独立再验（见观察项 O3）。
9. **版面目视**：P1–P8 逐版目视——P1 副标题/数字框/P6 图表头/P2 `ZO ONTHOUD JE HET` 框、P7 BRIEVEN 框（底边在 ZINNEN 规则线上方）均无溢出/重叠/压线；P8 练习 113–150 连续、答案 1–150 齐全；P8 答案区实测最小字号 10.125pt ≥ 9.75pt（中位数 10.35pt）；照片 7 张 + P6 图表均带出处/授权标注；§1.1 调色板：家具无金色，描边矩形 0（见观察项 O5）。
10. **网页 PDF**：P1/P8 目视与印刷版一致；文字层逐页多重集差分 0、token 数逐页一致（见机械门；P1 有 3 处 ≤0.2pt 位置舍入差，内容相同，见观察项 O4）。
11. **P1 栏断句核查**：P1 第 1 栏末 "…aan de Maas in" 在第 2 栏顶以 "Noord-Brabant: rond 12:00 uur…" 续接，非截断句（`.text.md` 第 9 行全文一致）。
12. **KIT 一致性**：`WEEKLY-KIT.md` §6 交付物字节/SHA 为 build 8 实测值；§7 门禁记录与本轮自跑结果一致（含 P7 token 915 的 build 7 笔误纠正说明，fix1 已顺带纠正，属记录笔误非成品问题）。

## 观察项（不计缺陷）

- **O1**：P3 阿姆斯特丹 intocht："de boot vertrok om 10:15 uur bij De Omval"；组织方时刻表记 10:15 为到达 De Omval 的时间（另有来源记首见约 10:20），各家对 10:15/10:30 表述不一且组织方自称 "richttijden"。与 proof1 O3 同一已知 nuance，属 KIT §8 已登记的核心核验债范畴，不作新缺陷。
- **O2**：范文 "81 words" 按空白切分计得 81 词（含独立短横 "–" 一词）；不计短横为 80 词，仍在 80–100 档内。计数口径差异，非成品问题。
- **O3**：P3 照片署名 "W. Punt / Anefo" 未独立再验（核心 KIT 记载经 Commons API 核验；Wim van Rossem 已独立证实为真实 Anefo 摄影师）。无反证，列此备查。P5 "Elise Iovenko / Unsplash" 本轮已补验：该摄影师名在 Unsplash 存在，核心 KIT 引 exact Commons 文件名。
- **O4**：print/web 文字层 P1 有 3 处位置差（`De Lucerna` x 394.0 vs 393.8；`SINTERKLAAS` 884.1 vs 884.2；`PAKJESAVOND` 1109.4 vs 1109.5），均为 ≤0.2pt 字体子集渲染舍入，内容逐字相同、多重集差分 0。非缺陷。
- **O5**：SVG 朴素色值扫描见调色板外颜色 10 个，全部局限于 P1 三色蛾品牌标记（嵌套 SVG：#4F765D/#84A283/#F1E8D4/#4D72B4/#7898CD/#D7B257/#EDD17F/#34483A）与绿底栏副标题淡色 #cac8ba；家具无金色使用。非缺陷。
- **O6**：pdftotext 逐页词数（768/820/722/705/793/740/896/2112）与 KIT 记载（795/830/738/724/807/748/915/2318）计数口径不同（词切分方法差异）；两种方法下 print 与 web 逐页均相等。非成品问题。

## 机械门结果（自跑，tools/venv 解释器）

详见 `GATE-LOG.md`。结论：**全部通过**。

| 门 | 结果 |
|---|---|
| occlusion（`tools/occlusion_audit.py svg/`） | 0 flags，rc=0（自检阳性对照全过） |
| p8 extract（`p8.py extract --total 150`） | 150/150，rc=0 |
| p8 compare vs core（`p8.py compare --total 150`） | CLEAN，0 missing/extra，keydiff [137, 138]（已裁定合法，见上） |
| freeze（`freeze.py baseline`，同一解释器重跑构建比对） | 8/8 SVGs byte-identical，rc=0；shipped SVGs 完整性复核无变化 |
| print/web 文字层（PyMuPDF 位置排序） | 8 页 multiset diff 0；token 数逐页一致（218/203/189/184/196/201/188/386）；P1 仅 3 处 ≤0.2pt 位置舍入（O4） |
| pdftotext 非空 | print 45,404 B / web 45,409 B；web PDF 1,574,228 B = 1.50 MB < 7 MB |
| P8 答案字号 | 最小 10.125pt，中位数 10.35pt（≥ 9.75pt） |
| VOL 核对 | `tables.py vol 2026-W47` = 4；印刷文字层 VOL.4 ×10、VOL.5 ×5 |
| 徽章计数 | A2 46 / B1 73 / B2 31，与 KIT 一致 |
| §1.1 SVG 审计 | 家具无金色，描边矩形 0；调色板外色值仅限蛾标与绿底副标题淡色（O5） |

## 结论

**(a) 零问题。本轮全量复校零缺陷，可以定稿。**

fix1 的两处改动（P7 `Editor's`、P1 `"Group win"`）均已改对并经放大裁图核实；其余内容未动；全部机械门通过；核心事实经公开来源抽查无误。
