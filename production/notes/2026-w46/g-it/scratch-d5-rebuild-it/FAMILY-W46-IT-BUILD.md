# W46 意大利语目标家族 D5 重建 — Builder 报告

- 家族：W46 it（目标语 it；读者 de/en/es/fr/ja/ko/nl/pt/ru/zh-cn/zh-tw；无 it 读者）+ core-it
- 刊期：2026-11-09 – 2026-11-15，VOL.3，W46 due 2026-11-16
- Builder 工作目录：`hidden_files/d5-redo/scratch-2026-w46-it/`（`baseline/`、`patched/`、`logs/`、`bin/`）
- 正典解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3）
- 结果：**12/12 终轮 20/20**（10 版 run2，pt 与 core-it run3）。只降字号修复 35 处 + run3 补 3 处；无文字内容改动。
- 纪律：只写 scratch 内 `patched/`；production 由 closer 同步；无 commit/push；未跑 `lint --write`，未动 index.json；未重跑 webpdf 覆盖终轮网 PDF。

## §0 方法

### §0.1 导出器核实（P3b）：ADOPT

- 任务书写的 `hidden_files/style-port-it/textexp_it.py` 不存在。实测真导出器是 `hidden_files/style-port-it/export_it.py`（头取自 production 副本 `.text.md`、VOL 按 `production/volumes.json` 纠为 VOL.3；it 格式：标题行 `# <slug>`、无 `# Page N`、每页 `## <PageName>`、除 `### Risposte` 外无 markdown emphasis）。原生校验器是 `hidden_files/style-port-it/verify_textexp_it.py`（exit 0 当且仅当 UNEXPECTED=0 + header OK + 习题行数/编号一致 + 页数一致；差异分类 SEP/CJK/WORD/TRIM）。
- 试跑（`scratch-2026-w46-it/trial-export/`）：生产版 de 导出与 issues/ 已发版 BYTE-IDENTICAL（647 entries、150 题）；fanout 版 de 导出与 fanout `.text.md.new` BYTE-IDENTICAL（55,733 B；648 entries），与已发版差异仅为 intended transforms（SEP `' · '`→U+3000、CJK 间距合拢、WORD 每周词拆行 1→2 行、TRIM）。
- port 团队 `style-port-it/w46/*/verify-*.txt` 11 版齐全，差异类全是 SEP/SEP+CJK/WORD/TRIM，无 UNEXPECTED（de：SEP 87、WORD 1、TRIM 1；zh-cn：SEP 74、SEP+CJK 14、WORD 1）。TRIMS 有据：de/es 各 1 条 P7 LETTERE note 删从句（Newsreader 下 note 多绕一行压线）。
- 结论：导出器 ADOPT，交付 text.md 取新鲜导出 `.text.md.new`（新 §1.1 格式），不是 carry-over（D49 的 pt 情形不适用，it 有导出器）。it 导出器无 24pt 阈值（stub 无条件记录全部字符串，按 kind 映射 `###`）；D47 核对见 D47 节（12 版 `### Risposte` 各 1 行，0 丢失）。

### §0.2 D1 定性：D1+D5 一次做

- 生产 svglib：D1 fix 0 处、Newsreader 0 处、`_D5_READER` 0 处（pre-D1、前 Newsreader 代旧样式）。fanout svglib（`style-port-it/w46/<reader>/`）：D1 fix 1 处、Newsreader 8 处。故 patched svglib = fanout 版 + D5 安装（PLAN：W46 it 属“旧样式（port 已建未入仓）”17 家之一，§1.1 组装 + D5 一次渲完；D10：协调员已批准把 fanout `.py` 集组装进仓内 core-it，W43/W46；builder 在 scratch 建 `patched/core-it/`，closer 同步）。
- fanout 与生产 `.py` 集差异：bslib4 + content12/34/56/7/8 + svglib 全部 7 个源文件都不同（§1.1 全面改版：刊头几何、moth、颜色、分隔符 U+3000 等）；fanout svglib 尺寸：latin 版 ~18,156–18,165 B，ja/ko/zh-cn/zh-tw ~20,587–20,746 B（含 kinsoku 等）。
- 生产 `run.py` md5 `183d86d469b8480da4a9721f7b241036` = W47 版 runner（打印 TOTAL，可用；patched 与生产 `run.py` 相同，无差异）。生产 `render.py` 是死路径（`BASE=~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-<r>`，core 写 `La-Lucerna-VOL3.pdf`），改用 fanout render.py（ED 相对路径，逐版已适配印 PDF 名）。fanout `run.py`（md5 `b26c6fe1…`，455 B pilot）不用。生产 assets 只有 `CREDITS.md`；故事 JPG（`castagne.jpg`、`tartufo.jpg`）+ `lucerna-moth.svg` 自 fanout assets 拷入 scratch（D20：JPG 不进 production）。

### §0.3 基线（`baseline/`，生产 `.py` + 生产 run.py + fanout render.py + 生产 KIT/ABSTRACT + 已发版 `.text.md` 锚点）

- 构建 12/12 BUILD-OK；每版 TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；text.md 导出与 issues/ BYTE-IDENTICAL 12/12；issues/ frontmatter pin（pdfBytes/pdfSha256）与 issues/ PDF 文件核对 12/12 一致；p8 extract 150/150（12 版全）；基线网 PDF 比 issues 版少 1 字节者居多（de 673,008 vs 673,009；ja/zh-cn/zh-tw/nl exact），系 webpdf 非确定性，非缺陷；基线 core-it 印 PDF 与 zh-cn 印 PDF 逐字节相同（20,987,115 B，同 SHA 前缀）。
- 基线印 PDF 字节：de 7,094,519、en 7,092,151、es 7,089,756、fr 7,090,771、ja 20,219,149、ko 11,601,420、nl 7,128,505、pt 7,093,030、ru 7,051,943、zh-cn 20,987,115、zh-tw 19,363,060、core-it 20,987,115。基线印 PDF SHA 前 12 位见 `logs/baseline-record.txt`（de `a09a3dd5eb71` 等）。
- 修前 D5 普查（`d5_census.py` totals，Latin/Cyrillic/curly-in-CJK）：de 491/0/1、en 486/0/1、es 487/0/0、fr 490/0/0、ja 341/0/0、ko 340/0/0、nl 489/0/0、pt 488/0/0、ru 348/250/0、zh-cn 347/0/1、zh-tw 347/0/0、core-it 347/0/1。
- 基线 D18 间隙 px：de 143.0、en 109.2、es 90.3、fr 139.1、ja 66.8、ko 188.2、nl 43.3、pt 47.0、ru 64.8、zh-cn 119.1、zh-tw 119.1、core-it 119.1。基线 D37 余量 pt：de −44.8、en +23.0、es −47.0、fr −54.1、ja +152.0、ko N/A、nl −35.6、pt −93.7、ru −79.5、zh-cn N/A、zh-tw +152.2、core-it N/A。**基线 D37 负值是横向量测 artifact：旧样式副刊头行在 y=574、奶油框顶 y=588，墨水底 ≤ 框顶、无垂直重叠（overlap=False），不是缺陷。**fanout de（新样式）实测：D18 292.8px；D37 行末 1361.0、框左缘 1439.5、余量 +78.5px = +58.9pt（y=612，垂直重叠成立）。
- 基线门禁（tag=baseline，固定后脚本重跑）：de/en/zh-cn/core-it 18/20，其余 19/20。FAIL 仅两类，均为预期基线态：G3-census 12/12（修前 D5 违规在位）；G16-quotes 仅 de（defective=1）、en（2）、zh-cn（2）、core-it（2）（curly-in-CJK 各 1 处，fix2 应清）。其余 18 门全 PASS：G15a 三方字符多重集差 0、G15c UNEXPECTED=0、D18/D37、G7 extract 150/150、G15b 仅记录（rc=1，pt rc=2）。

