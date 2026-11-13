# PROOF-NOTE — 2026-w47-es-zh-tw（proof2，独立重校）

- **版**：`production/2026-w47/2026-w47-es-zh-tw/`（未提交、未推送，与任务一致）
- **校员**：proof2（独立重校，从头完整重校，非仅复核清单）
- **日期**：2026-11-11（America/Toronto）
- **基准**：core-es fix build 10（已独立定稿，(a) 零缺陷）重建版（es re-fanout，10/10，未提交）

## 结论：(a) 定稿，0 缺陷

本轮证明 150/150 合格、全部门禁通过、简体字残留 0、旧版对比无意外变化、8 页目视无缺陷。
proof1 的 5 项缺陷（D1–D5）全部已在重建版修复并逐项复核到位（见 §2）。
只记录、不计入判定：字体（SC 字体声明，见 §7）。

## §1 身份复核（开工前，全部相符）

| 件 | 大小 | SHA-256 | 结果 |
|---|---|---|---|
| 印 `La-Lucerna-VOL4-es-zh-tw.pdf` | 17,263,265 B | `ef5f1cde27036e5c810c4f779fd43e743857ab763c77df9b09bf6d885d804365` | ✓ 与任务一致 |
| 网 `La-Lucerna-VOL4-es-zh-tw-web.pdf` | 1,725,936 B | `5b7d87967332783dd0314d54ab2b8483e7d0036b4bdc8609ae3226f2c5de6500` | ✓ 与任务一致 |
| `2026-w47-es-zh-tw.text.md` | 43,800 B，1,803 行 | `930fc2bab9b7f99ad45c1a2d50349a750bb76b52f89bad2dc0f203b62310f36f` | ✓ 与任务一致（注：无裸 `text.md`，文件名为 `2026-w47-es-zh-tw.text.md`）|
| 核心 es 印 | 17,212,955 B | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` | ✓ 与重建基线一致，未变 |
| 核心 es 网 | 1,410,471 B | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235` | ✓ 未变 |
| 核心 es text.md | 1,822 行 | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` | ✓ 未变 |

旧版对照（`scratch-refanout-es/backup-old/`）亦复核为 proof1 的旧版：印
`23926bd9729a041142472d066f0be2365d0edb54af3771e35e83e4d870ab8ff6`
（17,262,202 B），网 `3e96ea85cb5bfe3cdadd1d1ef1b861c26d4954ddca4daf1798738b03dd573920`
（1,686,124 B），text.md `0e6a0fbb89c1a686dd4484e5c2cc8d7cd14bd78627ecef6419987dbab1040fd0`
（1,786 行）。

## §2 proof1 缺陷复核——全部已修复

| # | 缺陷（proof1） | 重建版复核 | 状态 |
|---|---|---|---|
| D1 | `antes del jueves`→`hasta`（7 处西语 + keys 116/139 + 核心残留） | `antes del jueves`=0；`hasta el jueves`×5（content12）、×3（content8）、×7（text.md）；keys 116/139 为 `hasta`；notes 3/9/22/65/123 为「郵寄投票最遲須在 19 日申請」；P2 `hasta ese día`；ABSTRACT 改为「最遲11月19日申請郵寄投票」 | ✓ 已修 |
| D2 | consejo 句截断（`content12.py:131`） | 句尾完整：`…te enseñamos cómo leer un debate sin perderse.`（P1 目视亦见完整） | ✓ 已修 |
| D3 | P1 CINCO CLAVES 盒溢出（盒底 1288.0，中文行 y=1300） | 盒 700→720，盒底 **1308.0**，本盒末行基线 1300.0，空隙 +8.0；墨迹底 1302.2，墨迹空隙 **+5.8**（「五大看點，不編數字：全在本期裡講清。」框内，目视确认） | ✓ 已修 |
| D4 | P5 词库缺 `correo`/`envío`（核心级） | 按协调员裁定：**接受现状（as-is），不改，不计入缺陷**（见 core-es3 C3；Q70 `correo`、Q72 `envío` 可由正文/提示解出；`sobre`/`urna` 无空可填） | 接受现状 |
| D5 | P7 样信 derbi 在周五非周六 | `content7.py:99` Marta 来信现为 `el sábado veo el derbi`，半角括号 `(ejemplo, escrito por la redacción)`（裁定的 MERGE 形式）；P7 目视确认 | ✓ 已修 |

6 项 classify REVERT 全部落盘复核：content12.py:116 短释「辯論」；content56.py:117 全段「…讀懂競選：辯論、政綱與民調」；
content8.py:124/125 y=1337、:129 Flow y=1363；content56.py:22 `本週計劃`。

## §3 门禁汇总（全部通过）

| 门禁 | 结果 | 证据 |
|---|---|---|
| run.py（scratch 副本） | **rc=0**，TOTAL 150；A2 50 / B1 72 / B2 28；页分布 1:10 2:18 3:18 4:18 5:18 6:18 7:12 8:38；MODELO 97 词 | `run-copy.log` |
| render.py（scratch 副本） | **rc=0**；重渲染印 PDF 与交付版 **SHA 完全相同**；重渲染网 PDF 差 4 字节（见 O6，内容等价） | `render-copy.log` |
| SVG 一致性（freeze baseline） | 8/8 SVG 字节相同；核心完整性重哈希干净，rc=0 | `freeze.log` |
| occlusion_audit.py | 自检 6 类 planted 全部触发 1 次、干净对照静默；本版 **0 flags，rc=0** | `occlusion.log`、`occlusion-selftest.log`、`occlusion.json` |
| p8.py extract | **150/150** 已注记，rc=0 | `p8-extract.log`、`p8-extract.json` |
| p8.py compare（vs core P8） | **CLEAN**；missing=[]、extra=0、keydiff=[137, 138]（两处读者语翻译题，西语句相同，属合法本地化） | `p8-compare.log`、`p8-compare.json` |
| freeze.py diff（core→本版） | rc=0；逐页 ± 串：P1 +24/−23、P2 +30/−30、P3 +20/−20、P4 +22/−22、P5 +28/−28、P6 +7/−7、P7 +32/−35、P8 +174/−179；新增 CJK 952。西语正文与 core build 10 **逐字节相同**（仅双语家具中文部分转换 + P7 来信括号重分段） | `freeze-diff.log`、`freeze-diff.json` |
| freeze.py diff --strict-cjk | **rc=1，预期行为**（见 §4） | `freeze-diff-strict.log`、`freeze-diff-strict.json` |
| 印/网文字层 | pdftotext -layout **逐字节相同，106,384 B**；纯文本提取亦相同（44,733 B） | `print.txt`、`web.txt`、`print-plain.txt`、`web-plain.txt` |
| P8 最小字号（minfont.py，印 P8） | 最小有效 **10.125 pt**（n=718），0 处低于 9.75 pt 下限 | `minfont.log` |
| keycheck_core.py | **149/150** 精确；唯一不符 #150（REG 键 `（開放題，範本如下）` vs 印 `✓`）——与 core 同款已裁定的开放题例外 | `keycheck.log`、`keycheck-150.json`、`keycheck-extract.json` |
| creambox.py 全扫 + creambox_diag.py（真墨） | 全部盒本盒末行在内；**0 本盒墨迹溢出**；最紧墨迹空隙 +0.1（P2 ¿SABÍAS? `ley.` 543.4/543.5；P5 VOTAR `compara precios antes de pagar.` 1251.4/1251.5——与 core-es3 O2 相同，墨迹在内，非缺陷）；P7 工具箱最小 +8.8（CARTAS 盒） | `creambox.log`、`creambox-diag.log` |
| boxtitle_core.py | 25 行标题，**0 负空隙 = 0 超框** | `boxtitle.log` |
| sweep_de.py | box-vs-hline 0；桥 20 个，桥孤儿 0，桥寡妇 0 | `sweep.log` |
| P8-keys 末端 | Flow 末端 col 3/3 y=**2506**（底 2560），无 OVERFLOW；P8 最末基线 2554.06（key 75 注），与旧版 2554.06 相同，均 <2560 | `run-copy.log` |

## §4 简体泄漏重验——残留 0（本轮重点）

- 直接 grep：`本周计划` 在全部 content*.py、text.md、ABSTRACT.txt 中 = **0**；`本週計劃` text.md ×1、content56.py:22 ×1。
  `antes del jueves`=0；`antes de ese día`/`19 日前`=0（ABSTRACT 现为「最遲11月19日申請郵寄投票」）。
- OpenCC 逐字扫描（`s2t(c)!=c`）覆盖 text.md、ABSTRACT.txt、全部 content*.py、8 个 SVG、print.txt：
  唯一命中 **「台」×1**——text.md:233、content12.py:181、P2 SVG、print.txt，词为 **「電台」**
  （「週三：電台住房辯論，PSOE 對 PP」）。**裁定：同形字，非泄漏。**
  台是台灣標準繁體用法（電台、電視台、台灣，教育部标准）；该词自 core 完整继承
  （core 同为「电台」，仅 電→電 转换）；OpenCC 默认 s2t 把 电台→電臺只是机械偏好，
  不是简体使用的证据。
- freeze CJK 多重集配对重算（新增 947 / 移除 932；与 freeze.py 的 952 之差 5 字为方法差：
  逐页字符串多重集 vs 全局字符多重集）：**新增字符中简体独有 = {}（空集）**。
  每个新增繁体字要么是被移除简体字的繁体对应字，要么属于合法读者语措辞差异：
  佛朗明哥 ×19 vs core 弗拉门戈 ×19（19 次精确镜像——台湾 vs 大陆译法）、
  繁體中文副标题 vs core 简体中文、引号计数。本版**无任何简体字**。
- 弯引号配对：text.md « 53/53、「 5/5；8 页 SVG 逐页平衡（P7 31/31、P8 5/5 +「 2/2）；
  直引号/直单引号 0；U+FFFD 0。
- 内部标签扫描：text.md 中 SOP/proofread/cover/lint 均为 0；`zh-tw`/`es-zh-tw`/`2026-w47`
  各 ×1，均为首行标题 `# 2026-w47-es-zh-tw`（与 core 同款文件头，非读者正文）；
  `12 de noviembre`=0；VOL.4 ×1（标题行）、VOL.5 ×3（均为合法下期预告）。

