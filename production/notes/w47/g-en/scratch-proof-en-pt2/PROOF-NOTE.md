# PROOF-NOTE — 2026-W47 en-pt（独立复校 proof2 · Q73 delta 后）

- 版：`2026-w47-en-pt`（目标语 English，读者母语 Portuguese）
- 复校员：独立复校员（与建版者/delta agent 非同一人），2026-11-11
- 对象（`production/2026-w47/2026-w47-en-pt/`，开工前盘上 `sha256sum`+`stat` 核对，与任务单先验值逐字一致；收尾复测三件 SHA 未变，见 GATE-LOG §0）：
  - 印刷 `The-Lucerna-VOL4-en-pt.pdf` — 29,345,708 B，SHA-256 `52452731bc5988209215cb8f83548b14a7d1a933953dac09688e7f8d82a3b700`
  - 网页 `The-Lucerna-VOL4-en-pt.web.pdf` — 2,418,222 B，SHA-256 `467068e289700e570c5e2c55a9f6c372dc618a0fb4e8d49ccf277429151b7128`
  - `2026-w47-en-pt.text.md` — 54,120 B，SHA-256 `f85c55cef1cf7fe824fe59f3c9ff97bad8f4938d423bcc737a9afe60fbab7422`
- 核心：`core-en`（fix2 定稿，Q73 键为 up），复核前后未变；盘上 core SVG 8 页哈希与 proof1/delta 所载逐个一致（见 GATE-LOG §3）。
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-pt2/`（`TMPDIR=<scratch>/tmp`；只在 goals 侧写；不 commit、不 push；未修改 production 下任何文件——收尾三件 SHA 与开工一致，`git status` 只显示该目录本就未跟踪）。
- 探针：`/dev/null` 存在 + `git hash-object -w` 成功 + scratch 真实写成功（`tmp/probe.txt`），开工前通过。

## 结论：(a) 定稿零缺陷

Delta 范围经独立核实恰为声称的一处改动；150 题逐项手核零不符；全部机械门通过；8 页逐页目视干净。

### Delta 范围独立核实（与 delta 前状态逐项比对，非采信 delta 自述）

- registry diff（vs `scratch-delta-en-pt/registry-pre.json`）：恰好 1 行，第 583 行 `"key": "speak"` → `"key": "up"`（Q73）。
- text.md diff（vs `scratch-delta-en-pt/text-pre.md`）：恰好 1 行，l.1151 `73. [A2] Completar frases — speak (speak up = falar sem medo)` → `… — up (…)`。
- SVG diff（vs `scratch-delta-en-pt/svg-pre.sha256`）：仅 `svg/p8-test.svg` 变（`1365ad54…` → `d9ce301c…`）；其余 7 页字节一致。P5 不变是正确预期——键只印在 P8，P5 题干 `Speak ___: tell a teacher.` 未改。
- freeze diff 佐证：p8 +106/−100（proof1 为 +105/−99，+1/−1 恰为改动的 1 个键字符串）；其余各页加减数与 proof1 一致。

### Q73 四源一致（delta 键，独立复核）

| 源 | 实测值 |
|---|---|
| registry Q73（`registry.json:579–584`） | `{"n": 73, "page": 5, "level": "A2", "type": "Completar frases", "key": "up", "note": "speak up = falar sem medo"}` |
| text.md l.1151 | `73. [A2] Completar frases — up (speak up = falar sem medo)` |
| P8 印出键（SVG `p8-test.svg`，x=538.5，y=2276.83；p8 extract `"73": "up"`；150dpi 裁片目视） | `73. up`（裁片 `crops/p8-answers-73.png`） |
| P5 题干 + 注释（SVG `p5-youth.svg`，题干 y=1925.1；注释在 Nota 行联接文本中） | `Speak ___: tell a teacher.` + `speak up = falar sem medo`（裁片 `crops/p5-q73-stem.png`） |

另：core-en registry Q73 亦为 `up`，四源与核心一致。`Speak [up]: tell a teacher.`——speak up 为固定搭配，正确。

### 150 题手核（key-vs-stem 逐项读题干，非三源一致性代劳）

- 方法：自写 `fill-audit.py` 解析 `content*.py` 的 `f.ex`/`match_set` 调用（Q1–111，源顺序，与 registry 键 0 偏差）；cloze Q112–119 直接对 `content8.py:29` 段落 + 选项组逐项验算；Q120–132 对 `content8.py` 的 mcq/read_qs 数据表逐项验算；Q133–136 对 `content8.py` d_items；Q137–140 翻译题逐句验算；Q141–144 配对题对定义表验算；Q145–149 对话填空对对话逐空验算；Q150 开放写作题为预期例外（键为说明句）。
- 结果：150/150 键填入题干成句，无一不适配。逐项要点见 GATE-LOG §5（Q1–111 列表在 `fill-audit.txt`）。
- 抽查要点：Q73（上）；Q79 `Children are speaking up this week.`——(speak)→are speaking，up 不动，正确；Q112–119 cloze 逐项唯一适配（Tuesday / call / continues / will meet / writes / will certify / wears / will watch）；Q133–136 `will meet` / `won` / `more` / `whether` 各与题干一致；配对五组（P2 24–27、P3 38–41、P4 56–59、P5 74–77、P8 141–144）字母与定义逐组相符，Q39→a / Q40→d 与 proof1 四方核对一致。
- 既存重复（proof1 (a) 已带、非本次引入）：Q6=Q12（January 同题干同键）、Q2=Q95（call）、Q5=Q96（changed），为跨页/跨级别复用。

### 紧余量记录（紧但装得下，不构成缺陷，均已真墨实测+目视）

- P2 AND YOU? 盒：末行 `para a redação.` 基线 1539.85，0.30em 启发式报 −1.0px；本轮 72dpi 渲染卡真墨复核：墨水最末行 1157 PNG px（=1542.7 SVG），盒底 1158.7 PNG px（=1544.9 SVG），**真墨余量约 +2.2px SVG**（proof1 以全分辨率 cards 卡测得 +0.9px SVG，两法同为正数、同一结论，差值来自阈值与分辨率）；裁片 `crops/p2-andyou-bottom.png` 目视 `p` 下行笔完整在奶油盒内，分隔线在其下。启发式为假警报。
- P6 HOW LONG? 标题：源 advance +8.9px，真墨 +8.5px（与 proof1 同值）。
- P1 THE WEEK IN NUMBERS 标题：源 advance +13.6px，真墨 +13.5px（与 proof1 同值）。
- P1 SEARCHES 盒末行 +6.3px（0.30em 口径）、P2 DID YOU KNOW 末行 +7.9px，均与 proof1 同值，未变。

## 观察（不构成定稿阻碍，报协调员；均为 proof1 观察的延续）

### 观察 1：KIT §6 旧标题行与 §3 字号单位口径仍在（proof1 观察 2/3）
- KIT §6 写 P2 栏头旧文案；KIT §3 “P8 min font 13.5 pt”未注明 SVG 单位（PyMuPDF 实测 10.12pt，≥9.75pt 门通过）。delta 未动 KIT 该两行（任务只要求 delta 条目）。属 KIT 文字问题，不影响版面。

### 观察 2：两处跨栏断行仍在（proof1 观察 4，核心同款结构）
- P5 “D PRESENT CONTINUOUS”栏头 + instruction 前半在中栏底部，后半与 78–81 题在右栏顶部；P7 不规则动词句在左栏底部断开、尾行在中栏顶部。文字完整，无丢失；是否改排版由核心定。

### 观察 3：freeze 口径已按更正执行
- 本轮 freeze 按更正口径跑了两条：标准 `--build core-en` 8/8（核心可自我复现且未被本次改动），以及版 baseline `--build <版目录> --core-svg <版 svg>` 8/8（版自我复现，p8 `d9ce301c…` 与修后 SVG 快照一致）；另以 `sha256sum` 直接复核盘上 core-en SVG 8/8。构建方旧陷阱（build-copy 里装版目录冒充核心）本轮未重犯，但 freeze.log 的 “core” 列在版 baseline 下实为版 SVG 哈希，读数时须认清 `--core-svg` 指向。

### 观察 4：D5 字体（只记录数量，不判）
- `pdffonts`：印版 41 个字体对象、网版 41 个字体对象，全部 embedded + subset；字体族：NotoSansCJKsc（Regular/Bold）、NotoSerifCJKsc Regular、Newsreader（Regular/Italic/Bold）、UnifrakturMaguntia、DejaVuSans。拉丁读者解释层在 Noto Sans CJK SC 是已知待用户裁定的全线问题，不作本版缺陷。

## 已核实无问题的项（全量核对，见 GATE-LOG.md）

- **机械门全绿**：occlusion 0 flags（真实审计，未加 --selftest；core 0，NEW vs core 0）；p8 extract 60/150（与核心同集合），compare CLEAN，keydiff [137, 138, 139, 140, 150]（预期读者语键）；freeze 核心 8/8 + 版 baseline 8/8 + core 只读对照 8/8；freeze diff 新增 CJK 合计 9，全部 U+3000；印/网 token 多重集差分 0/0（layout 与非 layout 口径各 8,862 / 8,879 token；逐页 layout 字节一致 8/8，p8 23,483 B）；网版在 scratch 副本重渲染 2,418,223 B（发货 2,418,222 B，差 1 字节为 fontTools 时间戳），文字层逐字节一致；keycheck 150/150；P8 最小字号 10.12pt（印/网一致）；框题源扫查 12/12、SVG 扫查 18/18 全 fit；creambox canonical 32 盒：inside-only 余量无负值，BELOW-WINDOW 全部为 +24~+37px 的下一栏头/下段正文，P7-TOOLBOX 7 盒最小 desc-clear +41.6px；PNG 条带扫查 23 处启发式旗标全部裁定为下一栏头/下段（与 proof1 同集合），唯一 PNG-SPILL 406px 为 P1 THE WORD OF THE WEEK 栏头字顶；check_s11 ALL PASS；verify_ed ALL PASS（Q39/40、Q46/52/55/125、Ashes 措辞、P8 字号、零真实 CJK 全过）；家具 `tables.py furniture pt` badge/footer/`Página {n} de 8`/`Nota — `/`— Página {n} —` 与 SVG 一致，VOL.4。
- **引号/撇号/禁词**：弯双引号 “ ” SVG 82/82、text.md 81/81，各自成对；« » SVG 2/2、text.md 4/4，成对；无直引号；U+2019 0 处；行首标点 0；禁词（SOP / proofread / geometry audit / cover / lint / placeholder / TODO / XXX / Lorem）可见文本 0；陈旧措辞（`Ashes begin`、`Perth is winning!`、`second week in Perth`、`Confirmado em`、`foram decididos`、旧标题 `THE SENATE, IN NUMBERS` / `SATURDAY, NOVEMBER 21`）0 命中；CJK 仅 U+3000，SVG 可见文本 141 处，text.md 0 处。
- **目视**：印版 8 页逐页渲染目视 + 网版 P1/P8 渲染目视；除紧余量记录的三处外，无溢出、重叠、压页脚、图片与出处问题；P8 答案块 150 键收尾在页脚之上；本轮渲染与 delta 渲染逐页像素对比 8/8 均为 0px（阈值 30），即 delta 后 PDF 与 delta 渲染件同一。
- **工具失误记录**：首轮 `sweeps.txt` 生成脚本漏 import Counter 导致 NameError，未出数；已重跑，CJK/registry/keydiff 结果见 GATE-LOG §10。重跑不影响任何门禁结论。
