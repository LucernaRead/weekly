# GATE-LOG — W47 core-pt 独立复校（fix1 后，re-proof）

- 复校员：独立复校。日期：2026-11-11。对象：`production/2026-w47/core-pt/`，fix1 本地 commit `4b688318`（未 push）。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-pt1/`；TMPDIR = 该目录下 `tmp/`。
- 本日志只记命令与结果；结论与缺陷见 `PROOF-NOTE.md`。

## §0 探针与 SHA

```
$ echo test | git -C ~/workspace/weekly-git hash-object -w --stdin
9daeafb9864cf43055ae93beb0afd6c7d144bfa4          # 通
$ echo "probe pt1 ..." > hidden_files/w47/probe-proof-core-pt1.txt   # 写成功
$ cd production/2026-w47/core-pt && sha256sum A-Lucerna-VOL4.pdf A-Lucerna-VOL4-web.pdf 2026-w47-pt-zh-cn.text.md
98f44af82f82df7c7fec1014fff7098d0448bf775b2aeda484f2e69233235181  A-Lucerna-VOL4.pdf        (25,311,644 B) ✓ 与任务一致
d1d26cd70823e83e6165268b055b481981cd5cc3bdcffaec40042f7bf28a521f  A-Lucerna-VOL4-web.pdf    (1,608,359 B)  ✓
9dd550b6d7d19703ce6643357e9aad3f5367dfc40379bd41d56db999fd36afbe  2026-w47-pt-zh-cn.text.md (36,876 B)    ✓
```

## §1 gates_core.py — 16/16 PASS

```
$ tools/venv/bin/python gates_core.py   (cwd: production/2026-w47/core-pt)
> gates.log
[PASS] P1 VOL.4 + week dates :: top strip
[PASS] P1 subtitle topics :: subtitle line
[PASS] footer+page line 8/8 :: VOL.4 ZH footer + page line on all pages
[PASS] no VOL.3 edition label residue :: VOL.3 may appear only as the cited promising issue in the P7 disclosure
[PASS] press-time note + final named :: P4 press-time note present; final date named
[PASS] P1 masthead lines fit 1820 :: {330: 319.2, 372: 682.7}
[PASS] same-baseline ink collisions = 0 :: 0 collisions
[PASS] page-frame ink crossings = 0 :: 0 crossings | min margins L/R/T/B = [47.0, 47.9, 35.0, 33.0]
[PASS] P6 chart-label coverage <30% :: [('dias úteis', 0.0), ('10 dias', 0.0), ('fins de semana e feriado', 0.0), ('5 dias', 0.0)]
[PASS] gloss items enumerated :: {2: 6, 3: 6, 4: 6, 5: 6, 6: 5} total 29
[PASS] gloss headwords survive in render :: 0 missing
[PASS] P7 quotes 2x + page tag + ZH on P7 :: 8 quotes; all (2, True, True)
[PASS] readers corner disclosure :: PT/ZH verbatim True, ZH example label True, VOL.5 carry True
[PASS] images embedded + credits 5/5
[PASS] P7 quotes clear of preview box :: max quote-region baseline 2373.17
[PASS] P1 headline <= 56 non-space chars :: 41 chars
FAILURES: none
```

## §2 occlusion audit — 0 flags

```
$ tools/venv/bin/python tools/occlusion_audit.py <core>/svg --json <scratch>/occlusion.json
selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
<core>/svg: 0 flags
occlusion.json: {"flag_count": 0, "flags": []}
```
注：首次调用误把 `--json` 当开关（须带输出路径），rc=2；按 `--help` 更正后重跑，rc=0。审计对“文本溢出自盒底 / 盒题横向溢出”有盲区——相关项以 §3 + §4 的 PIL 真墨为准，不以此门代证。

## §3 creambox.py 全版扫描 — 31 盒，0 真溢出

```
$ md5sum hidden_files/w47/tools/creambox.py
ee7a55d8b2057cf4ad42a97bb1197383      # 正典，与 fix1 核对一致；未用窄带 creambox_check.py 作证据
$ python3 hidden_files/w47/tools/creambox.py <core>/svg/*.svg > creambox-all.log
rc=0；31 盒
```
逐盒裁定（inside-only 口径；BELOW-WINDOW 6 处全为已知假阳性类）：

| 页 | 盒 | inside-only | BELOW-WINDOW | 裁定 |
|---|---|---|---|---|
| P1 | y=786 | +45.0 | +37.0 `AGORA VOCÊ 即学即练`（下块标题） | 假阳性 |
| P1 | y=588 | +51.0 | — | 通过 |
| P1 | y=1238 | +16.0 / desc +9.7 | — | 通过 |
| P1 | y=1874 **D1** | **+20.4 / desc +14.4**，末行基线 2327.6 | +38.0 quiz 标题行（下块） | 假阳性；盒内通过（另见 §4 真墨 +16） |
| P2 | y=605 | +48.1 | — | 通过 |
| P2 | y=858 | +47.7 | — | 通过 |
| P2 | y=200 | +11.4 / desc +4.9 | — | 通过 |
| P2 | y=545 | +4.4 / desc −1.6（末行中文，无降部） | — | 假阳性（§4 真墨 +4.0） |
| P2 | y=1618 ×4 | +60.8 / +31.5 | +32.0 `Atenção: …`（盒下独立段落） | 假阳性（2× 裁切目视：段落位于盒下白纸上，见 crop-p2-atencao.png） |
| P3 | y=200 | +47.7 | +37.0 `UM DIA, DOIS SENTIDOS`（下块标题） | 假阳性 |
| P3 | y=200 **D2** | **+10.4 / desc +3.9**，末行 `16h30.` 基线 540.6 | — | 通过（另见 §4 真墨 +11） |
| P3 | y=577 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +4.0） |
| P3 | y=877 | +19.4 | — | 通过 |
| P4 | y=270 | +47.7 | — | 通过 |
| P4 | y=200 | +110.8 | — | 通过 |
| P4 | y=602 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +4.0） |
| P5 | y=200 | +46.6 | — | 通过 |
| P5 | y=777 | +47.7 | — | 通过 |
| P5 | y=200 | +5.4 / desc −1.1（末行 `2027.`，数字无降部） | — | 假阳性（§4 真墨 +6.0） |
| P5 | y=539 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +3.5） |
| P6 | y=343 | +47.7 | — | 通过 |
| P6 | y=200 **D3** | **+13.2 / desc +6.9**，末行 `Página do Participante.` 基线 840.8 | — | 通过（另见 §4 真墨 +9） |
| P6 | y=866 | +19.4 | — | 通过 |
| P6 | y=1594 ×2 | +40.0 / +62.0 | +42.0 `EXERCÍCIOS 第6版练习`（下块标题） | 假阳性 |
| P7 | y=200 工具盒 | +26.7 | — | 通过 |
| P7 | y=1098 工具盒 | +4.5 / desc −1.5（末行中文） | — | 假阳性（§4 真墨 +3.5） |
| P7 | y=1394 工具盒 | +22.6 | — | 通过 |
| P8 | — | 0 盒 | — | — |

P7-TOOLBOX 汇总：3 盒，最小盒内 clearance +4.5，最小 desc-clear −1.5（即上表中文末行，假阳性）。

## §4 PIL 真墨复测（渲染 PNG cards，1950×2700；脚本 pil_measure.py / pil_desc.py；2× 裁切 crop-d1/d2/d3/d7.png + crop-p2-atencao.png）

```
D1 rows 2280-2360: [[2285, 2303], [2312, 2332], [2349, 2350]]
D1: box bottom=2348 last ink row=2332 ink clearance=+16px PASS >=+5
D2 rows 500-570: [[500, 514], [526, 540]]   (552-570 无墨)
D2: box bottom=551 last ink row=540 ink clearance=+11px PASS >=+5
D3 rows 790-875: [[796, 811], [825, 845]]   (855-875 无墨)
D3: box bottom=854 last ink row=845 ink clearance=+9px PASS >=+5
D7 model lines found: 10
  673.9 ink-right=1797 +65px | 693.4 ink-right=1813 +49px | 712.9 ink-right=1840 +22px
  732.4 ink-right=1797 +65px | 751.9 ink-right=1838 +24px | 771.4 ink-right=1801 +61px
  790.9 ink-right=1778 +84px | 810.4 ink-right=1838 +24px | 829.9 ink-right=1839 +23px
  849.4 ink-right=1723 +139px
  model words counted from SVG lines: 90 (= 88 + 'Texto modelo:' ×2)
desc-clear 负值盒真墨复测（末行墨底 vs 框底）：
  P2 E-VOCÊ  bottom 880   last ink 876  +4.0px | P3 E-VOCÊ  bottom 851   last ink 847  +4.0px
  P4 E-VOCÊ  bottom 876   last ink 872  +4.0px | P5 E-VOCÊ  bottom 782.5 last ink 779  +3.5px
  P5 NUMBERS bottom 513   last ink 507  +6.0px | P7 A-PALAVRA bottom 1372.5 last ink 1369 +3.5px
```
D1 备注：2349–2350 两行墨为盒下 quiz 分隔线（qy=2350），在框底 2348 之下，不计入盒内墨底；裁切目视确认线在盒外。

## §5 p8 / freeze

```
$ tools/venv/bin/python tools/p8.py extract --p8 <core>/svg/p8-avaliacao.svg --total 150
noted set = 150 of 150 (parse: lines)   # 首次调用漏 --p8 参数 rc=2；补参数后 rc=0
$ tools/venv/bin/python tools/p8.py compare --core-dir <core> --edition-dir <core> --target pt --total 150
core 150 noted / edition 150 noted — status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]
$ tools/venv/bin/python tools/freeze.py baseline --build <core> --core-svg <core>/svg --out <scratch>/freeze
8× "OK ... produced <same sha>"；core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
$ tools/venv/bin/python tools/freeze.py diff --core-svg <core>/svg --edition-svg <core>/svg
p6: +0/-0；p7: +0/-0；p8: +0/-0；TOTAL added CJK characters: 0
```
注：`freeze_direct` 无此子命令（与 fix1 核对一致：freeze.py 仅 baseline/diff）；以 baseline 8/8 + diff 自比为 freeze 证据。

## §6 印/网文字层 + 字号 + 弯引号 + ABSTRACT

```
$ pdftotext -layout A-Lucerna-VOL4.pdf print-all.txt; pdftotext -layout A-Lucerna-VOL4-web.pdf web-all.txt
print bytes 104916 words 7262；web bytes 104916 words 7262；word multiset diff: 0；only-in-print: []；only-in-web: []
$ pdfinfo 两版：Pages 8；Page size 1462.5 x 2025 pts
$ tools/venv/bin/python -c (fitz spans): pages 8；min font overall 10.12pt；P8 min 10.125pt；sizes ≤11pt: 10.12×604, 10.5×8, 10.88×71
   → ≥ SOP §1.1 下限 9.75pt ✓
$ 弯引号（印/网一致）：U+201C 3，U+201D 3，U+2019 0，« 40，» 40
$ cat ABSTRACT.txt (524 B)：首句 "A Lucerna 葡萄牙语周报 VOL.4：…" 含 masthead ✓（SOP §9）
```

## §7 keycheck — 印 PDF RESPOSTAS-only vs text.md Respostas

```
脚本：keycheck.py（初版）→ keycheck3.log（终版，顺序解析）
$ pdftotext -f 8 -l 8 -raw A-Lucerna-VOL4.pdf print-p8-raw.txt
text.md answers parsed: 150，1..150 全有
print RESPOSTAS answers parsed: 150，1..150 全有
common: 150；diffs: 0；only in md: []；only in print: []
```
解析器 artifact 记录：初版 33 个“差异”全为 (a) text.md `**Página N**` 页眉混入答案值、(b) PDF 简析分隔符 `—` 后无空格；次版剩余 1 项 (1, '', '—主语 + 动词 + 方式）源于答案 134 内嵌 `1 a 1.` 产生的幽灵键（两侧对称）；终版以“严格递增 1→150 顺序解析”排除幽灵键后 diff 0。Q134 全句 `O Grêmio empatou por 1 a 1.` 已目视确认两处俱全；Q150 `✓ 范文见本版 H 区（88 词）`一致。

## §8 150 键手验（逐题语义，非仅 compare）

方法：text.md 全文通读后，逐题对照正文核对题干与键；结果 150/150 语义正确，零错误。按页小结：
- P1（1–10）：1 consciência · 2 feriado · 3 sexta · 4 três · 5 6 · 6 decidem · 7 B · 8 B · 9 C · 10 B — 全对。
- P2（11–28）：11–15 B×5 · 16 cai · 17 dura · 18 descansamos · 19 abrem · 20 aproveita · 21 3 · 22 1695 · 23 2023 · 24 27 · 25 a · 26 b · 27 c · 28 d — 全对。
- P3（29–46）：29 C · 30 A · 31 B · 32 B · 33 A · 34 quilombo · 35 resistência · 36 escravizados · 37 líder · 38 memória · 39 combate · 40 morreu · 41 nasceu · 42 defendeu · 43 formaram · 44–46 造句句合法 — 全对。
- P4（47–64）：47 A · 48 B · 49 B · 50 B · 51 A · 52 b · 53 a · 54 d · 55 c · 56–58 mais · 59 menos · 60 empatou · 61 venceu · 62 abriu · 63 garantiu · 64 foram — 全对。
- P5（65–82）：65 B · 66 B · 67 A · 68 B · 69 B · 70 gabarito · 71 oficial · 72 extraoficiais · 73 espera · 74 nota · 75 pesa · 76 sairá · 77 publicarão · 78 decidirá · 79 chegará · 80 Verdadeiro · 81 Falso · 82 Verdadeiro — 全对。
- P6（83–100）：83 B · 84 A · 85 B · 86 B · 87 B · 88 A · 89 B · 90 B · 91 B · 92 B · 93 serão · 94 contam · 95 fixa · 96 pesa · 97 prazo · 98 dia útil · 99 coerência · 100 chute — 全对；83–86 算术：16–30 日共 15 天 = 10 工作日 + 5 休息日。
- P7（101–112）：101 em · 102 numa · 103 é · 104 B · 105 empatou · 106 venceu · 107 abriu · 108 B（saíram）· 109 sair · 110 for · 111 tiver · 112 B（sair）— 全对。
- P8（113–150）：113 A · 114 A · 115 B · 116 A · 117 B · 118 A · 119 A · 120 B（5 小时）· 121 B · 122 A · 123 B · 124 B · 125 A（周六 21，36 轮）· 126 B · 127 A · 128 A · 129 B · 130 B · 131 A · 132 B · 133–136 造句 · 137–140 翻译 · 141 c · 142 d · 143 b · 144 a · 145–149 A · 150 ✓ 范文（88 词）— 全对。

## §9 外部事实抽查（2026-11-11 检索；6 组全过）

- Copa：比分/总比分/点球/决赛（见 PROOF-NOTE §4.1；来源 sounoticia、sportradar、obairrista、brasileirao.com.br、mktesportivo）。
- F1：Norris 胜 / Verstappen 第 2 / Hadjar 第 3 / Mercedes 车队冠军（Reuters 经 businessday、appistos 引 FIA 战报、racer.com）。
- Enem：Edital 64/2026、10º dia útil、27–30 Nov 窗口、2027 年 1 月出分（focaedu、estacio、centerdrop、techtudo、sisu.pro.br）；自算工作日：11 月 16 日起计，扣 20 日假日与两周末，10º dia útil = 11 月 30 日；16–30 日 = 15 天 = 10 + 5。
- Consciência Negra：1695、12.519/2011、14.759/2023、2026 年 11 月 20 日周五（afrocultura、axefinder、ocalendario、pt.wikipedia）。
- Seleção：巴西 × 新加坡 11 月 17 日周二 7h（CBF 官网 cbf.com.br）。
- 日历骨架：`TZ=America/Sao_Paulo date -d` 核 13 个日期星期全符；Enem 报名 5,051,345 人（Inep Painel，gov.br）；Nubank Parque 现名（2026 年 5 月 4 日更名，en/pt.wikipedia）。

## §10 D5 传播核查（grep 实测，非转述）

```
core-pt 现文案：content34.py:134 与 text.md:215 均为 "... o título 冠军 ..."
fanout 各版 content34.py:134：
  pt-fr: o título champion ｜ pt-de: o título Meister ｜ pt-es: o título campeón
  pt-it: o título campione ｜ pt-nl: o título kampioen ｜ pt-ru: o título чемпион
  pt-ja: o título 優勝者 ｜ pt-ko: o título 우승자 ｜ pt-en: o título title（正确）
  pt-zh-tw: o título 冠軍（同义歧义）
→ 8 版取“人”义，1 版正确，1 版沿用歧义，1 版（zh-cn 核心）为源头。
```
