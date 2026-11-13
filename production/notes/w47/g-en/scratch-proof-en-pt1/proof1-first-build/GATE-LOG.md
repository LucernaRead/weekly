# GATE-LOG — 2026-W47 en-pt proof1（独立复校机械门）

复校员：独立复校员（与建版者非同一人）。日期：2026-11-11。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-pt1/`
（`TMPDIR=<scratch>/tmp`；/tmp 未写。探针：`git hash-object -w` 成功 + scratch 写文件成功。）

## 0. 对象核对（开工先验）

| 文件 | 字节 | SHA-256（完整） | 任务单 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-pt.pdf` | 29,345,286 | `50484ca9c0ef23231977066164281455491180ef7843efc8d266805cdcc5ce0e` | 前 16 `50484ca9c0ef2323` ✓ |
| `The-Lucerna-VOL4-en-pt.web.pdf` | 2,381,728 | `c150c65509fa722ef17d54f0c823878c7f958fcca6aaaae879e10c36e7430071` | 前 16 `c150c65509fa722e` ✓ |
| `2026-w47-en-pt.text.md` | 53,549 | `329a027375eda3fe73abf2ed27819456abb8a57ad4849ec3e342db6632d004ba` | 前 16 `329a027375eda3fe` ✓ |

核对方法：盘上 `sha256sum` + `stat`；与 KIT §2 所载 SHA 亦逐字一致。两 PDF 各 8 页（`pdfinfo`）。

## 1. 遮挡审计 `tools/occlusion_audit.py` — 0 flags ✓

- 自检：`--selftest` OK（6 类 planted flags 各命中 1 次，clean 对照静默）。
- 本版：`occlusion_audit.py ../production/2026-w47/2026-w47-en-pt --core ../production/2026-w47/core-en --json occlusion.json`
  → `0 flags`；core `0 flags`；NEW vs core `0`。退出码 0。
- 盲区说明：该审计不检“盒内文字漫出盒底”（文字未被遮盖）。此类缺陷由第 6 门 creambox 全版扫查覆盖，见第 6 节（查出 P2 一处，核心级）。

## 2. P8 `tools/p8.py` — extract 60/150，compare CLEAN ✓

- extract（本版 p8-test.svg，total 150）：`noted set = 60 of 150`（与核心同集合），
  集合 `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]`（`p8-extract.json`）。
- compare（`--core-p8 core-en/svg/p8-test.svg --edition-p8 …/p8-test.svg --total 150`）：
  `core 60 noted / edition 60 noted / status: CLEAN / missing=[] / extra_count=0 / uncertain=[] / keydiff=[137, 138, 139, 140, 150]`。
  注：`--core-dir/--edition-dir` 形式因工具按 target 推导 p8 文件名（en→`p8-exercices.svg` 不存在）而报错，改用显式 `--core-p8/--edition-p8` 路径重跑通过（工具文件名推导问题，已记入 KIT §10 工具 note 的同类项）。
- keydiff 逐项说明（均属预期、非缺陷）：
  - 137：翻译键。核心 “Os democratas venceram a Câmara e o Senado.” 的中文对应为 “民主党赢得了众议院和参议院。”——读者语译文不同，键义同（“The Democrats won the House and the Senate.”）。
  - 138：同上（“A apuração continua.” / “计票继续。”）。
  - 139：同上（“O novo Congresso se reunirá em janeiro de 2027.”）。
  - 140：同上（“Quebre o silêncio.” / “打破沉默。”）。
  - 150：开放写作题。核心为中文“开放题 — …”，本版为葡语 “Questão aberta — veja os pontos no quadro de redação; o modelo está no quadro desta página (Pontua-se por pontos)”；破折号体，`detect_note` 可识别（KIT §5 第 1 条 es 教训已处理）。
- **注意**：p8.py compare 只比对“集合相等 + 有注键的键值”，Q39/Q40 的互换错误两边（核心与本版）完全一致，故 compare 仍报 CLEAN——该缺陷由人工逐题核对发现（见 PROOF-NOTE 缺陷 1），不在 p8.py 的检出范围内。

## 3. freeze `tools/freeze.py` — baseline 8/8，diff 仅 U+3000 ✓