### §0.4 装机（步骤 2）

- `tools/mechanism-w47/apply_variant.py --target it --reader <r> --week 2026-w46`（先 `--check` 干跑 rc=0，再正式安装 rc=0，日志 `logs/install-check-<r>.log` / `logs/install-<r>.log`）。
- `_D5_READER` 实际行号 **svglib.py:100**：latin（de/en/es/fr/nl/pt）、cjk（ja/ko/zh-cn/zh-tw；core-it 按 zh-cn 装 cjk）、ru（`"ru"` 旧分支）。fix2 每版 5 处；**fix-xru=0**（D26，W47-only 未引入）；D1 每版 1 处。`test_d5_routing.py` **FAILURES: 0**。ja：CJK index SC→JP + 自当周 core-zh-tw 移植 kinsoku 块；ko：SC→KR；zh-tw 保持 SC 面（FR §0.3 先例：生产 zh-tw 即 SC 面，改 TC 会改变全部繁体字形/字宽、超出 D5 范围）。

### §0.5 门禁口径（19 verdict/版 + G15b 仅记录）

- G1–G14 + G15a/G15c + G16 + D18 + D37；G15b 仅记录（D27）。`bin/gates_it.py`：`<ed> <baseline> <tag> <logdir> <tslug> <reader> <core_svg> <issues_pdf> <print_pdf> <web_pdf>`，写 `GATES-SUMMARY-<tag>.txt` + 各门日志进 `logs/<slug>/`。G9 freeze baseline 8/8；G10 freeze diff vs baseline；G8 p8 compare（core 用 `patched/core-it/svg`，run1/run2/run3；基线门用 `baseline/core-it/svg`；zh-cn 与 core 自比 keydiff `[]`）；G12 boxtitle（`--backup-root` = scratch 根目录；备份树 `scratch-fanout-it/backup/<slug>/svg/` 已由 baseline_record.py 从基线 svg 拷好；boxtitle 的 week_dir = 版目录父级即 `patched/`，故 core 对照为 `patched/core-it`）。
- G15a：patched 用 port-aware `pdfdiff_it_run.py`（port 语义：新网 PDF 文字层会丢掉 U+3000，故分隔符两侧删除后比对；VOL 不应有差异；weekly-word `»:`→`»`；TRIMS 按表；通过标准 `IDENTICAL after intended transforms`）+ 印/网多重集差 0。**基线 G15a 用 plain 多重集**：pdfdiff 工具只对 OLD（已发）做 TRIM/WORD 归一化，不对 NEW 做，基线（未 trim 的生产内容）用它必报 2 段假差异（WORD 冒号的 `-raw` 抽取顺序 artifact + TRIM 单侧归一化）；基线实测：默认 pdftotext 下印/网/已发三方多重集差均为 0（de：`bestenTexte` ×1、`»:` ×1、`»` ×59，三方一致）。
- G14 creambox（it 家适配）：上游 `tools/d5_creambox_audit.py` 断言 base 与 patch 的 #f0eee5 矩形数相等；it 旧样式基线 0 个 #f0eee5 盒（奶油填充为 #fdfaf0/#f1ead6/#f3edda/#e8dfc8），base-vs-patch 无法跑（`AssertionError: box count changed: base 0 vs patch 5`）。改用 `bin/creambox_patch_it.py`：复用该工具自身的 `texts()`/`rects()`/`abs_flags()`，只对 patched 版做绝对检查（任一元素墨水超出 #f0eee5 盒 > OVER_TOL 2.0px 即缺陷）；box 下溢出由 G11 覆盖。de run1 实测：1 缺陷（与 boxtitle 的 TYPISCHE FEHLER +37.8px 一致），驱动有效。
- D18：刊头标语行间隙（内容识别：取 date run `SETTIMANA DAL 9 AL 15 NOVEMBRE` 所在 y 为顶行 y，间隙 = date 左墨 − slogan 组右墨，SVG px，PIL ink_box，引 `tools/occlusion_audit.py` 的 `ink_box`，含 letter-spacing）。D37：副刊头行 = P1 上 bold、含 ` — `、y<700 的行（意大利语标语行非 bold，LA NOTIZIA/kicker 行无 em dash，故唯一；ja/zh-tw 新样式描述行无 ` — ` 后缀、短标签，D37 为 N/A；ko/zh-cn 在 P1 上根本没有副刊头行，D37 为 N/A）；奶油框 = 首个 x>1000 且 y+h ≥ 行 y 的 cream 填充 rect（`#f0eee5` 新样式／`#f1ead6`／`#fdfaf0` 旧样式）；余量 pt = (框左缘 − 行末) × 0.75（印 PDF 页 1462.5pt / SVG 1950 单位）。D37 通过条件：N/A，或余量 >0，或无垂直重叠（行墨底 ≤ 框顶）。
- G15c：`verify_textexp_it_run.py`（原生校验器副本，ED/输出由环境变量传入），要求版目录内有 `<slug>.text.md.new` + `textexp-<reader>.log` 含 `entries: N exercises: 150`。
- D41：本家无斜体旗标（见 D41 节）。

### §0.6 工具注记