## §5 150 题手验——150/150（三源一致）

三源：REG（副本 run.py）vs P8 提取键 vs text.md RESPUESTAS 块（text.md:1388 起，150 行，
1–150 无缺失）：**0 不一致**（#150 例外除外）。
全 stem→key 表已建并逐题通读（`stem-key-table.txt`，844 行；138 个 `ex()` + 3 个 `match_set` = 150 REG 条目），
全部正确，包括：匹配组 Q25–28（c/b/d/a）、Q52–55（c/b/a/d）、Q141–144（c/d/b/a）；
Q96 `Aunque` + 直陈式；Q112 `tenga`；Q132 B；Q150 范文手数 **97 词**（run.py 亦报 97；P8 印「范文（97 词）」）。
已记录的继承性不完美（非缺陷，proof1/core 已记录）：#103 键注「a las 21:00（介詞 a）」而题干为 18:30；
#56 注「榜首之爭更重要」vs amistoso 语境；C3 P5 词库（见 §2 D4）。
P8 key 91 注「提議的」不等於「確定的」——合法繁体引号风格本地化（core 为「“提议的”」），键字母 C 相同。
P6 时间线「16 NOV. — …(sin confirmar)」与正文「los dos partidos aceptan la cita, pero no hay hora publicada」
同义（acordado no es cerrado），自 core 继承，core 定稿时已通过，非新缺陷。
P7 `FRASES DE LA SEMANA` 8 句机械 exact-match：每句在全版 SVG 文本中恰好 **2×**（原文页 + P7），
页码标注正确（P1/P2/P3/P3/P4/P5/P6/P6）。

