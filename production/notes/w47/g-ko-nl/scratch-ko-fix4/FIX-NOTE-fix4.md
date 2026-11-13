# W47 KO core — 第四轮返修工作记录（fix4，run 10，2026-11-11）

> 返修 builder（叶子，未再派 subagent；与 builder、第一至四轮校对员、fix3/fix3b builder 均不同人）。
> 任务：按第四轮复校笔记（`hidden_files/w47/scratch-proof-ko4b/PROOF-NOTE.md`）修缺陷 1–4。
> **结论：4 项全部修完。** 缺陷 1 诊断已钉死（见 §0，Pillow 版本差，非字体文件漂移）、
> 环境锁定后重验为真 8/8（run 10 前，源码未动）；缺陷 2 KIT freeze 表述已按实测改写；
> 缺陷 3 ABSTRACT 三处去空格；缺陷 4 P4 「D 짝 맞추기」标题已随内容移入第 3 栏。
> 整期重建（run 10）+ 全套机械门见 §5；P2/P4 外其余 6 页 SVG 与 run 9 逐字节同。

## 0. 开工探针与成品核对（先于一切动手）

- 写探针（两次皆通，才动手）：`git hash-object -w`（weekly-git 内，stdin，返回 `d32b752b…`，rc=0）；
  真实文件写 `scratch-ko-fix4/work/probe.txt` 成功。前几棒遇到的 Disk quota 写失败本轮未复现；
  `df` 显示 /home 仍有 53G 可用。注：任务书称 scratch-ko-fix4「已有 check2.py」——实测该目录
  根本不存在（新建），全 goal 树下也无 ko 专用的 check2.py（仅 zh-cn 等他语种的有）；
  本轮自写核查脚本（见 §5），未沿用他语种的 check2.py。
- 成品核对（动手前）：印刷版 `Lucerna-VOL4.pdf` 46,232,133 字节、SHA-256 `48c2fa98…`；
  网页版 `Lucerna-VOL4-web.pdf` 4,232,753 字节、SHA-256 `c0309268…`；
  text.md 26,014 字节、SHA-256 `81ebd0a3…`——与任务书逐项一致。

## 1. 缺陷 1 诊断：freeze 0/8 的成因（已钉死：Pillow 版本差，不是字体文件漂移）

### 1.1 现象复述
- run 9 构建（2026-11-11 00:07 UTC）的 shipped SVG 哈希为 c47bc434…/8619ec50…/…；
  此后三次独立重建（fix3 freeze-run8 23:56、fix3b freeze-run9 00:24、第四轮校对 freeze 00:49）
  产物逐字节相同（f6547a83…/cef2d804…/…），但与 shipped 全部不同——工具自报 0/8。
  两次重建产物彼此相同 ⇒ 当前环境下重建是确定性的，差异不是随机性。

### 1.2 排除项（有证据）
- **字体文件未变**：`/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc`
  SHA-256 `93069d8e…`、Bold `9d3c0d76…`；`dpkg -V fonts-noto-cjk` 零输出（rc=0），
  即文件与已安装包（1:20230817+repack1-3）的元数据一致；文件 mtime 全是 1970-01-01
  （镜像构建产物，无信息量）。无任何字体重装记录：`/var/log/dpkg.log` 仅有
  2026-11-11 01:26 两行 `startup packages configure`，`/var/log/apt/` 根本不存在。
- **VM 重启不是成因**：本机 boot 时间 2026-11-11 01:25:23 UTC（`uptime -s` / `who -b`），
  在全部 0/8 重建（23:56、00:24、00:49）之后；且重启后本轮重建仍复现同一组哈希，
  说明漂移在重启前就已存在、且跨重启保持。
- **venv 未动**：`tools/venv` 的 PIL .so 文件 mtime 均为 2026-10-22（venv 建于 10 月 22 日）。

