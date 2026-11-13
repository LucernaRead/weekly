# PROOF-NOTE — 2026-w47-ja-pt 第一轮独立校对（叶子）

- 校对员：叶子（第一轮独立复校，与 builder / 核心 builder / 各轮复校员不同人）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-pt/`（target 日本語，reader 葡萄牙文）
- 日期：2026-11-11
- 结论：**(b) 缺陷清单 — 本轮发现 1 项缺陷，未达零问题，不可定稿**（按 SOP §8.4，定稿须一整轮全量校对零问题；定稿与否由协调员定，本笔记只报事实）

## 身份复核（先核身份，通过）

- 印刷 PDF `Lucerna-VOL4-JA-PT.pdf`：29,103,006 字节，SHA-256
  `5e7542bc94e191e418fd49326676523e545aeb3eb2363d48c19c1cc6dcb33e56`
  （自行算出，与 KIT 登记的完整值逐字一致）
- 网页 PDF `Lucerna-VOL4-JA-PT-web.pdf`：4,485,027 字节，SHA-256
  `499149398ebed4848a02b2e8efcaaf9bbbbfe1c97effe651ffde8029d8a6629c`
  （自行算出，与 KIT 登记的完整值逐字一致）
- 两 PDF 均为 8 页，1462.5 × 2025 pt。

## 缺陷清单（1 项）

### D1 — P2「11月のことば」第 1 词框，葡文释义第二行溢出框外（轻微）

- 位置：P2 下部「11月のことば」四词框之首（熊手框），`svg/p2-kurashi.svg`。
- 原文（成品现状）：词框内释义两行——
  `um ancinho de bambu para negócios` / `prósperos`；
  第二行 `prósperos` 落在词框浅底色块之外、白纸上，紧贴下一行
  `文で覚えましょう：『19日に、浅草で熊手を買います。』`的上方。
- 应为：释义两行都落在词框之内（如其余三词框：`Celebrar com palmas` /
  `o dia em que começam as vendas` / `quando começa a cair um pouco de neve`
  均单行框内）；或缩短释义至单行，或加高词框。
- 证据（几何 + 目视双重确认）：
  - SVG 坐标：词框 rect x=88, y=1618, w=422.5, h=150，即底边 y=1768；
    释义行 1 基线 y=1752.06（框内），行 2 `prósperos` 基线 y=1776.76，
    墨迹超出底边约 9px；下一行基线 y=1800，无重叠。
  - 从印刷 PDF 重新渲染的 P2 全页目视 + 局部 2× 放大裁图
    （`gates/p2-words-crop.png`）确认 `prósperos` 在米色块之外、白纸上。
  - 核心版同一词框 high=150 不变，中文释义单行框内；是 fan-out 释义变长
    两行后、词框未随之加高所致（注：同页两处 Nota 框 builder 已加高
    115.95→145.675，词框未加高）。
  - 全版浅色框溢出扫描（8 页 SVG，`#f0eee5` 框 + 文本几何）：仅此一处真溢出；
    另三处 “ink-cross” 候选（P2/P3/P5 `あなたは？` 框末行 `envia-nas.`）
    为约 0.1–0.7px 的量测噪声，核心版同位置中文末行亦同（0.5px），不列缺陷。
- 严重度：轻微（minor）——文字完整可读，无重叠、无裁切、无描边穿线；
  但属肉眼可见的破框，零问题门槛下计为 1 项缺陷。

## 全量复校结果（除 D1 外全部通过）

### 1. 全文独立复校
- 印刷 PDF 8 版逐版目视（pdftoppm 从印刷 PDF 重新渲染，
  `render-print/p-1.png`～`p-8.png`，不采信 builder 的图）+ 网页 P1/P8
  （`render-web/wp1-1.png`、`wp8-8.png`）：除 D1 外，无溢出、重叠、压页脚、
  压框线、豆腐块；图片与出处齐全（P1 枫叶、P3 葡萄园、P5 岚山池塘、
  P7 酉之市 2025 照片注明年份、P8 岚山寺院；P4 无图，与核心一致）。
- 核心↔fan-out 全文 diff（`gates/textdiff-core-pt.txt`，359 行核心行 →
  379 行葡文行）：全部改动只在讲解层（译注、栏目副题、页脚、题型标签、
  答案简析、P7 披露、金句葡文释义）；日文正文、题干、选项无一字改动，
  核心冻结成立。
