# GATE-LOG — 2026-W47 it-ru proof1（全部机械门实跑证据）

版：`production/2026-w47/2026-w47-it-ru/`，build3。工具：`~/workspace/weekly-git/tools/venv/bin/python`，正典 creambox `hidden_files/w47/tools/creambox.py`（md5 ee7a55d8b2057cf4ad42a97bb1197383，已核对）。TMPDIR 全程指向本 scratch 下 `tmp/`（未用系统 /tmp）。探针：`git hash-object -w` 通过（9daeafb9864cf43055ae93beb0afd6c7d144bfa4），goals 侧小文件写入通过。源文件未改动、未 commit、未 push。

## §0 — 版身份与任务数字核对（以磁盘为准）

| 文件 | 磁盘字节 | 磁盘 SHA-256 | 任务所给 | 结论 |
|---|---|---|---|---|
| `La-Lucerna-VOL4-RU.pdf` | 14,181,162 | `b70e7b62da565b7fdb4aa18a56995bb7c366af395fca7c31847ebf857254b2b4` | 一致 | ✓ |
| `La-Lucerna-VOL4-RU-web.pdf` | 1,407,790 | `1c93b80d57de5e76b036bd60a2f2af05fde2d65c1ceb05e469344b657debd964` | 一致 | ✓ |
| `2026-w47-it-ru.text.md` | 67,722 | `7d3679679bccbaba3c4c94f0e5b6591c11b6ab03219c8e376d5b065148e63b55` | 一致 | ✓ |

三者全与任务一致，无停工事由。印 PDF 8 页，1462.5×2025pt；网 PDF 8 页，同尺寸，1,407,790 B（<7MB）。

**任务数字与磁盘不符 1 项（非缺陷，记录于此）：p8 compare keydiff。**
任务预期 keydiff 恰为 [137,138,139,140]。实测（`tools/p8.py compare --core-p8 …/core-it/svg/p8-valutazione.svg --edition-p8 …/it-ru/svg/p8-valutazione.svg --total 150`，RC=0）：`status: CLEAN missing=[] extra_count=0 keydiff=[137, 138, 139]`。逐键核对（`p8.py extract` 两边）：137 核心「圣母健康节人们走过还愿桥。」→ 本版「В праздник Мадонны делла Салюте люди переходят обетный мост.」；138 核心「周日晚上亚特兰大对国米。」→ 本版「В воскресенье вечером «Аталанта» играет с «Интером».」；139 核心「周六，拉齐奥在主场对莱切。」→ 本版「В субботу «Лацио» играет дома с «Лечче».」；**140 核心与本版 key 同为意语句「Ogni cifra deve essere chiara.」**——题干是中文句（核心）/俄语句（本版），key 是意语目标句，两边相同，故无 diff。这是正确行为，不是缺陷。KIT §8 的 [137,138,139] 与实测一致；任务的 [137,138,139,140] 预期不成立。

## §1 — occlusion 审计

`tools/occlusion_audit.py <edition>/svg --json occlusion.json`，RC=0。
- 自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- 结论：`0 flags`（8 页全版）。
- 说明：该工具对奶油框内溢出、框标题溢出、横向溢出、降部溢出有盲区，故以下各项另行实测，不以 occlusion 0 为据。

## §2 — 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

`tools/creambox.py <edition>/svg/*.svg` → `creambox.log`（767 行），RC=0（无退出码，扫描件）。
- P7-TOOLBOX 汇总：`3 boxes, min inside clearance +4.5, min desc-clear -1.5`。
- 全部「inside-only」末行 clearance 均 ≥ +4.5px；desc-clear 为负的 9 行见 §3 逐一实测（无一漫出）。
- BELOW-WINDOW（+24 ~ +44px）逐一裁定，均为下一标题/页脚/表格续行，非整行漫出（+12~+18px 的漫出模式未出现）：
  - P1 +24.0 `LA PAROLA DELLA SETTIMANA`（下一栏目标题）；P1 +44.0 页脚「Ответы на стр. 8」碎片；
  - P3 +37.0 `IL TORRAZZO E IL TORRONE`（下一栏目标题）；
  - P4 +29.0 `SAB 7.11` / +40.0 `Cagliari – Frosinone 1–0`、`Torino – Lecce 1–1` 等（赛果表续行，表内行）；P4 +26.0 `La 12ª giornata si gioca…`（表后段落）；
  - P6 +42.0 `ESERCIZI` 栏目标题 + 页脚碎片。
  以上均经 P1/P4/P6 目视确认。

## §3 — 降部溢出实测（任务 (d)；框高按基线+1.9px 定、无降部余量的已知漏检类）

9 个 desc-clear 为负的奶油框末行，PIL 真墨（实际渲染字体：西里尔 NotoSans-Regular / 拉丁 Newsreader-Regular）+ 200dpi 像素扫描：