### 1.3 锁定成因：构建与 freeze 用的 Python/Pillow 不是同一个
- 本机有两个 Pillow：系统 `/usr/bin/python3` 带 **PIL 10.2.0**，`tools/venv/bin/python`
  带 **PIL 13.0.0**（其 `_imagingft` 链接 wheel 自带的 `libfreetype-…so.6.20.6`，
  即 FreeType 2.14 系；系统 libfreetype6 为 2.13.2）。
- 直接实测（同一字体文件、同一 KR 面、同一字符串，40px）：
  - `NotoSerifCJK-Regular.ttc` index=1，「삼성 라이온즈가 12년 만에 한국시리즈 우승을 차지했어요」：
    系统 PIL 10.2 `getlength` = **991.296875**；venv PIL 13.0 = **1002.15625**（宽 ~1.1%）。
  - Sans 同串两边同为 393.296875——漂移不在 Sans，而在 Serif 度量（断行正由 Serif 韩文决定）。
- 历史佐证：freeze-run4 与 freeze-run6 均为工具自报 **8/8**（逐文件 OK 行俱全，
  `freeze6/svg/` 的重建产物哈希与当时 shipped 一致），0/8 首次出现于 fix3 的
  freeze-run8（23:56）——即 run 7–9 的构建改用了系统 python3（PIL 10.2），而 freeze
  始终用 venv python（PIL 13）重建。fix3b 的 freeze-run9（00:24）`svg/` 里
  **已经**是漂移产物 f6547a83…——漂移在第四轮校对之前就已存在，不是校对轮引入的。

### 1.4 定路线：锁定 run 9 构建环境，不在当前环境（venv PIL 13）重建
- 决断性试验（源码未动，run 10 前）：`/usr/bin/python3 tools/freeze.py baseline`
  （即以系统 python3 / PIL 10.2.0 重建），工具自报 **8/8 SVGs byte-identical**，
  逐文件 OK，产物就在 `freeze-syspy/svg/`（直接 sha256 比对，`freeze-syspy.log`），
  且 `core integrity` 行确认 shipped SVG 未变。P2 FLOW OVERFLOW 只出现在 PIL 13
  重建里，PIL 10.2 重建的构建日志干净（run 9 日志同样 0 警告）——溢出是度量变宽的
  派生物，不是源码问题。
- 因此本轮全部构建（run.py、check_core.py、check_gloss.py、textmd.py）一律用
  **`/usr/bin/python3`（PIL 10.2.0）**；渲染（render.py）与 webpdf 需要 venv 才有的
  cairosvg/fontTools，仍用 `tools/venv/bin/python`（渲染不依赖 PIL 度量——SVG 已定稿，
  CairoSVG 只做光栅/矢量化；且 run 9 的渲染同样走 venv，见 render-run9.log）。
  KIT 中「环境锁定」已写入复现命令（见 §6）。

## 2. 缺陷 2：KIT 的 freeze 8/8 表述失实（已改写；Round 5/6 已审计）

- 失实处：KIT「Mechanical gates」节 run 9 行与 Round 9 记录行（原 line 81/110）。
  fix3b 称「直接 sha256 比对 build-copy 8/8」——比的是 `shutil.copytree` 的副本，
  其 mtime 仍是 run 9 构建时间 00:07:15–00:07:30（本轮复核 `freeze-run9/build-copy/svg/`
  的 mtime 与哈希：哈希 = shipped 哈希，前缀 c47bc434…，因 copytree 保留 mtime 且
  从未被重建覆写——重建产物实际写在 `freeze-run9/svg/`，哈希 f6547a83…，与 shipped 全异）。
  工具自报的 0/8 才是真实结果；「副本 mtime 00:07，确为本次运行新写」一说不成立。
  **fix3b 的 "freeze 8/8" 不可采信，本轮未引用。**
