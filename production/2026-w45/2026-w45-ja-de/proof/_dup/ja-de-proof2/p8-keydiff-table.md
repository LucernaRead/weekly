# P8 keydiff 逐项对照（第二轮独立校对，p8.py compare 显式双路径 --total 150）

结论：CLEAN，核心 noted 150 = 本版 noted 150，missing=[] extra=[] uncertain=[]；keydiff 21 项 = 2 真重定向 + 1 提示本地化落入 keydiff + 18 括号分支伪影；提示本地化总数 2 项（#139 不在 keydiff 内，#140 在内）。

与核心逐段（绕排重组后）完全相同的段：0 段（修复前唯一相同段 #37 已消除）。

| 题号 | 核心印刷段 | 本版印刷段 | 提取键（核心 → 本版） | 真键是否相同 | 裁定 |
|---|---|---|---|---|---|
| 1 | 3 — 文化日在11月3日（周二） | 3 — Der Kulturtag ist am 3. November (Dienstag) | 3 — 文化日在11月3日 → 3 — Der Kulturtag ist am 3. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 2 | 9 — 读书周到11月9日（周一） | 9 — Die Lesewoche läuft bis zum 9. November (Montag) | 9 — 读书周到11月9日 → 9 — Die Lesewoche läuft bis zum 9. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 5 | 7 — 神户灯光秀从7日（周六）开始 | 7 — Die Beleuchtung in Kobe beginnt am 7. (Samstag) | 7 → 7 — Die Beleuchtung in Kobe beginnt am 7. | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键）；另伴 dash→paren 方法翻转，真键仍不变 |
| 7 | B — 文化日在11月3日（周二） | B — Der Kulturtag ist am 3. November (Dienstag) | B — 文化日在11月3日 → B — Der Kulturtag ist am 3. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 8 | C — 读书周到11月9日（周一） | C — Die Lesewoche läuft bis zum 9. November (Montag) | C — 读书周到11月9日 → C — Die Lesewoche läuft bis zum 9. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 9 | B — 立冬在11月7日（周六） | B — 立冬 ist am 7. November (Samstag) | B — 立冬在11月7日 → B — 立冬 ist am 7. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 29 | A — 文化日在11月3日（周二） | A — Der Kulturtag ist am 3. November (Dienstag) | A — 文化日在11月3日 → A — Der Kulturtag ist am 3. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 32 | B — 工艺展到11月8日（周日） | B — Die Ausstellung läuft bis zum 8. November (Sonntag) | B — 工艺展到11月8日 → B — Die Ausstellung läuft bis zum 8. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 65 | A — 万圣节在10月31日（周六） | A — Halloween war am 31. Oktober (Samstag) | A — 万圣节在10月31日 → A — Halloween war am 31. Oktober | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 69 | C — 横滨中区民祭在11月8日（周日） | C — Bürgerfest Naka, Yokohama, 8. November (Sonntag) | C — 横滨中区民祭在11月8日 → C — Bürgerfest Naka, Yokohama, 8. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 78 | ○ — ハロウィンは10月31日（土） | ○ — Halloween war am 31. Oktober (Samstag) | ○ — ハロウィンは10月31日 → ○ — Halloween war am 31. Oktober | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 101 | 27 — 读书周从10月27日（周二）开始 | 27 — Die Lesewoche begann am 27. Oktober (Dienstag) | 27 → 27 — Die Lesewoche begann am 27. Oktober | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键）；另伴 dash→paren 方法翻转，真键仍不变 |
| 113 | A — 文化日在11月3日（周二） | A — Der Kulturtag ist am 3. November (Dienstag) | A — 文化日在11月3日 → A — Der Kulturtag ist am 3. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 115 | A — 日本大赛第1战在10月24日（周六） | A — Spiel 1 der Japan Series war am 24. Oktober (Samstag) | A — 日本大赛第1战在10月24日 → A — Spiel 1 der Japan Series war am 24. Oktober | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 117 | B — 万圣节在10月31日（周六） | B — Halloween war am 31. Oktober (Samstag) | B — 万圣节在10月31日 → B — Halloween war am 31. Oktober | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 118 | A — 立冬在11月7日（周六） | A — 立冬 ist am 7. November (Samstag) | A — 立冬在11月7日 → A — 立冬 ist am 7. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 137 | 文化日是11月3日。 — 对照第3版 | Der Kulturtag ist am 3. November. — Siehe Seite 3 | 文化日是11月3日。 → Der Kulturtag ist am 3. November. | 否（合法重定向） | 真重定向（E区翻译题，ZH→DE，合法） |
| 138 | 乱扔垃圾，要罚2,000日元。 — 对照第5版 | Wer Müll wegwirft, zahlt 2.000 Yen Strafe. — Siehe Seite 5 | 乱扔垃圾，要罚2,000日元。 → Wer Müll wegwirft, zahlt 2.000 Yen Strafe. | 否（合法重定向） | 真重定向（E区翻译题，ZH→DE，合法） |
| 140 | 神戸の紅葉のライトアップを見に行きたいです。 — 对照第6版（神户的灯光秀） | 神戸の紅葉のライトアップを見に行きたいです。 — Siehe Seite 6 (Kobe-Beleuchtung) | 神戸の紅葉のライトアップを見に行きたいです。 — 对照第6版 → 神戸の紅葉のライトアップを見に行きたいです。 — Siehe Seite 6 | 是 | 提示本地化落入keydiff（真键日语原样；paren分支把提示干并入提取键） |
| 146 | A — 借りられます＝能借（可能形） | A — 借りられます = ausleihen können (Potentialform) | A — 借りられます＝能借 → A — 借りられます = ausleihen können | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |
| 147 | A — 读书周到11月9日（第7版） | A — Die Lesewoche läuft bis zum 9. November (Seite 7) | A — 读书周到11月9日 → A — Die Lesewoche läuft bis zum 9. November | 是 | 括号分支伪影（真键逐字相同；提取键差异仅因提示译文被并入提取键） |

不在 keydiff 的提示本地化第 2 项：#139 核心 `読書週間は10月27日から始まります。 — 对照第7版` → 本版 `読書週間は10月27日から始まります。 — Siehe Seite 7`（无括号、dash 分支键相等）。