## §6 目视（8 页印 + 网 P1/P8）与旧版对比

8 页印 PDF 100 dpi 逐页目视（`png/p-1.png`…`p-8.png`，生产 cards 与重渲染逐字节相同）：
P1 CINCO CLAVES 框内中文行、完整 consejo、`hasta el jueves 19`、新段落均无问题；
P2 `hasta ese día`、日历、电台词；P3 Sargent 画 + PD 标注；P4 六场表 + 冠军联赛框；
P5 `本週計劃`、投票箱照片 + CC0 标注、VOTAR 框末行框内；P6 双 23 NOV 行、Academia 行、
RTVE 图表 45/45/30/30/15 与 JEC 脚注（195 分钟，45+45+30+30+15+30=195 ✓）；
P7 Marta 来信「el sábado veo el derbi」、ERRORES/LA PALABRA/CARTAS 三框、8 金句、VOL.5 横幅；
P8 150 键四栏、97 词范文、天鹅笔图。网 P1/P8 目视与印一致。
旧版对比（text.md diff + pdftotext token 多重集 diff + 逐页像素 diff）：
- text.md diff：127 行变、约 40 段，**全部**由已记录的修复集解释（antes→hasta 7 处 + 键/注、
  consejo 补全、derbi 周五→周六、P1/P2 新段落、P6 重构、JEC 脚注改写）。
  diff 中无 `本周计划` 变化（旧版已是 `本週計劃`；泄漏仅存在于 fresh fanout，已在交付前 revert）。
