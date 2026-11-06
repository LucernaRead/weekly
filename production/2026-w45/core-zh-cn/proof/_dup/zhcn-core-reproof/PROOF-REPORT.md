# 独立复校报告 — Lucerna Weekly W45 简体中文核心 VOL.2（修复后从头全量复校，SOP §8.4）

**结论：ZERO PROBLEMS，可定稿。**

待校版本：`files/weekly-report-w45-zhcn-core/`（8 SVG + 8 卡 1950×2700 + print PDF 44,361,569 字节 + web PDF 3,141,620 字节，均为 pdfinfo 实测 8 页）。
本复校只读源码与成稿，未改任何源码，未派生下级代理，未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git。
证据目录：`hidden_files/w45/zhcn-core-reproof/`（本文件、逐页提取文本 p1–p8.txt、occlusion-audit.txt、selftest.txt、p8-extract.txt/.json、checks.txt、levels.txt、images-md5.txt、baseline-scan.txt、p8-rule-crop.png、p1-quizrow-crop.png、p4-feature-crop.png、p4-fix-crop.png）。

## 0. 首轮唯一问题（Q55 支撑缺失）—— 已修复，从头验证成立

- 源码改动点实测：`hidden_files/weekly-report-w45-zhcn-build/content34.py:124` 唯一一行含 “TES一度落后”，全文 grep “TES打赢了G2”（旧裸句）已无命中；修复员所称“唯一改动”与源码一致。
- 纸面链条（仅凭本期纸面可推出）：
  - P4 正文（y=826.98–902.98 三行，目视裁剪 p4-fix-crop.png 干净无重叠）：“IG打赢了HLE，TES一度落后，后来翻盘打赢了G2”；
  - P4 B 组题干 Q55：“TES打赢G2，是一场___。”；
  - P8 key 55：翻盘，附注 “TES turned the game against G2 around”（p8-ceyan.txt:218）；
  - P4 词语框亦有 “翻盘 fānpán — a comeback win, turning a game around” 作词义支撑。
  - 链条完整：落后→翻盘→胜，填空者无需外部知识即可推出 翻盘。
- P4 其余文本未变：与首轮提取文本 diff，仅目标段落重排（4 行→5 行，+9 字 “一度落后，后来翻盘”）；P1/P2/P3/P5/P6/P7/P8 提取文本与首轮逐字 identical。原始 `<text>` 节点数 P4 为 138，与 KIT 所称 137→138 一致（本报告 txt 行数 137 系空节点剥离口径差，非纸面差）。
- P8 键未动：新旧 p8-extract.json 的 keys 全等（diff {}），key 55 仍为 翻盘；P8 提取文本与首轮 identical。

## 1. 几何审计与 P8 压线

- `tools/occlusion_audit.py --selftest`：OK（6 类 planted 全部触发，clean 对照静默，见 selftest.txt）。
- 对最终 SVG 全量审计：**0 flags**（见 occlusion-audit.txt）。
- 同基线墨迹碰撞：自写估算扫描（CJK 1.0em / 拉丁 0.55em）报 5 处跨栏同 y 配对，经逐项核查与卡片目视（p1-quizrow-crop.png：Q7–Q10 行各栏间有明确空隙）均为估算器高估，与首轮复校的裁定一致；规范审计 0 flags 为准，真实碰撞 0。
- Kinsoku：逐节点行首扫描（，。；：？！、）》」』·）0 命中。
- P8 规则线：SVG `<line y1=1264>`；题流末行基线实测 y=1232.7（“凉。”），净空 31.3 px，下一文本 y=1302.0；裁剪图 p8-rule-crop.png 显示规则线上下干净，无压线。

## 2. P8 答案键 150/150 与分级分页

- `tools/p8.py extract --p8 …/p8-ceyan.svg --total 150`：noted set = **150/150**，编号连续，— Page N — 表头 1–8 齐全。
- 芯片逐页统计：P1 A2 10；P2 A2 15/B1 3；P3 A2 15/B1 3；P4 B1 18；P5 A2 1/B1 17；P6 B2 18；P7 A2 4/B1 4/B2 4；P8 A2 11/B1 24/B2 3。合计 **A2 56 / B1 69 / B2 25**，分页 **10/18/18/18/18/18/12/38**，与 KIT 完全一致（配对组以范围节点计入，单号芯片 130 + 4 组×4 = 150，无缺重）。
- 写作范文《我的立冬周末》拼接实测 **172 字**（无空格含标点），在 120–180 内，与 KIT/P8 标注 “172-character model” 一致。

## 3. P7 金句

8 条在全文拼接计数中各恰 **2 次**（正文 + P7），页码标签全部正确：「不用等11月11日」p.1；「下单就能发货」p.2；「先看结算页，再付款」p.2；「水开始结冰」p.3；「三场都输了」p.4；「小局一场没赢」p.4；「故事够不够好」p.5；「别以后，就现在」p.5。

## 4. 事实 / 日期 / 星期（date -d，Asia/Shanghai）