- `bin/gates_it.py` 在基线门禁中陆续修了 6 处解析 bug（均非基线问题）：G2 读 `findings`（非 `defects`）；G6 解析 `N flags`（非 stdout 关键词计数）；G7 读 `noted_set` 长度（非 `extract_count`/`extracted`）；G11 `spills` 是 list（`len==0` 通过）；G14 读 `totals.defects`；G15a 见 §0.5。另 G11/G12/G13 的 json 目录分开（原共享 `json-<tag>/` 下三工具同写 `<slug>.json` 互相覆盖，事后重读会错）。修后基线门禁全量重跑（旧版 7 版摘要作废）。
- `bin/measure_it.py` 修 2 处：D37 描述行加宽阈值（`_inkw > 600`）误删 ja（~540px）/zh-tw（~528px）行——P1 上 bold ` — ` 行唯一，阈值去掉；正常分支补设 `res["d37_row"]`（原只在 N/A 分支设，致 gates 误判 N/A）。
- `bin/run_gates_batch.sh`：core_svg 按 side 取值（baseline→`baseline/core-it/svg`，patched→`patched/core-it/svg`）；初版硬编码 baseline core，run1 门禁前修好。
- `bin/run_batch.sh` 接口为 `<side> <tag> <listfile>`、清单格式 `dirslug|webname|reader|textslug`；首次 run1 启动误传单参数（`set -u` 下 `$2` 未绑定，3 批空跑），重写清单后重起，无损失。
- 工具自检已过：occlusion `--selftest`（6 类全触发）、creambox `--selftest`（OK，含旧样式基线 fallback）、head_check `--selftest`（OK）。

### §0.7 几何常量（it 家实测）

- 页 1950×2700（SVG 单位）；MX=88；CW=422.5；GUT=28；COLX=[88, 538.5, 989, 1439.5]；RIGHT=1862。p.text 盒标题预算 400.5（422.5−22 内缩）；f.box 标题预算 404.5（422.5−18 pad）；e.head 预算 422.5。P1 右栏盒 (1439.5, 588, 422.5, 700)，底 1288；P1 描述行 y=612（de/en/fr/pt/ru，新样式）、y=372（es/ja/nl，bold 16pt，取代意大利语标语）；顶条 y=92，页脚 y=2624。

### §0.8 事故

- OUT 重定向修好前，第一轮基线 de 构建把 `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-de/svg/` 内 8 个 SVG 在 2026-11-15 21:28 UTC 覆盖重写（同生产源重建，files/ 树非交付位置）；修好后不再写该处。setup.sh 内 `grep -rl 'files/weekly-report' baseline/` 仅命中各版 WEEKLY-KIT.md 的文字提及，无代码引用残留。
- `pkill -f run_gates_batch.sh` 曾误杀本次 exec 自身（命令行含该串）；后改按 PID 杀，只杀两个残留 `gates_it.py` 孤儿进程。旧版基线门禁 7 版摘要已随固定脚本重跑作废。
- 磁盘：开工 73G/150G，终轮后 74G/150G（50%），未触 100G 门。

## §1 de / en（Latin）

### de（2026-w46-it-de）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 18/20 | 16/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=491（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=1 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash；patch-only 驱动：1 缺陷 = P7 标题） | PASS defects=0 |
| G16 quotes | FAIL defective=1（基线已知） | PASS 0 | PASS 0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1, TRIM 1） | PASS IDENTICAL（SEP 87, WORD 1, TRIM 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=648, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 143.0px / −44.8pt（无重叠） | — / +21.3pt（重叠） | **163.2px / +21.3pt（重叠）** |

修复（run1→run2，探针 = 本版 svglib `text_w`）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:258` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content7.py:73` | P7 盒标题 `ERRORI TIPICI TYPISCHE FEHLER` | 23 → 20 | +37.8px | 381.1px / 400.5 |

注：P7 标题 23→21 探针 400.1px、余量仅 0.4px，取 20 求稳（FR 前例：+42.8  creambox 取 23→20）。

### en（2026-w46-it-en）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 18/20 | 16/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=486（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=2 | PASS 0 |
| G14 creambox | PASS 0 | FAIL（上游审计 crash） | PASS defects=0 |
| G16 quotes | FAIL defective=2（基线已知） | PASS 0 | PASS 0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1） | PASS IDENTICAL（SEP 87, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=648, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 109.2px / +23.0pt（无重叠） | — / +106.6pt（重叠） | **132.9px / +106.6pt（重叠）** |

修复（run1→run2）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:258` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content12.py:91` | P1 目录标题 `IN QUESTO NUMERO CONTENTS` | 24 → 21 | +40.2px | 385.3px / 400.5 |
| `content7.py:73` | P7 盒标题 `ERRORI TIPICI Common mistakes` | 23 → 22 | +9.8px | 392.4px / 400.5 |

## §2 es / fr（Latin）

### es（2026-w46-it-es）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 16/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=487（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=1 | PASS 0 |
| G14 creambox | PASS 0 | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1, TRIM 1） | PASS IDENTICAL（SEP 87, WORD 1, TRIM 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=647, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 90.3px / −47.0pt（无重叠） | — / −12.7pt（无重叠，y=372 行） | **100.6px / −12.7pt（无重叠）** |

修复（run1→run2）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:257` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content7.py:73` | P7 盒标题 `ERRORI TIPICI ERRORES TÍPICOS` | 23 → 21 | +26.8px | 390.3px / 400.5 |

### fr（2026-w46-it-fr）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 16/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=490（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=3 | PASS 0 |
| G14 creambox | PASS 0 | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1） | PASS IDENTICAL（SEP 87, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=648, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 139.1px / −54.1pt（无重叠） | — / +15.4pt（重叠） | **161.1px / +15.4pt（重叠）** |

修复（run1→run2）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:258` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content12.py:91` | P1 目录标题 `IN QUESTO NUMERO SOMMAIRE` | 24 → 21 | +45.2px | 390.2px / 400.5 |
| `content7.py:73` | P7 盒标题 `ERRORI TIPICI ERREURS TYPES` | 23 → 22 | +6.8px | 389.8px / 400.5 |
| `content7.py:84` | P7 盒标题 `LA PAROLA MOT DE LA SEMAINE` | 23 → 21 | +29.5px | 392.1px / 400.5 |

## §3 ja / ko（CJK）

### ja（2026-w46-it-ja）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 17/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=341（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | PASS 0 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 85, SEP+CJK 2, WORD 1） | PASS IDENTICAL（SEP 85, SEP+CJK 2, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=647, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 66.8px / +152.0pt（无重叠） | — / N/A（短标签，无 ` — ` 行） | **110.4px / N/A** |