- token diff：移除 `antes`×11、`cómo.`×1、`viernes`×1（derbi）、`日前申請`×5+1、
  `PSOE/confirmado/había/ninguna`；新增 `hasta`×11、`perderse.`、`sábado`×1、
  `最遲須在`×5+1、RTVE/Academia/debate-a-ocho措辞、`Acuerdo…del 4 de noviembre`。无其他变化。
- 像素 diff（新 vs proof1 旧渲染，强差阈值 >30）：P1 28,620 px（行 985–2519，CINCO 框增高 + 正文重排区）、
  P2 10,467 px（仅第 1 栏，行 842–2279）、**P3/P4/P5 逐像素相同**、P6 249,809 px（全文 + 时间线 + 图表头区，
  重构所致，图表本身未移位）、P7 3,386 px（仅 derbi 行，行 1589–1611）、P8 10,876 px（键注区）。
  **无超出修复集的变化。**
- 印 vs 网像素差（文字层相同前提下）：P3/P5/P7/P8 为照片降采样（webpdf.py 已知行为），
  P1 强差 10,823 px 全部集中在行 0–400（黑体刊头字体子集渲染差异），400 行以下 0 强差；
  P2/P4/P6 仅数百像素抗锯齿噪声。无内容差异。
- 词汇表复现：P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5；P5 sobre 5 / papeleta 2 / censo 3 / plazo 3 / urna 5——均 ≥2×。

## §7 只记录、不计入判定：字体

本版 SVG 声明 `Noto Sans CJK SC` / `Noto Serif CJK SC`（P1 统计：Newsreader 104、Noto Sans CJK SC 70、
Noto Serif CJK SC 12、UnifrakturMaguntia 1）；`svglib.py` 指向 `NotoSerifCJK-Regular.ttc` /
`NotoSansCJK-Regular.ttc`，字体栈注释称 `Noto Serif CJK SC`。
即繁体中文版以 SC（简体）CJK 字体文件渲染。系统同一 .ttc 内含 TC 字面
（fc-list：NotoSansCJK-Regular.ttc 含 JP/HK/KR/SC/TC；NotoSerifCJK-Bold.ttc 同样），
但本版未请求 TC 字面。本项为生产级待定项，**只记录，不影响本轮判定**；
本轮未逐字裁定 SC/TC 字形变体。

## §8 观察（O，非缺陷，均继承自 core/旧版或工具行为）

- O1 孤儿标题（proof1 O1 继承）：P2 「D LAS PALABRAS」栏底、P4 「B LAS PALABRAS」栏底——
  标题在栏末、条目在下一栏；core 同款。