| 页 | 框底 | 末行（基线） | PIL 墨底 − 框底 | 像素最深墨 − 框底 | 结论 |
|---|---|---|---|---|---|
| P2 | 960.6 | della musica e dei musicisti. (955.3) | 无降部字母，墨底=基线 | 框底下无墨 | 在框内 |
| P2 | 1379.6 | редакцию (1374.0) | −0.8px | −1.5px | 在框内（发丝） |
| P3 | 1021.1 | continua fino al 6 dicembre. (1015.8) | 无降部字母 | 框底下无墨 | 在框内 |
| P3 | 1319.6 | пришлите (1314.5) | −0.3px | −1.0px | 在框内（发丝） |
| P4 | 1140.4 | по (1135.9) | 无降部字母 | 框底下无墨 | 在框内 |
| P5 | 1010.7 | domenica 22 novembre. (1005.4) | 无降部字母 | 框底下无墨 | 在框内 |
| P5 | 1278.8 | пришлите (1273.6) | −0.5px | −1.0px | 在框内（发丝） |
| P7 | 1344.0 | с (1339.5) | 无降部字母 | 框底下无墨 | 在框内 |
| P7 | 1673.0 | переносится (1667.9) | −0.3px | 像素初扫 +11.8px 为误报（见下） | 在框内（发丝） |

P7「переносится」像素初扫 +11.8px 的真相：扫描带（框底+12px）触及了框下 y=1686 的 FRASI 绿色分隔线顶缘抗锯齿，不是该行降部；PIL 真墨底 1672.7（−0.3px），裁图 `crop-p7-col3end.png` 目视确认框内收尾、线在框外。es-fr/es-ru 同类缺陷（«А вы?»/«E TU?» 末行降部漫出）**本版未复现**。
证据文件：`descender.log`、`crop-p7-col3end.png`。

## §4 — 横向溢出：P2 配对题 (a) + P1 副标题 (b) + P1/P7 框标题 (e) + 全版右缘扫描

参考线：页边 1950px；版心右边界 1862px（SOP §1.1 左右留白 66pt：1462.5−66=1396.5pt=1862px）。

### (a) P2 配对题 b/d 首行
PIL 真墨（Newsreader 23px）与 200dpi 像素扫描一致（本版 ±0.1px；核心 ±1.2px，抗锯齿阈值所致）：

| 行 | 核心墨右（PIL / 像素） | 本版墨右（PIL / 像素） | vs 版心 1862 | vs 页边 1950 |
|---|---|---|---|---|
| b 首行 | 1831.0 / 1832.2（“il ponte di barche per la festa in”） | 1875.0 / 1874.9（“il ponte di barche per la festa del 21”） | **+12.9px（+9.7pt）** | −75.1px |
| d 首行 | 1821.8 / 1822.1（“la piccola luce di cera accesa in”） | 1877.8 / 1877.8（“la piccola luce di cera che si accende”） | **+15.8px（+11.9pt）** | −72.2px |
| a 首行（对照） | 1811.2 | 1811.2 | −50.8px | — |
| c 首行（对照） | 1806.5 | 1806.5 | −55.5px | — |

本版 `content12.py:262,264` 改写了核心意语定义（见 PROOF-NOTE D1），10 个 it-* 版全是新写法，核心盘上仍是旧写法。裁图 `crop-ed-p2-match.png` / `crop-core-p2-match.png` 目视确认 b/d 探出栏右缘。任务前提「核心 it 自身溢出 ~11–13pt」在磁盘核心上不复现（核心 b/d 距版心 −29.8 / −39.9px），见 PROOF-NOTE O1。
证据：`ink-p2.log`、`pixel-p2.log`、`match-dump2.log`。

### (b) P1 副标题（三法一致）
- 刊头顶行 y=92（最右 `SETTIMANA DAL 16 AL 22 NOVEMBRE 2026`）：PIL 墨右 1802.4px，在版心内 −59.6px。
- 刊头带 y=330（`ИТАЛЬЯНСКИЙ　VOL.4　LA SERIE A　IL TORRONE　VENEZIA`，最右 `VENEZIA`）：PIL 墨右 1761.6px，在版心内。
- y=372 标语（`IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`，居中）：PIL 墨右 1290.1px。
- **但 P1 右栏另有两行副标题/栏目标题越出版心**（D2/D3）：y=694 `На этой неделе　Cosa succede, giorno per giorno`，PIL 1904.5 / 像素 1903.7 / PDF span 1905.5px（**+42.5px / +31.9pt**）；y=1352 `IN QUESTO NUMERO　СОДЕРЖАНИЕ`，PIL 1898.0 / 像素 1896.5 / PDF span 1898.7px（**+36.0px / +27.0pt**）。核心同行墨右 1839.2 / 1822.8px，均在版心内。
- 结论：刊头副标题本身无溢出；it-de D1 同类（右栏标题行越出）在本版以 D2/D3 形式复现。
证据：`ink-p1p7.log`、`pdfspan-p1p7.log`、`ink-core-p1p7.log`。

