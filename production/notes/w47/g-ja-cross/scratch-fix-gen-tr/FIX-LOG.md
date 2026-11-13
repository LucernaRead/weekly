# FIX-LOG — gen_tr.py 工具盒 pad 假值修复（W47 de 家庭生成器）

- 日期：2026-11-11。执行者：gen-tr 机制修理工（叶子，不派 subagent）。
- 范围：只修 `hidden_files/w47/scratch-fanout-de/gen_tr.py` 的 TB_NEW 两处（pad 90→110 +
  假注改写）；在自有 scratch 目录重生成 8 语 tr 文件并与 live 逐行 diff；nl/ru/pt rail-up
  只设计、不上线。**不改任何已定稿的版、不 commit、不 push。**
- Scratch：`hidden_files/w47/scratch-fix-gen-tr/`（本日志 + `regen/` 重生成件 +
  `regen/gen_tr.py` 修后副本 + `regen/tr_en.py` / `regen/vals_*.json` 重生成源数据副本 +
  `probe.txt` + `tmp/`）。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` rc=0；
  真实写文件探针 OK。全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。

## 0. 先读结论（已盘验事实）

- 协调员 brief、`scratch-fix-de-toolbox-family/FIX-LOG.md`、de-es fix1（`scratch-fix-de-es1/FIX-LOG.md`）、
  de-pt（`scratch-fix-de-pt-toolbox/FIX-LOG.md`）、de-zh-tw（`scratch-fix-de-zh-tw-toolbox/FIX-LOG.md`）
  已读。de-es/de-pt/de-zh-tw 的 proof2/proof3 笔记中**未找到**工具盒条目（grep `toolbox|pad 90|pad 110|
  creambox` 在 `scratch-proof-es/PROOF-NOTE-es.md`、`scratch-proof-pt/PROOF-NOTES-PT.md`、
  `scratch-proof-es2/PROOF-NOTE-es2.md` 均 0 命中）：工具盒缺陷是 fix1 轮用 creambox 实测发现的，
  不是 proof 轮的条目；proof 轮无 creambox 检查（见 pt FIX-LOG §2 末）。
- 根因（工具盒 FIX-LOG §2，已逐版复算）：P7 工具盒公式 `tbh = 62 + Σ(n·29.5+6) + pad` 按
  `n·29.5+6` 计，实际墨进是 `20.5 + n·29.11 + 6`（`Page.para` 首基线偏移），6 项累计少算 123，
  仅被 29.5-vs-29.11 的行高高估部分抵消（+0.39/行）。清除量 clearance(pad) = pad + 0.39Σ − 93.89：
  Σ=9 时 pad−90.4，Σ=10 时 pad−90.0，Σ=8 时 pad−90.8。pad 90 时清除 −0.4/0.0/−0.8，
  pad 110 时 +19.6/+20.0/+19.2（与 core-de +18.8 同级）。
- 假验证已证伪：fan-out 注释称“90 validated by en/fr occlusion 0 flags”。occlusion 审计只标记
  被后画不透明元素覆盖、或被细线穿过的文字；工具盒文字画在自家盒子之后、无任何东西覆盖它，
  审计对该缺陷类全盲——0 flags 不能证明盒底清除。该注现已从生成器中清除。
- 生产版现状（只读核查，`production/2026-w47/2026-w47-de-*/content7.py` 未动）：
  es/fr/it/ja/ko/zh-tw 为 pad 110 单行修；nl/ru 为 pad 110 + `RTOP = CTOP − 20`（行 76–77、84）；
  pt 为 `tbt = CTOP − 20` + `+ 90 + 20`（行 84–85、86–87、92）；en 另走 D3 解法
  （`tbh = None`，由模拟墨进反算，行 76、90）——en 不在本生成器修复范围内。

## 1. gen_tr.py 改动（仅 L116–117 两处）

文件：`hidden_files/w47/scratch-fanout-de/gen_tr.py`

改前（L116–117）：
```python
TB_NEW = ('tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 90'
          f"  # {LANG} fan-out: same pad fix as en/fr (formula underestimates ink advance; 90 validated by en/fr occlusion 0 flags)")