- O2 最紧墨迹空隙 +0.1（见 §3 creambox 行）：P2 `ley.`、P5 `compara precios…`——与 core-es3 O2 相同，墨迹在内。
- O3 孤字换行（逐行扫描全版，仅 3 处，与旧版**逐坐标相同**，core 亦有同样 3 处）：
  P2 y=721.3「止）」、P5 y=440.8「止）」（「（週四：郵寄投票申請截止）」换行尾）、P8 y=1570.1「二」
  （key 44 注「時間在前，動詞第二」换行尾；core 同注亦为孤「二」，y=1505.5）。CJK 换行单字残留，
  非任务孤儿标点清单（。/」/：/–）所列；孤儿标点实质计数 = **0**（SVG 中 4 个独行 –/— 均为行内分段，
  如 `巴薩–黃潛`、`137./138.… — 對照原文` 分隔符，非孤儿）。
- O4 P7 横幅几何：深色矩 y=2464.51、h=118、底 2582.51，页脚线 y=2596，空隙 13.5 px，与 core 完全相同。
- O5 版中大片留白（P5/P6 中栏）：core 同款布局。
- O6 网 PDF 字节重现性：重渲染网 PDF 与交付版差 4 字节（1,725,940 vs 1,725,936），
  位置在压缩流内；但文字层逐字节相同、8 页渲染逐像素相同、41 个字体子集标签完全相同——
  内容等价，非内容差异。印 PDF 重渲染逐字节相同。webpdf.py 的网 PDF 输出非字节确定性，
  属工具行为记录，非本版缺陷。
- O7 WEEKLY-KIT.md §1 仍引旧版 SHA/字节（17,262,202 B / 23926bd9…）；新 SHA 见 §7（重建节），
  与盘上一致。内部文档小瑕，不影响交付件。
- O8 行首标点换行（CJK 换行行为）：P2 日历「；提議舉行雙雄辯論）」、P7 A2 释「）；比賽在 a las 21:00 開球。」
  ——行首为 ；/），与旧版相同、core 同款，非孤儿标点清单所列。
- O9 已接受现状（proof1/core 已记录）：#103/#56 键注（见 §5）；C3 P5 词库（见 §2 D4）。

## §9 事实一致性抽查（全文 text.md 1,803 行通读）

选举 11 月 29 日周日 9:00–20:00；竞选 11 月 13–27 日（15 天）；反思日 11 月 28 日周六；
民调禁发 11 月 24–28 日（5 天）；西甲第 13 轮 11 月 20 日周五–23 日周一，积分 巴萨 33 / 皇马 30 /
马竞 28；欧冠第 5 轮 11 月 24/25 日；佛朗明哥 UNESCO 2010 年 11 月 16 日内罗毕；圣塞西莉亚 11 月 22 日周日；
毕尔巴鄂乐队 11 月 22 日 12:00 Euskalduna 宫；黑色星期五 11 月 27 日周五；MiDNI 暂停 11 月 5 日解除；
Sargent《Bailaora española》1880–81 PD。均与 core 定稿版一致，无新事实/语言缺陷。
P7 banner 几何（§8 O4）、P8-keys 末端（§3）均已量取。

## 附：产物清单（全部在 scratch-proof-es-zh-tw2/）

`PROOF-NOTE.md`（本件）、`GATE-LOG.md`、`run-copy.log`、`render-copy.log`、`print.txt`、`web.txt`、
`print-plain.txt`、`web-plain.txt`、`copy-web.txt`、`old-print.txt`、`old-web.txt`、`p8-extract.json`、
`p8-compare.json`、`freeze-diff.json`、`freeze-diff-strict.json`、`keycheck-150.json`、`keycheck-extract.json`、
`occlusion.json`、`stem-key-table.txt`、`scan_cjk.py`、`copy/`（run/render 副本，其印 PDF SHA 与交付版相同）、
`freeze/`、`png/`（印/网/副本网 100 dpi 渲染 + P8 200 dpi）、`tmp/`、`logs/`（各门禁日志 +
`textmd-old-new.diff`、`print-old-new.diff`）。