### (e) P1/P7 框标题逐个真墨实测
对 P1（4 个奶油框）、P7（3 个奶油框）全部文本做 PIL 真墨扫描：墨右 > 框右缘 或 > 版心者仅以下 3 行（与 (b) 的 D2/D3 及 D4 为同一批，无其他）：
- P1 `　Cosa succede, giorno per giorno`：墨右 1904.5 vs 框右 1862.0（+42.5px）；
- P1 `СОДЕРЖАНИЕ`：墨右 1898.0 vs 框右 1862.0（+36.0px）；
- P7 `ОШИБКИ`（`ERRORI TIPICI　ТИПИЧНЫЕ ОШИБКИ` y=242）：墨右 1892.9 vs 框右 1862.0（+30.9px）；PDF span 1896.5px；核心同行墨右 1735.8px。
无纵向越框（墨底均在框底内）。es-pt D1（+10.9）同类漏检未在本版其他标题上出现。
证据：`boxtitle.log`。

### 全版右缘像素扫描（200dpi，暗像素阈值 <120）
8 页无一越过页边 1950px。越出版心 1862px 者仅：P1 两处（D2、D3）、P2 两处（D1 的 b/d，另 +0.4px 的竖线抗锯齿可忽略）、P7 一处（D4，+31.6px 像素值）。P3/P4/P5/P6/P8 仅 +0.4~+0.9px 的竖线/框线抗锯齿，无文本越出。
证据：`right-edge-scan.log`。

## §5 — freeze（基线 + diff）

- `tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out scratch/freeze-baseline`：RC=0，**8/8 SVGs byte-identical**（核心 8 文件重算 hash 前后一致，未被改动）。`freeze-baseline.log`。
- `tools/freeze.py diff --core-svg …/core-it/svg --edition-svg …/it-ru/svg`：RC=0。新增 CJK 仅 U+3000，每页 1 个，共 8 个（SOP §1.1 家具全角空格分隔符，豁免）；其余新增/删除串为俄语讲解层替换中文讲解层（核心本身带中文讲解层，见 freeze-diff.json：核心 P1 CJK 197 → 本版 20，P8 1015 → 22）。
- 注：freeze diff 的增/删串含两条意语改写（P2 配对定义，D1），KIT 称「0 unexplained」但未在 KIT §9 列出该改写——改写经 `content12.py` 跨 10 版核实为全家一致，属 fan-out 侧改动，见 PROOF-NOTE D1/O1。

## §6 — p8 compare（显式 --core-p8/--edition-p8，--total 150）

见 §0：`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139]`，extract 两边 noted 均为 150/150。`p8-compare.json` / `p8-core.json` / `p8-ed.json`。
另：`p8 extract` key 与 text.md RISPOSTE 逐条比对 0 不符（见 §9 方法）。

## §7 — keycheck 150/150

`keycheck-150.json`：逐题手验（题干 + 原文/图表/段落复算 + 语法规则），全部 PASS。逐题依据见文件内 `basis` 字段；要点：
- 编号连续 1–150，无缺重（138 个单编题干 + 25–28 / 52–55 / 141–144 三组共 12 题）；级别 A2 47 / B1 70 / B2 33（与 KIT 一致，机械复算）。
- 验算类：Q85 13−11=2、Q86 6+7=13、比分表 10 场 24 球（3+1+2+3+3+2+3+1+2+4）、范文手数 99 词、P7 八句金句逐字出自本期文章（各 1 次正文 + 1 次 P7，用脚本计数复核）。
- 机械交叉核对：p8.py 抽取的 150 个印 key 与 text.md RISPOSTE 0 不符；印 P8 noted 150/150。

## §8 — boxtitle（见 §4(e)）、文字层、P8 字号、引号