- baseline（`--build core-en`，出到 `freeze-baseline/`）：重渲染 8/8 SVG 与发货核心 SVG sha256 **逐字节一致**（p1 31aa7fb85345ea87、p2 1197d8db0b376c8d、p3 efb83ce76688554b、p4 4290f464ea92fecb、p5 cc255d287f24db27、p6 6236f2766f290dd4、p7 1677d47db03231a2、p8 a5ad8d607c21c182；已逐个比对），核心 SVG 重哈希无改动。
- diff（core-en SVG vs en-pt SVG，`freeze-diff.json`）：各页增减字符串均为讲解层替换；**新增 CJK 字符合计 9，全部为 U+3000 全角空格**（p1 2、其余每页 1）；删除的 CJK 为核心中文讲解层。符合 en×pt 的换语预期。

## 4. 印/网文字层同一 — token 多重集差分 0/0 ✓

- `pdftotext -layout` 两版：印版 106,905 字符、网版 106,909 字符（差 4 字符为排版空白），token 各 8,753、distinct 各 2,513；
  **print−web 0 token，web−print 0 token**。两版各 8 页。
- 网版 P1/P8 渲染（`pdftoppm` 72dpi，`web-p1-1.png` / `web-p8-8.png`）目视与印版卡一致，无豆腐块、无缺字。

## 5. keycheck（150 题键核对，复校员脚本 `keycheck2.py`）— 150/150 ✓（除 PROOF-NOTE 缺陷 1 的键值错）

- text.md 答案区解析：150 行唯一题号，无缺号、无重号。
- 与 `registry.json` 逐题比对：key 0 不符、level 0 不符、type 0 不符（第一版脚本曾因正则 `[AB]2` 误写漏采 B1 行，已修正为 `[AB][12]` 并重跑；该漏采为脚本 bug，不是文件问题）。
- 各页题数：P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39，合计 150；级别 A2 62 / B1 66 / B2 22；与 KIT §1 一致。
- 答案内容逐题验算（MC 41 + 图表读数 6 + 快问 4 的键控选项；配对 5 组以 SVG 印刷字母核对；填空/转换/完形/对话/翻译逐题对题面与正文）：
  全部正确，**唯 Q39/Q40 互换**（PROOF-NOTE 缺陷 1；键值本身在 registry 与 text.md、P8 印刷三处一致地错，故 keycheck 的一致性比对不能发现，靠人工对题面发现）。

## 6. creambox 全版扫查（P7 工具盒清除量 + 全部奶油盒）— 查出 P2 一处（核心级）

- **说明：`tools/creambox.py` 在仓内不存在**（`find` 全仓 + workspace 均无；`tools/README.md` 亦无此工具）。本复校员在 scratch 内自写等价扫查两版：
  - `creambox.py`：32 个奶油盒（#f0eee5）的 PNG 盒底像素带 + SVG 盒底下 40px 内文字；
  - `creambox2.py`：每盒“最后一行行内基线 + 0.30em 下行余量”与“盒底下 45px 内续行 + 前行是否断句”。
- **P7 工具盒（任务必查项）干净**：盒 `x=1439.5, y=651, w=422.5, h=357.21`，底边 1008.21；末行 `apuração vai mudar de novo.` 基线 y=959.68，下行余量 42.1px；盒底带（bottom+1..+10）暗像素 0；裁片 `crop-p7-toolbox-bottom.png` 目视干净。下一栏头 READERS' CORNER 在盒底之下 37px，属正常栏距。
- **全版 32 盒裁定**：其余 31 盒的盒下续行均为下一栏头（+35~37px 标准栏距）或下一段正文，无盒内句子跨底。唯二须说明：
  - **P2 DID YOU KNOW? 盒（缺陷，核心级）**：末行 `November 3.` 基线 y=1171.08，盒底 1158.4 之下 12.7px；前行 `one of them was on the ballot on` 行内余量 11.4px，句子在盒底处断开；裁片 `crop-p2-sayit-bottom.png` 目视确认该行在盒外白地。核心同盒同坐标。
  - **P1 SEARCHES 盒（观察）**：葡语行 `Interesse relativo, não números exatos.` 基线 y=1274，盒底 1256 之下 18px；核心同位置为中文行（同 y=1274）。读作盒下 caption，无断句，核心同款。
  - P2 AND YOU? 盒曾报下行余量 −1.0px（0.30 系数保守估计）：像素核查末行墨水最末行 y=1516，盒底 1517.9，**无墨水出盒**，不算缺陷。