- 150 题逐题验算：题号连续 1–150（25–28 / 43–46 / 141–144 为核心既有的
  四项配对合题，与核心版逐字相同）；分版 10/18/18/18/18/18/12/38、
  级别 A2 48 / B1 73 / B2 29（重跑 registry 实测，与 KIT 一致）；
  图表题验算：P6 图 38/24/22/16=100%，ex 91: 38−24=14、ex 92: 38+24=62、
  ex 93: 合计 100；日期/星期均与核心一致（19 日周四、22 日周日、
  23 日周一、12 月 1 日周二等）；范文 154 字。
- 金句 8 条：日文逐字与核心一致，在正文 + P7 金句栏各出现一次，
  空白压缩后计数 8× 恰为 2；葡文释义页码标注 (p. 1/2/3/4/7) 均与原文所在版相符。
- VOL：文本层 VOL.4 共 10 处（P1 顶条 + 徽章 + 各页页脚），VOL.5 共 3 处
  （P4 结尾条、P7 披露、P7 下期预告），与 KIT 登记一致；
  VOL.3 仅 1 处，为 P4 前号注 `前号（VOL.3）では…`，与核心逐字节相同
  （W46 即 VOL.3，合法）。
- 徽章逐页计数（SVG 文本元 `>A2<` 等精确计数，与核心版逐页逐级完全相同）：
  P1 A2 11 / B1 2 / B2 1；P2 A2 15；P3 A2 7 / B1 8；P4 B1 18；
  P5 B1 18；P6 B2 18；P7 A2 4 / B1 4 / B2 4；P8 A2 9 / B1 22 / B2 4。
  （徽章元总数 145 ≠ 150，因 P1 含 4 个栏目级徽章、P8 有 3 题共用徽章——
  核心版同一结构；级别分布以 registry 为准：A2 48 / B1 73 / B2 29。）
- 刊头 196px（147pt）、P1 头条 56px（42pt），实测与 KIT 一致；
  §1.1 grep：纸色 `#fbfaf6` 每页 1×，旧 `#f7f1e2` 0×，禁用色 0×，
  `·` 0×，页脚行 `Página N de 8` 每页 1×。
- P8 最小字号 9.975pt（答案，162 spans），次小 10.35pt（题干，79 spans）——
  ≥9.75pt 底线，题干 10.35pt 未动（已记录的 adjudication，不列缺陷）。
- ABSTRACT.txt 为葡文单行，内容真实（酉之市/新酒/相扑/流行语 30/红叶、
  VOL.4、A2–B2、150 题）。

### 2. 翻译层专项
- 讲解/界面语言确为葡萄牙文（欧葡 `tu` 体一致：`Agora és tu`、
  `Envia-nos a tua carta`、`procura o número`、`encontra o teu número`）。
- 核心 221 键：map 文件不在盘上（见观察项 O3），改以结果验证——
  核心↔葡文全文 diff + CJK 字符集差分：葡文版新增 CJK 字符为 0
  （文本与 SVG 皆然），被替换掉的字符全为核心简体中文讲解层；
  逐行核对 379 行葡文行，无一处错译/漏译/他语残留。
- 练习小节头冻结为日语：A 理解、B ことば、C 数字と日付、C 文を作りましょう、
  D ペアにしましょう、D 正しい・正しくない、B グラフ、C 数字と事実、
  D 文を完成しましょう、B 一般問題、スポーツ体育——8 版逐版目视确认；
  题型标签为葡文（Completa / escolha múltipla / Relacionar /
  Constrói uma frase / Verdadeiro ou falso? / Traduz / Escrita）。
- E 组 4 个中文句答案键已译成葡文，逐条核对题干（日文原文）与答案：
  - 137 `二の酉は11月19日です。` → `O Ni-no-tori é a 19 de novembro.`
  - 138 `新酒は11月19日に解禁されます。` → `O vinho novo sai a 19 de novembro.`
  - 139 `流行語のノミネートは、11月5日に発表されました。` →
    `As nomeações para as palavras do ano foram anunciadas a 5 de novembro.`
  - 140 `紅葉を見に行く人は、予報の日付と今の様子を確かめましょう。` →
    `Quem vai ver as folhas deve verificar as datas previstas e a situação atual.`
  4 条均正确，注分别为 `Ver página 2/3/5/6`，与核心对照页一致。
- ちいかわ：一律 `Chiikawa`（P5 正文、ex 67、P7 B1 桥接、ex 106、P8 ex 128、
  答案键 67/106/128），`吉伊卡哇` 全版 0 次；りくりゅう：一律 romaji
  `ryuuryuu`（P7 金句释义、P8 答案键 66/80/105、注 77/105）。