```

改后（L116–117）：
```python
TB_NEW = ('tbh = 62 + sum(len(wrap(t, "serif", False, 20.5, CW - 44)) * 29.5 + 6 for t in tb) + 110'
          f"  # {LANG} fan-out: pad 110 restores the core-de value. The formula still underestimates ink advance (it misses the +20.5/entry para offset, 6 entries = +123, only partly offset by the 29.5 vs 29.11 line-height gap), so 110 is a compensating value, not a formula fix. Verified by 6 hand-fixed editions (creambox-measured clearance +19.2..+20.0). Occlusion 0 flags cannot prove box-bottom clearance: the audit is blind to text spilling past its own box.")
```

改动点：
1. pad `+ 90` → `+ 110`（恢复 core-de 值；TB_OLD 本就是 `+ 110`，改后 TB_NEW 与 TB_OLD
   仅差注释——即生成器不再改动 pad 数值，只附加说明）。
2. 注释改写为真实依据三点：(a) occlusion 0 flags 不能证明盒底清除（审计对该类全盲）；
   (b) 110 由 6 版手工修 + creambox 实测清除 +19.2…+20.0 证实；
   (c) 公式本身仍低估墨进（漏 +20.5/项），pad 110 是补偿值、不是公式修复。
   未动其他任何行（`layout_extra` 机制、TR/TYPEMAP/INSTRMAP/E 生成逻辑均未碰）。

## 2. 重生成清单（只写 scratch，未覆写任何 live tr 文件）

方法：把修后 `gen_tr.py` + `tr_en.py`（生成源，纯数据无 import）+ 8 份 `vals_<lang>.json`
复制到 `scratch-fix-gen-tr/regen/`，用 `~/workspace/weekly-git/tools/venv/bin/python gen_tr.py <lang>`
逐个跑（`TMPDIR=<scratch>/tmp`）。每份输出均打印 `278 TR keys, typemap 10, instrmap 5, E 4`，
与 live 文件行数一致（341 行）。

**实际重生成 8 语（以 gen_tr.py 实际支持的语种为准）：es、it、ja、ko、nl、pt、ru、zh-tw。**
源数据：各语 `vals_<lang>.json`（values/overrides/typemap/instrmap/E_new/abstract/…/`layout_extra`）
+ 共享源 `tr_en.py`（TR_EN 键序）。

**任务所列“en/fr/es/it/pt/nl/ru/ja”与实际支持集不符，特此纠正：**
- en、fr **无法重生成**——`scratch-fanout-de/` 下没有 `vals_en.json` / `vals_fr.json`
  （只有 es/it/ja/ko/nl/pt/ru/zh-tw 8 份 vals）。en 是生成源本身（`tr_en.py`），fr 是手工产物。
  因此 fr 的 live `tr_fr.py` 仍带旧 pad-90 注释（行 329），en 的 `tr_en.py` 另有自己的注释
  （行 332，称“90 puts the Leserbriefe box 10px below the toolbox ink”），本次均未动，
  见 §5 未决项。
- zh-tw 是本次实际重生成的第 8 语（任务清单漏列，生成器支持集包含它）。

## 3. 逐行 diff（重生成 vs live `scratch-fanout-de/tr_<lang>.py`）

结论先行：**8 语 × 1 行 = 8 处 diff，全部属于“pad 行”，0 处“其他”。**
每处均为 live 行 337（LAYOUT 里的 TB_NEW 行）整行替换：pad `+ 90` → `+ 110` + 注释改写。
除行 337 外，8 份文件其余 340 行与 live **逐行完全相同**（含 `layout_extra` 的 content34
ey 条目——nl/ru/pt 的 ey 条目重生成一致）。

| 文件 | 行号 | 旧值（live） | 新值（重生成） | 类别 |
|---|---|---|---|---|
| tr_es.py | 337 | `… + 90  # es fan-out: same pad fix as en/fr (formula underestimates ink advance; 90 validated by en/fr occlusion 0 flags)` | `… + 110  # es fan-out: pad 110 restores the core-de value. The formula still underestimates ink advance (it misses the +20.5/entry para offset, 6 entries = +123, only partly offset by the 29.5 vs 29.11 line-height gap), so 110 is a compensating value, not a formula fix. Verified by 6 hand-fixed editions (creambox-measured clearance +19.2..+20.0). Occlusion 0 flags cannot prove box-bottom clearance: the audit is blind to text spilling past its own box.` | pad 行 |
| tr_it.py | 337 | 同上结构（`it fan-out: …`） | 同上结构（`it fan-out: pad 110 restores …`） | pad 行 |
| tr_ja.py | 337 | 同上结构（`ja fan-out: …`） | 同上结构（`ja fan-out: pad 110 restores …`） | pad 行 |
| tr_ko.py | 337 | 同上结构（`ko fan-out: …`） | 同上结构（`ko fan-out: pad 110 restores …`） | pad 行 |
| tr_nl.py | 337 | 同上结构（`nl fan-out: …`） | 同上结构（`nl fan-out: pad 110 restores …`） | pad 行 |
| tr_pt.py | 337 | 同上结构（`pt fan-out: …`） | 同上结构（`pt fan-out: pad 110 restores …`） | pad 行 |
| tr_ru.py | 337 | 同上结构（`ru fan-out: …`） | 同上结构（`ru fan-out: pad 110 restores …`） | pad 行 |
| tr_zh-tw.py | 337 | 同上结构（`zh-tw fan-out: …`） | 同上结构（`zh-tw fan-out: pad 110 restores …`） | pad 行 |

