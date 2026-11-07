# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 -> FR x JA edition transform. SINGLE SOURCE for all
explanation-layer edits (fix-round edits go here, never only into content
files). Every replacement is a whole line or a unique literal, asserted.
French target text is NEVER a replacement target. Registry type names
(Chinese internal metadata, never printed) are intentionally kept, per the
W43 FR x JA precedent; they are the only Chinese strings allowed to survive
in code, and none of them is printed.
Run from this directory: ../../tools/venv/bin/python transform.py
with TRANSFORM_ROUND=1, then =2, =3... Re-running a round after it was
applied fails loudly (old strings gone) -- restore from the core copy
first; never run the same round twice on the same tree.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

ROUND = int(os.environ.get("TRANSFORM_ROUND", "1"))
_SECTION = [1]


def section(n):
    _SECTION[0] = n


# Core P8 noted set, measured from the shipped core P8 SVG with
# tools/p8.py extract --total 150 (noted 97/150, parse: joined). This
# becomes the edition's explicit PRINT_NOTES set (W43 FR x JA precedent),
# so the Japanese edition prints notes for exactly the same exercises
# even though Japanese notes are longer than the core's <=10-char rule.
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33,
               34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71,
               72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95,
               96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
               116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
               129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141,
               142, 143, 144, 145, 146, 147, 148, 149, 150]
assert len(PRINT_NOTES) == 97, len(PRINT_NOTES)
BARE = sorted(set(range(1, 151)) - set(PRINT_NOTES))
assert len(BARE) == 53, len(BARE)


def rep(text, old, new, count=1):
    n = text.count(old)
    assert n == count, f"expected {count}x {old[:60]!r}, found {n}x"
    return text.replace(old, new)


def apply_file(fname, pairs):
    if _SECTION[0] != ROUND:
        print(f"skip section {_SECTION[0]} for {fname} (ROUND={ROUND})")
        return
    path = os.path.join(HERE, fname)
    text = open(path, encoding="utf-8").read()
    for old, new, *rest in pairs:
        text = rep(text, old, new, rest[0] if rest else 1)
    open(path, "w", encoding="utf-8").write(text)
    print(f"{fname}: {len(pairs)} replacements applied")


def md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()


section(1)
# ---------------- svglib: whole-file swap to the JA core version --------
# (W43 FR x JA precedent). The JA core svglib differs from the W45 FR core
# svglib ONLY in: JP face selection (2 spots) + kinsoku oidashi + SEAM_SLACK.
if _SECTION[0] == ROUND:
    ja_src = os.path.expanduser(
        "~/workspace/goals/lucernaread-social-media-operations/"
        "hidden_files/weekly-report-ja-build/svglib.py")
    assert md5(ja_src) == "d73e23b365676c3618d7e060b835eb4d", md5(ja_src)
    assert md5(os.path.join(HERE, "svglib.py")) == \
        "0703a8814abe388f131c89f3d7ffb946", "core svglib changed?"
    shutil.copyfile(ja_src, os.path.join(HERE, "svglib.py"))
    print("svglib.py: swapped to JA core version d73e23b3...")

# ---------------- OUT redirect (all 5 content modules) ------------------
for _f in ["content12.py", "content34.py", "content56.py",
           "content7.py", "content8.py"]:
    apply_file(_f, [
        ("weekly-report-w45-fr-core", "weekly-report-w45-fr-ja"),
    ])

# ---------------- bslib4: footer + page line + gloss prefix ------------
apply_file("bslib4.py", [
    ('"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
     '"Le Lucerna · フランス語週刊 VOL.3 · 本文はフランス語 · 解説は日本語"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"{n} ページ（全 {total} ページ）"'),
    ('("译注｜" + s', '("解説 — " + s'),
])