- Round 5/6 审计（任务要求一并核查）：**Round 5/6 的 "freeze 8/8" 不是同一比对路径，
  是真实的。** 证据：`freeze-run6.log` 工具自报 8/8 且逐文件 OK，
  `freeze6/svg/` 的 8 个重建产物哈希（9bd57ce3… 等）与当时 shipped 一致；
  `freeze-run4.log` 同样逐文件 OK（Round 1 的 "freeze 8/8" 亦然）。
  Round 5 本人无单独 freeze 日志（fix2 目录只有 freeze-run6.log），但 KIT Round 6
  载明 run 5→6 构建日志逐字节相同（仅去括号一处文字改动、零版式影响），故 run-6
  freeze 覆盖 run-5 的 SVG。结论：只有 run 9 的 freeze 表述失实，已改写（见 §6）；
  Round 5/6 表述保留，并在 KIT 增加审计注，说明其证据链与 run 9 的不同。
- 改写后的真实结果（run 10，见 §5）：锁定环境（系统 python3）下 freeze baseline
  **8/8**（工具自报，逐文件 OK，产物在 `freeze-run10/svg/`——重建产物与
  shipped SVG 逐字节同，包括因缺陷 4 改动的 P2 与 P4）；其余 6 页与 run 9
  逐字节同，P2/P4 系有意改动；freeze diff run9→run10 全 8 页 +0/−0 字符串、
  CJK 增 0。另：venv python 跑 freeze 仍自报 0/8（对照试验，产物仍是
  f6547a83… 组，`freeze-run10-venv.log`；P2 产物因改动变为 997ef89f…）——
  这是解释器不匹配的已知现象，不是门禁失败；KIT 已注明为 control。

## 3. 缺陷 3：ABSTRACT.txt 数字带空格残留（已修）

- 改动（纯文本，SVG/PDF/text.md 不受影响——core-ko 的 *.py 均不引用 ABSTRACT.txt，
  已 grep 核实）：
  - 「泡菜成本 199,456 韩元」→「199,456韩元」
  - 「三星 12 年后重夺」→「12年后」
  - 「150 道练习题」→「150道练习题」
- 核实：四种模式 `12 年后` / `199,456 韩元` / `150 道` / `11 月` 在 ABSTRACT.txt 中
  均为 0 次；全文残留的数字+空格仅 D-3 / A2 / B2 三处代号（词间分隔，第四轮已裁定不计）。

## 4. 缺陷 4：P4「D 짝 맞추기」标题孤悬第 2 栏底（已修）

- 成因：`Flow.head` 只保证标题自身 82px 能塞进栏尾（`_fit(h+30)`），不管后随的
  match_set（362px）——C 节结束时第 2 栏只剩 91px，标题塞得下、内容塞不下，
  `match_set` 的 `_fit(362)` 把内容推去了第 3 栏。
- 修法（标题随内容移栏，不动文字、不调栏宽）：
  - `bslib4.py` 新增 `Flow.keep(h)`：若 h px 在本栏余量内放不下且不是末栏，
    先进下一栏（keep-with-next）；`match_set` 增可选参数 `head=None,
    head_size=25, head_gap=13`，按自身绘图公式算出标题+内容总高，先 `self.keep(总高)`，
    再 `self.head(...)` 画标题。
  - `content34.py` P4 D 节：删掉独立的 `e.head("D　짝 맞추기")` 一行，
    给原地内联的 `match_set` 调用加 `head="D　짝 맞추기"` 参数（D2，键 d/a/c/b）。
    P3 的 D 节（content34.py:113）未动——第四轮未报其孤悬，`flow[P3-ex]` 正常收尾。
  - 绕走的弯路（已回滚，记录在案）：最初把 4 项左/右列抽为模块级 `_d_lefts` /
    `_d_rights` 列表并在内容区另调 `e.keep`——textmd.py 会把模块级 Assign
    List/Tuple/Dict 字面量收进 text.md，结果 text.md 从 333 项涨到 338 项
    （哈希 `a12d12d0…`）；同期一次 textmd 调用还误传了带前导 `# ` 的标题，
    产生了 `# # …` 行。教训：textmd 只收集 (a) 接收者为 `p`/`f` 的 CALL_ARGS
    位置参数（`e.head`/`e.match_set` 不收），(b) 模块级 Assign List/Tuple/Dict
    （OUT 除外）。调用参数里的字面量是安全的——最终方案把标题作为 kwarg
    传进原调用，text.md 回到 333 项、哈希 `81ebd0a3…`（与 run 9 逐字节同）。
    回滚后重构验证：P4 哈希未变（`4b18a1d9…`，几何同），证明两版实现等价。