（上表 it/ja/ko/nl/pt/ru/zh-tw 行的旧/新全文与 es 行逐字对应，仅语言名前缀不同；
完整 diff 输出为每文件 `337c337` 一组，4 行 diff 输出，无其他行。）

**生成器与 live 不一致项：无。** 任务提示的两处疑似手工同步项均已核查：
- `tr_pt.py:243` 附近的 `pess.` 值（`beginnt (3.ª pess. sg.)` 等）：重生成与 live 完全一致——
  这些值已在 `vals_pt.json` 的 values 里，不存在只存在于 live 的手工修，重生成不会洗掉。
- `tr_en.py:76` 附近的 `Words` 值（`WEIHNACHTSWÖRTER Words`）：`tr_en.py` 是生成源（TR_EN），
  不是生成产物，不参与重生成，不存在被洗掉的风险。
- 其余：8 文件 0 处非 pad diff，说明 live tr 文件自生成后除 pad 行外无任何偏离 vals JSON
  的手工改动——**重生成是安全的，不会洗掉任何已同步手工修**（但本次仍只写 scratch，未覆写 live）。

附注（diff 基线说明）：`scratch-fanout-de/tr_it.py` 与 `scratch-fanout-de-rebuild-A/tr_it.py`
当前 diff 为 0 行（工具盒 FIX-LOG §5.4 称 it 副本 stale 的情况已不存在，应已同步）；
`tr_fr.py` 仍 stale（与 rebuild-A 差 22 行，皆为盒标题缩短类翻译值，与 pad 无关，不影响本次 diff）。

## 4. rail-up 设计（nl/ru/pt，只设计、不上线）

### 4.1 为什么需要独立条目

- nl/ru/pt 的 Σlines = 10，NOCH EIN WORT 已结束于 1547.5，距 1548 Sätze 规则仅 0.5px。
  平铺 pad 110 会把整条 col-3 rail 下推 20px → NOCH EIN WORT 结束于 1567.5，越过规则。
  必须整条 rail 上移 20（rail 顶 330→310），使工具盒底、LESERBRIEFE、NOCH EIN WORT
  全部保持原位，只把工具盒内的最后基线从 813.0 抬到 793.0。
- fr/it/ja/ko/zh-tw/es 绝不加此条目：它们的 NOCH EIN WORT 有余量，pad 110 单行已够。
  条目的作用域机制就是“只写进 `vals_nl.json` / `vals_ru.json` / `vals_pt.json` 的
  `layout_extra`”——`gen_tr.py` 已原样发出 `layout_extra`（pad 条目之后），**生成器本身
  不需要为此再改一行**。
