# PROOF-NOTE — W47 德语家 round-4 独立重校

- **任务**：W47 德语家 11 版全新一轮完整重校（SOP §8.4：修后由不同人从头全量复校）
- **重校员**：round-4b（恢复协调员 #6 派单，只读，未做任何修复/提交/推送）
- **日期**：2026-11-13（EST）
- **范围**：`~/workspace/weekly-git/production/2026-w47/` — core-de + 2026-w47-de-en/es/fr/it/ja/ko/nl/pt/ru/zh-tw
- **SOP**：`~/workspace/weekly-git/SOP.md` 全文已读（§8 校对循环、§1.1 版式、附录 1–5）
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-de-round4b/`
- **生产 HEAD**：`b06cb15e80dc46269f52cbf963aa93f3a5f88fa0`（2026-11-12 17:13 UTC）；生产自 round-3 修复后未变（见 SHA 表：core-de / de-fr / de-ko / de-ru 与 round-3 修复后 SHA 一致）
- **磁盘**：开始 97G，门禁期间 98G，结束 98G（`df -h`；停手线 100G，未触及）

## 结论：(a) CLEAN — 零问题

11 版全部通过：通读、150 题逐题复核、事实/日期/算术重验、8 页逐页目视、全部机械门禁。无缺陷。以下回归项全部成立；观察项均为 round-2/3 已接受或已记录的非缺陷（见 §6）。

## 1. 磁盘实测 SHA 表（2026-11-13 从磁盘重算，完整 sha256）

| 版 | 印 PDF (Die-Lucerna-VOL4-de*.pdf) | 网 PDF (*-web.pdf) | .text.md |
|---|---|---|---|
| core-de | `db33da70620c0ae2ca5e0712d310ae0466711646be0b881d9eeac60c6d8311d3` (11,776,953 B) | `2d555df1209c10eeb54315f7ffda47bc787a763a8874b711116c5d18ac587eab` (1,861,111 B) | `a99c19716142773bbb25271cf5c18f724b4a7b722dd5dd6ba3800c3d8d7972c0` (49,839 B) |
| de-en | `aaaad1ed122ad23442e77e57615e9d823326f0111745afdc3fdeecba3ef61f91` (10,350,173 B) | `6e50a693d200fbb2beef36254b9f57266a325d9252fe6af5d315515e27b98f04` (1,510,219 B) | `6fb1fb37415bf055d52162bb9c213b271c08dba02f13256524cb3b87d78f2418` (49,975 B) |
| de-es | `07f87aa040311a5ed8da0fc636b339f5f60b6ab6d4c600dd85918bc51ea0d257` (10,354,441 B) | `8e27d9c5f9353327de68d70e06a45bd192662246d85080ecd0747d425203e6a8` (1,514,482 B) | `ec37787fa1d5d9ec56d962bf10e0b864227799c5908c3df4dd98fc2e2d599369` (50,467 B) |
| de-fr | `4f6ccacfb20eaa7cddae91b8041761e2183e551287c83eb31e5385cfa744d38f` (10,352,491 B) | `22525742a6bbfdc13ab0bb8df86aabd2e3f4b9d5a3f49e682cfef930f029a0d3` (1,512,524 B) | `80f1a96deb470d0cb3c798df7602bcfb36919d1292fd7b4f6c24495ccae9fbf8` (50,392 B) |
| de-it | `e01bc56325c4b8343f6ac9f5fd67b1ca7f709c0da5be052e1eb9150ec1da3e85` (10,348,832 B) | `87c448ebbc7923ccc4d4b873436dffa6e78b4350ac0de05d48336c3006621d99` (1,508,883 B) | `96babe5753bf972378eed6ed6ae8b195b2164720106d608fbe4206e55c21f2cb` (50,058 B) |
| de-ja | `60942dc9dd9ff8da645b761bde07c4031db866dc5dde5537c01a4be780620a8b` (16,798,018 B) | `579e4a2ac75ac8e57ea25f0db72ba805eb0af43ef74ba65fdda89edf5ba73d90` (1,949,457 B) | `e32d3cb404865284c94bef09f44bbaf9fa32ae5f883ac8b92bc3dcc2f9aaee23` (52,154 B) |
| de-ko | `013b5d8e255e71728e74152790bf54a99591caa3d32ab1fc490e8e1202be7865` (12,925,712 B) | `ef851f6fa7d626a033b8dad4363272a78e0a4182c466be26b70cc16506ae33cc` (1,789,538 B) | `a8804776b2863a48b4ec09b1864ea074a3ddb7a9d61b39a3273fdcfdb83eb475` (51,730 B) |
| de-nl | `5dd1a9bb6b67690be6c2fa9195c8a23c6acd7e483b9c51f40e0ce080f9c191e9` (10,347,280 B) | `049a48c9145882998f873ea6a121f67c7d4acb15d9041b07784a48a21a5aa8d0` (1,507,320 B) | `7cee007495073fcd5c882f937b2595cf1b8c2dcc247fb21b07bbf39815ddc5f7` (49,770 B) |
| de-pt | `23c1505097e1d8a36fb4126c3479bebff44bd054e04b5bb40f031f7ced00c740` (10,354,731 B) | `bda89b7b21802e0faa789c05aba2215d9ebb4379ec461257790531f7b8fb3589` (1,514,731 B) | `b1b6a7e20abd04a0adfa3d979920919749d3280bd128b9775003e31a330597ca` (50,158 B) |
| de-ru | `4e953850861bd191ebc6ae5bf7a44d2f29493c53080583c4b1d669dda8ebda05` (10,506,857 B) | `38bd5b1a08d12653db85056424447e7f389018234da9ebc90462059f7b66d6c6` (1,654,623 B) | `f768fb76cb70b3914db941a63985f3ec6578fa390e27fb42a9283998e8ca8d45` (56,774 B) |
| de-zh-tw | `8597094b9ad2093862d3e6fe4f5a03b62c62207a3d5fde31853465e184a1398a` (11,835,999 B) | `dd26b2ac11a5cd0ab35b07d6f39b8ac555b84cc0a687bc57d99f959369075122` (1,936,175 B) | `6865f9d835f17082f84bf500fc07211942d01a7c5520c87c298ceac74939ea6b` (49,330 B) |

## 2. 显式回归检查（round-3 修复，逐项独立复核）

### R3-F1 — `überkleben` 孤儿注释：×0，11 版全部通过
- `content56.py`、`text.md`、印 PDF 文本层、网 PDF 文本层四处 grep，11 版全部 0 命中（我方门禁 §8 逐版输出，见 `gates-all4b.log`；另对 core-de 等逐版核对）。
- P5 译注框目视确认：core-de P5 框内为 `der Adventskalender降临节日历 · das Türchen小门 · der Wunschzettel愿望单 · das Christkind 圣婴 · basteln 制作。`，无 überkleben。

### R3-F2 — de-ko `달력를`→`달력을`：全部通过
- 旧形 `달력를`：`content56.py` ×0、text.md ×0、印 PDF 文本层 ×0、网 PDF 文本层 ×0。
- 新形 `달력을`：`content56.py:53,59` 在位；text.md ×2；印 PDF ×2；网 PDF ×2。
- 渲染目视：de-ko P5「UND SIE?」框原文 `대림절 달력을 만드나요? 소원 목록에는 무엇이 있나요? 독일어로 두 문장 써 보세요!`，을 正确。

### P5-only SVG 变化：全部通过
- 各版 SVG 与 round-3 前状态（`scratch-reproof-de-round3/` 每版 `fix-round3/pre-svg-sha.txt`）对比：**11 版均只有 `p5-jugend.svg` 变化**（diff 恰为新旧 hash 两行）。其余 7 页 SVG 字节未变。
- 另：de-fr / de-it / de-ja / de-ko 的 p8 SVG mtime 虽晚于 round-4 renders，但其 SHA 与 round-3 前状态一致（core-de `711effc2da94`、de-fr `73aa24a77ff0`、de-it `d64f36b4211a`、de-ja `b7317b50d97f`、de-ko `32e5f5f5c13b`），属无内容改动的触碰，renders 内容有效。

### de-ru A5 已接受项 + head_check "2 defects" 双记：解释成立，不是新缺陷
- 我方 de-ru 门禁 head_check：**FAIL 1 defect**，唯一一项即 A5：`HEAD TOO WIDE [P8-battery]: D　SÄTZE BAUEN　Предложения`（`gates-run.out` §7，`head RC=1`）。
- A5 本体（HEADS-NOTE，de-ru KIT §7）：`SÄTZE BAUEN` +0.7u（像素）/+1.8u（SVG ink）/+2.9u（PDF span advance），三项均 <3u，无碰撞；已接受，非缺陷。P8 目视确认标题在栏内留有余地。
- round-3 报告的 "2 defects" 与我方 "1 defect" 是**同一项被记两次**：round-3 的 run-build.log 被两次构建 pass 追加写入（重建 pass + 门禁重跑 pass），每 pass 各记一次；我方单次重建只记一次。去重后 distinct 项 = 1 = A5。解释成立，无新缺陷。
- de-ru P1/P7 的 D1–D6 缩短（KIT §7，round-3 已接受）目视确认在位且无溢出：P1 带标题 `DIE BUNDESLIGA IST ZURÜCK — BAYERN–KÖLN!`、数字框 `WOCHE IN ZAHLEN`、目录 `DIESER AUSGABE`；P7 工具箱 `WERKZEUGKASTEN`、读者来信 `LESERBRIEFE`（21pt）、`Ещё слово`。

### de-fr 单空格 artifact（O-R3-3）：未变，不是缺陷
- 印/网字节比对：`PRINT==WEB BYTES: False`，唯一差异为 1 个抽取空格：印 `(früh→\nfrüher` vs 网 `(früh →\nfrüher`，首差异字符 44414，多重集差 −1 空格；与 round-3 记录完全一致。SVG 字节相同，内容无差异。`PRINT==WEB MULTISET: True`。
- 其余 10 版印/网字节完全一致。

## 3. 机械门禁（我方自跑，11/11，日志 `gates-all4b.log` + 各版 `gates-run.out`）

| 版 | verify | p8 compare (150) | occlusion（真实审计） | boxtitle | spill | edge | D5 | freeze | 印=网 多重集/字节 | 重建 SHA 一致 | head_check |
|---|---|---|---|---|---|---|---|---|---|---|---|
| core-de | RC=0, 150 题 | CLEAN, keydiff [] | selftest OK, 0 flags | 0 DEFECT, 1 marginal | 0 SPILL | 0 TOUCH, 0 NEAR | PASS | RC=0 | True / True | SVG+双 PDF 一致 | PASS 0 |
| de-en | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-es | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-fr | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / **False（O-R3-3 单空格）** | 一致 | PASS 0 |
| de-it | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-ja | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT, 1 marginal | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-ko | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-nl | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-pt | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |
| de-ru | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT | 0 | 0 | PASS | RC=0 | True / True | 一致 | **FAIL 1 = 已接受 A5** |
| de-zh-tw | RC=0, 150 | CLEAN, [137,138,139,150] | selftest OK, 0 flags | 0 DEFECT, 1 marginal | 0 | 0 | PASS | RC=0 | True / True | 一致 | PASS 0 |

- **occlusion 为真实审计**：每版先跑 `--selftest`（6 类 planted 缺陷全部触发、干净对照静默），再跑真实审计，0 flags。未以 selftest 代替审计结论。
- **p8 keydiff [137,138,139,150]**（全部 fanout 版共有）：Q137–139 答案为读者母语翻译句（属 fanout 正常差异）、Q150 为开放题标签（`开放题`/`Open task` 等）。合法差异，非缺陷；core-de 自身 keydiff []。
- **verify 细节**（core-de 为例，全版同类）：编号连续 1–150；verify 后 SVG 字节不变；SOP §1.1 版式审计 True，旧版式 hex 0 个。
- **重建**：每版在全新 scratch 目录经 `tools/run_build.py` 重建，SVG 集合相等且字节一致，双 PDF 与生产 SHA 一致。
- **spill**：每版 0 SPILL（OBSERVE 候选 84–165 条，均为 [observe] 级相邻元素，无溢出）。
- **D5 census**：拉丁/西里尔误入 CJK 字体 0，curly 引号误入 CJK 0，noto_sans 元素 0；全部 PASS。

## 4. 通读范围与核对方法

- **core-de text.md 全文通读**（`2026-w47-de-zh-cn.text.md`，1,185 行）：150 题逐题与题干/答案核对——编号连续 1–150；配对题 25–28、52–55、141–144 正确；比较级 Q56–59 正确；算术 Q85（44+33=77）、Q88（44+33+23=100）正确；日期 Q11–15、Perfekt Q16–20、weil/dass/ob Q76–79、93–96、101–112、113–120、对话 Q145–149、翻译 Q137–140 全部正确。
- **10 个 fanout 版读者层全文通读**：core-vs-fanout diff（`diffs/de-<lang>.diff`）+ 读者专有行摘录（`diffs/reader-de-<lang>.txt`，每版约 235 行）逐行核对。全部翻译正确；德语核心除 de-ru 已接受的 D1–D6 外无改动。zh-tw 为独立措辞（例 `將臨期日曆`/`追思主日`，非简转繁；与 core 相同的行如 `例句`、`工具箱` 为共享汉字）。
- **P7「Sätze der Woche」**：8 条引文逐条与本期文章原文核对，出处页码正确（S.1×2、S.2、S.3、S.5、S.4、S.6×2）。
- **Muster 范文词数**：`(84 Wörter)` 标注核实——空白分词计 84（含独立破折号 token；不含则为 83），与 `wc -w` 口径一致，非缺陷。
- **无 U+FFFD**：11 份 `.text.md` + 全部 `content*.py` 扫描为 0。个别 exec 输出中出现的 `���` 为传输/显示 artifact，文件内容经 grep 确认为正确字符。
- **事实重验（2026-11-13 网查）**：拜仁–马竞 2-0（Karl 54'、Laimer 74'）；德甲第 9 轮 30 球/9 场、莱比锡–奥格斯堡 5-2、汉堡–门兴 3-1、拜仁客胜美因茨 2-1、多特–埃尔弗斯贝格 2-1、斯图加特–不莱梅 1-0、弗赖堡–柏林联合 2-0、第 10 轮周五 11 月 20 日拜仁–科隆开幕；欧冠第 4 轮多特–贝蒂斯 2-1、莱比锡–曼城 2-3、加拉塔萨雷–斯图加特 2-0；11 月 5 日欧联/欧协勒沃库森–马赛 0-1、水晶宫–霍芬海姆 1-1、特拉布宗–弗赖堡 0-1；塞尔维亚–德国 11 月 13 日周五 20:45、贝尔格莱德 Rajko Mitić 球场、UEFA 观众禁令（仅 U15 儿童约 5,000 人 + 50 名德国球迷）——正文「vor fast leeren Rängen (UEFA-Strafe: nur Kinder und 50 deutsche Fans)」准确；欧国联 A2 组 4 轮后荷兰 8、希腊 8、德国 5、塞尔维亚 0，「Nur die ersten beiden kommen weiter」正确；电力税居民 2.05 ct/kWh（自 2003 年未变）、Merz 推动全面下调尚未落地、联邦议院最终预算辩论 11 月 24–27 日（正文：预算表决周五 11 月 27 日）正确；科隆圣诞市场 Dom（Roncalliplatz）+ Markt der Engel（Neumarkt）11 月 16 日–12 月 23 日、追思主日 11 月 22 日关闭、Hafenweihnachtsmarkt 自 11 月 13 日、亚琛 11 月 20 日–12 月 23 日正确；Wilhelm Ritter（1860–1948）《Weihnachtsmarkt auf der vorderen Insel Schütt》（1930）正确；Kepler 1903《Im Lande des Christkinds》首版印刷降临节日历（Reichhold & Lang，慕尼黑），24 图剪下 + 24 格贴上——正文修正句「Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben」与史实格式完全吻合；「über 120 Jahre alt」正确（123 年）。
- **日期/星期核验**（`date`，Europe/Berlin）：2026-11-03 周二、04 周三、05 周四、06 周五、07 周六、08 周日、13 周五、16 周一、17 周二、18 周三、19 周四、20 周五、22 周日、24 周二、25 周三、26 周四、27 周五、29 周日、12 月 23 日周三——正文全部星期表述一致。算术：18+11=29、15+7=22、16+6=22；第 9 轮进球 4+3+3+7+4+1+3+2+3=30 ✓；忏悔祈祷日距首个降临主日 11 天 ✓。

## 5. 目视检查（8 页 × 11 版）

- **复用 renders 的时效证明**：先比 mtime（de-fr/it/ja/ko 的 p8 SVG mtime 晚于 renders，但 SHA 证明内容未变，见 §2），再在本人 scratch 重渲染 core-de 全 8 页（`pdftoppm -r 130`，`rerender-core/`），**8/8 与 round-4 renders 逐字节一致**（P1 SHA `7116ff96c608f7ec780d574564360b5fb865b10e59d4e53aeeeb4dba63adecee`）。复用成立。中断工人的目录未删除。
- **core-de P1–P8 全分辨率逐页看完**：干净——无溢出、无重叠、无豆腐、无压页脚；刊头、带标题+黄色 kicker、头条、数字框、Fragen 框、目录、照片+图注/credit、Blitzquiz、P2 文章+侧栏+算术+练习、P3 Ritter 画+图注+练习、P4 赛果表+照片+练习、P5 Kepler 图+题 65–82、P6 投票条 44/33/23 + 题 83–100、P7 三小课+例句+题 101–112+金句+纠错诊所+下期预告、P8 题 113–150 + Muster 范文 + 全部答案，页脚 `第N版／共8版` 正确。
- **10 个 fanout 版联络表**（`visual/sheet-<lang>.png`，每版 8 页 4×2）：全部结构干净，与 core 版式一致，无明显溢出/豆腐/缺图/页脚错误。
- **全分辨率抽查**：de-ru P1（D1–D3 在位，西里尔字母干净）、P7（D4–D6 在位）、P8（A5 `SÄTZE BAUEN` 在栏内留有余地）；de-ko P5（R3-F2 `달력을` 在位）；de-ja P1（日文干净，无豆腐）；de-zh-tw P1（繁体干净，无豆腐）。

## 6. 观察项（非缺陷，沿用 round-2/3 记录）

- **O-R2-1**：P1 数字框 gloss 在 ja/ko/ru/zh-tw 版略去 `20.30` 开球时间；时间仍见于上方德语句，无信息损失。
- **O-R3-4**：P7 工具箱标题贴右框边 +1.0px（字形完整，无裁切）：core-de `工具箱`、de-ja `道具箱`、de-zh-tw `工具箱`（各 1 marginal，`gates/boxtitle/*.json`，over 1.0px、clip false、overlap null）。其余 8 版 0 marginal。
- **de-ru D1–D6**：已接受的版式驱动缩短（KIT §7），意义不变，见 §2。
- **P1 kicker 缩短**：各 fanout 版 P1 kicker 只取 core 前半句（如 `BUNDESLIGA IS BACK`，略去 `国家队决战`），10 版一致的模板选择。
- **P1 过去时表述**：正文「Deutschland traf in Belgrad auf Serbien」用过去时，而比赛为 11 月 13 日周五晚间（生产之后）；未写比分，只写赛前已知的入场条件；本期时间立足点为 11 月 16–22 日当周。round-3 已接受此表述。
- **en 工具箱措辞**：`der Buß- und Bettag = repentance and prayer`，略去 "day of"，余版为 `day of repentance and prayer`；一致性小差异，非错误。
- **P1 无首字下沉**：与已接受的 W46-FR 相同，非缺陷。

## 7. 缺陷清单

无。结论 (a) CLEAN。

## 附：文件索引（本 scratch）

- `PROOF-NOTE.md`（本文件）
- `gates-all4b.log`（11 版门禁总日志，`GATES-ALL4B-DONE`）、`run_gates4.sh`、`gates-all4.sh`、`run_all.sh`
- 各版 `<slug>/gates-run.out`（完整逐版门禁输出）+ `<slug>/gates/`（verify/p8/occlusion/boxtitle/spill/edge/d5/freeze/print-raw/web-raw/head/rebuild 原始产物）
- `diffs/de-<lang>.diff`（core-vs-fanout 全文 diff）+ `diffs/reader-de-<lang>.txt`（读者层摘录）
- `rerender-core/core-r4b-{1..8}.png`（core-de 重渲染，8/8 与 round-4 renders 逐字节一致）
- `visual/sheet-<lang>.png`（10 版联络表）
- 复用（未改动、未删除）：中断工人目录 `../scratch-reproof-de-round4/`（`gates-all4.log`、`diffs/`、`renders/` 90 张 PNG）；round-3 记录 `../scratch-reproof-de-round3/`；`../scratch-fix-xru-heads/HEADS-NOTE.md`。