修复（run1→run2，仅 2 处 D head）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:257` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |

注：ja 描述行新样式为 y=372 短标签 `イタリア語テキスト　日本語の解説`（无 ` — ` 后缀），D37 N/A，无越框风险。

### ko（2026-w46-it-ko）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 16/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=340（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=1 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 86, WORD 1） | PASS IDENTICAL（SEP 86, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=647, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 188.2px / N/A | — / N/A | **201.4px / N/A** |

修复（run1→run2）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:257` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content12.py:90` | P1 目录标题 `IN QUESTO NUMERO 이번 호 차례` | 24 → 22 | +15.7px | 381.6px / 400.5 |

注：ko P1 标题 24→23 探针 399.0px、余量仅 1.5px，取 22 求稳。

## §4 nl / pt（Latin）

### nl（2026-w46-it-nl）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 16/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=489（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=2 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1） | PASS IDENTICAL（SEP 87, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=647, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 43.3px / −35.6pt（无重叠） | — / −5.6pt（无重叠，y=372 行） | **67.8px / −5.6pt（无重叠）** |

修复（run1→run2）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:257` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content12.py:90` | P1 目录标题 `IN QUESTO NUMERO INHOUD` | 24 → 23 | +4.2px | 387.6px / 400.5 |
| `content7.py:84` | P7 盒标题 `LA PAROLA WOORD VAN DE WEEK` | 23 → 20 | +44.5px | 386.5px / 400.5 |

注：nl P7 标题 23→21 探针 405.9px 仍超 5.4px，取 20。

### pt（2026-w46-it-pt）

| 门 | 基线 | run1 | run2 | run3（终轮） |
|---|---|---|---|---|
| 总分 | 19/20 | 15/20 | 19/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 | PASS 0 |
| G3 census | FAIL lat=488（预期） | PASS rc=0 | PASS rc=0 | PASS rc=0 |
| G11 spill | PASS 0 | FAIL spills=1 | FAIL spills=1 | PASS 0 |
| G12 boxtitle | PASS 0 | PASS 0 | PASS 0 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1） | PASS IDENTICAL | PASS IDENTICAL（SEP 87, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=648, exercises=150 |
| G15b（仅记录） | rc=2 | rc=2 | rc=2 | rc=2 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 | 同左 |
| D18 / D37 | 47.0px / −93.7pt（无重叠） | — / −17.9pt（重叠） | — / +4.9pt（重叠） | **68.8px / +4.9pt（重叠）** |

修复：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:258` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content12.py:29` | P1 描述行（middle-anchored，x=975） | 16 → 15 | D37 −17.9pt | 行末 1432.6px，D37 +4.9pt |
| `content12.py:86` | P1 周计划注文（p.para，双行） | 16.5 → 13 → 11.5 | 溢出 +6.68px → +1.95px | 单行 365.3px / 378.5 |

注（pt 注文两轮）：run1 溢出为 P1 右栏盒（底 1288）下注文第二行 `horários podem mudar.` 基线 1294.7（+6.68px）。首轮按“第二行 = 起点 + 2.35·s”模型取 13pt，run2 仍溢 +1.95px（第二行 1290.0）——实测纠正模型：p.para 首行基线与字号无关（恒为 1272.4），第二行 = 1272.4 + 1.35·s。故单行才是稳解：全文宽 524.2px@16.5，≤378.5 需 s≤11.9；取 11.5pt（365.3px），且即使仍折为双行、第二行基线 1287.9 亦在盒内。run3 证实单行（SVG 内两片段同 y=1272.4），G11 0 SPILL。D37 描述行 16→15 探针行末 1432.6px；门禁实测行末 1433.0px、余量 +4.9pt（重校 D37 独立量测同值；探针与实测差 0.4px。注记原称 +5.1pt 有误——按 1432.6px 同算式应为 +5.2pt；以门禁 +4.9pt 为准，仍 >0，通过不受影响）。

## §5 ru

### ru（2026-w46-it-ru）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 18/20 | **20/20** |
| G1 run | PASS TOTAL=150 | PASS TOTAL=150 OVF=0 HDW=0 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | PASS 0 | PASS 0 |
| G3 census | FAIL lat=348 cyr=250（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | FAIL defects=1（BODY 行） | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 87, WORD 1） | PASS IDENTICAL（SEP 87, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=648, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 64.8px / −79.5pt（无重叠） | — / +32.3pt（重叠） | **168.0px / +32.3pt（重叠）** |

修复（run1→run2，仅 1 处）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:86` | P1 日历注文（body 行）`Даты — по календарям; время может измениться.` | 16.5 → 15.5 | +17.5px | 392.7px / 400.5 |

注：ru 是唯一 run1 即无 HDW 的版——同串 D head 在 ru svglib 下 25pt 仅量 395.2/396.2px（< 422.5），故两 D head 留 25 不动。G12 的 BODY 缺陷是唯一非标题溢出（其余 10 版的 boxtitle 缺陷全是标题行）。

## §6 zh-cn / zh-tw / core-it（CJK + core）

### zh-cn（2026-w46-it-zh-cn）

| 门 | 基线 | run1 | run2（终轮） |
|---|---|---|---|
| 总分 | 18/20 | 15/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=347（预期） | PASS rc=0 | PASS rc=0 |
| G6 occlusion | PASS 0 | FAIL flags=1（TEXTX） | PASS 0 |
| G12 boxtitle | PASS 0 | FAIL defects=1 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 |
| G16 quotes | FAIL defective=2（基线已知） | PASS 0 | PASS 0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 74, SEP+CJK 14, WORD 1） | PASS IDENTICAL（SEP 74, SEP+CJK 14, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=647, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[]（与 core 自比） | 同左 | 同左 |
| D18 / D37 | 119.1px / N/A | — / N/A | **155.2px / N/A** |