# ---------------- content12: P1 + P2 ------------------------------------
apply_file("content12.py", [
    ('# ================= P1 · 头版 (A2) =================',
     '# ================= P1 · front page (A2) ================='),
    ('# ================= P2 · 生活 (A2) =================',
     '# ================= P2 · everyday life (A2) ================='),
    ('"VOL. 3 · 总第 3 期"', '"VOL. 3 · 通算第 3 号"'),
    ('"HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语"',
     '"HEBDOMADAIRE EN FRANÇAIS · 毎週一号 · フランス人が読んでいるフランス語を読む"'),
    ('"法 语 周 报 · VOL.3 · 决 赛 周 末"', '"フ ラ ン ス 語 週 刊 · VOL.3 · 決 勝 週 末"'),
    ('"周一开学 · 全法同步复课"', '"月曜開校 · フランス全国で一斉に再開"'),
    ('"大师赛开赛 · 音乐节开幕 · 详见第 2 版"', '"マスターズ開幕 · 音楽祭開幕 · 詳しくは2ページ"'),
    ('"法语正文 · 简体中文讲解 — 给简体中文读者的版本"',
     '"フランス語テキスト · 日本語の解説 — 日本語読者のための版"'),
    ('"SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末"',
     '"SPORT · CULTURE · GASTRONOMIE · LA UNE · 決勝週末"'),
    ('f.gloss("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。")',
     'f.gloss("se jouer 決まる、行われる · une finale 決勝 · une demi-finale 準決勝 · un quart de finale 準々決勝 · une nocturne 夜のイベント · un frisson ぞくぞくする興奮 · la coquille Saint-Jacques ホタテ。")'),
    ('f.box("LES DATES · 决赛周末日程"',
     'f.box("LES DATES · 決勝週末の日程"'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · さあ練習", 25)'),
    ('f.ex("A2", "完成句子", "finales", "周日 8 日举行决赛"',
     'f.ex("A2", "完成句子", "finales", "決勝は日曜8日"'),
    ('f.ex("A2", "完成句子", "nocturne", "周六 7 日晚是最后夜场"',
     'f.ex("A2", "完成句子", "nocturne", "最終ナイトイベントは土曜7日の夜"'),
    ('f.ex("A2", "完成句子", "coquilles", "波尔诺曼底卖扇贝"',
     'f.ex("A2", "完成句子", "coquilles", "ポール＝アン＝ベッサンでホタテを売る"'),
    ('f.ex("B1", "完成句子", "reprend", "周一 2 日全法复课"',
     'f.ex("B1", "完成句子", "reprend", "月曜2日にフランス全国で再開"'),
    ('f.ex("B1", "完成句子", "samedi soir", "半决赛后才知道决赛选手"',
     'f.ex("B1", "完成句子", "samedi soir", "準決勝の後でないと決勝進出者は分からない"'),
    ('f.ex("B1", "完成句子", "saveurs", "三个决赛：网球、刺激、美味"',
     'f.ex("B1", "完成句子", "saveurs", "3つの決勝：テニス、スリル、味覚"'),
    ('"本周日程 · 11 月 2 日至 8 日"', '"今週の日程 · 11月2日から8日まで"'),
    ('"周末决赛结果周六晚、周日揭晓。"', '"週末の決勝の結果は土曜夜と日曜に判明します。"'),
    ('"DANS CE NUMÉRO · 本期目录"', '"DANS CE NUMÉRO · 今号の内容"'),
    ('"决出胜负；上演。本周末一切都将见分晓。"', '"決まる、行われる。今週末はすべてが決まります。"'),
    ('p.text(bx + 22, 1914, "EN BREF · 快讯", 24, "sans", True, OLIVE)',
     'p.text(bx + 22, 1914, "EN BREF · 短信", 24, "sans", True, OLIVE)'),
    ('p.text(MX, qy + 36, "QUIZ ÉCLAIR · 闪电问答", 26, "sans", True, OLIVE)',
     'p.text(MX, qy + 36, "QUIZ ÉCLAIR · クイズ", 26, "sans", True, OLIVE)'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"トップ記事を読んで正解を選ぼう · 答えは8ページ"'),
    ('qf.ex("A2", "单选", "C", "决赛在周日 8 日"',
     'qf.ex("A2", "单选", "C", "決勝は日曜8日"'),
    ('qf.ex("A2", "单选", "A", "扇贝节在滨海波尔"',
     'qf.ex("A2", "单选", "A", "ホタテ祭りはポール＝アン＝ベッサン"'),
    ('qf.ex("A2", "单选", "B", "周一 2 日早上全区复课"',
     'qf.ex("A2", "单选", "B", "月曜2日の朝に全学区が再開"'),
    ('qf.ex("A2", "单选", "A", "最后夜场周六 7 日"',
     'qf.ex("A2", "单选", "A", "最終ナイトイベントは土曜7日"'),
    ('p.band("VIE QUOTIDIENNE · 生活", "Le Lucerna", "NIVEAU A2 · La rentrée · 开学复课")',
     'p.band("VIE QUOTIDIENNE · 日常生活", "Le Lucerna", "NIVEAU A2 · La rentrée · 新学期の始まり")'),
    ('f.gloss("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。")',
     'f.gloss("la rentrée 新学期の始まり、再開 · reprendre 再開する、再び始める · un cartable 学校かばん · un décalage ずれ、時差 · en revanche それに対して、反対に · un rituel 習慣、儀式。")'),
    ('f.bridge("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。")',
     'f.bridge("解説 — une valise スーツケース · une ambiance 雰囲気 · le bilan まとめ、総括。")'),
    ('"说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。"',
     '"月曜の始まりについて話しましょう。月曜の朝どこにいましたか。休みにどの本を読みましたか。フランス語で2文書いて編集部へ送ってください。"', 2),
    ('p.text(ix + 22, yy3 + 26, "ET VOUS ? · 说说你自己", 24, "sans", True, OLIVE)',
     'p.text(ix + 22, yy3 + 26, "ET VOUS ? · あなたはどうですか", 24, "sans", True, OLIVE)'),
    ('p.text(MX, dy + 28, "DIRE LA DATE · 这样说日期", 28, "sans", True, OLIVE)',
     'p.text(MX, dy + 28, "DIRE LA DATE · 日付の言い方", 28, "sans", True, OLIVE)'),
    ('"lundi 2 novembre · 注意：1 日说 le premier，其余用基数词"',
     '"lundi 2 novembre · 注意：1日は le premier、それ以外は基数詞"'),
    ('("lundi 2 novembre", "11 月 2 日星期一 · la rentrée")',
     '("lundi 2 novembre", "11月2日（月） · la rentrée")'),
    ('("mardi 3 novembre", "11 月 3 日星期二 · votes à l\'Assemblée")',
     '("mardi 3 novembre", "11月3日（火） · votes à l\'Assemblée")'),
    ('("mercredi 4 novembre", "11 月 4 日星期三 · sorties cinéma")',
     '("mercredi 4 novembre", "11月4日（水） · sorties cinéma")'),
    ('("samedi 7 novembre", "11 月 7 日星期六 · nocturne et demis")',
     '("samedi 7 novembre", "11月7日（土） · nocturne et demis")'),
    ('("dimanche 8 novembre", "11 月 8 日星期日 · les finales")',
     '("dimanche 8 novembre", "11月8日（日） · les finales")'),
    ('p.text(MX, ey + 28, "EXERCICES · 第 2 版练习", 28, "sans", True, OLIVE)',
     'p.text(MX, ey + 28, "EXERCICES · 2ページの練習", 28, "sans", True, OLIVE)'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"答えは8ページ · 問題はレベルをまたいで出題され、番号順に答えを探してください"'),
    ('e.bridge("用法语补全日期（注意星期与数字）。")',
     'e.bridge("フランス語で日付を補いましょう（曜日と数字に注意）。")'),
    ('e.ex("A2", "完成句子", "lundi", "复课在星期一"',
     'e.ex("A2", "完成句子", "lundi", "再開は月曜日"'),
    ('e.ex("A2", "完成句子", "1er", "11 月 1 日说 le premier"',
     'e.ex("A2", "完成句子", "1er", "11月1日は le premier と言う"'),
    ('e.ex("A2", "完成句子", "samedi", "最后夜场在星期六"',
     'e.ex("A2", "完成句子", "samedi", "最終ナイトイベントは土曜日"'),
    ('e.ex("A2", "完成句子", "dimanche", "决赛在星期日"',
     'e.ex("A2", "完成句子", "dimanche", "決勝は日曜日"'),
    ('e.bridge("用 aller + 动词原形改写（最近将来时）。")',
     'e.bridge("aller + 不定詞で書きかえましょう（近接未来）。")'),
    ('e.bridge("读第 2 版文章，选出正确答案。")',
     'e.bridge("2ページの記事を読んで正解を選びましょう。")'),
    ('e.ex("A2", "单选", "C", "三区同一周一早上复课"',
     'e.ex("A2", "单选", "C", "3つの学区が同じ月曜の朝に再開"'),
    ('e.ex("A2", "单选", "B", "冬令时从 10 月 25 日开始"',
     'e.ex("A2", "单选", "B", "冬時間は10月25日から"'),
    ('e.ex("A2", "单选", "A", "11 月晚上天黑得早"',
     'e.ex("A2", "单选", "A", "11月の夜は早く暗くなる"'),
    ('["rentrée=开学 a", "reprendre=重新开始 b", "cartable=书包 c", "rituel=习惯 d"]',
     '["rentrée=新学期の始まり a", "reprendre=再開する b", "cartable=学校かばん c", "rituel=習慣 d"]'),
    ('instr="把词和释义配对"', 'instr="語と意味を結ぶ"'),
    ('instr="填空"', 'instr="空所補充"', 4),
    ('instr="改写"', 'instr="書きかえ"', 4),
])

# ---------------- content34: P3 + P4 ------------------------------------
apply_file("content34.py", [
    ('# ================= P3 · 文化 (A2→B1) =================',
     '# ================= P3 · culture (A2→B1) ================='),
    ('# ================= P4 · 体育 (B1) =================',
     '# ================= P4 · sport (B1) ================='),
    ('p.band("CULTURE · 文化", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣")',
     'p.band("CULTURE · 文化", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · ハロウィーンと諸聖人")'),
    ('f.gloss("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。")',
     'f.gloss("se déguiser 仮装する、変装する · un sort 魔法、いたずら · une ambiance 雰囲気 · le souvenir 思い出、記念 · confondre 混同する · discret 控えめな、静かな。")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · さあ練習", 25)', 2),
    ('f.bridge("判断对错（Vrai / Faux）。")',
     'f.bridge("正しいか間違っているか判断しましょう（Vrai / Faux）。")'),
    ('f.ex("A2", "阅读判断", "Vrai", "万圣节在 10 月 31 日星期六"',
     'f.ex("A2", "阅读判断", "Vrai", "ハロウィーンは10月31日土曜日"'),
    ('f.ex("A2", "阅读判断", "Vrai", "诸圣节墓园摆满菊花"',
     'f.ex("A2", "阅读判断", "Vrai", "諸聖人の日は墓地が菊でいっぱいになる"'),
    ('f.ex("A2", "阅读判断", "Faux", "菊花绝不能当礼物送人"',
     'f.ex("A2", "阅读判断", "Faux", "菊を贈り物にしてはいけない"'),
    ('f.ex("B1", "阅读判断", "Faux", "11 月 2 日是 jour des morts，不是诸圣节"',
     'f.ex("B1", "阅读判断", "Faux", "11月2日は jour des morts で、諸聖人の日ではない"'),
    ('f.ex("B1", "阅读判断", "Vrai", "文中：le rire d\'abord, le souvenir ensuite"',
     'f.ex("B1", "阅读判断", "Vrai", "本文より：le rire d\'abord, le souvenir ensuite"'),
    ('f.bridge("用 déguisement / tombe / citrouille / souvenir 填空。")',
     'f.bridge("déguisement / tombe / citrouille / souvenir で穴埋めしましょう。")'),
    ('f.ex("B1", "完成句子", "déguisement", "万圣节穿变装服装"',
     'f.ex("B1", "完成句子", "déguisement", "ハロウィーンでは仮装衣装を着る"'),
    ('f.ex("A2", "完成句子", "tombe", "花放在墓碑上"',
     'f.ex("A2", "完成句子", "tombe", "花は墓石に置く"'),
    ('f.ex("A2", "完成句子", "citrouille", "南瓜是万圣节的象征"',
     'f.ex("A2", "完成句子", "citrouille", "かぼちゃはハロウィーンの象徴"'),
    ('f.ex("B1", "完成句子", "souvenir", "诸圣节是纪念之日"',
     'f.ex("B1", "完成句子", "souvenir", "諸聖人の日は記念の日"'),
    ('f.bridge("改写句子（用 ne...jamais / ne...plus / ne...pas）。")',
     'f.bridge("文を書きかえましょう（ne...jamais / ne...plus / ne...pas を使います）。")'),
    ('"jamais + de（无冠词变化）"', '"jamais + de（無冠詞への変化）"'),
    ('"ne...plus = 不再"', '"ne...plus = もう〜ない"'),
    ('"n\'est pas = 不是"', '"n\'est pas = 〜ではない"'),
    ('f.bridge("即学即练 · 公园万圣节小题。")',
     'f.bridge("さあ練習 · パークのハロウィーン小問題。")'),
    ('f.ex("A2", "完成句子", "nocturne", "周六 7 日是最后夜场"',
     'f.ex("A2", "完成句子", "nocturne", "土曜7日が最終ナイトイベント"'),
    ('f.ex("B1", "完成句子", "badge", "敏感儿童有免费驱怪徽章"',
     'f.ex("B1", "完成句子", "badge", "敏感なお子さまには無料の怪物よけバッジ"'),
    ('f.ex("A2", "完成句子", "Plailly", "阿斯泰里克斯公园在 Plailly"',
     'f.ex("A2", "完成句子", "Plailly", "アステリックス・パークは Plailly にある"'),
    ('f.ex("B1", "单选", "B", "Peur sur le Parc 10 月 3 日至 11 月 8 日"',
     'f.ex("B1", "单选", "B", "Peur sur le Parc は10月3日から11月8日まで"'),
    ('f.ex("B1", "完成句子", "couleurs", "恐惧等级用颜色区分"',
     'f.ex("B1", "完成句子", "couleurs", "怖さのレベルは色で区別"'),
    ('f.ex("A2", "完成句子", "19 heures", "夜场从 19 点到凌晨 1 点"',
     'f.ex("A2", "完成句子", "19 heures", "ナイトイベントは19時から深夜1時まで"'),
    ('p.text(ix + 22, by3 + 40, "LES MOTS DES FÊTES · 节日词表", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, by3 + 40, "LES MOTS DES FÊTES · 祭りの単語", 23, "sans", True, OLIVE)'),
    ('"un saint — 圣人"', '"un saint — 聖人"'),
    ('"un cimetière — 墓园"', '"un cimetière — 墓地"'),
    ('"une tombe — 坟墓"', '"une tombe — 墓"'),
    ('"un jour férié — 公共假日"', '"un jour férié — 祝日"'),
    ('"se souvenir — 纪念、想起"', '"se souvenir — 記念する、思い出す"'),
    ('"un déguisement — 变装服装"', '"un déguisement — 仮装衣装"'),
    ('"une citrouille — 南瓜"', '"une citrouille — かぼちゃ"'),
    ('"un bonbon — 糖果"', '"un bonbon — お菓子"'),
    ('"un fantôme — 幽灵"', '"un fantôme — 幽霊"'),
    ('"un sort — 魔法、诅咒"', '"un sort — 魔法、呪い"'),
    ('"10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。"',
     '"10月3日から11月8日まで、12回のナイトイベント。最終は11月7日。昼間は10時から19時まで開園。"'),
    ('p.text(ix + 22, dy3 + 40, "DATES À RETENIR · 本周日历", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, dy3 + 40, "DATES À RETENIR · 今週のカレンダー", 23, "sans", True, OLIVE)'),
    ('"注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。"',
     '"注意：ディエップのホタテ祭りは11月14〜15日で、今週ではありません。"'),
    ('p.band("SPORT · 体育", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")',
     'p.band("SPORT · スポーツ", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")'),
    ('f.gloss("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。")',
     'f.gloss("un tournoi 大会、トーナメント · sur dur ハードコート · en salle 室内 · un tableau principal 本戦の組み合わせ表 · le tenant du titre 前回優勝者 · basculer 逆転する、傾く · les tribunes 観客席。")'),
    ('f.bridge("读第 4 版文章，选出正确答案。")',
     'f.bridge("4ページの記事を読んで正解を選びましょう。")'),
    ('f.ex("B1", "单选", "B", "决赛在周日 8 日"',
     'f.ex("B1", "单选", "B", "決勝は日曜8日"'),
    ('f.ex("B1", "单选", "A", "大师赛在室内硬地球场举行"',
     'f.ex("B1", "单选", "A", "マスターズは室内ハードコートで行われる"'),
    ('f.ex("B1", "单选", "C", "2025 年卫冕冠军是辛纳"',
     'f.ex("B1", "单选", "C", "2025年の前回優勝者はシナー"'),
    ('f.ex("B1", "单选", "B", "法甲第十轮大场面：朗斯–马赛"',
     'f.ex("B1", "单选", "B", "リーグ・アン第10節の目玉：ランス対マルセイユ"'),
    ('f.ex("B1", "单选", "A", "周日 8 日还有轮椅单打决赛（中午）"',
     'f.ex("B1", "单选", "A", "日曜8日には車いすシングルス決勝もある（正午）"'),
    ('f.bridge("把网球词和释义配对。")',
     'f.bridge("テニスの単語と意味を結びましょう。")'),
    ('["tournoi=赛事 a", "raquette=球拍 b", "tribunes=看台 c", "tenant=卫冕者 d"]',
     '["tournoi=大会 a", "raquette=ラケット b", "tribunes=観客席 c", "tenant=前回優勝者 d"]'),
    ('instr="配对"', 'instr="組み合わせ"'),
    ('f.bridge("用比较级完成句子（plus / moins）。")',
     'f.bridge("比較級で文を完成させましょう（plus / moins）。")'),
    ('f.ex("B1", "完成句子", "plus vite", "室内球速更快"',
     'f.ex("B1", "完成句子", "plus vite", "室内では球速が速い"'),
    ('f.ex("B1", "完成句子", "plus grand", "大师赛是仅次于大满贯的级别"',
     'f.ex("B1", "完成句子", "plus grand", "マスターズはグランドスラムに次ぐ大会"'),
    ('f.ex("B1", "完成句子", "moins longue", "室内赛季比室外短"',
     'f.ex("B1", "完成句子", "moins longue", "室内シーズンは屋外より短い"'),
    ('f.bridge("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。")',
     'f.bridge("解説 — un choc 強豪同士の対決 · recevoir 迎える、もてなす · familier おなじみの。")'),
    ('("« Allez ! » — 加油！ · « Quelle action ! » — 好球！"',
     '("« Allez ! » — がんばれ！ · « Quelle action ! » — すごいプレー！"'),
    ('("« Il marque ! » — 他得分了！ · « C\'est gagné ! » — 赢了！"',
     '("« Il marque ! » — 決めた！ · « C\'est gagné ! » — 勝った！"'),
    ('("« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！"',
     '("« Quel point ! » — すごいポイント！（テニス） · « Balle de match ! » — マッチポイント！"'),
    ('p.text(ix + 22, vy + 40, "LES MOTS DU TENNIS · 网球词表", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, vy + 40, "LES MOTS DU TENNIS · テニス用語", 23, "sans", True, OLIVE)'),
    ('"le tennis — 网球"', '"le tennis — テニス"'),
    ('"une balle — 球"', '"une balle — ボール"'),
    ('"un set — 一盘"', '"un set — 1セット"'),
    ('"un match — 比赛"', '"un match — 試合"'),
    ('"un point — 一分"', '"un point — 1ポイント"'),
    ('"la finale — 决赛"', '"la finale — 決勝"'),
    ('"un adversaire — 对手"', '"un adversaire — 対戦相手"'),
    ('"un titre — 冠军头衔"', '"un titre — タイトル"'),
    ('p.text(ix + 22, sy4 + 40, "À SUIVRE · 拭目以待", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, sy4 + 40, "À SUIVRE · 続報に注目", 23, "sans", True, OLIVE)'),
    ('mf.head("MICRO-DRILLS · 即学即练", 24)', 'mf.head("MICRO-DRILLS · ミニ練習", 24)'),
    ('mf.bridge("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。")',
     'mf.bridge("finale / quarts / demi-finales / tableau / fauteuil / choc で穴埋めしましょう。")'),
    ('mf.ex("B1", "完成句子", "quarts", "四分之一决赛在周五"',
     'mf.ex("B1", "完成句子", "quarts", "準々決勝は金曜日"'),
    ('mf.ex("B1", "完成句子", "demi-finales", "半决赛在周六"',
     'mf.ex("B1", "完成句子", "demi-finales", "準決勝は土曜日"'),
    ('mf.ex("B1", "完成句子", "finale", "单打决赛在周日"',
     'mf.ex("B1", "完成句子", "finale", "シングルス決勝は日曜日"'),
    ('mf.ex("B1", "完成句子", "tableau", "正赛签表从周一开始"',
     'mf.ex("B1", "完成句子", "tableau", "本戦の組み合わせ表は月曜日から"'),
    ('mf.ex("B1", "完成句子", "fauteuil", "轮椅赛事周五至周日"',
     'mf.ex("B1", "完成句子", "fauteuil", "車いすの大会は金曜から日曜まで"'),
    ('mf.ex("A2", "完成句子", "choc", "朗斯–马赛是周末焦点战"',
     'mf.ex("A2", "完成句子", "choc", "ランス対マルセイユは週末の目玉試合"'),
    ('p.text(ix + 22, db4 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, db4 + 40, "LE DÉBAT · 討論", 23, "sans", True, OLIVE)'),
    ('"事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。"',
     '"決勝進出者が事前に分からないのは、もっとわくわくしますか、それともがっかりしますか。賛成2文、反対2文を書きましょう。"'),
    ('instr="改写"', 'instr="書きかえ"', 3),
])

# ---------------- content56: P5 + P6 ------------------------------------
apply_file("content56.py", [
    ('# ================= P5 · 青年 (B1) =================',
     '# ================= P5 · youth (B1) ================='),
    ('# ================= P6 · 时事 (B2) =================',
     '# ================= P6 · current affairs (B2) ================='),
    ('p.band("JEUNESSE & MUSIQUE · 青年", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 音乐节")',
     'p.band("JEUNESSE & MUSIQUE · 若者と音楽", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 音楽祭")'),
    ('f.gloss("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。")',
     'f.gloss("un lieu 場所、会場 · une affiche ポスター · les paroles 歌詞 · donner le ton 雰囲気を決める · se promener 散歩する、ぶらつく · pile ちょうど、ぴったり。")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · さあ練習", 25)'),
    ('f.bridge("读第 5 版文章，选出正确答案。")',
     'f.bridge("5ページの記事を読んで正解を選びましょう。")'),
    ('f.ex("B1", "单选", "B", "音乐节 11 月 2–8 日，整整一周"',
     'f.ex("B1", "单选", "B", "音楽祭は11月2〜8日、まる1週間"'),
    ('f.ex("B1", "单选", "A", "15 届音乐节"',
     'f.ex("B1", "单选", "A", "第15回の音楽祭"'),
    ('f.ex("B1", "单选", "C", "Avant-Garde 在巴士底各场地，周四至周六"',
     'f.ex("B1", "单选", "C", "Avant-Garde はバスティーユの各会場で木曜から土曜まで"'),
    ('f.ex("B1", "单选", "B", "俱乐部之夜在周五、周六"',
     'f.ex("B1", "单选", "B", "クラブナイトは金曜と土曜"'),
    ('f.ex("B1", "单选", "A", "开幕夜：Headache、Iceage、DIIV"',
     'f.ex("B1", "单选", "A", "開幕の夜：Headache、Iceage、DIIV"'),
    ('f.bridge("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。")',
     'f.bridge("lieux / paroles / affiche / ambiance / danse / découvre で穴埋めしましょう。")'),
    ('f.ex("B1", "完成句子", "lieux", "10 个场地"',
     'f.ex("B1", "完成句子", "lieux", "10の会場"'),
    ('f.ex("B1", "完成句子", "paroles", "歌词也是法语学习材料"',
     'f.ex("B1", "完成句子", "paroles", "歌詞もフランス語の学習材料"'),
    ('f.ex("B1", "完成句子", "affiche", "海报上写着演出信息"',
     'f.ex("B1", "完成句子", "affiche", "ポスターには出演情報が書いてある"'),
    ('f.ex("B1", "完成句子", "ambiance", "每晚气氛各不相同"',
     'f.ex("B1", "完成句子", "ambiance", "毎晩雰囲気が違う"'),
    ('f.ex("B1", "完成句子", "danse", "音乐节上人们跳舞"',
     'f.ex("B1", "完成句子", "danse", "音楽祭では人々が踊る"'),
    ('f.ex("A2", "完成句子", "découvre", "发现不认识的乐队"',
     'f.ex("A2", "完成句子", "découvre", "知らないバンドを見つける"'),
    ('f.bridge("把音乐词和释义配对。")',
     'f.bridge("音楽の単語と意味を結びましょう。")'),
    ('["concert=音乐会 a", "scène=舞台 b", "groupe=乐队 c", "billet=门票 d"]',
     '["concert=コンサート a", "scène=舞台 b", "groupe=バンド c", "billet=チケット d"]'),
    ('instr="配对"', 'instr="組み合わせ"', 2),
    ('f.bridge("补全对话（音乐节门口）。")',
     'f.bridge("会話を完成させましょう（音楽祭の入り口で）。")'),
    ('f.ex("B1", "完成句子", "ce soir", "今晚演出的乐队"',
     'f.ex("B1", "完成句子", "ce soir", "今夜出演するバンド"'),
    ('f.ex("B1", "完成句子", "deux places", "买两张票"',
     'f.ex("B1", "完成句子", "deux places", "2枚のチケットを買う"'),
    ('p.text(ix + 22, qy5 + 40, "MOTS DE LA MUSIQUE · 音乐词表", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, qy5 + 40, "MOTS DE LA MUSIQUE · 音楽用語", 23, "sans", True, OLIVE)'),
    ('"un festival — 音乐节"', '"un festival — 音楽祭"'),
    ('"un concert — 音乐会"', '"un concert — コンサート"'),
    ('"une chanson — 歌曲"', '"une chanson — 歌"'),
    ('"un chanteur — 歌手"', '"un chanteur — 歌手"'),
    ('"danser — 跳舞"', '"danser — 踊る"'),
    ('"écouter — 聆听"', '"écouter — 聴く"'),
    ('"une salle — 演出厅"', '"une salle — ホール"'),
    ('"le public — 观众"', '"le public — 観客"'),
    ('p.text(ix + 22, dy5 + 40, "PARIS CREATOR WEEK · 创作者周", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, dy5 + 40, "PARIS CREATOR WEEK · クリエイター週間", 23, "sans", True, OLIVE)'),
    ('"11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。"',
     '"11月4〜5日ラ・ヴィレット：クリエイター週間。オンラインのクリエイターと観客が直接会います。"'),
    ('p.text(ix + 22, ty5 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, ty5 + 40, "LE DÉBAT · 討論", 23, "sans", True, OLIVE)'),
    ('"十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？"',
     '"10の会場での音楽祭は、1つの大きな会場よりよいでしょうか。フランス語を学ぶためにどんな音楽を聴きますか。"'),
    ('p.band("POLITIQUE & CHIFFRES · 时事", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 预算周")',
     'p.band("POLITIQUE & CHIFFRES · 時事と数字", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 予算週間")'),
    ('f.gloss("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l\'unanimité 一致通过/否决 · un amendement 修正案。")',
     'f.gloss("un budget 予算 · une mission （予算の）項目 · un député 国民議会議員 · rejeter 否決する · à l\'unanimité 全会一致で · un amendement 修正案。")'),
    ('p.text(chx + 22, chy + 40, "LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）", 24, "sans", True, OLIVE)',
     'p.text(chx + 22, chy + 40, "LE CALENDRIER PRÉVU · 予定の投票日程（結果は未定）", 24, "sans", True, OLIVE)'),
    ('"本页日程为计划安排，结果尚未产生，下期跟进。"',
     '"このページの日程は予定であり、結果はまだ出ていません。次号で追います。"'),
    ('e6.head("LIRE LE CALENDRIER · 读日程", 25)', 'e6.head("LIRE LE CALENDRIER · 日程を読む", 25)'),
    ('e6.bridge("读上图日程，选出正确答案。")',
     'e6.bridge("上の日程を読んで正解を選びましょう。")'),
    ('e6.ex("B2", "图表读数", "B", "周二 3 日：文化与媒体"',
     'e6.ex("B2", "图表读数", "B", "火曜3日：文化とメディア"'),
    ('e6.ex("B2", "图表读数", "A", "周三 4 日：农业"',
     'e6.ex("B2", "图表读数", "A", "水曜4日：農業"'),
    ('e6.ex("B2", "图表读数", "C", "周四 5 日：国土协调与科研"',
     'e6.ex("B2", "图表读数", "C", "木曜5日：国土整備と研究"'),
    ('e6.ex("B2", "图表读数", "A", "周五 6 日：公共财政与经济"',
     'e6.ex("B2", "图表读数", "A", "金曜6日：公共財政と経済"'),
    ('e6.ex("B1", "图表读数", "B", "10 月 23 日社保预算收入被 115–1 否决"',
     'e6.ex("B1", "图表读数", "B", "10月23日に社会保障予算の歳入が115対1で否決"'),
    ('e6.ex("B1", "图表读数", "C", "参议院从 11 月 9 日起审议"',
     'e6.ex("B1", "图表读数", "C", "上院は11月9日から審議"'),
    ('e6.head("LES MOTS · 词汇", 25)', 'e6.head("LES MOTS · 単語", 25)'),
    ('["député=议员 a", "rejeter=否决 b", "vote=投票 c", "amendement=修正案 d"]',
     '["député=国民議会議員 a", "rejeter=否決する b", "vote=投票 c", "amendement=修正案 d"]'),
    ('("« Le texte part au Sénat. » — 法案送交参议院。"',
     '("« Le texte part au Sénat. » — 法案は上院へ送られます。"'),
    ('("« Ce calendrier peut encore bouger. » — 日程仍可能变动。"',
     '("« Ce calendrier peut encore bouger. » — 日程はまだ変わる可能性があります。"'),
    ('("« Les résultats ne sont pas connus. » — 结果尚未揭晓。"',
     '("« Les résultats ne sont pas connus. » — 結果はまだ分かっていません。"'),
    ('g.bridge("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。")',
     'g.bridge("解説 — prévu 予定された、計画された · réaliser 実現する、成し遂げる · distinguer 区別する。")'),
    ('g2.bridge("用比较级完成句子。")',
     'g2.bridge("比較級で文を完成させましょう。")'),
    ('g2.ex("B1", "完成句子", "plus long", "预算辩论比一场音乐会长"',
     'g2.ex("B1", "完成句子", "plus long", "予算の議論はコンサートより長い"'),
    ('g2.ex("B2", "完成句子", "moins simple", "预算比时间表复杂"',
     'g2.ex("B2", "完成句子", "moins simple", "予算は日程表より複雑"'),
    ('g2.ex("B2", "完成句子", "aussi important", "文化预算与农业预算同样重要"',
     'g2.ex("B2", "完成句子", "aussi important", "文化予算と農業予算は同じくらい重要"'),
    ('g2.head("MICRO-DRILLS · 即学即练", 25)', 'g2.head("MICRO-DRILLS · ミニ練習", 25)'),
    ('g2.bridge("用 examine / ont rejeté / part / peut / connus 填空。")',
     'g2.bridge("examine / ont rejeté / part / peut / connus で穴埋めしましょう。")'),
    ('g2.ex("B2", "完成句子", "examine", "国民议会审议预算"',
     'g2.ex("B2", "完成句子", "examine", "国民議会が予算を審議する"'),
    ('g2.ex("B2", "完成句子", "ont rejeté", "议员们否决收入部分"',
     'g2.ex("B2", "完成句子", "ont rejeté", "議員たちが歳入部分を否決した"'),
    ('g2.ex("B2", "完成句子", "part", "法案送交参议院"',
     'g2.ex("B2", "完成句子", "part", "法案は上院へ送られる"'),
    ('g2.ex("B1", "完成句子", "peut", "日程仍可能变动"',
     'g2.ex("B1", "完成句子", "peut", "日程はまだ変わる可能性がある"'),
    ('g2.ex("B1", "完成句子", "connus", "结果尚未揭晓"',
     'g2.ex("B1", "完成句子", "connus", "結果はまだ分かっていない"'),
    ('g2.head("LE DÉBAT · 讨论", 25)', 'g2.head("LE DÉBAT · 討論", 25)'),
    ('g2.bridge("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。")',
     'g2.bridge("議論｜結果が出ていないとき、日程を先に公表すべきでしょうか。prévu（予定）と décidé（決定済み）を区別しましょう。")'),
])

# ---------------- content7: P7 ------------------------------------------
apply_file("content7.py", [
    ('p.band("LANGUE EN MAIN · 精讲", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 本周金句")',
     'p.band("LANGUE EN MAIN · ことばの精講", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 今週のフレーズ")'),
    ('cA.head("NIVEAU A2 · 基础", 27)', 'cA.head("NIVEAU A2 · 基礎", 27)'),
    ('cB.head("NIVEAU B1 · 进阶", 27)', 'cB.head("NIVEAU B1 · 中級", 27)'),
    ('cC.head("NIVEAU B2 · 挑战", 27)', 'cC.head("NIVEAU B2 · 上級", 27)'),
    ('cD.head("BOÎTE À OUTILS · 工具箱", 27)', 'cD.head("BOÎTE À OUTILS · ツールボックス", 27)'),
    ('cD.bridge("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。")',
     'cD.bridge("ツールボックス｜今号の3文はレベル別に1文ずつ。フレーズはすべて今号の記事からの引用で、原文を読み返すのが一番効果的です。")'),
    ('p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", 27, "sans", True, OLIVE)',
     'p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 今週のフレーズ（すべて今号の記事から）", 27, "sans", True, OLIVE)'),
    ('p.text(RIGHT, py + 26, "每句一个语法点 + 一道小题 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")',
     'p.text(RIGHT, py + 26, "各フレーズに文法ポイント + 小問題 · 答えは8ページ", 20, "sans", False, GREY, anchor="end")'),
    ('"语法点｜reprendre：复课、重新开始（pause 后）。"',
     '"文法｜reprendre：再開すること（pause の後）。"'),
    ('"语法点｜ne...pas encore：尚未、还不。"',
     '"文法｜ne...pas encore：まだ〜していない。"'),
    ('"语法点｜passé composé 代动词：se + être + 过去分词。"',
     '"文法｜passé composé の代名動詞：se + être + 過去分詞。"'),
    ('"语法点｜comparatif：plus + 形容词，ou 对举。"',
     '"文法｜comparatif：plus + 形容詞、ou による対比。"'),
    ('"语法点｜se promener：代动词，漫步、穿梭。"',
     '"文法｜se promener：代名動詞、散歩する、ぶらつく。"'),
    ('"语法点｜pouvoir + 动词原形：可能、可以。"',
     '"文法｜pouvoir + 不定詞：〜できる、〜かもしれない。"'),
    ('"语法点｜se jouer：决出胜负、上演（代动词）。"',
     '"文法｜se jouer：決まる、行われる（代名動詞）。"'),
    ('"语法点｜rencontrer：与观众见面；y 代指地点。"',
     '"文法｜rencontrer：観客と会う；y は場所を指す。"'),
    ('"pas encore 尚未"', '"pas encore まだ〜ない"'),
    ('"plus + 形容词"', '"plus + 形容詞"'),
    ('cf.head("CLINIQUE DES ERREURS · 易错诊所", 25)',
     'cf.head("CLINIQUE DES ERREURS · 間違い", 25)'),
    ('cf.bridge("每句有一处错误：找出来并改正。")',
     'cf.bridge("各文に誤りが1つあります。見つけて直しましょう。")'),
    ('"jamais + de：否定句中 des 变 de"',
     '"jamais + de：否定文では des が de になる"'),
    ('"主谓一致：créateurs 复数 → rencontrent，不是 rencontre"',
     '"主語と動詞の一致：créateurs は複数形 → rencontrent、rencontre ではない"'),
    ('"虚拟式：il examine，不加 s"',
     '"接続法：il examine、s はつけない"'),
    ('"事实：决赛在 8 日，不是 7 日"',
     '"事実：決勝は8日、7日ではない"'),
    ('instr="改错"', 'instr="誤り直し"', 4),
    ('p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 读者园地", 24, "sans", True, OLIVE)',
     'p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 読者の広場", 24, "sans", True, OLIVE)'),
    ('"小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。"',
     '"小墨のコメント｜編集部の例文：週末の出来事を passé composé で語るのが安定し、セミコロンで2日をつなぐ書き方も見習えます。手紙も、今号の作文の力作も、VOL.4へ送ってください！"'),
    ('"编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。"',
     '"編集部より：印刷時点で手紙も VOL.2 の作文投稿も届かず（W44号は未発行）、今号は例文を明記して掲載。VOL.4で実際の投稿を講評します。"'),
    ('p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 下周预告", 24, "sans", True, "#f3edda")',
     'p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 次号予告", 24, "sans", True, "#f3edda")'),
    ('"下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！"',
     '"来週は、上院での社会保障予算の審議、11月11日の休戦記念日、ディエップのホタテ祭り。そして皆さんからのお便りも！"'),
])

# ---------------- content8: P8 ------------------------------------------
apply_file("content8.py", [
    ('p.band("EXERCICES & RÉPONSES · 练习与答案", "Le Lucerna", "综合评估 ÉVALUATION · 答案在本版下方")',
     'p.band("EXERCICES & RÉPONSES · 練習と答え", "Le Lucerna", "総合テスト ÉVALUATION · 答えはこのページの下にあります")'),
    ('("A2", "C", "11 月 8 日 2026 是星期日")',
     '("A2", "C", "2026年11月8日は日曜日")'),
    ('("A2", "A", "去南泰尔看决赛")',
     '("A2", "A", "ナンテールへ決勝を見に行く")'),
    ('("A2", "B", "决赛选手周六晚才揭晓")',
     '("A2", "B", "決勝進出者は土曜夜に判明")'),
    ('("A2", "B", "品尝语境（un régal）→ goûté")',
     '("A2", "B", "試食の文脈（un régal）→ goûté")'),
    ('("B1", "C", "se promener 漫步")',
     '("B1", "C", "se promener 散歩する")'),
    ('("B1", "A", "avoir + 过去分词 goûté（不配合）")',
     '("B1", "A", "avoir + 過去分詞 goûté（一致なし）")'),
    ('("B1", "C", "les finales 主语复数 → ont lieu")',
     '("B1", "C", "les finales は複数主語 → ont lieu")'),
    ('("A2", "A", "elle écrit 她写")',
     '("A2", "A", "elle écrit 彼女は書く")'),
    ('bf.head("A · TEXTE À TROUS · 完形填空", 24)', 'bf.head("A · TEXTE À TROUS · 穴埋め", 24)'),
    ('bf.bridge("选项：")', 'bf.bridge("選択肢：")'),
    ('bf.head("B · CHOIX MULTIPLE · 单选", 24)', 'bf.head("B · CHOIX MULTIPLE · 選択問題", 24)'),
    ('("A2", "B", "7 nov. = samedi（最后夜场）"',
     '("A2", "B", "7 nov. = samedi（最終ナイトイベント）"'),
    ('("B1", "B", "s\'intéresser aux（à+les）"',
     '("B1", "B", "s\'intéresser aux (à + les)"'),
    ('("B2", "B", "si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j\' 是 je 在元音前的省音"',
     '("B2", "B", "si + imparfait → conditionnel présent；j\' は母音の前での je のエリジオン"'),
    ('("B2", "A", "主语 ce programme 三单 → semble"',
     '("B2", "A", "主語 ce programme は三人称単数 → semble"'),
    ('("B1", "B", "将来时 aura lieu（决赛在周日）"',
     '("B1", "B", "将来時 aura lieu（決勝は日曜日）"'),
    # NOTE: core text is 将来时 (simplified form); the line above uses it.
    ('("A2", "A", "三区同日复课"',
     '("A2", "A", "3つの学区が同じ月曜日に再開"'),
    ('("B1", "C", "扇贝节在 11 月 7–8 日"',
     '("B1", "C", "ホタテ祭りは11月7〜8日"'),
    ('bf.head("C · LECTURE · 阅读理解", 24)', 'bf.head("C · LECTURE · 読解", 24)'),
    ('("A2", "C", "夜场 19 点至凌晨 1 点"',
     '("A2", "C", "ナイトイベントは19時から深夜1時まで"'),
    ('("A2", "A", "小徽章给小 Léo 驱怪"',
     '("A2", "A", "小さなバッジは小さな Léo の怪物よけ"'),
    ('("B1", "B", "周日先看决赛再吃扇贝"',
     '("B1", "B", "日曜はまず決勝を見てからホタテを味わう"'),
    ('("B1", "A", "周日晚上早睡因为周一上学"',
     '("B1", "A", "日曜夜に早く寝るのは月曜が学校だから"'),
    ('("B2", "A", "周一是上学日（复课后正常周一）"',
     '("B2", "A", "月曜は登校日（再開後の通常の月曜日）"'),
    ('bf.head("D · PHRASES · 完成句子与转换", 24)', 'bf.head("D · PHRASES · 文の完成と変換", 24)'),
    ('"aller + 原形（futur proche）"', '"aller + 不定詞（futur proche）"'),
    ('"si + 半过去时 venais"', '"si + 半過去 venais"'),
    ('"passé composé : a + 过去分词"', '"passé composé : a + 過去分詞"'),
    ('"selon moi = 在我看来"', '"selon moi = 私の意見では"'),
    ('"il est prévu que + 虚拟式"', '"il est prévu que + 接続法"'),
    ('bf.head("E · TRADUCTION · 翻译", 24)', 'bf.head("E · TRADUCTION · 翻訳", 24)'),
    ('("B2", "读一份日程，本身就是在了解法国。", "lire un programme = 读日程"',
     '("B2", "日程表を読むことは、それ自体がフランスを理解することです。", "lire un programme = 日程表を読む"'),
    ('"Traduisez : « Lire un programme, c\'est déjà comprendre la France. »"',
     '"日本語に訳しなさい：« Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"比较级 plus vite + court"', '"比較級 plus vite + court"'),
    ('"Traduisez : 他跑得比他哥哥更快。"',
     '"フランス語に訳しなさい：彼は兄より速く走ります。"'),
    ('"Traduisez : 学生们自 10 月 17 日起就在放假。"',
     '"フランス語に訳しなさい：生徒たちは10月17日から休みです。"'),
    ('"Traduisez : 今晚，我们要准备书包。"',
     '"フランス語に訳しなさい：今夜、私たちはかばんを準備します。"'),
    ('"ne...pas encore = 尚未"', '"ne...pas encore = まだ〜ない"'),
    ('"Traduisez : 人们尚不知道决赛选手是谁。"',
     '"フランス語に訳しなさい：決勝進出者が誰なのか、まだ誰も知りません。"'),
    ('bf.head("F · LES MOTS · 词汇配对", 24)', 'bf.head("F · LES MOTS · 語の対応", 24)'),
    ('["tournoi=赛事 a", "nocturne=夜场 b", "budget=预算 c", "coquille=扇贝 d", "festival=音乐节 e"]',
     '["tournoi=大会 a", "nocturne=夜のイベント b", "budget=予算 c", "coquille=ホタテ d", "festival=音楽祭 e"]'),
    ('instr="配对"', 'instr="組み合わせ"'),
    ('("A2", "samedi", "11 月 7 日是星期六")',
     '("A2", "samedi", "11月7日は土曜日")'),
    ('("A2", "coquilles (des coquilles Saint-Jacques)", "在市场买扇贝")',
     '("A2", "coquilles (des coquilles Saint-Jacques)", "市場でホタテを買う")'),
    ('("B1", "goûter", "goûter 品尝（原形）")',
     '("B1", "goûter", "goûter 味わう（不定詞）")'),
    ('("A2", "recette", "à la portaise 是一种做法")',
     '("A2", "recette", "à la portaise は調理法の一つ")'),
    ('("A2", "week-end", "Bon week-end ! 周末愉快")',
     '("A2", "week-end", "Bon week-end ! よい週末を")'),
    ('bf.head("G · DIALOGUE · 对话补全", 24)', 'bf.head("G · DIALOGUE · 会話の穴埋め", 24)'),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "写作", "自由記述 — ポイントは作文欄に、範文はこのページの作文欄の中にあります", "ポイントで採点")'),
    ('p.text(wx, wy + 26, "H · ÉCRITURE · 写作", 25, "sans", True, OLIVE)',
     'p.text(wx, wy + 26, "H · ÉCRITURE · 作文", 25, "sans", True, OLIVE)'),
    ('"用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。"',
     '"フランス語で80〜100語で書きましょう：11月7〜8日の私の週末。試合1つ、祭り1つ、料理1つを書きましょう。"'),
    ('p.text(mx2 + 22, wy + 38, "MODÈLE · 范文", 23, "sans", True, OLIVE)',
     'p.text(mx2 + 22, wy + 38, "MODÈLE · 範文", 23, "sans", True, OLIVE)'),
    ('p.text(MX, ky + 26, "RÉPONSES · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)',
     'p.text(MX, ky + 26, "RÉPONSES · 全解答と解説（1–8ページ）", 26, "sans", True, OLIVE)'),
    ('kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
     'kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)'),
    ('s += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"'),
    ('if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):',
     'if e["note"] and e["n"] in PRINT_NOTES:'),
])

if _SECTION[0] == ROUND:
    # Insert the explicit PRINT_NOTES set into content8 (before keys).
    path = os.path.join(HERE, "content8.py")
    text = open(path, encoding="utf-8").read()
    marker = "# ---- keys ----"
    assert text.count(marker) == 1
    block = ("# Explicit printed-note set: the core's noted set (tools/p8.py\n"
             "# extract, 97/150). Japanese notes are longer than the core's\n"
             "# <=10-char rule, so the length rule is replaced by this set.\n"
             "PRINT_NOTES = " + repr(PRINT_NOTES) + "\n\n")
    text = text.replace(marker, block + marker)
    open(path, "w", encoding="utf-8").write(text)
    print("content8.py: PRINT_NOTES block inserted")

section(2)
# ---------------- Round 2: occlusion-audit fixes (6 NEW flags) ---------
# P1 agenda note overran its box by 4px (single-line p.text): shorten.
apply_file("content12.py", [
    ('"週末の決勝の結果は土曜夜と日曜に判明します。"',
     '"決勝の結果は土曜夜と日曜に判明。"'),
    # P2 ET VOUS Japanese prompt wrapped to 4 lines, pushing the col-3 box
    # over the date-section rule and title: 38-char 2-line form.
    ('"月曜の始まりについて話しましょう。月曜の朝どこにいましたか。休みにどの本を読みましたか。フランス語で2文書いて編集部へ送ってください。"',
     '"月曜の朝どこにいましたか。休みに読んだ本は。フランス語で2文送ってください。"', 2),
])
# P5 Creator Week box title overran its box (ink 1927 > border 1885):
# bare festival name, the FR x EN shipped form.
apply_file("content56.py", [
    ('p.text(ix + 22, dy5 + 40, "PARIS CREATOR WEEK · クリエイター週間", 23, "sans", True, OLIVE)',
     'p.text(ix + 22, dy5 + 40, "PARIS CREATOR WEEK", 23, "sans", True, OLIVE)'),
])
# P8 battery overflow (+116px = 4 extra lines): the four JA->FR stems
# wrapped to 2 lines each at size 20. Compact 和訳/仏訳 prefixes bring
# each stem back to 1 line; keys and instruction meaning are unchanged.
apply_file("content8.py", [
    ('"日本語に訳しなさい：« Lire un programme, c\'est déjà comprendre la France. »"',
     '"和訳：« Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"フランス語に訳しなさい：彼は兄より速く走ります。"',
     '"仏訳：彼は兄より速く走ります。"'),
    ('"フランス語に訳しなさい：生徒たちは10月17日から休みです。"',
     '"仏訳：生徒たちは10月17日から休みです。"'),
    ('"フランス語に訳しなさい：今夜、私たちはかばんを準備します。"',
     '"仏訳：今夜、私たちはかばんを準備します。"'),
    ('"フランス語に訳しなさい：決勝進出者が誰なのか、まだ誰も知りません。"',
     '"仏訳：決勝進出者はまだ誰も知らない。"'),
])

section(3)
# ---------------- Round 3: line-start small-kana fix --------------------
# P7 clinic bridge wrapped with "ましょう" split as "まし | ょう。"
# (small kana stranded at a line start -- JA column defect class).
# Reword to a 19-char single-line form; meaning unchanged.
apply_file("content7.py", [
    ('cf.bridge("各文に誤りが1つあります。見つけて直しましょう。")',
     'cf.bridge("各文に誤りが1つ。見つけて直しましょう。")'),
])

section(4)
# ---------------- Round 4: word-split + orphan-tail fixes -------------
# P4 comparative bridge split "moins" as "moin | s" (the W43 FR x JA
# defect #1 shape): drop "文を" as in the W43 fix. (P4 lives in
# content34.py; the P6 bridge in content56.py is a different string.)
apply_file("content34.py", [
    ('f.bridge("比較級で文を完成させましょう（plus / moins）。")',
     'f.bridge("比較級で完成させましょう（plus / moins）。")'),
])
# P7 grammar bridges whose final lines stranded one kanji ("対 | 比。",
# "指 | す。"): shorten each to a single line, meaning unchanged.
apply_file("content7.py", [
    ('"文法｜comparatif：plus + 形容詞、ou による対比。"',
     '"文法｜comparatif：plus + 形容詞、ou の対比。"'),
    ('"文法｜rencontrer：観客と会う；y は場所を指す。"',
     '"文法｜rencontrer：観客と会う；y＝場所。"'),
])
# NOTE (repro pass): the P8 #107 note lives in content7.py, NOT
# content8.py -- an earlier draft of this round applied it to
# content8.py and aborted after the P4/P7 applies above. The real
# #107 fix is round 5 (content7.py). This block is intentionally
# absent so rounds 1-7 run clean from a fresh core copy.

section(5)
# ---------------- Round 5: P8 #107 note (lives in content7.py) --------
# The clinic note registered in content7 IS the P8 note for item 107;
# the round-4 apply targeted content8.py by mistake. Same wording fix,
# simulation-verified: "examine" lands whole in the keys flow.
apply_file("content7.py", [
    ('"接続法：il examine、s はつけない"',
     '"接続法：examine、s はつけない"'),
])

section(6)
# ---------------- Round 6: zero-doubt wording --------------------------
# P2 date-head note used "注意：" (a form shared with the core's
# Chinese layer). The word itself is valid Japanese, but switch to
# the unambiguous "注：" so no residual scan can mistake it.
apply_file("content12.py", [
    ('"lundi 2 novembre · 注意：1日は le premier、それ以外は基数詞"',
     '"lundi 2 novembre · 注：1日は le premier、それ以外は基数詞"'),
])

section(7)
# ---------------- Round 7: second 注意： -------------------------------
# Same zero-doubt class as round 6: the P3 DATES box note used
# "注意：" (valid Japanese, but the same shared form). Switch to
# "注：" so no residual scan can mistake either occurrence.
apply_file("content34.py", [
    ('"注意：ディエップのホタテ祭りは11月14〜15日で、今週ではありません。"',
     '"注：ディエップのホタテ祭りは11月14〜15日で、今週ではありません。"'),
])

print(f"transform ROUND={ROUND} done")