- **印/网文字层比对**（pdftotext 两版）：印 44,174 字符 / 网 44,284 字符；非空白字符多重集相等（print-only 与 web-only 差集仅为空格 106 + 换行 4）；词多重集差异纯为 pdftotext 对字母间距西里尔词的切分不同（印「ИТАЛЬЯНСКИЙЕЖЕНЕДЕЛЬНИК」vs 网「ИТАЛЬЯНСКИЙ ЕЖЕНЕДЕЛЬНИК」），与 KIT §8 所述一致。词数 7,602 / 7,709。`textlayer.log`。
- **P8 最小字号实测**（PyMuPDF 逐 span）：P8 最小 **9.75pt**（618 个 span，其中 RISPOSTE 键），与 KIT 称的 13 SVG px = 9.75pt 一致，为 SOP §1.1 让步第 4 步下限；其余各页最小 11.62pt（P6 为 12.75pt）。`p8font-quotes.log`。
- **弯引号全版扫描**（8 个 SVG + text.md）：U+201C 0、U+201D 0、U+2019 0、直双引号 0；« » 每页成对平衡（P1 9/9、P2 6/6、P3 6/6、P4 0/0、P5 6/6、P6 5/5、P7 27/27、P8 36/36）；直单引号 `'` 共 68 处，经逐一上下文核查全是意语省音（l' / d' / c'è / all' / dell' / cent'anni / d'Oro 等），无引号用法。`apos.log`。
- **CJK 全版扫描**（SVG）：除 U+3000 家具分隔符外，仅 P1 三色蛾品牌标「三色蛾」（核心亦有，同一元素）与 P8 全角冒号 ：×7（冻结合动词变位表，核心亦有）。text.md 的 CJK：U+3000×101、：×14、「翻译」×4（D5）。`cjk-scan.txt`。

## §9 — text.md 校验与外部事实来源

- text.md 1317 行通读；题量按页 10/18/18/18/18/18/12/38；ABSTRACT.txt 一行俄语 682 B、无 ASCII 双引号，含真实主题与「A2–B2」「150 упражнений」。
- 日期/星期经 `date` 核验（Europe/Rome）：2026-11-16 周一、11-17 周二、11-12 周四、11-21 周六、11-22 周日；11月16–22日刊期正确。
- 事实来源（取自核心 KIT §4，复校未改动任何事实，仅核对本版内一致性）：Serie A 第 11 轮（11月6–8日，24 球 10 场）与第 12 轮（11月21–23日）；Nitto ATP Finals 都灵 11月15–22日；Festa del Torrone 克雷莫纳第 29 届 11月7–22日；Eurochocolate 佩鲁贾第 32 届 11月13–22日；Alba 白松露集市至 12月6日；Manovra 2027（DPB 10月15日；法案 C. 3174-bis；听证 11月9–12日；修正案截止 11月17日 18:00）；Madonna della Salute 11月21日周六；全国植树日 11月21日；Santa Cecilia 11月22日周日；BookCity 米兰 11月23–29日；Torino Film Festival 11月24日–12月2日（9 天）。本版内上述日期/比分/数字全部自洽；P6 练习图表已标「DATI INVENTATI PER L'ESERCIZIO」。
- §1.1 扫描复核：纸色 #fbfaf6；无金/红褐/近黑；VOL.4×9、VOL.5 仅 3 处合法（P2 互见、P7 披露、P7 下期预告）；徽章色 A2/B1/B2 齐全；无全页双线框；「·」148 处只在选项串/gloss 列，刊头（y=92）与页脚（y=2624）行为 0。

## §10 — 判为非缺陷的项

- 练习小节头一律冻结为日语（任务裁决；tr-en 的 8 条英译已废弃，不报）。
- E 组 keydiff [137,138,139]，status CLEAN（§0 论证；Q140 key 为意语句，两边相同）。
- it 家庭文件名大写读者码（`La-Lucerna-VOL4-RU.pdf`，既定格式）。
- 动词变位表全角冒号 ：（16–20、60–61，冻结合核心；P8 印版 7 处与核心一致）。
- 「·」在选项串/gloss 列（冻结合核心，W46 接受先例）；家具行无「·」。
- P3/P5 中段空白（核心版式，KIT §10）。
- P1 无 drop cap（与核心及已接受的 W46-FR 版一致）。
- P8 字号 9.75pt（SOP §1.1 让步第 4 步下限，与核心一致）。
- 俄语说明行词隙偏紧（KIT §10 已披露的 svglib 特性；可读、无重叠、无豆腐）。
- 核心 P2 配对题在本版 D1 语境下不复现——记为 O1，未决事项，不作本版缺陷减免（D1 以本版实测为准）。

## §11 — 证据文件清单（本 scratch 内）

`PROOF-NOTE.md`、`GATE-LOG.md`、`keycheck-150.json`、`occlusion.log`、`occlusion.json`、`creambox.log`、`freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`、`p8-compare.log`、`p8-compare.json`、`p8-core.json`、`p8-ed.json`、`ink-p2.log`、`pixel-p2.log`、`ink-p1p7.log`、`pdfspan-p1p7.log`、`ink-core-p1p7.log`、`boxtitle.log`、`right-edge-scan.log`、`descender.log`、`textlayer.log`、`p8font-quotes.log`、`apos.log`、`cjk-scan.txt`、`counts.log`、`svg-dump.log`、`match-dump.log`、`match-dump2.log`、`print.txt`、`web.txt`、`png/p-1.png` … `png/p-8.png`（200dpi 印 PDF 渲染件）、`png-core/core-p2-2.png`、`crop-ed-p2-match.png`、`crop-core-p2-match.png`、`crop-p7-col3end.png`。