修复（run1→run2）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:257` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |
| `content12.py:49` | P1 f.box 标题 `LA SETTIMANA IN CIFRE 数字看本周`（`tsize=` 收尾行） | 23（默认）→ 20 | +42.6px | 388.8px / 404.5 |

注：run1 G6 TEXTX（`　数字看本周` 墨水与 `A Cremona continua la Festa del ___.` 重叠 14.6×4.0px）与 G12 同源——f.box 标题超宽 42.6px 伸入隔栏；标题缩至 20pt 后两门同清（run2 SVG 实测标题字号 20）。f.box 修复按 D19 指收尾行 `content12.py:49`（`], tsize=20)`），标题行本身是同一 f.box 调用的首行。

### zh-tw（2026-w46-it-zh-tw）

| 门 | 基线 | run1 | run3（终轮） |
|---|---|---|---|
| 总分 | 19/20 | 17/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=347（预期） | PASS rc=0 | PASS rc=0 |
| G12 boxtitle | PASS 0 | PASS 0 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 72, SEP+CJK 15, WORD 1） | PASS IDENTICAL（SEP 72, SEP+CJK 15, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=648, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[137, 138, 139] | 同左 | 同左 |
| D18 / D37 | 119.1px / +152.2pt（无重叠） | — / N/A（短标签，无 ` — ` 行） | **155.2px / N/A** |

修复（run1→run2，仅 2 处 D head）：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:258` | P2-ex D head `D LE PAROLE DI SAN MARTINO` | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA` | 25 → 23 | 446.0px / 422.5 | 410.3px |

### core-it

| 门 | 基线 | run1 | run2 | run3（终轮） |
|---|---|---|---|---|
| 总分 | 18/20 | 15/20 | 18/20 | **20/20** |
| G1 run | PASS TOTAL=150 | FAIL HDW=2 | FAIL HDW=2 | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check | PASS 0 | FAIL defects=2 | FAIL defects=2 | PASS 0 |
| G3 census | FAIL lat=347（预期） | PASS rc=0 | PASS rc=0 | PASS rc=0 |
| G6 occlusion | PASS 0 | FAIL flags=1（TEXTX） | PASS 0 | PASS 0 |
| G12 boxtitle | PASS 0 | FAIL defects=1 | PASS 0 | PASS 0 |
| G14 creambox | PASS 0（base-vs-self） | FAIL（上游审计 crash） | PASS defects=0 | PASS defects=0 |
| G16 quotes | FAIL defective=2（基线已知） | PASS 0 | PASS 0 | PASS 0 |
| G15a pdfdiff | PASS 多重集差 0 | PASS IDENTICAL（SEP 74, SEP+CJK 14, WORD 1） | PASS IDENTICAL | PASS IDENTICAL（SEP 74, SEP+CJK 14, WORD 1） |
| G15c exporter | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0 | PASS UNEXPECTED=0, entries=647, exercises=150 |
| G15b（仅记录） | rc=1 | rc=1 | rc=1 | rc=1 |
| G7 p8 extract | 150/150 | 150/150 | 150/150 | 150/150 |
| G8 p8 compare | keydiff=[]（自比） | 同左 | 同左 | 同左 |
| D18 / D37 | 119.1px / N/A | — / N/A | — / N/A | **155.2px / N/A** |

修复：run2 轮 `content12.py:49` f.box 标题 `tsize=20`（23 默认 → 20，+42.6px → 388.8px / 404.5，G6+G12 同清）；**run2 轮漏了两处 D head**——修复脚本只对 10 个读者目录应用了 e.head 25→23，未覆盖 core-it 自有 `content12.py`/`content56.py`（core-it 与 zh-cn 源逐字节相同、但文件各一份）。run2 18/20 暴露后补修，run3 20/20：

| file:line | 内容 | 旧 → 新 | 越界量 | 探针余量 |
|---|---|---|---|---|
| `content12.py:49` | P1 f.box 标题 `LA SETTIMANA IN CIFRE 数字看本周`（`tsize=` 收尾行，run2） | 23（默认）→ 20 | +42.6px | 388.8px / 404.5 |
| `content12.py:257` | P2-ex D head `D LE PAROLE DI SAN MARTINO`（run3） | 25 → 23 | 436.6px / 422.5 | 401.7px |
| `content56.py:221` | P6-ex D head `D LE PAROLE DELLA MANOVRA`（run3） | 25 → 23 | 446.0px / 422.5 | 410.3px |

教训已记入 §10：core-it 不是 zh-cn 的符号链接，任何“逐读者目录”的批量操作必须把 core-it 单列一行。

### §6 core-it 交叉核对（已发 (it, zh-cn) 是 core-it 构建）

- production 目录结构：`production/2026-w46/` 下**没有** `2026-w46-it-zh-cn/` 目录，只有 `core-it/`（含 `2026-w46-it-zh-cn.text.md`、`WEEKLY-KIT.md`、`content12/34/56/7/8.py`、`bslib4.py`、`ABSTRACT.txt` 等）。(it, zh-cn) 的生产家就是 `core-it/`。
- 字节证据：基线 core-it 印 PDF 与基线 zh-cn 印 PDF 逐字节相同（20,987,115 B，同 SHA 前缀）；终轮 run3 core-it 印 PDF 与 run2 zh-cn 印 PDF 逐字节相同（7,421,626 B，SHA-256 全值相同 `5c233acaaca951c2…2254a`）；text.md.new SHA 全值相同。
- fitz 实测：已发 (it, zh-cn) PDF 的 P1 首行 `VOL. 3 · TERZA EDIZIONE`、页脚 `La Lucerna · 意大利语周报VOL.3 · LUCERNA ITALIAN WEEKLY` 与 core 构建的文本一致（旧样式分行方式不同，新样式分行，字符串同）；终轮 core-it 与 zh-cn 的 P1 首行/页脚/描述行 fitz 抽取一致。
- 结论：与 D5 字面条款无冲突，closer 无覆盖风险；closer 将 `patched/core-it/` 同步进 `production/2026-w46/core-it/`，**不**新建 `production/2026-w46/2026-w46-it-zh-cn/`（`patched/2026-w46-it-zh-cn/` 只是 core-it 的构建镜像，不同步为新目录）。

## D47 节（`###` 行核对：只记录，不补行）

- it 导出器无 24pt 阈值（stub 无条件记录全部字符串，按 kind 映射 `###`）。逐版核对：已发版 vs `.text.md.new` 的 `###` 行多重集差 12/12 为 0。
- 12 版各有且仅有 1 行 `###`，均为 `### Risposte`（P8 答案标题）：已发版行号 ~993–995，新导出行号 +2（WORD 拆行致总行数 +2，如 de 1295→1297）。丢失 0 行、多余 0 行。D47 补行不适用；closer 无针对性重验。
- 全表：de 1/1、en 1/1、es 1/1、fr 1/1、ja 1/1、ko 1/1、nl 1/1、pt 1/1、ru 1/1、zh-cn 1/1、zh-tw 1/1、core-it 1/1（已发/新）。

## D41 节（斜体旗标：无）

- run1–run3 全 12 版 G6 occlusion 共 2 个旗标，均为 zh-cn/core-it run1 的同一 TEXTX（f.box 粗体标题超宽伸入隔栏，见 §6），非斜体量测 artifact；修复后 run2/run3 G6 0 flags。无 W45 ru 式斜体误报，无需像素实测定性。

## §7 内容抽查