- 扫查脚本与裁片均在 scratch 内（`creambox.py` / `creambox2.py` / `crop-p*.png`）。

## 7. P8 最小字号 — 10.12pt（PDF 实测），≥ 9.75pt 下限 ✓

- PyMuPDF（tools venv）实测：印版与网版 P8 最小字号均为 **10.12pt**（答案块，`LucernaNotoSansCJKSC-Reg`）；全版其余各页最小 11.62pt。
- 换算：SVG 设定 13.5 单位 × 0.75（1950px→1462.5pt）= 10.125pt，与实测一致。SOP §1.1 下限 9.75pt 为 PyMuPDF 口径，10.12 ≥ 9.75，门通过；KIT 所写 “13.5pt” 未注明是 SVG 单位（见 PROOF-NOTE 观察 3）。

## 8. boxtitle 宽度 — 真墨全部装得下 ✓（KIT 数字不可复现，见观察 2）

- 真墨实测（渲染 PNG，墨 vs 框界；记录见 `boxtitles.txt`）：
  THE SENATE 403px 余 1.0px；ODD SOCKS 402px 余 1.5px；SATURDAY 401px 余 3.0px；HOW LONG? 395px 余 8.0px；THE WEEK IN NUMBERS 余 17.5px；THE CALENDAR 余 88.5px；COMING SOON 余 112px；HAYMITCH'S GAMES 余 59px；WHY PERTH? 余 73px；A PRACTICE BALLOT 余 80px；THE TOOLBOX 余 77px；SPEAK UP 余 175px；MODEL 余 666px；P7 各栏头（ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER / NEXT WEEK / GOLDEN SENTENCES / THE DRILLS）余 38–139px。
- 三个最紧的（1.0 / 1.5 / 3.0px）已目视，字未碰框线；occlusion BOXTITLE 亦 0 flags。
- KIT §4 的宽度数用 `svglib.text_w(…, True, 23)` 复测不符（serif：THE SENATE 462.5、SATURDAY 432.5；sans：425.8、397.0；KIT：408.4、379.4），且三题实际字号为 25/28pt 而非 23pt。版式无问题，KIT 口径待补。

## 9. 全文通读 + 目视

- `2026-w47-en-pt.text.md` 全文 1,306 行通读；8 张印版卡逐页目视；网版 P1/P8 渲染目视。
- 弯引号 “ ” 81/81 成对（每页各自成对）、« » 4/4、无直引号；撇号 ASCII（构建归一化，与核心一致）。
- 禁词 0（可见文本；SOP / proofread / geometry audit / cover / lint / placeholder / TODO / XXX / Lorem / 桥接）。
- 家具：`tables.py furniture pt --target en --week 2026-W47` 输出与本版 badge / footer / `Página {n} de 8` / `Nota — ` 逐字一致，VOL.4。
- ABSTRACT.txt：一行葡语、无 ASCII 双引号、含真实主题与题数。
- 图片 8 张：PD/CC0，`assets/CREDITS.md` 逐张有作者与来源（football1910.jpg 未使用，随复制留存）。
- 外部事实逐项网核：I'm a Celebrity、Anti-Bullying Week、Hunger Games、Ashes、ATP Finals、英超、World Children's Day 均与权威来源一致；星期与算术全对（详见 PROOF-NOTE）。

## 10. 结论

- 机械门：遮挡 0、P8 CLEAN、freeze 8/8、印网 0/0、keycheck 150/150、creambox（除 P2 一处外）清、P8 字号过、框题装得下——**全部通过**。
- 人工核对：查出 **2 项核心级缺陷**（Q39/Q40 答案互换——严重；P2 DID YOU KNOW? 末行出盒——轻微）+ 4 项观察。en-pt 讲解层本身零缺陷。
- **本版暂不能定稿**：待核心修复上述两项并重渲染后，fan-out 重跑、本复校员再做一轮全量 proof1（SOP §8.4）。