- 验证 P4：重建后标题 `<text x="989.0" y="1641">D　짝 맞추기</text>`（第 3 栏顶），
  第 2 栏已无该标题；4 项内容同在第 3 栏（x=989，y=1731–1842），右列 a–d
  y=1887–2001；第 2 栏 y=2400 以下只剩 C 节末项 60；P4-ex 流收尾
  col 2/3 y=2053（原 2002，+51 = 标题占位）；其余流收尾与 run 9 逐字节同（见 §5）。

### 4b. 同类缺陷：P2「D 짝 맞추기」标题同样孤悬（自查发现，第四轮漏报）

- 8 版目视 + 全版孤悬标题几何扫描（全部 size-25 橄榄粗体 sans 标题，8 页）发现：
  P2 D 标题在 (989, 2262.75) 第 3 栏，其下该栏**零**文字；内容 25–28 项全在
  第 4 栏（x=1439.5，y=1936–2047）。run 9 即已如此；第四轮称「仅 P4 D 孤悬」，
  此处漏报。全 8 页扫描仅此一处孤悬（P4 D 修后其下 11 行文字；其余标题均有内容；
  P7 无 size-25 标题，不同版式）。
- 修法与 P4 完全相同：`content12.py:291` 删独立 `e.head`，给 P2 的 `match_set`
  （A2，键 d/a/c/b）加 `head="D　짝 맞추기"` 参数。改后标题在 (1439.5, 1897)
  第 4 栏顶、紧贴其内容上方；第 3 栏的标题已消失；P2-ex 流收尾 col 3/3 y=2309
  （原 2258，+51 = 标题占位；第 4 栏内内容下移 52）。
- 超出四项清单仍修的依据：与缺陷 4 同一缺陷类（「标题与内容同栏」原则），
  在任务要求的 8 版目视中发现；user 立规「自己看出问题自己修」「没做好的就重做」。
  计为修复 #18（与 P4 D 的 #18 同条，见 KIT 修复日志）。

## 5. run 10 整期重建 + 全套机械门（最终成品，2026-11-11）

- 构建（系统 python3，PIL 10.2.0）：`run.py` → `build-run10.log`；与 run 9 的日志
  diff 仅 2 行（P2-ex 2258→2309；P4-ex 2002→2053）。**0 FLOW OVERFLOW / 0 HEAD TOO
  WIDE**。TOTAL 150（A2 51 / B1 72 / B2 27；逐页 10/18/18/18/18/18/12/38）。
  模型字数 169。
- SVG 哈希（run 10）：p1 `c47bc434…` 同；p2 `faf9e3c530f200b1…` 变；p3 `b447a559…` 同；
  p4 `4b18a1d9b3c2f8dc…` 变；p5 `09f7fc23…` 同；p6 `d45b0355…` 同；p7 `e6908156…` 同；
  p8 `e88f7d42…` 同（`svg-hashes-run10.txt`）。text.md 回到 333 项、哈希 `81ebd0a3…`
  （与 run 9 逐字节同）。
- 构建共跑了 3 次（初建 → 渲染/webpdf；实现重构后重建 → P4 哈希同为 `4b18a1d9…`，
  证明重构几何等价；P2 修后第三建）。日志以同一批 run-10 文件名覆写保存。
- 渲染（venv render.py）+ webpdf（venv `tools/webpdf.py`）：最终印刷版
  `Lucerna-VOL4.pdf` **46,232,169 字节**、SHA-256
  `7b004b36066254d7e1e25e92fb81c39428df36a28af182c2b1ad2ab1545aeb5e`；
  网页版 `Lucerna-VOL4-web.pdf` **4,232,790 字节**、SHA-256
  `e9c1ca0ce22d31ed36ee70469a839ed09f7eca60e1bbd05a6b179b5dc818fbfa`，
  9 页内嵌字体、49,379 文本字节。注：webpdf 产物逐次运行有 3 字节级差异
  （4,232,772 → 4,232,775 → 4,232,790；字体子集排序/种子所致），但文本层恒为 49,379
  字节——产物不逐字节稳定，文本层稳定。