- `transform.py:311–318` 按顺序逐条做字面替换，每条断言 old 在目标文件中恰好出现 1 次
  （`count == 1`，否则 loud fail），故锚点必须唯一。已在 core-de `content7.py` 上核验（§4.3）。

### 4.2 推荐方案（Option B，3 条目；以 nl/ru 已落地手修为模板）

hand-fix 形状（nl/ru，生产版 `content7.py:76–77、78–79、84`）：
```
76 tbh = 62 + sum(...) + 110  # fix1 D1: ...
77 RTOP = CTOP - 20  # fix1 D1: ...
78 p.rect(ix, RTOP, CW, tbh, fill=BOX)
79 yy3 = RTOP + 16
84 ry = RTOP + tbh + 16
```
对应 `vals_{nl,ru,pt}.json` 的 `layout_extra` 追加（排在现有 content34 ey 条目之后）：

| # | file | old（core 原文） | new | 说明 |
|---|---|---|---|---|
| R1 | content7.py | `p.rect(ix, CTOP, CW, tbh, fill=BOX)` | `RTOP = CTOP - 20  # {LANG} rail-up: whole col-3 rail raised 20 so the +20 pad leaves the rail bottom where it was (toolbox bottom 813.0, NOCH EIN WORT ends 1547.5, 0.5px before the 1548 rule); ~63px slack above the box, 20 used`\n`p.rect(ix, RTOP, CW, tbh, fill=BOX)` | 定义 RTOP 并切换工具盒 rect；定义行紧贴首次使用处 |
| R2 | content7.py | `yy3 = CTOP + 16` | `yy3 = RTOP + 16` | rail 文字起点跟随上移 |
| R3 | content7.py | `ry = CTOP + tbh + 16` | `ry = RTOP + tbh + 16` | LESERBRIEFE 起点跟随（`wy3 = ry + rh + 16` 由 ry 派生，NOCH EIN WORT 自动跟随） |

注：R1 的 new 是两行（定义行 + rect 行）；`gen_tr.py` 的 `layout_extra` 发射逻辑（`sq()` 转义）
已支持含 `\n` 的 new 值——三语现有 ey 条目外，追加这三条即可。OLD 锚点均为 core 原文短行，
与 pad 条目（TB_OLD → TB_NEW）无重叠，应用顺序无关。

备选 Option A（不推荐）：把 `RTOP = CTOP - 20` 追加到 pad-110 行之后（即 R1 的 old 取
TB_NEW 整行、new 为该行 + `\nRTOP = …`）。等价几何，但锚点是含长注释的整行 TB_NEW，
注释一改锚点即断；且手修把 RTOP 定义放在 tbh 行之后、rect 行之前，Option B 的落点
（rect 行正上方）在输出文件里是同一行号效果（core 行 77 位置），可读性相当。

### 4.3 锚点唯一性核验（core-de `content7.py` 实测）

| 锚点 | 出现次数 | 位置 |
|---|---|---|
| `p.rect(ix, CTOP, CW, tbh, fill=BOX)` | 1 | 行 77 |
| `yy3 = CTOP + 16` | 1 | 行 78 |
| `ry = CTOP + tbh + 16` | 1 | 行 83 |
| `tbh = 62 + … + 110`（pad 条目锚点 TB_OLD） | 1 | 行 76 |

`CTOP, CBOT = 330, 1480`（行 17）；`CTOP` 本身绝不能改——A2/B1/B2 三列 Flow
（行 19、40、54）仍从 `CTOP = 330` 起。rail 只切换上述三处使用点。

### 4.4 预期效果（三语相同，Σ=10）

- 工具盒：顶 330 → **310**，底 **813.0 不变**；最后基线 813.0 → **793.0**；
  清除 **+20.0**（基线；ink +14.8，按 pt 实测 descender 5.2）。