- 星期全部正确：2026-11-02 周一、11-07 周六、11-08 周日、11-10 周二、11-11 周三、11-15 周日、10-29 周四、10-30 周五、10-31 周六、10-27 周二。
- 双 11：纸面时间表与 KIT 口径一致（京东现货 10-12 20:00、淘天预售 10-15 20:00、尾款+现货 10-20 20:00、现货至 11-13；峰值 11-10 20:00 仅作下周事件；11-11 从未写成已发生或到货）。
- 立冬 17:52：无须改动。首轮校对已独立证实日本国立天文台 18:52 JST = 北京时间 17:52；本期纸面内部一致（P3 正文 “17点52分交节”、P3 日历 “11月7日 17:52”、Q41 键 52）。
- S16：P4 明确印 “本期截稿时是10月27日，第四轮还没有打” 及英文 “Standings as of Oct 27, 2026”，QF 对阵未知声明诚实；全文无截稿后赛果；决赛北京时间 11-15 03:00（纽约 11-14）与纸面一致。
- 影片：P5 纸面《三星堆：未来往事》100 分钟、截至 10-26 中午猫眼约 119.2 万元（24、25 日场均 2 人次口径在题干/键中一致）；《我们仅有一次的人生》11-07 上映、114 分钟、原名/奖项/slogan 齐全；未印冲突的首日票房口径。
- 记者节 11-08：仅日历 + 语言角度，无媒体管理/观点引导内容。

## 5. 红线

全文检索 战争/地缘/外交/政治/选举/民调/周年/长征/桥接 均为 0；“The Lucerna”“Le Lucerna”均为 0；“Lucerna”23 次；无国际政治、无中国国内政治、无周年纪念主打。

## 6. W43 承诺处置

- 立冬 11-07 作主打：P1 头条 + P3 专版 + P7 词条 ✓。
- S16 仅报至 10-27 截止 + VOL.3 预告完整报道 ✓。
- 双 11 仅 buildup + VOL.3 预告 “包裹到了吗？”（下期提问，非已到货报道）✓。
- 读者角：P7 明确标注 “编辑部示例信，不是真实来信” + 中英双语延期披露（“延期不是取消 / Deferred, not cancelled”，说明 VOL.1 预告内容、至今无真实来信、无可刊登投稿、继续征集）；无编造人名、署名或引言 ✓。
- VOL.3 预告（P7）：“双11当天11月11日星期三，包裹到了吗？S16淘汰赛打完了，谁进了决赛？总决赛北京时间11月15日凌晨3点。还有你们的来信和第8版最佳作文。”星期与时间均与 §4 核实一致。

## 7. 图片

- `<image>` 计数 P1 1 / P2 1 / P3 2 / P4 1 / P5 1 / P6–P8 0，共 6 张，与 KIT 一致。
- 嵌入 payload MD5 与构建 assets 逐一匹配：locker 420c6150…、valley 550e463b…、frost d0b015bc…、dumplings e8d75277…、lanparty 6b8e9037…、popcorn a903e35f…（全长见 images-md5.txt）。
- 纸面署名与 CREDITS.md（Commons API Artist 字段）一致：Map hobby、Paul Gilmore、Gerda Arendt、Syced（×2：饺子、LAN 派对）、Based5290；资料图均标 资料图，P4 注明 2003 法国，未冒充本周事件；全部 CC0/公有领域。

## 8. P6 图表与篮子算术

- SVG rects 实测：x=325 起，宽 **810 / 537 / 480 px**，即 3.0 px/元自零起，对应 270 / 179 / 160 元。
- 纸面算术：A 240+80−50=270；B 199−20=179；C 120+40=160（无降）；图表注 “Practice data only — not real shop prices” 与正文 “练习数字” 口径一致。

## 9. 简体纯洁性（独立复查）

宽表繁体独用字扫描（麼魚龍龜鳳學讓說話體邊還這們為無與興舉髮復乾係裏麵頭長門問開關東絲紅後語聽豐萬幹雲幾餘隻）命中 0；魚 0 次，鱼 恰 2 次（均为 “鸡鸭鱼肉” 中的简体 鱼）。

## 10. ABSTRACT.txt 与 KIT 一致性

- ABSTRACT.txt：英文单行（444 字节，唯一换行符为行尾）、无 ASCII 双引号；含真实主题关键词（Double 11 spot sales、Start of Winter Nov 7、S16 quarter-finals、AI film Sanxingdui、winter film We Only Have One Life）+ 学习者检索短语（learn Chinese by reading real Chinese news、A2 to B2 exercises、150 questions）。
- KIT 与纸面一致：题数/分级/分页、金句、图片清单与署名、来源口径、W43 承诺处置、PDF 页数与字节数——磁盘实测 print **44,361,569** 字节 / 8 页、web **3,141,620** 字节 / 8 页，与 KIT 所载完全一致；8 卡均为 1950×2700；P1 配对徽章 “简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers” 在版。
- 可见字符数口径说明（非问题）：按 `<text>` 节点解码后拼接实测 22,990（无空格）/ 26,717（含空格），KIT 所载 23,038 / 26,765 恰为原始实体计数（12 处 `&amp;` 按 5 字而非 1 字计，+48）；修复前后差值恰为 +9，与本次改动完全吻合。故 KIT 数字在其实测口径下可复现，不构成纸面/KIT 不一致。
- 观察项（非阻断，沿用首轮备注）：KIT 的 P8 几何备注数字（“题流末 y=1262 / bottom 1252”）与原始文本基线（1232.7）口径不同，其实质结论（干净、无压线）已由 SVG 坐标与裁剪图证实为真；建议 KIT 注明测量口径，不改纸。

## 未做事项（按任务限定）

未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git；构建源码只读（仅 grep/读取），未派生下级代理。
