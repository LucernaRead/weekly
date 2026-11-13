# PROOF-NOTE — 2026-W47 ru-nl（re-fanout 重建版，VOL.4）

- 校对员：proof1（SOP §8.4，与重建者不同人）
- 日期：2026-11-11
- 对象：`production/2026-w47/2026-w47-ru-nl/`（俄语目标 × 荷兰语读者）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-nl2/`
- 先验依据：协调员 16:58 UTC 三 SHA + re-fanout 报告 `scratch-refanout-ru/FANOUT-REPORT-ru.md` ru-nl 小节 + 版内 `WEEKLY-KIT.md`

## 结论：(b) — 不通过，须修后重校

**1 项实测缺陷（D7，见下）。** 除 D7 外，全部机械门与 150 题手验均通过；但按 SOP §8.4 零发现门，D7 存在即不得定稿。修 D7 后仅须就 D7 重校（重渲染 + 重量 P7 band），其余门结论不变。

## 三 SHA 实测（均与先验值一致）

| 文件 | 字节 | sha256 实测 | 先验 |
|---|---|---|---|
| `Lucerna-VOL4-ru-nl.pdf`（印） | 21,315,805 | `8982ce29eaf2bc57661a089b9bf0bd8021444130e2e0c9aa505f9176de4a1e17` | 一致 |
| `Lucerna-VOL4-ru-nl-web.pdf`（网） | 3,387,072 | `abc3ec69f695129c9e248dae36880da1754f6af5ef32b62f5438435458512593` | 一致 |
| `2026-w47-ru-nl.text.md`（文） | 64,053 | `96dc93598dec047b87a168c2332bc30b611b8a42250d22e65c7e1da2920ac694` | 一致 |

## 缺陷清单

### D7 — P7 band 副标 “Drie niveaus, drie thema’s” 中’ 与 s 之间 16 px 空隙（词内断裂）

- **源码：** `content7.py:12`，`p.band("ЯЗЫК　TAAL", "Lucerna", "Фокус на язык　Три уровня, три темы　Drie niveaus, drie thema’s")`；U+2019（’）为全版 SVG 唯一一处 U+2019（全版 text run 扫描：U+2019 ×1，U+0027 ×0；core-ru 为 0），源自 D1 KEEP 值。
- **实测值（像素墨）：** P7 band y≈168，荷兰段 run 起点 x=1584.2（SVG）。’ 的 advance 为 18.0 px（18 px 字号，Noto Sans CJK SC 子字体 idx 2 的 U+2019 为 1 em 全宽），墨本身仅 1 列；实测墨列（card / 印 PDF / 网 PDF 三源一致）：
- `a`（thema 末）墨右缘 x=1803/1804；
-’ 墨 x=1807（card）/ 1808（PDF）；
- `s` 墨左缘 x=1824（card）/ 1825（PDF）；
- **’ → s 墨间隙 16 px**。同 run 内其他相邻字母墨间隙仅 1–6 px（“Drie” 2–3 px，“niveaus” 1–2 px），16 px 为 3–16 倍异常值。
- **渲染证据：** card `cards/p7-yazyk.png`、印 PDF 96 dpi 渲染 `p96-7.png`、网 PDF 96 dpi 渲染 `w96-7.png` 三者同一坐标、同一间隙。放大裁切 `ed-p7-band-themas.png`（x 1560–1870, y 140–190, 4×）肉眼即见 “thema' s”。读作荷兰语时仍可辨认 “thema's”，属 cosmetic，但为页眉 band 上肉眼可见的词内断裂，不在任何已知 ruling 内（KIT §7 的 4–6 px 窄空格 ruling 覆盖的是西里尔–拉丁交界处窄距，与此 16 px 词内宽距相反）。
- **根因：** band 文字按 sans fallback 走 Noto Sans CJK SC，该字体 U+2019 advance 为 1 em，标记贴左缘，`s` 被推出 16 px。修法不在校对权限内（仅记录）：建议将 U+2019 换为半宽形式（W46 TM 值已有’→' 的同类先例），或将 band 荷兰段改走 Noto Sans。
- **范围：** 仅此一处；全版无其他 U+2019 / U+0027。

## 观察项（非本版缺陷，不阻塞）

### O1 — 两套 adjudicator 工具各有 bug；re-fanout 的 “42/42 CLEAR” 未被其自带工具有效量出（方法论问题，非本版缺陷）

- `scratch-fanout-ru/adjudicate_ru.py` 硬编码 `SX = 1950/1800`，对本族（SVG 宽 1950）错误；其 42/42 CLEAR 是在约偏右 8% 的列上量的。修正 SX=1.0 后在 card 上重裁：38 CLEAR + 4 OVERLAP（均为 `Краснодар` 与收 `»`，P1 ×1、P4 ×3，PIL 重叠 3.1×11.0 px）。
- core-ru 同 42 旗标与本版一致（34 字节相同；8 处仅 y 位移或镜像 run 顺序）；core 以 SX=1.0 重裁同样 38/4；4 处像素与 core card 逐字节相同（core 继承）。
- **决定性核查在交付物 PDF 上**（96 dpi MuPDF 渲染 + 修正版 adjudicator）：印 PDF 与网 PDF 均为 **41 CLEAR / 1 OVERLAP**；4 处 `Краснодар»` 在两 PDF 上均为 CLEAR、间隙 1 px（行级：最小单行间隙恰为 1，无 0 行）。唯一 PDF OVERLAP 是 P7 `Кипренского` vs `, 1827 `—— adjudicator 背景翻转造成的假阳性（取样行撞上上方深色普希金肖像，把亮像素当墨测）；正确阈值重测：最宽净空 8 px（印 PDF）/ 9 px（card），thr<128 时 9/11 px；4× 裁切 `ed-p7-kiprensk-pdf.png` / `ed-p7-kiprensk-card.png` 肉眼可见空隙。
- core proof1 自带 adjudicator（`scratch-proof-core-ru1/adjudicate.py`）计数器反向（`if n>=2: cur+=1` 数的是连续墨列却称作 gap；`CLEAR if best>=1`）。它打印的 4 处 “gap=11px” 实为 11 列墨列——与其自有 p96 渲染上的 1 px 间隙一致。
- **结论：** 两份 “42/42 CLEAR” 结论碰巧为真（交付 PDF 每处交界 ≥1 px，字形清晰可辨，4× 裁切 `ed-p1-krasnodar-ed.png`、`ed-p4-krasnodar-a/b/c-ed.png` 已验），但都不是被各自工具有效量出的。**建议**修 `adjudicate_ru.py` 的 SX 与 core proof1 的计数器；本版无需因此返工。
- 附：阈值扫查 J±15 曾出现 4 px 假 “净空”，定位在 (243,246)/(1184,1187)——`»` 字形内 chevron 间白——与 (216,217) `р` 字腔内；J±10 窗口正确排除。印 PDF 在 J 处恰有 1 列净列，card 无。

### O2 — check_core 残留 2 项（core 继承，非新缺陷）

- orphan 1：P7 y553 `”».`；same-baseline collision 1：P1 y1712 `чёрная`。golden BAD 0、gloss fail 0。两项与 core-ru 同值同位，不作本版缺陷。

### O3 — 已核实、无需处理

- 字面 `___` = 87 处：text.md 87、版内 SVG 联合文本 87、core text.md 87，一致；core 继承的模板缺口，不作缺陷。
- P3/P5 中段留白：文章短、练习区固定起始位，结构性留白，与 core 同型。
- 西里尔–拉丁交界窄空格（如 P1 `От редакцииLucerna`、P3 `криминальнаяcrimineel`、P7 `синоптикиобещают`）：KIT §7 已裁定的 4–6 px 正常类。
- P7 普希金肖像为半脸裁切：与 core 同图同框（`x=88 y=1200 w=873 h=280`，`preserveAspectRatio="xMidYMid slice"`，图片 base64 sha 前 16 位 `8d178ac7c49340d2` 两版相同；紧裁图像区像素相同），core 继承。
- P8 无 Morozko 图：`run.log` 明确 `P8 morozko SKIPPED: no room (col 3 y 2389.29)`，设计如此；freeze 删西里尔 15 词均为 P8 caption 词，已全部解释（见 GATE-LOG）。
- P6 日条 21/22 黄色格：非奶油框（黄色填充），不在 32 奶油矩形内；200 dpi 目检数字居中无溢出。

## 门禁总览（实测值，详见 GATE-LOG.md）

| 门 | 实测 | 结果 |
|---|---|---|
| 三 SHA | 均与先验一致（上表） | PASS |
| run.py | rc=0；TOTAL 150；0 FLOW OVERFLOW / HEAD TOO WIDE；scratch 重建 8/8 SVG 字节相同 | PASS |
| check_core | rc=0；golden BAD 0；gloss 0；golden 8/8 ×2；orphan 1 / collision 1（O2） | PASS |
| p8 extract + compare | 150/150，rc=0；compare CLEAN；keydiff [137,138,139,140]；与 core `ru-p8.json` 直接 keydiff 相同 | PASS |
| occlusion 真实审计 | 42 TEXTX，0 LINEX，0 COVER/FOOTER/EDGE；交付 PDF 上 41 CLEAR / 1 假阳性（O1）；最小间隙 1 px | PASS |
| freeze | core 基线 8/8；版内自比对 8/8；core→版删除 distinct 487 / count-sum 854；西里尔删除 15（全在 P8，全部解释）；无法解释 0；新增 CJK 仅 U+3000 ×8 | PASS |
| 印/网文字层 multiset | 逐页相同，共 31,087 字符；8/8 页 | PASS |
| s11_check | rc=0，FAILURES: none；P8 最小字号 9.75 pt；纸色 #fbfaf6；无禁色；无 CJK 可见；网 3,387,072 B < 7 MB | PASS |
| creambox | 32 奶油矩形；0 负向内侧净空；95 BELOW-WINDOW 行（+28×25, +32×41, +34×4, +37×25，均为既有 +24..+37 区间）；1 处 −1.0 为假阳性（无降部字形，真墨底 1153，两渲染净空 +6 px） | PASS |
| 盒标题 PIL 真墨 | 32/32 有标题；最小 clear 18.9 px（P6）；0 负值；0 处 <10 px；最紧处 PDF 像素交叉验证一致（943 vs 942.1） | PASS |
| D1 | text.md L459/L504/L596 精确；4 个 nl KEEP 值均在 SVG 内；网 PDF 嵌 LucernaNotoSerif-Italic（CGSAUI+）与 LucernaNewsreader-Italic（JIOAFO+）；P1 `чёрная пятница` 带空格 ×5，无无空格 | PASS |
| kicker | 9 双空格墨间隙 [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]，最小 5.9 px ≥ 4 | PASS |
| D2 | Q25 `День студента` 在 `content12.py:276`；全称 ×2 在 text.md | PASS |
| D6 | `желании` ×2（text.md L173 练习、L694 答案表）；p8 key 20 = `желании` = core | PASS |
| web PDF 重渲染（scratch） | 3,387,112 B；文字层逐页 multiset 与发货网 PDF 相同；SHA 不同系 fontTools wall-clock（预期，不作证据） | PASS |
| 150 题手验 | key-vs-stem 逐题语义核对 150/150；5 组 matching 渲染字母顺序已按 SVG 实测核对；练习 key vs P8 答案表 150/150 相同；8 页 200 dpi 目检无溢出/重叠/裁切 | PASS（除 D7） |