- freeze（锁定环境，系统 python3）：`freeze-run10.log` **8/8**（产物在
  `freeze-run10/svg/`）；freeze diff run9→run10 全 8 页 +0/−0 字符串、CJK 增 0；
  venv 对照 `freeze-run10-venv.log` **0/8**（产物仍是漂移组 f6547a83…；P2 产物
  997ef89f…），预期现象，见 §1。
- 其余门（均以最终成品重跑）：
  - `occlusion_audit.py`：venv 与系统 python3 各 **0 flags**（selftest OK，6 类全触发；
    注意该工具内部用 PIL ImageFont/getlength 度量，故对解释器敏感——两边一致为 0）。
  - `tools/p8.py extract`：**150/150**；`compare`（core 对自身）：**CLEAN**
    （missing=[] extra_count=0 keydiff=[]）。
  - `check_core.py`（系统 python3）：gloss fails 0，P7 短语 8/8 原样，orphan issues 0，
    日期全对；日志与 run-9 日志 diff 完全相同。`check_gloss.py`：10 项，
    日志与 run-9 日志逐字节同（故亦与 run 6 同）。
  - 文字层：印刷版与网页版各 49,379 字节，`cmp` 通过；run9→run10 非空白字符多重集
    相同（+3 字节仅为 pdftotext 换行位置）。
  - P8 字号（PyMuPDF，印刷版）：答案区（y≥976.5pt）162 spans，最小 **9.975pt**
    （158 个 9.975pt + 4 个 12.75pt），≥ SOP 下限 9.75pt；P8 SVG 与 run 9 逐字节同，
    故字号恒同。
  - 150 键逐题验算（新 extract vs 第四轮已验 `p8-keys.txt`）：149/150 键部逐字同；
    仅第 150 项为解析器格式差（proof 保留整注「✓ 范文见本版 H 区（169字）」，
    `p8.py` 的 `keys` 只返回 bare 「✓」；注文本已由 grep 在 P8 SVG 中确认存在）。
    D 组：61→c、62→d、63→a、64→b；133–136 句皆同；40→11、43→b、124→B。
    键的正确性继承第四轮独立 150/150 验算（P8 SVG 逐字节同；P1–P7 文字多重集不变）。
  - 孤悬标题重扫：**0 处**（见 §4b）。
- 目视（`pdftoppm -r 100`，最终印刷版 + 网页版 P1/P8）：
  - P1–P4 首版渲染已目视（见初版记录）；P5–P8 首版渲染已目视（见初版记录）；
    最终渲染的各页 PNG 与首版逐字节比对：仅 P2 变化，其余 6 页同（`final--*.png`，
    哈希比对记录在本节末尾文件清单里；P2 最终版重读：D 标题与 25–28 项 + a–d
    同在第 4 栏，无溢出/重叠/页脚侵入/豆腐块）。
  - P4 最终 PNG 与已目视版逐字节同（D 标题与 61–64 项同在第 3 栏，梯形图、照片、
    日历均无问题）。
  - 网页版 P1/P8 最终 PNG 与首版逐字节同，已目视：P1 刊头/蛾/下拉首字/照片/页脚
    俱全；P8 答案区完整，第 150 项注「✓ 范文见本版 H 区（169字）」在版。
- **本轮自查结论：零问题。** run-10 成品待第五轮独立复校（见 §6）。

## 6. KIT 改写 + 文件清单

### 6.1 KIT（`core-ko/WEEKLY-KIT.md`）改写
- 「Measured exercise counts」标题 run 9 → run 10；P8 字号行改写为「P8 SVG 横跨 run 8/9/10
  逐字节同，run-10 重测 9.975pt」。