- 终轮印 PDF（de/en/zh-cn/pt run2/run3）fitz 抽查：P1 头条 `San Martino porta il vino nuovo: l'Italia assaggia l'autunno` 在位；P8 含 150 号；8 页。p8 extract 150/150（12 版终轮全）；G8 keydiff 除 zh-cn/core 自比 `[]` 外均为 `[137, 138, 139]`（E-section 翻译重定向，§6 KIT 已述，冻结层未动）。
- 修复字号落 SVG 实测：de P7 标题 20pt（y=242）、en P1 标题 21pt（y=1352）、zh-cn f.box 标题 20pt（y=1308.4）、pt 注文 11.5pt 单行（两片段同 y=1272.4）、pt 描述行 15pt（y=612）、ru 注文 15.5pt（y=1272.4）。
- WORD 拆行实测（de）：已发版 141 行 `« l'estate di San Martino » : tre giorni miti dopo il primo freddo, …` 一行；新导出 141 行 `« l'estate di San Martino »`、143 行 `tre giorni miti dopo il primo freddo, …` 两行（G15c WORD 1）。
- 印 PDF 字节较基线缩小（de 7,094,519 → 6,094,041；ja 20,219,149 → 11,185,676）系 §1.1 换字体集（Newsreader + Noto Serif 子集化），非内容丢失——G15a 三方多重集差 0、G15c 习题 150/150 证实。

## §8 同步清单（`diff -rq patched/ vs production/2026-w46/` 实测，排除 `__pycache__`/svg/cards/PDF/`.text.md`）

逐版差异文件清单（11 个生产目录 + core-it，模式完全一致；详表 `logs/sync-list.txt`）：

| 版 | 不同的文件（9 个/版） | patched-only（不同步） | production-only（不动） |
|---|---|---|---|
| de/en/es/fr/ja/ko/nl/pt/ru/zh-tw（10 版） | `WEEKLY-KIT.md`、`bslib4.py`、`content12.py`、`content34.py`、`content56.py`、`content7.py`、`content8.py`、`render.py`、`svglib.py` | `assets/castagne.jpg`、`assets/tartufo.jpg`、`assets/lucerna-moth.svg`（D20）、`run*.log`、`render-*.log`、`textexp-<r>.log`、`<slug>.text.md.new`（见下） | de/en/fr：`it-<r>-freeze.json`、`it-<r>-p8.json`；其余版无 |
| core-it | 同上 9 个 | 同上（`2026-w46-it-zh-cn.text.md.new`、`textexp-zh-cn.log`、run3 日志） | `final-it-freeze.json`、`final-it-occlusion.json`、`final-it-p8.json`、`finish`、`fix`、`freeze`、`it-gates.log`、`key-audit`、`proofread-gates`、`proofread-gates-round2` |

- `run.py` 12/12 无差异（patched 沿用生产 W47 版 runner）；`transform.py` 无差异（未动）。
- text.md 取件口径：**以 patched/ 侧导出件 `.text.md.new` 为准**（`patched/<dir>/<slug>.text.md.new`；`logs/<slug>/<slug>.text.md.new` 不存在——fr 家已证实；版目录内同名 `.text.md` 是已发版锚点，绝不取）。closer 将各版 `.text.md.new` 写入 `issues/2026-w46/<slug>/<slug>.text.md`；core-it 的取 `patched/core-it/2026-w46-it-zh-cn.text.md.new`，写入 `issues/2026-w46/2026-w46-it-zh-cn/2026-w46-it-zh-cn.text.md`，并同步替换 `production/2026-w46/core-it/2026-w46-it-zh-cn.text.md`。ABSTRACT.txt 排除（未动）；故事图 JPG 不进 production（D20）。
- `patched/2026-w46-it-zh-cn/` 不同步为新目录（见 §6）；zh-cn 读者版的 KIT（`patched/2026-w46-it-zh-cn/WEEKLY-KIT.md`，与 core-it KIT 同文、pin 取 run2 值）随 core-it KIT 一并核对即可，不另立目录。

## §9 交付物 SHA 总表（终轮实测；印/网 PDF 为构建名）

| 版 | 终轮 | 印 PDF（字节 / SHA-256） | 网 PDF（字节 / SHA-256） | text.md.new（字节 / SHA-256） |
|---|---|---|---|---|
| de | run2 | 6,094,041 / `167a5f9b452b4b136d52d3c4b9043925d3fbbe773af45ccff856cabd2c260127` | 564,425 / `67a4fa151b88e71f14f807a6e0d1b0fdbb9bc3bdc26cfb8d72e27daeffe266a7` | 55,733 / `8fda16960269c40e5f18f866d7139bf541d56030de42039b817c38c4bab9fb99` |
| en | run2 | 6,092,275 / `ad15251f47bb40e8a4cb9ad6a640f6a1f3d70f829df441fe5fb5c6466edcb0c5` | 562,623 / `19b4164d59136ed0612267f4bbea5d7ec8a4fe547934dff73fa54e907a2c0679` | 55,576 / `0b5e591c97168f4239a14934f3154a415695ab384b668530512a5ef0ece03e15` |
| es | run2 | 6,092,419 / `a0d679b5ee255164bd6389ec397ecddd61cfe4abeacdd0c0c2576587405fad7e` | 562,764 / `5f20036a7d75ff87bc6f039d11c72ff464bf6012135410eb24d6a4e08708b5cf` | 56,119 / `c78fc702afc825100c27fe608d43fa05f0b3c477b86796575d297633ad8fd7a4` |
| fr | run2 | 6,090,932 / `0ae79606161bed30eaee7220f9888b61c233b03530424b456a05b6af7495bb84` | 561,278 / `8805d6101af3941bdd48512627fa9e88e6753953b2683f754383dba72bd4fcbc` | 56,544 / `848e17628181d975632e06bd74528660e4e96eaf28d3ed4fdc0ca3c0b5008c0f` |
| ja | run2 | 11,185,676 / `75cc5ea34647f2940eb8a967f105fc055ea55e34880db990ecd80f62b04bf9e8` | 972,047 / `e63b00cbb242c2f6b663704ee67600710337aa8a3501d3d8b16bd1cf835b6fb4` | 58,101 / `cf3f4af3f6f62e815963ded0c60019838b4fefc9b97fd147c4490eca2aab1ec4` |
| ko | run2 | 8,315,805 / `4827c2befa9bff2e087cc535fc41538911aee053934858b056390adf7ee1d9ff` | 828,456 / `73688a35980d5f2217fcfb61f2bbd1c58b55271d1f5ca1de0fd4388566309bf2` | 57,414 / `da1562234b14118614afb9dff00f97e68a274c098092bedc1bdf0d70b3d0ad36` |
| nl | run2 | 6,089,510 / `f5f2ae497d22ece727323145995403cd8b9b8218bd5a66aeae822aa15e385e1f` | 559,816 / `67482186681ab49a5ad7595979f8a8d61662a15bcbad565f3b5e5f8e8efa8f4f` | 55,180 / `724bbdcda3a13806d19f5ba6309fa7f5dd53a209da05b0b99fb0bceecbea70bb` |
| pt | run3 | 6,095,290 / `ef41b3605c5a31c984b245ba554f931d8e8c5d45cb0915a6ebe11ec8798f1d94` | 565,660 / `548072004b875ee74b1c6d1356c4ee4123e2ea3bfbf0cc810cb96c28b0959ab2` | 55,879 / `bfb178094ed995300a7f697e2dd5e99faeb4d8b897417de713b67615320956f5` |
| ru | run2 | 6,354,279 / `8aeba5aa2f5d63a0493ddafc1b7f6f69d49e21b891d1673a7443c635fda1e4ee` | 801,833 / `14e3fade5a892633c8403a1f9d62f7d0baaac531c091897ff110829828ab8433` | 67,357 / `c5a3bd5b0ee4621e04c9f848f0ab26a59c6659a7ef749f4382f2fe0a648a5552` |
| zh-cn | run2 | 7,421,626 / `5c233acaaca951c2bec1e0c96bbdf83d1decd1257021ea9ac43dea297dc2254a` | 881,589 / `51533441f3764b00c06bf333e4c05aafc40bdb7211ea0f34f66a51b7c2c93c02` | 52,972 / `b4db0b227caabd7394f40f2f1638e612d9aa4627f911b034e7df5ef927095e7c` |
| zh-tw | run3 | 7,500,102 / `46c50a7df2e8a0ff16f58346fd2ac1f70af21616ddbbef709da803bbf6964682` | 983,685 / `b36c81097f8b63b12f4a65e006ce9ee17e7e369e2285593c2572b203545085d7` | 52,971 / `f2b1c9d93e8821e89383880647da465939be776ddd52981987384194f4da0adc` |
| core-it | run3 | 7,421,626 / `5c233acaaca951c2bec1e0c96bbdf83d1decd1257021ea9ac43dea297dc2254a` | 881,591 / `9226a03ea5e980209fbf4a97eb3a780616c1e497111b7f21e49b88b668df4f27` | 52,972 / `b4db0b227caabd7394f40f2f1638e612d9aa4627f911b034e7df5ef927095e7c` |