- LESERBRIEFE：y **829 不变**，底 1381.5，清除 +10.4 不变。
- NOCH EIN WORT：y / 结束 **1547.5 不变**（仍 0.5px 在 1548 规则之前），清除 +42.9 不变。
- A2/B1/B2 列、P7 intro、phrases（py=1560）、clinic、teaser：全部不动。
- 观感：工具盒顶比 A2/B1/B2 列头（330）高 20px；工具盒 FIX-LOG 已在 nl/ru 全页 100dpi
  渲染上确认读感干净、无碰撞（intro 结束于基线 262，rail 顶 310 之前无任何 col-3 元素）。

### 4.5 风险

1. **锚点漂移 loud-fail（安全的失败）**：core `content7.py` 若改动 rect/yy3/ry 任一字面，
   transform 即报 `layout anchor not unique` 并停住，不会静默跳过。后续 core 改动后须重验 §4.3。
2. **作用域错放**：条目只属于 nl/ru/pt 三份 vals；若误抄进其他语的 vals，该版 rail 会被
   无故抬高 20（几何仍合法但与手修版不一致，且浪费上方余量）。上线时须逐份核对。
3. **pt 的文本形式分叉**：pt 生产版手修用的是 `tbt` + `+ 90 + 20` 形式（行 84–85），而
   生成器方案产出 `RTOP` + `+ 110` 形式。两者数值全等（90+20=110；tbt=RTOP=310），几何
   完全一致，但**文本逐行 diff 会有 5 行措辞差异**。若未来有人拿生成件与 pt live 版逐行比对，
   须以几何等价为准裁定，不要误判为内容差异。建议上线时在 pt 的 FIX-LOG 备注此点。
4. **重复应用 loud-fail**：transform 对已抬升过的文件重跑时，old 锚点计数为 0 即断言失败
   ——这是保护，不是缺陷；重跑前须确认目标是 core 原文。
5. **未验证**：本设计未在任何版上跑过 transform + rebuild + creambox；上线时必须走完整门禁
   （driver ALL GATES PASS + creambox 复测 +19.2…+20.0 + NOCH EIN WORT 1547.5 终验），
   本次不做（任务只要求设计）。

### 4.6 本次未动

- `gen_tr.py` 未为 rail-up 加任何条目；`vals_nl.json` / `vals_ru.json` / `vals_pt.json`
  未改；任何 live 文件（含三语 `content7.py`）未动。本节纯设计。

## 5. 未决项（需协调员另行裁定，本次不做）

1. **en/fr 的 pad 行仍带旧注**：`tr_en.py:332`（en 自己的 90 注释）、`tr_fr.py:329`
   （`90 validated by en occlusion 0 flags`）不在本次修复内——两者无 vals 文件，无法经
   gen_tr.py 重生成。fr 若未来补 vals 并重生成，pad 行自动修正；en 的情况特殊
   （生产版已是 D3 模拟墨进解法，`tbh = None`，其 LAYOUT 注释另有“110 留 104px 死空间”
   的说法未在此核查），须 en 线另行裁定。
2. **公式本身未修**：pad 110 仍是补偿值。根治（公式计入 +20.5/项 para 偏移）是
   `tools/`/bslib 层面的改动，超出本次“只修生成器 pad 值”范围，需另立任务。
3. **live tr 文件未覆写**：重生成件只在 `scratch-fix-gen-tr/regen/`。是否把 8 份
   `tr_<lang>.py` 的行 337 同步进 live（即把本次修复落地到 fan-out 产物），由协调员定
   ——同步时仅需替换每文件行 337 一行（§3 表），其余行与 live 完全相同，无洗掉手工修的风险。
4. **rail-up 未上线**：§4 设计待裁定；上线时须补 transform + rebuild + creambox 全门禁，
   并处理 pt 的 `tbt`/`RTOP` 文本形式分叉（§4.5-3）。
5. **fr stale 副本**：`scratch-fanout-de/tr_fr.py` 与 rebuild-A 版差 22 行（盒标题翻译值，
   与 pad 无关）；任何未来 transform 须用 rebuild-A 的当前副本（工具盒 FIX-LOG §5.1 已记）。