- 新增 Round 10 记录（第四轮 4 缺陷、环境锁定、逐门结果、8/8 freeze、待第五轮复校）。
- Round 9 记录的 freeze 表述订正为失实（工具自报 0/8，8/8 是比对 copytree 副本所得；
  详见 §2）。
- 修复日志新增 #15（缺陷 1 环境锁定）#16（缺陷 2 KIT 订正 + Round 5/6 审计）
  #17（缺陷 3 ABSTRACT 余项）#18（缺陷 4 P4 D + P2 D 同类）。
- Mechanical gates：freeze 条目全改写（锁定环境真 8/8 + 历史订正 + venv 0/8 control 注），
  p8 条目（run-10 日志、compare CLEAN、150 键逐题比对）、occlusion 条目（双解释器 0 flags）、
  check_core/check_gloss 条目（run-10 日志）、文字层条目（49,379 字节）、渲染目视条目
  （run-10 8 页 + 网页 P1/P8、孤悬重扫 0）。
- Output files：run 10 的印刷版/网页版字节与 SHA、文字层 49,379 字节、text.md 不变、
  ABSTRACT 去空格注。
- Open verification debts：第四轮复校 2026-11-11 已完成（缺陷 1–4 → run 10 修完）；
  run-10 成品待第五轮独立复校。
- Round 1/5/6 的 "freeze 8/8" 行原样保留（已审计为真，见 §2；Round 5 覆盖于 run-6 freeze）。
- 红线遵守：只改 core-ko/ 与本 scratch 目录；未碰 W43/W45/W46、其他目标语、
  `tools/p8.py`、`tools/freeze.py`；未跑 insert.py / lint --write / git push / add / reset
  / stash；未提交。

### 6.2 本轮改动文件（core-ko 内）
- `ABSTRACT.txt`（§3：三处去空格）
- `bslib4.py`（`Flow.keep` + `match_set` 的 `head` 参数）
- `content34.py`（P4 D：`head="D　짝 맞추기"` kwarg）
- `content12.py`（P2 D：`head="D　짝 맞추기"` kwarg）
- `WEEKLY-KIT.md`（§6.1）
- 其余 core-ko 文件未动。印刷版 / 网页版 PDF 与 SVG 为 run 10 构建产物（见 §5）。

### 6.3 scratch-ko-fix4 文件清单
- `FIX-NOTE-fix4.md`（本文件）
- `work/probe.txt`（开工探针）、`work/pg--1..8.png`（首版 run-10 渲染 8 页）、
  `work/webpg1-1.png` / `work/webpg8-8.png`（首版网页 P1/P8）、
  `work/final--1..8.png`（最终印刷版 8 页）、`work/final-web1-1.png` /
  `work/final-web8-8.png`（最终网页 P1/P8）
- `build-run10.log` / `textmd-run10.log` / `render-run10.log` / `webpdf-run10.log`
- `svg-hashes-run10.txt` / `freeze-run10.log` + `freeze-run10.json` +
  `freeze-run10/svg/`（锁定环境 8/8 产物）/ `freeze-run10-venv.log` +
  `freeze-run10-venv.json` + `freeze-run10-venv/svg/`（对照 0/8 产物）
- `freeze-syspy.log` + `freeze-syspy.json` + `freeze-syspy/svg/`（修前锁定环境
  8/8 决断性试验，源码未动）/ `freeze-diff-run9-run10.log`
- `print10.txt` / `web10.txt`（最终文字层，各 49,379 字节）
- `p8-extract-run10.json` + `.log` / `p8-compare-run10.log` / `p8-keys-run10.txt`
- `check-core-run10.log` / `check-gloss-run10.log`
- `occlusion-run10.log` + `.json` / `occlusion-run10-syspy.log` + `.json`
- `text-run9.md`（run-9 text.md 副本，供比对）

### 6.4 待办（本轮外）
- run-10 成品的第五轮独立复校（协调员派员；不在本轮Builder职责内）。