- 其他中文残留：除有意保留的中文原文引用外，无。逐处说明——
  `解禁日` 11 处全为日文正文/题干/译注词头（如金句 2、ex 30/36/38/39 题干、
  `Nota — 解禁日 o dia da saída` 词头）；CJK 字符集差分证明无新增汉字。
- §8.1：译注词头均真实出现在正文里（抽查：P2 威勢よく、P6 決めつける、
  P1 見頃等；词头与核心版相同，核心已过 §8.1）。
- P1 趋势框来源行 `Fontes e datas nos artigos` 单行框内；P7 披露葡文 5 行，
  未编造来信（明确写无来信、VOL.5 刊登）；P7 桥接 `ノミネート nomeação`、
  `〜勝〜敗 vitórias–derrotas`、`金星 kinboshi` 均正确。

### 3. U+2019 缺陷类回归
- 8 个 SVG 中 U+2019 总数 0（逐个 SVG 皆 0）；直撇号 U+0027 亦为 0——
  本版无任何撇号，无宽字形断裂可查。

### 4. 机械门（全套自跑，见 GATE-LOG.md）
- occlusion 审计：0 flags（自检 6 类全触发、干净对照静默），exit 0。
- p8 extract：150/150；p8 compare vs 核心：CLEAN，missing=[]、extra=0、
  uncertain=[]、keydiff 恰为 [137, 138, 139, 140]。
- freeze：构建解释器 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0，
  与 KIT §9 构建命令一致）重跑 run.py，8/8 SVG sha256 与成品逐字节相同。
- run.py 重跑 exit 0，FLOW OVERFLOW / HEAD TOO WIDE 0 次；
  P8-keys 流末 col 3 y=2397（底 2540），与 KIT 一致。
- print/web 文字层：pdftotext 各 46,976 字节，逐字节相同。
- web PDF 4,485,027 字节（< 7 MB）。

## 观察项（不计缺陷）

- O1 — P8 答案键 #81 简析略去题干的 SNS 细节：题干为
  `赤いカエデの写真を、SNSに ___ 人も多いです。`，核心简析
  “把红色枫叶照片上传到SNS的人很多”，葡文简析为
  `Muitos publicam fotos de bordos vermelhos`（未提 SNS）。
  答案键（上げる）无误，释义大意保留；列为观察。
- O2 — P8 答案键 #86 简析机构名泛化：核心简析“按日本气象协会预报……”,
  葡文简析为 `Previsão meteorológica do Japão: Arashiyama 13 nov.`，
  未点出“日本気象協会”（题干本身保留全名）。答案键（A）无误；列为观察。
- O3 — 任务单点名的 `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`
  与 `map-pt.json` 在校对时不在盘上：该目录当时仅含另一 agent 的 ko 文件
  （`.probe-stick8`、`build-ko-stick8-run1.log`、`ko-sha-stick8-pre.txt`），
  未动用。221 键机制改以全文 diff + CJK 字符集差分 + p8 compare 的结果验证
  （结论见 §2），审计链缺源文件一环，非本版内容缺陷。
- O4 — P2/P3/P5 `あなたは？` 框末行（葡文 `envia-nas.`）基线距框底仅约 5px，
  墨迹约 0.1–0.7px 触底边量测值——核心版同位置中文末行亦同（0.5px），
  目视框内，无溢出；不列缺陷。
- O5 — P3/P5/P6 中部栏目留白为核心既有版式（核心 KIT §7 已披露的 W46 模式），
  非 fan-out 引入；不列缺陷。
- O6 — P8 题干 10.35pt（任务单已记录的 adjudication），本轮实测仍为
  10.35pt（79 spans），不动；不列缺陷。
- O7 — P7 ex 107 选项 C `候補に` / `選ばれること` 折行、ex 111/112 题干
  `(4面)` 日文页码标注，均为核心既有形式；不列缺陷。

## 附件（本目录）
- `GATE-LOG.md`：机械门逐项记录
- `gates/`：textdiff-core-pt.txt、pt-p8.json、pt-p8compare.json、
  pt-occlusion.json/.log、rerun-run.log、sha-shipped.txt、sha-rerun.txt、
  s11-grep.txt、u2019.txt、print.txt、web.txt、p2-words-crop.png
- `render-print/`：从印刷 PDF 重渲染的 8 页 PNG；`render-web/`：网页 P1/P8
- `rerun/`：freeze 重跑副本（tools/venv/bin/python run.py，8/8 相同）