- D47 各版已发版值：`### Risposte` 各 1 行（已发版行号 ~993–995；新导出行号 +2）。已发版 text.md 与新导出 BYTE 差异仅 intended transforms（见 G15c diff classes）。
- 网 PDF 字节非确定性：core-it 网 881,591 vs zh-cn 网 881,589（同源同内容，2 字节差）；基线亦有 ±1B。§9 以终轮实测为准，closer 同步后不必重跑 webpdf 复核字节。
- 印 PDF 文件名：构建名 `The-Lucerna-VOL3-it-<r>.pdf`（core-it 为 `The-Lucerna-VOL3-it.pdf`）；KIT §10 所列 `La-Lucerna-VOL3-<R>.pdf` 为 files/ 树发行名，不属本次同步。

## §10 closer 交接

- KIT custody：KIT 正本在 production 侧；builder 只改了 scratch 内 `patched/` 的 12 份 KIT（§7 末 pin 块 + 末节 D5 重建节；读者版 §11、core §10；zh-cn 读者版 KIT 与 core-it KIT 同文，pin 各取本版终轮值）。closer 单向同步进 production。
- D19 核对：KIT 内全部 `content*.py:NNN` 引用 37 处逐行核对 patched 文件，0 坏（f.box 修复指 `tsize=` 收尾行 `content12.py:49`；p.text/e.head 引用行本身含新字号字面）。本报告内引用同按此规则，写完后用 `d19-final-fixed-nl.py` 修正版逻辑复核（见下残留项）。
- 残留项：无。12 版终轮全绿；D47 0 丢失；D41 无；§6 无冲突；磁盘 74G/150G。
- closer 待办（按序）：
  1. 按 §8 清单同步 11 个生产目录 + core-it（每版 9 文件：`WEEKLY-KIT.md`、`bslib4.py`、`content12/34/56/7/8.py`、`render.py`、`svglib.py`）；`run.py`、`transform.py` 无差异不碰；production-only 文件不动；assets JPG/moth、构建日志不同步。
  2. text.md：各版取 `patched/<dir>/<slug>.text.md.new` 写入 `issues/2026-w46/<slug>/<slug>.text.md`；core-it 取 `patched/core-it/2026-w46-it-zh-cn.text.md.new`，并替换 `production/2026-w46/core-it/2026-w46-it-zh-cn.text.md`。**不**新建 `production/2026-w46/2026-w46-it-zh-cn/`。
  3. 同步后核对：每版同步文件的 SHA 与 §9 印/网/text 一致（源文件 SHA 即 §9 值；网 PDF 2 字节级非确定性只认内容，不重跑 webpdf）。
  4. 终轮门禁摘要复本：`logs/*/GATES-SUMMARY-run2.txt`（10 版）+ `logs/2026-w46-it-pt/GATES-SUMMARY-run3.txt` + `logs/core-it/GATES-SUMMARY-run3.txt` 已随本报告复本写入 `notes/g-it/scratch-d5-rebuild-it/`（D29，cmp 一致）。
  5. 本报告的 D19 复核（报告内 `content*.py:NNN` 引用）由 closer 用修正版逻辑跑一遍；KIT 侧已核 37/37。
- builder 侧教训（已记入本报告，供后家参考）：core-it 不是 zh-cn 的符号链接——批量修复必须把 core-it 单列一行（本次 run2 漏两处 D head，run3 补）；pt 注文 p.para 首行基线与字号无关，降字号须算双行基线或取单行；G14 上游审计在旧样式基线（0 个 #f0eee5 盒）上断言，须用 patch-only 绝对检查替代；G15a pdfdiff 只归一化 OLD 侧，基线须用 plain 多重集。

## §11 zh-tw 字体面修复（D52，2026-11-15；重校 FAIL 驱动）

- 缺陷（REPROOF §11，D51）：patched zh-tw 版以 SC 面渲染繁体中文，已发版为 TC 面。证据：生产 zh-tw svglib 为 `_tc_index` + TC 家族名，已发版印 PDF `pdffonts` 嵌 `NotoSansCJKTC/SerifCJKTC`；patched run2 版为 `_sc_index` + SC 家族名，重建印 PDF 嵌 SC 面。机制 `base_core_for()` 规定 reader zh-tw 用 `core-zh-tw`（TC 面）作基底；builder 误用 fanout zh-tw（SC 面）+ 安装，未改写面。U+8AAA 說 SC vs TC 差 1728/14400 像素（12%），`說` 在本版正文出现 13 次。门禁全绿未能检出（字符多重集对字体面不敏感）。
- 修复范围：只动 zh-tw 一版。`svglib.py` 手术式改写回 TC 面（7 行），其余 11 版的 patched/、logs/、KIT 一律未动（其余 11 版 33 件交付物 SHA 与 §9 全值一致，复核见 fix 工日志）；content 文件未动。

### 改写行全表（`patched/2026-w46-it-zh-tw/svglib.py`）

| 行 | 旧 | 新 |
|---|---|---|
| 11 | `def _sc_index(path):` | `def _tc_index(path):` |
| 15 | `if f.getname()[0].endswith("SC"):` | `if f.getname()[0].endswith("TC"):` |
| 25 | `_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}` | `_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}` |
| 49 | 注释 `"Newsreader, Noto Serif CJK SC"` | `Noto Serif CJK TC` |
| 52 | 注释 `Noto Serif CJK SC` | `Noto Serif CJK TC` |
| 76 | `_FAMILY` `"serif": "Noto Serif CJK SC"` | `"Noto Serif CJK TC"` |
| 77 | `_FAMILY` `"sans": "Noto Sans CJK SC"` | `"Noto Sans CJK TC"` |

- 不改行（`grep -ni sc` 全量判定）：L114 `Noto Sans CJK SC/TC` 已是双面通称，fix2 引言对两面均成立，留；L23/24 `NotoSansCJK-Regular.ttc` 路径无面后缀（面由 `_tc_index` 运行时选），留；L57 `Noto Sans CJK <variant>` 通称，留；`esc`、ASCII 等为 grep 假命中，无面语义，留。`_char_font` 无面字面——它返回类名（serif/sans/deja），发出面由 `_FAMILY`（L76/77，已改）决定。

### 两项核对（缺一不可，均通过）

1. 改写前后 diff 仅限面相关行：`diff` 改前备份 vs 改后文件 = 上表 7 行，无他行（`fix-zh-tw/diff-before-after.txt`）。
2. 改后文件 = fanout 版 + D1+D5 安装 + TC 面：fanout→改后 diff 132 行 vs fanout→改前 diff 112 行（与 de/en/zh-cn 的 112 行模式一致，ja 179、ko 126 为下标改写所致）；两 diff 相减仅差上表 7 行（另有 `_D5_READER` latin/cjk 读者差与 kinsoku 行号移位，均系既有基底差）。运行核实：改后 `_IDX` 四 TTC 均为 index 3，与生产 TC 版 `_IDX` 逐值相同。

### 重建（run3，仅 zh-tw；run.py + render.py + webpdf + export）

| 门 | run3 |
|---|---|
| 总分 | **20/20**（19 计分门全绿 + G15b 仅记录行） |
| G1 run | PASS TOTAL=150 OVF=0 HDW=0 |
| G2 head_check / G3 census / G4 render / G5 webpdf | PASS 0 / PASS rc=0 / PASS print=7,500,102B / PASS web=983,685B |
| G6 occlusion / G7 p8 extract / G8 p8 compare | PASS 0 / 150/150 / keydiff=[137, 138, 139] |
| G9 freeze / G10 freeze-diff / G11 spill / G12 boxtitle | PASS 8/8 / PASS rc=0 / PASS 0 / PASS 0 |
| G13 edge / G14 creambox | PASS touches=0 nears=0 / PASS defects=0 |
| G15a pdfdiff / G15b（仅记录）/ G15c exporter / G16 quotes | PASS IDENTICAL（SEP 72, SEP+CJK 15, WORD 1）/ rc=1 / PASS UNEXPECTED=0, entries=648, exercises=150 / PASS 0 |
| D18 / D37 | 155.2px / N/A（与 run2 同值） |

- 归一化对照：run3 vs run2 `GATES-SUMMARY` 除 tag 行与 G4/G5 字节外逐字相同；`pdfdiff`/`verify`/`textexp`/`measure` run3 日志与 run2 逐字节相同；G10 freeze-diff added_strings 总量 run2 = run3 = 1591。
- `pdffonts` 复核（run3）：印 PDF 嵌 `NotoSansCJKtc` ×16、`NotoSerifCJKtc` ×7；网 PDF 嵌 `LucernaNotoSansCJKTC` ×16、`LucernaNotoSerifCJKTC` ×7；`CJKsc/CJKSC` 面 0 处（印/网皆无 SC 残留）。SVG 全版 `font-family="Noto Sans CJK TC"` ×347、`"Noto Serif CJK TC"` ×268，SC 面 0 处。

### 新旧 SHA 对照（zh-tw；§9 已更新为 run3 值）

| 件 | run2（SC 面，作废） | run3（TC 面，终轮） |
|---|---|---|
| 印 PDF `The-Lucerna-VOL3-it-zh-tw.pdf` | 7,490,560 B / `73ae0b90…dad5e67` | 7,500,102 B / `46c50a7df2e8a0ff16f58346fd2ac1f70af21616ddbbef709da803bbf6964682` |
| 网 PDF `2026-w46-it-zh-tw.web.pdf` | 978,308 B / `277447a3…942eec` | 983,685 B / `b36c81097f8b63b12f4a65e006ce9ee17e7e369e2285593c2572b203545085d7` |
| text `2026-w46-it-zh-tw.text.md.new` | 52,971 B / `f2b1c9d93e8821e89383880647da465939be776ddd52981987384194f4da0adc` | 52,971 B / 同值（实测 byte-identical，导出与面无关） |

- KIT 已重 pin 为 run3 值（印/网新 SHA，text 注明 run2 同值；末节门禁行 run2→run3，数值不变）。closer 同步 zh-tw 时取 run3 交付物与 `logs/2026-w46-it-zh-tw/GATES-SUMMARY-run3.txt`。

### D19 重核（D48 修正版逻辑，修复后重跑）

- TOTAL 77，PASS 77，FINDING 0（KIT 37 处 + 本报告 40 处，与重校 v1 同值）。svglib 改动不影响 D19 引用行（引用行在 content 文件内，未动），实测确认。

### 本次一并修正的报告文字（只改文字，不动交付物）

1. entries 计数：es/ja/ko/nl/zh-cn/core-it 六版实测 647（§1–§6 各表原一律写 648），已逐版更正；de/en/fr/pt/ru/zh-tw 648 不变。
2. pt D37 注记：原称余量 +5.1pt 有误——门禁实测行末 1433.0px、余量 +4.9pt；按注记引用的 1432.6px 同算式应为 +5.2pt，自相矛盾；已改为 +4.9pt 并注明（§4 表格原已是 +4.9pt，未动）。
3. §6 zh-tw 表头 run2（终轮）→ run3（终轮）：run3 各门数值与 run2 相同（上表），仅终轮轮次变了。
